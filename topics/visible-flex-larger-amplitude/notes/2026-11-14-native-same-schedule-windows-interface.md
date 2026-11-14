# 原 RK12 调度的 6+6 短块接口

2026-11-14。独立薄模块：

`../computations/geometry_20261114_native_same_schedule_windows.mjs`

它尚未执行任何 RK 或矩阵计算。本地只做 Node 语法和纯源字符串变换/反变换检查。它不会自动触发原生求解、试步或新的 Actions；是否采用仍取决于同矩阵均衡的实际回执。

该模块把 [原 stage J 生成诊断](2026-11-14-native-stage-J-generation-and-propagation-scope.md) 中的“同 schedule 分组”变成可接入现有已验证 seed 恢复链的一个 API。它不是修改 `shootingParts`、`steps` 或 `linearSteps`，也不声称新的完整 DN 已通过。

## 1. 真实目标段与两条原调度

actual28 的 stage43 和 stage58 各自只有一个 profile，`integrationBreakpoints=[]`，都是 12 步，原 `portRatio=1`。

| 原 stage | 实际位置 | 原 profile 参数范围 |
|---|---|---|
| 43 | rawCell0 / rawSegment3 / part4 | $[4/8,5/8]$ |
| 58 | rawCell0 / rawSegment1 / part5 | $[5/8,6/8]$ |

模块继续使用这个**原 profile 对象**，不把它重新参数化到半区间。局部 x 是该原子 profile 的 x，原 h 一律是原算式 `1/12`。两种后台按其原表达式分别保留：

- withJac：原 `78718-tail-fourier-product-flow.mjs` 普通分支，`x=n*(1/12)`。
- no-J：原 core 调用，`x=k/12`，通过原 live `engine.rk4`。

这两个浮点生成式不被冒认为逐位相同。每个实际短块保存每一步 x/h 的 Float64LE bits，以及原四个 RK abscissae `x, x+h/2, x+h/2, x+h` 的 bits。原 profile、原 root policy、原局部 RHS/J、原每步加法括号不变。两个目标无 cusp，因此此第一版明确拒绝拿它处理带 cusp 的新段；未选中的原段仍应走其原完整 flow。

## 2. 实现究竟改了什么

`prepareWindowedFlowSource(originalText)` 首先锁原模块 SHA

`717ac5c64bd8d72391912b46125e3c1815b63173f41df34c7a944b18857d574f`。

它提取原 `flowStateWithJacobian` 函数，只做两项可逆文本变换：

1. 原 `n=0; n<count` 变成显式 `firstStep; lastStep`。
2. 原 h/x 声明之后插入只读 schedule 观察；a/b/c/d 的原表达式、field、increment、state update 和 tangent update 全部保留。

逐项撤销这两处变换必须恢复完整原函数文本。纯源检查得到：

| 源身份 | SHA256 |
|---|---|
| 提取的原函数 | `177cf5f563aecdcab4431d842d8dfdd7f7915667b73fe956c87c48c1571c9fe4` |
| 范围化函数 | `30d86f562b19cf362e51b40179f25770fac95051d52957faecf8004922fe4a36` |
| 两项变换记录 | `fee03d28780e7c23b914185b9b7f35a0642e46c471a2c0a4fb70a18931116d48` |

新函数关闭于**原 live engine 的 `rhsWithJacobian` 对象**，不另造局部数学 RHS。每个短块 tangent 由单位阵重启；其两块 J 因而有新身份，不会冒作 actual28 的长段 J。模块本身不把两块乘回一个巨大长矩阵。

## 3. 可直接调用的 API

以下代码只用于将来的公开 Actions probe；调用前，launcher 必须已完成原 17/19/21/22/23/28 的 H、配置、source、容量、live stages、graphs/gains/far/scales 身份核验。

```javascript
import {createNativeSameScheduleWindows, originalNodeSplitLayout}
  from './geometry_20261114_native_same_schedule_windows.mjs';

const n = 43;  // 另一个明确目标为 58
const cell = dn.tail.cells[n];
const windows = createNativeSameScheduleWindows({
  engine: cell.engine,
  cell,
  sourceTopic: process.env.VISIBLE_FLEX_SOURCE_TOPIC,
  stageIndex: n,
  steps: 12,
  split: 6
});

const fullInput = new Float64Array(226);
fullInput.set(originalStates[n + 1]);
const split = windows.splitPropagation(fullInput, {withJac: true});
// split.inner：原 k=0..5 的全 state/tangent 与原 guard 摘要。
// split.outer：从该全中间 state 接原 k=6..11。
// split.innerShapeJ：内半段形状 J；未施加原端口换算。
// split.outerShapeJWithOriginalPort：外半段形状 J；原 Pi/portRatio 只在出口一次。
// split.exit.out：完整旧坐标的原出口形状。
// split.exit.meanHeight：保留整段均值 state 后按原两项相加式得到。

const noJ = windows.splitPropagation(fullInput, {withJac: false});
// 使用另一条原 no-J x 生成式；不能冒作 withJac 的字节身份。

const layout = originalNodeSplitLayout(576, [43, 58], originalScales);
```

模块只要求和实际场相同的 `M=112,size=226`，并显式支持 `[0,6]`、`[6,12]`、`[0,12]`。最后一项用于必要时与原完整 span 对照，但没有自动重复运行它。调用者记录模块/source/spec 的实际 SHA。

`profile.toString()` 的 SHA 只描述函数文本，**不是完整 closure 几何身份**。必须连同原 source/config、stage 的 part/rawLeft/rawRight/mu、冻结 profile/calibration 的原身份一起使用，不能仅用这个函数文本 SHA 证明同 g。

## 4. 节点顺序、端口和原尺度

原 stage n 的输入方向是旧节点 $n+1\to n$。若其旧节点 n 的新索引为 j，新节点顺序是：

| 新 stage | 输入 → 输出 | 原 RK 步 | 出口端口 |
|---|---|---|---|
| j，outer 半段 | 中间节点 $j+1\to j$ | 6..11 | 原 `portRatio` |
| j+1，inner 半段 | 旧输入节点 $j+2\to j+1$ | 0..5 | 1 |

这与 shooting 列表的 outer→inner 顺序一致；不能把执行顺序 0..5、6..11 直接当作 cell 列表顺序。选择 [43,58] 后新 depth 为 578、节点 579，形状系统增加 448 个未知量和 448 个匹配方程。

`originalNodeSplitLayout` 返回所有 `oldToNew`、新 stage→旧 stage/window、完整显式新尺度和原 σ bit SHA。每个旧节点的 σ 原样保留；插入中间节点先明确取其**原 parent stage 的 σ**。该内部尺度规则是新算法的明示选择，不由新 gains 推导，也不冒作原 σ。

**模块没有构造新 graphs 或 gains。** 原 cut 的全部 H、原 far G、raw-depth、旧节点和旧节点尺度不变。必须避免直接调用会重新 `scaleFor` 的默认新 subdivision 构造器，因为那会以新 gains 改写尺度。

## 5. 均值和实际有限等价的范围

原两个额外 mean 积分 state 不反馈形状 RHS，但它们会参与完整输出。本模块在两半之间保留全 226 项中间 state，因此 probe 组合不会因人为清零 mean state 改变其状态更新次序。

若后来新增 shooting 系统只把 224 个形状量列为独立未知，则内部 mean 不宜再当作新增独立几何条件；完整响应必须按旧原 stage 的调度、原均值累加括号另行读回。不能将“形状无 mean 反馈”扩张成“把每个新半段均值清零、再任意 reduce 仍逐字等于旧完整均值”。

精确实数算术下，若原 12 步映射是 $\Phi_1,\ldots,\Phi_{12}$，新增约束

$$z=\Phi_6\circ\cdots\circ\Phi_1(y_{in}),\qquad
y_{out}=\Phi_{12}\circ\cdots\circ\Phi_7(z)$$

消去 z 就是原离散映射。实际 binary64 的短块 J 重启/矩阵乘加、原状态和根求值误差仍须测量；这里没有将新 J 的误差等同于旧长 J，也没有证明 conditioning 必改善。

## 6. 接到下一实际 probe / 扩展系统所需的最小变更

如 request36 的实际证据需要此分支，可复用冻结 25/28 的原 TailClient 握手和完整 signed-zero seed 恢复。唯一新增 native 请求处理应在原求解之前：

1. 在 43/58 的同一原入端、原 engine/profile 上运行这两个短块，保存完整中间 state、各短块 J、guard 摘要与实际 x/h bits；用 actual28 的 stage-out / guard-mean / 原 J 作已绑定对照。
2. 明确保存对应关系及全原坐标，不在这一 probe 自动 Newton 或声明成功。两块若 guard/finite 失败，保原异常和已完成部分。
3. 若短块证据支持扩展线性系统，旧的 574 个未分组 stage 可继续用同基态 actual28 的原 J；只替换两个原长段为四个新短块并增加两个实际中间状态。**这是一份新 augmented J，有新身份**，不能继续冠 actual28 的整 J SHA。
4. 扩展系统求得方向后，限制到旧节点，真实调用旧原完整 no-J flow、原 σ、cut/far 和原 trial 判据。内部残差很小不能替代原整体 readback；原 tol、guard 和最终 audit 不放宽。
5. 若最终请求完整响应，原整体 mean、端点导数和 fresh audit 按真实原门再读。`linearSteps`、原远端 Robin、所有 mode 和完整 H 始终不改。

本模块提供第 1 步所需实际短块算术和节点/尺度映射；剩余 launcher/hook 应只做这项绑定和保存，不复制新的求解器，不把本 source-only 准备称为实际已改善。
