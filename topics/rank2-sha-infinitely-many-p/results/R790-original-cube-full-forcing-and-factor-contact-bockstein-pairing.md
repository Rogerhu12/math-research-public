# R790 — 同一原 cube 的全首次 forcing、因子接触 Bockstein 与全余列转置
> 完整范围增补：[移动常数项与两个原短块长度](../notes/2026-11-15-r790-moving-factor-and-two-short-blocks.md) 已将本篇接到原 q=Yq°、G(t,0)=H(t)（允许H(0)=0）和ell=1,2；保整个原q，因子真截面格为H⁰(X,O(C))，ell=2多保第三余行与全左对τ。本文旧式仍为其ell=1、H=1特例。

日期：2026-11-15。**状态：下述原完整 $p^2$ 接口已证明；显示全余列矩阵的指定成员性、原 $p^3$ 同修正类及主目标仍开。**

本篇保原 $P^{\rm fact}$，不先把 $q(t,Y)$ 投影成 scalar，也不替换原修正 $R$。在 R782 的实际 $r=2$ 范围，完整首 forcing 只读首共振前的原有理 Taylor 前缀：其中 $\xi$ 精确成为同一因子接触矩阵的第一 $p$-Hensel 缺陷。原整个 $\mathcal W_D$ 的首次修正于是是一个显示的非齐次双输出矩阵加原第三单位行。

这也给实际转置：每个杀全部余列的真左对，都诱导同一因子接触矩阵的真左行；原 forcing 配对等于固定主部项、显式 carry 项和该因子首 Bockstein 的配对。没有假设这个左行可提升，也没有把因子的 Hensel 缺陷删掉。

## 1. 同一个候选与原精确低轴

保 R782/R787 的原数据
$$
p=12h+11=6s-1>101,\qquad s=2h+2,\qquad
r=2,\ \ell=1,\ k_{\rm carry}=0,\qquad f_D<p,
$$
$$
P^{\rm fact}=qt^2F^3\in\mathcal W_D,\qquad
m_F=3,\quad m_q=0,\quad b_0=3,\quad D\ge3b.
\tag{1}
$$
取同一个合法整因子提升，并按 R782 归一
$$
F(t,0)=\lambda d^c,\qquad
G=F/(\lambda d^c),\qquad G(t,0)=1,\qquad
\mathfrak q(t,Y)=\lambda^3d^{3c}q(t,Y).
$$
则原来源**准确仍为**
$$
\boxed{P^{\rm fact}=t^2\mathfrak q(t,Y)G(t,Y)^3.}
\tag{2}
$$
$\mathfrak q$ 可含 $Y$，未改成其常数 charge。
本文的原非空候选保精确接触 $h$；只假设接触至少 $h$ 时，下列公式仍成立，但所称第三单位须另有 $V(0)\ne0$。R788 已排原 $b=3$ 的强窗；本文条件公式可保 $b\ge3$，实际剩余强候选须 $b\ge4$。

置
$$
N=s-13=2h-11,\qquad L=N-h=h-11>0.
\tag{3}
$$
原 R434/R687 的非共振有理前缀是
$$
\boxed{
\rho(t)=d(t)\exp\left(\sum_{n\ge1}\ell_nt^n\right),
\qquad
\ell_n=\frac{17}{3n}\frac{(1/3)_n}{(5/6)_n},
\qquad d=1+8t.
}
\tag{4}
$$
在 $t^{<s}$ 中它准确等于原 regularized $g$，不是只模 $p$ 相同。
$n<s$ 时，(4) 的所有分母和形成此前缀所需的阶乘在 $p$ 处为单位；故这段可按同一有理数读取模 $p^2$ 或更高精度。

用旧角 $t$ 记
$$
\mathcal H(t)=
\sum_{n\ge0}\frac{\binom{2n}{n}}{4^n(6n+1)}t^n.
$$
R687 的准确换参为
$$
w=-t\mathcal H(t)^6,\qquad
b_s=(t/w)^s=(-1)^s\mathcal H^{-6s}.
\tag{5}
$$
这里 $s=2h+2$ 为偶数，$6s=p+1$，所以在本篇实际 $<L<p$ 的整前缀中
$$
\boxed{\bar b_s=\mathcal H^{-1}\pmod{t^L}.}
\tag{6}
$$
证明只需在这个 $p$-整截断环中用
$\bar{\mathcal H}^{\,p}\equiv1\pmod{t^L}$。
(6) 不删除 R687 全目标中的 $H^{-p}$；这里只读取其确实低于 $p$ 的指定前缀。

## 2. 两段接触数据与真实 p-Hensel 缺陷

定义全部来自同一 $G$ 的数据：
$$
\boxed{
\begin{aligned}
e(t)&=(\mathcal E\bar G)(t,\bar\rho(t))\pmod{t^L},\\
V(t)&=t^{-h}\bar G(t,\bar\rho(t))\pmod{t^L},\\
Q(t)&=\bar{\mathfrak q}(t,\bar\rho(t))\pmod{t^L},\\
B_h(t)&=
\overline{\frac{\pi_{<h}G(t,\rho(t))}{p}}
\in k[t]/t^h .
\end{aligned}}
\tag{7}
$$
其中 $\mathcal E=Y\partial_Y$。
$V$ 的除法在先验证 $\bar G(t,\bar\rho)\in t^h$ 后才作；
$B_h$ 的除法先在原整环中作，因其整个 $\pi_{<h}$ 前缀可除 $p$。
不能对其余未整除的高系数一起除 $p$。
在精确接触 $h$ 下
$$
e_0=e(0)\ne0,\qquad V_0=V(0)\ne0,\qquad Q_0=Q(0)\ne0.
\tag{8}
$$

令 $Y=\psi(t)$ 为同一个整因子的原光滑支，
$$
\eta=\log(g/\psi)=\eta_0+p\xi,\qquad
\eta_0=t^hu,\quad u(0)\ne0.
$$
可取 $\eta_0$ 的严格 $<h$ 前缀为零；原其余规范和整高尾保持。

**引理 1。** 在本篇全部可读位置，
$$
\boxed{u=V/e\pmod{t^L},\qquad
e\,\xi=B_h\pmod{t^{L-2}}.}
\tag{9}
$$
因 $t^2\xi$ 才进入指定目标，第二式的长度已足够。
更强的第二式在 $t^{<h}$ 上成立，只需将 $e$ 也读到该长度。

**证明。** $\psi\equiv\rho\pmod{p,t^h}$，所以
$(\mathcal EG)(t,\psi)$ 与 (7) 的 $e$ 在 $<h$ 中相同。
在原 logarithmic normal 坐标展开
$$
G(t,\psi e^\eta)=e\eta+\frac{f_2}{2}\eta^2+\cdots .
$$
模 $p$ 后，$\eta_0^2$ 从 $2h$ 起；
$V$ 最后读取的位置为 $h+L-1=2h-12<2h$，
故 $V=eu$。
另一方面，在严格 $<h$ 的原整前缀中，
$\eta_0$ 为零，$\eta=p\xi$；
模 $p^2$ 后仅 $pe\xi$ 留下。
由 (4) 这段 $g$ 就是同一个 $\rho$，所以除 $p$ 得 $B_h=e\xi$。$\square$

这一步不用 R676 的高 CM 分子，也没有重选 $\xi$。
它识别的是原给定因子提升的实际低位缺陷。

## 3. 完整首 forcing 只用 (7)

仍用原
$$
M=c_*U_0w^{13}J,\qquad
\Gamma^+=\mathcal O[w,\epsilon]/
(w^s-p\epsilon,\epsilon^3,w^{14}\epsilon^2),
\qquad t^s=p\epsilon b_s,
\tag{10}
$$
及同一个 Gaussian 单位 $a\in\mathcal O^\times$。
所有共同 charge 和 $P_{134}$ 保原运输。
前两块只在合法的 $w^{13}$ 后行读取成长度 $N$ 的 $t$ jet；
第三块始终保其原物理 $w$。

**定理 1。** 原 (2) 已在相对首核 $\ker\bar J$，
两条十三行门均已通过。它的整个首 Bockstein 在上述原坐标中为
$$
\boxed{
\widehat\beta_0=0,
\qquad
\widehat\beta_1=
t^hQ(t)\left\{
\mathcal H(t)^{-1}V(t)^3+
6at^2e(t)V(t)B_h(t)
\right\}\pmod{t^N},
}
\tag{11}
$$
$$
\boxed{
\left[(c_*U_0)^{-1}M(P^{\rm fact})/p\right]^{(2)}
=3aQ_0e_0V_0^2\,w^{13}\pmod{w^{14}}.
}
\tag{12}
$$
前两块最初十三行以及第三块的 $w^{<13}$ 行全为零。
(12) 在 (8) 下是原真实单位行。

**证明。** 原 $G^3$ 的普通、第一和第二 Gaussian 部分分别从
$3h+2$、$2h+2=s$、$h+2$ 起，故全相对首核门成立。

R755 的完整展开，在当前 $d_0=2$ 和 $r=2$ 下给
$$
\widehat\beta_1
=e^3\mathfrak q_C\,t^hu
(b_su^2+6at^2\xi)\pmod{t^N}.
\tag{13}
$$
其 $C_4$ 项至少从 $2h$ 起，超过 $N$；
这包括 $\mathcal E\mathfrak q$，所以这里没有假设 $\mathfrak q$ 为 scalar。
第三块中 native $\xi$ 项至少两阶，
$C_4t^{h-2}$ 至少 $h$ 阶，只有
$3aw^{13}b_s\mathfrak q_Ce^3u^2$ 的常数留下。
普通低块为零，且 R755 的同一目标读取给上述所有最初十三行零。

在 $<L<h$ 中可将 $\mathfrak q_C,e_C$ 换成在 $\rho$ 上的值。
代入 (6)、(9)，
$e^3u^3=V^3$、
$e^3u\xi=eVB_h$，
得到 (11)。
第三块用 $b_s(0)=1$ 和 $e^3u^2=eV^2$ 得 (12)。
完整 $w^{13}$ 没有被 $t^{13}$ 替换。$\square$

因此整个 (11)–(12) 只需：

- (4) 的 $<N<s$ 前缀模 $p$；
- 其中 $<h$ 前缀模 $p^2$；
- 同一个原因子、余因子及 $a\bmod p$。

这只是该 cube 的**第一** forcing 的输入界。
不能把它外推成任意 $R$ 的 $M\bmod p^3$ 输入界。

## 4. 原整个 W_D 的准确首次修正矩阵

保所有原列
$$
\Phi_{n,j}=Y^nq_n(t)t^j,\qquad
0\le n\le D,\quad0\le j\le e_{n+1}.
$$
令
$$
c_i(n,j)=[t^{\,i-j}]q_n(t)\bar\rho(t)^n,\qquad0\le i<N.
\tag{14}
$$
负次数按零。逆共同 Gaussian 三角单位，并分别除原 $a,a^2/2$ 后，
原 $\bar M$ 在其实际 $w^{13}$ 像上的完整矩阵为
$$
\boxed{
\mathsf A_{D,N}(\Phi_{n,j})=
\left((c_i(n,j))_{i<N},\
(nc_i(n,j))_{i<N},\
n^2q_n(0)\mathbf1_{j=0}\right).
}
\tag{15}
$$
这不是另造来源：每个 $q_n,e_{n+1}$、所有高系数均为原列。
$\bar M$ 中 $g$ 的 $t^{\ge s}$ 部分带原 carry 因子 $p$，不进入 (15)。
共同 charge 的居中在整个目标上是原三角单位；
对 (11)–(12)，其额外混合项也因 $\widehat\beta_0=0$、
$\widehat\beta_1\in t^h$ 而不改变指定右端。

置
$$
\boxed{
\mathcal B=\frac{Q_0e_0V_0^2}{a}\in k^\times,
\qquad
T_{\rm nor}(t)=
\frac{t^hQ}{a}
\left(\mathcal H^{-1}V^3+6at^2eVB_h\right)
\pmod{t^N}.
}
\tag{16}
$$
于是对同一个原来源修正 $R$，准确有
$$
\boxed{
M(P^{\rm fact}+pR)\in p^2\Gamma^+
\ \Longleftrightarrow\
\mathsf A_{D,N}(R)=(0,-T_{\rm nor},-6\mathcal B).
}
\tag{17}
$$

这里没有免费逆整 $m_{13}$：
定理 1 已先证明 forcing 的全部不可除行是零；
原 $\bar M$ 的像本来就在显示的 $w^{13}$ 子空间内，
在这个共同子空间选坐标才得到 (15)。
两条十三行生成的实际 carry 已完整出现在 (11)、(12)。

## 5. 去掉已付三常数行后，仍保全部非 F² 余列

原 $t=0$ 只允许 $n=0,1,2$。三常数行的单位矩阵直接给
$$
R(0,Y)=-3\mathcal B(Y-1)^2.
\tag{18}
$$
用 R771 的真实原列
$$
\boxed{
Q_2=1-2Y-(1+9t)Y^2q_2
=(Y-1)^2-\frac{9t^2Y^2}{d},
\qquad q_2=(t-1)/d.
}
\tag{19}
$$
则每个可能的同 $R$ 准确写成
$$
R=-3\mathcal BQ_2+Z,\qquad
Z\in W_D^{(1)}
:=\overline{\mathcal W}_D\cap t\,k[t,Y,d^{-1}].
\tag{20}
$$
这个真实子格的完整基为：

- $n=0,1,2$ 的原列，仅取 $1\le j\le e_{n+1}$；
- 所有 $n\ge3$ 的原列，仍取 $0\le j\le e_{n+1}$。

没有先取 $F$ 或 $F^2$ 整除子格。
第三常数行已由 (19) 支付，余下准确的全矩阵为
$$
\mathsf B_{D,N}(Z)=
\left(Z(t,\bar\rho)\bmod t^N,\
(\mathcal EZ)(t,\bar\rho)\bmod t^N\right).
$$
其两条常数行都为零，可在 $t\,k[t]/t^N$ 上读取。

**定理 2。** 原完整首次提升 (17) 等价于
$$
\boxed{
\mathsf B_{D,N}(Z)=
\left(
3\mathcal BQ_2(t,\bar\rho),\
3\mathcal B(\mathcal EQ_2)(t,\bar\rho)-T_{\rm nor}
\right),
\qquad Z\in W_D^{(1)}.
}
\tag{21}
$$
(19) 的全部高尾参与 (21)，没有只减其 $t=0$ 平方项。
特别
$$
\mathcal EQ_2=2Y(Y-1)-18t^2Y^2/d
$$
是实际完整 normal 行。
(21) 包含 R787 的全 $D_2$，也包含所有不被 $F^2$ 整除的原余列；
同一个 $Z$ 必须同时满足两输出。

## 6. 因子接触矩阵的真正第一 Bockstein

给定 $\bar G$，令 $\mathcal A_G$ 是同一 $b$ 帽内、
只准 $d$ 极、每个 Gauss 值均不低于 $G$ 的原显示因子格。
使用的是 $G$ 的**实际**角值，不用五型最大亏损替代。
其基由 R782(19)、(23) 取实际亏损得到，
并包括常数 $1$；因为 $G(t,0)=1$，其每个 Gauss 值都不大于零。

固定同一合法整格提升，定义
$$
\mathsf C_h:\mathcal A_G\longrightarrow\mathcal O[t]/t^h,
\qquad H\longmapsto H(t,\rho(t))\bmod t^h.
\tag{22}
$$
由真实接触，$\bar G\in\ker\bar{\mathsf C}_h$。
其第一 Bockstein 是
$$
\boxed{
\beta_{\mathsf C}(\bar G)
=[B_h]\in\operatorname{coker}\bar{\mathsf C}_h.
}
\tag{23}
$$
这是标准整有限矩阵的首 Bockstein；
(7) 给其具体代表，而不是任选一个 $\xi$。
在五型的显示系数中，若
$G=1+\sum x_{n,j}Y^nr_n t^j$，
则这个代表正是
$$
\overline{
\frac{\mathbf e_0+\widetilde{\mathsf H}_{<h}\,\widetilde{\mathbf x}}p
}.
\tag{24}
$$
(24) 的每个分子先在原整环中验证可除 $p$。

对任意 $H\in\mathcal A_G$，Gauss 乘法给真实同预算来源
$$
\boxed{3t^2\mathfrak q G^2H\in\overline{\mathcal W}_D.}
\tag{25}
$$
其径向次数不超过原 $P^{\rm fact}$；
每个角值至少等于原 $t^2\mathfrak qG^3$ 的角值。
它的全部系数又含 $t^2$，故属于 $W_D^{(1)}$。
这尤其适用于常数 $H=1$，没有给常数变分新增来源预算。

改变同一格中的合法因子提升 $G\mapsto G+pH$ 时，
$B_h$ 改变 $\bar{\mathsf C}_h(H)$，
而原 cube 的基准改变
$3p t^2\mathfrak qG^2H\bmod p^2$。
因此该改变只能连同 (25) 的同一个实际来源修正一起运输；
不能把 $B_h$ 自行设为零。

## 7. 全余列真左对到因子 Bockstein 的转置

令 $(\lambda,\mu)$ 是 (21) 的一个真左对，即对
$W_D^{(1)}$ 的每条完整原列都有
$$
\boxed{
(\lambda+n\mu)\bigl(q_n\bar\rho^n t^j\bigr)=0
}
\tag{26}
$$
（$n=0,1,2$ 时 $j\ge1$，$n\ge3$ 时 $j\ge0$，
全部仍受原 $e_{n+1}$ 帽）。
它们作用在 $t\,k[t]/t^N$ 上；可任意延拓到常数项，
下述式子不依赖该延拓。

定义
$$
\boxed{
\nu(f)=
\mu\!\left(6t^{h+2}QeV\,f\right).
}
\tag{27}
$$
$\nu$ 只读 $f$ 的严格 $<h-13$ 前缀，
因 $N-(h+2)=h-13$。

**定理 3。** $\nu$ 是 (22) 的真正左核行：
$$
\boxed{\nu\circ\bar{\mathsf C}_h=0.}
\tag{28}
$$
因此 $\nu(B_h)$ 是 (23) 的代表无关配对。

**证明。** 对 (25) 的真实列，在 $\rho$ 上，
普通值从 $2h+2>N$ 起；
第三常数行有 $t^2$，为零。
其第一 Euler 值中，含 $G^2$ 的项同样超过截止，
仅留下
$$
6t^{h+2}QeV\,H(t,\bar\rho)\pmod{t^N}.
$$
由 (26) 对该完整原列取值，得到 (28)。
这个证明使用了整个真实来源返回 (25)，
没有先假定某个核或像对微分算子稳定。$\square$

为写出全部固定主部，令
$$
K_n=(\lambda+n\mu)(q_n\bar\rho^n),\qquad n=0,1,2.
$$
由 (19)、(26)，
$$
\lambda(Q_2(t,\bar\rho))+
\mu((\mathcal EQ_2)(t,\bar\rho))
=K_0-2K_1-K_2.
\tag{29}
$$
$q_2$ 的额外 $9t$ 项由 (26) 中真实的 $j=1$ 列消掉；
不是在 primal 方程 (21) 中删掉它。
若改变 $\lambda,\mu$ 在常数上的延拓，
因 $q_0(0)=q_1(0)=1,q_2(0)=-1$，
(29) 的组合不变。

于是 (21) 的指定右端在这个真左对上的完整值为
$$
\boxed{
\begin{aligned}
\mathscr O_{\lambda,\mu}
={}&3\mathcal B(K_0-2K_1-K_2)\\
&-\mu\!\left(a^{-1}t^hQ\mathcal H^{-1}V^3\right)
-\left\langle\nu,\beta_{\mathsf C}(\bar G)\right\rangle .
\end{aligned}}
\tag{30}
$$
有限线性代数给精确充要条件：
$$
\boxed{
\text{原同一个 }P^{\rm fact}\text{ 有完整首次修正}
\iff
\mathscr O_{\lambda,\mu}=0
\text{ 对全部满足 (26) 的真左对。}
}
\tag{31}
$$
这里的三项都有实际同源定义：
固定平方主部、完整 $u^2$ carry 对应的三次值项，
以及同一低有理前缀的因子 Bockstein。
尤其最后一项不是一个自由高轴参数。

如果另证 $\beta_{\mathsf C}(\bar G)=0$，
则最后一项确实可由同格因子提升消去；
若未证，不能因 $\nu$ 已杀 $\bar{\mathsf C}_h$ 就断言它杀其 Bockstein。
这正是 (30) 保留的实际提升问题。

## 8. 同 R 与下一位

(17)、(21)、(30) 均只针对原完整第一次 $p^2$ 提升，
而且始终保同一个 $R$。
它们已完整包括原两条十三行及第三单位行，
没有从相对 $J$ 的必要条件直接跳到全 $M$ 结论。

通过 (21) 后，$M(R)/p$ 与第二代表
$M(P^{\rm fact}+pR)/p^2\bmod p$
仍需原 R687/R651 的全高尾、低行右逆及相同修正。
本篇不能把这些数据也缩成 (7)，
更不能由因子接触或一个来源端可逆变换推出 $p^3$ 可解。

新增的可检验接口是 (30)：
可继续在 (26) 的全实际左空间中找一个非零配对，
或实际证明其全为零并运输同 $R$；
因子五型的模 $p^2$ 接触数据则通过 (23)、(28) 精确参与。
本文尚未完成这个判定，不将其充要表达式当作主目标非零。

依赖：
[R782](R782-original-r2-five-profile-factor-and-inhomogeneous-contact-gate.md)；
[R787](R787-original-factor-return-and-whole-square-source-normal-kernels.md)；
[R755](R755-whole-original-cube-carry-filter-and-specified-value-class-invariance.md)；
[R771](R771-original-r2-full-fiber-and-complete-boundary-compensation.md)；
[R687](R687-original-cm-three-digit-matrix-and-complete-same-correction-transport.md)。
