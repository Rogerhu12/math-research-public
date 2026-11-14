# 新背景转包与闭图预算入口的 root 完整差分复核

2026-11-09，/root。状态：**PASS，仅新参数/身份接口、原数学保持及已观察的只读预检证据。** 没有新转包、grid、ExactHermite、metric、曲率、root、flow或solver调用。

root全文读取新producer相对冻结base的全部差分、新consumer相对冻结budget-v2的全部差分，以及两位作者互换角色的完整独审。新增数学外的每个函数均在差分中完整出现；旧数学段另作下述逐字/AST核查。

## 参数与来源

新producer bdf6307f仅增加iterationCheckpointFile、sharedEngines、trialDiagnosticFile、trialStatePrefix四个已审记录/引擎分配键。路径键只许string/null、sharedEngines只许bool/null；其余变化按键存在性及canonical JSON检查，嵌套false/0与true/1不再互混，未知新增null不再漏过，allow_nan=False。旧v2问题被如实保留，正式consumer绑定修正v3与策略2b4fd1d1真实身份。

producer完整检查旧manifest、packet、data和六个背景定义文件。consumer另固定六个预审背景文件SHA，核height/positive-alpha/tight-alpha/校准/原bookkeeping连接、旧实际source CP与manifest参数、原包及数据。正式分支还核新manifest与实际CP、严格参数、原新精确物理径向域和完整packet loader；没有把新增字段例外扩展成改变g或校准表的许可。

## 模式和数学段

参数模式只从真实闭CP读参数，不能同时接收新manifest或几何证书；输出排除finished、新map/data身份。正式模式必须真实完成的manifest和finished transfer。producer与consumer都以真实的新脚本SHA、base与policy记录身份，没有伪写旧实现。

root实际静态验证六个原数学函数AST相同，producer从old_info至write_npz完成的整块字节相同；consumer从正alpha门直到函数末尾，删去唯一新增base身份字段后逐字相同。检查记录在root-transfer-pair-static-review.json。由原已审算法证明可复用这些算术与不等式；本次没有直接把旧图metric/κ数值转给新图。

两完整独审记录了：producer真实quarter参数预检独立exit0、JSON字节同，19参数接受/拒绝例通过；consumer也独立exit0并重新核同一十二个允许差异。这都是元数据兼容性证据，未运行正式几何分支。root另检查whole-metric-reach-v2的消费接口，它绑定closed-budget输入与同图证书，不硬编码旧budget-v2脚本身份，故此处没有第三个旧身份例外需要伪装或绕过。

未来只在真实最终CP完成实际export、共同cut及新图证书后，才运行正式转包/预算，并对新图自己的metric、曲率与所有全局比例重证。最后whole脚本原门仍为1e−6，还须明确另核原G5的2e−9目标；本次不支付该门。
