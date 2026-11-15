# Request 85：从真实82候选以同η=0.1续一次原八步预算

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：独立工作流与来源接线草稿；仅源文本/原字节静态操作。** 没有修改任何科学源码，没有在本地导入数学模块或进行数值调用，也没有修改仓库、提交、派发或预填未来 run 身份。主控负责唯一发布与 Actions 执行。

## 1. 本次选择的实际依据

[actual82正式结论](2026-11-15-actual-request82-damped-resume-eight-full-steps.md) 已完整读回：原 η=0.1 的八次方向均在首个 α=1 通过，没有拒绝、域失败或回溯截断。实际总 merit 为 `15492237698.871288 → 11949245423.478903`，最终单位缺陷仍为 `[224.4830723005632,-154577.5000610159,2058.380235692375]`。各分量并非同时改善，原候选小残差标志仍 false。

因此85只从真实82最终参数重新线性化，继续一次**同η=0.1、最多八个方向、每方向原20档试步**。当前原记录没有要求扩大回溯或改变η，下一次也没有下降或共振保证。没有把这些候选当作非零幅度 parent。

## 2. 唯一父件与冻结源码

真实父运行 `43665944742` / source `f1a2c80826d106d1c92db7aeffd1dbfcd84625c6` / job `132665204485`。其 artifact 为 `14141564704`，267442 B，ZIP SHA `fa07a132734ca9cc604cbccc74926c8840683fd6c0eff4d2c7b510ab898c2214`。

只消费以下完整原状态文件的 `final.parameters`：

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43665944742-1-smallcoreresonance/small-core-damped-resume/damped-resume-status.json
54263 B
SHA256 1e56d89cf97e6e26904c7092e974a516905c52dd0dd47d10bd40dd4e3c3384fd
```

新初值逐 binary64 位绑定：

```json
[0.07254576672993071, -0.0403277008444164, -0.11497411877394303]
```

本轮没有新的科学入口。仍调用：

- `geometry_20261115_small_core_damped_resume.py`，15452 B / `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a`。
- 其原方向引擎 `geometry_20261115_small_core_damped_search.py`，13733 B / `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728`。
- 原模型/检查 `geometry_20261114_small_core_resonance.py`，25799 B / `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`。

入口原本就接受自身 schema `R259-original-three-equation-column-scaled-LM-resume-v1`：父必须是已完成诊断，`success=false`、native false、nonzero false；它核完整11消费源集合、父入口 ec9、方向1691、四原输入和完整父字节。此次没有猴补这个检查或把 actual80 的旧 schema 改名。

70个实际82 source pin、四原数学输入、runtime、public78恢复过程全部逐值保留。publisher仍是 `root_20261114_publish_actions.py` / `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`。

## 3. 精确CLI与输出

工作流还是原单一 `smallcoreresonance` job，原 scientific step 中 `subprocess.call(argv)` 只有一次。数学CLI完全沿用原82，仅 parent 文件、SHA与其实际参数身份变成82：

```text
python -u geometry_20261115_small_core_damped_resume.py
  --accepted <原accepted96 b4d2b98a…>
  --prepared <原prepared112 0f94dd88…>
  --tail-anchor <原真T112零锚 e788a28d…>
  --tail-config <原T112配置 01930f3b…>
  --parent-status <上述actual82完整状态文件>
  --parent-status-sha256 1e56d89cf97e6e26904c7092e974a516905c52dd0dd47d10bd40dd4e3c3384fd
  --damping 0.1
  --candidate-steps 8
  --backtracks 20
  --candidate-resonance-tolerance 1e-08
  --interval-bits 160
  --interval-depth 14
  --out "$VISIBLE_OUT/small-core-damped-resume"
```

完整无缩写CLI在 `2026-11-15-request85-source-static-check.json.actual_command_shape`，完整四输入路径/长度/SHA在request。示例中的省略号仅用于接口阅读，不被传入实际命令。

原未加权三方程、6×3正阻尼方向、真实方向斜率、原0.2 Armijo系数、20档 `1…2^-19`、每次原模型/域求值、原完整112右残差、参数FD、160位/14深度Arb和完整699节点zero-core circle均不变。原tol `1e-8` 也不变。η仅是候选算法参数，未加入原非线性residual；三设计参数的搜索仍不冒同一固定g精化。

输出目录仍为 `small-core-damped-resume/`，状态仍为 `damped-resume-status.json`，schema不变。输出包含原 parent副本、初末诊断、全部方向/trial、完整 scalar域及circle。job前的额外只读来源副本改名为 `prior-candidate/actual82-damped-resume-status.json`，来源账改名 `request85-input-and-source-identity.json`。旧readback步骤、全部失败保全、上传artifact和原publisher正文逐字不变。

## 4. 最小文件差异和唯一触发

拟放入仓库的两件仅是：

| 草稿basename | 唯一既有仓库目标 | 字节 / SHA256 |
|---|---|---|
| `visible-larger-public-small-core-resonance.yml` | `.github/workflows/visible-larger-public-small-core-resonance.yml` | 15230 / `d5c4481b2ff1a36167834d7f91fccb6ae70bc860f156a7968e6d4bb634432664` |
| `public-small-core-resonance-request.json` | `topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json` | 18263 / `0add5cb89b786fc3d83a05f49ef5e2f15dfdb5887bc760262d09852e4a901247` |

**保留原computations request路径触发；没有另建第二工作流、第二request或附加dispatch。** job concurrency、预算60分钟、scientific step45分钟、权限、运行时、BLAS单线程、action pins、public源恢复与publication均保留。

相对已实际执行82的完整diff已提供：

- `2026-11-15-request85-workflow.diff`：标签/request号、82父路径/长度/SHA/参数、来源副本名、`scientific_source_unchanged=true`的准确接线。科学调用run正文不变。
- `2026-11-15-request85-request.diff`：真实82父tuple、参数、85号、时间与动因；source/runtime/inputs/sourcechain/proofs均不变。

`new_resume_producer_is_explicitly_distinct=false`准确表达本次是同源自身续接；它与当初82新增resume入口的历史元数据不同。新request保留完整父tuple，不用同源作为省略父身份的理由。

## 5. 已完成的静态核对

`2026-11-15-request85-source-static-check.json` 为33036 B / `461c9e82f93685839459d204e71b9a3f52cf0ccc94c67863f7d9a54350a76704`。105项源/布局检查全部通过，范围仅：

- 原82request实际SHA与baseline一致；新parent54263B完整SHA、原参数bits、schema及11消费源全对应。
- 全70源原文件逐SHA核对，Python只作AST解析；没有数学import或执行。
- 7个shell段仅 `bash -n`，4个inline Python段仅AST；实际scienceCLI原正文不变。
- workflow中硬写的三来源chain、参数dict和父tuple经AST literal解析与request逐值相同。
- 同一个原push trigger、job、runtime/source恢复/readback/upload/publisher与原预算保持。

这是可发布的具体后继草稿，不是新的科学门或一次已运行结果。尚无85 run/artifact、下降、共振或非零解可宣称。主控可按正常Git同步流程唯一发布；实际85完成后仍依据原试步和最终记录决定下一步。

## 主控发布接线

主控完整读取以上两份diff和接口，独立核全部70源字节/AST、7段shell及4段inline Python，原科学调用正文保持逐字相同。完整父status的参数逐binary64字节绑定；仅参数与来源改变。新增独立回执见[主控静态核对](2026-11-15-request85-root-static-check.json)。本发布版仅把草稿回执/差异链接改成唯一仓库文件名；原接口7119B/05745119c71442ecde12999d2bf4a7b32c7eef3ae0dba5be34fe2aa2bd31ce24的其余正文保持。
