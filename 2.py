import pandas as pd
import numpy as np

df = pd.read_table('inputs/2.txt', header=None, sep=' ')

df['play'] = np.where((df[1] == 'X') & (df[0] == 'A'), 'Z',
                    np.where((df[1] == 'X') & (df[0] == 'B'), 'X',
                    np.where((df[1] == 'X') & (df[0] == 'C'), 'Y',
                    np.where((df[1] == 'Y') & (df[0] == 'A'), 'X',
                    np.where((df[1] == 'Y') & (df[0] == 'B'), 'Y',
                    np.where((df[1] == 'Y') & (df[0] == 'C'),'Z',
                    np.where((df[1] == 'Z') & (df[0] == 'A'), 'Y',
                    np.where((df[1] == 'Z') & (df[0] == 'B'), 'Z', 'X')))))
)))

df['points'] = np.where(df[1] == 'X', 1, np.where(df[1] == 'Y', 2, 3))

df['result'] = np.where((df[1] == 'X') & (df[0] == 'C') |
                        (df[1] == 'Y') & (df[0] == 'A') |
                        (df[1] == 'Z') & (df[0] == 'B'), 6,
                        np.where((df[1] == 'X') & (df[0] == 'A') |
                            (df[1] == 'Y') & (df[0] == 'B') |
                            (df[1] == 'Z') & (df[0] == 'C'), 3, 0
))

df['adjusted_points'] = np.where(df['play'] == 'X', 1, np.where(df['play'] == 'Y', 2, 3))

df['adjusted_result'] = np.where((df['play'] == 'X') & (df[0] == 'C') |
                        (df['play'] == 'Y') & (df[0] == 'A') |
                        (df['play'] == 'Z') & (df[0] == 'B'), 6,
                        np.where((df['play'] == 'X') & (df[0] == 'A') |
                            (df['play'] == 'Y') & (df[0] == 'B') |
                            (df['play'] == 'Z') & (df[0] == 'C'), 3, 0
))

print(df.head())

print(f"\nFirst result: {df['points'].sum() + df['result'].sum()}")
print(f"Second result: {df['adjusted_points'].sum() + df['adjusted_result'].sum()}")

