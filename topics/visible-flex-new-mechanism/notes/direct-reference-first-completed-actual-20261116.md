# Direct-reference 首次完成实际：27 次接受与末模型配额截断

日期：2026-11-16 UTC。本文只消费已经完成的公开 Actions 输出；没有重新运行任何开发检查、几何评价、LP、优化或科学计算。原数组、日志、模型 payload 和 checkpoint 只留原 runner/原日志，不随本文发布。

## 1. 已得到的结果与准确停因

新的 direct-reference 求值方法在同一进程内完成了 28 个模型，接受 27 个新点：26 次普通全步和 1 次 same-layout SOC 全步。两网最大 $\eta$ 从 **0.26623355613853394** 降到 **0.26610226672562226**，下降 **0.00013128941291168372**。终点两网最大曲率为 **57.99972678574561**，原两网各 14 项门全部通过，原 163 维精确盒通过；新目标 $\eta\le0.26$ 仍未达到。

实际使用 **62 次 primary LP 与 1 次 SOC，共 63/64 次**。第 28 个模型的 LP 松弛求解成功，但完整仿射范数评价尚未满足切平面 gap 容差；经原修复规则计算的改善为负。在只剩两个共享 LP 名额时，既有 allocation 规则只授该 primary 一次调用、保留一次 SOC，因而在加入下一轮分离切面之前返回。该模型没有进行物理 trial。

因此，本次停止是**配额分配截断的未收敛切平面模型**。它不是 64 次全局 LP 已耗尽、不是科学时间或单 LP 时限退出，也不证明完整凸模型或实际问题已到驻点。阶段名称 `affine-spectral-finite-model-stalled` 不能单独承担这些更强结论。

## 2. 原运行、只读回读和证据范围

科学运行：

- [run 43780594182](https://github.com/Rogerhu12/math-research-public/actions/runs/43780594182)，job **133016656592**，source **a0d71ea94446f0fcf64d1f69e4dbadd5910204ba**。
- 2026-11-16 **00:33:09 UTC** 完成，Actions conclusion 为 success。该 conclusion 表示审计入口完成，不替代上述科学结果分类。
- 原日志 **8,352,495 B**，SHA256 **ee418c296ab6af5cac1066a19811cc0393c53f7b576244b151183e09f1fe62c9**。
- 请求文件 **41,005 B**，SHA256 **f622a092cbae2b8279f14aebea3f6a3708f1b09b5aa45dd336f3fc7ab74f1cc4**。161 个 source bindings 为 152 个 Python 源、8 个 workflow 和一份祖先人读 note；原 COMPLETE 的 Python 源闭包逐项匹配。

原大日志的原生传输关闭后，使用只读 observer 从原 Actions 读取，没有重跑科学。前两份 observer 因输出限额只给 LIMIT：run 43781737655 / job 133020248595 与 run 43782502991 / job 133022644213；它们分别观察到语义输出 2,439,337 B、1,521,111 B 超过 660,000 B。这是回读输出限制，不能计作新的科学失败。

第三份 observer：

- [run 43783131728](https://github.com/Rogerhu12/math-research-public/actions/runs/43783131728)，job **133024669538**，source **bf89891c487f143317ade7f6b99f665b7b997957**，成功。
- observer 原日志 **660,096 B**，SHA256 **8193f42fafab7c0915377ddff1979438cf3080af696c5b6f7f18a3985e8e1340**。
- 输出明确标记 `priority_output_is_partial=true`、`complete_terminal_MODEL_and_all_minimum_model_gates_preserved=true`。完整保留原 MODEL28、全部 28 模型的固定最小表、全部实际 trial 的两网门、终态及主要成本；次要逐模型 controller 证明和大部分逐模型 oracle 汇总没有输出。本文不声称读完了所有原始大 payload，也不从遗漏字段推算未给出的总量。
- observer elapsed **8.008070619999998 s**，科学与开发执行均为 0。

下表对原 JSON 子串与结尾 LF 分开记账；二者不能混用。

| 原记录 | 不含 LF 的字节 / SHA256 | 含一字节 LF 的字节 / SHA256 |
|---|---|---|
| COMPLETE | 3,981,390 / 529f40fb1f7ba39c30f35f558640c4ac0a364733b9d3ec05be450615beedc02e | 3,981,391 / c9731defe5d0bc80b6f8aaad43e9a834a45e2a53618668c05ec8e06f93ce8c90 |
| MODEL28 | 87,807 / fe46c267b82dca20c727c0cd4f7c6018d83177f5286ce81150da231a3186332d | 87,808 / 4177aefe47ee4675b4f4fc4ceadf3fcb300b0fe7c36450acef6aab5331cf78f1 |
| DEVELOPMENT_REUSED | 3,778 / 4253b279c4f38b2356403eff1b47d3aa1eb862d84c2c425a0eefbdecc0d8b415 | 3,779 / 99d6c415f849dcdd60c8ed774928f7b34441a6df6fbe619791056fca257e9e3f |
| REQUEST 输出记录 | 27,432 / 2df9f5c646ebb0d9f0cda1a3c843fd66d22071b6857ca5d69c2a1dd3d6c5cc04 | 27,433 / c9a013fbfb305cef8e5f5c6fd367ce6aae74f6625744898717b970497697c692 |

三组共 9 个新接口检查已经在此前同任务首运行通过；本轮只消费认证收据，执行数 **0**。两个先前入口失败的科学费用仍并入本独立任务，没有借复用开发收据清零。

## 3. 全部模型与真实接受

表中 $B$ 是建模时真实 trust，gap 是原返回字段；“三次上限，inexact”没有被改写为 gap 已过。第 21 行是 SOC 后接受点。新 C/F 行是本模型真实 trial 的新增粗/细行，末行没有 trial，故不将它写成观察到的零行。

| 模型 | primary LP / SOC | B | 原 gap 判定 | 接受后的两网最大 η | 接受后的最大 κ | 新 C/F 行 |
|---:|---:|---:|---|---:|---:|---:|
| 1 | 2 / 0 | 0.00025 | met | 0.26622869288992607 | 57.999848364468356 | 1/0 |
| 2 | 2 / 0 | 0.00025 | met | 0.26622263811295266 | 57.99981092371375 | 1/1 |
| 3 | 2 / 0 | 0.00025 | met | 0.26621729482262535 | 57.99985461076409 | 0/5 |
| 4 | 1 / 0 | 0.00025 | met | 0.2662135577272118 | 57.999803487853285 | 0/1 |
| 5 | 2 / 0 | 0.00025 | met | 0.2662049260366368 | 57.999805605103305 | 0/0 |
| 6 | 3 / 0 | 0.00025 | met | 0.26620030755287627 | 57.99988315802952 | 0/0 |
| 7 | 2 / 0 | 0.00025 | met | 0.2661947280663144 | 57.999898122707535 | 0/0 |
| 8 | 3 / 0 | 0.00025 | 三次上限，inexact | 0.2661897501633561 | 57.9998006412713 | 0/0 |
| 9 | 3 / 0 | 0.00025 | met | 0.2661846284643238 | 57.99989476051471 | 0/0 |
| 10 | 3 / 0 | 0.00025 | met | 0.2661792812871071 | 57.99980521906743 | 0/0 |
| 11 | 2 / 0 | 0.00025 | met | 0.26617500835963237 | 57.999811999349774 | 0/0 |
| 12 | 1 / 0 | 0.00025 | met | 0.26617020656110735 | 57.999848332929744 | 0/0 |
| 13 | 3 / 0 | 0.00025 | met | 0.2661634171750691 | 57.99984372978924 | 0/0 |
| 14 | 3 / 0 | 0.00025 | met | 0.2661586631021142 | 57.999841969905354 | 1/0 |
| 15 | 3 / 0 | 0.00025 | met | 0.2661540322503452 | 57.999872269554565 | 0/0 |
| 16 | 3 / 0 | 0.00025 | met | 0.2661497459846922 | 57.99987431802775 | 0/0 |
| 17 | 2 / 0 | 0.00025 | met | 0.2661429508344666 | 57.999848395619054 | 0/0 |
| 18 | 3 / 0 | 0.00025 | 三次上限，inexact | 0.26613999651830356 | 57.99986534118239 | 1/1 |
| 19 | 3 / 0 | 0.00025 | met | 0.26613365702385416 | 57.99984735208883 | 0/0 |
| 20 | 1 / 0 | 0.00025 | met | 0.26612936946070764 | 57.99985239447201 | 0/0 |
| 21 | 2 / 1 | 0.00025 | met | 0.26612619587453223 | 57.99987439041138 | 0/0 |
| 22 | 2 / 0 | 0.000125 | met | 0.2661211366616516 | 57.99993233669523 | 1/0 |
| 23 | 2 / 0 | 0.000125 | met | 0.2661190313467215 | 57.999934311861274 | 0/0 |
| 24 | 2 / 0 | 0.00025 | met | 0.26611534119435887 | 57.99975998356774 | 0/0 |
| 25 | 1 / 0 | 0.00025 | met | 0.2661124976500254 | 57.99973301342488 | 1/0 |
| 26 | 2 / 0 | 0.00025 | met | 0.26610586263726377 | 57.99975531388311 | 0/0 |
| 27 | 3 / 0 | 0.00025 | 三次上限，inexact | 0.26610226672562226 | 57.99972678574561 | 0/0 |
| 28 | 1 / 0 | 0.00025 | 配额截断，inexact | 无新 trial | — | — |

全部 28 次实际 trial 都采用 $\alpha=1$：27 次首 primary trial，加第 21 模型的一次 SOC trial。26 次 primary 被接受，第 21 次 primary 被拒；其 SOC 被接受。没有通过回溯缩短 trial 的事实。全部 trial 的两网原 14 门均为 true，全部 omitted-hard 计数为 0。新增池行合计粗 6、细 8，实际学习记录保留。

模型 8、18、27 是未满足切面 gap 但满足原返回/修复条件并经真实两网门接受的步骤；这与末模型 28 经完整仿射评价后不再具有正改善而在几何前拒绝不同。原规则没有因 inexact 标签自动授或撤销接受。

实际 trust 转移可见：模型 21 后 $B$ 从 0.00025 降到 0.000125，模型 22、23 真用此值；模型 23 后恢复到 0.00025，模型 24 的 factory 和 LP 真用了该值。末 legacy/covered 两个 streak 均为 0。优先回读没有保留全部逐项增长/hold 证明，本文只报告这些实际值，不给某个新增策略单独归功。

## 4. 第 21 模型：硬门已过但 metric 变坏，原 SOC 修回

模型 21 建模点最大 $\eta=0.26612936946070764$。首全步两网 $\eta$ 分别为 0.26612722641491915、0.26613161431303145，因此两网最大值增加了 0.0000022448523238072227。完整 actual/predicted ratio 为 **−0.3839068399713508**，原 request-shrink 为 true。

该 trial 的曲率分别为 57.999855531061264、57.99987439041138，所有原 14 门通过。故这次拒绝的具体原因是严格 metric 下降失败，不能称曲率门失败。

随后原 same-layout SOC：

- 共享 LP ordinal **50**，调用前已收费，HiGHS status 0 / success true。
- LP 用时 **0.30551398700001187 s**，原单次限额 10 s。
- 实际使用原 scalar RHS **0.006126195893436824**；报告中的 affine RHS **0.0061264457666106165** 只是另列比较，没有代替原 SOC 约束。
- 同一步最小 scalar slack **0.006123022326165957**，完整 affine slack **0.006123522072513543**，原比较前提保持。
- SOC 后两网 $\eta$ 为 **0.2661261946017748 / 0.26612619587453223**，下降 **0.000003173586175408971**，完整 ratio **0.6771646016067163**，两网原门全过，新增 C/F 行均为 0。
- 接受后下一 $B=0.000125$。本文不把 SOC 接受等同 hold 资格通过。

## 5. 第 28 模型：求解成功的松弛 LP 尚不足以给完整模型下降

这是完整读取的原 terminal MODEL，物理基点 SHA 为 **bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c**，即第 27 个接受点，$B=0.00025$。

| 字段 | 原实际值 |
|---|---:|
| 建模前共享 LP 已启动 / 总限额 | 62 / 64 |
| 剩余额度 / 本模型 grant | 2 / 1 |
| scoped absolute ceiling | 63 |
| 调用后累计 / 末剩余 | 63 / 1 |
| LP 行数 / 变量数 | 9,822 / 161 |
| HiGHS status / success / iterations | 0 / true / 1,060 |
| wrapper / solver seconds | 0.3911994019999838 / 0.379206355000008 |
| 原单 LP 时限 | 10 s |
| 松弛 $\rho$ | 0.006095597967724765 |
| 松弛预测改善 | +0.000006668757897542073 |
| 完整仿射 $\rho$ | 0.006124556969870298 |
| 修复后完整仿射改善 | −0.000022290244247991087 |
| epigraph gap / 容差 | 0.00002895900214553316 / 0.000000001 |
| repaired objective | 0.006124806969870299 |
| repaired 原单位最大行残差 / bounds violation | 4.1928130889087867e−20 / 0 |
| returned candidate / gap met / inexact | false / false / true |
| physical trials / corrections | 0 / 0 |

原状态为 `new-task-pair-allocation-primary-ceiling-reached`；保留的内部停止字段为 `original-shared-LP-budget-after-inner-call`，但 **global_exhausted=false**。实际几何前拒绝字段是 `no-evaluated-affine-model-improvement-above-original-floor`。

本轮 cut 初始化装入 512 条 bank 支持和 4 条此前付费 attainer 补充支持，共 516 条；只有该初始化 cut round，没有新增 separation round。由此可同时成立：HiGHS 对当前线性松弛求解成功，而完整仿射范数模型仍有明显 gap。不能将 LP success、阶段名或剩余一个名额解释成全模型无下降方向。

本模型原完整 oracle 已实际付费评价一个方向、两张完整角网，得到四个 metric attainer；这些新信息可供下一明确的新切面规则使用。原 MODEL 没有保存未知旧 159 维 proposed step（该分支先返回），因此后继不能声称恢复了那个向量或复现了其全部 selected separation。可以保存原 attainer 来源，并在严格绑定的模型上把其法向验证为单位球支持；这与恢复未知旧步是不同的主张。

## 6. 缺陷学习、迁移与池/bank 的终态

### 6.1 学习只在下个模型提交

输入保留旧 8 个 committed events / 7 个 commits；没有重放历史 trial 重新训练，也没有改写旧事件所属 context。新任务产生 27 个真实首全步样本并在下模型作 27 次提交，末 pending 为 0。

初始 $\gamma_C=17.022353404161095$、$\gamma_F=18.064283125328743$；模型 1–21 使用它们。模型 21 的真实样本得到 **28.617940275291502 / 36.60765398014518**，在模型 22 前提交，模型 22–28 使用新值。当前模型内的 guard target 保持冻结。

模型 1–11 的 modified rows 总数为 4，模型 12–28 为 6，所有模型都真正启动了使用相应 guard 的 LP。末模型 C/F modified rows 为 2/4；$\gamma B^2$ allowances 为 **1.788621267205719e−6 / 2.2879783737590742e−6**，最大 target 增量为 **9.733362845544358e−7 / 1.222526080269113e−6**。这些系数来自经验缺陷，仍不是跨中心的连续误差上界，也不能仅从其增大断言它导致了末次不改善。

末 learning state SHA 为 **ce036b3e10183adf94ac1b11c9f3616bdde8339452b5d63716dac2e7edc58b26**。末系数的 exact binary64 分数分别为 2013808518123655/70368744177664 与 5152069275746559/140737488355328。

### 6.2 旧支持合法迁移，新 context 真实绑定

输入 438 条原法向及其顺序保持，逐项单位球/ID 检查通过；新 fresh context bank SHA 为 **7ef2c21e2ea0459a389295006c7085441df8f334d23fc1998d0665df9e271793**，ordered entries SHA 为 **994b060771400b8f5f4aaadb8dcaba954467323bec2299a324e7e9a1a1e9097b**。首个实际 complete-model binding 为 **89be4260319a9b7c70a4fe2ad63ad136ff54b3251acc5f1ce9e0929bc2809d5b**。

只把合法支持法向迁移到新求值 context；旧数值 $A,b$ 没有直接复用，首模型实际重建必要行/J。不可把 old bank hash 当作 new context hash。原 $g,b_0$、永久 reference163、输入 exact159 与物理约束保持；源配置与新配置之间仅有已声明的四项资源/计时元数据差异。

### 6.3 可恢复末点

| 项目 | 终态 |
|---|---|
| 物理 state SHA | bff1348df63200e43bb720e98fa359b057e7370dfbc2090095ba2800803f173c |
| trust / legacy streak / covered streak | 0.00025 / 0 / 0 |
| 粗池 rows / version | 4438 / 7 |
| 细池 rows / version | 4533 / 6 |
| bank entries / capacity | 512 / 512 |
| bank insertions / evictions / inward adjustments | 4842 / 65 / 2502 |
| bank state SHA | 3d674785e4f46a8a5489ab49e6ff7de20d889eec92e4c7a6776ece452acf1611 |
| ordinary evaluation SHA | 8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1 |
| objective evaluation SHA | 49c5f2e8a40c076b716c314bd9a3b41f4a0b8cd1ed40b51e0e83c87ce8266888 |
| factorization SHA | b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963 |
| 新配置 SHA | 1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19 |
| 原付费配置 SHA | b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6 |

4,842 是包含更新的 insertion 计数，不能当作新增不同法向数。模型报告的 cut rows 合计 16,169，其中初始重装行合计 14,062（包含重复重装与每模型补充支持）；减去后实际额外 append 的 cut rows 为 **2,107**。这些也不等于 bank 的不同 entries 数。

原 future checkpoint 保存 reference163、末159/163、完整有序池、bank normals、learning history 与 controller。本文只公开小元数据，不复制 payload。

## 7. 两网原门与数值边界

终态由真实接受时的完整两网 gate 收据核对；没有另做独立末几何评价。新 independent-final geometry 调用数为 0，不能把复用接受收据称为新末验。

| 量 | 粗网 | 细网 |
|---|---:|---:|
| 最大 $\eta$ | 0.26610151616656474 | 0.26610226672562226 |
| 最大 $\kappa$ | 57.99970793595668 | 57.99972678574561 |
| 最大 ball norm² | 0.9905404962357236 | 0.9905404962801558 |
| inner-strip margin | 4.3356534640270894e−8 | 4.335367392860334e−8 |
| mirror 最小值 | 0.09897001594108734 | 0.09897001594145101 |
| 最小 height | 0.02 | 0.02 |
| 全部 14 原门 | true | true |

14 项原字段为 cap_and_box_eligible、curvature_lambda_bound_pass、curvature_scaled_PSD_row_pass、hard_ball_pass、hard_strip_pass、independent_direct_curvature_pass、independent_direct_mirror_radius_pass、mirror_polynomial_pass、outer_strip_pass、previous_metric_budget_pass、regularity_screen_pass、signed_height_pass、single_grid_admissible_recovery_point、single_grid_hard_gate_pass。

163 维精确盒与带旧容差的 height/cap 门分别核对，不混成同一种“精确非负”证明。末模型记录的 affine cap margin **−2.7755575615628914e−17**、重构 margin **−5.551115123125783e−17** 在旧 **1e−9** 容差内；它们不是两个数学非负数，也不是粗/细各一个。

本结果仅授已定义两张离散网的实际原门；不从这些数值追加全连续曲面、全局嵌入或 reach 结论。目标 $\eta\le0.26$ 未过。

## 8. 真实费用：新任务累计、当前进程与祖先分账

新独立任务限额是 **科学墙钟 1800 s（含输入/prepare/冷 ordinary）、64 次共享 LP（含 SOC）、160 次真实 value、单 LP 10 s**。旧已耗尽 m7 epoch 不复活。

| 成本字段 | 实际 |
|---|---:|
| 两次先前入口失败已付科学累计 | 28.690336299000023 s |
| 本进程科学增量 | 228.90499491399999 s |
| 本独立任务科学累计 | 257.595331213 s |
| 本进程总 elapsed | 230.059030169 s |
| 本进程科学钟前 import/hash 等差额 | 1.1540352549999966 s |
| 本次 prepare | 10.074265682000004 s |
| 其中 24 个必要不可变输入 | 6.9143023889999995 s |
| 前一失败收据 / paid9 读取 | 1.3660907559999984 s |
| 原 guard 输入日志 / 收据读取 | 1.7937416700000028 s |
| 新 constructor | 0.10788703200000072 s |
| 本次 recovery path | 218.622569602 s |
| 共享 true values | 58：粗 29 + 细 29 |
| 新独立末 geometry | 0 |
| primary LP wrapper 总时长 | 23.83004208099976 s |
| primary LP solver 内部总时长 | 23.0725505179999 s |
| SOC solver 时长 | 0.30551398700001187 s |
| peak RSS（Linux） | 7,259,612 KiB |

LP wrapper 与内部 solver 时间有包含关系，不相加。source snapshot 的优化钟 **255.903941489 s**、future checkpoint 的科学钟 **257.59346094600005 s** 与最终 COMPLETE 的 **257.595331213 s** 是不同采样时刻，不抹成同一个值。读取收据与必要输入也在本新科学钟内；既有开发不重跑。

粗 selected J 共 28 refresh / 280 batches / cache-hit 1，用时 **14.463139775000002 s**；细网 28 / 756 / 1，用时 **35.598754311999926 s**。没有生成完整159/163列的整角参数张量。其普通重放差是同新实现内部一致性诊断，最大位置/一阶/二阶约 $5.55\times10^{-17}$、$2.22\times10^{-16}$、$7.11\times10^{-15}$，不能冒作旧实现全部数组逐位相等证书。

优先回读没有输出全部28模型的 oracle 汇总，本文不补猜总 JVP 时间。末模型自身记录 1 方向 / 2 全网、direction **0.525053894 s**，16 条当前 metric J 行重建 **0.162563862 s**；这16行不是16个新的实际学习池行。legacy value_geometry_seconds **49.90259652700003 s** 与 fine doubled-angle value_seconds **18.05485164100007 s** 的计时 scope 与下节 adapter 不同，不叠加成“总 geometry”。

旧关闭 epoch 作为祖先费用单列：run43773136836 / job132993290386 的旧 active **241.3142038439999 s**、旧 initialization **293.5427817930001 s**、旧 LP10 / shared values15、唯一冷粗 value **205.448292651 s**。它们没有装入新64/160计数，也没有被删除或重新计为本轮新研究。

## 9. 新 direct-reference 的冷调用与同进程缓存

adapter 实际 started/completed **58/58**，failed 0，累计 **64.4447182289999 s**。首次必要粗、细两次普通评价之间保存了各自 timing snapshot，后续 trial 不会覆盖首次冷/命中证据。

| component | 冷 / miss 事实 | 后续事实 |
|---|---|---|
| reference fixed-height primitive | 首粗 prefix-miss 41.24051114499999 s | 57 hits 共 0.008664933 s |
| reference height jets | 首粗 miss 3.9513918689999983 s | 57 hits 共 0.026398876 s |
| 完整 scalar grid | 两个 grid miss 合计 7.945030371999991 s | 56 hits 共 0.000165617 s |
| fields/frame | 58 次，共 9.196748992 s | 每个真实 state 仍实际计算 |
| null-height | 58 次，共 1.34547272 s | 没有删去五个 null-height 贡献 |
| periodic primitive | 合计 0.494137791 s | 原锚与积分保留 |
| position assembly | 合计 0.146280932 s | 原最后组装 |
| height-control prefix | 首 miss 0.000618435 s | 57 hits 共 0.011040366 s |

首次粗 adapter **45.32524793699999 s**；首次细 **8.196821645 s**，其中 reference primitive / jets 已命中，仅各 **0.000148174 / 0.000431272 s**。两次初始 adapter 合计 **53.52206958199999 s**；后续调用复用了本进程中的原对象与缓存。没有跨 run 保存数组，也没有为比较方法补跑旧几何。

这组计时说明新路径实际保留了首次必要 reference 构建并消耗了同进程命中结果。不能把旧205.448秒全部归因于删除的冗余，也不能据两个不同上下文的单次耗时宣受控加速倍数。

## 10. 实际规则读取

原科学 public actual pull：**00:29:02.474925–00:29:05.021925 UTC**，从 a0d71ea94446f0fcf64d1f69e4dbadd5910204ba 到 **cdb90b6a2014fd6842c6755cc17e3c219476ddec**；README 两份均与 expected blob 相同、差异空、returncode0/passedtrue。stdout 1,219 B，SHA256 00a231fda5240580d2ecfec6a50146a5d974d8011199192a18fceb1dd5ff3e5f。

原科学 private actual pull：**00:29:07.372033–00:29:08.176405 UTC**，before=after **c0c9529bd4681191261676e0abeace5ea4aab1be**；root README 同、topic README 不存在、QUEUE 本 session 唯一 ongoing。没有公开私有正文。

第三 observer public actual pull：**00:54:53.975613–00:54:54.251593 UTC**，before=after **bf89891c487f143317ade7f6b99f665b7b997957**；两 README 空差/通过。stdout123B，SHA256 fc0f5ea785e047df1e820cd24f9a4076d4d78b38b350de2a4755a2b89b9557ad。

第三 observer private actual pull：**00:54:56.925505–00:54:58.211034 UTC**，从 d662054fedf7dd39d0163d63f4ec78541055a819 到 **0cec35dcb8df7d19dc67ceb045ed7cfb471a7af1**；root同、topic不存在、QUEUE唯一ongoing。

公共根 README blob **21bd547f56590b7f2dd279d0297efb289a9b2783**，topic README blob **d0432faff569c8e9af7ed4809847e12880976c11**；私有根 blob **5ba164843b1f5802184178a82d786264404873a3**。这些是实际 pull/read 收据，不以读旧 source 替代。

## 11. 下一项具体问题：把已付末方向变成更有效的模型支持

不再原样增加64次预算重跑同阶段。当前新证据足以提出一个可独立审查的机制问题：**末次没有正的完整修复候选、没有物理 trial，且只剩一个 SOC 预留名额时，是否允许把这个名额用于一次带新支持的 primary？**

该规则若实施，必须保留以下界限：

1. 来源是完整已付 MODEL28 的一个实际方向及四个全网 attainer。它们给出新的单位球法向选择信息；未知旧步不能编造。
2. 所有512旧 bank支持和4条已有补充支持仍保留。新增法向即使对应同一 row，也不能覆盖删除原支持；必须在真实同 center / grid / epsilon / row / $e,f,de,df$ / guard / trust 下形成合法切面。
3. 若只使用本任务未用第64名额，就是一次有明确代价的 allocation 改动：之后没有SOC额度。必须公开这一机会损失，实际失败保留最后接受点，不免费重解、不递归加预算。
4. 若需新独立任务或不同 norm-cone 求解机制，必须另列新任务的算法差异和资源，完整保留本任务63次LP与257.595秒以及祖先费用，不改名抹账。
5. 新候选仍经过原完整仿射修复、原真实两网14门、原严格metric下降和全部fallback。新切面并不保证下一步改善，也不把原停止改写成驻点。

另一可研究的方向是直接解决完整范数锥或保留每个行的多条支持以减少反复松弛缺口。但当前没有证据证明bank淘汰、单行法向替换或经验guard就是末次停因；这些只能作为新方法待付的具体假设。本文截至本次实际结果，不包含新的科学执行或策略效果声明。
