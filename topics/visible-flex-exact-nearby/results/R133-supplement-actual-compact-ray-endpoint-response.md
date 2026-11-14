# R133 续篇：真实 compact 控制的两射线端图与完整 rho5 返回响应

2026-11-14，visible-exact / newton_source。

**状态：已证明。** 固定第53、55束的当前完整非径向解、原内部标签及当前两个
$\Gamma$ 参数。本文把第60束已传播的 gauged 场送入实际物理角的两条射线，
支付全部端图和两射线返回的强导数。没有用径向原点的角平移替换真实端图。

写 $X_*=\|X\|_{\mathcal X_\beta}\le2^{-262144}$、$\beta\ge224$。
第 $j\ge8193$ 层的一个真实 compact 方向满足第59束 (C.5)，支持在第56束的
当前未占用区间 $I\subset[7/16,15/32]$；既有形状可以位于 $I$ 外。
其支集尺度为 $\rho$，并令
$$
 P_j=h_j^{-14}\delta_j^{-7/4}.
 \tag{R.1}
$$
若 $I_i$ 是一个完整 strict 负组件，定义
$$
 \mathcal N_i=
 \sum_{\operatorname{cell}(k)\cap I_i\ne\varnothing}(N_k^c)^\#,
 \qquad (N_k^c)^\#=N_k^c+\mathbf1_{k\ge130}N_{k-1}^c .
 \tag{R.2}
$$
此处最多两个求和项，保留跨胞组件的全部输入。令 $H_\pm$ 是从该组件左切口
到右切口的真正物理角流，$S_\pm=H_\pm^{-1}$，
$\mathcal R=H_-^{-1}\circ H_+$。以初始物理角为函数变量，有
$$
 \boxed{\quad
 \|D_\psi H_\pm\|_{C_*^6},\quad
 \|D_\psi S_\pm\|_{C_*^6},\quad
 \|D_\psi\mathcal R\|_{C_*^6}
 <2^{843}\mathcal N_iX_*P_j\rho^5 .
 \quad} \tag{R.3}
$$
其中 $\|f\|_{C_*^6}=\sum_{\ell=0}^6\|\partial_\theta^\ell f\|_\infty/\ell!$。
这些范数包含 mean。对非控制组件仍有由实际 $D_\psi X$ 引起的响应，并不置零。

相关实际输入为
[第59束准确通量规范](R119-supplement-actual-compact-profile-flux-gauge-and-principal-port-derivative.md)、
[第60束全标签与 gauged 场](R119-supplement-actual-compact-profile-label-response.md)、
[当前全图](R119-supplement-controlled-profile-full-label-and-raw-ports.md)、
[当前联立相位](R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md)、
[实际 strict 密度传播](R119-supplement-actual-strict-density-complete-relative-Cauchy.md)、
[原两相位补偿](R119-supplement-radial-phase-compensation-and-full-Wronskian-Hessian.md)、
[真实高振荡方向](R119-supplement-high-oscillation-polynomial-phase-preserving-control.md)和
[其完整支集/Hessian](R119-supplement-high-oscillation-small-amplitude-Hessian.md)。
以下只在它们真正支付的 strict 切口间工作；不向 type-zero 延伸 $q_0>1/16$。

## 1. 范数和真实小量

所有 Fourier 范数包含零模，并先取各模的径向上确界再求和。记
$$
 \|f\|_{\mathcal A_s^a}
   =\sum_{m\in4\mathbb Z}(1+|m|)^a e^{s|m|}|f_m|,
 \qquad
 n_i=4\mathcal N_iX_*,\quad r_i=2^{32}(j_i+4)n_i .
 \tag{R.4}
$$
第53束的 $N^c$ 已包括真实全局规范因子；这里不改回旧 $N$。
完整物理四态的宽4界，利用 $(1+M)^2e^{-2M}\le1$，给
$$
 \sup_{I_i}w^{-1}
    (\|p\|_{\mathcal A_2^2}+\|k\|_{\mathcal A_2^2})\le n_i.
 \tag{R.5}
$$
第60束 (L.2) 的两个分量及前两角导求和界特别给
$$
 \widehat n_i:=\sup_{I_i}w^{-1}
   (\|\widehat p\|_{\mathcal A_2^1}
       +\|\widehat k\|_{\mathcal A_2^1})
 <2^{832}\mathcal N_iX_*P_j\rho^5 .
 \tag{R.6}
$$
若一个组件跨两胞，逐胞取上确界再以 (R.2) 相加即可；这不交换 $\sum_m\sup_r$
与 $\sup_r\sum_m$。下面始终用 $\widehat z$，不加回第60束 (L.18) 的局部
$\rho^4$ 裸场项。

当前第53束完整和 $\sum_k(K_k^{\rm ref})^2N_k^c<2^{160016}$，
连同至多两个胞及其邻项、$K_k^{\rm ref}\ge j_i+4$，给安全界
$$
 r_i<2^{160056}X_*<2^{-32},\qquad n_i<1/64.
 \tag{R.7}
$$
实际 strict 组件满足 $|I_i|<4\delta_{j_i}<1$、$\int_{I_i}q_0\,dt<1$。
原完整角图证明按当前 $N^c$ 重实例后，在每个内部时刻也有
$\|H_\sigma-H_\sigma^0\|_{C^8}<r_i$；参考 $H_\sigma^0$ 是实际当前
径向 profile 的平移。它不是未扰 profile 的另一角图。

## 2. 消去额外背景径向导数的准确恒等式

沿用第59束的物理变量，避免将 $p_\theta$ 与 $q_0$ 混淆：
$$
 q=p_\theta,\quad K=w+k,\quad T=1-p^2,\quad E=1+w^2,
 \quad J=K+Eq,\quad D=ET-K^2,\quad z=k_\theta-p.
$$
$$
 d=Ez/J,\qquad v_*=w\sqrt D/J,\qquad
 f=\frac{w[-k-q+w(kq-p^2)]}{J},\quad
 \mathcal B=w\partial_w+f\partial_k.
 \tag{R.8}
$$
这里 $f$ 是非线性控制系数；后文的 quartic ramp 函数记为 $f_x^0$，二者不同。
在 log 半径 $t$ 中，真正完整方程是
$$
 (p,k)_t=(z,Ez^2/J)-Q(0,f),\qquad w_t=-Qw,
 \qquad q_0=\sqrt Q>0.
 \tag{R.9}
$$
先只取 $(z,Ez^2/J)$ 这一部分，记其径向导数为 $\partial_t^V$。
直接链式法则给两个完整有理恒等式
$$
 \partial_t^VD-dD_\theta=0,\qquad
 \partial_t^VJ-dJ_\theta=Jd_\theta+Ez^2/J.
 \tag{R.10}
$$
例如 $\partial_t^Vq=k_{\theta\theta}-q$，不可漏掉这一列。
由 $\log v_*=\log w+\frac12\log D-\log J$，(R.10) 准确给
$$
 \boxed{\quad
 (v_*)_t-d(v_*)_\theta+v_*d_\theta
       =-Q\mathcal Bv_*-v_*d^2/E.
 \quad} \tag{R.11}
$$
没有假设 $Q$ 为常数；它对 $\mathcal B$ 的系数在 (R.9) 中完整保留。
因此第59束 (C.24) 所含的背景径向导数可由已有状态和角导准确替换。
附带程序以七个独立 jet 变量清分母验证 (R.10) 和 (R.11)，不作数值抽样。

## 3. 真射线变分与径向参考项的准确分开

令 $g_\sigma=-d-\sigma q_0v_*$、
$\mathcal L_\sigma=\partial_t+g_\sigma\partial_\theta-(g_\sigma)_\theta$。
真正 Eulerian 角变分与修正为
$$
 \mathcal V_\sigma=\dot H_\sigma\circ S_\sigma,\qquad
 \widehat{\mathcal V}_\sigma
      =\mathcal V_\sigma-\psi\,\sigma v_*/(2q_0).
$$
代 (R.11) 入第59束 (C.23)，得到完整有源式
$$
 \mathcal L_\sigma\widehat{\mathcal V}_\sigma
       =A_\sigma[\widehat z]+F_\sigma^0-\psi G_\sigma,
 \tag{R.12}
$$
$$
 A_\sigma[\widehat z]=-D_zd[\widehat z]-\sigma q_0D_zv_*[\widehat z],
 \qquad F_\sigma^0=\frac{\sigma\psi q_{0,t}}{2q_0^2},
$$
$$
 G_\sigma=\mathcal Bd+\frac{\sigma q_0}{2}\mathcal Bv_*
 -\frac{\sigma v_*d^2}{2q_0E}
 -\frac{\sigma(v_*-1)q_{0,t}}{2q_0^2}.
 \tag{R.13}
$$
所有 $\psi_t$ 已准确消去，而真实 $q_{0,t}$ 保留。最后两项通常非零。
径向参考的 $\widehat z=0,d=0,v_*=1$，所以准确只剩 $F_\sigma^0$。

将 Banach 逆级数用于 (R.5)，有
$$
 \|J^{-1}\|<2/w,\quad\|D^{-1}\|<2,\quad
 \|v_*\|<2,\quad\|v_*-1\|<8n_i,\quad\|d\|<4n_i.
 \tag{R.14}
$$
各式在 $\mathcal A_2$ 中成立。第59束完整公式又给
$\|\mathcal Bd\|+\|\mathcal Bv_*\|<2^{10}n_i$。
写 $\chi=w^{-1}(\|\widehat p\|_{\mathcal A_2^1}
+\|\widehat k\|_{\mathcal A_2^1})$，完整变分满足
$$
 \|\delta J\|\le2w\chi,\qquad
 \|\delta D\|<3w^2\chi,\qquad
 \|D_zd[\widehat z]\|<5\chi,\qquad
 \|D_zv_*[\widehat z]\|<16\chi .
 \tag{R.15}
$$
这是由 $\delta D=-2K\widehat k-2Ep\widehat p$、
$\delta J=\widehat k+E\widehat p_\theta$、
$\delta d=E(\widehat k_\theta-\widehat p)/J-d\delta J/J$ 和
$\delta v_*=v_*(\delta D/(2D)-\delta J/J)$ 直接得出。
特别没有漏去 mean 或把 $\widehat k$ 代成某个非mean投影。
于是
$$
 \|A_\sigma[\widehat z]\|<16(1+q_0)\chi,
$$
$$
 \|G_\sigma\|\le n_i\left[
 2^{10}(1+q_0/2)+\frac1{4q_0}
                      +\frac{4|q_{0,t}|}{q_0^2}\right].
 \tag{R.16}
$$
其中 $16n_i^2/q_0\le n_i/(4q_0)$ 使用 $n_i\le1/64$，二次项没有被删去。

## 4. 原物理角的完整 variation-of-constants

固定组件左端，$H_\sigma(t_L,\xi)=\xi$。设
$$
 A_{Rt}(\xi)=
   \frac{\partial_\xi H_\sigma(t_R,\xi)}
        {\partial_\xi H_\sigma(t,\xi)}.
$$
compact 方向在两个端点及邻域为零，故 $\widehat{\mathcal V}=\mathcal V$ 于端点。
对 (R.12) 沿真实 $H_\sigma$ 积分，准确得到
$$
 \dot H_\sigma(t_R,\xi)=\int_{t_L}^{t_R} A_{Rt}(\xi)
  [A_\sigma+F_\sigma^0-\psi G_\sigma]
                      (t,H_\sigma(t,\xi))\,dt.
 \tag{R.17}
$$
实际输入角仍是 $\xi$，未把两支分别换角后相减。

$C_*^6$ 是 Banach 代数。宽2的 Fourier 界支付所需 $C_*^6$，因为
$\sum_{\ell=0}^6M^\ell/\ell!\le e^M$。
对 $\|H-\text{translation}\|_{C^8}<r_i<2^{-32}$，完整 Faà di Bruno
正系数式给 $\|u\circ H\|_{C_*^6}<2\|u\|_{C_*^6}$。
且 $\|H'-1\|_{C_*^6}<3r_i$，由逆级数
$$
 \|A_{Rt}\|_{C_*^6}<2,\qquad
 \|A_{Rt}-1\|_{C_*^6}<7r_i .
 \tag{R.18}
$$
程序对各阶 $0,\ldots,6$ 的实际正系数组合直接核查上述两个小常数。
因此 (R.15)、$|I_i|<1$ 与 $\int q_0dt<1$ 付出完整背景响应
$$
 \left\|\int A_{Rt}A_\sigma(t,H_\sigma)dt\right\|_{C_*^6}
                        <128\widehat n_i .
 \tag{R.19}
$$

在控制支集用真实 ramp 坐标
$dt=a\,dx$、$a=\eta_j/\sqrt{12}$、$B=\Delta/a>2^{190}$。
在 $x\in[7/16,15/32]$，令 $f_x^0=30x^2(1-x)^2$，则
$Q=7+Bf_x^0$，
$$
 7/4<f_x^0+7/B<2,\quad |(f_x^0)'|<2,
$$
$$
 \sqrt{7B/4}<q_0<\sqrt{2B},\quad
 |q_{0,t}|<\sqrt B/a,\quad
 |q_{0,t}|/q_0^2<1/(a\sqrt B).
 \tag{R.20}
$$
例如 $f_x^0(7/16)=59535/32768>7/4$，
$(f_x^0)'(7/16)=945/512<2$，且 $f_x^0$ 递增、导数递减。
这里两个既有 bump 及其它已选形状均离开本次未占用支集及其邻域，
所以 (R.20) 使用的是该处的准确当前 profile。
令 $W_j=a\sqrt B+B^{-1/2}$。用
$\int|\psi|dx\le2\rho^5$ 和 (R.16)，逐项积分给
$$
 \int|\psi|\,\|G_\sigma\|dt<2^{12}n_iW_j\rho^5,
 \qquad
 \int|F_\sigma^0|dt<\rho^5/\sqrt B .
 \tag{R.21}
$$
第一个式子分别支付 $1,q_0,q_0^{-1},|q_{0,t}|/q_0^2$；不是在整个
strict 组件上用一个不适用的支集估计。

径向参考的端角响应准确为
$$
 \dot H_\sigma^0(t_R)
 =\int F_\sigma^0dt
 =\frac\sigma2\int\psi_t/q_0\,dt
 =\frac\sigma2D\Theta[\psi].
 \tag{R.22}
$$
分部积分边项由真实 compact 支集为零。对本方向，两原相位导数在当前
径向 profile 准确为零；不将这一原点消去推广为整条非零新参数区间上的
恒等零，也不将其用于非径向 $\Gamma^*$ 列。
将 (R.18)–(R.22) 代 (R.17)，得到完整实际单射线差
$$
 E_i:=\|\dot H_\sigma-\dot H_\sigma^0\|_{C_*^6}
 <128\widehat n_i+
              (2^{14}n_iW_j+7r_i/\sqrt B)\rho^5 .
 \tag{R.23}
$$
特别实际 $\dot H_\sigma$ 的 mean 不是由 (R.22) 删除的。

## 5. 真返回、逆图及其所有导数

取真实逆图 $S_-=H_-^{-1}$，准确链式法则为
$$
 \dot{\mathcal R}
 =\frac{\dot H_+-\dot H_-\circ\mathcal R}
                   {H_-'\circ\mathcal R}.
 \tag{R.24}
$$
小量逆图常数也可以有限有理地完整支付。对 $r_*=2^{-32}$，以正系数
majorant $b(t)=\sum_{n=1}^8b_nt^n$，取
$$
 b_1=(1-r_*)^{-1},\qquad
 b_n=\frac{r_*}{1-r_*}
 \sum_{\ell=2}^n[t^n]
          \left(\sum_{k<n}b_kt^k\right)^\ell/\ell! .
 \tag{R.25}
$$
真实逆函数微分公式给 $n!b_n$ 为各阶导数上界。程序完整核查
$b_1-1<2r_*$、$n!b_n<2r_*$ ($2\le n\le8$)。这些正系数比值在 $r$ 上
单调，故同一结论对实际 $r_i\le r_*$ 成立。零阶逆图误差由
$S(x)=x-c-e(S(x))$ 直接小于 $r_i$。
因此
$$
 \|\mathcal R-\mathcal R^0\|_{C_*^6}<15r_i,
 \quad\|u\circ\mathcal R\|_{C_*^6}<2\|u\|_{C_*^6},
$$
$$
 \|(H_-'\circ\mathcal R)^{-1}\|_{C_*^6}<2,
 \quad\|(H_-'\circ\mathcal R)^{-1}-1\|_{C_*^6}<7r_i .
 \tag{R.26}
$$
若不先假设 $D\Theta[\psi]=0$，(R.23)–(R.26) 仍给
$$
 \|\dot{\mathcal R}-D\Theta[\psi]\|_{C_*^6}
                    <6E_i+7r_i|D\Theta[\psi]| .
 \tag{R.27}
$$
故对实际相位 annihilator，得到
$$
 \|\dot{\mathcal R}\|_{C_*^6}
 <2^{10}\widehat n_i+
       (2^{17}n_iW_j+64r_i/\sqrt B)\rho^5 .
 \tag{R.28}
$$
$\dot S=-(\dot H/H')\circ S$ 以相同 Banach 逆和 composition 给
$\|\dot S\|_{C_*^6}<4\|\dot H\|_{C_*^6}$；没有逆图误差尚未支付的列。

## 6. 实际第60束的完整消费

在当前整 $[7/16,15/32]$ 上仍有 $Q>B$，而其长度为 $1/32$。
由 $\int q_0dt<1$ 得 $a\sqrt B<32$；加 $B^{-1/2}<1$，有 $W_j<33$。
又 $h_j<1$、$P_j>\delta_j^{-1}>j+5$。若 $I_i$ 与本方向支集相交，
其编号满足 $j_i+4\le j+5$。故 (R.4)、(R.28) 的显式 compact 部分小于
$$
 2^{41}\mathcal N_iX_*P_j\rho^5.
$$
(R.6) 的完整响应部分小于
$2^{842}\mathcal N_iX_*P_j\rho^5$，两者严格小于 (R.3) 的 $2^{843}$。
非控制组件只有第一部分。
单射线的 (R.23) 给 $2^{840}\mathcal N_iX_*P_j\rho^5$，
其逆图再乘4也在 $2^{843}$ 内。因此 (R.3) 同时包含两射线、两逆图和真返回。

有限方向 $\sum_\nu c_\nu\psi_\nu$ 用
$\sum_\nu|c_\nu|P_{j_\nu}\rho_\nu^5$ 代替单一 $P_j\rho^5$。
若该加权和有限并且参数仍在原真实 $C^4$ 球内，Bochner 极限及第60束的
全频可微性给相同无限方向结论。没有将这个加和免费换成任意
$\ell^\infty$ norm，也没有漏掉方向个数。

## 7. 完整 angular operator 的合法强导数

取 $C_Su=u\circ S$、$D_Hu=H'(u\circ H)$，二者为完整物理角上的算子。
准确有
$$
 \dot C_S=-\mathcal V\,\partial_\theta C_S,\qquad
 \dot D_H=D_H\partial_\theta M_{\mathcal V},
 \qquad\mathcal V=\dot H\circ S .
 \tag{R.29}
$$
它们是强导数；没有声称裸 pullback 在同阶 Sobolev 上范数可微。
对 $s=0,1$，完整 product/chain 规则由 $C_*^6$ 界给
$H^{s+1}\to H^s$；负阶由 $D_H=C_S^*$ 的对偶式，之间由插值。
以安全总常数 $2^{10}$ 支付 composition、Jacobian、各一次导数与对偶转换，
由 (R.3) 得对 $-1\le s\le1$
$$
 \|\dot C_S\|_{H^{s+1}\to H^s},\quad
 \|\dot D_H\|_{H^{s+1}\to H^s}
 <2^{853}\mathcal N_iX_*P_j\rho^5 .
 \tag{R.30}
$$
完整输入频带 $M\le|m|\le2M$ 因而至多再付 $1+2M$。
输出始终是全部 Fourier，不以投影删掉频带外响应；mean 亦保留。

## 8. 仍保留的物理行、mean 和两个全局参数列

本偏导固定当前 $\Gamma$。在真实联立图上，准确总导数仍为
$$
 D_\Omega^{\rm total}\mathcal R
 =\partial_\Omega\mathcal R\big|_\Gamma
 +(D_\Omega\Gamma_1^*)\partial_{\Gamma_1}\mathcal R
 +(D_\Omega\Gamma_2^*)\partial_{\Gamma_2}\mathcal R .
 \tag{R.31}
$$
两个 bump 列和其真实无限联立导数并未由径向 annihilator 消失。
同当前 $\Gamma$ 的参考也须按同样规则微分。

真实物理端口仍为第59束 (C.28)
$$
 (u,\pi)=
 (\Lambda^{-1/2}w_{\rm Jac},\sqrt\Lambda\,\zeta
                         -T_\ell\Lambda^{-1/2}w_{\rm Jac}).
 \tag{R.32}
$$
本文支付其中真实 angular map 的全部强微分。$\Lambda,T_\ell$ 的变化、
fixed-label kernel、跨支 order0 项与全部 current-$\Gamma$ 列仍需在完整
physical 散射公式中消费，不能把 (R.30) 当成全网络同阶相对导数。

背景的真实 holonomy 行始终是
$\langle D_z\mathfrak m[\widehat z]\rangle=0$；它不令
$\widehat k_0$ 或端角变分的 mean 为零。独立高度仍按
$\dot\lambda+\int(\widehat k_0+\psi f_0)dr$ 积分，实际参考高度另保
$-\int w\psi\,da$。Jacobi 的两个独立 mean 仍在其完整 height/flux 端口内。
第60束 (L.21)–(L.22) 的两个 weak 源、total/bare 端荷以及普通源单位变化
也原样保留：任意径向 $L^1$ 源不能因本结果免费多得一个 $\rho$。

本文解决实际非径向 principal 端角相对于同当前径向参考的响应，
不声称完整 $\mathcal F=0$、中频网络或最终闭曲面已经闭合。
下一步在这些准确端图上支付密度/shear、全 kernel 与两个全局参数响应。

[精确代数及有理预算程序](../scripts/fourfold_actual_compact_ray_endpoint_response.py)
与[实际执行报告](../notes/2026-11-14-R133-actual-compact-ray-endpoint-rational.json)
保留全部输入身份。恢复前的临时函数存储已经失效；本篇报告在恢复后的实际
Python 运行中重新生成，不冒称找回旧临时执行字节。
