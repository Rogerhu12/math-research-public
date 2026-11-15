# R393. 实际182r2完整原160扫描与剩余136字节传输超限

作者：ChatGPT /root（AI协作）。日期：2026-11-15。此结论只报告实际元数据读回，不重算原科学，不修改原160的接受/失败分类。

## 1. 唯一实际来源

| 对象 | 实际身份 |
|---|---|
| request182r2 run | 43756253033 |
| source | 3b9877749db9212f937cd79cb464554887004078 |
| compute job | 132940880237 |
| 完整本次job日志 | 33724 B / c6bc73ebbf3ab95108219a1b665a73f0a1a6a8dbe59f5a221a134ba9bbb8503d |
| reader | 75754 B / c4728fbb2be01d3cf6648e18f3c8421daa71ee6ceceb99f9b6ece247e8e4ca74 |
| request | 10686 B / bdeebd5d68fbe241018eacdacfdfb3dc056edeb0cece4fc3adb1c11f31927748 |
| workflow | 8336 B / b84e300fd1d97a7ae994d840666690425435fd1a5db41585e3013df5b085ef0c |
| 原160 run / job | 43729874541 / 132859748674 |
| 原160 source | b34692d09c8d5ecdd7b859e43489da4413f1468e |

root仅在本次job终止后读其日志一次；没有在本地取原160大科学日志。原160流的完整解析、必要字段选择及大小检查只由公开Actions中的182r2执行。既有八个来源的bytes/SHA及双README绑定通过；仅reader做AST，原科学模块未导入或编译。完整源接口见[182](../notes/2026-11-15-request182-original160-native128-necessary-readback-interface.md)，首182事实见[R388](R388-actual182-complete-original160-log-and-necessary-summary-overflow.md)。

## 2. 原流扫描已完成，正文仍未传回

本次Actions读到原日志EOF：3234095 B、3513物理行，SHA256为27c888838abc2cabbe0dd14886ffdcffa76e4d35f21048b30367799d04363149，与首182一致。原raw没有保存为新文件。内部reader exit0、protocol_error_count=0、protocol_errors=[]、error=null、resource_partial=false。

内部临时result.json为89897 B / ca9ad0c1ca1ee236c24b23f3594962cbb050268495f7a5d9dfc8714edfe59ec2。加实际request/临时结果身份后的完整必要摘要为90136 B / 3fd32f1d1d3f3d43322ece8043d01057e8230f635876ee79d938049ed2504cee，超过固定90000字节上限136字节。外层因此如实exit70；transport_complete、readback_complete、summary_complete和complete_necessary_scope_returned全部false。

这次返回的唯一fallback正文不含分隔LF时3277 B / b4a164e0c37014354876681dee419091b48a6248a2d955ad7b54fa5b7eb21729；本次summary文件及打印身份**含最终LF**，为3278 B / a1ba365bb8c3f7d94a39fd45812fa59bb934e0cae652b25b1a4c320dac16aabb。保留步骤核同该文件；二者不是两个不同科学摘要。

## 3. 实际section大小与修订边界

Actions在上限检查前输出必要摘要各顶层section的字节数。主要部分如下；这些只用于传输诊断，不能替代各部分科学正文。

| 已选择的section | Bytes |
|---|---:|
| components | 37914 |
| original_QR_resource_error_and_lifecycle_events | 14492 |
| original_terminal_events | 13195 |
| owner | 10114 |
| verified_original_diagnostic_byte_streams | 6521 |
| original_event_counts | 1580 |
| selected_original_diagnostic_matching_text | 1154 |
| necessary_metadata_representation | 685 |

首182的92966 B已降至90136 B，但仍不能把未传出的科学内容写成已审读。全日志事件计数仍只支持“有一条trial、一条final、一条owner_final、两次component_start/return及一次all_components_return”等元数据存在性；不由这些计数推断某组件成功、原trial接受、数值误差、全部stage/column付清，或独立audit实际范围。

下一修订只允许缩短重复schema自述，或在当前同一必要JSON里共享严格相同元数据；原owner、四组件、全部trial/终态、数值词、键存在/null、错误、资源状态与未完成阶段必须保留。90000上限及1200秒/32GiB等既有预算不提高；不分包、不编码原科学对象，不新加科学门。新执行须另记录真实run/source/summary，不能回填本次失败。

## 4. 清理与尚未支付的科学责任

本次job的原始绑定步骤成功，必要读回步骤failure，保留小摘要步骤success，清理步骤skipped。内部临时结果留在本次runner直到其销毁，没有上传Git、Release或artifact，也不承诺跨job持久存在。根15要求保源码/参数/run/SHA/紧凑结论，此处不归档可重算原日志或完整科学表。

R359的四组件、原native128逐trial、stage/边界/endpoint/audit的真实完成状态、未访范围和最终flags仍待完整必要正文。首182及r2读回失败都不改变原160 child70，也不把该70解释为数学拒绝。全部576×224、112/338、fullDN/finalJ/audit、同g450闭场与README几何/metric标准继续未付。
