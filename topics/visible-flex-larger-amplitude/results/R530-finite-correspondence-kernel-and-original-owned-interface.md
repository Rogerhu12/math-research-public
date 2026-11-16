# R530：有限双向全对应内核与原 owned 调用的完整接口

作者：OpenAI ChatGPT（AI，geometry 子任务）。日期：2026-11-16。

**可信度：已证明（限下述程序条件命题）；源码已写，未执行科学计算。** 本文登记 R526 的实际有限内核和一份明确的 R520 调用源视图。没有新请求、实际场、接受父、选定 $\gamma$、数值结果或性能结论；当前217、223及其他冻结工作流未改变。

本实现直接消费原绑定器生成的 `BoundImages`。它不复制完整场、帽函数、位置覆盖器、原 owner 或原数值求解器。发布两运行件：新的29146B内核，以及10974B完整 literal source plan。46134B新调用器只在 Actions 的真实 computations 中由已刊 R520 逐处生成，不作为另一份大依赖复制入 Git。

## 530.1　已付证明与本次职责

数学依据是正式 [R526](R526-complete-bidirectional-distance-correspondences-and-quotient-lower-bound.md)，21774B，SHA256 `a02c931e0453b499abfa763a934953581d7d2f995d71301e5d19526c2efb4b49`。其中已证明全部双向对应及所有交叉边给下界，以及

$$
0\le L_*\le\Delta(A,B)\le d_{\rm E}(A,B).
$$

本文只证明该程序的前缀组织、原始输入绑定和中断状态满足上述命题，不重新证明 R526，也不将 $\Delta$ 冒作 $d_{\rm E}$。固定正候选 $\gamma$ 必须由未来实际调用者明确给出；本包没有一个预设的数值候选。

原 [R520](R520-generated-current-images-original-owned-quotient-interface.md) 已把实际222派生源和三场族登记到 R517 的完整输入绑定。原 R517 提供：

- 完整 R425 `result.json`、输入binding、position result、所有位置账本行及 stored/decoded 身份读取；
- 原实际 R417 帽函数在准确有理闭盘点的求值，保全部同侧负幅度与重叠marker；
- `BoundImages.cover0/cover1/witness0/witness1`；
- 准确平方距离、有理平方根外包、普通成员身份和临时完整 gzip decision ledger。

本次的 `registered_backend` 逐项绑定实际 R520 plan、明确 family、实际 module 路径、完整 source bytes/SHA、R425/cap 名称、SHA和schema。不能把任意传入球表、旧 schema 或另一个类实例当现成的完整输入。

## 530.2　发布件、生成件及原依赖

| 角色 | 完整 basename | Bytes | SHA256 |
|---|---|---:|---|
| 新内核 | `geometry_20261116_bidirectional_distance_correspondence.py` | 29146 | `d73e4ad2839ad4f058b840895a5708dda3cf324d2574b5ab5a9c82536df77eec` |
| 新 source plan | `R530-original-owned-distance-correspondence-source-plan.json` | 10974 | `bae555ea0617fdd1efb3e895e9471a9018fb8060298f321a8253c238c1a98ed6` |
| Actions生成的新调用器 | `geometry_20261116_current_generated_distance_correspondence.py` | 46134 | `3d6ff2c2547e0096c79e9cfe1490399364c55ed571a4c80eac49a2e101ba15f0` |
| 原调用器 | `geometry_20261116_current_generated_image_quotient.py` | 47597 | `8d48856dcdc642f56779bff949a473b352c26edf0fda9e65937e2ce4feba1ef2` |
| 原三族binding计划 | `R520-current-generated-image-quotient-source-plan.json` | 11453 | `e288f2d037c65f05682ec498ab4230613920d82a3deb15780567d43088fe5877` |
| 原 owned helper | `geometry_20261116_request220_owned_roles.py` | 25670 | `4afc01350bbaa239556f3b3edab6260b727e772df3b04351e357b0831149efc3` |
| 原222修复入口 | `root_20261116_request222_source_classification_repair.py` | 28224 | `20360bb001f3849b3468071b4ca6f7b4017d5aa2bb7fb476791316d1a96a432f` |

发布内核位于本题 `computations/`；source plan位于 `notes/`。计划包含18个完整 `before/after/count` 替换以及完整输出SHA，未删数学核的任何必要输入。

完整调用器差异为14380B，SHA256 `4f7db810024812cd0e6984c4c25ae38ca17f9dc2afb04df4b3acde88cd868e34`。它是临时交接材料，不是新科学结果或另一份必需运行源；所有变化已完整包含于发表的计划。

原R520的三个真实 binder 保持：

| family | 原实际 binder | Bytes | SHA256 |
|---|---|---:|---|
| `original112` | `geometry_20261116_full_E3_quotient_lower_bound.py` | 39936 | `0c69c61c09a8f518e792495fd1109b7f310d57da69676368a51233b648a4ba89` |
| `resolution112` | `geometry_20261116_R520_resolution112_quotient_kernel.py` | 40003 | `5e53b80c1dd1db9f2817241bb6de06755b51381b4d61e5842847fe3784e9a02a` |
| `incrementalM` | `geometry_20261116_R520_incrementalM_quotient_kernel.py` | 40066 | `372a7d3cb7000e21fb3427568175b48d86e589538d3897116e3cc53f7aa63139` |

后两件由原 R520 `prepare` 真正生成；它们仍仅改变原R517输入来源登记。R530 不调用其 pose 遍历，而调用其完整 `bind_r425`、准确距离原语与原账本工具。

实际三族 producer/cap/shared/held tuple 全按原 R520 plan，不增加未知第四族，不把真实派生源重标成 c87b/0ff1。原222派生220请求仍是99330B/`2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2`。

## 530.3　数学数据和两方向统一编号

在实际完整绑定返回以后，取

$$
A=S_0,\qquad B=S_{\pi/2}.
$$

内核保原四列表的次序：

- `cover0`：$A$的完整包含球；
- `cover1`：$B$的完整包含球；
- `witness0`：$A$的真实成员球；
- `witness1`：$B$的真实成员球。

所有坐标和半径由原 binder 转为 `Fraction`。不把盒中心冒作准确曲面点。原位置覆盖必须完整；原R425 work-resolution、metric/reach/germ成功不是新前提。

设真实成员数量为 $n_0,n_1$，目标球数量为 $m_0,m_1$。前 $n_0$ 个变量分别将 `witness0[i]` 配到 `cover1[k]`；后 $n_1$ 个变量将 `witness1[j]` 配到 `cover0[k]`。完整候选族是

$$
\{0,\ldots,m_1-1\}^{n_0}
\times
\{0,\ldots,m_0-1\}^{n_1}.
\tag{530.1}
$$

重复编号始终合法。没有排序匹配、最近球、最大marker、唯一帽点或单射筛选。数量以两个 `base/exponent` 因子的准确形式返回，不为打印巨大整数而提前展开候选乘积。

某个顶点的两中心为 $X_v,Y_v$，真成员误差/目标球半径之和为 $s_v$。内核调用原准确平方距离及有理平方根上下界，形成

$$
G_{vw}=\max(0,l^X_{vw}-u^Y_{vw},l^Y_{vw}-u^X_{vw}),
\qquad
L_{vw}=\frac{(G_{vw}-s_v-s_w)_+}{2}.
\tag{530.2}
$$

新定一个变量时，与所有先前已定变量逐一形成这条边。因此原同侧边和全部双向交叉边均属于同一个前缀；没有只做两次互不关联的单向匹配。

## 530.4　前缀内核的准确状态

`CorrespondenceCover` 使用DFS栈。每个frame有：

- `prefix`：已固定的全部候选编号；
- `next_candidate`：下一个变量尚未访问的第一个编号；
- `lower`：这个已定前缀全部边的最大准确下界；
- `witness_edge`：达到所存最大值的原实际边，包含两区间、全部误差数及原列表地址。

一个frame的未访集合是其固定前缀，加上当前变量的半开编号后缀，再乘所有更后变量的完整目标列表。下潜时，把父frame的后缀推进一项并加入完整子frame，作为一次新的栈赋值；两个动作之间没有预算回调。原父列表在整次替换形成前仍存在。

这些后缀块始终互不相交，且覆盖每一个尚未退役的完整对应。空后缀frame可以暂留到下一次安全弹出，不增加候选。只有在原预算检查以后才移除它。

这里的“完整”是对(530.1)全部有限对应的责任，不是对已经选过的某些峰顶或样点的责任。固定成员并不自动构成整面稠密网；这仍是R526终止条件的独立范围。

## 530.5　退休、未证叶与中断的程序命题

**命题530-A。** 若原绑定真实完整，原平方根区间正确，程序没有未返异常且返回 `requested_quotient_lower_bound_proved=true`，则

$$
d_{\rm E}(S_0,S_{\pi/2})\ge\gamma.
\tag{530.3}
$$

**证明。** 空前缀下界为零。假设父前缀的下界是其所有边的最大值。加入第 $v$ 个顶点时，`evaluate_child` 保留父下界，再逐个计算所有 $w<v$ 的新边。得到新前缀全部边的最大值，归纳成立。

若这个值至少为 $\gamma$，R526定理526-A的同一条边不等式对该前缀的任意完整延拓均成立，故整块延拓可以退役。程序先写实际决策账本，再推进对应的编号后缀。下潜和耗尽frame的处理均保持530.4的完整分割。栈为空时，全部候选均已被一个真实下界至少为 $\gamma$ 的前缀覆盖，故 $L_*\ge\gamma$。R526给(530.3)。证毕。

若到达一个完整赋值，所有 $\binom{n_0+n_1}{2}$ 条边均已沿前缀付完，但最大值小于 $\gamma$，本程序立即返回**未证**。该完整赋值、它所属的原栈后缀以及其他所有未访块保持原样。程序没有必要继续展开余下候选来证明这个给定判据本次不能全退役。

这一返回不是：

- 一个真实刚体运动；
- 全等或 $d_{\rm E}<\gamma$ 的证明；
- 全局 $L_*$ 已经求得；
- 当前场或原BVP的拒收；
- 原所有候选已完成的标志。

它只表示，在本次明确输入包围和精度下，至少一个有限对应尚未被距离必要条件排除。R526已有 $\Delta<d_{\rm E}$ 的纸面反例，不能由此把不足归因于预算或机器误差。

在原预算、信号、磁盘余量或任一明确work上限中止时，当前候选始终还在原frontier。当前边还会保留 `pair`、`distance_side`、已完成的A距离区间（若已算出）、已付边的下界、下一旧顶点编号和对应ledger ordinal。仅一侧距离算完不会用于形成新的边下界。

## 530.6　真实API与结果

内核的实际完整入口为：

~~~python
produce(
    *,
    backend, family, original_plan,
    computations, directory, result_sha256,
    out, cap_points,
    desired_gamma, sqrt_bits,
    max_prefixes, max_distance_evaluations, max_cover_balls,
    check_budget, caller_clock_identity
)
~~~

`backend` 是原R520根据实际family已完整source绑定并加载的K模块；不是字符串形式的假binder。`directory/result_sha256` 指向同job原held producer的真实完整结果；`original_plan` 是原R520 plan，不是新的R530 caller plan。

函数只调用一次 `K.bind_r425`，得到原 `BoundImages` 后直接构造 `CorrespondenceCover`。没有通过摘要、SHA、JSON构造一份假内存场。已有严格绑定的同一内存对象也可直接传给 `CorrespondenceCover`；这种库调用仍需原真实source/budget/ledger条件，不能省掉它们。

新 `Work` 只增加对应法自身三个明确的工作计数：

| 字段 | 准确计数对象 |
|---|---|
| `max_prefixes` | 实际开始评价的非空候选前缀 |
| `max_distance_evaluations` | 实际有理平方距离平方根外包次数；每条新边两次 |
| `max_cover_balls` | 原完整位置ledger真实terminal球数，由原binder收费 |

它没有另起时间起点。每次 `check` 调回同一个原 owned caller 的绝对截止、原信号和原余量检查。到限抛原K.Stop并保原原因。没有“为了新算法能过”修改时间、容量或原求解门。

`result.json` 保新kernel schema/source、原proof身份、完整family/binder/plan、原clock、实际输入范围、原observed source、各work计数、全部错误/资源原因、当前frontier和当前边游标。只有完整成功才设置全局量：

- `requested_quotient_lower_bound_proved=true`；
- `quotient_distance_lower_bound=desired_gamma`。

部分返回的 `minimum_retired_prefix_lower` 只是已退役前缀中的最小值，明示不是全局下界。程序没有从它补填未访部分。

返回码：

| 情形 | kernel返回码 | 必要读回 |
|---|---:|---|
| 全候选已退役 | 0 | 完整必要对象 |
| 未分离完整对应，或原资源停止 | 2 | 保完整未访与原原因 |
| 实际异常 | 1 | 原类型/文本/完整traceback及未访 |
| 必要正文超90000B | 70 | 原正文bytes/SHA及真实result身份，明确未完整回传 |

返回码不改原BVP/metric/reach任何门。原调用者仍须真实观察owned进程静止，才能讨论其原清理条件。

## 530.7　完整输入、两帽与数据生命周期

原binder继续要求原完整position result与result内的position逐值一致，全部root完成、pending为空、两帽root存在；随后真实流读整个原gzip位置ledger并核行序、全部terminal/split/严格空盘单元计数及stored/decoded身份。新kernel不以这份大原件的SHA代替其读取。

原真实活动成员和准确有理帽参数保留在 `all-actual-member-balls.json`。帽点使用真实

$$
F_{\rm side}(x,y)=(x,y,\ {\rm side}\,[H+\sum_i A_i(1-\|p-c_i\|^2/R_i^2)_+^4]).
$$

准确有理参数须在原闭cuff盘内；全部同侧marker参与。支撑中心不等于峰顶，负幅度和重叠不能省。帽成员在两phase中固定；活动成员按原quarter-turn规则变换。这些均调用原R517/R417绑定器，不在R530复制第二个帽数学函数。

新 `complete-correspondence-decisions.jsonl.gz` 是同job临时完整账本，记录开始前缀、每条已完成边、整前缀退休及未分离叶。原准确中心/半径来自完整输入账本；边行用原列表地址与前缀ordinal定位，不重复搬全目标球表到聊天。该新账本有stored及decoded bytes/SHA/rows。

程序不删任何原场、原far账、原R425 payload或新决策账本；不上传可重生大raw。成功行只通过身份报告，不声称其正文已经全部传回。整个frontier、当前未完成边、实际未分离叶、错误及资源文本仍是完整必要正文，不能缩成一个SHA后宣布读回完成。

## 530.8　一份source view复用原调用器

新source plan只生成：

`geometry_20261116_current_generated_distance_correspondence.py`。

其相对原R520变化只有明确的来源/调用责任：

1. 独立R530 schema、source、frame和事件；
2. 增加真正R530内核的完整source pin；
3. 原K继续做完整image binding，新C负责有限对应计算；
4. `max_boxes/max_depth` 的pose工作参数在这个新方法中不使用，明确改为 `max_prefixes`；
5. 必要读回核新C结果schema/source，同时核其返回的原K binder身份；
6. 原两image view的source-preparation schema明确仍属真实R520；`prepare` 委托原R520函数，不给原准备结果改标签。

原Binding的derived220、完整repair、startup、原BVP-launch实际deadline、held/raw/shared/cap来源检查均保。原 `launch` 中 OwnedTree 创建、PID/start_ticks/session、TERM→KILL/reap、原绝对截止和实际quiet算法保；唯一差异是新独立事件名和该新source自己的实际argv。

原 `run` 内 `check_budget` 正文保持：信号、原绝对截止、原refinement磁盘保留。原startup BVP的32GiB门也不因这个后置库改变。

原 `build_readback` 的held quiet只观察原procedure记录的进程及所记owned组，不把R530新child自己当成原held仍运行。新R530 child则由原H的实际OwnedTree独立观察；新必要读回在child返回后再次使用原namespace owner观测。没有“因为自检在运行，所以永远不能读原场”的来源错位。

## 530.9　实际CLI和准备顺序

下列是未来同job调用合同，变量必须来自该job实际路径与receipt；本次没有创建这些数值输入或触发命令。

先按原R520流程实际生成两个image binder view，且只做一次。若本job已有真实完成的原准备结果，使用该结果而不覆盖原文件：

~~~sh
python -u "$COMP/geometry_20261116_current_generated_image_quotient.py" prepare \
  --base "$BASE" --computations "$COMP" --plan "$ORIGINAL_R520_PLAN"
~~~

新源材料化入口：

~~~sh
python -u "$COMP/geometry_20261116_bidirectional_distance_correspondence.py" materialize \
  --base "$BASE" \
  --computations "$COMP" \
  --original-plan "$ORIGINAL_R520_PLAN" \
  --plan "$R530_CALLER_PLAN" \
  --plan-sha256 bae555ea0617fdd1efb3e895e9471a9018fb8060298f321a8253c238c1a98ed6 \
  --out "$R530_SOURCE_PREPARATION_DIRECTORY"
~~~

`COMP` 必须是该Python源的实际HERE，也必须是原222真实metadata工作视图内的computations。新output位于原BASE内的全新自有目录。材料化先绑定原R520 source/plan和原已生成两view的完整receipt，再逐literal count形成全部新source bytes，核完整输出SHA，最后以 `xb` 写新basename。不覆盖任何旧源或同名现存view。

材料化真实receipt：

- 文件：上述新目录的 `result.json`；
- schema：`R530-original-R520-owned-distance-correspondence-source-view-v1-actual-preparation`；
- 保当前run/source、原caller、新kernel、完整新plan、真实原image-view准备receipt、唯一原namespace start；
- 失败保 `error` 与整个未确认source列表；
- 该操作只做source文本材料化，不生成image或证明任何下界。

实际 owned 调用和必要读回：

~~~sh
python -u "$COMP/geometry_20261116_current_generated_distance_correspondence.py" launch \
  --input "$ACTUAL_R530_INPUT" --input-sha256 "$ACTUAL_R530_INPUT_SHA256"

python -u "$COMP/geometry_20261116_current_generated_distance_correspondence.py" readback \
  --input "$ACTUAL_R530_INPUT" --input-sha256 "$ACTUAL_R530_INPUT_SHA256"
~~~

`launch` 内部真实调用同一新source的 `run`，沿原OwnedTree建立独立session。不能由调用者直接跑 `run` 再补造owner记录；原 `bind_running_owner` 会核实际PID、start_ticks、session与原record。

## 530.10　完整input字段

新输入schema为

`R530-current-generated-images-original-owned-distance-correspondence-v1-input-v1`。

| 字段 | 真正来源/含义 |
|---|---|
| `entry` | 新生成46134B调用器的实际file/bytes/SHA |
| `family` | 原已登记 `original112`、`resolution112` 或 `incrementalM` |
| `namespace` | 同一实际原BASE，不能建立第二个science起点 |
| `computations` | 实际metadata工作视图的COMP/HERE |
| `source_plan`、`source_plan_identity` | **原R520三族plan**路径和11453B/e288身份；不是R530 caller plan |
| `held_directory` | 同job该族原held wrapper目录 |
| `held_procedure_sha256` | 原真实procedure.json完整SHA；原未返时按原not_started责任保留，不能捏造 |
| `cap_point_plan` | 实际有理帽点计划receipt；其schema仍是原 `R520-current-generated-images-original-owned-quotient-v1-explicit-cap-points-v1` |
| `desired_gamma` | 明确正有理字符串，不提供默认值 |
| `out` | 原BASE内新自有结果目录，不包含原source/input/held |
| `actual_owner_role` | 原OwnedTree记录的新明确role名 |
| `actual_owner_record` | 原BASE内该role实际 `role-ownership.json`；与child结果目录分开 |
| `resources` | 下表明确工作预算 |

`resources` 保：

- `budget_seconds`；
- `owner_bind_budget_seconds`；
- `sqrt_bits`，整数且 $0\le{\tt sqrt\_bits}\le8192$；
- `max_prefixes`；
- `max_distance_evaluations`；
- `max_cover_balls`。

后三项为明确正整数，不接受布尔值冒整数。它们只限制执行工作，不是新的几何/求解门。旧pose `max_depth` 与 `max_boxes` 不能解释成对应算法已支付的工作。

帽计划仍为原schema加 `points` 列表，每点明确 `x,y,upper`，前两者准确有理、最后一项bool。所有点都须是真实当前帽定义的闭盘参数，不能给已有点云的猜测坐标。

## 530.11　原clock、未启动范围和quiet

原R520流程仍先绑定：

1. 真222修复结果及唯一 `namespace-start.json`；
2. 原startup资源计划，其namespace科学时长18900秒、读回保留2700秒；
3. 后续实际 `BVP-launch/result.json` 指向的真正launch-bound deadline；
4. 上述deadline与原startup通过实际source-namespace receipt及同一原起点的关系；
5. 该family真实held/deadline/shared/atlas及whole-image结果。

startup plan与实际BVP deadline不是同一文件，不伪要求两者byte相等；同一后置held和新consumer实际使用的launch-bound deadline仍必须相同。

若BVP原deadline、原held procedure、原whole-image producer或原完整position cover未返，沿原not_started/未付范围返回。没有从部分源数据或zero-filled球表启动搜索。

绝对科学截止仍由原namespace起点加18900，原终测保留和child shutdown余量照原配置扣除。新显式role cap只裁已有余额；原读回仍裁到同一起点加21600。时间/工作失败不重开钟，科学资源失败不伪转数学否定。

本包不删除raw、不写可冒充整个工作流清理许可的marker。是否最后可以清理，仍需未来真实caller接它的完整必要receipt，并满足原所有scope和真实owned quiet；单独kernel返回0不等于整体cleanup。

## 530.12　必要正文和90000B边界

kernel独立frame：

~~~text
BEGIN_R530_COMPLETE_CORRESPONDENCE_NECESSARY
END_R530_COMPLETE_CORRESPONDENCE_NECESSARY
~~~

原owned薄调用器的独立frame：

~~~text
BEGIN_R530_OWNED_CORRESPONDENCE_NECESSARY
END_R530_OWNED_CORRESPONDENCE_NECESSARY
~~~

对应事件：

- `R530_actual_owned_caller_source`；
- `R530_actual_original_owned_correspondence_invocation`；
- `R530_complete_necessary_readback_identity`。

kernel必要正文包含全部frontier、当前前缀/边/半边游标、未分离完整赋值、所有实际错误/资源原因、原完整输入和新决策账本身份。成功全数组/全部边行仍在临时大原件；不声称已通过聊天逐行读回。

owned必要正文仍包括真实wrapper、actual child/launch/owner/quiet和kernel必要对象，按实际source绑定核 `result.json` 与必要摘要指针。它不会仅因为child exit2就把完整必要对象丢弃，也不会因源scope正确而填数值成功。

两层分别有90000B限制。即使内层恰低于限制，外层增加真实owner元数据后仍可能超限；此时外层如实70，原正文identity和raw保留。没有“所有未来frontier都保证适配90K”的承诺，不通过删未访、分包或编码绕限。

## 530.13　明确未付和以后可做的事

本次已接一个实际可调用的后置角色，但没有把它加进217、222或其他运行中的工作流，没有生成实际input、$\gamma$或场。它也不自动要求另跑原pose方法；未来可按同一预算组织两种合法下界法。

本方法的有限成功依R526；一般 $\gamma<d_{\rm E}$ 不保证能由距离松弛排除。固定C盒、固定成员点或固定位置球不保证随本搜索收紧。若首个完整对应未分离，诚实未证即可，不能据此否定原field或增加BVP gate。

没有新增浸入/嵌入、reach、同g精确解、连续$t$极限或机器精度声明。只有实际整个对应族被正确退役后，才得到(530.3)，再按原定义可推出相应 $\delta_{\rm E}$ 下界；直径与任务比例仍由其原同场完整输入负责。

所有科学算术、import后的科学调用、编译和任何实际验证都只允许原公共Actions。本文交付过程仅源文本、JSON/literal变更、字节身份与上述条件推理；没有本地执行、AST、fixture或独立实验门。
