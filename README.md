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
这个时代叫做AI，我们是北外智能会计博士课题组，致力推动具有**经济学基础的会计学的语言学转向**(**The Linguistic Turn of Accounting on Economic Basis**)。


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

## Features 主要功能
1. Get Report 今日财报
```python
df = cp.gettoday()
```
|    | 标题                                               |   证券代码 | 证券简称   | 网址                                                            | 日期       |   id |
|---:|:---------------------------------------------------|-----------:|:-----------|:----------------------------------------------------------------|:-----------|-----:|
|  0 | 唐源电气：国金证券关于唐源电气2022年度现场检查报告 |     300789 | 唐源电气   | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519757.PDF | 2023-01-03 |    1 |

```python
report = cp.getreport(df.iloc[0, 3])
```
2. Accounting Item 会计科目
```python
gold_asset = cp.Asset(account="gold", debit=1000,date="2023-01-01")
print(gold_asset.bubble)
```
3. Information Asymmetry 信息不对称
```python
info = cp.AsymmetricInformation(sender="investor", receiver="company_A", message="I am very interested in investing in your business", hidden_information="I have a limited budget")
info.get_advantage()
```
4. Entrepreneur 企业家
```python
john = cp.Entrepreneur(name="John Smith",age=30,wealth=100000,utility_function=0, experience=5,company=LLC("Apple","Electronics",1000000),entrepreneurship=Entrepreneurship(leadership=9.0))
john.strive_for_excellence()
```
5. Strategy 策略
```python
huawei = cp.FinancialStrategy("huawei","defense",poison_pill(1000,0.1))
```

## MODULE 主要模块:
- [x] **Accounting Account 会计科目**：`Asset资产`，`Liability负债`，`Equity所有者权益`，`Income收入`，`Cashflow现金流`
- [x] **Legal Entity 法律实体**： `LLC(Limited Liability Company)有限责任公司`，`Partnership合伙企业`，`Public  Company公众企业`，`SME(Small and medium-sized enterprises)中小企业`
- [x] **StakerHolder 利益相关者**：`Bank银行`，`Government政府`，`Media媒体`，`Public公众`，`Rating Agency评级机构`，
- [x] **Person 个体**：${\color{red}Consumer消费者}$，`Employee员工`，`Entrepreneur企业家`，`Manager经理`，`Investor投资人`，`Partner合伙人`，`Shareholder股东`，`Supervisor监管者`，`Creditor债权人`，`Auditor审计`，`Beneficiary受益人`，`Fiduciary受托人`，`Craftsman工匠`
- [x] **Market 市场**：`Commodity商品`，`Bubble泡沫`，`Perfectly Competitive Market完全竞争市场`，`Monopoly Market垄断市场`，`Oligopoly Market寡头垄断市场`
- [x] **Conglomerate 集团**：`Associate Company联营公司`，`Joint Venture合营公司`，`Subsidiary子公司`
- [x] **Department 部门**：`Board Of Directors董事会`
- [x] **Event 事件**：`Acquisition并购`
- [x] **Institution 制度**
- [x] **Policy 政策**：`Acquisition并购`
- [x] **Contract 合约**：`Lease租约`，`Loan Contract借贷合同`，`Labor Contract劳动合同`，`Financial Instrument金融工具`
- [x] **Information 信息**：`Signal信号`，`Speculative Information投机信息`，`Asymmetric Information不对称信息`，`Incentive激励`
- [x] **Risk 风险**
- [x] **Scheme 图示**：`Ponzi Scheme庞氏骗局`
- [x] **Control 控制**：`Voting Power 投票权`，`Commodity Control商品控制权`，`Significant Influence重大影响`
- [x] **Culture 文化**：`Entrepreneurship企业家精神`，`Craftsmanship工匠精神`
- [x] **Strategy 战略**：`Long Term Strategy长期策略`，`Financial Strategy财务策略`
- [x] **Tax 税法**：`VAT(Value-Added Tax)增值税`，`Consumption Tax消费税`，`Personal Income Tax个人所得税`，`Corporate Income Tax企业所得税`，`RealEstate Tax房产税`，`TransactionTax印花税`
- [x] **Abnormal 异象**：`Winner Curse赢者诅咒`

## Accounting Gym-Env 配套的智能会计强化学习虚拟环境
<a href="https://pypi.org/project/cpagym/">
<img src="https://raw.githubusercontent.com/accounting-intelligent-ai/cpagym/main/cpagym.png" width = "200" height = "200" alt="logo" align=center />
</a>

Check out: https://cpanlp.com