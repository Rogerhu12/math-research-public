# 实际 121 第五批到九控制量候选：Request 123 完整接口

作者：OpenAI ChatGPT / amplitude，geometry 负责独立分段读回器。日期：2026-11-15。分类：新标量族及一次有界科学实验的源码接口；没有实际 123 数值结果。

## 1. 本次确切起点和要回答的问题

实际 [121 运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43694950669) 的源码提交为 `da16069e10e11d4541992fa66c6f03ee7165baf7`。第五个科学子进程完成了八个方向且八次接受，原最终标志仍为假。原未加权三方程 merit 为 `738.1754024784359`，首项 unit 残差为 `-38.42330959663998`，完整 $3\times6$ 浮点响应的最小奇异值为 `0.0068574945219558045`。这些是保存的原报告读数，不能推成秩证书、无根结论或已接受非零场。

该次编排停止于工程读回：原正常视图即使省略后仍为 93000 字节，超过 90000 字节界限，留下 16702 字节的 metadata-over-budget 摘要，随后编排返回 70。不是数学门拒绝。公开保留的第五批摘要没有完整外 trial 行；新实验不声称恢复这些未进入原日志的内容。

本次使用其真实末六参数，再追加三个零系数：

```json
[0.4091209275836485,0.2513669199841148,0.4996145196964636,-0.006902208058565607,-0.035813559588767495,0.5645740576397902,0.0,0.0,0.0]
```

前六参数顺序原样保留；新参数是同三个支撑上的原始二次形状系数。只做一个新的八方向候选批次。初始相对半径明确重设为 `0.1`，不把上一批保存的末半径 `0.000390625` 冒作续接值。每个模型、参数响应、域检查与最终诊断重新计算。

| 起点身份 | 字节 | SHA256 |
|---|---:|---|
| 121 第五批保留 fallback 摘要 | 16702 | `24c3b370b23840ddaf93c52caa36a4b434ff3018e31a65ccb0f4d574a6d5b30e` |
| 原科学 status，本文仅保其报告身份 | 4646850 | `cfe09440cd7d89bb9a1b79513ff17695c16f683cc745dd73fb4412c87742241d` |
| 超限正常视图，未声称完整恢复 | 93000 | `d170c8b33010b6579837fbd7a6d8106f1fefba6d7dffc4711fe349cea5b6a478` |
| 本次九参数短 recipe | 2239 | `cc4e90955ad20f740f4107166c0e94039445c18e12462caafdfa48316299501e` |

实际父 producer 是冻结的 `geometry_20261115_small_core_six_control_curved_recipe.py`，SHA256 `e154afe28c588ce0c2ae936d4304b67ec84e2b46c96b03e48ce4113e2401a761`。其 schema 是 `R259-six-control-full-three-two-normal-curved-trust-recipe-v1`。起点 schema、source、run、status 与 fallback 身份均按真实来源保存，不重标为新九参数 producer。

短 recipe 只承载字面参数与来源。科学入口不读父 status、父完整摘要或父数组；来源 SHA 不等于本次重新核过父 raw。来源闭包由原定义明确给出，并已与可用 fallback 中的 24 件原来源对照。当前 producer 新增 family/search 两件，闭包为 26 件。

## 2. 九控制量的精确数学变动

令原第 $i$ 个支撑保存的左端点和宽度为 $\ell_i,w_i>0$，$x_i=(s-\ell_i)/w_i$，$t_i=2x_i-1$，$P(x)=64x^3(1-x)^3$。原偶形状为 $b_i=w_i^2P(x_i)$。在每个开支撑 $0<x_i<1$ 上，本次设计为

$$
a(s;p,\theta,\eta)=a_0(s)+\sum_{i=1}^{3}p_i b_i(s)
 +\sum_{i=1}^{3}\theta_i b_i(s)t_i
 +\sum_{i=1}^{3}\eta_i b_i(s)t_i^2.
$$

支撑之外及端点，三个形状的 0、1、2 阶 jet 均按原零延拓处理。新增原始二次形状的 jet 为

$$
\begin{aligned}
B_i &= w_i^2 P t_i^2,\\
B_i' &= w_i(P't_i^2+4Pt_i),\\
B_i'' &= P''t_i^2+8P't_i+8P.
\end{aligned}
$$

$P$ 在两个端点有三重零点，所以二次因子不会破坏 $C^2$ 零 jet。这里采用各自保存的 `left` 与 `stored_width`；不把独立存储的 binary64 `right` 无说明等同于实数式 `left+width`。原三个支撑、标量基函数和所有旧控制量不移动。

九参数顺序固定为

```text
[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]
```

旧六列是 `[0,1,2,3,4,5]`，旧四列仍是 `[0,1,2,4]`。新增列仅 `[6,7,8]`。这里没有用居中多项式替换 $t_i^2$，也没有伴随隐藏的 $p_i$ 重参数化；这种替换会改变当前参数尺度及信赖域的算法意义。

在每个原支撑内部，函数 $b_i, b_it_i,b_it_i^2$ 的线性独立可归结为多项式 $1,t,t^2$ 的独立；不同支撑之间也可分别看待。这个函数层面的事实不推出端点响应增加秩、不推出存在低三共振根，也不保证任何接受步或条件数改善。当前旧 $3\times6$ 已可有三行秩，新增自由度的实际用途必须由新 $3\times9$ 响应与非线性试探显示。

## 3. 零新增系数与浮点作用范围

当 $\eta_1=\eta_2=\eta_3=0$ 时，声明的实数式严格退化为旧六控制族。实现保留旧三个偶控制的加法路径、旧 odd 加法顺序 `theta2,theta1,theta3`，再按 `eta1,eta2,eta3` 顺序追加非零二次项；零二次系数不执行附加浮点加法。

域检查施加于完整九控制量之和。实现没有先调用旧六控制 profile 的早期域 guard 再追加新项，因为一般非零二次项可能改变完整标量的合法性；提前只判旧六部分会改变新族定义。

`zero_added_quadratic_reduction` 在实际 Actions 中比较新零扩展与真实旧六源码各自 `evaluate` 返回的 circle、方程等保存数组（排除不同维数的 parameters），不调用旧六 `jacobian`，所以不构成独立旧六参数响应比对。新初始 description 的完整 $3\times9$ 响应及其旧六列奇异值另按实际新计算读回。上述数组比较结果只记录。源码或接口没有把逐字相等提升为开始候选、参数接受或最终科学通过的新增条件；也不提前宣称实际数组已相同。

## 4. 完整响应、方向和曲线路径

原三项 unit 方程与未加权 merit $W=\frac12 r^T r$ 保留，完整 112 个尾斜率行及原 full112 小残差标志保留。新族仅扩展设计参数维数，完整原 circle 传播与末端残差形成没有删除高 109 行或把尾响应对角化后伪称一般结果。

每个当前点计算新的完整 $3\times9$ 参数响应 $J$。原参数尺度仍为 $S_j=\max(1,|p_j|)$，方向写为 $v=Sz$，采用原正阻尼问题

$$
\min_z \|JSz+r\|_2^2+\mu^2\|z\|_2^2,
\qquad \|z\|_2\leq\Delta.
$$

实际使用完整 $12\times9$ 增广矩阵的带列置换 QR 和完整三角解。正阻尼 floor、最多 64 次上界扩张及 64 次几何区间细化沿原算法；不使用 normal equations、`lstsq` 的截秩、SVD cutoff 或只保几个参数列。

对完整当前约束两行的行平衡 $2\times9$ 矩阵转置做完整 QR，形成 $9\times2$ normal 平面 $N$ 和 $9\times7$ tangent 基。实际候选路径仍为

$$
q(\alpha)=p+\alpha v+SNw,
\qquad c(q)\approx c(p)+\alpha(Jv)_{2:3}.
$$

内层仅求这个原两分量目标的近似修正，预算仍为 12 次 normal Newton、每次 20 档内回溯。每次使用当前九控制完整响应再投影到完整 $2\times2$ normal 系统；没有重新引入 $J_{33}$ 除法或单个参数恢复。

外层原 20 档为 $\alpha=2^{-j}$，$j=0,\ldots,19$，八个方向总预算同时计入接受和完全拒绝的方向。每个实际返回候选必须通过原有限域、真实 $r^TJv<0$ 和完整三残差的原 `.2` Armijo；内层目标或目标误差从不覆盖实际残差。`1e-8` normal tolerance 只决定内层停时，不成为新的外层接受条件。所有试探和失败仍保存，完全拒绝不采用试探参数，原半径更新规则不变。

原代数界限继续记录为最多 160 次外 trial、38560 次直接 seed 加 normal 回溯评价和 1920 次 normal fresh-J 调用；这些不是实际调用数，也不包含每个完整 J 内的 complex-step 评价或原最终检查。超时必须表述为资源中断，不写成已试完预算或无根结论。

## 5. 原最终检查的责任

初末实际参数均执行原三档实 FD：`2e-5,1e-5,5e-6`，每档尝试全部九列。某一列域异常不得悄悄跳过余下列；报告保每列状态，任意无效时相应完整最大误差保持未定义，不从有效子集冒完整通过。原 full-three 方程、全部 112 原右残差及 unit 停止阈值保持。

标量区间检查在新九参数族上重新形成，仍使用 160 bit、深度 14。原返回 `a'` 与原有限求积系数的声明实模型范围保留；它不自动等于精确连续导数恒等式或完整非零场证书。

原完整 circle 检查仍为 453 维方形物理问题：固定本次全部六个附加系数 `theta1..3,eta1..3`，只留下原三个 $p$ 为 active controls。所有物理态、入口、末端、M112/T112、2048 角及 4096 物理/材料角检查、节点/中点/两 RMS/边界原判据保持。新增记录键为 `frozen_six_added_shapes_square_check`。固定形状后与九参数标量的数学函数相同，接口不提前声称不同组合顺序的 binary64 值逐字相同。

该候选实验不调用 native 非线性尾求解器，不产生 accepted nonzero-$\lambda$ 场，也不把原零尾线性数据改名为当前非零 H 响应。现有六控制 full112 适配器不能直接冒作九控制适配器；将来非零全场必须显式冻结本次六个附加形状并付真实 H/native/fullJ/FD/finalaudit 责任。本请求不预先承担或宣称完成这些任务。

## 6. 冻结源码及短输入

| 文件 | 字节 | SHA256 |
|---|---:|---|
| `geometry_20261115_small_core_nine_control_family.py` | 44390 | `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629` |
| `geometry_20261115_small_core_nine_control_curved_recipe.py` | 54884 | `824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf` |
| `root_20261115_small_core_nine_control_curved_scalar_readout.py` | 30892 | `f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d` |
| `actual121-batch5-explicit-nine-control-parameter-recipe.json` | 2239 | `cc4e90955ad20f740f4107166c0e94039445c18e12462caafdfa48316299501e` |
| `public-small-core-nine-control-request.json` | 37691 | `0a1df1539a46e6f557b37eca9ccc71c6922fa38c6b52cc8d4bfdbfa2b7e259d3` |
| `visible-larger-public-small-core-nine-control.yml` | 17973 | `5343c5104051b6191a7b1bfa6c82d35d4958257ab5037d94898bb8c102855c06` |

科学 status 为 `nine-control-curved-status.json`，schema 为 `R259-nine-control-full-three-two-normal-curved-trust-recipe-v1`。recipe schema 为 `R259-explicit-nine-control-raw-quadratic-shape-recipe-v1`。entry 支持明确的原六来源零扩展，也支持未来本 exact 九 producer/schema 的真实九字面参数来源；这个能力不预填未来运行身份。

四数学输入原 SHA 不变：

| 输入 | 字节 | SHA256 |
|---|---:|---|
| 原 accepted input | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| 原 M112 prepared | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 原 T112 零尾 anchor | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原 T112 config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

工作流只从历史提交 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复这四件到本请求 `RUNNER_TEMP` 目录，逐字节数/SHA 验后传原路径参数槽。不会重新把它们写入当前 main，也不依赖 104 清理后的 HEAD 仍有原数据路径。原 78 件公开数值源码按原恢复器临时恢复；题目 computations 中的完整旧源闭包仍在当前源码 checkout。

## 7. 唯一 Actions 接线

唯一 push trigger 是：

```text
topics/visible-flex-larger-amplitude/computations/public-small-core-nine-control-request.json
```

工作流目标为 `.github/workflows/visible-larger-public-small-core-nine-control.yml`。没有 workflow_dispatch、分支修改、第二科学请求或实际 123 run 预填。源码入口及 reader 放题目 computations；本接口及 reader 接口放 notes。原 81 个 request source pin 全保，加入两科学源后为 83；workflow 支持 pin 为原规则 runner 加新 reader 两件。原父科学闭包 24、当前 26，不混用 request 总数与实际 producer 消费定义。

环境保持 Python 3.12.14、NumPy 2.3.5、SciPy 1.17.0、python-flint 0.9.0，三个 BLAS/OMP 环境均为 1。原一批 science step 75 分钟、compute job 90 分钟；report job 10 分钟。模型的方向/试探预算与所有阈值不因 wallclock 增减。

原 `root_20261114_current576_rules_runner.py` SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` 不改。只显式装入实际已读两 README 的完整字节 baseline：根 `74c08a36f6c997d0bc1e64a7956b42276f5fa5d7`、题目 `bff8aea253a9e6a7a4fac28d810ac454c5499fec`；原每 2700 秒真实 pull/rebase/diff/变规停运语义与 H 唯一规则行责任均保留。固定 science checkout 不由规则监控同步改写。`merge.stat=false` 只是避免 pull 展示已删大 raw 的 Git 输出成本，不是科学门。

CLI 等价于：

```bash
python -u computations/geometry_20261115_small_core_nine_control_curved_recipe.py \
  --accepted "$ACTUAL_ACCEPTED_INPUT" \
  --prepared "$ACTUAL_PREPARED_INPUT" \
  --tail-anchor "$ACTUAL_ZERO_ANCHOR" \
  --tail-config "$ACTUAL_CONFIG" \
  --parameter-recipe computations/actual121-batch5-explicit-nine-control-parameter-recipe.json \
  --parameter-recipe-sha256 cc4e90955ad20f740f4107166c0e94039445c18e12462caafdfa48316299501e \
  --initial-relative-radius 0.1 --candidate-steps 8 --backtracks 20 \
  --normal-iterations 12 --normal-backtracks 20 --normal-target-tolerance 1e-8 \
  --candidate-resonance-tolerance 1e-8 --interval-bits 160 --interval-depth 14 \
  --out "$RUNNER_TEMP/visible-small-core-nine-control-curved/small-core-nine-control-curved"
```

工作流以原 runner 包裹这条 argv。该 CLI 只描述将由公共 Actions 执行的实际调用；本地没有运行。

## 8. 解决 121 超限的分段读回

新 reader 的完整协议见 [九控制量分段读回接口](2026-11-15-nine-control-segmented-scalar-readout-interface.md)。它只读原件，不导入科学模块。正常 primary schema 为 `original-nine-control-full3-curved-trust-segmented-scalar-readback-no-raw-retention-v1`，仍通过 `scalar_summary`、`scalar_summary_bytes`、`scalar_summary_sha256` 三个 job output 传递不超过 90000 字节的主 JSON。

每个完整方向独立打印 `BEGIN_VISIBLE_NINE_CONTROL_<GROUP>_PART_<NNNNN>` / END 段，保原 17 列所有 trial 行、实际九参数/三残差、当前完整方向模型和 curve frame。每段有独立字节数/SHA、组及路径/索引范围；组有原 canonical SHA，描述器列表也有 canonical SHA。单方向或其他具名字段过大时完整结构分段，不靠截 trial 或把实际错误文本截断腾空间。

工作流 reader stdout 原样进入 compute job 日志，不重定向到随后会删的临时文件；report job 只打印 primary，不重新合并八组大 payload。primary 保初末 FD、scalar/circle、来源与最终标志；若某具名字段也过大，它被完整移动到显式索引组。全部 inner normal trial 大对象仍按原读回范围由原 status SHA、计数和 failure examples 负责；不能把标量协议称作完整 status raw 归档。

科学步骤之后 reader 用 `always()` 读取真实已有结果或异常；传输失败与数学失败分开。只有读回步骤之后才删除本请求临时科学树、四输入和 78-source 恢复树。仅对本请求、当前属主的目录补必要写位，拒绝根路径 symlink；不操作别的批次或共享仓库数据。cleanup 成功不冒充 reader 或科学成功。

没有 raw artifact、Release、node_modules 或科学 data 提交。规则同步临时仓库/小元数据只留在临时 runner，平台结束后销毁。实际来源、参数、运行号、原标量与输入输出 SHA 由日志和后续正式结论保留。

## 9. 静态范围与尚未发生的事项

新两科学源与 reader 已 AST parse；新 recipe 的前六 IEEE 字面值与实际 fallback 参数逐字对应，新增三项为零。source-only 比较显示八个核心数学函数在明确维数/字段替换以外保留原结构；特别是完整 circle matrix 和传播后半段不改。request/workflow 通过 8 个 Bash 语法与 5 个 inline Python AST 检查，来源 schema/closure、输入 SHA、输出名称、分段 stdout 责任及预算一致。

临时检查记录只描述源码/字节，未执行模型导入、QR/SVD、FD、Arb、circle、任何 fixture 或 Actions 科学调用，不成为新科学门。当前没有 123 接受结果、rank 证书、低三根或 native 完成记录。实际运行后应先读所有新 trial、完整原最终标志与真实新响应，再决定是否继续；不能用本接口保证进展。

完整两数学源 diff、request/workflow 相对原 117 的完整 diff 和仅本地静态回执在独立交付目录。公开复算所需是本节冻结源码、短参数配方、请求和工作流；不需要发布可重算静态回执或原科学 raw。
