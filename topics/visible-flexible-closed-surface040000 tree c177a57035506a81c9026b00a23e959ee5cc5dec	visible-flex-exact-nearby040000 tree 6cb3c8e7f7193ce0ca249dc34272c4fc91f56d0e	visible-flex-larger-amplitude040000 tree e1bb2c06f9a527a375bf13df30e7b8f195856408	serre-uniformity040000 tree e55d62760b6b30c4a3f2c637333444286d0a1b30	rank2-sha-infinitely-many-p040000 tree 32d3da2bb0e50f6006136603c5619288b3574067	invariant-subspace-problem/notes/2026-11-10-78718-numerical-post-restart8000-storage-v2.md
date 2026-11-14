# restart8000 后链的另名存储 v2 条件计划

日期：2026-11-10；作者 `/root/numerical_recovery`；会话 Astra-visible-flex-78718bd0。

本稿冻结一个**纯计划入口**，将已全文独审的 16 件新存储源明确接到 root
restart8000 的成功后生产链。没有执行 producer、solver、候选初始化、几何证书或
网格导出，没有产生新成功 CP，也没有宣称主运行已经成功。原单容器计划保持原字节，
仍为实际首选；只有真实单容器大小需要出现时，才选择这条另名资源支路。

完整存储家族已通过 [v2 独审](2026-11-10-78718-audit-storage-family-v2.md)；
本计划器的全文独审在本稿冻结时尚待执行。家族的来源/字节语义通过与新候选实际通过
生产链是不同事实。以下实际检查均明确没有构造候选 argv。

## 1. 两件新源与不变的成功门

| 文件 | B | SHA256 |
| --- | ---: | --- |
| `scripts/78718-plan-post-restart8000-storage-v2.py` | 20326 | `99c053a1563a31c94de2b2d9b99db70aad603c2bafa89f023abc69800748badc` |
| `scripts/78718-check-post-restart8000-storage-v2.py` | 4988 | `c0a25ca74795429f6cd68cca0ae473957cc92dc4760c5fbc6170c33ebd4a0841` |
| 不变原入口 `scripts/78718-plan-post-restart8000-v1.py` | 32491 | `c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456` |

新计划器是独立文件，先校验原计划器完整 SHA，再 import 其定义并直接调用原
`base.build(args)`。它不覆写函数、常量、成功状态或模块绑定，不以局部首 DN、
程序自报状态或 guard 状态取代 root 的真实工具自然出口。

因此它完整继承 [原计划及实际输入说明](2026-11-10-78718-numerical-post-restart8000-chain.md)
§§1–3 的真实成功谓词：固定新 final auditor、原 `validate_inputs`、完整 `final_audit`、
新鲜审计报告与指定已保存 final 报告逐字段相同、真实 root exit 0、完整 PP/outer/BC/
自有末 DN/源码/运行期绑定。必须得到
`PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE`。
CP 路径与自有最后 `tail_seam.tail_record` 由完整成功审计实际解析；未知未来路径或 SHA
不能填写为已经观察到的输入。失败 run02、状态未知的 restart8000-01 不能给本计划正入口。

这是 **root restart8000** 的后链入口。独立 seed8000 的固定 actor 是
`/root/independent_audit`，完整成功报告字段为 `independent_observation`，其 launch/schema/
成功状态也另名。本入口不会接受或改写那个身份；若它以后有真实成功，使用另名并经过
完整核审的对应后链入口。不能把独立执行者的观察伪写为 `/root`。

## 2. 全部实际改变：九个 CLI 文件族与来源记录

原完整 `build` 通过后，新代码只对其内存中的计划副本执行以下准确路径替换。
比较使用完整绝对脚本路径，不按子串匹配文件名，也不遍历替换一般参数。

| 原计划 CLI | 新支路 CLI | 对应任务 |
| --- | --- | --- |
| `db6f-root-mirror-hermite.py` | `78718-prefix-mirror-hermite-storage-v1.py` | 保留原 file-cap 外层，替换内部 producer 及其 additional source |
| `db6f-audit-metric-supplier.py` | `78718-prefix-metric-supplier-storage-v1.py` | 同一解析目标供应包 |
| `db6f-audit-metric-polynomial.py` | `78718-prefix-metric-polynomial-storage-v1.py` | 基础图完整 metric |
| `db6f-root-common-cut-v2.py` | `78718-prefix-common-cut-storage-v1.py` | make、geometry、metric、moment 四任务 |
| `db6f-audit-prefix-angular-metric.py` | `78718-prefix-angular-metric-storage-v2.py` | 必要时完整角弧认证 |
| `db6f-audit-closed-budget-transfer-v3.py` | `78718-prefix-closed-budget-storage-v1.py` | 同一图闭预算 |
| `db6f-audit-terminal-error-gate.py` | `78718-prefix-terminal-error-storage-v2.py` | 正常完整原 2e−9 终门 |
| `db6f-export-closed-mesh.py` | `78718-prefix-export-closed-mesh-storage-v1.py` | 同一图 mesh plan/build |
| `db6f-tail-review-closed-mesh.py` | `78718-prefix-review-closed-mesh-storage-v1.py` | 实际独立 same-plan mesh manifest 的比较模板 |

new `source`、`additional_sources` 的路径/大小/SHA 与这些实际新脚本同步；原执行参数、
依赖、条件、输出名字、whole 的可选参数和 mesh 文件解析模板都保持。源码逐条保存
真正替换的 argv 索引，并只撤销这些索引和对应 source 后与原记录作全字段比较，
从而不能把任何数值参数变化藏在“路径替换”内。九个来源均必须在实际原计划中被用到，
且未来计划中不能残留这九个旧 CLI 路径。

唯一另外改变的单步文字字段是 `prefix-base.completion_requirement`：它明确实际
defining M24 base、descriptor、所有分片的闭存/大小/SHA要求。整个计划的 schema、status
和 planner 自绑定另名；原 plan-v1 的来源仍保留为 ancestor。新代码追加完整来源与替换
账本，明确 `storage_branch_selected_or_activated=false`。`branch_policy.storage` 说明资源
条件，但不自动选择分支。没有新增数学验收门。

以下原门保持：完整 final success；自有 CP/自有末尾；原物理 g 与源背景；全域而非局部
prefix/tail 认证；同一闭图 whole/reach/held/H 条件；精确 `1/500000000`；真实 M12 旧图
误差下界及改善常数；同一图网格/固定帽/PL检查；最终未参与者原输入完整求解到网格复跑。

## 3. 完整 16 源闭包与存储等价的准确含义

所消费的是 [完整家族 v2 独审](2026-11-10-78718-audit-storage-family-v2.md) 中的
四件 v2 与另十二件原字节源，不能拿历史 routing-v1 中的四个旧 v1 名字混接：

| 类别 | 新源 |
| --- | --- |
| 两个 byte storage core | `78718-prefix-byte-shards-v1.py`、`78718-prefix-storage-v1.py` |
| producer / 两 reader | `78718-prefix-fullxyz-hermite-storage-v1.py`、`78718-prefix-mirror-hermite-storage-v1.py`、`78718-prefix-continuous-hermite-storage-v1.py` |
| 基础认证 | `78718-prefix-metric-polynomial-storage-v1.py`、`78718-prefix-metric-supplier-storage-v1.py`、`78718-prefix-volume-moment-storage-v1.py`、`78718-prefix-common-cut-storage-v1.py` |
| 已修正实际来源的三件角界源 | `78718-prefix-angular-arithmetic-storage-v2.py`、`78718-prefix-metric-budget-storage-v2.py`、`78718-prefix-angular-metric-storage-v2.py` |
| 闭预算与终门 | `78718-prefix-closed-budget-storage-v1.py`、`78718-prefix-terminal-error-storage-v2.py` |
| 网格 | `78718-prefix-export-closed-mesh-storage-v1.py`、`78718-prefix-review-closed-mesh-storage-v1.py` |

`verify_storage_inputs` 逐字 hard-pin 这 16 件源，并核 ledger-03 的 14 项原/新来源身份、
两个 core、14件原来源实物大小/SHA；不执行 builder 或 import adapter。它还直接从实际
AST 读取新 terminal 的13项 prefix pins、原21项 tail/reference pins和 angular 的11项
pins，每项实物重哈希。新 terminal 的 `BOUND`、`FACTOR`、`LOWER`、`REFERENCE` 完整
赋值 AST 与原终门全等。新 mesh reviewer 的固定 exporter SHA 必须匹配新实际 exporter。

完整引用的冻结证据为：

| 证据 | SHA256 |
| --- | --- |
| `storage-adapters-source-ledger-03.json` | `1b7e05df897d10e77c056151e2beb0b8eee1ea7e86e28fb9bdef9899b22a6dde` |
| `storage-provenance-fix-diff-03.txt` | `100fd59c1ca1281f8b455dbf4dc77c019cfc0e715fae38b453c6c18477fc9c9b` |
| `audit-storage-family-v1.md` | `4912e2cd32bb2df8b8095d1e93e968bbe9417aa357894114caddd22cda230093` |
| `audit-storage-family-v2.md` | `2fe0c4a0d62c0864a8e318c4ac5e07111c67f024e2d3319565a96bcc4a733b1f` |
| `audit-storage-v2-source-closure-01.json` | `7215eeda5b88d5895e804f659873762c348b8a3a15c19fbaaffa081c07a8a6dd` |
| `storage-readers-check-03.json` | `0cd8154250c031eb41304d07374f4b1cc7692b5be8b612c730e62b0abd4dcdb7` |
| `audit-post-restart8000-plan-v1.md` | `e53db48be38381a3e793fb2e2b016b0c0ba51c3ea8acf9fb0c530fadf736cdfb` |

表内文件均在 notes 下带 `2026-11-10-78718-` 前缀。builder-v3/checker-v2 也以其实际完整
SHA 绑定。此处的 source 检查不是再次执行全家族测试，完整语义证明沿用已审字节；
不会把来源报告视为新的几何证书。

该 codec 保留的是 producer 按原规则序列化并 gzip 后的 NPZ 字节串 P。`data_sha256`
继续为 P 的 SHA；P 的每个连续字节段不超过 4,600,000 B，再独立 gzip。reader 核 descriptor、
每片 SHA/长度、连续覆盖、完整 P 的 SHA，再由原 NumPy/精确读者解释其相同字节。
正负零、NaN payload、dtype/shape/order 不靠数值近似判等。它不是把数组重排或重算成
另一个“差不多”的数据集。此等价与实际合成覆盖见前置完整独审，本轮不重复声称实跑。

新 defining base 使用 `data_storage`，不再声称某个物理 `data_file` 的 SHA 就是完整 P
的 SHA。common-cut 的 M64 expanded metadata 与 defining M24 base 分开；实际 terminal
继续核 base/descriptor/parts/helper/codec 的完整绑定。原临时单容器失败输出保持不覆盖；
新支路使用完整新生产目录。

## 4. 保留的原消费者与各阶段参数

以下实际 CLI 完全不替换：tail endpoint export、radial invariant、collar check、first
bounds、背景 transfer-v3、full-tail、metric-only、complete-metric-report、exact bridge、
whole-metric-reach-v2、背景高度采样、PLY/PL 审计。它们继续使用原来源、原参数和当前
真实图自己的输出。新 `angular-arithmetic-storage-v2.py` 的独立 tail CLI 不在这条生产路由。

这项接线依据前置完整 review，而不只是按名字猜测：whole 和 bridge 消费 JSON/hash
证明；height sampler 消费 tail/radii/background；PL checker 消费 PLY。完整新终门分别绑定
13项新 prefix 与21项原 tail/reference；旧 M12 参照不随新存储改名。新 supplier 的 target
NPZ、尾背景 NPZ、mesh fixed mask 仍是各自的原格式，不是遗漏的 prefix descriptor 消费者。

所有数字沿用原 [后链命令](2026-11-10-78718-numerical-post-restart8000-chain.md)：

| 阶段 | 保持的参数及真实通过条件 |
| --- | --- |
| tail export | depth8 / steps32 / flow-steps32 / angular512 / degree192 / critical网格 / critical-cells0 / base64 / ratio.05 / endpoint.025 / difference.00005 / audit128 / fractions.25,.5,.75；必须实际完整 manifest、所有 shard 与后来写出的 collar |
| mirror prefix | M24 / angular768 / quadrature8 / subdivide1 / ell0；原物理 linear port、实际 CP、同一 source-root；外层 file-cap 保持4,999,999 |
| target / base metric / bridge | 使用本次新 base；基础 metric 是原 bridge 的实际输入，不能跳过后直接借旧 bridge |
| common-cut | make width.15；实际 correction start/width 由本图确定；geometry angular256/radial1；完整 metric 不以 parser 的 angular/radial 参数变相加密；moment angular512/radial1 |
| angular | 只有本图 baseline 经真实 eta 转移后未过原 B 时考虑；完整选中路线 budget2e−9/initial-arcs128/max-depth4；省略 `--intervals`，局部 pilot 不能充完整证书 |
| tail | 新 tight 背景包；full angular128/radial1/curvature6/direct8.5/block128；必要时自有 lowmetric 转包和 metric-only radial1/block128，并与同一 full curvature 做 completeness |
| closed budget / whole | 本图 geometry、selected complete metric、moment、tail-first、固定 H/positive-alpha、新背景绑定；只有实际使用 metric-only 才传对应 whole 可选参数 |
| terminal | 正常 forward candidate 模式，精确原 B=1/500000000，真实旧 M12 下界和所有原来源；普通 whole 1e−6 通过不足以付 G5 |
| mesh | angular144/prefix128/tail64/collar4/cap12；背景高度取本图 plan 的 radii；build 实际 t=0,1/4,1/2；按 manifest 真实 .ply 或 .ply.gz 名字/大小/SHA 解析 PL 参数 |

base/angular 与 full/metric-only 仍产生四条互斥最终路线。只选实际所需完整路线；计划不
选择、更不执行它们。same-plan 独立 mesh 比较要求真实独立建出的 manifest，不能代替
从原 seed 的完整 solver→tail→prefix→certificate→mesh 复跑。

## 5. 实际纯检查与负门

| 实际回执 | 自然退出 | 范围 |
| --- | ---: | --- |
| `d59369` | 0 | 初次源码 compile +元数据闭包；0候选 argv，无数据/producer/backend执行 |
| `d9dfc8` | 0 | 冻结 checker 真执行；127原固定绑定、56存储绑定合并159件；16源/9替换/13+21+11 pins；未 import NumPy/SciPy；0 solver/producer/生产 argv |
| `634795` | 2 | 真实 restart8000-02 launch +明确不存在的 observation；完整旧成功门拒绝，0 argv |
| `4b340e` | 2 | 同一 launch 借 run02 的真实失败 root observation；拒绝 `Wrong actual root observation identity`，0 argv |
| `f57656` | 0 | 再核新旧源/报告实际 SHA 和两个未来目录仍不存在；没有运行任何生产步骤 |

实际报告：

| 文件名在共同 `2026-11-10-78718-numerical-post-restart8000-storage-v2-` 前缀后 | B | SHA256 |
| --- | ---: | --- |
| `static-01.json` | 66508 | `446894565beab95320c320c15fac0f8c304aa1ac36a4e3e5f7043abb04799052` |
| `negative-missing-exit-01.json` | 315 | `f18bcad1471b6214677c2a98094e5ba9bc6641f9642d4ceffa87f476f03bb5d9` |
| `negative-wrong-run-01.json` | 318 | `a5ff186e3556b1eb3fa5639714d3c82538bdda454986cc40efeb283513da70ec` |

静态报告中的 `plan_ready=false`、`successful_main_claimed=false`、
`complete_final_audit_replayed=false` 与 `candidate_argv_constructed=false` 是实际范围。
没有成功 CP 时不造正例。原终门仍有26件 M12 参照对象缺失，以及由其中实际 packet 头部
才能确定的一份 data 后代；静态 report 不把 expected SHA 写成实际已经验证的 SHA。
这些最终旧参照应在真实终门需要前按原清单取齐，不作为提前重做整个主求解的理由。

静态复核只需新输出名字，不创建生产目录：

```sh
VF_REPO=/workspace/scratch/78718bd0c4a9/math-research
VF_T="$VF_REPO/topics/visible-flexible-closed-surface"
VF_S="$VF_T/scripts"
VF_N="$VF_T/notes"
VF_PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
cd "$VF_REPO"
"$VF_PY" "$VF_S/78718-check-post-restart8000-storage-v2.py" \
  --out "$VF_N/2026-11-10-78718-numerical-post-restart8000-storage-v2-static-02.json"
```

两负门的可重放 argv 均在冻结清单中保留；另换报告文件名和未创建的生产目录即可。
它们不是停止当前 solver 的命令，未使用或轮询 root 持有的 session 72917。

## 6. 真成功之后的具体调用

以下文件名是明确的**未来约定**，不是已经观察到的文件。实际 root exit0 和完整 final
仍须先产生；若 root 保存的观察名字另有安排，应传那一份真实已闭文件。不得从 guard
合成 exit 或改 actor，也不得将 active log/首尾包提前写成完整成功。

```sh
VF_REPO=/workspace/scratch/78718bd0c4a9/math-research
VF_T="$VF_REPO/topics/visible-flexible-closed-surface"
VF_S="$VF_T/scripts"
VF_N="$VF_T/notes"
VF_PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
VF_STEM=2026-11-10-78718-numerical-m14-restart8000-02
VF_LAUNCH="$VF_N/$VF_STEM-launch.json"
VF_OBS="$VF_N/$VF_STEM-root-observed-exit.json"
VF_FINAL="$VF_N/$VF_STEM-final-audit-01.json"
VF_STORAGE_PLAN="$VF_N/2026-11-10-78718-numerical-post-restart8000-storage-v2-plan-01.json"
VF_STORAGE_RUN="$VF_N/2026-11-10-78718-post-restart8000-storage-v2-run-01"
cd "$VF_REPO"

# 仅在已有真实 root exit0 后；若此 exact final 已实际完成，不重复覆盖它。
"$VF_PY" "$VF_S/78718-prefix-audit-restart8000-v1.py" \
  --launch "$VF_LAUNCH" --mode final --observed-execution "$VF_OBS" --out "$VF_FINAL"

# 纯计划，无 producer/solver；全部引用真实成功，不创建 VF_STORAGE_RUN。
"$VF_PY" "$VF_S/78718-plan-post-restart8000-storage-v2.py" \
  --launch "$VF_LAUNCH" --observed-execution "$VF_OBS" --final-audit "$VF_FINAL" \
  --run-directory "$VF_STORAGE_RUN" --out "$VF_STORAGE_PLAN"
```

存储计划需给 `ACTUAL_MAIN_SUCCESS_BOUND_CONDITIONAL_STORAGE_PLAN_ONLY`，其中
`plan_ready=true` 只表示成功输入已绑定、未来 argv 完整；不是生产通过。新命名空间
必须以 `2026-11-10-78718-post-restart8000-storage-v2-` 开头且完全不存在。
实际选择资源支路后才按 `directory_preparation` 创建目录，并按每个结构化 argv
和依赖逐项执行，不将 JSON 字符串当成 shell quoting。

每步保留真实 argv/cwd/environment、工具自然出口、输入/源码不变证据，以及全部自有
输出的大小/SHA/闭存字段。即使 producer 实际过了文件上限，也仍须完整的本图 prefix、
tail、closed budget、normal terminal、mesh/PL 和独立全链。所有文件单件小于5 MB，超过
1 MB 的数据压缩；本分片层只解决 prefix 容器，不假定未来其它输出自动满足上限。

原存储 A/B 的缺失字节状态、新78718的不同身份、旧失败运行与状态未知运行均保留。
本条件计划没有恢复旧进程、没有修改正在运行的主源或参数、没有改变当前数学问题的
完成标准。后续真实候选即使过门，仍按 README 核全时闭图和更强振幅目标。
