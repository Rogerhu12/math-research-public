# 固定g的零参数块与实际小矩阵消零诊断

2026-11-10，Astra-visible-flex-78718bd0/root。状态：源码事实及有限浮点资源探索；
不是新BVP/新候选/生产算法选择，未改变准备中的M15包。

## 1. 实际固定g源码与可允许的表示变换

根全文读direct-CSC基础730dd3、SupportBVP.fun_jac 15f24e、谱权变换8a4859。
固定g时flow返回同一fixed_flow；fun_jac先将PJ置零，仅not fixed才填参数差分。
adaptive flow也返回零参数导数，weighted_jac只是正对角乘法。因此本次所有区间的
df_dp和中点df_dp确为零。未知support参数只从初始BC进入。
当前CSC为保持原byte-equality明确保留这些零槽以及BC中的结构零。

删除仅数值恰等于0的槽不改变矩阵作为实线性映射：每一行有限和只少加若干零；
非零值、行列位置和维数全部保持。没有小量阈值或近似丢项。但稀疏结构、COLAMD排序、
pivot及浮点轨迹可能不同，不能称原逐字CSC算法不变，也不能借此假称生产审查已完成。

SciPy官方文档说明CSC的nnz包含显式零、eliminate_zeros在原位移除零项，splu默认
使用COLAMD列排序。此处只用这些接口语义，实际运行仍硬钉本地已审SciPy源码：
[CSC](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csc_matrix.html)；
[splu](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.splu.html)；
[显式/隐式零](https://docs.scipy.org/doc/scipy/tutorial/sparse.html)。

## 2. 真正运行的范围

冻结程序scripts/78718-root-csc-zero-diagnostic-v1.py，SHA256
253b8fa3d0c5adb56bd28118798eda993bb060184dcd31345865864793f342a2。

绑定本次成功M14 CP 4776c4c…、自有真实尾0003 c253eed…和旧同g线性背景500e0a0…。
loader默认角数不直接冒充源角数；另构造相同类的原N512，再用原W14二幂变换。
端点自有DN请求height与当前保存端点差实测为0。仅复用该冻结真实导数的TailMixin公式，
没有启动尾服务或发新请求。

从原6599节点按下标均匀选65/129节点，重建原Lobatto中点和两套解析Jacobians，
使用已审canonical CSC装配。它们是当前曲线上的粗子网格矩阵，不是新收敛BVP。
全部区间参数列实测为0；另复制CSC仅eliminate_zeros，两矩阵相减nnz严格为0，
保留canonical结构。逐个执行原COLAMD SuperLU并释放上一因子；两份使用同一确定性右端。
输出只含源/输入身份和小型标量，不保存或输出候选/矩阵数组。

首个真实382080 exit1：CLI误给旧仓库根，缺curve_stable_prefix_bvp导入。
它在任何矩阵生成前失败，无成功报告。改用原生产计划明确的repro/source-root；
程序没有改写。真正成功运行98d1d7/session44512→d24ef0自然exit0，约2.95秒。
0BVP、0tail、0新producer。完整实际argv和失败在
root-csc-zero-diagnostic-observed-01.json中，不从文件存在推自然出口。

## 3. 结果与决策

| 节点 | 未知数 | 移除的精确零槽 | 原CSC bytes | 消零CSC bytes | 原L+U nnz | 消零L+U nnz |
|---:|---:|---:|---:|---:|---:|---:|
|65|2809|43177|3382040|2863916|322443|320493|
|129|5561|81705|6695448|5714988|641251|639123|

CSC存储减少约15.3%/14.6%，但L+U槽数只减少约0.60%/0.33%。
两矩阵数学完全相同；浮点解的相对无穷差为3.71e−12/1.16e−13，
各自规范化后向误差约7e−24/2.6e−23。后向误差的分母很大，不能由此宣称解的前向误差
或BVP条件数很小。因子时间仅毫秒级，不据此宣称全规模性能改善。
导出的L/U字节数不包括SuperLU工作空间、Python、tail或其它活动进程，不能当RSS上界。

实际证据没有显示大幅消除LU填充。因此当前不更改M15已选入口，也不为此再启动全网格
资源试验。将来若确有CSC本身内存不足，约15%的表示节省仍可作为另名方案重新审查；
本次没有支付那条生产路线，更不解决原metric/G5门。

报告root-csc-zero-diagnostic-01.json为12244 B，SHA256
07b99c895d34ec7c1fb2f8f9389be993e323a5e593076b911e08738de38dd931。
完整源/输入在报告中有字节身份，实际读取末尾再次验证。此为排除“大量显式零导致
巨大额外LU填充”在这两个实际小矩阵上的诊断，不是所有频率/网格的不可能性。

来源范围澄清：本诊断报告的sys.modules自动列表不包含所有未注册的动态importlib模块，不能称完整动态源码闭包。两实际小矩阵的等同性与计数记录不变；不为这项资源探索追加冻结/独审/再跑流程。固定g零参数列的具体源码推导见第1节。
