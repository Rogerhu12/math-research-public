# R77：显式径向对称对象的主返回是半返回的准确平方

2026-11-12，visible-exact-astra-f6a2 / reproduce_newton。

**已证明的结构结论：** 对本课题显式对称化的 exact-affine 几何族，在同一物理角坐标及已经采用的两个分支约定下，回向半返回与前向半返回是同一个映射。因此完整主返回的自然实提升准确等于前向半返回的平方。结论不适用于此前只近似镜像的原始样条图，也不把一个完整返回的小残差自动转成半返回的小残差。

本结果减少真实流验证所需的不同半程，不代付其全部复域、根部连续性、参考误差、复合或参数预算。相关实际输入仍由 [R57](R57-real-parameter-N-tube-and-common-root.md)、[R59](R59-moving-phase-frame-complex-modulus-gate.md)、[R62](R62-moving-turn-actual-parameter-second-source.md)、[R68](R68-reference-coordinate-defect-flow.md) 和 [R75](R75-real-parameter-principal-return-regularity.md) 分别提供。

## 1. 对象与准确径向反射

使用明确施加偶奇投影的同一 affine 族，而不是把二进制 knots 的近似对称性当成恒等式。对每个固定参数，径向标量满足

$$
a(-r)=a(r),\quad \beta(-r,\theta)=\beta(r,\theta),\qquad
Z(-r)=-Z(r),\quad \gamma(-r,\theta)=-\gamma(r,\theta).
\tag{1}
$$

这些等式来自定义中的 (f(r)±f(−r))/2，因此在全部样条共同区间、其拼接点和参数的线性方向上准确成立。原始 affine 组合在投影前作出；没有把浮点物化的邻近控制点代入该定义。

在旋转柱坐标基底中，真实单位切向量为

$$
T=(-\cos\gamma\sin\beta,\ \cos\gamma\cos\beta,\ \sin\gamma),
\qquad F_\theta=aT.
\tag{2}
$$

令 P(T) 为先前定义的准确零均值角原函数。角原函数的存在、规范和无限 Fourier 定义保持不变。反射矩阵 S=diag(1,1,−1) 与角原函数交换，因为角导数与零均值规范均与 S 交换。由 (1)–(2)，

$$
F(-r,\theta)=S F(r,\theta),\qquad
F_r(-r,\theta)=-S F_r(r,\theta).
\tag{3}
$$

因此 X=F_r 的两个水平分量是 r 的奇函数，竖直分量是偶函数。柱坐标基底只依赖 θ，不改变这一径向奇偶性。无限原函数也包含在 (3) 中；本证明不以其有限 DFT 近似替换它。

同步目标的 a 与 E 均为偶函数。这里 E 是同一真实图规定的径向平均第一基本形式系数；(3) 使其准确为偶。因此

$$
K_0(r)=-\frac1{a(r)\sqrt{E(r)}}
\frac{d}{dr}\left(\frac{a'(r)}{\sqrt{E(r)}}\right)
\tag{4}
$$

也是偶函数。若正转折为 t>0，负转折准确为 −t；本条只给反射关系，转折的存在、唯一性及简单性仍须由各对象的证书支付。

## 2. 同一个真实移动框架中的奇偶性

以下采用已实现且由 R59 核对的变量，避免在改符号时另选法向或角坐标。记

$$
\begin{aligned}
b&=\beta,\quad c=\cos\gamma,\quad s=\sin\gamma,\quad
p=\beta_r,\quad q=\gamma_r,\quad u=\gamma_\theta,\\
h&=-\sin b\,X_1+\cos b\,X_2,\qquad
v=-\cos b\,X_1-\sin b\,X_2,\\
Q&=cX_3-sh,\qquad P=1+\beta_\theta,\\
D&=PcQ-uv,\qquad M=pcQ-qv,\qquad W=Q^2+v^2.
\end{aligned}
\tag{5}
$$

此处 Q 是移动框架分量；它不是下面转折正规化的 q_turn。由 (1) 和 (3) 可逐项得到：

| 关于 r 为偶 | 关于 r 为奇 |
|---|---|
| b,c,X₃,Q,P,q | s,h,v,p,u |

于是

$$
D(-r,\theta)=D(r,\theta),\quad
W(-r,\theta)=W(r,\theta),\quad
M(-r,\theta)=-M(r,\theta).
\tag{6}
$$

这也与真实未归一化二型系数及面积恒等式一致：

$$
N_{\rm raw}=-a^2D,\qquad M_{\rm raw}=-a^2M,\qquad
|F_r\times F_\theta|^2=a^2W.
\tag{7}
$$

源码 scripts/fourfold_phase_uniform_field_time_grid_fast.py 的 f_invariants 正是 (5)，不是只对径向背景成立的替代式。

## 3. 转折端点与两个场的准确关系

固定参数和同一正根 t，取 r=t sin τ，−π/2≤τ≤π/2。假设真实目标在内部满足 K₀<0，并令

$$
q_{\rm turn}(\tau,\theta)
=\frac{-K_0(t\sin\tau)}{\cos^2\tau}.
\tag{8}
$$

该量实际不依赖 θ。简单根给其两个端点的正规连续值；由 K₀ 偶性，q_turn 关于 τ 为偶，并在实区间选相同的正平方根。于是同一物理角 θ 的两个主场可写为

$$
f_\sigma(\tau,\theta)
=-t\cos\tau\frac{M}{D}
-\sigma t\cos^2\tau\sqrt{q_{\rm turn}}\frac{W}{D},
\qquad\sigma\in\{-1,+1\}.
\tag{9}
$$

这就是原来的 −r_τ(M+σ√(−K₀)W)/D；在实内部 cos τ≥0，不产生额外平方根符号。式 (9) 也明确给出两个端点 fσ=0，没有 0/0。D 非零和各解析域仍须按同一对象、同一参数、同一根部 germ 证明。

由 (6)、cos τ 的偶性和 q_turn 的偶性，准确有

$$
\boxed{f_{+}(-\tau,\theta)=-f_{-}(\tau,\theta).}
\tag{10}
$$

等式对固定物理角成立，**不包含 θ 的反射、平移或另一个 involution**。在已证明存在的共同复域上，它按解析延拓保持；这不自动授权扩大复域。

## 4. 实流、自然提升与平方恒等式

采用目前实际程序的准确分支约定：

- P：解 θ_τ=f₋(τ,θ)，从 τ=−π/2 到 τ=+π/2。
- B：解 θ_τ=f₊(τ,θ)，从 τ=+π/2 到 τ=−π/2。

令回程解 θ(τ) 的初值为 θ(+π/2)=θ₀，并定义 z(s)=θ(−s)。由 (10)，

$$
z_s=-f_+(-s,z)=f_-(s,z),\qquad z(-\pi/2)=\theta_0.
$$

在相同几何与角图上，ODE 唯一性立即给

$$
B(\theta_0)=z(+\pi/2)=P(\theta_0).
\tag{11}
$$

实流使用连续的物理角提升，不在端点取模；场的周期是 π/2。因此 P(θ+π/2)=P(θ)+π/2，而 (11) 是实提升之间的等式。整个主返回 R 先作 P，再作 B，所以

$$
\boxed{R=P\circ P.}
\tag{12}
$$

规范角 x=4θ 下，写 p(x)=4P(x/4)、r(x)=4R(x/4)，则同样准确有 r=p∘p。这里没有缺少一个整圈常数。

参数固定时，只需真流在所用域存在且唯一；在 R75 的参数正则合同下，平方关系也可直接求导。例如

$$
r_x(x)=p_x(p(x))p_x(x),\qquad
r_\delta(x)=p_x(p(x))p_\delta(x)+p_\delta(p(x)).
\tag{13}
$$

这些是准确链式公式；各实际导数及其域界仍需证明，不能把公式当作数值横截界。

## 5. 如何用于现有参考及严格复合

已保存的前向参考以 H(x)/4 为起点。它的规范终点 A(x)=p(H(x)) 并不是 p(x)。因此不能简单计算 A∘A。若同一个 H 的准确局部逆在所需复域成立，定义 C=H⁻¹∘A，则

$$
r\circ H=A\circ H^{-1}\circ A=H\circ C\circ C.
\tag{14}
$$

这正是以后只付前向真场，再在同一标签图中作准确复合时应使用的关系。H⁻¹ 的分支、两次像域、参考接缝、最终 Fourier 或 Wiener 费用均须保留。

一个直接误差合同是：若同域上的前向近似 p̂ 满足 |p−p̂|≤ε，p(x)、p̂(x) 及连接线段都落在已付的下一次输入域，并且该线段上 |p̂′|≤L，则

$$
|p(p(x))-\widehat p(\widehat p(x))|\le(1+L)\varepsilon.
\tag{15}
$$

证明是加减 p̂(p(x))。它不要求半返回先满足某个近共轭关系；其所需的像域与 L 也不能免费从实节点推得。复带到 Wiener 的转换仍按已付内带余量进行。

同样，单凭 r∘H≈H(·+α)，不能无预算地反推 p∘H≈H(·+α/2)。即使在圆周层面，给定一个旋转的平方也有两个不同的半旋转选择；这里的自然实提升还必须与未取模的真实 ODE 路径相容。

## 6. 当前 δ₅ 的独立有限端点预测

另存独立输入包 data/phase_ring_continuation/step5_forward549_exact_reference_package.npz.gz，包含最后一段全部八个 U/L、Q 控制、准确 Q_forward,end、整数初始修正和原始完整 JSON 身份。SHA256 为 ddfaf470a6d64badee122b637c8ce6234db379f8f1da1473db431eced2fa16a7。它从已逐字恢复的完整前向参考提取，不重新选系数。

使用准确的有限函数

$$
Y_{\rm ref,end}(x)=x/4+U_{4f,\rm end}(x)+Q_{f,\rm end}(x)a(x),
\qquad a=H_5/4-Y_{4f,\rm start},
\tag{16}
$$

保留乘积全部 644 个正频率，脚本 scripts/fourfold_half_return_predictor.py 对

$$
\rho_5=\frac{15121+\sqrt5}{27422},\qquad
d_0=\pi\rho_5,\quad d_1=d_0+\pi
$$

分别计算完整有限残差 4Y_ref,end−H₅(·+dⱼ)。d₀≈1.73258869993663132832，而有限终点的平均增量约为 1.73258869993392123609。对 d₀，实际有向有限 Wiener 上界为：

| 标签带宽 | 完整有限预测的 A_s 上界 |
|---|---:|
| 0 | 2.768×10⁻¹¹ |
| 1/512 | 3.003×10⁻¹¹ |
| 1/256 | 3.480×10⁻¹¹ |
| 1/128 | 6.939×10⁻¹¹ |

另一圆周半旋转选择 d₁ 的平均残差约为 −3.14159265359250333069。故当前**有限参考预测**选择 d₀，且不含额外 π；这不是通过完整返回的小残差推断得到的。实际 ODE 提升的最终数值确认仍要把同一 δ₅ 前向的真实缺陷校正纳入。

报告为 notes/2026-11-12-step5-half-return-finite-prediction.json。全部数字只涉及所保存的明确有限函数、准确二次无理旋转和有向算术；不包含 δ₅ 的真实流残差，不把 Q_retarget 宣称为准确变分 Jacobian，也不宣称半返回共轭已经成立。

本结构证明不终结主目标；它允许后续严格工作将不同真实场的验证范围缩到前向半程，再准确复合。

