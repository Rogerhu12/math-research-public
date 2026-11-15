# R374：actual176 找到 38 个反证节点，但完整日志计数与有界读回尚未完成

## 374.1 结论

actual176 是对 actual165 已保存日志的纯 JSON / 字节 / 元数据读回，未重新计算 C、profile、区间、导数、域不等式或任何模型。

它在公开 Actions 内完整流式取得原 compute 日志并到 EOF，内部找到 38 个唯一原严格反证节点。但扫描得到的 final-cover / pending / unresolved 数量未与原 target result 对齐，触发实际 ValueError；随后必要摘要 95577 B 超过固定 90000 B，程序按设计返回一份 2388 B 的明确失败摘要，process exit70。38 条具体 u 位置和 a/as 界没有在该有界摘要中返回，不能称这项定位已经交付。

这不改变 R356 中原 accurate domain 的科学结论；也不提供一个新域反证或新域通过。完整原计数为何有差额仍需基于原 emitter / 实际字段定位，当前不能宣布原日志丢失、错误修改原计数或把缺项填成预期。

## 374.2 实际来源

| 项目 | 原身份 |
|---|---|
| 新 run / attempt | 43746302206 / 1 |
| source commit | 97a99672e779d4b1f4aadcdb6adb6c7198187378 |
| job | 132910242777，original165-refutations，failure |
| 新 reader | root_20261115_read_actual165_strict_refutations.py，28097 B |
| reader SHA256 | 07d3b2608bf4f9614ed74465ddb40f068f130f69f1e5208912bfc3ab6bddb631 |
| request SHA256 | c0e938965b9f4824e58d7d302d7d66bd65e88c38cb055a5b73aa289ed81529ec |
| workflow SHA256 | 3919128037850ae017676bb7e35f008aefec9e1bc44f51969fe8212a09ee23ad |
| 新 job 原日志 | 27353 B / 870588b883b3aaaae5d2e4b4bb9c02ef6a1ec29ece3f06ff2bb83e46911b7b46 |
| 唯一必要摘要，含末 LF | 2388 B / b222781546adbd8f7bfe477241aa1147d424dbae8dd94bf157673aab60b4d94f |

原被读对象仍是 actual165 run43736208020 / job132879253906 / source1f2ec637430e5c6b27b1a93720e106539281a156。其原 source 为 94125 B / 61b98b3e853b31535ac31b66d4cf4513f1271d9852acfb09b948990a30acb205。

原 target result 身份保持 105512 B / e5ec825f39c2f57aa6f04b46c56371b6876670a04ac7c5c9129bdcc80af2c619。reader 走到 finish 中的 cover-count 比较之前，已通过该完整对象的字节、run、source、schema、源文件身份核对。本文没有重新取原1.48GB日志到本地或会话，只读取此次小 job 的真实输出。

## 374.3 实际读取范围与未完成范围

原流式日志 identity 在 Actions 内实际形成：

- bytes=1486048285；
- SHA256=4ab8c6d688a27869353bb428288d467502c7aed6ad8cd96140a6cfaea508aea2；
- raw_lines=165009；
- full_log.complete=true，raw_log_saved=false；
- resource_partial=false。

新 reader 观察到的原计数如下。右列是其绑定的原 result / R356 计数，不能反向替代左列：

| 字段 | 本次实际扫描 | 原目标计数 |
|---|---:|---:|
| original_final_cover_events | 32667 | 32977 |
| original_pending_or_refuted_events | 32480 | 32526 |
| original_unresolved_events | 32442 | 32488 |
| original_unique_refutations | 38 | 38 |

38 个节点的发现与全 cover / pending 统计完成是两个不同事实。代码对已找到的反证节点在内部执行原 pending.enclosure 与 final-cover 原字节联结；但当前小摘要没有返回这些 38 行本身，所以本结论只保其实际计数，不声称亲读其具体位置或 bound。

实际异常原文为 ValueError: All original final-cover events are accounted as metadata，位置为 reader main 的 scan.finish()，以及 finish 中对 cover_count 的比较。该异常之前的无未完相关 segment / 无 malformed relevant 及完整原 result 存在检查已在固定源码路径上执行；这是源码顺序对实际错误位置的解释，不是新观察到的缺失事件种类。

目前没有证据证明所有缺项由同一种格式导致。尤其不把可能的动态 label、日志前缀、原记录变体或 transport 行格式猜测当成实际原因。后继应先查固定原 emitter 的确切 label / 输入解码责任，并保真实观察计数。

## 374.4 传输失败与科学结果分离

finish 异常之后，reader 内部保存的小结果为：

- result.json：95389 B / af4f4c85b1955bc669dcf7a13c6c96ae959c9942a470de13f8a232d204891c06；
- 原必要 summary 候选：95577 B / d0689fe6497c5ce32f67a202c5e5279d33dcf65e5b156357fc55ee45f9d02b67。

这两份对象没有通过新协议拆包返回，也不另存 Git / Release / artifact。最终 2388 B 摘要明确：

- reader_exit_code=2，process_exit_code=70；
- readback_complete=false；
- summary_complete=false，transport_complete=false；
- original_internal_scan_complete=false；
- complete_necessary38_table_returned=false；
- transport_error=necessary-original-metadata-exceeds90000bytes；
- no_new_output_segment_or_reassembly_protocol=true。

其中完整原 log 到 EOF 与内部读回完成不同：前者 true，后者因计数不齐为 false。原 scientific exit4 属于 actual165，不改成176的2或70；176的返回状态只描述元数据读取 / 传输。

实际 workflow 的源绑定步骤成功，扫描步骤失败，always 保留摘要步骤成功，cleanup skipped。always 步骤核到同一2388 B摘要已打印，只输出 receipt，没有再次打印表或重下载原日志。未清理对象仅随 runner 生命周期存在；不得凭其 SHA 假称未来可直接恢复其正文。

## 374.5 直接后继责任

下一次纯日志读取必须保持实际原 tuple、105512 B result identity、38 节点逐原绑定和固定90000 B读回界。修正应针对真实 emitter 格式与必要 metadata 的冗余；保全部38个 node / piece / u 两端 / depth / classification / reasons 及必要原 a/as 严格反证界，但无需重复发送同一 node identity、嵌套 receipt 或同一 enclosure SHA。

任何计数仍不齐必须继续明确未完成；不能减少原范围来制造成功。必要表超过上限仍明确 readback 未完，不上调界、不拆包，不由这项元数据任务增加新的数学接受条件。175及当前非零场实验不以该后继读取为前置门。

本文的所有数字均为原日志字段或字节身份。没有重新评估任何 a/as、目标系数或严格不等式。
