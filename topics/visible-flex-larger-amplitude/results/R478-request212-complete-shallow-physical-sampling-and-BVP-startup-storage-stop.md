# R478 — request212 的完整浅逆采样、BVP 启动磁盘停止与必要读回边界

- **可信度：实算记录与实际必要读回；仅限下述 run、原文件和已返回范围。**
- 公开 source：`9a9dbfa80ddf2c68d2dfda8e2b8c8a93d7e82060`。
- [官方 run 43810550597](https://github.com/Rogerhu12/math-research-public/actions/runs/43810550597)，attempt 1，2026-11-16 05:29:19Z 启动。
- [compute job 133111042532](https://github.com/Rogerhu12/math-research-public/actions/runs/43810550597/job/133111042532) 与 [report job 133152030600](https://github.com/Rogerhu12/math-research-public/actions/runs/43810550597/job/133152030600) 均已真实 completed / failure。
- 本文只读这两份终态官方日志及其中原 JSON；没有重跑积分、RHS、矩阵、区间包围、原求解或其他科学计算。完整日志各取一次，未读取运行中日志。

## 478.1 直接结论

本次独立实验把原物理点逆像工作的 `sample_inverse_depth` 从24明确改为2，保留原32bit工作目标、全部物理点计划、完整C/root族、全部112 far频率及原BVP/末门。真实采样现在返回：

| 原字段 | 本次实际值 |
| --- | ---: |
| `completed` | true |
| `native_geometry_ready` | true |
| `complete_unique_sample_points` / `actual_point_count` | 13850 |
| `complete_native_field_occurrences` | 16128 |
| `actual_inverse_range_count` / sampling工作单元 | 65102 |
| `actual_coarse_valid_point_leaves` | 15123 |
| `complete_necessary_unpaid` | 空列表 |
| `unpaid_inverse_leaves` | 空列表 |
| `numerical_sample_work_resolution_complete` | false |
| `error` | null |

这支付了本次完整有限native几何输入的生成，且明确没有把工作目标未满足改写为数学失败。全部112有限far传播、全部候选单位Robin行、112个joint nominal代表行及四个原native数组也都完成。

candidate binding 随后真实形成当前native配置、完整十参BVP配方及同一绝对deadline。**真正453/450求解仍未启动。** 原227ef601 launcher在启动子进程前记录：

```json
{
  "kind": "insufficient-startup-free-storage",
  "actual_free": 11761553408,
  "declared_required": 34359738368,
  "scientific_process_not_started": true
}
```

因此本次首个未付BVP责任是原声明32GiB启动存储要求；不是逆像工作计数停止、不是墙钟耗尽、不是原native trial拒绝，也不是准确C或BVP无解。步骤19的exit124是该launcher的实际资源返回，不能只据数字称超时。

另有一个独立读回问题：原规则/资源必要摘要形成94138B，超过90000B运输上限，步骤25返回70且没有输出该摘要正文。该步骤后半的212 composition readback因shell的 `-e` 未执行。最终清理程序如实跳过删除；不能把步骤26的success标签说成raw已清，不能把本次说成八份必要范围全已返回。已返回的五份主摘要及closed metadata均完整解析，明确保留这一缺口。

## 478.2 公开来源、日志与必要摘要身份

完整原日志包括原逐行时间戳和BOM。解析只在每物理行去掉一个行首BOM及原时间戳；下表原SHA未做此规范化。

| job | 原日志字节 | SHA256 | 物理行数，含末空行 |
| --- | ---: | --- | ---: |
| compute133111042532 | 614288 | `94841c2226c8a654a71e1f33f01bb62fa5c79b067b2976b6dedf56b11b37fa63` | 2290 |
| report133152030600 | 343336 | `bc30aafaeb4a1ec5eabd2b62082fcf86b726d22d8c378295b2b9ebbc85a5c91d` | 122 |

compute原日志从05:29:22.4143501Z开始，末系统警告时间07:24:02.1035423Z；report从07:24:07.3870492Z开始，最后清理消息07:24:07.9430118Z。compute中12个实际BEGIN/END JSON文档全部可解析；report重印五主摘要，其正文与compute对应正文逐字相同。脚本回显里的marker字面不算实际输出。

下表按原reader/step output的实际字节口径。**C主摘要无末LF；另五项含一个末LF。** 没有把两种口径混用。

| 必要scope | 实际字节口径 | 字节 | SHA256 |
| --- | --- | ---: | --- |
| C完整主摘要 | 无末LF | 37550 | `45b12518f49538ce5b7f3b3e0c53182677fb2b31b675deb548776b806de5a6b1` |
| 原cut完整2jet | 含末LF | 5831 | `7c74328ef9568d04d420799caf1d2e23aca0332b4cc7d8c58e89a40e2b2e05c4` |
| 原deep112必要 | 含末LF | 7327 | `d54fbe210a912adce8feeffebd83cb26454e9e3ddcbb01384af27334d074c67e` |
| 新准确十参构造/绑定 | 含末LF | 53171 | `715aa3f054eca99f8d66cc593e0bf188e0dee6e73be683e1dd2096101c174d8f` |
| sampler与双BVP必要 | 含末LF | 62064 | `b2f7da5f89ff2ead64b0d348b99a0032b2db85e978073de7de08ccf3d788ffa5` |
| closed/held与其独立规则scope | 含末LF | 18870 | `170c879dbad51422bf0413904cc13424e327c4c44dca397f0be278c3bc02a8e2` |

未返回的两份责任：

1. 原规则资源scope实际拟输出94138B / `1731dc1b2284441db6402a6176471deb38b2603a4b78dca58baf2bcb3009c416`。原事件明确 `no_part_transport=true`、`no_cleanup_marker=true`。这里只取得身份和超限事件，未取得其94138B正文，不据SHA补填原规则文档。
2. 212组合的prepare/verify事件已返回同一receipt身份，但步骤25里的最后readback未执行，没有 `BEGIN_REQUEST212_SOURCE_COMPOSITION_NECESSARY` 或其readback-complete marker。源组成实际初始化与终态必要读回是不同责任。

report原 `request205_report_transport_scope.errors=[]`；它因compute/BVP的实际failure继续exit2，没有把运输成功变成科学成功。report只给closed summary身份及outcome，closed完整正文位于compute。真正R452 postsolve/held未启动，故没有伪造这两项科学正文；其not-started原因由上述closed metadata完整返回。

## 478.3 本次212的组成、字词与不变范围

实际入口为：

- [212工作流](https://github.com/Rogerhu12/math-research-public/blob/9a9dbfa80ddf2c68d2dfda8e2b8c8a93d7e82060/.github/workflows/visible-current-C-actual202-shallow-inverse-closed212.yml)：99644B / `d1022e74a6217d582f08692b2458bb4d20a3a5dec61ba4dc88907a27e13c3cc0`。
- [212独立outer request](../notes/current-C-actual202-shallow-inverse-closed212-request.json)：9965B / `8803750dbb21bcc24e0809e7bdc4389c567de9b8a10532d52b42b2f7a7ee30bf`。
- 原205完整合同：97406B / `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`。
- 实际派生dispatch：89076B / `62c21e3c6fbbe8e17f4016e527d125bcd9f1cf84eda434b2a7afbbc883c4c4c7`。
- 实际 `request212-composition.json`：6355B / `b2cd1d0dadfadaab85c8c40183ee8bc9627924bda6d09e586d6ea5efd06585ff`。

两个原事件 `request212_explicit_sampling_work_composition_prepare` 与 `...verify` 都明确：

- 原深度24，本次深度2；
- 原205其余科学成员保持；必要reader的显式新身份属于声明的来源差异；
- 原154个来源加3个明确元数据/读回来源，实际157；
- 当前run/source均是212现场；
- 未继承旧run结果或旧accepted parent。

计算步骤8实际绑定157个来源；Actions中的文本/语法预检记录23个bash块和22个Python heredoc身份，且该预检没有导入或执行科学源。本文没有在本地重复AST、编译或科学试跑。

物理采样实际源仍为 [原32b0 sampler](../computations/geometry_20261115_current_C_pruefer_joint_radial_sampling.py)，69702B / `32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4`；变更的是显式逆像工作深度，不是删除节点或更换C族。32bit值目标、1000000点逆像工作单元上限、完整112、steps=12及全部原数学门保持。

本次真正调用的必要reader为：

| 用途 | 文件 | SHA256 |
| --- | --- | --- |
| 新完整point/stack基础reader | `root_20261116_current_C_sampling_scope_necessary_readout.py` | `47d7ec771331f417dffb783a79e02d1ae9720e9ad0a699a72c37cf3031718cb2` |
| actual202双phase外层reader | `root_20261116_actual202_sampling_scope_two_phase_necessary_readout.py` | `6e40dc6365246113d8abc07110582a030b4930195070a71ba08e9872a11bb1e7` |

实际BVP必要schema为 `actual202-complete-sampling-scope-ten-two-phase-necessary-readback-v1`，实际frame为 `BEGIN_ACTUAL202_COMPLETE_SAMPLING_SCOPE_TEN_TWO_PHASE_NECESSARY`。本次全部点完成，故未付列表实际为空；这不是把旧reader缺少的point/radius/stack字段自动填零，也没有从203/205/209未完采样填入本次值。

原205内部schema、namespace、candidate的 `actual_request_number=205` 与deadline名称是被显式复用的程序合同。它们绑定的run/source/派生request SHA在这次都是真212；不能把这些内部字面改写为旧205实绩。

## 478.4 原输入、准确C、六primitive与cut二阶jet

原五输入从公开历史 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复并逐字核对：

| 原输入 | 字节 | SHA256 |
| --- | ---: | --- |
| calibration ledger-ready | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| tail-config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| stored-ready | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |
| accepted.json.gz | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| complete-seed453.json.gz | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |

原完整seed确为699节点、453状态，原producer `9a1ae018d71e38ff901c4b9156b23502a4efde44f812c1ff4e03323878b659db`，原seed的 `success=false`。它只作为计划中的初猜；旧RHS、metric、tail、接受状态均未继承，本次也未实际进入重映射/RHS求解。

C源仍为f12f完整v3，实际参数为：

```json
{
  "analytic_guard_bits": 8,
  "budget_seconds": 3600,
  "deep_definition": "original-exact-root-family",
  "integral_absolute_bits": 96,
  "integral_evaluation_limit": 100000,
  "integral_relative_bits": 80,
  "max_depth": 48,
  "max_panels": 200000,
  "max_query_nodes": 200000,
  "precision_bits": 256,
  "query_depth": 12,
  "value_width_bits": 24
}
```

原C实绩：

- 160原cell、1440原piece全部完成；
- 六primitive `A,B,sqrtE_A,sqrtE_B,w_A,w_B` 均保完整深端及有限头；
- 121832 integral panels，307101 rigorous analytic component integrals；
- 200000 inverse-cover nodes；
- 两条原query均给出完整合法闭域包围；
- `elapsed_seconds=1880.2217261719998`，`error=null`；
- 未访source/query suffix均null；完整原root族统一包含，未选择准确深root。

有限头诊断的 `coarse_valid_panels_at_maximum_depth=3` 与whole-query的2609条工作未决是不同层级；不能相加或互换为同一失败计数。所有307101实际analytic component均finite、fallback=0；callback资源stop为0，最后真实panel的六个工作目标都已恢复通过。全部这些是原诊断，不构造唯一数值因果解释。

两query的实际范围：

| query | 合法闭域完成 | 工作分辨率 | 原leaf span | 原refined_nodes |
| --- | --- | --- | --- | ---: |
| 原binary cut点 | true | true | [0,1) | 5 |
| 原完整自然径向域 | true | false | [1,108625) | 93979 |

whole-query原停止文为 `Declared inverse-cover node resource budget reached`，保2609个有效coarse片段；`complete_unpaid_scope`只含2609个 `query-resolution` 原行，无未访source或query后缀。首条原工作未决是source_piece1400、original_cell4、segment5、闭参数区间 `[54365/65536,108731/131072]`，inverse_refinement_depth8，`entire_possible_inverse_fragment_included=true`。这不是丢失准确域或把C包围判为错误。

原C完整临时result为32114B / `2d0b1c47cdb960f880e196672f27651db34ee2c32f1c5f2bd5c5e04535b8746a`，input binding为25648B / `9a399e28c321807bf7b6e3989e289e216b52ab92bd919cc3303f9a79d1b9cbc5`。完整原账身份：

| 原账 | 行数 | 字节 | SHA256 |
| --- | ---: | ---: | --- |
| six-primitive-panels | 108628 | 2079629833 | `30336b8ac29623428e33182f88745124d70b2e3d7f510b403ccedea4d17ce873` |
| complete-source-radial-panels | 14644 | 25513827 | `da2ba4cb44ad3276b147cff40fe978de9a40966780586a7efb62fc986d853a59` |
| query-closed-inverse-cover | 108625 | 197572200 | `98188fa682e374923673639b3a57a2d9bc436cc29b96537677313b7385cf443d` |
| unpaid-complete-scope | 2609 | 5209016 | `9964a6e6c2c9d16badaac70709c5fd428bca21a5bae0466df5360f40fe2f6a3a` |

这里保已返回身份和范围，没有把这些大账正文下载或转成Git内容。

原cut仍为字词 `333333333333d33f`，准确有理值 $5404319552844595/18014398509481984$。cut reader完整读取唯一head叶，span[0,1)，没有新增导数宽度门。原三个闭盒如下，数值写作“整数乘二幂”；没有取中点替代准确C：

| 量 | lower | upper | exact full width |
| --- | --- | --- | --- |
| $E$ | $297036851754023534385\,2^{-68}$ | $297036860731551973169\,2^{-68}$ | $8977528438784\,2^{-68}$ |
| $E_r$ | $-1377364570695686333\,2^{-62}$ | $-1377334639942752445\,2^{-62}$ | $29930752933888\,2^{-62}$ |
| $E_{rr}$ | $-18506607869532518095\,2^{-57}$ | $3541147354781501745\,2^{-57}$ | $22047755224314019840\,2^{-57}$ |

原自然外半径display为 `[0.30000000000000715908123386 +/- 6.75e-27]`；减原binary cut的display为 `[7.1701834641e-15 +/- 1.01e-26]`。这些只是原包围的显示，完整准确端点在已返回cut摘要中。原完整cut readout为5685B / `f2f30bd5a1b21a970a0bbff4ed602e0edb6c06bbc28be9a811d2ad1e01d75083`。

## 478.5 真实actual202候选与当前准确十参构造

旧180仅真实恢复其原selection所需文件；没有把旧180域证搬成当前actual202候选域证。选中旧recipe字节2136 / `cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb`，旧definition377615 / `f568b81618f1f8b041327be55397293235ad5b3492310e03cb5b4ae75ab7b164`只承担已声明的结构来源。

当前准确候选来自实际202的十条Decimal50原词，按R449明确先投影binary64、再将所得字词解释为新的准确dyadic参数。实际202来源为run43784544723/source1a757004b7ebff1f43563bd57b5d13961648d681，原必要65926B / `ae541e15e47d5fac46dbda02e57d2487d9168ec1811d93d171d1d0989923df2f`。原有限Gauss目标及旧unit接受没有转移到当前C。

本次全部十个投影行的 `original_rational_exactly_represented=false`；精确投影差由原candidate记录返回，没有声称旧十个Decimal50有理数逐字等于binary64。当前准确新点与词为：

| 参数 | 当前准确dyadic | 原binary64 LE字 |
| --- | --- | --- |
| p1 | 338454297525575/1125899906842624 | `70d4d382283dd33f` |
| p2 | 8439592011787243/36028797018963968 | `eb6be9a3c3fbcd3f` |
| p3 | 757556927375085/2251799813685248 | `68376dbcf387d53f` |
| theta1 | -2769125553396035/36028797018963968 | `86b2e59102adb3bf` |
| theta2 | -3637238244232963/288230376151711744 | `069e050b19d889bf` |
| theta3 | 8385926008702661/9007199254740992 | `c586dc8cf4caed3f` |
| eta1 | 4774893172091903/4503599627370496 | `ffeb5c73bdf6f03f` |
| eta2 | 2175078337637993/4503599627370496 | `a4b9b18ee3e8de3f` |
| eta3 | 8832431992147443/9007199254740992 | `f30d65d30c61ef3f` |
| xi | 4670693574119973/4503599627370496 | `25125797f897f03f` |

原candidate保9个结构字段：core_end、cut_radius、kappa、collar_width、first_transition_width、last_transition_width、first_support、root_choice、collar_mode；其模型recipe为3211B / `b02790e6c81082e6c548d9a990a26fd9e88f2ce6d2f18d14e31f4c9251c922a2`。

真正72c factory使用本次C/cut盒，形成准确definition379215B / `5d26b26ac20cadb6df74fa87768a28bb400bedd6e1dcc2d13ae26fc077b043be`，result20079B / `81ce7e86094961fa96d13dff4acb3855889c9a83ec355d81fb5a6eea750a3a1f`。11个原严格构造条件全部true，base域452叶/485节点完整，base耗时0.17589542799987612s。当前全部十参数固定点的域检查：

| 原字段 | 实际值 |
| --- | ---: |
| complete | false |
| elapsed_seconds | 301.421962075 |
| processed_nodes | 29090 |
| passed_leaves | 1810 |
| unresolved_terminal_leaves | 12937 |
| unvisited_stack_entries | 15 |
| all_parameter_values_retained | true |
| closed_coverage_kept | true |

原域账422724564B / `83c05b465a0b8bc3ea8a4fa993a7380f4687fdc671f39cd96c60316c0a3b5f10`，没有在chat逐叶搬运。该域工作未决没有成为新的BVP入口拒绝门，也不能改写为当前准确十族全域通过。

原candidate另有独立coast中心必要诊断：公式 $a_s(1/2)=-\kappa+2L_C\theta_3$，原记录 `every_retained_C_choice_center_refuted=true`、`center_strict_speed_domain_enclosed=false`、`new_acceptance_gate=false`。这是当前起始十点的原诊断，不归因于本次磁盘停止；不推出后继十参数搜索都无解，不将其充作本次未启动的solver拒绝。

## 478.6 完整深端、真实物理far与112代表行

R312深端源fe667不变，全部物理频率 $m=2,4,\ldots,224$ 的112行完成，原root族全含，未选择准确root。深端result5857B / `e5c8534cda5565167f2c7f3220a007325678604fd4506e8cadc9014331c4b52d`；112行494612B / `d68c5547b0323dd2a2bff3fa4087ed5aad831646cabff7c7804519025aa528b9`。该producer自身未做有限头传播，也不宣称cut DN；其原未付列表须和后继真正支付的范围逐项区分。

32b sampler随后真实传播到本次物理far，不采用旧原图或gains：

- far半径字 `f0e68a5235e3a93f`，原binary64值0.05056158669090205；
- 选择规则是严格大于完整node8半径上端点的下一个binary64；
- 原选择来源source_panel10385、source_piece1367、original_cell8、segment8、参数1；
- 最终包含far的候选实际来自source_panel10386、source_piece1368、闭参数末端1/4；
- 本次实际far坐标 $\mu$ 字 `90ab830cf215743c`，原值1.7421589017645275e-17。不能复制209或任何旧run的$\mu$字。

完整112 mode表均返回 `complete=true`、`complete_required_far_propagation=true`、`unit_family_complete=true`。每个mode实际1候选、1单位行、1个required inverse leaf且1个completed leaf；`norm_unproved=0`、`error=null`。所有112均到上述真实最后panel/piece/parameter。原表中coarse=0，range_splits均3685，Taylor/angle-lift/row-norm工作split均0；norm-splits与accepted-panel计数按实际mode分别保留，未把它们替换为统一数字。

全112 joint nominal行状态为 `actual-finite-joint-nominal-row-formed`。每行实际首次precision256就形成，未用到4096 cap；无numeric失败或未启动mode。旧box的Q/Pi中心在112行中均记录exact-zero，但当前新nominal两槽均实际形成，不能把旧盒中心零当真实列零、共振或无解。完整family误差与名义字的差分别保在原行账；代表点不被声明为同一个全局准确C realization。

原必要reader确实逐行解析112 mode、112候选闭管、112逆像leaf与112 numeric selection；全general row及其误差在Actions中完整解析并与代表字核对。reader没有重新计算这些矩阵/误差，chat没有取完整区间大表正文。

本次有限far总工作单元2044754，accepted-panel与commit各1604049行。线性phase真实资源receipt：

| 原字段 | 实际值 |
| --- | ---: |
| actual_elapsed_seconds | 3941.4238297730003 |
| declared_seconds，原owner实际裁剪后 | 11523.894858678183 |
| declared_work_units | 25000000 |
| actual_work_units | 2044754 |
| actual_checks | 4053992 |
| storage_observations | 15836 |
| free_bytes_reserve | 2147483648 |
| phase_finished | true |
| stop | null |

这是phase计时；原绑定/runtime setup明确不包含在该phase时钟中。它没有耗尽25M工作单元，没有发生该phase时间或2GiB存储stop。

## 478.7 depth2的完整物理点计划与新数组

实际grid仍为576 stage、577 node、112mode、spacing2、steps=12、每stage28个原field位置；rawNode是[0,72,144,216,288,360,432,504,576]。node形成规则原样记录为binary64的对数径向插值，两个端点用原准确字。原结果明确所有实际RK4 midpoint/endpoint字均枚举，所有实际舍入field半径均按C域核查，没有把越过名义grid端点的值clip回去。

本次完成13850个唯一半径点、16128次field使用；逆像leaf账实际16917行，其中15123个coarse-valid点叶。coarse是合法覆盖与未达到work-only目标的区分，不能删除完整逆像候选或用它掩盖缺样。两项未付列表均为空。

采样phase原receipt：

| 原字段 | 实际值 |
| --- | ---: |
| actual_elapsed_seconds | 123.74473656800001 |
| declared_seconds，实际裁剪后 | 1440.4868573347728 |
| declared_work_units | 1000000 |
| actual_work_units | 65102 |
| actual_checks | 149930 |
| storage_observations | 587 |
| free_bytes_reserve | 2147483648 |
| phase_finished | true |
| stop | null |

原sampler总elapsed为4067.62586181s。两phase原elapsed不是“总数中所有工作”的新归因；不把其差值另解释成已测瓶颈。

四个原数组全部completed，格式都是little-endian binary64、C顺序：

| 数组 | shape | 字节 | SHA256 |
| --- | --- | ---: | --- |
| 完整general far矩阵 | [112,224] | 200704 | `4ee672099c3cbc80ecee6107bbc798daada012ead3b14bee40f4d41da6e8e958` |
| full-stage field geometry | [576,28,5] | 645120 | `17954e62c456f8cb46185aabef4c9fa8694bfb15498a54cb2968eb55c9b1a43b` |
| node mu | [577] | 4616 | `3a18a8ec7ce41ce9e008909b113a433874236b3626955cce0b1f150d0a942841` |
| node radii | [577] | 4616 | `6e5b18eaa512e74cf68082bdda53d8220eb87ece003c39019947ce93d2fe032b` |

sampler result44568B / `d09e7e9e92ba0efcd6e1fac22da66ac0b7162b0fa3712cde0daf6ae8633ac3cb`；geometry2022574B / `80fc845d9aebbb71577b4679d1b8f5741e79a6012ca00d59837ded8a1a4d51c3`。完整input binding canonical SHA为 `db29ee8c0cfc880b73ffbccfd84bccc92decefaf4cf97005cc387b76026ac769`。

仍未支付：`exact_global_C_realization_of_numeric_representatives_certified=false`、`nonlinear_solve_or_DN_computed=false`、`closed_field_or_BVP_accepted=false`。本次返回的准确区间族和数值输入代表是两种对象；完整有限数组不是准确连续解、非线性DN或全闭面证书。

## 478.8 真实临时账、后续磁盘要求与未启动BVP

原sampler的完整stream身份如下。成功coefficient、panel、commit与point-values流只有全字节hash/行数被reader核，没有把每行数值独立重审；其他标明“逐行”的流确实在Actions中全部解析。

| stream | 行数 | 字节 | SHA256 | 原读取范围 |
| --- | ---: | ---: | --- | --- |
| coefficient-boxes | 15459 | 30287462 | `8932f8ca1f5071a08879f237989fcafee7754168cab647714b7d199bf794118c` | byte/hash/count |
| far-accepted-panels | 1604049 | 95028212980 | `aba486e649d354a61857e03de6927a300ed1373b34bc41676c36025354af177c` | byte/hash/count |
| far-panel-commits | 1604049 | 798985781 | `930f254763d71b2420cefe91a96cf7ce1b86b9a83b9e9b50adaef59512f10853` | byte/hash/count |
| far-all-mode-rows | 112 | 1705701 | `de7ff440fcd5ce81bb43667c7f466b1669b57a2bb0ac6ff9088db166514a73c0` | 全原行解析 |
| far-complete-tubes | 112 | 2094674 | `b9239c436ca3862cfc08f72e742477d9d7e78640844b2c13568e42630086610c` | 全原行解析 |
| far-inverse-leaf-coverage | 112 | 65691 | `a834078b1efb4580f81d7019901714b298dc34ee0fa4374f1c61f594d0e53eb3` | 全原行解析 |
| numeric-far-row-selection | 112 | 1023798 | `c5936bc39b507f6a7f643b7497179da4870ebed5b6467b1683c609800abbfa88` | 全原行解析 |
| numeric-point-values-and-errors | 16128 | 61483687 | `5dd90105d543cb8a2aadb8d092ec8043635dfa4bfb098ab2b71f69a794cc4348` | byte/hash/count |
| sample-inverse-leaves | 16917 | 28931878 | `c1c3be4e4df32743a5ffbde64970e6cb54431df6265f56ec380af7530b1b8d09` | byte/hash/count |
| complete-unpaid-scope | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 全原行解析，实际空 |

原general far完整区间及代表导出JSON另为1305711B / `f8d2fb152b756405e89e34b9d3a2ac559ffe8e47e683bb145ac096cf736e94df`，只保身份，不在本文复制正文。

必要reader对实际自有范围共hash20个文件、95962633407B；原完整path/byte身份索引SHA为 `827f9bdac6b8728d9850a3439d02679309a132e4a7772dd6dc7535c134d6cbe3`。这项不是整个runner磁盘用量，也不是BVP已读取95GB科学数据；它只界定reader实际hash的自有范围。原数组未被reader重算。

启动时临时盘清理已使free从91971571712增加到110572691456B，总盘154993672192B。有限far结束原最后存储记录free11892830208；点采样最后存储记录free11790274560。随后BVP启动器真正检查free11761553408，低于其原34359738368要求。95,028,212,980B的far accepted日志是明确占用对象，不能只说“机器慢”或“精度不够”，也不能在未查后续消费者前擅删该账或降低原启动阈值。

candidate绑定此前确已成功：

| 真实对象 | 字节 | SHA256 |
| --- | ---: | --- |
| 当前native client配置 | 5960 | `35cf554efe92e8df9a01eb7db1538c2f94dd88235b2c868b16ad9063c59cd1a3` |
| 实际candidate binding | 22195 | `8253baf69e1cc2c07fdf83750c356ab3adb38ed89caf037d9b01f1202f59796f` |
| 实际BVP输入result | 6756 | `d7311928861fe33fa6e790b09f1f3734de4082445f499b990db1398695d33a82` |
| 当前十参453/450配方 | 20408 | `4d27707e790eec39126f141599f48972f72d29ee074d09723869c8db5402703d` |
| 实际current-BVP deadline | 1328 | `8299b8bafc99011353ab9135eefc4b5da2f8d858fe7a0043aee8bd37d521090a` |
| 原launcher停止result | 3380 | `c45bd65360cf2ca42f651d49735aa7019556d5f72f3607af5a1f15aee58901de` |

实际driver仍56cbf3b2、launcher仍227ef601；没有用旧cb057或把actual202候选改名为joint203父。原lambda=.001、17 inner trials、8 outer、native32×10与所有原容差保留，但没有真正执行这些迭代。

launcher原字段：`actual_child_process_started=false`、`actual_child_exit=null`、`completed_driver_return=false`、`current_finite_BVP_accepted=false`、`error=null`、`external_interruption=null`；elapsed0.0004956870006935787s。two-phase reader对design453与frozen450均记录 `exists=false,not_started_not_success=true`；shared-native目录不存在，未推断任何请求。

由此仍全部未付：真实当前H、current root/RK、完整非零响应、338×112 J、双mean、FD、fullDN、fresh final/audit、真实accepted453、同点完整accepted450与checkpoint。也没有实际失败的native trial可供追溯；缺失字段不能填成0残差或空成功表。

## 478.9 原钟、closed后缀、全owner静止与读回失败

namespace原起点1794806966.3080468，science预算18900s，readback预留2700s，job360min。实际BVP deadline1794825866.3080468，由同一起点形成；candidate binding没有重开钟。采样未来BVP reserve明确3600，原BVP单进程最大7200仍在。原namespace在早期阶段是启动裁剪计划，不声称存在覆盖所有早期绑定工作的全局绝对kill；真正BVP/closed启动器采用实际deadline。

closed外层确实运行并读取真实BVP停止result，然后返回：

- `upstream_stop="original-complete450-acceptance-or-quiet-not-returned"`；
- `unstarted_outer_roles=["postsolve","held"]`；
- `actual_exit_code=3`、`error=null`、`resource_stop=null`；
- `elapsed_seconds=0.005275652000818809`；
- 原八项work cap仍为construction_parameters120、radial_replay1800、original_cuff_atlas120、shared_field600、metric1800、reach1800、held_witnesses120、held1800；
- 不曾因metric或reach未通过而挡held，而是共同的真实accepted450前提没有产生。

因此没有首次W/H/marker实际冻结、材料B记录、径向重放、准确cut场、固定帽、metric、全pair reach、全像held、含反射deltaE、mesh/M/t精化或显示。没有从空目录造field或把旧recipe数值当已接受父。

closed独立metadata完整返回，`necessary_readback_complete=true`、`quiescent=true`、`metadata_errors=[]`、`raw_cleanup_performed=false`。它只支付not-started及资源来源的读回，不支付下游科学。

原全owner观测在07:16后的实际读取中列出8个真实role、16份parent/science启动receipt：selection、C、construction、far、sampling、binding、bvp、postsolve。逐PID/start_ticks与独占science PGID核后，`live_original_owned_processes=[]`、`unknown_owner_scopes=[]`、`quiescent=true`；共享父PGID没有被误作科学组。closed字段里保留历史名称 `all_seven_role_launch_receipts_identity`，不能用这个字段名字否认观测实际列出的8个role。

原2700s规则runner期间有实际pull/rebase与规则stamp；compute可见9次 `actual_rules_sync_completed`，包含sampling的round1。最后postsolve的实际规则read为main181eee60…，stamp8fa286e6…，README原两blob仍21bd547f56590b7f2dd279d0297efb289a9b2783与bff8aea253a9e6a7a4fac28d810ac454c5499fec；该role `README_change=null`、`periodic_sync_failures=[]`。C与deep的已返回rules result亦无规则变更停止。**原全部规则/资源摘要仍超限未回传，不能把局部已返来源扩大为缺失94138B全文已读。**

BVP必要reader实际记录：5个JSON文档、0个native日志、4个显式遗漏member身份，`original_read_errors=[]`、`complete_necessary_readback_without_recorded_error=true`。0日志由native未启动而来，不代表已运行但无异常。其完整parser和字节scope属于本次具体读回，不能替代后续native末门。

## 478.10 实际八份读回、清理及完整未付责任

原七必要步骤与212组成读回分别是：

| 必要责任 | 本次实际结果 |
| --- | --- |
| C | 步骤22 success，完整必要JSON已返 |
| cut | 步骤13 success，完整必要JSON已返 |
| construction/candidate | 步骤18 success，完整必要JSON已返 |
| deep far | 步骤23 success，完整必要JSON已返 |
| sampler / 双BVP | 步骤24 success，R477新schema完整必要已返 |
| closed/held及其资源scope | 步骤21 success，真实not-started metadata已返 |
| 原规则/资源scope | 步骤25 failure，94138B超限，正文未返，marker未写 |
| 212完整composition终态读取 | 同步骤25中排在前项之后；前项exit70，故该调用未执行 |

实际cleanup步骤26程序运行成功，但检查原步骤outcomes时读到 `RULES_READBACK_OUTCOME=failure`，打印：

> request205_owned_cleanup_skipped

原事件明确 `raw_left_only_until_runner_destruction=true`、`no_missing_readback_or_scientific_completion_inferred=true`。它没有主动删除当前namespace；runner销毁时的临时数据处理不能倒称为完整读回之后的主动清理。所有大raw仍只在该job临时环境，没有上传artifact、放入Git或由chat取大数组正文。

本次严格分开的最终责任：

1. **已付有限输入生成：** 原C完整头/六primitive/闭query合法包围，cut三盒，新准确十参定义，完整112 deep/far及joint名义行，完整depth2物理点计划与四个native数组，真实candidate/config/recipe/deadline。
2. **仍是数值工作未决：** C的2609个whole-query work-resolution片段、三个有限积分coarse panel的各自原范围；当前ten域12937 terminal/15 stack；点采样32bit工作目标未全达。这些均不能凭标签转成数学反证，也不减少已完整覆盖的候选。
3. **真实BVP资源未付：** 32GiB启动free要求未满足，453/450/native/J/FD/最终audit未起。已生成输入不可冒accepted父。
4. **下游几何未起：** 同一准确g与材料合同、全tmetric/reach/held/deltaE、精化误差下降、显示均无本次实绩。
5. **读回未完成：** 94138B原规则摘要未返；212终态composition readback未执行；没有完整八scope清理marker。已返回prepare/verify及ownerquiet不能填补这两项。

后继应沿实际大账的消费者和存储生命周期解决可执行资源缺口，保所有仍需读取的科学输入与原34359738368 free要求；同时修必要元数据冗余及独立always读回的组织。本文不预先批准删除任何大账，不降低存储阈值，不改已运行212或在跑214/216，也不承诺下一次一定完成。完整浅逆采样的这项真实进展与其后的资源/运输缺口都应进入当前责任状态。
