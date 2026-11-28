# M32 v4 的真实日志异常与独立 v5 原状态恢复

v4 已实际返回 exit 1。它在 151.212504 秒抛出 `TypeError("dict() got multiple values for keyword argument 'seconds'")`；父进程实测总用时 151.918382 秒，子进程峰 RSS 872124 KiB。这是本次新资源日志回调的接口错误，不能登记为原数学边值问题失败。

原 1497 点 nodal Jacobian 与 1496 个中点 Jacobian 均已实际返回。direct CSR 在构造完成时把其 `seconds` / `maximum_rss_kib` 通过回调传给 wrapper，而旧 `event` 同时显式给定同名字段，故记录抛异常。异常发生在第一次 factor 之前；`factor_count=0`，没有方向、Newton 步、原 raw_return、physical 返回或 metric audit。不能把两次 Jacobian 求值当成一个 BVP 接受结果。

新的完整 nodal 检查点已在这次 J 前实际落盘：`last-nodal-jac-input.npz` SHA `4da6eaef2a2d7c9b0139df225b0cd1a63b69d95689ee6b9fc4fba5acef63e010`。其 1497 点 x、97×1497 的 y、32 个 p、31 个 pscale 与第二次中断留下的真 nodal 状态逐位相同；源码入口核对也已实际执行。完整源、终态和数组 SHA 见同名 JSON。

旧 `fixed_support_literal_driver_v4.py` 保持 SHA `c678f8c9fc3f5b878ee389e7cf36353f7267b2bd071184cb49c43d9c5ad77553` 不变。新独立 `fixed_support_literal_driver_v5.py`（SHA `213ed5dffdb3925cdae43c22c0d1ac1fe6496f7c42a92ce254ddc99952ae85d7`）仅把 assembler 日志映射改成 `event(..., assembly=fields)`，保留内部全部原字段，避免覆盖 wrapper 自己的时钟/RSS。除文档版本标记外，源差异没有其他修改；原 direct CSR、完整 QR、物理未知量、固定 g、mean1168、初猜数组和全部原门均不动。

在实际 v5 求解前，用设计链已真实保存的一条完整 M48 direct-CSR 记录（包括真实 seconds/RSS）回放了从 v5 源 AST 提取的原 event 函数与 callback。实际回放成功，嵌套字典与输入记录逐项相等，外层仅有事件名/自身时钟/RSS/assembly 四项。它没有再构造矩阵、没有伪造场或运行额外数学探针。

v5 随即在同一个已授权独占前缀 J 窗口启动（session85064），沿已核同一原 1497 nodal helper 输入继续原 BVP；没有重算 helper、没有推断新的中点初猜、没有重新铺网格。此记录时 v5 尚未有终态或接受结论。原两个 exit137 与本次日志错误分别保留，不能被入口修复抹掉。
