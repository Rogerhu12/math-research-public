# 旧 strong post43 记录的原字节恢复

2026-11-14，root，AI辅助。

按照只读旧工作区的 successor-strong-transfer 清单，本次将90件共3,767,902字节逐SHA恢复并保存；完整路径、长度和哈希见 `2026-11-14-strong-post43-recovery-manifest.json`。这是过去本地计算的记录保全，没有重新运行数值求解，也不宣称它们是本次公开 Actions 产生的新结果。当前用户授权已明确允许本公开仓库提交与本仓 Actions；原历史文件里的审批状态不作为当前阻塞。

这批记录包括原iterate-H提取、half-trial高角诊断、第四轮SIGKILL记录、同一完整H实际尾审计及R6前缀重启。历史完整H审计确有原exit0、全J/full audit和residual约1.19748e−10；后续R6确已生成J/QR，但在共享磁盘实际ENOSPC后被主动SIGTERM，退出143/owned_wait4−15，绝无新增前缀接受。两种状态都保留，不能将计算曾进入QR冒称求解成功。

原完整raw前缀分块并未都包含在这90件内。manifest明确 `all_original_raw_prefix_chunks_archived_here=false`，列出三个仍在旧只读工作区的 recovery index。因此本包是可核对的历史记录和部分恢复输入，不伪称可移植的完整接受checkpoint。

主线使用本公开仓已接受的大核.99输入和完整DN接口，不为保全记录而恢复这条旧小幅half-step支线。需要其中实际输入时须按索引重新取得完整原字节；新计算仍只使用本仓 GitHub Actions。
