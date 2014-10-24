Trabalho de Administração de Custos - Método Absorção com Departamentalização
===============

### Executando o projeto ###

Para executar o projeto, basta ir na pasta custeio_absorcao e executar:
```
python manage.py runserver
```

O servidor local passará a responder em `http://localhost:8000`

Para acessar o admin, abra: `http://localhost:8000/admin`

### Instalando o projeto ###
Dê um
```
git clone https://github.com/diegoaniceto/absorcao_custos.git
```
Caso não tenha definido um virtualenv para essa pasta, dê um:
```
virtualenv env
```
E depois:
```
source env/bin/activate
```
Agora instale as dependências usando
```
pip install -r requirements.txt
```
Sincronize os modelos com o banco (caso já exista algum, exclua o arquivo '.db'):
```
python manage.py syncdb
```
Rode o script para povoar o banco
```
python povoa_banco.py
```

Pronto, já pode executar o projeto.

### Documentação do projeto ###
Link Docs:
https://docs.google.com/document/d/19RtQXSB7aPvgkXt6ln_3puDTUDya7vCDIO4ikgYYZIM/edit
