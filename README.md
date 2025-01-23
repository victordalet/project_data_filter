# project_data_filter

---


## Install package

```bash
pip install -r requirements.txt
```


## Run the project

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
python src/main.py
```


## Run create data

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
python tools/create_random_file.py <extension[csv,yaml,xml,json]> <mode [student,item]>
```