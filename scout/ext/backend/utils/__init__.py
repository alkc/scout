# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals
from .get_case import get_institute, get_case
from .get_genotype import get_genotype
from .get_transcript import get_transcript
from .generate_md5_key import generate_md5_key
from .get_genes import get_genes
from .get_compounds import get_compounds
from .get_mongo_variant import get_mongo_variant


# These are the valid SO terms with corresponfing severity rank
SO_TERMS = {
  'transcript_ablation': {'rank':1, 'region':'exonic'},
  'splice_donor_variant': {'rank':2, 'region':'splicing'},
  'splice_acceptor_variant': {'rank':3, 'region':'splicing'},
  'stop_gained': {'rank':4, 'region':'exonic'},
  'frameshift_variant': {'rank':5, 'region':'exonic'},
  'stop_lost': {'rank':6, 'region':'exonic'},
  'start_lost': {'rank': 7, 'region': 'exonic'},
  'initiator_codon_variant': {'rank':8, 'region':'exonic'},
  'inframe_insertion': {'rank':9, 'region':'exonic'},
  'inframe_deletion': {'rank':10, 'region':'exonic'},
  'missense_variant': {'rank':11, 'region':'exonic'},
  'protein_altering_variant': {'rank':12, 'region':'exonic'},
  'transcript_amplification': {'rank':13, 'region':'exonic'},
  'splice_region_variant': {'rank':14, 'region':'splicing'},
  'incomplete_terminal_codon_variant': {'rank':15, 'region':'exonic'},
  'synonymous_variant': {'rank':16, 'region':'exonic'},
  'stop_retained_variant': {'rank':17, 'region':'exonic'},
  'coding_sequence_variant': {'rank':18, 'region':'exonic'},
  'mature_miRNA_variant': {'rank':19, 'region':'ncRNA_exonic'},
  '5_prime_UTR_variant': {'rank':20, 'region':'5UTR'},
  '3_prime_UTR_variant': {'rank':21, 'region':'3UTR'},
  'non_coding_transcript_exon_variant': {'rank':22, 'region':'ncRNA_exonic'},
  'non_coding_exon_variant': {'rank':23, 'region':'ncRNA_exonic'},
  'non_coding_transcript_variant': {'rank':24, 'region':'ncRNA_exonic'},
  'nc_transcript_variant': {'rank':25, 'region':'ncRNA_exonic'},
  'intron_variant': {'rank':26, 'region':'intronic'},
  'NMD_transcript_variant': {'rank':27, 'region':'ncRNA'},
  'upstream_gene_variant': {'rank':28, 'region':'upstream'},
  'downstream_gene_variant': {'rank':29, 'region':'downstream'},
  'TFBS_ablation': {'rank':30, 'region':'TFBS'},
  'TFBS_amplification': {'rank':31, 'region':'TFBS'},
  'TF_binding_site_variant': {'rank':32, 'region':'TFBS'},
  'regulatory_region_ablation': {'rank':33, 'region':'regulatory_region'},
  'regulatory_region_amplification': {'rank':34, 'region':'regulatory_region'},
  'regulatory_region_variant': {'rank':35, 'region':'regulatory_region'},
  'feature_elongation': {'rank':36, 'region':'genomic_feature'},
  'feature_truncation': {'rank':37, 'region':'genomic_feature'},
  'intergenic_variant': {'rank':38, 'region':'intergenic_variant'}
}
