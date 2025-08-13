## Tarefas para a integração PHP/MySQL no site online985

### Fase 1: Planejamento da Integração
- [x] Pesquisar melhores práticas para integração de PHP e MySQL com sites frontend (CONCLUÍDO)
- [x] Definir as funcionalidades dinâmicas a serem implementadas (ex: formulário de contato com armazenamento de dados, área de notícias/blog) - Foco inicial no armazenamento de mensagens do formulário de contato.- [x] Escolher a abordagem de conexão com o banco de dados (MySQLi ou PDO) - Usaremos PDO por ser mais moderno e seguro.
- [x] Planejar a estrutura do banco de dados (tabelas e campos) - Tabela 'contacts' com campos: id, name, email, phone, message, created_at.

### Fase 2: Configuração do Ambiente PHP e MySQL
- [x] Instalar PHP e MySQL no ambiente (se necessário) - Instalado e serviços iniciados.
- [x] Configurar o servidor web para PHP (Apache/Nginx) - Apache2 configurado.
### Fase 3: Criação do Banco de Dados e Tabelas
- [x] Criar o banco de dados MySQL
- [x] Criar as tabelas necessárias para as funcionalidades dinâmicas

### Fase 4: Desenvolvimento do Backend PHP
- [x] Criar scripts PHP para conexão com o banco de dados
- [x] Desenvolver APIs PHP para inserção, leitura, atualização e exclusão de dados (CRUD)
- [x] Implementar validação e saneamento de dados no backend

### Fase 5: Integração Frontend-Backend
- [x] Modificar o formulário de contato para enviar dados ao backend PHP
- [x] Implementar requisições AJAX (Fetch API ou XMLHttpRequest) no frontend para interagir com as APIs PHP
- [x] Exibir dados dinâmicos do banco de dados no frontend (se aplicável)

### Fase 6: Testes e Depuração
- [x] Testar a conexão com o banco de dados
- [x] Testar todas as operações CRUD
- [x] Realizar testes de segurança (ex: injeção de SQL)
- [x] Depurar erros e ajustar o código

### Fase 7: Deploy da Aplicação Dinâmica
- [x] Preparar os arquivos do backend para deploy
- [x] Realizar o deploy do backend PHP e MySQL
- [x] Atualizar o site frontend com as novas funcionalidades

