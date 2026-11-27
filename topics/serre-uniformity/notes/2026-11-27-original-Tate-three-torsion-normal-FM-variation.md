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
