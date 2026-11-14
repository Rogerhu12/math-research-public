# 独立 seed8000 成功后的两个另名后链计划

日期：2026-11-10；作者 `/root/numerical_recovery`；会话 Astra-visible-flex-78718bd0。

本稿冻结 **独立 actor 的原单容器后链基底** 和 **同一 actor 的条件存储 v2 包装**。
它们各自使用实际独立主运行的完整成功谓词，不通过修改 root-only 模块的 globals 来
冒认身份。所有原数学参数、真实 CP/自有末尾绑定、完整 final 新鲜重放和原 2e−9 终门
保持。当前只实际执行源派生、静态输入核查与必要负门，没有启动任何 BVP/producer，
没有造成功 CP，也没有输出一个假正向计划。

独立主入口已由未参与优化者全文核审，见
[independent-seed8000 完整审稿](2026-11-10-78718-audit-independent-seed8000-entry-v1.md)，
20,752 B / SHA `4bf8d07536b0df21f824bf06ba753af3905d6db252744b46b58fadf0aeeff9e3`。
本稿冻结时，独立主运行尚未实际启动；启动与重 BVP 的资源顺序由 root 调度。
这里的新两个后链计划仍待完整独审，不能把主入口通过当成它们已经通过。

## 1. 四件新源、两份完整来源文件

| 文件 | B | SHA256 |
| --- | ---: | --- |
| `scripts/78718-build-independent-post-plans-v1.py` | 11273 | `e62c201b15355687f9645690b4e3d57e0341348cafd853e2d38d8bfb7b60f461` |
| `scripts/78718-plan-post-independent-seed8000-v1.py` | 32715 | `b3526176d56179a3edce6a71a159591a1e9f5ceecd9d253a4eeec95887e07053` |
| `scripts/78718-plan-post-independent-seed8000-storage-v2.py` | 20428 | `c94d7b8204ad8184a181fc6d8b4b9b495f3dd0d9fdf3609f6ea23168ed4fc223` |
| `scripts/78718-check-independent-post-plans-v1.py` | 9298 | `184664829bec0f529eb8f48c997bedf15ba30497ad6659d3d142ec3775924281` |
| `notes/2026-11-10-78718-numerical-independent-post-plans-derivation-01.json` | 11863 | `c85e5953bfb4298c765c59e4e03fa9a1a13b938e4cebaa2b56957fc10dbf13ac` |
| `notes/2026-11-10-78718-numerical-independent-post-plans-source-diff-01.txt` | 10465 | `38537c125310eadc6f15862d780034e3edc8ea27c515859732fe4d883d05b8c4` |

原来源保持实际字节：

- `78718-plan-post-restart8000-v1.py`，32,491 B / SHA
  `c6ef233eb40517bf1986b3ea25d0bb31d102d4b219727c6d69a97b38ee1e0456`。
- `78718-plan-post-restart8000-storage-v2.py`，20,326 B / SHA
  `99c053a1563a31c94de2b2d9b99db70aad603c2bafa89f023abc69800748badc`。

原单容器计划的全文独审为
[原 plan-v1 审稿](2026-11-10-78718-audit-post-restart8000-plan-v1.md)，SHA
`e53db48be38381a3e793fb2e2b016b0c0ba51c3ea8acf9fb0c530fadf736cdfb`。
root 条件存储计划后来亦已全文独审通过，见
[root storage-v2 审稿](2026-11-10-78718-audit-post-restart8000-storage-v2.md)，
19,888 B / SHA `d0b677402a799510f980467564562f17ef24a305e853d1b0e4f8a01c21dd7ecd`。
这些审稿分别属于各自冻结身份；本稿没有把它们移成新独立计划的实际执行记录。

## 2. 为什么完整成功谓词确实属于独立执行者

独立原单容器基底从原 plan-v1 做17项唯一文本替换，不 import 原 root-only 模块后篡改
其常量。新文件自己的全局值明确为：

| 绑定 | 独立值 |
| --- | --- |
| 完整 auditor | `78718-prefix-audit-independent-seed8000-v1.py` |
| auditor SHA | `067f8944cb0d75ceffc846119b1ca2511f0e6e886799258e4659b023d8828578` |
| launch schema | `78718-true-m14-w14-independent-seed8000-launch-v1` |
| 完整成功状态 | `PASS_INDEPENDENT_OBSERVED_SEED8000_M14_W14_FINITE_COUPLED_CLOSE` |
| final 报告观察字段 | `independent_observation` |
| 计划观察字段 | `independent_actual_exit_observation` |
| 原单容器未来目录前缀 | `2026-11-10-78718-independent-post-seed8000-` |

新 `audited_success` 仍先钉完整 auditor 字节，再调用其 `c.validate_inputs(launch)` 和
原 `final_audit(context, observed)`，要求新鲜完整结果与指定已保存 final 报告逐字段相等。
它没有换成状态摘要，也不跳过 main input 的165件来源、完整原物理检查、十函数 typed
runtime、14物理 callback、PP、outer、BC、自有最后真实 DN 与关闭输出。

真正 actor 门由该已审独立 auditor 的 `final_audit` 固定要求：

1. observation 的 `observer` 必须严格为 `/root/independent_audit`，stem/status/actual exit
   都对应这一次独立主运行；exit 必须为真实自然0。
2. recorder_source 必须为固定独立记录器实物；tool_return_metadata 必须有真实整数
   exit_code、匹配的 chunk receipt，且不再带活动 session。
3. 对观察记录绑定的每件实际文件重哈希，核完整 required closed files、launch/reproduction。
   不从 guard 的 child exit 推断自然出口，不能以 root 的真实观察代替独立者的真实观察。

记录器本身不提供密码学身份认证；调用者必须是约定执行者，并向它传入该执行者真正
收到的 tool return。完整独跑协议要求独占持续工具轮询、真实回执立即保存；此新计划
没有调用记录器，也没有人为制造可接受的正例。

完整 final 通过后，CP 与末包的选择接口保持：从报告真实 `prefix_CP` 读取 CP，解析其
`tail_seam.tail_record`，要求它是此 stem、此 `tail_calls` 的自有最后响应，并在完整 final
关闭文件集合中逐字绑定。物理 linear port SHA、background g、primary Python/Node 和
实际 source-root 都保持。不能借 root 最后尾包、失败 CP 或另一次成功图证书。

## 3. 原数学后链与存储包装的完整不变部分

builder 要求原完整文本 SHA，逐项旧字符串恰好出现一次，得到新源码后 compile。
它实际比较完整顶层函数 AST 集合：

- 独立原单容器基底有12个完整函数 AST 与原版相同；仅 `audited_success`、`build` 因
  上表身份/字段/目录/说明字符串不同。特别 `verify_fixed_inputs` 与 `command_plan` 完整
  AST 全同，全部 backend 参数、branch 条件、own图路径、依赖和 mesh 解析模板未变。
- 独立存储包装从 root storage-v2 做11项唯一替换；其8个完整函数 AST 保持，仅
  `load_base`、`build` 的身份字符串不同。`verify_storage_inputs`、`replace_command_records`、
  `static_command_names` 完整 AST 全同。

两份新源码的实际全 diff 是10,465 B，已由作者完整读取（工具 `d0d7f0`）；原→新完整
文字替换账本为11,863 B。静态 checker 又独立按账本重建两文件的每个字节，并重造完整
diff 核全等。AST数量是关系检查，不冒称替代完整来源文本和原算法审查。

新独立存储包装自己的 `BASE_NAME/BASE_SHA` 指向上表独立基底 `b3526176…`，并直接调用
其 `build(args)`；不会反过来调用 root-only 成功门。它仍先由完整独立成功门取得真实
候选，随后才在内存计划副本里换九个已审 prefix CLI 家族及其 source 记录。

存储 family、16个 SHA、九项 CLI 映射、13个 terminal prefix pins、21个原 tail/reference
pins、11个 angular pins、原 BOUND/FACTOR/LOWER/REFERENCE AST 及 exporter/reviewer 绑定，
都与 root 的已审 storage-v2 完整相同。具体路由与原参数逐项见
[storage-v2 设计](2026-11-10-78718-numerical-post-restart8000-storage-v2.md) §§2–4。

因此下列原约束没有变化：原单容器优先；只在真实文件大小需要下选择另名存储支路；
不会自动切换；logical gzip/NPZ 字节保持；每片原始字节≤4,600,000、每物理文件<5 MB；
所有 tail/reference/whole/PL 使用原来源；全部节点/模式/求积/分割参数相同；普通whole
1e−6不付终门；完整normal terminal仍以精确1/500000000与真实旧M12误差下界验收；
所有本图几何/误差/reach/网格门及README全时要求保持。

## 4. 真实执行与当前不能声称的事情

| 实际工具回执 | 自然退出 | 实际动作与结果 |
| --- | ---: | --- |
| `a9dd12` | 0 | 纯 builder；17+11项唯一文本替换；产出两新源码与完整账本/diff，0 planner import/solver/producer |
| `6e137f` | 0 | 冻结 checker；两源完整字节/AST/diff重放；127原固定输入、56存储输入合并166个实物绑定；0 NumPy/SciPy、0候选argv |
| `2b9509` | 2 | 独立原单容器基底：真实已准备 independent launch +明确不存在的观察；拒绝 FileNotFoundError，0生产argv |
| `d81ffa` | 2 | 同一基底借 root run02 的真实失败观察；拒绝 Wrong actual independent observation identity，0生产argv |
| `774331` | 2 | 独立存储包装：同一独立 launch +明确不存在的观察；拒绝 FileNotFoundError，0生产argv |
| `2084f5` | 2 | 独立存储包装借 root run02 真实失败观察；拒绝 Wrong actual independent observation identity，0生产argv |
| `1e1572` | 0 | 再核四新源、两个完整审稿的真实大小/SHA及函数差异摘要；0数学调用 |

报告文件共同位于 notes 下、带 `2026-11-10-78718-numerical-independent-post-plans-` 前缀：

| 后缀 | B | SHA256 |
| --- | ---: | --- |
| `static-01.json` | 66465 | `58e9a1297373ed5c17901d417a55db62ca5a6eb8a6a83585ef10b83566b2d8bf` |
| `negative-original-missing-01.json` | 266 | `542903ae4255fad4a58f569ada19c3aad299cc750a2a702084a079825fd805c0` |
| `negative-original-root-01.json` | 276 | `c20692bf731dafc4035d1bcec9bb05a90a46676cdd33088e5c4e3a219a0eba59` |
| `negative-storage-missing-01.json` | 315 | `f18bcad1471b6214677c2a98094e5ba9bc6641f9642d4ceffa87f476f03bb5d9` |
| `negative-storage-root-01.json` | 325 | `23115909291e6d4688eb5deb5829edb0f896960beb1b30e92eb5d4c636c6be88` |

缺文件的通用拒绝 JSON 与较早另一身份的拒绝报告可能逐字相同；本次有上表自己的真实
执行回执和冻结清单中的实际 argv，不把旧回执迁到新运行。四份报告都是本次新输出。
没有成功 CP 的情况下未制造成功样例或替代审计结果。当前静态报告的 plan_ready、
complete_final_audit_replayed、candidate_argv_constructed 都是 false。

原终门的26件M12参照对象及由待取point packet头部确定的data后代仍未就绪。
静态检查明确 terminal_reference_ready=false，不把expected SHA当成实测SHA。
原固定背景、M8已审基底、43份source-root等已准备输入仍按原身份实核。

## 5. 纯复核命令

以下只检查源码与静态输入，不构造候选argv；输出使用新的名字，不能覆盖原报告。

```sh
VF_REPO=/workspace/scratch/78718bd0c4a9/math-research
VF_T="$VF_REPO/topics/visible-flexible-closed-surface"
VF_S="$VF_T/scripts"
VF_N="$VF_T/notes"
VF_PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
cd "$VF_REPO"
"$VF_PY" "$VF_S/78718-check-independent-post-plans-v1.py" \
  --out "$VF_N/2026-11-10-78718-audit-independent-post-plans-static-01.json"
```

如独审需要实际重放 builder，可传新的 ledger/diff 文件名；两个源码目标若已存在只允许
相同字节，不会覆盖不同源。builder 不 import planner 或数学 backend，实际源码重放与
原数据重算是不同动作。四项负门的精确实际 argv 都在本次冻结清单中，重放时仅更换
新报告路径和未创建的未来目录。

## 6. 实际独立成功之后的具体入口

本节仅为未来约定。所有 observed-exit/final/plan 文件必须来自后来真实执行；本稿不
声称它们现在存在。独立执行者的主求解采用已经另行冻结的 published-M14 seed8000
路线，不强制额外重复6500失败，也不从root最终CP起步。两个后链入口保持这种身份，
并没有把它改称逐字重放 root failed-CP restart算法。

```sh
VF_REPO=/workspace/scratch/78718bd0c4a9/math-research
VF_T="$VF_REPO/topics/visible-flexible-closed-surface"
VF_S="$VF_T/scripts"
VF_N="$VF_T/notes"
VF_PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
VF_IND_STEM=2026-11-10-78718-independent-m14-seed8000-01
VF_IND_LAUNCH="$VF_N/$VF_IND_STEM-launch.json"
VF_IND_OBS="$VF_N/$VF_IND_STEM-independent-observed-exit.json"
VF_IND_FINAL="$VF_N/$VF_IND_STEM-final-audit-01.json"
VF_IND_PLAN="$VF_N/2026-11-10-78718-independent-post-seed8000-original-plan-01.json"
VF_IND_RUN="$VF_N/2026-11-10-78718-independent-post-seed8000-original-run-01"
cd "$VF_REPO"

# 仅在固定独立执行者真的收到自然exit0、记录真实tool return后；不覆盖既有final。
"$VF_PY" "$VF_S/78718-prefix-audit-independent-seed8000-v1.py" \
  --launch "$VF_IND_LAUNCH" --mode final --observed-execution "$VF_IND_OBS" --out "$VF_IND_FINAL"

# 原单容器为实际首选；此调用只是完整成功后的纯计划。
"$VF_PY" "$VF_S/78718-plan-post-independent-seed8000-v1.py" \
  --launch "$VF_IND_LAUNCH" --observed-execution "$VF_IND_OBS" --final-audit "$VF_IND_FINAL" \
  --run-directory "$VF_IND_RUN" --out "$VF_IND_PLAN"
```

基底计划的状态应为 `ACTUAL_INDEPENDENT_MAIN_SUCCESS_BOUND_FUTURE_PRODUCTION_PLAN_ONLY`。
每个source、CP、末尾、实际输出都属于该独立图，目录必须尚不存在。计划的
own_successful_checkpoint/own_final_audited_tail 给出真实输入身份；执行后必须取得自己的
export/target/bridge/common-cut/prefix/tail/whole/terminal/mesh证明链。

如果实际单容器出现大小需要，保留其真实失败，另用未使用的存储目录：

```sh
VF_IND_STORAGE_PLAN="$VF_N/2026-11-10-78718-independent-post-seed8000-storage-v2-plan-01.json"
VF_IND_STORAGE_RUN="$VF_N/2026-11-10-78718-independent-post-seed8000-storage-v2-run-01"
"$VF_PY" "$VF_S/78718-plan-post-independent-seed8000-storage-v2.py" \
  --launch "$VF_IND_LAUNCH" --observed-execution "$VF_IND_OBS" --final-audit "$VF_IND_FINAL" \
  --run-directory "$VF_IND_STORAGE_RUN" --out "$VF_IND_STORAGE_PLAN"
```

存储状态应为 `ACTUAL_INDEPENDENT_MAIN_SUCCESS_BOUND_CONDITIONAL_STORAGE_PLAN_ONLY`。
plan_ready只表示成功输入绑定与未来命令完备，storage_branch_selected_or_activated仍false；
调用者按真实资源条件选择后，才创建该新目录并实际运行依赖链。原来 root-only 两入口
及其 frozen bindings均不修改、不作为独立观察别名。

两种未来计划每一步都要求真实argv/cwd/environment/自然出口/源码与输入SHA/全部自有
输出闭存。若独立算得的有限图与root图字节不同，其证书与网格不能交叉借用；应完成
自己的完整链并准确报告差别，再以真正满足README的同一图做最终判断。普通same-plan
mesh比较不代替独立原seed求解，全链实际成功也不自动补上严格无限尾存在性差距。

本次工作没有消费root的session 72917，没有改变任何主solver源、参数、预算或种子，
没有新建生产目录。原门、当前失败/未知运行记录和进一步几何目标都保持。
