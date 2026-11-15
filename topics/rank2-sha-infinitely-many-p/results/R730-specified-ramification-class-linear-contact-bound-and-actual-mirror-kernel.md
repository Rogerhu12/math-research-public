# R730 — 指定分歧类的线性接触门、真实镜轴商与新增原首核

日期：2026-11-15。**状态：已证明。**

本篇继续 R727 的指定列
$z_c=\pi_{\rm v}\mathsf M_0(qt^rFUA)$。
先证明一个实际限制：在 R701 的固定角最高系数范围，
若 $UA$ 在整个原分歧交概形 $Z=(F,\mathcal EF)$ 上为零，
则原接触必须满足
$$
h\le4\deg_tF+8\deg_YF.
$$
更准确地，原 ODE 迫归一化曲线上一个指定商函数
在固定六纤维以外具有显示的极点总量。
这付清高接触窗中的 $UA|_Z\ne0$，不假定某个自由简单分歧点存在。

随后给整个原 $F\mathcal H_2$ 在 R547 单位商中的准确像。
指定 $z_c$ 若仍为零，必须有一个同预算镜轴核在 $Z$ 上取非零值 $UA$；
它产生一条与 $P^{\rm fact}$ 独立的真实原首核。
原首核一维时，$z_c$ 因而确有单位行。
一维条件本身仍未证明；本篇没有据此宣称完整指定 forcing 非零。

## 1. 同一实际因子、固定角和原两个长度

保 R701、R722、R726、R727 的同一个整基准
$$
P^{\rm fact}=q\,t^rF^3\in\mathcal W_D,\qquad q=d^{-C_D}Q,
$$
$$
p=6s-1>101,\quad
1\le\ell\le r<h,\quad
k=2h+r-s,\quad0\le k<\ell,
\tag{1}
$$
$$
d=1+8t,\quad h_7=7+4t+16t^2,\quad
e=\mathcal EF=YF_Y,\quad
\mathcal E=Y\partial_Y,\quad \delta=t\partial_t.
$$
$C\subset X$ 是同一几何整因子曲线，
$P=(0,1)$ 是原光滑点，$e(P),Q(P)$ 为单位；
$\kappa=C^2$、$\chi=-K_XC$、全部十九角格 $\mathcal H_j$ 不变。
以下几何计算使用其模 $p$ 对象；整来源和高位仍按同一提升保留。

置
$$
b=\deg_YF,\qquad a_F=\deg_tF,\qquad b\ge2.
$$
保 R701 的准确固定角最高系数假设：
$f_b(t)$ 的所有零都在
$$
S_0=\{0,1,-1/8,\alpha_+,\alpha_-\},\qquad
\alpha_\pm=(-1\pm3\sqrt{-3})/8.
\tag{2}
$$
它来自同一个整 $S$-unit 最高系数，不把模 $p$ 的偶然分解另作整提升。
记 $S=S_0\cup\{\infty\}$。
继续保
$$
\boxed{p>\max(a_F,b).}
\tag{3}
$$
这在原 $p>8b^2+4bu_{\rm cap}$、$u_{\rm cap}\ge0$ 下自动成立，
因为 $a_F\le u_{\rm cap}+4b$。
(3) 只用于以下局部 tame 估值，不把超出原截止的 ODE 延长。

沿同一分支，
$$
\eta=\log(g/\widetilde\psi)=t^hu+p\xi,\qquad u(0)\in\mathcal O^\times,
\tag{4}
$$
保原 $\xi_0$ 和 Gaussian。
由 (1)，$h<s<p$。
原矩阵始终是 $J$ 或完整 $M=c_*U_0w^{13}J$。

使用 R545 的实际角平衡整数
$$
1\le c=\mu_{d,1}\le u_{\rm cap}-\mu_{\infty,1}
$$
以及 R727 已付的同源截面
$$
\boxed{
U=d^c\in\mathcal H_1,\qquad
A=t^2Y^2(t-1)^2h_7^2d^{c-1}\in\mathcal H_1.
}
\tag{5}
$$
本篇聚焦 $Z_d>0$ 的情形；若原角负部为零，可以取 $c=0$，
R727 的两条剩余切向来源本已为零。
(5) 的全部十九角及 $b\ge2$ 的来源帽照 R727 保留。

为免与原角负部混淆，本文的
$$
\boxed{Z=V(F,e)\subset X}
\tag{6}
$$
始终表示 R550 的真实有限完全交概形。
$F,e$ 是 $\mathcal O_X(C)$ 的截面，
$\operatorname{length}Z=\kappa$，$P\notin Z$。
不把它缩成仿射简单根的集合。

## 2. 归一化、tame 局部和指定极点量

可先扩张至代数闭剩余域；所有非零和像条件最后按原域下降。
令 $\widetilde C\to C$ 为归一化。
$t,Y$ 在其函数域中的次数分别为 $b,a_F$。
由 (3) 两个映射可分，每个局部分歧指数均小于 $p$。

在 $t(Q)\notin S$ 的点上，$Y$ 不可能有极点：
若有，原多项式方程的最高项
$f_b(t)Y^b$ 具有严格最小估值；
$f_b(t(Q))$ 是单位，其他项不能取消。
故这些点只有 $Y$ 为单位或 $Y$ 为零两种情形。

定义一个准确的非负整数
$$
\boxed{
\Delta_F
=\sum_{t(Q)\notin S}
\max\{0,\operatorname{ord}_Q(e)-\operatorname{ord}_Q(UA)\}.
}
\tag{7}
$$
它是指定有理函数 $UA/e$ 在固定六纤维以外的极点总次数。
在这些仿射点，(5) 的全部 $t$ 因子都是单位，故
$$
\operatorname{ord}_Q(UA)=2\operatorname{ord}_QY.
\tag{8}
$$
特别 $\Delta_F$ 的这一部分不依赖平衡整数 $c$。

**引理 1（包括奇点的 tame 导数界）。**
若 $t(Q)=t_0\notin S$，
令 $e_t=\operatorname{ord}_Q(t-t_0)$，
则
$$
\boxed{\operatorname{ord}_Q(F_Y)\ge e_t-1.}
\tag{9}
$$

**证明。** 这里 $f_b(t_0)$ 是单位，
所以 $F$ 的全部 $Y$ 根在 $t=t_0$ 的代数局部扩张中整。
由 $e_t<p$，所选正规分支可用参数 $v$ 写成
$t-t_0=v^{e_t}$；常数域代数闭，允许整单位的 tame 根。
该分支的 $e_t$ 个共轭根为 $Y(\zeta v)$，$\zeta^{e_t}=1$。
对除自身以外的每个共轭，
$Y(v)-Y(\zeta v)$ 的 $v$ 阶至少一；
它们不相同，因为 $k((t))[Y]$ 就生成该正规局部分支。
原导数
$$
F_Y(t,Y(v))
=f_b(t)\prod_{Y_i\ne Y(v)}(Y(v)-Y_i)
$$
因此至少获得这 $e_t-1$ 份正阶。
其他局部分支的根仍整，贡献非负估值。
这证明 (9)，即使原仿射点有多个分支或为奇点也成立。
没有使用该点光滑或简单分歧。证毕。

若 $Y(Q)=0$，令 $m=\operatorname{ord}_QY\ge1$，
以及 $\Delta_Q$ 为 (7) 的该点贡献，则 (8)、(9) 给
$$
\operatorname{ord}_Q(e)\ge m+e_t-1,\qquad
\operatorname{ord}_Q(e)\le2m+\Delta_Q.
$$
于是
$$
\boxed{e_t\le m+1+\Delta_Q\le2m+\Delta_Q.}
\tag{10}
$$
当 $\Delta_Q=0$ 时，这特别给所需 $e_t\le2m$。
还可以直接由
$F_t\,dt+F_Y\,dY=0$
得到 $\operatorname{ord}(e)=\operatorname{ord}(F_t)+e_t\ge e_t$；
这里 $m,e_t<p$ 保两条微分的首项不消失。
两种证明均在正规分支上成立，不跳过原奇点。

若 $Y(Q)$ 是单位，则 (8) 给
$\Delta_Q=\operatorname{ord}_Q(e)\ge e_t-1$。
尤其 $\Delta_Q=0$ 时 $F_Y$ 为单位，
原仿射点确实光滑，且 $t$ 不分歧。

## 3. 原 ODE 在正规曲线上的全部极帽

在 $k(\widetilde C)$ 中定义
$$
V=\delta\log Y=\frac{t}{Y}\frac{dY}{dt},
$$
$$
\boxed{
\mathcal F_F
=\mathcal R-\{6(1-t)\delta-(1+2t)\}V,
\qquad
\mathcal R=\frac{t(154+160t+1792t^2)}{3(1+8t)^2}.
}
\tag{11}
$$
这只用有理导数，不要求全域的 log 存在。

先在 $t(Q)\notin S$ 逐点估计。

- 若 $Y$ 为单位且 $e_t=1$，$V,\delta V$ 均正则，故没有极点。
- 若 $Y$ 为单位且 $e_t\ge2$，
  $V$ 的极阶至多 $e_t-1$，$\delta V$ 的极阶至多 $2e_t-1$。
  因而
  $$
  \operatorname{pole}_Q(\mathcal F_F)
  \le2e_t-1\le3(e_t-1)\le3\Delta_Q.
  $$
- 若 $Y$ 有零阶 $m$，则 $m,e_t<p$，
  $V$ 的极阶为 $e_t$，$\delta V$ 的极阶至多 $2e_t$。
  由 (10)，
  $$
  \operatorname{pole}_Q(\mathcal F_F)
  \le2e_t\le4m+2\Delta_Q.
  $$

$Y$ 的全零除子次数为 $a_F$。
所以固定六纤维之外的全部极阶总和满足
$$
\boxed{
\deg(\mathcal F_F)_\infty\big|_{t\notin S}
\le4a_F+3\Delta_F.
}
\tag{12}
$$
导数首项在某些更高阶因特征 $p$ 消失只会改善上界；
本证明没有把未知高阶首项当作单位。
必须为单位的局部整数 $m,e_t$ 则已由 (3) 支付。

固定六纤维不使用 (7) 的任何消失假设。
对每一正规分支，仍用其实际分歧指数 $e_t$，有下表：

| $t$ 纤维 | $\mathcal F_F$ 的极阶上界 | 理由 |
|---|---:|---|
| $0$ | $0$ | $\delta$ 保正则阶，$V$ 正则，$\mathcal R$ 正则 |
| $1$ | $e_t$ | $6(1-t)$ 抵消 $\delta V$ 的一份 $e_t$ |
| $-1/8$ | $2e_t$ | 原 $\mathcal R$ 的双极及完整 $\delta V$ |
| 每个 $h_7$ 根 | $2e_t$ | 原一般有限非零纤维界 |
| $\infty$ | $e_t$ | $V,\delta V$ 正则，原 $A,B,\mathcal R$ 至多一份 $t$ 极 |

例如在 $0$ 或 $\infty$，$t/(dt/dv)$ 是 $v$ 乘单位；
若 $Y$ 有零或极，$V$ 的常数为其真实阶数与 $e_t$ 的比，
若 $Y$ 为单位则 $V$ 仍正则。
在 $1,-1/8,\alpha_\pm$，
$V$ 的一般极阶至多 $e_t$；
表中已保所有 $Y$ 零、极及分歧分支。
这些均为不同纤维，$p>101$ 保固定坏根和分母不合并。

每个纤维的分歧指数总和为 $\deg(t)=b$。
所以表中完整固定部分的总极阶至多
$$
\boxed{8b.}
\tag{13}
$$
没有因原 $F$ 的某个高角重数很大就删掉该处；
全部高角已在这些完整纤维界内。

## 4. 真实接触给非零 forcing 和线性门

原 R507 的精确 ODE 在 $t^s$ 之前给
$$
\mathcal P\log g=\mathcal R\pmod{t^s},\qquad
\mathcal P=6(1-t)\delta^2-(1+2t)\delta.
$$
沿 $P$ 的同一 Hensel 分支，(4) 因而给
$$
\boxed{
\mathcal F_F
=h(6h-1)u(0)t^h+O(t^{h+1}).
}
\tag{14}
$$
$0<h<s=(p+1)/6$，故 $h(6h-1)$ 是单位。
因此 $\mathcal F_F$ 是正规曲线上的非零有理函数，
在原 $P$ 的零阶准确为 $h$。
这只读原首共振之前的窗口，不需要把 ODE 延过 $s$。

非零有理函数的零、极总次数相等。
由 (12)–(14) 得到：

**定理 1。**
$$
\boxed{
h\le4a_F+8b+3\Delta_F,\qquad
\Delta_F\ge
\max\left\{0,\left\lceil\frac{h-4a_F-8b}{3}\right\rceil\right\}.
}
\tag{15}
$$

若实际截面 $UA|_Z=0$，由于 $Z$ 在 $C$ 上是 $e|_C$ 的 Cartier 零除子，
其准确限制序列给
$$
UA|_C=e\,L_C,\qquad L_C\in H^0(C,\mathcal O_C(C)).
\tag{16}
$$
把 (16) 拉回归一化后，
$UA/e$ 是相应线束的正则截面。
在 $t\notin S$ 的原仿射框中没有边界极，故 $\Delta_F=0$。
这里 (16) 使用整个真实 $Z$，
包含原固定角、重交点及非约化结构；
没有只在光滑自由点上验值。

由此：

**推论 1。**
$$
\boxed{
h>4a_F+8b\quad\Longrightarrow\quad UA|_Z\ne0.
}
\tag{17}
$$
反向不作声明：在奇点处，
归一化上无极不必自动降成原局部环中的整除。
(17) 只使用严格成立的正向 (16)。

$\Delta_F$ 是指定正规曲线商函数的极点质量，
不是原矩阵余核的维数或 Smith 因子数；
(15) 不将这些不同量混同。

在原满主阶临界范围
$$
u_{\rm cap}=b+O(1),\quad
a_F\le5b+O(1),\quad
h=\frac{141}{32}b^2+O(b),
$$
(17) 对充分大 $b$ 成立，
并且
$$
\boxed{\Delta_F\ge\frac{47}{32}b^2+O(b).}
\tag{18}
$$
本结论逐个应用于已存在且满足 (2) 的实际因子，
并不假定这样一个原首核已被构造。

## 5. 整个原 FH2 在垂直单位商中的准确像

现在使用 R727 的同一整单位块。
取实际 $\lambda(F)=1,\lambda(A)=0$，
令 $\mathcal L=\ker\lambda\subset\mathcal H_1$；
原单位来源为
$$
(\mathcal H_2/\mathcal OF^2)\oplus\mathcal L
\longmapsto q t^r(\mathcal W_FH+F^2K).
\tag{19}
$$
保原 cube 的 $p$ 因子，不把整个 $F^2\mathcal H_1$ 商掉。

令 $\mathsf M_0=J$ 或完整 $M$，分别取
$$
T=s-r,\qquad T=s-r-13.
$$
以下保
$$
\boxed{h>\kappa,\qquad q_T:=T-h>\kappa,\qquad T\le2h.}
\tag{20}
$$
因此 $T>2\kappa$、$T<p$。
(19) 的物理像是原整目标的自由直和项，
记其商为 $\mathscr Q_{\rm v}$，商映射为 $\pi_{\rm v}$。

以下所有像和核在模 $p$ 中读取，
$\mathcal H_i$ 简写其约化。
定义同一个实际正镜轴核
$$
\boxed{
K_{\rm mir}
=\ker\left(\mathcal H_2
\xrightarrow{H\mapsto H(t,\psi e^{2\eta_0})}
k[t]/t^T\right),\qquad \eta_0=t^hu.
}
\tag{21}
$$
没有给它添独立 normal 数据。

**定理 2。** 整个真实 $q t^rF\mathcal H_2$ 在
$\overline{\mathscr Q}_{\rm v}$ 中的像准确为
$$
\boxed{
\operatorname{im}\left(
\mathcal H_2\xrightarrow{H\mapsto
\pi_{\rm v}\overline{\mathsf M}_0(qt^rFH)}
\overline{\mathscr Q}_{\rm v}\right)
\simeq
\frac{H^0(Z,\mathcal O_Z(2C))}
{\operatorname{res}_Z K_{\rm mir}}.
}
\tag{22}
$$
指定 $z_c$ 在此同构中恰由 $UA|_Z$ 表示。

**证明。** 先计算原物理核。
若 $qt^rFH$ 被 (19) 吸收，
有同一个 $K\in\mathcal H_2$、$L\in\mathcal H_1$
使
$$
G=FH-\mathcal W_FK-F^2L
$$
的原完整高两块为零。
模 $p$ 时允许全 $\mathcal H_1$ 替代 $\mathcal L$，
因为多出的一条 $F$ 只给原 $F^3$，其首位为零。

$\eta_0^2=0\bmod t^T$，所以两 Gaussian 行准确给
$G|_C=0\bmod t^T$。
但 $G|_C=2eK|_C$。
$e(P)$ 单位、$T>2\kappa$，
且 $K|_C$ 的线束次数为 $2\kappa$，
因此 $K|_C=0$，同一个原来源写成 $K=FK_1$，
$K_1\in\mathcal H_1$。

原恒等式
$\mathcal W_F(FK_1)=F(F\mathcal EK_1-eK_1)$
于是给
$$
G=F\{H+eK_1-F(\mathcal EK_1+L)\}.
$$
按 R511 的同一实际镜轴身份，
它物理为零当且仅当括号属于 (21)。
反向也直接代回；若出现 $L$ 的 $F$ 分量，
在首位中由原 $F^3$ 消掉，而非在整系数中删 cube。
因此该物理核准确是
$$
\boxed{K_{\rm mir}+e\mathcal H_1+F\mathcal H_1.}
\tag{23}
$$

$F,e$ 在原 $X$ 上为正则序列。
Koszul 序列
$$
0\to\mathcal O_X\to\mathcal O_X(C)^2
\to\mathscr I_Z(2C)\to0
$$
结合 R495 的 $H^1(\mathcal O_X(C))=0$
及有理曲面的 $H^1(\mathcal O_X)=H^2(\mathcal O_X)=0$，
给准确全局商
$$
\mathcal H_2/(F\mathcal H_1+e\mathcal H_1)
\simeq H^0(Z,\mathcal O_Z(2C)).
$$
再商 (23) 即得 (22)。证毕。

## 6. 分母就是原第一连接核，未付的量没有隐藏

在 (20) 下，准确有
$$
\boxed{
\ker(\operatorname{res}_Z:K_{\rm mir}\to H^0(Z,\mathcal O_Z(2C)))
=kF^2.
}
\tag{24}
$$
确实，若 $B\in K_{\rm mir}$ 且 $B|_Z=0$，
则 $B|_C=eL_C$，$L_C$ 的线束次数为 $\kappa$。
(21) 使 $B|_C$ 在 $P$ 至少有 $h$ 阶零；
$h>\kappa$、$e(P)$ 单位迫 $L_C=0$，
从而 $B=FB_1$、$B_1\in\mathcal H_1$。
再由同一镜轴中的 $F$ 阶恰为 $h$，
$B_1|_C$ 消到 $q_T>\kappa$，
所以 $B_1$ 是 $F$ 的常数倍。
反向 $F^2$ 在镜轴上具有 $2h\ge T$ 阶，故成立。

R524/R550 的原第一连接
$$
\alpha_\eta:H^0(C,N^2(-hP))\to\operatorname{coker}E_{q_T},
\qquad N=\mathcal O_C(C),
$$
给同一正合列
$$
0\to kF^2\to K_{\rm mir}\to\ker\alpha_\eta\to0.
$$
因此
$$
\boxed{
\operatorname{res}_Z K_{\rm mir}
\simeq\ker\alpha_\eta
}
\tag{25}
$$
是其真实单射限制像，
不是 $\kappa$ 个可以任意填写的分歧值。

(22) 于是给指定列的准确判据
$$
\boxed{
\bar z_c=0
\quad\Longleftrightarrow\quad
UA|_Z\in\operatorname{res}_Z K_{\rm mir}.
}
\tag{26}
$$
(17) 现在保证右边若成立，命中的必是一个非零原第一连接核值。
本篇未把 (25) 的未知像替换成零或整个目标。

## 7. 真正的新原首核，而非来源呈示中的零关系

联合 (17)、(20)，假设 $\bar z_c=0$。
由 (26) 选择同一个实际 $B\in K_{\rm mir}$，满足
$$
B|_Z=UA|_Z\ne0.
\tag{27}
$$
于是
$$
\boxed{P_{\rm new}=qt^rFB\in\mathcal W_D}
\tag{28}
$$
是一个非零原首核：整个 $F\mathcal H_2$ 已由 R495 返回旧预算，
(21) 则保证对应的 $J$ 或完整 $M$ 首位准确为零。

它与 $P^{\rm fact}=qt^rF^3$ 线性独立。
否则由原多项式环的消去，
$B$ 是 $F^2$ 的常数倍，
与 (27) 在整个 $Z$ 上的非零矛盾。
所以得到：

**定理 3。** 在 (17)、(20) 的实际范围，
$$
\boxed{
\bar z_c=0
\quad\Longrightarrow\quad
\dim_k\ker\overline{\mathsf M}_0\ge2.
}
\tag{29}
$$
特别，
$$
\boxed{
\ker\overline{\mathsf M}_0=k\bar P^{\rm fact}
\quad\Longrightarrow\quad
\bar z_c\ne0.
}
\tag{30}
$$
这时 $\mathscr Q_{\rm v}$ 自由，
故 $z_c$ 在该商中有单位行，
可把其实际来源列作为再一条整单位列消去。

(28) 不是 R727 中因两个相同来源呈示而产生的形式零关系。
它是原 $\mathcal W_D$ 中真正非零、由 (27) 证实独立的元素。
也没有声称其公共 $t$ 阶一定是 $r+1$：
此处的独立性来自完整分歧值，不借用 R722 的另一个高 $t$ 阶判据。

对 $J$ 使用 $T=s-r$；
对原 $M$ 必须用 $T=s-r-13$。
(29)–(30) 各自只约束对应矩阵的核，不能互换。
当前没有预先证明这些原核一维，
所以 (30) 是明确的条件推论，不是主目标的完成声明。

## 8. 原 forcing、其余列与同一 R 的完整边界

本篇把 R727 的指定列放入完整真实商 (22)，
并证明其分歧输入在临界高接触窗中非零。
剩余问题因此是这个指定非零输入是否落入 (25) 的真实像，
以及其与 R726 指定 forcing、投影后的切向 $00$ 块、
所有其它 $\mathcal W_D$ 列的联合。

即使 (30) 可用，也只增加一条已指明的单位列；
它不证明整个原 forcing 在余核中非零，
不允许将两个单位块的秩直接相加，
更不赋予所有新增来源原三中央零。

所有使用的整 Schur 变换保持同一个
$P_2=P^{\rm fact}+pR$。
原 $P_{134}/U_0$、原 $\xi_0$、$U_1/p$、
两条十三行 carry、低行右逆高尾、
原 cube 的 $p$ 因子及第三精度 $d_2/G_2$ 均继续保留。
定理2、3是在首位上的准确判断；
它们不把模 $p$ 的镜轴类自动提升为完整模 $p^3$ 解。

依赖：[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R507](R507-original-euler-resonance-and-actual-forcing-transpose.md)；
[R524](R524-original-three-layer-boundary-kernel-and-first-escape-window.md)；
[R547](R547-zero-charge-vertical-unit-block-and-actual-cubic-schur-column.md)；
[R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[R701](R701-sharp-two-charge-clearing-and-complete-same-correction-cap.md)；
[R727](R727-original-balanced-sections-and-single-residual-column-in-vertical-unit-quotient.md)。
