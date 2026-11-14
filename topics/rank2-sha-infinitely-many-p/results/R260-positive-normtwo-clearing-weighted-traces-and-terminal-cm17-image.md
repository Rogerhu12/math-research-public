# R260 — 正权 norm-two 清极、两条加权迹与真实 CM17 终像

日期：2026-11-13。**状态：一个原 degree-136 正权来源、准确 norm-two 迹、基本原 E34 投影、二纤维 primitive 消元，以及随后真实 CM17 的秩一终像均已证明。基本 E34 系数非零不延续成原高次 E34 通道；最后一步的该投影准确为零。**

本篇支付 [R254](R254-octic-ray-original-companions-and-full-fourth-order-transport.md)
之后的一个具体同 degree frame 选择。它与 R259 的相邻权极补偿使用
同一 norm-two 纤维，但取实际的乘 $x$ 正权来源，并把最后必要的
$[\bar\beta]_*[\beta]^*$ 一起算完。

## 1. 同 degree 的 frame 比与一个完整三十五维正权来源

保持 $E_0:y^2=x^3-x$、$dz=dx/(2y)$，置
$$
\alpha=1+i,\quad\beta=4-i,\quad
S_8=-y\vartheta\sigma^3,\quad F=S_8^{17},\quad
G=F^2,\quad H=F(\alpha z),\quad s=x^{-2},\quad U=x^2.
$$
原 CM2 公式是
$$
\sigma(\alpha z)=\alpha\sigma\vartheta,\qquad
\vartheta(\alpha z)=-y\vartheta\sigma/x,
$$
$$
x(\alpha z)=-\frac i2(x-x^{-1}),\qquad
y(\alpha z)=\alpha^{-3}y\frac{x^2+1}{x^2}.
$$
代入 $S_8$，连同 $\vartheta^2=x\sigma^2$，得到
$$
\boxed{
S_8(\alpha z)=(1+x^{-2})S_8(z)^2,
\quad H=\vartheta^{136}(1-s^2)^{17},
\quad G=\vartheta^{136}(1-s)^{17}.}
\tag{1}
$$
所以同 degree-$136$ 的准确 frame 比为
$$
R=H/G=(1+x^{-2})^{17}.
$$
用原微分 $D_zx=2y$ 计算，而不把 $x$ 当作加法参数，得
$$
\frac{R''}{R}=\frac{68(3U^2+62U-69)}{x(U+1)^2}.
\tag{2}
$$
$GR''$ 在 $T_0$ 有真正二阶极点。取实际正权清极来源
$$
\boxed{
M_+=xGR''
=68\vartheta^{136}(1-s)^{17}(1+s)^{15}(3+62s-69s^2).}
\tag{3}
$$
(3) 的多项式次数恰为三十四，所以是原
$\vartheta^{136}\mathbf Q[s]_{\le34}$ 三十五维 $i=1$ 空间中的全纯截面。
在 $x=0$ 处，$s$ 有四阶极，而 $\vartheta^{136}$ 有一百三十六阶零；
最高项准确互相支付。它的质量为 $M_+(0)=204$。

R259 的相邻权补偿源记为
$$
C_{\rm n}=GR''+4692H/x
=544H\frac{x(9U+25)}{(U+1)^2}.
$$
两者准确满足
$$
\boxed{xC_{\rm n}=M_++4692H.}
\tag{4}
$$
这里乘 $x$ 的影响全部可见：它改变 $i$ 特征和原点质量。

## 2. 真实 norm-two deck lift 与两条迹

不能直接把两个标准 Mumford 平移相加。$F$ 的原周期半特征为
$(-1)^{m+n}$，而 $\alpha T_0=i\Omega_0$，所以
$$
\mathcal T_{T_0}^{136}H=-H.
$$
实际拉回线丛 $[\alpha]^*F$ 的 canonical deck lift 因而是
$-\mathcal T_{T_0}^{136}$。对 $Hh$ 的正有限平坦迹准确为
$$
\boxed{[\alpha]_*(Hh)=F\,\operatorname{Tr}(h),\qquad
\operatorname{Tr}(h)=h(x)+h(-1/x),\qquad[\alpha]_*H=2F.}
\tag{5}
$$
这说明下面有理函数的正号和已包含原 Gaussian 与半特征。

令 $w=\alpha z$、$v=x(w)$、$V=v^2$。则
$$
v=-\frac i2(x-x^{-1}),\qquad
V=-\frac{(U-1)^2}{4U}.
$$
由 (2)–(5) 逐项得到
$$
\boxed{[\alpha]_*M_+=F(w)\left(-4488-\frac{4352}{V-1}\right),}
$$
$$
\boxed{[\alpha]_*C_{\rm n}=4352iF(w)\frac{v}{V-1},\qquad
[\alpha]_*(xC_{\rm n})=F(w)\left(4896-\frac{4352}{V-1}\right).}
\tag{6}
$$
最后两式是同一个二次纤维的两条不同实际迹。
它们的标量迹矩阵在 $1,x$ 基中为
$$
\begin{pmatrix}2&2iv\\2iv&2-4V\end{pmatrix},
\qquad\det=4(1-V).
\tag{7}
$$
这个函数域矩阵的可逆性不被解释为 $J$ 对乘 $x$ 的等变性。

令 $\mathcal W=-y\vartheta\sigma^{67}$，
$D=U^8(U-1)^8$、$D_G=U^8(U-1)^7$，故 $F=\mathcal W D$。
第一条迹的原正权多项式为
$$
P_+=-4488D-4352D_G.
\tag{8}
$$
取原 $L=\log((x-1)/(x+1))$、$\nabla_F=\partial-F'/F$，
因为 $L''=-4-8/(U-1)$，有完整协变分解
$$
\boxed{\mathcal W P_+=544\nabla_F^2(FL)-2312F.}
\tag{9}
$$
质量也核对：$544\cdot(-4)-2312=-4488$。
不能删除 (9) 的 $-2312F$ 参考项。

## 3. 基本 degree-68 来源的全部原五块与 E34 系数

用 R248 的实际 $N=\mathscr T_\pi/(2+i)$，以及 R246 的原 $v$ 投影
$\Pi_v=(1+N^4+N^8+N^{12})/4$。在
$S_8(\beta z),S_8(\bar\beta z),A_{136},S_{2312},S_{39304}$
的固定归一中，$\Pi_v(\mathcal W P_+)$ 的准确系数为

| 原来源 | 系数 |
|---|---:|
| $S_8(\beta z)$ | $-77412135/262144-34636021i/524288$ |
| $S_8(\bar\beta z)$ | $-77412135/262144+34636021i/524288$ |
| $A_{136}$ | $1340259855/524288$ |
| $S_{2312}$ | $-559068341/2097152$ |
| $S_{39304}$ | $-560669027/2097152$ |

这五块之外的十二维余项非零，证书保留其全部原多项式。
实际 $\mathcal V$、$Q_{+,v}$ 经由原 $\Pi_v$ 才杀掉它。

令 $E_2$ 为同一个实际 $\lambda^2$ 投影，$\kappa=2^{-1/4}$。
R246 已付出的 $Q_{+,v}S_{2312}(2z)=-640i\kappa B(2z)$ 给出
$$
\boxed{
Q_{+,v}\bigl(E_2[\alpha]_*M_+\bigr)(2z)
=\frac{2795341705i\kappa}{16384}\,B(2z).}
\tag{10}
$$
这是基本来源的一条确切非零原 E34 系数。对应的全 Mellin 式是
$$
J_{272c_0}\left(Q_{+,v}\bigl(E_2[\alpha]_*M_+\bigr)(2z);u\right)
=\frac{2795341705i\kappa}{16384}
\,(2^{p-1})^u J_{68c_0}(B;u).
\tag{11}
$$
算子始终放在 $J$ 的实际输入内；(11) 没有把未知来源的中央零
传过一个有限投影。

同样，(9) 应按 R245/R254 的完整二阶式使用：
$FL/z^2$ 的质量为 $-2$，保留 $W_F=zF'/F$、
$W_{F,0}=W_F-d(68c_0)z^d$，以及 $u-1,u-2$ 的全部项。
这给 $J_{68c_0}(\mathcal W P_+)=544J_{68c_0}(\nabla_F^2FL)-2312J_{68c_0}(F)$。

## 4. 两条真实 primitive 迹可以准确消去非恒定对数

这一计算使用原函数上的乘法，再取完整 Mellin；它不是 $J$ 的乘法公式。
写
$$
c(x)=C_{\rm n}/H=544x(9U+25)/(U+1)^2.
$$
在二次函数域 $x^2-2ivx-1=0$ 中，准确为
$$
\boxed{
c=a(V)+xb(V),\qquad
a=\frac{6800iv}{V-1},\quad b=-\frac{4624}{V-1},\qquad
N(c)=\frac{73984(225V-289)}{(V-1)^2}.}
\tag{12}
$$
若 $\Phi(z+T_0)=-\Phi(z)-2C$，令 $\Psi=\Phi+C$，则 $\Psi$ 为
deck 负型。$\operatorname{Tr}(c\Psi)$、
$\operatorname{Tr}(xc\Psi)$ 的非恒定部分分别是
$2b(x-iv)\Psi$、$2(a+2ivb)(x-iv)\Psi$。
由 (12) 得
$$
\boxed{
17\operatorname{Tr}(xc\Phi)-9iv\operatorname{Tr}(c\Phi)
=-544C\frac{225V-289}{V-1}.}
\tag{13}
$$
这是全部 primitive germ 的等式，非恒定对数确实消去。
左侧第二项含实际乘 $v$；没有将其换成一个可自由提出的 Mellin 标量。

对真正 R253 的 $\Phi_k$，把所有 frame 函数作 $[\beta]$ 拉回，
并利用 $\beta T_0=T_0$，得到同一原高次式
$$
\begin{aligned}
&17[\alpha]_*
 \left(x(\beta z)C_{\rm n}(\beta z)\Phi_k(z)\right)\\
&\quad-9i x(\beta w)[\alpha]_*
 \left(C_{\rm n}(\beta z)\Phi_k(z)\right)\\
&\qquad=-544C_k F(\beta w)
               \frac{225x(\beta w)^2-289}{x(\beta w)^2-1}.
\end{aligned}
\tag{14}
$$
若从实际 $z$ 二阶微分而非已定义的 $C_{\rm n}(\beta z)$ 出发，
两边同乘 $\beta^2$，如 R259 的完整三块式。
两个左端源在原点正则；第二条迹的至少二阶零支付乘 $x(\beta w)$
的极点。其余 $\beta$ 挠点处也由相同的 $C_{\rm n}$ 零点支付。

式 (14) 的右端仍是一个纯 $[\beta]^*$ 来源。下一节计算这一点的
后果，不能停在 (10) 或 (13)。

## 5. 完整 CM17 终像只剩同一个 CM 方向

令
$$
\mathcal C=[\bar\beta]_*[\beta]^*
$$
为 R248/R259 同一原规范的实际对应。
R259 的 theta 群结构证明其像由 $\ker\beta$ 的原 deck 线丛线性化
固定，因此下降到 degree-$4$ 来源，再经 $[\beta]^*$ 拉回。
该 degree-$4$ 空间的完整实际基为
$$
S_8\{1,1/x,x/y,1/y\},
$$
四个 $i$ 特征分别为 $1,-1,i,-i$。
它们全纯、互相独立，度四的 Riemann–Roch 维数给出完整性。
所以每个固定 $i$ 块的像维数至多一；正权块准确落在
$\mathbf Q(i)S_8(\beta z)$。这是源的真实终像，不是一个把未知
中央行删掉的规定。

R259 已用两个完整十七点纤维计算并核定此秩一泛函。本篇把 (8)、
(6) 的加权补偿行和 (14) 的右端原多项式逐项送入同一个泛函，得
$$
\boxed{
\mathcal C(\mathcal W P_+)=c_M S_8(\beta z),\qquad
c_M=-\frac{584661059}{131072}+\frac{2075649i}{262144},}
$$
$$
\boxed{
\mathcal C\!\left(F\left(4896-\frac{4352}{U-1}\right)\right)
=c_XS_8(\beta z),\qquad
c_X=\frac{319380173}{65536}-\frac{59007i}{4096}.}
\tag{15}
$$
对 (14) 中未乘 $C_k$ 的右端，多项式是
$-122400D+34816D_G$，其准确 CM 标量为
$$
c_{\log}=-\frac{3990324677}{32768}+\frac{20529285i}{65536}.
\tag{16}
$$
三个标量都非零，但它们全在同一个 $N=1$ 的 CM 方向。因此
$$
\boxed{E_2\mathcal C(\mathcal W P_+)=0,\qquad
\frac{1-N^4+N^8-N^{12}}4\,\mathcal C(\mathcal W P_+)=0.}
\tag{17}
$$
相同结论适用于 (15) 的第二行和 (16)。
所以 (10) 的基本 E34 系数，在真实 $[\beta]^*$ 和共轭十七迹之后
不构成原高次 E34 行；它准确消失。原四个八次 companion 投影也为零。

## 6. CM 终像的完整单位和中央参考

仍取惰性 $p>19$，排除固定系数的有限坏素位。置
$$
U_{\beta,p}=\beta^{p+1}/17,\qquad q_2=2^{p-1},\quad q_4=4^{p-1}.
$$
令 $J_8$ 为 $S_8$ 自然 degree-$4$ 的完整行，$J_\vartheta$ 为
原 degree-$1$ 行，$J_{F_0}$ 为 $F_0=(x^2-1)\sigma^4$ 的 degree-$4$ 行。
它们均取中心一归一。

由 R246 的负 CM 方向相位，三条全 $u$ 式准确为
$$
J_{272c_0}\bigl((\mathcal C\mathcal W P_+)(2z);u\bigr)
=c_M(q_2U_{\beta,p})^uJ_8(u),
$$
$$
J_{272c_0}\bigl(\mathcal V(\mathcal C\mathcal W P_+)(2z);u\bigr)
=-c_M(q_4U_{\beta,p})^uJ_\vartheta(u),
$$
$$
\boxed{
J_{272c_0}\bigl(Q_{+,v}(\mathcal C\mathcal W P_+)(2z);u\bigr)
=-2\kappa c_M(q_2U_{\beta,p})^uJ_{F_0}(u).}
\tag{18}
$$
求最后一行中央导数时，必须保留
$-2\kappa c_M(\log_pq_2+\log_pU_{\beta,p}+J_{F_0}'(0))$。
不能由参考曲线的秩零删去这三个项。
如果在 norm-two 源端移出 $z\mapsto\alpha z$，同样还须保留
$U_{\alpha,p}^u$；(5)–(18) 都在实际源内先做完整迹，未作这种省略。

本篇支付了一个具体边界：在 $\beta$ 变量中的纯 frame 修正，可以
产生基本非零 E34 系数和完整 primitive 消元，但其真实 CM17 终像仍为
CM 参考。要进入原八次块，需要保留不在 $\beta$ 变量中的实际载体；
例如 $F(\beta z)/x(z)$，它不属于上述纯拉回秩一结论的输入形式。

## 精确证书

- [脚本](../scripts/check-normtwo-positive-clearing-and-original-transport.py)
  与 [输出](../scripts/check-normtwo-positive-clearing-and-original-transport.json)：
  41 项精确检查全部通过，含 (2)–(4)、三个完整有理迹、二纤维坐标和
  primitive 消元、基本原五块、真实 E34 系数、最后秩一泛函及全部零投影。
- R248/R246 固定原 CM5 与 dyadic 规范；R259 固定真 norm-two deck lift
  及完整 conductor-$17$ 秩一泛函；R254 固定所有完整 Mellin 连接和移权。
- 不使用目标素数样本、数值 theta 拟合或中央泛函的未付等变性。
