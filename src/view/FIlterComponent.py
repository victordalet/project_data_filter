from typing import Dict, List, Union

import streamlit as st

from src.struct.structur_def import FilterType
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

        if st.sidebar.button("Apply Filters"):
            if st.session_state.uploaded_data is not None:
                data = st.session_state.uploaded_data
                filtered_data = Action.apply_filter(data, filters)
                st.session_state["filtered_data"] = filtered_data
                st.session_state["filter_history"].append(filtered_data)
                st.write("### Filtered Data")
                st.write(filtered_data)

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

    @staticmethod
    def create_table_history_filter():
        for i, f_data in enumerate(st.session_state["filter_history"]):
            if st.button(f"Apply Filter -{i + 1}"):
                st.session_state["filtered_data"] = f_data
                st.write(f_data)
