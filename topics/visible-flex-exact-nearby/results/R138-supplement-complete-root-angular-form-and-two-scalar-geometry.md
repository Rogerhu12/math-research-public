# R138 补篇：真实根端全角能量型与两标量几何入口

2026-11-20，visible-exact-astra-ac637-20261120 / global_route。

**本篇证明准确消元式，不宣告未计算的正性门通过。** 原 96 个 low-even 根行与全部 high-stable 根行，连同完整均值，在同一实际 frame 上化成一个单独的全角二次型。均值的消元分母在 (U.11) 明列；在其尚未实际分离前，均值仍是独立变量。此二次型的高频主系数由已付正支撑严格为正，剩余有限部分与尾误差是明确的新消费者。

同一外锚到根圈的几何输入，只需两个 scalar 支撑坐标的一次径向积分；随后用根圈角 ODE，保留它与真实周期径向 frame 的残差比较。局部角平行运输不会被冒认成已闭全圈 frame。

## 1. 原根域，不更换 high 行

在真正 $r_*$ 处，所有量用原 moving 角 $\phi$，$N=|D_\phi|$ 的非零物理频率为 $4|j|$。令 $P_H$ 投影到原 $|j|\ge97$，$J$ 的乘子为 $i\operatorname{sgn}j$，故 $J\sin4j\phi=\cos4j\phi$。

写 $f=h_1(r_*)$、$\mu=\langle h_2(r_*)\rangle$。同一全局参考的准确根坐标是
$$
Z_s=(1+\widetilde p)^{-1/2}
       \{N^{1/3}(-Jh_1)+h_2\}.
$$
因此原齐次根数据恰为
$$
\boxed{\quad h_2=\mu+P_HN^{1/3}Jf.\quad}
\tag{U.1}
$$
来源为 [全局参考](R133-supplement-global-positive-reference-and-current-collar.md) (G.13) 的准确矩阵，以及 [真实 full-delta 七列图](R133-supplement-full-real-delta-positive-high-root-to-regular-graph.md) (P.1)。其中 $g(r_*)=N^{-1/3}$，故 $\widetilde p$ 的正归一化不改变零 stable 行。

原 low nonmean even96 为零；并未令 high even 为零。原外端 mean、regular 图、独立源和接口仍在原问题中。本文只处理 prescribed stable 输入为零的齐次核；非零 stable 列按原完整公式另保。

## 2. 精确 physical-to-moving 角图在根上的作用

以下 $u,v,m,a,b_0$ 均为根值，$m=\langle v\rangle<0$，$b_0=a'/e$。将所有物理 frame 与位置按自己的真实 $\theta=\Theta(\phi)$ 拉回，在公式中省略拉回符号。令
$$
\vartheta=\Theta_\phi=v/m>0,\quad
q=I_\phi(h_2-v\mu/m),\quad t=q/v,\quad
T=X-uY,\quad \rho=a/m.
\tag{U.2}
$$
由完整 $D\Psi$，物理方向准确为
$$
\begin{split}
b\circ\Theta&=f/v-u h_2/v^2-(q/v)B_\phi,\\
c\circ\Theta&=-h_2/v^2-(q/v)C_\phi,
\qquad B=u/v,\quad C=1/v.
\end{split}
\tag{U.3}
$$
这保留了逆角变化。特别，不能从 low $h_2=0$ 推出完整物理 $c=0$。

记物理旋转缺陷的角密度为
$\mathsf H=\vartheta H$。则
$$
\omega_\phi=g_{\rm curv}+\mathsf H,
\quad
\boxed{\quad
g_{\rm curv}=\rho\{fY+(t_\phi+\mu/m)T-t u_\phi Y\}.
\quad}
\tag{U.4}
$$
证明只需把 (U.3) 代入
$g_{\rm curv}=a\vartheta(-cX+bY)$，再使用
$$
t_\phi=h_2/v-\mu/m-qv_\phi/v^2.
$$

由于 $I_\phi J=N^{-1}$，(U.1) 给
$$
q=q_f+\mu q_0,\qquad
q_f=P_HN^{-2/3}f,\qquad q_0=-I_\phi(v-m)/m.
\tag{U.5}
$$
$q_f$ 仍有全部未知高频；$q_0$ 保留原全部 nonmean 背景。

## 3. 周期相容式完整保留并确定 mean

对同一真实径向 frame，定义原角缺陷
$Z=O_\theta-O\Omega_\theta$。准确的 root frame 公式给
$$
T_\phi+u_\phi Y
=\vartheta b_0(Y+uX)+\mathsf Z_T=:\mathcal A,
\quad
\mathsf Z_T=\vartheta(Z_X-uZ_Y).
\tag{U.6}
$$
此处完整 $Z$ 不为零。角 primitive 分部积分使 (U.4) 的平均变成
$$
\langle g_{\rm curv}\rangle
=\rho\{\langle fY-t\mathcal A\rangle
                  +(\mu/m)\langle T\rangle\}.
\tag{U.7}
$$

四重等变令该向量平均平行于同一真实旋转轴。可以用原世界 $e_z$ 投影；
为下文只需两个轴坐标的实现，更方便取固定环境单位向量
$\ell=X(r_*,0)$。只要所得到的 $\mathcal D$ 非零，它已同时证明
$\ell$ 对真实轴的投影非零，因此一个 scalar 相容式等价于完整向量相容式。
定义
$$
\begin{split}
\mathcal L f&=\rho\left\langle
 fY-\frac{q_f}{v}\mathcal A\right\rangle\cdot\ell,\\
\mathcal D&=\rho\left\{
 \frac1m\langle T\rangle
   -\left\langle\frac{q_0}{v}\mathcal A\right\rangle\right\}\cdot\ell,\\
\mathcal H&=\langle\mathsf H\rangle\cdot\ell.
\end{split}
\tag{U.8}
$$
周期旋转的准确相容式为
$$
\boxed{\quad \mathcal D\mu+\mathcal Lf+\mathcal H=0.\quad}
\tag{U.9}
$$
它是 $\int\omega_\phi=0$ 的真实后果，不是增加新的 curvature 边界条件。
外端的原独立物理 mean 方程仍保留。

只在实际证明 $|\mathcal D|\ge d_*>0$ 后，才可使用
$$
\boxed{\quad \mu=-\mathcal D^{-1}(\mathcal Lf+\mathcal H).\quad}
\tag{U.10}
$$
完整分母就是 (U.8)，不是一个曲率均值的近似。标准平面腰校验中
$X=e_z$、$Y_z=0$、$u=b_0=Z=0$，准确得到
$$
\mathcal D=a/m^2>0.
\tag{U.11}
$$
(U.11) 只核公式符号，不把实际正根当作这个平面腰。

## 4. 根端准确全角二次型

令 $g_f$、$g_m$ 分别为 (U.4) 中 $(f,\mu)=(f,0)$ 和 $(0,1)$ 的完整输出。若 (U.10) 已合法，则
$$
g=\omega_\phi
=\mathcal Rf+\widehat{\mathsf H},\quad
\mathcal Rf=g_f-g_m\mathcal D^{-1}\mathcal Lf,
\quad
\widehat{\mathsf H}=\mathsf H-g_m\mathcal D^{-1}\mathcal H.
\tag{U.12}
$$
两个右侧向量都平均为零。残差输运补篇 (T.17) 证明实际 $\omega$ 的环境平均为零；同一 C4 加反射对称也使其 moving 平均为零。因此
$$
\boxed{\quad \omega=I_\phi g.\quad}
\tag{U.13}
$$
这里原 $2\pi$ 环境向量周期没有改为 $\pi/2$；四重周期只作用于标量系数。

对 $G=F-\tfrac12e_z$，根端两个准确型是
$$
\boxed{\begin{split}
\mathcal B_L&=\int_0^{2\pi}
G\cdot[(I_\phi g)\times g]\,d\phi,\\
\widetilde{\mathcal B}_L&=\int_0^{2\pi}
G\cdot[(I_\phi g)\times(g-2\mathsf H)]\,d\phi.
\end{split}}
\tag{U.14}
$$
Jacobian 已包含在 $g,\mathsf H$，无额外误乘 $v/m$。
当 $H=0$，两者同为
$$
\mathfrak b_*(f)=\int G\cdot[(I_\phi\mathcal Rf)\times\mathcal Rf].
\tag{U.15}
$$
其真实对称双线性形式由
$\tfrac12\int G\cdot[(I\mathcal Rf)\times\mathcal Rk
 +(I\mathcal Rk)\times\mathcal Rf]$ 给出。
完整 $H$ 的交叉项和平方项则由 (U.12)--(U.14) 直接保留；不能在齐次 moving 核中免费设 $H=0$。

## 5. 高频主符号的严格符号与有限任务范围

本节说明为什么根圈消费者有一个有限入口，不代替其实际数值下界。
背景在角上光滑，$a,m$ 在本根圈是常量。先忽略已显示的 smooth mean 秩一项，它是 smoothing。
对高频 $f$，(U.4) 的两个最高阶项为
$$
g_1=\rho fY,\qquad
g_2=(\rho/v)N^{1/3}Jf\,(X-uY).
$$
相应 primitive 的最高项为
$I g_1=-\rho N^{-1}JfY$ 和
$I g_2=(\rho/v)N^{-2/3}f(X-uY)$。
因为 $Y\times(X-uY)=n$，cross 项给正主符号
$$
\boxed{\qquad
\sigma_{-2/3}(\mathfrak b_*)
=\frac{2a^2s}{m^2(-v)}|\xi|^{-2/3}>0.
\qquad}
\tag{U.16}
$$
$I g_2$ 与 $g_2$ 的最高 self 项因同向叉积为零。
其下一项及 $q_f$ 乘背景导数的项至多 order $-4/3$；$g_1$ self 项至多 order $-2$。
这些断言可直接用完整 Fourier 系数验证：
$I M_a-M_aI$ 在非零输出上是
$-I M_{a_\phi}I$ 加所保留的 mean rank；
$N^\tau$ 的频率差在同号邻频上由 mean-value 公式下降一阶，远离对角的部分由 smooth 背景 Fourier 尾控制。没有将 $P_H$ 穿过背景乘子。

因此，$N^{1/3}\mathfrak b_*N^{1/3}$ 的完整对称算子是
正乘子 $2a^2s/[m^2(-v)]$ 加一个 compact 余项。
这里只使用该 compact 余项可由完整 Fourier 多项式和其导数尾在算子范数逼近的事实。
它保证某个有限角 cutoff 之后有正下界，**不保证原 cutoff97 已经足够，也不保证有限部分非负**。
任何提高数值 tail cutoff 都保留原97及之后的真实 stable 行；中间模只进入实际有限矩阵，不会被删掉。

## 6. 同外锚的两标量径向输入

在反射轴 $\theta=\phi=0$，$u=B=0$，$Y$ 恒定，
$A=Kv_{\rm axis}$。只需积分
$$
q=G\cdot X,\qquad s_0=G\cdot n,\qquad e=a\gamma,
$$
$$
\boxed{\quad
\binom q{s_0}_r
=eKv_{\rm axis}
 \begin{pmatrix}0&1\\-1&0\end{pmatrix}\binom q{s_0}
 +\binom e0.
\quad}
\tag{U.17}
$$
外端准确初值是
$$
q_R=a_Rt_R+(h-1/2)z_R,
\qquad s_{0,R}=a_Rz_R-(h-1/2)t_R.
\tag{U.18}
$$
所有对象都是第 1 节同一 Qrepair、$\eta_0$、同一个原外锚。
无需为512条角线重跑旧模型几何。

一个充分的读取方式是：消费原完整4650闭行的已付 signed intrinsic、mean 数据；从准确 dyadic candidate cubic 只形成新的 cosine-sum 轴投影。每个原 candidate/scalar 接口仍在分区中，状态连续传播。整个正区 $K<4$、$\int e<2$ 已付。
先计算原 candidate 的轴，再比较同端锚的 Qrepair。由
$|\Delta v|<4\cdot10^{-18}$、$|G|<222/125$，正交变分常数式给
$$
\|\Delta(q,s_0)\|_2
<16(4\cdot10^{-18}).
\tag{U.19}
$$
此差保留全部 mean 修补；不重新评估旧 intrinsic target。

对一个旧闭行，设 $e,w=eKv_{\rm axis}$ 的真实球分别以
$e_c,w_c$ 为中点，半径为 $r_e,r_w$。
精确传播常系数二维旋转及其 affine 力，行误差至多
$$
\Delta r\{r_e+(222/125+16\epsilon)r_w\},
\quad\epsilon=4\cdot10^{-18}.
\tag{U.20}
$$
旧误差随正交旋转保范数，故全部行费用直接相加。中点只定义一个明确新比较 ODE，不充当真实系数；(U.20) 完整支付球半径。
最后的 $[r_*,r_b]$ 用原 whole-root germ、准确根区间及长度界接入；不把 $r_*$ 换成中点，也不越过原 scalar/candidate germ。

## 7. 根角比较模型及必须保留的实际费用

给定 (U.17) 的根值球，可作一次整体正交旋转，在该轴上设
$$
X_0=e_z,\quad Y_0=e_y,\quad n_0=e_x,\quad
G_0=s_0e_x+qe_z.
\tag{U.21}
$$
这里 $G_0$ 已编码固定世界点 $p=\tfrac12e_z$ 的相对位置。
此局部坐标的 $e_z$ 是 (U.8) 的 $\ell=X(r_*,0)$，不是原世界竖直向量。
第 3 节说明，用 $\ell$ 得到的实际非零分母已经足以恢复完整周期 mean；
因此不必再积分一个世界转角来知道真实旋转轴在局部坐标中的分量。

在整个 $0\le\phi\le2\pi$ 上解明确的 ideal angular 系统
$$
\begin{split}
\bar X_\phi&=(b_0v/m)\bar Y+(au/m)\bar n,\\
\bar Y_\phi&=-(b_0v/m)\bar X+(a/m)\bar n,\\
\bar n_\phi&=-(au/m)\bar X-(a/m)\bar Y,\\
\bar G_\phi&=(av/m)\bar Y.
\end{split}
\tag{U.22}
$$
全部角系数是原完整 degree32 多项式，均值 $m$ 保留。
它只是一条新根圈比较 ODE；选择全圈而非扇区拼接，避免需要未知世界旋转轴的坐标。
实际 $G,O$ 有原 $P,Z$，因此 (U.22) 的端点 holonomy/position 缺陷必须保留，不能把四个未闭扇区直接粘成全周期实际 frame。

实际完整角缺陷记录已经给
$\|E\|<3.127699\cdot10^{-8}$、
$\|E_\phi\|<4.222016\cdot10^{-6}$、
$\|P_M\|<4.956566\cdot10^{-8}$、
$\|(P_M)_\phi\|<7.013365\cdot10^{-6}$，并保全部6143接口。
根圈比较必须按 support 补篇的同物理角转移使用这些量，另加真实 Qrepair 费用。
如果 full-operator tail 使用一阶角范数，还必须支付下面准确的一阶差式，不能从 C0 差免费提升。

具体地，在旧 moving 模型的物理拉回 $M=O^M\circ\Theta^{-1}$ 上，令
$\upsilon=\Theta_r/\Theta_\phi$，$\epsilon=\Theta_r-\tau$。则
$$
M_r=M\Omega_r+\mathcal C,
\quad\mathcal C=-\epsilon M\Omega_\theta-\upsilon E,
\tag{U.23}
$$
$$
(F^M\circ\Theta^{-1})_r=eM_X+\mathcal D_F,
\quad\mathcal D_F=-a\epsilon M_Y-\upsilon P_M.
\tag{U.24}
$$
物理 $\theta$ 导数满足
$E_\theta=E_\phi/\vartheta$、
$(P_M)_\theta=(P_M)_\phi/\vartheta$、
$M_\theta=M\Omega_\theta+E/\vartheta$。
所以 $\Delta=O^P-M$ 有
$$
\|\Delta_\theta(r)\|
\le\int_r^R\{\|\Delta\|\|(\Omega_r)_\theta\|
                         +\|\mathcal C_\theta\|\},
\tag{U.25}
$$
其中 $\mathcal C_\theta$ 是 (U.23) 的完整乘积导数；
位置导数差同理由
$\int[e\|\Delta_\theta\|+\|(\mathcal D_F)_\theta\|]$ 给出。
这些都是旧 closed-row 系数和旧 $E,E_\phi,P_M,(P_M)_\phi$ 的新消费，
不需重算旧 whole geometry，也没有未知方向的范数。
Qrepair 与旧物理模型的一阶差另用同一正交变分公式及完整角图导数支付。

当前独立新目标因而清楚分为：真根 $(q,s_0)$；根角比较与真实 C0/C1 转移；完整 $\mathcal D$；最后是 (U.15) 有限角矩阵及全尾/mean/cross 费用。
每一个可以独立保存真实完整结果；其中任何一个通过都不会冒称其余目标或本课题已完成。
