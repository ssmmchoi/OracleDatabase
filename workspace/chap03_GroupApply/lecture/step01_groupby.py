# -*- coding: utf-8 -*-
"""
DataFrame 객체 대상 그룹화
 - 형식) DF.groupby('집단변수').수학/통계함수()
"""

import pandas as pd
tips = pd.read_csv("C:/ITWILL/Work/4_Python-II/data/tips.csv")
tips.info()
tips.head()


