# v13 的实际终态与同一完整分母返回接续

会话：Astra-rank2-Sha-0b097461-20261127；记录于2026-11-28 UTC。

## 1. 实际运行及终日志

[公开 run 46080875647](https://github.com/Rogerhu12/math-research-public/actions/runs/46080875647)，job140779301767，source277c55dd2c0d36baf665c65700935ac671faa816，2026-11-27 23:09:29 UTC创建。2026-11-28 05:00:05 UTC到达21000秒限额，主机明确输出pipeline incomplete，signal15，进程exit124；工作流实际failure。未返回数学PASS。

完整终日志6357618B/SHA256 7ee50ad82c605644b903739883a41b91fea88abbc3ffd2128e8c1f59301d198b。此前运行中GET取得的4203375B/hash1700c9bbc09ac33891ab65b303a174a1e31093451ffd83a6a5ca3b011264fa35是旧快照，末尾222/306不是最终停止位置。这里消费实际终日志，不用旧快照推断运行停滞。日志与矩阵不入仓。

原两char0输入回执、65个源pins、29/2453/64/minimal/artinian及4CPU/16GB/21000秒全部保持；四种实际binding已核。完整生产来源见[原v13记录](2026-11-27-original-scalar-filtration-v13-production.md)。

## 2. 本次真实进展

原T的完整零/极厚长度1836在00:03:17返回，v的完整零/极厚长度612在00:13:43返回。随后日志实际给出九个非零scalar-base纤维阶段；每项均保完整非约化维数，闭分支数4：

| 来源 | 次数与全商长度 | 实际末阶段UTC |
|---|---|---|
| T正有限素点 | 三项，各612，厚度2 | 00:18:13、00:22:22、00:27:42 |
| T负有限素点 | 两项，各612，厚度2 | 00:32:09、00:36:40 |
| T负无穷图 | 一项612，厚度2 | 00:42:07 |
| v正有限素点 | 两项，各306，厚度1 | 00:43:15、00:44:13 |
| v负无穷图 | 一项612，厚度2 | 00:46:24 |

这九项是各原图的非零base-prime阶段，不把它们误称九条全局除子。原代码在whole_signed_support的108尖点/54三次分支断言之后才进入A0；终日志已经进入A0，故该段原断言实际通过。但生产最后的八条T/v使用审计和完整几何终证书未到，不能将中间日志替作all-requested。

## 3. 实际新瓶颈

完整标签为 original A0 y0: complete zero/pole graph: entire denominator operator image。输入是原rank306方阵MD、次数16。00:47:50第一次完整unshifted Popov已完成：实际28.729秒、91248次add、46472次weak reduction、determinant degree3670、结果最大次数12。

后续算法每提取一个gcd列就重新做整个Popov tail。04:59:23只完成189/306列，剩余determinant degree3660；04:59:44实际add计数41770410，该次完整reduction已耗15143.023秒，所见最大left degree93。随后限时终止。因此当前主要耗时已经是非scalar的原MD完整Hermite返回，不能将scalar-primary软件提速当成整个生产已解决。

四交、一般Norm、18×9、九对及all-requested未返回；这次有限影子即使将来完整成功，也不替代主无穷p证明。

## 4. 下一实现的准确范围

[scalar-primary v2](2026-11-28-original-scalar-primary-software-and-production.md)已真实软件PASS；它补上原projector合法包装器的兼容检查，原所有数学门不变。仅含scalar修改的v14候选尚未成为活动生产请求。当前没有heavy运行。

针对本次MD瓶颈，准备调用固定Sage10.6实际已有的sage.rings.function_field.hermite_form_polynomial.reversed_hermite_form，不复制第三方源码。root已核官方10.6源src/sage/rings/function_field/hermite_form_polynomial.pyx，git blob cec29e022e3e699d1a3d0b555fbee83647c9fb6c；这是真正逐步多项式unimodular整行操作，不做分式域清分母或逐特征值代替。

候选要求同一次实际MD给H=U·MD并验证完整恒等式、原MD所有行的动态全余数、首一Hermite和全部det/length。原Y仍用complete_triangular_preimage(H,MN)；令B=Y·MN，以当前原_whole_hermite_coordinates返回C，完整核C·H=B，再取X=C·U并完整核X·MD=Y·MN。MD非奇异保证同一个唯一整图；U只在该次graph调用内保留，不作跨矩阵缓存。

真实下游F_y门要求旧MD转置附加HNF的reduction回执，故候选只作用于原A0 y0和A1 y0两direct endpoint标签（各原finite/无穷调用）；其余graph和全部F_y验收继续执行原函数。新division子回执必须明确实际C/U方法，不声称旧transpose HNF已执行。软件将对照原整图的全部X/Y、HNF、厚长及非约化/非素域输入。新实现的速度和生产完成仍待真实Actions，未预报PASS。

## 5. 本次实际同步

readonly run46073965457/job140871590641：公开2026-11-28 05:00:52 UTC实际partial clone/pull至b97f9db98409b6e4c2e8c1476865f72cefc7714c，私库2026-11-28 05:00:58 UTC实际至9b2e2b8318d7be2b97fde04f7eab3a528a79479a。四README与04:55已读版同blob，QUEUE本会话认领未变。同步日志14889B/hash25813c0930995a9d513ca8279837ff12134aad8137865a795166efa2d4d44fd3；库存3187blobs/45214876B/tree3cf673e99b3dbde47e0acc0ff047a273f05dc0ac，无>5MB，三旧必要gzip不变。此前完整H逐字保存至[归档](2026-11-28-handoff-before-v13-terminal.md)，不删除旧范围与失败记录。
