# Git 同步只读诊断

本包只整理本地配置、既有发布/维护日志及一次已授权认证的 `ls-remote` 协议记录。没有由本代理发出 pull、fetch、push、Git 配置写入或对象库变更。

## 实际证据

18:17:37 的主代理记录证明 `remote.origin.partialclonefilter=blob:none` 写入退出 0。18:23:56 开始的维护作业又实际执行 `config --local remote.origin.partialclonefilter blob:limit=10485760`，同样退出 0。18:47:49 在唯一工作仓库读取的有效配置来自 `.git/config`，为 10 MiB；协商算法仍为 skipping。该明确的后续覆盖足以解释配置差异，无需假定环境恢复回滚。

认证只读 `git -c protocol.version=2 ls-remote origin refs/heads/main` 退出 0，用时 6.73925551299908 秒。原 packet trace 广告 protocol v2 和 `fetch=shallow wait-for-done filter`，证明服务端支持过滤协商。仅启用 packet trace，未启 HTTP trace，未将令牌、认证头或环境保存到文件。

## 可用范围

原 ls-remote 没有发送 fetch，也没有 have/ACK 协商，因此本包不能断言反复 1.1 GB 大包的完整原因。每次命令显式覆盖过滤键可以避免本地配置被维护程序覆盖；这只是配置控制办法，性能须在主代理原有正常 pull/push 流程中实测。主代理随后选择的 1-byte 阈值也没有在本包接受性能验证。

17:35 至 18:48:33 的既有事件快照保留每次完成的 pull/push 退出码和时间。18:47 后普通 push 已连续成功，若干 pull 仅 4–5 秒；不把该变化归因于未受控的单个配置因素。远端写入与维护耗时也会影响拒推窗口。若大包复现，可在下一次主代理原本要执行的 pull 上附加 packet trace，不能为了诊断另发 fetch。

本包消费器重新核对上述已保存证据，正式退出 0；它不重发网络请求，不能把消费器资源当作原网络探测的 CPU/RSS。原 ls-remote 只测了退出码和墙钟时间。
