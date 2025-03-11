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
import numpy as np
import os
from tkinter import filedialog
import tkinter as tk
from pprint import pprint

# def open_dialog():
#     file = filedialog.askopenfilename()
#     return file
# input_file = open_dialog()

input_folder = r"C:\Users\admin\Downloads\all_uk_products\big_files"

# try:
#     os.makedirs(output_path)
# except:
#     print('Directory already exist')

for file in os.listdir(input_folder):
    input_file = os.path.join(input_folder, file)
    brand_name = (file.split('/')[-1].split(' - '))[0].replace('.csv', '')
    file_name = (file.split('/')[-1]).replace('.csv', '')

    output_path = f'./Output/{brand_name}'
    output_path = r"C:\Users\admin\Downloads\all_uk_products\split_files"
    print(input_file)
    file_size = pd.read_csv(input_file)['Title']
    # Calculate the number of rows
    # Calculate the number of rows
    total_rows = len(file_size)

    # Determine the split points
    split_points = np.linspace(0, total_rows, num=3, dtype=int)[1:]  # We need 3 split points

    # Convert to a list
    split_row = split_points.tolist()
    empty_row = True

    new_split = []
    for i in range(len(split_row)):
        while empty_row:
            if pd.isna(file_size.iloc[split_row[i] - 1]):
                
                new_split_row = split_row[i] + 1
                new_split_row_2 = split_row[i + 1] + 1
                split_row[i] = new_split_row

                split_row[i + 1] = new_split_row_2

            else:
                empty_row = False

        if i < len(split_row) - 1:      
            split_row[i] -= 1

            split_row[i + 1] -= 1

    # pprint(file_size[split_row[0]:split_row[1]])
    # print(split_row)


    df = pd.read_csv(f'{input_file}', encoding='utf-8-sig')
    start_index = 0

    # Loop over the split indices to create each split
    for i, end_index in enumerate(split_row):
        # If it's the last index in split_indices, include all remaining rows
        if i == len(split_row) - 1:
            split_df = df[start_index:]
        else:
            split_df = df[start_index:end_index]
        
        # Save the split DataFrame to a new CSV file, including the header
        new_file = output_path + f'/{file_name} Batch_' + str(i+1) + '.csv'
        split_df.to_csv(new_file, index=False)
        
        # Update the start index for the next split
        start_index = end_index