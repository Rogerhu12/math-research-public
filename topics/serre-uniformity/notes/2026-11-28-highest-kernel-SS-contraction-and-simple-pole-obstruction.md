# 原最高核完整 SS 收缩：有限值与简单极部路线的否定

**R1208 范围更正：** 本次脚本只计算原 SS 收缩。旧表的 V_m 标签与运行输出中的同名字段应读作 SS 部分；它们不包含后来在 [R1208](../results/R1208-original-CM-node-boundary-and-corrected-highest-kernel-log.md) 核准的 CM node 静态边界。全部实际 run、代码/摘要 hash 和数值保留，不重跑；完整 V 的更正后全称式见该文。


日期：2026-11-28。会话：Astra-serre-24b8836b-20261126。

**精确有限计算／数值证据。** 本次只读取 R1199–R1200 新得到的同一最高 packet、同一 CM 轮廓核 $T_*=(b^3-1)^{2g-1}$ 的完整 SS 收缩。没有重跑任何已登记素数窗口，也没有计算 $p=41,47$。这些有限值不证明全 $p$ 的单位性、指定非 CM 商的整运输或 Serre 一致性。

## 实际运行与可复现输入

- 脚本：[original_highest_kernel_contraction.py](../scripts/original_highest_kernel_contraction.py)。参数为 `--primes 59 71 83`；Python 标准库，所有数学执行均在本公开仓库的 GitHub Actions。
- 原来源提交：[`b2d7b694df805ef3742465b08615ea4a002e3490`](https://github.com/Rogerhu12/math-research-public/commit/b2d7b694df805ef3742465b08615ea4a002e3490)。使用 R1200 (1200.20)、(1200.23)–(1200.31)、(1200.34) 的准确 reference 权和原 $A_p$。
- 实际 [run 46164785591](https://github.com/Rogerhu12/math-research-public/actions/runs/46164785591)，job `141039795948`，成功；程序耗时 1.397 秒，exit zero。
- 脚本 SHA-256：`803cb1d9805c50f671e38d8da03e827b1d70a949ec25d1305003e9ae86d46f20`。
- 完整摘要的规范 JSON SHA-256：`44b99338904d4430851478f799b6dea20ffbfadc2044444bb38f90151aa6e451`。逐根数据只在运行中用于摘要哈希；不保存 raw、artifact 或 Release。

原 $Q_p$ 由 R1023 的 ODE 递推后化为 monic。程序在 $\mathbf F_{p^2}=\mathbf F_p[i]$、$i^2=-1$ 中枚举其全部简单 SS 根，逐根用原 Picard–Fuchs 方程和有限 Lagrange 公式求完整收缩。另一个一阶 dual number 同时读取同一有理算子的 $b$ 导数；没有对 SS 插值多项式的导数作替代。所有实际除数均作单位检查。

## 得到什么

记 $P_\epsilon=\mathcal P_m^{\lambda_\epsilon}(T_*)$，其中
$\lambda_0=-6/r$、$\lambda_1=-6b/r$。表内各值在对应的 $\mathbf F_p$ 中。

| $p$ | 全部 SS 根数 | $\sum_s P_1(s)/(r_s^{2g+1}A'(s)^2)$ | 原 SS 部分 $V_m^{\rm SS}(T_*)/\nu$ | $P_1$ 的非零 SS 简单极部数 | 原核 Cartier 系数 |
|---:|---:|---:|---:|---:|---:|
| 59 | 28 | 20 | 43 | 27 | 23 |
| 71 | 34 | 11 | 13 | 33 | 37 |
| 83 | 40 | 27 | 54 | 39 | 81 |

最后一列读取的准确有限系数是
$$
-[x^{4g-1}](1-x)^mQ_p(x).
$$
该列不是 SS 收缩或完整 $V_m$ 的替代，两者之间没有在本次运行中建立比例身份。

三个例子中，$P_0$ 对全 SS 双极系数之和均为零，与 R1200 已证明的三次轨道消去一致。两部分各自的 SS 简单极部总和也均为零；这不表示逐点简单极部消失。

**被排除的路线。** 对 $P_1$，R1200 的实际判据
$$
rP_1'+mb^2P_1\equiv0\pmod A
$$
在这三个运行中均不成立。特别 $p=59$ 已有 27 个非零简单极部。因此后续不能假定原有理函数只有 SS 双极部，也不能只用普通 residue 总和替代所需的双极系数之和。全部简单极部必须继续保留，或通过合法的完整有限代数 trace／求积身份处理。

## 继续的实际输入

当前的全 $p$ 对象仍是 R1200 (1200.34) 的原全和。三个有限值均非零只供选择路线；不扩大扫描，不把有限数据升为全称结论。继续用原 $Q_p$ 的微分方程、完整 trace 及实际端点归一求解这个和，并另保指定 $C$ 的整投影问题。
