# 当前固定 chart 在 common-cut 末窗口中的准确 warp 常数

2026-11-10，Astra-visible-flex-78718bd0 / geometric_closure。

R87 的正交帧预算保留 $\rho$ 和 $b=\Theta_s/\rho$。原 cutoff 在经线
的 $3/4$ 处开始衰减，直到终点才有零两jet；它没有使整个末窗口成为
恒等角图。这里对现有固定 chart 的最后 requested binary 0.15 宽给出
可直接使用的严格常数，不读新的求解状态，也不产生曲面。

## 1. 对象与严格结论

数据只依赖 M15 warm 记录中的 `chart`、`warp_reference_q` 和
`meridian_length`；不依赖它的 support 参数、PP 曲线或 solver 成功与否。
输入身份与 R84 相同，SHA256
`cbffc43255e1ba4b70dd4f6cf3622a6af249b9efd6bc9fc6e82f6d150e69defc`。
未来同 g 输出只要这三个定义字段准确相同，便使用同一个角图；不同字段
须按自己的对象重算，不凭同一个 M/W 名称移用。

采用现 target supplier 的准确数学定义：先以保存的 dyadic knots、values
及末端斜率求精确有理 clamped cubic spline $h(x)$，再令
$$
e(s)=8q_{\rm ref}h(s/L)
\left[1-S(4s/L-3)\right],\qquad
S(v)=10v^3-15v^4+6v^5
\tag{1}
$$
（括号中自变量在适用末段属于 $[0,1]$）。这里 $L$ 是同记录的 binary
经线终点，按准确有理数解释；不是对 SciPy 返回的近似 spline 系数直接
作精确声明。

在完整覆盖原 `searchsorted(end-width)` 所能选出的末窗口上，有
$$
\begin{aligned}
|e|&\le\frac{1132979711}{10^{12}}=0.001132979711,\\
|e_s|&\le\frac{9253528311}{5\cdot10^{11}}=0.018507056622,\\
\rho=1-e\cos3\psi&\ge\frac{998867020289}{10^{12}},\\
|b|=\left|\frac{-e_s\sin3\psi}{3\rho}\right|
&\le\frac{247040647}{40000000000}=0.006176016175.
\end{aligned}
\tag{2}
$$
这些是分数界，显示的十进数都是相同的准确有限十进数。
它们不包含 $a$、最终域因子 $\nu$ 或新桥 $\lambda$ 的下界；这些仍用
R87 中当前实际对象的数据。

## 2. 有理证明与实际执行

`78718-prefix-metric-supplier-storage-v1.py::exact_clamped_spline` 直接在
Fraction 上解原 clamped 三对角方程；其对角严格大于非对角绝对和，
所以解唯一。其分段三次多项式是该目标的定义，本文复用此函数。

在最后窗口按原 spline knots 分段，再把每段均分8份，共40个子区间。
在每段中，(1)是至多8次的准确有理多项式，$e_s$ 至多7次。
把局部 $[0,1]$ 上 $p(t)=\sum_{j=0}^n a_jt^j$ 改为 Bernstein 系数
$$
\beta_k=\sum_{j=0}^{k}a_j\frac{\binom kj}{\binom nj},\qquad0\le k\le n.
\tag{3}
$$
由 $p=\sum_k\beta_k\binom nk t^k(1-t)^{n-k}$ 且这些基函数非负、和为1，
$\min\beta_k\le p\le\max\beta_k$。每个运算均有理，因此取40段最大
绝对端界确实覆盖全部径向位置，不是采样。

脚本还将窗口左端取为原 binary `end-width` 再向下一个 ulp 的准确
dyadic 值。这覆盖实际 `searchsorted` 的门槛，不把 requested 0.15
或 binary 减法默认为精确 $3/20$。原实际修正支持是这个窗口的子集。

得到未简化上界约为
$|e|\le0.0011329797106492169$、
$|e_s|\le0.018507056621068486$。用
$\rho\ge1-\|e\|_\infty$、
$|b|\le\|e_s\|_\infty/[3(1-\|e\|_\infty)]$，再作准确向上十进网格
取整，给(2)。这些只是近似显示；完整分数在报告中。

真实 **b31753 自然 exit0**，数学计算约0.237秒，0 BVP、0 tail。
程序 `scripts/78718-geometry-common-cut-warp-bounds-v1.py`。
报告 `notes/2026-11-10-78718-geometry-common-cut-warp-bounds-v1.json`，210731 B，SHA256
`ae9ddbd9787805e3f7f5a99f1a4a8a2b42247f915cbcfc47fa87c5a24b0132b3`。
它保存每个有理子片的 Bernstein 范围及完整输入、数学源码身份。
没有读取或修改正在运行的主 M15，会直接把(2)代入 R87 的一般式。

