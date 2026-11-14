# R290：混合有限头乘任意正常尾的排除与真实头矩行列式

2026-11-14，normal-annihilator / 789f。**状态：已证明的中间结论；一般关联正常见证仍开。**

本文把 [R236 的纯有限头排除](R236-appendix-positive-normal-cross-blocks-and-pure-finite-head-exclusion.md)推广到任意混合有限头与任意正常尾的精确张量乘积。尾密度可以无限秩、任意纠缠，不要求连续核、Walsh 对角、可实施乘积基或乘积尾。另排除任意物理有限头块对角正常密度。证明使用原实际有限头的标量矩 Hankel 行列式；它不是原 primitive Gram 的 Hankel 正性主张。

## 1. 原有限头与准确适用对象

在原 Haar 表示或任意一个真实尾上，以 $T$ 表示当前实际归一化生成元，以

$$
\mathcal B=\overline{\mathbb C[I,T]}^{\|\cdot\|},\qquad
\mathcal C=\{T\}'
$$

表示当前范数代数与完整交换子。取 $S\in\mathcal B$，满足零字符且首形式阶为一。原 $S_N,S_Y$ 以及 R253 沿它们得到的每个实际消元尾符号均满足此条件。

固定一个正长度物理头 $M\ge1$，令 $q=2^M$。用原归一化物理头基 $e_0,\ldots,e_{q-1}$，保留全部非零头权 $c_1,\ldots,c_{q-1}>0$，置

$$
\beta=\prod_{i=1}^{q-1}c_i,\qquad
J_0=\sum_{i=1}^{q-1}c_i e_{i,i-1}.
$$

原算子准确写为

$$
T=J(z):=J_0\otimes I+\beta^{-1}e_{0,q-1}\otimes z,
\qquad T^q=I_q\otimes z.
\tag{1.1}
$$

这里 $z$ 是远尾上的实际非零生成元的正标量倍数；不是可任意选择的外部参数。后文先把 $z$ 当作一个标量不定元建立有限矩恒等式，再将其代回这个真实尾算子。

记远尾范数代数与完整交换子为 $\mathcal B_{\rm far}$、$\mathcal C_{\rm far}$。由 [R124 §2 的固定 dyadic 余数有界除法](R124-dyadic-residue-factorization-and-order-one-kernels.md)，准确有

$$
\boxed{S=\sum_{r=0}^{q-1}T^r(I_q\otimes b_r),
\qquad b_r\in\mathcal B_{\rm far},
\qquad b_1\in\mathcal B_{\rm far}^{\times}.}
\tag{1.2}
$$

$b_1$ 的可逆性来自其字符等于 $S$ 的非零一次形式系数；这是原范数代数中的真实有界单位，不是未付费用的形式除法。

任意 $R\in\mathcal C_{\rm far}$ 的提升 $I_q\otimes R$ 与 (1.1) 中的每个块交换，故属于 $\mathcal C$。以下仅使用这些真实提升及其与 $T$ 的有限幂相乘。

**主定理。** 不存在

$$
\rho=\sigma\otimes\nu,\qquad
0\ne\sigma\ge0\text{ 在 }\mathbb C^q\text{ 上},\qquad
0\ne\nu\ge0\text{ 为远尾迹类},
$$

满足

$$
\operatorname{Tr}(\rho SG)=0\qquad(G\in\mathcal C).
\tag{1.3}
$$

事实上证明只需要 $\sigma$ 是任意复矩阵、$\nu$ 为任意迹类，且 $\operatorname{Tr}\sigma\ne0$、$\operatorname{Tr}\nu\ne0$。正性是原见证应用中保证这两个迹锚非零的条件。

## 2. 任意非零迹头矩的 Hankel 行列式

这一节单独使用标量不定元 $u$，并令

$$
J(u)=J_0+\beta^{-1}u e_{0,q-1},\qquad J(u)^q=uI_q.
$$

给定任意 $q\times q$ 复矩阵 $\sigma$，$\tau=\operatorname{Tr}\sigma\ne0$，定义

$$
m_k(u)=\operatorname{Tr}(\sigma J(u)^k),\qquad
H_\sigma(u)=(m_{k+r}(u))_{0\le k,r<q}.
\tag{2.1}
$$

这是一个标量多项式矩阵。对于 $0\le k<q$，单一路径至多经过一次进位，所以

$$
m_0(u)=\tau,\qquad m_k(u)=c_k'+u d_k'\quad(1\le k<q),
\qquad c_k'=\operatorname{Tr}(\sigma J_0^k).
\tag{2.2}
$$

置 $c_0'=\tau$，并令

$$
K=\max\{0\le k<q:c_k'\ne0\}.
\tag{2.3}
$$

**引理 2.1。** 存在多项式 $p_\sigma$，$p_\sigma(0)\ne0$，使

$$
\boxed{\det H_\sigma(u)=u^{q-1-K}p_\sigma(u).}
\tag{2.4}
$$

特别此行列式永远不是零多项式，且其零点 $u=0$ 的重数在 $0,\ldots,q-1$ 之间。

**证明。** 在 Laurent 变量 $t$ 中代入 $u=t^q$。$J(t^q)$ 的特征值为互异的 $\zeta t$，其中 $\zeta^q=1$；对应代数谱投影可直接写为

$$
P_\zeta(t)=\frac1q\sum_{k=0}^{q-1}(\zeta t)^{-k}J(t^q)^k.
$$

定义头谱权 $w_\zeta(t)=\operatorname{Tr}(\sigma P_\zeta(t))$。由 (2.2)，

$$
w_\zeta(t)=\frac1q\left[\tau+
\sum_{k=1}^{q-1}\zeta^{-k}\bigl(c_k't^{-k}+d_k't^{q-k}\bigr)\right].
\tag{2.5}
$$

$K$ 的定义保证它的最低 Laurent 项准确为

$$
w_\zeta(t)=q^{-1}c_K'\zeta^{-K}t^{-K}+\text{更高次项}.
\tag{2.6}
$$

当 $K=0$ 时这就是非零常数项 $\tau/q$。其余 $d_k'$ 项的次数都严格为正，所以不可能消掉 (2.6)。

令 Vandermonde 矩阵 $V(t)$ 的 $(k,\zeta)$ 元为 $(\zeta t)^k$。谱投影分解给

$$
H_\sigma(t^q)=V(t)\operatorname{diag}(w_\zeta(t))V(t)^{\mathsf T}.
\tag{2.7}
$$

$\det V(t)^2$ 等于一个非零常数乘 $t^{q(q-1)}$；而 (2.6) 的 $q$ 项乘积等于一个非零常数乘 $t^{-qK}$ 加更高次项。故 $\det H_\sigma(t^q)$ 的最低项为非零常数乘

$$
t^{q(q-1-K)}=u^{q-1-K}.
$$

左侧本来就是 $u$ 的多项式，所以得到 (2.4)。这里没有使用正定性、Hankel 正性或任何浮点采样。$\square$

整个证明直接使用原有权 $J(u)$，没有将头的物理度量换成一个未运输的无权度量。如果改用固定对角相似 $D^{-1}J(u)D$，迹泛函必须同时运输成 $D^{-1}\sigma D$；后者可能失去 Hilbert 正性，但迹保持不变，本引理只要求非零迹，因而同样合法。本稿不需要这次相似。

## 3. 同一个尾泛函上的有限消元与单位剥除

反设 (1.3) 对 $\rho=\sigma\otimes\nu$ 成立。对 $0\le k<q$，定义实际尾算子

$$
c_k=\operatorname{Tr}_{\rm head}\bigl[(\sigma\otimes I)ST^k\bigr]
=\sum_{r=0}^{q-1}m_{k+r}(z)b_r.
\tag{3.1}
$$

这里的 $c_k$ 不与上一节的标量 $c_k'$ 混同。对全部真实尾 $R\in\mathcal C_{\rm far}$，合法右源 $G=T^k(I_q\otimes R)$ 给

$$
\boxed{\operatorname{Tr}(\nu c_kR)=0
\qquad(0\le k<q,\ R\in\mathcal C_{\rm far}).}
\tag{3.2}
$$

向量记法是 $c=H_\sigma(z)b$。所有矩阵系数都是 $z$ 的标量多项式，所以在原尾代数中彼此交换。伴随矩阵恒等式（这里是代数 adjugate，不是 Hilbert 伴随）给

$$
\operatorname{adj}H_\sigma(z)\,c
=\det H_\sigma(z)\,b.
$$

将余数 $r=1$ 的分量提取出来，并把每个 adjugate 系数吸收到 (3.2) 的真实右源中，得到

$$
\boxed{\operatorname{Tr}\bigl(\nu\det H_\sigma(z)b_1R\bigr)=0
\qquad(R\in\mathcal C_{\rm far}).}
\tag{3.3}
$$

令 $d=q-1-K$。由 (2.4)，$\det H_\sigma(z)=z^dp_\sigma(z)$。真实 $z$ 拟幂零而 $p_\sigma(0)\ne0$，故 $p_\sigma(z)$ 在远尾范数代数中可逆；$b_1$ 也由 (1.2) 是真实单位。取 (3.3) 的右因子为 $[p_\sigma(z)b_1]^{-1}R$，准确消去这两个固定单位，得到

$$
\boxed{\operatorname{Tr}(\nu z^dR)=0
\qquad(R\in\mathcal C_{\rm far}).}
\tag{3.4}
$$

此处固定头 $q$、固定 $\sigma$；全部 adjugate、$p_\sigma(z)^{-1}$ 和 $b_1^{-1}$ 的范数都只是有限常数。没有声称这些费用在移动 $q$ 上统一，也没有把一般零字符尾元有界除以 $z$。

## 4. 原归一化高幂关闭最后的正常迹锚

若 $d=0$，(3.4) 取 $R=I$ 已给 $\operatorname{Tr}\nu=0$，矛盾。

若 $d>0$，对每个充分大 $\ell$，$2^\ell\ge d$，取真实有界尾多项式

$$
R_\ell=\frac{z^{2^\ell-d}}{\|z^{2^\ell}\|}.
$$

由 (3.4)，

$$
\operatorname{Tr}\left(\nu\frac{z^{2^\ell}}{\|z^{2^\ell}\|}\right)=0.
\tag{4.1}
$$

右源 $R_\ell$ 的范数允许增长；每一步用的是准确的全右零式。真正最后取正常极限的输出是范数恰为 $1$ 的实际归一化幂。原高幂定理在每个真实尾上给

$$
\frac{z^{2^\ell}}{\|z^{2^\ell}\|}\longrightarrow\tfrac12I
\quad\mathrm{WOT}.
\tag{4.2}
$$

$z$ 为原尾生成元的正标量倍数，该倍数在归一化中取消，所以这是 [R12 的原归一化高幂结论](R12-normalized-powers-and-compact-commutant.md)，不是新造的纯模型极限。由统一范数界，(4.1) 可对固定迹类 $\nu$ 取极限，得 $\operatorname{Tr}\nu/2=0$，矛盾。主定理得证。

上述证明也说明，若 (1.3) 只要求范数代数 $\mathcal B$ 的右源，结论仍成立：本证明实际使用的尾 $R$、两个单位逆、adjugate 系数及最终 $R_\ell$ 全部可取在远尾范数代数，提升后仍在 $\mathcal B$ 中。只有在直接陈述完整尾配对时才写成 $\mathcal C_{\rm far}$。

## 5. 任意物理有限头块对角密度也不可能

设一个正正常密度在同一个原物理头上块对角：

$$
\rho=\sum_{i=0}^{q-1}|e_i\rangle\langle e_i|\otimes\nu_i,
\qquad \nu_i\ge0,
\qquad \nu=\sum_i\nu_i\ne0.
\tag{5.1}
$$

各尾块任意，不要求彼此相等或对角。

**引理 5.1。** 对任意 $F\in\mathcal C$，其全部物理头对角块相同。

**证明。** 由 $FT=TF$ 和 (1.1)，对 $1\le i<q$ 的 $(i,i-1)$ 块，左右分别是 $c_iF_{ii}$ 和 $c_iF_{i-1,i-1}$。$c_i\ne0$，故相邻对角块相等。$\square$

因此对全部原 $F\in\mathcal C$ 有准确正常泛函身份

$$
\boxed{\operatorname{Tr}(\rho F)
=\operatorname{Tr}(\nu F_{00})
=\operatorname{Tr}\bigl[((I_q/q)\otimes\nu)F\bigr].}
\tag{5.2}
$$

特别 $F=SG$ 仍在 $\mathcal C$。如果 (5.1) 是 $S\mathcal C$ 湮灭者，(5.2) 就使同一个真实尾 $\nu$ 的正乘积密度 $(I_q/q)\otimes\nu$ 成为湮灭者，与主定理矛盾。这里没有把不同 $\nu_i$ 各自宣布为湮灭者，也没有换一个独立挑选的尾密度。

## 6. 原相容链的真实相关性与支撑后果

对真正的原见证 $\rho$，R253 给

$$
\nu_j=\operatorname{Tr}_{<j}\rho,
\qquad \operatorname{Tr}(\nu_jQ_jR)=0
\quad(R\in\mathcal C_j),
$$

其中每个 $Q_j$ 在第 $j$ 位开始的实际尾上首形式阶仍为一。将主定理用于这个同一 $\nu_j$，得到：

- 对每个 $j\ge0$ 及每个 $M\ge1$，$\nu_j$ 都不能在其前 $M$ 位与剩余远尾之间精确分成两个正常正态的张量乘积；前块密度可以任意混合。
- $\nu_j$ 不能对其任何正长度物理初始头为块对角。特别，若原 $\rho$ 与某一个物理位指标乘子交换，则取到该位的部分迹给被排除的一位块对角情形。因此实际见证不能与任何单个物理位指标交换。
- 任意非平凡切分后的真实尾边缘不能为秩一。因为若远尾边缘纯，正性将原密度支撑压到有限头张量这一条尾直线，原密度便精确因式为某个混合头密度乘该纯尾，已被主定理排除。

这些是从真实零式得到的严格相关性和支撑约束，强于单纯排纯头；它们没有给相关程度、非纯距离或熵的统一正下界。R289 的低秩相容链可以在每次切分保持非零相关，同时相关量很小，因此不能由上述严格不等式直接推出熵密度正。

## 7. 量词和未闭部分

本稿固定一个有限物理头就完成其全部乘积态排除，没有通过移动头规模来隐藏 adjugate 或单位逆费用；最后只对实际一致有界归一化高幂使用正常性。一般正密度的头尾关联不满足 $\rho=\sigma\otimes\nu$，其多项尾泛函不能由本稿的一个标量 Hankel 系统同时消去。因此本稿未排一般有限秩正常见证，R276 的全链正完成缺口仍开放。

形式上，主证明只需要 (1.2) 的某一个 $b_s$ 为真实单位；所以也适用于首形式阶 $s<q$ 的符号。原应用统一取 $s=1$，从而每个正长度头 $q\ge2$ 都合法。没有将这一观察用于 $s\ge q$ 的切分，也没有声称所有零字符元都可直接除以当前生成元。
