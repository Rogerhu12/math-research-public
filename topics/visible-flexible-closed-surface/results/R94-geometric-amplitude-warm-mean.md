# R94：同一度量下的几何振幅暖启动及完整均值修正

状态：**已证明的坐标命题与已接入真实计算的初猜函数。** 在同一个径向度量、同一个节点和相同角频率/求积下，缩放物理 raw 的 $Q$ 与非均值 $L$，再重解均值和投影动量，可精确缩放高度与径向高度的非均值部分。完整径向高度还含一个必须重新计算的均值修正，不能声称整体乘同一比例。正分支也不由缩幅自动保证。

这只准备初猜。真正的 tail DN、最终 H、物理度量、边界条件及成功残差不由本命题改变。作者 Astra-visible-flex-78718bd0，2026-11-10；根指定编号 R94，按根 README §13 直接登记。

## 1. 原坐标与缩幅任务

固定截面 $r>0$、背景斜率 $w>0$、$W=w^2$、$E=1+W$、cell 尺度 $\mu>0$ 和方向 $\varepsilon\in\{-1,1\}$。角频率是 $\ell_j=mj$，令

$$
c_0=1,\quad c_j=\sqrt2\cos(\ell_j\theta),\quad
s_j=\sqrt2\sin(\ell_j\theta)\quad(1\le j\le M).
$$

可用连续角平均，也可用原程序的有限平均
$\langle f\rangle_N=N^{-1}\sum_{n=0}^{N-1}f(2\pi n/N)$。
后者保留原分辨条件 $N>4mM$。以下代数对两种平均都成立；存在性与正分支分别按所用平均解释。实际代码只检查有限角点，并不是全角区间证书。

[R86](R86-geometric-momentum-prolongation.md) 中的原变量是

$$
\begin{aligned}
u-\langle u\rangle&=r^4\sum_{j=1}^M Q_j\cos(\ell_j\theta),\\
P&=-\sum_{j=1}^M\frac{\ell_jr^3Q_j}{w}\sin(\ell_j\theta),
& P_\theta&=-\sum_{j=1}^M\frac{\ell_j^2r^3Q_j}{w}\cos(\ell_j\theta),\\
L&=\lambda_0+\sum_{j=1}^M\lambda_jc_j,\qquad
K=L-P_\theta,&u_r&=w(1+K),\\
S&=1-WP^2,\quad
D=1-W(2K+K^2+EP^2),&A&=1+K+EP_\theta.
\end{aligned}
\tag{1}
$$

角连接及其投影 root 满足

$$
\omega=\frac{1+W(1+K)P_\theta/S}{\sqrt D},\qquad
\left\langle\frac{\omega-1}{W}\right\rangle=0,
\qquad
\left\langle c_j\frac{\omega-1}{W}\right\rangle
=\tau\pi_j,\quad
\tau=\frac{\varepsilon\sqrt{12}\mu}{\sqrt2r^4W}.
\tag{2}
$$

raw 的第二组分量并不是 $\pi$，而是

$$
R_j=\frac{\sqrt2w}{\sqrt{12}r^3}\lambda_j,\qquad 1\le j\le M.
\tag{3}
$$

它不含 $\lambda_0$；均值由式 (2) 第一条 root 方程重新确定。

旧初猜 fallback 同时把 $Q,\pi$ 乘比例 $s$，一般不会把非均值 $u_r$ 精确乘 $s$，因为式 (2) 非线性。本文改用

$$
(Q,R)\longmapsto(sQ,sR)
\longmapsto\text{重解均值、重新投影 }\pi.
\tag{4}
$$

这里 $s>0$；实际半振幅 bootstrap 取 $s=1/2$。

## 2. 完整均值公式

记原 root 为 $L^0=\lambda_0^0+L_*^0$，其中
$L_*^0=\sum_{j=1}^M\lambda_j^0c_j$。
新 raw 数据要求

$$
Q^s=sQ^0,\qquad
\lambda_j^s=s\lambda_j^0\quad(j\ge1).
$$

令重新解出的均值为 $\lambda_0(s)$，并定义

$$
d(s)=\lambda_0(s)-s\lambda_0^0.
\tag{5}
$$

于是完整新场为

$$
P^s=sP^0,\qquad
P_\theta^s=sP_\theta^0,\qquad
L^s=sL^0+d(s),\qquad
K^s=sK^0+d(s).
\tag{6}
$$

**命题。** 若新均值 root 存在于所用正分支，且按式 (2) 重新定义所有 $\pi_j^s$，则

$$
\begin{aligned}
u^s-\langle u^s\rangle
   &=s\bigl(u^0-\langle u^0\rangle\bigr),\\
u_r^s-\langle u_r^s\rangle
   &=s\bigl(u_r^0-\langle u_r^0\rangle\bigr),\\
\boxed{\displaystyle
u_r^s=w+s(u_r^0-w)+wd(s).}
\end{aligned}
\tag{7}
$$

其余角导数由上述式子直接微分：
$u_\theta^s=s u_\theta^0$、
$u_{\theta\theta}^s=s u_{\theta\theta}^0$、
$u_{r\theta}^s=s u_{r\theta}^0$。
平均高度值本身是独立的积分常数，本局部节点函数不替它作全尾位置积分。

**证明。** 第一个等式来自所有 $Q_j$ 同比例缩放。由式 (6)，

$$
u_r^s=w(1+sK^0+d)
=w+s(u_r^0-w)+wd.
$$

最后一项与 $\theta$ 无关，故去掉均值就得第二个等式，角导数也随之成立。按式 (2) 重投影后，指定的完整 $L^s$ 满足新全模 root 的每一条方程；正分支上 root 的唯一性已由 R86 的正定 Jacobian 与凸分支证明，因此它正是新动量状态所表示的物理 jet。证毕。

特别地，除非另证 $d(s)=0$，不能把式 (7) 简化为
$u_r^s-w=s(u_r^0-w)$，更不能把完整 $u_r$ 乘 $s$。

## 3. 均值 root、局部存在性和可用的误差控制

把均值视为独立变量 $z$，令

$$
\mathcal M(s,z)=
\left\langle
\frac{\omega(Q=sQ^0,L=z+sL_*^0)-1}{W}
\right\rangle .
\tag{8}
$$

在 $A,S,D>0$ 分支上，由 R89 的逐项微分或直接微分式 (2)，

$$
\partial_z\mathcal M(s,z)
=\left\langle\frac A{D^{3/2}}\right\rangle>0.
\tag{9}
$$

所以固定 $s$ 的可行均值区间内，root 至多一个。旧状态满足
$\mathcal M(1,\lambda_0^0)=0$，导数非零，故隐函数定理给出
$s=1$ 附近唯一光滑的 $\lambda_0(s)$，仍在原正分支内。
对有限平均这是有限个解析函数的结论；对连续平均，只要给定统一正性裕量，角积分下微分也成立。这个局部结论不宣称 $s$ 从1一直走到任意指定值时分支不会终止。

更明确地，若候选区间
$[s\lambda_0^0-\eta,s\lambda_0^0+\eta]$
完整位于正分支，且

$$
\mathcal M(s,s\lambda_0^0-\eta)\le0
\le\mathcal M(s,s\lambda_0^0+\eta),
\tag{10}
$$

则连续性和严格单调性给出唯一 root，且 $|d(s)|\le\eta$。
也可以在该区间证明 $\partial_z\mathcal M\ge b_*>0$，
令 $\rho=|\mathcal M(s,s\lambda_0^0)|$；若
$\eta\ge\rho/b_*$，两端符号由积分式得到，于是同样得到
$|d(s)|\le\rho/b_*$。
这里必须先确保整个用于积分的区间仍在分支内，不能把导数下界脱离其范围使用。

不存在一般的、未经证明的符号规则
$\lambda_0(s)\ge s\lambda_0^0$。
实际函数直接调用原 mean root，保留原分支和容差，并报告计算出的均值偏移，不假设其符号。

## 4. A、S、D 的精确变化；缩幅不自动支付正性

式 (6) 给出

$$
\boxed{\displaystyle
A^s=1+s(A^0-1)+d(s),\qquad
S^s=1-Ws^2(P^0)^2.}
\tag{11}
$$

完整 $D$ 是

$$
D^s=
1-W\{2(sK^0+d)+(sK^0+d)^2+Es^2(P^0)^2\}.
\tag{12}
$$

若希望看清均值修正的作用，将其展开为

$$
\begin{aligned}
D^s={}&(1-s)+sD^0
+Ws(1-s)\{(K^0)^2+E(P^0)^2\}\\
&-W\{2(1+sK^0)d+d^2\}.
\end{aligned}
\tag{13}
$$

因此当 $0\le s\le1$ 时，保持完整 $L$ 线性缩放的部分具有良好凸性，但重新解出的 $d(s)$ 仍可能改变 $A,D$。不能从未消去均值的凸域，直接推断消去均值后的 raw 数据域全局凸。

例如若旧截面满足
$A^0\ge a_0>0$、$D^0\ge d_0>0$、$S^0\ge q_0>0$，
并已知 $|K^0|\le K_*$、$|d(s)|\le\eta$，
则对 $0\le s\le1$ 有条件下界

$$
\begin{aligned}
A^s&\ge1+s(a_0-1)-\eta,\\
S^s&\ge(1-s)+sq_0,\\
D^s&\ge(1-s)+sd_0
-W\{2(1+sK_*)\eta+\eta^2\}.
\end{aligned}
\tag{14}
$$

第一式来自式 (11)，第二式用
$S^s=(1-s)+sS^0+Ws(1-s)(P^0)^2$，
第三式由式 (13) 丢弃非负项并取绝对值得到。
这些是明确的条件公式，不替代实际程序检查，也不提供全角误差证书。

## 5. 为什么同比例缩 π 是不同的初猜

式 (2) 可写成
$\tau\pi=\lambda+\mathcal Q(Q,\lambda)$，
其中 $\mathcal Q$ 是原 root 的非线性投影修正。
一般

$$
\mathcal Q(sQ,s\lambda)\ne s\mathcal Q(Q,\lambda).
\tag{15}
$$

因此给 $(Q,\pi)$ 同比缩放后，root 求出的非均值 $\lambda_j$
一般不等于 $s\lambda_j^0$。
若在旋转态附近对所有扰动引入小量 $\epsilon$，
$\mathcal Q$ 的首项为二次项，原 root 的显式稳定公式给出

$$
\mathcal Q(sQ,s\lambda)
=s^2\mathcal Q_2(Q,\lambda)+O(\epsilon^3),
$$

而同比例动量的目标是
$s\lambda+s\mathcal Q_2(Q,\lambda)+O(\epsilon^3)$。
两者通常在 $s(s-1)\mathcal Q_2$ 阶就不同。
这只解释误差阶，不宣称所有第 $j$ 模都严格按 $s^j$ 缩放；有多个输入谐波时，其非线性混合项不能用单一模指数替代。
式 (4) 直接使用真实非线性投影，不需要猜这些缩放指数。

## 6. 全节点实现及 node0 的 port 规范

可执行函数是
[78718-tail-geometric-amplitude-warm.mjs](../scripts/78718-tail-geometric-amplitude-warm.mjs)，
导出 geometricAmplitudeWarm(inputStates,dn,scale)，返回
states 和 diagnostics。它不创建新的物理 tail，不构造稳定图，不运行 DN。

沿用 R86 的准确节点约定：

- node0 使用 cell0 的最后一个 profile、$x=1$。存档的 $\pi$ 先乘 cell0.portRatio 转成该 engine 的 $\mu$ 规范；新 $\pi$ 存回前再除同一个 portRatio。
- node $i>0$ 使用 cell $i-1$ 的第一个 profile、$x=0$，直接使用该 cell 的 $\mu$ 规范。
- 每个节点用同一当前 engine 的 root/toRaw，缩放全部 $2M$ 个 raw 数据，再调用 initializeFromRaw 重求均值及动量。
- 不把平均高度常数从一个节点随意复制到另一个节点；它仍由真正 tail 的积分和接缝处理。

该函数只替换没有可用切线预测器时的初猜缩幅。已有真实全节点 tangent 预测仍优先。函数本身不施加最终新 H 的线性边界修正；调用者保留原 correctInitialBoundary 代码，再用原完整非线性方程决定是否成功。

实际源码为3416 B，SHA256
61c401abf66ca792f1c085f6a4b5b5911a62c3f966adb2dc11bd911b196148af。
它已接入根真正启动的 fast04，当前生产版本不再修改。

## 7. 已观察到的真实半 H 暖启动

根在 fast04 实际启动后，worker 的真实记录给出
M22/N512、865个节点、$s=1/2$：

实际事件时间为2026-11-10 12:10:53.077 UTC；[标量摘录](../notes/2026-11-10-78718-tail-geometric-amplitude-warm-actual-01.json) 由 cd67f8 从根正在运行的 trace 中读取，没有另跑 DN。摘录记录观察当时的 trace 前缀身份，不要求其后追加的日志保持原哈希。

- 最大 Q 缩放误差为0。
- 非均值 $u_r$ 缩放的 Fourier-l1 浮点误差约 $2.24748\times10^{-17}$。
- 完整平均径向高度相对线性缩放的偏移最大约 $1.625431\times10^{-4}$，因此均值修正实际不可省略。
- 新 $\pi$ 相对旧 $\pi$ 同比缩放的最大相对偏移约0.557998。
- 实际 root 最大相对残差约 $5.03384\times10^{-14}$，节点/角点样本中的 minLeading≈0.561749、minD≈0.995847。

这些是已运行函数的浮点诊断，不是全角连续下界。随后真实 shooting 的首轮 evaluate 已完成，但仍有较大的归一残差，不能把暖启动通过说成新半 H 解已经收敛。无须为这些已得事实再开一套重复 DN；主运行的自然出口和后续向原 H 的真正延拓，由根的当前记录继续更新。

本结果没有改变固定 $g$ 或最终目标 H，也没有用小振幅中间状态支付原题的完成标准。

