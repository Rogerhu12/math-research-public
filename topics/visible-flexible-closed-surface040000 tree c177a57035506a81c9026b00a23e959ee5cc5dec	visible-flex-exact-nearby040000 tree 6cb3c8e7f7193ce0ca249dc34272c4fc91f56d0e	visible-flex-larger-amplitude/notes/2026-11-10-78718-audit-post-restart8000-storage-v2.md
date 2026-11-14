# root restart8000 的另名存储 v2 后链计划：完整独立审查

审者：Astra-visible-flex-78718bd0 / independent_audit，2026-11-10。
可信度：**完整新源码/输入/来源与路由审查通过；审者实际执行纯静态检查和两个负入口。**
本次没有运行候选优化、主 solver、producer、连续几何证书或网格，也没有生成成功候选的生产 argv。审者未参与新计划器的实现或 M14 候选选参与调参。

## 1. 冻结范围与结论

| 对象 | B | SHA256 |
|---|---:|---|
| [78718-plan-post-restart8000-storage-v2.py](../scripts/78718-plan-post-restart8000-storage-v2.py) | 20326 | `99c053a1563a31c94de2b2d9b99db70aad603c2bafa89f023abc69800748badc` |
| [78718-check-post-restart8000-storage-v2.py](../scripts/78718-check-post-restart8000-storage-v2.py) | 4988 | `c0a25ca74795429f6cd68cca0ae473957cc92dc4760c5fbc6170c33ebd4a0841` |
| [numerical-post-restart8000-storage-v2.md](2026-11-10-78718-numerical-post-restart8000-storage-v2.md) | 17380 | `16be12285b5c08f56863a1fb60940bfd6498c97073f49836e87738fa411c1faa` |
| [numerical-post-restart8000-storage-v2-frozen-entry-01.json](2026-11-10-78718-numerical-post-restart8000-storage-v2-frozen-entry-01.json) | 5567 | `11db4a5ee903693308f274dcd891371e85ec5e7fa3fedee767b949b93fe0e725` |

本审已全文阅读两件新源码和完整说明，核对冻结元数据及真实负入口 argv。原始成功计划器 `78718-plan-post-restart8000-v1.py` 保持 SHA
`c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456`。
其完整前序独审见 [audit-post-restart8000-plan-v1.md](2026-11-10-78718-audit-post-restart8000-plan-v1.md)，SHA
`e53db48be38381a3e793fb2e2b016b0c0ba51c3ea8acf9fb0c530fadf736cdfb`。
本次另直接复核原 `Bindings`、`command_plan` 的 prefix 路由和完整 `build`，以核新旧接口，而不重复充分的旧生产源审查。

**通过的是一个纯计划入口及其准确接线。** 在真实 root restart8000 完整成功条件满足后，它可以产生保留原数学和验收门的另名存储条件计划。原单容器计划保持原字节，仍为实际首选；新计划不自动选择或执行存储支路。它不接受独立 seed8000 的 `independent_observation`，不预支任何未来成功 CP，不把存储语义和静态来源通过当作候选几何通过。

截至本次审查，没有成功输入正例，故没有实际构造本候选生产 argv、执行完整后链或支付 G5。下面对变换的通过是完整源码证明加真实静态/拒绝路径，不是伪造一个成功运行来测通流程。

## 2. 前置已审家族与本次新增问题

完整存储家族曾分别审为：

- [audit-storage-family-v1.md](2026-11-10-78718-audit-storage-family-v1.md)，SHA `4912e2cd32bb2df8b8095d1e93e968bbe9417aa357894114caddd22cda230093`：字节语义和 reader 实跑成立，但两份报告中三个旧来源路径遗漏，故当时未采整个 family。
- [audit-storage-family-v2.md](2026-11-10-78718-audit-storage-family-v2.md)，SHA `2fe0c4a0d62c0864a8e318c4ac5e07111c67f024e2d3319565a96bcc4a733b1f`：另名 arithmetic-v2、metric-budget-v2、angular-metric-v2、terminal-v2 修正及完整传播已审通过，其余十二源保持原字节。
- [audit-storage-v2-source-closure-01.json](2026-11-10-78718-audit-storage-v2-source-closure-01.json)，SHA `7215eeda5b88d5895e804f659873762c348b8a3a15c19fbaaffa081c07a8a6dd`：本人实际完整变换及闭包核验。

本次不另造 reader 或替代数学，不重复充分的字节/reader 测试。新增任务是核清：当前纯计划器是否完整消费这套真正通过的四件 v2 加十二件不变源、是否保留原真实成功入口、是否只改准确路径和对应来源身份，以及是否把全部消费者闭合到同一个 defining 图。

## 3. 完整真实成功门在任何命令生成之前

`load_base()` 先按完整 SHA 校验原计划器文件，再导入其定义。新模块没有覆写原函数、常量、actor、成功状态、模块变量或 runtime 身份门。

新 `build(args)` 在独立生产目录名前缀检查后，首先直接执行 `original = base.build(args)`。存储输入核验和任何路径替换都在这次调用成功之后。原 `build` 按原顺序：

1. 检查生产目录位于当前 topic 的 notes 下且完全不存在，计划输出也是 notes 下的新文件，并且不在将来的生产目录内。
2. 调用原 `audited_success`，要求真实 root 观察、固定 restart8000 入口和完整 `final_audit`，将新鲜完整报告与指定保存的完整报告逐字段比较。
3. 成功状态必须为 `PASS_ROOT_OBSERVED_RESTART8000_M14_W14_FINITE_COUPLED_CLOSE`；其自有 CP 和自有最后尾包从完整成功结果实际解析，不从文件名猜测或借先前运行的 CP。
4. 重新核固定原物理背景、源码及相关真实文件，闭合 launch 的全部输入、final 的全部必需输出、reproduction 和 root observation；完整绑定后才调用 `command_plan`。

因此缺 root 实际自然出口、错误 actor/run、旧失败或状态未知运行、缺 final、保存 final 与实际重放不符、缺自有末 DN/PP/outer/BC/运行期来源等，都不能靠选择 storage 分支绕过。原程序完整成功检查没有被拆成较弱的局部检查。

这仍是 root restart8000 的接口。独立 seed8000 使用另一 launch/schema/status、固定 `/root/independent_audit` 和 `independent_observation`；本计划不改写这些字段，也没有接受它的另一路径。若独立运行以后成功，必须另名接自己的后链，不能把其真实观察改写成 root 观察。

## 4. 16 件存储源、原来源及证据链完整绑定

`verify_storage_inputs` 使用原 `Bindings`。每次 `add` 都读取实际文件并核 SHA、必要时核大小；同一路径多角色合并时还比较先前身份，防止在规划期间发生不一致。它依次绑定：

- 不变原计划器。
- ledger-03、v2 完整 diff、两份完整独审、本人 v2 来源重放、root 的真实 v2 reader 报告、原生产计划完整审稿。
- 已审 builder-v3 和 reader-checker-v2 的实际完整 SHA。
- 两件存储 core 及十四个实际新 adapter。

随后读已固定 SHA 的 ledger，要求其 `new_source_names` 的值集合正好为 16 源，变换行数为 14。两个 core 的固定摘要与十四行新源摘要合成的映射必须与 `FAMILY` 全等，不允许重复新名字；每行的十四个原文件和十四个新文件都重新按其 SHA 和大小绑定。故此处没有把旧 v1 的三处报告来源遗漏重新带回计划，也没有把未恢复的旧 A/B 源冒充为新源。

这里不重新执行 builder 或导入 adapter。逻辑等价和全部函数保持已由前序完整独审证明，而当前恰消费同一组字节；这种复用不会把“引用审稿”伪称成新候选数学运行。

## 5. 终门、角度后端和网格的准确来源闭包

本次直接审了 AST 提取代码：`assignment` 只在模块顶层找唯一的指定赋值，缺失或不唯一都拒绝；`literal` 用 `ast.literal_eval`，不会执行候选后端。固定原/新源先经 SHA 绑定，所以不存在把任意新表达式当成原赋值的问题。

新 terminal 的 `PREFIX_SOURCES` 必须恰为全部 16 件家族去掉 terminal 自身、mesh exporter、mesh reviewer 后的 **13 件**。它不是只验证“数量等于 13”，而是整份名字→SHA 映射全等。新 terminal 的 `SOURCES` 与原 terminal 的原 **21 件** tail/reference 映射全等，并逐件重哈希实物。

对 `BOUND`、`FACTOR`、`LOWER`、`REFERENCE`，新旧完整赋值 AST 必须相同；保留了原 $1/500000000$ 门、旧 M12 下界、改善常数和原参照身份，不以普通 whole 的 $10^{-6}$ 通过代替终门。

新 angular 的 `SOURCES` 共有 **11 件**，逐件绑定；其中每个 `78718-` 名字必须在当前 `FAMILY` 中具有完全相同的 SHA。结合固定 angular 文件自身的 SHA，这也保留了原来源映射中的全部旧数学依赖。新 mesh reviewer 的 `EXPORTER_SHA` 必须恰等于新 exporter 的实际 family 摘要。

这正是前序修补的实际传播闭包：arithmetic-v2 与 metric-budget-v2 的真实来源报告，经 angular-v2 和 terminal-v2 使用，而没有保留历史 v1 的旧路径文字。原 tail/reference 来源则完整保留，不随 prefix 表示改名。

## 6. 九类 CLI 路径替换及数学参数保持

声明替换为以下九类，均以完整脚本绝对路径为键：

| 原 CLI | 实际新 CLI | 路由 |
|---|---|---|
| `db6f-root-mirror-hermite.py` | `78718-prefix-mirror-hermite-storage-v1.py` | file-cap 内的 producer 入口及 additional source |
| `db6f-audit-metric-supplier.py` | `78718-prefix-metric-supplier-storage-v1.py` | 同一解析目标 |
| `db6f-audit-metric-polynomial.py` | `78718-prefix-metric-polynomial-storage-v1.py` | 基础图 metric |
| `db6f-root-common-cut-v2.py` | `78718-prefix-common-cut-storage-v1.py` | make、geometry、metric、moment |
| `db6f-audit-prefix-angular-metric.py` | `78718-prefix-angular-metric-storage-v2.py` | 完整选中角弧认证 |
| `db6f-audit-closed-budget-transfer-v3.py` | `78718-prefix-closed-budget-storage-v1.py` | 同一图闭预算 |
| `db6f-audit-terminal-error-gate.py` | `78718-prefix-terminal-error-storage-v2.py` | 正常完整终门 |
| `db6f-export-closed-mesh.py` | `78718-prefix-export-closed-mesh-storage-v1.py` | mesh plan/build |
| `db6f-tail-review-closed-mesh.py` | `78718-prefix-review-closed-mesh-storage-v1.py` | 实际独立 mesh manifest 比较模板 |

`static_command_names` 从固定原 `command_plan` 的 `add` 和 `script` 调用中读取字面脚本名。原函数已完整审过，这种 AST 抽取对其全部字面来源覆盖为 22 件；九个旧名必须全部包含在内。这个过程不调用 `command_plan`，不填任何候选 CP，也不生成生产 argv。

真正的替换函数收到的是原完整成功 `build` 返回的计划。它先 `deepcopy`，然后对 `commands` 的 `argv` 和 `manifest_or_independent_input_templates` 的 `argv_template` 按严格对应顺序处理。只有某 token 为字符串、且整个字符串等于已固定的旧脚本路径时才替换；不对一般参数、子串、注释或未解析模板作文本替换。

每个被替换来源的 `source` 身份，及 prefix wrapper 的 `additional_sources` 身份，都须与当前旧实物完全相同后才换成实际新实物。该步骤保存准确的 argv 索引、旧路径和新路径。九个旧路径各自的使用计数必须正数，未来 argv/模板中不得再残留这九个旧路径。

## 7. 逆替换比较的完整保持性证明

逐记录处理后，代码再复制新的记录为 `restored`：

- 只撤销账本记录的 argv 索引，并先确认该位置确为对应新路径。
- 只撤销实际换过的主 source 和 additional source，且先逐字段确认其是相应新身份。
- 对唯一特别记录 `prefix-base`，撤销其 `completion_requirement` 的文字变化。

然后 `base.same(restored, before)` 比较整份记录。这要求所有其它字段完全相同，包括每个数值/布尔/字符串参数、argv 顺序、输出名、条件、依赖、cwd、执行状态、未解析 manifest 选择器和 completion 说明。

因此该变换保持了原 tail 的 depth8/steps32/flow32/N512/degree192，以及 mirror 的 M24/N768/quadrature8/subdivide1/ell0、common-cut width .15、原全域认证参数、原四种 baseline/angular 与 full/metric-only 条件路线、same-plan 网格参数和原独立全链义务。任何未声明的数值变化都会使还原比较失败。

唯一新增的单步完成文字明确 demanding base M24、实际 `data_storage` descriptor、所有内容寻址分片及其完整哈希/长度要求；原 `78718-run-file-cap.py` 仍是外层主 source，原 `RLIMIT_FSIZE=4,999,999` 入口和全部参数保持。这段文字是已审资源表示应有的实物闭存要求，不改曲面或原数学通过标准。

## 8. 共同 defining 图及保留消费者

前序存储审查证明 codec 保存的是原 producer 序列化后 gzip/NPZ 字节串 $P$：`data_sha256` 为完整 $P$ 的 SHA，各连续 raw part 长度不超过 4,600,000 B，再按规定 gzip；reader 完整核 descriptor、每片身份/长度/顺序、连续覆盖和最终 $P$ 的摘要，再解释相同字节。正负零、NaN payload、dtype、shape、order 的保持来自字节同一性，不是数值近似。

本计划使用的是上述同一 family：mirror 指向新 fullxyz producer，reader/common-cut/metric/moment/closed-budget/terminal/mesh 均接当前 family。defining base 的 M24 与 common-cut expanded metadata 的 M64 没有混同。terminal 读取真实 base/descriptor/parts/helper/codec 的身份闭包，不能把一个物理分片的摘要冒充完整 $P$ 的摘要。

九类以外的原 CLI 保持：tail endpoint、radial、collar、first bounds、背景 transfer-v3、full-tail、metric-only、complete-metric-report、exact bridge、whole-metric-reach-v2、背景高度采样和 PLY/PL 检查。这不是漏接：前序完整来源/消费者审查已核 whole/bridge 的 JSON 证明消费、height sampler 的 tail/radii/background 输入和 PL 的 PLY 输入。新 supplier 的目标 NPZ、tail 背景 NPZ、mesh fixed mask 属于各自原格式，并非 prefix descriptor 消费者。

此次新计划不改变所有这些前置已审源字节。它也没有把 arithmetic-v2 的独立 tail CLI 插入生产路由。原 M12 reference 文件、原21件 tail/reference 源及其真实下界仍保持原身份。

## 9. 顶层来源记录和分支边界

替换完成后，新 `Bindings` 对原计划全部 preexisting rows 逐角色重新核实，再合并存储绑定，最后绑定自身源码。只有原计划的 `this-plan-source` 角色被改称 ancestor；原源身份保留，不被新计划身份覆盖。每个最终主 source/additional source 必须属于实际已绑定路径集合。

顶层仅追加/更新另名 schema、status、本计划源、完整 family 验证、路径替换账本及资源分支说明。原 full final、root observation、自有成功 CP、自有末尾、固定背景、原图常数和未来义务仍由原结果保留。再次要求精确 terminal bound 不变、`branch_selection_performed=false`、solver/production 调用数均为 0。

`storage_branch_selected_or_activated=false` 的含义正确：这个程序只构造一个条件支路的计划，不判断单容器是否真的超限，也不执行选择。选择应基于实际观察的单容器资源需要；单纯运行纯计划器不等于已选择这条支路。新生产目录必须另名且不存在，不覆盖先前单容器失败输出。

对 mesh 文件仍保留原真实 manifest 解析模板；不能提前猜 .ply/.ply.gz、未来 SHA 或独立 manifest。same-plan mesh 比较也不能代替未参与者从原种子真实 solver→tail→prefix→certificate→mesh 的完整复跑。

## 10. 纯 checker 的实质与边界

checker 先要求精确冻结的主解释器路径，核新 planner 完整 SHA，compile 并导入其定义；调用原 `verify_fixed_inputs` 和新 `verify_storage_inputs`，合并并重新绑定全部来源。对原 22 个命令脚本逐件要求属于绑定集合，并检查没有导入 NumPy/SciPy。

其报告区分了 `plan_ready=false`、`successful_main_claimed=false`、`complete_final_audit_replayed=false`、`candidate_argv_constructed=false`、`production_commands_emitted=0` 和资源分支未激活。报告的存在不是成功 final，也不是未来图的 descriptor。

本次静态检查没有调用 `base.build`、`command_plan`、`replace_command_records` 或任何数学后端；路径变换正确性由上面的完整源码证明支付。没有真正成功 CP 前，故意不合成正向输入来执行完整 build。

## 11. 审者亲手执行的记录

首次使用环境变量中的解释器路径调用 checker，真实工具 `782d38` 自然 exit 1，明确报 `Use the absolute frozen primary Python`。它在任何输入检查/报告写入前拒绝；这次不能记成通过。随后按冻结说明使用完整绝对路径执行，源代码未改。

### 11.1 真实静态正例

```text
/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python \
  scripts/78718-check-post-restart8000-storage-v2.py \
  --out notes/2026-11-10-78718-audit-post-restart8000-storage-v2-static-01.json
```

真实工具 `6d1077`，自然 exit 0。报告为 [audit-post-restart8000-storage-v2-static-01.json](2026-11-10-78718-audit-post-restart8000-storage-v2-static-01.json)，66,508 B，SHA
`446894565beab95320c320c15fac0f8c304aa1ac36a4e3e5f7043abb04799052`。

实际得到 127 件原固定绑定、56 件存储绑定，合并含新入口/checker 的 159 件唯一实物；16 源、9 类替换、13+21+11 来源 pins 全通过。0 adapter import、0 NumPy/SciPy、0 solver、0 producer、0 候选 argv。报告与作者 `d9dfc8` 的确定性报告逐字段相同；摘要相同来自内容确定性，不把两次执行混为一次。

### 11.2 真实缺出口负例

以真实 restart8000-02 launch、明确不存在的 observation/final、全新未创建的 `post-restart8000-storage-v2-audit-negative-missing-01` 目录调用新 planner。真实工具 `73cfd5`，自然 exit 2，拒绝缺失真实观察。

报告 [audit-post-restart8000-storage-v2-missing-exit-01.json](2026-11-10-78718-audit-post-restart8000-storage-v2-missing-exit-01.json)，315 B，SHA
`f18bcad1471b6214677c2a98094e5ba9bc6641f9642d4ceffa87f476f03bb5d9`。
没有生成 argv、没有创建生产目录、没有调用 producer。

### 11.3 真实借旧运行观察负例

以同一真实 restart8000-02 launch，传入原 direct-csc-02 的真实失败 root observation，未伪造任何字段；使用另一全新未创建的 `post-restart8000-storage-v2-audit-negative-wrong-run-01` 目录。真实工具 `e87bcd`，自然 exit 2，拒绝 `Wrong actual root observation identity`。

报告 [audit-post-restart8000-storage-v2-wrong-run-01.json](2026-11-10-78718-audit-post-restart8000-storage-v2-wrong-run-01.json)，318 B，SHA
`a5ff186e3556b1eb3fa5639714d3c82538bdda454986cc40efeb283513da70ec`。
同样 0 argv/producer，说明新包装没有绕过原实际 root 身份门。

工具 `df7740` 后续仅重新核四件冻结交付的大小/SHA、两份静态报告全等、三份本人报告存在和两个未来生产目录不存在，自然 exit 0。没有扩展为数学重算或重复充分的 reader 检查。

## 12. 尚待实际候选完成的事项

静态检查仍给 `terminal_reference_ready=false`：原终门缺 26 件固定 M12 参照对象，另有一份必须由真实 packet 头部才能确定的 data 后代。这里保留的是 expected 身份和真实缺失状态，没有把 expected SHA 记为实际已验证。它们应在实际终门消费前按原清单取齐；新计划没有用存储支路删除这项需求。

真正发生 root 完整成功以后，仍须实际运行所选择的原单容器或新资源分支，保存每步真实自然出口和全部自有闭存输出，并完整通过 prefix/tail/closed-budget/whole/正常严格 terminal/mesh/PL。所有文件大小约束保持；新 codec 只解决 prefix 容器，不能推断未来其它大输出自动满足上限。

本审没有消费 root solver 的工具 session，没有观察或宣称其当前状态，没有修改冻结主入口/源、选择 M14 预算或启动独立 seed8000。旧未知会话仍不能由本检查判定成功、失败或活跃。完整未来独立复跑资格和任务保持。

**最终意见：这两件新源及其声明的条件接线通过，无实质修正项；可以作为已审的纯计划入口保留。尚无新成功图、实际存储生产或最终数学完成声明。**
