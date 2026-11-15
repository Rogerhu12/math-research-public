# R133：统一割线帽行与完整 finite193 非线性接收式

2026-11-15。状态：本篇从已成功 CPA 的同一个有限扰动证明推出统一算子结论，再与 AR/CH 的真实割线恒等组合；没有新增数值运行。未知态的物理角准入、H1 cut 域、非零仿射源、high inverse 和全函数匹配仍分别保留。

引用 [CPA 实际两域](R133-supplement-actual-weighted-cap-inner-difference-and-finite193-inverse.md)、[F 完整有限反馈合同](../notes/2026-11-15-R133-selected-parameter-finite193-scalar-feedback-contract.md)、[D 的 product-space 证明](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md)、[AR 一次积分](R133-supplement-actual-cap-affine-height-and-single-integral-boundary-elimination.md)、[CH 真实 H1 chart](R133-supplement-real-H1-physical-chart-remainder-and-complete-boundary-error.md) 与 [NF 完整五输入](R133-supplement-divergence-nonlinear-core-source-and-complete-finite193-receivers.md)。

## SR1. 固定对象与一个完整 CPA case

固定同一个参数、同一个 $Q_\delta$、$\nu_\delta$、$\eta_0$，以及原 moving $\phi$、physical $\theta$ 和 Bodd/Ceven 反射规范，参数范围为
$$
 |\delta|\le10^{-10},\qquad I=[0,L],\quad L=9/10,\qquad
 \bar Q=Q_\delta(L).
 \tag{SR.1}
$$
原中心与 canonical 连续方向的定义 SHA 分别为440866a3和6a71cb81开头的完整原身份；不换成 mean-completed 的另一方向。
记 $\Pi=\Pi_{\le96}$，包括 odd96、even96 和 even mean，$H=1-\Pi$。
主体源和状态使用 normalized-circle Euclidean pair，真实径向测度为 $dr$；原正交坐标已经撤去 weighted-state 变换，没有额外 $\alpha$ 或 $\rho$。

选定 CPA.5 或 CPA.6 的一个完整 case，令 $\kappa$ 是该 case 实际有向球的上端，$g_Y,p_Y,a_Y,c_Y$ 是同一 case 的四个 transferred columns。不能混合两个 case 的 entry。三个输出是
$$
 B=L^2([0,L];L^2_\phi),\quad
 N=L^2([0,2383968743003/10^{13}];L^2_\phi),\quad
 C=L^2_\phi\text{ 的真 }L\text{ 端迹}.
 \tag{SR.2}
$$
帽差的输入是完整 $L^2_{\theta,\mathrm e,\perp}$，输出范数是
$L^2_{\theta,\mathrm o}\oplus_1\mathbb R$，最后一项为 physical Cmean。
CPA 给出的 $\kappa<1/5$ 是这个完整内端 norm-sum 的界；不是 whole-cap 无权差界。

## SR2. CPA 有限证明对所有同范数的帽增量统一

保持 AR 的固定 $S_\delta$、$J_\delta$ 和真实全输入 $H_{C,\delta}$。
对任意实有界线性算子
$$
 \mathcal K:L^2_{\theta,\mathrm e,\perp}
       \longrightarrow L^2_{\theta,\mathrm o}\oplus_1\mathbb R,
 \qquad \|\mathcal K\|\le\kappa ,
$$
定义完整边界行
$$
 \mathcal B_\delta^{\mathcal K}
 =\mathcal B_\delta^0-
          J_\delta\mathcal K P_{\perp,\theta}H_{C,\delta}.
 \tag{SR.3}
$$
这里 $H_{C,\delta}$ 作用在输入的第二分量；$\mathcal B_\delta^0$ 使用固定旧 physical $K_0$。
$\mathcal K$ 可以不是某个单一背景处的微分。
它的 scalar 输出不得再作 $P_\perp$；该投影只在 physical $\gamma$ 输入侧。

F.15--17 的坐标差只作用于固定旧 $K_0$，另一个完整帽差只使用
$$
 \|J_\delta\mathcal K P_\perp H_{C,\delta}\|
 \le c_{\rm cap}\kappa .
 \tag{SR.4}
$$
因此与旧原97行比较时，低输入与高输入分别都满足同一个已消费上界
$$
 \epsilon_L,\epsilon_H
       \le\epsilon_*+c_{\rm cap}\kappa.
 \tag{SR.5}
$$
这正是 CPA 的新第二列预算。F 的 $\epsilon_*,c_{\rm cap}$ 已由两个完整合法公式取 minimum；这里不重取某个未知算子的 entry 或真实 kernel。$H_{C,\delta}$ 的 physical 输出通常有无限 Fourier 支撑，(SR.4) 不截它。

D.11--14 的构造对 (SR.3) 原样成立：在 whole-body $L^2$ 和独立193维 cut coordinate 的 product space 上，使用实际旧 $G_0,R_0$ 重建，非负 Lipschitz 矩阵只含
$$
 M=
 \begin{pmatrix}
 g_B^{\,0}e&p_B^{\,0}\epsilon_L\\
 g_C^{\,0}e&p_C^{\,0}\epsilon_L
 \end{pmatrix}.
 \tag{SR.6}
$$
CPA 已实际支付同一上包络下的两个正 diagonal gaps 与正 determinant。
对所有 $\|\mathcal K\|\le\kappa$，同一个正加权 product norm 因而给 contraction 和真实 finite193 BVP 的唯一解。固定 cut coordinate 经原 Green 重建后就是其实际 trace；没有把 arbitrary body $L^2$ 的 trace 当成有界算子。

存在性、唯一性与每个输出的估计只用 (SR.5)，不要求 $\mathcal K$ 是一个实际微分、不要求其正性或自伴性，也不要求它随外部状态连续。
特别地，同一 CPA 四列一致给
$$
 \|u\|_Y\le
 g_Y\|F\|_{B}+p_Y\|b\|_{97}
                 +a_Y\|v_H\|_B+c_Y\|z_H\|_{L^2_\phi},
 \quad Y=B,N,C ,
 \tag{SR.7}
$$
其中 $v_H,z_H$ 是原独立 high-body/high-cut 数据。
$a_Y$ 已含 selected 主体的97--288变化，
$c_Y$ 已含完整坐标差及 (SR.4) 作用于 high cut 的那一份。
不再在右侧重复加 $c_{\rm cap}\kappa\|u(L)\|$ 或同一 high-cut 费。

本节是回读 D/F 的统一证明，不是从某一个数值逆的成功擅自推广到所有算子。原实际数值完全不变。

## SR3. 原96腰行的统一第五列

令 $\mathcal D_\delta=\partial_r-\Pi\mathcal A_\delta\Pi$、
$U=(I_{96},0)$，保持 NF.22--23 的已知中心系数及 $\ell_0$。
对 $b_0\in\mathbb R^{96}$，置
$$
 W_{b_0}(r)=(1-r/L)U^tb_0.
$$
则 $UW_{b_0}(0)=b_0$，$W_{b_0}(L)=0$，而
$\|\mathcal D_\delta W_{b_0}\|_B\le\ell_0\|b_0\|$。
由于 (SR.3) 只读真 $L$ 端值，$\mathcal B_\delta^\mathcal K W_{b_0}(L)=0$ 对每个 $\mathcal K$ 都成立。
若 $G_{\delta,\mathcal K}$ 是 (SR.2) 的 ordinary inverse，则
$$
 W_{b_0}-G_{\delta,\mathcal K}\mathcal D_\delta W_{b_0}
 \tag{SR.8}
$$
准确解 homogeneous finite body、左源 $b_0$、右源0。
因此统一第五列可取
$$
 \begin{split}
 w_B&=\sqrt{L/3}+g_B\ell_0,\\
 w_N&=\left(\int_0^{2383968743003/10^{13}}
                         (1-r/L)^2\,dr\right)^{1/2}+g_N\ell_0,\\
 w_C&=g_C\ell_0 .
 \end{split}\tag{SR.9}
$$
这里使用本篇同一 CPA case 的 $g_Y$，不把旧 $\kappa=0$ 的 $\bar w_Y$ 直接改名。
尚未对 $\ell_0,w_Y$ 运行新的数值消费。
原 Green 的真实 interfaces、virtual-waist jump 和 complete mean 仍在原逆内。
若实际态另有 value jumps，其独立原 jump 源另加，不能放进普通 $L^2dr$。

## SR4. 实际帽上的割线平均算子

取同一 selected 背景的两态
$$
 Q_h=Q_\delta+h,\qquad Q_k=Q_\delta+k,\qquad u=h-k .
$$
在真 cut，要求 CH 的实角 chart 存在，两个
$\gamma_h=P_\perp(C_{Q_h}-\widehat C)$、
$\gamma_k=P_\perp(C_{Q_k}-\widehat C)$
都进入所选 CPA case 的同一个真实 $A^0$ 球。
normalized nonmean heights $f_h,f_k$ 均在原 $\dot A^2$ 球，且 $s_B$ 固定。
这些是真实独立前提；whole $C^0$ 或 H1 半径 $2^{-10}$ 不自动支付物理 $\gamma$ 准入。

先固定 height 为 $f_k$，沿实际 physical $\gamma$ 的直线段定义
$$
 \mathcal K_{hk}
 =\int_0^1
  [D_\gamma\Gamma(\gamma_k+t(\gamma_h-\gamma_k),f_k)-K_0]\,dt .
 \tag{SR.10}
$$
原 M 图在 $A^0\times\dot A^2$ 内的一阶 Banach 微分足够定义这个积分。
对每个 $A^0$ 方向，CPA 的统一 Hilbert 界给
$\|\mathcal K_{hk}v\|\le\kappa\|v\|_2$；
再由该反射子空间的稠密性唯一延拓到完整 $L^2_{\theta,\mathrm e,\perp}$。
因此 (SR.3)--(SR.9) 适用于这个 $\mathcal K_{hk}$。

该步只沿 physical 输入空间中的真实凸线段。
不需要 moving 两态之间每个中间态都有已付的 physical $\gamma$ 范数；
也不假设 rough Hilbert 开球上的全图 $C^1$ inverse theorem、$\Gamma$ 的二阶微分，或实际 tail 的 $f(\gamma)$ 为 Lipschitz。
均值输出保持为完整标量。

## SR5. 两态准确残差式及真实 chart 余项

保持 AR 的固定
$$
 T_\delta(b,c)=(P_{\mathrm o,96}S_\delta b,\langle c\rangle_\theta),
 \qquad J_\delta(b,c_0)=(P_{\mathrm o,96}S_\delta b,c_0).
$$
记 $R_\Psi(h)=\Psi(\bar Q+h)-\Psi(\bar Q)-D\Psi(\bar Q)h$，
$\Delta R=R_\Psi(h)-R_\Psi(k)$。
则
$$
 \gamma_h-\gamma_k
 =P_{\perp,\theta}H_{C,\delta}u_2
                         +P_{\perp,\theta}\Delta R_C .
 \tag{SR.11}
$$
定义
$$
 \begin{split}
 \mathcal E_{hk}
   &=T_\delta\Delta R
       -J_\delta(K_0+\mathcal K_{hk})P_\perp\Delta R_C,\\
 \mathcal H_{hk}
   &=J_\delta[\Gamma(\gamma_h,f_h)-\Gamma(\gamma_h,f_k)] .
 \end{split}\tag{SR.12}
$$
若 $\mathcal R_\partial^f(Q)$ 是 NF.18 的固定 $S_\delta$ 残差，
完整有序代回给
$$
 \boxed{\quad
 \mathcal R_\partial^{f_h}(Q_h)
       -\mathcal R_\partial^{f_k}(Q_k)
   =\mathcal B_\delta^{\mathcal K_{hk}}u
                        +\mathcal E_{hk}-\mathcal H_{hk}.
 \quad}\tag{SR.13}
$$
这里 $K_0+\mathcal K_{hk}$ 的 scalar 输出仍然存在。
$P_\perp$ 只删除 $\gamma$ 输入的 mean，绝不删除 physical $C$ 的完整均值方程。
特别地，$T_\delta\Delta R$ 的 mean 为
$$
 \frac{\mu_h^2}{\bar m^2(\bar m+\mu_h)}
      -\frac{\mu_k^2}{\bar m^2(\bar m+\mu_k)},\qquad
 \mu_h=\langle h_2\rangle_\phi,\quad\mu_k=\langle k_2\rangle_\phi .
 \tag{SR.14}
$$
fixed $S_\delta$ 消除了另一个坐标选择会产生的 $DS_Q$ 乘非零基点 residual；并非将该 residual 假设为零。

对值情形 $k=0$，令
$r=\|h_2(L)\|_{H^1}$、$s=\|h_1(L)\|_{H^1}$、$e=\|h_2(L)\|_2$。
CH.17--18 的原计算给
$$
 \|\mathcal E_{h0}\|_{97}
 \le7rs+114re
 \le128\|h(L)\|_{H^1_\phi\oplus_2H^1_\phi}^{\,2}.
 \tag{SR.15}
$$
这里仍只要求 CH 值门 $r\le2^{-10}$；没有偷偷要求 $s$ 小。
若两态分别满足
$$
 \|h_1(L)\|_{H^1}+\|h_2(L)\|_{H^1}\le\varrho,\quad
 \|k_1(L)\|_{H^1}+\|k_2(L)\|_{H^1}\le\varrho,\quad
 \varrho\le2^{-10},
$$
则 CH.21--22 给
$$
 \boxed{\quad
 \|\mathcal E_{hk}\|_{97}
 \le2^{11}\varrho
             \|h(L)-k(L)\|_{H^1_\phi\oplus_1H^1_\phi}.
 \quad}\tag{SR.16}
$$
两处均只有 chart 余项；$c_{\rm cap}\kappa\|u(L)\|_2$ 已在 (SR.3) 左侧。

I.16 的完整 height 列沿真实凸球积分，另外给
$$
 \|\mathcal H_{hk}\|_{97}
       \le\frac7{25}\|f_h-f_k\|_{\dot H^2_\theta}.
 \tag{SR.17}
$$
这是两个已给合法 height 之间的 source 界，不是 $f(\gamma)$ 的 Lipschitz 结论。
scalar Cmean 在此列内保留。若 $s_B$ 变化，则须恢复
$\dot f_B=(\dot y_B-f_B\dot s_B)/s_B$，不适用本节 fixed-$s_B$ 简式。
meanheight、$\lambda$、span 与其他规定端口仍独立。

## SR6. 同一个状态差的五输入接收式

记两态的真实 ordinary residual 为
$$
 \sigma_h=(Q_h)_r-\mathcal F(Q_h,\nu_\delta),\qquad
 \sigma_k=(Q_k)_r-\mathcal F(Q_k,\nu_\delta).
$$
使用 NF 的完整 $\mathcal N_\delta$，准确主体式为
$$
 \mathcal D_\delta u_L
 =\Pi(\sigma_h-\sigma_k)
     +\Pi[\mathcal N_\delta(h)-\mathcal N_\delta(k)]
     +\Pi\mathcal A_\delta u_H .
 \tag{SR.18}
$$
令
$$
 \begin{split}
 F_{hk}&=\Pi(\sigma_h-\sigma_k)
                     +\Pi[\mathcal N_\delta(h)-\mathcal N_\delta(k)],\\
 b_{hk}&=\mathcal R_\partial^{f_h}(Q_h)
       -\mathcal R_\partial^{f_k}(Q_k)-\mathcal E_{hk}+\mathcal H_{hk},\\
 w_{hk}&=Uu(0).
 \end{split}
$$
由 (SR.13)，右行准确是
$\mathcal B_\delta^{\mathcal K_{hk}}u_L(L)
   =b_{hk}-\mathcal B_\delta^{\mathcal K_{hk}}u_H(L)$。
所以同一个完整状态差满足
$$
 \boxed{\quad
 \|u_L\|_Y\le
 g_Y\|F_{hk}\|_B+p_Y\|b_{hk}\|_{97}
       +a_Y\|u_H\|_B+c_Y\|u_H(L)\|_2
       +w_Y\|w_{hk}\|_{96},
 \qquad Y=B,N,C.
 \quad}\tag{SR.19}
$$
所有四个 CPA 列均属于同一 actual case，第五列由 (SR.9) 给。
这里不把 high-body 与 high-cut 认作同一 norm，也不把 left collar norm 当成右帽 norm。
两态真解且完整97行匹配时，$\sigma_h=\sigma_k=0$、两边界 residual 为0；只有这时相应项消去。
如果两态使用同一个 height，(SR.17) 的输入为0。
若还有真实 value jumps，另加原 complete jump columns。

NF.12--13 对整个真实 core 的同一半径域有效时，可估
$\Pi[\mathcal N_\delta(h)-\mathcal N_\delta(k)]$，
并由 $384$ 的投影导数费消除未知 $u_\phi$ 的 ordinary-source 要求。
该域若只在 collar 成立，就只能在那里使用，不能扩大成 (SR.19) 的全 $[0,L]$ 输入。

## SR7. 非零 selected affine 与值接收式

取 $k=0$、一个固定合法 $f_{\rm ref}$，
$b_\delta^{f_{\rm ref}}=-\mathcal R_\partial^{f_{\rm ref}}(Q_\delta)$，
$b_{0,\delta}=-UQ_\delta(0)$，
$f_\delta=(Q_\delta)_r-\mathcal F(Q_\delta,\nu_\delta)$。
对给定 $Q_h$，置
$\rho_{\partial,h}=\mathcal R_\partial^{f_h}(Q_h)$、
$\rho_{0,h}=UQ_h(0)$。
则 (SR.19) 成为
$$
 \begin{split}
 \|h_L\|_Y\le{}&
 g_Y\|-\Pi f_\delta+\Pi\sigma_h+\Pi\mathcal N_\delta(h)\|_B\\
 &+p_Y\|b_\delta^{f_{\rm ref}}+\rho_{\partial,h}
                    -\mathcal E_{h0}+\mathcal H_{h0}\|_{97}\\
 &+a_Y\|h_H\|_B+c_Y\|h_H(L)\|_2
       +w_Y\|b_{0,\delta}+\rho_{0,h}\|_{96}.
 \end{split}\tag{SR.20}
$$
这里保留同源向量相加后再取 norm 的可能性；没有凭 positive upper 进行 signed 抵消。
对真解、真97行和真腰条件，可用明确的正预算
$$
 \begin{split}
 \|h_L\|_Y\le{}&
 g_Y\{\|\Pi f_\delta\|_B+\|\Pi\mathcal N_\delta(h)\|_B\}\\
 &+p_Y\left\{\|b_\delta^{f_{\rm ref}}\|_{97}
       +128\|h(L)\|_{H^1\oplus_2H^1}^{\,2}
       +\frac7{25}\|f_h-f_{\rm ref}\|_{\dot H^2}\right\}\\
 &+a_Y\|h_H\|_B+c_Y\|h_H(L)\|_2
       +w_Y\|b_{0,\delta}\|_{96}.
 \end{split}\tag{SR.21}
$$
这比以旧 $\kappa=0$ 逆再把 $c_{\rm cap}\kappa$ 当右源的写法消去了同一线性反馈的重复费用。它没有令非零 $b_\delta$ 消失。
$f_\delta$ 必须是 R/MC 的完整 canonical selected 残差，含 raw response mean 和真实连续 offset；F.13 的额外参数 volume source 不能替它。

若选择的 affine 预算本已 uniform 于整个 $f_B$ 球，AR.19 那种完整 source 与 (SR.17) 不可为同一 height 重复收费。
(SR.21) 的写法以特定 $f_{\rm ref}$ 为基点，然后只加实际 height 差。
独立 meanheight、真实 span 和高 odd matching 均未由97行删除。

## SR8. 已推进的结论与实际剩余门

CPA 的真实有限逆现在可以统一消费每一对合法态给出的实际割线平均帽算子。
边界左侧吸收完整 bounded cap 差一次后，右侧只需真实 chart 的二次值费或 H1 差分费、非零 affine 与独立 height/waist/high 数据。
该结论不要求 $\Gamma$ 的二阶微分，也不在未知方向上使用复角或裸 composition-minus-id 小界。

$\mathcal K_{hk}$ 允许依赖这对态，故 (SR.19) 是对同一对态的统一后验接收式。仅有这条不等式不构造非线性 fixed point：
仍需同对象的 $\gamma$ 准入、CH 的 H1 cut 域、whole-core 半径及源、五输入的小量闭合和真正 high inverse。
特别地，actual tail height 的选解若只有连续性，(SR.17) 不能被改写为 $\|\gamma_h-\gamma_k\|$ 的线性费。
只完成 body 和97行，也不等于全函数匹配或最终闭曲面。

所有 CPA 实际数值、旧 F 的 $\kappa=1/5$ 失败记录和所有成功科学运行原样保留。本篇没有重做 Green、Poisson、cap、旧积分或 scalar comparison。
