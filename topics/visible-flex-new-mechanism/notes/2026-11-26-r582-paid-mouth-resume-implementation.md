# R582 已付真实口参数直接续接核心返回（2026-11-26）

本实现承接 run45800483161/job139842104318 的三条完整 ACTUAL_CIRCLE_SEED，不回放M168/M169/8倍容差的任何向内或向外ODE。原run在完成三份种子后，因比较字段为numpy.bool_而在JSON输出失败；原收据见2026-11-26-r582-paid-seed-json-failure-receipt.md。

## 输入身份和源的分离

新科学文件 scripts/r582_paid_mouth_core_return_20261126.py 导入并准确绑定原源fd4bd864c3e9e96d741b7bc896a1bf6f9d50ba54eda0c02bd898f21bd42427a4。原源文件完全保留；新入口不调用它的main。

新paid_seed_json仅4609 B，固定SHA256 517c1f85592434ed015f2eca6de235fc5750b42a035471df2d4e10c178eb33a7。它包含三条原SEED的原JSON字节/hash、每条实际mouth/共同归一六jets/对数尺度和向内规范量，以及原已付成本。没有把逐cell大表、原stdout或积分数组存入仓库。所有小数逐项来自原日志解析，作为后继的新数值输入。

原圆核81q、实际71/pending75网格及其独立来源仍由原source_state_json保留并经原校验。新paid输入另逐项约束原run/job/source、原M/rtol/atol/max_step/tolerance_refinement及三记录顺序。三条记录必须全已到s=.82，否则拒绝替换。

## 新执行内容

只执行原失败前尚未到达的内容：

- 从最后M169/8实际mouth六jets建立原UndividedReturn。
- 原同一对紧支撑均值控制mu、nu，原盒、原初值(0,0)，保持tail不动。
- 原257线性fit节点、独立细格、完整几何与动态几何极值交换。
- 原24基、最后冻结均值后48/96基的线性返回细化。

原ActualTail对象只用于合作时钟；新入口源码不存在inner_slope、outward或integrate调用。COUNTS中新inner/outer RHS应为0。日志另标new_inner_or_outer_seed_transfers_executed=0，复用口参数以PAID_SEED_INPUT打印，不能误读成新SEED计算。

比较字段显式bool(...)，且复用的JSON数值本身已经是原生标量；三份已付口的标量差在同一新run正确打印。没有为修接口另开一个验证run或再做种子。

## 数学/数值范围不变

原a,z几何、完整不除z_s的两条线性方程、C² Hermite端口、variable-projection条件梯度及rcond/rank/normal-equation报告全部沿用。角指标仍明确是cos2/sin2幅度同时取绝对所得保守谱上界，不叫真实连续角峰。

最佳候选、最佳资格所用细格、最后trial、实际网格、pending/下一proposal、自然OptimizeResult和时钟检查点依原审后版本分别保存。若没有几何合格线性改善，不捏造接受。字段 last_trial_* 指最后一个完成完整 assess 的候选，不指优化器尚未完成评估的每次查询。

原114.013392 s为整个已付seed子进程墙钟，包含导入和序列化失败；没有最终科学时钟。它与下一新科学时钟分别报告，不作为两个同型精确计时强行相加。原29向内cell/480向外段的RHS计数和旧圆核输入成本仍在paid参数中。

## 冻结包与运行

- 新source：20241 B，SHA256 4afa0f904acc14fb892ccbcddf38ea006af9c829f0451c23b0e7f654ce8671e4。
- request-r582-paid-mouth-core-return-20261126.json：12546 B，SHA256 e198c94f773bc136cb9d6d279402723f97e1ba97b5677867a59a2113f0b0b6e1。
- workflow visible-r582-paid-mouth-core-return-20261126.yml：2708 B，SHA256 472d86aa5d26d8d8808f5bc1efee630370ba0b6c12b708b1321872f348b5e363。

单lane/max1；原1800秒合作段、50分钟job，Python3.12.14/numpy2.3.5/scipy1.17.0与固定Actions SHA。仍由原stdlib runner真实双仓pull、核README/QUEUE、剥离凭证后执行科学；仅stdout，无artifact/cache/Git写入。

本地只解析源码AST、核字节hash、输入原记录和依赖闭包；没有导入科学模块或执行科学函数。全部6个绑定已通过静态字节核验。完成门仍未付，必须接着获得实际完整返回及有限非圆改正。
