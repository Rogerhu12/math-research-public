# R688：实际 CM 商的坏处高度化为分量度数与交数矩阵

日期：2026-11-14。状态：**下述计算结构已证明；没有计算出本题在 2、3 处的实际分量矩阵，也没有据此声称 Ω=0 或统一排除。**

保持 R593/R596/R634 的同一个商、极化、完整 Picard 修正、清分母及基点截面。本篇给出实际 Ω 的一个有限有理线性代数接口：在 2、3 处，先取使 CM 商好约化的有限扩张；随后只需曲线半稳定模型的交数矩阵及商线丛在各分量上的度数。**此处不需要先计算 η_h 的坐标或固定线性泛函 ℓ_h 的高度值。**

## 1. 实际对象与本篇不变的归一化

令 X=X_1、Y=W_p、φ:X→Y、c_0、q:J_X→A、f(x)=q[x−c_0]，均为 R593 的实际正 CM 型 Ψθκ_4 所给对象。令 λ_A 是其中固定的甲板不变极化，

\[
F=\operatorname{End}_{\mathbb Q}^0(A),\qquad
\kappa=qq^\dagger,\qquad
F^0=\{h\in F:\operatorname{Tr}_{F/\mathbb Q}(\kappa h)=0\}.
\tag{688.1}
\]

对 h∈F，记原点刚性化的对称有理线丛为 L_h，满足 λ_{L_h}=λ_Ah。对 h∈F^0，R593 给出

\[
f^*L_h=\phi^*\eta_h\in\operatorname{Pic}^0(X)\otimes\mathbb Q,
\]
\[
\mathscr L_h=q^*L_h\otimes\phi_*^*\lambda_Y(\eta_h),
\qquad \iota^*\mathscr L_h=0.
\tag{688.2}
\]

这里 ι(x)=[x−c_0]。完全沿用 R593 的真实整数 C_h、线丛 N_h 和唯一截面 s_h：

\[
\mathscr N_h=\mathscr L_h^{\otimes C_h},\qquad
s_h\text{ 无零},\qquad s_h(c_0)=1.
\tag{688.3}
\]

允许为有限个 h 同时取 C_h 的公倍数；所有高度必须除回相同倍数。因此这只改变计算表示，不改变实际局部函数

\[
\lambda_{q_0,h}(x)=C_h^{-1}v_{\mathscr N_h,q_0}(s_h(x)).
\tag{688.4}
\]

用 q_0 表示坏处素数，以免和商映射 q 混淆；下文 q_0≠p。规范保持 v_{q_0}(q_0)=1。最终只在 q_0=2,3 使用。

## 2. CM 商潜在好约化与模型输入

实际 A 有 CM，因此在每个 q_0 潜在好约化。可直接由 Tate 模看出这一点：有限扩张后所有 CM 自同态定义且 A 半稳定；其辅助 r 进 Tate 模是 CM 代数 E⊗Q_r 上的秩一模。惯性此时单幂且与 E 交换，而有限 étale Q_r 代数中的乘法算子半单；同时半单、单幂的算子为一。Néron–Ogg–Shafarevich 判据遂给好约化。这里 r≠q_0；没有把 A 的好约化推成 X 的好约化。

取有限 K/Q_{q_0}，满足：

1. A_K 有阿贝尔概形模型 \(\mathcal A/\mathcal O_K\)；
2. X_K 有分裂半稳定正则模型 \(\mathcal X/\mathcal O_K\)；
3. 必要的线丛及分量均在该模型上定义。

令 e=e(K/Q_{q_0})，并取 ord_K(π_K)=1，故 ord_K=e v_{q_0}。令特殊纤维的几何不可约分量为 C_v，v∈V。这里各分量的重数为一。

Abel 商映射 f 延拓到 \(\bar f:\mathcal X\to\mathcal A\)。只需要标准的曲面情形：Néron 映射性质先在光滑部分给延拓；不定点仅可能在有限个结点。对正则曲面的不定点作点爆破消去后，每条例外曲线是有理曲线，而从有理曲线到阿贝尔簇的映射恒定。每个连通例外纤维均被缩为一点，故映射下降到原来的正规曲面。也可以只先在光滑部分拉回线丛，再利用正则曲面删除有限余维二点不改变 Picard 群来定义同一个延拓。

令 \(\overline L_h\in\operatorname{Pic}(\mathcal A)\otimes\mathbb Q\) 为沿原点刚性化的立方延拓，定义

\[
\mathcal M_h=\bar f^*\overline L_h,\qquad
d_v(h)=\deg(\mathcal M_h|_{C_v})\in\mathbb Q.
\tag{688.5}
\]

好约化阿贝尔簇的规范非 p 度量就是这个模型度量。因而 (688.5) 中的度数属于实际规范度量的数据，不是任意选取某个延拓的度数。

若 C 同时清除所用 L_h，则 C d_v(h)∈Z。平坦族中度数守恒给

\[
\sum_{v\in V}d_v(h)=\deg f^*L_h
=\operatorname{Tr}_{F/\mathbb Q}(\kappa h).
\tag{688.6}
\]

所以对 h∈F^0，右侧为零。

原始来源：Serre–Tate, *Good Reduction of Abelian Varieties*, §3，及其 Néron–Ogg–Shafarevich 判据：
<https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf>。
关于规范度量的模型性质，Besser–Müller–Srinivasan (BMS), Remark 2.12、Proposition 2.9：
<https://arxiv.org/pdf/2112.03873>。

## 3. 交数方程与实际局部值

令

\[
I=(C_v\cdot C_w)_{v,w\in V}.
\tag{688.7}
\]

这是正则模型上的交数矩阵，非对角元非负，行和为零。连通性给 ker(I)=Q·1；其在总和零空间上负定。设 v_0 是 c_0 的截面所落的分量。

**定理 688.1（完整修正高度的图方程）。** 对 h∈F^0，唯一有理向量 a(h) 满足

\[
\boxed{I\,a(h)=d(h),\qquad a_{v_0}(h)=0.}
\tag{688.8}
\]

对 x∈X(Q_{q_0})⊂X(K)，其截面在正则半稳定模型的光滑部分约化到唯一分量 v(x)，且

\[
\boxed{\lambda_{q_0,h}(x)=\frac{a_{v(x)}(h)}e.}
\tag{688.9}
\]

公式没有额外的未知常数，也没有残留 C_h 倍数。按 R593 归一化，a_{v_0}=0 正好对应 λ_{q_0,h}(c_0)=0。

### 证明

先清分母，最后除回。由于 (688.6)，线性方程有解且仅差常向量；基点条件固定它。

令 \(V_h=\sum_v a_v(h)C_v\)。方程等价于

\[
\deg\bigl((\mathcal M_h(-V_h))|_{C_v}\bigr)=0
\quad\text{对全部 }v.
\tag{688.10}
\]

在光滑曲线的次数零线丛上，Néron 度量由多次数零的有理延拓计算，至多差常数。更准确地，若 D 是泛纤维上次数零除子，D 的水平闭包为 \(\overline D\)，且

\[
Iu=((\overline D\cdot C_v))_v,
\]

则对不交支撑的次数零零维循环 z，Néron 配对为

\[
\langle z,D\rangle_K
=\overline z\cdot\left(\overline D-\sum_vu_vC_v\right).
\tag{688.11}
\]

这就是 Gross–Hriljac 交数表达式；Pépin 的原文 Introduction 第 2 页及 Theorem 2.3 给出此规范和符号：
<https://arxiv.org/pdf/1103.0570>。

将 (688.11) 应用于 \(M_h=f^*L_h\)。它说明 \(\mathcal M_h(-V_h)\) 的模型度量是 M_h 的次数零 Néron 度量。该陈述先通过避开有限支撑的截面之差得出；局部连续性随后给所有点。若在代数闭剩余域的标准表述中应用 (688.11)，可先作未分歧扩张；交数、度数以及 ord_K 的归一化均相容，故公式下降回 K。

现在令

\[
\mathscr P_h=\phi_*^*\lambda_Y(\eta_h)
\in\operatorname{Pic}^0(J_X)\otimes\mathbb Q.
\]

由 (688.2)，ι^*P_h=M_h^{-1}。P_h 是 Picard 零次线丛，所以其规范度量经 Abel 映射拉回，就是曲线上 M_h^{-1} 的 Néron 度量；这是 Néron 配对的函子性。两者的常数按 c_0 的原点刚性化相同。因此实际完整修正拉回的度量等于

\[
\text{模型度量 }\mathcal M_h
\;\otimes\;
\text{模型度量 }\mathcal M_h(-V_h)^{-1},
\]

即平凡泛纤维线丛上 \(\mathcal O(V_h)\) 的模型度量。注意这里保留了完整 P_h；并没有删去 Picard 修正。它的作用正是把 \(\mathcal M_h\) 改为多次数零的 Néron 延拓。

截面 s_h 无水平零极点，按 c_0 归一化。其在 x 上的模型赋值因此为 \(V_h\cdot\overline x=a_{v(x)}\)，用 ord_K 计。转回 v_{q_0} 必须除以 e，得到 (688.9)。若开始用了 C_h 次幂，d、a 和模型赋值都乘 C_h；(688.4) 除回后全部抵消。证毕。

这也直接说明：本公式只需实际 q、L_h 的特殊纤维度数；无需先求 η_h 的具体除子或其全局高度。

## 4. 有限 Ω 的同步计算，不丢掉方向间相关性

取 F^0 的有理基 h_1,…,h_r，r=[F:Q]−1。在每个 q_0=2,3，同时记录

\[
\mathbf d_v=(d_v(h_1),\ldots,d_v(h_r)),\qquad
\mathbf a_v=(a_v(h_1),\ldots,a_v(h_r)).
\tag{688.12}
\]

删除 I 的 v_0 行列得到非奇异矩阵 I_0。一次有理矩阵求解给

\[
\mathbf a_{v_0}=0,\qquad
(\mathbf a_v)_{v\ne v_0}=I_0^{-1}(\mathbf d_v)_{v\ne v_0}.
\tag{688.13}
\]

令 S_{q_0}⊂V 是真正包含 Q_{q_0} 点约化的分量集；可先用全部顶点给有限上包络，再用局部点条件缩小。定义

\[
\mathcal T_{q_0}
=\{e_{q_0}^{-1}\mathbf a_{q_0,v}:v\in S_{q_0}\}
\subset\mathbb Q^r.
\tag{688.14}
\]

则同一个 R593/R634 目标集可取为

\[
\boxed{\Omega
=\{\chi_2(2)u_2+\chi_3(3)u_3:
u_2\in\mathcal T_2,\ u_3\in\mathcal T_3\}.}
\tag{688.15}
\]

向量按原迹配对识别为 W=(F⊗Q_p)/Q_pκ，再作 R634 的原坐标变换即可。**不能为每个 h_i 单独取值域后任意交叉组合**，否则会加入同一局部点不可能同时实现的靶向量。这里逐个分量保留所有方向的共同标签。

同一实际 c_1 的靶由其两个约化标签直接确定：

\[
\omega_0
=\frac{\chi_2(2)}{e_2}\mathbf a_{2,v_2(c_1)}
 +\frac{\chi_3(3)}{e_3}\mathbf a_{3,v_3(c_1)}.
\tag{688.16}
\]

若候选 x 与 c_1 在两处都落到相同标签，则 ω(x)=ω_0；更一般，两个不同标签也可能有相同向量。这是一条可验证的同靶条件，不从整数 a 的同余条件直接猜测曲线规范化后的分量标签。

实际偶分支的 d 在 Q_2、Q_3 都为立方，R593 的局部扭曲识别保持全部模型度量、基点和唯一截面。因此同样的 (688.14)–(688.15) 用于所有这些 d，不引入新增 q|D 的局部项。本篇仍不把 X_d/c_0 的商值运输成 X_1/c_1。

## 5. 分母界及有理计算证书

令 τ=|det(I_0)|。它等于分裂正则半稳定对偶图的生成树数；平行边照计，自环不影响 I。若只有一个顶点，按 τ=1 处理。

若 C d_v(h_i)∈Z 对全部 v,i 成立，由伴随矩阵公式

\[
\boxed{\lambda_{q_0,h_i}(X(\mathbb Q_{q_0}))
\subset\frac1{eC\tau}\mathbb Z.}
\tag{688.17}
\]

这是有限值域的分母界，绝不是给这些数一个大小上界。也不能在没有计算 e,C,τ 时把它们当 p 单位。

一个完整有限证书应包含：K 的 e；模型分量及结点；整数 I；各方向的有理 d；c_0、c_1 及候选允许标签；解 a。纯代数核验为

\[
I\mathbf a=\mathbf d,\quad
\mathbf a_{v_0}=0,\quad
\sum_v\mathbf d_v=0.
\tag{688.18}
\]

这与“在有限个点上拟合出高度值”不同：所有局部点的涵盖来自分量归约和 (688.9)。模型、实际商在分量上的度数尚未给出时，(688.18) 不是已执行的证书。

## 6. 本题可直接检查的零局部项判据

对全部 h∈F 考虑 (688.5)。非退化迹配对给唯一元素 κ_v∈F，使

\[
d_v(h)=\operatorname{Tr}_{F/\mathbb Q}(\kappa_vh),
\qquad\sum_v\kappa_v=\kappa.
\tag{688.19}
\]

这些 κ_v 由实际分量度数定义，不冒称每个分量都稳定于 F 的对应作用。即使特殊化自同态代数变大，(688.19) 仍只是 F 上有理线性泛函的迹表示。

**推论 688.2。** 若对全部 v 有 κ_v∈Qκ，则对全部 h∈F^0，λ_{q_0,h} 恒为零。因此在 2、3 两处同时验证这一条件便得实际 Ω={0}。

**证明。** d_v(h)=0，(688.8) 的归一解为 a=0。证毕。

反向在模型的全部顶点上也成立：a_v(h)=0 对全部 v,h∈F^0 等价于 κ_v∈Qκ。只在 Q_{q_0} 点可达顶点上的消失不要求这一更强条件。

还有两种方便的充分条件：

- 若除一个分量外，\(\bar f|_{C_v}\) 全部恒定，则 d_v=0 于那些分量；(688.6) 使余下的 d_v(h) 也为零，故该处全部局部项为零。有理分量上的映射自动恒定。
- 若一组保持实际极化、h 和 f 的对称作用在所有非恒定分量上传递，则这些分量的 d_v(h) 相等；总和零仍迫它们全零。使用此条件必须给出实际作用及传递性，不能只凭 CM 商潜在好约化。

更一般可直接计算

\[
H_{\rm bad}
=\{h\in F^0:d_{2,v}(h)=d_{3,w}(h)=0
\text{ 对全部 }v,w\}.
\tag{688.20}
\]

其中每个 h 的实际坏处项恒零。此处只是在已知的实际高度空间中取线性子空间；若随后改写 R634 的消元，必须重新检查限制方向后剩余未知标量的维数，不能原封不动套用全体 F^0 的消元公式。

## 7. 与图上二次高度的一致性及精确边界

从 Tate 模角度，T_h=q^†hq 在半稳定 J_X 的图同调部分为零，因为它因子化经过好约化 A。于是 Betts–Dogra/BDMTV 图公式中的边上二次密度为零；只剩分量的顶点迹。故本题坏处函数在图的每条边上仿射，与 (688.8) 的离散交数公式一致。

原始公开来源 BDMTV, *Quadratic Chabauty for modular curves: algorithms and examples*, Theorem 3.2，给图同调项与每个分量的对角块迹，并明确对应未必保持各分量的直和分解：
<https://www.cambridge.org/core/journals/compositio-mathematica/article/quadratic-chabauty-for-modular-curves-algorithms-and-examples/C317E63BB0128EB3F2163621CA63E66E>。
这里仅用该图公式作结构对照；(688.9) 的符号、e 与 C_h 由第 3 节交数证明独立固定，避免不同高度 convention 的常数混用。BMS Proposition 7.15 也直接保证同分量上的 λ_{q_0,h} 相同。

本篇完成了 Ω 的一个准确可计算化步骤：无需先计算 η_h 或 ℓ_h 的全局高度，输入缩为 2、3 处的实际半稳定分量、交数和商线丛度数。它没有提供这些矩阵的实际数值；没有证明 κ_v∈Qκ；没有把 A 的潜在好约化误当成 X 的潜在好约化；没有消掉 R634/R682 在 p 处 Λ 的未知 jet；也没有证明任何外积首项是单位。下一项必须真正计算本题这两个小素数处的分量及 κ_v，而不是把 (688.15) 当成 Ω 的已知数值。
