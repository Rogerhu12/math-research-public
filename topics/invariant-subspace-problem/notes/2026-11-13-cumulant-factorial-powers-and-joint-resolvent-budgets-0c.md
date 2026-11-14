# 实际 Bell 累积量的分阶阶乘幂界与联合预解预算

日期：2026-11-13（UTC）。作者：Astra-ISP-0c017065；AI-assisted，GPT-6 Astra Pro。
状态：已证明。固定原实际 Haar 模型，保留全部 carry；本稿只给有界累积量及联合函数演算的增长预算。混合重根的排核还需要另稿中的实际 Boolean 主项、Bézout 逆和完整自然域。

## 1. 结论、记号与真正的正锥

原算子为 $Af(y)=w(y)f(y-1)$，其中 $w\ge0$，
$\|A\|=\alpha_0=e^{-20}<1$。因此 $A$ 及
$N_j=A^{2^j}/d_j$ 保持函数的逐点非负锥。
这里的“正”始终指这个 Banach 格正锥，**不是 Hilbert 自伴正性**。

实际等式及界为
$$
N_j^2=\eta_jN_{j+1},\qquad
\|N_j\|=1,\qquad 0<\eta_j\le e^{-770\,16^j},
$$
$$
d_j=e^{-\Lambda_j},\qquad
\Lambda_j=100\,16^j-105\,8^j+(150j+25)2^j.
\tag{1.1}
$$
使用 [R109](../results/R109-invariant-restriction-exact-quartic-type.md) 的全幂界
$$
\|A^k\|\le \exp\!\left(-\frac{100}{15}k^4+105k^3\right).
\tag{1.2}
$$
下面只需要其推论：存在固定 $K_A,c_A>0$，
$\|A^k\|\le K_Ae^{-c_Ak^4}$ 对所有整数 $k\ge0$ 成立。
有限个小 $k$ 吸入 $K_A$；这一步没有把真实二进位范数换成错误的精确平滑式。

固定规范系数 $a_j=(-1)^j/(j+1)$、任意复 $b\in\ell^2$，
$t_j=e^{-2b_j}$，并置
$$
R_j=\frac{I-t_jN_j}{I+t_jN_j},\qquad
L_n(v)=\left.\frac{d^n}{ds^n}
\log(\cosh s+v\sinh s)\right|_{s=0},
$$
$$
G_n=\sum_{j\ge0}a_j^nL_n(R_j),\qquad n\ge2.
\tag{1.3}
$$
每个 $L_n$ 是次数不超过 $n$ 的标量多项式，$L_n(1)=0$。
这些是 R176/R236 的真实有界倾斜累积量。

**定理。** 对每个固定 $n\ge2$，存在只依赖 $n,b$ 和原模型的
$K_n\ge1,D_n>0$，使
$$
\boxed{\|G_n^k\|\le
K_n\frac{D_n^k}{(k!)^{n-1}}\quad(k\ge0).}
\tag{1.4}
$$
因此对所有 $z\ne0$，
$$
\boxed{
\|(z-G_n)^{-1}\|
\le\frac{K_n}{|z|}
\exp\!\left((n-1)(D_n/|z|)^{1/(n-1)}\right).
}
\tag{1.5}
$$

固定 $p\ge2$、$\varepsilon>0$。对 $0<s\le1$，
令 $\rho_n=\varepsilon s^n$（$2\le n\le p$）。
若 $F$ 在闭多圆盘的某个邻域全纯，且在其边界多圆周上
$|F|\le M_F$，则
$$
\boxed{
\|F(G_2,\ldots,G_p)\|
\le K\,M_F\,e^{C_\varepsilon/s^2}.
}
\tag{1.6}
$$
$K,C_\varepsilon$ 与 $s,F$ 无关；允许 $F$ 随反射次数和 $s$ 改变，
只要逐次满足明确的全纯域与 $M_F$ 条件。

## 2. 一个包含全部复倾斜的正主控

令 $L=\max(1,\sup_j|t_j|)<\infty$。
写
$$
L_n(1+x)=\sum_{\ell=1}^n c_{n,\ell}x^\ell,
\qquad
W_n(z)=\sum_{\ell=1}^n|c_{n,\ell}|
\left(\frac{2Lz}{1-Lz}\right)^\ell.
\tag{2.1}
$$
$W_n$ 在零点附近解析、$W_n(0)=0$，全部 Taylor 系数非负，
并是分母为 $(1-Lz)^n$ 的有理函数。
$N_j$ 准幂零，所以 $W_n(N_j)$ 的 Taylor 级数在算子范数绝对收敛，
是保持函数非负锥的实际算子。

为支付统一界，取 $J$ 使 $L^2\eta_j\le1/2$ 对 $j\ge J$ 成立。
真实平方关系给
$$
(I-LN_j)^{-1}
=(I+LN_j)(I-L^2\eta_jN_{j+1})^{-1},
$$
故高位的逆范数不超过 $2(1+L)$。
有限个低位分别使用其真正的准幂零预解式，再取有限最大值。
所以
$$
\sup_j\|(I-LN_j)^{-1}\|<\infty.
\tag{2.2}
$$
同理，若
$$
W_n(z)=zW_{n,1}(z)=w_{n,1}z+z^2W_{n,2}(z),
$$
则两个 $W_{n,i}$ 仍是上述固定极点的有理函数，于是
$$
B_{n,1}:=\sup_j\|W_{n,1}(N_j)\|<\infty,\qquad
B_{n,2}:=\sup_j\|W_{n,2}(N_j)\|<\infty.
\tag{2.3}
$$
这里没有把 $N_j$ 范数为1直接代入一个半径可能小于1的标量 Taylor 界；
低位逆和高位真实平方关系都已使用。

原 $L^2$ 函数模满足 $|N_jx|\le N_j|x|$。
由
$$
R_j-I=-2t_jN_j(I+t_jN_j)^{-1}
$$
的实际绝对范数收敛级数，逐项三角不等式给
$$
|L_n(R_j)x|\le W_n(N_j)|x|.
\tag{2.4}
$$
令
$$
M_n=\sum_{j\ge0}(j+1)^{-n}W_n(N_j).
\tag{2.5}
$$
(2.2)--(2.3) 使该和按算子范数绝对收敛；
$M_n$ 保持函数非负锥且属于 $\mathcal A$。
由 $|a_j|^n=(j+1)^{-n}$，
$$
|G_nx|\le M_n|x|,\qquad
|G_n^kx|\le M_n^k|x|.
\tag{2.6}
$$
第二式逐次使用第一式和正锥保持性。
因此 $\|G_n^k\|\le\|M_n^k\|$。

## 3. 每个实际局部指数的完整 carry 界

由偶、奇幂分开及 $N_j^2=\eta_jN_{j+1}$，对任意 $\zeta\in\mathbb C$，
$$
\begin{aligned}
\|e^{\zeta N_j}\|
&\le \cosh(|\zeta|\sqrt{\eta_j})
+|\zeta|\frac{\sinh(|\zeta|\sqrt{\eta_j})}
{|\zeta|\sqrt{\eta_j}}\\
&\le(1+|\zeta|)e^{|\zeta|\sqrt{\eta_j}}.
\end{aligned}
\tag{3.1}
$$
零参数时按连续值解释。
这是真正的算子指数，偶次部分和奇次部分都已包含全部高位进位。

由 (2.3)，
$$
W_n(N_j)=w_{n,1}N_j+E_{n,j},\qquad
\|E_{n,j}\|\le B_{n,2}\eta_j.
\tag{3.2}
$$
两个加数都是 $N_j$ 的函数而交换。
因此对 $v\ge0$、$z\in\mathbb C$、$t=|z|$，
$$
\boxed{
\|e^{zvW_n(N_j)}\|
\le (1+w_{n,1}tv)\,
\exp(C_n^{(0)}tv\sqrt{\eta_j}).
}
\tag{3.3}
$$
可取 $C_n^{(0)}=w_{n,1}+B_{n,2}$，因为 $\eta_j\le\sqrt{\eta_j}$。

## 4. 随参数选择有限头，但不删任何进位

给定 $t\ge0$，取最小整数 $h\ge1$，使
$$
385\,16^h\ge2\log(2+t).
\tag{4.1}
$$
分解 $M_n=M_{n,<h}+M_{n,\ge h}$。
所有项属于同一个交换代数，所以两个部分交换。

对真实尾，先对有限乘积使用 (3.3)，再由指数的范数连续性取极限：
$$
\|e^{zM_{n,\ge h}}\|
\le
\prod_{j\ge h}\left(1+\frac{w_{n,1}t}{(j+1)^n}\right)
\exp\!\left(C_n^{(0)}t
\sum_{j\ge h}(j+1)^{-n}\sqrt{\eta_j}\right).
\tag{4.2}
$$
超快尾给
$$
\sum_{j\ge h}(j+1)^{-n}\sqrt{\eta_j}
\le 2e^{-385\,16^h}\le 2(2+t)^{-2}.
\tag{4.3}
$$
所以最后的指数因子一致有界，未把它当作零。

对任意 $A\ge0$，
$$
\sum_{j\ge1}\log(1+A/j^n)
\le A^{1/n} I_n,\qquad
I_n=\int_0^\infty\log(1+x^{-n})\,dx<\infty.
\tag{4.4}
$$
这是单调函数的积分比较；$n>1$ 保证无穷端可积，零点的对数也可积。
于是
$$
\|e^{zM_{n,\ge h}}\|
\le K_n^{(0)}e^{C_n^{(1)}t^{1/n}}.
\tag{4.5}
$$

有限头有明确而实际的 $A$ 因子：
$$
M_{n,<h}=A U_{n,h},\qquad
U_{n,h}=\sum_{j<h}
\frac{(j+1)^{-n}}{d_j}
A^{2^j-1}W_{n,1}(N_j)\in\mathcal A.
\tag{4.6}
$$
由 $(150j+25)/8^j\le25$，(1.1) 给 $\Lambda_j\le125\,16^j$。
又 $\|A^{2^j-1}\|\le1$，且 $\sum(j+1)^{-n}<2$，所以
$$
\|U_{n,h}\|\le2B_{n,1}e^{125\,16^{h-1}}.
\tag{4.7}
$$
最小性及 $h=1$ 的单独情形给
$$
16^{h-1}\le1+\frac2{385}\log(2+t).
\tag{4.8}
$$
因而 $\log(2+t\|U_{n,h}\|)\le C_n^{(2)}+2\log(2+t)$。
低头因子随 $t$ 的增长已明确支付，没有使用只对固定 $h$ 的无量化常数。

## 5. 原四次幂界吸收整个低头指数

$A$ 与 $U_{n,h}$ 交换。由 (1.2) 的 $K_A,c_A$ 推论，
$$
\|e^{zAU_{n,h}}\|
\le K_A\sum_{k\ge0}
e^{-c_Ak^4}\frac{(t\|U_{n,h}\|)^k}{k!}.
\tag{5.1}
$$
令 $\ell=\log(2+t\|U_{n,h}\|)$。
Young 优化给某个仅依赖 $c_A$ 的 $C_A$，
$$
-c_Ak^4+k\ell
\le-\frac{c_A}2k^4+C_A\ell^{4/3}.
$$
舍去 $1/k!\le1$ 并求收敛的四次级数，得到
$$
\|e^{zM_{n,<h}}\|
\le K_n^{(1)}
\exp\!\big(C_n^{(3)}(1+\log(2+t))^{4/3}\big).
\tag{5.2}
$$
对固定 $n$，$(1+\log(2+t))^{4/3}\le C_n^{(4)}(1+t^{1/n})$。
合并真实交换的头尾两部分，
$$
\boxed{
\|e^{zM_n}\|\le K_n e^{C_n|z|^{1/n}}
\qquad(z\in\mathbb C)
}
\tag{5.3}
$$
对某些固定 $K_n\ge1,C_n>0$ 成立。
原 carry 的低头与高尾分别由 (5.2)、(4.3) 支付，未使用纯模型替代。

## 6. Cauchy 系数界与全部实际预解式

对整算子函数 $e^{zM_n}$ 用 Cauchy 系数估计。
当整数 $k\ge1$ 时取圆半径 $R=(nk/C_n)^n$，得到
$$
\|M_n^k\|
\le K_n k!e^{nk}
\left(\frac{C_n}{nk}\right)^{nk}.
$$
由 $(k!)^n\le k^{nk}$，
$$
\|M_n^k\|
\le K_n
\frac{D_n^k}{(k!)^{n-1}},
\qquad
D_n=(eC_n/n)^n.
\tag{6.1}
$$
$k=0$ 由 $K_n\ge1$ 包含。再用 (2.6) 就得到 (1.4)。

对 $z\ne0$，实际 Neumann 级数
$\sum_{k\ge0}z^{-k-1}G_n^k$ 由 (1.4) 绝对收敛，
左右乘 $z-G_n$ 均望远镜为 $I$，所以它确是实际有界预解式。
对整数 $s=n-1\ge1$、$x\ge0$，
$$
\sum_{k\ge0}\frac{x^k}{(k!)^s}\le e^{s x^{1/s}}.
\tag{6.2}
$$
证明是把 $(e^{x^{1/s}})^s$ 的非负多重级数只保留所有指标相等的对角项。
(1.5) 立即成立；不只是在一个未核定的远离零点的区域成立。

## 7. 各坐标按 Bell 权缩小的共同多圆周

有限个 $G_n$ 全部在交换代数 $\mathcal A$ 中。
因此真实联合函数演算为
$$
F(G)=\frac1{(2\pi i)^{p-1}}
\int_{\prod_{n=2}^p\{|z_n|=\rho_n\}}
F(z)\prod_{n=2}^p(z_n-G_n)^{-1}\,dz_2\cdots dz_p.
\tag{7.1}
$$
每个坐标谱为零，上述任意正半径都合法。
由 (1.5)，圆周长度的 $\rho_n$ 正好消去预解式前面的 $\rho_n^{-1}$：
$$
\|F(G)\|\le
M_F\prod_{n=2}^pK_n
\exp\!\left(\sum_{n=2}^p(n-1)
(D_n/\rho_n)^{1/(n-1)}\right).
\tag{7.2}
$$
置 $\rho_n=\varepsilon s^n$，注意
$n/(n-1)\le2$ 且 $0<s\le1$，得到 (1.6)，可取
$$
K=\prod_{n=2}^pK_n,\qquad
C_\varepsilon=\sum_{n=2}^p(n-1)
(D_n/\varepsilon)^{1/(n-1)}.
\tag{7.3}
$$
常数与 $F,s$ 无关。有限个系数函数可逐个使用这一共同预算；
不能将它解释为对任意非全纯或有极点的函数仍有效。

## 8. 任意物理排列的弱 $\ell^1$ 系数上界

同一结论不要求系数在原物理位上的调和衰减。设 $a\in\ell^2(\mathbb C)$，
其幅度递减重排为 $\rho_k$（$k\ge1$），并假设
$$
B:=\sup_{k\ge1}k\rho_k<\infty.
\tag{8.1}
$$
零行的结论平凡；以下设 $B>0$。仍取任意复 $b\in\ell^2$，并按原物理位
定义 $R_j$ 与 $G_n=\sum_j a_j^nL_n(R_j)$。
则 (1.4)--(1.6) 全部成立，常数现在允许依赖 $a$（事实上相应预算只需 $B$）、
$b,n,p,\varepsilon$ 和原模型。

为证明它，只需把 (2.5) 改成实际正主控
$$
M_n=\sum_{j\ge0}|a_j|^nW_n(N_j).
\tag{8.2}
$$
由
$$
\sup_j|a_j|\le B,\qquad
\sum_j|a_j|^n=\sum_{k\ge1}\rho_k^n
\le B^n\zeta(n)<\infty
\tag{8.3}
$$
及 (2.2)--(2.4)，该和按范数收敛且仍有
$|G_n^kx|\le M_n^k|x|$。复相位已由这个真实函数正锥主控支付，
不需要对模型作坐标置换。

仍按 (4.1) 取**物理头** $j<h(t)$。对尾指数使用 (3.3) 后，只在下列
标量乘积中作数列重排：
$$
\begin{aligned}
\sum_{j\ge h}\log(1+w_{n,1}t|a_j|^n)
&\le\sum_{k\ge1}\log(1+w_{n,1}t\rho_k^n)\\
&\le I_n(w_{n,1}B^nt)^{1/n}.
\end{aligned}
\tag{8.4}
$$
原物理尾的进位项则直接满足
$$
\sum_{j\ge h}|a_j|^n\sqrt{\eta_j}
\le 2B^ne^{-385\,16^h}\le 2B^n(2+t)^{-2}.
\tag{8.5}
$$
故真实尾指数仍有 $K_ne^{C_nt^{1/n}}$ 界。
这里没有把排序后的第 $k$ 项误认为原物理第 $k$ 位。

有限物理头仍具有真实因子
$$
M_{n,<h}=A U_{n,h},\qquad
U_{n,h}=\sum_{j<h}|a_j|^n d_j^{-1}
A^{2^j-1}W_{n,1}(N_j).
\tag{8.6}
$$
由 (8.3)，
$$
\|U_{n,h}\|\le
B_{n,1}B^n\zeta(n)e^{125\,16^{h-1}}.
\tag{8.7}
$$
结合完全相同的 (4.8)，仍有
$\log(2+t\|U_{n,h}\|)\le C+2\log(2+t)$。
第5节的原四次幂界遂逐字给出
$\|e^{zM_n}\|\le K_ne^{C_n|z|^{1/n}}$。
第6节的 Cauchy 系数优化及第7节的联合多圆周积分不再使用系数的位置，
故 (1.4)--(1.6) 对 (8.1) 的所有物理排列成立。

本节只需要弱 $\ell^1$ **上界**；没有使用
$\limsup k\rho_k>0$。任何后续选位或反射平均若需要后一个下界，
须在其自己的证明中另付，不能从本节的预解预算推出。

## 9. 范围与所需的下一接口

本稿覆盖规范系数及第8节的全部弱 $\ell^1$ 上界系数行、任意固定复 $\ell^2$ first 指数权，以及每个固定有限最高阶 $p$。
给出的分阶指数 $1/(n-1)$ 是后续按 Bell 权选圆周的关键；
若只用所有坐标相同的 $e^{C/|z|}$ 粗界，较高坐标的半径 $s^n$ 会造成错误的 $e^{C/s^p}$ 成本。

本稿没有构造 Bézout 逆，没有证明完整 Bell 多项式核为零，
也没有从无重根结果取极限。
若后续逆系数在上述多圆盘全纯且具有已证边界界 $M_F$，
本稿允许一次联合求值，只支付 $e^{C/s^2}$，而不是对每个位的逆分别重复支付该预解成本。
普通 ISP、一般正常湮灭者与边界 $N=M$ 均仍开放。
