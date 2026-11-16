# R453 — actual205：准确十参数域未付、完整 112 远端行完成与物理点工作上限

作者：ChatGPT（amplitude，原终态日志唯一读回）  
日期：2026-11-16

**可信度：启发式／数值证据，限本次公开 Actions 的实际输出；下文对停止位置与原控制流的归责为源码和原记录支持的结论。本文没有证明新十参数点的完整准确域、非线性解或闭面存在。**

## 1. 实际结论

request205 在新 job 中完成了原连续 C 的完整有限头／深端包围、原二进制 cut 的完整点二阶 jet、全部 112 个深端远端行、全部 112 个物理 far 的单位行族，以及全部 112 个实际 joint nominal 数字代表行。随后物理点逆像采样达到原定 1,000,000 次工作上限：只返回 3 个 unique points，完整 native field occurrences 为 0。原当前几何未就绪，candidate binding 在原已有的 native-ready 条件处返回；453、450 和全部闭面后处理没有启动。[S1–S6]

另一个独立事实必须同时保留：本次实际 202 投影得到的新准确十参数点，其 factory controls-on 域检查返回 complete=false，含 10,594 个终端未决叶和 16 个未访 stack 项。controls-off 的 base_domain.complete=true 与构造条件通过，都不能代替该点的完整十参数域证明。这个域未付字段在冻结 205 源中是完整记录的未付责任，**不是导致本次 BVP 未启动的额外阻断门**。实际阻断来自物理采样未完成。[S4–S5；§4–5]

compute 和 report 均为 failure；七份必要读回及原 quiet／cleanup 步骤均为 success。report 的非零退出沿原 workflow 保留 compute failure，并非读回丢失。本文不将任何 job、summary 或来源核对的 success 转换成科学接受。

## 2. 唯一实际身份及读取边界

| 项目 | 实际值 |
|---|---|
| repository | Rogerhu12/math-research-public |
| source commit | e17aef55b9cc4d3f53054d2b79c853ff395d1227 |
| run / attempt | 43796116341 / 1 |
| created | 2026-11-16T03:06:19Z |
| compute job | 133065195355，failure |
| report job | 133108834041，failure |
| request | notes/current-C-actual202-accurate-ten-closed-geometry205-request.json；97,406 B；06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4 |
| workflow | .github/workflows/visible-current-C-actual202-accurate-ten-closed-geometry205.yml；95,760 B；726d97e1aada5d34ddfa949753ce59c6909122d3de8c39bd5a2160fdb8712c36 |

[实际 run](https://github.com/Rogerhu12/math-research-public/actions/runs/43796116341)；[冻结 source](https://github.com/Rogerhu12/math-research-public/tree/e17aef55b9cc4d3f53054d2b79c853ff395d1227)。

两个原日志各读取一次。连接器返回解码字符串，本地只做运输前缀识别、文本／JSON 选择和身份核对，没有导入科学模块或重算区间、ODE、J、FD、BVP。

| 日志 | 返回文本重新编码为 UTF-8 后的字节数 / SHA-256 |
|---|---|
| compute | 630,882 / 09e735505d79c9aa6047bc9286c79c0543d818bc101f13a75a251dc376f6b570 |
| report | 302,008 / 502d947a9b729d0c376a47cccc1b1a035267e5c0b9dcea94a2efaff67d83779a |

这两个身份**不是 HTTP 原始字节身份**。compute 有 2,243 个物理行、2,221 个时间前缀；report 有 115 个物理行、114 个时间前缀；各仅首行有 BOM。仅按物理行剥除可选行首 BOM 与严格锚定的 GitHub UTC 时间前缀，未改变 JSON 正文。原返回字符串保留。

下列 SHA 均对应 BEGIN/END 之间的单份原必要正文，不含分隔 LF。每份小于 90,000 B。S1–S5 在 compute 与 report 中的**完整正文字符串逐字相等**；S6–S7 从 compute 完整读取。

| 标号 / 原帧 | 字节数 | SHA-256 |
|---|---:|---|
| S1 REQUEST205_ACTUAL_CONTINUOUS_E_SCALAR_SUMMARY | 37546 | 5ae2bb329801bf38160d05481560c01e4f39f0edbf523388f88ecfbcc4f9c337 |
| S2 REQUEST144_ORIGINAL_C_CUT_TWOJET_SUMMARY | 5830 | 881ffee8e2a5118d1a99c4f441b784ee49ec8c362720628ddd5eedc3790fd5d8 |
| S3 REQUEST205_ACTUAL_DEEP_FAR_SUMMARY | 7325 | 95b5d8b0c1e0d8df2a2dbb0dc0d51a3521625033161b1e26b416a004c732d917 |
| S4 REQUEST205_ACTUAL202_TEN_CONSTRUCTION_NECESSARY | 40776 | ae3f91823c48d134343212175787efb9417e58922b9a9e1cc3b9960cbae4a36a |
| S5 REQUEST205_ACTUAL202_TEN_TWO_PHASE_NECESSARY | 54436 | 5a7122513ac5c469be9d9761009033e72d87edaf914c16dd046f68e9110d8d89 |
| S6 REQUEST205_CLOSED_POSTSOLVE_METADATA | 17585 | c52b1951dab749b3bcd9f44a2dd76846f829b66437ef776ef1ae9ba8370e1ec7 |
| S7 REQUEST205_NECESSARY_RULE_RESOURCE_SUMMARY | 79021 | 96b2e76a729a60e1a95f8a296ecde57d1ff067ffb0415a7f3701baa9cfdc08db |

已读范围包括七正文、全部 112 个 mode 标量记录、112 个数字行选择记录、两个必要未付记录、七角色以及全部返回规则／资源元数据。原成功 tube、全区间矩阵、全部积分／逆像叶与大 raw 树没有逐值搬入对话；它们的实际读取／解析范围和身份按原 reader 字段保留。本文只刊必要研究结论、参数、来源和 SHA，不重刊这些可重算表。

## 3. 新候选点：从 actual202 取字词，不转移其接受

来源是 [R439](R439-actual202-ten-unit-tolerance-complete-final-diagnostics-and-projection-scope.md) 的实际 finite-Gauss 十词：run43784544723，source1a757004b7ebff1f43563bd57b5d13961648d681，compute133029129971／report133029647087。原 Decimal50 十词紧凑 JSON 为 553 B／ba7d7fe3c7fd2599bb7f06863c117b11c6c9f4feb255a160de13023e22129369。

冻结 [R449 adapter](../computations/geometry_20261116_actual202_accurate_ten_candidate.py) 在本次 Actions 中投影为下列 binary64 数字词，并将每个实际 binary64 的准确有理值作为新连续十族参数。各原 Decimal50 有理数均不与其投影有理数严格相等；原完整有符号投影差额已读，定义为 $Q(\mathrm{binary64})-\mathrm{original}$。没有将旧 finite-Gauss 函数、残差、J、FD、接受状态或连续度量证书移入当前族。[S4]

| 坐标 | 实际 binary64 显示 | 新准确有理词 |
|---|---|---|
| p1 | 0.3006078031169812 | 338454297525575/1125899906842624 |
| p2 | 0.23424573424821857 | 8439592011787243/36028797018963968 |
| p3 | 0.33642285729444277 | 757556927375085/2251799813685248 |
| theta1 | -0.07685867368645391 | -2769125553396035/36028797018963968 |
| theta2 | -0.012619205139983169 | -3637238244232963/288230376151711744 |
| theta3 | 0.9310248137664635 | 8385926008702661/9007199254740992 |
| eta1 | 1.0602392679563761 | 4774893172091903/4503599627370496 |
| eta2 | 0.482964410161822 | 2175078337637993/4503599627370496 |
| eta3 | 0.9805969361117931 | 8832431992147443/9007199254740992 |
| xi | 1.0371023093913518 | 4670693574119973/4503599627370496 |

prepare 阶段 exit=0、exception=null、native calls=0。实际 candidate point 为 8,531 B／2fef001d53722b53bf622e4cddf70d327ce47df7612434d56f59b3b683c2fd5b；新 model recipe 为 3,211 B／b02790e6c81082e6c548d9a990a26fd9e88f2ce6d2f18d14e31f4c9251c922a2。

结构模板是 actual180 恢复出的 2,136 B／cc87d9327c33a208ac36e7dadaa5608cc3597e8d9f9bc0bd615631a6681fc6fb。明确复制九个结构字段：core_end、cut_radius、kappa、collar_width、first_transition_width、last_transition_width、first_support、root_choice、collar_mode。模板来源恢复不把旧 actual180 九参数点或其域证书转移到本次十参数点。

前九项仍按 support0/1/2 × power0/1/2 排列；第十项是 support1、power4。准确函数用本次完整 C/cut 语义叶、完整新 DAG 定义；没有用 cut 球中点替换准确叶，也没有把原有限表解释成连续解。

## 4. 本次完整十参数域检查的实际未付范围

本次 factory 为 geometry_20261115_continuous_ten_fixed_power_scalar_factory_v3.py，46,691 B／72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682。其原数学与预算未改。[S4]

| 原字段 | actual205 |
|---|---|
| exact_model_definition_created | true |
| construction_conditions.all_strict_conditions_proved | true |
| nonempty_family_conditions_paid | true |
| full_current_ten_domain_certificate_complete | **false** |
| error / factory return | null / 0 |
| model_definition | 379,215 B／1b1e0d0755d40468f353ef644dc36492a65cb1c7671e832b58968b15c20b24b9 |
| factory result | 20,085 B／b00133407a5f2e3ed87920c7d4cc621da1aec1b88e7f3fc13d1d12fa9a9e29b9 |

controls-off 的 base_domain 在 0.16624391699997432 s 内返回 complete=true：485 个 processed nodes、452 个 passed leaves、0 个终端未决、0 个未访。账本 341,626 B／44404058eeda65e217cafcb865a793b5e10d17c1b78b53ccb36128d4d775f024。它只支付对应基底／非空族的充分构造责任。

保留全部十参数的 requested_parameter_domain 在 301.2905380930001 s 后返回 complete=false：24,405 个 processed nodes、1,810 个 passed leaves、10,594 个 unresolved terminal leaves、16 个 unvisited stack entries。原账本 350,878,184 B／33bbf8c6db4a2dbc08debec7a81327aa0337464f543a01b87f100538dc6580d2；完整原 domain 对象 canonical SHA 为 da29834e1e74f32ff39912c23031b8b62a59c7548d62761f450e2ccc8fc30514。

### 4.1 全部返回的未决／未访地址

下表完整保留 S4 返回的闭区间地址。reader 只在原 endpoint 字符串准确相同处合并相邻地址，所有共端点均保留；没有重新估算科学界。

| 类别 | piece | 原名称／闭 local 区间 | 原条数 | 返回的原 depth 集合 |
|---|---:|---|---:|---|
| 终端未决 | 416 | negative-speed-coast；[729496873/2147483648, 364751085/1073741824] | 10594 | [32] |
| 未访 | 416 | [364751085/1073741824, 1] | 14 | [31,29,26,22,21,20,18,16,13,8,5,3,1] |
| 未访 | 417 | [0,1] | 1 | [0] |
| 未访 | 418 | [0,1] | 1 | [0] |

原完整 a/ap/app 逐叶界没有被必要摘要导出。原 sufficient-certificate 判定失败，可能包含未隔开的有效性；**不能由 complete=false 或终端未决计数证明这些点严格不合法**。同样不能用返回的局部极值包围或 base_domain=true 声称完整十域已过。上表是实际域检查责任，不应与 §7 中物理点采样未返回的逆像地址混同。

### 4.2 原 300 s／depth32／终端条件

原 prove_domain 对每个闭 piece 建 stack，深度优先遍历，每次处理前检查 processed≥65536 或已用时间≥300 s；每个 piece 的初始深度为 0。实际取出的区间要同时证明

$$
a_{\rm lo}>0,\qquad (a_s)_{\rm lo}>-1,\qquad (a_s)_{\rm hi}<1.
$$

若尚不能证明且 depth<32，就二分并保留两个闭半区间；达到 depth32 仍未证时记 unresolved terminal leaf；预算耗尽时原 stack 全部记未访。complete 仅在 stack 为空且 unresolved 为 0 时为 true。每次昂贵 piece_range 返回之后才再检查时钟，所以原 300 s 预算对应实际 301.2905380930001 s 并不矛盾。两个 pass 分别是 controls-off 和 controls-on，sqrt_bits=256；不是删减十参数或自动调参搜索。[冻结 factory 的 prove_domain/main]

## 5. 域未付是否阻止原 BVP：冻结源码的确切答案

沿实际冻结源，答案是**不会另以该域 complete=false 阻断原 BVP**，但域未付责任始终保存：

1. factory.main 先核原 construction_conditions；若该结构条件未付可抛原 ArithmeticError。本次它为 true。factory 写出新定义，然后执行 requested-parameter pass。无 error 时原 return=0，与完整域字段 true/false 分开。
2. geometry_20261116_actual202_accurate_ten_pipeline.py 的 construct 保存 fresh_factory_current_parameter_domain_complete，并明确 fresh_interval_domain_flag_not_used_as_new_BVP_gate=true。它保原返回码／真实定义／recipe／C 来源核对，不要求完整域字段为 true。
3. 同 pipeline 的 bind_current_inputs 先读取 current-geometry/result.json。只有原 completed=true 且 native_geometry_ready=true 才继续组当前配置并调用 R449.bind。本次两个字段均 false，故在这里返回 2，未调用 R449.bind。
4. R449.bind 与实际 driver 的 read_bound_candidate 保结构条件、真实新定义／参数／完整当前来源及原 native 前提；requested_parameter_domain 的完整性只进入原记录。没有新加半径／速度／秩或域 certificate 接受门。
5. coast_center_diagnostic 在 R449.bind 内。本次 bind 未执行，所以**本次没有实际中心速度诊断值**；本文未在本地补算或借别的 run 填值。

pipeline 源为 32,025 B／baa207cc4902ea029b7be21fac7f4a0f878a4075bca733f6a76108a656a076ba；R449 candidate 为 31,509 B／ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38；实际 driver 56cbf3b23d80600121adc2bbeb368e3930d4e5cffe6a2e2a0ab4919cc1018615 保留其原完整 453→450 接口，本次未启动。

## 6. C、原 cut 与深端真正完成的范围

### 6.1 完整原 C 包围与分辨率未付必须并列

S1 的原 producer 为 f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df。实际 result：32,110 B／8de5b7042d6f424737341dc256bb37557b92ff142b7ccf47ff0083b577847b3d。

原 160 个 cell、1,440 个有限 piece 和六 primitive 的完整 finite head 已完成；深端、finite joins、protected join 与全部原 admissible root choices 的包围保留。elapsed_seconds=2327.880233091。原 counts：integral_panels=121832，inverse_cover_nodes=200000，rigorous_analytic_component_integrals=307101。

两个闭查询的**有效包围均完整**；全查询 numerical_work_resolution_complete=false。具体：

| 查询 | 有效闭域包围 | 工作分辨率 | 原未付 |
|---|---|---|---|
| 原 cut point | complete | complete | 0；5 refined nodes，1 head leaf |
| whole-natural-domain | complete | false | 93979 refined nodes；2609 query-resolution fragments；原 inverse-cover node budget reached |

原 stop 字符串为 “Declared inverse-cover node resource budget reached”。全部 2,609 项都是 query-resolution 责任，不是遗漏 query 或 source suffix；原 unvisited_query_suffix 与 unvisited_source_piece_suffix 为空。对应未付账本 5,209,016 B／9964a6e6c2c9d16badaac70709c5fd428bca21a5bae0466df5360f40fe2f6a3a。粗但有效的闭包围没有因工作分辨率未达而丢弃。

原 natural outer radius 显示为 [0.30000000000000715908123386 +/- 6.75e-27]；与原二进制 cut 的差显示为 [7.1701834641e-15 +/- 1.01e-26]。这些是原输出文字，未在此重算。原 cut 准确词为 5404319552844595/18014398509481984，没有换成准确十进制 3/10，也没有重标定 cut 或 warp。

未选择一个确定 deep root 实现、没有把有限 root 表冒成连续解、没有自动付出原 continuous-g 选择或 same-field metric。原六 primitive 大账本 2,079,629,833 B／30336b8ac29623428e33182f88745124d70b2e3d7f510b403ccedea4d17ce873；这里只保身份与原完成字段。

### 6.2 原 cut 二阶 jet 与深端全 112

S2 的 point_twojet_enclosure_complete=true，全部原 point leaf 进入 hull，selected_original_leaf_count=1、span=[0,1)、work-resolution-unmet=0、unpaid_reason=null。cut 文件 5,685 B／38f7ea53d2912b826b4872ca6cec7d24543fe053879387a3a537ee3421b08d60。原 E 显示 [1.0064000 +/- 3.04e-8]；完整 E/Er/Err 的原有理上下界均已读。没有新增导数容差门，也未宣称 cut DN 或有限 selector 导数已证。

S3 完整 112 个偶频率 m=2,4,…,224 的 deep far 行已包围，unpaid_mode_suffix=[]、error=null；elapsed_seconds=0.01151207799966869。原 physical node160／far port159／source cells160..∞，m2 的原 graph 准确为 0；原 theorem Green 上界 9、矩阵扰动界 1/65536 均未改变。完整行流 494,612 B／d68c5547b0323dd2a2bff3fa4087ed5aad831646cabff7c7804519025aa528b9，result 5,856 B／64ec2519759fb7e8858efaf9108018e77ac70e33c9e455ec4e6fdee4749f8544。

这些 deep 行本身不等于有限头全传递、cut-height denominator、非线性 full-DN 或闭面接受；本次后续有限 far 的实际范围由下一节单独报告。

## 7. 全 112 physical far 与 joint 数字行，随后点采样停止

原 sampler 为 geometry_20261115_current_C_pruefer_joint_radial_sampling.py，SHA 32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4；joint helper 为 24c7681c75d5615bcfbfa7b14cdf0155a858bf09578f856433313408b6a16e97。原 sampler result：44,660 B／7e78c78cc97caf54aec062bec8023a5407d00edfd0fbc2899182f971bdb69878。[S5]

### 7.1 这次实际完成的行

全部 m=2,4,…,224 的 112 个 mode 均 attempted/completed/factorized/unit-family complete，not_started=[]、mode errors=null。每 mode 都保 1 个完整 candidate、1 个 inverse leaf 和对应原单位行；norm-unproved=0。成功 coefficient/tube／general row 的全部原误差界保在本 job 临时 ledger；必要读回没有删除候选或只读几个 mode 冒全 112。

全部 112 个 joint nominal 数字行已实际形成，status 均为 actual-finite-joint-nominal-row-formed；failure=[]、not_started=[]。每行实际使用 precision_bits=256、attempt=1、source_panel=10386、piece1368、inverse_leaf=0。原 old-center 诊断对 112 行都是 Q/Pi 中心同时准确为零，但新 joint 行不是该两个独立零中心。

必要例子仅保原已读数字词：

| mode | 原实际 Q | 原实际 Pi |
|---:|---|---|
| 2 | -0.9999999998277826 | 0.000018558951890992953 |
| 4 | 0.9773555604602079 | 0.2116036588471787 |
| 224 | 0.9999999999168174 | -0.00001289826718382189 |

完整 nominal-row ledger 为 1,025,756 B／00ca3154b4ef0edc3c788e5dedac0fb26ac0046760670a91e6d1bdd94ee6c180。完整 general-far JSON 为 1,307,673 B／cba30c2d929c9c7d1c13076391cbe399c07525841df9d70d5b9fc566036992da。全部 112 原行的读取／配对声明来自原 reader；本文不重算单位范数，也不将 nominal 参数盒中心宣称为某个统一准确 C 实现。完整不确定族与到数字词的误差账本仍是其责任。

因此本次已经进入并完成 joint 数字代表步骤；本次停止不能归因为旧 R396 的独立两个中点同零。与 R420/actual197 仅完成 105 个 far、未进 joint 的范围也不同。

### 7.2 真实 far／mu／网格

实际 far word=0.05056158669090205，f64le=f0e68a5235e3a93f；原 cut word=0.3，f64le=333333333333d33f。far 按原规则取严格大于完整 node8 上界的下一 binary64；来源 cell8／segment8／parameter1／panel10385／piece1367。实际 mu word=1.7421589928370103e-17，f64le=705c211ef215743c。这些都由本 job 真形成，没有借旧 run 的 far 或 mu。

计划为 576 段／577 节点、每段 12 步、112 modes，rawNode=[0,72,144,216,288,360,432,504,576]。原所有 RK4 中点／端点参数 words 在实际 field plan 中保留，非旧 source-piece 网格直接冒用；这只是完整计划与实际字词检查范围，不表示该 577 节点 field 已生成。

### 7.3 真正停止是点阶段 work-unit limit

| 原字段 | linear phase | physical-point sampling phase |
|---|---:|---:|
| elapsed_seconds | 4705.123924623 | 272.1988946870006 |
| actual attempts / work units | 2044754 | 1000000 |
| resource checks | 4053992 | 2000234 |
| 原本 job 裁定时间上限 | 11116.349047978718 | 1389.5436309973397 |
| work-unit 上限 | 25000000 | 1000000 |

sampler 总 elapsed=4980.186752515。点阶段捕获的原停止为 WorkStop，message=declared-phase-work-unit-limit-reached，phase=current-C-physical-point-sampling，停止记录内 elapsed=271.5671995570001。阶段最终 receipt 的 elapsed 与停止瞬间字段各自保留，不混为一个值。

实际 actual_point_count=3、actual_inverse_range_count=1000000、actual_coarse_valid_point_leaves=499929、complete_native_field_occurrences_done=0。原 numeric-point stream 为 0 B。phase_finished=true 只是该阶段资源收据已正常封口，不是 native_geometry_ready。

最后存储检查 free=14708715520 B，reserve=2147483648 B；原资源停止字段没有指向磁盘、点阶段时间或规则改变。不能把本次明确的计数上限改写成 SIGTERM、超时或非线性拒绝。

### 7.4 原必要未付记录及未返回地址

S5 返回两个未付行：

- 原 row0：kind=actual-current-C-physical-point-inverse，current_state=null、last_unaccepted=null；原行 SHA c681eb14d82b6a457ceee7c364dddd6dd790a41e79751a3518524d7327d2c358。
- 原 row1：kind=current-C-native-sampling-unfinished；完整 112 far 已完成，unstarted_far_modes=[]，complete_native_field_occurrences_done=0，all_remaining_field_plan_preserved=true，并保原 WorkStop；current_state=null、last_unaccepted=null。原行 SHA 190db318e8f5738109937410a0547d71bcd865f490ec02dbf5dbf27c637233ee。

完整 unpaid ledger 为 2,740 B／5d92947277b33117db4c61c573493b30cf2ae9c5867669f336a2b67f32cbff68，两行都由原 reader 解析。但旧必要 selector 没有选出 point_index、radius_word、role、all_pending_closed_fragments 等完整点逆像地址；本文不能由 3 个成功点、null 或 ledger SHA 推断当前第几个半径／stack。§4 的域地址完整，与这里的读回字段缺口是两个不同范围。

## 8. 下游实际未开始的链，不是失败的数学试探

candidate-binding-procedure-result：1,407 B／946ec7f23f329d958d87bd516ccd0c0925936760e2306a850c26c597b37ea23c，elapsed=0.0019997999997940497、exit=2、error=null、resource_partial=false、child_calls=[]。它原样保存 geometry.completed=false 和 native_geometry_ready=false，然后列出 unstarted：

- current-native-config-binding；
- complete453；
- complete450；
- closed-postsolve。

实际缺少 actual202-ten-BVP-input/adapter-result.json、实际 BVP result.json 和 current-BVP-deadline.json。workflow 明确输出 request205_actual_candidate_BVP_recipe_not_created 后退出 2。不是从静态模板补造一个本 job BVP deadline 或已绑定 recipe。

S5 的 actual_BVP_process_not_started=true、actual_candidate_binding_missing=true、original_launch_identity=null、original_launch_selected=null；design453 和 frozen450 均 exists=false／not_started_not_success=true；live shared client directory 不存在。H、J、完整 FD、原 native/full-DN、338×112 末项、独立 audit、450 checkpoint 都未开始。

S6 的 outer result 为 5,306 B／e9f0b48c4a0789ce4c426c3b276c45e385fecbaebc96674cb42308568ec62338，exit=3、error=null、resource_stop=null、external_interrupt=null，elapsed=0.004304869000407052。其原 upstream stop=actual-BVP-launch-result-absent，actual_deadline_absent_no_template_substitution=true。

所以 R409 radial replay、原 cuff atlas、shared field、metric、reach、独立 held、首次 construction A、材料 B、共同材料查询、精化与显示都没有实际运行。R452/R437 源已接好并不表示本次生成了这些对象。没有可用于续算或几何后处理的 accepted450／末十词状态。

## 9. 原钟、规则、真实收口与 raw 清理

原 namespace 时刻 unix1794798390.1535575；原 science=18900 s、readback reserve=2700 s、job timeout=360 min。实际启动 sampler 时剩余 16105.892678976059 s；明确留 3600 s 给 BVP 后，sampler allowance=12505.892678976059 s，按原 14400:1800 比例裁成 §7 的两时间上限。当前 3600 是 request205 可审的原资源参数；不是在 R449.bind 之后改生成 recipe。BVP 原上限 7200 s 未变。[S7]

binding 时原剩余 11122.98179769516 s，closed 时 11118.703978538513 s。故本次点采样停止不由原总钟到期造成。来源绑定／运行设置仍按原合同排除在 sampler 自身阶段时钟之外；本文不额外声称旧前置所有阶段已由一个全局绝对 kill 包住。

七角色 selection、C、construction、far、sampling、binding、postsolve 的实际 return 分别为 0、0、0、0、2、2、3。各角色保存实际 PID／PGID／startticks，owner 和 child 已返回；quiet 观察中没有 live 或 unknown 后代。完整七 role receipt 索引为 5,486 B／279ba5496f7945f626fc71ee30e4f5c846133502987fcec41b8e98311893da50。

原2700 s规则同步共八次：selection/C/construction/far各1次，sampling2次，binding/postsolve各1次。全部 README_change=null、periodic_sync_failures=[]，没有规则变更停止或运行中科学 checkout 修改。根／题 README 实际基线仍是21bd547f56590b7f2dd279d0297efb289a9b2783和bff8aea253a9e6a7a4fac28d810ac454c5499fec；原普通 pull/rebase/push 范围保留。

七必要读回全部实际 success 后，原 compute 在 **2026-11-16T05:22:49.7536288Z** 输出 request205_owned_temporary_payload_removed，quiescent=true、original_sources_inputs_and_raw_not_uploaded=true。S6 的 raw_cleanup_performed=false 是该 reader 当时尚未执行后续总清理的局部字段，不与最后总 cleanup=true 矛盾。

S5 完整 owned byte scope 为 96,770,094,126 B／14 files，索引 SHA 442e379e097780b74b2aa9a19fecc5ccfdb5c27af2c9f3618d5f8c66ae076f46。其最大 far accepted-step ledger 为 95,028,240,860 B／cf70aa257381b6945a0d715d65d26b5846adb0cc122d4db88881c99f53543022；只是原实际身份与读取范围，不把约95 GB表搬入本文或当逐值独立数学核验。全部 raw 已真实清理，没有保存新 artifact／Release／Git 数据，不能凭 SHA 恢复本 job 未返回的点 stack。

report 把五原主摘要逐字返回，errors=[]，最后按 frozen workflow 在 compute failure 时返回 2。因而两个 failure 与七个 readback success、真实 quiet/cleanup success 可以同时成立；无须用传输故障解释本次科学停止。

## 10. 对后继的具体含义：保留域责任，调整点逆像工作分配需真重跑

[R449](R449-actual202-to-accurate-continuous-ten-fresh-candidate.md) 的新连续点语义与本次准确域未付必须保留。不能因为原 finite-Gauss actual202 接受、base_domain 完成或所有112far形成，就宣称新点是完整合法连续域、已完成 BVP 或近似精确闭面。

本次实证指向原物理点逆像展开的工作分配：1,000,000 次范围工作只返回3点、0完整field。与 [R440 actual203](R440-actual203-complete112-far-and-physical-point-sampling-work-stop.md) 是各自原日志独立得到的同类计数停止，本次没有从203推填原因。

已准备的 [R476/request212](R476-original-C-inverse-work-depth-and-complete212-source-contract.md) 对205来源合同仅把实际 /native_sampling/parameters/sample_inverse_depth 从24改为2，并独立补必要 reader 的八个原字段；这里仅记录其声明的源码／参数范围，不预报运行结果：

- sample_max_nodes=1000000、sample_value_bits=32、precision_bits=256、steps=12，以及原 linear 14400 s／point1800 s、原完整112far／joint行／全部逆像候选／字段误差均保留。
- 原源严排除、闭二分覆盖、有限正的终端粗盒保留；value-resolution=false 不新增 BVP 门。depth2若仍不能证明有限正盒，必须返回原 partial。
- 该24→2是**物理点采样的 inverse work depth**；factory requested-parameter domain 的 domain_budget_seconds_per_pass=300、domain_max_cells=65536、domain_max_depth=32、domain_passes=2、sqrt_bits=256 均沿原205合同保留，原十词、结构宽度、全部准确控制项及完整终门不变。
- C 的 max_depth=48、query_depth=12、max_query_nodes=200000、budget_seconds=3600 与原六 primitive 控制也保留，不能把物理点 depth2 说成降低 C 包围或 factory域证明的数学要求。
- 新 reader 将原 point_index、radius_word、role、actual_error_type、actual_error、all_pending_closed_fragments、retained_original_leaf_rows、complete_point_not_returned 明确选回；它不能追补已清理的205缺失地址。
- 未来 far inverse cover、mu、数字词与 point resolution 可以因真实工作深度不同而变化，必须在新 actual job 全部重生。不得继承205不存在的 native ready、453／450或闭面成功。

本次没有新的实际末解可续；下一实际执行应保原完整科学链，诚实收回新的域／点／native／闭面各自范围。域未付没有被藏进新增通过门，也没有被资源调整自动解决。题 README 所需完整闭面、全 $t$ 强 $C^2$、统一度量误差、reach、held／rigidity 及同目标精化均仍未由 actual205 支付。

## 11. 最小可复现来源与范围证明

冻结 request 的完整源表和原五输入身份决定这次重生；本报告不复制该表。主要实际切点如下：

| 来源 | 完整 SHA-256 | 作用 |
|---|---|---|
| R449 candidate | ee3675ce3465930f2ce32283a468f5fad464639ca6ccda6352f027f00f0c6c38 | 202字词→新准确十点；实际 prepare |
| continuous ten factory | 72c4635e9fe89a88ea5c899369d3fc1cd87c3556e25e1023b7e6066141697682 | 实际新DAG、两次原域检查 |
| actual202 pipeline | baa207cc4902ea029b7be21fac7f4a0f878a4075bca733f6a76108a656a076ba | construction／原native前提／binding控制流 |
| original C producer | f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df | 原完整C与闭query |
| joint physical sampler | 32b0b7e2b02f54f5086b6c9485c1f63bce4702c3a690fed49bbc78d9d690d5f4 | 原112far、joint数字行、物理点工作 |
| two-phase necessary reader | 80c26207dea0d393a102dabba9f1e5ed9580460cc40876d2668975ae9499af1f | 本次未起453/450与原采样必要范围 |

范围论证如下。S4 的 actual factory身份和实际 recipe／definition收据，将 §4 的域记录绑定到 §3 的新准确十点；原 factory return逻辑证明 complete=false本身不产生这里的error。S5 保存 physical sampler 的 actualresult／源身份、原WorkStop和两个native-ready字段；原pipeline条件据此唯一解释binding未启动，再由实际missing BVP recipe和S6缺upstream result解释下游未起。S7的原角色收据、七读回success与quiet／cleanup事件完整支持生命周期结论。五个双处出现的主正文逐字相等，只支付运输与选择一致性；它不加强任何数学条件。

以上只使用原记录、原字段选择与可核源码控制流。没有用额外采样、重新计算、隐藏失败、降低门槛或从摘要身份推断未读大矩阵。本文必要结论可以由固定 source/run 与原 Actions 日志重现；未返回／已清理的原数据范围如实保留。
