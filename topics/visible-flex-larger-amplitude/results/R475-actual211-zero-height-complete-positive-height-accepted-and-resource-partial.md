# R475：actual211 的完整零高返回、首个正高真实接受步与后续资源未付

作者：AI（amplitude；根线程统一发表）  
日期：2026-11-16（UTC）

**可信度：数值证据。** 本文完整读取本次公开 Actions 的必要结果及原错误、规则和清理收据，登记已经实际发生的有限计算。来源／控制流的条件说明不把有限数值结果升级成准确连续导数、全局几何或原 full-DN 接受证明。没有本地科学计算、补跑、独立 fixture、阈值修改或新的数学接受门。

## 1. 本次实际结论

Request211 真正运行了 R466 的 recorded-factor 收缩、R471 的有条件零非线性通量省略和 R474 的有条件零系数线性乘积省略。原 112 模、576 段、226 状态、224 形状列、两个 mean、原 noJ primal／root／RK、当前完整 R273 校正及所有末端要求保留。

本次先在零高 $s=0$ 完成原 native 调用，原返回 `converged=true`、`residual=0`，请求耗时 **284.14534865100006 s**。随后在首个正高 $s=1/64$，原迭代 0 的完整 current576 withJ 求值完成，完整 R273 线性校正返回；原第 0 档、步长 1 的非线性 trial 被真实接受，记录的原范数从 **196395.0911309943** 变为 **5181.565456345417**。

这个正高调用没有收敛返回。接受步以后，迭代 1 的后续局部方向计算在 **tailStage=105、tailRawCell=1、tailRawSegment=4** 记录 `finite-trace-direction-resource-budget`。总 owner 按原 **18000 s** 科学时钟结束；子进程返回 `-15`，wrapper 返回 `124`，实际 elapsed 为 **18000.253912736 s**。原规则没有变化，未因规则变更终止科学。

因此：

- 零高 native 请求已经原样收敛；它没有请求最终 endpoint Jacobian 或 audit。
- 首个正高请求确有一次完整当前校正和一个真实接受 trial；这不是根据模型下降或计数推测的接受。
- 正高 native 完整响应、端点完整 $338\times112$ 返回、原终审、boundary FD 和 coupled full-DN 尚未付；没有把程序完成、helper 完成或 QR 返回升格为这些接受。
- 本次停止是原资源范围，不能改写成正高 trial 的数学拒绝、所有允许步长失败或该问题无解。
- 原必要读回及独占进程静止完成后，当前 job 原临时 payload 已真实清理。本文不保有可继续积分的完整状态，也不能据 checksum 恢复已删数组。

## 2. 唯一实际 run、原帧及读取范围

| 项目 | 本次实际身份 |
| --- | --- |
| 公开 source head | `7e62fb22bff15bfe53e1481b4e7ba21d2f905786` |
| run / attempt | `43810051801 / 1` |
| compute job | `133109494332`，结论 `failure` |
| report job | `133235382702`，结论 `success` |
| 工作流 | `.github/workflows/visible-larger-public-six-control-zero-eliding-contracted-trace-r273.yml` |
| 请求 | `public-six-control-zero-eliding-contracted-trace-r273-request.json`，80994 B，`5985662c19540f55c9bf1d2137ebc568db9d70bd026ffddd4bc89f0d0112a4ed` |
| recipe | `actual119-batch3-zero-eliding-contracted-trace211-lambda0p001-recipe.json`，18761 B，`1a949e873bfb4ef8e4cc87a132911c023e5ba8318c8979a45ef2f3218d9e29a7` |
| 实际 reader | `root_20261116_six_control_zero_eliding_contracted_trace_r273_scalar_readout.py`，SHA `6131ffcb23042cc8be445ccdc46c983fed74205c560f2a18b18a193a8a07fe76` |
| 原必要正文 | **81156 B**，`5994fe81eb2ce1076e90746989189e2bf0fad718ff0b926d7be4b36237375088` |

正文长度不含 frame 分隔换行。原 frame 为 `BEGIN_REQUEST211_ZERO_ELIDING_CONTRACTED_TRACE_R273_NECESSARY_SUMMARY` 与对应 END。compute 与 report 的这一正文逐字相等。compute 科学步骤 11 失败，必要读回 12、条件清理 13 均成功；report 的成功只表示这次必要结果已按规则返回。

每个终态 job 日志只取一次。连接器返回解码文本的 UTF-8 重编码身份分别是：

| 连接器返回文本 | 字节 | SHA-256 |
| --- | ---: | --- |
| compute | 224563 | `f21928176752e5dc014c37c1d4cdd27231c1e9162605a9b14dce7ae7529a98da` |
| report | 168404 | `2ca2359ad086a180961694309e1f848682d0c05c7e63ac64dcd6ed2bd7358139` |

这不是 HTTP raw 字节声明。读取时保留上述原文本，逐物理行去单个行首 BOM，再剥官方 timestamp 来识别 JSON/frame；未从运行中日志截取科学结果。report 身份事件原时间为 `2026-11-16T10:25:32.6106156Z`。

本线程完整读了全部返回的来源与政策、原 actual H、有限初猜与 preflight、唯一 native response、全部 15 个原 trace 事件与唯一 trial、height-path 状态、两次累计统计、每个 engine 最后位置、完整一个 R273 校正摘要及其全部诊断、原 selected identities、规则／owner／清理收据。原大矩阵、完整 root tape、逐角原场、完整 checkpoint 数组、129248 行 exact ledger 和完整 H 原输出没有再刊入 Git。原必要摘要已经完整读取，不因本文不重复大数组而改称未读。

`summary_complete=true`、`transport_complete=true`、`errors=[]` 和 `necessary_original_error_text=[]` 是必要 reader 的原值。后一个空列表不抹掉 native completion 内真实的资源错误；后者在 §6 单独保留。原错误 stack 只按 reader 返回必要前缀及完整身份，本文不声称读到了未返回的 stack 全文。

## 3. 实际源闭包与原输入

本次隔离临时源码生成和绑定成功，真正执行目录为：

`$RUNNER_TEMP/visible-original64-zero-eliding-contracted-trace211/runtime-source-views/computations`。

源码 receipt 为 74847 B／`c21861e9b4d30869b07f345472e0b3b51586a57d589233251013d26ecab9a3dd`，schema `request211-actual-private-source-views-v1`。147 个真实公开文件被复制；21 个临时 source views 包括原 210 的 11 个历史输出和本次 10 个当前输出。历史 11 件在 Actions 由原 208 文本重新生成，不冒充 Git 中存在的公开文件，也不充当当前入口。

全部 168 个来源的 canonical map 为 19633 B／`4d4773f6bfd13fbd3d62f2e6b368f6590cbeac27fa52523aae76b9c114030f20`。实际 public/private request、recipe、plan 各自字节一致；plan 为 81398 B／`4d19708494cf1f33b8fcbe47053769b9fe7653d6cc33624a7e3126db77787fda`。实际 imports 使用 private HERE，真实 `GITHUB_WORKSPACE` 保留。来源生成没有运行科学模块。R472 所记录的旧 210 缺失递归 import 不能移作本次原因：本次已经实际走到完整 current576 校正与原 trial。

主要实际计算源如下；同名完整 SHA 是来源，不是计算正确性或性能证书。

| 角色 | 完整 SHA-256 |
| --- | --- |
| 实际 loader | `9ca91d9f3efac6d944d81545b6ad89f1b33eb07a942598e35065319782243d13` |
| R474 flow | `1a5ce3f7b2af7016b2752af1654be68d1d708c3b4cc6660fbec33bb468f09ae1` |
| R471 variation | `d4f2f32b61c084a67615ebb26b88b62c7d18de06056f09f5f68f86efa0f143e0` |
| R466 contraction helper | `2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59` |
| R471 zero-flux helper | `e6ce93089c0ee03324fbaeb86ced15b1852b3ad498b322c4adfd959d7c869fde` |
| R474 zero-coefficient helper | `eb487b2dff111d0af543a722c0882d28f7408eeb61e4e25559cef147d2e16e02` |
| 原 root | `cbf753894f32e3460e646725757cbaed1f227b166f9693dda54829ee46ecfc88` |
| 原 split | `a47df10fcde701c6c657b496d003dbe837eecfca4a51abaf40d6f7c387049372` |

原 capacity、root observer、matched split 也在完整 source map 内。原 root/RHS primal 恢复、loaded root/split、原磁盘源码未改均为本次 source manifest 的实际记录。R466 对象仍是 R465 局部 constant-defect nominal coefficient system；数值收缩没有宣称与原 195 所有 IEEE 字词相等、一般缺陷导数为常数或舍入误差已严格包住。

四个原输入仍为：

| 输入 | 字节 | SHA-256 |
| --- | ---: | --- |
| accepted | 2614352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | 4220043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail anchor | 6815 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

本次原六参数字面仍为：

```json
[0.41654476801167684,0.23884336093393582,0.5270922473095916,-0.13437878055563054,-0.005765450212224129,0.4141025261683763]
```

$\lambda=0.001$，原前三 active、后三 frozen。原 $M=112,N=2048$、699 个初始 mesh 节点保持；初猜 `initial_collocation_max=0.0000068749454041621035`，`success=false`、`new_coupled_finite_acceptance=false`。实际初猜压缩件为 2476282 B／`28d02e1d254ec87e84f8d6ca4ec32ab554594764f28568d54a2daa354956cc07`，不是原输入 prepared 文件身份。

原有限 preflight 通过，未增节点；它只覆盖实际原 RHS 所查询的 nodes、midpoints 和两个 RMS 单元内采样分数，不是全连续域证明：

| 原查询类 | 最小 beta² | 实际 $s$ | $a$ | $a_s$ |
| --- | ---: | ---: | ---: | ---: |
| nodes | 0.0022538385815712436 | 2.262368580603409 | 0.30861147192664384 | -0.9974201152840357 |
| fraction 0.5 | 0.002267325049764346 | 2.2641940822709667 | 0.30679069544928395 | -0.9973944426775293 |
| fraction 0.17267316464601146 | 0.002245239130645116 | 2.2629990109034166 | 0.30798266870607605 | -0.9974170601308882 |
| fraction 0.8273268353539885 | 0.002259211840830444 | 2.2621383298889284 | 0.3088411286208252 | -0.9974201152840357 |

各项原 $\phi=0$；两个长小数是采样位置，不是 RMS 残差数值。完整 H 的 112 个原词已经读取；其 `<f8`／C order 身份为 896 B／`d19e25eabad7f2c84ecdd10580caee1c3b41ef9d1e0a1a3ae07c58486277eced`，无负零列。这里保身份而不重刊该可重算全向量。

## 4. 零高和首个正高的原控制流

height-path 使用同一真实 worker 和 owner。原政策从零开始，首正增量 $1/64$，接受后的增量乘 2、上限 $1/4$、最多 64 个请求。零高和中间请求 `jacobian=false,audit=false`；最终原 $H_*$ 请求才索取完整 endpoint Jacobian。首次正高若遭原数学拒绝就停止，不进行额外反复减半。原 native 每请求最多 32 iterations、每 iteration 原 10 trials，容差 $2\times10^{-9}$ 均保留。

零高请求的 H 是完整 112 个 $+0$，二进制身份 896 B／`d54f02b97ed5bc2a642756268b41d4b8f7a077e73224e1580d22436834a14db5`。本次不是以对称性直接跳过初始全 tangent：原初始 withJ、两个 mean 和 tangent predictor 都实际执行。iteration 0 的事件为 elapsed 277857 ms、norm 0、minA=minD=1；随后 `tangent_predictor_ready` 的 `maxChartCondition=385639393697279100000`。原 response trace elapsed 为 284107 ms，而 Python 请求包耗时为 284.14534865100006 s；两者是各自原计时口径，不能互换。

唯一正式 native response 中，112 个 height/slope/second 的 canonical JSON 各为 225 B／`64c19f2662ac257bca17a036d0c4809671b09bf950df1d6c82b42461fabe7e56`；meanSlope **0.08000000000000027**、meanSecond **-1.866666666666673**，两个 correction 为 0。原 cut radius 0.30000000000000004，E 1.0064、Ep -0.2986666666666687；minLeading=minD=1、endpointFullD=endpointPhi=0、formalCurvature=1.8488889638984891。这些是原有限返回值，不是准确 collar 或完整曲面审计。

该 response 的 `full_J_present=false`、`full_J_identity=null`、`audit=null`。存在一个 finite Fourier/depth checkpoint，必要返回的 canonical identity 为 266315 B／`70ff2c3b025669df9e07124ecd3bc46a6830b5a756c175c700c9ca4a87922520`；未导出或重新读取其完整数组，JSON 身份也不宣称保住序列化前的全部负零。

第二请求是真实 $H_*/64$，`requested_H_identity` 为 896 B／`fb6da818e40bcdaa0bc57ceb9a86d5ae2845132054389a2eac73ea866283a032`。warm predictor 使用原完整 nonlinear shooting tangent，记录 `maxRelativeCorrection=3.844494357362678e+252`，仍只作为初猜，原 residual/guards 决定结果。没有因这个很大的诊断数另加拒绝门。

原已观察事件链为：

| call / iteration | 原事件 | 原 elapsed_ms | 原值／含义 |
| --- | --- | ---: | --- |
| 1 / 0 | iteration | 277857 | norm 0，minA=minD=1 |
| 1 | response | 284107 | converged=true，residual=0 |
| 2 / 0 | iteration | 14240820 | norm 196395.0911309943，minA 0.9315748352465438，minD 0.9999646599422697 |
| 2 / 0 | correction | 14262174 | 同原范数，chartCondition=null |
| 2 / 1 | accepted-trial-recovery-only | 14438964 | norm 5181.565456345417，来自 iteration0／trial0／step1 |
| 2 | failure | 原事件无此计时字段 | finite-trace-direction-resource-budget |

`accepted-trial-recovery-only` 只恢复已经实际接受的 trial 事件，不伪造完整迭代 1 withJ 返回或完整请求 response。

唯一 trial 原行是：

| call | iteration | trial | step | baseNorm | kind | trialNorm |
| ---: | ---: | ---: | ---: | ---: | --- | ---: |
| 2 | 0 | 0 | 1 | 196395.0911309943 | accepted | 5181.565456345417 |

该行原 error/stage/rawCell/rawSegment/stageInputSHA256/stageInputBytes 全为 null。没有把后来的错误位置写回这个成功 trial。call1/iteration0 的 0…9、call2/iteration0 的 1…9、call2/iteration1 的 0…9 均无原 trial 记录；这表示未观察到对应 trial，不表示全部被拒。未观察到的后续 iterations 不补表。

## 5. 已付的完整 current576 R273 校正

唯一 observed correction 位于 `call-0002/iteration-000`，native_call=2、iteration=0、snapshot_sequence=0。原 `snapshot_completed=true`、`linear_direction_returned=true`，不是由 helper 计数推断。

| 原对象 | 返回身份 |
| --- | --- |
| 当前状态 | `e169f6cd2d92427fdef08f021ea77b2f328a554a2db8ca1f80ea062dc0fe2fbe` |
| 当前 norm binary64le | `01e3a2ba58f90741` |
| 新矩阵身份 | `84a3c55d4edeb530710d704476a81c36b4f869cb85d2e4b7880c7becad5b5e7f` |
| native delta | `abd9467c676ba31744c87b041b02675a8b997adb8faef0736012e519ff5eb456` |
| formed model | `08ca2efeb9ea735b5864759e6466c7c3973321c535827db0f156b23df9327097` |

完整 QR 原 status=0、signal/error=null，stderr 0 B／空文件 SHA。diagnostic_completed 和 linear_direction_computed 均 true，$\eta$ CLI 原词为 `"1"`，诊断耗时 **19.823707264000404 s**、maximum RSS **830272 KiB**。

完整 factor 报告 **129248 rows × 129248 columns**、258496 augmented rows、576 stages、577 nodes、224 block width、577 penalty blocks、1153 QR calls、1152 formations、129248 pure constant rows。实际 factor＋constant **464891392 B**，与原 expected 同值，小于原 cap 2147483648 B；formation-underflow-to-binary64-zero=0。factor 耗时 19.123108665000473 s、最小绝对三角对角 1.1915065260525806。其 dtype 名称为 `float128`，但该 job 实际 `significand_bits=64`、itemsize=16；不能把名称写成 113-bit 四倍精度，也不是准确有理 QR。

原 exact affine 读回完成 **129248 rows／576 stages／28901488 original product positions**，使用同一最终 binary64 delta。最大值原读数和地址：

- affine：global row **9073**、node **40**、row **1**、Q mode **2**，原 sigma 字 `18343b692928e33e`；绝对值显示  
  `2.080989969356976325294974117582200167249079456913236239274670783E-1`，signed 为其负值。
- stored base：global row **13326**、node **58**、row **222**、Pi mode **111**，原 sigma 字 `17355deb870d323f`。绝对值显示  
  `1.963950911309942815828591424238622203439184896080448259729949171E+5`，signed 为其负值。

上述十进制只是原 exact readback 的显示；完整 witness 身份分别为 `2809df705344fcf3800ca9ca12d6adeb03e59b5fa4979812f6f80acc24b910ce` 与 `5cbd5339e690a2634b9ee44e80644cb649b871ba757a3f3a37f9fe40ff62cd83`。完整 exact ledger 为 4968605 B／`2cbbc231a3fe2e9781b785053b95e40a17241393a969ad8e7612cfb147dba19b`，在 Actions 内处理；主端没有逐行接回。它涵盖实际 unscaled cut/stage/far rows 后除以原 sigma，不含 $\eta$ penalty rows，也不新增 native trial 门。

原 formed-model 数值诊断全部保留必要值：

| 量 | 原 longdouble 显示 |
| --- | --- |
| base objective | 46495115297.14168885 |
| objective | 0.04429308343276567084 |
| model drop | 46495115297.097395767 |
| formed residual 2-norm | 0.22078455579084220437 |
| formed residual infinity norm | 0.20809899693569761938 |
| full unpreconditioned model gradient 2-norm | 1.0273267970073187821e+22 |
| factor variable square | 3.3199235930748789415e-12 |
| constant square | 0.08858616670758600262 |
| formed energy minus factor energy | 1.5462541546506147414e-10 |
| factor triangular residual infinity | 1.2026282727693876854e-06 |

这些都是相同 formed f64 coefficients 上的数值 longdouble actions，没有准确最优性或原 R273 posterior certificate。特别大的 model gradient 不隐藏；也没有以它另造原 native 接受门。非线性接受仍由 §4 的原 trial 判定。

原闭合 payload retirement 删除 **1751 files／709355693 B**，retirement_error=null，位于完整 delta 验证和记录之后。它不同于 job 结束的总清理；必要 reader 明示未重新打开已退休矩阵／factor。完整当前 J 的 Actions 范围已付，不等于主端已逐元素读取 J。

## 6. 真正中断位置、原 null 与未付职责

第二调用的原 native-completion record 为 `kind="failure"`、`original_return=null`，包含：

```text
Error: finite-trace-direction-resource-budget
tailStage = 105
tailRawCell = 1
tailRawSegment = 4
finite_trace_variation.resource_budget = true
original_root_trace = null
```

stack 的完整身份为 **2130 B／`1e88dc9ab2e0fe91ba995c1d9079376fdf2b972955af5c730febaa122663bfad`**。必要前缀显示调用从 variation 的 `resourceCheck`、`residualAndGramDirection`、`finiteRootDirection`、`completeFiniteRootTraceJacobian` 到 flow 的 `fromCaptured`；最后文件路径被原 selector 截断，`text_not_returned_in_full=true`。没有借文件名猜一次浮点失败或把资源错误改称域错误。

对应累计 completion 表的 `call`、`snapshots_completed`、`directions_returned` 原值都是 null。其 directory 和原 request 明确是 call-0002，另一个 current-correction 行证明 iteration0 真完成；本文仍保留这些原 null，不用新值覆盖一个没有最终 summary 的调用。最外层 `current_R273.client`、`external_calls`、`final_statistics` 也为 null；不能由两次 checkpoint 统计伪造最终完整 statistics。

height-path 留在 `phase="original-request-in-flight"`、`complete_endpoint=false`、`last_converged_s=0`、`last_converged_call=1`、`original_full_DN_accepted=false`。其持久文件中的 `resource_partial=false` 是中断前留下的原值；最外 owner 实际 `wall-clock-budget-partial`、elapsed、TERM 和 native resource failure 才给这次终止范围。本文同时保留两层原状态，不把旧 inner false 当作“没有资源停止”。

如下各量本次没有被付：

| 原责任 | 返回范围 |
| --- | --- |
| 正高 $1/64$ 完整 native 收敛 response | 没有；只有原已接受 trial 与后续失败 |
| 正高 iteration1 完整当前 J／下一 R273 校正 | 没有完整返回；只记录具体局部中断位置 |
| $s=1$、原完整 $H_*$ endpoint | 未到达 |
| 完整 $338\times112$ endpoint response Jacobian、两个 mean 导数返回 | 未到达；不能由累计局部 J 数推断 |
| 原 endpoint 独立 audit | 未到达；zero-H 的 audit 也没有请求 |
| boundary FD / FD groups | null |
| original full-DN／accepted result／outer history／full-result identity | 全部 null |
| all-original-full-DN evaluations／banded-solve reports | 空列表，不能改写成功 |

本文没有追加“全部解析 J”之类原合同没有的接受门；它只登记本来要求的实际完整返回／FD／audit 未出现。有限 trace tangent、recorded-factor formal map、连续准确导数和 IEEE rounding-map derivative 的责任仍按各原来源区分。

## 7. 累计统计：真实执行了什么，没有证明什么

两次统计来自同一组 8 engines，第二次累计包含第一次；**下面两列不能相加**。每个 engine 的 `first_stage` 依次为 0、72、144、216、288、360、432、504，`stage_count=72`。原 `original_all576_stages_addressed=true` 是完整分布／布局责任，不把中断的下一次完整 J 填完。

### 7.1 原 root 与 local J

| 原累计计数 | call1 返回处 | call2 失败处 |
| --- | ---: | ---: |
| root_returns | 27772 | 60656 |
| zero_update_returns | 27772 | 28616 |
| normal_returns | 27772 | 60656 |
| fallback_returns | 0 | 0 |
| original_root_evaluations | 27772 | 160114 |
| original_line_trials | 0 | 49729 |
| differentiated_accepted_updates | 0 | 49726 |
| complete_local_jacobians | 27772 | 60655 |

call1 成功更新数 histogram 是 `[27772,0,...,0]`，总 30 项；call2 是 `[28616,17286,11819,2935,0,...,0]`，其余 26 项原值 0。不是 60656 个不同状态，也不是 60655 个完整 stage maps。原 root 成功返回最大 accepted-updates 29、iteration30可在最后接受后 throw 的政策不变。

### 7.2 R466 recorded-factor 收缩

call1 下表全部为 0；call2 的累计值为：

| 原计数 | 值 |
| --- | ---: |
| calls_started / calls_completed | 49726 / 49726 |
| preassemblies_started / preassemblies_completed | 49726 / 49726 |
| contracted_updates_completed | 49726 |
| explicit_original_fallbacks_started / completed | 0 / 0 |
| complete_direction_columns_returned | 11138624 |
| exact_backsolve_defect_components | 5619038 |
| exact_nonzero_backsolve_defect_components | 5612105 |
| backsolve_defect_projection_changed_components | 5565065 |
| nonzero_backsolve_defect_projection_lost_components | 0 |
| backsolve_defect_projection_overflow_components | 0 |
| exact_zero_backsolve_defect_updates | 0 |

两处 fallback_reason_counts、missing_counter_scopes 和 unfinished-solve/last-fallback 列表都为空。准确 dyadic backsolve defect 先形成再显式投影，非零项没有在本次投影中丢为零或溢出；这不支付 contraction roundoff bound，更不把一般可变 defect 导数设成常量。原 primal 和 zero-update root path 没有被此收缩改动。每 update 全 fallback 历史并未记录，本文不重建。

### 7.3 R471 零非线性通量

| 原计数 | call1 返回处 | call2 失败处 |
| --- | ---: | ---: |
| calls_started / completed | 27772 / 27772 | 60655 / 60655 |
| actual_zero_trace_candidates | 27772 | 27772 |
| certified_zero_dflux_calls | 27772 | 27772 |
| original_angular_fallback_calls | 0 | 32883 |
| sparse_direction_entries_checked | 702964864 | 702964864 |
| complete_angular_rows_checked | 56877056 | 56877056 |
| complete_shape_direction_pairs_checked | 6370230272 | 6370230272 |

call2 的实际 fallback 两原因分别为 `actual-empty-unsupplied-successful-trace-unavailable:32039` 与 `actual-shape-state-not-zero:844`。资格不符走原完整 angular loop；这是原求值路径，不是数学拒绝。

call1 八个 last_observation 均为 `original-positive-zero-dflux-retained`、decision `retain-original-positive-zero-dflux`、completed=true；angle/direction_pair/sparse_row/reason/detail 原为 null。call2 八项均为 phase `actual-trace`、decision `original-complete-angular-loop`、reason `actual-empty-unsupplied-successful-trace-unavailable`、completed=true；angle/direction_pair/sparse_row 为 null、detail 为原空字典。共同 mode_count112、angular_rows2048、shape_columns224 没有缩减。

各 engine 的 started/completed 对在 call1 为 `[3472,3468,3472,3472,3472,3472,3472,3472]`，call2 为 `[10416,8575,6944,6944,6944,6944,6944,6944]`，每项两计数相等。它们只是各 engine 最后已经完成的该 helper 调用，不能排除下一层 root direction 正在中断。

### 7.4 R474 零系数线性乘积

| 原计数 | call1 返回处 | call2 失败处 |
| --- | ---: | ---: |
| calls_started / completed | 27772 / 27772 | 60652 / 60652 |
| finite_input_calls | 27772 | 60652 |
| original_complete_loop_calls | 0 | 0 |
| actual_A_entries_checked | 1405929728 | 3070446848 |
| actual_used_T_entries_checked | 1393487872 | 3043274752 |
| zero_j_terms_skipped | 1393526896 | 1422070894 |
| scalar_products_skipped | 312150024704 | 318543880256 |
| retained_j_terms_completed | 12402832 | 1648375954 |

两处 fallback_reason_counts 和 missing_counter_scopes 都为空。每个 last_observation 的 rows226、shape_columns224、phase `zero-eliding-complete-loop-returned`、qualification=true、row225、shape_index223、j_action `skip-actual-zero-coefficient`、j_completed=true、decision `actual-zero-coefficient-elision`、completed=true；input_index/first_nonfinite_input 原为 null，`current_inner_columns_not_individually_recorded=false`。

call1 八项 started/completed 与上一小节相同；call2 为 `[10416,8572,6944,6944,6944,6944,6944,6944]`，每项仍成对相等。R471 与 R474 调用数不等，不能强行补成同数；它们位于不同实际调用接点，当前中断也没有完成后续全部层。

R474 只在实际 A 与实际使用的 T 前缀有限时省略 A 的两种零，原非零乘后加及 j 次序完整保留。有限 inputs 不表示每个中间乘积／累加都有限；其原 scope 只承诺条件下有限输出词和非有限类别，不冒 NaN payload 逐字相等。当前计数不测量耗时份额、不证明完整 J，也不新增 output-finiteness 门。

两次完整统计对象 canonical 身份为 36830 B／`b4f13cd3e39908b84d0c0fca574d9051041095c187244e37eff1f8edf92ba564` 与 38981 B／`acd16b5ddbc7f6eed88d045118336db58433ed1d96f605aabc0068db3c71e51c`。必要 reader 只是把原 integer counters 按实际 engines 求总并保每 engine 最后观察；没有重跑科学。

## 8. 原规则、必要范围与实际清理

原规则 runner 从 **05:25:26 UTC** 到 **10:25:26 UTC**，science_returncode=wrapper_returncode=124，README_change=null、`science_terminated_for_actual_rule_change=false`、scientific_checkout_modified=false。7 个同步轮启动，periodic_sync_failures=[]；原 argv/budget preserved。原 `partial_scientific_files_not_removed=true` 描述规则 runner 结束时没有抢先删除科学现场，后续独立必要读回才付清理条件。

必要 reader 前、后均读同一个 process receipt **12847 B／`a4ee813dba1745a7d6ff1450a775d84968c0a6ef082044867fe397c8491e154c`**。两处 owned group before/after 都是 members/live/errors 空列表，quiescent=true、signals=[]、launcher_reap_claim=true。没有给 parent 共享 PGID 发信号，也不要求共享 PGID 全空。

原条件 cleanup 事件时间 **2026-11-16T10:25:27.3894688Z**，记录：

- schema `request211-conditional-owned-cleanup-v1`，实际 run/source 如 §2；
- `complete_readback_and_quiescence_authorized=true`、`removed=true`；
- scalar 和 source-view generation outcome 均 success；
- `original_rules_parent_quiescent=true`，parent 观察为 null；这按原同 PID/start-time 缺席责任解释，不伪造整个共享进程组空闲；
- parent receipt SHA `904bc3211b762443b7a80ce777f7f61f5684cb82825f892f759be8b17a8c13c5`；
- readback marker SHA `b82e0597ffec643fbea3094a9d0806b8423ba7044682a42488d3a043b015c6cb`；
- `no_artifact_release_or_git_raw_upload=true`，cleanup 不是原科学接受门。

必要正文小于原 90000 B 硬上限，未分片／编码大科学树；本文亦不把 raw 数组、矩阵或 exact 行账本作为可重算输出搬回 Git。原 stdout-stderr 为 5827 B／`a19d50921528ede498bd79bd9571ae63d4e4beb0db8b8255fdc15532c6c46446`，native stderr 和 QR stderr 各是**实际存在且读过**的 0 B 空文件，不能把未生成文件冒充空。

若要后继继续求解，必须明确真实初猜输入及新运行，不能从本文的接受 trial norm/身份造回末态。Request224 的来源改进若另行发表，仍须从它明确绑定的原输入真实重生；不继承本次接受状态、J、QR、FD 或时钟。

## 9. 与已有数值证据的边界及下一未付工作

R467 的 actual208 零高请求耗时 **5774.443653623 s**；本次记录为 **284.14534865100006 s**。这是两个实际 run 的同类原请求读数，不是微基准。两次没有 dFlux、linear、root、内存或系统调度的独立分项计时；本文不把差值全部归给某 helper，也不承诺下一 run 的速度。零高虽已有快速接受，内部原完整 tangent/predictor 仍实际执行，不能据零 residual 删掉 J 或两个 mean。

本次最重要的新增实际范围是：正高首请求已经越过完整 current576 J 和 R273 校正，并有一次真实非线性接受。剩余主要数值责任仍是同一完整原问题的后续当前 J、原迭代收敛、最终完整 response/audit/FD/full-DN。source 层的结构省略可以独立证明与接线，不能把那些条件证明当成本次未完成部分的数值结果。

## 10. 来源

本题目录内的主要可核来源：

1. §2 冻结实际 source 下的 Request211、recipe、workflow 以及唯一实际必要 reader；run `43810051801` 的 compute/report 必要帧和原清理事件。
2. `results/R471-zero-nonlinear-split-flux-finite-trace-fast-path.md`、已刊 R473 的有限输入零系数等价证明、`results/R474-finite-input-zero-coefficient-linear-implementation.md`；R474 已刊 `9ff15fddedfa1be31f9e486b225c4a64c9f6e7fd`。
3. `results/R465-recorded-factor-backsolve-defect-and-complete-column-contraction.md` 与已刊 R466 原实现；它们的 formal-map／误差责任没有被本文改变。
4. `results/R467-actual208-contracted-trace-resource-partial-and-complete-readback.md`，25544 B／`c8709222176ffe7845a37fb1ad8f429d5c61af058f79c99c783edd72d6814597`，已刊 `2e85e46cf5771a4764d1ac15a25da806e3e1f36d`。
5. R472 实际 210 缺依赖结论及 Request211 的显式递归来源补充；本次 private source view 的成功范围只按 §3 的实际 receipt 判定。
