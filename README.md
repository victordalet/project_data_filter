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

### Active chat bot

You need to install lamma and download the model
- `curl -fsSL https://ollama.com/install.sh | sh`
- `ollama run llama3.1:8b`

```
export ACTIVE_CHAT_BOT=True
```

## Run with docker

```bash
docker compose up -d
```


## Run create data

```bash
export PYTHONPATH=$(pwd)/src:$(pwd)
python tools/create_random_file.py <extension[csv,yaml,xml,json]> <mode [student,item]>
```