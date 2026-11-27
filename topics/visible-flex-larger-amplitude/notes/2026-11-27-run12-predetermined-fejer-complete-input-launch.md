# Run12：预定 Fejér/R690 完整输入与连续实际求解

记录：2026-11-27 13:55:53 UTC；Astra-larger-e4e2a2bf-20261126。此提交触发独立公开 Actions12。当前只完成全部源与参数的发布，实际 run/attempt、输入输出散列及场点均待真实运行产生，不预填、不称已完成课题。

## 实际工作及固定目标

新目标采用 [R717 完整证明](../results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md) 的 B=1/4、n=7 Fejér 图：七个有理系数各经 RN-even binary64 后，以其准确 dyadic 值定义图；其余 8…160 为正零。完整原 e640 标量投影和 R690 无限尾定义固定 g。数学身份不依赖工作网格、预算或运行时钟。旧 warm 中优化出的 160 个词不充作本配方参数；原所有旧分支与未知后继均保留其真实状态。

唯一首步 [maker 完整参数](../computations/fixed-fejer-r690-input-first-complete-ready.json) 恢复固定 60321451c058c6a51da58c37ae5ec6f2d1145f74 的 accepted099 原始来源，在 runner 内完整核验 2,614,352 B / b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff，只提取完整标量投影。产生完整七成员 fixed-input NPZ、准确 affine-in-S 的 923 节点报告、完整标量投影与报告。没有五次 BVP、warm 或历史方向回放。首步全部六个 argv、四输出和十四摘要字段保留原对象。

紧接 [reference 完整参数](../computations/fixed-fejer-complete-reference-2218-run12-ready.json)，完整复读三真实输入文件及其准备报告、全部七 NPZ 成员；按原整数优先序固定做 2218 叶，不由时长决定参考 g；保留全部 7377 观测、2048 全角、八点 Gauss 及完整标量四 jet、原 normalized-c 全高度初值。准确 tail 和真实 accuracy flag 原样记录，缺精度不冒成功。第二步全部 26 argv、七输出和 62 摘要字段保留。

两步共享 `{work}/fixed-fejer-r690-inputs`，参考输出为 `{work}/fixed-fejer-reference`；全部科学数据仅 runner。完整新 seed/base/Q 随参考一并发布，后继完整 immutable normal/full solver 直接消费实际新参考和全来源。没有额外 fixture、AST、抽样审核或重放门。当前157个非固定 core、全部 SO3/H 自由变量、32 normal 阶段、原范数与科学工作预算均须保留。

## 全部历史与几何边界

完整十一历史 payload、原角色、发现序、保护及 literal 地址全部保留。相同 literal(cell,u,phi) 在新 g/new mesh 明确重解释，不声称同一物理 s 或空间点，不迁旧场值、根或数值证书。原未知末点/typed 不设为空，也不为新目标增加另一个前置条件。新全域证书支付新目标自身的全部义务。

R717 仅给设计图和全像/直径的条件界；改变当前自由 core 后不能继承初始 X/Y/曲率。当前没有新场、全闭面、全相位 reach、relative metric、整像 Hausdorff 或含反射非全等结论。全上/下片、接缝、两帽、固定握持、全 mixed pairs、全域误差和同 g 的实际 mesh/频率/t 精化仍须完成。

## 完整控制器与发布

控制器 `public_actions_controller_parallel12_compact_metadata.py` 为 19984 B / e818a7c181b245da595d1089baa4bb1169a444c50083f3bdbe84182cc07e05ac，完整 followups 为 32762 B / 046f0d7b8d27df95f5249438fdaf435b00c482b009fa8956f27dbdc662a6b314。控制器来自原11完整体：仅改独立12命名、将 HANDOFF 自有行省去长 stage id（完整 stage 仍保总索引/分卷），以及加入明确 `bootstrap_mode=followups_only` 分支。历史来源 fetch、分离源码 worktree、全部参数、自然返回和原科学调用保持；新分支从真实空 completed 开始，不编造 warm 父。

[完整请求](../computations/resume-20261127-actions-request-12.json) SHA 8998259a1d7991c0101ce93c5a3a21e38cdca1b6da0b1bcb8e15e2f68623902f；[完整初始队列](../computations/resume-20261127-followups-12.json) SHA 6abc9ba8570ef97dbc957955958e4c314632cec33b1f3687a5aad305417e8e1b，`finish_when_done=false`。这保留同一 runner 的真实文件，完整科学/pure 源一旦齐备即追加执行；既有 step 对象不删字段。350 分钟 workflow 和 20000 秒控制器界限只管任务编排，不构成研究停止理由。

每次真正 pull --rebase 都比较根 README 与本题 README，变动时打印完整差异交由研究者读取，已读提交写自有 HANDOFF 块；普通推非快进即拉取后再推直至成功。两规则在基线 c8ffb62b8527f6c1ee587e5ded8c0b9665037da2 的 SHA 分别为 581402c2148ee8c4ee2af741198ab54a56d71de2b5a7b0d0edf65359121cb102 / 3c1c03b358792b6c9937b95fcfea05b80a572a4da2cce615c4c9832fe929057d。Root 云 HEAD 检查不冒真实 pull。完整源码、全参数和实际紧凑返回保留 Git；raw 数组、全日志、证书及网格只在 runner，不上传 artifact 或改名输入。

## 完整交付入口

- [maker 全部源与接口](2026-11-27-fixed-fejer-r690-input-recipe-and-complete-api.md)；[完整总表](../computations/fixed-fejer-r690-input-complete-source-delivery.json)。说明的两处 Euclidean-quotient nonplanarity 已准确改为 noncongruence；不改任何运行体或 ready 身份。
- [reference/base 完整说明](2026-11-27-fixed-fejer-complete-reference-and-base.md)；[完整四源、46处派生与来源总表](../computations/fixed-fejer-complete-reference-base-source-delivery.json)。所有原文本正逆派生范围如实保留，不称本地科学执行。
- 新完整 normal 九下层、不可写点完整上层和相应费用正在同一目标接续，不能由“prepared”推成“executed”。

原 run10 仍独立监测，其 e711 target 与本新目标不同；原11已证输入守卫失败及后续发布越界，两因见 [实际终态](2026-11-27-run11-fixed-reference-word-mismatch-and-publication-failure.md)。不重试旧失败输入来冒本新目标已重建，也不删除其责任。继续直到本题 README 全部完成条件成立。
