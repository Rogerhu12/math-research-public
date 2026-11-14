# R222：共同乘积循环向量、精确 ℓ^{4/3} 尾条件与有限秩湮灭泛函的可排类

日期：2026-11-13（UTC+8）。作者：normal_states。

状态：以下共同换因子构造及有限秩排除结论完整。没有证明任意有限秩泛函都落在本类，没有证明任意有限个乘积向量的非零线性组合都循环。这里直接针对慢主理想的有限秩接口，不把稠密向量类误当全空间。

## 1. 与主目标匹配的陈述

令 $H=L^2(\mathbb Z_2,\mu)$，$\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|}$。设 $S\in\{A\}'$ 在全 $H$ 上具有稠密像。特别可取已经证明全空间稠密像的 $S_N$ 或 $S_Y$。

给定有限个向量
$$
f_\nu=v_\nu\otimes h^{(\nu)}_{\ge d},\qquad 1\le\nu\le q,
\tag{1.1}
$$
其中 $v_\nu\in\mathbb C^{2^d}$ 为任意有限前缀，每个 $h^{(\nu)}$ 为 R16 的归一化收敛无限乘积尾。扩大 $d$ 可吸收各向量不同的有限前缀及有限个首坐标为零的局部因子，因此可设
$$
t_j^{(\nu)}=\frac{h_j^{(\nu)}(1)}{h_j^{(\nu)}(0)}
\quad(j\ge d)
$$
全部有定义。R16 收敛性给
$$
t^{(\nu)}-1\in\ell^2.
\tag{1.2}
$$

假设物理比率的虚部差满足
$$
\boxed{
\operatorname{Im}(t^{(\nu)}-t^{(1)})\in\ell^{4/3}
\quad(1\le\nu\le q).
}
\tag{1.3}
$$
条件允许各实部差为任意慢的 $\ell^2$ 尾，不要求其在 $\ell^1$。特别，全部物理比率最终为实数时自动满足；共同的任意复杂 $\ell^2$ 虚部也允许。

**定理1.1。** 存在一个 R16 循环向量 $g$，以及真正有界的 $C_\nu\in\{A\}'$，使
$$
f_\nu=C_\nu g\quad(1\le\nu\le q).
\tag{1.4}
$$
每个 $C_\nu$ 都由 $\mathcal A$ 中一致有界的有限换因子乘积的强极限，再乘一个真正有限多项式得到。因此它与每个 $S\in\{A\}'$ 交换。

**推论1.2。** 存在多项式序列 $p_n$，同时满足
$$
Sp_n(A)f_\nu\longrightarrow f_\nu\quad(1\le\nu\le q).
\tag{1.5}
$$
更一般，同一序列可在共同代数模 $\{Cg:C\in\{A\}',\ CS=SC\}$ 的每个固定向量上作此逼近。

因此，若有限秩泛函
$$
\phi(T)=\sum_{\ell=1}^r\langle Tx_\ell,y_\ell\rangle
\tag{1.6}
$$
的全部第一因子 $x_\ell$ 属于 (1.1) 各向量的有限线性张成，并且
$$
\boxed{\phi(SF)=0\quad(F\in\mathcal A),}
\tag{1.7}
$$
则必有 $\phi(I)=0$。第二因子 $y_\ell$ 可以是任意 $H$ 向量，无正则性条件。

尤其，任何非零正有限秩算子 $\rho$，若 $\operatorname{Ran}\rho$ 包含于该有限张成，就不能给出满足 (1.7) 的正泛函 $\operatorname{Tr}(\rho\,\cdot)$。本结论使用的正是 $S\mathcal A$ 的湮灭条件，不暗中将它加强为 $S\{A\}'$ 的湮灭条件。

## 2. 一个准确的共同尾几何判据

下述序列引理既给 (1.3) 的构造，也说明指数 $4/3$ 对这里采用的单侧亏量条件是准确的。

**引理2.1。** 设有限行 $t^{(\nu)}-1\in\ell^2$。以下两条等价：

1. 所有 $\operatorname{Im}(t^{(\nu)}-t^{(1)})\in\ell^{4/3}$；
2. 存在 $s-1\in\ell^2$，使每条
   $$
   \sum_j\left(|t_j^{(\nu)}-s_j|-\operatorname{Re}(t_j^{(\nu)}-s_j)\right)<\infty.
   \tag{2.1}
   $$

这里只判定明确的 (2.1)，不声称它是所有可能有界换因子的必要条件。

### 2.1 充分方向与可见的共同参考行

置
$$
b_j^{(\nu)}=\operatorname{Im}(t_j^{(\nu)}-t_j^{(1)}),\qquad
w_j=\left(\sum_{\nu=1}^q|b_j^{(\nu)}|^2\right)^{1/3},
$$
$$
v_j=\max\bigl(0,\,1-\operatorname{Re}t_j^{(1)},\ldots,
1-\operatorname{Re}t_j^{(q)}\bigr),\qquad
s_j=1-v_j-w_j+i\operatorname{Im}t_j^{(1)}.
\tag{2.2}
$$
有限个 $\ell^2$ 行的逐项最大值仍在 $\ell^2$，所以 $v\in\ell^2$。且
$$
\sum_jw_j^2
=\sum_j\left(\sum_\nu|b_j^{(\nu)}|^2\right)^{2/3}
\le\sum_\nu\sum_j|b_j^{(\nu)}|^{4/3}<\infty.
$$
故 $s-1\in\ell^2$。

令 $\delta_j^{(\nu)}=t_j^{(\nu)}-s_j=p_j^{(\nu)}+ib_j^{(\nu)}$。有
$p_j^{(\nu)}\ge w_j\ge0$。当 $w_j>0$ 时，
$$
|\delta_j^{(\nu)}|-p_j^{(\nu)}
=\frac{|b_j^{(\nu)}|^2}{|\delta_j^{(\nu)}|+p_j^{(\nu)}}
\le\frac{|b_j^{(\nu)}|^2}{2w_j}.
$$
对 $\nu$ 相加，右边为 $w_j^2/2$。当 $w_j=0$ 时，全部 $b_j^{(\nu)}=0$，且亏量准确为0。因此
$$
\sum_{\nu,j}\bigl(|\delta_j^{(\nu)}|-\operatorname{Re}\delta_j^{(\nu)}\bigr)
\le\tfrac12\sum_jw_j^2<\infty.
\tag{2.3}
$$

### 2.2 必要方向

若 (2.1) 成立，固定一条 $\delta=t^{(\nu)}-s\in\ell^2$，记
$d_j=|\delta_j|-\operatorname{Re}\delta_j\ge0$，则 $d\in\ell^1$。准确恒等式给
$$
|\operatorname{Im}\delta_j|^2
=d_j\bigl(|\delta_j|+\operatorname{Re}\delta_j\bigr)
\le2d_j|\delta_j|.
$$
由 Hölder 不等式，
$$
\sum_j|\operatorname{Im}\delta_j|^{4/3}
\le2^{2/3}
\left(\sum_jd_j\right)^{2/3}
\left(\sum_j|\delta_j|^2\right)^{1/3}<\infty.
$$
两条这样的虚部相减，便有 (1.3)。引理得证。

## 3. 共同参考行确实给收敛 Haar 乘积

扩大有限前缀后可设 $s_j$ 都在1的固定小邻域。取局部归一化函数
$$
g_j(0)=\frac{\sqrt2\,e^{-i\arg(1+s_j)}}{\sqrt{1+|s_j|^2}},
\qquad g_j(1)=s_jg_j(0).
\tag{3.1}
$$
局部均值为正数
$$
\mu_j=\frac{|1+s_j|}{\sqrt{2(1+|s_j|^2)}}.
$$
且
$$
1-\mu_j^2=\frac{|1-s_j|^2}{2(1+|s_j|^2)}.
$$
所以 $\sum_j(1-\mu_j)<\infty$；这些局部函数的归一化无穷乘积在 Haar $L^2$ 中收敛到范数1的尾向量。

令 $e_0$ 为低 $d$ 位整数0的单位物理基向量，定义
$$
g=e_0\otimes g_{\ge d}.
\tag{3.2}
$$
R16 的有限前缀定理证明 $g$ 是实际 $A$ 的循环向量。

为说明 (1.2) 没有增加隐含假设：R16 的乘积收敛给各局部函数 $h_j\to1$，同时尾均值乘积趋于1。因此
$\sum_j(1-|\mu_j^h|^2)<\infty$。局部恒等式
$$
1-|\mu_j^h|^2=\tfrac14|h_j(0)-h_j(1)|^2
$$
再结合最终 $h_j(0)$ 远离0，便得到 $h_j(1)/h_j(0)-1\in\ell^2$。

## 4. 真 carry 下的有限换因子一致界

固定 $\nu$，略去上标。令
$$
W_j=\frac{h_j(0)}{g_j(0)}
(I+t_jN_j)(I+s_jN_j)^{-1},\qquad
Y_n=\prod_{d\le j<n}W_j.
\tag{4.1}
$$
$N_j$ 是实际 $A$ 的归一化幂；因其拟幂零，分母对每个复 $s_j$ 均在 $\mathcal A$ 中可逆。因此每个 $Y_n\in\mathcal A$。

下面重写 R127 §6 所需的预算，保留真实 carry。设
$$
W_j^0=\frac{h_j(0)}{g_j(0)}(I+\delta_jE_j),\qquad \delta_j=t_j-s_j.
$$
高位 $s_j,t_j$ 一致有界且趋1，二次关系 $N_j^2=\eta_jN_{j+1}$ 给 $(I+s_jN_j)^{-1}$ 一致有界。又
$$
N_j(I+s_jN_j)^{-1}-E_j
=(N_j-E_j)-s_jN_j^2(I+s_jN_j)^{-1},
$$
故
$$
\|W_j-W_j^0\|\le C|\delta_j|\eta_j.
\tag{4.2}
$$
所有常数在这个固定有限族上统一。因为 $\eta\in\ell^1$、$\delta\in\ell^2$，右边可和。

纯剪切矩阵的精确奇异值给
$$
\log\|W_j^0\|
=\tfrac12\log\frac{1+|s_j|^2}{1+|t_j|^2}
+\operatorname{arsinh}(|\delta_j|/2).
$$
在1附近展开前一项，使用 $\operatorname{arsinh}u\le u$，得到
$$
\log\|W_j^0\|
\le\tfrac12(|\delta_j|-\operatorname{Re}\delta_j)
+C(|s_j-1|^2+|t_j-1|^2).
\tag{4.3}
$$
$\|W_j^0\|\to1$，因此 (4.2) 只再增加 $C|\delta_j|\eta_j$ 的对数上界。由 (2.1)，全部右侧总和有限，有限个早期因子只改变常数。因此
$$
\boxed{\sup_n\|Y_n\|<\infty.}
\tag{4.4}
$$
没有把有限局部压缩当成乘法，也没有先删除真实 carry 后直接宣称有界。

## 5. 精确局部替换与真正强极限

在第 $j$ 位，输入 $g_j\otimes u$ 准确等于
$$
\frac{g_j(0)}{\sqrt2}(I+s_jN_j)(e_0^{(j)}\otimes u),
$$
因为真实递推中的 carry 项在该位 $e_0^{(j)}$ 上为零。因此 $W_j$ 准确把该位的局部因子 $g_j$ 换成 $h_j$，不改变其余尾向量。

于是
$$
Y_ng=e_0\otimes\left(\prod_{d\le j<n}h_j\right)\otimes g_{\ge n}
\longrightarrow e_0\otimes h_{\ge d}.
\tag{5.1}
$$
这个收敛来自两个乘积尾都趋于 Haar 参考向量，不需要它们有任何指定的收敛速度。

每个 $Y_n$ 与 $A$ 交换，故在 $g$ 的稠密多项式轨道上也逐点收敛。(4.4) 使其延拓为全空间强极限 $Y\in B(H)$，并有 $YA=AY$。此外，每个 $S\in\{A\}'$ 都与每个 $Y_n$ 交换，强极限给
$$
SY=YS.
\tag{5.2}
$$

最后，存在真正有限多项式 $p_v$，使
$$
p_v(A)(e_0\otimes u)=v\otimes u
\tag{5.3}
$$
对任意尾向量 $u$ 成立。确实，$A^ne_0$ 对 $0\le n<2^d$ 只沿低头链前进，不发生出头进位；每步权均非零，用各链权乘积除各目标坐标即可定义 $p_v$。

对每个 $\nu$ 构造对应 $Y_\nu$，置
$$
C_\nu=p_{v_\nu}(A)Y_\nu.
$$
(5.1)—(5.3) 给 $C_\nu g=f_\nu$，完成定理1.1。

## 6. 稠密像如何真正给同时主理想逼近

由于 $g$ 循环，$\{p(A)g:p\in\mathbb C[z]\}$ 在 $H$ 稠密。$S$ 有界，故其像的闭包等于 $\overline{SH}=H$：任意 $Sh$ 可用 $Sp(A)g$ 逼近，再用 $SH$ 的稠密性逼近任意目标。因此可选多项式 $p_n$，使
$$
Sp_n(A)g\longrightarrow g.
\tag{6.1}
$$

由已证的 $C_\nu S=SC_\nu$ 和 $C_\nu A=AC_\nu$，
$$
Sp_n(A)f_\nu-f_\nu
=C_\nu\bigl(Sp_n(A)g-g\bigr)\longrightarrow0.
$$
这证明 (1.5)，并对有限线性组合保持成立。

若 (1.6)—(1.7) 成立，只使用 $p_n(A)\in\mathcal A$ 就有
$$
0=\phi(Sp_n(A))\longrightarrow\sum_\ell\langle x_\ell,y_\ell\rangle=\phi(I).
$$
所以本证明没有把 $\phi$ 对 $S\mathcal A$ 的湮灭未经解释地扩展到 $S\{A\}'$；实际的近单位元素本身就是 $Sp_n(A)\in S\mathcal A$。

也可直接写出循环第一因子分解：若 $x_\ell=D_\ell g$，则对任何 $F\in\mathcal A$，
$$
\phi(F)=\left\langle Fg,\sum_\ell D_\ell^*y_\ell\right\rangle.
$$
由于该第二因子正交于稠密的 $S\mathcal A g$，它为零，特别 $\phi(I)=0$。

## 7. 例子与准确的剩余缺口

### 7.1 任意慢实乘积尾

只要每个 $t_j^{(\nu)}$ 最终为实数且 $t^{(\nu)}-1\in\ell^2$，(1.3) 自动成立。相应乘积向量可以具有任意慢的 Haar 柱尾收敛；它们的任意有限线性张成依然属于本条有限秩排除类。

这比“柱尾快于某个固定指数”的充分条件覆盖不同的向量：这里允许没有任何指定下降速度的实乘积尾。也没有要求这些有限和本身已经被证明循环。

### 7.2 真正允许非实相对尾

例如两条比率的虚部差 $b_j=(j+2)^{-p}$，当 $p>3/4$ 时满足 (1.3)，即使 $p\le1$ 使其不可绝对可和。各实部差仍可任取 $\ell^2$ 行。更一般，可在任意共同复杂 $\ell^2$ 背景虚部上加入这些相对差。

### 7.3 此共同因子机制的明确边界

若取 $t_j^{(1)}=1$、$t_j^{(2)}=1+i(j+2)^{-2/3}$，两条都是合法 $1+\ell^2$ 比率，却有虚部差不在 $\ell^{4/3}$。引理2.1 说明不存在任何 $s-1\in\ell^2$ 同时使两条单侧亏量可和。

这只阻止本文使用 R127 单侧亏量界构造共同乘积生成向量；没有否定其他有界换因子、非乘积循环生成向量或完整有限秩分解存在。

一般有限秩正常泛函的第一因子可以是任意 $L^2$ 向量，未必在这里的有限产品张成中。稠密的可排类仍不能通过取闭包排除全部见证，因为 (6.1) 的逼近多项式没有统一算子范数界。普通 Hilbert ISP 与慢符号在所有未知不变子商上的性质均未因此完成。

## 内部依赖

R16 的收敛乘积与任意有限前缀循环性；R127 §6 的真实换因子方法（所需范数预算与强极限在本文 §§4–5 重新写出）；真实 dyadic 递推及 $\eta\in\ell^1$。不使用未知的全体有限产品和循环性，也不使用正常泛函固定真空因子分解。
