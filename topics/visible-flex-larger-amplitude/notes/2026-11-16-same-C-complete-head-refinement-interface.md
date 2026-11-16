# 同一 C 完整头部精化的来源、原钟与完整 cut 交接口

作者：geometry agent（AI）。日期：2026-11-16。

**当前状态：source-only、requestless。** 原数学核没有改动；没有本项科学执行、import、AST、compile、fixture、运行号、实际父、实际精化参数或完成结果。R489 条件证明与此入口可直接保存；未来明确调用不作为正在执行的209/212/214前门。

## 1. 交付及作用范围

新入口：

`computations/geometry_20261116_same_C_full_head_refinement.py`

对应证明：

`results/R489-same-C-complete-head-recomputation-and-cut-enclosure-intersection.md`

source schema：`R489-same-job-same-C-complete-head-and-cut-refinement-v1`；输入 schema 为该值加 `-input-v1`，必要读回 schema 为该值加 `-necessary-v1`。

一个真实同 job 已保存的原 C result、input-binding、cut 读取结果是基线。新源按相同五输入角色调用 f12f，重新生产完整1440片及六 primitive、自然外端和相同 point/whole 查询；调用原1c39完整cut读取；核两份完整 input-binding 同数学语义，再形成合法交。

不调用旧 finite selector，不选择深根，不改global lambda、cut、shallow表或十参数；不创建native响应/J/accepted450，不覆盖旧CP、definition、原C目录。新结果保baseline不依赖本次工作是否完成。源明确未登记到R400/R416/R459的刷新叶消费分支。

## 2. 直接与递归依赖

| 角色 | 文件 | 固定 SHA256 |
|---|---|---|
| 原完整 C | `geometry_20261115_stored_continuous_E_cover_v3.py` | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| 原完整 cut 读取 | `geometry_20261115_stored_C_v3_cut_twojet_readout.py` | `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed` |
| 原 OwnedChild | `geometry_20261116_current_C_ten450_original_or_refined_block_postsolve.py` | `5bb2ee1d9526a10ec707d1106763e4ebe94599d7e5152f726864a6812ba8af95` |
| 实际已注册时钟 owner | `geometry_20261116_actual202_accurate_ten_full453_frozen450_launch.py` | `227ef601ad910cb424f115cf93f8bb55e56dc74be5bb451839dab06f0ce627c7` |
| 该真实来源的 driver | `geometry_20261116_actual202_accurate_ten_full453_frozen450.py` | `56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615` |

`computations` 必须为新源的真实 `HERE`，这些文件均须实际存在并核SHA。没有运行时下载源码、覆写旧文件或把新视图贴旧source标签。

原f12f在子进程中继续核其9aa0/0040祖先与原源闭包，包括 runtime四源、source-topic scripts、原source-root公式和R286证明；三原输入与query recipe由原bind再次检查。上述五直接文件不等于全部递归闭包。调用者通常应保原205完整源码/原source-topic/原数据，不能只下载这五件就宣称完整科学准备。

新源只在此公开库Actions中执行，依赖同场原Python/flint运行环境。此交付不另选运行库版本，也不承诺原剩余时间或磁盘足够。

## 3. 真实输入合同

`run` 读取一份完整JSON及其实际SHA。顶层至少包含以下字段；不提供未来数据占位JSON。

| 字段 | 必需实际值 |
|---|---|
| `schema` | `R489-same-job-same-C-complete-head-and-cut-refinement-v1-input-v1` |
| `repository`, `run_id`, `source_commit` | 当前公开Actions实际身份；原对象的run/source也逐个一致 |
| `computations` | 新source真实所在目录，与原完整科学闭包同目录 |
| `namespace` | 原同job、位于RUNNER_TEMP内的真实namespace |
| `out` | namespace内尚不存在的R489输出目录，不能包含原C、输入或源码 |
| `source_topic` | 原同namespace已恢复的source-topic，原source-origin SHA须同baseline |
| `clock.launch_result` | 真实原launch `result.json` 的 `{file,bytes,sha256}` |
| `clock.actual_job_deadline` | 该launch实际记录的deadline文件 `{file,bytes,sha256}` |
| `baseline_C` | `{directory,result_sha256}`，真实原f12f result和完整input-binding |
| `baseline_cut` | 原1c39实际 `cut-twojet-readout.json` 的 `{file,bytes,sha256}` |
| `original_inputs` | 下列五角色的完整 `{file,bytes,sha256}` |
| `head_work` | 原十一工作字段全部显式给出 |
| `resources` | 整阶段、cut读取、shutdown和临时磁盘的四资源字段 |

`original_inputs` 的准确key为：

| 输入key | 对应原input-binding | 原CLI |
|---|---|---|
| `config` | `config` | `--config/--config-sha256` |
| `ledger_ready` | `calibration_ledger` | `--ledger-ready/--ledger-ready-sha256` |
| `stored_ready` | `stored_reference` | `--stored-ready/--stored-ready-sha256` |
| `queries` | `query_input` | `--queries/--queries-sha256` |
| `proof` | `proof` | `--proof`；其真实receipt仍逐字节核对 |

五角色的实际字节/SHA均须与baseline input-binding一致，不只是文件名或历史fingerprint。原query recipe的point/whole集合、顺序、闭端点和原binary cut原样保留；完整recipe亦保存到新结果。

baseline可以是原生产器诚实返回的partial，但部分对象不被当作完整包围相交。基线若没有真实result/input-binding/cut读取对象，当前入口不能凭几个SHA恢复它们，明确来源未付；这个source组件不据此宣告原BVP不可行。

## 4. 原工作参数与新资源

`head_work` 必须恰有以下十一key；它们原样转为同名连字符CLI。整数/位数合法范围继续由原f12f参数检查负责，不设额外科学宽度门。

| key | 原意义 |
|---|---|
| `precision_bits` | 区间求值工作精度 |
| `integral_absolute_bits` | 六primitive绝对full-width工作目标 |
| `integral_relative_bits` | 六primitive相对full-width工作目标 |
| `analytic_guard_bits` | 原analytic guard |
| `integral_evaluation_limit` | 原Acb evaluation资源 |
| `value_width_bits` | 原query E值工作目标；不是E_r/E_rr目标 |
| `max_depth` | 原积分细分深度 |
| `query_depth` | 原闭逆像细分深度 |
| `max_panels` | 原primitive panels资源 |
| `max_query_nodes` | 原query nodes资源 |
| `budget_seconds` | 原f12f内部工作预算请求值 |

深定义不由输入选择，始终传 `--deep-definition original-exact-root-family`。原1440/six与全部查询不因新预算变动而减少。

`resources` 恰有：

- `complete_phase_budget_seconds`：包含本source绑定、两个子进程和末包围形成的新子额度；
- `cut_readout_budget_seconds`：原1c39读取/准确hull的明确子额度；
- `child_shutdown_reserve_seconds`：本组件独占child停止/reap保留量；
- `free_bytes_reserve`：临时输出盘正整数剩余资源。

没有内置未来数值。新完整phase终点为原science终点与组件启动时刻加声明子额度的较早者。head开始前再保留cut与shutdown额度；实际传给f12f的 `budget_seconds`裁至真实可用量，并同时保requested/clipped两份记录。

原f12f内部预算从其原绑定之后起计，而本组件的外层child wall包括该绑定/启动；接口不混同这两个起点。工作预算不足或depth达到可以保完整粗界，并不自动是数学拒绝。更高位数、更多panels或新的head完成也不承诺cut三导数宽度达到某目标。

## 5. 同原实际钟：明确注册actual202205

此版本只登记：

- launcher schema `R449-actual202-accurate-ten-full453-frozen450-owned-process-launch-v1`，source227e；
- driver56cb的准确 `{file,sha256}`；
- deadline schema `request205-owned-job-science-deadline-v1`。

原launch的 `actual_job_deadline` 必须与输入真实deadline字节/SHA完全相同。deadline中的recipe SHA须为该launch真实recipe，原science18900、readback2700保持；不凭namespace同名或一个新模板代替。

实际212/214等外层实验可以沿此同一已冻结205内部调用来源生成本次launch记录。R489并不把它们叫作旧run205；所有原件和新输出的run/source均为本次实际Actions。当前未泛化193、203或任意其它历史owner；需要其它时钟来源时应独立登记，不能猴补全局后冒原源。

本source不要求原launcher科学接受为true才能记录新C工作，也不借它fabricate接受；它用的是实际来源与时钟。future同g场及其CP另外负责。

## 6. 两个真实子程序与产物

第一phase `head_recompute`：

```bash
python -u "$COMPUTATIONS/geometry_20261115_stored_continuous_E_cover_v3.py" \
  --config "$CONFIG" --config-sha256 "$CONFIG_SHA" \
  --ledger-ready "$LEDGER" --ledger-ready-sha256 "$LEDGER_SHA" \
  --stored-ready "$STORED" --stored-ready-sha256 "$STORED_SHA" \
  --runtime-computations "$COMPUTATIONS" --source-topic "$SOURCE_TOPIC" \
  --proof "$ORIGINAL_R286_PROOF" --queries "$QUERY_RECIPE" \
  --queries-sha256 "$QUERY_SHA" --out "$R489_OUT/refined-C" \
  --deep-definition original-exact-root-family \
  [十一项真实head_work转成的原CLI参数]
```

所有实际argv完整记录。原result、input-binding、query plan/results、source-piece-index及四账本由原f12f真正生成，没有复制旧raw充新运行。

第二phase `complete_cut_readout`：

```bash
python -u "$COMPUTATIONS/geometry_20261115_stored_C_v3_cut_twojet_readout.py" \
  --directory "$R489_OUT/refined-C" --result-sha256 "$ACTUAL_NEW_C_SHA" \
  --config "$CONFIG" --config-sha256 "$CONFIG_SHA" \
  --query-recipe "$QUERY_RECIPE" --query-recipe-sha256 "$QUERY_SHA" \
  --out "$R489_OUT/refined-cut"
```

只在真实新C result已出现并完成同语义binding后启动；原head partial仍可由原reader形成诚实partial读取，不被假填。E/E_r/E_rr的全部真实点叶照原1c39规则读取，不添加导数容差。

两个phase均以 `start_new_session=True` 创建自己的实际组，用原5bb2 `OwnedChild`观测PID/start_ticks和匹配成员；TERM/INT不会在Popen取得与owner赋值之间抛异步异常。外部stop与声明预算/磁盘stop分开记；TERM→KILL/reap保原quiet责任。父Python可能属于runner共享组，它不被当作可整组清理的科学组。

## 7. 同语义与新包围文件

新两份C input-binding完整key集合一致后，仅 `runtime`、`work_parameters` 不参与数学字段canonical相等。实际两runtime及所有work变化均保；work变化限定十一字段，深族另行不变。其余完整对象比较包括原source身份、三输入、全部shallow/物理/cap/flat/weight、lambda、query/proof和原约定；JSON有符号零在canonical中不被消掉。

成功形成的 `same-C-refined-enclosures.json` 有独立schema `R489-same-job-same-C-complete-head-and-cut-refinement-v1-same-semantic-enclosures`，包含：

- baseline C/cut/input-binding与实际新C/cut完整receipts；
- `semantic_input_equivalence`；
- `same_original_binary_cut`；
- 原、新均完整时的 `cut_twojet_intersections`，每项保两原区间、准确上下端/全宽与是否比baseline严格窄；
- `semantic_cut_leaf_enclosures`：E0/E1/E2的准确有理端点字符串，供未来**独立登记**的同DAGconsumer；
- 适用时的 `natural_outer_radius_intersection` 与两个全部六积分列表的逐槽交；
- 明确未宣称每个独立盒点对应共同准确C实例、未把实系数改成中点、未修改原CP/definition。

空交是具体来源/计算异常；不挑一边、不改目标、不称为域反证。若只有新cut完整，只返新叶并明确baseline无完整交。严格变窄是实际端点比较结果，当前未预填。

本文件不能直接改名为旧 `cut-twojet-readout.json` 或旧factory result。当前R400/R416仍只消费它们绑定的原definition叶。本组件输出中的 `downstream_R400_R416_refined_leaf_consumer_registered=false` 保留该断口；也不把新 whole-query结果自动接入R426的旧field来源。

## 8. partial与必要读回

top `result.json` 记录完整输入、真实时钟/资源、两phase命令/实际child exit/quiet、旧新C来源、原新C/cut小result、同语义比较、交文件、异常/信号和未启动理由。新source全部科学结果与调用层错误分责；原 f12f result 的 `full_finite_head_complete`、query complete、work resolution、当前不完整piece、pending/source/query后缀和所有错误原字段都保。

原C未写最终result时，保已存在raw目录和完整新责任未付，不从若干成功panels拼成一个假完整头。读回若发现一个真实child result已写、但调用者在登记它之前停止，会完整读取其原metadata并标为 `actual_uncommitted_original_child_result`，不在metadata读回阶段补做同语义算术交或修改producer完成标志。

大账本只在原owned临时目录：读回逐完整流核byte/SHA与物理行数；外部硬停时保最后物理行是否完整，不用半行造paid科学地址。原完整query小结果保正文，原stderr完整文本保入必要对象；stdout大成功/进度内容只身份，不拆传。必要结果清楚声明未独立重算每个成功primitive/逆像数值。所有原未决科学行仍在其原ledger，不能声称hash等于工具端逐数值读取。

读回检查原producer PID/start_ticks、所有已启动自有child成员和实际独占组；未知、活跃或身份冲突时不产生complete marker。原readback绝对终点不重置；若原deadline缺失或到期，必要scope保持未付。

单份正文最大90000 B，frame为：

```
BEGIN_R489_SAME_C_FULL_HEAD_REFINEMENT_NECESSARY
END_R489_SAME_C_FULL_HEAD_REFINEMENT_NECESSARY
```

超限return70，仅小fallback和实际完整attempt身份，不分包、不编码大raw、不抬限。所有raw仍临时保留。正常完整必要scope且quiet时写 `readback-complete.json`，schema为必要schema加 `-complete-marker`，绑定本次run/source/summary bytes+SHA。

这个marker只声明读回与静止；其中另有 `scientific_recomputation_completion` 表示本组件实际完成状态。一个诚实partial也可以完成必要读回，不会因此成为完整C、更窄盒或accepted场。

## 9. 顶层CLI与调用者剩余职责

```bash
python -u "$COMPUTATIONS/geometry_20261116_same_C_full_head_refinement.py" run \
  --input "$ACTUAL_R489_INPUT" --input-sha256 "$ACTUAL_R489_INPUT_SHA"

python -u "$COMPUTATIONS/geometry_20261116_same_C_full_head_refinement.py" readback \
  --directory "$R489_OUT" --result-sha256 "$ACTUAL_R489_RESULT_SHA" \
  --out "$R489_NECESSARY_OUT"
```

`run`成功取得完整新source/cut时可以return0；所有原phase exit及粗界/工作标志仍原样报告，不能只看顶层exit推其它责任。来源/数学算术异常return2；明确资源/外部stop另保原exit与stop原因。`readback`以必要完整/quiet决定0或2，必要超限70。

调用者须实际形成输入及其SHA、复用原规则维护/owner/全job绝对钟，保readback和最后条件cleanup所需时间；本组件不自行写Git、上传artifact、派发workflow或删除raw。尚无本项request/workflow，未虚构未来217/R490运行。未来真实下游接受父、固定目标叶consumer、所有metric/reach/held与README误差精化仍独立未付，不由本入口替代。

## 10. 冻结文件与临时交接

最终source/proof/interface的精确字节/SHA在本目录 `publication-files.json` 中列齐；source完整增加diff及manifest仅作为临时交接，不作为科学结果或独立测试门。实际发表仅新source、R489证明和本接口，不复制原f12f/1c39/5bb2或任何原raw。

本项的源码依赖核对、JSON/hash和文本写作都是元数据操作；原积分、区间交和cut hull只在明确Actions实际调用中发生。当前既无严格收紧承诺，也无已经达到机器精度或原solver容差的结论。
