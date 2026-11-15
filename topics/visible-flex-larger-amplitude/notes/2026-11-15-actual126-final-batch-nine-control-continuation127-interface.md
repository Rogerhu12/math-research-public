# request127：从 actual126 第8批真实末点继续原九控制临时批次

作者：OpenAI ChatGPT /root。日期：2026-11-15。

本请求只更新真实起点、来源记录和工作流身份。原科学family、搜索入口、分段reader及已实际执行的批次wrapper逐字不改。它没有预先给出127的结果、接受场或新的几何证书。

## 1. 已执行依据与明确起点

[R287](../results/R287-actual126-eight-nine-control-batches.md)记录实际run43699369075、source b80ec2ad7d63918eb12fa6f02eef57fd5b6f5a1a。八个独立原批次各八方向接受、十四个外层试探；fresh首merit279.1236575692574，经真实链降到49.739792814348064，末unit第一项仍为−9.973944268492758，所有unit/full112/nonzero/native/success仍false。唯一链停止原因是 explicit_independent_batch_count_completed，没有零接受、原非预算停止、传输失败或资源中断。

因此127从真正第8批末九参数接原算法。参数顺序保持 p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3：

```json
[0.35492774711914105,0.21566361592859798,0.4379141866432249,-0.07589766636480334,-0.029272702912017837,0.7848308334598069,0.6773078757503707,0.4883556214691533,0.21781452899246784]
```

这九个数分别与原链 last_fully_read_parameters、第8行 final_parameters、原第8primary.final.parameters一致。source closure也与该primary.original_fields.consumed_source_sha256完整26项一致。只转录参数，没有保存或恢复上一轮J、merit、状态、差分、域对象或trust状态。

第8批的原身份为：

| 原对象 | 字节数 | SHA-256 |
|---|---:|---|
| 原status | 1512486 | 0b18be04bcd7331138c326d78a4975fdfb11fbc9a5b1b60418c0159812c8848b |
| 原primary，不含日志分隔LF | 62555 | c3126e3d46b1be0e3880e8f096db9b79172ef7649484e4ac4d94f9630ffa0613 |
| 原完整scalar view | 113376 | b5e1f7ad8ea1e99603fab3d3f98b0feb15c5ccf83caebbda5f3c312156bce2bf |
| 原整个八批链摘要，不含LF | 20119 | e7d726ca58b4fdefbd68b26fe3e61848cd65286d12e17a0843da047b7b508aa8 |
| 真正原第8末compact restart recipe | 1841 | 2153c417344eabf53ff915b2469c6fcd781d219d4f2654686424bb94b8c806f4 |

本次新参数文件采用明确的缩进JSON编码，因此2288B/e667ca5f的新配方不冒称与原1841B/2153c417临时配方字节相同。原status/大数组已按第15条消费后清理；短配方中的原SHA只是来源身份，消费者不会假称已重新下载原status或由SHA恢复场。

## 2. 三个更新文件与全部未改来源

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| computations/actual126-final-batch-nine-control-parameter-recipe.json | 2288 | e667ca5fcd73821b1394e09459022cd0b4c1f2310cb31deab2e036c75ef1adc0 |
| computations/public-nine-control-batch-request.json | 41500 | d75c1478315e46e818745fa2c50681eea78d828a9d30c9ca16c6fb9a3f5c2fc3 |
| .github/workflows/visible-larger-public-nine-control-batches.yml | 18134 | fa921b4ed3e48abba58a7223f8db525e89996dea0d5268e1b7b54ff54308b8ff |

workflow仍为本公开库同一独立九控制批次入口，由 public-nine-control-batch-request.json 的push触发；当前请求号改为127，report框名和元数据event相应改为VISIBLE127/request127。原126已经终态，不取消运行中的科学。

以下四项逐字不改，整个request的84项source_sha256及两项workflow_support_source_sha256映射也逐项不改：

| 原源码 | SHA-256 |
|---|---|
| geometry_20261115_nine_control_temporary_batches.py | b15a6571a1ebc5dc72f1037212fd86a10d7a5848957c2faca4ae9e7fd69f21bb |
| geometry_20261115_small_core_nine_control_family.py | 086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629 |
| geometry_20261115_small_core_nine_control_curved_recipe.py | 824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf |
| root_20261115_small_core_nine_control_curved_scalar_readout.py | f57a7dfae95f3e629aa412003e10ea4e32a9821b754c3d575318f97b09b7317d |

科学子入口仍读取自己的26项源定义，父与当前26项闭包相同；它们的完整canonical来源映射为3068B/183c35516a15f8447500d796eebf7f7a26ce7f4005f484e160a7886a9ad9a9db。完整固定来源、wrapper协议和清理顺序见[126完整接口](2026-11-15-actual125-nine-control-temporary-batches126-interface.md)，本请求不新增数学或读回门。

## 3. 每批原计算和停止规则

每个子进程仍为原最多八方向，每方向二十档外回溯，法向最多十二次、每次二十档。全部三残差、完整3×9导数、12×9 QR、两法向/七切向、实际原W及0.2 Armijo不变。实际内层目标误差不是外层接受门；126的20次内层tol=false接受不被追溯拒绝，也不预设127应出现同样行为。

每批初始相对半径明确重置0.1，末半径不跨批继承；最多八个独立子进程，不能把它描述成单个连续64方向过程。原初末全部九列差分、160-bit/depth14声明实表达式域、原完整453零圆、所有原final仍在每个子进程内执行。新batch重新形成实际初值和全部模型对象，浮点描述不承诺与前一过程末位逐字一致。

只有完整真实status和原分段reader均完成后，wrapper才生成该批自己的origin和真实末参数短配方。原非预算停止、零接受、子进程/reader失败、规则中断、资源中断以及最多八批保持原停止语义。3600秒只在完整批次之间检查，不是改写原单个科学调用的超时。科学step75分钟、job90分钟、report10分钟及原进程组规则监控不变。预算结束只描述这次运行，不使课题完成。

当前η三项保留为真实非零数。原zero-added-quadratic辅助读回继续在反事实η=0点比较旧六族evaluate数组；它不是当前起点，也不是旧六J。原科学入口若在该辅助构造处遭遇域失败，仍保原异常，不为了继续而禁用或重标通过。

## 4. 原输入、规则同步和输出传输

原四数学输入保持 accepted96、prepared112、zero anchor和T112 config，全部SHA和字节数不改；仅从公开历史8bd267107cc8710d371f3b62c02986655ac965b0恢复到本run临时目录。原78份公开native来源仍按原恢复器一次恢复。Python3.12.14、numpy2.3.5、scipy1.17.0、python-flint0.9.0、单BLAS线程与126一致；没有本地科学运行。

原规则runner源码及2700秒真实pull、双README差异检测/中断责任不变。明确审读的根blob为74c08a36f6c997d0bc1e64a7956b42276f5fa5d7，题blob为bff8aea253a9e6a7a4fac28d810ac454c5499fec。root终端恢复后另外每push前且至少每小时真实pull，并将所读main提交写入HANDOFF；该规则不被Actions周期监控替代。

每个batch的原reader stdout继续逐字写在唯一批次框中，原方向组及各part的SHA/字节数保留。原primary另在对应BEGIN_VISIBLE_NINE_BATCH_001_PRIMARY至008框独立打印；没有把八份primary挤进GITHUB_OUTPUT。report只传紧凑列式链索引，打印BEGIN_VISIBLE127_CHAIN_SUMMARY和SHA事件，SHA范围仍是UTF-8 JSON、不含分隔LF。

完整status、原reader、下一recipe都消费后才清理已结束批次raw；always报告步骤读取链后，才清理本请求拥有的其余临时科学输入/源缓存/未完成payload。没有Git、Release或新artifact raw上传。保存内容仅完整源、实际参数、run/source/输出SHA及紧凑结论。

## 5. 本请求未付的责任

127目前只是明确执行入口，没有预填run、候选成功、非零112、native、完整fullDN或最终审计。即使低三条件通过，也须实际付高109/完整112和非零场；圆参考、差分或数值奇异值不能替代那些责任。

真正fixed-g450必须在真实完整父场的最终九系数上冻结；闭合、强C²全时族、连续g、全域相对metric、嵌入、reach、固定有内点区域和整个像幅度仍各自保留。达到READMEs全部标准之前，本轮批次/时长结束都不是收尾条件。
