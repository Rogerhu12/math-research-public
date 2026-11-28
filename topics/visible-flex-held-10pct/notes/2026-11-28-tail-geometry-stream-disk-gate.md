# 全谱几何链的真实逐文件磁盘门已运行

完整尾几何继续使用原 `seam_run_tail_geometry_v2.py` 和原导出/认证算法。新的独立 launcher 在 `tail-fullheight-ulp-geometry-all-20261128-a` 初始化原 stage0 summary 的逐字节副本，所有已经完成的 stage0、共同 mean-chain、source/H、完整谱与证书仍指向原绝对路径；旧 stage0 summary 和资源记录绑定的哈希因此保留。原 contract 比较正常执行，没有重算首段。

空间控制只在落盘入口增加：Node preload 包装原 `fs.writeFileSync`，Python launcher 包装 `Path.write_text/write_bytes`。每次写入前按真实待写字符串/缓冲区长度检查 filesystem free 是否至少为“本次字节 + 128 MiB”。不足时保留已算好的当段数据在内存中等待，空间恢复后执行同一次原写入；没有跳段、删模、缩问题或改变任何数学数值。所有真正 child argv 仍由原 pipeline 保存，额外 launcher/guard 的完整源哈希保存在独立 execution 记录。

两运行时已实际写回 UTF-8 文本和包含全部 256 个字节值的二进制，与原字节逐位相同。这个小核验只确认真实写入口及字节保持；不声称曾人为制造满盘，也不声称消除了其他 workspace 同时写入的竞争。

真实 continuation 已写出 89 个完整剩余 stage（1151 至 1063）后，原 exporter child 返回 −9，controller 返回 2；没有数学异常栈，也没有触发磁盘等待门，退出原因尚未确定。89 个实际文件和原 partial manifest 完整保留，小 JSON 绑定真实终态、源清单和首个实际段；不把工程退出称为数学失败，也不把部分数据称为全链完成。后继将按独立原进程的小 chunk 继续，并核验保留所有已经写出的段。全 1,152 段、共同 mean、170 个 planar 模和 25 个 height 模全部保留，后继原连续认证和深端 collar 检查照常执行。
