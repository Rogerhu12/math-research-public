# 实际角域与边界绕数的独立核查

2026-11-12，independent-audit。范围是两份新源的数学与逐行接线，
没有重跑完整网格，也没有将单段域证书称为全流或 PDE 逆。

## 1. 已读来源

完整读取：

- `scripts/fourfold_phase_actual_angle_anchor_domain.py`，SHA256
  `b0d6a4d6e9b1d91ac338a741ce2c9cb2f8bf5957a86906c17206e777208617f8`；
- `scripts/fourfold_phase_angle_boundary_winding.py`，SHA256
  `1857af6dcad966f02995d57f706dfb4e46a2f1282be0150d896ae4407ded2cae`。

同时读取它们调用的 `invariant_enclosures`、
`whole_angle_outer_invariants`、`frame_membership`、`real_anchor` 和
完整 Fourier alias / tail 公式。既有原函数误差入口保持同一准确 affine
对象、真实 common germ 和物理角 $\theta$。

## 2. 静态实际角锚点

旋转柱坐标写 $X=F_r$，
$$
h=-\sin\beta X_1+\cos\beta X_2,\quad
v=-\cos\beta X_1-\sin\beta X_2,
$$
$$
Q=\cos\gamma X_3-\sin\gamma h,\quad
A=\cos\gamma h+\sin\gamma X_3,\quad P=1+\beta_\theta.
$$
使用真实恒等式 $X_\theta=a'T+aT_r-J_{\rm rot}X$ 得
$$
Q_\theta=a\gamma_r-P\sin\gamma v-\gamma_\theta A,
\qquad v_\theta=a\cos\gamma\beta_r-Ph.
$$
所以 $D=P\cos\gamma Q-\gamma_\theta v$ 及代码的完整 $D_\theta$
展开准确。没有对截断位置原函数作谱微分来代替这个真实恒等式。

`static_grid` 用物理频率 $n=4k$，复角偏移因子 $e^{-ny}$，
Native inverse DFT 后乘 $N$；有限 phase 导数各乘 $(in)^j$。
实际原函数的无限尾费用在每个 $X$ 分量加回，随后再作非线性区间运算。
代码要求网格至少容纳 primitive 并单独拒绝有限 phase 的混叠。

一个周期长度是 $\pi/2$，最近实节点距离至多
$g=\pi/(4N)$。连续边界下界采用
$$
\min_j\{\operatorname{Re}D(\theta_j+iy)
       -g|\operatorname{Re}D_\theta(\theta_j+iy)|\}
       -\tfrac12g^2\sup|D_{\theta\theta}|.
$$
其中最后一个 norm 来自完整 strip 的真实粗模数；未将节点最大值
充当导数 norm。准确实性处理另一边界，周期 harmonic minimum
再处理 strip 内部。$D$ 的构造没有除以 $D$，因此没有循环假设其无零。

## 3. 复时间扩展

`invariant_enclosures` 先对每个已保留时间系数支付完整角 Fourier
alias 和 omitted tail，再在较大的时间盘用 Cauchy 支付无限时间尾。
新静态锚点的时间位移费用准确为
$$
\sum_{i=1}^{p-1}\|D_i\|_{\sigma}R^i+
 M_D(R/S)^p/(1-R/S).
$$
常项没有被重复扣费。真正 $-K$ 的正实部门和更大盘的曲率解析性
分别检查；最后的 $f,f_\theta,f_{\theta\theta}$ 商式保留分母各阶费用。
这些是所列实际 germ / 时间段的域结论，没有证明真实特征流留域。

## 4. 真边界到准确多边形的同伦

每个 $z_j$ 是实际 $D$ 球的准确 dyadic 复中点。代码对从
$\theta_j$ 到 $\theta_{j+1}$ 的整段曲线收费
$$
\epsilon_j+\Delta|D_\theta(\theta_j+iy)|
       +\tfrac12M_2\Delta^2,
\quad \epsilon_j\ge|D(\theta_j+iy)-z_j|,
\quad\Delta=\pi/(2N).
$$
再取它与 $|z_{j+1}-z_j|$ 的最大值。如果此半径严格小于 $|z_j|$，
真实曲段和多边形边同处于一个不含零的凸圆盘，逐点直线同伦合法。
相邻端点处同伦相接，故给整条闭曲线同伦，而不只是节点非零。

当每个准确比值 $z_{j+1}/z_j$ 的实部严格为正时，主值对数的虚部
就是这一条不绕零线段的准确幅角增量。求和除以 $2\pi$ 包含多边形
的整数绕数。浮点只提出候选整数，最终使用 Arb 区间严格包含于
候选的 $\pm1/4$ 邻域；非零同伦和整数隔离须同时通过。

实轴上已有同一对象的实际非零门；实函数沿整个周期不变号，故底边
绕数为0。上下边的周期侧边相消，argument principle 因而给上 strip
零点数为顶部正向绕数的负值。四个直接 Fourier 节点只作公式交叉
检查，不代替上述整段同伦门。

**周期范围。** 代码 $\theta_j=\pi j/(2N)$ 走的是物理角的一个
$\pi/2$ 基本周期。若最终报告给顶部绕数 $-4$，对应这个基本周期内
上 strip 四个零点；完整物理 $2\pi$ 周期重复四次，对应十六个。
不能把两个计数口径混用。

## 5. 结论与限制

未发现两份新增源的公式或有限 / 无限误差接线缺口。边界实部为负
本身没有被当作存在复零点的证据；真正零点计数使用完整不含零同伦
和 argument principle。结果仍限于准确参数、所列真实径向 germ 和
报告指定的时间范围，不给其它参数的 strip、全程流或完整 PDE 逆。
