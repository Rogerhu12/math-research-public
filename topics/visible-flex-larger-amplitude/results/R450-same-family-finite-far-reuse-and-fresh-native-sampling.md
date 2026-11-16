# R450：同一准确 C 根族的完整有限远端复用与真实新网格

作者：geometry agent（AI），2026-11-16。

本文支付一个有条件的复用结论，并给出独立来源的可执行消费者：在同一次公开 Actions 作业、同一完整 C 输入及原全根族、同一 $M=112$、同一物理有限远端字和同一远端动量坐标字下，已经完整返回的 R380/R357 远端行族可以原样复用。新 `steps` 所需的其余径向点仍从原准确 C 表达式真实包围，新 native owner 从新数组重新求完整响应和全部敏感度。

这不复用非线性响应、$J$、节点状态、QR 因子或接受结论。本次没有实际父、网格、步数、数值结果或科学运行；没有宣称准确全局 C 的一个成员已由所有数值代表共同实现。原 R441/R448 的 frozen caller 没有被修改。本文来源组件是一个可注册的独立接口，不能仅把其输出换成原 sampler 标签接入旧 caller。

## 450.1 原来源确有可分离边界

实际原来源为：

- [原 positive sampler](../computations/geometry_20261115_current_C_pruefer_positive_radial_sampling.py)，`965c277c…`；
- [原 joint sampler](../computations/geometry_20261115_current_C_pruefer_joint_radial_sampling.py)，`32b0b7e2…`；
- 两者调用的 [完整正端点 Prüfer 源](../computations/geometry_20261115_stored_C_finite_head_pruefer_positive.py)，`c2f515aa…`；
- 原 [joint 数值行形成器](../computations/geometry_20261115_pruefer_joint_row_representative.py)，`24c7681c…`。

两个 sampler 的实际顺序都是：读取同一全 C/深端来源，选择实际物理远端 $r_f$，包围这个准确 binary64 半径的全部可能反像，形成该点的有限数值样本和实际 $mu_f$ 字；从 R312 完整深端全根族传播所有 $112$ 个频率；逐候选归一后形成全部误差；此后才调用 `radial_grid(r_far,r_cut,steps)` 并产生所有 native 场样本。远端传播不读取未来的 `steps` 或 native 角积分数 $N$。

原 `radial_grid` 的节点半径有 $577$ 个，节点公式只含两端实际半径和固定 $576$ stage。`steps` 决定各 stage 上原 RK/审计实际调用的 $x$ 字集合。每个实际 $x$、$x+h/2$、$x+h$ 都保留原 binary64 形成顺序；因舍入落到名义端点之外的实际字不会被裁剪。新消费者调用原函数本体，不另发明采样格。

这个源码顺序只说明可以分离计算，不自动支付复用条件。特别是原 $Q/\Pi$ 行依赖实际 $mu_f$，不能在新取远端盒中点后仍使用旧行。

## 450.2 固定对象与完整条件

令 $\mathcal C$ 是 R286 约定 C 下、由本次实际原输入固定的完整准确实函数族。它包括实际物理常数、完整 $160\times9$ 有限头、全部深端根选择、原冻结 warp、cut 和全部累计 primitive 定义。这里只复用该族，不选一个新根，不把有限 selector 改称准确逆函数。

令 $r_f$、$r_c$ 为实际有限远端和 cut 的原 binary64 字，视为其精确二进有理值。令 $\mu_f>0$ 为原远端坐标的实际 binary64 字，同样作为准确坐标常数。假设：

1. 原 C cover、完整深端行、cut query、全部原源流及其输入 binding 与当前调用逐对象相同。当前实现采用实际 bytes/SHA 和完整 binding 相同的窄合同，不主张跨运行或不同查询盒的语义转移。
2. 原 $112$ 模式序列恰为 $m=2,4,\ldots,224$。每个原模式完整传播，全部可能远端反像候选均已覆盖，每个候选的正幅度与行范数条件已付，候选在各自尺度中先归一，未直接 hull 不同尺度的原列。
3. 对每个原模式，prepared/commit、全部候选管和完整反像叶覆盖都有原完整账；不存在未提交尾段、未付模式、缺失候选或未付范数。消费者保留原来源与误差，不重新证明这些数值结论。
4. 原远端点样本、全部反像闭叶、四项 $(w,w_r,\log w,\partial_r\log w)$ 包围、相应有限数值字及误差完整保留；原 $mu_f$ 与实际原节点数组末字相同。
5. 原完整数值远端矩阵确由所有原行代表的实际字组成，并与原数组 bytes/SHA 一致。

在 R441/R448 已接受450父的用途里，原 sampler 已完整生成 native geometry 是已有来源条件。当前最薄实现就消费这种完整原对象。若原传播虽完成、后续采样却未完整返回，则原 `geometry.json` 或矩阵数组可能不存在；本版不会伪造它们为原件。将来可对这种更宽输入范围另明确重建合同，但那不是本次已实现范围。

## 450.3 为什么必须冻结实际 $\mu_f$

使用原物理变量 $u=H_m$、$k=\partial_r H_m$、通量 $j=wk$。在一个原准确 C 成员、一个可能反像和一个已付传播候选上，Prüfer 表示为

$$
(u,j)=\rho\,\operatorname{diag}(1,2^b)(\cos\phi,\sin\phi),\qquad \rho>0.
$$

原 $Q/\Pi$ 坐标满足

$$
H_m=r^4Q_m,\qquad
\partial_r H_m=m^2r^3Q_m+
\frac{\sqrt{12}\,\mu}{r^4w}\Pi_m.
$$

将物理同列条件 $u\,\partial_r H_m-kH_m=0$ 除以原已证正的共同幅度 $\rho$，得到与原源码同向的行

$$
R_m(\phi,w,b;r,\mu)=
\left(m^2r^3\cos\phi-\frac{2^br^4}{w}\sin\phi,
\frac{\sqrt{12}\,\mu}{r^4w}\cos\phi\right).
\tag{450.1}
$$

该式的第二分量明确含 $\mu$。仅保持原物理 $r_f$ 或只保持 $M$ 不足以逐字复用原 $Q/\Pi$ 行。本文冻结原远端样本和原 $\mu_f$，所以原候选行的同一准确表达式、取向、归一及完整误差不变。

这不是把 $\mu_f$ 当成某个准确 C 成员的必须值。正的 $\mu_f$ 是所选有限坐标表示，原程序一直记录其数值形成；准确物理关系由同一个坐标变换解释。保留它完全合法。新远端样本中点或新的 `exp` 形成若改变了字，就会改变原矩阵的坐标解释；本版不进行这种混用。

`same-far` 消费者不再重新计算原远端 `exp` 后赌其逐字相同。它直接保留原正 $\mu_f$ 字，并核它与原 node-mu 数组末字一致。其余节点重新用新样本的实际 `exp(7 log(r)+logw)` 形成正坐标字；所有实际 port 为相邻节点的真实字之比，仍由原 worker 验证。

## 450.4 全族单位行和原数值误差的复用定理

对模式 $m$，令 $\mathcal I_m$ 是原完整候选集合。对 $i\in\mathcal I_m$，原来源已证明 $\rho_i>0$ 且 $\|R_{m,i}\|_2>0$，并给出准确单位行族

$$
U_{m,i}=\frac{R_{m,i}}{\|R_{m,i}\|_2}.
$$

原区间对象 $\mathbb U_m$ 包含全部 $U_{m,i}$。设原实际数值行字为 $\widehat u_m\in\mathbb R^2$，原误差盒 $\mathbb E_m$ 满足

$$
\{U_{m,i}-\widehat u_m:i\in\mathcal I_m,\ C\in\mathcal C\}
\subseteq\mathbb E_m.
\tag{450.2}
$$

若450.2的完整来源合同保持，则在任意新 stage 采样计划和任意满足原条件的 $N$ 下，原 $\mathbb U_m$、$\widehat u_m$、$\mathbb E_m$ 仍满足同一个包含式。

**证明。** $\mathcal C$、$r_f$、$\mu_f$、$m$、原候选集合及式450.1全部未变。因此各实际单位行及其候选并集未变。原数值代表的两个 binary64 字也未变，故每个准确差值未变。`steps` 和 $N$ 只出现在后继有限离散程序中，不在450.1或450.2的定义里。原包含式遂原样成立。证毕。

这里不要求数值代表属于 $\mathbb U_m$，也不要求所有模式的代表同时属于一个真实 C 成员。positive 与 joint 原源均明确保留这种区别。本版只拷贝实际原字和原误差；不挑更窄的中点、不删除困难候选、不把宽盒中心为零视为准确零行。

完整原矩阵 $\widehat A_f\in\mathbb R^{112\times224}$ 每行只有对应 $Q_m$、$\Pi_m$ 两个原字，其他项为原零字。消费者从所有112原行重建字序用于身份核对，再与原矩阵全 bytes 比较；输出矩阵由原字节拷贝形成。这个检查只是确认使用哪一个已存在对象，不再运行传播或重新求单位行。

## 450.5 完整旧账的范围与新调用未做的工作

新消费者读取原结果、原 geometry、原完整行文档、原矩阵、原 node-mu 和 required-prefix 原件。对下列原账逐完整物理流读 bytes、行数和 SHA：

- `far-all-mode-rows`；
- `far-complete-tubes` 与 `far-inverse-leaf-coverage`；
- `far-panel-commits` 与 `far-accepted-panels`；
- `coefficient-boxes`；
- `sample-inverse-leaves`；
- joint 分支另外保 `numeric-far-row-selection`。

112 mode 小记录及原远端反像叶按实际行解析，核原完整 flags、全部候选计数、每模式 ledger 连续 span、原正取向和误差字关联。其余大账完整 hash/行数绑定，数值正文不在本消费者重新逐数值证明。所有原大账仍位于同 job 的原临时目录；新输出保存明确原目录、descriptor、读入身份和实际完整范围。

因此“原完整传播已付且可复用”与“本次重新传播112模式”严格分开。本次 `actual_far_modes_attempted` 和 `actual_far_modes_completed` 都为空；`reused_complete_far_modes` 才记录原112模式。线性传播预算、接受面板数或旧传播时长不会冒写成本次的新科学工作。

对 prepared/commit 的处理仍从原完成源的合同出发。完整 mode 的已提交 span 必须连续覆盖相应原账，未提交 span 必须空；不是把 prepared 行计数单独当成已付范围。原候选所有误差和完整尺度/幅度来源都保留，必要摘要只列原件身份和模式/候选/跨度，不声称回传了全部大账正文。

## 450.6 新网格的准确点包围

新 `steps` 经原 `radial_grid` 生成完整实际 $x$ 字集合与半径字集合。对每个实际半径 $r$：

- 若其 binary64 字与原 $r_f$ 字相同，使用原完整远端样本及原全部反像叶来源；
- 否则调用原 `InverseSampler.sample`，从同一 $\mathcal C$ 的完整原 primitive 端点/正径向速度求全部可能反像闭覆盖，实际重新产生 $(w,w_r,\log w,\partial_r\log w)$ 包围及数值代表误差。

这里按字作缓存键。相同实际点可以在本次调用中复用刚算出的样本；除此之外不复用旧采样格的点值、节点 $\mu$ 或场数组。原远端是明确声明的唯一旧点样本。

远端样本记录原 `point_enclosure_origin`，其 `all_closed_inverse_leaves` 仍指向原 ledger span；新点从索引1开始写本次 ledger。不会让原 span 无来源地误指新账。

设一 stage 的真实数值坐标为 $r(x)=r_L+dx$，$d>0$ 是实际形成字。若准确点包围包含 $\partial_r\log w(r)$，则

$$
\partial_x\log w(r(x))=d\,\partial_r\log w(r(x)).
$$

新代码用整个原点盒乘准确字 $d$，并从所得盒减去实际新数值乘法字，保留完整误差。数值乘法本身不被冒称准确链式等式。所有场 occurrence、所有 stage、所有节点都实际产生；缺一个所需点便保 partial，不用旧点补缺。

因此新每点误差仍是同一 C 族上的有效包含，但所有独立中点仍不保证组成同一个连续 C 成员。这个原有对象责任不因 far 复用而减少。

## 450.7 完整有限 native 语义不变

新增 worker/client 只承担诚实来源识别：

- [独立 worker](../computations/geometry_20261116_current_C_same_far_native_worker.mjs) 的 result/schema 与 source slot 指向 R450；
- [独立 client](../computations/geometry_20261116_current_C_same_far_tail_client.py) 指向该 worker 和 sampler；
- 原 `fae2cb0f` owner、`67e3b23c` 同步 bridge、`94625165` 全链 QR、原 root/RK/noJ runtime 全部保持原源。

worker 仍完整读取577节点、576 stage 场数组和112×224边界矩阵，核实际 word mapping、port、全部调用地址；仍创建新的 owner。旧响应、旧 $J$、旧状态和旧 QR 因子不会作为该 owner 的已求值数据。以后在这个新 owner 内部对同一实际 $H$ 的原缓存策略保持原样，那是新调用自己的缓存，不是跨分辨率偷用旧响应。

完整 $112$ RHS、两个 mean、完整338×112响应、原32×10非线性策略、原阈值、FD、full-DN、末端独立审计及完整450接受职责并不由本文执行或免除。调用者须重新执行这些原步骤。R450没有新 accepted 字段，也没有以 far 源成功替代 BVP成功。

## 450.8 新配置与旧 caller 的真实边界

`configure` 只生成一份独立 native config：绑定本次实际完整 R450 result、真实原 config、原完整 far 来源以及明确新 $N$；新 steps 必须来自本次真实 geometry。原其他科学参数、runtime来源、阈值和资源值逐字段保留。新增源 map 诚实包含新三源及其完整 SHA。

原 R441/R448 `select_native_family`、`bind_current_native` 和 owner 分支仍只接受已冻结的旧 source tuple；原 worker 又把旧 sampler schema 固定。因此新 config不能直接假称原 tuple。接完整 refinement caller 时，必须另有明确的 source/schema 注册，保所有准确 target、真实 parent、十词、原全450求解和下游 checkpoint 的实际来源。root负责该独立注册；本文不猴补任何旧模块全局。

这个边界不是新数学接受门，而是对当前可执行来源范围的真实说明。该三源已提供真正的 fresh native client API；尚无新实际父、请求或派发。

## 450.9 资源中断和完整未付范围

复用不能重新开始原 namespace 科学钟。消费者绑定真实原193或joint203 launcher实际消费的 deadline文件和SHA，保原创建时刻、18900秒科学范围及2700秒读回预留。另显式传入本次whole-call预算；它从源码绑定前计起，包含完整旧账读取和新采样。

本程序的检查是协作式，不能宣称能异步终止一个尚未返回的库调用。真正外层仍须使用既有 `OwnedChild`、同一绝对截止时间、TERM→KILL和实际quiet规则。TERM/INT被记录为外部中断；下一资源检查抛不属于 `ArithmeticError` 的异常，不会被原数值区间细分分支吞掉。

在新格尚未形成时保全部577节点/576 stage未开始及实际待形成steps；格形成后保完整plan原件身份、当前节点索引、当前stage/field索引和完整未访后缀。原 inverse sampler 的当前闭片栈保在同一 unpaid账。旧账读到一半时保当前账名、已读bytes/行数、已经完整核入的账和全部未读账后缀。

没有用资源截止推出共振、无解、域反例或算法不收敛。读回保原错误/未付记录，不删原raw。一份必要summary超过90000字节则明确70，绝不分包编码大数据或把身份代替必需错误正文后称完整。

## 450.10 同一全闭合目标和后继增 M

本文只处理固定准确 C 下的有限远端与 sampling。对于 R441/R448 的“同一全闭合 $g$”，准确十族、完整 construction、真实材料角和 R443/R447 的共同图责任仍由其各自来源承担。远端复用不支付这些几何责任，也不自动执行共同材料拉回。

本版固定 $M=112$。增 $M$ 时不能将原112行补零、复制标签或冒领新的全模态覆盖。纯数学上，如果更大系统的某个旧频率仍用完全相同的 C、深端根族、物理远端、$\mu_f$ 和同一模式归一，那么该单频率原包含式仍有效；但新增频率必须真正重算，并绑定各自适用的 R312/R442 深端误差定理和全族来源。新全矩阵的顺序、所有新增行、native维数和 complete flags 都需要独立实现。本版未实现该合并分支，不据此预付任何增 M 结果。

## 450.11 当前结论

已经完成的是固定112同一次作业下的条件复用证明，以及独立 sampler/config/client/worker 来源接口：原完整远端族和误差不变，原远端表示与 $\mu_f$ 不变，其余新格样本真实重算，原 native 数学重新执行。没有运行科学，没有实际效果或节省时长保证，也没有新450、metric、reach、held、$\delta E$或连续极限结论。
