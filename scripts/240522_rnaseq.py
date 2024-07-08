import os
import sys

import pandas as pd

sys.path.append(".")  # noqa
from seolab.tools.fastqc import fastqc
from seolab.tools.sratoolkit import fastq_dump
from seolab.tools.star import star_align_reads, star_genome_generate
from seolab.utils import update_environ_path
from seolab.utils.fileio import read_tsv, to_tsv

HOME_DIR = os.path.expanduser("~")
OPT_ROOT = os.path.join(HOME_DIR, "opt")
GEO_ROOT = f"{HOME_DIR}/data/ncbi/geo"
ENSEMBL_ROOT = f"{HOME_DIR}/data/ensembl"


def create_metadata():
    """Create metadata of samples"""

    # GSE255410
    rows = [
        {"geo_sample_id": "GSM8072137", "sra_run_id": "SRR27922610", "desc": "CD19_AAVS1_Donor_ND500"},
        {"geo_sample_id": "GSM8072138", "sra_run_id": "SRR27922609", "desc": "CD19_AAVS1_Donor_ND607"},
        {"geo_sample_id": "GSM8072139", "sra_run_id": "SRR27922608", "desc": "CD19_AAVS1_Donor_ND612"},
        {"geo_sample_id": "GSM8072140", "sra_run_id": "SRR27922607", "desc": "CD19_FOXO1KO_Donor_ND500"},
        {"geo_sample_id": "GSM8072141", "sra_run_id": "SRR27922606", "desc": "CD19_FOXO1KO_Donor_ND607"},
        {"geo_sample_id": "GSM8072142", "sra_run_id": "SRR27922605", "desc": "CD19_FOXO1KO_Donor_ND612"},
    ]
    df = pd.DataFrame(rows)
    gse_dir = os.path.join(GEO_ROOT, "GSE255410")
    out_file_txt = os.path.join(gse_dir, "samples.txt")
    to_tsv(df, out_file_txt)
    print(out_file_txt)

    # GSE255412
    rows = [
        {"geo_sample_id": "GSM8072152", "sra_run_id": "SRR27921210", "desc": "FOXO1WT-CD19_Rep1"},
        {"geo_sample_id": "GSM8072153", "sra_run_id": "SRR27921209", "desc": "FOXO1WT-CD19_Rep2"},
        {"geo_sample_id": "GSM8072154", "sra_run_id": "SRR27921208", "desc": "FOXO1WT-CD19_Rep3"},
        {"geo_sample_id": "GSM8072155", "sra_run_id": "SRR27921207", "desc": "NGFR-CD19_Rep1"},
        {"geo_sample_id": "GSM8072156", "sra_run_id": "SRR27921206", "desc": "NGFR-CD19_Rep2"},
        {"geo_sample_id": "GSM8072157", "sra_run_id": "SRR27921205", "desc": "NGFR-CD19_Rep3"},
        {"geo_sample_id": "GSM8072158", "sra_run_id": "SRR27921204", "desc": "TCF1-CD19_Rep1"},
        {"geo_sample_id": "GSM8072159", "sra_run_id": "SRR27921203", "desc": "TCF1-CD19_Rep2"},
        {"geo_sample_id": "GSM8072160", "sra_run_id": "SRR27921202", "desc": "TCF1-CD19_Rep3"},
        {"geo_sample_id": "GSM8072161", "sra_run_id": "SRR27921201", "desc": "FOXO1WT-HA_Rep1"},
        {"geo_sample_id": "GSM8072162", "sra_run_id": "SRR27921200", "desc": "FOXO1WT-HA_Rep2"},
        {"geo_sample_id": "GSM8072163", "sra_run_id": "SRR27921199", "desc": "FOXO1WT-HA_Rep3"},
        {"geo_sample_id": "GSM8072164", "sra_run_id": "SRR27921198", "desc": "NGFR-HA_Rep1"},
        {"geo_sample_id": "GSM8072165", "sra_run_id": "SRR27921197", "desc": "NGFR-HA_Rep2"},
        {"geo_sample_id": "GSM8072166", "sra_run_id": "SRR27921196", "desc": "NGFR-HA_Rep3"},
        {"geo_sample_id": "GSM8072167", "sra_run_id": "SRR27921195", "desc": "TCF1-HA_Rep1"},
        {"geo_sample_id": "GSM8072168", "sra_run_id": "SRR27921194", "desc": "TCF1-HA_Rep2"},
        {"geo_sample_id": "GSM8072169", "sra_run_id": "SRR27921193", "desc": "TCF1-HA_Rep3"},
    ]
    df = pd.DataFrame(rows)
    gse_dir = os.path.join(GEO_ROOT, "GSE255412")
    out_file_txt = os.path.join(gse_dir, "samples.txt")
    to_tsv(df, out_file_txt)
    print(out_file_txt)


def load_metadata(geo_series_id):
    """Load metadata of samples"""
    in_file_txt = os.path.join(GEO_ROOT, geo_series_id, "samples.txt")
    df = read_tsv(in_file_txt)
    return df


def activate_environment():
    """Activate analysis environment by updating PATH variable"""

    paths = [
        f"{OPT_ROOT}/sratoolkit.3.1.0-ubuntu64/bin",  # SRAtoolkit (3.1.0)
        f"{OPT_ROOT}/fastqc-v0.12.1",  # FastQC (0.12.1)
        f"{OPT_ROOT}/STAR_2.7.10b/Linux_x86_64_static",  # STAR aligner (2.7.10b)
        f"{OPT_ROOT}/samtools-1.20",  # samtools (1.20)
        f"{OPT_ROOT}/gffread-0.12.7.Linux_x86_64",  # gffread (0.12.7)
        f"{OPT_ROOT}/salmon-1.10.0/bin",  # salmon (1.10.0)
    ]
    update_environ_path(paths, append=False)


def download_reads():
    """Download sequenced reads"""

    activate_environment()
    for geo_series_id in ("GSE255410", "GSE255412"):
        df = load_metadata(geo_series_id)
        for row in df.itertuples():
            out_dir = os.path.join(GEO_ROOT, geo_series_id, row.geo_sample_id)
            out_files = [os.path.join(out_dir, f"{row.sra_run_id}{suffix}.fastq") for suffix in ("_1", "_2")]
            if all(os.path.isfile(out_file) for out_file in out_files):
                continue
            os.makedirs(out_dir, exist_ok=True)
            fastq_dump(row.sra_run_id, out_dir=out_dir, split_files=True)


def check_quality_reads():
    """Check quality of reads by FastQC"""

    activate_environment()

    for geo_series_id in ("GSE255410", "GSE255412"):
        df = load_metadata(geo_series_id)
        for row in df.itertuples():
            sample_dir = os.path.join(GEO_ROOT, geo_series_id, row.geo_sample_id)
            for suffix in ("_1", "_2"):
                fastq_file = os.path.join(sample_dir, f"{row.sra_run_id}{suffix}.fastq")
                fastqc(fastq_file)


def generate_genome_index():
    """Generate genome index by STAR"""
    activate_environment()
    release_dir = os.path.join(ENSEMBL_ROOT, "release-112")
    genome_fasta_file = os.path.join(release_dir, "Homo_sapiens.GRCh38.dna.primary_assembly.fa")
    sjdb_gtf_file = os.path.join(release_dir, "Homo_sapiens.GRCh38.112.chr.gtf")
    genome_dir = os.path.join(release_dir, "Homo_sapiens.GRCh38.star")
    star_genome_generate(genome_fasta_file, sjdb_gtf_file, genome_dir)


def align_reads():
    """Align sequenced reads by STAR"""
    activate_environment()
    for geo_series_id in ("GSE255410", "GSE255412"):
        df = load_metadata(geo_series_id)
        for row in df.itertuples():
            sample_dir = os.path.join(GEO_ROOT, geo_series_id, row.geo_sample_id)
            read_files = [os.path.join(sample_dir, f"{row.sra_run_id}{suffix}.fastq") for suffix in ("_1", "_2")]
            out_prefix = os.path.join(sample_dir, "star") + "/"
            star_align_reads(read_files, out_prefix)


def main():
    """python3 scripts/240522_rnaseq.py"""

    # create_metadata()  # Create metadata of samples
    # download_reads()  # Download sequenced reads
    # check_quality_reads()  # Check quality of reads by FastQC

    # generate_genome_index()  # Generate genome index by STAR
    # align_reads()  # Align sequenced reads by STAR


if __name__ == '__main__':
    main()
