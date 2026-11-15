# R367 — 实际 Request 169 重发：新连续标量完成构造，首 far 模态切图未付，完整 BVP 未启动

作者：AI。日期：2026-11-15。

状态：公开 Actions 已发生结果的完整范围结论。本文读取原日志、原小摘要与所导出的原元数据；没有在本地重新积分、传播、形成矩阵、运行原 RHS 或求解。它不证明完整 112 有限头 DN、当前非零 $H$、新连续目标的完整 BVP、同场相对 metric、全局 $C^2$ 闭场、embedding 或 reach。

## 367.1 实际结论与最先未付位置

本次是 R362 记录的缺少 sparse 文件之后的真实重发。该来源问题已经消除，原全部来源绑定、连续 C、实际 cut 两阶 jet、新九控制标量构造和 112 个深端行都执行完成。随后，原射影 far 传播在第一个频率 $m=2$ 上保留 49 个已提交闭面板后停止。原错误为：

> Neither complete physical-far endpoint component excludes zero

这是原 `PanelUnpaid`，发生在 original source panel row 17、source piece 3 的 depth 32 子区间。该次线性记录只有 100 attempts；资源 `stop=null`。它不是 25,000,000 attempts 上限、实际墙钟或磁盘储备耗尽，也不是一次 native 十档试步失败。

实际 far 候选数、单位行数均为 0。全部后续频率 $4,6,\ldots,224$ 未启动。随后 BVP 入口读取真实 `native_geometry_ready=false` 后没有生起完整 BVP 进程，故没有生成当前 $H$、当前尾响应/J、原 FD 检查、453 维迭代或 final fresh audit。Report 的 exit 2 传播这个实际未付范围；它不把输出传输成功记作数学成功。

本次原件依据：

- [实际 run 43741519736](https://github.com/Rogerhu12/math-research-public/actions/runs/43741519736)。
- [compute job 132895511639](https://github.com/Rogerhu12/math-research-public/actions/runs/43741519736/job/132895511639)。
- [report job 132910383303](https://github.com/Rogerhu12/math-research-public/actions/runs/43741519736/job/132910383303)。

## 367.2 唯一实际来源与日志身份

| 对象 | 实际身份 |
|---|---|
| source commit | `de9a730a8f9cf8ea1f3e31fa6f6dd9cfb64e1d80` |
| compute | `132895511639`，failure |
| report | `132910383303`，failure |
| workflow | `visible-larger-public-current-C-projective-full453-physical-DN.yml` |
| workflow bytes / SHA-256 | 86,335 / `887dc763df1d0d8f6f69a5eaea03f2b1b7c643e4e21fba03b707c07ce0902115` |
| 实际 request bytes / SHA-256 | 37,078 / `41ccd38061cbf561cc6751cc220a272c9dc24723f088b2826e046ff62d740ff3` |
| 实际 recipe bytes / SHA-256 | 9,940 / `f8f6b353458f04052940a05bbe28d28c48b0050f631f76f813267924a31d4765` |
| compute 完整解码日志 bytes / SHA-256 | 771,044 / `d71e911fb75c3d7dcf8f17eb6f05e103c5495becceffd82cddea5e036d15755d` |
| report 完整解码日志 bytes / SHA-256 | 168,805 / `67c5d6de47998e65fc7c5ed71390ddf6d1823c1605ad2d4ee2525ffe5f4b77ca` |

日志哈希针对工具返回的完整 UTF-8 解码文本（包括原始开头 BOM），不是压缩 ZIP 的哈希。两个完成日志各读取一次；没有读取 running 日志或重新下载科学大包。源码身份由本次 preflight 原事件给出：58 个 direct source 全核；实际工作流还在 Actions 内核了 19 个 bash block 和 18 个 Python heredoc。此处不冒本地编译或对源码重新执行。

与本次真正走到的路径有关的冻结源如下。其余 direct pin 仍由上述 37,078 B request 与原 preflight 完整列表确定。

| 源文件 | bytes | SHA-256 |
|---|---:|---|
| `geometry_20261115_stored_continuous_E_cover_v3.py` | 89307 | `f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df` |
| `geometry_20261115_stored_C_v3_cut_twojet_readout.py` | 19023 | `1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed` |
| `geometry_20261115_stored_continuous_C_far_graph.py` | 16333 | `fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a` |
| `geometry_20261115_continuous_nine_scalar_factory_v3.py` | 42270 | `0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e` |
| `geometry_20261115_continuous_nine_scalar_numeric_v3.py` | 22469 | `7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60` |
| `geometry_20261115_continuous_nine_v3_actual_construction.py` | 20377 | `738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0` |
| `geometry_20261115_current_C_projective_radial_sampling.py` | 60118 | `b290dd6030224efc36bfeb30a53e00d76c43c924ae67a0c068e0d23d4d82d8c4` |
| `geometry_20261115_stored_C_finite_head_projective.py` | 77731 | `5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216` |
| `geometry_20261115_current_C_projective_full453_physical_dn.py` | 62843 | `c35806666d9f0d7912ed6496e51d520421bf0d24db22972fc43d4e6e0b5d1c9b` |
| `geometry_20261115_current_C_projective_full453_launch.py` | 19213 | `9a7602ada770fcdc2bcc1b81456459afb2448eff414453b5529c62d4df80df63` |
| `root_20261115_current_C_projective_full453_scalar_readout.py` | 18339 | `a4b8f1f4a1cc3a0703c94f345b2b90e41525b54a031d3d47ca68fb58a3eeaea2` |
| `root_20261115_current_C_projective_native_scalar_readout.py` | 33600 | `8a3ddc5d59244b245292bd5a0e3fb33768527017148cc4e697d2f2cf771989e7` |

原三层范围必须分开：声明 C 的严格区间族；有限数值 profile 的明确代表；原完整物理 BVP 的实际调用。前两层在本次有各自结果，第三层未启动。源标签之间没有自动支付“这些中点属于同一个准确 C 根序列”的责任。

## 367.3 原输入、九个字面参数与未执行的 BVP 配置

五原件从公开历史提交 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复后按原字节核验，没有将当前 main 路径的存在当作来源：

| 原件角色 | bytes | SHA-256 |
|---|---:|---|
| config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| calibration_ledger | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| stored_reference | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |
| accepted | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| complete_seed | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |

完整初猜原件的 producer 是 `9a1ae018d71e38ff901c4b9156b23502a4efde44f812c1ff4e03323878b659db`。实际 metadata 为 699 个 nodes、每 node 453 维，旧 `success=false`。这不是新目标的成功场。原 RHS、metric、tail、zero-J 和 acceptance 不继承；公共 $u$ 重新参数化、fresh RHS 和 current $H$ 原本须由未启动的新 BVP 实际形成。

本次明确取 $\lambda=0.001$，前三个参数活动、后六个冻结。原九参数全文：

```json
[0.3055213835477326,0.21645013203050154,0.34270051957744246,-0.06322334619266512,-0.01747451701873286,0.9376115689625685,1.0751306255033548,0.6886900390922872,0.9385431607625546]
```

其来源只取实际 146 的 final 九个字面系数：run `43716274591`、source `69765fcd81ca84819cdeb09c4fe14c55fdb5fb80`，原 status SHA `252a9ceabf63305cdab40312b104e397acb7a8deb52ea513d4ecc038104d80e5`、primary SHA `befc5446223c3f45bc96f4d53aeae6e0115f2fe3214051bc4219f2465fefe1e9`。没有把旧 merit、J、radius、尾数据作为本次 fresh 值。

本次 recipe 保原完整 453 状态、338 个物理分量、112 模态、699 初猜节点、max-nodes 1200、原内层 17 个 trial、8 outer、RMS $10^{-6}$、BC $10^{-11}$、原 FD 阈值 $5\times10^{-5}$、native 32 轮/每轮 10 档/strict norm decrease/$2\times10^{-9}$、correction $\eta=1$ 与全敏感度 $\eta=0$。这些配置均未因本次 far 停止而改变，也没有被执行结果自动支付。18 个协议入口只是路径预算说明，不是新调用上限或新数学门。

## 367.4 同 job 连续 C 与两个闭查询的实际返回

实际 C source 是 f12f7470 原 v3；模型是 R286 声明 C，全 160×9=1440 个有限头片、所有六 primitive、原完整 deep root family 保持。实际 elapsed 为 2624.792453377 s，`error=null`，`complete_original_pieces=1440`、`full_finite_head_complete=true`。

计数为 integral_panels 121,832、inverse_cover_nodes 200,000、rigorous_analytic_component_integrals 307,101；deep_root_values_computed=0，没有选一个数值深根冒全根族。原 finite joins 与 protected join 的结构条件返回 true，但这不证明整个后续 453 场的 C² 接缝。

原 full-deep-plus-head 六 primitive 的显示串逐字如下。显示串只作阅读；准确对象仍是各记录的 dyadic endpoints：

| 原分量名 | 原 display |
|---|---|
| `A` | `[0.153108624575236913660813795 +/- 6.04e-28]` |
| `B` | `[0.0006007753386900131932393033 +/- 6.76e-29]` |
| `sqrtE_A` | `[0.155428043739402048155120789 +/- 5.82e-28]` |
| `sqrtE_B` | `[0.0006038258763311991045034738 +/- 8.20e-29]` |
| `w_A` | `[0.0193506687326223318482260558 +/- 2.49e-29]` |
| `w_B` | `[2.06702624761192542912554e-5 +/- 7.14e-29]` |

两个实际闭查询分别为：

| 查询 | 完整域包围 | work resolution | 实际范围 |
|---|---|---|---|
| 原 binary cut 点 | true | true | 5 refined nodes，1 个 head leaf，0 个未决精度片 |
| whole-natural-domain | true | false | 93,979 refined nodes，leaf span [1,108625)，2609 个原 query-resolution 记录 |

全 query leaf 流原件为 197,572,200 B / `98188fa682e374923673639b3a57a2d9bc436cc29b96537677313b7385cf443d`，共 108,625 行。C 原结果 32,110 B / `6b8ad76636f56786672836076259360e6c1d381bc9c7d27d895930a70c239e36`；原 query-results 1,898 B / `16d5b0660e18640555a550731e583300d45915de742438d0dcab6c1a1dd33b50`。

2609 个记录全部为 `query-resolution`，原 reason 是 inverse-cover node resource budget reached。没有 unvisited source-piece suffix 或 unvisited query suffix；这些 coarse 闭包围仍合法，不能写成域失败。第一项是 source piece 1400、cell 4、segment 5、原闭参数区间 `[54365/65536,108731/131072]`、inverse depth 8。该项原 `inherited_valid_coarse_enclosure=true`、`work_resolution_met=false`。完整 unpaid ledger 为 5,209,016 B / `9964a6e6c2c9d16badaac70709c5fd428bca21a5bae0466df5360f40fe2f6a3a`。

自然外半径原 display 是 `[0.30000000000000715908123386 +/- 6.75e-27]`；其减原 binary cut 的 display 为 `[7.1701834641e-15 +/- 1.01e-26]`。没有把 natural $R_{\rm out}$ 重命名成 0.3，也没有作额外平延拓。原有限 selector/旧导数未获连续解认证，a601 同场 metric 阈值仍 false。

## 367.5 原 binary cut 的完整两 jet

点取值是 config.rCut 的实际 word `333333333333d33f`，即 $5404319552844595/18014398509481984$，未重新归一。1 个完整 head leaf [0,1) 行范围的所有返回值均进入 hull。cut readout 原件 5,685 B / `f6dbeb61d83be0966b4a68b6fd2e5abd6952f80fd951859579cdc6f0f3aaedda`。

| 原量 | 原准确 dyadic 闭端点 | 原 exact_full_width |
|---|---|---|
| `E` | $[297036851754023534385\,2^{-68},\;297036860731551973169\,2^{-68}]$ | `8977528438784` × $2^{-68}$ |
| `E_r` | $[-1377364570695686333\,2^{-62},\;-1377334639942752445\,2^{-62}]$ | `29930752933888` × $2^{-62}$ |
| `E_rr` | $[-18506607869532518095\,2^{-57},\;3541147354781501745\,2^{-57}]$ | `22047755224314019840` × $2^{-57}$ |

本次这些端点与此前独立 C 查询出现相同字面值不意味着重用旧求值；本次 source/run/输入与实际全 query 流另有完整身份。原 v3 的 work target 只要求 E 宽度，不要求 $E_r,E_{rr}$ 宽度；没有因为 $E_{rr}$ 盒宽而撤掉合法包含，也没有把它改作新 BVP 接受门。这三盒本身不是 cut DN。

## 367.6 新九控制标量：准确构造、数值编译、域未决分别保留

实际使用 R323 显式窗口：

- collar $d=1/524288$，first/last transition 各 $1/1024$，$\kappa=1/2$；
- 原 core end `4458563631096791/4503599627370496`；
- first support 的 left `3566850904877433/72057594037927936`、stored width `4458563631096791/18014398509481984`；
- nine coefficients 全保上述实际字面值。

原 geometry pointer 是 `/fixed_scalar_profile/geometry`，core end pointer 是 `/mesh/-1`。本次没有把 legacy finite-Gauss 或 clip 的标签自动当准确两 jet。R300 的新对象声明及源表达保持明确，`literal_old_g_preserved=false`。

原 11 个严格构造条件全部 true：cut collar derivative/radius gap、coast length、两端 transition derivative/radius、bridge gap、total width、core-end radius above cut、真实 cut speed inward/subunit。它支付构造的规定条件，不是九控制全部范围或 BVP 成功。

| pass | elapsed s | passed leaves | processed nodes | unresolved terminal | unvisited stack | complete |
|---|---:|---:|---:|---:|---:|---|
| 无九控制的 base | 0.18919981199996982 | 452 | 485 | 0 | 0 | true |
| 原指定九控制 | 301.9698686920001 | 1735 | 24380 | 10657 | 15 | false |

两个 pass 各保全部闭覆盖，后者 `all_parameter_values_retained=true`。它是该充分区间算法的 partial，不是在本次新判定连续速度域反例。之前对固定 R320 点的独立严格反例也不能充作本次未运行的三 active BVP 的全轨迹结论。

本次准确模型定义 377,837 B / `4d9fbc00afd410dc7e97e5dbb32a2f2e83b35c6661bdc23fa459c6fa3165326c`；新数值规范 270,229 B / `4e21c20b2d82b32e0758797aef1c5c14bd70c5af021b6df03e8601bd02dbae5a`。数值编译报告 419 片、418 seam、207 对完整 finite jet words 相同、数值物理长度 2.723563252110879。该原计数来自编译摘要；本文不重新输出或重建 152,147 B 完整 seam 分段，也不把未逐值独核的大表说成再次审过。

编译使用原 E0/E1/E2 中点的明确数值代表，分别为 1.0064000151459218、-0.29866508687182997、-51.92187136748508，原 word 为 `23eefbe6361af03f`、`9993242b541dd3bf`、`ce3b87e1fff549c0`。原记录 `numerical_midpoints_not_asserted_one_true_tail_root=true`、`true_evaluator_error_bound_not_supplied=true`。准确定义不被数值长度或这些中点替换，有限 word 相同也不支付 exact-real 全局 C²。

本次 construction elapsed 302.82473100399966 s、original factory return code 0、phase `complete-with-original-paid-and-unpaid-scopes`、`error=null`。准确对象创建与显式数值 profile 编译成立；`all_nine_requested_domain_complete=false`、`same_field_metric_or_C2_geometry_certificate=false`、actual tail/native calls 0、actual BVP/fullDN success false。

## 367.7 全 112 深端返回与实际 far 点

R312 深端 source fe66789e 的实际 elapsed 0.014278093000029912 s。全部频率 $2,4,\ldots,224$ 共 112 行返回，`unpaid_mode_suffix=[]`。行流为 494,612 B / `d68c5547b0323dd2a2bff3fa4087ed5aad831646cabff7c7804519025aa528b9`；deep result 5,857 B / `a96c1d7922d4a88435904d6affbcdb19ec15775eec844f3f04aadf1c6f4260de`。

这是 physical node 160 / port 159、所有 $n\ge160$ 原准确深根族的线性端行。原 `root_choice_resolved=false`、deep root values computed 0、finite ODE/RHS calls 0、cut_DN_matrix null、cut-height denominators false。全112深端成立不包含 112 个有限头到 cut 的非共振责任。

sampler 重新确定本次的实际物理 far 点。原规则是“严格大于完整 node8 半径 upper endpoint 的下一个 binary64”：

| 实际字段 | 原值 |
|---|---|
| source piece / source panel | 1367 / 10385 |
| original cell / segment / parameter | 8 / 8 / `1` |
| physical far value / word | 0.05056158669090205 / `f0e68a5235e3a93f` |
| $\mu$ value / word | 1.7421589928370103e-17 / `705c211ef215743c` |
| 当前 point/inverse count | 1 / 25 |
| 完整物理 far 可能逆像叶 | source piece 1368，闭区间 `[0,1/4096]` |

不把该准确 binary far 点说成等于不确定的原 node8 半径。它属于当前 C 自然域的责任已在原 sampler 绑定中重新核；far row 不通过除高度生成。单位行正常化仍须原 R357 的方向、幅度符号和完整 norm 隔零条件；本次尚未到任何 far 候选，故“row_norm_unproved_count=0”只表示没有执行该候选检查，不是归一条件已付。

## 367.8 首模态原状态、两端点盒与最大深度停止

当前 sampler 原 result 为 40,050 B / `e077819e4cb6d0fc2ee78fb37320ca83e10e6cefd1af0909cdbef16807e411b1`。其顶层 `error=null` 是受控返回容器；必须同时读取原 mode.error 和 complete flags，不能将顶层 null 解释成完成。

$m=2$ 原统计：

| 字段 | 原值 |
|---|---:|
| accepted / committed panels | 49 |
| complete step rows | [0,49) |
| complete panel commit rows | [0,49) |
| coefficient range splits | 23 |
| uncertain endpoint pivot splits | 27 |
| norm / defect work splits | 0 / 0 |
| valid coarse panels | 0 |
| actual total attempts | 100 |
| far tube candidates / unit rows | 0 / 0 |
| completed inverse leaves / required leaves | 0 / 1 |
| uncertain far row norm splits | 0 |
| uncommitted step span | [49,49) |
| uncommitted far span | [0,0) |
| uncommitted transaction | null |

最后提交位置为 panel 17、piece 3、参数 `334530667/536870912`，commit row 48。原状态 chart 0、balance exponent -384、amplitude sign +1、factor count 49，factor-chain SHA `ce389b50e0f237bd7264d93a128dfc7c4113537b71bbb91e904c79c1b518cc0b`。其被选坐标严格为 1；另一完整分量盒是

$$
[-709529937\,2^{123},\;1060426683\,2^{123}].
$$

这不是准确方向为零的证明。失败候选另先作原精确二幂重标，whole incoming norm 原值 1.97519862465560436248779296875；候选两端点盒为：

- 第0分量 $[-106266603284618213790286762995471494170387669828664472570725324414829924974595\,2^{-405},\;97463335294809271157299742250686464314406246982913610848372943719079790772223\,2^{-404}]$；
- 第1分量 $[-38257779167572226857654915373350538227729197453261693685896496087684211539969\,2^{-254},\;114356188566491272098376885736973457421462642756929531118178605476576996884479\,2^{-255}]$。

两个原 pivot record 均 `exact_absolute_lower_bound="0"`、`strictly_excludes_zero=false`、sign 0。原 `needs_pivot_split=true`，`needs_norm_split=false`，local work goal met true。因此不能强行挑一个中点作合法 chart，也不能由准确基本矩阵可逆直接推当前宽盒存在可验证 pivot。

原显示给出的 whole fundamental Duhamel defect 约 $7.8755465\cdot10^{-53}$、whole solution error radius 约 $1.5555769\cdot10^{-52}$、Taylor remainder 约 $3.9324295\cdot10^{-1145}$；本文只转录原 display 的量级，不在本地重算、比较具体贡献或推断“唯一根因”。继承盒、二幂重标与完整误差仍共同进入该次区间包含。

## 367.9 完整未付栈、源后缀与未启动模态

失败候选为

$$
[334530667/536870912,\;2676245337/4294967296],
$$

depth 32。当前 panel 的完整 outward-order 栈共有 19 项，全部属于 original source panel row 17、source piece 3：

| 原栈索引 | 左端点 | 右端点 | depth |
|---|---|---|---:|
| 0 | `334530667/536870912` | `2676245337/4294967296` | 32 |
| 1 | `2676245337/4294967296` | `1338122669/2147483648` | 32 |
| 2 | `1338122669/2147483648` | `669061335/1073741824` | 31 |
| 3 | `669061335/1073741824` | `83632667/134217728` | 30 |
| 4 | `83632667/134217728` | `20908167/33554432` | 27 |
| 5 | `20908167/33554432` | `2613521/4194304` | 25 |
| 6 | `2613521/4194304` | `1306761/2097152` | 22 |
| 7 | `1306761/2097152` | `653381/1048576` | 21 |
| 8 | `653381/1048576` | `326691/524288` | 20 |
| 9 | `326691/524288` | `81673/131072` | 19 |
| 10 | `81673/131072` | `40837/65536` | 17 |
| 11 | `40837/65536` | `20419/32768` | 16 |
| 12 | `20419/32768` | `5105/8192` | 15 |
| 13 | `5105/8192` | `2553/4096` | 13 |
| 14 | `2553/4096` | `1277/2048` | 12 |
| 15 | `1277/2048` | `639/1024` | 11 |
| 16 | `639/1024` | `5/8` | 10 |
| 17 | `5/8` | `3/4` | 3 |
| 18 | `3/4` | `1` | 2 |

原 `subsequent_required_original_panel_suffix={first:18,stop:10387}`。该 suffix 是 current far 的所需源前缀内范围，不得换成全 cut 的 14644 末点。另有独立 `complete-finite-far-unstarted-mode-suffix`：attempted unpaid 为 [2]，remaining modes 是全部偶频率 4 至 224；本次并未把其逐模态生成值补零。

唯一 far inverse leaf 为 piece1368、`[0,1/4096]`。原 committed covered interval=null、complete_original_inverse_leaf_spatial_scope_paid=false、committed_candidate_count=0、complete_unit_row_count=0，same_closed_endpoint_retained=true。全流与该一行的原身份已保，不能用还没抵达该叶的状态填 far 值。

## 367.10 真实资源、规则同步与清理顺序

原 request 的 explicit projective plan 是 linear 14400 s、25M attempts、point sampling 1800 s、1M inverse nodes、2 GiB free reserve。实际在原 rules startup 后，为原 BVP 7200 s 留计划空间而同倍率 clip；它不是从 namespace 起的通用硬 kill clock。

| scope | 原 declared effective 秒 | 原实际 phase 秒 | work units | stop |
|---|---:|---:|---:|---|
| physical point sampling | 960.8740745915306 | 0.4408826520002549 | 25 / 1000000 | null |
| projective finite-far | 7686.992596732245 | 0.1312898299997869 | 100 / 25000000 | null |
| sampler 总结果 | — | 4.146346821000407 | 原分别计数 | 顶层 error=null |

线性最后实际 disk free 107,869,614,080 B，储备 2,147,483,648 B；因此不是存储阈值停止。两个 phase 内时钟均排除原 binding/runtime setup，不能将其当全部 job elapsed。后续 BVP launcher 未启动，其独立 deadline 与 SIGTERM/SIGINT 转发合同此次没有被执行。

原 rules runner 确实分别在 17:32:53、18:16:42、18:21:47、18:21:50 UTC 做了各自 round0 同步。最后一次原事件读 `e445927c98c5d89f8bb7aece33496180d7ddb755`，发表 `e84be4e8360dbad53bfde85fe6822981e9b59001`。这是 Actions 的实际规则同步，不能写成本地 terminal pull。根/题 README 原 blob 仍按 `21bd547f56590b7f2dd279d0297efb289a9b2783` / `bff8aea253a9e6a7a4fac28d810ac454c5499fec` 绑定。

所有六项最终读回 outcome 为 success：C、cut、construction、far、BVP necessary readback、rules；owner observation quiescent，unknown scopes 空，BVP launch null。随后 18:21:57.0049167Z 原 `request169_owned_temporary_payload_removed` 记录只删除本 request 的 owned raw。读回先于删除，没有 artifact、Release 或 main raw 上传。Report 已完整读五摘要，再以 compute/BVP outcome failure 退出2。

## 367.11 原字节读回的已付范围与限制

本次必要 BVP/sampler 原块以下均以原 JSON payload 加其约定 LF 逐 SHA 核同；7 项全部 true：

| 原 label | bytes | SHA-256 | 实际核同 |
|---|---:|---|---|
| `BVP_LAUNCH` | 130 | `ee99d34c4e262a23d7358edd169e686404090f5b6e553dc41b98697b2f810a5c` | true |
| `SAMPLER_UNPAID_0000` | 15305 | `8cac8f3b95c6f2257a82905463d26d20b739b16f26dd9bc686fc3c9c4221dd34` | true |
| `SAMPLER_UNPAID_0001` | 1104 | `4396e8cd05d70dc6b42182ddf46d5c1a89d8c239e638933ccd8a48b1460914b0` | true |
| `SAMPLER_COMPLETE_MODE_000000` | 22682 | `cc5fbbe393cb0a59f9eb7b69492e8f0d277a6d6b207c06b6d51136ada96afa56` | true |
| `SAMPLER_COMPLETE_FAR_LEAF_000000` | 1102 | `6afd3e5a5998acf7c5051916bf4c9ad8182f9f9eee18fd21c3f3601932aa127d` | true |
| `BVP_SAMPLER` | 11012 | `51ba9cfa4b0f179e10e89070cb63d34dcea37ad99d20377b2b8beae0bdce50f2` | true |
| `BVP_COMPLETE_EXPLICIT_RAW_SCOPE` | 120 | `f48ba30141e7ca4d09bf7a006489b9dd942e7c707533581cca7f7f3b8d4addb9` | true |

Compute 与 report 的 C、cut、far、construction、BVP 五份 primary payload 字符串逐字相等；没有用 report 重新序列化取代原 compute 字节。BVP reader 的 original_read_errors=[]、complete_scalar_readback_without_recorded_read_error=true，源文件共10项，explicit recomputable omission count0。这个0只在该 reader 已声明的 necessary metadata范围成立，不表示大科学数组已全部返回。

sampler 原账本身份：

| 原流 | bytes | SHA-256 |
|---|---:|---|
| coefficient-boxes | 164885 | `dd7569b0d7cc994a679c48d3172f53c9751e62ff11964728bac05ee9c597be2f` |
| complete-unpaid-scope | 16147 | `af9dc0e94f9e82e0de3ea15132ed421809e4faa0a950b4ad15d42e6d5e7a99b2` |
| far-accepted-panels | 648216 | `628887d0e2b48dc4fe42d529e28ccc4c082632b90e3d596f7e816db17efb994d` |
| far-all-mode-rows | 22153 | `00bad377fc043a37938db32d4fd96e427cc82e7a009210662d96287f5f71bcc7` |
| far-complete-tubes | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| far-inverse-leaf-coverage | 567 | `d1ac609344eb5994304cc7000ef0bddbf18bec66eea61f69a9d26293279c7a42` |
| far-panel-commits | 23304 | `f96dcca72f66969b0d62a2f1b8c2aded3242bcb4d8d6396b32db8adc986f52f0` |
| numeric-point-values-and-errors | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| sample-inverse-leaves | 1794 | `ce74469293a53c8abb6ae523e0d82a20acb50a64d5b439a636dab9ebe62dff2f` |

完整 mode 行、两个 unpaid 行和一个 far leaf 行均实际从返回小块读到；其准确端点/当前栈的范围已在上文列出。Coefficient 77 行、prepared panel49行、commit49行只由 Actions reader 单次全流 SHA/行数核验；本文没有取得它们的大 payload 或逐值另算。Prepared 行只有落在原 commit span 才属于 paid prefix。

原 numeric-point-values-and-errors 为0 B，不应补造577点实值、当前H或任何root/J。全深112原行流被原 reader完整解析并给出频率；此处仍是其原身份和范围读回，不是在本地再次数值核全部112行。原九控制域大流351,376,445B/完整 seam152,147B及其巨量内部表只留本次已报告身份与明确摘要范围，没有通过新的分包协议搬运或当成独立全表审计。

## 367.12 与此前结果、后续方法及课题完成条件的关系

R362 是首次169工程来源缺失；本篇是该问题消除后的真实科学范围。R368 的168旨在新C自己的零输入/native链，169旨在新九标量+真实当前profile产生H的完整453链；二者不能互相换run/输出身份。它们各自实际在 m2 的同一 source panel/depth 的射影端点隔零条件处未付，但169还包含自己的准确标量构造和未决九控制域，不能仅将168结论改编号。

本次 source 的25M上限没有触发，故再提高该上限不是对本次明确 stopping condition 的直接修复。R375 已给出另一种完整两图 Riccati 比较包含及全闭时段存在条件，后继177应从原完整深根族重新传播、保全部C系数和幅度误差，不能缩窄本次遗留宽盒或借准确可逆性宣称可除。新方法有自己的闭分母责任与诚实 partial；本篇不预言其运行结果，也不把其作为先验批准门。

本次支付的是原 C/切点/新标量构造/深端与具体失败现场。当前非零H、当前真DN/J、338响应、原FD、完整453解、fresh audit、最终九冻结同g精化、相对metric、全局接缝、embedding/reach及题目最终量均未由本次支付。继续求解须沿这些原责任推进，不能把源代码可调用或读回完整称为最终场已完成。
