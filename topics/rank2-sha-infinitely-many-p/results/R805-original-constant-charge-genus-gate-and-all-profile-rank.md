# R805 — 原常数 charge 的全分支属门与全部 profile 的同预算秩界

日期：2026-11-15。**状态：以下全参数结论已证明。指定 forcing 的全像成员性与主目标仍开放。**

R743 的属门及其实际两连接秩界曾要求最高 $Y$ 系数的零点只在固定角。
本篇用原常数 charge 的已付形状
$$
F(t,0)=\lambda d^cH(t),\qquad d=1+8t,
$$
去掉这个最高系数假设。最高系数可以有任意真实移动根；其全部极点成本仍计入。

关键是：原曲线正规化上，除 $t=0,1,-1/8,\infty$ 四个纤维外，
$Y$ 的零除子总重数不超过 $z=\deg H$。
结合原二阶方程，准确得到
$$
h\le6g(\widetilde C)+2\deg_tF+10\deg_YF+2z-6.
$$
因此 R782/R792/R797 的全部已分类 profile 均可使用同一实际
$359\kappa/96+o(\kappa)$ 单位秩下界；不再附加最高项 $S$-unit 条件。
这没有把该属门改成 $h\le\kappa+13$，也没有把单位秩当指定类非零。

## 1. 原曲线、角帽与共同范围

取原同一个实际来源
$$
P^{\rm fact}=qt^rF^3\in\overline{\mathcal W}_D,\qquad
q=d^{-C_D}Q,\qquad Q\in k[t,Y],
\tag{1}
$$
其中
$$
p=6s-1>101,\qquad f_D=\lfloor9D/2\rfloor+4<p,\qquad
r\ge1,\quad F(0,1)=0,\quad F_Y(0,1)Q(0,1)\ne0.
$$
$F\in k[t,Y]$ primitive、不可约。
沿 R495 的全部十九个真实角吹起，记其严格变换为 $C$，
$$
a=\deg_tF,\quad b=\deg_YF\ge3,\quad
\kappa=C^2,\quad\chi=-K_XC,\quad
\mathcal N=\mathcal O_C(C).
\tag{2}
$$
原点 $P=(0,1)$ 光滑且未被吹起，$C$ 几何整。
令 $\widetilde C$ 为正规化、$\gamma=g(\widetilde C)$。
原算术亏格仍为
$$
g_C=1+\frac{\kappa-\chi}{2};
$$
后文不把它与 $\gamma$ 混同。

假设已经由同一原来源付出
$$
\boxed{
F(t,0)=\lambda d(t)^cH(t),\quad
\lambda\in k^\times,\quad c\ge0,\quad
H\in k[t]\text{ monic},\quad(H,d)=1,\quad z=\deg H.
}
\tag{3}
$$
$H$ 可以有重根，也可含 $t$；不要求 $H(0)\ne0$。

在原光滑支 $Y=\psi(t)$ 上，保低于首共振的准确接触
$$
\eta_0=\log(g/\psi)=t^hu(t),\qquad
u(0)\ne0,\qquad0<h<s.
\tag{4}
$$
这里的对数仅指原正规局部参数；全局计算使用有理导数。
实际整提升中的 $p\xi$ 不被改选或删除。

所需的 tame 和小次数条件在 (1) 中自动满足。
确实，R467 的整个原来源帽给
$$
d^{C_D}\overline{\mathcal W}_D
\subset k[t,Y]_{\deg_t\le M_D,\ \deg_Y\le D},
\qquad M_D=f_D+C_D.
$$
由 (1) 的乘积次数准确相加，
$$
3a+r+\deg_tQ\le M_D,\qquad3b+\deg_YQ\le D.
\tag{5}
$$
而 $D<p$、$C_D<p/2$，故 $M_D<3p/2$，从而
$$
\boxed{a<p,\qquad b<p.}
\tag{6}
$$
$t:\widetilde C\to\mathbf P^1$ 是次数 $b$ 的可分映射，
其所有几何局部分歧指数小于 $p$，所以 tame。
同理 $Y$ 的映射次数为 $a<p$。
这些是原系数次数的推论，不是另加一般位置假设。

## 2. 常数 charge 精确控制移动零点

可先扩张到代数闭常数域；实际有限矩阵秩、截面维数及所用不等式随后下降。
置
$$
S=\{0,1,-1/8,\infty\}.
$$

**引理 1。** 在 $\widetilde C$ 上，
$$
\boxed{
\sum_{\substack{Q\in\widetilde C\\t(Q)\notin S\\
\operatorname{ord}_QY>0}}\operatorname{ord}_QY
\le z.
}
\tag{7}
$$
此外
$$
\sum_Q\max(0,-\operatorname{ord}_QY)=a.
\tag{8}
$$
因此 $S$ 外 $Y$ 的零点与极点的**不同分支数**总和至多 $z+a$。

**证明。**
对有限 $\alpha\ne-1/8$，仿射平面曲线与 $Y=0$ 的完整局部交数为
$$
I_{(\alpha,0)}(F,Y)
=\dim_k k[[t-\alpha,Y]]/(F,Y)
=\operatorname{ord}_{\alpha}F(t,0)
=\operatorname{ord}_{\alpha}H.
\tag{9}
$$
$F(t,0)\not\equiv0$，所以这个交数有限。

即使原点 $(\alpha,0)$ 是奇点，(9) 也等于正规化上所有经过该点的
$\operatorname{ord}_QY$ 之和。
一种直接核法是将原一维局部环嵌入其有限正规化：
商为有限长度模，乘 $Y$ 在该商上的核与余核长度相等；
由相应商序列，原环模 $Y$ 与正规化模 $Y$ 的长度相等。
正规化的每个 DVR 给出的长度正是 $\operatorname{ord}_QY$。
这保留所有奇支和交点重数，不将一个分裂纤维认成一个简单点。

在 $\alpha\notin S$ 求和便得 (7)。
可能出现在 $H$ 的 $0,1$ 根只使这个上界更宽，不需删掉这些合法 $H$。

(8) 是非恒定有理函数 $Y$ 的极除子次数：
$[k(C):k(Y)]=\deg_tF=a$。
这里 $Y$ 非恒定：否则几何整性会使 $F$ 为一次水平因子，与 $b\ge3$ 矛盾。
最后每个零、极分支的非零阶至少为1，所以分支数受 (7)、(8) 控制。
证毕。

引理 1 对最高系数 $f_b(t)$ 没有任何零点位置限制。
其所有移动极点已经完整保存在 (8)，并会进入下面的极预算。

## 3. 原 ODE 在所有正规分支上的准确极帽

沿用同一个原 Euler 导数和 forcing：
$$
\delta=t\frac{d}{dt},\qquad
V=\frac{t}{Y}\frac{dY}{dt},
$$
$$
\mathcal F_F=
\mathcal R-\{6(1-t)\delta-(1+2t)\}V,\qquad
\mathcal R=\frac{t(154+160t+1792t^2)}{3(1+8t)^2}.
\tag{10}
$$
$V,\mathcal F_F$ 是 $k(C)$ 中的有理函数；不使用全局 $\log Y$。

令 $e_Q$ 为 $t$ 在某个正规分支 $Q$ 的分歧指数。
对 $t(Q)=\alpha\notin S$，可选 tame 参数 $v$ 使
$t-\alpha=v^{e_Q}$。

若 $Y(Q)$ 有限非零、$e_Q=1$，则 (10) 正则。
若 $Y(Q)$ 有限非零、$e_Q\ge2$，则
$$
\operatorname{pole}_Q V\le e_Q-1,\qquad
\operatorname{pole}_Q\delta V\le2e_Q-1
\le3(e_Q-1).
\tag{11}
$$
若 $Y$ 在 $Q$ 为零或极，写 $Y=v^mU(v)$，
$m\ne0$、$U(0)\ne0$。无论 $m$ 正负，
$dY/Y=m\,dv/v+dU/U$，故
$$
\operatorname{pole}_Q V\le e_Q,\qquad
\operatorname{pole}_Q\mathcal F_F\le2e_Q
\le3(e_Q-1)+2.
\tag{12}
$$
因此原移动根不需要被当成新的整个特殊纤维：
每个零、极分支只加两份极成本。
若正特征使某个导数首项消失，极阶只会下降，(11)、(12) 仍成立。

固定四个纤维逐支计算为
$$
\begin{array}{c|cccc}
t(Q)&0&1&-1/8&\infty\\ \hline
\operatorname{pole}_Q\mathcal F_F\text{ 上界}
&0&e_Q&2e_Q&e_Q .
\end{array}
\tag{13}
$$
在 $0,\infty$，$t/(dt/dv)$ 是 $v$ 乘单位，
故 $V$ 与 $\delta V$ 正则；无穷远系数至多再添 $e_Q$。
在 $1$，$1-t$ 支付一次 $e_Q$ 的导数极。
在 $d=0$，原 $\mathcal R$ 的双极和导数都由 $2e_Q$ 覆盖。
这些估计同时允许 $Y$ 的零、极、原十九角的高重数和原曲线的奇点。

每个完整纤维满足 $\sum_{Q\mid\alpha}e_Q=b$，
所以 (13) 的全部贡献至多 $4b$。
在 $S$ 外应用 (11)、(12)、引理1，再用 tame Riemann–Hurwitz
$$
\sum_Q(e_Q-1)=2\gamma-2+2b,
$$
得到
$$
\boxed{
\deg(\mathcal F_F)_\infty
\le3(2\gamma-2+2b)+2(a+z)+4b
=6\gamma+2a+10b+2z-6.
}
\tag{14}
$$
总分歧和允许包含已经单算的固定纤维，这是合法上界。
也可在实际计算中从分歧和扣除这些已知纤维，得到更强的有限界；
本篇不预付它们的未知分支数据。

## 4. 全 profile 的正规化属门

R467/R507 的原低轴方程在 (4) 的真实长度内给
$$
\boxed{
\mathcal F_F
=h(6h-1)u(0)t^h+O(t^{h+1}).
}
\tag{15}
$$
$p=6s-1$、$0<h<s$ 保 $h(6h-1)\ne0$。
所以 $\mathcal F_F$ 非零，其在原 $P$ 的零阶准确为 $h$。
一个非零有理函数的全零、极次数相等，由 (14) 得：

**定理 1。**
$$
\boxed{
h\le6\gamma+2a+10b+2z-6,\qquad
\gamma\ge
G_F^{(0)}:=
\max\left\{0,
\left\lceil\frac{h-2a-10b-2z+6}{6}\right\rceil\right\}.
}
\tag{16}
$$

这是目标素数 $p$ 内的结论。
没有使用辅助素数或有理子式的跨 $p$ 单位，
也没有将原 ODE 延长到首共振 $s$ 以外。

其原来源范围如下：

- R782、R792 的 $q(t,0)\ne0$ 分支，包括 $r=2,3,4$，均有 $H=1,z=0$；
- R797 的 $r=2,q(t,0)=0$ 全部六十四格有 $z\le2$，允许 $H(0)=0$；
- 对 $r\ge3,q(t,0)=0$ 的其他分支，只要已由原分类付出 (3)，便用其**实际** $z$ 代入 (16)。本定理不替这些分支新定一个未证明的 $z$ 上界。

最高 $Y$ 系数的全部移动根都被允许。
因此无需再核 R743 的最高系数固定角假设。
对于 $z\le2,b\ge3$，新有限属界相较 R743 的
$h\le6\gamma+2a+14b-6$ 还少了 $4b-2z$ 的显示线性成本。

## 5. 接回同一个实际两连接，不扩大来源

保原 $\mathcal H_j=H^0(X,\mathcal O_X(jC))$、同一个 $\eta$，
以及 R550 的两个真实连接
$$
\alpha_\eta:
H^0(C,\mathcal N^2(-hP))
\longrightarrow\operatorname{coker}E_{T-h},
$$
$$
\beta_\eta:
H^0(C,\mathcal N^3(-TP))
\longrightarrow\operatorname{coker}E_{\rm mir},
$$
$$
a_\eta=\dim\ker\alpha_\eta,\qquad
b_\eta=\dim\ker\beta_\eta.
\tag{17}
$$
使用强窗
$$
h>\kappa,\qquad T-h>\kappa,\qquad T\le2h,
$$
并严格区分
$$
\boxed{T=T_J=s-r\quad\text{或}\quad T=T_M=s-r-13.}
\tag{18}
$$
完整 $M$ 的两个十三行不能从 (18) 删掉。

为给有限有效界，引用 R743 引理2的纯曲线函数
$\mathcal C(G,d,A)$。
它不使用最高系数假设：对 $d<0$ 取0、$d=0$ 取1；
对 $0<d<p$，设
$$
\pi(E,r)=\sum_{j\ge1}(E-1-j(r-1))_+,
$$
$$
\mathcal C(G,d,A)=1+\max\left(
\{0,1\}\cup
\left\{r:2\le r\le d,\
\exists\,1\le\nu\le\lfloor d/r\rfloor,\
G\le\nu\pi(\lfloor d/\nu\rfloor,r)+(\nu-1)(A-1)
\right\}\right).
\tag{19}
$$
该引理在 $k(C)=k(t,Y)$、$\deg t=b,\deg Y=a$ 上给
$$
h^0(C,\mathscr L)\le\mathcal C(G,d,a+b)
\quad(\deg\mathscr L=d,\ \gamma\ge G).
$$
其正规化、primitive $t+cY$、可能的复合次数 $\nu$ 与
正特征 Castelnuovo–Severi 均保留；没有用一般位置或把算术属代入正规化属。
(6) 与 $d<p$ 保原可分门。

令
$$
d_\alpha=h-\kappa-\chi,\qquad
d_\beta=T-2\kappa-\chi.
$$
两者非负时均小于 $p$，因为 $h<T<p$。
Riemann–Roch 与 (16)、(19) 因而给：

**定理 2。** 对上述全部原 profile 的同一个实际来源，
$$
\boxed{
\begin{aligned}
a_\eta&\le
\frac{3\kappa+\chi-2h}{2}
+\mathcal C(G_F^{(0)},d_\alpha,a+b),\\
b_\eta&\le
\frac{5\kappa+\chi-2T}{2}
+\mathcal C(G_F^{(0)},d_\beta,a+b).
\end{aligned}}
\tag{20}
$$
若相应原线束负度，直接取其无截面结论；并可取既有 Clifford 界的较小者。
(20) 没有把连接核等同其定义域。

R495 的整返回仍给同预算全部
$qt^r\mathcal H_3\subset\overline{\mathcal W}_D$。
R550 的准确像秩公式也完全不变：
$$
\dim\varepsilon(F\mathcal H_2+e\mathcal H_2)
=\frac{7\kappa+3\chi}{2}-a_\eta,
$$
$$
\dim\varepsilon(\mathcal H_3)
=\frac{9\kappa+3\chi}{2}-a_\eta-b_\eta.
\tag{21}
$$
这里 $e=\mathcal EF$，$\varepsilon$ 是同一个原物理双输出评价，
不是自由环境矩阵。

## 6. 全部已分类 profile 的准确临界主阶

若一个实际候选族满足
$$
\frac h\kappa\to\frac98,\qquad
\frac T\kappa\to\frac94,\qquad
a+b+z=o(\kappa),\qquad\chi=o(\kappa),
\tag{22}
$$
则 (16) 给
$$
G_F^{(0)}\ge\frac{3}{16}\kappa+o(\kappa).
$$
例如原 $D=3b+O(1)$、
$\kappa=47b^2/12+O(b)$、$a=O(b)$、固定 $z$ 的全部已分类格均满足这些线性成本条件，
只要它们确实具有 (22) 的原接触；这里不制造强接触因子。

R743 的全部复合线系优化只用这个属下界，
所以原两临界数保持
$$
\mathcal C(G_F^{(0)},d_\alpha,a+b)
\le\frac{\kappa}{32}+o(\kappa),
$$
$$
\mathcal C(G_F^{(0)},d_\beta,a+b)
\le\frac{5\kappa}{48}+o(\kappa).
$$
于是
$$
\boxed{
a_\eta\le\frac{13\kappa}{32}+o(\kappa),\qquad
b_\eta\le\frac{17\kappa}{48}+o(\kappa),
}
\tag{23}
$$
以及真正原整矩阵的单位秩下界
$$
\boxed{
\dim\varepsilon(F\mathcal H_2+e\mathcal H_2)
\ge\frac{99\kappa}{32}+o(\kappa),\qquad
\dim\varepsilon(\mathcal H_3)
\ge\frac{359\kappa}{96}+o(\kappa).
}
\tag{24}
$$

(23)、(24) 的常数与 R743 相同；
新增的是对全部实际 profile 的适用性，以及 (16) 的较强有限线性项。
没有把两个相交单位块相加。
原完整 $\mathcal W_D$ 包含这个同预算块，但其指定 forcing 是否在全像内，
仍不能只靠 (24) 判定。

## 7. 对指定同 R 问题的边界

本篇不声称 $h\le\kappa+13$。
一般 $t$-分歧仍产生 (11) 的真实极成本，(16) 的主项仍是 $6\gamma$；
原临界 $\gamma$ 可以是 $\kappa$ 量级，不能由此排掉全部强接触。

R790 的指定配对仍须同时保
$$
3\mathcal B(K_0-2K_1-K_2),\qquad
-\mu(a^{-1}t^hQ\mathcal H^{-1}V^3),\qquad
-\langle\nu,\beta_{\mathsf C}(\bar G)\rangle.
$$
本篇没有将第三项设零，也没有将原常数 charge 的形状误认成
首 Bockstein 的自动提升。
R750 的完整主部像、R771 的 trace 补偿、全部非 $F^2$ 列与原同一个 $R$
继续保留。

原 $P_{134}/U_0$、低行右逆高尾、两条十三行 carry、
$P_2=P^{\rm fact}+pR$ 及真正下一位 $d_2/G_2$ 均不改变。
这些全来源条件仍是接下来判定指定余类的实际对象。

依赖：
[R467](R467-tame-branch-contact-and-all-factor-degree-barrier.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[R743](R743-normalization-genus-and-actual-two-kernel-rank-improvement.md)；
[R790](R790-original-cube-full-forcing-and-factor-contact-bockstein-pairing.md)；
[R792](R792-original-nonzero-constant-charge-classification-and-cubic-extension.md)；
[R797](R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)。

本篇为全参数原曲线证明，不新增有限素数扫描或可复算输出数据。