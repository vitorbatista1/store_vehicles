# 🚗 Car Dealership Management System

Este é um projeto de um sistema de gerenciamento para uma loja de carros, desenvolvido com Python e Django. Ele permite gerenciar o catálogo de carros, informações de clientes e realizar vendas de maneira eficiente.

## 📋 Funcionalidades

- Gerenciamento de carros:
  - Cadastro, atualização e remoção de veículos.
  - Listagem de veículos disponíveis para venda.
  - Filtros por marca, modelo, ano e preço.
- Controle de clientes:
  - Cadastro de clientes.
  - Histórico de compras.
- Gerenciamento de vendas:
  - Registro de vendas realizadas.
  - Relatórios financeiros.
- Painel administrativo seguro.

## 🔧 Tecnologias Utilizadas

- **Backend**: [Python](https://www.python.org/), [Django](https://www.djangoproject.com/)
- **Banco de Dados**: SQLite (pode ser configurado para outros bancos, como PostgreSQL ou MySQL)
- **Frontend**: HTML, CSS, JavaScript (padrão do Django Admin)
- **Outras Dependências**:
  - Django Rest Framework (para API)
  - Bootstrap (para estilização)

## 🚀 Como Executar o Projeto

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Virtualenv para gerenciamento de ambientes virtuais.
- Git (opcional, para clonar o repositório).

### Passo a Passo

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/sua-loja-de-carros.git
   cd sua-loja-de-carros
   ```

2. **Crie e ative o ambiente virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows
   ```

3. **Instale as dependências**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as migrações do banco de dados**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Crie um superusuário** (opcional, para acessar o painel administrativo):

   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor de desenvolvimento**:

   ```bash
   python manage.py runserver
   ```

7. **Acesse a aplicação**:

   - Frontend: [http://localhost:8000](http://localhost:8000)
   - Painel administrativo: [http://localhost:8000/admin](http://localhost:8000/admin)


## 📞 Contato

- **Autor**: Vitor Batista
- **Email**: [vitorbatista177@outlook.com](mailto\:vitorbatista177@outlook.com)
- **LinkedIn**: [https://br.linkedin.com/in/vitor-batista-80a4a11b0](https://https://br.linkedin.com/in/vitor-batista-80a4a11b0)

---

*Desenvolvido usando Python e Django.*

