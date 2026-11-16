# R898 — 原有理 Hecke 方向的权四比值排除与条件次数下界

日期：2026-11-16。**状态：已证明（公开 Actions 中的精确有限域秩，结合下述完整特征零证明）。**

保留 R874 的原有理 Hecke 方向
$$
u=(915,1097,2962)/55569,\quad
F=\mathbf Q(a),\quad a^3=17,\quad
\lambda=(68+7a-13a^2)/3,\quad v_{\rm new}=\lambda^3v.
$$
令 $Y_{\rm new}(Q)$ 是原微分 $H_u/\lambda$、原椭圆方程与首项规范决定的 Laurent germ；
其开头仍为 $-Q^{-1}-(v_{\rm new}+3)/2$，不另选目标映射。

**结论。** 不存在 $A,B\in M_4(\Gamma_0(867);F)$、$B\ne0$，使
$Y_{\rm new}=A/B$ 作为原 Laurent germ 恒等。该结论在任何特征零系数扩张后仍成立。
若这个原 germ 延拓为 $X_0(867)$ 上的有理函数，则该函数到 $\mathbf P^1$ 的次数至少为 $324$。

这没有排除权六或更高权表示，没有认证原映射存在，也没有给原 shadow 或 Sha 非零结论。

## 1. 原空间与完整有理基

$867=3\cdot17^2$，其模群指数为 $1224$，cusps 数为 $36$，椭圆固定点数均为零，故
$$
g(X_0(867))=1+1224/12-36/2=85.
$$
权二模形式是 $\mathcal L=\Omega^1(C)$ 的截面，其中 $C$ 为全部 cusp 除子；
$\deg\mathcal L=204$。因此
$$
\dim M_2=120,\qquad
\dim M_k=102k-84\quad(k\ge4\ {\rm even}).
$$
特别 $\dim M_4=324$。

原 producer 从同一个 Sage 有理 $M_2$ 基出发，按固定顺序选权四乘积，
在参数指定的素数 $1000037$ 上检查其前 $409$ 项的独立性，直至正好选出 $324$ 项。
每项本来就是有理权四模形式；有限截断上的独立性蕴含特征零独立性，
结合上述完整空间维数，这些乘积是 $M_4$ 的完整有理基
$g_1,\ldots,g_{324}$，而非某个未证生成的子空间。

本次 run 的完整基步骤确已结束；其确定性 recipe SHA-256 为

    3cf33f7bca9c4966d3a6b9f62ec1654eda987f6d69d9350e063a7ceb43cd4d67

用于低重建的完整有理基系数行 SHA-256 为

    8214a794f0d654974d1c5c67033afda608ef6c632da53f7b95da08897f10b025

数据不另行保存，原脚本、参数及下面的 source/run 可以重建它们。

## 2. 必要的有限线性系统

写 $y(Q)=QY_{\rm new}(Q)$。若
$$
A=\sum_{j=1}^{324}a_jg_j,\qquad
B=\sum_{j=1}^{324}b_jg_j
$$
满足原恒等式，则
$$
QA-yB=0.
\tag{1}
$$
取 (1) 的 $Q^0,\ldots,Q^{817}$ 系数，得到 $818\times648$ 矩阵 $M$：
$$
M_{i,j}=
\begin{cases}
0,&i=0,\ j\le324,\\
[Q^{i-1}]g_j,&i\ge1,\ j\le324,\\
-[Q^i](y g_{j-324}),&j>324 .
\end{cases}
\tag{2}
$$
任何真正的比值表示必须给 (2) 的一个非零核向量。
这里只使用恒等式的必要有限前缀；并未把短前缀零冒充整条椭圆恒等式。

原 $y$ 由已提交的三角递推求出；其递推每步只除 $2$ 和 $3m+1$。
原 CM 系数、$\lambda,v_{\rm new}$ 和全部基系数都经过脚本中明确的分母单位检查。
在本节所需的 $m\le818$ 范围，下节素数也不整除这些递推分母。
因此 (2) 的约化是同一特征零矩阵的真实约化。

## 3. 单个有限域满秩已经排除所有特征零核

公开 run 的精确输出是
$$
\ell=1000000033,\qquad a\bmod\mathfrak l=50539607,\qquad
\operatorname{rank}_{\mathbf F_\ell}(M\bmod\mathfrak l)=648.
\tag{3}
$$
脚本验证 $\ell$ 为素数、$a^3=17$ 有三个不同根、所用根确实满足原方程，
并验证相关全部分母可约化。因 $\ell\nmid 3\cdot17$，该根给 $F$ 的一个非分歧次数一素点 $\mathfrak l$。

由 (3)，$M\bmod\mathfrak l$ 有一个 $648\times648$ 非零子式。
同一子式在 $F_{\mathfrak l}$ 中是单位，因而在 $F$ 中非零。
所以 $\operatorname{rank}_F M=648$，其核为零。
或者将任何假定非零核向量乘一个局部标量，使其坐标全整且至少一个为单位；
约化后会得到 (3) 的非零核向量，矛盾。
这一步不需要 CRT、有理重建或最终非线性证书；也没有把未满秩的模 $\ell$ 结果提升为特征零秩等式。

固定非零子式在任何特征零扩域中仍非零，故结论保系数扩张。
权二比值若存在，乘以任一非零有理权二形式即可给权四比值，故也被排除。

## 4. 条件有理函数的次数下界

假设原 $Y_{\rm new}$ 确延拓为 $X_0(867)$ 上的非恒定有理函数，
记其极除子为 $D_Y$、次数为 $d$。
权四线丛是 $\mathcal L^2$，次数 $408$。Riemann–Roch 给
$$
h^0(\mathcal L^2(-D_Y))
 \ge 408-d+1-85=324-d.
\tag{4}
$$
若 $d\le323$，(4) 保证有非零截面 $B$；
$A=Y_{\rm new}B$ 也属于 $H^0(\mathcal L^2)=M_4$，
产生已排除的比值表示，矛盾。因此 $d\ge324$。
这里没有预先把该有理函数的存在视为已认证。

## 5. 完整公开运行记录与未结束部分

- 仓库：Rogerhu12/math-research-public。
- source commit：969b3f439e706e539595424e18ddb573197475fa。
- producer：scripts/produce-original-rational-hecke-map.py，Git blob ed97dc7e5d92b4c743857e07422b64581dcc1de5。
- 原 germ：scripts/original_low_weight_cm_tools.py，Git blob 78932ee8d47e2d7938736c0a44e15edf1951393e。
- 参数：ci/original-rational-hecke-map-request.json，Git blob 6bdc92ca24f7c6ca08b42f8cee818809b2596b9b。
- 参数包含 weights=[4,6]、max_split_primes=96、split_prime_start=1000000000、product_basis_prime=1000037；原 u、整数返回17和原目标 rescaling 全固定。
- [公开 run 43835679463](https://github.com/Rogerhu12/math-research-public/actions/runs/43835679463)，job 133191600105，固定 Sage10.6 image sha256:19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb。
- 上述权四 CASE 在 2026-11-16 09:05:15 UTC 输出；权六完整基在此前约298秒处也已完成。
- job 于 14:59 UTC、其360分钟工作流边界附近以 cancelled 结束。最后一条完整权六阶段记录为53个分裂素数、1585位模数、模秩904、B首阶1。没有最终 RESULT，没有原 map PASS。
- 权六的这些模秩不证明其特征零精确秩，也不证明候选不存在。它们只定位本次实际运行已经推进到逐素数重建；不能把本次瓶颈记为“仍未生成 M2 基”。

R889 Newton 与 R892 PARI 路径继续保留全部原最终认证要求；不因本篇的排除结果删除或替换原来源。
