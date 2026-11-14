# R133：随解曲率角的完整非线性系统、反向构造及平均模能量

**已证明（准确等价结构与完整线性 Cauchy/source 合同）。**
在当前四重反射类中，把曲率角作为非线性未知量的自适应坐标，可以把完整
Codazzi 系统写成一个封闭的方程组。其主部只含一个径向平均和一个明确的
角向原函数。反向构造物理角也有显式公式，所以不必先假设固定中心坐标的
非局部变分变换存在逆。

本篇不宣称该新方程已解，或平均模可以删去。平均模的完整变分恰是下面
必须保留的一个独立标量耦合。全部非零 Fourier 变分也未截断。

## 1. 空间、归一与准确等价方程

令真实径向目标为 $g=E(r)dr^2+a(r)^2d\theta^2$，
$\gamma=\sqrt E/a$、$\beta=a'/a$、$K=K(r)$。在当前四重反射类中，$u=B/C$
关于角为奇函数，$v=1/C<0$ 为偶函数，二者周期为 $\pi/2$。
角平均用整圆归一积分，$I=\partial_\phi^{-1}P_0$ 是零均值周期原函数。

对真实物理场令 $D=\langle C\rangle_\theta<0$，固定曲率角的原点为

$$\phi(r,\theta)=D^{-1}\int_0^\theta C(r,s)\,ds,
\qquad \phi_\theta=C/D>0.$$

这与此前 (H.2) 的反射归一一致，是整个圆的度1微分同胚。以下 $u,v$ 改写成
$(r,\phi)$ 的函数，并定义

$$m=\langle v\rangle_\phi=1/D<0,\qquad
S=u^2+Kv^2,\qquad d=-\beta I S.\tag{M.1}$$

那么完整无源 Codazzi 方程准确等价于

$$\begin{aligned}
u_r&=d u_\phi+\gamma mK v_\phi-\beta u(1+S),\\
v_r&=d v_\phi-\gamma m u_\phi+\beta v(1-S).
\end{aligned}\tag{M.2}$$

同时平均模满足完整标量恒等式

$$m_r=\beta m(1-\langle S\rangle_\phi).\tag{M.3}$$

这里的奇偶反射是构造所选基解的实际对称性；它不把允许的 $v$ 平均模设为
零，也不声称 (M.2) 是没有反射归一的一般双平均系统。相位族仍由原物理角
的轴对称度量作用生成，不能把计算角 $\phi$ 偷换成物理目标角。

### 正向推导

由 $d\phi=(C/D)d\theta$，立即有
$\langle v\rangle_\phi=1/D$。进一步

$$\frac{\langle A\rangle_\theta}{D}
=\langle Av\rangle_\phi=\langle u^2+Kv^2\rangle_\phi.
$$

真实无源曲率角恒等式 (H.4) 因而成为
$d_\phi=\beta(\langle S\rangle_\phi-S)$。反射使 $d$ 为奇函数，其积分常数
为零，得到 (M.1)。对物理互逆方程作完整链式法则，使用
$v\phi_\theta=1/D=m$，即得 (M.2)。对第二行取平均，周期分部积分给

$$\langle d v_\phi\rangle
=-\beta\langle(\langle S\rangle-S)v\rangle;
$$

它与反应项的 $\langle Sv\rangle$ 准确相消，得到 (M.3)。这里保留了真平均，
并非只检查非零 Fourier 行。

### 反向构造，不预设一个变分逆

反之，给同一径向目标上满足 (M.2) 的足够正则、四重奇偶场 $u,v$，且 $v<0$，
直接定义

$$\theta(r,\phi)=\frac1{m(r)}\int_0^\phi v(r,s)\,ds.
\tag{M.4}$$

于是 $\theta_\phi=v/m>0$，周期增量为 $\pi/2$，$\theta(r,0)=0$。由
(M.2)–(M.3)，先对 $\theta_\phi$ 求径向导数，再用原点处 $u=d=0$，得

$$\theta_r=-\gamma u+(d/m)v.\tag{M.5}$$

所以这是整个圆上与径向变化相容的真实角图。把 $u,v$ 按其逆复合回物理角，
完整链式法则恢复原 (H.6)。定义

$$C=1/v,\qquad B=u/v,\qquad A=Kv+u^2/v,$$

则 $AC-B^2=K$ 且两条 Codazzi 方程准确成立。这个反向构造不依赖旧固定
中心图下 $h\mapsto h-\delta\phi\,\widehat q_\phi$ 的可逆性。局部标架积分、
全局 holonomy、真正闭帽及固定握持条件仍按原任务逐项支付。

## 2. 近似中心的完整残差变换

这一简化不能以近似中心已解方程为前提。设原物理中心在 (H.6) 的两个残差
为 $r_u,r_v$，正号约定为“径向导数减右端”。仍按其实际 $C/D$ 定义曲率角。
记它搬入 $\phi$ 后的场为 $\widehat q=(u,v)$。实际坐标漂移与 (M.1) 的差为

$$e=I\left(\frac{r_v}{v}\right),\qquad
e_\phi=\frac{r_v}{v}-\left\langle\frac{r_v}{v}\right\rangle_\phi.
\tag{M.6}$$

确实，原 $R_C=-r_v/v^2$，所以
$\langle R_C\rangle_\theta/D=-\langle r_v/v\rangle_\phi$，完整残差版 (H.4)
正好给 (M.6)。反射仍固定零积分常数。因此新系统的完整中心残差是

$$\boxed{f_{\rm centre}=(r_u,r_v)+e(u_\phi,v_\phi).}\tag{M.7}$$

没有删除 $R_C$、其平均或由坐标径向导数产生的项。若 $|v|\ge g>0$，四重
原函数的完整 $L^2$ 范数满足

$$\|e\|_2\le\tfrac14\|r_v/v\|_2\le\|r_v\|_2/(4g).\tag{M.8}$$

该式在 turning 处也没有 $1/K$。若要使用下文负型能量，则逐项用该能量中的
实际 $u_\phi,v_\phi$ 付 (M.7)；不能把新残差直接等同于旧的两个多项式残差。

## 3. 完整 moving-chart 线性化

在固定真实目标上，对 (M.2) 的 moving-chart 未知量作变分
$h=(\xi,\zeta)$，令

$$z=\langle\zeta\rangle_\phi,\qquad
T_h=2u\xi+2Kv\zeta,\qquad \dot d=-\beta I T_h.$$

完整线性系统为

$$h_r=[dI+\gamma mJ(K)]h_\phi+L_0h+Nh+f,
\qquad J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},\tag{M.9}$$

$$L_0=\begin{pmatrix}
-\beta(1+3u^2+Kv^2)&-2\beta Kuv\\
-2\beta uv&\beta(1-u^2-3Kv^2)
\end{pmatrix},\tag{M.10}$$

$$Nh=\dot d\binom{u_\phi}{v_\phi}
+\gamma z\binom{K v_\phi}{-u_\phi}.\tag{M.11}$$

这是对完整非线性式逐项微分的结果；没有投影掉某个高模或平均列。
原固定中心图中的裸 $\gamma u_\theta$ 不再出现在局部矩阵，但其作用不能
被称为免费消失：实际角导仍在 (M.11) 的非局部项与平均项中，必须完整估计。

对第二行取平均，等价地微分 (M.3)，得到

$$z_r=\beta(1-\langle S\rangle)z
-\beta m\langle T_h\rangle+\langle f_2\rangle.\tag{M.12}$$

这给实际平均列的一个独立可用演化方程。只有当真实边界资料规定相应平均
输入为零时，才能取 $z(r_0)=0$；本定理不自行作这个设定。

### 度量参数列仍是完整源

对当前 $a$ 不变的 $E_\nu=E e^{\nu h_0}$ 家族，$\dot\beta=0$，
$\dot\gamma=(h_0/2)\gamma\dot\nu$，$\dot K$ 按真实目标公式求取。除了
(M.9) 的状态变分外，实际参数源为

$$\begin{aligned}
f_\nu={}&-\beta I(\dot K v^2)\binom{u_\phi}{v_\phi}
+\dot\gamma m\binom{K v_\phi}{-u_\phi}
+\gamma m\binom{\dot K v_\phi}{0}\\
&-\beta\dot K\binom{uv^2}{v^3}.
\end{aligned}\tag{M.13}$$

这里 $I$ 本来就保留零均值投影；参数源的真平均仍通过 (M.12) 的
$\langle f_2\rangle$ 进入，未另设成零。

## 4. 负型区间的二维正比较系统

只在 $K<0$、与0分离的闭区间上写 $q=\sqrt{-K}$，令

$$\mathcal E=\bigl\langle|\xi|^2+q^2|\zeta|^2\bigr\rangle^{1/2},
\quad M=|z|,\quad
R=\|\sqrt{u^2+q^2v^2}\|_\infty,\quad
L=\|\sqrt{u_\phi^2+q^2v_\phi^2}\|_\infty.$$

矩阵 $H=\operatorname{diag}(1,-K)$ 对称化主部，且
$(L_0)_{12}=K(L_0)_{21}$，所以能量中的局部非对角项准确相消。
两个实际能量对角是

$$\begin{aligned}
G_1&=-\beta(1+3u^2+Kv^2)-\tfrac12d_\phi,\\
G_2&=\beta(1-u^2-3Kv^2)+\frac{K'}{2K}-\tfrac12d_\phi.
\end{aligned}\tag{M.14}$$

四重原函数的完整 $L^2$ 算子范数为 $1/4$，而
$\|T_h\|_2\le2R\mathcal E$。故 (M.11) 的两项分别不超过
$|\beta|RL\mathcal E/2$ 与 $\gamma qLM$。完整 ordinary source 记为
$F=\|H^{1/2}f\|_2$，则右上导数意义下有

$$\frac d{dr}\binom{\mathcal E}{M}
\le
\begin{pmatrix}g&\gamma qL\\2|\beta m|R&c\end{pmatrix}
\binom{\mathcal E}{M}+\binom F{F/q},\tag{M.15}$$

其中

$$g=\max_\phi\{G_1,G_2\}+|\beta|RL/2,
\qquad c=\beta(1-\langle S\rangle).$$

不要求两个对角非负；非对角确为非负，所以该有限二维比较方程的传播矩阵
保持正锥。按常系数闭盒上界逐段指数化即可给整个无限维 Cauchy/source 算子
的显式上界。反向使用 $\max\{-G_1,-G_2\}+|\beta|RL/2$ 与 $-c$，其余绝对值
项保留。可以把初始真平均 $M_0$ 独立输入；需要单一完整能量增益时使用
$M_0\le\mathcal E_0/q(r_0)$，不能将它直接丢弃。

对全部同奇偶类 $L^2$ 初值与 $L^1_rL^2_\phi$ 源，先沿真实特征流处理主部。
局部矩阵和 (M.11) 都是有界零阶或有界非局部算子；原函数范数已经支付。
短区间 Volterra 收缩、(M.15) 和有限拼接给完整唯一 Cauchy 解。这里所有
允许 Fourier 模都同时存在，并不是一个有限频率求解结论。

## 5. 真实分片中心的接缝

新的未知函数直接定义在共同的计算圆 $\phi$ 上。若用原物理角保存的分片
中心，则每侧必须实际变换为

$$\widehat q_\pm(\varphi)
=q^{\rm phys}_\pm\bigl(\phi_\pm^{-1}(\varphi)\bigr).\tag{M.16}$$

所以修正的真实仿射跳是 $j=-[\widehat q]$，两侧使用同一个 $\varphi$。
原物理中心的微小跳、两个角图的差和逆复合都在 (M.16) 中，不是一个免费零
跳。对于同一连续目标 $K$，moving-chart 线性场的齐次接口是同一圆上连续，
加入实际跳后比较向量增加

$$\binom{\|H^{1/2}j\|_2}{|\langle j_2\rangle|}.\tag{M.17}$$

这与原固定物理变分的 (H.16) 是不同未知量的合同；不能混用两者的接口，或
把旧图下的跳范数直接转授为 (M.17)。

## 6. 已得到什么、下一步实际要付什么

当 $\beta=0$ 时，反射类有 $d=0$、$m_r=0$；固定真平均后的完整非线性系统
确为径向线性波型/混合型系统。这是上述准确等价式的直接特例，说明本次
重写把非线性的实际来源单独显现出来。

当前真实 $\beta$ 并非零。必须在同一保存中心上严格支付 $m,R,L,G_1,G_2$、
二维传播、(M.7) 的真实残差和 (M.16) 的实际接缝，才有新的数值 Cauchy 常数。
本篇没有提前声称它小于此前1493的界。完整 turning、正帽两迹、实际返回
小除数及非线性后验收敛也仍须继续完成。
