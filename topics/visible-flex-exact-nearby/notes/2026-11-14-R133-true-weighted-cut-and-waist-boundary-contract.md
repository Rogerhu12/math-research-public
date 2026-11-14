# 完整权重下的真实 cut、腰边界及最后接口合同

本篇给出新公开消费者
`scripts/fourfold_codazzi_regular_cut_true_weighted_boundaries.py` 的证明规则。
在该消费者公开实际运行前，文中不登记新的数值结论。输入全部来自已成功
的 1977 格全帽、14 门 true cut 及 5970 格完整 dyadic frame 提案。

## 1. 坐标和完整两端

原 moving 状态采用完整物理正交 Gram：96 个 odd 正弦状态，even mean
及 96 个非零余弦状态。新的径向权重是

\[
 R(r)=\operatorname{diag}(I_{96},\rho(r)I_{97}),\qquad y=Rh.
\]

rho 是原完整提案记录的准确连续正分片线性函数，mean 与全部 even
状态一起变换。其对数导数已在连续 operator validator 中单独保留。
本篇只消费准确两端值，不改变这个函数，也不另选一个接近的权重。

原 true cut 的 97 行具有

\[
 B=\begin{pmatrix}I_{96}&J_*\\0&M_*\end{pmatrix},
 \qquad
 B_R=BR(L)^{-1}
   =\begin{pmatrix}I_{96}&J_*/\rho_L\\0&M_*/\rho_L\end{pmatrix}.
 \tag{W.1}
\]

第二行是独立真实 even mean 匹配；不能删掉。原全帽误差只作用于完整
even 输入，odd 单位块准确不变。因此，若原 low97 算子误差为 epsilon，
则完整 weighted 误差是至多 epsilon/rho_L。原全部 high 输出同样支付
1/rho_L，但这项没有给未知 high 输入算子或完整高频闭合。

## 2. 原完整腰 frame 的准确 L0、D0

令 Q 是原保存的完整 193×96 腰 dyadic frame，
G=Q*Q，P=QG^(-1)Q*。使用全部 Gram 验证 G 正定。
腰算子 U 保留最前面的全部 96 个 odd 坐标，所以 UU*=I96。
若方阵 UQ 可逆，令

\[
 S=Q(UQ)^{-1},\qquad L_0=\|S\|.
 \tag{W.2}
\]

S 是腰限制 U:ran P→R96 的真逆，且 S U P=P。由完整状态的正交
分解，边界 Uy=g0 给

\[
 \|Py\|\le D_0\|(I-P)y\|+L_0\|g_0\|,
 \qquad D_0=\|S U(I-P)\|.
 \tag{W.3}
\]

因为 UU*=I、SUP=P、S 的像是 ran P，有

\[
 [SU(I-P)][SU(I-P)]^*=SS^*-P.
\]

U 是压缩算子，S 在 ran P 上的奇异值均不小于 1；因而准确得到

\[
 D_0^2=L_0^2-1.\tag{W.4}
\]

程序对全部 S*S 选取一个 dyadic 辅助 eigenbasis，重新验证其完整
Gram 和全部 congruence/Gershgorin 项。浮点 eigenvalue 不作证据。
所得 L0 平方上界代入 (W.4) 给 D0 上界，保留全部 even 方向及 mean。

## 3. 新 cut frame、真均值和补空间逆

令 Q_L 是原 weighted 提案的完整 cut frame。其准确投影仍为
P_L=Q_L(Q_L*Q_L)^(-1)Q_L*，而不是 Q_L Q_L*。
记 g>0 为完整 Gram 下界，Q_Leven 为其全部 97 个 even 行。
原有向 cut 给准确 dyadic 的 nominal J、M。直接计算

\[
 r\ge\|B_RP_L\|
 \le\frac{\|\widehat B_R Q_L\|
      +(\epsilon/\rho_L)\|Q_{L,\mathrm{even}}\|}{\sqrt g}.
 \tag{W.5}
\]

这同时支付了原 physical→moving 误差、新权重、原 QR 舍入和新 frame
Gram，未假设两个浮点子空间精确相同。

原已付 mean 给 |(M_*)0|≥m0>0，原 low odd 误差给
||(J_*)0||≤j0。取完整 even 输入中仅 mean 一个坐标来显式求一个右逆，
96 个 odd 输入随后解完其余 96 行。这个构造不删除剩下的 96 个 even
输入。该右逆范数由正矩阵

\[
 \begin{pmatrix}1&j_0/m_0\\0&\rho_L/m_0\end{pmatrix}
 \tag{W.6}
\]

的最大奇异值 ell 控制。故 B_R B_R*≥ell^(-2)I97，并且

\[
 B_R(I-P_L)B_R^*
   =B_RB_R^*-B_RP_LB_R^*
   \ge (\ell^{-2}-r^2)I_{97}.\tag{W.7}
\]

程序要求右侧严格为正。其平方根倒数给 LR，DL=LR r，因而真实边界
B_R y=gL 给

\[
 \|(I-P_L)y\|\le D_L\|P_L y\|+L_R\|g_L\|.\tag{W.8}
\]

所有 97 行、193 个输入状态及独立 mean 均参加了计算。原已付 high
输出仍另记；本篇不将有限 low kernel 称为全无限边界的核。

## 4. 腰处的零长接口和后续 Green

连续 validator 的每格 exact polynomial 以该格原右端 frame 为锚。
它到达左端后的投影与下一个原 frame 一般不同，即使差极小也有实算
delta。5970 个格各有这样一跳，最后一格的腰跳也必须保留。

本篇 (W.2)–(W.4) 使用原保存 Qwaist，因此其位置是虚拟的 0−。
最内格 polynomial 的左端位于 0+。全局消费者要先支付这条零长接口，
使用真实 sec(delta)、tan(delta) 门，最后检验 D0 rho_Riccati(0−)<1。
不能用原 D0 与跳之前的 rho_Riccati(0+) 相乘。

原 cut frame 正是最外格的右锚，故 cut 端没有额外虚构的一跳。
所有实际 trial 跳和独立边界源仍分别支付。完整 source Green 应保留
每格 signed rate 与径向衰减；本篇不把全残差乘一个未经验证的统一逆常数。

完整 ordinary 物理范数还须用
`||h(r)||<=max(1,1/rho(r))||y(r)||` 逐点或逐格换回。
原 ac1 到连续修补背景的 operator 变化、未知 high 输入、真正参数响应
及非线性背景费用仍保留为独立未付项。
