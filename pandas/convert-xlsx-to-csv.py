import pandas as pd

def main():
    data = pd.read_excel('GNS_Config_Standard_IOS_Template.xlsx', sheet_name=None)
    for sheet_name, df in data.items():
        df.to_csv(f'sheets/{sheet_name}.csv')

if __name__ == "__main__":
    main()
