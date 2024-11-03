# Action do Django admin com página intermediária

Código usado na apresentação do 75° PUG-PE sobre como criar uma action no django admin com uma página intermediária.
O código é baseado num sistema de eventos e a action serve para disparo de emails para os participantes do(s) evento(s) selecionados.

## Como rodar o projeto local:

1. Clone o repositório e acesse o mesmo pelo terminal.

```console
git clone git@github.com:matheusfs99/django-admin-action-intermediate-page.git
cd django-admin-action-intermediate-page
```

2. Crie um virtualenv

```console
python -m venv .venv
```

3. Ative o virtualenv.

- Unix:

```console
source venv/bin/activate
```

- Windows:

```console
venv/Scripts/activate
```

4. Instale as dependências.

```console
pip install -r requirements.txt
```

5. Configure a instância com o .env

```console
cp .env-example .env
```

6. Execute as migrações e criação do banco de dados sqlite3

```console
python manage.py migrate
```

7. Inicialize o servidor local do django:

```console
python manage.py runserver
```

## Para configurar o envio de email via gmail, siga o seguinte tutorial para obter o EMAIL_HOST_USER e o EMAIL_HOST_PASSWORD e adicioná-los ao .env:

- https://support.google.com/accounts/answer/185833?hl

## Acesso admin

O admin do django está habilitado. Para acessá-lo, rode o seguinte comando:

```console
python manage.py createsuperuser
```

e preencha os dados solicitados para criação de um super usuário.

A url para acessar o admin é http://127.0.0.1:8000/admin
