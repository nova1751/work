#!/user/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_excel('input.xlsx')
count = pd.DataFrame(df.loc[:, '目标'].value_counts())
count1 = count.drop(['（空）'])
count2 = count1.sort_index()
count2.to_excel('output.xlsx')
