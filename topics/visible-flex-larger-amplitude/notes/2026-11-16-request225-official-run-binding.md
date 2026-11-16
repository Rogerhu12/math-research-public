# Request225 官方启动与已发表源绑定

作者：ChatGPT（AI）。日期：2026-11-16 UTC。

## 实际发布与启动

[R527完整调用链](../results/R527-live128-paired-stage-and-radial-cache-complete-chain.md)及[接口](2026-11-16-request225-live128-paired-cache-original-full112-interface.md)的六件初始原文由本公开仓库行政Actions真实部分clone、pull/rebase、规则检查和普通push：

| 项目 | 已返回的实际值 |
|---|---|
| 发布行政run / job | 43852500565 / 133248350959 |
| 实际读取main | e8fcdc6926ee6381e82f6cd2f211811de21fb16b |
| 最后真实pull核规则 | 2026-11-16T10:51:09.7634965Z |
| 正式发布head | 5af07ed64877475bc05a488306246c9be22926bb |
| 实际科学head | 5af07ed64877475bc05a488306246c9be22926bb |
| 官方workflow / id | visible-larger-public-live128-paired-cache-original-fullDN.yml / 420014512 |
| 官方run / attempt | 43852521165 / 1 |
| event / branch | workflow_dispatch / main |
| 官方创建时间 | 2026-11-16T10:51:13Z |
| compute job | 133248437738 |
| 官方HEAD的root tree | 699e5b27e9b233703f59987b86f0ce75b64af89c |

真实pull后的根README blob21bd547f56590b7f2dd279d0297efb289a9b2783、课题README blobbff8aea253a9e6a7a4fac28d810ac454c5499fec均未变。HANDOFF记录该已读提交。科学run的head恰等于实际发布head，无需用相近提交或树局部相等替代同一commit。

行政程序在已push后，对已注册workflow只发一次POST，HTTP200返回本run及官方URL；没有根据push事件猜启动，也没有在未知响应后重发。该程序记录API version2026-03-10，dispatch_started为10:51:11.675210+00:00；行政工作流只在其分支，不进main。

## 原字节与运行范围

四个执行发布件保持初始完整身份：

| 角色 | B | SHA256 |
|---|---:|---|
| generator | 22915 | b30d418965454b63d5a0e8f6bc50277e38849e959e24ec92552bc722ec83a3ce |
| plan | 55391 | 6e8109e64bafb6e78428298ccc25a5b4d71df29c0b224b0ea20076da006dd1c6 |
| request | 64734 | 42fe3eff48338d540707c690d6aadd0cfdfeaa278a1145b1db885bea9df37285 |
| workflow | 18518 | 5ed7a2c3fd2fdab0d2fe02aeb050a07e3bfe8f3344b23ba3bd16f7573b274d53 |

10:52 UTC官方job metadata显示步骤1–10 success：原运行环境、14新source生成、原完整pin/语法检查、容量与输入恢复均已完成；步骤11“Fresh current-H fullJ R273 live128 original FD fullDN and final fresh audit”为in_progress。这些是步骤控制状态；不能推出任何native、FD、fullDN或final audit已经完成或通过。

R528由exact_refinement作为唯一终态读者；root未取任何科学日志。当前实际run不因后续main文档勘误而换源。初始R527说明中的338行序误述已另透明更正；原真实a090/08d48代码一直按slope112、second112、两个mean correction、height112，冻结请求的历史说明字段不参与数值索引。

官方证据：[科学run](https://github.com/Rogerhu12/math-research-public/actions/runs/43852521165)、[compute job](https://github.com/Rogerhu12/math-research-public/actions/runs/43852521165/job/133248437738)、[实际发布提交](https://github.com/Rogerhu12/math-research-public/commit/5af07ed64877475bc05a488306246c9be22926bb)。没有读取运行中科学日志、恢复未返raw或预填成功。
