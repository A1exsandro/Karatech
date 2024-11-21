# Karatech Backend

# Criar e ativar ambiente Virtual Linux
* python3 -m venv .venv
* . .venv/bin/activate

# Instalar dependências
* pip install -r requirements.txt

# Alguns Comandos python
* pip freeze > requirements.txt

PYTHONPATH=/home/adriana/workspace/Karatech/backend/api uvicorn main:app
