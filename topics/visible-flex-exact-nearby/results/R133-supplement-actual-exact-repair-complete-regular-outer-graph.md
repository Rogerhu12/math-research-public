# R133 补充：精确M32修复背景的实际完整 regular 外图

**状态：已证明（完整外部非线性DN导数、mean和高频Riccati端口的修复转授）。**

公开 Actions [43601149891](https://github.com/Rogerhu12/math-research-public/actions/runs/43601149891)
的第一个新数学子过程实际完成25门、退出码0。
数学原件自记0.0025708019999939324秒，包装层记录实际子过程墙钟5.0005183秒。
它在原精确连续M32修复背景上重新验证完整外图，未重算原端点、cap矩阵或非线性长求解。

## 1. 同一物理背景和新参考

对象是原ac1的精确连续repair，定义
`440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`，
固定物理$\eta_0$与原$\nu$。
本次消费完整65个right-offset、真实even mean和已证固定物理角的完整cap背景变化，
包括无限物理Fourier尾。
修复带宽M32是背景属性，未赋给未知扰动。

新外端标量Riccati数据准确为
$$
p_M(25/8)=q_*/(-m_{\rm repaired}(25/8)),\qquad
1/8<p_M(25/8)<1/5.
$$
它与[实际修复正根collar](R133-supplement-actual-exact-repair-positive-root-collar.md)
所用同一新global reference一致。
完整regular外图本身保非均值图、独立mean输出和所有affine列。

## 2. 新背景与完整算子费用

[公开转授合同O1–5](../notes/2026-11-14-R133-repaired-positive-CI-contract.md)
说明物理角Cauchy、真实角图变化、完整Hilbert共轭和同一DN算子的插值。
实际有向上界可放宽为：

| 项目 | 严格上界 |
|---|---:|
| 物理角$\Delta C$的$A_{1/64}$范数 | $4.969137\cdot10^{-19}$ |
| 修复后外部$Z$的$A^0$范数 | $2.533005\cdot10^{-13}$ |
| 修复后$Z_\theta$的$A^0$范数 | $3.250004\cdot10^{-11}$ |
| 完整Hilbert共轭费用 | $7.190442\cdot10^{-9}$ |
| 同一完整$Z\mapsto d$导数的$H^1$范数 | $0.000242359318250$ |
| 完整moving $H^s$物理恢复 | $0.029726519750$ |
| even非均值onto图逆 | $0.029726519149$ |
| 独立moving mean rank | $0.000001083804247$ |
| 完整Robin $H^1$行误差 | $0.000052691852880$ |
| 完整Robin $H^{1/6}$行误差 | $0.000002522851893$ |

原完整复背景球与holonomy小根门均重新通过。
$H^{1/6}$由同一个全DN算子的$L^2/H^1$插值得到；
没有把Hilbert共轭单独的结论替代DN导数，
也没有使用同阶bare composition减恒等的小量。

## 3. 真高端口和全部独立源列

完整有理包络重新验证后，实际端口费用为：

| 原合同中的端口或输出 | 严格上界 |
|---|---:|
| 全高Riccati端口反馈 | $0.000022100488421$ |
| 完整低96输入到高端口 | $0.000023400517152$ |
| 独立外高度$f_B$源到高端口 | $0.000028326913811$ |
| 普通Robin源到高端口 | $21.000464373$ |
| 独立mean源到高端口 | $25.345773220$ |
| 独立mean源到mean输出 | $49.000053107$ |
| $f_B$源到mean输出 | $0.000004014099051$ |

每列采用原完整regular/Riccati合同的源规范，所有mean和低输入均保留。
该端口是主体$s=0$高模估计所需的$H^{1/6}$真外反射。
主体$s=1$仍保独立右高端口；本结果未授一个尚未证明的物理$H^{7/6}$外图。
原外场的全Fourier尾参与了所有新预算，没有在物理角中截尾。

## 4. 实际输入和证据

| 对象 | SHA256 |
|---|---|
| exact repair native | 6ee8b07fe94a8d9f87865a9ebb6650266b7eca792d435136ba533be92b1959fc |
| 原完整物理cap背景变化 | 35db98d4124d50ef3bd69f3ec3aa6906289e3f6083c3ba91c8197da7547830ff |
| 原完整Hs外图 | b62e06091e0d46198b80f0442da3627fe0ea79d23500bf823a9a96ee2f95e117 |
| 新数学source | 5d1e8a86aa268d4d98bc929264d706b418b88cb99518ca646d84258d3068ffbe |
| 新完整外图native | 75e7c0e1447306a97971ee05dcb68b8d357cb4fffa5c1a37335a6fc29a473424 |
| 原完整摘要 | 1f8a0eb70945c15b25f94361fcee9e39730afbcfeed39917485139687c55dba6 |
| 实际双子过程记录 | 459745352095624995f1a4c0864eb1e6dec7de5eff87c54ec1f2e3fce5ea99f1 |

[完整外图摘要及25门](../notes/repaired_positive_ci/run-43601149891-1-exact-M32-repaired-positive/evidence/repaired-complete-regular-Hs-outer-summary.json)
和[实际过程](../notes/repaired_positive_ci/run-43601149891-1-exact-M32-repaired-positive/process.json)
保原退出、全部身份与各列数值；同目录保存完整native。

本结论只转授真实外图，不单独授正主体低head、全负返回、全BVP或真正参数Schur。
