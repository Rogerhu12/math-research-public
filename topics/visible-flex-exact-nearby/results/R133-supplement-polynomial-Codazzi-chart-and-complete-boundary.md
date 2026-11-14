# R133：跨转向点的多项式 Codazzi 坐标、完整物理边界与余项

**已证明的是本篇的准确变换、完整线性化、频率支撑和非线性余项界。** 文末实际
谱计算与浮点 Jacobian 核验明确属于数值诊断；它们不证明整个主体存在。

在实际径向度量 $g=E(r)dr^2+a(r)^2d\theta^2$ 上，记
$\gamma=\sqrt E/a$、$\beta=a'/a$、$K=K_g(r)$。真实正交第二形式为
$\left(\begin{smallmatrix}A&B\\B&C\end{smallmatrix}\right)$。只要 $C\ne0$，令

$$
u=B/C,\qquad v=1/C.
\tag{P.1}
$$

则全部 Gauss–Codazzi 方程准确等价于

$$
\boxed{\begin{aligned}
u_r&=\gamma(uu_\theta+Kvv_\theta)-\beta u(1+u^2+Kv^2),\\
v_r&=\gamma(uv_\theta-vu_\theta)-\beta v(u^2-1+Kv^2).
\end{aligned}}
\tag{P.2}
$$

这里所有角非线性至多三次，没有 $C$ 商，也没有 $\sqrt{-K}$。$K=0$ 处没有
代数坐标奇点；这并不意味着任意 Cauchy 数据能穿过混合型转向点。

## 1. 准确推导、反向重建和 residual

原实际系统为

$$
B_r=\gamma A_\theta-2\beta B,\quad
C_r=\gamma B_\theta+\beta(A-C),\qquad A=(K+B^2)/C.
\tag{P.3}
$$

由 (P.1) 有

$$
B=u/v,\quad C=1/v,\quad A=(u^2+Kv^2)/v.
\tag{P.4}
$$

对它们求导并使用 $K_\theta=0$，所有 $v_\theta/v$ 项准确相消，得到 (P.2)。
反向地，若 (P.2) 的解满足 $v\ne0$，则 (P.4) 给 $AC-B^2=K$，同样的计算
恢复 (P.3)。本题目标确是径向；若改成 $K_\theta\ne0$ 的另一个目标，第一式
必须增加 $\gamma K_\theta v^2$，不能照搬当前公式。

对任意候选，不要求它已解方程，定义原残差

$$
R_B=B_r-\gamma A_\theta+2\beta B,\qquad
R_C=C_r-\gamma B_\theta-\beta(A-C)
$$

以及 (P.2) 的残差 $R_u,R_v$。准确恒等式是

$$
R_u=v(R_B-uR_C),\quad R_v=-v^2R_C;
\qquad
R_B=R_u/v-uR_v/v^2,\quad R_C=-R_v/v^2.
\tag{P.5}
$$

因此若 $|v|\ge d>0$，便可用 $d^{-1},d^{-2}$ 明确将新残差转换为原物理
残差。这个几何转换仍需支付分母，不能因为内部方程多项式化就将它略去。

主矩阵是

$$
\gamma\begin{pmatrix}u&Kv\\-v&u\end{pmatrix}.
\tag{P.6}
$$

在严格负曲率区，它由 $\operatorname{diag}(1,-K)$ 左乘后成为对称矩阵。
令 $k=\sqrt{-K}$，则原真实 Riemann 变量恰为 $p=u+kv,q=u-kv$；$p$ 的主
输运速度是 $\gamma q$，$q$ 的是 $\gamma p$。本篇坐标没有在 $k=0$ 除以 $k$。

## 2. 对振幅零点也正则的完整归一化

取同一实际旋转参考 $C_r<0$，置 $s=1/C_r$，按数值 continuation 的振幅 $\alpha$
写

$$
u=\alpha U,\qquad v=s+\alpha V.
\tag{P.7}
$$

旋转参考满足 $s_r=\beta s(1-Ks^2)$。将此准确项减去，再把方程展开，得到在
$\alpha=0$ 仍无除法的系统

$$
\begin{aligned}
U_r={}&\gamma[\alpha UU_\theta+K(s+\alpha V)V_\theta]
 -\beta U[1+\alpha^2U^2+K(s+\alpha V)^2],\\
V_r={}&\gamma[\alpha UV_\theta-(s+\alpha V)U_\theta]\
&+\beta[V-K(3s^2V+3\alpha sV^2+\alpha^2V^3)
 -\alpha(s+\alpha V)U^2].
\end{aligned}
\tag{P.8}
$$

它保留 $U$ 的所有 sine 模、$V$ 的 cosine 零模及全部非零模。共同反射使 $U$ 奇、
$V$ 偶，由方程保持。没有删除曲率 mean。

若原保存候选为 $B=\alpha b,C=C_r+\alpha c$，其准确坐标变换为

$$
U=b/(C_r+\alpha c),\qquad
V=-c/[C_r(C_r+\alpha c)].
\tag{P.9}
$$

有限 Fourier $b,c$ 经 (P.9) 一般会产生无限模；将其投影作为 warm start 不等于
已经解了新系统。本篇实际诊断完整打印该投影误差。

## 3. 全 Jacobian、参数列与独立 action

以 $v=s+\alpha V$ 简写。线性化 (P.8) 写成

$$
\binom{\delta U}{\delta V}_r
 =\mathsf A\binom{\delta U_\theta}{\delta V_\theta}
 +\mathsf B\binom{\delta U}{\delta V}+F_\nu\delta\nu,
$$

其中

$$
\mathsf A=\gamma\begin{pmatrix}\alpha U&Kv\\-v&\alpha U\end{pmatrix},
\tag{P.10}
$$

$$
\begin{aligned}
B_{11}&=\gamma\alpha U_\theta-\beta(1+3\alpha^2U^2+Kv^2),\\
B_{12}&=\gamma\alpha K V_\theta-2\beta\alpha K Uv,\\
B_{21}&=\gamma\alpha V_\theta-2\beta\alpha vU,\\
B_{22}&=-\gamma\alpha U_\theta+\beta(1-3Kv^2-\alpha^2U^2).
\end{aligned}
\tag{P.11}
$$

当前 compact metric 为 $E_\nu=E e^{\nu h}$，$a,\beta$ 不变，且 $h$ 仅支持于
$(.05,.18)$。由实际旋转系数的参数列计算

$$
\dot s=-\dot C_r/C_r^2,\qquad
\dot K=\dot\ell C_r^2+2\ell C_r\dot C_r,
\quad T=3s^2V+3\alpha sV^2+\alpha^2V^3.
$$

保持状态 $U,V$ 固定时，准确的全部参数列为

$$
\begin{aligned}
F_{U,\nu}={}&\dot\gamma(\alpha UU_\theta+KvV_\theta)
 +\gamma(\dot K v+K\dot s)V_\theta
 -\beta U(\dot K v^2+2Kv\dot s),\\
F_{V,\nu}={}&\dot\gamma(\alpha UV_\theta-vU_\theta)-\gamma\dot sU_\theta\\
&+\beta[-\dot K T-K(6sV+3\alpha V^2)\dot s-\alpha\dot sU^2].
\end{aligned}
\tag{P.12}
$$

源 `fourfold_codazzi_reciprocal_polynomial_system.py` 将 (P.10)–(P.12) 的完整乘法
矩阵以 Toeplitz/Hankel Fourier 公式组装，不丢低模、mean、参数列或远离对角的元素。
独立 `full_action(r,y,p)` 用完整 FFT 合成变分、真实乘法和投影，再返回 action；
它不借用已组装的 Jacobian 矩阵。

## 4. 原物理边界、mean 与振幅条件

真实归一化曲率是

$$
b=B/\alpha=U/v,\qquad c=(C-C_r)/\alpha=-C_rV/v.
\tag{P.13}
$$

因此 $U(0)=0$ 与整个腰 $B(0)=0$ 等价。原振幅行是物理 $c$ 的第四 cosine 系数
加1等于0，不能改成 $V$ 的第四系数。原选择的 mean 行也是 $c_0(R)=0$ 或
$c_0(0)=0$，不能改成 $V_0=0$。在真实周期解中，腰的转角条件另写成

$$
\left\langle\frac1{v(0,\theta)}\right\rangle=-1/a(0)
\tag{P.14}
$$

才对应一次绕行。仅 $U(0)=0$ 不给 (P.14)。用已经存在的周期帽完整匹配时，
原框架传播定理处理周期性及转角整数；这里不额外免费选择该整数。

物理边界的完整微分为

$$
\delta b=\frac{\delta U}{v}-\frac{\alpha U}{v^2}\delta V
 -\frac{U\dot s}{v^2}\delta\nu,
$$
$$
\delta c=-\frac{\delta V}{v^2}
 -\frac{\dot C_r V(2s+\alpha V)}{v^2}\delta\nu.
\tag{P.15}
$$

第二式用到了 $C_rs=1$，没有漏掉 reference 对 $\nu$ 的变化。
当前 finite probe 保留所有原物理行：全部腰 $U$、所选 mean、腰第四振幅和全部
retained 外端 $b_m+q_*c_m$。$q_*$ 仍是其明确标注的线性 regular 模型，不能
称完整 nonlinear regular 条件。物理边界中的 $1/v$ 也仍有无限角商尾，不能由
内部的三次支撑直接删去。

真正主体可在 $L_0=1.5$ 使用[通用真实周期帽图](R133-supplement-universal-small-inner-periodic-cap.md)：
取 $\zeta=(v^{-1}-C_r)_{\ne0}$，其完整右边界应为

$$
\mathcal J(u/v)+q\zeta-\mathcal N(\zeta,f_B)=0,
\qquad \langle v^{-1}-C_r\rangle-\mathcal M(\zeta,f_B)=0,
\tag{P.16}
$$

$\mathcal J$ 的 Fourier 乘子为 $i\operatorname{sgn}(m)$。已证
$\|\mathcal N\|<1.663187\cdot10^{-8}$、$|\mathcal M|<4.636375\cdot10^{-9}$，
并有真实完整导数列。这里 (P.16) 的两个函数是实际解出的全频帽图，不是当前
有限 probe 的 $q_*$ 边界。独立 $f_B$ 与远端 label 方程继续保留。

## 5. 完整频率支撑和真正二次余项

若某一有限候选的 $U,V$ 仅含 Fourier 指数 $|j|\le M$（物理频率 $4j$），则
(P.8) 的完整内部右端与 residual 仅含 $|j|\le3M$。径向系数 $K,\gamma,\beta,s$
是实际函数而不是有限多项式，但不增加角支撑。角网格严格大于 $6M$ 时，完整
有限多项式乘法可无 alias 地恢复这些系数；浮点和径向连续误差仍需分别支付。

给出独立于有限截断的全非线性预算。取任意完整 Fourier Banach 代数角范数
$A$，其权对卷积次乘；使用 pair 和范数。固定真实 $\nu$，令 $x=(u,v)$，
$h=(\xi,\eta)$，记

$$
M_0=\|u\|_A+\|v\|_A,\quad e_0=\|\xi\|_A+\|\eta\|_A,
\quad e_1=\|\xi_\theta\|_A+\|\eta_\theta\|_A,
\quad \kappa=\max(1,|K|).
$$

对于 (P.2) 的完整右端 $F$，准确二次以上余项满足

$$
\boxed{\quad
\|F(x+h)-F(x)-DF(x)h\|_A
\le\kappa\bigl[|\gamma|e_0e_1
 +|\beta|(3M_0e_0^2+e_0^3)\bigr].\quad}
\tag{P.17}
$$

证明：二次输运余项的四项是
$\xi\xi_\theta,K\eta\eta_\theta,\xi\eta_\theta,-\eta\xi_\theta$，其 pair 和
至多 $\kappa e_0e_1$。三次反应可写为 $-\beta x(u^2+Kv^2)$；减去一次展开后为

$$
-\beta\{2h(u\xi+Kv\eta)+x(\xi^2+K\eta^2)+h(\xi^2+K\eta^2)\}.
$$

逐项代数乘法分别给 $2\kappa M_0e_0^2,\kappa M_0e_0^2,\kappa e_0^3$，证明
(P.17)。这个界涵盖所有未知高模和 mean，不是有限矩阵的一项估计。

若两个修正满足 $\|h\|_0,\|\widetilde h\|_0\le r_0$、
$\|h\|_1,\|\widetilde h\|_1\le r_1$，同一余项的差还满足

$$
\kappa\left[|\gamma|(r_0\|h-\widetilde h\|_1+r_1\|h-\widetilde h\|_0)
 +|\beta|(6M_0r_0+3r_0^2)\|h-\widetilde h\|_0\right].
\tag{P.18}
$$

这里尚缺真正有限体区边界算子的全空间逆；(P.17) 不能单独替代它。若验证时
继续把 $\nu$ 当未知量，还须加它的完整二阶系数变化。也可固定已保存的准确
dyadic $\nu$、不再固定腰第四幅度，改解固定目标上的边界问题；此时仍须付该
线性算子的可逆性及最终实际幅度，不能从 augmented 数值 QR 自动推出。

分片径向候选的准确 dyadic 接口也须保留。令 $v_\pm=s+\alpha V_\pm$，则

$$
\Delta C=-\frac{\alpha\Delta V}{v_+v_-},\qquad
\Delta B=\frac{\alpha\Delta U}{v_+}
 -\frac{\alpha^2U_-\Delta V}{v_+v_-}.
\tag{P.19}
$$

因此应先在 $U,V$ 的有限支撑中支付每个准确 jump，再在真解连续后重建，不能
因为浮点 spline 被称为连续就删除这些接口点源。

## 6. 已执行的必要核验和完整谱诊断

源 `fourfold_codazzi_reciprocal_polynomial_audit.py` 在 $M=8$、8个实际径向位置、
$\alpha=0,.7,.75$ 核验全部 Jacobian、参数列和物理边界行。最终报告
`notes/2026-11-13-R133-reciprocal-polynomial-small-audit-v2.json` 中：

- 全乘法矩阵与独立 FFT action 的每径向相对差小于 $4.2\cdot10^{-16}$；
- 单独 $\nu$ 列使用各自径向尺度，误差小于 $2.4\cdot10^{-11}$，没有被外端巨大
  $\gamma$ 掩盖；
- 全物理边界差分误差小于 $7.7\cdot10^{-12}$；
- 直接由原 $B,C$ 方程转换的 RHS 与 (P.8) 差小于 $2.9\cdot10^{-15}$。

这些是必要的浮点程序检查，没有因此支付全 PDE 舍入误差。

`fourfold_codazzi_reciprocal_spectrum_probe.py` 完整读取原 $.70$ 与 $.75$ 的全部128模
及全部径向 shards，在明确保存的径向样本和4096角网格上做谱诊断。输出
`notes/2026-11-13-R133-reciprocal-spectrum-alpha070-alpha075-floating.json.gz` 保存全部
正指标 Fourier envelope、各 cutoff 尾和投影残差。主要结果为：

| 原候选 | $U$ 的 $>128$ sampled $\ell^1$ 尾 | $V$ 的 $>128$ 尾 | 原物理 B 残差 | 直接投影到新128模后的物理 B 残差 |
| --- | ---: | ---: | ---: | ---: |
| $.70$ | $6.052\cdot10^{-7}$ | $4.011\cdot10^{-6}$ | $.001292$ | $.001084$ |
| $.75$，原 finite false | $.000112892$ | $.000887891$ | $.305325$ | $.282092$ |

因此新变量没有免费消除旧大振幅尾。必须在新多项式系统中重新求实际解；把旧解
转换后仍很大的残差完整保留。优势是新有限输入的完整内部 residual 确实只到 $3M$，
而非对未付倒数尾作乐观截断。

`fourfold_codazzi_reciprocal_candidate_tools.py` 提供完整旧/新坐标 warm start 和
真实物理诊断。后者另输出所有节点及四分点的完整 $U,V$ 多项式残差、独立原物理
Gauss–Codazzi 残差、物理边界的未保留商尾、腰/外端两个 mean 和实际参数。
该接口不作径向外插，不静默降低旧保留模数，也不把投影视作 BVP 解。
