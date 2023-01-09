[![](https://raw.githubusercontent.com/accounting-intelligent-ai/cpanlp/main/cpanlp.png)](https://cpanlp.com)

CPANLP: Certified Public Accountant Natural Language Processing toolkit

We are the accounting-intelligent-ai Team of Beijing Foreign Studies University. We develop A package to drive the linguistic turn of accounting.我们是北外智能会计团队，开发了这套智能会计python组件，助力会计的语言学转向。

Redefining [Accounting](https://cpanlp.com/overview/redefine)!
Developed by **Bfsu Intelligent Accounting Team** (c) 2023
[Github](https://github.com/accounting-intelligent-ai/cpanlp)

[![PyPI - Python Version](https://img.shields.io/static/v1?label=pypi&message=v1.0.19&color=blue)](https://pypi.org/project/cpanlp/)
## 特点

## 安装说明
```python
pip install cpanlp
```

## 主要功能
1.获取今日财报
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

2.模拟会计科目
```python
import cpanlp as cp
资产1 = cp.Asset(account="黄金", debit=1000,date="2023-01-01")
资产1.makemoney()
```
Check out: https://cpanlp.com