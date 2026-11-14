# 固定辅助域 −15 的实际类群和与跨素数不可除性

日期：2026-11-12。状态：以下理想、固定模曲线映射、高度和不可除性
均已证明。本篇把 R102 的原点不可除性推进到已经作完类群求和的点；
尚未证明 Kolyvagin 导数不可除，也未完成原 E17 的无穷素数目标。

固定 R103 的
$$
F=\mathbb Q(\sqrt{-15}),\quad h_F=2,\quad
E:y^2=x^3-17x,\quad N=9248.
$$
取一次有理模参数化 $\pi:X_0(N)\to E$，规范为 $\pi(\infty)=O$。
以后不改变 $F$ 或 $\pi$。对在 $F$ 中惰性且 $\ell\nmid 3N\cdot15$
的素数，记
$$
\mathcal O_\ell=\mathbb Z+\ell\mathcal O_F,\quad
H_\ell=F[\ell],\quad H_1=F[1],\quad
G_\ell=\operatorname{Gal}(H_\ell/H_1),\quad q=\ell+1.
$$
沿用 R100 的相容 Heegner 点 $x_\ell\in X_0(N)(H_\ell)$ 和
$P[\ell]=\pi(x_\ell)$。$G_\ell$ 是阶 $q$ 的循环群。

## 1. 类群代表可用同一个分歧理想选定

置
$$
\alpha_\ell=\frac{3+\ell\sqrt{-15}}2,\qquad
h_\ell=\frac{3+5\ell^2}{4},\qquad
\mathfrak r_\ell=(3,\alpha_\ell)\subset\mathcal O_\ell.
\tag{1}
$$
由于 $\ell$ 为奇数，
$\mathcal O_\ell=\mathbb Z[\alpha_\ell]$，而
$$
\alpha_\ell^2=3\alpha_\ell-3h_\ell,\qquad
h_\ell\in\mathbb Z,\qquad 3\nmid h_\ell.
\tag{2}
$$
因此 $\mathcal O_\ell/\mathfrak r_\ell\simeq\mathbb F_3$，
且
$$
\mathfrak r_\ell^2
=(9,3\alpha_\ell,\alpha_\ell^2)
=(9,3\alpha_\ell,3h_\ell)
=(3).
\tag{3}
$$
最后一步使用 $\gcd(3,h_\ell)=1$。特别地，$\mathfrak r_\ell$
是可逆 proper 理想，逆为 $\mathfrak r_\ell/3$；不需要将
非最大阶的分歧理想先验当成可逆理想。

其延拓到 $\mathcal O_F$ 是
$$
\mathfrak r=(3,\sqrt{-15}),
$$
即 $3$ 上的分歧素理想。它不主：写
$\mathcal O_F=\mathbb Z[\omega]$、$\omega=(1+\sqrt{-15})/2$，
范数为
$$
N(a+b\omega)=a^2+ab+4b^2.
$$
$b=0$ 时这个数不等于 $3$；$b\ne0$ 时它至少为
$15b^2/4$，故作为整数至少为 $4$。于是不存在范数为 $3$
的元素。

所以 $[\mathfrak r_\ell]$ 在 $\operatorname{Pic}(\mathcal O_\ell)$
中恰有阶 $2$，且在延拓映射到 $\operatorname{Pic}(\mathcal O_F)$
后仍非平凡。令 $\tau_\ell$ 为它的 Artin 元，则
$$
\tau_\ell^2=1,\qquad
\operatorname{Gal}(H_\ell/F)
   =G_\ell\times\langle\tau_\ell\rangle.
\tag{4}
$$
确实，右侧两个子群相交平凡，后一因子满射到
$\operatorname{Gal}(H_1/F)$，其阶为 $2$。
故 R100 中的类群代表可以对所有 $\ell$ 统一选为
$$
\mathcal C_\ell=\{1,\tau_\ell\}.
\tag{5}
$$
这里“统一”指同一个理想 $3$ 的构造，并非把不同环类域的
Galois 元误认为同一个群中的元素。

定义实际点
$$
X_\ell=(1+\tau_\ell)P[\ell]\in E(H_\ell).
\tag{6}
$$
它甚至在 $H_\ell^{\langle\tau_\ell\rangle}$ 中有定义；
该域仍是 $F$ 的阿贝尔扩张。

## 2. 类群和来自一个固定的非恒定有限映射

考虑两条退化映射
$$
d_1,d_2:X_0(3N)\longrightarrow X_0(N).
$$
若源点为 $(A,C_{3N})$，记 $C_3,C_N$ 为其中相应阶数的唯一子群，
则
$$
d_1(A,C_{3N})=(A,C_N),\qquad
d_2(A,C_{3N})=(A/C_3,\operatorname{im}C_N).
\tag{7}
$$
它们均在 $\mathbb Q$ 上定义，因 $\gcd(3,N)=1$，这些层结构
确实都是循环子群。

对 $x_\ell=(A_\ell,C_N)$，取 $\mathfrak r_\ell$ 决定的
次数 $3$ CM 同源，其核为 $C_3=A_\ell[\mathfrak r_\ell]$。
这个核与 $C_N$ 互素，故 $C_3+C_N$ 是阶 $3N$ 的循环子群，
给出一点
$$
z_\ell\in X_0(3N)(H_\ell).
$$
CM 互反律准确给
$$
d_1(z_\ell)=x_\ell,\qquad
d_2(z_\ell)=\tau_\ell x_\ell.
\tag{8}
$$
在格模型中，$A_\ell=\mathbb C/\mathfrak a$，取商后格为
$\mathfrak r_\ell^{-1}\mathfrak a$；$N$ 层结构一同运输。
采用相反的 Artin 规范会将 $\tau_\ell$ 换成其逆，而
$\tau_\ell^{-1}=\tau_\ell$，所以 (8) 不含方向歧义。
主理想 $(3)$ 的同一化是格的整体缩放，保持 $X_0(N)$ 的循环
层结构；这里没有要求它保持一个额外指定的全层基。

固定映射
$$
\Phi=\pi\circ d_1+\pi\circ d_2:X_0(3N)\longrightarrow E
\tag{9}
$$
遂满足 $\Phi(z_\ell)=X_\ell$，是精确等式而非模挠点等式。
两退化映射都把 $\infty$ 送到 $\infty$，因此 $\Phi(\infty)=O$。

设 $f(q)=q+\cdots$ 是 $E$ 的归一新形式，$\omega_E$ 为不变微分。
存在固定 $c\in\mathbb Q^\times$ 使
$\pi^*\omega_E=c f(q)\,dq/q$。在无穷尖点，两条退化映射分别为
$\tau\mapsto\tau$ 和 $\tau\mapsto3\tau$，所以
$$
\Phi^*\omega_E
=c\bigl(f(q)+3f(q^3)\bigr)\frac{dq}{q}\ne0.
\tag{10}
$$
括号的 $q$ 系数为 $1$。这证明 $\Phi$ 非恒定，因而是光滑射影
曲线间的有限态射。这只是两条确定的退化映射之和，不是把完整
$T_3$ 对应中的全部分支相加；后者的特征值不影响 (10)。

## 3. 完成类群求和后仍有双向对数高度界

存在只依赖于固定 $E,F,\pi$ 的正常数 $c_1,c_2,C$，使上述
充分大的 $\ell$ 满足
$$
c_1\log\ell-C
\le \widehat h(X_\ell)
\le c_2\log\ell+C.
\tag{11}
$$
证明沿用 R102 §1 的高度引理，但把固定参数曲线和映射换成
$X_0(3N)$、$\Phi$。
源点 $z_\ell$ 的 $j$ 值仍有判别式 $-15\ell^2$，因此该处
CM 阶高度公式与 $j$ 的高度比较给
$h(j(z_\ell))\asymp\log\ell$。

这里 $j:X_0(3N)\to\mathbb P^1$ 和 (9) 都是固定非恒定有限映射。
它们拉回的正次数除子均 ample；比较这些固定 ample 高度，
再用 Weil 高度与典范高度的有界差，即得 (11)。
这个论证证明了实际和 $X_\ell$ 的下界，不能用
$\widehat h(P[\ell])$ 的下界和三角不等式替代。
特别地，$X_\ell$ 对所有充分大的这些 $\ell$ 均非挠。

## 4. 每个充分大的输入 p 都可使类群和不可 p 除

令 $\mathcal P_F$ 为 R103 的输入素数集合。对每个充分大的
$p\in\mathcal P_F$，可选一个素数 $\ell$，同时满足
$$
\ell\equiv7\pmod{1020},\qquad
\ell\equiv p-1\pmod{p^2},
\tag{12}
$$
以及
$$
X_\ell\notin pE(H_\ell).
\tag{13}
$$

先核 (12) 是合法的 Kolyvagin 辅助选择。
因 $p\nmid1020$，CRT 给模 $1020p^2$ 的一个互素剩余类。
$\ell\equiv7\pmod{60}$ 使它在 $F$ 和 $\mathbb Q(i)$ 中均惰性，
而 $\ell\equiv7\pmod{17}$ 排除坏素数 $17$。
在本 CM 曲线上 $a_\ell(E)=0$，并且
$$
v_p(\ell+1)=1,\qquad
M_\ell=\min\{v_p(\ell+1),v_p(a_\ell(E))\}=1.
\tag{14}
$$
也有 $4p\mid\ell+1$，故 $\ell\ge4p-1$。

Linnik 定理给这样的一个素数
$\ell\le C_0(1020p^2)^L$，其中常数不随 $p$ 改变。
由 (11)，对于这个选择，
$$
0<\widehat h(X_\ell)\le C_1\log p+C_2.
\tag{15}
$$
固定 CM 曲线在 $F^{\rm ab}$ 中非挠点的典范高度有统一正常数
下界 $c_{E,F}$，这是 R102 §2 已核的 Baker 定理。
若 $X_\ell=pR$，$R\in E(H_\ell)$，则 $R$ 非挠且
$$
\widehat h(X_\ell)=p^2\widehat h(R)\ge p^2c_{E,F},
$$
与充分大 $p$ 时的 (15) 矛盾。故 (13) 成立。

所得不可除性是在实际 $E(H_\ell)$ 中，不是只在张量
$E(H_\ell)\otimes\mathbb Q$ 中；也没有因取
$H_\ell^{\langle\tau_\ell\rangle}$ 而缩小可除点所在的域。

## 5. 尚未消去的步骤准确只剩增广导数

用 (5) 的代表，R100 的点现在准确为
$$
Y_\ell=(1+\tau_\ell)D_\ell P[\ell]
       =D_\ell X_\ell.
\tag{16}
$$
环类群阿贝尔，所以两个算子交换。由于 $a_\ell(E)=0$，
原 Heegner 范数关系还给 $N_{G_\ell}X_\ell=0$。

本篇已对每个充分大的输入 $p$ 构造合法的 $M_\ell=1$、
范数为零而不可 $p$ 除的实际 $X_\ell$。要应用 R100 的单支撑判据，
仍须证明 $D_\ell X_\ell\notin pE(H_\ell)$。
R102 §5 的循环格模型说明，$X_\ell\notin pE(H_\ell)$ 与范数零
本身没有这一推论：在 $\mathbb Z_p[\zeta_p]$ 上，
$u=\zeta_p-1$ 非 $p$ 倍，而 $D u=p$。

因此这里消去的是类群和可能把原点消掉的额外不确定性。
没有把实际的增广最底层原始性，或原 E17 的有限 Sha，列作已证。

## 使用的已核输入

- [R103 的固定辅助域及全部局部条件](2026-11-12-explicit-minus15-heegner-field.md)。
- [R100 的标准 Heegner 点、Artin 作用和导出点规范](2026-11-12-one-prime-heegner-class-and-explicit-points.md)，
  及该文所列 Howard（2004）、BCGS（2026）的原始来源。
- [R102 的 CM 高度比较、Baker 下界和 Linnik 输入](2026-11-12-heegner-height-and-augmentation-primitivity.md)。
  本篇另以 (1)–(10) 完整证明了固定类群代表和新映射；
  未把一般类群迹的非恒定性当作黑箱。
