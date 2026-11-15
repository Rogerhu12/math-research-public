# 完整两网仿射阶段：原始实际结果与已读边界

日期：2026-11-15。会话 Astra-new-mechanism-9974ea84。**主课题继续进行；没有满足全部完成门的候选。**

## 1. 原运行与读取身份

科学计算仅来自公开仓库 [run 43728280256](https://github.com/Rogerhu12/math-research-public/actions/runs/43728280256)，job 132854922848，源码提交 [7329385a2dd84a40a271181c017c9a4028ae0f31](https://github.com/Rogerhu12/math-research-public/commit/7329385a2dd84a40a271181c017c9a4028ae0f31)。原工作流和所有步骤成功。这里从同一已结束任务的原输出读取，没有重算候选、开发测试或科学阶段。

原日志直接接口连续三次 Transport closed，故用只读公共观察器读取原 10,217,369 B 日志，SHA256
65c4dbae5dd981eae9bb8fa6ffccd338c6988e1b4e1778813ef839025421fddd。
首观察 run 43732106770 严格遵守 90,000 B 语义 stdout 上限，拟输出 98,963 B 后只报结构退出；收窄嵌套字段目录后的 run 43732214112/job 132866939491 成功读出原 development 和 actual 记录。仅语义 stdout，不写原 payload、Release 或 artifact。

已读 actual 原 JSON 位于原 log 第3093行，时间 2026-11-15T15:24:09.7813799Z，JSON子串 3,282,055 B / SHA256
472214901278f46f7257787407f7818dd69f05bbc3c420773c7c77ab83e9d060。
这与 summary 文件（带换行）3,282,056 B / SHA256 fcd318dc43449bcb521a9f8256647ea14589dc0d4aec1bac3ef19cd82bc1e1a2 的字节对象不同，不能混用哈希。

receipt 55,785 B / SHA256 77435aab53274594ad70ba8e4da0a6e6fe7961de6e10b7d587bff85ddb65acb7。root 已逐项核对原请求的54个直接来源与 receipt 全合；实际106个递归科学来源亦全部对应 receipt 唯一同名路径并同 SHA。原正式 audit 16,929,326 B / SHA256 cee75e9b9fc5249a47a317b9c193f15896618a093f349c7e560b32b50b865242 只留元数据，不入仓库。

## 2. 真实改善及全部原网格门

同一固定 g、原 b0、原163物理表示/159独立坐标；没有更换参考度量、材料区或误差定义。所有值来自原最终同一状态的两次独立值评价。

两网最大相对 metric η 从0.26640117915606165降到0.2663817176174397，真实下降0.000019461538621978747。

| 原最终观察 | 粗网384 | 细网768 |
|---|---:|---:|
| 各网最终 η | 0.26638171726382853 | 0.2663817176174397 |
| 各网最终最大绝对主曲率 | 57.9999624436237 | 57.99998339453157 |
| 各网镜像半径最小有限值 | 0.10092575980598417 | 0.10092575980649648 |
| 各网最大绝对 y | 0.38998955638936217 | 0.38998995941104003 |
| 各网内条带余量 | 4.4361063783471266e-7 | 4.0588959970833116e-8 |

两网各14个原 gate boolean 全为 true：cap/box、曲率λ与scaled-PSD行、硬球、硬条带、独立直接曲率、独立镜像半径、多项式镜像门、外条带、旧 metric 预算、正则筛、signed height、恢复点及硬门。原物理盒 violation 准确为0，未经 clipping。原目标13/50仍未达到，主课题1e−6更未达到。

原高度门也如实保留浮点现象：仿射高度 0.14270420084310473，重构高度 0.1427042008431047，目标 0.14270420084310476；相应 margin 为 −2.7755575615628914e−17、−5.551115123125783e−17。原声明容差下 eligible=true，但 both_height_margins_nonnegative_in_current_arithmetic=false。这不是精确非负或连续高度积分证书。

最终极值在 t=0.465、θ=0；原记录表明此处 E−1 占主导，F/a 约6e−16。旧 raw δ=0.26640845723039297 是失败的 metric 辅助量，仍不是几何 δhold。

## 3. 次数与费用分账

原记录 new_scientific_solver_calls=1，old_optimizer_calls_this_run=9，分别为本轮必要的九个输入阶段恢复；不能把9次恢复冒成零，不能把 inner LP 数冒成新科学阶段数。

| 原费用 / 调用 | 实际值 |
|---|---:|
| 新 optimization active | 35.28716934900001 s |
| 九输入准备/恢复 prepare | 805.206120942 s |
| 新 audit elapsed | 39.814420190999954 s |
| 原整个 process | 845.020544428 s |
| 原 peak RSS（Linux KiB） | 3794308 |
| 初始化及 trial 完整值评价 | 16 |
| 最后同状态独立完整值评价 | 2 |
| 新 driver 合计完整值评价 | 18 |
| 原共享完整值 cap | 40 |

方向扫描不冒普通几何值评价；方向JVP、增补metric行J的成本由原单独栏目记账。新 selected 路径未构造完整163/159角向参数张量，原记录 original_full163_geometry_J_batches_in_new_selected_paths=0。

## 4. 原开发检查

原 development log 第741行、2026-11-15T15:10:00.1264327Z，JSON子串30,521 B / SHA256 41efb0b8356cb166c4ae3c8f9f2f48b5287cbcb85fe0d6bb4f031f0fe923a36d。passed=true，completion=complete，耗时4.727428111000009 s，最大RSS113.19140625 MiB。

原同源码绑定复用首运行已完成的6个方向检查；本次继续的 array 10项、error identity 5项、真实第九handoff 10项和pipeline I/O 4项均为 true。没有重跑旧developer suites。array中并列目标保留早先完整norm修正 incumbent 的断言已按真实冻结规则更正，不以最后一轮 gap 替换被返回 incumbent 的状态。

## 5. 后续已读内容与仍未读边界

日志控制标记现已正确转义，原pull、checkpoint及六个模型/七个trial均已读取；第5来自原COMPLETE_REPORT而非缺失的native打印。详细原门/误差/24输入身份与有限模型停止原因见[六模型解释](complete-affine-six-model-interpretation-20261115.md)。10primary+2SOC实际耗尽12LP，最后只有一次未收紧的完整模型评价，不能作驻点结论。

九次恢复的详细drift与较大SOC控制器表仍在继续只读原日志。本轮科学不重跑，后继以新中心重建支持方向改变重复cut瓶颈；不以同预算续跑或阶段报告收尾。主课题所有连续几何完成门仍未共同支付。
