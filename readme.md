
## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/leandro-matos/django-project.git
cd django-project
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd blog
python manage.py migrate
python manage.py createsuperuser
```

* Acessar localhost:8000
* Acessar localhost:8000/admin para informações de posts, contatos.
