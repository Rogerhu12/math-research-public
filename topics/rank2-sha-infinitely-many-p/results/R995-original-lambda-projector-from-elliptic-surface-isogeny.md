# R995 — 由真实三同源直接构造原最高 $\lambda$ 的自伴 Chow 投影

**2026-11-27 方向更正：** [R1006§11](R1006-actual-full-nine-trace-and-original-katz-square.md)明确区分R804的算术Tate角色与上同调的对偶角色。原算术 $V_j$ 应取 $P_-$；本篇§4/§6据此更正单线标签。严格Chow恒等式、最高双线投影及全部对应自然性不变。

日期：2026-11-26。会话：`Astra-rank2-Sha-0b097461-20261127`。

**状态：已证明。** 对 R991 的实际 $I_9/I_3$ 模曲面 $S$，其真实
degree3 自对应在 $t_2(S)$ 上满足严格的 Chow 关系 $f^2=-3$、
$f^\dagger=-f$。与 $E_{27}$ 的 CM 对应 $g=[\delta]^*$ 配对后，
$$
P_{\rm high}=\frac12\left(1+\frac{f\otimes g}{3}\right)
$$
是一个自伴 Chow 幂等元，恰保留 $(3,0),(0,3)$ 两条最高线。
它可以直接作用在新的实际 CM 图族上，保原全部有限 $\eta_j$ 后
AJ 目标就是原 $\lambda_j$。本篇不要求 $S$ 有有限维 Chow 动机，
不要求 $S$ 到 K3 的 Chow 逆，也不假设 realization 保真。
尚未证明所得投影循环非零或其 AJ 跨 $p$ 非零。

## 1. 固定曲面、实际映射与对应约定

固定
$$
K=\mathbf Q(\omega),\quad \delta=1+2\omega,\quad\delta^2=-3,
\quad E=E_{27}:y_0^2+y_0=x_0^3.
$$
令 $S$ 为下式的光滑相对极小模型：
$$
B:\ v^3=t(1-27t),\qquad
\mathcal E_t:\ y^2+xy+t y=x^3\quad\text{over }B.
\tag{1}
$$
R991 已支付它的模群、全部2/3/17局部型以及
$\rho(S)=12$、$\operatorname{rank}T(S)=2$。
取 Kahn–Murre–Pedrini 的自对偶 refined Chow–Künneth 分解，记
$$
P=\pi_2^{\rm tr}(S),\qquad M=(S,P,0)=t_2(S),
\qquad e=\pi_1(E)=\Delta_E-E\times O-O\times E.
\tag{2}
$$
可在 $K$ 上作(2)；为讨论第7节的下降，也可先取定义于
$\mathbf Q$ 的分解。NS 部分使用所有 Galois 共轭除子及交矩阵的逆，
不需要逐条除子在 $\mathbf Q$ 上定义。

[实际对应注](../notes/2026-11-27-congruence-i9-i3-surface-and-correspondence-scope.md)
已给一个指定的次数3有理映射 $F:S\dashrightarrow S$。
它覆盖 $\iota_B:(t,v)\mapsto(1/27-t,v)$：先以
$\{O,(0,0),(0,-t)\}$ 为核作规范 Vélu 商，得到
$$
\mathcal E'_t:\ y'^2+x'y'+ty'=x'^3-5t x'-t-7t^2,
$$
再在短 Weierstrass 坐标中用
$(u',w')\mapsto(u'/\delta^2,w'/\delta^3)$。
这个几何映射满足
$$
F^2=[-3]_{S/B},\qquad \deg F=3,
\tag{3}
$$
以及在全局二形式
$$
\Omega=\frac{dt}{v^2}\wedge\frac{dx}{2y+x+t}
\quad\text{上}
\quad F^*\Omega=-\delta\Omega.
\tag{4}
$$
(3)是有理映射等式；其右边的纤维次数为9，不能看成恒等。

下文的 $F^*$ 表示图闭包的转置所诱导的 pullback 对应，
$F_*$ 表示图本身的 pushforward 对应。定义
$$
f=P F^*P\in\operatorname{End}(M),\qquad
g=e[\delta]^*e\in\operatorname{End}(h_1(E)).
\tag{5}
$$
$\dagger$ 表示转置及 Poincaré 对偶下的伴随；由于(2)自对偶，
$f^\dagger=PF_*P$。所有断言先在有理 Chow motives 中作，
需要 CM 正线时再把系数扩至包含 $K$ 的固定数域。

## 2. 一般椭圆曲面的纤维乘法在 $t_2$ 上严格等于标量

这里支付从(3)到 Chow 关系的关键一步。

**引理。** 设 $X\to C$ 是特征零域 $k$ 上有截面的光滑射影
椭圆曲面，$[n]_{X/C}$ 表示一般纤维的乘法所给的有理自映射。
对任意整数 $n$，在 $t_2(X)$ 上有
$$
[n]_*=[n]^*=n\,1_{t_2(X)}.
\tag{6}
$$
当 $n=0$ 时解释为映到零截面的对应。

**证明。** 记 $L=k(X)$，$\xi$ 为 $X$ 的一般点；它在基变换到
$L$ 的某个光滑椭圆纤维上给 $L$-点 $P_\xi$，零截面给 $O_\xi$。
椭圆曲线的 divisor-class 与群法同构给严格的 rational equivalence
$$
([n]P_\xi)-n(P_\xi)+(n-1)(O_\xi)=0
\quad\text{在 }\operatorname{CH}_0(X_L).
\tag{7}
$$
它先在该光滑纤维上成立，再推入 $X_L$：左式 degree 为零，
其群法和是 $nP_\xi-nP_\xi=0$，故是主除子。
此论证也包括负 $n$，不是只对正乘法的 cohomology 计算。

令 $r:X\to C\to X$ 是投到基曲线后取零截面的映射。
(7)说明对应
$$
\Gamma_{[n]}-n\Delta_X+(n-1)\Gamma_r
\tag{8}
$$
在第一因子一般点处限制为零。Chow localization 因而说明其类可由
支撑在 $D\times X$、$D\subsetneq X$ 的对应表示。
$\Gamma_r$ 则支撑在 $X\times O(C)$，第二投影不 dominant。

记 $J(X,X)$ 为由这两类非 dominant 对应生成的双边理想。
[KMP, Definition7.4.2、Theorem7.4.3] 给无条件同构
$$
\operatorname{CH}^2(X\times X)_\mathbf Q/J(X,X)
\ \simeq\ \operatorname{End}(t_2(X)),
\tag{9}
$$
映射就是夹上 $\pi_2^{\rm tr}$。将(8)模 $J$，给第一条(6)。
$J$ 在转置下稳定，自对偶 projector 把同一等式转置，给第二条。
证明没有使用 finite-dimensionality 或任意 regulator 的单射性。$\square$

引理的“支撑在曲线上”是对应在某一投影下不 dominant，
并非声称一个曲线本身的零循环都在 $\operatorname{CH}_0(X)$ 中为零。
这一区别对 $q(X)=1$ 的当前曲面是必要的。

## 3. 图复合、异常曲线与 $f^2=-3$

对光滑射影曲面间的 dominant 有理映射 $u$，取图的解消
$$
X\xleftarrow{\ b\ }\widetilde X\xrightarrow{\ a\ }Y,
$$
其中 $b$ 为点吹起的复合，$a$ 为 generically finite morphism。
图对应可写成 $a_*b^*$ 或其转置。更换解消只增加异常曲线产生的
Tate 对应；每一项在源或靶的一侧不 dominant，所以在(9)中为零。

同理，两个图的 correspondence 复合在共同有定义的稠密开集上
就是复合有理映射的图。剩余项的支撑落在被删去的曲线之上，
属于 $J$。因此在 $t_2$ 上，实际有理映射的复合与图对应复合一致。
也可直接用 [KMP, Corollaries7.8.10–7.8.11] 的 birational functoriality；
这里已经指出其在本情形中消掉的是哪些几何项。

应用(3)与引理(6)，得严格 Chow 等式
$$
\boxed{f^2=-3\,1_M.}
\tag{10}
$$
特别 $f$ 可逆，$f^{-1}=-f/3$。
另在同一一般点上，pullback 后 pushforward 的每个几何点按剩余域
次数计数，总次数恰为 $\deg F=3$。异常项仍在 $J$ 中，故
$$
f^\dagger f=3\,1_M.
\tag{11}
$$
把(10)的逆代入(11)，得到
$$
\boxed{f^\dagger=-f.}
\tag{12}
$$
这也给 $ff^\dagger=3$。
本证明没有把一般 generically finite map 的 $F^*F_*$ 冒称为
全 Chow motive 上的 $3\Delta$；这里是在已证明(10)的 $t_2$ 上求逆。

对椭圆曲线 $E$，经典 $h_1$ 上的乘法关系及
$[\delta]^2=[-3]$、$\deg[\delta]=3$ 同样给
$$
\boxed{g^2=-3\,1_{h_1(E)},\qquad g^\dagger=-g.}
\tag{13}
$$
这里 $[\delta]^*\varpi_E=\delta\varpi_E$，其中
$\varpi_E=dx_0/(2y_0+1)$。

## 4. 完整自伴最高投影及 CM 正线

在
$$
N=M\otimes h_1(E)=(S\times E,P\otimes e,0)
$$
上记 $A=f\otimes g$。由(10)、(12)、(13)，
$$
A^2=9,\qquad A^\dagger=A.
\tag{14}
$$
定义
$$
\boxed{
P_{\rm high}=\frac12\left(1_N+\frac A3\right),\qquad
P_{\rm mix}=\frac12\left(1_N-\frac A3\right).
}
\tag{15}
$$
直接由(14)得
$$
P_{\rm high}^2=P_{\rm high},\quad P_{\rm mix}^2=P_{\rm mix},
\quad P_{\rm high}P_{\rm mix}=0,\quad
P_{\rm high}+P_{\rm mix}=1_N,
\tag{16}
$$
且两个 projector 均自伴。这些都是 Chow 对应等式。

为辨别正负，不能只看两个平方均为 $-3$。
由(4)、(13)，在 $T(S)$ 的 $(2,0),(0,2)$ 线上，$f$ 的特征值
分别为 $-\delta,\delta$；在 $H^1(E)$ 的 $(1,0),(0,1)$ 线上，
$g$ 的特征值分别为 $\delta,-\delta$。因此
$$
\begin{array}{c|rrrr}
\text{Hodge型}&(3,0)&(2,1)&(1,2)&(0,3)\\ \hline
A&+3&-3&-3&+3.
\end{array}
\tag{17}
$$
所以(15)的正号恰是最高投影，负号恰是混合投影。

在系数域包含 $K$ 后，给出更精确的单线 projector：
$$
e_S^+=\tfrac12(1-f/\delta),\quad
e_S^-=\tfrac12(1+f/\delta),\qquad
e_E^+=\tfrac12(1+g/\delta),\quad
e_E^-=\tfrac12(1-g/\delta).
\tag{18}
$$
四个都严格幂等，
$$
P_+=e_S^+\otimes e_E^+,\quad
P_-=e_S^-\otimes e_E^-,\qquad
P_{\rm high}=P_++P_-.
\tag{19}
$$
$P_+$ 选 $(3,0)$，$P_-$ 选 $(0,3)$；其转置互换，
不应分别冒称自伴。

为避免把 R804 的 Tate 模帽号与上同调帽号混用，令 $\chi_E$
为 $T_pE$ 上 $[\delta]=\delta$ 一线的算术角色，
$\chi_E\bar\chi_E=\varepsilon_{\rm cyc}$。由 R991 的完整纯实现比较，
$P_+$ 的 étale 实现为 $\chi_E^{-3}$，$P_-$ 为 $\bar\chi_E^{-3}$。
在真正的 $H^3(2)$ 中并施算术 $e_{\eta_j}$ 后，后者给
$V_j=\eta_j^{-1}\chi_E^3\varepsilon_{\rm cyc}^{-1}$，正是 R804 原表示。
这是严格 projector (18)的实现识别；完整 dual 与有限角色的转换见
R1006(52)–(56)，不再用一个未区分约定的帽号替代。

## 5. 它如何实际作用于 CM 图

令 $b=(t_b,v_b)\in B(L)$ 为 R991 新输入的一个非 cusp CM 点，
$L/K$ 为包含全部级点与所需同源的有限扩张。
取具体同源 $\varphi:E_L\to S_b$，令
$$
\Gamma_\varphi=\{(\varphi(Q),Q):Q\in E\}
\subset S\times E,
\qquad Z_\varphi=(P\otimes e)_*[\Gamma_\varphi].
\tag{20}
$$
$Z_\varphi$ 是 codimension2 同调零循环：$P\otimes e$ 仅作用在
$H^3(S\times E)$，因此杀掉原循环的 $H^4$ 类。
定义
$$
\boxed{Z_\varphi^{\rm high}
=\frac12 Z_\varphi+\frac16 A_*Z_\varphi.}
\tag{21}
$$
这里(21)由有限个已指定图、其转置及 Chow projectors 组成，
可以不经 K3 运输而直接构造。

为说明非抽象的几何项，令 $b'=\iota_B(b)$。
在这两个光滑纤维上，$(F\times[\delta])^*[\Gamma_\varphi]$
由实际 fiber-product 曲线
$$
\mathcal C_\varphi=
\left\{(R,Q)\in S_{b'}\times E:
F_{b'}(R)=\varphi([\delta]Q)\right\}
\tag{22}
$$
给出。它向 $E$ 的投影为 degree3；向原图的总次数为9。
在特征零的光滑椭圆纤维上相应同源为 étale，故(22)取其完整
scheme-theoretic cycle；若分成若干图，则必须保留全部分支。
不能随意挑一个三同源逆像。

严格的操作次序是
$$
A_*Z_\varphi
=(P\otimes e)_*\circ(F\times[\delta])^*
\,(P\otimes e)_*[\Gamma_\varphi].
\tag{23}
$$
因而(22)也要对内层 projector 的每项使用；没有擅自假定任意选择
的 $P$ 在全 $h(S)$ 上与 $F^*$ 交换。所有 projector 的修正项都是
有限代数对应，其消去关系由(9)–(16)支付。

对 R991 的三个2阶子群、十八个17阶子群的全部带权和，逐项应用
(20)–(23)。权重、CM 级点域、其上全部 Galois 作用保持原样。
特别 $P_{\rm high}$ 不把该和变成 spherical 向量，也不删除
不合意的 trace 分量。

## 6. 原 finite-character trace 及 AJ 全交换关系

扩大 $L$ 为包含原 $H$ 的有限 Galois 扩张，令 $Z_L$ 是上一节
任一完整带权来源。先取 $\operatorname{Cor}_{L/H}$，再取原
$$
e_{\eta_j}=\frac1{18}\sum_{\sigma\in\operatorname{Gal}(H/K)}
\eta_j(\sigma)^{-1}\sigma.
\tag{24}
$$
$P_-$、$P_{\rm high}$ 和它们的全部几何对应都定义于 $K$，
所以与(24)、restriction、corestriction 严格交换。
于是具体定义
$$
Z_{j,L}^{-}=P_-\,e_{\eta_j}\,\operatorname{Cor}_{L/H}(Z_L)
\tag{25}
$$
（作用在系数扩张后的 Chow 群）。

对任意系数素数 $p$，étale AJ 的对应自然性给交换图
$$
\begin{array}{ccc}
\operatorname{CH}^2(S\times E/H)_{\rm hom}
&\xrightarrow{\ P_-e_{\eta_j}\ }&
\operatorname{CH}^2(S\times E/H)_{\rm hom}\otimes\mathbf Q(\zeta_{18})\\
\operatorname{AJ}_p\downarrow&&\downarrow\operatorname{AJ}_p\\
H^1\!\left(H,H^3_{\rm et}((S\times E)_{\bar K},\mathbf Q_p)(2)\right)
&\xrightarrow{\ P_-e_{\eta_j}\ }&
H^1\!\left(K,V_j\right),
\end{array}
\tag{26}
$$
右下角按 finite-character descent 与固定系数域解释。
更具体地，先取 $H$ 上 $\eta_j$-特征子空间，再用
inflation–restriction 的有限群投影同构；若 $p\mid18$ 则只在有理
系数下使用该写法。这样(26)没有把错误方向的 $\eta_j$ 混入表示。
AJ 的 Tate twist 是 **$(2)$**，因为循环 codimension 为2。

所有对应定义于固定数域且分母固定。因此存在一个固定非零整数
$D$，清除(2)、(15)、(18)、(24)及选定几何模型的分母后，对
$p\nmid D$ 同样得到相应整格上的对应与 projector。
它们与 Galois restriction/corestriction 及 local cohomology
交换；只要输入类属于原 Bloch–Kato $f$/ordinary 条件，其投影仍属于
相同条件，因为这些条件对直接因子的映射自然。
这一步不要求预先知道类非零。

(26)同样适用于 de Rham、Betti 和 syntomic 比较。
因(15)自伴，在任何已定义且对对应自然的高度配对中，有
$$
\langle P_{\rm high}x,y\rangle
=\langle x,P_{\rm high}y\rangle,
\qquad
\langle P_{\rm high}x,P_{\rm mix}y\rangle=0.
\tag{27}
$$
(27)是配对已定义时的形式后果，不声称高度非退化，也不由
总高度非零断言最高高度非零。

## 7. 最高双线投影可下降到 $\mathbf Q$

这一加强不是(25)所必需，但可直接支付。
$S,E$ 均定义于 $\mathbf Q$，Vélu 商也定义于 $\mathbf Q$。
复共轭只把式(1)对应中的 $\delta$ 改成 $-\delta$，所以
$$
F^c=[-1]_{S/B}\circ F.
\tag{28}
$$
由(6)，在 $M$ 上 $f^c=-f$；在 $h_1(E)$ 上同样 $g^c=-g$。
因此
$$
(f\otimes g)^c=f\otimes g
\tag{29}
$$
是严格 Chow 等式。选取定义于 $\mathbf Q$ 的(2)，则
$$
\mathcal A=\tfrac12\operatorname{Cor}_{K/\mathbf Q}(f\otimes g)
\tag{30}
$$
限制到 $K$ 等于 $A$。restriction 在有理 Chow 群上单射，
因为 corestriction 乘回次数2。故
$\mathcal A^2=9$、$\mathcal A^\dagger=\mathcal A$ 已在
$\mathbf Q$ 上成立，(15)的最高双线与混合投影均下降到
$\mathbf Q$。正/负 CM 单线(18)及三个 finite $\eta_j$ 仍在原 $K$
和指定系数域中使用，不把双线下降误读成单线在 $\mathbf Q$ 上定义。

## 8. 本篇究竟替代了哪一步

R991 的局部 test vector 与明确模曲面已经给新的实际图来源。
原先还缺一个可在 Chow 层执行的最高/混合分离；本篇通过
(15)、(21)、(25)把它补成有限对应，不再为此目的要求
$t_2(S)\simeq t_2(\text{某个K3})$ 的双逆。
一般曲面间的 Chow 比较仍是另一问题，并未由本篇解决或使用。

原 $\lambda_j$ 的 $\eta_j$、3处 uniformizer 值、2/17带权和、
ordinary 方向及 $H^3(2)$ 全部保持。
需要继续支付的是：某一个完整来源 $Z_L$ 的
$\operatorname{AJ}_p(Z_{j,L}^{+})$ 实际非零及该结论跨无穷多个 $p$，
或者一条能够直接计算(25)的 reciprocity/nonvanishing 定理。
idempotent 的存在及(27)不提供这两个非零结论。

## 文献

- Bruno Kahn, Jacob P. Murre, Claudio Pedrini, *On the transcendental part of
  the motive of a surface*, in *Algebraic Cycles and Motives*, Vol.2,
  London Mathematical Society Lecture Note Series **344** (2007), 143–202。
  使用 Proposition7.2.1、Proposition7.2.3、Definition7.4.2、
  Theorem7.4.3、Corollaries7.8.10–7.8.11；
  [作者原文 PDF](https://webusers.imj-prg.fr/~bruno.kahn/preprints/surfaces4.pdf)。
  这些曲面 Chow 结果均不假设 Kimura finite-dimensionality。
- [R991](R991-three-cubic-twists-and-explicit-level-nine-toric-input.md)：
  实际模群、同一曲面、三个 cubic twist 的全部有限数据及最高三次扭曲运输。
- [实际 I9/I3 对应注](../notes/2026-11-27-congruence-i9-i3-surface-and-correspondence-scope.md)：
  完整 Vélu 同源、$F^2=[-3]$、$F^*\Omega=-\delta\Omega$。

本篇没有新增数学程序、数值采样或旧运行重算。
