# 独立审查：固定角坐标与线性 DN 共轭

2026-11-09，Astra-visible-flex-950f9f73 / independent_audit。
审查者未参与角坐标选择、prefix 求解或 tail 优化。

**结论：解析坐标公式和非恒定 DN 共轭公式 PASS；完整接口尚未认证。**
审查对象为 `2026-11-09-950f-prefix-fixed-angle-chart.md` 的解析部分及
`scripts/950f-prefix-warped-bvp.py` 中的相应实现。当前计算仍是有限
prefix 与线性端口诊断，不能称为完整非线性尾匹配。

## 坐标与 Frenet 速度

固定 $e=8q_*<1$，置
$$\theta=\psi-\frac e3\sin3\psi,\qquad
\rho=\theta_\psi=1-e\cos3\psi>0.$$
这是固定材料圆坐标的微分同胚。度量拉回为
$ds^2+a(s)^2\rho(\psi)^2d\psi^2$，同一几何度量没有改变。

写 $V=\alpha N+\beta B$，由 $F_s\perp F_\psi$ 与 $|F_s|=1$
得到 $\alpha^2+\beta^2=1$；由 Frenet 公式有
$$\partial_s\log|F_\psi|=-\alpha\kappa.$$
所需长度律为 $\partial_s\log|F_\psi|=a'/a$，故
$\alpha=-a'/(a\kappa)$，选择同一正分支
$\beta=\sqrt{1-\alpha^2}$ 正确。此论证要求实际坐标曲线为正则、
$\kappa>0$ 且分支余量正；代码的域检查保留了这些条件。

切回材料角的链式法则
$$F_\theta=F_\psi/\rho,\qquad
F_{\theta\theta}=F_{\psi\psi}/\rho^2-F_\psi\rho'/\rho^3$$
也正确。对背景圆项直接取导、仅对其差值作谱表示，避免了把固定
背景的投影误差误认为解的误差。

## 独立的 Bessel 核对

记 $D_k$ 为物理材料角的 $3k$ 模式线性 DN。对 $j,k\ge1$，候选的
输入转换矩阵为
$$C_{kj}=\frac1\pi\int_0^{2\pi}
 \cos(3k\theta(\psi))\cos(3j\psi)\rho(\psi)\,d\psi.$$
利用 $d_\psi\sin(3k\theta)=3k\rho\cos(3k\theta)$ 分部积分，
再将正弦乘积拆开，直接得到
$$C_{kj}=\frac jk\{J_{k-j}(ke)-J_{k+j}(ke)\}.$$
输出转换矩阵及输出均值分别为
$$B_{ik}=J_{k-i}(ke)+J_{k+i}(ke),\qquad
\overline{\cos(3k\theta)}^{\,\psi}=J_k(ke).$$
因此有限模式的非恒定 DN 矩阵确实为 $B\operatorname{diag}(D)C$，
与候选公式一致。$\theta$ 均值的输入行是
$(-e/2,0,\ldots,0)$，与常数模式的 DN 为零相容。

独立程序 `scripts/950f-audit-angle-dn.py` 不导入 prefix 代码，用
上述 Bessel 公式与独立的 8192 点积分交叉核对。在 weighted K64
物理端口、$M=8,e=.64$ 时，DN 矩阵最大差为 $1.57\cdot10^{-13}$
以下，输出均值行差为 $2.74\cdot10^{-14}$ 以下。报告为
`2026-11-09-950f-audit-angle-dn.json`，保存了物理端口文件哈希。
这些是浮点交叉检查，不是区间误差证书。

## 必须另付的线性均值

虽然物理常数高度的 DN 为零，非恒定物理模式拉回到 $\psi$ 后
一般有非零均值。因此线性 DN 输出的 $\psi$ 均值为
$$\sum_{j=1}^M\left(\sum_{k=1}^K
 D_kC_{kj}J_k(ke)\right)z_j.$$
在上述 K64/M8 数据上，括号内的八个系数约为
$$4.770704,\ 4.820962,\ 2.585914,\ 1.190421,
\ .500665,\ .198166,\ .075169,\ .027516.$$
这是线性阶段已有的效应，不能只归入“非线性 mean 修正”。
原 `terminal` 函数匹配了 $M$ 个非恒定系数；另行积分实际
$\psi$ 均值高度，并不单独证明它在 cut 的斜率与上式匹配。
需要输出该差值或给出强制相等的独立证明。此问题已告知实现者，
不影响纯坐标公式的正确性。

## 离散 FFT 与全角误差的区别

真正的傅里叶系数绝对和上界确实控制全角上确界。但新表示含
解析非多项式的背景 $e^{i\theta(\psi)}$ 及 $1/\rho$，误差不再是
已知有限次数的三角多项式。代码在有限角网格上求得的 FFT l1
应标为离散诊断；要把它升级成全角上界，需要尾项控制，或在
数值允许的层级中至少给出同一几何的角网格加密证据。物理 DN
截断 $K$ 也须单独加密，不能与 prefix 的 $M$ 混为一项。

本审查不证明大振幅 prefix 的收敛、非线性接口、Cartesian 二阶
接缝、闭合或 reach。
