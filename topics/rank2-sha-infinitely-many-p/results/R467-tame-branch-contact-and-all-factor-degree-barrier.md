# R467 — 全部分支的原 ODE 接触界与真首核因子次数障碍

日期：2026-11-14。**状态：已证明。** 本篇去掉 R461 的横截因子和单一接触因子假设。在整个原 $J=0$ canonical 格内，任一真实相对首核都必须含随 $p/D$ 增长的径向次数因子；多个不同的小次数因子、切向分支及其任意重数不能逃开这个界。特别，若全部接触因子在径向变量上都是一次，则必要 $p\le138D+77$。

证明使用原径向 ODE、其在每个 tame Puiseux 分支上的整数幂共振，以及同一局部 Hensel 因子的完整判别式。来源没有换成矩形内的任意多项式；原 $P_{134}/U_0$、真正第二核和两条十三行 carry 仍通过 R449 的准确接口保留。本篇没有排除径向次数随 $\sqrt p$ 增长的平衡临界区，也没有新增中央零。

## 1. 同一真实来源与原 ODE

取
$$
p=6s-1>83,\qquad 1\le\ell<s-13,\qquad L=2s+\ell,
\qquad f_D=\lfloor9D/2\rfloor+4<p.
$$
沿用 R461 的整个原格
$$
\mathcal W_{D,0}
=\bigoplus_{n=0}^D Y^nq_n(t)\mathcal O[t]_{\le e_{n+1}},
\qquad Y=\mathscr R,\qquad
q_n=(th_7)^{A_n}(t-1)^{B_n}d^{-C_n},
$$
其中
$$
d=1+8t,\quad h_7=7+4t+16t^2,\quad
A_n=\lfloor(n+1)/4\rfloor,\quad
B_n=\lfloor(n+1)/3\rfloor,\quad C_n=\lfloor n/2\rfloor.
$$
乘同一个实际角单位 $d^{C_D}$ 后，所有真实来源满足
$$
\boxed{d^{C_D}\mathcal W_{D,0}\subset
\mathcal O[t,Y]_{\deg_Y\le D,\ \deg_t\le M_D},
\qquad M_D=f_D+C_D=5D+4-(D\bmod2).}
\tag{1}
$$
这只是实际来源的次数上界。物理评价中 $d(t(w))^{C_D}$ 及其逆都是完整整单位；在原目标中运输后保持所有真核、Bockstein 和相对余核。由 $f_D<p$ 有 $D<p$。

原径向量、regularized 轴和实际 Gaussian 评价为
$$
\rho(t)=d(t)\Theta(t)^{17},\qquad
g(w)=e^{-\kappa w^s}\rho(t(w)),\qquad
Y_{\rm phys}=g(w)e_2(a\epsilon),\quad a=p\kappa\in\mathcal O^\times.
\tag{2}
$$
$t=-w+\cdots$ 是同一整参数的单位倍；$g$ 和 $\rho$ 在次数小于 $s$ 时相同。以下将共同的模 $t^s$ 低轴记为
$\rho_{<s}\in k[t]$，其中 $k$ 可先作代数闭包。这种剩余域扩张不改变实际矩阵的秩和核条件。

R461 已从原 theta 方程直接证明
$$
\mathscr D(Y)=A(YY''-(Y')^2)+BYY'-CY^2,
\tag{3}
$$
其中
$$
A=6t(1-t)d^2,\qquad B=(5-8t)d^2,
\qquad C=(154+160t+1792t^2)/3.
\tag{4}
$$
特征零的 $\rho$ 满足 $\mathscr D(\rho)=0$，所以
$$
\mathscr D(\rho_{<s})\in t^{s-1}k[[t]].
\tag{5}
$$
若一个正规单位 $Y_*$ 满足 $\mathscr D(Y_*)=0$，置
$v=Y_*'/Y_*-8/d$ 会得到
$$
6t(1-t)v'+(5-8t)v=34/3.
\tag{6}
$$
对 $v=\sum v_nt^n$，准确递推为
$$
v_0=34/15,\qquad
(6n+5)v_n=(6n+2)v_{n-1}.
\tag{7}
$$
$v_0,\ldots,v_{s-2}$ 都是单位，而在 $n=s-1$ 处，左系数为 $p=0$，右侧为 $-3v_{s-2}\ne0$。这就是原首共振；以下保留这个准确右端和原角单位。

## 2. 每个 tame 单位分支仍有同一个共振

**引理 1。** 若 $e$ 与 $p$ 互素，$t=u^e$，则不存在
$\psi\in1+u k[[u]]$ 满足 $\mathscr D(\psi)=0$。

**证明。** $\partial_t=(eu^{e-1})^{-1}\partial_u$。若有这样的 $\psi$，则
$$
v=\frac{\partial_t\psi}{\psi}-\frac8d
\in u^{1-e}k[[u]]
$$
满足 (6)。对 $k((u))/k((t))$ 的 tame 作用作平均
$$
\Pi(v)=\frac1e\sum_{\zeta\in\mu_e}v(\zeta u).
\tag{8}
$$
这个投影只保留整数 $t$ 次幂，并与 $\partial_t$ 和 (6) 的全部有理系数对易。因为 $1-e>-e$，$\Pi(v)$ 没有负的整数 $t$ 次幂，即 $\Pi(v)\in k[[t]]$。常数右端在平均后仍为 $34/3$，所以 $\Pi(v)$ 也满足 (6)，与 (7) 的首共振矛盾。这里没有把不同分支当作不同中央条件；只是在同一个实际方程内作整可逆平均。$\square$

下面设 $F\in k[t,Y]$ 不可约，
$$
F(0,1)=0,\qquad a_F=\deg_tF,\qquad 1\le b_F=\deg_YF<p.
$$
不再假定 $F_Y(0,1)\ne0$。$F$ 不可能被 $t$ 整除；又因 $b_F<p$，它对 $Y$ 可分。其任意局部分裂域的 Galois 群嵌入 $S_{b_F}$，故其阶与 $p$ 互素。剩余域已代数闭，所以所有局部根都在某个共同的 tame 扩张 $k((t^{1/e}))$ 中，$p\nmid e$。这一步排除了不受 (8) 控制的 wild 分支，而不是假设分支都是整数幂。

令 $c_F$ 为 $Y=1$ 在非零多项式 $F(0,Y)$ 中的重数，$1\le c_F\le b_F$。对应的 Hensel 分解可写成
$$
F(t,Y)=G(t,Y)U(t,Y),\qquad
G\in k[[t]][Y]\text{ monic},\quad \deg_YG=c_F,
$$
$$
G(0,Y)=(Y-1)^{c_F},\qquad U\in k[[t]][Y],\qquad U(0,1)\ne0.
\tag{9}
$$
即使 $F$ 的最高次系数在 $t=0$ 消失，仍可提取这个 monic 有限 Hensel 因子；$U$ 的最高次系数可以被 $t$ 整除，不影响 $U(0,1)$ 为单位。

记 $G$ 的不同根为 $\psi_1,\ldots,\psi_{c_F}$，都满足 $\psi_i(0)=1$。引理 1 给
$$
\mathscr D(\psi_i)\ne0\qquad(1\le i\le c_F).
\tag{10}
$$

## 3. 判别式支付全部分支的隐式微分损失

设
$$
h_i=\operatorname{ord}_t(\psi_i-\rho_{<s})\in\mathbb Q_{>0}\cup\{\infty\},
\qquad H_i=\min(h_i,s).
$$
因为 $A$ 恰含一个 $t$，在 (3) 中比较两个单位分支，准确有
$$
\operatorname{ord}_t\mathscr D(\psi_i)\ge H_i-1.
\tag{11}
$$
的确，差值的两次导数至多损失两阶，而二阶项的 $A$ 补回一阶；其余项的损失不超过一阶。二次误差的阶至少 $2H_i-1\ge H_i-1$。再用 (5) 即得 (11)，也覆盖 $h_i\ge s$ 或 $h_i$ 为非整数的情形。

继续用 R461 的真实隐式微分多项式，记 $D_F=F_Y$：
$$
\begin{aligned}
K_F={}&A\{Y[-F_{tt}D_F^2+2F_{tY}F_tD_F-F_{YY}F_t^2]-F_t^2D_F\}\\
&-BYF_tD_F^2-CY^2D_F^3.
\end{aligned}
\tag{12}
$$
在每个分支上恒有
$$
K_F(t,\psi_i)=F_Y(t,\psi_i)^3\mathscr D(\psi_i).
\tag{13}
$$
由 (10)，$F\nmid K_F$，所以
$\mathcal R_F(t)=\operatorname{Res}_Y(F,K_F)$ 非零，且原完整次数给
$$
\deg_t\mathcal R_F\le a_F(6b_F-1)+2b_F.
\tag{14}
$$

不能在切向分支上把 $F_Y$ 当单位。这里保留其准确总阶。由 (9)，
$$
F_Y(t,\psi_i)=G_Y(t,\psi_i)U(t,\psi_i),
$$
其中每个 $U(t,\psi_i)$ 为单位。因此
$$
\sum_i\operatorname{ord}_tF_Y(t,\psi_i)
=\operatorname{ord}_t\operatorname{Disc}(G)\ge c_F-1.
\tag{15}
$$
最后一个界可直接在完整有限自由环
$k[[t]][Y]/(G)$ 上证明：乘 $G_Y$ 的行列式是判别式，模 $t$ 后相当于在
$k[X]/X^{c_F}$ 上乘 $c_FX^{c_F-1}$，该映射恰秩一。因为 $c_F<p$，系数 $c_F$ 是单位，所以该 $c_F\times c_F$ 矩阵的行列式至少含 $t^{c_F-1}$。$G$ 可分保证判别式非零。这同时说明此处用的是所有分支共同的完整判别式，未逐支免费除掉非单位 $F_Y$。

另一方面，(9) 的结果式乘法给
$$
\mathcal R_F=\operatorname{Res}_Y(G,K_F)\operatorname{Res}_Y(U,K_F).
$$
第二个因子属于 $k[[t]]$，不会贡献负赋值；第一个因子是全部 $K_F(t,\psi_i)$ 的乘积。故由 (11)、(13)、(15)，
$$
\begin{aligned}
\operatorname{ord}_t\mathcal R_F
&\ge\sum_i\operatorname{ord}_tK_F(t,\psi_i)\\
&\ge\sum_i H_i-c_F+3(c_F-1)
=\sum_iH_i+2c_F-3.
\end{aligned}
\tag{16}
$$

因为 $U(t,\rho_{<s})$ 是单位，
$\operatorname{ord}_tF(t,\rho_{<s})=\sum_i h_i$。又有
$$
\sum_i\min(h_i,s)\ge\min\left(\sum_i h_i,s\right).
$$
换回与 $\rho_{<s}$ 模 $t^s$ 相同的原 regularized 轴，得到本篇的全部分支界。

**定理 1。** 令
$H_F=\operatorname{ord}_tF(t,g)$，其中只需读取其截断 $\min(H_F,s)$。则
$$
\boxed{\min(H_F,s)
\le a_F(6b_F-1)+2b_F-2c_F+3
\le a_F(6b_F-1)+2b_F+1.}
\tag{17}
$$
这个界不要求横截，也不要求 $F$ 只有一个局部分支。$c_F=1$ 时恢复 R461；$c_F\ge2$ 时，判别式反而给出式中显示的额外改进。它的用途是限制实际低轴接触；未把超出 $s$ 的 regularized 尾误作原 ODE 的自由解。

若 $b_F=1$，仍可使用 R461 的更强有理分支计算：
$$
\boxed{\min(H_F,s)\le4a_F+3.}
\tag{18}
$$
其原分子为 $A(W'U-WU')+BWU-CU^2$，其中对 $F=uY-v$ 取
$U=uv,W=v'u-u'v$，完整次数不超过 $4a_F+2$。径向一次时 $c_F=1$ 自动成立。

## 4. 任意真实首核的全部因子共同受限

取非零真实来源 $P\in\mathcal W_{D,0}$，假定
$\bar P\in\ker\bar J$。记
$\widehat P=d^{C_D}\bar P\in k[t,Y]$。

首先，实际三块的最低行迫使 $t\mid\widehat P$。在 $t=0$ 处，真实 $q_n$ 只允许 $n=0,1,2$，所以
$\widehat P(0,Y)=c_0+c_1Y+c_2Y^2$。三个实际 Gaussian 常数行分别读
$\widehat P$, $aE\widehat P$, $a^2E^2\widehat P/2$ 在 $Y=1$ 的值，其中 $E=Y\partial_Y$。对应矩阵的行列式为 $2$，而 $a,2$ 都是单位，所以 $c_0=c_1=c_2=0$。这正是原来源的角含量，不能用自由矩形替代。

在代数闭剩余域内准确分解
$$
\widehat P=t^r Q\prod_{i=1}^m F_i^{\nu_i},\qquad
r\ge1,\quad Q(0,1)\ne0,\quad F_i(0,1)=0,
\tag{19}
$$
其中 $F_i$ 两两不同、不可约且不等于 $t$；允许 $m=0$。写
$$
a_i=\deg_tF_i,\quad b_i=\deg_YF_i,\quad
c_i=\operatorname{mult}_{Y=1}F_i(0,Y).
$$
所有 $1\le b_i\le D<p$，所以定理 1 均适用。原整个来源次数 (1) 给
$$
\boxed{\sum_i\nu_i a_i\le M_D-r,\qquad
\sum_i\nu_i b_i\le D.}
\tag{20}
$$
真实 $J$ 的第一块给
$$
r+\sum_i\nu_i H_i\ge s,\qquad H_i=\operatorname{ord}_tF_i(t,g).
$$
即使有 $H_i\ge s$，准确截断后仍有
$$
s\le r+\sum_i\nu_i\min(H_i,s).
\tag{21}
$$
故 (17) 给完整的因子逐项必要条件
$$
\boxed{s\le r+\sum_i\nu_i
\{a_i(6b_i-1)+2b_i-2c_i+3\}.}
\tag{22}
$$
这里没有假定某一个因子承担全部高接触，也没有删掉不同分支的重数。

**定理 2。** 若一个整数 $B\ge1$ 满足所有接触因子 $b_i\le B$，则任意这样的真实首核都满足
$$
\boxed{p\le(36B-6)M_D+18D-36B+11.}
\tag{23}
$$
当 $m=0$ 时，“所有接触因子”的条件为空，结论仍成立；此时 (21) 直接给 $r\ge s$。

**证明。** 由 $c_i\ge1$、$b_i\ge1$，有
$2b_i-2c_i+3\le2b_i+1\le3b_i$。所以 (20)–(22) 给
$$
\begin{aligned}
s&\le r+(6B-1)\sum_i\nu_i a_i+3\sum_i\nu_i b_i\\
&\le(6B-1)M_D-(6B-2)r+3D\\
&\le(6B-1)M_D+3D-6B+2.
\end{aligned}
$$
代入 $p=6s-1$ 即得 (23)。$\square$

若 $p>6M_D-1$，纯角情形 $m=0$ 已由 $r\le M_D$ 排除，故确有接触因子。其最大径向次数满足
$$
\boxed{\max_i b_i\ge
\left\lceil\frac{p+6M_D-18D-11}{36(M_D-1)}\right\rceil.}
\tag{24}
$$
分母为正，因为 $M_D\ge4$。在 $D\asymp\sqrt p$ 时，这个下界按 $\sqrt p$ 增长；固定次数因子相乘、全部切向分支或增加小因子的重数，均不能替代所需的一个高径向次数因子。

## 5. 全部接触因子径向一次时的统一排除

若 (19) 中每个 $b_i=1$，用 (18) 取代 (17)，得到
$$
s\le r+\sum_i\nu_i(4a_i+3)
\le4M_D-3r+3D
\le4M_D+3D-3.
$$
因此
$$
\boxed{p\le24M_D+18D-19\le138D+77.}
\tag{25}
$$
这是任意多个不同径向一次因子的结论，允许各自不同的接触阶和任意实际重数；$Q$ 可以包含所有不经过 $(0,1)$ 的高次因子。它不要求首核形状是单一 $t^rF^mQ$，也不要求各一次因子在所有角点都为单位。

R461 对单一一次因子幂保有略强的常数 $138D+59$；本篇 (25) 扩大的是允许的真实因子结构。两者不矛盾，也不把多个不同因子的接触阶错误地合并成一个。

## 6. 原第二核、完整中央和剩余接口

原矩阵仍为
$$
M^{\rm orig}=c_*U_0m_{13}J.
$$
由 R449 的完整精确序列，
$K_2^{\rm red}(M^{\rm orig})\subset\ker\bar J$。所以 (22)–(25) 同时适用于原真正第二核的所有非零约化，不是只对一个试验矩形或自由首核的排除。原最初十三个自由行、两条十三行 carry、$G_2=C_2(J)/\overline H$ 和第三位 Miller 强迫均保留；这里没有对其作删行或免费除 $p$。

本篇没有使用两个原完整中央失败去制造新来源零，也没有给 $F_i$、其导数或任意乘积赋中央零。对于 (24) 允许的高径向次数部分，仍须在同一实际仿射修正格中实现或排除 R459 的非零 normal jet，并比较真实 $\pi\beta_J$ 与完整第二障碍。定理 2 在平衡临界区仍容许 $b_i\asymp\sqrt p$，故没有证明整个相对 $J$ 满秩，也没有达到本课题的跨 $p$ 完成标准。


## 7. 原混合 j 来源的完整扩展

[补充证明](../notes/2026-11-14-r467-mixed-j-original-theta-extension.md)在原 Theta 变量内保留全部 j 列、原 V 的六次成本及 R453 一次整返回。取 N=17D+36J<p、M=floor(11D/2)+4+11J，全部接触因子径向次数至多 B 时，p≤(36B−6)M+6N−36B+11；全部对原 Theta 一次时 p≤234D+480J+77。原真第二核同样受限，J=0 仍优先用本文较强的原 R 坐标界；未排临界高次数，也未新增完整中央零。
