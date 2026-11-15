# R415：actual196 的持久 128 原结果、SIMD 后续未完成及必要读回入口错误

AI 辅助研究记录；日期：2026-11-15。本文只读取本仓库公开 Actions 的本次原日志、已发布请求与源码，不进行本地科学运算、重放、编译或导数计算。正文刊登必要研究结论和来源；可重算的大数组、原事件全集不另存入仓库。

## 1. 本次结论与可读范围

actual196 在持久 binary128 owner 中实际形成 1 个方向、评价 1 个 trial、接受 1 步，完整 129248 行／576 stage 的末范数为原词

$$
9.68582474751023176032080482454992093\times10^{-11}.
$$

原 owner 标记 `below_original_tolerance=true`，停止原因为 `shooting-tolerance-reached`。独立 fresh replay 完成，全部残差与全部 226 态输出的 binary128 word 均与 owner 相等。这些是本次桥事件直接返回的结果，不借用 133、160、190 或 192 的原输出。

后续桥记录同时明确：`complete_stage_maps=false`、`complete_boundary112_response=false`、`complete_mixed_endpoint338x112_readout=false`，`native_accepted=false`、`fullDN_accepted=false`。其 `complete_original_C_based_physical_program_audit=true` 是本次返回的汇总标志；审计的完整 stage／query 计数、极值、失败与未访明细只留在临时组件正文，未被必要读回取出。因此本文保留该原标志，但不声称已经逐值核过完整审计，也不把它覆盖为 owner 层原本为 false 的 `original_geometric_final_audit_complete`。

计算 job 的直接失败发生在科学 step 返回以后：必要 reader 仍要求请求号 190，实际请求为 196。它在读组件正文之前抛出 `ValueError: Actual independent request190`。这是确定的元数据入口错误，非 90 KB 超限、非本次全局墙钟耗尽，也不是完整原问题已接受。报告 job 成功只打印“必要摘要缺失”。具体 stage 编译错误、实际 SIMD backend 和真实吞吐没有返回，不能根据静态 ADL 风险补填本次原因。

## 2. 唯一真实运行及读取身份

| 项目 | 原值 |
| --- | --- |
| 源 commit | `4677faa0966475d17e10b20b75f0234c62fe3768` |
| run | [43770686357](https://github.com/Rogerhu12/math-research-public/actions/runs/43770686357) |
| compute job | [132985694072](https://github.com/Rogerhu12/math-research-public/actions/runs/43770686357/job/132985694072)，failure |
| report job | [133003040441](https://github.com/Rogerhu12/math-research-public/actions/runs/43770686357/job/133003040441)，success |
| 请求 SHA256 | `cf914ce6affdeb5fa457113c9e28e62868398bd002577bfa3f6bb992c140c080` |
| 原入口实核源数 | 84 |
| compute 返回文本 | 129856 B；`17812f0fbc1eb787de3997117550121084da6f1d328a183a7c7bc9e842fe2f05` |
| report 返回文本 | 4485 B；`df9f38fe01238f6b84aec677891a4a44f0546b4eaa00b370f62b2a153b1a547f` |

两份日志均由官方 GitHub job-log 集成各读取一次。上表的字节数和 SHA 是工具返回的**解码文本经 UTF-8 重新编码**的身份，不是 HTTP 原响应、重定向下载体或 ZIP 原字节的身份。读取保留工具返回全文；解析时只逐物理行剥除日志运输 BOM／时间戳，不改变 JSON 内科学词。

compute 共 989 个物理行、30 条实际 JSON 事件；本文已逐条读完全部事件及异常原文。桥返回事件在原第 840 行，去运输前缀后保原 JSON 文本并附一个 LF 的身份为 10491 B／`4e8e61be3361038e45e1da6cb6a8d6e9c392e0f7e74bfcc14a4d9779ded4adfb`。这与对解析对象重新序列化是不同的字节合同。

关键本次源身份如下。它们说明实际绑定了什么，不替代未返回的执行正文。

| 源角色 | SHA256 |
| --- | --- |
| SIMD digit kernel，9006 B | `1695b945c706523036ab85d46e1db89494719ff1b5a86efe469c39d696a556e6` |
| SIMD trace header，29035 B | `b183eeecf4f3009bf202dd0f465c8d4fdb17d8cc0ce14bb90d1ed5e6ecf485ac` |
| SIMD stage cpp，12670 B | `b6537c6ce86754a6a2a75eb928e543a7083fa2311eb70a4764066f2a70dda91a` |
| component launcher，29167 B | `9a860d42f47881d23bd8a19042aa6614f596363c7a4ac39ffd4e301907fecbab` |
| same-job helper，38340 B | `a3a879a1a57a36f278941dd06a513a46d66a2b7ef61b30d0730b30cc99c537f7` |
| bridge，15787 B | `cb6ae99b241f2f2d3e5640364287378dc61ff174432a75deb5fa9edc840e2344` |
| 必要 reader，37020 B | `a1106a6a3f6530d149ee21a38e90a6b271f55ee3738b4548bac3017b4c8995dd` |

## 3. 本次实际 fresh64 输入和完整 R273 方向

原 failed73 状态在本次仅为初猜，failed95 不成为接受锚。原当前状态／当前 H 的 fresh snapshot 确实产生；其 `result.json` 为 1316 B／`45841434e9e907d7d77bb2a39ab7ead2c805af1a0370e3e0c9d29f904e598cd4`。

本次 fresh64 范数原读数是 `0.000060618737006888706`，binary64 little-endian word 为 `71f299f11bc80f3f`。这是原 binary64 当前评价，不能写成已经返回的初始 binary128 范数；后者在现有必要范围中没有完整正文。

R273 原方向事件记录：

- 全 129248 行、129248 列，577 节点、576 stage，block width 224。
- 正则参数 `eta_cli_text="1"`，原 binary64 word `000000000000f03f`。
- 增广行数 258496；QR 调用 1153、formation 调用 1152；factor 完成，`actual_error=null`。
- factor／constant 实际及预期均 464891392 B；formation 下溢计数为 0。
- 本次 factor 时间 `16.051270459999955` 秒；这些是原程序读数，不是本文重算。
- 完整方向 SHA256：`4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6`。
- 新矩阵身份 `9ec5004fa385c05e0a4d40eb84bb2fdaeef931914fcee244058f20da75dda296`。
- 全行准确有限 binary64 affine model 的原最大范数显示为 `9.685623139820915231844260456306540893890861679791289092058094119E-11`；最坏行为 stage 9、Q mode 1、全局行 2128。

最后一个数是完整冻结矩阵的 affine readback，和下节实际 nonlinear binary128 范数不是同一对象。原 longdouble factor 也未被称为准确有理运算或新的 128 Jacobian。原64方向只用于约定的 fixed-chord 链，本次 packet 字段明确 `only_fixed64_J_is_reused_as_approximate_chord=true`。

同一实际输入的状态 SHA 为 `f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6`。原 cut、far、scale、stage-J、stage-out、stage-residual、physical-height 的十个数组身份在原 fresh-direction／bridge 事件中完整返回并已读；正文不重复刊登整张可重算数组清单。

## 4. 原 packet 与实际持久 owner 的责任

本次 input packet 为 10348368 B／`1c9df6b2aa203d526eee11fe443ebcb474584c677b76ed3901b6a0f6c1f37aa8`，binding 为 3671 B／`f49354531457d94798c0fe27d59cb55b49c2e50d35ffa12303137a13f5032604`。

原 literal 三角表、geometry 与 schedule 均按本次来源绑定：

| 范围 | 本次原字段 |
| --- | --- |
| 状态／形状维数 | 226／224 |
| 角节点数 | 2048 |
| stage／残差总数 | 576／129248 |
| 原 profile steps 参数 | 12 |
| 实际 schedule 的 RK 原子步数 | 6943 |
| geometry 采样调用数 | 20829 |
| schedule JSON SHA | `3594f1f5da9327c4396350aea82a9086e18d27be96e3db3096c4f6bb00128c1c` |

6943 来自实际 profile／cusp schedule，不能替换成 $576\times12$。packet 导出器未调用 RHS/root/J；它仍准确 lift 原 binary64 geometry 和 literal 表，并没有重新校准连续 geometry。

持久 owner 的实际 CPP 为 `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd`。它的末记录保留：

| 原字段 | 本次原值 |
| --- | --- |
| directions_computed／trial_evaluations／accepted_steps | 1／1／1 |
| attempted_trial_addresses | `[[0,0]]` |
| requested_direction_indices | `[0]` |
| stop_reason | `shooting-tolerance-reached` |
| complete／below_original_tolerance／budget_exhausted | true／true／false |
| rows_completed／stages_completed | 129248／576 |
| 原未访方向 | 1 至 31 |
| 最后已请求方向的原未访 trial | 1 至 9 |

本文不补写桥中未单独返回的 trial 参数词；`[0,0]` 是原记录的地址。未访后缀源于本次达到原 stopping condition，不能冒成剩余方向实际执行。

最坏行为 stage 9，input node 10→output node 9，Q mode 1，全局行 2128。其原 residual 为 `4.99890220172700756918252291853272271e-25`，sigma 为 `5.16104960810073433235339041548094359e-15`；归一化范数的 binary128 hex 为 `0x1.a9fcb11a67aa9fdf970095730bcp-34`。这些都是原显示词，未在本地相除或比较生成新科学量。

独立 fresh replay 的三个原布尔量均为 true：

1. `independent_fresh_replay_complete`；
2. `fresh_replay_full_residual_words_equal_owner`；
3. `fresh_replay_all226_output_words_equal_owner`。

本次末 state 与末 residual 各 2067968 B，SHA 分别为：

- state：`e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2`；
- residual：`18cfb3face9b286513f624003984d318bc6b6c735ed803a3cbffde15dc6be39b`。

owner 全 summary 139390 B／`547c2e714fe5ffd4e2e962960648bc2b638188ff205ee218b432edc8fb21e586` 只返回身份。本文依赖桥中实际公开的 `scientific_summary` 子对象，不声称读取该完整文件。其原 `elapsed_seconds=1844.34919936`，不等同于整 job 或后续全部组件的用时。

## 5. 后续四组件：保留原 flag，也保留未读范围

原准备的 physical packet 为 5104360 B／`1c9fab18574bb130f905daef5fcff66163a0fe987528ace2d9bc81829fc52151`；binding 为 7343677 B／`8ae8ac64d81c5a0e215b1b24b11bf3558065be40f40ab94c087aca7aed5bf866`。其中计划 7488 queries、6943 atomic audit steps；这是原输入计划，不能当成本次完成计数。

| 本次桥原字段 | 原值 | 已返回证据与限制 |
| --- | --- | --- |
| complete_stage_maps | false | 有 start／return 身份，stage 完整正文未出 |
| complete_boundary112_response | false | 无完整112边界响应正文 |
| complete_mixed_endpoint338x112_readout | false | 无完整338×112端点正文 |
| complete_original_C_based_physical_program_audit | true | 保留原汇总标志；完整audit计数、极值、错误／pending正文未出 |
| all_requested_components_completed | false | 不能称四组件完成 |
| native_accepted／fullDN_accepted | false／false | 原完整接受未付 |

stage 获原 science cap 8000 秒、component total allowance 8345 秒；audit 获 1800／2145 秒。原 start 只记录这些允许预算，不能据此声称本次 stage 实际用尽 8000 秒。

stage return 的完整原事件身份是 11015 B／`42753e4ab6bfed974ee82bbf1e70008d193dbd1620c791d3644e988d259cda19`；audit return 为 15388 B／`836b0cabfbfcf73dd6742261940b7abdd3d86c6857c2116585cdd83094d46488`；all-components return 为 28716 B／`4bac5286f8f9062c314a1c02b40cc437e7c097d619a1a9dbb1cf4ac895fd2d7f`。正文只有这些 descriptor，没有对应大对象内容。

stage、audit 外层 `*.stderr.log` 均返回 0 B，owner-child.stderr 亦为 0 B。**外层空 stderr 不能证明内层编译成功，不能代替 retained 编译 stderr，也不能证明具体 SIMD backend 曾执行。** 本次没有从这些缺失正文推出三处 namespace 歧义是否实际触发，更没有提速倍数或 576×224 性能测量。

bridge 明示 `C_equals_F_e_claimed=false`、`all338rows_analytic_Jacobian_claimed=false`、`old_dL_graph_word_equality_claimed=false`、`nominal_factor_residual_derivatives_proved_zero=false`。R402／R405／R414 的条件代数和完整位数合同不因 owner 残差达标而变成准确连续 ODE、准确 Jacobian、完整 native 或几何证书。

## 6. 失败原文与为什么 report success 不补科学范围

官方 job metadata 显示 compute step 1–14 success；第 14 步是原绝对 deadline 的 owner／四组件 procedure。第 15 步 `Read one necessary original metadata summary after the actual child stops` failure。

实际异常定位到 `root_20261115_native_simd_digit128_necessary.py` 第 635 行：

```python
require(request["request_number"]==190,"Actual independent request190")
```

继而抛出：

```text
ValueError: Actual independent request190
```

源码直接表明，这个 `require` 在 reader 自身源身份核对及 `try: ... build(...)` 之前。因此本次未调用必要摘要的 `build`，也没有进入其可返回失败摘要的异常捕获区；不能把整30条桥事件误称已经由必要 reader 完整解析四组件原文件。

report job 的环境 `ACTUAL196_SUMMARY`、`ACTUAL196_SHA256`、`ACTUAL196_BYTES` 皆空。它实际只打印：

```json
{"event":"actual196_scalar_summary_missing","compute_result":"failure","no_scientific_values_or_success_inferred":true,"native_accepted":false}
```

故不存在可供校验的 `BEGIN_VISIBLE196_NECESSARY_SUMMARY` 正式帧。report success 只表示这个诚实缺失分支运行完成。

## 7. 预算、规则、停止和清理

本次 packet 原资源计划保留 owner 6000 秒、fresh replay reserve 1200 秒、stage 8000／boundary 600／endpoint 600／audit 1800 秒及原 overhead；readback／cleanup reserve 120 秒。fresh64 prebridge 已记入全局钟，不重置。进入 owner 时原 `global_remaining_seconds=18552`，guard allowance 18432。

实际 wall guard 返回：

- `elapsed_seconds=2947.86334807`；
- `child_returncode=0`、`guard_returncode=0`、`wall_timeout=false`；
- `error=null`、`signal=null`；
- 最后 `global_wall_budget_exhausted=false`。

原64 worker 在独立 owner 返回后受控停止；记录 fresh snapshot 1、fresh R273 direction 1、原 nonlinear noJ trial 0。持久128状态没有写回原64 worker。原64循环结果仍 `native_accepted=false`、`residual=null`、`task_completed=false`，不能用独立owner替该对象补完成。

原规则 runner 的真实同步为：

| round | 原 UTC | origin_main_read | published_commit |
| --- | --- | --- | --- |
| 0 | 2026-11-15 22:42:13 | `29ae411af294facd35083fe345d6779c239b88df` | `1f50686af77605646965fcd36b547dad317d4f1f` |
| 1 | 2026-11-15 23:27:17 | `5899928eedc707938656e8333ec59f9de18e26da` | `ea19234d1f2b8b1236772d94c0f59749cd0f467f` |

2700 秒规则同步维持；根 README `21bd547f56590b7f2dd279d0297efb289a9b2783`、题 README `bff8aea253a9e6a7a4fac28d810ac454c5499fec`。本次没有由规则变化终止的原事件。

原 owner／original-input cleanup 先明确 deferred。最终 cleanup step 虽 success，实际事件是 `native196_final_cleanup_skipped`，原因为 `necessary-summary-or-child-close-receipt-absent`；`matching_processes=[]`，`no_raw_upload_follows=true`，并明确 runner teardown 可回收临时文件。因此没有为获得“清理成功”而主动删除未读现场，也没有新 artifact／Release／Git raw 保存。runner 已结束；本文不以旧 SHA 假装现在仍能恢复其组件文件。

## 8. 必要后继与尚未完成的目标

这次实际付清的是原 fresh64 完整方向、持久128实际停止及独立 replay 的已返回范围。完整576×224 stage map、112边界响应、338×112端点、完整native/fullDN、准确连续场及几何完成标准仍不能由本次记录宣布成立。

request199 已以独立来源接入：保原数学、完整列／行、113位及 SIMD 字词合同和预算；只对三处调用显式限定 namespace，并修正本次必要 reader 的请求／输出身份。它不是旧196剩余文件的恢复，不放宽科学门，也不假定三处静态歧义就是196实际未返回的stage原因。其真实结果须由自己的原日志和单份必要摘要承担。

本记录已经读取本次全部30条实际 JSON 事件、失败原文、两份日志的全部可用正文；没有逐值读取仅返回 descriptor 的组件大对象。不能因大对象未传回便把 owner 真接受抹掉，也不能因 owner 真接受便补造完整组件或宣布研究完成。
