# ProjetoCamadaNegocios

Plataforma de aluguel de imóveis por temporada — clone didático do Airbnb — desenvolvida com **Flask** e **MongoDB**.

---

## Funcionalidades

| Recurso | Detalhes |
|---|---|
| Login | Autenticação por email/senha com hash bcrypt (werkzeug) |
| Busca de imóveis | Filtro por cidade e preço máximo por noite |
| Disponibilidade | Visualização de períodos ocupados por imóvel |
| Reserva | Criação com verificação de conflito de datas |
| Painel | Listagem de reservas como hóspede e anfitrião |
| Anúncio | Cadastro de novo imóvel (perfis `anfitriao` e `ambos`) |

---

## Tecnologias

- **Backend:** Python 3.10+ + Flask 3.x
- **Banco de dados:** MongoDB (coleções: `usuarios`, `locais`, `reservas`)
- **Frontend:** HTML + CSS + JavaScript puro (sem frameworks)

---

## ⚡ Setup rápido no Windows

### 1. Instalar dependências

Abra o **PowerShell** ou **Prompt de Comando** na pasta do projeto e execute:

```bat
setup.bat
```

> Se o Python não for encontrado, [baixe aqui](https://www.python.org/downloads/) e marque **"Add Python to PATH"** durante a instalação.

### 2. Instalar o MongoDB

Baixe e instale o **MongoDB Community Edition**:  
👉 https://www.mongodb.com/try/download/community

Após a instalação, o MongoDB inicia automaticamente como serviço do Windows.

### 3. Iniciar o servidor

```bat
start.bat
```

Acesse **http://localhost:5000** no navegador.

---

## Setup manual (qualquer sistema)

```bash
# Criar e ativar ambiente virtual
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac

# Instalar dependências
pip install -r requirements.txt

# Iniciar
python app.py
```

Se o MongoDB estiver em outro endereço:

```bash
# Windows PowerShell
$env:MONGO_URI="mongodb://192.168.1.10:27017/"; python app.py

# Linux/Mac
MONGO_URI="mongodb://192.168.1.10:27017/" python app.py
```

---

## Dados de demonstração

O banco é populado automaticamente na primeira requisição.

| Email | Perfil | Senha |
|---|---|---|
| carlos@email.com | anfitriao | 123456 |
| maria@email.com | hospede | 123456 |
| ana@email.com | ambos | 123456 |

> Para reinserir os dados do zero: `python routes.py`

---

## API REST

| Método | Endpoint | Descrição |
|---|---|---|
| `POST` | `/api/login` | Autenticar usuário |
| `GET` | `/api/locais` | Listar imóveis (filtros: `cidade`, `preco_max`, `anfitriao_id`) |
| `POST` | `/api/locais` | Cadastrar imóvel |
| `GET` | `/api/locais/<id>/ocupacao` | Períodos ocupados de um imóvel |
| `GET` | `/api/reservas` | Listar reservas (filtros: `hospede_id`, `anfitriao_id`, `status`) |
| `POST` | `/api/reservas` | Criar reserva (valida conflito de datas) |