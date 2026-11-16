# 原最后 LP 槽的完整实际：第64次已用，候选拒绝与输出缺项

日期：2026-11-16。原公开 run [43789033043](https://github.com/Rogerhu12/math-research-public/actions/runs/43789033043)，job133043031523，源码提交 a08ed9fb3bd44ece17befa23651b281e67f6bb1b。该原任务的最后一个 LP 槽已实际使用；本次没有新增接受点，现选仍是 accepted index27。工作流成功只表示入口与报告完成，不表示数值改善或主题完成。

## 1. 原输出、身份与真实拉取

root读原 job stdout 2957208B，SHA256 a465b5f6b09de317c8b9b541953171968543e91f3de3ad52ae4bac9e6dc5f8c0。以下均为相应 JSON 加一个 LF 的指纹，不把原 payload 放入 Git：

| 原记录 | Bytes | SHA256 |
|---|---:|---|
| REQUEST | 29010 | 490f26b19a4f457fb162312b85815f336203c9c279b7241df844f93b1f4ca3c5 |
| DEVELOPMENT_REUSED | 6127 | 504fb215085d6996d7be9595266500a266ac515bd302d5ee7fca1cb753a1924c |
| PRIOR_WORK_REUSED | 8385 | 6151623d177c31d73a281b914e678da1badcf1ff0be4da096cd2a50095d35ee7 |
| MODEL | 146427 | 1d449ca76a8706ab0481b51b91c21d23d01cd2645124036dba205755ba638609 |
| COMPLETE | 2682421 | af48ff341b831df4ce24038b33aa2153161fa8f5da7a2d0387f29b042123c45b |

REQUEST全部168路径、COMPLETE全部158 Python源与已发请求逐项相同；request bytes/hash也完全一致。旧11开发case与旧9检查只读原已付回执，当前case/group/stub执行均0。当前core不冒称被旧测试覆盖；原float10.0及三字段适配按已发布源码执行。第二失败原log只读一次，首失败不另下；原direct源为完整checkpoint读取一次。旧科学、方向、LP、profile不重跑。

公开实际 pull --rebase 于01:55:28.774081–01:55:30.892365 UTC，a08ed9fb…→9dc87d1b1bcfa060575d93d5e3370866db286af3。根README blob21bd547f56590b7f2dd279d0297efb289a9b2783、本题d0432faff569c8e9af7ed4809847e12880976c11，原SHA256相同、diff均空。私有实际pull01:55:32.766502–01:55:33.476551，before=after d77a9f45b59828b3187393c57dcebf993f5c1639；根5ba164843b1f5802184178a82d786264404873a3同、本题README无、QUEUE本会话唯一进行中。root02:00:22已读，并于02:05再次核回执；下次实际pull最迟02:55:28 UTC。API快照不称pull。

## 2. 最后模型的实际支持与调用

原512 bank行和4独立补充行完整保序。仅增加由原已付LP63完整oracle attainer得到的4个不同单位球支持，重复0，支持总数由516变520。旧报告字段 total_new_cut_rows=520 是已播种行总数，不能误称新增520行。新4支持不偷偷插入原512 bank；旧4与新4的provenance分开保在原checkpoint。

新4 attainer标签是粗43708/101701、细87416/203402；向内舍入调整分别0/1/0/1。已付attainer元数据SHA606cab87e2c7e967aa284a8d2fe5614e973affb7da150a9afff2e2fc5dcce407，原方向指纹ed0a3bde4d5d532ce6f210eb6c864a09b1a989a1a774866cb60d2a42a2a72df5；原未输出LP63精确步仍未知。

重建bank中496行的selected J复用、16行补当前原行；旧4补充全部复用；新4中2复用、2补原行，共18新row-J。合并A SHA47676f1c9cc56fca349f3c9082f1f93a0cb0fcc1a178250b787852ae90fea423，合并b SHAb00c36eeae58f5c28d28287488e92932aca72e518ad1b7443c0fef6f8c8a634c。

新调用为原共享序号64、1个primary、0个SOC。累计64=63 primary+1 SOC，原64上限没有重置。原模型编号28以 continuation_record_ordinal=1另记，没有覆盖原MODEL28。HiGHS实际9826行、161变量、12655888矩阵字节，status0/success、1028迭代，native LP .4294943079999882秒，inner .44180475600001046秒，原单次10秒上限保留。

| 实际量 | 数值 |
|---|---:|
| relaxed rho | .0060956036326755714 |
| full affine/repaired rho | .006096865741778756 |
| 完整 gap | .000001262109103184958 |
| 原动态 gap tolerance | .0000006751229804438652 |
| repaired linear residual | 6.1464945817508304e-18 |
| repaired bound violation | 0 |
| native linear residual | 3.8215191601465026e-10 |
| repaired predicted gain | .000005400983843550922 |

gap未合。本模型动态容差不是固定1e-9；此前负gain模型的floor不能代替这里的原规则。完整repair门允许输出 inexact candidate，本次实际如此；没有证明精确凸子问题最优。原目标中norm辅助代价2.5e-7，修复weighted objective .006097115741778757。报告normalized norm .25，physical common B .0002500000000000835、independent最大步.004，body/tail/height真半径分别.00025/.00003125/.001。

## 3. 真正两网 trial：原硬门通过，改善失败

新共享value共4次：恢复中心粗/细各1（原单网序号30），alpha=1候选粗/细各1（序号31）。没有额外末geometry。

| 量 | 粗网 | 细网 |
|---|---:|---:|
| trial eta | .26609807865831336 | .26610465853261767 |
| trial kappa | 57.99976229911655 | 57.99978114843467 |
| 原14门 | 全true | 全true |
| 新soft行 | 1 | 0 |
| 遗漏hard行 | 0 | 0 |

盒门也真，但原两网目标实际改善为 **−.000002391806995405421**。候选的细网eta比原接受点 .26610226672562226 更差；affine预测eta约.266096865741778、gain .0000054009838442170555。实际/预测gain比−.4428465376667212，实际减affine非线性偏差 .000007792790839733499。完整affine支持改善不能代替原非线性目标下降。

原处理结果为 new-rows-return-to-last-accepted-before-SOC。新增粗soft行先入池，回到最后接受点；剩余LP已0，所以没有新SOC、没有重用第64槽、没有新增接受。候选physical SHA5f2d9b8af09ffc48f180a47af89ac4e7fe36d4713b6660ce6217d887cbdc384f仅是身份指纹。

## 4. 必须继承的当前真实末态

接受数仍27，当前physical SHA bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c；independent159数组SHA712af66b0cb7a953596b4084041555884efb6554fca58e53c4ee4ab3ed64b5c6。其粗/细eta .26610151616656474/.26610226672562226，kappa57.99970793595668/57.99972678574561；原两网14门和盒真、目标.26未达。这些是metric辅助量，非握持位移。

池为 **4439/4533、版本8/6**；B由.00025降为 **.000125**，两个streak均0。bank仍512、SHA3d674785e4f46a8a5489ab49e6ff7de20d889eec92e4c7a6776ece452acf1611；insertions4842/evictions65/inward2502。下一方法不能恢复旧v7/6或旧B。

新曲率学习event35在最终收尾时恰commit一次：总36events、35commits、pending0；gamma粗43.39425351670855、细44.0738041005123，新stateSHA44eb8308c6ee5b2c1ab3b73951f6f111a5a5a7423636ea7a132b19b53003b00d。新模型执行时使用其冻结的旧gamma28.617940275291502/36.60765398014518；不回写改变已付模型。下一模型须使用当前学习状态。此经验保护不是连续误差或reach证明。

固定cfg SHA1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19、coordinate b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580、fixed g/b0、permanent enriched reference和159→163坐标均未改。旧14门没有降级。

## 5. 完整科学费用，不选较早checkpoint总钟

| 账目 | 科学秒 |
|---|---:|
| 原direct累计（已含其两入口失败） | 257.595331213 |
| 末槽首次类型失败增量 | 2.884255101000008 |
| 末槽第二schema失败增量 | 10.578692648000015 |
| 本次新增 | 85.07154129899999 |
| **同任务最终累计** | **356.129820261** |

累计62共享values=31粗+31细；本次4值、1LP、0SOC、0接受。当前process86.31020710600001秒、peakRSS816876KiB。原更早关闭epoch费用仍独立保其原note，不二次加回当前science；所有失败已付费用没有丢。

本次失败回执读取.852369647秒、原direct源读取1.04497729秒、24输入与不可变准备7.317734209秒，科学输入合9.215315709秒；constructor .142207083秒，恢复/模型/trial75.611043401秒。原科学启动前import1.238665807秒独列，不重复并入科学。

4次真实geometry合54.654478802秒，无失败；reference fixed primitive一次miss41.674018983秒，3hits合.000487413秒；reference height jet miss4.019579542秒、3hits .001404013秒；current complete scalar 2miss8.111138579秒、2hits .00000647秒。不能仅据这次墙钟与旧205秒冷失败作受控速度比较。

selected J粗1refresh/10batches/4.315013385秒，细1refresh/27batches/13.459759254秒；无全角159/163稠密张量、factorization内无普通geometry。oracle新方向2（primary及actual trial-quality）、cached reuse1、full grid scans4；新方向费1.114053302秒、新18row-J .565574727秒。无已付方向/LP/profile回放。

COMPLETE中的checkpoint时间356.127966801早于最终报告；下一继承基线必须取最终356.129820261。较早stage增量85.030957444也不能代替最终本次费用。

## 6. 新候选 exact159 未实际输出：原记录中的错误

原 COMPLETE.new_candidate_step_record 实际为 **null**，其stage metadata准确是canonical null的4B/SHA74234e98afe7498fb5daf1f36ac2d78acc339464f950703b8c019892f982b90b。两个硬编码布尔字段 all_new_candidate_exact159_is_retained_once_even_if_not_returned 与 new_candidate_exact_step_saved_separately 却为true，和真实内容矛盾，不能用它们证明已保存。

MODEL只保 proposed_step_fingerprint：159维、canonical JSON6122B、SHA5d4b0d5846e6db57e749e174f79c762716f877892372676e6053e435b08fcf06。trial159/163也只有元数据：5693B/1056b6b914c7f632845f04ad33dd9b2dd0287f3eb921e1ef752e69e507e11174，5852B/1515a8b27f514bf399f0c357d36dc64649b73ea47e5256d08c12b49f7a8c36c8。逐层检查原COMPLETE/MODEL的159/163数组，只有原reference和最后接受点及其副本，没有新候选或新step的完整向量。

静态原因明确：末槽wrapper只在 overridden evaluated(step) 捕获新步，但原 _candidate 调 slack(step)，父类slack直接去oracle；最后唯一LP之后不再进入下一轮cuts的evaluated。raw model曾有 exact_binary64_independent_proposed_step，随后语义selector将其改成指纹；trial也被compact_metadata缩掉。临时audit.json的指纹存在，却没有把该raw向量打印到可读取原stdout；它既未上传artifact，也不应为了补此缺项重跑LP64。

这是报告保真缺陷，已发生的LP、真实两网trial、池更新、学习和拒绝结果仍按实际入账。新方法从已完整保存的accepted27恢复；历史缺失步保持未知。新solver必须在真实返回有限primal后直接捕获exact159，独立于任何后续slack/evaluated调用，保存成功标志须从实际记录存在性导出。

## 7. 后继边界

本原64-LP任务已关闭。不能在同预算下启动LP65、改64计数或为补向量重演64。下一已设计的有限锥方法给真实每个原行完整Lorentz约束，是不同的子问题接口；须先固定恢复合同和显式新conic预算，保祖先64/62/356.129820261、同cfg与原目标/两网/全oracle门，新账和原全局剩余额度取交。旧原11/9不重测，新接口仅支付必要新检查。

当前没有达到题README的同g精度、全时嵌入、reach、宏观位移及完整有限族门；本结果写毕即推后继续open中的理论与新数值子题。
