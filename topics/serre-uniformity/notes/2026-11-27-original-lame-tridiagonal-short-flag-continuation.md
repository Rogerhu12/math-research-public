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
