# R478 — 原二倍连接的新线差、非零 log2 质量项与完整混合 carry

日期：2026-11-14。**状态：已证明。** 本篇在 R471 的同一个奇来源
$C_X$ 内，把新曲线行写成一个完整二倍连接差的固定投影。给出两个
连接来源的整表示、原 principal Mellin 比较和不可删除的非零
$\log_p2$ 质量项；另在原独立连接输入与二倍奇来源中计算所有深度的
完整 carry。其两个输入的核心尺度不同，不能用一个共同缩放替代。

这些恒等式没有单独赋任何连接中央导数为零，也没有把新线投影
当成未投影的 $W_*$。已知 log2 项非零，尚不能排除其余完整行抵消它。

## 1. 保同一个奇来源、连接和物理周期

沿 R471 的 $b=17$、同一 ordinary ray、同一 $\Omega_p$，置
$$
C=C_X=\frac{\Theta(z)\Theta(2z)^2\sigma(4z)}{2240b},
\qquad
q=17\frac{\Theta'}{\Theta},
$$
$$
G=C'-qC=S+\frac{H_X}{560b},\qquad
H_X=\frac{5H_3-2H_5}{3},\qquad
g_0=C'(0)=G(0)=\frac1{560b}.
\tag{1}
$$
全部符号均为原来源，特别 $H_X$ 不被认作一条新 Hecke 特征线。
记
$$
a=\bar\pi_0,\quad \pi=\pi_0,\quad a\pi=p,\quad
\lambda=-a^{-1},\quad\beta=a^{-1}=-\lambda,\quad
\kappa=p/a^2,\quad d=p-1.
\tag{2}
$$
当前 $p>19$、$p\equiv7\pmod{64}$，故所有显示固定分母为单位。
连接与奇来源的真实 core 分别是
$$
\nu_q|_p=\beta[\pi]_*\nu_q,\qquad
\nu_C|_p=\beta[\kappa]_*\nu_C.
\tag{3}
$$
第一式由 R463 的完整 Eisenstein–Kronecker 分布支付；
两个尺度的比 $\pi/\kappa=a$ 必须保留。

定义同一实际二倍来源及两个连接函数
$$
B(z)=C(2z),\quad G_2(z)=G(2z),\quad D(z)=C'(2z),
$$
$$
Q_0(z)=q(z)C(z),\qquad Q_2(z)=q(z)C(2z).
\tag{4}
$$
注意 $D$ 是先对 $C$ 求导再代入 $2z$，故 $B'=2D$。
所有来源的 Amice 解释一律是 $z=\Omega_p\log(1+T)$。

## 2. 完整二倍连接差及真正新曲线投影

仍取原 CM 元素 $\delta^2=-3$。原除法单位和对数导数准确为
$$
u_2=\delta^{-3}\frac{\Theta(2z)}{\Theta(z)^4}
   =\frac{X-8b}{\delta^3X},
\qquad R_2=(\log u_2)'=\frac{48by}{x(X-8b)},
$$
$$
2q(2z)-4q(z)=17R_2(z),\qquad X=x^3.
\tag{5}
$$
R471 的完整整组合为
$$
W_*=101W_{13}-64W_{15}=37R_2 B
=-\frac{111}{280}\sigma^4\sigma(2z)\sigma(8z)\Theta(4z)^2.
\tag{6}
$$
因此得到整个函数恒等式
$$
\boxed{
Q_2-\frac12Q_0(2z)=-\frac{17}{148}W_*.
}
\tag{7}
$$
等价地，对 $B$ 使用其实际 degree136 的连接，
$$
\boxed{(\partial_z-4q)B=2G_2+\frac{17}{37}W_*.}
\tag{8}
$$
两边作为完整函数相等，而不是仅比较单位质量或首项。

令 $P=\mathcal Q\Pi_0$ 是 R465/R477 的 whole 第一轴秩一投影。
整个 principal $[2]^*\mathcal S_{34}$ 块在 $P$ 的核中，
故 $PG_2=0$。R466 给
$$
PW_*=-\frac{3848}{5}S_{\rm new}.
$$
于是
$$
\boxed{
P\bigl(Q_2-\tfrac12Q_0(2\cdot)\bigr)=\frac{442}{5}S_{\rm new},
\qquad
P\bigl((\partial-4q)B\bigr)=-\frac{1768}{5}S_{\rm new}.
}
\tag{9}
$$
这里 $P$ 作用于 (7)、(8) 已经证明属于 $\mathcal S_{136}$ 的
**整个组合**。单独的 $Q_2$ 和 $Q_0(2z)$ 有连接的拟周期项；
不能分别把它们未经定义地放进同一个有限 theta 投影。

### 2.1 连接来源整有界，但不冒认单独 theta 截面

R471 已给 $Q_0$ 的无逆表示
$$
Q_0=\frac{17}{2240b}\Theta'\Theta(2z)^2\sigma(4z).
\tag{10}
$$
二倍 identity 还给
$$
\Theta(2z)=\Theta(z)\{\Theta(z)^3-8b\sigma(z)^6\},
$$
从而
$$
\boxed{
Q_2=
\frac{17}{2240b}\Theta'(z)
\{\Theta(z)^3-8b\sigma(z)^6\}
\Theta(4z)^2\sigma(8z).
}
\tag{11}
$$
式 (11) 的两行相邻因子相乘。它是一条完整的有权输入恒等式，
没有在原单位测试中倒置 $\Theta$。原 $\Theta,\sigma$ 的 Amice
级数整有界，且 $\Theta'$ 对应
$\Omega_p^{-1}(1+T)\partial_T$；在当前普通处 $\Omega_p$ 为单位。
所以 (10)、(11) 都给整有界测度。

全纯性也由它们的原函数表示直接得到。全纯不等于属于
untwisted $\mathcal S_{136}$；本篇只在 (7)、(8) 的完整相消后
使用这个有限 theta 空间。

## 3. 原 principal Mellin 比较与非零质量 log2

记 $J_0,J_2,J_*$ 分别为 $Q_0,Q_2,W_*$ 的原 principal 单位
Mellin 行：
$$
J_F(u)=\int_{\mathbf Z_p^\times}
\langle y\rangle^{du}\,d\nu_F(y).
\tag{12}
$$
因为二是单位，(7) 准确给
$$
\boxed{
J_2(u)=\frac12\langle2\rangle^{du}J_0(u)
-\frac{17}{148}J_*(u).
}
\tag{13}
$$
R471 已计算
$$
J_0(0)=\frac{\lambda(1+\kappa)}{560b},\qquad J_*(0)=0.
$$
因此
$$
\boxed{J_2(0)=\frac{\lambda(1+\kappa)}{1120b}.}
\tag{14}
$$
两个连接函数本身的总质量均为零，不影响 (14) 的非零单位质量。
对 (13) 求导得到
$$
\boxed{
\frac{17}{148}J_*'(0)
=\frac12J_0'(0)-J_2'(0)
+\frac{d\lambda(1+\kappa)}{1120b}
\log_p\langle2\rangle.
}
\tag{15}
$$
最后一项严格非零。确实，$2$ 是 $p$ 单位；若
$\log_p\langle2\rangle=0$，则 $\langle2\rangle=1$，于是
$2^{p-1}=1$ 于 $\mathbf Q_p$，也就于 $\mathbf Q$，矛盾。
其余因子均非零且为单位。这里不要求 log2 的赋值有统一上界，
也不借未证明的非 Wieferich 结论。

(15) 不能单独推出 $J_*'(0)\ne0$，因为 $J_0'$、$J_2'$ 未知；
$J_*'$ 本身也仍含六条非算术外谱。新曲线零只作用于 (9) 的
完整投影，不能取代 (15) 左端的未投影观察。

## 4. 二倍连接的完整三态径向核心

从 (3)，对原导数测度有
$$
\nu_{C'}|_p=\beta\kappa[\kappa]_*\nu_{C'}.
$$
另外，R471 的 $G$ 和 $W_*$ 的实际核心分别为 $\lambda$、$\beta$。
置
$$
r=\beta\kappa,\qquad c=\frac{17}{148}.
$$
在 (4) 的三个来源上，准确有
$$
\nu_D|_p=r[\kappa]_*\nu_D,\qquad
\nu_{G_2}|_p=\lambda[\kappa]_*\nu_{G_2},\qquad
\nu_{W_*}|_p=\beta[\kappa]_*\nu_{W_*}.
\tag{16}
$$
式 (7) 又给
$$
Q_2=\tfrac12(D-G_2)-cW_*.
\tag{17}
$$
所以对每个 $n\ge0$，
$$
\boxed{
[\kappa^{-n}]_*(\nu_{Q_2}|_{p^n\mathbf Z_p})
=r^n\nu_{Q_2}
+\frac{r^n-\lambda^n}{2}\nu_{G_2}
+c(r^n-\beta^n)\nu_{W_*}.
}
\tag{18}
$$
逆缩放只在显示的真实深域上使用。对 $n=1$，这就是同一原
三态来源上的三角 core；(16)、(17) 已直接证明其所有迭代，
没有对一般输入卷积猜 scalar core。

## 5. 原 q 与 B 两独立输入的完整进位

现在始终保独立张量
$$
\mu=\nu_q(x)\otimes\nu_B(y),\qquad Y=x+y.
\tag{19}
$$
其总输出是 $\nu_{Q_2}$。两个原输入同时深的准确式是
$$
\mu|_{\{x,y\in p^n\mathbf Z_p\}}
=\beta^{2n}[\pi^n,\kappa^n]_*\mu.
\tag{20}
$$
相较于总输出的 $\kappa^n$ 归一，(20) 的真实输出是
$a^n x+y$，而不是 $x+y$。

令 $A_n=a^n$、$N_n=p^n$，并沿 R463 的原规范定义
$$
u_{A_n}=\delta^{1-N_n}
\frac{\Theta(A_nz)}{\Theta(z)^{N_n}},\qquad
R_{A_n}=(\log u_{A_n})'.
$$
完整恒等式为
$$
A_nq(A_nz)-N_nq(z)=17R_{A_n}(z).
\tag{21}
$$
对实际紧开进位域
$$
\Gamma_n=\{x+y\in p^n\mathbf Z_p\}
\setminus\{x,y\in p^n\mathbf Z_p\},\qquad n\ge1,
$$
定义其归一输出测度
$$
\mathcal C_n=(Y/\kappa^n)_*(\mathbf1_{\Gamma_n}\mu).
$$
由 (18) 完整减去 (20)，再代入 (21)，得到
$$
\boxed{
\mathcal C_n=
\frac{r^n-\lambda^n}{2}\nu_{G_2}
+\frac{17}{148}(r^n-\beta^n)\nu_{W_*}
-17a^{-3n}\nu_{R_{A_n}B}.
}
\tag{22}
$$
证明中的 $Q_2$ 系数恰好消掉，因为
$$
\beta^{2n}\frac{N_n}{A_n}
=\frac{p^n}{a^{3n}}=r^n.
$$
全部不同输入深度、输出发生相消的情形都包含在 $\Gamma_n$ 中。
尤其 $n>1$ 时没有将它缩成“至少一个输入单位”。

最后一项是实际有界整原点测度：由 (21)，
$$
R_{A_n}B=\frac{A_nq(A_nz)B-N_nQ_2}{17},
$$
而 $A_n$ 是普通单位，$q,B$ 都整有界。但它可有真实全局
division 极点，不能把它放进固定的 $\mathcal S_{136}$，
也不能对它单独施加 (9) 的有限投影。

由于 $R_{A_n}(0)=B(0)=W_*(0)=0$、$G_2(0)=g_0$，
整个进位测度的总质量为
$$
\boxed{\mathcal C_n(\mathbf Z_p)
=\frac{r^n-\lambda^n}{1120b}\in\mathcal O^\times.}
\tag{23}
$$
这里 $r\in p\mathcal O$、$\lambda\in\mathcal O^\times$。
(23) 是整个归一输出的质量；若再要求输出为单位，须把
(22) 三项一起限制到 $\mathbf Z_p^\times$，不能以这个总质量
替代相应单位质量或中央导数。

## 6. 已付的真实连接接口与剩余条件

(9) 把新曲线接到原奇来源的固定二倍连接差；
(15) 保留其未投影 principal 比较中的已知非零 log2 项；
(18)、(22) 支付同一来源的全部径向状态和原独立输入进位。
三种式子在共同 $\Omega_p$ 下相容，但适用对象不同，不能合并
成一个未付的投影／限域交换。

要从这些式子推出原三曲线的至少一条完整中央非零，仍须控制
(15) 的两条连接观察，或者把 (22) 的完整 division 行及其所有
补域合法送到 (9)。固定新线中央零、原 $S,T$ 中央零和一个非零
log2 质量项之间，目前尚未得到排除全部相消的等式。
因此本篇不收尾主目标。

依赖原完整来源与已付规范：

- [R463：连接与奇来源的不同核心尺度及 division 恒等式](R463-original-connection-pi-core-and-exact-division-log-carry.md)。
- [R471：同一个 C_X、完整六sigma因式和连接单位质量](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)。
- [R466：W_* 的完整新曲线投影及其真实身份](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。
- [R465：整个二倍旧 theta 块在新投影的核中](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R469：新曲线完整普通／惰性 Sha 桥](R469-e2312-full-weight-square-ordinary-inert-sha-bridges.md)。
