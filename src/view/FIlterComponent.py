import streamlit as st

from src.view.action import Action


class FilterComponent:
    @staticmethod
    def display_filter_bar():
        st.sidebar.header("Filters")
        num_filters = st.sidebar.number_input(
            "Number of filters", min_value=1, max_value=10, value=1
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
