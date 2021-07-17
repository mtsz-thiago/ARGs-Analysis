from prefect import task, Flow, Parameter, context
from Bio import SeqIO

import yaml

@task
def load_fasta(fasta_input_path: str):

    logger = context.get("logger")

    with open(fasta_input_path, "r") as f:
        fasta_data = SeqIO.parse(f, "fasta")
        in_mem_data = [s for s in fasta_data]

    logger.info(f"# sequences read: ${len(in_mem_data)}")

    return in_mem_data


def main(kmer_sz: int, fasta_input_path: str):
    with Flow("train") as flow:

        kmer_sz_param = Parameter("kmer_sz", default=5)
        fasta_input_path_param =  Parameter("fasta_input_path")
        
        load_fasta(fasta_input_path_param)

    flow.run(fasta_input_path=fasta_input_path, )

if __name__ == "__main__":

    params = yaml.safe_load(open("params.yml"))["train"]

    main(**params)