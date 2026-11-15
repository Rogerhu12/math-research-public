# Request 138：同一实际 134 起点的完整 normal 轨迹原 merit 选择

作者：OpenAI ChatGPT（amplitude agent）；日期：2026-11-15。

**分类：独立算法源码与可执行接口；没有本次实际数值结果。** 本请求只实现 [R299 同轨迹有限候选选择](../results/R299-same-normal-trace-full-merit-selection.md)，不更改已完成的 135。135 的实际结果及真正末点、末半径见 [R301](../results/R301-actual135-carried-radius-thirty-two-batches.md)。本文件不占用新的结果编号。

## 1. 真实起点与比较口径

138 从与 135 完全相同的**实际 134 第 32 批末参数与半径**开始，随后每批携带本次真正保存的末半径。它不是从 135 最后点继续，不把旧状态、Jacobian、merit、FD 或域证书改名为新计算。

直接复用已公开的小配方：

- 路径：`computations/actual134-final-batch-nine-control-carried-radius-recipe.json`。
- 原公开提交：`41ef8d7de1843bd8c831eb9d9166673bb552409c`；Git blob：`0d85005b3dc07f4bf06d45a141468fdfa9d0e846`。
- 2,407 B；SHA256 `494f73d108669feb547e26dabef6c71ef589cfae149611163453a86b98c45151`。
- 真实来源：134 run `43704292938`，source `19911f56968ad3581636e77d240c4d5e9064645f`，第 32 批。
- 原 status：6,525,034 B，SHA256 `14308777d3f7440e6aa3a1054022800a0800b73c6e51ab6123bc350b92bcba24`。
- 原 primary：62,594 B，SHA256 `7f732c5d4980b1a273682f56ca19de74721797101dbff36a5c5be795eef21fb5`。

九参数按原顺序 $[p_1,p_2,p_3,\theta_1,\theta_2,\theta_3,\eta_1,\eta_2,\eta_3]$：

```json
[0.3055203761844937,0.21645138982853507,0.3426956535903166,-0.06322286579803658,-0.017473800295252997,0.9376133742168962,1.075134071398223,0.6887022298418047,0.9385918098098012]
```

初始相对半径是原保存值 **0.000390625**。两个入口都将这组参数重新 evaluate、description、形成完整 $3\times9$ J；共同配方不等于不同运行的全部有限矩阵必然逐位相同。首次方向可以根据原保存的 initial J、direction、frame、merit 和原数值身份直接比较。若本次选择了不同接受点，后面的模型与轨迹便不再是同点比较。

这里消费的是已公开的参数配方与原文件身份。未重新取得或伪造已删除的 134/135 raw status。父 status/primary 的 SHA 是出处；它们不被当作本次状态缓存。

## 2. 五个独立执行／接线文件

| 文件（均置于本题 computations，workflow 除外） | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261115_small_core_nine_control_same_trace_merit_recipe.py` | 50825 | `e8704af6daa13eac4d0301a6ef1debdca4c9cb0b10a806544644a2e1d162329a` |
| `root_20261115_small_core_nine_control_same_trace_merit_scalar_readout.py` | 32682 | `4973404938189fc37b8563508da7212959a34d1527abd1c5910f717f27e504cd` |
| `geometry_20261115_nine_control_same_trace_merit_temporary_batches.py` | 55234 | `79c178f4ea76880e0a1cc01ead06cf95fb0e98e74f8f6b8dacedfa98b5f95ad6` |
| `public-nine-control-same-trace-merit-request.json` | 52545 | `1f203c07b9d6780acdc1e9422fb48840d1579dda735b10cc9947eea6cf914ea4` |
| `.github/workflows/visible-larger-public-nine-control-same-trace-merit.yml` | 21180 | `2effcf049445664a0b164876f9df0934d592015fe961b7a01d7e6e80b01c3d30` |

调用已经独立发布的 R299 helper：

`geometry_20261115_nine_control_same_trace_full_merit_candidate.py`，19,265 B，SHA256 `d4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf`。

本次不改这个 helper，也不改原 824c 九族 producer、ed786 的 135 producer、原 f57/24c5 reader、原 fd5/df85 wrappers 或 family0865。

## 3. 唯一候选算法变化

新 producer 从已冻结 135 文本建立：

1. `norm`、`full3_trust_direction`、`next_radius`、`full_column_qr_solve`、`curve_frame` 五函数原正文保持。
2. 完整八方向 outer 循环及其 20 档回溯、fresh accepted-point J、原半径更新、整方向拒绝后的 quarter 均原正文保持。
3. final、except、finally 尾部原正文保持：初末九列三档 FD、完整 scalar Arb、固定六个新增 shape 的原 453 圆检查、所有 unit/full112/native/nonzero/success 责任不变。
4. 旧 `curved_candidate` 定义由一个有明确 source pin 的 helper 加载槽取代。main 在 Actions/source 绑定后把本次局部名字 `curved_candidate` 绑定到 helper 的同签名函数。没有修改或调用旧 producer 的 main。

该 helper 先完成原工作路径，再决定返回哪个已评估状态。它从零 normal 坐标出发，继续执行原每次 fresh full J、完整 $2\times2$ QR、inner merit 回溯、域失败和停止规则。shadow bookkeeping 不修改工作状态、normal 坐标、原试探或回溯判断。

有限候选集合包含已有成功评价的 seed、每次当前工作点、每个成功评价的 normal trial（包括被 inner Armijo 拒绝者）和原工作返回。只对原已经计算并保存的完整三方程 merit 作有限数比较；原工作返回在相等时优先。若选择严格更小者，保留其完整状态副本，返回其真实参数、三残差及完整112相关数组。后续 J 由原代码在该真正接受点重新计算。

**选择不等于接受。** outer 原代码再次计算该返回状态的原完整 merit，用原
$W(p)+0.2\alpha\,r^\mathsf TJv$
作接受判据。内层目标误差仍不是外层接受门；不会将真实残差替换为目标值或置零。

特别保留：

- 原直接 seed 失域时，该 alpha 按原失败结束；不从不可达 shadow 候选恢复。
- 原工作调用未完成／异常时，不以曾有好点为由制造成功。
- 没有有限可选 merit 时保留原工作返回，交原 outer 判断。
- 只在原调用真正完成后才选择；不会提前退出 normal 循环以减少原预算。
- 选择中增加的完整状态复制或记录若发生资源异常，如实失败，不声称已完成。
- alpha 恰为零时保留原无评价返回分支。
- 原工作停止原因另存于 `original_working_trajectory_return`；不能把它错误解释为被选择点自身的求根轨迹。被选点的真实 target error 和 flag 另行按原公式记录。

每个正常调用至多保留 254 个现有 scalar merit 读数位置及一个最佳完整状态副本；没有新增 model.evaluate 或 model.jacobian。若未来候选改变参数，后续调用数和路径当然可能改变，不能声称整个32批运行费用不变。

## 4. 完整 normal 标量读回

旧 reader 的17个 trial 列保持。独立新 reader 增加：

`outer_searches[i].complete_normal_traces[j].complete_original_normal_scalar_record`

该值直接取原 status 中对应的整个 `normal_correction`，包含：

- 全部 normal iterations、各自全部 trials、接受／拒绝原因、原参数、三残差、target error、原 full3 和 inner merit；
- 每个实际 normal J、完整二维 QR scalar 报告、原 slope、更新与停止；
- 所有原 evaluation errors 和 exceptions；
- 原工作返回、全部 selector samples、选择来源、有限数旗标、原保存与读回 merit 词比较；
- 不完整 normal 调用在原 status 中真实留下的记录，不补造其未执行部分。

不再只复制第一／最后异常样本而将中间内容仅以 hash 代替。原完整状态副本、mesh 和矩阵 raw payload 不在日志中重复；这里保留的是原 normal 的完整 JSON 标量记录。没有新 evaluate、J、merit、范数或 FD。

使用原无损结构分段器：每段至多90,000 UTF-8字节，可声明对象／列表及精确子路径、完整子值、连续列表范围或字符串范围。每组 canonical bytes/SHA、每段 bytes/SHA、ordered part-index SHA 和 full view SHA 均保留。输出段是原 scalar 日志协议，不是把 raw 数据拆块提交 Git/Release。

新 schema：

- producer：`R259-nine-control-full-three-two-normal-same-trace-merit-carried-radius-trust-recipe-v1`；
- status：`nine-control-same-trace-merit-carried-radius-status.json`；
- primary：`nine-control-same-trace-merit-carried-radius-full3-curved-trust-segmented-scalar-readback-no-raw-retention-v1`；
- complete view：`nine-control-same-trace-merit-carried-radius-full3-curved-trust-scalar-view-v1`；
- segment：`nine-control-same-trace-merit-carried-radius-complete-direction-scalar-segment-v1`。

段分隔符为 `BEGIN_VISIBLE_NINE_SAME_TRACE_MERIT_<GROUP>_PART_<NNNNN>` 与相应 END。每个 batch 仍有独立 `VISIBLE_NINE_BATCH_XXX_ORIGINAL_READER_STDOUT` 外框及单独 primary，便于完整重建。完整 FD/Arb/circle 若自身超出 primary 预算，可移到有名完整组；不能删掉字段使其假装小于90KB。

结构分段只解决传输大小，不限制 normal 科学调用，也不缩减任何原试探。若完整组索引仍超过90KB，保留已经输出的段并明确 transport incomplete；不得冒 complete summary。完整 normal 记录可能比135显著增大；日志或资源失败须诚实保留，不据此改变原数学门。

## 5. 32批生命周期与停止

独立 wrapper 保留原 `original_stop` 整个函数，未引入“至少下降多少”、最小奇异值、inner tolerance 或 root 接受新门。

每批仍为：

1. 实际短配方给九参数及真实末 radius；
2. 一次独立原8方向／20外回溯／12×20normal child；
3. child 执行原完整 final；
4. 独立 reader 输出完整正常／失败标量；
5. 完整读取新 status 与 primary 的真实身份；
6. 只从该实际结果构造下一 own-schema 小配方；
7. 消费后删除本批 owned 临时原始输出。

原 zero accepted 停止保留：即使最后 radius 变小且能构造出处明确的配方，wrapper 仍停止，不能借 R299 自动重启。原 unit/full112 flag、非预算停止、child/reader exception、资源／规则信号按原规则停止。

最多32个独立批次，3600秒只在完整批次之间检查。不是一个256方向不中断求解器，也不挪用最后批次 final 的时间预算。所有32计划行始终存在，未启动行用 null 明确未评价；启动但未完成的行保留真实例外和已有值。不得从前一批补造成功、参数或清理结果。

下一批只携带真实九参数与 final_relative_trust_radius，包括最后一个完整拒绝方向的 quarter；不 floor、clamp、reset 或 repair。零半径也不伪改，由原正方向规则处理。

## 6. source闭包和历史身份

原135的 **87个源pin + 3个support pin全部保留原值**。本次新增 helper、新 producer、新 wrapper，source合计90；新增完整normal reader，support合计4。

- 首父仍为原824c的26源定义。
- 历史ed786 carried producer定义为27源，只作明确 baseline/source身份；其main不执行。
- 当前 producer定义为29源：原26 + ed786 baseline + R299helper + 本新producer。
- 后续同一新producer的真实status→recipe保own29→29。
- 原b15八批、fd5 reset32、df85 carried32三个wrapper都只保留来源身份，不被偷偷执行。
- 新 reader明示自己的 producer、family和selector源身份，不冒24c5旧reader。

当前入口只接受原824c来源或自己的真实来源。没有把135末状态的 ed786身份改成新source，也没有把135末参数用于当前首次请求。原输入、family及 source集合按代码/请求实际核对；这些是来源接线，不是数值收敛门。

## 7. Actions接线、四输入与清理

独立 push trigger 仅为：

`topics/visible-flex-larger-amplitude/computations/public-nine-control-same-trace-merit-request.json`

工作流为 `.github/workflows/visible-larger-public-nine-control-same-trace-merit.yml`，不改原135 trigger。Python3.12.14、NumPy2.3.5、SciPy1.17.0、python-flint0.9.0及BLAS单线程保持。compute job90分钟，science step75分钟，独立report10分钟，保持135的资源合同。

四个原数学输入保持完整 bytes/SHA，经公开历史提交
`8bd267107cc8710d371f3b62c02986655ac965b0`
暂时恢复到本request的 RUNNER_TEMP；原78source恢复流程不变。旧准备数据不重新入库，本任务不启动native求解。原零H高度J仍只是原模型/圆检查的给定输入，不构成非零native锚。

科学调用形态为：

```text
python -u geometry_20261115_nine_control_same_trace_merit_temporary_batches.py
  --request <本次公开request文件>
  --request-sha256 <该原文件实际SHA>
  --repository-directory <触发checkout>
  --original-input-paths <本request临时四输入路径JSON>
  --rules-directory <本request规则同步目录>
  --out <本request全新temporary-batches目录>
```

wrapper逐批给原child完整四输入／短配方／实际半径及全部原预算，并单独执行当前reader。上面没有未来run、未取得的父输出或虚构完成状态。

已读根README新差异仅补充协调方对另一课题可重算数据的删除及历史恢复说明；第15条规则本身不变。原规则runner3b8保持2700秒实际pull/rebase/README差异检查；工作流只按已读根README blob21bd547f及本题bff8aea2覆盖其metadata BASELINES。H保原唯一规则行，科学checkout不随runner改变；Git `merge.stat=false` 保留。child环境按原方式不继承令牌与Git命令配置，令牌不写输出。

每批消费后清理raw；最终always链摘要在最终owned临时输入、sourcecache、科学目录清理之前。清理仅本request RUNNER_TEMP树，不跟随symlink，按原所属用户调整只读目录删除责任。无artifact、Release或raw提交；report只接完整32行小链索引，不能累积32份primary到GITHUB_OUTPUT。

## 8. 是否值得做，以及弱方向精度边界

138是有条件支配性质支持的**候选返回选择实验**。R299证明同一完成工作轨迹的候选集合包含旧工作返回，因此其保存有限 merit 的最小值不会更大。实际接受仍需要原 outer 在被选真实状态上读回 merit 后通过同一界；没有由保存小数直接升级为精确连续残差保证。

已有135日志只保存 seed与working-return的相关读数，不包含所有normal中间merit。对这357个原已完成调用只作已有标量的顺序比较，10个seed的保存merit严格更小；但没有一个记录满足“seed已过该原Armijo界、working-return却被拒绝”。这是原数值选择，不是重算merit、差值、范数或新trial。

尤其首次共同方向 alpha1 的原135记录是：

| 已保存字段 | 原值 |
|---|---:|
| uncorrected seed full3 merit | 3189.9257010514043 |
| original working-return full3 merit | 4.963821695184112 |
| original full3 Armijo bound | 4.963213527858338 |

所以不能预言仅选择seed便能救回首次大步；138完整输出将检验其余已走过normal候选是否有实际价值。R299也不保证两条随后分叉的32批轨迹有终点支配关系。

selector完全没有提高J精度。若理想J与实际用于方向的 $\widetilde J$ 满足 $\widetilde J=J+E$，同一方向 $d$ 的真实一阶斜率为

$$
r^\mathsf TJd=r^\mathsf T\widetilde Jd-r^\mathsf TEd.
$$

因此从保存的负斜率推出真实严格下降，需要实际误差项对该方向足够小；仅整列尺度的FDrelative或很小的保存奇异值不能提供这个方向性保证。这是误差解释，不是本次新增接受门。R301的极弱有限奇向量和微小原下降仍是必须保留的限制。

本次应直接读：是否真正选择了另一状态；该状态来自哪一inner trial；同一call保存与outer重读是否一致；原outer是否真实接受；radius如何按原规则响应；随后fresh J/原FD和完整final实际如何。若选择很少或仍停在微小下降，只继续同算法增加小步不能解释弱方向精度；更准确的方向动作或不同全局化需另源另身份，不能把本次selector重标成这类改善。这里不预选那条后继、不设置新的数值阈值，也不给出收敛保证。

## 9. 本地源级验证范围

只作文本、完整diff、SHA/JSON、AST和Bash语法；没有导入模型、运行reader、计算新merit/J/FD/Arb、做fixture或本地科学。

五个非candidate数值函数、完整outer循环及final/except/finally文本与135相同；wrapper 的 original_stop 及另外九个参数／半径／CLI／读回／配方函数 AST 相同。四执行组件sourcepin、90+4表、首26/current29、原2,407B父配方一致。工作流8个shell片段与5个inline Python仅静态语法通过。

完整相对135差异独立提供：producer、reader、wrapper、request、workflow五份。旧科学源原字节未改。上述检查是已完成的实现说明，不是附加科学验收／独立审查门；实际数值仍只在本公开仓库Actions得到。
