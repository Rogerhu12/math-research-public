# RET72：旧有限尾场的曲率与正分支定位报告退存

日期：2026-11-28。范围：只从当前课题树移除下面三份已经生成的旧有限状态诊断报告；原科学输入、全部计算源、参数、证明、比较记录以及失败结论不在删除集合。本文不代表重新执行了旧科学计算，也不提供连续曲率、闭面、嵌入或 reach 证书。

完整逐文件来源、完整配置、实际标量、全部恢复命令及未知项见 [完整 provenance](../computations/legacy-finite-tail-curvature-retention-72-complete-provenance.json)。执行删除由 root 在 fresh HEAD 核对确切 path/blob/bytes 后普通提交完成。本工作只保护未引用的完整 Git blobs，不写 refs 或队列。

## 1. 三个确切输出及固定恢复版本

固定恢复提交为 `79f9aa50f5980db0ef1d5e8ae4234e14f7ff2fbd`。表内路径都在本课题的 `notes/` 下。

| 文件 | 字节数 | Git blob | 整体 SHA-256 |
| --- | ---: | --- | --- |
| numerical-m2-smallcut30-q02-lambda05859375-curvature16.json | 77490 | e326be90136394b667c977a3061c93ee14352365 | 2193fc741dcdd2a40cd75a515cee4bca52959806b6214a6a5adc265190d8760f |
| numerical-m2-smallcut30-q02-lambda05859375-branch.json | 40259 | c28cadea4eb9a953222ce47c233f24c918b14759 | 0ea89b77a804c7b18a7f455fcd0124352902db89760e898ce211a9d18c7187f2 |
| numerical-m2-smallcut30-q02-lambda05390625-curvature24.json | 178390 | 934a3ca41ce496ac0a799b1a4365ecf0b83bdb83 | null：所读既有小记录没有给出 |

三件毛计 296139 B。前两份完整小正文已读取；第三份超过 100000 B，未读取正文，其 SHA-256 不猜填。第三份的原输入、有限分辨率、诊断结论及实际未达到的更强目标来自下列完整保留的小比较报告和原说明。任何未来需要其完整 jets、状态向量、stage rows 或 whole-file 校验的读者，必须从固定 Git 对象恢复原全文；本台账中的标量不是替代输入。

本批不重复 RET71 两份 conditioning 输出，也不涉及 solver 独占的 Hermite/Nelder 或尚缺旧 adapter 的 rational-trace 组。

## 2. 实际生成路径：完整原状态重读

两个定位器都接受三个位置参数：完整 source topic、原 response JSON.gz、独立的新 output 路径。它们先完整解压原 response，要求其成功且没有 failed 标记，随后读取整个 `config`、全部 `response.checkpoint.states`、完整 `request.height`、原 residual/audit 和完整 source 字典。

实际有限场计算沿原 `createRecalibrationFactory`、split-flux compact tail、Fourier root-split engine 和 momentum physical-jet evaluator。遍历每个保存的 stage、每个 profile、原 auditSteps（缺省时 steps）上的全部径向位置及 engine.N 全部角点。原 stage 状态直接来自那个 response；这里没有重新续接分支，没有调用新的 nonlinear solve，也没有把摘要中的少量极值点当成全输入。

`config` 中 trace、iteration checkpoint、trial diagnostic 和旧 initialCheckpoint 路径保留其原字与原意义。定位器没有把这些路径当作本次场的额外科学读取：它直接使用该成功 response 内所有已保存状态。原非线性求解怎样取得那些状态，仍属于该原 response 和原来源链；本批不声称重建其未取得的运行环境或未知客户端。

本批完整来源登记含 29 份小源：本课题两定位器与同场精化比较器，以及外部 source topic 的 26 个实际模块。九文件 loader manifest 逐文件保留；完整依赖覆盖 recalibration、subdivision、tangent、Fourier product/root、physical jets、momentum、cusp、warp 与原 raw Cauchy。没有仅凭相近模块名宣称旧源相同。

## 3. 原 curvature16 定位器的确切全文恢复

curvature16 原报告自记定位器 SHA-256 为：

`dc02074bbbcca521936e08169b931dda23cd073d006832d91ab5f24aa73ce61a`。

当前 `computations/numerical-tail-curvature-locator.mjs` 为 7312 B、SHA-256 `7ced4518031a60175cec2375bdf4e382cc171af7510c446d398123c74a5aa8e1`，后增了 physical-Darboux 极值、原 profile 归一化报告字段及说明。完整六处文本反替已经恢复 6813 B 原源，整 SHA 与原报告自记严格一致。本批保存该完整源为：

`computations/retention72_numerical_tail_curvature_locator_original.mjs`。

完整六个 before/after 块也在台账中。它们是源文本差异，不包含数值结果的编码或分块。重算旧 curvature16 时，应在独立恢复树将这份完整原源放回原入口 basename；不能把当前新增报告字段版本的 SHA 冒作原版本。

branch 定位器 5817 B 的当前完整源 SHA 与原报告自记相同：

`0fd1c3e852eda3975ef40cb5a867244f38da1409fe1c0e5e951128f30154ca04`。

curvature24 的大正文没有读取，因此其原 self-SHA 保持 null。现存完整 7312 B 定位器给出了该确切成功有限场的完整再生成路径；它相对于恢复的原定位器只多上述明确的报告变化，所有原数值扫描正文保持。这里不声称未知大报告自记了哪一个定位器 SHA，也不声称新重算会有相同 elapsed、路径或整体输出字节。

## 4. 三份完整科学输入与恢复边界

这些 gzip 均为原科学输入，不是本批删除项；本次不读取任何二进制正文。完整压缩字节按下表从 `60321451c058c6a51da58c37ae5ec6f2d1145f74` 恢复，不先解压再重压以替代身份。

| 原输入（notes/ 下） | 字节数 | Git blob | 原记录 whole SHA-256 |
| --- | ---: | --- | --- |
| numerical-m2-smallcut30-q02-tail16-response_0011.json.gz | 106273 | 53bb89a5cd1bd5a5e6374c127d36833f47a35f59 | 2a7e29e8cd382c358046d5a4dc1d202cffe0db07c4c62e787b3f415e1e7191ba |
| numerical-m2-smallcut30-q02-lambda05390625-tail16-response_0001.json.gz | 107141 | 07c19b4b5ed2ba431996d21d8bc2614f25f068d1 | 2c8d87f87a8ce47548594c194bf305f1f4f802845abcf56594f5587e433f85ee |
| numerical-m2-smallcut30-q02-tail24-parts8-finepath-response_0009.json.gz | 300408 | 2ff2701c3c5b9b12ea306b3b75b8ebb01e72bfca | a8be45117161052ec924ec67c837f9b6e3a08b1672003baffd0f7f9c8db5070a |

第一份供两个 .5859375 诊断；第三份才是 .5390625 的 M24 诊断输入。中间那份是同 .5390625 的 M16 比较输入，不能用更高幅度的第一份替代。保留的完整 refinement JSON 逐项比较这对 coarse/fine 的全部物理构造、完整 H、原有模式和新增零模式，记录 19 个共同源身份相等、每原 profile 的实际步数相同，以及所有发生变化的配置路径。

两定位器在结束全部场扫描后读取 `source-origin.json` 的唯一字段 `source_revision`。旧完整输出给出其消费值 `869436630c99aa5a68afb55bd8877c826034d117`；原 source-origin 整文件的 byte/SHA 身份未知。本台账明确允许在独立恢复树创建新的、明确标识为恢复用的 metadata JSON，仅含这个原消费字段。它不冒原整文件，不证明 checkout 属于该旧 commit；实际数学代码由完整逐源身份绑定。该字段只被写入输出来源说明，不选择方程、网格、根、精度或源路径。

旧 response 还带有原 Python 客户端等 provenance 字典，包括尚未恢复的 4752 B 客户端版本。这些值原样保留，定位器不导入或运行这些客户端。本批没有把“携带旧身份”扩大为“重新执行了原 nonlinear 求解”。

## 5. .5859375 / M16 的实际有限结论

原 response residual 为 2.299355556993617e-10。完整原 audit 的 physical fullD 为 4.23072619656857e-5、normalizedFullDefect 为 .009803895401092007、minLeading 为 .13354791718673648、minD 为 .9997187745677653、formalCurvature 为 8.033705579162039、actualMetric 为 4.486013560622838e-9。完整其余 audit 项和配置已逐字存入台账。

三个不同位置不得混为一个因果：

- 最大形式主曲率 8.033705579162039 位于 stage 7、rawCell 0、rawSegment 7、x=.7083333333333334、theta=.8344855486097889、r=.2865662100127457、A=.9911084089301638。其两个主曲率为 8.033705579162039 与 .08333614878502171。
- 最小 A=.13354791718673648 位于 stage 19、rawCell 0、rawSegment 4、x=.875、theta=6.160466844148735、r=.24404912798072775。该点不在反射轴上；原 branch 的 axisFormulaApplicable=false。其局部两个主曲率仅为 .0020256908620606383 与 -.007078037140055967。
- 最大归一化 Darboux 缺陷位于 stage 16、rawCell 0、rawSegment 4、x=1、theta=0、r=.27706848308305876；该点 formalGaussResidual 为 .000042307269045979194。

原两个定位报告记 elapsed 33.783 与 22.138 秒。这些是已记录值；原进程 exit code、OS argv、Actions run ID、运行时构建与 wall/memory limit 没有在所读来源完整给出，均保留 null，不以有输出倒推出已知 exit code。台账给出可用的完整重算 argv，明确它不是臆造的原 OS 命令记录。

## 6. .5390625 / M24 精化实际付了什么

这份成功状态的配置为 M24、N512、depth 8、shootingParts 8、steps 12、auditSteps 12、projectionFloor .05；完整其余参数必须从它自己的精确 response 读取。residual 为 2.1993004349522447e-10；physical fullD 为 2.6586883787704095e-6；normalizedFullDefect 为 .00030804998431122906；乘以 shootingParts 后的原 profile 指标为 .0024643998744898325；minLeading=.22258706809051962、formalCurvature=8.022166212065562、actualMetric=1.409452554668759e-10。

保留比较记录给出的 fine/coarse physical 和原 profile 缺陷比约 .33283793393733。它是约三倍改善，不能把切段改变导致的坐标因子再算成六倍改善。物理曲率几乎不变；小 metric 残差没有支付二阶缺陷或连续闭面责任。

原说明仍完整保留：M24 这条续接在实际预算与失败的大步之后，没有达到更强的 .5859375 目标。报告中的成功 .5390625 状态不得写成更高幅度成功。曲率24 的极值位置只引用保留说明里的有限十进制精度，未假装读取了大报告中的全精度字段。

## 7. 保留的完整结论与读者

下列文件全部留树，既不删除也不改写数学结论：

- [完整同 H 精化比较](numerical-m2-smallcut30-q02-lambda05390625-refinement.json)：11425 B，blob c1a9a99479ffbb05fa3d200962e7f0138c6c057b。
- [尾场 shooting subdivision 说明](numerical-tail-shooting-subdivision.md)：7834 B，blob c8803d006551b1b773fd07ca5cbf886fcabb3739。
- [正分支定位说明](numerical-tail-positive-branch.md)：8992 B，blob 172e6a2afa39b559fdd7d1412c6e531df0f38b1b。
- [原 M2 状态总记](numerical-m2-status.md)：27647 B，blob 0744be11efe73371c766129d8cf0bf4c406f892f。

两生成器以原 response 为输入，不以被删的另一个定位报告为输入。叙述性读者保留原链接含义；后续任何实际 whole-file 读者需先按固定提交将原文件恢复到其要求的相对路径。检索并不等于全仓库没有其他读者，因此本批不作“没有消费者”的断言。既有完整科学输入与未来调用的恢复责任不因现树退存而消失。

## 8. 可执行恢复合同及未做的工作

每条删除记录都带完整 `git show` argv 与单独恢复根目录中的目的路径。恢复旧输出用固定 79f9aa50... 的原 blob；恢复原 gzip 用固定 60321451... 的原压缩 blob；恢复 source topic 使用台账逐源完整路径和 whole 身份，并保持九文件 loader manifest 的实际查找规则。重算 curvature16 须放回本批保存的原 dc020 全文；branch 使用原 0fd1 全文；curvature24 使用明确记录的可用完整 7ced 生成器，未知原 self-SHA 仍是未知。

完整旧输出的数值数组没有重新编码、分块或保存成差分。台账仅保存完整原参数、来源、恢复命令和必要实际标量结论。原输出字节的确切保全由 Git 完成，不由新摘要代替。

本批只做完整小文本、源接口及树元数据阅读和文本哈希；没有本地科学、AST、compile、数值 fixture、性能试验或重放。没有把重算作为退存或下一真实科学入口的新增门。最后精确 path/blob/bytes 是否仍与 fresh HEAD 相等，由唯一 refs 写者 root 在普通发布前处理；若不等，该条保留等待明确身份，不扩大删除范围。
