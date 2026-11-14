# R106 补充：小缺陷坐标中完整一形式的二阶全时拉回

2026-11-13，constructive-route。

**已证明并已执行一个实际中心标量预算。** 本结果把 R106 的正则首相位密度、
cut 与 root 一形式接到 R72 的同一缺陷坐标。有限主项保留完整有符号时间顺序；
余项不再使用粗 $e_J$ 乘根大密度。没有宣称实际七场 Fourier 或整个 $b-\beta$
已经完成。现有 endpoint 累计不能自动当作本文要求的全部部分时间累计。

## 1. 同一真实流与两个完整部分时间积分

沿实际共同递增时间，令

$$
X_t=g(t,X),\quad X(a,x)=x,\qquad
|g|,|\widehat g|\le M(t),\quad |g-\widehat g|\le\eta(t)
\quad\text{on }|\Im x|\le S_g .
$$

两个场及其有限近似均具有 $2\pi$ 标签周期。设
$A(t)=\int_a^t M,\ E(t)=\int_a^t\eta$，其终值为 $A,E$。
取 $s<\sigma<S_g$，置

$$
R=S_g-\sigma,\quad d=R-A,\quad \delta=\sigma-s,\qquad A\le R/2.
\tag{106OF.1}
$$

完整有限近似时间积分是

$$
C(t,x)=\int_a^t\widehat g(v,x)\,dv,\qquad
D(t,x)=\int_a^t\partial_x\widehat g(v,x)\,C(v,x)\,dv.
\tag{106OF.2}
$$

它们不是每段重置为零的积分，也不是只保存最终值的数组。R72 的证明逐个
时间前缀成立，给

$$
\begin{gathered}
|X-x|,\ |C|\le A,\qquad
|X-x-C|\le A^2/(2d)+E,\\
|X-x-C-D|\le F:=E(1+A/R)+A^3/(2d^2).
\end{gathered}
\tag{106OF.3}
$$

这些界都在 $\sigma$ 带成立，内部可用 $A(t),E(t)$ 更紧地替换终值。
有向物理时间的符号已放入 $g$；积分的参数保持共同递增。

## 2. 一形式的准确二阶有限参考

设实际标签一形式是 $B(t,x)\,dx$，其选定有限参考为
$\widehat B(t,x)\,dx$。在相同标签带 $|\Im x|\le S_B$ 假设

$$
S_B>\sigma+A,\qquad
|\widehat B(t,\cdot)|\le M_B(t),\qquad
|B-\widehat B|(t,\cdot)\le\varepsilon_B(t).
\tag{106OF.4}
$$

定义不删零频的有限参考

$$
\boxed{
\mathcal T_2[\widehat B](t,x)
=\widehat B+
 \partial_x\left[\widehat B(C+D)+\frac12(\partial_x\widehat B)C^2\right].}
\tag{106OF.5}
$$

于是对所有时间，在 $s$ 带有

$$
\boxed{
|B(t,X)X_x-\mathcal T_2[\widehat B]|
\le Q\,\varepsilon_B(t)+K\,M_B(t),}
\tag{106OF.6}
$$

其中可取

$$
Q=\exp(A/d)\le(1-A/d)^{-1}\quad(A<d),
\tag{106OF.7}
$$

及完全显式的

$$
\begin{aligned}
L_0&=S_B-\sigma,\qquad L=L_0-A,\\
K&=\frac1\delta\left[
F+\frac{A^3/(2d)+AE}{L_0}+\frac{A^3}{3L^2}\right].
\end{aligned}
\tag{106OF.8}
$$

最后的有理 $Q$ 仅在严格 $A/d<1$ 时使用；不以边界 $A=R/2$ 自动授予。

**证明。** 在展开源参考时先取原函数 $P_x=\widehat B$。若
$\widehat B$ 有非零平均，$P$ 含线性项；无需强行令 $P$ 周期。
写 $u=X-x$。沿整条 $x$ 到 $X$ 线段，Taylor 积分式给

$$
P(X)-P(x)=\widehat B(x)u+\frac12\widehat B_x(x)u^2+\mathcal E_3,
\qquad |\mathcal E_3|\le\frac{M_BA^3}{3L^2}.
$$

这里 $P'''=\widehat B_{xx}$，用 $|\widehat B_{xx}|\le2M_B/L^2$；
在 $x$ 处另有 $|\widehat B_x(x)|\le M_B/L_0$。又

$$
|u^2-C^2|\le(|u|+|C|)|u-C|
\le A^3/d+2AE .
$$

代入 (106OF.3)，得到 primitive 差

$$
\left|P(X)-P(x)-\widehat B(C+D)-\tfrac12\widehat B_x C^2\right|
\le M_B\left[F+\frac{A^3/(2d)+AE}{L_0}+\frac{A^3}{3L^2}\right].
$$

这个差是周期函数：$X(x+2\pi)=X(x)+2\pi$，线性 monodromy 准确相消。
因此取完整标签导数并在 $\delta$ 损失上用 Cauchy，得到
$\widehat B(X)X_x-\mathcal T_2[\widehat B]$ 的界。
真实变分方程 $X_{x,t}=g_x(t,X)X_x$，沿已付带有
$|g_x(t,X)|\le M(t)/d$，故 $|X_x|\le e^{A/d}$；
最后加上 $(B-\widehat B)(X)X_x$ 即得 (106OF.6)。$\square$

一形式参考中的每个修正均为完整标签导数，所以平均准确等于
$\widehat B$ 的平均。但源的零频仍会产生
$\widehat B_0(C_x+D_x)$ 等非均值修正，**不能在拉回前删除零频**。
对完成的总一形式再取非均值部分是另一项准确投影。

## 3. 真正的相位密度、cut 和 root 如何代入

R68 的同一有限参考是 $Y(t,x)$，实际物理射线为
$\Theta(t,x)=Y(t,X(t,x))$。因此

$$
H(t,\Theta)\Theta_x\,dt
=\underbrace{H(t,Y)Y_x}_{B(t,x)}(t,X)X_x\,dt .
\tag{106OF.9}
$$

R106 七场得到的根正则一形式
$\mathcal R_\sigma+\partial_\theta S_{\rm reg}$，以及严格区完整密度，
都以此形式代入。若根源以 $ds$ 表示、共同时间是 $u$，则
$B=H(s(u),Y)Y_x\,ds/du$，保留实际符号；这里不再乘归一化常数 $4$。
所有角导先按物理 $\theta$ 执行，变成标签函数后才使用 $\partial_x$。

对每个 cut 或 root 端点的一形式，同一 (106OF.5)–(106OF.8) 单独应用于
其实际时间。整个 root 完整组合
$B_{\rm ct}-V_\rho/4-\sigma L_\theta/4$ 必须先按七场公式保留；
根端 $\sigma L_\theta(0)/4$ 亦保留。所有内 cut 只有在同一个真实位置、
方向、标签和 frame 下才能相消。

对时间源积分及有限多个端项求和，完整误差为

$$
Q\left(\int\varepsilon_B\,dt+\sum_e\varepsilon_e\right)
+K\left(\int M_B\,dt+\sum_e M_e\right).
\tag{106OF.10}
$$

若时间尾、几何近似、真正无限 primitive、有限求值或取系数选择误差尚未包含
在 $\varepsilon_B$，必须先加入；本文没有把采样点误差升级为连续带误差。

## 4. 准确的部分时间有限代数与保存范围

在每个已有共同时间段 $u\in[-1,1]$，令
$\widehat g_j(u,x)$ 是带真实半宽符号的完整有限多项式。给定此前累计
$C_-,D_-$，准确有

$$
\begin{aligned}
C_j(u)&=C_-+\int_{-1}^u\widehat g_j(v)\,dv,\\
D_j(u)&=D_-+\int_{-1}^u\partial_x\widehat g_j(v)C_j(v)\,dv.
\end{aligned}
\tag{106OF.11}
$$

把 (106OF.11) 代入 (106OF.5) 再准确积分，保留所有时间次幂、Fourier 和频，
即可得到完整有限有符号主项。这需要保存/重新构造完整局部时间多项式，
或者为删去的部分单独付费。

旧 g0 index 的 omitted_local_J 使用整个对称区间的奇偶抵消。
它只约束完整段末端，不自动约束 $-1<u<1$ 的部分积分。
只保存 first-integral 和 endpoint 二阶 cross 的报告不能直接满足 (106OF.11)。
若确需省去全部部分时间局部二阶积分，至少可另付
$A^2/(2R)$ 的全时费；当前实际门中这样做约大 $2600$ 倍。
有全部相应时间行时应直接保留有限代数，避免此损失。

实际 native helper
scripts/fourfold_phase_one_form_chronological.py 的角变量是归一标签 $x$，
故 Fourier 导数乘 $ik$；它不使用 root 七场中的物理 $4ik$。
源截至本稿尚未实际运行候选，不能由代数接口存在推断相位计算完成。

## 5. 同一已完成中心的实际标量门

准确输入为已通过整条 550 段 forward 的原 g0 index
SHA256 4174c3edde41f5c8ab12b036d4760c20ec987e475158aa2855ea08158ff7cb45，
其小摘要及 R106 全时对象核验均已持久化。程序重读显示球的中点加半径，
得到向外的完整 $A,E$；不是从 approximate 浮点字段抄写。

使用

$$
S_g=1/256,\quad S_B=1/512,\quad \sigma=3/2048,\quad s=1/1024
$$

以及同一实际中心

$$
A<4.092563989255516\times10^{-8},\qquad
E<1.850689783210977\times10^{-18},
$$

11 个 BigInt 门实际通过，证明

$$
K<2.708\times10^{-13},\qquad Q<1.00002 .
\tag{106OF.12}
$$

严格数值与准确分数保存在
notes/2026-11-13-R106-center-one-form-prefactors.json。
它是中心整个时间前缀的传播系数；$M_B,\varepsilon_B$ 仍须由同一真相位
有限源完成。本文没有借 endpoint $P/T$ 作为全时参数源，也没有把
中心 (106OF.12) 转授到整个 $\eta=10^{-9}$ 家族。
实际整盒版本只需重新支付共同 $A,E$ 并代入同一证明。

源报告的复域和 R46 最终 frame 仍分别检查。将来若转换成 R104 的
Sobolev/Wiener 乘子和，还须保留这一次真实域损失与强余项；
本结果不把数值上很小的 sup 误差自动当作同宽高阶乘子误差。
