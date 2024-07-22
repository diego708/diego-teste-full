# diego-teste-full
Desafio DEV


** Instalar o Sistema **

Instalar o Python 
(Utilizado a versão 3.12.3)

Criar o ambiente Virtual
python -m venv plataforma

Entrar na pasta e ativar o ambiente virtual
cd .\plataforma\
.\Scripts\activate

git clone https://github.com/diego708/diego-teste-full.git

Acessar a pasta sistema

Instalar os programas dependentes
pip install .\requirements.txt

Acessar a tela inicial 
python manage.py runserver
http://127.0.0.1:8000/home/


*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

Criar o projeto no GitHub
https://github.com/diego708/diego-teste-full.git

Criação do projeto em Django

django-admin startproject sistema

python manage.py startapp home
python manage.py startapp cadastro
python manage.py startapp projeto
python manage.py startapp relatorio


python manage.py makemigrations cadastro
python manage.py makemigrations projeto
python manage.py migrate

* Requirements

* Testes Unitários

* Diagrama de classe

*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-

