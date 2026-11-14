# R133：同一连续中心的全频 moving 帽边界与 Poisson 接口

2026-11-14，visible-exact-astra-0df9。

**状态：已证明。** 在同一 continuous repaired M32 中心、固定物理
$\eta_0$、$\delta=0$ 上，把已证完整 physical 帽逆改写为 moving
角的全部边界行和完整帽延拓。任意未知高频、独立 even mean、
全部允许的源与端口均保留。下列符号预算为严格上界，但不声称
已经足够闭合完整 low/high Schur。

$L=9/10$、$R=25/8$。引用
[全频物理帽 Green](R133-supplement-actual-final-all-mode-physical-cap-Green.md)、
[连续中心共轭](R133-supplement-continuous-centre-physical-cap-and-residual-conjugation.md)
及[完整 residual Hessian](R133-supplement-local-triangular-cap-Hessian-and-trial-source.md)
的同一对象、同一实际外端图。中心定义为
440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47。
原非零参数族或今后若修改的外 connector 不自动继承本篇。

## 1. 全反射类和正确测度

角积分归一化。$\mathscr H_{\rm o}$、$\mathscr H_{\rm e}$ 分别为
全部 $4\mathbb Z$ Fourier 频率的 odd、even $L^2$ 空间，
even 空间包括独立 mean。原背景 $u$ odd、$v$ even，
$m=\langle v\rangle_\phi\ne0$，真实角图 $\Theta$ odd。记

$$
 \Theta_\phi=v/m>0,\quad Vf=f\circ\phi,\quad Ug=g\circ\Theta,
 \quad B=(u/v)\circ\phi,\quad C=(1/v)\circ\phi .
 \tag{P.1}
$$

$V$ 从 moving 角到 physical 角，$U=V^{-1}$。换元给

$$
 \|V\|\le\sqrt{J_\phi},\quad J_\phi=\|\Theta_\phi\|_\infty,
 \qquad \|U\|\le\sqrt{J_\theta},\quad
 J_\theta=\|\phi_\theta\|_\infty .
 \tag{P.2}
$$

原证书分别给 $J_\phi<1.015211829$、
$J_\theta<1.015446803$，不能互换。定义完整奇行换图

$$
 \mathcal Sg=v\,Ug,\quad
 \|\mathcal Sg\|_{L^2_\phi}^2
       =\langle mv|g|^2\rangle_\theta .
 \tag{P.3}
$$

这里 $m,v$ 同号。使用原严格界
$0<\underline m\le|m|\le\overline m$、
$0<\underline v\le|v|\le\overline v$，故

$$
 \|\mathcal S\|\le s_*:=\sqrt{\overline m\,\overline v},
 \qquad
 \|\mathcal S^{-1}\|\le(\underline m\,\underline v)^{-1/2}.
 \tag{P.4}
$$

这些是全函数算子，不是原有限 $96\times128$ 矩阵。

## 2. 准确微分、完整 even 同构和 mean

令 $I_\theta=\partial_\theta^{-1}P_{\ne0}$，保持原零均值规范。
由原 C.11，在 $r=L$ 记

$$
 H_B=-M_{BC}V-M_{B_\theta}I_\theta M_CV,\qquad
 H_C=-M_{C^2}V-M_{C_\theta}I_\theta M_CV .
 \tag{P.5}
$$

$M_a$ 表示乘法。对全部 odd/even 输入 $(h_1,u)$，
其中 $u=h_2$，准确有

$$
 (D\Psi h)_B=M_CVh_1+H_Bu,\qquad
 (D\Psi h)_C=H_Cu,\qquad \mathcal SM_CV=I .
 \tag{P.6}
$$

奇行的 $h_1$ 系数恰是恒等算子，不含截断误差。
$H_Bu$ odd，$H_Cu$ even。完整 mean 恒等式是

$$
                 \Pi_0H_Cu=-\Pi_0u/m^2 .
 \tag{P.7}
$$

直接证明：令 $f=CVu,e=I_\theta f$，则
$H_Cu=-Cf-C_\theta e$。由 $e_\theta=f-\Pi_0f$，
分部积分给 $\Pi_0H_Cu=-(\Pi_0C)(\Pi_0f)$。
换元分别给 $\Pi_0C=1/m$、$\Pi_0f=\Pi_0u/m$。
所以 moving 非mean输入的 physical $C$ mean 为0；
这没有删除帽解本身的独立 mean 输出。

$H_C$ 是整个 even $L^2$ 的有界同构。原 C.12–C.13
给其完整逆：

$$
 p_c=I_\theta(c-mC\Pi_0c),\qquad
 H_C^{-1}c=U\{-v^2(c-vC_\theta p_c)\}.
 \tag{P.8}
$$

花括号内的 $v$ 用 physical 角。这里 $c$ even、$p_c$ odd，
反射固定 primitive 的积分常数；原 inverse-angle 恒等式
$\phi=\theta+mI_\theta(C-\Pi_0C)$ 因而适用。
该反射规范不能在任意未固定角 gauge 的函数类中省略。
(P.8) 包括常数输入，不把 $h_2$ 从其导数重建。

令 $B_*,C_*,B_1,C_1$ 为原 C.4–C.8 后表的完整
$\|B\|_\infty,\|C\|_\infty,\|B_\theta\|_\infty,
\|C_\theta\|_\infty$ 上界。$\|I_\theta\|=1/4$ 给

$$
 \|H_B\|\le b_*:=\sqrt{J_\phi}(B_*C_*+B_1C_*/4),
 \qquad
 \|H_C\|\le c_*:=\sqrt{J_\phi}(C_*^2+C_1C_*/4).
 \tag{P.9}
$$

这里只乘原完整界，没有将两个独立上界相减。

## 3. 同一完整帽逆和 residual Hessian

$G$ 是原 full physical Green，已经包含全系数反馈和实际外端
Robin/mean 图。其独立 inner 输入为 $c_{\ne0}(L)$，
$c_0(L)$ 是输出。设 $\mathcal R=Q_r-F(Q)$，则

$$
 \mathcal A=G D^2\Psi[\mathcal R,D\Psi^{-1}(\,\cdot\,)],
 \qquad \|\mathcal A\|_{\mathfrak M\to\mathfrak M}
 <\chi_H:=.003840162<1 .
 \tag{P.10}
$$

$\mathfrak M$ 是先对各 Fourier 系数取径向 supremum、再取
$\ell^2$ 的两分量 $\ell^1$ 模块。原完整 Hessian 证明已将
$-e x_\theta$ 改写为 divergence 源加 ordinary 源；
(P.10) 不要求未知输入有额外角导。全部1341真格、mean项与
原端口均保留。准确 conjugation 因此给

$$
                   \widetilde G=(I-\mathcal A)^{-1}G .
 \tag{P.11}
$$

背景 $\chi_{\rm phys}$ 仅在 $G$ 中计一次，不重复支付。
取其它源/端口为0，对 $c\in\mathscr H_{\rm e,\perp,\theta}$ 定义

$$
 \mathcal Kc=\widetilde G[c_{\ne0}(L)=c],\quad
 K_Bc=(\mathcal Kc)_B(L),\quad
 K_0c=\Pi_0(\mathcal Kc)_C(L).
 \tag{P.12}
$$

原全频 inner gain 直接给

$$
 \|\mathcal Kc\|_{\mathfrak M}\le\kappa\|c\|_2,\qquad
 \|K_Bc\|_2+|K_0c|\le\kappa\|c\|_2,\qquad
 \kappa=\frac{13.316116}{1-.003840162}.
 \tag{P.13}
$$

第二式用模块的 pair $\ell^1$ 定义，包含完整 mean。
本篇保持这个由原有向界组成的准确有理表达式，不生成新小数。

## 4. 全 moving 边界行及充分必要性

将所有非 inner-$c_{\ne0}$ 的原 source/端口经 (P.11)
产生的特解记为 $g$；其 inner 非mean $C$ 迹为0。
数据保留原 source 空间与反射类。一般 physical Green 的
$B$ mean 端口在此 odd 类中由反射强制为0，不能被重新解释为
违反该类的任意输入；even mean/holonomy 端口完整保留。

令 $P_\perp=I-\Pi_0$。存在满足真实外端图和全部源、具有 moving
inner 完整迹 $(h_1,u)$ 的帽解，当且仅当

$$
 \boxed{\begin{aligned}
 h_1+\mathcal Eu&=\mathcal Sg_B(L),\\
 \mathcal Mu&=\Pi_0g_C(L),
 \end{aligned}}\quad
 \mathcal E=\mathcal S(H_B-K_BP_\perp H_C),\quad
 \mathcal M=-m^{-2}\Pi_0-K_0P_\perp H_C .
 \tag{P.14}
$$

必要性：唯一 physical 解写成
$x=\mathcal K(P_\perp H_Cu)+g$。比较其 $B$ 迹并乘
$\mathcal S$ 得第一行；比较其独立 $C$ mean 得第二行。

充分性：上述 $x$ 已有正确 nonmean $C$ 迹。第二行使完整
$C$ 迹成为 $H_Cu$，由 (P.8) 完整 moving even 迹恰为 $u$。
第一行再由 (P.6) 给正确 odd 迹 $h_1$。$G$ 与
$D\Psi^{-1}$ 的唯一性给帽解唯一。
这没有忽略 $C_0(L)$，也没有把它添加成原物理 Green 的
第五个独立端点条件。端点采用相同真实单侧迹；
state jumps 作为原 physical jump 数据另行传入。

## 5. 完整 Poisson 列及全部高输入

定义

$$
 \mathcal Pu=D\Psi^{-1}\mathcal K(P_\perp H_Cu),
 \qquad g_{\rm mov}=D\Psi^{-1}g .
 \tag{P.15}
$$

任意完整 even $u$ 都可代入。但只有 (P.14) 满足时，
$\mathcal Pu+g_{\rm mov}$ 的完整 even inner 迹才等于 $u$。
不能预先把 (P.15) 当成任意两 Dirichlet 数据的解。

原 complete reconstruction 给
$\sup_r\|D\Psi^{-1}x(r)\|_{L^2_\phi\oplus_1L^2_\phi}
<40.814490\|x\|_{\mathfrak M}$。故

$$
 \|\mathcal Pu\|_{C^0_r(L^2_\phi\oplus_1L^2_\phi)}
 \le p_*\|u\|_2,\qquad p_*:=40.814490\,\kappa c_*,
$$
$$
 \|\mathcal Pu\|_{L^2([L,R];L^2_\phi\oplus_2L^2_\phi)}
 \le\sqrt{R-L}\,p_*\|u\|_2 .
 \tag{P.16}
$$

第一行直接控制真实 $r=R$ 迹及 mean，不从第二行推出trace。
任何 moving low-head 投影 $P_L$ 也服从这些界。
因此正侧 given-head inverse 所需的帽内 $[L,R]$ head 有了
真实 Poisson 输入列，不能将该段head设零。

设 $P_H$ 为全部 $|j|\ge97$ moving even 输入，$P_L=I-P_H$。
对任意相应 odd-output/even-input 正交投影，有

$$
 \|P_{\rm out}\mathcal EP_{\rm in}\|
       \le s_*(b_*+\kappa c_*),\qquad
 \|\mathcal MP_H\|\le\kappa c_*,
$$
$$
 \|\mathcal MP_L\|\le\underline m^{-2}+\kappa c_* .
 \tag{P.17}
$$

high mean 行的界用 $\Pi_0P_H=0$ 和准确 (P.7)，没有删除
高输入通过真实帽 inverse 产生的 $K_0$ 输出。
原97输入矩阵及其全部 high 输出只是有限输入列的原认证；
它们并未变为无限 high-to-low 算子。完整帽 inverse 和
composition 能混合无限频率，不能套主体的有限带宽恒等式。
若需更小常数，须另付 $K_B,K_0$ 的实际频率/方向分辨估计。

## 6. 完整 source、mean、端口和参数列

保持原数据 norm：$e_D,B_0,e_0$ 是原 outer Robin/两 mean 输入；
$F_B,F_C$ 是 ordinary $L^2_rL^2_\theta$ 源；
$G_B,G_C$ 是 divergence 模块源；
$J_B,J_C$ 是全部真实 physical jumps 的 $L^2$ norm 之和。
对符合本篇反射类的数据，保留原完整预算

$$
 \begin{aligned}
 \mathfrak F={}&53.846164\|e_D\|_2
 +5.571744(|B_0|+|e_0|)\\
 &+12.725633\|F_B\|_{L^2}+22.179140\|F_C\|_{L^2}\\
 &+18.407084\|G_B\|_{\mathfrak M}
       +41.065564\|G_C\|_{\mathfrak M}\\
 &+53.846164J_B+88.158880J_C .
 \end{aligned}
 \tag{P.18}
$$

独立 inner nonmean $C$ 已通过 $\mathcal K$ 保留，不再塞进
定义为零 inner-$c_{\ne0}$ 的 $g$。若该原数据改变
$\epsilon_C$，完整场、奇迹和 mean 分别改变
$\mathcal K\epsilon_C,K_B\epsilon_C,K_0\epsilon_C$，费用为
$\kappa\|\epsilon_C\|_2$；若它表示真实界面 jump，完整匹配数据
同时使用该 jump，不能仍声称原相同的 even 迹。不能把任意 raw weak 源
免费视为这些空间的输入；ordinary、divergence和真实点荷按原
合同进入。odd 类强制的 $B_0=0$ 保为其实际零值，其它 even
mean 条件没有改变。

置 $q_*=\mathfrak F/(1-.003840162)$，则

$$
 \|g\|_{\mathfrak M}\le q_*,\qquad
 \|\mathcal Sg_B(L)\|_2+|\Pi_0g_C(L)|
       \le\max(s_*,1)q_*,
$$
$$
 \|g_{\rm mov}\|_{C^0_rL^2_{\rm pair}}\le40.814490q_* .
 \tag{P.19}
$$

metric/参数方向须先换成原真实 source/端口，再使用这些列。
$\nu$ bump 在帽内消失只使帽内直接 metric source 为0；
主体 incoming 迹、完整参数方向和全局 Schur 并未消失。

新增结论是完整全频接口、Poisson 列及符号预算。没有新本地
数值实验，没有重算原帽、Hessian或target。下一项仍为实际
频率交叉与主体/正负高图联立、完整无限逆及真实参数响应，
之后才可调用非线性存在与最终几何。
