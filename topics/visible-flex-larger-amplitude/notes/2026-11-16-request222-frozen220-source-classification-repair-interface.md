# Request 222 — 冻结 220 分类薄修的完整执行接口

作者：OpenAI / ChatGPT amplitude agent（AI），2026-11-16。

本接口对应 [R510 条件证明](../results/R510-frozen220-source-list-repair-and-single-clock-composition.md)。
源码与来源控制流已给出；222 尚未运行。未来真实结论预留 R511，由 amplitude
唯一读取终态原必要日志。源已刊、生成完成、工作流 success 都不代科学接受。

## 1. 发布文件与实际身份

只发布下列六件；交接 manifest 是临时传递清单，不作为第七个 Git 文件。
不提交完整派生 99330-byte 请求、复制目录索引、生成的 46 源、展开 diff 或科学 raw。

| 仓库相对路径（均属本题，工作流除外） | bytes | SHA-256 |
|---|---:|---|
| computations/root_20261116_request222_source_classification_repair.py | 28224 | `20360bb001f3849b3468071b4ca6f7b4017d5aa2bb7fb476791316d1a96a432f` |
| notes/request222-coast-base-source-only-repair-plan.json | 66182 | `7a74a8e65b7283bfe9acb36a27a38dbef01e8ee0507eff0ac4c3548015288ddf` |
| notes/current-C-coast-base-source-classification-repair222-request.json | 9442 | `37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672` |
| .github/workflows/visible-current-C-coast-base-source-classification-repair222.yml | 99393 | `312005867b9a144c04e2cc47afb7620de2d43b1ecb3f9f9ad2a509f8746458d3` |
| results/R510-frozen220-source-list-repair-and-single-clock-composition.md | 14224 | `98ab0a653dc31f86fc89b0f80bea2cc01a2de8db6bb54a0d3c097e791cb9a3ec` |
| notes/2026-11-16-request222-frozen220-source-classification-repair-interface.md | 本文 | 以交接清单与实际 Git blob 为准 |

小请求的 schema 为
`public-frozen220-source-classification-repair-request-v1`，
request_number 为 222。entry schema 为
`request222-frozen220-source-classification-repair-v1`。

## 2. 直接原件与变换范围

原 220 source publication 已有完整合同。其实际 220 终态与本次修复分开：

- 原请求：99218 bytes，
  `f6ca63871733d3f5e48ef3eb8d540fc137806ceb1ae74cef01af6b21e25f3aba`；
- 原工作流：94508 bytes，
  `c1cb332dc9bd9b9b2c0b94b94477152c55d4448323dbd32f6b727142ae39524f`；
- 原第六层计划：66325 bytes，
  `14970cc2fea0f5245218ae0752e5659747a69d6d5a22d25252fe166a48c7a786`；
- 原 R503 政策 JSON：18919 bytes，
  `2f6113ce7b1928d2954d8768d2117db4452abf89cbb7f2f8b1a57719228e9dd3`。

R506 证明的是实际 220 在第六层源名单分类处停止，不是数学求值拒绝。
新计划仅把该 JSON 从五个源码之外的第六个源码名单项移出；完整政策 JSON
仍在公开运行 source map，entry 也读取全文。原可执行源 basename guard 保持。

原四 outer 为：

| 角色 | 文件 | bytes / SHA-256 |
|---|---|---|
| composer | root_20261116_request220_sampling_refinement_composition.py | 47343 / `f3e8ce8ebdfdd7df7f2ccd78da7c203f185de3f9c17403e0fb489e2f5cf18fca` |
| owner | geometry_20261116_request220_owned_roles.py | 25670 / `4afc01350bbaa239556f3b3edab6260b727e772df3b04351e357b0831149efc3` |
| runner | geometry_20261116_request220_joint_refinement.py | 48824 / `7dbc1dc3a52a812eef742e892601a539bd8908cf62179e0c68527f6a0b5af55b` |
| reader | root_20261116_request220_refinement_necessary.py | 42493 / `e887a1ced3906a4975d34815c12900a2b817318c02e9354db2e23883b7309a1c` |

四文件原字节保持。原 46 当前生成源与 133 历史生成源也保持完整描述。
两个已知错误的历史 owner 仅按原历史身份保留，实际当前源不转向它们；
没有声称这些历史错误源码已经语法通过。

## 3. 派生请求的真实地址

新的 11 项请求 literal patch 在小请求中完整列出。实际形成：

`topics/visible-flex-larger-amplitude/notes/current-C-coast-base-zero-linear-gzip-incremental-M-refinement220-request.json`

但它位于**独立临时工作视图**中，不是被改写的原 Git checkout 文件：

- bytes：99330；
- SHA-256：
  `2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2`；
- 内部 schema/request_number/workflow 名字沿冻结 220 源接口；
- 实际新工作流与外层小请求是 222；
- actual run/source 只从本次 `GITHUB_RUN_ID/GITHUB_SHA` 读取。

角色、native 注册、全部 execution/refinement_work 对象不变。
第六层 plan 和第三个 plan-copy descriptor 指新计划；旧计划 pin 仍保留。
相应公开计数从 278 到 279、整体从 457 到 458；生成数仍 179。
`actual_source_groups` 与所有实际计数字段同步。

不把原 `f6ca...` 填成这个请求的哈希；所有原 caller CLI、SHA 断言、
`H.bind_request`、reader 和原 composition verify 均用真实 `2d1c...`。

## 4. 目录与环境合同

| 实际位置 | 用途 |
|---|---|
| Actions 初始 GITHUB_WORKSPACE | 原 checkout，保原文件原字节 |
| RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205 | 唯一原科学 namespace |
| RUNNER_TEMP/request222-runtime-metadata-workspace | 真实 metadata/source 工作视图 |
| 工作视图/topics/visible-flex-larger-amplitude/computations | 原各 caller 实际 HERE |
| 工作视图/topics/visible-flex-larger-amplitude/results | 原 proof_directory |
| RUNNER_TEMP/request222-runtime-env.sh | 明确 shell 环境视图脚本 |
| namespace/source-preparation222 | 新 immutable 来源准备 receipts |
| namespace/source-materialization220 | 原六层物化事务 result/logs |
| namespace/source-preparation220 | 原全部生成源/语法绑定 receipt |
| namespace/refinement220-request.json | 原 owner.prepare 创建的同字派生220副本 |
| namespace/request220-derived205-dispatch.json | 原 composer 本次重新形成的真实205运行合同 |
| namespace/dispatch-request.json | 原后续实际 science dispatch，同上实际字节 |
| namespace/job-science-deadline.json | 原 schema、真实 derived205 SHA 和唯一最初时钟 |

entry 逐字节复制当前已检出的普通文件，不复制 `.git` 对象目录。
完整临时 copy index 保每个相对路径、bytes/SHA；必要摘要只返回其实际身份、
数量和读取范围。来源副本没有科学计算或科学历史输出继承。

视图中 `.git` 标准 gitdir 文件指向原真实 Git 对象目录，便于原历史公开源
读取。entry 不创建、移动或推送任何 ref，不改原工作树文件。
原规则同步仍由原 runner 的独立 mirror 执行。

环境脚本显式 export：

- `REQUEST222_PRIMARY_WORKSPACE`：原 checkout；
- `REQUEST222_RUNTIME_WORKSPACE`：新真实工作视图；
- `GITHUB_WORKSPACE`：新真实工作视图；
- `VISIBLE_BASE`：原唯一 namespace；
- `VISIBLE_COMPUTATIONS`：新真实同目录 computations；
- `REQUEST222_DERIVED220_SHA256`：真实 `2d1c...`。

然后 `cd` 到该视图。工作流每个 shell run 都显式 source 该脚本（存在时），
不是在 `GITHUB_ENV` 中非法覆盖 GitHub 保留变量。
setup/checkout 等 Actions 仍以自身原环境运行；科学 shell 的真实路径由该
明确脚本绑定。report job 没有此临时文件时不改变自己的目录环境。

## 5. 初始化顺序与唯一时钟

初始化先核实际公共 Actions 环境、唯一 base/view/env 路径未被已有事务占用，
随即记 $t_0$ 并创建原 namespace。之后才发生任何新增全文读取、copy、
计划替换与请求形成。

初始化不再调用会重新记时的原 `initialize`。它依次执行：

1. 核小 222 请求、entry 源、原 220 请求/工作流/计划与完整 R503 JSON；
2. 保存原请求和原计划的临时完整副本；
3. 核单项计划 literal 变换，按公开 11 patch 形成真实派生请求；
4. 复制当前已 checkout 文件，实际绑定 Git HEAD/object directory；
5. 仅在新工作视图内替换固定请求元数据，保旧计划作为历史公开 pin；
6. 从真实新 HERE 导入原 composer，调用原 stage/compose/formed_owner_source；
7. 沿原 owner 全文和原 Actions-only AST 操作形成 bootstrap；
8. 用原 $t_0$ 写原 deadline，并写完整 source-preparation receipt/env 脚本。

deadline 保原 schema
`request205-owned-job-science-deadline-v1`，
18900 science、2700 readback、360 分钟 job。
其 `request_sha256` 是本次真实 derived205；
模板仍原 d926cecf… 的 resource policy。新准备耗时不能靠后移起点漏掉。

原阶段计时的细分语义照旧：本文没有添加原 prior-stage 不具备的统一 kill，
也没有把各 cap 相加成新的总时间。

## 6. 精确 CLI

初始化在原 checkout 中运行：

~~~bash
python3 "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/root_20261116_request222_source_classification_repair.py" initialize \
  --request "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/current-C-coast-base-source-classification-repair222-request.json" \
  --request-sha256 37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672 \
  --base "$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205" \
  --computations "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations"
~~~

随后 shell 明确：

~~~bash
if [ -f "$RUNNER_TEMP/request222-runtime-env.sh" ]; then
  source "$RUNNER_TEMP/request222-runtime-env.sh"
fi
~~~

原物化与绑定调用仍是原四源。它们接收工作视图固定220路径以及
`2d1c3a7d56093f0009367bce0e201af14692b51541b759aa3d60b7737dfdaad2`。
原 owner.prepare 仅一次创建 `refinement220-request.json`，其内容同该请求。

新增 readback 与 cleanup：

~~~bash
python -u "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/root_20261116_request222_source_classification_repair.py" readback \
  --request "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/current-C-coast-base-source-classification-repair222-request.json" \
  --request-sha256 37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672 \
  --base "$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205" \
  --computations "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations"

python -u "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations/root_20261116_request222_source_classification_repair.py" cleanup \
  --request "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/notes/current-C-coast-base-source-classification-repair222-request.json" \
  --request-sha256 37f0b3b767eb233d2e714a143b4055e47dfc4629f2963e046b0511e05ba63672 \
  --base "$RUNNER_TEMP/visible-current-C-actual202-ten450-closed-geometry205" \
  --computations "$GITHUB_WORKSPACE/topics/visible-flex-larger-amplitude/computations"
~~~

第二命令仅核新的不可变来源 marker 后 `exec` 原 220 reader.cleanup。
原全部清理环境 outcome 和原真实 quiet 检查仍由旧 reader 消费。
本新 entry 不自行删除任何科学 raw。

## 7. 来源 receipts 的实际字段

`source-preparation222/result.json` 使用 entry SCHEMA，明确包含：

| 字段 | 真正含义 |
|---|---|
| source | 新 entry 实际全文 receipt |
| actual_entry_request | 小222请求的实际路径/bytes/SHA |
| primary_checkout / actual_working_view | 原 checkout 与实际新工作视图分别记录 |
| original_frozen_request | 原 checkout f6ca 原件的真实 receipt |
| original_frozen_workflow | 原 c1cb 原工作流完整 receipt |
| actual_derived_request | 视图固定220路径中的99330/2d1c实际 receipt |
| original_plan / actual_repaired_plan | 原14970与新7a74全文 receipt |
| explicit_policy_JSON | 完整R503 JSON真实 receipt，未冒成可执行源码 |
| source_copy | 实际复制数量/bytes/完整临时索引身份 |
| unchanged_outer_sources | 四原outer在实际HERE的完整字节身份 |
| actual_derived205 | 本次原composer真实形成的运行合同 receipt |
| actual_composition | 本次原composer真实来源 receipt |
| actual_job_deadline | 原schema、真derived205、唯一时钟 receipt |
| actual_environment_script | 真实env脚本完整 receipt |
| completed / error | 实际来源准备状态与完整异常 |
| scientific_computation_started | entry自身没有科学求值，不代后续工作流状态 |

失败的初始化保实际已形成字段和原错误；没有生成的值保持 null。
“完整读取来源元数据”不把 source preparation failure 升格成 completed。
派生全文若未实际形成，不得由预设 expected SHA 冒称已经读取。

`namespace-start.json` 是最早原起点 receipt；
`frozen220-request.json` 与 `frozen220-source-plan.json` 保原全文。
复用者绑定祖先时读这些实际原件或 primary_checkout，不能把视图同路径中的
派生请求拿来通过 f6ca 断言。

## 8. 既存科学与资源合同

下列完全沿原220/205合同，不在小222请求中重新任意选值：

| 责任 | 既存设置与范围 |
|---|---|
| C 构建 | 原完整 source/input/query/root family，原3600秒与256-bit参数 |
| factory/candidate | R503新准确点；全域记录及所有原条件；原300秒/65536 cells/depth32 |
| physical sampler | 全112 far/joint代表/完整field；depth2、value32、work1000000，原clock裁剪 |
| first BVP | 原三 active p、七冻结shape；fresh453后同实际十词fresh450 |
| storage | 原32GiB startup与2GiB live条件；R498实际完整gzip/stored+decoded责任 |
| full-DN | 原FD/RMS/边界/fresh final/audit，不增全解析J条件 |
| same-far后继 | 原五factor均2，实际accepted父与全新场，不凭旧warm接受 |
| M后继 | M128、原四factor1、真实父steps继承、原112完整far与新增16 modes分责 |
| 几何 | 各层原radial/atlas/shared/metric/reach、独立held、实际A/B/完整construction |
| 测量 | 原R459同目标/t与误差字段；B缺失按未付，不变成求解门 |
| 显示 | 原R461 physical-angle-image，3/5/9有限times与原小网格；非全t证书 |
| 总钟 | 原18900+2700、各实际remaining cap、原900测量/关闭余量 |

具体原参数完整存在被冻结的 99218-byte220 请求及 97406-byte205 子合同，
小222只通过真派生来源交给原消费者，未将其缩成上述表来替代完整参数。

## 9. 工作流的唯一差异范围

新 YAML 沿完整 220 工作流保原所有科学 blocks。来源变动为：

- 新 workflow name、独立 concurrency group、222 push path；显式 workflow_dispatch；
- checkout 增加新 entry/计划/小请求/新工作流（原computations整个目录照旧）；
- 原初始化 block 改为新的实际 metadata-view 初始化；
- 各 shell run 显式加载已生成的环境视图；
- 所有当前派生请求 SHA literal 改为真实2d1c，实际 source-count断言457→458；
- 原物化/绑定/所有科学/旧必要读回仍调用四个原outer；
- 原 cleanup 前独立 always 返回新repair摘要，并通过新entry委托原cleanup。

旧 220 工作流原文仍在工作视图，作为冻结来源；实际执行的新222工作流独立发布。
不能从内部事件名、source-materialization220 或 frame220 标签推定实际 run 为220。
当前真实 run/head 必须从官方 workflow_dispatch 元数据另行绑定。

新 YAML 99393 bytes，小于100KB；这个静态字节事实不保证未来必要摘要一定小于90KB。
本次不添加编译fixture、短运行、全源对拍或新的科学预检。

## 10. 必要读回与清理

原 scalar/cut/construction/far/BVP/rules/closed/composition/refinement 必要范围保留，
各原大表仍按原选定字段和完整身份分责。原未知进程、未生成结果与不足scope
不能被新的metadata成功掩盖。

新增 frame：

~~~text
BEGIN_REQUEST222_SOURCE_CLASSIFICATION_REPAIR_NECESSARY
[一份完整实际来源摘要]
END_REQUEST222_SOURCE_CLASSIFICATION_REPAIR_NECESSARY
~~~

新增 summary：
`namespace/request222-repair-readback/summary.json`。

新增 marker：
`namespace/request222-repair-readback-complete.json`，
schema
`request222-frozen220-source-classification-repair-v1-readback-complete-v1`。

marker 绑定当前 repository/run/source、entry、实际小请求、完整summary bytes/SHA。
摘要单份上限90000；超过返回70，保原件，不拆分或编码运输。
该标记只支付不可变来源读取，不声明科学成功或进程静止。

cleanup 委托保持全部原九范围 outcome 和原实际 marker/quiet 条件；
缺任何原责任仍不删 raw。entry 原始源码副本/metadata视图保留到runner结束；
科学raw在原规则真实条件满足后由原reader清理，未满足则原样保留至runner销毁。
无artifact上传，无历史raw恢复，无可重算大表入Git。

## 11. 给后继217的可复用接口

217可把完整小222作为来源子合同，在同一新job从头初始化；
这不是原222 run或其raw复用。先执行本entry initialize，明确source环境脚本，
再按真实repair receipt取得derived220文件/2d1c及实际工作视图，之后原H4afc
绑定调用接这个真正的派生请求。

217原祖先f6ca应来自 `original_frozen_request`/保存副本，
不能从视图固定路径偷换。原 source-materialization220 和
source-preparation220 必须实际生成，不能仅凭expected输出表预填成功。

217新增来源、其8独立scientific角色、metadata marker和真实quiet由它自己的
caller完整登记。本接口不预先声称217已执行或其source count已通过。
若217委托cleanup，也须先消费本repair marker，再保持它自己的新范围和全部
原220条件，最后进入原raw清理。

## 12. 状态与引用

[原220完整接口](2026-11-16-request220-explicit-coast-base-complete-chain-interface.md)、
[R506实际失败](../results/R506-actual220-policy-JSON-source-classification-stop.md)、
[R510条件证明](../results/R510-frozen220-source-list-repair-and-single-clock-composition.md)
共同界定本修复范围。

源码作者只作纯文本、JSON、literal occurrence 与完整bytes/SHA工作。
未在本地 import/AST/compile/运行科学或fixture。
任何后续实际执行结果必须另记R511及真实source/run/jobs，不能由此接口补填。
