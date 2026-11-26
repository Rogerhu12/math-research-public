# 原 M12 耦合角基的完整三行 Gram 法矩阵消费器

**状态：代数接口已证明；独立非零有限接口核已实际执行 exit 0。尚未运行真实 M12 全半面的新预条件求解，未宣称新的误差下降、精确解或完成第 5 条。**

这里消费已有 [R244](../results/R244-complete-radial-normal-preconditioning-spectrum.md) 的完整径向带矩阵与右预条件结论。新内容是原 M12 的实际耦合平面角基和完整三行 Gram 目标的专用消费器及有限验证。强分支的独立 $x/y/z$ 角列不能原样替代这里一个系数同时控制 $x,y$ 的角列。

## 1. 同一原目标的全部点协方差

沿用 `6a65-streaming-cartesian-full-gram.py` 的实际节点、权重、正目标角尺度 $b$、第一位置导数 $x_s,x_u$。在一个节点记 $\tau^2=w_s b/N$。未改变的加权残差为

$$
\tau\left(|x_s|^2-1,\sqrt2\frac{x_s\cdot x_u}{b},\frac{|x_u|^2}{b^2}-1\right).
$$

记修正的一阶导数为 $v_s,v_u$。完整微分是

$$
\tau\left(2x_s\cdot v_s,\frac{\sqrt2}{b}(x_u\cdot v_s+x_s\cdot v_u),\frac{2}{b^2}x_u\cdot v_u\right).
$$

按 $(v_u,v_s)$ 的次序，其 $6\times6$ 协方差块为

$$
K_{00}=\tau^2\left(\frac{2x_sx_s^T}{b^2}+\frac{4x_ux_u^T}{b^4}\right),\qquad
K_{11}=\tau^2\left(4x_sx_s^T+\frac{2x_ux_u^T}{b^2}\right),
$$

$$
K_{01}=\tau^2\frac{2x_sx_u^T}{b^2},\qquad
K_{10}=\tau^2\frac{2x_ux_s^T}{b^2}=K_{01}^T.
$$

这由逐行外积直接得到，保留全部三行及每个 $xy,xz,yz$ 交叉项。$K_{01}$ 本身一般不对称，不可只保对角或先错误对称化这个单块。

原 M12 的一个平面列是

$$
\beta_a(u)=(\cos(m_a u),\sin(m_a u),0),\qquad m_a=3k+1,
$$

且 $m_a$ 可以为负；高度列为 $(0,0,\cos(n_a u))$，包括 $n_a=0$ 的真常数。径向表示为

$$
W(s,u)=\sum_{i,a} c_{ia}B_i(s)\beta_a(u).
$$

实际的 $B_1$ 是物理 $s$ 导数，完整 chart 链式因子沿用原供应器；不是对单位网格坐标直接求导后遗漏尺度。令 $B_0=B$，则对角列的微分向量分别为 $B_0\beta_a'$ 和 $B_1\beta_a$。因此

$$
Q_{ab}^{de}(s_i)=\sum_j \bigl(\beta_a^{(1-d)}(u_j)\bigr)^T
 K_{de}(s_i,u_j)\beta_b^{(1-e)}(u_j),\qquad d,e\in\{0,1\},
$$

$$
H_{(r,a),(k,b)}=\sum_i\sum_{d,e=0}^1
 B_d(s_i,r)Q_{ab}^{de}(s_i)B_e(s_i,k).
$$

这恰等于原离散完整 $J^TJ$。没有删残差行、角列、径向列或不同角列的交叉块。整个计算只需保存局部节点块的 $K,Q$ 和径向带，不形成大 $J$。

## 2. 负平面频率、实系数和离散 alias

平面向量的两个复系数是

$$
\beta_a=e^{im_a u}(1/2,-i/2,0)+e^{-im_a u}(1/2,i/2,0).
$$

公式对负 $m_a$ 仍成立；它不会把负平面模式误作两个独立实 Cartesian 系数。高度非零模式的两系数是 $(0,0,1/2)$，常数只使用一个 $(0,0,1)$ 槽，另一槽严格为零。角微分在每个槽乘其真正的 $if$。

设实际 $N$ 个角节点上的矩阵序列为实值 $K_j$。完整 rFFT 给出

$$
\widehat K_\ell=\sum_{j=0}^{N-1}K_j e^{-2\pi i\ell j/N}.
$$

计算复槽乘积所需的是 $\sum_jK_j e^{iqu_j}$。先对 $q$ 取模 $N$；若结果在 $[0,N/2]$，取相应 rFFT 槽的共轭，否则取其负频率对应的原槽。这对任意离散 $K_j$ 恒等成立，没有假定原位置场、材料重参数或协方差是某个有限 Fourier 多项式，也没有截掉高频或 alias 项。新代码直接复用 R244 的 `positive_exponential_moment` 完成这一步。

整个 $Q$ 只在完成所有符号、Cartesian 分量和导数块的和以后，按转置关系平均浮点舍入误差。这一步不替换任何非对称的 $K_{01}$ 子块。

## 3. 完整径向带和保持 lambda 为零

五次 B 样条在一点最多有六个连续径向列，其物理一阶导数支撑不扩大。故只有 $|r-k|\le5$ 的径向块可能非零。按径向优先、每径向块 $C$ 个角列排列，完整标量下半带宽为

$$
\min(6C-1,n-1),\qquad n=C\,n_r.
$$

新代码累计整个局部 $(6C)\times(6C)$ 块的下三角，没有采用逐角通道对角近似。$S$ 严格沿用旧 streaming operator 已生成的所有 H1 Cholesky 因子；每个实际角列必须恰归入一组。设

$$
P=H+\eta S,\qquad \eta>0,
$$

$$
D=\operatorname{diag}(P)^{-1/2},\qquad LL^T=DPD,\qquad T=DL^{-T}.
$$

由原 $S>0$ 得 $P>0$，且 $T^TPT=I$。新实际 LSMR 只接收 $JT$，右端仍为 $-r$，**不加入正则残差行，必须保持 `damp=0`**。于是 $d=Tx$ 给出原物理问题 $\min_d\|Jd+r\|^2$ 的双射变量变换。$\eta S$ 只出现在右预条件器中，不能挪入原目标。

若原问题有零空间，不同右预条件坐标的最小坐标范数规则可能选择不同物理最小解；不能据目标相同声称逐个系数方向必相同。每个真实方向仍须回到完整物理目标试步，并重新执行实际场的原观察、连续预算及几何检查。

R244 的 $\lambda=0$ 边界在此原样保留：

$$
0\preceq T^THT\preceq I.
$$

这不提供严格正的统一谱下界；有限核得到的近单位谱不外推到整个 M12。若选取的 $\eta$ 导致实际浮点 Cholesky 失败，代码如实报错，不删列或把正则偷偷加到目标。当前消费者默认 $\eta=10^{-6}$；下述独立有限核明确用 $10^{-5}$。真实大场尚未运行。

若 $q=T^Tg$ 是新坐标的正规梯度，正确恢复式是

$$
g=D^{-1}Lq.
$$

这里不能继续用旧 H1 坐标的 $L_Sq$。新接口同时提供该恢复式和从全三行实际 `raw_transpose` 直接计算 $J^T(Jd+r)$ 的路径。后续接入暖续必须消费新恢复式或直接物理转置，不能只比较预条件后的残差数字。

## 4. 实际非零有限核

新的有限核采用 8 个非均匀径向元、裁掉两端各三列后的 7 个径向自由列、order 3 的 11 个耦合角列、$N=24$、每元 4 点求积，共 **77 个实际非零系数、2304 个残差行**。背景是明确的非旋转解析位置函数，使用非恒定物理 chart 尺度和正角尺度。独立密集 $J$ 直接用正弦/余弦公式构造，不调用新的 FFT 协方差装配。

实际命令，输出只写临时目录：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/visible-flexible-closed-surface/scripts/6a65-m12-complete-gram-normal-fixture.py --scripts topics/visible-flexible-closed-surface/scripts --out /tmp/m12-complete-gram-normal-finite-check.json
```

本会话在 `/tmp/visible-flex-6a65e705/exact-work/full-gram-precondition` 的新源码上实际执行相同入口，`--scripts` 指向公共仓库的既有消费者，实际 **exit 0**。运行环境 NumPy 2.3.5、SciPy 1.17.0；内部计时 0.4537552859983407 秒，完整装配/Cholesky 0.049929078013519756 秒。

| 实际核验 | 数值 |
|---|---:|
| 完整带 $H$ 对独立 $J^TJ$ 的相对差 | $1.4132103600468612\times10^{-15}$ |
| $T^TPT$ 对 $I$ 的相对差 | $2.11112809391451\times10^{-13}$ |
| 物理 $J$ / $J^T$ 对独立密集实现 | $8.870048367976906\times10^{-15}$ / $2.5329763021915627\times10^{-15}$ |
| 新右预条件 $J$ / $J^T$ 对独立密集实现 | $8.909831482841069\times10^{-15}$ / $5.873162433292014\times10^{-15}$ |
| 完整伴随相对差 | $9.529965072247541\times10^{-16}$ |
| 新坐标恢复物理梯度相对差 | $1.9377856976445156\times10^{-16}$ |
| 未正则化的完整物理正规残差相对差 | $6.371760682693426\times10^{-15}$ |
| 此有限核的 $T^THT$ 最小 / 最大特征值 | $0.9963263127389007$ / $0.9999980771951962$ |
| 完整 $H$ 中不同角通道块占 Frobenius 范数比例 | $0.6868503780806114$ |
| 两端修正完整两 jets 最大值 | $0$ |

有限核实际经过 576 次按装配块累计的 alias 频率对；同时包含正、负平面频率与高度真常数。这个核没有使用原 M12 大场，不冒充真实非线性迭代改善。

## 5. 源身份与下一真实消费者

| 文件 | 字节 | SHA-256 |
|---|---:|---|
| `6a65-m12-complete-gram-normal-preconditioner.py` | 14055 | `f19a09b0d4efbb9f6f8122de446f371306d291dfa47cf0dfeb7727fe0e0b18f9` |
| `6a65-m12-complete-gram-normal-fixture.py` | 8423 | `c6a358a17f879689435411d7dcf8bdd70900dcf9ec5eca67b7b65ede4f6e78fa` |
| 既有 `6a65-streaming-cartesian-full-gram.py` | — | `0c1b791f7c8526b366759ac86e52dd9339f8817e081b86f992ade75b6d22323c` |
| 既有 R244 helper | — | `1fdaa80e4a56631c858c1a0f4f31557ec8a72254170b6b1df4ec16cbe6437361` |

完整可重算 `finite-check.json` 不提交；本次临时文件 3273 字节，SHA-256 `0e030fe275ed189a16e79f49e345c1e0e5a6421352e71fb83f59536bc69ea774`。根 README 第 15 条优先。

对于固定 h487/M48 的 486 个径向自由列和 146 个角列，$n=70956$、半带宽 875，一个实际 double 带数组为 497259648 字节，约 474.224 MiB；这是静态存储数量，不是已测大场 RSS 或耗时。完整 $H$、Cholesky 因子和其它数组都必须留在 CI runner，不能用本地小核占用来推断大场资源。

下一真实消费者将把现有 `StreamingLinearized` 实例传给 `CompleteGramRightPreconditioned`，保持所有原行/列/权重和本次真实暖初场，使用 `blocks.physical_gradient` 或 `raw_transpose` 记录物理正规残差，再走同一完整非线性试步和全部观察/连续预算。当前实际运行的 M48 source `3046ad8c20d2d64c435ad9b0bd50cde5e31c0798` 未热改；是否采用本预条件器、以及下一真实 solve 的 $\eta$ 和预算，依据该 run 的实际正规残差决定。
