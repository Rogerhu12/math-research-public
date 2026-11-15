# Request156：同一连续 C 完整有限头重试的执行接口

作者：geometry agent（AI）。日期：2026-11-15。状态：只有可执行接线与来源合同；未运行本请求，不预填新 run、结果 SHA、cut 非零分母或完整 DN。

## 1. 本次唯一科学预算变化

本请求从已发表 Request148 的完整接线派生。使用完全相同的 R306 v3 连续 C 源、R312 全 112 模态深端源、R324 两坐标有限头源和原点 cut 两 jet 读者；13 个 source pins 原字节不变。唯一原数值工作预算变化是：

| 项 | Request148 | Request156 |
|---|---:|---:|
| 上游 v3 完整头和闭查询 `budget_seconds` | 1800 | 3600 |
| 上游科学 step 外层时间上限 | 45 min | 75 min |
| compute job 外层上限 | 110 min | 150 min |
| R324 线性传播 `budget_seconds` | 1800 | 1800 |
| R324 线性 step 外层上限 | 35 min | 35 min |

其余 C 精度、六 primitive、1440 个原片、所有根族、query 顺序、原 closed endpoints、200000 panel / 200000 query node 上限、最大深度、值宽工作目标以及 R324 各参数完全保留。该改变是公开声明的上游工作预算重试，不是目标模型改变，也不是放宽数学包含或非共振条件。

原 `public-stored-C-finite-head-request.json` 及工作流保持不动。新 trigger 唯一为：

`topics/visible-flex-larger-amplitude/computations/public-stored-C-finite-head-retry-request.json`

新工作流为 `.github/workflows/visible-larger-public-stored-C-finite-head-retry.yml`，独立 concurrency group `visible-larger-public-stored-C-finite-head-retry`，`cancel-in-progress: false`。请求号 156，lane `storedCfiniteheadretry`。不会推送或修改其他请求以触发本次。

## 2. 实际 148 依据与本次未付范围

真实 Request148：source `da307af38f4c9ae29fdb650603342da53a181060`，run `43719446020`，compute job `132828030323`，report job `132836205506`。原 C result SHA：

`50572f01210e23a5e37b17f43206afa6f48676e2c78bb40ddf22594e95cf84b7`。

其原结果完成 1432/1440 个 source pieces；piece 1432 的当前闭区间及完整 pending stack 与未访 `[1433,1440)` 后缀均已保存于实际报告。完整 cut cover 和自然 $R_{\rm out}$ 当次未付，R324 因实际前置未付，没有启动任何模态传播、panel 或系数求值。独立深端步骤已给全 112 个深尾线性图。这些不是当前请求的输入数组或新的运行结果。

本次重新生成三原输入对应的完整 C 输出、全部原闭 cut 查询与深端列，然后把同一新 job 的实际 result SHA 传入 R324。不会从 144 的旧 cut 盒、143 的旧深端值、148 的已完成前缀、旧 finite tail、旧 J 或任何已接受场复制数值作为当前输出。旧实际结果仅说明本次为何显式扩大上游 wall budget。重试仍可能 partial；不承诺 3600 秒内完整，也不由“多给时间”推出任何数学责任已付。

原完整结论见 [R327](../results/R327-actual148-incomplete-C-head-and-unstarted-cut-transfer.md)，有限头数学合同见 [R324](../results/R324-continuous-C-finite-head-flux-and-closed-tube.md)。

## 3. 为什么无需修改固定 binder

冻结 R324 源的 `original_core(binding)` 仅在比较 C 数学对象时排除：

`{"query_input", "runtime", "work_parameters"}`。

`bind_inputs` 仍逐字核：

- 同一 run、source commit、repository 和两个实际生产源；
- 完整原 C input binding，除上述明确的工作/查询字段；
- R286 声明 C、原 exact root family、原参数与原三输入；
- R312 far port 159 / physical node 160 / 完整 112 模态；
- 当前 cut plan、当前 result / manifest / 全 ledger descriptors；
- 原 R324 / R312 证明及完整源码身份。

源中没有 `cover.work_parameters.budget_seconds == 1800` 这种锁。CLI 线性 `--budget-seconds` 只控制新的线性 phase，其本次实际值继续为 1800。工作参数仍完整进入当前原 result 与 binding；把它从“数学对象相同”比较排除，不会把真实 3600 记成 1800。

Request 中保留 `execution.original_v3_work_budget_seconds=1800` 作为旧依据，同时新增 `current_v3_work_budget_seconds=3600`。原“全部工作预算不变”标记已明确设为 false，而不是保留错误标签。workflow preflight 明确核新上游预算、75/150 外层上限和线性 1800。

## 4. 完整冻结科学来源

以下 13 件与 Request148 一项不变：

| 文件 | SHA-256 |
|---|---|
| `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_stored_continuous_E_cover_v2.py` | `004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea` |
| `geometry_20261115_stored_continuous_E_cover.py` | `9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed` |
| `tail_frozen_geometry.mjs` | `db6664fcd7be618d2b684c39c01c53d97833d11e14af206b12c71e4b058713e3` |
| `strong_frozen_calibration_factory.mjs` | `77e9d2fc0e277ef69c9a4300ceba2d3d6b03056fc6a4868fab049a1a1c290247` |
| `closure_bounded_point_cache.mjs` | `35289a4de44ec409bc211f82c7a1bee81a10c6bc1c5fb31e4ca9a8634cc09043` |
| `exact_20261114_closed_background.mjs` | `be358bf780c88ebd85cdf07d9e8d2cc3b37ca20a4d8ea3a1ba69e7c40c2c4e1b` |
| `exact_20261114_public_resume.py` | `11399783f01b145ee3f23d88213af368daee9c16dfb858b40dd7316870b300a5` |
| `source-dependencies.json` | `7de25376ab0ec10277840ccdca8ec6b46b41bee6add97acd9d38c06bbc8cd941` |
| `root_20261114_current576_rules_runner.py` | `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde` |
| `geometry_20261115_stored_C_v3_cut_twojet_readout.py` | `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed` |
| `geometry_20261115_stored_continuous_C_far_graph.py` | `fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a` |
| `geometry_20261115_stored_C_finite_head_flux.py` | `4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d` |

R324 源：

`geometry_20261115_stored_C_finite_head_flux.py`，58317 B，`4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d`。

R306 v3 源：

`geometry_20261115_stored_continuous_E_cover_v3.py`，`f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df`。

R312 深端源：

`geometry_20261115_stored_continuous_C_far_graph.py`，`fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a`。

原 source restore 仍只执行一次；不重建旧 scientific sources、不更改公式或以不同源码代替同 SHA。公共 source revision、全部公式文件 pin、三原输入历史 ref、13 源闭包以及五个原数学 proof pins 都由原 preflight 核实。

根 README 当前 blob `21bd547f56590b7f2dd279d0297efb289a9b2783`；题 README blob `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。规则同步 wrapper 保其冻结源，运行时显式绑定这两个当前原文 baseline，保 2700 秒真实 pull/rebase 与规则改变停止责任。Git 凭证只存在规则同步父进程，科学子进程移除 `GH_TOKEN/GITHUB_TOKEN/MR_TOKEN`。

## 5. 实际输入、query 与数值参数

三输入仍从公开历史 commit `8bd267107cc8710d371f3b62c02986655ac965b0` 取原 blob，逐 byte/size/SHA 核实；不修改 JSON 不换 target：

| 角色 | 原 bytes | SHA-256 |
|---|---:|---|
| config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| calibration_ledger | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| stored_reference | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

完整 query recipe `topics/visible-flex-larger-amplitude/computations/original-stored-continuous-E144-queries.json` / `4e59c69fae54045e100180e2d7576b848423a503394ff0b4dd87f6e219b7fd59` 保持原字节。第一项仍是 config 原 binary64 `rCut` 的闭点区间，第二项仍为整个原自然连续域；workflow 按原 64-bit word 绑定，不能把名义 0.3 或新的 $R_{\rm out}$ 重新归一化当 cut。

C 参数完整为：

```json
{
  "deep_definition": "original-exact-root-family",
  "precision_bits": 256,
  "integral_absolute_bits": 96,
  "integral_relative_bits": 80,
  "integral_evaluation_limit": 100000,
  "value_width_bits": 24,
  "max_depth": 48,
  "query_depth": 12,
  "max_panels": 200000,
  "max_query_nodes": 200000,
  "budget_seconds": 3600,
  "analytic_guard_bits": 8
}
```

R324 参数完整为：

```json
{
  "precision_bits": 256,
  "budget_seconds": 1800,
  "max_panels": 200000,
  "max_depth": 32,
  "local_defect_bits": 12,
  "panel_norm_limit": "1/2",
  "taylor_terms": 24,
  "max_geometry_cache_records": 65536
}
```

R312 仍 `far_port=159, precision_bits=256`；模式完整集合 $m=2,4,\ldots,224$。原 160×9 source 顺序、深端整根族、两坐标 $u,j=wk$、精确二幂 reframe、完整 Duhamel 初盒误差传播、所有 cut inverse leaves、未付分母及未启动模态的报告语义不变。若 cut 列可得但高度包含零，则保原未付分母；不得私自筛掉模态或改成数值商。

## 6. 步骤依赖、真实部分结果与退出

完整执行顺序：

1. 源、proof、规则、query、request 的静态身份核。
2. 三原输入恢复并核原 cut word；恢复原 public source 一次。
3. 原 R306 v3 连续头和闭 query，显式 3600 秒工作预算。
4. `always()` 原完整 point-cut leaf / 两 jet 读者。
5. 原 R312 全 112 深端生产器。
6. `always()` 原 R324 有限头程序；实际 C / far result SHA 在运行时计算，禁止预填。
7. 原 C compact 标量块、深端完整 row ledger 身份块、有限头所有 mode / pending ledger 身份块读回。
8. `always()` 删除本请求拥有的临时根。
9. report job 仅重复四个已核 bytes / SHA 的原摘要块，无新科学算术。

上游科学失败不取消 `always()` 的真实 partial 读取。R324 的前置未付退出与真正已启动传播后的资源/数学错误由原 source result 明确区分；若根本没有原结果，reader 只写 unavailable 与已有文件身份，不构造 paid 或 pending 的假记录。非零 step / job exit 不被 wrapper 改成科学 success，report success 也不覆盖 compute 的失败状态。

C 标量完整 current query 和未付作用域仍由原 reader 读；cut 块保持原读者 schema/marker `REQUEST144_ORIGINAL_C_CUT_TWOJET_SUMMARY`，不因为请求号改变重写它。其余当前工作流块改为 `REQUEST156_ACTUAL_CONTINUOUS_E_SCALAR_SUMMARY`、`REQUEST156_ACTUAL_DEEP_FAR_SUMMARY`、`REQUEST156_ACTUAL_FINITE_HEAD_SUMMARY`。每块原 90000 B 传输上限不变；若超过，只报告 size/hash 和未交付范围，不截 trial、leaf 或未付记录，不拆伪完整数学证书。

## 7. 临时 raw 生命周期

唯一 owned 根：

`$RUNNER_TEMP/visible-stored-C-finite-head156`。

其中有原三输入、恢复的原 source、三生产器输出、cut reader 暂件和各规则同步记录。完整原 raw 必须先由实际读者打开、核对应全文件 SHA / 行数，并输出四个原摘要与身份；随后末尾 `always()` cleanup 才可删除这一个命名根。不能先清理再读，也不触及其他 run 或 parent 的目录。

compute 的四个 `GITHUB_OUTPUT` 摘要由 report job 复印原 bytes；report 不再需要已删除的 raw。若 runner 被硬杀而未执行 cleanup，GitHub runner 生命周期负责临时存储销毁，不能伪称 cleanup 代码已经执行。正常 cleanup 失败单独记录，与科学 partial / complete 分开。

不 upload artifact、Release 或 Git raw，不持久化派生数据。正式保存的是三件接线/接口、参数、实际未来 run 和输出 SHA / 小结论。当前文档没有新实际结果，R331 的新 C 非线性 provider 仍是独立后续；完整线性 cut 列或数值 Robin 都不自动证明非线性无限尾 DN、完整 453/699 BVP、全局闭场或标准完成。

## 8. 相对 148 的完整差异边界

除请求身份、独立 trigger/concurrency/临时根、当前日志 schema/marker、显式旧 148 依据、本次预算披露与 workflow 的新 3600/75/150 核验外，原 steps、源/输入/proof pins、科学 CLI 字段、四 reader 算术与退出/清理顺序保持。R324 科学源一字未改。完整 JSON/YAML diff 仅存临时交接目录供主控读，不作为新科学证据或新门槛。

本地只源文本、JSON/YAML 结构、AST / bash 语法与哈希检查；没有导入任何数值源、运行 Arb / profile / RHS / J / ODE 或尝试新结果。
