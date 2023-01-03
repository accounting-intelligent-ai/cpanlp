# Project description
CPANLP: Certified Public Accountant Natural Language Processing toolkit

注册会计师的自然语言包，做最好的会计自然语言处理组件

Redefining [Accounting](https://cpanlp.com/overview/redefine)!
Developed by **Bfsu Intelligent Accounting Team** (c) 2023
Github:https://github.com/accounting-intelligent-ai/cpanlp

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
|    | mch                                                                                                                            |   zhqdm | zhqjc    | ggbh                                                            | name   | riqi       |   id |
|---:|:-------------------------------------------------------------------------------------------------------------------------------|--------:|:---------|:----------------------------------------------------------------|:-------|:-----------|-----:|
|  0 | 唐源电气：国金证券关于唐源电气2022年度现场检查报告                                                                             |  300789 | 唐源电气 | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519757.PDF |        | 2023-01-03 |    1 |
|  1 | 唐源电气：关于购买理财产品的进展公告                                                                                           |  300789 | 唐源电气 | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519756.PDF |        | 2023-01-03 |    2 |
|  2 | 科拓生物：北京科拓恒通生物技术股份有限公司向特定对象发行股票发行情况报告书                                                     |  300858 | 科拓生物 | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519729.PDF |        | 2023-01-03 |    3 |
|  3 | 科拓生物：北京市君致律师事务所关于北京科拓恒通生物技术股份有限公司2022年向特定对象发行股票发行过程和认购对象合规性的法律意见书 |  300858 | 科拓生物 | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519727.PDF |        | 2023-01-03 |    4 |
|  4 | 科拓生物：关于签订募集资金三方监管协议的公告                                                                                   |  300858 | 科拓生物 | http://static.cninfo.com.cn/finalpage/2023-01-03/1215519725.PDF |        | 2023-01-03 |    5 |

Check out: https://cpanlp.com