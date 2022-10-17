import sys
import argparse  
import os
from base.config import base_config, cfg_convert


def get_config():
    strategy = 'sche_f3net' # 'sche_test'
    parser = base_config(strategy)
    
    # Add model-specific parameters here
    # parser.add_argument('--param', default='some_params')
    
    config = cfg_convert(parser)
    
    # In here, 'batch' means how many samples can be fed to the GPU in one iteration. It only decided by the GPU memory and model consumption. The actual batch size is defined in 'strategy' as 'agg_batch'.
    config['ave_batch'] = 16
    if config['loss'] == '':
        config['loss'] = {'sal': ['ad', 1, 1]}
    
    return config