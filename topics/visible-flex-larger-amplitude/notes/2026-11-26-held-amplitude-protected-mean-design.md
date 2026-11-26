# 同场 D/L 预算保护下的完整均值度量设计入口

2026-11-26，Astra-larger-e4e2a2bf-20261126 / construction，使用 solver 的原自由坐标幅度行和 geometry 的完整 D/L 证明。

本入口给 R684/R688 的新旋转均值度量设计补上其原来欠缺的实际幅度保护。原题目固定握持、整像20%振幅和 reach 等要求不变；当前计算使用选定见证的充分 D/L 预算来维持朝这些要求前进的设计空间，有限点约束不冒称最终全域证书。源的 AST/compile 和纯 argv 核验已完成，**尚未运行这条新增保护求解**。

完整数学推导见 [固定 D/L 与整像幅度约束](2026-11-26-fixed-DL-whole-image-amplitude-constraints.md)。本文件登记全部实际接口、完整原行保留、同场 nonlinear 复读、永久地点和归因范围。

## 为什么需要新增约束

moving-mean 目标只量当前场 Gram 的角涨落，允许轴向尺度、目标均值和自由 core 高模一起变化。旧 `.992/.025` 曲率必要筛使用的是 $D$ 下界，不能维持 $D$ 上界，更不能继承旧父22.8%的全像振幅。仅固定 core 前三个非零系数，不等于固定整像 held 幅度或含反射 Euclidean 非平凡性。

本分支固定 marked 直径预算 $\bar D$、原 unmarked body 预算 $\bar B\le\bar D-2h$、相位见证距离预算 $\bar L$，其中 $h=1/1000$。要求 $\bar D\le4.5$、$5\bar L\ge\bar D$，并保帽高 $H\ge\max(H_{\min},\bar L+h)$，$H_{\min}>1$。这样若最终连续证明同一原场满足 body 半径和两个见证距离全域界，R661 的固定直径0.9握持与 marked held 差下界可达到20%；标记、嵌入、非平凡性及 reach 仍各按原组合器付清。

根会话已从真实 `mean-metric-design-physical-p4-face-PCG-first/final.npz`（bundle 前缀e3d69d2e）的完整同场 first 读取 body $D_{up}=4.118090829150488$、body $L_{low}=.9387771461187304$、$H=1.8781964685903891$，因此确定本新算法分支的首预算参数为 **Dmarked=4.2、L=.9、Hmin=1.01**。它们是设计预算，不新增验收条件，也不修改题目20%要求。该R688后继自身完整first真实容纳这些预算，故首方向实际选择它继续；未来父若不适配，则付真实restoration或换输入，不能默默放松预算。

上述名义参数对应21/5、9/10、101/100；实际 CLI 和源明确按传入 binary64 的 exact Fraction 解释，并在减 marker 厚度时向下舍入 B、加 marker 厚度时向上舍入高度下界。20%关系用 `5*Fraction(L)>=Fraction(Dmarked)` 核，不把十进制名义分数与浮点载体混为一谈。最终精确 g/几何证书仍回到同场 exact FullHold 定义。

## 1. 每个真点都约束哪三项

当前 $r_0=1+\sum_{j=1}^M c_j$ 使用**全部当前 core 系数**。物理见证 $p=(0,r_0,0)$ 在原旋转 $\phi$ 架中为 $r_0v_\phi$，其中 $v_\phi=(\sin\phi,\cos\phi,0)$。对该架下同一个实际位置 $X$，采用

$$
g_D=4|X|^2/\bar B^2-1\le0,\qquad
g_{L,\sigma}=1-|X-\sigma r_0v_\phi|^2/\bar L^2\le0,\quad \sigma=\pm1.
$$

quarter 的两个见证分支一起覆盖完整反射轨道；不把正 quarter 的单个分支当全圈。轨道 multiplicity 不平均任何几何不等式。

其原位置 cotangent 为

$$
\partial_Xg_D=8X/\bar B^2,\qquad
\partial_Xg_{L,\sigma}=-2(X-\sigma r_0v_\phi)/\bar L^2.
$$

原完整 point pullback 已支付 $X$ 的所有自由 core/node/H 分支；在这个原自由 covector 上，给每一个自由 core 前缀槽另加

$$
\frac{2\sigma (X-\sigma r_0v_\phi)\cdot v_\phi}{\bar L^2},
$$

然后才过原 $T^*$。不能只更新前三个固定系数，不能把这个支路加在 coarse 坐标尾部，也不能冻结 $p$。源绑定 original free prefix `[:M-K]` 及完整 R671 point adapter，防止漏掉解析 k 偏置。

帽的两个 scalar 行始终加入：

$$
g_{cap}=4(R^2+H^2)/\bar B^2-1\le0,\qquad
g_H=(\max(H_{\min},\bar L+h)-H)/\bar L\le0.
$$

$R$ 必须与当前同一 FullHold 的 `problem.R` 逐bit一致；它不是自由变量。H梯度分别为 $8H/\bar B^2$ 和 $-1/\bar L$。既有 $H>1$ 标记配方要求被显式保留，不能只用较小的 $\bar L+h$ 顶替。

每个新行沿用真实非齐次不等式 $Cz\le b$，$C=T^*\nabla g/\|T^*\nabla g\|$、$b=-g/\|T^*\nabla g\|$。导数恰零时保留原零行及其实际 margin，不删除或伪称全局不可行。新行的 `current_product` 仅是兼容旧字段的 $g\le0$ alias；报告按 `constraint_kind` 与旧 reach product 分开，不能拿`.992-g`解释新margin。

## 2. 完整筛与有限 QP 工作集分别做什么

`held_amplitude_screen.Accumulator` 消费当前 R671 六jet循环已经得到的 F，无须额外重构数百万个场点。每个真实观察 stage 的全部 N quarter 角都读三项真值，stage bitset 确保没有缺行；各已知任意地点按 exact binary cell/u/phi 读取两距离分支和body半径。`finish(expected_arbitrary_locations=...)` 独立比较实际任意地址集合与全部曲率/半径永久记忆的 exact union，只有 grid 和这套地址都完整才标 complete。

全点 extrema/真值通过与工作集 heap 上限分开：默认只提出最多2个 body 地点、4个距离地点，距离地点一律加±两行，再加两个帽/H scalar 行，即**至多12行额外工作行**。每组最坏地点总提出，其余地点须处于声明的 amplitude active band（默认.025）。其余未被选进 QP 的所有点仍在真实筛与永久记忆中，没有靠减少工作行放宽接受条件。

原完整几何 QP 工作集（默认上限192行）按原 C、b、metadata 逐块复制为新 mmap 的 prefix，逐条保留。实际原行数、追加幅度行数、新 combined cache bytes、旧 prefix cache bytes 和两份文件总 scratch bytes 都在每方向报告；实际 `ru_maxrss` 照常记录。没有偷删原行给新幅度行腾位置。

每个可能被接受的 nonlinear trial：先读其当前 moving-mean 完整残差/true Phi 与 rho/Gram 域；若有下降可能，再从该**同一个 trial**读全网格曲率及幅度、全部永久任意点、帽/H。只有曲率和幅度全部通过才接受。已被目标或域拒绝的 trial 不执行多余全场几何读，也不声称它幅度可行。

每次实际真读发现的幅度极值及选中地址，精确加入原 curvature/radius 两套永久地点，因此原完整 parent-history 合并器和 R676 重映射都能继续继承，且下次幅度筛总在每个地点检查±两支。Rejected ray 也保留这些地址。若新增记忆后当前父需要重读，重读后**同时**检查曲率和幅度，再启动下一方向；若当前父暴露失败则诚实记录该分支没有可行原点，不删证人、不宣称实现了 Phase I，也不推出真实全局不可能。

末审另付读数完整性：grid k 或 arbitrary principal/radius 非有限时明确 incomplete，防止 NaN 比较静默跳过却标完整通过。没有新增自动梯度 fixture。helper 的 `directional_checks` 是可选诊断，此完整入口不调用。

## 3. 目标和求解器保持哪个身份

新完整 driver 从已刊 R688 真实完整 body `bf25c6d70b6ae4c92e08162b8c75969edcd301ba44d00554f8a55fc806f056bc` 出发，追加上述约束/真筛/报告；原 R684 mean transform、完整 J/J*、当前 R688 coarse Gram、R685 v5/显式 v3 fallback、原变量和 H²母范数均不变。没有接 SOC；若未来接入，须包括新旧全部 C，不能在旧C上校正后称幅度已支付。

默认仍为 p4、epsilon .001、scale .05；本分支 launcher 默认打开已刊 R687 centered Phi−constant 的稳定 scalar 读数，原 Phi仍保存。这个常数消去不改梯度、Hessian、μ单位或实际母问题。首预算2 directions ×64 advances，仅是实际推进预算，不是完成声明。μ显式指定，不能从另一目标机械继承。

新增报告 schema 为 `complete-mean-design-with-held-amplitude-budgets-v1`，**不能交原 R684/R688 reader 冒充旧完整body**。`read_amplitude_design_report.py` 直接绑定本完整新driver SHA和所有新/旧关键源，再核真实各方向的全部接受分支、原/新增行数，输出小摘要。原嵌套 `mean_coarse_driver_derivation` 只说明被继承的 R688 base；新幅度报告和独立源身份说明总driver的新增行为。

这仍是设计阶段，目标均值随候选变化；本源不能当固定最终 g 精化。合格候选后走单独 `frozen_mean_metric.py` 管线冻结相同数学目标；固定目标的后续求解若改变场，也必须重新维护这些幅度要求及同场连续证书，不能继承当前有限筛的通过。

## 4. 首命令与回读

下例选择已真实返回完整first且适配预算的R688 e3d69d2e父，parent/report/evidence三路径一致。实际证据见[首面PCG与同场first](2026-11-26-actual-first-mean-face-PCG-and-amplitude.md)；source/driver SHA和parent完整SHA由launcher/driver记录。

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/launch_mean_metric_amplitude_actions.py" \
  --repo "$FLEX_REPO" --work "$FLEX_WORK" \
  --bundle "$FLEX_WORK/mean-metric-design-physical-p4-face-PCG-first/final.npz" \
  --parent-report "$FLEX_WORK/mean-metric-design-physical-p4-face-PCG-first/report.json" \
  --carrier "$FLEX_WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$FLEX_WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$FLEX_WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --manifest "$FLEX_WORK/geometry_path/curvature-qp-spectral-hessian-r22-union-next-four-witnesses-compact.json" \
  --eta-start-node 885 --lambda-value 1 --averaging physical \
  --marked-diameter-budget 4.2 --witness-lower-budget .9 --amplitude-height-floor 1.01 \
  --amplitude-budget-evidence "$FLEX_WORK/mean-metric-design-physical-p4-face-PCG-first-geometry/first.json" \
  --damping .01 --directions 2 --maxiter 64 \
  --active-rows 192 --qp-atol 0 --qp-rtol 1e-6 \
  --reach-safety-factor .992 --active-band .025 \
  --spectral-p 4 --spectral-epsilon .001 --spectral-scale .05 --target 5e-7 \
  --outdir "$FLEX_WORK/mean-metric-design-amplitude-protected-first"
```

`--amplitude-budget-evidence` 是真实预算选择来源的路径/SHA审计，不自动继承该文件的任何连续结论。数值原点和每个 trial 都按当前真实场重新读。后续若parent已带幅度预算，launcher禁止默改三预算参数；需要改变算法问题时必须另作明确新分支。

```bash
python "$FLEX_REPO/topics/visible-flex-larger-amplitude/scripts/resume_20261126/read_amplitude_design_report.py" \
  --repo "$FLEX_REPO" \
  --report "$FLEX_WORK/mean-metric-design-amplitude-protected-first/report.json" \
  --out "$FLEX_WORK/postprocess/held-amplitude-protected-first-summary.json"
```

之后仍对同一个 `final.npz` 用原 f122 `exact_reference_tail_interval.py --mode first --cells all` 付完整 D/L/嵌入读数，并继续曲率/far/marker等原连续组合器。不能由必要曲率筛宣布 reach；`sampled_minimum_witness_distance_squared` 也不是全域距离下界。附带的三步队列JSON保留这个同场 first回读，所有raw只在runner。

## 5. 完整源身份和回读字段

| 源 | Bytes | SHA256 |
|---|---:|---|
| held_amplitude_inequalities.py（solver） | 28793 | d06920f34b566cf6ccc4ebd0dace1a08463bee8b3f95f8b1933cdf22c15fa154 |
| held_amplitude_screen.py | 10310 | d9cd7ef55a92526a7cf7d9ed4a90a964fb0915713562f550cfcbe3970125d64f |
| fullclosed_mean_metric_amplitude_qp.py | 68753 | ae6fbf5e1b1ff1b4ceb9bb1fd97d4ea6933e115946a2bc37b1b0578b9bba1db0 |
| launch_mean_metric_amplitude_actions.py | 12618 | dfc3e593f893f0bb7dc46db71338b7518b7960ca3ee2969e5cf23a81988eb27e |
| read_amplitude_design_report.py | 10195 | 4cf90def9421393a1d318c09e285e32ca918091fc942ed6e5f093eae486c7669 |

全部新源逐行无尾空白、AST/compile通过。纯 `--print-command` 得151个argv项、74个flags，逐一与完整新driver argparse匹配；没有科学raw读取或数值fixture。solver核完整prefix/typed linear值/真trial分支和永久点，geometry核quarter±p/全grid/expected任意点集合及D/L充分预算；这仍是静态审查，不称数值验证。

实际运行至少读取：final bundle SHA、原/末 max与相同p/epsilon/scale/测度 Phi、中心化实际gain、accepted alpha/真实QP状态、实际old/new行数与cache/峰值内存、幅度每项最大g、cap/H值、expected/read永久地址一致、最终必要曲率筛和真实新first全域D/L。每一新实际场单独承担其后续全域结论。
