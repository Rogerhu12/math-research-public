# 实际 raw 终态接真积分 oracle 与新／旧 atlas 的只读绑定

**状态：元数据入口已执行；未来实际 λ1 终态的端到端读取仍待该终态出现。** 本条审查并补上 R41 通用 oracle 的生产读取入口，不求解 BVP、不读取场数组、不复算旧坏 metric。

## 1. 两种入口不能混用

R41 的 `audit_generic_raw_core.py` 有意把旧检查点改成显式的新平面设计：命令可指定新的主／控制宽度和 λ。它的默认值 `.32/.4/1` 不适合直接读取未来实际终态，例如未来实际采用主宽度 `.24` 时，不能再由默认值覆盖。

新增 [actual_integral_binding.py](../scripts/resume_closed/actual_integral_binding.py) 完全使用实际检查点保存的参数。它没有覆盖宽度、λ、q、完整控制、profile 或材料长度的参数入口。`inspect_actual_checkpoint` 检查原完整 prefix／actual tail／outer 接受条件、九个 raw 源及其逐文件 SHA、core kind/path、完整参数维数、全部物理控制、保护反射规范，以及 `exact_circle_core` 与 λ 是否一致。

这些接受条件不包括本题的完整 metric 门。当前 M16 虽通过原接受门，metric 仍坏；本绑定不提升它的可信度等级。

## 2. 新设计与同 g 精化的锚

调用者必须明确选一种模式，代码不在匹配失败后自动换模式：

| 模式 | 固定 atlas 的来源 | 必须满足的条件 |
|---|---|---|
| `new-design` | 这个完整实际终态自身 | 不接受旧 atlas 参数；使用它重新解出的 profile、名义物理 cut 及自身 $L_{\rm bin}$ |
| `fixed-metric-refinement` | 明确指定的原 accepted 锚 | 候选确由 `fixed_metric=True` 求解；完整 profile／tail 物理输入和 $L_{\rm bin}$ 字面一致；物理 core family 一致，频率数不降低 |

固定 core family 指基频、raw kind/path，以及 $a,b_p,b_c,\lambda$、反射中心、η、主频锁定等实际定义。它不把作为未知量求得的 $q,c_j$ 锁死。每层完整向量必须重新读取；R41 证明 raw 每列独立于最终 J，因此增加 J 并追加零才具有明确嵌套含义，之后求解得到的新控制依然要重新验所有界。

源库的清单和 SHA 也保持显式：当前入口只接受已审的九个 raw 源。未来若启用另一套正交控制表示，应增加自己的协议审查，不能用一个旧 kind/path 静默冒充。

## 3. δ 改变后为什么必须使用新锚

原 actual endpoint wrapper 明确禁止 `--fixed`：它从旧 accepted 原参数起步，新的 δ 仍由实际 BVP 求得。原 coupler 的终态写盘式为

```text
frozen_profile.delta = original_profile.delta + solved_parameter[0]
meridian_length = actual_flow.end
```

这些才是新终态的物理 profile 和材料长度，不能继续使用初始化检查点的 δ 或长度。

在其余 profile／bridge 输入保持不变时，真实长度满足

$$
L_*(\delta)=\frac{\delta}{1-\mathrm{ramp}}
\left(\frac1{v_u}+\frac1{v_d}\right)+L_{\rm bridge}.
$$

所以 δ 的变化本身就改变真实 meridian metric 及长度，不是一个新的核心角参数可以抵消的表示误差。新设计模式用该终态自己的 $L_{\rm bin}$ 建立 R31 的共同 atlas；此后所有固定 g 精化严格保留它。

名义 `physical_tail_parameters.rCut/wCut` 定义真实桥积分。`physical_tail_cut` 中经过浮点求积、求导后的 slope／second 仍是派生源值，不作为独立物理输入。Atlas 使用真实 $L_1,L_2,L_3$、固定 $L_{\rm bin}$ 和原同一 cut Hermite 坐标约定；不能以重调物理 bridge 修 seam 的方式冒称原 g。

## 4. q、完整 c 和参考 lift 的身份

终态保存的两个幅度用途不同：

- `actual_primary_amplitude` 进入实际积分 core 和它的真反函数；
- `gauge_amplitude` 乘源有限未知场与初始投影，进入 R39 有限主部的 $q_gV_{\rm in}$。

同 g 精化可以重新求解实际 q。当前真实 M16 就有
`actual q=.03991248545080898`、`gauge q=.04`，因此不能把两者合并。

完整 c 按原参数乘原 scales 得到，全部 binary64 物理值记录为精确分数。新入口不从 R41 的旧全 15c 记录回填，也不自动删掉新高模。R41 的数值区间、R37 的角余项和 R39 的径向预算都只属于各自原输入，新终态 q/c/δ 一旦变化便须绑定自己的新证书。

## 5. 与现有实际读场器的连接

`load_actual_integral(...)` 的顺序是：

1. 做上述完整元数据绑定，按声明选择自己的新锚或保留旧锚。
2. 调用已登记的 `m3_integral_prefix.load_integral_prefix`，检查 source topic、short bridge 和完整 port，并通过原 `load_checkpoint` 解码可能分块的系数。
3. 再次确认实际 core 的全部控制、q、设置未被读场器改变。
4. 把实际 core 及其完整 provenance 传给 R41 `GeneralExactRawM3Core`，从此次宽度和控制重算 β／圆心／二矩投影／真原函数。
5. 以选定锚的物理 profile、名义 cut、原材料长度构造 `TruePrefix`。

原读场器已经安装的一次参考 lift 不被再添加。其 `M3IntegralCartesianPrefix` 表示仍按原定义处理一次 lift 与整个中心 Hermite 修正；新的有限主部编译器也保持同一乘数。每个新进程读取一个源检查点，保持已有 source-module 隔离约定。

如果调用者要求实际圆弧终态，可置 `require_lambda_one=True`（CLI 为 `--require-lambda-one`）；代码将拒绝旧 λ=.02 态。它不会把旧态加上一个 λ1 标签后继续。

## 6. 本次执行范围和剩余验证

本次仅对已存在的原 M16、原 M8 锚执行 CLI 的元数据模式，没有解码网格或求值积分。结果为：

- Intrinsic metric identity 仍为
  `2bb0e06e98b6ae3cfffe3808886895383262d4ef7ee25e67578808dbf8f83d0b`；
- Core family identity 为
  `13dabe7ce03bb0fbafab20598632c12a8b444408a8091cfe574e8113726007da`；
- 实际与 gauge 两个 q 明确保留为不同有理数，J=16，全部 15c 保留；
- 原材料长度仍为 `1.3603133321372538`；
- `exact_circle=false`，完整 metric 门没有被推断为通过。

最终执行 exit 0，tool chunk `0ce59c`，约 .50 秒。命令、源／输入／输出 SHA 和紧凑绑定记录见
[actual_integral_binding_execution.json](../scripts/resume_closed/actual_integral_binding_execution.json)。这是新入口检查，不重复 R41 的积分证书或旧整域 audit。

目前尚没有可用于这里的完整实际 λ1 终态，故没有声称 `load_actual_integral` 已对新 endpoint 做端到端验证。未来终态出现后，使用它自己的全部数据执行这一连接，再付新核的全角余项、径向预算、真实尾共缝及全图验收。匹配 atlas/family 也不等于固定时间范围、空间收敛、全时嵌入或 reach 已获证。

审读的 endpoint 写盘入口为 `resume_m3/couple_m3_raw_circle_endpoint.py` 与 `continue_m3_raw_circle_endpoint.py`；它们的源码未被本条修改。
