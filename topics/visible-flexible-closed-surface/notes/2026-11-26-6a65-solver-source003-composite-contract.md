# source003 显式复合消费者：原 Cauchy 观察与独立 Cartesian 实验

**状态：可执行入口与静态接线已准备；尚未取得真实原长分支末态及 matching observer，未发 active 后继请求，未执行这里的新数学尝试。**

该消费者针对已载入强分支 controller 的真实约束设计。原 controller 只承认 J*(4K+3)+2 的 Cauchy/角参数布局，不能把 7760 维 Cartesian 向量塞成原状态。这里保留真实原状态和 observer，在显式冻结的新 source epoch 中另做独立模型实验。新实验有自己的 state、baseline、接受数和标量记录，不能计入原 Cauchy 步数。

## 冻结文件

| 文件 | 字节数 | SHA-256 |
|---|---:|---|
| scripts/6a65-resume-cauchy-with-independent-cartesian-v2.cjs | 7922 | 83a039b3a2fadec7f2d48b555d1e49aecdb08de82cda6f1125f507a647e13c35 |
| scripts/6a65-composite-cauchy-cartesian-observer-v2.cjs | 14351 | 1b3ca8e723760d9a0b27358320149d401d55948eab1b26c68b992596afbe3561 |
| 准备配方 6a65-cartesian-source003-restored-stage-draft.json | 2056 | 84818ec5ac348534297c95480e540f4dc6985ae088ef8967e7f1cafd77b45039 |
| dispatcher 补丁 6a65-cartesian-composite-restored-v2-dispatch.patch | 1671 | 46443354b283375bee0344708b10998c940c27b841a3ed818c5be296b70cb413 |

这些为第三次失盘后新恢复的文本身份。尤其不能继承失联前未返回的 composite-v2 修改操作。两个 cjs 的实际 node --check 均 exit 0；补丁的实际 git apply --check 为 exit 0。检查没有运行 actual Cauchy normal、没有科学接受，也没有在准备阶段更新 main。

## 真实执行顺序

1. init 实际核原 Cauchy 状态及其 matching observer，保留全部 z、N、参数布局、metricTau、curvatureTau、完整曲率和几何目标。通过原 factory 完整 value 建立本次重评，标明 accepted=false；全局 cauchyAcceptedSteps 从实际输入继承，只把本阶段计数置 0。
2. run 调用原完整 R206 Cauchy LM，不加新曲率放大，不改 rho 设计空间。只有实际接受时，全局 count 和本阶段 count 各加 1；真实拒步保留原状态。没有硬编码 12→13。
3. 原 controller 执行本阶段真实 observer。新 dispatcher 仅对明确带 cartesianDownstream 标识、且文件名恰为该阶段 current-field 或 stalled-current-field 的输出走复合入口。其他 Cauchy 观察继续原入口，避免之后无关观察重复实验。
4. 先通过原 Cauchy 实际 factory 完成原 observer，另存其真实字节并记录 SHA。随后独立调用 6a65-cartesian-independent-experiment-v2.py，将此时全部实际 g、原 field、A、Z 和角 primitive 固定，完成自己的全 13 行新 baseline、一个完整 LM 尝试及更密观察。
5. 独立结果写自己的小标量 note，作一次普通本地 commit。子消费者不 pull/push，不读父进程凭据，不写 HANDOFF。父 controller 子进程返回后立即按原流程真实 pull/rebase、写 H 回执并 push 整个 HEAD，包含这条独立 commit。
6. 返回给父 controller 的仍是原 Cauchy observer schema、原维数、原 metric/curvature/immersion 和三项未变回执。独立结果只放 separately labelled receipt。独立数值失败有自己的实际 exit/signal/failure；不能改称原 Cauchy 新接受或完整数学成功。

Cauchy LM 中 rho 仍是设计自由度，不能把其迭代写成“整个过程同一 g”。独立 Cartesian 的 fixed g 指第 3 步真实原状态给出的 g；它自己的目标和原 Cauchy 目标分开比较。

## 实际身份与发布边界

复合入口从父 scalar-run-manifest.json 读取实际 run/attempt/source epoch，核候选 SHA、完整父阶段记录中的 checkpoint SHA 和冻结配方字节。source003 是待实际父末态出现后的新冻结；当前 source002 不热改。配方 draft 明确不是合法 matching followup，仍缺实际 run/state/observer/readrules/source commit 的最后绑定。

独立 Python 入口固定使用已冻结 v2，字节 SHA 为 8959a77106e563174c8233b369472dd0fa3e79aa2ff850e560c88e3a4099b418。它在训练和密观察缓存分别实际计算当前 g 的采样 K_g=-a_ss/a。不能把另一个冷零系数输入的 K_g 或几何值移借到长分支。

Git 接口已逐读已载入 controller：execute 等子 observer 结束，observe 再调用普通 publish；publish 不重置 HEAD，故会保留前面的独立本地 commit。子消费者只在父上次真实 pull 至少 15 秒后、距 45 分钟轮询阈值尚余至少 90 秒、且工作树干净时创建自己的唯一 note commit。若父报告未审 README 变化或出现其他脏文件则不冒进。该局部窗口只防并发事务冲突，不提供新的数学证明。

依赖环境在 runner 内实际核 numpy==2.3.5/scipy==1.17.0；若原同 job 已有匹配环境便复用，否则以真实 subprocess 建临时 venv 并记录 exit。数值子进程移除已知 GitHub/研究令牌和 Git credential 环境项。完整 state、缓存、原始 stdout 与 observer 都留在此 runner 的 Git 外路径，不上传 artifact、release 或参数数组。

## 接线参数

准备阶段标签为 Cauchy-original-then-Cartesian1，原 Cauchy 子阶段只请求一个真正完整尝试；original schema 不变，accepted_counter=cauchySameObjectiveContinuationSteps。原阶段的 accepted 计数不得承接独立 Cartesian 数。

phase 的 transition_kind 使用已载 controller 支持的 new_discretization_and_geometry_guide，但配方明确该名只涵盖独立下游 Cartesian 空间；原 Cauchy objective/layout 不变。真正 active 小请求应由根会话在实际长分支 state 与 observer 均存在后绑定发布；不能拿预计第 12 态或计划结束时间填入哈希。

准备文件的静态成功不构成该实际 source003 已消费、Cartesian 已接受，或课题完成。
