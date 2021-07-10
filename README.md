Deep ARG
===

Experimentações e estudos de workflows e métodos para a identificação de ARGs (genes de resistência a antibióticos)

## Sobre

Este reposítório reune um conjunto de scripts, notebooks, etc. que constituem experimentações e estudos a cerca de maneiras de fazer a identificação de ARGs.

## Desenvolvimento

### Requisitos

Este repositório usa recursos da AWS para storage e processamento

- [docker](https://www.docker.com/): para conteinerizar o ambiente de desenvolvimento.
- [AWS Account](https://aws.amazon.com/pt/): para acesso a serviços e recursos em nuvem.

> O uso de recursos em nuvem implica em cobraça. 

### Dev Container

O [Dockerfile](./Dockerfile) na raiz deste repositório define uma imagem para o ambiente de desenvolvimento do projeto. Se você for uma pessoa do [VSCode](https://code.visualstudio.com/) o [./devcontainer] facilitará sua vida. Siga o [tutorial](https://code.visualstudio.com/docs/remote/containers) para habilitar o uso.

> Por conveniência as configurações `aws` serão montadas no container de desenvolvimento, portanto configura seu cli para sua conta de dev e o resto está feito

