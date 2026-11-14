# R461 — 原径向 ODE 与真首核因子的统一次数下界

日期：2026-11-14。**状态：已证明。** 在整个 $J=0$ 原 canonical 格中，直接使用原径向坐标 $\mathscr R$，不收 $\Theta$ 坐标的十七倍次数。原 ODE 的单位首共振给任一横截代数分支的有效接触界。结合实际来源次数，得到：若真立方首核为 $t^rF^3Q$、$Q$ 原点单位、$F$ 对 $\mathscr R$ 横截，则其径向次数满足一个明确的、随 $p/D$ 增长的下界；特别 $p>80D+89$ 时不可能有径向一次的这种首核。更一般的单一一次因子幂也有线性 $D$ 的排除界。

这些结论用于真实相对 $J$，所以由 R449 也排除相同因子形状的原真正第二核。它们没有排除高径向次数的平衡临界因子、多个不同接触因子的乘积或混合 $j$ 部分，未把两完整中央零扩张到新来源。

## 1. 原来源和没有十七倍损失的完整多项式框

取 $p=6s-1>83$、$1\le\ell<s-13$、$L=2s+\ell$，继续使用原整个单部分
$$
\mathcal W_{D,0}=\bigoplus_{n=0}^D
\mathscr R^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
$$
其中
$$
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},\quad
d=1+8t,\quad h_7=7+4t+16t^2,
$$
$$
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor,
$$
$$
f_n=\deg q_n+e_{n+1}=\lfloor9n/2\rfloor+4.
$$
保留来源使用范围 $f_D<p$，所以 $D<p$；以下所有出现的因子重数都小于 $p$。

对这个**整个固定预算的格**乘同一个角单位 $d^{C_D}$，有
$$
\boxed{
d^{C_D}\mathcal W_{D,0}\subset
\mathcal O[t,Y]_{\deg_Y\le D,\,\deg_t\le M_D},\quad
Y=\mathscr R,\qquad M_D=f_D+C_D=5D+4-(D\bmod2).}
\tag{1}
$$
每个径向系数的次数恰受 $f_n+C_D\le M_D$ 控制。物理评价中 $d(t(w))^{C_D}$ 是完整整单位，故这次操作保持 $J$ 的所有真核、Bockstein 和相对余核；完成比较后用它的整逆返回原目标。

实际径向量及其 regularized 轴是
$$
\rho(t)=d(t)\Theta(t)^{17},\qquad
g(w)=e^{-\kappa w^s}\rho(t(w)),\qquad
Y_{\rm phys}=g(w)e_2(a\epsilon),\quad a=p\kappa\in\mathcal O^\times.
\tag{2}
$$
因此在次数小于 $s$ 的 $t$ 轴上，$g$ 与原 $\rho$ 的系数完全相同。$t=-w+\cdots$ 是同一整严格参数的单位倍；接触阶在这两种坐标中相同。

## 2. 原有理径向 ODE 和不可消的首共振

由 R305 的实际 theta 方程，$Z=\log\Theta^{17}$ 准确满足
$$
6t(1-t)Z''+(5-8t)Z'=34/3.
\tag{3}
$$
所以对 $Y=\rho=d\Theta^{17}$，置
$$
A(t)=6t(1-t)d^2,\qquad B(t)=(5-8t)d^2,
$$
$$
\boxed{
C(t)=\frac{34}{3}d^2-384t(1-t)+8(5-8t)d
=\frac{154+160t+1792t^2}{3}.}
\tag{4}
$$
得到同一个真实径向方程
$$
\boxed{\mathscr D(Y):=
A(YY''-(Y')^2)+BYY'-CY^2=0.}
\tag{5}
$$
这里 $\deg A=4,\deg B=3,\deg C=2$；$d^2$ 清掉的是原实际对数导数，未换一个自由 formal frame。

**共振引理。** 在剩余域的 $k[[t]]$ 中，没有任何单位 $Y_*(t)$ 满足 (5)。

**证明。** 若有，置
$v=Y_*'/Y_*-8/d$。消去单位 $Y_*^2d^2$，准确得到
$$
6t(1-t)v'+(5-8t)v=34/3.
$$
写 $v=\sum v_nt^n$，则
$$
v_0=34/15,\qquad
(6n+5)v_n=(6n+2)v_{n-1}\quad(n\ge1).
\tag{6}
$$
$v_0,\ldots,v_{s-2}$ 都是单位：此前所用分子、分母都不是 $p$ 的倍数。到 $n=s-1$，左系数为 $6s-1=p=0$，右侧却为
$-3v_{s-2}\ne0$，矛盾。这个原第一共振不取决于选哪一个 $Y_*(0)\ne0$，也没有使用中央导数非零假设。$\square$

原特征零 $\rho$ 并不矛盾；其第 $s$ 个系数正有原 $p$ 分母。它在次数小于 $s$ 的整截断继续满足 (5) 至少到 $t^{s-1}$ 之前。

## 3. 任意横截因子的真实接触界

设 $F\in k[t,Y]$ 不可约，满足
$$
F(0,1)=0,\qquad F_Y(0,1)\ne0,\qquad
a_F=\deg_tF,\quad b_F=\deg_YF\ge1.
$$
令 $\psi(t)\in k[[t]]$ 为其唯一正规分支，$F(t,\psi)=0$、$\psi(0)=1$。原 regularized 轴给接触 $h$；若它在已读窗口中不出现，$h\ge s$ 只表示前 $s$ 项仍接触。以下 $\min(h,s)$ 完全由原低轴决定。

**定理 1。** 准确有
$$
\boxed{\min(h,s)\le a_F(6b_F-1)+2b_F+1.}
\tag{7}
$$

**证明。** 由横截性，$\psi$ 与原 $\rho$ 在次数小于 $H:=\min(h,s)$ 时相同。式 (5) 的二阶项含一个 $t$，所以
$$
\mathscr D(\psi)\in t^{H-1}k[[t]].
\tag{8}
$$
这是与实际低轴的比较，不把 regularized 高轴当成原 ODE 的自由解。由共振引理，$\mathscr D(\psi)$ 非零。

记 $D_F=F_Y$。隐式微分后，$D_F^3\mathscr D(\psi)$ 是下面真实多项式在 $Y=\psi$ 的值：
$$
\begin{aligned}
K_F={}&A\bigl[
Y(-F_{tt}D_F^2+2F_{tY}F_tD_F-F_{YY}F_t^2)
-F_t^2D_F\bigr]\\
&-BYF_tD_F^2-CY^2D_F^3.
\end{aligned}
\tag{9}
$$
逐项得到完整次数
$$
\deg_tK_F\le3a_F+2,\qquad
\deg_YK_F\le3b_F-1.
$$
没有删除原 $d^2$ 的两个次数；若某个低阶导数为零，只会降低这个上界。

$K_F(t,\psi)$ 非零，所以 $F\nmid K_F$。其非零结式满足
$$
\deg_t\operatorname{Res}_Y(F,K_F)
\le b_F(3a_F+2)+a_F(3b_F-1)
=a_F(6b_F-1)+2b_F.
\tag{10}
$$
Sylvester 无分母 Bézout 式在正规分支上给结式的消失阶至少为 $H-1$；$D_F(0,1)$ 还是单位，所以这里没有隐式导数的负阶损失。比较次数与消失阶即得 (7)。$\square$

### 径向一次因子的更强界

若 $F=u(t)Y-v(t)$，则 $u(0)=v(0)\ne0$，且
$\deg u,\deg v\le a_F$。令
$$
U=uv,\qquad W=v'u-u'v.
$$
$\psi'/\psi=W/U$，其 (5) 对数方程的非零分子准确为
$$
\boxed{N_F=A(W'U-WU')+BWU-CU^2.}
\tag{11}
$$
分母 $U^2$ 在原点为单位，且 $\deg N_F\le4a_F+2$。由同一个共振引理，$N_F$ 非零；(8) 给它至少 $H-1$ 阶零。因此
$$
\boxed{b_F=1\quad\Longrightarrow\quad
\min(h,s)\le4a_F+3.}
\tag{12}
$$
这是整个有理分支的直接分母计算，不只测试一个截断近似式。

## 4. 原立方首核强制径向次数增长

设一个实际来源 $P\in\mathcal W_{D,0}$ 的约化，在 (1) 的完整角单位运输后，满足
$$
d^{C_D}\bar P=t^rF^3Q,\qquad r\ge1,\qquad
F_Y(0,1)Q(0,1)\ne0,\quad F(0,1)=0.
\tag{13}
$$
并假定 $\bar P\in\ker\bar J$。所有这些条件都是原有限格中的条件；没有以矩形内任意多项式替代来源。

式 (1) 直接给
$$
3b_F\le D,\qquad 3a_F+r\le M_D.
\tag{14}
$$
真实首核的第二 Gaussian 行又给
$$
r+2h\ge s.
\tag{15}
$$
当 $h\ge s$ 时，以下推论仍有效：由 (7) 已有 $s$ 不超过该接触上界，而不需把未读的高轴自由延长。

**定理 2。** 每个 (13) 的实际首核都满足
$$
\boxed{3s\le(12b_F-2)M_D+11,}
\tag{16}
$$
等价地
$$
\boxed{p\le(24b_F-4)M_D+21,
\qquad
b_F\ge\frac{p-21+4M_D}{24M_D}.}
\tag{17}
$$
其中整数次数当然还须向上取整。结合 $3b_F\le D$，另得
$$
\boxed{p\le(8D-4)M_D+21.}
\tag{18}
$$

**证明。** 记 (7) 的右端为 $H_F$。若 $h<s$，由 (15) 得
$s\le r+2h\le r+2H_F$；若 $h\ge s$，(7) 给 $s\le H_F\le r+2H_F$。因此两种情形统一为
$$
\begin{aligned}
s&\le r+2a_F(6b_F-1)+4b_F+2\\
&\le\frac{(12b_F-2)M_D+(5-12b_F)r+12b_F+6}{3}\\
&\le\frac{(12b_F-2)M_D+11}{3}.
\end{aligned}
$$
第二行用 (14)，最后一行用 $r\ge1$、$b_F\ge1$，所以 $5-12b_F<0$。再用 $p=6s-1$ 即得 (16)–(18)。$\square$

这个下界在固定 $D/\sqrt p$ 的临界规模下迫使 $b_F$ 本身按 $\sqrt p$ 增长。因此小径向次数的高接触因子不是一个尚可免费填入 R459 的接口；它们已被原 ODE 排除。另一方面，(18) 的常数并没有排掉平衡的高 $b_F$ 临界区，不能据此声称整个 $J$ 满秩。

## 5. 径向一次因子：全部 r 和更高重数的明确范围

对立方使用 (12) 代替 (7)，同样得到
$$
s\le r+2(4a_F+3)
\le\frac{8M_D-5r+18}{3}
\le\frac{8M_D+13}{3}.
$$
所以
$$
\boxed{b_F=1\quad\Longrightarrow\quad
p\le16M_D+25\le80D+89.}
\tag{19}
$$
这是对全部角含量 $r\ge1$、全部允许 $\ell$ 的统一必要界；没有寻找有限素数样本。特别 $p>80D+89$ 时，整个原格中不可能有 (13) 的径向一次立方首核。

更一般，假定同一个真实单因子形状为
$$
d^{C_D}\bar P=t^rF^mQ,\qquad b_F=1,\quad
2\le m\le D<p,\quad r\ge1,\quad Q(0,1)\ne0.
$$
此处 $m$ 是单位，所以首 Euler 行准确给
$r+(m-1)h\ge s$。实际来源次数给 $ma_F+r\le M_D$。再用 (12)，得完整固定重数界
$$
\boxed{m s\le4(m-1)M_D+3m^2-6m+4.}
\tag{20}
$$
特别 $m=2$ 时 $p\le12M_D+11$，$m=3$ 恢复 (19)。不用固定 $m$，还统一有
$$
s\le4M_D+3D-6,\qquad
\boxed{p\le24M_D+18D-37\le138D+59.}
\tag{21}
$$
证明只需将 $r\ge1$ 代入
$$
r+(m-1)(4a_F+3)
\le4M_D+3m-6+\frac{4-4M_D}{m}
\le4M_D+3D-6.
$$
这些仍是**一个横截因子乘单位余因子**的结论。多个不同的接触因子、切向分支或混合 Kummer 部分不在这个假设内。

## 6. 接回真正原第二核和两条完整中央

R449 已证明，同一个原
$$
M^{\rm orig}=c_*U_0m_{13}J
$$
满足 $K_2^{\rm red}(M)\subset\ker\bar J$。所以 (17)、(19)–(21) 同时排除上述因子形状的原真正第二核，不能以原 carry 把一个根本不是相对首核的向量补成真第二核。

这一步使用的是 R449 的完整精确序列，未删除 $P_{134}/U_0$、最初十三个自由行或两条十三行 carry。反过来，对于没有被本篇排除的相对首核，仍须计算实际 $\pi\beta_J$、$C_2(J)/\overline H$ 和原完整第二障碍；本篇没有自动支付它们。

原两条中央仍只约束同一 $S$、$T=VT_0$ 的三个完整权及原第三位。上述 ODE 接触界不需要这些中央零，所以它既不把未知因子的中央值赋零，也不从本篇推出无穷多个好素数。

下一实际比较须保留 (17) 所迫的增长径向次数，或者转向不同接触因子的真组合；继续在固定小 $b_F$ 上搜索不会覆盖当前临界来源。

## 依赖与证书

R305 的原 theta ODE；R434 的同一角轴与 regularized 低轴比较；R453/R456 的来源格和 $f_D<p$；R459 的实际角含量与单部分单位运输；R449 的原真正第二核包含。脚本 `scripts/check-r461-radial-ode-factor-bound.py` 核 (4)、隐式与有理分支的真实微分分子、次数和全部整数预算公式，不扫描目标素数。
