# 真 λ=1 原 R53 设计 → 原 full DN / 8outer → 同源几何入口

2026-11-28 UTC。本条处理确定的来源接口缺口，不提供真 λ=1 数学输入。四个独立新源已通过实际语法编译；没有构造接受输入、重复负向测试、启动 BVP/尾或执行连续证书。旧 memo-only loader、旧图定义和旧来源记录均不改。

## 同一 runner 上已经可用的数值入口

`resume_20261126/continue_original_actual_dn_chord.py` 的 SHA 是 `7a1ce40d5141c08f4d76b2bc201f3113b04d02f12f60c06809a9053ba03321cc`，不是一个 Git commit。它已支持真正原 R53 λ=1、curvature_blend=1、完整 M≤64；其字面 mean 使用真 source 的 `max(audit-angular,16*(3*M+1))`，没有1168固定值或旧暖 phase KIND 前提。

在当前冻结 CI 数值树和保留全部 raw 的同一 `@WORK@` 中，令 `RUN` 为真正 λ=1 接受 run，`CONFIG` 为其 `--port` 对应 `tail-M{M}.json`，且文件 SHA 必须等于该 port 的 `source.config_sha256`。原 controller 把这两个文件放在同一目录；不重新编码出一个“近似同配置”。随后调用：

```bash
python -u @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261126/continue_original_actual_dn_chord.py \
  --repo @REPO@ --work @WORK@ \
  --source-run RUN --tail-config CONFIG \
  --streamed-rhs-block 8 \
  --outdir @WORK@/lambda-one-actual-dn-01
```

它从真正 raw 全量重启，保 source profile/chart/core/settings/gauge/mean/全部模式，配置真 M 的 native4，保 chord3、完整 H/J/audit 与原八次 outer 门。δ 与 support 控制仍为设计未知数，不能称固定 g 精化。默认 warm 因子为 `.25,.5,.75,.9`，之后必做完整未缩 H。该命令并不会自动退回低 λ 或重生已存在的低 λ 输入。当前 CI worker v3 在数值链结束后保留同一冻结树与 work，新唯一 request id 可继续执行这个已存在 CLI。

不要误用 `couple_actual_prefix_memoized.py`：它为当前 M24/native-tail24 真 memo 包而设。`warm_actual_dn_refine_*` 的 v2/v3 KIND 与 mean1168 则属于另一明确未知族。两者都不能用改标签方式读本链。

## 新的诚实 7a 返回读取门

`analytic/chord_actual_coupled_prefix.py` 只认上述7a源的实际 successful summary、真实 child0、原 actual/finite 门以及该条求解的 `prefix-execution.json`。direct 与原 streamed 两种执行分别按自己的真实 argv/sidecar 核对。新门还复核 native4 manifest/owned sources、原 baseline 与 runtime/chord3、真实设计锚、原全部物理声明、完整 raw PPoly/pscale/RMS 与 physical 六jet，以及未缩完整 endpoint H/state/height-J/audit。

它使用7a真正的 `original_actual_gate_passed`、`prefix_execution` 和 `height-binding.original_run` 字段，不伪称 memo source 或添加不存在的 memo sidecar。H 的唯一最终定义是7a原 `seam_audit` 在实际 physical 端点请求的 `height-binding.candidate_H`；raw candidate 即使近似相等也不替代它。源和最终 physical 的 δ 可以因原设计 outer 改变，读取时由真正最终 flow/record 构造 g，不借原线性设计锚的 δ。

## 真实返回后的几何接线

假定上述新目录中真正 `summary.json` 全门通过，实际 run 为其 `actual/run.json`：

```bash
python -u @REPO@/topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/chord_coupled_prefix_continuous.py \
  preflight --coupling-summary @WORK@/lambda-one-actual-dn-01/summary.json \
  --source-run @WORK@/lambda-one-actual-dn-01/actual/run.json \
  --outdir @WORK@/lambda-one-actual-source-check
```

同一独立入口的 `geometry`、`tables`、`metric`、`cut` 阶段复用已审原区间代数，各阶段保原参数与门。`geometry/tables` 接实际 run；`metric/cut` 只接由本入口生成且绑定同一实际场的表/证书。每份输出传播 `source_kind=actual_lambda_one_chord_final_physical_height`、真实 coupling summary、最终 physical-H/packet、当前 physical SHA、字面 mean 与全部 adapter SHA；不继承其他场的 R73/R74/R76/R77 数值。

完整尾定义仍由原 `seam_run_tail_geometry_v2.py` 导出：`--tail-response` 取本次最终 physical packet，`--height-reference` 取本次 `height-binding.json`，`--height-reference-key candidate_H --warm-factor 1 --height-arithmetic numpy`，source-topic/native-record-dir 取本次7a真实 native-source/native-runs，source-port 取原实际 run 的完整 port。必须保全部 stage、全声明 Fourier 谱、共同 mean 和公共两jet；stage0 不代替完整 bundle。

`analytic/chord_complete_tail_radius_identity.py verify` 在真正完整 bundle 到位后核半径身份，并必须显式提供本条 coupling summary；它保原 normalization/全谱/完整源门。`analytic/chord_actual_closed_map.py` 用同一真实返回、完整尾和全 cut 公式读取整图，也必须提供 coupling summary。两者只改明确来源入口和新文件所在目录的导入路径；原图数学公式不变。未有真实完整数据时不得使用这些入口宣称新证书。

## 仍明确存在的执行边界

原7a数值入口当前支持 direct/SuperLU 或旧 streamed/SuperLU，没有自动接本次 mapped QR 资源链。实际若出现资源阻碍，应在原完整系统上另作诚实资源接线，不能改原门或丢列。M>64 还需全链 native/runtime 独立扩维，详见已登记 tail high-mode boundary audit；本入口保持该真实限制，不能截成64模。若首冻之后确需新代码，须明确新冻结 snapshot，同时保旧树及同runner全部实际场，不将销毁并重生当默认续接路径。
