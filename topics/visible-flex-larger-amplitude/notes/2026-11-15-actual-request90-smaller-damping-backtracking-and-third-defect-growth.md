# 实际90：η=0.01的八方向均回溯接受，40次拒绝且第三方程增大

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：本公开仓库Actions原结果完整读回与来源/文件字节审计。** 本地仅解析已经完成的JSON、gzip、SHA、原数值literal和整数维数；未导入数学模块或重算RHS、Jacobian、矩阵动作、FD、范数、Arb、优化器。该读回不增加新科学门。

## 1. 原结果与当前结论

[实际90运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43670368504) 用冻结ec9入口，从真实87最终参数出发，仅将显式方向阻尼从父η=0.1改为当前η=0.01。八个方向全部找到原准则接受的trial，但接受α为`[1/16,1/32,1/32,1/32,1/32,1/64,1/32,1/32]`，共48个trial、40次拒绝。全部48条记录都有原actual_merit，没有`domain_or_cell_error`，20档预算没有耗尽。

原保存merit为`11289805820.156862 → 11213045978.398226`。最终单位方程为`[229.78524027424547,-149015.7614289278,14843.921358477846]`；第一和第三分量没有改善。原`diagnostic_completed=true`，但`success=false`、`low_mode_candidate_has_small_full_recorded_right_residual=false`，仍没有低三共振根、非零幅度parent或原BVP接受。

这轮证据把当前限制与“域外拒绝”或“回溯档数不够”分开：拒绝发生在已返回原merit的trial，且原预算未耗尽。更小η仍给出原负方向斜率，但实际非线性步长需要缩小。它不证明η是此前慢降唯一原因，也不支持再盲降η或把原Jacobian判为错误。

## 2. 实际来源与输入

| 项目 | 实际身份 |
|---|---|
| run | `43670368504` |
| source | `4424f9c45f8866f54872e876430b8a3dd56aec1b` |
| job | `132678845557` |
| artifact | `14143584095`，`visible-mainline-smallcoreresonance-43670368504-1` |
| ZIP | 269478 B；`23c18e81de8e4f5d1492e818abf034437961d801bff54dcc0d59b493b179e7e1` |
| 最终status | 60951 B；`5a4d157aa0bcada3cdd1d319adb419f23b94f52bfc1c945a3c6afe1207cb2f5a` |

主控已核官方artifact元数据、完整ZIP SHA/CRC/路径并唯一下载。本次读回再核下载标记和全部11个原成员共463099 B。科学step8、原readback9、artifact10及publisher11均success；此步骤结论来自主控已取得的官方metadata，本次没有另作joblog审计。过程成功不等于原status里的科学候选成功。

原父87完整状态54279 B /`e805446d14713957dd67e715d9d28193c14c20002e00b0a1ace2e4ac1c03dd80`在本artifact两份副本逐字相同，且与原request、identity、status.parent_status完整绑定。只继承`final.parameters`：

```json
[0.057323451817869575, 0.002679377797021207, -0.11058649307511116]
```

当前原status明确记录父η文本`"0.1"`和当前η文本`"0.01"`，binary64当前值0.01。父参数和新initial参数逐bits一致；本次初始unit/merit原保存值恰与87最后对应字段一致，这是本轮观察，不据此建立“同参数必逐字同模型”的一般结论，也不复用父J/merit/state冒新计算。[实际87记录](2026-11-15-actual-request87-damped-resume-eight-full-steps-low-three-unresolved.md) 中85末值与87初值的末位差仍保留。

冻结科学源继续为ec9`geometry_20261115_small_core_damped_resume.py`、1691`geometry_20261115_small_core_damped_search.py`、3b9`geometry_20261114_small_core_resonance.py`。全部70源的原Actions记录、request SHA及当前对应源码字节一致；11 consumed数学源为其准确子集。四原输入accepted96/prepared112/真实T112零锚/config的SHA在request、identity、父及当前status中一致。本次不重新读取这四个大input payload，不冒其再次独立字节审计。

## 3. 八方向、全部回溯与原merit

| 方向 | 原merit起值 | 接受α | 原merit终值 | 拒绝档数 | 原完整模型斜率 |
|---:|---:|---:|---:|---:|---:|
| 0 | 11289805820.156862 | 1/16 | 11255501554.362804 | 4 | -1475822176.490281 |
| 1 | 11255501554.362804 | 1/32 | 11243427370.404392 | 5 | -996443780.7292473 |
| 2 | 11243427370.404392 | 1/32 | 11235264719.58767 | 5 | -847825300.4007009 |
| 3 | 11235264719.58767 | 1/32 | 11229554463.52902 | 5 | -733713367.7205863 |
| 4 | 11229554463.52902 | 1/32 | 11225275937.603651 | 5 | -644421473.5597749 |
| 5 | 11225275937.603651 | 1/64 | 11219863307.91122 | 6 | -573129340.84918 |
| 6 | 11219863307.91122 | 1/32 | 11216436186.738636 | 5 | -536198146.9716612 |
| 7 | 11216436186.738636 | 1/32 | 11213045978.398226 | 5 | -483121947.6654232 |

全部完整3×3原J、3分量r、列尺度D、保存A、6×3增广矩阵、rhs、z、恢复d、原Jd和原48条trial逐值保存在[完整literal读回](2026-11-15-actual90-original-readout.json)的`original_status_value.searches`。本地只核字段对应、维数、原相邻merit连接和接受/拒绝标志，没有重算方向或merit。

每个方向原`augmented_lstsq_rank=3`、零列列表为空、正阻尼0.01；原normal-equations、行方程重加权和向原非线性残差添加阻尼三标志均false。增广rank3不是原3×3J非退化或横截性证明。所有完整模型斜率都是原保存的`r dot (J d)`，没有以负LS目标代替。

40条拒绝均保留，尤其以下两类不能混写：

- 大多数拒绝档原actual_merit高于本方向起值。例如方向0的α=1/8为`11889030078.25868`，起值为`11289805820.156862`，之后α=1/16接受。
- 方向5的α=1/32原merit为`11221704597.679981`，已低于起值`11225275937.603651`，但原`accepted=false`；原方向斜率为`-573129340.84918`，原代码仍要求0.2 Armijo充分下降。后续α=1/64以`11219863307.91122`接受。这里没有本地重算Armijo阈值，结论直接来自原数值、标志和冻结准则。

因此不能把全部拒绝简化为“merit增加”，也不能把没有域异常解释成较大步长一定可行。当前八次外层诊断已执行，没有新增回溯门或改动原20档。

## 4. 最终低三与完整112条读数

最终原参数：

```json
[0.04241436079648833, 0.02766947731512731, -0.10800335072481342]
```

| 原保存量 | 初始 | 最终 |
|---|---|---|
| 单位方程d1 | `228.5006013402948` | `229.78524027424547` |
| 单位方程d2 | `-150264.2154200839` | `-149015.7614289278` |
| 单位方程d3 | `474.3331904136449` | `14843.921358477846` |
| 低三单位轨迹最大值 | `[10.983808399124847,3511.3343880422008,8.91934961510355]` | `[11.045488913386865,3482.160845702764,279.1248035445189]` |

原完整112右残差的前三个是`[106.13949126986391,8895.423227596319,233.49572349658644]`；其余109为原保存`-0.0`，完整带符号字段保存在literal中。原完整112首阶height前三个为`[-5.10199250698002,-207.86589399715476,-4.390648965022086]`，其余为原0。这些是圆附近低三首阶模型的记录，不是真实非零H的native nonlinear响应，不能拿它们作完成的非零尾锚。

完整真实零锚slope-J报告仍为112×112、全部条目消费、非对角最大0、非对角非零数0、实际记录严格对角，`ready_linear_graph_used=false`。三个原target均非零，原可选对角低三搜索的适用记录不变。这里没有静默抹去非对角高块；当前源明确`high_free_core_Schur_elimination_computed=false`、`high_mode_nonresonance_proved=false`。实际81在另一参数点的高109结果不继承到当前90。

单位方程循环阈值与完整112右残差末尾小候选标志仍各按原1e−8定义；没有以某一分量、加权范数或原circle合法性替代它们。

最终原3×3参数J为：

```json
[[-37.30565026384013,-5.470028525545402,105.47723542423763],
 [3295.1952915617762,35516.023725371,-29379.349426876972],
 [19256558.735071484,23663870.270838052,-72000128.47538549]]
```

原保存奇异值为`[78197274.89976357,25389.76358431318,3.699248800488512]`，原数值condition为`21138690.34422261`。特别是当前原`∂d3/∂p3=-72000128.47538549`有限且非零，这是一个后继算法可使用的局部读数；当前点d3不小，所以不能由此宣称邻近根存在、精确IFT条件已满足或原参数图已被证明非退化。

## 5. FD、Arb及完整圆场范围

最终独立原参数差分记录：

| 原中心差分step | 原valid | 原maximum_relative_error |
|---:|---|---:|
| 2e-05 | true | 1.5098650030008722e-08 |
| 1e-05 | true | 3.878724677379875e-09 |
| 5e-06 | true | 9.113386660122363e-10 |

本地没有重算任何FD或比较误差。它们是原最大相对坐标检查，不单独证明弱奇异方向或原高块横截性。

原Arb160位/最大深度14，覆盖声明区间`[0,5113846463878377/2251799813685248]`，465个leaf、22次split、0 unresolved，全部原叶记录正半径与`|ap|<1`。本次完整解压并读取465个叶JSON及其原flags，但没有重新评价Arb表达式。

原标量证书明确：使用源返回ap；不把ap等同有限Gauss a的真导数；不包围binary64评价舍入，不提供精确标量导数兼容/C²接口证书，也不覆盖圆R或整个Frenet域。不能把这个声明实表达式a/ap结果升级为完整有限BVP证书。

原circle-reference完整699节点、每节点453个states与rhs值都已读入原JSON并核字节/维数。它是固定core为零的完整圆场，原`success=false`、`new_coupled_finite_acceptance=false`、无真实非零native尾。

- node与midpoint域失败数均0；原两RMS各698点、invalid均0。
- 4096均匀φ的原rho guard通过，rho min1；left/完整boundary/常值collocation最大均0。
- 原physical collocation max `4.14815751192954e-16`。
- 查询标量a min `0.30000000000000027`；圆R min `0.29999999841549285`；原β²min `0.005153125401965886`。
- 原`R−a`节点最大 `1.984908404306651e-9`，原radius-cell分母绝对最小 `0.9992505550049908`。
- 低三2×2右块condition原最大值 `[1.3950728980222518,4.568977828194337,17.1135964148631]`；低三原collocation tangent residual max `4.547473508864641e-13`。

原三mode在node0/349/698共九个完整FFT方向比较均保留；末端三项误差为`8.677964880242839e-14`、`1.8948628188295834e-13`、`5.004166523299402e-13`。circle原文件的`low_three_unit_modes_UH`和rhs轨迹只有低三，不能冒全部112单位模逐个完成。

## 6. 全原件字节范围

| 原成员 | 字节 | SHA256 |
|---|---:|---|
| `exact-diagnostic-command.json` | 3003 | `97c62b1a55848aac23dc85c30abc209265354fe0e5c65f33efca5a7580bb7646` |
| `prior-candidate/actual87-damped-resume-status.json` | 54279 | `e805446d14713957dd67e715d9d28193c14c20002e00b0a1ace2e4ac1c03dd80` |
| `public-source-preparation.json` | 20424 | `b06044d221a2eea868dc044df644dd70eba9476688350ea269a33b518ee34f28` |
| `public-source-restore.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `request90-input-and-source-identity.json` | 35574 | `69770434d1e792a8397be9073c02583f8e72eeccb850448f243d5f7420b2d2e0` |
| `small-core-damped-resume/circle-reference.json.gz` | 139721 | `fb6addea691fa9f77ddc23c4baa9bd6ac38b6c9af0751daf582ec0ef5e3f9719` |
| `small-core-damped-resume/complete-scalar-domain.json.gz` | 74994 | `066406b425233474471b8ba4b6f0526a3b893bb35ecc6a821e52e8b9cc3378d6` |
| `small-core-damped-resume/damped-resume-status.json` | 60951 | `5a4d157aa0bcada3cdd1d319adb419f23b94f52bfc1c945a3c6afe1207cb2f5a` |
| `small-core-damped-resume/parent-damped-status.json` | 54279 | `e805446d14713957dd67e715d9d28193c14c20002e00b0a1ace2e4ac1c03dd80` |
| `small-core-resonance-readback.json` | 19874 | `7ad9914572fc4803042c090baec1b52260b8bdddb1ed9904c8a35118c6dfbffe` |
| `small-core-resonance.log` | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |

两个gzip除压缩文件SHA外，还记录完整decoded字节数/SHA；原status指向circle的SHA与真实gzip一致，scalar摘要与完整scalar原JSON逐值对应，readback所复制字段与status逐值一致。

[完整字节回执](2026-11-15-actual90-original-byte-audit.json.gz) 为透明gzip；[小摘要](2026-11-15-actual90-byte-audit-summary.json) 保身份/范围。233项结构、来源与字节关系通过：11原成员、70source payload、11 consumed子集、两份真实87父副本、四input来源回执、八方向/48trial、465叶、699×453圆states/rhs及全部原FD/FFT记录对应。

范围边界保持明确：原public78恢复manifest被完整读取，但78源码payload没有在这里另行重审；完整112尾J只有原Actions消费/对角报告，没有独立raw J导出供本地再审。Arb与circle读数也只有原原件读取，未做数学复算。真正大幅非零有限场没有生成，因而也没有任何此类接受证书。

## 7. 后继决定的证据边界

90已完成八次候选方向，不是工作流或publisher失败。原0.01方向的较小接受步与第三单位缺陷增加，提供了改变候选算法的具体动因；它不支持把下一轮直接规定为更小η，也不支持延长一个本来未耗尽的回溯预算作为主要修法。

主控已授权准备独立92源码：在[R278条件框架](../results/R278-finite-resonance-projective-normalization-and-local-elimination.md)下，从真实90最终p试验实际非线性p3内层求根，保原三方程、完整未加权merit/gdot/Armijo与末FD-Arb-circle。首投影和所有内层试探必须单独保存，近似d3根不置零覆盖或冒精确IFT；新入口/schema与预算另行明确。这是尚在准备的候选算法，不是本轮已计算结果、成功根或已派发92。88保存模型谱诊断也不成为92的新科学门。
