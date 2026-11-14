# R142：D2 高角补余的等距行压缩

**状态：已证明。** 对本文明确的 D2 原生三场族，在同一有限角网格上，
高 Gauss、高梯形 Codazzi 和高 Gauss2 Codazzi 的全部点值二范数目标，可以
等距地改写为更少的 Fourier 行。保留频率以上直到 Nyquist 的所有独立行均
被保留；这是同一有限目标的坐标变换，没有降低角分辨率、改变物理度量或
替换连续误差证明。当前浮点实现的实际差异在 §7 明确记录。

## 1. 空间、网格及完整独立行

令 `W=4H`，计算角取

\[
 \xi_j=2\pi j/W,\qquad j=0,\ldots,W-1.
\]

对向量 `v=(v_j)`，本文的两个 D2 子空间分别为

\[
\begin{aligned}
 V_+&=\{v:v_{j+W/2}=v_j,\ v_{-j}=v_j\},\\
 V_-&=\{v:v_{j+W/2}=v_j,\ v_{-j}=-v_j\},
\end{aligned}
\]

下标按 `W` 取模。记

\[
 c_k(j)=\cos(2k\xi_j),\qquad s_k(j)=\sin(2k\xi_j).
\]

则

\[
 V_+=\operatorname{span}\{c_0,\ldots,c_H\},\qquad
 V_-=\operatorname{span}\{s_1,\ldots,s_{H-1}\}.             \tag{1}
\]

证明：有限几何级数给出

\[
 \sum_{j=0}^{W-1} e^{2\pi i qj/W}
 =\begin{cases}W,&W\mid q,\\0,&W\nmid q.\end{cases}
\]

对有限 Fourier 展开，半周周期使所有奇数频率系数为零；反射的正、负
特征条件分别留下余弦、正弦系数。最高独立频率为 `W/2=2H`，其中
`c_H(j)=(-1)^j`，而 `s_H(j)=0`。这同时证明 (1) 的张成性与独立性。

令已保留阶数为 `K<H`。原有限偶投影保留 `c_0,...,c_K`，原奇投影保留
`s_1,...,s_K`。其各自高角补空间的完整独立行因此为

\[
 c_{K+1},\ldots,c_H;\qquad s_{K+1},\ldots,s_{H-1}.       \tag{2}
\]

偶高空间有 `H-K` 行，奇高空间有 `H-K-1` 行。这里的“高”指完整有限
网格投影的正交补，不对连续函数的无限 Fourier 尾作任何截断声明。

## 2. Nyquist 权与准确等距恒等式

由上述几何级数，普通模式 `1<=k<H` 满足

\[
 \langle c_k,c_l\rangle=(W/2)\delta_{kl},\qquad
 \langle s_k,s_l\rangle=(W/2)\delta_{kl}.
\]

此外 `||c_H||^2=W`；它与其余余弦行正交。设 `v` 已在偶高空间，则其
普通 Fourier 系数与 Nyquist 系数为

\[
 a_k=\frac2W\langle c_k,v\rangle\quad(K<k<H),\qquad
 a_H=\frac1W\langle c_H,v\rangle.
\]

原消费者对点值采用 `sqrt(2/W)` 归一化，因此

\[
 \left\|\sqrt{2/W}\,v\right\|_2^2
   =\sum_{k=K+1}^{H-1}a_k^2+2a_H^2.                    \tag{3}
\]

压缩向量必须包含 `sqrt(2)*a_H`。等价地，偶压缩矩阵 `C_+` 的普通行是
`(2/W)c_k^T`，最后一行为 `(sqrt(2)/W)c_H^T`。奇压缩矩阵 `C_-` 的每一行
为 `(2/W)s_k^T`。奇空间没有 Nyquist 行。于是对相应高空间中的 `v`，

\[
 \|C_\pm v\|_2^2=\|\sqrt{2/W}\,v\|_2^2.              \tag{4}
\]

定义 `Q_±=C_±/sqrt(2/W)`，则

\[
 Q_\pm Q_\pm^T=I,
 \qquad Q_\pm^T C_\pm v=\sqrt{2/W}\,v.                 \tag{5}
\]

式 (5) 也给出旧点值行的准确回构。所有权重、径向平均和组间拼接都可以
在此变换之前或之后实施，因为它们是线性操作且不改变角奇偶性。

## 3. 当前 provider 的解析 D2 前提

这一前提来自实际场定义，而非从少数样本拟合对称性。当前入口是
`RawBumpDAE` 及保留其角公式的 clean、exact-cylinder、turn-mesh 子类，
使用 `physical_bumps`、`positive_bernstein`，中央基为 `balanced_seed`
或 `circle`。以下是在它们已明确的参考相位上的结论。

固定 balanced seed 的半径 `rho_*(xi)` 是偶的、`pi` 周期函数。准确的
材料坐标 `U_*(xi)=arc_*(xi)/a0` 因而满足

\[
 U_*(-\xi)=-U_*(\xi),\qquad
 U_*(\xi+\pi)=U_*(\xi)+\pi.
\]

移动计算角

\[
 U(s,\xi)=(1-\beta(s))U_*(\xi)+\beta(s)\xi
\]

保留同样两个关系。因此 `U_xi` 是偶的 `pi` 周期函数，`U_s` 是奇的
`pi` 周期函数，`U_s/U_xi` 也为奇函数。物理 `a,a',a''` 和 bump 参数
都与角无关。

原生 correction 的 `n,l` 只含 `cos(2k xi)`，`m` 只含 `sin(2k xi)`。
seed lifting 仅向 `n` 添加径向权乘偶的 `1/rho_*`（或圆基常数）。
正 Bernstein 尾的弯折角是 `alpha(-y)=-alpha(y)`，故
`kappa(y)=alpha'(y)` 是偶函数。其完整尾 II 是

\[
 (n,m,l)=\kappa(a\sin U)
      (\cos^2U,-\sin U\cos U,\sin^2U).
\]

这一表达式的 `n,l` 为偶的 `pi` 周期函数，`m` 为奇的 `pi` 周期函数。
乘任何实际径向 lifting 权，或对中央、尾、径向参数求导，均不改变这些
角对称性。准确中央柱的节点约束也保留相同空间。

完整 Gauss 缺陷 `G=ln-m^2-K_g` 为偶函数。在移动角中，Codazzi 的角算子
`U_xi^{-1} d/dxi` 交换奇偶，而对流项 `(U_s/U_xi)d/dxi` 保持奇偶。
故完整 `R_n` 是偶的，`R_m` 是奇的；半周周期同时保留。相邻节点梯形
平均与真实 P1 单元的 Gauss 点平均只沿径向组合这些函数，也保留对称性。
因此本题三种高角补余，以及对任意独立原生未知量方向的导数，都满足
§1–2 的同一 D2 前提。

这个论证只使用实际三场及其一阶 Codazzi 公式，不除以 `n`，也没有引入
新的曲面正则性要求。完整场的定义见
[`fd2d_gc_raw_bump_dae.py`](../scripts/fd2d_gc_raw_bump_dae.py)、
[`fd2d_gc_blended.py`](../scripts/fd2d_gc_blended.py) 和
[`fd2d_positive_flat_developable_family.py`](../scripts/fd2d_positive_flat_developable_family.py)。
真实 P1 格内平均的意义见 [R140](R140-physical-codazzi-cell-integrals-and-actual-P1-quadrature.md)。

## 4. 目标、Jacobian 和受约束求方向的等价性

设一组旧高角残差为 `r(z)=w sqrt(2/W) v(z)`，其压缩版本为
`r_c(z)=w C v(z)=Q r(z)`。`Q` 仅依赖保存的 `W,K` 和相应行排列，不依赖
未知场或设计参数。由 (5) 和 §3，

\[
 r=Q^Tr_c,\qquad J=Q^T J_c,\qquad J_c=QJ,              \tag{6}
\]

其中 `J=Dr`。所以对任意实际增量 `d`，

\[
 \|r+Jd\|_2^2=\|r_c+J_cd\|_2^2,
 \quad J^TJ=J_c^TJ_c,
 \quad J^Tr=J_c^Tr_c.                                  \tag{7}
\]

将 `Q` 按径向节点、单元以及 `n/m` 方程组成块对角矩阵，式 (6)–(7) 逐块
成立。其他原方程、curvature merit、参数边界及阻尼项保持原样后，二范数
目标和相同约束下的线性方向问题完全相同。准确中央柱消元 `d=Bq` 也可在
压缩前后实施，因为 `QJB=(QJ)B`。

这不意味着压缩系数的最大绝对值等于旧点值的最大绝对值。候选诊断继续
读取完整原角网格的 `full_gauss`、`full_codazzi_cells` 及其最大值；不能
以系数最大值替换这些原有点值诊断。

## 5. 任意非 D2 场的适用边界

对任意点值向量 `r`，`Q^TQ` 是相应 D2 高空间的正交投影。一般只有

\[
 \|r\|_2^2-\|Qr\|_2^2
    =\|(I-Q^TQ)r\|_2^2\ge0.                           \tag{8}
\]

例如 `v_j=cos(xi_j)` 不具半周周期；它与所有偶频率行正交，但其旧归一化
点值范数为 1。若对它直接使用本文的高偶压缩，便会丢掉非零目标。
因此不能仅因某个采样图“看起来对称”而删除其余行。

实现明确限制于 §3 的已声明角公式，并报告其有限对称误差。后续 provider
若改变了角依赖，必须重新满足这一解析前提，或保留相应额外空间。该限制
是等价变换本身的适用范围，没有给原构造添加新的几何验收条件。

## 6. 浮点评价与回构误差

实际计算使用浮点角、三角函数和矩阵乘法，故不宣称输出逐位等距。
代码既保留原完整点值诊断，又报告反射误差、半周误差、行 Gram 误差及
旧点值回构误差。这些有限数值记录与 §2 的实数恒等式分别陈述。

一般地，设实际矩阵为 `Qhat`，有
`||Qhat Qhat^T-I||_2<=delta`，`delta<1`。若保存的两种残差满足
`r=Qhat^T r_c+e_r`、`||e_r||<=epsilon_r`，则

\[
 \big|\|r\|^2-\|r_c\|^2\big|
 \le \delta\|r_c\|^2
 +2\sqrt{1+\delta}\,\|r_c\|\epsilon_r+\epsilon_r^2.      \tag{9}
\]

证明只需展开平方，使用
`||Qhat^T r_c||<=sqrt(1+delta)||r_c||` 和 Cauchy–Schwarz。
若同一方向 `v=Jd=Qhat^T v_c+e_v`，则同样展开给出

\[
\begin{aligned}
 |r^Tv-r_c^Tv_c|\le{}&\delta\|r_c\|\|v_c\|\\
 &+\sqrt{1+\delta}(\epsilon_r\|v_c\|+
                       \epsilon_v\|r_c\|)
 +\epsilon_r\epsilon_v.                               \tag{10}
\end{aligned}
\]

这些式子说明应记录哪些舍入项；当前 §7 的数值是实际浮点评价的误差
观察，没有把普通浮点 Gram 和范数计算冒充有向舍入区间证书。

## 7. 实际单次对照与直接小行装配

新代码为：

- [`fd2d_gc_d2_complements.py`](../scripts/fd2d_gc_d2_complements.py)：
  `high_gauss_merit_d2` 和 `codazzi_complement_d2`；
- [`fd2d_gc_gauss_cell_codazzi_d2.py`](../scripts/fd2d_gc_gauss_cell_codazzi_d2.py)：
  `gauss_cell_codazzi_d2`，与旧 Gauss-cell helper 使用相同主参数和返回键。

每一径向块的 Jacobian 直接乘高 Fourier 投影后放入小行稀疏矩阵。没有
先构造旧的大点值 Jacobian，再以另一个大稀疏矩阵压缩它。Gauss2 的
`retained_residual/J`、完整点值数组和实际求积点定义保持原样；其高行在
每格内按完整偶高 `n` 行、完整奇高 `m` 行排列。根侧的 cell chunk wrapper
可把新 Gauss2 入口作为 `consumer`，两种内存改进作用于不同层次。

以已闭 `joint02-accepted-0020.npz`（SHA256
`2bf2d98aaa6c57752a78aeabf96a4d5541528c998b669b59fc139556203f1a22`）
作唯一实际对照。它有 99 节点、`K=15`、`W=256`。对所有独立节点、尾参数
及物理 bump 参数组成的一个明确混合方向，比较旧点值目标和新直组小行。
未进行新的有限差分组、BVP 或实际 body 积分。

会话 `4558`、完成块 `a5267d` 实际自然返回 0，总计 17.421 秒，峰 RSS
324,784 KiB。完整数据在
[`2026-11-12-fd2d-metric-d2-compression-check-01-report.json`](../notes/2026-11-12-fd2d-metric-d2-compression-check-01-report.json)。

| 补余块 | 旧行数 → 新行数 | 旧非零元 → 新非零元 | 新残差与压缩旧值最大差 | 新 `Jd` 与压缩旧值最大差 |
|---|---:|---:|---:|---:|
| 高 Gauss | 25,088 → 4,802 | 1,363,038 → 261,071 | `7.807e-18` | `2.429e-17` |
| 高梯形 Codazzi | 50,176 → 9,506 | 2,366,441 → 449,207 | `8.674e-18` | `1.943e-16` |
| 高 Gauss2 Codazzi | 50,176 → 9,506 | 2,381,260 → 452,020 | `1.388e-17` | `1.250e-16` |

三个 `0.5||r||^2` 目标差的绝对值均小于 `1.735e-18`，目标方向导数差
小于 `6.072e-18`。旧点值残差由新行回构的最大差小于 `3.192e-15`；
同一 `Jd` 回构最大差小于 `1.259e-14`。未乘 merit 权的实际完整补余样本，
反射和半周对称误差分别不超过约 `1.322e-13` 与 `1.411e-13`；偶、奇
行 Gram 最大条目误差分别约 `9.112e-15` 和 `7.435e-15`。这些量全部
保存在报告中，未被当作真实模态删除阈值。

原 `F`、原三场、网格、计算角数组、全部返回的完整角诊断均逐位不变。
Gauss2 的保留残差及本次保留 `Jd` 也逐位不变。以上是实现等价性的有限
证据，不改变这份历史场未收敛的状态；强幅度闭曲面的连续度量、拼缝和
整体几何仍沿原有消费者推进。
