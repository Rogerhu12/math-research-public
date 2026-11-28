# G12/G14 第一次真步被 SIGKILL：准确输入保留，未产生新场

日期：2026-11-28。实际执行回执记录：新 query 的完整 source-bound 绑定 exit 0/82.493805262s，准确暖转移 exit 0/5.091342096s；随后 `actual-H2-increment-direct-LM` 子进程在 612.993204925s 返回 **-9**，driver 最终 exit 247，`finished=false`。没有 accepted-step 日志，也没有完整 result 或 field。不能把这次退出计作收敛或数学失败。

当前 namespace 看不到已死进程的历史 RSS，且没有可读 cgroup memory.* 计数，因此只据实称系统 SIGKILL，**内存压力是待解的嫌疑，不是已经证明的原因**。代码中确有一个具体可消除的浪费：完整 Gram 装配后还先构造 eta-H1 factor，H2 核随即删除，再复制 raw Gram 构造真正的 H2 factor。该配置每份 band 为 753,051,648 bytes，G12 的完整物理一阶缓存又比 G6 加倍。

全部准确输入已保存：原 source 数学定义、g、参数/时间范围不变；新 13,185 半径 cache、原源连续界、487-span/G12 grid 和暖转移场均完整。暖输入 field SHA `6aafee941eefdada991efa93316f89f9ddbdcd57f05c8bf33a51d19fe74e3d61`。

中断遗留 244 个训练 source packet，共 682,329,624 bytes。现逐一按完整实际 radial-block/N768 key 找回，所有 NPZ CRC 读取、dtype、shape、finite 检查通过。逐文件 SHA256 已写本地 postmortem ledger；这些摘要是在 SIGKILL 之后登记，不能伪称已有进程退出前的完整摘要回执。恢复输入与新计算应继续由明确哈希和原 evaluator 保证隔离。

下一实步保持原目标与该暖输入，只改变内存布局/装配方式：去掉未用 H1 factor，准确完整 Gram 以一份 Fortran band 原地加 H2 增量正则并因式分解；若 lambda 重试，必须重新装原 Gram，不能把已因式分解矩阵当 raw H。此修复的实际一致性检查和同输入重跑另记；M64 未在原高内存配置上启动。

- 失败回执：`d453b7417b221c01e772d885ba24c3817c3487ca448450e61ba3d9d61200dbbe`。
- 原 driver 执行回执：`36bd2d0da95ad2717675476a82b0d27f3c880589ab3cdc0f2771777cbecdfd7a`。
- 原 driver 日志：`168fea132dc31925f0172e02724bbd82c82c4c4c3cf685ffcbff4c2c90b1dbad`。
- 遗留 packet 事后完整性 ledger：`af9fb7c098363b30af9c2b9dc384dd469eab6af610fb373c3099f28f359272c6`。

原始 packet、源数组仅留 scratch，不进入 Git。课题继续，当前可消费完整新场仍为已保存的 M48 场。
