# true53 四cut：准确支撑metadata接线与原同钟继续

日期：2026-11-16。此修改继续[原任务](true53-four-cut-exchange-master-design-20261116.md)，并如实保留[首失败](true53-four-cut-first-input-failure-and-carried-account-20261116.md)及[布局错误](true53-four-cut-layout-descriptor-failure-20261116.md)。当前原9662行问题仍一次都没有求解。

## 1. 只传分类器实际读取的准确数据

原 `RationalRowGrid.classify` 完整body只读取传入对象的 `left/right`，然后以原rational nodes判 `left<t<right`。它不读取M、columns或layout。

`ExactFiveHeightBasis` 已从真实 `source_definition.original_basis.interval_exact` 恢复 `left_exact/right_exact`；原 `EntryTail154Subspace` 的端点是 `9/250,423/500`，原159子空间要求height/tangent端点准确相同。本次直接从同一个已绑定的 `self.field.coordinates.basis` 取这两个Fraction，建立只含两个属性的metadata view，再调用原classify。两端另外严格匹配上述原有理值。

因此既不把简化切片冒成完整published descriptor，也不为这一次分类重建原子空间。该接线与原classify逐式相同。原field/configuration/coordinate/model/cache身份仍在原入口绑定，非另造物理支持。

上一修复的5743可变metric行逐序比较、全部installed逐hash、原5+4梯度、支撑外恒零依据与完整网格值全部保持。所有JVP/新gradient/finite/line/actual数学公式未改。此次没有执行开发、compile、额外原数据观察或测试。

## 2. 完整旧失败不漏记

最新失败source **de4d16fe93b12ef77d946bc8eef64e51fa9ed5a5**，run **43826338594**，job **133160965959**：

- 原log3757837B / e9bb74a1749ad0d689070f7261d544895d6c91080d7a1af1075bb1aa6ab21ea2。
- 原FINAL_CLOCK JSON+LF10813B / 7ad8d3c6acd6851d1055e4da26d8a07ca4da3f9a01e041ee3a524ec83fffe2ce。
- 同task已付 **91.37788493000002秒**，其中包含首失败36.79963991600005秒；总祖先 **1750.3576756209998秒/128值**。
- 两次都0finite/JVP/新gradient/scalar/actual，原restore1与repair1均已消耗。

继续入口只读这份原clock一次；它已含前一原clock来源，不能把首失败再加一遍。科学时间始终是

$$
T_{\rm task}=91.37788493000002+T_{\rm current},
\qquad T_{\rm task}\le600
$$

的同一个已分配账户，当前imports/input/输出均计入。保原restore1/repair1，明确允许新增一个repair，使修复总上限为2；没有给一份新600秒。原32finite/3072迭代/6144系统/32双网/128新gradient/64scalar/3pair及6value上限全部不变。

原失败没有导出完整context数组，因此只能计费恢复必要缺失fields/frame；U/T/e/f、旧J、旧方向和旧finite不重算。前次失败事件已有的原source标记保留，新增carried标记不覆盖更早来源。

## 3. 两个实际改动源码

| 文件 | UTF8 B | SHA256 |
|---|---:|---|
| frame_metric_true53_augmented_scope.py | 9433 | 54e62b3d35e23e9a5c8e5faf7ff9244823e98c888f1ced4468ad39361eb3ac3d |
| frame_metric_true53_augmented_first_jets.py | 65347 | 87465f375413a313cfe7c9458aef4875c24de4680eca94817274ba24f8566b7b |

transfer/audit/core继续上次已发布源，直接从scope读最新carried来源与时间；原workflow不改，request小改动触发唯一继续run。method_design及两次失败/修复出处全部保留，source pins增加本说明。

## 4. 不变的研究目标

仍以真实新增四行开始首次finite求解；后续仅真新增原行后求解新矩阵。完整gain合格才原guard/scalar/14门。单任务结束不结束主课题；目前仍点53、η细.26601514422985384、κ57.9992694544513，全部主完成门未付。
