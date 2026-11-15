# Request128：从实际127第8批九参数启动原同worker完整112高度路径

作者：ChatGPT（amplitude 子任务）。日期：2026-11-15。

**类型：未执行的源码接线与显式数值实验设计。** 本项把已经公开的九控制完整112入口、原高度路径helper及其进程外壳接到一个独立Actions请求。下面的来源数字仅从实际127原JSON／日志字段复制；没有本地运行任何科学模块、native、FD、矩阵动作或测试场，也没有为Request128填写未来run、响应或接受结果。

## 1. 实际来源与本次实验

参数取自[实际127完整结果R290](../results/R290-actual127-eight-nine-control-batches-and-retained-final-responsibilities.md)的**第8批末点**。原run为 [43700393105](https://github.com/Rogerhu12/math-research-public/actions/runs/43700393105)，source为 `47bda30230e7aea8a85b5ecd039832c023249f87`；compute／report job分别为 `132770038307`／`132770558044`。此次选择确为原run最后一批，不是中间批或虚构的accepted场。

固定参数顺序为：

```text
[p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3]
[0.32187323564609926,
 0.21204423511345535,
 0.3992005008064338,
 -0.08290967451783622,
 -0.021154050830509367,
 0.8576496337449642,
 0.9744108740349993,
 0.6297613969180598,
 0.43487814523197305]
```

原参数来源的三个身份完整保留在recipe和request中：

| 原对象 | 字节数 | SHA-256 |
|---|---:|---|
| 第8批原 `nine-control-curved-status.json` | 1812905 | `1c4e24d005620ec08e87bf4450cd69e8d5d2f1203922a73cf122b1c9c859ab74` |
| 第8批compact primary | 62531 | `bc100938dfdc657560e84d52b49f5432cfb94c7b4e2d251bd1147ced09033bd5` |
| 第8批完整scalar view的canonical JSON | 117124 | `14c627634a1196c3ae144e17c6d2751caf3714cc7fcad1fcaae4e3751e1bca3b` |

原producer为 `geometry_20261115_small_core_nine_control_curved_recipe.py`，SHA `824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf`；原九族为 `geometry_20261115_small_core_nine_control_family.py`，SHA `086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629`；原批次外壳SHA为 `b15a6571a1ebc5dc72f1037212fd86a10d7a5848957c2faca4ae9e7fd69f21bb`。这三者的身份保留，不在Request128重新执行原小核心候选搜索。

原末点unit三项为 `[-4.717371832840097,-0.0018359077734816124,-8.732263938333927e-6]`，原merit为 `11.126800189953372`；unit阈值、完整一阶右端阈值、native以及非零场接受标志仍为false。原active前三列浮点最小奇异值 `5.317869964775124`、完整九列最小值 `12.921473215918594` 只是该原点已保存的数值记录，不承担根存在或严格rank证明。

本次新实验显式取 `lambda_target=0.001`、`initial_guess_kind=fresh-circle-low-three-linear`，M112／N2048。原末点的全部九系数定义新scalar族；前3个是完整设计场中的active坐标，后6个shape系数固定。原127的J、merit、field或native缓存不作为当前状态加载；入口真实重建圆／低三线性初猜、完整场及当前残差。低三尚未到阈值不会被新增成禁止有限正lambda实验的门。

recipe以 `initial_parameter_origin` 保存以上来源，供冻结reader直接选取；request的 `parameter_recipe.origin` 与它逐值一致。原127大status与完整view仅留下身份，不重新保存进main、Release或新artifact。正lambda是本请求的新参数，不声称原127已经计算过该非零场。

## 2. 四个发布文件及独立触发

| 发布位置 | 字节数 | SHA-256 |
|---|---:|---|
| `computations/actual127-batch8-nine-height-path128-lambda0p001-recipe.json` | 4868 | `739a2a00be77cdcc0c4596393da55335c16a07a361cf0a635b5b2f9228fdcff8` |
| `computations/public-nine-control-height-path-request.json` | 24859 | `2ef24cc239f609131dc1692557bd20be02a1236bb765a4df0e3c8c480537c0e5` |
| 根 `.github/workflows/visible-larger-public-nine-control-height-path.yml` | 17040 | `dcdcfe05b3efea538314884738c9f2b8c74412b6c8ea6cc4282f280c80700ff4` |
| `notes/2026-11-15-request128-actual127-nine-control-height-path-interface.md` | 本文 | 不自引用自身SHA；交付清单记录 |

前三者组成唯一新请求。workflow只在main上该课题 `computations/public-nine-control-height-path-request.json` 的push触发；独立concurrency group不取消已运行任务，没有另加第二个手动触发入口。旧124的workflow、request和科学源都不改。

request schema为 `public-nine-control-height-path-request-v1`，request number为128，lane为 `nineheightpath`。recipe schema为 `explicit-nine-control-height-path-nonzero112-recipe-v1`。全部输出属于新的实际运行，不能把原124的事件标签、原127状态或新的report成功改称科学接受。

## 3. 执行源、哈希基线与真实依赖

实际执行的三份九H源原字节不变：

| 角色 | 文件 | SHA-256 |
|---|---|---|
| 完整九控制设计场及H(s)入口 | `geometry_20261115_nine_control_height_continuation_full112.py` | `0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924` |
| 总预算／进程组外壳 | `root_20261115_nine_control_height_path_run.py` | `d075af46b0dc57aafa4b484eee292e309fcd83adcd95e7c0a30a2a534e770d5e` |
| 原字段读回 | `root_20261115_nine_control_height_path_scalar_readout.py` | `c756ede79cba7a4490f97801e8afe31e51e373a5e0946df89c7ab0f489ec2427` |
| 原完整112高度路径helper | `geometry_20261115_original_tail_height_path.py` | `e830a1679908cdc0cdd8c1ecd5663bbf6b82b24a3d52e44cf678aedc227eee48` |
| 原真实尾client | `exact_20261114_true_tail_client.py` | `1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09` |

原数学和生命周期合同见[九H适配器接口](2026-11-15-nine-control-same-worker-height-path-full112-interface.md)及[九H外壳／reader接口](2026-11-15-nine-control-height-path-runner-and-readout-interface.md)。本请求不重复实现solver、改变root、RHS、native Newton、完整FD或fullDN。

完整request含**110个源码SHA pin**：原124的103个逐个保留，新增7个为九族、九候选producer、九批次外壳、00e4九full112基线及本次0433／d075／c756。旧source同时存在不表示都执行：

- 807f六full112、557f六H入口及00e4九full112仅作原来源哈希基线；本次实际入口始终是0433。
- 原824c候选搜索和b15批次外壳只绑定参数来源，不在本次复跑搜索。
- 旧120／124外壳、旧reader及原publisher仍列在保留表中，但本workflow不调用它们。
- 0433实际显式 `closure` 合并有29项，全部包含在110项表中；29不是对所有传递import数量的冒称。
- 原 `prepare_public_source` 仍一次恢复完整78份原public来源；这与本课题110项来源／执行／运维pin的计数口径不同。

未连接same-g450消费者、closed SavedPrefix或未来的场重构dispatch；不把九scalar设计场冒成旧v3／v4 scalar身份。原入口仍为338个物理未知量、完整112 core及3个active标量，共453维；109个高core未知量保留，边界仍为左341行、右112行。九个设计量全部固定后的450维问题属于独立后继。

## 4. 四原输入与两个ready槽的临时恢复

四输入均从原公开历史commit `8bd267107cc8710d371f3b62c02986655ac965b0` 精确Git blob恢复到本请求RUNNER_TEMP。源文件路径、字节数及SHA逐项写在request；不依赖清理后main仍有旧data，不修改当前科学checkout。

| 原输入角色 | 字节数 | SHA-256 |
|---|---:|---|
| accepted，原free3 `stage-00/actual.json.gz` | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| 原M112 prepared | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 原零高度尾锚 | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原T112-config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

“accepted”是原输入的固定角色名，不表示它已经是当前九族／lambda的完整场。原零H锚只服务线性初猜；当前H响应必须新求。原config不含 `initialCheckpoint`，workflow在恢复原字节后记录这一事实；保原112／spacing2／N2048、solveTolerance `2e-9`、maxIterations32，不删字段、重写config或隐式采用另一个DEFAULT_CONFIG。

两个原几何ready输入沿113已修正机制恢复到原client现有环境槽：

| 环境槽 | Git blob | 字节数 | SHA-256 |
|---|---|---:|---|
| `VISIBLE_FLEX_FROZEN_LEDGER_READY` | `4fa8a8a7ae5d482cd0eaf35790db85201bbac4a3` | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| `VISIBLE_FLEX_FROZEN_STORED_READY` | `b6c44fe237750f13c8b10366f15525b481a74e09` | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

这是原几何来源，不是一个accepted尾缓存。原完整source恢复和ready槽共同供原worker使用；没有载入失败91／95／103checkpoint，也没有为了启动省略或替换原输入身份。

## 5. 原e830高度路径完整policy

本recipe和request同时保留原helper的全部policy字段，按原数值逐项一致：

| 项目 | 本请求显式值 |
|---|---|
| schema | `explicit-original-complete112-height-path-policy-v1` |
| 首个正增量 | `0.015625`，即1/64 |
| 接受后增量倍数／最大增量 | 2／0.25 |
| 明确原数学拒绝后的倍数／最小增量 | 0.5／`9.5367431640625e-7` |
| bootstrap请求总上限 | 64，包含零H和最终J请求 |
| 零H／中间出口J | false／false |
| 端点出口完整J | true |
| bootstrap audit | false；最终原audit仍须真实完成 |
| 端点全H词 | 直接使用原 `H_star` 全部浮点词 |
| 整体科学预算 | 18000秒 |
| 资源限制的解释 | partial，不宣称数学不存在 |

路径参数s缩放当前新初猜得到的**全112个H分量**。它不改变lambda，不是表面族相位，也不能只对低三分量续接。先在真正的新worker、空client缓存且无initialCheckpoint下求全零H；之后只有原native真实收敛才推进 `last_converged_s`。中间设置 `jacobian=false` 仅是不要求出口完整J，原内部Newton的withJ未取消。

只有原helper验证同源、同配置、同H、原record／trace明确且Python缓存未变的数学拒绝，才缩小正增量。IPC或记录不明、异常退出不会被猜成可缩步的数学拒绝。零H失败不推断正高度不存在；最小增量、次数及墙钟边界均诚实保留。

达到端点仍必须取得原 `jacobian=true` 的完整当前H响应。随后同一个owner/client/worker继续原实际H边界FD、完整fullDN及最终fresh native J／audit。原17次回溯、节点／中点／两套RMS、BC、材料域及真实tail更新全部保留。

## 6. 科学预算和原门

| 责任 | 原值／本次值 |
|---|---|
| 完整设计场外迭代 | 8 |
| 每轮原内回溯 | 17 |
| 每次原native Newton／line-search | 32／10 |
| 原collocation及冻结RMS容差 | `1e-6` |
| 原BC容差 | `1e-11` |
| 原native容差 | `2e-9` |
| 原完整边界FD阈值 | `5e-5` |
| jac workers／max nodes | 2／1200 |
| material／physical angles | 4096／4096 |
| node heap | 1536 |
| 总科学墙钟／science step／compute job | 300／330／350分钟 |

d075在启动科学子进程前建立同一monotonic截止，覆盖bootstrap、FD及完整DN。e830在请求间检查；外壳同时控制单个请求内部的墙钟及独立进程组，按原TERM／等待／KILL职责收尾。不会给每个高度重新发300分钟，也不把step／job的额外调度余量当作科学预算。预算中断保存partial，不把未达到阶段伪写成科学拒绝或完成。

本请求不传 `--prepare-only` 或 `--continuation`。原0433虽有真实own-schema场续接分支，本次d075命令只使用fresh-circle路线；没有偷偷提供未存在的完整场文件。只有原fullDN返回并设置真实新耦合接受，0433才可声明success；仅高度端点成功、FD成功或进程正常退出均不能替代该责任。

## 7. 运行环境、规则监控与输出生命周期

Python3.12.14、Node24.22.1、numpy2.3.5、scipy1.17.0、python-flint0.9.0沿原124，BLAS等线程数均1。checkout／setup actions保原固定commit。只作部分clone，恢复历史blob时不改变科学checkout `GITHUB_SHA`。setup保留 `git config --global merge.stat false`，避免规则pull的diffstat触及已清理大data。

原规则runner `root_20261114_current576_rules_runner.py`，SHA `3b8b6dd5eb5df373ffa14525f02e1a0376bafc2da91ce564631f771752e2afde`，代码不变。外层仅将BASELINES设为请求显式核过的当前两README：根blob `74c08a36f6c997d0bc1e64a7956b42276f5fa5d7`、课题blob `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。原2700秒真实pull／rebase、唯一规则同步行及规则变更停科学保持。H须保唯一 `规则同步记录：` 行与原10KB界限；这些是现存运行合同，不是新增数值判据。

新临时根为 `$RUNNER_TEMP/visible-nine-height-path-128`。原输入、78源临时副本、进程日志、field、native record及factor均在本请求临时树。reader与owned cleanup使用 `if: always()`；顺序为科学／partial结束、原字段读回、该请求临时树清理。cleanup先核目录不是symlink且严格在RUNNER_TEMP之下；清理错误单独记录，不改原科学接受结果。

没有artifact上传、Release上传或raw文件回写Git。原科学stdout事件直接保留在compute日志，reader只读取已有JSON／日志及文件SHA，不新求norm、J或FD。原helper事件名仍可含 `request124`，它标识冻结helper；外层request128、实际 `GITHUB_RUN_ID/GITHUB_SHA` 与新0433binding区分本次执行。

## 8. 90KB读回、真实接受身份与边界

冻结c756reader保 `scalar_summary`、`scalar_summary_bytes`、`scalar_summary_sha256` 三个GITHUB_OUTPUT键。report仅复述一份compact UTF-8 JSON并复核长度／SHA，使用：

```text
BEGIN_NINE_CONTROL_HEIGHT_PATH_SCALAR_SUMMARY
<实际原字段和实际阶段标志>
END_NINE_CONTROL_HEIGHT_PATH_SCALAR_SUMMARY
```

哈希不含标记和分隔换行。没有output时给小的unavailable对象；reader过大时沿原次序记录sectioncounts、缩减具名细节并标 `summary_complete=false`，必要时输出诚实失败对象。不会把缺少阶段用旧127、零H响应或旧FD补齐。report成功与真实科学子进程结果分开。

若将来真正通过全部原门，当前producer身份必须仍是：

```text
schema = nine-control-height-path-three-active-nonzero112-complete-physical-DN-v1
source_sha256 = 0433e1014a4d55ca52554ec5b17e9afa1d01a3b8e376d2afda890b26c35aa924
binding = nine_control_full112_implementation
```

binding保四输入、recipe、全部实际source闭包、完整九参数、六固定shape、三active、453责任及e830policy；只有真实端点完成才含 `completed_height_path_status`。最终field、response、audit仍是原完整求解器实际产物。本文并不声称目前已有这个accepted输出，也不把它改名成00e4、旧六族或same-g450以适配后继硬锁。

本实验即使通过完整非零设计场门，仍不代替独立same-g450求解／加密、封闭Cartesian装配、全t嵌入、reach或课题完成标准。现阶段的具体目标是把真实127参数作为显式初猜，在完整原方程和原门下实际尝试正lambda场。

## 9. 相对124的完整差异及本地检查范围

交付三份完整差异：`workflow-relative-to-original124.diff`、`request-relative-to-original124.diff`、`recipe-relative-to-original124.diff`。改动限于新九族入口／外壳／reader和namespace／trigger身份，实际127第8批参数出处，原source表增加7个来源，以及明确本请求的九系数／固定6／active3／453责任。原4输入、2ready、78来源恢复、e830policy、全部科学预算／门、规则runner代码和cleanup顺序不变。

本地完成的是原JSON字段复制、source byte/SHA与AST检查：110个实际源pin对应；原124全部103pin保留；显式runtime closure29项包含；9段Bash语法与6段inline Python AST通过。没有导入科学模块，没有执行workflow／reader／native，没有生成数值fixture、派发或写Git。静态回执仅用于说明这次源码准备的范围，不作为附加科学验收门，也不需归档进main。

本文件与三件请求文本可直接由主控普通发布；实际run、失败阶段、partial或成功，以及全部真实输出SHA，只能在随后公开Actions执行后记录。
