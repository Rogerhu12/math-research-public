# RET97：22–25 号终态 Actions 的完整控制器输出保全

本批只从当前树退役九份旧 controller index/part Markdown，共 **338,269 字节**。四个运行均已有真实官方 `completed/cancelled` 记录。所有科学源码、完整参数、request、queue、证明、独立人写运行记录、25 号完整父场的恢复责任均保持原样；27–33 号活动运行不在范围内。26 号刚返回的官方取消另作独立批次，不在这九项中。

本批依据根 README §15 和已实施 RET78/79 的完整来源、参数、实际记录及固定 Git 恢复合同。它没有重新执行科学计算，也没有推断取消原因。下面的“已返回”始终只指原控制器实际记录的自然返回；官方取消不反向抹去 25 号已经完成的原科学步骤。

## 1. 固定完整恢复与删除边界

固定恢复提交为 `f176c0d52fef4ca6a15dd4a83e3c2c5504284792`。每个原文件的完整字节数、SHA-256、Git blob 和实际正文均已保全于 `terminal-runs22-25-retention97-complete-provenance.json`。当前根操作者仅可在 fresh HEAD 上再次核对相同 path/blob/size 后，普通提交退役这九个明确对象；任何不匹配项保留。

| 原完整文件 | 字节 | 原 Git blob |
|---|---:|---|
| `notes/2026-11-28-public-actions-46090913581-1-part-001.md` | 16601 | `ece3181bad61eae661a6480ddec59ff8976f83a4` |
| `notes/2026-11-28-public-actions-46090913581-1.md` | 48488 | `dc76b7e5c140bb054f2ac0bda5aa518ac69738ff` |
| `notes/2026-11-28-public-actions-46094430214-1-part-001.md` | 16606 | `82b902ab2cfa5222c57560485fa5629f97665419` |
| `notes/2026-11-28-public-actions-46094430214-1.md` | 51483 | `c784647a90be8574b3ca81fe48920cce46100214` |
| `notes/2026-11-28-public-actions-46096380016-1-part-001.md` | 16607 | `c1e68f6d4819b1fdf4f4668d11e14570c93016ed` |
| `notes/2026-11-28-public-actions-46096380016-1.md` | 59887 | `ecfb80f065984c9d7738d47e7084e01788eda7b6` |
| `notes/2026-11-28-public-actions-46099929359-1-part-001.md` | 54364 | `1378240607367436af10107e965bb2aea69bfa20` |
| `notes/2026-11-28-public-actions-46099929359-1-part-002.md` | 33046 | `9614c809d95c25d757c0406b9f168cb6094541f1` |
| `notes/2026-11-28-public-actions-46099929359-1.md` | 41187 | `5b78bc523489b271d859e5f2b4925a0d3b14abae` |

恢复者在一个独立历史 checkout 中使用 `git show f176c0d52fef4ca6a15dd4a83e3c2c5504284792:FULL_PATH > FULL_PATH`，并核对表内完整 bytes、SHA-256 与 Git blob。也可直接取同一完整 Git blob。历史 25 号初始 queue、pure-only queue 与 RET84 前的完整人写 note 则使用账本每条自己的固定恢复提交，不能拿当前路径上的另一版本代替。

这是完整文件的历史恢复，不是把数字数组分块、编码或压缩传出。原报告、NPZ、root packet、逐胞数组和完整日志均未在本批读入。原 25 号 51,804,983 字节报告及 8,554,125 字节纯读取输出，只保留本来已公开的完整身份与实际小标量；本批不声称它们现在仍可从某个新 runner 取得。

## 2. 实际终态与不能混淆的结果

| 运行 | 官方 job 完成时间（UTC，2026-11-28） | 已实际返回的步骤 | 末状态的边界 |
|---|---|---|---|
| 22：46090913581/1 | 06:51:08，cancelled | maker 0、reference 0 | 科学仍未观察到自然返回；最后 current accepted3，下一 trial 只有自己的统计 |
| 23：46094430214/1 | 07:32:27，cancelled | maker 0、reference 0 | 原 fullwave restoration-continuation；current accepted2，后续 trial 的几何/接受未知 |
| 24：46096380016/1 | 07:56:19，cancelled | maker 0、reference 0 | paired-halfwave 五分之八宽度；current accepted3，下一 trial 只有自己的统计 |
| 25：46099929359/1 | 08:39:51，cancelled | maker 0、reference 0、原 science 0、原 pure 0 | 原完整场 accepted4 后启动同源 restart01；restart accepted0，未返回新的完整场 |

四次取消的原因都没有官方证据，本批统一保为未知，不能由 350 分钟上限或时间差推断。

22 号最后已确认 current 是 `b34824acd5f82b1540ff7c582fc0319b3311974e9e8860845f9c0d26d084846d`，Phi 为 681.6470516175362，Gram 为 0.40616529581758637，reach 约束值为 +0.5235597907246015，distance-plus 为 +0.11392305204890485。后继 `480be58574d985b3f714bc2567d92adcf3e7b46366248d1722c9665afd814938` 只有自己的统计返回；其几何、接受与 final/typed 均未补值。

23 号最后 current `87c07682c4ee3fa23e87a0c236e7321d62c62986646db3d572b320557e4ada7f` 的 Phi 为 3825.0581646753217，Gram 为 0.6460503043451958，reach 为 +0.9678293850088526。trial `491dae08135b3f508dd369016137accb78a76cfc08a3d1e3295449af7446aa55` 已真实拒绝；再后 `344a0b8d8a14eacee9b65961d5bc8f006e07e43349b768857f1812fdbbd4ea2c` 只返回统计，不继承 current 的几何。它使用原 fullwave 物理 seed 与其实际 damping-continuation policy，不冒 22 号半波模型。

24 号最后 current `0860037c29fd448e6b114e0897436b67aa7cc0edeaeb427674888949c022ef07` 的 Phi 为 886.6498827366873，Gram 为 0.4729659923630599，reach 为 +0.6114243730497866，distance-plus 为 +0.06086507728771828。下一 `90c83f96571608d3fa3dfd12cbf75255fa7dc2d3aa4a7da103cffdc127cc3839` 的统计不构成新的接受或完整场。

25 号原独立科学自然返回 0，耗时 9668.217378869 秒；原 pure 自然返回 0，耗时 313.30434169100045 秒。原完整点为 `a28ae9998fb54207f0ccccd1a9abdf0e89beff1025f5e01334b856b21d3da3cf`，Phi 为 681.6450227773521，Gram 为 0.40616533555531326，reach 为 +0.5225620087197518，typed memory 为 13 条。stop 是 `declared_restoration_budget; actual_violation_remains_and_is_not_accepted`，不是可行性通过。最终 bundle SHA-256 为 `de44d265d795c4c4686dbc0fcf2273c06219644611b61c9fe2d7ab4b24bb7b1f`；它只来自本次原完整 report 与 verify-final-bundle pure，不是从实时进度取点。

25 号原 science 的 458 个 formal selector 返回 439 项、记录 19 个 summary error；pure 的 445 个 selector 返回 423 项、记录 22 个 summary error。这些原已公开值和缺项边界完整保留，不把 exit0 扩写成所有 selector 或所有科学条件成功。原完整 stage JSON 里不存在的私有 runner journal 细节不在本批编造。

后来的 restart01 使用原完整 report/final 和全部真实 typed/history，原算法、137 source roles、19 runtime files、全部预算不变；只是合法同源续跑模式的 140 词 science argv。其 quarter-step `596a530c788e88ccb94ecbdd0f16d4df3bd349d9fd460ac3516b55173cef2e90` 已拒绝；之后 eighth-step `8f375b5d6745979dbe42f3e3aad3143b7b9ed896eac3543b4fe780b8007cf8da` 只有自己的统计。取消前 restart 的新 final、typed、接受仍未知。原 accepted4 与 restart accepted0 分属不同调用，不能合并或覆盖。

## 3. 完整公开记录怎样保留

两个新结果文件按完整运行分组：

- `terminal-runs22-25-retention97-complete-run22-to-run24-results.json`：完整六个已返回输入阶段，及三个运行各自完整的末观察对象。
- `terminal-runs22-25-retention97-complete-run25-results.json`：完整四个已返回阶段，及 restart01 的完整末观察对象。

每个原 JSON fence 的对象从开括号到闭括号完整保留，只删除字符串外 ASCII 空白；所有数值字面、字符串、转义、字段顺序、数组顺序都保持。没有选取一部分 metrics 替代完整原 stage。已有的完整 source/command/input/output SHA、秒数、scope、parent identity、全部公开标量和 observation errors 都在其中；它们不是新计算值。原 Markdown 的标题、时间戳、分卷边界与精确序列化则由九个固定完整 Git 文件恢复。

索引中的完整 request 与保留 request 的解析值完全相同。23 号经原 controller 的 JSON 序列化后个别 token 写法不完全相同，因此账本没有冒称其请求 fence 与 request 原字一致；精确两种历史正文分别由各自 whole identity 恢复。其它三个请求的字符串外空白规范化 token 也逐字相同。

独立人写 note 的全部叙述、数值表、失败、未知与时间顺序保持原样。22–24 的 RET84 原 JSON-fence 完整引用仍指向其固定旧全文；25 的 83,007 字节原完整人写 note 不改。这里不把那些完整历史引用误列为当前文件的旧字节 guard。

## 4. 已实际读取的生成与消费链

四个 controller 的完整 `Publisher.render` 读取 runner `status.completed`、有界 active-progress 与整个原 request；`Publisher.publish` 写出这九个 index/part 以及自己的 HANDOFF slot。22→23/24 仅 slot/name 文字不同。25 还使用完整 geometry-location followup，公示进度的 bound 对应扩大；原数学求解不在这些行政模块中。

`_Followups.poll/begin` 读取完整 queue 并核 parent request，建立真实 source commit 的独立工作树，按完整 argv 运行程序；只做原 `{repo}/{work}` 替换。它把每次完整 command、source、输入和 parent bundle 的真实 SHA 写入 runner journal。科学输入不是这些 Markdown。

`run_step/finish_record/save` 只在真实子进程自然返回后读取原 outputs 与 summary，先保存完整 runner status/journal，再发布有界 metadata。每次 source commit、输出 whole 身份、缺项和错误按原记录保留。实时观察是两次完整有界读取；22–24 保原 48 selectors，25 保原 64 selectors。它没有把试探点统计当成 accepted 或 final。

历史人写 note、restart binding、delivery 与旧读者可能按路径或 SHA 引用这些 Markdown，因此没有“没有消费者”的泛化断言。需要原 whole 的读者须在独立历史 checkout 恢复该原完整对象；本批结果索引不能代替某个依赖原字节的消费者。

## 5. 全部科学源、参数和输入责任

保留每个运行的全 request、真实 queue、完整 science/pure ready、source delivery 和完整 source registry：22/24/25 的 137 roles 与 23 的 138 roles 各自严格，23 多出的真实 policy 角色不删。账本的 `whole_file` 引用只消除重复列写同一 metadata record；完整 path/bytes/SHA-256/Gitblob/restore commit 均在同一账本的明确 catalog，按零基 index 完整解析。

原 M160/J923/N2048、32 normal stages、完整原域、自由变量、8-Gauss、各 root/backtrack/LM/line-trial/angle-block 预算都保留。science 原 157 词、pure 原 7 词与 458/445 formal selectors 不变；25 restart 的原 140 词与全部 458/445、64 live selectors 同样完整保留。350 分钟 workflow、20000 秒 controller admission、Python3.12.14、NumPy2.3.5、SciPy1.17.0、Torch2.5.1 CPU 与原环境线程参数均由完整 workflow/request/argv 记录，未为容量减配。

四个 independent 分支的 maker/ref source 分别是原完整 89cc/e717。maker 依固定公开提交 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 恢复 accepted099 原完整输入，只消费原 scalar 参数投影，随后确定性建立七模 RN-even chart、923 affine nodes 与全部标量账。reference 保 2218 counted-tail、7377 carrier、全部原八点 Gauss 和实际 scalar accuracy=false 的诚实边界。每个运行均自己真实生成输入，没有借用别的运行的 report、point 或 packet。原全6/26输入 argv、14/62 summary 与所有输入返回身份保持。

原25restart 是明确的真实父 report/final 消费者。终态后不能把这份 metadata 当作另一个 runner 的 raw checkpoint；若新执行需重新生成完整输入和科学场，必须如实记录新结果，不能保证旧点、旧时间或旧接受过程逐字重复。

## 6. 执行范围

本批没有科学执行、AST、fixture、benchmark、重放或新准入门。没有修改任何 request、queue、workflow、源码或 ref，也没有重演网络取消/发布时间。只交完整小工件和精确删除条目给 root 普通发布。

发布者当前 guard 只使用账本 `current_retained_guards`；历史 queue、RET84 前 note 与外层 workflow 分列，不能把历史 whole 冒作当前。固定 Git 恢复是维护原结论和原 whole 消费者的责任，不是要求用户先批准一场新科学重跑。
