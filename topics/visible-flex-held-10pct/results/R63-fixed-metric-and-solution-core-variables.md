# R63：固定目标度量的未知核心，与规定精确入口的区别

维护：Astra-held10-06bbeb39-20261126 / fixed_metric。2026-11-26。

**状态：已证明（度量独立性、同一个无限维核心空间及其连续性、两种离散系统的代数区别）。** 不包含新完整 BVP 存在性、数值收敛或 10% 完成结论。

本条补足一个此前接续路线容易混淆的区别。冻结完整旋转目标度量并不一般要求把某一有限近似的所有入口 Fourier 系数视为精确边界数据。后者是一个更强的 BVP。允许系数作为同一个完整方程的未知解进行精化，必须满足下文规定的、与离散阶数无关的物理数据及 Cauchy 条件；不能用改名掩盖形状参数任意漂移。

## 1. 连续 Frenet 方程的目标度量

**命题 1。** 设 $a\in C^1([0,L])$、$a>0$、$a(0)=1$，且
$X\in C^2([0,L]\times\mathbb R/2\pi\mathbb Z,\mathbb R^3)$。
令

$$
G=|X_\theta|^2>0,\qquad T=X_\theta/\sqrt G,
$$

并设 $X_{\theta\theta}$ 在 $T^\perp$ 中的分量处处不为零。写

$$
\kappa=\frac{|X_{\theta\theta}-\langle X_{\theta\theta},T\rangle T|}{G},
\quad
N=\frac{X_{\theta\theta}-\langle X_{\theta\theta},T\rangle T}{\kappa G},
\quad B=T\times N.
$$

若

$$
X_s=\alpha N+\beta B,\qquad
\alpha=-\frac{a'}{a\kappa},\qquad
\beta=\sqrt{1-\alpha^2}>0, \tag{1}
$$

且 $|X_\theta(0,\theta)|=1$，则

$$\boxed{X^*e=ds^2+a(s)^2d\theta^2.} \tag{2}$$

**证明。** 正交单位标架给 $|X_s|^2=1$ 和
$\langle X_s,X_\theta\rangle=0$。对后一恒等式关于 $\theta$ 求导，使用 $X\in C^2$，得

$$
\langle X_{s\theta},X_\theta\rangle
=-\langle X_s,X_{\theta\theta}\rangle
=-\alpha\kappa G.
$$

所以

$$G_s=2\langle X_{s\theta},X_\theta\rangle
=2(a'/a)G.$$

固定 $\theta$ 解这个一维线性方程，得到
$G(s,\theta)=a(s)^2G(0,\theta)=a(s)^2$。这与已得的另外两个度量分量组成 (2)。这个证明不需要对 $N$ 或 $B$ 求导，因而没有额外假定 $C^3$ 正则性。证毕。

因此，任意允许的单位速入口曲线都给出同一个形式目标 (2)；曲线改变后方程能否延拓或匹配真实尾是另一个问题。目标 (2) 只含 $a$，没有入口的外在形状系数。

对一个事先固定的材料图 $\theta=\Theta(s,\psi)$，其表达为

$$
g_\Theta=(1+a^2\Theta_s^2)\,ds^2
+2a^2\Theta_s\Theta_\psi\,ds\,d\psi
+a^2\Theta_\psi^2\,d\psi^2. \tag{3}
$$

固定 $a$ 和 $\Theta$ 后，此坐标变换也不引入入口形状参数。

## 2. 与阶数无关的原支撑函数空间

下面把实际三重核心的有限系数放进一个明确的无限维空间。置

$$
\mathcal A_4=\left\{(b_j)_{j\ge1}:\;
\|b\|_{4}:=\sum_{j\ge1}(1+(3j)^4)|b_j|<\infty\right\}.
$$

对于 $b\in\mathcal A_4$，定义

$$
h_b(\varphi)=1+\sum_{j\ge1}b_j\cos(3j\varphi),\qquad
\rho_b=h_b+h_b''.
$$

取开集 $\rho_b>0$。每个有限向量按**末尾严格补零**嵌入此同一空间。符号 $b_1=q_{\rm actual}$、$b_{j\ge2}=c_{3j}$ 仅是现有源码记号的对应。

令 $P=2\pi/3$，并定义

$$u_b(\varphi)=\int_0^\varphi\rho_b(v)\,dv.$$

由 Fourier 级数的绝对一致收敛，$h_b\in C^4$、$\rho_b\in C^2$。每个完整 $P$ 周期内余弦积分为零，所以

$$u_b(\varphi+P)=u_b(\varphi)+P.$$

严格正的 $\rho_b$ 使 $u_b$ 有单调逆 $\varphi_b$。原支撑曲线

$$
\gamma_b(u)=h_b(\varphi_b(u))e^{i\varphi_b(u)}
+h_b'(\varphi_b(u))i e^{i\varphi_b(u)}
$$

满足

$$\gamma_b'(u)=i e^{i\varphi_b(u)},\qquad
\kappa_b(u)=\varphi_b'(u)=\frac1{\rho_b(\varphi_b(u))}.$$

证明只需对支撑曲线先关于 $\varphi$ 求导，得到
$i\rho_b e^{i\varphi}$，再乘 $\varphi_b'=1/\rho_b$。所以全部 $b$ 给出的入口周长均为 $2\pi$、速度均为 $1$。这正是命题 1 的相同入口度量条件。

## 3. 固定 R53 圆化数据仍保持单位速，并连续依赖未知核

固定 $0<S<S+d<P/2$、$k>0$、$\lambda\in[0,1]$。
本节取实际最终圆化使用的 `curvature_blend=1`，因此 $k$ 是固定数据。
令 $c=P/2$。取与当前源码相同的偶截止函数 $\chi(x)$：

- $\chi(x)=1$ 于 $|x|\le S$；
- $\chi(x)=0$ 于 $|x|\ge S+d$；
- 在过渡带使用 $1-S_9((|x|-S)/d)$，其中
  $S_9(t)=126t^5-420t^6+540t^7-315t^8+70t^9$。

于是 $\chi\in C^4$，且 $\int_0^c\chi(x)\,dx=S+d/2$。置

$$
C(x)=\int_0^x\chi(v)\,dv,\qquad
\Omega_b(x)=\int_0^x\chi(v)(k-\kappa_b(c+v))\,dv,
$$

$$
B_0=c-S-d/2>0,\qquad
\eta_b=-\Omega_b(c)/B_0.
$$

在 $0\le u\le P$ 定义相位

$$
\Phi_b(u)=\varphi_b(u)+\lambda\{\Omega_b(u-c)
+\eta_b[(u-c)-C(u-c)]\}. \tag{4}
$$

这就是 `_omega`、`_beta_all`、`_phase_fields` 的实积分定义。现有有限 Gauss 规则用于评价这些积分；本命题不把有限求积值称为精确值。

由于 $h_b$ 关于 $0,c$ 反射对称，有 $\varphi_b(c)=c$、
$\kappa_b(c+x)=\kappa_b(c-x)$。因此 $\Omega_b,C$ 为奇函数；
在两端的相位修正精确消失：$\Phi_b(0)=0$、$\Phi_b(P)=P$。
微分 (4) 得

$$
\Phi_b'=(1-\lambda\chi)\kappa_b+\lambda\chi k
+\lambda\eta_b(1-\chi). \tag{5}
$$

在端点邻域 $\chi=0$，所以相位的各阶导数在周期两端匹配。将其延拓为
$\Phi_b(u+P)=\Phi_b(u)+P$。令

$$
I_b=\int_0^P i e^{i\Phi_b(v)}\,dv,\qquad
z_b=\frac{I_b}{e^{iP}-1},\qquad
\Gamma_b(u)=z_b+\int_0^u i e^{i\Phi_b(v)}\,dv. \tag{6}
$$

分母非零。由定义 $\Gamma_b(P)=e^{iP}\Gamma_b(0)$，同时一阶、二阶导数满足同一旋转匹配；因而旋转延拓给一条闭 $C^2$ 曲线，且

$$|\Gamma_b'|=1.$$

若 (5) 为正，它还满足当前 Frenet 核所需的正曲率条件。这里不以有限样点替代该正性。

**准确圆弧。** 当 $\lambda=1$，在 $|u-c|<S$ 有 $\Phi_b'=k$，故

$$\Gamma_b(u)-k^{-1}e^{i\Phi_b(u)}$$

的导数为零。该材料窗上的曲线是一段半径 $1/k$ 的准确圆弧。其中心位置依赖未知 $b$；曲率和材料窗是固定数据。低于 $1$ 的 $\lambda$ 不得到这个结论。

**连续性。** 若 $b^{(m)}\to b$ 于 $\mathcal A_4$ 且
$\rho_{b^{(m)}}\ge r>0$，则

$$\Gamma_{b^{(m)}}\longrightarrow\Gamma_b\quad\text{于 }C^2.$$

完整证明如下。加权绝对和控制支撑函数的 $0$ 至 $4$ 阶导数，所以
$h_m\to h$ 于 $C^4$、$\rho_m\to\rho$ 于 $C^2$。
逆函数首先满足

$$\|\varphi_m-\varphi\|_\infty
\le r^{-1}\|u_m-u\|_\infty.$$

这是因为 $u_m$ 的斜率至少为 $r$，可对同一个 $u$ 的两个逆像应用中值不等式。再使用

$$
\varphi_m'=\frac1{\rho_m\circ\varphi_m},\qquad
\varphi_m''=-\frac{\rho_m'\circ\varphi_m}{(\rho_m\circ\varphi_m)^3},
$$

$$
\varphi_m'''=
\frac{3(\rho_m'\circ\varphi_m)^2}{(\rho_m\circ\varphi_m)^5}
-\frac{\rho_m''\circ\varphi_m}{(\rho_m\circ\varphi_m)^4}
$$

及统一正下界，得到 $\varphi_m\to\varphi$ 于 $C^3$、
$\kappa_m\to\kappa$ 于 $C^2$。在 (4) 中积分和固定的非零除数
$B_0$ 都连续，所以 $\Phi_m\to\Phi$ 于 $C^1$（实际可得更高阶）。
最后 (6) 中 $z_m\to z$，并且
$\Gamma_m'=i e^{i\Phi_m}$、$\Gamma_m''=-\Phi_m'e^{i\Phi_m}$
一致收敛。证毕。

这给出一个充分条件，不声称当前计算已有这种加权 Cauchy 性。仅比较每个固定低模的值不足以满足它。

## 4. 一次性固定的完整问题

定义本条可用于后续求解的物理输入集合 $\mathscr P$：

- 完整旋转前缀 $a_\delta$（包括全部桥段）与整个共同材料定义域；
- 完整真实尾背景、其连续深尾方程与固定闭合条件；
- 对称阶数、$S,d,k,\lambda$、固定材料图 $\Theta$；
- 高度原点、刚体规范与最终时间区间；
- 如需要，预先指定的非零分支区域，例如 $b_1\in[q_-,q_+]$ 且 $q_->0$。

未知量为 $b\in\mathcal A_4$、前缀场 $X$、原尾场及其由相同场确定的均值原函数。方程包括 (1)、入口 $X(0)=\Gamma_b$、完整真实尾方程、全部共同 Cartesian 两 jet 和固定闭合条件；刚体自由度用 (6) 的旋转中心、反射轴和固定高度原点归一。不另加独立可调均值或 ODE forcing。

该问题与 $M$ 无关。有限阶只近似未知函数和方程。若在同一个
$\mathscr P$ 上获得 $b^{(M)}$ 的上述 Cauchy 性以及共同坐标中的全场
$C^2$ Cauchy 性，才有同一个最终核心 $b^\infty$ 和同一最终几何。
这不是把任意层间参数变化自动称为收敛。

更明确地：若全场 $F_M$ 在共同紧定义域上于 $C^2$ 收敛到 $F$，
且相对同一个正定 $g$ 的完整度量误差趋于零，则

$$F^*e=g.$$

因为一阶导数一致收敛时每个内积 $\langle\partial_iF_M,\partial_jF_M\rangle$
一致收敛到对应极限内积。因 $g$ 正定，$F$ 是等距浸入。此论断不自动
支付嵌入、全时间 reach、握持幅度或 $\delta_E>0$，这些条件仍须单独证明。

### 与用户的「参数不变」要求的关系

上述 $\mathscr P$ 不得跨加密层更换。特别是不能让 $\delta$、尾 valley/
warp、背景校准的物理根、圆弧窗或时间区间随 $M$ 优化，再把它们标成
未知解系数。$b_M$ 被允许变化的唯一理由，是它从一开始就是这个
$M$ 无关完整 BVP 的未知函数近似。若某次验收合同另外明确指定整个
入口 $\Gamma_*$ 或其全部系数，则该合同须继续保持；改成当前问题
必须另起序列，不能改写旧序列的身份。

## 5. 有限维兼容债的准确适用范围

设 $K$ 为节点数，$n=3M+1$。原有限系统有

$$n(K-1)\text{ 条内部方程},\quad n\text{ 条入口方程},\quad
M\text{ 条全部终端方程}.$$

未知为 $nK$ 个场值与 $M$ 个入口系数。入口消元
$Y_0=I_M(p)$ 后，两边同为 $n(K-1)+M$ 维。这只说明方程数量一致，
不保证 Jacobian 可逆或存在解。

若另外指定 $p=p_*$，未知数才减少 $M$。写剩下的内部和终端线性化为
$A\Delta Y+r_E$、$C\Delta Y+r_T$。在 $A$ 可逆时，同时消去全部残差
的必要且充分条件确实是

$$\eta=r_T-CA^{-1}r_E=0.$$

证明是内部方程唯一迫使 $\Delta Y=-A^{-1}r_E$，代入终端即得。
因此旧 `FrozenPhysicalField` 的兼容债公式正确；它属于「入口曲线
也被精确规定」的更强问题。它不构成第 4 节固定度量问题的无解证明。
允许入口函数作为未知，也不使这些终端条件消失；它只是保留了原来
允许的几何未知量。

## 6. 本次核对的实际代码与 SHA-256

恢复清单
`scripts/nonlinear_tail/m3_coupled_seed_deliverable/m3_source_recovery_manifest.json`
的 SHA-256 为 `8e177f9cd0ab54d6db1d29baff4faad5ba5fda5f073c4743ab55d35dda73576e`。
清单恢复包中的路径相对于 `topics/visible-flexible-closed-surface/`：

| 源路径 | SHA-256 |
|---|---|
| `notes/fixed_metric_mode3_bvp.py` | `e2e5cf08339c82fac24ef296dc721cec4e43852d2a6d963721ce69a1d8d7a11c` |
| `notes/fixed_metric_mode3_flow.py` | `0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5` |
| `scripts/950f-prefix-warped-bvp.py` | `eb70e36397ea47638e042e7f2ef465ccef30cd853342adf049c2e3718261ac70` |
| `scripts/950f-prefix-adaptive-chart-bvp-v2.py` | `958a9e2e428f8d64dfc786bed515bad77a208433fa16af7cbbe6f03b1bcc7ebe` |

其中 `SupportBVP.flow` 在 `fixed=True` 时返回事先固定的 `fixed_flow`；
`chart` 只读相同轮廓、桥长与固定参考端点；`WarpedFlow.__init__` 用
固定 `warp_q` 设置角图。`initial` 才把 $p$ 解码成未知核心，且其
$q_{\rm actual}$ 不是固定状态 gauge。

本课题的
`scripts/resume_transfer/material_flattened_support_core.py` SHA-256 为
`1d655f2bdad53e1d320c1115a9873abe399a9b7ba930722c415d02dedb9b1f20`。
它对应第 3 节公式的数值评价；有限 quadrature/反函数误差不由本条免除。

旧
`scripts/resume_n4/frozen_physical_field_refinement.py` SHA-256 为
`6fb4c749a6409aa0ad7ad76d31cf0999dab7bcd946bc7b7ff2048c5f9cba63c2`。
其固定入口解释按第 5 节保留。

## 7. 研究范围

本条没有把当前 $\lambda=.002$ 的开放 linear-DN 前缀升级成准确圆弧，
没有取得新的真实尾响应，没有支付某个 $b_M$ 序列的 Cauchy 性，
没有构造满足本题全部条件的闭族。它给出的实际改进是：后续可以在
明确同一个 $\mathscr P$ 上求原来允许的入口形状未知，并用同一极限核
和全场收敛来判断固定度量，而不必无理由地冻结一次有限近似的所有
核心系数。具体新运行必须另登记参数、完整误差和结果。
