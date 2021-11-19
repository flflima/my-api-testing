# My API Testing

Script em Python para consultar uma API e salvar o corpo da resposta.

## Passos

Instalando ambiente de desenvolvimento `venv`:

```console
sudo apt-get install python3-venv
```

Criando ambiente:

```console
python3 -m venv .
```

Ativando o ambiente:

```console
source bin/activate
```

Instalando dependências:

```python
pip install -r requirements.txt
```

Executando:

```python
python src/get_dogs_breeds.py
```

API utilizada:

https://dog.ceo/dog-api/