# CPANLP: Certified Public Accountant Natural Language Processing toolkit

[![](https://raw.githubusercontent.com/accounting-intelligent-ai/cpanlp/main/cpanlp.png)](https://cpanlp.com)


We are the accounting-intelligent-ai Team of Beijing Foreign Studies University. We develop A package for intelligent certified accountants.
这个时代叫做AI，我们是北外智能会计博士课题组，致力推动具有经济学基础的会计学的语言学转向(**The Linguistic Turn of Accounting on Economic Basis**)。


Redefining [Accounting](https://cpanlp.com/overview/redefine)!
Developed by **Bfsu Intelligent Accounting Team** (c) 2023
[Github](https://github.com/accounting-intelligent-ai/cpanlp)

[![PyPI - Python Version](https://img.shields.io/static/v1?label=pypi&message=v1.0.35&color=blue)](https://pypi.org/project/cpanlp/)
[![Downloads](https://static.pepy.tech/badge/cpanlp/week)](https://pepy.tech/project/cpanlp)

## Install安装说明
For detailed installation instructions, see the
[documentation](https://cpanlp.com/documentation).
```python
pip install cpanlp
```

## Features主要功能
1.Get Report今日财报
```python
import cpanlp as cp
df = cp.gettoday()
```
|    | 标题                                               |   证券代码 | 证券简称   | 网址                                                            | 日期       |   id |
|---:|:---------------------------------------------------|-----------:|:-----------|:----------------------------------------------------------------|:-----------|-----:|
|  0 | 唐源电气：国金证券关于唐源电气2022年度现场检查报告 |     300789 | 唐源电气   | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519757.PDF | 2023-01-03 |    1 |

```python
report = cp.getreport(df.iloc[0, 3])
```

2.Accounting Item会计科目
```python
import cpanlp as cp
gold_asset = cp.Asset(account="gold", debit=1000,date="2023-01-01")
print(gold_asset.bubble)
```

3.Information Asymmetry信息不对称
```python
import cpanlp as cp
info = cp.AsymmetricInformation("investor", "company_A", "I am very interested in investing in your business", "I have a limited budget")
info.get_advantage()
```

4.Entrepreneur企业家
```python
import cpanlp as cp
john = cp.Entrepreneur("John Smith",30, 5,LLC("Apple","Electronics",1000000))
john.strive_for_excellence()
```
Check out: https://cpanlp.com