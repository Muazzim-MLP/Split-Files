# Author: Darren Ting, darren@mlperformance.co.uk
# Date Created: 03/08/2023
# Last Updated: 03/08/2023

# File Descriptions

#########################################################################################################################
##                                                                                                                     ##
## This code will split the csv based on your need, initially deisgn for 5000 single variant product                   ##
##                                                                                                                     ##
##                                                                                                                     ##
#########################################################################################################################

import pandas as pd
import math
import os
from tkinter import filedialog
import tkinter as tk

def open_dialog():
    file = filedialog.askopenfilename()
    return file
input_file = open_dialog()

brand_name = (input_file.split('/')[-1].split(' - '))[0].replace('.csv', '')
file_name = (input_file.split('/')[-1]).replace('.csv', '')

output_path = f'./Output/{brand_name}'

try:
    os.makedirs(output_path)
except:
    print('Directory already exist')

def to_csv_batch(src_csv, dst_dir, file_name, size, index=False):
    # Read source CSV
    df = pd.read_csv(src_csv, encoding='utf-8-sig')
    low, high = 0, size 
    if len(df) > size:
        # Loop through batches
        for i in range(math.ceil(len(df) / size)):
            fname = dst_dir+ f'/{file_name} Batch_' + str(i+1) + '.csv'
            df[low:high].to_csv(fname, index=index)                     
            # Update selection
            low = high
            if (high + size < len(df)):
                high = high + size
            else:
                high = len(df)
    else: 
        pass
    return (f'Done split {src_csv} into {i} file')

file_size = pd.read_csv(input_file, encoding='ISO-8859-1')

if len(file_size) > 800000:
    smaller_dir = f'{output_path}'    
    isExist = os.path.exists(smaller_dir)    
    if not isExist:
        os.makedirs(smaller_dir)        
    to_csv_batch(f'{input_file}', smaller_dir, file_name, 4000)

