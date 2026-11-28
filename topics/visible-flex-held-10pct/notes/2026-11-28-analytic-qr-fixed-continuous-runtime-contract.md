# 真 QR 固定度量返回到连续前缀证书的实际函数接线

本条核对已有 `analytic/qr_fixed_actual_prefix_continuous.py` 的实际调用链，
没有新增接受门，也没有放宽严格的 $\lambda=1$ 原 QR / full-DN 来源门。
当前尚无真实符合该门的 fixed 返回，不能声称已得到新场的连续证书。

## 来源与数学数据的实际去向

`geometry` 和 `tables` 都先调用 `accepted_fixed`，由原真实 QR 锚和
完整前驱链重核 fixed 返回。它随后才导入保留原树的 Cartesian provider，
因此不会在来源选择之前把另一个源树的同名模块缓存成合法输入。

`load_fixed_prefix` 使用自身 `model.load_model` 和原 `fixed=True`
构造器，不调用原只认 design 的 `actual_m3_metric_model` 去解释自身
返回。首参数仍是 $\log(q_{\rm actual}/q_{\rm seed})$，而物理 $\delta$、
gauge $q$、warp-reference、原字面径向图、整个 profile、mean 节点数和
GL6 规则都来自完整 `fixed_problem`。全部支持模式和完整真核心 lift 保留。

`FixedActualNewMetric` 从真实 fixed 物理参数重建这个同一对象，再构造
原 `FrozenTarget`。其 R87 `up/down` 列表由精确有理多项式逐段展开，
没有旧两段上升形状或旧 $k=0.2,S=0.5$ 的输入断言。每一场仍须自己生成
真正角域表；此处没有搬用旧场的任何数值界。

`FixedActualCutMetric` 的构造器明确替代原只认 raw candidate-H 的初始化。
它调用 `reader.load_complete_tail`，绑定自身最终保存物理 PPoly 端点的
完整 H、对应真实 packet、同一端口、完整谱、完整 native 均值和共同
二 jet。后续 `complete_cut_coefficients`、`cut_angular_tables` 以及所有
区间误差和几何方法仍是原函数。高 planar modes、height modes、零模
均值导数都没有省略。

最终几何、表、metric、cut 报告保留完整 `fixed_problem`、最终物理 H
绑定、物理文件 SHA、实际 provider 来源及适配器来源。原 label 没有
回写或重贴。`require_report` 在继承任何同场补集证书前逐项核这些身份。

## 一次真实函数连接观察

对当前原样冻结源码，独立 Python 进程导入真实模块，实际构造派生类，
并调用已有 `adapted_main` 生成和编译四个 proof main。没有调用这些
main，没有传入 source run，也没有构造假 accepted payload。

全部 6 个声明的原区间源码 SHA 实际一致；4 个生成函数均编译成功。
实际方法解析顺序是：

```text
FixedActualCutMetric, CutMetric, FixedActualNewMetric, NewMetric, object
```

原 cut 的 `cut_weights/evaluate/geometry` 和原 metric 的
`weights/evaluate/enclose` 均通过 Python `is` 对象同一性检查。
这是对真实继承和动态源码替换的运行观察，不是对未存在科学输入的
正向接受测试。

工具会话 `10058`、终态块 `841fa0` 实际 exit 0。
小回执 `held10-analytic-work/qr-fixed-real-loop-linkage-20261128-a/linkage.json`
SHA256 为 `47e9b5924f7bdefbd9936ca4862e3bfbf1a0531c85adf5f8ed99d458f053bd76`。
本条未修改任何已冻结数值或几何源码。

## 真 fixed 返回后的直接命令顺序

下面变量必须指向同一个实际 fixed 场及其完整 final-physical-H bundle，
不是 design、旧 raw-H 场或尚在运行中的摘要。`CUT_WIDTH` 是实际选定并
在 cut、mesh 和尾 placement 中保持相同的切口宽度；旧场的 `.12`
证书不能替代新场对这一宽度的验收。

```sh
python topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/qr_fixed_actual_prefix_continuous.py geometry \
  --source-run "$FIXED_RUN" --outdir "$PREFIX_GEOMETRY" --angular 1536 --batch 8
python topics/visible-flex-held-10pct/scripts/resume_20261128/geometry/cartesian_prefix_curvature_rounding.py \
  --certificate "$PREFIX_GEOMETRY/summary.json" --out "$RATIONAL_CURVATURE"
python topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/qr_fixed_actual_prefix_continuous.py tables \
  --source-run "$FIXED_RUN" --outdir "$PREFIX_TABLES" --angular 1536
python topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/qr_fixed_actual_prefix_continuous.py metric \
  --tables "$PREFIX_TABLES/summary.json" --outdir "$PREFIX_METRIC" --target 9.9e-7
python topics/visible-flex-held-10pct/scripts/resume_20261128/analytic/qr_fixed_actual_prefix_continuous.py cut \
  --tables "$PREFIX_TABLES/summary.json" --geometry-bundle "$COMPLETE_BUNDLE" \
  --base-metric "$PREFIX_METRIC/summary.json" --base-geometry "$PREFIX_GEOMETRY/summary.json" \
  --base-curvature "$RATIONAL_CURVATURE" --cut-width "$CUT_WIDTH" \
  --outdir "$PREFIX_CUT" --target 9.9e-7
```

特别是 geometry 的 binary64 `12.3` 阈值之后，仍须原
`cartesian_prefix_curvature_rounding.py` 对同场完整数据支付精确
$123/10$ 的小差值。cut 继承门会检查这一步的真实来源和严格余量。
上述格数仅是命令参数示例；若实际连续界不能分离，必须依同一场继续
合法加密，不能把本接线记录当数学验收。

原 QR anchor 本身仍用独立 anchor 来源入口，不能直接传进这个 own-fixed
入口。两场同 $g$ 的 C² 比较须继续通过已准备的 anchor/fixed 或
fixed/fixed 合同，而不是仅比较各自声明的模式数。
