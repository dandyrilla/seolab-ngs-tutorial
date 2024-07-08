"""
Tools (written in C using htslib) for manipulating next-generation sequencing data
https://github.com/samtools/samtools
"""

import os
from subprocess import check_call


def samtools_faidx(fasta_file):
    """Run samtools faidx (index fasta file)"""

    check_call(["samtools", "faidx", fasta_file])


def samtools_sort(bam_file, sorted_bam_file=None):
    """Run samtools sort"""

    if sorted_bam_file is None:
        filename, ext = os.path.splitext(bam_file)
        assert ext.lower() == ".bam"
        sorted_bam_file = f"{filename}.sorted{ext}"

    check_call(["samtools", "sort", bam_file, "-o", sorted_bam_file])


def samtools_index(bam_file):
    """Run samtools index"""

    check_call(["samtools", "index", bam_file])
