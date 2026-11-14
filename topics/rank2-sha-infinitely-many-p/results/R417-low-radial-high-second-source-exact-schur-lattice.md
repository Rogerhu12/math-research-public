# R417：低径向、高第二来源预算的真实 Schur 格与全部 Smith 因子

日期：2026-11-14。**状态：已证明。** 在保持原径向次数 $D=1$ 时，本篇用真实 $T$ 幂列计算整个三块评价像。只要 $J_0\ge s-8$，相对评价的唯一模 $p$ 余核由一个明确的实际首核向量支付，其 Schur 系数在所有好惰性 $p>83$ 上均为单位。乘回原十三阶公共因子后，完整矩阵恰有二十七个 $p$ 因子，没有隐藏的 $p^2$ 因子。增加到 $j\asymp p/6$ 的实际来源成本完整保留；结论没有把原两个中央零假设传播到任意乘积。

## 1. 实际来源及统一参数

使用 R403/R415 的共同 $E_1:y^2=x^3+1$ 正规化，令
$$
p=6s-1>83,\qquad 1\le\ell<s-13,\qquad L=2s+\ell,
$$
$$
\Gamma_L=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),\qquad
a=a_p\in\mathcal O^\times,\quad \alpha=36/17.
\tag{1}
$$
原物理来源为
$$
\mathscr R_{\rm phys}=g(w)e_2(a\epsilon),\qquad
T_{\rm phys}=\widehat T(w)e_2(\alpha a\epsilon),
$$
$$
g(0)=1,\qquad t(w)=-w+\cdots,\qquad
\widehat T(w)=w+\cdots.
\tag{2}
$$
全部普通级数仍用原 Gaussian 正规化，在所用有限窗口中整；尤其 $\widehat T$ 不是在高阶擅自换成未正规化的原 $T$。

取有限的实际列呈示
$$
\mathcal W_{1,J_0}=\bigoplus_{j=0}^{J_0}
\left(\mathcal O[t]_{\le4}\oplus
\mathscr R\mathcal O[t]_{\le8}\right)T^j,
\qquad J_0\ge s-8.
\tag{3}
$$
这里 $N=14(J_0+1)$ 是自由呈示的秩。即使 $J_0>16$，(3) 仍定义为带真实标签 $(n,k,j)$ 的自由模块，评价其真实函数；不声称这些函数全无代数关系，也不把 R406 的十七部分直和证明延长到这些幂。实际角次数、$T$ 幂次数及其全局代价均未减少。

记实际相对评价及完整评价为
$$
J:\mathcal W_{1,J_0}\longrightarrow\Gamma_L,
\qquad M=m_{13}J:\mathcal W_{1,J_0}\longrightarrow\Gamma_{L+13}.
\tag{4}
$$
相对 Euler 在列 $\mathscr R^nt^kT^j$ 上的本征值准确是 $n+\alpha j$。公共 charge 四十仍属于原 $G_0=w^{13}U_0$，没有移到这个相对本征值里。

## 2. 模 $p$ 像准确为径向超平面

在 $\Gamma_L$ 的两条径向常数 $e_s=\epsilon$、$e_{2s}=\epsilon^2$ 上定义整行
$$
\lambda^J=(-a/2)[e_s]^*+[e_{2s}]^*.
\tag{5}
$$
R415 的完整三块恒等式在相对目标中同样给
$$
\lambda^J J(P)=
pa[w^s]\{(\mathcal E_{\rm rel}-1/2)P\}_{\rm reg}
+p^2[w^{2s}]P_{\rm reg}.
\tag{6}
$$
其原因仍是 $j>0$ 的普通常数为零，而 $j=0$ 时径向次数只有零、一，所以 $W_{2,0}=W_{1,0}$。特别 $\bar\lambda^J\bar J=0$。

**命题 1。** 对 (1)–(3) 的全部参数，
$$
\boxed{\operatorname{im}\bar J=\ker\bar\lambda^J,
\qquad\operatorname{rank}\bar J=L-1.}
\tag{7}
$$

**证明。** 仍按普通 $w$ 阶 $r$ 过滤模 $p$ 的整个目标。其第 $r$ 阶有三行，当 $r<\ell$；有两行，当 $\ell\le r<s$。真实列 $(n,k,j)$ 的首阶为 $r=k+j$，其该阶首向量为
$$
(-1)^k w^r e_2\big((n+\alpha j)a\epsilon\big).
\tag{8}
$$
模 $p$ 后所有高 carry 含 $p$，不产生较低 $w$ 阶；$g,t,\widehat T$ 的全部高项则仅产生更高阶。以下均是 (3) 中真正存在的列。

- $r=0$：取 $(0,0,0)$、$(1,0,0)$。它们在三条常数行上张成 $\ker\bar\lambda^J$，秩二。
- $1\le r<\ell$：取
  $$
  (0,1,r-1),\quad(1,1,r-1),\quad(0,0,r).
  \tag{9}
  $$
  三个 charge 是 $c,c+1,c+\alpha$，其中 $c=\alpha(r-1)$。首向量行列式，除符号单位外，是
  $$
  \frac{a^3}{2}\alpha(\alpha-1),
  \tag{10}
  $$
  为单位，因为 $\alpha=36/17$、$\alpha-1=19/17$ 且 $p>83$。
- $\ell\le r\le\min(J_0,s-1)$：取 $(0,0,r)$、$(1,0,r)$，charge 差为一，两行行列式为单位 $a$。
- $J_0<r<s$：取
  $$
  (1,r-J_0,J_0),\qquad(1,r-J_0+1,J_0-1).
  \tag{11}
  $$
  因为 $J_0\ge s-8$，这里 $1\le r-J_0\le7$，角次数分别不超过七、八。又 $s\ge15$ 给 $J_0\ge7$，故两个 $j$ 都非负。由 $\ell\le s-14<J_0$，这些阶只有两行；两个 charge 差为 $\alpha$，所以行列式仍为单位。

(9) 所用 $j\le r<\ell$ 自动不超过 $J_0$。不同 $r$ 选出的列首阶不同，因此没有重复标签。删去目标的 $e_{2s}$ 常数行后，选出的 $L-1$ 行列构成分块三角单位子式：$r=0$ 的两行行列式为 $a$，其余由 (10)–(11) 给出。故模 $p$ 秩至少 $L-1$；(5) 已给一个非零左行，得到 (7)。$\square$

## 3. 一个真实首核列给出全惰性单位

取 (3) 中的实际基列
$$
\boxed{P_* = \mathscr R t^8 T^{s-8}.}
\tag{12}
$$
它的正规化普通部分是
$$
(P_*)_{\rm reg}=g(w)t(w)^8\widehat T(w)^{s-8}
=w^s+O(w^{s+1}).
\tag{13}
$$
所以整个模 $p$ 的三块像均为零，即 $P_*\in K_1(J)$。这里使用的是相对评价本身的真实首核，尚不需要十三行边界来使它入核。

在首 Bockstein 中用 (6) 除以 $p$。其第二项保持为 $p[w^{2s}](P_*)_{\rm reg}$，由实际正规化整性模 $p$ 为零。(13) 的 $w^s$ 系数恰为一，相对 charge 为 $1+\alpha(s-8)$，故
$$
\bar\lambda^J\beta_1^J(P_*)
=\bar a\bigl(1/2+\alpha(s-8)\bigr)
=-\frac{547}{34}\bar a.
\tag{14}
$$
这里使用 $s\equiv1/6\pmod p$。整数 $547$ 是素数且 $547\equiv1\pmod6$，故不可能等于本篇的惰性素数；$p>83$ 同时排除 $2,17$。因此 (14) 对本篇每一个 $p$ 都是单位，没有额外有限坏素数集合。

这一步只用首项为一，未在高阶以未正规化的 $T^{s-8}$ 替换 $\widehat T^{s-8}$，也未假设该实际乘积继承任何原中央零条件。

## 4. 整像是唯一指数 $p$ 格

令
$$
\Lambda=\{v\in\Gamma_L:\lambda^J(v)\in p\mathcal O\}.
\tag{15}
$$
它是 $\Gamma_L$ 的指数 $p$ 子格；在有限剩余域的情形，这是商同构于 $k$ 的长度一子格。

**定理 2。** 在 (1)–(3) 下，实际整像准确为
$$
\boxed{J(\mathcal W_{1,J_0})=\Lambda.}
\tag{16}
$$
所以 $J$ 的全部非零 Smith 因子是 $L-1$ 个单位和一个 $p$；其余 $N-L$ 列是自由核方向。

**证明。** (6) 给出像包含于 $\Lambda$。(7) 给出 $L-1$ 个单位 Smith 因子，剩余目标方向是一维。实际首核向量 (12) 在这一维上的首 Bockstein 是单位 (14)，故剩下的 Smith 因子准确为 $p$，不能为 $p^2$ 或零。等价地，把 (12) 添到命题 1 的 $L-1$ 个源列后，所得整方子式的行列式是 $p$ 乘单位。其像与 $\Lambda$ 同为长度一子格，包含关系即为相等。$\square$

特别，这个整像不是仅由一条抽象模 $p$ 秩式推测出来的；首提升已经由同一个真实列 $P_*$ 付清。

## 5. 原十三行、二十六条跨界带与二十七个 $p$

仍用完整目标的实际整基
$$
e_r=w^r/p^{\lfloor r/s\rfloor},\qquad
m_{13}(e_r)=p^{\delta_r}e_{r+13},
$$
$$
\delta_r=\left\lfloor\frac{r+13}{s}\right\rfloor
-\left\lfloor\frac r s\right\rfloor.
\tag{17}
$$
由于 $s>13$、$L+13<3s$，$\delta_r=1$ 恰在
$$
\mathcal B=[s-13,s-1]\ \cup\ [2s-13,2s-1].
\tag{18}
$$
这两条完整边界共二十六个指数。径向常数下标 $s,2s$ 均不在其中。

(15) 的一组整基是
$$
e_r\ (r\ne s,2s),\qquad
u_1=e_s+(a/2)e_{2s},\qquad u_2=p e_{2s}.
\tag{19}
$$
乘 $m_{13}$ 后，特殊两列是
$$
e_{s+13}+(a/2)e_{2s+13},\qquad p e_{2s+13}.
\tag{20}
$$
在目标的这两行作行列式一的基变换
$$
v_1=e_{s+13}+(a/2)e_{2s+13},\qquad
v_2=e_{2s+13},
\tag{21}
$$
便将 (20) 变成一个单位因子和一个 $p$ 因子。(21) 不触及 (18) 的二十六条边界像；其余来源基仍按 (17) 逐项为单位或 $p$。因为 $J$ 整满射到自由格 $\Lambda$，(19) 每个向量均有真实整源提升，且可选整右逆，故这是原完整矩阵的整 Smith 计算。

**定理 3。** 完整 $M$ 的非零 Smith 因子准确为
$$
\boxed{\underbrace{1,\ldots,1}_{L-27},\qquad
\underbrace{p,\ldots,p}_{27}.}
\tag{22}
$$
自由余核秩为十三，自由来源核秩为 $N-L$。对每个 $h\ge1$，
$$
\operatorname{length}_{\mathcal O}\ker(M\bmod p^h)
=h(N-L)+27.
\tag{23}
$$
没有 $p^2$ 因子：唯一的额外 $p$ 因子来自 (19)，其两个坐标不在原跨界带内。这是保留十三行及整基变换后的结论，不是把两个 Smith 数列逐项相乘。

## 6. 整个原 $U_0$、真正第二余核及双接触

原物理矩阵是
$$
M^{\rm orig}=c_*U_0M.
\tag{24}
$$
整个 $c_*U_0$ 是原目标上的整可逆变换，故保持 (22)–(23)。本篇不声称它保持 (16) 的具体指数 $p$ 格；其实际像应准确写成 $c_*U_0m_{13}\Lambda$。对应左行按 $\lambda(c_*U_0)^{-1}$ 运输，保留原 $P_{134}$、全部高项和公共 charge。

令
$$
\mathcal F_{13}=\bigoplus_{r=13}^{L+12}\mathcal O e_r
\subset\Gamma_{L+13}.
\tag{25}
$$
这是完整像的饱和格，且是目标中的理想：整基的乘积只增加下标，越过边界只多出非负的 $p$ 次数。乘目标单位及其逆均保持它。因此 (24) 的饱和格仍是同一个 $\mathcal F_{13}$。

按 R338 的真实定义，
$$
C_2(M)=\operatorname{coker}\bar M\big/\beta_1^M(K_1(M)).
\tag{26}
$$
(22) 的二十七个 $p$ 因子都由完整首 Bockstein 支付，所以
$$
\boxed{C_2(M)=\Gamma_{L+13}/(p\Gamma_{L+13}+\mathcal F_{13})
=\bigoplus_{r=0}^{12}k[e_r].}
\tag{27}
$$
同式适用于原 (24)。可提升模 $p^2$ 左核的约化只支撑最初十三行；这些行在原矩阵中恒为零。所以真实第二 Bockstein 为零。代入 R406 的同源双接触公式时，所有使用的 $\bar\lambda_{1,j+13}$、$\bar\lambda_{2,j+13}$ 也均为零，于是实际耦合向量仍为 $q=r=0$。

这个结论保留 R403 两条完整中央基准及其全部 wrap。它证明的是来源增至 (3) 后实际有限评价的第二对偶已经消失；并不判定原 $S,T$ 的中央导数是否同时为零。因而要从非零双接触逼出主结论，来源预算必须低于本篇阈值，或另有新的全局配对。不能将任意 $T$ 幂列当作由两个中央零条件自动提供的零列。

## 依据与核验

- R403 的共同实际正规化、两条不同 Gaussian charge 及完整中央基准。
- R415 的原径向行和完整首提升恒等式；本篇使用的 (12) 更属于 $K_1(J)$ 本身。
- R338/R351 的完整十三行运输及首 Bockstein 提升判据。
- R412 的整基 (17) 与真实第二余核读法；本篇另行给出指数 $p$ 格，未套用其整满射假设。

脚本 [check-r417-low-radial-exact-schur.py](../scripts/check-r417-low-radial-exact-schur.py) 核选列条件、charge 行列式、固定系数 $547$，并在两个实际正规化矩阵上核 (14)、(22)。全参数结论由正文的选列与整格证明给出。
