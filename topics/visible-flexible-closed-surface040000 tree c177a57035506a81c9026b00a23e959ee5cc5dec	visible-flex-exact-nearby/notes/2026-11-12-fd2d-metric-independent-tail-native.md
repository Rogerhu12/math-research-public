# R158 的独立 tail 参数布局：实际 native reader

## 1. 对象与已闭结论

[R158](../results/R158-exact-angular-nesting-with-fixed-tail-degree.md) 只扩大原始/中央角空间，原 tail 仍有 16 个 Bernstein controls。实际新实体为

`notes/2026-11-12-fd2d-nested-angular-k31-tail16-01-field.npz`，SHA256
`19cffa6028804219373ed20be8e29d3d11938b3ebdae16ed8caee2aeb79554c9`。

它保存 123 个径向节点、每点 95 个原始系数，以及 54 个全局参数。准确布局如下：

| 对象 | 个数 / 切片 |
|---|---|
| 原始 `n` 偶模 | `K+1=32`，原始列 `[0,32)` |
| 原始 `m` 奇模 | `K=31`，原始列 `[32,63)` |
| 原始 `l` 偶模 | `K+1=32`，原始列 `[63,95)` |
| 中央曲率参数 | 31，参数 `[0,31)` |
| 正尾 Bernstein controls | 16，参数 `[31,47)`，degree 15 |
| 物理 profile bumps | 7，参数 `[47,54)` |

新读者已经按此布局完成真实小核。它不调用旧 `K+1` tail 解码构造器，也不创建补齐或截短的虚假参数包。旧读者继续按原规则拒绝这份 54 参数实体；旧源保持冻结。

当前实体来自原 warm04 的准确零填充，仍保留原 warm04 的实际几何和残差问题。这里没有求解新 BVP、没有传播 body，也没有将升阶或 native 可读性称为强目标证书。

## 2. 源码与调用

`scripts/fd2d_gc_independent_tail_native_field.py`：23,627 字节，SHA256
`d030b81e792e252be1d44d795d1c393a7a8c8fbf4336319de5bcabe0b2a4bbfd`。

```python
from fd2d_gc_independent_tail_native_field import (
    IndependentTailPositiveTraceNativeField,
)

r = IndependentTailPositiveTraceNativeField(
    field_path,
    candidate_path,
    reference_inlet=inlet_path,
    reference_cache=cache_path,
)

# 全物理材料角；包括准确 cut 的值、一阶和二阶角导。
q = r.physical_angular(s, u, side="right")
# q 中有 n,m,l 与 n_u/m_u/l_u、n_uu/m_uu/l_uu。

# 原生 atlas 坐标；非 cut 内点的完整五个 jets。
j = r.evaluate_native(s, xi, side="right")
# value、_x、_xi、_xixi、_x_xi。

# 仅角 jets 的原生接口同样支持准确 cut。
a = r.evaluate_angular_native(s, xi, side="right")

definition = r.definition()
# 将 definition 原样保存为 JSON 后可迁移重建：
r2 = IndependentTailPositiveTraceNativeField.from_definition(definition_path)
```

源继承已闭 `PositiveTraceNativeField` 的空间求值方法。只有初始化和布局元数据另写；coast、atlas、R153/R155 的定义验证保持原有准确 guard。验证用的小 helper 直接写在新源中，没有运行时 monkeypatch、没有 source-text 执行，也没有改动旧类或已保存数组。

接口保留原 fixed-material 24 列 body RHS/Cartesian two-jet 公式，但本次没有运行它们对应的 ODE。未来真正 body 消费必须使用当时的实际保存场。

## 3. 明确身份及参数验证

构造器要求原 archive 明确保存：

- `modes`、`central_parameter_count`、`tail_parameter_count`、`profile_count`，均为正整数标量；中央个数必须等于 raw `K`。
- `representation_kind = ruling_atlas_coast_Gauss_l_terminal_positive_trace_fixed_tail_degree_v1`。
- `nested_angular_definition` 中的 schema、三个切片、两个 defining source SHA、独立参数个数语义与实际数组完全一致。
- 实际 candidate SHA、固定 base T、物理 bump supports、原始严格递增 P1 mesh、seed、coast、atlas、reference-evaluation、R153 和 R155 全部定义包。

冻结 R158 provider SHA 为
`f61c95a57a88d2fee99c6e57241110f8c3ee453ded1060e02ba31f77912f868c`；其继承 R155 provider SHA 为
`582e85efb95f3f735b6fd19e47a94182462368c1f16aeb75399fa81729cc6e61`。

参数按明示 `[0,31) / [31,47) / [47,54)` 分别交给 `BalancedCurvatureCore`、`PositiveFlatDevelopableFamily` 和 `RadialBumpProfile`。tail controls 从 16 改成 32 会改变有限 Bernstein 函数，故本读者不会做这种代换。实际 terminal `trace_gauge_pairs` 用新的每节点 95 列重新核对；inactive 节点集合仍由保存 mesh 和真实窗端点决定。

`angular_embedding_definition` 若存在则完整保存为来源信息，并核对目标布局。**它本身不证明后来修改高模系数的当前场仍等于旧场。** 本读者也支持此 schema 下真正的非零高阶系数；此时直接求值新实际系数，不截断回 K15。真正零填充同场关系只在本次特定实体上由第 5 节逐字节核对。

## 4. 完整场和 cut 的求值范围

完整场依次为：保存的 P1 correction，加完整 seed/tail/coast lifting，在已保存 R149 atlas 中求值；然后施加原 R153 coast Gauss-l 窗，最后施加原 R155 terminal 正 trace 窗。各次变换均为原已闭函数。角阶增大没有改变物理材料角 `u`、原物理度量、atlas、窗或冻结 reference。

全物理角导仍按真实 atlas 链式公式

\[
f_u=\frac{f_\xi}{U_\xi},\qquad
f_{uu}=\frac{f_{\xi\xi}-f_uU_{\xi\xi}}{U_\xi^2}
\]

计算。原生径向和 mixed jets 沿所选 `side` 使用同一 P1 格斜率及 atlas 单侧径向导数；coast/terminal 窗内部如请求这些 jets，继承的函数仍使用真实分段 `K_s`。只请求角 jets 时不增加 `K_s` 或全局 C³ 条件。

准确 cut 原始 correction 为零，tail controls 非负，目标 `K=0`。因此 reader 在 cut 直接保留准确 tail 的值及角二 jet，包括 `n=m=l=0` 的未弯弧。R155 square-root 的径向导数不由这一角 trace 恒等式决定：

- `physical_angular` 和 `evaluate_angular_native` 支持准确 cut。
- `evaluate_native` 或需要完整径向 II jet 的 `physical` 在准确 cut 明确拒绝。
- 没有静默令 `E_s=0`，也没有声称任意保存 P1 场与 cut 的角二阶迹已连续相接。

新读者保持这些原有作用域，不因换参数布局扩张结论。

## 5. 零填充为何保留同一完整函数

令旧 `K=15`、新 `K'=31`。对每个保存径向节点，旧 `n,l` 的偶模和 `m` 的奇模系数逐字节复制到相同频率的位置，所有新增频率系数为准确正零。保存 mesh 不变，故任意格内 P1 值与单侧 P1 径向导数在相同频率上仍相同。因此三个原始全角函数以及任意存在的角导、径向/混合导完全相同。

中央参数也只添加零系数；同一准确 weighted-mean 基中所有新项恒零，中央曲率/转角/积分位置的定义不变。原 16 个 tail controls 逐字节复制且 degree 保持 15；七个物理 bump 参数及其支持不变。全部冻结 reference 与 atlas 身份相同。

随后作用的 R153/R155 非线性函数及窗不变。它们在共有定义域上对同一输入给出同一输出；按链式法则，其角 jets 也相同。这是准确函数恒等式，不依赖有限样本。小核只检查实际程序正确消费了这些实体，不能替代连续几何证明。

不同宽度 Fourier 求和在浮点执行时可能改变相加顺序。因此下述小差别诚实记录，不能声称求值逐位相等。

## 6. 实际小核

脚本 `scripts/fd2d-metric-independent-tail-native-check.py`：10,765 字节，SHA256
`969932f55e7b0d83ac9e048acb23ab4a131b1d33214df7df714c3e402f327d21`。

旧输入 `notes/2026-11-12-fd2d-positive-trace-warm04-warm.npz` 的 SHA 为
`a0ebb07b210d373b5a9aced7b79137f28fc5f7ffa6a797ea960113f9ee3980ac`；新实体内 `angular_embedding_definition.input` 与此实际输入一致。

实际执行器 session **82192**，初始 chunk `f49649`，最终 chunk `20e169`；子进程真实 **exit 0**。wrapper 13.10643 秒，内部 7.49142 秒，峰 RSS 81,292 KiB。

核对范围为 7 个实际径向位置、各 6 个共同物理材料角，共 **42 个 `(s,u)` 点**：中央、coast rim、coast 平台、两窗之间、terminal ramp、terminal 平台、准确 cut。另在 coast 平台和 terminal ramp 各 6 个原生角点比较完整五 jet。没有全域采样、BVP 或 body 积分。

实际结果：

| 项目 | 结果 |
|---|---:|
| mesh、supports、旧 raw 三组系数、旧中央系数、tail、profile 逐字节复制 | 全部真 |
| 新增 raw/中央系数为准确正二进制零 | 真 |
| 六个原完整定义包保持 | 真 |
| 全部同场值/角导/额外 native jets 最大绝对差 | `2.842170943040401e-14` |
| 相应归一最大差 | `1.8225172618703494e-16` |
| 准确 cut 值与 `tail.cut_port(u)` 差 | `0` |
| 该组 cut 角样本中完全零 II 的个数 | `4` |
| 准确 cut 径向 II query 按原合同拒绝 | 真 |
| definition 重载后同点值/u/uu 差 | `0` |
| 旧 reader 按旧参数维数拒绝新包 | 真 |
| 新旧所有绑定源码结束时 SHA 未变 | 真 |

归一差使用 `max(abs(diff))/max(1,max(abs(left)),max(abs(right)))`。准确 cut 三个角 jet 与旧场逐位相同；非零最大差来自内部角导的有限求和。

复现命令：

```bash
python scripts/fd2d-metric-independent-tail-native-check.py \
  --field notes/2026-11-12-fd2d-nested-angular-k31-tail16-01-field.npz \
  --old-field notes/2026-11-12-fd2d-positive-trace-warm04-warm.npz \
  --candidate notes/2026-11-12-fd2d-flatcut-peak-spacer34-01-cyl032-candidate.json \
  --inlet notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz \
  --cache notes/2026-11-12-fd2d-metric-frozen-coast-reference-01-cache.npz \
  --out-prefix notes/NEW_UNIQUE_STEM
```

本次首核即真 0，没有更换输入、重拟合或调整误差门。完整报告、定义、见证数组及退出收据均在同 stem `2026-11-12-fd2d-metric-independent-tail-native-check-01-*`；外控制台在 `notes/process-observations/`。完整闭存身份由另名 manifest 记录。

该结果只支付独立布局下同一实际场的可重建原生求值。新的强幅度主解、其连续 Gauss–Codazzi/metric 后验、全几何与闭图展示仍由后续真实结果分别承担。
