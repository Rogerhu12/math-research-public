# R529 — 原 J/K 小核、完整四输出 carry 与真实 S/W 补偿

日期：2026-11-14。**状态：已证明。** 同一个原六 sigma 来源中，两个正交的半整轴 $J,K$ 都有真实一层核心 $\beta=-\lambda$。用 $K$ 单位第六矩整逆，可以在任意正 $J$ 深度返回整个四输出 $(J,Y,\xi_2,d_0)$，并保原独立 sigma 的实际近相消域。整逆的正测试被 $J$ 核和原三阶几何原样保留。

原五深一单位网格在这个 carry 内给准确赋值 $5n$，不需要新射线或新的大素数门。本测试的局部质量整条为零。旧 $W$ 不在上述四输出中；其完整移动及两个真实补偿项在 §8 保留。同一局部测试的 $W-6\delta Y$ 中央差还准确有赋值 $5n+3$。这些均是完整原输入中的等式，没有给未控制补域赋零。

## 1. 同一原六输入与三个小轴

沿用 R493、R506、R522：
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
\gamma=3+\omega,\quad\bar\gamma=2-\omega,\quad b=17,
$$
$$
\lambda=-\bar\pi_0^{-1},\quad \beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\qquad
\rho_0=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
物理变量的次序为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。原观察为
$$
Y=(\delta,2\delta,\gamma,\bar\gamma,1,2)\xi,\qquad
W=(\delta,2\delta,\gamma,\bar\gamma,3\delta,4)\xi.
\tag{2}
$$
$Y_*\rho_0=\nu_S$，$W_*\rho_0=6\delta\nu_T$。令
$W'=W\mathcal T$、$W_2=W\mathcal T^2$，仍保原三阶等距
$\mathcal T^3=I$、$Y\mathcal T=Y$ 及
$h=\omega^2\mathcal T_*\rho_0$。

取 R506 的实际反射轴
$$
C=\frac{\xi_1+\omega^2\xi_3-\omega x-c}{2},
\qquad C\mathcal T=\omega^2x,
$$
并定义
$$
\boxed{
J=C-x,\quad K=C-\omega^2x,\quad
H_0=\xi_1-\xi_3+x,\quad
\eta=\frac{2(1-\omega)}3,\quad E=H_0-\eta K.
}
\tag{3}
$$
完整原行是
$$
\begin{aligned}
2J&=(1,0,\omega^2,-(2+\omega),-1,0),\\
2K&=(1,0,\omega^2,2+\omega,-1,0),\\
3E&=(2+\omega,0,\omega-1,0,1-\omega,0).
\end{aligned}
\tag{4}
$$
直接 Hermitian 计算给
$$
\boxed{
J\perp K,E,\qquad K\perp E,\qquad
N(J)=N(K)=\frac32,\quad N(E)=1,
}
\tag{5}
$$
$$
K,E,H_0\perp Y,\xi_2,d_0,\qquad
J\mathcal T=J,\quad K\mathcal T=\omega^2K,\quad
E\mathcal T=\omega^2E.
\tag{6}
$$
特别 $E$ 不含原独立输入 $x$。这里没有从四维压缩坐标反推一个未经证明的原输入事件。

## 2. 完整小 theta 核与绝对标量

原六 sigma 在与 $2J$、$2K$ 正交的五个输出保留时，分别是标准 even degree $6$。两行各有四个 odd 系数，其他系数为零；完整交叉极化消失，所以没有隐藏伴随 flat twist。对 $3E$ 则为标准 odd degree $9$。

当前 R496 的完整中心已付
$$
g_\pi\equiv91+72\omega\pmod{576}.
$$
因此
$$
\boxed{
g_\pi\equiv7=1+6\pmod{12},\qquad
g_\pi\equiv1\pmod{18},\qquad
g_\pi\equiv1\pmod6.
}
\tag{7}
$$
前式使整个 even $\mathcal S_6$ 的 canonical Heisenberg 交织为 scalar；后两式保相应 odd 半特征并给 whole scalar。真实非零锚分别取
$$
\Theta(\delta z)\in\mathcal S_6,\qquad
\sigma(3z)\in\mathcal S_9^{\rm odd},\qquad
\sigma(\delta z)\in\mathcal S_3^{\rm odd}.
\tag{8}
$$
原 $\Theta$ 与原 sigma 的完整核心都是 $\beta$；固定普通单位的拉回保持该规范。因此绝对标量均为 $-1$，不是仅交织相同到一个未定因子。

以任一物理行 $L$ 记
$$
P_{L,r}=I+\frac{\kappa^r-1}{N(L)}\bar L^{\,t}L.
$$
对 $\mu=\rho_0$，精确有
$$
\boxed{
\nu_\mu|_{J\in p^r}=\beta^r(P_{J,r})_*\nu_\mu,\quad
\nu_\mu|_{K\in p^r}=\beta^r(P_{K,r})_*\nu_\mu,\quad
\nu_\mu|_{E\in p^r}=\beta^r(P_{E,r})_*\nu_\mu
}
\tag{9}
$$
对所有整数 $r\ge0$ 成立，保各自全部另外五个原输出。清分母 $2,3$ 是当前处单位，不改变深度条件或正交投影。

由 (6) 和 $h=\omega^2\mathcal T_*\rho_0$，同样三式对真实 $h$ 成立。此处只声明这两个已经支付的来源；不把它们免费推广至所有旧 $W$ 四挠态。

## 3. 独立 sigma 的完整 J/K carry

置
$$
R_3=\xi_1+\omega^2\xi_3-c,\qquad
R=R_3/2,\qquad a=(2+\omega)/2.
$$
则
$$
\boxed{J=R-ax,\qquad K=R+ax,\qquad N(R)=N(a)=3/4.}
\tag{10}
$$
$R$ 与 $x$ 是原三 sigma 块和原独立第四 sigma 的真实两个输出，非形式替代。可保其余四个实际输出为
$$
U_1=\xi_3-\omega\xi_1,\quad U_2=c+\xi_1,\quad \xi_2,\quad d_0.
\tag{11}
$$
$(R_3,U_1,U_2)$ 对 $(\xi_1,\xi_3,c)$ 的行列式是 $3$，故 (10)–(11) 在当前处是完整格的可逆变换。两个输入各自有 $\beta$ 核；$R_3$ 的 degree $3$ 核已由 (7)–(8) 绝对定标。

对于任意 $r\ge1$，真正近相消域准确为
$$
\boxed{
\Gamma_r^J
=\{J\in p^r,\ R,x\ {\rm unit}\}
=\{J\in p^r,\ K\ {\rm unit}\}.
}
\tag{12}
$$
因为在 $J\in p^r$ 上 $R\equiv ax\pmod p$，
$K\equiv2ax\pmod p$，且 $2a$ 是单位。这里四个伴随 (11) 均未丢弃。

## 4. 一个 K 单位整逆恢复整个四输出

R522 的完整 degree $3$ 偶线给，对任意其余五个 $H_0$ 正交输出，
$$
\text{第六 }H_0\text{ 矩}
=216b\Omega^6\cdot\text{第零 }H_0\text{ 矩}.
\tag{13}
$$
本篇使用无 $H_0$ 单位指示的这个版本，记
$$
P_0=\frac{H_0^6}{216b\Omega^6}.
$$
定义
$$
\boxed{
\widehat P_K=
\frac1{216b\Omega^6}
\sum_{j=0}^6\binom6j
\frac{\eta^j E^{6-j}K^j}{1+\lambda\kappa^j}.
}
\tag{14}
$$
$j>0$ 的分母模 $p$ 是 $1$。$1+\lambda$ 的单位性也已付：若
$p\mid(\bar\pi_0-1)$，则在当前 $p\ge71$ 由 Hasse 的迹界迫使
$\operatorname{Tr}\pi_0=1$，与原 $\pi_0\equiv1\bmod27$ 的迹 $2$ 冲突。因此 (14) 是整多项式测试。

取真正四输出
$$
\boxed{\Pi_{\rm fix}=(J,Y,\xi_2,d_0).}
\tag{15}
$$
它们均与 $K,E,H_0$ 正交，且逐个被 $\mathcal T$ 固定。其 Gram 行列式是 $6$；添上 $K,E$ 的完整六输出 Gram 行列式是 $9$。附证书给全部六乘六矩阵、逆及 Gram。

用 (9) 对每个 $K^j$，单位限制的精确因子为
$1+\lambda\kappa^j$。逐项取消 (14) 的分母，再用
$E+\eta K=H_0$ 和 (13)，得整个来源身份
$$
\boxed{
(\Pi_{\rm fix})_*
\{{\bf1}_{K\ {\rm unit}}\widehat P_K\,d\nu_\mu\}
=(\Pi_{\rm fix})_*d\nu_\mu,\qquad \mu=\rho_0,h.
}
\tag{16}
$$
这是整个四变量测度，允许任意依赖它们的真实紧开条件。

由于 $J\perp E,K$，整个 (14) 被 $P_{J,r}$ 固定；由于 (6)，它也被 $\mathcal T$ 固定。$K$ 单位条件同样不变。因而这两个实际来源的 (16) 仍有原关系
$(\Pi_{\rm fix})_*h=\omega^2(\Pi_{\rm fix})_*\rho_0$，不是新增独立的算术零行。

## 5. 任意 J 深度的同源整条算术返回

在真实像 $J\in p^r$ 内置
$$
\boxed{
J_r=J/\kappa^r,\qquad
Y_r=Y+(\kappa^{-r}-1)\left(-2+\frac{4\delta}{3}\right)J,
}
\tag{17}
$$
并记 $\Pi_{\rm fix}^{(r)}=(J_r,Y_r,\xi_2,d_0)$。
这是 $\Pi_{\rm fix}\circ P_{J,r}^{-1}$ 的准确式；逆尺度只在其显示的深域使用。

由 (9)、(12)、(16)，对于每个 $r\ge1$ 有
$$
\boxed{
(\Pi_{\rm fix}^{(r)})_*
\{{\bf1}_{\Gamma_r^J}\widehat P_K\,d\nu_\mu\}
=\beta^r(\Pi_{\rm fix})_*d\nu_\mu.
}
\tag{18}
$$
因此
$$
\boxed{
\int_{\Gamma_r^J,\ Y_r\ {\rm unit}}
\langle Y_r\rangle^{du}\widehat P_K\,d\rho_0
=\beta^rJ_S(u).
}
\tag{19}
$$
对 $h$ 同式右侧为 $\beta^r\omega^2J_S(u)$。
这不是只给忘去原输入后的一个质量或有限 jet。

## 6. 原五深一单位网格和全部首五项

仍取原实际独立事件
$$
\mathcal D_n
=\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n,\ x\ {\rm unit}\},
\qquad n\ge1.
\tag{20}
$$
在此 $K,J,Y,W,H_0$ 均为单位，而 $E\in p^n$。
由 (11)，同一事件也准确是
$\{R_3,U_1,U_2,\xi_2,d_0\in p^n,\ x\ {\rm unit}\}$。

测试 (14) 不含 $\xi_2,d_0$。这两个仍独立的深 sigma 质量为零，故
$$
\boxed{\int_{\mathcal D_n}\widehat P_K\,d\rho_0=0.}
\tag{21}
$$
同一原因消掉全部 $\log\langle x\rangle$ 和固定单位尺度的 log 项。
这是一条针对本测试的整条身份；R527 的另一测试有非零局部质量，不能混用。

把五个深输入共同缩放为变量 $t$，自由 $x$ 不动。按
$(\xi_1,\xi_2,\xi_3,c,d_0)$ 次序，令
$$
z=(\delta,2\delta,\gamma,1,2),\qquad
e=E|_{x=0},\qquad f=(\eta K)|_{x=0}.
$$
这里 $e+f=(1,0,-1,0,0)$，$\eta K=x+tf\cdot\xi$、
$E=t e\cdot\xi$。定义整个解析积分
$$
\mathcal A_Y(t)=
\frac d{216b\Omega^6}
\int_{x\ {\rm unit}}
\log\langle\bar\gamma x+t z\cdot\xi\rangle
\sum_{j=0}^6\binom6j
 \frac{(t e\cdot\xi)^{6-j}(x+t f\cdot\xi)^j}
 {1+\lambda\kappa^j}\,d\rho_0.
\tag{22}
$$
五个实际 sigma 的核心给
$$
C_{Y,n}:=\int_{\mathcal D_n}d\log\langle Y\rangle\widehat P_K\,d\rho_0
=\beta^{5n}\mathcal A_Y(\kappa^n).
\tag{23}
$$

为核完整第五阶，写
$$
\prod_{i=1}^5(e_i+s f_i+t z_i)
=\sum_{a,\ell}P_{a,\ell}t^a s^\ell .
$$
所有正 log 次数和所有六次测试项恰给
$$
q_j=-\frac1{84\cdot216}
\sum_{\substack{1\le a\le5\\ \ell=j-1-a\ge0}}
\frac{(-1)^{a-1}}{a\bar\gamma^a}
\binom6{5-a}a!(5-a)!\,P_{a,\ell}.
\tag{24}
$$
其七个准确值是
$$
\boxed{
\begin{array}{c|c}
j&q_j\\ \hline
0,1,2,4&0\\
3&(5-20\delta)/27783\\
5&-80/64827-8\delta/7203\\
6&(-7118+24944\delta)/9529569 .
\end{array}}
\tag{25}
$$
$x$ 的实际剩余次数恰为 $1$，所以使用的是正第一单位矩
$I_1=(1+\lambda\kappa)\Omega$，没有未知负矩或 log 矩。由此
$$
\boxed{
[t^5]\mathcal A_Y
=\frac db(1+\lambda\kappa)
\sum_{j=0}^6\frac{q_j}{1+\lambda\kappa^j}.
}
\tag{26}
$$
完整和为
$$
\sum_jq_j=\alpha_H
=\frac{-3221+5000\omega}{27\cdot7^6},\qquad
N\alpha_H=\frac{1021}{3^5\cdot7^7}.
\tag{27}
$$
当前 $p\equiv7\bmod64$ 排除 $p=1021$，其余分母坏素数早已排除。因此 (26) 在整个现有普通 ray 为单位，本篇不新增射线或大素数门。

低于第五阶由五个独立零质量 sigma 全部消失。整六次测试及 log 展开给
$v_p([t^m]\mathcal A_Y)\ge-\lfloor\log_pm\rfloor$；五个 sigma 的实际 $\mu_6$ 型使幂次仅为 $5\bmod6$。对当前 $p\ge71,n\ge1$，全部高项严格深于首项。因此
$$
\boxed{v_p(C_{Y,n})=5n,\qquad n\ge1.}
\tag{28}
$$

## 7. 同一个 carry 内的真实非零像

置 $\mathcal D_{n,r}=P_{J,r}\mathcal D_n$。在完整框架
$(J,K,U_1,U_2,\xi_2,d_0)$ 中，这个域的准确全部条件为
$$
\boxed{
J/\kappa^r\in\mathcal O,\quad K\ {\rm unit},\quad
U_1,U_2,\xi_2,d_0\in p^n,\quad
J/\kappa^r+K\in p^n.
}
\tag{29}
$$
它迫使 $J/\kappa^r$ 为单位，故 $J$ 深度准确为 $r$，
并包含于同一个 $\Gamma_r^J$。由
$x=(K-J/\kappa^r)/(2a)$ 可直接核原独立 $x$ 单位条件。
这不是用两个输出深度替换五个独立隐藏事件。

所有条件和测试真实运输后，(9)、(21)、(28) 给
$$
\boxed{
\int_{\mathcal D_{n,r}}\widehat P_K\,d\rho_0=0,\qquad
v_p\!\left(
\int_{\mathcal D_{n,r}}
d\log\langle Y_r\rangle\widehat P_K\,d\rho_0
\right)=5n.
}
\tag{30}
$$
整条局部积分准确是 $\beta^r C_{Y,n}$。
(19) 仍含实际补域
$$
\{\Gamma_r^J,\ Y_r\ {\rm unit}\}\setminus\mathcal D_{n,r}.
\tag{31}
$$
原 $J'_S(0)=0$ 时，这个补域反号补偿 (30)，不能删掉。

## 8. 旧 W 的全部转置与两项真实补偿

$W$ 不属于 (15)。在完整框架 $(J,Y,\xi_2,d_0,K,E)$ 中，
$$
\boxed{
\begin{aligned}
W={}&\left(4-\frac{8\delta}{3}\right)J
+\left(\frac52+\frac\delta6\right)Y
+(1-3\delta)\xi_2-\left(1+\frac\delta3\right)d_0\\
&+\left(\frac13-\delta\right)K
+\left(-2+\frac{4\delta}{3}\right)E .
\end{aligned}}
\tag{32}
$$
两个末项非零，所以 (16) 不能被称为保持旧 $T$ 行的联合恒等式。

原三条 $W_j=W\mathcal T^j$ 的 $J$ 转置却完全可写：
$$
\boxed{
W_{j,r}=W_j+(\kappa^{-r}-1)\frac{-5+\delta}{3}J,
\qquad j=0,1,2.
}
\tag{33}
$$
这是实际 $W_j\circ P_{J,r}^{-1}$；由 (6)，(32) 的 $K,E$
部分在 $W_j$ 中乘 $\omega^{2j}$，前四输出部分不动。

未作 $K$ 单位逆的 $P_0$ 本来保完整 $Y,W,W'$。又因
$H_0\perp J$，对原 $\rho_0$ 准确有
$$
\int_{J\in p^r,\ W_{0,r}\ {\rm unit}}
 \langle W_{0,r}\rangle^{du}P_0\,d\rho_0
=\beta^r6\delta J_T(u).
\tag{34}
$$
将左边依真实 $K$ 单位/非单位域分开，得到全部等式
$$
\boxed{
\begin{aligned}
\beta^r6\delta J_T(u)
={}&
\int_{\Gamma_r^J,\ W_{0,r}\ {\rm unit}}
 \langle W_{0,r}\rangle^{du}\widehat P_K\,d\rho_0\\
&+\int_{J\in p^r,\ K\in p,\ W_{0,r}\ {\rm unit}}
 \langle W_{0,r}\rangle^{du}P_0\,d\rho_0\\
&+\int_{\Gamma_r^J,\ W_{0,r}\ {\rm unit}}
 \langle W_{0,r}\rangle^{du}(P_0-\widehat P_K)\,d\rho_0 ,
\end{aligned}}
\tag{35}
$$
其中
$$
\boxed{
P_0-\widehat P_K=
\frac{\lambda}{216b\Omega^6}
\sum_{j=0}^6\binom6j
\frac{\eta^jE^{6-j}K^j\kappa^j}{1+\lambda\kappa^j}.
}
\tag{36}
$$
第二积分的条件是 $K\in p$，不是擅改为 $K\in p^r$。
(35) 对整个 Mellin 变量成立，保所有质量及 log 项。
两补偿项尚未被原 $S/T$ 中央消去。

## 9. 同一小管的真实 S/W 差恰有赋值 5n+3

在 (22) 中把 $z$ 换成旧 $W$ 的
$(\delta,2\delta,\gamma,3\delta,4)$，自由 $x$ 系数仍是 $\bar\gamma$。
用同一个 (24)，得到 $q_j^W$。令
$\Delta_j=q_j^W-6\delta q_j$，全部非零项准确为
$$
\boxed{
\begin{array}{c|c}
j&\Delta_j\\ \hline
3&(-50-10\delta)/3969\\
4&-5/3087-65\delta/27783\\
5&-1510/64827+382\delta/194481\\
6&(7295+563\delta)/194481 .
\end{array}}
\tag{37}
$$
其余项为零，且
$$
\sum_j\Delta_j=0,\qquad
N(\Delta_3)=\frac{400}{3^8\cdot7^3}.
\tag{38}
$$
因此在当前处
$$
\sum_j\frac{\Delta_j}{1+\lambda\kappa^j}
=-\lambda\sum_{j=3}^6
 \frac{\Delta_j\kappa^j}{1+\lambda\kappa^j}
$$
准确有赋值 $3$；$j=3$ 的系数是单位，其余更深。
高 $t$ 尾仍仅为 $5\bmod6$，严格深于 $5n+3$。于是若
$$
C_{W,n}=\int_{\mathcal D_n}
 d\log\langle W\rangle\widehat P_K\,d\rho_0,
$$
就有
$$
\boxed{
v_p(C_{W,n}-6\delta C_{Y,n})=5n+3,\qquad n\ge1.
}
\tag{39}
$$
(21) 对该 $W$ 积分也成立，所以这里没有被遗漏的单位尺度 log 质量。
按同一个 $P_{J,r}$ 送到 (29)，把 $Y,W$ 都用 (17)、(33)
真实转置，差积分再准确乘 $\beta^r$，仍有赋值 $5n+3$。

这条同域非零差和 (35) 的原完整 $T$ 行同时成立；它要求保留
(31)、$W_{0,r}$ 的不同单位补域以及 (35) 的两个额外项。
本篇没有使这些补域自动相等或消失。

## 精确证书与依赖

- [完整原行、框架逆、小核规范与所有第五系数](../scripts/check-r529-low-j-k-core-and-actual-st-carry.mjs)；
  [全部精确数据](../scripts/check-r529-low-j-k-core-and-actual-st-carry.json)。
  同一 BigInt/CM 主体已在 V8 执行；没有浮点近似。检查包括
  三个范数、全部正交关系、原三阶矩阵、完整六输出逆、全部转置、
  七个 $Y/W$ 系数、两个精确范数及 (38) 的全部消去。
- [R522：原 degree3 偶张量与完整 S/T 正六次测试](R522-common-degree3-even-factor-and-same-st-positive-test.md)。
- [R496：现有 ray 的完整 576 中心](R496-original-new-axis-even-core-and-four-source-group.md)。
- [R493：原三阶几何及同一六 sigma](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R506：真实 C 轴及原六输入反射](R506-original-reflection-axis-four-core-and-complete-w-c-rectangles.md)。
- [R471：原 Theta 核与完整来源规范](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)。
- [R527：须区分的另一个非零局部质量测试](R527-original-h0-b-sixth-inverse-and-complete-joint-carry.md)。

本篇新增的是低度 whole 核、任意层同源 carry、四输出整逆、
无需新门槛的真实非零管，以及完整 $W$ 补偿和同域差。
主目标的固定曲线无穷素数结论仍未由这些等式闭合。
