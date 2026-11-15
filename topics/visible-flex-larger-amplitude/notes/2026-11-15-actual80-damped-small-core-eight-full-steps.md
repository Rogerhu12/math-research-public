# 第80轮实际回执：八次完整步长接受，三个共振方程仍未解出

作者：ChatGPT（geometry 分工）  
分类：原件读回／有限三参数候选搜索  
日期：2026-11-15 UTC

## 1. 实际结论与范围

第80轮完成了新的列尺度正阻尼候选搜索。八轮均在第一个原试步 `alpha=1` 接受，实际只执行八个 trial，没有域拒绝或 merit 拒绝。原未加权 merit 从 `65077006698.67736` 降到 `15492237698.871113`。这与第78轮八次均只能在 $2^{-17}$ 接受的读数不同，说明本次实际方向在本次原回溯条件下允许完整步长。[第78轮正式结论](2026-11-15-actual78-small-core-eight-tiny-Newton-steps.md)

本次并没有解出三个共振方程。最终原 unit defects 为

$$
(206.4299715953469,\;-176013.15201356995,\;1950.1545213062855),
$$

原完整112维一阶右残差的前三项为

$$
(95.35152101950872,\;10507.019296282351,\;30.676041046423595).
$$

原 `low_mode_candidate_has_small_full_recorded_right_residual=false`，`success=false`，`native_nonlinear_solver_called=false`，`full_nonlinear_nonzero_lambda_solution_computed=false`。本次记录的是已完成诊断和候选进展，不是非零 BVP、native 尾、full DN、同 $g$ 精化或完整闭面接受。第三个 unit defect 的幅值从 `316223.4753016901` 降到 `1950.1545213062855`；第二个最终幅值仍大，并且比本轮起点的 `173656.799408131` 更大。没有把总 merit 的下降写成各分量都下降。

以上数值直接来自[完整原状态文件](public-actions-43664043053-1-smallcoreresonance/small-core-damped-search/damped-search-status.json)；本地没有重新形成残差、求方向、计算 norm／SVD、运行 FD、Arb 或圆参考。

## 2. 实际运行与完整身份

| 项目 | 原实际记录 |
| --- | --- |
| repository | `Rogerhu12/math-research-public` |
| run | [43664043053](https://github.com/Rogerhu12/math-research-public/actions/runs/43664043053) |
| triggering source | `5a17ad802c28a0a00f2776201cea4cef27f68da7` |
| job | `132659392179` |
| job 时段 | `2026-11-15T01:38:39Z` 至 `01:39:27Z` |
| 科学 step | `01:39:13Z` 至 `01:39:18Z` |
| producer 保存的 `seconds` | `3.4193658109999987` |
| artifact | `14141985111`，`visible-mainline-smallcoreresonance-43664043053-1` |
| ZIP | `265623 B` |
| ZIP SHA256 | `1bc8586e5369b182d61214e064db42ac06cdf9ae8a0d26b2c231390e8f2f5ade` |

工作流科学 step、原状态复制、完整 artifact 和普通 publisher 全部完成。工作流的 success 与状态里的候选 `success=false` 是不同层次的事实。根唯一下载并验证 ZIP；本次读者只消费其完成标记和已提取原件。

新入口为 `geometry_20261115_small_core_damped_search.py`，13733 B，SHA256 `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728`。它导入且保留原 `geometry_20261114_small_core_resonance.py`，SHA256 `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`。这是两个明确不同的源身份，不能把新候选方向称作原 Newton 搜索未改变。

完整原件相对本题 notes 的目录为：

`public-actions-43664043053-1-smallcoreresonance/`

| 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| [完整状态](public-actions-43664043053-1-smallcoreresonance/small-core-damped-search/damped-search-status.json) | 52985 | `ebe5b50c6af5ec9cfbe201e4d19a1b24dc9357e28ac8fe89354d5c04fd13ee2a` |
| [完整 scalar 区间原件](public-actions-43664043053-1-smallcoreresonance/small-core-damped-search/complete-scalar-domain.json.gz) | 79214 | `64c093bdf8fe676eda6dbdc28685a658d0ed08db1da4cc83733fe0a53a3ef8b5` |
| [完整圆参考原件](public-actions-43664043053-1-smallcoreresonance/small-core-damped-search/circle-reference.json.gz) | 139948 | `99f3f0cb0a18b54d6d3063ed766d6bdfd8048daecaf8056c5619ed161b40b167` |

Arb 原 JSON 解压后428098 B，SHA256 `e2afdbabde48d71477dbcbd82f2770b76385075849da81c9de0c0de78ca577d0`；圆参考原 JSON 解压后3569295 B，SHA256 `639f9c237e4fb5225bdac188196e1aa21da019b5b8d1c98dca4ea5d1469b8aba`。

## 3. 父状态、同一模型与新方向

本次明确读取第78轮原 `resonance-status.json`：50438 B，SHA256 `09031496410951afc018b223b921db111a43b3e0852592b87aafd5351b4f0c40`。完整父文件在本 artifact 的 `prior-candidate/actual78-resonance-status.json` 和 `small-core-damped-search/actual78-parent-status.json` 各保留一份，两份逐字相同。

起点逐值为父文件 `final.parameters`：

```json
[0.09365081258727412, -0.13201200770909496, -0.12389206129693811]
```

本轮重新求出的初始诊断有11个字段不与第78轮最终诊断逐字相同，包括一阶高度／右残差、unit defects、参数 Jacobian、SVD 和 FD 读数。三参数本身精确保留；全部11处原值对照已保存在 companion 中。这里不猜测这些末位差异的唯一来源，也不拿父最终 merit 冒作本轮实际重新求值的起始 merit。

四个数学输入继续是原件：

| 输入 | 原 SHA256 |
| --- | --- |
| accepted96 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared112 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| 真实完整 T112 零响应 | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| 原 T112 配置 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

新方向使用原三方程 $r$ 和原参数 Jacobian $J$，按实际列二范数构造 $D$，再解完整增广6×3最小二乘：

$$
A=JD^{-1},\qquad
\min_z\frac12\|Az+r\|_2^2+\frac12\eta^2\|z\|_2^2,
\qquad d=D^{-1}z,\qquad \eta=1.
$$

没有形成法方程、没有行重加权，也没有把阻尼项加入原非线性残差。原实际 `r @ (J @ d)`、原0.2 Armijo 和最多二十个试步均保留；rank／SVD 只作读数。每个完整 $r,J,D,A,[A;\eta I]$、右端、$z,d,Jd$、rank、SVD 与实际 `gdot` 全在原状态里。[原算法与完整预算接口](2026-11-15-small-core-damped-search-interface.md)

原 mesh699、M=T112、物理角2048、材料／边界角4096、原 RHS worker1、Python3.12.14／NumPy2.3.5／SciPy1.17.0／python-flint0.9.0 与单线程 BLAS 均保持。

## 4. 八轮完整原 trial 账

每一行只有一个原 trial，`alpha=1` 且 `accepted=true`。以下全部 merit 和 gdot 为原 producer 保存值，没有本地重新做平方和或 Armijo 算术。

| iteration | 原 `merit_before` | 原 `actual_merit` | 原 `true_model_merit_slope` |
| ---: | ---: | ---: | ---: |
| 0 | 65077006698.67736 | 18929336763.490906 | -74194982299.63829 |
| 1 | 18929336763.490906 | 15826652575.188774 | -4958333530.398621 |
| 2 | 15826652575.188774 | 15610311953.628124 | -333395609.66483116 |
| 3 | 15610311953.628124 | 15576677040.41054 | -40988053.77636887 |
| 4 | 15576677040.41054 | 15554655168.375761 | -22526960.04725971 |
| 5 | 15554655168.375761 | 15533582695.97343 | -21146479.908560365 |
| 6 | 15533582695.97343 | 15512792230.963749 | -20835590.794718046 |
| 7 | 15512792230.963749 | 15492237698.871113 | -20596770.889035426 |

每次接受 merit 与下一轮记录的 base merit 逐 binary64 字节相同。八个增广 rank 均为3，`exactly_zero_columns=[]`，实际 gdot 均负。第一轮增广奇异值为 `[1.9998668291155457, 1.000266297444315, 1.0000000000001867]`，最后一轮为 `[1.9998339255348467, 1.0003320800011668, 1.0000000000002105]`。这只是本次求方向模型的数值读数，不是原未缩放参数 Jacobian 的严格条件数界或共振横截性证明。

第一轮实际恢复方向为

```json
[-0.0019267386687836293, -0.007299727243572823, 0.0009155120717849158]
```

最后一轮为

```json
[-0.00004789838368740126, 0.0003767693186834911, 0.00002041881388229159]
```

原 `Jd` 第一轮为 `[-1.2436689161661747,-2228.927011119146,-235852.3518888103]`，最后一轮为 `[0.09375698075218547,116.59585551810963,-30.774748882538844]`。后几轮第一个分量已有小幅上升，同时第三个分量继续下降；总 merit 接受不能替代逐分量结论。

最终设计参数为：

```json
[0.09071772300091886, -0.13939413969182854, -0.12252606423015384]
```

## 5. 完整一阶右端与参数检查

原真实零尾斜率 Jacobian 继续读全112×112：报告 `maximum_absolute_offdiagonal=0`、`nonzero_offdiagonal_entries=0`、`all_entries_consumed=true`、`exactly_diagonal_as_recorded=true`，没有用 ready 的线性图替换。初始非零三个目标为 `[0.4619073494154277,-0.05969451246161594,0.015730056624372334]`，`target_zero_indices=[]`。

| 原字段 | 本轮初始 | 本轮最终 |
| --- | --- | --- |
| unit defects | `[207.5687844070032,-173656.799408131,316223.4753016901]` | `[206.4299715953469,-176013.15201356995,1950.1545213062855]` |
| 一阶高度前三项 | `[-4.609249908451861,-242.23830837131047,-93.53500679572052]` | `[-4.583991689469192,-245.52524489416493,-0.5768316319249398]` |
| 完整一阶右残差前三项 | `[95.87754702682122,10366.357976313015,4974.213172451392]` | `[95.35152101950872,10507.019296282351,30.676041046423595]` |
| 原数值参数条件数 | `2984504.4280113387` | `2903112.919201124` |

完整112维右残差的后109项仍为原负零，原 `high_right_leak_max=0`。这不代表已经计算高自由核心 Schur 消元或证明高模非共振；两个对应标志仍为 false。本次与另行安排的高109检查是不同任务。

最终原3×3参数 Jacobian 是

```json
[[-113.15133922387191, 227.54399662521465, 116.91996924720341],
 [4648.887031024472, 313257.0933687249, -73141.2951493348],
 [40181338.10811115, 9822943.53933729, -88012335.89300084]]
```

其保存的奇异值为 `[97248194.7028936,305858.87388515985,33.49790290956174]`；没有在本地重算这些数，也没有把最小数值奇异值当严格可逆／横截性证书。

原实参数差分检查全部 `valid=true`：

| FD 步长 | 初始保存的最大相对误差 | 最终保存的最大相对误差 |
| ---: | ---: | ---: |
| 2e-5 | 5.838135555647939e-9 | 5.878307134608705e-9 |
| 1e-5 | 1.4363089241393176e-9 | 1.4824694931505723e-9 |
| 5e-6 | 4.797647594703794e-10 | 5.883313145742735e-10 |

这是本诊断三个参数方程的 FD，不能移作完整非零 native/full-DN 响应的 FD。

## 6. 原 Arb 与完整零核心圆参考

最终 Arb 原表达式证书保持160 bit、最大深度14，覆盖 `[0,5113846463878377/2251799813685248]`。原记录为494 leaves、51 split cells、0 unresolved，`complete_declared_real_expression_domain_certified=true`。全494条叶子及相邻端点字符串连续账已保留并比对；本地没有重新运算区间。

这项证明对象仍是完整声明的实 scalar 表达式的正半径及 source-returned $|ap|<1$。原四个限制字段保持 false：没有包围 literal binary64 evaluator 的全部 roundoff，没有证明独立返回 `ap` 就是有限 Gauss `a` 的字面导数，没有核销全 C² 接口，也没有据此覆盖真实圆 $R$ 和完整 Frenet 域。

最终 scalar specification 的保存 SHA256 为 `b3f4d4da5b6c8bb73fa72d94a68a97f1c5391d58873df730087f3c5ce03543d3`，mathematical identity 为 `3219e328b3ebd8c10e0ecd5351305265896b3a741461913ba4ca075db59edc31`。本设计搜索确实改变三个 scalar 参数，不称各候选处于同一冻结 $g$。

圆参考保留原 schema `R259-original-circle-collocation-low-three-resonance-diagnostic-v1`。完整保存699×453 states、699×453 RHS，以及两套699×3×2低模数组。其目标为 `[0,0,0]`，`original_large_core_targets_retained=false`；它不是非零父场。圆的源方程仍为 $R'=ap\,R/a$，不是直接令 $R=a$。

原完整圆读数为：

- node／midpoint 域失败数均0；完整原边界有限。
- 原4096角 uniform-$\phi$ rho guard 有效，`rho_min=1`。
- 两个原 RMS fractions `0.17267316464601146`、`0.8273268353539885` 各698个查询，invalid count 均0。
- 原 `physical_collocation_max=4.3660821485991264e-16`；left、complete-boundary、constant-collocation max 均0。
- 保存的圆 node／mid最小半径 `0.2999999984126292`，最小 `beta2=0.005153125420959248`。
- 原节点 `R-minus-supplied-a` 最大读数 `1.988109787909309e-9`。

原 full-FFT tangent 检查仍是节点0、349、698各三个模式，共九次。最终端点三模式的保存相对误差为 `4.3523871749964216e-14`、`9.510858220041197e-14`、`2.526729879824845e-13`。全部物理行比较标志为 true；这不替代非零完整父场和闭合指标。

## 7. 原件核对范围

附属 `2026-11-15-actual80-original-byte-audit.json` 的29项检查全部通过。范围包括11个 artifact 原件加完成 marker 共12件、完整状态和两个父文件、69个源逐 SHA、4输入描述器交叉身份、实际 CLI、八个方向模型的完整保存数组形状与别名、各实际 merit 的前后字节衔接、完整112维结果、494个 Arb 叶子、完整圆数据及九次 tangent 报告别名。

四个原大型数学输入不在本地窄 checkout，本次没有再次下载或声称独立全字节重审；它们由本次 Actions 的原完整输入核验回执与父／新状态的 SHA 链绑定。69个源码则确已用完整本地或该实际提交的 Git 原字节重新哈希。

`2026-11-15-actual80-complete-original-readout.json` 保存完整原 status、全部八次方向和 trial、实际 argv、父来源、11处重新求值差异、最终 scalar 的小身份。它与本 note 一起交根归档。没有局部修改原源或原科学输入。

## 8. 下一项有依据的有限实验

本次八次完整步长接受且都经过原域和原 merit 规则，支持从真实本次 final 参数继续一个有界试验。后一半 unit defect 第二分量仍很大，原保存的归一化矩阵第二行约为 `[0.0001,0.032,-0.0008]`，而第三行约为 `[1,1,-1]`；这是从各原矩阵直接读出的尺度差异。它说明固定 $\eta=1$ 对较弱方向保有较强惩罚，是值得实际检验的解释，不是已证明的唯一原因。

建议下一项只试一个明确较小的 $\eta=0.1$，从真实本次最终参数出发，继续最多八轮／二十回溯；同一原方程、实际 gdot、0.2 Armijo、域条件、阈值、FD／Arb／圆参考都保持。只改变公开声明的方向模型阻尼系数，不搜索多个系数后隐藏择优。若新方向被原规则拒绝，就保留真实拒绝；不预言根存在、全步长继续成立或候选变小。

这个建议依据本轮真实趋势，尚未运行。后继应以独立 resume schema 和显式真实父 status／producer SHA 绑定，避免把被冻结的第80轮源内 actual78 起点偷偷改掉。新的 bounded candidate 仍不构成原 BVP/native/full-DN 的额外门或接受证书。
