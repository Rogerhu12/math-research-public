# R414 — 原负块的完整 principal 分离、两条实际辅助来源与中央质量项

日期：2026-11-14。**状态：已证明。** R411 的实际差来源经过任意一轴
的真实 $\mu _6$ 平均后，准确成为两条具体一变量来源的张量。
因此两个 mixed 项的整个双 principal Mellin、所有输出环带和完整
正则化都分解为原两条 rank-two 函数与这一辅助乘积。
辅助第一条正是 R404 的原六次矩列；它不是任意 CM7 本征来源，
本篇给出两个完整纤维的严格反例。辅助中央斜率没有被赋成原曲线斜率。
主目标仍未完成。

## 1. 同一来源中的两条首项一辅助列

沿 R404、R407、R411，固定 $\delta^2=-3$、$\omega=(-1+\delta)/2$、
$E_b:y^2=x^3+b$ 的原 reduced sigma、微分和普通周期。
使用同一
$$
\mathcal C(Z)=\sigma(\delta Z)\sigma(2\delta Z)
              \sigma(\gamma _7Z)\sigma(\bar\gamma _7Z),
\quad \gamma _7=(5+\delta)/2,
$$
$$
F_0=S(2z)T(2w),\quad F_j=B_j(2z,2w)\ (j=2,3),\quad
D=F_2-F_3,
$$
其中 $F_2+F_3=F_0$。定义
$$
\begin{aligned}
H(z)&=\mathcal C(2z)\sigma(3z)^2\sigma(z)^2,\\
G(w)&=\mathcal C(2w)\sigma((4+3\delta)w)^2
                         \sigma((-4+3\delta)w)^2,\\
X&=x(3z),\quad U=x(z),\\
Y&=x((4+3\delta)w),\quad V=x((-4+3\delta)w).
\end{aligned}
\tag{1}
$$
本篇的两条辅助来源准确是
$$
\boxed{
A(z)=-\frac{H(z)(X+U)}{6720},\qquad
B(w)=\frac{G(w)(Y+V)}{14784}.}
\tag{2}
$$
这里 $A\in\mathcal S_{136}(K)$、$B\in\mathcal S_{288}(K)$，
$K=\mathbf Q(\delta)$。分式没有真极：每个 $x(az)$ 的双极被对应的
$\sigma(az)^2$ 消去。所有特征、Gaussian 和 degree 与原二覆盖一致。
在当前 $p>19$ 的普通模型中，(2) 的分母都是单位，来源有界整。
即使 $p$ 整除某一 CM 尺度的范数，整系数线性推前仍有效。

用 $\mathcal C(2z)=-672z^4+O(z^{10})$，直接得到
$$
H(X+U)=-6720z^6+O(z^{12}),\qquad
G(Y+V)=14784w^6+O(w^{12}).
$$
第二式使用
$(4+3\delta)^2+(-4+3\delta)^2=-22$。
所以两条源都首项一、原点质量零：
$$
\boxed{A=z^6+O(z^{12}),\qquad B=w^6+O(w^{12}).}
\tag{3}
$$
R404(24) 的那条实际辅助源 $E$ 满足准确关系
$$
\boxed{A(z)=-\frac{3\delta}{55}E(2z).}
\tag{4}
$$
因此这里没有换掉 R404 的未知辅助中央列。

## 2. 实际三项分离和真实角投影

两次使用 R404 的原 sigma 加法式，得到完整函数身份
$$
\begin{aligned}
42336\delta F_2&=HG(V-X)(U-Y),\\
42336\delta F_3&=HG(Y-X)(V-U).
\end{aligned}
$$
相减给
$$
\boxed{
42336\delta D
=H(X+U)G(Y+V)-2(HXU)G-2H(GYV).}
\tag{5}
$$
这三个张量都由原十二 sigma 来源得出，没有引入一个抽象同型空间。

令 $\Pi _0F(z)=\frac16\sum_{\zeta\in\mu _6}F(\zeta z)$。
原绝对恒等式
$\sigma(\zeta z)=\zeta\sigma(z)$、
$x(\zeta z)=\zeta^{-2}x(z)$ 给
$$
\begin{array}{c|ccc}
\text{第一轴来源}&H&H(X+U)&HXU\\ \hline
\mu _6\text{ 权}&2&0&4
\end{array},\qquad
\begin{array}{c|ccc}
\text{第二轴来源}&G&G(Y+V)&GYV\\ \hline
\mu _6\text{ 权}&2&0&4.
\end{array}
\tag{6}
$$
因此在任意一轴作真实平均就已足够，准确有
$$
\boxed{
(\Pi _0\otimes I)D=(I\otimes\Pi _0)D
=(\Pi _0\otimes\Pi _0)D=c\,A\otimes B,
\qquad c=\frac{7040\delta}{9}.}
\tag{7}
$$
常数由
$-6720\cdot14784/(42336\delta)=7040\delta/9$ 得到。
它对 $p>19$ 是单位；(7) 本身是非零的来源身份。
其首个双角系数正好是 R411 已支付的
$[z^6w^6]D=c$。

还可直接读两个原辅助矩列：
$$
\boxed{[w^6]D=cA(z),\qquad [z^6]D=cB(w).}
\tag{8}
$$
事实上 $G$ 从 $w^8$ 起，而 $GYV$ 的幂次恒为 $4\pmod6$，
所以 (5) 中只有中间权零项贡献 $w^6$；另一轴相同。
例如
$$
[z^6]F_2=32T(2w)+\frac c2B(w),\qquad
[z^6]F_3=32T(2w)-\frac c2B(w).
\tag{9}
$$
普通测度上 (8) 准确表示，保留另一输出后，
$\int V^6\,d\nu_D=720\Omega_p^6c\,d\nu_A$
和另一轴的对应式。这里没有把六次矩换成 principal 中央值。

## 3. 实际输出的完整 principal 函数

固定 R407 的同一个无穷 ray、原普通周期及原输出。
对一变量来源 $G_1$，记
$$
J_{G_1}(u)=\int_{\mathbf Z_p^\times}
                         \langle x\rangle^{du}\,d\nu_{G_1}(x),
\qquad d=p-1.
$$
对二变量来源采用两个独立的实际输出单位条件。

若 $F(\zeta z)=\zeta^kF(z)$，Amice 单射给
$[\zeta]_*\nu_F=\zeta^k\nu_F$。另一方面
$\langle\zeta x\rangle=\langle x\rangle$，且乘 $\zeta$ 保持每一个
输出环带。因此 principal 测试准确杀掉 (6) 中的非零权。
这一步运输了测试函数和完整输出域，不是只对 theta 向量作形式投影。

由 (5)–(7) 得整个单位格上的函数身份
$$
\boxed{
J_D(u,v)=cJ_A(u)J_B(v),
\quad
J_{F_2,F_3}(u,v)=\frac12
  \left[J_{S(2\cdot)}(u)J_{T(2\cdot)}(v)
                 \mathbin{\pm}cJ_A(u)J_B(v)\right].}
\tag{10}
$$
这里 $+$ 对应 $F_2$，$-$ 对应 $F_3$。
同样的等式逐个适用于任意两条输出环带。
更一般，任一轴 tame 指数被 $6$ 整除时仍作这个准确分离；
本篇只需要两个 principal 分支。

对 $|q_1|_p,|q_2|_p<1$，用 R407 的真正连续测试，按输出深度
$n,m$ 加权 $q_1^nq_2^m$，并测试原单位部分 $p^{-n}Y,p^{-m}V$。
记其积分为 $\mathcal R_G(q_1,q_2;u,v)$。
完整收敛式因而也是
$$
\boxed{
\mathcal R_D=c\,\mathcal R_A(q_1;u)\mathcal R_B(q_2;v),
\quad
\mathcal R_{F_2,F_3}
=\frac12\left[
\mathcal R_{S(2\cdot)}(q_1;u)\mathcal R_{T(2\cdot)}(q_2;v)
\mathbin{\pm}c\mathcal R_A(q_1;u)\mathcal R_B(q_2;v)\right].}
\tag{11}
$$
没有删除输入单位相消、原公共八输入或深输出的补域。

## 4. 两条辅助来源的真实 core 和完整中央运输

保持 R407 的
$$
K_1=K_{136}\otimes I,\quad K_2=I\otimes K_{288},\quad
\lambda=\bar\pi^{-1},\quad\beta=\bar\pi^{-2}.
$$
R411(13) 的完整倍点 trace 给
$\operatorname{Tr}_{[2]}r(x_3+x)=0$，故第一条实际来源满足
$$
\boxed{K_{136}A=-A.}
\tag{12}
$$
真实 CM trace 与 $\mu _6$ 作用交换。对 R411 的 $K_2^4D=-D$
使用 (7)，再用 $A\ne0$，得到
$$
\boxed{K_{288}^4B=-B.}
\tag{13}
$$
此外 $B$ 的四条 $B,K_{288}B,K_{288}^2B,K_{288}^3B$ 在 $K$ 上
线性独立：原 trace 及其正规化在 $K$ 上定义，
$X^4+1$ 在 $K=\mathbf Q(\sqrt{-3})$ 上不可约，(3)、(13) 即给
最小多项式准确为 $X^4+1$。扩到当前完备域不改变这个秩。

置
$$
a(q;u)=q\lambda\langle\beta\rangle^{du}.
$$
R407 原全 core 和 (12)、(13) 给
$$
\boxed{
\mathcal R_A(q;u)=\frac{J_A(u)}{1+a(q;u)},\qquad
\mathcal R_B(q;v)=
\frac{\sum_{j=0}^3a(q;v)^jJ_{K_{288}^jB}(v)}{1+a(q;v)^4}.}
\tag{14}
$$
在 $(q,u)=(1,0)$ 处分母都是单位，因为 R407 已证明
$1-\lambda^2$、$1-\lambda^8$ 为单位。
(11) 的每一个实际 mixed 单项因此都有同一个整解析延拓。

### 4.1 质量的准确 telescoping

设 $B_j=K_{288}^jB$、$m_j=B_j(0)$。必须保留全部 $m_j$；
只有 $m_0=0$ 和 $m_4=-m_0=0$ 已经由来源确定。
原全 core 给
$$
J_{B_j}(0)=m_j-\lambda m_{j+1}.
$$
所以
$$
\sum_{j=0}^3\lambda^jJ_{B_j}(0)
=m_0-\lambda^4m_4=0.
\tag{15}
$$
同样 $J_A(0)=0$。于是
$$
\boxed{\mathcal R_A(1;0)=\mathcal R_B(1;0)=0.}
\tag{16}
$$
这里没有从 $B(0)=0$ 偷换成 $J_B(0)=0$；后者实际等于
$-\lambda m_1$，本篇没有令 $m_1$ 为零。

令
$$
\begin{aligned}
\mathfrak a_p&=\frac{J'_A(0)}{1+\lambda},\\
\mathfrak b_p&=\frac1{1+\lambda^4}
\sum_{j=0}^3\lambda^j
 \left[J'_{B_j}(0)+j\,d\log_p\langle\beta\rangle J_{B_j}(0)\right].
\end{aligned}
\tag{17}
$$
这准确是 $\partial_u\mathcal R_A(1;0)$ 和
$\partial_v\mathcal R_B(1;0)$。
第二式中的尺度质量也可用 (15) 写成
$d\log_p\langle\beta\rangle\sum_{j=1}^3\lambda^jm_j$；
它没有被隐去。

原两条 rank-two 中央行仍准确为
$$
\mathfrak s_p=\frac{J'_S(0)}{1-\lambda},\qquad
\mathfrak t_p=\frac{J'_T(0)}{1-\lambda}.
$$
由于 (16) 及原 $S,T$ 质量零，从共同二覆盖返回原输出时的
$\langle2\rangle^{-d(u+v)}$ 在下式的交叉中央系数中不产生额外项。
因而得到完整且已付尺度的中央关系
$$
\boxed{
\begin{aligned}
\partial_u\partial_v\mathcal R_{B_2}(1,1;0,0)
 &=\tfrac12(\mathfrak s_p\mathfrak t_p+c\mathfrak a_p\mathfrak b_p),\\
\partial_u\partial_v\mathcal R_{B_3}(1,1;0,0)
 &=\tfrac12(\mathfrak s_p\mathfrak t_p-c\mathfrak a_p\mathfrak b_p).
\end{aligned}}
\tag{18}
$$
这里左端使用拉回前的 R404 $B_2,B_3$，右端辅助源保持 (2) 的规范。
对整个单位格 (10) 退覆盖时，仍须保留同一个完整尺度函数；
因为 $J_B(0)$ 未必为零，不能把 (18) 的无质量项结论直接复制到
未经正则化的单项单位格。

由 (11)、(16)，两条 mixed 正则化各自属于
$uv\mathcal O\langle u,v\rangle$。
如果两条原曲线中央同时失败，准确得到
$\partial_{uv}\mathcal R_{B_2}=c\mathfrak a_p\mathfrak b_p/2$
及其相反数；这没有迫使任一辅助斜率消失。

## 5. 第一辅助源的完整代数式与真实 CM7 非本征证书

不能仅由固定 ray 上的 (12) 把 $A$ 认作某条椭圆曲线的扭曲来源。
下面给出它在同一代数 theta 模型中的完整式，并严格检验这一点。
在 $b=1$ 的同源缩放模型上，置 $X=x^3$，
$$
\begin{aligned}
R(X)&=X^2+20X-8,\\
P_4(X)&=X(X-8)^3-512(X+1)^3,\\
P_8(X)&=7X^2(X-8)^6-256X(X-8)^3(X+1)^3
                                      +65536(X+1)^6,\\
L(X)&=10X^3-24X^2+192X+64.
\end{aligned}
$$
则准确有
$$
\boxed{
A(z)=\frac1{70}\sigma(z)^{136}x^2
 (X+1)^2(X-8)^2R(X)P_4(X)P_8(X)L(X).}
\tag{19}
$$
这可完全由原 division 式推得。R297 给
$$
\mathcal C(z)=6\sigma^{29}x^2y(X-8)(7X^2-4X+16).
$$
把 $x(2z)=x(X-8)/(4y^2)$、
$y(2z)=R(X)/(8y^3)$、$\sigma(2z)=-2y\sigma^4$ 代入，得到
$$
\mathcal C(2z)=-96\sigma^{116}x^2
(X+1)^2(X-8)^2R(X)P_4(X)P_8(X).
$$
又由三倍点式及 $\psi_3=3x(X+4)$，
$$
\sigma(3z)^2\sigma(z)^2(x(3z)+x(z))
=\sigma^{20}\{2x\psi_3^2-8(X+1)R(X)\}
=\sigma^{20}L(X).
$$
结合 (2) 即得 (19)，包括 $1/70$ 的常数。
其次数为 $65$，首项系数一，故再次核定原点阶六。

### 5.1 两个完整原迹纤维

使用 R297 的真实代数算子
$M_{\gamma _7}=[\gamma _7]_*[\bar\gamma _7]^*$，不加未经定标的
Weil 相位。令
$$
r=(2-6\delta)/7,\qquad \bar r=(2+6\delta)/7,
\quad Q_7(x)=\gamma _7(x^3-r).
$$
在目标横坐标 $a$ 处，全部七个逆像的首一多项式是
$$
f_a(t)=t^7-\gamma _7^2at^6+(28r+12)t^4
       +2\gamma _7^2ar t^3+r(7r+24)t-\gamma _7^2ar^2.
\tag{20}
$$
在 $K[t]/(f_a)$ 中，准确的共轭输出是
$$
x_{\bar7}=
\frac{t\{t^6+(28\bar r+12)t^3+\bar r(7\bar r+24)\}}
     {\bar\gamma _7^2(t^3-\bar r)^2}.
$$
若 $P_A(x)$ 表示 (19) 的整个 sigma 后多项式，真实迹为
$$
\boxed{
\frac{M_{\gamma _7}A}{\sigma^{136}}(a)
=[t^6]\left[
 \left(\frac{\bar\gamma _7(t^3-\bar r)}
            {\gamma _7(t^3-r)}\right)^{136}
 P_A(x_{\bar7})f_a'(t)\bmod f_a(t)\right].}
\tag{21}
$$
这是完整七点 trace，不是截取局部系数。

在精确有限域 $\mathbf F_{1009}$ 中取 $\delta=260$。
于是 $\gamma _7=637$、$\bar\gamma _7=377$，
所有写出的有理常数分母均可逆。脚本按 (19)–(21) 直接得到

| $a$ | $P_A(a)$ | $(M_{\gamma _7}A)/\sigma^{136}$ | 准确比值 |
|---|---:|---:|---:|
| $1$ | $262$ | $655$ | $507$ |
| $3$ | $7$ | $403$ | $490$ |

两个 $P_A(a)$ 都非零，比值相差 $17\ne0$。
为把分母和可分性也明确付清，证书逐个输出并乘回验证
$(t^3-r)^{-1}$、$(t^3-\bar r)^{-1}$、$(f_a')^{-1}$
在两个商环中的完整多项式。
两份 $f_a$ 的升幂系数分别为
$$
(70,815,0,963,843,0,858,1),\qquad
(210,815,0,871,843,0,556,1).
$$
因此 (21) 在这两个纤维确有良好约化。
若特征零中 $M_{\gamma _7}A=\alpha A$，则比较两个纤维的交叉乘积
必须为零；其约化却为非零。严格得到
$$
\boxed{A\text{ 不是原 }M_{\gamma _7}\text{ 的任何标量本征向量。}}
\tag{22}
$$
同源缩放返回 $b=17$ 不改变这个结论。
这只排除未经支付的单本征来源识别，不否认 $A$ 可以有多个算术
特征分量；那些分量的原中央运输仍须另证。

## 6. 已付接口与仍须推进的桥梁

本篇把 R411 的真实负块在目标 principal 测试下从二变量四态问题
准确压成 (2) 的两个一变量来源；第二条仍需全部四个真实 core 状态。
原 mixed 中央与原 rank-two 中央的关系完整写成 (17)、(18)，
包括第二轴尚不能删除的尺度质量项。

若继续用另一合法 Riemann 输出或真实非交换对称，需要将 (2) 的
实际测试输出送回原 $S,T$ 的完整中央泛函。
单凭 (12)、(13)、非零首矩或 (7) 的张量分离没有做成这一步。
(22) 又排除了仅看固定 ray 的负号就将 $A$ 称作另一条单 CM 曲线
来源的捷径。

## 7. 精确证书与依赖

脚本 `scripts/check-original-negative-principal-sources.py` 只使用 Python
标准库，执行 (19)–(21) 的两份完整有限域纤维，验证每个商环逆元，
输出所有输入多项式和准确反例比值；同名 JSON 保存输出。
它不扫描目标素数，也不以数值近似证明任何中央非零。

- [R297：原代数来源与完整 CM trace](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R404：原 mixed 联合与六次辅助矩](R404-two-original-ranktwo-riemann-joint-and-complete-two-axis-central-transport.md)。
- [R407：同一二覆盖及整的完整正则化](R407-original-riemann-cover-finite-cores-and-integral-regularization.md)。
- [R411：实际交换、完整二挠 trace 与四态负谱](R411-original-mixed-swap-and-four-state-negative-core.md)。
