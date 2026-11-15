# actual93：不要求内层先过阈值的原三方程恢复，八次方向均接受

- **类型：数值证据与源码／原件字节核对。** 不宣称低三共振根、非零边值解、原 native 接受或大振幅完成。
- **日期：2026-11-15。** 作者：ChatGPT（exact_refinement）；原候选算法及工作流由主控实现、公开派发。
- **计算地点：** 方程、Jacobian、Schur、SVD、merit、有限差分与 Arb 运算均已在公开 GitHub Actions 完成。本次本地只读 JSON／gzip、核 SHA／字节及字段关联、统计记录数；没有科学重算。

## 1. 实际结论

93 的八次外层方向全部得到原完整三方程 merit／`.2 Armijo` 接受。最后停止原因是 **`explicit outer direction budget completed`**，不是外层二十档全部失败，也不是域错误。原 merit 从 `8016828215.535884` 下降到 `146733.11420722902`。全部 `692` 次原 evaluate 和 `93` 次原完整参数 Jacobian 都返回，没有求值异常或观察器异常。

这次策略允许原内层最后的有限实际点进入外层检验，即使第三单位方程未达到内层 `1e-8` 目标。八个实际接受点全部属于这种情形；原第三残差始终完整保存，没有置零。这付清了“92 的单独内根资格阻止原 full-three merit 下降点进入外层”的一种实际推进方式。它不证明非精确内恢复总会有效，也不将推进唯一归因于一个改动：93 同时加入实际第三残差的线性 normal 修正，并在同一父参数处重新求值。

最后真实接受参数：

```text
[0.5078436152033409, -0.3849212262335502, 0.5911288427829965]
```

原单位方程与完整 112 维右端残差前三项分别为：

```text
unit d:       [-206.33215777138622, 500.8924725765619, -3.79434721027843e-08]
full112[:3]:  [-95.30634009534685, -29.90053194615119, -5.968529647024014e-10]
```

其余 109 个原右残差为带符号零。`original_unit_stopping_tolerance_met=false`、`low_mode_candidate_has_small_full_recorded_right_residual=false`、`success=false`，且没有调用 native。工作流 `success` 不能改写为数学求根成功。以下所有数值来自完整原 status、全部 inner 与原事件账，而不是新的本地计算。

## 2. 实际运行、原件与冻结身份

|项目|原值|
|---|---|
|运行|[43674264245](https://github.com/Rogerhu12/math-research-public/actions/runs/43674264245)|
|执行源提交|`8adc3251a8fe2ee7bcbc5d6d8381631b1558141e`|
|job|`132690828561`，全部步骤包括 publisher 成功|
|artifact|`14145249554`，`visible-mainline-smallcoreresonance-43674264245-1`|
|ZIP bytes|`620340`|
|ZIP SHA256|`16bb4f5542472de72a5d03ef72fc5da113c925de844ff4fbd8a7856f17662d37`|
|科学入口|`geometry_20261115_small_core_inexact_p3_restoration.py`|
|入口 bytes／SHA256|`45133`／`ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e`|
|原方程源|`geometry_20261114_small_core_resonance.py`，`3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`|
|schema|`R278-original-three-equation-inexact-p3-restoration-LM-v1`|
|完整 status|`small-core-inexact-p3-restoration/inexact-p3-restoration-status.json`|
|status bytes／SHA256|`372627`／`0913ea5d90ddb23bd408b33175887b5b24665fe0db8324d873bbe0b08c12a647`|
|原报告耗时|`8.097614818000011` 秒|

主控唯一下载已核 ZIP 大小、SHA、CRC。本审计不再传输 ZIP，也不把本地 `.download-complete` 当原 Actions 成员。解包共 28 个原成员及 1 个本地 marker。对应公开目录为 `notes/public-actions-43674264245-1-smallcoreresonance/`。

`complete-diagnostic-readback.json` 为 `97529` 字节／`e4ed56a106860b462c2b0879bfcbd940d54c6425b92c532dbd45aad13230b276`；`small-core-resonance-readback.json` 为 `21702` 字节／`404de15d168ddd45800b12207773fbf745642fdbbf99b875e96f239c8183a6c8`。两者摘要字段与完整 status 逐字面和 binary64 词核同，本文没有只依赖摘要。

## 3. 真正父输入与 fresh 求值边界

父件是 92 最后**实际接受**点的完整 status，`498765` 字节／`e822be884ac07e2b2c46ac7aba7f589ba5233e86cdbb33ad9c95108cc8dca01e`。本包 `prior-candidate/actual92-p3-inner-root-status.json` 与新科学目录的 `parent-status.json` 两份原件逐字相同，也与已经完成的 92 全字节审计身份相同。

只读取父 `final.parameters`：

```text
[0.6929598480979777, 0.1236195236907518, 0.5225323995570981]
```

没有用 92 最后未接受的 inner probe 替换父点。93 不做初始投影；`initial_projection.performed=false`，fresh 父状态直接进入第 0 轮。

四个数学输入保持：

```text
accepted    b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff
prepared    0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714
tail_anchor e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51
tail_config 01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5
```

四个完整 payload 已在 92 付过字节审计；93 本次将 request／runtime／producer 摘要和 92 完整 receipt 逐项核同，不再下载或用 Git 重读大输入。72 个本次 request source payload 和 producer 声明的 13 源身份均完整核同；后者包含旧 92、resume、damped-search 三个明确的父来源文件，93 不执行它们的旧方向算法。

**同一父参数不许可复用父方程值或父 J。** 原读数是：

|量|92 最后保存|93 同参数 fresh evaluate|
|---|---:|---:|
|d1|`-233.46281549983243`|`-233.46281549983243`|
|d2|`126623.86001929421`|`126623.86001929315`|
|d3|`-7.863297485366516e-09`|`-1.3917459060815845e-07`|
|三方程 merit|`8016828215.536017`|`8016828215.535884`|

本文保留这次有限求值差别，没有本地算差、ULP、条件放大或指定唯一原因。93 第 0 轮使用本轮 `fresh-parent-original-description-FD` 的完整 J；后续每个 J 均核对到本轮事件账的同参数返回。“相同固定零尾 anchor 的 112×112 J”与“当前三参数方程的 3×3 J”是两个不同对象，不能混用。

## 4. 实际 normal＋Schur 算法及原接受规则

将当前完整原单位残差和参数 Jacobian 写成

$$
r=(r_{12},r_3),\qquad
J=\begin{pmatrix}J_{11}&J_{13}\\J_{31}&J_{33}\end{pmatrix},\qquad J_{33}\ne0.
$$

冻结源码形成

$$
n_3=-r_3/J_{33},\quad t=-J_{31}/J_{33},\quad
K=J_{11}+J_{13}t,\quad \rho=r_{12}+J_{13}n_3.
$$

用两列原欧氏尺度 $D$（恰为零的列取尺度 1，仍保留该坐标），显式 $\eta=0.1$，解

$$
\min_z\left\|\begin{pmatrix}KD^{-1}\\\eta I_2\end{pmatrix}z-
\begin{pmatrix}-\rho\\0\end{pmatrix}\right\|_2^2,
\quad v_{12}=D^{-1}z,\quad v_3=n_3+t v_{12}.
$$

在精确代数中 normal 项消去第三线性行；实际浮点代码仍保存完整 `J@v` 与 `r+J@v`，不覆盖第三项。例如最后第 7 轮原报告为：

```text
actual r3                -1.610411785803352e-08
normal_p3_correction      2.1256668760696225e-17
original J33              757603086.3222643
actual Jv third           1.60227361161788e-08
actual (r+Jv) third       -8.138174185472037e-11
```

这些是原 Actions 已存值，既不成为新增接受门，也不将线性消去当成精确非线性 IFT 曲线。

外 trial 从 `p+alpha*v` 得 seed，然后内层只改变 p3，最多 12 次更新、每次 20 档，仍争取原 `abs(d3)<=1e-8`。内层结束后，其最后真实有限点只要有**同点**有限完整 J 与非零 J33，就可进入外层检验。根标志仍按实际阈值填写。

外层仍采用完整原三方程

$$
\phi(p)=\tfrac12\|r(p)\|_2^2,\qquad s=r(p)^T J(p)v<0,
$$

并要求实际恢复点满足

$$
\phi(p_{\mathrm{candidate}})\le\phi(p)+0.2\alpha s.
$$

`actual_total_parameter_displacement` 和 `actual_restoration_displacement_from_seed` 分开保存；实际恢复后位移通常不等于 $\alpha v$。上述斜率属于原当前线性方向，不能冒作一条已证明 IFT 恢复曲线的导数。

外层 8 方向／20 档、内层 12／20、原 unit 及最终 full112 的 `1e-8` 阈值、Arb 160 bits／深度 14 均保持；阻尼罚项未加到原非线性 merit。非零分母、局部曲线和阈值的区别见 [R278](../results/R278-finite-resonance-projective-normalization-and-local-elimination.md)。

## 5. 八次接受的完整原读数

轮号从 0 开始。下表直接取原 `searches`，最后一列是实际接受点的 d3，而非线性预测。

|轮|本轮原 merit|试点数|接受 alpha|接受后的原 merit|接受点真实 d3|
|---:|---:|---:|---:|---:|---:|
|0|`8016828215.535884`|1|`1.0`|`3483426293.6319866`|`2.9190154151453873e-08`|
|1|`3483426293.6319866`|1|`1.0`|`492192629.0230227`|`-4.707006528905516e-08`|
|2|`492192629.0230227`|2|`0.5`|`233211221.31504178`|`-1.1895590933618493e-08`|
|3|`233211221.31504178`|1|`1.0`|`3705654.5586422784`|`-1.0562913910347124e-07`|
|4|`3705654.5586422784`|5|`0.0625`|`3532205.8901866726`|`5.2163879049171163e-08`|
|5|`3532205.8901866726`|1|`1.0`|`337475.3841378977`|`1.0004872215570691e-07`|
|6|`337475.3841378977`|1|`1.0`|`186295.48623162817`|`-1.610411785803352e-08`|
|7|`186295.48623162817`|3|`0.25`|`146733.11420722902`|`-3.79434721027843e-08`|

八个接受点的内阈值标志全为 false；这是改变内层候选资格，不是放宽原最终方程容差。完整原 gdot 分别为：

```text
-15953879456.81151
-6932180998.044287
-979487742.7189149
-464090511.95786214
-7324953.825935682
-6963888.164162733
-623062.1400610778
-328421.3133278802
```

### 5.1 七个拒绝点仍由完整原 Armijo 排除

全部 15 外试点都得到有限实际恢复点及其完整 J；8 接受，7 由原完整三方程 Armijo 拒绝。没有外试点因为缺少有限恢复点被拒。

|外轮／trial|alpha|实际原 merit|原 Armijo 上界|
|---|---:|---:|---:|
|2／0|`1.0`|`364487367.3026608`|`296295080.4792397`|
|4／0|`1.0`|`146261444.2625362`|`2240663.7934551416`|
|4／1|`0.5`|`30595236.80500082`|`2973159.17604871`|
|4／2|`0.25`|`6886133.708246334`|`3339406.867345494`|
|4／3|`0.125`|`3924030.7383943554`|`3522530.7129938863`|
|7／0|`1.0`|`661536.5286760153`|`120611.22356605211`|
|7／1|`0.5`|`182697.16148755196`|`153453.35489884013`|

第 2 轮 alpha 1 的 merit 已下降，但充分下降不够，之后 alpha 1/2 才接受。第 7 轮 alpha 1/2 也属于“下降但不够”。第 4 轮 trial 2 虽然是唯一达到内根阈值的点，仍被 full-three merit 拒绝。93 没有将外检验退化成只看 d3 或任意下降。

## 6. 全部十五个内层恢复

15 个完整 gzip 的大小／SHA、全部数值词、每个 current／trial 与事件账关联均已核。共有 91 个内层 current J、361 个内 trial、76 次内更新接受。14 个末次停止原因原文为 `all inner backtracks failed original domain or strict actual abs(d3) decrease`；本轮完整事件账没有域异常，不能仅凭组合文本说成“14 次域失败”。

|inner|外轮／trial|current J 数|内 trial 数|内接受数|最后实际 d3|内阈值|
|---:|---|---:|---:|---:|---:|---|
|1|outer-0/trial-0|7|26|6|`2.9190154151453873e-08`|否|
|2|outer-1/trial-0|5|24|4|`-4.707006528905516e-08`|否|
|3|outer-2/trial-0|10|30|9|`4.231762521346785e-08`|否|
|4|outer-2/trial-1|5|24|4|`-1.1895590933618493e-08`|否|
|5|outer-3/trial-0|8|28|7|`-1.0562913910347124e-07`|否|
|6|outer-4/trial-0|6|25|5|`1.615600602838897e-08`|否|
|7|outer-4/trial-1|6|26|5|`-6.667579037728053e-08`|否|
|8|outer-4/trial-2|4|3|3|`4.3761000249930085e-09`|是|
|9|outer-4/trial-3|9|30|8|`-7.691289753979265e-08`|否|
|10|outer-4/trial-4|5|24|4|`5.2163879049171163e-08`|否|
|11|outer-5/trial-0|4|23|3|`1.0004872215570691e-07`|否|
|12|outer-6/trial-0|7|26|6|`-1.610411785803352e-08`|否|
|13|outer-7/trial-0|7|26|6|`-3.936350583759029e-08`|否|
|14|outer-7/trial-1|4|23|3|`4.9839504525587414e-08`|否|
|15|outer-7/trial-2|4|23|3|`-3.79434721027843e-08`|否|

本轮没有“用满 12 次内更新仍未达标”的另一个停止分支。所有内层最终完整 J 都绑定最后真实参数；本轮均可复用同点的最后 current J，没有将前一点 J 搬到新参数。

### 6.1 原存储词显示的局部分辨率现象

仅比较原 JSON 解码 binary64 词、不形成新差／ULP／Newton 步或 RHS，可核出：inner `1、4、12、15` 的末二十档试探参数全部逐词等于该 current。它们保存的 p3 Newton 方向分别为：

```text
inner 1    -5.4914773700369295e-17
inner 4     3.583399950221195e-17
inner 12    2.1256668760696225e-17
inner 15    5.3726548566934115e-17
```

其余十个未达内目标的报告，末二十档也有 18 或 19 个参数与 current 逐词相同。所有逐档词对照保存在字面附件；inner 8 达标后没有这组末次回溯。

这是这批既定参数试探的原件事实，说明机械缩小同一 current 的 p3 步可能不改变实际存储参数。它不是整个三参数空间根不存在的证明或统一误差下界，更不支持更换原阈值。本次策略允许该实际有限点继续接受外层完整 merit 检验，随后新外层坐标可继续变化。

## 7. 每轮自己的原保存谱及非线性检验

所有完整 K／列尺度／增广矩阵与右端／方向／原 J 动作／线性残差／SVD 都保存在完整 status 与字面附件。下表只取已经保存的奇异值和第二奇异方向移除系数，没有重算谱或比例。

|轮|scaled K 第一奇异值|第二奇异值|第二方向移除系数|
|---:|---:|---:|---:|
|0|`1.4142134041266974`|`0.0006690204617096215`|`4.47568345547164e-05`|
|1|`1.4142128911470464`|`0.0013778655636452646`|`0.00018981531445403057`|
|2|`1.4142076584460175`|`0.004086415621641203`|`0.0016670954152155492`|
|3|`1.414210197831234`|`0.003084858204481073`|`0.0009507302659652898`|
|4|`1.3226159049648196`|`0.5006866963821701`|`0.9616398456462257`|
|5|`1.41377008161426`|`0.0354140696956549`|`0.11143939140041058`|
|6|`1.4139405103758298`|`0.027789082714947316`|`0.07168737527949565`|
|7|`1.4130569268099187`|`0.05718497700014728`|`0.2464274024332156`|

每一行都属于自己的当前有限 Schur 模型，不能以旧 85／88 模型谱或 92 最后的谱替代。第 4 轮局部谱并未保证大 alpha 的恢复后 merit 下降，原试探仍拒绝它们，最后在 1/16 接受。

第 7 轮完整原线性预测 `r+Jv` 与该轮 alpha 1 实际恢复点分别为：

```text
linear: [-178.90593708615694, 9.932494966240824, -8.138174185472037e-11]
actual: [-182.4135460006347, 1135.6928966879668, -3.936350583759029e-08]
```

该实际点被原 merit 拒绝，alpha 1/4 后才接受。本文没有对两向量本地作差或新范数，也没有把差别唯一归为某段非线性、内恢复或舍入。

## 8. 最后原 J／FD／112 行及圆／标量检查

最终 `model.description` 的 fresh J 绑定最后实际参数；本轮其全部词也恰与最后 inner 的同点 J 相同：

```text
[[-664.3936933663905,   610.9338250928995,  -538.9189433638402],
 [1007526.7640086645,  5966.292074939401, 512886.3756502762],
 [67033101.35869059, -15393147.418586014,706233195.9685296]]
```

原奇异值 `[709574576.3565865,954746.2770807218,609.8870501358955]`，普通浮点条件数 `1163452.439592673`。这不是区间横截性或高 109 模非共振证明。

原三档独立实参数有限差分：

|step|原最大相对误差|valid|
|---:|---:|---|
|`2e-05`|`6.9446534019950346e-09`|true|
|`1e-05`|`3.7035294149978364e-09`|true|
|`5e-06`|`2.585242730137743e-09`|true|

这些是当次实际普通浮点检查，不是精确导数误差外包。完整 first-order native height 前三项为 `[4.5713069613919455,0.6987023548051475,3.8903359562157565e-07]`，余项为零；这只是原一阶读出，非实际 native 解。固定零尾 J112 仍由相同真实 anchor 全矩阵取得，逐项对角身份与 92 已完成的完整输入字节审计关联。

原 `high_free_core_Schur_elimination_computed=false`、`high_mode_nonresonance_proved=false` 保留；高模右残差为零不是高模齐次核已排除。

### 8.1 圆参考仍明确是零 core

`circle-reference.json.gz` 为 `140101` 字节／`36eb3f6e4c182893fac4f5860a07242ed27dd38ee071d9b2689125a3e5db40af`。完整 699 节点、`699×453` states／RHS 和**低三**单位模态／RHS 各 `699×3×2` 都保留，不能说成 112 个单位模态。

`fixed_core_targets=[0,0,0]`，`original_large_core_targets_retained=false`。原圆检查 physical collocation `4.0722633598555547e-16`，boundary／left／constant residual 均 `0.0`；node／midpoint／两原 RMS 查询域失败均 0，统一 phi/rho guard 有效、rho minimum `1.0`。九个原完整 FFT 切向抽查保存在附件。这是零 core 圆参考检查，不是最后非零 core 候选已通过整场 BVP。

### 8.2 Arb 的真实覆盖范围

`complete-scalar-domain.json.gz` 为 `161830` 字节／`073739bcad3c7f7ae6748f8e059762b3d1557d0d6f34ed8c9583d1eb14812ec1`。原 160 bits／最大深度 14 的结果有 1091 叶、648 splits、0 unresolved，覆盖 `[0,5113846463878377/2251799813685248]`，报告 `complete_declared_real_expression_domain_certified=true`。

本次逐叶核原成功／失败布尔、端点文字及相邻连续次序，没有重做 Arb。原范围是声明实 scalar／有限 Gauss 表达式及返回 ap；literal binary64 舍入没有外包，没有证明返回 ap 就是有限 Gauss a 的导数或 C² 接口，也未覆盖源圆半径与完整 Frenet 域。不能从零 unresolved 自动填补这些缺口。

## 9. 字节范围与完整附件

独立 `audit_actual93_inexact_p3_bytes.py` 只用标准库读取、hash、JSON 对应、binary64 pack／词分类和整数计数，没有导入生产者或科学库，没有 Git／网络／RHS／J／矩阵／merit／SVD／Fraction／FD／区间运算。

**5785 项核对全部通过：**

- 28 原 artifact 成员完整 SHA／大小、另 1 本地 marker；原 status、15 inner gzip、全事件账、两摘要原件完整保全。
- 72 个 request source payload；13 源闭包及真实角色、入口源码常量、四输入 pins 互相一致。
- 78 个 restored-source 原 Actions receipts 与冻结完整 `source-dependencies.json` 对应，不冒本地第二次恢复 78 载荷。
- 四原数学输入与实际 92 已付完整 payload 审计同 SHA；本次没有重复读取本地已缺失的大输入。此前 audit `65135` 字节／`dca47829ec3202809cb96e615d0909796d0fa4bbc4471cdd944bdf2a79f31409`。
- 全 15 inner／91 current J／361 内 trial／76 内接受；8 outer／15 外 trial／8 外接受，参数／残差／J 与原事件逐项关联。
- 785 顺序事件：692 evaluate 返回（413 实、279 复）、93 J 返回、0 异常；两个 description／FD 来源明确。
- 164 个完整数组另列 JSON-decoded binary64 身份，含全部 current J、各方向关键数组、初末读数、整圆 mesh／states／rhs／低三模式及 RHS。其他保存字段仍受完整原 JSON SHA 与无损副本覆盖；164 不是声称 status 只有这些数组。
- 1091 原 scalar 叶及原端点／标志保全，不重科学。可选证明文档在本地未检出者仅保原 request receipt，不冒本轮复读。

随文交付：

|文件|bytes|SHA256|
|---|---:|---|
|[2026-11-15-actual93-literal-readout.json.gz](2026-11-15-actual93-literal-readout.json.gz)|`87410`|`20d1506b5466130a26ec95873bb467a4f829e3711be4d0bd2761fb552b3411c5`|
|[2026-11-15-actual93-byte-audit.json.gz](2026-11-15-actual93-byte-audit.json.gz)|`48333`|`a0a40d45d4691dee5e85f76a3a5213562be128d9fa79b2e1b264863cc39b69a2`|
|[2026-11-15-actual93-byte-audit-summary.json](2026-11-15-actual93-byte-audit-summary.json)|`4142`|`30f5a97aafdf2fff32e98e273ac70de5238ed8528645be474580303f88446650`|
|[2026-11-15-actual93-original-complete-status.json.gz](2026-11-15-actual93-original-complete-status.json.gz)|`29477`|`42c3fc46b74c45729921514e9782ffc14a6ea010d6494d97074b809030dce110`|
|[2026-11-15-actual93-original-evaluation-ledger.jsonl.gz](2026-11-15-actual93-original-evaluation-ledger.jsonl.gz)|`56249`|`fc4cee87c95c5a45a35940e6a78ef64ad8c42de24da8f683eb157590aec1a325`|
|[2026-11-15-actual93-original-inner-reports.json.gz](2026-11-15-actual93-original-inner-reports.json.gz)|`66903`|`b9ba959c1ce0244a7b59d8c4fa399af3cb1360328ebb3f75342c54e8dd21778c`|

完整原事件账未压缩 `1148511` 字节／`07ccdb8ce07fd32c07cb2b8b5c75292936d7612f4e9a98af31f9026957e596ec`。全部 inner JSON 合并时只添加列表分隔并保原数值 token；未压缩 `2853629` 字节／`32b077d286f245db75bbd757ec6e86dc3c0ceb5e37ef150aafa1426905624852`。这些字节证据不是新的科学门。

## 10. 有依据的直接后继与尚未支付的结论

本轮只因八方向预算结束，最近 alpha 1/4 仍通过原完整 merit 检验。从**本轮真实最后参数**继续同 ce93 算法、eta 0.1、8／20 外预算和 12／20 内预算，是现有原件直接支持的下一次试验；不是预言必下降或根存在。

冻结 `checked_parent` 已有 own-schema 分支，核完整父文件 SHA、同 SCHEMA／producer／13 源闭包及 `last_accepted_point_semantics`，随后只读取 `final.parameters`。无需修改算法或身份标签即可接实际 93；下一次仍 fresh evaluate／完整 J，不继承本轮残差／谱／FD／域证明。主控独占 request 96 接线；本文不派发，也不增加等待审核门。

R278 三项目化残差与完整参数 J 接口可以作为不同后继准备，但不能以旧 92 的停滞掩盖 93 的真实推进，也不能只凭更均衡的尺度替换原 unit／full112 判据。低三根、根处横截、当前参数的高 109 非共振、非零振幅分支、原 native／full BVP、固定度量全族及 README 完成标准仍各自未付。

参见 [92 完整内层资格阻点](2026-11-15-actual92-p3-inner-roots-outer-descent-and-restoration-bottleneck.md)、[93 算法接口](2026-11-15-inexact-p3-restoration-search-interface.md)、[88 旧保存模型谱](2026-11-15-actual88-saved85-singular-directions-and-local-damping-predictions.md)。本文只报告本次原件支持的数值事实，不以局部线性预测、approximate inner root 或 job success 冒最终完成。
