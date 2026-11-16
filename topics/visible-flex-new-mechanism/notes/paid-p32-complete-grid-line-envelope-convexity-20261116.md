# 已付 p32 的完整两网标量线包络：凸性、下降判据与输入边界

2026-11-16。性质：下列有限维凸性和右导数命题为纸面证明；没有执行新的 JVP、包络采样、标量优化或物理 trial。是否存在本次 p32 的实际下降子段仍未知。

## 1. 新问题的准确来源

[最后 cone32 的实际笔记](final-cone32-first-actual-and-complete-grid-separation-20261116.md) 对应公开 run [43800505444](https://github.com/Rogerhu12/math-research-public/actions/runs/43800505444)、source `8dfe5272b6d4f4fb752c8962689b22a95c61f78a`。完整 p32 已保存。原有限锥候选返回 AlmostSolved，线性/盒/included-cone 原门通过，但全步在 fine 87417 得完整 affine 最大值 0.26602970125710546；基点最大值为 0.2660182947853382185。rho 修复后原模型 gain 为负，没有物理 trial。

这里只问一个新的标量问题：固定这个实际已付方向 $p=p_{32}$，是否有 $0<\alpha<1$ 使同一个原完整两网 affine metric 包络下降？它不是重新求解 cone32，不修改其状态，也不恢复旧 MaxTime31 缺失的 rho/norm。HiGHS64 和 cone32 调用账都已封存。

下文完全沿用原源码：

- [frame_metric_affine_spectral_model.py](../scripts/frame_metric_affine_spectral_model.py)，`phi`、`phi_gradient`；
- [frame_complete_affine_metric_oracle.py](../scripts/frame_complete_affine_metric_oracle.py)，`CompleteDirectionalMetricOracle`、`direction_frame_jets`；
- [frame_selected_row_radial_jacobian.py](../scripts/frame_selected_row_radial_jacobian.py)，`_families`、`_ordinary_slice_and_replay`；
- [frame_five_height_field.py](../scripts/frame_five_height_field.py) 与 [frame_direct_reference_geometry159.py](../scripts/frame_direct_reference_geometry159.py) 的原 metric、height、null-height 和 $X_s$ 组装。

这些文件按该 source 读取；本笔记没有改变任何旧文件。

## 2. 原两个谱分支沿线的凸性

固定一条原网格点，记其基点数据为 $e,f$，已指定参数方向的真实一阶收缩为 $d,h$。固定原 $\epsilon=10^{-8}>0$。group 0 取 $\sigma=1$，group 1 取 $\sigma=-1$。原分支恰为

$$
\phi_\sigma(\alpha)
=\frac{\sigma(e+\alpha d)
+\sqrt{(e+\alpha d)^2+4(f+\alpha h)^2+\epsilon^2}}2.
\tag{1}
$$

因此 trace 项只是仿射项；第三个 norm 坐标是原固定 $\epsilon$，没有引入新 trace 参数或改谱模型。

令

$$
q(\alpha)=(e+\alpha d,\ 2f+2\alpha h,\ \epsilon),
\qquad v=(d,2h,0),\qquad r(\alpha)=\|q(\alpha)\|_2.
$$

由于 $r\ge\epsilon>0$，每个分支在整条实线上光滑，且

$$
\phi_\sigma'(\alpha)
=\frac12\left(\sigma d+\frac{q(\alpha)\cdot v}{r(\alpha)}\right),
\tag{2}
$$

$$
\phi_\sigma''(\alpha)
=\frac{r(\alpha)^2\|v\|_2^2
-(q(\alpha)\cdot v)^2}{2r(\alpha)^3}\ge0.
\tag{3}
$$

不等式由 Cauchy–Schwarz 给出。若 $(d,h)\ne(0,0)$，分子至少为 $\epsilon^2(d^2+4h^2)>0$；若方向收缩全零，该分支为常数。因此每个分支凸。

这里的证明把固定输入数视为实常数，说明原模型函数的解析性质。后续 binary64 的 `hypot`、求最大值、舍入后的参数 apply 仍是数值执行，不能由本证明替代其误差记录或实际门。

## 3. 完整包络和正 slack 都凸

设 $\mathcal I$ 是原粗、细网格的所有点和两个分支。当前粗网 160×384、细网 160×768，因此共有 184320 个点、368640 个分支。定义

$$
\Phi(\alpha)=\max_{i\in\mathcal I}\phi_i(\alpha),
\qquad
\rho(\alpha)=\max\{0,\Phi(\alpha)-13/50\}.
\tag{4}
$$

有限个凸函数的最大值凸，故 $\Phi$ 和 $\rho$ 均连续、凸且有左右导数。原完整模型的 outside constant 本次为0；若以后有非零固定 outside slack，可把它作为常数分支加入，凸性同样成立。

$\Phi(1)>\Phi(0)$ 并不推出 $(0,1)$ 全部不可用。它只排除全步在该模型量上的改善。端点之间可能先降后升；是否发生必须由全部原网格行决定。

本方法所讨论的是原完整 affine metric 包络，不是把旧 solver 的 norm auxiliary 任意改成 $\alpha$ 的代价，也不是给旧 conic objective 新最优性标签。若另行引入 norm 惩罚，必须单独定义其系数和归一化；本文不这样做。

## 4. 全部真实 active 行给出必要充分的方向判据

对任意 $a$，定义精确 active 集

$$
I(a)=\{i\in\mathcal I:\phi_i(a)=\Phi(a)\}.
$$

有限最大值的左右导数为

$$
\Phi'_+(a)=\max_{i\in I(a)}\phi_i'(a),
\qquad
\Phi'_-(a)=\min_{i\in I(a)}\phi_i'(a).
\tag{5}
$$

证明：非active行与当前最大值有严格正 gap；集合有限，故在充分小邻域内不可能越过所有active行造成一阶贡献。对active行分别使用光滑一阶展开，取右侧最大和左侧最大，即得到式(5)。这同时处理镜像、周期对称或不同网格造成的多个active行，不能只选 tie-breaking 返回的一个 ID。

**命题。** 以下两件事等价：

1. 存在 $0<\alpha\le1$ 使 $\Phi(\alpha)<\Phi(0)$；
2. 全部精确 active 行满足
   $$
   \max_{i\in I(0)}\phi_i'(0)<0.
   \tag{6}
   $$

若第1件成立，凸函数的端点割线给
$\Phi'_+(0)\le[\Phi(\alpha)-\Phi(0)]/\alpha<0$。
反之，右导数严格负，按定义充分小正 $\alpha$ 即严格下降。若 $\Phi'_+(0)\ge0$，凸性给
$\Phi(\alpha)\ge\Phi(0)+\alpha\Phi'_+(0)\ge\Phi(0)$，
所以整条正向线都无严格下降。这是本条**固定线模型**上的结论，不是其他方向或非线性实际 metric 的结论。

同理，内点 $a\in(0,1)$ 最小化 $\Phi$ 当且仅当

$$
\Phi'_-(a)\le0\le\Phi'_+(a).
\tag{7}
$$

端点0最优当且仅当右导数非负；端点1最优当且仅当左导数非正。只要式(6)严格成立，而当前已付的 $\Phi(1)>\Phi(0)$ 仍成立，就有内部最小点。

式(6)不是从四个全步 attainer 直接可得的判断。它需要 $\alpha=0$ 的全部真实active行及其方向收缩。实际浮点值相等的集合不自动等于精确解析active集；无区间误差证明时，应把相关导数结论报告为浮点观测，不能据容差选出的active集合宣布严格“整线无下降”。

## 5. 此标量结论不授原 proposal 或真实几何资格

已付 p32 在全步原线性/盒门内，不足以让任意缩放自动继承所有 proposal target。特别是原曲率 guard target 可能严格高于基点当前余量；零步不必属于该加强的提案可行域。因此不能未经核查就用凸域论证说 $\alpha p32$ 对原所有 guarded RHS 可行。

对原精确物理盒，基点与全步在同一仿射物理映射内时，理想实数线段有凸性；但具体参数 apply 的 binary64 舍入、exact159→163 重构和最终门仍必须按原函数实际检查。

另一方面，新方法可以明确只将 $\Phi$ 的下降作为**真实验收前的方向选择**。它不伪造缺失的当前selected159 J，不声称重走旧 `_candidate` 或原conic gate；任何选出的未试点仍须原完整几何、精确物理盒、两网14门与原严格 $\eta$ 下降规则。曲率、嵌入性/strip/ball/height、遗漏行学习都不能用该一阶包络替代。

原 $\epsilon$ 正则化与实际两网 $\eta$ 也必须分别标记。模型下降只用于提案；实际接受依旧读取原真实 $\eta$，没有把模型差额当实际收益。

## 6. 原日志能复用什么，缺少什么

本次原输出确实保存了 p32、161辅助值、原尺度和基点物理向量，以及当前g/b0/坐标/两网/学习/池/支持的完整恢复定义。四个全步 attainer 各保存原 $e,f,d,h$。这些资料可以精确指定新线和校对相应原点的读出。

但原 oracle 在每个 radial batch 只保两个最大行；它丢弃其余点的 $d,h$。最终cache中只存四最大值、四attainer和direction SHA。普通基点的 e/f 全阵列也没有进入该已付日志；原日志的数组SHA不是数组内容。

因此，四个已知分支只能给 $\Phi$ 的**下界**，不能给整包络上界，不能由它们证明任意 $\alpha$ 的完整下降。源代码和物理参数可以重新生成所缺数组，但那是必须如实收费的新科学计算，不能写成“只解析旧日志已得到全线”。

真正完整的有限线缓存是每个原点的四个标量
$(e_i,f_i,d_i,h_i)$，配原行顺序和两个原grid定义。一次生成后，任意 $\alpha$ 的式(1)–(4)不再需要几何、JVP或selected159 J。完整缓存应先进入本次原 stdout 和临时runner文件，再在同一进程多次消费；不得提交Git、Release、artifact或跨run数组cache。若以后从已付原stdout消费，它的身份、原数组指纹、源点及方向也必须完整核对。

## 7. 新方法的计费与授权边界

本次已按main只读核根README blob
`21bd547f56590b7f2dd279d0297efb289a9b2783`
和题README blob
`d0432faff569c8e9af7ed4809847e12880976c11`。
根授权段和规矩6要求继续推进子问题，规矩13指定公共Actions；约6小时是设施能力说明，不是把某个已耗尽模型自动续费的合同。题README没有规定1200/1800或32/64这些方法级数字。

原1200/1800科学钟、32cone和64HiGHS是既有请求合同，必须保持原终账。本方法若执行，须有独立的标量方法身份，显式记录：

- 一次线系数建造、两个原grid覆盖；
- 新标量优化会话数，以及每次完整包络/导数查询数；
- 必要读取、准备、first-jet、缓存序列化、标量求解及任何真实trial费用；
- 源终钟968.6757049859999/1324.8055252469999、原124值和封存32/64；
- 新方法与旧剩余科学/value上限的关系，不能暗中换名重置。

不形成159维求解不等于“0solver”。标量优化也是新的计算，必须有单独额度和记录。若仅在既有时间交集内工作，当前名义剩余为231.32429501400009秒；它不是冷准备肯定能完成的承诺。具体新请求应在执行前写明有限查询数和真实trial范围，本文没有启动或预授计算。

本纸证只把下一问题降为同一已付方向上的完整有限标量问题。p32是否有足够大的模型下降、是否能通过真实门、是否推进0.26目标，全部留待新方法的公开实际结果。
