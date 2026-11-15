# Actual 85：八次全步候选下降完成，低三共振仍未解；发布另受 HANDOFF 长度限制

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：公开 Actions 实际候选诊断、原件读回与字节审计。** 下列数学数值全部来自实际 run `43667636063`。本地只读取原 JSON、文件字节、SHA、原值相等关系、binary64 参数身份和整数维数；没有重新计算 residual、Jacobian、方向、merit、有限差分、Arb 或 circle。

## 1. 科学结果与发布结果分开

从 actual82 的真实最终参数开始，原 η=`0.1`、8 次迭代、20 档回溯的候选搜索**完整完成八次方向，每次都在第一档 α=`1` 接受，没有被拒试步**。原未加权 merit 从 `11949245423.478903` 降至 `11479182858.417969`。诊断状态为 `diagnostic-completed`、`diagnostic_completed=true`。

这没有解决低三共振。最终三个原单位缺陷仍为：

```json
[227.29559514822407, -151517.87117025955, 805.4623398988991]
```

`success=false`、`low_mode_candidate_has_small_full_recorded_right_residual=false`、`full_nonlinear_nonzero_lambda_solution_computed=false`、`native_nonlinear_solver_called=false` 均保留。没有新的已接受非零同伦 parent、原完整 BVP、大幅曲面或闭面结果。

工作流的科学步骤 8、原件读回步骤 9、artifact 保存步骤 10 均成功。**随后 publisher 步骤 11 失败**，其官方原日志在 `2026-11-15T02:25:09Z` 记录：

```text
root_20261114_publish_actions.py:202
RuntimeError: Preserve a unique rule-read line and the original HANDOFF size bound
```

原进程返回 1。这是保存科学 artifact 之后的发布层错误，不是候选计算、FD、Arb 或 circle 失败。主控从原日志定位到规则记录替换触发原 HANDOFF 大小约束；后续由主控压缩交接记录并原字节恢复这批小产物，不改变 publisher 门或数学源，也不需要重新运行科学计算。本 note 冻结时只记录错误和恢复范围，不把尚未报告的后续 Git 发布写成已经成功。

官方日志独立于科学 artifact：`132670464205-logs.txt` 为 `49644` B，SHA `8403d7bc6f609bbd017cd9d5d4f40d1dd79f34d4ca6ffdf2cb93699bcb18ba6d`。日志的原错误文本和源行已单独核对。

完整初末结果、八个原 6×3 方向、全部试步及发布错误身份均保存在 [literal readout](2026-11-15-actual85-original-readout.json)；[完整字节审计](2026-11-15-actual85-original-byte-audit.json) 和 [小摘要](2026-11-15-actual85-byte-audit-summary.json) 明示各自范围。这些文件不是新增科学门。

## 2. 运行、来源与真正父候选

| 项目 | 实际身份 |
|---|---|
| 公开 run | [43667636063](https://github.com/Rogerhu12/math-research-public/actions/runs/43667636063) |
| source commit | `c9daab1a9f7b1330c6099450bd018bfab9026b0d` |
| job | `132670464205` |
| artifact | `14143056682`，`visible-mainline-smallcoreresonance-43667636063-1` |
| 原 ZIP | `268505` B；`708ce51fb634552d376013d05b57e4f42cdc07d699e25753a2af0a2ea36e5775` |
| 已解包原成员 | 11 件，共 `455455` B；两个原日志为零字节 |
| 原诊断用时 | `2.867001565999999` s |
| 原 schema | `R259-original-three-equation-column-scaled-LM-resume-v1` |

主控唯一下载原 ZIP 并核 size、SHA、CRC、安全路径和完成 marker。本文只消费该已解包目录，没有重复下载或重新求解。原件恢复的目标公开目录为 `notes/public-actions-43667636063-1-smallcoreresonance/`。

本次沿用已冻结的三层科学源码：

| 层 | 文件 / SHA256 |
|---|---|
| own-schema 续接入口 | [geometry_20261115_small_core_damped_resume.py](../computations/geometry_20261115_small_core_damped_resume.py)，`ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a` |
| 列尺度阻尼方向 | [geometry_20261115_small_core_damped_search.py](../computations/geometry_20261115_small_core_damped_search.py)，`1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728` |
| 原 R259 方程与检查 | [geometry_20261114_small_core_resonance.py](../computations/geometry_20261114_small_core_resonance.py)，`3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |

真正父状态来自 actual82，run `43665944742`、source `f1a2c80826d106d1c92db7aeffd1dbfcd84625c6`。父原 `damped-resume-status.json` 是 `54263` B / `1e56d89cf97e6e26904c7092e974a516905c52dd0dd47d10bd40dd4e3c3384fd`。本次 `prior-candidate/actual82-damped-resume-status.json` 与 `small-core-damped-resume/parent-damped-status.json` 两个副本逐字节相同。

唯一复用的数学初猜是父 `final.parameters` 的原三个 binary64 值：

```json
[0.07254576672993071, -0.0403277008444164, -0.11497411877394303]
```

这些值在父 final、本次 parent binding、request、实际命令和本次 initial 中逐位相同。父和本次使用同一 resume schema、同一 `ec9a56fd…` 源和同 η=`0.1`。原状态明确 `only_literal_parameters_reused=true`、`parent_J_or_merit_or_state_reused=false`；初始模型与描述实际重新求值，不是把父 J、merit 或 circle 标签换名。

原四输入仍绑定 accepted96、prepared112、真正零高度 T112 尾响应、T112 config，其 SHA 依次为：

- `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`；
- `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`；
- `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`；
- `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。

它们在原 request、运行前 verified identity、父状态与本次状态中一致。此候选搜索改变 scalar 设计参数，因此其全过程不能描述成保持单一固定 $g$ 的几何精化；原公式和三个控制支持保持同源，也不等于各轮参数值不变。

## 3. 原方向与所有八次试步

本次没有改变 [R259](../results/R259-small-core-homotopy-and-resonance-conditions.md) 的三项原单位方程 $r(p)$、其原参数 Jacobian $J(p)$ 或原非线性目标。冻结方向引擎以原列范数形成 $D$，求：

$$\min_z\ \frac12\|JD^{-1}z+r\|_2^2+\frac12\eta^2\|z\|_2^2,\qquad d=D^{-1}z,\qquad\eta=0.1.$$

所有八份原记录都保留完整 6×3 增广矩阵、六项右端、三列尺度、缩放方向、恢复的三参数方向及原 $Jd$。八个原返回秩均为 3，`exactly_zero_columns=[]`。没有行方程重加权，没有组成正规方程，也没有把阻尼项计入原非线性 residual 或原 merit。

原目标为 $m(p)=\frac12\|r(p)\|_2^2$；试步 $p+\alpha d$ 按实际原模型和原域求值，以真实记录的 $r^T Jd$ 检查原条件：

$$m(p+\alpha d)\leq m(p)+0.2\alpha r^TJd.$$

回溯预算仍为 20 档 $\alpha=2^{-j}$，$j=0,\ldots,19$。本次没有走到第二档，也没有一个失败 trial。

| 迭代 | 原 merit_before | 原 actual_merit | 原真实斜率 $r^TJd$ | 实际 α / 试步数 |
|---:|---:|---:|---:|---:|
| 0 | `11949245423.478903` | `11857177282.869364` | `-97590551.78529117` | `1 / 1` |
| 1 | `11857177282.869364` | `11778842971.475813` | `-82524876.18599023` | `1 / 1` |
| 2 | `11778842971.475813` | `11711382129.186562` | `-70732657.79707752` | `1 / 1` |
| 3 | `11711382129.186562` | `11652701574.972935` | `-61294383.16658413` | `1 / 1` |
| 4 | `11652701574.972935` | `11601227422.48267` | `-53602148.21022714` | `1 / 1` |
| 5 | `11601227422.48267` | `11555749495.037792` | `-47238005.10096173` | `1 / 1` |
| 6 | `11555749495.037792` | `11515319616.403164` | `-41905324.62610968` | `1 / 1` |
| 7 | `11515319616.403164` | `11479182858.417969` | `-37387953.12203577` | `1 / 1` |

八次原斜率均为负，八次实际接受完成所给的迭代预算，然后执行最终检查。这不是 line search 截断，没有“最近被拒档”需要推断，也不需要因 publisher 失败而扩大回溯或重复同一次候选。

## 4. 最终参数、分量与全 112 行的原义

最终参数为：

```json
[0.06389479553738595, -0.012958081345244933, -0.11220747933971734]
```

三个原单位缺陷从 initial 的

```json
[224.4830723005632, -154577.5000610159, 2058.380235692375]
```

变成 final 的

```json
[227.29559514822407, -151517.87117025955, 805.4623398988991]
```

总 merit 下降不意味着每个分量下降：第一项实际增大；第二项仍有很大负缺陷；第三项下降。本文不从这些打印值本地重算百分比、范数、方向质量比或参数条件数，也不把阻尼当成唯一已证原因。

原目标低三 core 仍为 `[0.4619073494154277, -0.05969451246161594, 0.015730056624372334]`，均非零。完整 112 行首阶右残差 final 的前三项是：

```json
[104.98950588871833, 9044.785448730578, 12.669968215409119]
```

这些是乘原目标后的完整右残差，不能与三项单位缺陷混为同一数。其余109项保留原带符号零，`high_right_leak_max=0.0`。全部112项高度向量和112项右残差都存于原初末报告，没有裁成只读前三项的计算。

原初末报告都记录完整112×112真零尾 slope J 实际全条目消费，`nonzero_offdiagonal_entries=0`、`maximum_absolute_offdiagonal=0.0`、`exactly_diagonal_as_recorded=true`，并保留 `ready_linear_graph_used=false`。三项单位共振方程在这里依赖已实际测得的这个对角事实，不是把非对角条目阈值清零或默默省略完整尾耦合。

不过，本候选入口仍明确 `high_free_core_Schur_elimination_computed=false`、`high_mode_nonresonance_proved=false`、`high_mode_nonresonance_or_interval_transversality_proved=false`。actual81 的高109结论绑定别的 actual78 参数，不能继承给本次 final 参数。此处也没有低三参数的区间横截证明。

原候选阈值仍是 `1e-8`，其小完整右残差标志仍为 false。这是候选诊断标志，本来就不是原非线性 BVP 接受门。本次没有改变阈值来获得成功标签。

## 5. 参数导数与声明 scalar 域

final 原三参数 Jacobian 为：

```json
[
  [-71.9315506504092, 48.217108005339206, 109.32189126283022],
  [-8948.488214804847, 91414.350103322, -31243.731911725532],
  [31902324.156211372, 19476540.307536047, -73565444.45135504]
]
```

保存的 final 奇异值是 `[82516487.07773717, 85436.77882713315, 3.1617049680040474]`，数值条件数 `26098730.87868442`。这些是原浮点诊断，不能作为严格横截证书。

| 最终原参数 FD 步长 | 原 maximum_relative_error | valid |
|---:|---:|---|
| `2e-5` | `8.84379391402425e-9` | true |
| `1e-5` | `2.1750304800170322e-9` | true |
| `5e-6` | `6.167107431449232e-10` | true |

这些检查针对同一三项原共振方程的参数导数；不是新非零高度 native full-J 或完整 nonlinear BVP 边界验证。原完整circle切向系统仍区分源码返回的 `a/ap` 与有限 Gauss 半径表达式的真导数，不使用独立 `app` 字段冒充后者。

原 Arb 检查在 final 参数下用160位、最大深度14覆盖区间 `['0','5113846463878377/2251799813685248']`。实际 `466` leaves、`23` splits、`0` unresolved，所有466个原叶记录都标记严格正半径和返回的 $|ap|<1$。

该结论的范围仍是**声明的精确实数 scalar 表达式**：包含原prefix和完整保存的有限Gauss表达式，使用源码返回的 `ap`。它不包住literal binary64 evaluator的全部舍入，不把返回 `ap` 认作有限Gauss `a` 的精确导数，不证明全部scalar C²接口，也不覆盖source-circle R 的完整Frenet域。原status各范围字段和完整叶记录均保留；本地没有重算Arb。

## 6. 另行完成的完整零core circle检查

同一final参数的 `circle-reference.json.gz` 保存699节点、每节点453项增广状态和RHS、全112模及完整均值高度；不是仅三个低模示意。

| 原 circle 指标 | 实际值 |
|---|---|
| 全原reference finite / boundary finite | true / true |
| node / midpoint 失败 | `0 / 0` |
| 原4096角rho guard | valid，minimum `1.0` |
| physical_collocation_max | `4.487783842460624e-16` |
| left / complete boundary residual max | `0.0 / 0.0` |
| constant_collocation_max | `0.0` |
| 两原RMS查询族 | fraction `.17267316464601146`、`.8273268353539885`，各698点，均0 invalid |
| core / controls 跨节点同值 | true / true |

原半径对象仍分开：final sampled `a` minimum为 `0.30000000000000027`，source-circle `R` minimum为 `0.2999999984148426`；source-circle sampled最小 $\beta^2$ 为 `0.005153125406278547`，节点原 `R_minus_supplied_a` 最大值 `1.9856352673208733e-9`。circle的很小collocation残差不使这两个有限对象逐位相同。

原 full-FFT 切向检查共九项，node0/349/698各模式1/2/3，都比较完整物理行。末节点三个原相对误差分别为 `4.372102934820961e-14`、`9.513934511583125e-14`、`2.4865832007450146e-13`；其余六项也完整存于readout。

这个circle明确使用 `fixed_core_targets=[0,0,0]`，`original_large_core_targets_retained=false`，`reference_is_not_a_nonzero_parent=true`；它不是原大核目标的完整解。上述小collocation/BC值没有建立非零同伦parent，没有新native非零H求解，没有闭曲面接受。

## 7. 完整原件、来源与字节审计范围

本次完整读取全部11个原小包成员，并核对其字节、记录和来源。关键文件如下：

| 原文件 | 字节数 | SHA256 |
|---|---:|---|
| `small-core-damped-resume/damped-resume-status.json` | `54251` | `72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a` |
| 两份原父82 status，各一份 | `54263` | `1e56d89cf97e6e26904c7092e974a516905c52dd0dd47d10bd40dd4e3c3384fd` |
| `small-core-damped-resume/circle-reference.json.gz` | `139790` | `f9d38046788b71765d44015187d3ca7513b4b040883bd1aee177a8fb387207b0` |
| `small-core-damped-resume/complete-scalar-domain.json.gz` | `75230` | `b2daeccc275dff4c88aaf7747bcd7ae513d02f5ddbcf729f304ef370ac915896` |
| `small-core-resonance-readback.json` | `19871` | `26d501b8a1c7db33ef1faf3d9401d69651925546ead18f1c4c954f4ce10fa917` |
| `request85-input-and-source-identity.json` | `34364` | `1fce1159375e734b0386fefd04bbf5717d34042df74179493deb3b56ee98745b` |
| `exact-diagnostic-command.json` | `2999` | `809b413c0e17680ce7802447556c4268e3ad20d73f4f3a91714f2b5534674cd7` |

其余public source准备报告和两个空日志完整列入audit；另行取得的官方joblog属于外部出版证据，不混入科学artifact的11件成员计数。完整audit通过218项文件/字段/结构检查：

1. 所有11件长度与SHA、两个gzip完整解压CRC/解压后SHA、原完成marker，与已取得原记录对应。
2. 70个request source pin与原Actions verified source记录及当前冻结源字节一致；status实际消费的11源是严格对应子集。
3. request原字节/SHA与原identity相同；完整命令保真实父SHA及η文本、8/20、160位/深度14。
4. 两父副本逐字节相同，原父schema/producer和只复用literal final参数的身份一致；参数bits在父/binding/request/命令/initial吻合。
5. 原small readback是status原字段复制，未重新执行科学；其status描述器准确绑定上述54251B新status。
6. 八组原方程/J与各方向记录内unscaled方程/J相同，六行三列形状、返回秩、原方向和全部实际试步均保存。只核原记录，不重新乘矩阵或解least-squares。
7. 全部466个原Arb叶及summary与status一致，完整699×453 circle、低三UH记录、最终冻结参数、原域和九项FFT切向记录互相绑定。
8. 原官方发布错误日志的实际字节/SHA及准确错误文本另行核对，和科学成功的范围分开。

四原输入的绑定在request、verified identity、父/当前status间核对。本地仅额外重读现仍保存的同SHA prepared112/config原payload；accepted96与旧零尾响应不在这个小artifact中，不宣称本次独立重审它们全部payload。public source准备报告保原78/91数值子集恢复范围，本次没有再读全部78个恢复payload。

本artifact没有独立导出112×112 slope-J数组；全矩阵消费/对角事实来自实际Actions报告与固定原输入，不冒称此处新审完整J raw。全部Arb叶和circle是字节/结构读回，不是本地重新验证数学表达式或数值解。完整非零native factor或非零accepted field也未产生。

## 8. 可供下一候选的准确状态与仍未完成的问题

新完整status为 `54251` B / `72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a`，schema仍为 `R259-original-three-equation-column-scaled-LM-resume-v1`，producer仍为 `ec9a56fd…`。冻结own-schema入口可以从其真实 `final.parameters` 重新求值一个后续候选；它复用的仍只是参数初猜，不能复用一个不存在的非零场或native解。

本次可支持的具体判断是：原搜索没有被回溯预算限制；当前数据不要求增加backtracks，发布失败也不要求重新支付这八步。有限预算下降持续但低三残差远未达到候选容差，第一分量还增大。若后续改变η，应明确为另一个有独立原方向、真实斜率和原域/Armijo试步的算法比较，不能从本次打印值保证更小η会成功，也不能把阻尼称为已证明的唯一瓶颈。

本note不指定或声称已经完成下一科学请求。主控先按原字节恢复本批11件公开产物，后续选择须绑定这个真实status。低三共振、相应参数横截和当前参数的高块条件，以及非零同伦的完整BVP/native/闭面/幅度接受，仍需分别取得实际证据。
