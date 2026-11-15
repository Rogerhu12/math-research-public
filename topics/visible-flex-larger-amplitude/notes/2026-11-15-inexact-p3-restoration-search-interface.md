# Request93：保留真实第三残差的非精确 p3 恢复与原三方程求解

日期：2026-11-15（UTC）。作者：/root GPT-6 Astra Pro。状态：独立源码准备完成；本接口不预填运行、根或接受结果。全部新科学运算只允许在公开 `Rogerhu12/math-research-public` Actions。原92源不修改，本地仅源码、AST、原JSON/字节与接线核对。

## 1. 实际92揭示的具体算法限制

真实92是 run `43672921972` / source `1755a4f414a77d41d85eae9a0e1625f55a74be90` / job `132686715503`，全部步骤成功。原 artifact `14144239294`、676336 B、ZIP SHA `f10832bad2ebf3b48a4da501bc0a50b7556e7a839eb86ddd532cab497338d74a` 已完整保留。

原完整 status 为498765 B、SHA `e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e`，schema `R278-original-three-equation-approximate-p3-inner-root-LM-v1`。它的真实最后接受参数是：

```json
[0.6929598480979777, 0.1236195236907518, 0.5225323995570981]
```

其三原单位残差为 `[-233.46281549983243,126623.86001929421,-7.863297485366516e-09]`，完整三项 merit 为 `8016828215.536017`。初始投影和两次外层更新确实按原完整 merit 接受；第三轮的二十个外层试点没有取得可用内层根。原 unit/full112/native/BVP 标志并未通过。

例如原 inner21 最后点的完整 merit 是 `3363859873.8268824`，d3 为 `-1.4999553547574013e-08`；它未达到内层的原 `1e-8` 目标，因而92没有把它送入外层 merit 判定。这不是一个已接受点，也不是严格下降的独立证明。本轮只继承原92完整 `final.parameters`；不继承任何未接受 inner 点，不复用旧 J、merit、FD 或模型状态。

后继算法仍尝试原内层目标，但将“能否供原外层 merit 试验使用”与“是否已达到内层原单位阈值”分开。每个真实残差和最终原阈值完整保留。此变化是明确的新候选算法，不是对旧92的结果重命名，更不是放宽原非线性尾或完整 BVP 的验收。

## 2. 独立源与完整来源闭合

源文件 `geometry_20261115_small_core_inexact_p3_restoration.py`：45133 B，SHA256 `ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e`。新输出目录 `small-core-inexact-p3-restoration`，status `inexact-p3-restoration-status.json`，schema：

```text
R278-original-three-equation-inexact-p3-restoration-LM-v1
```

新源校验十二个既有文件并报告自身，共十三个直接来源。其中原92 `3b48efd71eb696fef66acbe7fbd163bb8dc8ca63287bfa8c4e873a2600fbf9d9` 只承担父身份来源；`ec9`/`1691` 仍是更早父来源。它们的旧搜索循环没有执行。真正直接调用的原方程、完整3×3参数 J、描述/FD、Arb 和完整零核心圆函数均来自不变的 `geometry_20261114_small_core_resonance.py`，SHA `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`。

四个原数学输入不变：accepted `b4d2b98a…`、prepared `0f94dd88…`、true-zero tail-anchor `e788a28d…`、config `01930f3b…`。原78源码恢复、Python/NumPy/SciPy/flint环境、原699 mesh、M112/T112、完整112×112真实零H J、三个原非零target和全4096材料/边界角保持。新源核同原完整输入 SHA；任一非对角真实 J 或零target不能被静默丢弃为此单位三方程模型。

父解析支持原始 JSON 和透明 gzip，但 CLI SHA 始终绑定实际传入文件字节，另核decoded SHA/size。第一个父只能是上面的真实92完整 status；未来本算法自身输出只能在完整 source closure 和最后接受点语义都完全一致时续接。新源不会以早期90 schema冒当前父，也不从保存Jacobian外推新点。

## 3. 线性消去完整保留实际 d3

在一个实际原域内点p，取原三方程 r=(r1,r2,r3)和实际完整原J。仅当J全部有限且J33非零时形成以下有限线性模型。记J11为左上2×2块，b=J[:2,2]，c=J[2,:2]，d=J33：

\[
n_3=-r_3/d,\qquad t=-c/d,\qquad
K=J_{11}+bt,\qquad \rho=r_{1:2}+bn_3.
\]

给定两个外参数方向v12，令v3=n3+t v12。在精确线性代数中，直接代入得

\[
r+Jv=\begin{pmatrix}\rho+K v_{12}\\0\end{pmatrix}.
\]

这只是当前有限线性系统的块消去，不需要当前非线性r3为零，也不证明邻域存在隐函数。实际代码以原binary64数组形成上述量，保留它实际得到的 `r+Jv` 三个分量，包括第三分量的浮点读数；没有把保存的r3或第三线性残差强行写成零。

K每列以原`hypot.reduce(abs(K),axis=0)`形成正尺度D；严格零列用1作为尺度，两列均保留。A=K D^{-1}，以eta=0.1求4×2增广最小二乘

\[
\min_z\|\rho+Az\|_2^2+\eta^2\|z\|_2^2,
\qquad v_{12}=D^{-1}z,\quad v_3=n_3+t v_{12}.
\]

使用`numpy.linalg.lstsq([A;eta I],[-rho;0],rcond=None)`，不构造正规方程。所有方向、尺度、完整原J动作、秩/奇异值和实际r3保留。阻尼罚项只属于方向模型，没有加到原非线性残差或原merit中。一般非零r3下，normal correction本身不保证原merit下降，因此必须直接检查本方向的原完整斜率

\[
g=r^T(Jv).
\]

若g非有限或g>=0，明确停止该实际方向，不预填接受。另保同一个实际2×2 A的可选SVD、rho投影和eta滤波读数。可选读数失败只留观察异常，不推翻已形成方向、不另增试探或验收门；不能把rho投影叫作未经normal correction的r12投影。

## 4. 实际恢复流程及不能混淆的两个标志

外层最多八个方向，每方向保留原二十档alpha=2^{-k}，k=0…19。每档先形成实际seed p+alpha v，然后仅改变p3进行至多十二次Newton更新，每次最多二十档回溯。

内层的目标仍为原`abs(d3)<=1e-8`。每个更新使用当前点的完整原3×3 J，方向为-d3/J33；原node/mid域及原单元异常照常发生并完整保存。只当实际`abs(d3)`严格减小时才更新内层当前点；没有依据预测值或假零残差接受。第一、第二参数逐位保持固定。所有实际中间点都只是恢复探针。

遇到目标达到、方向不可形成、预算用尽或所有内层回溯不能严格减小时，保留最后一个实际有限点。该点本身仍需有同点实际完整有限J和非零J33，才可成为外层候选。若最后一次已取得的J确实在同一参数点，则只复用这一实际同点返回；否则重新调用原完整J。记录最后J参数身份，避免在更新后的点误用上一步J。

两个字段分别为：

- `usable_inner_root`：实际原第三单位阈值已达到，并且同点J有限/J33非零。
- `usable_restoration_point`：实际完整有限点及其同点有限J/J33非零；**不要求**第一标志为真。

后者才控制是否进入外层原merit试验。一个未达阈值的点不会因此被称为根、完成场或已经接受状态。若seed没有有效原域求值，或最后点的实际J不可用，候选仍不可用，原异常/完整报告保持。

每次恢复生成独立`inner-solves/inner-NNNN.json.gz`，含所有steps/trials、实际三残差、完整112右残差/高度、实际3×3 J、原域返回、预算/停止原因以及全调用成本。所有原模型与J调用事件继续完整写入`large-arrays/original-model-evaluations.jsonl`，artifact保全。

## 5. 原完整三项外层验收

本轮不先强制投影父点。fresh parent原求值与原description/FD执行后，以该实际点为起点；最初J来自该fresh description，后续J来自实际接受候选的同点原J。父保存J不会当当前J。

令q为该档真实恢复点，原merit始终是m(q)=1/2 r(q)^T r(q)。只按原规则检验

\[
m(q)\le m(p)+0.2\,\alpha\,g,\qquad g=r(p)^TJ(p)v<0.
\]

保留q的全部真实三残差，包括未达到1e-8的d3。满足原规则才更新外层当前点；未满足的内层点、未接受seed及最后探针均不写成最终父。

实际q-p通常不等于alpha v，因此逐档分别保存seed、真实总参数位移q-p、恢复位移q-seed、实际r3、原merit和原Armijo bound。g清楚标为原seed方向v在当前原J中的模型斜率；不将其冒作未经证明的非线性恢复曲线导数，也不以approximate IFT保证回溯一定成功。原二十档用尽则诚实停止。

## 6. 最后原检查和保持未完成的结论

迭代早停仍逐原单位方程以1e-8判断。最后原完整112行候选标志也保原1e-8定义，与单位早停分开记录。无论搜索预算停止或无法找到接受步，只要流程可完成，均在最后真正接受点（或fresh parent）直接调用原description三档FD、原Arb160bit/depth14标量域、完整699×453零核心圆检查。它们原来的输入、函数、门与范围均不改变。

`success=false`、`native_nonlinear_solver_called=false`、`full_nonlinear_nonzero_lambda_solution_computed=false`、高109当前参数非共振/横截性未证和exact IFT未证保持。原圆仍是零核心参考，不是非零父场。3b9之外完整native tol2e-9、full BVP RMS1e-6/BC1e-11以及本课题闭面全部完成条件均不由此替换。

## 7. 唯一执行和异常保全

预定93只更新现有smallcoreresonance唯一请求路径，不额外dispatch。显式外8/20、内12/20、eta0.1、原unit1e-8、Arb160/14；job60分钟、科学45分钟。实际实现的预算结束或job超时都不是完成证明。所有科学包导入和数学调用在public Actions环境检查之后。

保原publisher `22e640bb`、原artifact always上传、原partial/error记录、普通真实pull/rebase/README检查。完整trace在large-arrays，status与每个inner报告都保留；小readback只复制现有原字段，不重新做科学检查。对较大readback的缩略展示不删除原status或完整artifact。

源与实际92的完整文本差异保存为`source-from-actual92.diff`。源静态回执明确不执行此科学文件、不导入数学模块、不生成任何伪造输入。当前接口仅定义下一实际候选算法，实际结果必须另从本公开Actions读回。
