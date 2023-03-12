import os
import pandas as pd 

root_path = "/Users/peixinhua/Downloads"
file_name = 'key_step_route_repayment_rate.xlsx'

def load_file_data():
    original_df = pd.read_excel(os.path.join(root_path,file_name))
    original_df['step_route'] = original_df['step_route'].apply(lambda x: string_handle(x))
    output_path = os.path.join(root_path,'output.xlsx')
    original_df.to_excel(output_path)

def string_handle(character: str):
    character_list = character.split('-')
    concatenage_str = ''
    for item in character_list:
        if  not 'checkpoint' in item:
            concatenage_str = concatenage_str + '-' + item
    return concatenage_str

def main():
    load_file_data()

if __name__ == '__main__':
    main()