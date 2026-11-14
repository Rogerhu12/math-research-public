# 真实连续全矩阵 projector 验证器与四格公开 pilot

## 输入、范围与分工

原公开 run `43588509643` 已实际完成全部 5970 个 cut-to-waist 提案格，
保存每格完整 193×96 dyadic 端 frame、准确连续正权重和全部边界诊断。
提案 native SHA256 为
`6dbc3acfcfbdd051c83344561f13102d30f20699db1e0046357d0ede1ec79639`。
916,497,210 字节的原 frame artifact `14112195633` 继续保存在本公开
仓库 Actions；本验证不重做任一提案格，也不下载整个 frame 集到本地。

本次首先在一个公开 runner 中消费互斥的四个实际格
`[0,1)`、`[76,77)`、`[3300,3301)`、`[5969,5970)`，分别覆盖真实 cut、
原提案最大 step-matrix 范数所在格、最小 rho 所在格和腰端。
这是完整连续全矩阵消费者的四格执行门，不是 5970 格结论。任何真正
成功的格在后续全域派发中都须排除并原样复用；失败的原 native/过程保留。

同一公开 run 先运行全部 193 状态的人工 skew/hyperbolic 代数对象和
真实 sec/tan 接口门。人工对象只能验证代码约定，不能代替原候选的四格。
后续所有新数值门均在本公开仓库 Actions 中执行；本地只做源码、SHA
和既有字节的核对。公开实际输出才是可消费记录。

## 新 exact 局部多项式定义

没有假设原提案未保存的浮点 operator 矩阵在别的 runner 上逐位相同。
每个原完整右端 frame `Q` 都作为 exact dyadic 锚点。新 reference 的
物理修补背景三次系数以及 beta、gamma、K、s 的 Taylor 系数明确记录
为新的 dyadic 数；全连续真背景相对这些参考系数的误差按完整原 scalar
germ、第三 jet、intrinsic primitive 以及准确 candidate/repair 支付。

reference 运算定义为完整有限 Fourier 代数及三阶径向截断；所有超出
三阶的真实径向乘积进入 uniform Wiener 误差。角支撑和反射零只在
数学上准确不存在、且有向区间确实含零时置零。193 状态有限矩阵保留
全部 96 odd、96 nonmean even 以及独立 even mean。

两个完整 nonlocal 项保留为
`-2 beta Q_phi I(u h_1+K v h_2)` 和 `gamma mean(h_2) J(K)Q_phi`。
第一个项的中间 primitive 全部 128 个模式均进入矩阵，最后才投影到
193 状态；没有把中间支撑提前截到 96。物理完整 L2 Gram 始终保留。

准确权重 `R=diag(I_96,rho I_97)` 对全部 even 状态连同 mean 一起作用。
rho 为原记录的正 dyadic 节点之间准确线性插值。`1/rho` 的 reference
采用准确三阶几何级数，剩余项有明确全格界；even 对角完整加入
`rho_prime/rho`。得到一个新定义的准确三阶矩阵多项式 A0 与有向的
完整真算子差 `||A-A0||<=epsilon`。

以 `s=(r-right)/(left-right)`，新 exact 多项式 frame 定义为

\[
 X_0=Q,\qquad
 X_{n+1}=\frac{left-right}{n+1}
       \sum_{j=0}^{\min(3,n)} A_{0,j}X_{n-j},\quad 0\le n<24.
\]

它由已经记录的系数及锚点唯一确定，Arb 运算只对这一 exact 对象作
有向包络。低次微分残差由递推定义准确抵消；仅最高余项需要计入。
这避免把相关区间重复相减形成伪残差。

## 完整 Gram、normal 变化及 signed rates

原锚的准确正交投影是 `P0=Q(Q*Q)^(-1)Q*`；不能把不完全正交的
dyadic Q 直接当成精确正交矩阵。首先用完整 Gram 和全矩阵增长界验证
全格 X 的最小奇异值为正，再用已得 signed restricted rate 改善该界。
每一步改善都只使用先前已经有效的下界，避免循环假设。

令 `Y_n=(I-P0)X_n`，`a_j>=||A0,j||`，
`b_j>=||(I-P0)A0,j P0||`。准确递推给出

\[
 \|Y_{n+1}\|\le\frac{|left-right|}{n+1}
       \sum_j\bigl(b_j\|X_{n-j}\|+a_j\|Y_{n-j}\|\bigr),\quad Y_0=0.
\]

因此使用完整 normal 多项式而非 `h||A||` 控制 span 变化：若全格
`sigma_min X>=g_s>0`，同 rank 正交投影恒等式给

\[
 \|P(r)-P_0\|\le
   \min\!\left(1,\frac{\sum_n\|Y_n\|}{g_s}\right).
\]

令 H=Sym A。锚的完整 restricted 最大特征值通过一个选出的 dyadic
辅助 eigenbasis、其完整 Gram 以及有向全 congruence/Gershgorin 界验证，
不将浮点 eigenvalue 当结论。补空间也从准确 `I-P0` 投影获得并验证
全部 97 列 Gram。由投影距离 delta，forward mu、backward nu 和 cross
各保留 `||Delta H||+2||H0|| delta`，尤其保留 mu、nu 的负号。

完整矩阵微分残差给

\[
 e\ge\|(I-P)AP-(I-P)P'P\|
   \le\frac{\|X'-A_0X\|+\epsilon\|X\|}{g_s},
 \qquad c\le2\|PH(I-P)\|+e.
\]

## 全接口与后续全局消费

每个新的 X 左端和下一个原保存 frame 之间都重新比较准确正交投影，
完整 193×96 normal 残差除以有效 Gram 下界给出真实接口距离 delta_j。
即使该距离很小也必须保存，不能当成零。

delta_j 是 `||P_plus-P_minus||`，不是混合传播中的 tangent 系数。
全局消费者须在 `delta_j<1` 下支付
`sec=1/sqrt(1-delta_j^2)` 与 `tan=delta_j/sqrt(1-delta_j^2)`，或消费
另行验证的完整接口 block。所有真实 source 跳也必须保留。

局部四格 native 不授予任意全局 inverse。后续必须覆盖 5970 格、验证
准确两端完整边界，并以保留径向衰减的正 Green/Riccati 门消费全部
signed rate、coupling 和接口。原无权重 cap-cut 的 LR、DL 需要准确
变换到本权重及新锚点，不能直接抄用。

未知高输入、全部独立源、原 ac1 到修补中心的算子比较、真实响应、
参数 Schur 和非线性闭合均继续单独保留。
