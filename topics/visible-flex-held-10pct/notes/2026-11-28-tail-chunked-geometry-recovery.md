# 原全谱 geometry 的分批恢复已实际接续

旧整批原 exporter 在写完 stage 1151 至 1063 后 child 返回 −9；89 个完整 gzip 文件与 partial manifest 逐文件哈希匹配，没有额外未登记 stage 文件。退出原因未确定，未触发磁盘等待门，也没有数学异常栈。本次保留这 89 个段的原字节，不重算。

第一版分批入口随后令原 exporter 实际完成 1062 至 1047 共 16 段，原 child 返回 0，其 15 个内部公共节点检查均成功，耗时 14.418 秒。此后 Python 记录峰值时，局部字典 `resource` 遮蔽同名模块，触发 `AttributeError`；这是我新增 bookkeeping 的错误，不能叫 Node 或数学失败。该首批 16 段的成功原 manifest 和全部字节亦保留。

独立 `chunked_tail_geometry_resume_v2.py` 用 `process_resource` 模块别名纠正该错误，并从原 controller 的真实 completed/returncode=0 记录继承首批 16 段。它把原 89 + 首批 16 的全部文件、完整谱、完整 mean-chain、相邻 literal 半径与 Cartesian/Fourier 二阶 jet 逐项核对后，从 **stage 1046** 接着做，未重算这 105 段或原 stage0。

v2 的第一批实际完成 1046 至 1031 共 16 段，原 child 返回 0，耗时 **14.764439438 秒**。该时刻真实 `getrusage(RUSAGE_CHILDREN).ru_maxrss` 为 **343,660 KiB**，是此 controller 已等待 child 的累计最大 RSS，不是先前失覆盖的 `/proc` sampler。后继每批最多 16 段、Node heap 512 MiB，并继续在每次真实落盘前保留 128 MiB 磁盘门。

每一批均运行未改动的原 exporter：同一完整真 full-H 包、同一全局原 mean-chain、170 个 planar 模与 25 个 height 模全部保留。新批内端只复制上一个实际段的公共外端，原 stage0 的内端一直作为 node1 的实际锚点；每一对相邻段还会重新按字面核同。所有 source、真实 child 返回、保留文件清单和小进度快照均有独立哈希；原 partial child 从未被改标成完整成功。

此条登记实际分批恢复和资源测量，完整 1,152 段 bundle、全尾连续认证和深端 collar 仍随主链继续；不把已恢复的部分段当完整尾或闭图。
