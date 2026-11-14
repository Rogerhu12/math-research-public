# 外头真实背景的正 Peano 核与全模解析传播预算

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

本证明给 [外头 Green/Schur 支付表](2026-11-12-tail-outer-green-schur-payment-plan.md)
中的可执行有限核与高模诊断。它使用已经保存的真实 source 面板，并保留实际
cap、valley controls、warp 以及外端 blend。不把内层特殊 profile 的积分原函数
外推到外0–11层。

## 1. 任意正背景上的准确正核

令 $H_m(r)$ 是背景线性高度模，$m\ge2$ 为偶数。R44 的兼容线性方程等价于

$$
H_{m,rr}+\frac{w_r}{w}H_{m,r}
-\frac{m^2w_r}{rw}H_m=0.
\tag{OBF.1}
$$

因此 $Z_m=wH_{m,r}$ 满足
$H_{m,x}=(r_x/w)Z_m$、$Z_{m,x}=m^2w_xH_m/r$。
固定整个外头的正实常数 $\mu_*$，置

$$
u_m=m^2-4,\qquad\nu_m=m^2(m^2-1)/12,
$$

$$
q=(r_c/r)^{u_m}\frac{H_m}{r^4},\qquad
v=(r/r_c)^{u_m}\frac{r^4(Z_m-m^2wH_m/r)}{\sqrt{12}\mu_*}.
\tag{OBF.2}
$$

直接求导可得

$$
q_x=a_m v,\qquad v_x=-b_m q,
\tag{OBF.3}
$$

$$
a_m=\sqrt{12}\mu_*(r_c/r)^{2u_m}r^{-8}r_x/w>0,
\qquad
b_m=\nu_m\sqrt{12}\mu_*^{-1}(r/r_c)^{2u_m}r^6r_xw>0.
\tag{OBF.4}
$$

为核查消去，将 $C=r^4Z_m-m^2r^3wH_m$ 求导。利用 (OBF.1)，所有含 $w_rH_m$
的项准确消去，得到
$C_r=-u_mC/r-m^2(m^2-1)r^6w(H_m/r^4)$；第一行从 $H_m/r^4$ 求导即得。
再作 (OBF.2) 的对角规范便得到 (OBF.3)–(OBF.4)。
这个推导只要求 $r_x>0,w>0$，不要求 $w_r$ 正、未cap或未warp。
由 $(H,Z)$ 到 $(q,v)$ 的行列式恒为 $1/(\sqrt{12}\mu_*)$，
所以整段背景规范流的行列式准确为1，且由于 $\mu_*$ 固定，跨胞元没有额外尺度跳变。

对一个真实面板 $I$，已经认证的正半径宽度 $\Delta r_I$、$r_I,w_I$ 给

$$
A_m:=\int_I a_m dx
\in\sqrt{12}\mu_*(r_c/r_I)^{2u_m}r_I^{-8}\Delta r_I/w_I,
$$

$$
B_m:=\int_I b_m dx
\in\nu_m\sqrt{12}\mu_*^{-1}(r_I/r_c)^{2u_m}r_I^6\Delta r_Iw_I.
\tag{OBF.5}
$$

这些都是正测度 $dr$ 上的区间积分界，而不是把某个面板中点当成常系数 ODE。
真实积分的先后顺序由 [R29](../results/R29-real-head-columns-and-boundary-green-envelope.md)
的正 Peano–Baker 路径界保留。若 $A_m^+B_m^+<1$，其已证明矩阵包围完整真实流和
所需子区间 majorant。程序使用更严格的声明门；门失败时必须细分同一 source，
不能把失败当成真实奇点。

有符号列的传播复用 R29 的共同幅度 projective 表示。两个独立规范基列同时传播，
其最终区间行列式必须包含1；准确行列式为1来自方程，数值包含仅是必要一致性核查。
全外头背景 $B_0$ 列以 node12 的 $Q_m=1$ 归一，初始动量取已认证真实内头线性
账本中的 `raw_worker_slope`。该字段使用 $\mu_{11}$ 坐标；取 $\mu_*=\mu_{11}$
时没有额外 $\rho$ 变换。它并非从 worker 有限 Robin 条件推定的值。

当 R44 的完整非均值第二源为 $N_m$ 时，(OBF.3) 第二行的额外源准确为

$$
\left(\frac r{r_c}\right)^{u_m}
\frac{r^4w^2}{\sqrt{12}\mu_*}\,N_m.
\tag{OBF.6}
$$

候选残差同样乘此系数。因此将规范 Green 核转回实际 $P/K$ 源时，必须保留这一列，
不能把 normalized、canonical 或物理残差的数值直接互换。

## 2. 背景第二源列与有限 Schur 比值

令 $a$ 为 node12、$b$ 为待验证的外端。设 $\phi$ 是上述真实 $B_0$ 列，
$\psi$ 是满足 $\psi_q(b)=0,\psi_v(b)=1$ 的同一背景列。
Wronskian $W=\det(\phi,\psi)=\phi_q(b)$ 恒定。
若 $W\ne0$，零外高度、内端在线性 $B_0$ 直线上的源核第二列为

$$
G(x,t)e_2=
\begin{cases}
\phi(x)\psi_q(t)/W,&x<t,\\
\psi(x)\phi_q(t)/W,&t<x.
\end{cases}
\tag{OBF.7}
$$

其跳跃为 $e_2$，因为
$\psi(t)\phi_q(t)-\phi(t)\psi_q(t)=(0,W)^T$。
左右边界条件由 $\psi_q(b)=0$ 与内端直线直接核查，故是准确两点核。
同一公式也由 R44 的有限秩修正得到。

若真实 head 导数相对 $B_0$ 的低高度差准确为零，则低模内端只新增 $\delta v$。
外端高度响应是 $-b^4(b/r_c)^{u_m}\psi_q(a)\delta v$，而背景参数列的外高度是
$b^4(b/r_c)^{u_m}\phi_q(b)$。故 Schur 相对误差可直接用

$$
-\frac{\psi_q(a)}{\phi_q(b)}\,\delta v.
\tag{OBF.8}
$$

这是准确比值公式，不是该比值已经很小的断言。它说明应保留两列的同一有序位置，
避免把独立的巨大 Cauchy 传播上界乘一个全局最坏 trace 差。

## 3. 对全部高模有效的独立解析传播预算

正 Peano 有限窗不足以说明无穷高模在某个条带中有界。
为此可同时利用 R44 的原物理归一背景矩阵

$$
A_m=\begin{pmatrix}-s-\ell&-ms\\-m\ell&-2\ell\end{pmatrix},
\qquad s=r_x/r>0,\quad\ell=w_x/w.
$$

在每个真实面板选一个**固定**正数 $b_I$，令 $u=(P,\bar K/b_I)$。
例如程序取准确向上 dyadic
$b_I=(1+\sup_I|\ell|/\inf_I s)^{1/2}$ 的上包。
则 $u$ 的矩阵对称部分最大特征值不超过

$$
d_I(x)+m\gamma_I(x),\qquad
d_I(x)=\max(-s-\ell,-2\ell),\quad
\gamma_I(x)=\tfrac12|s b_I+\ell/b_I|.
\tag{OBF.9}
$$

这是对称二乘二矩阵的对角最大值加非对角绝对值上界。
逆向传播的相应对角界为
$\widetilde d_I=\max(s+\ell,2\ell)$，$\gamma_I$ 不变。
面板间 $b_I$ 变化时，前向欧氏范数乘数为
$\max(1,b_{\rm old}/b_{\rm new})$，逆向乘数为其反向版本。
所有这些乘数与 $m$ 无关，均须计入。

积分 (OBF.9) 并乘全部真实界面变换，可得整已覆盖区间

$$
\|\Phi_{PK,m}(x,a)\|_2
\le\exp(D_++m\Gamma),\qquad
\|\Phi_{PK,m}(a,x)\|_2
\le\exp(D_-+m\Gamma).
\tag{OBF.10}
$$

$\Gamma=\sum_I\int_I\gamma_I$，$D_\pm$ 含对角积分、全部 frame 跳变和首尾到
真实 $P/K$ 坐标的范数因子。程序对同一真实 $s,\ell$ 区间乘真实 source 长度给
向上包围；$b_I$ 固定，所以没有遗漏 $b_I'$。
无须通过角截断极限，因为每个偶整数 $m\ge2$ 都满足同一明确公式。

如果条带损失 $\tau_a-\tau_x\ge\Gamma$，则这个齐次传递在相应 Fourier
加权范数中具有与 $m$ 无关的界，欧氏/两分量 $\ell^1$ 的有限换范数因子另乘即可。
若所得 $\Gamma$ 大于可用宽度，这只说明**这一充分预算没有支付**：不能据此断言
真实传播不有界或外头不存在。未知源的连续条带核和一阶角导数恢复仍须另算；
齐次传播 (OBF.10) 不冒充完整有理源 Green 门。

## 4. 执行状态

实现为 `computations/tail_outer_background_column_flow.py`。
先消费实际 cells11、10，保留 $m=2,4$ 的真实 $B_0$ 与两个独立基列，
并在同一次流中记录对全部偶模有效的 (OBF.10) 预算。
该首段计算只到 node10；在完成 cells9–0、全部46窗、实际 $\Delta B$ 与全频源门
之前，均不宣称已得完整外头 Schur 逆或外头精确解。
命令和未运行身份先记录于
[准备清单](2026-11-12-tail-outer-background-flow-prepared-r1.json)，
实际运行另存正式资源及结果，不用准备记录冒充执行结果。
