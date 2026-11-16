# Request218 — 真实发布、官方启动与首次运行绑定

作者：ChatGPT /root（AI）。2026-11-16 UTC。只记录实际来源与任务元数据，没有读取运行中的科学日志或预填求解结果。

| 项目 | 真实值 |
|---|---|
| 正式入口发布提交 | 44f5f282f0154cce3e23fe873d3f220c5e39e9fe |
| 科学run / attempt | 43830433500 / 1 |
| 实际科学source commit | 0f101b697beb04db9bf6c225a488755e191f3a54 |
| event / branch | workflow_dispatch / main |
| 创建 | 2026-11-16T08:20:32Z |
| workflow id | 419881031 |
| compute job | 133174205129 |
| 唯一终态读者/结论 | amplitude / R507 |

[实际run](https://github.com/Rogerhu12/math-research-public/actions/runs/43830433500)；[实际compute](https://github.com/Rogerhu12/math-research-public/actions/runs/43830433500/job/133174205129)；[完整入口接口](2026-11-16-request218-zero-linear-gzip-complete-chain-interface.md)。

公开恢复Actions run43830091210/job133173073074在08:17:57–58真正git pull --rebase origin main并核两README，已读a07453ec81e832b0aeef99bded2efaa763adaf13，两blob仍根21bd547f56590b7f2dd279d0297efb289a9b2783、题bff8aea253a9e6a7a4fac28d810ac454c5499fec。08:18:00实际Git推到上述44f5提交。

紧接的第一次官方dispatch在08:18:00.7209287Z真实HTTP404，没有run ID；之后按44f5查询实际run列表为0。默认分支workflow全文确实为92730B/1c32571314db923c2beb8ca61df47214b2826dd0cebeca92b63426701cd5c3fa。因此不把这个行政HTTP失败当作科学执行或原门拒绝。

明确行政重试run43830418320/job133174147952先GET真实workflow，08:20:30.2003685Z返回id419881031、state=active，登记created_at为08:18:00Z。先核同workflow实际dispatch run集合为空后，仅一次POST到其数字id；08:20:32.9543521Z返回HTTP200和真正workflow_run_id43830433500。行政两个run都不混入科学编号；未盲目重发一个可能已经成功的请求。

官方科学run实际head是0f101b697beb04db9bf6c225a488755e191f3a54，不能冒为入口最初发布44f5。根端在这个准确head分别取回并核完整entry：request95251B/8945e38bd7dec8ad72355515b09051f88ff275fb14ab888b1cfad654efc7a615，workflow92730B/1c32571314db923c2beb8ca61df47214b2826dd0cebeca92b63426701cd5c3fa，与正式两件逐字身份一致。

08:21首次官方jobs仅显示compute前1–6成功，step7临时容量进行，8起五层源生成及之后科学尚pending。这里不据初始化成功宣称生成闭包/原C/全部far/BVP/450/精化/几何/读回已完成。唯一owner继续看终态；不得从此记录补任何未返数值，也不另取运行中大日志。

原全部272+133来源、18900+2700唯一钟、32GiB原门、完整453→450→五因素→M128及全必要/quiet/90K责任见原接口，均未因404和启动重试改变。R503新点另属220，不更改218。
