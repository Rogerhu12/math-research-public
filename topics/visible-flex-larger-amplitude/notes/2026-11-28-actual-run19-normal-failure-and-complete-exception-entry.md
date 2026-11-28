# 实际 19 的准确 normal 失败边界及完整原程序异常捕获入口

本说明记录一个真实执行事实和一个源码层可修复的报告边界。它不提供 19 的内部失败归因，也不把缺少报告解释为均值、法向根、物理场或连续几何不存在。

## 1. 真实返回及仍未知的部分

公开 run `46076669320/1` 的完整第二卷在固定提交 `337cd41922aac5dbec0359f0bee6ccf2a282455a`：
`notes/2026-11-27-public-actions-46076669320-1-part-002.md`，
39,841 字节，SHA256
`ffcf15e785d46f1cc4ebe542f7a1344310be12bdd39d738e507381bebf1f88e4`，
Git blob `74cbdf87541ba6a1a82cd00fb5fb10069f679da1`。

原第 4 步完整 pure reader 返回 0。第 5 步准确 normal 返回 1，用时
`324.00838658499924` 秒；实际源提交为
`b9275d6373a1caa703a5eb77356f3e9662515463`，完整执行源为下表的 c6f6。
该步 `outputs=[]`、`metrics={}`，紧凑返回只包含缺失声明的
`fixed-fejer-meridian-batched-bhalf-first-R722-normal-root-and-sixjet-fees-v1/report.json`
的 summary error。没有返回实际 Python exception type、message 或 traceback。

原执行的完整对象、全部 38 个原参数词、真实绝对路径、输入来源、缺失输出与 cleanup 原对象已逐值保存于
[完整事实 JSON](../computations/actual-run19-accurate-normal-failure-and-capture-entry-evidence.json)：
14696 字节，SHA256 `7a8961f53fb2c4d6a7c45102c966c84f8e0b677612fdf7d1d9d393fc50fad285`，blob `cee31d5a310645431cbf1058748b44a1de268125`。
原 pure 完整对象仍在上述整卷中，事实 JSON 给出其确切节和 JSON block 定位，没有删改它。

这证明一个未成功返回准确报告的真实执行。它不证明：

- 900 秒预算耗尽；真实返回时间少于该数也不能定位失败位置。
- 任何特定 source guard、snapshot、mean candidate、packet、scalar 或 root 失败。
- runner 内没有未声明的临时文件或中间计算。
- 原公开 workflow 的 success 代表每个科学 followup 成功。
- 末工作场可行、连续费用已付或终态 runner 可续接。

19 已终态，本包没有排、执行或建议补跑该 run。其未返回异常原因保持 null。

## 2. 已完整读取的原源和确定的控制流

| 角色 | 完整 basename | 字节 | SHA256 | Git blob |
|---|---|---:|---|---|
| normal | `fixed_fejer_meridian_batched_producer_R722_complete_normal_root_and_sixjet_fees.py` | 40559 | `c6f6c9726b23ceb25533d5a6a6ac41fd31e8a3c14226895d5fc32e74787c0108` | `b50928f14b339f2641c7600a32edfe786409bbbe` |
| input | `fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py` | 32969 | `d892bedeadca4fe0689069ac7489a41c1d348311c2b84dad292bf48133e71cc7` | `6a724fcd48a0d1da27b4762c9ac4ef6ac734cae4` |
| radial | `fixed_fejer_meridian_batched_producer_R722_accurate_reference_control_radial_boxes.py` | 46495 | `7c66ed0f31323451156c1cd76ae7401eb497f37377393bb66503523ad2aaac54` | `091a84d4222e36b0ee690e0c4f742c726dc80b17` |
| kernel | `fixed_fejer_meridian_batched_producer_R722_posterior_mean_jets.py` | 45225 | `4fc252f8977f4f4246d2cc13583efc0bccd4b28742df3a797d1c266cdd1eac7d` | `e3fa2b73f5ae0dddaa049133bd9a8d61c89d8908` |
| reference | `fixed_fejer_axisymmetric_reference.py` | 60335 | `e7175f591a14844331b55c9c09cc6d0ff25f1e2f390706c951f9b6a6008322cb` | `8ad0794ebf0daab9a278c5ea1de784e93b64fd8c` |
| packets | `fixed_fejer_meridian_root_packets.py` | 73723 | `c750d234fc370d3c74da4577bc99f7fca417dbed169bc3a9d1e7222ea99c84b4` | `2b294ce46cf51c24c90b6e71c26d0d9c4269d28f` |
| continuous | `so3_axisymmetric_continuous_integrand.py` | 29047 | `a846d373421df655da3bbba2491847b0cd016ae6db09b5d4176be227b2bc9ce6` | `76d475cc54814b19e1d3aaaab8200a9ba7d7d151` |

上述整源均作为原字来源保留，本包没有改写其中任一个。

c6f6 的 `main` 从第 566 行开始。顺序为：

1. 解析全部原参数，核公开 Actions，加载准确 rotation/radial/input/posterior 四角色完整源。
2. 在第 574 行构造 `ActualNormalPacketPoint`。该构造完整读取实际报告和 pure；核全部 137 个科学角色；重读六个真实固定输入与 target/model/chart；核每个 immutable packet/array；选同一点完整 required-angle snapshot；恢复完整自由向量与校准记录；构造准确参考上下文；读完整 saved mean candidate batches。
3. 建立原 `WorkBudget`，随后第 582 行构造全部已记录 literal angles 和 1024 个闭圆角胞的请求。
4. 原样建立全部准确参数、完整 input/request 与 immutable request identity。
5. 第 659 行第一次写科学 `report.json`。
6. 第 660 行才进入现有的 accurate geometry/journal setup 的 `try`。

因此，第 1–4 项任意真实异常可以发生在首科学报告之前。原代码在这一区域没有独立 exception artifact；这是一项可由完整源直接确认的记录缺口，不能据此判定 19 恰在哪一步失败。

原 geometry setup/job 的异常处理还会先调用 `actual.recheck()`，再写部分报告。重核自身可能抛出异常；这是必要完整性守卫的真实语义，不应删除。外层捕获可保 Python 的 cause/context chain，而不修改它或覆盖原异常。

也核对了一条具体怀疑：d892 调用 e717 的
`AxisymmetricReferenceContext.from_files`，实际 keyword 是
`repo, reference_bundle, carrier, node_report, scalar_input, preparation_report, panels`。
原调用提供这组实参；没有发现“缺少 material-envelope-binding keyword”的接口错误。
同样，当前证据不允许把重复角候选、缺 packet 或某个 model guard 预填成实际原因。

## 3. 新入口的准确职责

完整源：
[capture_complete_accurate_fee_exception.py](../scripts/resume_20261126/capture_complete_accurate_fee_exception.py)，
14448 字节，SHA256 `16c18a231f19718594dba5abb8cb72e67c7eda3f2974aa061d2bcf72cfc57f5e`，
Git blob `2584e65a5306ca8aae5c6478e8a0c1551dac81b1`。

入口只接受：

- 实际完整原 Python 文件的路径、字节数、SHA256；
- 本次调用专用且与原输入/输出分开的新诊断目录；
- 字面分隔词 `--` 后的全部原程序 argv。

它先核原文件的全字身份，再用
`runpy.run_path(original_path, run_name="__main__")` 调原程序一次。
原 `__file__`、完整 `sys.argv`、源所在目录和原源码正文保留。
输入/packet/source/target/model/root/mean/角域等科学守卫全部仍由原程序执行。
入口不导入另一个近似科学实现，不更改已有算法，也不替换源常量或 source registry。

捕获器不打开任何科学报告、NPZ 或数组；它只读自己和所执行原源来记录 whole identity。
原 stdout 保留，不追加另一个可被当成科学返回的 stdout JSON。
简短诊断提示写 stderr，完整诊断写独立文件。

原程序的 `SystemExit`、非零退出及其它 `BaseException` 原样再抛出。
若原 `__main__` 以 0 退出，诊断只记“原入口返回”；原费用可能仍返回
`complete=false` 或 enclosure unavailable。包装器从不以 exit 0 推出科学完成。
异常保存本身失败时只尽力写 stderr，不能替代原异常或改成功返回的原退出状态。

这是执行证据入口，没有额外 F、J、J*、根、校准、数值探针或科学步骤。
900 秒预算和叶数预算仍在原源码原位置建立并执行；包装器不缩放、不提前耗用、更改或重置它们。

## 4. 诊断文件与边界

必需的小输出为：

```text
<fresh diagnostic directory>/execution-diagnostic.json
```

schema：
`complete-accurate-fee-original-entry-exception-capture-v1`。

它保留本次 invocation identity、捕获器和原源 whole record、完整原 argv、run/attempt、环境 source commit、PID、真实 UTC 时间、是否已调用原入口、原退出码或真实 exception type/module，以及数学完成未推断字段。

发生可捕获 Python 异常时另保：

```text
exception-message.txt
python-exception-traceback.txt
```

完整 traceback 包含 Python cause/context chain 和整个 ExceptionGroup，
不捕获 locals，不打印数组，不进行新的科学调用。每份原文件都有绝对 path/bytes/SHA256。
trace 本身小于 95,000 字节且完整诊断能保持小于该限制时，全部 traceback 文本也直接嵌入小 JSON，供实际返回保留；没有用固定尾段假称完整 trace。

若原 argv、完整 exception 或 metadata 较大，完整 event 另存 runner 文件，
小 JSON 给其确切 whole record，并明确
`complete_python_traceback_text_in_this_diagnostic=false`。
完整原内容保留而不是被静默裁掉。大原 trace/event 仍仅在 runner，
后续是否读它必须按现有真实大小和返回规则决定，不能预称已经取得。

绑定源之前写入初始记录，源匹配之后保存 ready-to-invoke 状态；
进入原调用时仅在内存把 invocation count 设为 1。
若平台杀进程、SIGKILL、内存终止或整个 runner 丢失，没有 Python 控制权就不能保证终末诊断。
初始记录只证明包装器到过相应位置，不证明原程序已返回，更不是完整费用报告。

参数解析、Actions 权限或诊断目录本身无法建立时，也不能伪称已捕获原科学异常。
这些属于入口/文件系统执行失败；它们不放宽原科学输入合同。
诊断目录须为新路径；原 scientific outdir 可以按原程序合同继续同目录，不得因此随意换它。

## 5. 完整参数转换器与可逆关系

完整文本构造器：
[derive_complete_accurate_fee_exception_capture_step.mjs](../scripts/resume_20261126/derive_complete_accurate_fee_exception_capture_step.mjs)，
11211 字节，SHA256 `1e0c80553a622ec7130e385d19907630d7716d1c044a384f49cb4aa479e6a9f6`，
blob `540cf31841da575c91ead73a19937fb6f37e5bd6`。

它只构造 JSON，不执行任何科学源。输入 recipe schema 为
`complete-original-accurate-fee-exception-capture-recipe-v1`。
recipe 必须提供以下完整字段：

| 字段 | 内容 |
|---|---|
| `parent_ready` | 原完整 ready 的仓库相对 path/bytes/SHA256，可附已知 Git blob |
| `parent_step_pointer` | 该完整文件中实际 step 的 RFC6901 JSON pointer |
| `target_source` | 与原 step.script 完全相等的原源 path/bytes/SHA256，可附 blob |
| `new_step_id` | 本次新 controller step ID |
| `diagnostic_directory_relative_to_work` | 独立新诊断目录，不能是原 scientific outdir |
| `output_ready_path` | 生成完整新 ready 的相对文件名 |

构造器以 `--repository-root`、`--recipe`、`--output-directory` 三个文本构造参数读取全父 ready 和完整源，核它们的 whole identities。
没有嵌入一个假未来场、未返回 report SHA，或可以重排 19 的当前 step。

新 controller step 的完整原对象保存在结果中。只作必要执行包装：

- `script` 指向捕获入口，原真实 source path 放在包装器显式参数中。
- 包装头 8 个词加一个 `--` 后，原全部参数词逐值、逐序保留。因此原 N 的 38 词变成 47 词；原 38 词及所有数值完全不变。
- 新 id 只区分这一次调用；原 scope 全文保留并追加诊断含义。
- 全部原 outputs、完整 summary、progress selectors、parent relation 及其它 step 字段保留。
- 仅另加独立诊断 JSON 的 declared output 和其明确 execution selectors。
- 原完整 ready 全文以 whole file identity 加空 JSON pointer 保留；结果同时保存完整原 step，不裁掉其原对象。

转换器按完整对象构造逆映射，去掉包装头、独立诊断输出与 selector，恢复原 id/script/scope后，与整个原 step 比较；这只是文本构造的完整性，不是新增科学验收或执行测试。
若完整输出超过文件容量，构造器拒绝裁内容；应共享完整原历史，而不能删域、预算、参数或 selectors。

本包没有为 19 产生新可排的具体 ready，也没有发 queue、触发 workflow、重跑科学或变更 refs。
后续真正选定可消费的完整 report 后，根端可把已准备的那个准确源专属 ready 包装为一个真实 fee step；这不是先运行一个测试，再运行科学。

## 6. 原 source checkout 与同目录续费不变

捕获器不会改原 `--repo`、`--report`、`--outdir` 或 snapshot selector。
若是同一 normal outdir 的续费，原 immutable request/binding 对绝对 source records 的要求仍照原实现生效：
必须先由真实已返回的首次 step/source_worktree/command 确定合法旧 `--repo`，不能把新 step 的
`{repo}` 猜作可替代的绝对路径。

包装器自己的当前文件可以位于本次 source checkout；实际被执行的原源也按明确路径和全字身份绑定。
这不意味着可以删原输入/来源文件或把路径身份抹成只有 hash。原程序的完整 recheck 继续决定合法性。

controller 的本次 entry source SHA 是捕获器的 SHA；
原科学报告里的 source SHA 仍是被执行的真实 N 源 SHA。
新诊断以 expected/actual target whole record 把两者明确关联，不能把 wrapper SHA 冒成 N 或借 N SHA 冒 controller 入口。

晚续 normal 若改 whole report identity，早先 geometry/R723/R716 对旧报告的绑定不会因此自动更新。
仍须按既有完整消费顺序读取最新真完整 N，再生成相应 G/R723 和后继；诊断不代替这些报告。

## 7. 来源族和未来工作边界

捕获器可包装任何已钉完整原 fee 程序，但它没有能力把错误来源变合法。
20 的原 full-wave、22 的 paired-halfwave、25 的 cache family、26/27 的 R725 和新的 R726 都必须使用各自明确适配的 input/model/source/seed/根域。
“同参数名”“同 g”或工作进度相似不能让 c6f6 自动消费这些其它族。

R726 必须读真实 Slerp B/J/两角链，准确存在域按已登记的 R726/R727 条件处理。
旧 chord/R722 根势不能只换 hash 继续使用。该准确后继是另外的实际数学实现，不由本异常入口完成。

所有未来完整报告、point、snapshot、实际异常和费用在本包中仍为 null。
没有把已成功的 pure 返回、初始化 progress、partial report、accepted count 或 workflow success 当作准确完成。

## 8. 实施范围

本包完成全源文本、完整实际失败事实、可逆参数构造源及其完整身份说明。
没有进行本机 AST、compile、数值、微基准、fixture、科学 replay 或新增运行前门。
可确认的是原源码报告边界与新捕获源的明确职责；19 的实际内部异常仍未知，后续真正执行记录将给出它自己的事实。
