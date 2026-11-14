# 同一完整物理角图的有括界 Newton 求值

本件只改变 native reader 的数值反解器。原完整图册、物理度量、raw 字段、coast/terminal 变换和所有原生导数公式均保持。未做 BVP、全 Jacobian 或 body 积分；不把这次有限比较称为连续几何证书。

## 实际问题与新入口

原 `RawLiftedNativeField.invert_angle` 在每一步更新括界后，要求 Newton 候选离两边界至少达到当前区间长度的5%。一个已经接近根的候选也可能被这条条件退回中点。它仍是正确反解器；本件只尝试减少相同函数的重复求值。

另名 `scripts/fd2d_gc_fast_material_inverse.py` 提供 `invert_material_angle(reader,x,u)` 及可显式选用的 `FastMaterialInverseMixin`。初始种子和原缓存保持，全部查询仍调用 `reader.chart` 的完整函数。严格在当前括界内的有限 Newton 候选可以使用；不在括界内或发生浮点停滞时改用中点，此外每4轮对未完成点执行一次中点步。最多256轮只是一次函数求值的错误保护，达不到明确容差会抛错，不返回未经验证的近似。

停止条件逐点保留原式：`abs(U(s,xi)-u_reduced) <= 32*eps64*(1+abs(u_reduced))`。按原圈数恢复未折叠角；恢复后完整函数的实际反解误差也单独记录。这里没有把迭代过程中某一点的正导数冒充整个角区间的连续下界。

可选择 `class Reader(FastMaterialInverseMixin, PositiveTraceNativeField): pass`。这是数值求值选择，不修改旧源、存档 schema 或定义的实际场。K31 原生读者也具有相同接口，但本次没有额外重跑 K31。

## 一次真实小比较

固定18 b4 accepted2，输入SHA `d2c538f65b10f0ea6262d5e831efd17c80116ca958fd6634a9cbb831fac57bfc`。取入口、两coast rim、退出图过渡、terminal平台和准确cut六个截面，每面64均匀材料角，加三个跨周期角，共402点。比较完整n/m/l及物理u、uu导数。

同一份脚本初次从仓库根调用，候选在run report中的相对 `notes/` 路径未能解析，85028/39836c真实exit1；原控制台和退出收据保留。未改变脚本，只从其实际topic工作目录以新输出前缀调用，18872/1e9206真实exit0。

第二次内部耗时13.447572秒、峰RSS75956KiB。六截面旧方法总求值7.857193秒，新方法4.087838秒。两个coast截面的完整chart调用51次分别降到31和23次，退出过渡48降31；准确cut仍一次。总时间包含字段与角两jet求值，不能把这组有限时间外推为全部body加速比。

全部402点的原停止条件满足；新旧完整字段和角两jet最大逐分量scaled差为4.159567e−12，平台/准确cut比较差0。报告保全部实际绝对差、反解误差、调用数与时间，样本实体可重放。不同迭代器达到同一容差后不声称浮点逐字节相同，更不从有限点推出最终全域metric/reach已付。

本helper没有改21/22主求解、旧native定义或18 differential screen。
