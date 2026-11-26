# 强分支的同 job 末态消费与并发发布修复

**可信度：程序实现及实际基础设施验证；不是新数学接受步或完成证书。**

本记录补的是已发生的实际断点：Actions `45767322734` 在第 20 个数学接受步后因 main 的 ref compare-and-swap 竞争而发布失败。该 run 没有产生第 21—60 步。其第 20 步已有的报告提交、真实标量及可见哈希另见 `2026-11-26-6a65-solver-actions-twentieth-cas-failure.md`；这里不以重生补造原输出身份。

新入口为 `scripts/6a65-actions-strong-branch-20261126.py`，配套 workflow 为 `.github/workflows/visible-flex-6a65-strong-20261126.yml`，具体请求为 `ci-requests/6a65-strong-branch-20261126.json`。它们与原 controller 分名，冻结各自触发提交的 source；本记录不声称新 workflow 已执行。请求按根会话最新实际本地结果设置：R219/N128/84点先恢复已见3步，实际152915点观察后立即消费R208两峰插结，继续20个新空间接受步，其中前3步为已见配方恢复。合计原17步恢复、这两个阶段6步恢复和17个新接受尝试；阶段末态原件留在同一个runner等待真实后继。

## 1. 已见输入的恢复链

一个 runner 内按下列次序恢复实际后继输入。每个 LM 调用均在独立 Node 进程中完成一次完整 normal 和实际试步，父 Python 进程等待真实退出；所有已见接受步均标成重生，不计新研究结果。

| 阶段 | 实际入口 | 本阶段重生接受数 | 后继接口 |
|---|---|---:|---|
| R211 原 metric | `6a65-run-metric-branch-recovered-20261126.cjs`，参数 `original 1 run` | 2 | original checkpoint |
| 四次 metric，τ=.05 | 同入口，参数 `.05 1 run` | 6 | quartic checkpoint |
| gap=1，Δ=.05，R215 | `6a65-geometry-gap-length-value.cjs` | 0 | 新完整 baseline/seed |
| gap 分支 | `6a65-geometry-run-gap-length.cjs` | 3 | gap checkpoint |
| 原 42 固定峰点 | `6a65-geometry-run-fixed-peak.cjs` | 3 | fixed-peak checkpoint |
| K7→11，N64 保留 | `6a65-gap-fixed-peak-angular-injection.cjs` | 0 | 同场零注入及其完整 baseline |
| K11 原 42 点 | `6a65-geometry-run-fixed-peak.cjs` | 3 | 实际 K11 checkpoint |

以上共 17 个已见接受步。阶段转换、纯 value 和零注入均不算接受步。原输入、各阶段源码以及输出的 SHA-256 都从本次真实字节计算；新运行不能继承旧检查点的 SHA-256。旧失败的纯 quartic 第 20 态不是这条强分支配方的输入。

K11 重生结束后，立即调用根会话的 `6a65-gap-refined-metric-observer.cjs`。它显式使用保存的 gap/clock factory，并逐系数检查 `Object.is`，保留当前 angular primitive。控制器核验候选与输入的实际文件哈希、观测 schema 和三个同场标记。这里没有再实现一套 observer。

## 2. 新阶段必须明确建立自己的 baseline

控制器要求请求显式列出至少一个 continuation，不允许默认为原 42 点再运行长段。每个 continuation 指定 `init_script`、`run_script`、argv、initial/checkpoint schema、输出后缀、accepted counter 和实际步数；若其中某些步先前已观察，另给 `prior_observed_steps`。

R219 接口已经按实际源码读取：

```text
node --expose-gc 6a65-run-low-wide-expanded-peaks.cjs candidate input prefix init
node --expose-gc 6a65-run-low-wide-expanded-peaks.cjs candidate input prefix run
```

对应配置为：

| 字段 | 实际值 |
|---|---|
| `transition_kind` | `new_discretization_and_geometry_guide` |
| `init_script` / `run_script` | `6a65-run-low-wide-expanded-peaks.cjs` |
| `init_arguments` | `["{candidate}","{source}","{prefix}","init"]` |
| `run_arguments` | `["{candidate}","{source}","{prefix}","run"]` |
| `initial_suffix` | `-initial.json` |
| `checkpoint_suffix` | `-state.json` |
| `initial_schema` | `6a65-R219-expanded-peaks-initial-v1` |
| `checkpoint_schema` | `6a65-R219-expanded-peaks-checkpoint-v1` |
| `accepted_counter` | `r219AcceptedSteps` |
| `report_suffix` | 不设；完整初始 baseline 在 initial 中 |
| 输入身份字段 | `source.inputSHA256` |

R219 将实际帽换成新预算、N64 换成 N128，并把原 42 点与新增 42 点合为 84 点。控制器把它登记为新 objective/discretization；只使用它真正返回的新 baseline，计数从零开始。它不把 N64 与 N128 的 finite primitive 说成相同。

每次 `run` 必须保留输入的完整 `options` 和 `peakMetricRows`，输出维数核验为

$$
n=J(4K+3)+2,\qquad i_A=n-1,\qquad i_{Z_c}=J(2K+1).
$$

K11、J33 的实际状态为 1553 列。控制器不写死 1025 列，也不删径向、角向、cut-height 或 amplitude 通道。每个接受必须严格降低该次 normal 的完整 R²；同时单列原网格 metric、加点 metric、合并峰值、曲率、几何见证和真实 OS exit。峰值迁移与积分下降因此不会混在一个“成功”标签中。

每个 continuation 的实际末态仍在 runner/temp 时立即观测。若请求列有后续 continuation，它消费该态及其观察文件，再建立新 baseline。初始或运行 argv 可引用 `{candidate}`、`{source}`、`{observer}`、`{prefix}` 及显式冻结的小配方 `{recipe}`；不使用 shell eval，也不默认复用过时峰点。

## 3. 发布、规则读取与临时数据

每个实际接受步、阶段新 baseline 和额外观察都会更新本 run 独有的同一小报告，随后 commit/push。报告同时保留每个阶段的用途、输出哈希和 stdout 哈希。整个报告限制在 100KB 以下；数组、完整 normal/checkpoint、stdout、frozen source inventory 留在 runner/temp，不上传 artifact 或 Release。输出目录若位于 Git worktree 内，入口直接拒绝。

每次求解前与发布前都真实执行 `git pull --rebase origin main`；长进程期间 45 分钟再次 pull。每次 pull 比较根 README 和本题 README，只打印新差异，并将实际读到的提交号写入 HANDOFF 唯一 `<!-- 6a65-ci-rules -->` 标记行。该行与本次标量报告一同普通 commit/push，完成后才开始下一个 pull 或数值进程，因而不会把未提交的 H 改动带入下一次 rebase。根会话其余 HANDOFF 段不由 CI 改写。

如 README 有变化，控制器明确标为未审，先将本次实际读取及未审状态写入上述回执并推送，再退出数值子任务。根会话需要读取这些差异并更新请求；它不会虚构“自动理解新条款”。根会话继续负责研究任务和其余 HANDOFF 状态的推进。

本地 `user.name` 与 `user.email` 在初始化时设置，覆盖实际 rebase 产生提交的场景。GitHub 凭据只来自 workflow 的 `github.token` 环境变量，通过进程级 Git 配置传递，不写文件；数值子进程不继承 `GH_TOKEN` 或 `GITHUB_TOKEN`。

新 CAS 分类器匹配普通 non-fast-forward、`fetch first`，以及实际见到的 `cannot lock ref ... is at ... but expected ...` 和 `incorrect old value provided` 竞争。竞争时立即 pull/rebase，再追加本次 H/report 普通回执 commit 后 push，循环至成功，全程不用 amend 或 force。特别是 rebase 可能发现先前本地提交已经被另一写者纳入 main；这种情况下仍只追加普通提交，不改写那个已发布的 HEAD。权限、受保护分支 hook 和网络失败仍为显式失败，不冒充并发 ref 竞争。

若 rebase 仅在 HANDOFF 冲突，自动恢复还须核验：待重放提交去掉唯一 CI marker 后，与合并基底的其余文本完全相同。只有满足这项逐字检查时，才保留上游 H 的全部非 marker 文本、补入本 CI marker，实际执行 `git rebase --continue`。任何额外文件冲突或非 marker 的本地修改均不套用这个恢复分支。真正出现过的 pull 命令退出值及 marker 恢复事实另存回执。

报告中的 `running` 只表示最近一次成功发布时的状态；是否仍在运行必须同时查实际 Actions run/job 的终态。入口结束时输出真实 controller 退出信息；完成请求的有限步数不会被当成课题完成。

## 4. 同 job 后继小配方接收口

首请求指定独立的 `ci-requests/6a65-strong-followup-20261126.json`，该路径不触发另一个 workflow。每一段结束先完成真实 dense observer，再发布 checkpoint/observer 的实际 SHA-256，保留这两个原文件并等待根会话的新配方。首请求使用径向 4 分与半周 256 角区间，保留当前 N128 primitive。

等待期间每 30 秒只读 fetch，并输出包含 UTC、run ID、当前输入哈希和规则检查提交号的 heartbeat。发现新配方将要消费，或距上一次实际 pull 达到 45 分钟时，才执行 literal pull、检查双 README、把 SHA 写进 H 并普通提交推送。这样既满足每次 pull 必有 H 回执，也不因轮询而每 30 秒写 H。没有用静态 `running` 页面替代进程状态，也没有内部等待截止时间擅自丢弃 raw。外部 Actions 的 350 分钟资源时限仍需根会话据实际进度管理。

接收的小文件必须是当前 `origin/main` 的真实 Git blob，严格匹配当前 `run_id`、`attempt`、`parent_state_sha256` 和 `parent_observer_sha256`。本地临时文件、另一次运行的旧配方和已经消费的 ID 不能启动动作。合法的 continue 配方结构为：

```json
{
  "schema": "6a65-strong-branch-same-job-followup-v1",
  "followup_id": "root-chosen-new-unique-id",
  "run_id": "ACTUAL_CURRENT_RUN_ID",
  "attempt": "ACTUAL_CURRENT_ATTEMPT",
  "parent_state_sha256": "ACTUAL_CURRENT_CHECKPOINT_SHA256",
  "parent_observer_sha256": "ACTUAL_CURRENT_OBSERVER_SHA256",
  "rules_read_commit": "ROOT_ACTUALLY_READ_FULL_GIT_SHA",
  "action": "continue",
  "source_commit": "PUBLIC_MAIN_ANCESTOR_WITH_NEW_SCRIPTS",
  "continuations": []
}
```

这里的占位文字和空数组只是协议示意，不是可运行配方；真实文件必须使用实际哈希及非空完整 continuation。新脚本限制在本课题的 `scripts/6a65-*.cjs`；只有完整已公开 main 祖先提交可作为 `source_commit`，冻结新 source epoch 时再次保存全清单哈希并要求候选文件字节不变。实际已载入的 Python controller 身份单独保存，后来 pull 的新 controller 文件不能冒充正在运行的旧程序。新小配方可借 `{observer}` 读取刚完成的观察，由根提供的 adapter 冻结新的点/结点及完整 baseline，然后再开始真实接受步。

若根明确决定释放该 runner，必须提供同样严格匹配输入的 `action: "release_runner"` 及非空 `reason`。该动作登记为显式释放资源，不是数学完成。无效配方记录拒绝，旧运行或已消费的配方不再消费，当前 raw 保留；只有匹配的新配方才能继续或释放。controller 还保存每次 pull 时的原 HANDOFF Git blob，根会话可据此核对独立 marker 与其它段的历史。

## 5. 本次实际验证

新 Python 入口编译通过。使用已存在的 quartic 第 6 态与 K11 第 3 态实际 JSON，成功读取 1025/1553 维完整布局及它们的 scalar schema；这是消费兼容性检查，没有重跑优化。

实际 GitHub ref-CAS 报错文本、`incorrect old value provided`、普通 NFF 均被识别；protected-branch hook、permission 和 network 三类文本均不被误判。

另在独立 scratch bare Git 仓库做了真实竞争回放：controller pre-publish pull 后，第二个 clone 推进 main；第一次 push 实际被 NFF 拒绝，controller 随即真实 pull/rebase、刷新回执并第二次 push。进程真实 exit 0，发生 2 次 pull、2 次 push，最终本地 HEAD 等于远端 main，两边写入都保留；rebase 时 bot identity 已存在，全程未用 force。该测试没有操作公共研究仓库的 Git 分支，也没有伪造一次 GitHub Actions 执行。

接收协议的独立临时 Git 验证也真实 exit 0：指定提交的 archive snapshot 读取成功；未发布小文件不消费；匹配且已发布的小配方可接受；本地未发布修改、错误 state SHA、错误 observer SHA 均被拒绝；另一个 run 的旧配方被忽略；明确匹配的 runner release 可识别。这些只验证控制协议，没有启动数值进程。

最后按逐次 H 回执的新语义另做了两次真实竞争回放，均自然 exit 0，每案实际 3 次 pull、3 次 push 尝试。第一案 root 同时修改 H 的非 marker 段，实际发生 rebase 冲突，经过上述严格 marker 检查恢复后，两边的 H 内容全部保留。第二案另一写者先将 CI 的待推提交纳入 main，再提交 root 段；CI 随后的 rebase 与普通回执提交保留了这个已发布 root commit。两案每次 pull 前工作树均干净，所有实际 pull 的 SHA 都已出现在推送后的 H 历史，最终工作树干净，未使用 amend 或 force。

后续科学结果只能来自真实新运行。此实现、基线转换和基础设施验证不支付精确等距方程、连续余项、全域/全时嵌入、非局部 reach 或最终非平凡柔性族。

## 实际启用的R208后继

初始请求已直接列入第二段 `r219-observed-radial`，分类为 `same_field_radial_refinement`，入口 `6a65-r219-radial-refine-from-observer.cjs` 消费真实state与observer，参数 `candidate source observer prefix both`，输出initial/report。它使用R208完整有理延拓，保持物理场/帽/时钟/角求积，重建径向求积baseline后继续既有R219 runner。对应本地实际三个结及三接受见 `2026-11-26-6a65-r219-observed-radial-three-accepted.md`；CI仍以自身真实选择、实际字段和退出回执为准。

## 自然拒步时保留真实末态

新阶段若数值进程自然exit0、checkpoint全部schema/输入哈希/列布局/计数均正确，但LM未接受，controller另核z与父态完全相等。该状态的指标使用其真正baseline，不能使用最后一个被拒trial的evaluation；计数不增。它立即真实观察保留下来的完整场，跳过未发生的余下计划并进入严格匹配后继等待。非零exit或不合法checkpoint仍明确报错；原17步恢复不套此分支。这是失败状态的保存机制，不把拒步称为数学改善；尚无本job拒步实际发生的声明。
