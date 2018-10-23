# Grank -  Github 项目活跃度分析工具
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/grank.svg?style=flat-square)](https://pypi.org/project/Grank/) [![PyPI](https://img.shields.io/pypi/v/grank.svg?style=flat-square)](https://pypi.org/project/Grank/) [![GitHub tag](https://img.shields.io/github/tag/lctt/grank.svg?style=flat-square)](https://github.com/lctt/grank/) [![GitHub](https://img.shields.io/github/license/lctt/grank.svg?style=flat-square)](https://github.com/lctt/grank/) [![GitHub last commit](https://img.shields.io/github/last-commit/lctt/grank.svg?style=flat-square)](https://github.com/lctt/grank/)

[![Travis (.com)](https://img.shields.io/travis/com/LCTT/Grank.svg?style=flat-square)](https://travis-ci.com/LCTT/Grank)
[![GitHub issues](https://img.shields.io/github/issues/lctt/grank.svg?style=flat-square)](https://github.com/lctt/grank/)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/lctt/grank.svg?style=flat-square)](https://github.com/lctt/grank/)


## 特性

- 读取 Commit 信息分析
  - 支持抓取特定时间段的 commit 数据
- 使用 GraphQL 进行数据的抓取
- 分析结果自动排行，并生成活跃度折线图
  - 提供所有项目的活跃度、社区化排行
  - 提供单个项目的活跃度、社区化整合图像

## 样例图片展示

**多项目活跃度**

![](https://postimg.aliavv.com/newmbp/3xexn.jpg)

**多项目社区化**

![](https://postimg.aliavv.com/newmbp/f2fce.jpg)

**单项目社区化及活跃度**

![](https://postimg.aliavv.com/newmbp/ebrrr.jpg)


## 安装需求

**Python 3.4 +**

## 使用方法

1. 使用 pip 安装项目 `pip install grank`
2. 获取 Github 的 [Personal Access Token](https://github.com/settings/tokens)
3. 使用 `grank login` 设置 Token
4. 使用 `grank config` 设置社区化企业关键词
5. 使用 `grank analy [mode] <owner> [<repository>]` 来分析特定用户/组织和项目，比如 `grank analy lctt grank`,分析结果可以在执行命令目录的 result 目录中找到。
6. 使用命令行模式操作，如 `grank --token=XXXX --start=2018-01-01 --stop=2018-05-21 --askrule=0 --rule=inc analy <owner> <repository>` 其中 token 必须指定，其他可以使用缺省设置

## 命令列表

1. `grank checklogin` 显示当前 Token 的登录用户
2. `grank login` 设置用户 Token
3. `grank config` 设置关键词，用于社区化分析
4. `grank analy [mode]` 分析组织名下或用户名下项目的活跃度或社区化程度，mode 的默认值为`all`，可设定为`social`或`activity`。调用方法 `grank analy lctt` / `grank analy --social lctt grank`。
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

## Contributors

Thanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars1.githubusercontent.com/u/13283837?v=4" width="100px;"/><br /><sub><b>Bestony</b></sub>](https://www.ixiqin.com/)<br />[💻](https://github.com/LCTT/Grank/commits?author=bestony "Code") [📖](https://github.com/LCTT/Grank/commits?author=bestony "Documentation") [💡](#example-bestony "Examples") [📦](#platform-bestony "Packaging/porting to new platform") [👀](#review-bestony "Reviewed Pull Requests") [⚠️](https://github.com/LCTT/Grank/commits?author=bestony "Tests") [🔧](#tool-bestony "Tools") | [<img src="https://avatars0.githubusercontent.com/u/128338?v=4" width="100px;"/><br /><sub><b>Xingyu.Wang</b></sub>](http://wxy.github.io/)<br />[💬](#question-wxy "Answering Questions") [🐛](https://github.com/LCTT/Grank/issues?q=author%3Awxy "Bug reports") [💻](https://github.com/LCTT/Grank/commits?author=wxy "Code") [👀](#review-wxy "Reviewed Pull Requests") [📢](#talk-wxy "Talks") | [<img src="https://avatars1.githubusercontent.com/u/23754818?v=4" width="100px;"/><br /><sub><b>LuMing</b></sub>](http://LuuMing.github.io)<br />[💻](https://github.com/LCTT/Grank/commits?author=LuuMing "Code") [📖](https://github.com/LCTT/Grank/commits?author=LuuMing "Documentation") [⚠️](https://github.com/LCTT/Grank/commits?author=LuuMing "Tests") |
| :---: | :---: | :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!
