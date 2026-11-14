# S9 六弓形准确端口：代数身份、全 jets 与人工检查

2026-11-14，mechanism。独立实现 `scripts/polygonal_flat_tail_port.py`，没有修改旧七个已发布运行依赖，没有接入或重跑新的研究 runner。全帽准确几何证明由 `repo_sources` 独占，见 [R44 六边形帽证明](../results/R44-S9-six-cap-exact-embedding-and-normal-chord.md)。本文只说明接口及其开发检查。

## 1. 准确的物理身份

外半径、握持盘半径、幅度列表固定为

\[
R=137/500,\quad r_c=11/50,\quad
(A_0,\ldots,A_5)=(3/16,1/8,1/8,3/16,1/8,1/8).
\]

边法向为 \(n_j=(\cos(j\pi/3),\sin(j\pi/3))\)。所有坐标通过有理部分和 \(\sqrt3\) 系数的字典准确保存，而不是保存三角函数打印值。弦偏距和弓高准确为

\[
d=(R/2)\sqrt3,\qquad w=R-(R/2)\sqrt3.
\]

这里 \(w\ne R-r_c\)：后者只是原径向开放尾的长度。二者不混用。

物理身份还包括 S9 的准确整数系数、全六幅度顺序、反射号、积分定义和闭盘定义域。浮点 \(\sqrt3\) 和 Gauss 积分只作同一个模型的数值评价，不进入准确身份。

`PolygonalFlatTail` 拒绝超出 \(r\le R\) 的普通调用（仅容许表示该边界所需的机器舍入余量）。这很重要：六个准确弓形只在源闭盘内保证互不交，不能把盘外重叠的圆柱公式误认成同一个等距延拓。

## 2. 标量与位置接口

对第 j 片，设

\[
a=e_r\cdot n_j,\qquad b=e_\theta\cdot n_j,
\qquad z=r a-d,\quad \alpha=A_jS_9(z/w),
\quad C=\cos\alpha,\ S=\sin\alpha.
\]

每点最多一片活跃，因此可把各片相对平尾的零背景增量相加：

\[
u_j=\arctan\frac{(1-C)ab}{1-(1-C)b^2},\qquad
v_j=-\frac{\sigma bS}{\sqrt{1-b^2S^2}},\qquad
(\Delta\beta)_j=\sigma\arctan(aS/C).
\]

全场 \(u=\sum u_j,v=\sum v_j,\beta=-\sigma\pi+\sum\Delta\beta_j\)。分母统一为正，不需要 unwrap。它们产生的准确 frame 是

\[
T=e_\theta+\sum_j[(C_j-1)b_jn_j-\sigma b_jS_j e_z],
\]

\[
V=-e_r+\sum_j[(1-C_j)a_jn_j+\sigma a_jS_j e_z].
\]

由唯一活跃片性质，二者始终单位正交，且准确满足
\(V_\theta+T-rT_t=0\)。方向约定仍是 \(dr/dt=-1\)，返回字段 `s` 表示这个 core-to-cap 的 t 导数。

`scalar_jets(r,theta)` 重用已冻结的 `Jet22` Taylor 代数，返回每个标量的
`value,s,ss,theta,st,tt,ss_theta,ss_thetatheta`。

`position_jets(r,theta,height=h,quadrature_order=32)` 返回
`X,Xs,Xtheta,Xss,Xst,Xtt,normal,principal_curvature_absolute,height_drop`。
其中位置定义是

\[
P_\sigma(q;h)=(q,\sigma h)+
\sum_j[(Y_j(z_j)-z_j)n_j-\sigma H_j(z_j)e_z].
\]

所有片共用一个 h。接口不会替每片或每圈选不同高度。

对单片，代码直接实现以下增量；其余是在平极坐标 jets 上相加：

\[
\begin{aligned}
P_{tt}&=-a^2S\alpha'n_j-\sigma a^2C\alpha'e_z,\\
P_{t\theta}&=-e_\theta+
[b(1-C)+rabS\alpha']n_j+
\sigma[bS+rabC\alpha']e_z,\\
P_{\theta\theta}&=-re_r+
[ra(1-C)-r^2b^2S\alpha']n_j+
\sigma[raS-r^2b^2C\alpha']e_z.
\end{aligned}
\]

平区与片界的全部修正 jets 准确归零。S9 角度为 C4、位置为 C5；没有声明顶点无限阶平坦。

## 3. 同一理论预算与接口限制

`analytic_budget()` 记录一般公式

\[
K_*\le\frac{315A_{\max}}{128w},\quad
\rho_*\ge\frac{128w\cos^2 A_{\max}}{315A_{\max}},\quad
\Delta_H\le A_{\max}w/2.
\]

在本次固定 \(R\) 和 \(A_{\max}\le3/16\) 下，引用独立证明的严格有理下界 \(\rho_*>3/40\)。这是**全帽点对**法弦界，不是帽到未知桥的 reach，也不是任意盘外延拓的认证。

完整 position/state 身份与同 g 连接器尚需未来独立 runner 绑定。现模块没有把旧全跨度右端 Hermite lift 搬进来，也没有使用失败的大残差状态作暖起点。未来若使用这只准确帽，其物理模型与旧 S11 单方向尾不同，必须另建完整身份。

## 4. 人工检查范围与结果

本地 `--check-only` 只用了人工半径 \(9/10\)、握持盘半径 \(3/5\)，以及幅度
`[1/7,1/9,1/9,1/7,1/9,1/9]`。没有评价本次研究选择的真实参数，也没有优化。

正、负两侧结果一致：

- 标量到 ss_theta 的有限差分比较最大相对误差约 \(1.18\times10^{-9}\)；
- 位置全二 jet 的比较最大相对误差约 \(2.61\times10^{-10}\)；
- 准确 E/F/G 的浮点误差约 \(2.22\times10^{-16}\)；
- 目标积分性残差约 \(3.10\times10^{-16}\)，frame 与位置导数差约 \(3.89\times10^{-16}\)；
- 两重/镜面对称检查、顶点有限 jets、S9 端点准确有理 jets、固定两阶求积比较均通过；
- 超出源闭盘的调用被拒绝。

这些数字是人工实现检查，不能作为真实 core/bridge/帽组合的连续证书。模块仍明确标记浮点 jets 和求积没有区间误差认证。

开发命令：

```bash
python topics/visible-flex-new-mechanism/scripts/polygonal_flat_tail_port.py \
  --check-only \
  --out "$RUNNER_TEMP/polygonal-flat-tail-port-check.json"
```

当前交付仅为准确帽端口。新的完整连接求解器、暖初态的公开预评价、固定 g 精化和完整 reach 仍未完成。

后续完整连接入口与本次部署范围见 [饱和热runner冻结说明](frame-collar-saturated-heat-implementation-20261114.md)；本端口检查本身不转授整体可行性。
