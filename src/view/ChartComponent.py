from typing import List

import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

from src.struct.stats_manager import StatsManager


class ChartComponent:
    @staticmethod
    def create_stats_component(data: pd.DataFrame):
        ChartComponent.create_column_stats(data)
        if "first_name" in data.columns:
            ChartComponent.create_student_stats_component(data)
        elif "name" in data.columns:
            ChartComponent.create_item_stats_component(data)

    @staticmethod
    def create_column_stats(data: pd.DataFrame):
        col1, col2 = st.columns(2)
        for column in data.columns:
            if pd.api.types.is_bool_dtype(data[column]):
                boolean_stat = StatsManager.boolean_stats(data, column)
                with col2:
                    st.markdown(f"#### {column}")
                    ChartComponent.create_pie_chart(
                        ["True", "False"],
                        [
                            boolean_stat["true_percentage"],
                            boolean_stat["false_percentage"],
                        ],
                        ["#4CAF50", "#F44336"],
                        f"Répartition des valeurs de {column}",
                    )
            elif pd.api.types.is_numeric_dtype(data[column]):
                min_value = StatsManager.min(data, column)
                max_value = StatsManager.max(data, column)
                avg_value = StatsManager.average(data, column)
                with col2:
                    st.markdown(f"#### {column}")
                    ChartComponent.display_stat("Min", min_value, color="#4CAF50")
                    ChartComponent.display_stat("Max", max_value, color="#F44336")
                    ChartComponent.display_stat(
                        "Moyenne", round(avg_value, 2), color="#2196F3"
                    )

            elif pd.api.types.is_list_like(data[column]):
                list_stat = StatsManager.list_stats(data, column)
                with col1:
                    st.markdown(f"#### {column}")
                    ChartComponent.display_stat(
                        "Min Length", list_stat["min_length"], color="#4CAF50"
                    )
                    ChartComponent.display_stat(
                        "Max Length", list_stat["max_length"], color="#F44336"
                    )
                    ChartComponent.display_stat(
                        "Average Length",
                        round(list_stat["average_length"], 2),
                        color="#2196F3",
                    )

    @staticmethod
    def create_student_stats_component(data: pd.DataFrame):
        st.markdown("### Statistiques pour les étudiants")

        data["mean"] = data["grades"].apply(lambda x: sum(x) / len(x))
        ChartComponent.create_bar_chart(
            data["age"].unique().tolist(),
            data.groupby("age")["mean"].mean().tolist(),
            "Moyenne des notes par âge",
            "Âge",
            "Moyenne des notes",
        )
        ChartComponent.create_bar_chart(
            ["Apprenti", "Non apprenti"],
            [
                data[data["apprentice"] == True]["mean"].mean(),
                data[data["apprentice"] == False]["mean"].mean(),
            ],
            "Moyenne des notes par apprentissage",
            "Apprentissage",
            "Moyenne des notes",
        )

    @staticmethod
    def create_item_stats_component(data: pd.DataFrame):
        """Crée le composant pour afficher les statistiques des articles."""
        st.markdown("### Statistiques pour les articles")

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

        ChartComponent.create_bar_chart(
            data["category"].unique().tolist(),
            data.groupby("category")["price"].mean().tolist(),
            "Moyenne des prix par catégorie",
            "Catégorie",
            "Moyenne des prix",
        )

    @staticmethod
    def create_pie_chart(
        labels: List[str], values: List[float], colors: List[str], title: str
    ):
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
    def create_bar_chart(
        labels: List[str], values: List[float], title: str, x_label: str, y_label: str
    ):
        fig, ax = plt.subplots()
        ax.bar(labels, values)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title)
        st.pyplot(fig)

    @staticmethod
    def display_stat(title: str, value, color: str = "#000000", font_size: int = 20):
        st.markdown(
            f"**{title}:** <span style='color: {color}; font-size: {font_size}px;'>{value}</span>",
            unsafe_allow_html=True,
        )
