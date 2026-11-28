# SC 首次同一计算被动保全原 root96 输出

日期：2026-11-28 UTC。责任会话：`visible-exact-astra-b0d5a16-20261128`。

本次修改发生在 SC 首次科学执行之前。SC 的三个原自然目标和数学 pure
完全不变；不重新运行任一已完成目标，也不新增一个 root norm 目标。
原 `complete_TC_column_errors` 的同一次调用本来就返回每一列的
low/mean root 界、high/mixed root 界、完整 physical root 界及 waist 界。
旧 owner 只把最后一项写入公共 `columns` 对象，其他已算项会丢失。

现在保留全部原字段，同时在同一个完整 `columns` 对象增添
`complete_root_error_records`，包含自然顺序 `column_001` 至
`column_096` 的以下三个原返回值：

- `low_odd96_and_moving_mean_root_error_upper`：原 $d_j$。
- `high_root_mixed_error_upper`：原 $z_j$。
- `complete_physical_root_error_upper`：原 $\sqrt{d_j^2+z_j^2}$。

仅对已有返回值做原 `new_record` 有向序列化，再从保存后的整个对象读回
并逐项确认包含该原上端点。纯函数仍只调用一次，三个自然目标的完成
顺序不变；没有额外的 solve、积分、范数或 receiver 求值。

`passive_root_record_identity` 同时保留完整 P224 actual、完整 TC
positive/negative 对象、原 joint math 的 whole SHA，全部原
`original_received_gains`、完整非零源索引 `[1,2,7]` 及准确组合公式。
metadata validator 要求全部96列和每列全部三个记录，不能接受少数列、
只有六个 receiver 或低频截断。旧 waist96 和两种 signed96 矩阵的字段
与判定公式全部保留。

新增的整个 root96 对象与 waist96 一起保留在同一小报告中，不分块。
该 `columns` 文件预算从45000提升到85000 bytes；完整 publication
上限相应从250000提升到290000 bytes。实际 owner 和公共 worker 均对
整文件执行该上限；topic 的200000000-byte容量规则、120000-byte独立
reserve 和完整容量核验保持不变。科学预算和 arithmetic 参数未改。

后续 CFC 可直接复制第一次 SC 已付费并完整保存的 $e_j$，与原完整
negative root/strict 残差组合，补正 AP96/H96 的真 PDE phase/height 行。
无需再从 $D_j/C_R$ 保守倒推，也无需重算原 SC root/waist 目标。
完整均值、normalizer、独立参数方向和剩余 signed Schur 载体仍保留。

本记录是保存接口的修改，不宣称 SC、CFC 或完整物理 square 已数值成功。
