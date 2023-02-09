# CPANLP🎺: Certified Public Accountant Natural Language Processing toolkit
### Talk is cheap ,show me the code
Narrating Accounting using Python
- sales increased 12% compared with fourth quarter 2021:
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

[![PyPI - Python Version](https://img.shields.io/static/v1?label=pypi&message=v1.1.29&color=blue)](https://pypi.org/project/cpanlp/)
[![Downloads](https://static.pepy.tech/badge/cpanlp/week)](https://pepy.tech/project/cpanlp)

## Install & Import 安装和导入
For detailed installation instructions, see the
[documentation](https://cpanlp.com/documentation).
```python
pip install cpanlp
import cpanlp as p
```

## Features 主要功能
1. Get Report 今日财报
```python
df = p.gettoday()
```
|    | 标题                                               |   证券代码 | 证券简称   | 网址                                                            | 日期       |   id |
|---:|:---------------------------------------------------|-----------:|:-----------|:----------------------------------------------------------------|:-----------|-----:|
|  0 | 唐源电气：国金证券关于唐源电气2022年度现场检查报告 |     300789 | 唐源电气   | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519757.PDF | 2023-01-03 |    1 |

```python
report = p.getreport(df.iloc[0, 3])
```
2. Accounting Item 会计科目
```python
gold_asset = p.Asset(account="gold", debit=1000,date="2023-01-01")
print(gold_asset.bubble)
```
3. Information Asymmetry 信息不对称
```python
info = p.AsymmetricInformation(sender="investor", receiver="company_A", message="I am very interested in investing in your business", hidden_information="I have a limited budget")
info.get_advantage()
```
4. Entrepreneur 企业家
```python
john = p.Entrepreneur(name="John Smith",age=30,wealth=100000,utility_function=0, experience=5,company=LLC("Apple","Electronics",1000000),entrepreneurship=Entrepreneurship(leadership=9.0))
john.strive_for_excellence()
```
5. Strategy 策略
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

## Finance Exception 会计异常:
```python
if abs(percent_change) > 10:
  raise AbnormalFluctuation(stock_name, percent_change)
```

## Module 主要模块:
- [x] **Abnormal 异象**：`Winner Curse赢者诅咒`，`Bubble泡沫`
- [x] **Accounting Account 会计科目**：`Asset资产`，`Liability负债`，`Equity所有者权益`，`Income收入`，`Cashflow现金流`
- [x] **Business 业务**：`MainBusiness主营业务`
- [x] **Contract 合约**：`Lease租约`，`Loan Contract借贷合同`，`Labor Contract劳动合同`，`Financial Instrument金融工具`
- [x] **Control 控制**：`Voting Power 投票权`，`Commodity Control商品控制权`，`Significant Influence重大影响`
- [x] **Culture 文化**：`Entrepreneurship企业家精神`，`Craftsmanship工匠精神`
- [x] **Department 部门**：`Board Of Directors董事会`
- [x] **Entity 实体**： `LLC(Limited Liability Company)有限责任公司`，`Partnership合伙企业`，`Public  Company公众企业`，`SME(Small and medium-sized enterprises)中小企业`，`Conglomerate 集团`
- [x] **Environment 环境**：`EconomicEnvironment并购`，`IndustryEnvironment行业环境`，`CreditEnvironment信用环境`
- [x] **Event 事件**：`Acquisition并购`，`Certification认证`，`Meeting会议`，`Resignation离职`，`Repurchase回购`，`Registration注册`，`Lawsuit诉讼`，`StockHoldingIncrease增持`
- [x] **Information 信息**：`Signal信号`，`Speculative Information投机信息`，`Asymmetric Information不对称信息`，`Incentive激励`
- [x] **Incentive 激励**
- [x] **Institution 制度**
- [x] **Person 个体**：${\color{red}Consumer消费者}$，`Employee员工`，`Entrepreneur企业家`，`Manager经理`，`Investor投资人`，`Partner合伙人`，`Shareholder股东`，`Supervisor监管者`，`Creditor债权人`，`Auditor审计`，`Beneficiary受益人`，`Fiduciary受托人`，`Craftsman工匠`
- [x] **Market 市场**：`Commodity货物`，`Goods商品`，`Market Structure市场结构`
- [x] **Policy 政策**：`AccountingPolicy会计政策`，`DividendPolicy股利政策`
- [x] **Project 项目**
- [x] **Pragmatics 语用**：`Promise承诺`
- [x] **Risk 风险**
- [x] **StakerHolder 利益相关者**：`Bank银行`，`Government政府`，`Media媒体`，`Public公众`，`Rating Agency评级机构`
- [x] **Scheme 图示**：`Ponzi Scheme庞氏骗局`，`ESOP员工持股`，`DebtRestructuringPlan债务重组`
- [x] **Strategy 战略**：`Long Term Strategy长期策略`，`Financial Strategy财务策略`
- [x] **Tax 税法**：`VAT(Value-Added Tax)增值税`，`Consumption Tax消费税`，`Personal Income Tax个人所得税`，`Corporate Income Tax企业所得税`，`RealEstate Tax房产税`，`TransactionTax印花税`
- [x] **Team 团队**：
- [x] **Utility 效用**：

## Accounting Gym-Env 会计强化学习环境
<a href="https://pypi.org/project/cpagym/">
<img src="https://raw.githubusercontent.com/accounting-intelligent-ai/cpagym/main/cpagym.png" width = "200" height = "200" alt="logo" align=center />
</a>

Check out: https://cpanlp.com