# RET99：六个已终止运行的完整控制器输出退存

## 1. 范围与固定恢复点

本批只处理下表六个旧运行的 13 份 `public-actions-…md` 索引、分卷，毛大小 **473,592 B**。每份正文均在大小检查后完整读取；没有读取任何大于等于 100,000 B 的正文或任何 gzip、NPZ、二进制数组。固定恢复提交为：

`5a8759e2104c9ab9168875ae465af18f307a0e8b`

完整台账 `computations/terminal-runs27-33-retention99-complete-provenance.json` 为 95578 B，SHA-256 `b2120dee1c24b27e1c550c320c4331ca31ee3d30c2f82e256d25e12dca5dfd6b`，Git blob `4a2c3085474617df60e749a6f3a7af2336b56e71`。它列出全部 13 个精确删除身份、65 个完整当前保留身份、4 个明确历史版本、6 个完整 workflow 和根 README，以及全部六个运行的完整源、参数、返回结果与恢复责任。本说明不替代台账里的任何完整数组。

根代理执行普通提交；本代理只创建未被 ref 引用的完整 blobs，不改 request、queue、workflow 或分支。发布前由根代理按新 HEAD 比较每个删除路径的完整 Git blob 与字节数。

## 2. 六个实际终态及仍未知事项

| 旧运行 | 官方终态 UTC | 已实际取得的结论 | 仍不能推定的结论 |
|---|---|---|---|
| 27 / 46105138690 | 09:42:20，failure | 两输入各自返回 0；接受次数 3，当前点以 `12d82f1c` 开头，Phi 748.4181663644251，Gram 0.487646571786265，最大有限违反量 0.6999403610404435。 | 官方失败原因未知；后一个 `c6928f7a` 试点只有自己的统计，没有自己的几何或接受结论；没有完整 final/typed。 |
| 28 / 46108296054 | 09:40:01，failure | **原科学和原 pure 均已自然返回 0**。原 final 点 `a28ae999`，恢复接受 4 次，metric 接受 0，Phi 681.6450227773521，Gram 0.40616533555531326，有限最大违反量 0.5225620087197518，feasible=false；之后两个元数据读取也各自返回 0。 | 后接的 R729 显式 final 续跑只有实际开始记录，没有其自己的完整返回；不能把原 final 的数据转移给该续跑。官方失败原因未知。 |
| 29 retry / 46112781312 | 09:40:48，failure | 两输入返回 0；当前 `bc818314` 点接受 1 次，Phi 584.8125864670693，Gram 0.4179453237576573；reach 项已为 -0.03475313540129943，distance-plus 仍为 +0.13820228685007474。 | 下一 `30412f0b` 点只有自己的统计；没有其自己的几何、接受、final/typed。这个 retry 的官方失败原因未知，不能套用更早原 29 的容量异常。 |
| 31 / 46122200592 | 09:40:24，failure | 两输入返回 0；当前 `337dc8a3` 点接受 1 次，Phi 14106.362105626435，Gram 0.8223753558623952，reach 项 +0.7621406738864105。 | 后一个 `ec99d7de` 点未取得自己的几何与接受结论；没有完整 final/typed；官方失败原因未知。 |
| 32 / 46125006601 | 09:41:53，failure | 两输入返回 0；当前初点 `7e06e86e`，接受 0，Phi 14106.361942260944，Gram 0.822374918515021，reach 项 +0.7631911760908718。 | `1ec67648` 试点自己的统计已返，但几何/接受未知；R729 trigger、adoption、gap 不从试点差异推测；官方失败原因未知。 |
| 33 旧运行 / 46130690181 | 09:38:59，failure | 真实完整原日志证明 maker 0、reference 0。reference 用时 499.93597806900004 秒，完整报告 84,971 B 的身份已在原终态 note 保存。 | 没有科学开始、模型、点、final、typed 或 pure 返回。**只有这一运行**的完整原日志确证 Publisher.sync 真 pull 了根 README §16 的变化，随后要求读取确切差异而抛出 RuntimeError；这不是数值失败或超时。 |

表格是完整记录的导航，不是唯一结果载体。每个当前点、试点、模型、源、时间、六个带符号几何项、最大曲率及其位置、实际 summary errors 和缺失输出，都保留在完整台账对应 case 与原逻辑块中。所有人写完整叙述、数值表、原时间顺序和官方 jobs 记录仍在当前树。

## 3. 全源、资源及全部参数保留

六个实际 controller、公共 followup、六个 workflow 均完整读取并保留。controller 的 `Publisher.render` 从真实 step/进度记录生成这些 Markdown；原科学读取实际输入/reference/carrier/source/point 文件，pure 读取真实完整 report/final/typed，不把待退的索引或分卷当成数学输入。

27、28 的完整 workflow 预算为 350 分钟；29 retry、31、32、33 为 360 分钟。所有原 checkout/setup 版本、CPU Torch、NumPy/SciPy/Python、BLAS 环境、资源和命令均以原全文件保留。29 retry 及 31–33 的完整容量等待正文仍在：真实 sync 后生成完整拟发布内容并检查 200,000,000 B 课题与 H 大小，超限则等待和 pull，不丢返回记录、不杀 child。官方同时 failure 并不能证明相同原因。

每组完整 source binding、parameter binding、delivery、science/pure ready 均在 65 项当前保留表中。27/28/29/31 保留原 157/7 词 argv、458/445 formal selectors；32/旧 33 为原 157/7、575/564；所有原 64 live scalars 都保留。后接 28 的 R729 continuation 独立保留全 142/7 词、587/568 selectors 与真实 13 成员父场要求。没有减少任何原数值预算、角域、径向域、变量、法向阶段或 typed/history。

固定输入配方完整 maker 89cc 和 reference e717 仍在：同一确定性七项 RN-even Fejér 配方、固定前三词、160 个 core 词、923 个准确 affine 节点、7377 carrier 和原 8-Gauss；2218 叶完整标量费用及 accuracy_reached=false 原样保留。完整实际输入阶段含各自 6/26 词 argv、14/62 selectors 和各自全输出身份。原 accepted099 gzip 只作为既有确定参数投影来源，固定 60321451c058c6a51da58c37ae5ec6f2d1145f74 的路径、2,614,352 B、完整 SHA/blob 均已登记；本批没有读取它。参数投影 e640 不冒实际 scalar 身份。任何不同 run 的实际文件身份不相互代用。

## 4. 28 的三个不同阶段不合并

原 28 科学耗时 10456.962818394999 秒、pure 348.8245757200002 秒，二者实际 exit 0；原 report 为 51,908,815 B，SHA-256 `53af35f6e91a6d4021d40fcf7b5a091fa74fd9d49b645b9c5c89c2f2d47cb1fa`。完整 final、13 成员与 typed/history 身份仍按真实原记录保存，没有经 API 读取大 report 或 NPZ。

随后第一元数据读回有 16 个 scalar 与 13 个原 non-scalar-summary errors；第二次为 90/90 scalar、零 summary_errors/missing_outputs。两者原 errors 以及完整原元数据都保留，不能因第二次成功而抹掉第一次。完整 `read_complete_existing_fixed_scalar_metadata.py`、当时 90-selector 队列和独立标量结论 note 均已明确 whole 身份。它没有新 F/J/normal/integration。

再后 R729 explicit-final continuation 使用真正原完整父场；它只有自己的开始事件，两份进度文件原缺失，未取得新点或新结论。原初始队列、90-selector 队列和当前续跑队列是三个不同 whole 版本，台账分别记录准确恢复提交，不能按同名路径互换。

## 5. 原 33 与当前 retry 严格分开

旧 33 request/queue 的完整版本固定于 `3ff5795e46cc5a2b50f0ba27d6c747a00bc54d03`：41,482 B / blob `4d3d8753a571febbe98f7d95f3717406a1febf27`，80,264 B / blob `55458eecbdd30c6ad4bfc3ae3f2b425ae5b3154f`。这两项仅是历史 whole 版本，不作当前 guard。

当前 retry 的 request 为 45,113 B / blob `01a54493aa65c133fadffc98090eb3a1832b8727`，queue 为 80,280 B / blob `de659fd7787046fea517e0579da6db86fcec9aeb`。这两个当前完整文件都保留、不改写。删除列表只含旧 run ID 46130690181 的两个输出；任何新 retry run 的索引/分卷均不在范围。

原 33 日志完整 64,705 B、SHA-256 `ad490cac7f23076de59607b79514f6a2df58009836c9bc73cc3b55c02b6c06ac` 的身份和四条实际 input started/returned 事件在完整人写终态 note 中保留。第二输入虽没有成功发布进旧分卷，真实日志已证明 exit 0，不能写成未运行；但也不能据此声称科学已启动。

## 6. 恢复和消费者责任

每个待退 whole 文件都具备完整固定 commit、path、bytes、SHA-256、Git blob。台账逐逻辑 JSON fence 记录一基序号、完整原文本字节数和 SHA，指向整个原块，含每个原数组、字段、null、错误和数值字面；没有按几个摘要字段冒充整对象。文件的其他叙述、表格、链接同样由完整固定 Git 恢复。

旧 whole-hash reader 应在隔离历史 checkout 用 `git show <commit>:<path>` 或对应完整 blob 恢复原字，核精确身份，再按旧合同读取；不能拿当前 retry、后续 note 或格式化版本冒旧 whole。完整人写官方终态 note、原完整科学源、所有参数和唯一输入仍留树。这里没有要求重演远端发布事件或启动新科学来证明可以退存。

新科学重跑会有自己的实际 run、字节、点、根、模型、误差与失败；不声称重演过去的墙钟时间、取消或网络异常。RET99 不产生任何新连续几何、reach、noncongruence 或研究完成结论。所有尚未闭合的条件和未知状态保持原义。

## 7. 发布边界

唯一可删除项是完整台账 `deletion_files` 的 13 项。65 个 `current_retained_guards` 对应准备时固定 HEAD 的当前身份；若根发布前某人写 note 或 retry queue 合法更新，须明确记录新 current 与旧 historical 两层，不能强制回写旧体。4 个历史版本及 7 个外部课题路径记录不作当前 topic guard。

本代理没有执行科学、AST、fixture、benchmark、重放或 refs/queue 写入。全部新工件保持完整且小于 100,000 B。准确净退字节数、三件新增记录和 13 个删除条目由最终 delivery manifest 一并给出。
