"""
STAR manual 2.7.0a
https://physiology.med.cornell.edu/faculty/skrabanek/lab/angsd/lecture_notes/STARmanual.pdf
"""

from subprocess import check_call


def star_genome_generate(genome_fasta_file, sjdb_gtf_file, genome_dir, run_thread_n=8):
    """Run STAR to generate genome index"""

    args = [
        "STAR",
        "--runMode", "genomeGenerate",
        "--runThreadN", str(run_thread_n),
        "--genomeDir", genome_dir,
        "--genomeFastaFiles", genome_fasta_file,
        "--sjdbGTFfile", sjdb_gtf_file,
    ]
    print(" ".join(args))
    check_call(args)


def star_align_reads(read_files, out_prefix, run_thread_n=8):
    """Run STAR to align reads"""

    if not isinstance(read_files, list):
        assert isinstance(read_files, str)
        read_files = [read_files]

    args = [
        "STAR",
        "--runMode", "alignReads",
        "--runThreadN", str(run_thread_n),
        "--readFilesIn", *read_files,
        "--outFilterType", "BySJout",
        "--outFilterMultimapNmax", "20",
        "--alignSJoverhangMin", "8",
        "--alignSJDBoverhangMin", "1",
        "--outFilterMismatchNmax", "999",
        "--outFilterMismatchNoverReadLmax", "0.04",
        "--alignIntronMin", "20",
        "--alignIntronMax", "1000000",
        "--quantMode", "TranscriptomeSAM",
        "--outFileNamePrefix", out_prefix,
    ]
    print(" ".join(args))
    check_call(args)
