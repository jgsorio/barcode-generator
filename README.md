# Bar Code Project

API REST simples, feita com **Flask**, que gera imagens de código de barras (padrão **Code128**) a partir de um código de produto enviado por requisição HTTP. Projeto desenvolvido durante o NLW da Rocketseat.

## Tecnologias

- Python 3.10+
- [Flask](https://flask.palletsprojects.com/) — servidor web e rotas
- [python-barcode](https://pypi.org/project/python-barcode/) + [Pillow](https://python-pillow.org/) — geração da imagem (PNG)
- [Black](https://black.readthedocs.io/) + [pre-commit](https://pre-commit.com/) — formatação de código

## Estrutura do projeto

```
bar-code-project/
├── run.py                          # Ponto de entrada: sobe o servidor na porta 3001
├── requirements.txt
├── images/                         # Imagens geradas (criada automaticamente, ignorada pelo git)
└── src/
    ├── helpers/
    │   ├── barcode_generate.py     # Classe BarcodeGenerate: valida e gera o código de barras
    │   ├── http_request.py         # Abstração de requisição (header, body, params)
    │   └── http_response.py        # Abstração de resposta (status_code, body)
    └── main/
        ├── routes/
        │   └── barcode.py          # Blueprint com a rota POST /barcode-generate
        └── server/
            └── server.py           # Criação do app Flask e registro das rotas
```

### Como funciona

1. A rota `POST /barcode-generate` recebe um JSON com o campo `product_code`.
2. O body é encapsulado em um `HttpRequest` e repassado para `BarcodeGenerate.validate_and_generate`.
3. A classe gera uma imagem PNG Code128 em `images/<product_code>.png` (criando a pasta se necessário).
4. Retorna um `HttpResponse` convertido em JSON: status `200` em caso de sucesso ou `400` se ocorrer algum erro.

## Instalação

```bash
# 1. Clone o repositório
git clone https://github.com/jgsorio/barcode-generator
cd bar-code-project

# 2. Crie e ative um ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. (Opcional) Ative o hook de formatação com Black
pre-commit install
```

## Como usar

Inicie o servidor:

```bash
python run.py
```

A API ficará disponível em `http://localhost:3001` (modo debug ligado, escutando em `0.0.0.0`).

### Endpoint

`POST /barcode-generate`

**Body (JSON):**

| Campo          | Tipo   | Descrição                                                       |
| -------------- | ------ | --------------------------------------------------------------- |
| `product_code` | string | Código a ser codificado (caracteres ASCII aceitos pelo Code128) |

**Exemplo de requisição:**

```bash
curl -X POST http://localhost:3001/barcode-generate \
  -H "Content-Type: application/json" \
  -d '{"product_code": "123456789"}'
```

**Resposta de sucesso (200):**

```json
{
  "message": "Barcode generated successfully",
  "file": "images/123456789.png"
}
```

**Resposta de erro (400):**

```json
{
  "message": "Error generating barcode: ..."
}
```

A imagem gerada fica salva na pasta `images/`, dentro do diretório de onde o servidor foi iniciado.

## Formatação de código

O projeto usa o Black via pre-commit. Para rodar manualmente em todos os arquivos:

```bash
pre-commit run --all-files
```
