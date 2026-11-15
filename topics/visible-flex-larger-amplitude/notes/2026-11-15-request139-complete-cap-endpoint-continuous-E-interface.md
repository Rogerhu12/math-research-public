# Request139：完整 cap 端点 primitive 与实际预算停止的独立 v3 接口

- 作者：AI
- 日期：2026-11-15 UTC
- 状态：source-only 实现及执行接线；没有本地科学计算，没有预填139的run、结果或成功。
- 数学全文：[R306](../results/R306-complete-cap-endpoint-primitives-and-budget-preserving-integration.md)。
- 真实依据：[R304](../results/R304-actual136-cap-callback-budget-and-unpaid-domain.md)。
- 目标仍为 [R286](../results/R286-original-stored-continuous-integral-and-metric-bridge.md) 的明确约定 C；[R297](../results/R297-continuous-E-unit-panel-and-piecewise-enclosure.md) 的单位面板包含与完整全宽要求不变。

## 1. 本次恰好改变什么

独立入口是 [geometry_20261115_stored_continuous_E_cover_v3.py](../computations/geometry_20261115_stored_continuous_E_cover_v3.py)，89307 B，SHA256：

`f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df`

它没有覆盖9aa0或0040源。启动时仍逐字核原9aa0，并新增逐字核其实际136前身0040。

第一项改进：在原 $\chi$ 恒为1、完整闭面板 $q=w_x$ 已证非负或非正时，使用完整 cap/flat/valley/cut 后 $w$ 的端点恒等式，求三项 $A,\sqrt E A,wA$ 的严格包围。源生成每端所有可能原分支的并集，然后与原实范围乘长度相交，按原全宽目标复核。whole-panel $q=0$ 可准确给这三项零；不是在一个点观察到零就认定整片恒零。

第二项改进：Acb callback 中确切捕获真正的 `ResourceStop(Exception)`，登记本次分量与原原因后转入 python-flint0.9.0支持的 `ValueError` 通道。外层只凭该实际登记恢复原异常，交已有pending收尾；没有登记的SystemError不被猜成预算停止。原全局异常继承与墙钟预算不改。

每一分量已有严格包围且达到原工作目标时，可以不重复调用Acb；所有六分量仍被保存并参与同一累计。这是复用已有完整包含，不是截掉分量。未达目标的分量保原Acb／真实范围fallback／细分，深度用尽仍明确保存有效粗界及工作精度未付。

## 2. 仍原样的数学对象与实现

源的以下整个定义经纯AST对比与0040完全相同：

- `Jet2`、`smooth`、`cap_primitive`；
- `Piece` 全类，包括原 raw/cap/valley/flat/cut 覆写顺序、weight、全部六实 integrands、径向导数和cap判定；
- `complex_cap_branches`、`branch_integrand_component`、`complete_integrand_component`；
- `ContinuousHead` 全类，包括160个原cell、每cell9段、全部深尾与protected join；
- `QueryCover` 全类、query解析、finite-join条件；
- `ResourceStop`、`WorkBudget`、CLI参数定义、原 `goal_met/goal_records`。

因此没有cap换raw，没有丢两个 $\chi$ 过渡，没有省去 $B,\sqrt E B,wB$，也没有因端点式而改写复解析callback规则。

源修改的既有函数恰为 `bind_inputs`、积分器初始化、`analytic_integrals`、`integrate`、`build_head`、`main`。新增 `complete_endpoint_functions` 与积分器 `endpoint_integrals`。完整diff提供所有新增／修改行，非数值对照结果。

输入约定C仍与原finite selector不同。没有48层selector树；没有复用R26的另一个数值证书；没有finite输出→连续模型的误差桥已通过声明。实际场、C零响应/J、非线性尾或同g metric都不是本请求的输入或输出。

## 3. 真实来源与运行依赖

| 项目 | Bytes | SHA256 |
|---|---:|---|
| 新v3源 | 89307 | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| 原v2源 | 77697 | `004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea` |
| 原初始producer | 66415 | `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed` |
| R286原模型证明 | 37491 | `81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb` |
| R297单位面板证明 | 15793 | `3505389d22bc63f6d7b5c7cde62e36e856d94993841fc7eb3cdd034ff92a10e0` |
| R306端点与余责证明 | 13875 | `6f3593306fa66098c73f2aaa12ca21788263c24eac6f31c881bb52308b601ea1` |

Python为3.12.14，python-flint固定0.9.0。没有导入新版数学源去本地尝试运行。实球 `atan` 的存在及语义已据 [官方0.9.0文档](https://python-flint.readthedocs.io/en/stable/arb.html)只读确认；callback的受支持异常集合据该tag原 `acb.pyx` 只读确认。

Workflow source pins共10个，原9个不删不换，只增加新v3。这10个包括4个原runtime模块、public resume、source-dependencies、规则runner及三个世代producer。原来源复原后仍核完整9个 formula source SHA，具体清单在request，未重新计算原ready。

规则runner仍原 `3b8b6dd5…`，2700秒同步周期；本请求只按本轮已读README字节显式替换runner的基线元数据，不改其真实pull/rebase、规则变化停止和原child状态传播逻辑。

本次基线：

- 根README Git blob `21bd547f56590b7f2dd279d0297efb289a9b2783`；
- 题README Git blob `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。

若发布前又有真实规则变更，由主控读原差异后更新本请求；这里不声称本地额外git pull。

## 4. 同三输入、同原query与同预算

仍从历史公开提交 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复原字节，不新归档raw：

| 输入 | Bytes | SHA256 |
|---|---:|---|
| T112 config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| calibration ready | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| stored ready | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |
| 原132闭query recipe | 782 | `4fa2baa15518ee5045d4a21305ff3f727ef594f966e8a95f9bc6f89eaac3b979` |

原完整查询仍是从真实cuff至由全部primitive确定的自然 $R_{\rm out}$。没有名义cut补平，没有把前缀半径标成自然外半径。全部160×9有限pieces与所有 $n\ge160$ 的准确根族责任保留，根值未被虚构或数值选出。

原科学参数逐dict保留：

```json
{
  "deep_definition": "original-exact-root-family",
  "precision_bits": 256,
  "integral_absolute_bits": 96,
  "integral_relative_bits": 80,
  "analytic_guard_bits": 8,
  "integral_evaluation_limit": 100000,
  "value_width_bits": 24,
  "max_depth": 48,
  "query_depth": 12,
  "max_panels": 200000,
  "max_query_nodes": 200000,
  "budget_seconds": 1800
}
```

外部science step45分钟、compute job65分钟、report job5分钟都沿136。没有用时间扩张代替算法改进。

## 5. CLI与身份

CLI参数名与136完全相同：

```text
python geometry_20261115_stored_continuous_E_cover_v3.py
  --config ACTUAL_CONFIG --config-sha256 01930f3b...
  --ledger-ready ACTUAL_CALIBRATION --ledger-ready-sha256 563a9997...
  --stored-ready ACTUAL_STORED --stored-ready-sha256 c1c44f23...
  --runtime-computations CHECKED_COMPUTATIONS
  --source-topic RESTORED_ORIGINAL_SOURCE_TOPIC
  --proof ACTUAL_R286_PROOF
  --queries original-stored-continuous-E132-queries.json
  --queries-sha256 4fa2baa1...
  --out FRESH_REQUEST_OWNED_DIRECTORY
  [完整request中的原预算／精度参数]
```

上例短SHA只用于显示，workflow与request传完整64位SHA。原R286 proof由source自己核；R297与R306完整字节在workflow核并绑定request。科学child清除GH_TOKEN/GITHUB_TOKEN/MR_TOKEN，只有原规则同步父进程有认证环境。

独立输出schema为 `R286-original-stored-convention-C-continuous-E-cover-v3`。query-plan和目标model schema保持原定义；新的producer身份不可冒旧9aa0或0040。未来消费v3的连续E若需要扩展已有metric严格schema，必须显式接新来源，不能重标旧producer。

`input-binding.json`新增：

- `preserved_unit_panel_producer_source`：原0040完整receipt；
- `integral_strategy`：`R306-complete-cap-endpoints-and-supported-budget-transport-v3`；
- `complete_cap_not_replaced_by_raw`；
- `endpoint_rule_requires_whole_closed_panel_derivative_sign`；
- `callback_resource_stop_requires_actual_captured_exception`。

这三个布尔声明描述新实现责任，不是预造实际运行结果。

## 6. 原端点与组件记录

每次尝试端点规则记录：

- `chi_identically_one_from_original_piece`、完整 `entire_closed_panel_w_derivative` 和 `proved_sign`；
- 适用分量固定为0、2、4；
- 每端准确有理参数、所有可能原cap分支和完整w球；
- 端点积分的严格球；
- 原range交集与各项原full-width goal；
- 若值域无法证明，记录失败原因并保原完整求积。

整面板导数准确零时，原完整range本身已证明三项为零，无需另算端点；记录 `derivative_identically_zero_on_entire_panel`。这不触发此前136已修掉的“点零即复解析”错误，原 `real_abs(analytic=...)` 源完全未变。

`actual_component_attempts`保每项是已有完整包围达标、真实Acb成功，还是回退既有独立有效范围。如果Acb返回范围与已有范围不能相交，显式记录收紧失败；不把空交称成功。没有“成功前几个分量就省略后几个”的返回路径。

新诊断统计包括端点规则尝试／同号未证／χ过渡保留／实际cross-cap启用／三项包围达标、已有完整目标使Acb跳过的分量数，以及实际捕获／恢复的callback预算停止。所有具体数值等实际139产生，不在本接口预填。

## 7. 资源停止和partial字段

在Acb callback内部真正出现ResourceStop时，`last_actual_callback_resource_stop`保存原类型、message、piece/cell/segment、分量、精确闭参数区间、当时analytic要求及专用ValueError传输标识。它明确 `inferred_from_elapsed_or_SystemError=false`。

正常恢复后的资源停止沿原DFS收尾：

- 已付的完整pieces计数真实返回；
- 当前piece全部pending闭面板保存在temporary unpaid ledger并在partial receipt列出；
- 当前piece之后的完整原后缀由原source-piece index定位；
- 已接受面板的六项累计及前缀径向端点单列；
- 请求的完整闭query仍访问或明确给whole-query／unvisited suffix未付记录。

新 `partial_finite_head_prefix`字段仅在源已有正常partial返回而未完整时出现，包含：

```text
complete_original_pieces
accepted_panel_count
all_six_integrals_over_only_accepted_prefix
prefix_radial_endpoint
current_incomplete_piece
unvisited_whole_piece_suffix
complete_finite_head_or_natural_Rout_not_claimed = true
```

`current_incomplete_piece`保原piece/cell/segment、accepted参数前缀、全部pending参数面板及这个piece的已付六项累计。完整的 `finite_head_all_six_primitives`、`full_deep_plus_head_all_six_primitives` 和 `natural_outer_radius`仍只在原完整条件满足时出现。

未知SystemError等仍保原generic failure；没有登记的异常不被转成正常预算退出。此时有可能仍只有保守whole未付范围，本接口不承诺从任意未知故障恢复未返回对象。已知受控partial可能进程exit0，但其query/model/work-resolution原flags仍明示；job成功不是完整连续E或BVP成功。

## 8. 唯一workflow与raw生命周期

继续同一个workflow路径：

` .github/workflows/visible-larger-public-stored-continuous-E.yml `

仅push本题 `computations/public-original-stored-continuous-E-request.json`触发，原同一concurrency、`cancel-in-progress:false`不变。没有另外并发重复原136。

流水线按原顺序：

1. sparse取源／证明，核10源及完整query／规则基线；
2. 恢复真实三输入及原公共源；
3. rules-runner包住无token数值child；
4. always原值readout，完整result/query／unpaid统计和后缀入≤90000B摘要；
5. always只删本139自己namespace内的temporary输入、源副本、raw ledgers；
6. 独立report只校验并输出原bounded JSON和bytes/SHA。

不上传artifact、Release、raw Git数据。readout不重算primitive或误差；若摘要真的超限，它保明确bytes/SHA并以工程失败停止，不截字段冒完整。主控后续阅读真实结果与必要原日志；失败和未付都不是几何否证。

## 9. 静态范围与交付清单

源级检查只做文本／AST／哈希。原数学定义完整对照已通过；10个实际源码SHA已核；9段bash做 `bash -n`，7段内嵌Python做AST解析；原三输入、原query、原预算dict逐值相同。没有导入flint或任何科学模块，没有执行endpoint函数、原ready构造器或任何积分。

交付草稿全部在 `/tmp/continuous-E-endpoints139/`：

| 文件 | Bytes | SHA256 |
|---|---:|---|
| v3 source | 89307 | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| 相对0040完整source diff | 24739 | `a0ca998d1d58756fa028c20019a5dcdcdffec0d656067fa84bcbccb740741508` |
| 原request路径的新139内容 | 9854 | `3c210929e574d912014ed47f5ca7b09e14139f920d3fe7f8e1747d5e8fde9257` |
| 原workflow路径的新139内容 | 21202 | `1e93333abb1979a063cdc1d88159333b3f36a9169aa6161416b2a4c47f3bdf3d` |
| request完整diff | 5747 | `ea2f2aa39471fe9e1d2f704965a8ae93e82ac3eaf0371930264b2848b17e9765` |
| workflow完整diff | 13979 | `91f3c2920e55f6423045aa6fe16cc92c601c390b30bfac892fccb1a9561464ca` |
| request139-static-check.json | 2282 | `69b50345ae11c130cf13f4577f60ed684c19466c6e483cf298333331bbb942e3` |

临时build／check脚本只用于生成和解析源码，不是科学入口。主控统一实际发布与dispatch；本交付不包含任何API/Git修改，也不预选未来field或阈值结果。
