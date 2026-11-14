# 两个实际执行问题与继续计算

2026-11-14。此记录只陈述真实过程、输入修复和恢复；不把过程退出
当作数学门失败，也不声称尚未结束的原生计算已经完成。

## 1. 全物理帽矩阵的 SIGBUS

停用公开代跑后，本地从原8个已保存块接续完整660块 QR。该次实际
子进程返回 `-7`（SIGBUS），观察时长195.732063962秒、最大子进程
RSS170808 KiB。它已经完成全部660个 QR 因子；matrix-RHS 的最后
原子检查点为 forward `next_index=104`，全部96列保留。

当时 overlay 总63 GB、已用59 GB、可用约756 MiB。`top.npy` 的
逻辑大小为97827968字节、已分配约15421440字节。磁盘压力与 mmap
写入位置都已观察到，**没有据此断言唯一的内核错误原因**。原进程
记录、已完成因子、forward 检查点及未完成 backing 文件原样保留。

恢复将整个 case 的175个实际文件逐 SHA256 复制到本机空闲 tmpfs，
并在恢复写入前对原 `top.npy` 完整预分配 backing；预分配前后 SHA
一致。原 source、case、输入、全部数学门和第104行之前的数据均
未变。新过程从真实第104行继续，不重做全部660块，也不把原返回码
改成成功。完整逐文件记录见
`2026-11-14-R133-physical-cap-SIGBUS-prefix-recovery.json`。

另只清理已完整成功的两份 regular trial 的1538个可重建 QR seed
缓存，共230540048字节。全部真实 trial 大分片、当前消费者输入、
原 ac1、mean/native 和输出导数定义都保留。删除前完整文件 SHA 和
恢复来源见 `2026-11-14-R133-completed-regular-QR-cache-prune.json.gz`。
需要重新因子化时应在新 work 目录运行原 source，不能把已清理的
缓存目录当成仍可直接恢复的因子集。

## 2. mean/body 消费器的实际 parser 错误

首次运行旧 `fourfold_codazzi_mean_completed_head_body_residual.py`
在 `prepare` 读取真实 plain JSON 腰证书时，调用了从另一个模块
导入的 gzip-only `read`。实际异常为
`gzip.BadGzipFile: Not a gzipped file (b'{\n')`，返回1、时长
2.14608209秒，尚未执行任何真实径向行。旧 source 和失败过程记录
保留，没有重新贴成成功。

新 `fourfold_codazzi_mean_completed_head_body_residual_v2.py` 只按
文件的实际 gzip magic 接受原压缩证书或原明文 JSON。全 Fourier
产品、标量 mean 流、参数源、所有接口和原数学门均不变。新 kind
与新 producer SHA 明确区分旧对象报告。新 v2 已实际读入所有输入
并开始7721个完整公共闭格的 coefficient 阶段；这不是全域完成声明。

两个对应新入口
`fourfold_codazzi_regular_mean_completed_physical_boundary_v2.py` 与
`fourfold_codazzi_signed_nu_adjoint_pairing_v2.py` 明确绑定 v2 的
kind/source，采用同一真实 plain/gzip 读取函数。除此之外不改任何
物理转置、mean、幅度符号、双积分或跳项。它们须等真实完整 body
输出后才能执行，当前没有其原生完成主张。
