# 2026-11-27 run08：实际第6步投影拒绝与完整定义读回

## 真实返回

[run08](https://github.com/Rogerhu12/math-research-public/actions/runs/45929088658) 的新第6–8步均已实际返回退出码1。第6步使用整份 `6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19`，真实运行6.137976809000065秒，报告内部0.2782167989998925秒；失败是：

`ValueError: The actual whole mesh or complete fixed material chart differs from historical input`。

该报告完整4407字节/SHA256 `87573603d6bc53ff720ceaeb76114dc6f8b1df130d6d6dab5946ce4818c41045`。它已实际绑定当前run/attempt、公开卷与reference输出，但在mesh/chart联合守卫处退出；**没有进入2397-leaf数值重建，也没有得到候选旧载体或新binding**。不能根据这个联合错误区分到底是哪一项不同，也不能将其解释为新的warm/数学域相等结论。

第7步a52e和第8步475f各运行6.137662245999763、6.138384421999945秒，均无科学/纯读回输出；后续不是完整新场结果。实际第6步46项summary_errors和两缺失输出、第7步一summary_error和两缺失、第8步一summary_error和一缺失全部保留。

完整真实卷固定于提交 `c509ce70c930b0c3bd0c0339dcfaa50a5a08cee9`：

- [实际第2卷](2026-11-27-public-actions-45929088658-1-part-002.md)，30776字节；
- Git blob `0ed825a2586eab017c1325d144aff214ff9164c3`；
- SHA256 `6b904adbf7604a68982fa0359bd45523adf45fc202f7c11f5228700013a08261`。

完整原三对象仍在活动队列，没有为本次诊断删除或改写。原[全源码/参数修复说明](2026-11-27-run08-current-warm-projection-and-complete-old-carrier-repair.md)保留为实际已尝试的完整来源，其“尚未返回”描述属于发表时状态；以本次真实返回更新，不冒成功。

## 直接读取实际定义，不放宽身份守卫

新增一步只读取同runner实际preparation报告（29810字节/4a3357f5…）与上述失败报告，两个完整SHA写死。它核实际4e reference source、complete状态、整个reference_definition canonical model SHA以及实际6cc失败身份，输出完整实际定义及mesh/chart/current warm/first3摘要、原失败和真实warm public binding。

该动作不读数值数组、不重建scalar、也不调用F/J/root。它只是针对已经发生的联合守卫错误读取真实完整定义；不作新求解前门、不声明同g/载体同字或通过原守卫。

完整源 [read_actual_run08_projection_failure.py](../scripts/resume_20261126/read_actual_run08_projection_failure.py)：5089字节，SHA256 `f10faa77ccfe5d9c569b3f05d1fe9a5055e85269c154e79af8b3980e92829ded`。环境失联后只作完整文本/参数检查，未宣称Python AST或compile已经执行。唯一执行位置是本公开Actions的真实run08/attempt1，完整8词argv、parent、outputs和所有摘要字段保存在 [完整参数](../computations/run08-actual6-current-projection-readback-ready.json)。

本次追加新唯一step ID `read-actual-run08-complete-current-projection-definition-after-step6-20261127`，输出到新的runner路径，不覆盖失败文件。当前未返回的诊断结果不预填。若证实是接口接错，修复确切完整源码；若输入确已改变，则更换完整原输入重建或开展具有明确固定目标和历史责任的完整新分支，不能放宽mesh/chart要求后冒称原同场。

科学完成标准与全部E/typed/同g/精化责任不变，继续研究。

## 实际第9步：mesh相同，完整固定chart不同

第9步已实际完成并返回0，控制器seconds为6.154771044999961，读取内部0.0009769970001798356。完整实际输出为8083字节/SHA256 `4c3bbbff7f13ec801d8300c58c2d45c6feb8fc786d9a2cb3de9f752a395c61ec`。完整preparation与失败report的原wholeSHA和model SHA均重新通过。

| 实际定义字段 | 当前实际值 | 历史要求 | 比较 |
|---|---|---|---|
| 全mesh SHA256 | `eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262` | 同左 | 相同 |
| 全固定chart core SHA256 | `7c4c9b736c0c8081e9f00a131db5fb63af224aa64fb476c07c78c09b5288bb48` | `90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e` | 不同 |
| 实际完整reference model | `492456a67601cac752dc8e5cb79c14eaccc7339b2d3206f0d570bb60b02c5c5e` | 不冒旧model同一 | 原样保 |
| 实际whole warm | `4c34e0889a40e67a3a0a38abce030bb0358f74333fc1d8c95f669d5beefd9a0f` | 不冒旧whole warm | 原样保 |

这次真实读回将第6步的联合拒绝具体定位到模型记录中的固定chart字节身份不同，mesh身份并未改变。不能从“参数/源同”或差异可能很小推断同一个固定材料度量，也未取得旧chart全部系数逐字对照。原6cc的严格拒绝保留，不把expected摘要换成7c就宣称原90的历史责任已付。

完整实际definition和warm binding留在runner该8083字节输出；controller只允许scalar summary，所以本次误选的四个非标量字段 `actual_fixed_core_first3`、`actual_reference_definition`、`actual_current_warm_public_binding`、`original_failure` 被如实登记为四项 `Requested summary is not scalar`。它们没有在公开卷完整返回，不能把已公开标量说成完整对象已公开。所有必要的本表标量已实际返回；无需为了补打印重新运行数值构造。

更新后的真实卷为固定提交 `a145bbec0c1b24bf709c9bd86e7656703e68b11d`、blob `eb0fab203d187e4498983eb30a08c574827311d1`，37303字节/SHA256 `f3a69d930714259c9a954a9910602743194a73299c69e4c1f2bf6eeea3b8e429`。先前30776字节的6–8快照身份仍有效，二者是不同时间的完整卷，不混同SHA。

### 全参数6–9归档与继续路径

真实6–9四对象现按自然阶段分成两份完整归档。每份包括原完整队列头、固定原队列65,523字节/SHA256 `87ec42ac3100b7bc55e5ba1404d7312a965144eefe0842c5fdf1e69a491b6f81`、完整原step及实际完整compact return。失败、summary_errors和missing_outputs原样保留。没有归档任何待返任务。

- [resume-20261127-followups-08-returned-006-007-archive.json](../computations/resume-20261127-followups-08-returned-006-007-archive.json)：70664字节，SHA256 `2ff1c679a8cff5e49c26c719e7999dcb2bdb24b9828b87944ab186c915ed6df1`。
- [resume-20261127-followups-08-returned-008-009-archive.json](../computations/resume-20261127-followups-08-returned-008-009-archive.json)：41221字节，SHA256 `37fa7d6c7185c8d97d6f749708f7caad7c851402674915f087345079e27716a5`。

控制器继续 `finish_when_done=false`。后续必须实际取得原完整chart输入并重建，或完整声明独立冻结的新目标及原历史边界，再以完整源/参数继续；不能放宽旧守卫、改名旧SHA或把本次元数据读回当数学同一性/metric/reach/精化证明。原分支仍保，题目未完成。
