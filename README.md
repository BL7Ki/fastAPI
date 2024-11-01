Configurações de ambiente e os 12 fatores
Uma boa prática no desenvolvimento de aplicações é separar as configurações do código. Configurações, como credenciais de banco de dados, são propensas a mudanças entre ambientes diferentes (como desenvolvimento, teste e produção). Misturá-las com o código pode tornar o processo de mudança entre esses ambientes complicado e propenso a erros.

Além disso, expor credenciais de banco de dados e outras informações sensíveis no código-fonte é uma prática de segurança ruim. Se esse código fosse comprometido, essas informações poderiam ser usadas para acessar e manipular seus recursos.

Por isso, usaremos o pydantic-settings para gerenciar nossas configurações de ambiente. A biblioteca permite que você defina configurações em arquivos separados ou variáveis de ambiente e acesse-as de uma maneira estruturada e segura em seu código.

Isso está alinhado com a metodologia dos 12 fatores, um conjunto de melhores práticas para desenvolvimento de aplicações modernas. O terceiro fator, "Config", afirma que as configurações que variam entre os ambientes devem ser armazenadas no ambiente e não no código.
=========================================

O arquivo .env é usado para armazenar variáveis de ambiente em aplicações, especialmente em projetos de desenvolvimento web. Essas variáveis geralmente contêm configurações sensíveis ou específicas do ambiente de execução, como:

Credenciais: Dados como chaves de API, tokens, logins e senhas, evitando que essas informações fiquem hardcoded (gravadas diretamente) no código-fonte.
Configurações do Banco de Dados: Parâmetros de conexão, como DB_HOST, DB_USER, DB_PASSWORD, etc.
Configurações Específicas de Ambiente: Variáveis que podem mudar entre ambientes (desenvolvimento, teste, produção), como URLs de serviços externos ou a porta de execução.
Ao usar um arquivo .env, o código pode acessar essas variáveis sem a necessidade de expô-las diretamente, aumentando a segurança e tornando o projeto mais modular. Ferramentas como o dotenv em Python ou Node.js são comuns para carregar e ler essas variáveis automaticamente.

========================================

a base de dados precisa ir para o git ignore

========================================

Migrações em banco de dados são processos para gerenciar e aplicar mudanças na estrutura de um banco de dados de forma organizada e controlada. Elas são comumente usadas em desenvolvimento para garantir que a estrutura do banco (como tabelas, colunas, índices, etc.) evolua conforme novas funcionalidades são implementadas na aplicação. Com migrações, você pode:

Criar e modificar tabelas: Adicionar ou remover tabelas, colunas e alterar tipos de dados.
Gerenciar histórico de alterações: Cada mudança tem seu próprio "script de migração" com um histórico, permitindo reverter ou reaplicar alterações.
Sincronizar ambientes: Manter o banco de dados atualizado nos ambientes de desenvolvimento, teste e produção de maneira uniforme.
Automatizar: Scripts de migração ajudam a automatizar e documentar mudanças, tornando-as reproduzíveis e minimizando erros.
Em frameworks como Django (Python), Rails (Ruby) e Laravel (PHP), o uso de migrações é muito comum, e elas geralmente são geradas automaticamente, com comandos para criar, aplicar e reverter alterações.

No arquivo alembic.ini: ficam as configurações gerais das nossas migrações. Na pasta migrations foram criados um arquivo chamado env.py, esse arquivo é responsável por como as migrações serão feitas, e o arquivo script.py.mako é um template para as novas migrações.