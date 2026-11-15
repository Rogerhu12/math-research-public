# Request 90：从真实87候选将显式方向阻尼改为 η=0.01

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：独立工作流与来源接线草稿；仅源文本、原JSON及文件字节操作。** 本稿没有修改科学源码、仓库或分支，没有本地数学导入或执行，没有派发，也没有填写未来run。主控负责唯一正常Git发布与公开Actions运行。这份接口说明不增加候选或BVP接受门。

## 1. 真实动因和唯一算法参数变化

[实际87正式结论](2026-11-15-actual-request87-damped-resume-eight-full-steps-low-three-unresolved.md) 完整读回八个原方向。八次均在首个 `alpha=1` 接受，没有被拒trial或回溯预算耗尽。原保存merit为 `11479182858.417963 → 11289805820.156862`，最终单位方程为 `[228.5006013402948,-150264.2154200839,474.3331904136449]`。分量没有同时改善，第二分量仍大。`diagnostic_completed=true`，但 `success=false`、原完整右残差小候选标志false；没有共振根或非零幅度parent。

本次从真实87的最终参数重新评价原模型，把显式正阻尼参数从父 `eta=0.1` 改为当前 `eta=0.01`。仍最多八个方向、每方向原20档回溯，原三方程、原未加权merit与全部最终检查保持。η改变的是原方向子问题，没有加入或替换原非线性方程。参数搜索期间的设计p继续变化，不冒固定同一个g的精化。

这是一个明确的候选算法参数选择。它不证明过去的慢降唯一由η导致，不保证较小η接受、加快下降或得到根。新的初值、模型和浮点评价也不与87同一固定矩阵相认；不能把两轮表现只归因于η。独立saved85局部模型消费者不是本次运行的前置门。

父87起始merit `11479182858.417963` 与85末记录 `11479182858.417969` 的末位不同已经在正式87记录保留。本草稿只复用87最终三个参数，不复用父J、merit、模型状态或宣称新旧重评价逐位相等。

## 2. 真实父原件与冻结源

实际87：run `43669359806`，source `3c7c5eeffb4e234b92d15656378685ea434d91b8`，job `132675725853`；artifact `14142618899`，268956 B，ZIP SHA `252a1f9c535001d755cd7572bfdbb8708043a179664909bb3b2c5480d453eff4`。科学、原读回、artifact保存与publisher均成功。

唯一父状态为原公开路径：

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43669359806-1-smallcoreresonance/small-core-damped-resume/damped-resume-status.json
54279 B
SHA256 e805446d14713957dd67e715d9d28193c14c20002e00b0a1ace2e4ac1c03dd80
```

只复用 `final.parameters`。草稿literal与原JSON各参数binary64位均已比对：

```json
[0.057323451817869575, 0.002679377797021207, -0.11058649307511116]
```

| 角色 | 原文件与字节 | 完整SHA256 |
|---|---|---|
| 同schema续接 | `geometry_20261115_small_core_damped_resume.py`，15452 B | `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a` |
| 原列缩放正阻尼方向 | `geometry_20261115_small_core_damped_search.py`，13733 B | `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728` |
| 原三方程及最终检查 | `geometry_20261114_small_core_resonance.py`，25799 B | `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |

全部70源pin、四原数学输入、runtime、原78公共源恢复和proofs与87逐值相同。accepted96、prepared112、真实T112零锚和原配置的完整公开路径、字节、SHA保存在新request中。publisher仍是 `root_20261114_publish_actions.py` / `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`；不修改其大小界限或普通同步规则。

## 3. 为什么原own-schema接口允许新的显式η

冻结ec9入口的 `checked_parent(path, expected_sha256, current_source_sha256)` 核父原字节、完成诊断范围、同schema生产者、原方向源、完整11消费源集合、三参数literal及四原输入。它没有当前damping参数；原父 `damping_cli_text`、`damping_binary64` 仅写入来源receipt，未与当前η比较。静态检查遍历原AST确认这两个父字段只在receipt赋值出现，没有父/当前阻尼相等的判断。

`main` 独立解析当前 `--damping` 字符串，要求其binary64值有限且严格正，然后把此值传给原 `damped_direction(np, derivative, residual, damping)`。因此本次不需要修改、绕过或重新命名任何原guard。

元数据明确区分：父 `previous_damping_cli_text="0.1"`，新 `new_explicit_damping_cli_text="0.01"`，`same_positive_damping_as_parent=false`；scope中对应同父阻尼字段也是false。当前direction model和CLI都记录0.01。父54279 B原件自身保持不变，其η=0.1不会被改写为本轮η。

## 4. 原调用与全部保留范围

原单一科学step的通用run正文和45分钟timeout与87逐字相同；正文从新request读取参数，因此实际传入新的η和父路径。该事实不等于η没有改变。唯一调用为：

```text
python -u geometry_20261115_small_core_damped_resume.py
  --accepted <原accepted96路径>
  --prepared <原prepared112路径>
  --tail-anchor <原真实T112零锚路径>
  --tail-config <原T112配置路径>
  --parent-status <上述真实87完整状态路径>
  --parent-status-sha256 e805446d14713957dd67e715d9d28193c14c20002e00b0a1ace2e4ac1c03dd80
  --damping 0.01
  --candidate-steps 8
  --backtracks 20
  --candidate-resonance-tolerance 1e-08
  --interval-bits 160
  --interval-depth 14
  --out "$VISIBLE_OUT/small-core-damped-resume"
```

尖括号仅为接口说明。静态receipt的 `actual_command_shape` 列出全部真实路径，工作流不传占位符。

每轮仍用原三方程和三列完整参数Jacobian，原列尺度D、6×3方向子问题与恢复 `d=D^-1 z`，并从恢复方向计算真实 `r dot (J d)`。实际merit仍是原三方程平方和的一半，不把η罚项加入真实merit。原0.2 Armijo系数、20档 `1…2^-19`、域/线性代数异常处理和接受逻辑不变。

循环的原单位方程阈值与结束时完整112右残差小候选标志是不同读数，二者均保原 `1e-8`，不互换或冒原BVP接受。最终参数FD、原160位/14深度Arb及完整699节点zero-core circle由原函数执行。输出low3单位轨迹不冒全部112单位模已独立求解。

所有112×112真实零锚斜率J条目仍读取；原可选三方程搜索仍要求实际严格对角和三个原目标非零，不能阈值化非对角项、静默删除高109或换成ready代理。本轮不继承其他参数处的高109非共振或Arb结论。高块/横截性、非零分支存在及最终大幅BVP均未因此证明。Arb的范围仍限声明实表达式a/ap，不是整个有限场或整段几何证书。

输出继续 `small-core-damped-resume/damped-resume-status.json` 和 `R259-original-three-equation-column-scaled-LM-resume-v1`。预运行来源副本为 `prior-candidate/actual87-damped-resume-status.json`，身份账为 `request90-input-and-source-identity.json`。原readback、完整artifact及publisher正文不变，保留失败/未接受候选的真实记录。

## 5. 唯一发布目标与完整diff

| 草稿basename | 既有仓库目标 | 字节 / SHA256 |
|---|---|---|
| `visible-larger-public-small-core-resonance.yml` | `.github/workflows/visible-larger-public-small-core-resonance.yml` | 15267 / `aba91c0d4e94d8576484fccc4420482a97ace6bd6ed715af67af5861bff89271` |
| `public-small-core-resonance-request.json` | `topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json` | 19213 / `016ee1e1bd39bceb8b498de32f69a564c6f66d10cc8886635d9465a9cd772e54` |

只更新这一个既有workflow及其原computations request trigger，不新建第二派发入口。原单job、60分钟job预算、45分钟科学预算、concurrency、单线程BLAS、Python3.12.14/numpy2.3.5/scipy1.17.0/python-flint0.9.0及全部action pins保持。

`2026-11-15-request90-workflow-from-actual87.diff` 完整列出request90号、真实87父公开路径/字节/SHA/参数literal、当前η0.01、身份副本名称和显示文字；公共恢复、科学通用调用正文、readback、artifact及publisher不变。`2026-11-15-request90-request-from-actual87.diff` 完整列出父tuple、参数、η、真实算法范围和当前元数据；不保留父publisher失败等不适用于87的陈旧文字。`2026-11-15-request90-workflow-explicit-replacements.json` 保留10组明确替换及出现次数。历史87报告本身不修改。

## 6. 静态检查与交付

`2026-11-15-request90-static-check.json`：34214 B / `39648be5da2ee3a57e6d983d7b20f46ed59c84732bc7c719614e5c3087e50bf1`。

116项仅源与字节检查全部通过：

- 实际87 baseline request/workflow SHA；父完整54279 B、SHA、schema、三参数bits、11消费源及四输入对应。
- 70源逐文件SHA；Python只AST解析，无科学模块导入、数值fixture或科学调用。
- 7段shell仅 `bash -n`；4段inline Python仅AST。参数dict、父tuple、三源chain由AST literal与request核对。
- 原own-schema允许独立当前正η；父η仅保来源，当前/父阻尼元数据明确不同。
- 新旧diagnostic除了初值literal和η逐值相同；direction model除了η字段逐值相同。全部原预算、科学源和最终检查保持。
- 真87八次全步/零拒绝作为动因；无未来run、下降、根、非零parent或BVP成功声明。

全部草稿、baseline、完整diff、checker和冻结清单仅在 `/tmp/visible-larger-request90/`。本地没有执行SVD、norm/dot、模型、Jacobian、FD、Arb或候选搜索。主控可按原规矩审读后唯一发布；实际90结果仍须以其Actions原回执判断。

## Root实际接线

主控已完整读本接口及两diff，独立核70冻结源/7shell/4inline/原87父完整status和参数IEEE；父η只作来源、当前η独立正值路径由原AST确认。124项纯静态回执 `2026-11-15-request90-root-static-check.json` 为24188B / 4de44ac3b1da946e4b1292a15cadeabf9550e3601d599289154df5874266ca0e。原workflow/request冻结字节保持，只将本接口伴随链接改为唯一公开名称并补实际接线；未来90结果未填写。
