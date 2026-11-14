# 固定 g 下联合 u/v 与中心速度的全局帽高线性门

状态：纸面推导与下一求解接口设计。尚未选择真实新初态、求解器或大规模预算，也没有调用研究求解。正在运行或准备运行的短入口审计仍保原代码与原目标；本稿不修改它。

## 1. 需要保留的约束

下一求解应把共同帽高下限保为一条真正的线性不等式，单独于 direct-metric 和球/条带罚项。已有一次高度提案若只作为初始值，而后仍运行仅带系数盒的 least_squares，优化器可以再把帽子压低；这不是高度门被支付。

[R60](../results/R60-independent-center-speed-fixed-ports-and-position-two-jets.md) 的独立中心速度给出

$$
X(t,\theta;p,c)
=a(t)\Pi T(t,\theta;p)+z(t;c)e_z,
\qquad
z(t;c)=z_0+B_0(t)+\sum_{j=0}^{8}c_jI_j(t).
\tag{1}
$$

这里 $a$ 是已经选中并冻结的完整度量，$p$ 是当前 $u/v$ 参数，$B_0(t)=\int_0^t b_0(s)\,ds$ 的参考由不可变原 $c_0$、当前已选入口表示与固定 $g$ 定义。即使使用有界 atan 参考，它也不随本次当前 $p,c$ 变化。$I_j(t)=\int_0^t\widetilde C_j(s)\,ds$ 是选中入口权重后的高度列的共同原函数。

令 $\sigma$ 为侧号，$L$ 为内圆帽端，则

$$
h(p,c)=\sigma z(L;c)
=h_{\rm base}+\lambda^\mathsf Tc,\qquad
h_{\rm base}=\sigma[z_0+B_0(L)],\qquad
\lambda_j=\sigma I_j(L).
\tag{2}
$$

因此

$$
\partial_ph=0,\qquad \partial_ch=\lambda^\mathsf T.
\tag{3}
$$

这不是在各角圈或各径向查询处另选一个高度。仍然只有一个中心积分和一个帽高。冻结度量、核心、六帽、固定参考和高度基定义后，式 (2) 是同一个物理场族中的准确仿射关系。

现 $W_4$ 权重非负，标准正侧的 $\lambda_j$ 非负。原 B7 列在短入口之外，故 $\lambda_4=81/1000$ 准确；其他列也由准确分段多项式积分定义。实现暂用浮点评价时，不把该评价称为完整有理积分证书。

## 2. R66 门及数值评价边界

当前固定核心 $B=7/25$、六帽外半径 $R_{\rm cap}=137/500$、柱半宽 $w=1/50$ 和目标 $\tau=61/1000$ 下，[R66](../results/R66-core-flat-cap-two-normal-reach-height-gate.md) 的标准正侧必要条件为

$$
h\ge h_{\rm nec}
=\frac{81+\sqrt{3685}}{1000}.
\tag{4}
$$

若显式选择设计余量 $m_h\ge0$，本次约束是

$$
\lambda^\mathsf Tc\ge h_{\rm nec}+m_h-h_{\rm base}.
\tag{5}
$$

目前短入口审计采用的余量为 $m_h=1/1000$。后续 solver 不应在未记录时改成更低门限，也不能把新的核心 $B$ 偷换进式 (4)。若未来改变核心，则应由 R66 的完整分支重算；仅凭 $h>0$ 并不对所有参数都强迫同一个 upper 分支。

这里的 $\tau=61/1000$ 是明确选定的 reach 设计目标。式 (4) 的必要性以完整嵌入满足 $\operatorname{reach}\ge\tau$ 为前提；它不是仅从课题的 $0.03D$ 自动推出。球界 $D\le2.02$ 下该 $\tau$ 足够且留有余量；若只知核心迫 $D\ge2$，题目本身仅强迫 reach 至少 $0.06$。不应把某候选未通过这一更强设计门直接写成整个课题的排除。

式 (5) 的数学定义与数值评价须分开。$B_0(L)$ 是准确角均值与径向积分定义，而当前只有固定评价规则及有限精化差。因此：

- 物理约束身份保存准确的 $b_0$、$I_j$、R66 输入与余量定义；
- 数值评价身份另保存共同固定分区、GL 阶、角均值阶、热评价阶以及评价得到的截距和行向量；
- 优化过程中不悄悄更换这个截距的求积规则；
- 最终同态精化必须重新报告真实共同帽高和门限差，不把 finite difference 当严格误差界；
- 若以后得到 $h_{\rm base}$ 的区间包围，可用其下端建立保守行；目前不能声称已经有这种连续证书。

把高度门写成线性约束只支付这个必要条件。它不证明等距、浸入、镜合单射、曲率上界或非局部 reach。

## 3. 联合目标与准确导数

沿用 [R57](../results/R57-direct-reconstructed-metric-and-auxiliary-frame-space.md)：

$$
e=|X_t|^2-1,\qquad q=X_t\cdot T,\qquad
r_{\rm metric}=(e,\sqrt2\,q).
\tag{6}
$$

固定评价网格上保留已明确的均方归一化和当前球/条带 smooth-positive 项，总目标 $F=\tfrac12\|r\|^2$。现有解析位置参数列给

$$
\nabla F=J_r^\mathsf Tr.
\tag{7}
$$

对于高度列，所有位置与导数的变化已经是显式的：

$$
\partial_{c_j}X=I_j e_z,\qquad
\partial_{c_j}X_t=\widetilde C_j e_z,\qquad
\partial_{c_j}X_{tt}=\widetilde C'_j e_z.
\tag{8}
$$

$u/v$ 列影响 $T$ 和 $a\Pi T$，但不影响 $b_0$、$z$ 或帽高截距。由此 full state 中的高度行是

$$
A_h=(0_{\!u},0_{\!v},\lambda^\mathsf T).
\tag{9}
$$

式 (3) 只有在本次完整 $g$ 与参考已经冻结时才成立为一个固定行。若未来重启 body 度量设计，有界参考依赖完整 $a'$，$h_{\rm base}$ 便会随度量参数变化；那是另一个模型/导数任务，不能直接沿用此处的固定截距。

## 4. 三类可执行路线及其范围

### 4.1 SLSQP：原参数、一个线性行与原盒

保留当前物理系数，使用原 $u/v$ 和高度盒，加式 (5) 的单行约束。目标和梯度直接由已有 $r,J_r$ 生成，不新增辅助 beta 参数。

SciPy 官方 SLSQP 文档支持在 minimize 中传 bounds 和 constraints；新式 LinearConstraint 会被转换为内部约束形式。官方终止参数也涉及约束违反量，但 success 本身不是本课题的几何或高度证书。[S1]

这条路线的额外实现最少。它不承诺全部中间试探都满足高度门；必须分别记录试探点与满足帽高/盒的可选点，只有后者可成为最终候选。低于门的更小目标不能覆盖最后一个可行 checkpoint。

### 4.2 trust-constr：明确要求约束迭代保持可行

同样使用原变量和式 (5)，可给 LinearConstraint 的 keep_feasible 选项，并提供解析目标导数。官方明确说明该选项只被 trust-constr 使用，其他 minimize 方法不能据此保证中途可行；有限差分导数也可能产生违反约束的评价，因此这里应继续用解析列。[S2]

trust-constr 另有独立的最优性、约束违反和信赖域终止信息，报告时可以逐项保存。[S3] 这可能更适合要求帽高始终保留的后续单次求解，但不能在没有实际初态和人工边界例检查时宣布优于 SLSQP。起点正好落在高度或系数边界时，必须在人工测试中覆盖，不能默认为严格内点。

若使用 $J_r^\mathsf TJ_r$，应标明它是 Gauss–Newton Hessian 近似；残差不为零时它不是完整目标 Hessian。也可采用库支持的准 Newton 策略。当前不预先选定大求解的 Hessian、步长或迭代预算。

### 4.3 固定帽高的可行局部参数化：合法但更窄

取已选择的 $h_*$，令一个高度列依赖其他八列：

$$
c_4=\frac{h_*-h_{\rm base}-\sum_{j\ne4}\lambda_jc_j}{\lambda_4}.
\tag{10}
$$

这使共同帽高恒等于 $h_*$，但原 $c_4$ 盒变成其余高度变量的两条耦合仿射不等式。它不是只剩独立坐标盒的 least_squares 问题。

等价的零总积分列为

$$
\widehat C_j=\widetilde C_j-
\frac{\lambda_j}{\lambda_4}\widetilde C_4,\qquad j\ne4.
\tag{11}
$$

若在一个已知可行起点附近选足够小的独立扰动盒，并严格付

$$
\begin{aligned}
0\le\epsilon_j&\le\min(c_j-\ell_j,u_j-c_j),\quad j\ne4,\\
\sum_{j\ne4}
\left|\frac{\lambda_j}{\lambda_4}\right|\epsilon_j
&\le\min(c_4-\ell_4,u_4-c_4).
\end{aligned}
\tag{12}
$$

则这个局部子盒可保原系数盒和固定帽高。该做法允许复用带盒 TRF，但搜索的是 $h=h_*$ 的受限子类，不等价于全部 $h\ge h_{\rm nec}+m_h$。若只引入高度 slack，$c_4$ 的耦合盒约束仍然存在。

官方 least_squares 定义的是坐标盒约束；不能把普通 TRF 当成已经接受了式 (5)。[S4] 大权重高度残差也不是硬不等式的替代证明。

## 5. 初态与全局线性可行性

先等短入口实际审计选定模型与初始化，不同时改核心 $B$、目标度量或物理六帽。每个候选应被称为“帽高与系数盒数值可行”或“不满足这些约束”，不能简称几何可行。

固定盒 $\ell_j\le c_j\le u_j$ 时，单独高度行的最大可达值准确是

$$
h_{\max}
=h_{\rm base}
+\sum_j\max(\lambda_j\ell_j,\lambda_ju_j).
\tag{13}
$$

它只检查高度与盒是否兼容。B7 helper 的区间还含固定 $T$ 的样本球与 signed-height，因此它为空不等于整个联合 $u/v+$height 问题为空。

若 B7 无法提供初始化，而希望另设计九高度系数的最小改动，可先研究一个明确的小凸子问题

$$
\min_{\ell\le c\le u}\frac12\sum_j d_j^2(c_j-c_j^{(0)})^2,
\qquad
h_{\rm base}+\lambda^\mathsf Tc\ge h_{\rm target}.
\tag{14}
$$

这里要求所有 $d_j>0$，并先检查式 (13) 保证可行集非空；于是目标严格凸，最小点唯一。该问题的单乘子解具有

$$
c_j(\mu)
=\operatorname{clip}\!\left(
c_j^{(0)}+\frac{\mu\lambda_j}{d_j^2},\ell_j,u_j
\right),\qquad \mu\ge0.
\tag{15}
$$

左侧高度随 $\mu$ 单调，可由有限分段或一维根找满足门的点。这里仅给接口备选，没有实施额外初始化或把它混进当前一次 B7 审计。任何这样的改动都须冻结真实新系数并重新计算中段 $E/F$、球和镜合；它可能改动入口自由的下一阶高度项。

## 6. 球、条带、signed-height 与 reach 不能混为一门

当前原目标使用球半径 $R_{\rm ball}=1.01$、条带半宽 $0.38$。这次正在执行的初态审计继续如实报告原目标。

以后若要调整目标，应注意：在完整曲面确满足该球界、且原长轴端点确实保留时，支持见证给

$$
D\le2.02,\qquad
\delta_{\rm hold}\ge1-p.
$$

幅度门只要求 $p\le0.394$。原 $0.38$ 留有额外余量，可能比数学门更严格；$p=0.394$ 则没有连续认证误差余量。这些都是条件预算，不能把当前有限样本当全域包围。若后续改 $p$ 或权重，必须登记新 objective，先在同一个场上分别评价旧、新成本，不把换目标造成的数值变化当优化下降。

联合 $u/v$ 变化下，样本球与 signed-height 不再只是高度系数的线性限制。它们的解析列分别来自

$$
\partial\!\left(\frac{|X|^2}{R_{\rm ball}^2}-1\right)
=\frac{2X\cdot\partial X}{R_{\rm ball}^2},
\qquad
\partial(\sigma X_z)=\sigma\,\partial X_z.
\tag{16}
$$

若继续仅作为 smooth-positive 项，其通过与否仍须独立审计；若以后改成 NonlinearConstraint，则是明确新增的约束任务和成本，不能暗中宣称旧目标已经硬性支付。

同样，帽高门和当前帽片自身曲率界不支付连接带的实际主曲率或完整闭面的非局部法弦。B7 一步只建立下一求解可用的高度起点，不应被称为完整几何进展。

## 7. 需要保存的接口和回执

建议后续独立模块提供如下职责，名称仅是待实现接口：

- HeightAffineGate：绑定固定 $g$、固定参考、准确高度基、R66 分支和设计余量；返回物理定义与数值截距/行的两个身份。
- margin(state)：计算式 (5) 的数值余量，$u/v$ 列恒零。
- reconstruct_margin(problem,state,data)：用同一个 query-independent 共同原函数的 center(L) 独立重核实际帽高，并报告与仿射行的差。
- scalar_objective_and_gradient：缓存一次现有解析 $r,J_r$ 的结果，返回 $\tfrac12r^\mathsf Tr$ 与 $J_r^\mathsf Tr$。
- select_checkpoint：分别保留最佳帽高/盒可行点和最低目标试探点；最终选点只从明确允许的前者中取。
- freeze_and_refine：冻结准确 binary64 有理系数，断言完整 $g$ 不变，再作同态角均值、$\Pi$、共同原函数的独立精化。

变量缩放可以使用 $y=S\widehat y$，但必须同步用 $J_rS$ 和 $A_hS$，原系数盒也同时变换。实际物理状态仍保存未缩放的准确系数，不把 solver 坐标混入字段定义。

SLSQP 或 trust-constr 的 success、迭代次数、停止原因、约束违反量都保留，但都不替代最后的完整位置审计。中途预算结束只保存已计算的 checkpoint；不得把一个稍越高度门但成本较低的试探点悄悄改成结果。

## 8. 公开人工检查先于真实联合求解

真实 solver 尚未实施。实现后至少应在公开人工数据上检查：

1. 一个无约束最小点会压低帽高的二次 toy，约束版本确将候选保在声明的行与盒内。
2. 初态在高度边界和系数边界上的情况，保存清楚的成功或失败原因。
3. 人工位置模型中，式 (3) 的零 $u/v$ 列和高度列与独立有限差分一致，实际 center(L) 与行值一致。
4. 式 (10) 消元后的耦合盒确实仍被处理；不能遗漏 $c_4$ 越界。
5. 只选择高度/盒可行 checkpoint；预算退出、错误输入身份、评价规则改变均不产生误标。
6. 研究参数仍只从公开仓库 Actions 进入，人工检查不读取实际系数，也不伪造 Actions 环境。

代码中的数学行不依赖某个 SciPy 发行版；具体运行仍须记录 Python/NumPy/SciPy 版本。下列官方页面本次访问显示 SciPy 1.18.0，并不代表现有 Actions 环境就是该版本。

## 9. 一手 API 来源

[S1] SciPy，minimize(method='SLSQP')：
https://docs.scipy.org/doc/scipy/reference/optimize.minimize-slsqp.html 。

[S2] SciPy，LinearConstraint，尤其 keep_feasible 的求解器范围：
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.LinearConstraint.html 。

[S3] SciPy，minimize(method='trust-constr')：
https://docs.scipy.org/doc/scipy/reference/optimize.minimize-trustconstr.html 。

[S4] SciPy，least_squares 的目标与盒约束定义：
https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html 。

以上来源访问于 2026-11-14。它们支持接口选择和限制；式 (1)–(16) 的本题几何与线性结构推导由本文及所引仓库结果给出。
