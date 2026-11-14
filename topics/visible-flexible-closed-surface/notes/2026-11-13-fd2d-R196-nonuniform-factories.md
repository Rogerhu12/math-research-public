# R196 非均匀 metric / curvature factory 实际接入

## 可直接消费的入口

本组消费 [R196](../results/R196-nonuniform-cubic-basis-and-exact-knot-insertion.md)，不新增数学假设或结果号。三个旧来源保持不变：R190 metric、R191 实际曲率/参数两 jet、R196 准确 cubic basis。

新源：

- [fd2d-nonuniform-metric-provider-R196.cjs](../scripts/fd2d-nonuniform-metric-provider-R196.cjs)
- [fd2d-nonuniform-curvature-provider-R196.cjs](../scripts/fd2d-nonuniform-curvature-provider-R196.cjs)
- [fd2d-check-nonuniform-position-factories-R196.cjs](../scripts/fd2d-check-nonuniform-position-factories-R196.cjs)

调用约定：

~~~javascript
const splines = createR196CubicSplines();
const metric = createR196MetricProvider(engine, bundle, {
  ...options,
  radialBasisCount: knots.length - 4,
  radialKnots: knots
}, splines);
const curvature = createR196CurvatureProvider(
  engine, metric, curvatureOptions, createR191Algebra()
);
~~~

knots 是 R196 准确有理 pairs，必须随保存实体保留。只存新的 radialBasisCount 并用旧 uniform factory 恢复，会得到不同的函数，因此新 metric 构造器明确要求 radialKnots，且若 count 不匹配则拒绝。

新曲率构造器直接共享 metric.radialBasis 和 metric.radialCuts 的实际对象，检查准确 knot 列表和 count 一致；不独立猜另一张径向网格。

## 保留的数学和身份

完整 $T,T_s,T_{ss},T_u$、quarter primitive、实际 Gram/法向、全部 $\theta/\phi/Z/\rho$ 参数导数、曲率谱 hinge 和原权重合成公式均沿用冻结来源。仅把径向 centered-cardinal basis 的零至二 jet 换成显式简单 knot basis，并从这些 knots 生成径向 cuts。

新 definition 沿用原 R190/R191 数学 schema；同时新增 implementation、radialBasisDefinition 和 radialBlockLayout，明确这是新的非均匀实现。原 stateLayout 五项完整保留：

~~~text
theta:[0,JK]
phi:[JK,2JK]
height:[2JK,2JK+J]
cutHeight:2JK+J
radius:[2JK+J+1,2JK+2J+1]
~~~

radialBlockLayout 另外说明 $J,K$、每 block 宽 $2K+2$、局部 channel 顺序及全局 cutHeight 索引。普通 dense H/g 输出尚未换 packed 存储；可以由独立 R198 层消费相同布局。

原有限求积 cut 合并容差 $2\times10^{-14}$ 也明确保留在 definition 中。这是有限数值求积表的既有规则，不合并或移动定义本身的准确 spline knots。本次两个插入点远离该尺度。新 cuts 导致新的有限径向目标，不能把新旧不同求积表的完整残差向量说成相同。

半径系数域仍是原统一绝对值盒。由 R196 非负插入行与行和不超过一，准确 prolongation 保留该盒；本次保存值也实际位于原域。没有把负半径或旧 domain guard 绕开。

## 实际一次共同点核

输入是已保存的 J27/433 真实接受态：

[2026-11-12-fd2d-direct-position-R191-J27-curvature-weight02-01.json](2026-11-12-fd2d-direct-position-R191-J27-curvature-weight02-01.json)，

Git blob 为 52f36eb8accb540972bf4c8766db19f41c891008。与已闭 R196 注入相同，插入 $q=3/20,23/60$，得到 J29/465。没有启动 LM、BVP 或 whole normal。

纯 JavaScript/V8 实际执行 684 ms。比较五个相同物理点，包括中央柱、metric 峰附近、真实插入 knot、active curvature 峰、准确 cut。metric 在各径向点比较原 quarter 17 个角行；参数方向为每个旧参数 $.001\sin(i+1)$，以同一个 Boehm 映射注入新空间，全部参数组都有方向。

为了读取旧 metric 的公共点行，测试适配器仅把原 private makeSlice/sliceValues 暴露为 metricRows；其算式和原源均未更改。新 metric 自带这个只读公共点入口。旧 curvature 使用原公开 point API。

| 检查 | 实际最大绝对差 |
|---|---:|
| metric 的 $r_E,r_F$ | $5.55\times10^{-15}$ |
| metric 的完整参数 $Jv$ | $1.44\times10^{-16}$ |
| $X,X_s,X_u,X_{ss},X_{su},X_{uu}$ | $5.43\times10^{-13}$ |
| 上述位置两 jet 的完整参数 $Jv$ | $7.55\times10^{-15}$ |
| 实际主曲率最大绝对值 | $6.12\times10^{-13}$ |
| 曲率 hinge 三行值 | $6.11\times10^{-13}$ |
| 曲率 hinge 的完整参数 $Jv$ | $7.94\times10^{-15}$ |

真实 active 点为 $s=.3935625,u=.88357293$：旧曲率 $9.64609543175175$，新值 $9.646095431751139$，guide $9.5$，两边 penalty 均实际非零，因此该 JVP 核不只是零 hinge 的空检查。中央及 cut 两点位置两 jet 对照差为零。

所有新局部 basis 返回至多四个径向 block。不会按一个小量阈值删除曲率/Jacobian 项；局部性来自 sparse Cox–de Boor 支撑。R198 可以在自己声明的 band 宽度下保留每个真实非零贡献。

完整报告：[2026-11-13-fd2d-R196-nonuniform-factories-check-01.json](2026-11-13-fd2d-R196-nonuniform-factories-check-01.json)。

## 解释范围

本次实数同函数来自 R196 的准确恒等式，浮点差按实际测值记录。它证明的是接入正确性，不证明新离散目标已经下降，不证明连续 metric 或曲率，也没有交付新的 accepted 求解态。主求解应在新 state 中绑定准确 knots、完整新源、原中央和 scalar 定义，再真实计算新有限目标。

完整曲率/metric 连续证书仍由 R193/R194 与实际准确输入盒承担；半径设计的同一性仅对准确注入成立，后续新的 $\rho$ 方向仍会改变物理目标度量。
