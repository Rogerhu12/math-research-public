# 保强位孔数的精确线性规约、真空 forcing 与完整 Green Schur

日期：2026-11-15。Astra-ISP-789f；AI 辅助，GPT-6 Astra Pro。

本稿对原 $C=F_m(B_m)+E$ 保留全部强位，给出一个直接按强位孔数对角作用的精确规约。它与前稿的特定 Artin 替换不同：本稿的物理变换及其伴随都固定整个强真空头空间。完整核 forcing 因而保持原低次数，但 Gram 逆及 Green 的共同残量仍必须保留。本稿不声称已得到原固定 Green 列的 $O(R^3)$ 费用。

## 1. 原物理空间及一个完整行恒等式

原头满足 $B^d=0$，$A=F(B)$，其中 $F$ 是原 $N$ 或 $Y$ 有限函数，

$$
F(0)=0,\qquad F'(0)=d_0^{-1},\qquad d_0=e^{-20}.
$$

强块含 $R$ 个真实 Boolean 位，

$$
E=\sum_{i=1}^R a_iE_i,\qquad a_i>0,\qquad
N_s=\sum_i n_i,\qquad [N_s,E]=-E.
$$

头与强块为原正交张量积，$B$ 与全部强块算子对易。令

$$
L=B/d_0+E,\qquad C=F(B)+E,
$$

以及原头上的单位多项式

$$
\omega(B)=\frac{d_0F(B)}{B},\qquad \omega(0)=1.
\tag{1.1}
$$

这里分式只表示 Taylor 单位多项式，绝不求 $B^{-1}$。置

$$
\boxed{\mathcal W=\omega(B)^{N_s}
=\bigoplus_{n=0}^R\omega(B)^n.}
\tag{1.2}
$$

它在原物理强孔分解中对角，每块可逆，而且与 $B$、$N_s$ 对易。原加权头基的全部 $W_j$ 均保留；(1.2) 不是把 $B$ 换成未加权 Jordan 矩阵。

逐强孔行有

$$
E\mathcal W=\mathcal W\omega(B)E.
$$

因此得到完整算子恒等式

$$
\boxed{C\mathcal W=\mathcal W L\omega(B),\qquad
C=\mathcal W L\omega(B)\mathcal W^{-1}.}
\tag{1.3}
$$

证明在第 $n$ 个强孔输出行直接为

$$
F(B)\omega(B)^n v_n+E\omega(B)^{n+1}v_{n+1}
=\omega(B)^{n+1}\bigl((B/d_0)v_n+Ev_{n+1}\bigr).
$$

所有 $n=0,\ldots,R$ 都包含在内，顶行 $v_{R+1}=0$。所以没有删掉强位顶边或加入新的修复。

因为 $\omega(B)$ 与 $L$ 对易，

$$
\ker C^k=\mathcal W\ker L^k,
\qquad
\operatorname{Ran}C^k=\mathcal W\operatorname{Ran}L^k.
\tag{1.4}
$$

$E_i\mathcal W=\mathcal W\omega(B)E_i$ 也逐位成立；各位核旗、$E$ 的幂核旗及全部强孔截断都被双向保持。这里没有认同其原物理正交补或最小范数。

## 2. 真空 forcing 全部固定，Gram 不被删掉

记 $\Omega_s$ 为强真空。对任意原头向量 $f$，令 $f_\Omega=f\otimes\Omega_s$。由 (1.2) 的 $n=0$ 块，

$$
\mathcal W f_\Omega=\mathcal W^{-1}f_\Omega
=\mathcal W^*f_\Omega=\mathcal W^{-*}f_\Omega=f_\Omega.
\tag{2.1}
$$

令 $K=\ker L$，$\iota:K\hookrightarrow\mathcal H$ 为原物理等距包含，定义

$$
\mathcal G=\iota^*\mathcal W^*\mathcal W\iota>0,
\qquad c_f=\iota^*f_\Omega.
$$

则完整核投影准确为

$$
\boxed{
P_{\ker C}f_\Omega
=\mathcal W\iota\mathcal G^{-1}c_f.}
\tag{2.2}
$$

所以 forcing 的确是 $\iota^*f_\Omega$，没有先乘一个可能巨大的反向列。

还可明确其原次数：令 $N_Be_a=ae_a$。$L$ 严格降低 $N_B+N_s$ 一次，所以 $\ker L$ 按总次数正交分解，且 $P_K$ 保持该分解。固定 $f_\Omega=e_a\otimes\Omega_s$ 时，$c_f$ 准确落在 $K$ 的总次数 $a$ 块。

**但 $\mathcal G^{-1}$ 不一定保持这个块。** 本稿没有将 $\mathcal G^{-1}c_f$ 截到次数 $a$，也没有将其高强孔部分删掉。两个不同总次数的核列可通过同一强孔中的头矩阵 $\omega(B)^{*n}\omega(B)^n$ 发生交叉。

## 3. 真正 Green 输入是共同残量

令 $Q_C=P_{\ker C^*}$。由 (1.3)，完整伴随最小逆为

$$
\boxed{
(C^*)^\dagger f_\Omega
=(I-Q_C)\mathcal W^{-*}(L^*)^\dagger
\omega(B)^{-*}\mathcal W^*(I-P_{\ker C})f_\Omega.}
\tag{3.1}
$$

为验证中间 Moore–Penrose 逆的域，先有
$\mathcal W^*(I-P_{\ker C})f_\Omega\perp K$。
又因为 $\omega(B)^{-1}K=K$，乘其逆伴随仍在 $K^\perp=\operatorname{Ran}L^*$。
由
$C^*=\mathcal W^{-*}\omega(B)^*L^*\mathcal W^*$
逐因子乘回即得正确方程，最后的 $I-Q_C$ 给最小性。

代入 (2.2)，(3.1) 的实际 $L^*$ 输入是

$$
\boxed{
\omega(B)^{-*}
\left[f_\Omega-\mathcal W^*\mathcal W\iota
\mathcal G^{-1}\iota^*f_\Omega\right].}
\tag{3.2}
$$

括号里的两项共同正交于 $K$。不能分别估计以后丢掉第二项，也不能只以 $\omega(B)^{-*}f_\Omega$ 代替 (3.2)。与此前 Artin 全空间表达相比，(3.1) 将 $F(d_0L)/L$ 的差商逆重组为纯头因子 $\omega(B)^{-*}$；其余费用准确进入同一个 $\mathcal W$ 和 $\mathcal G$。

## 4. 全左、全右及裸商的同源运输

设 $D$ 是实际远尾删除，与头和强块全部对易。令 $h=d+R$，保全部 $h$ 段。

若线性头 $L$ 的完整右链 $c_1,\ldots,c_h$ 满足

$$
Dc_1=r_0,\qquad Lc_j+Dc_{j+1}=0,\qquad Lc_h=0,
$$

则

$$
b_j=\mathcal W\omega(B)^{j-1}c_j
=\omega(B)^{N_s+j-1}c_j
\tag{4.1}
$$

是原头 $C$ 的完整右链，来源准确为 $\mathcal W r_0$。所有头幂旗及逐段远尾旗 $\ker D^{j-1}$ 被双向保持。因此完整右域、零源域和裸商均能运输，全部原 nuisance 仍在。

若线性头左链 $c_0,\ldots,c_p$ 满足低行方程、顶部来源 $Lc_p=r_0$，则

$$
v_j=\mathcal W\omega(B)^{j-p-1}c_j
\tag{4.2}
$$

是原头的合法左链，顶部来源同样为 $\mathcal W r_0$。负次幂因 $\omega(B)$ 为单位而合法。

每一行的物理度量准确变为

$$
\omega(B)^{*a}\mathcal W^*\mathcal W\omega(B)^a,
$$

$a$ 必须取该行的实际指数。随后求最小范数必须在这些共同度量中消全部零源。本文不从 (4.1)–(4.2) 推出与 $m,R$ 无关的两费比较。

## 5. 与保真空 Artin 替换的精确关系

在

$$
\mathcal A=\mathbb C[x,y_1,\ldots,y_R]/(x^d,y_1^2,\ldots,y_R^2),
\qquad E=\sum_i a_i y_i
$$

中，令 $\psi=F^{-1}$ 为原形式逆。定义

$$
\alpha_0(x)=x,\qquad
\alpha_0(y_i)
=y_i\frac{\psi(F(x)+E)-x}{d_0E}.
\tag{5.1}
$$

商的常数项为一；每个新 $y_i$ 仍可被原 $y_i$ 整除。因此 (5.1) 保全部关系，并在极大理想模其平方上为恒等。它的显式逆为

$$
x\longmapsto x,\qquad
y_i\longmapsto y_i
\frac{F(x+d_0E)-F(x)}{E}.
\tag{5.2}
$$

并有

$$
\alpha_0(x+d_0E)=\psi(F(x)+E).
$$

所有函数需取到整个 Artin 代数的 $h-1$ 阶，不能截为旧 $d-1$ 阶。

在真实 creation 表示
$\mathcal J(x^ny_I)=W_ne_n\otimes e_I$
中，置
$\mathcal S_0=\mathcal J\alpha_0\mathcal J^{-1}$、
$V_0=\mathcal S_0^{-*}$。则

$$
V_0LV_0^{-1}=\psi(C)/d_0.
$$

强真空空间约化 $\mathcal S_0$：$x$ 完全不变，含任一 $y_i$ 的单项式仍含该位。因此 $\mathcal S_0$、其逆及两个伴随都在该空间为恒等。

还可准确验证

$$
\boxed{V_0|_K=\mathcal W|_K.}
\tag{5.3}
$$

令
$v(x,t)=[F(x+d_0t)-F(x)]/t$，
$q_{ab}(n)=[x^at^b]v(x,t)^n$。
由 (5.2) 的 creation 正规次序，取伴随得

$$
V_0=\sum_{a,b}q_{ab}(N_s)E^bB^a.
$$

对 $k\in K$，$E^bk=(-B/d_0)^bk$。所以

$$
V_0k=v(B,-B/d_0)^{N_s}k
=\omega(B)^{N_s}k.
$$

这证明两个构造给同一个完整核 Gram；全空间变换则不同。主恒等式 (1.3) 已由真实孔行直接证明，不依赖本节形式代数论证。

## 6. 差商的裸列仍可有四次指数

本节仅讨论原 $N$ 模型，说明为什么 forcing 简化后仍不能拆开 (3.2) 或其 Artin 形式。

令

$$
J(z)=F(d_0z)/z
=1+\sum_{i=1}^{m-1}\gamma_i z^{2^i-1},
\qquad
\gamma_i=b_i d_0^{2^i}/d_i>0.
$$

所有非零指数 $2^i-1$ 为奇数。由有限形式几何级数，对每个 $n$，
$[z^n]J(z)^{-1}$ 的所有贡献均有同一符号 $(-1)^n$；故不存在同次数相消。取 $q=2^{m-1}=d/2$，便有

$$
\left|[z^{q-1}]J(z)^{-1}\right|\ge\gamma_{m-1}.
\tag{6.1}
$$

对固定 $f_a=e_a\otimes\Omega_s$，将 $J(L)^{-*}f_a$ 投到头指标 $a$、强孔 $q-1$ 的物理子空间，严格得到

$$
[z^{q-1}]J(z)^{-1}\;
e_a\otimes(E^*)^{q-1}\Omega_s.
$$

若原强前缀含 $q-1$ 个权至少 $(m+q)^{-2}$ 的位，则

$$
\|J(L)^{-*}f_a\|
\ge
\frac{b_{m-1}d_0^q}{d_{m-1}}
\frac{(q-1)!}{(m+q)^{2q-2}}.
\tag{6.2}
$$

因此原真实 $d_i$ 给

$$
\log\|J(L)^{-*}f_a\|
\ge\frac{25}{4}d^4-\frac{105}{8}d^3-O(d\log d).
\tag{6.3}
$$

但当 $a=0$ 时，$f_0\in\ker C$，所以真正的 Green 列严格为零。这个最简单的同源例子直接显示：裸差商列的大量高强孔输出可由完整核残量完全消去，(6.3) 不能下界 Green 费用。

## 7. 仍须支付的共同高孔项

因为 $\omega(B)-I$ 幂零，

$$
\mathcal W
=\sum_{k=0}^{d-1}\frac{N_s^k}{k!}
\bigl(\log\omega(B)\bigr)^k,
\qquad
\mathcal W^{-1}
=\sum_{k=0}^{d-1}\frac{(-N_s)^k}{k!}
\bigl(\log\omega(B)\bigr)^k.
$$

这是精确有限多项式，但 $N_s$ 取遍 $0,\ldots,R$。此前有限复参数 gauge 的 $|a|\le2$ 预算不能直接替代这些全部强孔幂。

本稿完成的是：全部强位的精确规约、强真空 forcing 的真实固定、完整 Schur 与 Green 输入的同源表达，以及完整左右域的实际行度量。剩余目标仍是控制 $\mathcal G^{-1}$ 的跨总次数回馈和 (3.2) 的联合高孔部分；只保线性 $L$ 的分次结构而删掉这些度量，会改变原问题。

原 $N=M$、固定原强块 Green $O(R^3)$ 及完整 ordinary 两费封口均未由本稿完成。
