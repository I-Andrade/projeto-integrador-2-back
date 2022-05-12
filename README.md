# projeto-integrador-2-backend
Projeto Integrador 2 - Univesp - 1º Sem. 2022.

# Dicas para instalação do projeto para rodar local

Criar um ambiente Virtual - Utilizando o PIP, a instalação do VirtualEnv pode ser feita com um simples comando:
python -m venv env

Ativar o ambiente
cd env
cd Scripts
activate.bat

Clonar o repositório
git clone https://github.com/I-Andrade/projeto-integrador-2-backend.git

Entrar na pasta do projeto
cd projeto-integrador-2-backend

Instalar as dependências do projeto:
pip install -r requirements.txt

Faça a primeira Migrate
python manage.py migrate

Crie um SuperUser
python manage.py createsuperuser

Rodar o projeto
python manage.py runserver




