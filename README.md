# API E-commerce

API REST desenvolvida em **Python** com **Flask**, utilizando **SQLite** para persistência dos dados e **Redis** como camada de cache.

O projeto foi desenvolvido com foco no aprendizado e aplicação prática de conceitos de desenvolvimento **Back-end**, incluindo APIs REST, organização em camadas, acesso a banco de dados, cache e testes automatizados.

## 🚀 Tecnologias

* **Python**
* **Flask**
* **SQLite**
* **Redis**
* **Pytest**
* **API REST**
* **Git/GitHub**

## 🔌 Endpoints

### Criar produto

```http
POST /products
```

Exemplo de requisição:

```json
{
    "name": "cafe",
    "price": 15.90,
    "quantity": 10
}
```

### Buscar produto pelo nome

```http
GET /products/<product_name>
```

Exemplo:

```http
GET /products/cafe
```

A busca utiliza o **Redis como cache**, reduzindo consultas repetidas ao banco de dados.

## 🗄️ Banco de dados

O projeto utiliza **SQLite** para armazenar os produtos.

Estrutura da tabela:

```sql
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price FLOAT NOT NULL,
    quantity INTEGER NOT NULL
);
```

O SQLite é responsável pela persistência definitiva dos dados.

## ⚡ Redis

O **Redis** é utilizado como mecanismo de cache da aplicação.

Quando um produto é pesquisado, a aplicação verifica primeiro se ele está disponível no Redis.

O fluxo de busca funciona da seguinte forma:

```text
Requisição
    ↓
Verifica Redis
    ↓
Produto encontrado?
    ├── Sim → Retorna produto
    │
    └── Não → Consulta SQLite
                  ↓
            Salva no Redis
                  ↓
            Retorna produto
```

Essa estratégia permite reduzir consultas repetidas ao banco de dados e melhorar o desempenho da aplicação.

## 🔴 Configuração do Redis

O Redis deve estar em execução para que o sistema de cache funcione.

Por padrão:

```text
Host: 127.0.0.1
Port: 6379
```

Para verificar se o Redis está funcionando:

```bash
redis-cli ping
```

Resultado esperado:

```text
PONG
```

## ▶️ Como executar

Clone o projeto:

```bash
git clone <URL_DO_REPOSITORIO>
```

Entre no diretório:

```bash
cd API-ecommece
```

Crie o ambiente virtual:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:

```bash
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Certifique-se de que o Redis esteja executando na porta `6379`.

Depois execute a aplicação:

```bash
flask run
```

A API estará disponível em:

```text
http://127.0.0.1:5000
```

## 🧪 Testes

Para executar os testes:

```bash
pytest
```

Para visualizar os testes com mais detalhes:

```bash
pytest -v
```

## 🎯 Objetivo do projeto

O principal objetivo deste projeto é colocar em prática conceitos importantes do desenvolvimento Back-end utilizando Python.

Entre os principais conceitos trabalhados estão:

* Desenvolvimento de APIs REST;
* Flask;
* SQLite;
* Redis;
* Cache;
* Separação de responsabilidades;
* Acesso a dados;
* Tratamento de erros;
* Testes automatizados;
* Organização de projetos Python.

## 📚 Aprendizados

Durante o desenvolvimento, o projeto permite compreender na prática como diferentes componentes de uma aplicação Back-end trabalham juntos.

Um dos principais pontos estudados é a utilização do **Redis como cache**, permitindo entender a diferença entre armazenamento persistente e armazenamento temporário.

O projeto também ajuda a desenvolver uma visão mais prática sobre organização de código, comunicação entre camadas, consultas ao banco de dados e tratamento de situações como produtos não encontrados.

## 👨‍💻 Autor

**João Vitor Abreu**

Desenvolvedor Back-end com foco em **Python, APIs REST, bancos de dados e desenvolvimento de sistemas**.

* Portfolio: https://vitorabreuportifolio.lovable.app
* LinkedIn: https://www.linkedin.com/in/vitorabreudev
* GitHub: https://github.com/abreu-developer
