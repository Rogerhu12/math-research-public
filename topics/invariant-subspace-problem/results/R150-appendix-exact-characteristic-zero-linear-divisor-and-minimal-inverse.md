# R150 continuation：原线性块的 46 次确定因子与最小逆分母

作者：normal_annihilator / 789f。2026-11-14 UTC。

状态：以下是原矩阵在 $\mathbb Q[s]$ 上的精确结论。它计算全部九阶子式的 gcd 及横向线性逆的最小共同分母；**没有把原非线性方程中的二次项删去，也不单独推出原十七式的目标归属。**

## 1. 原线性矩阵与真正的单位补空间

在原六模式数据中，令 $D=\det J_3$，$B_s$ 为原物理极式 $p_s(z)=v(s)^TKv(z)$ 的乘法矩阵。原十一条 $N$ 方程的线性部分在清除固定分母、尚未除各行整数内容时为

$$
N_{\mathrm{lin}}(s)=6J_2B_s^T\operatorname{adj}(J_3)B_sJ_2.
$$

这是 $6D J_2 A_{v(s)}$，所以与原 $A_y$ 有相同的秩及参数确定因子，只差固定可逆常矩阵和非零常数。

令

$$
u(s)=(1,s,\ldots,s^{10})^T,\qquad u'(s)=\frac{d}{ds}u(s).
$$

从原数据完整组矩阵后，已逐项核得对称性及两个多项式恒等式

$$
N_{\mathrm{lin}}u=N_{\mathrm{lin}}u'=0.
$$

取真正的多项式矩阵

$$
T(s)=[u(s),u'(s),e_2,\ldots,e_{10}].
$$

它的左上两阶块为 $\bigl(\begin{smallmatrix}1&0\\s&1\end{smallmatrix}\bigr)$，其余补列为标准坐标，故 $\det T=1$。因此 $T$ 在 $\mathbb Q[s]$ 上是单位矩阵变换，而不只是函数域上可逆。

由对称性及双核恒等式，

$$
T^TN_{\mathrm{lin}}T=\begin{pmatrix}0_{2\times2}&0\\0&S(s)\end{pmatrix},
\qquad S=(N_{\mathrm{lin}})_{\{2,\ldots,10\},\{2,\ldots,10\}}.
$$

这证明原线性块的全部九阶子式理想由 $\det S$ 生成。无需把某一个普通子式误当全部 gcd，也无需枚举 3025 个九阶子式。

## 2. 精确九阶行列式

[脚本](../notes/2026-11-14-r150-linear-operator-divisor-789f.py)直接从原 $K,\operatorname{adj}J_3,D$ 组出多项式矩阵，使用整多项式 Bareiss 消元；每一步除法都核对余式为零。固定 $D$ 为

`23366320238786911411830138211362846399922176000`。

去掉 $\det S$ 的非零整数内容后，完整因式分解为

$$
\boxed{D_{\mathrm{lin}}(s)
=s^8(s-2)^2(s+6)^2F_+(s)^3F_-(s)^3E_8(s)^2,}
$$

其中

$$
F_+=5s^3-25s^2+32s-8,\qquad
F_-=5s^3+135s^2+864s+864,
$$

$E_8$ 是原八次式。因此

$$
\deg D_{\mathrm{lin}}=8+2+2+9+9+16=46.
$$

这是特征零原线性块的整个九阶确定因子。原始矩阵、双核及对称检查、Bareiss 主元次数、行列式整数内容、全部 primitive 升幂系数及因子都保存在[精确回执](../notes/2026-11-14-r150-linear-operator-divisor-receipt-789f.json)。计算受 60 秒、512 MiB 上限约束，实际用时 **0.081225842 秒**，退出码 0；依赖版本为 python-flint 0.9.0 / FLINT 3.6.0。

## 3. 横向线性逆的最小共同分母

已有[原精确秩定理](R150-appendix-rank-one-centered-linear-operator-exact-rank.md)证明：在 $D_{\mathrm{lin}}$ 的每个复根上，原 $A_y$ 的秩准确为 8；其余有限点秩为 9。上节单位合同给

$$
\operatorname{rank}S(s)=\operatorname{rank}N_{\mathrm{lin}}(s)
$$

于每个有限参数成立。于是每个 $\det S$ 的根处，$S$ 只降一秩，至少一个八阶子式非零。故全部八阶子式的 gcd 是非零常数，$\operatorname{adj}S$ 的所有条目没有共同非恒定因子。

由 $S^{-1}=\operatorname{adj}S/\det S$，其全部有理函数条目的最小共同参数分母恰为

$$
\boxed{D_{\mathrm{lin}},\quad\deg=46.}
$$

这同时排除了“原九目标的 24 次模 31 分母只是直接取一个横向线性逆”的解释；不需要另作重复余子式计算。

## 4. 与 24 次目标候选的准确关系

由[九目标完整向量结果](../notes/2026-11-14-r150-nine-targets-common-annihilator-789f.md)得到的特征零候选为

$$
h_0=s^3(s-2)F_+^2F_-^2E_8.
$$

它准确整除 $D_{\mathrm{lin}}$，且

$$
\frac{D_{\mathrm{lin}}}{h_0}=s^5(s-2)(s+6)^2F_+F_-E_8
$$

次数为 22。因此候选的支撑落在真实线性退化集合中，重数小于一般线性逆所需重数。

原完整 $N$ 方程仍含 $4MKM$ 二次项，全部六条 $\Gamma$ 也仍需保留。本条没有从 $A_yM$ 的线性性质推出 $A_yM=0$，没有证明 $h_0T$ 已在特征零原理想中。这里确定的是一个精确且可用于后续提升的线性分母边界。
