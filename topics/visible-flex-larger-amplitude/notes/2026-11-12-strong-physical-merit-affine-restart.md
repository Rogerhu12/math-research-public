# q105：固定正坐标尺度与原仿射内层的精确恢复

## 当前状态与问题分类

旧 `disk-r2`（工具 session 4388）已经正式退出：工具码 137，资源包装器记录子进程 signal 9，wall 4749.0637369 s、CPU user 610.624152 s、system 24.600835 s、peak RSS 260752 KiB。没有发出主动中止；原因未知，不能从这些数据推断 OOM、时限或并行任务的因果关系。

它完成三次完整 Jacobian/磁盘 QR 和十四次原矩阵流式后向核验。两个真正接受的内层步长为 1/8 和 1/32；第三因子完成且 α=1 被原 merit 拒绝，但第三步尚未接受。没有完成新 H 的真实尾部复核，也没有实际耦合成功解。最后完整恢复点为已经逐字保全的 `disk-r2-saved-iterate-0003/...-iterate-0003.json.gz`，SHA256 `ace0a1ed3a1067ee1de3c13157bf81afe0aa0a90e4eb8b44751f05bfb4c669be`。它仍明确为 `solver_success=false`、`physical_surface=false`、真实耦合验收待完成。

新 `physical-merit-r3` 从该状态续算同一个 q105 问题。目标为 actual c2=0.105、c4=−0.006655700963004517、c6=−0.0004116733380408847，表示 gauge 仍为 0.09。M24/N768、tol=1e−7、最大2400点、完整73场与27参数、原始 RMS/BC/真实尾部/最终物理审计门均保留。

这里的“固定”指整个新运行固定一个正对角坐标尺度 S；**不是冻结度量 g 的谱精化**。δ、LB、vp 仍是实际设计变量，求解期间度量随它们变化。原物理方程不改，数值回溯接受准则明确改变。

## 为什么改变回溯的坐标尺度

两个已保存的完整原始状态之差能复现实际 Newton 方向，而不是只比较几个核心系数。第二步的原 merit 复现为 18308544847.65049，与运行记录 18308544847.650482 的相对差约4.44e−16；其中全场平方和仅0.06132695720981331。原参数的高频缩放很小，使 c20/c22 等原参数坐标主导欧氏平方和。

新尺度定义为：所有场坐标权重1；log(c2/gauge) 权重 c2_target/gauge；其余核心参数权重为已保存的物理系数尺度除以 gauge；δ/LB/vp 偏移权重1。27个权重均严格为正，并在整次运行中固定，不随 Newton 状态更新。对上述同一完整方向，固定 S merit 为0.06135659823737801，独立直接表达式一致。

代数依据见 `2026-11-12-strong-actual-newton-coordinate-merit.md`：在 Z=SU 下，J_Z=JS⁻¹，因此坐标变换后的修正为 S J⁻¹R。保留原矩阵求解，只以其固定加权平方和作 Armijo 比较，是明确的等价坐标范数选择。它不证明条件数改善、全步接受、全局收敛或曲面成功；原始误差与物理门仍须实际通过。

实现只替换原 owned Newton 的两处 `step@step` / `newstep@newstep`，保留原线性方程、domain 拒绝、迭代预算、停止阈值和检查点 observer。原矩阵的每次流式后向核验也保留。所有原文件不改，独立入口记录原源码、显式变换、变换后源码及新源 SHA。

## 恢复原 H0/K0/J0，不把旧响应充作新 H 审计

旧第一次内层的实际入口 raw 为 `exactraw-r1-iterate-0001.json.gz`，SHA256 `25565866efec651ae38fda64684b1a1c8d0f4c89f57ba2abe820800a04a9f18a`。原已完整审计的 H0 包 SHA256 为 `92989c9bbeb8514c4dd3e395a6b0527c850028727d8f9e9d17090914f2b6a186`，ready SHA256 为 `0f81b1eded8853d35804437aa80777c0134ad4202712da80194de6508b0efe47`。

新入口把这个原始入口与最新内层恢复点明确分开：

1. SHA校验原入口、最新完整 raw、所有 x/y/p 分块、各自原 config 和同一尾部数学参数。
2. 用实际约定 `tail_height` 从原入口末端恢复全部24维 H0，并逐位比较旧请求；没有额外相位翻转。
3. 通过原严格 recorded port 核对完整 source、ready、160层冻结校准指纹、完整请求与原 audit。
4. 原外层第一轮只在这里显式请求原 H0，恢复全部 K0 与74×24完整 J0；按原外层代码取其24×24斜率块作同一仿射边界。
5. 最新 raw 的不同 H 单独记录，并明确尚未在此审计。旧 H0 包不冒充它的真实响应。

当前恢复点 H2=−2.440976378536627e−5，而 H0,2=−2.4465375341970328e−5，两者确实不同。原内层返回之后的 `Hnew` 真实 full-H 求解、真实物理边界误差、8轮外层预算和最终 `audit=True` 原样保留。每个 changed-H 响应必须先完整存包，再释放 Node worker；相同 H 的已审计响应复用会显式标记源包，不声称又做了一次独立审计。

原 a84 入口仍以 `fixed_argument('--coupling','outer')` 强制外层耦合；传入 nested 会被拒绝，不会绕过这次原仿射恢复。

## 已做的实现核对

标准库 prepare（session37720，exit0）检查了完整布局、原命令约束及唯一源变换，不启动 worker。

随后 `strong_physical_merit_affine_protocol_check.py` 在真实已保存数据上完成五项检查（session54883，exit0，peak75220KiB，wall16.558s；内部计时3.260s）：

- 完整第二步方向复现原 merit，并与独立固定 S 表达式比较。
- 用实际 owned loader 加载原 Newton，并同时编译新 merit 和原检查点 observer 链；没有执行 Newton。
- 最新完整参数向量改变一个 binary64 位时拒绝恢复。
- 原入口高度相位错误时拒绝恢复。
- 原 Actual 外层方法作为明确的协议夹具编译，通过真实严格 recorded port 恢复完整 H0/K0/J0，在第一次 `solve_bvp` 调用入口以专用哨兵停止。

最后一项是协议核对，未构造新的物理解、未运行 BVP、Jacobian 或 Node；报告明确保留这些零计数。原完整 source/ready 守卫实际执行。夹具输出只是旧 audited packet 的明确复用，也不是新的数值审计。

## 可复现入口与活动边界

冻结命令为 `2026-11-12-strong-actual-q105-freeq4-m24-tol7-physical-merit-r3-command-plan.json`，SHA256 `2bc534d7adc77b90793dc33edb6336ab9ee9ed2ff45095c2ee86e6c0f43bcdbc`。它包含完整 argv、资源包装器、环境、源 SHA 和逐字恢复输入。正式新运行 session20793 使用这些原样配置。

入口 `strong_physical_merit_actual_bvp.py` SHA256 `11f3e91efaa52ec1daae63aac042576e84867e5ded7b1e8cff2b23721f8fe8a0`；运行适配器 `strong_physical_merit_and_affine_resume.py` SHA256 `e330336daab09ef9d0bcb93cb36e04581636e33e645ed5e319987c3cc0f2810f`。二者及所有原依赖在活动运行期间冻结。新运行的日志、检查点、sidecar 和最终包不列入这次静态源/协议清单；以后按实际接受步和正式终态分别保全。

本记录未声称 q105 实际耦合成功、固定 g 收敛、闭合 C²、reach 或题目完成。
