# independent-seed8000：原公开 M14 种子的独立数值入口

2026-11-10，Astra-visible-flex-78718bd0 / numerical_recovery。
**冻结供完整独审；纯准备已实际完成，候选 solver 从未由本作者启动。**
指定未来执行者为 `/root/independent_audit`。本文件不宣称已经完成独立求解、
新闭图、终门或 README。本轮 root 的 restart8000-02 由 root 自己监控；
本文没有读取它的工具 session 或消费它的自然出口回执。

## 1. 这是另一条预先明确的路线

root 在只读核对原种子协议后，选择：从原已发表真 M14/N512 prefix 与它自己的
最后 `_tail_0002` 开始，以同一 g/M14/N512/W14、同 tol/BC 和 max_nodes8000
重新求完整 nonlinear-DN 联解。此选择由作者预先冻结；独立执行者不选初猜、调参或优化。
不强制重做6500历史失败，也不回退M12或另作 raw lift。

它不等于当前 root 的“run02失败CP→restart8000”命令逐字 replay。
没有在新输入中使用 root 本轮失败 CP、失败末包0003、失败观察或6599初猜诊断。
如果将来独立产物的数学 payload 与 root 图不同，就按原完整协议把它当作另一张
同 g 图重新认证、比较并明确最终采用对象；不能借用 root 图的证书或改系数凑 hash。

原输入目录是本轮逐字重建的旧来源路径：
`/workspace/scratch/db6f0b0e7462/math-research/topics/visible-flexible-closed-surface/notes/`。
重建不是恢复旧进程。

| 原始角色 | 文件 | SHA256 |
|---|---|---|
| 真 M14 prefix seed | `2026-11-09-db6f-prefix-flat-v17v18-fixed-m14-d12-p8-s32-q512-outer-from14.json.gz` | `3df8eefb18c4271283c7ae2b076afcda3fb42b169c8a7296ee4bce3e3b3ad3d0` |
| 该 seed 自有末 DN/J/audit | 同 stem `_tail_0002.json.gz` | `009bf5472ca412fae7d900d4ec18d26cd217221138666c2899dfceb3ead8f762` |
| 原97项 reference | `2026-11-09-db6f-prefix-spectral-affine-m14q512-01-launch.json` | `e45c553ea6832525c6a2719a197dbcc49a7ee5dd77badfb4b363e19a4b974a83` |
| 原141项 source launch | `2026-11-10-78718-numerical-m14-direct-csc-02-launch.json` | `b935a5863a88e6c4541357a558c6b3874ed3ba89174b65032b0494425681c671` |
| 原152项运行来源闭包 | 同上 stem 的 `-guard-launch.json` | `c5a9bb2d5bba1099db7b489d52b423b0fff135be339a8ea435989f235d3b8063` |

原 source launch 的历史主计算后来失败，但它在启动前绑定的代码、config、公开 seed
仍是这些 source 身份；新入口没有从其失败输出推断任何新成功。
原 seed 是2633节点、finite `solver_success=true`；自己的 warm 残差为
`5.397833270174952e-10`。完整 PP、profile/chart/port/summary/reproduction 的身份
见 `numerical-original-independent-seed-bindings-01.json`，其97项已实核。
公开 seed 的有限成功不代表其旧整图已经达到 G5。

## 2. 明确冻结的八件新源

全部在本题 `scripts/`，每件<100KB。旧 restart8000、所有原 mathematical kernels、
canonical core/checker 和 root recorder 均不修改。

| 文件 | B | SHA256 |
|---|---:|---|
| `78718-build-independent-seed8000-entry-v1.py` | 27706 | `0bf553b59da21e48676dceae8046c062160210bbec059c6530ddb75ffd943b43` |
| `78718-prefix-independent-seed8000-inputs-v1.py` | 16312 | `3508c37cb4d9ff48702143b00fa668b6938b40e1e85e97d6ac0ae74cc55397be` |
| `78718-prefix-prepare-independent-seed8000-v1.py` | 6324 | `f06e3c4a4fc9dfdfea73ace6eceb7658493106ede5dfac88947f51ae722c31df` |
| `78718-prefix-spectral-independent-seed8000-v1.py` | 18858 | `2fec0b89aab9611677fef9c2eab70b78d9eef8e22b85dfcd5b46753e2d4517b5` |
| `78718-prefix-audit-independent-seed8000-v1.py` | 32581 | `067f8944cb0d75ceffc846119b1ca2511f0e6e886799258e4659b023d8828578` |
| `78718-check-independent-seed8000-runtime-v1.py` | 5014 | `c9a9adfc03688740ee258fff6895d4b0a62aa25832a9ab133dd5b75c8aba3f52` |
| `78718-prepare-independent-seed8000-guard-v1.py` | 2880 | `f40f1157153a608c3744e772fffc5f8097195c25d2000c20ea9f7c7e7f8b9e4d` |
| `78718-record-independent-tool-observation-v1.py` | 3825 | `65daca0b3bc7b8512bab1fff4edf672c2d158a0b21198b2d0f5a23815a7f0a6b` |

生成器从七件冻结旧源作唯一声明的逐字变换，输出全 unified diff；同时 source-only
compile，拒绝覆盖不同内容的已存在新文件，检查所有旧文件仍逐字不变。
真正执行的 `9d0781` exit0 只生成这些源码和账本，没有载入科学模块或运行数学。

生成账本 `numerical-independent-seed8000-derivation-01.json`：4383 B，
SHA `cf8fac0eff1898278a610cec059ae93fc2ff90fc671f3ea359d4a4a3bd5fdf9f`。
完整差分 `numerical-independent-seed8000-source-diff-01.txt`：46,451 B，
SHA `7746ccfbb3ffeb30ab1bce533155c7fcf16f5ca2f8b444a390369648e4a79a93`。
对照的旧文件 SHA 逐件写在生成器和账本内，不把新入口冒称旧源码身份。

## 3. 每一层实际改动

### 输入与准备

先运行原未改动的 source ancestor `validate_inputs`，付原97/141来源、固定g、
W14和全部 prerequisite。再只读原152 guard source bundle，核全部真实文件并检查
包含原141项；这个 guard 仅作为**启动前来源清单**，不用于判断任何自然出口。

直接 seed/末包硬钉第1节原 M14 身份，旧 packet 的完整17 jet/616 Jacobian/8 audit
和原参数来源由原 check_packet 核；原 PP 哈希全部包含在原来源闭包。
config 从原真实 config 复制，仅更新新 I/O，`initialCheckpoint` 保持原自己的0002。
委托 argv 从原复制，仅改新 tail-config/out-prefix、明确的原 seed 路径和 max_nodes8000；
其他参数、显式空 warmup、fixed/lagged/preserve-restart-mesh 均不变。

新 settings 为 M14、prefix/angular512、audit1024、nodes1601/max8000、tol2e−9、
bc_tol1e−8、physical_bc_tol2e−11、Node heap1536。nodes1601不覆盖保存的2633节点。
root 对另一个失败CP初猜算出的6599并不声称适用于此公开 seed，也不保证此路线收敛。

共同 canonical source prerequisite 可复用 root 的真实小检查 fbfe98 及其已冻观察。
这是已审通用代码前提，不是这个新独立主计算的观察。准备层还把新 recorder、
runtime checker、guard preparer 逐字纳入165项来源，明确 `executor=/root/independent_audit`。

### 数学调用和完整 runtime

driver 不改原 `runner.main`、coupled outer loop、物理 RHS/BC、DN/J/audit 请求、
保存物理 quintic、谱权 W14 或 release-LU/direct-CSC 数学函数。
before/after/restoration 仍核完整十函数 typed code：四个 SciPy、三个 foundation、
两个 selected closure及 selected Newton；原 raw记录和其所有闭包检查继续保留。

实际 `be613c` 的 AST 对照，在仅规范已声明文件名/status/exit-scope字符串后，
driver的15个函数全部与旧版相同，auditor的10个函数相同，只有 `final_audit`
增加执行观察者及工具回执约束。对照报告为1831 B，
SHA `4b7fe19de274c639f31bd2017bff2135e60037c6d2709accd0ec1d1d2b594630`。
这仍是 source 对照；不把它替代任何真实求解。

### 最终出口和 actor

最终成功名为
`PASS_INDEPENDENT_OBSERVED_SEED8000_M14_W14_FINITE_COUPLED_CLOSE`。
除明确的新来源/status身份外，原 weighted/physical residual、physical BC、全部 outer
真 DN、PPoly全部槽/完整有限性、最后自有 Jac/audit/两jet、所有 runtime/restoration
和 reproduction/闭文件门都保留，max8000上限仍不放宽。

新增观察约束为：

- `observer` **字面**必须是 `/root/independent_audit`，不能把其回执伪记为 `/root`。
- 必须是该 stem 的 `observed-process-completed`，真实 positive session id、非空 tool receipt、exit0。
- `recorder_source` 必须恰为这份已绑定的新固定actor recorder。
- 保存的 `tool_return_metadata.exit_code/chunk_id` 必须与顶层真实出口记录相等，
  且工具返回不再含活动 session id；运行中返回或 Unknown process id 不能付终门。
- 完整 final 仍重新读自身 reproduction、CP、所有PP和末尾文件，逐件对照观察中的 SHA。

记录器自身只是一份受审元数据程序，不能密码学证明调用者身份；真实性来自指定执行者
亲自取得并保存实际工具返回。它不读 guard 的 child exit 字段来填造自然退出。
其 start/complete/unavailable 分开命名，未知出口不得改写为成功或失败。

## 4. 作者实际执行的纯小检查与负门

| 工具回执 | 真实退出 | 已执行范围 |
|---|---:|---|
| `9d0781` | 0 | 七源生成/完整diff/source compile；0数学。 |
| `bb8e2a` | 0 | 原97/141/152、旧公开seed/末包及共用code前提；0写、0solver。 |
| `ac32b3/session82852 → 289aed` | 0 | 10个实际live source identity、10个改变必拒、restoration；1函数factory、0矩阵/RHS/Newton/BVP/DN。 |
| `be613c` | 0 | driver/auditor实际AST对照，仅source。 |
| `d45c80` | 0 | 新纯prepare，165绑定；只写config/launch/preparation三件。 |
| `c0b05b` | 0 | 新纯guard元数据，167绑定；没有启动任何进程。 |
| `b26925` | 2 | 完整 final 缺真实独立出口，正确拒绝。 |
| `ea61ea` | 2 | 试用实际旧 root 观察，正确拒绝固定actor/身份不符。 |
| `19b835` | 0 | 两个 recorder 负测试总检查通过；两个子程序均拒绝且零观察文件产生。 |

runtime 报告 `numerical-independent-seed8000-runtime-check-01.json`：98,368 B，
SHA `8f993d8d2b0580fd0f8bd399efec5cc9eeb1850c2012828a2c77ca0866ba91ac`。
两份负 final 分别577 B/SHA `00514b5a8ecf407cbfaa31da3cdd18b66398d36233a823e24a0bb8f764b14388`
和547 B/SHA `8723a327fbfec467304d791a51218b4310a14a8ac0998bad25e2e0cdbe6c395f`。
recorder负测试1249 B/SHA `a99fc5435e7be50a9e85e1d1f3b0e2ac9282c51093281981b93887e24505ab1d`。
它实际输入的是旧run02的真实guard完成元数据和本作者小检查的真实running tool返回；
两者都没有合法自然工具出口，均拒绝。没有伪造或创建任何正向独立观察。

已纯准备的将来主 stem：`2026-11-10-78718-independent-m14-seed8000-01`。

| 实际文件 | B | SHA256 |
|---|---:|---|
| `-launch.json` | 100701 | `a00359ad76c53e92890f5cd098878929838b6505923deaef92d5603bec421019` |
| `-preparation.json` | 6749 | `846d3f2e8fb85b595d1a93460348714043af1a58f0f43ac14df102645faab3e5` |
| `-guard-launch.json` | 49374 | `5dad81b17ce9e382933f10bf4e52c0c4cd6fee6bb86c8e54c93e4cc839a26e4b` |

launch略超过100KB，只在程序内验证，不能全文倒进对话。prepared不代表已经求解。

## 5. 独审可实际重放的无 solver 命令

下列 `VF_CHECK` 必须取未使用的新小检查名字；不能覆盖作者报告或将来主输出。

```sh
VF_T=/workspace/scratch/78718bd0c4a9/math-research/topics/visible-flexible-closed-surface
VF_S="$VF_T/scripts"
VF_N="$VF_T/notes"
VF_PY=/opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python
VF_CHECK=2026-11-10-78718-independent-seed8000-audit-pure-01
VF_RUNTIME=2026-11-10-78718-audit-independent-seed8000-runtime-01

"$VF_PY" "$VF_S/78718-check-independent-seed8000-runtime-v1.py" \
  --out "$VF_N/$VF_RUNTIME.json"
"$VF_PY" "$VF_S/78718-prefix-prepare-independent-seed8000-v1.py" \
  --out-prefix "$VF_N/$VF_CHECK" \
  --code-check-report "$VF_N/2026-11-10-78718-numerical-canonical-code-root-check-01.json" \
  --code-check-observed "$VF_N/2026-11-10-78718-numerical-canonical-code-root-observed-01.json"
"$VF_PY" "$VF_S/78718-prepare-independent-seed8000-guard-v1.py" \
  --launch "$VF_N/$VF_CHECK-launch.json"
"$VF_PY" "$VF_S/78718-prefix-audit-independent-seed8000-v1.py" \
  --launch "$VF_N/$VF_CHECK-launch.json" --mode final \
  --out "$VF_N/$VF_CHECK-negative-final.json"
```

最后命令现在必须真实拒绝，预期exit2；它不是测试通过的正向候选。
源码生成器的既有版本可在全diff和源hash重算时读取或幂等重放，不能修改已冻结旧源。

## 6. 将来的唯一执行者和持续实际工具回执

只在完整独审及 root 排程后，由 `/root/independent_audit` 亲自启动新 guard
的 `executor_start_command`。它仍为原 `78718-run-m14-csc-resource-6g.py`，
DATA每进程6GiB、Node1536、磁盘free 512/768MiB，未改变数学或承诺总RAM上界。
完整 argv 已在 guard JSON 中，不需要重新选择参数。

唯一执行者在同一个持续 `functions.exec` 控制cell内实际调用 `tools.exec_command`，
保存真初始 session id/chunk id；之后连续等待实际 `tools.write_stdin` 返回。
每约12次（当前空轮询实际约5秒）只汇报小元信息，保存每次真实返回。
监控cell自身失效仍是未知状态；此方式不宣称根治执行器失效。

观察记录命令的结构是：

```text
PRIMARY_PYTHON 78718-record-independent-tool-observation-v1.py
  --out-prefix ACTUAL_INDEPENDENT_STEM
  --phase start|complete|unavailable
  --session-id ACTUAL_SESSION_ID
  --tool-result-json JSON_OF_THE_ACTUAL_TOOL_RETURN
```

其中 JSON 必须直接来自该执行者刚收到的真实工具返回，不能由guard字段推导。
终端传参使用真正的shell引用；`JSON.stringify` 本身不是shell quoting。
示意引用函数为 `s => "'" + String(s).replace(/'/g, "'\\''") + "'"`，对每个独立参数作引用。
结束条件仅为实际工具返回 `session_id == null`、整数 `exit_code`、非空 `chunk_id`；
若抛 `Unknown process id`，只记录 `unavailable`，不填 exit code。

此记录器写出的文件后缀分别为 `-independent-observed-start.json`、
`-independent-observed-exit.json`、`-independent-unavailable-session.json`。
不是 root 观察，也不修改 root recorder。自然出口后的完整审计命令为：

```sh
VF_RUN=2026-11-10-78718-independent-m14-seed8000-01
"$VF_PY" "$VF_S/78718-prefix-audit-independent-seed8000-v1.py" \
  --launch "$VF_N/$VF_RUN-launch.json" --mode final \
  --observed-execution "$VF_N/$VF_RUN-independent-observed-exit.json" \
  --out "$VF_N/$VF_RUN-final-audit-01.json"
```

这条命令目前没有真实独立出口可消费，未执行正向模式。
first mode若将来首包已闭存可作局部检查，不会支付完整finite-close。

## 7. 后端仍需本图自己的完整实际计算

即使上述 finite-close 将来真正通过，也只支付有限 original solver 身份和数值门。
还必须从本独立 CP 的自有最后尾重新导出 tail/prefix/target/bridge/common-cut，
重做完整 continuous metric/geometry/moment/tail/closed-budget/whole/原2e−9 terminal，
并生成同图网格和真实独立结果报告。不能把 root 新图后端移给此另一次计算。

已冻结的 `78718-plan-post-restart8000-v1.py` 明确只接受 root 的 restart8000 成功身份；
它**不能直接消费此新 independent-seed8000 final**。未来接线应使用另名、另审的
success-only计划器，或按冻结相同参数明确执行原全链；不得静默改旧计划器的actor/schema。
storage完整新族也按实际超限和已审完整来源另作明确接线，不改本次主方程。

基本完成条件和最终独立全链都尚未满足；严格无限尾存在性仍与有限数值证据区分。
达到基本条件后继续强目标，不把这份入口准备当作阶段收尾。

## 来源

- `numerical-original-independent-seed-scope.md`：原seed确切层次、公开M14与两段重放的区别。
- `2026-11-09-db6f-audit-final-independent-pipeline.md` §§1、3、5、10：完整独跑和不同payload处理。
- `2026-11-10-78718-audit-restart8000-entry.md`：冻结数学/完整canonical及原出口门。
- `numerical-restart8000-monitored-retry.md`：root实际监控方式及失去旧句柄的限定观察。
- 上表实际回执、生成ledger与全diff：本次实际准备范围。
