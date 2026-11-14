# R496 — 新缺一 sigma 轴的完整两层核、四个实际来源与 48 元群

日期：2026-11-14。**状态：已证明。**

R493 的实际三阶几何变换 $\mathcal T$ 固定 $Y_s$，使
$W'=W\mathcal T$ 不含原独立输入 $\xi_4$。本篇在同一个原
六 sigma 联合上取 $V'=W'/2$，支付整个两层核心的四挠中心相位。
原三个来源只须增加一个真实来源 $q$，便与旧 $W$ 核闭合。
在适当整基中，这两个真实核心生成 $48$ 元群；R494 的原
$W,Q,U,\mathbf R$ 深度矩形也保这个四维空间。

新增的 $q$ 和 $z=q-h/2$ 有**整个 W 边际恒零**。
$z$ 的整个第一 $Y$ 二挠不变部分也为零，principal 部分只在
原正 $N_7^9$ 块。这里不由零质量、有限矩阵或非零边际
给它另赋一个算术中央条件。文末保全部物理变换和词像格。

## 1. R493 的同一真实缺一输入轴

用 R493 的六个未缩放输入
$$
\boldsymbol\xi=(\xi_1,\xi_2,\xi_3,\xi_4,c,d_0),\qquad
\rho_0=-\frac1{84}\nu_\sigma^{\otimes6}.
\tag{1}
$$
物理输出仍为
$$
\begin{aligned}
Y_s&=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma\xi_4+c+2d_0,\\
W&=\delta\xi_1+2\delta\xi_2+\gamma\xi_3+\bar\gamma\xi_4+3\delta c+4d_0.
\end{aligned}
\tag{2}
$$
从未缩放输入到 R465 的 $t_i$ 坐标是固定 $p$ 单位对角变换；
本篇所有公式都可经该变换逐项写回原坐标。

R493 给实际 Hermitian 等距 $\mathcal T$，满足
$$
\mathcal T^3=I,\quad Y_s\mathcal T=Y_s,\quad
h=e_1+e_2=\omega^2\mathcal T_*\rho_0,
\tag{3}
$$
以及准确
$$
W'=W\mathcal T
=(2+2\delta)\xi_1+2\delta\xi_2
 +(2+2\delta)\xi_3+(3+\delta)c+4d_0.
$$
故取
$$
\boxed{
V'=W'/2=(1+\delta)\xi_1+\delta\xi_2
 +(1+\delta)\xi_3+\frac{3+\delta}{2}c+2d_0.}
\tag{4}
$$
它的系数都在 $\mathbf Z[\omega]$ 中，第四系数为零，degree 为
$4+3+4+3+4=18$。以下用行向量 $v$ 表示 (4)，$w$ 表示 (2) 的 $W$。

可取五个完整伴随
$$
r_j=2\xi_j-\bar v_jd_0,\qquad 1\le j\le5.
\tag{5}
$$
从 $\boldsymbol\xi$ 到 $(V',r_1,\ldots,r_5)$ 的矩阵记 $M_V$。
直接有
$$
\det M_V=-288,\qquad
M_V\bar M_V^{\,t}=
\begin{pmatrix}18&0\\0&H_5\end{pmatrix},
\quad (H_5)_{jk}=4\delta_{jk}+\bar v_jv_k.
\tag{6}
$$
这保全部五个伴随；尤其 $r_4=2\xi_4$。
不需要把后面五个非对角 theta 轴先化成一个边际。

原第一 $V'$ 半特征平凡：仅 $\delta$ 和 $(3+\delta)/2$ 是奇
CM 系数，其余非零系数为偶。因此完整原来源在该轴属于
$\mathcal S_{18}$。R426 已付整个 $K_{18}=-I$，所以
$$
\nu_{\rho_0}|_{V'\in p^n\mathbf Z_p}
=(-\lambda)^n(P_{V,n})_*\nu_{\rho_0}.
\tag{7}
$$
它保 $\xi_4$ 及全部 (5)。这也与 (3) 将 $h$ 的原 $W$ 核
拉回得到的结果完全一致。

## 2. 同一个固定覆盖中的十六个真实平移

仍记
$$
f_t=\mathsf T_{t,W}^{(72)}\rho_0,\qquad
t=\ell/4,\quad \ell=m+n\omega,\quad m,n\in\{0,1,2,3\}.
\tag{8}
$$
这些是完整六变量来源，而非 $W$ 边际。
在原 $M$ 坐标中它们全在 R465 的原整张量格内。
在新 $V'$ 坐标中则须保平坦 twist；不能先断言
它们全在原 $\mathcal S_{18}$。

对 (6) 的所有六个生成变量作固定 $[4]$ 覆盖，全部十六个
来源进入同一个 untwisted 整 theta 格；第一因子是
$\mathcal S_{288}$。矩阵 $4M_V$ 的行列式在当前普通处为单位，
故这是完整普通测度的合法重新表示，未遗失任一输入事件。
后五轴可保完整 Hermitian 格 $16H_5$，第一轴与它们无交叉。

原 $W$ 平移在未覆盖 $V'$ 生成变量上的分量是
$$
\frac{a\,t}{18},\qquad
\boxed{a=w\bar v^{\,t}=29+7\omega=\frac{51+7\delta}{2},
       \quad N(a)=687.}
\tag{9}
$$
所以在 degree $288$ 上的合法 Heisenberg 参数准确是
$a\ell/288$。原五伴随的平移原样保留。

## 3. 真正两层 V′ 核的完整中心

当前 R488 ray 给
$$
g\equiv91+72\omega\pmod{576},\qquad
g^2\equiv217+432\omega
       =1+216\delta\pmod{576}.
\tag{10}
$$
第一覆盖轴的真实 $K_{288}^2$ 将 (9) 的参数变成
$$
\frac{g^2a\ell}{288}
=\frac{a\ell}{288}+\frac{q_\ell}{4},
\qquad q_\ell=3\delta a\ell.
\tag{11}
$$
第二项是原未覆盖 $\mathcal S_{18}$ 的格周期。
其格特征为一，但它与第一项的 canonical 交叉相位不能省略。

用 $E(1,\omega)=1$ 及
$\mathsf T_s\mathsf T_t=e^{\pi iNE(s,t)}\mathsf T_{s+t}$，
在 (11) 中准确得到
$$
\exp\!\left[-\pi i\,288
 E\left(\frac{a\ell}{288},\frac{3\delta a\ell}{4}\right)\right]
=\exp\!\left[-\frac{3\pi i}{2}N(a)N(\ell)\right]
=(-i)^{N(\ell)}.
\tag{12}
$$
最后一步用 $N(a)=687\equiv3\pmod4$。
$g^2$ 的模 $576$ 代表改变只加偶格周期，相关交叉相位为一。
式 (7) 给同一个原来源的 $K_{288}^2\rho_0=\rho_0$，
所以没有额外待定绝对标量。

于是，写
$$
\epsilon(t)=(-i)^{N(4t)},\qquad F:=K_{V'}^2,
$$
有完整来源等式
$$
\boxed{Ff_t=\epsilon(t)f_t.}
\tag{13}
$$
这是两层实际限制之后的 normalized 来源算子；
外部测度系数是 $\lambda^2$，见 §9。
式 (13) 没有改变其余五个 $V'$ 伴随或原独立 $\xi_4$。

作为整个覆盖的检查，$g^8\equiv289=1+288\pmod{576}$，
使 $K_{288}^8$ 与完整 Heisenberg 群交换。
实际非零锚 $\Theta(12z)$ 的核心为 $-1$，故整个
$K_{288}^8=I$。但本篇只把**偶** $V'$ 深度与旧 $W$ 核合用；
没有将未经处理的奇深状态塞回原 degree72 张量格。

## 4. 旧 W 核的精确十六系数

定义
$$
a_t=\begin{cases}-1/4&t\in E[2],\\+1/4&t\notin E[2].\end{cases}
\qquad
e_0=f_0,\quad e_1=\sum_ta_tf_t,\quad e_2=\sum_ta_t\epsilon(t)^2f_t.
\tag{14}
$$
这是 R488 的原三态。
当前 $g$ 在四挠上为 $-1$，且原 degree72 中的格周期相位为一，
所以
$$
K_Wf_t=\mathsf T_{-t,W}K_Wf_0.
$$
将全部 canonical 乘法写开，若 $t=\ell/4$、
$r=\ell'/4$，在固定十六代表中得到
$$
\boxed{
K_Wf_t=\sum_r a_{r+t}\,
 i^{-\det(\ell,\ell')}\,f_r,}
\tag{15}
$$
其中 $\det(m+n\omega,m'+n'\omega)=mn'-nm'$。
这个指数来自原 degree72 的
$\exp(72\pi i E(-t,r+t))$，不是无中心的有限平移和。

(13)、(15) 对同一批完整函数成立，故其任意有限线性组合都是
完整来源等式。系数按四个 $\mu_6$ 轨道
$$
\{0\},\quad E[2]\setminus\{0\},\quad N(\ell)\equiv1\pmod4,\quad
N(\ell)\equiv3\pmod4
$$
聚合后，$K_W$ 的准确矩阵为
$$
\begin{pmatrix}
-1/4&-3/4&3/2&3/2\\
-1/4&-3/4&-1/2&-1/2\\
1/4&-1/4&-1/2&1/2\\
1/4&-1/4&1/2&-1/2
\end{pmatrix},
\qquad F=\operatorname{diag}(1,1,-i,i).
\tag{16}
$$
这些有限表只用于支付已定义来源的等式；实际独立性在下一节证明。

## 5. 只增加一个真实来源

置
$$
\boxed{q=Fe_1=\sum_t a_t\epsilon(t)f_t,\qquad
h=e_1+e_2,\qquad z=q-h/2.}
\tag{17}
$$
由 (13)–(16) 逐项得到
$$
K_Wq=-q,\qquad
Fe_0=e_0,\quad Fe_1=q,\quad Fq=e_2,\quad
Fe_2=e_1+e_2-q,\quad Fh=h.
\tag{18}
$$
所有项仍是原 $W$ 四挠平移，故同处 R465 的原 $M$ 格和原
$L=(2Y_s,2Q_s,2U_s,\mathbf R)$ 格；没有再扩大 theta level。
系数 $1/2,1/4,i$ 在一个固定系数扩张中整且为单位。

使用 R488 的
$$
u=e_0+h/2,\qquad v=e_1-h/2
$$
后，完整核心成为
$$
\boxed{
\begin{array}{c|rrrr}
 &u&v&z&h\\ \hline
K_W&v&u&-z&-h\\
F&u&z&-v&h .
\end{array}}
\tag{19}
$$
它还给
$$
\boxed{F^2=K_A^2=R}
\tag{20}
$$
在整个四维空间上成立：R488 的两层 $A$ 核在每个 $f_t$ 上
准确乘 $\epsilon(t)^2$，原四挠参数两次回到原值。

四个来源确实线性独立，而非只有四个形式标签。
R488 已证 $u,v,h$ 独立。
由 (19)、(20)，$K_Wz=-z$、$Rz=-z$，
而 $\operatorname{span}\{u,v,h\}$ 中这两个负特征的共同交为零。
又 $Fz=-v\ne0$，所以 $z\ne0$，且不在该三维空间。

在 $(u,v,z)$ 上，(19) 是有向带符号置换：
$F$ 是固定 $u$ 的四分之一转动，$K_W$ 交换 $u,v$ 并反 $z$。
它们生成全部 $24$ 个三维有向带符号置换。
另一方面
$$
\boxed{(K_WF)^3=\operatorname{diag}(1,1,1,-1)}
\tag{21}
$$
在 $(u,v,z,h)$ 上独立反转 $h$。所以完整实际群恰有
$$
\boxed{48\text{ 个元素}.}
\tag{22}
$$
这是已证明四个完整来源上的真实核群；它不是对未付物理域作商
后得到的形式矩阵群。

## 6. 新来源的短半周期表达

R494 已证明全部 $f_t$ 保独立原 $\sigma(d_0)$ 因子，且
$$
f_t=\chi_{\rm lat}(4t)\,\mathsf T_{t,B}^{(56)}e_0,\qquad
a_t=-\chi_{\rm lat}(4t)/4.
$$
定义完整加权算子
$$
J_\epsilon=\frac14\sum_{t\in E[4]}
 \epsilon(t)\mathsf T_{t,B}^{(56)}.
\tag{23}
$$
因此 $q=-J_\epsilon e_0$。
在 R494 的 entire degree56 Schrödinger 基上，用其
$\mathsf T_{(s+r\omega)/4}e_j=i^{s(j+7r)}e_{j+14r}$，直接求和得
$$
J_\epsilon H_{2,B}=4J_\epsilon.
\tag{24}
$$
因为 $h=-H_{2,B}e_0/2$，严格得到
$$
\boxed{q=(J_\epsilon/2)h.}
\tag{25}
$$

为给 (25) 完整的较小表达，在
$\operatorname{im}(H_{2,B})=[2]^*\mathcal S_{14}$ 上取底层基
$e_j$，半周期生成元满足
$$
X^7e_j=(-1)^je_j,\quad Z^7e_j=e_{j+7},\quad X^7Z^7=-Z^7X^7.
$$
(23) 准确下降为
$$
\left.J_\epsilon\right|_{[2]^*\mathcal S_{14}}
=(I-iZ^7)(I-iX^7).
\tag{26}
$$
所以回到原 $B$ 的 canonical 四挠平移，
$$
\boxed{
q=\frac12(I-i\mathsf T_{\omega/4,B})
             (I-i\mathsf T_{1/4,B})h
=\frac h2-\frac i2
 \bigl(\mathsf T_{1/4,B}+\mathsf T_{\omega/4,B}
                     +\mathsf T_{(1+\omega)/4,B}\bigr)h.}
\tag{27}
$$
第二等号保了
$\mathsf T_{\omega/4,B}\mathsf T_{1/4,B}
=i\mathsf T_{(1+\omega)/4,B}$ 的中心。
底层 $(J_\epsilon/2)^2-(J_\epsilon/2)+I=0$，
也由 (26) 直接得到。
(27) 不涉及给某个半周期常数任意选择平方根。

### 6.1 整个 W 边际确实为零

从完整来源中抽出独立 $\sigma(d_0)$，写
$$
h=\widehat h\otimes\nu_\sigma
$$
并把固定常数并入五输入残余 $\widehat h$。
令 $H_B(z)$ 为 $\widehat h$ 忘掉 $Q,\mathbf R$ 后的真实
$B$ 生成函数。由 $W=B+4d_0$，
$$
W_*h\quad\text{的生成函数为}\quad H_B(z)\sigma(4z).
$$
R488 已证整个 $W_*h=0$。全纯函数环是整环，而
$\sigma(4z)\ne0$，所以 $H_B=0$。

(25) 只在残余 $B$ 上作用，且与忘掉 $Q,\mathbf R$ 交换。
因此其新残余的 $B$ 边际是 $J_\epsilon H_B/2=0$。
再乘回同一个独立 sigma，严格得到
$$
\boxed{W_*q=0,\qquad W_*z=0.}
\tag{28}
$$
这里约消的是明确抽出的五输入残余乘积；
没有把因 sigma 质量零而平凡为零的全六输入 $B$ 边际拿来约消。
故没有一个需要另识别算术角色的非零 $W$ 来源。

### 6.2 整个第一 Y 负块与正块

R493 的 $\mathcal T$ 固定 $Y_s$，且
$$
B\mathcal T=(2+2\delta,\,2\delta,\,2+2\delta,\,0,\,3+\delta,\,0).
\tag{29}
$$
在 (27) 三个非零四挠平移中，令 $t=\ell/4$，
$\ell=1,\omega,1+\omega$。它在未加倍 $Y_s$ 上的平坦参数是
$$
\boxed{(29+3\delta)t
=\frac{(16+3\omega)\ell}{2}
\equiv\frac{\omega\ell}{2}\pmod\Lambda.}
\tag{30}
$$
这是三个互异、非零二挠 flat twist。
在原加倍 $Y=2Y_s$ 的 degree136 格中，
它们准确给三个非平凡二挠特征。
所以 $z$ 的整个第一轴二挠平均为零；$q$ 的二挠不变部分是 $h/2$。
在 principal 角型上，R466/R476 的
$K_{136}=R_{-1}B_2=-N_7^9$ 遂给
$$
\boxed{
\frac{I-N_7^9}{2}\Pi_{0,Y}q=\frac12\Pi_{0,Y}h,\qquad
\frac{I-N_7^9}{2}\Pi_{0,Y}z=0.}
\tag{31}
$$
这里可保完整另外五个 $Y$ 伴随；不是仅一个质量等式。

$z$ 的完整 $Y$ 边际还确实非零：
(27) 中三个未投影边际各是六个非零线性 sigma 因子的全函数乘积，
并且具有 (30) 的三个互异 flat 特征，不能彼此相消。
三个 $Y_s$ 系数在原六 sigma 中全非零，所以没有一个因子
恒为 $\sigma(0)$。原 $\mu_6$ 对十六标签保 $N(\ell)$，
故其聚合边际属于 principal 角型。
这证明了一个真实非零正块来源，但没有给它任何未经证明的
rank-two 身份或中央零。

## 7. R494 的完整旧 M 矩形也保四态

在四个真实来源上，直接由 (15) 得
$$
H_{2,W}q=4q,\qquad H_{2,W}z=4z.
$$
所以 $B_2=H_2/2-I$ 固定 $q,z$。
R494 的 $J_{56}=-K_W$ 在整个原 $W$ 四挠平移张成空间上成立：
把 canonical cocycle 展开后，等式正是
$$
\chi(r+t)=\chi(r)\chi(t)(-1)^{\det(r,t)},
\qquad \chi(t)=(-1)^{N(4t)}.
$$
故 $K_B=K_WB_2$，从而
$$
K_Bq=-q,\qquad K_Bz=-z.
$$
所有四态的系数都对 $t\mapsto-t$ 不变，因此 R488 的完整
$K_AK_c=-\chi I$ 仍成立。依照 R494 同一个整双深域的证明，
$K_Q=-\chi K_B$、$K_U=-K_WK_B$ 也保四态。
新增两态的实际 scalar 表为
$$
\boxed{
\begin{array}{c|rrrrr}
 &K_W&K_B&K_Q&K_U&K_{R_1}K_{R_2}K_{R_3}\\ \hline
q&-1&-1&\chi&-1&\chi\\
z&-1&-1&\chi&-1&\chi .
\end{array}}
\tag{32}
$$
$u,v,h$ 的表仍逐字为 R494 的表。

因此 R494(33)–(35) 的原真实矩形
$\mathcal D_{\mathbf n,r}$，对 $q,z$ 也准确有
$$
\boxed{
\nu_\zeta|_{\mathcal D_{\mathbf n,r}}
=(-1)^{n_W+n_U}\chi^{n_Q+r}
\lambda^{n_W+n_Q+n_U+3r}
(P_{\mathbf n,r})_*\nu_\zeta,\qquad \zeta=q,z.}
\tag{33}
$$
它保全部原输入，而不仅是四态中的某个边际。
原 $Y_s$ 的变化仍必须使用 R494(38) 的三个不同尺度。

## 8. 原算术投影与新增状态的准确范围

四态仍在原 $L$ 完整 theta 格中，故 R483 的三个 rank-one
第一轴算术投影可以逐态施加。需要的同时 CM13/19 特征也保持：
$F=K_{V'}^2$ 与整个 simultaneous CM trace 的交换子至多标量，
而 $[4]^*\mathcal S_{18}$ 上 $F=I$，CM trace 保该非零子空间且
可逆，迫交换标量为一。原整坐标的行列式只含 $2,3$，与
$13,19$ 互素，完整纤维重排与 R483 相同。

于是旧五伴随实现仍可用于 $q,z$。
若三个原 rank-two 中央导数同时为零，原 $S$ 和 $S_{\rm new}$
投影的完整第一单位中央行仍为零，允许任意独立旧五伴随测试。
$T$ 的正 $W$ 投影在 $q,z$ 上已由 (28) 整个消失。
参考 $H_{\rm ref}$ 及其完整伴随、所有外谱仍须保留。
本篇未计算或猜定新增参考伴随的质量。

式 (31) 不允许在混合 $W,V',A$ 管内先施投影再删条件。
下面的全部物理变换使这种区别明确可检验。

## 9. 新轴的实际输入变换与两种返回

在未缩放六输入中定义
$$
\boxed{
P_{V,n}=I+\frac{\kappa^n-1}{18}\bar v^{\,t}v.}
\tag{34}
$$
它把 $V'$ 乘 $\kappa^n$，逐个固定 (5)，特别固定原
$\xi_4$。源算子 (13) 的真实含义是
$$
\boxed{\mu|_{V'\in p^2\mathbf Z_p}
=\lambda^2(P_{V,2})_*F\mu}
\tag{35}
$$
对全部四个来源成立。
原第一输出被准确送至
$$
\boxed{
Y_s\longmapsto
Y_s+\frac{37-3\delta}{36}(\kappa^n-1)V'.}
\tag{36}
$$
原其他五输入也按 (34) 改变；不能只保 $\xi_4$ 而删除其余条件。
$W'=2V'$，所以当前处的深度条件等价，但物理尺度中的 $2$ 保留。

旧 $W$ 仍满足
$$
\mu|_{W\in p\mathbf Z_p}
=\lambda(P_W)_*K_W\mu,\qquad
P_W=I+\frac{\kappa-1}{72}\bar w^{\,t}w.
\tag{37}
$$
这与 R465 的 $t_i$ 版本经固定对角变换严格相同。

由 (20)，原两层 $A$ 与新四层 $V'$ 给同一个来源算子，
但不同物理域：
$$
\boxed{
(P_{A,2}^{-1})_*(\mu|_{A\in p^2})
=\lambda^{-2}(P_{V,4}^{-1})_*(\mu|_{V'\in p^4}).}
\tag{38}
$$
两个逆推前只施于所示受限像格。
原 $A$ 缩放会改变 $\xi_4$，新 $V'$ 缩放保持它，
所以 (38) 不能被改成两个域相等。

令
$$
C_p=(P_{V,2}P_W)^3.
$$
R488 的准确词像格规则与 (21) 给
$$
\boxed{
\mu|_{C_p\mathbf Z_p^6}
=\lambda^9(C_p)_*Z\mu,\qquad
Z(u,v,z,h)=(u,v,z,-h).}
\tag{39}
$$
再平方得到
$$
\mu|_{C_p^2\mathbf Z_p^6}
=\lambda^{18}(C_p^2)_*\mu.
\tag{40}
$$
$\det C_p=\kappa^9$；群关系不使 $C_p$ 为恒等。
这里保的是连续操作后的准确像格，不是原 $W,V'$ 坐标的
朴素矩形。R493 的五深一单位网格、原 $\xi_4^6$ 测试，
以及全部旧伴随条件若附在 (35)–(40)，都须按显示矩阵转置。
它们的补域尚未因此被置零。

## 10. 可重现证书及直接依赖

- [check-r496-original-new-axis-and-four-state-group.py](../scripts/check-r496-original-new-axis-and-four-state-group.py)
- [check-r496-original-new-axis-and-four-state-group.json](../scripts/check-r496-original-new-axis-and-four-state-group.json)

脚本精确检查实际 $W\mathcal T=2V'$、(6)、全部模 $576$ 中心、
十六个完整系数、四态核心、群阶 $48$、degree56 到 degree14
的半周期算子及 (34)–(36) 的原输入运输。
全来源归属、绝对锚、独立性、边际整环约消及物理限制已在正文
证明，不靠有限素数扫描。

直接依赖：

- [R493：原六 sigma 因式、实际三阶几何与非零完整网格](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R488：原 A 核、三态 D8 与真实词像格](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)。
- [R494：B56 绝对核心和完整旧 M 深度矩形](R494-original-b56-core-and-complete-m-depth-rectangles.md)。
- [R483：原三曲线完整条件行与参考环带差](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。
- [R426：整个 degree18 的实际核心](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。

