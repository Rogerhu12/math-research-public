# R580：同次解析角投影组件完整接口

作者：ChatGPT（AI，amplitude agent）  
日期：2026-11-16

**状态：独立源码和条件证明已完成，未执行科学算术、未创建新请求或运行。** 本接口不宣称实际 strip、投影缺陷、FFT 形成误差或 metric 已付。它是原完整场覆盖的可选同次消费者，不增加科学接受门。

## 1. 交付、来源与发布边界

| 仓库相对路径（本题目录内） | bytes | SHA256 | 作者 Git blob |
|---|---:|---|---|
| computations/geometry_20261116_same_evaluation_analytic_angle_projection.py | 35149 | 0abe4629415a0e9219a50cf248f30bdceb9819b4338189b811101bdadf3d543f | f782b585f74025ab04dfd0bb14f5dad4b359d53f |
| results/R580-complete-complex-angle-strip-and-exponential-tail-alias.md | 22439 | b6cbc74f504ba6cf4bc0694a4080acfffba1be893c74d236db919b5e0c2f36b0 | 521626162800ea09013fa9f964955ab7a19f7a47 |

以上是作者源码/证明对象，不是 Actions raw。完整交付为这两件及本接口三件。交接 manifest 仅传路径/身份，不是新的运行输入，也不要求把可再生的展开输出入 Git。后继 request 必须真正把新增源加入原完整 source pins；单有运行中记录的自身 SHA 不代替外层源绑定。

原来源的完整身份、真实柱坐标和全部数学证明见 [R580 正文](../results/R580-complete-complex-angle-strip-and-exponential-tail-alias.md)。主要祖先为：

- R575：已发表 main 2a43e90a791bb87e2ecea83efe7cc7c1b0786b76，source 24673/d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7。
- R553：已发表 main d1956f73114f35a23d1d7caa323589fa8b7eb690，source 24412/81d33e7135eeba50b7d0b372d82cbcd656f0da34cf3f2691792f865e2dada96b。
- R521：已发表 main f763b778f7fb85d30b4ce341a73054d93fe85dcd，source 18782/4217bf9a30ade1934c473146131067de2ff778ea62bc0b7811b55356a7cd71ad。

没有修改这些来源、当前任何运行或原 scientific predicate。

## 2. 唯一的实际绑定入口

源 schema：

R580-same-evaluation-analytic-angle-projection-v1

公开 binder：

~~~python
observer = R580.bind_loaded_analytic_projection_defect(
    actual_R575_observer,
    strip_width_cap=explicit_positive_rational,
    exponential_terms=explicit_positive_integer,
)
~~~

实际 R575 可来自原已有调用：

~~~python
actual_R575_observer = R575.bind_loaded_projection_defect(actual_R553_tubes)
~~~

R580 检查 type(actual_R575_observer).__module__ 对应的**实际定义模块**，其真实文件必须位于同一个 computations/HERE，basename、完整 SHA、schema 和 BoundProjectionDefect 类对象全匹配。它不遍历模块表取第一个同路径对象，不允许新类借旧 schema 混入。

实际冻结 R575 source 是 geometry_20261116_same_evaluation_full_angle_projection_defect.py；其 SHA 是 d2cfc1e35509486dd77f5f2ae4aecba3c0527b2e16b910be69540a73f3c2d6b7。R580 复用该对象的 tubes/T、api、field/current、M/N、sqrt_bits、budget_check，并核它们与 R553 对象实际一致，field.saved.N 也必须是同一 N。实际 sqrt_bounds 定义模块再次按 R521 pin 绑定。

原 R575 constructor 已经绑定真实 R553、675 系数解释器、R521 和五个 DFT 参考源；其 describe() 完整进入 R580 binding。不得把旧 source table 删掉只留 R580 三个名字。

**不要求先执行 R575.inspect、R575.summary，也不要求其 B2 可用。** 这里只借已付的实际来源/上下文。若旧消费者本来同时运行 R575，则保其独立 inspect/retirement/summary，不把两者结果互相作为前门。

所有新增科学调用仍要求 GITHUB_ACTIONS=true 且 GITHUB_REPOSITORY=Rogerhu12/math-research-public。内部有理 helper 属于此调用内部，不各自建立新环境或新执行权限。

## 3. 参数与继承项

| 项 | 实际类型/约束 | 责任 |
|---|---|---|
| strip_width_cap | Fraction、整数或可准确解释的 rational 字符串；严格正；bool/float 拒绝 | 真实显式政策，不是实际已付 strip |
| exponential_terms | Python int，非 bool，且至少 1 | 所有 0..L 项完整形成；上界分支另覆盖完整余项 |
| M | 原实际正整数 field_modes | 全部 M 模式，不下采样 |
| N | 原实际偶 angular_count，N>=4M+4 | 原网格，所有保留 bins 严格低于 Nyquist |
| sqrt_bits | 原实际 R553/R575 正包围精度 | 同时用于相对 dyadic 上下包围，不改原系数精度 |
| budget_check | 原实际 callable | 所有新增工作消耗原绝对钟；没有新总钟 |
| field/current/api | 原同一对象 | 不重新求 BVP、root、场或 target |
| sigma | 本接口不数值选择 | 两固定符号同一界；实际分支识别仍未付 |

本次没有实际 recipe、h0、L、终端 leaf 或实际 bound。宽度上限不强制随 1/M 缩小；过大的 h0 可使有限指数上界很松或昂贵。有限 L/precision 也可能使最终包围很松；合法政策不等于可达到科学目标。

describe() 返回普通 JSON 可编码 binding，包含：

- 自身实际 file/bytes/SHA；
- actual_R575_source、actual_R575_binding、actual_R521_sqrt_source；
- bound_policy、bound_policy_identity（canonical UTF-8 + LF 的 bytes/SHA）；
- 实际 field_modes/angular_count/physical_size/layout；
- 同次记录/原退休责任、无需 B2 成功、原 budget 及未新起 clock/child/cleanup 的明确 scope。

## 4. 原 DFS 的实际接点

本组件不拥有遍历、分裂、接受或写盘。未来消费者应在**原**逻辑中增加旁路字段，结构如下；示意的 original_decision/append 指原现存代码，不是本组件新增函数：

~~~python
# 所有对象、原预算和 source pins 已真实绑定。
tube_record = actual_R553_tubes.inspect(cell, actual_scalar_context)
analytic_record = observer.inspect(cell, tube_record)

# 原来的 metric/DFS 决定保持原表达和阈值；不读 analytic_record 作为门。
split = original_decision

tube_retirement = actual_R553_tubes.commit_original_retirement(
    cell, tube_record, split=split)
analytic_retirement = observer.commit_original_retirement(
    cell, analytic_record, split=split)

# 同一原 cell 账本保 tube_record/analytic_record/两份原实际退休记录。
# 若原 R553 inspect/commit 已由既有代码调用，复用该返回，不重复调用。
~~~

不要求重新生成 cell。原先非 prefix cell 时 inspect/retirement 返回 None；它们继续自己的原责任。每个 prefix 原观察和原退休各至多按实际流程登记一次。source 不用计数冒充全角证明：最终还要求原 R553 complete_prefix_constant_cover。

### 4.1 inspect 输入

inspect(cell, actual_tube_record) 真正消费的 R553 return 至少含：

| 原键 | 要求/用途 |
|---|---|
| schema/original_cell/available | 必须是原 R553 cell schema、同 cell；available 非 true 明确未付 |
| coefficient_tube.field_modes/physical_size | 同 M、3M+2 |
| coefficient_tube.radial/prefix_span | 同原径向 interval 与 field.pieces 当前 span |
| coefficient_tube.complete_coefficient_box | 完整 r0..rM,t1..tM,z0..zM，每个准确闭区间 |
| angular_box.angular | 同原 cell 的 q 区间，0<=qlo<=qhi<=1 |
| angular_box.complete_frequency_count/frequencies | M 和完整 [2,4,...,2M] |
| angular_box.d/e | 原物理角导数的完整三个旋转分量 |
| scalar_box.A/mu/nu/actual_same_target_return | 原同一准确径向 target 的角常量及真实 return |
| joint_invariants.d_squared/cross/W/P | 原同一完整 joint 盒；不重选独立中点 |

完整 coefficient/tube return 留在原同次账本。R580 的 source_tube_record_identity 与 coefficient/joint identities 只绑定实际读过的对象；它们不允许以后从已删除 payload 的 SHA 重造原输入。

### 4.2 inspect 输出

正常 prefix 返回 schema 加 -cell，包含原 cell、policy identity、available、完整来源 tube identity、analytic_strip、reasons、error。available=true 只表示该原局部叶的本条件成分已形成，绝不是整圆或全场完成。

analytic_strip 的完整主要组为：

| 组 | 实际字段范围 |
|---|---|
| 布局 | M/N、完整系数数目、全部 frequencies、两个均值保留范围 |
| 来源 | complete_coefficient_box_identity、actual_joint_box_identity、实际 scalar return identity |
| 标量 | A/mu/nu 区间，角常量声明，rho 未被插入 P/速度 |
| 实轴 | D/E/C0、Q/W/P intervals、nu_abs |
| 全部有限角差 | d/e 三分量 slope、a/b、完整 exp factor identity/定义与同对象 cache scope |
| 宽度 | h0、C1/Q1/W1/P1、两 half-margin caps（零 slope 时为 null）、准确 h*、下包围 chosen h、bits |
| 复差 | d/e/cross/Q/W/P 全部差界 |
| 正域 | abs(W) 下界、Re(P) 下界、右半平面主根与双线性说明 |
| 向量界 | 完整 Hermitian C3 norm 上界；direct/near-real 两式及 B/dot/sqrt/numerator 中间界 |
| 责任 | 固定 sigma、两符号同界、没有识别实际 worker/root、local 不等于 fullcircle |

普通 rational 字符串由 Fraction 完整输出；整数、bool、null 类型保留。没有任意树数字编码、压缩原科学字段或把缺失值冒 null。源在数学输入异常时保 type/message/actual_phase，并将本诊断标 unpaid。

## 5. 真实退休与全局 summary

commit_original_retirement(cell, diagnostic, split=original_split)：

- split=true：只增加实际 split 计数；全部原 children 仍待付。
- 原 terminal：核同 source schema/cell/policy 及实际正 h/Wgap/Pgap、完整 M/N；合格才累计 min h、max C、min W/P gap。
- 未付：保原 cell、reason、原 evaluation_error、retirement_record_error；first/last unpaid 均保，不从其它叶补值。

最终调用：

~~~python
necessary = observer.summary(
    original_coverage=actual_original_coverage,
    complete_cell_ledger=actual_complete_ledger_identity,
    original_error=actual_original_error,
    original_stop=actual_original_stop,
    close_errors=actual_close_errors,
)
~~~

内部调用原 R553 metadata summary，不重求场。只有原 complete cover、全部 observation/retirement/split/terminal counters 相同、terminal>0、paid=terminal、unpaid=0、pending=None 同时成立，才形成全局条目。**没有要求原 metric/B2 成功。**

完整 -necessary 对象保：

- binding、实际原 R553 summary identity、实际完整 exp-factor identity；
- complete_original_cell_ledger 和同结果内原 coverage 的关联；
- 原 DFS/R553 complete 值、全部六个 count 与 exact counter match；
- complete_prefix_analytic_projection_bound；
- 真正全局 bound、global h/C；不完整时这些 global 项不冒成功；
- observed_paid_leaf_extrema（明确非完整 cover 时只是观察值）；
- first_unpaid、last_unpaid、last_observed、unfinished operation、global-bound error；
- 逐叶完整账与所有未访根仍在原 ledger/coverage 的责任；
- phase_scope、未付范围、原科学谓词未改/没有新场查询网格钟子进程清理的状态。

本对象不替原 coverage 的未访地址，也不承诺单独携带全部 cell ledger 行。后继 reader 若选择本对象须完整保它与原完整 scope；不能只挑较小全局数值而丢失败/前沿。

## 6. 独立条件函数及全部尾/alias 输出

源另提供：

~~~python
result = R580.conditional_exponential_projection_bound(
    strip_half_width=h,
    vector_sup=C,
    field_modes=M,
    angular_count=N,
    exponential_terms=L,
    enclosure_bits=bits,
    budget_check=actual_original_callback,
)
~~~

这是**条件函数**：h/C 两个数字本身不证明整圆全纯、固定分支、parity 或同一实际场。observer.summary 才把原同次覆盖责任与该计算连接。函数也必须在原公开 Actions 中运行。

前提是在完整物理角带上同一个旋转向量 v 为全纯，Hermitian norm<=C，pi 周期、实轴 parity=(even,odd,even)，sigma 固定。保持原 phi 而非材料角或 q 误缩放。

输出 schema 加 -conditional-uniform-bound，完整含：

1. M/N/3M+2/layout、physical-angle coordinate、旋转 frame/三复分量范数、h/C 和必须另付实际 strip 的声明。
2. 全部 signed frequencies [-2M,-2M+2,...,2M]、数量、原 grid first/last/count/formula、无重复 endpoint、Nyquist 和最大保留 bin。
3. 准确系数界 ||v_hat[k]||<=C exp(-abs(k)h)、pi 周期和三个 parity。
4. rational_exponential_majorant 的 L、全部项 0..L、准确 r 定义、方向、r 与正 1-r 包围、bits、完整各指数 power/geometric-sum 上下端点。
5. 完整 tail/alias 公式、continuous_Fourier_tail_upper、all_retained_alias_sum_upper、由 disjoint omitted bins 得到的 alternative tail bound、alias_upper_used、最终 uniform defect。
6. 全部方向包围已包含、所有整数 alias/无限偶尾已包含、两个 means、T mean 的严格 parity 前提。
7. 没有支付 actual FFT/trig/profile/root/RHS 形成、solver residual/metric floor，固定 grid 不声称与任意 phase 交换。

准确 h/C/L 定义整个有理主界。最终正幂和用 O(log n) 拼接所有 n 项；它是完整几何和的等价组织，不是只计算部分模态。精度有限时上界可松；r 的上端点等于 1 不代表失败，因为独立包围的正 gap 保全部分母责任。

## 7. 原预算、异常与临时生命周期

新增工作每个实际系数/频率循环、指数缩放/Taylor/平方、sqrt 前、完整幂和层及保留 bin 元数据均调用原 budget。完整 finite coefficient 盒、RHS、trig grid、FFT、BVP 均不在本源重新计算。

exact/value helper 只准 Fraction/int/rational string，拒绝 bool/float 的非明确 lift。构造输入错误可报 ValueError；这不是把新增 domain 状态写回原接受门。inspect 和 terminal 记录中只有以下类被转成诊断 unpaid：

ArithmeticError、ValueError、TypeError、KeyError、IndexError。

RuntimeError 类型资源停止、MemoryError、KeyboardInterrupt、SystemExit 保原类穿透，不清掉实际 pending，不捕获后自动重跑。全局形成若中断，原 recovery 带真实 error/stop 再调用 summary 时不完整，不重试数值工作。各 callback 调用之间的单次整数操作仍可能消耗资源；源没有凭 callback 承诺每条机器指令有独立截止。

缓存只有同 observer 的完整 U_n 列；固定政策/精度/M，全部 M 完成才发布。未完成 cache 不能被标作完整。新增工作消耗原钟，可能改变实际到达前沿；无相同资源前沿或速度保证。

没有 main/CLI/file writer、worker、进程池、信号控制、owned-group 改动或 cleanup API。原 live field/目标/完整 ledger 必须在原 same-job raw 存在期间消费；只保 SHA 不能以后恢复 payload。未来工作流必须保所有原 source/预算/quiet/原必要读回，再沿原授权清理；本组件不自行加 marker 或要求保存 raw 入 Git。

## 8. 必要读回和真实后继接线尚缺项

本次仅交组件。未来若要真正执行，还需显式接：

- 新源 pin 与实际同目录加载；保原 R575/R553/所有 field owner 和原 reference pins。
- 实际政策 h0/L；不能从本文任意填未来数值。
- 每个原 cell 的同次 tube-return/inspect/原退休记录写入原 ledger。
- 在原 summary/recovery 中保本完整 summary、原 coverage/错误/stop/close scope。
- reader 对完整新必要字段的实际选择；原单份 90KB、超限70、原 quiet/清理条件不变。

本文未提供新 request、workflow 或 reader view，不把这些尚未接的调用说成现有 run 已执行。不保证新增必要对象在 90KB 下适配；若真实超限，按原合同返回真实完整文件身份及未返回边界，不能删科学字段假装完成。

R575 的 B2 代数界与本解析界可在未来同时有**同一实际完整场/覆盖**证据时比较；本接口不要求先算 B2，也没有偷换成只有较小结果被保留而丢另一原完整 scope。

## 9. 证明结果如何与原误差责任连接

新增结论仅包围准确有限 Fourier 样本/准确 DFT 重建相对准确连续旋转速度的缺陷。它覆盖所有保留 bin 的无限 aliases，而不是只验证有限网格点。

已有 base 缺陷可经真实共同材料 pullback 和实正交注册/反射转述；固定 parity/grid 投影不可未经实际共轭证明与任意 phase 交换。非对称帽不被假定旋转对称；complex 世界架不被假定 unitary。

以下状态明确保持未付：机器 FFT/三角表/profile/root/RHS 形成；名义标量相对准确 C；原 cubic residual/路径成员；实际 worker 根与固定 sigma；非 prefix 片/帽/collar/cut；rho、材料图、boundary anchors 和全局 relative-metric floor。新严格正 h 只来自原实际正 tube 条件，不提供这几项的替代门。

即使实际原 tube 完整，所得 h 可能极小，C 或有理指数包围可能很松。本文证明有效性和完整来源，未给任何真实参数值、数值进展、终态成功或性能结论。
