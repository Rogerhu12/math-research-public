# 有限 momentum 图中的 A：正性、条件数与角向法曲率

状态：**以下恒等式有完整证明；对候选的定位只是现有数据解释，待独立审查，不是新求解或连续正分支证书。**

作者：`/root/tail_theory`，2026-11-09。此记录回应 M14/M16 继续加频时的 branch guard 问题。

下文是源码所表示的实数数学模型；未假设实际双精度的 `exp(2*logw)` 与 `exp(logw)**2` 逐位相等。相关舍入误差不由这些恒等式支付。

## 1. 源变量的含义

引用本题已冻结的
`repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs`
和 `f6tail_momentum_physical_jets.mjs`。为避免与曲率预算混淆，把源码的 `K` 在本文记为 $k$。变量满足

$$
E=1+w^2,\qquad k=L-P_\theta,
\qquad u_r=w(1+k),\quad u_\theta=rwP.
$$

源码中的三个支路量为

$$
S=1-w^2P^2,\qquad
D=1-w^2(2k+k^2+EP^2),\qquad
A=1+L+w^2P_\theta.
$$

因此有精确恒等式

$$
D=E-w^2\bigl((1+k)^2+EP^2\bigr),\qquad
A=1+k+EP_\theta.
\tag{1}
$$

$D>0$ 控制高度梯度相对于目标度量的余量。$A$ 并不是第一基本形式的面积因子；不能把 $A$ 的下降直接解释成嵌入失败。

## 2. Newton 矩阵的加权 Gram 形式

令 $c_0=1$、$c_j=\sqrt2\cos(m_j\theta)$。有限角网格满足源码的无混叠次数条件，因此在精确算术下

$$
\frac1N\sum_{\ell=0}^{N-1}c_i(\theta_\ell)c_j(\theta_\ell)=\delta_{ij}.
$$

源码初始化 $B=I$，再累加

$$
b_m c c^{\mathsf T}/N,
\qquad a_m=L+w^2P_\theta=A-1,
$$
$$
b_m=a_m+(1+a_m)\bigl(D^{-3/2}-1\bigr)=AD^{-3/2}-1.
$$

所以

$$
B=\frac1N\sum_{\ell=0}^{N-1}
\frac{A(\theta_\ell)}{D(\theta_\ell)^{3/2}}
c(\theta_\ell)c(\theta_\ell)^{\mathsf T}.
\tag{2}
$$

还需证明这个矩阵确实是 moment 映射的 Jacobian。记 $s=\sqrt D$，源码的 $f_c,g_c$ 满足

$$
\frac12+f_c=\frac1{s(1+s)},\qquad
1+g_c=\frac1{Ss}.
$$

把源码中的点态 nonlinear moment 修正记为 $q$，化简后得到

$$
L+q=\frac{s^{-1}-1}{w^2}
       +\frac{(1+k)P_\theta}{Ss}.
$$

在固定 $Q,r,w$ 时，$P,P_\theta,S$ 不随 $L$ 变，且 $\partial_L D=-2w^2(1+k)$。利用 $D+w^2(1+k)^2=ES$，逐项微分得到

$$
\begin{aligned}
\partial_L(L+q)
&=\frac{1+k}{D^{3/2}}
 +\frac{P_\theta\bigl(D+w^2(1+k)^2\bigr)}{S D^{3/2}}\\
&=\frac{1+k+EP_\theta}{D^{3/2}}
=\frac{A}{D^{3/2}}.
\end{aligned}
$$

再对点态 moment 作同一有限角网格的 Fourier 投影，链式法则给出的系数 Jacobian 正是 (2)。因此后文使用该矩阵的正定性来推导 moment 映射的单调性有直接依据。

若各角节点上 $A\ge a_*>0$、$0<D\le D^*$，则

$$
\lambda_{\min}(B)\ge \frac{a_*}{(D^*)^{3/2}}>0.
\tag{3}
$$

这是正定性的充分条件；$A$ 在某个角点很小，不等于整个有限 Gram 矩阵已经奇异。另一方面 $A$ 趋零确实会削弱这一通用下界，可能增加角向 root 的敏感性。式 (2) 是离散数学恒等式；实际双精度三角表及累加另有舍入误差，本文未作浮点本征值认证。

## 3. 与角向法曲率的关系

这里作一个明确的条件假设：$u$ 是某个对

$$
g=E\,dr^2+r^2\,d\theta^2
$$

精确等距浸入的高度函数，且取上向法线。由 (1)，

$$
n_z=\sqrt{1-|\nabla_g u|_g^2}=\frac{\sqrt D}{\sqrt E}.
$$

目标单位角向向量为 $e_\theta=r^{-1}\partial_\theta$，其高度 Hessian 为

$$
\nabla_g^2u(e_\theta,e_\theta)
=\frac{u_{\theta\theta}}{r^2}+\frac{u_r}{Er}
=\frac wr\left(P_\theta+\frac{1+k}{E}\right).
$$

利用 $\nabla_g^2u=n_z\,\mathrm{II}$，得到

$$
\mathrm{II}(e_\theta,e_\theta)
=\frac{wA}{r\sqrt E\sqrt D}.
\tag{4}
$$

这也恰是冻结 height-jet 代码中的形式角向二阶系数。因而当 $w,r,D$ 保持适当正界时，$A\downarrow0$ 对应这一方向的法曲率趋零；它不是曲率上界趋于无穷的同义词。式 (4) 不把有限 Galerkin 的形式第二基本形式当成已验证实际 XYZ 图的第二基本形式。

## 4. 高频为何敏感

若高度的某一项为 $h_m(r)\cos(m\theta)$，则

$$
P_{\theta,m}=-\frac{m^2h_m(r)}{rw}\cos(m\theta).
\tag{5}
$$

中谷的小 $w$ 与 $m^2$ 会放大很小的高频高度系数对 $A$ 的影响。这是结构性的坐标敏感性，不能仅凭新增高度系数很小就认为 branch margin 几乎不变。升频时保持旧 raw height/slope 再重算 momentum 的做法与此一致；直接给新增 momentum 模补零不具有同一含义。

## 5. 对已有 raw0/segment4 定位的解释

`db6f-prefix-tail-quadrature-m14-initial-solved.json` 记录的 M14 低 $A$ 点位于 raw0、segment4、原 profile 坐标 $x=1/4$，对应 p8 的相邻 stage 端点。这里仅引用已有数值定位，不新算或认证其最小值。

冻结构造中 segment4 是中谷 plateau。该段 `valleyControls[0]=3.125` 为常数，`warpWeightLevels[0][2]=3` 为常数，cap level 为保存的 $0.1$。未 cap 的 $\log w$ 关于原 profile 坐标是严格递减的仿射函数；恒定 cap 保持其单调性。因此该位置不同于 segment5 中 $w_x$ 变号造成的尖锐径向尺度。已审 depth2 primitive 中，这一整段的 16 个叶都是 analytic 叶，没有 range 叶。

$x=1/4$ 本身只是 shooting 分段点，不是 raw-cell 端口；这里没有新的 $2^{11/4}$ momentum 端口缩放。现有资料因而未显示此处有明显的径向 cusp 或人为端口归一化错误。仍须保留：这不排除一般 RK、角积分、Newton 条件数或高频截断误差。

由此更有依据的下一步是逐级升频、保持 raw 状态含义，并在下一次已有 root 计算中观察 $D,S,A$、Newton 矩阵及高频贡献。本文不建议把降低 `projectionFloor` 当成解决问题本身，也未证明某一更低 floor 的继续过程有效。

## 6. 初始 root guard 与真实 root 的区别

这是源码中一个具体但尚未归因到本次失败的风险。`root(state,profile,x,guess)` 在没有 `guess` 时直接以 `L=target` 为初猜；循环中的第一次 `evaluateL` 就执行 D/S/A guard。因此，**Newton 尚未迭代的初猜被拒绝，并不证明该角向方程没有可行 root。**

可以精确说明可行分支的结构。固定 $r,w,Q$，则每个角节点上的 $P$、$P_\theta$、$S$ 已固定，而 $L(\theta)$ 对未知 Fourier 系数为线性函数。由 (1)，

$$
D=ES-w^2(1+L-P_\theta)^2.
$$

给定 $f>0$，先假设各节点 $S>f$。于是 $ES-f>0$，条件 $D>f$ 等价于

$$
-\frac{\sqrt{ES-f}}w
<1+L-P_\theta<\frac{\sqrt{ES-f}}w.
$$

条件 $A>f$ 等价于 $L>f-1-w^2P_\theta$。这些都是系数空间中的开线性半空间；它们的交集 $\mathcal C$ 为凸域，允许为空。

在非空 $\mathcal C$ 内，$D\le E$，所以由 (2)

$$
B\succeq\frac{f}{E^{3/2}}I.
$$

令 $\Phi(L)$ 为 moment 映射。对任意 $L_0,L_1\in\mathcal C$，沿域内线段积分其 Jacobian 得

$$
(L_1-L_0)\cdot(\Phi(L_1)-\Phi(L_0))
\ge\frac{f}{E^{3/2}}\|L_1-L_0\|^2.
$$

因此该可行凸域内的 root 至多一个。无论用哪个可行初猜，若真正解到同一个原方程及原 guard，数学上仍是该唯一 root；这不要求降低 floor 或改变物理度量。

若未来日志证明失败发生在第一次角向 root 评估，重用邻点或前次成功 root 的 $L$ 作为候选初猜是一个有理由检验的方向；仍须先验证新 $Q,r,w$ 下该初猜可行，并重新检查完整残差。本文没有运行这一修改，也没有保证它总能找到初猜或 root。若失败源自 $S\le f$，由于 $S$ 不依赖 $L$，改变角向初猜本身不能修复它。
