# R401 — E24 的精确中央常数、原四个模符号与全部好素数单位性

日期：2026-11-14。**状态：以下精确特殊值、全部实/CM 周期换算及原来源的固定整数常数已证明。没有使用 BSD 公式、数值认数或未知高度。主目标的无穷中央非零仍未证明。**

本篇付清 R397、R402 中保留的固定非零数
$
 \kappa_{24}=\frac{L(E_{-8},1)}{6\Omega_{24}},
 \qquad E_{-8}:y^2=x^3-8 .
$
准确结论是
$
 \boxed{\frac{L(E_{-8},1)}{\Omega_1}=\frac1{\sqrt6},
 \qquad
 \kappa_{24}=\frac1{6\sqrt[3]3}.}
 \tag{1}
$
所有根在原实嵌入取正值。
因此 $\kappa_{24}$ 在每个 $p>3$ 的每个代数完成处都是单位。

R398 的实际源 $\Phi_{24}=a_{24}T_{24}$ 有
$
 a_{24}=-145152\sqrt[3]9=-6048\cdot24\sqrt[3]9,\qquad
 T_{24}=z^6+\cdots .
$
对于这个真实首项一来源，完整实常数成为固定整数
$
 \boxed{\widetilde\kappa_{24}:=\kappa_{24}a_{24}^2
 =2^{15}3^8 7^2=10534551552.} \tag{2}
$
它在所有 $p\notin\{2,3,7\}$ 为单位。
原未除首项来源的 $\kappa_{24}$ 与首项一来源的
$\widetilde\kappa_{24}$ 不可混用，尤其在七处。

## 1. 已出版的实际模形式及固定原函数

令
$
 E_1:y^2=x^3+1,\qquad
 f(\tau)=\eta(6\tau)^4=\sum_{n\ge1}a_n e^{2\pi in\tau}.
 \tag{3}
$
Martin–Ono (1997), Theorem 2 的 conductor36 行明确给出：
这个标准首项一 eta newform 的 Hasse–Weil 曲线就是
$(a_1,a_2,a_3,a_4,a_6)=(0,0,0,0,1)$。
因此其完整 L 函数是 $L(E_1,s)$。
这里没有借助数值吻合来识别模形式。

在上半平面定义实际 Eichler 原函数
$
 \mathcal F(\tau)=\sum_{n\ge1}\frac{a_n}{n}e^{2\pi in\tau}
 =2\pi i\int_{i\infty}^{\tau}f(z)\,dz,\qquad
 \mathcal F(i\infty)=0.
 \tag{4}
$
它在有理 cusp 的值按上半平面极限取，存在且为相应模符号。
令
$
 L_1=L(E_1,1)>0,\qquad
 F(u)=\frac{\mathcal F(u/6)}{L_1},\qquad
 \zeta=\exp(\pi i/3)=\frac{1+\delta}{2},\quad\delta=\sqrt{-3}.
$
沿正虚轴的 Mellin 积分给
$
 F(0)=1,\qquad F(i\infty)=0. \tag{5}
$
R302 已独立由六个原 Kronecker 点证明
$
 \boxed{L_1=\Omega_1/6,} \tag{6}
$
其中 $\Omega_1$ 是 $dz=dx/(2y)$ 下的 primitive 正实周期。
本篇只使用这个已经付清的周期规范，不从 BSD 推出 (6)。

## 2. 两个精确变换，包含原函数的常数

Dedekind eta 的标准变换
$
 \eta(u+1)=e^{\pi i/12}\eta(u),\qquad
 \eta(-1/u)=(-iu)^{1/2}\eta(u)
$
在四次幂后没有平方根选择的残留，给
$
 \eta(u+1)^4=\zeta\eta(u)^4,\qquad
 \eta(-1/u)^4=-u^2\eta(u)^4.
$
对 (4) 求导并使用 $F(i\infty)=0,F(0)=1$，得到
$
 \boxed{F(u+1)=\zeta F(u),\qquad F(-1/u)=1-F(u).} \tag{7}
$
第二式右边的一不能删除：
其导数和为零，令 $u\to i\infty$ 才准确确定该常数。

这些是原函数的全恒等式，因而在所有有理端点的 cusp 极限成立。
不是仅知道两个函数的导数或模周期相等。
尤其没有将模符号的周期绕数丢掉。

## 3. 原四个端点的完整精确求值

设 $\chi=\chi_{-8}$ 为模八的 primitive 奇二次特征，
$
 \chi(1)=\chi(3)=1,\qquad \chi(5)=\chi(7)=-1,
$
偶数上为零。需要的原端点是 $\tau=a/8$，
对应 $u=3a/4$，不是 $a/8$ 直接代入 (7)。

仅使用 $\zeta^2-\zeta+1=0$ 与 (7)，先得
$
 \begin{aligned}
 F(1/2)&=1-\zeta^{-2},\\
 F(2/3)&=1-\zeta^{-2}F(1/2),\\
 F(3/4)&=1-\zeta^{-2}F(2/3)
       =-\zeta^{-2}+\zeta^{-4}=2\zeta-1=\delta,\\
 F(1/4)&=1-\zeta^{-4}.
 \end{aligned} \tag{8}
$
再平移整数二、三、五，得到准确表
$
 \boxed{
 \begin{array}{c|c|c|c}
 a&u=3a/4&\chi(a)&F(u)\\ \hline
 1&3/4&1&\delta\\
 3&9/4&1&\delta\\
 5&15/4&-1&-\delta\\
 7&21/4&-1&-\delta
 \end{array}.}
 \tag{9}
$
例如 $F(9/4)=\zeta^2(1-\zeta^{-4})=\delta$，
$F(21/4)=\zeta^5(1-\zeta^{-4})=-\delta$。
因此原完整加权和为
$
 \sum_{a\bmod8}\chi(a)\mathcal F(a/8)=4\delta L_1. \tag{10}
$
所有四个 cusp 和全部常数都在表中；没有遗漏一个权为零以外的陪集。

## 4. 原 Gauss 和与完整二次扭曲 L 值

直接计算该 primitive 特征的 Gauss 和：
$
 \tau(\chi)=e^{2\pi i/8}+e^{6\pi i/8}
            -e^{10\pi i/8}-e^{14\pi i/8}
           =2i\sqrt2. \tag{11}
$
对 $\operatorname{Im}\tau=\varepsilon>0$，所有 Fourier 和绝对收敛，
有限 Gauss 恒等式给
$
 \sum_{a\bmod8}\chi(a)\mathcal F(a/8+i\varepsilon)
 =\tau(\chi)\sum_{n\ge1}
       \frac{a_n\chi(n)}{n}e^{-2\pi n\varepsilon}. \tag{12}
$
令 $\varepsilon\downarrow0$。
右边的 Abel 极限等于扭曲 cusp form 的 Mellin 值 $L(f\otimes\chi,1)$；
这也可由其 cusp 两端的指数衰减直接积分证明。
因此这里没有在条件收敛点未经说明地重排无限和。

$E_{-8}$ 正是 $E_1$ 的二次扭曲 $d=-2$：
短 Weierstrass 的常数乘 $d^3=-8$，其 primitive 判别式特征为
$\chi_{-8}$。
好素数处的迹因此为 $a_\ell\chi(\ell)$。
二、三处两曲线均为 additive，原 Euler 因子均为一；
R395 已付新导子 $(8\delta)$、经典 conductor576。
所以 (12) 插值的是完整
$
 L(f\otimes\chi,s)=L(E_{-8},s),
$
不是再删过坏位的 L 函数。

联立 (10)–(12)，得到
$
 \boxed{
 L(E_{-8},1)=\frac{4\delta}{2i\sqrt2}L_1
            =\sqrt6\,L_1=\frac{\Omega_1}{\sqrt6}.}
 \tag{13}
$
正号与原正实 L 值完全一致，不需要在最后任选代数根。

## 5. 实周期、CM 周期与两种来源常数

R393、R398 的实际物理模型满足
$
 \Omega_{24}=\Omega_1/24^{1/6}.
$
因此 (13) 给
$
 \kappa_{24}
 =\frac{24^{1/6}}{6\sqrt6}
 =\frac1{6\sqrt[3]3},
$
证明 (1)。
作为独立周期核对：$E_1$ 的格为
$\Omega_1(\mathbf Z+s\mathbf Z)$，其最短纯虚周期为
$\Omega_1(2s-1)=i\Omega_1/\sqrt3$。
二次同构使用 $u=\sqrt{-2}=i\sqrt2$，故 $E_{-8}$ 的正实周期是
$\Omega_1/\sqrt6$。所以 (13) 也给
$L(E_{-8},1)/\Omega_{-8}=1$，而这不是本证明使用的 BSD 输入。

再乘 R398 的实际 $a_{24}^2$，有
$
 \kappa_{24}a_{24}^2
 =\frac{6048^2\,24^2\,3^{4/3}}{6\,3^{1/3}}
 =\frac{6048^2\,24^2}{2}
 =2^{15}3^8 7^2 .
$
这证明 (2)。

若 $T_{24}=\sum t_mz^m$，R397 的完整实周期公式现在明确为
$
 \boxed{
 \frac{(2\pi/\sqrt3)^mL(\psi_{24}^{2m+1},m+1)}
      {m!\Omega_{24}^{2m+1}}
 =10534551552\cdot216^{-m}t_m^2,
 \qquad6\mid m.}
 \tag{14}
$
换到 CM 生成周期 $s\Omega_{24}$，则完整公式是
$
 \boxed{
 \frac{(2\pi/\sqrt3)^mL(\psi_{24}^{2m+1},m+1)}
      {m!(s\Omega_{24})^{2m+1}}
 =(1-\omega)10534551552\cdot72^{-m}t_m^2.}
 \tag{15}
$
中央 $s^{-1}=1-\omega$ 和权因子三的变化同时保留。
对实际未除首项的 $\Phi_{24}$，将整数
10534551552 换回 $\kappa_{24}$，并把 $t_m$ 换为 $s_m=a_{24}t_m$。

## 6. 对原普通与惰性接口的直接影响

R397 的原普通恒等式现在具有完全指定的常数
$
 \mathcal K_{24,p}(T)=
 \frac{1-\omega}{6\sqrt[3]3}\,\Omega_p
 (1+T)^{-a_{72,p}}G_{24,p}(T)^2 .
 \tag{16}
$
固定因子在所有普通好 $p>3$ 为单位。
若改用首项一来源，则固定常数为
$(1-\omega)10534551552$，七处的区别仍须保留。

R402 为新惰性分支保留的准确式是
$
 \operatorname{ord}A_p=2e,\qquad
 v_p([T^{2e}]A_p)=v_p(\kappa_{24})+2v_p(j_e)-2e .
$
本篇已经证明 $v_p(\kappa_{24})=0$ 对其全部 $p\ge11$ 成立，
故可明确简写为
$
 \boxed{v_p([T^{2e}]A_p)=2v_p(j_e)-2e.} \tag{17}
$
所有 Gaussian、物理/共同 frame、Euler 和阶乘依然使用 R402 的原式。
(17) 支付固定常数的单位性，并不支付随 $p$ 变化的 $j_1\ne0$。

至此新曲线的原整体常数不再是未指定代数数，也没有新的坏素数集。
无穷多个素数的整个中央导数非零，仍需在两个真实 rank-two 来源中证明。

## 出处与精确复现

- Y. Martin、K. Ono，*Eta-quotients and elliptic curves*，
  Proc. Amer. Math. Soc. **125** (1997), no. 11, 3169–3176，
  Theorem 2 的 conductor36 行：
  [作者全文](https://uva.theopenscholar.com/files/ken-ono/files/026_8.pdf)，
  [DOI](https://doi.org/10.1090/S0002-9939-97-03928-2)。
  本篇只用该已发表的实际 $f=\eta(6\tau)^4$ 与曲线对应。
- [R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)：
  原微分、CM 格和 $L(E_1,1)/\Omega_1=1/6$ 的六点精确证明。
- [R395](R395-e24-six-actual-translates-fixed-divisor-and-square-normalization.md)、
  [R398](R398-e24-actual-polynomial-six-sigma-source-and-original-central-comparison.md)：
  E−8 的原局部输入以及新实际来源的整体常数。
- [R397](R397-e24-original-ordinary-square-and-full-selmer-bridge.md)、
  [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)：
  原普通/惰性完整桥。

(8)–(10) 在整数环 $\mathbf Z[\zeta]/(\zeta^2-\zeta+1)$ 中运算：
四个值的 $(1,\zeta)$ 列依次为
$(-1,2),(-1,2),(1,-2),(1,-2)$，
加权和为 $(-4,8)=4\delta$。
(11) 是四项明确 Gauss 和，(13)–(17) 只余有理幂运算；
故本篇的数值全由固定符号身份确定，不依赖高精度浮点数。
