# R142 补篇：真子域协方差的单母格对角控制与准确矩复用

2026-11-26，visible-exact-astra-198c63d-20261126 / low_inverse。

**已证明的 pointwise PSD 上界及可执行 pure adapter。** 本篇不改变正在运行的 R142，不生成新的科学 manifest，不预报任何 ε 或速度结论。它给完整母格 D 和各真子域 σ 的可验证公式，使真子域 coefficient enclosure 可以使用母格一次准确矩；零行保留在原193维物理空间中。是否启用须依 R142 的完整实际结果决定。

## CD1. 同一对象与完整 source family

保持 [R142](R142-low193-parent-moment-continuation.md) 的同一比较 BVP、原155母格、1424细格、true physical lengths、97/96端点和193输出观察。实际原场、real δ family、independent even mean、五种原 source roles 不改。

在一个母格及一个 varying role 上，令 U(t,δ) 为原 balanced source matrix。它正是 GM 中的 actual source 左乘已规定的 exact dyadic balance；源列仍是原 Hilbert 输入的完整193列或128列。不是从 finite source support 截断未知解。

取得一个完整母格 entrywise absolute upper A=(a_ij)，每个 a_ij 为固定非负实数，且对母格每个物理点、原 full family 均有 |U_ij(t,δ)|≤a_ij。真子域由原 [CC 系数证明](R141-supplement-genuine-child-coefficients-and-unchanged-hybrid-sources.md) 逐闭合交段、signed assembly、hull 和 parent intersection 构造。它提供另一个 absolute upper B=(b_ij)；可逐 source entry 取两条有效 absolute upper 的较小者，保证

$$
 |U_{ij}(t,\delta)|\le b_{ij}\le a_{ij}
 \quad(t\hbox{ 在声明的完整 child},\ |\delta|\hbox{ 在原全族}).
 \tag{CD.1}
$$

这里交的是同一 source entry 的实数包围，不是对两个 PSD covariance 取 entrywise minimum。母/子 source 都必须对应同一个真实算子、同一比较生成元及同一原输入单位。

## CD2. 一个母格 D，零行也有准确资格

以全部原输入列定义

$$
 c_j=\sum_i a_{ij},\qquad
 q_i(A)=\sum_j a_{ij}c_j=(AA^{\mathsf T}{\bf1})_i.
 \tag{CD.2}
$$

选固定 directed upper 点 d_i≥q_i(A)，置 D=diag(d_i)。运算只需两次全列/全行求和，不必形成 AA^T。

若 d_i=0，则 0≤q_i(A)且

$$
 q_i(A)=\sum_j a_{ij}\sum_k a_{kj}\ge\sum_j a_{ij}^2,
$$

故 a_ij=0 对每一原列成立。于是对应 U 的整条输出行准确为零。特别是这也适用于某个 source role 的 independent-mean 输出恰为零；它不授别的 role 的 mean 为零。

记 J={i:d_i>0}。所有 PSD 论证先在 J 上进行，再在其余原坐标补零。源码仍保存193行和全部原输入列，没有删除 mean 坐标、端点或 source column。若 J 为空，则 U准确为零，D=0，不调用非零矩例程来给零源添加人工尾。

## CD3. 子域 σ 的完整 PSD 证明

同样以全部列计算 q_i(B)=(BB^T1)_i，并置

$$
 \sigma_{\rm exact}=
 \begin{cases}
 \max_{i\in J}q_i(B)/d_i,&J\ne\varnothing,\\
 0,&J=\varnothing .
 \end{cases}
 \tag{CD.3}
$$

(CD.1)–(CD.2) 给 0≤σ_exact≤1。对任意真实向量 x，

$$
 \begin{aligned}
 x^{\mathsf T}UU^{\mathsf T}x
 &=\|U^{\mathsf T}x\|^2\\
 &\le |x|^{\mathsf T}BB^{\mathsf T}|x|\\
 &\le \sum_i q_i(B)x_i^2
 \le \sigma_{\rm exact}x^{\mathsf T}Dx.
 \end{aligned}
$$

中间一式来自非负对称矩阵 P=BB^T 的恒等式

$$
 \sum_i(P{\bf1})_ix_i^2-|x|^{\mathsf T}P|x|
   =\frac12\sum_{i,k}P_{ik}(|x_i|-|x_k|)^2\ge0.
$$

因此对整个 child 及 full family，准确有

$$
 \boxed{\quad U(t,\delta)U(t,\delta)^{\mathsf T}
             \preceq \sigma D.\quad}
 \tag{CD.4}
$$

实现先向上计算每个 q_i(B)、比值和最大值 σ_hat。取 σ=min(1,σ_hat) 仍合法：
D 与 σ_hat D 都已分别证明包住同一个真实 covariance，而且它们是同一个 PSD D 的标量倍数。空 J 定义 σ=0；零 d_i 行必须另核整条 a_i 为零，不执行0/0。

这里没有据 interval matrix 的 entrywise 符号推断 PSD。也没有假定 source 随径向不变：D 与 σ 是它的 pointwise covariance majorant。

## CD4. 只缩放 Z、Y，原观察 U 与 true h 不缩

[GM/GI](R141-supplement-exact-cell-Green-moments-and-shared-output-covariances.md) 中，对固定同一 H/Q template，两个准确 source moment 映射 Z(V)、Y(V) 对 covariance V 线性。共享的 observation moment U 只依赖 H、Q，完全不依赖 source。

每个母格/role 只调用一次原 source_moments(template,D)，取得包含准确 Z(D)、Y(D) 的完整矩阵球。每个 child 以 directed arithmetic 形成

$$
 Z_{\rm child}=\sigma Z(D),\qquad
 Y_{\rm child}=\sigma Y(D),\qquad
 U_{\rm child}=U.
 \tag{CD.5}
$$

这不是断言浮点例程在两次调用中逐字线性，而是对其包围的准确线性映射应用 (CD.5)。因 σ为固定非负上界点，缩放后的矩阵球包住准确 moment(σD)。

原 packet 仍使用各 child 独立的 certified node carriers、真 h 和 h²。完整同格项仍为原 signed 两三角之和

$$
 h^2\{\operatorname{tr}(O_L I_L)+\operatorname{tr}Y
                 -2\langle L,Y\ell^{\mathsf T}\rangle_F\}.
 \tag{CD.6}
$$

不能只缩放这个 scalar 而遗留不一致的 I_L/I_R。adapter 同时由 (CD.5) 重建全部输入 covariances，再调用原 packet formula。O_L/O_R、完整193 atoms、shared A/B/K 和 point-stage 生命周期均不改变。任何 point certificate 仍须由实际 owner 完成自己的全部盒。

## CD5. 五源缓存和实际成本的准确边界

配套 [pure adapter](../scripts/fourfold_codazzi_low_centre_child_diagonal_moment_provider.py) 显式继承已发布 ParentMomentProvider，并显式接收原 WholeChildSignedCoefficientProvider；不 monkeypatch 原 module、context 或 generator。

- ordinary_raw_low_source 和 transformed_low_source 仍用原准确 constant-source covariance，缓存为 parent/count。
- true_coefficient_defect、low_second_kind_correction 和 centre_high0_return_source 各自有独立母格 A、D 及准确矩。
- 每一个 varying source 的 B、σ和缩放后的 moments 都以完整 child box 与 template token 缓存，不把较小 child 的 σ给 sibling 使用。
- 每条 source 的全部原列、真实 mean、family parameter 和 role 单位都保留；三个 role 不共用一个未经证明的尺度。
- 全零 source 直接给零 Z/Y，仍保同一个 observation U 和原193维格式。

按现155母格/1424细格且一个完整 defect pass 的静态计数，varying-source dense moment 调用从逐child1424次变为每parent至多155次；实际 child coefficients、各 frame 和原 Green 产品仍必须计算。完整后续 four-source pass 的两个 constant 与两个 varying roles 也各自最多每母格一次 moment。这个调用数不等于实测 wall-time，没有预称6小时内完成或减少实际内存。

## CD6. 不免费继承当前 GM covariance 的优劣

当前 GM 母格上界保留 M M^T 加完整 radius diagonal；本篇 D 则对整个 source absolute matrix 作对角控制。一般既不能断言 D≼V_GM，也不能断言 σD≼V_GM。因此本篇不能承诺 ε下降，更不提供尚未计算的 ε<1。

同样，真 child source enclosure 只收窄实际 A的包围；比较生成元仍是 H_parent/n。固定母格中点模型与真实径向场之间的确定性差不会因 source child 更细就消失。若它成为主导误差，应另建真正 child-midpoint comparison，并为新 BVP 支付新证明；不能改写旧 Green 的成功身份。

当前 R142 在运行，本篇未修改其任何 active script/manifest/workflow，未启动重叠科学。待其完整实际结果需要新界时，独立 owner 才能把这里的 pure provider 接入完整旧输入准入、真实 failed/complete 分支和逐结论保存规则。缺失的私有载体如需重新物化，仍须如实登记为新目标所需载体；任何旧成功目标不得重登记。
