# R2：同一全前缀的传输分子相消与普通源 Green 界

日期：2026-11-10。作者：visible-exact-astra-76e8 / a_posteriori_pde。

**状态：已证明。** 对同一 flat17 精确径向背景、第一周期和唯一精确桥，完整证明下列全频估计：齐次 incoming 到内部与普通 source 到 outgoing 的角解析带损失从原保守 $0.918$ 降为 $0.459$；普通 source 到内部仍保留 $0.918$，其常数和角阶另有改进。全程保留普通两分量 $L^2$ 源、均值及真实接口，不另要求源的径向导数。

这不是当前非径向候选的真实核心–无限尾 Robin 逆，也未证明本题可见振幅精确闭曲面。完整推导如下；研究延伸记录在 `notes/2026-11-10-a-posteriori-pde.md`。

## 0. 实际输入及作用域

已读取相邻课题以下原文；R74/R77/R79/R80 与本会话从 `origin/main` 提取的副本逐字一致：

- `topics/visible-flexible-closed-surface/results/R74-ramp-analytic-cauchy-provider.md`；
- `R75-flat17-sturm-frequency-propagator.md`（本次所读 Git blob `eedd5e70768c34d36989a2988c67a3d48233c751`）；
- `R77-actual-support-robin-bridge-port-transfer.md`；
- `R79-exact-bridge-two-barrier-feedback.md`；
- `R80-full-prefix-analytic-ordinary-source-provider.md`。

沿用它们的同一个真实 Sturm 系统
$$
Z_n'=-in\begin{pmatrix}0&V(r)\\1&0\end{pmatrix}Z_n+g_n,
\qquad Z_n=(x_n,y_n)^T,\qquad k_n=(1+n^2)^{1/2}.
\tag{0.1}
$$
第一周期记为 $c$，其后的唯一精确桥记为 $b$。源始终是普通 $L^2_r$ 的两分量源，不对第二分量另加径向导数或端点迹。

记
$$
P=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\quad z=PZ,\quad J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$
一个模块的 incoming 和 outgoing 分别为
$$
\mathrm{in}=(z_+(0),z_-(R))^T,\qquad
\mathrm{out}=(z_-(0),z_+(R))^T.
\tag{0.2}
$$
令 $I=|\mathrm{in}|$、$O=|\mathrm{out}|$、$F=\|g\|_{L^2}$、
$$
E=|Z(0)|+|Z(R)|,\qquad
\mathcal N=\max\{\|Z\|_{L^\infty_r},\|Z\|_{L^2_r}\}.
$$
R75/R80 已由有限维 ODE 真正构造逐模解，且齐次散射矩阵酉；本文无需假设待估解已存在。所有 Fourier 求和在第 6 节说明。

下面只使用以下已付输入：

1. 周期 $R_c<3/2$，中央负势段长 $\ell_c>5/12$，$|V|<81/80$；每个非负势外区双向传播 $\|T^c_n\|\le6k_n^2$；全周期 Cauchy 传播 $\|T^c_n(R_c,0)\|\le17k_n^5e^{\alpha|n|}$，$\alpha=459/1000$。
2. 桥 $R_b<21/10$，左负势段长 $\ell_b>1/15$，$|V|<1200$。右非负势段可写成 $V=\omega v$，其中 $\omega$ 递减、$v$ 递增，$1/5<\omega<216$、$0\le v<17/4$、$V<918$。
3. 任一中央非正势区的弱零 Dirichlet Green 表示给
$$
\sup|y|\le\max(|y(0)|,|y(\ell)|)
 +\left(\frac{|n|\ell^{3/2}}4+\sqrt\ell\right)F.
\tag{0.3}
$$
这来自 $(-\partial_r^2-n^2V)y=in g_1-\partial_rg_2$、$0\le G\le\ell/4$ 和 $|G_t|\le1$；没有对 $g_2$ 求经典导数。

## 1. 桥的非负势外区：一次角阶损失即可

**命题 1。** 对桥的同一右非负势外区内任意两点、任意方向和全部 $n\in\mathbb Z$，
$$
\|T^b_n(r_1,r_0)\|\le3100k_n.
\tag{1.1}
$$

**证明。** 固定 $n$，置 $m=k_n^{-1}$、$q=\sqrt{V+m^2}$、$S=\operatorname{diag}(1,q)$。R75 的直接能量计算在 $V\ge0$ 区给
$$
\|T(r_1,r_0)\|
\le e^{R_b/2}\max(1,q_0)\max(1,q_1^{-1})
\exp\!\int(\log q)'_+.
\tag{1.2}
$$
保留这里的两个实际端点值，不把它们各自先换成最坏常数。

先取正向 $r_0<r_1$。因 $\omega'\le0$、$v'\ge0$，
$$
(\log q)'_+\le\frac12\frac{v'}{v+m^2/216}.
$$
由 $\omega\in(1/5,216)$，积分得到
$$
\exp\!\int(\log q)'_+
\le\sqrt{\frac{v_1+m^2/216}{v_0+m^2/216}}
<\sqrt{1080}\,\frac{q_1}{q_0}
<33\frac{q_1}{q_0}.
\tag{1.3}
$$
式中第二个不等式分别使用
$v_1+m^2/216\le5q_1^2$ 和
$v_0+m^2/216\ge q_0^2/216$。
把 (1.3) 代回 (1.2)，端点因子相消成
$$
33\max(1,q_0^{-1})\max(1,q_1).
$$
由于 $q\ge m$、$q<\sqrt{919}<31$、$e^{R_b/2}<3$，结果小于
$3\cdot33\cdot31k_n=3069k_n$。

反向走时 $v$ 递减、$\omega$ 递增，直接有
$$
\exp\!\int(\log q)'_+\le\sqrt{\omega_{\rm end}/\omega_{\rm start}}<33.
$$
式 (1.2) 的两个端点因子之积至多 $31k_n$，仍得同一上界。$n=0$ 的真实传播为恒等矩阵，当然满足 (1.1)。证毕。

这个改进没有 WKB 余项、没有简单转折点假设，也包括零势端点；它只保留了原能量证明中被分别取上界而丢掉的端点相消。

## 2. 负势段的局部平均估计

**引理 2。** 在长度 $\ell$ 的区间上满足 (0.1)，设 $|V|\le V_*$、$Y=\sup|y|$。对 $n\ne0$，取 $h>0$ 满足 $2h\le\ell$。则
$$
\sup|x|
\le\left(\frac2{|n|h}+\frac{|n|V_*h}{2}\right)Y
 +\frac23\sqrt h\,\|g_1\|_2
 +\frac1{|n|\sqrt h}\,\|g_2\|_2.
\tag{2.1}
$$

**证明。** 对任意 $r$，至少可向一侧取长度 $h$ 的子区间。将 $y'=-inx+g_2$ 在该子区间积分，得到 $x$ 的区间平均至多 $2Y/(|n|h)+\|g_2\|_2/(|n|\sqrt h)$。另一方面，由 $x'=-inVy+g_1$，
$$
|x(r+t)-x(r)|\le |n|V_*|t|Y+\sqrt{|t|}\|g_1\|_2.
$$
在 $0\le|t|\le h$ 上平均此式，得到余下两项。端点值只取 $x,y$ 的实际连续代表；未取 $g$ 的端点迹。证毕。

桥取 $h=(35|n|)^{-1}$。因 $\ell_b>1/15>2/35$，该取法对全部非零整数模有效。于是
$$
X_b:=\sup|x|\le88Y_b+6F_b.
\tag{2.2}
$$
这里 $2/(|n|h)+|n|1200h/2=610/7<88$，而源的两个系数的 Euclidean 范数平方至多
$35+4/315<36$。

周期中央取 $h=(6|n|)^{-1}$。因 $\ell_c>5/12>1/3$，有
$$
X_c\le\frac{121}{10}Y_c+\frac52F_c.
\tag{2.3}
$$
确切的 $Y$ 系数是 $12+81/960<121/10$；源系数平方至多 $6+2/27<25/4$。

这一步避免了用整段 $|n|\int|V|$ 来估 $x$，并因此减少了角阶损失。

## 3. 两个单屏障模块的完整 ordinary-source 界

### 3.1 桥

由命题 1、$\sqrt{R_b}<3/2$，在右外区及中央负势段的两端，
$$
|Z|\le3100k_nE_b+4650k_nF_b.
$$
式 (0.3) 的源系数小于 $(183/80)k_n$，所以
$$
Y_b\le3100k_nE_b+4653k_nF_b.
\tag{3.1}
$$
由 (2.2)，中央的 Euclidean 范数不大于 $X_b+Y_b$；外区已有更小的界。再乘 $\sqrt{R_b}<3/2$，可统一写成
$$
\boxed{\quad
\mathcal N_b\le414000k_nE_b+622000k_nF_b.
\quad}
\tag{3.2}
$$
常数直接来自
$89\cdot3100\cdot(3/2)=413850<414000$ 和
$(89\cdot4653+6)\cdot(3/2)=621184.5<622000$。

零源时散射酉，$O_b=I_b$，而
$$
E_b\le\sqrt2\sqrt{I_b^2+O_b^2}=2I_b.
\tag{3.3}
$$
因此桥的齐次内部算子满足
$$
\mathcal N_b\le830000k_n I_b.
\tag{3.4}
$$

### 3.2 周期

原有外区 $6k_n^2$ 传播界及 $\sqrt{R_c}<5/4$ 给外区
$|Z|\le6k_n^2E_c+(15/2)k_n^2F_c$。
中央 Green 源系数小于 $(7/4)k_n$，故
$$
Y_c\le6k_n^2E_c+\frac{37}{4}k_n^2F_c.
\tag{3.5}
$$
式 (2.3) 给 $|Z|\le(131/10)Y_c+(5/2)F_c$。乘 $5/4$ 后得
$$
\boxed{\quad
\mathcal N_c\le99k_n^2E_c+155k_n^2F_c.
\quad}
\tag{3.6}
$$
因为 $\frac54\frac{131}{10}6=98.25<99$，而
$\frac54(\frac{131}{10}\frac{37}{4}+\frac52)=154.59375<155$。
零源时 (3.3) 同样成立，故
$$
\mathcal N_c\le200k_n^2I_c.
\tag{3.7}
$$

### 3.3 普通源 outgoing 的精确对偶性

**引理 3。** 对任一这样的模块或模块的真实串接，若其齐次 incoming 到内部 $L^2$ 算子范数至多 $C_n$，则零 incoming 的普通源到 outgoing 算子范数也至多 $C_n$。

**证明。** 令 $Z$ 解非齐次方程且 incoming 为零，$W$ 为任意齐次解。由 $A_n^*J+JA_n=0$，
$$
\int_0^R W^*Jg\,dr=[W^*JZ]_0^R
=\mathrm{out}(W)^*\mathrm{out}(Z).
\tag{3.8}
$$
右式的两个符号直接由 (0.2) 得到。齐次散射酉，所以令 $W$ 的 incoming 遍历单位球时，其 outgoing 也遍历单位球。用 Cauchy–Schwarz 及 $\|J\|=1$，得到
$|\mathrm{out}(Z)|\le C_n\|g\|_2$。对 $L^2$ 源，一阶解为 $H^1$，上述积分恒等式直接成立，也可由平滑源逼近证明。证毕。

由此以及线性叠加，
$$
O_c\le I_c+200k_n^2F_c,\qquad
O_b\le I_b+830000k_nF_b.
\tag{3.9}
$$
一般地，若 $O\le I+CF$，则
$$
E\le\sqrt2\sqrt{I^2+O^2}\le2I+\sqrt2CF<2I+\frac32CF.
$$
代回 (3.2)、(3.6)，得到全部普通源的内部界
$$
\boxed{\begin{aligned}
\mathcal N_c&\le200k_n^2I_c+30000k_n^4F_c,\\
\mathcal N_b&\le830000k_nI_b+520000000000k_n^2F_b.
\end{aligned}}
\tag{3.10}
$$
桥源常数的算式是
$414000\cdot1245000+622000=515430622000<520000000000$。
周期源常数的算式是 $99\cdot300+155=29855<30000$。

$n=0$ 时 $Z'=g$，由两个 incoming 直接积分，$R_c<3/2$、$R_b<21/10$ 即得远小于 (3.2)、(3.6)、(3.9)–(3.10) 的界。因此所有已显示结论包括均值。

## 4. 双屏障接线必须保留 transmission 分子

写两个模块的酉散射矩阵的交叉传输为 $t_c,t_b$，内部反射为 $r_c,r_b$，故
$$
|t_c|^2+|r_c|^2=|t_b|^2+|r_b|^2=1.
$$
对齐次外输入 $I_L,I_R$，界面变量满足
$$
v=t_c I_L+r_cu,\qquad u=r_bv+t_bI_R.
\tag{4.1}
$$
记 $I=(|I_L|^2+|I_R|^2)^{1/2}$、$\rho=|r_br_c|$、$\tau_c=|t_c|$。因为 $\tau_c>0$，$\rho<1$。消元给
$$
u=\frac{r_bt_cI_L+t_bI_R}{1-r_br_c},\qquad
v=\frac{t_cI_L+r_ct_bI_R}{1-r_br_c}.
\tag{4.2}
$$
两个分子作为 $\mathbb C^2\to\mathbb C$ 的线性泛函，范数都等于
$$
\sqrt{|r_b|^2|t_c|^2+|t_b|^2}
=\sqrt{1-\rho^2};
$$
第二个分子的对应恒等式相同。因此
$$
|u|,|v|\le\sqrt{\frac{1+\rho}{1-\rho}}\,I
\le\frac{1+|r_c|}{\tau_c}I
\le\frac2{\tau_c}I.
\tag{4.3}
$$
关键是分子保留了 $t_c,t_b$，不能先换成 $|I_L|+|I_R|$。
每个模块的 incoming 长度因而满足
$$
I_c,I_b\le\sqrt{1+4/\tau_c^2}\,I
\le\frac{\sqrt5}{\tau_c}I<\frac9{4\tau_c}I.
\tag{4.4}
$$
R75 的周期传递给
$$
\tau_c^{-1}=|D_c|\le17k_n^5e^{\alpha|n|},\qquad\alpha=459/1000.
\tag{4.5}
$$
注意：这一项只有一次 $\tau_c^{-1}$，没有 R80 粗消元中出现的 $\tau_c^{-2}$。

## 5. 同一全前缀的新全频估计

记两个模块的源合并范数为
$F=(F_c^2+F_b^2)^{1/2}$，全前缀内部范数仍为 $\mathcal N$。
逐模式有
$$
\boxed{\quad
\mathcal N_n\le32000000k_n^7e^{\alpha|n|}I_n
+400000000000000k_n^{14}e^{2\alpha|n|}F_n.
\quad}
\tag{5.1}
$$
全 outgoing 有更好的普通源估计
$$
\boxed{\quad
O_n\le I_n+32000000k_n^7e^{\alpha|n|}F_n.
\quad}
\tag{5.2}
$$

**证明齐次项。** 全内部范数至多两模块内部范数之和；由 (3.10)、(4.4)、(4.5)，
$$
\mathcal N_n\le(200k_n^2+830000k_n)\frac{153}{4}k_n^5e^{\alpha|n|}I_n.
$$
用 $k_n\ge1$ 及
$(200+830000)153/4=31755150<32000000$ 即得 (5.1) 的第一项。

**证明源项。** 令外 incoming 为零，两个模块的源 outgoing 为 $\eta^c,\eta^b$。精确界面方程为
$$
v=r_cu+\eta_R^c,\qquad u=r_bv+\eta_L^b.
$$
酉性给
$$
|1-r_br_c|^{-1}\le2\tau_c^{-2}
\le578k_n^{10}e^{2\alpha|n|}.
\tag{5.3}
$$
由 (3.9)，
$$
|r_b\eta_R^c+\eta_L^b|
\le\sqrt{200^2+830000^2}\,k_n^2F
<830001k_n^2F.
$$
因此 $|u|\le479740578k_n^{12}e^{2\alpha|n|}F$，再由 $v=r_cu+\eta_R^c$，
$$
|u|,|v|<480000000k_n^{12}e^{2\alpha|n|}F.
$$
代入 (3.10) 并合并直接源列，常数至多
$$
(200+830000)480000000+30000+520000000000
=399016000030000<400000000000000,
$$
角阶至多 $14$，故得 (5.1) 第二项。一般输入由线性叠加得到。

最后，整个前缀仍是同一 $J$-守恒一阶系统，其齐次散射酉；对全前缀直接应用引理 3 及已经证明的齐次内部界，得到 (5.2)。这一步保留了两个模块普通源经接合后的全部相消，不能用两个源 outgoing 的粗三角估计代替。证毕。

与原 R80 相比，homogeneous 内部项从 $2\cdot10^{11}k^{13}e^{.918|n|}$ 改为 $3.2\cdot10^7k^7e^{.459|n|}$；ordinary-source outgoing 从 $1.5\cdot10^{11}k^{13}e^{.918|n|}$ 改为同一个 $3.2\cdot10^7k^7e^{.459|n|}$。内部 ordinary source 仍保留 $.918$ 带损失，但常数和角阶降为 $4\cdot10^{14}k^{14}$。

## 6. 真实全 Fourier 解与物理单位

定义
$$
\|h\|_{\sigma,s}^2=\sum_{n\in\mathbb Z}e^{2\sigma|n|}k_n^{2s}|h_n|^2,
\qquad\sigma\ge0.
$$
对任意 $s\in\mathbb R$，输入满足右端有限时，(5.1) 给
$$
\max\{\|Z\|_{C_rX_\sigma^s},\|Z\|_{L^2_rX_\sigma^s}\}
\le3.2\cdot10^7\|\mathrm{in}\|_{\sigma+\alpha,s+7}
+4\cdot10^{14}\|g\|_{L^2_rX_{\sigma+2\alpha}^{s+14}}.
\tag{6.1}
$$
而 (5.2) 给
$$
\|\mathrm{out}\|_{\sigma,s}
\le\|\mathrm{in}\|_{\sigma,s}
+3.2\cdot10^7\|g\|_{L^2_rX_{\sigma+\alpha}^{s+7}}.
\tag{6.2}
$$
证明先对每个整数模解实际有限维 ODE 并接合，再取 Fourier 部分和。两个部分和之差满足相同估计、右端是输入尾，因此在 (6.1) 的两个空间中为 Cauchy 列；由方程及 $|V|<1200$，径向导数在 $L^2_rX_\sigma^{s-1}$ 收敛。接点迹相等保留，未产生接口 delta 源。逐模唯一性给唯一性。实数据的共轭对称和均值均保留。这里没有通过任意系数完备化暗中把非分布当成曲面函数。

原物理 GC 源 $f$ 与 Sturm 源的同一换算已由 R80 付清：$\|g\|_{L^2_r}<(5/4)\|f\|_{L^2_s}$；GC 变量 $U=(\beta,\pi)$ 的内部两范数至多 $540$ 倍 Sturm 范数。因此可保守写
$$
\mathcal N^U_n\le2\cdot10^{10}k_n^7e^{\alpha|n|}I_n
+3\cdot10^{17}k_n^{14}e^{2\alpha|n|}\|f_n\|_{L^2_s},
\tag{6.3}
$$
而 outgoing 的物理源项至多 $4\cdot10^7k_n^7e^{\alpha|n|}\|f_n\|_2$。端口仍是原 Sturm 端口，不能将这些数值静默套到未经换算的位置边界行。

## 7. 本题仍未完成的接口

这里的两端是明定的辅助 incoming，不是平面核心的 $x(0)=0$ 与实际非径向无限尾的 $D\mathcal T(H)$。后者存在全角模耦合，仍须建立完整线性逆、有限低模兼容、无限尾普通源控制和非线性闭合。内部源的固定角带损失尚未去掉，不能把本结果直接当作可反复使用的无损 Newton 逆。几何握持、reach 与精确等距的最终联合证明均未由本结果支付。
