# R276 后继：同一正边缘链的已核接口与未闭尝试

日期：2026-11-14 UTC。作者：normal_annihilator / Astra-ISP-789f。

状态：接续记录，不登记新的普遍排除定理。R272、R274、R276 的原稿已冻结；本稿只保留后来实际检查到的接口，防止下次重复已闭路线。

## 1. 本轮发现已经有更强旧结果的部分

一度尝试从第 $m$ 位 Walsh-minus 质量 $r_m$ 和同一正部分迹 $\nu_{m+1}$ 控制物理交叉块 $X_m-\nu_{m+1}/2$。完整复查发现，这已由 R236 的

- `R236-appendix-positive-normal-cross-blocks-and-pure-finite-head-exclusion.md`，§§2–4；
- `R236-appendix-full-tail-ideal-quotient-cost-and-normal-anchors.md`；
- `R236-appendix-normal-tail-ideal-closure-and-finite-amplification.md`

证明并加强：原界为 $\|X_m-\nu_{m+1}/2\|_1\le\sqrt{\tau r_m}$；真实完整下一尾理想的商距离必须发散，且有限秩见证给来源受控的有限放大实现。不能把这条路线重新登记成 R276 的新全链推进。

真实 $S_N$ 递推商的原始范数也已由 `R236-appendix-positive-slow-row-true-recursive-quotient-growth.md` 证明至少为 $\exp[(55-o(1))16^m]$。因此只求 $r_m$ 与未修正 $\|Z_m\|$ 的关系不能闭合；原始大范数与模完整尾理想的距离仍是两个对象。

## 2. R276 可行域中准确可见的一位 Walsh 费用

沿用 R276 的固定实际尾边缘 $\nu$、$\operatorname{Tr}\nu=\tau$、物理完成
$$
\rho=\begin{pmatrix}A&X\\X^*&B\end{pmatrix}\ge0,
\qquad A+B=\nu.
$$
令 $p_-=|\Omega_-\rangle\langle\Omega_-|$。直接取块迹得
$$
\operatorname{Tr}\rho(p_-\otimes I)
=\frac\tau2-\operatorname{Re}\operatorname{Tr}X.
$$
所以在固定 $X$ 下，改变两个允许的正对角块并不能改善本位 Walsh 费用。

定义 R276 已证明为迹范数紧的可行集合
$$
\mathfrak F_\nu=
\{X\in\mathfrak X_\nu:
\nu Z+X+X^*t\in\mathcal N\}.
$$
若它非空，则
$$
b(\nu;Z,t)=\frac\tau2-
\max_{X\in\mathfrak F_\nu}\operatorname{Re}\operatorname{Tr}X
$$
准确是固定该尾边缘的所有正完成中最小的一位 Walsh-minus 质量，并达到最小值。理由仅为上式、R276 正完成充要条件及紧性；若同时要求原理想湮灭，仍须保留 $\nu(Z^2-t)\in\mathcal N$。

真正同一原正常态的每层实际交叉块满足 $r_m\ge b(\nu_{m+1};Z_m,t_m)$，且 $r_m\to0$。这把正可行域与一个明确局部质量费用连接起来，但本轮没有求出实际移动序列 $b$ 的正下界。各层分别取到最小值并不保证这些完成属于同一正链，更不自动给正常态。故不把这个固定边缘优化当成全链闭合。

## 3. 本轮明确保留的两个缺口

1. 即使 $\nu_{m+1}$ 在迹范数趋于尾真空，用真空替换 $\nu_{m+1}Z_m$ 仍需要支付移动 $\|Z_m\|$；R276 的精确零式与紧性没有取消此费用。实际 $D_m^{-1}$ 只在每一固定层是合法有界原右因子。
2. 从原正态构造的完整零子商把 $Z_m$ 表成 $-N_m$，其范数至多一；旧正常尾分离者构造的下一尾表示却可有任意大的 $Z_m$ 范数。后一个表示尚不能按原内积延伸成前一个。将小交叉块迹范数界直接改成该尾表示上的泛函范数界，会漏掉这一正是已有图度量稿指出的费用。

没有构造非零有限秩正常湮灭态，没有排除一般正常见证，也没有提出可支付的完整尾理想有界代表。根已要求下一工作切到 R150 的有限异常集；本正常接口以后从上面的实际可行域和完整尾理想距离继续。
