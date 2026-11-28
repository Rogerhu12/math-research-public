# 原 R53 moving-chart 的完整解析 delta 列：真实全向量核验

2026-11-28，对真实接受的原 design `lambda002_m24`，在全部879个源节点、
全部73个state分量及原collocation midpoint依赖和全部BC行上，实际核验了
加性delta的解析参数列。这里固定计算`t`、完整`Y`、所有support控制、gauge q
和warp reference；delta仍是原design参数，没有换成物理s的偏导。

入口 `analytic/material_delta_column.py::OriginalDeltaColumn` 目前是独立的
列求值器，没有安装到任何活solver。检查器为
`analytic/check_material_delta_column.py`。不组另一个大J，不运行BVP或tail。

## 保留的完整导数

设当前物理前缀长度为`P`，固定chart join为`j`。前缀中
`s=tP/j`，`P_delta=P/delta`；故在固定t下

\[
a_\delta=(a-1)/\delta,\qquad (a_s)_\delta=0.
\]

桥中的`s_delta`和`(ds/dt)_delta`由原平滑五次chart逐项求导；桥半径的导数
来自**实际GL64有限表达式**的前因子和全部移动积分节点，不用声明的`a_s`替换
另一个有限quadrature函数的导数。`a_s`作为原RHS单独使用的量，也对其原
phase表达式单独求导。

角图使用`x=s/end`，保留`x_delta`、spline、late cutoff和end变化，得到
`theta_delta, rho_delta, (theta_s)_delta, v_delta`。原完整core/reference lift
没有删除。前缀中其window在固定t下不变；若`h=a*chi`，则

\[
h_\delta=a_\delta\chi,\qquad (h_s)_\delta=-\chi_s/\delta.
\]

令`d=F_psi`、`dd=F_psipsi`，`alpha=-a_s/(a*kappa)`。除了原
`frame_jvp(d_delta,dd_delta)`，显式metric项为

\[
\alpha_{\rm explicit}
=\frac{-(a_s)_\delta/a+a_sa_\delta/a^2}{\kappa},
\qquad
\beta_{\rm explicit}=-\alpha\alpha_{\rm explicit}/\beta.
\]

完整速度变化还包括这两项乘`N,Bin`，以及`v_delta*d+v*d_delta`。因此

\[
f_\delta=(ds/dt)_\delta\,\mathcal P(W-G_s)/q
 +(ds/dt)\,\mathcal P(W_\delta-(G_s)_\delta)/q.
\]

collocation中点满足
`Ymid_delta=-h*(f_delta,right-f_delta,left)/8`，保留原全state JVP后再进入
Simpson残差。入口和物理cut的显式delta边界列为零；本次完整原差分也实际
给出了零BC列差。

## 真实完整向量结果

唯一源run SHA256：
`1ad1682601655468ecacfe22867d20fe849e87406fac64f1d3b3f9c36ab63891`。
其`M24/nt768`、`lambda=.002`、实际delta`.06413464112662924`保持不变。

| 比较 | h=1e-6 | h=5e-7 |
|---|---:|---:|
| 全879节点RHS列的最大差 | `1.7850401311111644e-8` | `3.815570521789548e-8` |
| 全RHS列相对L2差 | `2.274782019930918e-10` | `4.3882549946786767e-10` |
| 全64191行collocation列最大差 | `3.173600763594483e-11` | `6.893087543971371e-11` |
| 全collocation列相对L2差 | `5.054893645682758e-10` | `9.745353667996284e-10` |
| 全BC列最大差 | 0 | 0 |

解析RHS列用时1.38361秒；包括全部midpoint链的解析F_delta用时4.18086秒。
两个中心差分全残差列分别用时13.58678、12.33294秒；这是本次实际并发环境
的观察耗时，不是通用速度承诺。恢复原参数后，节点RHS和完整原残差均逐位
复原。全过程85.55957秒，峰RSS241044 KiB。

## 可追溯输出与限制

逐字实际输出：
[`2026-11-28-analytic-delta-column-complete-observed.json`](2026-11-28-analytic-delta-column-complete-observed.json)。
scratch原目录为`held10-analytic-work/delta-column-m24-complete-v2/`。

| 项目 | SHA256 |
|---|---|
| 实际JSON / repo逐字副本 | `08d809ba6ed4466ae18a4ef6b2e456cbfcbb8d7ba45c8f71b91b7d44bf11cf48` |
| `material_delta_column.py` | `7e4e6c6322a52e08169ba0d07c6a81a1ac9eabfebe2d3de746e5c3873c92db03` |
| `check_material_delta_column.py` | `888b2ab9213fbc52782c140f261e76b7cd3955bafa9d09a6932be59827d2c942` |
| 完整列数组NPZ | `d652fd7762642f85c0e6323998a0453962e157fd75cf112a6661636d81a87a7d` |

此前32节点初验已通过；第一次全列checker因SciPy私有函数参数顺序错误在
比较前退出，未修改原方程。修正调用顺序后，上表来自实际exit0的v2全量调用。
未以异常初验充当验证，也没有运行另一个非线性分支。

这是解析公式及一份真实场的浮点全向量核验，不是区间导数认证、无限维逆界
或高lambda求解结果。原ShortBridge有限quadrature与clipping边界处的浮点
误差仍保留在比较中；不从本表推断这些实现处具有未经证明的严格光滑性。
后续可在新进程中只替换原delta参数列，保留全部state/core列和全部原门；
当前活链未修改。
