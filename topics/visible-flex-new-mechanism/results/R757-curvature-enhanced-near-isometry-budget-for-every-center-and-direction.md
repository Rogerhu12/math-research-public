# R757　容许度量误差和实际主曲率时的全中心、全方向帽姿检验

材料、两个有标记刚圈、向量面积 $B$、材料面积 $A$、共形长度 $L$、给定中心 $C$ 的三分量调和场 $H$ 和矩阵 $M(H)$ 沿用 [R755](R755-vector-area-harmonic-energy-and-all-pose-budget.md)。给定 $g=E(r)dr^2+r^2d\phi^2$；$a=.075,\ b=.22,\ \sin\vartheta=.27$。$n_i,n_o$ 为两边的**实际有向单位法向**，须由严格端迹给出。程序同时包围规定的 $.27$ 和原 R755 已验证的二进制角所对应的真旋转，统一使用其正弦区间 $[.26999999999999,.27000000000001]$。原浮点矩阵元素仅在已核实的旋转包围意义下使用。取实 $C^2$ 浸入 $F$、实际诱导度量 $G$、面积比 $J=dA_F/dA_g$，并假设

$$
 \|G-g\|_{g,\mathrm{op}}\le\eta<1,\qquad \mu=1+\eta,\qquad
 |\kappa_1(F)|,|\kappa_2(F)|\le M_c .
$$

若使用 $M_c=100/3$ 是为必要地检验绝对 reach 至少 $.03$。只给相对直径的 reach 时须另以已证明的实际尺度换算。下文不假设材料径线对 $G$ 是测地线。

## 曲率和两个非负能量项

对定向单位法向 $n$、任意环境向量 $v\ne0$，记 $z=v\cdot n,\ m=v\cdot B/A$。向量面积的微分恒等式给 $\int Jz\,dA_g=Am$。由 $1-\eta\le J\le\mu$ 及 $dF g^{-1}dF^T\preceq\mu(I-nn^T)$，调和边值正交给

$$
\begin{aligned}
 v^T[\mu A I-M(H)-BB^T/(\mu A)]v
 &\ge v^T M(F-H)v\\
 &\quad+\frac1\mu\int\big[(Jz-m)^2+(\mu^2-J^2)z^2\big]\,dA_g .
\end{aligned}
$$

右侧第二行展开即 $\mu\int z^2dA_g-Am^2/\mu$。由 Weingarten 公式 $\|n_r\|\le M_c\sqrt{G_{rr}}\le M_c\sqrt{\mu E}$。令 $s_e(r)$ 为材料径长自端 $e$ 到该纬圈，$d_e=M_c\sqrt\mu\,s_e$；对所有材料角有 $\|n-n_e\|\le d_e$。于是

$$
 N_\eta=\max_{e=i,o}\bigl(|v\cdot n_e-m|-(\eta+d_e)|v|\bigr)_+,\qquad
 Z_\eta=\max_{e=i,o}\bigl(|v\cdot n_e|-d_e|v|\bigr)_+
$$

分别下界 $|Jz-m|$、$|z|$。前者用 $|J-1|\le\eta$，后者只用法向传播。两项各在整纬圈成立。

写 $d\ell=\sqrt E\,dr$。在真实材料正交标架，$(v\cdot F_\ell,v\cdot F_\phi/r)$ 的点态范数至多 $\sqrt\mu\sqrt{|v|^2-Z_\eta^2}$。引入 $d\phi/(2\pi)$ 的两分量 $L^2$ 范数

$$
 h_v(r)=\|(v\cdot H_\ell,\,v\cdot H_\phi/r)\|_{L^2},\qquad
 Y_\eta=\big(h_v-\sqrt\mu\sqrt{|v|^2-Z_\eta^2}\big)_+ .
$$

对 $F-H$ 用逆三角不等式。合并两个不同非负项即得整个姿态族的必要条件

$$
 \boxed{\quad
 v^T[\mu A I-M(H)-BB^T/(\mu A)]v
 \ \ge\ 2\pi\int_a^b r\sqrt E\,[N_\eta^2/\mu+Y_\eta^2]\,dr .
 \quad}                                                        \tag{1}
$$

$\eta=0$ 时本式仍成立；R755 在准确等距时还可追踪两帽的**指定径切向**，两套右端界可分别检验。本式不向有度量误差的试面套用该测地切向结论。对于同一 $C,v$，$\eta$ 增大时 (1) 左边不减、右边不增。若在某个误差上限仍有严格负余量，则更小上限同时排除。

## 真实调和能量和全部中心

设 $x=\int_a^r\sqrt E\,dr/r$，两刚圈标架为 $D_i,D_o$。令

$$
 U=\frac{-a\cosh(L-x)D_i+b\cosh x\,D_o}{r\sinh L},\qquad
 V=\frac{a\sinh(L-x)D_i+b\sinh x\,D_o}{r\sinh L}.
$$

实际 $H_\ell=-C/(Lr)+Ue(\phi)$，$H_\phi/r=Ve'(\phi)$。故

$$
 h_v^2=\frac{(v\cdot C)^2}{L^2r^2}
       +\tfrac12 v^T(UU^T+VV^T)v .
$$

所有中心只通过 $(v\cdot C)^2$ 进入 (1)：左边中减去 $2\pi(v\cdot C)^2/L$，$Y_\eta$ 随同一平方非减。对某方向 $v$ 在 $C=0$ 严格负余量即可排除**所有中心**。要证明指定中心矩形全部满足 (1)，足以对各端角证明所有方向；固定 $v$ 时 $|v\cdot C|$ 的最大值在角上。R738 的矩形 $|C_x|\le.0115,\ C_y=0,\ |C_z|\le.0426$ 关于原点对称，故两对反角仅需两套真正不同的计算。一个原末态中心被排，另一个中心的资格仍由其各自余量决定。

区间运算先尝试单位方向的一致界。左边用真实块对角矩阵的最小特征值，$xz$ 块为实对称二阶矩阵。右边的 $N_\eta$ 以 $\|n_e-B/A\|$ 代 $|v\cdot(n_e-B/A)|$ 后逐胞上估。对 $Y_\eta$，每端用 $Z_e=(|v\cdot n_e|-d_e)_+$ 先各自算上界，最后取两者最大。其一项以 $h_v\le\sqrt{\lambda_{\max}(Q_H)}$ 和 $Z_e\le(1-d_e)_+$ 代入，$Q_H$ 是上式的真实调和矩阵。另一上界是调和双梯度减去该端平面径、角双标架后的 $L^2$ 算子范数，即在 $Q_H$ 中以 $U-D_e,V-D_e$ 替换 $U,V$。后者成立因为对应端的切向允许量至少 $\|D_e^Tv\|$，且 $\sqrt\mu\ge1$。先逐端取两个上界的较小值可减少法向与平面切向极端方向的包络损耗。若最小特征值仍大于等于全右边上界，则所有方向通过 (1)。

全方向还可用三面尺度齐次覆盖。选择绝对坐标最大的一项，令该坐标为 $1$，另两个在 $[-1,1]$；整体变号不影响 (1)。对子盒的完整区间余量下端非负即放行。中点或初选谱向量的实际区间余量上端为负才排除。剩下的盒二分，未完成的叶明确保留。通过这些必要条件仍不提供满足三 Gram、两 jet、法管及运动的物理场。

[全中心区间消费者](../scripts/r757_near_metric_pose_budget.py) 仅消费自然完成的 R755 的完整 FINAL 及原付费 journal。核验两件字节 SHA、原 R738 终态和 64 阶 calibration 身份、相同 fingerprint、完整 424 个原积分胞和末态 $A/\pi,L,\int\sqrt E$。用前后缀求物质距离、共形距离及调和系数包围；程序所有面积和矩阵同时除以 $\pi$。新方向和球面子盒各自保留费用与结果。未提供原材料完整证明时，本篇不宣称旧 $E_\sharp$ 或实际中心已通过或已排除。

## 若固定材料被排除，可直接更换的实物径剖面

以下给出 (1) 确实可通过的材料变化方向，并保留原两端的真 dyadic 胞。先看充分通过本门的一致标尺。设 $\widetilde A=A/\pi,\ \widetilde B=B/\pi$，且 $\widetilde A\ge|\widetilde B|$；置

$$
 H_*=\frac{2C_{\max}^2}{L}
 +(a^2+b^2)\coth L+2ab\,\mathrm{csch}\,L .
$$

则 $\|M(H)\|/\pi\le H_*$ 对 $|C|\le C_{\max}$。单位方向有 $N_\eta\le2$，仅距至少一端的材料径长 $\le2/(M_c\sqrt\mu)$ 时可能非零。用面积权 $2r\,d\ell$ 得 $\int(N_\eta^2/\mu)dA_g/\pi\le32b/(M_c\mu^{3/2})$；又 $\int Y_\eta^2dA_g/\pi\le H_*$。因此

$$
 \mu\widetilde A-\frac{|\widetilde B|^2}{\mu\widetilde A}
 \ \ge\ 2H_*+\frac{32b}{M_c\mu^{3/2}}                         \tag{2}
$$

足以使该矩形整球方向通过 (1)。这个粗界只作换源思路；原实物优先用 (1) 逐胞定量判定。

在中央 $[.085,.21]$ 选择新旋转图源，以 $p=w/\sqrt{1+w^2}$ 表示其径向坡 $w$。 在宽 $.0625$ 的前半段，以首尾各 $.00005$ 缓冲，放置线性升宽 $.0307$、平顶宽 $.001$、线性降宽 $.0307$ 的单位梯形。将全直线零延拓的梯形与支半径 $.000025$ 的正偶光滑单位核卷积，得到 $f$。负半用关于 $.1475$ 的奇镜像。故整中央 $|f'|\le1/.0307$，两个真恒平台宽各至少 $.00095$，两端开段仍为零。令 $p=\lambda f,\ 0<\lambda<1$，中央取 $w=p/\sqrt{1-p^2}$；以源曲面 $(r\cos\phi,r\sin\phi,\int w\,dr)$ 接上原静止各端的径向母图。中央的真 $g$ 为 $dr^2/(1-p^2)+r^2d\phi^2$，正负镜像使新中央的两端等高；新源两帽的高差只含沿用的真尾积分。只在原剖面中央回平处拼接，尾上用其真实径坡和原尾高度常数。新源两主曲率为 $p'$、$p/r$；中央绝对值分别 $<32.58,\ <11.77$，原尾界见 R738。以常高圆盘及水平外平面径向延拓成 proper 全图，逐偏置层的投影单射给**此辅助源图**的 reach 至少 $1/32.58>.03$。这里圆盘与无限平面是证明所选源图法管的延拓，原闭壳其余刚件需要另作跨片检查。[R738](R738-broad-dyadic-collars-with-thick-macroscopic-phase-geometry.md)；[R662](R662-tilted-two-plane-global-tube-and-offset-cap-clearance.md)。

当 $\lambda\uparrow1$ 时，两平台让新的 $\widetilde A,L$ 同时趋于无穷，而 $H_*$ 有界。于是某个 $\lambda<1$ 必通过 (2)，且每个这样的有限新源均有上述真实中央曲率界。这未给未知终姿同 $g$ 的填充。中部绝对高度仍可能增长，必须重新支付整像直径、全壳不同片法球、宏观握持/运动，并为新 $E$ 重新求解。在旧 $E_\sharp$ 尚无严格排除时，不要求原科学工单改用此源。
