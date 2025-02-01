import pandas as pd
import streamlit as st
from src.view.action import Action


class App:
    file_uploader: st.file_uploader

    def __init__(self):
        self.title: str = "Data Filter"
        if "uploaded_files" not in st.session_state:
            st.session_state.uploaded_files = []
        if "uploaded_data" not in st.session_state:
            st.session_state.uploaded_data = None
        if "filters" not in st.session_state:
            st.session_state.filters = []
        if "filtered_data" not in st.session_state:
            st.session_state.filtered_data = None

    def create_home_component(self):
        st.title(self.title)
        file_uploader = st.file_uploader(
            "Upload a file",
            type=["csv", "json", "yaml", "xml"],
            accept_multiple_files=True,
        )
        self.create_input_filter()
        self.create_sort_component()
        self.create_save_component()
        self.create_download_component()

        # Load data from uploaded file
        data = Action.check_upload_file(file_uploader)
        if data:
            file_type, data = data
            st.session_state.uploaded_data = data
            self.create_table_component(data)

    @staticmethod
    def create_table_component(data: pd.DataFrame):
        st.write("### Uploaded Data")
        st.write(data)

    @staticmethod
    def create_input_filter():
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
                st.write("### Filtered Data")
                st.write(filtered_data)

    @staticmethod
    def create_sort_component():
        st.sidebar.header("Sort")
        sort_column = st.sidebar.selectbox(
            "Select column to sort", ["name", "quantity", "price", "category"]
        )
        sort_order = st.sidebar.radio("Sort order", ["Ascending", "Descending"])
        if st.sidebar.button("Apply Sort"):
            if st.session_state.uploaded_data is not None:
                data = st.session_state.uploaded_data
                sorted_data = Action.sort_data(
                    data, sort_column, sort_order == "Ascending"
                )
                st.write("### Sorted Data")
                st.write(sorted_data)

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
                    st.session_state.uploaded_data,
                    f"{file_name}.{file_format}",
                    file_format,
                )

    @staticmethod
    def create_download_component():
        st.sidebar.header("Download Filtered Data")
        if (
            st.session_state.filtered_data is not None
        ):  # Vérifier si les données filtrées existent
            file_format = st.sidebar.selectbox(
                "Select download format",
                ["csv", "json", "xml", "yaml"],
                key="download_format",
            )
            file_name = st.sidebar.text_input(
                "Enter download file name", "filtered_data", key="download_name"
            )
            if st.sidebar.button("Download Filtered Data"):
                filtered_data = st.session_state.filtered_data
                if file_format == "csv":
                    csv = filtered_data.to_csv(index=False)
                    st.sidebar.download_button(
                        label="Download CSV",
                        data=csv,
                        file_name=f"{file_name}.csv",
                        mime="text/csv",
                    )
                elif file_format == "json":
                    json = filtered_data.to_json(orient="records")
                    st.sidebar.download_button(
                        label="Download JSON",
                        data=json,
                        file_name=f"{file_name}.json",
                        mime="application/json",
                    )
                elif file_format == "xml":
                    xml = filtered_data.to_xml(index=False)
                    st.sidebar.download_button(
                        label="Download XML",
                        data=xml,
                        file_name=f"{file_name}.xml",
                        mime="application/xml",
                    )
                elif file_format == "yaml":
                    yaml = filtered_data.to_yaml()
                    st.sidebar.download_button(
                        label="Download YAML",
                        data=yaml,
                        file_name=f"{file_name}.yaml",
                        mime="application/yaml",
                    )

    def run(self):
        self.create_home_component()


if __name__ == "__main__":
    App().run()
