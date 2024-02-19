import numpy as np
import struct
import os
import pandas as pd
import matplotlib.pyplot as plt


# Function to sample a smaller dataset from a larger dataset
# instance_size: the size of output dataset would be
# input_df: the dataset will be sampled (the larger dataset)
# index: the number of the smaller dataset would be (can be used to sample multiple small dataset)
def instance_gene(instance_size, input_df, index):
    inst_gene = input_df.sample(n=instance_size)
    
    # filePath: output file path (user may change it by preference)
    # fileName: output file name (user may change it by preference)
    filePath = 'problem_instance/'
    fileName = 'instance-' + str(index) + '-' + str(instance_size) + '.csv'
    completeFileName = os.path.join(filePath, fileName)
    
    inst_gene.to_csv(completeFileName, index_label=labels, index=False)
    return inst_gene

def main():
    # instance_sizes: output dataset size(user may change it by preference)
    # geo_df: input dataset information (user may change it by preference/need)
    instance_sizes = [120, 100, 80, 60]
    geo_df = pd.read_excel(r'PR_DATA.xlsx')
    
    # main loop to to sample a sequence of smaller datasets from a larger dataset
    for i in range(5):
        input_instance = geo_df
        for ele in instance_sizes:
            output_instance = instance_gene(ele, input_instance, i)
            input_instance = output_instance

if __name__ == "__main__":
    main()

