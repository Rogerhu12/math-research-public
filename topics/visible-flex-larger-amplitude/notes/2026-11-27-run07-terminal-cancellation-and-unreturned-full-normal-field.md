# 2026-11-27：run07 公开 Actions 终态取消与完整 normal 场未返回边界

## 1. 实际结论

2026-11-27 05:02:15 UTC，GitHub 最新 attempt 的实际 jobs API 返回，公开运行 [45909290354/1](https://github.com/Rogerhu12/math-research-public/actions/runs/45909290354) 与 job `140213487518` 都已结束，运行和 job 的结论均为 `cancelled`。job 的第 5 步“Execute public research and publish independent compact records”同样是 `completed/cancelled`。

这条证据说明运行终止，不能把它改写成 complete normal 场的成功、数学不可行、根失败、QP 失败或某一具体 Python 异常。本次没有取得能确定取消原因的 annotation、完整 child 退出记录或该科学阶段 compact return；本 note 不推测取消原因。

截至本次读取，最后公开控制器索引仍记录 2026-11-27 04:44:16 UTC，阶段 `followup:complete-material-envelope-cached-normal-first-20261126-07` 为 `running`，实际子进程退出码显示“尚未退出”。该索引仅列出阶段 1、2、3 的完整成功返回。这个较早的索引和较新的 API 终态必须同时保留：API 终态不会自动补出科学 child 的实际返回。

## 2. 精确运行与源码身份

| 项目 | 实际值 |
|---|---|
| Repository | `Rogerhu12/math-research-public` |
| Run / attempt | `45909290354 / 1` |
| Workflow ID | `432162487` |
| Job ID | `140213487518` |
| 触发事件 | `push` |
| 初始公开 head | `1cb2fcf6e2d890bd1e11f2913fc64dc499743c7f` |
| Workflow | `.github/workflows/visible-larger-centered-normal-20261126-07.yml` |
| Request | `visible-larger-resume-20261126-07` |
| Request SHA256 | `ba0f4a6afa1e7c7491b1c6e8584f5fe2955192695eb32b5d89a92c26de795337` |
| 实际已加载 controller SHA256 | `9a554b0613a2a6766c25c27f46d5fa3d96c9291af0da475aebefd46ee5d63aea` |
| Run created / started | `2026-11-26T23:10:08Z` |
| Run API updated | `2026-11-27T05:00:28Z` |
| 本次终态观测 | `2026-11-27 05:02:15 UTC` |
| Run / job / research step 结论 | `cancelled / cancelled / cancelled` |

上述 created、started、updated 是 run API 字段，不是科学 child 的起止时间或数值耗时。该完整 run API 响应共 13473 字节，SHA256 `a796797f6aaed095681d5dd2ad9f8799340a0f272008f57e6b32e705a379edab`；只在本 note 复述必要元数据，没有把完整日志、科学数组或逐点数据转入仓库。

实际 jobs 记录显示 setup、checkout、setup-python、安装依赖四步成功。research 第 5 步取消，post setup-python 跳过，post checkout 与 Complete job 成功。后处理成功不代表研究步骤成功。`logs_url` 在该 jobs 响应中为 null；这也不是全日志不存在的证明。

## 3. 公开 compact 的准确边界

最后读取的索引为：

`notes/2026-11-26-public-actions-45909290354-1.md`

其 Git blob 为 `6a8f104de5701549f9c5c6ac5e69afb0acb75bdf`，UTF-8 3897 字节，SHA256 `c60012c79255c3e901a4f6453a86ce78533edef7317468e86e6135dbafda9ff0`。索引记录的时间是 2026-11-27 04:44:16 UTC。实际返回卷为：

`notes/2026-11-26-public-actions-45909290354-1-part-001.md`

| 阶段 | 实际公开返回 | 退出码 |
|---|---|---:|
| 1. complete warm | completed | 0 |
| 2. independent-axisymmetric-R690-reference-prepare-v2-first-20261126-07 | completed | 0 |
| 3. restore-actual-run05-complete-carrier-2397-leaves-20261126-07 | completed | 0 |
| 4. complete-material-envelope-cached-normal-first-20261126-07 | 最后索引为 running；终态前没有该阶段 compact return | 未知 |

原阶段 3 已实际逐字再生旧 `dc5ffc55ecc4478d265bbad6e8f2abcf672709d99365e14ead01478a4042e7d0` carrier，227202 字节；该结果及新旧 cells/u/Gauss 的实际字节核对保留于既有完整阶段 3 记录。阶段 1–3 是必要输入生产的成功，不等同后续场、normal 分支、全域度量或几何的成功。

没有公开第 4 阶段完整 return，因此不能填写 final checkpoint/report 身份、实际 Phi、有限观测最大残差、接受的方向数、最后 normal stage、root 缺陷、完成角数或内层驻点状态。也不能从缺少后续分卷推出 runner 从未建立任何中间缓存或文件。

## 4. 完整科学任务与未返回的后继

第 4 阶段的实际完整入口是已刊的 `fullclosed_reference_centred_c1_material_envelope_so3_qp.py`，SHA256：

`cc0a07369a2d9ea5e22d261441420acb4e486a8c0d43f29f57e03378e82627b5`。

它使用原固定参考、完整 normal 32 段、全部原变量与原范数、全部材料包络、原完整非线性筛和 QP/Phase I 机制。输出目录为 `reference-centred-c1-material-envelope-normal-lift-first`。完整 argv、输入、所有 source pins、纯 reader 和后续费用/精化参数仍以原完整队列、已刊 ready 与完整参数归档为准：

`computations/resume-20261126-followups-07.json`。

本终态记录不修改或缩减其中任何科学参数。已经发表并排入队列的完整 pure reader、全实际 mean-batch 费用、完整 node 输入/费用以及 M320 两步，均没有在上述公开索引中返回。准入参数不等于实际执行或成功；本 note 不给它们补填阶段号、数值、paid 状态或 checkpoint。

M320 的完整源码、零嵌入/父字段合同及费用源仍是可审查、可复现的后继，但只能绑定之后实际存在且通过其原完整 guard 的父。不能把 run07 未返回的 cc0a 场当成已得父，也不能把 M320 未返回当作频率精化失败。

## 5. 未知历史责任不因终态消失

完整包络政策的有限地址责任为原 11 个完整输入 payload 的 P0，与旧/当前全部材料格 G 的并集。原 source-closure 证明和实际 carrier 再生负责这个有限地址全集；它们没有恢复未知 child 中每条 typed 行的首次发现 provenance、保护角色晋升、顺序或实际筛值。

因此，终止的 run07 不被记作“没有新位置”“没有 typed 记忆”或“所有历史为空”。下一独立分支若采用已经明示的新包络契约，必须保持全 P0 与全 G 的完整真实筛，明确未知历史的角色/顺序没有冒作实际继承；若以后取得适用的真实报告，则依完整 source、model 和实际父合同合并。未知计算中间结果不能从哈希、相同 argv、计数或其他 run 的字段构造。

新 run08 的独立 fixed-chart 输入与 run07 有各自的完整数学身份。run08 必须采用其真实定义，不把 run07 的值或证书转移给它；旧材料地址责任可以通过已经明确的独立包络机制承担，其数学目标身份与历史地址责任仍分别核对。

## 6. 接续方向及证据限度

本次长时间没有首场返回，使完整 normal 帧的计算成本成为下一需要处理的实现问题，但本次证据没有给出逐函数实测时间，不能宣称某一个函数已经被 profile 证明为唯一瓶颈。

已读取的完整源码显示：拟接入的解析局部 Newton J3 只替换 `_stage_jacobian`；normal frame 的 order 1/2 仍涉及完整闭合三分量对六控制量的多次反向微分，以及所有 32 段的当前点、frame、目标和隐式导数传递。后继将从实际完整 working 表达式推导解析 frame 导数，保留所有变量、段、角、永久行及活动上游图；它不是取消原研究标准或缩小子问题。任何新源、数值算术变化和实际成本均需独立记录，不能预报加速或收敛。

本 note 只登记真实终态、真实已有返回和未返回边界，没有执行本地科学计算，也没有把 API 取消状态解释为数学结论。
