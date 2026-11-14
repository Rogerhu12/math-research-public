# 实际publisher的未来blob过滤设置

2026-11-13，作者 /root（GPT-6 Astra Pro，AI辅助）。原publisher持续普通push被远端并发推进拒绝，始终立即实际pull --rebase再重推，没有force。观察到反复约0.94GB重复fetch pack，但尚未证明传输原因。

Git官方 git-config 文档说明 remote.<name>.partialclonefilter 的变更只影响未来新commit的fetch；partial-clone 文档说明动态缺失对象fetch不作普通pack协商。参见 https://git-scm.com/docs/git-config 和 https://git-scm.com/docs/partial-clone 。据此，原独占维护helper在已完成Git命令之间将此唯一local配置从blob:none改为blob:limit=10485760，保留历史promisor，不重写任何ref或历史。

真实首次report为16:34:37–16:34:52 UTC、formal_success=true；变更前后204722个已索引OID标识及refs完全相同，OID标识流SHA 9a92255482ae93b203187a0da86d0255eb6b5b45cc0990ec659d20d54a75532e。这是索引标识/pack-trailer/ref核，不是每个对象内容独立解压重hash。旧新源、准备记录和实际report逐字保存。

随后仍有竞争拒推，也开始有新的普通push成功；这里不把时序当作配置导致性能改善的证明。原逐结论发布、每次pull核双README及失败立即rebase重推规则保持。
