# R168 准确删柱的 parent-native / body 消费者

2026-11-12，Astra-visible-flex-fd2d / constructive_geometry。

本组实现 [R168 §8](../results/R168-smaller-corner-caps-and-shorter-cylinder-window.md) 的实际读取入口。它不改父 candidate、NPZ、窗口或活动求解；也不把当前坏有限场重新跑成一份 body。数学定义始终是父完整函数在 $s+\Delta$ 的复合，默认 $\Delta=7/50$。

## 1. 绑定和数学对象

源码 `scripts/fd2d_gc_shortened_cylinder_native.py` 的主接口为：

```python
ShortenedCylinderNativeField(parent_definition, delta="7/50")
ShortenedCylinderNativeField.from_definition(child_definition)
ShortenedCylinderBodyView(native)
load_shortened_body_reader(child_definition)
```

父 reader 由刚闭的 `load_actual_body_reader` 明确加载，所以完整 K31 / tail16 / profile7 切片、保存的 P1 mesh、reference、R149 atlas、R153、R155 和所有 source 身份均先按原 reader 核对。子定义完整绑定父 definition 字节及其全内容，不按旧 `2K+1+J` 猜尾维数。

在新的上半区间上定义

$$
\widetilde a(s)=a_{\rm parent}(s+\Delta),\qquad
(\widetilde n,\widetilde m,\widetilde l)(s,u)
=(n,m,l)_{\rm parent}(s+\Delta,u).
$$

所有完整 atlas/lifting/nonlinear 窗口也由父求值的同一次平移自动消费；没有重新求窗端点或重新投影。$d(s+\Delta)/ds=1$，所以角 jet、已有单侧径向 jet 和 profile 参数方向均直接复合。准确 cut 的径向 II jet 仍遵守父 reader 的原拒绝范围，未额外置零。

这是新的物理度量和较短物理域。原中央曲线、参数向量和完整外字段不变，不声称它是父全局 $g$ 的同域加密，也不声称中央 gap 因删柱改变。

## 2. 确认父中央柱，不要求 raw n 归零

本次父实体是 23b4：

`notes/2026-11-12-fd2d-raw-bump-reuse23-b0004-accepted-0001.npz`，

SHA256 `41b5854938e7273a3109494442e9b96a929f576844b52faf60e96076e407fd82`。

它的 `central_field_definition` 明确给中央柱终点 `.32`。九个中央 P1 行一致，所有 $m,l$ Fourier 系数准确为零；profile 首段准确平柱，全部 bump supports 在柱外，seed 在柱内为常数 1，tail/coast/terminal lifting 在柱内关闭，计算角亦不随径向变化。由实际固定材料角 ODE，整柱严格有 $F_s=0$、$X_s=e_z$。

raw $n$ 最大系数约 $.7075$，它承载实际中央曲率参数，绝非错误或需要抹去的量。消费者完整保留它；也不增加“浮点 raw $n$ 与另一种 core 求值必须逐 bit 相等”的条件。

因此子图的中央初始曲线/标架就是父图原来的中央初始曲线/标架。若已有父实际 24 态值，可调用

```python
native.translate_parent_body_state(state, upper=True)
```

只把实际 $X_z$ 减去浮点代表的 $\Delta$；其余 frame 和全部角变分不变。准确数学关系是

$$
\widetilde X(s,u)=X_{\rm parent}(s+\Delta,u)-\Delta e_z.
$$

该方法没有创造一个父图未保存的实际中间态。下半片用 `upper=False`，对应反向平移。

## 3. 准确平移与浮点坐标分开

`delta="7/50"` 表示准确有理数。若调用者直接传一个 float，则 API 明确按该 binary64 的准确有理值解释；建议用有理字符串避免无意改变定义。

新的积分分点是：删去父坐标不大于 $\Delta$ 的节点，将其余保存节点准确减去 $\Delta$，再加新原点 0。每个保存的父 P1 坐标按其 binary64 准确值记录；子定义同时保存：

- 准确有理平移后的分点；
- 供有限 ODE 使用的 binary64 代表；
- 对应父节点索引；
- 两者的角色及舍入误差语义。

这些点只用于把原函数的 P1 分段明确交给积分器，**没有新插值数组定义子字段**。源仍是完整父函数的复合。子 native 不提供一份伪造的 child coefficient archive；body-only view 的旧 `values[-1]` 兼容入口只用于原通用 cut 检查读取父 cut 的零 correction 行，不能拿它按子 mesh 作 P1 内插。

在命名分点的浮点代表上求值，程序显式选择对应父节点；只有准确相等才触发，不对附近点作 snapping。特别地，子 cut 始终调用父准确 cut 标记，而不是依赖浮点 `child_end + Delta` 恰好相等。普通非命名坐标则使用浮点加法；其误差是数值求值误差，不改变数学复合的定义。

父 profile 的准确分片/命名 cut 语义完整继承。这里没有把父浮点 `end` 新认证为准确解析积分长度。未来准确 profile 区间 reader 可直接查询整个 $[s_0+\Delta,s_1+\Delta]$；无需重算父 phase 积分。父区间包中仍未支付的误差，也不会被本包装层消除。

## 4. 唯一实际小核

实际命令为：

```bash
python scripts/fd2d-shortened-cylinder-native-check.py \
  --parent-definition notes/2026-11-12-fd2d-actual-body-native-binding-01-definition.json \
  --delta 7/50 \
  --out-prefix notes/2026-11-12-fd2d-shortened-cylinder-d014-01
```

session `39711`，初 chunk `a7ec22`，最终 chunk `bb0ef0`，**真实 exit 0**，报告内部耗时约 4.985 秒。

检查只包括四个径向标签与两个材料角：新原点、一个实际保留的 coast 节点、一个普通外点和准确 cut。完整 $n,m,l$ 及其材料角一、二 jet 与**显式映到的父坐标**求值的差为零，目标 $a,a_s,a_{ss},c,K$ 差亦为零。完整参数字节不变，子 definition reload 通过。

父 mesh 129 点，子积分分点 126 点。子 cut 的浮点代表为约 `1.348973178358129`；其数学含义是父相应准确 cut/坐标语义减去 $7/50$。准确 cut 选择回到父 `1.4889731783581288` 的声明端点，保留该处原完整角二 jet。

本次普通坐标求值的显式加法误差为约 $1.24345\times10^{-16}$；子 cut 浮点代表相对其准确平移坐标的误差为约 $9.76996\times10^{-17}$。两类误差分开保存。它们不是新的 metric 或曲率误差证书；尚须由实际连续导数/求值后验传播。

中央初值逐字节相同；用准确柱公式构成的父柱内 24 态经平移后与子初值的差为零。此处没有声称恢复了一个原来未保存的 ODE 中间态。

没有重复 R158 全套五 jet 核，也没有运行 whole F/J、body ODE 或 BVP。

## 5. 直接 body 入口与旧报告标志修正

新 `scripts/fd2d-shortened-cylinder-body-screen.py` 明确支持两个 schema：当前独立尾 native，以及本删柱 wrapper。它只在新加载的 driver 实例内替换 reader 和来源报告，复用旧 v2 的全部有限积分、实际 Cartesian 两 jet、单一刚体 cut registration 公式。

审读时另发现旧 v2 静态报告残留 `auxiliary_l_is_independent=True`；这不适用于 R153/R155 完整字段。新 launcher 把全域的 `auxiliary_l_is_independent` 和 `auxiliary_n_is_independent` 都明确记为 false，不改任何旧闭源或数学公式。因此这个入口也可用于原 independent-tail definition，避免继承旧标志。

未来真正决定做有限 body 后处理时可用：

```bash
python scripts/fd2d-shortened-cylinder-body-screen.py \
  --native-definition notes/2026-11-12-fd2d-shortened-cylinder-d014-01-definition.json \
  --out-prefix notes/FRESH-SHORTENED-BODY-STEM \
  --angles 32 --radial-samples-per-span 2 \
  --rtol 2e-10 --atol 2e-12 --max-step .02
```

**这条 body 命令本次未执行。** launcher 只作语法编译。

为了兼容既有单一刚体比较，`tail` 继续作为父尾的**参考位置模型**，其名义 `plane_height` 不是子图真实高度；最终同一个刚体 registration 决定真实新位置。子图准确关系仍为 $Z_{\rm new}=Z_{\rm parent}-\Delta$，不能从名义尾高读出数值。

## 6. 不转借的全局结论

R168 §8 已给同半片及涉及剩余中央柱的法球继承证明。新上下外片之间的法球、较小原点球包、whole-core held 球、实际 cuff 高度及切口配准仍需由同一实际图支付。定义文件将这些输入明确列为未付。

本消费者是只读 native/body 表示，不是新 BVP 的未知量布局，也没有重算一个新自由列/gauge 系统。若后续要在新的物理度量上重求参数，应另明示该求解表示，而不能把父 coefficient 行数与子积分节点数混用。
