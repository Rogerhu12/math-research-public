# 当前完整原生字段到实际 body / 二 jet 的薄适配

2026-11-12，Astra-visible-flex-fd2d。范围为接口审读、明确分派和一次保存定义的无几何求值核对；不改当前求解、不另开 BVP，不重复 R158 已闭的 42 点/五 jet 原生核。

## 1. 已具备的读取能力和原入口缺口

`fd2d_gc_independent_tail_native_field.py::IndependentTailPositiveTraceNativeField` 已完整支持当前明确布局：raw/中央角阶 $K=31$，尾 Bernstein 控制量 16 个，物理 profile 参数 7 个，总参数 54 个。切片准确为中央 `[0,31)`、尾 `[31,47)`、物理 profile `[47,54)`。它直接读保存的 P1 mesh、完整 correction 数组和参数，不按旧 `2K+1+J` 推测尾维数，不重建、清理或插值节点。

同一 reader 继承已有 R149 图册、R153 coast Gauss-l 和 R155 terminal positive-trace 的完整函数及角向二 jet。它核保存的 nonlinear 定义、全帽支撑/inactive 节点、trace gauge pairs 和实际 atlas mesh；R163 的 129 节点实体不需要改原生公式。今后的 131 节点实体须保存自身准确节点及已经随 mesh 重算的定义包；本次没有生成或核对一个未来 131 节点实体。

旧 `fd2d-metric-bump-body-screen-v2.py` 仍固定实例化 `RawBumpSeedNativeField`。该入口不能正确解码上述独立尾布局，也没有消费完整 R153/R155 字段。另一个独立问题是旧通用 body 函数使用 `.physical(...)`：新完整 native 的该方法包含径向 II jet，在准确 cut 有意拒绝，而 body 重建及切口位置二 jet 根本不需要这个未声明的导数。

| 现有部件 | 本次结论 |
| --- | --- |
| independent-tail native reader | 已有正确完整函数与明确布局；直接复用 |
| `body_initial_from_core`、`body_rhs_from_fields`、`actual_body_twojet` | R124 的固定材料角 24 态公式与维数无关；直接复用 |
| raw body 的 `field_summary`、`cut_comparison` | 真实位置导数/同一个刚体对齐公式可复用；需 body 专用角 jet 视图 |
| 旧 bump body v2 CLI | 原生分派过旧；本次另名薄入口替换分派和报告来源 |
| R125 `fd2d-metric-gc-primitive-continuous.py` | 实际实现是旧 `NativeLogField`、旧准确 clock/chart interval 模型；没有因本次适配而支持当前字段 |

R165 改的是有限方程的求积组合，不改变这些保存数组所定义的完整物理场，因此无需另造 R165 专属 body reader。

## 2. 新接口保持哪些数学对象

新文件 `scripts/fd2d_gc_actual_body_reader_factory.py` 提供：

```python
bind_saved_body_reader(field, *, foundation_definition)
load_actual_body_reader(native_definition)
ActualBodyAngularView(native)
```

`bind_saved_body_reader` 从已经明确绑定的 foundation definition 只取得固定 candidate、中央 moment/mean 包、reference inlet/cache 和 source 身份。**选定实体自身**提供所有节点、系数、参数、counts、窗口、atlas 和 R153/R155 定义。基础包中另一旧字段的证书不转移给新实体。保存的新 native definition 保持原来可 reload 的 schema；body adapter 来源单独保存。

`ActualBodyAngularView.physical(x,u,side=...)` 只调用已有 `native.physical_angular`，其余方法和对象直接委托原 native。完整 native 的 `.physical` / `.evaluate_native` 未改，准确 cut 仍不声明径向 II 导数；没有人为置 $E_s=0$。

若材料角 $u=U(s,\xi)$、$h=U_\xi>0$，原接口已有

$$
l_u=\frac{l_\xi}{h},\qquad
l_{uu}=\frac{l_{\xi\xi}-l_uU_{\xi\xi}}{h^2},
$$

对 $m,n$ 同理。R124 的固定材料角 body RHS 只用 $J,l,m,l_u,m_u,l_{uu},m_{uu}$；实际位置二 jet 的代数读取只需当前 24 态、$a,l$。这就是使用已有角接口的理由，并未增加表面正则条件。真实 $X_{uu}$ 仍由实际角变分取得，未以辅助 $n$ 代替。

新 `scripts/fd2d-native-actual-body-screen.py` 在一个新加载的 driver 模块实例内显式替换旧 `bound_reader`，复用旧 v2 的全部有限积分流程和 raw body 的实际几何/切口比较函数。它不修改旧文件、类或任何活动进程。报告会明确列新 adapter、实际 native source 和未改的 integration driver，不把旧 seed-only reader 写成已消费来源。

## 3. 本次唯一实际小核

输入是不可变的

`notes/2026-11-12-fd2d-raw-bump-reuse23-b0004-accepted-0001.npz`，

SHA256 `41b5854938e7273a3109494442e9b96a929f576844b52faf60e96076e407fd82`。

进程 session `20029`，初 chunk `300980`，最终 chunk `f9e271`，**真实 exit 0**；报告内部耗时约 3.97 秒。实际结果：

- 原 mesh `(129,)`、raw `(129,95)`、parameters `(54,)` 的 dtype、shape、全部 C-order bytes 在 bind 及重新读取新 definition 后均逐字节相同。
- 七个完整定义包原样相等：nested angular、angular atlas、coast reference、Gauss-l、positive trace、seed weight、atlas mesh。
- 当前 coast inactive-l 节点为 66–72；terminal inactive-trace 节点为 124–127；完整 trace gauge pair 数 128。它们来自当前真实 mesh 的原生验证，并未移用旧 123 节点索引。
- 本次原生字段点求值、body ODE、residual/Jacobian、BVP 次数均为零。没有重复已有的原生五 jet 核。

绑定文件为 `...actual-body-native-binding-01-definition.json` 和 `...-adapter.json`；真实小核范围/数组身份保存在 `...-report.json`。新 thin CLI 已语法编译，没有运行 body main。

## 4. 可直接调用的命令

当前已经生成的不可变定义可供未来明确决定的有限后处理调用：

```bash
python scripts/fd2d-native-actual-body-screen.py \
  --native-definition notes/2026-11-12-fd2d-actual-body-native-binding-01-definition.json \
  --out-prefix notes/FRESH-FINITE-BODY-STEM \
  --angles 32 --radial-samples-per-span 2 \
  --rtol 2e-10 --atol 2e-12 --max-step .02
```

**此命令本次未执行。** 对下一真实 accepted 实体，先另名只绑定：

```bash
python scripts/fd2d_gc_actual_body_reader_factory.py \
  --field notes/ACTUAL-NEXT-ACCEPTED.npz \
  --foundation-definition notes/2026-11-12-fd2d-metric-independent-tail-native-check-01-definition.json \
  --out-prefix notes/FRESH-NATIVE-BINDING
```

再把该次生成的 `FRESH-NATIVE-BINDING-definition.json` 给同一 body CLI。不能把本次 23b4 definition 改名后当下一 accepted 的定义。未来节点数量不硬编码；若新 source 或表示真正改变，应明确更新 reader 分派，不按形状猜旧布局。

程序调用也可直接取得 view 后复用 `body_initial`、`body_rhs`、`body_jets`。所有通常需要径向 II jet 的微分诊断仍应直接调用原 native 的相应接口，不能把 body-only alias 当通用径向 reader。

## 5. 最终仍需实际支付的输入

这一小组只接通读取接口，不把当前有限残差场当完成图。后续完整后验仍需：

1. 明确冻结实际 accepted NPZ、native definition、candidate、moment/mean、reference inlet/cache 及全部 source 身份；R153 完整 active coast 上的 $n>0$ 必须属于该同一实体，不能借用旧 22 状态的 R164 证书。
2. 对该实际完整函数支付所选 R119/R125 连续残差及初值误差，或 R124 的真实 frame/位置/角变分求值残差和全域包。现有旧 log 的 R125 interval 脚本不是当前表示的区间 reader；有限 body 点值也不是这份包。
3. 切口采用同一个实际刚体变换，付全圈六个真实位置 jet 的误差及求值误差。旧 `cut_comparison` 的 position-only Kabsch 只产生有限样本诊断，未证明准确 registration 或 C² 接合。若使用 R126 修补，须输入其完整领圈/全角二 jet 预算。
4. 尾的 reference `plane_height=1.25` 不等于实际前缀 cut 高度。实际位置、同轴规范、held 球包、非局部法球、尾/帽交叉和强比例仍按已有 R121/R130/R133 等真实条件支付。

没有增加独审或新门，也没有因这次接口修正改变当前主 BVP 的场、离散目标或运行。
