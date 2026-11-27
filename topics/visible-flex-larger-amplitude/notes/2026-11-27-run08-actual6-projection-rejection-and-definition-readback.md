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
