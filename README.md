# CPANLP: Certified Public Accountant Natural Language Processing toolkit

### 给您拜年了 Happy 🐰 Year
```python
def Happy 🐰 Year():
    wishes = ["新年快乐！兔年大吉！", "天天开心，身体健康！", "全家幸福，事事顺心！"]
    happy_asset = Happy_New_Year_Asset("Everybody","2023-01-22",0.005,wishes)
    happy_asset.add_wishes(wishes)
    happy_asset.amortize(1)
    happy_person = happy_asset.account
    happy_income = happy_asset.amortization_history[0][1]
    print(happy_person,"新年第一天的幸福：",happy_income,"😄") 
if __name__ == '__main__':
    Happy 🐰 Year()
```
[![](https://raw.githubusercontent.com/accounting-intelligent-ai/cpanlp/main/cpanlp.png)](https://cpanlp.com)


We are the accounting-intelligent-ai Team of Beijing Foreign Studies University. We develop A package for intelligent certified accountants.
这个时代叫做AI，我们是北外智能会计博士课题组，致力推动具有`经济学基础的会计学的语言学转向`(**The Linguistic Turn of Accounting on Economic Basis**)`。


Redefining [Accounting](https://cpanlp.com/overview/redefine)!
Developed by **Bfsu Intelligent Accounting Team** (c) 2023
[Github](https://github.com/accounting-intelligent-ai/cpanlp)

[![PyPI - Python Version](https://img.shields.io/static/v1?label=pypi&message=v1.0.1&color=blue)](https://pypi.org/project/cpanlp/)
[![Downloads](https://static.pepy.tech/badge/cpanlp/week)](https://pepy.tech/project/cpanlp)

## Install & Import 安装和导入
For detailed installation instructions, see the
[documentation](https://cpanlp.com/documentation).
```python
pip install cpanlp
import cpanlp as cp
```

## Features主要功能
1. Get Report今日财报
```python
df = cp.gettoday()
```
|    | 标题                                               |   证券代码 | 证券简称   | 网址                                                            | 日期       |   id |
|---:|:---------------------------------------------------|-----------:|:-----------|:----------------------------------------------------------------|:-----------|-----:|
|  0 | 唐源电气：国金证券关于唐源电气2022年度现场检查报告 |     300789 | 唐源电气   | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519757.PDF | 2023-01-03 |    1 |

```python
report = cp.getreport(df.iloc[0, 3])
```
2. Accounting Item会计科目
```python
gold_asset = cp.Asset(account="gold", debit=1000,date="2023-01-01")
print(gold_asset.bubble)
```
3. Information Asymmetry信息不对称
```python
info = cp.AsymmetricInformation(sender="investor", receiver="company_A", message="I am very interested in investing in your business", hidden_information="I have a limited budget")
info.get_advantage()
```
4. Entrepreneur企业家
```python
john = cp.Entrepreneur(name="John Smith",age=30,wealth=100000,utility_function=0, experience=5,company=LLC("Apple","Electronics",1000000),entrepreneurship=Entrepreneurship(leadership=9.0))
john.strive_for_excellence()
```
5. Strategy策略
```python
huawei = cp.FinancialStrategy("huawei","defense",poison_pill(1000,0.1))
```

Check out: https://cpanlp.com