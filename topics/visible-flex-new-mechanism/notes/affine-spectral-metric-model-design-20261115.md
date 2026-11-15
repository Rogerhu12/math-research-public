# 仿射 metric 两变量的凸谱模型：同一 159 维几何、同预算切平面设计

作者责任：本稿由本会话的研究协作代理编写；数学推导、源代码范围和运行结果的区分由本会话负责。本文是新算法设计，尚未运行任何新人工、LP 或真实几何计算。旧实际只读消费。

## 1. 已观察的问题与本次唯一改动

已完成的因子化 actual 为 run `43716860154`、source `a7bb0a16f4ba434a4e88c4f0519ccc4f7806c498`、job `132820200829`。第 6 模型在保持 $B=1/8000$ 后，没有新增粗/细行，真实两网 metric 下降为 $6.199635707027085\cdot10^{-7}$，标量 LP 预测为 $5.398433585785539\cdot10^{-6}$，比值约 $0.11484138$。第 8 模型新增 1 条粗行和 5 条细行，细网 metric 反而增大。全部已评硬门通过不等于软目标模型准确。

旧报告没有保存每个 metric 行的 $(de,df)$，所以不能从这两条现象认定哪一种非线性是主因。新增模型只针对一个原式上确实存在的缺口：当前代码先将 $e,f$ 合成为谱函数，再把整个谱函数线性化；本稿保留其范数曲率，只对 $e,f$ 做仿射近似。

这不是新表面自由度。原 $g,b_0$、完整 163 物理系数及 159 独立坐标、五个真实 null-height 坐标、原两网、行 ID、全部物理盒、支持与 cap、曲率及其他硬门都继承。原标量 spectral 正则量仍是 $\epsilon=10^{-8}$。新内层只用 HiGHS；不引入另一个锥规划依赖。

## 2. 同一真实原式及两种 epigraph

令 $U=X_s$、$T=X_\theta/a$。原几何保证 $|T|=1$，因此归一 metric 差为

$$
\mathcal E=
\begin{pmatrix}e&f\\ f&0\end{pmatrix},
\qquad e=|U|^2-1,\qquad f=U\cdot T.
\tag{1}
$$

真实 $\eta=\|\mathcal E\|_{\mathrm{op}}=(|e|+\sqrt{e^2+4f^2})/2$。原 proposal 的两函数为

$$
\phi_\sigma(e,f)
=\frac{\sigma e+\sqrt{e^2+4f^2+\epsilon^2}}2,
\qquad \sigma\in\{1,-1\}.
\tag{2}
$$

原 group 0 对应 $\sigma=1$，group 1 对应 $\sigma=-1$；legacy slot 名称不改变该规范。固定 metric 目标 $b=13/50$，软 row 仍是 $b-\phi_\sigma$。两函数的最大值在真实 $\eta$ 之上，偏差不超过 $\epsilon/2$。实际验收仍用未正则化的原 $\eta$ 与原 Schur 行。

在一个已接受的实际基点 $x$，取独立增量 $p\in\mathbb R^{159}$。每个现有选中软行 $i$ 保真导数为

$$
E_i(p)=e_i+d e_i\,p,\qquad
F_i(p)=f_i+d f_i\,p,
\tag{3}
$$

$$
d e_i\,p=2U_i\cdot \delta U_i,\qquad
d f_i\,p=T_i\cdot\delta U_i+U_i\cdot\delta T_i.
\tag{4}
$$

新有限模型约束

$$
\phi_{\sigma_i}(E_i(p),F_i(p))\le b+\rho.
\tag{5}
$$

这等价于

$$
\left\|(E_i(p),2F_i(p),\epsilon)\right\|_2
\le 2(b+\rho)-\sigma_i E_i(p).
\tag{6}
$$

右边非负已包含在该范数不等式中。若同一点两个 branch 都被选中，可写范数加 $|E_i|$ 的同一个 epigraph；实现仍按原整数 ID 分别保留，不能因此压缩、改排或凭空补齐旧池。未入池的网格行仍由原全值与学习机制处理。

$\rho$ 是旧 soft slack 辅助变量，仍满足 $\rho\ge\max(0,\rho_{\mathrm{out}})$，没有上界。物理步长范数辅助变量、原 $161=159+2$ primary 变量布局和原目标 $\rho+\text{weight}\cdot h_\infty$ 保留。这里的 $h_\infty$ 是原物理盒归一范数辅助量，与几何高度函数无关；固定 curvature auxiliary 仍不优化。

## 3. 凸性与原 scalar LP 的精确关系

$(E,F)$ 对 $p$ 仿射，(2) 是仿射函数加 Euclidean 范数，故每个 (5) 的左边凸。设

$$
v_i(p)=(E_i(p),2F_i(p),\epsilon),\qquad
n_i(\bar p)=\frac{v_i(\bar p)}{|v_i(\bar p)|}.
$$

$\epsilon>0$ 保证所有有限 $p$ 均有光滑梯度。在任意内层点 $\bar p$，

$$
\begin{aligned}
\phi_{\sigma_i}(E_i(p),F_i(p))
&\ge c_i(\bar p)+g_i(\bar p)p,\\
g_i(\bar p)
&=\frac12\{(\sigma_i+n_{i1})de_i+2n_{i2}df_i\},\\
c_i(\bar p)
&=\frac12\{(\sigma_i+n_{i1})e_i+2n_{i2}f_i+n_{i3}\epsilon\}.
\end{aligned}
\tag{7}
$$

等号在 $p=\bar p$ 成立。$p=0$ 的切平面就是旧 scalar spectral row；这将由真实同一 $de,df$ 与原 J 的逐行链式导数比对，而不从两 branch 的 J 相除反推 $df$。特别是 $f=0$ 不产生奇异恢复。

沿任意 $p$，记 $v_0=v_i(0)$、$\Delta v=v_i(p)-v_0$、$r_0=|v_0|$、$z=(v_0/r_0)\cdot\Delta v$。谱曲率余项为

$$
d_i^{\rm spec}
=\phi_i(E_i(p),F_i(p))-\{\phi_i(e_i,f_i)+D\phi_i(0)p\}
=\frac{|v_0+\Delta v|-r_0-z}{2}\ge0.
\tag{8}
$$

两个 branch 在同一点的该余项相同。可用

$$
d_i^{\rm spec}
=\frac{|\Delta v|^2-z^2}
 {2(|v_0+\Delta v|+r_0+z)}
\tag{9}
$$

作稳定诊断；原始直接差及浮点负微量仍要如实记录，不能裁剪后冒准确零。新模型只保 (8) 这一项，并不包含真实 $e,f$ 对参数的全部二阶导数。

## 4. 切平面 LP 与有界返回规则

### 4.1 原数组与新 cut

先调用冻结的 `selected_model` / `build_primary`，得到全部旧原行、163 物理耦合盒与 norm 行。所有 hard 原行和 RHS 不变，旧 $p=0$ 的 soft 平面也保留。按原布局 $p=\operatorname{diag}(\text{step_scale})z$，(7) 给新增行

$$
[g_i(\bar p)\operatorname{diag}(\text{step_scale}),-1,0]\,
(z,\rho,h_\infty)
\le b-c_i(\bar p).
\tag{10}
$$

每条新 cut 绑定原 grid、原整数 row ID、branch、同一接受基点和 $de,df$ 的数组 SHA，以及切点的实际二进制增量。新行不是新的表面取值点，不占原物理 pool，也不能授权忽略后来的真实新行。

### 4.2 必须直接计算完整模型

每次 HiGHS 返回有限原单位可行解后，先恢复真实独立增量 $p$，再完整评价所有现有 soft 行：

$$
\rho_{\rm aff}(p)
=\max\left(0,\rho_{\mathrm{out}},
 \max_i\{\phi_{\sigma_i}(E_i(p),F_i(p))-b\}\right).
\tag{11}
$$

不得把 LP 的 $\rho_{\mathrm{LP}}$ 当作 (11)。将返回辅助变量上调到 (11) 不改变 $p$、$h_\infty$ 或任何 hard/box 行，且满足全部范数约束及全部已有 supporting cuts。最终以实际修复后的完整数组再做原单位 residual 检查。浮点实算只给浮点可行性声明，不授区间证书。

记录

$$
\Delta_{\rm epi}
=\max\left(0,\rho_{\rm aff}(p)-\rho_{\mathrm{LP}}\right).
\tag{12}
$$

原始有符号差单独保留。拟固定每个 outer 模型最多 3 次 primary HiGHS 调用，即至多两个新增切面轮次；每轮对当前有实质违反的全部旧 soft 行加 cut，而不是只追一个 worst row。

定义本次切面停止阈值

$$
\tau_{\rm cut}
=\max\left(\text{原 metric row tolerance},
 \frac18\max(0,\rho_0-\rho_{\rm aff}(p))\right).
\tag{13}
$$

这只是求有限 proposal 的精度选项，不改变真实门的任何 tolerance。$\Delta_{\rm epi}\le\tau_{\rm cut}$ 标为 `evaluated-affine-epigraph-gap-met`。不声称经过浮点 HiGHS 的有限 cuts 已给严格最优证书。

### 4.3 预算、未收敛与返回

所有 inner HiGHS 调用都立即计入原共享 12 次 LP，包含初次 primary、切面修正和原 SOC。每次调用仍受原每 LP 10 秒及剩余共享 120 秒中的较小者控制。所有 cut 构造和范数评价也算新阶段 active wall time。原两网 value 上限 40 不增加。

仅保存已经通过原单位 LP residual、原物理 step/box 检查，并将 $\rho$ 按 (11) 上调后的候选。以修复后的原目标 $\rho_{\rm aff}+\text{weight}\,h_\infty$ 选择当前最好候选。不能把零步自动当 reserve 可行 incumbent：原 strip/curvature proposal floor 可能使接受基点本身不满足更强的 proposal RHS。

若因 3 次内层上限、剩余共享 LP、wall、重复 cut 或数值失败停止：

- 已有合格候选且 $\rho_0-\rho_{\rm aff}$ 超过原 improvement floor 时，可以返回它，但必须标明有限模型 gap 未达标及停止原因；预测只用 (11)。
- 没有这样的候选则返回具体失败/模型停滞，保留最后实际接受点；不把 LP 下界改善当实际模型下降。
- 不补发旧 primary，不扩预算，也不把内层 cut 数计为免费操作。
- 若剩余最后一次 LP 已用完，允许按原流程评最后一个已形成 proposal；不能再发 SOC 或下一 LP。

算法不保证比旧 scalar LP 更快；本次实验的决定性信息是同样预算下的真实下降、所需切面数、原模型误差两项和新增真实行的分账。

## 5. 回溯、SOC 与控制器的准确范围

本次修改 primary 的有限软模型。原 SOC 仍使用实际 $y$ 两网的原 row 值，加已接受基点的旧 scalar J，原硬 margin、原 box/correction 半径、原 scaling 与真实验收不动。它是保留的独立 correction proposal，不将它冒称已求解新凸模型。

原 SOC 的预算由旧 scalar primary gain 形成。冻结的 `frame_entry_tail_height_blocks.build_correction` 直接调用 `predicted_slack(primary,p)`，后者重新取同一 $p$ 的准确 scalar-model minimum slack $\rho_{\rm lin}(p)=\max(0,\rho_{\rm out},\max_i\{-v_i-J_ip\})$；它没有借用某次 LP 返回的非最小辅助 $\rho$。正是这个 $\rho_{\rm lin}(p)$ 不大于 (11)，所以其原 soft correction 预算比按新模型形成的预算更严格（若两者均有正 gain）。若未来换 API 使用 LP 辅助值，必须另核该比较前提。本次不借新模型放宽该 RHS。其旧线性预测、原 parabolic 线性界作为 proposal 来源单独保存。

对每一个实际 primary、SOC 和 parabolic candidate，控制器的整体预测统一直接用该 candidate 相对原接受基点的实际舍入总位移 $s=z-x$ 代入 (11)。这样不把折线/曲线的旧 scalar 上界当新凸模型值。原比值阈值、下降验收、halve/grow 常数、支持/低阶不变量和所有 hard gates 不改；改变的是预测函数，必须在 evaluation identity 中显式记载。

成功 SOC 保持半径的原 17 条规则继续核全部真实条件。其 base-total 诊断需要将旧 scalar 预测替换为同一 $s$ 的 (11)，同时保留旧预测作为历史说明；物理 $z-x$ 与 $z-y$ 范数、pool/model/point 绑定、原单位 solver residual 和全部门不变。不能仅换标签而继续把旧 scalar 数作为新模型的 ratio 分母。

新的 original model signature 必须包括 $e,f,de,df$ 与 policy SHA。否则同样的 scalar J 并不能唯一确定新模型。

新真实粗/细行出现时，按旧流程回到最后已接受点并重建当前池的模型；不能拿旧 $de,df$ 或 supporting cuts 跨越 pool、state 或 grid 身份。

## 6. 两项误差与遗漏行的完整账

对于已评价 candidate，在同一原 selected row 上定义

$$
\ell_i=\phi_i(e_i,f_i)+D\phi_i(0)s,\quad
m_i=\phi_i(E_i(s),F_i(s)),\quad
a_i=\phi_i(e_i^{\rm actual},f_i^{\rm actual}).
$$

则准确代数分解为

$$
a_i-\ell_i
=\underbrace{m_i-\ell_i}_{d_i^{\rm spec}\ge0}
+\underbrace{a_i-m_i}_{d_i^{e,f}\text{ 可正可负}}.
\tag{14}
$$

所有 actual $e,f$ 来自已经计算的同一完整 ordinary cache，在学习新行之前按原 ID 提取；不另调用 geometry 或 J。每 branch/grid 保 extrema、最坏原 row ID、两项和及 identity residual。不能把 $d_i^{e,f}$ 叫作谱范数曲率。

最大值一般在不同 row 达到。定义包含原外部 soft bound 与零 floor 的 $\rho_L,\rho_M,\rho_A$，分别对应 selected $\ell,m,a$；令 $\rho_F$ 为同一已评价完整两网的正则化谱 slack，$\rho_T$ 为真实 $\eta$ 的 slack。则

$$
\rho_T-\rho_L
=(\rho_M-\rho_L)+(\rho_A-\rho_M)
 +(\rho_F-\rho_A)+(\rho_T-\rho_F).
\tag{15}
$$

第一项非负，第三项是遗漏网格行的余量且非负，第四项绝对值至多 $\epsilon/2$；第二项可有任意符号。不要用行级余项最大值替代这些最大值差。若 fine 未真正评价，只记录 coarse 分解，并显式标记缺少完整两网；不估计 fine。

(14) 是本次新增必需的两项分解；(15) 则避免把第 8 模型这种新行现象误归给第一项。此前 m6/m8 没有这些数据，所以本稿不追认其原因。

## 7. 新文件与最小原接口

只在独立 pending 写新文件，不改冻结旧 source：

1. `frame_metric_affine_spectral_model.py`：纯数组的 (2)–(15)、cut 装配、精确模型评价、有限 inner LP 返回/计数；使用原 `ArrayLP`/原物理 map 和 HiGHS，不构造几何。
2. `frame_selected_row_metric_observables.py`：复用已发 selected-J 的完整角 kernels、三径向虚方向、径向收缩和五 null-height，但在同一虚方向流中同时输出 soft 行的真实 $de,df$。硬 J 原函数仍逐行调用；不另生成 163/159 全角参数张量，不从两个 branch 反除 $f$。
3. `frame_metric_height159_affine_spectral.py`：从已付 FactorizedHeight159Objective 扩展所需 cache，保持 state/pool/version/grid/row-order/evaluation SHA；调用冻结 primary 数组构造后附新模型；outer loop 只替换 primary solver/共享计数/精确预测与新增误差诊断。
4. `frame_metric_height159_affine_spectral_audit.py`：完整严格 handoff、原 24 输入与首批新人工/新阶段输出。原七输入恢复加刚完成 factorized stage 的必要恢复每次仅一次，保同 runtime Field/H/null basis/真实末 controller 与所有池。不能从精简 summary 的 SHA 猜造原状态；如恢复失败，保原具体错误且不开始新阶段。
5. 新开发入口单独核新观测行、cut/epigraph、预算/失败/缓存及 loop 接口，不重复旧 selected-J suite。人工和真实首跑均仅公开 Actions。

第二项的新增 $de,df$ 在已有因子化 batch 中随 virtual jets 收缩；它不是重新编译或评价另一个 profile/forcing 问题。现有普通 full coarse/fine values 仍调用权威 parent。输出只保存选中 scalar derivative 矩阵，不形成旧完整参数 jets。

由于旧 summary 已按规则不保留可重算 payload，新 actual 的最终状态只能由严格同源临时恢复链形成；这 8 次必要恢复不算新算法改善。新阶段自身是唯一新的优化调用。handoff 必须继承实际末半径/成功 streak，而非把本次历史 $.0000625$ 写成强制输入；历史 canonical hash 只供诊断。

## 8. 仅新功能的公共开发检查计划

拟一次独立开发入口包括：

- $\phi_\pm$ 的 branch/epsilon/epigraph 等价、切平面相切与低估；
- $f=0$、小 $e/f$ 的 $de,df$ 链式导数，避免 branch 反除；
- 非零横向 $(de,df)$ 的正谱余项与可正可负真实几何余项，(14)–(15) 全账；
- cut row 在原 scaled 独立变量与 163 物理 map 下的一致性；
- 单次 inner LP budget 消耗、最多 3 次/原共享 12 次、无剩余 LP 不再求解；用新 stub，不跑旧科学；
- gap 未满足时 $\rho_{\rm aff}$ 上调/原 hard rows 保持、较早 incumbent 与最终 cuts 的相容；
- same-state/cache rollback、soft ID 重复及原 group 映射；新增 J 输出只比对已付 virtual jet 的 $e,f$ 行，不再重旧六 jet suite；
- 当前没有 selected point 的失败报告/IO 必须保留原错误；新模型计数与必要恢复计数分开。

所有通过/失败都以公开 run 的实际返回为准。本地只写源码、读旧源和已发记录；本稿未执行这些检查。

## 9. 输出与停止边界

建议 lane `metric_height159_affine_spectral`，主临时文件 `metric-height159-affine-spectral-audit.json`、summary 同 stem 加 `-summary.json`，开发 `--check-affine-spectral-only`。root 统一接 workflow/publisher/request。

stdout 必须完整打印新模型逐次 inner LP status/count/gap、返回 incumbent 的准确预测、两项误差与遗漏行、真实两网 gate/eta、已接受序列、所有 pool 增量、active/J/LP/value 分账和原源码/input identities。payload 仅 runner 临时，依 README 15 不入 Git、Release 或 artifact。

新 stage 未达到目标时继续研究实际揭示的限制，不把 new solver 成功、内层 gap 小、有限网格下降或浮点硬门通过称为本课题完成。尤其本模型不证明连续 isometry/reach/hold，也没有证明额外径向/角向自由度不再需要。

