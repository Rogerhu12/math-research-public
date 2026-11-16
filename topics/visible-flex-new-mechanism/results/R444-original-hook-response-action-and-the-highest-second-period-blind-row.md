# R444：原 hook 响应的最高规范作用与当前十二副本的第二周期盲行

日期：2026-11-16。**完整原式纸面证明；没有执行新的符号、积分、profile、秩、零点、开发检查或科学计算。**

本文直接消费原八个 $\mathcal B_X\mathfrak H$ 响应、同一个实际圆及 [R437](R437-highest-rational-gauge-row-vanishes-on-the-complete-period-kernel.md) 的最高有理规范行。新增结论有两部分：

1. 八个原响应对两个真实 period 像泛函的作用准确由八对四次积分给出。它们保持 whole $E$、全部自然查询、全部内部通量及 ordered 通道；不需要把任一单包二次输出假成紧函数。
2. 对 [R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md) 当前真实八/十二复制母库，第二组八个积分全部准确为零。这也使 R437 的第二个 incoming 修正项为零。第一组保留八个真实值，给出该支路内的完整条件性可调判据。

这里的盲行只针对这八个原响应，不是整个 $\mathcal R$ 的障碍。没有证明第一组非零，没有重新计算任何响应秩，也没有把 signed 响应差当成零基准实际路径。原全部 period range、其余十二行及同一个规范仍完整保留。

## 1. 固定实际输入与两种不同的泛函

固定已经安装的实际几何、原右锚 $r_*$、同一个实紧圆
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
$$
记
$$
\Delta=f\odot f-g\odot g,\qquad
D_\theta=\sin^2\theta\,\Delta
-2\sin\theta\cos\theta(f\odot g).
\tag{1}
$$
所有二次槽都按原对称双线性规范极化；$X(f,g)$ 不额外乘 $2$。

原二阶三矩满足
$$
\mathbf I(f,f)=\mathbf I(g,g),\qquad
\mathbf I(f,g)=0,
\tag{2}
$$
其中
$$
I_0(a,b)=\int a''b'',\quad
I_1(a,b)=\int xa''b'',\quad
I_2(a,b)=\int(x^2a''b''+2a'b').
$$
原第三 hook 为
$$
\mathfrak H=C(P,S)-3C(P,R),\qquad
L_f(k)=\mathfrak H(k;f,f).
\tag{3}
$$
当前逐包比例圆已有 $L_f(g)=0$，而 $\Delta\mathfrak H=0$ 给 $L_f(f)=0$。因此
$$
L_f(\phi_\theta)=0.
\tag{4}
$$
下面第2—4节只需要(2)、(4)，不先要求采用十二副本。

令整个几何的原第三成本为 $T=\tau\mathfrak H$，$\tau\ne0$。这是与端芽参数 $\kappa$ 不同的原常量，不能互换。依 R437 记
$$
Y=\Phi_{p_2},\qquad
\ell_f(k)=I_2\{Y(f,f),k\}.
$$
真实 period 像泛函是
$$
\mathfrak p_f:\operatorname{Im}(L_f|_{C_c^\infty(I)})\longrightarrow\mathbb R,
\qquad
\mathfrak p_f(L_fk)=\ell_f(k).
\tag{5}
$$
它因 $\ell_f|_{\ker L_f}=0$ 而良定义。本文不将其延拓到尚未证明属于像的一般目标。

真正的最高有理规范行另为
$$
\boxed{P_{2,\theta}(k)=\frac{\kappa}{24}\ell_f(k).}
\tag{6}
$$
下文出现的 $1/\tau$ 是 period 特解或 $\mathfrak p_f$ 的变化；要成为(6)的行值还必须乘 $\kappa/24$。

## 2. 从完整原响应得到真像方向

采用 [R255 §4](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md) 的完整原式。对任意 $X\in E_8$，
$$
\begin{aligned}
\mathcal B_X\mathfrak H(f^2,\phi)
={}&2\mathfrak H(XD;D)
-4\mathfrak H(\phi;\phi,XD)
+4X\{\phi,\mathfrak H(\phi;D)\},\\
&D=f^2-\phi^2 .
\end{aligned}
\tag{7}
$$
原积分、三个槽及真实左尾均包含在(7)中。

由完整对角零身份极化，
$$
\mathfrak H(k;\phi,\phi)+2\mathfrak H(\phi;\phi,k)=0.
\tag{8}
$$
在当前圆上，(2)和 [R259 §5](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md) 的全部八个左二次尾给
$$
X\Delta,\quad X(f,g),\quad XD_\theta\in C_c^\infty(I).
\tag{9}
$$
这是整个输入的三矩闭合；不是单个微包的三矩为零。

对(7)的 $k=XD$ 使用(8)，准确得到
$$
\mathcal B_X\mathfrak H(f^2,\phi)
=2L_f(XD)+4X\{\phi,L_f(\phi)\}.
\tag{10}
$$
因此由(4)，
$$
\boxed{\mathcal B_X\mathfrak H(f^2,\phi_\theta)
=2L_f(XD_\theta).}
\tag{11}
$$
没有丢掉(7)的第三 history 项：它先按原式成为(10)的第二项，再由已经支付的第三条件为零。

特别，八个方向属于原 $\mathcal R_{71}\subset\mathcal R$，没有新造形式算子。不同标签是否产生独立成本不在此处假设。

## 3. Whole E、自然查询与全部内部通量保持

令 $p=u'$、$r=u''$、$t=u'''$，$A_u=6pt-2r^2$。原 $\mathfrak H$ 的完整局部自伴系数为
$$
D^3L_u=D^2(A_uD^2)+D(b_uD),\qquad
b_u=-6(rt)',\qquad c_u=0,
\tag{12}
$$
并保原右三个零常数。由 [R432 §4—5](R432-complete-zero-order-kernel-and-all-degenerate-point-response-matrices.md)，每个 $\mathcal B_X\mathfrak H$ 都满足
$$
\pi(\mathcal B_X\mathfrak H)=0,\qquad
\mathcal Q_{\rm all}(\mathcal B_X\mathfrak H)=0,\qquad
\Lambda_{\rm all}(\mathcal B_X\mathfrak H)=0.
\tag{13}
$$
其中 whole self 的原公式为
$$
\mathfrak q_u(\mathcal B_X\mathfrak H)
=-\frac14\int c_u\,X(u,u)=0.
$$
自然总量也可直接由
$$
2\int u'''L_u(X(u,u))
=-2\int u\,\mathscr A_uX(u,u)
=-2\int(\mathscr A_uu)X(u,u)=0
$$
得到。紧 outer 和紧系数支付边界，不把 $X(u,u)$ 的真实左二次尾删掉。因此(13)同时杀当前有限自然查询以及 [R433](R433-actual-universal-ordered-flux-zero-and-explicit-local-cap-currents.md) 新增的全部 ordered 查询：
$$
\boxed{\mathcal B(E_8,\mathfrak H)\subset\mathcal R\cap\ker J^+.}
\tag{14}
$$

原累计通量同样是完整身份。对任意光滑 $w$，即使它在单包左侧有真实二次尾，
$$
\int_{\ell_u}^{x}u'(L_uw)''
=A_u(x)\{u'(x)w''(x)-u''(x)w'(x)\}.
\tag{15}
$$
原左平端支付积分常数；(12)中的 $(A_ur)'+b_up=0$ 直接验证(15)。

故(11)在所有实际 $A_f=0$ 内部点上的两个 period partial 均为零，全部 $C_i=R_iH_{e,i}+T_iH_{d,i}$ 也为零。这里保留右方各包的真实 $X$ 尾，没有冻结 suffix。全部平台、平端、累计及连接的原 range 兼容也保持：变化本身就是同一个紧 $L_f$ 的真实像。这个陈述不将尚未在像内的初始目标变成在像内。

## 4. 两个 period 特解与最高行的准确变化

按 R326/R437 的规范，
$$
V_\theta=\sin^2\theta\,V_d+
2\sin\theta\cos\theta\,V_e,\qquad
G_d=-\frac{V_d^c}{2\tau},\quad G_e=-\frac{V_e^c}{2\tau}.
$$
先固定原 incoming 矩阵和已经施加的同一个端口清理规范。在成本上增加一个 signed 响应 $\eta\,\mathcal B_X\mathfrak H$，(1)、(11)给
$$
\delta V_d=2\eta L_f(X\Delta),\qquad
\delta V_e=-2\eta L_f(X(f,g)).
\tag{16}
$$
于是
$$
\delta G_d=-\frac{\eta}{\tau}L_f(X\Delta),\qquad
\delta G_e=\frac{\eta}{\tau}L_f(X(f,g)).
\tag{17}
$$

若原两个完整紧特解确实存在，则可取
$$
\delta k_d=-\frac{\eta}{\tau}X\Delta,\qquad
\delta k_e=\frac{\eta}{\tau}X(f,g).
\tag{18}
$$
这些是允许的紧函数；其它特解与它们相差的全核不改变 $\ell_f$。定义八个方向上的真实线性函数
$$
d_f(X)=I_2\{Y(f,f),X\Delta\},\qquad
e_f(X)=I_2\{Y(f,f),X(f,g)\}.
\tag{19}
$$
则
$$
\boxed{
\delta\mathfrak p_f(G_d)=-\frac{\eta}{\tau}d_f(X),\qquad
\delta\mathfrak p_f(G_e)=\frac{\eta}{\tau}e_f(X).
}
\tag{20}
$$
真正(6)的两个幅系数变化是上述各式再乘 $\kappa/24$；完整相位行的变化为
$$
\delta P_{2,\theta}(k_\theta)
=\frac{\kappa\eta}{24\tau}
\{-\sin^2\theta\,d_f(X)
+2\sin\theta\cos\theta\,e_f(X)\}.
\tag{21}
$$
式(19)—(21)保全部 inner history、原 $I_2$ 的一阶导项和真实相位因子。

## 5. 当前库的三矩闭合是逐完整 base 的真实条件

下面使用 R431 的具体包装范围。

[R277 §6(22)—(25)](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md) 的格点 base 满足
$$
\sum_i R_i t_i^m=\sum_i T_i t_i^m=0
\quad(0\le m\le10),\qquad T_i=a_ib_i.
$$
每个实际微包三矩的平移公式次数至多二，因此逐完整 base 给
$$
\mathbf I(F,F)=\mathbf I(G,G),\qquad \mathbf I(F,G)=0.
\tag{22}
$$
R280 的两种真实布局仍保这两组格点矩，再先作完整八/十二包装，最后才作五个已定位整块的正幅混合。不是把某个未闭合 micro 当作 base。

R324 §8—9 和 R431 §1、§4、§7 的后续构造都从起点保母包三矩，且每一基本位置的全部实际副本同步改变。宽度、八/十二真实平移、最终块位置及幅权在同一次构造中冻结。因此(22)对现在的每个完整 base 仍准确成立；本稿不从另一母库借用它。

由 R259 的原尾表，对任何 $X\in E_8$，(22)使
$$
X(F,G)\ \text{在这个完整 base 的两外 collar 为零}.
\tag{23}
$$
其包内原 primitive 仍全部保留。共同正缩放、整个 $G$ 翻号、八副本的真实幅度与后置完整块的幅度都不改变(22)—(23)。

## 6. 先消真实跨副本尾，再使用四次差分

### 6.1 跨副本项准确为零

若 $q\in C_c^\infty$、$p_2(x)=Ax^2+Bx+C$，则
$$
\begin{aligned}
I_2(p_2,q)
&=2A\int x^2q''+
2\int(2Ax+B)q'\\
&=4A\int q-4A\int q=0.
\end{aligned}
\tag{24}
$$
此处两个贡献都必要。不能只因 $p_2'''=0$ 就删掉 $I_2$ 的一阶导项。

不交完整 base 之间，原 $Y(F,F)$ 在右侧真零、左侧为原二次多项式；另一项 $X(F,G)$ 由(23)真紧。因此(24)杀所有跨 base 项。内层二次算子的交叉输入又因 profiles 本身及所有 collar 不交而为零。于是，对任意有限个完整 base，
$$
e_f(X)=\sum_b e_{F_b}(X),
\tag{25}
$$
各项另乘其真实四次幅度与 $G$ 的符号。这里没有把 $Y(F_b,F_b)$ 的左尾置零。

### 6.2 同副本的平移次数

保持完整固定 base，定义
$$
\mathscr E_X(t)
=I_2\{Y(T_tF,T_tF),X(T_tF,T_tG)\},
\qquad T_tF(x)=F(x-t).
\tag{26}
$$
原八个二次式的真实平移次数上界为
$$
\begin{array}{c|rrrrrrrr}
X&P&R&S&L&U&V&T&Y\\ \hline
\deg_t&0&1&1&2&2&3&3&4.
\end{array}
\tag{27}
$$
这是 R255(4)、R259 原式中 local 项及 $J_0,J_1,J_2$ 一起换元的界。例如 $Y$ 的 $x^2J(x^2F''^2+2F'^2)$ 计至四次；$V=\Phi_{p_1}$ 计至三次，不能与 $Y=\Phi_{p_2}$ 混名。

由(23)，(26)可在平移后的完整 base 上积分。换元回固定 base，右锚仍在其右零 collar；真实 $J$ 不产生未记录的锚常数。两次 $x$ 求导不增加平移次数，$I_2$ 的外权至多二，所以
$$
\deg_t\mathscr E_X\le 4+\deg_tX+2\le10.
\tag{28}
$$
固定任何真实正宽后仍为此次数界；没有取零宽极限。

### 6.3 使用原十二副本的四次幅权

R259 §9(29)—(30)的实际定义是
$$
t_j=t_0+j\Delta_c,\quad 0\le j\le11,\qquad
\epsilon_j=(-1)^j,\qquad
\gamma_j=\binom{11}{j}^{1/4}>0,
\tag{29}
$$
第 $j$ 个完整副本是
$$
(\gamma_jT_{t_j}F,\ \epsilon_j\gamma_jT_{t_j}G).
$$
$Y(F,F)$ 二次、$X(F,G)$ 二次且对 $G$ 为奇，故此处的真实权是
$$
\epsilon_j\gamma_j^4=(-1)^j\binom{11}{j}.
\tag{30}
$$
它是当前 $F^3G$ 四次配对的权，不是自然五次查询的 $\gamma_j^5$。

将(25)、(28)—(30)合并，第十一有限差分准确给
$$
\boxed{
I_2\{Y(f,f),X(f,g)\}=0
\quad\text{对全部 }X\in E_8 .
}
\tag{31}
$$
后续五个完整 block 的正幅混合继续由(24)—(25)相加；每个 block 的(31)已经为零。因此结论适用于 R431 最终实际母库及 R433 使用的同一圆，不要求再次改变 shape 或插入新的纤维观察。

## 7. Incoming-e 项消失与八列支路的严格 iff

### 7.1 同一个真实 incoming 矩阵

R437(34)—(35)保留实际 incoming $X_*=\Phi_{\mathsf m_*}$：
$$
G_d^c=G_d^0+L_f(X_*\Delta),\qquad
G_e^c=G_e^0-L_f(X_*(f,g)).
$$
在目标确在原像内时，(31)给
$$
\boxed{\mathfrak p_f(G_e^c)=\mathfrak p_f(G_e^0),}
\qquad
\mathfrak p_f(G_d^c)=\mathfrak p_f(G_d^0)+d_f(X_*).
\tag{32}
$$
因此当前包装准确支付 R437 未判定的第二个 incoming 四次项。第一项仍保留。$X_*$ 来自同一真实路径，不因此成为新的自由八参数。

### 7.2 只在原八响应支路内的最高行判据

先有两个真实紧 period 特解，记
$$
b_d=\mathfrak p_f(G_d^c),\qquad
b_e=\mathfrak p_f(G_e^c).
$$
在 signed 空间 $\mathcal B(E_8,\mathfrak H)$ 内增加一个完整响应 $\mathcal B_Z\mathfrak H$，(20)、(31)给
$$
(b_d,b_e)\longmapsto
(b_d-\tau^{-1}d_f(Z),\,b_e).
\tag{33}
$$
所以这个支路内同时使最高规范的两个系数为零，**当且仅当**
$$
\boxed{b_e=0,\qquad \tau b_d\in d_f(E_8).}
\tag{34}
$$
这是准确线性像判据：

- 若八个真实数 $d_f(P),d_f(R),d_f(S),d_f(L),d_f(U),d_f(V),d_f(T),d_f(Y)$ 全零，(34)要求 $b_d=b_e=0$；
- 若至少一个真值非零，则该支路可在 signed 层改任意 $b_d$，但仍必须先有 $b_e=0$。

本文没有评价这些八个数，也没有宣称第二种情形发生。八列最高行矩阵的秩至多一；不是断言恰一。若原响应之间存在关系，(33)仍一致，因为零成本的 $L_f(Z\Delta)=0$ 使 $d_f(Z)=0$。

改变 incoming 的真实量 $\delta X_*$ 若另外已经确定，只在(33)的第一坐标增加 $d_f(\delta X_*)$；第二坐标仍不变。此说法不授任意 $\delta X_*$ 的实际选择。

## 8. 同一规范、全部基准与 actual 实现的边界

本稿(18)是两个 period 特解的真实紧改变。它们在完整相位中组成
$$
\delta k_\theta=-\frac1\tau ZD_\theta.
\tag{35}
$$
所以仍使用同一个二阶规范族、同一个 seed 和原双零相位。还可准确保留已付的三个合法性矩：R326 §2(6)在同一个八复制最终库上给
$$
I_j\{a,X(b,c)\}=0\quad(j=0,1,2),\qquad a,b,c\in\operatorname{span}\{f,g\},
$$
其每基本位置的副本在 R431 中仍同步，故 $\mathbf I(\phi_\theta,\delta k_\theta)=0$。这不是另加三条控制假设。

(35)不自动满足十个端口系数中除 $P_2$ 外的九行；它们和同一个核修正仍须按原 R327 联合方程检验。若还要保持其它 s 段 ruling，也仍须保其完整变化。

此外，$\mathcal B_Z\mathfrak H\in\ker J^+$ 是 signed 成本的身份，不是某一实际完整 word 的成本为这一列。[R101](R101-finite-replication-and-signed-fourth-character-costs.md) 与 R392 的真实 prototype、回桥、整数复制和后置校正仍携带完整基准。若实际构造的成本写成
$$
V_{\rm base}(t,n)+\mathcal B_{Z(t,n)}\mathfrak H,
\tag{36}
$$
则 $V_{\rm base}$ 的 whole $E/J^+$、两 period 目标、全部内部 partial、$C$、incoming 及最高行贡献必须同时记录。尤其复制次数为 $n$ 的 prototype 自成本可含 $n$ 倍基准，不能归入与 $n$ 无关的误差。

只有在完整实际基准也已经满足相应条件，或同一个有限增强构造真正校正它以后，才可消费(34)作 actual 联合支付。本文没有提供这一新增实际截面，更没有以“响应在 $\ker J^+$”宣布(36)的基准也在核中。

## 9. 准确新增范围

本稿给出原 $\mathfrak H$ 支路在最高有理兼容门上的完整作用，且从当前实际幅权、全部三矩和真实二次尾证明第二个作用恒零。它还有一个不依赖响应实现的直接后果：当前圆上最高规范的第二个 incoming 四次项确实为零。

下一未付问题仍是原实际 $b_e$ 的值及其在这八列以外响应或完整路径成本上的变化、第一组八个真实值、全 period range、其他十二行，以及这些要求与 whole $J^+$、全部 $C$ 和原型基准的同一个实际有限构造。不能把(31)或(34)扩成整个 $\mathcal R$ 的不变性，也不能由最高行可调单独宣称完整第四 range 或主课题完成。
