# R239. 材料切口的均值唯一性与共同平面配准

2026-11-14，exact_refinement，AI 辅助。

**状态：已证明的条件引理；当前候选的连续假设尚未核销。** 本文解释完整材料高度和全部非均值径向斜率为何在适当正分支上可决定均值，并给出一个共同平面刚体配准及二阶接缝的充分条件。本文不把有限 Fourier 行、有限角网格或主法向投影器等同于这些连续假设，也不宣布新候选已经闭合。

## 1. 切口、方向与源码归一化

在固定切口 $r=r_0>0$ 附近，采用相同的材料角 $\theta\in\mathbb R/(2\pi\mathbb Z)$ 和相同的径向坐标。给定旋转度量

$$g=E(r)\,dr^2+r^2\,d\theta^2,\qquad E(r_0)=E_0>1,\qquad w_0=\sqrt{E_0-1}>0.\tag{239.1}$$

先把真实物理高度按选定的固定符号反射到 native 高度 $z$；上半片现有约定是 $z=-Z+\text{常数}$。下文所有 $z_r$ 都是同一个增加 $r$ 的坐标导数，不把 $s$ 向导数直接代入。若 $r=a(s)$，则

$$z_r=\frac{z_s}{a_s},\qquad z_{rr}=\frac{z_{ss}}{a_s^2}-\frac{a_{ss}z_s}{a_s^3}.\tag{239.2}$$

固定切口的完整周期高度 $h(\theta)=z(r_0,\theta)$。允许加一个常数高度平移，但先把这个常数对齐。设

$$W(\theta)=z_r(r_0,\theta)=b+\widetilde W(\theta),\qquad \langle\widetilde W\rangle=0,\qquad \langle f\rangle=\frac1{2\pi}\int_0^{2\pi}f(\theta)\,d\theta.\tag{239.3}$$

这里 $b=\langle z_r\rangle$ 是物理径向斜率均值。为与现有 native 引擎准确对应，定义

$$P=\frac{h_\theta}{r_0w_0},\quad K=\frac{W}{w_0}-1=k_0+\widetilde K,\quad k_0=\frac b{w_0}-1,\quad \widetilde K=\frac{\widetilde W}{w_0}.\tag{239.4}$$

$k_0$ 是相对斜率均值；不是物理高度均值。再记

$$\begin{aligned}
S&=1-w_0^2P^2,\\
T&=2K+K^2+E_0P^2,\\
D&=1-w_0^2T=E_0S-w_0^2(1+K)^2,\\
A&=1+K+E_0P_\theta.
\end{aligned}\tag{239.5}$$

这些量正是 `general_exact_tail_cauchy.mjs` 的 `angles`/`meanRoot` 及 `78718-tail-fourier-root-momentum.mjs` 的 `evaluateL` 所用的量。后者写 $L=K+P_\theta$，故 $A=1+L+w_0^2P_\theta$，而 $\langle L\rangle=\langle K\rangle=k_0$。非均值 cosine 的正交归一化不改变这一均值等式。

本引理的正分支是**全部连续角度**上的

$$S>0,\qquad D>0,\qquad A>0.\tag{239.6}$$

源码的有限网格 `D/S/A > projectionFloor` 是该条件的离散检查，并不自行证明 (239.6)。本文也不由 (239.6) 默认为平面投影 turning number 等于 $1$；该整数必须来自实际闭投影、连续延拓或另一个已证明的几何条件。

## 2. 平面投影的准确转角公式

设 $F=(u,z)$ 是在切口附近的精确等距浸入，$u=(X,Y)$ 是水平投影。切口上令

$$v=|u_\theta|=r_0\sqrt S,\qquad \mathsf T=\frac{u_\theta}{v},\qquad \mathsf N=J\mathsf T,\quad J(x,y)=(-y,x).\tag{239.7}$$

取现有圆形 native 背景的平面方向，即

$$u_r=\alpha\mathsf T+\beta\mathsf N,\qquad
\alpha=-\frac{z_rz_\theta}{v},\qquad
\beta=-\frac{\sqrt D}{\sqrt S}<0.\tag{239.8}$$

圆形参考 $u=(r\cos\theta,r\sin\theta)$ 确实有 $\mathsf T=(-\sin\theta,\cos\theta)$、$\mathsf N=(-\cos\theta,-\sin\theta)$、$\beta=-1$。若另一块采用相反平面方向，不能直接套用同一个 $\mathrm{SE}(2)$ 配准结论；须先明确允许的反射及其对整体方向的影响。

在角度的通用覆盖上写 $\mathsf T=(\cos\psi,\sin\psi)$。由

$$\partial_ru_\theta=\partial_\theta u_r$$

的 $\mathsf T$ 分量，得到

$$v_r=\alpha_\theta-\beta\psi_\theta,\qquad
\psi_\theta=\frac{\alpha_\theta-v_r}{\beta}.\tag{239.9}$$

这个公式只用一、二阶切口导数，不需要预先知道 $z_{rr}$。为检查所有 $r_0$ 因子，先用物理量

$$p=\frac{h_\theta}{r_0}=w_0P,\qquad W=b+\widetilde W=w_0(1+K),\qquad S=1-p^2,\qquad D=E_0(1-p^2)-W^2.\tag{239.10}$$

于是

$$v_r=\frac{1-pW_\theta}{\sqrt S},\qquad
\alpha=-\frac{Wp}{\sqrt S},\qquad
\alpha_\theta-v_r=-\frac{S+Wp_\theta}{S^{3/2}}.
$$

代入 (239.8) 可得

$$\boxed{\displaystyle
\psi_\theta=\frac{S+Wp_\theta}{S\sqrt D}
=\frac1{\sqrt D}+\frac{w_0^2(1+K)P_\theta}{S\sqrt D}.}\tag{239.11}$$

其中 $p_\theta=h_{\theta\theta}/r_0$；没有把物理 $h_{\theta\theta}$ 错当成 $p_\theta$。若一般地取 $\beta=\sigma\sqrt D/\sqrt S$，则 (239.11) 的右侧整体乘 $-\sigma$。本文后续均固定 $\sigma=-1$。

若实际切口的平面投影闭合且正则，$\psi(2\pi)-\psi(0)=2\pi\nu$，其中整数 $\nu$ 是它实际的 turning number。因此

$$\langle\psi_\theta\rangle=\nu.\tag{239.12}$$

闭合本身不保证 $\nu=1$。例如，可以由一条已知正向严格凸的单周闭曲线出发，并证明整个延拓中 $u_\theta$ 从不为零；连续切向映射的次数不变才得到 $\nu=1$。若直接使用正曲率判据，还须核实单周、方向与闭合，而不能仅据若干正曲率样本作结论。

## 3. 与源码完全一致的均值残差及其导数

对固定的完整 $P$、$\widetilde K$，把 $k_0$ 当作唯一变量，定义

$$G(k_0)=\left\langle
\frac{T}{\sqrt D(1+\sqrt D)}+
\frac{(1+K)P_\theta}{S\sqrt D}
\right\rangle.\tag{239.13}$$

这是 `general_exact_tail_cauchy.mjs::meanRoot` 的连续版本；其有限网格代码以 $N^{-1}\sum$ 代替 $\langle\cdot\rangle$。利用 $1-D=w_0^2T$，(239.11) 给出

$$G(k_0)=\frac{\langle\psi_\theta\rangle-1}{w_0^2}
=\frac{\nu-1}{w_0^2}\quad\text{对实际闭投影}.\tag{239.14}$$

所以源码的均值方程 $G=0$ 选择的是 turning number $1$ 的分支。若两个实际切口具有同一个其他 turning number，它们的 $G$ 仍相同，但不能称它们满足源码的 $G=0$ 方程。

现在求导。由于 $S,P,P_\theta$ 对 $k_0$ 固定，$K_{k_0}=1$，直接化简得到

$$\begin{aligned}
\partial_{k_0}\frac{T}{\sqrt D(1+\sqrt D)}
&=\frac{1+K}{D^{3/2}},\\
\partial_{k_0}\frac{(1+K)P_\theta}{S\sqrt D}
&=\frac{E_0P_\theta}{D^{3/2}}.
\end{aligned}
$$

因此

$$\boxed{\displaystyle G'(k_0)=\left\langle\frac{A}{D^{3/2}}\right\rangle>0.}\tag{239.15}$$

这也与源码 `meanRoot` 中逐角累加的 `df += A/(D*sqrt(D))` 一致。Fourier root 的 `evaluateL` 把同一均值残差稳定改写为 `moments[0]=L[0]+quad[0]`；其均值 Newton 矩阵元 `B[0]` 也是同一个离散平均。该改写没有新增 $r_0$ 或 $w_0$ 因子。

若改用物理斜率均值 $b=w_0(1+k_0)$，以及未归一化总转角
$\tau(b)=\int_0^{2\pi}\psi_\theta\,d\theta$，准确换算是

$$\boxed{\begin{aligned}
\frac{dG}{db}&=\frac1{w_0}\left\langle\frac{A}{D^{3/2}}\right\rangle,\\
\frac{d\nu}{db}&=w_0\left\langle\frac{A}{D^{3/2}}\right\rangle,\\
\frac{d\tau}{db}&=2\pi w_0\left\langle\frac{A}{D^{3/2}}\right\rangle
=\int_0^{2\pi}
\frac{b+\widetilde W+(E_0/r_0)h_{\theta\theta}}
{\bigl[E_0(1-h_\theta^2/r_0^2)-(b+\widetilde W)^2\bigr]^{3/2}}\,d\theta.
\end{aligned}}\tag{239.16}$$

中间的 $\nu$ 在比较非闭合的假设均值时表示实数 $\langle\psi_\theta\rangle$，只有在实际闭投影上才是整数。最后一式明确显示物理归一化中的全部 $r_0$ 因子。若用弧长坐标斜率均值代替 $b$，还须按 (239.2) 乘对应的固定 $a_s$，不能省略方向符号。

## 4. 正分支上的均值唯一性

**引理 239-A。** 两个切口具有同一 $r_0,E_0$、同一完整 $h$、同一完整非均值 $\widetilde W$、同一方向 (239.8)，并且实际闭平面投影具有同一 turning number。若两者连续地满足 (239.6)，则它们的均值 $b$ 相同。

**证明。** 设两个均值对应 $k_0^{(0)},k_0^{(1)}$。$S$ 与均值无关。对每个固定 $\theta$，$A$ 关于 $k_0$ 仿射，故两个端点的 $A>0$ 推出整个均值线段上的 $A>0$。同时

$$D(k_0,\theta)=E_0S(\theta)-w_0^2\bigl(1+k_0+\widetilde K(\theta)\bigr)^2
$$

是 $k_0$ 的凹二次函数。因而端点 $D>0$ 推出整个线段 $D>0$。这证明插值没有离开正分支；不是把只在端点做过的数值检查误作中间检查。

等价地，对每个角度，$D>0$ 定义一个均值开区间，$A>0$ 定义一个半直线。所有角度的交仍是区间。连续函数在紧角域及闭均值线段上的严格正性还给出统一的正下界。

由同一 turning number 和 (239.14)，$G(k_0^{(0)})=G(k_0^{(1)})$。但 (239.15) 在该线段上严格为正，所以两个均值相同。证毕。

因此，对一个已证明 turning number 为 $1$ 的精确切口，只要完整非均值 native DN 斜率与正分支均值根共享上述条件，就不必另给一个独立的均值自由度。这个结论的前提包括**完整连续非均值函数相同**，不包括“前 $T$ 项一致但剩余模式未经控制”。

还有一个条件定量版。若均值线段上已证明 $A\ge a_*>0$、$D\le d^*$，则中值定理给出

$$|b_1-b_0|\le\frac{w_0(d^*)^{3/2}}{a_*}\,|G(k_1)-G(k_0)|
=\frac{(d^*)^{3/2}}{2\pi w_0a_*}\,|\tau(b_1)-\tau(b_0)|.\tag{239.17}$$

可以取 $d^*=E_0$，因为 $D=E_0S-W^2\le E_0$。若 $P$ 或非均值 $\widetilde W$ 也有误差，则还须支付这些函数变化对 $G$ 的影响；(239.17) 不能直接用于两组不同截频输入。积分误差、角截断尾和连续正性也都必须另行控制。

## 5. 一个共同平面刚体决定整条切口及一阶 jet

**引理 239-B。** 假设两个精确等距切口已经具有完全相同的 $h$ 和完整 $W=z_r$，并满足 $S,D>0$ 及同一方向 (239.8)。则存在一个与 $\theta$ 无关的 $Q\in\mathrm{SO}(2)$、$c\in\mathbb R^2$，使

$$u^{(1)}(\theta)=Q u^{(0)}(\theta)+c,\qquad
u_r^{(1)}(\theta)=Q u_r^{(0)}(\theta).\tag{239.18}$$

**证明。** 同一 $h,W,g$ 给出相同的 $v,\alpha,\beta$ 和 (239.9) 的同一 $\psi_\theta$。两个单位切向的角度在通用覆盖上只差一个常数，故存在固定 $Q\in\mathrm{SO}(2)$ 使 $\mathsf T^{(1)}=Q\mathsf T^{(0)}$，也有 $\mathsf N^{(1)}=Q\mathsf N^{(0)}$。于是 $u_\theta^{(1)}=Q u_\theta^{(0)}$；积分给出一个固定平移 $c$。再用同一 $\alpha,\beta$ 即得径向导数的等式。证毕。

这不是对不同角度独立拟合旋转和平移。取一个点的位置和水平切向即可固定同一个配准；两条完整曲线之后必须满足 (239.18)。切口闭合也随该固定配准继承。高度均值已经在第1节用一个固定竖直平移对齐。

该引理只处理某一切口的局部装配。若要对整族使用随 $t$ 选择的配准，还须证明其连续性/所需正则性，并核对点态固定的 $H$ 和统一世界坐标系；本引理不自动支付全族 clamping。

## 6. 同一非特征 Darboux 分支何时决定二阶 jet

设两侧还有同一个 $E'_0=E'(r_0)$，并且各自的二阶高度 jet 满足该固定度量的 Darboux 恒等式

$$\left(z_{rr}-\frac{E'_0}{2E_0}z_r\right)
\left(z_{\theta\theta}+\frac{r_0}{E_0}z_r\right)
-\left(z_{r\theta}-\frac{z_\theta}{r_0}\right)^2
=\frac{r_0E'_0}{2E_0^2}\,D.\tag{239.19}$$

这个等式对足够光滑的精确等距浸入由 Gauss 方程得到：$K_g=E'_0/(2r_0E_0^2)$，$\det g=E_0r_0^2$，$1-|\nabla z|_g^2=D/E_0$，而 Hessian 的三项正是左侧所列。对于只按 $C^2$ 定义的候选，应由其精确构造或相应的兼容性论证支付 (239.19)，不能从“保存了二阶 jet”推断它成立。有限 Frenet 投影、有限尾计算和物理五次读出一般只给带残差的版本。

在 native 正分支上，径向最高导数的系数为

$$B=z_{\theta\theta}+\frac{r_0}{E_0}z_r
=\frac{r_0w_0}{E_0}\,A>0.\tag{239.20}$$

因而这是一个非特征分支，(239.19) 唯一给出

$$\boxed{\displaystyle z_{rr}=\frac{E'_0}{2E_0}z_r+
\frac{\left(z_{r\theta}-z_\theta/r_0\right)^2+r_0E'_0D/(2E_0^2)}
{z_{\theta\theta}+(r_0/E_0)z_r}.}\tag{239.21}$$

如果完整 $h$ 和 $W$ 相同，它们的所需角导数相同；于是 (239.21) 强迫 $z_{rr}$ 相同。这里要匹配真实 $E'_0$，不能只匹配 $E_0$。若 (239.20) 退化，就不能使用这个唯一性推论。

在第5节的共同平面配准后，$u,u_r,u_\theta$ 已相同。对整条切口的恒等式求角导数，给出 $u_{\theta\theta}$ 与 $u_{r\theta}$ 相同。最后，平面诱导度量满足

$$|u_r|^2=E_0-z_r^2,\qquad u_r\cdot u_\theta=-z_rz_\theta.
$$

径向求导得到决定 $u_{rr}$ 的两个线性方程

$$\begin{aligned}
u_r\cdot u_{rr}&=\frac{E'_0}{2}-z_rz_{rr},\\
u_\theta\cdot u_{rr}&=-z_{rr}z_\theta-z_rz_{r\theta}-u_r\cdot u_{r\theta}.
\end{aligned}\tag{239.22}$$

由于 $D>0$，$u_r,u_\theta$ 线性独立，两个方程唯一决定平面向量 $u_{rr}$。所有右侧已经相同，故两侧的 $u_{rr}$ 也相同。连同高度分量，这证明共同配准后的完整六项

$$F,\quad F_r,\quad F_\theta,\quad F_{rr},\quad F_{r\theta},\quad F_{\theta\theta}\tag{239.23}$$

一致。通过同一 $r=a(s)$ 且 $a_s\ne0$ 的变换，可等价得到物理 $s$ 坐标下的六项一致。

## 7. 当前新候选接口实际得到什么

`exact_20261114_material_tail_packet.py` 对接受的完整 core 先反解

$$\theta=\phi+\sum_{j=1}^M\frac{(1-4j^2)c_j}{2j}\sin(2j\phi),
$$

然后在材料角上计算实际高度和全部物理一、二阶导数。它保留材料均值、完整输入 core、原切口 jet、换角矩阵及核心换角导数，并在 $N=1024,2048,4096$ 上比较多种 tail-mode 预算。其 finite packet 并不假设 $M=96$ 的原法向角多项式在材料角下仍只有 $96$ 项。

`geometry_20261114_full_dn_boundary.py` 的全部非均值 DN 行可以据本引理设计 square BVP，但实际验收仍必须保留并检查 native 响应的 `meanSlope`、`meanSecond`、完整 Cartesian 六 jet、固定 $g$ 与连续/加密残差。实际 native `heightJetJacobian` 的 row-major 布局是

| 行编号（零起） | 输出 |
| --- | --- |
| $0,\ldots,T-1$ | 非均值 slope |
| $T,\ldots,2T-1$ | 非均值 second |
| $2T$ | meanSlopeCorrection |
| $2T+1$ | meanSecondCorrection |
| $2T+2,\ldots,3T+1$ | height |

固定 $g$ 下 `meanSlope = backgroundSlope + meanSlopeCorrection`，背景对高度列为常数，因此第 $2T$ 行也是完整 meanSlope 对 $T$ 个高度列的导数。`numerical-tail-slope-jacobian.mjs` 已把 slope 和这一均值一阶行换为实际 shooting tangent 的解析导数；该事实不把其余 finite-difference 二阶行升级成精确极限。

本引理的连续输入尚未被当前新候选实际核销，具体包括：完整材料角 Fourier 余项、连续正分支、真实闭平面投影及其 turning number、同 $E,E'$ 的实际非线性尾、Darboux/metric 残差、统一配准后的全六 jet、全族闭嵌入、reach 和目标幅度。当前所有截频残差只作为有限诊断。课题保持未完成。

## 源码对应

- [`general_exact_tail_cauchy.mjs`](../../visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/general_exact_tail_cauchy.mjs)：`angles` 中的 $S,D,A$ 和 `meanRoot` 的残差、导数。
- [`78718-tail-fourier-root-momentum.mjs`](../../visible-flexible-closed-surface/scripts/78718-tail-fourier-root-momentum.mjs)：`evaluateL` 的同方程 Fourier-product 均值与 Newton 矩阵。
- [`78718-tail-tangent-core.mjs`](../../visible-flexible-closed-surface/scripts/78718-tail-tangent-core.mjs)：`cutJets` 的完整 meanSlope/meanSecond，以及 `heightJetJacobian` 行序。
- [`numerical-tail-slope-jacobian.mjs`](../computations/numerical-tail-slope-jacobian.mjs)：`actualSlopeJacobian` 与 `replaceFirstSlopeRows` 的实际一阶/均值一阶导数。
- [`exact_20261114_material_tail_packet.py`](../computations/exact_20261114_material_tail_packet.py)：完整材料换角、原物理六 jet 与有限谱预算；没有把本文条件当成已满足。
