import os
import pandas as pd
import numpy as np

root_direct = '/Users/peixinhua/Downloads/Garbage line selection'
output_folder = os.path.join(root_direct,'output')

def main():
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for f in os.listdir(root_direct):
        if '.xlsx' in f:
            data_df = pd.read_excel(os.path.join(root_direct,f))
            filter_output_data(data_df,f)

def filter_output_data(df: pd.DataFrame,f: str):
    temp_df = df[df['total_calls'] > 1000]
    connected_rate_average = temp_df['connected_rate'].mean()
    print(connected_rate_average)
    print(df['connected_rate'])
    print(np.where(df['connected_rate'] < connected_rate_average,1,0))
    df['new'] = np.where(df['connected_rate'] < connected_rate_average,1,0)
    df.to_excel(os.path.join(output_folder,f.split('.')[0] + '_' + 'output.xlsx'))

if __name__ == "__main__":
    main()