# 条件增长首轮：计算完成，结果日志被开发诊断长度门阻断

本记录对应公开 Actions [run 43680023529](https://github.com/Rogerhu12/math-research-public/actions/runs/43680023529)、几何 job 132708447996、源提交 9b7c07f25514808595dcf4efe7e79220fc57a8d6。它记录一次**结果提炼失败**。现有证据确认新人工检查通过、请求的计算程序正常返回、来源与输出哈希发布完成；现有证据不包含本轮接纳数、增长次数或最终几何门，不能据此宣布算法改善或数学失败。

## 1. 已发生的阶段

| 阶段 | 公开结果 | 可据此得出的范围 |
|---|---|---|
| 真正 pull 并检查双 README | success | 运行前规则检查已执行 |
| 新接口人工检查 | stdout passed: true | 此版增长库及 driver 的人工入口已通过 |
| 请求的有界几何计算 | stdout complete-two-grid-fixed-curvature-spectral-trust-growth-audit；步骤 success | 程序完成并产生临时报告；status 不推出门通过 |
| 小摘要生成 | success | 原生摘要在临时目录生成 |
| 人可读结果日志 | failure | 尚未打印科学 model/trial/gate/growth 表 |
| metadata-only 发布 | success | 仅 receipt 被提交，没有报告 payload 或 Release 资产 |

人工返回的日志时间为 2026-11-15 05:13:05.687 UTC；计算返回为 05:22:08.142 UTC。两条 stdout 之间约 542.454 秒是作业观察到的间隔，不等同于优化器活跃时间、报告内准备时间或共享预算使用量。后三者未能从本轮日志读取。

增长库 frame_metric_spectral_trust_growth.py 的 SHA256 为 19394bea4779c4497851c169a15dddad5839469067d550f64bef7af3bb88dcc6；driver frame_metric_spectral_trust_growth_audit.py 的 SHA256 为 801f1c3038d54dec422e9d8e3bb1162105fc560374debb5bf83a8b38083be3e6。

请求保留既有固定度量、固定高度参考、163 参数、双网格门和 12 LP / 40 值评 / 120 优化秒预算，新增下一模型的条件增长规则。这里确认的是代码与请求定义，并未把未知的实际退出原因填成预算耗尽或收敛。

## 2. 日志失败的确定原因

失败 traceback 来自 print_research_outcomes.py，运行版本 SHA256 为 354fa7a80c7b4a5e219cbdb11d1150db9b95ac1f6bceae686e67e0ebe70eb603：

1. main 先调用 print_development_diagnostics。
2. 函数递归展开开发报告内所有布尔字段，包含内部 toy 模型、试探与条件记录中的重复值。
3. 开发日志超过 20,000 字节，在打印前抛出 ValueError: development observation log exceeds 20 KB。
4. 科学报告的读取和打印排在该调用之后，因此没有执行。

这不是人工检查失败：它已返回 passed: true。它也不是几何计算超时、异常或不可行性的证据。作业最终 failure 来自独立的只读观察器。

不能根据输出报告约 8.7 MB、摘要约 75 KB 或正常返回，倒推出模型数、接纳数、全网门、增长动作及最终误差。这些仍需实际结果读取。

## 3. 已保存的元数据

公开 receipt 路径为 notes/actions-43680023529-1-metric_spectral_trust_growth/receipt.json。它保留来源、请求、run 及以下临时输出身份，所有 payload_published 均为 false：

| 临时输出 | 原文 bytes | 原文 SHA256 |
|---|---:|---|
| 完整 audit | 8,733,103 | 1dc16d03cb6b8be33c0aaea25eadb8cb410c3d909e66dd48b28d253df13d3149 |
| 原生 summary | 74,795 | 21e8a9ca1ccb7dfc70bd9b2ac2a3b5faffeb12f19000f36d2816a55ff9120b81 |
| development | 98,567 | ff801919e55e0a062ecd72e83a98ae41bfb6240795d66076e79c0e36d54f7ef2 |
| pre-research pull receipt | 253 | d64c11b675669aff88a8c6daa71a58fd8d87e1e8aa8add5b81cc4978e2762593 |

receipt 的 gzip SHA 使用其标明的流式虚拟 gzip 规则；它不是已上传文件地址，也不表示压缩数据被保存。

发布器完成真实 pull/rebase；发布 pull 的 HEAD 从计算源变为 7738878ccf32de1c5294e476341b0205b3ab1cf9，双 README 无变化，远端 main 是 HEAD 的祖先且没有进行中的 rebase。研究执行源仍是 9b7c07f…，不可将发布时 HEAD 写成计算源。

根 README 第 15 条禁止保存可重算数据、证书和 Actions payload。因此本轮没有将完整 audit、summary 或 development 放入仓库、Release 或 artifact，也不能改名参数或分块保存来规避。

## 4. 最小修复及恢复范围

观察器修复只处理已知故障：

- 开发日志打印顶层及直接子检查器断言，不递归展开内部 toy 数据；标题明示范围。
- 科学结果先打印，开发诊断随后处理；开发诊断异常不再先吞掉科学结果。
- 保留科学 35 KB、开发 20 KB 总门，不用静默截断隐藏失败。
- 增长库、研究 driver、物理定义、容差、目标及预算不变。

新增只读打印分支可单独编译或用人工文本覆盖，不必重复旧几何人工链作为数学门。

原临时科学报告未持久化，后续公开恢复须按绑定源码、参数和原合法输入重新执行必要计算，再在同一 job 中读取临时结果。这是取回被观察器错误阻断的证据，不是新算法改进或第二个独立成功样本。新的 run、时间字段与 raw SHA 必须如实记录，不得伪称新报告与原报告逐字节相同。

在读到恢复结果前，本轮结论停留在：**增长实现的人工入口通过，计算程序完成，实际几何结果尚未提炼。** 精确等距、完整嵌入及全曲面 reach 均未因此认证。
