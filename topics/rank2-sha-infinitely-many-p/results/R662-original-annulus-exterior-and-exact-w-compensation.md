# R662 — 原 Y 环带外部质量、Q/p 尺度与完整 W 补偿的准确抵消

日期：2026-11-15。**状态：已证明。**

本篇把 R659 的非零补偿差放回原 $S/T$ 中央关系。
所得结论是：若原两个中央导数同时为零，R659 的非齐次项
并不被迫消失。它由一个明确的原 Y 环带外部质量精确补偿。
该外部质量在 R659 的无限子族上本身是单位；
所以不能再把它作为零质量误删。

全文使用原 R594 的同一个 $q_N$，保原 $Q/p^m$ 归一，
并给有限层的准确 W 词关系和完整误差界。
原 T 行也在同一真实交域上下降为两个固定的混合单位观察；
全部五项 S5 来源保持，尚未将这两个行化成裸负一矩。

## 1. 同一来源和两个准确的全算术行

沿用 R645、R650、R653、R659。记
$$
Q=Q_5=c+2d,\qquad L=L_5=2c-d,\qquad Y=A+Q,
$$
$$
W=A+b_QQ+b_LL,\qquad
b_Q=(11+6\omega)/5,\quad b_L=(2+12\omega)/5,\quad
b_Y=(20+3\omega)/17 .
\tag{1}
$$
全部其余三个 A 伴随和 C 纤维均保留。
取原固定 carry 深度 $N\in4\mathbf Z_{\ge1}$，
以及 R659 的相对密度一普通子族。于是原 $M_{0,N}$ 为单位。
令
$$
\chi=\chi_{65}=-1,\qquad a_5=\chi\lambda=\beta=-\lambda,\qquad
\ell_\lambda=\log\langle\lambda^2\rangle\ne0,\qquad d_p=p-1.
\tag{2}
$$
$\chi$ 的准确值及原 $\sigma^5$ 负一非零来自 R655；
本篇不更换该来源或尺度。

原正分支 $q_N$ 是 R645(6) 的
$$
q_N=\frac{1_{\{C\ {\rm unit},\,F-C\in p^N\}}}{b\Omega^6}
 \widehat P_p((F-C)/\kappa^N,F+13C,G).
\tag{3}
$$
它的完整 $\pi_4$ 中性是
$(\pi_4)_*(q_N\mu_0)=\beta^N(\pi_4)_*\mu_0$；
而 $C,F,G$ 与 Y 正交。原全 Y 核和 A 两层核是
$$
\mu_0|_{Y\in p^k}=\lambda^k(P_{Y,(-\kappa)^k})_*\mu_0,\qquad
\mu_0|_{A\in p^{2r}}=\lambda^{2r}(P_{A,\kappa^{2r}})_*\mu_0 .
\tag{4}
$$
Q 的整个核心是 $a_5$，与 A 正交。

固定 $m\ge0$，令 $r$ 为趋向无穷的偶整数，且
$r>\max(m,N)$。考虑原完整 Y 环带行
$$
\mathcal F_{r,m}(u)=
\int_{Y\in p^{r+m}\mathbf Z_p^\times}
 q_N\left\langle\frac{Y}{\kappa^r p^m}\right\rangle^{d_pu}
 \,d\mu_0 .
\tag{5}
$$
由 (3)、(4) 的完整来源身份，
$$
\boxed{\mathcal F_{r,m}(u)
=\lambda^{r+m}\beta^N
 \langle\lambda^2\rangle^{m d_pu}J_S(u).}
\tag{6}
$$
原 $(-1)^{r+m}$ 是根单位，不影响 principal Mellin；
而 $\kappa^m/p^m=\lambda^{2m}$ 必须保留。
因 $J_S(0)=0$，(6) 的质量恒为零。
若再假设 $J'_S(0)=0$，其中央导数也为零；
不是把 (6) 的整个 Mellin 函数赋为零。

把 (5) 按真正的 A 深域分开：
$$
\mathcal F_{r,m}=\mathcal I_{r,m}+\mathcal O_{r,m},
$$
$$
\mathcal I_{r,m}:\ A\in p^{2r},\qquad
\mathcal O_{r,m}:\ A\notin p^{2r}.
\tag{7}
$$
两项都保原 $q_N$、Y 环带和 (5) 的同一个归一。
尤其 $\mathcal O_{r,m}$ 是原全算术行中的实际外部域。

## 2. 原交域的完整返回，及真实冻结门

令
$$
B_r=P_{A,\kappa^{2r}}P_{Q,\kappa^r},\qquad
g_r=\lambda^{2r}a_5^r=\chi^r\lambda^{3r}.
$$
因为 $2r>r+m$，
$$
\{A\in p^{2r},Y\in p^{r+m}\mathbf Z_p^\times\}
=\{A\in p^{2r},Q\in p^{r+m}\mathbf Z_p^\times\}.
$$
A、Q 的完整限制交换，因而准确有
$$
\boxed{
\mathcal I_{r,m}(u)=g_r
 \int_{Q\in p^m\mathbf Z_p^\times}
 q_r\left\langle\frac{Q+\kappa^r A}{p^m}\right\rangle^{d_pu}
 \,d\mu_0,\qquad q_r=q_N\circ B_r.}
\tag{8}
$$
这里没有把 A 深认成四个原 sigma 各深。

保持 R653 的
$$
a=-(5+6\omega)/29,\qquad b_F=(5+6\omega)/5,\qquad g=3-2\omega,
$$
$$
F_0=F-aA-b_FQ,\quad D_0=F_0-C,\quad E_0=F_0+13C,\quad
G_0=G-gaA-gb_FQ .
$$
设
$$
\Delta_r=a\kappa^{2r}A+b_F\kappa^rQ .
$$
则整个实际权是
$$
\boxed{
q_r=1_{\mathcal G_{0,N}}p_r,\qquad
p_r=\frac{\widehat P_p((D_0+\Delta_r)/\kappa^N,
                       E_0+\Delta_r,G_0+g\Delta_r)}
                  {b\Omega^6},
}
\tag{9}
$$
$$
\mathcal G_{0,N}=\{C\ {\rm unit},D_0\in p^N\}.
$$
(9) 的门是准确相等，而不只是渐近相等：$r\ge N$ 使
$\Delta_r\in p^N$，且原 C 单位保持。
它仍带原全部 $\lambda,\kappa$ 整右逆。

在 $Q\in p^m\mathbf Z_p^\times$ 上，$r>m$ 给
$$
p_r-p_{0,N}\in p^{r+m-N}\mathcal O,\qquad
\log\left\langle\frac{Q+\kappa^rA}{p^m}\right\rangle
-\log\left\langle\frac Q{p^m}\right\rangle
\in p^{r-m}\mathcal O .
\tag{10}
$$
两个单位 cut 准确相同。后一界来自真实比值
$1+\kappa^rA/Q$，没有少保逆 $Q$ 的 $m$ 层。
前一界来自原 degree 六整多项式；因 $p\ge71$，所用阶乘是单位。

## 3. 外部零阶质量及尺度导数的完整极限

定义同一个真实有限层外部行
$$
O^{[0]}_{r,m}=g_r^{-1}\mathcal O_{r,m}(0),\qquad
O^{[1]}_{r,m}=(d_pg_r)^{-1}\mathcal O'_{r,m}(0).
\tag{11}
$$
以下导数式假设 $J'_S(0)=0$；
质量式只用原 $J_S(0)=0$。R653 的全 S5 分离给
$$
\int_{\mathcal G_{0,N},\,Q\in p^m\mathbf Z_p^\times}
 p_{0,N}\,d\mu_0=-M_{0,N}a_5^m(1-a_5),
$$
$$
\mathcal K_{N,m}
=-M_{0,N}a_5^m
 \{\ell_D+m\ell_\lambda(1-a_5)\},
\tag{12}
$$
其中 $\ell_D=\int_{Q\ {\rm unit}}\log\langle Q\rangle\,d\nu_{D_5}$
是原 R653 的固定 principal log 行。

(6)–(12) 给准确的有限层估计
$$
\boxed{
O^{[0]}_{r,m}
=M_{0,N}a_5^m(1-a_5)+p^{r+m-N}\mathcal O,
}
$$
$$
\boxed{
O^{[1]}_{r,m}
=M_{0,N}a_5^m
 \{\ell_D+m\ell_\lambda(1-a_5)\}
+p^{\min(r-m,\ r+m-N+1)}\mathcal O .
}
\tag{13}
$$
第二个误差中的 $+1$ 只属于
$(p_r-p_{0,N})\log\langle Q/p^m\rangle$；
真正的观察 log 变化只有 $p^{r-m}$，没有提高它的赋值。

在 R659 的子族上，$M_{0,N}$ 与 $1-a_5=1+\lambda$ 均为单位。
故每个有限偶 $r>\max(m,N)$ 的
$\mathcal O_{r,m}(0)$ 已是单位，不只是极限非零。

令 $r$ 沿偶数趋向无穷，得到真正外部积分的极限
$O_m^{[j]}=\lim_r O_{r,m}^{[j]}$。完整输运矩阵为
$$
\boxed{
a_5^{-m}
\begin{pmatrix}O_m^{[0]}\\O_m^{[1]}\end{pmatrix}
=
\begin{pmatrix}1&0\\m\ell_\lambda&1\end{pmatrix}
\begin{pmatrix}M_{0,N}(1-a_5)\\M_{0,N}\ell_D\end{pmatrix}.
}
\tag{14}
$$
因此
$$
\boxed{a_5^{-m}O_m^{[1]}-O_0^{[1]}
=m\ell_\lambda O_0^{[0]}\ne0\qquad(m\ge1).}
\tag{15}
$$
这就是原算术零留下的明确外部系数。
它是非零的零阶质量，不能因为整个原 S 的单位质量为零而删除。

更具体地，有限层的 (15) 误差在
$p^{e_{r,m}}\mathcal O$，其中
$$
e_{r,m}=\min(r-m,r-N+1).
$$
若
$$
r>v_p(m\ell_\lambda)+\max(m,N-1),
\tag{16}
$$
则真实有限层差
$a_5^{-m}O^{[1]}_{r,m}-O^{[1]}_{r,0}$
的赋值恰为 $v_p(m\ell_\lambda)$。
这里 $r$ 可以依原 $p,m$ 选取；没有把这个深度当成新的固定 ray 条件。

若改按 $Y/\kappa^{r+m}$ 归一，(14) 的第二行须同时减去
$m\ell_\lambda O_m^{[0]}$；三角项才消失。
共同部分与外部部分都按这个规则改变。
不能只在一侧改归一后以 (15) 推出矛盾。

## 4. 同一有限层测试的完整 W 词关系

对原 $\mu_0$ 上任意连续测试 $f$，whole W 两层核心给
$$
\mathscr W(f)=
 \int_{W\notin p^2}f\,d\mu_0
 +\lambda^2\int(f\circ P_{W,\kappa^2}-f)\,d\mu_0
=(1-\lambda^2)\int f\,d\mu_0 .
\tag{17}
$$
所有共同门、进入门、离开门和门外负测试都在此式内。

取 (8) 的实际 log 测试
$$
f_{r,m}=1_{\{Q\in p^m\mathbf Z_p^\times\}}q_r
 \log\left\langle\frac{Q+\kappa^rA}{p^m}\right\rangle .
\tag{18}
$$
于是，仍在原 $J'_S=0$ 假设下，有限层就有准确等式
$$
\boxed{\mathscr W(f_{r,m})+
                 (1-\lambda^2)O^{[1]}_{r,m}=0.}
\tag{19}
$$
这里是先作共同域返回 $B_r$，再作真实 W 核；
原权的顺序是 $q_N\circ B_r\circ P_{W,\kappa^2}$。
没有交换两个非正交物理变换。

实际 W 转置明确是
$$
\begin{aligned}
D_0&\longmapsto D_0-(\kappa^2-1)(6+\omega)W/60,\\
Q&\longmapsto Q+(\kappa^2-1)(5-6\omega)W/72,\\
A&\longmapsto A+(\kappa^2-1)29W/72,\qquad C\longmapsto C .
\end{aligned}
\tag{20}
$$
原 $\mathcal G_{0,N}$、Q 环带、(9) 的全部多项式和
(18) 的 log 按 (20) 同时移动。
$r\ge N$ 的稳定门恒等仍对每个变换后的整输入成立，
但它不把 Q 环带或 W 失败支删掉。

由 (10)，$f_{r,m}$ 一致趋向 R659 的
$$
f_m=1_{\mathcal G_{0,N},\,Q\in p^m\mathbf Z_p^\times}
 p_{0,N}\log\langle Q/p^m\rangle .
$$
真实 pushforward 保一致误差，所以
$\mathscr W(f_{r,m})\to\mathcal B_{N,m}$。
(19) 于是给
$$
\boxed{\mathcal B_{N,m}+(1-\lambda^2)O_m^{[1]}=0.}
\tag{21}
$$
这逐项解释 R659(33)：
$$
\begin{aligned}
&a_5^{-m}\mathcal B_{N,m}-\mathcal B_{N,0}\\
&\qquad=-(1-\lambda^2)m\ell_\lambda O_0^{[0]} ,
\end{aligned}
\tag{22}
$$
其非零右边恰由原外部质量产生。
所以原中央零与 R659 的强制非零补偿差没有在此矛盾；
要继续闭合，就必须控制 (21) 的同一个实际外部行。

## 5. 原 T 中央在同一交域上的完整剩余两行

第二个原算术条件也可完整放回，不能把它笼统地当作又一个零。
定义
$$
\mathcal F^W_{r,m}(u)=
\int_{Y\in p^{r+m}}q_N\,
 1_{\{W P_{Y,(-\kappa)^{r+m}}^{-1}\ {\rm unit}\}}
 \langle W P_{Y,(-\kappa)^{r+m}}^{-1}\rangle^{d_pu}\,d\mu_0 .
$$
同一全核心和原 $\pi_4$ 中性准确给
$$
\boxed{\mathcal F^W_{r,m}(u)
=\lambda^{r+m}\beta^N\,6\delta J_T(u).}
\tag{23}
$$
它与 (5) 的域不同：这里是 Y 深，单位观察是完整移动的 W。

仍按 $A\in p^{2r}$ 分成 $\mathcal I^W+\mathcal O^W$。
共同域是 $A\in p^{2r},Q\in p^{r+m}$，故可进一步对 Q 作真核心。
令 $\epsilon=(-1)^m$（$r$ 为偶数），得到
$$
\mathcal I^W_{r,m}(u)=g_ra_5^m
 \int(q_N\circ B_r\circ P_{Q,\kappa^m})\,
 1_{\{Z^W_{r,m}\ {\rm unit}\}}
 \langle Z^W_{r,m}\rangle^{d_pu}\,d\mu_0 ,
$$
$$
\boxed{
\begin{aligned}
Z^W_{r,m}={}&
\{\kappa^{2r}(1-b_Y)+\epsilon b_Y\kappa^{r-m}\}A\\
&+\{\kappa^{r+m}(b_Q-b_Y)+\epsilon b_Y\}Q+b_LL .
\end{aligned}}
\tag{24}
$$
全部原 A、L 和其余伙伴仍在。
当 $r>m$ 时，单位 cut 准确稳定为
$$
B_\epsilon=b_LL+\epsilon b_YQ\ {\rm unit}.
$$
定义同一个原五输入权上的四个实际行
$$
\boxed{
\Theta_\epsilon^{[j]}=
\int_{\mathcal G_{0,N}}p_{0,N}\,
 1_{\{B_\epsilon\ {\rm unit}\}}
 (\log\langle B_\epsilon\rangle)^j\,d\mu_0,
\qquad \epsilon=\pm1,\quad j=0,1 .
}
\tag{25}
$$
$(\log)^0$ 在这里表示常数一。
(9)、(24) 给有限层质量误差 $p^{r+m-N}$ 和
log 误差 $p^{\min(r-m,r+m-N+1)}$，所以
$$
\boxed{
\lim_{r\ {\rm even}\to\infty}
 \frac{\mathcal I^W_{r,m}(0)}{g_ra_5^m}=\Theta_\epsilon^{[0]},
\qquad
\lim_{r\ {\rm even}\to\infty}
 \frac{(\mathcal I^W_{r,m})'(0)}{d_pg_ra_5^m}
       =\Theta_\epsilon^{[1]}.}
\tag{26}
$$
若再用原 $J_T(0)=J'_T(0)=0$，
相应完整 $\mathcal O^W$ 极限准确是 (26) 的负号，
不是 $\Theta_\epsilon^{[j]}=0$。

这些行的 Q/L 来源仍是 R653 全部五项
$$
F_{12}\otimes D_5-D_5\otimes F_{12}
 +3Z_5\otimes Z_5
 +6b(X_5\otimes\Sigma_5+\Sigma_5\otimes X_5).
\tag{27}
$$
(25) 的单位观察含 L 和 Q，不能只取 principal 的一项。
把 Q 真反射后，$\Theta_++\Theta_-$ 恰选 (27) 的前两项，
$\Theta_+-\Theta_-$ 恰选后三项，均附相同因子二及同一个
$B_+$ 测试。这是完整来源的奇偶拆分；
它没有把混合单位观察换成 Q 单位或 L 单位。

R655 的原 $I_{\Sigma,-1}\ne0$ 以及 R661 的两个 log 行身份
可继续用于 (27) 的实际分部，但必须支付 (25) 的仿射单位 cut。
不能由一个已知裸负一矩删掉其余四项和相应补域。

## 6. 已付边界

现在原两个中央同时零所留下的实际有限行已明确：

- Y 外部首二行是 (14)，其零阶质量为单位；
- 冻结门 W 补偿满足有限层 (19) 及极限 (21)，非齐次差由该质量补偿；
- 原 T 行留下 (25) 的两种完整混合单位观察，连同 (26) 的真实外部反号。

没有把 (14) 的不同尺度 log 质量拆开赋零，也没有把
(25) 的单位 cut 认成 R653 的独立 Q 测试。
下一缺口是这些同源实际外部行之间的附加关系，而不是再证明
R659 的局部强制差非零。主目标尚未完成。

## 精确文件

- [check-r662-annulus-exterior-and-exact-w-compensation.js](../scripts/check-r662-annulus-exterior-and-exact-w-compensation.js)
- [check-r662-annulus-exterior-and-exact-w-compensation.json](../scripts/check-r662-annulus-exterior-and-exact-w-compensation.json)

证书仅核真实原行、全部正交关系和 W 转置系数；
全核心、原算术回接、有限层误差及全部补域由上面完整证明支付。
