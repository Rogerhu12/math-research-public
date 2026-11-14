# 正 C epicycle 倾角探索：精确公式、实际小样本和未付证书

2026-11-09；root / Astra-visible-flex-db6f0b0e。
**状态：作者代数推导待独审；浮点取样仅启发式。**
本稿不进入 results，不更新原 η=1/√2 的 R46/R49 参数，不属于 flat17 加密。

## 1. 冻结可重现源与实际执行

源：scripts/db6f-root-positive-epicycle-seed-scan.js，3,528 B；
固定 commit 4155fcf7218c06c9ecf56611acc63b33b2137ac4，
Git blob ce7234bf9005aabf2810a66c8b4b47fa5056361b。
root 按固定 commit 全文回读逐字一致后，实际以 functions.exec 的 JavaScript
隔离运行时运行同一源码的 scanEpicycleSeeds({count:360})，
开始与返回均为 2026-11-09 23:31:59 UTC。
它返回 HEURISTIC_FLOAT64_SAMPLES_ONLY，共 7 个倾角，每个 360 个角样本。
没有终端进程退出码，没有 PDE、隐函数求值、主 solver 或既有研究数据读取。
节点坐标/点对数组只在运行内临时使用，未通过集成保存或输出。

此前 23:19:43 UTC 有同一核心函数的探索运行。
再前一个临时版本的严格模式指令与默认形参冲突，被 JavaScript 解析器拒绝，
未进入采样；冻结源已修正该语法问题。
当前固定源码可在恢复的 Node 中运行：

    node topics/visible-flexible-closed-surface/scripts/db6f-root-positive-epicycle-seed-scan.js 360

终端 Node 路径目前尚未执行。固定源码的 flags 明确不提供 reach、嵌入、
正曲率或共同度量族的证书。

## 2. 必须随倾角一起改变的完整公式

令 $3-2\sqrt2<\eta<1$，$\sigma=\sqrt{1-\eta^2}$，

$$
p^2=\frac{2(1-\eta^2)}{1+6\eta-3\eta^2},\qquad q=\sqrt{1-p^2}.
$$

取
$\bar d=R_z(\theta)R_y(\arccos\eta)(p\cos3\theta,-p\sin3\theta,q)$，
$d_0=-\bar d$。一般倾角时

$$
\bar d_W=\sigma q e^{i\theta}
+\tfrac12p(\eta-1)e^{4i\theta}
+\tfrac12p(\eta+1)e^{-2i\theta},\qquad
\bar d_z=\eta q-\sigma p\cos3\theta.
$$

尤其水平频率 1 系数和余弦系数使用 $\sigma$，
不能把只在 $\eta=\sigma=1/\sqrt2$ 时相等的旧公式直接套来。
竖直向量面积常数为

$$
(1-\eta^2)q^2+\tfrac12p^2(\eta^2-6\eta+1)=0,
$$

水平分量由 C3 消去。计算周期原函数 $c'=d_0\times d_0'$ 可得

$$
c_W=i\{Re^{i\theta}+Ae^{4i\theta}+Pe^{-2i\theta}
                  +Be^{7i\theta}+Ce^{-5i\theta}\},\quad
c_z=-U\sin3\theta-V\sin6\theta,
$$

其中

$$
\begin{aligned}
R&=\sigma\{\eta+(3-\tfrac32\eta)p^2\},&
A&=pq(1-\eta)^2/4,\\
P&=pq(2+\eta-\eta^2)/2,&
B&=\sigma p^2(1-\eta)/28,\\
C&=\sigma p^2(1+\eta)/20,&
U&=\sigma pq(3-2\eta)/3,\quad V=\sigma^2p^2/12.
\end{aligned}
$$

令 $J=(\eta-3)q-\sigma p\cos3\theta$、$W=10-6\eta$。
在速度非零处，

$$
k^2=W-J^2,\qquad
\kappa=\frac{J^3-(19-9\eta)J-3Wq}{(W-J^2)^{3/2}}.
$$

这些是完整一般倾角的作者代数式，尚未单独交未参与者全文审查。
实际取样中 $|c'-(d_0\times d_0')|$ 的最大浮点残差
为约 $3.65\times10^{-15}$；这个样本核不替代恒等式证明。

## 3. 有限取样给出的方向，而非全域下界

η=1/2 的 360 样本中，κ 约落在 [.05697,4.57898]，
中心线点对直径最大样本约 3.40088。
原直纹带在 v=0 的冻结形算子为

$$
\begin{pmatrix}0&-1\\-1&\kappa\end{pmatrix},
$$

相应局部曲率半径与该样本直径之比约 .06141。
这不是曲面 reach/D 的下界，样本直径本身也不是直径上界。

更关键的是有限平坦出口。若以同一入口的冻结
$a=1,M=-1,C=\kappa>0$ 比较 $Q=0$，形算子变成秩一，
其非零特征值为 $\kappa+\kappa^{-1}$。
因此很小的 κ 虽使原带的一侧曲率较小，却可能让平坦出口很弯。
上述冻结系数模型不冒充实际有限 δ 解；真实 M、C 的变化还需 PDE 估计。
这解释了为何不能只按原带的最大 κ 排参数。

η=3/5 的样本 κ 范围约 [.1348783,6.6289330]，中心线直径最大样本约 2.90352。
样本 normal-chord 最小值约 .1510201。
normal-chord 对全域取下确界才与中心线 reach 有关；
有限取样的最小值不提供那个下确界的正下界。
本稿没有将 .151 或任何据此形成的比例当作已证明结果。

## 4. 一个系数较简单的备选 η=3/5

此时 $\sigma=4/5,p^2=4/11,q^2=7/11$，位置系数简化为

$$
R=12/11,\quad A=2\sqrt7/275,\quad P=56\sqrt7/275,\quad
B=8/1925,\quad C=32/1375,
$$

$$
U=24\sqrt7/275,\qquad V=16/825.
$$

这些式子没有混用 η=1/√2 的系数。端点 $c=\cos3\theta=\pm1$ 的曲率式为

$$
\kappa_\pm
=\frac{4080\sqrt7\pm5216}{(688\mp192\sqrt7)^{3/2}}.
$$

令 $t=-J$，曲率对 t 的导数分子为

$$
\frac{2176}{25}+8t^2-\frac{288}{5}\sqrt{\frac7{11}}\,t.
$$

它的全实轴最小值为 $5792/275>0$。
因此配合正速度，可把这个种子的全角曲率界归结到上述两个端点；
这一作者推导仍待完整独审。

若后续继续本分支，具体未付步骤是：
严格的中心线全点对 reach 下界；足够薄直纹带及实际平坦延拓的整体
reach 传递；实际有限变形参数和像幅度。既有 R45 的 reach 不能移来。

## 5. 当前优先级

几何分工另在证明从平坦端向非减 Q 起步的光滑存在定理，
并构造近圆柱的实际固定 H 族。该路线有望用更直接的全局弦长和 Hessian
控制取得目标 reach，无须本分支的复杂两角全点对证书。
因此本倾角取样先保留为备选，不继续把大量采样当证明累加。
实际闭合、有效 .05D 幅度、主 flat17 G5 和最终独立全流程均保持未完成。
