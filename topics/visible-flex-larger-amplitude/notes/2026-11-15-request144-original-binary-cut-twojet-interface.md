# Request 144：原 binary cut 优先 query 与同一 v3 全叶两 jet 读回接口

作者：AI（geometry）  
日期：2026-11-15  
状态：独立读回源码和公开 Actions 接线已形成；本接口没有预填 Request 144 的 run、结果或接受结论。  
数学执行范围：仅公开仓库 Rogerhu12/math-research-public 的 Actions。

## 1. 这次接线的准确改动

Request 139 已实际完成原 160×9 个有限头 piece、全部六 primitive 和整个自然闭径向域的有效包围；原整域 work-resolution 仍未完成，参见 [R311](../results/R311-actual139-complete-continuous-C-domain-and-unpaid-resolution.md)。它证明原 binary cut 被真实自然半径覆盖，但原 query 总结果只提供 $E$ 总界，不能从该总界推造 $E_r,E_{rr}$。

144 保持同一已发表 `geometry_20261115_stored_continuous_E_cover_v3.py` 的原字节与所有科学预算。明确新增第一项 query：原 config 的 `rCut` 点；原 whole-natural-domain query 作为第二项完整保留。有限头与所有 primitive 仍在本次实际重算，没有依赖已清理的 139 raw。

新增独立读回源只在同次 Actions 中读取该点 query 的完整叶区间流，按原精确 dyadic 两端生成 $E,E_r,E_{rr}$ 三个区间的并包和全宽。它不重积分、不调用 ODE/J、不选择新深根、不改原目标 C、不加入导数宽度接受门。原 E 的 work-resolution 判据保持原样。

此运行不要求新 accepted 场，也不产生 cut DN。新 g factory 的 v3 消费必须使用自己的明确源身份；原只认 v2 的 factory 不因这次结果出现而自动变成 v3。

## 2. 文件与身份

| 文件 | 字节 | SHA-256 |
| --- | ---: | --- |
| geometry_20261115_stored_C_v3_cut_twojet_readout.py | 19023 | `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed` |
| original-stored-continuous-E144-queries.json | 1303 | `4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59` |
| public-original-stored-continuous-E-request.json | 11288 | `dcd4a892c8b38bf5f3f1923ea530a58095e76fd52ccdfeed4962370f5ff21e1f` |
| visible-larger-public-stored-continuous-E.yml | 27336 | `209794c4601c6bcc4ef04a9d0491b3d3c8c84c6d7a2f2f49b0d8ec99c14464c0` |

前三件位于 `topics/visible-flex-larger-amplitude/computations/`，workflow 位于 `.github/workflows/`。原 shared request 的路径保持
`computations/public-original-stored-continuous-E-request.json`；只有这个原 push trigger 触发本次计算，不增加并行重复 lane。

唯一新计算读回源 schema：

`R286-v3-original-binary-cut-complete-twojet-hull-v1`。

原数学 producer 的实际身份保持：

- v3：89307 B / `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df`；
- 原 v2：77697 B / `004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea`；
- 原 v1：66415 B / `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed`。

当前运行文件 pin 由原 10 件加新读回源成为 11 件。原 9 份 formula source、原 restore revision、两件旧 producer、R286/R297/R306 三篇证明和三原输入全保持。没有把新的字节读回源加入原物理公式。

## 3. 原 cut 的字词含义

新 query id 是 `original-binary-config-cut-point`，类型是 `closed-rational-radius-interval`，两端都闭。Recipe 的两个数值 token 是原 config 中已有的 JSON numeric `0.3`。这里不是数学上精确的 $3/10$：

1. 原 config 原 bytes 由 SHA 绑定，恢复后用 Python 原 JSON 语义读取其 binary64 数值；
2. 新 query 的两个 numeric token 以同一语义读取；
3. workflow 在任何科学执行前逐个 `struct.pack("<d", value)` 比较三者；
4. 原 v3 的 `rat` 用 binary64 的精确有理值形成查询端点；
5. 新读回源再次以实际 config 的 `as_integer_ratio()` 与实际 producer query 的 rational 字符串比较。

因此查询的是那个原二进制字，且保持实际 little-endian word、精确有理表示和来源 config SHA。没有用 nominal decimal、自然 $R_{\rm out}$ 中点或重新缩放的 cut 替代它。

第二项保留：

`whole-original-source-natural-continuous-domain` / `whole-natural-domain`，两端闭。它的右端是由完整六 primitive 形成的真实自然 $R_{\rm out}$，不是名义 cut。

若第一项消耗预算，原 v3 会按其已存在逻辑保留第二项的完整未访后缀；本接线不隐藏它，也不扩大 1800 秒预算来强迫第二项完成。

## 4. 三个真实原输入

全部从已付历史 ref
`8bd267107cc8710d371f3b62c02986655ac965b0`
在 Actions 内逐 byte 恢复；输入不重序列化。

| 输入 | 原字节 | SHA-256 |
| --- | ---: | --- |
| T112-config.json | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| 原 calibration ledger ready | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| 原 stored-reference ready | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

原路径分别沿 request139。第一件公开 Git blob 为 `543d8364593985305438dda6a0c89b4b1a9c7ec5`，后二件为 `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3`、`b6c44fe237750f13c8b10366f15525b481a74e09`。

新的 query 文件额外绑定上述三个 SHA。读回同时比较实际 v3 input-binding 中的 config/query 原件 bytes/SHA 及两 ready SHA。它不从历史 ready 的 finite 指纹推定 C 是旧 finite selector 的连续认证解。

本次模型始终是明确的
`R286-original-stored-continuous-model-convention-C-v1`，
deep definition 为 `original-exact-root-family`。所有允许的原精确根序列均保留，未选定某一条深根；没有 R26 数值证书替代，也没有改全局冻结 warp 系数。

## 5. 新读回源 CLI 与输入闭合

```text
python geometry_20261115_stored_C_v3_cut_twojet_readout.py \
  --directory "$VISIBLE_BASE/continuous-E" \
  --result-sha256 "$ACTUAL_SAME_RUN_V3_RESULT_SHA256" \
  --config "$VISIBLE_BASE/original-inputs/tail-config.json" \
  --config-sha256 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5 \
  --query-recipe "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/original-stored-continuous-E144-queries.json" \
  --query-recipe-sha256 4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59 \
  --out "$VISIBLE_BASE/cut-twojet-readout"
```

实际 result SHA 由同 job 中真实文件即时计算，不在请求中填未来值。新输出目录必须不存在且不能拥有原输入。

入口先检查 `GITHUB_ACTIONS=true` 与确切仓库名。它只导入 Python 标准库，不 import v3/Flint，不运行原模型构造器。其计算只包括原 finite/binary scalar 到精确有理表示、整数 dyadic 比较、并包和全宽；这些新读回算术也只在 Actions 运行。

来源必须同时满足：

- v3 result schema/source SHA/model 与当前 `GITHUB_RUN_ID/GITHUB_SHA`、仓库一致；
- 原报告保留 `original_real_profile_and_model_C_unchanged` 和明确模型选择标志；
- 原 input-binding 的 source、config、query、两 ready、physical `rCut` 与 convention 一致；
- 实际 query output 的唯一点 id、原 index 0、类型、精确端点与闭端点标记一致；
- 所有被读描述器的原相对路径受限于结果目录，逐完整 bytes/SHA 核对。

本脚本是同 job 读回接口。以后跨 job 消费已发表小结果时，应另以真实结果原件 SHA 绑定，不通过伪造当前 run 环境让这个入口冒充当次 producer。

## 6. 何时可输出完整两 jet

`point_twojet_enclosure_complete` 只在原实际报告同时具有下列事实时为 true：

- 原点 query 的 `complete_closed_domain_bound` 和 `domain_containment_proved` 为 true；
- 原 query 的 `continuous_model_family_conditions_proved` 为 true；
- 全有限头完成；
- 原完整连续 family conditions 为 true；
- 该点的完整 `leaf_ledger_rows = [first,stop)` 存在且非空。

读回还用原 dyadic $R_{\rm out}$ 下端与原 cut 做精确比较，并核原 cuff 不在 cut 之外。这是对既有 domain certificate 的原边界交叉核，不重新选择域或增加几何阈值。原自然半径及其与名义 binary cut 的差的完整记录直接复制进读回。

若源、点域或 family 条件未完成，则 `same_point_E_Er_Err_enclosures = null`，保原 point/result/error/suffix 和完整流身份。它返回诚实 partial metadata；没有据此判目标不存在，也没有填猜测导数。若原 producer 没有最终 result，workflow 只输出明确 unavailable 事件。

若点域完成而 whole query 后续未完成，已经完整证明的点两 jet 可以保留；报告同时保原全 query domain/work-resolution、未访后缀和 error，不能把局部点成功改写成所有 query 成功。

## 7. 完整闭叶并包为何有效

设 $\mathcal S$ 是 R286 所允许的原精确深根序列集合，$c$ 是绑定的原 binary cut。对任意 $\sigma\in\mathcal S$，原连续半径严格单调，其真实逆像位于原 v3 保留的闭逆像叶覆盖之中。原 `entire_possible_inverse_fragment_included` 保证没有以点采样代替整个可能逆像片。

令实际点 query 的原叶集合为 $\mathcal L_c$。每个叶 $\ell$ 有源已计算的
$$
I_{\ell,0},\quad I_{\ell,1},\quad I_{\ell,2},
$$
分别包围该叶所有可能逆像上的 $E,E_r,E_{rr}$。读回对 $j=0,1,2$ 定义
$$
I_{c,j}=
\left[
\min_{\ell\in\mathcal L_c}\inf I_{\ell,j},
\ \max_{\ell\in\mathcal L_c}\sup I_{\ell,j}
\right].
$$
任意真实逆像至少位于一个保留叶，故对应的真值属于 $I_{c,j}$。叶在闭端点上重叠或因根族不确定性而重复覆盖，不影响包含关系；不能因此删叶，也不需要选其中一个叶代替整个覆盖。

原 head 叶使用其真正连续表达式的导数；deep 叶保留其无限原根族和 cuff 包含范围。读回自身不根据有限点值差分重建导数，不把 `ap` 标签或旧 finite source 的导数误当成 C 的真导数。

每个原端点均以整数 mantissa 和整数 binary exponent 表示。比较时将两整数移到同一二幂格点，只有精确整数比较，没有先转换 binary64/display 中点再并包。全宽也直接用同一格点上的上端减下端，报告为精确 dyadic。这里“全宽”不是半径；没有丢掉因显示圆球造成的外扩。

额外一致性检查要求新完整叶 $E$ 并包包含在原 query 报出的 $E$ 区间内。原 producer 的 `arb.union` 可能向外扩大，所以新精确端点 hull 可以更窄；这不构成重算原积分或删叶。

三个分量各自并包会失去它们之间的相关性，但保留包含性。下游不能任取三个中点并宣称它们必然同时来自同一条原 C 根序列；若新数值构造把中点当参数，那是需要另行声明的构造选择，不能从本接口得到真实 jet 恒等证书。

## 8. 全叶和完整流的实际读取

读回按原 `query_inverse_cover` 描述器顺序流式读取整文件，一次核完整 byte count、row count、SHA。对点的 `[first,stop)` 范围内每行，核：

- `query_id` 是那个唯一原 cut 点；
- `kind` 只为原 `head` 或 `deep`；
- `entire_possible_inverse_fragment_included = true`；
- `work_resolution_met` 保原 bool；
- 三个区间均有完整有序 dyadic 上下端。

每一条点叶都参与三个 hull；未达到原工作分辨率的叶同样参与。点外的 whole-query 行也计入完整流 hash/行数，但不混入点 hull。实际点叶数、各 kind 计数、未达工作分辨率叶数与原 span 一并记录；读回不输出重复的大叶 payload。

原 source 的区间有效性依靠已固定 v3 与 R286/R297/R306 的数学责任。这个读回不声称第二次独立计算所有积分，也不拿 hash 检查替代连续分析。

## 9. 两类宽度与输出 schema

原 v3 的 query 工作条件只考察 $E$ 值的 width。144 没有要求或伪称该条件已经控制 $E_r,E_{rr}$。源里显式记录：

- `derivative_work_resolution_requested_by_original_v3 = false`；
- `no_derivative_tolerance_gate_added = true`；
- `valid_coarse_hulls_not_discarded_for_missing_work_resolution = true`。

完整点两 jet 的存在性/域覆盖与它们是否足够窄以供某个后续任务，是两件事。实际宽度只在运行后报告；本接口不填 $10^{-6}$ 已达标，也不把一次粗包围说成任意精度的收敛 oracle。

临时 `cut-twojet-readout.json` 的核心字段如下：

| 字段 | 精确含义 |
| --- | --- |
| `actual_source_result` | 同次原 v3 result 完整 bytes/SHA |
| `actual_original_config` / `actual_original_query_recipe` | 两原输入及 decoded 身份 |
| `actual_input_binding` / `actual_query_results` | 原文件完整描述器 |
| `complete_original_query_leaf_stream` | 原全叶流 file/bytes/rows/SHA |
| `original_binary_cut` | 原 key、little-endian word、精确有理数、未重归一标志 |
| `actual_point_query` | 原 query 小记录完整复制 |
| `point_twojet_enclosure_complete` | 上述完整源与点域责任 |
| `same_point_E_Er_Err_enclosures` | 三个精确 hull 及各 exact_full_width，或 null |
| `selected_leaf_span` / `selected_original_leaf_count` / `selected_leaf_kind_counts` | 原点叶跨度、数量及类型计数 |
| `original_natural_outer_radius` 及差值记录 | 原真实自然半径，非 cut 重标 |
| `original_all_query_*` / `original_error` / `original_unvisited_query_suffix` | 全请求责任保留 |

报告还明确旧 finite selector/旧点导数未认证、没有 accepted field、没有相对 metric 阈值、没有 cut DN 或有限头线性 transfer、原根族未选择。输出 schema 不自动支付这些责任。

## 10. Actions 顺序与预算

唯一 shared workflow 按如下实际依赖执行：

1. 原 11 件 source/三 proof/request/query/双 README pin 核与源码编译；
2. 原 config/两 ready 原 byte 恢复，核真实 binary cut；
3. 原公共 source subset 恢复一次；
4. 原规则 runner 包住同一个 f12f v3：完整有限头，点 cut 第一、whole-natural 第二；
5. token-free 独立两 jet 读回，逐完整叶流构造精确 hull；
6. 原字节/metadata scalar reader，完整保 result、两 query 与未付责任；
7. 无论成功/partial/工程失败，读回后仅清本 request144 自有临时目录；
8. report job 分别重现两个已绑定摘要，不再执行科学算术。

原科学参数逐字保持：

```text
deep_definition = original-exact-root-family
precision_bits = 256
integral_absolute_bits = 96
integral_relative_bits = 80
analytic_guard_bits = 8
integral_evaluation_limit = 100000
value_width_bits = 24
max_depth = 48
query_depth = 12
max_panels = 200000
max_query_nodes = 200000
budget_seconds = 1800
```

原 science step 45 分钟、compute job 65 分钟、report 5 分钟保持。新增读回 step 的工程 timeout 为 10 分钟，不延长原 1800 秒数学工作预算。Python 3.12.14 / python-flint 0.9.0、checkout/setup 的冻结 commit 均保持。

原 rules helper 2700 秒周期不改；原 helper 的来源 SHA 不改，只按原已付接线传入本次已审双 README baseline：root `21bd547f56590b7f2dd279d0297efb289a9b2783`，topic `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。只有规则同步父进程获得 token，数值子进程和新读回进程均去掉 token 环境变量。

## 11. 摘要、失败与保留范围

原 metadata scalar 块继续采用不含分隔 LF 的 compact UTF-8 bytes/SHA，标记为：

`BEGIN_REQUEST144_ACTUAL_CONTINUOUS_E_SCALAR_SUMMARY` / 对应 END。

独立两 jet 块采用新 source 的 canonical JSON（包含其末 LF）：

`BEGIN_REQUEST144_ORIGINAL_C_CUT_TWOJET_SUMMARY` / 对应 END。

两块各有独立 90000 B 上限、bytes、SHA 和 GITHUB_OUTPUT 字段；report 按各自 LF 约定验证后原样输出。两者不合并成一个被迫截断的结果；原所有点叶并未以 stdout 分段保存，大流只在 job 临时读取。

若摘要确实超界，记录该完整临时输出的 bytes/SHA 后报工程 70；不截叶、不删字段冒完成、不把它解释成原连续目标失败。若 producer 没有 result，或新读回工程失败，report 明示 unavailable，不以 job 前面的成功步骤猜测两 jet 成功。

严格区分：

- 源/点域 partial：可输出诚实 null jet 和未付原事实；
- 原合法粗包围：保留并报告宽度，不因 work-resolution false 删除；
- byte/schema/跨源身份不符：工程错误，不产生证书；
- 原 producer 错误或 rules stop：保持原返回及现场范围；
- 同次成功完整点读取：只能声称完整点两 jet 包围，不能扩成 accepted 场。

当前根 Rule15 下，完整积分/逆像叶及临时 input/readout 均在最后 owned cleanup 删除，不上传 raw artifact、Release 或 Git。发布仅 source、query/request、workflow、run/输出 SHA 和紧凑实际结论。若以后需要同一字面大结果，须以同一来源重新实际计算，不能说本次 raw 已在仓库保留。

## 12. 本地已做和未做

本地只读了公开 f12f 全源、原 139 request/workflow、真实 139/143 日志与已知原 config 文本；据此核字段、生成新源码/参数、做文本差异和文件 SHA。终端仍不可用，因此没有声称本地 AST/bash/YAML 工具已经执行；workflow 保留原 Actions AST 编译和全部身份核。

原 f12f 数学源码未改。源级比较确认原科学参数和三个输入完全相同，差异只有 query 顺序的明确增加、新独立读回入口及两个摘要的报告接线。完整 request/workflow/query 文本 diff 仅为本次审读临时资料，不作为可重算结果提交。

本次没有进行本地科学、没有启动 GitHub workflow、没有移动分支/ref、没有生成未来结果。实际 144 run 与点两 jet 数值范围由主控公开运行后再写正式结论。
