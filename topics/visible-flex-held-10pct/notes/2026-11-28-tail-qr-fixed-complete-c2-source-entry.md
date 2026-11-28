# 新 QR 固定度量两场的完整尾部 C² 比较来源入口

本条是**新来源合同和可执行入口**。本会话尚未有可供本入口使用的两个真实已接受 QR 固定度量场，因此本条不含新的 C² 数值上界、Cauchy 结论或完成验收。没有重跑旧 λ=.002 的 1152 段，未继承 R90 的数值。

## 修复的具体缺口

原 `resume_20261126/seam_compare_tail_c2_v2.py` 的实际源门只识别旧 warm fixed-metric 的两个 KIND，并要求 mean1168；它的切口高程入口是旧的连续真高度解释。新 QR anchor 与其 original-support fixed-g 后继有各自已发布的真实 schema、完整 physical-H 绑定和冻结的有限均值规则，不能改标签后送入旧门。

此外，原 `seam_run_tail_geometry_v2.Pipeline.complete` 合并 stage0 与其余真实逐段证书后，汇总的 `source` 是 pipeline；深 collar 证明的 `source` 仍是原 certifier。原比较器把这两者强制设为同一来源，会拒绝这个真实且已被原流水线支持的结果。新入口分别验证两个来源与它们的真实组件清单，不修改任何旧记录。

新文件为 `scripts/resume_20261128/tail/qr_fixed_complete_tail_c2.py`，SHA256 为 `d62f02658ed8c43e81e21d41b1603f250e182bd4a4993229de4520862d7edde2`。

## 同一个完整 g 和两场真实来源

右场必须由 `qr_fixed_actual_cartesian_prefix.accepted_fixed` 实际通过，保留 KIND `original_r53_literal_fixed_metric_qr_anchor_actual_dn_v1`。左场允许另一真正已接受的同 KIND 场，或右场完整 `fixed_problem.actual_anchor` 指向的真实 QR anchor；后者仍通过自己的 QR/native4/chord3/8outer 门，并必须提供该 anchor 的实际 coupling summary。

程序以已接受 anchor 的完整 raw、physical、最终 physical-H packet/binding、原 profile、原模型、literal radial chart、angular chart、core settings、q gauge、warp reference 和有限均值规则，调用原 `bootstrap` 与 `first_fixed_problem` **重新构造完整 literal 固定问题并要求逐字相等**。这一步是模型定义和输入验证，不调用 BVP、native flow 或新 Jacobian。两条 own fixed 链也必须具有逐字相同的完整 `fixed_problem`。

每场分别验证实际 baseline、runtime、port、native manifest、完整 packet 和原接受门。runtime 只剔除原来允许的执行键；两场 baseline 仅允许完整 `modes/quadrature/steps` 的数值分辨率不同。port 的 `config_sha256` 必须绑定各自真实 baseline。没有把一个场的 baseline 或 raw-H 当成另一个场的输入。

## 完整有限尾和精确比较

新类只改写来源初始化与身份输出，直接继承原 `CompleteTail.stage`、`CompleteTail.spans`。以下数学函数直接调用原已冻结实现：完整共半径细分 `common_spans`、完整傅里叶比较 `compare_span`、quintic Hermite、限制多项式、精确 Bernstein 上界与向外平方根。

因此比较会消费两边全部真实 finite stages、各自深 collar 和中心盘，建立两场所有真实节点的精确有理共同半径分割；所有平面和高度模取全集并集。每个 stage 的完整谱、原全 mean 链、共享两阶 jet、源数据 SHA、证明投影与完整 span 库存仍由旧严谨方法逐项检查。两场 native 完整 state 与真正最终 physical-H 相符，并各自绑定自己的 runtime 与 manifest。

直接 certifier 汇总与原 pipeline 的完整合并汇总有明确不同的合法分支。合并分支核真实两个组件、stage0 原样复用、无重复的全部 stage、相同定义、同一深 collar；不会重签汇总来源。原 metric 或 K<10 分配门为 false 的事实仍输出为 false，C² 有限图比较不伪称那些门已通过。

两场 true background 的 parameters、cells、checkpoint 和 factory 必须完全相同，且两个完整 tail 的 literal cut radius 都必须等于各自物理 rCut，才能按原公式精确消去背景。若这些条件不同则拒绝，不把旧 radius=Rc 的观察带入新场。

## 绝对切口高度

两边分别提供真正 source-bound continuous tables 的 summary。程序使用各自 `FixedActualContext.require_report` 或 anchor 的 `CoupledContext.require_report`，检查实际表来源、所有绑定源码、完整 `exact-defining-jets.npz`、全部模和零模唯一性、actual physical endpoint、完整 core lift 与角图在 cut 的零两阶 jet。

新有限图的 `Z_cut` 定义为这些原始 binary64 defining jets 中 cut 的零 Fourier 模；转成 `Fraction.from_float` 后是该有限图的**精确常数**，不是把 query 采样高度当精确值。完整尾的 `mu_cut` 则从真实全链取值。程序付的是

$$
\Delta Z_{\rm cut}+\Delta\mu_{\rm cut}-\Delta\mu(R,\theta),
$$

并精确消去同一个 true background。没有把各段均值清零，没有平移对齐、取中点对齐或漏掉位置项。由此可给该两幅有限尾图的绝对 C⁰、Cartesian 一阶和二阶上界。cut 修补前缀、中心柱和 marker 的差不在该 tail baseline 的比较范围内，完整闭图仍须分别拼合它们的实际证明。

## 已执行检查与限制

新源 `py_compile` 和 `--help` 均真实 exit0。额外源码核验确认：新类没有覆写原 stage/spans；从 `maxima` 初始化至共同分割完全消费及向外平方根的 2242 字节循环与原比较器逐字相同。检查记录为 scratch `held10-tail-preparation/qr-fixed-complete-tail-c2-entry-check-20261128/summary.json`，SHA256 `c14f3bc11c13608051ac836542750c68805358b15d3989aceeae674f6a68305f`；同名小 JSON 随本 note 保存实际记录。

没有伪造阳性 pair，没有执行数值 C² 比较。一个真实 finite pair 的上界也不会自动成为 Cauchy 序列证明；后续 source 连续投影误差同样不能设为零。

## 真输入返回后的命令

```bash
python topics/visible-flex-held-10pct/scripts/resume_20261128/tail/qr_fixed_complete_tail_c2.py \
  --left-source-run "$ACTUAL_ANCHOR_RUN" \
  --left-coupling-summary "$ACTUAL_ANCHOR_COUPLING_SUMMARY" \
  --right-source-run "$ACTUAL_FIXED_RUN" \
  --left-tail-certificate "$ACTUAL_ANCHOR_COMPLETE_TAIL_CERTIFICATE" \
  --right-tail-certificate "$ACTUAL_FIXED_COMPLETE_TAIL_CERTIFICATE" \
  --left-prefix-tables "$ACTUAL_ANCHOR_PREFIX_TABLE_SUMMARY" \
  --right-prefix-tables "$ACTUAL_FIXED_PREFIX_TABLE_SUMMARY" \
  --outdir "$NEW_SCRATCH_PAIR_DIRECTORY"
```

own fixed→own fixed 时省略 `--left-coupling-summary`；两边必须都是同一个真正完整固定问题的实际已接受结果。所有科学数组与完整 span receipts 仍只在 scratch。
