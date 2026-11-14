# 独立 seed8000 两条成功后计划的完整独审

审者：Astra-visible-flex-78718bd0 / independent_audit，2026-11-10。
可信度：**四件新源、完整文本派生、真实 actor 成功接口和两后链接线通过；审者实际重跑静态闭包与两个错 actor 负门。**
本审不是候选优化，不选择种子、模式、节点预算或物理参数，不构造成功 CP，不运行 producer。本人的独立主求解后来按 root 的资源调度真实启动，观察记录与本纯计划审查分别保存；它尚不能由本审报告判定成功。

## 1. 冻结对象及完整阅读

| 文件 | B | SHA256 |
|---|---:|---|
| [78718-build-independent-post-plans-v1.py](../scripts/78718-build-independent-post-plans-v1.py) | 11273 | `e62c201b15355687f9645690b4e3d57e0341348cafd853e2d38d8bfb7b60f461` |
| [78718-plan-post-independent-seed8000-v1.py](../scripts/78718-plan-post-independent-seed8000-v1.py) | 32715 | `b3526176d56179a3edce6a71a159591a1e9f5ceecd9d253a4eeec95887e07053` |
| [78718-plan-post-independent-seed8000-storage-v2.py](../scripts/78718-plan-post-independent-seed8000-storage-v2.py) | 20428 | `c94d7b8204ad8184a181fc6d8b4b9b495f3dd0d9fdf3609f6ea23168ed4fc223` |
| [78718-check-independent-post-plans-v1.py](../scripts/78718-check-independent-post-plans-v1.py) | 9298 | `184664829bec0f529eb8f48c997bedf15ba30497ad6659d3d142ec3775924281` |
| [numerical-independent-post-plans-derivation-01.json](2026-11-10-78718-numerical-independent-post-plans-derivation-01.json) | 11863 | `c85e5953bfb4298c765c59e4e03fa9a1a13b938e4cebaa2b56957fc10dbf13ac` |
| [numerical-independent-post-plans-source-diff-01.txt](2026-11-10-78718-numerical-independent-post-plans-source-diff-01.txt) | 10465 | `38537c125310eadc6f15862d780034e3edc8ea27c515859732fe4d883d05b8c4` |
| [numerical-independent-post-plans-v1.md](2026-11-10-78718-numerical-independent-post-plans-v1.md) | 14775 | `38176916ac630b05e36183916486fbe90253bb91f4039d4eaf9316413fd1b14d` |
| [numerical-independent-post-plans-frozen-entry-01.json](2026-11-10-78718-numerical-independent-post-plans-frozen-entry-01.json) | 12103 | `d354a41f9ba54a0d2f8f943f6a8f4e7b90b4215bc5b947e3a9a126953134cbc2` |

本人已全文读四源、完整 diff 和完整说明。读取覆盖为：builder `18b74c`、checker `648ef8`；独立基底 `8275d1/ec459a/7ffb7a`；独立存储包装 `7f60a9/f34110`；全 diff `7c86c3`；说明 `41c893`。没有用局部 grep 代替完整新源码审查，也没有把导入/compile 当实际生产运行。

原两计划源保持：root 原单容器 `c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456`，root 存储 v2 `99c053a1563a31c94de2b2d9b99db70aad603c2bafa89f023abc69800748badc`。其前置完整独审分别见 [原计划审稿](2026-11-10-78718-audit-post-restart8000-plan-v1.md)（SHA `e53db48be38381a3e793fb2e2b016b0c0ba51c3ea8acf9fb0c530fadf736cdfb`）与 [root 存储计划审稿](2026-11-10-78718-audit-post-restart8000-storage-v2.md)（SHA `d0b677402a799510f980467564562f17ef24a305e853d1b0e4f8a01c21dd7ecd`）。本审不把它们的实际回执迁移到新入口。

## 2. 完整文本派生：17 + 11 项而非运行时改身份

builder 只读/写源码和来源元数据，导入模块仅为 argparse、ast、difflib、hashlib、json、pathlib。它不导入 planner、auditor、数值后端或存储 adapter。先按完整 SHA 核两个祖先、已审独立 final auditor 及主入口完整审稿，再执行声明的两组替换。

每个旧字符串必须在当时完整文本中恰好出现一次，且与新字符串不同；顺序逐项记账。派生后 compile，但不执行。对所有顶层函数要求集合相同，并比较完整 AST；两件输出源如果已存在，只接受完全相同字节，不覆盖不同源。账本和 diff 也必须为 notes 下的新文件，用排他写入。

基底的 **17 项**只涉及：模块说明、独立 auditor 的名称/SHA、launch schema、完整成功状态、导入模块名、报错文句、独立生产目录前缀、final 的观察字段和绑定角色、计划 schema/status/观察字段及准确的原种子范围说明。存储包装的 **11 项**只涉及：说明、独立基底名称/SHA、模块名/报错、独立存储目录、注释和自身 schema/status。

完整 diff 显示没有其它修改。12 个基底函数 AST 全同，仅 `audited_success` 和 `build` 含上述身份字符串变化；8 个包装函数 AST 全同，仅 `load_base` 和 `build` 含上述身份变化。特别：

- `verify_fixed_inputs`、`command_plan` 整个 AST 与原单容器基底相同。
- `verify_storage_inputs`、`replace_command_records`、`static_command_names` 整个 AST 与已审 root 存储包装相同。

顶层类、其它赋值、导入及全部函数外文本也受完整逐字重建和完整 diff 约束，不能只靠函数 AST 数量冒称全文件不变。新入口是另名文件，不通过 import root-only 模块后篡改 globals 来伪造独立 actor。

## 3. 真正独立成功谓词

独立基底自己的常量为：

| 项目 | 精确值 |
|---|---|
| auditor | `78718-prefix-audit-independent-seed8000-v1.py` |
| auditor SHA | `067f8944cb0d75ceffc846119b1ca2511f0e6e886799258e4659b023d8828578` |
| launch schema | `78718-true-m14-w14-independent-seed8000-launch-v1` |
| 完整成功状态 | `PASS_INDEPENDENT_OBSERVED_SEED8000_M14_W14_FINITE_COUPLED_CLOSE` |
| final 观察字段 | `independent_observation` |
| 计划观察字段 | `independent_actual_exit_observation` |
| 生产目录前缀 | `2026-11-10-78718-independent-post-seed8000-` |

`audited_success` 要求精确冻结主解释器，先钉完整独立 auditor 文件，再读取真实 launch、核 schema、调用该 auditor 的 `c.validate_inputs`，并核实际 launch 路径就是 context 的绑定路径。

随后直接调用已审独立 `final_audit`，按其真正 CLI 的外层字段构造完整新鲜报告，要求完整成功状态，并把新鲜报告与指定保存 final 用 canonical JSON 逐字段比较。没有把审核改成只看一行状态或只看 guard；缺 PP、outer、BC、自有最后 DN、typed runtime/callback 闭包、输入或关闭输出等任一原门，完整 auditor 都不会产生成功结果。

已审独立 final 的 actor 门固定要求 `/root/independent_audit`、对应 stem、真实整数自然 exit 0、真实 receipt、结束返回不带活动 session，以及固定独立 recorder 实物和完整 tool-return 元数据一致。这个观察是已审入口的实质条件，不能用 root 的真实退出或 guard 的子进程字段代付。

记录器本身不提供密码学身份认证；其约定执行者必须真的持有并提交自己的工具返回。新 planner 没有调用 recorder，也不产生观察。主入口完整独审和实际观察责任见 [independent-seed8000-entry-v1 审稿](2026-11-10-78718-audit-independent-seed8000-entry-v1.md)，SHA `4bf8d07536b0df21f824bf06ba753af3905d6db252744b46b58fadf0aeeff9e3`。

## 4. 自有 CP、自有末尾和关闭文件不借用

完整 final 成功后，CP 路径只能来自实际 `prefix_CP`。代码立即重哈希，与 final 的完整身份比较；再从该 CP 自己的 `tail_seam.tail_record` 解析尾包路径，并要求名称精确等于该 context stem 加实际 `tail_calls` 序号。末包须出现在完整 final 的 `required_closed_files` 中，当前实物身份完全相同。

还要求 CP 的物理 linear port SHA 为固定原值 `500e0a0c6d5388e07e3673ef192856804264c612edd6fe26ee09b882698a3702`。这一步不从 root 的尾包、旧失败 CP、另一图的保存摘要或方便的文件名选择数据。

独立 `build` 要求生产目录是 notes 下的新独立命名空间且完全不存在，计划输出也新且不在该未来目录内。它先执行上述完整成功谓词，再核固定输入；把 launch 的全部绑定、final 必需输出、reproduction、`independent_observation`、实际 launch/final、auditor、解释器与本计划源全部实物重哈希后，才调用 `command_plan`。

因此真实主求解的 start 观察不够，活动 trace 不够，入口预检通过不够，未知进程状态不够。它不预填未来成功 CP 或 SHA，也不在纯规划阶段创建生产目录。

## 5. 完整数学后链保持不变

`verify_fixed_inputs` 与 `command_plan` 的完整 AST 相同，且完整 source diff 没有其它文字变化。这保留原 43 source-root 文件、M8 底图及其 8 raw、tight/lowmetric 背景与六定义、原固定证明和全部 terminal reference 来源。

完整 `command_plan` 源码仍给 40 个条件未来命令和 16 个未解析 mesh/独立输入模板；这个数量来自源码结构，不是本轮实际生成了候选命令。关键参数均原样：

- tail exporter：depth8、steps32、flow32、angular512、degree192、原 critical 网格和完整 audit；必须保存后来完成的实际 collar。
- mirror prefix：M24、angular768、quadrature8、subdivide1、ell0，外层原 file-cap 为 4,999,999；实际 CP、原 physical port 和 source-root。
- supplier、base metric、exact bridge、common-cut make width .15，以及本图完整 geometry/metric/moment；不以局部区间 pilot 替代完整 angular。
- tail-full、必要时本图 lowmetric 和 metric-only/completeness；whole 只有实际使用 metric-only 时才传对应参数。
- baseline/angular 与 full/metric-only 的四条最终路线互斥；closed budget、held/H/reach、原 background 等全部门保留。
- 正常 terminal 的精确 B 仍为 `1/500000000`，且必须使用真实旧 M12 下界和原来源；普通 whole 的 $10^{-6}$ 通过不足。
- mesh plan/build 参数 angular144/prefix128/tail64/collar4/cap12，PL 的实际 t=0、1/4、1/2 文件仍由真实闭存 manifest 解析，不能预猜 .ply/.ply.gz、size 或 SHA。

每步的实际自然出口、全部自有输入/输出闭存、同一图连续证书和 README 条件仍然必需。same-plan mesh manifest 比较不代替未参与者原种子 solver→tail→prefix→certificate→mesh 全链。有限数值通过也不自动变成严格无限尾存在定理。

## 6. 独立存储包装确实接独立基底

包装的 `BASE_NAME` 是新独立基底，`BASE_SHA` 恰为 `b3526176…`，`load_base` 先核实字节再导入。它的 `build` 先检查更窄的独立存储目录前缀，再直接调用这个独立 `base.build(args)`。不会回去调用 root-only 成功门。

只有完整独立成功后才核存储家族并对内存计划副本做九类 CLI 路径替换。下列内容与已审 root 存储 v2 保持完整同一字节/AST：

- 全部 16 件 family SHA：两个 core、四件修正 v2、其它十件不变 adapter。
- ledger-03 的 14 项来源、两个 core 和完整新旧实物大小/SHA。
- terminal 的 13 件新 prefix pins、21 件不变 tail/reference pins、angular 的 11 件 pins；`BOUND/FACTOR/LOWER/REFERENCE` 完整赋值 AST；新 reviewer 绑定实际新 exporter。
- 九类 CLI 的完整绝对路径替换，source/additional_sources 同步，逐记录逆替换后的全字段比较。
- defining M24 base、M64 expanded metadata 的区别，descriptor/parts/helper/codec 的完整身份，logical gzip/NPZ 字节同一性及单件大小要求。

唯一另外变更的 prefix 完成文字仍是已审的资源闭存要求。所有数值参数、条件、依赖、输出名、whole 选择、mesh 模板保持。顶层原独立基底作为 ancestor 保留，新 wrapper 作为自身来源绑定；最终所有主 source/additional source 都必须在实际闭包内。

存储 `PROVENANCE` 中保留原 plan-v1 审稿是对未改算法来源的引用，不是把原稿的执行结果冒充新独立计划已执行。新计划本身由当前完整审查补齐。

## 7. 来源分片语义和条件分支边界

本轮没有重新发明 codec 或导入 adapter。前序完整存储独审证明连续字节分片还原原始 logical gzip/NPZ 字节串；完整 SHA 仍指该串，raw part 上限 4,600,000，物理文件小于 5,000,000。正负零、NaN payload、dtype、shape 和 order 由字节同一性保持。

新包装只消费那套已审四件 v2 加十二件不变源，不混历史 routing-v1、缺字节旧 A/B 或旧 terminal 源。原 tail/reference、whole/bridge、height sampler、PLY/PL 的格式和来源不改变，其消费范围已在完整 family 和 root wrapper 审稿中核清。

原单容器仍是实际首选；新包装不会从节点数猜超限，也不自动切换，`storage_branch_selected_or_activated=false`。只有后来真实观察到单容器资源需要时，调用者才选择该另名支路，并在另一个未使用的生产目录实际执行。保留真实单容器失败，不覆盖其输出。

## 8. 纯 checker 的完整实际工作

checker 对自身执行要求精确冻结解释器，先核两 planner 和 ledger SHA。它导入两个纯 planner 的定义，不改 root-only globals；再按 ledger 对两份实际祖先文本重放每一项唯一替换，要求新文本逐字相同，重建完整 unified diff 并核其全部字节。

它还核所有函数集合/AST 的声明、特别受保护的 route 函数，准确独立 auditor、launch/schema/status 及存储 wrapper 的独立基底连接。随后只调用 `verify_fixed_inputs` 和 `verify_storage_inputs`，把所有来源逐角色重绑，核 22 个字面 command source 全在实物闭包，且不导入 NumPy/SciPy。

本次 `36fc62` 真实静态重放因此不仅是 compile：包含 17+11 全文变换、全 diff、完整函数 AST 比较、所有 fixed/storage 输入哈希。它没有调用成功 `build`、`command_plan`、`replace_command_records`，没有生成一个伪候选 argv。没有真实成功输入时，来源验证与成功后实际执行必须分开记。

## 9. 审者亲手执行的回执

### 9.1 完整静态闭包

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-check-independent-post-plans-v1.py \
  --out notes/2026-11-10-78718-audit-independent-post-plans-static-01.json
```

真实工具 `36fc62`，自然 exit 0。报告 [audit-independent-post-plans-static-01.json](2026-11-10-78718-audit-independent-post-plans-static-01.json)，66,465 B，SHA
`58e9a1297373ed5c17901d417a55db62ca5a6eb8a6a83585ef10b83566b2d8bf`。
127 件原固定绑定、56 件存储绑定，连同派生/入口等合并为 166 件唯一实物；16 家族、9 CLI、13+21+11 pins 通过。0 数学后端导入、0 solver/producer、0 候选 argv。与作者确定性报告内容相同，真实执行回执则为本人这次的 `36fc62`。

### 9.2 两入口拒绝真实 root 观察

对真实已准备的独立 launch，分别调用两个新入口，传入旧 direct-csc-02 的真实 root 观察，使用明确不存在的 final 和全新未创建生产目录。没有伪造任何观察、成功状态、CP 或回执。

- 原单容器入口：真实 `8848ed`，自然 exit 2，拒绝 `Wrong actual independent observation identity`。报告 [negative-original-root-01.json](2026-11-10-78718-audit-independent-post-plans-negative-original-root-01.json)，276 B，SHA `c20692bf731dafc4035d1bcec9bb05a90a46676cdd33088e5c4e3a219a0eba59`。
- 存储入口：真实 `82142a`，自然 exit 2，同样拒绝实际 actor/run 身份。报告 [negative-storage-root-01.json](2026-11-10-78718-audit-independent-post-plans-negative-storage-root-01.json)，325 B，SHA `23115909291e6d4688eb5deb5829edb0f896960beb1b30e92eb5d4c636c6be88`。

两个报告都为 0 argv/producer/solver，两个未来目录均不存在。作者的缺观察负例 `2b9509/774331` 和其它负例属于其真实历史；本人已读冻结 argv 和记录，但不重复充分的缺文件测试，也不把作者回执写成本人执行。

`08d2de` 自然 exit 0，随后只读核冻结清单所列 12 件实物大小/SHA、本人静态报告与作者报告逐字段相同、两新未来目录仍不存在。报告确认基底 17 替换/12 不变函数、包装 11 替换/8 不变函数，以及 26 个缺失参照对象和 1 个待头部解析后代。

本人没有另跑 builder 写源；checker 已对完整文本实际重建，足够解决当前来源风险。也没有重复完整存储 reader 试验或任意扩大测试。

## 10. 当前主求解和后链之间的准确边界

这两后链审查期间，root 在自己的主运行真实自然结束后，明确安排本人执行已审的独立公开 M14/自有 0002/max8000 主入口。本人实际启动为 `7d2471`、session `23125`，固定独立 recorder `e78093` 自然 exit 0 写出启动观察 2,074 B，SHA
`9d4fdb7c7d03b65668619b9ac3ad2dd1f35c693ee7393dd0d5763aae2ef93445`。
该记录只说明启动，尚非自然成功出口。本人的独占持续工具观察另行保存；本计划审查不借 root 的退出、也不由启动信息生成正向计划。

这次源审/负门没有消费任何 root solver session，没有修改独立主运行的输入、参数或源，也不构成参与主候选优化。后链以后若成功消费输入，必须用本人真正收到的自然退出回执和相应完整 final，届时所有图和证书属于独立运行自己。

如果其有限图与 root 图的字节不同，不能交换 CP、尾包、连续证书或 mesh。应分别完成同一图自己的完整链，并准确记差异，再按 README 判断最终目标。后链纯计划的 `plan_ready=true` 也只表示未来命令与成功输入绑定，不代表生产已经通过。

## 11. 保留的缺件和最终义务

当前静态结果仍为 `terminal_reference_ready=false`：26 件旧 M12 参照对象待取，另有一份由真实 packet 头部决定的数据后代。它们只记录 expected 身份，未谎称已实核。正常终门消费前必须实际取齐；新 actor 和新存储都不删除旧下界门。

原种子主计算、完整自有生产链、真实 continuous/normal terminal、网格/PL、全时几何与进一步幅度/reach 目标仍须实际完成。本文没有新成功 CP，没有实际后链运行，没有最终课题完成声明。

**最终审查意见：四件新源及两后链所声明的独立 actor 接口、完整来源和不变数学路由通过，无实质订正项。保留为已审纯计划入口，真实成功后方可按自有数据实际执行。**
