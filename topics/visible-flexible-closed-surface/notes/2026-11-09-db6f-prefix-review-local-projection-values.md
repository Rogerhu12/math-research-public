# 四点投影比较：纯浮点层独审

结论：**PASS，限定于本节列出的四点纯浮点评估与报告解释。** 2026-11-09，coupled_prefix。本人未实现比较器；仅提供其中 M14 第4点的原端点输入。提取层和 Decimal 参照由 independent_geometry 另审，不将本审计冒充整个链条的未参与者独审。

审查对象 `scripts/db6f-tail-local-projection-values.mjs`，SHA256 `99aec526e2cc5c7949a2050f18b3f98c02cd8c270821fbb44a09c6f21b889444`，已全文阅读。输入为已冻结三个 M15 点包及 M14 stage37 点包，合计四点。独立重跑实际 exit 0，**没有调用 root、RHS、RK 或全尾 Jacobian**。新输出 `prefix-review-local-projection-values-replay.json.gz` 与作者输出逐字节同，SHA256 均为 `8146e56b0a1d9f9dcd03d5bc5f81ea955112d2f8f8962ad65d6611f79f8595a3`。

## 已核公式与边界

归一基为 $c_0=1,c_j=\sqrt2\cos(jk\theta),s_j=\sqrt2\sin(jk\theta)$。已逐支核对 `cosProduct` 的常数项与和/差频 $1/\sqrt2$、`sineSquare` 的和频负号，以及 $B^L$ 的 00、0j、同阶、异阶四类项。`analyticUK` 的差频符号正确：$s_i c_j$ 在 $i<j$ 时给负的 $s_{j-i}/\sqrt2$；没有再次把实际频率乘入已含频率的 U 系数。

`q2full` 的三项系数与同一冻结 E/p/pt/L 对应；B 的重建使用 $I+B^L+R_B$，flux 使用 $UK+R_F$。原 B 采用的浮点 `1+am` 与原 guard A 的分组不同，比较器没有把二者交换。原 pointwise q、D、S、sd、P、Pt、L、U 以及投影 quad/B 的逐值重建检查都在独立复跑中通过。

原 q、maxQuad 和 scale 的含义保留；显式低阶投影仅用于所比较的另一个评估值。当前两组 M/N 均满足原强无混叠条件，故采用理想等距基的系数公式有相应实数模型意义，但代码和报告均没有声称它与 literal rounded 表逐位等价。单列的 physical nonlinear momentum RHS 只是原 pref 乘频率后的 nonlinear flux 部分，没有被称为完整 RHS 或积分误差。

## 对报告的核对

已通读 `tail-local-projection-comparison.md` 的冻结版，SHA 与审计 JSON 绑定。报告明确保留一个最高单模变差的反例，使用全模/最高四模最大差表述有限收益；也承认所选最高 $q_2$ 系数尚未到机器噪声量级。

另外只从作者/复跑数据重新计算了新旧 moment 向量差相对原 scale 的最大值，为约 $4.77\cdot10^{-16}$；两个成功控制在新评估下仍低于原 $8\cdot10^{-14}$ 相对 root 停止门。失败点仍有约 $.022$ 的固定 L 残差。因而“这些固定点的改写不能消掉现有失败残差”与数据一致；报告没有进一步声称全局 shooting 不放大小扰动，也没有用这个局部结果解释全部阻尼。

本审不把80/120位一致性改称严格区间证，不给全径向域或无限高模误差界，不支持立即替换活动 engine。完整绑定和复跑状态保存在同名 `.json`。
