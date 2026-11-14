# R549 — 原六度负矩的真实 Cartier 行、Verschiebung 覆盖与固定幂普通归一

日期：2026-11-14。**状态：以下是同一 $f_4=x_\wp\sigma^6$、$f_1=-x_\wp y_\wp\sigma^6$ 的完整第一层几何识别。已显式构造原第二类微分的模 $p$ 原函数，准确认出 sigma 对数导数的 Artin–Schreier 方程为原 Verschiebung 覆盖，并把两条负矩写成该来源上真实的 Cartier 观察及一个无共振分母的有限二项式表达。剩余二次／五次椭圆积分没有删除；其实际幂零连接的 $p$-curvature 非零。本篇未证明固定负矩非零或其第一层无穷次非零。**

本篇继续 [R540](R540-original-degree-six-schwartz-full-weight-and-negative-two-katz.md)
的实际角色 $\xi$、普通地点、微分和原测度。
没有以“普通”替代这个固定角色的 Katz 值，也没有扩大已有素数样本。

## 1. 原来源、普通曲线与最终有限公式

固定 $b=17$；以下代数计算亦适用于任意 $p$ 进单位 $b$。
令
$$
p=6s+1>7,\qquad r=s-1,\qquad
h_s=\binom{3s}{s},\qquad \mathfrak h_p=b^s h_s\in\mathbf F_p^\times.
\tag{1}
$$
在 $\bar E_b:y^2=x^3+b$ 上取
$$
\omega_E=\frac{dx}{2y},\qquad
D=2y\frac{\partial}{\partial x}+3x^2\frac{\partial}{\partial y},\qquad
\omega_E(D)=1.
$$
原形式群周期为 $\Omega_p$，满足
$\beta^*\omega_E=\Omega_p\,dT/(1+T)$。
两条实际单位域负矩为
$$
I_4=\int_{\mathbf Z_p^\times}X^{-2}\,d\nu_{f_4}(X),\qquad
I_1=\int_{\mathbf Z_p^\times}X^{-5}\,d\nu_{f_1}(X).
\tag{2}
$$
积分变量用 $X$，以免与椭圆函数 $x$ 混淆。

在 $\mathbf F_p[t]/(t^s)$ 中定义
$$
\begin{aligned}
C(t)&=\sum_{n=0}^{s-1}\binom{3s}{n}t^n,\\
H(t)&=\sum_{n=0}^{s-1}\frac{\binom{3s}{n}}{6n+1}t^n,\\
Q(t)&=h_s^{-1}\sum_{n=0}^{s-1}\binom{3s}{s+n}t^n,\\
S_w(t)&=\exp\left(\sum_{n=1}^{s-1}
 \frac{\binom{3s}{s+n}}{n h_s}t^n\right).
\end{aligned}
\tag{3}
$$
指数函数只取到次数 $s-1$，所以所有阶乘及所写分母都是单位。
置
$$
\boxed{c_{4,p}=[t^{s-1}]H(t)^2C(t)S_w(t),\qquad
c_{1,p}=[t^{s-1}]H(t)^5S_w(t).}
\tag{4}
$$
它们正是已发布第一层笔记中的原 $AS$、$ABS$ 对角，不是另外的近似量。

本篇的固定幂普通归一是
$$
\boxed{
I_4\equiv-\frac{c_{4,p}}{2b h_s\Omega_p^2}\pmod p,\qquad
I_1\equiv\frac{c_{1,p}}{120b h_s\Omega_p^5}\pmod p.}
\tag{5}
$$
其分母全为单位。因此 $c_{4,p}\ne0$ 与 $I_4$ 是单位等价；
$c_{1,p}\ne0$ 与 $I_1$ 是单位等价。
系数为零只说明相应矩属于 $p\mathcal O$，不说明该 $p$ 进数为零。

下面证明 (3)–(5) 的原 Cartier 来源，以及普通 Hasse 条件仍没有支付的项。

## 2. Hasse、restricted derivation 与唯一第二类原函数

Cartier 的代数公式直接给
$$
\begin{aligned}
\omega_E&=\frac{(x^3+b)^{(p-1)/2}}{2y^p}\,dx,\\
\mathcal C(\omega_E)&=\mathfrak h_p\,\omega_E,\qquad
D^{[p]}=D^p=\mathfrak h_pD.
\end{aligned}
\tag{6}
$$
的确，$(x^3+b)^{3s}$ 中 $x^{p-1}=x^{6s}$ 的系数为
$\binom{3s}{2s}b^s=\mathfrak h_p$；其余指数都不给 Cartier 的 regular 一维项。
最后一个式子是 Cartier 与 invariant derivation 的标准对偶关系，
亦可由 $D^p$ 仍为 invariant vector field、在原点比较该同一系数直接得到。
$3s<p$，故 (1) 的 Hasse 值确实非零。

第二类微分 $\eta=-x\omega_E$ 在这里有一个特别简单的真实原函数。
定义
$$
z_0=-\frac1{4b},\qquad
z_j=-\frac{6j+1}{(6j+4)b}z_{j-1}\quad(1\le j\le s-1),
$$
$$
\boxed{\zeta_p=y\sum_{j=0}^{s-1}z_jx^{3j+2}\in L(pO).}
\tag{7}
$$
这是原曲线上的有理函数。直接求导：
$$
D(yx^{3j+2})=(6j+7)x^{3j+4}+(6j+4)b\,x^{3j+1}.
$$
中间项由递推相消，第一项给 $-x$，末项的系数是
$6(s-1)+7=p=0$，所以
$$
\boxed{D\zeta_p=-x,\qquad d\zeta_p=\eta.}
\tag{8}
$$
所有分母 $6j+4$ 都小于 $p$。该函数在 $\mu_6$ 下型为 $-1$。

这还是 $L(pO)$ 中该型的唯一原函数。若两个之差的导数为零，
差属于 $\overline{\mathbf F}_p(E)^p$；其 $p$ 次根至多在 $O$ 有一个简单极点。
椭圆曲线上 $L(O)$ 只有常数，且常数没有型 $-1$，故差为零。

(6)、(8) 还准确给出绝对首项。函数
$D^{p-1}\zeta_p-\mathfrak h_p\zeta_p$ 的导数为零、极点至多为 $pO$，
且仍具有型 $-1$，所以
$$
D^{p-1}\zeta_p=\mathfrak h_p\zeta_p.
\tag{9}
$$
在原点的参数 $w=x^{-1/2}=z+\cdots$ 中，
$D=\sqrt{1+bw^6}\,d/dw$。左端等于 $-D^{p-2}x$，
其 $w^{-p}$ 首系数为 $-1$：最高极点项只用 $d/dw$，
再用 $(p-1)!\equiv-1$。因此
$$
\boxed{\zeta_p=-\mathfrak h_p^{-1}w^{-p}+w^{-1}
       +\text{正次项},\qquad z_{s-1}=\mathfrak h_p^{-1}.}
\tag{10}
$$
没有从一个数值 Gauss 和选择这个符号。

若改用真正有理的 Néron 参数 $\tau=-x/y$，则
$$
\boxed{\zeta_p=-\mathfrak h_p^{-1}\tau^{-p}+\tau^{-1}+O(\tau).}
\tag{11}
$$
因为减去最高 $p$ 次极点后，(8) 排除所有其他大于一的负次极点；
余下简单极点的系数由 $D\zeta_p=-x$ 固定为一。

## 3. 原 sigma 的 Artin–Schreier 方程就是 Verschiebung

令 $\bar\sigma(\tau)$ 是原整 ordinary sigma 在 $\mathbf F_p[[\tau]]$ 中的约化。
R295／R300 的三次 CM 规范给
$$
\bar\sigma=\tau+\cdots,\qquad
g=D\log\bar\sigma,\qquad Dg=-x.
$$
这里没有另加一个二次 Gaussian。

对导数的 Leibniz 公式，特征 $p$ 下有
$$
\frac{D^p\bar\sigma}{\bar\sigma}=D^{p-1}g+g^p.
$$
结合 (6)、(8)、(9)，得到完整形式恒等式
$$
\boxed{g^p-\mathfrak h_p g=-\mathfrak h_p\zeta_p.}
\tag{12}
$$
它不是只对若干 Taylor 系数成立。

考虑由
$$
v^p-\mathfrak h_pv=-\mathfrak h_p\zeta_p
\tag{13}
$$
定义的曲线及其光滑射影模型。除 $O$ 外右端没有极点。
在 $O$ 用 (11) 作 $v'=v-\tau^{-1}$，右端变为正则函数；
对 $v'$ 的导数是 $-\mathfrak h_p\ne0$。因此这是处处 étale 的 $p$ 次覆盖。

该覆盖在代数闭包上连通。否则 Artin–Schreier 方程有有理函数根；
任何根在 $O$ 外无极点，在 $O$ 只有简单极点，因为其 $p$ 次方的极点阶为 $p$。
这会给出椭圆曲线上的非恒定 $L(O)$ 函数，矛盾。
所以覆盖是 genus 一的真实 étale $p$-isogeny。

还可用原 division 函数绝对识别它。设
$$
V=[\bar\pi_b]:\bar E_b^{(p)}\longrightarrow\bar E_b,\qquad
\bar\pi_b=\psi_b(\bar{\mathfrak p}),
$$
为原 Verschiebung，其导数为 $\mathfrak h_p$。
令 $r_V$ 是 R300 原
$r_{\bar\pi_b}=\sigma(\bar\pi_b z)/\sigma(z)^p$ 的约化。
其 divisor、首项及整个形式恒等式为
$$
\operatorname{div}(r_V)=V^*[O]-p[O],\qquad
r_V=\mathfrak h_p\tau^{1-p}+\cdots,
$$
$$
\boxed{\bar\sigma(V\tau)=r_V(\tau)\bar\sigma(\tau)^p,\qquad
g\circ V=\mathfrak h_p^{-1}D\log r_V.}
\tag{14}
$$
这里 $V\tau$ 表示源形式参数经 $V$ 的真实级数。
(14) 来自同一 characteristic-zero division 身份再约化，保原奇半特征与首项。
它给出 (13) 到原 $V$-cover 的带原点识别，排除了只知“同构到某个覆盖”留下的标量。

特别地，
$$
\boxed{f_4(V\tau)
 =x(V\tau)\,r_V(\tau)^6\,\bar\sigma(\tau)^{6p}.}
\tag{15}
$$
所以 sigma 部分在这个真实覆盖上已代数化为原 division 函数，
其余因子准确是 Frobenius 的 $p$ 次方。
(13) 的阶 $p$ 加性覆盖不是 R540 的阶三有限角色 $\xi$；
不能用前者替换后者的 Katz 分量。

## 4. 两个指定负矩究竟是哪两条 Cartier 行

原第一层笔记已经证明
$$
I_4\equiv\Omega_p^{p-3}(p-3)![z^{p-3}]f_4,\qquad
I_1\equiv\Omega_p^{p-6}(p-6)![z^{p-6}]f_1\pmod p.
\tag{16}
$$
其中先在单位域用 Fermat，再补全域；没有假定所求 scalar core。

令 $\ell(\tau)$ 为原椭圆积分 $z=\int\omega_E$ 在次数小于 $p$ 的截断。
它由原 characteristic-zero 级数得到，这一范围分母不含 $p$。
最高的不可积项位于 $\tau^{p-1}d\tau$，故不宣称 $\ell$ 是特征 $p$ 下的完整原函数。
然而 $f_4$、$f_1$ 的首阶分别为四、一，所以以下观察只用合法截断：
$$
\boxed{
\begin{aligned}
\left.\mathcal C(\ell^2 f_4\omega_E)\right|_O
 &= [z^{p-3}]f_4\cdot\left.\omega_E\right|_O,\\
\left.\mathcal C(\ell^5 f_1\omega_E)\right|_O
 &= [z^{p-6}]f_1\cdot\left.\omega_E\right|_O.
\end{aligned}}
\tag{17}
$$
证明是在任意正规参数中用
$\mathcal C(\sum a_n\tau^n d\tau)
 =\sum a_{pn+p-1}^{1/p}\tau^n d\tau$。
原系数在 $\mathbf F_p$ 内，$p$ 次根不改变它们。
$\ell$ 的更高补项、以及 $d\ell-\omega_E$ 的首个共振，都被
$\ell^2f_4$ 或 $\ell^5f_1$ 的至少六阶零推出 $\tau^{p-1}$ 之外。
因此 (17) 不依赖未经支付的高次原函数。

(15) 确实消掉了 sigma 的非代数部分，但 (17) 的 $\ell^2,\ell^5$ 仍在。
它们不是原 Hasse 观察 $\mathcal C(\omega_E)|_O$。

## 5. 从原 $AS/ABS$ 到完整有限二项式行

在特征零先取 $w=x^{-1/2}$、$t=bw^6$，再于合法次数约化。
由于 $y=-w^{-3}\sqrt{1+t}$，
$$
z(w)=wH(t),\quad C(t)=(1+t)^{-1/2},\quad
6tH'(t)+H(t)=C(t),
$$
$$
H(t)=\sum_{n\ge0}
 \frac{(-1)^n\binom{2n}{n}}{4^n(6n+1)}t^n.
\tag{18}
$$
写 $\zeta(z(w))=w^{-1}Z(t)$；由 $d\zeta=-x\,dz$，
$$
Z(t)=1-\sum_{n\ge1}
 \frac{(-1)^n\binom{2n}{n}}{4^n(6n-1)}t^n.
\tag{19}
$$
令
$$
S_w(t)=\left(\frac{\sigma(z(w))}{w}\right)^6,\qquad
L(t)=\log S_w(t).
$$
则
$$
\boxed{tL'(t)=Z(t)C(t)-1.}
\tag{20}
$$

这里有准确的固定系数表达：
$$
Q(t):=Z(t)C(t)=\sum_{n\ge0}q_nt^n,\qquad
q_0=1,\quad
\boxed{q_n=(-1)^n\prod_{j=1}^n\frac{6j-4}{6j-1}.}
\tag{21}
$$
可由 (18)、(19) 的二项式卷积直接验证；等价地两边满足
$6t(1+t)Q'+(2t-1)Q+1=0$、$Q(0)=1$。
因此原 sigma 的这一固定坐标还满足完整非齐次方程
$$
\boxed{6t(1+t)L''+(5+8t)L'+2=0,\qquad L(0)=0.}
\tag{22}
$$
常数项二保留；没有以齐次周期替代原来源。

在 $\mathbf F_p$ 中，
$(-1)^n\binom{2n}{n}/4^n=\binom{3s}{n}$ 对 $n<p$ 成立；
对于 $0\le n<s$，(21) 又准确给
$$
\boxed{q_n=\frac{\binom{3s}{s+n}}{\binom{3s}{s}}.}
\tag{23}
$$
因为中段比值递推为
$(2s-n+1)/(s+n)=-(6n-4)/(6n-1)$。
(18)、(20)、(23) 正是 (3)。

(23) 也直接可在原 $V$-cover 读出。由 (10) 及无其他负次极点，
(7) 的反向多项式为
$$
\sum_{k=0}^{s-1}z_{s-1-k}b^{-k}t^k
 =\mathfrak h_p^{-1}\sum_{k=0}^{s-1}\binom{-1/2}{k}t^k.
$$
将它代入 (12)，在次数小于 $2s$ 的实际范围得到
$$
Z(t)C(t)=\frac{1}{h_st^s}
 \left(C(t)-\sum_{k=0}^{s-1}\binom{-1/2}{k}t^k\right)
 \pmod{t^s},
$$
再次给 (23)。这把有限式与真实 isogeny 对齐，不仅给一个形式重写。

现在返回原笔记的变量 $u=bz^6$，在那里
$$
A(u)=z^2x,\quad B(u)=-z^3y,\quad S(u)=(\sigma/z)^6.
$$
完整坐标关系是
$$
u=tH(t)^6,\qquad
A=H^2,\quad B=H^3/C,\quad S=S_w/H^6.
\tag{24}
$$
Lagrange 的 residue 形式因而给
$$
[u^r]AS=[t^r]S_w C\,H^{-6r-5},\qquad
[u^r]ABS=[t^r]S_w\,H^{-6r-2}.
\tag{25}
$$
$r=s-1$ 时，指数分别为 $2-p,5-p$。
$H(t)^p\equiv1\bmod t^s$，所以 (25) 准确化为 (4)。

这一步保留全部 $H^2$ 或 $H^5$；不能在 (25) 中只保 sigma 或 Hasse 因子。
所用有限环的全部分母无 $p$；首次共振
$$
6s+1=p,\qquad [t^s]C=h_s\ne0
\tag{26}
$$
恰在 $H$ 的下一项。它是原椭圆积分的真实 Hasse forcing，
而不是已证明 $[t^{s-1}]H^2CS_w$ 非零的理由。

## 6. 原普通周期把变权幂准确降为固定幂

同一形式群同构满足，在模 $p$ 后
$$
[p]_{\bar E_b}(\tau)=\mathfrak h_p\tau^p+\cdots,\qquad
[p]_{\widehat{\mathbf G}_m}(T)=T^p.
$$
比较 $\beta(T)=\Omega_pT+\cdots$ 的首项，得到
$$
\boxed{\mathfrak h_p\Omega_p^p=\Omega_p,\qquad
\Omega_p^{p-1}=\mathfrak h_p^{-1}\pmod p.}
\tag{27}
$$
这使用原普通地点和原微分，不是随意选择周期的余类。

又
$$
(p-3)!\equiv-\frac12,\qquad (p-6)!\equiv\frac1{120}\pmod p.
$$
(24)、(25) 给
$[z^{p-3}]f_4=b^{s-1}c_{4,p}$、
$[z^{p-6}]f_1=b^{s-1}c_{1,p}$。
将这些式子和 (27) 代入 (16)，便得到 (5)。

因此第一层已经是固定幂 $\Omega_p^{-2}$、$\Omega_p^{-5}$，
不必继续携带随 $p$ 变化的 $\Omega_p^{p-3}$、$\Omega_p^{p-6}$。
但所有归一因子都是单位这一事实，仍只把非消失等价到 (4) 的指定有限行。

R540 在基曲线 $E_0$ 上识别的导子 $(6)$ 角色 $\xi$、primitive Katz 负点和
返回 $b=17$ 的 $\theta^9$ 常数完全保留。
(6)–(27) 是对同一物理来源的模 $p$ 计算；$\mathfrak h_p$ 不能代替
$\xi(\mathfrak p)$，Verschiebung 也没有把原普通地点换成共轭地点。

## 7. 剩余项的准确 $p$-curvature，及所余非消失任务

为标清为何 (17) 不能只用普通 Hasse 定理结束，取原曲线上的实际连接
$$
\mathscr U_q=(\mathcal O_{\bar E_b}^{\,q+1},\,\nabla=d-N_q\omega_E),
\qquad q=2,5,
$$
其中 $N_q$ 是一个 $(q+1)$ 阶单 Jordan 幂零块。
它的原点截断水平解含 $1,\ell,\ldots,\ell^q/q!$，
故正好保留 (17) 的二次、五次测试。这里只说到共振前的截断，
不声称 $\omega_E$ 在特征 $p$ 下有完整形式原函数。

按标准定义
$\Psi_\nabla(D)=\nabla_D^p-\nabla_{D^{[p]}}$，
由于 $D$ 与常数矩阵 $N_q$ 交换、$p>q+1$，(6) 给
$$
\boxed{
\Psi_{\mathscr U_q}(D)
 =(D-N_q)^p-\mathfrak h_p(D-N_q)
 =\mathfrak h_pN_q.}
\tag{28}
$$
其秩分别是二、五，均非零。这个计算保留了矩阵的符号与原 Hasse 标量。

因而“sigma 已在原 $V$-cover 代数化”与“把 (17) 化为 regular Hasse 行”
是两个不同步骤。前一步已经由 (14)、(15) 完成；
后一步仍含 (28) 的实际幂零连接，不能套用零 $p$-curvature 的 Cartier descent
把整个测试删除。这里只排除这一未经支付的推论，并不排除以后从
(3)、(22)、(26) 找到更强的实际系数恒等式。

当前得到的是一份完整有限问题：
$$
[t^{s-1}]\,H(t)^2C(t)
 \exp\!\left(h_s^{-1}\sum_{n=1}^{s-1}
       \binom{3s}{s+n}\frac{t^n}{n}\right)\ne0
\tag{29}
$$
若在本题射线上无穷次成立，则同一 $I_4$ 在这些素数是单位。
要证明固定 $I_4$ 本身非零，也可研究更深层；一次 (29) 为零并不否定它。
反过来，$\mathfrak h_p\ne0$、(13) 覆盖 étale、有限角色单重、
以及 (28) 幂零，都没有在本文中被当成 (29) 的证明。

即使负矩非消失得到支付，R533 双单位域回到原 $S/T$ 中央时的
真实混合条件及补域也仍须保留。本篇不把同一个数的 Cartier 重写赋成新的中央零。

## 8. 精确证书与文献

[脚本](../scripts/check-r549-original-cartier-verschiebung-negative-moments.mjs) 及
[数据](../scripts/check-r549-original-cartier-verschiebung-negative-moments.json)
直接检查 $\zeta_p$ 的全部多项式导数、绝对首项、V-cover 的反向多项式，
两个坐标中的完整有限对角，以及 Wilson 和周期归一中的所有符号。
只用已有的 $p=13,19,61$ 做实现交叉检查，没有扩大素数扫描。
其中 $p=61$ 仍给 $c_{4,61}=47,c_{1,61}=0$，与原笔记完全一致。
全部素数的结论由第 2–7 节的代数证明给出，不由这些有限行外推。

- 原第一层：[固定六度负矩的普通第一层](../notes/2026-11-14-degree6-negative-moment-first-layer.md)。
- 原算术身份：[R540](R540-original-degree-six-schwartz-full-weight-and-negative-two-katz.md)。
- 实际双单位核：[R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)。
- 原 sigma 与 division 函数：[R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
  [R316](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- N. M. Katz, *Nilpotent connections and the monodromy theorem: applications of a
  result of Turrittin*, Publ. Math. IHÉS **39** (1970), 175–232，
  (5.0.4) 的 $p$-curvature 定义、Theorem (5.1) 的零 $p$-curvature Cartier descent；
  [出版全文](https://www.numdam.org/article/PMIHES_1970__39__175_0.pdf)。
  本篇的 (28) 是对实际 $\mathscr U_2,\mathscr U_5$ 的直接计算，
  不调用任何未证的 $p$-curvature 猜想。
