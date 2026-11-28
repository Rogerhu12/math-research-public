# R618：从真实 seed 到 R579 的 canonical 核心输入生成器

2026-11-28，Astra-new-mechanism-8cdb3418-20261128。
**状态：源码完成，尚未执行新的科学计算，没有选择新的 $\mu$。**
源码为 `scripts/r618_convex_core_input_path_20261128.py`。
它供 hard-total-trace 后继使用；当前 centered run 的输入和源均不变。

## 1. 正确的角规范及 seed

构造器只消费真实 `HardTotalTraceHeight` 中从实际接受响应提取的
`seed_pc`、`seed_trace['e']` 和完整 source 身份。
不给当前场另转一个 $\pi/2$：这里 $\phi$ 始终是**外法线角**，

$$Y_\theta=R(-\sin\phi,\cos\phi),\qquad \psi=\phi+\pi/2,$$

且 $\theta=\phi=0$ 是右端支撑点。两个坐标反射给四个象限的同一 canonical 曲线。
R618 旧 position 的 tangent 角是 $\psi$，不是这里的 $\phi$。

对同一个 seed 多项式 $P_*$，生成器以声明的连续求积近似重新评价
$\langle(e+2P_*)^{-1/2}\rangle=1$，如实记录它与原512点 root 的差异。
这是新路径实际需要的连续函数评价，不更改 seed 的多项式、原 $E_*$ 或原接受状态。
在 $\mu=0$ 时，返回的24个 $P$ 系数逐项就是原 seed；若扩大 $J$ 则只补零。
不把新 ODE 误差写成首态的变化。

seed 的法线角反函数按

$$\frac{d\theta_*}{d\phi}=u_*(\theta_*),\quad
u_*=(e_*+2P_*)^{1/2},\quad\theta_*(0)=0$$

实际积分。随后准确导数公式为

$$\rho_*(\phi)=R u_*(\theta_*(\phi)),\qquad
\rho_*'(\phi)=R P_*'(\theta_*(\phi)).$$

这里没有数值差分。所有 quarter endpoint 漂移都输出；不缩放角周期或旋转坐标来藏误差。

## 2. 每个显式 $\mu$ 的真实输入

R579 的 $L_\epsilon,r,p,q$ 按其准确积分定义评价，$\epsilon=1/1000$、$R=17/20$。
设 $\Delta\rho=\rho_1-\rho_*$，则 $\rho_\mu=\rho_*+\mu\Delta\rho$。
在材料角上同时积分

$$
\phi_\theta=R/\rho_\mu,\quad
I_\theta=\Delta\rho\,R/\rho_\mu,\quad
Y_\theta=R(-\sin\phi,\cos\phi),
\quad I=\int_0^\phi\Delta\rho.
$$

完整路径方向使用

$$
\dot\phi=-I/\rho_\mu,\qquad
\dot u=\{\Delta\rho+\rho_\mu'\dot\phi\}/R,\qquad
\dot P=u\dot u-\dot e/2.
$$

$e_\mu-e_*$ 用准确因式分解
$\rho_\mu^3-\rho_*^3=\mu\Delta\rho(3\rho_*^2+3\mu\rho_*\Delta\rho+\mu^2\Delta\rho^2)$
求积，避免在小 $\mu$ 时先算两个相近的大积分再相减。
$P_\mu-P_*$ 也按增量组装。外部参数是 exact rational/decimal 字符串；
增加 $J$、角点或改变评价容差时，数学 target 仍是同一 seed 与同一 $\mu$。

新生成器给 retained modes 的 $P_\mu$、$\dot P_\mu$，以及 $N$ 和 $2N$ 的系数差、
采样截断误差、剩余已分辨偶系数和、曲率半径范围、canonical 核心支撑/包围球观测。
这些均是观察，不是无限 Fourier tail、全域误差、连接解或 reach 证书。
有限谱输入进入真实高度后仍必须重新消费其自身的同根 $\mathcal T(P)$。

## 3. 此输入没有隐含的宏观可解性

R579 的小椭圆参数可使曲率半径动态范围很大；生成器不假定 $J=48$ 足够。
宏观核心仍受原完整连接、fixed-E 均值分支、嵌入、跨片 reach 和固定 $g$ 精化所约束。
本源码没有新 workflow，没有选择 $\mu$，也不预置一个可由优化抹掉的自由核心。

另一个 $R=.8,\epsilon=.05$ 的厚核心将属于新设计输入与新参考度量。
它不能传入当前 $R=.85$ 构造器。后继新 factory 必须实际重建外段、字典和参考场，
再从自己的真实 seed 构造同形式路径；当前 target86da 和旧接受/误差结论不得跨用。
