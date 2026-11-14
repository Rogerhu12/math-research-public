# R133 补篇：完整 regular 补算子与腰幅度 ν Schur 的逐行等价

2026-11-14。本篇仅改变同一最终问题的消元次序：固定 ν 时在逆中保留全部外端 regular 行，把腰的物理 C4 幅度作为最后一个 scalar 输出。原 b4、mean、度量、幅度目标、远端数据和所有接口均保留。这里先给完整恒等式及新的有限试算合同；有界全频补逆和真实非零 Schur 仍须由实际证书完成。

## 1. 同一方程和唯一的参数号数

仍使用完整 ac1 中心、原物理 moving 未规范化方向 \(h=(\delta u,\delta v)\)，以及原 \(\nu=-2572625729470897/72057594037927936\)。令

\[
\mathcal D=\partial_r-D_QF,\qquad F_\nu=\partial_\nu F
\]

表示原 moving 向量场的导数。**本篇和实际源码的号数始终是**

\[
\mathcal D h=F_\nu\,\delta\nu+f.
\tag{P.1}
\]

如果改用非线性 residual \(\mathcal R(Q,\nu)=Q_r-F(Q,\nu)\)，则 \(\partial_\nu\mathcal R=-F_\nu\)；这只是另一命名，不能据此给本篇实际 `parameter_source` 添加负号。

以 \(U_0h=u_h(0)\) 表示全部腰 u Dirichlet 行，\(B_Rh\) 表示真正完整物理 regular 线性行（外 mean 及全部非mean Robin），\(\ell h\) 表示腰的真实物理 C4 幅度导数。\(B_R\) 包括原 m=4 的 b4 行，并保留此前已付的非线性帽导数、物理角和 mean 转换。实际有限提案使用其已记录的浮点模型；模型误差仍由完整边界消费者支付。

在共同 PPoly 接口取右减左的跳。定义完整补算子

\[
\mathscr A_{\rm reg}h=
\big(\mathcal Dh,\ U_0h,\ B_Rh,\ ([h]_i)_i\big).
\tag{P.2}
\]

全线性问题准确是

\[
\mathscr A_{\rm reg}h=\mathfrak f+\mathfrak F_\nu\delta\nu,
\qquad \ell h=g_{\rm amp},
\quad\mathfrak F_\nu=(F_\nu,0,0,0).
\tag{P.3}
\]

物理控制支于 \((.05,.18)\)，所以在腰和 \(R=25/8\) 没有显式目标参数边界列。变化量引起的完整角图/mean 变化已经包含在 \(\ell,B_R\) 中。独立 far 数据的 \(D_{f_B}\) 列仍属于 \(\mathfrak f\)；只有计算纯 ν 响应时才取这个独立方向为零。这里没有解掉 far label 方程。

## 2. 完整等价消元，不删除原 b4

在以后实际支付的空间中，若 \(G=\mathscr A_{\rm reg}^{-1}\) 存在，置

\[
h_f=G\mathfrak f,\qquad q_\nu=G\mathfrak F_\nu,
\qquad S_{\rm amp}=\ell q_\nu.
\tag{P.4}
\]

则原问题 (P.3) 与

\[
S_{\rm amp}\delta\nu=g_{\rm amp}-\ell h_f,
\qquad h=h_f+q_\nu\delta\nu
\tag{P.5}
\]

逐行等价。反向代入立刻恢复全部体源、腰 u、每条外 regular 行、全部 mean、每个接口及原腰幅度行。\(S_{\rm amp}\ne0\) 时得到唯一 scalar；没有这条真实非零证明时，本篇不宣称完成闭合。

对当前反射 head \(N=96\)，固定 ν 的未知量是 193 个物理系数；(P.2) 的边界为 96 个腰 u 行和 97 个外 mean/Robin 行，后者包含 j=1,…,96。腰幅度是第 194 个完整 bordered 方程；它仍通过 \(\delta\nu\) 满足。

原 b4-output 提案在固定 ν 时把外 b4 改成 scalar 输出。新提案从不对这个旧矩阵重贴新标签；两组源、记录和 case 各自独立。已观察的旧有限端部病态见 [实际诊断](../notes/2026-11-14-R133-b4-output-head-end-diagnostic.md)，但 (P.3)–(P.5) 的等价本身不依赖该浮点解释。

## 3. 全均值、参数转换及真实接口

本消元没有改变任何体算子，因此完整标量 mean 的方程、\(\Gamma<1.013237\)、独立 response mean 跳和 reference-subtracted 参数接触项均沿用 [实际完整均值 Green](R133-supplement-actual-final-complete-mean-Green.md) 的明确合同。

纯 ν 响应仍有完整物理 mean 源

\[
\langle F_{\nu,2}\rangle=-\beta m\,\partial_\nu K\,\langle v^2\rangle.
\]

它不能由有限反射空间或 \(U_0h=0\) 删除。参数转换 \(Y=\tau z-\rho w\delta\nu\) 仍保留原 \((T_i-1)\rho_iw_i\delta\nu\) 接口，即使物理 \([h]_i=0\)；此处没有把这个转换源误写成 (P.2) 中新的物理跳。

真正的外 mean 行仍来自完整非线性 regular 图。有限模型的 mean 行只能提供提案；精确完成时须使用原完整 mean Green 的真实外端范围，而不能保持浮点零 mean。

## 4. 同步转置与正确的腰号数

圆周内积使用归一化 \(L^2\)。有限正弦/余弦系数的 Gram 是
\(W=\operatorname{diag}(1/2,\ldots,1/2,1,1/2,\ldots,1/2)\)，mean 的权重为 1。

真实输出伴随满足

\[
\mathcal D^*\psi=0,\qquad
\psi(0)=U_0^*\lambda_U-\ell^\sharp,
\qquad\psi(R)=-B_R^*\lambda_R.
\tag{P.6}
\]

星号相对于真实上述内积；有限系数形式是

\[
W\psi_0=U_0^T\lambda_U-\ell_{\rm coeff},\qquad
W\psi_R=-B_R^T\lambda_R.
\tag{P.7}
\]

若 \(a_j\) 是完整腰幅度对 cosine(4jφ) 的导数列，(P.7) 特别给

\[
\psi_{2,0}(0)=-a_0,\qquad
\psi_{2,j}(0)=-2a_j\quad(j\ge1).
\tag{P.8}
\]

mean 没有额外因子 2。当前完整 96 列区间和无限尾已经有独立实际证书；有限提案采用同一已记录中点，误差不改成零。新的外端 \(\lambda_R\) 包含 m=4 的自由乘子，不能用旧 `omitted_physical_mode=4` schema。

对真连续响应/伴随，分部积分得

\[
\ell h=\int_0^R\langle\psi,\mathcal Dh\rangle dr
+\lambda_U U_0h+\lambda_R B_Rh,
\qquad
S_{\rm amp}=\int_0^R\langle\psi,F_\nu\rangle dr.
\tag{P.9}
\]

这是正的原 `parameter_source` 配对，没有另加负号。

## 5. 完整双残差恒等式，含每个 jump

以下给近似伴随所需的准确形式。取任意分片 \(\widetilde\psi\) 和完整边界乘子，置

\[
r^*=\mathcal D^*\widetilde\psi,\quad
\epsilon_0=\widetilde\psi_0+\ell^\sharp-U_0^*\lambda_U,
\quad\epsilon_R=\widetilde\psi_R+B_R^*\lambda_R.
\]

在每个接口以 \(\widetilde\psi_i^+\) 作为 jump 数据的 dual 值，定义

\[
\mathfrak Y\mathscr A_{\rm reg}h
=\int\langle\widetilde\psi,\mathcal Dh\rangle
+\lambda_UU_0h+\lambda_RB_Rh
+\sum_i\langle\widetilde\psi_i^+,[h]_i\rangle.
\tag{P.10}
\]

则没有近似地

\[
\begin{aligned}
(\ell-\mathscr A_{\rm reg}^*\mathfrak Y)h
={}&-\int\langle r^*,h\rangle
+\sum_i\langle[\widetilde\psi]_i,h_i^-\rangle\\
&+\langle\epsilon_0,h_0\rangle
-\langle\epsilon_R,h_R\rangle.
\end{aligned}
\tag{P.11}
\]

证明是对每片积分后使用
\([\langle\widetilde\psi,h\rangle]_i
=\langle\widetilde\psi_i^+,[h]_i\rangle
+\langle[\widetilde\psi]_i,h_i^-\rangle\)。它同时保留全部 response 跳和全部 adjoint 跳；即使 mean 已由准确标量解重建为连续，非mean 接口仍必须付。

给定任意完整响应提案 \(q\)，写

\[
E=\mathscr A_{\rm reg}q-\mathfrak F_\nu,\qquad
E^*=\ell-\mathscr A_{\rm reg}^*\mathfrak Y,
\qquad S_0=\ell q-\mathfrak Y E.
\]

在 (P.4) 的真补逆可用时，准确有

\[
\boxed{S_{\rm amp}-S_0=-E^*G E.}
\tag{P.12}
\]

这直接来自 \(q_\nu-q=-GE\)。所有源、边界、mean、jump 组成同一个数据空间，因此任何实际的两侧范数预算必须覆盖 (P.10)–(P.11) 的全部列；不能只把体内残差相乘。若真正支付 \(\|G\|\) 和两个完整残差，则
\(|S_{\rm amp}-S_0|\le\|E^*\|\,\|G\|\,\|E\|\)。这条条件式不是一个未计算的非零声明。

## 6. 新有限提案和消费身份

新 [regular head model](../scripts/fourfold_codazzi_final_regular_head_model.py) 复用原完整 moving 体作用及正的参数源，仅按 (P.2)、(P.7) 改边界消元。新 [bounded trial producer](../scripts/fourfold_codazzi_final_regular_head_trial.py) 有独立 kind、source、case 和输出；完整均值、N+2M 输出支持、全 FFT 后向门和准确单侧 Hermite 构造保持。

它采用原 n+1 QR 协议时，另放一条**独立零 dummy** 方程；dummy 不参与体方程或任何物理行，不是 ν，也不是 mean。真实输出仍是左端 \(\ell q_\nu\)。新伴随 metadata 的外端乘子是全部非mean regular 行，不把 j=1 强置零；准确初始 mean 系数对应 (P.8)。

原 body mean-completion 的局部恒等式可作用于这些明确标记的分片试函数，取其原 `amp-multiplier=-1` 仅表示 (P.8) 的左 mean 归一；它不能使旧 b4-output 边界消费者自动变成新输出的证书。完整新物理 boundary/transpose 消费器必须按 (P.10)–(P.11) 另行接入。

本篇完成的是原问题与新 Schur 消元的准确等价和正确转置合同。新 finite trial 的实际成功、完整残差、全频补逆、真实 Schur 非零及最终非线性闭合均按各自的实际证据登记。
