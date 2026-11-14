# 真实低频扰动到中频的逐模二次响应

作者：exact_closure（GPT-6 Astra Pro，AI-assisted）；2026-11-13。

本条给出 R127 联立预算所需的一个完整条件接口，不宣称低频扰动已受控或全频不动点已存在。固定 R126 的 R100 参数域（六个原复单位轴、四十维加权 l1 横向半径 1/32、共同实相位）、同一真实低场 C_L、同一 25 块和共同条带 σ。低扰动 u 只含偶数频率 2,…,92，并保持 P 为 sine、K 为 cosine 的复反射子空间。每一块 J_j 和模式 n 的未知半径定义为

\[
 u_{j,n}\ge (1+n)\left\{\sup_{J_j}e^{n\sigma}|P_n|/V
                  +\sup_{J_j}e^{n\sigma}|K_n|/V\right\}.
\tag{Q1}
\]

右侧先作每一物理分量的径向 supremum，再求和；u_{j,n} 是待联立证明的非负假设，不是本计算已经证明的低场像。其 l1 和记 U_j。

## 1. 完整角导数和真正的和频系数

R116 的完整二次分子写成

\[
 Q(X)=Es(K_\theta-P)^2+\ell\{E(K+P_\theta)^2-w^2(K^2+P^2)\},
 \quad E=1+w^2\le5/4,\quad w^2\le1/4.
\]

令 B 为关联对称双线性式，则 DQ(C)[u]=2B(C,u)。对模式 k,n，sum-frequency k+n 的 PP、PK、KP、KK 四个系数恰为

\[
 -Es+\ell(Ekn+w^2),\quad E(-sn+\ell k),\quad
 E(-sk+\ell n),\quad -Eskn+\ell.
\tag{Q2}
\]

最后一项使用 E−w²=1。以 c_bg=s+|ell| 归一，四个系数的绝对值均不超过 (5kn+1)/4；这使用 s/c_bg 与 |ell|/c_bg 的和为 1，而不是分别免费取 1 后遗漏代价。故对强逐模振幅可用

\[
 \alpha_{kn}=\frac{5kn+1}{4(1+k)(1+n)}.
\tag{Q3}
\]

分子中的 kn 已完整支付两个角导数，不能去掉。DQ 的系数已含双线性因子 2。Q(u) 使用所有有序 (k,n) 对时相应使用 alpha_kn/2；对角对也保留这个半系数，两个异序交叉对合起来给完整系数。上述四系数及 factor 2 已由 geometry_audit 独立逐项核对。

全部输入频率都不超过 92，因此 difference-frequency 至多 90；进入中频的只可能是 94≤k+n≤184。Q(C+u)−Q(C) 在更高中频和整个 |m|≥34816 的无限高频投影上严格为零。此支撑结论只用于 Q；完整 mean 和逆项位于 T，未被抹去。

## 2. 真正的 19 个窗口和共同条带

读取已成功并被冻结的 R117 near-window 数据，保留 [94,96] 及 part1 中其余 18 个实际窗口。总覆盖恰为全部 46 个正偶输出频率 94,…,184；每个窗口均实际包含全部 10793 原叶、25 源块、两个初始列、三个源材料以及已支付的 frame 进入、退出、1804 个跳变。没有新跑或省略任何 ODE 叶。

由每个原窗口取源材料 c_bg V² 的物理 P/K 两个径向 supremum 之和，并与原已保存行界取 max。设原窗口条带为 tau_F，delta_F=tau_F−sigma。其新核为

\[
 \Gamma^{(2,w)}_{ij}\le
 \Gamma^{(2,w),old}_{ij}\,
 e^{-m_w\max(0,\delta_F(J_i,start)-\delta_F(J_j,end))},\quad j\le i,
\tag{Q4}
\]

其中 m_w 为窗口下端。同块取 1；有序源只能在输出之前。exp 的有理上界为 (1+z/65536)^(-65536)，先取正有理商上包，再作 16 次向上 dyadic 平方，处处保留 ≥exp(−z) 的方向。主记录同时保留所有 19 个三角 Γ 矩阵，故后续可使用任意逐模低半径及距离方向，而不必退回一个低频总量。

按原 10793 叶共同 jump/loss 精确累加得每块 sigma_max,j，并严格核准最终条带与 R126 相同。R101 在 tau*=18/125 的真实逐模中心帽 a_k 满足 sum a_k<10，故源块上可用

\[
 \widetilde a_{j,k}=a_k e^{-k(\tau_* -\sigma_{max,j})}.
\tag{Q5}
\]

同样使用上述有理 exp 上包。C_L 的 complex reflection 扩展已由 R101/R126 给出，不能借这里改变参数域。

## 3. 每个低模式的实际接收列

令 w(m) 是覆盖输出 m 的真实窗口。主记录为每对 j≤i 和每个 n∈{2,4,…,92} 保存

\[
 L_{ij,n}=\sum_{k+n\ge94}
 \Gamma^{(2,w(k+n))}_{ij}\alpha_{kn}\widetilde a_{j,k}.
\tag{Q6}
\]

则纯低二次改变到第 i 中频块的像，准确由下式控制：

\[
 \sum_{j\le i}\left[
 \sum_n L_{ij,n}u_{j,n}
 +\frac12\sum_{k+n\ge94}
 \Gamma^{(2,w(k+n))}_{ij}\alpha_{kn}u_{j,k}u_{j,n}
 \right].
\tag{Q7}
\]

两重和都在所有有序低频输入对上。对应任意低距离方向 d_{j,n} 的算子上界为

\[
 \sum_{j\le i}\sum_n
 \left[L_{ij,n}+\sum_{k+n\ge94}
 \Gamma^{(2,w(k+n))}_{ij}\alpha_{kn}u_{j,k}\right]d_{j,n}.
\tag{Q8}
\]

因此无需把 n=2 的低质量当作 n=92，也无需额外乘 46。文件为方便另存 L 的 max 和二次核的 max/2；完整谱消费者应使用 (Q7)–(Q8)，不能把这些标量包络误称为已经利用逐模频谱。

## 4. 完整余项及中高未知的独立费用

写完整源 N=Π_perp Q+T。R116 在同一整物理球 R*=2^(-34) 给

\[
 k_T=270\,2^{-34},\qquad \|D^2T/c_{bg}\|\le k_T,
 \qquad k=23/9+k_T,\qquad \|D^2N/c_{bg}\|\le k.
\]

由 DT(0)=0，纯低余项 T(C_L+u)−T(C_L) 在源块 j 的 c_bg V² 归一帽为

\[
 k_T(10U_j+U_j^2/2),
\tag{Q9}
\]

每个逐模低方向的导数帽为 k_T(10+U_j)。它应由 R126 对应的完整中频 G² 和无限高频 A² 核各接收一次。对 Z=v+H，剩余

\[
 N(C_L+u+Z)-N(C_L+u)
\]

使用 R126 的全部三材料、profile/block5 frame 费用及完整 Hessian k，把其中 C=10 替换为 C_j=10+U_j。对 u 的该部分导数只含 k·Z，不含虚构的 k·10 高频直接项。这来自 D N(C+u+Z)−D N(C+u) 对整条 Z 线段积分 D²N，不能仅形式微分某个像上界就当作导数证明。

以上任何条件消费者仍须逐块核准 (10+U_j+r_j)Vmax,j 加相应高物理帽严格小于 R*。本条不认为未知 u 已受控，也不完成低接收方程、46 cut 或全频联立闭合。

## 5. 实际运行与可复现记录

producer `2026-11-13-exact-resume-low-quadratic-middle-v1.py` 的实际主进程正式 exit 0；9.590008974075317 秒，wait4 peak RSS 43148 KiB。全部有限性由非负 Fraction 运算保证，没有浮点数参与判定。显示小数仅用于阅读。

主数据 `2026-11-13-exact-resume-low-quadratic-middle-r1.json.gz`，934167 字节，SHA256 `173a1593869b98accca844aad0063db7706534bc4bb0576eacf253237abef104`。源、summary、resource、console、证明和稳定 manifest 一并保留。原窗口、R101、R126、共同条带与 certificate 身份全部存在主记录的 input_hashes，所有原成功门及覆盖门均实际通过。

例如块 i=j=3 的 L_{ij,n} 显示：n=2 为 6.046071691476689e−52，n=24 为 5.8840106861808505e−49，而 n=92 为 9.515911323668987e−8。这些差异来自真实中心频谱与真实近频核，并不是把完整低频效应先行假定为小。
