# 原 Lamé 三对角与短六阶条件的同源运输（工作续稿）

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126 / o1_theta。

本文只继续已经发布的 R1113 §§8–9。下列矩阵和运输均是原曲线上的精确恒等式；最后的指定短像空间包含问题仍未排除，不把完整算子的简单谱当成原两读数的非同时零证明。没有执行数学程序或重新扫描素数。

## 1. 原同一空间及三对角

沿用
$$
p=6k-1,\quad N=k-1,\quad m=3k-1,\quad
E:V^2=U^3+v^2,\quad v^2=-108,\quad
D U=2V,\quad D V=3U^2,
$$
以及原
$$
\mathscr B=D^3-3UD-3V,\qquad
\mathscr C=UD+V,\qquad
W_{\mathscr C}=U^2\,\overline{\mathbf F}_p[V]_{\le 2N}.
$$
R1113 已证明两个算子都保持该空间。置
$$
w=\frac{V-v}{V+v},\qquad
g_r=U^m w^r
 =U^2(V-v)^{N+r}(V+v)^{N-r},\qquad -N\le r\le N.
\tag{T1}
$$
这些是原 $\mathscr C$ 的本征基，$\mathscr Cg_r=6rv\,g_r$。在同一基中，
$$
\boxed{\ 
\mathscr B g_r=b_+(r)g_{r+1}+b_0(r)g_r+b_-(r)g_{r-1}\ },
\tag{T2}
$$
其中
$$
\begin{aligned}
b_+(r)&=\frac v4(6r+1)(6r+3)(6r+5),\\
b_-(r)&=\frac v4(6r-1)(6r-3)(6r-5),\\
b_0(r)&=-3vr(36r^2+13).
\end{aligned}
\tag{T3}
$$
端点准确为 $b_+(N)=b_-(-N)=0$；其余内部上下系数全部为单位。

为直接核实，记 $c=6rv$。有
$$
D\log g_r=\frac{c-V}{U},\qquad
\frac{D^2g_r}{g_r}=\frac{c^2-4cV+3v^2}{U^2}.
$$
第三次微分并减去 $3UD+3V$ 得
$$
\frac{\mathscr B g_r}{g_r}
=\frac{c^3+18cv^2+5cV^2-(9c^2+15v^2)V}{V^2-v^2}.
\tag{T4}
$$
现在使用
$$
\frac1{V^2-v^2}=\frac{w+w^{-1}-2}{4v^2},\qquad
\frac{V}{V^2-v^2}=\frac{w^{-1}-w}{4v}.
$$
三个系数依次分解为 (T3)。端点与内部单位性由 $-N\le r\le N$ 和 $p=6k-1$ 逐因子直接得到，未假设一般三对角矩阵在特征 $p$ 中半单。

## 2. 两个不同算子的实际谱

设 R1113 中
$$
\Psi=VU\,S(U^3),\qquad \deg S=N,\qquad \operatorname{lc}S=-1.
$$
完整原核 $J_P$ 的联合谱已给
$$
(D^2-2U)J_P=U(P)^pJ_P,\qquad
\mathscr B J_P=V(P)^pJ_P
\quad(\Psi(P)=0).
$$
在 $W_{\mathscr C}$ 上的准确特征多项式是
$$
\boxed{\ \det(X-\mathscr B|W_{\mathscr C})
      =-X\,S(X^2-v^2).\ }
\tag{T5}
$$
确实，两个 $U=0$ 点的原 $J_P$ 属于 $\mu_3$ 的平凡角色，不进入 $W_{\mathscr C}$。
三个非零二挠点形成一条 $\mu_3$ 轨道，在此角色中给一个 $0$ 本征值。
对每个 $S(\xi)=0$，$V=\pm\sqrt{\xi+v^2}$ 的两条 $\mu_3$ 轨道各给一条本征线。
$S$ 的系数在 $\mathbf F_p$，所以将这些值取 $p$ 次幂只置换根。首一化得到 (T5)。
R1113 已付 $S$ 可分且 $S(-v^2)\ne0$，故 (T5) 的全部根简单。

另一方面，
$$
\mathscr T:=\mathscr B+3\mathscr C=D^3
\quad\text{在同一个 }W_{\mathscr C}\text{ 上为正则幂零。}
\tag{T6}
$$
这里“正则幂零”是指一个长度 $2N+1$ 的 Jordan 块。原 $D\Psi=\delta\ne0$ 说明
$\Psi$ 是 $k(E)/k(E)^p$ 的 $p$-基。$D^p$ 为导子，并在该 $p$-基及 $k(E)^p$ 上为零，因此 $D^p=0$。
所以 $\mathscr T$ 幂零。在 (T1) 中它仍是三对角，只在对角线上增加 $18rv$。
内部上下系数仍全部为单位，首行递推说明每一本征空间至多一维。
于是幂零核一维，得 (T6)。

因此这里同时有一个简单谱算子 $\mathscr B$ 和一个正则幂零算子 $\mathscr B+3\mathscr C$。
二者不可在原短有界条件中互换。

## 3. 原短六阶条件的准确运输

记原
$$
z=\frac{1-V/v}{2},\qquad
F=z^k-h_k,\qquad
h_k=\frac{(1/3)_k}{(2/3)_k}=2^{1-2k}.
$$
R1061/R1076 的完整有界原函数证明给
$$
e=K_4=0
\quad\Longleftrightarrow\quad
\exists G\in k[V],\ \deg G\le k-2,\quad D^6G=F.
\tag{T7}
$$
此处 $h_k$ 是原首个有界原函数余核的精确常数，并非可自由改变的积分常数。

导子给出满射
$$
D:k[V]_{\le2k-1}\longrightarrow W_{\mathscr C},\qquad
P\longmapsto3U^2P',
\tag{T8}
$$
核恰为常数。所有涉及的微分整数小于 $p$，所以没有额外核。
该映射与 $D^3$ 对易。由 (T6)--(T8)，
$$
\boxed{\ 
e=K_4=0
\Longleftrightarrow
D F\in\mathscr T^2\bigl(U^2k[V]_{\le k-3}\bigr).
\ }
\tag{T9}
$$
正向直接微分 (T7)。反向若 $\mathscr T^2H=DF$，由 (T8) 可唯一到常数地取
$G\in k[V]_{\le k-2}$ 使 $DG=H$，于是 $D(D^6G-F)=0$。
括号内是次数至多 $k<p$ 的 $V$ 多项式，所以为常数。
原首个有界原函数的余核在常数 $1$ 上非零，而在 $F$ 上为零。
$D^5G$ 属于原 $U k[V]_{\le k-1}$，故该余核在 $D^6G$ 上亦为零，迫这常数准确为零。
这一步不能由一般函数域原函数的存在性替代。

右端的原向量全部显式：
$$
DF=\frac{3k(-1)^k}{(2v)^k}\,U^2(V-v)^N,
$$
且
$$
U^2(V-v)^N
=\frac1{(2v)^N}\sum_{r=0}^N(-1)^r\binom Nr\,g_r.
\tag{T10}
$$
(T10) 只将 $(V+v)-(V-v)=2v$ 的 $N$ 次幂展开。因此原强迫向量在 $\mathscr C$ 基中恰有一半支撑。
但是 (T9) 中的有界子空间仍是 $U^2k[V]_{\le k-3}$；不得把它扩大为整个 $W_{\mathscr C}$。

## 4. 同一真实三平移保留这个空间

R1095 的原算子为
$$
\mathscr S_Q f=(V+v)^{2k}f(T+Q),\qquad
\gamma=(2v)^{2k},\qquad \mathscr S_Q^3=\gamma^3.
$$
原加法律
$$
U(T+Q)=\frac{-2vU}{V+v},\qquad
V(T+Q)=\frac{v(V-3v)}{V+v}
$$
直接给
$$
\boxed{\ 
\mathscr S_Q(U^2P(V))
=4v^2U^2(V+v)^{2N}
 P\!\left(\frac{v(V-3v)}{V+v}\right).\ }
\tag{T11}
$$
所以 $W_{\mathscr C}$ 被这个实际三平移保持；这次保持性有完整乘子证明。
特别
$$
\begin{aligned}
\mathscr S_Q\{U^2(V-v)^N\}
 &=4v^2(-4v^2)^N U^2(V+v)^N,\\
\mathscr S_Q^2\{U^2(V-v)^N\}
 &=4\gamma v^2(-2v)^N U^m.
\end{aligned}
\tag{T12}
$$
第二行使用 $\mathscr S_Q^2=\gamma(V-v)^{2k}\tau_{-Q}$，并保留全部 $\gamma$。
因此 (T9) 的强迫向量经原三平移准确回到原 $U^m$，不是另选一个抽象本征向量。
但是 $\mathscr S_Q$ 不与 $D^3$ 对易；运输像空间时必须同时运输算子及子空间。
本文尚未把这些完整运输化为原 $\eta_k,\nu_k$ 非同时零。

## 5. 仍待解决的具体接口

当前准确目标是排除 (T9) 的指定包含，或在保留 (T11)--(T12) 的算子和子空间后排除等价包含。
(T5) 的简单谱以及 (T6) 的单 Jordan 块，都不足以单独排除它。

与原短 $\mathscr L=D^3/(-6v)$ 的单项式递推比较时，后者相邻项积是
$$
j(j+1)(3j+1)^2(3j+2)^2.
$$
(T2) 的相邻项积则是 $b_+(r)^2$。二者并非同一矩阵的平凡对角重标。
任何使用简单谱控制原短中间 minor 的论证，都须给出真实的后续变换，不能仅据“两者均为三对角”。

来源：R1061 §§11--14、19；R1076；R1095 §§5、9；R1113 §§1--9。


## 6. 两条真实 Green 端列：端点残项保留

(T2) 是对称矩阵，因为 $b_+(r)=b_-(r+1)$。定义两个有限向量
$$
y^-_{-N+j}=\frac{j!}{(2k+1)_j}\quad(0\le j\le2N),
\qquad y^+_r=y^-_{-r}.
\tag{T13}
$$
它们的每个分量均为单位，且
$$
\frac{y^-_{r+1}}{y^-_r}
 =\frac{r+1/6}{r+1/2},\qquad
\frac{y^+_{r+1}}{y^+_r}
 =\frac{r+1/2}{r+5/6}
\quad(-N\le r<N).
$$
准确的有限矩阵恒等式是
$$
\boxed{\ 
(\mathscr B+v)y^-=-4v\,e_{-N},\qquad
(\mathscr B-v)y^+=4v\,e_N.\ }
\tag{T14}
$$
因此 $(\mathscr B+v)^{-1}e_{-N}=-y^-/(4v)$ 与
$(\mathscr B-v)^{-1}e_N=y^+/(4v)$ 都是全分量单位的实际端列。

证明须保端点，不能把一个先约去分母的 $0\times\infty$ 项设零。
置 $x=6r$，内部递推乘 $4/v$。对第一向量，两个移位项分别化为
$(x+1)^2(x+5)$ 与 $(x-1)(x-3)^2$；其和减去 $2x(x^2+13)$ 恰为 $-4$。
左端 $r=-N$ 的第二个约分后表达式为
$$
\frac v4(x-1)(x-3)^2\big|_{x=5}=4v.
$$
有限矩阵没有此项，所以留出 $-4v e_{-N}$。
右端没有另一残项。对第二向量，两个移位项是
$(x+1)(x+3)^2$ 与 $(x-5)(x-1)^2$，相同差为 $+4$。
在右端 $x=-5$，约分后的第一项为 $-4v$，故有限矩阵的残项是 $+4v e_N$。
这证明 (T14)。

(T5) 也独立给
$$
\det(\mathscr B+v)=-vS(0)=-\frac{\delta}{2v},
\qquad
\det(\mathscr B-v)=vS(0)=\frac{\delta}{2v}.
\tag{T15}
$$
所以 (T14) 的逆算子确实存在，规范一致。

原 $J_1$ 不是这两个端列之一。若
$g_1=J_1-\delta\Psi=\mathscr S_Q\Psi-\delta\Psi\in V_0$，完整三阶 jet 给
$$
(\mathscr B-v)g_1
=3\delta\{UJ_0+V\Psi+\delta U+(v/3)\Psi\}.
\tag{T16}
$$
括号中的最高两项准确相消，属于原 $V_0$ 的相应角色，但其在 $\mathscr C$ 对偶基中的一般项不能删除。
(T14) 并未把 (T16) 的完整强迫向量替换成一个端点向量，也未把 (T9) 的短像问题改成可逆矩阵求解。


## 7. 原全部法向强迫列的闭式单位

以下使用相对 Cartier；底域常数不取 $p$ 次根。设
$$
\varepsilon_r=A(g_r,J_1)
 =D_R(\Phi g_r)(-Q),\qquad
d_r=A(g_r,UJ_0),\qquad -N\le r\le N,
$$
其中 $J_0=J(-Q,\cdot)=(V+v)^{2k}$，$J_1=D_PJ(P,\cdot)|_{P=-Q}$。
特别 $\varepsilon_0=e$ 是原指定第一读数，未改变源 $g_0=U^m$。
置 $\ell=k-r$，则 $1\le\ell\le2k-1$，且 R1113 的原 Miller 规范给
$$
g_r g_Q=F_\ell,\qquad
g_Q=\frac{U}{(V-v)^{2k}},\qquad
F_\ell=\left(\frac{V+v}{V-v}\right)^\ell.
$$
准确地，
$$
\boxed{\quad
d_r=\frac{C_{\rm rel}(UF_\ell\omega)}{\omega'}
 =\gamma\binom{3k-1+r}{2k},
\qquad \gamma=(2v)^{2k}.
\quad}
\tag{T17}
$$
这些 $2N+1$ 个数全部是单位。

先核 $A$ 与相对 Cartier 的同一读数。由
$J_0=U^p g_Q$，
$$
C_{\rm rel}(g_r UJ_0\omega)
 =U'\,C_{\rm rel}(Ug_r g_Q\omega).
$$
$Ug_r\in H=L((p+1)O)$；它的 $\mu_3$ 角色平凡，故其 $\ell_p$ 系数为零。
R1095 的完整 $H$ 公式中，另一第三类系数含 $\Psi(-Q)=0$，也为零。
因此右边的后一 Cartier 值为常数乘 $\omega'$。
前式的 $U'$ 系数正是原 $A(g_r,UJ_0)$，给 (T17) 的第一个等号。
这里没有把超出 $V_0$ 的 $Ug_r$ 默认为旧 $\Phi$ 输入。

这个读数也有完全多项式的独立付款。因 $dV=3U^2\omega$，
$$
UF_\ell\omega
 =\left(\frac1{3U^2}\right)^p
 (V-v)^{4k-1-\ell}(V+v)^{4k-1+\ell}\,dV.
\tag{T18}
$$
分子次数为 $8k-2<2p-1$，只有 $V^{p-1}$ 项被相对 Cartier 读到。
又 $dV'=3U'^2\omega'$，故全部 $3$ 和 $U'$ 标架正好相消。
令 $n=2k-1$、$a=4k-1-\ell=3k-1+r$。于是
$$
d_r
 =v^{2k}[x^{2k}](1-x)^a(1+x)^{p+n-a}
 =v^{2k}[x^{n+1}](1-x)^a(1+x)^{n-a}.
$$
第二等号只消费次数 $n+1<p$，由 $(1+x)^p=1+x^p$ 得到；没有丢掉进入指定系数的项。

对任意整数 $n\ge0$，以 $a$ 为变量，
$[x^{n+1}](1-x)^a(1+x)^{n-a}$ 是次数至多 $n+1$ 的有理多项式。
当 $a=0,\ldots,n$ 时，它为零，因为被读的表达式是次数 $n$ 的多项式。
其最高系数为 $(-2)^{n+1}/(n+1)!$，由
$\log((1-x)/(1+x))=-2x+O(x^3)$ 直接读出。因此
$$
[x^{n+1}](1-x)^a(1+x)^{n-a}
 =(-2)^{n+1}\binom a{n+1}.
\tag{T19}
$$
本题 $n$ 为奇数，且 $n+1<p$，所以这个有理恒等式可以约化，符号为正。
这给 (T17)。最后 $2k\le a\le4k-2<p$，二项式的分子、分母阶乘均小于 $p$，
所以每个 $d_r$ 都是单位。

(T13) 与 (T17) 有特别简单的精确关系：
$$
\boxed{\quad d_r\,y^-_r=\gamma.\quad}
\tag{T20}
$$
确实，写 $r=-N+j$ 后，二项式为
$\binom{2k+j}{2k}=(2k+1)_j/j!$。

## 8. 完整 Green 强迫递推及原中列零时的两邻列

原第三阶核恒等式在 $P=-Q$ 的一次 jet 是
$$
\mathscr B J_1=vJ_1+3\delta UJ_0.
$$
$A$ 的分部积分给 $\mathscr B^*=-\mathscr B$，所以在 (T1) 的实际对称矩阵中，
$$
\boxed{\quad
(\mathscr B+v)(\varepsilon_r)_{r=-N}^N
 =-3\delta(d_r)_{r=-N}^N.
\quad}
\tag{T21}
$$
这个分部积分即使 $UJ_0$ 的极阶超过 $H$ 也成立：把 $A$ 写成局部
$\operatorname{Res}_O(u^p fg\omega)$，$D(u^p)=0$，每个全导数留数为零。
所用右端正是 (T18) 的完整实际读数，未删任何最高偶项。
矩阵方向由 $b_+(r)=b_-(r+1)$ 固定，不额外转置未知系数。

置
$$
z_r=\frac{\varepsilon_r}{y^-_r},\qquad
w_r=b_+(r)y^-_r y^-_{r+1}\quad(-N\le r<N).
$$
全部 $w_r$ 均为单位。由 (T14)、(T20)--(T21) 得
$$
\boxed{\quad
w_r(z_{r+1}-z_r)=3\delta\gamma(N-r)
\quad(-N\le r<N),\qquad
z_{-N}=-\frac{\delta\gamma}{2v}.
\quad}
\tag{T22}
$$
证明保留有限矩阵两个端点。在内部，把 (T21) 的第 $r$ 行乘 $y^-_r$，
得到
$$
w_r(z_{r+1}-z_r)-w_{r-1}(z_r-z_{r-1})=-3\delta\gamma.
$$
右端 $r=N$ 没有 $w_N$ 项，故
$w_{N-1}(z_N-z_{N-1})=3\delta\gamma$。
向左逐行相加给 (T22) 的差分式。左端则必须保留
$(\mathscr B+v)y^-=-4v e_{-N}$，准确给
$$
3\delta\gamma(2N)-4v z_{-N}=-3\delta\gamma.
$$
所以 $z_{-N}=3\delta\gamma(2N+1)/(4v)$。
由 $p=6k-1$、$2N+1=2k-1=-2/3$ 在底域中的等式，得到 (T22)。
这也直接证明原端列 $\varepsilon_{-N}$ 为单位。

特别，若原中列 $e=\varepsilon_0$ 为零，则
$$
\boxed{\quad
\varepsilon_{-1}
 =\frac{4\delta\gamma k}{5v\,y^-_0}\ne0,\qquad
\varepsilon_1
 =\frac{4\delta\gamma N}{5v\,y^-_0}
 =-5\varepsilon_{-1}\ne0.
\quad}
\tag{T23}
$$
这里用 $b_+(-1)=-15v/4$、$b_+(0)=15v/4$，并分别在 (T22) 取 $r=-1,0$。
本题 $p\ge41$，$k,N$ 及所有显式分母都是单位。

(T23) 是两个相邻的原源 $g_{-1},g_1$ 的实际 Picard 一阶读数。
它不把这两个源认成原 $g_0=U^m$ 的四阶读数，也不把它们认成 primitive/Legendre mask 已保留的标签。
原共同零条件仍为 (T7)--(T9)；下一步需要支付 (T22) 与原 $J_4$ 或同一短子空间的准确接口。

root/o1_theta/o2_high_coefficient 独立纸核 §§7–8：同一相对 Cartier/全H边界、唯一指数、系数多项式恒等式、所有单位与Green两端残项均保留；旧 §§1–6 逐字保留。无数学程序执行。


## 9. 全部矩列及原平方读数：保留乘法后的移位

对 $0\le s\le2k-1$、$1\le\ell\le2k-1$，定义同一相对 Cartier 的标量
$$
M_{s,\ell}=\frac{C_{\rm rel}(U^{3s+1}F_\ell\omega)}{\omega'}.
$$
其完整闭式是
$$
\boxed{\quad
M_{s,\ell}=(2v)^{2k+2s}
 \binom{4k-1+s-\ell}{2k+2s}.
\quad}
\tag{T24}
$$
这里的 Cartier 输出确为常数乘 $\omega'$，不先假设高极输入仍属于旧 $\Phi$。
直接把 (T18) 的分子分别再乘 $(V^2-v^2)^s$，得
$$
U^{3s+1}F_\ell\omega
=\left(\frac1{3U^2}\right)^p
 (V-v)^{4k-1+s-\ell}(V+v)^{4k-1+s+\ell}\,dV.
$$
分子次数至多 $12k-4=2p-2$，故仍只读 $V^{p-1}$。
反转系数后被读的次数为 $2k+2s\le p-1$；用 (T19)，其中
$n=2k+2s-1$，便给 (T24)，所有整数分母都小于 $p$。

因二项式上指标非负且严格小于 $p$，
$$
M_{s,\ell}=0
\quad\Longleftrightarrow\quad
\ell>2k-1-s.
$$
所以 $s=0,\ldots,2k-2$ 与 $\ell=1,\ldots,2k-1$ 的方阵是反三角单位阵型：
反对角线上二项式恰为一。最后一行 $s=2k-1$ 则全零。
这明确保留了原高次乘积的最后边界行。

它也可按真正的 Newton 基写为
$$
\frac{M_{s,\ell}}{M_{0,\ell}}
=\frac{(4v^2)^s}{(2k+1)_{2s}}
 \prod_{j=0}^{s-1}\bigl(\ell^2-(4k+j)^2\bigr).
\tag{T25}
$$
这是把二项式商逐项展开，并用 $2k-1=-4k$ 于底域得到的恒等式。
节点依次为 $(2k-1)^2,(2k-2)^2,\ldots$，彼此不同。
它没有将原源改成任意插值多项式。

写原
$$
\mathcal R=U^2R(U^3),\qquad R(X)=\sum_{j=0}^{N}r_jX^j.
$$
原全部一阶列和四阶所需平方列准确是
$$
\boxed{\quad
\varepsilon_{k-\ell}
 =6\ell v\sum_{j=0}^{N}r_jM_{j,\ell},
\qquad
\kappa_\ell:=\frac{C_{\rm rel}(F_\ell\mathcal R^2\omega)}{\omega'}
 =\sum_{i,j=0}^{N}r_ir_jM_{i+j+1,\ell}.
\quad}
\tag{T26}
$$
第一式由 $D\mathcal R=\Psi$、
$DF_\ell=-6\ell vF_\ell/U$ 和
$C_{\rm rel}(d(F_\ell\mathcal R))=0$ 得到。
原核的一阶式给
$C_{\rm rel}(F_\ell\Psi\omega)=\varepsilon_{k-\ell}\omega'$；
其第三类项乘 $\Phi g_{k-\ell}(-Q)=0$，所以这里没有省略非零正规常数。
第二式只把
$\mathcal R^2=\sum r_ir_jU^{3(i+j+1)+1}$
展开，范围 $i+j+1\le2k-1$ 正好全在 (T24) 内。
特别
$$
e=v\sum_{j=0}^{N}r_jM_{j,k},\qquad K_4=\kappa_k.
$$
因为 $M_{s,k}=0$ 当 $s\ge k$，原平方的读数只剩
$i+j\le k-2$；这是已付零行造成的准确截断，不能把余下卷积再删去。
(T24)--(T26) 支付了两次读数的同一完整矩阵，但矩阵的完美性本身仍不排 $e=K_4=0$。

## 10. 原 $\Phi$ 的纯极基对调与目标两 jet 的完整有限和

这一节用原 $O$ 处 additive 参数 $t$，仅消费低于 $p^2$ 的已付整精度。
它不是把整个特征零 logarithm 或 $\zeta^p$ 无条件约化。
在原 j0 模型中
$$
U(t)=t^{-2}+\sum_{d\ge4}(d-1)G_dt^{d-2},
\qquad G_d=0\quad(d\not\equiv0\pmod6).
$$
对 $2\le r\le p-1$ 置
$$
q_r=\frac{(-1)^r}{(r-1)!}D^{r-2}U-(-1)^rG_r,
\qquad p_r=q_r+\frac{G_r}{2}.
$$
当 $r=p-1$ 时这里的 $G_{p-1}=0$ 是 j0 角色给的精确零，
不读取一般曲线的未整高权常数。
逐项微分可见 $q_r=t^{-r}+O(t)$；所以
$1,q_2,\ldots,q_{p-1}$ 是原 $V_0=L((p-1)O)$ 的纯极基。

令 $\mathcal C_r$ 为同一 sigma 规范的 Appell 多项式：
$$
\mathcal C_r(X;U(P),V(P))
=r![t^{r-1}]
 e^{(X-\zeta(P))t}
 \frac{\sigma(P+t)}{\sigma(P)\sigma(t)}.
$$
关于 $X$ 有
$\partial_X\mathcal C_r=r\mathcal C_{r-1}$。
原实际 Miller 核的 $O$ 首项及
$D_T\log K=h_{-FR}(T)+\Psi(R)$
给出其全部安全低 jet
$$
K(T,R)
=t^{p-1}\sum_{j=0}^{p-1}
 \frac{\mathcal C_j(\Psi(R);U(R)^p,V(R)^p)}{j!}\,t^j
 +O(t^{2p-1}).
\tag{T27}
$$
为核 source，取 $A=-FR$，原加法式准确为
$h_A(T)=\zeta(T-A)-\zeta(T)+\zeta(A)$。
因此 $t^p$ 乘上述 Appell 核具有同一对数导数和同一首项。
在次数 $j<p$，系数由除以 $1,\ldots,p-1$ 唯一确定；
可能的 $p$ 次单位歧义从 $j=p$ 才开始，未进入 (T27)。
所需 sigma 权至 $p-1$；其唯一可能危险的末权在 j0 上由 $\mu_6$ 杀掉。
实际 additive 坐标与整 eigen 坐标的首误差在远于 $2p-2$ 的范围，
所以本次首极替换没有 R1079 所警示的高位 carry。

由 $q_r=t^{-r}+O(t)$，相对 Cartier 在 $Z=O$ 的正规常数只读 (T27) 的 $j=r$ 项，得
$$
\Phi(q_r)
=\frac{\mathcal C_r(\Psi;U^p,V^p)}{r!}.
\tag{T28}
$$
这里底域常数保持不动；不能将相对 Cartier 的输出系数再取 $p$ 次根。

在本 j0 模型中，完整有界 primitive 身份为
$$
D^{p-r-1}U
=\frac{\mathcal C_r(\Psi;U^p,V^p)}{r!\delta^{r-1}},
\qquad 2\le r\le p-1.
\tag{T29}
$$
给出两个端点也适用的付款。
用 R1079 的 $\Psi=\zeta_{<p}^{\,p}+\delta t$ 安全负次展开，
Appell 原 sigma 分母使所有 $s\ge2$ 的
$\mathcal C_s(\zeta(t);U(t),V(t))$ 在 $O$ 正规；
唯一负次部分来自 $s=1$。
故 (T29) 右边的极阶至多 $p+1-r$。
误差最低阶至少为 $p^2-p(r-1)>0$，全范围仍安全。
其 $D$ 导数是上一项，起点为已付 $D^{p-2}U=\Psi$。
两边之差只能是常数：它是 $p$ 次幂、只在 $O$ 有低于 $2p$ 的极，而椭圆函数没有单极函数。

奇数 $r$ 的常数由奇偶性杀掉。
偶数 $r$ 满足 $4\le r\le p-3$ 时，R1075 的同权 theta-cycle 证明给
$$
G_{p+1-r}/(r-1)!=-\delta^{1-r}G_r.
$$
两边的权均至 $p-3$，所以该反射包括所有本次非零常数；
两边常数项分别为 $(p-r)!G_{p+1-r}$ 和 $-\delta^{1-r}G_r$。
$r=2$ 用 $G_{p-1}=0$；$r=p-2$ 为奇数且极阶至三；
$r=p-1$ 的极阶至二，常数为 $G_2=G_{p-1}=0$。
故不能只引用此前 Gaussian 写到 $p-3$ 的范围，但这两个 j0 端点确已补齐。

合并 (T28)--(T29)，令
$$
a_r=(-1)^r(p-r)!\delta^{r-1},
$$
得到真正原基上的反对角式
$$
\boxed{\quad
\Phi(q_r)=a_rq_{p+1-r}-G_r,\qquad
\Phi(p_r)=a_rp_{p+1-r}.
\quad}
\tag{T30}
$$
其中 $a_rG_{p+1-r}=-G_r$；非零常数只在偶数 $r$ 出现。
Wilson 给 $a_ra_{p+1-r}=(-1)^r$，与原 $\Phi^2=[-1]^*$ 完全相符。
这不是由维数或同角色猜测的对调。

最后把这一个原变换用于指定源，而不更换目标。
置
$$
c_s=[t^{6s+1}]U(t)^{-1/2},\qquad 0\le s\le N.
$$
在全部负次范围内，
$(t^2U)^m=(t^2U)^{-1/2}$：
两者之商是首项一的 $p$ 次幂，首非恒定项的次数大于 $p-1$。
于是原源恰为
$$
U^m=\sum_{s=0}^{N}c_s q_{p-1-6s}.
$$
差的常数由 $\mu_6$ 角色杀掉。这里所有 $r=p-1-6s\equiv4\pmod6$，
故相应 $G_r$ 全零。
(T29) 给原完整输出
$$
\boxed{\quad
\Phi(U^m)(R)
=\delta^{-1}\sum_{s=0}^{N}c_s\delta^{-6s}D_R^{6s}U(R).
\quad}
\tag{T31}
$$
因此两个真正 Picard 读数准确为
$$
\begin{aligned}
e&=\delta^{-1}\sum_{s=0}^{N}c_s\delta^{-6s}
 D^{6s+1}U(-Q),\\
16ve+4\delta^2K_4
 &=\delta^{-1}\sum_{s=0}^{N}c_s\delta^{-6s}
 D^{6s+4}U(-Q).
\end{aligned}
\tag{T32}
$$
最高微分阶为 $6N+4=p-1$，没有越过 $D^p=0$。
(T32) 保留所有项；$c_0=1$ 或某个端项为单位均不能据此删去其余卷积。
它与 (T26) 是同一原 $e,K_4$ 的两种完整读取，尚未把原短 flag 的共同零排除。

来源与审计：本节 Appell 构造保持 R1116 的同一 sigma 分母，低矩形整性用 R1079；
常数反射用 R1075 的同权证明；原相对 Cartier、$\Phi$、$J_4$ 标架用 R1061、R1095、R1113。
o2_high_coefficient 已独立纸核 (T27)--(T30) 的原 jet、全部阶乘、反射常数及两个 j0 端点；
root 与 o2_high_coefficient 随后逐式核新增 §§9–10 全文，包括移位平方、零末行和指定源两 jet 的完整有限和。
全文没有数学程序执行。


## 11. 后继：完整压缩微分及指定源共轭

新证明见 [R1137](../results/R1137-original-Lame-conjugation-with-complete-boundaries.md)。
它保留 $D_0=D-\Psi\ell_{p-1}$、$\Lambda=\Phi D_0\Phi^{-1}$ 的全部
秩三交换子边界、第四阶 $\delta^4c_N$ 共振，以及原 $U/B/C$ 的完整变换。
同一个 $\phi=\Phi(U^m)$ 准确满足
$$
2\Lambda^3\phi+3\Psi\Lambda^2\phi+6\Phi(V)\phi+3\delta\Psi=0.
$$
$\Lambda$ 仍是原纯极基降阶算子，不能自动当作目标局部微分；
原隐藏的移动 $p$ 重极亦在 R1137 中完整保留。
本节只指向新结果，不重写已经发布的 §§1–10。
