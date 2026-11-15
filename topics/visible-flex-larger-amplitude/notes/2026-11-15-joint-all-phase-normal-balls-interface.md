# R280 独立联合全相位入口：源与实际执行接口

2026-11-15。这里只交付已证明的条件几何结论和独立可执行源；没有本地执行精确算术、没有新的场输入或实际接受结论。原 R62 及所有 fullDN/闭场/cover 源保持冻结。

## 1. 文件

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| geometry_20261115_joint_phase_normal_balls.py | 8454 | c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466 |
| R280-joint-endpoint-all-phase-normal-balls-and-finite-cover.md | 19219 | 6d32cd819d19adeb721780c692100d59a2d361a19f8274f60394a548c3a30aab |
| 冻结依赖 root_mixed_phase_normal_balls.py | 9012 | ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6 |

新源放 computations；证明放 results。新源与冻结依赖必须处于同一源码目录。没有第三方依赖，仅 Python 标准库。没有改动旧计算或数据文件。

## 2. 输入与 CLI

与原 R62 同样，输入对象具有完整 cases 数组。每个 case 必须保留：

| 键 | 含义 |
|---|---|
| name | 可选案例标签 |
| moving_position、fixed_position | 三个准确有理数表示的中心坐标 |
| moving_normal_centre、fixed_normal_centre | 三个准确有理数表示的法向中心，可非单位长 |
| moving_position_radius、fixed_position_radius | 覆盖真实连续块的位置半径 |
| moving_normal_radius、fixed_normal_radius | 包含法向中心数值误差的连续单位法向半径 |
| tau | 原 reach 目标，正有理数 |

所有科学数字必须是整数或有理/十进制字符串。浮点 JSON 数字不被当作准确输入。中心若来自 binary64 实际词，可在 Actions 中把该词准确转换为有理数，但中心的几何误差仍须在相应半径中支付。转换并不证明连续包围。

示意命令：

    python computations/geometry_20261115_joint_phase_normal_balls.py \
      --input "$RUNNER_TEMP/pair-input.json" \
      --sqrt-bits 128 \
      --out "$RUNNER_TEMP/joint-pair-result.json"

main 在加载冻结算术模块之前同时要求 GITHUB_ACTIONS=true 与 GITHUB_REPOSITORY=Rogerhu12/math-research-public；本地不执行。输出路径必须尚不存在。根号位数默认 128，沿原入口显式范围 16..4096；源不会暗中提高位数、改变原 tau 或启动新网格。

本次未创建实际场输入、workflow、request 或虚构的 run/SHA。证明 §280.4 的有理配置是解析的严格扩张例子，可在确有执行需要时作为公开 Actions 的小型算术用例；它不是当前场的局部证书，也不是本题完成证据。

## 3. 数学与实现的最小变化

每个 case 首先调用冻结 R62 evaluate 一次，保留其完整记录；旧距离、四个法向弦余量、两端四次多项式和 Sturm 序列不改。

新代码将旧两个有理多项式准确相加，另把两个原 phase_pi_margin 相加并核对它与新四次系数相同。随后调用同一个原 Sturm 函数。新联合项仅在：

- 新 phase_pi_margin 严格正；
- 新多项式常数项严格正；
- 新多项式没有有限实根；

三项同时成立时为真。

最终无双法向布尔量明确是：

    old-moving OR old-fixed OR new-joint

没有用和替换原两个单端门。因为各端误差项可能为负，单独替换不能声称包含全部旧成功案例。

源同时保留另一个“距离 OR 无双法向”字段。原法向弦不等式通过与该字段分开：零弦满足原法向弦非严格不等式，不能仅据该不等式证明嵌入。

## 4. 输出

schema 为 R280-joint-all-phase-continuous-normal-balls-v1。

顶层记录本源、冻结 R62 源、完整输入 SHA、位数、案例数、完整案例结果、组合规则及作用域。各案例包含：

- original_R62_record：原 evaluate 的完整原记录，不换标签；
- joint_endpoint_certificate：两个原预算的平方、总预算、联合多项式全部升幂系数、phase0/pi 余量、完整准确 Sturm 序列和根数；
- original_single_endpoint_OR、joint_endpoint_pass 及最终 OR；
- new_joint_passes_where_both_old_endpoints_fail：仅比较已计算的布尔结果；
- 距离与无双法向的原语义组合；
- 连续包围、完整覆盖、曲率、实际 reach 和整面完成均未在此认证的明确标志。

stdout 仅输出源/输入/结果 SHA、大小、各类通过数与作用域。完整原记录可在 runner 临时目录用于该次计算；依新 Rule15 不把它作为可重算数据发布到 Git 或 Release。应保存源、参数配方、真实 run、输出 SHA 与紧凑结论。

## 5. 与真正闭场链的连接

后续真实已接受 fullDN 场的 shared-B 连续 cover 可以为原 R241 的混合块对生成这里需要的准确中心与已支付的连续位置/法向包围。在调用此入口之前仍须使用该场实际的：

- 全部二阶场数据、完整均值、单一 SE2、原 g 与 R249 接缝；
- R279 或其他已证明方法产生的连续曲率包围；
- 真实材料块、帽、标记、跨缝及同块的完整覆盖；
- 目标 tau 与真实整闭面 D 的原关系。

这些原责任没有变成新的审批或字节审计门。缺少真实场时，本入口可以作为一个数学算术组件存在，但不能为当前开放前缀生成实际 reach 结论。

R248 的整圆归约只沿其实际条件使用。若一个固定块对在不同相位必须使用不同门，整圆距离或联合门不保证通过；证明 §280.8–9 给出带有效包围的空间—相位有限细分充分条件。本次源没有实施该全曲面细分程序，也没有虚构相关运行。

## 6. 静态核查范围

只完成 AST、冻结依赖 SHA、源码调用与布尔结构检查。未导入新源或依赖，未调用 evaluate、Sturm、平方根或任何科学函数；没有在本地计算示例多项式、范数或余量。

冻结 R62 源在本地仅保一份只读文本副本用于 SHA/AST 对照，非交付的新第三方实现。没有 Git mutation、新科学数据取件或 Actions dispatch；只读 Git 对象中的小文本源码。
