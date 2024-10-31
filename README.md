Session basicamente serve para n fazermos chamadas diretas do codigo pro db, com a session 
a gente tem esse meio de campo para conseguir gerenciar melhor essas chamadas

engine = No SQLAlchemy, o engine é o componente responsável pela conexão com o banco de dados. Ele gerencia a comunicação entre o SQLAlchemy e o banco de dados que você está usando (como PostgreSQL, MySQL, SQLite, etc.). O engine permite que você crie uma interface de alto nível para manipular dados em um banco relacional, traduzindo comandos Python para SQL nativo e executando esses comandos diretamente no banco.