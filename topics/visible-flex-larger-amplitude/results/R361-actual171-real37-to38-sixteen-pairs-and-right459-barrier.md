# R361：实际 171 同 job 重生 37 查询八对、续做 38 查询八对，以及新 RIGHT-RMS459 障碍

日期：2026-11-15。本文只读取公开 Actions 的原 JSON、原字段与原字节身份；未在本地重算模型、范数、FD、QP 或科学数组。结论中的“接受”均指原暖步引擎的一次真实试步接受，不能替代完整非线性 native／full-DN 接受。

## 361.1 实际结论与范围

实际 171 完整执行了 **8 对原 37 查询 model+FD，然后从同 job 的真实末 pair 继续 8 对新 38 查询 model+FD**。16 个模型各接受一步、16 次 fresh FD 全部通过原实现检查；共访问 80 个原试步，其中 16 接受、64 拒绝。没有未执行的整对 model+FD 后缀。

停止原因为 `explicit_maximum_two_phase_batch_count`，即两阶段各 8 对的明确预算耗尽。原总 elapsed（含来源与输入恢复）为 `13364.315132717` 秒，原进程退出码为 0。最终仍明确：

- `success=false`；
- `new_coupled_finite_acceptance=false`；
- `nonlinear_native_or_full_DN_called=false`；
- 完整当前高度的非线性 native、full-DN、全闭曲面几何证书均未由本运行支付。

新增的 LEFT-RMS462 确实进入完整 38 查询模型。扩展第一对接受全步，但后段步长缩至 \(1/8192\)。最后六对的最近拒绝均出现 **唯一原 RIGHT-RMS459 域失败**；这些最近拒绝的 38 个选点、全角线性 reserve、node/midpoint/边界和原 \(\rho\) 守卫均通过。这是具体的新遗漏查询证据，不是舍入底线、局部极小、无解或 QP 最优的证明。

扩展第二对及随后若干较大试步仍会在已选 LEFT-RMS462 上出现真实非线性域失败。把一个站点加入线性约束没有证明该站点在任意有限步上自动合法；新增查询与非线性曲率责任必须分开。

## 361.2 公开运行、运输与源码身份

| 项目 | 实际身份 |
|---|---|
| run | [43739787509](https://github.com/Rogerhu12/math-research-public/actions/runs/43739787509)，attempt 1 |
| source commit | `298c7dbebc28b5fa94bea030b4efe1426b21bf67` |
| compute job | `132890174922`；全部步骤 success |
| 创建 / 终态 | `2026-11-15T17:12:21Z` / `2026-11-15T20:55:39Z` |
| workflow | `.github/workflows/visible-larger-public-thirty-eight-same-job-batches.yml` |
| request SHA-256 | `06d3b8c9f207ebcc9ee58cce3e78f59d48b689a193822569bf8e697034d8b748` |
| 原编排源 | `geometry_20261115_thirty_eight_same_job_batches.py` |
| 编排源 SHA-256 | `2564be712a79aae29b5c2ce99518a8508e10f581e8a204a2162aec7b20859866` |
| 原薄读者 SHA-256 | `32c2bca1cb068143dd01d99ef0eced97550fd24331a49684b66c7dad2743b80d` |
| 原 37 配方 | `public-thirty-seven-model-recipe.json`，27,755 B |
| 原 37 配方 SHA-256 | `f8a382475b48cd322b4f44c6a34047fe0552b14ee38832c99924edd08c5156ea` |
| 官方 job-log HTTP 响应 | 11,515,407 B |
| 该 HTTP 原字节 SHA-256 | `49c540d87bfe89284c338fff687c663ca70274e9034dc39f43f3b7b6aba272e1` |

两次 connector 日志调用均以 transport closed 结束，没有取得可冒充完整日志的正文。随后主控唯一一次通过官方 job logs endpoint 完整取件；302 后不携带原认证 header。本表日志身份是 **GitHub HTTP 原响应字节**，不是 connector 解码字符串再序列化的身份。

实际 `request171_source_bytes_checked` 记录：91 个保留来源、5 个新增 query/readout 源、1 个独立编排器，共 **97 个显式源码**；原科学门与原原子预算没有变化。源码、请求及配方可从上述固定 commit 逐字重取，不能以主分支后来修改的同名文件替代。

日志共 1,921 个物理行。解析视图仅在原行首剥离单个 BOM，再剥除锚定时间戳；原字节保持不动。行首 BOM 位置为 1、829、1310、1563、1670、1781。原 JSON 候选行没有解析失败。

历史完整 JSON 传输共 72 个 container、1,201 个 member、19 个结束记录。已内部完整重建 16 个 batch summary、37→38 handoff、清理前 chain end、清理后 surviving readback；每个 member/container/document 的原 canonical JSON+LF 长度与 SHA 全部吻合。该内部重建没有把原大科学表重新发布、拆传或变成新的科学检查门。

16 个 standalone 原 trials 与各自 driver status 的第 0 个 iteration 内完整 trials 逐原 JSON 值相等；原报告列出的 accepted、before、damping、固定权重 merit、iteration、direction metadata 和 trials 对照也均为 present/equal。这里的层级是 `complete_original_status_iteration_trial_JSON_records[0].trials`，不是把外层 iteration 容器当成原 trials 列表。

## 361.3 真父输入和同 job 37→38 交接

本次从仍可恢复的 **actual98 原 artifact** 重新开始轨迹，并非从已删的 actual155 末 warm SHA 伪造续接。

- actual98 run `43677587785`，artifact `14147700690`；
- artifact 名 `visible-followup-condensedqp-43677587785-1`；
- 完整 ZIP 809,042,943 B，SHA-256 `9917774d965e86b0a8d46677a1f54c0fb23fc8fa61a67cbab998e7493d33151a`；
- 原 warm：4,927,052 B，`b59f40c003bf924f3f3c10aa6783425a606b3e395fd86311cbba159b835feb67`；
- 原 status：3,379,453 B，`b7ad389fad867fecf85edc4313145980d6e8686f207acf781ff6a050e7eae6ff`。

原 ZIP 的完整 size/SHA 已由 Actions 检查；选中两成员的 CRC 已检查，原 JSON 未重序列化。其余成员未解压审计，不能把完整 ZIP SHA 写成全部成员内容审计。

四原数学输入由原历史 commit `918fdb11dbb7a424b6149b405e2c7fab3cc0c737` 恢复：

| 输入 | 原 bytes | SHA-256 |
|---|---:|---|
| accepted.json.gz | 2,614,352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared.json.gz | 4,220,043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail-anchor.json.gz | 6,815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail-config.json | 2,161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

前 8 对实际产生、后 8 对实际接收的同一 pair 为：

| 原 37 末对象 | bytes | SHA-256 |
|---|---:|---|
| warm | 5,035,122 | `1c659b97dbfeb5b34ea53049a74c9c6b406c497671fe529472dfce4991c25920` |
| status | 4,993,388 | `e01047eb25c6f70fac1c7fdef6aa554649765c1de8801776d9c377ba9cea85dd` |

原交接位置为 `parent-after-007`。warm/status 保留原 37 producer schema 与原文件字节；38 入口用实际 CLI expected SHA 接入，未改名冒充新 producer 或重序列化。handoff 当时的 `new38_model_not_yet_executed=true` 是交接时刻记录，不能误读为最终 38 模型未运行。

## 361.4 新 38 查询的真实范围

新增唯一查询为 LEFT-RMS462，fraction 原词 `0.17267316464601146`。它的 capture interval 和原 node462 支撑同时进入新模型，未只改查询标签。

完整集合为 22 个 LEFT 加 16 个 MID：

- LEFT：462、463、464、465、466、467、468、469、470、471、472、473、475、477、479、480、481、482、484、485、486、487；
- MID：471、472、473、475、477、479、480、481、482、483、484、485、486、487、489、490；fraction 为 0.5。

每个 query 保全部 2,048 个角，合计 **77,824 行**。实际 38 模型有 25 个独立 capture interval、30 个 endpoint，局部完整 B 支撑为 10,143 坐标；原 C 为 4,059 坐标，完整原外变量空间 236,036 坐标不变。最后 condensation 原记录为：retained physical node 462 至 491，30 个保留节点，698 个 physical nodes、3 个 scalar controls；外部变量没有冻结为零，完整 affine 列保留，没有形成 normal Schur matrix。

两 RMS fractions 仍对全部 698 interval 检查。RIGHT fraction 原词为 `0.8273268353539885`，所以 RIGHT459 虽未被选入 B，仍由原完整域检查实际拦截。原 rho 守卫保 4,096 角。

## 361.5 全部 16 对实际接受与 FD

每行 \(W_0,W_1\) 只对应这一行同一 fresh 模型的原固定权重 merit。不同模型重算了权重；不得把邻行数值相减当成同一固定目标的下降。

| batch | query | 已访问档数 | 原接受 \(\alpha\) | 同模型 \(W_0\) | 同模型 \(W_1\) | 原四阶 FD 最大相对误差 |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 37 | 4 | 1/8 | 43.36300372909822 | 43.33605694766007 | 8.7019221818232e-10 |
| 1 | 37 | 3 | 1/4 | 43.33456976744222 | 43.28585055875668 | 8.917585068991029e-10 |
| 2 | 37 | 4 | 1/8 | 43.28057984612335 | 43.259491029560984 | 9.99269334313201e-10 |
| 3 | 37 | 3 | 1/4 | 43.25889304148275 | 43.225388792823836 | 7.222736018938388e-10 |
| 4 | 37 | 3 | 1/4 | 43.22259857065184 | 43.19404702991091 | 7.070690710851065e-10 |
| 5 | 37 | 1 | 1 | 43.19145189347684 | 43.10940853870894 | 8.062709920950109e-10 |
| 6 | 37 | 3 | 1/4 | 43.10029022914125 | 43.0900111872662 | 1.0465268241594862e-09 |
| 7 | 37 | 2 | 1/2 | 43.08872613662628 | 43.06902479892305 | 7.11083854306579e-10 |
| 8 | 38 | 1 | 1 | 43.066102829129136 | 43.033000210523696 | 9.45263793035459e-10 |
| 9 | 38 | 2 | 1/2 | 43.0285778976809 | 43.01540124072149 | 8.299931257021095e-10 |
| 10 | 38 | 4 | 1/8 | 43.013378786843774 | 43.010054421660115 | 9.9704115005166e-10 |
| 11 | 38 | 5 | 1/16 | 43.00959628066999 | 43.00799368215984 | 9.977949607093397e-10 |
| 12 | 38 | 6 | 1/32 | 43.00776777975824 | 43.0069763791501 | 1.0747208828315966e-09 |
| 13 | 38 | 12 | 1/2048 | 43.0068623352288 | 43.00685005982653 | 9.788767831904815e-10 |
| 14 | 38 | 13 | 1/4096 | 43.00684832108198 | 43.006842184700886 | 9.841481779938845e-10 |
| 15 | 38 | 14 | 1/8192 | 43.00684131538674 | 43.00683824752586 | 9.643303646665e-10 |

原 17 档策略未增加或删减；每批从 \(\alpha=1\) 依次减半，首次接受后停止该批回溯。因此表中第 \(n\) 个访问是该批接受档，其后原 17 档中的更小步未执行，不应列为失败。前阶段共 23 档、后阶段共 57 档，合计 80 档。

每个接受档均有：node/midpoint 失败数 0、boundary finite、原 \(\rho\) guard valid；两 fractions 的 698 点 RMS invalid_count 均为 0；全部 selected negative-angle counts 为 0。全部 16 个 FD 的 `implementation_check_passed` 和 `second_order_truncation_contracts` 为 true，沿用原阈值 `5e-05`。FD 记录明确 fresh 当前 warm boundary FD 实际重算、复用的是本模型已完成的当前 nonlinear J；旧 FD/旧 warm SHA 未重标，未使用 ready linear graph。这不是完整 nonlinear tail DN 的验证。

末次 FD 二阶最大误差为 `9.883381933103533e-06`，四阶为 `9.643303646665e-10`；左右边界 Jacobian off-block 原最大值为 0，右行只依赖右 endpoint 的原标志为 true。

## 361.6 最近拒绝及整个后段回溯定位

最近拒绝的原 scope 如下；“唯一”只用于确实完整返回且原 invalid_count 为 1 的那一档。

| batch | 最近拒绝 \(\alpha\) | 原失败位置／范围 |
|---:|---:|---|
| 0 | 1/4 | midpoint471，原 RHS 非有限；selected LEFT464 与 MID471 亦有负角 |
| 1 | 1/2 | LEFT-RMS463 |
| 2 | 1/4 | LEFT-RMS463 |
| 3 | 1/2 | LEFT-RMS463 |
| 4 | 1/2 | LEFT-RMS463、464 |
| 5 | 无 | 第一档全步接受 |
| 6 | 1/2 | 唯一 LEFT-RMS462，37 选点均过 |
| 7 | 1 | 唯一 LEFT-RMS462，37 选点均过 |
| 8 | 无 | 新 38 第一档全步接受 |
| 9 | 1 | LEFT-RMS462 与 RIGHT-RMS459；selected LEFT462 有 4 负角 |
| 10 | 1/4 | 唯一 RIGHT-RMS459，38 选点均过 |
| 11 | 1/8 | 唯一 RIGHT-RMS459，38 选点均过 |
| 12 | 1/16 | 唯一 RIGHT-RMS459，38 选点均过 |
| 13 | 1/1024 | 唯一 RIGHT-RMS459，38 选点均过 |
| 14 | 1/2048 | 唯一 RIGHT-RMS459，38 选点均过 |
| 15 | 1/4096 | 唯一 RIGHT-RMS459，38 选点均过 |

后 8 批的全部已访问拒绝档可精确压缩为：

- batch9：\(j=0\) 同时 LEFT462/RIGHT459，\(j=1\) 接受；
- batch10：\(j=0,1\) 同时 LEFT462/RIGHT459，\(j=2\) 唯一 RIGHT459，\(j=3\) 接受；
- batch11、12：\(j=0\) LEFT462，随后直到接受前均唯一 RIGHT459；
- batch13、14、15：\(j=0\) LEFT462；分别 \(j=1\ldots10\)、\(1\ldots11\)、\(1\ldots12\) 均唯一 RIGHT459；下一档接受。

这里 \(\alpha=2^{-j}\)。这些后 8 批的 node/midpoint 原失败数均为 0，没有 boundary_domain_error；每个需要 RMS 的档均实际返回完整 RMS 检查。LEFT462 的负角并未被新线性约束“自动消灭”；在较小步处它已通过，而 RIGHT459 成为剩余完整域障碍。

最后三批最近拒绝的原 RIGHT459 数值为：

| batch | 最近拒绝 \(\alpha\) | minimum_beta_squared | 原最坏 \(\phi\) | 同档实际 merit reduction |
|---:|---:|---:|---:|---:|
| 13 | 1/1024 | -0.0020223275688027176 | 0.04908738521234052 | 2.4550640780773847e-05 |
| 14 | 1/2048 | -0.0020255659542920412 | 3.0925052683774528 | 1.2272721555461885e-05 |
| 15 | 1/4096 | -0.0020263760509493522 | 3.0925052683774528 | 6.135711309696035e-06 |

三个记录的 interval 均为 459，station 原词 `1.133688412478548`，left `1.129564641993276`，right `1.134549093493036`。原 scalar \(a,a_s,a_{ss}\) 分别为 `1.1943691436311463`、`0.017113226546956496`、`-2.499633895039872`。以上均为原已存浮点词，不是新严格区间证明。

末次最近拒绝 \(\alpha=1/4096\) 的完整 selected linear reserve：77,824 个有限值、负数与零均为 0，原最小值 `0.0005835110332270376`；selected linear beta² 原最小值 `0.0011670363660588289`。38 个实际 selected beta² 检查的 negative/nonfinite counts 均为 0。其原实际与预测下降比 `0.99999880632341`，所以拒绝不能写成这一步 merit 未下降或模型线性 reserve 不可行。

末次接受 \(\alpha=1/8192\) 的实际下降为 `3.0678608737844115e-06`，原预测下降为 `3.0678626109085915e-06`，比值 `0.9999994337672835`。末接受态最大 physical collocation 残差为 `0.007101312274733623`，位于 **interval461／原 residual row155819**，signed value 为其负值。这个最大残差位置与导致拒绝的 RIGHT459 是不同对象，不应合并成一个障碍。

## 361.7 完整模型与 QP 的已付、未付

全部 16 个最终候选标记为 `R270-condensed-complete-H`；原完整 \(A,A^T,B,B^T\) readback 已 fresh 求得，required direction fields finite、全部 original linear rows feasible。完整 B 支撑和外部坐标未删减；原 C 候选保留为对照。

末模型 damping 原值为 270.0。末 QP 原读数：

- full-model objective：`42.98947832591546`；
- 原实际 damped model decrease：`0.017362989471331768`；
- 原 \(\langle g,z\rangle\)：`-0.025131957493246503`；
- 完整线性 slack 最小值：`1.4710455076283324e-15`，77,824 行均 finite、负数与零计数为 0；
- 原 stationarity \(L^2\)：`25267.361840614423`；
- 原 R267 lower-bound raw float：`-4335.883919837897`；
- complementarity sum：`0.0011458693133393138`；
- 末 local dual 原因：`maximum-dual-sweeps`，已做 200 sweeps。

原报告始终保留 `full_QP_optimality_claimed=false`、浮点 posterior 非严格包围、全局 selector 改变后不声称条件最优。暖步接受及 FD 通过不能升级为 QP 全局最优、连续场误差界或物理 full-DN 成功。

末接受态完整 boundary max 为 `1.0032937225271052e-13`、left residual max 与 constant collocation max 为 0；这些局部原读数没有抵销上述 physical collocation 残差，更没有支付 nonlinear native/full-DN。

## 361.8 真实末对象、完整读回和实际清理

实际最后 warm/status：

| 对象 | bytes | SHA-256 |
|---|---:|---|
| warm-001.json.gz | 5,140,000 | `41698322cdbce8a95144e1d5f0d8782d1a9321cccfbcf8bf1c75208e7ea5ddc1` |
| driver-status.json | 8,427,530 | `3e0034a64382dab8d8d04d50a8689c7068174d35d6c5a8dfe3b516e198c8c79f` |
| model-000.json | 1,920,961 | `fdff7efcd7bb80c20f963e61565f42dfa3729aec8abeb454ff580e7bee3ca0a9` |
| response-check.json | 6,394,133 | `7afe7557082cbe010fb45651ab3646618e0290e6af7b99639a5dfca7a6e3e65c` |
| condensed-QP-summary.json | 129,731 | `db224f75c62b1f678b50f310a8485777f71ef02dd1b11778b10fe1c90516f2fc` |

这些是原 Actions 报告的原文件身份；本次读者没有再下载这些 raw，也未独立把已删原文件重新做 SHA。完整语义传输已验证的是原汇总中的所有字段和该传输本身的 canonical 身份。

末 batch 完整语义 JSON 的 canonical JSON+LF 为 1,884,347 B，SHA `16ea57221ae0ab4f3d67461d258d0f6ff64ff72eac0cdb0e44561d9908c61d29`；清理前 chain-end 为 11,857 B，SHA `1e24c0a8dcfa9cb3ab0dd1425f3baa5cb09702eaa58149873277629c2bfed058`。这两个身份不能混同 driver-status 原文件身份。

原事件有 32 条 `original_child_finished`、16 条 batch identity、16 条完整 summary stream index、16 条 payload retired；原 model/FD exit code 均为 0。末 chain-end 实际记录 `all_owned_temporary_payload_removed=true`。always surviving readback 的 `recovered=[]`、`errors=[]`，并明确“无 surviving batch 不推断科学成功”。末规则 namespace `visible-thirty-eight-171-rules` 的删除事件记录 `complete_readback_preceded_cleanup=true`；5 次规则同步事件正常记录。

原 raw/artifact、Release 和 Git 数据上传计数均为 0。临时 warm/J/factor/数组已清理；上述末 hash 不是可继续求解的文件。Actions 的短期 Git 对象缓存不由此 wrapper 擦除，也不能冒原 scientific raw checkpoint。

## 361.9 有证据的下一步与不可外推事项

这次运行支持一个具体后继：在原 38 全范围之外，增加真实 **RIGHT-RMS459** 的完整角线性约束和实际 endpoint/capture 支撑，保原完整域检查、17 档、固定权重 merit、全外变量、fresh 模型及 FD。它应独立声明 RIGHT fraction 与新的支撑范围，不能把它重标为 LEFT 或仅在查询表补一行。

实际 171 末 raw 已删除。后继若要从相同末场继续，必须在同一个公开 Actions 作业中按原来源重生本次两阶段并保留真实末 pair，再接新 query；也可以明确从 actual98 原父另起新轨迹，但不能称它为本次末场续接。这个选择是可执行来源协议，不是要求额外数学验收。

新增 LEFT462 后曾接受全步，只能作为实际观察；没有同点对照足以证明所有改进唯一来自该 query。RIGHT459 原失败也没有证明未来加入它会消除已选站点的非线性曲率问题，或使更大步可行。R334/R354/R398 的准确模型／闭段责任仍分别存在；本次没有用诊断代替原求解门。

本结论记录的是有真实进展、真实新域障碍的 16 对有限暖步实验。整体课题的完整非零场、native/full-DN、最终响应及几何证书目标仍未完成。
