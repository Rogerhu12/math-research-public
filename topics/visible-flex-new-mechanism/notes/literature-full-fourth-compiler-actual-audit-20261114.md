# 完整第四阶符号编译：公开Actions实际回执与全来源审计

日期：2026-11-14。root核对公开输出、全部源文件与开发检查。没有重新运行编译、profile积分、几何评价或优化。

## 1. 实际执行与完整字节核验

- 公开 [run43615655870](https://github.com/Rogerhu12/math-research-public/actions/runs/43615655870)，attempt1，lane full_range_compile。
- 实际source commit：218254b94ff7f51f92692f2f15c5f374af1990e7。
- root逐件从该commit的git对象读取80份receipt来源，长度和SHA256全部一致；2份输出原字节和raw字段全部一致。
- compiler源SHA256：a7f1771a33a8e73934f9549b3407a9e351fed59a9eec163c5b11c965c7f1dc52。
- runner两次真实pull后均核双README无变化，最后已读规则提交2ecaff15acff72a3aba55e0a0f6b8f068a64eb7b；不把后续main文件代替实际执行源。

| 输出 | bytes | SHA256 |
|---|---:|---|
| full-fourth-compiler-development-check.json | 2418 | 6dc28d58d367084a1115be6f902b244733066a85bdf01156541bcb85b8c75b3f |
| full-fourth-profile-algebra.json | 8783 | 811fc1840b0644330a562a7862bc56c2fd1f6d00158c96b7db3736b1e41a75db |

## 2. 实际完成范围

实际completion=complete，max_order=4，编译器记录耗时10.055273965秒；这不是整个Actions作业耗时。资源为267875 coefficient DAG节点、6365 profile原子（其中6355个右锚Volterra原子）、732个真实s历史状态。750000节点、100000原子/项、300秒预算均未触及。

真实二、三阶历史数为B27、U318、V387；三者准确共732。它们只在全局s起点取零，后续各段保留历史，不按packet或连接段重置。h、k的最大导数深度为3，profile最大jet为4。omega的导数通过真实omega'=k'/(2h)进入，不能由omega深度0误认为控制常数。

六个第四forcing通道已实际组合为全部五个物理相位谐波；没有仅列出组合公式而漏编表达式。输出数量如下：

| 相位mode | period RHS分离项 | ruling integrand分离项 |
|---|---:|---:|
| -4 | 3186 | 718 |
| -2 | 14959 | 3476 |
| 0 | 23195 | 5407 |
| 2 | 14959 | 3476 |
| 4 | 3186 | 718 |

这些是冗余表达式项数，不是独立函数维数、Gram秩或已经满足的方程数。正mode使用准确共轭，但输出仍逐个保留实际表达式hash。

## 3. 可复现身份和开发检查

- 有序coefficient DAG SHA256：5405503abaade65dc82d7899b46ea2ebb5c7db74448f431423cc5bb054f7912a
- 有序profile原子DAG SHA256：5fa5ace77241b9739daaab7447c4fb7e6026d864f917f99fd0835bcf09fd4a4e
- 有序状态RHS SHA256：85831fde07ccebb9cc8017f98b32d11319065c4c3073df2b1ca6c9d3fc9d87ec

小型开发toy原件2344B与Actions toy2418B的递归比较只有四项运行环境字段不同：repository、run_id、run_attempt、source SHA。全部代数检查及其余字段相同；完整编译输出中的toy_checks也完全相同。没有把长度不同误报为原字节相同。

准确检查包括profile乘法法则、共轭对合、右锚原函数求导及共轭、真实状态导数、二/三阶相位与五第四mode，以及准确种子相位的全部修正为零。完整源码及设计见[设计说明](literature-full-fourth-compiler-design-20261114.md)。

## 4. 尚未得到的结论与接续

本次只完成准确形式表达式编译。specific_P_geometry_supplied、profile_integrals_evaluated、geometric_design_evaluated、whole_range_conditions_satisfied、finite_family_certified均为false。B/U/V的恢复只在相应两条完整range已支付时代表真实周期双collar场；当前compiler没有据表达式存在代付这些条件。

下一计算必须使用[R45](../results/R45-reversal-four-block-third-period-cancellation.md)准确单P→D、M_P=0及其P/P/倒P/倒P四块，保同一个真实profile与全s历史，并以真实Gram核处理冗余。不能使用旧Klein八块N16384实例冒充新P，也不能令每个冗余分离项系数分别为零代替整个函数条件。

已完成编译无需重复运行；后续是具体几何/profile下的完整period与逐ruling支付，以及更高阶、有限族、闭嵌入和宏观reach。课题未完成。
