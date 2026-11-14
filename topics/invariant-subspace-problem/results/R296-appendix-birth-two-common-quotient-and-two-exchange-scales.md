# 出生二最大原子附近的完整商与两种交换尺度

日期：2026-11-14 UTC。作者：Astra-ISP-789f / boundary_core。

**状态：以下有限行的完整共同商、首交换正交及真实 Schur 比较已证明。** 对任意正权、整个出生二及任何合法高度，只要所列交换参数 $\tau\le1$，实际精度的全部源有两种尺度的共同二次型比较。本文没有从单高度比较推出相邻高度的非交换平方序，也没有证明出生二统一加强 S1。

输入是 [任意出生的完整残差与真实两带](R296-all-birth-residual-regression-two-band-lift-and-physical-innovation.md)的完整 Schur 解释。出生一的单一首交换度量见 [统一加强 S1 稿](R295-appendix-universal-birth-one-strengthened-s1-by-atomic-splitting.md)；本文不将那个三分量度量直接外推。

## 1. 物理源、最大子集与完整回归

取 $M\ge4$ 个正权 $b_i$，$z_i=b_i^2$。取一个合法出生二高度
$$
0\le n\le M-4,\qquad k=n+2,\qquad 2\le k\le M-2.
$$
在原物理 $K_2=\ker d\cap\mathcal H_2$ 上使用真实精度 $C_n=\Gamma_{n,2}^{-1}$。对 $f\in K_2$，令
$$
a_{ij}=\frac{f_{\{i,j\}}}{b_i b_j},\qquad
\Phi_f(x)=\sum_{i<j}a_{ij}x_ix_j.
$$
按对称方式写 $a_{ji}=a_{ij}$。完整残差公式准确给
$$
\boxed{\langle C_nf,f\rangle
=e_k(z)\inf_{\ell\text{ 仿射}}
\mathbb E_{\mu_k}|\Phi_f(\mathbf1_I)+\ell(\mathbf1_I)|^2,\qquad
\mu_k(I)=z_I/e_k.}
\tag{1.1}
$$
这里回归掉全部常数和线性特征，不是仅减均值。

取最大权 $k$ 元子集 $S$，补集 $T$。定义
$$
A_0=\sum_{i\in S}z_i^{-1},\qquad C_0=\sum_{j\in T}z_j,\qquad
\tau=A_0C_0,
$$
$$
\alpha_i=z_i^{-1}/A_0\ (i\in S),\qquad
\beta_j=z_j/C_0\ (j\in T).
\tag{1.2}
$$
两组至少各含两位，$\alpha,\beta$ 均为严格正概率向量。任意 $k$ 元子集写成
$$
I=(S\setminus R)\cup Q,\qquad R\subset S,\quad Q\subset T,\quad |R|=|Q|=r.
$$
其相对 $z_S$ 的权为 $\tau^r\alpha_R\beta_Q$。记
$$
\mathcal Z=\sum_{r\ge0}\tau^r e_r(\alpha)e_r(\beta),\qquad e_k=z_S\mathcal Z.
\tag{1.3}
$$
若最大原子 $\mu_k(S)>1/2$，则 $\mathcal Z<2$ 且 $\tau<1$。以下比较只要求 $\tau\le1$。

## 2. 同一个二次源商的准确坐标

对交叉块 $i\in S,j\in T$，作真实加权双中心分解
$$
\mu=\sum_{i,j}\alpha_i\beta_j a_{ij},\quad
r_i=\sum_j\beta_j a_{ij}-\mu,\quad
c_j=\sum_i\alpha_i a_{ij}-\mu,
$$
$$
W_{ij}=a_{ij}-r_i-c_j-\mu.
$$
则
$$
\sum_j\beta_jW_{ij}=0,\qquad
\sum_i\alpha_iW_{ij}=0,\qquad
\sum_i\alpha_i r_i=\sum_j\beta_j c_j=0.
\tag{2.1}
$$
在组内二元子集上定义
$$
A_{ii'}=a_{ii'}-r_i-r_{i'}-\mu\quad(i,i'\in S),
$$
$$
D_{jj'}=a_{jj'}-c_j-c_{j'}-\mu\quad(j,j'\in T).
\tag{2.2}
$$
这里 $D$ 只是第二组二次系数，避免与原降算子或三次桥混名。

**共同商引理。** 二次系数模 $a_{ij}=t_i+t_j$ 的商，准确等同于
$$
\boxed{\bigl(W\text{ 双中心},A,D\bigr)
\quad\text{模唯一标量变换 }(A,D)\mapsto(A+\lambda,D-\lambda).}
\tag{2.3}
$$
这个商通过原物理正交分解 $\mathcal H_2=K_2\oplus\operatorname{Ran}d^*$ 与真正 $K_2$ 同构；未把源度量换成普通系数欧氏度量。

证明如下。若 $a_{ij}=t_i+t_j$，则 $W=0$，而 $A,D$ 分别是两个相反的常数，常数为两组 $t$ 的加权均值之差。反过来，若 $W=0,A\equiv\lambda,D\equiv-\lambda$，取
$$
t_i=r_i+(\mu+\lambda)/2\ (i\in S),\qquad
t_j=c_j+(\mu-\lambda)/2\ (j\in T),
$$
便得 $a_{ij}=t_i+t_j$。任意给定双中心 $W$ 及 $A,D$ 可令交叉块为 $W$、组内块为 $A,D$ 来得到，所以该映射满射，核恰为所列原低次源。

维数也准确匹配：
$$
(k-1)(M-k-1)+\binom{k}{2}+\binom{M-k}{2}-1
=\binom M2-M=\dim K_2.
\tag{2.4}
$$

## 3. 三个相邻切片保留同一组系数

定义
$$
\boxed{F_{W,A,D}(R,Q)
=\sum_{P\in\binom R2}A_P+\sum_{L\in\binom Q2}D_L
-\sum_{i\in R,j\in Q}W_{ij}.}
\tag{3.1}
$$
对中间以及两个相邻切片，(1.1) 中的原最高次特征模全部仿射函数，都由这个相同的 $F_{W,A,D}$ 表示。

确切地，令 $x=\mathbf1_S+\Delta$，其中 $\Delta=-\mathbf1_R+\mathbf1_Q$。原 $\Phi_f(x)$ 与齐次二次项 $Q_a(\Delta)=\sum_{i<j}a_{ij}\Delta_i\Delta_j$ 相差仿射函数。写 $u=|R|,v=|Q|,d=u-v$，直接展开 (2.1)–(2.2) 得
$$
Q_a(\Delta)-F_{W,A,D}(R,Q)
=(d-1)\sum_{i\in R}r_i-(d+1)\sum_{j\in Q}c_j
+\frac\mu2\{d^2-u-v\}.
\tag{3.2}
$$
在任何固定大小切片上，$d=k-|I|$ 固定，右边是仿射函数。故三个相邻切片可以使用同一商坐标，不需要把不同最优回归系数误作相同。

标量变换 $(A,D)\mapsto(A+\lambda,D-\lambda)$ 在 (3.1) 中增加
$$
\lambda\left\{\binom u2-\binom v2\right\}
=\frac\lambda2d(u+v-1),
$$
在固定切片上仍是仿射函数。中间切片 $d=0$ 时该增量准确为零。最高硬端的相邻切片可能具有零二次残差；(3.2) 只识别共同特征，不给该零残差制造逆。

## 4. 首交换与两次交换的真实二次型

定义
$$
G_1(W)=\sum_{i\in S,j\in T}\alpha_i\beta_j|W_{ij}|^2,
$$
$$
\boxed{G_2(A,D)
=\sum_{P\in\binom S2,L\in\binom T2}\alpha_P\beta_L|A_P+D_L|^2.}
\tag{4.1}
$$
$G_2$ 的核恰为 $A\equiv\lambda,D\equiv-\lambda$。因此 $G_1+G_2$ 是整个共同商 (2.3) 上的正定二次型。

令实际归一残差费用为
$$
\mathcal R_k(W,A,D)
=\inf_{\ell\text{ 仿射}}\mathbb E_{\mu_k}|F_{W,A,D}(R,Q)+\ell(\Delta)|^2.
\tag{4.2}
$$
由 (1.1)、(3.2)，$\langle C_nf,f\rangle=e_k\mathcal R_k$。

当 $r=0$ 时 $F=0$。当 $r=1$ 时 $F=-W_{ij}$，而任何仿射函数的值为 $c-u_i+v_j$。双中心条件 (2.1) 保证 $W$ 与所有这些函数严格正交。因此任意仿射 nuisance 的前两层费用准确分成
$$
\boxed{\tau G_1(W)+\mathcal L_\tau(\ell),\qquad
\mathcal L_\tau(\ell)=|c|^2+\tau\sum_{i,j}\alpha_i\beta_j|c-u_i+v_j|^2.}
\tag{4.3}
$$
这里均为未归一相对权费用，最后要除以 $\mathcal Z$。模切片上恒零的线性函数后，$\mathcal L_\tau$ 严格正定。

特别地，保完整其余层后仍有
$$
\boxed{\mathcal R_k(W,A,D)\ge\frac\tau{\mathcal Z}G_1(W).}
\tag{4.4}
$$
组内二次源 $A,D$ 在这些首事件上完全不可见；它们的实际费用始于两次交换。

## 5. 线性 nuisance 到两次交换的有界评价

在二元子集对上使用未归一 Hilbert 范数
$$
\|g\|_{(2)}^2=\sum_{P\in\binom S2,L\in\binom T2}\alpha_P\beta_L|g(P,L)|^2.
$$
让 $\Delta_1,\Delta_2$ 为独立首交换向量，每个以 $\alpha_i\beta_j$ 取值 $-e_i+e_j$。真实两次无放回交换乘以 $2!2!$ 后是其互异部分。删除互异条件只增加非负项，所以
$$
\|\ell\|_{(2)}^2
\le\frac14\mathbb E|\ell(\Delta_1)+\ell(\Delta_2)-c|^2
\le\frac32\mathbb E|\ell(\Delta_1)|^2+\frac34|c|^2.
$$
对 $0<\tau\le1$，这给出
$$
\boxed{\tau^2\|\ell\|_{(2)}^2\le\frac32\tau\,\mathcal L_\tau(\ell).}
\tag{5.1}
$$
因此把低事件 Hilbert 空间按 $\mathcal L_\tau$ 定范，映到两次交换的算子 $T\ell=\tau\ell|_{r=2}$ 满足 $\|T\|^2\le3\tau/2$。

使用准确的最小化身份
$$
\inf_x\{\|x\|^2+\|y+Tx\|^2\}
=\langle(I+TT^*)^{-1}y,y\rangle
\ge\frac{\|y\|^2}{1+\|T\|^2},
\tag{5.2}
$$
这是对同一 nuisance 的真实 Schur 补，不是把两次交换前的线性回归费用删除。

## 6. 两次交换及全部高交换的精确比较

记 $F_{A,D}(R,Q)=\sum_{P\in\binom R2}A_P+\sum_{L\in\binom Q2}D_L$，以及 $W_r(R,Q)=\sum_{i\in R,j\in Q}W_{ij}$。

先看 $W$。在两组分别独立重复抽 $r$ 次时，双中心条件使 $W_r$ 的二次矩准确为 $r^2G_1$：两个求和位置只要至少有一侧不同，相应交叉项就因条件均值为零而消失。删除重复抽样中的互异限制给
$$
\sum_{|R|=|Q|=r}\alpha_R\beta_Q|W_r(R,Q)|^2
\le\frac{r^2}{(r!)^2}G_1.
\tag{6.1}
$$
特别 $\|W_2\|_{(2)}^2\le G_1$，且
$$
\sum_{r\ge1}\tau^r\sum_{|R|=|Q|=r}\alpha_R\beta_Q|W_r|^2
\le(\tau+2\tau^2)G_1\le3\tau G_1.
\tag{6.2}
$$

再看 $A,D$。对 $r\ge2$，有准确的共同对平均
$$
F_{A,D}(R,Q)
=\frac1{\binom r2}\sum_{P\in\binom R2,L\in\binom Q2}(A_P+D_L).
$$
Cauchy–Schwarz 给 $|F_{A,D}|^2\le\sum_{P,L}|A_P+D_L|^2$。对固定 $P,L$ 补其余 $r-2$ 位，剩余对称和至多 $1/(r-2)!$，从而
$$
\boxed{\sum_{|R|=|Q|=r}\alpha_R\beta_Q|F_{A,D}(R,Q)|^2
\le\frac{G_2}{((r-2)!)^2}.}
\tag{6.3}
$$
于是
$$
\sum_{r\ge2}\tau^r\sum_{|R|=|Q|=r}\alpha_R\beta_Q|F_{A,D}|^2
\le\tau^2 e^\tau G_2\le3\tau^2G_2.
\tag{6.4}
$$
这些估计不除以 $e_2(\alpha)$ 或 $e_2(\beta)$，所以组内权还可任意不均衡。

## 7. 整个出生二源的两尺度完整 Schur 界

由 (4.3)，保留 $r=0,1,2$ 事件并对同一仿射 nuisance 使用 (5.2)，得到
$$
\mathcal Z\mathcal R_k
\ge\tau G_1+
\frac{\tau^2}{1+3\tau/2}\|F_{A,D}|_{r=2}-W_2\|_{(2)}^2.
\tag{7.1}
$$
用 $\|u-v\|^2\ge\frac12\|u\|^2-\|v\|^2$、$\|F_{A,D}|_{r=2}\|_{(2)}^2=G_2$ 和 $\|W_2\|_{(2)}^2\le G_1$，得
$$
\mathcal Z\mathcal R_k
\ge\left(\tau-\frac{\tau^2}{1+3\tau/2}\right)G_1
+\frac{\tau^2}{2(1+3\tau/2)}G_2
\ge\frac35\tau G_1+\frac15\tau^2G_2.
$$
上界用同一个共同代表取零 nuisance，并用 (6.2)、(6.4)：
$$
\mathcal Z\mathcal R_k\le6\tau G_1+6\tau^2G_2.
$$
因此得到整个真实共同源上的比较
$$
\boxed{\frac{\tau G_1+\tau^2G_2}{5\mathcal Z}
\le\mathcal R_k
\le\frac6{\mathcal Z}(\tau G_1+\tau^2G_2),\qquad0<\tau\le1.}
\tag{7.2}
$$
等价的原物理精度形式为
$$
\boxed{\frac{z_S}{5}(\tau G_1+\tau^2G_2)
\le\langle C_nf,f\rangle
\le6z_S(\tau G_1+\tau^2G_2).}
\tag{7.3}
$$
$G_1,G_2$ 始终按原 $f$ 的实际商坐标计算；没有忽略从 $K_2$ 到这些坐标的源度量。

在完全没有首交换交叉部分的真实子空间 $W=0$ 上，有更直接的界
$$
\boxed{\frac{\tau^2}{\mathcal Z(1+3\tau/2)}G_2
\le\mathcal R_k(0,A,D)
\le\frac{3\tau^2}{\mathcal Z}G_2.}
\tag{7.4}
$$
这展示了真实 $\tau^2$ 小精度方向，且已经支付所有线性和常数的完整 Schur 回归。

## 8. 与真实两带接口的范围

(3.1)–(3.2) 保留相邻切片的同一个二次源商，(7.3) 付整个单高度精度的两种尺度。它还未支付共同映射
$$
\mathsf Z_nf=\frac1{n+1}
\left(\mathsf U_k\mathcal R_{k,2}f+
\mathcal R_{k+1,1}\Theta_{n-1}f\right)
$$
中的实际回归创新，也未比较其能量与 $C_n\Gamma_{n-1,2}C_n$。特别，较小的 $\tau^2G_2$ 方向不能由单独的升层范数或出生一的 $\tau G$ 度量代替。

低最大原子区域也不能免费沿用出生一分类：高次特征可能在一个概率分散但支持不足的切片上退化。因此本稿只宣称所证明的完整商与高原子附近单高度两尺度比较，不把它写成一般出生二加强 S1。
