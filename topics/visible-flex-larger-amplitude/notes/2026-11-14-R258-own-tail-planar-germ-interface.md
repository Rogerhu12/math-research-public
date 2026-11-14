# R258：完整本场尾部的非平面胚与 R238 输入消费者

## 状态和对象

新增独立入口 `computations/geometry_20261114_full_state_planar_germ.py`，SHA256 为
`6ac3997b756c9c8ec49e6526983d530cb3f92656f555b3da88ca584f6e3bfc62`。
本次只完成源码、AST 和依赖身份核对，**尚无本入口的 Actions 数值回执**；没有可接受的完整新父场时不伪造输入、不拿旧 A 结果替代。

数学依据是 [R258](../results/R258-complete-field-tail-cardinal-marker-chain.md)、[R254](../results/R254-exact-full-prefix-no-planar-germ.md) 的完整前缀结论以及 R238 的条件标记链。本入口不是新的求解器，也不是整题完成判据；不启动 BVP、native tail 或径向 ODE。

对象是同一真实闭组装输入所指定的**完整共享节点实 Hermite 规范形**：前缀保全部物理模式和 z0，并严格使用 assembly 明示的原入口或 R249 入口；尾部使用这个前缀自己的真实 final tail 和 complete readout，保全部 FFT 正频率与完整 Nyquist 项；内 collar 和完整材料角外修补按 R258 的精确端点规范定义。旧 R243 原始四角包不是这个 FFT 规范形，未被复用。

## 精确二进制身份

尾部半径直接从实际 `RefinedTail.r` 各标量调用 `as_integer_ratio()`，没有转成 Python `float`，也没有从显示的小数反推。实际 `node_coefficients()` 仍由已冻结原源生成：原源明确把 FFT 输入转为 binary64，调用 `np.fft.rfft`，再扩成 `np.clongdouble`。消费者不只依赖这段文字，而对每个完整节点实际数组检验：编码为 little-endian complex128 后，扩回 `clongdouble` 必须与原 generated 数组逐项完全相等。否则直接报告接口身份变化，不把截断后的 shadow 当原件。

精确四角分组运算读取**原 generated 标量**的整数比；complex128 仅作为已经证明无损的可移植哈希编码。节点记录包含原实际 dtype、完整形状、全部系数哈希、原节点压缩及解压字节哈希和径向 0/1/2 阶四角差 jets。前缀的 R254 接口本来定义在 binary64 共享物理节点上；本消费者先逐数组检查实际 dtype 确为 f8，再调用该接口，防止将来无声把更高精度节点转成另一个对象。

当前源码没有 `float(...)` 调用。这不表示原 producer 没有浮点运算；相反，原 producer 的 FFT、邻速度二导及其他先前舍入是当前实际节点定义的一部分，并由源和完整输入绑定。

径向 Hermite 的中间系数不从旧 longdouble 多项式另行降精度。消费者由上述**同一精确节点 jets**、相邻精确半径之差重建实系数多项式。它与 producer 独立舍入中间系数及浮点求值的关系仍按 R258 明确列为未付表示误差，不能自动继承旧 metric、curvature、reach 或 Hausdorff 数字。外修补起点同样使用精确 `cut - width`；报告另列 producer 浮点减法所得起点及两者精确差。

## 真实输入和调用

在公开仓库自己的 Actions 中、仓库根目录运行，依赖现有 NumPy/SciPy 环境与已验证接口的 `python-flint==0.9.0`：

```bash
python "$C/geometry_20261114_full_state_planar_germ.py" \
  --directory "$CLOSED" --basename surface \
  --checkpoint "$ACTUAL" --port "$PORT" --config "$CONFIG" \
  --tail-response "$FINAL_TAIL" --complete "$ACTUAL_COMPLETE" \
  --source-topic "$SOURCE_TOPIC" --out "$OUT/planar-germs"
```

其中 `C` 是本课题 computations，`CLOSED` 是本次完整 v3/v4 场的实际闭组装目录。`ACTUAL_COMPLETE` 必须是与 `FINAL_TAIL`、`CONFIG` 绑定的完整 readout；其节点树需仍在 manifest 所指的相对路径。`SOURCE_TOPIC` 是现有公开原源恢复器所得的原数值源目录。输出目录必须为空。

复用 `load_full_bundle()` 的全部来源门，包含真实 checkpoint/port/config/final tail/complete、plan/background/assembly、phase0 mesh 和 normal packet 的字节哈希、完整 scalar/prefix 定义、R249 选择和三组 nodal 身份、完整 H、唯一已记录 SE2 以及完整 mean/gauge。它安装原配准，**不重新拟合**。

若已经有同一 assembly 的 R254 实际回执，可加 `--prefix-report /path/prefix.json`。消费者逐项比较该报告的 producer SHA、checkpoint、完整 prefix definition、全部物理 knots/nodal 哈希以及所有原 witness artifact 哈希，然后复用已有证明，不重复搜索。没有该参数时，直接对刚由本 bundle loader 读取的同一 saved 实例调用 R254，不另造一份前缀节点。

可选 `--held-report /path/held.json` 只接受新版 full-state held 报告，并比较其完整 `complete_field_binding`。即使该条件报告为正，也只记录本场条件输入；没有支付连续误差包络和本规范形的表示关系前，不升级为真实连续像改变结论。

## 算法、输出和精确范围

逐节点完整 FFT 系数的四角差可按频率模 4 分组；这是精确恒等式，不是舍去高频。共同高度背景和空间平移仅从**同半径的差**中消去，没有把它们从曲面定义中删除。材料角在四个 cardinal 点严格固定，由完整正密度保证逆图也固定，所以切口的全部物理节点 0/1/2 jets 可直接精确求值，再按实际 `ap/app` 做径向转换。

每个原尾部径向单元在外修补精确起点处分开。每个分段的四角三重积是次数至多 15 的实多项式；内 collar 也如此。对固定的一组 17 个互异有理半径点寻找一个非零值，就足以证明该整段不存在任何平面开片。未修补段使用精确有理数。混合完整前缀和 native tail 的外修补含声明角的真实 `cos/sin`，消费者使用 Arb 球、默认 160 位，必要时倍增至 2560 位；只有严格球排除零才通过。打印出的浮点旋转矩阵绝不替代精确 SO(2) 作用。

所有分段和节点都检查；一个分段未解便保留未解，不把四角多项式为零解释为全场平面。既有 marker 检查只消费本 plan/assembly 的四个支撑圆，精确检查半径互异、正半径、非零高度、帽内包含、同帽分离和支撑中心仿射行列式；不用 bump 峰顶代替支撑中心。

输出包含 `intent.json`、本次或已绑定的 prefix 证明、`tail.json.gz`、`markers.json`、`summary.json`，以及所有精确见证/节点记录的压缩分块。分块只为保全本场完整证据和遵守单文件限制；不抽掉未过段。summary 中 prefix、own-tail/collar/outer-patch 和 marker 三部分通过时，进程返回 0；这个返回值不表示整曲面已满足 README。

下列字段始终保持诚实的未付状态：同一完整背景及全部绝对均值接缝的 C²、全相位全局嵌入、原 rounded renderer 与本共享节点规范形之间的表示误差、真实连续像改变、全部 R238 假设、实际 `delta_E` 和整个课题完成。R258 的解析结论是：**若**这些剩余条件由同场证据支付，则标记链排除非平凡刚体同像，连续像改变给出严格正的 Euclidean-quotient Hausdorff 距离；本消费者没有制造这个距离的定量下界，也没有新增六 jet 机器精度门。

## 本次静态核对

新源 AST 已通过，三个冻结依赖 pin 与当前原字节逐一一致：

| 依赖 | SHA256 |
|---|---|
| `geometry_20261114_full_state_continuous_cover.py` | `c39012655f36f652bacdbc39087c6934f03e6fde721830785fb0636930ceabe6` |
| `geometry_20261114_large_core_closed_assembly.py` | `e70d27a92bf153e49e50016706db854b339d96d3414d7f4c00a5993e1f7609c0` |
| `exact_20261114_refined_tail_adapter.py` | `6b06db6c7c96078b9fabe403a0b3ade14f8b30b07a78b565ed299c77f840d937` |

未在本地 import 数值模块或运行数学计算；尚未把未执行源码当作实际候选证书。
