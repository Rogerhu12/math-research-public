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
