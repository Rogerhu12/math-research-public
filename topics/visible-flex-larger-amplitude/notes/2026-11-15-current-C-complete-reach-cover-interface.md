# 当前准确 C 十族闭场的完整 reach 组件接口

2026-11-15，geometry，OpenAI / ChatGPT，AI 作者。**源码与条件接口；未执行。**

## 1. 本次交付与范围

独立入口为 `computations/geometry_20261115_current_C_ten_complete_reach_cover.py`，schema：

```text
R422-current-C-ten450-complete-closed-reach-cover-v1
```

本接口与 [R422 完整条件说明](../results/R422-current-C-closed-pair-universe-and-reach-binding.md) 配套。它保留真实 R400 accepted450 guard、R409 原完整输入和 R416 独立准确 cut 场，接 R417 完整两帽/R413 原 cuff，再复用既有曲率、法向球、全 phase 和局部图责任。

本轮没有 actual450、$K$、$\tau$、覆盖 plan 或 run；未 import、AST、编译或执行科学源码。没有新增 accepted request、fixture、下载原大数据或 Git ref 操作。源码的可执行 API 不表示已经取得实际证书。

运行文件当前身份：

| 文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261115_current_C_ten_complete_reach_cover.py` | 60426 | `3ea1ef9fb56ec10301defa18d832681d6061d8646e78893957ca160279b71834` |

R418 源码/已冻结全域 metric 消费者不变。本组件不读取或要求 R418 成功；实际路径直接由同场完整一 jet 包围。reach 成功也不会替代 R418 的同一原目标责任。

## 2. 真实输入对象

### 2.1 原 R409 目录与 R416 新准确场

`--directory` 指向未来同 job 的真实 R409 输出目录，`--result-sha256` 是其中实际 `result.json` 的 SHA。R416 `load_accurate_cut_field` 保留原 R400/R409 对完整 accepted450、checkpoint、full states/RHS/两阶节点、真实当前 C/native、全部来源和同参数的检查。

`--checkpoint-directory` 和 `--proof-directory` 只作为原 loader 的已有可选参数转交；它们不是新的外部成功标志。输入源必须确实在所给 `--computations` 中，所有直接源先逐 byte/SHA 核对。R416 原转递闭包还会按其自身原入口核真实依赖。

R416 返回：

```text
current.source_bundle = 原 R409 七元组，仅作为来源和原定义数据
current.field         = 独立新准确 cut patch 的完整活动场
current.target        = 原完整十族/模型 C target binding
current.model         = 同一 C/DAG 实系数 cut 构造
current.Active        = 实际已初始化的 675 六 jet 模块
current.binding       = 当前完整绑定
```

新活动块必须使用 `current.field.evaluate`。`source_bundle[5]` 的旧数值 `A` 不能作为新 patch 的 renderer。本源码不会调用旧 ac635/e70d main/loader，也不会把旧 nine/finite schema 改名充当前 C 十族。

### 2.2 原 cuff 与两帽

`--cuff-atlas` 和 `--cuff-atlas-sha256` 绑定真实 R413 原 atlas 输出。入口调用：

```python
atlas, atlas_receipt = Cuff.bound_json(path, expected_sha)
attachment = Cuff.bind_loaded_shared_bundle(current.source_bundle, atlas)
caps = Caps.bind_loaded_shared_bundle(
    current.source_bundle, atlas, attachment, computations)
```

R417 用实际 `type(A).__module__` 的 owner 核源及类对象，保留已修的同路径重复模块类身份处理。没有复制旧 a3 binder。当前帽是

$$F_{\rm side}(x,y)=(x,y,{\rm side}(H+b_{\rm side}(x,y))),$$

完整保当前原顺序 marker 的 `upper/center/radius/height`，准确内部字段为 `index/upper/center/radius/amplitude`。两侧相位固定；负振幅、重叠及全部支持相加。原 C 的 dyadic cuff、高度 datum、同 target 和实际 shared $B$ 首 datum 均交叉核同。

R417 `cell(path, upper, sqrt_bits)` 实际回传的下列字段直接使用，未改其数学：

- `original_ball_record.fixed_position/fixed_position_radius/fixed_normal_centre/fixed_normal_radius`；
- `Cartesian_six_jets.value` 的完整三个 `lower/upper` 有理区间；
- `curvature.both_principal_curvature_absolute_upper`；
- 完整原 graph/六 jet/单位法向/曲率记录仍在临时空间账本保存。

## 3. 原 callee 与完整来源 pins

| 直接源 | SHA-256 | 调用范围 |
|---|---|---|
| `geometry_20261115_current_C_accurate_cut_patch.py` | `28417b93fc4fa7780e049ab7d8c4d98e4f51412afd1ced5fc36558ae1e0d837b` | `load_accurate_cut_field`、准确 field/target/model |
| `geometry_20261115_current_C_original_cuff_target_atlas.py` | `02bb0c70198c54e4ebe8d0fa2ebb6f74d0b17a6193378b0169746926a3b52fd2` | `bound_json`、`bind_loaded_shared_bundle` |
| `geometry_20261115_current_C_ten450_fixed_cap_balls.py` | `0ff1fa60a619a7df8e58e72e240dc42e99850eacd05b6426cc70e9083f76afae` | 当前类 owner 绑定、`cell`、`dyadic_box` |
| `geometry_20261115_shared_active_interval_balls.py` | `675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b` | 实际 R416 所持模块的 `certify_cell`、`bounds`、原 `cell_specs` 索引定义；不运行旧初始化 |
| `geometry_20261115_local_cuff_cross_gram_owner.py` | `0b52a408e08a12c1a16594658510b589ce20d9b2a75430ed5676869e12290456` | `CuffOwner`、完整系数/常数、`test` |
| `geometry_20261115_rational_phase_cover.py` | `f6214d1dc66f9890e99f5d9bbbc93fa0e6524acd6ac879f0058ea023ebc17537` | `GATE_ORDER`、`catalog_for`、`strict_interval` |
| `geometry_20261115_joint_phase_normal_balls.py` | `c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466` | `evaluate_joint`，旧两单端 OR 与 joint 全保 |
| `root_mixed_phase_normal_balls.py` | `ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6` | 原准确有理核、向上根、法向球、Sturm/多项式 |
| `geometry_20261115_shared_curvature_diameter_budget.py` | `b1c2dfb9bd99c0777805da938c38e428da32db8ed5fa6238c9433ed9aede5ad0` | 仅纯 `ImageBounds`；不调用旧 loader/old tau 比较器 |

这些是直接源；R416 与 R417 自己的原完整闭包仍由原入口核。675 虽然在其历史文件里保留旧 source pins，但本组件**不调用**旧 `initialise_runtime`。实际已初始化的 `current.Active.__file__` 及 SHA 另核为本次 pinned 675；`certify_cell` 只在传入的 R416 field 上计算。

原数学定位：

- R241 §1–3：抽象商面、先嵌入后 reach；§5：真实路径包围可作为局部门。
- R37 §2–4、§7：完整非局部双法向责任、位置球、单位法向球。
- R248：共同材料逆作用、活动共同刚转/帽固定，强 $C^2$ 和正确相位约化。
- R279：直接六 jet 的 Gram/非零 cross 与曲率两个严格多项式。
- R280/R281：原四门 OR、两闭 RP1 图、准确 Sturm。
- R282：完整 collar 系数及逐空间×相位叶的同材料局部 membership。
- R24 §3：同一个凸 graph disk 的 Taylor 法向弦式；不是整个弱标记转移证书。

完整相对旧 `geometry_20261115_local_mixed_phase_cover.py`（28554 B / `4e31ad6b...`）的 unified diff 只作临时审读材料。新源是独立组合器，不是原 mixed 源的静默修改；旧源与原 static/R24 路径一字不改。

## 4. 全覆盖索引与真实调用边界

### 4.1 Curvature/path 责任

`Roots` 复用 675 索引顺序：upper 后 lower，原 piece 顺序，每片完整 radial×q 闭格；另有 upper/lower 两个完整 cap root。初始深度 $h$ 给 $2P4^h$ 个 active root，帽只有两个完整 disk root。

`CurvatureCover.run` 对每个 root 做闭 DFS：

- 活动块调用原 `certify_cell(current.field, piece, radial, angular, lower, sqrt_upper, bits, K)`。
- 原六 jet 内含 `value/u/q/uu/uq/qq`；`u` 是该片自己的实际 s 或 r。
- 保完整 `squared_cross_lower`、单位法向归一化及原 `R279` 字段。
- 活动未付块按 radial/q 交替二分；帽按原四叉路径分四块。
- 所有实际边界都在两个或多个闭 child 中，不删共同端点。
- cap 仅严格盘外域视为空，不把方形与 disk 内部互换。
- 原 K 由输入固定；活动用原 R279 严格门，帽用原 Hessian 上界的非严格 `<=K`。

同一 terminal cover 的全部一 jet 产生各原 piece 的 $U_i,V_i$ 上界。累计径向长度上界坐标先沿 prefix s 递增，再按原 r 递减穿过全部 native/patch/collar；下反射片取负。只有完整覆盖才产生可用的全路径包围。

这条路径在 cut 两侧分别按各自变量计长，并在实际同 q 公共端点粘合；没有强行等同两侧速度或使用旧数值 $v,b$ 代替 R416 准确过渡。全 q 的最短角差取 period-one 真圆距离，不把物理 q 当材料 Theta 的等量相位平移。

### 4.2 Pair 责任

`Roots.pairs` 的固定 rank 顺序为：

1. 全部 active–active 的 `i<=j`，包括同 root、两 sheet、每个不同 piece/seam。
2. 两帽的上/上、上/下、下/下。
3. 每个活动 root 与两帽的完整 Cartesian product。

共 $N_A(N_A+1)/2+3+2N_A$。不输入或读取旧 `worst`、邻点列表或 selected failures；`max_pairs` 只决定本次保留的实际未访 rank 后缀，不改变原 universe。

AA/CC 的静态门使用真实同场球。AA 两端同时旋转，所以整个静态证书对全相位有效；CC 两端固定。没有把旧某个 static pair 的一端拿来旋转。AC 每个 root 同时持有 `t`、`u` 两个 `[-1,1]` 闭根，其完整子叶使用原 R281/Sturm 或原 R282 真 membership。

Pair DFS 对 AA 交替分左右两端的 r/q；CC 交替分左右帽四叉；AC 分活动 r/q、帽四叉、phase 闭区间。每次 split 完整列出所有闭 children。phase-only 细分可以复用同一真实空间球；空间细分重新调用同一源的完整六 jet/帽 API。缓存只省重复求值，不改变来源、域或证明。

## 5. 判据、符号与不使用的结论

### 5.1 原门保持

静态距离、左右单端、joint 为 OR；单端/joint 严格，距离保原非严格边界。法向中心不需要单位长，实际正常归一化的法向由六 jet/cap 原界包住。

短路径门只在完整闭场 K 已付时使用 `K*length < pi_lower`，保原严格 $\pi/K$ 范围。AA 的路径使用当前完整一 jet；同帽路径只沿同一凸 disk 的参数直线。不会把两帽之间的直线当作曲面路径。

同帽的较直接门只使用 R24 §3：完整同侧 $H_b=\sum8|A_i|/R_i^2$，`H_b*tau<=1` 支付该同图的法向弦，并由 XY 恒等给单射。`R24_weak_marker_transfer_or_support_distance_claimed=false` 始终保留。

### 5.2 对角商、cuff 和相位

原相同材料点只按中央/cut/cuff/周期边界的准确商关系识别，不以距离阈值删除近点。R282 局部门必须在整个当前 leaf 的径向、cap disk 交及材料角×phase 区间上满足 membership。含零弦的 parent rank 不会整段豁免；非局部相位仍由原四门支付。

当前 collar 在 R416 cut patch 以外；原 CuffOwner 使用的全系数与 shared B 真是当前同场。完整 Phi、rho 正下界、mean/Nyquist、负 marker 与支撑重叠不省。

### 5.3 完整 flags

只有全部条件同时成立才设置：

```text
accurate_family_embedding_and_reach_certified = true
accurate_family_reach_lower = 原 tau
```

这些条件是实际已绑定的闭 C² 构造、完整正则/曲率、全部 AA/CC/AC 支付、`K*tau<=1`、没有执行错误或资源未退休部分。对 root 族的区间包围作统一充分条件，不用任意中点选择某个真实成员。

`README_reach_fraction_paid` 另需完整位置 cover 给出的整个标记 $F_0$ 的 `D_upper`，且原输入 tau 不小于 `3/100*D_upper`。本程序绝不从 D 重新选择 tau；它也不把 bbox 用作 reach 或 embedding 门。metric、held、非全等、原 BVP/数值 shadow 误差和课题全部终门仍分别未付。

## 6. 完整 CLI；本次没有实际参数值

```text
--computations PATH
--directory ACTUAL_R409_DIRECTORY
--result-sha256 ACTUAL_R409_RESULT_SHA
[--checkpoint-directory PATH]
[--proof-directory PATH]
--cuff-atlas ACTUAL_R413_ATLAS
--cuff-atlas-sha256 ACTUAL_R413_ATLAS_SHA
--curvature-upper EXACT_K
--target-reach EXACT_TAU
--active-depth INTEGER
--curvature-max-depth INTEGER
--pair-max-depth INTEGER
--interval-bits INTEGER
--sqrt-bits INTEGER
--max-cells INTEGER
--max-pair-nodes INTEGER
--max-pairs INTEGER
[--cache-entries 32]
[--max-constant-levels 32]
--budget-seconds FINITE_POSITIVE_SECONDS
[--free-bytes-reserve 2147483648]
--out NEW_OWNED_DIRECTORY
```

`K`、`tau` 为准确有理文本；正性是原几何定理适用范围，源码不自选或重调。未来若已有 owner 固定的 K/tau，应逐原输入传入，本次不生成数值实例。初始深度与最大深度、精度、cell/pair 预算均必须由未来执行 recipe 明示；不存在为使结论通过而暗改常数。

`produce(args)` 是同一主入口的 callable 版本；从 Actions 主线程调用，以便安装 SIGTERM/SIGINT 标志处理。参数 namespace 与 CLI 相同，fresh out 由它拥有。它不是接受一个 `completed=true` 字符串的捷径；仍运行全部原来源 guards。

## 7. 资源、停止与完整 pending

整体计时在创建自己的 fresh out 后、实际模块加载和输入绑定前开始，包含 setup；检查发生在明确操作边界。它不是绝对杀钟，不声称能在单次不可中断底层调用中精确截停。未来 workflow 的硬 step/job 限制仍独立存在。

每次检查实际 out 所在盘的剩余字节。SIGTERM/SIGINT 仅记录标志，不在 ledger 退休事务中间异步抛异常；下一个边界保全部 pending 后退出。硬杀或 I/O 故障若阻止最终文件闭合，不能从缺失的 result 推断通过。

曲率 `max_cells` 计完整 cell 尝试；pair `max_pair_nodes` 计每个实际空间×phase 节点尝试；`max_pairs` 计原根 rank 范围。R422 不改变 native 轮数/试步、原曲率数学范围或原相位 OR。

每个 DFS 都保当前 stack 顶，先检查资源，计算并写完整 terminal/split，再 pop/替换。已捕获资源/异常时保：

- 当前未退休 root 或 pair 的完整身份；
- 当前完整闭 frontier/所有兄弟；
- 未访 root 或 rank 的半开索引后缀；
- 已到最大深度的所有 terminal 未付地址，完整留在原账本；
- 若绑定未完成或扫描尚未启动，对应整个域/后缀的明确未付状态。

`resource_partial`、未付下界和原执行 error 分开。区间下界不正不是曲率/分离的实际反证；深度或工作量用尽不是无解。当前固定根族/模型盒可能仍较宽，空间细分不会自动生成新的 root 族或去掉原不确定性，也不承诺有限资源终止。

## 8. 临时输出和唯一必要摘要

输出仅写新 `--out`，不会改任何来源输入、旧 accepted flags、marker、target、R416/R417源或旧静态路线。

主要原件：

| 成员 | 完整作用 |
|---|---|
| `input-binding.json` | 本次所有真实输入/当前场/帽/原目标/直接源身份与显式 K/tau |
| `large-arrays/complete-root-universe.json` | 每原 piece、两 sheet、两帽与完整 rank 公式 |
| `large-arrays/complete-spatial-enclosures.jsonl.gz` | 每次真实活动六 jet/帽 cell 的完整原包围、球、正则/曲率值及来源 |
| `large-arrays/complete-curvature-cover.jsonl.gz` | 全部实际闭 split、terminal、原未付地址 |
| `large-arrays/complete-pair-space-phase-cover.jsonl.gz` | 全 root begin/end、每空间×phase 原门、完整 Sturm catalog、split 和 terminal |
| `large-arrays/actual-complete-collar-coefficients.json` | 原 R282 完整当前系数，含 mean/Nyquist |
| `large-arrays/actual-cuff-local-constants.json` | 原 CuffOwner 全候选/实际选择与范围 |
| `large-arrays/same-accurate-cut-DAG.json` | 同一 R416 实系数表达 |
| `large-arrays/complete-original-ten-target-binding.json` | 同一十参数/原 C/原目标 |
| `large-arrays/current-complete-cap-binding.json` | R417完整 marker/side/cuff/高度与来源 |
| `large-arrays/actual-used-complete-field-identity.json` | 本次真实使用的原节点/表达身份；不补造未用数组 |
| `result.json` | 完整计数、所有 pending、曲率/路径/D/pair/最终范围 |
| `necessary-summary.json` | 唯一对外必要摘要，最多90000 B |

每个 gzip ledger 保压缩原 bytes/SHA、decoded bytes/SHA 与完整行数。这里只记录这次实际流，不把它当 root 本地逐数值复核。完整大 ledger、DAG、输入数组和 source tree 不分包、编码或上传到 Git/Release/artifact。

唯一 stdout 标记：

```text
BEGIN_R422_CURRENT_C_COMPLETE_REACH_SUMMARY
<single necessary JSON>
END_R422_CURRENT_C_COMPLETE_REACH_SUMMARY
```

必要摘要保全部实际 completion flags、counts、各 family 数、完整未退休 frontier/后缀、K/tau/D/比例、原异常/停止、所有成员身份及剩余责任。完整原 piece 表和大量 terminal 账本仅以实际身份引用，明确未在聊天逐值返回。若必要摘要自身超过90000 B，返回70并保尝试 bytes/SHA、result身份和未完整读回状态，不提升上限、不静默截科学字段。

有 `GITHUB_OUTPUT` 时，写 `closed_reach_summary`、`closed_reach_summary_bytes`、`closed_reach_summary_sha256`。无内部执行异常的正常或资源 partial 返回0，不意味着数学通过；执行异常返回1，外部 signal 返回128+signal，summary超限70。没有自动 cleanup：后继读取/发布只拿必要摘要；临时原输出必须按实际读回状态处理，不能在尚未读回时主动删掉。

## 9. 本次静态边界与未付项

已做原源码阅读、source 文本写作、完整差异和 byte/SHA 核对、纯纸面参数路径/球/商覆盖推导。未 import/运行任一科学模块，未 AST/编译，未构造合成 fixture。R417 的字段/side 对应已按原实际源码窄核；它不是新调度门，更不是实际 reach 数据。

目前**整个实际几何 cover 均未执行**。当前源接口不能生成一个假的 accepted450，也不把准确 Hermite 定义节点当作已认证的原 RK 轨迹。准确模型的全闭场存在/接缝结构与所有实际正则、曲率、分离余量仍按上述层次分别支付。

未来完成本组件以后，仍需同场的全域相对 metric、held 集合/整像 Hausdorff、含反射 Euclidean 间隙、原非线性及所有课题标准。没有 request 号、未来 run、数值 K/tau、接受结论或额外前门在本次被填入。
