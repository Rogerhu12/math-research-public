# R133 补篇：完整物理帽矩阵图的连续残差合同

2026-11-14。**已证明：完整矩阵提案误差到真正全频帽图误差的接线。** 新96列有限提案 source 已给出并作必要入口核验；其全域求解、连续残差和最终数值误差仍须实际完成。本篇不把有限 QR 通过当作帽图误差或193态主体逆已经得到。

## 1. 同一个连续中心与真正物理角

使用准确连续值修复定义 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。它逐片在原 ac1 状态上加已经算出的完整65维 dyadic 常向量，保原目标、完整 even mean 和全部角模；原 ac1 文件不变。写

$$
 \bar u=\alpha U+e_u,
 \qquad \bar v=s+\alpha V+e_v,
 \qquad \bar m=\langle\bar v\rangle_\phi,
 \qquad \theta=\phi+\bar m^{-1}I(\bar v-\bar m).
 \tag{D.1}
$$

物理角反图必须保留；有限 moving Fourier 不被称为有限 physical Fourier。修复后的全频帽 Green 见 [连续中心帽及残差共轭篇](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)，原始完整源列和范数见 [实际全频物理帽 Green](R133-supplement-actual-final-all-mode-physical-cap-Green.md)。以下使用其中已经支付并在修复后仍有效的上取整数值。

在真正物理角中，方向为 $x=(b,c)=(\delta B,\delta C)$。令

$$
 q_B=2\bar u\circ\phi(\theta),\qquad
 q_C=\big[-\bar u^2-K(2s\delta v+\delta v^2)\big]\circ\phi(\theta),
 \quad\delta v=\alpha V+e_v,
 \quad Q_x=q_Bb+q_Cc.
 \tag{D.2}
$$

完整线性算子是

$$
\mathcal Lx=
\begin{pmatrix}
 b_r+2\beta b+\gamma\ell c_\theta-\gamma\partial_\theta Q_x\\
 c_r-\gamma b_\theta+\beta(\ell+1)c-\beta Q_x
\end{pmatrix}.
\tag{D.3}
$$

这只是准确微分 Gauss–Codazzi，不要求有限中心已经满足非线性方程。$ell=Ks^2$；(D.2) 中先消去两个径向大项，不能数值计算 `ell-u*u-K*v*v` 后假定它的小差准确。

## 2. 96 个独立输入和所有外端原行

记 $L=9/10,R=25/8$，并定义

$$
 J a=\sum_{j=1}^{96}a_j\cos(4j\theta),
 \qquad \|Ja\|_{L^2_\theta}=\|a\|_{\ell^2}/\sqrt2.
 \tag{D.4}
$$

真正帽解算子 $S$ 取 $c_{\ne0}(L)=Ja$，外端全部真正 homogeneous regular 行为零。它包含原第四 Robin、外 even mean；$c_0(L)$ 是输出。反射类使 $b_0=0$，一般无反射源则保全频帽定理的独立 $b_0(R)$，不得靠令 $M\to0$ 删除。

真正端口图为

$$
 \mathcal T a=(b_{\ne0}(L),c_0(L)).
 \tag{D.5}
$$

它的第一个分量有**全部**物理 Fourier 模。有限96列描述的是输入维数，不意味着输出或内部状态被截成96模。

允许任意完整、连续、分片绝对连续的矩阵提案 $\widehat S(r,\theta)$。当前新 producer 以193个 real physical 状态表示每列：96个 sine $b_j$、1个 mean $c_0$、96个 cosine $c_j$。数值求解保96条左输入行、97条右 mean/Robin 行，及一个单独零 dummy 以复用原 QR 存储。这个 dummy 没有体列，也没有改变任何物理行。

## 3. 完整连续误差合同

对每列定义准确残差 $R=\mathcal L\widehat S$，左误差 $E_L=P_{\ne0}\widehat c(L)-J$，右误差 $E_D,E_0$ 由**真正** nonlinear regular 导数行计算。若使用原 $q_j$ 浮点提案，它与真径向外线的差、真非线性导数、外源和均值费用都属于 $E_D,E_0$，不能免费置零。

允许把 $R_B,R_C$ 分成 ordinary 与 divergence 两部分。令 $r_B,r_C$ 分别是 ordinary 两分量作为
$\ell^2_{96}\to L_r^2L_\theta^2$ 算子的界；$d_B,d_C$ 是 divergence 原函数作为
$\ell^2_{96}\to\mathfrak M$ 的界，其中

$$
 \|f\|_{\mathfrak M}^2
 =\sum_{k\in4\mathbb Z}\sup_{r\in[L,R]}|f_k(r)|^2.
 \tag{D.6}
$$

仍按每个 Fourier 系数先取径向 supremum。它不能换成 $\sup_r\sum_k$。若提案有真实同物理角跳，令 $j_B,j_C$ 支付全部独立点源；连续 exact Hermite 提案则这两列严格为零。分别记边界算子误差为 $e_L,e_D,e_0,e_{B0}$。

已付全帽 Green 给

$$
\begin{aligned}
\|S-\widehat S\|_{\ell^2_{96}\to\mathfrak M^2}
\le\varepsilon_D:={}&
 13.316116 e_L+53.846164e_D+5.571744(e_0+e_{B0})\\
&+12.725633r_B+22.179140r_C\\
&+18.407084d_B+41.065564d_C\\
&+53.846164j_B+88.158880j_C.
\end{aligned}
\tag{D.7}
$$

这里 $\mathfrak M^2$ 是两个分量范数之和，与原帽定理完全相同。证明是对每个输入 $a$ 把 $Sa-\widehat Sa$ 写成负的完整误差数据的全帽 Green 解，再取 $\|a\|=1$ supremum。唯一性来自同一个完整帽逆，无需未知有限 Jacobi 行列式。

取左迹得到

$$
\boxed{\|\mathcal T-\widehat{\mathcal T}\|_{
 \ell^2_{96}\to L^2_{\ne0}\oplus_1\mathbb R}
 \le\varepsilon_D.}
\tag{D.8}
$$

若输出提案的 $j>96$ 槽为零，(D.8) **同时**控制真解输出的这些完整槽。它们必须由完整残差支付，而不是当成零输出删除。这正使帽图可以接有限 head 和无限 high 的统一 Schur。

ordinary 残差矩阵可用真实 Hilbert–Schmidt 界，例如

$$
 r_B\le\left(\sum_{j=1}^{96}
       \|R_B e_j\|_{L_r^2L_\theta^2}^2\right)^{1/2}.
 \tag{D.9}
$$

每个列范数须包含所有物理模、连续径向误差、真目标尾和舍入误差。它不能只取保留的193个 Galerkin 残差或径向节点上的值。物理 sine/cosine 的 $1/2$ Gram 和 even mean 的 Gram $1$ 贯穿 (D.7)–(D.9)。

## 4. 提案的完整径向定义

新 source 保存每个原背景接口节点的**同一组** dyadic 状态，以及两侧分别计算的完整径向导数。后验提案采用准确有理 Hermite 基函数：

$$
\widehat x(r)=H_{00}(t)x_i+H_{10}(t)h_i d_i^+
             +H_{01}(t)x_{i+1}+H_{11}(t)h_i d_{i+1}^-,
\quad t=(r-r_i)/h_i.
\tag{D.10}
$$

共享端值使相邻片严格连续，不再把四个展开系数分别舍入后产生值跳。径向导数可有已列明的单侧变化；(D.3) 及 ordinary 源使用各片真实导数。有限左端使用的 double `.9` 与准确 $9/10$ 的差也保留在元数据，后验须在真正 $L$ 评估首片定义并付 $E_L$，不能把两数称为同一有理数。

## 5. source、实际检查和下一门

新文件：

- [physical cap 模型](../scripts/fourfold_codazzi_physical_cap_head_model.py)：逐片准确重建修复 offsets，再为数值提案取其明确浮点值；物理反角的每次 Newton 迭代都检查实 Jacobian 正性。
- [96列完整 QR 提案](../scripts/fourfold_codazzi_physical_cap_DN_proposal.py)：完整矩阵 RHS、全部均值、原第四行和所有背景接口；每完成整块才推进检查点；独立完整 FFT action 的原后向门仍为 $5\cdot10^{-8}$。
- [公开 runner 入口](../scripts/fourfold_codazzi_physical_cap_DN_runner.py)：调用已发布公共六步恢复入口，在 runner 临时目录生成大数组，仅导出小实际报告和端口矩阵。

实际模型入口的完整列作用比较误差为 $1.732\cdot10^{-13}$，物理反角诊断残差为 $2.221\cdot10^{-16}$。新的 matrix-RHS QR 在一个完整7态、5节点、3独立输入系统上与独立稠密 LU 比较，误差 $<1.12\cdot10^{-15}$、全矩阵残差 $<5.56\cdot10^{-16}$。这只检验新代数接线，不授全帽误差。

当前真正的下一数值门是从提案的全 Hermite 数组付 (D.7) 的各项，再以 (D.8) 接 $[0,.9]$ 的完整193态连续投影及全 high 反馈。moving–physical 的残差敏感共轭仍由其独立普通/散度源费用接入；本篇没有省掉它。
