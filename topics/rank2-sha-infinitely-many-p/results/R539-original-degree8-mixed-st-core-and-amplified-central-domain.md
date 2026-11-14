# R539 — 原 degree8 混 S/T 核、完整两态与放大的合法中央域

日期：2026-11-14。**状态：已证明。** 原两条算术观察的差
$L=(W-Y)/2$ 是真正两个独立 sigma 输入中的 degree8 轴。
本篇付清 entire $\mathcal S_8$ 的全部中心、十六个 canonical lift
及绝对标量，得到
$$
K_8=\frac14\sum_{t\in E[4]}\mathsf T_t^8
     -\frac12\sum_{t\in E[2]}\mathsf T_t^8,\qquad K_8^2=I.
$$
这个核心**不是 scalar**。原六输入在此轴及其 degree8 正交
伴随上形成真实两态，整个原四 sigma 块保持。

该轴同时正交于 R536 测试使用的全部 $C,F,G$。
所以同一个严格零质量测试，在任意偶深 $L$ 核后直接返回原
$S/T$ 两条完整算术行，原第一权的变化准确显示。
原五深网格落在这些合法零域中，局部中央赋值从 $n$ 降为
$n-m$；选奇数 $n\ge3$、偶数 $m=n-1$，便在每个这样的完整
合法域中得到赋值一的同源子管。所有实际补域仍保留。

## 1. 原两个 sigma 与同一 Y/W 联合

保原共同规范
$$
\omega^2+\omega+1=0,\quad
\delta=1+2\omega,\quad\gamma=3+\omega,\quad\bar\gamma=2-\omega,
$$
$$
b=17,\quad\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad d=p-1,\qquad
\rho_0=-\nu_\sigma^{\otimes6}/84.
\tag{1}
$$
原六输入为 $(\xi_1,\xi_2,\xi_3,x,c,d_0)$。
令
$$
A=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma x,
\qquad
\alpha=\omega\bar\gamma=1+3\omega,\quad N\alpha=7,
$$
$$
\boxed{
L=\alpha c+d_0=\frac{W-Y}{2},\qquad
M=c-\bar\alpha d_0.
}
\tag{2}
$$
原观察准确分解成
$$
\boxed{
\begin{aligned}
Y&=A-\frac{3\omega}{8}L-\frac{1+6\omega}{8}M,\\
W&=A+\frac{16-3\omega}{8}L-\frac{1+6\omega}{8}M.
\end{aligned}}
\tag{3}
$$
特别 $W-Y=2L$，没有自由尺度或未付的来源替换。
记
$$
a=-3\omega/8,\qquad a_W=(16-3\omega)/8=a+2,\qquad
b_M=-(1+6\omega)/8.
$$

从 $(c,d_0)$ 到 $(L,M)$ 的整个矩阵和逆为
$$
\boxed{
\begin{pmatrix}L\\M\end{pmatrix}
=\begin{pmatrix}\alpha&1\\1&-\bar\alpha\end{pmatrix}
 \begin{pmatrix}c\\d_0\end{pmatrix},\qquad
c=\frac{\bar\alpha L+M}{8},\quad
d_0=\frac{L-\alpha M}{8}.
}
\tag{4}
$$
行列式为 $-8$，且
$$
\boxed{N(L)=N(M)=8,\qquad\langle L,M\rangle=0.}
\tag{5}
$$
当前普通处 (4) 是整自同构，原两个输入的同时深域与
$L,M$ 同时深域完全相同。不同深度时仍按 (4) 保留两个原条件。

原两个 sigma 的完整生成函数是
$$
\boxed{
F_0(l,m)=\sigma(\alpha l+m)\sigma(l-\bar\alpha m)
\in\mathcal S_8^{\rm even}\otimes\mathcal S_8^{\rm even}.
}
\tag{6}
$$
两个轴的交叉项全零，半特征都是两条奇 sigma 的乘积，
即标准 even 半特征。其余四个原 sigma 从始至终原样保留。
若真正忘去它们的三个伴随，则同一个三输入生成函数为
$$
-\frac1{84}\sigma(\delta z)\sigma(2\delta z)
 \sigma(\gamma z)\sigma(\bar\gamma z)\,F_0(l,m).
\tag{7}
$$
使用 (7) 时才能忘伴随；下面的核心和域身份均在完整原六输入
中成立。

## 2. entire degree8 的完整 Heisenberg 交织

原固定 ray 给
$$
\boxed{
g_\pi=\pi_0/\bar\pi_0\equiv11+8\omega\pmod{16},\qquad
g_\pi^2\equiv9=1+8\pmod{16}.
}
\tag{8}
$$
所以一层核心不能认成 scalar。

在标准 Schrödinger 基 $e_j$（$j\bmod8$）上，
$Xe_j=e_{j+1}$、$Ze_j=\zeta_8^je_j$。定义
$$
\boxed{B_8e_j=(-1)^j e_{3j+4}.}
\tag{9}
$$
由 $g_\pi=11+8\omega$ 的整半周期数据，两个基本生成元的
完整像为
$$
X\longmapsto-X^3,\qquad Z\longmapsto-Z^3.
\tag{10}
$$
(9) 正好实现 (10)。例如
$4+3(3j+4)\equiv j\bmod8$ 给第二个负中心号；
第一个负号来自 $(-1)^{j+1}/(-1)^j$。
并且
$$
B_8^2=I.
$$
这保留了模 $16$ 中的 $8\omega$ 项，而非只看模 $8$ 的
乘三作用。

canonical quarter lift 在此规范中为
$$
\boxed{
\mathsf T^8_{(s+r\omega)/4}e_j
=i^{\,s(j+r)}e_{j+2r},\qquad s,r=0,1,2,3.
}
\tag{11}
$$
十六项全部相加，保所有 $E[2]$ 项，得到
$$
\boxed{
A_8:=\frac14\sum_{t\in E[4]}\mathsf T_t^8
-\frac12\sum_{t\in E[2]}\mathsf T_t^8=-B_8.
}
\tag{12}
$$
也可令
$$
R_8e_j=e_{-j},\qquad
J_2=\frac12\sum_{t\in E[2]}\mathsf T_t^8-I.
$$
同一完整计算给
$$
\boxed{A_8=-R_8J_2.}
\tag{13}
$$
附证书保存 (11) 的全部 $16\times8$ 个系数，并精确核定
(9)–(13)，不只比较单个特征子空间。

## 3. 实际 Theta 锚支付绝对标量

由完整 Heisenberg 交织，whole $K_8$ 与 $B_8$ 相差一个 scalar。
$E[2]$ 固定子空间准确为 $[2]^*\mathcal S_2$。
在上述基中，可取
$$
e_0+e_4,\qquad e_2+e_6;
$$
$B_8$ 在这个整个子空间上为 $+I$。

真实非零截面 $\Theta(2z)$ 属于同一子空间。
[R471](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)
式 (12)–(13) 已付原 $\Theta$ 的实际核心为
$\beta=-\lambda$，固定倍点 $[2]$ 与普通核严格交换。
因此 $K_8$ 在该锚上是 $-1$。绝对 scalar 遂准确确定为
$$
\boxed{
K_8=-B_8=A_8=-R_8J_2,\qquad K_8^2=I
\quad\text{于整个 }\mathcal S_8.
}
\tag{14}
$$
这里没有从 projective 交织推测符号，也没有把 whole
degree32 的核心与本篇未经证明地相认。
实际输出 $W-Y=2L$ 的深域与 $L$ 相同，是因为 $2$ 为普通单位。

## 4. 原六来源的真实两态闭包

定义实际第二态
$$
\boxed{\rho_1=K_{8,L}\rho_0.}
\tag{15}
$$
(6)、(14) 使这个状态仍在同一完整 degree8 两轴张量格中。
它保其余四个原 sigma，但不把它冒认成原 $(c,d_0)$ 中仍然
分离的两个 degree1 来源。

原两个独立 sigma 同时深的标量是
$\beta^2=\lambda^2$，而 (4) 保同一个完整同时深事件。
两个正交 whole 核交换，所以
$$
K_{8,L}K_{8,M}\rho_0=\rho_0.
$$
利用 (14)，准确得
$$
\boxed{
K_{8,L}\rho_i=K_{8,M}\rho_i=\rho_{1-i},
\qquad i=0,1.
}
\tag{16}
$$

这也可在原全部 quarter 项中直接看见。
对 $t=m_0/4$，$L$ 平移 $t$ 与 $M$ 平移 $\alpha t$
在第一 sigma 中给完全相同的平移；第二 sigma 的差为
$8t=2m_0$。这是偶整周期，奇 sigma 的半特征号为 $+1$。
在原 CM 格上 $\eta_{\alpha t}=\bar\alpha\eta_t$；
将第二 sigma 的这个整周期乘子和两边 canonical 指数相消，
剩余指数准确为 $(-4+4N\alpha-24)\eta_tt=0$。
因此原联合上严格有
$$
\mathsf T^8_{L,t}F_0=\mathsf T^8_{M,\alpha t}F_0.
\tag{17}
$$
$\alpha$ 在 $E[4]$ 上可逆并保 $E[2]$，把 (12) 应用于
(17) 即再次得到 (16)。所有中心常数和原 $\sigma$ 半特征都保留。

令
$$
P_{L,t}=I+(t-1)\bar L^{\,t}L/8,\qquad
P_{M,t}=I+(t-1)\bar M^{\,t}M/8
\tag{18}
$$
为原六输入矩阵。它们逐个固定其余四个输入。
对全部 $r,s\ge0$，
$$
\boxed{
\rho_i|_{\{L\in p^r,\ M\in p^s\}}
=\lambda^{r+s}(P_{L,\kappa^r}P_{M,\kappa^s})_*
 \rho_{\,i+r+s\ ({\rm mod}\ 2)}.
}
\tag{19}
$$
若另附原四个共有 sigma 输入各深 $v_1,\ldots,v_4$，
则在 (19) 再乘 $\beta^{v_1+\cdots+v_4}$，并准确缩放这四个
原坐标。它们的任意其他条件或测试也可原样保留。
因此这是整六输入闭包，不是只给一条两变量边际。

## 5. 同一个 R536 测试确被混 L 核保持

使用已经发布的
[R536](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)
测试 $\mathfrak q_{n,p}$。该测试有完整 $\lambda,\kappa$ 的有限
定义，支持在三个真实且互不相交的 cubic carry 上；
原 $\mathcal D_n$ 中的加权质量严格为零。

它只依赖那里的 $C,F,G$。这些行与 $Y,W$ 都正交，因此由
$L=(W-Y)/2$，精确有
$$
\boxed{
\langle C,L\rangle=\langle F,L\rangle=\langle G,L\rangle=0,
\qquad
\mathfrak q_{n,p}\circ P_{L,t}=\mathfrak q_{n,p}.
}
\tag{20}
$$
所以 (19) 的纯 $L$ 行在乘上**同一个未移动测试**后继续成立。
其三个真实 carry 条件、$D/\kappa^n$ 和全部有限系数也都保持。
本篇不将这个不变性也用于 $M$；使用 $M$ 的矩形时，测试仍须
按 (4)、(18) 完整转置。

新状态 $\rho_1$ 的构造同样保持 R536 所需的整个 $C$ theta
空间及四个伴随核心，因为它们与 $L$ 正交。
因此 R536 的整纤维推前身份对 $\rho_0,\rho_1$ 均成立。
这不给 $\rho_1$ 的第一 $Y$ 或 $W$ 边际预设算术中央零。

下面只用偶数 $m$。由 (16)、(19)，偶深的 $L$ 核返回原
$\rho_0$，故无需未知第二态的算术行。

## 6. 同一个真实偶深域返回原两个中央

对偶数 $m\ge0$，定义准确的归一观察
$$
\boxed{
Y_m=Y+a(\kappa^{-m}-1)L,\qquad
W_m=W+a_W(\kappa^{-m}-1)L.
}
\tag{21}
$$
它们在 $L\in p^m$ 上整，并满足
$$
Y_m\circ P_{L,\kappa^m}=Y,\qquad
W_m\circ P_{L,\kappa^m}=W.
$$
不将 (21) 换成原未移动的 $Y,W$。

用 (19)、(20)，再用 R536 完整 $\pi_4$ 来源身份，得到对全部
Mellin 参数 $u$ 的准确式
$$
\boxed{
\begin{aligned}
\int_{\substack{L\in p^m\\Y_m\ {\rm unit}}}
 \langle Y_m\rangle^{du}\mathfrak q_{n,p}\,d\rho_0
 &=\lambda^m\beta^nJ_S(u),\\
\int_{\substack{L\in p^m\\W_m\ {\rm unit}}}
 \langle W_m\rangle^{du}\mathfrak q_{n,p}\,d\rho_0
 &=6\delta\lambda^m\beta^nJ_T(u).
\end{aligned}}
\tag{22}
$$
积分的实际支持还包含 $\mathfrak q_{n,p}$ 的完整 cubic carry。
(22) 保原全部归一，使用的仍是同一个原六 sigma 来源和同一个
有限测试。

因此原 $J'_S=J'_T=0$ 使 (22) 的两个完整中央均为零。
若 $m$ 为奇数，(19) 的右端为第二态；
本篇不把这一未知行也赋成零。

## 7. 原非零网格确落在这些合法混 Y 域中

保持原同一个网格
$$
\mathcal D_n=
\{\xi_1,\xi_2,\xi_3,c,d_0\in p^n,\ x\ {\rm unit}\}.
\tag{23}
$$
这里 $L,M\in p^n$，且 $Y,W$ 是单位。
当 $0\le m<n$ 时，(21) 的新增部分属于 $p\mathcal O$，所以
$$
\boxed{
\mathcal D_n\subset
\{L\in p^m,Y_m\ {\rm unit},W_m\ {\rm unit}\}.
}
\tag{24}
$$
在此 $\mathfrak q_{n,p}$ 只有 R536 的第零分支活跃，准确为
其单支测试的 $1/3$。原加权质量仍严格为零。

R536 中按五个深输入记 $D_f$。本篇的
$$
L_f=(0,0,0,\alpha,1)
$$
有完整混合系数
$$
\boxed{
[\xi_1\xi_2\xi_3cd_0]D_f^4L_f=288.
}
\tag{25}
$$
由 R536 的实际第七行 $\mathcal L=1$，令
$$
\alpha_L=-\frac{288}{84\bar\gamma}
=-\frac{72+24\omega}{49}.
$$
(21) 对原第一阶的准确改变量为
$$
\boxed{
b_Y=a\alpha_L=\frac{-9+18\omega}{49},\qquad
b_W=a_W\alpha_L=\frac{-153-30\omega}{49}.
}
\tag{26}
$$
其范数为
$$
Nb_Y=\frac{81}{343},\qquad Nb_W=\frac{2817}{343}
=\frac{9\cdot313}{343}.
\tag{27}
$$
$313\not\equiv7\bmod64$，所以当前 ray 上二者均为单位；
本篇不增加 R536 固定有限坏集以外的新素数例外。

将五个深输入同时缩放为 $T$，R536 的原固定第一系数为
$\alpha_Y,\alpha_W$。在同一个实际测试下，新的第一系数准确是
$$
\frac db(1+\lambda\kappa)
 \{\alpha_Y+(\kappa^{-m}-1)b_Y\},
\qquad
\frac db(1+\lambda\kappa)
 \{\alpha_W+(\kappa^{-m}-1)b_W\}.
\tag{28}
$$
全部常数 log 项仍因 R536 的整条质量消去而严格为零；
没有忽略 $\kappa^{-m}$ 的分母或将其看成单位。

若 $1\le m<n$，(26)–(27) 使 (28) 的赋值为 $-m$。
高阶系数的下界可写为
$$
v_p([T^r]\mathcal A_{\mathrm{obs},m})\ge
-mr-\lfloor\log_pr\rfloor.
\tag{29}
$$
这里 log 中每一阶最多产生相同次数的 $\kappa^{-m}$，
而 R536 的测试系数仍整。代入 $T=\kappa^n$，对 $r\ge2$，
$$
r(n-m)-\lfloor\log_pr\rfloor>n-m.
$$
所以，连同原五 sigma 的单位因子 $\beta^{5n}$ 和平均的 $1/3$，
$$
\boxed{
\begin{aligned}
v_p\left(\int_{\mathcal D_n}
 d\log\langle Y_m\rangle\,\mathfrak q_{n,p}\,d\rho_0\right)&=n-m,\\
v_p\left(\int_{\mathcal D_n}
 d\log\langle W_m\rangle\,\mathfrak q_{n,p}\,d\rho_0\right)&=n-m.
\end{aligned}}
\tag{30}
$$
这对所有偶数 $m$、$1\le m<n$ 成立，且同一域的质量为零。
取任意奇数 $n\ge3$、$m=n-1$，(30) 两项均准确具有赋值一，
并且其所在的完整原算术域由 (22) 合法控制。

## 8. 准确补域与接续边界

若原两个中央为零，则 (22) 的第一条准确给
$$
\boxed{
0=
\int_{\mathcal D_n}d\log\langle Y_m\rangle\,
                         \mathfrak q_{n,p}\,d\rho_0
+
\int_{\{L\in p^m,Y_m\ {\rm unit}\}\setminus\mathcal D_n}
d\log\langle Y_m\rangle\,
                         \mathfrak q_{n,p}\,d\rho_0.
}
\tag{31}
$$
第二项的来源、三个 carry 分支和全部原输入条件都与第一项相同。
$W_m$ 也有相同的完整分解。
(30) 迫使实际补域给出赋值 $n-m$ 的反号补偿，不能将它删掉。

本篇新增的连接是：一个真正混合原 $Y/W$ 的 whole 核具有完整
两态闭包，而其偶深词保持 R536 的全部有限测试，直接回到两个
已知合格曲线的完整算术行。非零原网格也确在同一合法域内，
并可把其局部赋值降到一。
还未支付的是 (31) 两个实际补域之间的进一步来源关系。
主目标没有由局部非零自动完成。

## 精确证书与依赖

- [check-r539-original-degree8-mixed-st-core.js](../scripts/check-r539-original-degree8-mixed-st-core.js)
- [完整十六项 lift、原六维框架及首项 JSON](../scripts/check-r539-original-degree8-mixed-st-core.json)
- [R536：全部 $\lambda,\kappa$ 的整纤维补偿、严格零质量及三支测试](R536-exact-fibre-mass-compensation-and-invariant-cubic-carry.md)
- [R471：原 sigma/Theta 核的绝对符号](R471-original-six-sigma-normtwo-factor-and-complete-input-carry.md)

证书已在当前 JavaScript 环境中精确执行：CM 几何使用 BigInt
有理数，八维 lift 使用有界精确整数与 $i$ 的四次根计算。
整个矩阵、两个负中心号、Theta 锚子空间和所有实际源系数均已
核定；没有用有限样本推断 entire 核或原两态闭包。
