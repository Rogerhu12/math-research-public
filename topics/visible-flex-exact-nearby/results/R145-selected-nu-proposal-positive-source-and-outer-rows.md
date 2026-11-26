# R145：同一 selected 成员的真实 ν-proposal 正区源与外端两行

2026-11-26，visible-exact-astra-198c63d-20261126。

**已证明。** 对原 selected 成员及同一许可外 height 背景，本篇完整支付
`q_nu = Z + z` 中修正 `z` 的正区 ordinary 源和实际外 Robin / 独立
physical mean 两行。只消费已完成的完整球及其已证公式；没有重新生产
旧积分、方向、端点、角图或 DN 常数。负区/germ/root 输入、height 荷、
完整逆和非线性存在仍须各自完成。

## 1. 对象、线性化点和符号

沿用 [N.1–N.2](R141-supplement-selected-member-and-complete-positive-Newton-source.md)
的同一 `Q_0,Z,eta_0,nu_0`，置

$$
 Q_\delta=Q_0+\delta Z,\quad \nu_\delta=\nu_0+\delta,
 \quad |\delta|\le d=10^{-10},\quad I=[r_*,R],\quad R=25/8.
 \tag{NP.1}
$$

原隐式选定参数满足 $|\delta_*|<d$，并未被换成一个半径端点。
所有 moving 源采用原归一化圆周和 ordinary $dr$；外边界采用同一个
归一化 physical 圆周。低投影保完整193维，包括 independent even mean。

记

$$
 A_\delta=D_Q\mathcal F(Q_\delta,\nu_\delta),\qquad
 s_\delta=\mathcal F_\nu(Q_\delta,\nu_\delta)
                   -(\partial_r-A_\delta)Z.
 \tag{NP.2}
$$

这是 [R.3–R.4](R133-supplement-selected-centre-complete-residual-and-collar-source-bounds.md)
的真实源；若 $q_\nu=Z+z$，则修正满足
$(\partial_r-A_\delta)z=s_\delta$。本篇的线性化点是这个明确的近似
`Q_delta`，不把它称为尚未构造的精确非线性解。

正区 $r_*>9/50$，原 metric bump 支持于 $[1/20,9/50]$。固定完整
exterior 的物理状态和同一 height 输入时，其显式 $\nu$ 导数确为零；
整个度量与坐标不变的依据是 [S.14–S.15](R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md)
及 [O.1](R141-supplement-selected-physical-outer-residual-values.md)。
但是 $Z$ 的实际状态边界导数一般非零，以下完整保留。

## 2. 同一成员 ordinary 源，无新径向积分

令 $L=9/10$。原完整7721证书已经给出 $s_0$ 在整个 $[0,R]$ 的三种
ordinary 上界。原 D 的 whole-core 证书及 R.4–R.7 另给

$$
 \|s_\delta-s_0\|_{[0,L]}
 \le (|\delta|/d)D_{\rm core},\qquad
 D_{\rm core}<4.325\cdot10^{-6}.
 \tag{NP.3}
$$

此处使用原 pointwise 正预算 $B(x)\le xB(d)/d$，然后径向平方积分；
不是对一个已保存的 residual norm 上界求导。完整 $D_{\rm core}$ 是
run 43713242980/1 中
`complete_scalar_fee_conclusions.whole_core.ordinary_L2_bounds.complete_additional_response_source`，
其完整球为

$$
[4.324390285362372026920313804384422883484124736142243558274088080\,10^{-6}
 \ \pm\ 3.29\,10^{-70}].
$$

亦可从已成 CRA 的同一正预算记录
$C_{\rm quad}\ge dD_{\rm core}/2$ 得到有向上界 $2C_{\rm quad}/d$；
该关系来自 [RF.14](R133-supplement-complete-core-residual-reuse-for-the-selected-centre.md)
的明确计算公式，不能对任意 residual upper 作这种倒推。

在 $[L,R]$ 上，原场关于 $Q$ 的三次精确式给

$$
 f_\delta=f_0-\delta s_0-\delta^2T_2-\delta^3T_3,
 \qquad s_\delta=s_0+2\delta T_2+3\delta^2T_3.
 \tag{NP.4}
$$

在 [N.14](R141-supplement-selected-member-and-complete-positive-Newton-source.md)
中，把每个非负整片预算准确分成二次项 $n_{2,j}$ 和三次项 $n_{3,j}$。
原 $e_0=dZ_0^\#$、$e_1=dZ_1^\#$ 已包含真实方向 mean，因此

$$
 \|2\delta T_2+3\delta^2T_3\|_{L^2_\phi}
 \le {2n_{2,j}+3n_{3,j}\over d}
 \le {3\over d}(n_{2,j}+n_{3,j}).
 \tag{NP.5}
$$

完整旧积分 $N^+$ 是整片平方和的上界，故

$$
 \|s_\delta-s_0\|_{[L,R]}
 \le {3N^+\over d},\qquad
 N^+<8.8\cdot10^{-16},\qquad
 {3N^+\over d}<26.4\cdot10^{-6}.
 \tag{NP.6}
$$

这里没有微分一个区间包围：微分的是准确的二/三次恒等式，再逐项使用
原正系数预算。旧 `new_outer_tail_selected_nonlinear_remainder_L2_upper`
完整球见 run 44765046846/1；其中心为
$8.7996531025025415697274419147916099434263641212463586452108588014776283612598690\,10^{-16}$，
半径 $8.40\,10^{-97}$，严格小于上述有理数。

两个径向部分先作正交直和，再与同一 $s_0$ 作三角不等式。因为

$$
 4.325^2+26.4^2=715.665625<715.669504=26.752^2,
 \tag{NP.7}
$$

得到完整的同成员源界

$$
 \boxed{\begin{aligned}
 \|s_{\delta_*}\|_{L^2(I;L^2_\phi)}&<2.9478\cdot10^{-5},\\
 \|\Pi_{96}s_{\delta_*}\|_{L^2(I;L^2_\phi)}&<2.9476\cdot10^{-5},\\
 \|P_Hs_{\delta_*}\|_{L^2(I;L^2_\phi)}&<2.8714\cdot10^{-5}.
 \end{aligned}}
 \tag{NP.8}
$$

具体分别相加的旧完整 $s_0$ 上界为
$2.725862\,10^{-6}$、$2.723698\,10^{-6}$、$1.961163\,10^{-6}$。
三个都来自同一 original whole-body source，完整 even mean 已在 low 中；
不再付第二次 mean/repair。对 $[r_*,L]$ 仅用 $[0,L]$ 的限制收缩，
没有改动真根或把两个旧上界相减。高源在 bump 外至 quarter-index288，
不把这个已知源支集外推到未知解。

## 3. 固定 physical theta 下的真实端点微分

在 $R$ 记 $Q_\delta=(u,v)$、$Z=(\xi,\zeta)$、
$m=\langle v\rangle$、$m_Z=\langle\zeta\rangle$，并写

$$
 \theta(\phi)=\phi+\mathcal I(v_\perp/m),\qquad
 B\circ\theta=u/v,\qquad C\circ\theta=1/v.
 \tag{NP.9}
$$

四重周期上 $\|\mathcal I\|_{A^0\to A^0}\le1/4$。在同一奇 lift 中

$$
 \dot\theta=\mathcal I\left({\zeta_\perp\over m}
                -{m_Zv_\perp\over m^2}\right),\qquad
 \dot\phi=-{\dot\theta\over\theta'},\qquad \theta'=v/m.
 \tag{NP.10}
$$

因此真正固定物理角的导数为

$$
 \begin{aligned}
 \dot B\circ\theta
   &=\frac{\xi}{v}-\frac{u\zeta}{v^2}
       +\left(\frac{u_\phi}{v}-\frac{uv_\phi}{v^2}\right)\dot\phi,\\
 \dot C\circ\theta
   &=-\frac{\zeta}{v^2}-\frac{v_\phi}{v^2}\dot\phi,\qquad
 \langle\dot C\rangle_\theta=-\frac{m_Z}{m^2}.
 \end{aligned}
 \tag{NP.11}
$$

在 (NP.11) 的首两式，$\dot\phi$ 是在 $\theta(\phi)$ 处的逆 lift
导数。最后一式独立来自准确恒等式
$\langle C\rangle_\theta=m^{-1}$，不是把 moving 平均与物理平均交换。
所有式都针对完整物理复合函数，包含其无限 Fourier 尾。

## 4. 已成端点球给出的有理微分界

这里只读 run 43611611635/1 的完整193方向端点、原 raw 端点和连续
repair、run 43615531666/1 的完整外图以及
[OA run 44769445246/1](R141-supplement-actual-selected-physical-outer-residual-values.md)
已复制的完整旧球。以下有理界覆盖整个 $|\delta|\le d$：

| 量 | 有理上/下界 | 原证据与转授 |
|---|---:|---|
| $|m|$ | $>29/5$ | 原 raw 与 full-delta mean 下界 |
| $|v|$ | $>5$ | $|m|-\|v_\perp\|$ |
| $\theta'$ | $>99/100$ | $1-\|v_\perp\|/|m|$ |
| $\|u\|_\infty$ | $<2\,10^{-12}$ | raw $U<1.481\,10^{-12}$ 加完整 repair 与 $dZ$ |
| $\|v_\perp\|_\infty$ | $<10^{-11}$ | raw $V<8.653\,10^{-12}$ 加完整 repair 与 $dZ$ |
| $\|u_\phi\|_\infty$ | $<1.4\,10^{-8}$ | $8U_{1/8}$ 加 degree32 repair 与 degree96 的 $dZ$ |
| $\|v_\phi\|_\infty$ | $<8\,10^{-8}$ | $8V_{1/8}$ 及同样两项 |
| $\|\xi\|_{A^0}$ | $<2.038\,10^{-11}$ | 原 exact endpoint 的完整球 |
| $\|\zeta\|_{A^0}$ | $<1.191\,10^{-10}$ | 原 `v_including_mean` 完整球 |
| $|m_Z|$ | $<1.33\,10^{-18}$ | 原准确有理 mean，未置零 |

最后的确切均值是

$$
 m_Z=-\frac{9847937731902734122348997765362540644707851006309484087203289}
 {7410693711188236507108543040556026102609279018600996098525285376506440296955904}.
 \tag{NP.12}
$$

原 raw 条带界为 $U_{1/8}<1.644\,10^{-9}$、
$V_{1/8}<9.604\,10^{-9}$。因 $|k|\le8e^{|k|/8}$，角导界可如表转授。
完整 centre repair 的 degree32 导数只付128倍，完整方向 degree96
只付384倍。使用原 $A^0$ pair repair $3.861\,10^{-18}$ 即已足够；
没有以一个仅有 $C^0$ 的任意未知量推导其导数。

将表中有理数代入 (NP.10) 得 $\|\dot\phi\|_\infty<6\,10^{-12}$。
再由 (NP.11)，逐项有

$$
 \begin{aligned}
 \|\dot B\|_\infty
 &\le {2.038\,10^{-11}\over5}
 +{(2\,10^{-12})(1.191\,10^{-10})\over25}
 +\left({1.4\,10^{-8}\over5}
       +{(2\,10^{-12})(8\,10^{-8})\over25}\right)6\,10^{-12}
 <4.1\,10^{-12},\\
 \|\dot C\|_\infty
 &\le {1.191\,10^{-10}\over25}
             +{8\,10^{-8}\over25}\,6\,10^{-12}
 <4.8\,10^{-12}.
 \end{aligned}
 \tag{NP.13}
$$

全部比较都是显示的有限有理不等式。它们不依赖重新求解外图或数值
微分。非均值物理输入 $\dot{\mathcal Z}=P_{\ne0}\dot C$ 满足
$\|\dot{\mathcal Z}\|_{L^2}\le\|\dot C\|_{L^2}$；投影在归一化
$L^2$ 下正交，不能误说其 $L^\infty$ 范数也不增。

## 5. 真正 proposal 外端 RHS

固定同一个原许可 $f_B$，原外残差函数为

$$
 \mathcal R_B(Q,f_B)=J_\theta B+Q_\theta\mathcal Z-d(\mathcal Z,f_B),
 \quad
 \mathcal R_C(Q,f_B)=m^{-1}-C_{\rm ref}-c_0(\mathcal Z,f_B).
 \tag{NP.14}
$$

若实际 $\nu$ 列采用完整物理状态，则其显式 exterior 源为零。
将 $Z$ 移到已知侧后，修正 $z$ 的真实两行恰为

$$
 r_B^Z=-D_Q\mathcal R_B(Q_\delta,f_B)Z,\qquad
 r_C^Z=-D_Q\mathcal R_C(Q_\delta,f_B)Z.
 \tag{NP.15}
$$

原真实 Hilbert 乘子范数为1，完整 $Q_\theta$ 的 $L^2$ 范数不大于1。
原 whole family DN 给

$$
 \|D_{\mathcal Z}d\|_{L^2\to L^2}<6\,10^{-6},\qquad
 \|D_{\mathcal Z}c_0\|_{L^2\to\mathbb R}<8\,10^{-7}.
 \tag{NP.16}
$$

这些在包含全部所选输入的同一真实凸球上成立；不是沿两近点的差商。
故由 (NP.13) 与完整 mean 恒等式，严格得到

$$
 \boxed{\quad
 \|r_B^Z\|_{H^{-5/6}_\theta}<9\,10^{-12},\qquad
 |r_C^Z|<4\,10^{-18}.
 \quad}
 \tag{NP.17}
$$

确切有理比较是
$4.1\,10^{-12}+(1+6\,10^{-6})4.8\,10^{-12}<9\,10^{-12}$，以及
$1.33\,10^{-18}/(29/5)^2+(8\,10^{-7})(4.8\,10^{-12})<4\,10^{-18}$。
归一化 $H^{-5/6}$ 范数不超过 $L^2$ 范数，故上述函数级界足够。

若 height 也作为独立未知变动，它的完整列仍必须加入。
本篇固定 height 的 proposal 不给实际 height/gauge 荷赋零。
原高与低两条 affine 注入路径和 endpoint 坐标中的 $\Theta$，继续按
[S.2–S.5](R141-supplement-actual-physical-source-pairs-and-reusable-bounds.md)
各付一次；(NP.17) 自身是物理源范数，尚未乘该未知坐标的权。

## 6. 关闭的义务与保留的义务

(NP.8) 和 (NP.17) 对同一个 selected 成员同时成立，关闭了原 open 中
“$\delta=0$ 的 Z 普通源不能自动用于 selected member”和
“显式 $\nu$ 源零不能替代 Z 真边界 discrepancy”这两项具体输入缺口。
本篇没有假造18项完整数据包：root even96、negative/germ/stable输入、
腰端、第四Robin、height、far label、独立接口与所有全局荷仍按原式联立。
同一 continuous Z 自身的 value jumps 为零，只限该已知对象。
完整 positive inverse、两WPN响应、true ν Schur及精确闭曲面存在性均未由
这些源上界推出。
