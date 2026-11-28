# R1177 — 原 syntomic 常数与正向 Frobenius 的符号字典

日期：2026-11-28。  
会话：Astra-serre-24b8836b-20261126。  
状态：已证明，纸面。本文校正一处一次坐标的比较号；不改变原 Kummer 类、整格、cochain、中央群律或原正向 Frobenius 的定义。

## 1. 结论：一次槽取负，原中央公式保持

本篇始终使用原三个约定：

- Kummer cocycle 是正根比 $g(u^{1/p^n})/u^{1/p^n}$；
- 原 affine representation 用左 cocycle 扭曲，原连接为 $\nabla=\nabla_{\rm coeff}+\Omega$；
- 原正向 Frobenius 写成 $\Phi=R(A_\Phi,Z_\Phi)\Phi_{\rm coeff}$，Tate $\mathbb Q_p(r)$ 的 coefficient Frobenius 为 $p^{-r}$。

令原 syntomic abelian cocycle 的两槽为 $(a,S)$，原中央 primitive 的两槽为 $(c,H)$。保持原 ordered product 和
$$
d_{\rm syn}(c,H)=-\mathfrak b\bigl((a,S),(a,S)\bigr).
$$
那么在同一个唯一 Hodge frame 中，准确字典为
$$
\boxed{\qquad
A_\Phi=-S,\qquad
Z_\Phi=\mathfrak b(S,S)-H
      =\mathfrak b(A_\Phi,A_\Phi)-H.
\qquad}
\tag{1177.1}
$$

这里 $\mathfrak b$ 是原完整 bilinear map，包括最低槽的正
$\lambda_\infty x t'$。第二式没有需要额外翻转的中央负号。

R1168 的 $\mathcal R(y)$ 是 syntomic 常数槽，故应记作
$S=\mathcal R(y)$，而不是未经比较就记成实际 $A_\Phi$。
本篇修正的是这一个 identification。
所有实际 normal 收缩、theta/Miller 函数、同根 gauges、
高 Hurwitz 系数及原有序 product 同伦仍按原式使用。

本篇适用于原已构造的 rational、integral-compatible 和有限第一层对象。
它不增加任何 Bernoulli 非零条件。
同一比较的整性由原 R1163–R1166 支付；下面的符号核验没有重新选格。

## 2. 一维正 Kummer 测试锁定这个负号

先在未分歧 $F/\mathbb Q_p$ 上取 $u\in1+p\mathcal O_F$，
并固定同一个兼容根系 $\widetilde u$。
取原正 cocycle $c_g$ 及 affine representation
$$
g e_0=e_0+c_g e_1,\qquad
g e_1=\chi_{\rm cyc}(g)e_1 .
\tag{1177.2}
$$
令 $t$ 为原正 cyclotomic period，置
$$
b_0=\frac{\log[\widetilde u]}t .
$$
因为
$$
g b_0=\frac{b_0+c_g}{\chi_{\rm cyc}(g)},
$$
下列两向量是 $B_{\rm cris}$ 中的 Galois 不变量：
$$
d_0=e_0-b_0e_1,\qquad d_1=e_1/t .
\tag{1177.3}
$$
它们满足
$$
\Phi d_0=d_0,\qquad \Phi d_1=p^{-1}d_1 .
$$

原唯一 Hodge 截面为
$$
e_{\rm H}=d_0+\log(u)d_1 .
\tag{1177.4}
$$
事实上
$e_{\rm H}=e_0+(\log u-\log[\widetilde u])e_1/t$，
括号中的分子属于 $\operatorname{Fil}^1$；
Tate 子对象的 $\operatorname{Fil}^0$ 为零，故这正是固定商上的唯一截面。
由 Frobenius 的半线性，
$$
\Phi e_{\rm H}
=e_{\rm H}+
 \left(\frac{\sigma\log u}{p}-\log u\right)d_1 .
$$
另一方面，原正 syntomic unit symbol 的第二槽是
$$
L(u)=\frac1p\log\frac{u^p}{\sigma u}
    =\log u-\frac{\sigma\log u}{p}.
$$
所以
$$
\boxed{\quad A_\Phi(u)=-L(u).\quad}
\tag{1177.5}
$$
这是原左扭曲、原 Hodge 截面和原正向 $\Phi$ 的直接计算。

### 2.1. 比较映射确实送到正 Kummer

不能用一个未经说明的 inverse Kummer 抵消 (1177.5)。
在同一 period complex 中取
$$
f=\log u-\log[\widetilde u]\in\operatorname{Fil}^1.
$$
它满足
$$
\bigl(\nabla f,(1-\varphi_1)f\bigr)
 =\left(d\log u,\frac1p\log\frac{u^p}{\Phi u}\right)
 =C_\Phi(u).
\tag{1177.6}
$$
而 $g f-f=-c_gt$。
对本篇使用的 mapping fibre
$\operatorname{Cone}(1-\varphi)[-1]$，
其到 Galois complex 的 connecting cocycle 是
$-(g f-f)$，因此 (1177.6) 正好给 $+c_gt$。

这也可直接从解的集合看见：
使连接形式 $(d\log u)$ 消失的 period 截面是
$e_{\rm H}-f\,d_1$，其正 Galois 差给原 (1177.2)。
故两处负号分别来自 mapping-fibre connecting 和
Frobenius extension 的 $1-\varphi$；不能只保其中一处。

Tsuji 的原正 Kummer/product 比较与此相同，出处见 §8。
本节只用一个可直接计算的 principal unit 锁定约定；
一般原单位、moment、norm 和 coefficient tensor 的方向，
随后由同一个函子性比较运输。

## 3. 完整二步群：连接和 Frobenius 同时核定

原群为
$$
(v,z)(v',z')
 =(v+v',z+z'+\mathfrak b(v,v')) .
\tag{1177.7}
$$
相应 affine matrix 在
$\mathbf1\oplus V\oplus Z$ 上为
$$
R(v,z)=
\begin{pmatrix}
1&0&0\\
v&1&0\\
z&\mathfrak b(v,-)&1
\end{pmatrix}.
\tag{1177.8}
$$
此处 $V$ 可以是原三个 abelian 槽的和，$Z$ 可以是原全部三个中心。

采用原 syntomic differential
$$
d_{\rm syn}(x,y)
 =\bigl(\nabla x,(1-\varphi)x-\nabla y\bigr).
\tag{1177.9}
$$
若 $(a,S)$ 是 degree-one cocycle，
则
$$
\nabla a=0,\qquad \nabla S=a-\varphi a .
$$
原 ordered product 的第二槽为
$$
\mathfrak b(S,a)-\mathfrak b(\varphi a,S).
$$
因此 $d_{\rm syn}(c,H)=-\mathfrak b((a,S),(a,S))$
等价于
$$
\begin{aligned}
\nabla c&=-\mathfrak b(a,a),\\
\nabla H&=(1-\varphi)c+
          \mathfrak b(S,a)-\mathfrak b(\varphi a,S).
\end{aligned}
\tag{1177.10}
$$
第一式说明原 connection 的 Lie 中央槽是 $c$：
$$
\Omega=
\begin{pmatrix}
0&0&0\\
a&0&0\\
c&\mathfrak b(a,-)&0
\end{pmatrix},\qquad
\nabla=\nabla_{\rm coeff}+\Omega.
\tag{1177.11}
$$
这里 $\nabla\Omega+\Omega^2=0$ 正是 (1177.10)。
所以 R1166 §16.1 中把 primitive 第一槽写成 $c=-\eta$
而同时把 $\eta$ 当原正连接中央槽的句子，必须改为 $c=\eta$。

### 3.1. 原正向水平条件

设
$\Phi=R(A_\Phi,Z_\Phi)\Phi_{\rm coeff}$。
其水平条件是
$$
\nabla_{\rm coeff}R+\Omega R=R\,\varphi\Omega .
\tag{1177.12}
$$
逐块展开给
$$
\begin{aligned}
\nabla A_\Phi&=\varphi a-a,\\
\nabla Z_\Phi
 &=-(1-\varphi)c
    +\mathfrak b(A_\Phi,\varphi a)
    -\mathfrak b(a,A_\Phi).
\end{aligned}
\tag{1177.13}
$$
将 $A_\Phi=-S$ 代入，并使用 (1177.10)，准确得到
$$
\nabla\{\mathfrak b(S,S)-H\}
 =-(1-\varphi)c+
     \mathfrak b(a,S)-\mathfrak b(S,\varphi a).
$$
这证明 (1177.1) 同时保持原 flat connection 和原 Frobenius。

### 3.2. 常数不是由“导数相同”另行选择

在固定 Hodge splitting 下，mapping-fibre extension construction
把第一槽送到 (1177.11)，把第二槽送到 coefficient Frobenius
与 extension Frobenius 之间的反向 transition。
按原 ordered matrix 顺序，该 transition 是
$$
R(S,H)^{-1}
 =R\bigl(-S,\mathfrak b(S,S)-H\bigr).
\tag{1177.14}
$$
可直接将两边乘上 $R(S,H)$ 核验其为单位矩阵。
(1177.9)–(1177.10) 正是这一 transition 的 flatness 和水平条件，
并不是只规定它们的上同调类。

这一构造在一次子对象上是 §2 的正 Kummer extension；
在纯中央子对象上同样是
$H\mapsto -H$ 的一次 extension。
原 ordered product 的第二槽则固定 (1177.14) 中
唯一的二次项 $\mathfrak b(S,S)$。
因此 (1177.14) 是同一 primitive 代表的实际矩阵，
没有再添一个可选的中央常数。

原 Tsuji comparison 保 Kummer 和 ordered product，
R1163 的 primitive groupoid 以及 R1166 的同根、refinement
和 product 同伦均沿这个 construction 运输。
改变 cochain 代表时携带原 gauge；
没有把所有选根的字面 cocycles 设成相同。
这使 (1177.1) 识别原整对象，而不只是构造一个
有相同 connection 的有理同构类。

需要区分两件事：
(1177.14) 是 inverse transition 的坐标等式；
一般群的 inversion 不是群同态。
而比较旧的同号一次读数与正确物理读数时，
同时翻转所有 abelian 槽、保持中心不变
$(v,z)\mapsto(-v,z)$，本身确是 (1177.7) 的群自同构。
后者解释了下文纯二次式为何不变，但不能替代前面的实际比较。

## 4. 原 scalar Steinberg primitive 的 whole-path 校准

继续 R1166 (1166.45)–(1166.53) 的同一 $U$、$\Phi U=v$：
$$
a=d\log U,\quad b=d\log(1-U),\quad
A=\frac1p\log\frac{U^p}{v},\quad
B=\frac1p\log\frac{(1-U)^p}{1-v}.
$$
原整 primitive 是
$$
h_{\rm syn}=(0,\beta_\Phi),\qquad
d_{\rm syn}h_{\rm syn}=-C_\Phi(U)C_\Phi(1-U).
\tag{1177.15}
$$
它的 Eulerian 展开、短积分 $J$、坏参数的共同 log lift、
所有 normal carry 和同根来源保持 R1155/R1166 原式。

为核定 Frobenius，只在原 rational period ring 写
$\lambda=\log U,\ \mu=\log(1-U)$。
对原正连接 $d+\Omega$，真正的 horizontal fundamental matrix 是
$$
G_{\rm flat}(U)
 =\mathcal H(-\lambda,-\mu,-\operatorname{Li}_2^p(U)).
\tag{1177.16}
$$
因为 $d\operatorname{Li}_2(U)=-\mu\,d\lambda$，
直接用原 ordered 群律得到
$$
dG_{\rm flat}\,G_{\rm flat}^{-1}=(-a,-b,0)=-\Omega.
$$
旧 $G=\mathcal H(\lambda,\mu,-\operatorname{Li}_2)$
满足的是 $dG\,G^{-1}=+\Omega$；
它不能不改号就作为原 $d+\Omega$ 的 horizontal matrix。

令 $D$ 为原 Tate coefficient Frobenius。
同一正向 Frobenius 的矩阵为
$$
\begin{aligned}
R_\Phi
 &=G_{\rm flat}(U)D\,G_{\rm flat}(v)^{-1}D^{-1}\\
 &=\boxed{\ \mathcal H(-A,-B,\ AB-\beta_\Phi)\ }.
\end{aligned}
\tag{1177.17}
$$
最后一式既可直接相乘，也可用
$$
\beta_\Phi
 =\operatorname{Li}_2^p(U)-p^{-2}\operatorname{Li}_2^p(v)
      +A\log(1-U)
$$
核验；整定义仍是 R1166 的实际收敛级数。
因此 R1166 (1166.54) 的中央
$h_R=AB-\beta_\Phi$ 完全不变，实际一次槽则为 $-A,-B$。

同理，R1155 中按旧正 $\log$ matrix 写出的 scalar
relative-Frobenius 三槽，接入原 R1151 的 physical convention
时须同时翻转前两槽，保留第三槽。
已有 $S/J$ 交换、倒置以及二次补偿式与这个 simultaneous flip
相容，不能把其中央项再翻一次。
这也不意味着所有被称为 Bloch–Kato logarithm 或 path coordinate
的量都逐字取负；必须先用其实际 torsor/path 箭头与
(1177.2)、(1177.12) 比较。
本节已给出所需的 whole-variation matrix，因而无需由名称猜号。

## 5. 原 R1168 读取的正确出口

保持 R1168 的全部 complex、$\mathcal R$ 和 $T$。
对原 abelian representative $v=(a,y_v)$，置
$$
S=\mathcal R_V(y_v),\qquad r=T_V(y_v).
$$
经过原有序 gauge 后，中央 syntomic 常数仍准确为
$$
H=\mathcal R_Z\!\left(
 y_h-\mathfrak b(y_v,r)+\mathfrak b(\varphi r,S)\right).
\tag{1177.18}
$$
于是完整出口为
$$
\boxed{
\begin{aligned}
A_\Phi&=-\mathcal R_V(y_v),\\
Z_\Phi&=\mathfrak b(S,S)
-\mathcal R_Z\!\left(
 y_h-\mathfrak b(y_v,r)+\mathfrak b(\varphi r,S)\right).
\end{aligned}}
\tag{1177.19}
$$
若必须用物理 $A_\Phi$ 写内部最后一项，则它是
$-\mathfrak b(\varphi r,A_\Phi)$；
不能把 $S$ 改名成 $A_\Phi$ 而不改这一处号。

因此 R1168 (1168.20)、(1168.25)–(1168.29) 的
原高 Hurwitz 系数向量是 $S_d$。
例如原未平滑四次、八次矩的实际 Frobenius 坐标是
$$
\boxed{\quad
\mathsf A_d^\Phi
=-\sum_{k=0}^d
 \binom dk\frac{b_E^k}{k+1}
 G_{p^2-1-pd+(p-1)k}(E)\,
       \omega^k\eta^{d-k},\qquad d=4,8.
\quad}
\tag{1177.20}
$$
所有原尺度和适用模型保持不变；
本式没有把特殊 CM 高系数公式外推到一般参考曲线。

同样，R1168 §§10–11 的 raw 和 primed 单个向量，
以及 R1174 (1174.18) 的单个 constant vector，
从 syntomic 出口读成 actual Frobenius 时各乘 $-1$。
原 raw 平滑因子、quotient 的 $\sigma$、exact/shear、
same-$C$ trace 及每个 coefficient Hodge frame 都保留。

这里**不改** R1167 的原 pointed coefficient
$x_P\in H^0$。那个对象是 Weil/Kummer 系数的实际 $H^0$ 类，
不是本篇 degree-one extension 的第二槽。
不能把本次 $H^1$ 字典的负号也乘到 $x_P$ 或其 pure powers。

### 5.1. 哪些二次式严格不变

若所有一次输入都一致使用 $S$，或都一致使用 $A_\Phi=-S$，则
$$
\mathfrak b(S,S)=\mathfrak b(A_\Phi,A_\Phi).
$$
特别，
$$
B_{k,l}
 =S_{4,k}S_{8,l}
   -\sum_C S'_{C,4,k}S'_{C,8,l}
 =A^\Phi_{4,k}A^\Phi_{8,l}
   -\sum_C A^{\prime,\Phi}_{C,4,k}A^{\prime,\Phi}_{C,8,l}.
\tag{1177.21}
$$
所以 R1168、R1169、R1174 的最高及两次配对 correlation
ordered/BCH 读式，以及双线性 $Q_\rho$ 和 shear defect $C_\rho$
全部保持原式。
原 BCH 读数仍为
$$
Z_\Phi^{\rm BCH}
 =Z_\Phi-\tfrac12\mathfrak b(A_\Phi,A_\Phi)
 =\tfrac12\mathfrak b(S,S)-H .
$$
单个 abelian 向量的零与非零也不变。
这不意味着任意只翻转一侧的线性等式或混合乘积都不变。

### 5.2. 已知 Tate 值不能再翻一次

原三个 abelian 槽是 $(X,Y,T)$。
若三个 syntomic 槽统一记作 $(S_X,S_Y,S_T)$，则
$$
(X,Y,T)=(-S_X,-S_Y,-S_T),\qquad
\lambda_\infty XT=\lambda_\infty S_XS_T.
\tag{1177.22}
$$
但 R1151/R1152 中已经按原 physical Frobenius 定义的
$T=s$，不是 $S_T$。如果一侧取 R1168 的 $S_X$，
另一侧直接使用这个实际 $s$，则必须写
$$
\boxed{\qquad
\lambda_\infty XT=-\lambda_\infty S_X\,s.
\qquad}
\tag{1177.23}
$$
不能因最低 bilinear 项是二次就漏掉这个混用号。
原群律中的号始终是正 $\lambda_\infty x t'$；
(1177.23) 是坐标字典，并未改变群律。

## 6. 对已刊记录的精确适用表

| 记录 | 需要校正的读法 | 保持不变的内容 |
|---|---|---|
| R1164、R1167 | 不对原 $H^0$ pointed Miller/Weil coefficient 加此负号 | 同根 functions、line frames、$x_P$、pure powers、normal/PD 代表 |
| R1166 §§14–18 | §16 正连接用 $c=\eta$；physical once slots 是 $-A,-B$；horizontal matrix 用 (1177.16) | 原 $\beta_\Phi,J$、$dh=-\Omega$、整尾、所有 product/refinement gauges、中央 $AB-\beta_\Phi$ |
| R1168 §§4–7、10–11 | 所有 $\mathcal R(y)$ 个别向量先称 syntomic $S$；actual vector 为 $-S$；中央出口按 (1177.19) | SDR、normal window、高 Hurwitz 系数本身、raw/primed 尺度；完整二次中央式 |
| R1169 与 R1174 | 原单向量的 PD 公式按 $S\mapsto -A_\Phi$；R1174 (1174.18) 的右边是 $S_{d,k}$ | same-$C$ 双积、最高/两次配对相关读数、$Q_\rho,C_\rho$ 及其零集证明 |
| R1173 | (1173.1) 定义的是实际 $\mathsf A_d^\Phi$，所以原 $W\mathbf A=\mathbf D$ 不改；用 syntomic $\mathbf S$ 时改写为 $W\mathbf S=-\mathbf D$ | actual reference-to-quotient 右增量、Hecke operators、单位理想、有限重建结论 |
| R1151、R1152、R1171 | 原物理坐标定义和独立确定的全局 labels 不因本次字典自动变号；凡接入 $\mathcal R$ 的地方用 (1177.19) | 原有限 FL 分类、群律、实际仿射 Taylor 方向、全局减法的定义 |
| R1149、R1150、R1175、R1176 | 不修改原正连接及由它直接求得的正向 Frobenius | 原全连接、唯一 Hodge 截面、有限精度算法、全部 integrality/pole/rigidity 证明 |

对 R1173 特别展开：令
$\Delta A_{i,C}$ 为原参考点到实际 quotient 的 physical 右增量，
则原 Norm 方程仍是
$$
W_{\ell,d}\mathbf A_d^\Phi
 =\left(\sum_C\operatorname{Sym}^d\psi_C^{-1}
                         \Delta A_{i,C}\right)_i
 =\mathbf D_{\ell,d}.
\tag{1177.24}
$$
若 $\mathbf S_d=-\mathbf A_d^\Phi$，则
$$
W_{\ell,d}\mathbf S_d=-\mathbf D_{\ell,d}.
\tag{1177.25}
$$
可以等价地定义 $\Delta S=-\Delta A$，
但不得只把未知量改成 syntomic 量，仍使用未改号的 physical 右端。
R1174 中引用 R1173 所恢复的向量时，继续使用实际 $A^\Phi$；
(1177.21) 说明其 correlation 公式不受影响。

本篇不重新核定任何独立 arithmetic period 公式。
例如 R1152 的 $r,s,z$ 由其原 positive Kummer、
path action 和正向 Frobenius 单独给出；
本次不能把已实际定义的 $r,s$ 再机械取负。
将其与 R1168 的 syntomic moment 作比较时，
才必须插入本篇字典。
同理，class-level CM norm 等式和全局 Heisenberg labels
不因表示这些类的局部坐标被纠正而改变。

## 7. 旧文顶部的最小更正文字

以下四段是各旧文的准确更正范围。
它们不要求覆盖旧证明或重算旧 source。

### R1166

> **符号更正，R1177。** 本文 $\beta_\Phi$ 及全部 syntomic/cochain 公式保持。接入原正连接 $\nabla=\nabla_{\rm coeff}+\Omega$ 与正向 $\Phi$ 时，§16 的第一连接槽应为 $c=\eta$，实际一次 Frobenius 槽为 syntomic 常数槽的负值；scalar 矩阵为 $\mathcal H(-A,-B,AB-\beta_\Phi)$。中央式 (1166.54)/(1166.54a) 不变。具体 whole-path 与整格字典见 R1177 §§2–5。

### R1168

> **符号更正，R1177。** 本文 $\mathcal R(y)$、高 Hurwitz 系数及 raw/primed 单个向量给 syntomic 常数 $S$，实际 Frobenius 一次槽为 $-S$。原完整中央式仍为 $Z=\mathfrak b(S,S)-H$，其中 $H$ 保留原有序 gauge；若用实际 $A_\Phi$ 代入，按 R1177 (1177.19) 改写内部末项。所有完整双积及相关中央公式不变，不改原 $H^0$ coefficient。

### R1173

> **字典说明，R1177。** 本文 (1173.1) 的 $\mathsf A_d$ 始终是实际正向 Frobenius 坐标，因此 $W\mathbf A=\mathbf D$ 及实际右增量不改。若从 R1168 的 syntomic 常数 $\mathbf S$ 计算，则 $\mathbf A=-\mathbf S$，等价方程为 $W\mathbf S=-\mathbf D$。已按实际 Frobenius 定义的 Tate 值不再取负。

### R1174

> **符号更正，R1177。** 本文开头的 $\mathsf A_d$ 是实际 Frobenius 坐标；(1174.18) 的 PD 右端则是 syntomic 常数，其物理值须取负。最高及两次配对的 same-$C$ 双积、相关中央读式、$Q_\rho$、剪切缺陷和零集分类均为完整二次式，因此保持。与实际参考增量或已知 Tate 值混用时，必须按 R1177 §§5–6 先统一坐标。

此外，R1155 的 scalar relative matrix 若直接用于原物理 once
slots，须用 (1177.17)；其中央有限 dilogarithm 读数不变。
这项说明不把其它文献的 path/Bloch–Kato convention
一概等同于本文 Frobenius convention。

## 8. 原文来源与核验范围

1. Takeshi Tsuji, *On p-adic nearby cycles of log smooth families*,
   Bulletin de la SMF **128** (2000), 529–575。
   [正式全文](https://www.numdam.org/article/BSMF_2000__128_4_529_0.pdf)。
   §2 的 mapping fibre $1-\varphi$、product (2.5)、
   symbol (2.6)–(2.7)、fundamental exact sequence (2.9)
   以及 Proposition 2.11（印刷页545，PDF第18页）
   给原正 Kummer/product 相容；Lemma 2.12
   （印刷页546，PDF第19页）固定根的一致性。
   本文已亲读这些原段。这里用的是既刊比较，
   不引入新的 coefficient comparison 定理。

2. Kenichi Bannai, Shinichi Kobayashi and Takeshi Tsuji,
   *On the de Rham and p-adic realizations of the elliptic polylogarithm for CM elliptic curves*,
   Annales scientifiques de l'ENS **43** (2010), 185–234。
   [正式 PDF](https://smf.emath.fr/system/files/2017-08/ens_ann-sc_43_185-234.pdf)。
   §4.1，Definition 4.3、Proposition 4.8 和 (4.9)
   （印刷页214–215），固定 Tate $\Phi=p^{-j}$
   与 $1-\varphi$ extension complex；
   Proposition 4.14（印刷页217）的显式
   $\Phi(e_i)=e_j-\xi_{ij}\omega^{*\vee}$
   与本篇一次负号相同。只消费这些定义和 extension 公式，
   不扩大该文 prime-to-$p$ CM specialization 的范围。

3. Tsuji, *p-adic Hodge theory*，2001 Arizona Winter School
   [作者讲义](https://swc-math.github.io/dls/DLSTsuji2.pdf)。
   Proposition 2.2（PDF第5页）显写
   $\nabla(1,0)=(0,x)$、$\Phi(1,0)=(1,-y)$；
   Lemma 3.5（PDF第8–9页）显写 connecting 为
   $-(g(a)-a)$。这些原式已亲读，作为符号的直接定位；
   本文 §§2–4 已重做全部所需代数，不以讲义代替一个
   未刊的新比较或新 admissibility 定理。

4. 本仓原 R1147 的左 cocycle representation，
   R1149/R1150 的正连接与正向水平条件，
   R1151 (1151.2)–(1151.3) 的有限 Frobenius 矩阵，
   以及 R1163–R1166 的实际 integral product/groupoid。
   本篇保持这些原定义，修正它们与 R1168 出口之间的一次比较号。

本结论由直接 $B_{\rm cris}$ 一维计算、
完整 ordered matrix 的水平条件、以及同一 scalar whole path
三种方式锁定；没有执行数学程序。
它修复一个确定的比较号，不宣称新的中央非零性、
global-subtracted 障碍或 whole-disc 排除。
