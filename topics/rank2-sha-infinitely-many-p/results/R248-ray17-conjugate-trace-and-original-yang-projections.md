# R248 — 二挠对数 ray 来源的共轭 CM17 迹、全部有限角色及原 A/B/H 投影

日期：2026-11-13。**状态：本文的固定有理来源、真实共轭迹、十七维 CM5 算子、十六个 torus 投影、原三曲线的有限运输和完整中央缩放均已证明。本文尚不证明三个原完整中央导数非同时为零。**

本篇接续 [二挠除子分布笔记](../notes/2026-11-13-two-torsion-log-distribution-and-primitive-projection.md)。该笔记给出的非零 ray 质量现在有明确的原 Yang 投影；不再只比较角色名称。

具体地，三个固定 ray 来源的共轭 CM17 迹，在原 $E_{136}$ 行上的系数全非零；经 R246 的真实 dyadic 运输，也给出原 $E_{17}$ 和 $E_{34}$ 的准确有限行。全部十二个额外角色保留在同一有限系统中。它们的三列线性独立，所以不能直接用三个来源的常数线性组合删去这些来源。

所有计算只在十七维商环及十七维截面空间内进行。全体来源先作 $[2]$ 拉回，再置于共同 degree-$4624=16\cdot17^2$ 模型；不构造 degree-$4624$ 的稠密矩阵。

## 1. 固定截面、两种十七作用与完整线丛

仍取
$$
E_0:y^2=x^3-x,\qquad dz=\frac{dx}{2y},\qquad U=x^2,
$$
$$
\beta=4-i,\quad\bar\beta=4+i,\qquad
\pi=2+i,\quad\bar\pi=2-i.
$$
使用 R243、R245 的准确规范
$$
S=-y\vartheta\sigma^3,\quad S(0)=1,\qquad
F=S^{17},\qquad W=-y\vartheta\sigma^{67}.
$$
于是
$$
F=W U^8(U-1)^8.                                      \tag{1}
$$
$S$ 的次数是四，其半特征为 twist-$T_0$；$F,W P(U)$ 的次数是六十八。
原新曲线截面写作
$$
H=A_{136}=W P_H(U),\qquad\deg P_H=15,
$$
其中 $P_H$ 是 R243 的首个 $z^4$ 系数为一的多项式。这里 $H$ 始终指原 rank-two 截面，分布笔记中的参考 $H_B=F/(U-1)$ 不改名为 $H$。

固定 $P\in E_0[\beta]\setminus\{0\}$，令 $i$ 在该循环群上为 $4\bmod17$，并置 $\lambda(3)=-i$。对 $k=1,2,3$，写
$$
B_k(z)=\sum_{a\in\mathbf F_{17}^{\times}}
             \lambda(a)^{-k}\frac1{x(z+aP)^2-1},
\qquad b_k=B_k(0),
$$
$$
G_k(z)=F(\beta z)B_k(z).                              \tag{2}
$$
分布笔记已完整证明 $b_k\ne0$，且在 $p>19$ 处均为单位；$G_k$ 是真实全纯 degree-$1156$ 截面。

(2) 中的角色是 $P\mapsto aP$ 的 ray-scalar 作用。本文用真实有限平坦迹和 CM5 矩阵，计算它到原 Schwartz 模型的 compact-torus 作用的变换。

旧 $A/B$ 的 degree-$68$ 线丛与上述 twist-$T_0$ 线丛不同。因此共同模型使用
$$
\widehat G_k(z)=G_k(2z),\quad
A_{17}(4\beta z),\quad B(2\beta z),\quad H(2\beta z),
                                                               \tag{3}
$$
及其共轭 CM 方向。它们的次数均为 $4624$，所有半特征已经付掉。后文先计算十七端的迹，再按 (3) 拉回；这个顺序保留同一 $16\times17^2$ 张量结构。

## 2. 三个 ray 函数实际下降到 $\mathbf Q(i)(U)$

### 2.1 完整四元轨道公式

若 $V=x(P)^2$，直接用椭圆曲线加法公式、$y^2=x^3-x$，得到
$$
\sum_{j=0}^3 B(z+i^jP)=\frac{4\mathcal A(U,V)}{\mathcal D(U,V)^2},
\qquad B(z)=\frac1{x(z)^2-1},                           \tag{4}
$$
其中
$$
\mathcal D(U,V)=(V-1)^2(U^2+1)-2(V^2+6V+1)U,
$$
$$
\begin{aligned}
\mathcal A(U,V)={}&(V-1)^3U^4
 +(V^4+34V^3-20V^2-18V+3)U^3\\
&-(3V^4+20V^3+82V^2+20V+3)U^2\\
&+(3V^4-18V^3-20V^2+34V+1)U-V(V-1)^3.
\end{aligned}
$$
例如先把 $z+P,z-P$ 配对，使用
$$
x(z\pm P)=\frac{(x+x(P))(xx(P)-1)\mp2yy(P)}{(x-x(P))^2},
$$
再把 $P,iP$ 配对，便得到 (4)，没有选取 $y(P)$ 的数值平方根。

非零 $\beta$ 核的四元轨道参数满足 R59 的四次式
$$
K_\beta(V)=(4-i)V^4+(-12+20i)V^3+(28+10i)V^2
                          +(-20-12i)V-i.                \tag{5}
$$
在此商环中，$P\mapsto3P$ 是
$$
g(V)=\frac{(1+4i)V^3-(20+12i)V^2+(-11+28i)V+14-20i}{4}.
                                                               \tag{6}
$$
已经有 $g^4(V)=V$ 及 $K_\beta(g(V))=0$。故 (4) 对四个 $g$ 轨道作 $i^{kj}$ 加权，再除以同角色的 $b_k$，准确落入 $\mathbf Q(i)(U)$。

### 2.2 完整有理分母与分子

令
$$
\begin{aligned}
D_\beta(U)={}&U^8+(-56+80i)U^7+(156-32i)U^6
 +(1144+176i)U^5\\
&+(-2234+576i)U^4+(1144+176i)U^3
 +(156-32i)U^2+(-56+80i)U+1.
\end{aligned}                                               \tag{7}
$$
则三个准确公式是
$$
\boxed{\frac{B_k(z)}{b_k}=\frac{N_k(U)}{D_\beta(U)^2}.}   \tag{8}
$$
为紧凑列出全部系数，令 $d_1=5,d_2=d_3=1$，并写
$d_kN_k(U)=\sum_{j=0}^{16}n_{k,j}U^j$。下表给 $j=0,\ldots,7$；其余准确满足
$$
n_{k,8}=0,\qquad n_{k,16-j}=-n_{k,j}.                    \tag{9}
$$

| $j$ | $n_{1,j}$ | $n_{2,j}$ | $n_{3,j}$ |
|---:|---|---|---|
| 0 | $-5$ | $-1$ | $-1$ |
| 1 | $130+1040i$ | $-390+160i$ | $-150+160i$ |
| 2 | $-4642+16064i$ | $4678-2176i$ | $2950+1664i$ |
| 3 | $16498-69616i$ | $16298-34656i$ | $-52070+16032i$ |
| 4 | $-1219654+791808i$ | $-31246+573952i$ | $168178-240128i$ |
| 5 | $4739242-4618544i$ | $141570-1344480i$ | $-957646+261664i$ |
| 6 | $-7405818+5265856i$ | $-291506+2954624i$ | $2509710+573568i$ |
| 7 | $1632314-1368368i$ | $913746-4379616i$ | $-1641598-669664i$ |

**(8) 的有限证明。** 对 (4) 的分母取 (5) 的 resultant，首一化后准确为 $D_\beta(U)$。因此每个加权有理式乘 $D_\beta^2$ 后是次数至多十六的多项式。(6) 在四次商环内给全部角色值；在 $U=0,\ldots,16$ 的十七个准确有理值决定全部系数，并给出上表。这里的次数界来自全局零极点，所有取值都在 $\mathbf Q(i)[V]/K_\beta$ 内准确计算。

特别每个 $N_k$ 的首项为一，和 $B_k(0)/b_k=1$ 一致；(9) 也准确保留 $B_k(z+T_0)=-B_k(z)$。

## 3. 同向核投影为零，共轭核给非零真实迹

### 3.1 同向 $[\beta]$ 旧空间

令 $e_a(z)=F(\beta z)B(z+aP)$，$a\in\mathbf F_{17}$。在 $[\beta]^*$ 的规范 theta 线性化下，
$$
U_{bP}e_a=e_{a+b}.                                      \tag{10}
$$
这是完整 frame 下的等式：$F(\beta z)$ 是该 pullback 的不变截面，故作用在商上的就是椭圆函数平移。十七个 $B(z+aP)$ 的双极点集合两两不交，因此 $e_a$ 线性独立。

同向旧空间的准确投影是
$$
\mathcal P_\beta=\frac1{17}\sum_{b\in\mathbf F_{17}}U_{bP}.
$$
分布公式给
$$
\mathcal P_\beta e_a
=\frac{-\beta^2 H_B(\beta z)-4\beta F(\beta z)}{17},
\qquad H_B=FB,
$$
所以
$$
\boxed{\mathcal P_\beta G_k=0\quad(k=1,2,3).}             \tag{11}
$$
(11) 在共同 $[2]$ 拉回后仍成立。它准确说明原 $[\beta]$ 拉回行的系数为零；不将它误解为共轭方向也为零。

### 3.2 共轭迹的完整 frame

R245 给出 $C_\beta,C_{\bar\beta}\in\mathbf Z[i][U]$，次数十六，满足
$$
S(\beta z)=W C_\beta(U),\qquad
S(\bar\beta z)=W C_{\bar\beta}(U).
$$
另外由原 sigma 和 theta division 公式，
$$
\sigma(\beta z)=\sigma^{17}K_\beta(U),\quad
\vartheta(\beta z)=\sqrt{x}\sigma^{17}Q_\beta(U),
$$
$$
Q_\beta(U)=U^4+(12-20i)U^3+(-10+28i)U^2
                            +(-20-12i)U+(1+4i).          \tag{12}
$$
准确有 $C_\beta=Q_\beta^2D_\beta$，共轭方向相同；并且
$$
U(\bar\beta z)=\frac{UQ_{\bar\beta}(U)^4}{K_{\bar\beta}(U)^4}.
                                                               \tag{13}
$$
由于 $\beta,\bar\beta$ 的范数相同且模二相同，两次 pullback 的自动因子完全相同。因此可以用 $F(\bar\beta z)$ 的规范 frame 作有限平坦迹，不增加猜测的 Gaussian 或单位相位。

定义 $T_k$ 为归一 $G_k/b_k$ 沿 $[\bar\beta]$ 的真实迹：
$$
T_k(z)=F(z)\operatorname{Tr}_{\bar\beta w=z}
 \left[\frac{F(\beta w)}{F(\bar\beta w)}\frac{B_k(w)}{b_k}\right].
                                                               \tag{14}
$$
它是同一 degree-$68$ twist 截面，且 $i$ 不变。因此
$$
T_k=W\mathcal T_k(U),\qquad\deg\mathcal T_k\le16.         \tag{15}
$$
次数界也可直接检查：$i$ 不变的 twist 截面在 $T_\pm$ 至少有一阶零，在 $T_0$ 至少有二阶零；除以 $W$ 后只能在 $O$ 有阶至多六十四的极点，故为次数至多十六的 $U$ 多项式。

由 (8)、(12)、(13)，全部系数的准确有限公式为
$$
\boxed{
\mathcal T_k(t)=t^8(t-1)^8
\operatorname{Tr}_{\,UQ_{\bar\beta}(U)^4-tK_{\bar\beta}(U)^4=0}
\left[
 \left(\frac{C_\beta(U)}{C_{\bar\beta}(U)}\right)^{17}
 \frac{N_k(U)}{D_\beta(U)^2}
\right].}                                                \tag{16}
$$
这是整个十七次纤维的迹，包含所有分支和重数。若单首一多项式是 $f$，商环中的迹通过
$$
\operatorname{Tr}(R)=[U^{16}]\bigl(Rf'(U)\bmod f(U)\bigr)
                                                               \tag{17}
$$
计算。$t=2,\ldots,18$ 的十七个准确值由已证次数界决定 (16)，脚本另核一个留出值及独立的 $t=\infty$ 纤维。

对应的投影而非全迹是
$$
\boxed{\mathcal P_{\bar\beta}G_k(z)=\frac{b_k}{17}T_k(\bar\beta z).}
                                                               \tag{18}
$$
三个 $T_k$ 的质量分别为
$$
m_1=\frac{335175701-1484437i}{335544320},\quad
m_2=\frac{67389911+221907i}{67108864},\quad
m_3=\frac{67158471+279001i}{67108864}.                    \tag{19}
$$
它们非零，因此共轭迹确实含有质量来源，不能直接等同于 $H$。

## 4. 同一十七维空间上的实际 CM5 算子

在 $\mathcal V=\{WP(U):\deg P\le16\}$ 上取真实
$$
\mathscr M=[\pi]_*[\bar\pi]^*.
$$
令 $\eta=1-2i=-i\pi$，并置
$$
q_\pi(U)=U-\eta,\qquad k_\pi(U)=\pi U-i,
$$
$$
c_\pi(U)=\frac{(U-\eta)^2}{\pi}
 \bigl((U-\eta)(\pi U-i)+4U(\pi\eta-i)\bigr).             \tag{20}
$$
直接对 $x(\pi z)=xq_\pi(U)^2/k_\pi(U)^2$ 求导，得
$$
S(\pi z)=-y\vartheta\sigma^{19}c_\pi(U).
$$
共轭方向的全部多项式为系数共轭，故 (20) 支付实际 theta frame。

若 $t=U(\pi z)$，$v=U(\bar\pi z)$，则在五次商环
$$
Uq_\pi(U)^4-tk_\pi(U)^4=0
$$
内有 $v=Uq_{\bar\pi}(U)^4/k_{\bar\pi}(U)^4$，以及
$$
\boxed{
(\mathscr M P)(t)=t^8(t-1)^8
\operatorname{Tr}\left[
\left(\frac{c_{\bar\pi}(U)}{c_\pi(U)}\right)^{17}
\frac{P(v)}{v^8(v-1)^8}\right].}                         \tag{21}
$$
结果仍在 $\mathcal V$，所以十七个准确值求出完整 $17\times17$ 矩阵。该矩阵在脚本输出中逐列列出，基为 $W,WU,\ldots,WU^{16}$；其整体符号由 (21) 的正有限平坦迹固定。

定义
$$
\mathscr N=\frac{\mathscr M}{2+i}.
$$
准确矩阵恒等式为
$$
\boxed{\mathscr N^{16}=1,\qquad
 \det(X-\mathscr N)=(X-1)(X^{16}-1).}                    \tag{22}
$$
直接在已确定的截面上核得
$$
\mathscr M S(\beta z)=(2+i)S(\beta z),\quad
\mathscr M S(\bar\beta z)=(2+i)S(\bar\beta z),
$$
$$
\mathscr M H=(-1+2i)H=i(2+i)H.                          \tag{23}
$$
R231 的 theta 群等变证明在这里逐字适用：两个范数五 pullback 同线丛，潜在十七挠字符因与 $i$ 交换而为零。在十七端，$\pi/\bar\pi=14=3^9$，原 $\lambda^{-k}$ 行的特征值为 $i^k$。新 dyadic 型上的实际共同标量由 (23) 固定为 $2+i$。因此后文的 $i$ 特征线就是原 $H$，而非重新命名的 ray 行。

## 5. 十六个角色投影和十二个额外来源

取 $\zeta=\zeta_{16}$，$\zeta^4=i$。全部准确投影为
$$
\boxed{\Pi_r=\frac1{16}\sum_{j=0}^{15}\zeta^{-rj}\mathscr N^j,
\qquad r=0,\ldots,15.}                                 \tag{24}
$$
$\Pi_0$ 秩二，其余十五个投影均秩一。$r=4,8,12$ 是原 $\lambda^{-1},\lambda^{-2},\lambda^{-3}$ 型。
其余编号指实际 CM5 算子连同 dyadic 相位的有限特征来源；不把它们自动解释成同一 dyadic 型的椭圆曲线角色。

令 $R_2=S_{2312}$、$R_3=S_{39304}$ 归一为质量一。它们的多项式分别是 (22) 的 $-1,-i$ 特征向量，已与 R246 的真实 dyadic 运输一致。完整系数列在脚本输出中；均为整数。其曲线身份及 Yang 非零来自原向量运输和非零质量，不从代数秩零倒推复 $L$ 值非零。

设
$$
E_k=\left(1-\Pi_0-\Pi_4-\Pi_8-\Pi_{12}\right)T_k.
$$
准确有
$$
\boxed{T_k=d_{k,-}S(\beta z)+d_{k,+}S(\bar\beta z)
       +a_{k,1}H+a_{k,2}R_2+a_{k,3}R_3+E_k.}             \tag{25}
$$
三个原 $H$ 系数为
$$
\boxed{
\begin{pmatrix}a_{1,1}\\a_{2,1}\\a_{3,1}\end{pmatrix}
=\frac1{2^{26}}
\begin{pmatrix}
886234888+2448712079i\\
-3413940145+2467870350i\\
2127156460+228850985i
\end{pmatrix}.}                                         \tag{26}
$$
每个均非零。其他 primitive 系数为

| $k$ | $a_{k,2}$ | $a_{k,3}$ |
|---:|---|---|
| 1 | $(196682749+141344547i)/(5\cdot2^{29})$ | $(73190217+46997426i)/(5\cdot2^{28})$ |
| 2 | $(42836499-34514645i)/2^{29}$ | $(29003206-2170199i)/2^{28}$ |
| 3 | $(-31173405-26833007i)/2^{29}$ | $(12645535-22348574i)/2^{28}$ |

两个 CM 参考的系数为

| $k$ | $d_{k,-}$ | $d_{k,+}$ |
|---:|---|---|
| 1 | $(35513803+84839419i)/(5\cdot2^{30})$ | $(374871479-57215793i)/(5\cdot2^{30})$ |
| 2 | $(9703039+34994109i)/2^{30}$ | $(149679475-3818047i)/2^{30}$ |
| 3 | $(2243349+26174665i)/2^{30}$ | $(106942009+17201269i)/2^{30}$ |

**额外来源的完整登记。** 对每个 $r\notin\{0,4,8,12\}$，(24) 给出 $\Pi_rT_k$ 的准确多项式。输出采用 $\mathbf Q(i)[\zeta]/(\zeta^4-i)$，每个系数列为 $1,\zeta,\zeta^2,\zeta^3$ 的四项。每个秩一来源独立归一，再列出三个 ray 来源的全部系数。因此十二个来源没有被省作未知误差项。

准确计算还给出：这十二型的三十六个投影质量全部非零。因此各额外来源都按 $U^{16}$ 系数一归一；输出同时保存该质量、三个准确投影质量及零/非零值。其余五个来源中，$H$ 的质量为零，两个 CM 参考及 $R_2,R_3$ 的质量为一。这里没有为十二个额外来源赋予未经证明的椭圆曲线算术身份。

合计额外质量为
$$
E_1(0)=\frac{533287446-65256677i}{5\cdot2^{27}},\quad
E_2(0)=\frac{89646280+6260567i}{2^{27}},\quad
E_3(0)=\frac{122139356+13018549i}{2^{27}}.                 \tag{27}
$$
三个额外多项式的系数列秩恰为三。例如取 $U^0,U^1,U^2$ 三行，其行列式为
$$
-\frac{14105746441669257119463780453
       +42908231973469112586496111i}{590295810358705651712}\ne0.
                                                               \tag{28}
$$
故三个 $T_k$ 的常数线性组合若消去全部十二个额外来源，该组合只能为零。这是已算出的有限系统的精确性质；不排除利用完整中央函数的进一步关系。

## 6. 到原 A/B/H 的真实 dyadic 运输

原 $[\beta]$ 方向首先有 (11)。在共轭方向，(18)、(25)、(26) 给出准确的非零 $H$ 系数。共同 $[2]$ 模型中的新来源在 $X^{8}=Z^{8}=-1$ 块；旧 $A/B$ 在不同 dyadic 块，因此未经运输时其直接投影为零。

使用 [R246](R246-third-dyadic-bidirectional-cm17-and-complete-central-bridge.md) 已完整支付 Gaussian、半特征和全部 Haar 相位的 $Q_{\rm norm}=\mathcal V$ 及 $Q_{+,\rm new}$，准确有
$$
Q_{\rm norm}H(2z)=\frac{i}{22}A_{17}(4z),
$$
$$
Q_{+,\rm new}R_2(2z)=-640i\kappa_4 B(2z),
\qquad\kappa_4=2^{-1/4}.                               \tag{29}
$$
于是三类原行的实际有限展开是
$$
\Pi_4T_k(2z)=a_{k,1}H(2z),
$$
$$
Q_{\rm norm}\Pi_4T_k(2z)
      =\frac{i a_{k,1}}{22}A_{17}(4z),
$$
$$
Q_{+,\rm new}\Pi_8T_k(2z)
      =-640i\kappa_4a_{k,2}B(2z).                       \tag{30}
$$
需要恢复未归一来源及高层投影时，再乘 (18) 的 $b_k/17$ 并作真实 $[\bar\beta]$ 拉回。这些都是固定代数非零标量，只有固定有限素位可能为非单位。

(30) 是截面身份；没有由此假设中央泛函与 $Q$ 或 $\mathscr N$ 交换。

## 7. 完整中央函数及所有质量缩放

固定惰性 $p$，$d=p+1$，并使用 R54 的 $c_0$。对 degree-$68$ 截面写
$$
J(V;u)=\mathcal J_{68c_0}(V;u),\qquad
U_{\alpha,p}=\frac{\alpha^d}{N\alpha}.
$$
E8 参考笔记已证明，对本篇的真实 CM pullback，
$$
\mathcal J_{nNc_0}(V(\alpha z);u)
=U_{\alpha,p}^{u}\mathcal J_{Nc_0}(V;u).
$$
因此 (18) 在共同 degree-$4624$ 模型中给
$$
\boxed{
\mathcal J_{4624c_0}((\mathcal P_{\bar\beta}G_k)(2z);u)
=\frac{b_k}{17}\,2^{(p-1)u}U_{\bar\beta,p}^{u}J(T_k;u).}
                                                               \tag{31}
$$
将 (25) 直接放入 $J$ 即为完整中央行，系数不随 $u$ 改变。两个 CM 参考准确为
$$
J(S(\beta z);u)=U_{\beta,p}^{u}J_8(u),\quad
J(S(\bar\beta z);u)=U_{\bar\beta,p}^{u}J_8(u),
\quad J_8(u)=\mathcal J_{4c_0}(S;u),                     \tag{32}
$$
其中 $J_8(0)=1$ 且为解析单位。

例如令 $j(V)=\partial_uJ(V;0)$、$j_8=J_8'(0)$，则 (25) 准确给
$$
\begin{aligned}
j(T_k)={}&a_{k,1}j(H)+a_{k,2}j(R_2)+a_{k,3}j(R_3)+j(E_k)\\
&+(d_{k,-}+d_{k,+})j_8
 +d_{k,-}\log_pU_{\beta,p}+d_{k,+}\log_pU_{\bar\beta,p}.
\end{aligned}                                               \tag{33}
$$
而 (31) 求导后，还准确增加
$$
\frac{b_km_k}{17}
 \bigl((p-1)\log_p2+\log_pU_{\bar\beta,p}\bigr).          \tag{34}
$$
质量 $m_k$ 是 (19)，不能删掉 (34)。

若所有 degree-$68$ 行统一除以 $J_8$，令
$$
\widehat j(V)=j(V)-V(0)j_8,
$$
则同一个未知 $j_8$ 从 (33) 消去，留下
$$
\boxed{
\widehat j(T_k)=a_{k,1}j(H)
+a_{k,2}\widehat j(R_2)+a_{k,3}\widehat j(R_3)+\widehat j(E_k)
+d_{k,-}\log_pU_{\beta,p}+d_{k,+}\log_pU_{\bar\beta,p}.}   \tag{35}
$$
这是已经付完规范的有限中央系统。两个秩零行的归一导数及十二个额外来源仍明确保留；(28) 表明不能仅对三行 (35) 取常数线性组合把额外来源全部删掉。

## 8. 精确证书与下一项具体接口

[脚本](../scripts/check-ray17-conjugate-trace-and-yang-projection.py) 及
[完整输出](../scripts/check-ray17-conjugate-trace-and-yang-projection.json) 包含：

- (8) 的全部分子、分母及四次商环推导；
- (16) 的三个十七项迹多项式及独立质量核对；
- (21) 的完整十七维矩阵、(22)、(23) 的准确等式；
- (24) 的全部角色来源、(25) 的全部系数及十二个额外来源；
- (26)、(28) 的非零证书。

所有等式使用固定 $\mathbf Q(i)$ 或 $\mathbf Q(\zeta_{16})$ 算术。十七个插值点的合法性由全局截面次数界给出；留出点只检查实现，没有代替证明。

接下来的具体有限问题是把 $\Pi_4=16^{-1}\sum_{j=0}^{15}i^{-j}\mathscr N^j$ 逐步运输到完整 Mellin 行，保留每步 norm-five 的 frame 和质量，再在其转置系统中检验新分布关系能否消去 (35) 中的额外导数。本文已支付原始 ray 来源到实际 $A/B/H$ 的有限接口；尚未把该有限接口当成原三中央导数的非零证明。
