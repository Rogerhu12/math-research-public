# R191：真实主曲率惩罚的完整位置两jet与参数导数

**状态：完整函数层面的公式、三行谱残差与其参数导数已证明；实际非零第16步状态的局部JVP核已在纯V8完成。以下是一个有限数值目标的明确扩展，$9.5$只是可选曲率指导值，不是新的课题完成门，也不是连续reach证书。**

本结果使用[R187](R187-closed-unit-angular-tangents-and-direct-position-metric.md)的完整两角位置族以及[R188](R188-quarter-periodic-primitives-and-certified-cell-integration.md)的quarter primitive。底层可以是原R187固定半径族，或R190明确改变内蕴度量的半径设计族。原文件和已有接受态不修改。

## 1. 对象、完整位置与全部未知量

固定材料坐标$s,u$。原两角函数为
$$
\Theta=\Theta_{\rm ref}+\sum_{j,k}A_{jk}B_j(s)\sin(2ku),\qquad
\Phi=\Phi_{\rm ref}+\sum_{j,k}D_{jk}B_j(s)\sin(2ku).
$$
$B_j$是支撑于中央柱与cut之间的$C^2$三次cardinal B-spline。角向三角复合始终作为完整函数，不作DFT或高模截断。定义
$$
T=(-\sin\Theta\cos\Phi,\ \cos\Theta\cos\Phi,\ \sin\Phi),\qquad
Y=\mathcal P T,
$$
其中$\mathcal P$是R187/R188的唯一零均值周期primitive。中央对称性保证$T$零均值且$|T|=1$。轴向中心为
$$
Z=Z_{\rm base}+\sum_j z_jB_j+z_{\rm cut}S_5((s-c)/(S-c)).
$$
R190另允许
$$
a=a_{\rm base}+\sum_j\rho_jB_j.
\tag{1}
$$
$\rho$变化明确改变物理度量；原$\Theta_{\rm ref},\Phi_{\rm ref},Z_{\rm base}$不随$\rho$偷偷改变。R187对应无$\rho$列。

完整位置以及全部实际两jet为
$$
\begin{aligned}
X&=aY+Ze_z,\\
X_s&=a_sY+aY_s+Z_se_z,& X_u&=aT,\\
X_{ss}&=a_{ss}Y+2a_sY_s+aY_{ss}+Z_{ss}e_z,\\
X_{su}&=a_sT+aT_s,&X_{uu}&=aT_u.
\end{aligned}
\tag{2}
$$
这里$Y_s=\mathcal PT_s,\ Y_{ss}=\mathcal PT_{ss}$，计算的是位置图的真实基本形式，不是一个尚未满足GC的形式II。

以下始终在实际浸入点工作，即$X_s\times X_u\ne0$。不浸入的数值试步无法定义主曲率，由消费者明确拒绝；这只是题目所需真实曲面的必要条件，不是额外设置的搜索门。

## 2. 角向完整导数及参数列

记$T_\Theta,T_\Phi$等为对两个角值的偏导数。R187已给出一、二阶角张量，第三阶所需者为
$$
T_{\Theta\Theta\Theta}=-T_\Theta,\quad
T_{\Theta\Phi\Phi}=-T_\Theta,\quad
T_{\Phi\Phi\Phi}=-T_\Phi,
$$
$$
T_{\Theta\Theta\Phi}
=(-\sin\Theta\sin\Phi,\ \cos\Theta\sin\Phi,\ 0).
\tag{3}
$$
它们只是在固定$s,u$对有限状态参数求导时出现；不要求曲面有径向第三导数，更不引入$C^3$曲面门。

完整角、径导数为
$$
T_s=T_\Theta\Theta_s+T_\Phi\Phi_s,\qquad
T_u=T_\Theta\Theta_u+T_\Phi\Phi_u,
$$
$$
T_{ss}=T_\Theta\Theta_{ss}+T_\Phi\Phi_{ss}
 +T_{\Theta\Theta}\Theta_s^2
 +2T_{\Theta\Phi}\Theta_s\Phi_s
 +T_{\Phi\Phi}\Phi_s^2.
\tag{4}
$$
$\Theta_u,\Phi_u$必须来自完整已知角lifting和实际$\sin(2ku)$的一阶导数，不能由有限DFT替代。

对任意一个角参数，记其变化为$v=\delta\Theta$或$v=\delta\Phi$。相应$v_s,v_{ss},v_u$由同一$B_j,B'_j,B''_j$及$\sin(2ku),2k\cos(2ku)$给出。统一令$i\in\{\Theta,\Phi\}$，有
$$
\begin{aligned}
\delta T&=T_i v,\\
\delta T_s&=(T_{i\Theta}\Theta_s+T_{i\Phi}\Phi_s)v+T_iv_s,\\
\delta T_u&=(T_{i\Theta}\Theta_u+T_{i\Phi}\Phi_u)v+T_iv_u,\\
\delta T_{ss}&=T_iv_{ss}
 +2(T_{i\Theta}\Theta_s+T_{i\Phi}\Phi_s)v_s\\
&\quad+\bigl(T_{i\Theta}\Theta_{ss}+T_{i\Phi}\Phi_{ss}
 +T_{i\Theta\Theta}\Theta_s^2
 +2T_{i\Theta\Phi}\Theta_s\Phi_s
 +T_{i\Phi\Phi}\Phi_s^2\bigr)v.
\end{aligned}
\tag{5}
$$
这由(4)逐项求导直接得到，包含常被漏掉的$B''$列、$T_{\Theta\Theta\Phi}$项及完整角一导的变化。

紧域上的连续导数允许对精确primitive在参数下求导：
$$
\delta Y=\mathcal P\delta T,\quad
\delta Y_s=\mathcal P\delta T_s,\quad
\delta Y_{ss}=\mathcal P\delta T_{ss}.
\tag{6}
$$
于是角参数的位置两jet列由(2)把$Y,T$分别换成其变化得到。

对中心高度列$(B,B',B'')$，
$$
\delta X=Be_z,\quad\delta X_s=B'e_z,\quad
\delta X_{ss}=B''e_z,\quad
\delta X_u=\delta X_{su}=\delta X_{uu}=0.
\tag{7}
$$
cut-height列使用相同公式，$B$换成给定quintic。特别不能因为某点$B'=0$就在曲率消费者里删去该列：其$B''$可能非零。

对半径列$\rho_j$，由于原角lifting与$\rho$独立，
$$
\begin{aligned}
\delta X&=B_jY,&
\delta X_s&=B'_jY+B_jY_s,&
\delta X_u&=B_jT,\\
\delta X_{ss}&=B''_jY+2B'_jY_s+B_jY_{ss},\\
\delta X_{su}&=B'_jT+B_jT_s,&
\delta X_{uu}&=B_jT_u.
\end{aligned}
\tag{8}
$$
(5)–(8)覆盖全部$\Theta,\Phi,Z,z_{\rm cut},\rho$列。固定$s$下只有有限几个B-spline支撑非零，因此局部列结构仍然有限。

## 3. 真实Gram归一与它的完整变化

令
$$
U=X_s,\quad V=X_u,\quad W=U\times V,\quad
w=|W|,\quad N=W/w,
$$
$$
E=U\cdot U,\quad F=U\cdot V,\quad G=V\cdot V,
$$
$$
L=N\cdot X_{ss},\quad M=N\cdot X_{su},\quad H=N\cdot X_{uu}.
$$
为避免与度量误差或形式II混用，本节$H$只是实际第二基本形式的$uu$分量。

取由$U,V$按Gram正交化得到的正交基
$$
e_1=U/\sqrt E,\qquad e_2=(V-rU)/\sqrt P,\qquad
r=F/E,\quad P=w^2/E.
$$
$E,P$均正。真实形算子的对称矩阵为
$$
\mathscr S=
\begin{pmatrix}A&B\\B&C\end{pmatrix},\quad
A=L/E,\quad B=(M-rL)/w,\quad
C=(H-2rM+r^2L)/P.
\tag{9}
$$
这由第二基本形式在上述基中的双线性展开得到。因此$\mathscr S$的两个实特征值就是该位置图的真实主曲率，即使$E,F,G$尚未达到目标值也成立。

任意参数变化必须同时微分法向和Gram基：
$$
\delta W=\delta U\times V+U\times\delta V,\quad
\delta w=N\cdot\delta W,\quad
\delta N=(\delta W-N\delta w)/w,
$$
$$
\delta E=2U\cdot\delta U,\qquad
\delta F=\delta U\cdot V+U\cdot\delta V,
$$
$$
\delta L=\delta N\cdot X_{ss}+N\cdot\delta X_{ss},
$$
并对$M,H$使用相应的$su,uu$两jet。接着
$$
\delta r=(\delta F-r\delta E)/E,\qquad
\delta P=P(2\delta w/w-\delta E/E),
$$
$$
\begin{aligned}
\delta A&=(\delta L-A\delta E)/E,\\
\delta B&=(\delta M-\delta rL-r\delta L-B\delta w)/w,\\
\delta C&=\bigl(\delta H-2\delta rM-2r\delta M
 +2r\delta rL+r^2\delta L-C\delta P\bigr)/P.
\end{aligned}
\tag{10}
$$
所以这里没有把法向、正交基、归一分母或R190的$\rho$作用冻结。唯一除数是实际浸入所保证的$E,w,P$，不除某个可能为零的II分量$n$。

## 4. 与主曲率hinge完全等值的三行残差

给定数值指导$C_*>0$。令
$$
f(x)=x-\operatorname{clip}(x,[-C_*,C_*])
=\operatorname{sgn}(x)\max(0,|x|-C_*),
$$
$$
Q=f(\mathscr S),\qquad
\mathcal R(\mathscr S)=(Q_{11},\sqrt2Q_{12},Q_{22}).
\tag{11}
$$
实对称矩阵的正交谱分解给
$$
|\mathcal R(\mathscr S)|^2=\|Q\|_F^2
=\sum_{i=1}^2\max(0,|\kappa_i|-C_*)^2.
\tag{12}
$$
故三行残差只是同一个主曲率惩罚的无特征向量歧义表示，并没有换成一个更弱的矩阵条目界。

设
$$
h=(A+C)/2,\quad d=(A-C)/2,\quad r_0=\sqrt{d^2+B^2},\quad
\lambda_\pm=h\pm r_0.
$$
当$r_0>0$，记
$$
P_\pm=\frac12\left(I\pm\frac1{r_0}
\begin{pmatrix}d&B\\B&-d\end{pmatrix}\right),\qquad
\alpha=\frac{f(\lambda_+)-f(\lambda_-)}{\lambda_+-\lambda_-}.
$$
在特征值不等于阈值$\pm C_*$的点，精确Fréchet导数为
$$
Df(\mathscr S)[V]=f'(\lambda_+)P_+VP_+
+f'(\lambda_-)P_-VP_-
+\alpha(P_+VP_-+P_-VP_+).
\tag{13}
$$
证明可先对一个对角$\mathscr S$逐条求导：对角变化乘$f'$，非对角变化由两个特征方向的一阶旋转给出上述分差；再按固定正交变换共轭。二维情况下也可直接微分
$f(\mathscr S)=\frac12(f(\lambda_+)+f(\lambda_-))I+\alpha(\mathscr S-hI)$，得到同式。

实现不在重复特征值处分除零。当两个特征值处于同一个仿射区间，$f(\mathscr S)$准确为$0$、$\mathscr S-C_*I$或$\mathscr S+C_*I$；其导数分别为$0$或恒等。这包括区间内部的所有重复特征值。其余分支$r_0>0$，可用
$$
Df(\mathscr S)[V]=\alpha V
+(f'(\lambda_+)-\alpha)\operatorname{tr}(P_+V)P_+
+(f'(\lambda_-)-\alpha)\operatorname{tr}(P_-V)P_-,
\tag{14}
$$
只需有界的归一方向$d/r_0,B/r_0$，不求特征向量导数。

在$|\lambda_i|=C_*$处，残差$f$确实不处处可微。实现明确采用该阈值上的inactive斜率$0$，这是可由阈值内侧逼近得到的广义导数选择，不把它称作经典光滑导数。平方目标(12)的一阶导数在阈值处仍一致，因为该阈值特征方向的残差为零。实际局部JVP核的active点远离阈值，没有用这条约定掩盖差分失败。

将(10)代入(13)或(14)，再取(11)三个条目，即得完整残差Jacobian。所有参数作用已由(5)–(10)进入。

## 5. 明确有限目标与局部normal累积

消费者保留原R187/R190全部metric行，不更换参数布局。默认$C_*=9.5$、数值权重$\omega=10^{-4}$，均由调用者明确指定。曲率径点是原物理profile及B-spline的所有knots，另加各相邻间隔的Gauss2点。

令knots为$0=s_0<\cdots<s_m=S$。选$0\le\eta\le1$。节点权重为
$$
w_i^{\rm node}=\frac{\eta}{2S}
\bigl((s_i-s_{i-1})+(s_{i+1}-s_i)\bigr),
$$
不存在的端间隔记零；每cell的两条Gauss权重为$(1-\eta)(s_{i+1}-s_i)w_j^{G2}/S$。两组权重总和为$1$。默认$\eta=1/2$。角向使用完整quarter节点及归一梯形权重，亦总和$1$。这是明确的有限优化目标，并未以这些权重宣称连续积分已经严格计算。

曲率行取$\sqrt{\omega w_sw_u}\mathcal R$，与原metric行拼接。因此
$$
F_{\rm total}=(F_{\rm metric},F_{\rm curvature}),\qquad
H=J^TJ,\quad g=J^TF.
\tag{15}
$$
每个曲率点只涉及其真实径向支撑列，可逐点累积normal而不构造高大的整体Jacobian。实现的value、normal、方向乘积使用同一有限点集、相同完整函数和相同权重；不是仅以真实曲率拒绝试步而继续使用缺少曲率列的旧Jacobian。

加入knots有直接实际依据：已保存第16步的曲率峰出现在$s=.36293298329056384$的B-spline knot。此选择仍只是新有限离散，不是额外几何完成条件。

四分之一积分在数学定义中是精确的R188 primitive。在程序中，对$T,T_s,T_{ss}$及它们的参数变化使用同一固定Gauss8点和第一矩。固定点有限和的参数微分准确交换，因此这里的J是所实现有限公式的完整导数。Gauss8对精确primitive的连续误差、有限角/径网格之外的metric与曲率，仍须按R188及后续连续包络另付；不得把这个有限数值事实冒成全域几何证明。

## 6. 明确源码与唯一局部实际核

三个新文件：

- [fd2d-position-curvature-chain-R191.cjs](../scripts/fd2d-position-curvature-chain-R191.cjs)，main blob 7abcea6d968125aee8bc807e2f797b2227746828。
- [fd2d-position-curvature-provider-R191.cjs](../scripts/fd2d-position-curvature-provider-R191.cjs)，main blob 9322c7d1cc804d6529ab397d030af0e6c23ca2c7。
- [fd2d-check-position-curvature-R191.cjs](../scripts/fd2d-check-position-curvature-R191.cjs)，main blob 6f0590f59b7a6278439a890b9e33f7acd9d6fe5b。

入口为
~~~js
const alg=createR191Algebra();
const guided=createR191CurvatureProvider(
  engine, originalR187orR190Provider,
  {guide:9.5,weight:1e-4,nodeShare:0.5}, alg);
~~~
guided.value/normal/evaluate继承原实际有限LM接口；总squaredNorm包含metric与曲率两项，并分别保留metricSquaredNorm、curvaturePenaltySquaredNorm。guided.point(s,u,z,{jacobian:true})给局部完整三行残差、全非零列、位置两jet参数变化。

真实输入为[第16步状态](../notes/2026-11-12-fd2d-direct-position-R187-LM-02-report.json)，
SHA256 b30236a681fdd4329386583a98e740ff2d281f853d9873835f093228129bafab，
main blob 416afb489caf4816fd634ecfac3d91a6ae93c3d2。
其181维向量原样保留，另在R190接口追加12个准确零半径系数，作为明确同场嵌入fixture。它不是新接受态。

纯V8实际执行261毫秒，没有OS子进程或OS退出码。检查三个真实物理点，固定$s=.36293298329056384$：

| $u$ | 实际采样 $\max|\kappa|$ | 状态 |
|---|---:|---|
| $\pi/2$ | 11.8362525545 | active |
| 1.55 | 11.6137749622 | active、非轴 |
| 1.47 | 7.3288827010 | inactive |

零$\rho$嵌入时全部位置0–2jet的对照差为$0$。对真实非零状态的一条同时含$\Theta,\Phi,Z,z_{\rm cut},\rho$的方向，三条步长$2\cdot10^{-6},10^{-6},5\cdot10^{-7}$的最大scaled曲率残差JVP差为$2.04\cdot10^{-10}$；额外纯$\rho$方向的最大scaled差为$4.37\cdot10^{-9}$。全部位置0–2jet参数方向的最大scaled差为$2.42\cdot10^{-9}$。inactive点的三行残差及J均为零。

这些是有限差分数值核，不是区间误差界。本闭组没有再装整个normal、没有运行BVP、没有宣布已获得新的非圆解。完整真实报告为[局部JVP报告](../notes/2026-11-12-fd2d-R191-curvature-local-jvp-01.json)。

## 7. 完成标准仍然不变

曲率惩罚可帮助实际求解避免把metric均方误差集中为窄曲率峰，但降低它不保证得到等距嵌入。最终仍须冻结候选、支付真实完整metric、C²接合、全域浸入与嵌入、非局部法球/reach、实际cut高度、held与含反射商距离等本课题要求。$9.5$不会替代这些要求，也不会成为阻止其他合法构造的新硬门。
