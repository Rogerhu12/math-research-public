# R31. 原 M16/steps64 实际全闭图的连续同 g 度量界

**状态：已证明。** 会话 Astra-held10-7322d0de-20261118；共同工作 `closed_geometry`。2026-11-17 UTC。

## 结论与范围

对 R28 的同一有限 C² 闭族、同一固定标记帽及同一物理参数，前缀的全径向、全角和全相位相对度量误差满足

$$
 \sup\left\|g^{-1/2}(F_\alpha^*g_{\mathbb R^3}-g)g^{-1/2}\right\|_{\rm op}
 <\frac{8253}{10^{10}}=8.253\times10^{-7}.
$$

实际合并预算的有理数显示为 $8.252019861516903\times10^{-7}$。结合 R29 的整个有限尾、R21/R28 的圆领及 R24/R28 的固定帽，**同一实际全闭曲面**上严格有

$$
 \sup_{M,\,0\le\alpha\le\pi/3}
 \left\|g^{-1/2}(F_\alpha^*g_{\mathbb R^3}-g)g^{-1/2}\right\|_{\rm op}
 \le\frac{590094565153063}{590295810358705651712}<10^{-6}.
 \tag{1}
$$

式 (1) 的最大预算项仍是 R29 的尾上界。它们都是连续充分界，不能当作真实最大误差的估计。

本条使用的实际映射、Cartesian 系数、解析中心、cut lift、尾以及标记帽全部保持 R28 的定义。因此 R28 的全相位 C² 嵌入、reach、固定握持区和 $\delta_{\rm E}>0$ 证明继续适用。握持下界仍只有 $\delta_{\rm hold}/D>0.00546265624736514$，未达到 $0.1$。本条完成低幅实际闭图此前缺失的连续 metric 门；不声称严格存在无限精确解，也不把课题标为完成。

## 1. 原物理输入的精确前缀度量

R23 及已核对的 M8/M16 `physical_metric_descriptor` 固定的是物理输入：

$$
 \delta=.06105607686781097,\quad v_u=.45,\quad v_d=.5,
 \quad\varepsilon=.4,\quad\eta=.05,
$$

一次 outward cycle、flat ramp、ShortBridge 曲率参数 $K=4$、peak fraction $p=.2$，以及同一个真实尾端口 $r_c=.3,w_c=.08$。这些常数均按来源文件中 binary64 数的精确有理值解释。64 点 Gauss 节点、求积结果和浮点派生的桥长不在物理参数描述符里。

本条把该物理描述符按实数公式和真实积分解释，并显式支付原数值求积实现到它的误差。定义

$$
 T_u=\frac{\delta}{v_u(1-\varepsilon)},\qquad
 T_d=\frac{\delta}{v_d(1-\varepsilon)}.
$$

flat ramp 的原函数为

$$
 P(t)=\begin{cases}
 \dfrac{\eta^2}{1-\eta}\left(\dfrac{(t/\eta)^4}{4}-\dfrac{(t/\eta)^5}{10}\right),&0\le t\le\eta,\\
 \dfrac{t^2/2-\eta t/2+3\eta^2/20}{1-\eta},&\eta\le t\le1-\eta,\\
 t-\dfrac12+\dfrac{\eta^2}{1-\eta}\left(\dfrac{((1-t)/\eta)^4}{4}-\dfrac{((1-t)/\eta)^5}{10}\right),&1-\eta\le t\le1.
 \end{cases}
$$

令

$$
 I(u)=\begin{cases}
 \varepsilon P(u/\varepsilon),&u\le\varepsilon,\\
 u-\varepsilon/2,&\varepsilon\le u\le1-\varepsilon,\\
 1-\varepsilon-\varepsilon P((1-u)/\varepsilon),&u\ge1-\varepsilon.
 \end{cases}
$$

真弧长 $\sigma$ 上的第一段半径是 $1+\delta I(\sigma/T_u)/(1-\varepsilon)$，第二段是 $1+\delta-\delta I((\sigma-T_u)/T_d)/(1-\varepsilon)$。两段在端点回到半径1、零一二阶径向 jet，且 $|a_\sigma|\le\max(v_u,v_d)<1$。

桥的真端点导数取自 R21/R27 的真实尾：

$$
 w_{r,c}=-\frac{7w_c}{r_c},\quad
 \phi_t=\operatorname{atan2}(1,w_c),\quad
 \phi'_t=\frac{w_{r,c}}{(1+w_c^2)^{3/2}}.
$$

令 $\phi_* =\phi_t+p(\pi/2-\phi_t)$、$d=\phi_*-\phi_t$，

$$
 L_1=\frac{3\phi_*}{2K},\qquad L_3=\frac{2d}{-\phi'_t},
$$

$$
 J_1(u)=\int_0^u\sin\!\left(\phi_*(3v^2-2v^3)\right)dv,
 \qquad J_3(u)=\int_0^u\sin(\phi_*-dv^2)dv,
$$

$$
 L_2=\frac{1-r_c-L_1J_1(1)-L_3J_3(1)}{\sin\phi_*}>0.
 \tag{2}
$$

桥的三段转角分别为 $\phi_*(3u^2-2u^3)$、$\phi_*$、$\phi_*-du^2$；半径由 $a_\sigma=-\sin\phi$ 的真积分定义。式 (2) 使末端半径**恰好**为 $r_c$，并且末端的一二阶真弧长导数为

$$
 a'_*=-\frac1{\sqrt{1+w_c^2}},\qquad
 a''_*=-\frac{w_cw_{r,c}}{(1+w_c^2)^2}.
 \tag{3}
$$

固定的物理前缀度量是

$$
 g_*=d\sigma^2+a(\sigma)^2d\theta^2,
 \qquad 0\le\sigma\le L_*=T_u+T_d+L_1+L_2+L_3.
 \tag{4}
$$

它与尾 $g_*=(1+w(R)^2)dR^2+R^2d\theta^2$ 在真正 $R=r_c$ 处相接。flat 段和桥的上述端点恒等式保证所需的连续一二阶轮廓 jets。全程 $r_c\le a\le1+\delta$、$|a_\sigma|\le1$。

## 2. 各层共用的材料坐标，以及字面的 cut 接缝

原 M8 和 M16 checkpoint 已逐项核对 `frozen_profile`、`physical_tail_parameters`、`physical_tail_cut` 和 `meridian_length` 相同；共同材料区间末端为原 binary64 数

$$
 L_b=1.36034614418862.
$$

原32步与 R28 的64步尾使用同一前缀。令 $\lambda=L_*/L_b$。仅使用 $\sigma=\lambda s$ 已足以比较内部度量，但有限图的 cut atlas 已由 R23 固定为两个 binary64 数

$$
 A_b=-.996815278536125,\qquad B_b=.14744006140246674.
$$

它们就是由固定 $(r_c,w_c)$ 得到的 `TailCutTarget.ap/app`，各层相同。为在该**既有 atlas** 中表达同一个 (4)，定义

$$
 \mu=\frac{A_b}{a'_*},\quad
 \nu=\frac{B_b-a''_*\mu^2}{a'_*},\quad
 D_1=\mu-\lambda,\quad D_2=\nu.
$$

用原固定宽度 $h=.04$ 的右端 Hermite 基函数 $H^R_1,H^R_2$，其右端分别具有第一、第二单位 jet，其他零至二阶端点 jets 为零，设置

$$
 \sigma(s)=\lambda s+D_1H^R_1(s)+D_2H^R_2(s).       \tag{5}
$$

更明确地，若 $t=(L_b-s)/h$，则

$$
 H^R_j(s)=(-h)^j H_j(t),\quad
 H_1(t)=t-6t^3+8t^4-3t^5,\quad
 H_2(t)=\tfrac12t^2(1-t)^3,
$$

仅在 $L_b-h\le s\le L_b$ 非零。于是

$$
 \sigma(L_b)=L_*,\qquad
 (a\circ\sigma)'(L_b)=A_b,\qquad
 (a\circ\sigma)''(L_b)=B_b.                         \tag{6}
$$

所以可在切口取 $R=a(\sigma(s))$ 作过渡坐标，它的两 jet 与 R23/R28 实际图共同缝**完全相同**。这也给出同一全局 $g$ 在切口的坐标一致性。

式 (5) 仅是同一物理度量 (4) 的坐标转换。它由原物理参数、原共同 $L_b$、原固定 atlas 和原宽度唯一确定，没有新增可调设计量，没有按 M8/M16 或尾步数分别调整。实际嵌入的空间像及所有几何结论不受这一记号明确化影响。

真积分计算严格给出

$$
 5.89920978114\times10^{-17}<\lambda-1
 <5.89920978182\times10^{-17},
$$

$$
 |D_1|<1.090203\times10^{-16},\qquad
 |D_2|<2.671763\times10^{-17}.
$$

由 Hermite 权重界，整个条带有

$$
 |\sigma-\lambda s|<1.746461\times10^{-18},\quad
 |\sigma'-\lambda|<2.183077\times10^{-16}.           \tag{7}
$$

特别地 $\sigma'>0$，所以它是覆盖同一物理区间的固定 C² 坐标变换。实现中用于全部预算的向外 binary64 包围为

$$
 .9999999999999998\le\sigma'\le1.0000000000000004.
$$

## 3. 真桥积分与辅助半径五次式的严格误差

原 `ShortBridge` 的数值实现使用64点 Gauss 原函数；原 port 显示半径 $.29999999999999993$、斜率 $.08000000000000027$。本证明直接使用第1节真端口及积分，以上源差由本节全部计入。

将两个桥 integrand 在 $u=1/2$ 展开到96阶。置 $z=u-1/2$，转角分别是

$$
 \phi_*/2+(3\phi_*/2)z-2\phi_*z^3,
 \qquad\phi_*-d/4-dz-dz^2.
$$

在复圆 $|z|=1$ 上，$|\sin\phi(z)|\le e^{|\Im\phi(z)|}<512$；源码还直接区间验证 $e^{3.5\phi_*}<512$ 和 $e^{2d}<512$。Cauchy 系数界因此使 $|z|\le.501$ 上的截断余项至多

$$
 \epsilon_J=\frac{512(.501)^{97}}{1-.501}
 <7.861\times10^{-27}.                            \tag{8}
$$

对每项多项式精确积分，再加积分区间长度乘 (8)，得到真实部分积分包围；区间基本函数与 Taylor 系数全程向外运算。小于 $.001$ 的解析延拓范围也受同一界控制。

原数值源 `flow.profile` 在实际有限图节点返回的三个 radius jets 定义一个**辅助**共享 jet 五次式 $a_5(s)$。它只用于有限多项式代数；目标度量始终是 (4) 的拉回。

在每个原跨度选包含中点的真实解析分段。用真实公式包围左右端的半径零、一、二阶导数，分别与 $a_5$ 的定义数据相减。若三个端点误差界为 $e_0,e_1,e_2$、跨度长为 $\ell$，Hermite 基的直接因子式给出插值误差贡献

$$
 2e_0+2\ell e_1+\ell^2e_2.
$$

解析分段上的五次 Hermite 余项为

$$
 \frac{f^{(6)}(\xi)}{6!}(s-l)^3(s-r)^3,
$$

其绝对值至多 $\sup|f^{(6)}/6!|\ell^6/64$。flat 各解析段次数不超过5，该项精确为零；桥上的六阶导数由区间 Taylor 算术包围。

真实分段界与原 binary64 节点的微小错位也有单独预算：将所选解析段延拓到整个跨度，越界距离乘“真实及延拓的一阶导数界之和”。真实 $|a_\sigma|\le1$ 再支付 (7) 的坐标值修正。因此这一步没有假设两个分段界逐位相同。

2464个跨度的完整结果为

$$
 \sup_s|a_5(s)-a(\sigma(s))|
 <6.631693\times10^{-16}.                          \tag{9}
$$

这包括源 Gauss 近似、原 port 的 ulp 差、原浮点派生长度、真实分段界错位和固定接缝坐标转换。

## 4. 有限 Cartesian 部分的完整多项式度量代数

先暂不加解析中心及 cut lift。原 Cartesian $X(s,\psi)$ 的每个 Fourier 系数是由原 binary64 共享两 jet 定义的五次 Hermite 函数。相位图仍为 R28 的同一显式函数

$$
 \theta=\psi-e(s)\sin(3\psi)/3,\quad
 \rho=1-e(s)\cos(3\psi),\quad
 \tau=\theta_s=-e_s(s)\sin(3\psi)/3.
$$

本次对 $e$ 本身的完整多项式检查给出

$$
 |e|< .1600000000000003,\quad
 \rho\ge\rho_0:=8399/10000,\quad
 |e_s|< .591265325945376.                           \tag{10}
$$

置 $Y=\rho X_s-\tau X_\psi$。相对辅助度量 $g_5=ds^2+a_5(s)^2d\theta^2$，三个清分母分子恰为

$$
 A=|Y|^2-\rho^2,\qquad B=Y\cdot X_\psi,\qquad
 C=|X_\psi|^2-a_5^2\rho^2.                        \tag{11}
$$

其相对误差矩阵是

$$
 \rho^{-2}
 \begin{pmatrix}A&B/a_5\\ B/a_5&C/a_5^2\end{pmatrix}.       \tag{12}
$$

对每个原径向跨度使用局部变量 $t=(s-l)/(r-l)$。所有 Cartesian、$e$ 和 $a_5$ 的五次幂系数先从定义的二进制端点 jets **以精确有理算术**算出，再向外转为 binary64 区间。这避免极短插入跨度上先舍入端点差后除以跨度产生的虚假损失。

式 (11) 的所有径向多项式与角 Laurent 系数直接完整相乘。最高径向次数20，最高绝对角频率198；没有角采样、DFT 截断或 alias 假设。有限卷积沿用 R29 已证明的中心—半径外向卷积核。

每个径向幂多项式转成同次 Bernstein 形式，整个 $0\le t\le1$ 的系数值由控制点凸包包围。对每个角 Laurent 系数取绝对上界并求和，得到全角的 $N_A,N_B,N_C$。由 (12) 的绝对行和界，若 $a_5\ge r_5>0$，则

$$
 \|M_5\|_{\rm op}\le\rho_0^{-2}
 \max\{N_A+N_B/r_5,\ N_C/r_5^2+N_B/r_5\}.         \tag{13}
$$

这里逐跨度取 $r_5=r_c-\epsilon$，其中 $\epsilon$ 是该跨度的 (9) 预算。

转回真正的目标度量

$$
 g=\sigma'(s)^2ds^2+a(\sigma(s))^2d\theta^2
$$

时，令 $T=\operatorname{diag}(1/\sigma',a_5/a(\sigma))$。相对误差满足恒等式

$$
 M=T(M_5+I)T-I,
 \quad \|M\|_{\rm op}\le\|T\|^2\|M_5\|_{\rm op}+\|T^2-I\|_{\rm op}.    \tag{14}
$$

(7)、(9) 和 $a\ge r_c$ 把 (14) 的全部标量预算变为精确有理数。原2464个跨度首尾相接，完整覆盖 $[0,L_b]$。本次得

$$
 \eta_0:=\sup\|M\|_{\rm op}
 <5.115025\times10^{-9}.                           \tag{15}
$$

实际有理预算显示为 $5.115024008481289\times10^{-9}$，执行文件保存完整分数。此处已包含同一真实 g 的所有背景和坐标误差。

## 5. 解析核心修正的连续第一 jet

R28 的二阶角 Taylor 盒已足够证明几何，但其包围损失不宜直接拿来支付 $10^{-6}$ metric。本次对**同一个**解析核心修正使用四阶角 Taylor 余项，没有重新生成核心或改变 lift。

设原支持函数为 $h(\phi)=1+\sum c_m\cos(m\phi)$，$m\in3\mathbb N$。由 R28 的 $\rho_c=h+h''>.838107809$，弧长函数

$$
 \mathcal A(\phi)=\phi+\sum\frac{1-m^2}{m}c_m\sin(m\phi)
$$

严格单调。每个待用逆值都以左右端严格区间符号验证；本次512个全角盒共1025个逆包围。求逆提议本身不当作误差界。

由

$$
 \phi_\psi=\frac{1-e(0)\cos3\psi}{\rho_c(\phi)}
$$

递归求出一至四阶区间 Taylor 系数。设中心修正的三个径向端点函数为 $\Delta_j(\psi)$，$j=0,1,2$。在每个盒中心严格计算其零至三阶导数，在完整盒包围四阶导数；若半宽为 $b$，则

$$
 |\Delta_j|\le\sum_{k=0}^{3}|\Delta_j^{(k)}(c)|b^k/k!
       +\sup|\Delta_j^{(4)}|b^4/24,
$$

$$
 |\partial_\psi\Delta_j|\le\sum_{k=1}^{3}|\Delta_j^{(k)}(c)|b^{k-1}/(k-1)!
       +\sup|\Delta_j^{(4)}|b^3/6.                \tag{16}
$$

这些是每个完整角盒的连续分量界。这里的三重对称来自字面的有限函数定义：`M3CartesianPrefix` 固定平面频率为 $1+3k$，同一个复数和 $\sum p_k e^{i(1+3k)\psi}$ 定义 $X+iY$；高度频率及核心支持频率都是 $3j$。任意原 binary64 系数都满足所述变换恒等式，不需要把数值 DFT 的近零禁模当成零。认证代码也对实际输入的三组频率作了整数余数硬检查。

核心弧长函数满足 $\mathcal A(\phi+2\pi/3)=\mathcal A(\phi)+2\pi/3$，唯一的严格逆因此也满足该平移关系。$\theta(\psi+2\pi/3)=\theta(\psi)+2\pi/3$，而端点第二径向目标中的 $-e''(0)\sin3\psi/3$ 严格周期。原中心三个目标 jets 与原有限 Cartesian jets 故分别精确协变；作差和角微分仍保留它。所有 $\Delta_j$ 及其角导数满足

$$
 v(\psi+2\pi/3)=R_z(2\pi/3)v(\psi).
$$

一个平面向量的三个相隔 $2\pi/3$ 的旋转中，至少一个 x 投影绝对值不小于其长度的 $\sqrt3/2$；y 同理。若全角分量界是 $A_x,A_y,A_z$，因此

$$
 |v|^2\le\frac43\min(A_x^2,A_y^2)+A_z^2.          \tag{17}
$$

(17) 只收紧已经完成的连续盒界，未增加角采样或重扫。最终范数上界为：

| 径向端点 jet $j$ | $\|\Delta_j\|_\infty$ | $\|\partial_\psi\Delta_j\|_\infty$ |
|---|---:|---:|
| 0 | $1.430309\times10^{-10}$ | $9.324159\times10^{-8}$ |
| 1 | $3.838480\times10^{-15}$ | $1.469206\times10^{-13}$ |
| 2 | $1.024259\times10^{-9}$ | $6.665742\times10^{-7}$ |

原宽度 $h=.04$ 的 Hermite 值权重可取 $1,2h/5,h^2/20$，第一导数权重可取 $5/h,2,h/4$。相应修正向量 $U$ 满足

$$
 \|U_s\|\le1.788911\times10^{-8},\qquad
 \|U_\psi\|\le9.329492\times10^{-8}.                \tag{18}
$$

R28 已经证明的完整 cut lift 则有

$$
 \|U_s\|\le2.662980\times10^{-9},\qquad
 \|U_\psi\|\le5.258763\times10^{-10}.               \tag{19}
$$

## 6. 第一 jet 扰动的合并以及全部相位

在真正参考正交标架中，两列导数为

$$
 \frac{X_s-(\tau/\rho)X_\psi}{\sigma'},\qquad
 \frac{X_\psi}{\rho a(\sigma)}.
$$

因此 (18) 或 (19) 的导数扰动算子范数可取

$$
 d_U=\frac{\|U_s\|}{\sigma'_-}
 +\left(\frac{\|\tau\|}{\rho_0\sigma'_-}
       +\frac1{\rho_0r_c}\right)\|U_\psi\|,
 \quad\|\tau\|\le\|e_s\|/3.                     \tag{20}
$$

执行使用未经十进制截断的全部有理预算，得到核心 $d_U$ 显示为 $4.100433949064299\times10^{-7}$、cut 为 $4.8734393212691514\times10^{-9}$。两个支撑条带不相交，故取两者最大值 $d$。

由 (15)，原导数矩阵范数不超过 $\sqrt{1+\eta_0}\le1+\eta_0$。Gram 扰动恒等式给出

$$
 \eta_{\rm prefix}\le\eta_0+2(1+\eta_0)d+d^2
 <8.253\times10^{-7}.                             \tag{21}
$$

活动区的相位作用是材料角平移和空间转动；参考度量 (4) 以及尾部旋转度量对该材料角平移不变。全角界故覆盖全部 $\alpha\in[0,\pi/3]$。标记帽逐点固定，使用原固定帽自身的度量，其误差为零。圆领沿用 R21/R28 的 $1.36\times10^{-29}$ 连续界。因此 (21) 与 R29 正好覆盖全闭面，得到 (1)。

## 7. 来源、实际执行与局限

同一 R28 输入的 `prefix-shared-cartesian.npz` SHA-256 为
`7818de0de1873edf18ded4551f0e6044f9c5768271c5cd7a07695020b706d052`。
源 M16 prefix checkpoint SHA-256 为
`7bab356153195aed714bcdd68c893755891bda8235c88cbc4cf065354ee30a6f`。
完整新代码和执行记录为：

- [prefix_true_profile.py](../scripts/resume_closed/prefix_true_profile.py)：固定真物理轮廓、真实桥积分、共同坐标转换及辅助 radius 误差。
- [interval_prefix_metric.py](../scripts/resume_closed/interval_prefix_metric.py)：有理共享 jets、完整径向多项式/Laurent 代数及 Bernstein 连续界。
- [certify_prefix_center_first_jet.py](../scripts/resume_closed/certify_prefix_center_first_jet.py)：同一解析核心的新四阶 Taylor 第一 jet 界。
- [sharpen_prefix_center_norms.py](../scripts/resume_closed/sharpen_prefix_center_norms.py)：精确三重协变的无重扫范数收紧。
- [certify_continuous_prefix_metric.py](../scripts/resume_closed/certify_continuous_prefix_metric.py)：2464个完整跨度与实际所有修正项的合并。
- [continuous_prefix_metric_execution.json](../scripts/resume_closed/continuous_prefix_metric_execution.json)：实际三条命令、全部来源、参数及输出 SHA-256。

四阶核心计算完成于106.42秒；协变收紧仅使用该输出的已证分量界；完整 prefix 计算完成于328.00秒，两次主计算均观察到 exit code 0。可再生的逐跨度表只在 scratch 保留，其 hash 进入执行记录。

R28 的数值加密对照仍与本证明相互区分：M8→M16、steps32→64 的全图采样 metric 下降到原求解容差附近，是既有数值证据；式 (1) 是当前同一个有限图的连续误差门。它们都没有单独证明无限方程有精确极限。接下来应将已补齐的全闭图接口用于有实质幅度提升的接受态，继续支付同 g 加密和 10% 握持标准。
