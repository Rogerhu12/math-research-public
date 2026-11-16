# R458：同一作业内的联合精化父链与固定闭面目标证据

作者：OpenAI ChatGPT `/root/amplitude`（AI），根协调方编辑；2026-11-16。

**可信度：已证明（限本文的来源组合、控制流与所列条件命题）；request207 的实际求解、联合精化、闭面验证及材料查询尚未执行。**

本结论给出一个可执行的有限精化实验合同。它在新的公开 Actions 作业内完整重生冻结的 request205 子流程，再以该作业真正接受的零活动参数场为父，依次增加五类离散分辨率及完整 Fourier 模数。每个新场重新运行几何消费者，并用同一个首次闭面目标计算实际误差证据。本文没有产生新的场、误差数值、接受记录或完成声明；两个预定后继也不是精化到机器精度的证明。

## 1. 冻结来源与命题的适用对象

本文逐文本阅读的三个新运行源如下。SHA256 是完整文件字节的身份，不是某次数值执行的结果身份。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| `geometry_20261116_request207_owned_roles.py` | 17026 | `304eaa41b3b9c0e1eab4e71678720f336cbd1a5e7f47ceb9ef1b6e8d2b0ddc5f` |
| `geometry_20261116_request207_joint_refinement.py` | 44927 | `76881ec3ad75c7d33ef2ea70cafbf12cf73dcb9273f137187f73a975368f4ea8` |
| `root_20261116_request207_refinement_necessary.py` | 33942 | `7902848f2aac3abb880ae604aa81f7f87bdd68b7b25f6a39dd0ffa92152dde24` |

具体参数来自 `current-C-actual202-joint-refinement207-request.json`，21956 字节，SHA256 `c798f376a63d552c12ff56b51fba8f11ed46bba4d858ec95df2838cfe3575015`。工作流为 `visible-current-C-actual202-joint-refinement207.yml`，98422 字节，SHA256 `37f426a26c97f637fae74cdcf185fb3ef5fc5025114a7b852613f9417673627e`。

外请求显式引用原 request205 的 97406 字节文本，SHA256 `06ae0670329d38b77448ef43f54021da3c5eb2575e9e7a290cec6b2968c1f6c4`，并保留其 154 个源 pin；新增 75 个 pin 后为 229 个。`bind_request` 不允许同名不同 SHA 覆盖旧源，并核实际文件、当前仓库、当前 run/source 与角色身份。沿用名字含 `205` 的 namespace、schema 或内部目录，只表示执行这份原子合同；实际记录必须属于新的 `GITHUB_RUN_ID` 和 `GITHUB_SHA`，不冒用历史 205 已删除的现场。

条件命题以 SHA256 身份可靠、实际已读文件稳定、所引用冻结消费者按其既定合同工作为前提。`receipt` 对文件读取前后 stat、长度和 SHA 做来源绑定；这支付输入身份，不支付数学不等式。本文不增加数值对拍、测试 fixture、秩门或新的验收阈值。

## 2. 真正连续的父链

记 $P_0$ 为本次新作业按原 205 全链真正完成的 frozen450 checkpoint。原 205 仍从准确 C、cut、真实十参数候选与全部 112 far 数据开始，经过完整三活动参数 453 求解，再在同一实际末十词下运行 fresh 零活动参数 450。其 FD、当前响应、full-DN、audit 及原接受条件均由原运行源决定；本文不把前一阶段三行删除后称为第二阶段接受。

新 runner 的 `accepted` 同时读取原接受布尔、driver 返回、子进程 exit、owned group 静止及资源/外部中断状态；后继 owner 还须真实返回。只有这组实际条件成立，才读取真正的 adapter、checkpoint、native configuration 与 sampling result，登记一个可用父场。正常外层退出、日志有 SHA、warm seed 或某个较小残差都不能替代它。

预定父链是：

| 层 | 直接真实父 | 本层改变 | 保持或重新承担 |
|---|---|---|---|
| $P_0$ | 本作业原 205 子流程 | 首个真正 frozen450 | 原全部 453→450 门及首次闭面定义 |
| $P_1$ | $P_0$ 的实际 accepted checkpoint | R456 的径向网格、field/native 角、native steps、material 角、physical 角五个 factor 均为 2 | 同准确 C、完整十词、原完整 450 数学及所有原门；真正重求新场 |
| $P_2$ | $P_1$ 的实际 accepted checkpoint | R457 目标 $M=128$；四个角/步 factor 均为 1 | 继承 $P_1$ 实际分辨率，完整变维深端/far/native/BVP，原全维门 |

**父链命题。** 若 $P_1$ 被登记，其父是本作业 $P_0$；若 $P_2$ 被登记，其父是已登记的 $P_1$，不是另一条从 $P_0$ 平行出发的模数轨道。

证明只需沿 `solve_level` 的控制流归纳。层 0 仅由本次 origin 的真实接受记录创建。层 1 输入指向该 origin 的实际目录与 checkpoint。层 1 未接受或结果缺失时，后继 solve 不启动并记录原因；接受时，新 owner 的实际返回目录成为唯一下一父。层 2 从这个目录读取配置和 `actual_resolution`。因此两条平行的成功记录不能被拼接成这条联合序列。几何、held 或 measurement 失败并不自行撤销已支付的 BVP 接受；进程归属不明、剩余时钟不足或真实父不存在则如实限制后续执行。

`solve_input(2)` 从旧 sampling 参数副本中显式 `pop("steps")`。R457 sampler 接口接受 14 个工作参数，实际 steps 应由真实父 `actual_resolution` 形成，不能让原 205 的旧 steps 再覆盖 R456 新场。四个 factor 为 1 表示保持父分辨率，不表示恢复旧基线。这是来源/参数接口修复，不改变任何 RK、root、QR 或接受公式。

M 路径使用原 R442 完整深端与全模数 far 构造，重新承担新增频率及全部当前频率责任。虽然输入中保留原 far 来源以说明历史绑定，不能据此称 $M=128$ 复用了原 112 行作为完整新 far。R462 的同 far 复用方案不在本执行链。原 M driver `395da6c8…` 与 checkpoint writer `18399ec7…` 不改，R457 只按真实 R456 driver/native/config/checkpoint 来源接入。层 2 是完整变维问题，不假称仍是 450 个方程。

## 3. 同一闭面目标需要哪些真正冻结数据

“十个系数相同”不足以推出完整闭面目标相同。共同对象还包括准确 C 与全许可 root 族、准确十族 DAG 及 cut/cuff 定义、完整十个有理/字词输入、首次 construction 的 $W,H$、全部 marker 的实际数值和顺序，以及首次材料注册、归一化和图的解释。新离散 native 场及新材料参数化可以改变，不能只比较 source 名称后忽略这层差别。

R452 首次实际过程提供 A（first-construction freeze）和可能存在的 B（actual-material transport record）。新 runner 从真正的首次 procedure/result/输入及输出 receipt 读取它们，不从文件名或旧 SHA 反造内容。`geometry_level` 使用首次真实 construction 与 first shared field；R456/R457 的消费者继续核相同目标、全十词和完整 construction 字词。A 或首次 shared 现场缺失时，相应几何责任标为未付，不伪造参数。

B 包含真实首次材料定义与相应 plan/assembly 来源。若 B 尚未生成，则共同材料 measurement 明确未付；它不阻止已具备真实父的下一次求解，也不额外阻止独立 held。B 存在也不等于所有共同材料逆查询已经执行。

在 [R443 的共同材料图条件](R443-common-material-angle-pullback-and-fixed-closed-target.md) 下，令 $\Theta_0$、$\Theta_j$ 为具有完整 lift 的严格正材料圆映射，$I_j=\Theta_j^{-1}$。共同首材料坐标到第 $j$ 场的 phase 运输为

$$
T_{j,t}(x,q_0)=\bigl(x,I_j(\Theta_0(q_0)-\alpha(t))\bigr),
\qquad \alpha(t)=\pi t/2.
$$

这个准确定义不需要为了存在性再增加一次数值逆验收。实际需要点/区间值时，由 R457 原逆查询和六 jet API 真正计算并报告未付范围。首次、当前材料字词不等不自动成为 solver 拒绝；同闭面目标也不能由“两个字段名称相同”代替上述运输合同。非对称帽 marker 禁止把整个闭面当成旋转对称；平 cuff 的抵消只在原粘合公式的适用区域使用。

## 4. 每层的新几何与独立 held

对每个已接受的新场，runner 都构造新的、绑定本层真实 checkpoint/native geometry 的五阶段输入：

1. 完整 `radial_replay`；
2. 当前场 `original_cuff_atlas`；
3. 当前场 `shared_field`；
4. 同准确目标的 `metric`；
5. 完整块/原叶 `reach`。

这些是新的真实消费者调用，不沿用上一层 metric/reach 成功布尔或上一层场的 raw。各阶段由自己的源、输入、实际输出身份及未访责任说明范围。R456/R457 后编排的原数学体和全域责任未被新 runner 缩减。

held 是独立分支。它需本层真正 shared/atlas 与实际 witness plan，但不要求 metric 或 reach 已成功。witness 构造读取实际准确场，选择唯一左端为 0 且右端为正的 prefix 首片，在 radial=`0`、$q=0,1/4,1/2,3/4$、`lower=false` 上形成原 R425 输入。该规则支付成员与来源，不保证四点能给正的分离量或达到所需 held 比例；完整全像 cover、误差和反射责任仍由原 held 源执行。其异常、预算停止或 witness 未付分别返回，不能反推 BVP 失败。

## 5. R459 测量的是实际误差，不是重复同一个通过布尔

引用 [R459](R459-fixed-closed-target-relative-error-and-refinement-evidence.md) 的准确场和共同目标合同。对任一许可的准确 C 实现 $\zeta$，设本层共同材料表达为 $F_{j,t,\zeta}$，固定目标为 $g_{0,\zeta}$。比较的量是

$$
\epsilon_j(\zeta)=\sup_{x\in M,\,t\in[0,1]}
\left\|g_{0,\zeta}^{-1/2}
\bigl(F_{j,t,\zeta}^{*}e-g_{0,\zeta}\bigr)
g_{0,\zeta}^{-1/2}\right\|_{\mathrm{op}}.
$$

它是完整相对二次型算子范数，不是某一矩阵项、RMS、有限残差或 `eta` 通过位。R459 只有按原全域 cover 条件覆盖全部活动片、cut、反射与帽责任时，才可给相应全域上界；粗界有效但宽度未达到工作目标，与某个根域尚未包住，必须区分。下界也须来自实际非空查询/单元的合法原包围，不能凭上界下降推定误差下降。

共同材料图满足 $T_{j,t}^{*}g_j=g_0$ 时，误差二次型随同一可逆图合同变换。广义特征值在共同可逆合同下不变；对固定 $t$，整圆上的 $T_{j,t}$ 为双射。因此原全空间 base-phase 的完整误差界，可按 R459/R443 的粘合条件传给全 $t$。这项证明与有限时间采样分工不同，非对称帽仍使用其完整固定图合同。

本次实际时间 subdivisions 为 **4、8、16**，分别对应层 0、1、2。每层都计划在 $t=k/n_j$ 上调用真正共同材料逆/六 jet 查询；统一 witness 集为 prefix 公共径向 $u=1/2$、$q=0,1/4$ 的上下两反射，共四点。参数 `max_inverse_steps=80` 是有限工作上限，不能当成逆存在或完成的证明。只有实际查询齐全且来源相同，才可报告嵌套时间网格已付；预设 4 整除 8、8 整除 16 不能填补未执行查询。

若实际返回统一合法区间 $L_j\le\epsilon_j(\zeta)\le U_j$，则：

- $U_{j+1}<L_j$ 足以证明这两个已绑定层的误差严格下降；
- $L_{j+1}>U_j$ 足以证明严格上升；
- 只有 $U_{j+1}<U_j$ 而区间仍重叠，只能说明上界改善；
- 区间重叠、查询未付或预算用尽，结论是未分辨，不能写成非收敛或严格下降。

`compare` 消费至少两个实际测量结果及其共同 first A/B、plan/assembly、目标、时钟、checkpoint 来源；缺少这些结果则明确未启动。任何区间严格分离或更小误差都不是下一层求解的新前门。跨层 $C^2$ 收敛、所有 $t$ 的更强参数可微性及 machine-floor 完成，亦不能由这两个有限后继和若干时间点自动推出。原 BVP、boundary、native 容差未经误差传播定理，不自动成为几何误差下限。

## 6. 一个绝对时钟，多个资源上限

原子合同的 `actual_job_deadline` 被逐实际 receipt 绑定到 origin、recipe、run/source，保留 schema `request205-owned-job-science-deadline-v1`。若其真实起时为 $b$，则科学截止 $D=b+18900$，必要读回截止 $D+2700$。新精化不会在进入 R456、M、geometry 或 measurement 时重开这两个时钟。

令实际当前时刻为 $s$，child shutdown reserve 为 30 秒，末端 measurement/close reserve 为 900 秒。源码对一般科学角色使用

$$
A(s)=\max\{0,D-s-900-30\},
$$

对 measurement 角色使用 $A_{\mathrm{meas}}(s)=\max\{0,D-s-30\}$。实际可用时间是声明 cap 与对应剩余量的较小者。900 秒只是给后段保留的资源策略，不保证这 900 秒足够完成测量，也不延长 $D$。

| 角色 | 预设秒数上限 |
|---|---:|
| R456 sampling/configure；完整 450 | 900；7200 |
| M 深端；sampling；完整 M BVP | 300；12000；7200 |
| 每级 radial / atlas / shared / metric / reach | 600 / 120 / 300 / 600 / 600 |
| 每级 witness；held | 120；300 |
| 每级 R459 measurement；最后 compare | 300；120 |

这些数不能相加成为新总预算。M sampling 的 linear/point 分配还按真实剩余时钟及 deep 预留裁剪，内层 owner 继续执行原裁剪。`max_nodes=2400`、内存/空间界、精度和单元数也是显式资源合同，不是允许截掉本应存在的网格点后冒完整解。measurement 使用原明确精度、cover 上限与时间查询上限；资源未付范围须留在结果中。

工作流在原全部必要读回之后安排精化角色，GNU `timeout` 按原 startup deadline 动态裁剪 rules parent；运行体又绑定真实 BVP 的同一个截止 receipt。二者不把尚未取得的 BVP 时钟编造出来。必要 reader 在缺失该时钟时可使用明示的 startup 运输截止处理错误，但这不生成 science 接受记录。原 rules runner 的 2700 秒同步责任和 README 来源核对保留。

## 7. 嵌套 session 的归属与静止责任

新角色使用实际独占 session，记录 PID、PGID、SID、Linux boot identity 与 `/proc` start ticks。父循环观察实际后代，并读取冻结内层 owner 的真实记录，以覆盖其中自行创建的 nested sessions。相同 PID 只有 start ticks 一致才视为原进程；发信号前再核真实身份，不能按 namespace 猜测 PID 或杀死未知进程。

停止路径有有界 TERM、KILL、wait/reap 和再观察。进程扫描异常、身份冲突、未知 namespace-bearing live process 或仍活跃的已知 owned process 都保留为未静止责任。未知进程不被伪归属，也不允许据“主 child 已退出”宣称全树静止。

因此这里证明的是：在实际登记/扫描证据满足源码条件时，后续消费与清理遵守该静止合同。它不声称有限次 `/proc` 观察能无条件证明从未被观察、也没有合法内层收据的任意进程历史。quiet、资源停止、外部信号和科学拒绝分别记录，生命周期限制不改数值接受标准。

## 8. 必要读回、超限和原 raw 的生命周期

新 reader 在 Actions 内读取原 metadata/result，并调用已 pin 的必要选择器；大成功列、矩阵、扰动表和科学原账只保在本次临时目录，公开返回其身份与明确选择范围。必要正文保真实父链、全部 12 个角色的启动/未启动状态、原接受和分辨率、原 FD/错误/partial 选择、完整 M 未付范围、几何/held/measurement 返回及比较责任。它不把未回的大表称为 root 已逐值读取。

stdout/stderr 的实际错误在所定范围内原文读取；仅实际字节完全相同者才共享正文并保全部路径。单个错误大于 90000 字节不能塞入摘要时，记录原身份及整段未返回范围，并将必要读回判为不完整，不编码分片搬运它。原 child 的协议 exit70 与科学过程的拒绝/部分完成分别保留。

新单份必要 JSON 上限仍为 **90000 字节**。先形成完整所选正文并记实际身份；超限则诚实 fallback/70、返回 section 大小和未完整责任，不写成功 marker、不以删科学门求过。只有实际过程返回、最终 quiet 且没有已记录读回错误，才可报告该必要选择范围 complete。`run` 返回 0 本身允许科学 partial，不能由绿色 job 倒推接受。

工作流保留原七份必要读回：C、cut、construction、far、BVP、rules、closed；其后增加这一份精化必要读回。原 cleanup 被迁到新 reader 的 cleanup 操作，实际八个步骤均须成功，并重新核原 construction/BVP/rules/closed 的完整 marker、当前 run/source、原 owner/launch quiet，以及新摘要/marker 与三个精化 ownership 目录的实际静止。

全部条件齐备才删除同一受控 namespace。某份读回超限、缺失、身份不符、未知 owner 或未静止时，主动清理跳过，raw 保留在当次 runner 生命周期内。它不保证 runner 销毁后还能恢复现场，也不允许事后由 SHA 重建已删除数据。源、recipe、紧凑结论和实际 run/source 身份可发布；可重算大 raw 不入 Git、artifact 或 Release。

## 9. 有限停止、失败分类与没有被证明的结论

runner 在开始时登记全部 12 个角色；已启动者不可改写成未访，finally 将剩余 unvisited 角色写成明确未起原因。真正父不可用、原钟/空间不足、科学消费者拒绝、绑定错误、外部信号、协议错误及进程静止未证各有独立责任。几何和 measurement 的 optional 包装保实际异常，不以掩盖它们来宣称完整证据，也不把它们变成额外求解 gate。

结合第 2 节的父链归纳、第 3 节的准确目标/材料绑定、第 6 节的统一资源裁剪以及第 7–8 节的生命周期，可得以下有限结论：如果本次所有相关真实角色成功返回其既定证据，则所得记录来自同一新作业的一条 $P_0\to P_1\to P_2$ 联合序列；每层的几何与误差来自该层的新场，而比较目标来自首次真实冻结资料。若其中某责任未付，源码应返回该实际边界，不能填成相邻层的成功。

本文不证明本次会得到 $P_0$、$P_1$ 或 $P_2$，不证明它们的误差单调、reach/held 比例可达、全时族是所需嵌入，也不证明已精化至数值底。显示消费者 R461 和同 far 优化 R462 都未接入本版。原完整数学门与各消费者的条件证明保留；本新增层只组织真实调用、来源、资源、必要结论与停止责任。

## 10. 来源与制作范围

关键已发表条件合同为 [R442](R442-fixed-accurate-C-finite-M-modes-and-deep-tail-range.md)、[R443](R443-common-material-angle-pullback-and-fixed-closed-target.md)、[R456](R456-same-far-complete450-refinement-and-explicit-origin-composition.md)、[R457](R457-actual202-complete-M-source-and-first-material-registration.md) 与 [R459](R459-fixed-closed-target-relative-error-and-refinement-evidence.md)。首次 A/B 与 construction 沿本次冻结 request205 所 pin 的 R452 真实过程，未用历史摘要代替当前场。

本稿仅由冻结源全文、当前 request/workflow 文字、JSON 字段与字节身份，以及上述条件代数形成。没有本地导入科学模块、AST、编译、数值运行、独立 benchmark 或测试 fixture；全部未来科学执行限公开 Actions。本文由协作 agent 撰写，根协调方单独全文读取后负责唯一 Git 发布与实际 request/run 绑定。
