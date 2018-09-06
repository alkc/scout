# clinvar Variant sheet
CLINVAR_HEADER = {
    'local_id' : '##Local ID',
    'linking_id' : 'Linking ID',
    'gene_symbol' : 'Gene symbol',
    'ref_seq' : 'Reference sequence',
    'hgvs' : 'HGVS',
    'chromosome' : 'Chromosome',
    'start' : 'Start',
    'stop' : 'Stop',
    'ref' : 'Reference allele',
    'alt' : 'Alternate allele',
    'var_type' : 'Variant type',
    'ncopy' : 'Copy number',
    'ref_copy' : 'Reference copy number',
    'breakpoint1' : 'Breakpoint 1',
    'breakpoint2' : 'Breakpoint 2',
    'outer_start' : 'Outer start',
    'inner_start' : 'Inner start',
    'inner_stop' : 'Inner stop',
    'outer_stop' : 'Outer stop',
    'variations_ids' : 'Variation identifiers',
    'condition_id_type' : 'Condition ID type', #default = 'HPO'
    'condition_id_value' : 'Condition ID value',
    'condition_comment' : 'Condition comment',
    'clinsig' : 'Clinical significance',
    'last_evaluated' : 'Date last evaluated',
    'variant_comment' : 'Comment on variant',
    'assertion_method' : 'Assertion method',
    'inheritance_mode' : 'Mode of inheritance',
    'clinsig_cit' : 'Clinical significance citations',
    'clinsig_comment' : 'Comment on clinical significance',
    'drug_response' : 'Drug response condition',
    'funct_conseq' : 'Functional consequence',
    'funct_conseq_comment' : 'Comment on functional consequence'
}

# extra from form:
# category@var_id

# clinvar CaseData sheet
CASEDATA_HEADER = {
    'linking_id' : 'Linking ID',
    'individual_id' : 'Individual ID',
    'collection_method' : 'Collection method', # default = 'clinical testing'
    'allele_origin' : 'Allele origin',
    'is_affected' : 'Affected status',
    'sv_analysis_method' : 'Structural variant method/analysis type',
    'clin_features' : 'Clinical features',
    'clin_features_comment' : 'Comment on clinical features',
    'tissue' : 'Tissue',
    'sex' : 'Sex',
    'age' : 'Age',
    'ethnicity' : 'Population Group/Ethnicity',
    'fam_history' : 'Family history',
    'is_proband' : 'Proband',
    'is_secondary_finding' : 'Secondary finding',
    'is_mosaic' : 'Mosaicism',
    'zygosity' : 'Zygosity',
    'co_occurr_gene' : 'Co-occurrences, same gene',
    'co_occurr_other' : 'Co-occurrence, other genes',
    'evidence_cit' : 'Evidence citations',
    'platform_type' : 'Platform type',
    'platform_name' : 'Platform name',
    'method' : 'Method',
    'method_purpose' : 'Method purpose',
    'method_cit' : 'Method citations',
    'testing_lab' : 'Testing laboratory',
    'reported_at' : 'Date variant was reported to submitter'
}
