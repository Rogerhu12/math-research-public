# R824 — 原free1187的596位断点与同核续接

2026-11-16。状态：**真实公开中间进展；完整极模块、原全局算子、eta与height未完成。**

## 已结束的原任务

run [43792912432](https://github.com/Rogerhu12/math-research-public/actions/runs/43792912432)，job133055178711，
source33f5c3288305cdfc8ed1adb5e1e4fee3ed940870。
原core 1ece3cf45f57fda2d1fe40f38efb3e225d2e05ce910a917eb38dbcd85fe3d1cb，
wrapper c590773947ac8e74110bf902e1f46f80859912393163b8ea55ce699717889a3c。
真core receipt的exception_type=BudgetStop，complete=false，完整阶段与最新lift保留；run退出1，error=null，
结束于2026-11-16 07:36:34.515826 UTC，不是推测的外层超时。

原artifact14205663835，serre-global-R824-original-global-polar-generators-43792912432-1，
1391989692字节，SHA256 fd1084f9742b715efa7a305ce724ffc6900ba45c64d5437d9baf1ad550a3aab6，
到期2026-11-17 07:36:37 UTC。

## 真正原目标与一致断点

|文件|字节|SHA256|
|---|---:|---|
|full-outputs-manifest.json|239439|27a030ff753d8ca155654b2e1ae451e76005e2943dfaf7b4f83b9f9608aa3c9a|
|R824-power5-free-1187-current.json.gz|5693|e0aaa50aff3706e745580747b8eeb8cd753805c3eae9116d9b94dc087e1dff4f|
|R824-power5-free-1187-history-00000596.json.gz|5737|31993dac408b593b67817123c707bfac6687e9ec6377980edbddf2c120be70ad|
|R824-power5-free-1187-lift-00000596.json.gz|84186258|071c3390f10e17a69a8e66357f3cac1ea632eea50134e4a0187175c047290e85|
|R824-retained-producer-inputs.tar.gz|612745716|71b16a02e29ecd682b23ab2cfa475194188acdb41c0380561eeb9af9580983ac|

manifest实际956项。首纯IO run43826442405读原历史等小件；随后run43827843962/source8e3841b8da46479c6bb7dee5ba4956ee5388f2bf只读current和最后596历史。两者complete均true，current.history_receipt准确指向上述history，current.lift与history.new_complete_lift的完整三元spec相等，全部target_configuration相同，history.digits=596。

原target_configuration保ordinary_power=5、prime1000000753、free_column1187，一条原L自由坐标=1、其余全0。完整14个原branch阶段、原chart/common-clear129和rational_block身份不变。original_R787_reserved_target_recomputed=false，原1186继续归R787，不挪目标。595大向量只保其历史指纹，596大lift保原始全字节。

这次小件读取不冒称已经再次重哈希84MB lift、612MB carrier或整1.39GBZIP；同一原wrapper在恢复时按原完整manifest逐SHA载入必要大断点。没有新数学在IO中执行。

## 本次公开续接

原请求只改resume到上述真实源。新request10696字节，SHA256
ba760988505debb9d508afb7def48e3de220cc6585724c0aa5e694a4abcf40b1。
原27个权5与244个权6范围、all_new/all_selected、300分钟预算、每8位重构、core/method/proof/helper与原source tag保持不变。从实际596后继续，不重501以前或保留的全部中间阶段。旧129/142/280Q、一次κ/246、r28不延143至155等边界继续生效。

恢复发布经真实git pull及两README比较后dispatch serre-p41-original-global-polar-generators.yml。
新run编号在实际启动后写回HANDOFF。准确生成与完整1778minor/1206核尚待原数学成功；本断点不等于它们完成。
