# Complete-model-covered soft ordinary growth：首次公共实际结果

日期：2026-11-15。撰稿：tail_cost；原日志单次下载与原字段摘录：root。本文只消费已经完成的一次公共运行，不执行新的开发检查、优化、几何评价或旧阶段重放。

## 1. 结果与归属

公共 run **43762868037**、job **132961344492** 于 **21:23:36 UTC** 成功结束，计算源为 **4f1365300b70831550d544df119d738b2531eff5**。

本轮从上一真实最优 checkpoint 继续，共完成六个模型：四次普通完整步接受、两次原 same-layout SOC 完整步接受。两网最大 metric 指标从

$
0.2663015219132816
\quad\text{降至}\quad
0.2662701215525791,
$

实际下降 **0.000031400360702482644**。末点两网最大曲率为 **57.99998346840656**。全部原两网验收门与原精确物理盒通过；新的 metric 目标 $0.26$ 尚未达到。

必须区分三种控制器行为：

- **实际发生了一次旧普通步增长。** 源 checkpoint 的 legacy streak 为 1；模型 1 形成旧规则的成功 pair，将 $B$ 从 $0.000125$ 增至 $0.00025$。模型 2 的真实 factory 和两个 primary LP 使用了这个半径。
- **实际发生两次旧 same-layout SOC 保半径。** 模型 2、6 的普通步分别在曲率门失败，随后完整 SOC 接受。旧 17 条件全部满足，原本将减半至 $0.000125$ 的下一半径保持为 $0.00025$。
- **本次新增的 covered-soft ordinary-growth 规则没有提出额外增长。** 四个普通接受模型通过新覆盖资格，但它们新增 soft ID 数全为 0。新规则的增长提案、后继 factory 使用、后继 LP 使用均为 **0**；原 expanded-layout hold 的合格次数也为 **0**。

因此，这次结果证明新代码在这条真实轨迹上完成了执行、保留原学习与 fallback，并准确记录了控制器行为；**不能把本轮下降归因于新增 covered-soft 规则，也不能把旧增长或旧 SOC hold 改称本次新机制的收益。** 不为等待该新规则触发而重复本阶段。

原始运行：[Actions run 43762868037](https://github.com/Rogerhu12/math-research-public/actions/runs/43762868037)，[job 132961344492](https://github.com/Rogerhu12/math-research-public/actions/runs/43762868037/job/132961344492)。

## 2. 原输入、源码与审读边界

本轮新阶段唯一的继续点来自已完成的 SOC-pair run **43758666042** / job **132948276657** / source **aca67097b60b7eacdcf20798395ce6d4d1ab2845** 的完整 future checkpoint。入口还读取原24份已完成输入以恢复原定义与参考；没有重跑该阶段或其任何前缀优化。

源配置保持

$
\text{max LP}=12,\qquad
\text{shared full values}=40,\qquad
\text{active seconds}=120,\qquad
\text{per-LP seconds}=10.
$

原 $g,b_0$、参考 complete163、独立159坐标、精确物理163映射、原盒、两网定义、学习规则和门的容差保持。source configuration SHA256 为

**b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6**。

输入包含完整有序 **59 条 norm bank**，两个完整原行池 **4432 / 4358**，半径 $B=0.000125$，legacy streak **1**。新增 covered streak 从 **0** 开始，不把历史模型追认为新规则成功。

源码合同为旧 **130** 份冻结科学源码加本次五份新增 Python 文件；新 request 另绑定五份 workflow，共 **140** 项。运行入口按 request 对每个所绑定文件核 SHA；paid 四组19检查的 source closure 必须与原 COMPLETE 的130项完全相同。实际入口已逐项核对：request 的 **140 项** source_sha256（135 份 Python、5 份 workflow）全部匹配；COMPLETE 的135份 Python 按 basename 标准化后与 request 中的 Python 子集全部相同。旧130份闭包记录 **all130_frozen_sources_match_current_files=true**。初始同一精确状态的 coarse/fine $\eta,\kappa$ 差均为 **0**；原配置、$g,b_0$ 与 permanent anchor 均未改变。

新输出 schema 为

**same159-current-best-complete-model-covered-soft-ordinary-growth-v1**，

阶段键为 **covered_soft_ordinary_growth_stage**，成功状态为

**complete-two-grid-covered-soft-ordinary-growth-audit**。

### 2.1 元数据

根仅下载本轮原 job log 一次。由于 agent 的函数 stores 隔离，本文作者通过根传递的原数值字段摘录，独立核对模型之间的计数、状态迁移和费用关系；下表原字节长度与 SHA 来自这次唯一原日志读取。没有第二次下载，也没有将日志或 checkpoint payload 写入 Git。

| 原件 | 字节 | SHA256 |
|---|---:|---|
| 原 job log | 5,818,416 | bd49ef570ab38e23af4bdbe47d71d567cca76d9add2d91d4953fe40ed34b5842 |
| COVERED_GROWTH_COMPLETE，不含行尾 LF 的原 JSON 正文 | 1,223,174 | 3e5e672f6569ee532740c737e54691fa80df305343821aa6d1b5b9629733af67 |
| COVERED_GROWTH_DEVELOPMENT，不含行尾 LF 的原 JSON 正文 | 18,219 | 04ede9feafc357a742bf97516dd9ea52a991d9300050cab94e05e6b2da6f28ca |
| COVERED_GROWTH_PRIOR_WORK_REUSED，不含行尾 LF 的原 JSON 正文 | 54,925 | 40869ef064fe85511dabfc401e6c27e74def1b2945a14dfdd8ff0eca8c07c577 |

原 REQUEST 记录为 **37,359 B**，SHA256 **8c720549a3ccbbc41e0597114abeff8b009e75eb2ae5bfaff05c7befd59a76db**。

### 2.2 本轮真实规则读取

本轮 public `git pull --rebase` 从 **21:18:02.368129** 至 **21:18:03.949586 UTC** 执行：

- Before：**4f1365300b70831550d544df119d738b2531eff5**
- After / 实际读取 HEAD：**a76ececa7caf544f07a6cc942f8dd22a4fcb619c**
- 根 README blob：**21bd547f56590b7f2dd279d0297efb289a9b2783**
- 本题 README blob：**d0432faff569c8e9af7ed4809847e12880976c11**

两 README 差异均为空；readmes_match_expected、passed 均为 true，returncode为0。原 git stdout 为1048 B，SHA256 **93eb63b1486c782bb2e16b5ec0901030153a0b39a3c499bfbbff09ca1f4b9ea2**。计算 source 与实际拉取后的 read HEAD 分开记录，没有把后者冒作计算 source。

Private 规则同步从 **21:18:05.743152** 至 **21:18:06.218539 UTC** 执行；before=after 为 **022973cf3fbd92e7fa7507c6c9311ff40d078e89**，根 README blob为 **5ba164843b1f5802184178a82d786264404873a3**，私有对应 topic 不存在。原规则 unchanged，QUEUE_unique_and_ongoing_for_this_session=true。这里只记录规则和会话状态元数据，不复制私有正文。

## 3. 新开发与旧证据复用

四组新增检查全部通过，共 **20 项**：

| 新组 | 项数 | 实际结果 |
|---|---:|---|
| complete_coverage_and_final_binding | 5 | 全部 true |
| two_streaks_and_frozen_fallbacks | 7 | 全部 true |
| actual_step_repaired_return_and_identity | 4 | 全部 true |
| fifty_nine_checkpoint_and_explicit_entry | 4 | 全部 true |

检查覆盖最终两次 factory 后的模型签名、实际 $d=y-x$ 已完成缓存、完整原 soft 域及 ID 类型/顺序、两 streak 和 at-cap 消费、原 fallback、repaired inexact 返回范围，以及直接59条 checkpoint 构造。它们是人工数组/接口检查，不是物理曲面或 LP 成功证书。

本轮这些开发组的 LP、几何、科学 JVP、优化器及旧 developer-suite 执行次数均为 **0**。原 SOC-pair 的19项、更早 hold 的26项，以及 m10、expanded、正/负 cache 的已付证据，都通过原日志和冻结源 SHA 复用；这些旧组、新旧历史优化与事件重放均未再次执行，也没有再下载旧 m10 日志。

人工网格本身为 coarse $4\times4=16$ 点、fine $4\times8=32$ 点；其真实接口保留163×159物理映射与 coupled LP 数组。正常通过全部组的源码路径建立26个新增完整 context fixture，另调用两次既有人工数组构造数据。每次构造包含准确有理高度基与身份 hash，因此本文不把整体开发成本称为可忽略。

日志中的 PRIOR 时刻 **21:18:08.648** 到 DEVELOPMENT 时刻 **21:18:09.842** 相隔约 **1.194 秒**。这是开发、import、源码 hash 和周边输出的时间包络，不是单独 developer 函数的精确计时。

## 4. 六个实际模型与两条 streak

下表 $(\ell,c)$ 分别表示 legacy 与新增 covered streak。所有接受 trial 都是原完整 $\alpha=1$，没有把回溯或局部修正标成普通完整步。

| 模型 | 模型 B | Primary / SOC LP | 接受方式 | 接受后两网最大 η | 接受后最大 κ | $(\ell,c)$ 前→后 | 下一 B 与依据 |
|---|---:|---:|---|---:|---:|---|---|
| 1 | 0.000125 | 1 / 0 | 普通完整步 | 0.2662980311209849 | 57.99998620492234 | (1,0)→(0,0) | 0.00025；旧 legacy pair 实际增长 |
| 2 | 0.00025 | 2 / 1 | 同布局完整 SOC | 0.26629407673622385 | 57.999983429335074 | (0,0)→(0,0) | 0.00025；旧17条件 hold |
| 3 | 0.00025 | 2 / 0 | 普通完整步 | 0.26628684231789823 | 57.999999689327986 | (0,0)→(1,1) | 0.00025；记录一次成功 |
| 4 | 0.00025 | 1 / 0 | 普通完整步 | 0.2662808023276887 | 57.99999616871111 | (1,1)→(0,0) | 0.00025；旧 at-cap pair 消费 |
| 5 | 0.00025 | 1 / 0 | 普通完整步 | 0.26627394664444215 | 57.99999625062543 | (0,0)→(1,1) | 0.00025；记录一次成功 |
| 6 | 0.00025 | 2 / 1 | 同布局完整 SOC | 0.2662701215525791 | 57.99998346840656 | (1,1)→(0,0) | 0.00025；旧17条件 hold，双 streak 清零 |

模型1的新覆盖资格也通过，但旧 pair 优先消费两条计数。其增长由模型2真实使用，不能只凭最终“下一半径”报告宣称使用。

模型4已在原 mapped 上限 $1/4000=0.00025$。旧 controller 仍消费成功 pair，两个计数都清零；没有把“在上限消费 pair”算成实际增长。

模型2、6走 SOC，因此普通增长的 first-only/no-SOC/原普通门、高 ratio 及 no-old-shrink 条件不全满足，新覆盖读取不启动。新 controller 原样保留旧 SOC hold 结果，并将 covered streak 清零。

四个普通接受模型1、3、4、5的完整实际/predicted ratio，依次为

$
0.9453155054461654,\quad
0.8272848623558001,\quad
0.8050545545557625,\quad
0.8744444175361098.
$

这些模型两网各14个原门都通过，原 ratio 分母/尺度条件保留。四个新覆盖资格均为真，**其中带非零新增 soft ID 的资格为0**。

本轮全部 **8 条实际 trial** 的 new-coarse/new-fine 都为 $(0,0)$，两网 omitted-hard 也均为0。因此没有出现“本 trial 新学 soft 行、但完整模型已经覆盖它们”的新增适用事件。

### 4.1 模型2的原 SOC

普通 trial 的两网 η 为

$
(0.26629407673622385,\ 0.2662940766097033),
$

曲率为

$
(58.000009710486225,\ 58.00002999043424).
$

两网只有 curvature PSD、direct curvature 及相应综合通过标志失败；其他原门通过。普通完整 ratio 为 **0.6416158073878252**，原 shrink 请求为真。

随后原 same-layout SOC 完整接受，η 保持上述值，曲率变为

$
(57.99996312472419,\ 57.999983429335074).
$

两网14门全部通过；原 base-total 完整 ratio 为 **0.687303829012092**。真实 correction 的共 body norm 为 **1.3153099043261562e−7**，总位移 $z-x$ 的共 body norm 为 **0.0002500000000000835**。

旧17条件全为真、failed 列表为空，故把其旧 fallback 半径 $0.000125$ 保持为模型半径 $0.00025$。本次新 ordinary-growth 没有参与这个决定。

### 4.2 模型6的原 SOC

普通 trial 的 η 为

$
(0.26626888486283645,\ 0.26627063573649323),
$

曲率为

$
(57.99999881521858,\ 58.000019044127484).
$

Coarse14门全部通过；fine 仅 curvature PSD、direct curvature 及相应综合标志失败。普通 ratio 为 **0.47845203667229547**，原 shrink 请求为真。

SOC 完整接受后：

$
\eta=(0.2662691277555188,\ 0.2662701215525791),
$
$
\kappa=(57.99996320367447,\ 57.99998346840656).
$

两网14门全部通过；base-total 完整 ratio 为 **0.5693947633212895**。真实 correction 共 body norm 为 **1.0053823595868039e−7**，真实总步共 body norm 为 **0.0002500089399671279**。旧17条件再次全真，保 $B=0.00025$。

### 4.3 两个 correction LP 的原账

两次 SOC 都是 **same_layout**，都在启动前记入原共享 ledger；共享 LP 序号分别为 **4、11**。两 LP 均为 **9218×322**，HiGHS status0/success true。

| 模型 | SOC LP 秒 | 原单位最大行余差 | bound 余差 | scaled-row 余差 |
|---|---:|---:|---:|---:|
| 2 | 0.38977445000000444 | 5.293955920339377e−23 | 0 | 0 |
| 6 | 0.4070328599999584 | 2.6469779601696886e−23 | 0 | 0 |

原 SOC RHS、实际 $z-y$/$z-x$、所有 hard gate 和学习记录均保留。没有扩池事件，因此不能把这两次成功改记为 expanded-layout hold 的新资格。

## 5. 原12 LP内的资源账与 norm memory

Primary LP 调用为 $1,2,2,1,1,2$，合计 **9**；SOC 为 $0,1,0,0,0,1$，合计 **2**，总共 **11**。余量按每模型结束为

$
12\longrightarrow11\longrightarrow8\longrightarrow6
\longrightarrow5\longrightarrow4\longrightarrow1.
$

最后1个 LP 因已付的 no-unpaired-primary 分配策略明确留下，**不是**原12次总额度耗尽。没有把预留槽位记作实际调用。六个 primary 都报告返回修复候选、epigraph gap met，inexact 均为 false。

Primary LP 累计 **4.308114311 秒**，SOC LP 累计 **0.7968073099999629 秒**。这些 solver 时间不是完整模型/几何成本。

### 5.1 Cuts 与旧字段含义

原字段 total_new_cut_rows 实际包含每模型重新装配的 bank 支撑行，不能把它们全部称为新发现 cuts。

| 模型 | 原字段总行 | 初始重装 memory 行 | 本模型真正新增 cuts |
|---|---:|---:|---:|
| 1 | 59 | 59 | 0 |
| 2 | 67 | 59 | 8 |
| 3 | 419 | 63 | 356 |
| 4 | 374 | 374 | 0 |
| 5 | 374 | 374 | 0 |
| 6 | 387 | 374 | 13 |
| **合计** | **1680** | **1303** | **377** |

这1303行在各自当前模型处按原规则重建，旧 numeric cut A/b 没有跨中心直接携带。该表是对原已算报告字段的费用解释，不重新生成支撑行。

### 5.2 完整两网方向与原 metric J

六模型的新完整方向次数为 **2/4/3/2/2/4**，共 **17**；两网扫描为 **4/8/6/4/4/8**，共 **34**；方向缓存命中为 **1/9/6/1/1/9**，共 **27**。

完整方向耗时合计 **10.97790893899969 秒**。新增原 metric J 行为 **0/0/1/1/1/2**，共 **5**，其记录耗时合计 **0.156495984 秒**。

Coarse/fine selected-J refresh 各 **6** 次；coarse 为60 batches、1次 cache hit、**11.314520486999868 秒**；fine 为162 batches、1次 cache hit、**32.469227837999824 秒**。合计记录 **43.78374832499969 秒**。

新 covered controller 只读取已完成的实际方向缓存与绑定证据，记录新增 J、JVP、geometry、LP、value 调用均为 **0**。指纹与控制器 bookkeeping 并非无成本；它们仍留在本轮实际时钟中。

## 6. 时间、值评价与终态

### 6.1 实际时间边界

| 原报告字段 | 秒 |
|---|---:|
| prepare elapsed | 17.298191293999935 |
| run audit elapsed | 306.995358627 |
| process total elapsed | 324.293553086 |
| optimization active | 35.064484719000006 |
| 初始 ordinary audit | 234.362847179 |
| recovery，包含 pre-active 首 J | 71.100559824 |
| value geometry 记录 | 216.72742779 |

这些计时有包含关系，不能全部相加。尤其：

- **35.064 秒 active 不是本轮总费用**；总 process 记录为324.294秒。
- Recovery 的71.101秒明确包含 active 开始前的首 J。
- 初始 ordinary audit 的234.363秒必须保留，不能写成新增开发耗时。
- PRIOR→DEV 的约1.194秒只支持前述开发/import/hash包络，不能解释余下时间。
- 没有对跨运行硬件、调度、缓存状态作受控比较，不据本表宣称加速或减速的因果结论。

Linux peak RSS 为 **2,247,600 KiB**，即 **2194.921875 MiB**。

本轮共享完整值评价 **18** 次，原共享上限40；末点另作两次独立同状态原网格验收，总计 **20** 次。所有失败 ordinary trial 的实际 fine 值与 SOC trial 的两网值均保留在账中。

### 6.2 池与 bank

输入两池为4432/4358。第一个模型开始时为 **4432/4451**，随后保持到末点，版本为 **1/2**。因此 fine 的 **+93** 发生在首模型前的原初始化/池准备路径，不能归入八条 trial 的学习或新增 covered-soft 资格。

终态完整池 SHA256：

- Coarse：**2960646cf6cb902c0bd7a7169b969289d2b2209b88405c517df5998f5da938b4**
- Fine：**b74a9f03749e6263c574d6fd9048c4b456942dd02ac96c396da6ef8ad85e1110**

Norm bank 从59条变为 **375** 条，上限512；insertions记录 **759**，其中包含旧键更新，不能当作759个新增不同方向。Evictions为 **0**，inward-rounding记录 **374**。

终态有序 bank/context SHA256：

**470bf8bb51da18007e90e1c8bd11d3ca4fd7e5f3487a5bec375860b184d2fbad**。

终态物理163身份 SHA256：

**6ef6682e7fb2ce0ab550e449e824c1b8061c0b4f4c486c9de49687f2ec10bc04**。

Future checkpoint 保存原参考163、精确独立159和物理163、完整池与有序 bank/context；末 $B=0.00025$，legacy/covered streak均为 **0/0**。本文只保存人类结论和身份元数据，不保存 checkpoint payload。

### 6.3 末点门与限制

末点两网14个原门、旧 $167/625$ metric 资格和精确物理盒通过。Fine 记录包括：

| 量 | 实际值 |
|---|---:|
| ball norm squared | 0.9905563566781846 |
| inner margin | 3.899563905118697e−8 |
| mirror 量 | 0.10042221058777327 |
| minimum height | 0.02 |
| nonregular count | 0 |

两网各自报告的 affine cap margin 和重构 cap margin 分别约为 **−2.77555756e−17** 与 **−5.55111512e−17**，在原 $10^{-9}$ 容差下通过；它们是轻微负浮点余量，**不能记成非负值**。

新 metric 目标0.26和后续曲率目标约16.3934均未达到。上述门仍是原离散两网判据，不是全连续曲面的误差包络或完整 nonlocal reach 证明。

## 7. 可归因结论与下一子问题

本轮新增规则真正执行了最终签名、实际步缓存、完整两网域及两条 streak 的逻辑；但本轮没有 trial 新学行，因此其新增的学习豁免条件没有产生半径决策变化。实际增长来自旧 pair，实际保半径来自旧 same-layout SOC。三类来源必须持续分账。

本轮可供后续利用的具体失败对象是模型2、6的原 ordinary trial：它们在原最大 $B=1/4000$ 下碰到真实曲率门，随后很小的原 SOC correction 支付了曲率并保住下降。后继若研究新的 proposal，应先从这两次已观察失败与成功 correction 的完整模型身份、真实门和方向关系出发，判断能否形成独立的曲率预测/校正机制；不能仅因末点仍可继续就加 LP、加时间或重复本阶段。

成本上，应独立解释初始 ordinary audit 与 pre-active 首 J 的时间边界，而不是将其归给约1.194秒开发包络或新增 controller。本文没有新运行来分解这些区间，也不预断某一源码分支是瓶颈。

下一个已授权新机制的实际入口应取本轮 **375-bank / 4432+4451 / B=.00025 / 双streak0** 的真实 future checkpoint；不退回上一59条输入，不重播本轮以等待 covered-soft 事件。
