# R311：固定 Robert 乘积与真正上层实 Norm 单位的代数表达式

**状态：已证明的明确全局代数定义；巨大乘积及根尚未求值。**

本篇保持 R171、R191、R201、R219、R305 的同一个 p=43、q、CM 主类、
Weil 根和 tame 生成元。我们用一个完全指定的有限 Robert 乘积及唯一正实
43 次根，定义一个特定普通单位 X∈L⁺，并证明 N_{L/F}X=U。
该 X 还生成整个 L/K。这里没有待选的非零比例、Hilbert 90 解或根的全局分支。

但有限乘积含 42(q²−1)/43 个因子，本次**没有执行这个乘积**；
也没有算出 X 的 R305 坐标、该 X 的范数行列式或 q 剩余相位。
因此 **𝓛 仍未求值**。本篇的“明确代数定义”不等于完成了数值 Norm 求解。

## 1. 域、点与两种实际生成元

令

\[
 A:y^2=x^3-x,\qquad K=\mathbf Q(i),\qquad p=43,
 \qquad F=K(z),\qquad L=FL_q.
\tag{311.1}
\]

F/K 是 R219 带标签的 44 次域；L_q/K 是 R191 导子 (q) 的循环 43 次域。
固定原来的复共轭 τ，并在同一个复嵌入中取非零实 p 挠点 P 和
非零实 q 挠点 Q。保留

\[
 P_2=(i,1-i),\qquad
 v(R)=\frac{64^{10}}{\psi_{11,A}(R)}.
\tag{311.2}
\]

P₂ 的 O_K-消去理想为 (1+i)³。每个下文出现的
P₂+[a]P+[b]Q 的消去理想因此为 (1+i)³pq，且没有任何 ψ₁₁ 的零点。

记

\[
 m_q=\frac{q^2-1}{43},\qquad
 H_q=(\mathbf F_{q^2}^{\times})^{43}.
\tag{311.3}
\]

R171 的同一个素数满足

\[
 q\equiv-1\pmod{172},\quad
 v_{43}(q+1)=1,\quad m_q\equiv21\pmod{43}.
\tag{311.4}
\]

因为 43∤q−1，H_q 包含 F_q×；也包含 μ₄。
符号 [b]Q 表示任意高斯整数提升 b∈O_K/(q)=F_{q²} 所给的 CM 作用，
与提升选择无关。

CM 的 primary CRT 描述给

\[
 \operatorname{Gal}(K(A[pq])/K)
 \simeq\mathbf F_{p^2}^{\times}\times\mathbf F_{q^2}^{\times}.
\]

这也可由 R70 的单素数描述及两模数的 CRT 直接得到：两模数共同的
(1+i)³ 射线域就是 K，因该处剩余单位恰被 μ₄ 商去。
F L_q 是 subgroup F_p××H_q 的不动域。
q 因子的唯一次数 43 子域在二处不分歧，导子恰为 q，故就是 R191 的 L_q。

在 L 中，σ 始终表示 R219 的 F 上生成元并固定 L_q。
在完整 CRT 群中可以把它提升成

\[
 (\beta\bmod p,1\bmod q),\qquad\beta=-1+2i.
\]

这里不是把同时非平凡作用于 q 因子的全局 Frob_β 偷换成 σ。
其限制到 F 的标签已经由 R219 的 44 条 CM 分支核准。

### 1.1 γ 的取向不是另选的 q 相位

令 ζ 为 R171/R191 的同一个 Weil 根，在 K_q 的剩余域中用同一个 i
表示。取

\[
 b_\gamma=\zeta^{41}\in\mathbf F_{q^2}^{\times}.
\tag{311.5}
\]

因 21·41≡1 mod43，

\[
 b_\gamma^{m_q}=\zeta,\qquad b_\gamma^{43}=1.
\tag{311.6}
\]

CRT 元 (1,b_γ) 在 L 上的限制正好是 R191/R305 的 γ。
为独立检查这点，取 A 的形式参数 t=−x/y。在 q 处，A 好超奇异；
[q](t) 的 mod q 首项次数为 q²。因此全部非零 q 挠点有
v_q(t(Q))=1/(q²−1)。由 CM 作用的线性项，

\[
 \frac{t([b]Q)}{t(Q)}\equiv b\pmod{\mathfrak Q}
 \qquad(b\in\mathbf F_{q^2}^{\times}).
\]

于是

\[
 T_Q=\prod_{h\in H_q}t([h]Q)\in L_q
\]

在 q 的赋值为 1/43；其在 (1,b_γ) 下的比值剩余恰为
b_γ^{m_q}=ζ。R191/R305 的 θ 也是同一局部循环扩张的一致化元，
并满足 γθ/θ≡ζ。tame 作用在一致化元上的这个剩余角色与所选
一致化元无关，而且在阶 43 的惯性群上单射，所以两个生成元相同。
这直接比较的是域自同构，没有添加一个正 Artin/逆 Artin 的猜测。

## 2. 一个不含自由实点选择的普通 Robert 单位

定义实际有限乘积

\[
 \mathscr R_q=
 \prod_{a\in\mathbf F_p^{\times}}
 \prod_{h\in H_q}
 v\bigl(P_2+[a]P+[h]Q\bigr).
\tag{311.7}
\]

这是 K(A[pq])/L 的实际 Norm，因此属于 L。
Robert 单位的模数为 (1+i)³pq，含多个不同素理想；
已发表的 Robert–Stark 单位性质给每个原始值以及此乘积为普通单位。
使用 (311.2) 的规范函数与 Robert 函数之间至多的单位根差不会改变整性；
下面的精确 Norm 恒等式则直接用 (311.2) 的规范同源分布来核准。

**实点选择没有留下一个 γ 相位。** A(R)[q] 的非零点彼此相差 F_q× 的
标量，而 F_q×⊂H_q，所以换一个非零实 Q 只重排 (311.7)。
同理，换一个非零实 P 被外层 F_p× 乘积吸收。
因此 P₂、同一个实 CM 直线和 (311.7) 已经固定了整个元素。
γ 的具体作用另外由 (311.5)–(311.6) 与 R191 的局部标记固定。

### 2.1 精确的 Norm 为一

规范 Kato–Siegel 分布关系对乘 q 同源给

\[
 \prod_{S\in A[q]}v(R+S)=v([q]R).
\tag{311.8}
\]

R185 §3.1 已对同一个 Δ¹⁰/ψ₁₁ 规范核过该分布：可能的全局公共符号
在奇数次数的 Norm 比中消失。这里的次数为 q²，仍为奇数。
因 q≡−1 mod4p，且 v(−R)=v(R)，对 R=P₂+[a]P 有
v([q]R)=v(R)。所以

\[
 \boxed{N_{L/F}\mathscr R_q=1.}
\tag{311.9}
\]

原来的底层单位准确为

\[
 u_0=\prod_{a\in\mathbf F_p^{\times}}v(P_2+[a]P),
\tag{311.10}
\]

即 R185、R219 的同一个 scalar Norm，没有新乘一个 m_q 或 44。
在 q 处，Q 的所有共轭都约化为原点；其余点保留非零的四挠部分。
故函数值在这里可直接约化，得到精确的剩余等式

\[
 \overline{\mathscr R_q}=\overline{u_0}^{m_q}.
\tag{311.11}
\]

若再选一个惰性辅助 r≡−1 mod172，用非零实 r 点及 H_r 定义相同的
双层乘积，便同时有两个 Norm 为一和
\(\overline{\mathscr R_{qr}}=\overline{\mathscr R_r}^{m_q}\) 等式。
这正是惰性双 ray 导数笔记使用的同一个完整 Robert 家族；
它的底层规范、两个 Norm 分支及局部 congruence 都在此处被固定。

### 2.2 精确的复共轭关系

τP=P、τQ=Q，而 τP₂=[i]P₂。
在 A:y²=x³−x 上，(311.2) 满足 v([i]R)=v(R)。
对 τ(311.7) 的每个点同时作 [−i]，再用 H_q 包含 −i 且对共轭稳定，
可将 q 因子重新排列，得到

\[
 \tau\mathscr R_q=\sigma^{22}\mathscr R_q.
\tag{311.12}
\]

因为在 F 上，CM 标量 −i 的类是唯一的阶二元 σ²²。
这一步使用完整普通单位，尚未模 43。

## 3. 原始导数的整数系数是 −7

沿用 R219，ω=8+25i∈F_{43²}，阶为 44。
令 a_j 为 15 Re(ωʲ) 的中心整数代表，并置

\[
 \Pi=\sum_{j=0}^{43}a_j\sigma^j,\qquad
 U=z^\Pi,\qquad E=\mathscr R_q^\Pi.
\tag{311.13}
\]

全部 a_j 仍是 R219 的原数组。特别

\[
 a_{-j}=a_j,\quad a_{j+22}=-a_j,\quad
 \tau E=E^{-1},\quad N_{L/F}E=1.
\tag{311.14}
\]

设 D=Σ_{j=0}^{42}jγʲ，并在 Kummer 模扩系数到 F_{43²} 后写
P_±=Σ_{j=0}^{43}ω^{±j}σʲ。
惰性双 ray 导数笔记 (E.1) 对本篇 (311.7)、(311.10) 的规范给

\[
 D\left(\frac{i}{1848}P_+[\mathscr R_q]\right)
 =32i\,d_0,
 \qquad
 d_0=\frac{i}{1848}P_+[u_0].
\tag{311.15}
\]

等式在 L 的模 43 Kummer 类中理解；全局导数代表与 D 之间相差的
43 倍 Hilbert 90 项在此消失。(311.9)–(311.11) 及其双层版本
说明这里确实是该笔记使用的家族，而不只是一个任选的 Norm-one 单位。
系数 32i 来自 2iλ_q，λ_q=16，保留原来的正 tame 方向。

R219 (219.12) 的底层标定是

\[
 P_+[u_0]=15iP_+[z].
\]

于是消去共同的 i/1848 后，

\[
 DP_+[\mathscr R_q]
 =32i\,P_+[u_0]
 =-480P_+[z]
 =36P_+[z]\pmod{43}.
\tag{311.16}
\]

对**系数环**作 Frobenius 共轭，得到
DP_−[𝓡_q]=36P_−[z]。此处是系数共轭，不是又对普通单位作 τ。
再用

\[
 \Pi\equiv\frac{15}{2}(P_++P_-)\pmod{43}
\]

得

\[
 \boxed{[E^D]=36[U]=-7[U]\quad\text{于 }L^\times/L^{\times43}.}
\tag{311.17}
\]

扩系数到 F_{43²} 是忠实的，所以最后已经返回普通 Kummer 模。
没有把形式的 i 系数当成一个普通整数幂；两共轭方向正是这样合并成
同一个真实整数 −7。

## 4. 唯一正实根与精确的上层 Norm

取中心导数

\[
 D_{\rm bal}=\sum_{j=-21}^{21}j\gamma^j.
\tag{311.18}
\]

它满足

\[
 D_{\rm bal}\equiv D\pmod{43\mathbf Z[\Gamma]},\qquad
 \tau D_{\rm bal}\tau=-D_{\rm bal},\qquad
 (\gamma-1)D_{\rm bal}=43\gamma^{22}-N_\Gamma.
\tag{311.19}
\]

由 (311.14)，E^{D_bal} 被 τ 固定。更具体地，在所固定的复嵌入下，

\[
 E^{D_{\rm bal}}
 =\prod_{j=1}^{21}\left|\gamma^jE\right|^{2j}>0.
\tag{311.20}
\]

R219 的 a_{−j}=a_j 和 σ²²z=1/z 同样给

\[
 U=z^{30}\prod_{j=1}^{21}|\sigma^jz|^{2a_j}>0.
\tag{311.21}
\]

由 (311.17)–(311.19)，U⁷E^{D_bal} 在 L 中是一个 43 次幂。
另一方面 μ₄₃∩L={1}：L 的绝对次数为 3784，不能含次数 42 的
Q(ζ₄₃)。因此这个 43 次根在 L 中唯一。它被 τ 固定，并且由
(311.20)–(311.21) 必为正。定义

\[
 \boxed{
 Y=\left(U^7E^{D_{\rm bal}}\right)_{\mathbf R_{>0}}^{1/43},
 \qquad X=Y^{37}/U^6.}
\tag{311.22}
\]

这不是“选一个使 Norm 正确的根”：右边先固定了一个复数中的正实根，
随后由 Kummer 等式证明它恰属于指定的实际域 L。
所有根式内部因子均为普通单位，所以 Y 的每个有限赋值为零。
因此 Y、X 都属于 O_L×∩L⁺。

取 Norm 得

\[
 (NY)^{43}=U^{7\cdot43},\qquad
 \boxed{NY=U^7},
\]

其中第二式再次使用 μ₄₃∩F={1}。最后

\[
 \boxed{NX=U^{7\cdot37-43\cdot6}=U.}
\tag{311.23}
\]

还可保留一个精确 Hilbert 90 检查式：由 (311.19) 和根的唯一性，

\[
 \frac{\gamma Y}{Y}=\gamma^{22}E,
 \qquad
 \frac{\gamma X}{X}=(\gamma^{22}E)^{37}.
\tag{311.24}
\]

本篇的证明给出这些全局恒等式；本次没有通过 R305 矩阵逐坐标重算它们。

## 5. 这是真正生成上层的混合单位

R219 已证明 [U] 在 F×/F×⁴³ 的忠实 χ、χ⁻¹ 分量非零。
若 σᵃγᵇ 固定 X，对 (311.23) 取 Norm 可得 σᵃU=U。
对该忠实非零分量投影便迫 44|a。
若再有 b≠0 mod43，则 γᵇ 生成 Γ，从而 X∈F；这将给 U=X⁴³，矛盾。
所以 X 在 Gal(L/K) 中的稳定子为一，

\[
 \boxed{K(X)=L,\qquad\mathbf Q(X)=L^+,\qquad
 [\mathbf Q(X):\mathbf Q]=1892.}
\tag{311.25}
\]

最后一步用 X 实、K 虚二次以及 [L:K]=1892。
这排除了把一个底域元素或 proper K-subfield 的单位 Norm 包装成忠实原像。

## 6. 已固定的局部根与仍未知的相位

对固定 q 素点，继续记

\[
 \ell(a)=\log_\zeta(\bar a^{m_q}).
\]

因为 Γ 全分歧，γʲE 的剩余值都相同；D_bal 的增广为零，故

\[
 \overline{E^{D_{\rm bal}}}=1,\qquad
 \overline{\sigma^jY}^{43}=\overline{\sigma^jU}^{7}.
\tag{311.26}
\]

设 β_j 是 σʲU 在 μ_{m_q} 中的唯一 43 次根；它由 R219 的局部
Norm 条件以及 gcd(43,m_q)=1 固定。则有唯一 t_j∈F₄₃ 使

\[
 \overline{\sigma^jY}=\beta_j^7\zeta^{t_j}.
\tag{311.27}
\]

这些 t_j **尚未求得**。全局正实根条件已经定义它们，但并没有执行
把该代数定义变成 q 剩余值的计算。
因 ℓ(σʲU)=0，R219 给

\[
 \boxed{
 \mathcal L=19\sum_{j=1}^{21}\operatorname{Im}(\omega^j)
          \ell(\sigma^jY)-3
 =12\sum_{j=1}^{21}\operatorname{Im}(\omega^j)t_j-3
 \pmod{43}.}
\tag{311.28}
\]

这里 19≡4·37、12≡19·m_q mod43。
在 R305 的基中若写 Y=Σy_nu_n，则 y_n∈O_F，且

\[
 \overline{\sigma^jY}
 =\frac1{43}\sum_{n=0}^{42}\overline{\sigma^jy_n}.
\tag{311.29}
\]

这些 y_n 也尚未计算。R305 给的是执行 (311.29) 的完整整环接口，
本篇给的是特定输入 Y 的全局表达式；两者之间的实际求值仍待完成。
由于 (311.22) 证明 X 是普通单位，该特定表达式本身没有外支撑。
若后续为方便执行改用非单位 Norm 原像，仍须保留 R200 的正号
基域 Artin 修正，不能沿用普通单位公式而丢掉外部素理想。

## 7. 真正运行的有限核验与未运行的内容

- [有限规范核验器](../scripts/verify_r311_robert_radical_normalization.py)
- [有限规范证书](../notes/r311_robert_radical_normalization_certificate.json)

```sh
python scripts/verify_r311_robert_radical_normalization.py \
  --certificate notes/r311_robert_radical_normalization_certificate.json
```

本次实际运行并通过的检查包括：同一个 q、ζ，b_γ=ζ⁴¹ 的精确 q 域
坐标和 b_γ^{m_q}=ζ；全部 44 个 Fourier 方向；Π 的反号与共轭关系；
中心导数全部 43 个系数；32i·15i≡−7；7·37−43·6=1。
证书逐项保留以下 false 字段：

```text
q_robert_product_evaluated
upper_norm_preimage_coordinates_computed
R305_norm_determinant_of_X_computed
q_residue_phases_computed
actual_L_computed
```

有限规范核验不能证明或冒充巨大 Robert 乘积已经执行；
根在 L 中的归属性与普通单位性来自 §§2–4 的数学证明。

## 8. 依赖与已核主来源

1. **R171、R191、R219、R305**：同一个已证明素数、Weil 根、射线域、
   σ/γ 标签、普通目标 U、原始 d₀ 的标定及正常整基。
2. **[惰性双 ray Robert 导数](../notes/2026-11-13-inert-ray-two-prime-robert-derivative.md)**，
   §§1–7、(E.1)：κ′q=2iλ_qd₀。该笔记已由两个实际 Euler 方向、
   Hilbert 90、有限—奇异关系、Chebotarev 和两行 Selmer 线性代数证明。
   本篇 §§1–3 固定其具体家族与全部比例，不调用一般未发表的导数定理。
3. A. J. Scholl, *An introduction to Kato's Euler systems* (1998),
   §1.2, Theorem1.2.1(iii)、其后 Remarks(iv),(v) 和证明，印刷 pp.384–386：
   规范函数的同源 Norm。这里使用精确分布，不仅比较除数。
   <https://www.dpmms.cam.ac.uk/~ajs1005/preprints/euler.pdf>
4. H. Oukhaba and S. Viguié, *On the Gras Conjecture for Imaginary
   Quadratic Fields*, Canadian Mathematical Bulletin **56** (2013), 148–160，
   §2 印刷 p.149 的多素模数单位性质，以及 §4 印刷 p.155 的 Robert–Stark
   关系与两种 Norm 分支；R163、R185 已核原函数与 (311.2) 的对应。
   <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0148F81E2EC11C708E2769B9AF48720C/S000843950000062Xa.pdf/on-the-gras-conjecture-for-imaginary-quadratic-fields.pdf>
