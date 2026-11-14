# R244 — 精确圆形区段内标量控制的设计核方向

## 命题与范围

考虑共同材料角 $\theta\in S^1$、固定区间 $s\in[0,L]$ 上的联合设计问题：
未知量包括场 $F$、core 参数 $c$、标量控制 $p$ 和由完整非均值高度迹驱动
的 tail。参考度量为

\[
g_p=ds^2+a(s;p)^2\,d\theta^2.
\]

本条研究的是允许 $p$ 变化的**设计系统**。它不是固定 $g$ 的等距弯曲
定理；控制冻结以后，下面的 $\delta p\ne0$ 方向就不再是允许变分。

假设：

1. 存在 $0<\ell<r<L$，使当前场在 $J=[\ell,r]$ 上恰为
   \[
   F(s,\theta)=a(s)e_r(\theta)+z(s)e_z,
   \qquad e_r=(\cos\theta,\sin\theta,0),
   \]
   其中 $a>0$、$a\in C^2$，并且
   \[
   z_s=w=\sqrt{1-a'^2}>0.
   \]
   在 $J$ 上平方根处于同一个正分支。
2. 存在允许的非零控制方向 $v$，其标量变分为
   $\delta a=b$；$b\in C^2(J)$ 非零，在两端均有
   $b=b'=b''=0$，并以零延拓到 $[0,L]\setminus J$。允许的设计模型在
   此方向可写成 $a_\varepsilon=a+\varepsilon b$，或至少具有同样的一阶
   变分并保持入口、cut 的标量 jets。
3. 场方程的残差在局部只依赖相应场及其导数，且对共同竖直平移不变。
   使用 Frenet 形式时，当前场位于算子可微的正则域，并选取下文的正
   binormal 分支。允许当前场在 $J$ 外尚未解出方程。
4. 左端条件只依赖入口场、core 与被固定的入口标量数据；core 不随下面
   的变分改变。右端 tail 及全部 DN 行依赖 cut 的非均值材料高度、其
   导数和不变的 cut 标量数据，对场的共同高度平移不变。没有额外固定
   下游绝对高度的边界条件。

**结论。**取 $\delta c=0$，并定义

\[
q(s)=
\begin{cases}
0,&s\le\ell,\\
-\displaystyle\int_\ell^s\frac{a'(u)b'(u)}{w(u)}\,du,
    &\ell\le s\le r,\\
-\displaystyle\int_\ell^r\frac{a'(u)b'(u)}{w(u)}\,du,
    &s\ge r,
\end{cases}
\tag{1}
\]

以及

\[
\delta F(s,\theta)=
\begin{cases}
0,&s\le\ell,\\
b(s)e_r(\theta)+q(s)e_z,&\ell\le s\le r,\\
q(r)e_z,&s\ge r.
\end{cases}
\tag{2}
\]

则 (2) 为 C² 变分；它在 $J$ 上满足线性化等距方程和原 Frenet 场方程，
在 $J$ 外使局部残差的一阶变化为零，并保持全部左条件及右非均值
height/DN 条件的一阶变化为零。tail 本身可取零变分。因此完整连续设计
残差的导数具有非零核方向 $(\delta F,\delta c,\delta p)=(\delta F,0,v)$。
若一个有限离散系统**恰好包含并精确实现**这些场与控制变分，同样的核
结论才可传到它的 Jacobian。

## 一、变分的正则性及线性化度量

$w$ 连续且在紧区间 $J$ 上为正，因此有正下界，(1) 定义良好。
在 $J$ 内

\[
q'=-\frac{a'b'}w.
\tag{3}
\]

由于 $a,b\in C^2$，右端为 C¹，故 $q\in C^2$。在两端，$b'=0$ 使
$q'=0$；求导 (3)，$b'=b''=0$ 使 $q''=0$。所以 $q$ 分别与上游零值、
下游常数值 C² 接合。$b$ 的零延拓也为 C²，从而 (2) 是全区间的 C²
变分。

在圆形区段，令 $e_\theta=(-\sin\theta,\cos\theta,0)$。有

\[
F_s=a'e_r+w e_z,\quad F_\theta=a e_\theta,
\quad\delta F_s=b'e_r+q'e_z,\quad\delta F_\theta=b e_\theta.
\]

直接计算得到

\[
\begin{aligned}
\delta(F_s\cdot F_s)&=2(a'b'+wq')=0,\\
\delta(F_s\cdot F_\theta)&=0,\\
\delta(F_\theta\cdot F_\theta)&=2ab.
\end{aligned}
\tag{4}
\]

而 $\delta g_p=2ab\,d\theta^2$，故 (4) 正好是联合设计问题的线性化
等距方程。没有把 $\delta g$ 错置为零。

在上游，场和度量都不变；在下游，$\delta a=0$ 且 $\delta F$ 为共同
常向量，所有场导数不变。因此度量残差的一阶变化也为零。这一点与原
残差是否已经为零无关。

## 二、原正分支 Frenet 方程的核对

沿固定 $s$ 的圆，取空间曲线的单位切向 $T$、主法向 $N$、binormal
$B=T\times N$，则

\[
T=e_\theta,\qquad N=-e_r,\qquad B=e_z,\qquad\kappa=1/a.
\]

当前原算子的速度形式为

\[
\mathcal V(F,a)=\alpha N+\beta B,
\qquad
\alpha=-\frac{a'}{a\kappa},\qquad
\beta=\sqrt{1-\alpha^2}>0.
\tag{5}
\]

因为 $a\kappa=1$，(5) 给出
$\mathcal V=a'e_r+w e_z=F_s$。圆形半径变为 $a+\varepsilon b$ 时，
$T,N,B$ 不变，$\delta\kappa=-b/a^2$，于是

\[
\delta(a\kappa)=0,\qquad
\delta\alpha=-b',\qquad
\delta\beta=-\frac{a'b'}w.
\]

因此

\[
\delta\mathcal V=b'e_r-\frac{a'b'}w e_z
                 =\partial_s\delta F.
\tag{6}
\]

这证明了原 Frenet 方程 $F_s-\mathcal V(F,a)=0$ 的线性化，而不只是
度量方程的一条必要条件。原源码对应
`computations/alternative-outward-probe.py` 的 `Probe.frame` 中
`al=-ap/(a*kap)`、`be=sqrt(1-al**2)` 与 `V=al*N+be*B`；完整 core
实现继承同一个几何速度。

若代码使用固定 normal angle $\phi$，而共同材料角为
$\theta=\Phi_c(\phi)$、$\Phi_c'>0$，则
$|F_\phi|=a\Phi_c'$、曲线曲率仍为 $1/a$，上述 Frenet 标架不变。
$\delta c=0$ 使材料图不变，所以 (6) 也在该坐标下成立。

在 $J$ 外，(2) 是零变分或共同高度平移，原 Frenet 几何速度仅由角导数
和标量数据决定，故其残差一阶变化为零。这里不要求上游 warm 场已经是
全局 Frenet 解；只要求当前算子在那里有定义、可微且具有所述平移不变性。

## 三、一个有限参数族使残差保持不变

上述线性化还可以直接由一条局部精确曲线导出。由于 $w$ 有正下界，
对足够小的 $|\varepsilon|$，

\[
a_\varepsilon=a+\varepsilon b>0,
\qquad
w_\varepsilon=\sqrt{1-(a'+\varepsilon b')^2}>0
\]

在 $J$ 上都成立。定义

\[
q_\varepsilon(s)=\int_\ell^s(w_\varepsilon-w)\,du
\quad(\ell\le s\le r),
\]

上游取零，下游取常数 $q_\varepsilon(r)$；在 $J$ 上令

\[
F_\varepsilon=(a+\varepsilon b)e_r+(z+q_\varepsilon)e_z,
\]

上游保留 $F$，下游取 $F+q_\varepsilon(r)e_z$。因 $b,b',b''$ 在两端为
零，$q_\varepsilon'$ 和 $q_\varepsilon''$ 在两端为零，整个场 C² 接合。
圆形区段上 $(F_\varepsilon)_s=(a'+\varepsilon b')e_r+w_\varepsilon e_z$，
故每个小 $\varepsilon$ 都满足该区段的正分支方程；其余区段的残差因
不变或共同平移保持原值。微分此曲线即得 (1)–(2)。

这说明即使当前 warm 在其他区段的残差非零，**残差函数沿此设计方向
的一阶变化**仍为零；不能将“非解点”误当作排除 Jacobian 核的理由。
若控制模型只有相同的一阶变分而非整条线性 $a_\varepsilon$，前两节的
微分论证仍直接成立。

特别地，若 support 内 $a'$ 为常数，则 $a'/w$ 为常数，
$q(r)=-(a'/w)(b(r)-b(\ell))=0$。这时一阶场变分本身也完全支撑于
$J$，连下游常数高度位移都为零。

## 四、左边界和完整非均值 DN 边界

$\ell>0$，故入口附近 $\delta F=0$、$\delta a=0$，并且
$\delta c=0$。所有依赖这些量的左条件变化为零，包括当前设计保留的
低 core 条件、入口高度条件和 normal-angle 入口关系。

因为 $r<L$，cut 附近场变分为常量 $q(r)e_z$。令 $H$ 为材料角高度的
全部非均值分量：无论是全部连续 Fourier 模式还是明确保留的全部模式，
常数的每个非零频率系数都为零。所以

\[
\delta H=0,\qquad \delta H_s=0,\qquad\delta H_{ss}=0.
\tag{7}
\]

cut 的 $a,a',a''$ 和坐标方向也不变。对原真实 tail DN 映射
$\mathcal D(H)$，(7) 使 $\delta\mathcal D=D\mathcal D(H)\,\delta H=0$；
tail 解可保持原状，全部非均值 DN 残差变化为零。此论证无需假设 DN
矩阵数值很小，也没有把完整 DN 替换成法向 projector 或删去边界行。

当前 `geometry_20261114_full_dn_boundary.py` 中 `MaterialTrace`
明确定义常数 $\phi$ 模式的非均值投影为零（`projection[:,0]=0`），
`FullDNBoundary` 的右条件为完整非均值 `derivative_s - cut_scale*slope`。
这与条件命题的高度平移不变性一致。若另外施加下游绝对均值高度约束，
本节需要重新检验，不能仍自动宣称有这个核。

取 $\delta p=v$ 为对应的控制方向，若采用 augmented 常参数变量，则
它在 $s$ 上取常值，$\partial_s\delta p=0$；core 变量同理为零变化。
故这些新增方程也不消除该方向。因为 $b\ne0$，联合方向非零，从而
设计 Jacobian 的核结论成立。

## 五、对当前 M96 失败回执能解释什么

本命题的精确前提是 support 上的共同 $\theta$ 圆。当前 warm 的圆段
在固定 $\phi$ 有限 M96 空间中通过完整模式投影表示；一般
$e_r(\Phi_c(\phi))$ 具有无限 Fourier 频谱，有限投影不等于精确共同
$\theta$ 圆。场变分 $b e_r(\Phi_c(\phi))$、径向 collocation 以及
相关乘积也未必被有限离散空间精确容纳。

因此 R244 解释了把控制放进已压圆区段时会出现弱可辨识设计方向的
结构原因；它**没有证明**当前有限 M96 矩阵精确奇异。约
$7\times10^{17}$ 的数值条件数或一次失败 Newton 回执不能替代上述
有限表示前提的证明。本条也没有从圆近似误差给出奇异值上界：若要
定量“近核”，还需相同范数下的算子与表示误差估计。

将三个控制 support 移到实际非轴 prefix，是为了避开本条明确识别的
圆段设计自由度；R244 不保证新 support 的所有设计列独立，也不预言
新的 fullDN 迭代必然收敛。新方案仍由完整真实方程、全部 DN 行及公开
Actions 的实际接受门决定。它不改变完成标准，不是新非线性解、闭面、
reach 或大幅度结论。
