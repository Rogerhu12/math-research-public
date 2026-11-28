# R87 λ=.256/M32：一次空闲页释放恢复的真实终态

此记录接续 [完整状态恢复](2026-11-28-design-r87-lambda256-interruption-and-allocator-recovery.md)，不覆盖已冻结启动回执，也不把工程终止列为数学排除。

唯一恢复 tool session 77523 在 2026-11-28 19:29:50.254761 UTC 真实 join：child −9、tool 247、owned remaining 0；运行 131.008228913 秒，子进程最大 RSS 794,052 KiB。原初始域门和完整 CSR 组装已经返回；外层 factor_start 已记录，没有外层 factor_return、solve 或新的 Newton 接受步，也没有 RMS/metric 返回。

这一次 pre-J 的实际匿名 RSS 从 137,035,776 字节降到 87,875,584 字节；RSS 从 156,168,192 降到 107,024,384 字节。已用 `collect_and_trim` 的空闲页释放实际生效，但不能据此断言全流程峰值已解决。不同尝试止于不同阶段，不能把两个终态峰的差直接解释为算法总峰降低。

真 join 后，仅检查并清理本次独占的暂存目录。实际发现 CSR backing 312,283,136 字节及其 layout，另有 factor backing 398,401,536 字节而尚无 factor layout。由冻结 `BeforeQRMappedBlockQR.__init__` 的顺序，后一文件只能在原完整 QR constructor 返回、CSR 清页之后创建；因此可推知本次已进入随后的 factor-storage 映射阶段。这个源码与文件生存期推断不等于记录到了外层 factor_return，也不解释 −9 的原因。清理记录保留路径、真实字节数和现存 layout SHA；仅删除可重生映射暂存，不删字段、源码或检查点。

本次保存的完整 pre-J x、Y、p、pscale 与前次两步之后的文件仍逐字节相同，SHA 为 `97ec9d07c25d18cd7da7dbade7d5f0902fc1c48b3bbad2ee5b22abe432ed4279`；全部 1185×97 状态与 32 个参数保留。最高真实全门锚仍为 `.128/M24`。没有自动同布局重试、λ 二分或重新生成双源升模输入。

现有 cgroup 限额与事件仍不可读，原因未证。完整小终态、原 CSR/QR/资源相位、实际 allocator 数值、来源 SHA 和限定清理证据见 [JSON](2026-11-28-design-r87-lambda256-trimmed-recovery-actual-terminal.json)。后继仍须通过全部原数学门。
