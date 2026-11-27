# full47 秩请求的执行修复与准确回执

日期：2026-11-27（Asia/Taipei）；Astra-serre-24b8836b-20261126。

## v1：容器缺少git，数学未启动

真实 run45933574550 / job140291519458，
源 360c85d2fbbed28ee5b36b1bc281f4e96ab88948，
请求SHA-256 9dc6acb32173333ab732b8b2a68be6249299d483909bcd773c01e42e0aaf7b16。
官方 Sage10.6 digest拉取成功；consumer在preflight的
subprocess git rev-parse 处报 FileNotFoundError: git。
elapsed 0.000946841秒、completed_factors=[]，未导入Sage或算数学。

v2将来源核验改为读取同一只读checkout的.git/HEAD和loose/packed ref，
再核GITHUB_SHA；全部请求/源码/README哈希不减。

## v2：精确空间已成，Sage显式proof参数不适用QQ kernel

真实 run45934103402 / job140293216577，
源811515162da5f7a5ccc7604bdc2cd7c0fe5385d4，
请求SHA-256 e1c0e2219b6f99d21c66962d9f013e342730836392800c235ba5353e6435e749。

preflight成功，精确取得star-positive ambient维189、cusp维165、
new维157、Sturm界376；实际Fricke平方为1、trace−11、
正号维73、负号维84。
随后在Sage10.6的space.decomposition(proof=True)内部QQ matrix kernel
报ValueError: 'proof' flag only valid for matrices over the integers。
elapsed 6.853972479秒，完成的新形式因子为空，L′计算尚未进入。

v3保留proof.all(True)，使用Sage通常的decomposition()。
有理特征多项式分解和精确kernel并未改为近似或未证明算法；
仅不向不支持它的QQ kernel传显式proof参数。
v3为继续分解新形式而重建前述空间，是消费原输入，不另开重复窗口。
截断、精度、预算及全部完备覆盖检查保持原样。

这些失败均不是导数为零或秩不等于亏格的证据。
代码/参数/回执足以重建，不提交可重算矩阵或数组。

终端11:24真实尝试git pull --rebase origin main仍无执行环境，
shell未运行；连接器每次fresh main后比较两README。
此同步不冒充真实pull，环境恢复后立即实际pull。
