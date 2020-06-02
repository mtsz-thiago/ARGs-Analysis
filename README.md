Deep ARG
===

Experimentações e estudos de workflows para a identificação de ARGs (genes de resistência a antibióticos)

## Sobre

Este reposítório reune um conjunto de scripts, notebooks, etc. que constituem experimentações e estudos a cerca de maneiras de fazer a identificação de ARGs.

## Requisitos


* [Anaconda]([ww](https://www.anaconda.com/)) - distribuição python para ciência de dados.
* [Docker](www.docker.com) - IaaC (Infrastructure as a Code).

## Conda env

O ambiente anaconda necessário para rodar os scripts está definido no arquivo YAML [bio_env.yml](./bio_env.yml). Para criá-çlo:

```shell
conda create -f bio_env.yml
```

para adicionar esse ambiente como ambeinte para o ipython:

```shell
python -m ipykernel install --user --name bio_env --display-name "bio_env"
```

## Docker usage

Existe uma imagem, [gaarangoa/deeparg](https://hub.docker.com/r/gaarangoa/deeparg),  que encapsula a linha de comando em um container.

```shell
docker run --rm -it -v $(pwd):/data/  gaarangoa/deeparg:latest \
    python /deeparg/deepARG.py \
    --align \
    --genes \
    --input /data/input_data/GCF_000746645.1_ASM74664v1_protein.fa \
    --output /data/output/ORFs \
    --type prot
```