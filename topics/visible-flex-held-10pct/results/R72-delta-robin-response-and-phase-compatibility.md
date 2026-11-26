# R72. δ 设计的精确端口响应、相位吸收条件与 mean 标量

维护：Astra-held10-06bbeb39-20261126。2026-11-26 UTC。

本条区分两个问题：核心入口切向量能否用 v4 phase 表示，以及改变物理 profile 的 δ 方向能否由固定 g 的核心变化补偿其端口响应。前者有 R71 的小 λ 结论；后者还涉及整个径向方程。本条给出原 multistage 线性 m 模的精确 δ 响应积分、完整桥项，以及一般有限 BVP 中必须检验的伴随标量。

**没有证明当前有限幅场存在兼容障碍，也没有证明新的变量选择使完整 BVP 可逆。** 以下共振结论明确属于指定的旋转背景线性模型；当前实际场是否接近它、所给积分是否非零，均未由本条测量。

## 1. 本模型 δ 改哪里，桥为什么可以固定

原 `multistage_flat_profile.py` 的定义为

$$
r=\delta/\delta_{\rm ref},\qquad
s=r\xi,\qquad a_\delta(r\xi)=1+r h(\xi),\qquad
v(\xi)=h'(\xi),\qquad 0\le\xi\le L_{\rm ref}.
\tag{1}
$$

原参考 up/down 两段的精确面积分别为 $+\delta_{\rm ref}$ 和 $-\delta_{\rm ref}$，末速度均为零。因此

$$
h(0)=h(L_{\rm ref})=0,\qquad v(0)=v(L_{\rm ref})=0,
\qquad a_\delta(0)=a_\delta(rL_{\rm ref})=1.
$$

实际 prefix 末端半径不随 δ 改变；它的物理 s 位置随 δ 移动。当前 `prefix_bridge` 仅含 `kind=turn_plateau_v1, curvature=4, peak_fraction=.2`。`ShortBridge` 构造只依赖固定 cut、起始半径1及这两个参数，其桥长和局部 profile 不含 δ。把桥写在自己的局部弧长 $u=s-rL_{\rm ref}$ 中后，整个桥方程与 δ 无关。不能仅凭 cut 的 R/E 固定就作这个判断；这里还用了**精确径向返回1及桥构造的全部输入固定**。

来源定位：multistage provider 第60–70行核精确面积返回，第93–107行定义缩放与桥的物理平移，第115–138行给 profile；`root_short_bridge.py` 第19–35行给桥全部依赖，第80–85行显示默认起始半径1的 dispatch。

δ 也不只是坐标改变。对边界保持标记的完整 warped metric，在这个前缀—桥带内，核心到 cut 的内蕴最短距离为
$rL_{\rm ref}+L_b$：任意连接路径长度至少为其 s 总变化，常角子午线达到这个值。因此其 δ 导数为 $L_{\rm ref}/\delta_{\rm ref}>0$。固定 g 的 phase 变化不能产生同一个完整度量切向量。下文所说“吸收”仅指补偿其**边界残差响应**，不把变 g 的设计方向改名为等距方向。

## 2. 原线性 m 模、完整桥转移与通式

原 `fixed_metric_mode3_flow.py` 第72–79行的线性系统，写 $b=\sqrt{1-v^2}>0$：

$$
\frac{dX}{ds}=\frac1a M_m(v)X,\qquad
M_m(v)=
\begin{pmatrix}
 -(m^2-1)v&-m^2b\\
 (m^2-1)v^2/b&m^2v
\end{pmatrix},\qquad X=\binom fg.
\tag{2}
$$

在固定参考前缀区间，式 (1) 给

$$
X_\xi=A_m(\xi,\delta)X,
\qquad A_m=\frac{r}{1+rh}M_m(v),
\qquad
\boxed{\partial_\delta A_m=\frac{M_m(v)}{\delta_{\rm ref}(1+rh)^2}.}
\tag{3}
$$

记前缀转移矩阵为 $P_m(\delta)$，桥的完整转移矩阵为 $B_m(\delta)$，cut 的 Robin 行为 $\ell_m(\delta)$。单位平面入口为 $e_1=(1,0)^T$。定义完整线性边界响应

$$
\mathscr R_m(\delta)=\ell_m(\delta) B_m(\delta)P_m(\delta)e_1.
$$

无论桥是否变化，正确导数首先是

$$
\boxed{\mathscr R_m'=
 (\ell_m'B_m+\ell_m B_m')P_me_1
 +\ell_m B_m P_m'e_1.}
\tag{4}
$$

若桥长 $L_b$ 变化，可在固定 $\tau\in[0,1]$ 上写
$\widetilde A_b(\tau,\delta)=L_b A_b(L_b\tau,\delta)$，并用

$$
B_m'=\int_0^1 B_m(1,\tau)
       \partial_\delta\widetilde A_b(\tau,\delta)
       B_m(\tau,0)\,d\tau.
$$

其中 $\partial_\delta\widetilde A_b$ 包含桥长、局部 profile 及其移动参数的全部链式项。若直接用变化的物理上端点，应保留相应的 $A_b(L_b)B_mL_b'$ 项。若 cut/尾改变，$\ell_m'$ 也不能省略。

**当前第1节的模型才有 $B_m'=0$、$\ell_m'=0$。** 移动的 prefix_end 已由固定 ξ 前缀和桥局部 u 两个区间处理；桥只整体平移其物理起点，没有漏掉一个改变桥内传播时间的项。原数值 radial chart 只是这两个物理区间的另一个参数化，不能重复加入一次移动端点贡献。

## 3. 共振时的精确 δ 标量

以下固定 m，省略下标。令
$X(\xi)=P(\xi,0)e_1$，$X_{\rm cut}=B X(L_{\rm ref})$。把固定 Robin 行归一化为

$$
\ell=(1,-C),\qquad
C=\sigma w_{\rm cut}\frac{R_{\rm cut}D_m-m^2}{m^2-1}
$$

时，其核为 $(C,1)^T$；这是原 `linear_terminal` 使用的物理线性端口方向。若使用一个不同的固定行归一化，以下响应整体乘同一个常数即可。

假设线性响应恰为零，即 $\mathscr R=0$。则

$$
X_{\rm cut}=\gamma(C,1)^T,\qquad \gamma\ne0.
$$

非零性由两个转移矩阵可逆和非零入口保证，亦是已登记高度响应结论的条件。设

$$
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad
\Delta_b=\det B>0.
$$

前缀的 $\operatorname{tr}A=rv/a=a_\xi/a$，且首末 a 均为1。因此
$\det P(L_{\rm ref},\xi)=1/a(\xi)$。利用任意二阶矩阵的恒等式
$U^TJU=(\det U)J$ 及 $X_{\rm cut}^TJ=\gamma\ell$，得到回传的伴随行

$$
\ell B P(L_{\rm ref},\xi)
=\frac{\Delta_b}{\gamma a(\xi)}X(\xi)^TJ.
\tag{5}
$$

参数变分公式与式 (3) 遂给出

$$
\boxed{\quad
\mathscr R_m'(\delta)
=\frac{\Delta_{b,m}}{\delta_{\rm ref}\gamma_m}
  \int_0^{L_{\rm ref}}
   \frac{X_m(\xi)^T J M_m(v(\xi))X_m(\xi)}{a(\xi)^3}\,d\xi.
\quad}
\tag{6}
$$

**桥没有被丢掉。** $X_{\rm cut}$、$\gamma_m$、Robin 行和 $\Delta_{b,m}$ 都含完整固定桥的转移。若桥是与同一真 profile 一致的连续系统，$a_b'=v_b$、$a_b(0)=1$、$a_b(L_b)=R_{\rm cut}$，才可再化简 $\Delta_{b,m}=R_{\rm cut}$。若使用原 GL64 查询器的 $\hat a_b$ 与另给的 $v_b$，本条保留

$$
\Delta_{b,m}=
 \exp\!\left(\int_0^{L_b}\frac{v_b(u)}{\hat a_b(u)}\,du\right),
$$

不把其与真原函数的差设为零。式 (6) 的简单 $a^{-3}$ 权重使用了前缀真 profile 的 $a_\xi=rv$；任一不一致的数值前缀评价也须回到一般变分式 (4)，或先支付其转移误差。本条没有给浮点积分值认证。

积分没有自动符号。写 $X=(x,y)^T$：

$$
X^TJM_mX=-\left\{
 \frac{(m^2-1)v^2}{b}x^2+(2m^2-1)vxy+m^2by^2\right\}.
\tag{7}
$$

括号内二次型的对称矩阵行列式为 $-v^2/4$；v 非零时它不定。因此不能从式 (6) 直接宣布 $\mathscr R_m'\ne0$，更不能由“linear-root”文件名把当前有限幅场当作已认证的简单共振。

## 4. 为什么入口列好，仍不保证吸收 δ 响应

在式 (2) 的旋转背景线性模型中，任一平面核心变化在 m 模入口为 $(a_m,0)$，边界残差为

$$
r_m=a_m\mathscr R_m(\delta).
$$

在 $\mathscr R_m=0$ 的共振点，任何固定 δ 的平面入口振幅变化均满足

$$
\partial_{a_m}r_m=0,
$$

而 profile 变化给

$$
\partial_\delta r_m=a_m\mathscr R_m'(\delta).
\tag{8}
$$

所以只要 $a_m\ne0$ 且式 (6) 的积分非零，选择第 m 个 Robin 残差的标量泛函就**消掉全部平面核心入口方向，却不消掉 δ 方向**。其它角模在线性模型中解耦，增加更多入口 phase 列也不能绕过这个特定标量。

这是一个明确的条件横截机制，不是维数计数。它说明“完整入口空间更丰富”并不蕴含“δ 方向一定可吸收”。但它也不证明当前非圆有限幅 BVP 有该泛函：非线性模态耦合可能使原来零的核心响应非零；即使非零，也可能很小。R70/R71 的核心列下界与这种径向端口弱响应完全相容。

## 5. 有限幅 BVP 要检验的精确伴随量

在共同固定计算区间 t 上写实际有限方程

$$
Y'=f(t,Y,d,\lambda,\delta),\qquad
Y(0)=I(d,\lambda,\delta),\qquad
T(Y(1),d,\lambda,\delta)=0.
$$

这里 f 必须包括原材料 chart 对流和完整 exact-lift；不能只拿入口 Fourier 投影代替它。相位 d 采用物理系数单位；δ 是原 profile 的参数，不能把 warm p0 的 log(q_aux/q_g) 当 δ。

令 $A=f_Y$、$B=T_Y$。对任意实际端口行向量 $w\in\mathbb R^M$，解有限维伴随方程

$$
-\psi'=A^T\psi,\qquad \psi(1)=B^Tw.
$$

对每个参数 $\tau\in\{d_1,\ldots,d_M,\lambda,\delta\}$ 定义

$$
\boxed{\beta_\tau(w)=w^TT_\tau+\psi(0)^TI_\tau
            +\int_0^1\psi(t)^Tf_\tau(t)\,dt.}
\tag{9}
$$

对一条真正的精确解分支，将线性化方程与 ψ 配对并分部积分，得到必要等式

$$
\sum_j\beta_{d_j}(w)\dot d_j+\beta_\lambda(w)\dot\lambda
          +\beta_\delta(w)\dot\delta=0.
\tag{10}
$$

这也是消去全部场后的端口响应的对偶表示。若 $\beta_{d_j}(w)=0$ 对全部 j 成立而 $\beta_\delta(w)\ne0$，δ 的该端口方向不在 phase 响应值域。若要固定 δ 继续 λ，则障碍条件换成 $\beta_\lambda(w)\ne0$。反之，只有所有左零泛函都消掉目标方向，才能断言相应的**有限线性方程**相容；存在性和可用逆界仍未由此得到。

对近零方向，仍有精确的控制代价下界。例如固定 λ、要求 phase 补偿单位 δ 响应，则

$$
\|\dot d\|_1\ge
\frac{|\beta_\delta(w)|}{\max_j|\beta_{d_j}(w)|}
$$

（分母为零时按上段讨论）。这给一个具体需要实测的标量比值；本条没有给它补造数值。它在 phase 的物理单位下使用，不能用未经说明的旧 support 缩放比较。

实际 accepted raw 仍有有限残差。若 $e=Y'-f$、$r_0=Y(0)-I$、$r_T=T$，Newton 方程右端的对应等式是

$$
\sum_\tau\beta_\tau(w)\Delta\tau
=-w^Tr_T+\psi(0)^Tr_0+\int_0^1\psi^Te\,dt.
\tag{11}
$$

因此不能把原 RMS 小直接当 RHS 为零。实际 collocation 应使用它的同点离散 Jacobian/残差及已登记的 Schur 消元，而非把连续积分近似伪装成精确离散等价。本条没有重新证明旧 Schur 引理；式 (9) 指明的是这次 δ/phase 比较中应保留的完整物理项。

## 6. mean 径向标量没有提供另一个独立的端口行

本节仅将 [R14](R14-mean-slope-from-turning-and-darboux.md) 的已证转角公式微分，不重新证明其接缝定理。假设其完整 exact-g、闭合和同符号分支条件成立，固定 cut 的 R/E。用连续角均值记

$$
p=c_0+\eta,\quad \langle\eta\rangle=0,\quad
v=\zeta_\theta,\quad a=\zeta_{\theta\theta},\quad
G=R^2-v^2,\quad D=EG-R^2p^2,
$$

$$
\omega=\frac{\epsilon R}{\sqrt D}\left(1+\frac{Rpa}{G}\right),
\qquad\langle\omega\rangle=n.
$$

其四个所需偏导为

$$
\omega_p=\frac{\epsilon R^2(Ea+Rp)}{D^{3/2}},\quad
\omega_a=\frac{\epsilon R^2p}{G\sqrt D},\quad
\omega_E=-\frac{\epsilon R(G+Rpa)}{2D^{3/2}},
$$

$$
\omega_v=\frac{\epsilon Rv}{D^{3/2}}
 \left\{\frac{2RpaD}{G^2}+E\left(1+\frac{Rpa}{G}\right)\right\}.
$$

令 $\mu=\langle\omega_p\rangle\ne0$；非零性正来自 R14 的同符号 Q 条件。对保持 turning number 的变化，

$$
\boxed{\dot c_0=-\frac{
\langle\omega_p\dot\eta+\omega_v\dot\zeta_\theta+
                  \omega_a\dot\zeta_{\theta\theta}\rangle
 +\dot E\langle\omega_E\rangle}{\mu}.}
\tag{12}
$$

当前 δ 与 phase 都保持同一个物理 cut R/E，故两者均有 $\dot E=0$。当其完整高度/非均值斜率响应相同时，平均径向斜率响应也相同；不能把平均斜率再加成一条独立的第 M+1 条兼容障碍。

在圆端，$\zeta$ 常数、$p=w\ne0$、$E=1+w^2$、$\epsilon=1$，有
$\omega_p=w,\omega_a=w/R,\omega_v=0,\omega_E=-1/2$，所以
$\dot c_0=\dot E/(2w)=0$。水平角度量的一阶式给 $f+g_\theta=0$，故平均径向位置扰动也为零；这两项对固定 cut 的 δ 和 phase 一视同仁。

这里的均值是连续角均值。当前 mean1168 是1168个字面 binary64 ψ 点的原 Vz 均值，不能与连续均值字面互换。尚未精确等距的实际图，其 metric/turning/离散 mean 到连续 mean 的差仍须同场审计，式 (12) 不自动消除这些残差。

## 7. 用 δ 替换第一 phase 方向：何时是有效的变量选择

可考虑新的设计未知 $(\delta,d_2,\ldots,d_M)$，固定 $d_1=0$。其入口仍为完整原锚加 R70 列；零控制时核心和两jet不变，λ1仍保准确保护弧。δ 在这条路上明确改变 g，不能标成 fixed-metric refinement。

在完整有限幅问题中，保留高模原 DN 后消去场和其余控制，若所选补块 K 可逆，旧 Schur 公式给两个不同的最后标量：$s_1$ 是第一 phase 的响应，$s_\delta$ 是 δ 的响应。用 δ 替换第一列可用的条件是 $s_\delta\ne0$，并且实际逆及步长仍满足原域门；不是只因未知数同为 M 就可用。

在第2–4节的旋转背景线性模型中，可以更具体地说明这个选择的动机。若只有主模 m=3 共振，其余保留模的 $\mathscr R_m\ne0$，则第一端口行消掉全部 phase 列。单位材料圆的曲率系数 $k_m$ 与入口径向振幅满足 $a_m=k_m/(m^2-1)$。R71 对 $J=\{2,\ldots,M\}$ 的同模投影下界，使高模 phase 到高模入口曲率的有限矩阵在小 λ 区间可逆；再乘非零的 $\mathscr R_m/(m^2-1)$，高模端口块仍可逆。若同时 $a_3\mathscr R_3'\ne0$，新的 δ 列在主模端口行非零，从而这个**线性模态模型**的替换矩阵可逆。

这项条件论证支持“用 δ 替换近共振的首相位振幅方向”作为实际设计选择，但没有证明当前非圆场的补块 K、$s_\delta$ 或全 BVP 可逆，也没有证明 λ 变化的 forcing 可被安全步长抵消。原 δ 设计继续求真实接受场，v4 继续原固定 g 求解，两者目前均不因本条被判定成功或失败。

若从 M32 等原设计锚引入该新族，必须保留源自己的完整 mean 规则（例如原 M32 的1552），不能套用现有 warm 的1168身份声称同图。只有新的真实 λ1 场及真实尾通过后，才可冻结其最终 δ，再按同一完整 phase 族做固定问题精化。

## 源码绑定与本条范围

| 源 | SHA-256 | 关键位置 |
|---|---|---|
| `scripts/resume_m3/multistage_flat_profile.py` | `887a8d04157dfcee504f80d8cc2e7b66d9ae430775b4bc1df0bfea70bd49ceed` | 精确面积60–70；δ缩放93–107；profile115–138 |
| 恢复源 `notes/fixed_metric_mode3_flow.py` | `0e5555fa23609e2e7154f0e952c6b7ddc402a4cf54be148842f36db886103dc5` | 物理桥66–70；线性系统与端口72–79 |
| 恢复源 `notes/fixed_metric_mode3_bvp.py` | `e2e5cf08339c82fac24ef296dc721cec4e43852d2a6d963721ce69a1d8d7a11c` | δ/核心55–83；chart85–103；terminal118–132 |
| 恢复源 `computations/root_short_bridge.py` | `7e00a3336a302ba94c751c09e6f75749d6973c86605269538c8f0b44c60779b4` | 完整桥构造19–35；线性55–64；dispatch80–85 |
| `scripts/resume_m3/round_raw_lib/exact_core_lift.py` | `28936553078df9d1a2c6486fab1613c20fd7cfdb9b4134d4c95e1d60fa5623f5` | 完整 lift11–28；入口/方程31–53 |
| `scripts/resume_m3/round_raw_lib/analytic_adaptive_core_jac.py` | `da6690d9f11eac38cec0acee31aa07555a8d1ddd81c1b24997db0421ea19e431` | 完整参数链14–24；δ列25–26 |

actual_tail 已独立核式 (3)、(5)、(6) 的符号、行列式权重及式 (7) 的不定性；seam_geometry 核了式 (12) 的连续均值适用范围。没有运行新的 BVP、伴随求解、线性响应积分或有限幅 Schur 诊断。本条全部未实测标量保持未实测，不由当前 Newton 失败反推几何不存在。
