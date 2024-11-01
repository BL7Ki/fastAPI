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

