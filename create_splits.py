import argparse
import glob
import os
import random
import pickle
import numpy as np
import shutil

from utils import get_module_logger

def create_directories(directories):
    for d in directories:
        if not os.path.exists(d):
            os.makedirs(d)

def split(data_dir):
    """
    Create three splits from the processed records. The files should be moved to new folders in the
    same directory. This folder should be named train, val and test.

    args:
        - data_dir [str]: data directory, /mnt/data
    """
    train_dir = os.path.join(data_dir, 'train')
    create_directories([train_dir])
    with open('filenames_training.txt', 'rb') as fp:
        filenames_training = pickle.load(fp)
    for filename in filenames_training:
        shutil.move(os.path.join(data_dir, filename), os.path.join(train_dir, filename))
    
    val_dir = os.path.join(data_dir, 'val')
    create_directories([val_dir])
    with open('filenames_validation.txt', 'rb') as fp:
        filenames_validation = pickle.load(fp)
    for filename in filenames_validation:
        shutil.move(os.path.join(data_dir, filename), os.path.join(val_dir, filename))
    
    
    test_dir = os.path.join(data_dir, 'test')
    create_directories([test_dir])
    with open('filenames_test.txt', 'rb') as fp:
        filenames_test = pickle.load(fp)
    for filename in filenames_test:
        shutil.move(os.path.join(data_dir, filename), os.path.join(test_dir, filename))
    

if __name__ == "__main__": 
    parser = argparse.ArgumentParser(description='Split data into training / validation / testing')
    parser.add_argument('--data_dir', required=True,
                        help='data directory')
    args = parser.parse_args()

    logger = get_module_logger(__name__)
    logger.info('Creating splits...')
    split(args.data_dir)

