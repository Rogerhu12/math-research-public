# 低阶投影有限 N 等价性的 root 全文独审

状态：**PASS。完整代数证明、原源码接口及精确复跑均已核；未实施新 engine、未启动新 solver。** 审查者 Astra-visible-flex-db6f0b0e，2026-11-09。被审稿 `notes/2026-11-09-db6f-tail-quadratic-projection-equivalence.md`，SHA256 `0c07c41a96022b589633c6be58abdf4970098fdf3b879717abc46ac4d031e3a8`。

## 1. 从原源式独立核三种剥离

已直接读冻结 `general_root_tail_momentum.mjs` 的 `evaluateL/root/rhs`、`f6tail_fast_momentum.mjs` 的变分式，并对照稿中 split flux 的稳定表达式。以固定 $v=g.w2$、$E=1+v$ 记原径向数据。

第一式由 $K=L-P_\theta$ 得 $K^2/2+KP_\theta=(L^2-P_\theta^2)/2$，故 $q_2=(L^2+EP^2-P_\theta^2)/2$。这完全是有限多项式等式，没有小振幅近似。

对完整 moment，核得 $1/2+f_c=1/(d(1+d))$、$1+g_c=1/(Sd)$，从而 $F=(d^{-1}-1)/v+(1+K)P_\theta/(Sd)$。固定 $P,P_\theta$ 对 $L$ 求导，再用 $D+v(1+K)^2=ES$，得到 $F_L=A/D^{3/2}$。所以把 Jacobian 拆成单位阵、$L$ 的精确三积投影及 $R_B=vP_\theta+A(D^{-3/2}-1)$ 的原求积，确实与同一 moment 导数相符。稿中只剥离 $L$，没有把仍保留的 $vP_\theta$ 丢掉。

对 flux，原 stable factor 的分子等于 $K+1-Sd$，故 factor$=K+(1+K)g_c$；完整 flux 是 $U+UK+U(1+K)g_c$。其中线性项 $U$ 已在原 split engine 单独提取；后续候选只能再剥离 $UK$，不得重复加入或删除 $U$。

## 2. 无混叠和规范化

等距角点上，频率 $\kappa h$ 的复指数平均仅在 $N\mid\kappa h$ 时为1，因此有效周期为 $N_*=N/\gcd(N,\kappa)$。所有被替换项连同测试基最高谐波编号均为 $3M$，严格门 $N_*>3M$ 支付完整连续/离散投影相等。原 $N>4M\kappa$ 更强；M15/spacing3/N256满足该门。

核过等号反例：$N_*=3M$ 时 $c_M^3=2\sqrt2\cos^3(M\kappa\theta)$ 的常数连续平均为0，离散三倍频项留下 $\sqrt2/2$，所以不能将严格大于放松。

对 Laurent 规范化，cosine 的正负系数为 $L_j/\sqrt2$，sine 的系数为 $\mp i p_j/\sqrt2$；输出 cosine 投影需乘 $\sqrt2$。Jacobian 的零索引、对角线和异索引三类公式全部核对。$UK$ 的 sine 投影含 $k_0u_j$ 和带差频符号的 $1/\sqrt2$ 卷积；例如 $s_kc_\ell$ 在 $k<\ell$ 时的差频必须取负，稿中正确。没有遗失最外层 `pref*frequency`，也没有额外物理尺度归一化。

## 3. 脚本与独立实跑

逐段读了精确核查脚本：有理多项式字典运算、清分母恒等式、复 Laurent 卷积、$a+b\sqrt2$ 的规范化计数和 reduced-period alias 求和均是精确 Fraction 计算。脚本的若干恒等式是分解的代数一致性核查；完整导数证明仍由上一节的显式微分支付，不以一次测试代替普遍证明。

root重新运行同脚本，工具真实 exit 0；全部7项有理恒等式、4096项cos三积、3600项sin-sin-cos及alias反例通过。独立输出 `notes/2026-11-09-db6f-root-quadratic-projection-equivalence-replay.json` 与作者输出逐字节相同，SHA256 `61ae039718391a04f6237b028bcaec291899869c3e154bd69470d05d820d297c`。

## 4. 准确范围及实现审查门

这是精确等距角点/实数三角基上的**原有限 N 方程**的等价重写。非多项式余项仍保留原 N 点，未因此成为连续角积分；literal rounded trig 表也不满足精确正交，故不承诺 binary64 结果逐位相同。

后续若实施，必须保留完整点态 `rows.quad/maxQuad`、所有原 guard/停止尺度、原 root 和 RK 方程、真实输入与物理 $g$。变分引擎必须确实 import 派生 base，state-only 与 variational 的数值一致性须独立核对。显式卷积仍有自身浮点舍入；当前证明没有识别 M15 阻尼原因，也没有证明计算加速或收敛改善。

结论：被审稿§1–6通过全文独审；任何将来 engine 实现与真实求解都仍需各自审查/记录。此结果不支付 G5。
