# R1048：原 AS 全函数、规范 Hasse 平方原函数与核的 critical-value 范数

日期：2026-11-27（UTC+8；2026-11-26 UTC）。
会话：Astra-serre-24b8836b-20261126；o2_high_coefficient / root。

**已证明：原 r=2 bare 系数所对应的核范数，可以用同一个实际
Ahlgren–Samart 旧形的完整函数、一个规范有理原函数，以及一个
保留全部 critical values 的唯一 cusp 留数读取。**
这里没有用一个同 shadow 的形式替换原源，也没有删除自由的
p 次幂项后擅自比较函数值。该自由项对本文的每一个局部留数均为零。

本文不证明该范数非零，不把原 r=2 结论扩张为 r=8 bare 结论。
R1037 的指定 CM jet 配对及其完整 graph-square 项仍另行保留。

## 1. 原对象、标架及尺度

取 R1041 的原行
$$
p=12g-1\ge41,\qquad p\equiv2,5\pmod9,
\qquad N=2g-1,\quad \ell=2N+2=(p+1)/3,
\quad m=(p-1)/2.
$$
在原 H_6 曲线 $\mathbf P^1_b$ 上，沿用
$$
r=1-b^3,\qquad
E_b:y^2=x^3+3brx+r(1-2b^3),\qquad
\omega=dx/(2y),\qquad
\operatorname{KS}(\omega^2)=\frac{db}{2r}.
\tag{1048.1}
$$
原 Hasse 为
$$
h=r^{N+1}A,\qquad A=bQ(b^3)\text{ 单首},\qquad
\deg Q=N,\quad \deg A=3N+1,
\qquad S=\{A=0\}\subset\mathbf F_{p^2}.
\tag{1048.2}
$$
所有根简单且避开 $r=0$。记
$$
\mathcal L=r\partial_b^2-4b^2\partial_b-\frac94b,
\qquad \mathcal LA=0,
\qquad \mathcal LT_0=A,
$$
$$
T_0\in\mathbf F_p[b^3],\qquad
\deg T_0=3N,\qquad \operatorname{lc}(T_0)=-1.
\tag{1048.3}
$$
$T_0$ 是 R1037 / R1041 已证明唯一的原核多项式。
令 $f=r^{4N+2}$，原核代表 $c_0\in\mathbf F_p[b]_{<3N+1}$
及完美对称型的规范为
$$
c_0(s)^p=\frac{T_0(s)A'(s)}{f(s)},\qquad
q_s=-\frac{f(s)}{A'(s)^2}\in\mathbf F_p^\times,
$$
$$
B(c_0,c_0)=\frac12\sum_{s\in S}q_s c_0(s)c_0(s^p).
\tag{1048.4}
$$
此处的 p 次方是实际 $\mathbf F_{p^2}$ 上 Frobenius；
对任意坐标作代换 $a(b^p)$ 时仍保持其系数不变。

原指定 oldform 写成
$$
F=V_{p-1}^{\dagger}
 =F_{p-1}(Q_{\!F})-2^{p-1}\zeta^2F_{p-1}(Q_{\!F}^4),
\qquad Q_{\!F}=e^{2\pi i\tau'/6}.
$$
为了不与多项式 $Q$ 混淆，本文给 Fourier 参数加下标。
在 (1048.1) 的同一 frame 中，R1041 给
$$
F=\xi r^{N+1}T_0,
\qquad
\xi=\rho^m12s_0\,864^N,
\qquad \rho^3=2,\quad \rho\in\mathbf F_p,
\quad s_0^2=-3,
$$
$$
\boxed{\qquad \xi^{p+1}=\rho/24.\qquad}
\tag{1048.5}
$$
这里保留原正 CM 嵌入及 Tate 相位。特别地，没有除掉一个尚未证明
为单位的 period。

## 2. 同一个 AS 全函数的微分桥

沿用 R1031 的实际 $\phi_p$：它是原 level-nine weight $-2$
弱全纯形式，具有原 $q^{-p}+O(q)$ 主部及原其它 cusp 条件。
令
$$
C=C_{\rm AS}(p)=\frac92\beta^3\in\mathbf F_p^\times,
\qquad
U=\phi_p(Q_{\!F})-\frac{\zeta^2}{4}\phi_p(Q_{\!F}^4).
\tag{1048.6}
$$
原 Faber 构造的全部主部在此保留。R1031 (1031.15)–(1031.16)
给真正的恒等式
$$
\Theta_{Q_{\!F}}U=-CF,
\qquad
\Theta_{Q_{\!F}}\big|_k
=6(hD_k+k\mathcal B),\qquad
\mathcal B=D_{p-1}h.
\tag{1048.7}
$$

两项 $\phi_p(Q_{\!F})$、$\phi_p(Q_{\!F}^4)$ 都是原 full-six
曲线上的 weight $-2$ 截面。确切地，对 $\gamma\in\Gamma(6)$，
$\tau'/6$ 与 $2\tau'/3$ 两个变量的共轭矩阵分别为
$$
\begin{pmatrix}a&b_\gamma/6\\6c_\gamma&d\end{pmatrix},
\qquad
\begin{pmatrix}a&2b_\gamma/3\\3c_\gamma/2&d\end{pmatrix};
$$
它们都属于原 $\Gamma_0(9)$，所以这里使用的是实际 full-six 源。
以下把它们在拉回的有理 frame $\omega$ 中读成有理系数。
偶权使原二次 twist 的选择相容；没有先假定 $U$ 作为函数下降到
$\mathbf P^1_b$。

由 KS 的尺度，在此 frame 中可写
$$
D_k=2r\partial_b+k\alpha_b.
$$
因为 $p-1=-1$ 于特征 p，
$$
\mathcal B=2rh'-\alpha_bh,\qquad
D_{-2}U=2rU'-2\alpha_bU.
$$
将这些代入 (1048.7)，连接项准确抵消：
$$
\Theta_{Q_{\!F}}U=12r(hU'-2h'U).
$$
因此得到原全函数微分式
$$
\boxed{\quad
d\left(\frac{U}{h^2}\right)
=-\frac{C\xi}{12}\,
  \frac{T_0\,db}{r^{\ell+1}A^3}.
\quad}
\tag{1048.8}
$$
等式先在原 fine 曲线的函数域成立；右侧是 (1048.1) 中
$b$ 上的固定有理微分的拉回。这说明的是微分在这个有理 Hodge
frame 中的实际下降，不是把权 $-2p$ 的截面当成 frame 无关函数。
若更换 Hodge frame，$U/h^2$ 的转换因子是一个 p 次幂，
所以同一微分式的运输仍然相容。

在每个 $s\in S$，原 AS 源在 fine 好模型上正则，
$h=0$ 且 $\mathcal B=2r^{N+2}A'$。由 (1048.7) 立即得到
$$
\boxed{\quad
U(s)=\frac{C\xi}{24}\frac{T_0(s)}{r_sA'(s)}.
\quad}
\tag{1048.9}
$$
所有 fine 点上的这个值一致；这是原恒等式给出的下降，
没有用任意解的取值替代真实 $U$。

## 3. 规范 Hasse 平方原函数

定义
$$
\boxed{\quad
H=r^{\ell+1}(AT_0'-T_0A').
\quad}
\tag{1048.10}
$$
由 (1048.3)，若 $W=AT_0'-T_0A'$，则
$$
rW'=4b^2W+A^2.
$$
又 $3(\ell+1)=p+4$，所以
$$
\boxed{\qquad H'=r^\ell A^2=h^2.\qquad}
\tag{1048.11}
$$
这是原 Hasse 平方的规范原函数；具体地
$$
H\in\mathbf F_p[b^3],\quad
\deg H=2p-1,\quad \operatorname{lc}(H)=-1,
\quad r^{\ell+1}\mid H.
\tag{1048.12}
$$
首系数直接来自 $\operatorname{lc}(W)=1$ 及 $\ell+1$ 为奇数。

置 $y=b^3$、$H(b)=\mathcal H(y)$，则
$$
\mathcal H'(y)=\frac13(1-y)^\ell Q(y)^2,
\qquad \deg\mathcal H=4N+3<p,
$$
$$
\boxed{\quad
\mathcal H(y)=-\frac13\int_y^1(1-t)^\ell Q(t)^2\,dt.
\quad}
\tag{1048.13}
$$
积分指逐项多项式积分；所有分母小于 p。$\mathcal H(1)=0$
固定唯一常数，故没有 first-p 积分歧义。

在原全部 SS 根处，(1048.10) 和 (1048.4) 给
$$
H(s)=-r_s^{\ell+1}T_0(s)A'(s),\qquad
\boxed{\quad c_0(s)^p=-\frac{H(s)}{r_s^p}.\quad}
\tag{1048.14}
$$
对这些值再取 p 次方，使用 $s^{p^2}=s$，得到准确的系数固定
剩余类式
$$
\boxed{\quad c_0(b)\equiv-\frac{H(b^p)}r\pmod A.\quad}
\tag{1048.15}
$$
分母 r 在这个商环中为单位。

## 4. 原核范数的完整 critical-value 和

由 (1048.4) 及 (1048.14)，得到
$$
\boxed{\quad
B(c_0,c_0)
=-\frac12\sum_{s\in S}
 \frac{H(s)^{p+1}}{r_s^{\ell+2}A'(s)^2}
=-\sum_{s\in S}\frac{H(s)^{p+1}}{r_s^2H'''(s)}.
\quad}
\tag{1048.16}
$$
第二式使用 $H'''(s)=2r_s^\ell A'(s)^2$。这里每个显示的分母
都是单位，但没有假定每个 $H(s)$ 非零，也没有假定全和不相消。
由 (1048.9) 还得到同一个实际 AS 函数值表达
$$
\boxed{\quad
B(c_0,c_0)=\frac{12}{C\xi}
                  \sum_{s\in S}H(s)^pU(s).
\quad}
\tag{1048.17}
$$

为保留所有 fine 点和 cusp，令 $\pi:X(6)\longrightarrow\mathbf P^1_b$
为 R936 / R1041 的有效 degree 12 tame cover，在原 $S$ 上不分歧。
在其函数域中设
$$
\eta_U=H^p\frac{h'}hU\,db.
\tag{1048.18}
$$
原所有 $S$ 上方的留数总和为
$$
\sum_{P\in\pi^{-1}S}\operatorname{Res}_P\eta_U
=12\sum_{s\in S}H(s)^pU(s)=C\xi B(c_0,c_0).
\tag{1048.19}
$$
这个 12 是实际 tame fine cover 的度数，不是 R932 原 Serre
下降中的 $d_1$，也没有另乘 fine Igusa cover 的 p−1。
全局留数定理因而给
$$
\boxed{\quad
B(c_0,c_0)=-\frac1{C\xi}
 \sum_{P\notin\pi^{-1}S}\operatorname{Res}_P\eta_U.
\quad}
\tag{1048.20}
$$
这一式起初保留全部其它点；下一节才用一个逐点成立的精确微分
把它们化为规范 cusp 留数。

## 5. p 次幂歧义在每一处留数中消失

在任一上述函数域中，若把 $U/h^2$ 换成 $U/h^2+Z^p$，
则 (1048.18) 的改变量是
$$
H^p hh'Z^p\,db
=\frac12d\bigl(H^ph^2Z^p\bigr).
\tag{1048.21}
$$
它在每个点的留数准确为零，包括原 cusp、CM 标记和所有 SS 点。
这不是只证明总留数为零，也没有假设 Z 在某处正则。

现在构造基底上唯一的规范原函数。记
$$
\nu=\frac{T_0\,db}{r^{\ell+1}A^3}.
$$
R1041 的原 whole-space Cartier 核给
$\operatorname{Car}(u^p\nu/12)=0$，其中 $u^m=h$。
Cartier 的 p 次幂线性性及其对可分拉回的相容性给
$\operatorname{Car}(\nu)=0$：Kummer cover 可分，故基底微分的
拉回是单射。此步骤保留了 r=0 处的全部极部，不能只由 SS
留数为零代替。

$\nu$ 在 S 的极阶至多 3，在 r=0 的极阶至多 $\ell+1<p$，
无其它有限极点；在∞为 $b^{-2p-2}(1+O(b^{-1}))db$。
其 Cartier 为零，故所有简单极部系数均为零。
逐项积分全部有限主部，得到唯一有理函数 J，满足
$$
dJ=\nu,\qquad J(\infty)=0,
\qquad \operatorname{ord}_{s}J\ge-2\ (s\in S),
\qquad \operatorname{ord}_{r=0}J\ge-\ell.
\tag{1048.22}
$$
这些极阶均小于 p。因而两个这样的解之差若导数为零，只能为
无有限极点的 p 次幂函数；再用∞归一化，差为零。
唯一性亦给 $J\in\mathbf F_p(b)$。

所以存在唯一多项式 $P_{\rm prim}$，使
$$
J=\frac{P_{\rm prim}}{h^2},\qquad \deg P_{\rm prim}<2p-2.
$$
它实际满足更精确的断言
$$
\boxed{\quad
P_{\rm prim}\in\mathbf F_p[b^3],\qquad
\deg P_{\rm prim}=p-2,\qquad \operatorname{lc}(P_{\rm prim})\ne0.
\quad}
\tag{1048.23}
$$
证明次数时必须保留∞处导数杀掉的 $b^{-p}$ 项。
若 J 的∞首零阶为 v，则 $0<v\le2p-2$；若 $p\nmid v$，
$dJ$ 的首阶为 $b^{-v-1}db$，与 (1048.22) 的
$b^{-2p-2}db$ 矛盾。因此 v=p，给出所示次数。
另一方面，若写 $\nu=v(b)db$，则 $v(\zeta b)=v(b)$，
故 $[\zeta]^*\nu=\zeta\nu$；由唯一性得到
$J(\zeta b)=\zeta J(b)$，没有剩余常数差。
因 $h(\zeta b)^2=\zeta^2h(b)^2$，得到 $P_{\rm prim}(\zeta b)=P_{\rm prim}(b)$。

把 (1048.22) 清分母，得到可直接复核的完整一阶式
$$
\boxed{\quad
rA P_{\rm prim}'+(b^2A-2rA')P_{\rm prim}=T_0.
\quad}
\tag{1048.24}
$$
特别地，对所有 $s\in S$，包括 $T_0(s)=0$ 的情形，均有
$$
P_{\rm prim}(s)=-\frac{T_0(s)}{2r_sA'(s)}.
\tag{1048.25}
$$

在原 fine 函数域内，(1048.8) 与 (1048.22) 的差导数为零。
在完美常数域上，函数域的微分常数恰是其 p 次幂子域，故
$$
\boxed{\quad
\frac{U}{h^2}=-\frac{C\xi}{12}J+Z^p
\quad}
\tag{1048.26}
$$
对某个实际 fine 函数 Z 成立。此式没有声称 U 在 b 上下降；
它只把其全部不下降部分准确收入导数为零的那一项。
在 S 上，两侧非 p 次幂项的候选极阶至多 2，原 U 正则，
所以 $Z^p$ 在这些点无极点；(1048.26) 也直接恢复 (1048.9)。

由 (1048.21)，(1048.18) 在每一点的留数都等于
$$
-\frac{C\xi}{12}\,\pi^*
 \left(H^p\frac{h'}hP_{\rm prim}\,db\right).
$$
基底括号中的微分在 r=0 无极点，因为 $H$ 被 $r^{\ell+1}$
整除；其它有限极点只在 S。因此 (1048.20) 化为
$$
\boxed{\quad
B(c_0,c_0)
=-\sum_{s\in S}H(s)^pP_{\rm prim}(s)
=\operatorname{Res}_{b=\infty}
 H^p\frac{h'}hP_{\rm prim}\,db.
\quad}
\tag{1048.27}
$$
所有 fine cusp 都已经由实际 degree 12 的留数拉回合计，
没有只选一个 fine cusp。三个 r=0 标记的原留数为零也在这里
逐点得到；不是在建立全函数恒等式前把它们删掉。

## 6. 同一规范 primitive 的二次多项式身份

令 $F_0=T_0/A$。由 (1048.10) 及 (1048.22)，
$$
F_0'=\frac{H}{rh^2},\qquad J'=\frac{F_0}{rh^2},
\qquad H'=h^2.
$$
因此
$$
K=F_0^2-2HJ
\quad\text{满足}\quad K'=-2h^2J=-2P_{\rm prim}.
$$
K 在 r=0 正则；在 S 的候选极阶至多 2。其导数是多项式，
而这些候选极阶严格小于 p，故全部有限极点消失。于是
$$
\boxed{\quad
K\in b\mathbf F_p[b^3],\qquad
\deg K=p-1,\qquad
K'=-2P_{\rm prim},\qquad
\operatorname{lc}(K)=2\operatorname{lc}(P_{\rm prim}).
\quad}
\tag{1048.28}
$$
次数与首系数由 $H=-b^{2p-1}+\cdots$、
$J=\operatorname{lc}(P_{\rm prim})b^{-p}+\cdots$ 得到。
角色由 $F_0(\zeta b)=\zeta^2F_0(b)$、$J(\zeta b)=\zeta J(b)$
及 H 不变给出。等价的无分母式为
$$
\boxed{\quad
A^2K=T_0^2-2r(AT_0'-T_0A')P_{\rm prim}.
\quad}
\tag{1048.29}
$$
本节没有把 $P_{\rm prim}$ 的非零首系数等同于 (1048.27)
中指定的高 residue；后者仍有实际 Frobenius critical-value 总和。

### 6.1. 规范分子是同一个 Hasse 平方的准确 p-block

作唯一的按次数分拆
$$
G=h^2=G_0+b^pG_1,\qquad \deg G_0<p,\quad\deg G_1\le p-2,
$$
$$
H=H_0+b^pH_1,\qquad \deg H_0<p,\quad\deg H_1\le p-1.
\tag{1048.30}
$$
由原角色及单首性质，$G_1\in\mathbf F_p[b^3]$ 单首、次数 p−2；
$G_0$ 只含指数为 2 mod3 的项，故 $\deg G_0\le p-3$。
同样 $H_0\in\mathbf F_p[b^3]$、$\deg H_0\le p-2$，
$H_1\in b\mathbf F_p[b^3]$、次数 p−1、首系数 −1。
$H'=G$ 给 $H_0'=G_0$、$H_1'=G_1$。

令 $a=[b^{p-3}]G$。则准确有
$$
\boxed{\quad
a\ne0,\qquad
P_{\rm prim}=\frac{G_1}{a},\qquad
K=-\frac{2H_1}{a}.
\quad}
\tag{1048.31}
$$
证明如下。写 $L=\operatorname{lc}(P_{\rm prim})$。
(1048.22) 的微分首项及第5节角色给
$$
J=L b^{-p}+O(b^{-2p-1}).
$$
这里中间非 p 倍指数都由导数排除；可能的 $b^{-2p}$ 项则因
$J(\zeta b)=\zeta J(b)$ 而为零。乘以 h² 并取 polynomial part，
得到 $P_{\rm prim}=LG_1$。因此
$$
J=\frac{LG_1}{b^pG_1+G_0}
 =L b^{-p}-La\,b^{-2p-1}+O(b^{-2p-2}).
$$
与 $dJ=b^{-2p-2}(1+O(b^{-1}))db$ 比较，给 $La=1$。
最后 $K'=-2G_1/a$、$H_1'=G_1$，加上两者相同的非平凡
$\mu_3$ 角色，排除常数差，证明 (1048.31)。

将此代入 (1048.29)，还得真正的二乘二 Wronskian 身份
$$
\boxed{\quad
H_0H_1'-H_1H_0'
 =\frac a2\,r^\ell T_0^2.
\quad}
\tag{1048.32}
$$
确切地，先将 $K=F_0^2-2HJ$ 乘以 h²；
然后使用 $P_{\rm prim}=G_1/a$、$K=-2H_1/a$，
所有 $b^p$ 项相消，得到所示式子。
这给原 Faber 源的一个完全指定的 Hasse 平方 p-block，非任意
满足同一微分方程的多项式。

相应地，原目标也可准确写成
$$
\boxed{\quad
B(c_0,c_0)
=-\frac1a\sum_{s\in S}H(s)^pG_1(s)
=\frac1a\operatorname{Res}_{\infty}
 H^p\frac{h'}hG_1\,db.
\quad}
\tag{1048.33}
$$
a 的单位性支付的是规范 primitive 的首项；它没有消去
(1048.33) 的完整 Frobenius critical-value 总和。

### 6.2. 同一 p-block 的原 f_N 端点平方

在 $b=1$，$H$ 的零阶至少为 $\ell+1$，而 J 的极阶至多为
$\ell$，所以 $HJ$ 在这里为零。因此第6节给
$$
K(1)=\frac{T_0(1)^2}{A(1)^2}=-\frac{2H_1(1)}a.
$$
又 $H(1)=H_0(1)+H_1(1)=0$。消费 R1043 的同一个
$f_N=-T_0(1)/6$，得到当前原行的准确式
$$
\boxed{\quad
f_N^2=-\frac{A(1)^2}{18a}H_1(1)
     =\frac{A(1)^2}{18a}H_0(1).
\quad}
\tag{1048.33a}
$$
所有外因子为单位；所以原端点非零等价于这个完全指定的
$H_0(1)$ 非零。本式保留规范原函数 H 的常数项与整个 p-block，
不是先前已排除的单个 sigma 系数平方猜测。
它仍没有证明 $H_0(1)$ 非零，也没有把该端点等同于 (1048.33)
的核范数。

## 7. 返回原 bare 判据及保留的问题

R1041 的准确原 fine 和为
$$
S_{\rm orig}^{\,p}=-36\rho B(c_0,c_0).
\tag{1048.34}
$$
原 Fourier Cartier 因子 $1/6$、KS 因子 $1/2$、
$\xi^{p+1}=\rho/24$、fine tame degree 12、
以及 R932 原 Serre 下降的 $d_1$ 全都保持原值。
因此 R978 / R988 / R1041 的同一个原判据仍是
$$
\overline{c_{p-2}^{+}}\ne0
\iff\overline{c_{p-2}^{-}}\ne0
\iff B(c_0,c_0)\ne0
\iff\operatorname{Res}_{\infty}
 H^p\frac{h'}hP_{\rm prim}\,db\ne0.
\tag{1048.35}
$$
本文没有证明这些等价条件成立。核一维、完美 B、规范
$P_{\rm prim}$ 的次数和非零首系数、AS 的低坐标 C 为单位，
都不能单独替代这个指定 residue 的非零。
也没有把 $f_N=-T_0(1)/6$ 的端点读数或 R1037 的
$B((1-\overline{\mathcal Q})\lambda,\overline{\mathcal Q}DJ)$
当作该自配对。

## 来源与验证范围

- [R1031](R1031-original-fN-and-actual-Faber-truncation-central-derivative.md)，
  §§1–4：原 AS 主部、真实 Faber 分拆、full-six oldform 和 Katz 尺度。
- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：
  实际 graph 核、系数固定的 Frobenius 坐标及原 B。
- [R1041](R1041-original-r2-bare-coefficient-and-Hodge-kernel-norm.md)：
  整个 Hodge frame、whole Cartier 核、原 $\xi$、全部 fine 点及真正 bare 判据。
- [R1043](R1043-original-fN-and-Hodge-kernel-CM-endpoint.md)：
  相同 $T_0$ 的端值尺度；本文不把端值非零与范数非零等同。
- 原 Ahlgren–Samart 文献、R932 / R936 / R952 的精确来源及原
  Robert 坐标比较，均按上述结果的原假设和完整规范消费。

全部新式为纸面微分、局部主部、完美域函数域的微分常数及全局
留数推导。没有数学程序执行，没有重复有限素数窗口。
