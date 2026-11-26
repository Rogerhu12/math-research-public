# B030 后端历史保留的原终态：真实 eta .243945588 与完整 epigraph 瓶颈证据

2026-11-27，Astra-new-mechanism-1f4a61a4-20261127。本条解析原自然结束的完整日志，没有重跑任何旧科学。

## 原身份与范围

- workflow `visible-r566-backend-preserving-20261127.yml`；run `45883086225`、job `140126984773`。
- source commit `7923e588c07cd47852dfdf4604db5bc8246ce92d`；run 内实际 pull 到 `dddd38c1c6628ad6f448ebbfe2dbee0892559e64`，根/课题 README 均未变。
- job `2026-11-26 19:21:52–20:01:58 UTC`，Actions success；科学原因 `cooperative_clock_or_unresolved_localizer_checkpoint`，原 STOP 为 `unresolved observed angular localization`。
- driver SHA256 `8cf64c40015350fca09dca3194b6c081078210d4d9146d9369922e8be7cc6930`；原 request SHA `9e3f3c1ca953392f017671868ce16bf8fc2b34ac612d2948f5f459b274a2092e`。
- 原完整 raw 21,831,112 B，SHA `86b6cfc91026975192da40e960b356680c09f3da5c227a37941ce013f59f4916`。
- 原 FINAL JSON 子串529,571 B，SHA `7f71616f8fe94fd1c58889a4e64d66b8253dd6ffef35c75549ffbf70760ae406`。

科学2372.056416865秒；子进程 `19:22:22.240719–20:01:55.156676 UTC`。最终outer27/metric；没有自然 OptimizeResult，不能把 Actions success 当成完整后端或课题完成。

## 真实保留状态

实际81q SHA：`bb921f60d02a3624552d79ebc623e3eb3306b174d981a3ca794a57b44d8edaa4`。

原 B030 物理参数完全保留：p=.85、q=.15、offset=.15，L=.9、open core/flat disk不改，ball1.012、strip约.3928、reach target约.06072。真实状态通过完整 **1212×3072** fine 和 **1292个全部完成的实际角峰定位**：

| 量 | 同一 retained q 的原值 |
|---|---:|
| 含全部已完成定位的 accepted eta | 0.24394558845134018 |
| 纯 fine-grid eta | 0.2439455461872826 |
| accepted物理几何违反 | 0 |
| 最大原算子曲率 | 16.442952646504224 |
| mean E最小 / 最大 | 0.999294447689674 / 3.282734770981071 |
| det最小 | 0.8847671689181204 |
| ball最大 | 1.0114938734606405 |
| abs(y)最大 | 0.3926032465880111 |
| z最小 | 0.02 |

metric-plus实际定位峰为 `s=.1828125,theta=.18629753390655193`；curvature峰为 `s=.7552734375,theta=pi/2`。该最终成功定位1292个candidate，共8500次目标求值、3个完整batch、32.29458766700009秒，未剩未处理候选。source actual 的 accepted eta 为 `.252604422421174`，本条记录的是新真实完整下降。

全库实际为605径向、1355个完整物理峰orbit、463个工作field/orbit行、1536均匀角及FFT节点。工作选择不删任何完整物理行。trust与next trust均 `.3003387451171875`，末后端trust决策未完成，未重置/冒用提议值；retained可行base-extra `.24394604211718696`。

## 历史保留确实执行，仍有新瓶颈

原日志有19条 `WORKING_ROWS_BACKEND_HISTORY_CONTINUES`：19次完整接受全部只更新独立物理best，不改原SLSQP raw数组，不重启同一后端的BFGS历史。真正工作/物理库交换仍导致27个完成outer，28个开始outer。没有跨Actions恢复旧未公开BFGS数组。

19个接受fraction包括1/64、1/1024、1/4、1/2、1/8、1/32、1/2048、1/16384和1/16；最后接受fraction1/2。不能由这一观测宣称每步都变大，也不能把另一个输入上的旧24次接受次数直接当作因果对照。

新日志复用**已经算出的** `active_rows.fun` 向量分组，没有额外科学求值。纯原日志按48个不同raw q去重后得到：

- **48/48** raw候选的全部已选工作物理组均通过1e-8。
- **48/48** raw候选只在metric epigraph工作行失败；最差组40次`metric_plus`、8次`metric_minus`。
- 全部48raw中的工作物理组最小值：ball `6.107675485159114e-10`、curvature-minus `.31818370514073924`、curvature-plus `9.633919308861018e-6`、det-floor `7.751431018602545`、mean-E-floor `2.9952968481106685`、mirror `.10749168780084747`、positive-height0、strip `1.1984029660858445e-6`。
- 12次 `unrepresented_required_coarse_rows_rejected` 的**完整coarse**分组记录也全为metric-only；每一次物理组都过1e-8。

这是本次实际证据，不是由一个全局最小值猜测瓶颈。工作物理组通过不自动覆盖未选物理行；本条仍分别保留完整coarse/fine/定位门。它指向具体下一改变：区分辅助e与真实q，只抬独立候选的e，重新执行原完整行及最终资格，避免单纯因e低估强缩q；任何e变化都不算实际eta下降。

## 末两个未接受对象和pending

末 raw q SHA `3b0324b2f39ecc09edc22d861e7a891d925c9c5b2033ee7817539feacb565072`，raw e `.24213702634476575`。物理工作组通过，但metric-minus `-2.5638939867150823e-5`、metric-plus `-3.7376113096732055e-5`。它没有被保留。

该raw与真正retained bb921…之间的fraction1/2另一个trial为

`bc9b991faee4beb81b91cbdc834aae6dbdcb1be951d803386f787c97430df097`。

这个trial的工作违反0、完整coarse 2,151,130行通过，完整1212×3072 fine已经做完：grid eta `.2430865314325668`、物理违反0；nested FFT三个差分别约`1.9984e-15,7.9612e-16,2.6695e-15`。但其e `.24304153423097635`，且随后1353个角定位候选**一个也尚未处理**：0batch、0目标求值、状态 `scientific_clock_checkpoint_with_remaining_brackets`。完整候选描述保存在原FINAL的 `last_trial_not_implicitly_accepted.observed_peaks.remaining_unprocessed_candidates`；完整同一fine径向位置另外在原 `THETA_PEAK_LOCALIZER_PARTIAL` 行保存。

因此 bc9b… **不是accepted状态**，不能以其更小grid eta覆盖bb921…。后继须保留/处理剩余真实候选，并保留源fine/nested已完成资格的准确范围，不能重称old fine为新检查或把未完成定位算零费用。

原未采用pending物理orbit1和工作行1，位置均 `s=.47812499999999997,theta=.2863430804053202`；工作行是`metric_plus`，源bc9b…的完整fine证据值 `.2430865314325668`。它们尚不在actual1355/463库内。不能把actual与next混成1356/464已通过。

## 成本与继续入口

所有原继承账本保留，特别是三个更早外部关闭后的未知未flush费用仍未知。已记录科学链下界为 `9988.810808117` 秒，不称准确总耗时。

本run新增：48完整Jacobian、2310方向block、Jacobian799.0249598829985秒、274个工作value key；48 callback proposal、226回溯value trial、48工作恢复、0回溯耗尽；63完整coarse、36完整fine、35完整定位，另1次未完成定位。

定位候选总48734，已完成47381，目标求值323855，未完成1353。15次fine/实际峰epigraph拒绝、12次完整coarse拒绝；27次working exchange、15次physical exchange；没有新的restriction/parity方向重放。

原oracle账本新增4563个FFT state、277个oracle构造、332266次point evaluation、2461804个point values、5800896个point参数方向；其prepare/point秒数分项属于总科学时钟，不再相加冒充独立壁钟。所有未闭合当前操作已计在总elapsed而非虚构completed计数。

后继实际入口为bb921…、605/1355/463、两个原pending、trust `.3003387451171875`，并另携bc9b…同一fine/1353未处理定位的未接受身份。继续保持原完整物理库、真实角峰、nested检查、工作margin与实际eta严格下降；本收据没有冻结g、连续全域reach、有限等距族或README完成声明。
