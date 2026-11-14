# R170 新尾充分域：闭存接口与一次有限小核

完整证明见 [R170](../results/R170-dyadic-Bernstein-box-for-the-same-flat-tail.md)。次数仍为 15、尾参数仍为 16；只把全局 $b_i\in[0,6/5]$ 换为八段局部 Bernstein 控制的 128 条双边约束。全部旧盒在新盒内。严格例子的准确全局中间系数为 $-17/1920$，局部控制仍在 $[1/128,33/128]$。

## 可直接消费的接口

```python
from fd2d_dyadic_bernstein_tail import (
    DyadicBernsteinControlBox, DyadicBernsteinFlatDevelopableFamily)

box = DyadicBernsteinControlBox()
certificate = box.certificate(b)       # 对实际 binary64 b 做准确有理检查
constraints = box.linear_constraints(b)
# constraints['matrix'] @ db 受 lower/upper 约束；同时给准确有理右端。
# 这是 128 x 16，不是额外 128 个自由参数。
repaired = box.repair_toward_constant(b)
# 返回 controls + info；新参数、真实差、theta 和重检证书均明确保存。
tail = DyadicBernsteinFlatDevelopableFamily(repaired['controls'])
```

矩阵条目是准确 binary64 的 $N/2^{45}$；`S @ b` 的普通浮点求值并未因此变成准确。`certificate` 用整数/有理运算，`linear_constraints` 同时给浮点与准确右端。收缩工具不会原地修改输入，已合法的输入逐字保留。

```python
from fd2d_gc_dyadic_tail_native import (
    DyadicBernsteinTailNativeField, load_dyadic_tail_body_reader)

field = DyadicBernsteinTailNativeField(parent_definition, b)
definition = field.definition()
# 将 definition 保存为 JSON 后：
reader = load_dyadic_tail_body_reader(new_definition_path)
# reader.physical(s, u) 走现有 physical_angular；cut 不冒径向 II jet。
```

完整 new schema 嵌入整个已绑定 parent definition，并列明新 tail override。旧 parent archive、旧类与旧 guard 原样保留；同一原 tail 系数时字段相同，改系数时是明确的新字段。所有 raw P1、真实 mesh、中央、七个 profile 参数、atlas、窗、R153/R155 公式保持原定义，plain lifting 副本同步消费新 tail。旧 `positive_bernstein` 标签仅用于继承的多项式导数公式；新域、类、schema 另行声明，不伪造旧类型名。

未来 solver 需显式接入：新的 family factory、新的 `parameter_domain`、替换 QP 的逐分量 tail bounds 为子盒线性约束，以及显式保存/恢复新 native schema。原 central/profile 域不改。不能只在 QP 添加 $S$ 后保留旧的 $b_i\ge0$；也不能把负 $b$ 直接交当前冻结旧入口。这一闭组没有修改当前 BVP/whole F/J。

## 本次实际退出与范围

命令：

```bash
python scripts/fd2d-dyadic-bernstein-tail-check.py \
  --parent-definition notes/2026-11-12-fd2d-actual-body-native-binding-01-definition.json \
  --out-prefix notes/2026-11-12-fd2d-dyadic-bernstein-tail-01
```

真实 owner session `89903`，首回执 `47b9b3`，完成回执 `fe9dd8`，自然退出码 0；脚本计时约 3.65645 秒。输入 parent 实体仍是 23b4 的 `41b58549…07fd82`，不是本次最新主线 accepted，也没有借给新主态任何证书。

本次完成了矩阵准确 dyadic/行和检查、24 个准确有理限制恒等式、准确严格例子与其实际舍入控制证书、同一旧合法控制下尾值/两 jet/非零参数 JVP 对照，以及两径向点乘两角的完整 native 身份/重载检查。尾值和 JVP 对照最大差均为 0；同控制 native 最大差为 0；新负全局控制的真实 cut 六项与 tail 直接公式最大差约 $1.11\times10^{-16}$。准确 cut 的径向 II 查询继续明确拒绝。

近边界输入取每分量为 `nextafter(1.2,+inf)`。准确域检查先拒绝；明确收缩用 $\theta=1/3377699720527873$，一次保存后的有理重检通过。实际每参数变化为 $-2^{-52}$，不是把越界输入容差放行。准确线段与 binary64 保存值的差也单独记录。

新定义文件包含完整 parent 信息约 67.8 KB。R132/R130/R168 的几何传递由 R170 的解析证明承担。上述小核不是前缀连续正域、Codazzi、metric、真实 cut 高度或闭曲面 reach/held 的证明，也没有运行 body ODE。
