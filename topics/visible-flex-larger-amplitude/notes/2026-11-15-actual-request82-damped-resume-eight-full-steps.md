# Actual 82：同一阻尼候选完成八次全步下降，低三共振仍未解

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：公开 Actions 实际候选诊断与原件字节审计。** 全部数学运算来自实际 run 43665944742。本文在本地只读原 JSON、原文件字节、SHA、记录间一致性与整数维数，没有重算模型、RHS/J、方向、merit、有限差分、Arb 或 circle。

**实际结果：从 actual80 的真实最终参数起步，η=0.1 的八次候选方向全部在首个 α=1 试步通过，原未加权 merit 从 15492237698.871288 降到 11949245423.478903。第82轮没有被拒试步，没有用完回溯档位，也没有发生域失败；它完成了所给的八次迭代预算。最终三项单位缺陷仍为 `[224.4830723005632, -154577.5000610159, 2058.380235692375]`，小残差候选标志仍为 false。** 工作流 success 与原 status 的 `success=false` 含义不同：诊断已完成，但没有得到已接受的原非线性 BVP、非零同伦 parent 或闭曲面。

完整初末诊断、八个 6×3 方向记录和所有实际试步均保留在 [原值 readout](2026-11-15-actual82-original-readout.json)。下表及后文数值都直接复制原记录，没有本地计算降幅比、范数或新的条件数。

## 1. 运行、源码与真实父状态

| 身份 | 原记录 |
|---|---|
| 公开运行 | [43665944742](https://github.com/Rogerhu12/math-research-public/actions/runs/43665944742) |
| source commit | `f1a2c80826d106d1c92db7aeffd1dbfcd84625c6` |
| job | `132665204485`，success |
| artifact | `14141564704`，`visible-mainline-smallcoreresonance-43665944742-1` |
| ZIP | 267,442 B；`fa07a132734ca9cc604cbccc74926c8840683fd6c0eff4d2c7b510ab898c2214` |
| 原件 | 11 个文件，共 451,795 B；两个日志原本为空 |
| phase / diagnostic_completed | `diagnostic-completed` / `true` |
| 原记录用时 | 2.6710125859999962 s |
| 科学成功 / 小残差候选 | `false` / `false` |

root 唯一下载完整 ZIP，核对 size/SHA、全部 CRC、安全路径和完成 marker。本次从这一已解包原目录读取，没有重复下载或重复运行科学计算。

三层科学源码保持冻结：

| 层 | 文件及 SHA256 |
|---|---|
| 本次续接入口 | [geometry_20261115_small_core_damped_resume.py](../computations/geometry_20261115_small_core_damped_resume.py)，15,452 B；`ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a` |
| 原阻尼方向 | [geometry_20261115_small_core_damped_search.py](../computations/geometry_20261115_small_core_damped_search.py)，13,733 B；`1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728` |
| 原 R259 模型及检查 | [geometry_20261114_small_core_resonance.py](../computations/geometry_20261114_small_core_resonance.py)，25,799 B；`3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |

实际父是 run `43664043053`、source `5a17ad802c28a0a00f2776201cea4cef27f68da7` 的 actual80。其原 `damped-search-status.json` 为 52,985 B / `ebe5b50c6af5ec9cfbe201e4d19a1b24dc9357e28ac8fe89354d5c04fd13ee2a`，本次 `prior-candidate/` 与 `parent-damped-status.json` 两个副本逐字节相同。续接只取该文件的 `final.parameters`：

```json
[0.09071772300091886, -0.13939413969182854, -0.12252606423015384]
```

这三个 binary64 值在父 final、本次 parent binding、request、命令记录和本次 initial 中相同。原父是 η=1 的诊断候选；本次明确指定 η=0.1。原 J、merit 和 circle 状态没有从父记录冒名复用，本次初始模型、参数导数、方向和最终检查全部实际重新求值。父 final 与本次 initial 的残差打印值有末尾差异，因此本文也不把两者说成有限数组逐位相同，更不从两次运行推导纯粹的 η 因果效应。

四个原数学输入仍为原 accepted96、prepared112、真正 T112 零高度尾响应和 T112 config，完整 SHA 依次是：

- `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff`。
- `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714`。
- `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51`。
- `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5`。

这些输入在 request、运行前 verified identity、本次 status 和原父 status 中一致。它们没有因本次三参数候选搜索而变成新的已接受有限场。

## 2. 本次模型和八次实际试步

本次保留 [R259](../results/R259-small-core-homotopy-and-resonance-conditions.md) 的原三项单位共振方程 $r(p)$、原 Jacobian $J(p)$、原完整 scalar 公式及三处控制支持。参数 $p$ 在这个诊断中会变化，因此整个搜索过程不能称为保持单一固定 $g$ 的精化。

冻结方向引擎使用原三方程列范数形成正对角坐标尺度 $D$，然后求原 6×3 最小二乘问题：

$$\min_z\ \frac12\|JD^{-1}z+r\|_2^2+\frac12\eta^2\|z\|_2^2,\qquad d=D^{-1}z,\qquad \eta=0.1.$$

六行增广矩阵、六项右端、全部三列、返回秩、奇异值、缩放方向、恢复后的参数方向和原 $Jd$ 都实际保存。本次八个方向的原返回秩均为 3，`exactly_zero_columns=[]`。没有行方程重加权，没有组成正规方程，也没有把阻尼项加进原非线性 residual。

原非线性目标仍是 $m(p)=\frac12\|r(p)\|_2^2$。原试步为 $p+\alpha d$，先由实际原模型求值，再用记录的真实斜率 $r^T Jd$ 检查原 Armijo 条件：

$$m(p+\alpha d)\leq m(p)+0.2\alpha\,r^T Jd.$$

允许的回溯档位仍为 20 档 $\alpha=2^{-j}$，$j=0,\ldots,19$。本次八个原斜率均严格为负，每个方向都只执行并接受第一档 α=1；不存在需要推测原因的最近拒绝点。

| 迭代 | 原 merit_before | 原 actual_merit | 原真实方向斜率 | 实际 α / 试步数 |
|---:|---:|---:|---:|---:|
| 0 | 15492237698.871288 | 14941880862.545143 | -1912218886.673851 | 1 / 1 |
| 1 | 14941880862.545143 | 13325010811.661715 | -2794026790.454113 | 1 / 1 |
| 2 | 13325010811.661715 | 12871747563.190142 | -584966174.4814471 | 1 / 1 |
| 3 | 12871747563.190142 | 12575167583.72954 | -351042676.5697698 | 1 / 1 |
| 4 | 12575167583.72954 | 12359375495.575476 | -243632957.3839583 | 1 / 1 |
| 5 | 12359375495.575476 | 12192682289.281822 | -183241125.56912273 | 1 / 1 |
| 6 | 12192682289.281822 | 12059090468.87741 | -144407165.41703865 | 1 / 1 |
| 7 | 12059090468.87741 | 11949245423.478903 | -117391322.21940584 | 1 / 1 |

源码最多执行八次，本次正好记录八次已接受迭代，随后进入原最终诊断。这说明本次结束于已给迭代预算完成；它不是新增的收敛判断，也不是 line search 失败。

## 3. 实际最终参数、分量与完整 112 行

最终保存参数为：

```json
[0.07254576672993071, -0.0403277008444164, -0.11497411877394303]
```

最终三个原单位缺陷仍为：

```json
[224.4830723005632, -154577.5000610159, 2058.380235692375]
```

总 merit 的下降不能改写成每个分量都改善。第一项从本次 initial 的 206.42997159534684 增至 224.4830723005632。第三项从 initial 的 1950.1545213188472，在首个 α=1 后达到 46973.72493584256，随后落到 2058.380235692375；这个最终值仍高于 initial。第二项由 -176013.1520135708 变为 -154577.5000610159，仍是三个原单位缺陷中幅值最大的项。本次没有给出更小 η 必然改善、方向停滞唯一源于阻尼或最终共振必然存在的结论。

三个固定低 core 目标保持 `[0.4619073494154277, -0.05969451246161594, 0.015730056624372334]`，均非零。原完整 112 行首阶右残差的最终前三项为：

```json
[103.69038091498498, 9227.428503677753, 32.37843766192994]
```

它们已经乘原目标，不能与单位缺陷混称；其余 109 项是原记录的零，`high_right_leak_max=0.0`。初末两份报告都实际消费全部 112×112 真正零尾 slope J，保存的非对角非零条目数为 0、最大绝对非对角为 0.0，`ready_linear_graph_used=false`。三项单位缺陷的使用依赖这个实际对角事实，未删除或阈值化非对角条目。

本入口的 `high_free_core_Schur_elimination_computed=false` 和 `high_mode_nonresonance_proved=false` 保持原义。actual81 的有限高 109 模见证绑定另一组 actual78 参数，不能继承到本次 actual82 最终参数。若后续需要此处的高块结论，必须绑定此处的真实参数与模型另作相应诊断。

原候选容差仍为 `1e-8`，`low_mode_candidate_has_small_full_recorded_right_residual=false`。这只是原候选诊断标志，本来就不是原非线性 BVP 的接受门；本次也没有借改变该容差取得成功标签。

## 4. 最终导数、声明 scalar 域与完整 circle 的不同范围

最终三参数 Jacobian 的原记录为：

```json
[
  [-85.60096680362619, 85.28837706199478, 111.71375992730454],
  [-11040.131865442778, 132911.0263605909, -35234.63705677554],
  [36159456.902625896, 17072958.962705664, -75446824.19365034]
]
```

原奇异值 `[85388631.23710111, 127343.35147604346, 6.36700620570951]`、原数值条件数 `13411111.67137394` 均属于这次浮点报告，不能代替参数横截的区间证明。

| 最终原有限差分步长 | 原 maximum_relative_error | valid |
|---:|---:|---|
| 2e-5 | 7.60517568680229e-9 | true |
| 1e-5 | 1.874469986361574e-9 | true |
| 5e-6 | 5.09761710307341e-10 | true |

这三个检查针对原三项方程的参数导数。它们不是新的非零高度 native full-J，也不是原完整 nonlinear BVP 的边界检查。

完整声明 scalar 的原 Arb 检查仍用 160 位、最大深度 14，覆盖原区间 `['0','5113846463878377/2251799813685248']`，实际 467 leaves、24 splits、0 unresolved，所有 467 个原叶记录均标记正半径且返回的 $|ap|<1$。这些是声明的精确实数 scalar 表达式包络。原字段明确：

- 包含原 prefix 和保存的完整有限 Gauss 表达式。
- 使用源码实际返回的 `ap`，没有把它冒认为有限 Gauss 半径的真导数。
- 没有包住 literal binary64 evaluator 的舍入误差。
- 没有证明 scalar 导数兼容性或全部 C² 接口。
- 该 scalar 包络不覆盖 source-circle R 的完整 Frenet 域。

同一最终参数另有完整 circle 原检查。该文件保存 699 个节点、每节点 453 个增广状态及 RHS、112 模、N=2048、完整均值高度；不是只保低三角模。

| 原 circle 读数 | 实际值 |
|---|---|
| finite / boundary_finite | true / true |
| node / midpoint 域失败 | 0 / 0 |
| 原均匀 φ rho guard | 4096 点，通过；min rho=1.0 |
| physical_collocation_max | 3.8903884454211113e-16 |
| left_residual_max / complete_boundary_max | 0.0 / 0.0 |
| constant_collocation_max | 0.0 |
| 两组原 RMS 查询 | fraction .17267316464601146 与 .8273268353539885，各 698 点，均 0 invalid |
| 全 core / controls 跨节点一致 | true / true |

原 scalar a 与 source-circle R 仍分别保留：最终节点/中点最小 a=`0.30000000000000027`、最小 R=`0.29999999841436714`、circle 最小 β²=`0.0051531254094319134`，节点上原 `R_minus_supplied_a` 最大值=`1.9861667865939125e-9`。不能因 circle 残差很小就把 a 与 R 逐值视作同一对象。

原 full-FFT 切向检查共九项：node0/349/698 各检查模式1/2/3并比较全部物理行。末节点三项原相对误差分别为 `4.4123029535050566e-14`、`9.643159559271634e-14`、`2.499731165475382e-13`。这些既有读数全部保留，本文未重算。

这个 circle 的固定 core 目标为 `[0,0,0]`，`original_large_core_targets_retained=false`，`reference_is_not_a_nonzero_parent=true`。因此其小 collocation/BC 残差不能当作原目标幅度下的解；本次没有 native 非零 H 求解、非零同伦场或闭面接受。

## 5. 完整原件字节与来源范围

本次 [字节审计](2026-11-15-actual82-original-byte-audit.json) 完成 215 项文件、字段和来源一致性核对；[小摘要](2026-11-15-actual82-byte-audit-summary.json) 提供主要身份。它们不是新的科学接受门。

已实际读取并核对：

1. 全部 11 个原成员的长度、SHA，以及两个 gzip 文件完整解压的 CRC/解压后 SHA；root 的原 ZIP 完成 marker 也吻合。
2. 70 个 request source pin 与运行前 verified source、当前冻结文件实际字节全部一致；status 的 11 个实际消费源是其中严格对应的子集。
3. 实际 original request 与运行前 identity 的 request SHA/结构一致；完整命令的 parent SHA、η文本、8/20/160/14 与原报告一致。
4. 两个原父80副本逐字节相同，parent binding/参数 binary64 bits 与本次 initial、命令、request 一致。没有强求重新求值的 r/J 与父数值逐位相同。
5. 原 readback 是 status 字段的原值复制，其 status 描述器准确绑定 54,263 B / `1e56d89cf97e6e26904c7092e974a516905c52dd0dd47d10bd40dd4e3c3384fd`。
6. 八组原方程/J 与各自 direction record 的 unscaled 方程/J 相同；全部六行增广记录、三列、方向、$Jd$ 和唯一实际 trial 都在原 status 中。只做记录相等/形状检查，没有重新乘矩阵或重解最小二乘。
7. 完整 circle 的状态/RHS 维数、最终 scalar 参数、原域和九项切向结果与 status 一致。完整 scalar gzip 的 467 个原叶、summary 与 status 一致。

四原数学输入的全 SHA 已跨报告核对；本文另对仍在本地的同 SHA prepared112/config 原件读取字节。accepted96 与旧零尾 wrapper 不在本次 artifact 中，不宣称本次再次独立审计它们的全部 payload。公开源准备报告的 78/91 恢复范围被原样保留，本文没有在另一目录重复读取全部78恢复 payload。

本次 artifact 没有独立导出完整 112×112 slope J 数组文件，所以其全矩阵消费与对角事实来自原 Actions 诊断/固定输入绑定，不能冒称这里独立复核了新尾矩阵 raw bytes。这里也没有完整非线性 factor 或非零 native 解可审。

## 6. 后继85的最小依据与未完成项

本次八次全步都通过，下一次有据可做的是从 **actual82 最终参数的完整原 status** 再进行一次同 η=0.1、8次迭代、20档回溯的 fresh 候选调用。冻结 `ec9a56fd…` 已支持自身 schema 的真实 parent，不需要新增数学源码或更改任何原域、方程、有限差分、Arb、候选容差或完整112右残差读出。

这个后继只是重新线性化并继续有限预算候选搜索。当前证据没有要求扩大回溯，也没有先证明应减小 η；本次各分量行为也不支持保证下一轮继续下降、保证某个共振根或保证后续非零同伦成功。

本 note 冻结时，request85 仍是待主控发布的后继草稿，未实际执行。新父唯一身份是：

| 新父项 | 原值 |
|---|---|
| file | `small-core-damped-resume/damped-resume-status.json` |
| bytes / SHA | 54,263 B / `1e56d89cf97e6e26904c7092e974a516905c52dd0dd47d10bd40dd4e3c3384fd` |
| schema | `R259-original-three-equation-column-scaled-LM-resume-v1` |
| producer | `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a` |
| parent meaning | 已完成的三参数候选诊断；不是非零幅度已接受场 |

仍需真实解决低三共振及相关参数横截、高块条件和非零幅度完整 BVP，之后才谈目标大幅与闭面验收。actual82 的这次预算改善不替代这些尚未完成的工作。
