# 固定物理角后代实时间参考的 cap 独立审查

本次通读新的证明和源码，未重复 prefix203 大批计算。
数学放松与接口核对成立：先对物理角统一控制相邻真实场的三重零商，
再仅在实时间 cap 代入完整有限参考，因此无需额外的参考复时间像门。
真实场的共同复时间解析域没有被省略。

## 版本

| 文件 | SHA256 |
|---|---|
| `scripts/fourfold_phase_real_time_cap_budget.py` | `1e538333e33a7b914f86ca204e5f6542bb8720e4c2b34cc998cc6cb65b75b83f` |
| `notes/2026-11-12-caps-from-real-time-reference-gates.md` | `acf125ffa16f134aea31bf6d372c8c091012d4dfb4adeb82f3f56bb4a625869e` |

## 数学与费用

固定同一准确对象、时间坐标和复物理角后，两个 ordinary 邻芽的
0、1、2 阶时间 jet 准确匹配，使差可除以 `(u-u*)^3`。在以真实
crossing 为中心、半径 `R-|u*|` 的盘使用最大模原理，得到统一商界
`(Mplus+Mminus)/(R-|u*|)^3`。外场模数对整个物理角带统一，因此所得
不等式也对该带统一。

仅在实时间代入同一个 Y，两个小场的 Yu 准确相消。已付的实时间像
门确保 θ=Y 仍在物理角带，正实部 q 门给 `|q|>=m`。单侧 cap 长度 d
的积分费用是 `|h|*(Mplus+Mminus)*d^4/(4*m*rho^3)`；点态费用将
`d^4/4` 换成 `d^3`。相邻芽逐对 telescoping，近重合 knots 的极短
中间芽不能跳过。费用已含一次 |h| 和一次 1/m，主流水线不能再重复
这两个因子。E 中加入积分误差，A/M 的共同大小预算也加入对应项。

该论证只适用于真正 ordinary 接缝。真实转折使用独立的 Q 消根芽，
没有被此三重零商论证覆盖。源码的 C4/C5 multiplicity 门正好支付
当前无限 R33 场的 C2 ordinary 匹配，而非只接受较弱的 C2 scalar 门。

## 实现身份

`real_time_reference_cap` 核对 descriptor、目标和根文件、准确仿射参数、
分支、原段/子段以及准确 PiTime 端点。两个参考门必须同标签带且覆盖
同一准确参考段；整段 Bernstein 控制门可覆盖其准确子段。
它还核对 native 真根包、C4/C5 输入和所用 main germ。将保存的条件
ledger 转成实际 density cap 时，显式检验 `0<=image<physical_strip`
和 `m>0`。

批入口另逐段核对全 q 报告的时间和 coefficient shard 哈希，重新
聚合有向上下界，再接受简单常数 m=3/100、Q=21/20。实轴实值的 Y
沿标签竖线积分给像宽 `S*Q`，没有需要未付的真实流性质。全 q 报告
的全 550 段范围不把 cap snapshot 的前 203 段扩成全腿；输出也明确
保持 `whole_reference_leg_caps=false`。

本审查只确认上述数学及源码连接，不重新授予 prefix203 的数值结果，
不支付 main-germ 的 f-P、有限 density 截断或真实流误差。
