# R271 附录：完整两远孔核的 Stieltjes Schur 与真实跨旗来源

日期：2026-11-16（UTC）。

作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：已证明。** 对原连续远尾，本文完整消去远一孔与二孔的所有 primitive 来源。给定零远孔头列 $a$ 后的真最小核能量是一个有限头矩阵 $H_2$；其系数为原无限一孔矩阵的 Stieltjes 型函数 $r(T)$。完整 Gram 与截二 boson Gram 的比较不含头条件数。最后把原首头的两孔核增益写成真实第三旗 Schur，明确它只看到核外返回源的一部分，未付全 $q_{\flat}$ 费用。

内积对第一变量线性。所有压缩、伴随和 MP 均使用原物理度量。

依据：

- [真一孔核与两孔正来源](R271-appendix-first-head-true-one-hole-kernel-elimination-and-two-hole-positive-schur.md)；
- [全低链两孔范围与无罚返回源](R271-appendix-true-low-chain-two-hole-range-and-unpenalized-return-source.md)；
- 原远尾 $D=\sum_{i\ge x}(i+1)^{-2}E_i$ 的真实硬核 incidence 行；其所需两层式在下文直接证明。

## 1. 原无限一孔矩阵与完整 MP

取整数 $x\ge6$，
$$
b_i=(i+1)^{-2},\quad z_i=b_i^2,\quad
S=\sum_{i\ge x}z_i,\quad z_{\max}=(x+1)^{-4}.
$$
远孔空间记为 $\mathcal H_j$；$D_j:\mathcal H_j\to\mathcal H_{j-1}$ 是原删除行。
在 $\mathcal H_1=\ell^2(\{i\ge x\})$ 上，$b=(b_i)$，$D_1=b^*$，
$$
D_2^*e_i=\sum_{j\ne i}b_j e_{\{i,j\}}.
$$
因而对有限支撑先逐坐标计算，随后按有界性延拓：
$$
\boxed{
F:=D_2D_2^*=S I-2Z+bb^*,\qquad
Z=\operatorname{diag}(z_i).
}
\tag{1.1}
$$
对角元为 $S-z_i$，非对角元为 $b_i b_j$。
尾积分给 $S\ge[3(x+1)^3]^{-1}$，故
$$
\epsilon:=\frac{2z_{\max}}S\le\frac6{x+1}<1,\qquad
F\ge(S-2z_{\max})I>0.
\tag{1.2}
$$
因此原无限行 $D_2$ 满射且闭值域，
$$
\boxed{D_2^\dagger=D_2^*F^{-1}}
\tag{1.3}
$$
是在整个 $\mathcal H_1$ 上有界的真实最小右逆。
这里没有把 primitive 压缩逆当作整层逆。
此外 $D$ 在全物理空间有界，因为 $\sum b_i<\infty$。

## 2. 两孔核全部列及零源

令 $C$ 为本题原有限强头 $A_m+D_{[m,x)}$，或任意有限维 nilpotent 头。
记
$$
F_j^C=\ker C^j,\qquad F_1^C=K.
$$
为避免与 (1.1) 混淆，下文的上标 $C$ 始终保留。
完整两远孔核是
$$
\mathscr K_2^C
=\ker(C+D)\cap
\big(\mathfrak h\otimes(\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2)\big).
$$
写其列为 $(a,v_1,v_2)$。原三个方程恰为
$$
Ca+D_1v_1=0,\qquad
Cv_1+D_2v_2=0,\qquad
Cv_2=0.
\tag{2.1}
$$
从最后两行得 $v_2\in K\otimes\mathcal H_2$、$v_1\in F_2^C\otimes\mathcal H_1$；
再由第一行得 $a\in F_3^C$。

反之，对任意 $a\in F_3^C$，
可先取 $v_1=-Ca\otimes b/S$，
再取 $v_2=-D_2^\dagger Cv_1$。
由于 $C$ 与尾行及 (1.3) 作用不同因子，
$v_2$ 的头值在 $K$，所以三行均严格成立。
因此全部可达零远孔头列正好是 $F_3^C$。

对给定 $v_1\in F_2^C\otimes\mathcal H_1$，
所有第二行、顶行的解为
$$
v_2=-D_2^\dagger Cv_1+\zeta,\qquad
\zeta\in K\otimes\ker D_2.
\tag{2.2}
$$
(1.3) 的最小值域与 $\ker D_2$ 正交，
故最小者是 $\zeta=0$，准确费用为
$$
\|v_2\|^2=\langle Cv_1,(I_K\otimes F^{-1})Cv_1\rangle .
$$
所有二孔 primitive 零源仍在 (2.2)；只是在这个真最小化中正交消去。

令
$$
C_2=C|_{F_2^C}:F_2^C\to K,\qquad T=C_2^*C_2\ge0,
$$
其中 $C_2^*$ 是这个受限算子的原物理伴随，不等于任意未压缩的 $C^*$。
给定 $a$ 后，剩余完整最小问题为
$$
\min_{\mathcal B v_1=-Ca}\langle Mv_1,v_1\rangle,\qquad
M=I+T\otimes F^{-1},\qquad
\mathcal B=I_{F_2^C}\otimes D_1.
\tag{2.3}
$$
$M$ 有界且 $M\ge I$；$\mathcal B$ 在全部 $F_2^C$ 上满射。
这一步保留了所有远一孔 primitive 方向。

## 3. 完整 Schur 的准确标量函数

对 $t\ge0$ 定义
$$
\chi(t)=\langle b,F(F+tI)^{-1}b\rangle,\qquad
r(t)=\chi(t)^{-1}.
\tag{3.1}
$$
$F>0$ 给 $\chi(t)>0$，尤其
$$
\chi(0)=S,\qquad r(0)=1/S.
\tag{3.2}
$$
有限头 $T$ 的谱有限且非负，故 $r(T)$ 是有界严格正矩阵。
按 $T$ 的正交谱分解，(2.3) 直接得到
$$
\boxed{\mathcal B M^{-1}\mathcal B^*=\chi(T).}
\tag{3.3}
$$
这是整层 $F^{-1}$ 的计算，并非先取 coherent 一维压缩后再逆。

因此唯一最小列为
$$
v_1(a)=-M^{-1}\mathcal B^*r(T)Ca,\qquad
v_2(a)=-D_2^\dagger Cv_1(a).
\tag{3.4}
$$
其总能量为
$$
\boxed{
H_2=I_{F_3^C}+C_3^*r(T)C_3,\qquad
\|(a,v_1(a),v_2(a))\|^2=\langle H_2a,a\rangle,
}
\tag{3.5}
$$
其中 $C_3=C|_{F_3^C}:F_3^C\to F_2^C$，
$C_3^*$ 同样是准确的源、目标间伴随。

设 $\mathcal J_2 a=(a,v_1(a),v_2(a))$。
所有 $a=0$ 的核列构成完整零源 $\mathcal Z_2$；
最小性给
$$
\mathscr K_2^C=\mathcal Z_2\oplus^\perp\operatorname{Ran}\mathcal J_2,
\qquad \mathcal J_2^*\mathcal J_2=H_2.
$$
$\operatorname{Ran}\mathcal J_2$ 因第零列恒等而闭。
对任意原头 forcing $g$，$i_0g=g\otimes\Omega$ 正交于 $\mathcal Z_2$，
所以
$$
\boxed{
P_{\mathscr K_2^C}i_0g
=\mathcal J_2H_2^{-1}P_{F_3^C}g,\qquad
\|P_{\mathscr K_2^C}i_0g\|^2
=\langle H_2^{-1}P_{F_3^C}g,P_{F_3^C}g\rangle .
}
\tag{3.6}
$$
这是真完整投影；没有删掉零源后改称一个较小 projection。

## 4. 不含头条件数的整个 Gram 比较

令 $F_0=S I+bb^*$。由 (1.2)，
$$
(1-\epsilon)F_0\preceq F\preceq F_0.
$$
对 $t\ge0$，正算子函数 $X\mapsto X(X+tI)^{-1}$
由逆的次序直接保持 Loewner 序；$t=0$ 时就是恒等。
又 $F_0b=2Sb$，故
$$
\frac{2(1-\epsilon)S^2}{2(1-\epsilon)S+t}
\le\chi(t)\le
\frac{2S^2}{2S+t}.
$$
取正标量倒数得到
$$
\boxed{
\frac1S+\frac{t}{2S^2}
\le r(t)\le
\frac1S+\frac{t}{2(1-\epsilon)S^2}.
}
\tag{4.1}
$$
在 $t=0$ 两端严格取等，均为 $1/S$。

定义同一真实头旗上的截二 boson Gram
$$
H_{\rm b}
=I_{F_3^C}+\frac{C_3^*C_3}{S}
+\frac{(C^2|_{F_3^C})^*(C^2|_{F_3^C})}{2S^2}.
$$
因 $C_2C_3=C^2|_{F_3^C}$，(4.1) 通过同一 $T$ 的谱演算给
$$
\boxed{
H_{\rm b}\preceq H_2
\preceq H_{\rm b}
+\frac{\epsilon}{1-\epsilon}
 \frac{(C^2|_{F_3^C})^*(C^2|_{F_3^C})}{2S^2}
\preceq\frac1{1-\epsilon}H_{\rm b}.
}
\tag{4.2}
$$
因此
$$
(1-\epsilon)H_{\rm b}^{-1}\preceq H_2^{-1}\preceq H_{\rm b}^{-1}.
\tag{4.3}
$$
它们始终是 $F_3^C$ 上的完整同源逆；
不从 (4.3) 推导完整头空间上的逆，也不要求 $H_2$ 保持 forcing 的更低旗。
常数 $\epsilon\le6/(x+1)$ 与头维数、头奇异值无关。

## 5. 原首头两孔增益究竟读哪一块

回到偶 $R$ 的原 $C$，沿无罚来源稿保同一个
$$
v=(I+S\Gamma)^{-1}e_0,\quad
r=(I-P_K)(CC^*)^\dagger v,\quad
q_{\flat}=P_{\operatorname{Ran}C^2}(C^*)^\dagger r.
$$
原 $e_1\in F_2^C$，且 $C^2e_1=0$。

将 $F_3^C$ 按原物理正交分解
$$
F_3^C=F_2^C\oplus^\perp U_3,\qquad
U_3=F_3^C\ominus F_2^C.
$$
$C(F_2^C)\subset K=\ker T$，所以由 $r(0)=1/S$，
$H_2$ 的这个完整块矩阵是
$$
H_2=
\begin{pmatrix}
H_1&B^*\\B&H_{22}
\end{pmatrix},\qquad
H_1=I_{F_2^C}+\frac{C_2^*C_2}{S},
\qquad
B=\frac1S P_{U_3}C^*C|_{F_2^C}.
\tag{5.1}
$$
特别高阶项不产生这个跨块，不能将其单独按环境范数放大。

令 $a_1=H_1^{-1}e_1$。原完整一孔核公式给
$$
a_1=e_1-C^\dagger v,\qquad Ca_1=S\Gamma v.
$$
因此
$$
Ba_1=P_{U_3}C^*\Gamma v
=-P_{U_3}C^*r,
\tag{5.2}
$$
最后使用 $C^*r=C^\dagger v-C^*\Gamma v$、
$C^\dagger v\in F_2^C$。
完整正 Schur
$$
\mathcal S_3=H_{22}-BH_1^{-1}B^*>0
$$
遂给真实投影增益
$$
\boxed{
\|P_{\mathscr K_2^C}f_1\|^2-\|P_{\mathscr K_1^C}f_1\|^2
=\langle P_{U_3}C^*r,\mathcal S_3^{-1}P_{U_3}C^*r\rangle .
}
\tag{5.3}
$$
若 $U_3=0$，按零二次型理解。

这准确说明它与完整无罚费用的区别。
后者使用 $C^{*2}q_{\flat}=C^*r$ 的整个来源，
而 (5.3) 只使用 $P_{U_3}C^*r$。
更具体地，
$$
P_{U_3}C^*r=(C^2|_{U_3})^*q_{\flat},\qquad
\operatorname{Ran}(C^2|_{U_3})=K\cap\operatorname{Ran}C^2.
\tag{5.4}
$$
第二式中，若 $z=C^2a\in K$，则 $a\in F_3^C$；
减掉 $P_{F_2^C}a$ 不改变 $C^2a$，故可从 $U_3$ 达到它。
所以原两孔核增益只看到 $q_{\flat}$ 在这个可达 primitive 头块上的分量。

本文给出完整 K2 的真最小 Gram、无头条件数比较及准确增益来源。
它没有把 (5.3) 的增益或任何跨 $m$ 增益可和性
替换成 $q_{\flat}$ 全部受限 Schur 的费用；
真实高旗反馈与普通封口继续保留。
