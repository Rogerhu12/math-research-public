# R133：新主体的真实曲率角、完整主部及无高角导的漂移恒等式

**已证明（准确结构定理，适用于真实解及保留残差的近似中心）。**
对径向目标 $g=E(r)dr^2+a(r)^2d\theta^2$，设 $K=K(r)$、
$\gamma=\sqrt E/a$、$\beta=a'/a$，在一段上给 $C<0$ 的真实实周期场
$B,C$。不先假定它满足 Gauss–Codazzi。令

$$
u=B/C,\quad v=1/C,\quad A=(K+B^2)/C,
\quad D(r)=\langle C(r,\cdot)\rangle<0,
$$
$$
R_C=C_r-\gamma B_\theta-\beta(A-C).
\tag{H.1}
$$

这里 $C_r$ 是径向导数；本篇的旋转参考如出现则写 $C_{\rm ref}$，避免混淆。
记角平均为 $\langle\cdot\rangle$，$\partial_\theta^{-1}$ 是 mean-zero 周期原函数。
准确角坐标

$$
\phi(r,\theta)=\theta+\frac1{D(r)}\partial_\theta^{-1}(C-D),
\qquad \phi_\theta=C/D>0
\tag{H.2}
$$

把互逆 Codazzi 线性化的整个非对角主系数化为纯径向系数。同时其共同漂移满足
保留实际残差的恒等式

$$
\begin{aligned}
d={}&\frac{\gamma\langle B\rangle}{D}
-\frac\beta D\partial_\theta^{-1}
 \left(A-\frac{\langle A\rangle}{D}C\right)\\
&-\frac1D\partial_\theta^{-1}
 \left(R_C-\frac{\langle R_C\rangle}{D}C\right),
\end{aligned}
\tag{H.3}
$$

$$
d_\phi=
\beta\left(\frac{\langle A\rangle}{D}-\frac AC\right)
+\frac{\langle R_C\rangle}{D}-\frac{R_C}{C}.
\tag{H.4}
$$

右边的函数按 $\theta=\theta(r,\phi)$ 复合。这些式子对近似中心准确成立；
不能在中心仍有残差时删除最后一行或最后两项。特别地，(H.4) 没有任何高角导。

## 1. 全圆坐标与漂移的完整推导

因 $D<0$、$C<0$，(H.2) 的导数严格正。其周期增量为 $2\pi$；若场四重，
增量同时满足 $\phi(\theta+\pi/2)=\phi(\theta)+\pi/2$。故它是整个圆的
定向保持度1微分同胚，不是一个局部角图。平移常数已由原函数 mean-zero
归一固定，没有另删平均端口。

写 $P=\partial_\theta^{-1}(C-D)$。由 (H.1)，

$$
D_r=\beta(\langle A\rangle-D)+\langle R_C\rangle,
$$
$$
P_r=\gamma(B-\langle B\rangle)
 +\beta\bigl[\partial_\theta^{-1}(A-\langle A\rangle)-P\bigr]
 +\partial_\theta^{-1}(R_C-\langle R_C\rangle).
\tag{H.5}
$$

因此 $\phi_r=P_r/D-PD_r/D^2$。从完整角变换中得到的共同主系数为
$d=\gamma B/D-\phi_r$。代入 (H.5)，所有裸 $B-\langle B\rangle$ 项以及
$\beta P/D$ 项准确相消，得到 (H.3)。两个原函数的输入本来就具有零均值，
这不是把原系统的 mean 方程丢掉。

直接对 $d$ 求 $\phi$ 导数，利用 $\partial_\phi=(D/C)\partial_\theta$，得

$$
d_\phi=\frac{\gamma B_\theta}{C}-\frac{C_r}{C}+\frac{D_r}{D}.
$$

再代入 (H.1)、(H.5) 即为 (H.4)。由 $A/C=u^2+Kv^2$，其主要角依赖
只是一项二次多项式。若互逆残差为

$$r_v=v_r-\{\gamma(uv_\theta-vu_\theta)+\beta v(1-u^2-Kv^2)\},$$

则准确 $R_C=-r_v/v^2$，故 $R_C/C=-r_v/v$。因此新的完整多项式残差
可以直接付入漂移；不需要另对残差求角导。

共同反射 $B$ 奇、$C$ 偶给 $\langle B\rangle=0$，且 $d$ 在曲率角中为奇函数。
这保留了真实反射恒等式，但不意味着两支完整回归已经是常数平移。

## 2. 完整线性化，不遗漏 mean 或参数源

在固定目标 $K,\gamma,\beta$ 上，互逆方程为

$$
\begin{aligned}
u_r&=\gamma(uu_\theta+Kv v_\theta)-\beta u(1+u^2+Kv^2),\\
v_r&=\gamma(uv_\theta-vu_\theta)+\beta v(1-u^2-Kv^2).
\end{aligned}
\tag{H.6}
$$

其整个线性化 $h=(\xi,\zeta)^T$ 满足

$$
h_r=\gamma\left[uI+vJ(K)\right]h_\theta+Lh+f,
\qquad J(K)=\begin{pmatrix}0&K\\-1&0\end{pmatrix},
\tag{H.7}
$$

$$
L=\begin{pmatrix}
\gamma u_\theta-\beta(1+3u^2+Kv^2)&
K(\gamma v_\theta-2\beta uv)\\
\gamma v_\theta-2\beta uv&
-\gamma u_\theta+\beta(1-u^2-3Kv^2)
\end{pmatrix}.
\tag{H.8}
$$

式 (H.8) 只是逐项微分 (H.6)，不使用中心是 PDE 解的假设。
将 $\widetilde h(r,\phi)=h(r,\theta(r,\phi))$，链式法则给

$$
\widetilde h_r=
\left[dI+\frac\gamma D J(K)\right]\widetilde h_\phi
+\widetilde L\widetilde h+\widetilde f.
\tag{H.9}
$$

因为 $v\phi_\theta=(1/C)(C/D)=1/D$，非对角主项确为径向函数。
这是固定中心坐标中的整个线性系统，不是仅主符号的近似。

若还保留 $\nu$、振幅或其他真实度量参数列，它们进入完整 $f$ 中；不能在
应用 (H.9) 时删除原有限系统保留的参数或 mean 行。这里的 $\phi$ 由固定
中心选定，线性未知量的变化不会被偷偷重复计为坐标变化。

## 3. 严格负段的完整能量恒等式

在 $K<0$ 的闭子段上令 $H=\operatorname{diag}(1,-K)$。矩阵
$H[dI+(\gamma/D)J(K)]$ 对称。更强地，(H.8) 有准确关系
$L_{12}=KL_{21}$，因此 $\operatorname{Sym}(HL)$ 的非对角元全部为零。
对真实或复数完整角场定义

$$
\mathcal E(r)=\int_{\mathbb S^1}
 (|\widetilde\xi|^2-K|\widetilde\zeta|^2)\,d\phi.
\tag{H.10}
$$

没有任何 Fourier 截断；mean 也在积分中。周期分部积分直接给

$$
\frac12\mathcal E'
=\int\left[
\left(L_{11}-\frac12d_\phi\right)|\widetilde\xi|^2
 +(-K)\left(L_{22}+\frac{K'}{2K}-\frac12d_\phi\right)
 |\widetilde\zeta|^2\right]d\phi
+\Re\int\widetilde h^*H\widetilde f\,d\phi.
\tag{H.11}
$$

所以若两项实系数都不超过 $G(r)$，则

$$
\frac d{dr}\sqrt{\mathcal E}
\le G(r)\sqrt{\mathcal E}+\|H^{1/2}\widetilde f\|_{L^2(d\phi)}.
\tag{H.12}
$$

在 $\mathcal E=0$ 处取通常的右上导数解释。推导中原本可能很大的
$v_\theta$ 耦合准确相消；仍然保留 $\pm\gamma u_\theta$、真实 $\beta$ 项和
$K'/(2K)$，不把后者的符号擅自改成免费的有利项。

按原物理角写，(H.10) 准确为

$$\mathcal E=\int(C/D)(|\xi|^2-K|\zeta|^2)\,d\theta.$$

因此所有归一及角 Jacobian 都明确保留。该能量在 $K\to0$ 退化；本篇没有
据此越过 turning，或把严格负段能量称为整个 mixed body 的逆。

## 4. 真正主射线与回归的全频合同

令 $k=\sqrt{-K}$、$\omega=-\gamma k/D>0$。在严格负段，(H.9) 主特征值
为 $d\pm\omega$。定义两支主射线流

$$
\frac{d\phi_+}{dr}=-d(r,\phi_+)+\omega(r),\qquad
\frac{d\phi_-}{dr}=-d(r,\phi_-)-\omega(r).
\tag{H.13}
$$

其准确角导满足

$$\frac d{dr}\log\partial_{\phi_0}\Phi_\pm
=-d_\phi(r,\Phi_\pm).$$

所以对 $I=[r_0,r_1]$，若 $L_d=\int_I\|d_\phi\|_\infty dr<\infty$，则
两流均为整个圆的定向保持同胚，导数在 $[e^{-L_d},e^{L_d}]$ 中。完整
主回归定义为

$$\mathcal R=\Phi_-^{-1}\circ\Phi_+.
\tag{H.14}$$

其导数在 $[e^{-2L_d},e^{2L_d}]$ 中。若
$\Omega=\int_I\omega dr$、$D_d=\int_I\|d\|_\infty dr$，则对同一 lift

$$|\mathcal R(\phi)-\phi-2\Omega|\le2D_d.
\tag{H.15}$$

证明只需对 (H.13) 积分：正向 $+$ 和反向 $-$ 都贡献 $+\Omega$，每段的
共同漂移贡献绝对值至多 $D_d$。若 $K$ 在 $r_1$ 简单趋于0且其他量保持
上述有界性，主流仍有极限；但系统本身的 turning 连接还需要完整 Airy/端口
分析，不能从主流存在推出。

对于四重 Wiener 范数，mean-zero 原函数满足
$\|\partial_\theta^{-1}f\|_{A_s}\le\frac14\|f\|_{A_s}$。故 (H.3) 中漂移与
候选残差的整个 $A_s$ 费用可直接由该系数消费，mean 补偿项仍完整保留。
复角宽、坐标逆的解析宽和真实回归小除数仍须另证；本篇没有用有限射线采样
证明 Diophantine 条件。

## 5. 分片准确中心的真实接缝

若中心来自准确 dyadic PPoly，不可假设其跨每个保存接口恰好连续。
(H.1)–(H.12) 先分别用于每个光滑片。设接口两侧曲率角为 $\phi_-,\phi_+$，
则任何原物理角下连续的线性场都必须满足

$$
\widetilde h_+(\varphi)=
\widetilde h_-\bigl(\phi_-\circ\phi_+^{-1}(\varphi)\bigr).
\tag{H.16}
$$

若实际修正对中心有给定物理跳 $j(\theta)$，则右边再加
$j\circ\phi_+^{-1}$；例如为抵消中心跳时 $j=-[\widehat x]$。
不能把这条准确坐标接合换成零接合，也不能把 $[C]\delta_{r_i}$ 与不连续的
$1/D$ 无定义地相乘后声称得到了全局 (H.3)。先在各真片做源与能量，再用
(H.16) 连接，才是完整分片主回归。

## 6. 本结构在当前任务中的范围

本篇适用于新的实际 $\nu$ 目标及同一目标上的任何 $C<0$ 中心，因而不依赖
旧 type-fixed 对象的返回常数。它提供可消费的全频主部和 residual 合同。
真正全逆尚需：同一主体的完整系数/坐标预算、真实 turning 到正帽的两迹连接、
全回归的适当平均与小除数条件，以及保参数的非线性后验闭合。

独立浮点生产器
`scripts/fourfold_codazzi_curvature_angle_return_probe.py`
读取全部候选系数，直接沿原物理角积分 (H.13) 等价的两支流，并输出曲率角
共轭后的主回归。该程序的图、经验旋转数及步长控制都明确标为浮点诊断；
不作为本定理的严格数值常数，也不代替完整 turning/scattering 算子。
