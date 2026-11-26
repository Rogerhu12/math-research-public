# R684/R688真实报告的完整源绑定归因入口

2026-11-26 07:18 UTC，Astra-larger-e4e2a2bf-20261126 / solver与root（AI）。

首physical/p4两方向和后继R688使用不同于旧SOC的完整driver/schema，不能交旧 `read_constrained_solver_report.py` 的SOC binder冒读。新增完整入口 [read_mean_metric_solver_report.py](../scripts/resume_20261126/read_mean_metric_solver_report.py)，22920 B，SHA256 `3489a041559a17be2975b8f7c5c39a27b4ab974976a9e0610dcbe153e3e0a98e`。

R684分支核完整2d44a097驱动字节及实际mean/Hessian/v3/point/准确尾来源；R688分支调用b57ab303完整deriver的bind_report，重建全部body和明确source roles。没有只凭一个schema标签判断它执行了哪种QP。已刊driver在旧worktree路径不存在时，R684只接受当前同SHA完整源；R688可显式--driver提供同一个完整派生body。

该程序只读实际已返回的JSON和小源码；普通浮点标量归因也仅在公开Actions执行。输出包括每次真实trial的目标下降/Armijo、是否确实执行了几何、真实失败类别；未执行的几何不能因默认布尔字段为true冒称通过。其q0/qz是代理QP能量而非真实Phi；实际下降与该alpha下的同一个未加阻尼模型比较，不把全步模型增益用于半步、四分一步。当前末face单独列真实记录长度、Pg变化和释放；面内界不称作释放之后的全QP界。

R688另外读取实际粗Gram准备及v5活动面代价、真正附加J/J*/residual入口计数与回退。wrapper/base嵌套调用不相加冒充独立产品，不由跨父的时间差推出加速。失败类别是小字符串列表及等价标量JSON；原长trial表/数组仍留runner，不向公开摘要搬运。

当前已排两次真实归因：首90b9051e报告→`postprocess/R684-first-attribution.json`，R688新方向实际返回后→`postprocess/R688-first-attribution.json`。这不是重跑方向；没有科学数组读取、场求值、J/J*或新fixture。源码仅AST/compile静态核，尚无本入口的实际返回，不提前归因alpha截断。
