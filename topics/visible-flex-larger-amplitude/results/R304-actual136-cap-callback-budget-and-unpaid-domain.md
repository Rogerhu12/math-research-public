# R304：实际136连续 E 的 cap 瓶颈、callback 异常与未付径向域

- 作者：AI
- 日期：2026-11-15 UTC
- 性质：真实公开 Actions 结果及原源码定位；没有本地科学重算，没有新的场、尾响应或 metric 证书。
- 承接：[R286](R286-original-stored-continuous-integral-and-metric-bridge.md)、[R293](R293-actual132-continuous-E-panel-budget-and-unpaid-whole-domain.md)、[R297](R297-continuous-E-unit-panel-and-piecewise-enclosure.md)。

## 304.1 实际结论

实际136执行了独立 v2 的完整原输入和原六 primitive 路径。它没有返回完整有限头，没有自然 $R_{\rm out}$，没有完成任意一个请求的闭径向 query。声明 C 的全域 $E,E_r,E_{rr}$ 消费责任仍未支付；不能从本次输出给 R300 填实际 cut jet，也不能将旧 a601 或九450 metric 标为通过。

本次没有再耗尽200000 panel数量上限。原计数是21334 panels，实际耗时为1800.0188949619999秒；终止为 `acb.integral` 跨 callback 边界返回的 `SystemError`。原科学步骤和 compute job 失败，独立原值 readout、临时 raw 清理及报告 job 成功。成功的 readout 不改变科学未完成结论。

原日志显示 v2 已完整走过 cell6、共1386个原 pieces；但这个进度不是 result 的返回值。异常跳出 `build_head` 后，主程序保守字段仍为 `complete_original_pieces=0` 和整个1440片的未付范围。本报告同时保留两种原证据，不以进度推造返回的完整六维累计量。

## 304.2 真实运行、来源和读取范围

| 项目 | 实际身份 |
|---|---|
| Run | [43707070768](https://github.com/Rogerhu12/math-research-public/actions/runs/43707070768) |
| Dispatch commit | `c1178bd2e17383a5a0f6bed1ec8fe1896704a528` |
| Compute job | `132790329190`，completed/failure |
| Report job | `132797941930`，completed/success |
| 科学源 | `geometry_20261115_stored_continuous_E_cover_v2.py` |
| 科学源 bytes/SHA256 | 77697／`004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea` |
| 保留的原 producer | 66415／`9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed` |
| Request SHA256 | `2b9945acbc3a113e8654d225140a68a087a9c7073cec129963f2cc01ffc15a6c` |
| 原 query recipe | 782 B／`4fa2baa15518ee5045d4a21305ff3f727ef594f966e8a95f9bc6f89eaac3b979` |
| 原 result | 13027 B／`745d601a05a4bb429c0345a1c4f42929aec172fdf975b8ff9555330336b48904` |
| 完整紧凑 actual readout | 14950 B／`26794a89d0404632f7c231bc810856dc0e542a18eec9d5b7cf32ce783618dd2e` |
| 本地读回方式 | 官方 `fetch_workflow_job_logs` 的完整 decoded UTF8 |
| 此 decoded log identity | 109387 B／`549996a98789da97b2b9d9bcd65101ad5cbc8d556f1353e6b58004b96e94ab79` |

14950字节摘要的 SHA 范围是原 compact JSON，**不含外侧分隔换行**，与日志中 `request136_actual_scalar_identity` 完全相同。这里的109387字节是连接器返回的 decoded log，不冒原二进制日志压缩包 identity。

科学 source/request/proof/query 共9件 source pins 已由本次 Actions 原步骤逐字核；不是本报告通过 source 文件名猜同源。实际 runtime 是 Python3.12.14、python-flint0.9.0、precision256bits。原 R286 证明仍为37491B／`81d061a6db372a531a119d54298a68d1b9804a7e08fea0fd33bc5fe75a809efb`。

本报告完整读取了官方日志中的 source核对、原154条 cell-complete事件、完整 result 标量、最后 panel、readout、规则runner和cleanup记录。没有读取203MB primitive ledger或19MB radial ledger的payload；下文列出的这些大文件身份来自真实 producer。它们已按规则15在 readout 后清理，不能把“看到producer SHA”称为已下载／已逐字审核全部数值行。

## 304.3 未改原数据与预算

本次从历史提交 `8bd267107cc8710d371f3b62c02986655ac965b0` 恢复真实三件数据：

| 输入 | Bytes | SHA256 |
|---|---:|---|
| 原 T112 config | 2161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| 原 calibration ready | 109004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| 原 stored ready | 29774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |

实际原输入没有重新序列化，也没有作为新数据重新入库。没有 accepted field、旧native响应或新ODE输入。

科学范围保持160个原 finite cells、每cell9 pieces、1440个原pieces，全部
$
(A,B,\sqrt E A,\sqrt E B,wA,wB)
$
及所有 $n\ge160$ 深尾根族。原 request 条件为：

| 参数 | 原值 |
|---|---:|
| precision_bits | 256 |
| integral_absolute_bits | 96 |
| integral_relative_bits | 80 |
| analytic_guard_bits | 8 |
| integral_evaluation_limit | 100000 |
| value_width_bits | 24 |
| max_depth | 48 |
| query_depth | 12 |
| max_panels | 200000 |
| max_query_nodes | 200000 |
| budget_seconds | 1800 |

v2保原 C 实表达、piece/cap/flat/valley/weight/cut、自然外半径定义和全部六分量。没有48-selector树、旧数值 factory、ODE、shooting J、非线性尾或新的场调用；没有借 R26 的另一个数值证书。

## 304.4 原进度与最后 panel

原事件依次输出159至6的154个完整 cell。以下只是原事件字面值：

| original_cell | completed_pieces | elapsed_seconds |
|---:|---:|---:|
| 10 | 1350 | 53.149526570999996 |
| 9 | 1359 | 55.69044660700001 |
| 8 | 1368 | 58.088238969 |
| 7 | 1377 | 60.132644019 |
| 6 | 1386 | 1055.147580824 |

随后最后已记录 panel 是：

- `source_piece=1391`，`original_cell=5`，`original_segment=5`；
- `depth=45`；
- 原闭区间
$
\left[\frac{14009612025055}{17592186044416},
\frac{28019224050111}{35184372088832}\right];
$
- 完整真实 range 有限；
- 原可能 cap branches 为 `["raw","transition-low"]`；
- 原 $w_x$ display 为 `[0.0213552108056 +/- 6.27e-14]`；
- 原 source 明确记 `interval_classification_is_not_a_unique_physical_failure_cause=true`。

这一末 panel 的已报 $w_x$ 区间不含零。因此不能把这一现场说成“绝对值零点造成的唯一困难”。它仍有 cap 分支边界。反过来，整个运行的 abs callbacks 不为零，也不能因末 panel 正导数就说其它所有 panel 已无绝对值问题。

这里没有将上述有理坐标本地换算为新的十进制位置，也没有重新计算任何导数、primitive、范数或误差。

## 304.5 六 primitive 和 Acb 的真实诊断

本次不是“所有 Acb 调用都失败”。原56739个 component attempts中56738个已有有限 enclosure，fallback计数为0；一个调用在停止时没有正常完成记账。

| 原计数 | 数值 |
|---|---:|
| integral_panels | 21334 |
| inverse_cover_nodes | 0 |
| rigorous_analytic_component_integrals | 56738 |
| analytic_panels_attempted | 9457 |
| analytic_components_attempted | 56739 |
| analytic_components_finite | 56738 |
| analytic_components_fallback | 0 |
| legacy_whole_panel_gate_satisfied | 8993 |
| legacy_gate_bypassed_for_cap | 103 |
| legacy_gate_bypassed_for_derivative_sign | 361 |
| analytic_cap_nonholomorphic_callbacks | 1949868 |
| analytic_absolute_value_nonholomorphic_callbacks | 128169 |
| real_range_failures | 9898 |
| real_range_goal_passes | 1979 |
| restored_six_goals_passes | 9375 |
| subdivided_after_restored_goal_failure | 80 |
| coarse_valid_panels_at_maximum_depth | 1 |
| complete_accepted_panels | 11355 |

原六个 full-width goal 失败次数依顺序是
$
(80,56,80,57,55,81).
$
它们是完整工作宽度判据计数，不是原BVP验收失败次数，更不是新metric误差。

末 panel 的**积分前真实range乘长度**的六个工作目标都未达到。完整 dyadic endpoints 和 display 在14950B原摘要内；没有丢弃某个分量：

| Component | 原 full-width display | 原 work-goal display |
|---|---|---|
| A | `[1.095637132695220599536580356816160119918089089623451301558354487042379332706e-28 +/- 3.33e-104]` | `[6.311536690530211759506004283703134262699684464086215032311188512827739928975e-41 +/- 4.01e-117]` |
| B | `[5.623468825535894870299569952970315749632320649858767142003966140470937233814e-39 +/- 3.34e-115]` | `[3.592949321332853317940924453543824816361685367359654954146870920005812152411e-43 +/- 1.09e-119]` |
| sqrtE_A | `[1.095644283462455521675948832234263350282996396129766257521165329080758965574e-28 +/- 2.05e-104]` | `[6.311559679045213828606225589747616251130895477673043298078628632531653756898e-41 +/- 3.86e-117]` |
| sqrtE_B | `[8.430610493534661970037035772337878293780679691900696853474294886258053028337e-39 +/- 1.07e-116]` | `[3.592949341938834857382126951939996130585361073800725931441206419907282366941e-43 +/- 4.25e-119]` |
| w_A | `[4.122565437914496339430676446925202087295677015165585303129239247432735737675e-31 +/- 1.03e-107]` | `[5.285961449636490892101100755438172613721247843380561827931046734372262859005e-43 +/- 4.52e-119]` |
| w_B | `[1.037101923908977425869187357949310233264833033276738728683878683600174883117e-36 +/- 8.44e-113]` | `[3.587339294574775655489389081274272159991162287114188004517945091626445006585e-43 +/- 3.33e-119]` |

工作 goal 仍为原
$
\varepsilon_A(b-a)+\varepsilon_R\max(|I_-|,|I_+|),
$
且用恢复后**全宽**检查，guard8bits本身不证明达到该目标。有限 coarse enclosing panel 与工作精度严格分开；原1个 maximum-depth coarse panel 被如实记录，未冒精度达标。

上述数据支持下一改进聚焦真实 cap 附近的 piecewise Acb 成本和闭包宽度处理。它们不证明每个大counter都来自同一个原因，也没有证明只加时间预算就能完成全域。

## 304.6 callback 异常的确切源机制

原 producer 最终 error 原文是：

```text
SystemError:
<cyfunction acb.integral at 0x71a5f9fc8720>
returned a result with an exception set
```

此地址只是这次进程的原字符串，不作为源身份。

0040源的 `ResourceStop` 直接继承 `Exception`。其 `WorkBudget.check()` 在墙钟达到1800秒时抛出该异常；Acb callback 内每次先调用这个 `check()`。原 callback 没有保存独立的异常类型/原因 side record。

为核这个传输边界，本次只读了官方 python-flint **0.9.0** 的 [acb.pyx](https://github.com/flintlib/python-flint/blob/0.9.0/src/flint/types/acb.pyx)，文件Git blob为 `3507137a9ab247e2978a17b7add0ec27df1722c6`，没有导入或运行它。其中：

1. `acb_calc_func_callback` 只对 `TypeError,ValueError` 保存 `ictx.exn_type/exn_obj/exn_tb`；
2. `acb.integral` 完成 native调用后只按这个已保存 ictx 重抛；
3. 当前 `ResourceStop(Exception)` 不在该捕获集合内。

这是可确定的源码接口风险。实际1800.0188949619999秒、原callback预算检查和最终SystemError与“预算异常未按受支持的通道传出”一致；但是本次没有单独保存那个内层异常，所以不能用这个推断覆盖原 error 类型，或把其它未知SystemError一律改写成预算。

最小独立修复是：在 callback 内**先确切捕获并保存**真正的 `ResourceStop`，仅把它转成带专用标识的 `ValueError`；Acb重新抛出后，由这个已保存记录恢复原 `ResourceStop`，交现有 `integrate` 的未付pending收尾。其它异常保其真实类型/原因，不靠 elapsed 数字猜测。无须改全局异常继承，也不放开任何科学门。

官方[Acb文档](https://python-flint.readthedocs.io/en/latest/acb.html)要求 analytic=True 时不能把非解析区间当作正常函数值。这项合同本身正确，应保留；不能为减少 cap counter 就把原跨cap callback改成虚假的单一解析分支。

## 304.7 为什么原返回值是0、而日志有1386

本次 `build_head` 是一次函数调用；其完整返回值本应包含 completed count、累计六primitive和余责。SystemError跳出该函数，主层 `head_result` 未取得这一返回对象，因此最终：

- `complete_original_pieces=0`；
- `finite_head_all_six_primitives=null`；
- `full_deep_plus_head_all_six_primitives=null`；
- `unvisited_source_piece_suffix={"first_piece":0,"stop_piece":1440}`；
- unpaid ledger仅一行 `producer-exception`，声明所有未由完成记录证明的source/query区域仍保守未付。

这不是“运行只碰过第0片”，也不是“已经完成1440片但摘要错写”。前者与原完整cell事件矛盾，后者没有任何原返回证据。

原 temporary ledgers 实际已写：

| Ledger | Rows | Bytes | 原 SHA256 |
|---|---:|---:|---|
| six-primitive panels | 11355 | 203635746 | `b18481b01a51727c89373099531b2a5a8a36c19e96b0e8fe2b2fa910efec16cc` |
| source radial panels | 11256 | 19930174 | `5b8d6b1749d32529b46de38ff3235442359e7831fe89bfd1b43695808af5defc` |
| query inverse cover | 0 | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| unpaid complete scope | 1 | 297 | `015c9ef516760c2076a277f33e131bab282a7ca0a20500d83a20ce2fa38c9630` |

没有下载这些大payload或事后重建累计量。后继源需要保存本次正常完成进度及真实pending，而不能把这个actual136原result改成后继格式。

## 304.8 深尾、seam与query的原范围

原结构报告为：

- 深尾原exact根存在条件已证；
- 深尾根数值没有计算，`deep_root_values_computed=0`；
- `all_admissible_original_root_choices_uniformly_enclosed=true`；
- `finite_joins.proved=true`；
- `protected_join.proved=true`。

这是原C模型的相应结构/深尾范围，不代表完整 finite头或物理径向 query 已完成。原 deep cover 的显示值包括 $E_r$ 的 `[+/- 3.22e-84]`、$E_{rr}$ 的 `[+/- 0.0446]`，以及完整160后无限cells和准确cuff；未把粗界当小metric误差。

实际全域结果同时保：

- requested_query_count=1，returned_query_count=0；
- inverse_cover_nodes=0；
- query-results.results为空；
- natural_outer_radius及其与nominalcut的差均null；
- all_requested_closed_query_bounds_complete=false；
- continuous_convention_C_query_enclosures_complete=false；
- numerical_work_resolution_complete=false；
- a601_same_field_binding_or_relative_metric_threshold_paid=false。

`unvisited_query_suffix=null` 是异常路径的原字段，不表示所有query已访问。必须与返回0、空results、整个原query-plan保留及producer-exception共同阅读。

因此既不能把名义cut与真实自然外半径认同，也不能对其外域补 $E=1$，更不能从一个粗深尾bound取三个点数作为 R300 的真实 cut jet。

## 304.9 规则runner与raw生命周期

本次规则runner真实开始／结束为 `11:04:10 UTC` 和 `11:34:10 UTC`。原记录：

- science_returncode=2、wrapper_returncode=2；
- periodic_sync_failures为空；
- README_change=null；
- science_terminated_for_actual_rule_change=false；
- original_scientific_argv_and_budget_preserved=true；
- sync_rounds_started=1。

实际第0轮pull记录为11:04:10、origin main `f59c795c69c05bed6efa45a937ab352def8e5972`，规则日志提交 `a2bd847d4bc5385d2143a1e5f3a474e9c54ee8d7`。本报告不把API读main称为额外git pull，也不把后来的README状态回填这次源。

11:34:11.1872783Z 原cleanup事件为 `request136_owned_temporary_payload_removed`，`raw_outputs_or_recovered_inputs_not_uploaded=true`。原ready、完整中间证书和raw ledgers没有上传新的artifact或Release；保本次脚本／参数／run／输出SHA和实际结论。

## 304.10 后继最小科学动作

本次真实证据决定的下一项是独立v3/request139，保原三输入、同1440pieces、六primitive、全部深尾、200000panels/1800s和完整query；不把139作为R297证明的审核门。

它至少需要同时处理：

1. 精确的 callback ResourceStop传输及完整pending/已付piece收尾，防止再把明确预算停止变为generic SystemError；
2. 对原cap处的实函数积分结构做有效优化，不能只改摘要或盲增预算。

一个已从原式定位的可行方向是：在原 $\chi=1$ 的闭panel，若完整 cap/flat/valley 后的同一个 $w$ 已证 $C^1$ 且 $w_x$ 同号，则
$
A=\frac{|w_x|}{K(1+w^2)^{3/2}}
$
的三个偶数primitive可由这个**完整 $w$**的端点差给出。不是把smooth-cap换回raw；端点值仍保所有可能原branches。跨未判定零点、两个 $\chi$ transition及其它未证前提仍保原完整积分／未付责任。该链式恒等式和真实cap拼接将独立完整证明后用于新源；本actual136没有执行这个算法，不预写它一定成功。

原全部科学目标、BVP／native／全闭场、同g精化、相对metric、reach/held及原完成条件都没有因这次数值求值器部分结果而降低或改标签。
