# Request 87：从真实85候选以同 η=0.1 续一次原八步预算

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：独立工作流与来源接线草稿；仅源文本、原JSON与文件字节操作。** 本次没有修改科学源码，没有本地数学导入或运算，没有修改仓库、提交、派发或填写未来run。主控负责唯一发布和实际Actions运行。

## 1. 已有证据与本次选择

[实际85正式结论](2026-11-15-actual-request85-damped-resume-eight-full-steps-publication-limit.md) 完整读回了八次原方向与试步。八次均在首个 `alpha=1` 接受，没有拒绝、域失败或回溯截断。原保存的merit为 `11949245423.478903 → 11479182858.417969`，末单位缺陷为 `[227.29559514822407,-151517.87117025955,805.4623398988991]`；分量并非同时改善。`diagnostic_completed=true`，但 `success=false`、原小残差候选标志false，仍没有共振根或非零幅度parent。

87仅从85末参数重新评价原模型，继续同 `eta=0.1`、最多八个方向、每方向原20档回溯。本轮记录支持保留这些算法参数；它没有提供下一轮下降或收敛保证。所有新方向、参数Jacobian、真实斜率、merit和域读数仍在公开Actions内重新计算，不能把85原模型数值改名为本轮数值。

85的科学步骤、原状态只读步骤和artifact保存均成功，随后的publisher在 `2026-11-15T02:25:09Z` 抛出：

```text
RuntimeError: Preserve a unique rule-read line and the original HANDOFF size bound
```

这是原publisher的HANDOFF大小检查失败。主控负责缩短HANDOFF并按原字节恢复85的11件原输出；本草稿不修改publisher、它的大小门或科学准则，也不为出版重跑85科学。以下公开父路径需要由主控在同一发布或先行发布中恢复。此文不提前宣称恢复已经完成。

## 2. 真实父状态与冻结入口

原85运行身份：run `43667636063`，source `c9daab1a9f7b1330c6099450bd018bfab9026b0d`，job `132670464205`；artifact `14143056682`，268505 B，ZIP SHA `708ce51fb634552d376013d05b57e4f42cdc07d699e25753a2af0a2ea36e5775`。

唯一父状态：

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43667636063-1-smallcoreresonance/small-core-damped-resume/damped-resume-status.json
54251 B
SHA256 72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a
```

只复用其中 `final.parameters` 的完整原值；草稿与原文件逐binary64位对应：

```json
[0.06389479553738595, -0.012958081345244933, -0.11220747933971734]
```

科学入口、原方向函数及原模型不变：

| 角色 | 文件 | 原SHA256 |
|---|---|---|
| 同schema续接，15452 B | `geometry_20261115_small_core_damped_resume.py` | `ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a` |
| 原正阻尼方向，13733 B | `geometry_20261115_small_core_damped_search.py` | `1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728` |
| 原三方程及最终检查，25799 B | `geometry_20261114_small_core_resonance.py` | `3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5` |

入口已有自身schema `R259-original-three-equation-column-scaled-LM-resume-v1` 的合法续接分支。它仍核真实父字节、完整11消费源集合、ec9/1691/3b9、四原数学输入及父诊断范围。没有替换父schema、绕过原guard或建立新科学gate。

全部70个源pin、四原输入、runtime与原public78恢复过程均逐值保持85。publisher仍为 `root_20261114_publish_actions.py` / `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca`。

## 3. 原调用、检查与输出

原单一科学step的run正文与实际85逐字相同，只有显示标签改变。该正文读取新request，调用一次原入口：

```text
python -u geometry_20261115_small_core_damped_resume.py
  --accepted <原accepted96，完整路径/bytes/SHA在request>
  --prepared <原prepared112，完整路径/bytes/SHA在request>
  --tail-anchor <原真实T112零锚，完整路径/bytes/SHA在request>
  --tail-config <原T112配置，完整路径/bytes/SHA在request>
  --parent-status <上述85完整状态路径>
  --parent-status-sha256 72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a
  --damping 0.1
  --candidate-steps 8
  --backtracks 20
  --candidate-resonance-tolerance 1e-08
  --interval-bits 160
  --interval-depth 14
  --out "$VISIBLE_OUT/small-core-damped-resume"
```

尖括号仅为接口说明。`source-only-static-check.json.actual_command_shape` 保留所有实际CLI路径与参数，工作流不传入占位符。

原未加权三方程、三列完整Jacobian、列规范化6×3正阻尼方向、恢复后的实际 `r dot (J d)`、原0.2 Armijo系数、20档 `1…2^-19`、原参数域异常与merit接受规则均不变。最终参数FD、160位/14深度Arb及完整699节点zero-core circle仍由原函数执行。η是方向算法参数，没有加到原非线性方程中；设计参数变化也不冒固定同一个g的精化。

所有112×112真实零锚斜率J的条目仍读取，不能阈值化掉非对角项或换为ready代理；原完整112右残差仍输出。本诊断本身没有计算高109自由core的Schur或证明非共振。其他参数点的高块结果、实际81的Arb结论或非零parent均不继承到本轮。Arb标量检查的范围仍是声明实表达式的a/ap，不是整段有限场/BVP证书。

输出目录仍为 `small-core-damped-resume/`，原状态文件和schema不变。预运行来源副本名称为 `prior-candidate/actual85-damped-resume-status.json`，来源账名称为 `request87-input-and-source-identity.json`。原readback、完整artifact保存和publisher步骤正文逐字保留；它们如实保留科学失败或未接受候选。

## 4. 唯一触发与完整差异

只有以下两件进入已有目标；没有第二workflow、第二request或额外dispatch：

| 草稿basename | 既有仓库目标 | 字节 / SHA256 |
|---|---|---|
| `visible-larger-public-small-core-resonance.yml` | `.github/workflows/visible-larger-public-small-core-resonance.yml` | 15232 / `c9ba367f40b9dd8de04ed4af9783efc4609ce39ab7a616467bba24fe659313d8` |
| `public-small-core-resonance-request.json` | `topics/visible-flex-larger-amplitude/computations/public-small-core-resonance-request.json` | 19239 / `5863a5b991149d5e04a4b5ddd903a52fffe03d26e3d6cbd416435cefa92aa3d0` |

原push trigger仍是上述computations request路径。原单job、concurrency、60分钟job预算、45分钟科学step预算、runtime、单线程BLAS及全部action pins不变。

完整差异在同目录：

- `2026-11-15-request87-workflow-from-actual85.diff`：request87号、真实85父路径/54251B/SHA/初值literal、来源副本与显示标签；原数学调用正文不变。
- `2026-11-15-request87-request-from-actual85.diff`：真实85父tuple、参数、87号/时间/动因与科学成功阶段和publisher失败的独立元数据；70源、runtime、四输入、sourcechain、proofs、direction model、其余诊断预算不变。
- `2026-11-15-request87-workflow-explicit-replacements.json`：7组明确文本替换和实际出现次数。

历史父85文件本身不重写。新request以同源自身续接身份描述本轮，不把85旧初值覆盖到原报告或把85成功阶段冒作科学根。

## 5. 静态回执与交付范围

`2026-11-15-request87-static-check.json`：33234 B / `8f7f183336c412429798d6747a5d59475b62900819e2f68857ad313587c64a82`。

107项检查通过，具体范围是原JSON/bytes与源布局：

- baseline85 request原SHA与已执行身份一致；新父完整54251B、SHA、schema、三参数bits和11消费源集合一致。
- 70源逐文件SHA核对，Python源码只AST解析；没有数学模块import或fixture。
- 7段shell仅 `bash -n`，4段inline Python仅AST；三来源chain、参数dict及父tuple均由AST literal读取并与新request逐值核对。
- 科学调用run正文及timeout、原四输入、runtime、原public78恢复、readback、artifact及publisher与85相同。
- 原科学成功阶段和publisher失败元数据分开；无未来run、下降、共振或已接受非零场声明。

完整draft、原baseline、副本、diff、静态回执和冻结清单均仅保存在 `/tmp/visible-larger-request87/`。主控可正常Git同步、恢复父原件并唯一发布；真正87结果需等Actions原读数再判断。

## Root实际接线记录

主控已恢复实际85全部11原件原字节，保存完整结论和出版恢复回执；未重跑85科学。两diff及本接口已全文读，另独立核70原源/7shell/4inline/真实父完整JSON与参数IEEE，见 `2026-11-15-request87-root-static-check.json`（21789B / e5030f3c3b420357a930f430a4890aaeda42925730e0986632dab3a2071feb73）。上述workflow/request原冻结字节未改，本接口仅将伴随文件接至唯一公开名称并补此实际记录。87未来实际结果尚未产生。
