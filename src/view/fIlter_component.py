from typing import Dict, List, Union

import streamlit as st

from src.struct.structur_def import FilterType
from src.view.chart_component import ChartComponent
from src.view.action import Action


class FilterComponent:
    @staticmethod
    def display_filter_bar():
        st.sidebar.header("Filters")
        num_filters = st.sidebar.number_input(
            "Number of filters", min_value=0, max_value=10, value=0
        )
        filters: List[Dict[str, Union[str, FilterType]]] = []
        for i in range(num_filters):
            st.sidebar.write(f"### Filter {i + 1}")
            filter_type = st.sidebar.selectbox(
                f"Select filter type {i + 1}",
                [f.value for f in FilterType],
                key=f"type_{i}",
            )
            column = st.sidebar.selectbox(
                f"Select column {i + 1}",
                (
                    st.session_state.uploaded_data.columns
                    if "uploaded_data" in st.session_state
                    else []
                ),
                key=f"column_{i}",
            )
            value = st.sidebar.text_input(
                f"Enter filter value {i + 1}", key=f"value_{i}"
            )
            filters.append({"column": column, "value": value, "type": filter_type})

        if "filtered_datasets" not in st.session_state:
            st.session_state["filtered_datasets"] = []

        if st.sidebar.button("Apply Filters"):
            if st.session_state.uploaded_data is not None:
                data = st.session_state.uploaded_data
                filtered_data = Action.apply_filter(data, filters)
                st.session_state["filtered_datasets"].append(filtered_data)
                st.session_state["filtered_data"] = filtered_data
                st.write("### Filtered Data")

                if len(filtered_data) == 0:
                    st.write("No data found.")
                else:
                    st.write(filtered_data)
                    ChartComponent.create_stats_component(filtered_data)

        else:
            if "uploaded_data" in st.session_state:
                data = st.session_state.uploaded_data
                if data is not None:
                    st.write(data)
                    ChartComponent.create_stats_component(data)

        st.sidebar.header("Previous Filtered Data")
        for idx, dataset in enumerate(st.session_state["filtered_datasets"]):
            if st.sidebar.button(f"Show Filtered Data {idx + 1}"):
                st.session_state["filtered_data"] = dataset
                st.write("### Filtered Data")
                st.write(dataset)
                ChartComponent.create_stats_component(dataset)

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
