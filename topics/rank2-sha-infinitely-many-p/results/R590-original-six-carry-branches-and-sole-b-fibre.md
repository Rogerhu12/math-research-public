# R590 — 原六支 carry、唯一 B 来源与完整七纤维矩化简

日期：2026-11-14。**状态：已证明。**

本篇把 R536 的同一个测试从三条 $C$ 分支扩成六条；原有限右逆、
全部 $\lambda,\kappa$ 系数和原四输出保持不动。负三支需要的真实
覆盖是 even42 与 even1638，其整个核心和绝对符号在现有射线上付清。

新的完整 $C$ 平均恰杀掉 R572 的 $\sigma^3$ 项。对原所有
$C$ 不动的混合测试，整个六变量来源因而准确只剩
$B=-y_\wp\sigma^3$ 与其真实四伴随；再对这个实际 $B$ 纤维积分，
把同一个 carry 写成单个五变量来源上的七个有界纤维矩。
这保全部隐藏 $Y/W$ 日志，未用伴随质量替代它们。

原六 sigma、原 $\mathcal D_n$ 上的严格零质量及单位首项仍成立。
它们不被偷换成投影后来源在同一 $\mathcal D_n$ 上的断言。
R585 的八条带、旧三支与新六支的差以及整个算术补项同时给出。

## 1. 原规范和实际纯 C 反射

沿用
[R531](R531-hidden-two-frame-native-central-carry.md)、
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R557](R557-third-source-common-carry-zero-mass-and-central-rows.md)、
[R572](R572-original-c-splitting-and-simple-pole-unit.md)、
[R582](R582-original-normtwo-deep-complements-and-five-line-domain.md)、
[R585](R585-original-four-unit-row-and-exact-fibre-cut-correction.md)
的所有普通射线、有限坏集、原周期和实际六输入。
记
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
原输入为 $(\xi_1,\xi_2,\xi_3,x,c,d)$，
$\rho_0=-\nu_\sigma^{\otimes6}/84$。
保
$$
C=(\xi_1-\xi_3+x)/\delta,\quad
D=D_4+c+(2+3\omega)d,\quad F=D+C,\quad
E=F+13C,\quad G=13H_1+(3-2\omega)F,
$$
$$
D_4=\xi_1+\omega^2\xi_2-2\omega\xi_3,\qquad
H_1=-\xi_1+2\xi_2+\omega\xi_3+(1+\omega)x .
\tag{2}
$$
$\pi_4=(Y,W,W',G)$ 始终是 R536 的原完整四输出，
$Y_*\rho_0=S,\ W_*\rho_0=6\delta T$，
$W_2=-\omega^2W-\omega W'$。
原 $C,F$ 正交，范数分别为 $1,13$，且都正交于 $\pi_4$。

对 $\zeta\in\mu_6$ 定义真实输入变换
$$
R_\zeta=I+(\zeta-1)\bar C^{\,t}C,\qquad
CR_\zeta=\zeta C .
\tag{3}
$$
它逐个固定 $F,Y,W,W',G,c,d$，故也固定
$U=c+\omega d,V=c-\omega d$。
特别纯 $C$ 反射
$$
\mathfrak r=R_{-1}=I-\frac23H_0^{\,t}H_0,\qquad
H_0=(1,0,-1,1,0,0)
\tag{4}
$$
在 $(\xi_1,\xi_3,x)$ 上的完整矩阵是
$$
\frac13\begin{pmatrix}1&2&-2\\2&1&2\\-2&2&1\end{pmatrix},
$$
其余三个输入固定。它在当前处是整自同构，
不是只在第一边际上定义的符号。

原第三支 $\eta=\omega^2H_*\rho_0$ 的 $H$ 只作用于 $(c,d)$，
故与所有 $R_\zeta$ 交换。保 R557 的实际身份
$$
(c+(2+3\omega)d)H=2\omega(c-d).
\tag{5}
$$

## 2. 六条实际轴的 entire42 / entire1638 核

令
$$
D_\zeta=F-\zeta C,\qquad E_\zeta=F+13\zeta C .
\tag{6}
$$
所有 $\zeta$ 都有
$$
D_\zeta\perp E_\zeta,\quad
N(D_\zeta)=14,\quad N(E_\zeta)=182,\qquad
D_\zeta,E_\zeta\perp\pi_4.
\tag{7}
$$
对 $\zeta\in\mu_3$，这是原三支，只改了根的排列顺序。
负三支的 $D_\zeta$ 一般不是整数行，不能免费套用 entire14；
本篇统一使用完整整数框架
$$
\boxed{
\mathcal F_\zeta=
(\delta D_\zeta,\ 3E_\zeta,\ 2Y,\ 2W,\ 2W',\ 6G).
}
\tag{8}
$$
它及 $\mathcal F_\zeta H$ 都是 CM 整数矩阵，行列式范数准确为
$$
\boxed{N\det\mathcal F_\zeta=2^{20}3^{10}7^3\,13^2.}
\tag{9}
$$
因此全部原输入、四伴随和 $H$ 后来源都保留；
这不是只查两个边际的度数。

前两行的度数为 $42,1638$。完整 sigma 半特征的检查如下；
数值表示整行中模 $2$ 非零的原 sigma 系数个数。

|$\zeta$|$\delta D_\zeta$|$3E_\zeta$|$\delta D_\zeta H$|$3E_\zeta H$|
|---|---:|---:|---:|---:|
|$1,-1$|4|4|2|2|
|$\omega,-\omega$|6|6|4|4|
|$\omega^2,-\omega^2$|6|6|4|4|

在本 CM 格的 $\mathcal O/2$ 中，三个非零系数都保持原 sigma
奇半特征，故各乘积是标准 even 半特征。
从正支到对应负支，$\delta D$ 只增加一个偶整行，
$3E$ 也只增加一个偶整行；没有被省掉的 flat 特征。
(7) 还使这两轴与全部四伴随的 Gaussian 交叉为零。
所以 (8) 给原联合在
$\mathcal S_{42}\otimes\mathcal S_{1638}$ 张量完整四变量系数格中
的真实身份。

现有 ray 给
$$
g_\pi=\pi_0/\bar\pi_0\equiv3\bmod4,\qquad
g_\pi\equiv1\bmod(27\cdot7\cdot13).
$$
故准确有
$$
\boxed{
g_\pi\equiv43=1+42\bmod84,\qquad
g_\pi\equiv1639=1+1638\bmod3276.
}
\tag{10}
$$
标准 even 空间的完整 Heisenberg 交织在这里为恒等；
中心检查分别是
$$
(43^2-1)/42=44,\qquad
(1639^2-1)/1638=1640,
$$
均为偶数。不能只用模 $N$ 的点置换忽略这个中心。

绝对锚取实际非零的
$$
\Theta(\delta\gamma_7 z)\in\mathcal S_{42},\qquad
\Theta(3\gamma_7\gamma_{13}z)\in\mathcal S_{1638},
\quad \gamma_7=3+\omega,\quad\gamma_{13}=4+\omega .
$$
乘子的范数分别为 $21,819$。原 $\Theta$ 的实际普通核心是
$\beta=-\lambda$；固定、在当前处为单位的 CM 拉回与核心严格交换。
不可约 Heisenberg 表示遂定整个归一标量均为 $-I$。
因此原 $\rho_0,\eta$ 以及它们的纯 $C$ 投影满足
$$
\boxed{
\mu|_{D_\zeta\in p^n}=\beta^n(P_{D_\zeta,\kappa^n})_*\mu,\qquad
\mu|_{E_\zeta\in p^m}=\beta^m(P_{E_\zeta,\kappa^m})_*\mu.
}
\tag{11}
$$
两轴正交，故可同时使用并保完整 $\pi_4$。
这里 $\delta,3$ 是当前处单位，物理归一仍是
$D_\zeta/\kappa^n,E_\zeta$，没有多乘一个周期或尺度因子。
本篇未增加新的 ray。

## 3. 同一个右逆的六支版本和全部算术行

完整保 R536 的已确定多项式
$$
P_p(D,E,G)=\sum_{k+j+\ell=6}a_{kj\ell}D^kE^jG^\ell,\qquad
\widehat P_p=\sum_{k+j+\ell=6}a_{kj\ell}u_jD^kE^jG^\ell,\qquad
u_j=(1+\lambda\kappa^j)^{-1}.
\tag{12}
$$
所有 $a_{kj\ell}$ 的有限 $\lambda,\kappa$ 依赖由原七行整右逆给出，
不重新选系数。对应的
$Q_p(C,F,G)=P_p(F-C,F+13C,G)$ 仍是
$-C^6/8$ 加原十个消去方向。

令
$$
\Gamma_{\zeta,n}
=\{C,F\ {\rm unit},\ F-\zeta C\in p^n\}
=\{D_\zeta\in p^n,E_\zeta\ {\rm unit}\},
$$
$$
q_{\zeta,n}
=\frac{1_{\Gamma_{\zeta,n}}}{b\Omega^6}
 \widehat P_p(D_\zeta/\kappa^n,E_\zeta,G).
\tag{13}
$$
六个根的两两差仅在 $2,3$ 处可能非单位，故当前六支严格不交，
并集准确为
$$
\Gamma_n^{(6)}
=\{C,F\ {\rm unit},\ F^6-C^6\in p^n\}.
\tag{14}
$$
定义
$$
\boxed{
q_n^{(6)}=\frac16\sum_{\zeta\in\mu_6}q_{\zeta,n}
=\frac12(q_n^{(3)}+q_n^{(3)}\circ\mathfrak r),
}
\tag{15}
$$
其中 $q_n^{(3)}$ 是原 R536 的三支测试。

**定理1（原完整四输出不变）。** 对每个 $n\ge1$，
$$
\boxed{
(\pi_4)_*(q_{\zeta,n}\mu)=\beta^n(\pi_4)_*\mu,\qquad
(\pi_4)_*(q_n^{(6)}\mu)=\beta^n(\pi_4)_*\mu .
}
\tag{16}
$$
范围包括原 $\rho_0,\eta$、两者线性组合及本篇的 $C$ 投影。
因此例如
$$
\int q_n^{(6)}\ell\,d\rho_0
=\beta^n(J'_S-6\delta J'_T),
\qquad
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
       -1_{W\ {\rm unit}}\log\langle W\rangle\}.
\tag{17}
$$
完整 Mellin 函数、混合 $\pi_4$ 条件和 $W_2$ 行也相同。

**证明。** 先用 (11) 的 $D_\zeta$ 核准确消去
$D_\zeta/\kappa^n$。随后每个 $E_\zeta^j$ 在单位域的系数是
$1-\beta\kappa^j=1+\lambda\kappa^j$，逐项消去原 $u_j$。
剩下的是同一个
$Q_p(\zeta C,F,G)/(b\Omega^6)$。
原 entire odd3 的 $C^2,C^4,C^5$ 条件矩为零，
$C^6$ 条件矩为 $-8b\Omega^6$ 倍质量，且 $\zeta^6=1$；
所以完整忘 $C$ 后返回原来源。
全部步骤固定 $\pi_4$，不改变 $\ell$ 或其他连续四输出测试。
平均即得第二式。证毕。

$R_\zeta$ 逐项置换 (13)，所以 $q_n^{(6)}$ 在整个 $\mu_6$ 下不变。
原 $\mathcal T$ 满足 $C\mathcal T=\omega^2C,F\mathcal T=F,
G\mathcal T=G$，故原三阶不变性也保留。
旧 $W$ 核固定这些真实伴随，因此保持整个六支测试；
没有删掉运输后的原输入域。

## 4. 完整 C 投影只留下 B，且不删除原奇项补偿

记 $\mathcal P_C$ 为原三阶投影，并定义
$$
\mathcal P_6=\frac16\sum_{\zeta\in\mu_6}(R_\zeta)_*,\qquad
\mu_B=\mathcal P_6\rho_0,\qquad
\mu_P=\mathcal P_C\rho_0-\mu_B .
\tag{18}
$$
使用 R572 的完整真实框架
$$
v=\delta C=\xi_1-\xi_3+x,\quad
Z=\xi_1-\xi_3-2x,\quad Q=\xi_1+\xi_3,\quad r=\xi_2,
$$
并保 $c,d$。纯 $C$ 作用只把 $v$ 乘 $\zeta$。
原 exact 三 sigma 恒等式的三个 $v$ 型分别是
$B=-y_\wp\sigma^3$ 的型 $0$、
$x_\wp\sigma^3$ 的型 $1$、$P_3=\sigma^3$ 的型 $3$。
于是 (18) 在完整联合中准确给
$$
\boxed{
\mu_B=\nu_B(v)\otimes\nu^\flat,\qquad
\nu^\flat=\frac1{42}
(\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
-\nu_{f_3}(Z)\otimes\nu_\Theta(Q))
\otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
}
\tag{19}
$$
其中
$$
\Sigma=\sigma^2,\quad\Theta=x_\wp\sigma^2,\quad
f_1=-x_\wp y_\wp\sigma^6,\quad f_3=-y_\wp\sigma^6 .
$$
同时
$$
\boxed{
\mu_P=\nu_{P_3}(v)\otimes\nu_\sigma(c)\otimes\Lambda_P,
}
$$
$$
\Lambda_P=\frac1{84}
(\nu_{\mathcal H_6}(Z)\otimes\nu_\Theta(Q)
-6b\nu_{f_4}(Z)\otimes\nu_\Sigma(Q))
\otimes\nu_\sigma(r)\otimes\nu_\sigma(d).
\tag{20}
$$
所有常数、原 $b=17$ 和同一个 $\Omega$ 均保持 R572 规范。
这里没有将 $\Lambda_P$ 或 (19) 的其余变量取质量。

若 $g$ 是任意在纯 $C$ 下不动的完整连续测试，则
$$
\boxed{
\rho_0(q_n^{(6)}g)
=\mu_B(q_n^{(6)}g)=\mu_B(q_n^{(3)}g),
}
\tag{21}
$$
$$
\boxed{
\rho_0(q_n^{(3)}g)-\rho_0(q_n^{(6)}g)
=\mu_P(q_n^{(3)}g).
}
\tag{22}
$$
前式用来源和六支平均的不变性；后式保原 odd 项的整个贡献。
原 $c,d,U,V$ 的深、单位切集以及全部 $Y/W$ log 都可放入 $g$。
它们一般不只是 $\pi_4$ 测试，所以 (22) 右边不能单域赋零。

若 $g$ 只依赖 $\pi_4$，则 (16) 和 $P_3(0)=0$ 给
$$
\boxed{\mu_P(q_n^{(3)}g)=0.}
\tag{23}
$$
这才是旧三支与新六支在完整算术行上相同的原因。

$R_\zeta$ 是保持第一 $Y/W$ 的真实伴随操作，在清除同一固定
$3$ 覆盖后，与这些第一轴上的实际 CM 纤维、角平均逐项交换；
交叉 Gaussian 项仍为零。故原 S/new/Href/T 条件行按真实投影
继续保留，原参考质量及其未知导数不改变。这里不从 (19) 的
分离给任何新的辅助来源赋中央零。

## 5. 原网格的零质量与单位首项：量词仍在原 rho0

保原真实域
$$
\mathcal D_n=\{\xi_1,\xi_2,\xi_3,c,d\in p^n,\ x\ {\rm unit}\}.
$$
其自由 $x$ 系数为
$$
F_x=C_x=1/\delta,\qquad
(D_\zeta)_x=(1-\zeta)/\delta .
$$
只有 $\zeta=1$ 的系数为零，其余五个都是当前处单位。
因此在**原来源、原域**上逐点有
$$
\boxed{
q_n^{(6)}|_{\mathcal D_n}=q_{1,n}/6
=\frac12q_n^{(3)}|_{\mathcal D_n}.
}
\tag{24}
$$
R536 的七行精确右逆不变，故
$$
\int_{\mathcal D_n}q_n^{(6)}a(x)\,d\rho_0=0
\tag{25}
$$
对原自由 $x$ 的任意有界连续测试 $a$ 成立。
这来自同一有限质量多项式逐系数为零，包含全部常数 log 项。

对 $L=Y,W,W_2$，原首项的准确式现在为
$$
\boxed{
\int_{\mathcal D_n}d_p\log\langle L\rangle q_n^{(6)}\,d\rho_0
=\frac{\beta^{5n}}6\,\mathcal A_L(\kappa^n),
\qquad
[T]\mathcal A_L=\frac{d_p}{b}\alpha_L(1-\beta\kappa),
}
\tag{26}
$$
其中固定原常数仍是
$$
\alpha_Y=-\frac{36+54\omega}{49},\quad
\alpha_W=-\frac{180+102\omega}{49},\quad
\alpha_{W_2}=-\frac{60+6\omega}{49}.
$$
它们及 R536 已付的归一差均为当前处单位；同一高阶界因 $6$
可逆不变。因此三行及两个原归一差仍对每个 $n\ge1$ 准确赋值 $n$。
原 $\mathcal T\mathcal D_n$、旧 $W$ 深管及其全部输入转置也保留，
只是 (45) 的 $1/3$ 变为 $1/6$。

但是 $\mathcal D_n$ 不由 $\mathfrak r$ 保持。
例如对原 $Y/W$ 的 $C$ 不动测试 $f$，
$$
\boxed{
\int_{\mathcal D_n}q_n^{(6)}f\,d\mu_B
=\frac16\sum_{\zeta\in\mu_6}
\int_{R_\zeta^{-1}\mathcal D_n}q_n^{(6)}f\,d\rho_0.
}
\tag{27}
$$
六个右域分别属于六个真实 carry，严格不交；
只有其中原 $\mathcal D_n$ 的值由 (26) 给出。
(26) 没有证明 (27) 非零，更不能据此删除另外五个域或其余补域。

## 6. 把 C 完整积分成同一个七纤维矩

令 $\nu_{B_C}=[1/\delta]_*\nu_B$；其生成函数是 $B(z/\delta)$，
质量为一，第六矩为 $-8b\Omega^6$。
在真正五个坐标 $(Z,Q,r,c,d)$ 上，
$$
\begin{aligned}
A_0&=(-2+\omega)Z/2+(4+3\omega)Q/2+2\delta r,\\
J_0&=\delta Z/6+(1-2\omega)Q/2+\omega^2r,\\
H_1&=\omega^2Z/2+(\omega-1)Q/2+2r,
\end{aligned}
$$
$$
\boxed{
F=J_0+c+(2+3\omega)d,\quad G=13H_1+(3-2\omega)F,\qquad
Y=A_0+c+2d,\quad W=A_0+3\delta c+4d .
}
\tag{28}
$$
这些是原观察的完整物理式，不含 $C$；所有隐藏条件可按原式使用。

对 $0\le s\le6$ 定义同一实际纤维矩
$$
\boxed{
b_{n,s}(F)=
\int_{C\in F+p^n\mathcal O}
\left(\frac{F-C}{\kappa^n}\right)^s\,d\nu_{B_C}(C).
}
\tag{29}
$$
$\kappa^n\mathcal O=p^n\mathcal O$，所以被积函数整有界。
这些是真实 $B$ 测度在指定同一 coset 上的矩，不是待选的七个常数。

**定理2（完整五变量实际权）。** 对任意连续
$\varphi(Z,Q,r,c,d)$，
$$
\boxed{
\int q_n^{(6)}\varphi\,d\rho_0
=\int\mathcal W_n(F,G)\varphi\,d\nu^\flat,
}
\tag{30}
$$
其中单个完整有界权是
$$
\boxed{
\begin{aligned}
\mathcal W_n(F,G)
={}&\frac{1_{F\ {\rm unit}}}{b\Omega^6}
\sum_{k+j+\ell=6}a_{kj\ell}u_jG^\ell
\sum_{t=0}^{j}\binom jt
(14F)^{j-t}(-13\kappa^n)^t\,b_{n,k+t}(F).
\end{aligned}}
\tag{31}
$$
这里 $k+t\le6$；原十列系数、全部 $u_j$ 和原负归一幂未简化。

**证明。** (21) 先把来源换成实际 (19)。
$\nu_{B_C}$ 在整个 $\mu_6$ 下不变；其余五变量和 $\varphi$ 不动。
所以每条 $C$ 分支的完整积分相同，六支平均准确等于 $\zeta=1$
的一条，无额外 $1/6$。
在该支设 $T=(F-C)/\kappa^n$，则
$$
D/\kappa^n=T,\qquad E=14F-13\kappa^nT .
$$
逐项展开 (12) 的 $E^j$ 后，对实际 coset 积分，正好得到 (31)。
$F$ 单位使该 coset 内 $C$ 自动单位，故原两个单位条件均已付，
没有把它们删成一个边际假设。证毕。

纤维矩还满足两条准确式：
$$
b_{n,s}(F+\kappa^nt)
=\sum_{j=0}^s\binom sj t^{s-j}b_{n,j}(F)\quad(t\in\mathcal O),
$$
$$
\boxed{b_{n+1,s}(\kappa F)=\beta\,b_{n,s}(F).}
\tag{32}
$$
第一式是在同一 coset 内展开分子；第二式用真实 $B_C$ 深核心，
并保其外部 $\beta$。这证明 (31) 是每个 residue 球上的完整
有限多项式权，且给它在深纤维之间的准确返回。
不把单位纤维的值猜成 $\beta^n$。

由 (16)、(30)，有整个来源身份
$$
\boxed{(\pi_4)_*(\mathcal W_n\nu^\flat)
=\beta^n(\pi_4)_*\nu^\flat .}
\tag{33}
$$
(33) 只忘去剩余 $F$ 方向；不能把它加强成
$\mathcal W_n\nu^\flat=\beta^n\nu^\flat$。
完整中央是
$\int\mathcal W_n\ell\,d\nu^\flat=\beta^n(J'_S-6\delta J'_T)$。

## 7. R585 的八条带、全部原补项和旧奇项准确相消

仍令
$$
\mathscr A_4=\{c,d,U,V\ {\rm unit}\},\qquad A_4=1_{\mathscr A_4}.
$$
原 $F=0$ 投影的四行是
$$
c_0=c-F/13,\quad d_0=d+(1+3\omega)F/13,\quad
U_0=U-2(2+\omega)F/13,\quad V_0=V-2\omega^2F/13 .
$$
置 $\mathsf A_0=1_{\{c_0,d_0,U_0,V_0\ {\rm unit}\}}$；
这里特用不同字体，避免与 (28) 的观察 $A_0$ 混淆。
$\mathsf A_0$ 是原 $\pi_4$ 的真实条件，R585 的八条变化域全保持。

令
$$
Q_{A,n}^{(6)}=\rho_0(A_4q_n^{(6)}\ell),\qquad
J_A=\rho_0(A_4\ell)=\nu^\flat(A_4\ell).
$$
完整 $F$ 核保持 (19)，而原 $F$ 比较证明只用了 (33)。
故 R585(15) 现在准确成为
$$
\boxed{
Q_{A,n}^{(6)}-\beta^nJ_A
=\int_{\{F\ {\rm unit}\}}
(\mathcal W_n-\beta^n)(A_4-\mathsf A_0)\ell\,d\nu^\flat .
}
\tag{34}
$$
右边仍按原四个第一次失败条件分为八个完整条带。
原 carry 外的 $-\beta^n$ 部分没有消失：
在 (31) 中 carry 已被逐纤维准确积分，(34) 仍完整保留
$-\beta^n1_{F\ {\rm unit}}$ 项。
不能把 $\mathcal W_n$ 的某个纤维质量替代整个右边。

对 $\epsilon=c,d,U,V$ 定义全部真实补项
$$
C_{\epsilon,n}^{(6)}
=\rho_0(1_{\epsilon\in p}q_n^{(6)}\ell),\qquad
I_n^{(6)}=\rho_0(1_{c,d\in p}q_n^{(6)}\ell).
$$
它们都可按 (30) 写成同一 $\nu^\flat$ 上的原实际条件。
四条线两两的深交集均为 $\{c,d\in p\}$，所以完整总行仍是
$$
\boxed{
\beta^n(J'_S-6\delta J'_T)
=Q_{A,n}^{(6)}
+C_{c,n}^{(6)}+C_{d,n}^{(6)}
+C_{U,n}^{(6)}+C_{V,n}^{(6)}-3I_n^{(6)} .
}
\tag{35}
$$
原 native 的 $L$ 单位条件并未增加或丢失；
R585 的真实集合恒等式仍给
$\mathcal N_n^{(6)}+U_n^{(5,6)}=3Q_{A,n}^{(6)}$。

最后将旧三支同名项减去新六支项。
由 (22)，每一个差恰为 $\mu_P$ 上原 $q_n^{(3)}\ell$ 的同一切集。
由 (23)，这些差在整个分区中准确满足
$$
\boxed{
\mu_P\!\left(
q_n^{(3)}\ell\left[
A_4+1_{c\in p}+1_{d\in p}+1_{U\in p}+1_{V\in p}
-3\,1_{c,d\in p}\right]\right)=0 .
}
\tag{36}
$$
括号恒等于一；这是原未知 odd 项在完整算术总行中的真正抵消。
各个 native、四单位或深补项并未被单独赋零。

因此 (34)–(36) 是把旧测试完整接到同一个五变量
$f_1\otimes\Sigma-f_3\otimes\Theta$ 来源的实际关系。
所有 $Y/W$ 单位与日志、$F/G$ 权、原 $q$ 的 $p$ 依赖及共同深补项
都保留。仍须在这些同一完整行上证明最终消去或非消失；
(26) 的一个原子域非零、$B$ 的单位质量以及 (33) 的条件返回
都没有完成这一剩余步骤。

## 8. 精确证书

- [check-r590-original-six-carry-branches-and-sole-b-fibre.js](../scripts/check-r590-original-six-carry-branches-and-sole-b-fibre.js)
- [check-r590-original-six-carry-branches-and-sole-b-fibre.json](../scripts/check-r590-original-six-carry-branches-and-sole-b-fibre.json)

脚本以 BigInt 的 $\mathbf Q(\omega)$ 算术保存六套完整框架、
$H$ 后整数格、所有 half-character 计数、行列式、whole 中心与
两个真实绝对锚、实际纯 $C$ 反射、所有五变量观察及 (31) 的
全部有限展开系数。它直接使用原 (2)，没有扫描试验素数。
无穷深度、来源投影、原网格的量词和全补域身份由正文证明。

