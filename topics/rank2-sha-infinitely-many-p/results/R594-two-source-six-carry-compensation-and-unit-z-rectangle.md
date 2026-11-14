# R594 — 同一六支 q 的双来源补偿、整九行右逆与真实 Z 单位矩形

日期：2026-11-14。**状态：已证明。**

本篇在 R590 的同一个六支 carry 家族中作明确的有限补偿。
原 $S/T$ 的整个四输出返回保持；原六 sigma 来源、实际 $B$ 投影来源
以及两者之差，对同一个测试、同一个原 $\mathcal D_n$ 的
未归一 $Y-W$ 对数差都准确有赋值 $n$。
其中 $B$ 来源的质量没有被赋零：两个观察的常数 log 在被积函数中
本来就相同，完整相减后消失。

补偿由真实 $9\times20$ 线性问题给出，显示的多项式右逆支付全部
$\lambda,\kappa$，只再删一个固定整数的有限素因子。
一个可能引入新负矩的项被准确置零；没有用正矩替代它。

随后将六个真实网格合并，在同一 $\nu^\flat$ 上得到
$\{Z\ {\rm unit},Q,r,c,d\in p^n\}$ 的完整非零矩形。
原 $q$ 的改变量和矩形外全部补域均显示保留；本篇不从矩形非零
推出原整个中央非零。

## 1. 同一个来源、同一个 carry 与扩大后的中性方向

沿用
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)、
[R557](R557-third-source-common-carry-zero-mass-and-central-rows.md)、
[R572](R572-original-c-splitting-and-simple-pole-unit.md)、
[R585](R585-original-four-unit-row-and-exact-fibre-cut-correction.md)、
[R590](R590-original-six-carry-branches-and-sole-b-fibre.md)
的完整普通射线和全部原周期。
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad b=17,\qquad
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d_p=p-1,\quad\Omega\in\mathcal O^\times .
\tag{1}
$$
保原六输入、$\rho_0=-\nu_\sigma^{\otimes6}/84$、
$\mu_B=\mathcal P_6\rho_0$，以及原 $C,F,D,E,G,Y,W,W'$。
特别
$$
D=F-C,\quad E=F+13C,\quad \pi_4=(Y,W,W',G),
$$
$$
\ell=d_p\{1_{Y\ {\rm unit}}\log\langle Y\rangle
             -1_{W\ {\rm unit}}\log\langle W\rangle\}.
\tag{2}
$$
$Y_*\rho_0=S,\ W_*\rho_0=6\delta T$，没有改变原算术归一。

R590 已付六支的 entire42、entire1638 核和全部半特征。
其投影来源准确为
$$
\boxed{
\mu_B=\nu_B(v)\otimes\nu^\flat,\qquad
\nu^\flat=\frac1{42}
(\nu_{f_1}(Z)\otimes\nu_\Sigma(Q)
-\nu_{f_3}(Z)\otimes\nu_\Theta(Q))
\otimes\nu_\sigma(r)\otimes\nu_\sigma(c)\otimes\nu_\sigma(d),
}
\tag{3}
$$
其中 $v=\delta C$，所有五变量是 R572/R590 的实际物理坐标。
$B=-y_\wp\sigma^3,\Sigma=\sigma^2,\Theta=x_\wp\sigma^2$、
$f_1=-x_\wp y_\wp\sigma^6,f_3=-y_\wp\sigma^6$ 保原规范。

在 $C=v/\delta$ 上，$B$ 的实际测度 $\nu_{B_C}$ 满足
$$
m_{B_C}(0)=1,\quad m_{B_C}(1)=\cdots=m_{B_C}(5)=0,\quad
m_{B_C}(6)=-8b\Omega^6 .
\tag{4}
$$
所以现在可使用完整二十个中性方向
$$
\boxed{\phi_{ij}=C^iF^jG^{6-i-j},\qquad
1\le i\le5,\quad0\le j\le6-i.}
\tag{5}
$$
按 $i$ 递增、再按 $j$ 递增排列。
定义新的多项式
$$
\widetilde Q_p=-C^6/8+\sum_{i,j}x_{ij,p}\phi_{ij},\qquad
\widetilde P_p(D,E,G)
=\widetilde Q_p((E-D)/14,(E+13D)/14,G).
\tag{6}
$$
其每个中性项在 (3) 上完整忘 $C$ 后为零。
因此对于 $\mu_B$ 的任意其余五输出测试，
$\widetilde Q_p/(b\Omega^6)$ 准确返回原来源。

原 R536 的 $q$ 及其数值系数保持原定义；
本篇用波浪号明确区分新测试。
新增 $C^1,C^3$ 方向的中性依赖本篇的完整六阶平均，
不声称它们在未平均的原单支上分别中性。

## 2. B 投影来源在原坐标上的完整 odd9 核

R590 的纯 $C$ 变换是
$$
R_\zeta=I+(\zeta-1)\bar C^{\,t}C,\qquad \zeta\in\mu_6 .
$$
在原三个坐标 $(\xi_1,\xi_3,x)$ 上共同取 $[3]$；
其余 $\xi_2,c,d$ 不变。对每个 $R_\zeta$，
完整六行矩阵均整，Gram 为
$$
\operatorname{diag}(9,1,9,9,1,1).
\tag{7}
$$
对 $\zeta=\pm1$，三个被覆盖行各有一个模二非零 sigma 系数；
对其余四根，各有三个。全部是标准 odd 半特征，
交叉 Gaussian 项全零。因此 $\mu_B$ 确实属于对应的完整
$\mathcal S_9^{\rm odd}\otimes\mathcal S_1^{\rm odd}
\otimes\mathcal S_9^{\rm odd}\otimes\mathcal S_9^{\rm odd}
\otimes\mathcal S_1^{\rm odd}\otimes\mathcal S_1^{\rm odd}$ 格。

现 ray 已有 $g_\pi\equiv1\bmod18$。
entire odd9 的完整交织为恒等，真实锚 $\sigma(3z)$ 支付绝对
外部核心 $\beta$。原 degree1 sigma 同样为 $\beta$。
所以在原坐标上，$\mu_B$ 的每个单轴完整核心都是 $\beta$。
特别对
$$
\mathcal D_n=\{\xi_1,\xi_2,\xi_3,c,d\in p^n,\ x\ {\rm unit}\}
$$
可同时用五个深核心：
$$
\boxed{
\mu_B|_{\mathcal D_n}
=\beta^{5n}[\kappa^n,\kappa^n,\kappa^n,1,\kappa^n,\kappa^n]_*
(\mu_B|_{x\ {\rm unit}}).
}
\tag{8}
$$
相同式对 $\rho_0$ 成立；原 $x$ 轴核心也为 $\beta$。
这次是对投影后整个来源的独立证明，不是把 R536 的原网格结论
直接移给 $\mu_B$。

## 3. 九个真实约束及 B 来源的完整第一行

写
$$
\widetilde P_p=\sum_{k+j+\ell=6}a_{kj\ell}D^kE^jG^\ell,\qquad
u_j=(1+\lambda\kappa^j)^{-1},\qquad
\widehat{\widetilde P}_p=\sum a_{kj\ell}u_jD^kE^jG^\ell.
\tag{9}
$$
在原五深坐标中，保 R536 的准确分解
$$
D=TD_f,\quad E=e_0x+TE_f,\quad G=g_0x+TG_f,
\qquad
e_0=(-14-28\omega)/3,\quad g_0=(32+31\omega)/3 .
$$
$D_f,E_f,G_f$ 是原三行删去 $x$ 列所得的五变量行。
记 $\mathfrak C=[\xi_1\xi_2\xi_3cd]$。原六条质量行仍为
$$
\begin{aligned}
\mathcal M_k={}&
\sum_{j+\ell=6-k}a_{kj\ell}u_j
\{j e_0\,\mathfrak C(D_f^kE_f^{j-1}G_f^\ell)
+\ell g_0\,\mathfrak C(D_f^kE_f^jG_f^{\ell-1})\},
\\[-2pt]
&\hspace{8cm}0\le k\le5 .
\end{aligned}
\tag{10}
$$
负指数项按其零前系数省去。再定义实际系数
$$
\boxed{L_k=\sum_{j+\ell=6-k}a_{kj\ell}u_je_0^jg_0^\ell .}
\tag{11}
$$
R536 原首项行就是 $L_4$。此外准确有
$$
\mathcal M_5=-240(2+3\omega)L_5 .
\tag{12}
$$
当前系数为单位，故 $\mathcal M_5=0$ 严格推出 $L_5=0$。

置
$$
\mathscr E_j=1-\beta\kappa^j=1+\lambda\kappa^j,\qquad
\boxed{\alpha_\Delta=\alpha_Y-\alpha_W=48(3+\omega)/49.}
\tag{13}
$$
$N\alpha_\Delta=2304/343$，在全部当前普通处为单位。

**引理1（真实 B 网格的第一对数差）。**
若 $\mathcal M_5=0$ 且 $a_{600}=0$，则在 (8) 归一后的原网格上，
同一六支测试的 $Y-W$ 对数差第一系数准确为
$$
\boxed{
\frac{d_p}{6b}\mathcal L_B,\qquad
\mathcal L_B=c_2\mathscr E_3L_2+c_3\mathscr E_2L_3
                              +c_4\mathscr E_1L_4,
}
\tag{14}
$$
其中固定完整系数是
$$
\boxed{
c_2=\frac{-16-24\omega}{441},\qquad
c_3=\frac{-16+4\omega}{147},\qquad
c_4=\frac{80+8\omega}{49}.
}
\tag{15}
$$

**证明。** 在原网格的真正解析参数 $T$ 下，
$$
Y=\bar\gamma x+TZ_Y,\qquad W=\bar\gamma x+TZ_W,\quad
\bar\gamma=2-\omega,\qquad Z_Y-Z_W=-2((1+3\omega)c+d).
$$
当 $x$ 单位、$T\in p\mathcal O$ 时，两个观察始终单位，
且两个常数 log 在被积函数中准确相同。因此第一项只来自
$$
T(Z_Y-Z_W)/(\bar\gamma x).
\tag{16}
$$
$\widehat{\widetilde P}_p$ 的一次 $T$ 变化乘的是零常数对数差，
故不贡献。

原三 sigma 经完整 $C$ 平均的最低六次生成多项式准确为
$$
\boxed{
\frac1{42}(z_Zz_Q^2-z_Z^3)z_rz_cz_d,\qquad
z_Z=(z_1-z_3-2z_x)/6,\quad z_Q=(z_1+z_3)/2 .
}
\tag{17}
$$
这是 R572 整个来源身份的最低齐次项，也可由六个 $R_\zeta$ 的
全部线性 sigma 因子直接相加，附证书逐项核过。

把原生成变量代成 $tD+s(Y-W)+z e_x$，(17) 中的各项是
$$
z_Z=(\delta t-2z)/6,\quad z_Q=(1-2\omega)t/2,\quad
z_r=\omega^2t,\quad
z_c=t-2(1+3\omega)s,\quad z_d=(2+3\omega)t-2s .
\tag{18}
$$
取 $t^ksz^{5-k}$ 并乘 $k!(5-k)!/\bar\gamma$，
$k=0,1$ 为零；$k=2,3,4$ 正好给 (15)，
而 $k=5$ 的系数为 $c_5=-80\delta/21$。
它乘 $L_5=0$，完整消失。

正次数的 $x$ 单位限制由第2节的实际核心给
$\mathscr E_{5-k}$，不是把正矩当成负矩。
当 $k=6$ 时本会出现 $x^{-1}$ 的真实单位矩；
唯一相应系数是 $L_6=u_0a_{600}$。
假设 $a_{600}=0$ 将该项整条消掉，没有给它猜非零或零值。
其余所用总矩次数准确为六，所以 (17) 已给全部正矩；
共同 $\Omega^6$ 与原归一 $b\Omega^6$ 相消。
六支在原 $\mathcal D_n$ 上只有 $\zeta=1$，外部 $1/6$ 保留。
这证明 (14)。证毕。

我们要求的九个真实条件现在是
$$
\boxed{
(\mathcal M_0,\ldots,\mathcal M_5,\ L_4,\ a_{600},\ \mathcal L_B)
=(0,0,0,0,0,0,\ 1,\ 0,\ 2\alpha_\Delta).
}
\tag{19}
$$
这包含原六 sigma 网格的六条质量消去和原单位首项，
同时完整支付 $B$ 来源的指定第一行。

## 4. 显示的 9×20 整右逆与全部 lambda/kappa

对 (5) 二十列应用 (19) 左边的真实九行，得 $A_p$；
右端减去固定 $-C^6/8$ 的九行，得 $b_p$。
其每一项都是 (9)–(15) 定义的明确有限 CM 代数式。

置 $\tau=(1+\lambda)^{-1}$。
因为 $u_0=\tau$，$u_j\equiv1\bmod p$（$j>0$），
且 $\mathscr E_1,\mathscr E_2,\mathscr E_3\equiv1\bmod p$，
准确有
$$
A_p\equiv A(\tau)=A_++\tau A_0\pmod p .
\tag{20}
$$
这里第八行 $a_{600}$ 没有乘 $u_0$；
它在 $A_+$ 中。附证书按原多项式直接构造这两个 $9\times20$
固定矩阵，未由列数猜其秩。

**引理2（完整多项式右逆）。** 存在显示的固定
$\mathsf B_0,\mathsf B_1\in M_{20,9}(\mathbf Q(\omega))$，满足
$$
\boxed{
A_+\mathsf B_0=-I_9,\qquad
A_+\mathsf B_1+A_0\mathsf B_0=I_9,\qquad
A_0\mathsf B_1=0 .
}
\tag{21}
$$
全部矩阵已保存在本篇 JSON；脚本从原二十个多项式重建并精确验证。

**构造和证明。** 将 (21) 的每个右端列写成同一个
$27\times40$ 的 CM 线性系统，按列从零起作准确消元。
实际秩为 $23$，主元列是
$$
0,1,2,3,4,5,6,7,8,9,10,11,12,14,\ 
20,21,22,23,24,25,26,27,29 .
$$
其余变量取零，得到两矩阵。
把它们代回，三个完整矩阵等式逐项成立。
这是特征零身份，包括所有九个右端列，不是一个试验素数上的秩。

两矩阵所有有理系数分母的最小公倍数为固定整数
$$
\boxed{
D_{594}=
12059737281753537088206344067469144307697108994059921290070191037277435690768800.
}
\tag{22}
$$
它只依赖原固定行；本篇再删除 $p\mid D_{594}$ 的有限素数。
已有无限 ray、全部旧坏集继续保持，故仍有无穷普通素数。

由 (21) 得显示右逆
$$
\boxed{
\mathsf B(\tau)=\frac{\mathsf B_0+\tau\mathsf B_1}{\tau-1},
\qquad A(\tau)\mathsf B(\tau)=I_9 .
}
\tag{23}
$$
原 R410 给 $1+\lambda$ 单位，
$\tau-1=-\lambda/(1+\lambda)$ 也是单位，所以 (22) 外
$\mathsf B(\tau)$ 整。

最后用**实际完整**矩阵而非其余式：
$$
\boxed{
N_p=A_p\mathsf B(\tau)\equiv I_9\pmod p,\qquad
x_p=\mathsf B(\tau)N_p^{-1}b_p .
}
\tag{24}
$$
$N_p$ 是通常的 $9\times9$ 整矩阵，行列式模 $p$ 为一，
故有整逆。于是 $A_px_p=b_p$，全部二十个系数整，
(19) 对完整 $\lambda,\kappa$ 精确成立。证毕。

(24) 不需要一个随 $p$ 变化的新射线条件，
也没有把 $u_j$ 或 $\mathscr E_j$ 先改成一后沿用近似系数。

## 5. 新六支测试保持原整个算术来源

用 (6)、(24) 的新多项式定义
$$
\boxed{
\widetilde q_n=
\frac1{6b\Omega^6}\sum_{\zeta\in\mu_6}
1_{\{D_\zeta\in p^n,E_\zeta\ {\rm unit}\}}\,
\widehat{\widetilde P}_p(D_\zeta/\kappa^n,E_\zeta,G).
}
\tag{25}
$$
所有域、实际坐标及 $\kappa^{-n}$ 保 R590 原定义。
此测试整有界，且在完整纯 $C$ 六阶群及原 $\mathcal T$ 下不变。

对 $\mu_B$，先用原 $D_\zeta$ 核，再用整个 $E_\zeta$ 单位逆，
最后用 (4)，每一支都完整返回 $\beta^n\pi_{4*}\mu_B$。
对原 $\rho_0$，六支测试和全部 $\pi_4$ 观察在纯 $C$ 下不动，
所以先作真实 $\mathcal P_6$ 即归到 $\mu_B$。从而
$$
\boxed{
(\pi_4)_*(\widetilde q_n\rho_0)
=\beta^n(\pi_4)_*\rho_0,\qquad
(\pi_4)_*(\widetilde q_n\mu_B)
=\beta^n(\pi_4)_*\mu_B .
}
\tag{26}
$$
同一证明保原 $\eta$、其 $C$ 投影及已付第一轴算术投影；
其整个 $B_C$ 条件矩和 whole42/1638 核已由 R590 支付。

原 R590 六支测试 $q_n^{(6)}$ 的系数没有被改写。
两测试的完整差严格满足
$$
\boxed{
(\pi_4)_*((\widetilde q_n-q_n^{(6)})\rho_0)=0 .
}
\tag{27}
$$
这只是在整个四输出上的零来源；任意子域的测试差仍须保留。
旧测试的额外首项记录不能直接套给新系数。

## 6. 两个真实来源同一网格上的非零，以及完整 log 质量

在原 $\mathcal D_n$ 上，(25) 只有 $\zeta=1$。
令 $\mathcal H_\mu(T)$ 是在
$x$ 单位、其余五个变量尚未深缩放的完整来源 $\mu$ 上，
对
$$
\frac{d_p}{6b\Omega^6}
\widehat{\widetilde P}_p(D_f,e_0x+TE_f,g_0x+TG_f)
\log\frac{\bar\gamma x+TZ_Y}{\bar\gamma x+TZ_W}
\tag{28}
$$
积分。实际两个单位条件在 $T\in p\mathcal O$ 下自动成立。
由 (8) 及原 sigma 核，
$$
\boxed{
\int_{\mathcal D_n}\widetilde q_n\ell\,d\mu
=\beta^{5n}\mathcal H_\mu(\kappa^n),
\qquad \mu=\rho_0,\mu_B,\rho_0-\mu_B .
}
\tag{29}
$$

原六条 $\mathcal M_k=0$ 使 $\rho_0$ 的同一网格质量及
任意自由 $x$ 常数 log 行严格为零；$L_4=1$ 保原第一项。
引理1和 (19) 则给第二来源的真实第一项。
准确有
$$
\boxed{
\begin{aligned}
[T]\mathcal H_{\rho_0}
 &=\frac{d_p}{6b}\alpha_\Delta(1-\beta\kappa),\\
[T]\mathcal H_{\mu_B}
 &=\frac{d_p}{6b}\,2\alpha_\Delta,\\
[T]\mathcal H_{\rho_0-\mu_B}
 &=-\frac{d_p}{6b}\alpha_\Delta(1+\beta\kappa).
\end{aligned}}
\tag{30}
$$
三个系数都在当前普通处为单位。

这里没有将 $\mu_B$ 的质量赋零。
例如将 (28) 去掉对数及 $d_p$ 后，归一网格的零阶质量准确为
$$
\boxed{
\frac{1-2\omega}{189b}
\{\mathscr E_3L_3-2\delta\mathscr E_2\}.
}
\tag{31}
$$
它来自完整 $B$ 最低六次项，使用了 $L_4=1,L_5=L_6=0$，
一般没有零理由。单独 $Y$ 或单独 $W$ 的
$\log\langle\bar\gamma x\rangle$ 项也须保持。
本篇使用的是原未归一 $Y-W$ 差，其两个常数 log 在 (28)
中逐点相消，因而不依赖 (31) 是否为零。

所有来源和新系数整有界，唯一的 log 分母是其次数。
因此
$$
v_p([T^r]\mathcal H_\mu)\ge-\lfloor\log_pr\rfloor .
$$
当 $T=\kappa^n$、$r\ge2$、$n\ge1$、$p\ge71$ 时，整条尾属于
$p^{2n}\mathcal O$。包括可能出现的更高负权单位矩在内，
都只是该完整有界尾的一部分；没有被单独赋值。

结合 (29)–(30)，得到
$$
\boxed{
v_p\!\left(\int_{\mathcal D_n}\widetilde q_n\ell\,d\rho_0\right)
=v_p\!\left(\int_{\mathcal D_n}\widetilde q_n\ell\,d\mu_B\right)
=v_p\!\left(\int_{\mathcal D_n}\widetilde q_n\ell\,d(\rho_0-\mu_B)\right)
=n
}
\tag{32}
$$
对每个 $n\ge1$ 成立。
这支付了两个不同实际来源在同一真实网格上的量词，
没有将一个来源的局部值移给另一个。

## 7. 六个实际网格的并域准确下降到五变量矩形

R572 的原坐标回代为
$$
x=(v-Z)/3,\qquad
\xi_1=Q/2+(2v+Z)/6,\qquad
\xi_3=Q/2-(2v+Z)/6 .
$$
所以
$$
\mathcal D_n
=\{Q,r,c,d\in p^n,\ Z+2v\in p^n,\ v\ {\rm unit}\}.
\tag{33}
$$
对六个真实原像
$\mathcal D_{\zeta,n}=R_\zeta^{-1}\mathcal D_n$，
相应条件是 $Z+2\delta\zeta C\in p^n$；
它们分别包含在六个不同 $\Gamma_{\zeta,n}$，故严格不交。

在真实五变量中写
$$
F=\delta Z/6+\rho_F,\qquad
\rho_F=(1-2\omega)Q/2+\omega^2r+c+(2+3\omega)d .
$$
有不省略任何输入的准确恒等式
$$
\boxed{
Z+2\delta\zeta C=2\delta(\rho_F-D_\zeta).
}
\tag{34}
$$
因此在六支测试的真实支撑上，
$$
\boxed{
\bigcup_{\zeta\in\mu_6}\mathcal D_{\zeta,n}
\quad\Longleftrightarrow\quad
\mathscr R_n=\{Z\ {\rm unit},\ Q,r,c,d\in p^n\}.
}
\tag{35}
$$
这里“等价”限定在 $\Gamma_n^{(6)}$，并未删除测试支撑。
四个深条件使 $F\equiv\delta Z/6\bmod p^n$，
所以原 $F,C$ 单位也准确支付。
这个域没有额外加一个 $L$ 单位限制。

并域在纯 $C$ 下不动；$\mu_B$ 和测试同样不动。
于是
$$
\int_{\cup_\zeta\mathcal D_{\zeta,n}}\widetilde q_n\ell\,d\rho_0
=6\int_{\mathcal D_n}\widetilde q_n\ell\,d\mu_B .
\tag{36}
$$
现在可用 R590 的完整 $C$ 积分，而不是把伴随取质量。
具体把 R590(31) 的系数换成 (9) 的新 $a_{kj\ell}$，
记所得七实际 coset 矩权为 $\widetilde{\mathcal W}_n(F,G)$。
全部 $\kappa$、$u_j$ 和真实 $B_C$ 纤维仍保留。
(35)–(36) 准确给
$$
\boxed{
\begin{aligned}
\int_{\mathscr R_n}\widetilde{\mathcal W}_n\ell\,d\nu^\flat
&=6\beta^{5n}\mathcal H_{\mu_B}(\kappa^n)\\
&=\beta^{5n}
\left\{\frac{2d_p\alpha_\Delta}{b}\kappa^n+p^{2n}\mathcal O\right\},
\end{aligned}}
\tag{37}
$$
所以其赋值对每个 $n\ge1$ 准确为 $n$。
在此矩形内原 $Y,W$ 都为单位，因为它们的自由 $Z$ 系数
同为 $(-2+\omega)/2$；这不是另换的一对观察。

作为几何核对，$Z+2v=3(\xi_1-\xi_3)$、
$Z-v=-3x$ 正交，度数为 $18,9$。
前者的 whole 锚 $\Theta(3z)$、后者的 $\sigma(3z)$
都在现 ray 上给 $\beta$；全部 $C$ 共轭仍整并保标准半特征。
(35) 本身是逐点域恒等式，并不依赖只比较这两个边际。

## 8. 同一原总行、测试改变量和唯一外矩形补偿

整个五变量来源仍满足
$$
(\pi_4)_*(\widetilde{\mathcal W}_n\nu^\flat)
=\beta^n(\pi_4)_*\nu^\flat .
$$
因此令 $\mathscr R_n$ 为 (35) 的真实矩形，准确有
$$
\boxed{
\beta^n(J'_S-6\delta J'_T)
=\int_{\mathscr R_n}\widetilde{\mathcal W}_n\ell\,d\nu^\flat
+\int_{\{F\ {\rm unit}\}\setminus\mathscr R_n}
                    \widetilde{\mathcal W}_n\ell\,d\nu^\flat .
}
\tag{38}
$$
右边第二项保全部原 $Y/W$ 各自单位、原七纤维矩和其余变量，
没有用矩形的非零值代掉它。
若原两中央同时为零，它必须准确抵消 (37)，其赋值也为 $n$。

R585/R590 的完整四单位比较同样保留。若
$A_4=1_{\{c,d,U,V\ {\rm unit}\}}$，
$\mathsf A_0$ 是原 $F=0$ 四行的单位指示，则
$$
\boxed{
Q_{A,n}^{\sim}-\beta^nJ_A
=\int_{\{F\ {\rm unit}\}}
(\widetilde{\mathcal W}_n-\beta^n)(A_4-\mathsf A_0)
\ell\,d\nu^\flat .
}
\tag{39}
$$
原八条单位变化域、carry 外的 $-\beta^n$ 项和四个深补项
仍是同一式的完整分解。
此外
$$
\boxed{
(\pi_4)_*((\widetilde{\mathcal W}_n-\mathcal W_n)\nu^\flat)=0
}
\tag{40}
$$
将本篇有限补偿准确接回 R590 的旧权；
在任意实际子域使用它时必须保该子域上的测试差。
本篇没有把 (40) 推成每个子域分别为零。

新增的实质为：一个整的九行补偿在同一原算术家族中，
同时支付原来源和 $B$ 来源的非零局部行；随后得到 (37)
这个无需 $C$ 隐藏切集的实际 $Z$ 单位矩形。
原负五行 $I_1$ 与 $\nu^\flat$ 的联系必须继续保
$\widetilde{\mathcal W}_n$ 和 (38) 的外矩形，
不能单凭两型张量或一个正矩单位宣布整个中央非零。
主目标尚未完成。

## 9. 精确文件

- [check-r594-two-source-six-carry-compensation.js](../scripts/check-r594-two-source-six-carry-compensation.js)
- [check-r594-two-source-six-carry-compensation.json](../scripts/check-r594-two-source-six-carry-compensation.json)

JSON 保存全部二十列、两个固定九行余式矩阵、
完整 $\mathsf B_0/\mathsf B_1$、实际主元和固定分母，
以及六套 odd9 完整框架、源最低六次多项式、全部第一矩和质量系数、
真实并域的准确物理回代。
脚本用 BigInt 的 $\mathbf Q(\omega)$ 算术自含重建所有数据，
三个完整右逆身份和全部来源几何等式已精确通过。
无独立数值素数假设；完整 $\lambda,\kappa$ 整逆、无穷深度
及所有补域量词由正文证明。
