# actual110：八个真实同31模型接受，后续最近拒绝转到原midpoint471

**可信度：数值证据。** 8个原模型均产生真实新warm，并各自完成原完整边界FD；原success、new_coupled_finite_acceptance、当前H的native及fullDN仍false。运行按8批预算结束，不是原17档全拒，也没有求得BVP。每批权重重新形成，只比较下表同一行内的merit，禁止跨行相减。

## 实际执行与来源

公开run **43685348016**，source `8d4a3af1d553cd85cfa9694ec8cfaf1c0b66ce3f`，job `132724561759`；06:25:12 UTC创建，原chain-end事件07:45:15 UTC，作业success。完整配方见[request110接口](2026-11-15-request110-same31-real-pair-batch-lifecycle.md)。入口 `computations/geometry_20261115_same31_temporary_batches.py` SHA `a1ba1cd895892906f594cd65313d03f11230edb940c8b0c77977dad92591552f`；request `public-same31-batch-request.json` SHA `ef159a8a938411320cbc99ea9faefba08dc1da29e616c423a593eed80cb39cbd`；workflow SHA `3363acf223a5c7f8ac354f485f5c2863c377afdde132980777bc140f8723343d`。

每批调用原 `geometry_20261114_thirty_one_query_collocation_observer_warm.py`：iterations=1、damping=270、LSMR=200、projection=200、line-search=17、budget=1200s、angles=4096、jac-workers=2；condensed预算600s/试探保留90s/恢复30s、512 working rows×200 dual sweeps。新warm再经 `geometry_20261114_thirty_one_query_condensed_response.py --angles 4096` 原FD，真实通过才传下一批。完整源pin和其余参数见上述request；没有重造A/AT/B/H/C或修改接受门。

从actual98 artifact14147700690开始，ZIP809042943 B / `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`；原warm `b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`、status `b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。这是新轨迹，不重标107父场。首批接受alpha/merit/FD读数与107相同，但完整warm/status SHA不同且107字段payload不可用；不声称整个场逐位相同。

## 八次原接受与原FD

| batch | 原接受alpha | 同模型W_before | 同模型W_after | 新warm原FD最大相对方向误差 |
|---:|---:|---:|---:|---:|
| 0 | 0.125 | 43.363003729098274 | 43.33594286031892 | 8.81884772255149e-10 |
| 1 | 0.0625 | 43.33449126616587 | 43.3300290784794 | 7.109471380649381e-10 |
| 2 | 0.0078125 | 43.32389204598073 | 43.321650079547496 | 8.123291574724692e-10 |
| 3 | 0.0078125 | 43.32249149408277 | 43.320201971795136 | 9.918682068427663e-10 |
| 4 | 0.00390625 | 43.321086957610326 | 43.319984473859456 | 9.31687781363812e-10 |
| 5 | 0.001953125 | 43.320360386442566 | 43.31981799504595 | 1.0704054827725046e-09 |
| 6 | 0.001953125 | 43.31999214241096 | 43.31943967126952 | 9.140500687973131e-10 |
| 7 | 0.00048828125 | 43.319629880281205 | 43.31949437849194 | 1.0788333791801373e-09 |

8对model/FD退出码均0，implementation_check_passed均true；每批重新计算当前模型完整J和真实新H边界差分，当前H不等原仿射锚。原31 typed queries、63488角行、236036完整自由坐标、109外部自由core及完整外部仿射恢复不变。QP只给浮点候选和后验，full_QP_optimality_claimed=false；512 working-row预算耗尽不冒完整最优性，局部QP的nonlinear_accepted=false也不覆盖下游真实原接受。

最后接受点physical collocation max **0.007107378585750384**，complete BC max **6.276408182782244e−9**；node/mid/RMS域有效，两组RMS各698点无坏点，4096角rho原读数0.16604058243274977。它们不满足完整BVP终检，不能把优化进展或FD正确称为native/fullDN接受。

## 新的具体限制：未选原midpoint471

batch0最近拒绝仍alpha=.25、LEFT-RMS464一处beta²=−0.2683514415128212；alpha=.125有效并接受。batch1–7紧邻接受档之前的拒绝均在原collocation midpoint471出现一处非有限原RHS：输入有限、node域无失败、midpoint的beta²负，尚未进入RMS。原31表虽含LEFT-RMS471，却不含collocation-midpoint471，两种位置不能互换。

| batch | 最近拒绝alpha | midpoint471原beta²最小值 | 原负角计数 |
|---:|---:|---:|---:|
| 1 | 0.125 | -0.06775083546009597 | 4 |
| 2 | 0.015625 | -0.05923987474642778 | 8 |
| 3 | 0.015625 | -0.03596232728504534 | 8 |
| 4 | 0.0078125 | -0.0037399290405073504 | 4 |
| 5 | 0.00390625 | -0.0004982435163811694 | 4 |
| 6 | 0.00390625 | -0.0007515627127094859 | 4 |
| 7 | 0.0009765625 | -3.8894462797367524e-05 | 4 |

该midpoint station=1.1918702857402743、左右站位1.1893780599903945与1.1943625114901544。末批最近拒绝alpha=.0009765625、beta²=−3.8894462797367524e−5；接受alpha=.00048828125。七个最近拒绝的nearest_failed_selected_queries均为空，表示31个选定查询未含这个真实失败，不表示原完整域通过。所有远档保留；例如batch2的alpha=.5/.25有有限原merit但上升，不能把全部拒绝都归为该点失败。

下一项保原31并加入实际midpoint471，形成独立32-query方向约束消费者；所有原非线性域/merit/边界/最终门不变，不预言新增行一定改善。110临时末场已清理，从可恢复actual98原件开始新轨迹，不冒由110末点续算或由哈希恢复warm，不上传raw。

## 原输出身份与规则同步

job日志临时读取身份411417 B / `6189a2a9868de01f7d235c03454782e281f39b6d841636753d86d1db3763ddc1`。逐批BEGIN/END内UTF-8 compact JSON的SHA **包含结尾LF**；八份原字节与日志声明一致。本地只有原字段选择和元数据核对，无科学导入或数值重算。

| batch | 原摘要字节数 | 原摘要SHA-256 |
|---:|---:|---|
| 0 | 36657 | `24ac029b138c888a086a35431b67be805f91169e900adcfed94776bd7970b156` |
| 1 | 33107 | `c10e5d03069ff27a92d9518bcdb5f86ab577ff7b91a1927846dd2c1811448e11` |
| 2 | 41702 | `5c09d6b1a32901da06915ed24e31f0e488718f3bcac699ed64049e70cce6cec7` |
| 3 | 40568 | `d5da0cf8221a330aaff555b15bada9bd27a63ccf7033e592b9046c4eee72e9aa` |
| 4 | 43061 | `6d6bcaa699a736025ee7de2b35404e20821ce972468f6201f34a2920568e0cd8` |
| 5 | 45530 | `a6dfa1ee32f419d16c398d242902f8955a6d544886221eff4c49ed472ced8127` |
| 6 | 45734 | `84f2fecd82f102f649c0e7c8c99634232df9480707a0c63a6fa29a8e0e48a239` |
| 7 | 50701 | `7d84ea7e294ec93b04a2538058304492ec391e6ad091e4149d58e04934dcbbae` |

最终真实warm5024330 B / `c02da9e1bef573ec9a3c2bc4eafc4d3312dee732c1b0c0a9fe05d066f9d5db46`；status5630024 B / `90bfb02a47590bcc7d43d4367e915da670df133e42cd97c761bdd7340fcdf0c1`；model1356665 B / `b3c5e866d97818fa02700a10735f2e79bfb6c10b86a80d9d1540ca392dcb750e`；FD4205955 B / `eabcc63f5474c7ba2908baad77291fcad48f8a8a27257f5161d146e018245f48`。这些是已清理的实际输出身份，不是可由SHA恢复的检查点。

原monitor06:25:36 UTC真实pull/read8d4a3af1并发布a8e9c87c；07:11:53 UTC读656c808d并发布b21d2781，双README不变。chain明确8个model/FD完成、owned临时payload清理，Git/Release/artifact上传0；旧summary的arrays_artifact_only只是上游遗留字段，不能覆盖真实零上传。运行成功、源码接口和本条数值证据均非课题完成。
