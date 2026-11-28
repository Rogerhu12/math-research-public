# R87 λ=.256/M32：完整存储回收分支的真实启动

首次 97ec 未接受场诊断已经真实返回 0、owned remaining 0 后，于 2026-11-28 19:43:20.006293 UTC 启动唯一新恢复，tool session 20732。输入仍是完整 nodal `97ec9d07c25d18cd7da7dbade7d5f0902fc1c48b3bbad2ee5b22abe432ed4279`；不把新诊断 physical 场当重启来源，不改变先前两步后的 x、Y、p、pscale，不重生成升模/割线。

独立入口 `prefix_reclaimed_csr_prefactor_qr_driver.py` 绑定 `complete_mapped_storage_reclamation_v3.py`。原完整 CSR/QR 的数值构造与原 solve、原残差精化及全部数学门保留。新存储类只在原 QR constructor 已返回而 factor mapping 尚未开始时释放空闲 allocator 页；以后每累计替换 16 MiB 原持久数组后再次释放，并在原 flush/MADV 操作之后对同一独占文件作 POSIX file-cache advice。advice 成功不等于实际 cgroup 计费已下降，真实观测另记。原 pre-J 和 solve 前后的 allocator 释放继续保留。

完整 RAM/disk 预算没有降低；实际 launch 门为 RAM 2,398,158,848 字节对要求 1,867,210,752 字节，disk 2,072,006,656 字节对要求 1,273,335,399 字节。运行时仍在每个实际网格和 QR 相位重新核门。新小存储日志保存在 outdir 的 `mapped-factor-storage-reclamation.jsonl`，位于旧限定 cleanup 目录外，不改变 owner/cleanup 合同。

目标仍为 `.256/M32`，角格 1024、q=warp=.012，RMS 2e−7、物理 BC 2e−9、metric 1e−6；原唯一 metric 审计观察器保留。该记录只登记精确来源、真实启动、literal 状态核验及首个实际 pre-J 门，不宣称新的 Newton 步、BVP 接受、存储峰改善或曲面完成。最高真实全门锚仍为 `.128/M24`。

完整原命令、全部绑定源 SHA、actual start 行哈希、literal 输入回执与资源门见 [JSON](2026-11-28-design-r87-lambda256-reclaimed-storage-start.json)。
