# R267 后续：原全旗平坦分母与实际范数稠密主理想的严格分离

日期：2026-11-29（Asia/Taipei）。作者：AI-assisted GPT-6 Astra Pro；会话 Astra-ISP-8542378f-20261127。

本稿使用同一原 Haar 算子与完整 carry，证明既有固定分母 $Q_*$ 虽在每个原普通不变旗上准亲和，却不在新实际范数理想上生成稠密乘子像。由此把两种此前尚未连接的来源条件准确分开。结论不排除 $Q_*$ 的原平方分子，也不排除原闭稳定根。

## 1. 同一原来源及结论

固定 $C=A^{(m_0)}$、$\mathscr A=C'$。沿用
$$
N_j=C^{2^j}/\|C^{2^j}\|,\qquad
N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
a_j=(j+1)^{-1},
$$
$$
V_j=(I-N_j)(I+N_j)^{-1},\qquad
Z=I+\sum_{j\ge0}a_jV_j,\qquad L=Z^{-1}.
\tag{1}
$$
这里 $E_j=|0\rangle\langle1|$ 是第 $j$ 位实际删除，$\eta_j$ 是同一原相邻权比。原界给 $\sum\eta_j<1$、$\|(I+N_j)^{-1}\|\le3$，并已支付 $Z$ 的最大增生实现及有限柱核心。

记
$$
g^2=\sum_{j\ge0}a_j^2,\qquad e=\sum_{j\ge0}a_j\eta_j,\qquad
h_0=1+2\log2,\qquad M_0=\sqrt{h_0^2+g^2}+8e.
\tag{2}
$$
原[范数 Banach 理想稿](R12-appendix-actual-norm-ideal-full-multipliers-quasimultipliers-and-common-inverse-core.md)定义
$\mathscr B=\overline{L\mathscr A}^{\,\|\cdot\|}$，并付清其收缩近似单位及 $\Omega(\mathscr B)$。

使用[固定分母原稿](R267-appendix-fixed-original-denominator-and-norm-square-vacuum-source.md)中的同一 $Q_*$，则
$$
\boxed{\operatorname{dist}(L,Q_*\mathscr A)\ge M_0^{-1}>0.}
\tag{3}
$$
特别 $\overline{Q_*\mathscr B}\ne\mathscr B$。这里没有把 $Q_*\in\mathscr B$ 当作前提；(3) 排除的是其乘子像的范数稠密性。

同样的分离对[同参数原构造](R267-appendix-all-factor-complex-parameter-odd-target-and-norm-square-source.md)中的每个固定 $T(z),P(z)$，以及每个固定 $X(s)$（$s\ne0$）成立。各自仍保留此前已经证明的全部 Hilbert 旗子商准亲和性质。

## 2. 一个完整原行的有界 UHF 余项

置
$$
K=\sum_{j\ge0}a_j\bigl(V_j-I+2E_j\bigr).
$$
准确 Cayley 式及 $N_j^2=\eta_jN_{j+1}$ 给
$$
V_j-I+2E_j=-2(N_j-E_j)+2N_j^2(I+N_j)^{-1},
$$
所以
$$
\|V_j-I+2E_j\|\le8\eta_j,\qquad \|K\|\le8e.
\tag{4}
$$
每个 $N_j$ 与 $E_j$ 均在原 UHF 代数中，$I+N_j$ 的逆也在同一单位化 $C^*$ 代数中。因此 (4) 是 UHF 里的范数绝对收敛级数，不只是强余项。

写 $\Omega_j=(|0\rangle+|1\rangle)/\sqrt2$、
$\chi_j=(|0\rangle-|1\rangle)/\sqrt2$。对有限集合 $S$，令
$x_S=\bigotimes_{j\in S}\chi_j\otimes\bigotimes_{j\notin S}\Omega_j$，
并记 $\epsilon_j=-1$（$j\in S$）、$\epsilon_j=1$（$j\notin S$）。
全部 $x_{S\triangle\{j\}}$ 两两正交，且
$$
E_jx_S=\frac{\epsilon_j}{2}
\bigl(x_S+x_{S\triangle\{j\}}\bigr).
$$
由原有限柱核心上的行收敛，
$$
Zx_S=Z_0x_S+Kx_S,
$$
$$
Z_0x_S=
\left(1+2\sum_{j\in S}a_j\right)x_S
-\sum_{j\ge0}a_j\epsilon_jx_{S\triangle\{j\}}.
\tag{5}
$$
后一正交级数在 $H$ 收敛；没有将无界 $Z_0$ 视为全域有界算子。

## 3. 保原强费用而被长等权块压掉的向量

给定任意 $b\ge1$、$q\ge1$，置
$$
J=\{b,\ldots,b+q-1\},\qquad
S=\{b+\lceil q/2\rceil,\ldots,b+q-1\},\qquad x=x_S.
$$
于是 $|S|=\lfloor q/2\rfloor$，$d=q-2|S|\in\{0,1\}$，并且
$$
\sum_{j\in S}a_j\le\log2.
$$
从 (5) 的正交性立刻得到
$$
\|Zx\|\le M_0,\qquad \|x\|=1.
\tag{6}
$$

保留同一原等权块
$$
F_{b,q}=\frac2{q+2}\sum_{j\in J}N_j,\qquad
D_{b,q}=\frac2{q+2}\sum_{j\in J}E_j.
$$
原 $F_{b,q}$ 是收缩，而且
$$
\|F_{b,q}-D_{b,q}\|
\le\frac2{q+2}\sum_{j\in J}\eta_j\longrightarrow0
\tag{7}
$$
在 $b$ 上一致。关键原来源结论是
$$
\boxed{\|F_{b,q}Zx_S\|\longrightarrow0\quad(q\to\infty),}
\tag{8}
$$
也在任意起点选择 $b=b(q)$ 下成立。

先完整支付 $Z_0$ 部分。令 $h=1+2\sum_Sa_j$、
$B_J=\sum_Ja_j$。把 (5) 乘以 $D_{b,q}$，按零、一、二次翻位正交分解，其系数在统一分母 $q+2$ 下准确为：

- 零翻位：$hd+B_J$；
- 单翻位 $j\in J$：$(h-da_j)\epsilon_j+2a_j$；
- 单翻位 $j\notin J$：$-da_j\epsilon_j$；
- 双翻位 $i,j\in J$：$-(a_i+a_j)\epsilon_i\epsilon_j$；
- 双翻位 $i\in J,j\notin J$：$-a_j\epsilon_i\epsilon_j$。

没有更高翻位。利用 $h\le h_0$、$B_J\le1+\log(q+1)$ 及
$$
\sum_{\substack{i<j\\i,j\in J}}(a_i+a_j)^2
=(q-2)\sum_{j\in J}a_j^2+B_J^2,
$$
得到保守但完整的同源界
$$
\|D_{b,q}Z_0x_S\|^2
\le
\frac{2(q+1)h_0^2+4(1+\log(q+1))^2+(q+19)g^2}{(q+2)^2}
\longrightarrow0.
\tag{9}
$$
$q=1$ 时双翻位和为空，同一个上界仍有效。(7) 及
$\|Z_0x_S\|\le\sqrt{h_0^2+g^2}$ 因而给 $F_{b,q}Z_0x_S\to0$。

再支付完整 $K$。任给 $\delta>0$，以只作用前 $M$ 位的 $K_M$ 作范数逼近，
$\|K-K_M\|<\delta$。准确地，
$$
\|D_{b,q}x_S\|=\frac{\sqrt{d^2+q}}{q+2},\qquad
\|[D_{b,q},K_M]\|\le\frac{4M\|K_M\|}{q+2}.
\tag{10}
$$
所以 $D_{b,q}K_Mx_S\to0$；由 (7) 同样有
$F_{b,q}K_Mx_S\to0$。最后用 $\|F_{b,q}\|\le1$，
$$
\limsup_{q\to\infty}\|F_{b,q}Kx_S\|\le\delta.
$$
令 $\delta\downarrow0$ 即得 (8)。这一步不要求因子块逃离有限头，也未丢掉低位 carry。

## 4. 代入原固定分母，不改选择

原相容族使用 $F_\nu=F_{b_\nu,q_\nu}$，且
$\|(F_\nu-I)\Omega\|\to0$。该条件本身迫使 $q_\nu\to\infty$。事实上
$$
1-\Re\langle F_{b,q}\Omega,\Omega\rangle
\ge\frac{2(1-\sum_j\eta_j)}{q+2}>0.
\tag{11}
$$
故有界 $q_\nu$ 不能满足原误差趋零。

按 §3 对每个真实块选择 $x_\nu$，令
$$
u_\nu=Zx_\nu.
$$
则
$$
\|u_\nu\|\le M_0,\qquad Lu_\nu=x_\nu,\qquad
\|F_\nu u_\nu\|\to0.
\tag{12}
$$

固定分母的准确原式为
$$
Q_*=R_0T(0),\qquad
T(0)=\mathrm{strong*}\!-\!\lim_M
\prod_{\nu=1}^{M-1}\bigl((1-\zeta_\nu)F_\nu\bigr)^{d_\nu/2}.
$$
每个 $\nu\ge1$ 的 $d_\nu/2$ 是正整数；所有其他因子为交换收缩。删去一个指定的 $F_\nu$ 后，余积的同一强极限存在且范数至多 $1$。因此
$$
\|Q_*u_\nu\|\le\|R_0\|\,\|F_\nu u_\nu\|\longrightarrow0.
\tag{13}
$$
这里 $R_0$ 是原固定有界首因子，不依赖 $\nu$。

任取 $A\in\mathscr A$，交换性及 (12)–(13) 给
$$
\|(L-Q_*A)u_\nu\|
\ge1-\|A\|\|Q_*u_\nu\|\longrightarrow1
\quad\text{作为下界}.
$$
结合 $\|u_\nu\|\le M_0$ 得 (3)，再取 $A$ 的范数闭包仍成立。

## 5. 整个原曲线的同一范数边界

对任意固定 $z$，
$$
Z_\nu(z)=(1-\zeta_\nu)F_\nu+z\zeta_\nu C/c,\qquad
\|Z_\nu(z)u_\nu\|\to0
\tag{14}
$$
来自 (12)、$\zeta_\nu\to0$ 与 $u_\nu$ 统一有界。

原 $T(z)$ 的完整整数尾指数为 $d_\nu/2\ge1$，因子范数乘积不超过
$\exp(|z|\sum d_\nu\zeta_\nu/2)$。从其中提出指定的一个 $Z_\nu(z)$ 后，其他因子的实际强极限有相同的统一上界，故 (14) 给
$$
T(z)u_\nu\to0.
$$
$P(z)=CZ_0(z)T(z)^2$ 及
$X(s)=CB(s)T(s^2)$ 的其余因子在每个固定参数处有界，所以
$$
P(z)u_\nu\to0,\qquad X(s)u_\nu\to0\quad(s\ne0).
\tag{15}
$$
由与 (3) 完全相同的交换配对，
$$
\operatorname{dist}(L,G\mathscr A)\ge M_0^{-1},
\qquad G=T(z),P(z),X(s),Q_*.
\tag{16}
$$
没有对随参数移动的前因子 $B(s)$ 声称一致范数界。

## 6. 准确的来源意义

这些 $G$ 都有既有的原 Hilbert 全旗准亲和证明，且相关原成员属于共同全部幂理想。然而 (16) 使其在 $\mathscr B$ 上的乘子像不稠密；与任意固定 $\mathscr A$ 元素相乘也不能修复这个范数稠密性。

相对地，[共同幂范数逼近稿](R12-appendix-accretive-sources-norm-approximated-by-common-power-quasiaffinities.md)构造的 $R_nP_\theta$ 真正在
$\mathfrak F\cap\Omega(\mathscr B)$。因此本结论识别的是两类实际共同幂来源的不同范数位置，而不是将旧强单位或全旗单射作废。

这不推出任何 $G$ 不存在原平方分子；它只证明不能把这些指定分母直接放进 $\mathscr B/\Omega(\mathscr B)$ 当成合法范数稠密分母。原平方源、同列强紧性以及一般平坦理想的范数闭包仍须另付。
