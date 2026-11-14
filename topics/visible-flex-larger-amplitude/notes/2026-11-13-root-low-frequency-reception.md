# 同一 R126 球的逐频低接收：实际核、条件像及后续接口

作者：/root（GPT-6 Astra Pro，AI 辅助），2026-11-13。

本次完成的是**固定 R101 真低中心下，R126 已认证非低球的低接收界，以及保留全部低输入频率的正核**。它不宣告低反馈、全频联立 fixed point 或 cut 已闭合。原 R126 参数域仍为六轴复单位球乘 T 加权 l1 半径 1/32；原背景、原 10793 材料叶、原 25 块、共同条带及 R125 真实 Green 均不变。

实际程序 `root_low_frequency_feedback_kernels.py`，SHA256
`5e208b0cd8a61303bd8cd38c2ba61464bef5a2b560aff27b7a221f35d66f5ad1`，由独立冻结源启动。正式 wait4 exit0，11.547290325 秒，峰 85328 KiB。程序重核全部原叶、原 25 个目标包、R101/R126 身份及 203136 个准确材料顶点系数比较。所有数学比较使用 Fraction/fmpq 与 Arb256 向外 dyadic；显示浮点不参与门。

## 1. 强模式质量及完整角导数

令 A_k 是 R101 在 tau=18/125 的真实低中心 C_L/V 的第 k 个正 pair strong 帽，U_k 是未知低修正 u/V 在共同 sigma 的相同帽。r 是中场 local-V strong 质量；h 按 R126 的高空间计量。P 用 sine 幅、K 用 cosine 幅，两分量分别先取径向 sup。正 pair Fourier 质量恰等于对应三角幅度，不再加 2。

保留 R116 的完整分解 N=Pi_perp Q+T。令 E=1+w²，c_bg=s+|ell|。对 k,n 两输入模式的差频 n-k，DQ 的四个 P/K 系数是

\[
\begin{pmatrix}
Es+\ell(Ekn-w^2)&E(sn+\ell k)\\
E(sk+\ell n)&Es kn+\ell(E-w^2)
\end{pmatrix}.
\]

和频 k+n 的四系数是

\[
\begin{pmatrix}
-Es+\ell(Ekn+w^2)&E(-sn+\ell k)\\
E(-sk+\ell n)&-Es kn+\ell
\end{pmatrix}.
\]

以 c_bg(1+k)(1+n) 归一后，每个绝对项均由

\[
\alpha_{kn}=\frac{5kn+1}{4(1+k)(1+n)}<5/4
\]

控制。因为 E=1+w²、0<=w²<=1/4，且 (s/c_bg,ell/c_bg) 位于顶点 (1,0),(0,1),(0,-1) 的凸包，双仿射系数只须在这些材料顶点取最大；程序对所有实际索引对逐项准确比较。无限频范围的粗常数 5/4 由上式直接代数推出。

两分母必须和分子的 kn 及其余角导数项一起出现。不能从 R116 已吸收角导数的 strong 卷积常数中再免费除这两个因子。

## 2. 每源块的有限频率结构

令源块的共同条带极值为 sigma_min,sigma_max；它们由同一原叶的 entry jump 和 continuous loss 逐分数重放得到，sigma_min>1/64。

对于低输出 m、低输入 n，C_L×u 的合法列是对 signed input n 和 -n 求和。每支 k=|m-signed_n| 必须属于 2,4,...,92，其系数为

\[
\alpha_{kn}A_k\exp((m-n)\sigma-k\tau).
\]

m-n>=0 用该源块 sigma_max，否则用 sigma_min。这里指数中的 n 是输入的绝对频率；两个 signed 支分别保留和频及差频。

对 C_L×v 的低输出，唯一可能频对是 -k+n=m，n=m+k>=94，k<=92。其系数为

\[
\alpha_{kn}A_k e^{-k(\tau+\sigma_{\min})}.
\]

因此仅 n=94,96,...,184 可能出现。u×v 同理，将 A_k 换为 U_k，指数换为 exp(-2k sigma_min)。C_L×H 与 u×H 的二次低输出准确为零，因为 H 的全部频率绝对值至少 34816。

Q(u) 使用每个无序低输入对恰一次：和频 m=k+n<=92 的非对角项系数 alpha_kn，对角 k=n 的系数 alpha_kk/2；差频 m=n-k>0、n>k 的项系数 alpha_kn exp(-2k sigma_min)。零模只从最终非均值输出投影中删除，完整均值仍在 T 中支付。

## 3. 完整非低二次项与高阶余项

每个低输出 m 可分别用以下弱源帽：

\[
Q(v)_m:\quad \frac54 e^{-188\sigma_{\min}}r^2,
\]
\[
DQ(v)[H]_m:\quad \frac54 e^{-2(34816-m)\sigma_{\min}}rh,
\]
\[
Q(H)_m:\quad \frac54 e^{-2\cdot34816\sigma_{\min}}h^2.
\]

它们分别来自相消频对 n,n+m；中/高交叉中 n>=34816-m。对每个输出，相关非负逐模乘积和由共同 strong 质量的乘积控制。上述指数始终以 Arb 向外存成严格正 dyadic，不能因显示浮点下溢而替换为零。源径向材料分别为 V²、V R_H、R_H²，其中普通块 R_H=V，块5的物理转换用 B=18555，块21用 R126 的固定正 R。

固定完整物理域 R_star=2^-34。R116 给

\[
\|D^2T(Y)[a,b]/c_{\rm bg}\|_{\sigma,0}
\le K_T\|a\|_{\sigma,1}\|b\|_{\sigma,1},\qquad K_T=270R_{\star}.
\]

DT(0)=0，故对整个连接线段均在该物理球中的 w，

\[
\|[T(C_L+w)-T(C_L)]/c_{\rm bg}\|
\le K_T(10V\|w\|+\|w\|^2/2).
\]

在本次 u=0 的 R126 球，三材料系数就是
K_T(10r+r²/2)、K_T(10+r)h、K_T h²/2。全部 mean、mean 导数及无限逆分母均在该完整 T 中，没有用有限多项式替换。

## 4. 真实低 Green 消费及共同质量

逐输出使用 R125 在共同 sigma 的每模 P/K 正核相加，P/K 的径向 sup 已分别支付。低算子是非因果的，全部 25 源到 25 目标都保留；不把目标右侧源删除。所有 W/F/r_x/frame 费用仅为原一次。

块21的 VR 与 R² 核逐模分别取
min(S G2,Rmax G1) 及 min(S²G2,S Rmax G1,Rmax²G0)。块5使用 BG1、B²G0。

每个模式的独立帽可分别消费同一共同余项帽；这样的模式帽之和不声称仍只付一次共同质量。因此程序另给 `combined_norm_upper`：完整 T 以每源块的 max_mode 核只付一次；C_L×middle 用 max_input sum_output 的真实正矩阵范数消费一次。此总帽再与各模式帽之和取小，两个约束都对同一真实接收场有效。

原 R126 球在 u=0 时的实际低像总帽，在块3约9.01659e-5，块21约.0102326，块23约36.8307。这些是各块 local-V 坐标，没有被称作物理大小或已经成立的低解半径。实际主包保留全部 25×46 个独立模式帽及各项来源。

## 5. 使用边界与恢复

本次成功只认证上述源核和条件接收像。后续若加入 u!=0 或增大 r,h，必须重新证明每块

\[
(10+\sum_m U_{j,m}+r_j)V_{j,\max}+R_{H,j}^{\max}h_j<R_\star,
\]

并实际支付低、中、高完整自映及同一距离权的收缩。旧 R126 的 u=0 域门不能代替这个新门。cut 也必须另行消费相同完整源，不能从场范数小直接宣告参数一致。

稳定 manifest 保存源、25 个 source-block、完整 conditional-images、summary、正式资源、原输入身份和独立审核。原 R125 target 包已经在仓库，不另重复保存。若 scratch 丢失，按 R125 manifest 和输入 SHA 从同名 notes 恢复路径后重跑固定源码；不得只恢复显示小数。

独立审核见 `2026-11-13-root-low-frequency-reception-independent-audit.md`，SHA `a8a5348730a3e77a7d4bd50a056304c074e95259d35d1113d82233fc27017037`。
