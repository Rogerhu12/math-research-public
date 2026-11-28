# 连续尾 metric 的实际小文件存储续接

本条记录一次已经执行的工程交接，不是 metric 不等式失败，也不是降低数值验收门。原 v2 数学源、全部场/高度/均值/谱、原 target、完整 Gram/Taylor 余项和严格 1e−6 门均保持原样。

## 真实旧终态与完整保留

原 owned session 95938 已完成 stage0–59，共60个完整实际stage，正在 stage60/span1 的9717字节叶写入前等待原128MiB磁盘预留。父任务明确同意为当前约10KB的单叶及约.5MB最终摘要使用独立小文件存储门。

在发送信号前，实际复核了原进程新鲜的写等待记录、尚未完成的摘要状态和当前free不足原门；保存旧contract/summary/等待记录快照与491份durable文件的完整SHA和长度。随后只对 owned TTY95938发送SIGINT，工具实际返回exit130；退出后再次复核491份文件、旧contract及旧summary全部字节未变。原程序没有KeyboardInterrupt finally写入，所以原summary的历史文字仍为running；独立terminal.json明确它已经停止，不能再凭旧字符串误认为活进程。没有向其他任务发信号。

## 实际独立后继

新入口 `tail_metric_complete_supplement_storage_v3.py` 已真实启动于 session79580，独立输出目录为 `tail-complete-metric-supplement-20261128-b`。它调用被冻结 v2 的全部数学函数。新metadata明确写v3源码、新16MiB门、旧v2数学控制源、旧128MiB contract及实际交接记录，没有把旧source/门伪称成新执行。

逐项比较旧新contract，除了控制源/schema/实际输出存储门，全部物理、目标、proof cutoff、最大深度、oracle来源和种子来源必须准确相同。旧60份完整stage证书直接继承，不重算原Gram或Taylor。未完成stage中的durable叶按原SHA/contract/实际radius区间核同后直接引用；只有尚未落盘的叶继续原计算。

新门严格要求 free≥16MiB+本次真实序列化字节数。初启时free一度仅409600字节，因此新门也真实等待；盘恢复后自动续行。实际stage60/span0已引用旧durable叶，先前未落盘的span1已真正计算并通过，metric向外界 `1.9278740223136813e−7`。这不是只写prepared后停止。

旧大geometry导出的128MiB门完全不改。新门只适用于这些小JSON证明写入；外部共享磁盘继续变化时仍按真实free等待，不挤占预留。

## 证据与后续

同名JSON列实际命令、两个owned session、原exit130、旧/新source及contract、原491文件清单、第一份新实际叶的SHA。全体原数组、完整尾、F的native输入输出和其他任务不变。原连续计算继续，只有全部1152段/18460个原spans真实通过后才可宣布完整有限尾metric；本条没有提前宣布此门或题目完成。
