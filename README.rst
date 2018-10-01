============
Grank -  Github 项目活跃度分析工具
============

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
4. *grank organ* 分析组织名下的项目，调用方法 *grank organ lctt*
5. *grank repo* 分析特定项目，调用方法 *grank repo lctt grank*
6. *grank user* 分析特定用户，调用方法 *grank user bestony*

