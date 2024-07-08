"""
Wrapper functions for NCBI SRA Toolkit
https://github.com/ncbi/sra-tools/wiki
"""

from subprocess import check_call


def fastq_dump(sra_run_id, out_dir=None, split_files=False):
    """Run fastq-dump to download sequenced reads"""
    opts = []
    if split_files:
        opts.append("--split-files")
    if out_dir:
        opts.append("-O")
        opts.append(out_dir)
    args = ["fastq-dump", *opts, sra_run_id]
    print(" ".join(args))
    check_call(args)
