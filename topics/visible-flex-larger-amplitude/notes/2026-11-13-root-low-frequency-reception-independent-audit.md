# R127 低接收频率核的独立源码审阅

2026-11-13，`/root/geometry_audit`（AI-assisted）。

本记录只审数学公式、源码消费及对象身份，不重算 ODE、Green 核、
已有正源积分或这次实际消费者。审阅冻结源为
`root-work/r127-inputs/root_low_frequency_feedback_kernels.py`，SHA
`5e208b0cd8a61303bd8cd38c2ba61464bef5a2b560aff27b7a221f35d66f5ad1`。
审阅未发现下列范围内的系数、指数、配对或目标范数遗漏。本记录
不代替该程序自己的正式退出与结果清单，也不证明 joint feedback。

## 1. 对象与 strong pair 归一

输入使用 R125 同一旧固定真实度量的全部 25×25×3×46 正 Green
核，原 source-x、物理 F、Wronskian 和分量 radial sup 已在 R125
支付。新消费者只选共同条带目标核，再加 P/K 两个分别取过 sup 的
系数，不重复乘 F、r_x、frame 或角强权。

中心谱是 R101 的同一个 R100 低解 C_L，文件
`2026-11-13-closure-r100-spectral-r1.json`，SHA
`1c12cde9889048daaced137a79a1504a4780d7f5315a5950c5fde4fda0d38651`。
其 A_k 是相对于 V、固定宽 τ*=18/125 的正模 strong pair 帽；
不是原始 Fourier 振幅。R126 的横轴半径 1/32 是该 R100 域的子域。
原反射 P 为 sine、K 为 cosine。正负两个 Fourier 半幅的质量和
恰等于相应完整 sine/cosine 幅度，这在复反射子空间也成立，不需
实共轭假设。

若把原始幅度写成 A_k exp(−kτ*)/(1+k)，其角导数 k 不能遗漏。
本程序已经使用完整系数

    alpha(k,n) = (5kn+1) / [4(1+k)(1+n)] < 5/4,

没有把两个分母当作免费的小因子。

## 2. 二次式的两个精确 pair 矩阵

R106(A16)–(A17) 给 U=−P−kK、C=K+kP，且 E=1+w²。
对不同来源的一个 k 模和一个 n 模，DQ 的正差频 n−k 输出的
完整 cosine 幅系数矩阵（行 P_k,K_k，列 P_n,K_n）是

\[
\begin{pmatrix}
Es+\ell(Ekn-w^2)&E(sn+\ell k)\\
E(sk+\ell n)&Es kn+\ell(E-w^2)
\end{pmatrix}.
\]

正和频 k+n 的矩阵是

\[
\begin{pmatrix}
-Es+\ell(Ekn+w^2)&E(-sn+\ell k)\\
E(-sk+\ell n)&-Es kn+\ell
\end{pmatrix}.
\]

最后一项用了 E−w²=1。两个矩阵都已包含 DQ=2B 和 cosine
输出的两个半幅，因此不另乘 2。相对于 c_bg=s+|ell|，再除两个
strong 因子 (1+k)(1+n)，每个绝对系数至多 alpha(k,n)。程序
实际用 s/c_bg、ell/c_bg 的三个三角形顶点以及 w² 的两个端点，
逐一核对全部被索引有限频对的八个矩阵项。双线性分式归一后的
系数在这些材料坐标上为多仿射，顶点包围合法。

## 3. 各频率分支及指数

目标 m=2,4,…,92。低方向 u 的输入 n 也在该低集合。C×u 的
源码循环 signed_n=n,−n，取 k=|m−signed_n|，恰保留正和频及
两种角色的差频。每项的宽度因子是

\[
\exp((m-n)\sigma-k\tau_*).
\]

当 m≥n，正系数使用该源块 sigma_max；当 m<n，负系数使用
sigma_min。这都是全块向上的方向；k=0 因中心无零模而排除。

对 C×near 或 u×near，非低输入 n≥94 要产生低 m，只能有
k=n−m≤92，故 near 仅需 94,…,184。对应两个因子分别是
exp[−k(τ*+σ)] 与 exp[−2kσ]，由同一原源块 sigma_min 支付。
near 表以 n 为列，而 u 的低频由 k=n−m 唯一确定，没有丢失
输入频率身份。

u² 只枚举 k≤n 的无序对。和频 k+n≤92 的非对角系数为 alpha，
对角为 alpha/2；差频只取 n>k，系数为
alpha exp(−2k sigma_min)。这与全部有序卷积及 Q=B(u,u) 一致。
零频只从最终低输出投影删去；完整零模 mean 对后续方程的作用
仍在 T=N−Π⊥Q 中支付。

有限非低场 v 的全部频率是 94≤n<M，M=34816；无限高场 H
包括 n≥M。它们产生低输出时只能通过反向频率抵消。因此每个
正低输出的三个完整正帽可分别取

\[
\tfrac54 e^{-188\sigma_{\min}}r^2,\qquad
\tfrac54 e^{-2(M-m)\sigma_{\min}}rh,\qquad
\tfrac54 e^{-2M\sigma_{\min}}h^2.
\]

第一项的较小频率至少 94；第二项有限频率至少 M−m；第三项
较小高频率至少 M。代码保留了所有这些严格正 tiny 项，不按浮点
下溢删除。C×H、u×H 的二次低投影则因频率支持确为零。三个
抵消帽都来自原共享 strong 模质量的正卷积，并非仅某一频对。

## 4. 完整高次 T 与两种输出消费

R116 的完整 mean 与无限逆给 D²T/c_bg≤270R*。在当前 R126
整球内 R*=2^−34，且 DT(0)=0。由 Taylor 积分，对中心帽
CL≤10V、有限场 Vr 和高场 W_H h，完整 T 增量有三个材料项

\[
K_T\left[V^2(10r+r^2/2)+VW_H(10+r)h+W_H^2h^2/2\right],
\quad K_T=270\,2^{-34}.
\]

普通块 W_H=V；块 5 用原 B=18555 的物理转换 W_H=B；块 21
用 R126 的固定 profile R，按同一个真实源分别取
min(SG²,RmaxG¹) 和 min(S²G²,SRmaxG¹,Rmax²G⁰)。这些分量
材料 min 对同一源有效，不能通过比较不同径向位置相除获得。

每个单独输出模允许接收同一个共同 T 总帽，故代码给出的
`separate_mode_caps` 分别有效。另给的总范数界只通过 max_m
支付该共享质量一次。线性的 C×near 总范数同样使用
max_n sum_m[G_m c_(m,n)]，再乘该块总输入质量 r；它保留
有限频率列，没有把每个 near 输入都单独领一次完整 r。

代码对两个合法总界取 min：一项是逐模帽直接求和；另一项使用
上述共享 T 与线性列和，其余正二次项完整求和。原低 Green 的
源位置 j<i、j=i、j>i 均保留，不把低非因果算子截成前缀。

## 5. 本次成立的范围及后续域门

实际 conditional image 只接收已经证明的 R126 固定低中心
nonlow 球，u=0；其 R*=2^−34 整球门已由 R126 输入核对。
source-block 保存的 u 频率核可供后续同对象使用，但今后 joint
消费者若允许 u≠0，或扩大 r、h，必须重新证明
10V+V|u|+Vr+W_H h 的整个复球仍在 R* 内。不得仅沿用旧
u=0 的物理域门。当前程序清楚保留 conditional 标签，没有因此
宣告 joint contraction、全频 PDE、全 cut、闭面或课题完成。
