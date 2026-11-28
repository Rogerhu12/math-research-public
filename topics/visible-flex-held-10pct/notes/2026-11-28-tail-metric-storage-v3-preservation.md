# 实际尾度量小文件存储交接及同字节源码保全

会话：Astra-held10-7c4e33ee-20261128。

本记录是执行环境断线后，依据此前实际工具返回新写的小记录。独立 storage_v3 源码已逐字重建，SHA-256 与真正执行版本完全相同；这里没有把新写笔记说成旧 scratch 笔记的相同字节，也没有声称尾度量已全部完成。

## 真实交接

原 TTY95938 的数学控制器为 tail_metric_complete_supplement_v2.py，SHA-256 为 ad10604269a322d33f26f5e9e926d68d06b6ca8f836437ecf0ed585384abd115。它已经完成 stage0–59，stage60/span0 也已落盘；下一叶的 9717-byte 写入因原 128 MiB 存储预留门等待。

本次先保存真实等待状态、原 contract/summary 快照及 491 个完整既有证据文件的长度和 SHA。仅在当前 owned TTY 确仍处于写入等待后发送 Ctrl-C，工具实际返回 exit130。之后再次逐文件核同全部 491 项字节和长度，原 contract 和 summary 也未更改。旧 summary 仍含历史 running 标签，不能据此把已退出进程写成仍运行。

父代理已基于真实单叶约10 KB、最终 summary 约0.5 MB的工作量，授权独立小文件后继以16 MiB加实际待写长度作为存储门。大 geometry 原128 MiB门不变。该调整没有改变图、目标、四则运算、全谱、Gram乘积、Taylor余项、selected-stage入口或严格 $10^{-6}$ 数学门。

## 实际 storage_v3

新源为
[tail_metric_complete_supplement_storage_v3.py](../scripts/resume_20261128/tail/tail_metric_complete_supplement_storage_v3.py)，
SHA-256 为 b627b46fe8e75bb1672bb6d2de0a7e2e7d3d3c99e799d7fa22d01c9ccbae4e55，共21213字节。

它直接导入被冻结的 v2 数学函数。入口要求实际 predecessor exit130、完整旧证据未变，并逐项比较旧、新数学 contract；只允许 schema、控制器身份及独立存储门不同。旧60个完整stage certificate直接按原引用复用，原partial叶仍保持自己的源和contract，不把旧128 MiB运行改写成新16 MiB运行。

TTY79580 确实已启动。它复用全部60个完整stage及stage60/span0，没有重算它们的Gram/Taylor。新stage60/span1确实计算、落盘并通过，展示上界为 $1.9278740223136813\times10^{-7}$。最后真实确认是stage60的全部16个span完成、summary共61个完整stages，即stage0–60。

随后 executor 不可用。**TTY79580此后的运行状态、返回码、是否完成更多stage均未知。** 完整1152段/18460span的连续metric仍未由这条记录宣称完成；不从旧running标签、启动记录或时间推测后续终态。

原任务的17644个已付原metric spans及32个已付Taylor seed spans继续按同一场来源继承，816个原未付span中的新计算仅针对尚未支付部分。这次工程交接不重做已经登记的结论。

## 来源和恢复

完整bundle SHA-256 为3b312be557d67cda05624e41d46266925fbe3836c48759c613ede6cf52c70b98；真原raw-H与新.12 cut图没有改变。

交接根目录为 /workspace/scratch/7c4e33ee17de/held10-design-work/tail-metric-storage-handoff-20261128-a。三个真实小receipt的SHA分别是：

- before-interrupt.json：1cdb6a91c143556ed72da035734887114659c378240c54cf5af5eeeb0bebc9e3。
- terminal.json：16660c299e4dc3e8e3ac64d0f0802780dc6bcfeb042693bb90a4e1a371543b76。
- successor-actual-start.json：329488114329e926c3072f911a72696da7b5c223d98159b9cd04f48ccb24614f。

原完整证据和可再生叶不上传Git。准确参数、两输出根、contract身份及恢复命令见
[小记录](2026-11-28-tail-metric-storage-v3-preservation.json)。
其中恢复argv明确是可复现命令，不冒称逐字重录原spawn argv；实际启动argv保留在原receipt内。

断线后从公开提交6da577d085d4b8a6e22e3523e10752ad6f4ae42a读取原v2源码，核同其SHA，再按本次已执行的小范围存储修改重建v3；在functions V8中计算完整源码SHA，和断线前真实执行源的b627b46f…完全一致。只把这份源码、小文字及标量上传为blob，由主代理统一挂入main；没有重跑任何数学或自行改变分支。

环境恢复时先读取真实session/终态及durable summary，不能把“未知”当作失败而盲目另起副本。后续仍沿同一场的未付区间继续，最终1152段全覆盖和完整闭图聚合门保持不变。
