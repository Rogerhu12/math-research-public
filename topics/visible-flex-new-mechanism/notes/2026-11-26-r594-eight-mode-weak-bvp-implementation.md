# R594 八模完整弱高度边值输入：实施身份

会话 Astra-new-mechanism-0105020f-20261126；公开 Actions 单 job。对应脚本
[r594_eight_mode_weak_height_bvp_20261126.py](../scripts/r594_eight_mode_weak_height_bvp_20261126.py)，
请求 [request-r594-eight-mode-weak-bvp-20261126.json](../computations/request-r594-eight-mode-weak-bvp-20261126.json)。

## 1. 为什么这次是新输入

上一 [body-forced $j=4$ 自然终态](2026-11-26-r576-body-forced-j4-natural-final.md) 给实际完整 $D$ 的 $j=10$ 峰
$6.629572284315579\cdot10^{-6}$，大于 $j=4$ 的
$1.2390611789482226\cdot10^{-6}$。
单个轴对称主部的强迫方向未消掉完整多模余项。

本次把 [R594](../results/R594-exact-nonlinear-radial-acceleration-and-galerkin-leakage.md)
的准确有限弱边值方程直接作为求解对象，对 $m=2,4,\ldots,16$ 求
$$
\left\langle\cos(m\theta)\frac{D}{M}\right\rangle
=\left\langle\cos(m\theta)\frac{A_t}{M}\right\rangle=0.
$$
$e'M/2$ 只因正频率测试的均值为零而消去；当前完整非线性 $E$、全部高度角谱和原 $D$ 都仍在。它不是在轴对称背景上再取一轮线性响应，也没有将实际 $f$ 投影到八模。径向函数暂由明确样条类离散，有限配置仍不是连续弱方程已经有根。

## 2. 整个已付场和真实数值来源

完整采用 run 45813421528 / job 139886872647 的实际 265 参数及全部 67 结点：
$q$ 原 JSON SHA256 为
`242afcd609b5a9f3ff9480689d296dfdc3171c51f46d1c35f6b1875c9959cab6`，
结点原 JSON SHA256 为
`9e3ce07c7d55f46135c31b86f45bddec557495c2f6648ef4b723b53637fb3e15`。
这些下一输入参数逐字绑定在源中，原 stdout/可重算场表不进文件。

旧 $\tanh$ 前四模、264 个坐标和所有局部径向项保留；旧 $\tanh$ 后强迫 $j=4$ 项也保留。旧强迫的冻结背景仍为
$H_{\rm force}=0.5188895813736972$，尺度仍为
$16533.1541790287$。不能改成最新末态
$H=0.5188907586810884$ 来重定义它。
必要的旧 dense 外传、core 流和强迫场重建全部计费；旧四个内 Riccati 和旧 $H$ shooting 不重跑。

新未知向量 496 维，初值只有 $H$ 为实际旧值，其余 495 个新增高度系数严格为零。新场是原实际场的仿射添加，原 265 参数本身冻结为来源常数。相同初始高度不依赖另做拟合。 原已付64角baseline不另作复跑门；保场由完整参数/固定归一和零新增量的定义保证，首次实际评价直接在新128角/八模核心问题上输出完整checkpoint。

## 3. 真内端线与准确核心自由阶

[R596](../results/R596-same-mild-tail-flat-kernels-through-sixteen.md) 已把同一固定尾的真实全平模证明扩到 $j\le16$。
新 $10,12,14,16$ 各自执行本模 $p,\varepsilon$ 的新 DtN 反推和 dense 外传，$M=25$ 的准确有限身份是
$\rho_{26}=0$、$y(\alpha_{26})=0$。
每模记录自己的 $\alpha_{17}$、平衡斜率、$\rho_{18}$、13 个外口 jets、对数归一和核心原 trace，分别计内/外 RHS。旧四模只从原已付口重建必要外场。

各新增齐次场采用各自真实内核和 core $A=1,C=0$ 段；中间沿原
$[0.55,0.65]$ 作完整二 jets 显式混合。原 forward/core 差和该混合都进入实际高度，不能将修正后的场称为完整区间上的准确齐次解。

新增径向函数为
$$
\Delta f=\epsilon\sum_{m=2,4,\ldots,16}
\left(a_m C_m^{\rm adm}
+\frac{\chi(r)(.85-r)^{\alpha+2}}{(.85-.30)^{\alpha+2}}B_m(r)\right)
\cos(m\theta).
$$
这里 $\alpha=.55$，$\chi=0$ 于 $r\le.23$、$\chi=1$ 于 $r\ge.24$，
使用原 $C^\infty$ flat step。它只限制新增 bulk；原场、每模真实端线没有被冻结或切成零。$B_m$ 在原 67 结点的 61 个五次 B-splines 中表示。固定 $a_2=0$ 保持原主核心幅度，另外 7 个核心幅度自由；另有 $8\times61$ 个 bulk 系数和一个静态 $H$。

[R597](../results/R597-nonlinear-core-trace-and-realizable-free-order.md)
表明若 $P_0=\lim Wf_r$，$P_1=\lim(Wf_r)'$，则
$$
(A_t)_R=-RP_1+\frac{\alpha}{1+\alpha}(e_R+2P_0)(P_0)_{\theta\theta}
-(P_0)_\theta^2,
\quad
\langle(e_R+2P_0)^{-1/2}\rangle=1.
$$
新的 $\delta^{\alpha+2}$ bulk 不改 $P_0$，却给
$P_1=k(\alpha+2)b(R)$；旧 $\delta^{2+2\alpha}$ 自由项没有这个端值响应。
脚本在真实核心使用此有限弱行，并用 R597 的
$$
e'_R=-2\frac{
\langle P_1/u_R^3\rangle+
\langle(P_0)_{\theta\theta}/u_R\rangle/[R(1+\alpha)]
}{\langle u_R^{-3}\rangle}
$$
报告完整 $D_R$、其均值和角谱。没有用 $R-\varepsilon$ 代替核心行。
原 forced 项的线性核心贡献 $-\epsilon^2q_{\rm force}S_4(R)/{\rm scale}$
明确包含；旧 $\tanh$ 和旧 bulk 对 $P_0,P_1$ 的余项按 R597 消失。

## 4. 非线性残差和解析 Jacobian

主体仍由已绑定的原 R576 几何实现求隐式 turning 根并重构实际 $Y$。
在每个候选上先有实际 $N>0,u>0$ 和原恒等式外向正域，以及采样高度为正。
本次不按 $\mathfrak a=E f_{\theta\theta}+rp$ 点除。
每个保留状态明确报告 $\mathfrak a$ 的正负范围、非负节点数、实际
$8\times8$ 弱质量矩阵的最差半径、全 eigenvalues、相对最小奇异值和有限秩。
失号不被隐藏成“已通过负性”，也不直接推论全机制不存在。

解析 Jacobian 对当前离解场使用
$$
\delta\langle\phi A_t/M\rangle
=\left\langle\phi\left(\frac{\delta A_t}{M}
-\frac{A_t\,\delta M}{M^2}\right)\right\rangle.
$$
因此非零残差时的分母变化项没有省掉。$e$ 的变化来自完整隐式 turning 方程；
$\delta W,\delta W'$、所有二 jets 以及 $W^2+e$ 的交叉项均包含。
由于这里测试的是 $D/M$ 而非 $R$，$e'$ 作为角常数准确消去；
这不是将 R594 中 $\delta R$ 的 $\delta\omega D$ 项任意扔掉。

核心 Jacobian 包括同一隐式 $e_R$ 的导数
$-2\langle\delta P_0/u_R^3\rangle/\langle u_R^{-3}\rangle$，
$P_0(P_0)_{\theta\theta}$、$(P_0)_\theta^2$ 以及独立的 $P_1$ bulk 响应。
固定的旧强迫字段不对新参数伪求导；$H$ 的支持不触核心，故其核心列为零。
16 列一组计算解析导数，未以巨大临时全表换空间。

同一个正式 run 只在第一个实际状态执行一次新的解析 Jacobian 方向观察，与完整 complex-step 弱残差比较；没有重跑旧接口检查。它用于发现新实现链式错误，不能认证连续线性逆。

## 5. 求解、接受和保留身份

固定行单位为径向梯形权平方根乘 $1/m^2$；核心八行权为 $0.1/m^2$。
它们在一次网格和所有试探中不变，不因候选变动改变 merit 的含义。
行单位不是删方程，全部弱行和未缩放物理缺陷同时报告。

全部列作有下限的范数缩放，对缩放 Jacobian 直接 SVD；所有奇异方向保留，
用阻尼求步，不形成正规方程。原高度 jets 的函数尺度限制仍作用于完整候选。
只有真实完整弱 merit 的下降超过 $32\epsilon_{\rm mach}\cdot{\rm merit}$（及
$10^{-30}$ 绝对下限）、预测下降为正且比值 $>.01$ 才接受。
完整原度量误差在每个保留状态报告；弱 merit 下降不被改称 $\eta_\infty$ 改善。

每个有效初点和每次真正接受后立即输出完整 496 维状态、$H$、物理峰、实际块谱和核心行。
时钟或数值失败时，FINAL 从最后已记录的真实 checkpoint 恢复 $q$ 和实际幅度，
并与“最后进入的幅度”分开；最后提议方向和未返回的外层变量不冒充实际末态。
若程序甚至未产生新有效 checkpoint，来源 265q 身份仍保留。

## 6. 唯一正式计算范围

一个公开 job，科学时钟 2400 s、job 45 min，最多 60 次每级 Newton/SVD 更新。
活动角节点 128；径向为旧相位格并对原每个 spline span 作 6 等分。
同一末 $q$ 用双径向密度和 256 角节点读全部原残差，
并对实际平面位置用原步长/半步长差分读曲率和度量；
高度分量仍用该定义的解析 jets。
主体报告 $D$ 的全部偶模 0 至 40，核心报告 0 至 34。
这些有限角谱读数不等于真正连续 Fourier 尾界。

幅度表与此前相同，仅在同一 $q$ 的 fine 和两份 direct
$\eta\le2\cdot10^{-9}$，且实际高度和直接外向比为正时进入下一级。
该门仍不是 reach/同度量族完成证书。

## 7. 明确尚未支付的对象

本包真实端线是本模齐次 flat germ，尚未求出非线性内尾 Dirichlet-to-Neumann 图。
新增 bulk 下方的全部原非线性残差仍在观察中；R588 的旧四模常数不会自动认证新增四模。
有限 DtN 截断与浮点 ODE 误差分开。真实连续角谱尾、径向离散到连续的误差、全局 reach、
最终固定同一 $g$ 的有限族和宏观三个比例均未授予。

当前所完成的是一个有完整端口身份、正确核心响应阶、实际非线性弱方程、
完整解析链式和可恢复状态的正式新计算输入。结果仍须由它的自然终态原 stdout 决定；
不会据此提前宣布有限解存在。

