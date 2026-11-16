# R901 — 原惰性双新来源的真实端点、三维 old 测试矩阵与绝对局部因子

日期：2026-11-16。**状态：已证明。** 本篇继续 R897/R900 的原始对角来源。所有旧坏位 2、3、17 的向量、原 q/q⁴ 呈示、CM 提取及 ordinary Euler 均不改变。这里只分析新增良好惰性素数处，有限 ring-class 角色真正分歧时的实际局部向量。

结论有两个部分。首先，ACR 的非对称来源在新增 ℓ 处确实使用相距2的两个端点；整个三维 old 空间在共同目标中只有02与20两项，且互为相反数。其次，对这两个真实端点，单位新向量/球向量的局部矩阵系数积分为 (ℓ+1)/ℓ³。以 vol(PGL₂(Z_ℓ))=1 计算的通常 Euler 正规化因子是 (ℓ+1)⁻²；YZZ 的实际 Haar 规范另给 (ℓ−1)/(ℓ²(ℓ+1))。

这些是原双新块全部非平凡局部角色的精确结果。局部测试非零不证明双新全局类非零，也不支付将该类除以 (ℓ₁+1)(ℓ₂+1) 的整性。

## 1. 同一个原来源与新增角色

保留 R826/R831 的三个原有序对
$$
(g,h)=(g_{10},g_{16}),\ (g_{16},g_4),\ (g_4,g_{10}),
$$
以及 first CM 表示、原2处的不同端点和 R900 的最高角色。

令 p>211 普通，n为原允许的平方自由辅助模数。取 ℓ|n，ℓ 在 K=Q(ω) 惰性，且 ℓ∤30·34p。设 χ 为原 p-primary ring-class 群 G_n 的有限角色，并要求
$$
\chi|_{G_\ell}\ne1.
\tag{1}
$$
它在 ℓ 处为 F_{ℓ²}× 上的非平凡奇数阶角色 θ，且
$$
\theta|_{\mathbf F_\ell^\times}=1,\qquad
\theta^\ell=\theta^{-1},\qquad
\theta^2\ne1.
\tag{2}
$$
这些条件来自 R900 的原类域商，不另选局部字符。

原 first CM 形式经这个 χ 扭曲后，在 ℓ 处的 unitary automorphic representation 记为 π_f。它是 conductor exponent2的 depth-zero supercuspidal，中心特征1。其 finite cuspidal type 由 θ 或 θ⁻¹给出；以下两种约定所得完全相同。原 g,h 在 ℓ 处未分歧、中心特征1，而且
$$
a_\ell(g)=a_\ell(h)=0.
\tag{3}
$$
因此其 unitary Satake 参数均为集合 {i,−i}。这里的 i 只描述复 unitary 规范，不加入原 p-adic 系数域。

其它 tame 角色或有限 wild 角色在 ℓ 处的未分歧因子不改变上述结论：反循环角色在有理主理想 (ℓ) 上取1；原 first CM 的中心特征及 (2) 保持不变。

## 2. ACR 原退化映射确实是0/2端点

必须使用 ACR §4 的实际记号
$$
Y(m)=Y(1,N(m)),
\tag{4}
$$
而不是 Y₁(Nm)。其 Definition 4.3 的非对称类由
$$
(1,\pi_1,\pi_2)_*\kappa^{(1)}_{n^2}
\tag{5}
$$
得到，并保留原 diamond、weight 和 test-vector 因子。

ACR(2.2) 中 π₂ 在上半平面作用为 z↦rtz。对
Y(n²)→Y(1)，参数是 r=s=1、t=n²，故
$$
\pi_1:z\longmapsto z,\qquad
\pi_2:z\longmapsto n^2z.
\tag{6}
$$
于是 ℓ 处的两个 old 向量准确为
$$
g_0(z)=g(z),\qquad h_2(z)=\ell^2h(\ell^2z)
\tag{7}
$$
在权二微分规范下的局部分量。不是相距1的两个向量，也不是两个同时由同一低层拉回的球向量。原2处 q/q⁴ 倍率与 (7) 分属不同素数，均保留。

在有限 χ 的 first CM quotient 上，(1)恰使 first 因子在 ℓ² 新。ACR 的 CM/Hecke 同构未将这个新线换成 ℓ 处的球线。

## 3. 完整三维 old 空间只剩两个端点

这一节在共同目标的有理 Chow 群中计算，保留实际 cusp 基点；为定义指定 Hecke 与 χ 投影，必要时再扩张到包含其数值的特征零系数域。“有理 Chow”不表示每个单独角色幂等元的系数都在 Q。若 first CM 导子还含其它辅助素数，把它们全部收入与 ℓ 互素的 M；原 g,h 可先按旧向量置于该共同 M 层。令
$$
X=X_0(\ell^2M),\qquad C=X_0(M),\qquad
q_a:X\to C,\quad z\mapsto\ell^a z,\quad a=0,1,2.
\tag{8}
$$
设 e_f 为上述 ℓ²-new first 因子，e_g,e_h 为原另外两因子。定义
$$
Z_{ab}=(e_f\otimes e_g\otimes e_h)_*
       (\mathrm{id}\times q_a\times q_b)_*\Delta_X.
\tag{9}
$$
每个实际 q_a 的几何次数为 ℓ(ℓ+1)。若要返回 X³ 的单个 old 副本，必须保留对应的 [ℓ(ℓ+1)]⁻² 拉回；本篇不将该数当作 p 单位。

当 |a−b|≤1 时，后两因子同时经过 X₀(ℓM) 的同一退化映射。first 的 ℓ²-new 投影杀掉这条 h¹ 拉回。R829/R831 的小对角图形恒等式和 Manin–Drinfeld cusp CK 相容遂给
$$
Z_{ab}=0\qquad(|a-b|\le1).
\tag{10}
$$
这是共同目标上的完整 Chow 等式。

取整数 A,B,C,D 使
$$
\ell^2AD-MBC=1,
$$
并令
$$
W=
\begin{pmatrix}
\ell^2A&B\\
\ell^2MC&\ell^2D
\end{pmatrix}.
\tag{11}
$$
它定义实际 partial Atkin–Lehner w_{ℓ²}。若 B_a=diag(ℓ^a,1)，则
$$
B_aW=\ell^a
\begin{pmatrix}
\ell^aA&B\\MC&\ell^{2-a}D
\end{pmatrix}B_{2-a},
\qquad
\begin{pmatrix}
\ell^aA&B\\MC&\ell^{2-a}D
\end{pmatrix}\in\Gamma_0(M).
\tag{12}
$$
所以 q_aw_{ℓ²}=q_{2-a}，权二几何微分没有额外倍率。

下面核 first 新线的绝对号。令 ρ_θ 是 finite cuspidal type，T为有限 split torus。其 T-fixed 空间一维。Weyl 元
$$
w=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$
保持这条线。对于任何非零 trace-zero d∈F_{ℓ²}，(2)给 θ(d)=1。对 T 的 character average，split regular 项为0；另半数 wt 为 nonsplit regular，cuspidal character为 −θ(d)−θ(d)^ℓ=−2。因此
$$
w|_{\rho_\theta^T}=-1.
\tag{13}
$$
此处 θ 为奇数阶是必要的，不能对任意 even-order 深度零角色不加修改地复用。

实际 conductor2 新向量由该 T-fixed 向量作 diag(ℓ⁻¹,1) 平移得到。局部 Atkin–Lehner 与其共轭相差中心 ℓ，而中心特征1，故新线特征仍为−1。其它有限位的 (11) 属于相应 K₀(M)；平凡 nebentypus 不添相位。因此
$$
e_f(w_{\ell^2})_*=-e_f.
\tag{14}
$$
各 cusp 基点在 CH₀_Q 中相同，modified diagonal 的同步 w_{ℓ²} 推前不变。由 (10)、(12)、(14)，置 Z=Z_{02}，得到
$$
\boxed{
(Z_{ab})_{0\le a,b\le2}
=
\begin{pmatrix}
0&0&Z\\
0&0&0\\
-Z&0&0
\end{pmatrix}.}
\tag{15}
$$
所以共同目标的任意两组 old extraction 系数给
$$
Z(\mathbf c,\mathbf d)=(c_0d_2-c_2d_0)Z.
\tag{16}
$$
这里是线性对应的提取，不是把随向量变化的归一 projector 当成线性。

(15)也适用于原 X₁ 呈示的 diamond-trivial 部分，但需用实际 X₁→X₀ 次数运输。新增 ℓ 的次数可能含 p；本篇只在 Q 系数下使用这种运输，不抹去其整成本。

## 4. 新向量的紧支使完整局部积分成为有限群平均

以下写 q=ℓ，F=Q_ℓ，G=PGL₂(F)，K₀=PGL₂(Z_ℓ)，并先固定
$$
\operatorname{vol}(K_0)=1.
\tag{17}
$$
所有向量都以各自 invariant Hermitian norm归一为1。记 v_f 为真实 conductor2 新向量，v_g、v_h 为球向量，v_{h,2}为(7)的局部平移向量。所求未正规化积分是
$$
I_q=\int_G
 \langle\pi_f(x)v_f,v_f\rangle
 \langle\pi_g(x)v_g,v_g\rangle
 \langle\pi_h(x)v_{h,2},v_{h,2}\rangle\,dx .
\tag{18}
$$
若原向量未归一，(18)按三份 norm平方的乘积作除法；因此改变 q-expansion 首项的标量不改变这个定义。

Knightly–Ragsdale Proposition 3.1 给 v_f 的实际 compact-induction 模型：共同平移之后，它是支撑于 ZGL₂(Z_ℓ) 的 finite T-fixed 单位向量 t。Proposition 1.1 给矩阵系数在该紧模中心之外为0。**没有 formal-degree 乘数 q−1。** 该论文另一个函数 Φ_θ 的定义含 formal degree，不能用它替代(18)的单位向量矩阵系数。

同一次共同平移将 g,h 移到 Bruhat–Tits 树中以中间顶点为中心的两个不同邻点。故(18)准确等于有限群
$$
\overline G=PGL_2(\mathbf F_q)
$$
上的归一平均；不会留下其它 Cartan shell。

## 5. 两个球向量的准确有限 Gram

令 P¹=P¹(F_q)。对任一球表示 π，a_q=0，记相邻顶点的 q+1 个单位平移向量为 v_x，x∈P¹。球 Hecke 关系给
$$
\sum_{x\in\mathbf P^1}v_x=0.
\tag{19}
$$
K₀ 对不同的有序邻点对传递，所以其 off-diagonal 内积为同一实数 b。对(19)与任意 v_x 取内积，得到
$$
1+qb=0,\qquad
\langle v_x,v_y\rangle=
\begin{cases}1&x=y,\\-1/q&x\ne y.\end{cases}
\tag{20}
$$
因此该有限 K₀ 空间恰是 Steinberg 表示
$$
\mathrm{St}=\mathbf C[\mathbf P^1]_0,
$$
并有明确 isometry
$$
v_x\longleftrightarrow
\sqrt{\frac{q+1}{q}}
\left(e_x-\frac1{q+1}\sum_ze_z\right).
\tag{21}
$$
原两因子的 Hecke 值同为0，故两份(21)均适用。端点对应不同的 x,y。

## 6. 一次 Schur 正交计算给绝对分子

令 ρ=ρ_θ，dimρ=q−1，t为其 T-fixed单位向量。有限 permutation 空间
$$
\mathcal W=\mathbf C[\mathbf P^1\times\mathbf P^1]
$$
分为对角和非对角两轨道；后者为 Ind_T^{\overline G}1，轨道大小
$$
[\overline G:T]=q(q+1).
\tag{22}
$$
ρ不出现在 C[P¹]=1⊕St 中，且 dimρ^T=1。因此它在 W 中出现一次，完全位于 St⊗St。

令 J:ρ^∨→W 为 invariant isometry。对固定不同点 x,y，evaluation 对应 T-fixed线。Schur 正交/轨道求和给
$$
|J(t^\vee)(x,y)|^2
=\frac{\dim\rho}{[\overline G:T]}
=\frac{q-1}{q(q+1)}.
\tag{23}
$$
可直接核其归一：矩阵系数模型
J(v)(gT)=c\langle v,\rho^\vee(g)t^\vee\rangle
的总 norm为 c²[\overline G:T]\|v\|²/(q−1)，故
c²=(q−1)/[\overline G:T]。

在 ρ⊗W 的唯一 invariant线上，单位向量是
$$
\frac1{\sqrt{q-1}}\sum_\nu e_\nu\otimes J(e_\nu^\vee).
$$
所以 t⊗e_x⊗e_y 的正交投影 norm平方为
$$
\frac1{q(q+1)}.
\tag{24}
$$
将 e_x、e_y分别改成(21)时，去常数部分不影响 cuspidal投影，两份长度倍率使平方 norm乘 (q+1)²/q²。有限群平均就是 invariant projector，因而
$$
\boxed{
I_q=\frac{(q+1)^2}{q^2}\frac1{q(q+1)}
=\frac{q+1}{q^3}.}
\tag{25}
$$
这是一个正的有理数，对全部满足(2)的实际 θ均相同；没有使用 θ 的复近似、任选相位或辅助数值。

## 7. 全部 local L 因子与两种 Haar 规范

采用 unitary automorphic L 因子。π_f的 inertia 无不变向量；其 adjoint 的未分歧部分是 unramified quadratic character。又因 θ²≠1，剩余两个 adjoint惯性字符非平凡。因此
$$
L(s,\operatorname{Ad}\pi_f)=(1+q^{-s})^{-1}.
\tag{26}
$$
由(3)，
$$
L(s,\operatorname{Ad}\pi_g)
=L(s,\operatorname{Ad}\pi_h)
=(1-q^{-s})^{-1}(1+q^{-s})^{-2}.
\tag{27}
$$
三重张量是 π_f的四个未分歧 twist，无 inertia invariants，所以
$$
L(s,\pi_f\otimes\pi_g\otimes\pi_h)=1.
\tag{28}
$$
据此，明确以(17)的 Haar 定义
$$
I_q^\natural=
\frac{\prod_{v=f,g,h}L(1,\operatorname{Ad}\pi_v)}
{\zeta_q(2)^2L(1/2,\pi_f\otimes\pi_g\otimes\pi_h)}I_q.
\tag{29}
$$
由(26)–(28)，Euler比是 (1+q⁻¹)⁻³，故
$$
\boxed{I_q^\natural=(q+1)^{-2}.}
\tag{30}
$$
这也由直接积分证明原端点确为非零局部 test vector；与 Dimitrov–Nyssen Theorem3 的 conductor2端点相容。

YZZ §1.4/式(2.2.6)使用不同 Haar：M₂(F)上的 self-dual additive measure、B×上的 ζ_q(1)|det|⁻²dx，再除中心 d×x。F=Q_ℓ 且标准 conductor0 additive character时，
$$
\operatorname{vol}_{\rm YZZ}(K_0)
=\zeta_q(1)(1-q^{-1})(1-q^{-2})
=1-q^{-2}.
\tag{31}
$$
中心 Z_ℓ× 的乘法体积为1。因此其实际 α 为
$$
\boxed{
\alpha_q^{\rm YZZ}
=(1-q^{-2})I_q^\natural
=\frac{q-1}{q^2(q+1)}.}
\tag{32}
$$
不能把(30)直接带入采用(31)的全局高度公式。这里仅计算局部函数；没有据 YZZ 的全局高度公式删去坏位补项。

## 8. 返回原双新来源与准确整性范围

对 R900 的双新块 N_{i;ℓ₁,ℓ₂}，每个可能非零角色在两素处都满足(1)。所以(15)和(25)–(32)分别在两处同时适用，原两处新增因子的乘积准确为
$$
I_{\ell_1}I_{\ell_2}
=\prod_{r=1}^2\frac{\ell_r+1}{\ell_r^3},
\quad
I_{\ell_1}^\natural I_{\ell_2}^\natural
=\frac1{(\ell_1+1)^2(\ell_2+1)^2}.
\tag{33}
$$
原2、3、17因子及全局 periods没有消失；(33)只是本篇新增位的完整乘数。

置 m_ℓ=v_p(ℓ+1)>0。原 p>211、ℓ≡−1 modp 给
$$
v_p(I_\ell)=m_\ell,\qquad
v_p(I_\ell^\natural)=-2m_\ell,\qquad
v_p(\alpha_\ell^{\rm YZZ})=-m_\ell.
\tag{34}
$$
这些局部非零数都不是可忽略的 p 单位。原 ACR 完整 norm标量 A_ℓ=−(ℓ+1)²/ℓ 与(30)另满足
$$
A_\ell I_\ell^\natural=-\ell^{-1}.
\tag{35}
$$
(35)是两个已分别证明的规范量之间的数值恒等式，不是把矩阵系数积分当作作用于 cohomology的 correspondence。

尤其：
- (15)排除了用同一个 ℓ²-old 三空间再造独立端点关系；不同 old 提取只给(16)。
- (25)排除了“新增局部向量其实为零，因此双新块必为零”的捷径。
- (30)–(34)并不证明 N_{i;ℓ₁,ℓ₂} 可除以 (ℓ₁+1)(ℓ₂+1)。复 Hermitian规范、角色幂等元以及共同目标拉回中的次数，不能代替原 O[Gal]-格的整同构。
- 原双新块的有界整除、实际增广阶及原 s=0 门仍需同一原来源上的新输入。

本篇没有将局部测试非零升级成全局 Chow 或 AJ 非零，没有将原 endpoint 换成 R814 canonical 类，也没有在本地执行数学计算。

## 原文及既有来源

- [R897 原 full wild–tame 系统](R897-original-endpoint-complete-wild-tame-system-and-specialization.md)、[R900 原惰性奇偶与双新块](R900-original-inert-layer-parity-and-exact-one-prime-return.md)。
- [R831 原二处共同目标和 cusp CK 规范](R831-original-dyadic-old-space-and-unique-endpoint-class.md)。本篇新增 ℓ 的向量、符号及次数另由(8)–(16)支付。
- Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL₂×GL₂*，[发表稿](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)：§2.2、式(2.2)，printed pp7–8；§4、Definition4.3与Lemma4.4，pp14–16；§6的原最高CM来源。
- Andrew Knightly–Carl Ragsdale, *Matrix coefficients of depth-zero supercuspidal representations of GL(2)*, Involve7(2014),669–690，DOI [10.2140/involve.2014.7.669](https://doi.org/10.2140/involve.2014.7.669)，[刊本](https://msp.org/involve/2014/7-5/involve-v7-n5-p08-s.pdf)：Proposition1.1、Theorem2.7、Proposition3.1及§3.3。formal degree与单位向量的区别在本文§4显式保留。
- Dimitrov–Nyssen, *Test vectors for trilinear forms when at least one representation is not supercuspidal*，[作者全文](https://arxiv.org/pdf/1005.0724)，Theorem3。本文的绝对积分由§4–7自含求出，不只引用非零测试判据。
- Yuan–Zhang–Zhang, *Triple product L-series and Gross–Kudla–Schoen cycles*，[2023作者全文](https://web.math.princeton.edu/~shouwu/publications/triple2023.pdf)：§1.4的 Haar、式(2.2.6)的 local factor。只用其明确规范；未调用含未付坏位项的 global nonvanishing推论。
