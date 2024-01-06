#	Api Auth django

### **como posso usar esta api no postman:**

- API de login, sign-up, rota post protegida e logout com o django, com o simple-jwt

Certamente! Vou guiá-lo através do processo de utilização da API com o Postman para as operações de login, sign-up, acesso a uma rota protegida e logout.

### 1. **Operação de Sign-up:**

- **Método:** POST

- **Endpoint:** `http://localhost:8000/api/signup/`

- Corpo (Body) da Requisição (JSON):

  ```
  json
  ```

- ```
  {
    "username": "seu_usuario",
    "password": "sua_senha",
    "email": "seu_email@example.com"
  }
  ```

- Envie a requisição e certifique-se de receber uma resposta indicando o sucesso ou falha do registro.

### 2. **Operação de Login:**

- **Método:** POST

- **Endpoint:** `http://localhost:8000/api/login/`

- Corpo (Body) da Requisição (JSON):

  ```
  json
  ```

- ```
  {
    "username": "seu_usuario",
    "password": "sua_senha"
  }
  ```

- Após enviar a requisição, você receberá um token de acesso no corpo da resposta.

### 3. **Acesso à Rota Protegida:**

- **Método:** GET
- **Endpoint:** `http://localhost:8000/api/protected/`
- Headers:
  - Key: `Authorization`
  - Value: `Bearer [seu_token_de_acesso]`
- Certifique-se de incluir o token de acesso obtido no passo anterior.

### 4. **Operação de Logout:**

- **Método:** POST
- **Endpoint:** `http://localhost:8000/api/logout/`
- Headers:
  - Key: `Authorization`
  - Value: `Bearer [seu_token_de_acesso]`
- Envie a requisição e certifique-se de receber uma resposta indicando o sucesso ou falha do logout.

Lembre-se de substituir `[seu_usuario]`, `[sua_senha]`, `[seu_email@example.com]` e `[seu_token_de_acesso]` pelos dados reais da sua aplicação.

Essas são operações básicas e genéricas. Dependendo da implementação específica na sua aplicação, podem existir requisitos adicionais ou parâmetros específicos. Certifique-se de ajustar conforme necessário com base nos detalhes da sua implementação.