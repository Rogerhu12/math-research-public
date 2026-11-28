# R1165 — 原椭圆系数的整留数收缩与 log-PD cone

日期：2026-11-28（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

**已证明，纸面。** 本篇把 R1163 的几何系数模型写成一个保整滤过的实际 Čech 收缩，并给出所对应的三项 log-PD complex。收缩直接读取同一 $\omega,x\omega$ 的系数，不用除 $p$ 的不定积分。它也说明把原 R1164 代表送入 coefficient cone 时，Frobenius homotopy 必须进入第二槽。

本篇没有计算原 $F_0$ 或宣称其中央槽为单位。一个 scalar symbol 所用的 embedding/refinement 与下文两开集模型之间的实际比较仍须随代表运输；不能以两者计算相同 cohomology 为由删去该比较的同伦。

## 1. 原短模型与两开集的 odd complex

设 $\mathcal O$ 为原未分歧 $p$-adic 底，$p>37$，同一 good elliptic curve 为
$$
\mathcal E:\ y^2=x^3+Ax+B,\qquad
t=-x/y,\qquad \omega=\frac{dx}{2y},\qquad \eta=x\omega .
\tag{1165.1}
$$
这里先固定曲线，随后改变的 $z$ 是原 torsion/source 参数，不是另一个椭圆模参数。若曲线自身随底变化，必须另保其 Gauss–Manin connection。

在 $O$ 处，
$$
\omega=(1+O(t^4))\,dt,\qquad
\eta=(t^{-2}+O(t^2))\,dt .
\tag{1165.2}
$$
这些展开整，且在 $[-1]$ 下 $t,\omega,\eta$ 均取负。

取 $U=\mathcal E\setminus O$，并取包含整条 $O$ 的 affine 邻域 $V$，使 $V$ 在 $[-1]$ 下稳定，$t$ 在 $V$ 正则且其零除子仅为 $O$，并使
$$
\eta_V=\eta-t^{-2}dt
\tag{1165.3}
$$
在 $V$ 正则。这样的 $V$ 由 (1165.2) 缩小得到；再与其 $[-1]$ 像相交。$U,V,U\cap V$ 均为 affine，所以两开集的 Čech–de Rham complex 计算原 relative de Rham cohomology。

令 $\mathcal C^-$ 表示该 complex 的 $[-1]^*=-1$ 部分；因 $2$ 是单位，可在整系数上投影。采用
$$
\begin{aligned}
\mathcal C^0&=\mathcal O(U)^-\oplus\mathcal O(V)^-,\\
\mathcal C^1&=\Omega^1(U)^-\oplus\Omega^1(V)^-\oplus
                       \mathcal O(U\cap V)^-,\\
\mathcal C^2&=\Omega^1(U\cap V)^- ,
\end{aligned}
$$
以及
$$
\begin{aligned}
d_0(f_U,f_V)&=(df_U,df_V,f_V-f_U),\\
d_1(\alpha_U,\alpha_V,h)&=\alpha_V-\alpha_U-dh .
\end{aligned}
\tag{1165.4}
$$
因此原两个 classes 的实际 cocycles 是
$$
\iota(\omega)=(\omega,\omega,0),\qquad
\iota(\eta)=(\eta,\eta_V,t^{-1}).
\tag{1165.5}
$$
第二个式子的 $t^{-1}$ 及 (1165.3) 的负号互相配合。

以下 residue 均沿原参数 $t$，取 $t^{-1}dt$ 的系数。它作用于实际 meromorphic forms；没有另选 Serre duality 或 Weil pairing 的尺度。

## 2. 直接读出两个系数的整投影

对 $c=(\alpha_U,\alpha_V,h)\in\mathcal C^1$，定义
$$
\boxed{\quad
\pi(c)=
 \operatorname{Res}_O\!\left(\frac{\alpha_U}{t}-h\eta_V\right)\omega
 +\operatorname{Res}_O(h\omega)\eta .
\quad}
\tag{1165.6}
$$
在其余 degrees 令 $\pi=0$，目标是
$M_E[-1]$，其中 $M_E=\mathcal O\omega\oplus\mathcal O\eta$。

首先，
$$
\pi\iota=1 .
\tag{1165.7}
$$
对 $\omega$，第一 residue 是 $1$，第二是 $0$。对 $\eta$，第一 residue 为
$\operatorname{Res}((\eta-\eta_V)/t)=\operatorname{Res}(t^{-3}dt)=0$，
第二为 $1$。

其次，$\pi d_0=0$。对 (1165.4) 的 boundary，第二 residue 为
$$
\operatorname{Res}((f_V-f_U)\omega)=0.
$$
这里 $f_V\omega$ 在 $O$ 正则；$f_U\omega$ 是原 proper 曲线上只可能在 $O$ 有极的 meromorphic form，故其 residue 为零。第一 residue 为
$$
\begin{aligned}
\operatorname{Res}\left(\frac{df_U}{t}
                  -(f_V-f_U)\eta_V\right)
 &=\operatorname{Res}\left(\frac{df_U}{t}
                         +f_U\eta-f_Ut^{-2}dt\right)\\
 &=\operatorname{Res}\left(d(f_U/t)+f_U\eta\right)=0.
\end{aligned}
\tag{1165.8}
$$
relative 底上的等式可先在 characteristic zero 泛纤维证明，再由整模无 $p$-torsion 得到；这里没有反除任何 residue 的 $p$ 因子。

Hodge filtration 中，$\operatorname{Fil}^1\mathcal C^1$ 的 $h$ 为零，故 (1165.6) 的像只在 $\mathcal O\omega$。因此 $\pi$ 是保 Hodge filtration 的整 chain map，而不仅是对 closed classes 的公式。

## 3. 实际收缩：用单位首项消主部

为使用 (1165.6) 时保留所有 chain homotopies，下面给出一个整 $H$，满足
$$
dH+Hd=1-\iota\pi,\qquad
\pi H=0,\qquad H\iota=0 .
\tag{1165.9}
$$

### 3.1 degree two 到 degree one

给 $\beta\in\mathcal C^2$。它在 $O$ 的 polar powers 都为负偶数：odd form 意味着其 $dt$ 系数为偶函数。各
$$
x^a\omega=t^{-2a}(1+\text{更高次})\,dt,\qquad a\ge1,
$$
有单位首项。按 pole order 从大到小消去 $\beta$ 的全部负次主部，得到 $b_U\in\Omega^1(U)^-$。最后增减唯一一倍 $\omega$，使
$$
\operatorname{Res}_O(b_U/t)=0 .
\tag{1165.10}
$$
于是 $b_V=\beta-b_U$ 在 $V$ 正则。定义
$$
H_2(\beta)=(-b_U,b_V,0).
\tag{1165.11}
$$
直接有 $d_1H_2\beta=\beta$，而 (1165.10) 给 $\pi H_2=0$。全部消元只用首项 $1$，不除 pole order 或 $p$。

### 3.2 degree one 到 degree zero

对 $c=(\alpha_U,\alpha_V,h)$，置
$$
b=\operatorname{Res}_O(h\omega),\qquad h_0=h-bt^{-1}.
$$
odd functions 的负次主部都是负奇数。各
$$
yx^a=-t^{-(2a+3)}(1+\text{更高次}),\qquad a\ge0,
$$
有首项 $-1$，因此可消去 $h_0$ 中所有 pole order 至少三的项。唯一可能的余项是 $t^{-1}$。它的系数也为零：每个 $yx^a\omega$ 的全局 residue 为零，而
$\operatorname{Res}(t^{-1}\omega)=1$，所以先减去的 $b$ 恰是这个最后的 gap coefficient。

因此可唯一写成
$$
h_0=f_V-f_U
\tag{1165.12}
$$
其中 $f_U$ 是上述 $yx^a$ 的有限整组合，$f_V$ 在 $V$ 正则。唯一性来自 proper 曲线上 global odd regular function 为零。定义
$$
H_1(c)=(f_U,f_V).
\tag{1165.13}
$$
令 $H=H_1+H_2$，在其他 degree 为零。

### 3.3 完整身份、滤过及完成

对 degree-one 的 $c$，差
$c-d_0H_1c-\iota\pi c$ 的 overlap function 为零。它的 $U$-form 的
$\operatorname{Res}(\alpha_U/t)$ 也为零。由于其两张 forms 的差是 $d_1c$，(1165.10) 的唯一归一说明
$$
c-d_0H_1c-\iota\pi c=H_2d_1c .
$$
degree zero 的身份由 (1165.12) 的唯一性给出；degree two 的身份就是
$d_1H_2=1$。这证明 (1165.9)。同时 $H_1H_2=0$，可取 $H^2=0$。

$H_1$ 在 $\operatorname{Fil}^1$ 上为零；$H_2$ 只输出 forms。因此 $H$ 保 Hodge filtration。$\iota,\pi,H$ 也全为 $\mathcal O$-线性，并且保 $p^n$ 倍子模。故这些公式从实际有限 pole-order complex 唯一连续延伸到其 $p$-adic completion；不能先忘记这条连续性再对无界 pole series 使用主部消元。

于是所有模 $p^n$ reductions 都具有同一整 filtered contraction。没有用 rational splitting、普通性，或只在 characteristic zero 成立的积分来建立它。

## 4. 全部原几何 projectors 与 PD 滤过

在 $\mathcal E^d$ 上使用 ordered product cover。每个 factor 先取 odd 部分，然后 tensor (1165.9)。若 $P=\iota\pi$，一个实际 tensor homotopy 为
$$
H^{(d)}
 =\sum_{j=1}^d
     P^{\otimes(j-1)}\otimes H\otimes
                 1^{\otimes(d-j)},
\tag{1165.14}
$$
张量算子的 Koszul 符号按原 degree 保留。其微分 telescope 为
$1-P^{\otimes d}$。

如须与所有 factor permutations 严格相容，将 (1165.14) 在这些 permutations 下平均。原 $d\le12<p$，所以只除 $d!$；odd projectors 只除 $2^d$，均为整单位。于是可限制到 R1163 的 signed $\epsilon_d$ 以及三个独立 paired projectors $P_0,P_2,P_4$。这不要求那三个 projectors 互相正交。

每个所得 filtered complex 只在 geometric degree $d$ 有 cohomology，且该 cohomology 是相应的整 direct summand $M$。所有 Hodge graded pieces 都自由。$M_E$ 的权为 $\eta$ 的零与 $\omega$ 的一；tensor 权和及实际 determinant factors 随 projector 保留。

令 $S$ 为原基底 PD ring，令
$$
D=S\widehat\otimes_{\mathcal O}M,\qquad
\operatorname{Fil}^{r}D
 =\sum_a \operatorname{Fil}^{r-a}S\,
                    \widehat\otimes\operatorname{Fil}^a_H M .
\tag{1165.15}
$$
把 $\iota,\pi,H$ 延伸为 $S$-线性。因为它们保 Hodge filtration，便严格保 convolution filtration (1165.15)。因此整 filtered relative PD–de Rham complex 实际收缩到 $D[-d]$。这也直接证明每个 $\operatorname{Fil}^r$ 的 cohomology 都只在 $d$，不是从一条未说明的 integral formality 假设出发。

本段只约去几何方向。底上的 $d\log z$ 没有被删除，实际 Frobenius 也没有被换成标记域上的 field automorphism。若 R1164 的 line frames 要求更细 cover，先保其真实 refinement map，再使用上述收缩；不声称 $\mathcal L_P$ 在整个 $U$ 上平凡。

## 5. 原 LT 基底上的实际 log-PD cone

现在使用 R1155 §16 的同一严格 LT 坐标及同一
$$
e=p^2-1,\qquad g=z^e-p,\qquad
S=\bigl(\mathcal O[z,\gamma_n(g):n\ge1]\bigr)^\wedge_p,
\quad \psi(z)=z^p .
\tag{1165.16}
$$
$\psi$ 在 $\mathcal O$ 上为原 $\sigma$。令
$$
\mathcal N=z\frac{\partial}{\partial z},\qquad
\Phi=\psi\otimes\Phi_M.
$$
这里 $\mathcal N$ 是 log-PD base derivation；不与 R1155 坏点 representation 的 Lie monodromy matrix 混为一物。曲线固定时其 geometric coefficients 对这个 base direction 常数，所以
$$
\mathcal N\Phi=p\Phi\mathcal N.
\tag{1165.17}
$$

$\Phi_M$ 是同一 good curve 的实际 crystalline Frobenius；不要求 $\mathcal E$ 自身存在 global Frobenius lift。原 $M_E$ 的强可除性及整 tensor/direct-summand 运算给
$\Phi_M(\operatorname{Fil}^a_HM)\subset p^aM$。

对 $0\le r\le p-2$，(1165.15) 上的 $p^{-r}\Phi$ 整。这里允许 $r$ 大于 $M$ 的最高 geometric Hodge weight：适配权 $w$ 的一项若 $w\ge r$，直接含 $p^r$；若 $w<r$，系数在 $\operatorname{Fil}^{r-w}S$，而原 PD 尾界给
$\psi(\operatorname{Fil}^{r-w}S)\subset p^{r-w}S$。因此并不需要额外假设 $r\le d$。

Tsuji §2 的实际 mapping fibre，经过 §4 的几何收缩与 degree shift 后，具有下面的 coefficient model：
$$
\begin{aligned}
C_r^0(D)&=\operatorname{Fil}^rD,\\
C_r^1(D)&=\operatorname{Fil}^{r-1}D\,d\log z\ \oplus D,\\
C_r^2(D)&=D\,d\log z,\\
d_0x&=\left(\mathcal Nx,\ (1-p^{-r}\Phi)x\right),\\
d_1(\omega,y)&=(1-p^{1-r}\Phi)\omega-\mathcal Ny .
\end{aligned}
\tag{1165.18}
$$
在最后两行把 $d\log z$ 的系数单独显示。form 上的 Frobenius 多一个 $p$，故 $d_1$ 是 $1-p^{1-r}\Phi$，不能仍写成 $1-p^{-r}\Phi$。由 (1165.17) 直接得 $d_1d_0=0$。

R1163 的三个输入对应
$(d,r)=(4,5),(8,9),(0,5)$；全部中心使用 $(d,r)=(12,14)$ 的实际 paired summands。实际 Poincaré coevaluation 仍按 R1163 的 $-c_1(\mathcal P)/2$，每份增加 geometric degree 二和 syntomic weight 一；四份给原 $\lambda_\infty x\gamma_5$ 的同一 weight 十四。不能重新将其 cup-pairing 常数设成未经校准的一。

这些 $d$ 均为偶数，故上述 geometric shift 不添加新的 ordered multiplication 符号。所有陈述先在 $p$-torsion-free 系统作出，再逐层约化；不在模 $p^n$ 后用一个可能已失去精度的式子定义 $p^{-r}\Phi$。

## 6. 代表进入 cone 时的 Frobenius homotopy

仅用 (1165.6) 投影第一槽不够。下面的代数身份给出必要的第二槽修正。

设实际 Frobenius 已在同一 filtered Čech/PD chain model $\mathcal C$ 上实现为 chain map $F$，且 $\iota,\pi,H$ 为已运输到该模型的实际收缩。记
$$
F_D=\pi F\iota,\qquad
Q_r=\pi(p^{-r}F)H .
\tag{1165.19}
$$
在 $\operatorname{Fil}^r\mathcal C$ 上，$Q_r$ 整：$H$ 保滤过，而 divided Frobenius 在该滤过上整。由 (1165.9)，
$$
\pi(p^{-r}F)-p^{-r}F_D\pi=dQ_r+Q_rd .
\tag{1165.20}
$$
在 relative geometric degree 已集中时，$F_D$ 正是 $\Phi_M$；加上 base 后是 (1165.18) 的实际 $\Phi$ 及其 form factor。

若 cone convention 是
$$
d(\alpha,\beta)=
 \left(d\alpha,\ (1-\varphi_r)\alpha-d\beta\right),
$$
则实际 chain map 为
$$
\boxed{\qquad
(\alpha,\beta)\longmapsto
       \bigl(\pi\alpha,\ \pi\beta+Q_r\alpha\bigr).
\qquad}
\tag{1165.21}
$$
将 (1165.20) 代入两边微分，第二槽的差准确为零。这里是加号。

(1165.19)–(1165.21) 是对实际已给 chain Frobenius 的显式公式，不能用来虚构尚未完成的 embedding comparison。若原 Tsuji embedding system 使用不同 PD envelopes 或 refinement，先将其 actual Frobenius、symbol 和 comparison homotopies 一起运输；那一步的实际 homotopy 仍是 (1165.21) 的输入。尤其不能只指定 cohomology 矩阵 $\Phi_M$，然后令 $F=\iota\Phi_M\pi$，并据此将原 $Q_r$ 宣为零。

因此 §2–§4 已给完整几何 coefficient projection 和收缩；将原 scalar symbol 的 Frobenius overlap 送进它，仍必须保实际代表。这个区别对指定中央 primitive 与 $F_0$ 至关重要。

## 7. 保序 cone 乘法及其明确同伦

对一般 filtered de Rham model，设 $(\alpha,\beta)$ 的 cone degree 为 $k$，另一项为 $(\gamma,\delta)$。两种常用 ordered products 是
$$
\begin{aligned}
P_0&=\left(\alpha\gamma,\
          \beta\gamma+(-1)^k\varphi_r(\alpha)\delta\right),\\
P_1&=\left(\alpha\gamma,\
          \beta\varphi_s(\gamma)+(-1)^k\alpha\delta\right).
\end{aligned}
\tag{1165.22}
$$
它们分别是 chain products；直接使用
$\varphi_{r+s}(\alpha\gamma)=\varphi_r(\alpha)\varphi_s(\gamma)$
及 Leibniz rule 即可验证。

定义双线性 degree-minus-one homotopy
$$
K((\alpha,\beta),(\gamma,\delta))
     =(0,(-1)^k\beta\delta).
\tag{1165.23}
$$
完整的链身份为
$$
P_0-P_1=dK+K(d\,\cdot,\cdot)+(-1)^kK(\cdot,d\,\cdot).
\tag{1165.24}
$$
第二槽两边都为
$\beta(1-\varphi_s)\gamma-(-1)^k(1-\varphi_r)\alpha\,\delta$。
这验证了所有 degree 的符号，而非只验证两个 closed classes。

degree-one factors 给 $K=(0,-\beta\delta)$。若指定 primitive 满足
$dh=-P_0$，改用 $P_1$ 时须同时用 $h+K$，因为
$d(h+K)=-P_1$。原中央 ordered coordinate 不允许删掉这个二次项。

在 (1165.18) 的一维 base complex 中，两项 degree-one 的 product 第二槽是
$$
y\,\omega'-\bigl(p^{1-r}\Phi\omega\bigr)y',
\tag{1165.25}
$$
第一槽的两个 base one-forms wedge 为零。geometric contractions、Poincaré classes 及 R1164 的 root/chord homotopies 仍按原顺序附上；(1165.25) 不替代它们。

## 8. 全 normal connection 与有界精度

### 8.1 不能先作 $g=0$

在 R1155 的唯一基 $z^j\gamma_n(g)$（$0\le j<e$）上，
$$
\boxed{\quad
\mathcal N(z^j\gamma_n(g))
 =(j+en)z^j\gamma_n(g)+ep\,z^j\gamma_{n-1}(g)
\quad(n\ge1).
\quad}
\tag{1165.26}
$$
$n=0$ 时只有 $jz^j$。因此若
$f=\sum m_{j,n}z^j\gamma_n(g)$，则
$$
[\mathcal Nf]_{j,n}
 =(j+en)m_{j,n}+ep\,m_{j,n+1}.
\tag{1165.27}
$$
这是原 normal carry，不是标记域上的 derivation：先令 $g=0$ 会丢掉第二项。

也必须保完整
$$
c=\frac{\psi(g)}p.
$$
由 $\psi(g)=(g+p)^p-p$ 及 Wilson，
$$
c\equiv-1-\gamma_p(g)\pmod {pS}.
\tag{1165.28}
$$
这里 $\gamma_p(g)$ 一般不为零。由于
$$
\gamma_p(g)^p=\frac{(p^2)!}{(p!)^p}\gamma_{p^2}(g),
\qquad
v_p\!\left(\frac{(p^2)!}{(p!)^p}\right)=1,
$$
$\gamma_p(g)$ 模 $p$ 为 nilpotent，故 $c$ 是 $S$ 中的单位。只有在原 evaluation $z=\varpi,\ g=0$ 后，才回到
$c_0=p^{p-1}-1\equiv-1$。

因此 R1155 的有限 evaluation 窗口不意味着可以在整个 syntomic complex 中删去所有 normal degree 大于二十八的项；$\psi$ 本身已经产生 (1165.28) 的 degree $p$ 项。

### 8.2 保微分与 divided Frobenius 的精度理想

对 $h\ge0$ 定义闭理想
$$
I_h=\sum_{a=0}^h p^{h-a}\operatorname{Fil}^aS .
\tag{1165.29}
$$
由唯一 normal basis，其商只保
$n<h$ 的系数，精度为 $p^{h-n}$；$n\ge h$ 的项均在 $I_h$。
特别 $S/I_1=\mathcal O_L/p$，其中保全部真实 ramified nilpotents。

由 (1165.26)，
$$
\mathcal N I_h\subset I_h .
\tag{1165.30}
$$
降低 normal degree 一时出现的 $p$ 恰补足提高的一位精度。另一方面，对 $0\le h\le p-2$，
$$
\psi(I_h)\subset p^hS .
\tag{1165.31}
$$
这是因为 $\psi(\operatorname{Fil}^aS)\subset p^aS$，包括所有 $n\ge p$ 的 factorial 尾；不能只检查 $n<p$。

故要在除 $p^i$ 后保模 $p$，$I_{i+1}$ 的误差足够小。对原需要的 $i\le28$，$p>37$ 使全部范围成立。

更明确，对 $1\le r\le p-3$，(1165.18) 有自然有限商 complex
$$
\begin{aligned}
\overline C_r^0
 &=\operatorname{Fil}^rD/
           (\operatorname{Fil}^rD\cap I_{r+1}D),\\
\overline C_r^1
 &=\left(\operatorname{Fil}^{r-1}D/
           (\operatorname{Fil}^{r-1}D\cap I_rD)\right)d\log z
       \oplus D/I_1D,\\
\overline C_r^2&=(D/I_1D)d\log z .
\end{aligned}
\tag{1165.32}
$$
其微分由原式诱导：$\mathcal N$ 保各 $I_h$，
$p^{-r}\Phi(I_{r+1}D)\subset pD$，
$p^{1-r}\Phi(I_rD)\subset pD$。
这逐项证明了 well-definedness。

(1165.32) 用来保一个已给原 representative 的指定读取精度。本篇不声称此有限商自动计算整个 syntomic cohomology，也不声称各权的这些商无需另配精度就形成完整 cup algebra。

### 8.3 与原有限窗口的接合

R1155 §16 的 factorial 尾证明实际上只需
$0\le i\le p-2$，并不需要 $i$ 小于系数的最高 geometric Hodge weight。于是对同一适配基 $e_b$、权 $w_b$ 和
$F_b=p^{-w_b}\Phi e_b$，
$$
\operatorname{ev}(p^{-i}\Phi x)\equiv
 \sum_{\substack{b:\,w_b\le i\\0\le j<p}}
 \frac{(-1)^{i-w_b}}{(i-w_b)!}
       \sigma(m_{b,j,i-w_b})\,\varpi^{pj}F_b\pmod p .
\tag{1165.33}
$$
当 $w_b>i$ 时所有项自动含 $p$。因此本篇的
$(d,r)=(12,14)$ 并没有越出整除界。

若同一系数先由 R1162 的整 $z$-函数写出，仍用其真实
$e$-block 与逐层 precision 公式取得 $m_{b,j,n}$。
(1165.6) 和 (1165.21) 现在说明这些系数应从哪一个
Čech/coefficient representative 读取；不能把 raw Frobenius matrix 再当 filtered input 施一次 $\Phi$。

## 9. 已支付的输入与尚须实际读取的量

本篇已给：

- 原 $\omega,x\omega$ 的两条 residue 投影及整 filtered contracting homotopy；
- 全部十二因子以下的原 signed/paired projectors 与 PD 滤过上的同一收缩；
- 保留 base log direction、正确 form Frobenius 因子的三项 coefficient cone；
- 代表运输时第二槽的 $+Q_r\alpha$，以及有序乘法的 $-\beta\delta$；
- 完整 normal connection、$\gamma_p(g)$ carry 及保持实际读取精度的有限商。

原 R1164 的实际整 frames、其 PD embedding/refinement 与 Frobenius-overlap homotopies 必须真的送入这些公式。原 theta norms、closed-point Cor、R1159–1160 的算术 subtraction 和指定中央 gauge 继续保留。实际 $F_0$ 及其 normal coefficients 尚未在本篇取值，主课题的绝对一致性标准仍未达到。

## Primary 与范围

T. Tsuji, *On p-adic nearby cycles of log smooth families*, Bulletin de la Société Mathématique de France **128** (2000), 529–575，[正式原文](https://www.numdam.org/article/BSMF_2000__128_4_529_0.pdf)，§2 尤其 pp.539–543 的 PD mapping fibre、(2.5)–(2.7) 及 Appendix Lemma A2（p.562）的实际 symbol。本篇使用的整 comparison 范围与 R1163 相同。

§§1–4 的收缩、§§6–8 的链身份及精度由正文自足证明。它们不需要 ordinary 假设，也不把分歧域误装成带 field Frobenius 的未分歧底。全文无数学程序执行。
