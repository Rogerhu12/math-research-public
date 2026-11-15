# Actual 87：同η的八次全步下降完成，低三共振仍未解

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：公开Actions实际候选诊断、完整原件读回与字节审计。** 本文数值全部读取原run `43669359806`。本地仅处理原JSON、SHA、gzip/CRC、字节/原值一致性、binary64参数身份和整数形状；没有重新计算方程、Jacobian、方向、merit、FD、Arb、矩阵动作或circle。

## 1. 本次实际结果

从真实85最终参数开始，原η=`0.1`、8次方向、每方向20档回溯的诊断完整完成八次方向。**八次都在第一档α=`1`接受，没有任何被拒试步。** 本轮重新求值后的原merit为：

```text
11479182858.417963 → 11289805820.156862
```

低三共振仍没有解决。最终原单位缺陷为：

```json
[228.5006013402948, -150264.2154200839, 474.3331904136449]
```

`diagnostic_completed=true`，但 `success=false`、`low_mode_candidate_has_small_full_recorded_right_residual=false`、`full_nonlinear_nonzero_lambda_solution_computed=false`、`native_nonlinear_solver_called=false`。第一单位分量继续增大，第二项仍很大；总merit下降不能写成三个分量同时接近根。

本次科学step8、原件readback9、artifact10和publisher11的官方结论均为success。它与85科学完成之后的publisher错误分开：本次没有把85原科学重算成一次出版修复，也没有继承不存在的非零parent。

全部原字段和八份方向保存在 [literal readout](2026-11-15-actual87-original-readout.json)；[完整字节审计](2026-11-15-actual87-original-byte-audit.json) 和 [小摘要](2026-11-15-actual87-byte-audit-summary.json) 保留完整范围。它们不是后继候选的新科学门。

## 2. 官方身份和完整原包

| 项目 | 实际身份 |
|---|---|
| run | [43669359806](https://github.com/Rogerhu12/math-research-public/actions/runs/43669359806) |
| source | `3c7c5eeffb4e234b92d15656378685ea434d91b8` |
| job | `132675725853` |
| artifact | `14142618899`，`visible-mainline-smallcoreresonance-43669359806-1` |
| ZIP | `268956` B / `252a1f9c535001d755cd7572bfdbb8708043a179664909bb3b2c5480d453eff4` |
| 原成员 | 11件，共 `457019` B，含两个空日志 |
| 原诊断用时 | `3.708353659000011` s |
| 原schema | `R259-original-three-equation-column-scaled-LM-resume-v1` |

主控唯一下载完整ZIP并核size、SHA、CRC、安全解包路径和完成marker。本文消费该原目录，没有另取包或重跑科学。官方step/publisher结论由主控给出，本次没有声称额外取得或重审完整官方joblog。

原科学三层均不变：

- `geometry_20261115_small_core_damped_resume.py` / `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a`；
- `geometry_20261115_small_core_damped_search.py` / `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728`；
- `geometry_20261114_small_core_resonance.py` / `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5`。

原70个request source pin和status实际消费的11源，与当前冻结源文件逐SHA相符。原η、8/20、容差与全部检查未变。

## 3. 真正父候选与重新求值的差别

父为actual85 run `43667636063` / source `c9daab1a9f7b1330c6099450bd018bfab9026b0d` 的原状态，54251 B / `72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a`。原 `prior-candidate/actual85-damped-resume-status.json` 与 `small-core-damped-resume/parent-damped-status.json` 两副本逐字节相同。

唯一复用的数学初猜为父 `final.parameters`：

```json
[0.06389479553738595, -0.012958081345244933, -0.11220747933971734]
```

父final、本轮binding、request、实际命令和initial三参数逐binary64位相同。原状态同时保 `only_literal_parameters_reused=true`、`parent_J_or_merit_or_state_reused=false`，且本轮模型与description真实重新求值。

不能因此把父末读数与新初读数宣称为逐位相同：

| 原字段 | 85末次原记录 | 87 fresh初次原记录 |
|---|---|---|
| merit | `11479182858.417969` | `11479182858.417963` |
| 第二单位缺陷 | `-151517.87117025955` | `-151517.8711702595` |
| 第三单位缺陷 | `805.4623398988991` | `805.4623399020538` |

这些数值分别原样保存；本地没有重算差值、归因舍入机制或将两次有限模型强制视作字节同一。后续merit表全部使用87本轮原记录。

四原数学输入仍是accepted96、prepared112、真正T112零高度响应和配置，原SHA依次为：

```text
b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff
0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714
e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51
01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5
```

四者在request、verified identity、父和本轮status中一致。设计参数在搜索中变化，所以搜索过程不冒同一个固定g的几何精化。

## 4. 全部八份方向与试步

仍以原三方程r及其参数Jacobian J构造列尺度D，求原6×3正阻尼方向：

$$\min_z\frac12\|JD^{-1}z+r\|_2^2+\frac12\eta^2\|z\|_2^2,\qquad d=D^{-1}z,\qquad\eta=0.1.$$

全部八份原6×3矩阵、右端、列尺度、z、恢复后的d、原Jd及实际斜率都在readout。增广返回秩均3，零列集合均为空；这是原数值记录，不是原J满秩或参数横截性证明。没有改变原三个方程的行权重或把阻尼加入非线性残差。

真实试步仍在原域下检查原未加权merit及原0.2 Armijo条件。20档预算是 `1…2^-19`；本次只用了每个方向的首档。

| 迭代 | 原merit_before | 原actual_merit | 原真实斜率 | 实际α / 档数 |
|---:|---:|---:|---:|---:|
| 0 | `11479182858.417963` | `11446729738.783155` | `-33524828.88995002` | `1 / 1` |
| 1 | `11446729738.783155` | `11417462176.072823` | `-30193624.4781083` | `1 / 1` |
| 2 | `11417462176.072823` | `11390968730.872835` | `-27299876.660217766` | `1 / 1` |
| 3 | `11390968730.872835` | `11366906268.36803` | `-24769569.819712356` | `1 / 1` |
| 4 | `11366906268.36803` | `11344986155.051592` | `-22543957.99747267` | `1 / 1` |
| 5 | `11344986155.051592` | `11324963717.690739` | `-20575876.133056104` | `1 / 1` |
| 6 | `11324963717.690739` | `11306630088.190746` | `-18827064.733052984` | `1 / 1` |
| 7 | `11306630088.190746` | `11289805820.156862` | `-17266198.25080994` | `1 / 1` |

没有最近拒绝档、没有20档截断，也没有本轮科学例外。阶段完成是用完所给八步预算后执行原最终检查，不能因8个全步而称已收敛。

## 5. 最终低三、完整112行及原参数导数

最终参数：

```json
[0.057323451817869575, 0.002679377797021207, -0.11058649307511116]
```

原低三固定目标仍是 `[0.4619073494154277,-0.05969451246161594,0.015730056624372334]`，三者非零。原完整112×112零锚slope-J全部消费，报告最大非对角项0、非零非对角数0，`ready_linear_graph_used=false`。

本轮final完整112行首阶右残差前三项：

```json
[105.5461071049269, 8969.94907992914, 7.461287944025818]
```

剩余109项是原保存的signed zero，完整数组保留在readout。这些前三项是乘相应原目标后的完整右残差，不是unit d本身。原迭代提前停止检查unit三方程；最终小残差候选标志检查完整112行。两处原tol均1e-8，但不能在目标缩放后默称同一数值判据。此次两者都远未通过。

零高行只是本特定零高core试探的结果。原status仍明确未计算高自由core Schur、未证明高块非共振或区间横截性；actual81在另一组actual78参数上的结果不能直接继承。

原final参数Jacobian为：

```json
[
  [-61.424209555027964, 27.378538007218882, 107.86795306331801],
  [-5903.90526538666, 69119.74438448333, -29955.759380183084],
  [28285572.05781767, 20975080.159062225, -72757290.27347714]
]
```

其原保存奇异值为 `[80831013.21276167,62249.60462003157,2.2055322265372443]`，数值条件数 `36649209.76451518`。原三个FD步长均valid，最大相对误差：

| 原步长 | 原maximum_relative_error |
|---:|---:|
| `2e-5` | `1.0077563448607579e-8` |
| `1e-5` | `2.539332911758288e-9` |
| `5e-6` | `7.422295551997082e-10` |

这些是原浮点导数/坐标差分诊断；它们不是精确参数横截证明，也不单独认证弱奇异组合方向的导数误差。没有在本地重新做SVD或FD。

三mode原轨迹max为 `[10.983808399124847,3511.3343880422008,8.91934961510355]`，原小右块条件max为 `[1.3950728979080156,4.568977826735946,17.11359640727734]`，原tangent collocation残差max为 `3.979039320256561e-13`。高参数敏感度不能直接改写为第三mode轨迹爆炸。

## 6. 原Arb标量域与完整zero-core circle

原160位、最大深度14的Arb报告共有466个叶、23个split、0 unresolved，全部原叶标记严格正a且 `abs(returned_ap)<1`。范围是完整声明实scalar表达式，不是literal binary64逐操作误差包络；也不证明a与独立返回ap的导数身份、C2接口、source-circle全区间或整个Frenet域。

原circle保存699个节点的453项增广状态及RHS、完整均值和场布局，另附完整低三单位UH及其RHS轨迹。不得把这些附加低三轨迹说成112个单位模态都独立导出。

| 原circle读数 | 实际值 |
|---|---|
| full reference / boundary finite | true / true |
| node / midpoint失败 | `0 / 0` |
| 原4096角rho guard | valid，minimum `1.0` |
| physical collocation max | `4.434793461280395e-16` |
| left / complete BC max | `0.0 / 0.0` |
| constant collocation max | `0.0` |
| 左/右RMS查询族 | `.17267316464601146` / `.8273268353539885`，各698点，均0 invalid |
| core及controls跨节点常值 | true / true |

final原采样a minimum为 `0.30000000000000027`，source-circle R minimum为 `0.29999999841510355`，最小beta平方为 `0.005153125404548042`，节点R与给定a最大差 `1.9853435007100018e-9`。两个有限对象没有被声明逐位相等。

全部九项原full-FFT切向检查保留，覆盖node0/349/698与mode1/2/3，每项比较完整物理行。末节点三项原相对误差为 `4.3202110795892547e-16`、`1.3753848535058893e-15`、`7.243532973201747e-15`。

circle明确 `fixed_core_targets=[0,0,0]`、`original_large_core_targets_retained=false`、`reference_is_not_a_nonzero_parent=true`、所有接受字段false。这些小collocation/BC读数不代表大核目标、非零同伦、native或闭面通过。

## 7. 原件与已付字节范围

| 原文件 | 字节 | SHA256 |
|---|---:|---|
| `small-core-damped-resume/damped-resume-status.json` | 54279 | `e805446d14713957dd67e715d9d28193c14c20002e00b0a1ace2e4ac1c03dd80` |
| 父85状态副本，两件各 | 54251 | `72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a` |
| `small-core-damped-resume/circle-reference.json.gz` | 139692 | `e6d299a45ab6c52569d336e718ba55e1f9aa3fb916afd4ffb11f9efaec9d7fae` |
| `small-core-damped-resume/complete-scalar-domain.json.gz` | 75333 | `96bcad5faebef09c4dce2c3a12858d09f67cb5baf9d30431a7ef7f759b9d5a03` |
| `small-core-resonance-readback.json` | 19878 | `9ec1a9682c7b9bc04789f6c2fe318920e070c4aa696093127a114d9752f9dcc3` |
| `request87-input-and-source-identity.json` | 35910 | `10ee16d9453c8c5ece35990f06a880f1703ee18a0016e208190b08bad3f97dff` |
| `exact-diagnostic-command.json` | 3001 | `935a090ce6f2fc80ea4a1e3fd887db57b39c4b9965120b21a9ef1bddf8eab2a4` |

其余原public-source报告和两个空日志均在完整inventory。216项原字节/字段/结构检查通过：

1. 全11件长度与SHA、两个gzip完整解压CRC及解压后SHA、原完成marker相符；原包下载SHA/CRC由主控完成。
2. 70个request pin、原Actions verified source记录与当前冻结文件一致；status11消费源是对应子集。
3. request原SHA与运行identity相同；原命令保真实父SHA、η文本和全部8/20/160/14参数。
4. 两父副本逐字节相同；父最终参数在binding/request/command/initial间逐binary64位相同；父末诊断与本轮fresh初诊断的数值差异另列，不强制相等。
5. small readback原字段与status逐值一致；原状态描述器准确绑定54279B文件。
6. 八组原方程/J与direction内unscaled数组对应，完整6×3形状、原方向、原Jd及全部八次trial保留；没有重新矩阵乘法或求方向。
7. 全466个叶的保存范围/标志与summary相符；699×453 circle、低三UH、冻结参数和九项切向读数相互绑定。

四原输入在request、verified identity、父与当前status间核身份。额外仅读现有同SHA prepared112/config原payload；本次小artifact不含accepted96或完整零尾payload，不冒独立重审。public78恢复报告只原样保全，不重新读全部78个源payload。

完整112×112 slope-J没有独立导出到此包；全部消费/对角事实来自实际Actions记录及固定输入，不能冒称此次新审J raw。Arb叶和circle只作原字节/结构核对，不在本地验证数值表达式或重算解。没有导出或产生非零native factor/accepted field。

## 8. 可供后继的真实状态与下一责任

新父状态为54279 B / `e805446d14713957dd67e715d9d28193c14c20002e00b0a1ace2e4ac1c03dd80`，同ec9 own-schema；final参数为本节前列三值。它仍只是候选参数初猜。

本轮没有回溯截断，因而不据此扩大20档预算。主控已据实际八个全步及仍大的原残差授权准备下一独立候选request90：从真87 final参数开始，只把显式η从0.1改为0.01，仍同ec9/1691/3b9、8/20和全部原检查。此处仅登记后继设计，不声称90已派发、下降或求根，也不说较小η必定改善。

saved85小矩阵谱消费者另为独立诊断，可以解释保存局部模型的阻尼滤波；它不替代下一真实候选的原域/merit/FD/Arb/circle，也不是后继前置门。低三真根、当前参数高块与横截条件、非零同伦完整BVP/native及最终幅度/闭面仍须分别取得证据。
