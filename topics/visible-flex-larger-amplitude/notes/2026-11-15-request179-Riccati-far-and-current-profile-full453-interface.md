# Request179：R375 全族远端传播、R357 取向单位行与真实 current-profile full453 接线

作者：AI。日期：2026-11-15。

状态：独立源码与运行合同已经形成，尚无本请求的实际求解结果。此文件不填未来 run、job、结果 SHA、接受状态或场数据。实际结果责任预留 R382。数学只在 Rogerhu12/math-research-public 的公开 Actions 执行；本次编辑只处理源码、已有文本字段、字节身份与解析推理，没有本地科学执行，也没有本地 Python AST、Node 或 bash 编译。

## 1. 本请求实际改变什么

本请求继承 actual169 重发版的五个数学输入、准确 R323 标量构造、初始九系数、三活动六冻结的完整 453 维 BVP、当前物理高度产生方式、原 FD、原 full-DN 和末次 fresh audit。它把物理远端传播从 R347 的逐面板二维矩形与端点 pivot 改成已经证明的 [R375 两图 Riccati 比较](../results/R375-continuous-C-two-chart-Riccati-comparison-and-cut-cover.md)。完整原深根族重新生成；不缩窄或继承 R358、R368、R367 已经很宽的传播盒。

物理远端的边界行继续用 [R357](../results/R357-original-C-oriented-unit-Robin-family-enclosures.md) 的完整候选取向单位行规则。每个候选先证幅度非零及其符号，再独立证原 Q/Pi 行范数严格正，再归一，最后对全部候选取 hull。这里不把端点高度除法变成新门。

此请求运行的是“新 R323 profile 产生当前 H → 同一 live worker 的完整 native/J → 原 FD → 原 full453 DN → 原 fresh audit”。没有另添一个零高度启动实验；首次 H 从本次新 profile 和完整初猜现场产生，数值与是否非零都不预填。177 的完整 cut-DN 主程序不在这里另跑；这里只复用其 R375 全族传播函数直到独立选定的真实物理远端。

原 actual169 来源为 commit de9a730a8f9cf8ea1f3e31fa6f6dd9cfb64e1d80、run 43741519736。其原实际停止及完整未付范围见 [R367](../results/R367-actual169-retry-new-scalar-and-unstarted-BVP-at-first-far-pivot-stop.md)。该运行的原数值数组、响应、J 和不良宽盒都不是本次输入。原科学源全部保留，本次六个运行源有独立名称与身份。

## 2. 冻结的源码、运行件与原闭包

以下 SHA 是 UTF-8 完整源码的 SHA-256。全部源码位于 computations/；完整 59 项直接来源表在新 request 内，driver 自身还核 52 项 PINS、26 项 NATIVE_PINS 及 7 项原运行模块身份。

| 角色 | 文件 | 字节 | SHA-256 |
|---|---|---:|---|
| Sampler | `geometry_20261115_current_C_riccati_radial_sampling.py` | 60,896 | `3216647087761aaf96a52e3748f64edbfe88dc0cc5aaba6b55f1cf5c778aa6d2` |
| Worker | `geometry_20261115_current_C_riccati_native_worker.mjs` | 18,264 | `600950b4bba88097005c45a515e9d8486161e6276250fb5849283b8e9a35d2e6` |
| Client | `geometry_20261115_current_C_riccati_tail_client.py` | 23,082 | `48764a4c4acceb70bc41c82af727c0a2be888f170095707478b3766ef74ac19e` |
| Driver | `geometry_20261115_current_C_riccati_full453_physical_dn.py` | 63,057 | `76c51a05c8ce40f78225aa3bfbd5db2b1ac39e0d6fb7f8b84f02e0dfaafd122f` |
| Launcher | `geometry_20261115_current_C_riccati_full453_launch.py` | 19,201 | `ed141b63e402d572552473cd69a7b19c6e55774c8f12fb89da54fa8e7b3c9029` |
| Reader | `root_20261115_current_C_riccati_full453_necessary_readout.py` | 50,768 | `1d0550377f8d506dadbb02b819a523bef81d9871ee683b0684d368b5897afe35` |

三件实际派发文件如下。workflow 位于仓库 .github/workflows/，两个 JSON 位于本题 computations/。只有 request 路径的普通 main push 触发独立 concurrency；本文件不触发、不修改分支，也不要求任何新审批。

| 角色 | 文件 | 字节 | SHA-256 |
|---|---|---:|---|
| Recipe | `current-C-riccati-full453-physical-DN179-recipe.json` | 10,294 | `d926cecf92f35cf4c7ae8cc86ad243287846d73df98c78e8ba1005c568ab8811` |
| Request | `public-current-C-riccati-full453-physical-DN-request.json` | 40,094 | `fa5cc945d7d714a20f85508e9289ce9fec3c2c0811e5bb6fbfe751f9d1601c75` |
| Workflow | `visible-larger-public-current-C-riccati-full453-physical-DN.yml` | 90,370 | `14352ae2211908c9ad7a4d4af25b10c6ac01d9b5fb5d57da8f920d7fd9c57782` |

R375 实际函数源为 geometry_20261115_stored_C_finite_head_riccati.py，84,732 B，SHA 34606e3fea2093f78cc3cb88fa6e5f7bcc32112c8f9053484628ad1a16e11124。R375 证明为 22,953 B，SHA c05a22becdc752bb87b7152761ae6b8ef02b30084bd09de62c7b305701609fec，已发布 58bbcda6c3af3a0e9afa7e8cbeedcd0873996f13。

其原 R347 源 5440e2e0457b360120c180a2531e3db899d8534cf6366183fd68d111ede18216、原 R324 源 4531b5b35093fa9c0010f9fdbd6700dcf4b099c076b5a3d69d20ccafda8af87d 继续作为真实数学函数依赖。相应 R347/R324 证明与 R375/R357 均在 sparse 清单，不能只改 request 的标签而漏取实际证明文件。

原完整 QR 前端 9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33、general-Robin QR 946251656306a6cbe137513e12bac305c7758e5ec7306995a63314bd0f400bb5、native owner fae2cb0fface7eadcc955fe09a07e9b59a7df8cd692bccc6cdf826c691eb8349、同步桥 67e3b23c9e5306764db3d6b8e0392eb8f59d4b63bfb671a0703fe33b2146c286 均逐字不改。原 noJ-matched 流 f9b292c4c3f80d1d7b3030ea0350416746795377833661af8d3095e349a73ad9 与原 Fourier root、product-J、cusp、physical-jet、metric 算法也不改。

闭包内保留旧 projective native launcher 与 native scalar helper 的来源项，是 driver 的既有显式身份合同；本请求不运行它们的旧启动或大日志分包入口。新 BVP reader 为标准库独立实现，不 import 旧 helper。新 workflow 的 rules 读回亦只调用新 reader 的标准库元数据函数。

临时 full diff、源级比较回执可重生成，仅供本次源码核对，不作为待提交数据文件或科学运行门。

## 3. 五个实际输入与完全相同的标量起点

五件输入只在本 job 临时目录恢复。历史公开 ref 为 8bd267107cc8710d371f3b62c02986655ac965b0，原路径、Git blob（若原合同给出）及全部 bytes/SHA 逐项在 request 中；原 input 不在 main 也不会改用近似或名称相近的文件。

| 角色 | 临时名称 | 原字节 | 原 SHA-256 |
|---|---|---:|---|
| calibration_ledger | `ledger-ready.json` | 109,004 | `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` |
| config | `tail-config.json` | 2,161 | `01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5` |
| stored_reference | `stored-ready.json` | 29,774 | `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d` |
| accepted | `accepted.json.gz` | 2,614,352 | `b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff` |
| complete_seed | `complete-seed453.json.gz` | 4,220,043 | `0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714` |

前三件生成同一个声明 C 对象及其六 primitive、原 binary64 cut 点、whole-natural-domain。后两件分别只供实际 core 与完整初猜；旧 metric、旧 RHS、旧 tail、旧 zero J、旧 accepted 标签不能转移到新目标。

完整初猜来自原 /mesh 与 /states，原 producer 明确是 699 节点、453 坐标，包含 338 个物理分量、112 个 core 坐标及 3 个标量活动变量。原 JSON 未保存的负零不冒恢复。新流程按公共 u 重参数化，保完整初值，重新计算本次 RHS、physical preflight、边界与实际当前 H；旧采样残差和旧参考尾不重用。

准确构造 entry 738dd352cf62fbd47eb80e867ac441b7d0c179074cbee93fb8dd6528ba0d4cb0、factory 0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e、numeric profile 7cfab12ebb8bf4a948336e7c605ea096a9597be43a4582f166f9067850ea4b60 逐字继承 actual169。原 atomic147 request 4b6f78bb25e0d87354e2ad786637fc9e4db5c7c34774d3cad4716638552ba707 的 construction、原九系数、参数来源、query 和五输入逐对象核同；只把本次上游 C 的明确墙钟预算维持为 actual169 的 3600 秒。

初始九参数，按 p1,p2,p3,theta1,theta2,theta3,eta1,eta2,eta3：

~~~text
[0.3055213835477326, 0.21645013203050154, 0.34270051957744246,
 -0.06322334619266512, -0.01747451701873286, 0.9376115689625685,
 1.0751306255033548, 0.6886900390922872, 0.9385431607625546]
~~~

这是 request146 原 final 的字面系数来源，不是已接受新目标。实际严格有限 cut 盒由同 job f12f v3 产生，再由原 R323 规则选择窗口；没有把旧运行的 cut 盒或长宽常量当新输入。历史已报告的 collar 1/524288、两个短窗 1/1024、kappa=1/2 只是原构造的实际识别依据；本 job 仍按同一实际公式重生并绑定。

当前已核定的 R381 严格速度反证适用于这一准确初始九参数对象；这不是“初点已合法”。coast 的参数支撑责任不能由新远端算法消除。179 继续让原 p1,p2,p3 活动，theta1..3、eta1..3 冻结；因 p3 仍活动，初点的反证也不是全搜索无解证明。本请求不新增以 R381 为前置阻挡的门；若将来某个真实末点被接受，必须对该末点承担准确连续域和 metric 的原责任。

## 4. 同一声明 C、真实物理采样与准确族范围

原 continuous E producer 仍是 f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df。声明 C 见 [R286](../results/R286-original-stored-continuous-integral-and-metric-bridge.md)；完整 cap 端点优化和 partial 包装沿 [R306](../results/R306-complete-cap-endpoint-primitives-and-budget-preserving-integration.md)。160×9=1440 原片、全部六 primitive A/B/sqrtE_A/sqrtE_B/w_A/w_B、准确深根族、原 q/cap/cusp 分支、闭端点、原头部累加、自然 Rout 的语义都保留。

原 query 两项原顺序保留：首先是 config 原 binary64 rCut 的闭点，其次是 whole-natural-domain；不是重标半径或使用名义 cut 重归一。原 point reader1c39b242…对全部原 inverse leaves 的 E/E_r/E_rr 做原完整 hull。原 C 未付或 point 未付时，不造 cut jets、factory、far 或 native 成功。

原深端 producer fe66789e7d94ab014662250e90642ab7fda3084b39c00b93836459220b33bb2a 仍从同三原输入生成 R312 全部 112 模态的准确根族。m=2,4,...,224，F=159、物理深节点160。原未选定深根族仍未选定，不用旧 ready graph、旧 gain 或旧 finite48 尾替代。

sampler 在整个 node8 半径盒之外选择同一个实际 binary64 rFar，保存原选择条件和字词。到该 rFar 的所有可能闭 inverse fragments 必须付全；传播全深列到该物理点而非把网格索引当物理 r。原 cut、rFar、每个 shooting node 与每一个 RK field 位置均保真实原字词和同场区间来源。

采样器仍输出完整 577 节点、576 阶段及每阶段全部原 field，原 x 坐标字词、r、dr/dx、log w、dlog w/dx 的列顺序不改。C 的严格区间负责包含各个对应准确量；各数值代表、exp/log 与原 worker 进一步运算仍是声明的有限数值映射，不声称这些代表同时来自准确 C 族的某一共同成员。数值误差、连续 target metric、无限非线性尾误差不会由原 native 残差自动支付。

## 5. R375 传播怎样准确进入原 R357 物理行

同原 x 方向，连续通量坐标为 $Z=(u,j)$、$j=wk$，$k=dH/dr$。在每一个固定 balance $b$ 的面板内，保

$$
Z(x)=a(x)\operatorname{diag}(1,2^b)V(x),\qquad a(x)\ne0.
$$

R375 的两图 ratio、准确有理极值系数、两条全闭时段 comparison barriers、原完整初盒和 Taylor 余项均保。只有整个闭时段辅助分母的严格正性付清后，才把 ratio 与幅度管记为已付。真实 ratio 本身不假定单调；只使用已证明的自治 barrier 单调性。闭系数族、根不确定性、原 C 与继承误差不能丢弃。

本 sampler 不把新的幅度误记成旧 R347 面板内的常数。prepare_far_tubes 保存

$$
a(t)=a_{\rm in}\exp\!\left(\int_0^t\gamma(\xi)\,d\xi\right)
$$

的 incoming log、整个闭时段 log 包围、完整 log-rate 盒、幅度 sign、原因子数及因子链 SHA、当前图和精确二幂变框。面板内幅度是同符号非零函数。切图只发生在合法端点；原 reciprocal 必须对整个 ratio 区间隔零。

在固定候选里，以原 rFar、原正坐标 mu 和物理频率 m 构造原 Q/Pi 行

$$
R_Q=-r_{\rm Far}^4 k+m^2r_{\rm Far}^3u,\qquad
R_\Pi=\frac{\sqrt{12}\,\mu}{r_{\rm Far}^4w}u.
$$

这里的 u,k 是 R375 归一后的完整候选管，原传播列对应同一个非零 a(t) 倍。R357 给出原 QF=1 列的取向单位行

$$
\widehat R=\operatorname{sign}(a(t))\,\frac{(R_Q,R_\Pi)}
{\sqrt{R_Q^2+R_\Pi^2}}.
$$

该规则逐候选先计算：幅度 sign 已付与范数严格隔零分别记录；它们不能相互替代。严格范数条件未付就保该候选 partial；不借真正解非零或某个中点非零推断整个盒可归一。所有候选各自有包含的单位行之后，才对相应两分量取 hull。因此不需要共同非零高度分量，也不把不同幅度的原列直接 hull。

完整 112×224 原边界矩阵中，第 m 模态行只在其实际 Q_m、Pi_m 两列写入本次明确数值代表，其余所有列保零；全部 112 行都必须形成。每个行代表、原 f64le、真实区间及“准确量减所用字词”的误差盒原样记录。两代表同时被 round 到零时诚实失败，不捏造可用边界。单位行盒的一个中点不被宣称为一个真实全局 C 成员，数值代表的长度也不被宣称在二进制算术中恰好为1。

到 rFar 的范围与177到原 cut 的范围不同。179 不输出已付 cut-DN 图，也不继承177未来可能的非零分母结论。两处使用同一 R375 解析函数不等于两项实际数值覆盖相同。

## 6. 面板事务、误差与 partial 范围

原候选事务边界保持。far-accepted-panels 是 prepared 记录；只有 far-panel-commits 完整写出并实际推进 last_paid 的区间才属于已付前缀。coeff、barrier、完整管、unit-row、inverse-leaf 的相互行引用与完整 SHA 继续存在于 Actions 临时账。

若系数范围、barrier 全段存在、范数、Taylor work、inverse 分裂或资源在中途未付，保当前 incoming state、最后未接受 candidate、完整在途事务、DFS stack、当前原面板区间、全部原未访问 suffix 和未开始的模态。零宽闭交集/公共端点不被删成开覆盖。所有 leaf 的完整原闭区间责任按原覆盖账核；无最大最坏列表冒全覆盖。

原 max-depth=32、norm work=1/2、Taylor24、local-defect-bits12、cache65536 均保。R375 下 local-defect-bits12 的明确意义是 barrier Taylor 列误差工作目标 $2^{-12}$，完整矩阵余项仍乘整个初向量范数；它不是旧 midpoint Duhamel 相对误差标签。准确系数变化由比较原理包含，不能以“小 defect”理由省略。合法粗包围与工作精度未付分开。

R375 类型标志 needs_barrier_split 代替旧 needs_pivot_split，并使用实际 barrier 计数和停止原因；sampler 的 point_column 在这些新标志上处理分裂。数学对象、原几何缓存、全部采样计划、原资源计数和事务推进未改。no-pole 未证、row-norm 未证或预算截止均不推出共振、真实零列、无解或 BVP 拒绝。

## 7. 原现场 native 与完整物理 BVP 合同

新 worker/client 只改变 sampler 名称、source pin 与 sampler schema；原运行协议、完整 state shape、负零恢复、当前 H SHA、独立当前输入绑定、原 cut target/scale 坐标、缓存/预测器与 full native owner 的数学函数不改。

真正当前 residual/J 每轮从原函数 fresh 形成。非线性 correction 仍用 eta=1 的完整 general-Robin 方程；末端112 RHS sensitivity 用 eta=0 的原完整方程。全部577节点/224坐标、cut112、stage576×224、far112，共129248原方程完整保留，sigma恢复不投影 cut 顶半，也不删 far 行。QR 大因子、纯常数行、完整 delta 和 sensitivity 暂存；浮点非零 pivot 不冒严格非共振。

原接受仍32轮、每轮原10档严格 norm 下降、tol=2e-9；guard 与全部原 noJ 试步不变。eta=1 没有进入最终 eta=0 导数方程。原338×112端点 jet、mean、真实 final J 与 fresh audit 的作用不因换 far propagation 被省略。

本次 BVP recipe 的 lambda=0.001、height_sign=-1、物理频率112、角度4096、场 quadrature2048、338物理+112core+3active=453、左341/右112都保。原 FD 的3种扰动、两级四阶 Richardson 和5e-5门保留。原 inner17试探、outer8、max_nodes1200、RMS1e-6、BC1e-11、frozen-physical RMS、末 fresh native audit 全部保留。

current profile 的真实端点 RHS 和 MaterialTrace 生成完整112 H，再由同一个 live TailClient 返回本次响应/J。原5项 cut 数值比较保留，不从 profile 覆盖 native 返回 jets 来伪造相等。相同 H 的原非audit缓存可用；audit=True仍强制真实独立 native 调用。首个 H 若与任何历史值不同，实际调用新的求解，不能重标旧 response。

native 或 BVP 在上游完整几何未付时不启动，记未启动范围；它不等于实际十档拒绝。原 same-g450 refinement、准确连续 metric、闭场、C2 seam、reach、held、finite-t 条件均不由某一次有限 BVP 成功自动成立。

## 8. CLI、同 job 路径与实际来源

sampler 继续原参数接口：

~~~text
geometry_20261115_current_C_riccati_radial_sampling.py
  --cover-directory <base>/continuous-E --cover-result-sha256 <actual>
  --far-directory <base>/deep-far --far-result-sha256 <actual>
  --code-directory <computations> --proof <actual R375>
  --unit-row-proof <actual R357> --out <base>/current-geometry
  --precision-bits 256 --linear-budget-seconds <actual clipped>
  --sampling-budget-seconds <actual clipped> --max-panels 25000000
  --free-bytes-reserve 2147483648 --max-depth 32 --local-defect-bits 12
  --panel-norm-limit 1/2 --taylor-terms 24 --max-geometry-cache-records 65536
  --sample-max-nodes 1000000 --sample-inverse-depth 24 --sample-value-bits 32 --steps 12
~~~

所有 actual SHA 在同 job 原文件生成后立即读原字节形成。入口没有接受未来结果 SHA 的占位常量。精确三输入和当前 cover/far binding 保原根族与目标；旧 ready 未改名成 C。

launcher 接 --recipe/--recipe-sha256、原 accepted/sha、完整 seed、当前 factory/result SHA、当前 tail-config/SHA、原 restored source-topic、computations、job-deadline 与独占 out。其 driver 内仍保唯一 client owner。launcher 的 SIGTERM/SIGINT 捕获、向自己 start_new_session 的子组传播信号、确认组停止、保存原现场均沿已修源；external interruption 与资源截止、数学拒绝分别记。

必要 reader 接：

~~~text
root_20261115_current_C_riccati_full453_necessary_readout.py
  --launch-directory <base>/BVP-launch
  --sampler-directory <base>/current-geometry
  [--sampler-result-sha256 <actual>]
  --computations <computations>
  --out <base>/BVP-scalar-readout
~~~

base 独占名为 visible-current-C-riccati-full453179。sampler 的新 schema 是 current-C-riccati-physical-radial-samples-and-general-far-v1；generic native geometry bundle 布局 v1 未改。driver 和 recipe 分别是 current-C-riccati-R300-v3-three-active-complete453-physical-DN-v1、explicit-current-C-riccati-R300-v3-three-active-complete453-recipe-v1。

## 9. 真实资源计划，不保证全部完成

| 范围 | 明确计划 |
|---|---|
| 单 compute job 硬限 | 360分钟 |
| namespace计划科学时间 | 18900秒，从本 namespace 建立时起计算 |
| 计划读回余量 | 2700秒；不是无条件保证 |
| 原 C 重建 | 3600秒，原1440片/6primitive，step75分钟 |
| 原 factory | 两次各300秒 domain pass，原65536/32，step20分钟 |
| 原 point twojet / deep | step10分钟 / 5分钟 |
| 远端线性共享预算 | 14400秒、25000000次原work、32depth |
| 后续点采样 | 1800秒、1000000 sample nodes |
| 采样 step 硬限 | 285分钟 |
| 完整 BVP 进程预算 | 7200秒；step135分钟 |
| 原 native QR child | 1800秒、factor上限2147483648B |
| 初始临时盘 | 明确至少32GiB资源检查 |
| 运行空闲盘保留 | 2GiB |
| 原数值运行 | Python3.12.14、Node24.22.1、numpy2.3.5、scipy1.17.0、python-flint0.9.0 |

原规则 runner 每2700秒真实同步并核 README。科学子进程移除 GitHub token；规则父进程单独持 token。原 argv 以结构化列表传递，不加会截断参数的内部 bare --，不通过 shell 解释科学参数。

采样入口在实际 rules startup 之后算剩余 $T$，先预留7200秒给原 BVP，再把线性14400与点采样1800乘共同系数

$$
c=\min\!\left(1,\frac{\max(0,T-7200)}{16200}\right).
$$

原参数与实际 argv、clip、时点都有原收据。采样源内部时钟仍排除其 source binding/runtime setup；namespace对前面 C/factory/sampling是启动时资源计划，不是覆盖全部阶段的绝对 kill 时钟。BVP launcher 一旦启动，确实同时执行自身进程预算和该 namespace 的剩余 deadline；外部 step/job 限制仍实际生效。2700秒只是预留计划，绑定、规则同步和外部截止都可能使读回无法完整完成。

18个协议入口是原 full-DN 路径上界说明，不是新增 call gate。一个 native call 的存储账不能当成全部 outer/call 容量保证。所有磁盘/时间/work中止均如实 partial，不能改成数学不可解或删去模态以凑完成。

## 10. 必要读回、遗漏范围与有条件清理

新 reader 只导入标准库，并实际核六个本请求 source pin。它在 Actions 内读当前原 JSON、JSONL 和完整二进制字节；它不重算 RHS、J、QR、exact row、Arb 包围或任何科学极值。

一份 BVP 必要摘要 schema 为 current-C-riccati-R300-full453-necessary-scalar-readback-v1，BEGIN/END_REQUEST179_CURRENT_C_BVP_NECESSARY_SUMMARY。canonical ASCII UTF-8 JSON含末LF，bytes/SHA同时输出；GITHUB_OUTPUT仍使用 bvp_summary、bvp_summary_bytes、bvp_summary_sha256。上限90000B，不能将大 payload切片或编码成可重构运输。

其返回范围精确定义如下：

- sampler的实际结果、输入绑定身份、每个原mode状态/counter、全部当前 pending/suffix/未开始频率、全部未付 inverse leaves；prepared/commit/coeff流只完整字节与行数身份，不冒独立逐值科学审计。
- 若全部112 general far rows实际存在，逐原行保两系数准确 dyadic端点、actual_word中的value/f64le、difference_exact_quantity_minus_numeric_word的原display及行身份；不重新形成它们。
- 原完整成功候选管/矩阵/因子链继续临时存在并读身份；返回范围不搬运全部大见证。barrier失败保必要原闭分母/初值/区间/停止点与全未付栈。
- 所有已存在 native trace/trial JSONL 在 Actions 内逐行解析；摘要返回每次实际call的终态、原计数与该call末次实际iteration全部trial。此前迭代的完整trial细节不返回，完整源流身份保留，不能据此声称 chat 逐条审过全部历史trial。
- 每个 actual linear child 的原结果/exit/失败、全部 RHS 的原数值最大残差字词、已有 exact direction 原decimal极值与位置都保；全577state、338×112J、大factor与allrow账只读原描述符/完整SHA，不在摘要重构。
- 原 BVP outer_history、完整原 FD 的必要方向/level误差、真实初末H、原5cut比较、可用的final audit和实际末参数按源字段选择；字段不存在就保未返回，不填成功或把未执行层视为零误差。
- Python/Node/linear完整日志都读原字节身份；只输出必要的首次/末次实际exception/traceback/signal/storage错误行。完整大stdout/stderr不再按12000B分段返回。没有被选中的错误文本不是“没有错误”的证明。
- 坏JSON、未终止尾行、读取失败均保原byte/SHA与有限原文excerpt，并记录读回错误。不能只写摘要hash随后假完整；也不将大坏文件分块返回。

正常摘要完整且无读错时才写 <out>/readback-complete.json；任何必要读取错误exit2、上限溢出exit70，均不写该marker。超限只报告真实完整摘要bytes/SHA及明确未输出范围，不静默删trial来冒完整。它是传输/读回失败，不改变已经发生的科学结果。

原 C、point twojet、construction、deep四份既有语义摘要独立保留；report job只重复这些实际小primary和本次BVP必要primary，不组装一个新的总大JSON。construction 的正常 original147 primary不变；其中断fallback改为必要已存字段和完整文件身份，超限exit70，不再 data=chunk 分段。规则/资源元数据有另一份必要摘要，科学大日志只身份与必要错误excerpt；它不是BVP大数据的分包替代。

清理前仍要求实际六个readback步骤都success、BVP新marker及rule marker同run/source、摘要SHA精确吻合，然后再次观察所有已登记科学进程。父Python只以 PID/start_ticks核，不要求继承的runner共享PGID为空；科学组只有已证 start_new_session 的自有PGID才检查全组。BVP独立组必须已有launcher真实停止回执。

任何读回超限/错误、活流、unknown owner 或缺marker都不主动删raw；保到runner销毁。允许清理时只删本179独占base，不动其他请求、源仓或原历史对象。没有artifact/Release/raw Git发布。原始大数据不会作为“审计通过”的伪证留在main。

## 11. 源级变更与实际执行界限

sampler相对b290的改变限于新runtime/source/schema/proof，R375整管幅度a(t)表达，needs_barrier_split的实际分裂标志与相应报告字段。16个原定义逐文本保持，尤其R357单位行本体、OwnedBudget、InverseSampler、choose_far_radius、finite_point_required、radial_grid及原raw数组写法。已交完整14,249B差异，不能把这段文本比较说成运行过的新科学。

worker/client/driver/launcher相对actual169的完整11,434B差异只接新basename/pin/schema及本179 deadline身份；原数学函数与实际ownership/信号处理不变。reader是独立标准库必要摘要，实现方式改变不改变原科学条件。

workflow源级自检只在Actions执行：实际59 source全部SHA，Python AST/编译，Node --check，全部inline Python heredoc编译与bash -n，原proof/input/query/recipe/current README核，精确恢复原5输入与一次public78源。不会把这些步骤伪称已在本地通过；本次已经做的只是文本闭包、字段、SHA和原JSON对象比较。

这套源码不保证R375一定让全部barrier在既定depth下可付，不保证112单位行都隔零，不保证native启动、线性非共振、正lambda BVP接受或准确连续域成立。真正返回后，按原source/run/参数、已付/未付范围与原门逐项记录；不据新method的证明把未来数值成功预填。
