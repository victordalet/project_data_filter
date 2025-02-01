import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from src.struct.stats_manager import StatsManager
from src.view.action import Action


class App:
    def __init__(self):
        self.title: str = "Data Filter"
        self.file_uploader = None
        self.initialize_session_state()

    def initialize_session_state(self):
        """Initialise l'état de la session pour stocker les fichiers uploadés."""
        if "uploaded_files" not in st.session_state:
            st.session_state.uploaded_files = []

    def create_home_component(self):
        """Crée le composant pour uploader des fichiers."""
        self.file_uploader = st.file_uploader(
            "Upload a file",
            type=["csv", "json", "yaml", "xml"],
            accept_multiple_files=True,
        )

    @staticmethod
    def create_table_component(data: pd.DataFrame):
        """Affiche le DataFrame sous forme de tableau."""
        st.write(data)

    @staticmethod
    def display_stat(title: str, value, color: str = "#000000", font_size: int = 20):
        """Affiche une statistique avec un style personnalisé."""
        st.markdown(
            f"**{title}:** <span style='color: {color}; font-size: {font_size}px;'>{value}</span>",
            unsafe_allow_html=True,
        )

        filters = []
        for i in range(num_filters):
            st.sidebar.write(f"### Filter {i + 1}")
            column = st.sidebar.selectbox(
                f"Select column {i + 1}",
                ["name", "quantity", "price", "category"],
                key=f"column_{i}",
            )
            value = st.sidebar.text_input(
                f"Enter filter value {i + 1}", key=f"value_{i}"
            )
            filters.append({"column": column, "value": value})

        if st.sidebar.button("Apply Filters"):
            if st.session_state.uploaded_data is not None:
                data = st.session_state.uploaded_data
                filtered_data = Action.apply_filter(data, filters)
                st.session_state["filtered_data"] = filtered_data
                st.write("### Filtered Data")
                st.write(filtered_data)

    @staticmethod
    def create_pie_chart(labels, values, colors, title):
        """Crée un pie chart pour afficher des proportions."""
        fig, ax = plt.subplots()
        ax.pie(
            values,
            labels=labels,
            autopct="%1.1f%%",
            colors=colors[: len(labels)],
            startangle=90,
            wedgeprops={"edgecolor": "black"},
        )
        ax.set_title(title)
        st.pyplot(fig)

    def create_student_stats_component(self, data: pd.DataFrame):
        """Crée le composant pour afficher les statistiques des étudiants."""
        st.markdown("### Statistiques pour les étudiants")

    @staticmethod
    def create_save_component():
        st.sidebar.header("Save Data")
        file_name = st.sidebar.text_input("Enter file name", "data_output")
        file_format = st.sidebar.selectbox(
            "Select file format", ["csv", "json", "xml", "yaml"]
        )
        if st.sidebar.button("Save Data"):
            if st.session_state.uploaded_data is not None:
                Action.save_data(
                    st.session_state["filtered_data"],
                    f"{file_name}.{file_format}",
                    file_format,
                )

        # Calcul des statistiques
        min_age = StatsManager.min(data, "age")
        max_age = StatsManager.max(data, "age")
        avg_age = StatsManager.average(data, "age")
        boolean_stat = StatsManager.boolean_stats(data, "apprentice")

        # Affichage des statistiques
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Âge des étudiants")
            self.display_stat("Min", min_age, color="#4CAF50")
            self.display_stat("Max", max_age, color="#F44336")
            self.display_stat("Moyenne", round(avg_age, 2), color="#2196F3")

        with col2:
            st.markdown("#### Répartition des apprentis")
            labels = ["Apprenti", "Non apprenti"]
            values = [boolean_stat["true_percentage"], boolean_stat["false_percentage"]]
            colors = ["#4CAF50", "#F44336"]  # Vert pour True, Rouge pour False
            self.create_pie_chart(labels, values, colors, "Répartition des apprentis")

    def create_item_stats_component(self, data: pd.DataFrame):
        """Crée le composant pour afficher les statistiques des articles."""
        st.markdown("### Statistiques pour les articles")

        # Calcul des statistiques
        min_price = StatsManager.min(data, "price")
        max_price = StatsManager.max(data, "price")
        avg_price = StatsManager.average(data, "price")

        # Affichage des statistiques
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Prix des articles")
            self.display_stat("Min", min_price, color="#4CAF50")
            self.display_stat("Max", max_price, color="#F44336")
            self.display_stat("Moyenne", round(avg_price, 2), color="#2196F3")

        with col2:
            st.markdown("#### Répartition des catégories")
            category_distribution = data["category"].value_counts(normalize=True) * 100
            labels = category_distribution.index.tolist()
            values = category_distribution.values.tolist()
            colors = [
                "#4CAF50",
                "#F44336",
                "#2196F3",
                "#FF9800",
            ]  # Couleurs pour les catégories
            self.create_pie_chart(labels, values, colors, "Répartition des catégories")

    def create_stats_component(self, data: pd.DataFrame):
        """Crée le composant pour afficher les statistiques en fonction du type de fichier."""
        if "first_name" in data.columns:  # Fichier de type Student
            self.create_student_stats_component(data)
        elif "name" in data.columns:
            self.create_item_stats_component(data)
        else:
            st.warning("Type de fichier non reconnu.")

    def run(self):
        st.title(self.title)
        self.create_home_component()
        data = Action.check_upload_file(self.file_uploader)
        if data:
            file_type, data = data
            self.create_table_component(data)
            self.create_stats_component(data)


if __name__ == "__main__":
    App().run()
