# R855 — 原四首行的全代数热连接与中心零格除 $p$ 行

日期：2026-11-16。**状态：以下 whole theta 格上的热连接、双变量整递推、中心零格的 lift-independent 除 $p$ 行，以及它与 R853 同一个指定首系数的等式均已证明。原横向 Hasse 导数也是 R636 的同一个 $c_p$。尚未证明四条实际除 $p$ 行不能同时为零。**

本篇始终使用原四个 $R_\nu$，没有改变它们的局部来源、Mumford 倍率或 Gaussian 规范。热递推在特征零的两个参数上进行，模 $p^2$ 计算后才可作原 $j=0$ 特化；不能先把 $g_2$ 置零，再把剩余固定矩阵反复乘方。

## 1. 通用曲线与原固定截面格

在
$$
\mathcal A_m=\mathbf Z[1/(6m)][g_2,g_3]
$$
上取
$$
y^2=x^3-\frac{g_2}{4}x-\frac{g_3}{4},\qquad
Dx=2y,\quad Dy=3x^2-\frac{g_2}{4},
\qquad D=\frac{d}{dz}.
\tag{1}
$$
原规范为 $x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、
$\sigma=z+\cdots$、$\zeta=D\log\sigma$，故 $D\zeta=-x$。

以下 $m$ 为固定正偶数。令 $\mathscr V_m$ 是有如下基的自由 $\mathcal A_m$-模：
$$
x^a\quad(0\le a\le m/2),\qquad
yx^a\quad(0\le a\le(m-4)/2).
\tag{2}
$$
它就是 $H^0(E,\mathcal O_E(mO))$ 的原函数格，秩为 $m$。
几何语句限于判别式非零的开集；下文显示的代数算子恒等式在未局部化的参数环上也成立。
对 $R\in\mathscr V_m$，写
$$
A_R(z)=\sigma(z)^mR(x(z),y(z)),\qquad
\varepsilon_m(R)=A_R(0),\qquad
j_{m,k}(R)=D^kA_R(0).
\tag{3}
$$
特别 $\varepsilon_m(x^{m/2})=1$，其余(2)的基元素中心值为零。
本篇所谓中心零格是准确的整核
$$
\mathscr I_m=\ker\varepsilon_m.
\tag{4}
$$
不是仅要求所选整提升的中心值被 $p$ 整除。

原四个来源采用
$$
(m_S,m_T,m_U,m_V)=(34,72,136,66),\qquad
A_\nu=\sigma^{m_\nu}R_\nu
=\Theta^{m_\nu/2}f_\nu(t),
$$
$$
\Theta=x\sigma^2,\qquad t=-x^{-3}.
\tag{5}
$$
$R_\nu=x^{m_\nu/2}f_\nu(t)$ 是
[R821](R821-original-four-central-axes-and-complete-four-block-carries.md)
和 [R853](R853-original-weighted-cartier-return-and-fixed-logarithmic-line.md)
已经固定的完整多项式，极阶为 $m_\nu-6$。因而
$$
R_\nu\in\mathscr I_{m_\nu},\qquad A_\nu=z^6+\cdots.
\tag{6}
$$
固定系数的分母仍按原坏集排除。为在(1)中延拓这些多项式，可把原
$b$ 写成 $-g_3/4$。最终行是 $\mathcal A_m$-线性的，所以不同的代数延拓只要在原特化点相同，给出的实际 jet 相同；这不允许改变原椭圆曲线的整提升。

## 2. 全热方程及其有限代数部分

设
$$
L_2=6g_3\frac{\partial}{\partial g_2}
 +\frac{g_2^2}{3}\frac{\partial}{\partial g_3}.
\tag{7}
$$
这里的参数导数保持 $z$ 固定。Weierstrass sigma 的准确热方程为
$$
L_2\sigma=\left(\frac12D^2+\frac{g_2z^2}{24}\right)\sigma.
\tag{8}
$$
这个规范可直接由 Eilbeck–Gibbons–Ônishi–Yasuda，
*Theory of heat equations for sigma functions*，
Glasgow Math. J. 67 (2025), (6.8) 取得：
其 $\mu_4=-g_2/4,\mu_6=-g_3/4$。
原始来源链接见文末；不是把另一 CM 模型的热算子移到本篇。

对(8)取对数导数，逐式得到
$$
L_2\zeta=-y-\zeta x+\frac{g_2z}{12},
$$
$$
L_2x=2x^2-\frac{g_2}{3}+\zeta Dx,\qquad
L_2y=3xy+\zeta Dy.
\tag{9}
$$
定义真正的代数导子 $\mathcal L$：
$$
\mathcal L|_{\mathcal A_m}=L_2,\qquad
\mathcal Lx=2x^2-\frac{g_2}{3},\qquad
\mathcal Ly=3xy.
\tag{10}
$$
代入(1)可核它保持曲线方程，且
$$
L_2R=\mathcal LR+\zeta DR.
\tag{11}
$$
现在令
$$
\boxed{\mathcal H_mR
=\mathcal LR-\frac{m-1}{2}xR-\frac1{2m}D^2R.}
\tag{12}
$$
由乘积求导，全部 $\zeta DR$ 及 $\zeta^2R$ 逐项相消，得到
$$
\boxed{
L_2A_R-\frac1{2m}D^2A_R-\frac{m g_2z^2}{24}A_R
=\sigma^m\mathcal H_mR.
}
\tag{13}
$$
这保留了热方程的二次势项，而不是仅给协变一阶导数。

### 2.1 确实保持 whole $\mathscr V_m$

若一个基单项在 $O$ 的极阶为 $r$，则(12)中可能把极阶升到
$r+2$ 的系数为
$$
r-\frac{m-1}{2}-\frac{r(r+1)}{2m}
=-\frac{(r-m)(r-m+1)}{2m}.
\tag{14}
$$
它在 $r=m,m-1$ 时准确为零。其余项的极阶至多 $m$，而(10)、
$D$ 及乘 $x$ 不在别处添极。逐基应用(14)给
$$
\mathcal H_m:\mathscr V_m\longrightarrow\mathscr V_m.
\tag{15}
$$
这是带 $L_2$ 系数导数的连接：
$\mathcal H_m(aR)=L_2(a)R+a\mathcal H_mR$。

原四个来源都在偶子模
$\mathscr V_m^+=\mathcal A_m[x]_{\le m/2}$。
在这个子模中，所有矩阵条目还可直接写出：
$$
\begin{aligned}
\mathcal H_m(x^a)
={}&-\frac{(2a-m)(2a-m+1)}{2m}x^{a+1}\\
&+\frac{a(6a-4m-3)}{12m}g_2x^{a-1}
+\frac{a(a-1)}{2m}g_3x^{a-2}.
\end{aligned}
\tag{16}
$$
零系数项不引入负幂。对含参数的线性组合还须加上 $L_2$ 对其系数的作用。
因此原四行可分别在 $18,37,69,34$ 维偶子模中计算；
不能把中间行提前截到 $j=0$ 的某一个固定 $\mu_6$ 型。

## 3. 全部高 jet 的准确双变量递推

对任一 $\mathcal A_m$-线性行 $\ell:\mathscr V_m\to\mathcal A_m$，定义对偶连接
$$
(\nabla_m^\vee\ell)(R)
=L_2(\ell(R))-\ell(\mathcal H_mR).
\tag{17}
$$
(12)的 Leibniz 规则保证(17)仍是 $\mathcal A_m$-线性行。
它不是把输入 $R$ 的参数导数漏掉后的普通矩阵乘法。

在(13)读取 $z=0$ 的第 $k$ 个导数：
$$
\boxed{
j_{m,k+2}
=2m\,\nabla_m^\vee j_{m,k}
-\frac{m^2g_2}{12}\,k(k-1)j_{m,k-2}.
}
\tag{18}
$$
最后一项来自
$D^k(z^2A_R)(0)=k(k-1)D^{k-2}A_R(0)$。
没有先在 $g_2=0$ 丢弃该项。

为只读偶 jet，置
$$
\mathcal T_{m,0}=\varepsilon_m,\qquad \mathcal T_{m,-1}=0,
$$
$$
\boxed{
\mathcal T_{m,r+1}
=\nabla_m^\vee\mathcal T_{m,r}
-\frac{r(2r-1)}{24}g_2\mathcal T_{m,r-1}.
}
\tag{19}
$$
归纳得到特征零恒等式
$$
\boxed{j_{m,2r}=(2m)^r\mathcal T_{m,r}.}
\tag{20}
$$
所有运算都在同一 $\mathcal A_m$ 中；(19)的分母只涉及固定的 $2,3,m$。

一个最早的检查已显示为什么反复横向项不能删除：
$$
\mathcal T_{m,2}
=(\nabla_m^\vee)^2\varepsilon_m-\frac{g_2}{24}\varepsilon_m,
$$
$$
\boxed{
\mathcal T_{m,3}
=(\nabla_m^\vee)^3\varepsilon_m
-\frac{7g_2}{24}\nabla_m^\vee\varepsilon_m
-\frac{g_3}{4}\varepsilon_m.
}
\tag{21}
$$
其中最后一项来自 $L_2g_2=6g_3$，在 $g_2=0$ 后仍存在。
而且 $(\nabla_m^\vee)^3\varepsilon_m$ 自身也须先在双变量环中形成。
(21)不能改成冻结后的矩阵三次幂。

## 4. 实际 Hurwitz 整格与第一个 $p$ 分母

sigma 的原 Hurwitz 展开有整系数，参数换为(1)后至多引入固定
$2,3$ 分母。也可在本格中直接检查封闭性：置
$$
\Theta=x\sigma^2=(D\sigma)^2-\sigma D^2\sigma,\qquad
Y_\sigma=y\sigma^3=\frac{\sigma D\Theta-2(D\sigma)\Theta}{2}.
\tag{22}
$$
于是每个(2)的截面准确等于
$$
\sigma^{m-2a-3\epsilon}\Theta^aY_\sigma^\epsilon,
\qquad \epsilon\in\{0,1\},\quad2a+3\epsilon\le m.
\tag{23}
$$
Hurwitz 级数环对乘法与求导封闭，故全部 $j_{m,k}$ 确属上述整环。
本篇没有先把普通 Taylor 系数全部当整数。
另一个不依赖全 sigma 整性定理的核验直接来自(18)：$j_{m,0}=\varepsilon_m$；
$j_{m,1}$ 在最高奇基 $yx^{(m-4)/2}$ 上为 $-1$，其余基上为零（$m=2$ 时奇基为空）。
这两个初行均整，(17)–(18)只含已倒置的 $2,3,m$，归纳即给所有 $j_{m,k}\in\mathscr V_m^\vee$。

现在固定原特化
$$
g_2=0,\qquad g_3=-4b,\qquad b\in\mathcal O^\times,\qquad
p=6s-1>211,
\tag{24}
$$
并保原固定坏集。所有 $m_\nu<p$。
令
$$
d=p+1,\qquad
c=[z^d]\log(\sigma/z),\qquad
\sigma^\circ=\sigma e^{-cz^d}.
\tag{25}
$$
R614/R636 的原 addition 整窗口使
$\sigma^\circ/z,xz^2,yz^3$ 的本节所需系数全部整；
窗口 $(p^2-1)/6$ 严格大于这里的 $d+m$。
因此对每个整 $R\in\mathscr V_m$，
$$
A_R^\circ=(\sigma^\circ)^mR
$$
在所需的全部非负次数整。完整系数等式是
$$
[z^d]A_R=[z^d]A_R^\circ+mc\,\varepsilon_m(R).
\tag{26}
$$
因为 $A_R=e^{mc z^d}A_R^\circ$，更高指数项不能进入第 $d$ 次。

R636 的原常数为
$$
c_p=\binom{3s-1}{2s-1}b^s\in k^\times.
\tag{27}
$$
由 $D\zeta^\circ=-x-dpc\,z^{p-1}$，以及原式
$DG=-x+c_pZ^{p-1}$ 的同一整窗口，准确有
$$
\boxed{pc\equiv-c_p\pmod p.}
\tag{28}
$$
这里 $d=p+1\equiv1\pmod p$，且 $v_p(c)=-1$。

另一方面
$$
v_p((p+1)!)=1,\qquad\frac{(p+1)!}{p}\equiv-1\pmod p.
\tag{29}
$$
把(26)乘以 $(p+1)!$，由(28)–(29)得到 whole 格上的秩一合同
$$
\boxed{
j_{m,p+1}(R)\equiv m c_p\,\varepsilon_m(R)\pmod p.
}
\tag{30}
$$
这是同一原整提升的合同，不是普通 theta 的 Cartier 规则，也不是把 CM 型当作一维特征来推断。

## 5. 只在准确中心零格上的 canonical 除 $p$ 行

特化(4)后仍记准确整核为 $I_m$。
由(30)，对 $R\in I_m$ 可定义
$$
\boxed{
\mathfrak B_{m,p}(\bar R)
=\frac{j_{m,p+1}(R)}p\bmod p,\qquad
\bar R\in I_m/pI_m.
}
\tag{31}
$$
若 $R'=R+pQ$ 是另一个同在 $I_m$ 的整提升，则
$Q\in I_m$，(30)给 $j_{m,p+1}(Q)\equiv0$。
所以(31)与提升无关，且为 $k$-线性行。

这个范围是必要的。若只要求 $\varepsilon_m(R')\in p\mathcal O$，
取 $R'=R+p x^{m/2}$，则
$$
\frac{j_{m,p+1}(R')-j_{m,p+1}(R)}p
=j_{m,p+1}(x^{m/2})\equiv m c_p\ne0.
\tag{32}
$$
因此不得把(31)扩为“任意中心值模 $p$ 为零的提升均给同一值”。

对 $R\in I_m$，(26)说明原第 $d$ 个 Taylor 系数本身整。
由(29)又有
$$
\boxed{
\overline{[z^{p+1}]A_R}=-\mathfrak B_{m,p}(\bar R).
}
\tag{33}
$$
(19)–(20)给这个指定行的准确有限计算式。令 $N=(p+1)/2=3s$，则
$$
\boxed{
\mathfrak B_{m,p}(\bar R)
=(2m)^N
\frac{\left.\mathcal T_{m,N}(R)\right|_{g_2=0,\ g_3=-4b}}p
\pmod p,\qquad R\in I_m.
}
\tag{34}
$$
除 $p$ 在特化后的整数上进行；它不声称
$\mathcal T_{m,N}/p$ 在整个双变量参数环中整。
要读(34)，必须把(19)保到模 $p^2$，最后才特化并作整除。
只保存模 $p$ 的(30)会把全部 $I_m$ 都送成零，恰好丢失目标行。

## 6. 同一 $c_p$ 是原横向 Frobenius 缺陷

这一节说明双变量项与 R636 的原 Frobenius 常数确实相连。
在特征 $p$ 的通用好曲线上，令
$$
\operatorname{Ha}_p(g_2,g_3)
=[x^{p-1}]
\left(x^3-\frac{g_2}{4}x-\frac{g_3}{4}\right)^{(p-1)/2}.
\tag{35}
$$
由 $\omega=(2y)^{-p}(y^2)^{(p-1)/2}dx$ 及 Cartier 的单项式公式，
$$
\mathcal C(\omega)=\operatorname{Ha}_p^{1/p}\omega,\qquad
D^p=\operatorname{Ha}_pD.
\tag{36}
$$
第一式按相对 Cartier 或在完美常数扩张中解释；第二式是原参数环上的导子恒等式。
第二式也由不变微分与不变向量的 Cartier 对偶式得到：
$\omega(D)=1$，故
$(\mathcal C\omega(D))^p=\omega(D^p)$。

在(24)，(35)的常数 $g_2^0$ 项为零。
其 $g_2^1$ 项只能来自 $2s-1$ 个 $x^3$、一个
$-g_2x/4$、$s-1$ 个 $b$，所以
$$
\left.\frac{\partial\operatorname{Ha}_p}{\partial g_2}\right|_{(24)}
=-\frac14\frac{(3s-1)!}{(2s-1)!(s-1)!}b^{s-1}.
$$
因此
$$
\boxed{
\left.\operatorname{Ha}_p\right|_{(24)}=0,\qquad
\left.L_2\operatorname{Ha}_p\right|_{(24)}
=6s\binom{3s-1}{2s-1}b^s=c_p\ne0.
}
\tag{37}
$$
最后等号在特征 $p$ 中使用 $6s=p+1$。

还有一个全函数域验证。(10)直接给
$$
[\mathcal L,D]=-xD.
$$
在特征 $p$ 中，
$(\operatorname{ad}D)^p=\operatorname{ad}(D^p)$；
逐次作用于 $\mathcal L$ 后，结合(36)得到
$$
\boxed{
D^{p-1}x=\operatorname{Ha}_p x-L_2\operatorname{Ha}_p.
}
\tag{38}
$$
在原 CM 特化点，它准确成为
$D^{p-1}x=-c_p$，与 R636 完整有理模型同号。

所以，原 CM 纤维上的 $D^p=0$ 不能在横向微分时继续当作恒等零：
横向首项是已知非零的同一个 $c_pD$。
本篇没有据(37)的非零替代四个指定的(34)。

## 7. 与 R853 同一个原输入的准确识别

回到 R853 的 $b=1$ 共同模型，保持其全部
$Z,G,\mathcal P_2$ 和原初始资料，令
$$
\eta_{\nu,p}
=Z^{-p-2}\mathcal P_2^{m_\nu/2}R_\nu\,\omega.
$$
R853 的原窗口给
$\alpha_\nu=\overline{[z^{p+1}]A_\nu}$。
由于(6)，首 Gaussian 重标项不进入这个系数，(33)遂准确给
$$
\boxed{\alpha_\nu=-\mathfrak B_{m_\nu,p}(\bar R_\nu).}
\tag{39}
$$
再用 R853(22)，得到不改输入的等式
$$
\boxed{
\mathcal C^4\eta_{\nu,p}
=\mathfrak B_{m_\nu,p}(\bar R_\nu)^{1/p^4}
\,\frac{x^2}{y}\omega.
}
\tag{40}
$$
(40)同时固定了两个构造的全部符号及倍率。

这里热递推处理的是原特征零截面及其模 $p^2$ Hurwitz jet。
它没有在 $g_2$ 方向对 R853 的特征 $p$ 有理模型任意求导。
后者横向变形必须另外保(36)–(38)及全部原 Frobenius 初始资料。
同样，本篇不把固定 torsion 原注的 CM13 算子删成一个裸有理代入：
凡调用该算子，仍须使用该注的完整 $P_{2,M}$ frame 和绝对倍率。

原其它 $b$ 模型按既有齐次运输恢复。若首 $z^6$ 已归一，
$A_{\nu,b}(z)=b^{-1}A_{\nu,1}(b^{1/6}z)$，故该首行乘
$b^{s-1}$；其为当前单位，不产生新的中央零条件。

## 8. 目前实际得到的约束与尚缺的步骤

四个完整中央若同时为零，原 R821 桥迫四个首行零，因而必须满足
$$
\mathfrak B_{34,p}(\bar R_S)
=\mathfrak B_{72,p}(\bar R_T)
=\mathfrak B_{136,p}(\bar R_U)
=\mathfrak B_{66,p}(\bar R_V)=0.
\tag{41}
$$
本篇把(41)固定为四个实际双变量热递推的除 $p$ 行，
并证明它们与 R853 的四个加权 Cartier 输出是同一组指定值。

以下推断并未成立：由 whole 格上(30)的秩一性推断(41)非零；
把 $\mathcal H_m$ 冻结到 $g_2=0$ 后的幂认成(34)；
或仅由原横向单位 $c_p$ 推出一个 $R_\nu$ 不在除 $p$ 行的核中。
真正尚需处理的是四个固定 $R_\nu$ 在完整(34)中的共同相容性，
包括其真实参数导数及模 $p^2$ 的残差。
没有把新的热算子当作第五个算术中央条件，也没有扩大原列格。

本篇没有数学数值运行、目标素数扫描或可重算输出。

### 依赖与原文

- J. C. Eilbeck, J. Gibbons, Y. Ônishi, S. Yasuda,
  [Theory of heat equations for sigma functions](https://doi.org/10.1017/S0017089524000417),
  Glasgow Math. J. 67 (2025), 365–422，(0.5)、(6.8)及(6.9)；
  [作者机构保存的已刊全文](https://pure.hw.ac.uk/ws/portalfiles/portal/154977881/theory-of-heat-equations-for-sigma-functions.pdf)、
  [出版方全文](https://www.cambridge.org/core/journals/glasgow-mathematical-journal/article/theory-of-heat-equations-for-sigma-functions/664736CB03AA93A5D9B981A7D2126A89)。
  本篇使用其 genus-one 正规，并在(9)–(23)自行支付 whole 截面格的乘积与对偶算子。
- [R614 原 addition 整窗口](R614-original-addition-integrality-window-and-complete-newton-tail.md)、
  [R636 原有理模型](R636-original-rational-cartier-return-for-two-critical-rows.md)、
  [R821 四个实际来源及全部 carry](R821-original-four-central-axes-and-complete-four-block-carries.md)、
  [R853 同源加权 Cartier 读数](R853-original-weighted-cartier-return-and-fixed-logarithmic-line.md)。
- [固定 torsion、完整 CM frame 与初始资料](../notes/2026-11-15-fixed-torsion-connection-and-original-frobenius-initial-data.md)。


## 9. 四个实际来源共有的 degree24 因子

本节在原共同 $b=1$ 模型上给出准确乘法身份；回原 $b$ 的运输仍按第7节和 R821 的固定齐次规范进行。置
$$
X=x^3,\quad t=-X^{-1},\quad
\mathfrak a=t(t-1)(7+4t+16t^2),\quad d=1+8t,
$$
$$
\boxed{
A_{24}=\frac{\Theta^{12}\mathfrak a}{7}
=\frac{\sigma^{24}}7(X+1)(7X^2-4X+16).
}
\tag{42}
$$
它是原 whole degree24 截面，$A_{24}=z^6+\cdots$。定义以下四个完整伙伴：
$$
\begin{aligned}
H_{10}&=\Theta^5d,\\
H_{48}&=\Theta^{24}d(1-4t)(1-20t-8t^2)
                         (1+96t+48t^2-64t^3),\\
H_{112}&=\Theta^{56}H_{18}/13,\\
H_{42}&=\Theta^{21}d^2(4t-1)(-1+228t-48t^2+64t^3).
\end{aligned}
\tag{43}
$$
这里 $H_{18}$ 是 [R812(2)](R812-original-same-charge-cancellation-and-complete-source-budget.md) 的完整四因子多项式，常数为13；没有截掉其高次项。直接由 R821(2)–(3)，
$$
\boxed{S=A_{24}H_{10},\quad T=A_{24}H_{48},\quad
U=A_{24}H_{112},\quad V=A_{24}H_{42}.}
\tag{44}
$$
四个伙伴的 degree 分别为下标，其中心值全部为一，且均为 $\mu_6$ 型零。它们确实全纯：把 $\Theta^rQ(t)$ 写成
$\sigma^{2r}x^rQ(-x^{-3})$ 后，(43)中四个 $Q$ 的次数依次为
$1,7,18,6$，故最低 $x$ 次数依次为 $2,3,2,3$，全非负。
相应最高极阶等于其 theta degree，中心值一也可在 $t=0$ 直接读取。
这证明的是同一个原来源的乘法分解，并未给 $A_{24}$ 或任一伙伴增加中央零条件。

### 9.1 共同因子的完整六 sigma 规范

取 $\omega^2+\omega+1=0$、$\gamma=3+\omega$，则
$\gamma\bar\gamma=7$。在本篇原 equianharmonic sigma 规范中，
$$
\boxed{
\frac{\sigma(\gamma z)\sigma(\bar\gamma z)}{\sigma(z)^{14}}
=7x^6-4x^3+16.
}
\tag{45}
$$
为说明这包括绝对倍率，先用 CM sigma 的原准周期式。
$\eta(\gamma\lambda)=\bar\gamma\eta(\lambda)$，所以两分子的指数因子之积恰为分母的指数因子。
$\gamma,\bar\gamma$ 都在模2格上可逆；odd sigma 在三个非零二挠标签上的半特征均为负，两个相同负号相乘为正。因此该商的半特征也平凡。
它是椭圆函数，唯一极点为 $O$、极阶12；又由
$\sigma(\zeta z)=\zeta\sigma(z)$ 对 $\zeta\in\mu_6$ 得其型为零。
故它在 $1,x^3,x^6$ 的三维空间中。

最后使用原 Laurent 规范
$$
\log(\sigma/z)=\frac{z^6}{210}-\frac{z^{12}}{84084}+O(z^{18}),\qquad
x=z^{-2}-\frac{z^4}{7}+\frac{z^{10}}{637}+O(z^{16}),
$$
以及
$$
\gamma^6+\bar\gamma^6=-286,\qquad
\gamma^{12}+\bar\gamma^{12}=-153502.
$$
前三个 Laurent 系数依次确定(45)的 $7,-4,16$。所以没有留下一个未付的单位或 Gaussian 指数因子。

再用准确倍点式 $\sigma(2z)=-2y\sigma^4$ 和 $y^2=X+1$，得到
$$
\boxed{
A_{24}
=\frac{\sigma(\gamma z)\sigma(\bar\gamma z)
        \sigma(2z)^2\sigma(z)^2}{28}.
}
\tag{46}
$$
六条实际输入的范数为 $7,7,4,4,1,1$，和为24；原点首项为
$\gamma\bar\gamma\cdot2^2/28=1$。式(46)保持了每个输入和全部半特征，未以裸范数代来源。

### 9.2 三个伙伴的真实倍点／CM 因子

令 $\delta=1+2\omega$，$\delta^2=-3$。由原倍点和 norm3 公式，
$$
\Theta(2z)=\Theta^4(1+8t),\qquad
\Theta(\delta z)=\Theta^3(1-4t),
$$
$$
\Theta(2\delta z)
=\Theta^{12}(1-4t)(1-228t+48t^2-64t^3).
\tag{47}
$$
例如 $x(\delta z)=-(X+4)/(3x^2)$ 给
$t(\delta z)=-27t/(1-4t)^3$，再把倍点式代入便得第三式，包含全部三次多项式。
因此 R821 的 $V/S=H_{32}$ 及(43)满足
$$
\boxed{
H_{10}=\Theta(z)\Theta(2z),\qquad
H_{32}=\Theta(2z)\Theta(2\delta z),\qquad
H_{42}=H_{10}H_{32}.
}
\tag{48}
$$
另外，原三倍点 division polynomial 给
$$
\Theta(3z)=\Theta^9(1+96t+48t^2-64t^3),
$$
$$
\Psi_{12}(z):=\frac{\sigma(4z)}{2\sigma(2z)}
=\Theta^6(1-20t-8t^2).
\tag{49}
$$
第二个商是完整全纯截面；右式直接支付其潜在分母处的消去和中心值一。
由(47)–(49)，
$$
\boxed{
H_{48}=\Theta(z)^2\Theta(2z)\Theta(\delta z)\Theta(3z)\Psi_{12}(z).
}
\tag{50}
$$
各因子的 degree 为 $4,8,6,18,12$，总和48。
这些身份均在原 CM 纤维上使用完整 theta frame；本节没有把它们当作对任意 $g_2$ 横向变形仍可删去伙伴的乘法规则。

## 10. 四条除 $p$ 行化为同一个真实反对角配对

写 $d=p+1=6s$，对任何实际 whole theta 截面 $A$ 记
$j_k(A)=D^kA(0)$；对中心严格为零者，记
$\mathfrak B(A)=j_d(A)/p\bmod p$，与(31)完全同义。
设 $A(0)=A'(0)=0$，$H(0)=1,H'(0)=0$，各自使用原整提升。
Leibniz 公式准确给
$$
j_d(AH)=j_d(A)+
\sum_{k=2}^{p-1}\binom{p+1}{k}j_k(A)j_{p+1-k}(H).
$$
对于 $2\le k\le p-1$，
$$
\frac1p\binom{p+1}{k}\equiv
\frac{(-1)^k}{k(k-1)}\pmod p.
$$
故
$$
\boxed{
\mathfrak B(AH)=\mathfrak B(A)+
\sum_{k=2}^{p-1}\frac{(-1)^k}{k(k-1)}
             j_k(A)j_{p+1-k}(H).
}
\tag{51}
$$
此式没有对中心值为一的 $H$ 定义一个不合法的 lift-independent 除 $p$ 行；
它仅读 $H$ 的严格低于 $p$ 的整 Hurwitz jet。
若两因子中心值均为零且仍保一阶 jet 零，右边的 $\mathfrak B(A)$ 项也为零，得到相应纯双线性式。

对(42)–(44)，只有 $k=6r$ 项保留。令
$$
\mathcal Q_p(A,H)
=\sum_{r=1}^{s-1}
\frac{j_{6r}(A)j_{6(s-r)}(H)}{6r(6r-1)}\in k.
\tag{52}
$$
四个实际方程准确成为
$$
\boxed{
\begin{pmatrix}
\mathfrak B_{34,p}(R_S)\\
\mathfrak B_{72,p}(R_T)\\
\mathfrak B_{136,p}(R_U)\\
\mathfrak B_{66,p}(R_V)
\end{pmatrix}
=
\mathfrak B_{24,p}(R_{24})\begin{pmatrix}1\\1\\1\\1\end{pmatrix}
+
\begin{pmatrix}
\mathcal Q_p(A_{24},H_{10})\\
\mathcal Q_p(A_{24},H_{48})\\
\mathcal Q_p(A_{24},H_{112})\\
\mathcal Q_p(A_{24},H_{42})
\end{pmatrix},
}
\tag{53}
$$
其中 $R_{24}=(X+1)(7X^2-4X+16)/7$，所有输入仍是原完整截面。
因此四中央同时零所迫的首行条件，等价于(53)第一行零及
$$
\boxed{
\mathcal Q_p(A_{24},H_{48}-H_{10})
=\mathcal Q_p(A_{24},H_{112}-H_{10})
=\mathcal Q_p(A_{24},H_{42}-H_{10})=0.
}
\tag{54}
$$
式(54)是在实际形式级数上取差，未将不同 degree 的差硬放进某一个未付的同线丛格。

这个配对在所有 $s-1$ 个自由低 jet 组成的环境中反对角非退化：
每个显示的 $6r(6r-1)$ 都是单位。但这一环境维数随 $p$ 增长；
非退化本身不证明固定的四个伙伴在其指定行上不能同时相消。

更具体地，令 $a_r=[z^{6r}]A_{24}$、
$h_{q,r}=[z^{6r}]H_q$。所读低系数均整，且
$$
\mathcal Q_p(A_{24},H_q)
=-\sum_{r=1}^{s-1}a_rh_{q,s-r}\pmod p,
$$
$$
\alpha_q=a_s+\sum_{r=1}^{s-1}a_rh_{q,s-r}
=-\mathfrak B(A_{24}H_q).
\tag{55}
$$
这由
$\binom{p+1}{k}k!(p+1-k)!/p=(p+1)!/p\equiv-1$
直接得到。于是(53)保留的正是原全部低卷积；
未把它误判成已经消去全部卷积的一个新相位等式。

## 11. 热张量乘法中必须保留的伙伴方向

对通用参数上的 $R\in\mathscr V_m,S\in\mathscr V_n$，从(12)逐项相减得
$$
\boxed{
\mathcal H_{m+n}(RS)
=(\mathcal H_mR)S+R(\mathcal H_nS)+\mathcal K_{m,n}(R,S),
}
$$
$$
\mathcal K_{m,n}(R,S)
=\frac{n(D^2R)S}{2m(m+n)}
+\frac{mR(D^2S)}{2n(m+n)}
-\frac{(DR)(DS)}{m+n}-\frac{xRS}{2}.
\tag{56}
$$
这个额外项也有完全不含 $\zeta$ 的实际双输入表示：
$$
\boxed{
\sigma^{m+n}\mathcal K_{m,n}(R,S)
=
\left.
\frac{(nD_1-mD_2)^2
\big(A_R(z_1)A_S(z_2)\big)}
{2mn(m+n)}
\right|_{z_1=z_2=z}.
}
\tag{57}
$$
证明把 $D A_R=\sigma^m(DR+m\zeta R)$ 和其二阶式代入。
所有 $\zeta DR,\zeta DS,\zeta^2RS$ 项准确相消，
剩余 $\zeta'RS/2=-xRS/2$，恰为(56)的最后一项。
所以(57)是同一线束乘法的完整第二伙伴方向；它不是零，也不是可以删除的中心单位。

对(44)可取 $m=24$、$n=10,48,112,42$。
若要反复使用热连接，(56)–(57)及后续所有横向导数须一起保留；
仅把 $\mathcal H_{m+n}$ 当作两因子热算子的和会改变(34)。
在 $j=0$ 上，两个型零因子的(57)为型四，这也不能使其在后继双变量递推中消失。

本附录新增的是原共同六 sigma 来源、四个完整真实伙伴、
以及它们在原除 $p$ 行中的准确共同配对和热张量项。
它没有证明(54)不相容，也没有将任一伙伴或平衡导数赋予新的算术中央零。
所有原 $P_{2,M}$ Frobenius 初始资料、CM13 frame、Gaussian 权和高 carry 范围仍原样保留。
