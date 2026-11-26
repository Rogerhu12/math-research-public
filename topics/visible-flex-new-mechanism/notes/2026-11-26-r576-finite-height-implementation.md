# R576 有限高度首轮：准确尾基、turning 设计与实际位置检查

状态：新输入的实现说明，尚未执行；不宣称有限等距闭面或固定 g 精化。全部科学仅在绑定的公开 Actions 执行，原 stdout 不入 Git/Release。

## 1. 本轮为什么换表示

R580 排除了旧圆背景中同一指数包络乘有限末端多项式的非零准确线性入口。本轮用 R571/R583 的真全平端模作为独立列，再直接解 R576 的有限非线性高度方程。径向目标 E 由准确 turning 条件设计，不把变化中的 E 当成固定度量序列。

采用同次 gain 自然终态中 R=.85、L=6、lambda=.5 的 profile 作为新输入的参考。原参考 H=.523503932624032 只用于选根；该旧 profile 的背景曲率上界为11.533378280521717，而其固定度量没有购买旧宏观弦长门。本轮不继承该失败度量的宏观结论。

旧 core onset 为 t^1.1，虽然高度为 C2，但近似 R576 残差的实际平面位置二阶导数可能需要更高高度导数。因此本轮明确换成
$$
W(r)=w_0(r)e^{-6S((r-.30)/.04)}
 +H S((r-.37)/.11)S((.61-r)/.13)
 +\lambda S(t/.1)\frac{t^{1.1}}{(1-t^2)^{.55}},
\quad t=\frac{r-.55}{.85-.55}>0.
$$
最后一项在 t<=0 时为0。S 是原脚本的 C-infinity logistic flat step。这只在 .55<r<.58 改变旧 profile，开尾完全相同，外端竖直渐近完全相同，内部 core onset 已变为 C-infinity。

这是明确新背景，必须重新进行真实 mode2 核心 shooting。程序在 H∈[.02,4] 的33个固定 log 节点读 Ccore/hypot(Acore,Ccore)，选最近旧 H 的换号 bracket，并实际 Brent 求根。旧 H、旧 C/A 残差和旧增益均不冒充新结果。

## 2. 基底的完整数学定义与数值边界

对 j=2,4,6,8，尾上基底是 R583 的准确无限 DtN 极限，归一 y(alpha17)=1。程序用准确索引 rho_{M+1}=0 的有限 M=25 数值评价，并保逐 cell logarithmic scales；R571 原 helper SHA 已绑定。

本轮需要整条连续径向基函数及任意新节点的 jets，旧收据只保存外口13jets与少量峰，没有保存内端斜率或大表。因此程序重新生成所需 dense seed profiles 是这份新非线性基的输入成本，不重报旧 seed 结论。最终 stdout 保存新的 alpha17、z_alpha17 等小型来源状态，后继可复用，不要求再次为同一端值付款。

确切内区 r_c<r<r(alpha17) 仍由无限 DtN 定义，并没有冻结成径向开环。当前数值 evaluator 只接受 r>=r(alpha17)；被省略的无限尾不记作已认证。有限 DtN 截断界与浮点 ODE 误差始终分开。

每个尾模沿新固定参考背景的真实二维系统延伸到核心。程序报告原 Acore,Ccore。随后用核心两条正则基本解 (A,C)=(1,0),(0,1)，以 .55<r<.65 的 C-infinity step 将 raw/Acore 接到 admissible 核心基本解 (1,0)。此校正的值、一阶和二阶导数全部放进高度；不是在外端把 Ccore 数值强行填零后继续使用旧中段方程。源文件还报告独立方向的转接误差观察。

数学上这等价于从 raw/Acore 减去 (Ccore/Acore) chi G，其中 G 的核心数据为 (0,1)。实现用完整 jet 的 raw-to-admissible blend，避免在极近核心处相消并避免数值分段跳。每条校正后高度列 S_j 都有
$$
S_j(R)=0,\qquad \lim_{r\to R}W S_j'=-\frac{j^2-1}{R}.
$$
除 j2 共振极近的情况外，校正通常不是原线性方程的齐次解；它的残差确实进入 R576 非线性方程。

## 3. 52 个有限控制与无限角谱

固定六个内部样条结点 .235,.27,.34,.48,.64,.78，五次 B 样条共12列。非径向预高度为
$$
v(r,\theta)=\epsilon S_2(r)\cos2\theta
 +\epsilon\sum_{j=4,6,8}c_jS_j(r)\cos j\theta
 +\epsilon\,B(r)\sum_{j=2,4,6,8}\sum_{k=1}^{12}d_{jk}B_k(r)\cos j\theta.
$$
正自由包络为
$$
B(r)=C^{-1}\left\{
 \sum_{j=2,4,6,8}(S_j(r)/m_j)^2
 +e^{-10^{-4}/(r-r_c)^4}(R-r)^{3.1}
 \right\}.
$$
m_j 和 C 由源中固定的第一次节点集计算并输出，属于这份静态表示的已识别归一量。包络对每个内部尾点严格正；在核心 W B' 趋零，因此不暗改核心通量。它使用 S_j 的二 jets，不需要原 t^1.1 onset 不存在的高阶导数。

实际高度采用
$$
Z=h+f,\qquad
f=.15\tanh(v/.15)-\langle .15\tanh(v/.15)\rangle.
$$
因此即使 v 只有四个显式角模，实际 f 一般有无限角谱；没有将固定 Fourier 高度当作非圆准确终点。核心 leading flux 不被 tanh 的高阶项改变：
$$
P_c(R,\theta)=-\frac{\epsilon}{R}
 \left(3\cos2\theta+\sum_{j=4,6,8}(j^2-1)c_j\cos j\theta\right).
$$
H、三个高模系数和48个 bulk 系数共52个未知数。epsilon 是静态非轴对称幅度；本轮固定顺序为
1e-5,3e-5,1e-4,3e-4,.001,.003,.01,.03,.1,.2。
高模也没有被假定自动闭合；全部高度行进入同一有限非线性求解。

## 4. R576 残差与隐式 Jacobian

每个 r、theta 上计算 b,N，并保持它们的正性。使用差量 e=E-W²，令
$$
V-W^2=-2Wf_r+f_r^2+(-W+f_r)^2f_\theta^2/b^2.
$$
在每一圈以相对于最大差量的 lambda=e-max(V-W²) 求 turning 根，避免大背景 W² 相减。56次括分加 Newton 给根。参数复步时，实 reference 只是固定的数值原点，后面的复数 Newton 对整个隐式根求导。

E' 与 Darboux 残差严格用 R576 的二 jets 公式。随后用零均值角原函数重构 psi,Y 及
$$
W_*=\Pi[b(\Pi\mathcal R)JT].
$$
优化残差是 W_*/sqrt(E)，不是只读取 Darboux 系数或某个低阶均值。所有原函数使用实矩阵，防止 FFT roundoff 的虚部污染 1e-25 复步导数。首个科学 run 自带一次真正的 central-direction 对照；这是该新隐式 Jacobian 的必要验证，不另设本地研究计算。

Gauss-Newton/LM 使用列尺度、阻尼和保定义域回溯；N,b,u 和 identity 预测的外向速度失去正性时拒绝该试步；后者仅为试步守护，直接位置差分的外向速度另在细网要求严格正。没有将这些守护行的失败掩成新的几何候选。

## 5. 必须从实际重构位置重新读 metric 与曲率

连续 R576 恒等式中的角积分，在有限 theta 节点上只是数值评价。特别，离散 turning 根的径向导数未必与连续分部积分式在粗网完全相同；不能把 P+W* 本身当成已经验证的位置导数。

本轮细网另作实际重构检查：直接对 Y(r±h,theta) 求径向一、二阶差分，对 Y 的角插值求一、二阶导数，重新组合完整 Xr,Xtheta,Xrr,Xrtheta,Xthetatheta。由此重算 E/F/G 全三行和主曲率。径向步长 h 与 h/2 都报告，包含 identity-based Yr 与直接差分 Yr 的差。这是实际位置的数值观察，仍不是连续或区间曲率证书。

同 q 的 r/theta 加密若漏峰，程序在预算内把细网提升为实际求解网；最大主动密度2，再在密度4验证。只要细网或直接重构 metric 未到声明的容差，便明确记为未解并停止本份幅度表，不把粗网成功拿去继续扩大幅度。直接差分观察阈值是8倍 metric 目标，明确容纳其数值误差；它不会被记成一个更严格的连续精度。

报告球、条带、高度、真实 metric、曲率只覆盖声明节点。当前没有把曲率或远点对 reach 写成未执行的全域硬证明。若实际非线性入口成功，才接 R579 的真实宏观核心通量目标及固定 g 精化。

## 6. 执行与身份

唯一新科学脚本是 scripts/r576_finite_height_turning_20261126.py；绑定两个原依赖和通用公开 runner。workflow 一 job，45分钟 wall timeout，科学声明预算2400秒。所有计算含 seed、shooting、Jacobian、拒绝试步、加密和真实重构均计数。

本轮不会提交 raw 日志、大数组、证书、artifacts 或 Release。stdout 的 small state 可供后继精确识别；最终收据只存 run/job/source/request/log hash 和必要小标量。

精确尾的浮点误差、全部无限角模、固定 g 精化、连续 reach 和宏观握持门仍未完成。本包是进入实际有限非线性边值问题的新输入。
