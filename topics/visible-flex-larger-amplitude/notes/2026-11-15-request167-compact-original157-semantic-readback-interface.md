# Request167：读取实际163语义日志中的157必要原字段

作者：ChatGPT /root/amplitude；2026-11-15。独立元数据入口，无科学执行、无新候选门、无未来run身份。R340保留其历史读取范围；本请求只补其尚未独立读到的原FD、全九维矩阵、终态模型和真实试探。

## 1. 唯一输入与来源

本次只下载已成功163的 read157 job `132868510914` 日志一次。固定run `43732715988`、source `4e1decc718c712b2eaa26a7da598d89236a21ef0`、attempt1、report `132868952547`；均必须官方metadata终态success。读取163原request/reader/workflow的固定小源码，核完整bytes/SHA。原151日志、原157 compute日志和原科学artifact均不重新下载。

原163已完成的157索引62991 B / `16a65e9d484cd0368d135af71ac6b90e0889cba567e5750a7fc05f5dd7cadf25`；其完整语义索引184436 B / `af7100596ea068ec0d194203a2724d8ba1dafb0c6443e03c6b3b31037554936a`。167在新日志里逐字核这两身份、全部begin/part/end及完整原descriptor列表。不是仅接受日志文本自称success。

所承接的原科学仍是157 run `43729310294` / source `c71cbeac7fd13c65cf50c7eb39842e9949737b25`；compute `132858021333`、report `132861152631`。原status51842612 B / `931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0`；完整view51846160 B / `82cf345fc42d371eb4adf69e78944a35fce88b3d9503407ec7dff2f25ee8e76a`；primary89063 B / `7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2`；chain29684 B / `9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd`。这些身份必须与163原完整收据一致。没有重新生成或重新序列化原科学status。

## 2. 正式新增文件

仓库题目录前缀为 `topics/visible-flex-larger-amplitude/`。

| 文件 | B | SHA256 |
|---|---:|---|
| computations/root_20261115_existing163_157_compact_semantic_readback.py | 48367 | `5610208579582ced4ab9f27d5466195bdfae081ed451cfb66cf7899f9d33d379` |
| computations/public-existing163-157-compact-semantic-request.json | 14702 | `dcd09ad515645c4f90dae169e74243f86a9764f5ee3de00950177413d01741fe` |
| .github/workflows/visible-larger-public-existing163-157-compact-semantic-readback.yml（仓库根） | 18157 | `37c2aed87212a0a41c4b2bf4f72e2a4b6b0b9d85909c2be66e8969a2ab5c5d6a` |

原 `root_20261115_existing151_157_log_readback.py` 保77301 B / `ecb77c7e4aae0b7888c58c753ca74d49f0528db3f743443582c3bc4503853250`。新源只导入这个经过hash核的**元数据工具**，复用原opaque numeric lexeme、官方网络、无凭据跳转、严格JSON和字节函数。没有导入任何科学源；实际来源报告明确这一元数据模块已导入，不沿用“源未导入”的错误文字。

## 3. 实际输出字段

### 3.1 初末FD及原状态

完整保留六组各27项检查，共162项：初末原binary64投影的一阶FD、初末持久Decimal50一阶FD、初末Decimal50全九轴二阶FD。逐项保原axis/parameter/step、valid/attempted/complete、relative_error、exception/error/traceback；持久一阶保原正负三残差和三行差分；二阶保原正负三残差与完整3×9 `actual_column_difference`。各level原max-error/valid等照抄，不在读者中重新取max、做差或判断误差是否可接受。

大扰动参数、正负完整3×9响应、对应full112响应表等只保原完整check的bytes/SHA和明确未重印字段列表。原二阶H本身另完整输出，不能把这些覆盖记录说成全部扰动矩阵均已独立逐值读到。初末状态保原三残差、112行线性右残差、112项线性H、3×9原J、三模Robin两项、原域余量及原准确性限制。原binary64投影点/参数词与持久点分开。

### 3.2 八个外方向的完整九维矩阵

每个原outer保原参数、三残差、轴J、半径、实际路径/接受及radius更新。其direction model完整保：

- 原完整3×9的second-forward J；
- 原完整3×9×9的三残差H；
- 原first-forward轴J及second-minus-first原差；
- 原九分量gradient、九个相对参数尺度；
- 选择的原模型点/三残差/merit/预测、九物理方向；
- 原直接方向响应、轴形成响应、二者差和原全三slope；
- 模型预算停止、所有未访后缀、原有限工作计数。

读者对初末及八方向上述必需矩阵做原JSON字段存在和完整维度校验；缺键不能由软selected略过后标complete。这里只核结构，不核范数、有限性或任何科学阈值。没有用矩阵乘法重建缺失字段。scaled H等重复大字段明确留原group身份；不能据此把舍入后的scaled数组冒成重新形成的原word。

### 3.3 八个内部模型的最后终态

每个原32次更新中的最后一条，保完整3×9 model K、九gradient、9×9 model Hessian、完整三模型残差、merit、当前九坐标/半径、选中动作/shift、radius controller、失败/未访原因。

原完整残差GN预条件器保12项augmented RHS、九solution、12项原QR线性残差、九项stationarity、九column permutation、上三角对角、ridge及原Q/R/augmented矩阵身份。GN若原本未返回solution，必须有其原exception或reason，单独标明original_GN_QR_solve_recorded=false；若返回solution，完整9解、12 RHS/原QR残差、9stationarity/排列/对角均须原字段存在且shape正确。原spectral diagonal及方法/限制字段照抄；大Q矩阵和中间shift史只保原identity。原fallback方向额外收集完整QR残差、列排列和对角字段，保实际直接响应、basis响应及stationarity；不假称fallback与主polynomial是同一路径。

每个outer的原全部32个update coverage都读到并计数，21槽/candidate的原异常行完整保留；不搬回256条内部更新的全部数值表，也不重新判断哪一点最优。

### 3.4 全部84次真实试探

原各outer试探数必须为 `[1,1,1,20,20,20,20,1]`。每次保原outer/trial/path/alpha、accepted、原Armijo bound、actual merit、真实三残差、预测及真实-minus-model差、原reason/exception、normal停止/target flag/returned error/三残差、真实evaluation次数、内部工作计数、same-trace选择与原错误。

四个accepted点的九参数/实际九位移保原词。被拒点的全部九参数、各次完整112向量及大normal中间表不重新印满；它们保该完整原trial的bytes/SHA并明确覆盖范围。所有84行均保留，不按“有改善”过滤或遗漏失败。矩阵/末点/接受门结论不从缺失数值推定。

## 4. 不算数学的紧凑表示

原科学数字由 frozen163 的 `RawNumber` 保存其JSON lexeme；Decimal字符串也原样保留。没有 `float`、Decimal科学算术、norm、rank、Jacobian、FD、矩阵action或优化。

完整选中矩阵可以在不同原字段中重复。新传输只在**canonical ASCII JSON字节完全相等**时共用一次完整数组；hash仅作查找，实际还比较原字节。输出单键引用：

```json
{"request167_exact_array_ref":"array-0000"}
```

相应 `complete-exact-array-0000` section给完整原value、bytes、SHA。恢复时先核所有数组，再在所有选中字段的准确JSON路径替换该引用。没有近似相等、重排序、求和、乘法、裁切或数值舍入。并非通过公式补回一个未保存的矩阵。

这是必要科学字段的可逆传输，不是把51MB全view机械切块。原巨大内部/扰动表仍仅有明确identity/coverage。

## 5. 五个报告与严格预算

新read job只生成五个完整named-section packet，每个ASCII≤76000 B；另有完整index≤18000 B。合计ASCII必须≤400000 B。GitHub按UTF16计算job outputs，因此这组上限同时留在原1MiB job-output界限内；无额外artifact。

每个section为一个完整语义对象，最大对象不能装入时明确失败。完整数组单独section，跨报告用上一节明确引用；没有以数值变化或“最后若干行”缩减。按完整section大小作纯整数字节装箱，固定五槽，报告不混入新科学。

六个独立report jobs分别只印一个packet或index，核compute输出的完整bytes/SHA，原文不重新json.dumps。标签为 `BEGIN_REQUEST167_PART_0` … `PART_4` 及 `BEGIN_REQUEST167_INDEX`。各报告缺失时明确 `selected-packet-unavailable`，不能把空报告冒完成。

如选择结果过大，异常index保**全部section的名称/实际字节数**、具体错误和完整traceback，complete=false/exit70。超大index的全文只在compute日志按元数据原ASCII块无损输出；report保其身份和未完成范围，绝不删字段后标complete。部分成功packets与读取层失败不改变原157科学结论。

## 6. 官方网络、生命周期与规则

固定源/请求核验后，通过官方REST读取163的run/job/report元数据；只GET，不改repo、workflow或任何ref。对官方job-log跳转，新的HTTPS请求不转发Authorization/Cookie，不打印签名URL或token。新代码不猜私有端点；没有查询日志分片的未授权API。

运行命令：

```sh
python -u computations/root_20261115_existing163_157_compact_semantic_readback.py \
  --request computations/public-existing163-157-compact-semantic-request.json \
  --request-sha256 dcd09ad515645c4f90dae169e74243f86a9764f5ee3de00950177413d01741fe \
  --out "$RUNNER_TEMP/visible-existing163157-$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT"
```

目录必须是本run专有、此前不存在的RUNNER_TEMP直系子目录。原日志一次下载到此处；完整字节身份和协议核对完成后，只清理这棵自建日志目录。finally保cleanup真实错误；workflow always再检查本run目录属主/regular file并清理未删原件。没有删科学源或父输入。

Python3.12.14，仅stdlib和冻结元数据helper；没有numpy/scipy/Flint/public78或科学包安装。read job最多35分钟、读步骤30分钟，低于原2700秒规则监控周期；开头核实际checkout的根/题README精确blob，未修改原规则监控参数。根21bd547f…、题bff8aea…不符就停止元数据入口并读新规则，不绕过。

所有report均permissions={}；read仅contents:read/actions:read。唯一push trigger是本新request path，cancel-in-progress=false；未创建当前run或未来run号码。

## 7. 静态来源与后续责任

这套交付在终端不可用时以小文本构造、逐字段检查、JSON解析、字节/SHA核对和完整source责任完成；未声称本地Python AST、YAML执行、网络SDK运行或数值fixture通过。旧163和157科学字节不改。主控唯一发布和实际调度。

实际167完成后，先读取小index与五份packet，按原字节恢复必要数组，再完成R350对原157科学机制的新增读数。这里尚未获得157原FD误差、terminal gradient/H或真实内部异常的新增值，不提前写“驻点”“秩亏”或“已证精度”。R351伴随helper和新C²零jet控制作为另一个来源明确的后继；本日志读回不是它的新增科学接受门。

## 8. 首跑真实读取层失败及本版最小修复

首跑run43735131654/source e5dd9ff898b62a85b9f3d98fdc98db4f91201e0d，read job132875931222在最终index编码处failure。官方已一次下载163语义日志8265333 B / caa25be9f57c9d69e3ab8e1764d4ef4431eacbfd40726953df76803dcdafb160；原157科学未执行。实际compute日志29026 B / d10df854ab0becb8b29fcf006b2c8fac13e76b73a43d6c1a45b020e4da92fd9c显示 frozen encoder 拒绝 Non-string JSON metadata key，指向新 summary.selection_scope.internal_coverage 的整数outer键。原完整报告没有输出，不能据此认定FD/矩阵已由root读到。

本版只把该输出字典的outer键明确转成字符串，另在最后metadata编码异常时保具体原错误、完整traceback和已有输入/清理身份为小failure index。所有原字段选择、必需matrix shape、预算、协议和科学来源不变；下一个实际元数据run仍只读同一已成功163日志一次，不重157科学。没有把先前缺失summary伪造恢复。
