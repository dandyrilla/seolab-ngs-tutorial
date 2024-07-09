# seolab-ngs-tutorial

In this tutorial, we will learn RNA-seq, ATAC-seq, and single-cell RNA-seq analysis methods using the following samples.

## Bulk RNA-seq

Expression profiling by high throughput sequencing

- [GSE255410](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255410):
  FOXO1 is a master regulator of CAR T memory programming (RNA_FOXO1_KO)
  - [GSM8072137](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072137): CD19_AAVS1_Donor_ND500
  - [GSM8072138](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072138): CD19_AAVS1_Donor_ND607
  - [GSM8072139](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072139): CD19_AAVS1_Donor_ND612
  - [GSM8072140](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072140): CD19_FOXO1KO_Donor_ND500
  - [GSM8072141](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072141): CD19_FOXO1KO_Donor_ND607
  - [GSM8072142](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072142): CD19_FOXO1KO_Donor_ND612

- [GSE255412](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255412):
  FOXO1 is a master regulator of CAR T memory programming (RNA_FOXO1_OE)
  - [GSM8072152](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072152): FOXO1WT-CD19_Rep1
  - [GSM8072153](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072153): FOXO1WT-CD19_Rep2
  - [GSM8072154](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072154): FOXO1WT-CD19_Rep3
  - [GSM8072155](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072155): NGFR-CD19_Rep1
  - [GSM8072156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072156): NGFR-CD19_Rep2
  - [GSM8072157](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072157): NGFR-CD19_Rep3
  - [GSM8072158](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072158): TCF1-CD19_Rep1
  - [GSM8072159](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072159): TCF1-CD19_Rep2
  - [GSM8072160](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072160): TCF1-CD19_Rep3
  - [GSM8072161](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072161): FOXO1WT-HA_Rep1
  - [GSM8072162](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072162): FOXO1WT-HA_Rep2
  - [GSM8072163](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072163): FOXO1WT-HA_Rep3
  - [GSM8072164](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072164): NGFR-HA_Rep1
  - [GSM8072165](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072165): NGFR-HA_Rep2
  - [GSM8072166](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072166): NGFR-HA_Rep3
  - [GSM8072167](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072167): TCF1-HA_Rep1
  - [GSM8072168](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072168): TCF1-HA_Rep2
  - [GSM8072169](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072169): TCF1-HA_Rep3

## Bulk ATAC-seq

Genome binding/occupancy profiling by high throughput sequencing

- [GSE255415](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE255415):
  FOXO1 is a master regulator of CAR T memory programming (ATAC_FOXO1_OE)
  - [GSM8072191](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072191): CD19_FOXO1-WT_2
  - [GSM8072192](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072192): CD19_FOXO1-WT_3
  - [GSM8072193](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072193): CD19_FOXO1-WT_1
  - [GSM8072194](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072194): CD19_NGFR_1
  - [GSM8072195](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072195): CD19_NGFR_3
  - [GSM8072196](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072196): CD19_NGFR_4
  - [GSM8072197](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072197): CD19_TCF1_3
  - [GSM8072198](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072198): CD19_TCF1_4
  - [GSM8072199](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072199): CD19_TCF1_1
  - [GSM8072200](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072200): HA_FOXO1-WT_2
  - [GSM8072201](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072201): HA_FOXO1-WT_1
  - [GSM8072202](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072202): HA_FOXO1-WT_4
  - [GSM8072203](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072203): HA_NGFR_2
  - [GSM8072204](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072204): HA_NGFR_4
  - [GSM8072205](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072205): HA_NGFR_1
  - [GSM8072206](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072206): HA_TCF1_3
  - [GSM8072207](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072207): HA_TCF1_1
  - [GSM8072208](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8072208): HA_TCF1_4

## Single-cell RNA-seq (scRNA-seq)

Expression profiling by high throughput sequencing

- [GSE263156](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE263156):
  FOXO1 is a master regulator of CAR T memory programming (scRNA_FOXO1_NGFR)
  - [GSM8186911](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8186911): FOXO1_tumor
  - [GSM8186912](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSM8186912): NGFR_tumor
 