# R787 实际预算停止与同一数学核心续算

日期：2026-11-15。状态：**运行记录与纯IO适配；尚无原完整A/B关系。**

原公开run[43683912711](https://github.com/Rogerhu12/math-research-public/actions/runs/43683912711)
在source `eab5e58bbf951c48ccf13a109bbdf0b0289a6f23` 执行。
核心于2026-11-15T11:06:48.732106+00:00结束，退出码1；
原core receipt准确写为
`BudgetStop: All completed R787 stages remain available for exact resumption.`。
不是原关系不存在的结论。工作流的最后完整证书verify因此失败；
原已成断点上传成功。

原artifact14159006977：
`serre-global-R787-original-power5-function-relation-43683912711-1`，
ZIP 5,148,711,108 bytes，
SHA256 `32652fdbb99ef41340bffb4ba1c9d1a56479de346c999f723023db2e1427645f`，
到2026-11-16T11:06:54Z。
其完整manifest为440819 bytes、1517个登记文件，
SHA256 `613f436b2c398cdcd5c9a92c4eb47e72bc81f8d0e8395322eff6455c89c0821c`。
原core receipt SHA256为
`ec4673e2b51e4b3e47b2fbea4ac75c34c7923e90d47ab3f80110cf35f426e8f7`。
这里只据实际公开metadata登记预算状态；
最后素数、Schur秩、14分支和实际Dixon位数待续算的全流式审核返回后登记，不能预填。

## 数学身份逐字保持

- 原数学核心 `scripts/R787_original_power5_relation_solver.py`：
  `93d3d72b01b0ed5d48486a632b74c3470b15affdcb1bd03e21f1b5283fc82d04`；
- 原字段核 `scripts/R781_original_Laurent_prefix.py`：
  `d024a7a6f5febd4658e8b5b5e5e3659f3c5fcc0daa39d70569ac408ef83a8751`；
- 原proof：
  `c46008726fb18f52a5430b72c4994ce76164f11bea51044f1677278294f7011d`；
- 原method：
  `1d91bfc7bdf61c40c4deda19833a5f50491630a61a7a25feb7a3a1e0b451204b`；
- 原R781/R786 producer对象、p41、V5维1234、129条件、14个L分支、
  辅助素数起点、每8位重构一次及原自由坐标规范全部不变。

原数学核心只读取同一素数最新完整Dixon文件，
下一位只需要这个当前向量、保留的chart/全部分支及原输入；
旧位向量已被后继完整向量覆盖。
因此可以只传其最新正文并保小SHA历史，不改变数学计算或丢掉需重新求出的阶段。
新wrapper中的 `prepare_inputs` 与原函数逐字相同。

## 只改传输与断点收缩

新wrapper SHA256：
`42157e0d95eb5d9aed28ef828a86dc5e7bec89e806e3e0a92aa0bcb1a36988b6`；
[实际续算请求](R787-public-original-power5-relation-request.json) SHA256：
`583e43bee1521aab3aabb5856032bdc2dc206e7959ce5d4818cfb4dccc6858e7`。

续算先流式下载并核真实ZIP字节数/SHA，逐1517个原manifest项全部验尺寸/SHA。
随后保每个素数最新完整Dixon向量、**全部非Dixon完成stage**、原输入包；
旧Dixon向量仅保存原name/bytes/SHA/prime/digits历史，最新向量的前项SHA照历史核对。
全部1372个原bundle成员按原producer的manifest核实：
R781有134项，R786有1238项。
不下载一份重做的替代数学输入。

若本次仍预算停止，输出阶段只删除被更新完整lift覆盖的旧大向量；
先写同包小SHA历史，再删冗余正文，全部其它完成stage保留。
若已存在成功FINAL，则不做这项裁剪，保留原certificate inventory的每项。
输入恢复在joblog输出 `RESTORE_REVIEW`，
包括真实prime、Schur秩、14分支、最后Dixon位数、原bundle核对计数，
不输出大坐标或秘密。

workflow SHA256：
`372df99700a9d5a54a9a3d48ef2a42497c9be33157b478a7cc8e73e8cbbaad6f`。
独立rules job真实部分clone和pull main，比较上次已读
`f59c795c69c05bed6efa45a937ab352def8e5972` 的两README；
变化只输出diff并让root读取后遵守。源码AST在公开runner执行，
计算仍只本公开仓库Actions。改为contents/actions只读，去掉自动Git发布，
只一日active artifact；不把可重算矩阵、证书或旧lift写Git/Release。

结果仍只认原非零A/B及全部129×20准确代回。
成功后接既有R792、R804点消费者；本次没有用R802替换原任务，
也没有把预算停止解释成数学否定。
