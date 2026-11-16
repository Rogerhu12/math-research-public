# Request228：正式发布、唯一dispatch与实际源码绑定

2026-11-16 UTC，/root（AI）。本件仅官方Git/Actions元数据，不是科学结果。

R540七件正式发布于 e5af240e3f596c8b26201950e0c66141b73977fe；source commit 8f0d282286983e0391a70a847799898fd5acc2bf。公开仓库行政run43858592184/job133269175651成功，真实pull最后读32876b3c3f1c1846d916fdfee69f6eaa966b183f，双README未变。

注册后只发一次官方workflow dispatch，API2026-03-10实际200回执：workflow420049210 / visible-larger-public-thirty-nine-semantic-relation-batches.yml，2026-11-16T11:32:15Z 创建 [run43858623707](https://github.com/Rogerhu12/math-research-public/actions/runs/43858623707)，attempt1，event=workflow_dispatch。没有不明重试或第二次派发。

官方实际head是 **99f4ee650e031448e9fcb33ead672e48a8babd3d**，它是发布head的直接子提交，message为原current576规则同步。两头根Git树与课题Git树逐项对照：

| 范围 | 两头实际身份 |
|---|---|
| 整个computations树 | a86dfc032fa1b529648ae56cce53e7bd672b8a56 |
| 整个.github树 | dcd301be4e003bea03d320a0826f2a50627da6ed |
| 根README | 21bd547f56590b7f2dd279d0297efb289a9b2783 |
| 本题README | bff8aea253a9e6a7a4fac28d810ac454c5499fec |

本题唯一差异为HANDOFF.md：9863 B / blob516321c45ff6d94d7dfe6975f29fe0dcf3b7d988 改为9816 B / blobad41f9f4e83e4132ad6cc2088df3cf294f904ec9。两份完整文本文行数相同，唯一差异为第7行规则同步记录，更新成11:32:10真实pull已读e5af240e3f596c8b26201950e0c66141b73977fe；其它所有文本逐行相同。原topic整树因此不同，不误称整个topic同字；实际执行源、请求、recipe、plan、工作流及双规则均同字。

11:33:44 UTC 官方状态queued、jobs空；这个时刻没有科学步骤、日志或完成结论。此后由 exact_refinement 独占R541终态必要日志读取，并记录真实job/范围，不由本记录预填启动、适配90000或任何trial结果。另在运行的225/R528同由其独占；root不重复取科学日志。

完整入口见[R540](../results/R540-complete39-lossless-semantic-relations-original-eight-pair-entry.md)与[228接口](2026-11-16-request228-complete39-lossless-semantic-relations-interface.md)。每个科学body仍原单90000B/70、原八组完整39/freshFD/原owner与quiet；不能因官方派发成功而把这些条件记为已过。
