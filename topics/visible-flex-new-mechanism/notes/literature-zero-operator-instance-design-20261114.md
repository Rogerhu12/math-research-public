# R37 的有限 N 控制编译与首轮数值设计

日期：2026-11-14。性质：**可复现计算设计，尚无本轮真实研究输出**。

本文件配合 `scripts/literature_zero_operator_instance.py`。它把
[R37](../results/R37-closed-geometry-zero-period-operator.md) 的有限维存在论证落实为一套有限控制；真正的几何设计、框架积分及优化只在本公开仓库的 GitHub Actions 运行。本地仅完成文末的初等公式与接口检查。

**范围。** R37 已证明某些充分大但未定量给出的有限 N 存在准确全零算子。此脚本冻结 binary64 参数后只报告该具体控制的数值残差，不把小残差当成准确 M=0，不把浮点桥当成已认证的准确闭合桥。它没有得到嵌入闭曲面、reach 下界或精确有限等距族。即使本轮全部数值残差很小，这些剩余要求仍须另付。

## 1. 固定十二种真实整圈

保持 R37 的四个状态

$$
(h_i,d_i)=(1,0),(1,1),(1,-1),(2,0),\qquad
a^2=(9+\sqrt{33})/8.
$$

每组的三种曲率是

$$
k_{i,0}=0,\qquad k_{i,+}=a+\alpha_i+\beta_i,
\qquad k_{i,-}=-a-\alpha_i+\beta_i,
$$

相应常段目标为 $\omega=(d_i+k)/h_i$。每种状态走 N 个真正完整的框架周期

$$T(k)=2\pi/\sqrt{1+k^2}.$$

默认首轮取 **N=16384**，八参数限制在 $[-0.2,0.2]^8$。N 只是本轮固定设计选择，没有由此声称宏观厚度；以后改变 N 必须另记设计身份。

框架方程为 $F_s=F\Omega(k)$，角速度轴为 $(-1,0,k)$。完整圈的末框架使用其解析恒等式 $I$，不是把长时间 ODE 的漂移强行重置为 $I$。同时保留完整圈的非零中心线位移：设 $\nu=(-1,0,k)/\sqrt{1+k^2}$，则

$$
\Delta\alpha=h^2NT(k)\nu\nu_1.
$$

框架整圈一般不是中心线的闭圈。所有后续闭合诊断都包含该轴向位移。

## 2. 正、光滑且有明确 omega 增量的连接

在归一化时间 $t\in[0,1]$ 使用全平阶跃

$$
S(t)=\operatorname{expit}\!\left(\frac1{1-t}-\frac1t\right),
$$

并在左右分别外延为 0、1。每个长度为 $\tau$ 的斜坡规定

$$
k=k_0+(k_1-k_0)S,\quad
b=\frac1{2h}=b_0(1-S)+b_1S+\eta S(1-S),\quad \eta\ge0.
$$

端点形式直接保存 $b_0,b_1,\eta$，不用展开多项式后相减来恢复端值。两端 b 正即全段 b 正，且全部端点导数与常值芽匹配。实际 primitive 是

$$
\omega=\omega_0+(k_1-k_0)
\left[b_0S+\frac{b_1-b_0}{2}S^2
+\eta\left(\frac{S^2}{2}-\frac{S^3}{3}\right)\right].\tag{1}
$$

因此 $\omega_s=k_s/(2h)$，该斜坡的真实增量为

$$
\Delta\omega=(k_1-k_0)\left(\frac{b_0+b_1}{2}+\frac\eta6\right).\tag{2}
$$

连接首先把输入 k 接到 0、输入 b 接到 $1/2$；最后从 $(k,b)=(0,1/2)$ 接到输出状态。中间普通框架词一律保持 $b=1/2$，其 k 首末为 0，故 omega 净增量为 0。

另插一对 $k:0\to1\to0$ 的斜坡，上、下行各取
$b=1/2+\eta_\pm S(1-S)$，其额外增量准确为

$$\Delta=(\eta_+-\eta_-)/6.$$

脚本扣除输入、输出端帽的 (2) 后得到所需 $\Delta$，并用光滑严格正的选择

$$
\eta_\pm=\eta_0+3\sqrt{\Delta^2+\delta_0^2}\pm3\Delta,
\qquad \eta_0=0.05,\quad\delta_0=0.25.
$$

这避免了 $\max(\Delta,0)$ 的折点，使八参数附近的控制仍有光滑依赖。普通斜坡默认长度 0.06，omega 门每段长 0.25。连接两端另保留长 0.02 的常值平台，所以外端确有开放常值邻域。

**一个 omega，不能逐段改规范。** 实际定义是从全曲线唯一初值积分 (1)。输出里的每段 `omega0` 是按前段端值顺序累积的浮点缓存，不是独立控制变量。原始浮点增量、接缝及全周期漂移全部保留；没有因目标值已知而在末端把 omega 改写成它。浮点 cache 接缝为零不构成严格闭合证明。若以后认证某个有限 N，可把 binary64 k、b、eta 的增量用有理数准确累加，并单独认证端点方程。

## 3. 三个正平台时间匹配框架

记

$$X(\theta)=\exp(\theta\Omega(0))=R_x(-\theta),$$

$$H=\exp\left(\frac\pi{\sqrt2}\Omega(1)\right),\qquad
Z(\phi)=HX(\phi)H=R_z(\phi).$$

在框架词中使用曲率 0、1 的平台，并用上述固定光滑斜坡连接。其三个自由平台时间来自恒等前缀

$$
X(2\pi+x_1)Z(5\pi/2+x_2)
X(2\pi+x_3)Z(3\pi/2).
$$

去掉斜坡且 $x=0$ 时它准确为 I；三个端点导数分别对应三条独立的旋转轴。所有时间都已加完整周期，在 $|x_j|<\pi-0.03$ 内保持严格正。

共同 block 的每个连接以 I 为目标。两条固定桥的目标分别为

$$g_1=R_x(\pi),\qquad g_2=R_y(\pi).$$

其末端词可用 $X(\pi)$ 与
$X(3\pi/2)Z(\pi)X(\pi/2)$ 实现。输入端帽、omega 门、全部光滑斜坡和输出端帽都包括在真实端点乘积里。

每个连接的三变量拟合最小化完整 $3\times3$ 末框架差。Jacobian 通过平台指数的准确导数计算，同时报告一次中央差分核对。默认最多 50 次函数评价；未过 $2\times10^{-9}$ 端框架门时，不允许把该连接当成已闭合控制继续优化。

变 k 斜坡用保持旋转乘积结构的四阶 commutator-free Magnus 公式积分；代码没有对结果做 SVD 投影、Gram–Schmidt 或端点重置。右乘 ODE 的早时加权指数置于左侧，BCH 首个非对易项是 $+\tau^3[A_0,A'_0]/12$。默认每段 96 步。

## 4. 真实八参数矩阵目标

对每个常段使用 R37 的准确密度

$$M_s=\mathbf w(h,d)\boldsymbol\ell(k,h,d)^T.$$

对光滑段直接使用已发表的低导数积分公式，令

$$d=h\omega-k,\quad \omega_s=k_s/(2h),\quad
d_s=h_s\omega-k_s/2,$$

$$q_0=\omega_s/h-\omega h_s/h^2,\quad q_1=-h_s/h^2,$$

$$K_0=k\omega^2-(k^2+1)\omega/h,\quad
K_1=2k\omega-(k^2+1)/h.$$

由这些量一次积分得到 $p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_0,t_1$，组成

$$
M=\begin{pmatrix}
p_0&2r_1&-4r_0\\p_1&2s_1&-4s_0\\p_2&2t_1&-4t_0
\end{pmatrix}.
$$

每个光滑段两端 $k_s=h_s=0$，所以逐段分部积分没有漏掉端项。程序不拟合多项式采样、不把 trace 投影为零；完整九个元素和实际 trace 都保存。

把共同 block 记为 W，两条后续桥记为 $B_1,B_2$。Klein 八边总矩阵的正确归一是

$$
\frac{M_{\rm total}}{8N}
=F_{\rm bulk}+
\frac1N\left(M_{W,\rm connectors}+\frac{M_{B_1}+M_{B_2}}2\right).\tag{3}
$$

取逐行坐标但删去 $(3,3)$，以 R37 零参数处的**准确整圈导数**构造固定 $8\times8$ 预条件矩阵。不随迭代改变尺度，不通过归一化改变 h 或几何。真实矩阵及未预条件范数同时输出。

外层最多 32 次函数评价、900 秒设计预算。Jacobian 使用绝对步长 $2\times10^{-5}\max(1,|p_j|)$ 的中央差分；预算允许时，对最终实际控制做一条独立方向差分比较并保存奇异值。设计预算用尽时保存已经完整计算的最佳控制，不制造一个成功状态。

## 5. Klein 位置相消和真实接缝分别保存

使用类型词 $1,2,1,2,2,1,2,1$。每种路径的起点恰好覆盖 Klein 群的四个元素；理想群复制的总位置和确实为零。

但有限精度桥端若只接近 $g_j$，直接按准确群元放置复制块会留下真实框架接缝。因此同时输出两种核对：

- **自然连续框架传播：** 完整乘上每一条实际数值路径的末框架，保留全周期 frame 与 alpha 闭合残差。
- **理想 Klein 放置：** 保存相消后的位置和，并逐条报告其 frame seam；它不能用来遮掩前一种误差。

omega 也沿八条边真实顺序累积。若某条路径相对原 primitive 有常偏移 $\delta$，矩阵变换为

$$M_\delta=T_\delta M T_{-\delta},\qquad
T_\delta=\begin{pmatrix}1&\delta&\delta^2\\0&1&2\delta\\0&0&1\end{pmatrix}.$$

程序保存按该规则顺序传播的全周期矩阵及其与 (3) 的差。物理带范围使用全部 omega prefix 偏移的最大绝对值，不能只用可能互相抵消的最终漂移。

## 6. 完全冻结后的精化

设计完成后冻结：八参数、N、所有常平台时间、全部斜坡控制、omega 门、h 定义和一个物理 $\xi$ 区间；整个控制 JSON 的 SHA256 是这次设计身份。

物理区间只在冻结时选一次：由控制的代数极值给 omega 范围，取两端都远离 $\xi+\omega=0$ 的长度 1 区间。二次正 b 的极值以及 omega 的单调端点值不依赖采样格。它们仍是公式的浮点评价，未冒称区间算术认证。加密时不重选 $\xi$、不改变尺度、不重解平台时间，也不调整八参数。

默认核对三档

| 档 | Gauss 每斜坡节点 | CF4 每斜坡步数 | 是否重新拟合 |
|---|---:|---:|---|
| 设计控制再评估 | 64 | 96 | 否 |
| 2 倍 | 128 | 192 | 否 |
| 4 倍 | 256 | 384 | 否 |

常圈与常平台保持解析求值。每档输出原始 M、trace、矩阵档间差、frame/alpha/omega 闭合、h/omega 范围、物理带范围及桥接缝。alpha 闭合同时除以球面弧长和真实中心线弧长 $\int h^2 ds$；二者均不冒充整曲面的直径 D。

若 M 的精化稳定在非零值，不能把它写成准确算子。若 frame closure 精化稳定在非零值，也不能通过重新求解桥来称作同一控制的收敛。需要改变控制时，应保留旧输出并创建新设计身份。

## 7. 公开 Actions 命令与数据界限

首轮完整命令：

```bash
python topics/visible-flex-new-mechanism/scripts/literature_zero_operator_instance.py \
  --turns 16384 --quadrature-n 64 --frame-n 96 \
  --validation-multipliers 1 2 4 \
  --ramp-duration 0.06 --gate-duration 0.25 --end-pad 0.02 \
  --gate-eta-floor 0.05 --gate-smoothing 0.25 \
  --frame-max-nfev 50 --frame-gate 2e-9 \
  --parameter-bound 0.2 --jacobian-step 2e-5 \
  --max-nfev 32 --design-seconds 900 \
  --out "$OUT/zero-period-finite-N-instance.json"
```

研究入口同时要求 `GITHUB_ACTIONS=true` 和
`GITHUB_REPOSITORY=Rogerhu12/math-research-public`。输出只保存控制定义、参数、矩阵及汇总，不保存每个长圈的所有采样点。单文件大小在写出前强制检查小于 5 MB。

当前脚本 SHA256：`f0d25654580e91ec43a2acdb498ed363bb58c5ec424e102b67ecae0d9a448cbe`。

## 8. 已完成的开发检查和仍需实际计算的部分

本地只运行 `--toy-check` 与 Python 编译检查。报告为
`notes/literature-zero-operator-instance-toy-20261114.json`，SHA256
`e698d0d39a50f27d3ff069cfbd68da3e637e09d44acef17660d30f8b8cc2ae17`。

该小检查不编译十二圈几何、不解优化问题。结果：常段两种密度公式差 $5.55\times10^{-17}$，点态 trace 身份差 $2.78\times10^{-17}$，omega 双门身份差 $1.11\times10^{-16}$；完整圈轴向位移公式、Klein 词均为零差；常控制 CF4 差 $1.54\times10^{-15}$；恒等前缀差 $1.66\times10^{-15}$，$g_2$ 词差 $4.47\times10^{-16}$；一般三旋转乘积的解析 Jacobian 与中央差分最大差 $2.19\times10^{-11}$。

repo_sources 已只读独立核对低导数密度、CF4 的右乘符号、$g_2$ 词、(3) 的因子、omega 平移共轭、端点 b 控制与固定设计精化。其提出的 prefix-omega 范围修正和公开仓库入口门已落实。

**下一实质检查。** 先用真实输出判断有限 N 的八参数修正是否落在邻域内、桥是否成功及固定控制加密是否稳定。若得到可用的显式实际控制，再把 [R39](../results/R39-explicit-moment-circle-and-third-order-range.md) 的成对 bump 接上，计算两条真正三阶 forcing 的完整 ruling 与周期函数。仍不能把二阶 circle $X+\varepsilon Y_\theta+\varepsilon^2Z_\theta$ 当成固定度量的精确有限族。
