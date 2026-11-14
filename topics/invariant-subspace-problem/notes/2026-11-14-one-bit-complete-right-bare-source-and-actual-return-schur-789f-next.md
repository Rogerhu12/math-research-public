# 同一加位源的普通右链、bare 商与真正高返回 Schur

日期：2026-11-14（UTC）。作者：Astra-ISP boundary_core / 789f；AI-assisted，GPT-6 Astra Pro。

状态：完整右链的一位 Gram、同一个实际边界源、full-to-bare 源映射及高返回 Schur 全部已证明。本文把 [joined 左加 bare 稿](2026-11-14-one-bit-joined-left-bare-quotient-gram-and-source-schur-789f-next.md) 接到原普通右 \(G\) 和 flat 形式，未证明高返回 Schur 的所需窗口上界。

沿用该稿的原头 \(A=VJ_dV^{-1}\)、原尾 \(D\)、新增位权 \(a>0\)、短核
\(E_h^{(p)}\)、投影 \(P_h^{(p)},Q_h^{(p)}\)、完整 \(R_{h,p}\) 和
\(\mathcal P(z)=\sum_{j<d}(Ve_j)(-z)^j\)。
所有普通右链都保留原逐头、逐孔短核旗。

## 0. 固定原孔截止、共同定义域与闭性

本文的完整算子结论针对原无限正尾 \(b\in\ell^1\) 以及固定的 \(q,d,a\)。
所有尾输入只使用孔层
\[
0\le p\le P_*:=q+d.
\]
这仍是无限维 Hilbert 空间，但只含有限个孔层；绝不在全孔直和上假定 \(D^\dagger\) 有界。

[已证 R279 §2.3](../results/R279-bosonic-affine-primitive-gram-transfer-and-low-occupation-bounds.md)
给每个这样的完整层一个有界右逆。具体地，选至少 \(2P_*-1\) 个正权物理位为有限块 \(I\)；
令 \(R_I\) 为其第 \(0,\ldots,P_*-1\) 输入层上单步最小右逆的直和，
\(D_{\rm out}=D_{I^c}\)。在总孔层 \(p-1\) 上，
\[
\mathcal R_p
=R_I\sum_{\ell=0}^{p-1}(-D_{\rm out}R_I)^\ell,
\qquad D\mathcal R_p=I.
\]
外孔每次减少一，故最后余项严格为零。组合这些右逆，得到本稿全部
\(D^h:\mathcal H_p\to\mathcal H_{p-h}\) 的满射性和有界 MP；
\(p<h\) 的零目标约定相应提升为零。加入一位后的 \(D_a\) 同样满足这一结论。
因此所有出现的 \(R_{h,p}\)、\(R_d\)、\(\mathsf R_q^{\rm hi}\)
在本稿指定的完整固定层域上处处有界。常数可以依赖 \(q,d\)，没有全孔统一断言。

原实际新边界源是闭空间
\[
\mathscr R_{a,q}
=\bigoplus_{i=0}^{d-2}
e_i\bigl(\ker D_a^{\,d-i-1}\cap\mathcal H_{a,q}\bigr).
\]
本文的源算子都以这个同一空间为目标。其满射不是仅由“取实际值域”宣告的：
对 \(r\in\mathscr R_{a,q}\)，置 \(r'=V^{-1}r\)，在新未来首头层取
\[
f_{q+j}=(-1)^j
(D_a^j:\mathcal H_{a,q+j}\to\mathcal H_{a,q})^\dagger r'_{j-1},
\qquad 1\le j<d,
\]
其余层为零。上三角的 \(V^{-1}\) 保留源旗，
所以 \(r'_{j-1}\in\ker D_a^{d-j}\)。以上 \(f_{q+j}\)
属于 \(E_{a,d}\cap E_{a,j}^{\perp}\)，且边界公式准确输出 \(r\)。
这是完整右源的有界右逆；再取真正 bare 商，得到同一个 bare 源的有界右逆。
故下文的源 Gram 都是在 \(\mathscr R_{a,q}\) 上的有界正可逆算子。

另外，完整首头参数 \((x-aR_dy,y)\) 中，
\(x\in E_d\) 与 \(R_dy\perp E_d\) 正交。因此其物理范数不小于
\(\|(x,y)\|\)；(1.3) 的完整链有同一下界。
裸源中的 \(G_{h,p}(a)\) 在每个固定层满足
\[
G_{h,p}(a)\succeq (1+a^2\|R_{h,p}\|^2)^{-1}I.
\]
有限个层的最小值为正。结合其可逆的首头读出，裸链 Gram 也有严格下界。
这些事实将同时用于 (1.4)、(2.2) 和 (4.1)--(4.4)，不在各式之间改变完成空间。

### 0.1 不把固定层结论误用为一般无界逆结论

若改用尚未证明上述满射的抽象 \(D\)，则每个提升必须先取自然图域
\[
\mathfrak D_{h,p}
=\{v\in E_h^{(p-1)}:
D^{h-1}v\in\operatorname{Ran}
(D^h:\mathcal H_p\to\mathcal H_{p-h})\}.
\]
\(R_{h,p}\) 是此域上的闭最小提升；全部公式必须限在所出现这些图域的共同交中。
不能仅由 \(v\in E_h\) 宣称 \(R_{h,p}v\) 已定义，
也不能把全孔直和上的 \(D^\dagger\) 当成有界算子。
本文不对这样的抽象 \(D\) 宣称处处有界的 (1.3)--(4.4)。

不依赖坐标逆的本义，是在同一个物理可行纤维上定义能量
\[
\mathfrak h_{\rm ret}(z)
=\inf\{\|c\|^2:
c\text{ 为完整右可行链，且其 bare 首源为 }z\}.
\]
无可行提升时取 \(+\infty\)。若相关高零源像尚未证明闭，
必须保留此下确界，或在距离公式中投影到该像的闭包；
不得提前把它写成达到的最小值或有界 Schur 逆。
在本稿原固定层模型中，前面的满射、下界及下文的闭核论证
已经排除了这些定义域问题，因而普通有界算子公式与该能量定义完全一致。

## 1. 完整未来 first-head 源与一位物理 Gram

对旧切口 \(q\)，置

\[
 F_{R,q}^{\rm full}=\bigoplus_{j=1}^{d}E_d^{(q+j)},\qquad
 T_{R,q}^{\rm full}f
   =P_{>q}^{\rm head}\mathcal P(D)f.
\tag{1.1}
\]

这是 [R239 §6](../results/R239-appendix-first-physical-head-quotient-gram-for-left-plus-bare.md)
的完整原右链参数化。它有有界逆，逆就是第零物理头，且保全部内部零输出、末段封口和原输入旗。

新增位总孔切口 \(q\) 对应旧空分支 \(q\)、旧占据分支 \(q-1\)。
对

\[
 x\in F_{R,q}^{\rm full},\qquad
 y\in F_{R,q-1}^{\rm full},
\]

逐层定义
\[
 R_dy=d(D^d)^\dagger D^{d-1}y,
\qquad
 K_q^{\rm raw}y=\mathcal P'(D)y-\mathcal P(D)R_dy,
\]
\[
 K_{R,q}y=P_{>q}^{\rm head}K_q^{\rm raw}y.
\tag{1.2}
\]

原新 first-head 源为 \((x-aR_dy,y)\)，所以整个普通完整右链准确为

\[
 \boxed{
 \mathcal T_a^{\rm full}(x,y)
 =\bigl(T_{R,q}^{\rm full}x+aK_{R,q}y,\
          T_{R,q-1}^{\rm full}y\bigr).}
\tag{1.3}
\]

其物理 Gram 为

\[
 \boxed{
 \mathbb H_a^{\rm full}=
 \begin{pmatrix}
 H_q&a(T_{R,q}^{\rm full})^*K_{R,q}\\
 aK_{R,q}^*T_{R,q}^{\rm full}
     &H_{q-1}+a^2K_{R,q}^*K_{R,q}
 \end{pmatrix},\qquad
 H_q=(T_{R,q}^{\rm full})^*T_{R,q}^{\rm full}.}
\tag{1.4}
\]

这里没有未来短核商，因此不能把 joined 稿的
\(\mathsf G_q(a)\) 或 \(\mathsf K_q\) 直接替入 (1.4)。

给定下源 \(y\)，对完整旧上右源作 Schur 后的余项为

\[
 H_{q-1}
 +a^2K_{R,q}^*(I-\Pi_{R,q}^{\rm full})K_{R,q},
\tag{1.5}
\]

其中 \(\Pi_{R,q}^{\rm full}\) 是旧完整右链像的物理正交投影。

## 2. 同一个实际边界源

把 (1.3) 的原 full kernel 在左侧补出
\(\mathcal P(D_a)(x-aR_dy,y)\)，以左端
\(r=A v_q=-D_a c_1\) 为源方向。定义

\[
 \mathcal B_{R,q}^{\rm full}x
       =A(\mathcal P(D)x)_q,\qquad
 \mathcal C_{R,q}y=A(K_q^{\rm raw}y)_q.
\]

于是

\[
 \boxed{
 \mathcal B_a^{\rm full}(x,y)
 =\bigl(\mathcal B_{R,q}^{\rm full}x
                   +a\mathcal C_{R,q}y,\
          \mathcal B_{R,q-1}^{\rm full}y\bigr).}
\tag{2.1}
\]

若沿用右链输出 \(Dc_1\) 的相反号规范，全部源映射共同乘 \(-1\)；
下列正 Gram 和 flat 形式不变。

这是 joined 稿读取的同一个物理边界源。
普通完整右源 Gram 因而为

\[
 \boxed{
 G_a=\mathcal B_a^{\rm full}
       (\mathbb H_a^{\rm full})^{-1}
          (\mathcal B_a^{\rm full})^*.}
\tag{2.2}
\]

所有源算子都取在 §0 已证明闭且满射的同一个实际新源 \(\mathscr R_{a,q}\) 上，不把目标空间未经证明地换成两个旧源空间的直和。

## 3. 完整右 first-head 到 bare first-head 的真实源映射

置

\[
 F_{R,q}^{\rm bare}
  =\bigoplus_{j=1}^{d}
      \bigl(E_d^{(q+j)}\ominus E_{j-1}^{(q+j)}\bigr).
\]

记 \(\mathsf Q_{R,q}\) 为逐未来层的 \(Q_{j-1}\)，并定义
\(\mathsf R_q^{\rm hi}\) 从占据旧未来层 \(p-1=(q-1)+j\) 到空分支新层
\(p=q+j\)，逐层为

\[
 R_{j-1,p}P_{j-1}^{(p-1)}.
\]

完整源对 \((x,y)\) 的 bare 首源坐标准确为

\[
 \boxed{
 \mathfrak J_a(x,y)=
 \bigl(\mathsf Q_{R,q}x+a\mathsf R_q^{\rm hi}y,\
        \mathsf Q_{R,q-1}y\bigr).}
\tag{3.1}
\]

以下写清这里的顶边抵消，不能将 \(Q_hR_dy\) 直接删掉。
逐层取 \(h=j-1\le d-1\)，把物理首头
\((x-aR_dy,y)\) 代入 joined 稿的商坐标，首先得到的是
\[
z=Q_hx-aQ_hR_dy+aR_hP_hy,\qquad w=Q_hy.
\tag{3.1a}
\]
而 joined 稿的规范参数 \((x_b,w)\) 并不直接等于 \((z,w)\)：
其可行列本身含完整顶边修正 \(-\mathcal P(D)R_dw\)，
第零物理头的商坐标为
\[
z=x_b-aQ_hR_dw .
\tag{3.1b}
\]
由于 \(h\le d-1\)，\(P_hy\in\ker D^{d-1}\)，故
\(R_dP_hy=0\) 以及 \(R_dw=R_dy\)。将 (3.1a) 代入 (3.1b)，准确得到
\[
x_b=z+aQ_hR_dw=Q_hx+aR_hP_hy,
\]
这才是 (3.1)。特别 \(R_dy\perp E_d\supset E_h\) 时
\(Q_hR_dy=R_dy\)，该项通常非零；消去发生在两个真实首源规范之间，
不是一个额外的核投影估计。

\(\mathfrak J_a\) 满射；将两个旧 bare 最小代表原样嵌入 full 源，得到一个明确有界右逆

\[
 \mathfrak I_a(z_0,z_1)=(z_0,z_1),\qquad
 \mathfrak J_a\mathfrak I_a=I.
\tag{3.2}
\]

虽然这个右逆写作自然包含，\(\mathfrak J_a\) 自身并非正交块投影：它保留
\(aR_{j-1}P_{j-1}\) 的真实交叉。

令 \(\mathsf Q_a^{\rm phys}\) 为新完整右物理空间中，逐未来层对
\(E_{a,j-1}\) 的正交最小代表投影。定义

\[
 T_a^{\rm bare}
 =\mathsf Q_a^{\rm phys}\mathcal T_a^{\rm full}\mathfrak I_a.
\]

完整旗的下降与原内部方程给

\[
 \boxed{
 \mathsf Q_a^{\rm phys}\mathcal T_a^{\rm full}
     =T_a^{\rm bare}\mathfrak J_a.}
\tag{3.3}
\]

其 Gram \(H_a^{\rm bare}=(T_a^{\rm bare})^*T_a^{\rm bare}\)
就是 joined 稿限制到未来源后的真实右 bare Gram；可以用该稿的
\(\mathsf G_q,\mathsf K_q\) 计算同一个式子。

高 first-head 旗被边界源杀掉，故同一个实际边界源严格分解为

\[
 \boxed{
 \mathcal B_a^{\rm full}
    =\mathcal B_a^{\rm bare}\mathfrak J_a,\qquad
 \mathcal B_a^{\rm bare}
    =\mathcal B_a^{\rm full}\mathfrak I_a.}
\tag{3.4}
\]

## 4. 真正的高返回 Schur：不能把两个取商次序交换

令

\[
 \mathcal N_a=\ker\mathfrak J_a,\qquad
 \mathcal W_a=\mathcal T_a^{\rm full}\mathcal N_a.
\]

由 §0，\(\mathfrak J_a\) 有界，所以 \(\mathcal N_a\) 是闭子空间；
\(\mathcal T_a^{\rm full}\) 是有界且有下界的映射，故 \(\mathcal W_a\) 闭；
由 (3.3)，它完全位于新物理高返回空间
\(\ker\mathsf Q_a^{\rm phys}\) 中。记其正交投影为 \(\Pi_{\mathcal W_a}\)，并置

\[
 H_a^{\rm ret}
 =(I-\mathsf Q_a^{\rm phys})
                \mathcal T_a^{\rm full}\mathfrak I_a,
\]
\[
 \boxed{
 E_a^{\rm ret}
 =(H_a^{\rm ret})^*(I-\Pi_{\mathcal W_a})H_a^{\rm ret}
 \succeq0.}
\tag{4.1}
\]

固定同一个 bare 首源 \(z\)，全部完整提升为
\(\mathfrak I_az+n\)、\(n\in\mathcal N_a\)。低、高物理分量正交，故

\[
 \boxed{
 \inf_{\mathfrak J_a f=z}
       \|\mathcal T_a^{\rm full}f\|^2
   =\langle(H_a^{\rm bare}+E_a^{\rm ret})z,z\rangle.}
\tag{4.2}
\]

这是“先取完整右核，再对其高返回零源取商”的真实度量。
环境物理空间先取 bare 商的度量只是 \(H_a^{\rm bare}\)。
两者的准确差额为 (4.1)，不能把它删掉。

由 (3.4) 和同一源的二次最小化，

\[
 \boxed{
 B_a^{-1}
  =\mathcal B_a^{\rm bare}(H_a^{\rm bare})^{-1}
                  (\mathcal B_a^{\rm bare})^*,}
\tag{4.3}
\]

\[
 \boxed{
 G_a
  =\mathcal B_a^{\rm bare}
       (H_a^{\rm bare}+E_a^{\rm ret})^{-1}
                  (\mathcal B_a^{\rm bare})^*.}
\tag{4.4}
\]

因此 (4.4) 与完整一位公式 (2.2) 完全等价，且现在和 bare 项位于同一个首源空间中。

## 5. 原 flat 与允许使用的准确充分条件

原左费 \(L_a\) 由 joined 稿的同源左块确定；
原两个费用仍严格为

\[
 \alpha_a(r)^2=\langle B_ar,r\rangle,\qquad
 \lambda_{\rm flat,a}(r)^2
   =\langle G_aL_ar,L_ar\rangle,
\]
\[
 \boxed{\Xi_a(r)^2
  =\langle(B_a+L_aG_aL_a)r,r\rangle.}
\tag{5.1}
\]

(4.4) 已将其完整右因子写到同一 bare 首源中；没有交换 \(L_a,G_a\) 的次序。

例如，如果在所需实际源的 bare 最小首源 \(z_r\) 上真正证明

\[
 \langle E_a^{\rm ret}z_r,z_r\rangle
       \le c\,\langle H_a^{\rm bare}z_r,z_r\rangle,
\tag{5.2}
\]

则 (4.2) 立即给同一个 \(r\) 的

\[
 \lambda_a(r)^2\le(1+c)\alpha_a(r)^2.
\tag{5.3}
\]

又完整源 Cauchy--Schwarz 精确给

\[
 \mu_a(r)^2=\langle L_ar,r\rangle
 \le\lambda_{\rm flat,a}(r)\lambda_a(r),
\]

从而

\[
 \mu_a(r)^2
 \le\frac{\sqrt{1+c}}2
       \bigl(\alpha_a(r)^2+\lambda_{\rm flat,a}(r)^2\bigr).
\tag{5.4}
\]

本文没有证明原高孔源上的 (5.2)。旧的全头 \(\Psi_{d,m}\) 估计给的是一个可能过大的全源版本；新的局部 phase 界也不能未经源识别直接代入 (5.2)。

## 6. 真实高返回在 bosonic 中的位置，以及已知的必要范围限制

在完整 bosonic 嵌入中，令 \(N_0\) 为集体模式占据、
\(N_\perp=N_{\rm total}-N_0\) 为横向总粒子数。原新第 \(j\) 个未来层的高旗
\(E_{j-1,q+j}\) 恰是原平方自由空间中满足

\[
 N_0\le j-2
 \quad\Longleftrightarrow\quad N_\perp\ge q+2
\]

的向量。因此，若 \(\mathscr C_{\rm flag}\) 表示同一个有限物理孔截止及全部原输入头旗，则准确为

\[
 \boxed{
 \text{原高返回空间}
 =\mathscr C_{\rm flag}\cap\mathcal H_{\rm hc}
                       \cap\{N_\perp\ge q+2\}.}
\tag{6.1}
\]

这里没有删掉逐段的头旗。对同一个截止内的真实完整环境核，这些原右输入头旗由完整 first-head 参数化自动保持。

对真实环境核 \(\mathcal K=\ker(A+D)\)，零占据重构与 \(N_\perp\) 交换。
故沿同一截止，其真正高零源的零模像是
\(\mathcal Z_A\cap\{N_\perp\ge q+2\}\)，其中 \(\mathcal Z_A\) 必须是实际平方自由可达像，不能替成全部横向 Fock 空间。

这把 (4.1) 化为一个明确的原硬核像／横向次数旗的角度问题，但不会自动消去该角度。

特别，已有
[R271 回文四头反例 §§1–5](../results/R271-appendix-palindromic-four-head-actual-minimal-sources-and-two-form-nonuniformity.md)
严格排除“仅用头上零模重构常数即可免费支付 (4.1)”这一更强命题。
该真实有限模型有 \(d=4,q=1\)、\(\|A_\varepsilon\|\) 一致有界、
\(S=3+8t^6\to3\)，故
\[
 C(A_\varepsilon,S)=
 \sum_{j<4}\|A_\varepsilon^j\|^2/(S^j j!)
\]
一致有界；但同一个实际源上
\[
 \mu_t^2=1,\quad
 \lambda_t^2\sim\frac{65}{12852}t^{-4},\quad
 \alpha_t^2\sim\frac4{8505}t^{-2},
\]
所以
\[
 \boxed{
 \frac{\mu_t^2+\lambda_t^2}{\mu_t^2+\alpha_t^2}
 \sim\frac{2925}{272}t^{-2}\longrightarrow\infty.}
\tag{6.2}
\]

这是既有实际反例对当前接口的范围说明，不是新造一个有限模型。
它不是原固定 \(A_m\)、不是原连续尾，也不满足原实际规范源的全部条件。
因此它不排除利用这些额外条件控制 (4.1)，但必须防止把完整真核的 head-only 预算直接当作未来 bare 的修复预算。

本文完成的是同一个加位源下 \(L,B,G,LGL\) 的准确接线及真正未付的正返回块；原 \(N=M\) 仍取决于该实际返回块或等价的固定测试 Schur 预算。
