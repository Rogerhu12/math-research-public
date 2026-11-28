# R87 λ=.256/M32：新存储类进入之前的真实工程终态

此记录接续冻结的 [新存储分支启动](2026-11-28-design-r87-lambda256-reclaimed-storage-start.md)，不回改启动事实，也不将这次终止称为新存储方法的实际失败。

唯一 tool session 20732 于 2026-11-28 19:45:46.779515 UTC 真实 join：原 child −9、tool 247、owned remaining 0，运行 146.78939088300103 秒。实际子进程最大 RSS 为 514,424 KiB，observer 最大采样单进程 RSS 为 432,369,664 字节。

本次原初始域门、literal 完整状态身份、首个 pre-J 资源门真实返回。随后没有完整 CSR assembly-return、factor-start、factor-return 或 solve 记录；没有新的 Newton 接受步、raw/RMS 或 metric 返回。新 `mapped-factor-storage` 目录和 `mapped-factor-storage-reclamation.jsonl` 均未创建，唯一 mapped/QR trace 各只有声明安装事件。因此，独立 reclaimed-storage 类尚未进入，不能根据本次结果评价其实际回收效果。

最新保存的完整 pre-J x、Y、p、pscale 仍逐字节为 `97ec9d07c25d18cd7da7dbade7d5f0902fc1c48b3bbad2ee5b22abe432ed4279`，1185×97 状态与 32 个参数完整保留，先前两步没有重做。真实 join 后的限定清理返回 `store_created=False, removed=[]`，没有删除原场或科学证据。

现有观测只能把终止置于完整偏导/CSR 返回之前的计算阶段，不能进一步确定是哪条分配或表达式。cgroup 限额/事件仍不可读，−9 原因未证，不能称数学失败、已证 OOM 或某个固定进程内存上限。没有继续同布局自动重启，也没有 λ 二分；最高真实全门锚仍为 `.128/M24`。

下一独立资源路线针对早于 QR 的真实完整 node/midpoint dY+dP 常驻和 CSR 输出，不删任何模式、节点、参数或方程。其实际实施/验证另记，不以准备替代计算。全部终态、资源门、精确原命令/来源与输入 SHA 见 [JSON](2026-11-28-design-r87-lambda256-before-reclaimed-storage-actual-terminal.json)。
