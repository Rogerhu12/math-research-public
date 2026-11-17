# 原物理尾下的 n4 双模线性设计

本记录建立新的物理前缀度量候选，使模式 4 和 8 的有限线性端口兼容条件同时接近零。
所有原尾参数和字面 DN 保持；没有把端口斜率设为自由设计参数。
线性双零、旋转背景预算和非线性等距存在是三个不同结论。

## 选定候选 root03

参数文件为 `root03-profile.json`：

| 参数 | 值 |
|---|---:|
| outward speed (v_u) | .4 |
| return speed (v_d) | .2644695137018561 |
| radial excursion (\delta) | .02840070836443855 |
| ramp fraction | .45 |
| acceleration edge fraction | .05 |
| cycles | 1 |
| original ShortBridge curvature | 4 |
| original ShortBridge peak fraction | .2 |

真实原 worker 的 m4 端口具有模式 (4,8,\ldots,96\)，SHA-256 为
`2a3412f96702f409b2e074ac23b3223d4e0f1d0fe1f1114e7ae34911a5bf9095`。
其前 8 个值逐字等于原 m4 port8；尾的所有物理参数没有改变。

24 模同步积分给出

\[
 \tau_1\approx5.19\times10^{-14},\qquad
 \tau_2\approx-3.57\times10^{-11},\qquad
 \tau_3\approx-0.658717.
\]

这是双模结果，没有得到三模共振。
容差由 (2\times10^{-12}\) 降到 (2\times10^{-13}\) 时，全 24 模归一化边界量的最大变化约 (1.21\times10^{-9}\)。
该变化是数值对照，不是连续或区间误差界。

用原始、未改动的单模 `BackwardLine` 类再次积分，核心向量为

\[
 (F_4,G_4)=(1,4.94\times10^{-14}),\qquad
 (F_8,G_8)=(-1,-3.52\times10^{-11}).
\]

恢复各段正归一化尺度后，两个原始齐次向量分别约为

\[
 (2016.49045,9.96\times10^{-11}),\qquad
 (-3028.36101,-1.07\times10^{-7}).
\]

因此零点没有依赖把整个齐次向量压到零，也没有使用射影线的任意翻号。
从尾端固定 (G=+1\) 出发，各段只除以正欧氏范数。
这排除了本次已检查的符号图误判；它仍是有限精度的根。

在 ((\delta,v_d)\) 物理参数坐标中，两条件的中心差分 Jacobian 约为

\[
 \begin{pmatrix}
 -5.27493551& .11696390\\
 405.71445&43.22876
 \end{pmatrix}.
\]

将两个差分步长一起缩小十倍，奇异值仍为约 (408.0445\)、(0.6751294\)。
这说明当前有限根附近两参数在所测尺度上具有独立作用；没有声称无限维逆算子一致可逆。

## 背景几何与圆弧窗口

在给定十进制参数被视为精确有理数时，`audit_double_root.py` 直接验证：

- 首个负曲率 ramp 的特征损耗满足 (\chi/R>.147\)。
- 两个 flat ramps 的旋转子午曲率上界均小于 8。
- 原 ShortBridge 的指定曲率为 4，末端曲率与纬向曲率也均小于 4。

实际浮点积分的特征损耗为 (\chi/R\approx.15051658\)，较粗的独立解析下界为约 .14772123。
这些条件只说明 R5 所保证的圆弧保护窗已在首次正曲率区前耗尽，不证明此后失去所有局部对称性或满足椭圆兼容条件。

独立尾背景证书给出相同物理 factory 的总增高区间

\[
 [.017226894332849643,\ .028865103743246846].
\]

其 factory hash 和端口的全部物理参数逐项相同；模式间隔不影响旋转背景。
此证书的证明及来源限制在 `tail_background_reference.json` 中明确记录。
它没有认证本候选的非旋转尾。

使用该尾增高上界、中央圆柱长度 .54，圆背景的球直径采样约为 2.51223；前缀背景高度约 .69789036。
这个尺寸是圆背景的采样预算，不是有限振幅完整闭族的连续直径证书。

独立纯圆弧证书 `circle_budget_exact.py` 使用

\[
 q=.06,\quad R=.1,\quad a=.147,\quad b=.08,\quad
 \alpha=.029,\quad\ell=.54.
\]

它证明：若完整闭族之后满足 (D\le2.65\)、支撑量至少 .08、全曲率至多 12.5，
则相应 counter-hold、握持直径和 reach 的三个比例均达到要求。
这个条件窗口不宣称上述完整几何界已被本线性候选实现。

## 搜索范围与可复现性

首先从原较快 profile 只调 ((\delta,v_d)\) 做了 4 个有限最小二乘试验。
它们终止于非零残差或物理边界；靠快返回速度减小残差的点曲率很大，不能接受。
这只是局部搜索诊断，不是不存在结论。

随后沿 (\tau_1=0\) 的真实根支用嵌套 Brent 法寻找 (\tau_2=0\)，获得 6 个不同 (v_u\)/ramp 的有限双零。
选 root03 是因为它较短，且给所选圆弧留下解析耗窗余量。
端口、完整模式线、搜索轨迹均可由脚本在 scratch 再生；包中只保存紧凑结论和物理参数。

最小线性源码从 `source_reference.json` 中三份明确历史源恢复。
完整尾 worker 源复用已发布 `even_circle/first_batch/recovery` 的闭包；
将本包 `mode4_physical_config24.json` 交给其 `export_original_worker_port.py` 即可再生字面端口。
例如：

```bash
python export_original_worker_port.py \
  --source-topic SOURCE_TOPIC \
  --config mode4_physical_config24.json \
  --out SCRATCH/mode4_port24.json

OPENBLAS_NUM_THREADS=1 python trace_double_branch.py \
  --source-root SOURCE_BUNDLE \
  --port SCRATCH/mode4_port24.json \
  --out SCRATCH/double-resonance
```

`SOURCE_BUNDLE` 是恢复后含 `topics/` 的目录；`SOURCE_TOPIC` 是其
`topics/visible-flexible-closed-surface` 子目录。
重新计算可改变末位数字；结果必须同时检查真实根残差和非零齐次向量，不能只保存一个符号变号区间。

后续双模非线性 BVP 使用新的两参数设计接口及两条完整真实线性 seed。
它属于另一项计算，应另行冻结源码、参数与终态，不能被本线性结论替代。
