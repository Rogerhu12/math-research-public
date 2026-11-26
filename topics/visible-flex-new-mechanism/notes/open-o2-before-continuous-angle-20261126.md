# O2 连续角峰实施前的完整已登记入口

逐字归档，原条件/范围/来源不撤。当前入口见主open。

### 新R566硬几何/动态径向计算

[完整实现与新输入](notes/2026-11-26-hard-geometry-exchange-implementation.md)已发布；两lane为原平行椭圆B.30/.38但fresh log-radius−.35/h.62，接实际振荡尾。所有球/条带/主曲率/高度/均E/行列式/镜像必要行保留，PhaseI只以σ未覆盖峰交换，PhaseII在完整fine几何可行内降η。[首run原终态](notes/2026-11-26-hard-exchange-first-run-restoration.md)已完整闭账：16外层全在恢复，fine V=.0058134/.0027596、κ16.4887/16.4387，Ebar/det谷底已受控但ball/strip仍略超，0metric阶段/OptimizeResult。[已识别末态续接](notes/2026-11-26-hard-exchange-identified-continuation.md)已发布：原81q/已付节点/trust逐项对原stdout核验；微小漏峰进入pending、后端返回时批量交换，仅显著缺口即时重启。120外层/80步、257×768容量、2400秒科学检查点；不重做fresh16轮，不放宽原门。[续接原终态](notes/2026-11-26-hard-resume-first-metric-progress.md)已付：B030 V=.00054365仍恢复；B038真实过fine几何并71次metric改善至η=.86360747，未达1e−6。两lane都以未采用的1536角提议超过768容量结束。[新联合预算及分块Jac](notes/2026-11-26-joint-budget-block-jacobian-implementation.md)已发布：R1.012/Y.3928/τ.06072保持主比例，新trust=.5明记，原末状态/实际及pending网格分开，B038实际纳1536角；本次首方向核对在Actions实际收费执行。新[连续θ峰接口](notes/2026-11-26-continuous-theta-peak-oracle-design.md)分开FFT积分网与真实约束峰角，保原完整Ebar/参数导数及求积误差；当前是明确后继设计，未改在途源。仍欠固定g精化和连续全闭reach。

[联合预算B030原终态](notes/2026-11-26-joint-budget-b030-first-metric-receipt.md)已独立闭账：完整新预算重建确过门后，真实fine η2.089589→.939818940292，V=0、κ16.452596，241×3072 fine；181.995016962新科学秒。真实119×1536、末119×3072提议未采用，仍角容量终态且无OptimizeResult。保此q/全部实际及pending点续接连续角峰；B038必须读自己的原终态，不混账。

[另一圆核设计入口](notes/2026-11-26-circular-core-continuation-implementation.md)单独发布：先在p=q=.18/offset.2只解17径向变量的几何，再以p同伦解锁81变量、逐阶段重新求完整门。其η0起点不付非圆分支；若小p步残差保持线性阶，转实际外端共振/seed，不以加迭代替代。所有p变化是换设计g，非同g弯曲。[首启动原失败](notes/2026-11-26-circular-entry-angular-guard-failure.md)发生在16角违反Model最小20保护处，尚无几何结果；新v2以32角/fine64首次真正执行，原模型/门/17变量策略不改。

