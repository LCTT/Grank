============
Grank -  Github 项目活跃度分析工具
============


.. image:: https://img.shields.io/pypi/pyversions/grank.svg?style=for-the-badge   :alt: PyPI - Python Version   :target: https://pypi.org/project/Grank/


.. image:: https://img.shields.io/pypi/v/grank.svg?style=for-the-badge   :alt: PyPI   :target: https://pypi.org/project/Grank/

.. image:: https://img.shields.io/github/tag/lctt/grank.svg?style=for-the-badge   :alt: GitHub tag   :target: https://github.com/LCTT/Grank

.. image:: https://img.shields.io/pypi/format/grank.svg?style=for-the-badge   :alt: PyPI - Format   :target: https://pypi.org/project/Grank/


.. image:: https://img.shields.io/pypi/implementation/grank.svg?style=for-the-badge   :alt: PyPI - Implementation   :target: https://pypi.org/project/Grank/

.. image:: https://img.shields.io/pypi/l/grank.svg?style=for-the-badge   :alt: PyPI - License   :target: https://pypi.org/project/Grank/



.. image:: https://img.shields.io/github/issues-raw/lctt/grank.svg?style=for-the-badge   :alt: GitHub issues   :target: https://github.com/LCTT/Grank/issues

.. image:: https://img.shields.io/github/contributors/lctt/grank.svg?style=for-the-badge   :alt: GitHub contributors   :target: https://github.com/lctt/grank/


特性
------------------
- 读取 Commit 信息分析
- 使用 GraphQL 进行数据的抓取
- 分析结果自动排行，并生成活跃度折线图

.. image:: https://postimg.aliavv.com/newmbp/0p4is.png

需求
------------------
**Python 3**

使用方法
------------------

1. 使用 pip 安装项目 *pip install grank*
2. 获取 Github 的 `Personal Access Token <https://github.com/settings/tokens>`_
3. 使用 *grank login* 设置 Token
4. 使用 *grank config* 设置社区化企业关键词
5. 使用 *grank repo <owner> <repository>* 来分析特定项目，比如 *grank repo lctt grank*

命令列表
------------------

1. *grank checklogin* 显示当前 Token 的登录用户
2. *grank login* 设置用户 Token
3. *grank config* 设置关键词，用于社区化分析
4. *grank analy* 分析组织名下或用户名下的项目，调用方法 *grank analy lctt* / *grank analy bestony*
5. *grank repo* 分析特定项目，调用方法 *grank repo lctt grank*
6. *grank clean* 清空当前目录下的临时文件和结果，调用方法 *grank clean*

配置文件说明
------------------


::

    [login]
    token = xxx #personal access token

    [social]
    rule = corp|inc # 进行社区化分析时的正则表达式规则

    [time]
    start_time = 2017-01-01 # 分析的开始时间
    end_time = 2018-10-01 # 分析的结束时间

    [rank]
    top = 3 # 绘图时绘制折线的项目数量

