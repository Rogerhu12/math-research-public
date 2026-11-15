# Request 88：只消费真实85已保存方向的独立谱诊断接线

日期：2026-11-15。作者：ChatGPT / amplitude。

**分类：独立Actions工作流与来源接线。** 本次只写`/tmp`草稿并做源/字节/语法检查；没有修改仓库、分支、科学源码，没有派发或本地数值执行。实际SVD、残差投影和滤波预测只能在本公开仓库Actions内运行。它不增加候选、BVP或后继任务的科学接受门。

## 1. 唯一消费者及明确范围

本请求只运行已经冻结的 [saved85消费者接口](2026-11-15-saved85-small-direction-spectrum-interface.md) 所述入口：

```text
geometry_20261115_saved85_direction_spectrum.py
21290 B
SHA256 20fcaa266aa1716be9ab910d2ab988d2259dc56e013b13d3cedccd69be9a9d20
```

它读取实际85完整状态中的八组原`r/J/D/A/z/d/Jd`与原trial/下一残差，对每一组保存的3×3列缩放矩阵A直接做SVD，输出残差在奇异方向上的投影、原已存方向的一致性读数，以及显式η=0.01和0.001的该局部线性模型预测。原η=0.1的读回同场保留。它不通过增广奇异值平方减去η平方来推断弱奇异值。

八次迭代分别有自己的保存模型，不能把八组当成一个固定A。新预测不求原RHS/J、不恢复场或尾端、不执行FD、Arb、候选搜索或非线性trial；不修改85已发生的接受决策，也不说明较小η实际可接受。直接浮点SVD不是严格秩或横截性证书。

本次不包含另一位代理的边界/项目化消费者，不等待该消费者、87/90后继或原生尾端成功锚。只有这一个独立保存数据分析入口。

## 2. 真实输入与13源闭包

唯一数学数据payload是以下已经恢复公开的原85状态：

```text
topics/visible-flex-larger-amplitude/notes/public-actions-43667636063-1-smallcoreresonance/small-core-damped-resume/damped-resume-status.json
54251 B
SHA256 72397df159924d54bfcf7892b0f22d0a6b9e796238b5d29f8802e22120fb1a0a
```

原运行run`43667636063`、source`c9daab1a9f7b1330c6099450bd018bfab9026b0d`、job`132670464205`；artifact`14143056682`，268505 B，ZIP`708ce51fb634552d376013d05b57e4f42cdc07d699e25753a2af0a2ea36e5775`。这些是原85来源，绝不填作本次88未来运行身份。本工作流不重新下载该ZIP。

85科学、原readback、artifact保存成功，随后publisher因HANDOFF大小界限失败；主控已恢复原字节供公开消费。本次不为出版问题重跑85科学。原状态仍`diagnostic_completed=true`、`success=false`，不是非零parent。

13个源pin精确由三部分组成：原状态`consumed_source_sha256`中的全部11个源码payload、新20fc消费者、原22e publisher。全部SHA在request和PYPINS硬编码字典逐项一致。11源只读取字节、校SHA、编译语法，不导入或执行原数学模块；所以无须恢复它们的运行时依赖树或78公共源。

| 来源角色 | 文件或范围 | 核对方式 |
|---|---|---|
| 原85完整消费源 | ec9 resume、1691方向、3b9模型及原8个数学辅助，共11源 | 与原状态完整集合相等，逐文件SHA；不数学导入 |
| 本次保存数据消费者 | `geometry_20261115_saved85_direction_spectrum.py` | 原20fc完整SHA |
| 原出版器 | `root_20261114_publish_actions.py` | `22e640bb764936215e0bf0d2a4cefcb69808e27b2c81cf0c6b94a751a1e5b9ca` |

四个大数学input只保留原状态的来源回执：

| 原input | 原SHA256 |
|---|---|
| accepted | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| prepared | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |
| tail_anchor | `e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51` |
| tail_config | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |

这些四个payload不checkout、不下载、不重新读入，也不冒再次字节审计。工作流sparse范围只含13源、该请求、原54251 B状态、双README及HANDOFF。

## 3. 唯一工作流、原运行时与CLI

新工作流文件：`.github/workflows/visible-larger-public-saved85-direction-spectrum.yml`。唯一push trigger：

```text
topics/visible-flex-larger-amplitude/computations/public-saved85-direction-spectrum-request.json
```

仅一个`modelresponse` job，没有workflow_dispatch、矩阵或第二科学调用；出版复用既有`modelresponse` lane，新job concurrency group为`visible-larger-public-saved85-direction-spectrum`，不取消正在运行的任务。

Python固定3.12.14，仅安装`numpy==2.3.5`。OpenBLAS/OMP/MKL均单线程。无SciPy、python-flint、Node、公共78恢复、native worker、网络artifact读取器或新候选solver。原11源的依赖不会因语法compile被导入。

job资源预算15分钟，唯一消费者step预算5分钟；这是小诊断资源预算，不是新数学容差。checkout/setup-python/upload-artifact仍用已采用的完整action commit pins。

实际调用只一次：

```text
python -u computations/geometry_20261115_saved85_direction_spectrum.py
  --status <上述真实85完整公开状态路径>
  --comparison-damping 0.01 0.001
  --out "$VISIBLE_OUT/saved85-direction-spectrum"
```

尖括号只用于接口说明。request及静态回执`exact_command_shape`保真实完整状态路径，工作流按`GITHUB_WORKSPACE`补绝对路径。wrapper不提前创建消费者子目录，保留20fc原fresh-output契约；只先建立外层输出根。

PYPINS核request88/13源/原status/input回执、触发HEAD与`GITHUB_SHA`，记录触发checkout双README blob。`request88-input-and-source-identity.json`在try/finally中保存，来源错误原样抛出并保error/traceback。消费者原exit code透传，不能用continue-on-error把失败当分析完成。

## 4. 输出、失败保全与普通出版

外层输出根为`$RUNNER_TEMP/visible-saved85-direction-spectrum/modelresponse/`。其中：

- `request88-input-and-source-identity.json`：请求原SHA、真实触发source、13源/原状态、旧input回执与来源范围。
- `numpy-install.log`、`saved85-direction-spectrum-command.json`、`saved85-direction-spectrum.log`：实际安装和唯一命令/返回码，不含凭据。
- `saved85-direction-spectrum/actual85-original-status.json`：原54251 B状态字节副本。
- `saved85-direction-spectrum/saved-direction-summary.json`：消费者原小摘要，schema为`R259-saved-actual85-three-by-three-direction-spectrum-v1`。
- `saved85-direction-spectrum/large-arrays/saved-direction-analysis.json`：八组完整分析、保存数组语义、所有预测及数值读回；只留完整artifact，由摘要descriptor绑定。
- 若消费者异常，其原`phase/error/traceback`、`saved-direction-error.txt`及已经完成的rows仍由原finally保全。
- `saved85-direction-spectrum-readback.json`：仅复制原summary选择字段/原SHA和rows数，不再进行数组运算，也不重判接受。

readback、完整upload和publisher都`if: always()`。readback仅报告其自己的缺失或解析异常，不替代消费者原失败。artifact仍命名`visible-mainline-modelresponse-<真实run>-<attempt>`，完整外层目录、compression-level1、保留30天。此处名称中的run由Actions生成，本稿不假定。

原22e publisher在上传后执行：

```text
python -u "$VISIBLE_COMPUTATIONS/root_20261114_publish_actions.py"
  --results "$VISIBLE_OUT" --lane modelresponse
```

它按原规则保bounded公开原件，`large-arrays`完整分析留artifact，public manifest记录其原文件SHA。公开目录仍`notes/public-actions-<真实run>-<attempt>-modelresponse/`。它实际普通`git pull --rebase`后核双README并更新规则读取记录，非快进按原逻辑重试；不修改publisher、大小界限或科学准则。publisher若失败，已经上传的完整诊断与失败证据仍在。

## 5. 冻结交付与仅静态核验

| 文件 | 字节 / SHA256 |
|---|---|
| `visible-larger-public-saved85-direction-spectrum.yml` | 14642 / `bc23829b3a090c999ecb604141fab67a74e900facb59a7087e5543ec9bcaaf86` |
| `public-saved85-direction-spectrum-request.json` | 7065 / `548ad1625e842b55245028fbac27b606634c1f0c7633c1d79be40004bb3c4eb9` |
| `request88-source-only-static-check.json` | 15190 / `12bfa21a48581e77af8e98450919728c383275f7086acf25ab3a179ca14c1f7c` |

两个新文件的完整`/dev/null` diff同目录，builder/checker/原modelresponse83工作流参考与冻结清单亦保留。原83或任何既有workflow/request均未修改。

静态回执58项通过：13源SHA和AST；原85完整54251 B/SHA/schema/11源集合；四input回执对应；唯一trigger/job/CLI；6段shell只`bash -n`；3段inline Python只AST；所有JSON输出后缀是实际换行，失败finally与原exit code路径明确。消费者AST只含stdlib和NumPy导入，Actions环境guard在NumPy导入与算术之前。

该静态检查没有导入消费者或原数学模块，没有执行SVD、dot/norm、矩阵、模型、RHS/J、FD、Arb或优化器。它只是交付接线核对，不成为另一个科学验收门。真正88分析结果须等待主控唯一派发后的原Actions回执。

## 主控发布接线

源码、workflow和request均保上表原字节；原`request88-source-only-static-check.json`保存为[唯一工作流静态回执](2026-11-15-request88-source-only-static-check.json)。主控已完整阅读源码、两个接口和完整工作流／请求，独立31项、13pins、6shell及3inline AST核对保于[主控回执](2026-11-15-request88-root-static-check.json)。[草稿冻结清单](2026-11-15-request88-draft-frozen-files.json)保原接口SHA；本节只是发布路径映射，不执行科学或预写结果。
