import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

from src.struct.stats_manager import StatsManager
from src.view.action import Action


class ChartComponent:
    @staticmethod
    def create_stats_component(data: pd.DataFrame):
        if "first_name" in data.columns:  # Fichier de type Student
            ChartComponent.create_student_stats_component(data)
        elif "name" in data.columns:
            ChartComponent.create_item_stats_component(data)
        else:
            st.warning("Type de fichier non reconnu.")

    @staticmethod
    def create_student_stats_component(data: pd.DataFrame):
        st.markdown("### Statistiques pour les étudiants")

        # Calcul des statistiques
        min_age = StatsManager.min(data, "age")

        max_age = StatsManager.max(data, "age")
        avg_age = StatsManager.average(data, "age")
        boolean_stat = StatsManager.boolean_stats(data, "apprentice")

        # Affichage des statistiques
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Âge des étudiants")
            ChartComponent.display_stat("Min", min_age, color="#4CAF50")
            ChartComponent.display_stat("Max", max_age, color="#F44336")
            ChartComponent.display_stat("Moyenne", round(avg_age, 2), color="#2196F3")

        with col2:
            st.markdown("#### Répartition des apprentis")
            labels = ["Apprenti", "Non apprenti"]
            values = [boolean_stat["true_percentage"], boolean_stat["false_percentage"]]
            colors = ["#4CAF50", "#F44336"]  # Vert pour True, Rouge pour False
            ChartComponent.create_pie_chart(
                labels, values, colors, "Répartition des apprentis"
            )

    @staticmethod
    def create_item_stats_component(data: pd.DataFrame):
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
            ChartComponent.display_stat("Min", min_price, color="#4CAF50")
            ChartComponent.display_stat("Max", max_price, color="#F44336")
            ChartComponent.display_stat("Moyenne", round(avg_price, 2), color="#2196F3")

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
            ChartComponent.create_pie_chart(
                labels, values, colors, "Répartition des catégories"
            )

    @staticmethod
    def create_pie_chart(labels, values, colors, title):
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

    @staticmethod
    def display_stat(title: str, value, color: str = "#000000", font_size: int = 20):
        st.markdown(
            f"**{title}:** <span style='color: {color}; font-size: {font_size}px;'>{value}</span>",
            unsafe_allow_html=True,
        )
