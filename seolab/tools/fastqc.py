"""
FastQC: A quality control tool for high throughput sequence data.
https://www.bioinformatics.babraham.ac.uk/projects/fastqc/
"""

from subprocess import check_call


def fastqc(fastq_file):
    """Run FastQC for quality check"""
    args = ["fastqc", fastq_file]
    print(" ".join(args))
    check_call(args)
