# 未收敛有限尾与 prefix 的自由切口 Schur 线性化

作者：/root/tail_theory，2026-11-09。**状态：只读方法与条件式完整推导，待独立审查；未实现新 worker，未调用新的 root、flow 或求解器。**

本文将现有多重打靶的内部消元与原 prefix 的切口匹配联成一个线性问题。关键是保留每个 stage 和深端 Robin 的实际残差 forcing。基点不必已经解出固定高度的 DN，但必须能在该点评价全部原 stage flow、局部 moment root 及相应线性化。本文不建立新的非线性存在性结论，不把未收敛状态称为 DN。

## 1. 问题、坐标和适用范围

所有物理度量参数、角模数、角求积、径向网格、深端条件和 guard 固定。设有限尾有 $d$ 个 stage。沿代码的编号，外切口为 $n=0$，深端为 $n=d$。每个 shape 节点是

$$
y_n=(Q_n,\Pi_n)\in\mathbb R^{2M}.
$$

这里 $Q,\Pi$ 是保存 CP 的节点坐标。一个 stage 的映射 $\Phi_n$ 从较深节点 $y_{n+1}$ 向外积分，输出时已经包含原代码对 momentum 行除以该 stage 的 portRatio；因此它与 $y_n$ 位于同一节点规范化中。本文的 $J_n$ 是这个**完整 stage 映射**的矩阵，不能再对其 momentum 行重复除 portRatio。

原尾内部残差为

$$
R_n=\Phi_n(y_{n+1})-y_n=(R_n^Q,R_n^\Pi),
\qquad 0\le n<d,
$$

深端条件为

$$
e=\Pi_d-G_{\rm deep}Q_d.
$$

$G_{\rm deep}$ 是冻结 finite-far 图的对角矩阵；它仍是原有限截断边界，不是精确无限尾。固定物理切口半径记为 $c$，其背景斜率为 $w_c>0$，$E_c=1+w_c^2$。原固定高度 DN 还施加 $Q_0=H/c^4$。完整 prefix/tail 问题则用 prefix 的实际切口高度与斜率匹配来确定 $H$；该 $H$ 不是预先必须等于某个辅助预测向量的额外约束。

数学推导对 $C^1$ stage 映射及其真实 Jacobian 成立。在实际有限角/RK 算法中，所用根、矩阵和流是数值近似；本文的消元恒等式对所提供矩阵仍成立，但其作为真实 Newton 方向的准确性需另验。理想等距角求积模型与 literal rounded 三角表不是逐位同一个实算术对象；本文不建立逐位等价或区间误差证书。

**局部可评价性不可省略。** 若基点某一 stage/RK 子点不能通过原 moment guard，或原 root 没有得到合格残差，则本稿没有可用的该 stage 线性化。先前被拒绝的 trial 输入不能直接充当合法基点。已经有有限原 shooting 残差的状态，或已审条件下的零 shape 初猜，才是拟议基点类型；是否实际全域可评价仍以原引擎输出为准。

## 2. 原尾的非齐次消元

把每个 $J_n$ 分成 $M\times M$ 块：

$$
J_n=
\begin{pmatrix}
A_n&B_n\\
C_n&D_n
\end{pmatrix}.
$$

原 Newton 的内部线性化是

$$
J_n\delta y_{n+1}-\delta y_n=-R_n,
\quad\text{即}\quad
\delta y_n=J_n\delta y_{n+1}+R_n.
\tag{1}
$$

注意残差在右侧的符号为正。这与代码中 out 减当前外节点的残差定义直接对应。

从深端开始，定义

$$
\Gamma_d=G_{\rm deep},\qquad b_d=-e.
\tag{2}
$$

于是深端线性化恰为 $\delta\Pi_d=\Gamma_d\delta Q_d+b_d$。假定在 $n+1$ 层已有

$$
\delta\Pi_{n+1}=\Gamma_{n+1}\delta Q_{n+1}+b_{n+1}.
$$

置

$$
\begin{aligned}
X_n&=A_n+B_n\Gamma_{n+1},&
Y_n&=C_n+D_n\Gamma_{n+1},\\
t_n&=B_n b_{n+1}+R_n^Q,&
u_n&=D_n b_{n+1}+R_n^\Pi .
\end{aligned}
\tag{3}
$$

若 $X_n$ 可逆，定义

$$
\Gamma_n=Y_nX_n^{-1},\qquad
b_n=u_n-\Gamma_n t_n.
\tag{4}
$$

将上述关系代入 (1) 的上下块，先得到

$$
\delta Q_n=X_n\delta Q_{n+1}+t_n,\qquad
\delta\Pi_n=Y_n\delta Q_{n+1}+u_n.
$$

消去 $\delta Q_{n+1}$ 即证明

$$
\delta\Pi_n=\Gamma_n\delta Q_n+b_n.
\tag{5}
$$

因此在所有 $X_n$ 可逆的前提下，全部内部方程和深端 Robin 线性化恰等价于切口关系

$$
\boxed{\delta\Pi_0=\Gamma_0\delta Q_0+b_0}
\tag{6}
$$

及从外向内的重建

$$
\delta Q_{n+1}=X_n^{-1}(\delta Q_n-t_n),\qquad
\delta\Pi_{n+1}=\Gamma_{n+1}\delta Q_{n+1}+b_{n+1}.
\tag{7}
$$

这是逐层代入的充分必要等价，不只是一个无 forcing 的 tangent 图。$b_0$ 包含所有 stage 缺陷和深端 Robin 缺陷。仅当这些残差均为零时，递推才保证全部 $b_n=0$；未收敛基点不能静默令它们为零。

原 core 的 correction 正是在 (6) 后另行指定 $\delta Q_0=H/c^4-Q_0$，再执行 (7)。其 gs、bs、cache.Gi、cache.t 分别对应 $\Gamma_n,b_n,X_n^{-1},t_n$。本文到此没有提出任何原 flow 或校正符号的变化。

如果某个 $X_n$ 奇异，只能说这个以 $\delta Q_n$ 为自由坐标的消元 chart 失效。不能据此宣布完整联合 Jacobian 奇异或原非线性问题无解。本稿不实现换 chart 或其他线性解法。

## 3. 切口局部物理高度与斜率

### 3.1 节点动量和 engine 动量

令 $\rho=2^a$。原 node0 的动量使用 $\mu_{-1}=\rho\mu_0$ 规范化，而 cell0 engine 使用 $\mu_0$。所以送入切口 engine 的局部状态是

$$
\widehat y_0=D_\rho y_0,\qquad
D_\rho=\operatorname{diag}(I,\rho I).
\tag{8}
$$

这个 $\rho$ 只用于局部切口 root/jet 的坐标转换，不再次作用于 §2 已规范化好的 stage 矩阵。

记原切口完整 moment root 为 $L=L(Q_0,\rho\Pi_0)$，其中 $L_0$ 是均值未知量，其余项使用正交余弦基。实际非均值物理高度和径向斜率的**普通余弦系数**为

$$
H_t=c^4Q_0,\qquad
(S_t)_j=m_j^2c^3(Q_0)_j+\sqrt2\,w_cL_j,
\quad m_j=3j,\ 1\le j\le M.
\tag{9}
$$

因此

$$
S_Q=\operatorname{diag}(m_j^2c^3)+\sqrt2\,w_c(L_Q)_{1:M},
\qquad
S_\Pi=\sqrt2\,w_c\rho(L_{\widehat\Pi})_{1:M}.
\tag{10}
$$

$L_Q,L_{\widehat\Pi}$ 必须来自同一个完整 $(M+1)$ 维 root；不能舍掉均值行后分别求各个非均值模。

### 3.2 无需 DN 的局部隐微分

设切口 moment 方程写成

$$
\mathcal F(L,Q,\widehat\Pi)
=\mathcal M(L,Q)-\kappa
\begin{pmatrix}0\\\widehat\Pi\end{pmatrix}=0,
\qquad
\kappa=\frac{\mathrm{orientation}\sqrt{12}\,\mu_0}
{\sqrt2\,c^4w_c^2}.
$$

在其 root Jacobian $\mathcal B=\mathcal M_L$ 可逆时，

$$
L_Q=-\mathcal B^{-1}\mathcal M_Q,\qquad
L_{\widehat\Pi}
=\mathcal B^{-1}\kappa
\begin{pmatrix}0\\I\end{pmatrix}.
\tag{11}
$$

这里只求一个节点的局部 moment root；不需要其余 stage 已经拼合，也不需要固定高度 DN 已存在。已审正 moment 分支的凸性/强单调结论是这个局部问题的相关依据，不代付整条尾 BVP。

另有直接交叉核：若 $f_Q$ 是**engine 状态**的 shape RHS 前 $M$ 行，$r_x$ 是同一切口 profile 的导数，则原公式给

$$
S_t=4c^3Q_0+\frac{c^4}{r_x}f_Q(D_\rho y_0),
$$

从而

$$
D_{y_0}S_t
=4c^3[\,I\ \ 0\,]
+\frac{c^4}{r_x}(D_{\widehat y}f_Q)D_\rho.
\tag{12}
$$

证明是把 $f_{Q,j}=(r_x/c)[(m_j^2-4)Q_j+\sqrt2\,w_cL_j/c^3]$ 代入。这与 (10) 相同；数值实施时仍须评估除以小 $r_x$ 及相消的影响，不能把恒等式直接当作误差界。

现有 heightJetJacobian 输出沿已传播 tangent 图收缩后的有限差分，不是 (10) 的两个独立偏导块，也不包含 $b_0$。它不能替代此处的局部偏导与内部 forcing。

## 4. 保留 prefix 内部残差的完整边界消元

令 $z\in\mathbb R^k$ 包含当前离散 prefix 的所有形状节点和原自由参数。将其 collocation 方程及原起点/对称/控制约束统记为

$$
F_p(z)\in\mathbb R^{k-M}.
$$

这里只移除原来的 $M$ 个尾斜率 terminal 行；原 prefix 的其他方程和物理参数保持。其物理切口高度和按原方向约定转换后的斜率记为 $H_p(z),S_p(z)\in\mathbb R^M$。

### 4.1 原代码的 $\sigma,q_g,\sqrt E$ 因子

在当前 cut 角图等于物理角的接口，令 $q_g$ 为固定的 shape gauge amplitude，$\sigma\in\{-1,1\}$ 为 bridge 方向。它们不是尾坐标 $Q$ 或实际求解中的 support amplitude。以 prefix 外端保存变量的高度块 $Z_b$ 和原 ODE 右侧高度块 $f_z$ 表示，

$$
H_p=\sigma q_g Z_b,\qquad
S_p=\sqrt{E_c}\,q_g f_z.
\tag{13}
$$

这直接来自原 TailMixin 的请求 $H=\sigma q_gZ_b$ 与 terminal

$$
\frac{q_g f_z-S_t/\sqrt{E_c}}{\mathrm{bcweights}}.
$$

所以斜率匹配向量 $S_p-S_t$ 与原 terminal 只差可逆正行缩放 $\sqrt{E_c}\,\mathrm{bcweights}$；不能在 $S_p$ 再多乘一次 $\sigma$。原自由 support 参数及其对 inlet 的作用全部保留在 $z,F_p$，不能把固定 gauge $q_g$ 与它混为一谈。若另一个应用让 gauge 或 $c,w_c$ 也变化，必须补全相应导数；本稿的同 $g$ 固定接口不含那些变化。

### 4.2 消去 prefix 内部修正

定义基点缺陷

$$
r_h=H_p(z)-c^4Q_0,\qquad
r_s=S_p(z)-S_t(Q_0,\Pi_0).
\tag{14}
$$

原完整联合 Newton 的 prefix 和高度行是

$$
F_{p,z}\delta z=-F_p,\qquad
H_{p,z}\delta z-c^4\delta Q_0=-r_h.
\tag{15}
$$

若方阵

$$
J_p=\begin{pmatrix}F_{p,z}\\H_{p,z}\end{pmatrix}
$$

可逆，置

$$
a_p=-J_p^{-1}\begin{pmatrix}F_p\\r_h\end{pmatrix},
\qquad
B_p=J_p^{-1}\begin{pmatrix}0\\c^4I\end{pmatrix}.
\tag{16}
$$

则 (15) 恰等价于 $\delta z=a_p+B_p\delta Q_0$。这里 $a_p$ 同时包含 prefix 内部残差及高度不匹配，不能因为使用一个已有 CP 而默认它为零。

斜率行的线性化是

$$
S_{p,z}\delta z-S_Q\delta Q_0-S_\Pi\delta\Pi_0=-r_s.
$$

代入 (16)，定义

$$
C_{\rm out}=S_{p,z}B_p-S_Q,\qquad
D_{\rm out}=-S_\Pi,\qquad
r_{\rm out}=r_s+S_{p,z}a_p.
\tag{17}
$$

于是得到完整的、带原 prefix forcing 的边界关系

$$
\boxed{C_{\rm out}\delta Q_0+D_{\rm out}\delta\Pi_0=-r_{\rm out}}.
\tag{18}
$$

若提供者已经直接给出 (18)，仍须说明其 $r_{\rm out}$ 是否包含 (16) 的内部 forcing、矩阵作用的节点坐标、物理高度/斜率规范化及行缩放。只有齐次“阻抗”矩阵而无 forcing，不足以代表未收敛 prefix 的联合 Newton。

若 $J_p$ 不可逆，这只是该 prefix Dirichlet chart 无法消元；完整联合系统仍可能可解。本文不把 chart 可逆性视为已从数值 CP 认证。

## 5. 最后 $M\times M$ 系统与等价性定理

将 (6) 代入 (18)，得到

$$
\boxed{
(C_{\rm out}+D_{\rm out}\Gamma_0)\delta Q_0
=-r_{\rm out}-D_{\rm out}b_0.
}
\tag{19}
$$

**定理。** 若所有 $X_n$、$J_p$ 以及 (19) 的系数矩阵可逆，则：先解 (19)，再用 (6)、(7)、(16) 重建的全部修正，唯一解出原 prefix 方程、高度/斜率匹配、所有尾 stage 方程及深端 Robin 的联合线性化。反之，任一联合线性化解必满足 (19) 并由相同重建式给出。

证明：§2 已逐层证明尾线性化与 (6)、(7) 双向等价；§4 已由可逆 $J_p$ 证明 prefix/高度行与 (16) 双向等价，并将斜率行等价改写为 (18)。唯一剩余变量是 $\delta Q_0$，代入得 (19)。可逆性保证唯一性，回代逐项满足每个被消去的原方程。没有使用基点 $R_n,e,F_p,r_h,r_s$ 为零的假设。

在这些 chart 条件下，完整联合线性化的非奇异性也等价于最后矩阵非奇异。该代数结论不保证最后矩阵条件数良好，不保证非线性 Newton 收敛，更不保证任何大步仍在正分支中。

## 6. 为什么不必先求出固定 $H$ 的 DN

固定高度 DN 的通常调用要求先把全部 $R_n,e$ 解到容差，再返回 $S_t(H)$。若这一内层过程卡在某个辅助 $H$，外层 prefix 便拿不到可靠响应；这不自动说明完整联合匹配无解。

本稿评价的是**未消去的原残差映射** $(F_p,r_h,r_s,\{R_n\},e)$ 及其局部导数。定义这些量只要求当前局部 root/flow 可评价，不要求它们的非齐次残差已消失。因此可以在一个尚未拼合的、但可评价的尾状态上计算 $J_n,R_n$，并通过 $b_0$ 把当前内部缺陷传到联合方程。

此时 $\Gamma_0$ 只是当前线性化中保持尾内部线性化方程的切口切向关系，不被称为某个已解 DN 函数的导数；$\Gamma_0\delta Q_0+b_0$ 更不能被写成新的非线性 DN。只有原残差最终足够小并完成原验收后，才有相应数值 DN/联解记录。

这里用 prefix 的高度、斜率匹配替代的是**求解布局中内层固定 $H$ 的辅助切口条件**。如果某个实验本身就要求固定 $H=H(1/4)$，自由切口联合步不再是该固定目标实验的响应，必须另外标为联合 warm。完整原 prefix/tail 问题的匹配方程保持不变；当前零态八轮固定目标对照不在本稿中被替换。

## 7. 现有接口能给什么，尚需什么

下列是未来若实施时所需的只读数据，不是已经实现或调用过的新接口：

1. 原 core 的 evaluate(states,target,true,scales) 能在给定节点计算 flows、已含 portRatio 的 J、stage residuals 和深端 end。target 只进入切口残差和尺度，不把输入节点强制改为边值。使用时保存完整当前 state、目标标签、源 hash、root/guard 统计和原尺度。
2. 原 correction 已在内部算出 $\Gamma_n,b_n,X_n^{-1},t_n$，但 trial-core 的公开返回对象没有直接暴露这段非齐次消元。未来需要绑定同一源码和同一已算数组的单独只读输出；不能只截取现有 tangentGraphAtCut，因为后者不传播 $b_n$。
3. 原 cutJets(node) 可在任意合法的局部切口节点评价 (9)，不要求整尾收敛；其所调用的是局部 root。偏导块可由 (11)，或由同源 rhsWithJacobian 按 (12) 获得。原沿图有限差分 heightJetJacobian 不足以单独承担此任务。
4. prefix 现有 fun_jac、原 inlet 参数导数和高度/terminal 的显式公式提供装配 $F_{p,z},H_{p,z},S_{p,z}$ 的来源。完整 $J_p$ 的离散 collocation 装配和一次分解后 $M+1$ 组右侧解，尚未在本稿中实现。不能调用现有 TailMixin.bc_jac 来取得它又假装绕开了 DN；该方法内部仍会调用 tail.solve。
5. 若只用旧低模图、块对角高模或旧 prefix 数据近似某个块，必须标为近似 warm predictor，不能援引本稿的“真实联合 Newton 等价”称谓。最终仍使用原完整方程校正。

原正 moment 分支要求和有限角/原 RK 方程保持。所有行尺度只作为原残差范数的权重；做本次线性化时冻结它们，不额外求导某个人为的、随 trial 高度变化的归一尺度。重新评价 trial 与最终验收时，应明确采用的原尺度并保留全部原门限。

## 8. 验收和冻结来源

一个线性修正、一个下降步或一个无固定 $H$ 的 warm 都不是新的解记录。未来若实施，应先核完整联合线性残差，再在每个 trial 上调用原 moment/RK 和 prefix 方程，保留全部 guard、失败及原残差；若只作 warm，随后仍由原真实耦合器校正。最终要求原 prefix collocation/边界容差、原 tail shooting 容差、真实 seam audit、同 $g$ 实际 XYZ 与独立连续几何证据；本稿没有支付其中任何新数值门。

主要源码绑定：

| 来源 | SHA256 |
|---|---|
| scripts/db6f-prefix-tail-trial-core.mjs | d475d0f6a0dab247efa751e468052d0f30829e1761ccf7f85094a13fe95902e5 |
| scripts/db6f-prefix-tail-trial-split.mjs | aa50ed54848a0e4e7e2be64a08160e17fa4379df2eed8bf8675baf2d2f344727 |
| repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs | 182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c |
| repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_fast_split_flux_engine.mjs | a1c84ba25846f0bf6e9d35092dbc0281d01f60f3d68700dfad20fd598e27e4b6 |

prefix 的具体实现来源为 scripts/950f-prefix-nonlinear-coupling-v2.py、scripts/950f-prefix-adaptive-chart-bvp-v2.py、scripts/950f-prefix-warped-bvp.py。其当次文件 hash 与上述表一起另存机读绑定。这里的源码定位用于证明规范化和接口范围；没有更改这些冻结文件。
