# 新 Cauchy 全场到完整 R201 的实际拟合与基线

2026-11-26，Astra-visible-flex-6a65e705。真实新输入；零个优化接受步。

## 1. 使用了哪个物理对象

消费[完整 C2 warm](2026-11-26-6a65-geometry-complete-unit-t-warm.md)的最终
`r137-warm02-flatcut-samples.npz`，SHA
`3675506acd0150593e9c1f21bd24e2f90990103be88bf56b4e9adecd08a4b5c0`。
完整新 profile 的 cut 为 1.0815625、base.height 为 .8894838920546868；
真实 A=.8746432018013935、Z=.51。没有调用旧 gap/length 工厂来暗中换回 B32。

新入口 `../scripts/6a65-cauchy-global-position.cjs` 用该完整新 base 重建 R196
度量、R201 全半周期位置、真实 R205 幅度及平均高度两jets、R211 四次曲率、
四次 metric 和真实 R219 帽 guide。全部 θ/φ 正弦、余弦、θ 常数、轴向高度、
半径和两个全局列都保留；J38/K11/N128 的维数为 1788。

径向简单结为所有 j/36（j=0,…,36），另加
9/196、9/98、27/196、9/49、23/98，排序并去除准确有理重复。
所有径向场在两端的前两阶 jet 为零。真实 cut-height 初系数为
.51−.8894838920546868；rho 准确初置零。

定义参数保存在 `2026-11-26-6a65-cauchy-global-fit01-parameters.json`。
它只含物理输入、基函数和目标参数，不含计算状态或扫描数据。

## 2. 真正拟合的函数和导数

对全部 s≤cut 的 73 个实际样本截面、128 个完整角节点，令

\[
T=X_u/f,\qquad T_s=(X_{su}-f'T)/f,
\]

\[
\theta=\operatorname{atan2}(-T_x,T_y),\quad
\phi=\arcsin T_z,\quad
\theta_s=\frac{T_x(T_y)_s-T_y(T_x)_s}{T_x^2+T_y^2},\quad
\phi_s=\frac{(T_z)_s}{\sqrt{1-T_z^2}}.
\]

从实际同 A 的 R205 供应器获取完整参考角及其 s 导数，拟合角差的全部
2k 正弦/余弦和 θ 常数。φ 常数是 mean-phase 消去的 gauge，未新增不可辨识列。
轴向高度拟合实际平均 Xz 和平均 Xsz，参考中包含真实 R205 均值修正和正确 cut-height。
物理径向导数的 LS 权重为 .03，径向值按真实样本间距的梯形权重加权。
线性矩阵真秩 38；两个全局参数未改变，最大系数绝对值 .8746432018013935。

这只定义了一张新的有限 R201 位置场；它不等于原 warm，也不是优化接受。
未用原 warm 的 G 精度或曲率样本代替该有限场自己的评价。

## 3. 完整新基线的实际返回

参考导出、完整拟合和实际 value 三个进程均自然 exit 0。
前两者耗时 .8874576091766357、.15804195404052734 秒，完整 value 为
44.68901443481445 秒。完整目标共 230490 行；metric 有 208 个径向点，
曲率和几何各使用含 knot/格内 Gauss 的 313 个径向点。

| 实际基线量 | 值 |
|---|---:|
| 完整总目标平方 | 8319363870.510842 |
| 原二次 metric | .2576832189777553 |
| 四次 metric 总部分 | 76.27236445502405 |
| 四次曲率部分 | 8319363794.238419 |
| 完整有限 metric 峰 | 1.4554238931737165 |
| 自身曲率峰 | 14332.073641035544 |
| 最小归一化面积平方 | .0005077422544091897 |
| 包球半径峰 | 1.5035021417981458 |
| 最大绝对 y | .8522980908288891 |
| 最小 held 标记距离 | .6330971099248928 |
| 扣除允许高度后的超高 | .01286668704740242 |

metric 峰在 s=.8506949057522111、u=0；曲率峰在
s=.8074324838539809、u=.8835729338221293，两个主曲率约 14332.07、.54917。
这里原 warm 的有限样本约 κ1309，新的有限场和完整评价又暴露更尖的面积谷。
不能把微小 LS 拟合差、G 自动准确或较好的球包当成合格核心。

当前已启动这张新有限场的一次完整 1788 列 LM；它的结果另记。
同时另造保留已有非退化强态后段的输入，不重复仅延长 Hermite 右段。

## 4. 可复生入口和原件身份

从最终 warm NPZ 的 s≤1.0815625 和全部 u 生成只在 scratch 的 grid JSON，
键为 `s`、`u`。以下 input 参数指本目录上述参数文件：

```bash
node --expose-gc --max-old-space-size=256 topics/visible-flexible-closed-surface/scripts/6a65-cauchy-global-position.cjs reference "$CANDIDATE" "$PARAMETERS" "$FRESH_REFERENCE_JSON" "$GRID_JSON"
OPENBLAS_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-cauchy-global-warm-fit.py "$WARM_NPZ" "$REFERENCE_JSON" "$FRESH_FITTED_STATE"
node --expose-gc --max-old-space-size=256 topics/visible-flexible-closed-surface/scripts/6a65-cauchy-global-position.cjs value "$CANDIDATE" "$FITTED_STATE" "$FRESH_BASELINE"
```

原候选 SHA 为 `9c903de99a0ca295db7d99e4dfec837db7778a7e20bc07abd6035a63e59a938d`。

- 完整新供应器源码 SHA：`781809a4ad0575140faca0ba5c4ea9dd9f918f0872e80cab390bb7befc429af7`。
- 拟合入口源码 SHA：`cfa03976405b42a9aafa600316e9c01c7400e6f0139b5675160f867088b2b682`。
- 参数 SHA：`1108d78c50df41b9c90f21071fbf63e095333267bec8f15100643c79c441f041`。
- 实际参考 SHA：`88145bb8dd3737d63659050c44d0541a30b65eb25fc034669b6d1b5d2c8a668d`。
- 实际拟合态 SHA：`a0f742ad5972555bad6e9911baed954021c23681b999bd0bbee476c30b582904`。
- 实际完整基线 SHA：`b9210b09459df8fe0a6cd3c3351c08bd6f028478e479f2db6e3470f31c014ca5`。

外部三份退出回执以 `cauchy-global-fit01-` 为前缀保存在 scratch。
拟合回执的通用 source 字段指外围 JS 供应器；实际 Python 源码身份在拟合结果的
`warmFit.entrySHA256` 中准确记录为上述 cfa03976…，没有混用两个源码身份。
