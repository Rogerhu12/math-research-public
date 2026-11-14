# 完整中央分区矩阵：全部坐标 Hessian、紧框架与相位 Ward 块

本稿把偶临界相位的完整源放入同一个中央硬源分区矩阵。它保留全部坐标交叉、完整硬源回归逆、真实换位表示及两侧源度量。新增的全源接口是：分区矩阵的完整对数 Hessian Schur 恰为 \(g\) 的紧框架提升，既没有只保一个方向，也没有遗漏任何低 primitive 源。

最后给出逐坐标严格的局部 Schur 身份与正块；这些局部块不能代替完整 Hessian 伪逆，所以一般相位上界仍未由此证明。

## 1. 同一固定源与中央正矩阵

取 \(2s\) 位，\(s\ge1\)。记 unweighted lowering/raising 为
\[
d=\sum_iE_i,\qquad e=d^*.
\]
固定物理 primitive 空间
\[
U=\ker d\cap\mathcal H_s,\qquad
V=\ker d\cap\mathcal H_{s-1},
\]
并以 \(i_U,i_V\) 表示等距包含。以下写成 \(U,V\) 上的算子，不另选非正交基。

给 \(z_i>0\)、\(t_i=\log z_i\)、\(\pi=\prod_i z_i\)，置
\[
Z_j=\operatorname{diag}(z_I:|I|=j),\qquad W=Z_s^{-1}.
\]
实际相位的共同固定源二次型是
\[
h=i_V^*Z_{s-1}^{-1}i_V,\quad
\ell=\pi^{-1}i_V^*Z_{s-1}i_V,\quad
q=i_V^*e^*We\,i_V,
\]
\[
g=i_V^*(dZ_se)^{-1}i_V.
\]
最后一个逆先在完整 \(\mathcal H_{s-1}\) 上计算。由真实顶补集身份，
\(q=\pi^{-1}i_V^*dZ_se\,i_V\)。

本稿中心对象为完整中央硬源分区矩阵
\[
\boxed{M(t)=i_U^*W(t)i_U,\qquad
W(t)=\exp\!\left(-\sum_i t_i n_i\right).} \tag{1.1}
\]
其中 \(n_i\) 是占据投影。记
\[
M_i=\partial_{t_i}M=-i_U^*n_iWi_U,\qquad
M_{ij}=\partial_{t_i}\partial_{t_j}M=i_U^*n_in_jWi_U. \tag{1.2}
\]
特别地 \(M_{ii}=-M_i\)。\(M>0\)，所有逆均在整个 \(U\) 上取。

## 2. 完整第一逆恰为中央硬源回归 Schur

令 \(E=e\,i_V:V\to\mathcal H_s\)。实际去权硬源是 \(W^{1/2}U\)，其物理正交投影为
\[
P_{\rm hard}=W^{1/2}i_U M^{-1}i_U^*W^{1/2}.
\]
对实际低源 \(v_b\)，dual raising 给 \(d_b e_bv_b=2v_b\)。因此
\(e_bv_b\) 的最小第一原像部分为 \(2\mathcal J_1v_b\)，其余恰为真实硬源投影。写回共同固定源，得到
\[
\boxed{
4g=E^*\left(W-Wi_UM^{-1}i_U^*W\right)E.
} \tag{2.1}
\]
这是实际 MP 定义的另一精确实现，不是只减一个标量均值；回归空间是完整 \(W^{1/2}U\)。

为简记，设
\[
Q_W=W-Wi_UM^{-1}i_U^*W.
\]
则 \(Q_W\succeq0\)、\(Q_Wi_U=0\)。

## 3. 所有坐标覆盖全部低源的紧框架

定义
\[
B_i=E_i|_U:U\longrightarrow V.
\]
它确落在 \(V\)，因为 \(dE_i=E_i d\)。中央补集 \(C\) 在 \(U\) 上为标量 \((-1)^s\)，且 \(Cn_iC=I-n_i\)，故
\[
P_U n_i|_U=\tfrac12I_U.
\]
又 \(d(n_i-\tfrac12)u=E_i u\)、\(d^2(n_i-\tfrac12)u=0\)，而其 \(U\) 分量为零，所以
\[
\boxed{(n_i-\tfrac12)i_U=\tfrac12 E B_i.} \tag{3.1}
\]

设整行
\[
\mathcal B:U^{\oplus 2s}\longrightarrow V,\qquad
\mathcal B(u_1,\ldots,u_{2s})=\sum_i B_i u_i.
\]
它是精确的缩放 coisometry：
\[
\boxed{\mathcal B\mathcal B^*=\sum_iB_iB_i^*
=\alpha I_V,\qquad \alpha=\frac{s+2}{3}.} \tag{3.2}
\]

这里给一个完全原 \(sl_2\) 的证明，不调用对称群不可约性。对 \(v\in V\)，
\(d^3E_i^*v=0\)，所以中央最高 primitive 投影在该向量上准确为
\[
P_U E_i^*v=
\left(I-\tfrac12ed+\tfrac1{12}e^2d^2\right)E_i^*v.
\]
逐项求和：
\[
\sum_i E_iE_i^*|_V=(s+1)I,
\]
\[
\sum_iE_i e d E_i^*|_V=2sI,
\]
\[
\sum_iE_i e^2d^2E_i^*|_V=4(s-1)I.
\]
第二式可用 \(dE_i^*v=(I-2n_i)v\)、\(E_i(I-2n_i)=-E_i\) 直接交换；第三式用
\(d^2E_i^*v=-2E_i v\) 与
\(\sum_iE_i e^2E_i=2ed-2\sum_i n_i\)。
合并得到
\[
(s+1)-s+\tfrac{s-1}{3}=\tfrac{s+2}{3},
\]
即 (3.2)。

因而 \(\mathcal B\) 满射。这里“所有坐标都保留”确实覆盖整个 \(V\)，不是只覆盖某个 \(X_sU\) 的较小像。

## 4. 完整非交换 Hessian Schur 就是 \(g\) 的提升

定义 \(U^{\oplus 2s}\) 上的完整块矩阵
\[
\mathscr H_{ij}=M_{ij}-M_iM^{-1}M_j. \tag{4.1}
\]
所有矩阵均来自同一 \(M\)，次序不交换。由 (1.2)，
\[
\mathscr H_{ij}=i_U^*n_iQ_Wn_j i_U.
\]
利用 \(Q_Wi_U=0\)、(3.1) 和 (2.1)，得到
\[
\boxed{\mathscr H_{ij}=B_i^*gB_j,\qquad
\mathscr H=\mathcal B^*g\mathcal B.} \tag{4.2}
\]
因此 \(\mathscr H\succeq0\)，且
\[
\ker\mathscr H=\ker\mathcal B,
\qquad
\boxed{g=\alpha^{-2}\mathcal B\mathscr H\mathcal B^*.} \tag{4.3}
\]
等距映射 \(\mathcal I=\alpha^{-1/2}\mathcal B^*:V\to U^{\oplus 2s}\) 还给
\[
\mathcal I^*\mathscr H\mathcal I=\alpha g.
\]
所以完整 Hessian 的非零部分，准确等于整个低源 \(g\) 的缩放。其 Moore–Penrose 逆也准确为
\[
\boxed{\mathscr H^\dagger=\alpha^{-2}\mathcal B^*g^{-1}\mathcal B.} \tag{4.4}
\]

## 5. 两侧源度量和 \(q\) 的全部 Ward 交叉

令
\[
\mathscr A=\mathcal B^*h\mathcal B,\quad
\mathscr C=\mathcal B^*\ell\mathcal B,\quad
\mathscr Q=\mathcal B^*q\mathcal B.
\]
记 \(R_{ij}\) 为物理坐标换位 \((ij)\) 在 \(U\) 上的酉限制。它们来自同一个真实置换表示，满足 involution、对称及所有 Coxeter 关系；不是可独立选择的矩阵。

首先对所有 \(i,j\)，由 (3.1) 得
\[
\boxed{\mathscr Q_{ij}=4M_{ij}+2M_i+2M_j+M.} \tag{5.1}
\]
特别地
\[
\mathscr Q_{ii}=M.
\]
其余两个度量的全部块如下：
\[
\boxed{
\begin{aligned}
\mathscr A_{ii}&=-z_iM_i,\\
\mathscr C_{ii}&=z_i^{-1}(M+M_i),
\end{aligned}} \tag{5.2}
\]
而 \(i\ne j\) 时
\[
\boxed{
\begin{aligned}
\mathscr A_{ij}&=z_i(-M_iR_{ij}-M_{ij}),\\
\mathscr C_{ij}&=z_i^{-1}(-M_jR_{ij}-M_{ij}).
\end{aligned}} \tag{5.3}
\]

证明 (5.3) 只需原局部算子身份。\(i\ne j\) 时
\[
E_i^*E_j=n_iP_{ij}-n_in_j,
\]
其中 \(P_{ij}\) 是完整物理换位。又
\[
E_i^*Z_{s-1}^{-1}=z_iW E_i^*.
\]
所以
\[
B_i^*hB_j
=z_i i_U^*W E_i^*E_j i_U
=z_i(-M_iR_{ij}-M_{ij}).
\]
对 \(\ell\) 用中央补集 \(Ci_U=(-1)^s i_U\)、
\(CZ_sC=\pi W\)、\(CE_i^*E_jC=E_j^*E_i\)，得到第二式。对角同样直接由 \(E_i^*E_i=n_i\) 得 (5.2)。

式 (5.1) 还与 (4.1) 给出整个硬源回归余项
\[
\mathscr Q_{ij}-4\mathscr H_{ij}
=(2M_i+M)M^{-1}(2M_j+M). \tag{5.4}
\]
这是同一完整源的交叉 Gram，不能只取其对角块。

## 6. 全相位块的无遗漏共同 Hessian 等价

实际共同相位块写为
\[
J=h g^{-1}\ell+2g-q,\qquad
\begin{pmatrix}\kappa h&J^*\\J&\ell\end{pmatrix}\succeq0
\quad\Longleftrightarrow\quad \Phi\preceq\kappa I.
\]
由 (3.2)、(4.4)，其完整行提升为
\[
\boxed{
\mathscr J
:=\mathscr A\,\mathscr H^\dagger\,\mathscr C+2\mathscr H-\mathscr Q
=\mathcal B^*J\mathcal B.
} \tag{6.1}
\]
因此对每个 \(\kappa\ge0\)，
\[
\boxed{
\Phi\preceq\kappa I
\quad\Longleftrightarrow\quad
\begin{pmatrix}
\kappa\mathscr A&\mathscr J^*\\
\mathscr J&\mathscr C
\end{pmatrix}\succeq0.
} \tag{6.2}
\]
两边严格等价，因为 \(\mathcal B\) 满射，且提升块共同杀死
\(\ker\mathcal B\oplus\ker\mathcal B\)。这里的 \(\mathscr H^\dagger\) 是完整 Hessian 的 MP 逆，不是把各对角 \(\mathscr H_{ii}^{-1}\) 拼起来。

所有 \(\mathscr A,\mathscr C,\mathscr Q,\mathscr H\) 已在同一个 \(M,M_i,M_{ij},R_{ij}\) 上显式给出。故 (6.2) 是全源共同矩目标，没有遗漏混合项或换成任意独立正块。

## 7. 真正成立的逐坐标 Schur 恒等与其限制

令
\[
P_i=-M^{-1/2}M_iM^{-1/2}.
\]
由于 \(W>0\)，而 \(n_i|_U\)、\((I-n_i)|_U\) 都单射
（其 unweighted 范数平方均为 \(I_U/2\)），有
\[
0<P_i<I,\qquad \sum_iP_i=sI.
\]
于是
\[
\mathscr H_{ii}
=M^{1/2}(P_i-P_i^2)M^{1/2}>0,
\]
\[
\mathscr A_{ii}=z_iM^{1/2}P_iM^{1/2},\qquad
\mathscr C_{ii}=z_i^{-1}M^{1/2}(I-P_i)M^{1/2}.
\]
在同一坐标上，准确有
\[
\boxed{
\mathscr A_{ii}\mathscr H_{ii}^{-1}\mathscr C_{ii}=M=\mathscr Q_{ii}.
} \tag{7.1}
\]
所以坐标内的类相位交叉等于 \(2\mathscr H_{ii}\)，并且
\[
\boxed{
\begin{pmatrix}
\mathscr A_{ii}&2\mathscr H_{ii}\\
2\mathscr H_{ii}&\mathscr C_{ii}
\end{pmatrix}\succeq0.
} \tag{7.2}
\]
证明是共同 \(M^{1/2}\) 同余后，各块都是同一个 \(P_i\) 的函数；其标量行列式为
\[
P_i(I-P_i)-4P_i^2(I-P_i)^2
=P_i(I-P_i)(I-2P_i)^2\succeq0.
\]

但是 (7.1) 不允许把 (6.1) 的完整
\((\mathscr A\mathscr H^\dagger\mathscr C)_{ii}\)
替成
\(\mathscr A_{ii}\mathscr H_{ii}^{-1}\mathscr C_{ii}\)。
因此 (7.2) 不是全相位界的证明。真正未付的是同一个完整 Hessian 伪逆中的跨坐标运输。

## 8. 自伴性给一个实际非交换微分身份

改用 \(w_i=z_i^{-1}\) 作自然变量，令
\[
\widetilde M(w)=i_U^*\operatorname{diag}(w_I)i_U.
\]
它是具体多仿射、次数 \(s\) 的正矩阵多项式。把 (5.3) 的物理自伴条件
\(\mathscr A_{ij}=\mathscr A_{ji}^*\) 写成自然变量，得到
\[
\boxed{
(w_i-w_j)\,\partial_{w_i}\partial_{w_j}\widetilde M
=R_{ij}\,\partial_{w_j}\widetilde M
-(\partial_{w_i}\widetilde M)R_{ij}
\quad(i\ne j).
} \tag{8.1}
\]
该式不要求 \(w_i\ne w_j\)，在合组处按原多项式身份读取。

这是由真 Boolean 局部换位推出的共同矩约束，不能把 \(\widetilde M\) 换成任意满足单独 Hessian 正性的矩阵函数。本文只证明 (8.1) 与完整相位接口；没有把其名称、可积性或某个外部微分系统自动当作收缩定理。

本文未增加有限样本扫描，未调用新的外部定理。任意两权的完整相位已由独立全位数证明闭合；一般更多权值仍须支付 (6.2) 的真实完整跨坐标项。

