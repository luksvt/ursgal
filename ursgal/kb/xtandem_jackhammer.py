META_INFO = {
    'engine_type' : {
        'search_engine' : True,
    },
    'output_extension'          : '.xml',
    'input_types'               : ['.mgf'],
    'create_own_folder'         : True,
    'include_in_git'            : False,
    'citation'                  : 'Craig R, Beavis RC. (2004) TANDEM: '\
        'matching proteins with tandem mass spectra.',

    'engine': {
        'darwin' : {
            '64bit' : {
                'exe'            : 'tandem',
                'url'            : '',
                'zip_md5'        : '65a270dd63acca8c29a66cbe1406c9ba',
                'additional_exe' : [],
            },
        },
        'linux' : {
            '64bit' : {
                'exe'            : 'tandem.exe',
                'url'            : '',
                'zip_md5'        : '4f53c35f9adae43f01106db95fe6419c',
                'additional_exe' : [],
            },
        },
        'win32' : {
            '64bit' : {
                'exe'            : 'tandem.exe',
                'url'            : '',
                'zip_md5'        : '0241c62699bde4d81995f2b9df56f781',
                'additional_exe' : [],
            },
        },
    },

    # 'engine_exe'                : {
    #     'win32'  : 'tandem.exe',
    #     'darwin' : 'tandem',
    #     'linux'  : 'tandem.exe'
    # },
    # 'zip_md5' : {
    #     'darwin' : { 
    #         '64bit' : '65a270dd63acca8c29a66cbe1406c9ba'
    #     },
    #     'linux' : { 
    #         '64bit' : '4f53c35f9adae43f01106db95fe6419c'
    #     },
    #     'win32' : { 
    #         '64bit' : '0241c62699bde4d81995f2b9df56f781'
    #     }
    # }
}

DEFAULT_PARAMS = {
    'validation_score_field'    : 'X\!Tandem:hyperscore',
    'evalue_field'              : 'X\!Tandem:expect',
    'validation_minimum_score'  : 0,
    'bigger_scores_better'      : True,
}

USEARCH_PARAM_VALUE_TRANSLATIONS = {
    True: 'yes',
    False: 'no',
    'da': 'Daltons',
}

USEARCH_PARAM_KEY_VALUE_TRANSLATOR = {
    'precursor_isotope_range'   : {
        '0'     : 'no',
        '0,1'   : 'yes',
        '0,1,2' : 'yes'
    },
    'enzyme' : {
        # NOTE: '{' & '}' are used by pythons format function, thus
        # they have to be escaped, i.e. {P} -> {{P}}!
        'argc' : '[R]|{P}',
        'aspn' : '[X]|[D]',
        'chymotrypsin' : '[FMWY]|{P}',
        'chymotrypsin_p' : '[FMWY]|[X]',
        'clostripain' : '[R]|[X]',
        'cnbr' : '[M]|{P}',
        'elastase' : '[AGILV]|{P}',
        'formic_acid' : '[D]|{P}',
        'gluc' : '[DE]|{P}',
        'gluc_bicarb' : '[E]|{P}',
        'iodosobenzoate' : '[W]|[X]',
        'lysc' : '[K]|{P}',
        'lysc_p' : '[K]|[X]',
        'lysn' : '[X]|[K]',
        'lysn_promisc' : '[X]|[AKRS]',
        'nonspecific' : '[X]|[X]',
        'pepsina' : '[FL]|[X]',
        'protein_endopeptidase' : '[P]|[X]',
        'staph_protease' : '[E]|[X]',
        'tca' : '[FMWY]|{P},[KR]|{P},[X]|[D]',
        'trypsin' : '[KR]|{P}',
        'trypsin_p' : '[RK]|[X]',
        'trypsin_cnbr' : '[KR]|{P},[M]|{P}',
        'trypsin_gluc' : '[DEKR]|{P}',
    }
}
USED_USEARCH_PARAMS = set([
    # 'minimal_required_assigned_peaks',
    # 'saps',
    # 'search_c_terminal_ions',
    # 'search_first_b1_ion',
    'modifications',
    'batch_size',
    'cleavage_cterm_mass_change',
    'cleavage_nterm_mass_change',
    'compensate_small_fasta',
    'cpus',
    'enzyme',
    'frag_mass_tolerance',
    'frag_mass_tolerance_unit',
    'frag_mass_type',
    'frag_method',
    'frag_min_mz',
    # 'input_file',
    'input_file_type',
    #'instrument',
    'label',
    'maximal_accounted_observed_peaks',
    'maximum_missed_cleavages',
    'mininimal_required_matched_peaks',
    'mininimal_required_observed_peaks',
    'neutral_loss_enabled',
    'neutral_loss_mass',
    'neutral_loss_window',
    'noise_suppression_enabled',
    'num_match_spec',
    'precursor_isotope_range',
    'precursor_mass_tolerance_minus',
    'precursor_mass_tolerance_plus',
    'precursor_mass_tolerance_unit',
    'precursor_mass_type',
    'precursor_max_charge',
    'precursor_min_charge',
    'precursor_min_mass',
    'score_a_ions',
    'score_b_ions',
    'score_c_ions',
    'score_x_ions',
    'score_y_ions',
    'score_z_ions',
    'semi_enzyme',
    'spec_dynamic_range',
    'stp_bias',
    'use_refine'
])
