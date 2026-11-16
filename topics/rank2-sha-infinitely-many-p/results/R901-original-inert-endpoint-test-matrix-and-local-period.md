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


## 附录 A：真实有限端点在自然局部整格中是本原元

本附录进一步区别(25)的平均积分与向量本身的整性。固定 q=ℓ≡−1 modp，故 q 和 q−1 都是 p 单位。取一个有限扩张 E/Q_p，其整数环 O 含 θ 的值及所用非平凡 F_q 加性角色的值，并在需要时包含原局部表示与向量的定义域。

### A.1 两个实际有限模型

用 Knightly–Ragsdale(2-11)–(2-13)的 Kirillov 模型定义
$$
L_\theta=\mathcal O[\mathbf F_q^\times].
\tag{A1}
$$
上三角矩阵的作用只是单位相位与置换；其余矩阵的每个 entry是
$$
-\frac1q\cdot(\text{加性单位相位})\cdot
\sum_{N(u)=c}\text{加性单位相位}\,\theta(u).
$$
唯一显示分母 q 是 p 单位。逆矩阵也由同一公式给出，所以(A1)是完整稳定整格，不只一个 E-空间的任意基。

令 t∈L_θ 为常数函数1，令
$$
t^\vee=\sum_{a\in\mathbf F_q^\times}e_a^\vee
\in L_\theta^\vee.
\tag{A2}
$$
两者都被 split torus T 固定，且
$$
t^\vee(t)=q-1\in\mathcal O^\times.
\tag{A3}
$$
这里 L_θ^∨ 是真正的 O-linear contragredient；不对 p-adic 系数作复共轭。

对原一个球表示，取一个球向量 v，并令 v_x为§5的 q+1 个实际邻点平移。定义其生成格
$$
M_{\rm sph}=\sum_{x\in\mathbf P^1(\mathbf F_q)}\mathcal O v_x.
$$
(19)是准确关系；(20)在 E 上给秩 q。因此
$$
\boxed{
M_{\rm sph}\simeq
M:=\mathcal O[\mathbf P^1(\mathbf F_q)]/
     \mathcal O\!\left(\sum_xe_x\right),
\qquad \bar e_x\longmapsto v_x.}
\tag{A4}
$$
没有额外整关系：任何 E-关系均为常数向量的倍数，而该向量的各坐标都是1，所以整关系系数必在 O。特别(A4)是商格，不可在 p|q+1 时免费换成 augmentation-kernel 格；两者在 E 上同构不代表其整指标为单位。

### A.2 不除群阶的完整不变泛函

对 x≠y，取 g_{xy}∈PGL₂(F_q) 把有序对 (∞,0) 送至 (x,y)，令
$$
A_{xy}=\rho_\theta^\vee(g_{xy})t^\vee,\qquad A_{xx}=0.
\tag{A5}
$$
有序对的稳定子正是 T，故(A5)与 g_{xy} 的选择无关，且全部 A_xy 在 L_θ^∨ 中整。

对固定 x，行和 Σ_yA_xy 被 x的 Borel稳定子固定。cuspidal Kirillov模型没有 Borel-fixed 向量，故该和严格为0。这里也可以直接用上 unipotent作用核：非平凡加性根的阶是 q，与 p 互素，相关根减1是 p 单位；因此其 fixed空间已经在 O 上为0。列和同理。于是(A5)给整 equivariant映射
$$
M\otimes_{\mathcal O}M\longrightarrow L_\theta^\vee.
\tag{A6}
$$
与 evaluation配对，再除以(A3)的单位，得到
$$
\boxed{
\mathscr L_\theta:
L_\theta\otimes M\otimes M\longrightarrow\mathcal O,
\qquad
\mathscr L_\theta(v,\bar e_x,\bar e_y)
=\frac{A_{xy}(v)}{q-1}.}
\tag{A7}
$$
它是完整有限群不变泛函，构造中没有除 |PGL₂(F_q)|、q+1或任何 p-primary群阶。

原不同端点的值准确为
$$
\boxed{
\mathscr L_\theta(t,\bar e_\infty,\bar e_0)=1.}
\tag{A8}
$$
交换两个端点时，(13)给−1。这与(15)的真实反号一致。

### A.3 Coinvariant 的准确本原性

设
$$
C_\theta=(L_\theta\otimes M\otimes M)_{PGL_2(\mathbf F_q)}.
$$
§6已经证明 C_θ⊗E为一维。(A7)在 C_θ 上满射到 O，因为(A8)取1。它的 kernel在 E 上为零，所以恰为 C_θ 的 O-torsion。因而
$$
\boxed{
C_\theta/C_{\theta,\rm tors}\simeq\mathcal O,
}
\tag{A9}
$$
且原端点 t⊗ē_∞⊗ē_0在这个 free quotient中是一个生成元。

对两个新增惰性素数，取两个(A7)的张量积，同样在相应两个有限群的 coinvariant去torsion后把真实双端点读为1。因此这些自然局部整格本身不强迫一因子 p，更不强迫 (ℓ₁+1)(ℓ₂+1) 的整除。

(A9)不把原 CM/Shapiro 全局 cohomology格与这个自然 Kirillov/邻点格无证相认：该实际比较须单独核定；下文附录B对原系数和测试类型支付整比较，同时显式保留old/new拼接、dual pairing和共同目标inverse degree。它给出的严格信息是，(25)中平均得到的 q+1不能被解释成原端点张量在上述完整局部格中的可除性。原全局类可能因全局关系而可除或为零；本附录没有断言相反结论。

这里全部结论由明确矩阵、两个 permutation格和行列和推得，没有运行有限群数值计算。


## 附录 B：原 CM 全新商的整类型、增广理想与双新类的准确除法

本附录把附录 A 的局部模型接回 ACR 的原 CM 提取。所接的是**原 cohomology 系数格和原两个端点的测试格**；不假设对角循环在该格中的像本原，也不把一个满射的系数泛函误作全局 AJ 的满射。

### B.1 原 cyclic p 群的两种新格不能混用

固定一个新增惰性 q，令
$$
h=p^{v_p(q+1)},\qquad G_q=\langle\sigma\rangle\simeq C_h,\qquad
R=\mathcal O[G_q],\qquad
N=\sum_{i=0}^{h-1}\sigma^i.
\tag{B1}
$$
原 reciprocity 决定 $\sigma$ 及有限字符方向；换生成元只改变下述增广理想的生成元，并不改其嵌入。置
$$
A=R/(N),\qquad I=\ker(\epsilon:R\to\mathcal O).
\tag{B2}
$$
它们都是 O-free；准确的 R-linear 整同构是
$$
\boxed{A\xrightarrow{\ \sim\ } I,\qquad
\bar a\longmapsto(\sigma-1)a.}
\tag{B3}
$$
因为 $I=(\sigma-1)R$，而
$\operatorname{ann}_R(\sigma-1)=\mathcal O N$。特别(B3)没有除 h。

这不等于把 R 整地拆成 old 与 new。实际有短正合列
$$
0\longrightarrow R
\xrightarrow{(\epsilon,\mathrm{quot})}\mathcal O\oplus A
\xrightarrow{(a,b)\mapsto a-b\bmod(\sigma-1)}
\mathcal O/(h)\longrightarrow0.
\tag{B4}
$$
证明可直接在 $\mathcal O[X]/(X^h-1)$ 中作除法；又
$A/(\sigma-1)A=\mathcal O/(h)$。交集
$\mathcal O N\cap I=0$，所以左箭头单射；若两个分量模 h 相合，选 R 中 b 的提升后用 N 调整其 augmentation，即得满的纤维积描述。

因此 $N/h$ 与 $1-N/h$ 只是在特征零中定义的分解幂等元；(B4)精确记录了其 p-primary 拼接。经一个非平凡有限字符 $\chi$ 读取(B3)时，嵌入 I→R 的值是
$$
(\chi(\sigma)-1)a(\chi),
\tag{B5}
$$
不是 $ha(\chi)$。若用反 reciprocity，$\sigma^{-1}-1=-\sigma^{-1}(\sigma-1)$；这个明确的群环单位必须随约定一同运输。

有其它原辅助层时，把 O 换成其完整群环；(B1)–(B5)由 O-flat base change 保持。以下先在每个有限 wild 层证明，再按真实 corestriction 取逆极限。

### B.2 不经单个角色幂等元的 universal Kirillov 模型

将原局部 reciprocity 商
$\mathbf F_{q^2}^{\times}\to G_q$
复合到 $A^\times$，记为 $\vartheta_A$。它在 $\mathbf F_q^\times$ 上为1。取含非平凡 F_q 加性角色值的有限 O 扩张；这是忠实平坦的整扩张，以下所有结论按该实际模型下降。

定义
$$
L_A=A[\mathbf F_q^\times],
\tag{B6}
$$
并在 Knightly–Ragsdale(2-11)–(2-13)中把有限角色值换成 $\vartheta_A$。所有矩阵 entry 在 A 中，因为唯一显示分母 q 是 O 单位。它们确实构成完整 PGL₂(F_q) 表示：$A\otimes E$ 分解为所有非平凡 $G_q$ 角色；每个角色都是奇数阶、在 F_q×上平凡而非 Frobenius-fixed，故原定理逐角色适用。矩阵关系在 $A\otimes E$ 中成立，而 A 是 O-torsion-free，因此在 A 中成立。这个论证不使用含 $1/h$ 的角色投影作为整算子。

令 t 为常数函数1。对有限 split Borel
$$
B=U\rtimes T,\qquad |U|=q,\quad |T|=q-1,
$$
(B6)的限制与 $\vartheta_A$ 无关：U给全部非平凡加性角色各一次，T传递地置换它们。特别
$$
L_A^U=0,\qquad L_A^T=At.
\tag{B7}
$$
在本题 $q\equiv-1\bmod p$，所以 $|B|=q(q-1)$ 是 O 单位。这里没有对完整有限群取平均。

### B.3 Split Borel 的明确整矩阵单位

令 $\mathcal V$ 是一个 O-torsion-free 的 A[PGL₂(F_q)] 模；假设在特征零的每个 A-character 上，它是相应 $\rho_\vartheta$ 的若干份，并置 $\mathcal S=\mathcal V^T$。对 $a\in\mathbf F_q$，定义
$$
e_a=\frac1q\sum_{b\in\mathbf F_q}
       \psi(-ab)\,u_b.
\tag{B8}
$$
这是 O 上的真正幂等元。特征零的 cuspidal 条件给 $e_0\mathcal V=0$；O-torsion-freeness把该等式提升为整等式。故
$\mathcal V=\bigoplus_{a\ne0}e_a\mathcal V$，各项由 T 整地互相搬运。

映射
$$
\boxed{
L_A\otimes_A\mathcal S\longrightarrow\mathcal V,\qquad
\mathbf e_a\otimes s\longmapsto e_a s
}
\tag{B9}
$$
是整同构。确切逆可以从任一 $e_a\mathcal V$ 取 T 的全部平移之和恢复 T-fixed 元；不同加性特征的直和使这一步不出现除 $q-1$，且 $t\otimes s\mapsto s$。先由此得到 B-equivariance。再到每个特征零 A-character：有限 cuspidal 的 B 限制是不可约的，B-intertwiner在 multiplicity 空间外只能为标量；因此该已定的 B 同构与完整有限群作用相容。O-torsion-freeness遂将完整 equivariance降回(B9)。

这也证明了一种具体饱和性：若 $\mathcal S$ 是已指定的整 T-fixed 格，那么完整 cuspidal 格由它唯一决定，不再有一个隐藏的 q+1 指标可在 B 方向插入。

### B.4 将(B9)用于 ACR 原 CM 商

这里使用 ACR Theorem3.3、Corollary3.6 的原整同构，而不改选 first CM 形式。记原 CM 提取系数格为
$$
\mathcal Q_n=
\mathcal O[R_n]\otimes_{\varphi_n,\mathbb T'}
 H^1_{\mathrm{et}}(Y(1,N_\psi(n^2))_{\overline{\mathbf Q}},
                   \mathbf Z_p(1)).
\tag{B10}
$$
已有同构 $\widetilde\nu_n$ 把它准确送到原 induced CM 格；它是 $\mathcal O[R_n]$-linear 同构并与原 norm map交换。因而在固定其它层之后，(B10)作为 R-module free of rank2；没有 q+1 分母。其 quotient
$$
\mathcal S_A=A\otimes_R\mathcal Q_n
\tag{B11}
$$
是 A-free of rank2。

为核完整局部类型而非只 T-fixed 线，用 ACR §2.1 的实际 isomorphism
$$
Y(1,N_\psi(n_0^2q^2))
 \xrightarrow{\ \varphi_q,\ z\mapsto qz\ }
Y(1(q),N_\psi(n_0^2q)).
\tag{B12}
$$
右端在 q 处是 ordered pair of distinct cyclic q-subgroups，即 split-torus level。取该实际源的 projective full-q-level cover。其 quotient by T 正是(B12)的源；在包含所有 determinant components 的 adelic 呈示中，T的阶是 q−1。若采用固定 determinant connected component，另有中心与 determinant 的 p′ 因子；它们都整地可逆。原旧 tame level 与 CM/diamond 条件全部保留。

所以 full-level 到原 split-torus level 的 pullback/trace，只需除 q−1；这与主文共同目标 $q_a$ 的次数 $q(q+1)$ 是两种不同映射。紧化 cusps 的 ramification 不破坏这个 p′ group invariants 描述；原 non-Eisenstein completion 同时移除 boundary cohomology。

在 full-q-level cohomology 上，先只施原 $\varphi_n$ 的所有 **q 以外** Hecke条件，再换系数到 A，最后除 O-torsion，所得记为 $\mathcal V_A$。完整有限群仍作用。由于 $|T|$ 为单位，T-invariants 与这些 quotient 操作交换。自然再施 $U_q=0$ 得到(B11)。

这一步没有留下一个未知有限指标。理由如下：在 A 的每个特征零角色上，原 CM 形式在 q 处都是 conductor2的 depth-zero supercuspidal；其 split-torus new line只有一维，且 $U_q=0$。故上段自然满射的 kernel在特征零为0，准确等于 O-torsion；目标(B11)本身 O-torsion-free。因此
$$
\mathcal V_A^T=\mathcal S_A.
\tag{B13}
$$
使用 q 以外的完整 Hecke eigensystem不会另加一个特征零表示：原 newform eigensystem确定同一个 automorphic representation；原其它 bad-prime operators也在所施条件中。局部 principal-congruence invariants恰为 finite cuspidal type；这亦由 KR 的 compact-induction 模型直接核得：非中心 Cartan coset若有 principal-congruence fixed 向量，会给 finite cuspidal 的 U-fixed 向量，因(B7)为0。

于是(B9)在原全新 CM 商上给出
$$
\boxed{\mathcal V_A\simeq L_A\otimes_A\mathcal S_A,\qquad
       t\otimes s\longmapsto s.}
\tag{B14}
$$
这个同构以原(B10)/(B11)的 T-fixed 格定标；不改其 CM period、Shapiro 规范或 first test vector。对 contragredient 约定，取相应 dual 同构及原 reciprocity，不用 Hermitian 共轭替代 O-linear dual。

### B.5 原邻点测试格及可下降的本原泛函

原 g,h 的球向量经实际 geometric degeneracy 平移所生成的格仍为(A4)的商格 M；这只是其全部真实测试向量的 span，不宣称它在 full modular cohomology 中是一个自对偶直和因子。

附录 A 的行列和证明在 A 上逐字成立，给
$$
\mathscr L_A:L_A\otimes_{\mathcal O}M\otimes_{\mathcal O}M
 \longrightarrow A,\qquad
\mathscr L_A(t,\bar e_\infty,\bar e_0)=1.
\tag{B15}
$$
除数仍只有 q−1。把(B14)的 multiplicity module保留，得到原全新 CM 类型与两份实际测试格上的整满射
$$
\bigl(\mathcal V_A\otimes M\otimes M\bigr)_{PGL_2(\mathbf F_q)}
 \longrightarrow\mathcal S_A.
\tag{B16}
$$
其 kernel恰为 O-torsion：每个特征零角色上 invariant multiplicity是1，而(B15)给实际截面 $s\mapsto[t\otimes s\otimes\bar e_\infty\otimes\bar e_0]$。因此 coinvariant的 O-torsion-free quotient准确是 $\mathcal S_A$。两个新增惰性素数同时作此操作，结论在 $A_1\otimes A_2$ 上同样成立。

这里已支付的是原**系数与测试类型**的完整整返回。全局 diagonal/AJ 是进入这个系数 quotient的一枚指定类；(B16)的满射不表示该指定类的像是单位，亦不把循环同调的 primitive generators当作 Chow 或 Galois H¹ 的 generators。

### B.6 原双新类唯一落在乘积增广理想

回到 R900附录 A 的实际双新类 $\mathcal N_{12}$，保任意原旧辅助模数和所有 wild 层。用(B10)及 Shapiro 将原 ring-class extension 的系数写成
$$
\mathcal R_{12}\otimes_{\mathcal O}T,\qquad
\mathcal R_{12}=\mathcal O[G_1\times G_2],
\tag{B17}
$$
其中 $T$ 是本题指定最高 CM 字符的原整格，群环带真实 induced/permutation Galois作用。两个 corestriction分别是系数上的 $\epsilon_1,\epsilon_2$，不是 $N_i/h_i$ 投影。

原17惯性有一个元素在 T 上为−1，在这些新增 ring-class 群上为1。因此对(B17)以及每个增广理想、quotient和任意模 $p^r$，均有 $H^0=0$。短正合列的 cohomology遂给
$$
H^1(I_1\otimes R_2\otimes T)
 \ \lhook\joinrel\longrightarrow\
H^1(R_1\otimes R_2\otimes T),
$$
像恰为第一 corestriction的核；它在 O 上饱和，因为右侧的 quotient嵌入一个 O-torsion-free 的 H¹。

再应用
$$
0\to I_1\otimes I_2\otimes T
 \to I_1\otimes R_2\otimes T
 \to I_1\otimes T\to0
$$
及同一 $H^0=0$，并利用
$H^1(I_1\otimes T)\hookrightarrow H^1(R_1\otimes T)$，得到
$$
\boxed{
\ker(\operatorname{cor}_1)\cap\ker(\operatorname{cor}_2)
=H^1(I_1\otimes I_2\otimes T)
}
\tag{B18}
$$
作为原 H¹ 中的**整、饱和、唯一嵌入**。此式同样用于 compact/ordinary Selmer，只需取原 local conditions的逆像；不凭本式产生新的局部条件。

R900已付原 $\mathcal N_{12}$ 的两个 partial corestriction为0，所以(B18)应用于这枚原类，而非任意形式模型。用(B3)两次，存在唯一
$$
\mathcal N_{12}^{\mathrm{aug}}
 \in H^1(A_1\otimes A_2\otimes T)
$$
使
$$
\boxed{
\mathcal N_{12}
=(\sigma_1-1)(\sigma_2-1)\,
 \mathcal N_{12}^{\mathrm{aug}}.
}
\tag{B19}
$$
(B19)表示由(B3)及原嵌入诱导的同构，不能把右端视为在原 R-module中任取一个可除解。每一有限 wild 层的提升唯一，因此它们与 wild corestriction兼容，给同一有界 Iwasawa来源上的(B19)。

对两个非平凡有限角色，其准确值为
$$
\mathcal N_{12}(\chi_1,\chi_2)=
(\chi_1(\sigma_1)-1)(\chi_2(\sigma_2)-1)\,
\mathcal N_{12}^{\mathrm{aug}}(\chi_1,\chi_2).
\tag{B20}
$$
若 $\chi_i$ 有 exact order $p^{a_i}$，第一因子的 p-adic valuation是
$1/(p^{a_i-1}(p-1))$；这与 $v_p(q_i+1)$ 完全不同。

(B18)的饱和性还给原问题所需的精确等价：任意整数 r≥0，
$$
\mathcal N_{12}\in p^r
 H^1(\mathcal R_{12}\otimes T)
\quad\Longleftrightarrow\quad
\mathcal N_{12}^{\mathrm{aug}}\in p^r
 H^1(A_1\otimes A_2\otimes T).
\tag{B21}
$$
所以原偶数块的 scalar p 整除并未由群环 new 支持自动增加；其真实余量就是(B19)中这枚原全新类的 scalar 格阶。

### B.7 三种 p 成本的明确分界

上述结论将原来源中的三处成本区分如下。

1. **CM/Shapiro 与全新 finite type：**(B10)–(B16)已经整地支付；其中没有 q+1 或 h 的隐藏规范因子。
2. **Old/new 同时分解：**(B4)的余核恰为 O/(h)，不能用单个角色的幂等元将它删除。真实范数核可用(B3)；这给(B19)，不给除以 q+1。
3. **共同目标与 old copy 的 inverse correspondence：**原 $q_a$ 的次数仍是 q(q+1)。若将主文(9)的共同目标 pushforward再认作高层某个归一 old projector，就必须保其 inverse degree；它不等于(B12)的 p′ full-level/T 运输。

此外，M的 invariant pairing本身不是一个整自对偶认同。由(20)给出的 canonical map
$$
M\longrightarrow M^\vee=\mathcal O[\mathbf P^1]_0,\qquad
\bar e_x\longmapsto
\frac{(q+1)e_x-\sum_y e_y}{q}
\tag{B22}
$$
有 cokernel
$$
\boxed{\operatorname{coker}(B22)
 \simeq\bigl(\mathcal O/(q+1)\bigr)^{q-1}.}
\tag{B23}
$$
确证：取 M 的 q个坐标基和 augmentation-kernel的差向量基，除去单位 q后，矩阵为 $(q+1)I_q-J_q$。因为 q为单位，常数线与坐标和为0的 q−1维补空间整直和；矩阵在两者分别为1、q+1。这付清(B23)，不需要整数 Smith计算。

因此将 pullback测试、dual push-extraction、Hermitian平均及共同目标归一互换时，必须明确使用哪个映射；(B15)的本原性不会自动消去(B22)或共同目标的 p 因子。

本附录没有证明(B19)的原类非零、没有证明其 scalar $p^{v_p(q_1+1)+v_p(q_2+1)}$ 整除，也没有由此决定 R893 的增广阶 s。它完成的是原全新系数格、局部类型与双新支持的准确整比较，使这些未付门不再被混作局部 formal-degree 或 CM 提取分母。

### 本附录所用的原文范围

- ACR，前引发表稿，§2.1的 $\varphi_q$；Theorem3.3与Corollary3.6的整 CM 同构及 norm兼容；§4真实非对称退化和固定 test-vector extraction。这里只使用其已显示的整同构，不援引新的 nonvanishing结论。
- Knightly–Ragsdale，前引刊本，(2-11)–(2-13)、Theorem2.5、§3 compact induction与Proposition3.1。B.2–B.5 的 universal A 与整 Borel 矩阵单位由这些明确矩阵及特征零类型自含推出。
- R900附录 A 的原双新类和两个 partial norm；R897 的同一 finite/wild 来源及原系数格；原17惯性−1与 $H^0(T/p^r)=0$ 沿用 R886/R891 的指定角色。
