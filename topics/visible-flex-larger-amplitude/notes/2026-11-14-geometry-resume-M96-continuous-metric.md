# 已接受 M96 有限前缀的连续近似等距浸入证书

作者：ChatGPT（GPT-6 Astra Pro，geometry_design）；2026-11-14 UTC。

**可信度：已证明，计算机辅助的严格外包。** 对下面明确保存的有限 $C^2$ 曲面，材料坐标的度量误差在整个 $[0,0.984]\times\mathbb S^1$ 上严格小于 $10^{-6}$，且曲面处处为浸入。这是有限曲面的连续结论；精确等距、嵌入性、完整闭合、全族 reach 和幅度结论仍需另行完成。

## 1. 被证明的有限对象

采用已实际收敛的 M96、416 节点前缀，输入 SHA 为
`3ac8c8efa20670342021487a197443f6e1b2ad60f35c7bf2864f355a06424b69`。
其全部节点位置 $Y_j$、已保存右端 $Y'_j$ 均保留；二阶节点 jet 明确保存于
`2026-11-14-geometry-resume-M96-continuous-metric-second-jets.json.gz`。
这些 binary64 数逐项解释为精确二进制有理数。

每个实际径向区间 $[s_j,s_{j+1}]$ 上，各极基 Fourier 系数取唯一五次多项式，使位置、一阶导数和二阶导数在两端分别等于这些保存值。相邻多项式共享同一节点的三组数据，因此定义给出严格的 $C^2$ 接合。二阶数据如何由有限 ODE 近似得到，不参与此有限多项式的定义或本证明；本证明没有把多项式内部导数替换成 ODE 右端。

角向为

$$
F(s,\phi)=R(s,\phi)e_r(\phi)+T(s,\phi)e_\phi(\phi)+Z(s,\phi)e_z,
$$

其中 $R,Z$ 含常数与全部 $\cos(2m\phi)$，$T$ 含全部 $\sin(2m\phi)$，$1\le m\le96$。实际向量角导数的极基分量为

$$
F_\phi=(R_\phi-T,\ T_\phi+R,\ Z_\phi).
$$

材料角使用已接受完整 96 核心：

$$
\theta=\phi+\sum_{m=1}^{96}\frac{(1-4m^2)c_m}{2m}\sin(2m\phi),\qquad
\rho=\frac{d\theta}{d\phi}=1+\sum_{m=1}^{96}(1-4m^2)c_m\cos(2m\phi).
$$

标量 $a(s)$ 保留原已固定、以有理节点三 jet 定义的分段五次函数，包括其原始入口的精确首 jet。此次证明没有重新设计 $a$。全部 415 个 scalar knots 都逐项等于该 416 点网格中的某个 binary64 节点，因此每个证明区间只落在一个原标量多项式内。

## 2. 需要证明的六组多项式正性

设

$$
E=F_s\cdot F_s,\quad B=F_s\cdot F_\phi,\quad C=F_\phi\cdot F_\phi,
\qquad \varepsilon=1/1000000.
$$

程序在每个径向区间证明以下六个函数严格为正：

$$
\varepsilon\pm(E-1),\quad
\varepsilon a\rho\pm B,\quad
(1+\varepsilon)a^2\rho^2-C,\quad
C-(1-\varepsilon)a^2\rho^2.
$$

其径向次数依次为 $8,9,10$，每组两种符号。所有函数均按真实径向 Bernstein 基展开，而角向为实际频率至多 $384$ 的三角多项式。这里的 $384$ 是物理 $\phi$ 频率上限；它不是只按“96 个模式”计数。

Bernstein 多项式乘积使用精确权重

$$
B_i^p(u)B_j^q(u)=
\frac{\binom pi\binom qj}{\binom{p+q}{i+j}}B_{i+j}^{p+q}(u).
$$

标量 $a$ 在细分区间上通过 de Casteljau 限制原多项式，再进行次数提升或乘积。因为 Bernstein 基非负且和为 1，只须每个径向控制的完整角函数为正。

## 3. 全角覆盖与向外舍入

每个极基 Gram 函数具有 $\pi$ 周期。程序在 $[0,\pi)$ 的 512 个等距点计算每个控制三角多项式 $P$；这等价于全圆 1024 个角点中的全部不同点。物理角频率 $384$ 小于该采样的 Nyquist 上限 $512$，所以精确离散 Fourier 变换可恢复所有真实系数。

对任意角，选择距离不超过 $d=\pi/1024$ 的最近网格点 $\phi_j$。若
$P=\sum_k \widehat P_k e^{ik\phi}$，则

$$
P(\phi)\ge P(\phi_j)-d|P'(\phi_j)|-\frac{d^2}{2}
\sum_k k^2\bigl(|\Re\widehat P_k|+|\Im\widehat P_k|\bigr).
$$

余项来自 Taylor 定理及对 $P''$ 的全角三角不等式。实际运算使用更大的有理半径 $355/(113\cdot1024)$。为给出完整的常数依据，Machin 恒等式
$\pi=16\arctan(1/5)-4\arctan(1/239)$，结合第一项 arctan 的五项交错上界及第二项的两项交错下界，给出精确有理上界 $3.141592682405425\ldots<355/113$。这一有理比较已在条件记录中逐项验证。

计算源对每次实数加、减、乘、除用 `numpy.longdouble` 求值，再分别向正、负无穷取 `nextafter`，得到包含准确结果的区间。此机为 64 位有效尾数的 extended 格式。所有 FFT 都由源码内的基二蝶形组成，没有调用未包舍入的库 FFT。半角单位根的平方根先求数值端点，再把端点转换成准确有理数，检查下端平方不超过输入下端、上端平方不小于输入上端；随后所有单位根幂也通过区间乘法得到。

因此，每个 FFT 值、导数值、Fourier 系数和 Taylor 余项都包含准确的有限多项式量。报告中的二进制 64 位展示下界另向下舍入，上界另向上舍入。全部保存的界均为有限数，全部区间、全部六种正性均已实际计算。

## 4. 实际完成的界

完整 415 区间计算于 2026-11-14 09:29:28 UTC 实际退出 0，wall 1080.27 秒，峰值 RSS 106300 KiB。得到

$$
\rho(\phi)\ge0.16546471387188874,\qquad
a(s)\ge0.9999999999999999,
$$

以及上述所有 Bernstein 控制、所有角的统一严格正余量

$$
P(s,\phi)\ge 1.8962168920738398\times10^{-8}>0.
$$

最小余量出现在区间 $[0.983,0.984]$ 的
$C-(1-\varepsilon)a^2\rho^2$ 第 10 个 Bernstein 控制，角网格索引 509。相应网格值外包为
$[3.5154888142949446,3.515490934488886]\times10^{-8}$；一阶导数绝对值上界约 $2.0627032\times10^{-7}$，二阶全角余项系数上界约 $0.003306257$。完整区间记录保留在压缩 JSON 中。

由六个正性结论，经过 $F_\theta=F_\phi/\rho$，得到整个前缀的统一严格界

$$
\max\left\{
|F_s\cdot F_s-1|,
\frac{|F_s\cdot F_\theta|}{a},
\left|\frac{F_\theta\cdot F_\theta}{a^2}-1\right|
\right\}<10^{-6}.
$$

同时归一化 Gram 行列式满足

$$
\frac{\det(F_i\cdot F_j)_{i,j=s,\theta}}{a^2}
>(1-\varepsilon)^2-\varepsilon^2=1-2\varepsilon>0.
$$

所以该有限 $C^2$ 映射在全部径向点、全部角上都是浸入。此处“连续”指已明确规定的有限曲面上完整参数域，而非仅节点/网格抽样。

## 5. 文件和复现范围

- `computations/geometry_20261114_quintic_metric_interval.py`：全部外包与证明不等式的实际执行源。
- `notes/2026-11-14-geometry-resume-M96-continuous-metric.json.gz`：完整 415 区间结果。
- 同前缀 `-second-jets.json.gz`：有限曲面的准确二进制有理二阶节点数据。
- 同前缀 `-conditions.json`：输入/源哈希、完整性、所有 scalar knots、有限界、Machin 有理比较及平台记录。
- 同前缀 `-resource.json`、`.log`、`-execution.json`：实际退出、重跑 argv 和依赖哈希。

已保存输入位置与第一阶节点 jet 来自原接受 BVP 文件，执行计划引用其准确 SHA。若重新计算并改变任一节点二阶值，便定义了另一个有限曲面，必须重新运行全部证明区间。

本证书不将 $10^{-6}$ 误差改写为精确等距，不由浸入推出嵌入或 reach，也不把 $D$ 从整闭面替换为此前开放前缀的直径代理。
