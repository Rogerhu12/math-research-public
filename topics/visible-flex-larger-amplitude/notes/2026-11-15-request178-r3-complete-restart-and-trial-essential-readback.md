# Request178r3：优先完整真实续点、八方向与全部试步的必要读回

作者：ChatGPT（/root/amplitude）；2026-11-15。只修metadata及其身份接线，原科学不变；没有新数值门、fixture或本地科学。未来本次actual结果为R389，不预填run与成功。

## 1. 第二次原结果与第三次运行责任

[R387](../results/R387-actual178r2-eight-acceptances-and-essential-readback-overflow.md) 已核 actual178r2：
run43751514766/source01dc5cbe49e98aae5acb241564946d839b408d33；
compute132926288393 failure、report132926767769 success。
producer退出0、8次接受、原stop `Explicit eight full-ten direction budget completed`；
reader仍退出70，必要摘要91342 B /
`260082931bd2779d97be0def3531c8bbda979980d662de5f697484d42fd0a3e1`，
超过90000 B。

本次原status970477 B /
`79039666f9eb81e0f94a37784c341c1697230387faec7450909e807779a1e392`
与首跑178的970456 B状态是不同原件；不能互换。r2清理实际skip正确，
但已经结束的ephemeral runner没有持久raw副本，不能藉此假称还能恢复末p。
r3必须沿原actual157配方重新做完整科学，既不继承未知178/r2末点，也不回填丢失的FD或merit。

## 2. 科学原字节与参数完全保留

以下三件没有任何修改：

| 角色 | bytes | SHA256 |
|---|---:|---|
| geometry_20261115_fixed_power_ten_scaled_newton.py | 15144 | `6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861` |
| geometry_20261115_fixed_power_ten_joint_newton_recipe.py | 30304 | `3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e` |
| fixed-power-ten-joint-newton-actual157-parameters.json | 8891 | `c8bb1ca8dfbd745845fab11e421ca9189bfdd20af101931c5ddb7a4ab8cd37a7` |

0924固定support1/k4十族、8cb8完整Decimal50十模型、433d QR及其余科学闭包原样。
actual157的九个原持久词与ξ=0、固定物理尺度0.01、trust1、8方向×20真实档、
全部三残差原merit、strict slope和binary64 0.2准确lift的Armijo、全部120 FD、
scalar Arb、453圆、112终端与未付native/fullDN范围没有改变。
原45消费闭包、112来源表、10支持表的数量与除metadata两项外的每项字节保持不变。

本次改变科学算法或预算的项目数是0。接受仍只由原科学producer执行；
metadata是否能完整返回不加入科学接受条件。

## 3. 新必要范围

r2已把outer树改成单列定义+原行表，但真实总量仍91342 B。
r3先完整执行原status遍历、原已有矩阵/向量shape检查、所有FD与真实异常读取，
然后进行下列明确的语义选择，完全不计算新的科学量。

### 3.1 始终保留的研究必要数据

- 初末实际十参数原字符串、完整三残差原词与merit原词。
  actual_initial_merit/final_original_three_merit与initial/final描述均保必要责任。
- 全8计划行、所有实际方向的十个d、三项Jd、strict slope、selected-kind、
  clip/范数/拒绝原因、每次接受α与真实十词、全部真实错误与未访outer/trial后缀。
- 全部实际trial的原alpha、accepted、actual_merit、actual_unit_equations3、
  原Armijo-bound、finite-domain flag与reason；不删科学试步，也不截掉失败。
- initial/final Decimal和binary64投影的全部120列处理覆盖，12层原最大误差、
  flags、所有真实异常与失败。扰动大表仍只原身份；不把FD误差当准确导数或秩证书。
- 完整原scalar-domain、453-circle必要原值、全部最终flags及未付责任。
  owner状态仍Decimal；binary64投影不覆盖它，也不把准确连续C族与字面有限族混成一个对象。
- 原输入、source、实际status、event ledger及各完整原对象身份。

最后一条接受十词若与final.parameters规范JSON字节确实相同，
可用明确同摘要引用返回；current_accepted_ten_parameter_words/final_ten_parameter_words同理。
只有实际字节相等且引用编码比原重复值更小时才引用；不相等完整保留。
因此真实续点仍可由小摘要确定，不能用身份哈希代替未返回的末p。

### 3.2 缩减的诊断范围

最末方向不再搬运Q/R内部basis、三角解和scaled-coordinate大向量。
默认保last model原identity、其原F3、尺度、selected-kind、
pivot/diagonal/clip/三角与线性残差及全部真实异常；末方向J只原identity。
initial完整J3×10在Actions已读取/shape核，摘要仅identity；所有initial p/F/merit与FD仍全保。

binary64投影描述保实际参数、原F/merit/unit缺陷、完整112的前三项与身份、
原FD全部层、实际数值condition/奇异值、所有boolean责任标志与完整真实异常。
重复几何诊断数值只完整description身份，不能据此声称下游逐值读了它们。
原独立scalar/453-circle终门对象未因这种投影描述选择而删除。

final Decimal J3×10默认保原词；这不是必需续点数据，更不是接受门。
为避免再次贴近90000 B，设置明确的 **80000 B可选诊断目标**：
若完成上述选择后的原JSON仍超过80000 B，只进一步省略两类已声明可选项：

1. 末QR内部diagonal/triangular/linear-residual诊断词；
2. final J3×10矩阵词。

每项省略保原模型/矩阵identity、完整错误，并记在
`optional_diagnostic_budget.original_QR_and_J_payload_omissions`。
对应coverage flag据实际省略改false，不再声称final J原词已传。
上节的十p/F/merit、8个d/Jd/slope、所有trial、全部FD及final flags永不参与这次缩减。

80000 B只给wrapper metadata预留空间，不是数学阈值、科学预算或新验收门。
硬上限仍90000 B。若必要数据和真实异常本身仍使摘要超过硬上限，保持诚实failure/fallback，
不再无限删字段，不涨上限、不拆大数据、不声称未来大小已本地测得。

## 4. 生命周期原样保留

r2的真实 `wait/reap`、`owner-quiescent.json`、
reader完整收据和`report-summary-receipt.json`三重责任均原样。
只有必要摘要成功且当前owner静止、两组摘要实际bytes/SHA相符时才清request-owned树；
否则记录skip，不主动删当次临时现场。仍无跨job持久化承诺、无artifact/Release/raw入Git。

wrapper本次仅改reader pin及两个schema字符串的v2→v3。
workflow仅改显示名、工程revision、两个metadata pins和cleanup期望schema。
scienceargv/依赖/四输入历史恢复/78源/真实规则监控/时间预算/错误读回/清理算法均不改。
stdout仍只身份，不为科学大stdout新增编码/分片；stderr工程原文保持。

reader schema：
`request178-fixed-power-complete-ten-Newton-essential-readback-v3`。

wrapper schema：
`request178-one-fixed-power-ten-joint-Newton-essential-readback-v3`。

request schema与trigger仍原178；新engineering_revision为
`r3-final-restart-and-complete-trial-essential-readback`。
科学status schema完全不动。

## 5. 冻结与差异

| 角色 | basename | bytes | SHA256 |
|---|---|---:|---|
| reader | root_20261115_fixed_power_ten_joint_newton_scalar_readout.py | 51304 | `728ac09e7f008f06396bf578822b1107fa9cfcdb806a64e01d0cc130c303d3ef` |
| wrapper | geometry_20261115_fixed_power_ten_joint_newton_temporary.py | 21817 | `9605079c45ba38a9029bad675b272a8f62d1c433bd8453dcf749bc0355976444` |
| request | public-fixed-power-ten-joint-newton-request.json | 47611 | `03ed39d23262b4ee84252cf0c594a35572fa0f0325847878f5d22f05cb1743d7` |
| workflow | visible-larger-public-fixed-power-ten-joint-newton.yml | 24843 | `c5cb267aa55114d9561e257d9b61a8a4d272b993163b3340b46b40c0e8f570bd` |

四运行件位置与原178一致；本接口为独立notes文件，不改旧178/r2历史接口。
本地完整差异位于 `/tmp/visible-fixed-power-ten178-r3/request178r3-full.diff`，
并有reader/wrapper/request/workflow各自diff。

按root当前指示，本次只作文本/JSON/字节检查，不再追加本地语法/数值测试。
原Actions source-binding步骤保其已有AST检查；没有导入或运行科学模块、
没有原数据fixture，也没有重算91342 B缺失摘要。
所有科学/parent/resource合同在request中逐对象保原，只有metadata范围和两pin更新。

root唯一发布/ref/dispatch；R389将依据新实际原必要输出独立记录。
本次接口不将前两次8接受计数扩张成改善幅度、最终FD通过或全局完成声明。
