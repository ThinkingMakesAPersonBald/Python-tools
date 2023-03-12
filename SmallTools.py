import os
import pandas as pd

root_path = '/Users/peixinhua/Downloads'

df_list = []
def main():
    for f in os.listdir(root_path):
        if '.xlsx' in f:
            df = pd.read_excel(os.path.join(root_path,f))
            df_list.append(df)
    merge_df = pd.concat(df_list)
    dpd_list = [1,2,3]
    day_list = ['2022-09-01','2022-09-02','2022-09-03','2022-09-04','2022-09-05','2022-09-06',
    '2022-10-01','2022-10-02','2022-10-03','2022-10-04','2022-10-05','2022-10-06',
    '2022-11-01','2022-11-02','2022-11-03','2022-11-04','2022-11-05','2022-11-06']
    for dpd in dpd_list:
        temp_df = merge_df[merge_df['DPD'] == dpd]
        for day in day_list:
            day_df = temp_df[temp_df['day'] == day]
            calculate_line_data(day_df,dpd=dpd,day=day)
            print(dpd,day)
    # dpd1_df = merge_df[merge_df['DPD'] == 1]
    # day_df = dpd1_df[dpd1_df['day'] == '2022-10-01']
    # calculate_line_data(day_df)
    # print(day_df)

def calculate_line_data(df: pd.DataFrame,dpd: int,day: str):
    df['list_total'] = df['total_calls'].sum()
    df['list_line_rate'] = df['total_calls'] / df['list_total']
    df['line_connect_rate'] = df['connected_rate'] * df['list_line_rate']
    df.sort_values(by='total_calls',ascending=True)
    df.to_excel(os.path.join(root_path,'Akulaku' + str(dpd) + "/" + day  + "_output.xlsx"))

if __name__ == "__main__":
    main()
