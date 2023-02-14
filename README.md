# CPANLP🎺: Certified Public Accountant talks just Like a Coder
### Talk is cheap ,show me the code
#### Narrating Accounting using Python Example from amazon financial report

sales increased 12% compared with fourth quarter 2021:
  - North America segment sales increased 13% year-over-year to $93.4 billion, or increased 14% excluding changes in foreign exchange rates.
  - International segment sales decreased 8% year-over-year to $34.5 billion, or increased 5% excluding changes in foreign exchange rates.
  - AWS segment sales increased 20% year-over-year to $21.4 billion.
```python
sale1 = p.Sale(quarter="Q4",amount=93.4,unit="billion dollars",growth_rate=13%,year=2022,segment="North America")
sale2 = p.Sale(quarter="Q4",amount=34.5,unit="billion dollars",growth_rate=-8%,year=2022,segment="International")
sale3 = p.Sale(quarter="Q4",amount=21.4,unit="billion dollars",growth_rate=20%,year=2022,segment="AWS")
sales = [sale1, sale2, sale3]
total_sales = 0
for s in sales:
    total_sales += s.amount
    print(f"Segment: {s.segment}, Sale: {s.amount}")

print(f"Total Sales: {total_sales}")
```

<a href="https://cpanlp.com">
<img src="https://raw.githubusercontent.com/accounting-intelligent-ai/cpanlp/main/cpanlp.png" width = "250" height = "80" alt="logo" align=center />
</a>

Narrating [Accounting](https://cpanlp.com/overview/redefine)! using Python
Developed by **Cpanlp Intelligent Accounting Team** (c) 2023
[Github](https://github.com/accounting-intelligent-ai/cpanlp)

[![PyPI - Python Version](https://img.shields.io/static/v1?label=pypi&message=v1.2.26&color=blue)](https://pypi.org/project/cpanlp/)
[![Downloads](https://static.pepy.tech/badge/cpanlp/week)](https://pepy.tech/project/cpanlp)

## Install & Import 安装和导入
#### Dependencies
- scipy 
- numpy
- pandas
  
For detailed installation instructions, see the
[documentation](https://cpanlp.com/documentation).
```python
pip install cpanlp
import cpanlp as p
```

## Features 主要功能
1. Accounting Item 会计科目
```python
gold_asset = p.Asset(account="gold", debit=1000,date="2023-01-01")
print(gold_asset.bubble)
```
2. Information Asymmetry 信息不对称
```python
info = p.AsymmetricInformation(sender="investor", receiver="company_A", message="I am very interested in investing in your business", hidden_information="I have a limited budget")
info.get_advantage()
```
3. Entrepreneur 企业家
```python
john = p.Entrepreneur(name="John Smith",age=30,wealth=100000,utility_function=0, experience=5,company=LLC("Apple","Electronics",1000000),entrepreneurship=Entrepreneurship(leadership=9.0))
john.strive_for_excellence()
```
4. Strategy 策略
```python
huawei = p.FinancialStrategy("huawei","defense",poison_pill(1000,0.1))
```

## Accounting Language Decorator 会计语言装饰器:
```python
@prob(probability=0.7) #Estimate 估计

@future_tense #Future Tense 将来时态

side_effects=["financial instability","loss of reputation","decreased employee morale"]
@with_side_effects(side_effects=side_effects)#Side Effects 副作用
```

## Accounting Exception 会计异常:
```python
if abs(percent_change) > 10:
  raise AbnormalFluctuation(stock_name, percent_change)
```

## Module 主要模块:
|  Module   | Content  |
|  :----:  | :----:  |
| **Abnormal 异象**  | `Winner Curse赢者诅咒`，`Bubble泡沫`|
| **Accounting Account 会计科目**  | `Asset资产`，`Liability负债`，`Equity所有者权益`，`Income收入`，`Cashflow现金流` |
| **Business 业务**  | `Main Business主营业务`，`Capacity产能` |
| ${\color{blue}Contract合约}$  | `Agreement协议`，`Arrangement安排`，`MOU备忘录`，`Commitment Letter承诺函`，`Lease租约`，`Loan Contract借贷合同`，`Labor Contract劳动合同`，`Financial Instrument金融工具` |
| **Control 控制**  | `Voting Power 投票权`，`Commodity Control商品控制权`，`Significant Influence重大影响` |
| **Culture 文化**  | `Entrepreneurship企业家精神`，`Craftsmanship工匠精神`，`Business Philosophy经营哲学` |
| ${\color{purple}Decorator装饰器}$| `Estimate预测` ，`Tense时态`，`Importance重要性`，`With Effects副作用`，`Validator验证`|
| **Department 部门**  | `Board Of Directors董事会` ，`Supervisory Board监事会`|
| **Economic System 经济系统** |  `Digital Economy数字经济` ，`Physical Economy实体经济` ，`Market Economy市场经济`，`Planned  Economy计划经济` |
| **Entity 实体**  | `LLC(Limited Liability Company)有限责任公司`，`Partnership合伙企业`，`Public  Company公众企业`，`SME(Small and medium-sized enterprises)中小企业`，`Conglomerate 集团` |
| **Environment 环境**  | `Economic Environment经济环境`，`Industry Environment行业环境`，`Credit Environment信用环境`，`Market Environment市场环境`|
| **Event 事件**  | `Acquisition并购`，`Certification认证`，`Grants补助`，`Meeting会议`，`Resignation离职`，`Repurchase回购`，`Personnel人事`，`Registration注册`，`Shares股份`，`Lawsuit诉讼`，`StockHoldingIncrease增持` |
| ${\color{purple}Exception异常}$| `Abnormal Fluctuation异常波动`，`Bubble泡沫`，`Winner Curse赢者诅咒`|
| **Information 信息**  | `Signal信号`，`Speculative Information投机信息`，`Asymmetric Information不对称信息` |
| **Incentive 激励**  |   |
| **Institution 制度**  |  |
| **Market 市场**  | `Commodity货物`，`Goods商品`，`Market Structure市场结构`|
| **Person 个体**  | ${\color{red}Consumer消费者}$，`Employee员工`，`Entrepreneur企业家`，`Manager经理`，`Investor投资人`，`Partner合伙人`，`Shareholder股东`，`Supervisor监管者`，`Creditor债权人`，`Auditor审计`，`Beneficiary受益人`，`Fiduciary受托人`，`Craftsman工匠` |
| **Policy 政策**  | `AccountingPolicy会计政策`，`DividendPolicy股利政策` |
| **Project 项目**  |  |
| **Pragmatics 语用**  | `Promise承诺` |
| **Risk 风险** | |
| **StakerHolder 利益相关者**  | `Bank银行`，`Government政府`，`Media媒体`，`Public公众`，`Rating Agency评级机构` |
| **Scheme 图示**  | `Ponzi Scheme庞氏骗局`，`ESOP员工持股`，`DebtRestructuringPlan债务重组` |
| **Strategy 战略**  | `Long Term Strategy长期策略`，`Financial Strategy财务策略` |
| **Tax 税法**  | `VAT(Value-Added Tax)增值税`，`Consumption Tax消费税`，`Personal Income Tax个人所得税`，`Corporate Income Tax企业所得税`，`RealEstate Tax房产税`，`TransactionTax印花税` |
| **Team 团队**  |  |
| **Utility 效用**  | |

## Accounting Gym-Env 会计强化学习环境
<a href="https://pypi.org/project/cpagym/">
<img src="https://raw.githubusercontent.com/accounting-intelligent-ai/cpagym/main/cpagym.png" width = "200" height = "200" alt="logo" align=center />
</a>

Check out: https://cpanlp.com