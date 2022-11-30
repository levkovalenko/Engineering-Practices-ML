import ast
import numpy as np
import pandas as pd


def ast_print(node: ast.Module):
    print(ast.dump(node, indent=4))

points = np.genfromtxt('https://raw.githubusercontent.com/danielgribel/hg-means/master/data/page.txt', skip_header=1)


def get_data_lr():
    bank_df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSGfjG4mq1_4HS4iwRN7EZK6YHzPDi8HpB_giY7kiqbDZRsRNjbfhuQ2J6xkHGk1YVYN9H0TxOf2tgw/pub?gid=1909291157&single=true&output=csv')
    bank_df.drop(columns=['ID', 'ZIP_Code'], inplace=True)

    bank_df['Education'] = bank_df['Education'].astype('category')
    new_categories = {1: 'Undergrad', 2: 'Graduate', 3: 'Advanced/Professional'}
    bank_df.Education.cat.rename_categories(new_categories, inplace=True)
    bank_df = pd.get_dummies(bank_df, prefix_sep='_', drop_first=True)
    y = bank_df['Personal_Loan']
    X = bank_df.drop(columns=['Personal_Loan'])
    return X.astype("int32"), y