# Deddens 代数：真实 Haar 模型的 localizing 性、范数不闭性与统一成本障碍

作者：OpenAI ChatGPT / literature 与 /root（GPT-6 Astra Pro）；会话 `Astra-ISP-b2a9acde-20261120`。日期：2026-11-20 UTC。

**状态：已证明的中间结论。** 以下所有模型内论证均完整给出。没有证明原算子有或没有普通非平凡闭不变子空间；一般 Hilbert ISP 仍未解决。本文不作文献新颖性主张。

内部依赖仅为原 [R9 模型](R9-radial-odometer-and-nilpotent-approximants.md)及 [R12 的精确归一化幂估计](R12-normalized-powers-and-compact-commutant.md)，不改变算子、表示、权或测度。

## 1. 设定与采用的外部判据

令 $H=L^2(\mathbb Z_2,\mu)$，$\mu$ 为 Haar 概率测度，

$$
(Uf)(y)=f(y-1),\qquad A=M_wU,
$$

其中 $w$ 是 R9 的连续非负代表，恰在 $0$ 为零，且

$$
w(y)=\alpha_{v_2(y)}\ (y\ne0),\quad
\alpha_j=\exp\!\left(-\frac{280}{3}16^j+90\,8^j-300\,2^j+\frac{850}{3}\right).
$$

特别地，$\alpha_0=e^{-20}$、$\alpha_j\downarrow0$、$w>0$ 几乎处处。置

$$
W_0=1,\qquad W_r(y)=\prod_{j=0}^{r-1}w(y-j),\qquad
\beta_r=\|W_r\|_\infty=\|A^r\|>0\quad(r\ge1).
$$

这里 $W_r$ 连续，零集恰为有限集 $\{0,1,\ldots,r-1\}\subset\mathbb Z_2$。任意正整数尾轨道 $\{y+n:n\ge n_0\}$ 在 $\mathbb Z_2$ 中稠密：在每个商 $\mathbb Z/2^m\mathbb Z$ 中，任意连续 $2^m$ 个整数给全体余类。因此对每个 $y$ 及 $n_0$，

$$
\sup_{n\ge n_0}W_r(y+n)=\beta_r,\qquad
\inf_{n\ge n_0}W_r(y+n)=0. \tag{1.1}
$$

等号只使用连续性、满支集和上述稠密性；没有把每个 odometer 的幂误当遍历。

定义

$$
\mathcal D_A=
\{X\in B(H):\exists C<\infty\ \forall n\ge1,\ f\in H,
\ \|A^nXf\|\le C\|A^nf\|\},
$$

并记满足这个不等式的最小常数为 $c_A(X)$；不存在时记 $c_A(X)=\infty$。该最小常数可取，因为任意一列合法常数下降至其下确界时，对每个固定 $n,f$ 取极限仍得合法常数。

这是 Miguel Lacruz, *Invariant subspaces and Deddens algebras*, Expositiones Mathematicae **33** (2015), 116–120 的定义。已核对作者 [arXiv:1403.5093v1 全文](https://arxiv.org/html/1403.5093v1)及[原 PDF](https://arxiv.org/pdf/1403.5093)。其 **Theorem 2**（作者稿 p.2）要求非零拟幂零算子的整个 Deddens 代数既 **范数闭** 又 **localizing**，才推出超不变子空间。**Lemma 3**（pp.2–3）将范数闭性等价为对全代数统一的 $c_A(X)\le C\|X\|$。以下不引用该定理来代替当前假设的验证。

## 2. 基础代数与乘法算子

逐项应用定义可得 $\mathcal D_A$ 为含单位的复代数，且

$$
c_A(X+Y)\le c_A(X)+c_A(Y),\qquad
c_A(XY)\le c_A(X)c_A(Y).
$$

对任意 $b\in L^\infty$，

$$
A^nM_b=M_{b(\cdot-n)}A^n,
$$

故 $M_b\in\mathcal D_A$ 且 $c_A(M_b)\le\|b\|_\infty$。另外 $A^r\in\mathcal D_A$，$c_A(A^r)\le\beta_r$，从而

$$
M_bA^r\in\mathcal D_A,\qquad
c_A(M_bA^r)\le\beta_r\|b\|_\infty. \tag{2.1}
$$

上式也可直接由 $A^nM_bA^r=M_{b(\cdot-n)}A^{n+r}$ 得出。

## 3. 正向与反向加权平移的准确分类

**定理 3.1。** 对任意 $r\ge1$ 和 $v\in L^\infty(\mathbb Z_2)$，有

$$
M_vU^r\in\mathcal D_A
\quad\Longleftrightarrow\quad
v/W_r\in L^\infty.
$$

当成立时，其最优成本恰为

$$
\boxed{c_A(M_vU^r)=\beta_r\|v/W_r\|_\infty.} \tag{3.1}
$$

分式只在 $W_r>0$ 的满测集上定义。对反向位移，

$$
\boxed{M_vU^{-r}\in\mathcal D_A\quad\Longleftrightarrow\quad v=0\ \text{a.e.}} \tag{3.2}
$$

**证明。** 记

$$
h_n(z)=\prod_{j=1}^n w(z+j).
$$

换元给

$$
\|A^nf\|^2=\int h_n(z)^2|f(z)|^2\,d\mu(z).
$$

对 $X=M_vU^r$ 再换元 $t=z+r$，两个范数被积系数之比的平方根为

$$
|v(t)|\frac{h_n(t)}{h_n(t-r)}
=\frac{|v(t)|}{W_r(t)}W_r(t+n),\qquad n\ge r. \tag{3.3}
$$

每个分母只在有限集为零；去掉这些集以及所有 $n$ 对应零集的可数并，不影响任何 $L^2$ 不等式。对非负乘法权，积分不等式对所有 $f$ 成立当且仅当其系数逐点几乎处处比较：否则在系数严格超标的一片正测度集上取指标函数即可反证。于是 (3.3) 的本质上确界是固定 $n$ 的最佳常数。

关键的交换次序在这里合法，因为 $n$ 为可数指标。对任意非负可测 $q_n$，有

$$
\sup_n\operatorname*{ess\,sup}_t q_n(t)
=\operatorname*{ess\,sup}_t\sup_n q_n(t). \tag{3.4}
$$

一方向显然；另一方向把每个 $q_n$ 的零测例外集取可数并，得到所有不等式同时成立的满测集。由 (1.1)、(3.3)–(3.4)，

$$
\sup_{n\ge r}\operatorname*{ess\,sup}_t
\frac{|v(t)|}{W_r(t)}W_r(t+n)
=\beta_r\operatorname*{ess\,sup}_t\frac{|v(t)|}{W_r(t)}. \tag{3.5}
$$

这证明必要性及 (3.1) 的下界。若分式有界，则 $X=M_{v/W_r}A^r$，由 (2.1) 得到同样的上界，且同时控制 $1\le n<r$；因此等号准确。

现在取 $X=M_vU^{-r}$，换元后对 $n\ge r$ 的比值为

$$
|v(t)|\frac{h_n(t)}{h_n(t+r)}
=|v(t)|\frac{W_r(t+r)}{W_r(t+n+r)}. \tag{3.6}
$$

再去掉所有分母零集的可数并，以及有限集 $\{t:W_r(t+r)=0\}$。若 $c_A(X)<\infty$，则在同一个满测集上 (3.6) 对全部 $n\ge r$ 一致有界。可是由 (1.1)，其分母有趋于零的子列，而固定分子中的 $W_r(t+r)>0$。故这迫使 $v(t)=0$。反向显然。$\square$

**有限 Laurent 和的推论。** 若

$$
X=\sum_{r=-R}^{R}M_{v_r}U^r,
$$

则 $X\in\mathcal D_A$ 当且仅当所有负 $r$ 的 $v_r$ 为零，且每个正 $r$ 的 $v_r/W_r$ 有界（$r=0$ 无额外条件）。证明逐项必要性时，选 $2^m>2R$，用有限阶特征标 $\chi$ 满足 $\chi(1)=\zeta=e^{2\pi i/2^m}$。乘法算子 $M_\chi,M_\chi^*$ 均属于 $\mathcal D_A$，且

$$
M_\chi M_{v_r}U^rM_\chi^*=\zeta^rM_{v_r}U^r.
$$

有限 Fourier 平均 $2^{-m}\sum_{j=0}^{2^m-1}\zeta^{-rj}M_\chi^jX(M_\chi^*)^j$ 恰提取第 $r$ 项，故每一项都属于代数。然后应用定理 3.1。充分性由有限和封闭性给出。

## 4. 范数不闭的明确见证

**定理 4.1。** $\mathcal D_A$ 不在算子范数下闭。

**证明。** 取

$$
v_j=\min(\sqrt w,jw),\qquad X_j=M_{v_j}U,\qquad X=M_{\sqrt w}U.
$$

由 $v_j/w=\min(w^{-1/2},j)$ 及定理 3.1，

$$
X_j\in\mathcal D_A,\quad c_A(X_j)=\alpha_0j,\quad
\|X_j\|\le\sqrt{\alpha_0}.
$$

这里成本等号使用 $w$ 在正测度集上任意小，而非仅在单个零点变小。标量函数满足

$$
0\le\sqrt t-\min(\sqrt t,jt)\le\frac1{4j}\qquad(t\ge0),
$$

故 $\|X-X_j\|\le1/(4j)\to0$。但 $w^{-1/2}\notin L^\infty$，定理 3.1 给 $X\notin\mathcal D_A$。$\square$

这一反例准确否定 Lacruz Theorem 2 的范数闭性假设，而非仅仅尚未证明该假设。

## 5. 单位球强闭包含秩一投影；整个代数确实 localizing

**定理 5.1。** 令 $P_{\bf1}f=(\int f\,d\mu){\bf1}$。则

$$
P_{\bf1}\in\overline{\{X\in\mathcal D_A:\|X\|\le1\}}^{\mathrm{SOT}}.
\tag{5.1}
$$

因此 $\mathcal D_A$ 是 localizing。

**证明。** 对 $n\ge0,k\ge1$，取

$$
X_{n,k}=M_{\min(1,kW_n)}U^n.
$$

对 $n=0$ 它等于 $I$；对 $n\ge1$，它等于 $M_{\min(k,1/W_n)}A^n$，故属于 $\mathcal D_A$。在零集上给乘子任意有限值即可。总有 $\|X_{n,k}\|\le1$，且对固定 $n$，由 $W_n>0$ 几乎处处及控制收敛，

$$
X_{n,k}\longrightarrow U^n\quad\text{SOT},\qquad k\to\infty.
$$

置 $C_m=2^{-m}\sum_{n=0}^{2^m-1}U^n$。对任何只依赖前 $s$ 个二进位的柱函数，当 $m\ge s$ 时 $C_mf=P_{\bf1}f$；这是有限群每个余类被等次访问的直接计算。柱函数在 $H$ 中稠密，且 $\|C_m\|\le1$，所以 $C_m\to P_{\bf1}$ 强收敛。

对每个固定 $m$，收缩算子

$$
Y_{m,k}=2^{-m}\sum_{n=0}^{2^m-1}X_{n,k}\in\mathcal D_A
$$

又强收敛到 $C_m$。因此对任意有限测试向量集及任意误差，可先选 $m$ 再选 $k$，使 $Y_{m,k}$ 同时逼近 $P_{\bf1}$。这就是 (5.1)，不要求未经证明的统一对角收敛速率。

为直接验证 localizing 的完整量词，取闭球

$$
B=\{f\in H:\|f-{f1}\|\le1/2\},
$$

它不含零。给定任意序列 $f_j\in B$，标量 $a_j=\int f_j\,d\mu$ 满足 $|a_j-1|\le1/2$。有子列 $a_{j_\ell}\to a$，且 $|a|\ge1/2$。由 (5.1)，对每个 $\ell$ 分别选择 $Y_\ell\in\mathcal D_A$，$\|Y_\ell\|\le1$，使

$$
\|Y_\ell f_{j_\ell}-P_{\bf1}f_{j_\ell}\|<1/\ell.
$$

此选择仅对已经给定的一个向量要求逼近，合法且不需要对整个球一致逼近。于是 $Y_\ell f_{j_\ell}\to a{f1}\ne0$ 于范数，准确满足定义。$\square$

**附带的传递性。** $\mathcal D_A$ 也传递。任何共同不变闭子空间既对所有 $M_b$ 不变，又对其伴随 $M_{\bar b}$ 不变，故其正交投影属于乘法 MASA 的交换子，是某 $M_{\mathbf1_E}$。再由 $A$-不变性、$w>0$ 几乎处处和保测性得 $E$ 对 odometer 模零不变。该变换遍历，故 $\mu(E)\in\{0,1\}$。若不引用遍历性，可用 $C_m\to P_{\bf1}$ 直接证明所有平移不变的指标函数常数。此共同不变结论不涉及仅对 $A$ 不变的未知子空间。

## 6. 统一 Deddens 成本族不能 localize

原 R12 给出

$$
F_j=\frac{A^{2^j}}{\|A^{2^j}\|},\quad
\|F_j-E_j\|=\eta_j:=\frac{\alpha_{j+1}}{\alpha_j}\to0,
$$

其中 $E_j=e_{10}$ 只作用于第 $j$ 个物理二进位。记

$$
P_j^0=E_j^*E_j,\qquad P_j^1=E_jE_j^*.
$$

**引理 6.1。** 对 $X\in\mathcal D_A$，

$$
\|P_j^0XP_j^1\|
\le\big(c_A(X)+\|X\|\big)\eta_j. \tag{6.1}
$$

**证明。** $E_jP_j^1=0$，所以 $\|F_jP_j^1\|\le\eta_j$。定义给

$$
\|F_jXP_j^1\|\le c_A(X)\|F_jP_j^1\|\le c_A(X)\eta_j.
$$

又 $\|E_jz\|=\|P_j^0z\|$，于是

$$
\|P_j^0XP_j^1\|=\|E_jXP_j^1\|
\le\|F_jXP_j^1\|+\eta_j\|X\|.
$$

得证。$\square$

对有限位集 $J$ 令 $P_J=\prod_{j\in J}P_j^0$。用第一个为一的位把 $I-P_J$ 分成正交投影之和，由 (6.1) 得

$$
\|P_JX(I-P_J)\|
\le\big(c_A(X)+\|X\|\big)\sum_{j\in J}\eta_j. \tag{6.2}
$$

**定理 6.2。** 对每个固定 $C<\infty$，族

$$
\mathcal F_C=\{X\in\mathcal D_A:\|X\|\le1,\ c_A(X)\le C\}
$$

不满足 localizing 的序列紧化要求。更准确地，对任意闭球 $B(f_0,r)$、$0<r<\|f_0\|$，存在序列 $f_m\in B(f_0,r)$，使任意子列及任意 $X_m\in\mathcal F_C$ 的范数收敛像只能趋于零。

**证明。** 选 $\ell\ge1$ 使 $p=2^{-\ell}<r^2/\|f_0\|^2$。取各含 $\ell$ 个位的高位块 $J_m$，且 $\min J_m\to\infty$，令 $P_m=P_{J_m}$。公平 Haar 乘积测度给

$$
P_m\to pI\quad\mathrm{WOT}. \tag{6.3}
$$

对柱函数这是高位独立性的准确等式；用柱函数在 $L^1$ 中的稠密性及 $\|P_m\|\le1$ 即扩展到全部配对。置 $f_m=(I-P_m)f_0$。由 (6.3)，$\|f_m-f_0\|^2\to p\|f_0\|^2<r^2$，删去有限项后它们均在球内。若 $X_m\in\mathcal F_C$，则 (6.2) 给

$$
\|P_mX_mf_m\|
\le(C+1)\|f_0\|\sum_{j\in J_m}\eta_j\to0.
$$

若某子列 $X_mf_m\to g$ 于范数，则 $\|P_mg\|\to0$；另一方面 (6.3) 给 $\|P_mg\|^2\to p\|g\|^2$。故 $g=0$。所有论证对子列不变。$\square$

此处算子 $X_m$ 不要求保正、半交换或为加权复合算子；与 R107 的正半交换子族结论相比，本定理控制的是全部具有统一 Deddens 常数的复算子。

## 7. 任何非零局部紧化都必须付出的定量成本

沿用定理 6.2 的球和 $f_m$，令 $\varepsilon_m=\sum_{j\in J_m}\eta_j$。如果 $X_m\in\mathcal D_A$、$\|X_m\|\le1$ 且沿某子列有 $X_mf_m\to g\ne0$，那么

$$
\boxed{\liminf_m\big(c_A(X_m)+1\big)\varepsilon_m
\ge\frac{\sqrt p\,\|g\|}{\|f_0\|}>0.} \tag{7.1}
$$

**证明。** 由 (6.2)，

$$
\|P_mg\|\le\|g-X_mf_m\|
+\big(c_A(X_m)+1\big)\varepsilon_m\|f_0\|.
$$

左端趋于 $\sqrt p\,\|g\|$，第一项趋于零，遂得 (7.1)。$\square$

对实际权，

$$
\eta_j=\exp(-1400\,16^j+630\,8^j-300\,2^j).
$$

因此这不是一个不指定速率的“可能失控”：在这些真实高位测试上，任何非零 localizing 选择的 Deddens 成本至少达到 $1/\varepsilon_m$ 的量级（常数取决于球及所得非零极限）。式 (7.1) 不涉及未知不变子空间或更换向量源。

## 8. 范数闭包仍不含非零紧算子

**定理 8.1。**

$$
\overline{\mathcal D_A}^{\|\cdot\|}\cap\mathcal K(H)=\{0\}. \tag{8.1}
$$

**证明。** 先由 (6.1) 知每个 $X\in\mathcal D_A$ 满足 $\|P_j^0XP_j^1\|\to0$。这个性质对算子范数极限封闭：若 $X$ 由 $Y\in\mathcal D_A$ 范数逼近，则

$$
\limsup_j\|P_j^0XP_j^1\|\le\|X-Y\|,
$$

再令逼近误差趋于零。因此对任意 $K\in\overline{\mathcal D_A}^{\|\cdot\|}$，上述角范数趋于零。

若 $K$ 同时紧，则对固定 $f$，$P_j^1f\rightharpoonup f/2$ 给 $KP_j^1f\to Kf/2$ 于范数。于是

$$
\left|\|P_j^0KP_j^1f\|-\frac12\|P_j^0Kf\|\right|\to0.
$$

而 $P_j^0\to I/2$ 于 WOT，故 $\|P_j^0Kf\|\to\|Kf\|/\sqrt2$。角范数趋零迫 $Kf=0$；$f$ 任意，得到 $K=0$。$\square$

式 (5.1) 与 (8.1) 不冲突：前者是单位球的强算子闭包，后者是代数的范数闭包。用强逼近的秩一投影代替原代数内的紧算子，会同时丢掉原 Deddens 成本；(7.1) 给出这种丢失的明确量。

因此本路线的准确状态是：**localizing 已证明；范数闭性已被明确反例否定；统一成本的局部紧化也已被排除。** 这不否定其他证明途径，也不解决原 $A$ 的普通不变子空间问题。

