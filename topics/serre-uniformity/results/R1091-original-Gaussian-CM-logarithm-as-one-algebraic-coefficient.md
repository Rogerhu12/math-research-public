# R1091：原 Gaussian CM 首对数的单个代数系数公式

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。
状态：**已证明；纸面推导。**

在原 $X=X_{\rm ns}^{+}(47)$、$q=4513$ 与原 Gaussian CM 点
$y=c_{1728}$ 上，仍令
$$
u_y=[23y-C_\infty],\qquad B_q=q+1-T_q.
$$
本篇把 R1085 的完整 Serre–Tate 首矩化为原短 Weierstrass
变形中的一个有限系数。它不要求先计算 $4511$ 次 Maass 导数，
也没有将未求出的 CM period 设为一。

取 R1086 中 trace $96$、全部 $47$ 挠点已在 $\mathbf F_q$ 上的模型
$$
E_z:\quad Y^2=X^3+A X+z,\qquad A=343,\qquad
\omega_{\rm alg}=\frac{dX}{2Y}.
\tag{1091.1}
$$
$z=0$ 是同一个原 CM 点的 fine lift。固定一组实际 $47$ 挠点基，
并沿此变形作唯一的 étale lift；由它得到原 nonsplit necklace。
对任意原整全纯微分 $\omega_F\in H^0(X_{\mathbf Z_q},\Omega^1)$，
记其在此 fine family 的拉回为
$$
\omega_F=F(z)\,k(z)\,dz,\qquad
k(z)=\frac{-3A}{4A^3+27z^2}.
\tag{1091.2}
$$
这里 $F$ 是原 weight-two section 在 $\omega_{\rm alg}$ 中的值，
不是另选的局部函数。

令原 Hasse invariant 与唯一所需的截断 primitive 为
$$
H(z)=[X^{q-1}](X^3+A X+z)^{(q-1)/2},
$$
$$
I(z)=\int_0^z \frac{k(w)}{H(w)^2}\,dw
       \pmod {z^q}.
\tag{1091.3}
$$
最后的积分只保留次数 $1,\ldots,q-1$，所以只除以
$1,\ldots,q-1$ 中的单位。主结论为
$$
\boxed{\quad
q^{-1}\log_J(B_q u_y)(\omega_F)
\equiv
\frac{23}{k(0)}[z^{q-1}]\,F(z)k(z)I(z)\pmod q.
\quad}
\tag{1091.4}
$$
右侧只需 $F$ 到次数 $q-2=4511$。
这是原 CM 首对数的准确值式；本篇尚未计算这个系数或声称其非零。

## 1. 原 fine family 与 Kodaira–Spencer 常数

因 $q\nmid 6\cdot47$、$A\ne0$，(1091.1) 在原点附近光滑，
全 $47$ 级结构 étale。因此它确实给原模曲线的 fine deformation。
Gaussian 自同构在原 necklace 中被保留；从 fine 到 coarse 的
ramification index 是二，后面始终使用全纯微分的实际拉回。

以下直接支付 (1091.2) 的常数与符号。
写 $D=4A^3+27z^2$。对原 invariant differential 求参数导数，
在 de Rham cohomology 中有
$$
\nabla_{\partial_z}\omega_{\rm alg}
=-\frac{9z}{2D}\omega_{\rm alg}
-\frac{3A}{D}\,X\omega_{\rm alg}.
\tag{1091.5}
$$
可以仅用 exact differentials 验证：置
$$
u=-\frac{9z}{2D},\qquad v=-\frac{3A}{D},\qquad
r(X)=-\frac{2Av}{3}+uX-vX^2.
$$
若 $f=X^3+A X+z$，直接逐幂比较给
$$
-\frac12=(u+vX)f+2r'f-rf'.
$$
乘 $\omega_{\rm alg}/f$ 即
$$
\partial_z\omega_{\rm alg}
=u\omega_{\rm alg}+vX\omega_{\rm alg}
+d(r/Y).
$$
原 $\langle\omega_{\rm alg},X\omega_{\rm alg}\rangle$ 取
Kodaira–Spencer 的 Tate 正号规范，故第二个系数为 $k$。

也可在通用 $A,z$ 上固定该符号：上述计算对两个参数给
$$
\operatorname{KS}(\omega_{\rm alg}^{\otimes2})
=\frac{9z\,dA-6A\,dz}{2(4A^3+27z^2)}.
\tag{1091.6}
$$
代入 Tate 模型 $A=-E_4/48,\ z=E_6/864$，
Ramanujan 的两式使右侧恰为 $dq_{\rm Tate}/q_{\rm Tate}$。
所以 (1091.2) 没有额外的 $2$、$47$ 或负号。
在尖点使用 $t=q_{\rm Tate}^{1/47}$ 时同一式是
$47\,dt/t$，与原 weight-two 到微分的规范相同。

## 2. Hasse 单位与完整 canonical differential

$q\equiv1\pmod4$。直接在 $z=0$ 取系数得
$$
H_0:=H(0)=
\binom{(q-1)/2}{(q-1)/4}A^{(q-1)/4}\ne0
\quad\text{in }\mathbf F_q.
\tag{1091.7}
$$
其阶乘全部小于 $q$，所以这一步不是数值猜测。
同时 $k_0=k(0)=-3/(4A^2)$ 是单位。

在严格 henselian ordinary deformation 上取 R1085 的 physical
Tate bases、canonical differential 及 Serre–Tate 参数 $s$，
canonical CM lift 对应 $s=1$。写
$$
\omega_{\rm can}=\Omega(z)\omega_{\rm alg},
\qquad t=\log s,\qquad \Omega_0=\Omega(0).
$$
原 Igusa 规范给
$$
H(E,\omega_{\rm can})=1,\qquad
\Omega(z)^{q-1}=H(z)\pmod q,
\tag{1091.8}
$$
以及 Katz 的原 Kodaira–Spencer 式
$$
dt=d\log s=\Omega(z)^2 k(z)\,dz.
\tag{1091.9}
$$
(1091.8) 也可由 canonical connected formal group
$\widehat{\mathbf G}_m$ 的 $dT/T$ 的 Cartier 系数为一直接得到；
按 weight $q-1$ 缩放微分即是所写的幂。
$\Omega_0$ 可以在 $\overline{\mathbf F}_q$ 中，未假设它在
$\mathbf F_q$、未将它任意归一为一。

在 $\overline{\mathbf F}_q[[z]]/(z^q)$ 中，
$\Omega(z)^q=\Omega_0^q$。由 (1091.8)，
$$
\Omega(z)\equiv \Omega_0\,\frac{H_0}{H(z)}
       \pmod {z^q},
\qquad \Omega_0^{q-1}=H_0.
\tag{1091.10}
$$
因此 (1091.9) 在所需的合法积分精度内给
$$
t(z)=cI(z)+O(z^q),\qquad c=\Omega_0^2H_0^2,
\qquad I(z)=i_0z+O(z^2),\quad i_0=k_0/H_0^2.
\tag{1091.11}
$$
积分中未使用次数 $q$ 的系数，故没有越过首个 $q$ 分母。
这些等式用于实际 characteristic-zero series 的合法短截断约化，
不是把整个 $\log$ 或 $\exp$ 在特征 $q$ 中形式定义到底。

## 3. 原首矩的留数换元与 period 消去

在同一 $s$ 坐标中写
$$
\omega_F=f_\omega(s)\frac{ds}{s}
        =g_\omega(t)\,dt,\qquad g_\omega(t)=f_\omega(e^t).
$$
所需 $g_\omega$ 到次数 $q-2$ 的全部阶乘都是单位。
令 $C=[t^{q-2}]g_\omega(t)$。由于 $t'(0)\ne0$，
实际 residue 的换元给
$$
C=\operatorname{Res}_{z=0}
        \frac{F(z)k(z)\,dz}{t(z)^{q-1}}.
\tag{1091.12}
$$
这只读取 $t$ 到次数 $q-1$，所以可以使用 (1091.11)。

在特征 $q$ 中，
$$
I(z)^q=i_0^q z^q(1+O(z^q)).
$$
将 (1091.11) 代入 (1091.12)，所有 $O(z^q)$ 项均不能贡献留数，
于是
$$
C=c^{1-q}i_0^{-q}
        [z^{q-1}]F(z)k(z)I(z).
\tag{1091.13}
$$
$H_0,k_0,i_0$ 都在 $\mathbf F_q$ 中；
但 $\Omega_0$ 仍按其实际值保留到此刻。由 (1091.10)，
$$
c^{1-q}=H_0^{-2},\qquad
i_0^{-q}=H_0^2/k_0.
$$
两者相乘准确为 $1/k_0$，证明
$$
\boxed{\ [t^{q-2}]g_\omega(t)
   =k_0^{-1}[z^{q-1}]F(z)k(z)I(z).\ }
\tag{1091.14}
$$
这一步使用 residue 换元，没有把 ramified 的 coarse 参数当成
fine 参数使用。也可由合法的 Lagrange coefficient formula 得到同式。

R1085 已在原全 $q+1$ Hecke targets 上证明
$q^{-1}\log_J(B_qu_y)(\omega_F)\equiv23C$，
包括两个 horizontal targets、全部 $q$ 个 Serre–Tate roots、
完整 Mahler 尾项、下降及特殊点的重数。
消费该结论即得 (1091.4)，不重做其点或尾项计算。

## 4. 原 Gaussian 对称与 coarse 重数

在 (1091.1) 中，
$$
(X,Y)\longmapsto(-X,iY),\qquad i^2=-1,
$$
给 $E_{-z}\to E_z$，其微分拉回为 $i\omega_{\rm alg}$。
在原 CM necklace 上该作用属于 nonsplit Cartan，
所以原 coarse 微分的 fine 拉回满足
$$
F(-z)=-F(z),\qquad k(-z)=k(z),\qquad I(-z)=-I(z).
\tag{1091.15}
$$
因 $q-2$ 为奇数，这个对称不强迫目标系数为零。
fine 微分在原点的一阶零正是 coarse ramification 所要求的零。
(1091.4) 中既不再除以二，也不删除这一零；
R1085 的 Hecke 分支重数已按同一个 coarse 微分计入。

## 5. 可直接实现的原代数输入

公式右侧有以下有限读法，未调用未知的 period 或任意同源模型：

1. 使用原模型 $A=343$ 的真实 $47$ 挠点。选一个非零 $P$，
   令 $Q=iP$；因为 $47\equiv3\pmod4$，它们在
   $\mathbf F_{47}$ 上独立。沿原 Cartan 乘一个 norm 合适的元素，
   可令真实 Weil pairing 为既定 $\zeta_{47}=2$。
   norm map 满射支付此选择，实际 consumer 必须验证所选的 pairing。
2. 只 Hensel lift 一个 $P(z)$ 至所需精度，
   然后令 $Q(z)=iP(-z)$。这正是 $Q$ 的唯一 étale lift，
   不是在 $z\ne0$ 错用 $i$ 为同一椭圆曲线的自同构。
   由原群加法得到全部 $[a]P+[b]Q$。
3. 设 $e_R$ 为 Khuri–Makdisi 的 $G_1(R)$，
   取 $\omega_{\rm alg}=dX/(2Y)$ 的规范。对实际短模型斜率
   $m(R,S)=(Y_R-Y_S)/(X_R-X_S)$，其准确关系为
   $$
   e_{R+S}=e_R+e_S+m(R,S).
   \tag{1091.16}
   $$
   当 $R=S$ 时用切线斜率。由任一不经过零点的 addition chain
   到 $46P=-P$，若累积得到 $e_{46P}=46e_P+L_{46}$，则
   $e_P=-L_{46}/47$。例如链
   $1,2,4,5,10,11,22,23,46$ 的所有相关分母在原点都是单位。
   之后群加法同时累积全部 $e_R$。
4. 在原 weight-one products 和其原 norm/Weil coefficients 上
   形成真正 $F$，再与 (1091.3) 的短级数相乘取一个系数。
   $F$ 只需到 $z^{4511}$，$I$ 只需到 $z^{4512}$；
   所有高次原乘积项仍保留。

(1091.16) 是 Khuri–Makdisi (2012), Corollary 3.13 与
Remark 3.14 在 $X=\wp,\ Y=\wp'/2$ 下的直接式。
若改写为 $Y_{\rm KM}=\wp'=2Y$ 的斜率，才应在该斜率前乘
$1/2$；本篇没有改变 $e_R$ 的尺度。
本节给实现方法，不声称尚未执行的 Hensel、Hodge basis 或
CM coefficient 已获数值认证。

## 6. 准确用途、来源与未完成项

R1089 证明原 $B_q$ 在整 Lie/Hecke 格上可逆，
所以它保持原点类对数的深度和非零性。
不过 (1091.4) 的左侧始终是 $\log(B_qu_y)$：
若要报告 $\log u_y$ 的具体数值，还须在同一实际块上施 $B_q^{-1}$，
不能把单位性当成具体数值相等。

R1088 已证明两条真实 fixed-cycle 类与
$u_{1728},u_0$ 在所有 cusp blocks 生成相同的整 Hecke 模。
本篇为其中 $u_{1728}$ 给可执行的原首对数值式。
真正整 Hodge 坐标、相应块上的非零系数、原高度规范及高度单位，
以及八个圆盘内部唯一性，仍待支付。
全 $p$ 的 Serre 主目标也仍 OPEN。

来源：

- N. Katz, *Serre–Tate local moduli* (1981)，
  Main Theorem 3.7.1–3.7.2 与 Theorem 4.3.1–4.3.2，
  [作者全文](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)；
  R1085 已固定此处所用的 physical bases 与 canonical lift。
- N. Katz, *p-adic properties of modular schemes and modular forms*
  (1973)，§2.0 与 Theorem 4.2.2（printed pp.97–98、147–149），
  ordinary canonical differential 与 Hasse invariant，
  [作者全文](https://web.math.princeton.edu/~nmk/old/padicpropMFMS.pdf)。
  (1091.8) 的所需缩放身份在 §2 另给直接说明。
- K. Khuri–Makdisi, *Moduli interpretation of Eisenstein series*,
  International Journal of Number Theory **8** (2012), 715–748，
  Corollary 3.13、Remark 3.14，
  [作者预印本](https://arxiv.org/abs/0903.1439)。
- [R1085 原 Hecke 首矩](R1085-original-ordinary-CM-Hecke-logarithm-and-Serre-Tate-moment.md)；
  [R1086 原 CM 模型与同点转移](R1086-certified-original-p47-ell4513-same-CM-transfer.md)；
  [R1088 两 fixed-cycle 的原整模](R1088-certified-principal-fixed-cycles-and-two-CM-integral-span.md)；
  [R1089 原 Bq 整可逆](R1089-certified-full-level47-auxiliary-Bq-and-component-groups.md)。

全篇没有运行数学程序、没有重扫旧 prime 窗口。
