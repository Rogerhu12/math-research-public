# R299 独立同轨迹原完整 merit 选择组件接口

作者：OpenAI ChatGPT（amplitude agent）；日期：2026-11-15。对应[完整选择定理R299](../results/R299-same-normal-trace-full-merit-selection.md)。只有独立源码与调用合同；没有请求、实际父配方、工作流或科学运行。已经执行完的135及其冻结三源不修改。

## 文件

`computations/geometry_20261115_nine_control_same_trace_full_merit_candidate.py`，19265字节，SHA256 `d4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf`。

组件包含原 `require_actions`、`norm`、`full_column_qr_solve` 的逐字正文，以及对原 `curved_candidate` 的五处明确局部改动。相对原函数的完整diff为8887字节，SHA256 `6b62dda0412f4ea9f6391e76f2d2ea38ef36542c752f9b0688e1d3c6a165a604`。它不是旧824c或新135 producer；没有把原producer动态改写后仍报告旧SHA。

## 最小可调用API

```python
source_receipt = selection.source_identity(computations_directory)

candidate = selection.curved_candidate(
    np, qr, solve_triangular,
    model, baseline, trace,
    parameters, state, direction, action, frame,
    alpha, args, normal_record, label)
```

位置参数签名与原函数相同。np/scipy原QR和triangular solve由正式producer按原运行环境提供；组件不导入或构造另一个科学模型。`model` 必须是该新producer原先真实构造的九控制family实例，`baseline` 提供原3169的 `original_merit`。实际model/输入/来源绑定由独立producer完整负责，不能只凭helper文件名就推断传入模型正确。

`source_identity` 只核原824c及原0865 family的文件字节和helper自身SHA，不评价方程、不作数值fixture，也不替代新producer的完整来源闭包。真正 `curved_candidate` 执行保原本仓库 Actions guard。没有独立CLI main；只执行此helper文件不能冒称已做候选搜索。

实际原参数预算由producer保留：8个完整方向、每方向20档外回溯、每调用12×20 normal。函数读取原args，不把任何预算静默扩大；半径沿实际父状态续接，不引入0.1重置。

## 保留原工作轨迹

所有原工作语句、工作 `current/w`、法向J/QR、内回溯、域异常处理及停止字符串按原顺序执行。四个原已有merit读取位置增加独立记录：

1. 直接种子的原merit；
2. 已形成的工作行原merit；
3. 原内试探完整字段已写出、内Armijo判断之前的原merit；
4. 原工作返回字段全部形成后的原merit。

只保一个完整影子state快照；只有严格更小的有限原merit才替换它。影子从不进入原normal迭代，不提前停止，不调用额外模型或J。全部原工作调用正常返回后才决定返回对象。

若原工作返回merit与影子最小值平手，保原工作state对象。没有有限影子时也保原返回；种子域失败、未捕获原异常或中断不从缓存伪造正常候选。复制/日志资源失败如实传播，不冒称科学拒绝或原轨迹完成。

选择器允许候选来自内层拒绝点或直接种子，因为这些点已经过原实evaluate的实际域检查且完整三项merit已形成；但它没有完整最终域证书或外接受资格。唯一接受仍由原外层完整三残差 merit/slope/.2 Armijo真实决定。

## 返回值与原记录的准确指代

返回值仍是完整原state字典，包含实际九参数、原三残差、全112右端、传递数组及原评价其余字段。采用完整快照，不能仅保存参数然后重新evaluate，也不能把目标写成残差。

原normal_record所有 `iterations`、inner trials、原评价错误及normal模型错误继续保留。新增字段为：

- `same_trace_selection_samples_columns` 和完整 `same_trace_selection_samples`：按原读取次序记录全部参数、残差、原merit、有限性、法向坐标与替换位置；原直接merit重复读数允许作为不同记录保留。
- `original_working_trajectory_return`：原工作末点的完整返回标量、原stop、误差和是否达到目标。
- `same_trace_full3_selection`：新schema `nine-control-completed-normal-trace-original-full3-minimum-v1`，包含原工作样本/选中样本、两个merit、平手规则、是否换点、原调用完成责任、零新增模型/J调用及有限排序边界。

若确实换返回点，`returned_parameters/equations/constraint_error/normal_coordinates` 与位移、相对步长、切向泄漏、目标容差旗标全部按所选state用原公式读回。原 `stop_reason` 保留但显式仅指原工作轨迹；不能把“工作轨迹达到目标”写成所选点也达到目标。

所选原merit另作一次原函数标量读回，并记录与缓存merit是否同word；它不是新的接受门。外层仍再读原merit，差异/异常/拒绝都按真实原门报告。R299的有限排序事实不冒充精确残差认证。

alpha=0路径保持原直接返回原点、无评价/无normal校正；不虚构一个已完成的影子选择记录。正常原外试探alpha全为正的二进制回溯值。

## 独立producer与reader必须显式接合

后继producer应有新basename、schema、status和source closure；它沿真实父参数/半径重新构造原family，然后把原外循环调用明确接到此helper。其余五个原数值助手、完整外循环、半径更新及final/except/finally可保原正文。旧135的参数/半径格式可以按声明消费，但不得改其来源标签。

如果采用实际135作为父并保其完整27源闭包，则当前闭包须另外加入新helper和新producer，不得丢掉真实父producer。实际源表应按新实现生成；本文不预填任何尚未指定的父run、p、radius或未来SHA。

外层一旦接受所选点，下一方向仍调用原 `model.jacobian` 在实际所选参数处形成新完整J。不能保留工作末点J作为已选点J。原完整初末九列FD、Arb、453圆和全部final职责不改，没有新inner-target/秩/奇值门。

旧135 reader只存部分inner细节示例，不足以完成本新实验的完整选择责任。组件提供：

```python
whole_normal_trace = selection.complete_scalar_trace(normal_record)
```

它返回完整scalar record的副本，无新模型动作。新独立reader必须为每个原outer trial输出该完整normal trace的具名分段组，并保所有原失败、每个候选样本、原工作末点、所选末点和实际outer结论。不能只留首尾失败例子或只报“最小值”。

沿原f57/24c结构分段协议，每片≤90000字节、每组有canonical bytes/SHA和完整part-index；超过单片限制按JSON路径/list范围分段，不丢字段。primary只保索引。完整三项和原全112信息在原final读回继续保留；大state快照只在本次调用内存，不形成新raw归档。

## 批次与停止范围

携带真实final radius的机制与135相同，包含原最后完整拒绝方向的quarter结果。原wrapper的0 accepted、非八方向预算stop、原旗标stop、异常、资源partial与运输失败stop都不变。最多32批、3600秒仅批间检查等是否采用，由主控明确新request；本文没有改变或启动这些预算。

对于同一已完成的normal调用，新增model.evaluate/J数为0；若换点会增加一次原3项merit读回和小维度返回诊断算术。复制和记录不是零墙钟成本。整条后继轨迹可能不同，不能宣称全链调用数不变或保证更快。

## 当前验证范围

只读原小源、文本替换、完整diff、纯JSON来源与SHA。两个数值helper及Actions guard原正文相同；删除五项新增段可逆恢复原curved_candidate完整文本。终端不可用，未声称执行本地AST/编译，更未运行模型或新fixture。

本组件与R299可直接作为独立源码/数学结果发布；后继真正求解必须先有明确的新producer及其真实接线，不能把一个requestless helper的保存冒成实际算法已运行。
