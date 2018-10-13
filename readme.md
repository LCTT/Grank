# Grank -  Github 项目活跃度分析工具

[![GitHub forks](https://img.shields.io/github/forks/lctt/grank.svg?style=for-the-badge&label=Fork)](https://github.com/lctt/grank/) [![GitHub stars](https://img.shields.io/github/stars/lctt/grank.svg?style=for-the-badge&label=Stars)](https://github.com/lctt/grank/) [![GitHub tag](https://img.shields.io/github/tag/lctt/grank.svg?style=for-the-badge)](https://github.com/lctt/grank/) [![GitHub contributors](https://img.shields.io/github/contributors/lctt/grank.svg?style=for-the-badge)](https://github.com/lctt/grank/) [![GitHub](https://img.shields.io/github/license/lctt/grank.svg?style=for-the-badge)](https://github.com/lctt/grank/) [![GitHub last commit](https://img.shields.io/github/last-commit/lctt/grank.svg?style=for-the-badge)](https://github.com/lctt/grank/)

[![Travis (.com)](https://img.shields.io/travis/com/LCTT/Grank.svg?style=for-the-badge)](https://travis-ci.com/LCTT/Grank)
[![GitHub issues](https://img.shields.io/github/issues/lctt/grank.svg?style=for-the-badge)](https://github.com/lctt/grank/)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/lctt/grank.svg?style=for-the-badge)](https://github.com/lctt/grank/)


[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/grank.svg?style=for-the-badge)](https://pypi.org/project/Grank/)
[![PyPI](https://img.shields.io/pypi/v/grank.svg?style=for-the-badge)](https://pypi.org/project/Grank/)
[![PyPI - Format](https://img.shields.io/pypi/format/grank.svg?style=for-the-badge)](https://pypi.org/project/Grank/)


## 特性

- 读取 Commit 信息分析
  - 支持抓取特定时间段的 commit 数据
- 使用 GraphQL 进行数据的抓取
- 分析结果自动排行，并生成活跃度折线图
  - 提供所有项目的活跃度、社区化排行
  - 提供单个项目的活跃度、社区化整合图像

## 样例图片展示

**多项目活跃度**

![](https://postimg.aliavv.com/newmbp/4g3wx.png)

**多项目社区化**

![](https://postimg.aliavv.com/newmbp/i5ni0.png)

**单项目社区化及活跃度**

![](https://postimg.aliavv.com/newmbp/wpoyf.png)

## 样例排行榜

![](https://postimg.aliavv.com/newmbp/emr57.jpg)

## 安装需求

**Python 3.4 +**

## 使用方法

1. 使用 pip 安装项目 `pip install grank`
2. 获取 Github 的 [Personal Access Token](https://github.com/settings/tokens)
3. 使用 `grank login` 设置 Token
4. 使用 `grank config` 设置社区化企业关键词
5. 使用 `grank analy <owner> [<repository>]` 来分析特定用户/组织和项目，比如 `grank analy lctt grank`
6. 使用命令行模式操作，如 `grank --token=XXXX --start=2018-01-01 --stop=2018-05-21 --askrule=0 --rule=inc analy <owner> <repository>` 其中 token 必须指定，其他可以使用缺省设置

## 命令列表

1. `grank checklogin` 显示当前 Token 的登录用户
2. `grank login` 设置用户 Token
3. `grank config` 设置关键词，用于社区化分析
4. `grank analy` 分析组织名下或用户名下的项目，调用方法 `grank analy lctt` / `grank analy lctt grank`
5. `grank clean` 清空当前目录下的临时文件和结果，调用方法 `grank clean`

## 配置文件说明

```
[login]
token = xxx #personal access token

[social]
askrule = 1 # 设置为1时将提醒用户设置规则
rule = corp|inc # 进行社区化分析时的正则表达式规则

[time]
start_time = 2017-01-01 # 分析的开始时间
end_time = 2018-10-01 # 分析的结束时间

[rank]
top = 3 # 绘图时绘制折线的项目数量
```

## 贡献项目

在您进行项目贡献前，请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

## 开源协议

[GPL-3.0](LICENSE)
