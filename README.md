AnGRA
===

Biblioteca para análise de genômica de resistência a antibióiticos. 

## Sobre

Este projeto deve gerar uma artigo científico e posteriormente gerar uma biblioteca python que facilite a análise da genômica de organismos resitentes a antibióticos.

## Desenvolvimento

### Requisitos

Este repositório usa recursos da AWS para storage e processamento

- [docker](https://www.docker.com/): para conteinerizar o ambiente de desenvolvimento.
- [AWS Account](https://aws.amazon.com/pt/): para acesso a serviços e recursos em nuvem.

> O uso de recursos em nuvem implica em cobraça. 

### Dev Container

O [Dockerfile](./Dockerfile) na raiz deste repositório define uma imagem para o ambiente de desenvolvimento do projeto. Se você for uma pessoa do [VSCode](https://code.visualstudio.com/) o [devcontainer](./devcontainer) facilitará sua vida. Siga o [tutorial](https://code.visualstudio.com/docs/remote/containers) para habilitar o uso.

> Por conveniência as configurações `aws` serão montadas no container de desenvolvimento, portanto configura seu cli para sua conta de dev e o resto está feito

