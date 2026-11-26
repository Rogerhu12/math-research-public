# 原奇幂的有界强多项式恢复、全部幂交换子与实际不变子商

作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。日期：2026-11-27（Asia/Taipei）。

**状态：完整证明的正向结构结论。** 对每个原 Haar 尾 $B_m$ 和每个奇数 $p$，原算子 $B_m$ 是 $B_m^p$ 的一致有界多项式的强极限。因此 $B_m$ 与 $B_m^p$ 有完全相同的普通闭不变子空间、完整交换子和强闭多项式代数。一般 $p$ 的这些对象只取决于 $v_2(p)$，且全空间交换子有准确有限重数模型。相同的多项式恢复也下降到每个真实闭不变旗的子商。

本稿不假定普通不变空间受 Deddens 保持，也不把未知子商重新识别为原完整尾。它没有构造非零真不变空间；新增的是能在同一实际空间、同一实际未知子商上使用的有界强逼近。

## 1. 原尾的准确归一化位

沿用[原尾有界根正文](../results/R12-appendix-tail-root-multiplicity-and-all-invariant-projection-distances.md)：
$$
B_mf(z)=\alpha_{m+v_2(z)}f(z-1),\qquad B_0=A,
$$
$$
\beta^{(m)}_n=\|B_m^n\|,\qquad
L_j=-\log\alpha_j
=\frac{280}{3}16^j-90\,8^j+300\,2^j-\frac{850}{3}.
$$
零点的权仍按原定义取零。对 $j\ge0$ 令
$$
d^{(m)}_j=\|B_m^{2^j}\|,\qquad
N^{(m)}_j=\frac{B_m^{2^j}}{d^{(m)}_j}.
\tag{1.1}
$$
令 $E_j=e_{10}^{(j)}$ 为第 $j$ 个物理位的独立升算子，其他位上取恒等。

准确整头循环给
$$
B_m^{2^j}
=\beta^{(m)}_{2^j-1} I_{2^j}\otimes B_{m+j},
\qquad
d^{(m)}_j=\beta^{(m)}_{2^j-1}\alpha_{m+j}.
\tag{1.2}
$$
因此真实首位进位式为
$$
N^{(m)}_j=E_j+\eta^{(m)}_jE_j^*N^{(m)}_{j+1},
\qquad
\eta^{(m)}_j=\frac{\alpha_{m+j+1}}{\alpha_{m+j}},
\tag{1.3}
$$
且
$$
\|N^{(m)}_j\|=\|E_j\|=1,\qquad
\|N^{(m)}_j-E_j\|=\eta^{(m)}_j.
\tag{1.4}
$$
这里 $N^{(m)}_{j+1}$ 在第 $j$ 位上为恒等，故 (1.3) 的张量位置准确。

原权差满足
$$
L_{t+1}-L_t
=1400\,16^t-630\,8^t+300\,2^t
\ge770\,16^t,
$$
从而
$$
0<\eta^{(m)}_j\le e^{-770\,16^{m+j}},
\qquad C_m:=\sum_{j\ge0}\eta^{(m)}_j<\infty.
\tag{1.5}
$$

对任意有限位集合 $G$，置
$$
V_G=\prod_{j\in G}N^{(m)}_j,\qquad F_G=\prod_{j\in G}E_j.
$$
前者是一个实际 $B_m$ 单项式；每个因子范数为一，所以
$$
\|V_G\|\le1,\qquad \|F_G\|=1.
$$
按递增位次序作乘积 telescoping，无需混合的 $N^{(m)}_j,E_i$ 交换，得到
$$
\boxed{\|V_G-F_G\|\le\sum_{j\in G}\eta^{(m)}_j.}
\tag{1.6}
$$

## 2. 同一个固定奇数 p 的明确高位组

现在固定奇数 $p\ge3$。令
$$
a=p-1=\sum_{j\in J}2^j,\qquad k=|J|\ge1.
\tag{2.1}
$$
因 $p$ 为奇数，$2$ 在模 $p$ 下可逆；存在正整数 $d$ 满足 $2^d\equiv1\pmod p$。取 $h$ 为 $d$ 的正整数倍，且
$$
h>\max J.
$$
于是下面的位组两两不交：
$$
G_\nu=J+h\nu,\qquad \nu=1,2,\ldots.
\tag{2.2}
$$
其位和为
$$
n_\nu=\sum_{j\in G_\nu}2^j=a2^{h\nu}\equiv-1\pmod p.
\tag{2.3}
$$
记
$$
D_\nu=\prod_{j\in G_\nu}d^{(m)}_j>0.
$$
则准确有
$$
V_{G_\nu}=\frac{B_m^{n_\nu}}{D_\nu}.
\tag{2.4}
$$
这里没有通过约去一个不满射算子来定义单项式。

定义实际平均
$$
R_L=\frac{2^k}{L}\sum_{\nu=1}^L V_{G_\nu},
\qquad
S_L=\frac{2^k}{L}\sum_{\nu=1}^L F_{G_\nu}.
\tag{2.5}
$$
由范数三角不等式，
$$
\boxed{\|R_L\|\le2^k,\qquad \|S_L\|\le2^k.}
\tag{2.6}
$$
由位组不交和 (1.6)，全部真实 carry 误差满足
$$
\boxed{\|R_L-S_L\|\le\frac{2^kC_m}{L}\longrightarrow0.}
\tag{2.7}
$$

## 3. 在原 Haar 向量上的强极限

**引理 3.1。** $R_L\to I$ 强收敛。

**证明。** 先取任意有限柱向量 $f$。选 $\nu_0$ 使 $\nu\ge\nu_0$ 时，$G_\nu$ 的全部位都高于 $f$ 的支持。由于原参考向量在每个位上为 $(e_0+e_1)/\sqrt2$，
$$
F_{G_\nu}f=\mathbf1_{E_\nu}f,\qquad
E_\nu=\{y:y_j=1\text{ 对每个 }j\in G_\nu\}.
\tag{3.1}
$$
这些事件互相独立、独立于 $f$，且 $\mu(E_\nu)=2^{-k}$。故
$$
\left\|
\frac{2^k}{L}
\sum_{\nu=\nu_0}^{L}
(F_{G_\nu}-2^{-k}I)f
\right\|^2
=\frac{(L-\nu_0+1)(2^k-1)}{L^2}\|f\|^2.
\tag{3.2}
$$
有限个初始组给至多
$$
\frac{(2^k+1)(\nu_0-1)}L\|f\|
$$
的误差。结合 (2.7)，对充分大的 $L$ 有完整实际界
$$
\|(R_L-I)f\|
\le
\left[
\sqrt{\frac{2^k-1}{L}}
+\frac{(2^k+1)(\nu_0-1)+2^kC_m}{L}
\right]\|f\|.
\tag{3.3}
$$
因此 $R_Lf\to f$。有限柱稠密，且 (2.6) 一致控制算子范数，故强收敛在全部原 $K$ 上成立。证毕。

## 4. 奇幂的实际多项式恢复

由 (2.3)，每个 $n_\nu+1$ 为 $p$ 的正整数倍。因此
$$
B_mR_L
=\frac{2^k}{L}\sum_{\nu=1}^L
\frac{(B_m^p)^{(n_\nu+1)/p}}{D_\nu}
=:q_L(B_m^p)
\tag{4.1}
$$
是 $B_m^p$ 的实际有限多项式，甚至没有常数项。由 (2.6) 和引理 3.1，
$$
\boxed{
q_L(B_m^p)\longrightarrow B_m\ \text{强},
\qquad
\sup_L\|q_L(B_m^p)\|
\le2^{s_2(p-1)}\|B_m\|.
}
\tag{4.2}
$$
这里 $s_2(a)$ 是 $a$ 的二进制一位数。对奇数 $p\ge3$，$2^{s_2(p-1)}\le p-1$。$p=1$ 的恢复取恒等多项式即可。

**定理 4.1。** 对每个 $m\ge0$、每个正奇数 $p$，
$$
\boxed{
\operatorname{Lat}(B_m^p)=\operatorname{Lat}(B_m),
\qquad
\{B_m^p\}'=\{B_m\}'.
}
\tag{4.3}
$$
两者生成的含单位强闭多项式代数也相同。

**证明。** 若闭空间 $M$ 被 $B_m^p$ 保持，则被每个 $q_L(B_m^p)$ 保持。逐向量取 (4.2) 的强极限，$B_mM\subseteq M$。反向由取幂立即成立。

若有界 $X$ 与 $B_m^p$ 交换，则与每个 $q_L(B_m^p)$ 交换；对任意固定向量取强极限得 $XB_m=B_mX$。反向也立即成立。强闭代数结论由相同的逼近和 $B_m^p$ 本来就是 $B_m$ 的多项式得到。证毕。

这是一条保持原实际未知不变空间的正向恢复，而非对一般算子默认“奇幂不增加不变空间”。

## 5. 全部整数幂的准确尾重数

令
$$
p=2^v s,\qquad s\text{ 为正奇数},\qquad d=2^v,
\qquad c=\beta^{(m)}_{d-1}>0.
$$
原整头身份给
$$
B_m^d=c\,I_d\otimes B_{m+v},\qquad
B_m^p=c^s I_d\otimes B_{m+v}^{\,s}.
\tag{5.1}
$$
将第 4 节对 $B_{m+v}^{\,s}$ 的有界强多项式恢复放大 $d$ 次，并合法吸收非零标量 $c^s$，得到 $B_m^d$ 是 $B_m^p$ 的一致有界多项式强极限。因此
$$
\boxed{
\operatorname{Lat}(B_m^p)=\operatorname{Lat}(B_m^{2^{v_2(p)}}),
\qquad
\{B_m^p\}'=\{B_m^{2^{v_2(p)}}\}'.
}
\tag{5.2}
$$
强闭多项式代数也相同。

把任意有界算子写成 $d\times d$ 尾块，(5.1) 表明每块都须与 $B_{m+v}^{\,s}$ 交换。定理 4.1 逐块适用，所以准确有
$$
\boxed{
\{B_m^p\}'=M_{2^{v_2(p)}}(\mathscr C_{m+v_2(p)}),
\qquad \mathscr C_t=\{B_t\}'.
}
\tag{5.3}
$$
该身份是原酉头尾坐标下的具体算子代数身份。它不声称 $M_d(\mathscr C_t)$ 在 $d>1$ 时交换。

特别，完整交换子只在 $p$ 为奇数时仍为交换代数；$p$ 为偶数时，其全部有限头矩阵部分已经给出非交换性。

## 6. 同一恢复下降到每个实际闭不变子商

设 $N\subseteq M\subseteq K$ 是任意闭 $B_m$-不变旗，令
$$
T=(B_m)_{M/N}
$$
为原 Hilbert 商上的诱导算子。它可以是未知空间上的限制或商；本节不改变其底空间。

若原有界多项式序列 $q_L(B_m^p)\to B_m^d$ 强，且范数一致有界，则其在 $M/N$ 上的诱导序列满足
$$
q_L(T^p)\longrightarrow T^d\quad\text{强},
\qquad
\|q_L(T^p)\|\le\|q_L(B_m^p)\|.
\tag{6.1}
$$
确切地，对每个商向量选代表 $x\in M$，其误差的商范数至多为原空间中
$\|(q_L(B_m^p)-B_m^d)x\|$，故趋零。

于是对每个正整数 $p$，
$$
\boxed{
\operatorname{Lat}(T^p)=\operatorname{Lat}(T^{2^{v_2(p)}}),
\qquad
\{T^p\}'=\{T^{2^{v_2(p)}}\}'.
}
\tag{6.2}
$$
特别，$p$ 为奇数时，$T$ 与 $T^p$ 在这个**同一实际未知子商**上有相同的普通不变空间及完整交换子。

这里没有将 $T$ 的幂强行写成一个完整 $I_k\otimes B_r$。因此 (6.2) 本身不允许把全空间根重数结论直接用于 $T$ 的根，更不允许把该子商自动补为原尾的有界模直和。

## 7. 与根及平坦来源的关系

恢复 (5.3) 允许将任何满足
$X^q=\lambda(I_k\otimes B_m^p)$ 的有界 $X$ 放入准确的有限放大尾交换子，即使事先仅知它与 $B_m^p$ 交换。下一条根重数推论可据此在深有限头的字符像中计算。

对于闭域根或平坦共同倍数，本稿没有付出其全域正则化；其可用之处是：(6.1) 的同源、统一有界强逼近确实保持每个已经存在的原不变空间及对相应原算子不变的闭图。不能从“所有幂的共同倍数”直接推出一个闭根的域包含。
