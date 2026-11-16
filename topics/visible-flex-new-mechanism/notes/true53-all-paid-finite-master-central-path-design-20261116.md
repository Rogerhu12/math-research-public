# true53 已付完整有限主问题：原始–对偶中心路径的新方法

日期：2026-11-16。数学重参数化与界的部分是下文完整纸证；有限浮点算法及其可能结果只作数值证据。当前没有新执行，也没有新合格方向或实际点。

## 1. 问题来源与新工作的准确范围

[首轮 true53 投影](true53-projected-direction-first-actual-no-qualified-direction-20261116.md) 的唯一 run `43811870681`、research job `133115100791` 已结束。23 次完整分离全部负 gain，末有限主问题仍超原始容差；其一百万坐标上限和保留的最后分离槽均不能作为重开该 session 的理由。原 `solve_complete_projection`、Hildreth、旧 HiGHS64 和 conic32 都不调用。

真正尚未解决的是：**已保存的全部原 selected 行及五条新梯度，是否支持原始可行的正 gain？** 旧投影只安装了小部分 metric 行；当前原 MODEL 已保存 5743 条 selected metric 梯度、2937 条 hard 梯度，以及五条后来新求的原 metric 梯度。这里一次性使用这些已付行，不重新建几何、J、JVP、原主问题或 guard。

新问题是一个明确的有限线性规划，方法改成同时求 primal/slack/dual 的中心路径 Newton 系统。它不是继续原投影的未完坐标迭代，也不消费原剩余额度。

原始来源固定为：

- source commit `42f95905deec3024dfee7a687bdc806d38c79baf`；
- research raw log 35105831 B，SHA-256 `fa7edaf1419325ce31e6926de44f8c9ebbddf1ea554d140fafef61aecbc9ceb9`；
- `TRUE53_PROJECTION_MODEL` 原 JSON+LF 27365833 B，SHA-256 `926681688d09311883c64dfa1dc40599a62d1904d7f6dbcaf478893fe14bd539`；
- 该完整模型 binding `e095e93d1455302af6904e703e762adad05d9cdef7220761c468e3ea0efca9a1`；
- 同一 `COMPLETE` 和 `FINAL_CLOCK` 给未变的接受点 53、完整状态与已付总额 1594.440227096 秒、128 次 ordinary value。新工作从这个总额另计，不能重复累加 cone32 或 p32。

程序只从上述原 stdout 读取模型。原大数组不经 Git、artifact、Release、cache 或对话传输；新 stdout 保存真正新结果，原输入以原 run/tag/hash 引用。

## 2. 同一原始有限问题的准确重建

令 $z\in\mathbb R^{159}$，实际独立步长仍是

$$
p=S z,\qquad
S=\operatorname{diag}(\mathrm{actual\_step\_scale}).
$$

令 $h$ 为原 163 个物理坐标的 infinity 范数上界：

$$
K=\operatorname{diag}(1/\mathrm{width})\,M\,
\operatorname{diag}(\mathrm{qscale}),\qquad
|Kz|\le h.
$$

整个 $M$、163 维 coupled 盒、原 trust、外坐标界、所有 hard targets 和四条 group8 guard 均从 MODEL 原样使用。没有把 $159$ 个独立坐标盒替代物理盒。

令 $r=\mathrm{common\_radius}=0.001$，把新的 gain 坐标写成

$$
d=r\gamma .
$$

原投影使用 $d=\mu s$，其中 $\mu=10^{-6}$。现在只是一个正的可逆坐标变化；几何步长、范数代价和所有原残差完全不变。选择 $r$ 的用途是让 gain 列与典型物理步长列处于相近量级，不改变 $d$ 本身。

对每个已付 metric 行 $j$，原当前值为 $\phi_j$、原物理梯度为 $g_j$，放入

$$
g_j^\top Sz+\mu h+r\gamma\le\phi_0-\phi_j.
\tag{1}
$$

5743 条 selected 行的原 margin 是 `target - phi_j`，故右端直接等于 `phi0 - target + margin`。五条新梯度已有原 `base_gap`；不重求 $\phi_j$。固定 target 常数分支是

$$
\mu h+r\gamma\le\phi_0-0.26.
\tag{2}
$$

hard 行完整保留

$$
-J_iSz+a_{h,i}h\le \mathrm{base}_i-\mathrm{target}_i,
\tag{3}
$$

其中原 `hard_original_h_column` 也从原记录读取，不能因预期是零就删掉。其余 652 个物理/范数行及 320 个外界行按原 `build_primary` 顺序原样重建。既有 scalar soft 行在这里按原意义成为 (1)，没有删掉任何 hard 条件。

新有限问题为

$$
\max_{(z,h,\gamma)} r\gamma
\quad\text{subject to (1)—(3) and every original domain row.}
\tag{4}
$$

**等价性证明。** 映射 $(z,h,s)\mapsto(z,h,\mu s/r)$ 可逆，逐行把原有限 maximin 不等式变为 (1)—(3)。原物理步长不变，且 $r\gamma=\mu s$。所以它精确保持该有限行集合的可行域、gain 和最优值。这里扩大的是纳入的已付 metric 行集合，不是物理域或容差。证毕。

(4)仍只包含已经有梯度的有限行；完整 coarse/fine 两网格其它行尚无资格由它推定。即使 (4)达到很小 primal/dual 残差，也必须另做真正新方向的完整分离。

## 3. 字面零行、外界和数值缩放

程序保留原不等式及原标签。只有**每个浮点系数字面等于零**的行才在 Newton 数组中单独处理：若其原 RHS 非负，它是已记录的常量真式；若 RHS 为负，严格有限模型有常量冲突，不能通过容差删行或硬加 diagonal jitter 隐藏。原容差结论单独记录。

对每个非零行，以

$$
\omega_i=\max(\|a_i\|_\infty,|b_i|)
$$

作正行缩放 $A_i=a_i/\omega_i,\ B_i=b_i/\omega_i$。这是有限问题的等价变换；所有可行性门最终都回到未经缩放的原行。

外界在原记录里应有严格宽度。如果某个外界是字面固定坐标，程序先把其固定值作准确仿射代入，再保留全部原行用于回验。不能对一个只有很小宽度的坐标作近似固定。

## 4. 同时求 primal/slack/dual 的 Newton 方程

写缩放后的问题为

$$
\min c^\top x,\qquad Ax+s=B,\quad s>0,
\qquad c=-e_\gamma .
$$

$\lambda>0$ 为不等式乘子，记

$$
r_p=Ax+s-B,\qquad r_d=A^\top\lambda+c,\qquad
\bar\mu=\frac{s^\top\lambda}{m}.
$$

不要求初值原始可行；初值 $x$ 取外界中点及 $\gamma=0$，$s_i=\max(1,B_i-A_ix)$，$\lambda_i=1$。这些值仅是算法初值，不能作为原始可行证据。

对给定互补右端 $r_c$，完整 Newton 方程是

$$
A\,\Delta x+\Delta s=-r_p,\qquad
A^\top\Delta\lambda=-r_d,\qquad
\Lambda\,\Delta s+S_s\,\Delta\lambda=-r_c,
\tag{5}
$$

其中 $S_s=\operatorname{diag}(s)$，$\Lambda=\operatorname{diag}(\lambda)$。消去 $\Delta s,\Delta\lambda$ 得

$$
A^\top W A\,\Delta x
=-r_d+A^\top S_s^{-1}r_c-A^\top W r_p,\qquad
W=\operatorname{diag}(\lambda/s).
\tag{6}
$$

回代

$$
\Delta s=-r_p-A\Delta x,\qquad
\Delta\lambda=S_s^{-1}(-r_c+\Lambda r_p+\Lambda A\Delta x).
\tag{7}
$$

(6)—(7)直接代入即给 (5)，因而正负号不依赖黑盒约定。若计算系统无法求解，记录失败；不擅加正则项后仍称精确 Newton。

先用 $r_c=s\lambda$ 求 affine predictor。用其保持正性的最大步估算 $\bar\mu_{\rm aff}$，取

$$
\sigma=\min(1,\max(0,(\bar\mu_{\rm aff}/\bar\mu)^3)).
$$

corrector 用

$$
r_c=s\lambda+\Delta s_{\rm aff}\Delta\lambda_{\rm aff}
-\sigma\bar\mu\,\mathbf1.
\tag{8}
$$

最终 primal 与 dual 各取 $0.995$ 倍到边界步长。每次实际 Newton 系统、所有 predictor/corrector 和发生的失败都计数。矩阵和右端可作正 diagonal 对称平衡；这只是 (6) 的可逆变换，回代必须报告原 (5) 残差。

这是一个明示的浮点算法，不预先承诺有限步收敛、最优性或发现不可行。人工例子和旧开发 suite 均不为防错另跑；直接求这个未解的实际有限问题，保留全部真实诊断。

## 5. 原始门与非精确 dual 也可使用的上界

每个候选都保存真实 161 维 primal、原单位逐类最大残差、$h_{\rm actual}=\|Kz\|_\infty$、修复 $h$ 后的全部有限 metric 最大值和 gain。原 hard/物理/范数/外界门用 $10^{-7}$，metric 用 $10^{-9}$；任何缩放残差很小都不能替代这些门。

有限问题对完整网格问题给松弛，因此其最优 gain 是完整问题的上界；**一个有限可行点的正 gain 不是完整下降的下界。**

还可避免把近似 stationarity 冒成精确对偶证书。把原行写成

$$
a_{i,x}^\top x+a_{i,\gamma}\gamma\le b_i,
\quad x=(z,h)\in[\ell,u].
$$

对任意非负原单位乘子 $\lambda$，若
$\nu=\sum_i\lambda_i a_{i,\gamma}>0$，则每个严格可行点都满足

$$
\gamma\le
\frac{\lambda^\top b-\min_{x\in[\ell,u]}
(\sum_i\lambda_i a_{i,x})^\top x}{\nu}.
\tag{9}
$$

右端最小值逐坐标是 $q_j\ell_j$（$q_j\ge0$）或 $q_ju_j$（$q_j<0$）。证明只是非负加总所有原不等式，再用整个外盒下界。若只要求带原容差的可行，除把每个 $b_i$ 换成 $b_i+\mathrm{tol}_i$ 外，支持函数也须在原 bound 行实际放宽后的 $[\ell_{\rm tol},u_{\rm tol}]$ 上取最小值。当前各坐标两侧都是原单位 $\pm1$ 行，故分别扩展该行容差；字面固定并准确代入的坐标仍固定。不能把 bound 行 RHS 放宽，却继续用精确原盒的支持函数。如果无法从原行恢复放宽外盒，就不提供该版本上界。

代码中的 (9)仍是 binary64 诊断，未作 outward rounding，不称严格数值证书。若它不为正或出现负 gap，必须先看原始可行性及舍入范围；不能仅凭这个数宣驻点或不可行。

## 6. 一次新执行及后续衔接

这次新范围只做一次 (4) 的实际有限求解，最多 96 个 predictor–corrector 迭代、192 个 Newton 系统，科学总时限 240 秒，含原日志读取、数组恢复、矩阵装配、所有失败和输出。0 普通几何、0 hard-J 重建、0 JVP、0 新 metric 梯度、0 scalar line、0 实际试点。该范围不是给旧64/32/投影增加额度。

一次原日志读取恢复上述 MODEL 和同次 COMPLETE/FINAL_CLOCK。不重新运行来源计算。新程序保存新 primal/dual/slack、真实迭代记录、行重建来源、原单位门和可供下一步消费的实际候选；原5743/2937/五条梯度只引用已存原记录，不复制到 Git。

下一步由此次实际结果决定，并继续工作：

- 若有限模型给原始可行且修复 gain 为正的候选，用这个确切方向做新的完整 coarse/fine 分离，保原全部 hard/163 盒及精确舍入条件；通过后才能进入完整 affine-$e/f$ 标量线和原实际两网格门。
- 若求解未达原始门，只记录该实际失败，继续具体剩余数学或算法问题；不把有限迭代耗尽称不可行，也不重复已付模型构建。
- 若上界或互补结构给有用信息，必须按 (9) 的实际证明范围解释，不能用它降低主课题的等距、reach 或全时标准。

本设计不改变第53点、$\eta=0.26601514422985384$、曲率上界58、target0.26、共同 $g$、实际物理参数或最终完成标准。
