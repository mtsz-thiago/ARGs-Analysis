from os import sep
# from prefect import task, Flow, Parameter, context
from Bio import SeqIO

import numpy as np
import pandas as pd
import typing as ty
import yaml

def load_fasta(fasta_input_path: str) -> ty.List[ty.Any]:
    
    with open(fasta_input_path, "r") as f:
        fasta_data = SeqIO.parse(f, "fasta")
        in_mem_data = [s for s in fasta_data]

    return in_mem_data

def build_kmer_seq(data: SeqIO, kmer_sz: int) -> str:
    seq_data = str(data.seq)
    num_kmers = len(seq_data)-kmer_sz+1
    kmers = [ seq_data[i:i+kmer_sz] for i in range(0, num_kmers) ]
    return ' '.join(kmers)

def random_labels(size) -> pd.Series:
    return np.random.randint(0,2,size=size)

def main(kmer_sz: int, fasta_input_path: str):
    
    data = load_fasta(fasta_input_path)
    
    kmers = np.array([ build_kmer_seq(seq, kmer_sz) for seq in data])
    labels = random_labels(len(data))

    train_df = pd.DataFrame({"sequence": kmers, "label": labels})
    train_df.to_csv("data/train.tsv", sep='\t',index=False)

if __name__ == "__main__":
    params = yaml.safe_load(open("params.yaml"))["train"]
    main(**params)