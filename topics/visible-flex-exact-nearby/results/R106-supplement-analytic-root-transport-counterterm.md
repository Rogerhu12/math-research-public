# R106 补充：用解析传输源计算完整根有限部

2026-11-13，constructive-route。

**已证明：** 原始高度的约化根密度，可以准确改写为一个有限 cut 边界项，
加上根处解析的有符号积分源。新式不需要先求真射线的四阶径向导数，
也不依赖先前 $2\times10^{19}$ 兜底所用的极小复 $s$ 盘。
本文给出完整有限 Fourier 核和真实误差合同；当前没有宣称全首相位的
有限 Fourier 参考已经运行，也没有支付 R104 的有效 cutoff 或全 PDE 逆。

## 1. 同一密度、方向和归一化

沿 R106 第 3–4 节，根附近先把径向坐标改成指向负区的 $\rho$，再令
$\rho=s^2$。正根处原 mixed 系数必须反号。物理角仍是 $\theta$，
其周期为 $\pi/2$。写

$$
v(s,\theta)=2s\,q(s^2,\theta)-2\sigma s^2k(s^2,\theta),\qquad
\Theta_s=v(s,\Theta),\qquad J=\partial_x\Theta .
\tag{106RT.1}
$$

这里 $k=k_*$ 是实际密度根因子除以 $a$，而非单独的目标曲率根因子。
初始标签 $x$ 可以是原物理根角，也可以是已经支付的实际输入标签；
$J(0,x)$ 不必为 $1$。

固定原 R37 高度、完整零阶项和 R50/R106 的同一约化密度，令

$$
G(\rho,\theta)=\rho^{5/2}D_{\rm red}(\rho,\theta).
$$

$G,q,k$ 在同一个真实 root germ 中解析。记 $G_i$ 为关于物理 $\rho$
的 Taylor 系数，$q_0=q(0,\theta)$，$k_0=k(0,\theta)$。实际恒等式为

$$
k_0G_0=-\frac1{16}.
\tag{106RT.2}
$$

这来自 $G_0=-a_0/(16\sqrt{K_{0,r}(t)})$、
$k_0=\sqrt{K_{0,r}(t)}/a_0$，包括无限原函数和整个真实参数族。
它不要求有限近似的两个球相乘后数值上恰等于 $-1/16$。
若直接处理完整 $\mathcal F/\mu$，只把常数换成 $5/16$；
以下证明只使用该乘积对角变量恒定。

R106 的半程归一化准确是

$$
\frac12D_{\rm red}\,d\rho
=\frac{G(s^2,\theta)}{s^4}\,ds.
\tag{106RT.3}
$$

此处不再乘 $4$。$\theta$ 微分是物理角微分；最终输入标签的 Fourier
微分另按 R106 的一形式规则处理。

## 2. 解析余源的准确公式

定义三个可去奇的解析函数

$$
G_{[2]}(\rho)=\frac{G(\rho)-G_0-\rho G_1}{\rho^2},\qquad
q_{[1]}(\rho)=\frac{q(\rho)-q_0}{\rho},\qquad
k_{[1]}(\rho)=\frac{k(\rho)-k_0}{\rho}.
\tag{106RT.4}
$$

这些量在程序中用同一 Taylor 系数列移位产生，不能对相近区间值作差再
除以趋零的 $\rho$。置

$$
B_1=-G_1-\frac23\partial_\theta(q_0G_0),\qquad
B(s,\theta)=-\frac{G_0}{3s^3}+\frac{B_1}{s}.
\tag{106RT.5}
$$

完整正则源是

$$
\boxed{
\begin{aligned}
\mathcal R_\sigma(s,\theta)={}&G_{[2]}(s^2,\theta)
+\frac23\partial_\theta(q_{[1]}G_0)(s^2,\theta)\\
&-\frac{2\sigma}{3}s\,\partial_\theta(k_{[1]}G_0)(s^2,\theta)
-2\partial_\theta(qB_1)(s^2,\theta)
+2\sigma s\,\partial_\theta(kB_1)(s^2,\theta).
\end{aligned}}
\tag{106RT.6}
$$

它在 $s=0$ 解析。其偶次部分与 $s$ 乘一个偶次部分分开保留，均允许
非零角平均和全部正负 Fourier 频率。

**定理。** 对 $s>0$，

$$
\frac{G(s^2,\theta)}{s^4}
=\partial_sB+\partial_\theta(vB)+\mathcal R_\sigma .
\tag{106RT.7}
$$

因此到同一真实 cut $s=c>0$ 的约化有限部准确等于

$$
\boxed{
\operatorname{FP}\int_0^c
 \frac{G(s^2,\Theta)J}{s^4}\,ds
=J(c,x)B(c,\Theta(c,x))
 +\int_0^c \mathcal R_\sigma(s,\Theta(s,x))J(s,x)\,ds.}
\tag{106RT.8}
$$

两项都是标签一形式。公式对真实根标签的任意已付复参数化成立；
没有把 $J$ 默认为 $1$。

**证明。** 直接微分 (106RT.5) 得

$$
\begin{aligned}
\partial_sB+\partial_\theta(vB)
={}&\frac{G_0}{s^4}-\frac{B_1}{s^2}
-\frac{2}{3s^2}\partial_\theta(qG_0)
+\frac{2\sigma}{3s}\partial_\theta(kG_0)\\
&+2\partial_\theta(qB_1)-2\sigma s\partial_\theta(kB_1).
\end{aligned}
$$

代入 $B_1$、$q=q_0+s^2q_{[1]}$、
$k=k_0+s^2k_{[1]}$，利用 (106RT.2)，逐项得到 (106RT.7)。
一形式的真拉回恒等式为

$$
\partial_s\{J B(s,\Theta)\}
=J\{\partial_sB+\partial_\theta(vB)\}(s,\Theta).
$$

所以只需检查下端有限常数。以实际根角 $\theta_0$ 为标签，
$\Theta=\theta_0+q_0s^2-2\sigma k_0s^3/3+O(s^4)$，相应

$$
J G_0(\Theta)
=G_0+s^2\partial_\theta(q_0G_0)
-\frac{2\sigma}{3}s^3\partial_\theta(k_0G_0)+O(s^4).
$$

最后一个显示项为零。$B_1(\Theta)J/s$ 没有常数项，因为 $\Theta-\theta_0=O(s^2)$。
故 $JB$ 在 $s=0$ 的有限常数准确为零。换到任意实际输入标签只把上述
一形式乘真实初始标签导数，不改变零常数。积分并取有限部即得 (106RT.8)。$\square$

如果真实 $k_0G_0$ 不是常数，(106RT.7) 要保留
$-(2\sigma/3s)\partial_\theta(k_0G_0)$，并产生 logarithm；
不能把上述可去奇结论套给另一个模型。

## 3. 对完整首相位必须保留的其余项

(106RT.8) 只替换 R106 (106.27) 的第一项。完整原始高度首相位仍为

$$
\begin{aligned}
h_\sigma={}&J_cB(c,\Theta_c)+\int_0^c(\mathcal R_\sigma\circ\Theta)J\,ds\\
&+\frac12\partial_x\int_0^{c^2}S\circ\Theta\,d\rho
-\frac14[J(V_\rho+\sigma L_\theta)\circ\Theta]_{c^2}
+\frac{\sigma}{4}J_0(\log\kappa_0)_\theta(\Theta_0).
\end{aligned}
\tag{106RT.9}
$$

$S=O(\rho^{-1/2})$，故其 $s$ 密度 $sS(s^2,\theta)$ 也解析。
cut 的三个一形式可先准确合成一个有限函数，避免分别用大模数相加。
这一步没有删除 cut 项或根端周期导数；对两根与严格区接合时仍须同
真实端点、同方向和同 frame。

## 4. 完整有限 Fourier 系数核

源文件 scripts/fourfold_subprincipal_root_regularized_transport.py 接受三个
**明确的有限** $\rho$–Fourier 多项式 $\widehat G,\widehat q,\widehat k$。
物理周期 $\pi/2$ 下频率为 $e^{4ij\theta}$，因此角导数乘 $4ij$。

核保留卷积的全部输出频率。令 $*_j$ 为完整 Laurent 卷积，帽子表示
有限输入，$\widehat B_1=-\widehat G_1
-\frac23\partial_\theta(\widehat q_0\widehat G_0)$。输出

$$
\begin{aligned}
\widehat{\mathcal R}_{2n}
&=\widehat G_{n+2}
+\frac23\partial_\theta(\widehat q_{n+1}\widehat G_0)
-2\partial_\theta(\widehat q_n\widehat B_1),\\
\widehat{\mathcal R}_{2n+1}
&=-\frac{2\sigma}{3}\partial_\theta(\widehat k_{n+1}\widehat G_0)
+2\sigma\partial_\theta(\widehat k_n\widehat B_1).
\end{aligned}
\tag{106RT.10}
$$

有限多项式范围之外的系数才定义为零。未知的真实系数不在此处填零，
其费用由下一节单独支付。真实恒等式 (106RT.2) 由几何证明使用；
有限球乘积残差无需、也不允许通过改动实际几何偷偷清零。
脚本同时返回准确 cut 多项式的 $s^{-3}$、$s^{-1}$ 两项。

## 5. 三个有限输入的完整误差传播

设真实与有限三个函数都在 $|\rho|\le R$、物理角带 $S$ 上解析。
在同一域已支付

$$
|G|\le M_G,\quad |q|\le M_q,\quad |k|\le M_k,\qquad
|G-\widehat G|\le e_G,\quad|q-\widehat q|\le e_q,\quad|k-\widehat k|\le e_k .
$$

这些是完整函数差，包括有限系数球选择、角 alias、未留 Fourier 模、
径向 Taylor 尾和无限 R33 primitive，不是节点最大值。
令 $\widehat M_q,\widehat M_k$ 是有限多项式在同一域的完整模数，
也可安全取 $M_q+e_q,M_k+e_k$。

选择 $r<R$、$\delta_1,\delta_2>0$，工作物理角带
$S-\delta_1-\delta_2>0$，$c^2\le r$，记 $d=1-r/R$。Cauchy 系数估计给

$$
\begin{gathered}
|\Delta G_{[2]}|\le e_G/(R^2d),\quad
|\Delta q_{[1]}|\le e_q/(Rd),\quad
|\Delta k_{[1]}|\le e_k/(Rd),\\
|B_1|\le B:=M_G/R+\frac{2M_qM_G}{3\delta_1},\\
|\Delta B_1|\le e_B:=e_G/R+
       \frac{2(e_qM_G+\widehat M_q e_G)}{3\delta_1}.
\end{gathered}
\tag{106RT.11}
$$

第一个移位商的证明，例如
$\Delta G=\sum a_n\rho^n$、$|a_n|\le e_G/R^n$，
所以 $\sum_{n\ge2}|a_n|r^{n-2}\le e_G/(R^2d)$；
并不对 $1/\rho^2$ 的区间值作粗除法。

在整个 $|s|\le c$ 和工作角带上，真正则源与选定有限源之差满足

$$
\boxed{
\begin{aligned}
e_{\mathcal R}={}&\frac{e_G}{R^2d}
+\frac{2}{3\delta_2Rd}
 \{e_qM_G+\widehat M_qe_G
       +c(e_kM_G+\widehat M_ke_G)\}\\
&+\frac{2}{\delta_2}
 \{e_qB+\widehat M_qe_B+c(e_kB+\widehat M_ke_B)\}.
\end{aligned}}
\tag{106RT.12}
$$

cut 多项式的差另有

$$
e_{B(c)}\le e_G/(3c^3)+e_B/c.
\tag{106RT.13}
$$

证明逐个使用完整乘积差
$uv-\widehat u\widehat v=(u-\widehat u)v+
\widehat u(v-\widehat v)$，再在相应角带损失上用 Cauchy。
(106RT.11) 的 $B_1$ 及其误差先只损失 $\delta_1$；
(106RT.12) 的外层角微分再损失 $\delta_2$，没有重复使用同一域裕量。

这些不等式适用于整个真实参数盒；有限源可以是一份中心参考，只要相对于
整个盒的三个 $e$ 已真实支付。它不要求有限源本身形成同一个参数族。

## 6. 接实际射线参考与有符号积分

设同一闭实 $s$ 段上，真射线 $\Theta,J$ 与参考 $Y,Q$ 满足
$|\Theta-Y|\le e_\theta$、$|J-Q|\le e_J$、$|Q|\le Q_*$。
角线段均在真源的已付角域中。若 $|\mathcal R|\le M$、
$|\partial_\theta\mathcal R|\le M_\theta$，则

$$
|(\mathcal R\circ\Theta)J-(\widehat{\mathcal R}\circ Y)Q|
\le M e_J+Q_*(M_\theta e_\theta+e_{\mathcal R}).
\tag{106RT.14}
$$

这是一次准确加减 $(\mathcal R\circ\Theta)Q$ 和
$(\mathcal R\circ Y)Q$，不把已证主返回端点误差当作全时误差。
全时 $e_\theta,e_J$ 可以引用 R106 已付管，但必须采用同一对象/标签/参数范围。
积分时乘该段实际 $ds$ 长度；若使用原 $\tau$ 网格，须真实乘 $ds/d\tau$。
cut 边界独立按 (106RT.13) 和同样的一形式误差规则支付。

有限参考 $\widehat{\mathcal R}(s,Y)Q$ 的全部 Fourier 系数及零频应保留。
其平均不替代完整函数，且有限乘积的高输出列不可丢弃。
R104 的 $b-\beta$ 还需要两根、严格区、(106RT.9) 所有项、
R46 真实 frame/共轭和普通源接线，及整个强余项；本式不提前授予这些输入。

## 7. 当前执行状态与下一实际输入

本证明的代数恒等式已用独立准确 Laurent 多项式核逐系数核算，
含非恒定 $k_0,G_0$ 而 $k_0G_0$ 恒定的校准，以及故意破坏该条件的
logarithm 残差校准。该小报告不是实际候选的积分证书。

实际候选已有同族 $|G|<0.046635$ 整根盘迁移，以及真实全时 $\Theta,J$ 管。
本次新增的整复根盘 q/k 入口尚待原生重跑；根处低 jet 不会被擅自外推。
得到真实 q/k 与完整非均值 Taylor–Fourier 系数后，(106RT.10)–(106RT.14)
可以直接生成有限有符号积分及误差。环境恢复前只保存源与证明，不捏造
整根盘或完整 b 的新数值报告。
