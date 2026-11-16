# R882 首 scope：原循环7对应十七系数的同素点消费

## 1. 已成源与唯一新增算术

本 scope 的结果名为 R882-original-cyclic-seven-common-place-coefficients，最终证书为 p41-original-cyclic-seven-common-place-coefficients-certificate.json。数学依据是 [R882](../results/R882-original-cyclic-seven-common-place-and-target-normal-interface.md) §§2–4。固定辅助素数1000000753及原 $\zeta\mapsto549966761,s\mapsto99932770$；不改变 R873 的原2058列顺序、2058选行、十七右端、82尺度或 source/target 规范。

R873 实际成功 run43832703159/source2ee14751d7b2cb4403931886b587ca6f64138c73 保存了准确整数数据及739处的旧单位解。新 core 只读取这些原字节，生成原矩阵和右端的新素点归约、新2058单位逆、17列坐标及全部2200行乘回。首 scope 不读取旧739数组作为新坐标，不重新执行原范数、Berkowitz、q展开或旧尾递推。

## 2. 直接来源与载体

标准库 public wrapper 读取成功 R873 artifact 的完整 manifest、元数据、准确最终证书和实际 stage index。只选择该证书的 section_basis、norm_target_index、exact_coordinate_expression、correspondence_DAG、source_audit、stage_manifest，以及前两者直接引用的八个补列与十七准确右端。所有选择由真实文件名/bytes/SHA驱动，旧configuration保持原样。

R873-retained-original-inputs.tar.gz 的344533352字节与原 source inventory918766字节完整绑定，作为原4960件来源载体原样续传。wrapper 按原 inventory 对包内成员逐SHA恢复，不从已经过期的 R799/R801 重取或重算。新 core 的实际旧源只用 R799/R801；原其他组继续留在该不可变载体中，供后继 R807 函数叶或其他明确消费，不能把未读取的原组说成本次新数学输入。

新选择的 R873 小阶段另包装为 R882-retained-R873-selected-stages.tar.gz。R882-original-source-inventory.json 同时记录该选择、原载体及实际core输入。R882-retained-inputs-receipt.json 记录完整选择数、两载体SHA和Range传输来源。wrapper 可以复用冻结 R873 stdlib wrapper 的 Archive/metadata/安全tar机制，但实际driver、运行receipt和数学tag均为新R882，绝不冒充旧wrapper。

## 3. 矩阵与右端构造

2050个原列逐项检查原 R799 basis index 与 R801 frontier 的 index、recipe、node_key、node_fingerprint 一致；原前缀段必须恰为R799的区间[0,109)，新增尾必须是R801中唯一覆盖109的已成段。原20实坐标排列保持不变。新八列直接读取 R873 已成补列0、1、2、3、73、74、75、76的110×20准确整数矩阵。

每64列保存一个完整新归约块，最后块保实际列数。每块的来源列表逐列指向原文件，完整矩阵形状为2200×2058。十七右端一次归约，形状2200×17，列序P0至P8、K0至K7。没有再次对原 q 数据做卷积或普通乘积。

## 4. 单位逆、解及终验

严格采用 R873 实际 section_basis 中的2058选行。先保存新行列式结果；若为零，返回明确 UnitFailure，已成归约块和真实零结果继续保留，所有成功标志为false。首scope不改变素数或选行。

若非零，计算新完整逆，并检查两个2058×2058矩阵积均为单位阵后原子保存。17列解为该真实逆乘原选行右端。随后以每64原坐标行为一块，准确核全部2200×17关系。每块保存原矩阵/坐标/右端引用及实际产品摘要。摘要不是替代计算；全部等式已在该数学阶段逐项比较。

最终 same-place-correspondence-coefficients 指向新逆、新坐标、完整回代块及原 R873 准确 unit-solve/DAG。它只声明同一准确特征零系数在新素点处整并具有所保存的约化，特征零有理坐标仍未展开。

## 5. 标签、阶段与恢复

数学tag绑定真实coreSHA、python-flint0.9.0、正式证明/方法SHA、三个实际源R873/R799/R801的身份和选件SHA、全部inputs、原载体身份以及固定strategy。预算、物理目录、下载方式不进入数学身份。矩阵块64、回代块64及原选行政策属于固定strategy。

全部数学阶段为输出根目录 R882-common-place-*.json.gz。完整阶段不可变；current文件明确complete=false。最终stage manifest按实际内容SHA命名，完整阶段与current分别列出。续算仅接受同core/tag，恢复所有已完成阶段和真实current；旧false FINAL不约束已推进的current或新manifest。true FINAL则核完整引用后原样保留。

已保存的新单位逆、17列坐标和完整回代块均直接读取，不重新求逆或回代。预算可在原子阶段之间停止；外层timeout为预算加900秒，SIGTERM后短宽限kill，保留完成stage与载体。若hard stop未写core receipt，wrapper只在run中记录真实null，不造receipt。

## 6. 运行与诚实边界

core CLI为 --config、--retained、--output、--budget-minutes，预算不超过300分钟。core及wrapper均要求真正公开仓库Actions环境。仅AST、来源字节和schema可以在算术之外检查；不在本地运行数学。

workflow仅本请求push或workflow_dispatch触发，contents/actions read，sparse checkout包含README、本topic与该workflow。rules步骤真实git pull --rebase origin main；README变化时相对请求上次已读commit打印diff。依赖安装使用块标量，固定python-flint0.9.0。全部artifact仅保留一天。

输出固定：target_normal_basis_computed、nine_reference_norms_computed、original_Picard_support_computed、height_or_nonp_calibration_computed均false。后继目标271右端和R879参考九范数按R882 §§6–8继续实现，不由本次17列完成自动宣称其成功。本次也不下载或重算R879参考系统与原R827 Krylov逆。
