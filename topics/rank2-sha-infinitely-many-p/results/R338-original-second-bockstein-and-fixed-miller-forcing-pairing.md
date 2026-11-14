# R338：原第二 Bockstein 的准确目标与固定 Miller forcing 配对

日期：2026-11-13。**状态：以下第二次提升的良定义目标、整个 canonical 原来源上的高轴作用、两个十三行边界中的准确公式，以及原完整中央下一位对该 forcing 的单个配对均已证明。只固定首核时，二阶目标必须再商掉首 Bockstein 的像。本篇保留这一实际像，不把两条接触尾当作独立列，也未由一个中央聚合式推出全部二阶类消失。**

## 1. 整个已付来源及同一个物理目标

沿用 R334、R335 的
$$
p=6s-1,\quad s>13,\quad 1\le\ell<s-13,\quad L=2s+\ell,
\qquad b=17,\quad p\ne17.
$$
系数环为原惰性位的整数环 $\mathcal O$，剩余域为 $k$。
保留 $w=z^6$、$t=-b/x^3$、$h_7=16t^2+4t+7$、
$a(t)=t(t-1)h_7$ 以及
$$
g=e^{-\kappa w^s}\rho,\qquad a_p=p\kappa\in\mathcal O^\times.
$$
本篇的 $a_p$ 始终是这个实际原常数，与角多项式 $a(t)$ 不同。

对固定 $D\ge2$，令 $\mathcal V_D$ 为 R335 整个原导子
$\mathfrak c_{\le D+40}$ 除去共同 $G_0$ 后的相对来源。
用形式径向变量 $R$ 写，它有准确的整基
$$
\Phi_{n,j}(R,t)=R^n q_n(t)t^j,\qquad
0\le n\le D,\quad 0\le j\le e_{n+1},
\tag{1}
$$
其中
$$
q_n(t)=
\frac{t^{\lfloor(n+1)/4\rfloor}
 (t-1)^{\lfloor(n+1)/3\rfloor}h_7^{\lfloor(n+1)/4\rfloor}}
 {(1+8t)^{\lfloor n/2\rfloor}},
$$
$$
e_m=3\lceil3m/4\rceil+2\lceil m/2\rceil+\lceil2m/3\rceil-2.
$$
每个 $q_n$ 在原点整。相对 Euler 算子
$$\mathcal E=R\partial_R\tag{2}$$
保持整个 $\mathcal V_D$，在 (1) 上准确乘以 $n$。
乘回 $G_0$ 后的原 charge 是 $n+40$；未删除这固定40次。

置
$$
W=\Gamma_L=\mathcal O[w,\epsilon]/
 (w^s-p\epsilon,\epsilon^3,w^\ell\epsilon^2),
\qquad W'=\Gamma_{L+13}.
$$
对 $\Phi\in\mathcal V_D$，记
$$W_i(\Phi)=(\mathcal E^i\Phi)(g,t).$$
实际相对评价 $J=\mathcal J_{\mathrm{can},D}:\mathcal V_D\to W$ 的三块为
$$
\begin{aligned}
J_0&=[W_0]_{<s},\\
J_1&=[a_pW_1+p\mathscr S W_0]_{<s},\\
J_2&=[a_p^2W_2/2+pa_p\mathscr S W_1+p^2\mathscr S^2W_0]_{<\ell}.
\end{aligned}\tag{3}
$$
$\mathscr S$ 是普通 $w$ 系数移去 $s$ 次的算子；它不是一个除以 $p$ 的来源操作。

R328、R335 给出的原完整评价，在一个已付的目标单位下准确为
$$
M=m_{13}J:\mathcal V_D\longrightarrow W',\qquad
J^{\rm orig}=c_*\mathcal U M,\quad c_*\mathcal U\in(W')^\times.
\tag{4}
$$
用 $e_r=w^r/p^{\lfloor r/s\rfloor}$ 表示各自自由整基，则
$$
m_{13}e_r=p^{\delta_r}e_{r+13},\qquad
\delta_r=\lfloor(r+13)/s\rfloor-\lfloor r/s\rfloor\in\{0,1\}.
\tag{5}
$$
$\delta_r=1$ 的两个完整区间是
$$[s-13,s-1],\qquad[2s-13,2s-1].\tag{6}$$
其余行为零指数。记这二十六行在 $W/p$ 中的张成空间为
$\mathcal B_{13}=\ker\bar m_{13}$。整个 $W'$ 始终保留。
因为 $L+13<3s<p$，下文所用原 Gaussian、对数和指数的有限系数都在
R324 已付的整性窗口内。

## 2. 固定模 $p^2$ 核与只固定首核是两个不同目标

先给任意两个有限自由整模之间的映射 $T:V\to Y$ 一个准确的定义。
置
$$
K_r(T)=\ker(T\bmod p^r),\qquad
C_1(T)=\operatorname{coker}(\bar T).
$$
首 Bockstein 为
$$
\beta_1^T:K_1(T)\longrightarrow C_1(T),\qquad
\bar P\longmapsto[T(P)/p]\bmod p.
\tag{7}
$$
当一个 **模 $p^2$ 的核向量本身** $P_2\in K_2(T)$ 已固定时，第二障碍是
$$
\boxed{\widetilde\beta_2^T(P_2)
 =[T(P)/p^2]\bmod p\quad\in C_1(T).}
\tag{8}
$$
这里 $P$ 是 $P_2$ 的任意整提升。更换为 $P+p^2Q$ 只加 $\bar T(\bar Q)$，
所以 (8) 有定义；它为零当且仅当这个指定的 $P_2$ 可提升到模 $p^3$ 的核。

若只固定 $\bar P\in K_1(T)$，则还必须允许更换第一次提升。
准确有短正合列
$$
\boxed{0\longrightarrow K_1(T)
 \xrightarrow{\ \bar Q\mapsto pQ\ }
 K_2(T)\longrightarrow\ker\beta_1^T\longrightarrow0,}
\tag{9}
$$
且
$$\widetilde\beta_2^T(pQ)=\beta_1^T(\bar Q).\tag{10}$$
因此真正落在首核上的二阶微分是
$$
\boxed{
d_2^T:\ker\beta_1^T\longrightarrow
C_2(T):=C_1(T)/\beta_1^T(K_1(T)),\qquad
d_2^T(\bar P)=[\widetilde\beta_2^T(P_2)].}
\tag{11}
$$
它的零准确等价于：存在一个模 $p^2$ 提升及其模 $p^3$ 核提升。
不可以把 (11) 的目标继续写成未经再商的 $C_1(T)$。

**证明。** (7)、(8) 的提升不变性已经说明。
一个首核向量可提升到 $K_2$，当且仅当其首障碍在实际 $\bar T$ 像中，
即 $\beta_1^T=0$。$K_2$ 中约化为零的元素恰为 $pQ$，其条件是
$TQ\in pY$，这给 (9) 及 (10)。两个首次提升之差正是这种 $pQ$，
所以 (11) 良定义。若其类为零，减去适当的 $pQ$ 后使 (8) 为零，
再用一个 $p^2$ 来源修正即可；反向立即成立。$\square$

这些论证分别应用于 $T=J$ 和 **完整原映射** $T=M$。
后者与 (4) 的真实原评价的所有核及障碍通过同一目标单位准确认同。

## 3. 十三行运输后的真正二阶商

由 (5)，原首核是
$$
\boxed{K_1(M)=\{\bar P:\bar J(\bar P)\in\mathcal B_{13}\}.}
\tag{12}
$$
它可以比 $K_1(J)$ 大。若 $J_r(P)$ 表示相对目标第 $r$ 个整坐标，则
对 (12) 中的提升，首障碍的准确代表为
$$
\boxed{
\sum_{\delta_r=0}\overline{J_r(P)/p}\,e_{r+13}
 +\sum_{\delta_r=1}\overline{J_r(P)}\,e_{r+13}
 \quad\bmod\operatorname{im}\bar M.}
\tag{13}
$$
对固定 $P_2\in K_2(M)$，第二障碍则准确为
$$
\boxed{
\sum_{\delta_r=0}\overline{J_r(P)/p^2}\,e_{r+13}
 +\sum_{\delta_r=1}\overline{J_r(P)/p}\,e_{r+13}
 \quad\bmod\operatorname{im}\bar M.}
\tag{14}
$$
式中每次除法都由相应核条件保证整性。这把两个跨界带的不同精度完整列出。

特别有一个用于下文的重要事实：
$$
\boxed{M(P)\in p^2W'\quad\Longrightarrow\quad J(P)\in pW.}
\tag{15}
$$
因为 (5) 至多增加一个 $p$，(15) 对所有列逐坐标成立。

若额外已知 $J(P)\in p^2W$，则 (14) 是
$\bar m_{13}[J(P)/p^2]$，其是否落入 $\operatorname{im}\bar M$，
等价于相对类在
$$W/p\big/(\operatorname{im}\bar J+\mathcal B_{13})\tag{16}$$
中为零。这是固定相对模 $p^2$ 提升的判据。
但是只固定首核时，真正原目标仍是
$$
\boxed{C_2(M)=
\frac{W'/p}
 {\operatorname{im}\bar M+\operatorname{im}\bigl(\beta_1^M:K_1(M)\to C_1(M)\bigr)},}
\tag{17}
$$
其中分母第二项按 (13) 取代表。
它同时允许 (12) 中不属于相对首核的首次修正，不能仅用 (16) 替代。
R331 的单位 Schur 化也须在这一完整整矩阵上进行；所有修正列的高尾仍在 (13)、(14) 中。

## 4. 高轴的准确二阶作用：整个原模与两条耦合尾

写出原轴的唯一低高分解
$$
g=g_<\exp(w^sH),\qquad
g_<=\exp([\log g]_{<s}),\qquad
H=w^{-s}\bigl(\log g-[\log g]_{<s}\bigr).
\tag{18}
$$
$g_<$ 只是同一实际矩阵的计算分解，不是另一条具有中央条件的 theta 来源。
以下记 $J_<$、$M_<$ 为把 (3)、(4) 的相对轴改成 $g_<$ 的辅助矩阵，
$W_i=(\mathcal E^i\Phi)(g_<,t)$。在有限目标中准确有
$$
\boxed{J_g(\Phi)-J_<(\Phi)
 =pH\epsilon J_<(\mathcal E\Phi)
  +\frac{p^2H^2\epsilon^2}{2}J_<(\mathcal E^2\Phi).}
\tag{19}
$$
证明只用 $w^s=p\epsilon$、$\epsilon^3=0$，以及 (2) 对整个来源的保持。
没有把目标乘以 $\epsilon$ 视为来源操作。

**定理1（实际二阶高轴作用）。**

1. $J_g$ 与 $J_<$ 有同一个首核、同一个首 Bockstein，故同一个模 $p^2$ 核及二阶目标。
   $M_g$ 与 $M_<$ 亦然，所指二阶目标是完整的 (17)。
2. 若 $J_<(P)\in p^2W$，则固定模 $p^2$ 提升的第二障碍变化为
$$
\boxed{\widetilde\beta_2^{J_g}(P_2)
-\widetilde\beta_2^{J_<}(P_2)
 =-[H\,\mathcal D(P)]\quad\text{于 }C_1(J),}
\tag{20}
$$
其中同一原 $P$ 给出
$$
\boxed{\mathcal D(P)=
 \left(0, a_p^{-1}[\mathscr S\bar W_0]_{<s},
                   [\mathscr S\bar W_1]_{<\ell}\right).}
\tag{21}
$$
3. 更一般，只要 $M_<(P)\in p^2W'$，则固定 **原** 模 $p^2$ 核的变化仍准确为
$$
\boxed{\widetilde\beta_2^{M_g}(P_2)
-\widetilde\beta_2^{M_<}(P_2)
 =-[\bar m_{13}(H\mathcal D(P))]\quad\text{于 }C_1(M).}
\tag{22}
$$
投到首核上，(20)、(22) 分别再投影到 (11)、(17)，即为真正的二阶微分差。

**证明。** 模 $p$ 的目标有 $w^s=0$。令
$\mathcal E_\epsilon=\epsilon\partial_\epsilon$，则
$$
\epsilon\bar J(\mathcal E P)=a_p^{-1}\mathcal E_\epsilon\bar J(P),\qquad
\epsilon^2\bar J(\mathcal E^2P)
=a_p^{-2}\mathcal E_\epsilon(\mathcal E_\epsilon-1)\bar J(P).
\tag{23}
$$
这个目标 Euler 算子保持所有截断关系。对相对首核，(23) 两式均为零，
所以 (19) 在该首核上属于 $p^2W$；首 Bockstein 不变。
对原首核，$\bar J(P)\in\mathcal B_{13}$，而
$\mathcal E_\epsilon\mathcal B_{13}\subset\mathcal B_{13}$，
$\mathcal E_\epsilon(\mathcal E_\epsilon-1)\mathcal B_{13}=0$。
乘 $\bar m_{13}$ 后也得到首 Bockstein 不变。这证明第一条。

若 $J_<(P)\in p^2W$，则其三块使
$$
\frac{[W_1]_{<s}}p\equiv-a_p^{-1}[\mathscr S W_0]_{<s},\qquad
\frac{[W_2]_{<\ell}}p\equiv-2a_p^{-1}[\mathscr S W_1]_{<\ell}\pmod p.
\tag{24}
$$
又 $\epsilon J_<(\mathcal E P)\in pW$，且
$$
\frac{\epsilon J_<(\mathcal E P)}p
 =\left(0,\frac{[W_1]_{<s}}p,
        a_p\frac{[W_2]_{<\ell}}p+[\mathscr S W_1]_{<\ell}\right)\pmod p
 =-\mathcal D(P).
\tag{25}
$$
(19) 的二次项在除 $p^2$ 后为零：首核已经使
$\epsilon^2\bar J(\mathcal E^2P)=0$。这证明 (20)。

对一般原 $p^2$ 核，(15) 仍保证 $P$ 在相对首核中，故 (25) 的除法整。
(24) 第二式保持完整成立，因为第三块不在 (6) 的跨界带。
第一式在 $w^{s-13}$ 之前成立；其余不确定项仅在第二块的最后十三行。
这部分恰属于 $\mathcal B_{13}$，且乘任何整 $H$ 后仍属于该边界空间或为零。
因此乘 $\bar m_{13}$ 后准确得到 (22)。$\square$

式 (21) 仅取 $P\bmod p$，不取其首次提升；在高轴变化下也不变，
因为两条移尾的变化分别是 $H[W_1]_{<s}$、$H[W_2]_{<\ell}$，由首核消去。
因此 (22) 与允许首次修正的 (17) 相容。

这里两条尾是同一原 $P$ 的 $W_0$ 和 $\mathcal E P$ 的 $W_1$。
$\mathcal E$ 确实保持 (1)，但一般不保持首核：
$W_2$ 在 $\ell\le r<s$ 的行以及 $W_3$ 尚未被首核控制。
所以不能直接把 $\mathcal E P$ 填入 $\beta_1$，也不能将 (21) 的两个多项式自由指定。

还有一个准确的已付窗口：在 (22) 中只需
$$\boxed{H\bmod w^{s-13}.}\tag{26}$$
其余项在第二块落入末十三行，在第三块则超过 $\ell<s-13$，都由
$\bar m_{13}$ 的实际作用消去。这里消去的是指定二阶差，未删除原目标的边界精度。

## 5. 高轴不是任意变量：原 theta 与固定单位给出全部系数

R334 的真实原系数为
$$
\mathcal L(t)=\log\Theta^{17}=\sum\ell_nt^n,\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n},
$$
$$
h(t)=\sum_{n\ge0}\frac{(1/2)_n}{n!(6n+1)}t^n,\qquad z=x^{-1/2}h(t).
$$
定义同一原常数
$$\alpha_p=p\ell_s\in\mathcal O^\times,\qquad
d_p=\ell_s-\kappa(-1/b)^s\in\mathcal O,$$
及固定有理级数
$$
\mathcal T(t)=\sum_{n\ge0}h_n
 \left(1-\frac1{6n+1}+\frac{\mathsf H_{2n}-\mathsf H_n}{3}\right)t^n
 -h(t)\log h(t).
$$
置
$$Q_s(t)=\log(1+8t)+\sum_{1\le n<s}\ell_nt^n.$$
将 R334 的高块先代回 **原** $t=t(w)$，再作普通系数移位，得到
$$
\boxed{\bar H(w)=
\mathscr S\bigl(Q_s(t(w))\bigr)
 +\left(\frac{t(w)}w\right)^s
       \bigl(d_ph(t(w))+\alpha_p\mathcal T(t(w))\bigr)
       \pmod{p,w^s}.}
\tag{27}
$$
第一项保留原低 $t$ 轴在物理 $w$ 轴中产生的所有高系数，不能只留第二项。
$d_p$ 和 $\alpha_p$ 也都是原数据，并非可选的提升参数。

该 forcing 的固定微分描述是
$$
(1+6t\partial_t)\mathcal T
=-(1-t)^{-1/2}\mathcal F,\qquad
\mathcal F=\log h+\frac13\log\frac{1+\sqrt{1-t}}2.
\tag{28}
$$
在原固定双覆盖 $y^2=v^6+b$、$x=v^2$、$v\sim z^{-1}$、$y\sim-z^{-3}$ 上，
$$
\boxed{\mathcal F=\frac13\log\frac{z^3(v^3-y)}2,\qquad
\operatorname{div}(v^3-y)=3(P_+-P_-),\qquad
\mathcal F'_z=1/z-v.}
\tag{29}
$$
它保留整个原椭圆对数 frame $z^3$。将 (27) 代入 (22) 才是这一固定 Miller
forcing 对真实第二 Bockstein 的作用；单独的单位非平凡性不替代该配对。

## 6. 原完整中央下一位恰给一个明确配对

令
$$
\widehat S_< =g_<a(t)/(7b)=w+\cdots,\qquad
c_1=[w^s]\widehat S_<,\qquad
c_{2,<}=[w^{2s}]\widehat S_<.
$$
由 (18)，实际 $\widehat S=g a(t)/(7b)$ 满足
$$
\boxed{[w^s]\widehat S=c_1,\qquad
c_2=[w^{2s}]\widehat S=c_{2,<}+[w^s](H\widehat S_<).}
\tag{30}
$$
没有二次 $H^2$ 项，因为 $\widehat S_<(0)=0$。

R334 已保完整 Newton 尾并证明
$$J'_S(0)\equiv(p/a_p)c_1-(p^2/a_p^2)c_2\pmod{p^3}.$$
因此原完整中央失败首先给 $c_1\equiv0\pmod p$，并进一步准确给
$$
\boxed{[w^s](\bar H\,\overline{\widehat S_<})
 =\overline{a_pc_1/p-c_{2,<}}\quad\text{于 }k.}
\tag{31}
$$
这是与 (22)、(27) 相同的实际高轴的一条配对。
它不是逐权消失；特别没有分别令 $c_1/p$、$c_2$ 或右端两项为零。

(22) 所需的是这个确定高轴与 (21) 两条耦合尾的配对，再投到
整个 canonical 来源的真实 $C_2(M)$。式 (31) 目前只控制与
$\widehat S_<$ 的这一条配对。一个纯粹的参数检查也显示必须使用原确定方程：
在辅助高轴中加 $\tau w^{s-1}$，会以系数一改变 (31) 左端，
却由 (26) 不改变 (22)。这不是另一条实际 theta，也不构成原中央失败的反例；
它准确表明，二阶控制若成立，需从 (27)–(29) 与实际来源像同时推出。

本篇得到的下一指定有限对象因而是
$$
\boxed{\bar P\longmapsto
\pi_2\bar m_{13}\!\left[
\left\{\mathscr S Q_s(t(w))+
(t(w)/w)^s(d_ph+\alpha_p\mathcal T)(t(w))\right\}
\left(0,a_p^{-1}\mathscr S\bar W_0,\mathscr S\bar W_1\right)
\right],}
\tag{32}
$$
其中 $\bar P\in\ker\beta_1^M$，$\pi_2:W'/p\to C_2(M)$，
两条尾按 (21) 截断，全部边界及首次提升像按 (13)、(17) 保留。
要把 (31) 运输为原深关系，尚须证明 (32) 的具体配对身份或其实际像成员性；
没有通过来源归一化、常数主元或一个非零 Miller 单位预付它。

## 固定精确证书

- `scripts/check-jzero-second-bockstein-and-fixed-forcing.py/.json`：
  核有限指数高轴式、两条 Euler 身份、第二接触尾系数、完整边界作用及二阶目标所需的首次提升修正。
  只有固定符号恒等式与一个复合数块长的截断代数检查，不扫描目标素数。

依赖：R324 原整性窗口；R328 完整十三行运输；R331 整 Schur 化；
R334 原中央下一聚合与固定 Miller forcing；R335 整个 canonical 原来源。
