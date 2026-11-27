# 原 Tate 三挠曲线族的完整 normal Fourier–Mukai 一阶变分

日期：2026-11-27（Asia/Taipei）。研究会话：Astra-serre-24b8836b-20261126。  
来源：原 [R1061](../results/R1061-actual-genus-two-etale-cover-and-original-three-torsion-Petri-point.md) 的 Miller / relative Cartier 规范、原 [R1095](../results/R1095-original-theta-kernel-dual-Psi-normalization.md) 的完整核与第三类边界，以及 [短旗标续稿](2026-11-27-original-lame-tridiagonal-short-flag-continuation.md) §§7–9 的实际 normal 列。

本篇给出一个真正曲线族的一阶原核公式。它准确恢复已付的 normal 单位，并把整个 normal 变分写成原固定源空间上的算子。它不把 normal 方向等同于 Picard 方向，也不把结果称为原 $e,K_4$ 非同时为零的证明。

## 1. 同一实际曲线族、目标与标架

固定
$$
p=6k-1\ge41,\qquad m=(p-1)/2=3k-1,\qquad
v^2=-108,\quad v^p=-v.
$$
底域记为完美域 $K$，可扩大到其代数闭包。所有 Cartier 都是相对 Cartier，故对底域 $K$ 线性，绝不在下式中擅取常数的 $p$ 次根。

令 $A=K[\epsilon]/(\epsilon^2)$。原保持三挠点的 Tate 族为
$$
E_\epsilon:\quad
V^2=U^3+\frac{\epsilon^2}{4}U^2+\epsilon vU+v^2,
\qquad Q_\epsilon=(0,v).
\tag{N.1}
$$
本篇只读模 $\epsilon^2$，故曲线方程中 $\epsilon^2/4$ 一项为零。
切线 $V=v+\epsilon U/2$ 与曲线在 $Q_\epsilon$ 有三重交点，因而这确实是同一个带三挠点的实际曲线族。

取 $\omega_\epsilon=dU/(2V)$。相对 Frobenius 的目标 $E_\epsilon^{(p)}$ 模 $\epsilon^2$ 是固定曲线 $E_0^{(p)}$；用原 $\mathbf F_p$ 模型将其坐标仍记为 $(U_R,V_R)$。记实际 Verschiebung 为
$$
\mathcal V_\epsilon:E_0^{(p)}\longrightarrow E_\epsilon.
$$
在 $\epsilon=0$ 时，$\mathcal V_0=-F$。原特殊纤维上
$$
D=d/\omega,\qquad D\Psi=\delta,\quad
D\mathcal R=\Psi,\quad
\Psi^2=U^p+2\delta\mathcal R,\qquad
\delta\in\mathbf F_p^\times.
\tag{N.2}
$$
这里 $\Psi,\mathcal R,\delta$ 全部使用 R1061 的原归一。

对一般目标点 $R$，令 $K_\epsilon(T,R)$ 是唯一在源原点首项为 $u^{p-1}$ 的原 Miller 函数，其中 $u=U_T^{-1/2}$ 取原切向分支。其真正除子是
$$
\operatorname{div}_T K_\epsilon
 =(\mathcal V_\epsilon R)-F_\epsilon^*(R)+(p-1)(O).
\tag{N.3}
$$
这由 $\mathcal V_\epsilon$ 是 $F_\epsilon$ 的对偶同源及原点刚化给出。所有等式先在一般 $R$ 上证明，再作为有理恒等式延拓；不在两个零极点相遇前代特殊点。

在特殊纤维，$K_\epsilon|_{\epsilon=0}=K$ 正是 R1061/R1095 的原核。
记
$$
h=h_{-FR}(T)=\frac{V_T-V_R^p}{U_T-U_R^p}.
$$
已经付清的原式是
$$
D_T\log K=h+\Psi_R,\qquad
D_Th+h^2=2U_T+U_R^p.
\tag{N.4}
$$

## 2. 实际 Verschiebung 的完整一阶

Hasse 系数按 $\omega_\epsilon$ 读取 $U^{p-1}$。其一阶系数为
$$
H_\epsilon
=\epsilon\,mv\binom{m-1}{2k-1}(v^2)^{k-1}
=-\epsilon\,\frac{\delta}{6v}.
\tag{N.5}
$$
确实，原
$$
\beta_{\rm Car}
=\binom{m}{2k-1}(v^2)^k=-\delta,
$$
两个二项式的比给出 $H_\epsilon/\epsilon=k\beta_{\rm Car}/v$；
而 $6k=1$ 于 $K$。

完整一阶同源坐标为
$$
\boxed{
\begin{aligned}
\mathcal V_\epsilon^*U
 &=U_R^p+\epsilon\,A_R,\\
A_R&=\frac{U_R^{2p}+V_R^p\Psi_R}{3v},\\
\mathcal V_\epsilon^*V
 &=-V_R^p+\epsilon\,B_R,\\
B_R&=-\frac{U_R^pV_R^p+U_R^{2p}\Psi_R}{2v}.
\end{aligned}}
\tag{N.6}
$$
下面说明这不是只凭形式权给出的候选。

由 $\mathcal V_\epsilon^*\omega_\epsilon=H_\epsilon\omega_R$，
实际一阶必须满足
$$
D_RA_R=\frac{\delta V_R^p}{3v},\qquad
D_RB_R=-\frac{\delta U_R^{2p}}{2v}.
$$
将 (N.6) 代入即得这两式；曲线的一阶约束也准确为
$$
-2V_R^p B_R-3U_R^{2p}A_R-vU_R^p=0.
\tag{N.7}
$$

实际一阶只可能在 $O$ 有极。由同源固定原点，其形式参数的一阶增量从一次项开始；对源 $U$、$V$ 的二阶、三阶极求一阶变化，分别得到极阶上界 $3p-1$、$4p-1$。

(N.6) 同样满足这两个界。用 $u=U^{-1/2}$，
$$
V=-u^{-3}(1+v^2u^6)^{1/2}.
$$
由 $D\Psi=\delta$ 及 $\Psi$ 极阶 $p$，$\Psi$ 唯一的负 Laurent 项是 $u^{-p}$；常数由原奇性为零。所以
$$
\Psi=u^{-p}+O(u).
$$
在 $V^p\Psi+U^{2p}$ 中最高 $u^{-4p}$ 两项准确抵消，余项极阶至多 $3p-1$；
在 $U^{2p}\Psi+U^pV^p$ 中最高 $u^{-5p}$ 两项也准确抵消，余项极阶至多 $4p-1$。

最后证明唯一性。两套满足上述要求的坐标之差记为 $a^p,b^p$，这是因为 $D$ 的函数域核恰为 $K(E)^p$。由 (N.7)，
$$
3U^2a+2Vb=0,
$$
故 $a=2Vg,\ b=-3U^2g$。$U^2,V$ 在仿射曲线上无公共零点，所以 $g$ 在 $O$ 外正则。两个极界给 $a$ 极阶至多 $2$、$b$ 极阶至多 $3$，于是 $g$ 在 $O$ 至少有一次零。全局正则函数只能为常数，因此 $g=0$。这证明 (N.6) 就是实际 Verschiebung 的一阶。

## 3. 原 Miller 核的完整一阶公式

$\dot K$ 表示固定源坐标 $U_T$、固定目标点 $R$ 对 $\epsilon$ 求导后代 $\epsilon=0$。准确公式是
$$
\boxed{\qquad
6v\,\dot K
 =\left[D_T^2-
       \left(\Psi_R+\frac{U_T^2}{V_T}\right)D_T-U_T\right]K.
\qquad}
\tag{N.8}
$$
这里 $U_T^2/V_T$ 必须保留：它支付固定 $U_T$ 的曲线变化在非零二挠点上的极。下述证明完全在原特征 $p$ 的相对曲线族中进行，不把特征零 sigma 的 $p$ 次幂直接约化。

由 (N.4)，右端除以 $K$ 后准确化为
$$
U_T+U_R^p-\frac{U_T^2}{V_T}\Psi_R
 +\left(\Psi_R-\frac{U_T^2}{V_T}\right)h.
\tag{N.9}
$$
比较它除以 $6v$ 与实际 $\dot K/K$ 的全部可能极：

1. **移动简单零点。** 在 $T=-FR$，取 $U_T-U_R^p$ 为局部参数。$h$ 的主部是
   $-2V_R^p/(U_T-U_R^p)$。因此 (N.9) 的主部除以 $6v$ 为
   $-A_R/(U_T-U_R^p)$，正是 (N.6) 规定的实际移动零点增量。

2. **相对 Frobenius 分母。** $E_\epsilon^{(p)}$ 已固定，故 $F_\epsilon^*(R)$ 的局部分母可用固定的 $U_T^p-U_R$。它对 $\epsilon$ 的导数为零。$K$ 在该点的 $p$ 阶极不产生附加 logarithmic pole；(N.9) 在一般的该点也正则。另一分支上普遍存在的分子抵消同样保留，不能先只约化特殊纤维的零点后再微分。

3. **三个 $V_T=0$ 点。** 固定 $U_T$ 时，
   $\dot V_T=vU_T/(2V_T)$。局部写 $K=A(U_T)+V_TB(U_T)$，允许一个在本点可逆的固定分母。实际 $\dot K$ 的极项是
   $vU_TB/(2V_T)$。在 (N.8) 中，
   $D_TK=3U_T^2B$ 于 $V_T=0$，故极项是
   $-U_T^4B/(2vV_T)=vU_TB/(2V_T)$，因为该点 $U_T^3=-v^2$。两者准确相同。

4. **原点。** 两边除以 $K$ 在 $O$ 正则。实际 $\dot K/K$ 的常数为零，来自首项 $u^{p-1}$ 的系数恒为一。对于 (N.9)，
   $U_T=u^{-2}$、
   $U_T^2/V_T=-u^{-1}+O(u^5)$、
   $h=-u^{-1}-U_R^p u+O(u^2)$，
   负项和常数全部抵消，其常数同样为零。

两者之差没有任何极，所以是全局常数；原点常数固定其为零。这给出 (N.8) 的真正全部归一。上述比较在一般 $R$ 上完成，故最后可按有理延拓消费原三挠点及其 jets。

## 4. 相对 Cartier 及完整 normal 算子

固定一个 $U$ 多项式 $f$，$\deg_U f\le m$。对一般 $R$ 定义
$$
C_{\mathrm{rel},\epsilon}
 (fK_\epsilon\omega_\epsilon)
 =t_f^\epsilon(R)\,\omega_Z'.
\tag{N.10}
$$
输入除 $F_\epsilon^{-1}R$ 外无极，Cartier 后至多一个简单极；总留数为零，所以输出全纯，(N.10) 确为一维相对全纯微分的真实标量。$\epsilon=0$ 时 $t_f^0=\Phi f$。

目标曲线及其 $\omega_Z'$ 已固定。在相对坐标 $U_T$ 下，Cartier 与底方向的一阶微分交换；此处它对 $\epsilon$、$v$ 均线性。另一方面
$$
\frac{\dot\omega}{\omega}=-\frac{vU}{2V^2}.
$$
将 (N.8) 连同这个微分标架项一起代入 (N.10)，用 $C_{\rm rel}(Dg\,\omega)=0$ 两次分部积分，得
$$
\boxed{\qquad
6v\,\dot t_f
 =C_{\rm rel}\left(
 \left[D^2f+\left(\Psi_R+\frac{U^2}{V}\right)Df\right]
 K\omega\right)/\omega_Z'.
\qquad}
\tag{N.11}
$$
完整的零阶抵消是
$$
D(U^2/V)=4U-3U^4/V^2
        =U+3v^2U/V^2.
$$
它同时消掉 (N.8) 的 $-Uf$ 和 $6v\,\dot\omega/\omega$ 的
$-3v^2Uf/V^2$。不能省略其中任何一项。

再消费 R1061 的完整原 Lamé 身份
$$
C_{\rm rel}\big((D^2f+2\Psi_R Df-2Uf)K\omega\big)/\omega_Z'
 =-2\delta\mathcal R_R\,\Phi f(R).
$$
定义真正的源算子
$$
\mathcal N
=2(U^3+v^2)\partial_U^2+5U^2\partial_U+U.
$$
则 (N.11) 等价于
$$
\boxed{\qquad
6v\,\dot t_f
=\Phi(\mathcal N f)-\delta\mathcal R\,\Phi f.
\qquad}
\tag{N.12}
$$
对单项式，
$$
\mathcal N U^j
 =(2j+1)(j+1)U^{j+1}
   +2j(j-1)v^2U^{j-2}.
$$
当 $j=m$ 时，最高系数因 $2m+1=p$ 恰为零。因此 $\mathcal N$ 真实保持 $\operatorname{span}(1,U,\ldots,U^m)$；(N.12) 中两个 $\Phi$ 都只使用已付的原 $V_0$ 输入，不需假设越界 $\Phi$。以 $f=1$ 核规范，右边是 $\Phi U-\delta\mathcal R=0$，恰给原 $t_1^\epsilon=1$ 的一阶。

必须保留一个标架范围：$t_f^\epsilon$ 是按实际 Miller / $M_0$ 规范取的**比值函数**。Verschiebung 核在 normal 方向移动，不能据特殊纤维的 $L((p-1)O)$ 断言其一阶仍在同一个固定极界空间。式 (N.12) 的 $\mathcal R\,\Phi f$ 可以有至 $2p-2$ 的极；这是真正的移动标架项，不得删除或冒成不变的低阶 Picard 微分算子。

## 5. 原指定源与已付 normal 单位

现在只取原 $f=U^m$。准确有
$$
Df=-U^{m-1}V,\qquad D^2f=3v^2U^{m-2},
\qquad \mathcal Nf=\frac{3v^2}{2}U^{m-2}.
$$
所以整个目标参数上的真实式为
$$
\boxed{\qquad
6v\,\dot t_{U^m}
=-\delta\mathcal R\,\Phi(U^m)
 +\frac{3v^2}{2}\Phi(U^{m-2}).
\qquad}
\tag{N.13}
$$
这是先保全第三类和所有极项，再用完整 Lamé 身份化简的结果。

在目标 $R=FQ=-Q$，$\mathcal R(-Q)=0$，且原
$K(T,-Q)=g_Q(T)$。由同一完整 Lamé 身份，
$$
3v^2\Phi(U^{m-2})(-Q)
 =2C_{\rm rel}(U^{m+1}g_Q\omega)/\omega'.
$$
原 $F_Q=U^m g_Q$，故
$$
\dot t_{U^m}(-Q)
=\frac1{6v}\,C_{\rm rel}(UF_Q\omega)/\omega'
=\frac{(2v)^{2k}}{6v}\binom{3k-1}{2k}
\in K^\times.
\tag{N.14}
$$
最后一个值直接消费短旗标续稿 §7 / §9 的同一原 normal 列；$2k\le3k-1<p$ 付清其单位性，没有执行新数值窗口。

(N.13) 并未将 $\Phi(U^{m-2})$ 变成 $\Phi(U^m)$ 在 $-Q$ 的第四 Picard jet。原
$e=D_R\Phi(U^m)(-Q)$、$K_4$ 及 $J_4$ 的全部三项 carry 仍按原定义保留。后继若用本式排 $e=K_4=0$，须另外证明这个具体 normal 算子与两指定 Picard 读数的真实关系。本文没有用特征零 heat、抽象秩二系统或一般 theta 非退化性代替该关系。

全文为纸面证明；root/o1/o2独立逐式核查实际同源唯一性、全部核极项、相对Cartier标架与有限源边界；没有本地数学程序执行。


## 6. 实际 $M_0$ 截面的移动除子与完整目标标架

本节把 (N.12) 的高极修正识别为实际 FM 截面标架的变化；固定的目标曲线仍是 $E_0^{(p)}$。令
$$
c=\frac{\delta}{6v},\qquad N'=\mathcal O_{E_0^{(p)}}(O),
$$
并令 $s$ 是 $N'$ 的原规范截面，$\operatorname{div}(s)=O$。以下公式中的 $U,V,\Psi,\mathcal R$ 都在目标变量 $R$ 上读取。

### 6.1 实际 Verschiebung 核的全局截面

定义三个真实线丛截面
$$
\begin{aligned}
S_\epsilon&=s^p(1+\epsilon c\mathcal R),\\
X_\epsilon&=s^{2p}(U^p+\epsilon A^\sharp),\\
Y_\epsilon&=s^{3p}(-V^p+\epsilon B^\sharp),\\
A^\sharp&=A+2cU^p\mathcal R,\\
B^\sharp&=B-3cV^p\mathcal R,
\end{aligned}
\tag{N.15}
$$
其中 $A,B$ 就是 (N.6)，没有另选同源或核相位。

先付清这些式子的整性。原 $\mathcal R$ 的极阶为 $p-1$，所以 $S_\epsilon$ 是 $N'^p$ 的全局截面，并且仍沿 $O$ 消失。原 R1061/R1095 的完整式
$$
6\Phi(V)=2V^p+3U^p\Psi-\Psi^3
$$
和 $\Psi^2=U^p+2\delta\mathcal R$ 给
$$
A^\sharp
=\frac{4\delta^2\mathcal R^2+6\Psi\Phi(V)}{6v}.
\tag{N.16}
$$
由于 $\operatorname{pole}_O\Phi(V)\le p-2$，右边极阶至多 $2p-2$。故 $X_\epsilon$ 是 $N'^{2p}$ 的全局截面，而不是有未付清高极的形式表达式。

将 (N.7) 与 (N.15) 合并，准确得到
$$
-2V^pB^\sharp
=3U^{2p}A^\sharp+vU^p+6cv^2\mathcal R.
\tag{N.17}
$$
$B^\sharp$ 是仿射坐标环中的函数；(N.17) 在 $O$ 又给极阶至多 $3p-2$。因此 $Y_\epsilon$ 同样是 $N'^{3p}$ 的真实全局截面。不能只用 (N.17) 除以 $V^p$ 后忽略二挠点；仿射正则性来自 (N.15) 本身。

三个截面满足原加权 Weierstrass 方程
$$
Y_\epsilon^2
=X_\epsilon^3+\epsilon vX_\epsilon S_\epsilon^4
+v^2S_\epsilon^6\pmod{\epsilon^2}.
$$
它们没有共同零点：特殊纤维上 $O$ 外 $S_0$ 非零，在 $O$ 则 $X_0,Y_0$ 的首值非零；由 Nakayama 引理，同一结论对 $A$ 成立。其仿射坐标比为
$$
\frac{X_\epsilon}{S_\epsilon^2}
=U^p+\epsilon A,\qquad
\frac{Y_\epsilon}{S_\epsilon^3}
=-V^p+\epsilon B.
$$
由 §2 已证明的实际同源唯一性，这个全局映射就是 $\mathcal V_\epsilon$。所以
$$
\boxed{\operatorname{div}(S_\epsilon)=\mathcal V_\epsilon^*(O).}
\tag{N.18}
$$
这里的除子包含真实的无穷小核重数。局部地，
$S_\epsilon=u^p+\epsilon cu+\cdots$；这与
$\mathcal V_\epsilon^*u=-u^p-\epsilon cu+\cdots$ 的同一零除子相符，不能将它缩成特殊纤维的 $pO$。

### 6.2 原 $f=1$ FM 截面的准确除子

沿原规范 Poincaré 变换，R1061 §16 的两条变换线在本相对族中仍由 degree-one twist 的 $H^1=0$ 给出。记其 Hom 线为 $\mathcal M_\epsilon$。同源相容和 $\widehat N\simeq N^{-1}$ 给
$$
\mathcal M_\epsilon
\simeq\mathcal V_\epsilon^*\mathcal O_{E_\epsilon}(O)\otimes N'^{-1},
\qquad \deg\mathcal M_\epsilon=p-1.
\tag{N.19}
$$
设 $s_f^\epsilon$ 是实际 Cartier 映射
$C_{\rm rel,\epsilon}\circ f$ 的 FM 截面；原比值正是
$t_f^\epsilon=s_f^\epsilon/s_1^\epsilon$。

实际 $s_1^\epsilon$ 的除子为
$$
\operatorname{div}(s_1^\epsilon)
=\mathcal V_\epsilon^*(O)-(O).
\tag{N.20}
$$
以下说明该等式在无穷小族中也有来源。把 (N.1) 先放回
$K[[\epsilon]]$ 上的完整 Tate 族。由 (N.5)，一般纤维 ordinary，
$\mathcal V$ 的非零核点有 $p-1$ 个。对任一这样的目标点 $R$，
原源生成截面的 Miller 表达式在 $O$ 的零阶从 $p-1$ 增至 $p$。
其 Cartier 输出仍全纯，但原 $u^{p-1}du$ 系数为零，所以
$s_1(R)=0$。这给出 $p-1$ 个不同零点；(N.19) 的度数使它们恰为整个零除子。
特殊纤维的 $s_1$ 是 R1061 已付的非零截面，故闭包中没有额外的整条特殊纤维因子。于是除子等式在整个族、特别在模 $\epsilon^2$ 中成立。这一步没有用普通纤维的集合核代替特殊纤维的非约化核。

(N.18)–(N.20) 现在给出
$\mathcal M_\epsilon\simeq N'^{p-1}$。为完全固定这一个同构的底域单位，
在实际固定三挠点 $R=-Q$ 的纤维上作刚化：将 $s_1^\epsilon(-Q)$
送到 $s^{p-1}(-Q)$。这是合法且唯一的，因为该点不在
$\mathcal V_\epsilon^*(O)$，原 Miller 首项给 $t_1^\epsilon=1$。
又 $\mathcal R(-Q)=0$，所以在这个明确的刚化下
$$
\boxed{
s_1^\epsilon
=s^{p-1}(1+\epsilon c\mathcal R).}
\tag{N.21}
$$
本节不是假设先前任意的原点标架自动具有这个常数；它明确使用同一实际 $-Q$ 纤维来固定比较。

因此，将真实截面以固定目标线 $N'^{p-1}$ 表示，其有理函数为
$$
\widehat t_f^\epsilon
=(1+\epsilon c\mathcal R)t_f^\epsilon.
$$
对 §4 的偶源，由 (N.12) 准确得到
$$
\boxed{
\widehat t_f^\epsilon
=\Phi f+\frac{\epsilon}{6v}\Phi(\mathcal Nf).}
\tag{N.22}
$$
两边现在都是固定 $L((p-1)O)$ 中的真实截面；被消掉的
$\mathcal R\Phi f$ 是 (N.21) 已付的移动标架项，而非被忽略的高极余项。

## 7. 完整 $J$ 的 normal heat 及全源矩阵

### 7.1 同一个原 $J$ 核的实际变分

令
$$
J_\epsilon(T,R)=(U_T^p-U_R)K_\epsilon(T,R),\qquad
\widehat J_\epsilon=(1+\epsilon c\mathcal R_R)J_\epsilon.
$$
这里 $U_T^p-U_R$ 是固定的相对 Frobenius 分母；固定 $U_T$ 求 normal 导数时它不变。它同时消掉原核在 $F_\epsilon^{-1}R$ 的全部 $p$ 阶极。目标端的修正恰是刚在 (N.21) 付清的同一实际标架。

由 (N.8)，再用完整的原双变量 Lamé 式
$$
(D_T^2-2\Psi_RD_T-2U_T+2\delta\mathcal R_R)J=0,
$$
得到
$$
\boxed{
12v\,\left.\partial_\epsilon\widehat J_\epsilon\right|_0
=\left(D_T^2-\frac{2U_T^2}{V_T}D_T\right)J.}
\tag{N.23}
$$
准确代数是：先在 (N.8) 加上 $\delta\mathcal R_RJ$，
再把 $\Psi_RD_TJ+U_TJ-\delta\mathcal R_RJ$ 换成
$D_T^2J/2$。因此没有残留未定的底域标量，也没有删去原
$\mathcal R$ 项后才认作 heat。

$1/V_T$ 一项仍须保留：它记录固定 $U_T$ 而移动曲线时的坐标变化。
(N.23) 是源曲线变形、目标曲线固定的实际公式，
不是目标变量 $R$ 上的二阶或四阶 Picard 微分方程。

### 7.2 自然奇源与整个 $V_0$ 的有限算子

§4 先取了不随族变化的 $U$ 多项式。完整原源空间还包括
$$
f_\epsilon=V_\epsilon U^j,\qquad 0\le j\le m-2.
$$
这时固定 $U$ 有
$$
\dot f=\frac{vU^{j+1}}{2V}.
$$
因此 (N.11) 的右边必须另加
$C_{\rm rel}(6v\dot f\,K\omega)/\omega'$。先保留这一项，再使用原完整 Lamé，
所得源函数为
$$
\frac12D^2f+\frac{U^2}{V}Df+Uf+6v\dot f.
$$
所有表面的 $1/V$ 极准确相消；逐项得到
$$
\boxed{
\mathcal N_{\rm full}(VU^j)
=(2j+5)(j+2)VU^{j+1}
+2j(j-1)v^2VU^{j-2}.}
\tag{N.24}
$$
在偶源上 $\mathcal N_{\rm full}$ 就是 §4 的 $\mathcal N$。
当 $j=m-2$ 时，$2j+5=p$，故最高外溢项为零。
于是它真正保持整个
$$
V_0=
\operatorname{span}(1,U,\ldots,U^m)
\oplus V\,\operatorname{span}(1,U,\ldots,U^{m-2}).
$$
对这个自然相对单项式标架，完整结论为
$$
\boxed{
6v\,\dot t_f
=\Phi(\mathcal N_{\rm full}f)-\delta\mathcal R\,\Phi f,\qquad
6v\,\dot{\widehat t}_f=\Phi(\mathcal N_{\rm full}f).}
\tag{N.25}
$$
若改用随模参数变化的纯极基 $q_r^\epsilon$，还必须加入其自身的系数变分；
不能把 (N.24) 的单项式矩阵直接当作该移动基的矩阵。

(N.21)–(N.25) 给出实际 normal 标架和完整有限源，不预设
$\Phi\mathcal N_{\rm full}\Phi^{-1}$ 是某个低阶目标微分算子。
尤其原 $e$ 和 $K_4$ 的 Picard jets 仍须按原 $J_1,J_4$ 的全部 carry 比较。
本次新增各式由o1_theta给出，root逐式核全局截面极界、实际核除子、普通族闭包、−Q刚化、完整heat及奇源边界；均为纸面推导，没有执行数学程序或新的素数窗口。


## 8. 实际三挠平移的 normal 输运与最高偶边界

本节保持 (N.21) 的同一个目标刚化，使用完整
$H_\epsilon=H^0(E_\epsilon,\mathcal O((p+1)O))$。
它给的是实际三平移矩阵随原 Tate 族的变分，未声称
$S\Phi=\Phi S$。

### 8.1 全曲面 divisor 与三挠相位

写
$$
l_+=V-v-\epsilon U/2,\qquad
l_-=V+v+\epsilon U/2,\qquad l_+l_-=U^3.
$$
把曲线写成 $l_+^2+(\epsilon U+2v)l_+=U^3$，
在 $(U,l_+)$ 坐标中用通过 $Q=(0,0)$ 的直线取第三交点，准确得到
$$
U(T+Q)=-\frac{2vU}{l_-},\qquad
l_+(T+Q)=-\frac{4v^2}{l_-},\qquad
l_-(T+Q)=\frac{2v l_+}{l_-}.
\tag{N.26}
$$
这些是完整 Tate 族的有理恒等式，不只在特殊纤维成立。
再平移一次给 $l_-(T-Q)=-4v^2/l_+$，所以
$$
\prod_{i=0}^2 l_-(T+iQ)=-8v^3.
$$

定义真正的线丛平移作用
$$
S_\epsilon f(T)=l_-(T)^{2k}f(T+Q),\qquad
\gamma=(2v)^{2k}\in\mathbf F_p^\times.
$$
因为 $\operatorname{div}(l_-)=3(-Q)-3O$，
且 $6k=p+1$，$S_\epsilon$ 保持整个 $H_\epsilon$。
(N.26) 给
$$
S_\epsilon^3=(-8v^3)^{2k}=\gamma^3=-4v^2.
\tag{N.27}
$$
特别地，三次方相位没有一阶 normal 修正。

还须保留核在整个乘积曲面上的 divisor。
原 $K_\epsilon$ 的源首项归一以及 (N.20) 给
$$
\operatorname{div}(K_\epsilon)
=\Gamma_{T=\mathcal V_\epsilon R}
 -\Gamma_{R=F_\epsilon T}
 +(p-1)(O\times E)
 -E\times(\mathcal V_\epsilon^*O-O).
$$
非 vertical 部分是 (N.3)；目标端的 vertical 部分正是
原 $s_1$ 的零除子，源 $O$ 首项恒一排掉额外底函数。
这里的 graph 与核除子均取 scheme 重数。
另一方面
$$
\operatorname{div}(U_T^p-U_R)
=\Gamma_{R=F_\epsilon T}+\Gamma_{R=-F_\epsilon T}
 -2p(O\times E)-2(E\times O).
$$
用 (N.18)、(N.21) 的真实修正，得到
$$
\boxed{
\operatorname{div}(\widehat J_\epsilon)
=\Gamma_{T=\mathcal V_\epsilon R}
 +\Gamma_{R=-F_\epsilon T}
 -(p+1)(O\times E+E\times O).}
\tag{N.28}
$$
因此 $\widehat J_\epsilon$ 真是
$\mathcal O((p+1)O)\boxtimes N'^{p+1}$ 的截面；
不是只在每条一般纤维上认同除子后留下未定目标函数。

目标三挠点仍记为 $Q=(0,v)$。
由于 $F_\epsilon Q=-Q$、$\mathcal V_\epsilon Q=Q$，
(N.28) 的两个 graph 都在
$(T,R)\mapsto(T+Q,R+Q)$ 下不变。
源用 $S_\epsilon$，固定目标用 $S_0$，所以两截面之比是底环单位
$C_\epsilon$。特殊纤维由 R1095 的原相位给 $C_0=\gamma^2$。
两端分别施三次平移，(N.27) 迫 $C_\epsilon^3=\gamma^6$；
因 $3$ 可逆，$C_\epsilon$ 的一阶项必为零。因此
$$
\boxed{
(S_\epsilon\otimes S_0)\widehat J_\epsilon
=\gamma^2\widehat J_\epsilon.}
\tag{N.29}
$$
这里先付清全局 divisor，再用真实三次方消掉底域单位，
没有由“相同 theta type”直接删相位。

### 8.2 完整 $H$ 上的有限 normal 连接

在 $H_\epsilon$ 中使用自然相对单项式基
$$
1,U,\ldots,U^{m+1},\qquad
V_\epsilon,V_\epsilon U,\ldots,V_\epsilon U^{m-1}.
$$
“系数 normal 导数”以下专指相对于这个基求导。
(N.23) 是固定 $U$ 的函数导数，两者在奇基上相差
$\dot{(V_\epsilon U^j)}=vU^{j+1}/(2V)$，这项必须先扣除。

定义 $H=H_0$ 上的算子
$$
\begin{aligned}
\mathcal P(U^j)
 &=j(2j-1)U^{j+1}
   +2j(j-1)v^2U^{j-2},\\
\mathcal P(VU^j)
 &=(2j+3)(j+1)VU^{j+1}
   +2j(j-1)v^2VU^{j-2}.
\end{aligned}
\tag{N.30}
$$
低端因子为零的项按零读取。
偶源由 $(D^2-2U^2D/V)/2$ 直接给第一式。
对奇源，准确有
$$
(D^2-2U^2D/V)(VU^j)
=2\mathcal P(VU^j)+\frac{6v^2U^{j+1}}{V};
$$
最后一项恰为 $12v$ 倍自然奇基的一阶变化。
故 (N.23) 在这个完整有限基中为
$$
6v\,\dot{\widehat J}_{\rm coeff}=\mathcal P_TJ.
\tag{N.31}
$$

这里两个最高边界都已付清：
偶端 $j=m+1$ 有 $2j-1=p$，奇端 $j=m-1$ 有 $2j+3=p$。
因此 $\mathcal P$ 保持整个 $p+1$ 维 $H$，
不是先丢掉 $U^{m+1}$ 或 $\Psi$ 后的压缩矩阵。

对 (N.29) 在上述基中求导，并代入 (N.31)，得到
$$
\bigl((6v\dot S+S\mathcal P-\mathcal P S)\otimes S\bigr)J=0.
$$
原 R1095 已证明 $J^\#:H^*\to H$ 是同构，而 $S$ 可逆，故
$$
\boxed{6v\,\dot S=\mathcal P S-S\mathcal P.}
\tag{N.32}
$$
这是同一实际三挠作用的 normal 输运公式，保全部最高边界。
它不把 $\dot S$ 设成零，也不将特殊纤维上的 $S$ 当作与原 $\Phi$ 交换。

### 8.3 与原指定源的准确比较

(N.24) 与 (N.30) 逐项给出
$$
\boxed{\mathcal N_{\rm full}+\mathcal P=D^2+U
\quad\text{于原 }V_0.}
\tag{N.33}
$$
等式把 $V_0$ 视为 $H$ 的子空间；右边可以包含最高偶方向。
特别地，原 $f=U^m$ 满足
$$
\mathcal P f
=U^{m+1}+\frac{3v^2}{2}U^{m-2}
=\mathcal Nf+h^*,\qquad h^*=U^{m+1}.
\tag{N.34}
$$
所以两个实际 normal 算子的差在原指定源上，恰含此前必须保留的
最高偶边界 $h^*$。

还可以不经矩阵推导，直接核原源的平移：
$$
S_\epsilon(U^m)=C U^2\,l_+^n,\qquad
C=(-2v)^m,\quad n=k-1.
$$
这里必须先按自然基约化所有 $V_\epsilon^2$，不能只微分
$l_+$ 中显式出现的 $\epsilon$。令 $W=U^3+v^2$，取唯一偶奇分解
$$
(V-v)^n=E_n(W)+V O_n(W),\qquad E_n,O_n\in K[W].
$$
在实际族中
$(V_\epsilon-v)^n=E_n(W+\epsilon vU)+V_\epsilon O_n(W+\epsilon vU)$。
所以相对于自然单项式基，准确有
$$
\boxed{
\begin{aligned}
\dot S(U^m)
 &= C U^3\left\{
 v\bigl(E_n'(W)+V O_n'(W)\bigr)
 -\frac n2(V-v)^{n-1}\right\}\\
 &=\frac{C U^3}{2V}
 \left\{-n(V-v)^n-vO_n(W)\right\}.
\end{aligned}}
\tag{N.35}
$$
第一行直接表明它是全局多项式。第二行来自
$n(V-v)^{n-1}=2V(E_n'+V O_n')+O_n$，其分子被 $V$ 整除；
没有二挠点附加极。例如 $n=2$ 时，它准确为
$C U^3(2v-V)$，而只微分显式 $\epsilon$ 会错误地少掉 $CvU^3$。

这正是先求固定 $U$ 的函数导数，再扣除自然奇基导数所得的同一向量。
因此 (N.35) 与 (N.32) 具有完全相同的曲线约化和标架约定。

(N.32)–(N.35) 尚未把
$\Phi(U^{m-2})(-Q)$ 的已知 normal 单位改成原 $K_4$ 单位。
使用后继时，$h^*$ 的完整第三类项和 $J_4$ 的所有 carry 仍须保留。
本节是原 finite theta 矩阵的纸面推导，没有新的数学执行。

本节经root/o1/o2逐式复核；root在发布前指出并纠正了自然奇基约化的遗漏，完整(N.35)采用已核修正版。


## 9. 整个原 $V_0$ 上不存在低阶目标 Picard 共轭

下面排除一个具体的错误期待：把 (N.25) 的完整有限矩阵
$\Phi\mathcal N_{\rm full}\Phi^{-1}$ 写成固定目标曲线上、
保持整个 $V_0$ 的四阶以下微分算子。结论不排除只针对
$f=U^m$ 在 $-Q$ 的一个读数身份；该指定问题仍须继续。

### 9.1 低阶亚纯算子保全部截面时必为标量

仍令
$$
L=\mathcal O_E((p-1)O),\qquad n=p-1,\qquad
V_0=H^0(E,L),
$$
基域取代数闭包，$D=d/\omega$ 是处处不为零的原不变向量场。
考虑一个 $K$-线性的亚纯微分算子
$$
\mathcal A=\sum_{i=0}^r a_iD^i,\qquad
a_i\in K(E),\quad 0\le r\le p-3,
$$
并假设它作为有理函数的算子满足
$\mathcal A(V_0)\subseteq V_0$。
这里是通常阶数小于 $p$ 的微分算子，没有加入 Frobenius、
系数半线性操作或随源变化的额外向量。

**首先，该算子其实是 $L$ 的全局正则微分算子。**
任一点 $P$ 的 $r$-jet 读取都有满射
$$
H^0(E,L)\longrightarrow L\otimes\mathcal O_E/\mathfrak m_P^{r+1}.
\tag{N.36}
$$
因为其余项 $H^1(E,L(-(r+1)P))$ 为零：
该线丛的度数是 $p-r-2\ge1$，由椭圆曲线的 Serre 对偶立即得零。
在 $P$ 选 $r+1$ 个全局截面，其局部 $D$-jet 矩阵可逆；
$r<p$ 保证各阶通常导数与 Taylor 读数之间的阶乘都是单位。
由假设，每个输出仍为 $L$ 的正则截面。用此单位矩阵解各局部
算子系数，得到它们在 $P$ 全部正则。$P$ 任意，故
$\mathcal A\in H^0(E,\operatorname{Diff}^r(L,L))$。

**再证明这种全局算子只有标量。**
设实际阶数 $r\ge1$。最高系数 $a_r$ 在换线丛标架时不变，
是全局正则函数，所以为常数。在 $O$ 外使用有理标架 $1$；
在 $O$ 使用正则标架 $u^{-n}$，其中 $u$ 是局部参数。
局部算子为
$$
u^n\mathcal A u^{-n};
$$
它的 $D^{r-1}$ 系数准确为
$$
a_{r-1}-rn\,a_r\,\frac{Du}{u}.
\tag{N.37}
$$
此系数在 $O$ 正则，而 $a_{r-1}$ 在 $O$ 外也正则。
因此微分 $a_{r-1}\omega$ 只有 $O$ 一处可能的简单极，
且其留数为 $rn a_r$，因为 $(Du)\omega=du$。
全局留数定理迫 $rn a_r=0$。但
$1\le r<p$ 且 $n=p-1$ 均与 $p$ 互素，所以 $a_r=0$，
与其为最高非零系数矛盾。逐阶递降，最终只剩全局常数乘法。

上述第二步也独立证明：
对任何 $0\le r<p$，全局
$H^0(E,\operatorname{Diff}^r(L,L))$ 只有标量。
第一步中较小的 $r\le p-3$ 范围，用于从“保全部全局截面”
严格推出“全局微分算子”，没有忽略可能的亚纯系数。

### 9.2 应用于实际 normal 矩阵

$\Phi:V_0\to V_0$ 是原相对、$K$-线性的可逆变换，
且 $\Phi(1)=1$。已付的实际式给
$$
\mathcal N_{\rm full}(1)=U,\qquad
\bigl(\Phi\mathcal N_{\rm full}\Phi^{-1}\bigr)(1)
=\Phi(U)=\delta\mathcal R.
$$
最后一项非恒定，故这个真正的有限矩阵不是标量。由 §9.1，
$$
\boxed{
\Phi\mathcal N_{\rm full}\Phi^{-1}
\text{ 不能在整个 }V_0\text{ 上由阶数 }\le p-3
\text{ 的亚纯目标微分算子表示。}}
\tag{N.38}
$$
特别地，$p>37$ 时不存在完整二阶或四阶目标 Picard 表示。

这与 (N.23) 不矛盾：该式包括源曲线的实际变化，
并非固定目标线丛上的微分算子。
$\mathcal N_{\rm full}$、$\mathcal P$ 也是对自然相对基取系数导数后的
有限矩阵；奇源的曲线变化是其中的必要部分。
只看偶多项式上的二阶表达式，不能删掉奇源补偿后把它当作
整个 $V_0$ 上的全局二阶算子。

本节只结清上述全空间低阶共轭方案。
原 $f=U^m$、$R=-Q$ 的具体配对，含移动源、第三类边界或特定
消失条件的关系，仍不受 (N.38) 排除。
全文由root给出，o1/o2分别独立核查jet生成、局部换帧、
单点留数及适用边界；无数学执行。


## 10. 原有限配对的真实 normal 变分与指定混合 jets

本节继续使用 (N.21) 的目标刚化和 §8 的自然相对基。
它同时保留配对本身、源基与核的变化；
不会把原 $A$ 在特殊纤维的常矩阵误当作整个族中不变的配对。

### 10.1 整个 $H_\epsilon$ 上的配对及全部自然基补偿

令 $f_\epsilon,g_\epsilon\in H_\epsilon$ 按自然相对单项式基取固定系数。
乘积微分只有 $O$ 一处可能的极，极阶至多 $2p+2$。
因此其相对 Cartier 输出准确属于
$$
\operatorname{span}_K(1,U_Z,V_Z)\,\omega_Z'.
$$
这里 $V_Z$ 项可能非零，不能按 $V_0\times H$ 的较小极界删掉它。
定义 $A_\epsilon(f,g)$ 为该输出中 $U_Z\omega_Z'$ 的系数。
在原参数 $u=U^{-1/2}$ 下，目标 $U_Z=u_Z^{-2}$，
$V_Z\omega_Z'=-u_Z^{-3}du_Z$，且 $F_\epsilon^*u_Z=u^p$，所以
$$
\boxed{
A_\epsilon(f,g)
=\operatorname{Res}_O u^p f_\epsilon g_\epsilon\omega_\epsilon.}
\tag{N.39}
$$
特别地，$A_0=A$ 正是原 R1095 的配对；本式没有新增标量。

自然系数固定并不表示有理函数固定。对奇基，
$\dot{(VU^a)}=vU^{a+1}/(2V)$，而
$\dot\omega/\omega=-vU/(2V^2)$。因而完整导数是
$$
\dot A(f,g)=\operatorname{Res}_O u^p
\left(\dot f\,g+f\,\dot g-\frac{vU}{2V^2}fg\right)\omega.
$$
从
$$
\omega_\epsilon
=(1+\epsilon vu^4+v^2u^6)^{-1/2}du
$$
可逐项给出整个有限矩阵：
$$
\boxed{
\begin{aligned}
\dot A(U^a,U^b)
 &=-\frac v2\binom{-3/2}{n}v^{2n},
 &&a+b=3k+2+3n,\\
\dot A(VU^a,VU^b)
 &=+\frac v2\binom{-1/2}{n}v^{2n},
 &&a+b=3k-1+3n,\\
\dot A(U^a,VU^b)&=0.
\end{aligned}}
\tag{N.40}
$$
前两行若没有非负整数 $n$ 满足所列等式，就按零读取。
在 §8 的全部 $H$ 指标范围内，出现的 $n$ 都不超过 $k-1<p$，
故这些二项式没有不合法分母。

第二行的正号已经包含两个自然奇基和微分标架的共同变化：
$V_\epsilon^2\omega_\epsilon
=u^{-6}(1+\epsilon vu^4+v^2u^6)^{1/2}du$。
交叉项则由 $V_\epsilon\omega_\epsilon=-u^{-3}du$ 恒定直接得到。
这与 (N.35) 中必须保留的曲线约化补偿是同一约定。

### 10.2 两个原有限连接与配对的准确相容式

对 $f\in V_0$、$g\in H$，有
$$
\boxed{
6v\,\dot A(f,g)
=A(\mathcal N_{\rm full}f,g)-A(f,\mathcal Pg).}
\tag{N.41}
$$
这里两边的每个有限空间都按已经付清的最高边界读取。

给出直接留数证明。将 $\dot f_{\rm nat}$、$\dot g_{\rm nat}$
记为固定自然系数而求固定 $U$ 的函数导数，(N.24)、(N.30) 等价于
$$
\begin{aligned}
\mathcal N_{\rm full}f
 &=\frac12D^2f+\frac{U^2}{V}Df+Uf+6v\dot f_{\rm nat},\\
\mathcal Pg
 &=\frac12D^2g-\frac{U^2}{V}Dg-6v\dot g_{\rm nat}.
\end{aligned}
$$
对 (N.39) 在特殊纤维分部积分时，$D(u^p)=0$，
所以 $D$ 反自伴、$D^2$ 自伴。这是局部留数恒等式，
对中途有表面 $1/V$ 的有理函数也合法，不必先删其有限极点。
两边之差中的 $D^2$ 项消去，剩余导数项为
$$
-\operatorname{Res}_O u^p
\left(D(U^2/V)-U\right)fg\omega.
$$
由 $D(U^2/V)-U=3v^2U/V^2$，
再加两个自然基项，恰为 (N.39) 的完整 $6v\dot A$。
因此 (N.41) 没有漏掉最高偶方向或自然奇基修正。

原退化方向的 transverse 值也可以完全定标：
$$
\boxed{\dot A(\Psi,\Psi)=\frac{\delta}{6v}=-H_\epsilon'(0)\in K^\times.}
\tag{N.42}
$$
这里 $\Psi_\epsilon$ 仅指把原 $\Psi$ 的自然奇基系数保持不变；
不声称 ordinary 纤维上仍有满足 $D\Psi=\delta$ 的同一有理 primitive。

确实，$\dot\Psi_{\rm nat}=vU\Psi/(2V^2)$，故
$$
6v\dot A(\Psi,\Psi)
=3v^2\operatorname{Res}_O u^p\frac{U\Psi^2}{V^2}\omega.
$$
另一方面，$\mathcal P$ 保持 $H$，而原 $\Psi$ 是 $A$ 的整个 radical。
由 $D\Psi=\delta$，
$$
\mathcal P\Psi
=-\frac{\delta U^2}{V}
 -\frac{3v^2U\Psi}{V^2}.
$$
所以 $A(\Psi,\mathcal P\Psi)=0$。
原 $\Psi=VU S(U^3)$ 使 $U^2\Psi/V$ 为 $H$ 中的偶多项式；
其原点首项为 $-u^{-p-1}$，于是
$$
\operatorname{Res}_O u^p\frac{U^2\Psi}{V}\omega=-1.
$$
代回就得
$3v^2\operatorname{Res}_O u^pU\Psi^2\omega/V^2=\delta$，
从而证明 (N.42)。本证明只用 $\mathcal P\Psi\in H$；
没有错误地要求 $\mathcal N_{\rm full}\Psi\in H$。

### 10.3 原 $f=U^m$ 的留数与第一 normal 混合读数

对原指定源 $f=U^m$，(N.39) 还可在同一个实际双覆盖
$$
C:\quad V^2=R^6+v^2,\qquad U=R^2
$$
上读取。选择满足 $V/R^3\to-1$ 的无穷远点 $P_\infty$，
在那里 $R=1/u$ 且 $dR/V=u\omega$。因为 $p-2m=1$，
准确有
$$
\boxed{
A(U^m,g)
=\operatorname{Res}_{P_\infty}g(R^2,V)\frac{dR}{V}.}
\tag{N.43}
$$
该点在双覆盖上不分歧，因此没有额外因子 $2$；
也没有将另一无穷远点的留数合并成新的读数。

令 $J_r(T)=D_R^rJ(T,R)|_{R=-Q}$。
目标曲线、$D_R$ 和点 $-Q$ 在本一阶族中固定。
由 (N.25)，对每个原 $f\in V_0$，
$$
\boxed{
6v\left.\partial_\epsilon
 D_R^r\widehat t_f^\epsilon(-Q)\right|_0
=A(\mathcal N_{\rm full}f,J_r)
=D_R^r\Phi(\mathcal N_{\rm full}f)(-Q).}
\tag{N.44}
$$
也可用 (N.41) 同时微分实际配对和实际核得到；
此处两个变化合并后才出现右端，不能只微分 $J$ 或只微分 $A$。

当 $f=U^m$ 时，$\mathcal Nf=(3v^2/2)U^{m-2}$。
原 $\Phi$ 保持偶性并将 $\mu_3$ 角色反转，
而 $m-2=3k-3$，所以
$$
\Phi(U^{m-2})\in K[U^3].
$$
两个原三挠点均被 $\mu_3$ 固定，故
$D_R^r\Phi(U^{m-2})(-Q)=0$，只要 $r\not\equiv0\pmod3$。
特别地，
$$
\boxed{
\left.\partial_\epsilon D_R\widehat t_{U^m}^\epsilon(-Q)\right|_0=0,
\qquad
\left.\partial_\epsilon D_R^4\widehat t_{U^m}^\epsilon(-Q)\right|_0=0.}
\tag{N.45}
$$

特殊纤维的这两项仍是原
$e$ 和 $16ve+4\delta^2K_4$；(N.45) 没有改变其定义。
与此同时，零阶 normal 读数仍是 (N.14) 的单位。
所以首个 normal 单位不等同于这两个指定 Picard jets 的首 normal 变化。
这是已付款的一阶范围结论，不排除更高阶实际族或保留移动源的关系。
若继续到更高阶，(N.1) 的 $\epsilon^2U^2/4$、
自然奇基、相对 Frobenius 目标及真实 FM 标架都须按所需精度保留，
不能迭代一阶式时将它们冻结。

本节全部为同一原来源的纸面推导；没有执行数学程序或新的素数窗口。

§10由o1_theta推导，root独立逐式核对全H的第三类输出、自然奇基补偿、完整留数矩阵和两个指定mixed jets；采用上述完整相对约定。


## 11. 同一三挠覆盖的实际椭圆商与全部 normal Hasse 系数

本节回到 (N.1) 的完整 $K[[\epsilon]]$ 族，保留
$\epsilon^2U^2/4$。所有曲线都取包含 $\epsilon=0$ 的光滑形式邻域。
相对 Frobenius 的目标参数为 $\epsilon^p$，且 $v^p=-v$；
下述等式使用相对 Cartier，对底环线性。
特别地，它们不是把绝对 Cartier 的常数开 $p$ 次根后所得的式子。

### 11.1 原三挠线的真实无分歧三次覆盖

令
$$
C_\epsilon:\quad
V^2=r^6+\frac{\epsilon^2}{4}r^4+\epsilon vr^2+v^2,
\qquad q_\epsilon(r,V)=(U,V)=(r^2,V).
$$
记 $P_\pm=(0,\pm v)$，仍取
$l_+=V-v-\epsilon r^2/2$、$l_-=V+v+\epsilon r^2/2$，故 $l_+l_-=r^6$。
在 $E_\epsilon$ 上 $\operatorname{div}(l_+)=3Q-3O$，
而 $q_\epsilon$ 在 $P_\pm$ 分歧、在两个无穷远点不分歧。
因此
$$
\operatorname{div}_{C_\epsilon}(l_+/r^3)=3(P_+-P_-).
$$
$P_+-P_-$ 不是主除子：否则光滑 genus-two 纤维上有一个一次函数。
所以添上
$$
\eta^3=l_+/r^3
\tag{N.46}
$$
给同一原非平凡三挠线的连通无分歧三次覆盖
$\pi_\epsilon:Y_\epsilon\to C_\epsilon$。
$3$ 可逆，故相同构造在整个形式族中为有限 étale。
$\epsilon=0$ 正是 R1061 中原互逆 $\chi,\chi^{-1}$ 线的三次子覆盖。
还须固定 Kummer 常数：用 R1061 的 $t=x_0^3$、
$r^3=t^{-1}+27t$、$V=27t-t^{-1}$、$v=-6\sqrt{-3}$，准确有
$$
\frac{V-v}{r^3}=-\frac{1-3\sqrt{-3}\,t}{1+3\sqrt{-3}\,t}.
$$
因此选择 $\eta|_0=-z/w$；这确定了原实际覆盖的相位。
下述 $u_0,\nu_0$ 同时为原 R1061 有序两微分的负值。
源与目标同时乘 $-1$ 不改变相对 Cartier 标量；
它不是一个未定的原尺度。

置
$$
a=r\eta,\qquad b=r/\eta.
$$
则在覆盖的实际函数域内
$$
ab=r^2,\qquad a^3=l_+,\qquad b^3=l_-,
\qquad b^3-a^3-\epsilon ab=2v,\qquad
V=(a^3+b^3)/2.
\tag{N.47}
$$
所有等式保原 $r,\eta$ 的标架，不只比较椭圆商的 $j$ 值。

原两条非平凡角色微分可写为
$$
u_\epsilon=a\,\frac{dr}{V}
=\eta\,q_\epsilon^*\omega_\epsilon,\qquad
\nu_\epsilon=b\,\frac{dr}{V}
=\eta^{-1}q_\epsilon^*\omega_\epsilon.
$$
它们全纯：$q_\epsilon^*\omega_\epsilon$ 在 $P_\pm$ 各有一次零，
(N.46) 的零极恰改变这两点的零阶而不增加极。
两个非平凡角色各一维，由 degree-zero 非平凡线的
Riemann–Roch 得到；不删去平凡角色的另外两维。

### 11.2 实际 involution、商曲线与微分尺度

覆盖有真正的对合
$$
\tau(a,b,r)=(-b,-a,r).
$$
它保持 (N.47)，在 $C_\epsilon$ 上诱导 $V\mapsto-V$，
并准确交换 $u_\epsilon,\nu_\epsilon$。
取其不变函数
$$
x=a-b,\qquad Y=(3x+\epsilon)r.
$$
由 (N.47) 得
$$
(3x+\epsilon)r^2=-x^3-2v,\qquad
\boxed{\quad
E_{\rm P,\epsilon}:\ 
Y^2=-(3x+\epsilon)(x^3+2v).
\quad}
\tag{N.48}
$$
$a+b$ 的平方为 $x^2+4r^2$，其符号正由 $\tau$ 改变，
所以这确为完整的二次商函数域。
特殊纤维的 quartic 有四个不同根，故本形式邻域中商是光滑 genus-one 曲线；
点 $(x,Y)=(-\epsilon/3,0)$ 给出一个实际截面。
其微分拉回的精确尺度为
$$
\boxed{
u_\epsilon+\nu_\epsilon=-3\,\frac{dx}{Y}.}
\tag{N.49}
$$
证明不需要选复周期。微分
$x^3+(3x+\epsilon)r^2+2v=0$ 给
$$
3(x^2+r^2)dx+2(3x+\epsilon)r\,dr=0,
$$
而 $2V=(a+b)(x^2+r^2)$，立即得到 (N.49)。

该椭圆商的微分属于两个非平凡三次角色的和，
所以它位于原三次覆盖的 Prym 部分；
本文只使用这个实际商及其微分，不需另称整个 Prym 与某固定椭圆曲线同构。

### 11.3 原 FM normal 值恰等于商的 Hasse 多项式

令
$$
F_\epsilon=(l_-/l_+)^k,\qquad
\theta(\epsilon)
=\frac{C_{{\rm rel},E_\epsilon}(F_\epsilon\omega_\epsilon)}
       {\omega'_{E_\epsilon}}.
$$
该输出全纯：输入在 $Q$ 的极阶为 $3k=m+1<p$，
Cartier 后至多在 $FQ$ 有一个简单极；唯一极的总留数为零。
这就是原 Miller / FM 指定值
$$
\theta(\epsilon)=t_{U^m}^\epsilon(FQ),\qquad FQ=(0,v^p)=(0,-v).
$$
确实，$g_Q=U/l_+^{2k}$ 的除子是
$(-Q)-p(Q)+(p-1)O$，原点首项仍准确为 $u^{p-1}$；
并且 $U^m g_Q=F_\epsilon$。
这里 $[p]Q=-Q$ 来自实际三挠点及 $p\equiv-1\pmod3$。

现在保留相对 twist。目标微分 $u_\epsilon',\nu_\epsilon'$
是 (N.47) 各坐标的 Frobenius twist：
目标方程用 $\epsilon^p,v^p=-v$。
源 $\eta\mapsto\zeta\eta$ 的目标作用为
$\eta'\mapsto\zeta^p\eta'=\zeta^{-1}\eta'$。
相对 Cartier 因而交换这两个基向量的角色。
又
$$
\eta^{-1}=\eta^p(l_-/l_+)^k,
$$
所以与原可分态射拉回的相容性给
$$
C_{\rm rel}(\nu_\epsilon)=\theta(\epsilon)u_\epsilon'.
$$
$\tau$ 与其目标 twist 交换两个微分，故完整非平凡角色矩阵为
$$
\boxed{
C_{\rm rel}(u_\epsilon)=\theta(\epsilon)\nu_\epsilon',
\qquad
C_{\rm rel}(\nu_\epsilon)=\theta(\epsilon)u_\epsilon'.}
\tag{N.50}
$$
常数 $\theta$ 没有被取 $p$ 次根，也没有从不同角色借入 ordinary 值。

对 (N.49) 使用相对 Cartier 与商拉回相容性，
$-3$ 在 Frobenius 下不变，于是 $\theta$ 准确等于
$E_{\rm P,\epsilon}$ 在 $dx/Y$ 标架中的 Hasse 系数。
更直接地写
$dx/Y=Y^{-p}\{-(3x+\epsilon)(x^3+2v)\}^{m}dx$，
其中多项式次数为 $2p-2$，只有 $x^{p-1}$ 一项被 Cartier 读取。
所以
$$
\boxed{
\begin{aligned}
\theta(\epsilon)
 &= [x^{p-1}]\{-(3x+\epsilon)(x^3+2v)\}^m\\
 &=(-1)^m\sum_{j=0}^{k-1}
   \binom m{3j+1}\,3^{m-3j-1}
   \binom m{k+j}\,(2v)^{m-k-j}\epsilon^{3j+1}.
\end{aligned}}
\tag{N.51}
$$
这是原 FM normal 值的完整多项式，不仅是相同零点或未定单位比例。

### 11.4 全部实际 normal 系数与首项核对

每个 $0\le j\le k-1$ 都满足
$$
0<3j+1\le3k-2<m<p,\qquad 0<k+j\le2k-1<m<p.
$$
因此 (N.51) 的全部 $k$ 个显示系数均为单位；
其它次幂的系数严格为零。
相应的通常导数阶乘 $(3j+1)!$ 也与 $p$ 互素，
所以全部阶数 $3j+1$ 的 normal jets 都非零。
所用最高阶 $3k-2<p$，目标族在该有限精度内仍确实固定；
完整相对式 (N.50)–(N.51) 则已保留更一般的目标 $\epsilon^p$。

第一项必须回到原 (N.14)，可完全纸核：
$$
\binom m k=2\binom m{2k},\qquad
2m=-1,\qquad (-3)^m=-1.
$$
最后一式来自 $p\equiv5\pmod6$ 下 $-3$ 为非平方。
将这些式子代入 (N.51) 的一次项，准确得到
$$
\boxed{\theta'(0)
=\frac{(2v)^{2k}}{6v}\binom{3k-1}{2k}.}
\tag{N.52}
$$
没有额外的 $2,3$、绝对 Cartier 符号或同源微分因子。

(N.51) 付清的是保持原三挠线的实际曲线族方向。
在固定 $E$ 上移动 Picard 参数时，该点一般已不再是三挠点，
所以不能把这个三次覆盖仍当作同一个覆盖随该方向移动。
原 $e,K_4$ 的指定 Picard jets 与 (N.51) 的高阶 normal 系数之间，
仍须另付真实来源的比较；(N.45) 已说明最初的混合读数并不相同。
本节没有由全系数单位直接宣布原两障碍非同时为零。

本节为完整代数纸证；已对照 R1061、R1095、R1126 与本篇原族，
没有数学程序执行、新素数窗口或仅凭 $j$ 的模型替换。


§11复核：root、o1_theta、o2_high_coefficient 对精确候选06f875eb的N.46–52逐式独立纸核通过；原覆盖相位、商微分、相对Frobenius与N.14首项全部相容。


## 12. 原 Prym 族的完整二阶 Gauss–Manin 来源

本节只针对 (N.48) 的实际椭圆商，不把其秩二系统当作
整个 $V_0$ 的目标微分系统，也不把其两个初值认作原 $e,K_4$。

### 12.1 原微分上的精确二类恒等式

写
$$
g=3x+\epsilon,\qquad h=x^3+2v,\qquad
Y^2=-gh,\qquad \omega_{\rm P}=\frac{dx}{Y}.
$$
固定 $x$ 求导，准确有
$$
\partial_\epsilon\omega_{\rm P}=-\frac{\omega_{\rm P}}{2g},
\qquad
\partial_\epsilon^2\omega_{\rm P}=\frac{3\omega_{\rm P}}{4g^2}.
$$
因此在这同一个相对函数域内，
$$
\boxed{
\left\{4(54v-\epsilon^3)\partial_\epsilon^2
      -12\epsilon^2\partial_\epsilon-3\epsilon\right\}
 \omega_{\rm P}
=-18\,d_x\left(\frac{h}{gY}\right).}
\tag{N.53}
$$
左边的系数直接化为 $27(6v-\epsilon x^2)/g^2$。
右边则用
$$
d_x(F/Y)
=\left(F'-\frac{F(gh)'}{2gh}\right)\omega_{\rm P},
\qquad F=h/g,
$$
得到
$$
F'-\frac{F(gh)'}{2gh}
=\frac{3(\epsilon x^2-6v)}{2g^2}.
$$
所以 (N.53) 是真实的 exact-differential 身份，
不是从一个模 $p$ 多项式反向猜测的 Picard–Fuchs 方程。

两条 de Rham 类确实独立。在 $\epsilon=0$ 的 $x=0$ 分支点，
用 $Y$ 作参数，
$$
x=-\frac{Y^2}{6v}+O(Y^8),\qquad
\omega_0=-\frac{dY}{3v}+O(Y^6)dY,\qquad
\dot\omega_0=-\frac{dY}{3Y^2}+O(Y^4)dY.
$$
$\dot\omega_0$ 只有这一处二阶极，其留数为零。
$\omega_0$ 的局部原函数与 $\dot\omega_0$ 的乘积留数为
$1/(9v)$，是单位；这给出两类的非零 Serre cup 配对，
符号只随 cup 的输入次序改变。
这里局部原函数所需的第一项没有任何 $p$ 分母，
二类极阶 $2<p$。于是 $\omega_{\rm P}$ 及其一次
Gauss–Manin 导数是同一实际 rank-two de Rham 束的基；
(N.53) 给出其完整标量方程。

这套论证也可在同一 quartic 的特征零形式提升上逐字进行。
因 $54v$ 是单位，$\epsilon=0$ 是这个真实微分方程的非奇异点，
而非借用一个未识别来源的抽象二阶系统。

### 12.2 两个规范局部 period 及有限精度

令
$$
t=\frac{\epsilon^3}{54v}.
$$
把 (N.53) 的标量方程除以 $4$，得到
$$
(54v-\epsilon^3)y''-3\epsilon^2y'-\frac34\epsilon y=0.
\tag{N.54}
$$
在特征零的形式提升中，取初值 $(y(0),y'(0))=(1,0)$ 和 $(0,1)$，
两个规范解准确为
$$
\boxed{
\begin{aligned}
y_0(\epsilon)&={}_2F_1\left(\frac16,\frac12;\frac23;t\right),\\
y_1(\epsilon)&=\epsilon\,
{}_2F_1\left(\frac12,\frac56;\frac43;t\right).
\end{aligned}}
\tag{N.55}
$$
可直接以 $\vartheta=\epsilon\partial_\epsilon$ 核对：
方程等价于
$$
\left\{\vartheta(\vartheta-1)
-t(\vartheta+\tfrac12)(\vartheta+\tfrac32)\right\}y=0.
$$
对 $y_0$ 代 $\vartheta=3t\partial_t$，
对 $y_1$ 代 $\vartheta=1+3t\partial_t$，
正是 (N.55) 中各自的 Gauss 方程和给定初值。

模 $p$ 使用这些解时必须保有限精度。
对 $\epsilon$ 次数严格小于 $p$ 的递推，
所有所需的通常导数阶乘均是单位，且 (N.54) 的首系数在原点为单位。
因此这两个初值在该范围确定唯一的实际 jets。
第一行需要的 $t$ 指标仅为 $0\le j\le2k-1$；
$(2/3)_j$ 的首个含 $p$ 因子出现在 $j=2k$，
对应 $\epsilon^{6k}=\epsilon^{p+1}$，不在所用范围。
不能把安全的有限前缀自动扩成整条特征零 period 的无条件模 $p$ 约化，
也不能忽略特征 $p$ 中次数 $\ge p$ 的新 Frobenius 自由项。

### 12.3 原 Hasse 截面的精确 Gauss 解

对 (N.53) 使用相对 Cartier，右边为零。
目标微分的参数为 $\epsilon^p$，所以对 $\epsilon$ 求通常导数时，
目标微分本身的导数为零。
从 (N.50)–(N.51) 得到的原 $\theta(\epsilon)$
因而真实满足 (N.54)，初值是
$\theta(0)=0$ 和已经定标的 $\theta'(0)$。

其完整多项式式也可以直接写成
$$
\boxed{
\theta(\epsilon)
=\theta'(0)\,\epsilon
\sum_{j=0}^{k-1}
\frac{(1/2)_j(5/6)_j}{(4/3)_j\,j!}
\left(\frac{\epsilon^3}{54v}\right)^j.}
\tag{N.56}
$$
这里 $(5/6)\equiv-(k-1)\pmod p$，
所以这是实际终止的 Gauss 多项式。
所有 $j\le k-1$ 的分母都是单位。
把 (N.51) 相邻系数相除，正得到
$$
\frac{(j+1/2)(j+5/6)}{(j+1)(j+4/3)}
\frac1{54v};
$$
故 (N.56) 与已付的完整 Hasse 多项式逐项相同，
没有使用超出安全范围的非终止变换或删除边界项。

(N.53)–(N.56) 为后继提供一个来源固定的二阶系统：
它来自原三挠覆盖的真实椭圆商和原微分，
同时保留相对 Frobenius 与有限分母范围。
但固定 $C$ 的 Picard 方向离开三挠子空间，
所以此处的 $y_0,y_1$ 初值尚不能换成
$e$ 与 $K_4$；该比较仍是原指定问题的一部分。

本节全部为纸面恒等式与原相对几何的核对，没有数学执行。


§12 发布前由 root/o1/o2 独立逐式纸审：原 exact-differential、唯一二类极的 cup 配对、两组 Gauss 初值、首个 p 分母边界和实际终止 Hasse 多项式均核定；尚未替换原固定曲线 Picard 的 e/K4。
