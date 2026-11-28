# 原连续 metric 证据恢复及独立 v4 续接（真实工程记录）

环境恢复后，旧 session `79580` 的恢复接口没有返回可确认的退出码；其 `summary.json` 历史字样仍是 `running`。本次只观察到旧进程身份不再存在，不能由此推断 exit 0、失败或信号。逐字节读取的旧 B summary 已实际保有 **62 个完整阶段（0–61）**，比断联前最后已知状态多一个阶段；stage 62 尚无已付叶。旧退出码继续记 `null`。

独立 recovery observation 保存了旧 summary 原字节、原 source/contract，以及 A/B 两目录已存在的 **526 个证据 JSON 文件**的实际路径、字节数和 SHA256。旧 v2 的真实 exit 130 存储交接仍是它自身记录，不挪作旧 v3 的退出码。

## 实际后继

新独立 `tail_metric_complete_supplement_recovery_v4.py` 读取上述 observation，核原 v2/v3 数学合同、全部继承文件和每个完整阶段的精确覆盖及原门后，继承全部 62 个阶段。它没有重算旧 Gram/Taylor 结论，没有变更实际场、完整谱、共同 mean、target 或 `1e-6` 门。每次小 JSON 写入仍保 **16 MiB + 本次待写字节**；原大型 geometry 的 128 MiB 门未改。

两次实际启动错误保留：恢复环境缺 `/usr/bin/time`，shell 在 Python 之前真实 exit 127；随后手工 CLI 将三个已冻结 seed summary 顺序调换，严格数学合同核验真实 exit 1，尚未写任何新证明。修正为原顺序（stage24/span15、stage24/spans0–14、stage16/all），冻结源码未改，即在全新 D 目录真实启动 session `47300`。这些均不是数学反例。

最新工具恢复明确仍返回该 session 标识，未返回退出码。随本记录冻结的真实后继 summary 已有 **86 个完整阶段，末阶段 85**，其中原 62 阶段完整继承；后续原连续证明继续。一次仅按进程名称筛选所得空列表没有足够进程身份信息，不被解释为终态。实际 source/contract/summary 快照和错误日志 SHA 见同名 JSON。

## 聚合入口范围

同时恢复的 `closed_map_complete_metric.py` 原字节 SHA 为 `4a2a799b49f01d8eb70925b4cf406d7ef39192f1faf80448fbf73cf3216d6fad`。它尚未作正向执行，原版本只识别 v2/v3 合同；新的 v4 完整继承链将由独立后继入口严格核验，不能通过跳过来源门来使用它。

本记录不声称完整 1152 段 metric 已付、不声称完整闭图 metric 已付，也不声称题目 README 完成。原完整 geometry、前缀/cut、placement 和已付局部结论保持各自既有范围。
