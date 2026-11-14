# R55：饱和热反射的三阶Cauchy jet与有限解析自由角基障碍

日期：2026-11-14。root提出三阶反射差与角正则性问题；repo_sources独立完成展开、准确R必要性及全证明，root全文复核。独立纸面推导；未运行研究几何、求解或扫描。

**结论范围。** 本文排除当前指定的“饱和三点反射＋无限周期热平均＋有限解析角向自由列”表示中的准确目标框架残差 $\mathcal R\equiv0$。原因是单圆柱帽的准确三阶径向 jet 要求一个角向非解析的补偿，而自由列的该阶系数为实解析函数。它不排除一般 $C^2$ 等距连接，不排除非解析自由空间，不给任何正的数值残差下界，也不取消当前公开 Actions 对 $10^{-6}$ 误差目标的真实探索。

本证明针对模型的无限热定义；有限 Gauss–Hermite 节点只属于评价规则。它不以某次求积误差或实际候选指标为前提。

来源：[R28 目标框架](R28-orthonormal-frame-reconstruction-and-metric-bound.md)、[R44 准确六帽](R44-S9-six-cap-exact-embedding-and-normal-chord.md)、[R48 无限热定义](R48-six-cap-angular-jump-and-heat-extension.md)及[R51 饱和源修正](R51-heat-source-radial-birth-and-saturated-reflection.md)。

## 1. 准确帽、径向变量与被审表示

使用 [R44](../results/R44-S9-six-cap-exact-embedding-and-normal-chord.md) 的准确六弓形帽。写

$$R=\frac{137}{500},\qquad d=\frac{\sqrt3}{2}R,
\qquad w=R-d>0,$$

$$n_j=(\cos\theta_j,\sin\theta_j),\qquad
\theta_j=\frac{j\pi}{3},\qquad A_j>0.$$

本轮准确幅度为

$$ (A_0,\ldots,A_5)=
\left(\frac3{16},\frac18,\frac18,
\frac3{16},\frac18,\frac18\right).$$

以下角跳论证实际上只用相邻两个 $A_j$ 都为正。

在第 $j$ 个帽内，令

$$a_j(\theta)=e_r(\theta)\cdot n_j,
\qquad b_j(\theta)=e_\theta(\theta)\cdot n_j,
\qquad z_j(r,\theta)=r a_j(\theta)-d.$$

这里小写 $a_j$ 只是方向余弦，不是后面的径向度量函数 $a(t)$。当 $z_j>0$ 时，

$$\alpha_j=A_j S_9(z_j/w),\qquad
S_9(x)=126x^5-420x^6+540x^7-315x^8+70x^9,$$

而 $z_j\le0$ 时该帽增量为零。在 $r\le R$ 的圆盘内最多有一个帽增量非零。

令 $g(r,\theta)=(u,v,\beta)$ 表示准确帽的三个实标量框架场，侧别 $\sigma\in\{+1,-1\}$。在单帽内有

$$
v=-\frac{\sigma b_j\sin\alpha_j}
{\sqrt{1-b_j^2\sin^2\alpha_j}},\qquad
\beta=-\sigma\pi+
\sigma\arctan\left(\frac{a_j\sin\alpha_j}{\cos\alpha_j}\right).
\tag{1}
$$

第三个场 $u$ 仍取 R44 的准确公式。本文的角跳只需 (1) 中的 $v$；在单帽开角上三个场均实解析。

令 $t_f$ 为活动连接到开放平度量尾段的接口，

$$\delta=t_f-t\ge0,\qquad
\varepsilon(\delta)=a(t_f-\delta)-R.$$

当前 S11 径向种子在该端满足

$$a'(t_f-\delta)=-1+O(\delta^6),
\qquad\varepsilon(\delta)=\delta+O(\delta^7).
\tag{2}
$$

饱和源参数和三点反射为

$$c_*\equiv w/4,\qquad
e=c_*\tanh(\varepsilon/c_*),$$

$$E_{\rm sat}=3g(R,\theta)-3g(R-e,\theta)
                         +g(R-2e,\theta).
\tag{3}
$$

无限热平均用 $\tau=\delta^6/(128h^6)$，等价于标准差
$\varsigma=\delta^3/(8h^3)$ 的周期 Gaussian 平均。紧支撑权
$\chi=1-S_9(\delta/h)$ 在端点满足 $1-\chi=O(\delta^5)$。

当前整个活动场可准确重写为

$$F=F_{\rm old}(c)-F_{\rm old}(c_0)
 +(1-\chi)F_{\rm old}(c_0)
 +\chi H_\tau E_{\rm sat}.
\tag{4}
$$

$c_0$ 是冻结的旧 234 系数锚；$c$ 是优化中的同布局系数。旧共享基场在前两项中相消。由于自由径向 B 样条锁住端点全二 jet，其差在最后一个径向样条片上有

$$F_{\rm old}(c)-F_{\rm old}(c_0)
 =\delta^3 P(\theta)+O(\delta^4).
\tag{5}
$$

$P$ 的每个分量都是全角实解析函数：有限材料角三角列、有限椭圆偏心角列及 $u_{\rm core}$ 均为实解析函数，有限线性组合仍为实解析。本文没有把任意光滑或非解析角基纳入 (5) 的结论。

## 2. 饱和三点反射缺少的准确三阶系数

先固定一个严格位于单帽内部、且远离帽中心和顶点的开角。对于充分小的 $\delta$，该角及其固定小邻域都位于同一帽分支，允许使用该单圆柱帽公式的局部解析延拓 $g(r,\theta)$ 到 $r>R$。这只是一个局部比较场，不声称六个帽在整个 $r>R$ 的区域仍不重叠或仍组成准确全帽。

下式中的 $g_r,g_{rr},g_{rrr}$ 都在 $(R,\theta)$ 取值。直接 Taylor 展开给

$$3g(R)-3g(R-e)+g(R-2e)
=g+e g_r+\frac{e^2}{2}g_{rr}
 -\frac{5e^3}{6}g_{rrr}+O(e^4).
\tag{6}
$$

又因

$$e=\varepsilon-\frac{\varepsilon^3}{3c_*^2}
 +O(\varepsilon^5),$$

所以

$$E_{\rm sat}
=g+\varepsilon g_r+\frac{\varepsilon^2}{2}g_{rr}
 +\varepsilon^3\left(-\frac56g_{rrr}
                        -\frac{g_r}{3c_*^2}\right)
 +O(\varepsilon^4).
\tag{7}
$$

相比之下，自然单帽延拓为

$$F_{\rm cap}(t,\theta)=g(a(t),\theta)
=g+\varepsilon g_r+\frac{\varepsilon^2}{2}g_{rr}
 +\frac{\varepsilon^3}{6}g_{rrr}
 +O(\varepsilon^4).
\tag{8}
$$

热平均与紧支撑权均不改变三阶系数。具体地，Gaussian 对称性及有界的角二阶导数给
$H_\tau E_{\rm sat}-E_{\rm sat}=O(\delta^6)$；对角再求一次导数仍是 $O(\delta^6)$。径向一阶差为 $O(\delta^5)$。S9 源标量的联合 $C^4$ 正则性足够这些估计；固定单帽开角上也可直接使用解析公式。
此外 $(1-\chi)(F_{\rm old}(c_0)-H_\tau E_{\rm sat})=O(\delta^5)$。

结合 (2)、(4)–(8)，在上述固定开角上，

$$F-F_{\rm cap}=\delta^3 p(\theta)+O(\delta^4),
\qquad
p=P-\left(g_{rrr}+\frac{g_r}{3c_*^2}\right).
\tag{9}
$$

这些展开可同时取一次角导和一次径向导；后者的首项为 $-3\delta^2p$。等号 (9) 明确区分 $\delta$、$\varepsilon$ 和饱和参数 $e$，没有把 $e$ 的三阶改变漏掉。

## 3. 准确目标残差强迫单帽三阶 Cauchy jet

使用 R28 的单位正交目标框架

$$T=\frac{e_\theta(\theta+u)+v e_z}{\sqrt{1+v^2}},
\quad N=e_r(\theta+u),\quad M=T\times N,$$

$$V=\cos\beta\,N+\sin\beta\,M,
\qquad \mathcal R=V_\theta-\partial_t(aT).
\tag{10}
$$

若 $\mathcal R=0$，积分重构的准确目标切向就是 $X_t=V$、$X_\theta=aT$。本节只对这一准确目标方程作必要性推导。

对于比较场 $F_{\rm cap}=g(a(t),\theta)$，令 $P_{\rm cap}(r,\theta)$ 为单帽准确平度量嵌入，则

$$T_{\rm cap}=\frac{(P_{\rm cap})_\theta}{a},
\qquad V_{\rm cap}=-(P_{\rm cap})_r.$$

因此，使用同一个真实 $a(t)$ 计算其残差，准确有

$$\mathcal R_{\rm cap}
=-(1+a') (P_{\rm cap})_{r\theta}=O(\delta^6).
\tag{11}
$$

这里没有把 $a'^2\ne1$ 的比较场错称为真实目标度量的准确解；仅用其残差到六阶才出现。

将 (9) 代入 (10)。由于 $T$ 只依赖 $u,v$，$\mathcal R-\mathcal R_{\rm cap}$ 的 $\delta^2$ 项恰为

$$3R\delta^2\{T_u p_u+T_v p_v\}.
\tag{12}
$$

$T_u$ 与 $T_v$ 线性无关。因此 $\mathcal R=0$ 及 (11) 首先迫

$$p_u=p_v=0.\tag{13}$$

再利用严格恒等式

$$\mathcal R\cdot T=-a'-V\cdot T_\theta,$$

以及

$$V_\beta=T\times V=:W,$$

得到余下 $\delta^3$ 系数

$$-p_\beta\,W_{\rm cap}\cdot(T_{\rm cap})_\theta=0.
\tag{14}
$$

在所选单帽开角上，该系数非零。事实上帽的圆柱法曲率为 $\alpha_j'$，其角方向的法曲率系数绝对值为

$$\left|W_{\rm cap}\cdot(T_{\rm cap})_\theta\right|
=R\alpha_j'(R a_j-d)b_j^2>0.
\tag{15}
$$

只需选靠近顶点但严格在帽内的开角：此处 $0<R a_j-d<w$、$S_9'>0$ 且 $b_j\ne0$。未将帽中心的退化点包括在 (15) 内。

所以 $p_\beta=0$，即准确残差为零必要求

$$\boxed{\quad
P(\theta)=g_{rrr}(R,\theta)
          +\frac{g_r(R,\theta)}{3c_*^2}
\quad}\tag{16}
$$

在顶点两侧的这些开角上同时成立。这是当前表示的三阶 Cauchy 相容必要条件。证明没有对一般 $C^2$ 曲面求未经允许的高阶导数；高阶展开来自已指定表示的正则性。

## 4. 必需的 $v$ 补偿在每个顶点有非零角二阶跳

取相邻帽 $j,j+1$ 的共同顶点
$\theta_v=\theta_j+\pi/6$，记

$$\eta=\theta-\theta_v,\qquad
c_0=\cos(\pi/6)=\sqrt3/2,\quad
b_0=\sin(\pi/6)=1/2.$$

在左帽侧 $\eta<0$，$b_j\to-b_0$；在右帽侧 $\eta>0$，$b_{j+1}\to+b_0$。两侧 $a_j\to c_0$，且

$$R a_j-d=-Rb_0\eta+O(\eta^2)\quad(\eta<0),$$

$$R a_{j+1}-d=Rb_0\eta+O(\eta^2)\quad(\eta>0).
\tag{17}
$$

由 (1) 和 S9 的首项，单帽中

$$v=-\frac{\sigma126 A_j}{w^5}\,
b_j(ra_j-d)^5+O((ra_j-d)^6).$$

固定角度对 $r$ 求三次导数得

$$v_{rrr}=-\frac{\sigma7560 A_j}{w^5}\,
b_j a_j^3(ra_j-d)^2+O((ra_j-d)^3),
\tag{18}
$$

而 $v_r=O((ra_j-d)^4)$。定义严格正的常数

$$C_* =\frac{7560R^2c_0^3b_0^3}{w^5}>0.$$

于是 (16) 右侧的 $v$ 分量 $K_v$ 满足

$$K_v(\theta_v+\eta)=
\begin{cases}
\sigma C_* A_j\eta^2+O(|\eta|^3),&\eta<0,\\
-\sigma C_* A_{j+1}\eta^2+O(\eta^3),&\eta>0.
\end{cases}
\tag{19}
$$

饱和修正 $v_r/(3c_*^2)=O(\eta^4)$ 不改变该首项。因此角二阶导数的右极限减左极限为

$$\boxed{\quad
[\partial_\theta^2 K_v]_{\theta_v}
=-2\sigma C_*(A_j+A_{j+1})\ne0.
\quad}\tag{20}
$$

这是两邻帽幅度的**和**，不依赖它们是否相等，也不可能因正幅度对称而抵消。使用 $v$ 分量因此避免了只看 $\beta$ 时可能出现的相邻等幅特殊抵消。

然而 (5) 的 $P_v$ 是整个角圆上的实解析函数，特别是二阶导数连续。如果它在顶点左右开角分别等于 (19)，就会被迫同时具有 (20) 的两个不等二阶极限，矛盾。

**命题。** 在 (1)–(5) 的准确物理定义、S11 径向端阶、正帽幅度和有限解析角向自由空间下，不存在 $\mathcal R\equiv0$ 的参数选择。

## 5. 可改变的接口与仍未证明的事

本门不是 R48 的固定第五角跳，也不是 R51 的内部径向半整数出生：饱和源确实移除了后者，但没有自动补足准确单帽的三阶径向 Cauchy 数据。它也不是由有限 Gaussian 节点造成的评价误差。

若下一模型仅把三点外推改成保三阶的四点外推，必须同时处理饱和映射 $e-\varepsilon$ 的三阶项；只改变反射权重不能消掉 $g_r/(3c_*^2)$。例如对未饱和位移，节点 $0,-1,-2,-3$ 的外推权 $4,-6,4,-1$ 保到三阶，但这只消除本条低阶失配，不自动支付更高阶 Cauchy 条件。继续增加有限匹配阶数后，仍须重新核查下一个阶数及正曲率产生的约束，不能从“保了更多 jet”推出准确连接存在。

有实质区别的下一接口是：物理基场真正包含单帽完整 Cauchy 数据及必要的非解析角/径向过渡，或在自由空间中加入所需的非解析 Cauchy 列，再对其全角正则性、二 jet 拼接、准确度量、嵌入和全曲面 reach 分别验证。仅增加有限解析 Fourier 列仍保留 (20) 的准确零矛盾；它可以改善某个正容差下的近似，本文没有给出限制这种近似的误差下界。

这些改动须记录为新的连续表示或设计，不能将新物理基改名为旧模型的同状态求积精化。当前已运行 Actions 的模型、源码和冻结系数保持原样，仍应完整审计其真实残差、GH 加密、几何及来源。
