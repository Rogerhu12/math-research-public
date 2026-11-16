# 原 E20 常数入口首次系统终止记录

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted GPT-6 Astra Pro。

实际执行来源为 `2026-11-16-r150-original-low-commutator-twenty-exact-constants-789f.py`，blob `58d3fec8f3a1e709d84bcbebb01b68dda60f1609`，30312 bytes，SHA256 `5d312e6b5255cb74e0f5a05753fd1f951b6a24f753d119ace2f52627696ae8cb`。数学预算 180 秒、地址空间上限 1024 MiB，外层墙时 240 秒；仅请求 `constants`，没有请求最终二十维精确解。

本地执行 session 16280 的真实退出码为 **137**，shell 报 `Killed`。没有 Python 最终 raw、manifest 或已登记的完整常数 phase。唯一 stdout 事件是 `original-physical-model-rebuilt`：事件相对用时 1.1135593490034807 秒，所报峰 RSS 75140 KiB。这不是整个进程的最终用时或最终峰内存。

原 stdout 共 99 bytes，SHA256 为 `bc403e71d38c5cdea94b9dcc9999db6bec9d5cc44c4f7ea06ba3655dc5f4185d`。原输出目录为空，原日志保留。它只记录原物理模型在该事件之前完成，不能据此认领完整数域常数、二十方阵、候选或乘回。

退出后只读系统信息显示 MemAvailable 为 1219688 KiB，无 swap；该执行环境没有暴露可读的 cgroup `memory.events`。现有材料不能精确定位系统终止原因，也不能从 137 推出数学核验失败。原常数阶段多个数域有理多项式消元之间尚无阶段事件，因此不能猜定某一个逆就是终止点。

后继拟采用独立版本，把六、五、十一维数域逆改为相应的 $18,15,33$ 维忠实有理表示求解，并增加逐逆候选/完整乘回检查点。这是待独立审读的资源与诊断改进；原对象、全部来源、两向乘回及 place 单位门不减少。原版本失败身份不被覆盖，不空续为成功。

本记录没有新的数学负结论，也不影响另已证明的原 E 二十低交换子因子化定理。精确执行身份为 `notes/r150-original-parameter-module-execution-789f/local-20261116-original-low20-constants180-terminated137.json`；所有原数组和 raw 仍不入仓。
