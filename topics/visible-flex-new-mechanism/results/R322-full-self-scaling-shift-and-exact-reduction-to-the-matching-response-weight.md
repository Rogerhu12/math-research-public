# R322：完整 self 的缩放权移与跨权响应成员问题的严格归约

日期：2026-11-15。**完整纸面证明；没有新原式编译、消元、profile 评价、人工执行或科学运行。** 本文不预报 R316 的实际成员结论。

[R314](R314-ordered-matrix-defect-localization-and-faithful-Euler-self-coordinates.md) 给完整 self 的九矩与局部 Euler 忠实坐标。本文另付一个范围问题：对一个真权齐次目标，允许全部真权的 pure-zero 响应，并不比允许同权响应更强。原因不是预先假设已知原列互不相消，而是完整缩放作用在同一真实空间中的有限 Laurent 分解，以及 self 准确的权移。

使用来源：[R89](R89-affine-covariance-and-positive-multiple-pair-P1.md)、[R105](R105-finite-canonical-fourth-cost-space-and-response-quotient.md)、[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)、[R201](R201-weight-zero-pure-image-and-failure-of-positive-character-readout.md)、[R247](R247-complete-response-Jacobi-presentation-and-pure-kernel-decomposition.md)、R314。

## 1. 真实空间、缩放与同锚

记完整 canonical 成本真空间为 U，完整可调响应真空间为
\[
R=\operatorname{span}\{\mathcal B_A(\tau):A\in E_8,\ \tau\in W\}
\subset U,
\]
并记
\[
U_{\mathrm p0}=U\cap\ker\pi,\qquad
R_{\mathrm p0}=R\cap\ker\pi.
\tag{1}
\]
$\pi$ 是完整 pure 模式投影。这里 $\mathrm p0$ 是全权 pure 核；真权零以后写成上标 $(0)$。

对 $H>0$ 定义
\[
(C_Hu)(x)=u(x/H),\qquad
(\mathsf P_HV)(f,g)(x)=V(C_Hf,C_Hg)(Hx).
\tag{2}
\]
这是 R89、R105 在平移参数为0时的完整全场作用。它包括二、三阶真实历史及全部右原函数，不仅作用在显式 x 多项式上。右锚同步乘 H。

R105 的正次数 Volterra 原式在支撑右方的空 collar 为零，故同步移动的右锚也可以放到包含这些支撑的一个共同更右空区；这一步保留原常数，没有将左尾重置。几何实现仍使用共同物理区间和正间隙，本稿不把 universal 延拓误作 $x+\omega=0$ 附近的合法浸入。

## 2. 原 R 和 pure 核确实留在同一真实空间

### 2.1 U 的不变性

R89 的真实变换
\[
h\mapsto Hh,\qquad k\mapsto k,\qquad \omega\mapsto\omega/H
\]
保真实 scalar 方程、frame 端点及零矩/零第三条件。变换后的常值 germ 可以改变，但 R105§5 已用真实零矩桥和真倒行证明成本 span 与 germ 无关。因此
\[
\mathsf P_HU=U,\qquad H>0.
\tag{3}
\]
此处等号使用逆缩放 $H^{-1}$；不是只给单向包含。

### 2.2 完整响应 R 的不变性

E8 的原 trace-zero 二次算子在 (2) 的同槽共轭下仍留在 E8。只需正缩放时，还可逐项从 R73 的完整原矩阵式看出八坐标权：
\[
(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)
:\quad(-1,0,1,-3,-2,-2,-1,0).
\tag{4}
\]
这包括全部原 J 项，不能仅从局部乘积部分计权。

R89§3 已证明完整第三真空间 W 与常值 germ 无关，而且
\[
\tau\longmapsto
\tau_H=C_H^{-1}\tau(C_H\cdot;C_H\cdot,C_H\cdot)
\]
是 W 的双射。对原完整响应公式逐槽共同共轭，得到
\[
\mathsf P_H\mathcal B_A(\tau)=\mathcal B_{A_H}(\tau_H).
\tag{5}
\]
式 (5) 保留外槽和两内槽，也保留所有嵌套 primitive 与历史。于是
\[
\boxed{\mathsf P_HR=R.}
\tag{6}
\]
没有把 $Z18\times E8$ 当作全部 R，也没有略去 R247 的其他 pure 核分支。

### 2.3 pure 核的不变性

正缩放不混合 Fourier 相位，故
\[
\pi\mathsf P_H=\mathsf P_H^{\mathrm{pure}}\pi.
\tag{7}
\]
由 (3)、(6)、(7)，
\[
\mathsf P_HU_{\mathrm p0}=U_{\mathrm p0},\qquad
\mathsf P_HR_{\mathrm p0}=R_{\mathrm p0}.
\tag{8}
\]
这些都是同一真实函数空间中的线性不变性，不是形式模板自由赋值，也不授实际成本半群有符号闭合。

## 3. 有限 Laurent 系数是真实空间内的谱投影

R105§6 给 U 有限维，且完整原递推中一个 profile jet、一个原函数和一个坐标幂分别给有限的整数缩放幂。因此存在有限整数集合 S 和实线性算子 $A_\sigma:U\to U$，使
\[
\mathsf P_H=\sum_{\sigma\in S}H^\sigma A_\sigma .
\tag{9}
\]

先说明这些系数没有离开 (8) 的子空间。令 $m=|S|$，取任意足够接近1的 $\rho>1$，并取
\[
H_j=\rho^j,\qquad j=0,\ldots,m-1.
\]
矩阵 $(H_j^\sigma)_{j,\sigma}$ 是以互异正数 $\rho^\sigma$ 为节点的普通 Vandermonde，故可逆。于是每个 $A_\sigma$ 是有限个 $\mathsf P_{H_j}$ 的实线性组合。因此
\[
A_\sigma R\subset R,\quad
A_\sigma U_{\mathrm p0}\subset U_{\mathrm p0},\quad
A_\sigma R_{\mathrm p0}\subset R_{\mathrm p0}.
\tag{10}
\]
这是有限线性空间论证；系数可有符号，不解释为一条实际路径。

其次，由群律 $\mathsf P_H\mathsf P_K=\mathsf P_{HK}$，对两个正参数分别比较有限 Laurent 系数，得到
\[
A_\sigma A_\tau=
\begin{cases}
A_\sigma,&\sigma=\tau,\\
0,&\sigma\ne\tau.
\end{cases}
\qquad
\sum_{\sigma\in S}A_\sigma=I.
\tag{11}
\]
所以 (9) 的系数确为相容谱投影，而不是仅一组未必独立的形式系数。

定义
\[
U^{(\sigma)}=A_\sigma U
=\{V\in U:\mathsf P_HV=H^\sigma V\ \forall H>0\},
\]
以及 $R^{(\sigma)}=R\cap U^{(\sigma)}$。由 (10)–(11)，
\[
\boxed{
R_{\mathrm p0}
=\bigoplus_{\sigma\in S}
\bigl(R^{(\sigma)}\cap\ker\pi\bigr),
\quad
U_{\mathrm p0}
=\bigoplus_{\sigma\in S}
\bigl(U^{(\sigma)}\cap\ker\pi\bigr).
}
\tag{12}
\]
特别，一个全部 pure 为零的跨权响应，其每个真权分量也 pure 为零。不能把这一事实仅凭一张未检查的系数谱宣称；(7)、(10) 已给出完整原因。

## 4. 完整 self 的权准确下降二阶

沿 R314，定义
\[
\mathcal Q(V):u\mapsto
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u^2,0).
\tag{13}
\]
输入 u 为任意真实紧实 profile。全部右锚和左尾仍按第1节。

由 (2)，在其真实左零 collar，
\[
(\mathsf P_HV)(u^2,0)(x)
=V((C_Hu)^2,0)(Hx).
\]
纯缩放不会把其他 x 次数混进二次系数，所以
\[
\boxed{
\mathfrak q_u(\mathsf P_HV)=
H^2\,\mathfrak q_{C_Hu}(V).
}
\tag{14}
\]
即使先在较大有限多项式左尾类中写式子，这个二次系数关系也准确；不需要把别的次数删掉后才成立。

定义 profile 泛函上的缩放为
\[
(\mathsf S_Hq)(u)=q(C_Hu).
\]
式 (14) 等价于
\[
\mathsf S_H\mathcal Q(V)=H^{-2}\mathcal Q(\mathsf P_HV).
\tag{15}
\]
若 $V\in U^{(\sigma)}$，则
\[
\boxed{
\mathcal Q(V)(C_Hu)=H^{\sigma-2}\mathcal Q(V)(u).
}
\tag{16}
\]
所以原成本的真权 $\sigma$ 对应 self 的真权 $\sigma-2$。这是完整 self，包括全部 C2 余项和所有真实尾，不是 principal 计数。

## 5. 不同 self 权在真实开缩放区间中可分离

设有限个 profile 泛函 $q_\tau$ 分别满足
\[
q_\tau(C_Hu)=H^{\tau-2}q_\tau(u)
\]
且 $\sum_\tau q_\tau=0$ 对所有真实紧 u 成立。

固定任意一个这样的 u。其支撑是合法 I 内的紧集，因此存在围绕1的正 H 开区间，使全部 $C_Hu$ 仍紧支撑于同一 I。共同右空 collar也可以一并固定。于是
\[
\sum_\tau H^{\tau-2}q_\tau(u)=0
\tag{17}
\]
在一个真实正开区间成立。

不同整数幂的有限 Laurent 多项式在开区间上线性独立：乘一个足够大的正整数幂 H 后就是普通多项式。因此所有系数 $q_\tau(u)=0$。u 任意，遂每个 $q_\tau$ 都是零泛函。

这个论证不需要将某个母包移到无穷远、不需要宽度趋零，也不借未知的固定圆忠实性。它使用的等号是**所有**真实紧 profiles 上的函数等号。只在一个固定母函数或一张固定圆上代入为零时，不能直接使用 (17)。

因此
\[
\mathcal Q(R_{\mathrm p0})
=\bigoplus_\sigma
\mathcal Q(R^{(\sigma)}\cap\ker\pi)
\tag{18}
\]
是不同 self 权的直和；允许其中个别权的像为零。U 的对应像也同样分级。

## 6. 真齐次目标的跨权支付等价于同权支付

**定理。** 设 $V\in U^{(\sigma)}\cap\ker\pi$。则
\[
\boxed{
\mathcal Q(V)\in\mathcal Q(R_{\mathrm p0})
\iff
\mathcal Q(V)\in
\mathcal Q(R^{(\sigma)}\cap\ker\pi).
}
\tag{19}
\]

右推左显然。反向，若 $\mathcal Q(V)=\mathcal Q(K)$，其中 $K\in R_{\mathrm p0}$，按 (12) 写
\[
K=\sum_\tau K_\tau,\qquad
K_\tau=A_\tau K\in R^{(\tau)}\cap\ker\pi.
\]
把 self 等号作用于 $C_Hu$，由 (16) 得
\[
H^{\sigma-2}\mathfrak q_u(V)
=\sum_\tau H^{\tau-2}\mathfrak q_u(K_\tau).
\tag{20}
\]
第5节逐系数分离给
\[
\mathcal Q(K_\sigma)=\mathcal Q(V),\qquad
\mathcal Q(K_\tau)=0\quad(\tau\ne\sigma).
\]
这就给出同权 pure-zero 响应 $K_\sigma$，证明 (19)。

其他权仍可存在不为零的真实响应，只是它们在本次完整 self 等号里必须分别落到 Q 的核。没有把这些响应的完整第四函数判为零。

## 7. 对本次权零十四目标门的条件后果

R201 的准确完整目标
\[
H=C_2+\frac1{48}R_{\mathrm{old}\,0}
+\frac{11}{64}R_{\mathrm{old}\,2}
-\frac{13}{96}R_{\mathrm{old}\,3}
\]
满足
\[
H\in U^{(0)},\qquad \pi H=0,\qquad\lambda_+(H)=1.
\tag{21}
\]
R196/R201 已给 $\dim R^{(0)}=16$、$\dim\pi R^{(0)}=3$，所以完整权零 response pure 核为13维。

R316 的新设计只对该完整13维核和 H 计算十四份全 self 的 T/Euler 坐标，没有再计算其他权。式 (19) 说明，对这个特定 H 而言，
\[
\boxed{
\mathcal Q(H)\in\mathcal Q(R_{\mathrm p0})
\iff
\mathcal Q(H)\in\mathcal Q(R^{(0)}\cap\ker\pi).
}
\tag{22}
\]

**截至本稿，R316 仍需公开实际结果；本文没有宣称 MEMBER 或 NONMEMBER。**

若公开实际给 MEMBER 并通过 fresh 原复合 T/Euler 核验，则得到具体
\[
H_{\rm self}=H-K_0,\quad
\pi H_{\rm self}=0,\quad
\mathcal Q(H_{\rm self})=0,\quad
\lambda_+(H_{\rm self})=1.
\]
这说明 $\lambda_+$ 不能经完整 universal self 因子化。它仍是线性空间代表，不自动是一个实际有符号路径。

若公开实际给真正的 NONMEMBER，由 R314 忠实坐标和 (22)，则不仅权零核不能支付：全部 $R\cap\ker\pi$ 也不能支付**这个 H 的完整 self**。这仍不证明 $\lambda_+$ 通过 Q 因子化；$C_4,C_6$ 或其他目标之间的剩余关系没有由该单目标门自动解决，也不把任何固定圆的代入当作 universal 忠实。

若新实际只因资源或结构接口停下，式 (22) 仍是一个有效归约，但没有任何新成员决定。

## 8. 九矩的权提供一个直接一致性检查

R314 的真实矩密度为
\[
j_u=(r^2,xr^2,x^2r^2+2v^2)^T.
\]
其三个积分在 $u\mapsto C_Hu$ 下分别乘 $H^{-3},H^{-2},H^{-1}$，所以
\[
\mathcal N_{ij}(C_Hu)=H^{i+j-6}\mathcal N_{ij}(u),
\qquad i,j=0,1,2.
\]
再用 R314 将矩阵识别为唯一有序加法缺陷，(14) 给
\[
\mathbf T_{ij}(\mathsf P_HV)
=H^{i+j-4}\mathbf T_{ij}(V).
\tag{23}
\]
因此对真权 $\sigma$ 的 V，
\[
\mathbf T_{ij}(V)\ne0\ \Longrightarrow\ \sigma=i+j-4.
\tag{24}
\]
特别在权零，九矩只有 $(2,2)$ 项可能非零。新源码仍计算、保留和核对全部九项；(24) 是准确真权一致性检查，不能用来预先掩盖一个不符的原结果。

式 (24) 也不意味其他 self 坐标消失：局部 Euler 部分仍完整存在，正是 R314 和本次门保留的剩余信息。

## 9. 完成范围

本文已证明真实 R、pure 核和其有限 Laurent 谱投影的不变性，完整 self 的准确权移，真实正开缩放区间上的分离，以及 (19)–(22) 的成员问题等价。

没有新科学执行；没有提前使用本次结果；没有把固定圆代入、实际有符号控制或完整 period/ruling 的相容自动包含进来。下一结论必须消费真实公开的十四目标完整回执，而不能从本文的归约本身推断答案。

作者责任：缩放、锚、真实子空间和每个有限系数分离步骤均在正文给出。本文的计算性后果明确为等待 R316 实际的条件后果。
