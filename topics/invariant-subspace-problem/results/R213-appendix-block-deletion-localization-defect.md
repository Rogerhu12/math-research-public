# R213A：归一化块删除的强交换子与局部配对缺陷

日期：2026-11-13（Asia/Taipei）。作者：kernel。

状态：完整接口及失败路线说明。沿用本轮核删除下界稿的设置，不声称局部化缺陷已经消失。

## 1. 归一化交换子的强极限

令
$$
s_m=\left(\sum_{j\ge m}|a_j|^2\right)^{1/2}>0,
\qquad\eta_{m-1}/s_m\longrightarrow0.
$$
对每个 $m$ 选有限终点 $n_m>m$ 使
$$
q_m=\left(\sum_{j=m}^{n_m-1}|a_j|^2\right)^{1/2}\ge s_m/2.
$$
在块 $I_m=[m,n_m)$ 上令
$$
h_m=q_m^{-1}\sum_{j\in I_m}a_j\chi_j,
\qquad D_m=|\Omega_{I_m}\rangle\langle h_m|,
$$
块外张量恒等。于是 $\|D_m\|=1$，$D_mQ_m=0$，故
$$
D_m\longrightarrow0\quad\text{强算子拓扑}.
\tag{1.1}
$$
此前完整进位预算给
$$
\|[D_m,X]\|\le(1+\sqrt5)q_m+2e_m,
\qquad e_m=O(g\eta_{m-1}),
$$
以及
$$
\|[D_m,Y]\|\le C_\varphi(432g^2\eta_{m-1}+74q_m^2).
$$
所以 $[D_m,T]/q_m$ 作为完整域上的有界延拓，范数一致有界。

对每个固定有限柱向量 $v$，充分大的 $m$ 使 $Q_mv=v$。秩一纯块计算给
$$
\|([D_m,X]-q_mI)v\|\le2e_m\|v\|.
$$
除以 $q_m$，使用 $e_m/q_m\to0$ 和 Bell 交换子预算，再由有限柱稠密性延拓，得到
$$
\boxed{[D_m,T]/q_m\longrightarrow I\quad\text{强算子拓扑}.}
\tag{1.2}
$$

## 2. 核上归一化删除是真实近似广义原像

对 $f\in M=\ker T$，所有 $D_mf$ 都在 $\operatorname{Dom}T$，所以
$$
T(D_mf/q_m)=-[D_m,T]f/q_m\longrightarrow-f.
\tag{2.1}
$$

**推论 2.1。** 如果 $D_mf/q_m$ 沿某个子列弱收敛到 $u\in H$，则
$$
u\in\operatorname{Dom}T,\qquad Tu=-f.
\tag{2.2}
$$
证明：闭线性算子图是 $H\oplus H$ 中的闭线性子空间，因而也弱闭；对 (2.1) 与所假设的弱收敛取图极限即可。

特别，非零核向量的归一化删除不能有弱极限零。如果该序列有界，Hilbert 空间弱序列紧性给一个实际广义原像 $u$，从而 $f\in\operatorname{Ran}T$。但有界性本身尚未证明；已经知道 $M\subseteq\overline{\operatorname{Ran}T}$ 不能代替它。

一般 $L^2$ 向量确实不满足归一化删除弱零：取非零纯第一阶
$$
f=\sum_{j\ge0}a_j\chi_j,
$$
每个块都准确满足
$$
D_mf/q_m=1.
\tag{2.3}
$$
因此，不能仅由 $D_m\to0$ 强和 $q_m\to0$ 推出归一化弱零，更不能用有限柱稠密性作无统一范数的延拓。

## 3. 局部乘法测试中的精确缺陷

令 $\psi$ 是固定有限 Walsh 多项式的乘法算子。它保持 $\operatorname{Dom}T$，$[\psi,T]$ 有界：对于 $X$，只有有限个真实低位项不交换，完整域结论由有限柱核心延拓；$Y$ 本身有界。

设 $\mathcal B(x,y)=\langle x,Cy\rangle$。$T$ 为 $C$ 自伴。对任意 $f,g\in M$，有
$$
\mathcal B([\psi D_m,T]f,g)=0.
$$
在真实域中展开乘积交换子，得到
$$
\mathcal B\bigl(\psi[D_m,T]f/q_m,g\bigr)
+\mathcal B\bigl([\psi,T]D_mf/q_m,g\bigr)=0.
$$
由 (1.2)，第一项趋于 $\mathcal B(\psi f,g)$。故第二项的极限由原核方程强制确定：
$$
\boxed{
\mathcal B\bigl([\psi,T]D_mf/q_m,g\bigr)
\longrightarrow-\mathcal B(\psi f,g).
}
\tag{3.1}
$$

所以将块删除乘以固定局部 $\psi$ 并不会自动把全等向性升级为局部等向性。需要独立证明 (3.1) 左侧趋零；若没有该额外估计，式子只是记录精确抵消。

本稿新增的是实际块构造的统一强极限 (1.2) 及其真实图后果 (2.2)。它没有证明归一化删除有界、弱零或存在全体核共用的非零正则像，故尚不解决未知核上的第二次除法。
