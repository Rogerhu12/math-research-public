# R86：保留几何一 jet 的非线性动量升频

状态：**完整中间命题与可直接使用的暖启动实现。** 同一角积分规则下，升频时保留高度系数 $Q$ 和径向导数系数 $L$、重新投影非线性连接，精确保持高度及其径向一 jet；直接给新增动量补零一般不保持它们。改变角求积规则时只保证非均值系数保持，均值须重求并计入差异。本文还证明固定截面上的二 jet 更新是正权 Galerkin 投影。它不声称已得到新的全尾或闭曲面解。

作者 Astra-visible-flex-78718bd0，`/root/independent_audit`，2026-11-10；根保留编号 R86。本文按根 README §13 直接登记，不设置独立审核或重跑门。

## 1. 原引擎中的变量必须区分

固定一个物理截面，记半径 $r>0$、背景斜率 $w>0$、$W=w^2$、$E=1+W$，该物理 cell 的动量尺度为 $\mu>0$，方向为 $\varepsilon\in\{1,-1\}$。角间隔为整数 $m\ge2$，令 $\ell_j=mj$，并使用正交归一余弦基

$$
c_0=1,\qquad c_j=\sqrt2\cos(\ell_j\theta)\quad(j\ge1).
$$

原引擎的高度、相对斜率和角导数变量为

$$
\begin{aligned}
u&=u_0+r^4\sum_{j=1}^{M}Q_j\cos(\ell_j\theta),\\
P&=-\sum_{j=1}^{M}\frac{\ell_jr^3Q_j}{w}\sin(\ell_j\theta),\\
L&=\sum_{j=0}^{M}\lambda_jc_j,\qquad K=L-P_\theta,\\
u_r&=w(1+K),\qquad u_\theta=rwP.
\end{aligned}
\tag{1}
$$

其中 $u_0$ 是所选的平均高度值。尤其

$$
\boxed{
u_r=w(1+\lambda_0)+\sum_{j=1}^{M}
\bigl(\sqrt2w\lambda_j+\ell_j^2r^3Q_j\bigr)\cos(\ell_j\theta).
}
\tag{2}
$$

定义

$$
S_0=1-WP^2,\quad
D_0=1-W(2K+K^2+EP^2),\quad
A=1+K+EP_\theta=1+L+WP_\theta.
\tag{3}
$$

以下讨论均处于 $S_0,D_0,A>0$ 的原分支中。实际程序另保留自己的正间隙检查，不在这里改变它。

角连接由 [R85](R85-darboux-curl-and-tail-metric-frequency.md) 的公式给出：

$$
\omega=
\frac{1+W(1+K)P_\theta/S_0}{\sqrt{D_0}}.
\tag{4}
$$

设 $\mathcal Q$ 是精确角平均，或一个固定的等距 N 点角平均。原角 root 要求

$$
\mathcal Q\!\left(\frac{\omega-1}{W}\right)=0,
\qquad
\mathcal Q\!\left(\frac{\omega-1}{W}c_j\right)
=\frac{\varepsilon\sqrt{12}\mu}{\sqrt2 r^4W}\pi_j
\quad(1\le j\le M).
\tag{5}
$$

所以 $\pi$ 是**非线性连接的投影坐标**，不是 $L$ 或 $u_r$ 的 Fourier 系数。即使 $Q,L$ 只有 M 模，(4) 一般仍具有所有倍数角频率。

## 2. 完整的一 jet 升频命题

**命题。** 给定满足 (5) 的旧 M 模数据，选 $\widetilde M\ge M$，保持同一 $r,w,\mu,\varepsilon,m$ 和同一平均算子 $\mathcal Q$。把 $Q_j,\lambda_j$ 在 $j>M$ 处补零，保留旧 $\lambda_0$ 和 $u_0$，并定义新动量

$$
\boxed{
\widetilde\pi_j=
\frac{\varepsilon\sqrt2 r^4}{\sqrt{12}\mu}
\mathcal Q\bigl((\omega-1)c_j\bigr),
\qquad 1\le j\le\widetilde M.
}
\tag{6}
$$

则新高度 $u$、$u_\theta$、$u_{\theta\theta}$、$u_r$、$u_{r\theta}$ 完全与旧值相同；(3) 的分支函数也相同。新高维角 root 的解恰是旧 $L$ 补零。旧动量分量保持，而新增动量通常不为零。

**证明。** $Q,L$ 的角函数不变，由 (1)–(4) 可知 $P,K,u,u_r,\omega$ 均不变；角导数亦不变。旧平均方程仍为零，(6) 恰好给新全部非均值 root 方程。对 $j\le M$，(6) 与旧 (5) 相同，因此 $\widetilde\pi_j=\pi_j$。

还需说明这是同一正分支的 root，而非随意挑选另一解。固定 $Q$ 时，(4) 对 $L$ 的点导数为

$$
\frac{1}{W}\frac{\partial\omega}{\partial L}
=\frac{A}{D_0^{3/2}}>0.
\tag{7}
$$

于是 root 映射在 $\lambda$ 坐标中的 Jacobian 是

$$
B_{ij}=\mathcal Q\!\left(\frac{A}{D_0^{3/2}}c_ic_j\right).
\tag{8}
$$

它正定：连续情形中任何非零有限余弦多项式的平方积分为正；N 点情形只需这些基函数在网格上独立，当前引擎的 $N>4m\widetilde M$ 已足够。更具体地，$N>2m\widetilde M$ 时这些余弦在等距离散平均下仍正交归一。

允许分支在 $\lambda$ 空间中是凸的。因为 $P$ 固定，$S_0$ 固定，且

$$
D_0=ES_0-W(1+K)^2,
$$

$D_0>0$ 等价于对仿射函数 $1+K$ 的上下界，$A>0$ 也是仿射不等式；对全部角点或整个角圈取这些条件的交集仍凸。沿两解之间的线段积分 (8)，非零系数差与 root 映射差的内积严格为正。因此该分支至多有一个 root。前面已给出一个，故它就是新解。证毕。

反之，若保持旧低动量而给新增 $\pi_j$ 直接补零，只要 (6) 的某个新增分量非零，旧补零的 $L$ 就不再解新 root。由唯一性，新的 $L$ 必须改变，进而 (2) 的 $u_r$ 一般改变。这正是本次 stage34 新峰的原因；它不是“原高度多项式加了几个零系数”这么简单。

## 3. 原 `toRaw` / `initializeFromRaw` 已实现所需坐标转换

原 `general_root_tail_momentum.mjs` 把 raw 的后半部定义为

$$
R_j=\frac{\sqrt2 w\lambda_j}{\sqrt{12}\,r^3}.
\tag{9}
$$

因此 `oldEngine.toRaw(oldState,profile,x)` 返回的是 $[Q,R]$，不是 $[Q,\pi]$。以下调用准确实现命题：

1. 用旧 M、旧 N、该节点实际 $\mu$ 的引擎，从旧状态得到 raw 的 $[Q,R]$。
2. 在新 raw 的前半部放旧 $Q$，后半部放旧 $R$，新增位置全部补零。
3. 调用 `newEngine.initializeFromRaw(newRaw,profile,x)`。它从 (9) 恢复非均值 $\lambda_j$，求唯一的平均 $\lambda_0$，然后按 (6) 生成所有新 $\pi_j$。

同一平均算子下，旧 $\lambda_0$ 已满足新平均方程，故精确算术下保持原值；后续完整 root 也回到同一个 $L$。如果还持有两个独立的平均高度状态，应单独复制它们；checkpoint 中仅存 $2M$ 个形状/动量分量时，转换不凭空宣称已经恢复整尾的平均高度积分。

这里 $R$ 的定义没有额外方向因子；方向 $\varepsilon$ 只在 (5)–(6) 的动量规范中出现。这与原引擎两条实际函数的公式一致。

## 4. 改变 N 时的准确限定

若新旧平均算子分别为 $\mathcal Q_1,\mathcal Q_2$，raw 补零仍精确保留全部非均值 $\lambda_j$ 和 $Q_j$。但是旧平均 $\lambda_0$ 未必满足新平均方程。

令

$$
\epsilon_{quad}=\mathcal Q_2\!\left(\frac{\omega_{old}-1}{W}\right),
$$

并令 $\kappa>0$ 是连接旧、新平均 root 的允许线段上
$\mathcal Q_2(A/D_0^{3/2})$ 的下界。由一维中值公式，

$$
|\widetilde\lambda_0-\lambda_0|
\le\frac{|\epsilon_{quad}|}{\kappa},
\qquad
\widetilde u_r-u_r=w(\widetilde\lambda_0-\lambda_0).
\tag{10}
$$

右边在角圈上是常数；非均值径向斜率系数和 $u_{r\theta}$ 不变。这个结论要求两平均 root 位于所述同一允许段，不能在没有正间隙时无条件使用 (10)。

实际浮点程序还包含 raw 转换、均值求根、全 root 重求的舍入与停止误差。因此即使 N 相同，实际回执也只报告测得的一 jet 差，不称逐位相同。N512→N1024 的本次数值差很小，但本文没有把它改写成跨 N 的无条件精确恒等。

## 5. 保持一 jet 后，新的二 jet 是正权 Galerkin 修正

在这一节使用连续精确角积分，固定半径 $r_0$，假设旧有限 ODE 的角 root 精确满足 (5)。由 R85，旧完整连接残差 $\Omega_M$ 在旧保留空间

$$
V_M=\operatorname{span}\{1,\cos(m\theta),\ldots,\cos(mM\theta)\}
$$

上正交为零。按第 2 节提升状态后，新有限 ODE 的瞬时导数给新的 $u_{rr}$；它不是复制旧二阶径向导数。

由于 $u,u_r$ 作为整个角函数已保持，R85 的完整 Darboux 分子中只有 $u_{rr}$ 改变。设 $h=\widetilde u_{rr}-u_{rr}\in V_{\widetilde M}$，则逐点准确有

$$
\widetilde\Omega-\Omega_M=a(\theta)h,
\qquad
\boxed{\ a(\theta)=\frac{wA}{D_0^{3/2}}>0.\ }
\tag{11}
$$

例如由 R85 的展开，$u_{rr}$ 的系数是
$r^2(Eu_{\theta\theta}+ru_r)/\Delta^{3/2}$，代入 (1)–(3) 即为 (11)。新有限 ODE 在整个 $V_{\widetilde M}$ 中消去连接残差，故 $h$ 唯一满足

$$
\boxed{
\langle a h v\rangle=-\langle\Omega_Mv\rangle
\quad\text{对所有 }v\in V_{\widetilde M}.
}
\tag{12}
$$

这就是正权质量矩阵方程。令 $P^a_{\widetilde M}$ 是内积
$\langle f,g\rangle_a=\langle a f\overline g\rangle$ 的正交投影，则

$$
h=-P^a_{\widetilde M}(\Omega_M/a),
\qquad
\widetilde\Omega
=a(I-P^a_{\widetilde M})(\Omega_M/a).
\tag{13}
$$

因此

$$
\|\widetilde\Omega\|_{a^{-1},2}
=\|(I-P^a_{\widetilde M})(\Omega_M/a)\|_{a,2}
\tag{14}
$$

随保留空间嵌套扩大不增。只要固定第一 jet 光滑且 $a$ 有严格正下界，偶的 $2\pi/m$ 周期余弦多项式在相应加权 $L^2$ 中稠密，故 (14) 趋零。这里保持的是**同一个截面的第一 jet**；没有得到一个统一径向长度上的全尾轨道收敛。

这一局部收敛还控制该截面的周期发展 metric。由 R85，第一 jet 保持使 $\rho e^{i\psi}$、$A$ 和 $\zeta$ 保持；精确均值 root 给 $\zeta=0$。对归一化 $L^2$ 范数，Fourier Cauchy–Schwarz 给

$$
\|Pf\|_\infty\le\frac{\pi}{\sqrt3}\|f\|_2.
$$

两次应用它，并用 $\rho\le r$，得到

$$
\|v_{\widetilde M}\|_\infty
\le\frac{\pi^2r}{3}\|\widetilde\Omega\|_2
\le\frac{\pi^2r\sqrt{a_{max}}}{3}
\|\widetilde\Omega\|_{a^{-1},2}.
\tag{15}
$$

再用 R85 的 $2\eta+\eta^2$ 界，可知该固定截面的实际发展 metric 趋零。每个有限维 root 的正定性也给其局部 ODE 的光滑向量场，因而提升状态有自己的短径向解；本论证没有给这些区间的统一长度，没有保持远端 Robin 条件或 prefix 接合，更没有证明完整闭面存在。

在固定 N 的离散系统中，R85 的 aliasing 项仍存在。保持第一 jet 使这项相同；离散质量矩阵消去的是与离散 Fourier 连接导数一致的残差。不能直接把连续式 (14) 的单调性套在含 aliasing 和浮点误差的 sampled physical metric 上。

## 6. 多重射击节点上的实际 $\mu$ / portRatio 映射

当前节点约定是：第 i 个小段以 `states[i+1]` 为输入，向外积分后，其动量除以本段 `portRatio`，与 `states[i]` 比较。转换必须遵循这一规范，不能按节点编号猜测 $\mu$。

本次实现对同一物理深度、同一 shootingParts、同一 rawNode 分区处理全部节点：

| 保存节点 | 使用的物理小段和位置 | 转入引擎前的旧动量 | 新动量保存时 |
|---|---|---|---|
|0|`cells[0]` 的最后 profile，x=1|乘 `cells[0].portRatio`|除以同一比值|
|i>0|`cells[i−1]` 的第一个 profile，x=0|直接使用|直接保存|

每次旧引擎都使用该小段的真实 `cell.mu`、旧 M、旧 N；新引擎使用同一 `cell.mu` 和新 M/N。对于内部物理 cell 的接口，选择外侧小段的输入规范正好与保存节点一致；无需再额外乘另一个 cell 的比值。

代码先调用原 `remeshCheckpoint` 得到正确宽度的数组，再提取其中旧宽的 $Q,\pi$，执行第 3 节转换。当前实现明确只接受相同 depth/parts；它不把原线性追加的深部初猜或重新插值的节点宣称为精确保持旧几何。

生产入口为：

- [全节点转换函数](../scripts/78718-tail-geometric-warm-remesh.mjs)：导出 `geometricWarmRemesh(prior,dn,engineFactory)`，返回 `{states,diagnostics}`。
- [新的真实 tail worker](../scripts/78718-prefix-tail-geometric-worker.mjs)：基于原 trial worker，只接入新的暖启动转换及少量诊断；原物理兼容检查、真正 DN/ODE/分支/残差、Jacobian、trial 拒绝记录和完整返回均保留。

这个 worker 不改正在执行的 M15 入口。它在 trace 和 ready 的 `warmEmbedding` 中记录旧/新 M/N、Q 差、径向一 jet 差等小标量，不把转换后的状态称作已经通过真正 tail solve。

## 7. 实际 stage34 对比：新增动量置零造成的峰迁移

输入仍是当前 M15 的首次真正 N512 响应，并非最终 outer 候选。位置为 cell0、stage34、x=0.125、r≈0.48461851182189386。它是对旧轨道作零动量补齐时，M18/M22 峰迁移到的位置。

使用原 `toRaw` 和 `initializeFromRaw` 的实际结果：

| 新 M | 新 N | 高动量补零的 metric | 保留 Q/L 后的 metric |
|---|---:|---:|---:|
|18|512|9.60018509e-9|7.88519205e-10|
|22|512|5.71071146e-9|2.43855219e-10|
|26|512|4.43703872e-9|1.11865300e-10|
|32|512|3.45610501e-9|3.29023502e-11|
|40|512|2.08777768e-9|9.48019441e-12|

Q/L 转换后在公共角点的 $u_r$ 差最大约 4.1e-16。N1024 重求均值后也测得同量级一 jet 差；例如 M22 的更密角网格最大 metric 约 2.46375484e-10。不同网格的最大值同时改变采样角，不把其差直接称作求积误差。

这些值说明：从“旧状态高动量补零到 M22 仍有 5.7e-9”不能推断真正同 g 的 M22 解必定达不到目标。该补零本身已改变几何一 jet。反过来，保留一 jet 后的单点值也不能保证完整 M22 尾达标。

[局部比较脚本](../scripts/78718-tail-geometric-mode-embedding.mjs) 和[实际报告](../notes/2026-11-10-78718-tail-geometric-mode-embedding-stage34-01.json) 保留了全部这些诊断及二阶导数改变；本次只改坐标表示和新局部向量场，未运行第二次 shooting。

## 8. 全 865 节点转换已实际完成，真实求解仍由主线执行

[全节点小程序](../scripts/78718-tail-geometric-warm-probe.mjs) 在同一物理构造和同一 865 个节点上实际执行了转换，不构造稳定图，不运行 DN/BVP。[报告](../notes/2026-11-10-78718-tail-geometric-warm-probe-m22-01.json) 给出：

| M15/N512 到 | 最大 Q 差 | 公共角点最大 $u_r$ 差 | 浮点 Fourier l1 差 |
|---|---:|---:|---:|
|M22/N512|0|5.80938263e-16|5.81077128e-16|
|M22/N1024|0|5.80090349e-16|5.80182461e-16|

新增高动量的最大大小可达到该节点旧低动量范数的约 0.05125358，不能当作无关紧要的零。新角 root 的最大相对残差约 7.78e-14；所有检查的节点/角点中最小 leading 超过 0.1068。这里全角 l1 仍是浮点系数差的诊断，不冒充向外区间证书。

实际工具回执为局部 5a4939/session58657 → 833bc4 exit0，以及全节点 8fdf73/session46809 → 31b1a1 exit0。这些回执说明实现已经运行；完整数学依据是前面的公式和证明，不以重复执行替代它。

下一步由新的 generic client 用转换后的初猜真正求解尾部及其与 prefix 的接合。只有新完整方程的真实解及实际导出图，才可用于全曲面 G5 精度判断；当前低阶数据、局部投影收敛或暖启动差很小均不能替代该步骤。

## 9. 同点分支正性也保持：升频不能凭表示抬高 A

以下是第 2 节命题的直接推论，对理解原数值 guard 有用。固定同一个 $g$ 和截面，由式 (1) 得

$$
P=\frac{u_\theta}{rw},\qquad
1+K=\frac{u_r}{w},\qquad
P_\theta=\frac{u_{\theta\theta}}{rw}.
$$

所以原角 root 的 leading 因子是

$$
\boxed{\displaystyle
A=1+K+EP_\theta
=\frac{ru_r+E u_{\theta\theta}}{rw}.}
\tag{16}
$$

**推论。** 第 2 节同求积规则的几何 $Q/L$ 升频精确保留同点的 $A,S,D$。因此若旧点具有 $A>a_*>0$，该正性在精确嵌入后保持；若旧点为 $0<A<a_*$，仅改表示不会把它变成 $A\ge a_*$。

**证明。** 升频保留全部旧 $Q$、把新增 $Q$ 置零，所以 $u_\theta,u_{\theta\theta}$ 不变；它还保留 $L$，从而保留 $K$ 和 $u_r$。式 (16) 给出 $A$ 不变，原公式
$S=1-WP^2$、$D=1-W(2K+K^2+EP^2)$ 给出其余两项不变。
若改变 $N$ 后仅均值系数变化 $\delta\lambda_0$，则同点
$A_{\rm new}-A_{\rm old}=\delta\lambda_0$，须用第 3 节的均值误差控制，不能继续声称无条件精确保持。证毕。

该结论不妨碍真正高模 ODE 在后续半径处产生更好的 $A$；第 5 节已经说明新的二 jet 会改变。它只排除“在同一个一 jet 截面上靠重新编码提高 leading”的误读。

实际 M15 第 2 请求 iteration5 的局部点及失败 trial 已用于验证这一解释，见[统一研究笔记第 12 节](../notes/2026-11-10-78718-tail-metric-error-research.md)。其中较低数值 floor 下找到的两个正 $A$ root，在同点 M22 几何嵌入后仍分别约为 0.0409031 和 0.0499059；这些是有限浮点诊断，不是新的完整尾解或已确认的全角下界。

## 10. 小 A 的真正几何压力须由 Gauss 方程判断

本节给出同一高度一 jet 必须满足的局部必要条件，不把有限投影 ODE 先验当成真等距面。

设局部 $C^2$ 浸入 $F$ 的诱导度量恰为
$g=E(r)\,dr^2+r^2\,d\theta^2$，其第三坐标为 $u$，且 $D>0$。
取法向使竖直分量 $n_3>0$。由

$$
|\nabla_g u|^2=\frac{u_r^2}{E}+\frac{u_\theta^2}{r^2},
\qquad
1-|\nabla_g u|^2
=\frac{E(1-WP^2)-W(1+K)^2}{E}=\frac D E,
$$

可得 $n_3=\sqrt D/\sqrt E$。Gauss 公式给出
$\operatorname{Hess}_g u=n_3\,\mathrm{II}$。
使用
$\Gamma^r_{rr}=E'/(2E)$、
$\Gamma^r_{\theta\theta}=-r/E$、
$\Gamma^\theta_{r\theta}=1/r$，
第二基本形式在正交标架
$e_r=\partial_r/\sqrt E$、$e_\theta=\partial_\theta/r$
中的矩阵为

$$
\begin{pmatrix}a&b\\b&c\end{pmatrix},
\quad
\begin{aligned}
a&=\frac{u_{rr}-E'u_r/(2E)}{\sqrt E\sqrt D},\\
b&=\frac{u_{r\theta}-u_\theta/r}{r\sqrt D}
  =\frac{wU}{r\sqrt D},\\
c&=\frac{u_{\theta\theta}+ru_r/E}{r^2n_3}
  =\frac{wA}{r\sqrt E\sqrt D}.
\end{aligned}
\tag{17}
$$

这里 $b,c$ 已由固定截面上的 $u,u_r$ 及其角导数确定，不需要先给定 $u_{rr}$。背景的高斯曲率为

$$
K_g=\frac{E'}{2rE^2}=\frac{ww_r}{rE^2}.
\tag{18}
$$

由于真等距浸入满足 Gauss 方程 $ac-b^2=K_g$，当 $A\ne0$ 时必有

$$
\boxed{\displaystyle a=\frac{K_g+b^2}{c},\qquad
\|\mathrm{II}\|_{\mathrm{op},g}
=\frac{|a+c|+\sqrt{(a-c)^2+4b^2}}2 .}
\tag{19}
$$

式 (19) 的第二式由实对称二阶矩阵两个特征值直接得到。若 $A=0$，则必要条件是 $K_g+b^2=0$，此时 Gauss 方程单独不确定 $a$。这些推导完整证明了本节的必要条件。

因此“小 $A$”本身不是大曲率的充分判据；还须看 $K_g+b^2$ 是否同步变小。另一方面，若 $A>0$ 且希望 reach 至少为 $\rho$，局部必要条件
$|a|\le1/\rho$ 强制

$$
A\ \ge\
\rho\,\frac{r\sqrt E\sqrt D}{w}|K_g+b^2|.
\tag{20}
$$

这只使用 reach 的主曲率半径必要条件；即使式 (20) 满足，也没有控制不同部位互相接近，不能推出 reach 下界。

### 已有 W22 trial 的固定点解释

对 stage35、r≈0.473823542 的一个实际已保存失败 trial，较低 floor 下得到 $A\approx0.0014904603$。同点
$K_g\approx-1.7562231\times10^{-5}$、
$b\approx0.00023050735$、
$c\approx2.2831349\times10^{-5}$。
于是若保持这份高度一 jet 并精确等距，式 (19) 要求
$a\approx-0.76688844$，形算子范数约0.766889。
这项点值没有显示宏观 reach 尺度的必然失败；它也不是全角、全径向或全时刻上界。

相同有限投影 ODE 的实际二 jet 只给 formal curvature≈0.0599468，但尚有最大逐点 Darboux 残差约 $1.72616\times10^{-5}$。两者并不矛盾：前者要求精确 Gauss，后者是有限 Galerkin 向量场的实际二 jet。不能用后一较小数值冒充前者。
完整浮点记录和实际执行范围在[统一笔记第 13 节](../notes/2026-11-10-78718-tail-metric-error-research.md)；本节的严格内容是式 (17)–(20)，数值点值未作区间认证。
