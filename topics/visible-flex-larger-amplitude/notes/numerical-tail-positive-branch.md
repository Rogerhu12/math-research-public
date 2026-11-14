# Tail 中 A、D、S 与 projectionFloor 的精确定义

这是固定源码所用数学变量与数值 guard 的直接推导；不是尾存在性或全图 reach 的证明。来源为固定 commit `869436630c99aa5a68afb55bd8877c826034d117` 的 `general_exact_tail_cauchy_raw.mjs`、`general_root_tail_momentum.mjs`、`78718-tail-fourier-root-momentum.mjs` 以及 compact-tail factory。代码路径相对于本题的固定 source dependency cache，逐文件摘要见本节末。

## 高度图与三个无量纲量

背景度量和背景高度写成
\[
 g=E(r)\,dr^2+r^2d\theta^2,\qquad E=1+w^2,\qquad b'(r)=w(r)>0.
\]
完整高度为 $Z=b+v$。程序的相对变量是
\[
 P=\frac{v_\theta}{rw},\quad K=\frac{v_r}{w},\quad
 L=K+P_\theta.
\]
于是程序中三个 guard 量恰为
\[
 S=1-w^2P^2=1-\frac{Z_\theta^2}{r^2},
\]
\[
 D=1-w^2\bigl(2K+K^2+E P^2\bigr)
   =E\left(1-|\nabla_g Z|_g^2\right),
\]
\[
 A=1+L+w^2P_\theta
  =1+K+E P_\theta.
\]
设水平投影度量 $\gamma=g-dZ^2$。直接计算得
\[
 \gamma_{\theta\theta}=r^2S,\qquad \det\gamma=r^2D.
\]
故 $D>0$、$S>0$ 保证所选水平投影图非退化；事实上 $D=ES-Z_r^2>0$ 已推出 $S>0$。代码分别检查二者，是为了保留显式数值余量。$D=0$ 会使该高度/水平投影坐标失效，但不单凭这一点排除可用别的坐标描述的嵌入。

## A 是角向 Hessian/法曲率的归一化量

因为 $\Gamma^r_{\theta\theta}=-r/E$，
\[
 \operatorname{Hess}_g Z(\partial_\theta,\partial_\theta)
 =Z_{\theta\theta}+\frac rE Z_r
 =\frac{rw}{E}A.
\]
对精确等距嵌入、选取 $n_z>0$ 的法向，有
$n_z=\sqrt{D/E}$，并且 $\operatorname{Hess}_gZ=n_z\,\mathrm{II}$。
因此单位角向切向量的法曲率为
\[
 k_\theta
 =\frac{wA}{r\sqrt E\sqrt D}.
\]
在 $r,w,D>0$ 下，$A>0$ 等价于这个方向的法曲率为正。$A$ **不等于** Frenet 速度约束余量，也不是 metric error。

$A=0$ 本身并不等价于浸入失效。它表示角向法曲率为零，并使该程序用径向二阶高度导数作为未知量的 Darboux 正分支求解退化；能否经过该点继续，属于另一张解图或另一分支的问题。不能从本求解器在 $A$ 接近零时拒绝，推出全体等距嵌入不存在。

## 动量 root 和正定矩阵

程序每个径角节点处并非直接令 $L$ 等于线性值，而是求完整有限谱角连接动量矩方程
\[
 \Pi_M\bigl(L+\mathcal Q(L,P,P_\theta)\bigr)=\mathrm{target},
\]
其中常数模的 target 为零（平均连接/holonomy 条件），其余模由当前动量给定。$L$ 取常数模加前 $M$ 个余弦模。`root()` 对这个系统作 Newton。

从源码 `evaluateL` 的 `bm` 表达式整理，Newton 矩阵的离散角积分恰为
\[
 B_{ij}=\frac1N\sum_{a=0}^{N-1}
 \frac{A(\theta_a)}{D(\theta_a)^{3/2}}
 e_i(\theta_a)e_j(\theta_a),
\]
$e_i$ 为离散正交归一余弦基。代码中的 `I + bm` 写法仅用于小量稳定计算，因为
$1+\mathrm{bm}=A D^{-3/2}$。
因此 $A>0,D>0$ 使 $B$ 正定，可用 Cholesky。最小权重趋近零时，矩阵条件数和径向流敏感性都可能增长；这解释了正根 guard 的数值作用。

## .05 的地位与可以怎样改变

compact-tail factory 的默认 `projectionFloor` 是 .05；独立 momentum engine 的默认值是 .1，但主线 factory 显式把 .05 传入 engine。随后 root/原始高度方程都执行 `D>floor && S>floor && A>floor`，Newton 试步也受同一限制。

数值 **.05 不是上述几何恒等式、动量矩方程、Darboux 方程或给定度量的一部分**。把它改为更小的严格正数，仅扩大所接受的正分支试步区域，不改变数学方程或物理背景 $g$。这可以作为从一个已成功正分支解继续的有意义实验，但应记录该算法参数的改变，并重新核验实际收敛残差、角向分辨率、矩阵条件数、$A,D,S$ 正性、曲率及最终固定参数加密。

不能将降 floor 当作自动成功：可能存在真实正分支边界，也可能是错误 warm、有限谱误差或 Newton 方向失效。尤其 `multiple-shooting line search failed` 只说明其有限次试步没有找到下降点；即使当时最小 A 约 .054，也不足以断言将 floor 降至 .01 必能继续。跨越 $A=0$ 更不属于简单降正 floor，因为现有 Cholesky/SPD 正分支结构可能失效。

本题原尾 M4 最后点 minA=.050254，确实紧贴默认 guard；其 normalizedFullDefect≈.01656，先有谱误差问题，不能把该低阶点作为降 floor 的存在证书。优化旧尾 M16 req9 的失败迭代 minA≈.05441，而最后成功点 minA≈.25798；失败迭代不是解，必须与成功解分开。

## 固定源码摘要

- `repro/source-root/topics/large-amplitude-twist-flex/scripts/general_exact_tail_cauchy_raw.mjs`：`0c8139fd146a52188a6eedfe898003f8417d745c2fcde6f2a9eb5479aa7855df`。
- `repro/source-root/topics/large-amplitude-twist-flex/scripts/general_root_tail_momentum.mjs`：`182847f2ff1b27ff211364729c2969e4b417973efe0bba5977b2ef26e500528c`。
- `scripts/78718-tail-fourier-root-momentum.mjs`：`cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88`。
- `scripts/78718-tail-tangent-core.mjs`：`ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3`。

## A 在实际流里是 guard，还是被反演？

两者均有。`f6tail_momentum_split_flux.mjs` 中动量 RHS 的显式 flux 分母为 $S\sqrt D$，没有直接写 $1/A$；但它先调用 $L$ 的非线性 root。实际 two-jet evaluator `f6tail_momentum_physical_jets.mjs` 对此 root 作隐式求导，明确计算
\[
 \dot L=B^{-1}\,\mathrm{right},
\]
并用它恢复 $v_{rr}$。所以去掉正性 guard 不能消除对 $A$ 加权算子的反演。

更直接地，令径向数值参数为 $x$，$r_x\ne0$，$k=(\log w)_x$，并令
\[
 U=K_\theta-P,\qquad \beta=\frac{r_x}{w}v_{rr}.
\]
源码计算的全点 Darboux 残差正是正因子乘以下式：
\[
 A\beta-G,
\quad
 G=\frac{r_xE}{r}U^2-kL+kw^2(KP_\theta-P^2).
\]
因此精确连续方程在这一径向演化图中是 $\beta=G/A$。原始高度 Galerkin 代码将它投影后解 $B\beta_M=\langle D^{-3/2}G e_i\rangle$；实际动量版本则通过 root 与隐式微分实现相关有限谱演化，不能假定两种有限截断的 second jets 完全相同。

当 $A=0$ 而 $G\ne0$，该图的 $v_{rr}$ 必然发散。当 $A=G=0$ 时，点上方程是特征退化，可能存在有限二阶导数但不能由此径向Cauchy式唯一求出。有限维 $B$ 在 $A$ 变号后偶尔仍可逆，只表明该矩阵没有零特征值；它不构成连续乘子可逆、C²控制或谱极限的证明。跨越时需要新局部图或额外兼容条件，现有 root、variational RHS 和 physical-jet 三条路径的 SPD/Cholesky 假设均须重新分析。

由 Gauss 方程还可作更精确区分。背景
\[
 K_g=\frac{w w_r}{rE^2},\qquad
 k_{r\theta}=\frac{wU}{r\sqrt D}.
\]
在 $A=0$ 的点，$k_\theta=0$，所以精确曲面必须满足
\[
 -k_{r\theta}^2=K_g.
\]
负 Gauss 点允许此相容关系；正 Gauss 点则不允许零方向法曲率。

尤其在本余弦/反射对称 ansatz 的反射轴 $\theta=0,\pi/2$，所有正弦项为零，故 $U=0$。**若**某个瓶颈恰在这些轴上，且对应 $w_r\ne0$，则 $A\to0$ 会迫使
\[
 k_r=\frac{K_g}{k_\theta}
     =\frac{w_r\sqrt D}{E^{3/2}A}
\]
发散；不能用“负 Gauss 可有渐近方向”越过这个轴上的特殊约束。该结论是条件性的：尚未为所有实际最后成功点定位最小A的角位置，不能把它套成当前幅度的存在性上界。只要 $A$ 保持严格正且较小，是否仍满足曲率预算取决于实际 $w_r,D$，不是 .05 这个固定数值本身。

补充调用路径摘要：

- `f6tail_momentum_physical_jets.mjs`：`2b96df25211c5d6ebfc7faf689ea7035704bf0bf7c1ea3aa50b1c137fbe39ea8`。
- `f6tail_momentum_split_flux.mjs`：`5d77ca058adb634547c91998002eeffb9de5395a9e1e130f7edd4fa65014f578`。

## 已定位的 M24 实例

完整混合路径最后成功的 \(\lambda=.5390625\) 有
\(A_{\min}=.2225870681\)，位置是反射轴 \(\theta=0\)、
\(r=.2348117057\)。这里 \(w_r=-.0010335153\)，形式主曲率约为
\((.00341156,-.00463799)\)，所以最小A点仍只有很小的曲率。
对应Gauss残差为 \(1.76\times10^{-8}\)，这些是有限谱两jet数据，
不将它们写作精确连续Gauss解。

同一实际尾的 \(\kappa_{\max}=8.02216621\) 位于别处
\(r=.2866580088,\theta=.83448555\)，此处 \(A=.99292013\)。最坏
Gauss缺陷则又在 \(r=.2770684831,\theta=0\)：内禀Gauss曲率为
\(-1.30802\times10^{-5}\)，有限形式主曲率一正一负，但其乘积误差
仍为 \(+2.65869\times10^{-6}\)。因此正分支裕量、最大曲率和最坏
Darboux误差是三个不同诊断，不能互相替代。

完整点位、轴上比较与输入哈希见
`numerical-m2-smallcut30-q02-lambda05390625-curvature24.json`；原始真实
求解及全尾audit见 `numerical-m2-smallcut30-q02-tail24-parts8-finepath-response_0009.json.gz`。
