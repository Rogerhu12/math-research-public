# n4：全 19 控制、自由 c8 与材料角的原积分核心读取接口

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

## 接口范围与实际来源

本条完成原生 n4 核心的来源绑定和代数接口，**不新增 BVP、尾求解或连续误差证明**。
来源为 `n4_work/raw-lam002-primaryb016-m20-v2.json.gz`，SHA-256
`c2a313809017c27872593db0edda0d2c5c230b273f08383dbae097f473f23677`。
该完整 $M=20$ 前缀已有原有限接受，但其边界来源仍是 linear DN；
它不是后续失败实际尾的成功替代品，也不是精确圆弧端点。

读取器只从 `parameters`、`central_correction_scales`、`gauge_amplitude`、
`plateau_settings` 和明确的 J16 字段定义核，不从 `core_summary` 反推参数。
本次所有 19 个控制均保留，包含自由的首项 c8：

$$
q_{\rm gauge}=.0125,\qquad
q_{\rm actual}=\operatorname{float}
\bigl(q_{\rm gauge}\operatorname{numpy.exp}(p_0)\bigr)
=.012488347919833637,
$$

$$
c_j=\operatorname{float}(p_{j-1}\,\mathrm{scale}_{j-2}),\quad j=2,\ldots,20,
\qquad c_2=-6.12148007708931\times10^{-8}.
$$

这里乘法的准确数组约定是 `parameters[1:] * central_correction_scales`；
每个实际 binary64 控制量同时保存十六进制与精确有理表示。
这个绑定固定原运行所使用的数，不宣称浮点指数等于实指数的精确值。
主核 eta $.1$、$a=.147$、主过渡 $.16$、控制过渡 $.16$、$\lambda=.02$，
中心为原字面 `pi/4`。完整物理 profile、port payload 和材料长度
$L_{\rm bin}=1.3064834033904538$ 也分别绑定。

v1 已真实调用原 constructor，核对全部 19 个控制、实际 q、M20 与 J16 保留。
其原输出为 `closed_work/n4-core-binding-native.json`，SHA-256
`0c9f3e5616ee00ae4f8312299777481e437c2ae6438de7c4d88e45c207803f89`。
原 constructor 报告的 rho 下界 `.8125335440132911` 仍只是其数值 guard，
本条没有把它升级为独立全角严格界。

v2 只增加来源准入检查：逐字绑定九个原核心依赖和原
`bimodal_chart_loader.py`，并固定当前支持的定义指纹。
未来可以读取同定义下的新 q/c/profile/宽度/λ 的完整接受 checkpoint；
若核心、投影或材料角源发生变化，必须明确更新接口，不能仅凭同一个 kind 字符串套用旧公式。
v2 核对并复用上述同输入原 constructor 证据，没有重复构造核心或重跑 flow。

## n4 的实际控制定义

令 $T=\pi/2$，$\chi_p$ 是原主窗口，$W=1-\chi_c$ 是原控制窗口。
主 rho 模式为

$$
s(\phi)=-15\{(1+\eta)\cos4\phi-\eta\cos8\phi\},
\qquad C=15(1+2\eta),
$$

$$
\beta=-\frac{\int_0^T\chi_p(C-s)\,d\phi}
{T-\int_0^T\chi_p\,d\phi},\qquad
s_\lambda=s+\lambda\{\chi_p(C-s)+\beta(1-\chi_p)\}.
$$

定义积分给出 mean 零；原实现的求积和系数舍入误差仍须另付。
当本 eta 下 $\lambda=1$ 时，保护弧的单位主 rho 为 $C=18$；
当前 $\lambda=.02$ 还不是该精确圆弧。

首个 compact 列释放 physical c8，仅消 mean：

$$
B_2=W\left(\cos8\phi-
\frac{\langle W\cos8\phi\rangle}{\langle W\rangle}\right).
$$

$j\ge3$ 的 compact 列则为 $W\cos(4j\phi)$ 减去同权下对
$\{1,\cos8\phi\}$ 的投影。这与 m3 的 mean/cos3 锁定约定不同。
低端 $\lambda=0$ 的原列为
$\cos(4j\phi)+\ell_j\cos4\phi$：$\ell_j$ 来自冻结的 canonical J16，
$j>16$ 时为零。每个控制列在原低端与其 compact 端之间作原 λ 插值。
**J16 不是截去 modes 17–20 的指令**；所有 19 个物理系数和参数 jets 都保留。

令 $b=\sum_{j=2}^{20}c_j b_{j,\lambda}$，则完整核为

$$
\rho=1+q_{\rm actual}s_\lambda+b+b'',\qquad
\Gamma=n+q_{\rm actual}V+b\,n+b'\,t,
$$

其中 $n=(\cos\phi,\sin\phi)$、$t=(-\sin\phi,\cos\phi)$，
$V'=s_\lambda t$，真实旋转中心由
$(R_T-I)V(0)=\int_0^T s_\lambda t\,d\phi$ 确定。
弧长参数满足 $u(0)=0$、$du/d\phi=\rho$；因此
$\Gamma_u=t$、$\Gamma_{uu}=-n/\rho$。
接口沿用原实际积分和反函数构造，不拿 nominal Fourier 标签替代这些函数。

## 材料角链及 atlas 边界

原 `bimodal_chart_loader.py` 给出的 $\theta$ 是材料参数 $u$，不是法角 $\phi$。
核心先解原反函数 $\phi=\phi(u)$，再评价上述 $\Gamma$。
令材料图的独立参数为 $\eta_c$，记

$$
S=(1+\eta_c)\frac{\sin4\psi}{4}
-\eta_c\frac{\sin8\psi}{8},\quad
C_c=(1+\eta_c)\cos4\psi-\eta_c\cos8\psi,
$$

$$
D_c=4(1+\eta_c)\sin4\psi-8\eta_c\sin8\psi.
$$

接口提供原代数链
$\theta=\psi-eS$、$\theta_\psi=1-eC_c$、
$\theta_{\psi\psi}=eD_c$、$\theta_s=-e_sS$、
$\theta_{ss}=-e_{ss}S$、$\theta_{s\psi}=-e_sC_c$。
例如
$\partial_{\psi\psi}\Gamma(\theta)
=-n\theta_\psi^2/\rho+t\theta_{\psi\psi}$。
图的 eta 与主核 eta 分别读取；本次都为 $.1$，接口不将二者定义成同一参数。

$e,e_s,e_{ss}$ 必须由同一物理径向 profile 和 atlas 提供。
读取器不重新选择材料坐标，不调整长度来修接缝，不解码 prefix 多项式，也不付
真积分到有限 Gauss、反函数、完整径向链或闭图的误差。
后续实际尾是否接受仍须查真实 solver/Jacobian/audit 与全 metric，
不能由 `actual_nonlinear_tail` 标志或核心 constructor 成功替代。

## 执行来源

源为 `n4_integral_core_binding.py` 与独立 v2
`n4_integral_core_binding_v2.py`。
v1 constructor 真实执行 exit 0；v2 仅元数据和原证据绑定，亦真实 exit 0。
完整输入、10 个定义源哈希、19 个实际控制、原执行记录、v1 命令及 v2 命令见
[`n4_integral_core_binding_execution.json`](../scripts/resume_closed/n4_integral_core_binding_execution.json)。
没有重复旧全域 metric、没有执行失败实际尾，也没有修改任何生产源或 checkpoint。
