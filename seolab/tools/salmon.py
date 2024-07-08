"""
Salmon: Highly-accurate & wicked fast transcript-level quantification from RNA-seq reads using selective alignment
https://github.com/COMBINE-lab/salmon
https://salmon.readthedocs.io/en/nb/index.html
"""

from subprocess import check_call


def salmon_quant_qmb(salmon_index, read1_file, read2_file, out_dir):
    """Run gene quantification by salmon with quasi-mapping-based mode"""

    args = [
        "salmon", "quant",
        "-l", "A",
        "-i", salmon_index,
        "-1", read1_file,
        "-2", read2_file,
        "--validateMappings",
        "-o", out_dir,
    ]

    print(" ".join(args))
    check_call(args)


def salmon_quant_ab(transcripts_file, alignments_file, out_dir):
    """Run gene quantification by salmon with alignment-based mode"""

    args = [
        "salmon", "quant",
        "-l", "A",
        "-t", transcripts_file,
        "-a", alignments_file,
        "-o", out_dir,
    ]

    print(" ".join(args))
    check_call(args)
