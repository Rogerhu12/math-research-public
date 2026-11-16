# p32 完整两网线包络首次实际：一个真实下降子步与第 53 个接受点

日期：2026-11-16（UTC）。本文消费唯一已执行研究及其后置只读 report；没有重新执行开发、几何、J/JVP、标量优化、LP、SOC 或锥求解。

## 1. 已发生的结果

本次从原第 52 个真实接受点出发，对已付第 32 次锥调用留下的同一个 $p_{32}$ 构造完整粗细两网仿射谱线包络。唯一生产标量会话实际查询 62 次，选出

$$
\alpha_*=\frac{4883617606959283}{9007199254740992}
=0.5421904710711004.
$$

随后只做这一个此前未试点的粗、细各一次真实几何评价。两网原 14 项门与原 163 维精确物理盒均通过，真实两网最大 $\eta$ 从 **0.2660182947853381** 降至 **0.26601514422985384**，下降 **0.0000031505554842770067**，超过原接受阈值 $10^{-7}$，并严格下降。该点真实记为 **accepted index 53**，物理状态 SHA256 为 **9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e**。

最终两网最大绝对主曲率为 **57.9992694544513**，仍通过原上限 58。目标 $13/50=0.26$ **仍未达到**。本次结果不构成连续曲面上的全域曲率、reach 或严格正高度证书。

这是新标量线方法的实际成功。它没有把旧锥调用 32 的 AlmostSolved 状态、其 $\alpha=1$ 处完整包络负改善或其旧候选资格改写成成功，也没有恢复任何旧求解额度。旧 **64 次 HiGHS / 32 次锥调用永久封存**。

研究阶段终态为 complete-two-grid-paid-p32-first-jet-scalar-line-audit；实际试点阶段为 new-scalar-line-two-grid-strict-descent-accepted。该判断由真实 TRIAL、末点与门收据支持，未从 Actions 的 success 字样推断。

## 2. 唯一运行与证据链

- 源提交：[ab1ba331a1d376d61e6e9f9b7f29f2bb9221a1e2](https://github.com/Rogerhu12/math-research-public/commit/ab1ba331a1d376d61e6e9f9b7f29f2bb9221a1e2)。
- 唯一 run：[43804573954](https://github.com/Rogerhu12/math-research-public/actions/runs/43804573954)。
- 研究 job：[133092260804](https://github.com/Rogerhu12/math-research-public/actions/runs/43804573954/job/133092260804)。
- 后置只读 report job：[133095041106](https://github.com/Rogerhu12/math-research-public/actions/runs/43804573954/job/133095041106)。
- 研究与 report 两 job 均 completed/success；report 读取研究日志时，包含 report 自身的整个 workflow 仍为 in_progress，这是正常的同工作流依赖关系。
- 研究原日志 **19,369,550 B**，SHA256 **12cab583514612fa08da7988b4f71aaf9478d019ec313ae5f2a4d06d70b15392**。
- report 原日志 **462,043 B**，SHA256 **db10cac8f845fbd823c3a77b6a1f12159d94d76ba3b72c79e63c2e2715cf9a6c**。
- P32_LINE_REPORT_COMPLETE 原 JSON **377,354 B / 7f97515790fff5081ba3191d2f8c42fc778634a36fe07ff867c6d70e232cf966**；含 LF 为 **377,355 B / 9c1563020201f6f7e18da5a8953fe61893e56c98a7bdeda8da22c0cb448af729**。

report 在 runner 内读取研究 stdout 一次，保留原记录指纹，验证完整 CACHE 记录与生产者收据相同，并只复制已付语义值；其 scientific imports / recomputations 为 0。本文独立消费一次 report 原日志，没有再次下载大研究日志。report 未超过其语义输出上限，未省掉查询表、真实 trial 或末端证据。

研究 job 的 UTC 调度墙钟为 **04:31:00 至 04:39:50，约 530 秒**。下文报告的进程单调科学钟为 **81.44572784500001 秒**。两种观测分别保留；本文不擅自解释它们的差额，也不称 81.4457 秒等于 job 的 UTC 墙钟。

前序真实输入是已发表的 [cone32 实际结论](final-cone32-first-actual-and-complete-grid-separation-20261116.md)，run43800505444/job133079366251/source8dfe5272b6d4f4fb752c8962689b22a95c61f78a。原完整 raw161 中的 $p_{32}$ 是本次方向来源，不含未保存向量的猜补。

## 3. 源闭包、原输入与开发执行

本次 request 文件为 computations/request-p32-line-envelope.json，**44,738 B / 7b300c90eeb4c4b7c1fefc5b449fd8c80ec8aa836b10324b2e34c9942d3936a4**。实际 REQUEST 与当前文件及全部 **200 项** source manifest 精确一致；其中 Python basename 闭包为 **176 项**。

manifest 规范 JSON 指纹为 **572680ffde786bc06a0d325728a8ebbaa2b24d068d006160a776725ee7143342**；176 项 Python 映射指纹为 **9eb71dcb47e960b5e9318f1ad09e131cc0e53368128aeedd1bea8c9141a3e8dc**。本次消费时又从冻结 request 逐 basename 重组，得到相同两个指纹。原 **189 项依赖 / 170 项 Python** 冻结部分全部匹配，原 98 个输入参数不变，必要 24 个已完成输入报告恢复一次。唯一前序原日志读取一次，更早原日志读取为 0。

原数学定义保持：

| 身份 | SHA256 |
|---|---|
| 完整固定 metric | fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6 |
| 固定 b0 | d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5 |
| 原 source configuration | 1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19 |
| 原坐标/永久 reference | b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580 |
| 原普通 field evaluation | 8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1 |
| 原 factorization definition | b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963 |

新开发只执行 **1 组 3 case**，全部通过：

| 新 case | 人工标量会话 | 小数组完整查询 | 观察 |
|---|---:|---:|---|
| smooth-original-phi-interior-minimum | 1 | 62 | best alpha 0.5000000000001444；模型改善 0.299999995 |
| two-original-branches-max-switch-minimum | 1 | 62 | best alpha 0.4999999999998555；模型改善 0.08885620753586526 |
| monotone-original-phi-endpoint-without-descent | 1 | 62 | best alpha 0；模型改善 0 |

因此人工为 **3 个新标量会话 / 186 次小数组查询**，与生产 **1 个标量会话 / 62 次完整两网查询** 分账，不能把“无 LP/锥”误称“零求解”。人工实际函数秒数 0.035107783999997366；科学 ledger 记录含调用包络的 development phase 0.04155341800000656 秒，包含在总 600 秒内，不再相加一次。

人工 ordinary geometry、参数 J、field direction JVP、LP/SOC/锥/tiny cone、生产系数建造、旧开发套件执行均为 0。此前 6/12/11/9 条的已付检查只通过原收据复用，未重跑。

## 4. 唯一完整 first-jet 系数建造与原 stdout 缓存

新方法沿原数据流构造 $U=X_s,T$ 及真实参数方向 $\delta U,\delta T$，保原全部角节点的周期算子、原参考高度与五 null-height 的两次实际加法，随后得到

$$
e=U\cdot U-1,\quad f=U\cdot T,\quad
d_e=2U\cdot\delta U,\quad d_f=T\cdot\delta U+U\cdot\delta T.
$$

本次没有为了包络建造 $X$ 或 center，没有调用普通几何、selected159 J、primary factory 或后端求解。完整粗网 160×384=61,440 点，细网 160×768=122,880 点；每点四个 binary64 系数，总 737,280 个数。两网各只建造一次，全部点恰由原顺序拥有一次。

建造总计 **14.261769182000002 秒**。原 reference height density jets 4.320260037000004 秒；粗网 0.13610569000000083 秒；细网 9.794821474999999 秒，其中原完整 scalar-grid 调用 9.529976267000002 秒。建造前后 fixed primitive 都为 prefix absent / partial points 0，故这次确未暗做 position prefix。

完整缓存以一个普通 JSON 原记录先输出，随后才做任何生产包络查询。其身份：

- 绑定 SHA256：**dc2e3a630ab01e821cb0311e1615c4b3d24d420c1362b090adf7a819d7f35df7**。
- CACHE 原 JSON：**15,234,254 B / 778f27a58df90e21b8e542d0bb5f26560ba33b373022411d2aeee995efb5c664**。
- CACHE JSON+LF：**15,234,255 B / fea965f210f9af45917461a56b6ea7719fa83495f15005c699cf8d4564d6b54e**。
- status complete，coarse/fine 均存在，生产者收据与后置 report 对整条原记录的实际指纹相同。

缓存留在本次研究原 stdout，未编码、分块经 API、上传 artifact、Actions cache 或写进 Git。report 不打印或重算这些数组。未来只能以该原输出与其身份消费已付缓存，不能重复建造后冒称复用。

各原 binary64 数组指纹：

| 网格 | 系数 | 元素数 | 原数组 SHA256 |
|---|---|---:|---|
| coarse | de | 61440 | b209c61bc14cdb4f173f21803b5f3107c646d35b9d8b0a059be66d15a669d463 |
| coarse | df | 61440 | d0a27d4309fa79a16afb33acb4f55cb6f67edd580e2dc2163a346cbcb1e5ed44 |
| coarse | e | 61440 | 45d080899e37770a8323ef862bc3989b97b868497c5d7c3100cdfedceef52244 |
| coarse | f | 61440 | 7e564684fcb289547e7567cc1bb63c6461f9ae869833b0dc31c35e4147fcabd4 |
| fine | de | 122880 | a84e47809769b11d0b14340511d58ba9b67c079d08fe13ffa1c66a76bdb35c5c |
| fine | df | 122880 | dd084828f044d375366dd05aecc526f5700936b741baf59a34564b87644a89ca |
| fine | e | 122880 | 80c38531b0f126fd7720c3f4d33b753d53abf239072784535e682968b726c981 |
| fine | f | 122880 | 7c1e5ef531470f7a0e567af16fea378188f992acba25666452aae9e86c30aeb4 |

全部 8 个已付端点 branch maxima（$\alpha=0,1$）和四个已付 attainer 的 16 个 $e,f,d_e,d_f$ 系数，本次 **24 个对照的实际 absolute error 都是 0**，原容差 $5\times10^{-12}$ 全部通过。此检查复用已经建好的数组/已付端点查询，内部新 geometry/JVP/query 为 0。它是有限的实际接口证据，不是旧整数组逐位重放证书。

## 5. 62 次生产包络查询的实际含义

每次查询使用相同 cache binding，在完整两网全部点取

$$
\Phi(\alpha)=
\max_{\text{两网点},\,\sigma=\pm1}
\frac{\sigma(e+\alpha d_e)+
\sqrt{(e+\alpha d_e)^2+4(f+\alpha d_f)^2+\epsilon^2}}{2}.
$$

生产会话实际 62 次查询全部完成、编号连续 1–62，且每次均在评价前收费；没有查询 63 或 64。会话耗时 **0.6305761680000046 秒**，所列 62 次 query.seconds 合计 0.615459147999978 秒，后者只是不含外层操作的分项和。

| 量 | 实际记录 |
|---|---:|
| $\Phi(0)$ | 0.2660182947853382 |
| $\Phi(1)$ | 0.26602970125710546 |
| best observed $\Phi(\alpha_*)$ | 0.2660150043760925 |
| observed model gain | 0.0000032904092457375356 |
| best query | 62 |
| 原模型改善 floor | 1e−10 |
| 最终搜索区间 | [0.5421904710708115, 0.5421904710715678] |
| 停止原因 | declared-search-query-limit-with-two-trial-queries-reserved |

$\alpha=1$ 的原坏分支是 fine group0/flat87417，$t=3/5,\theta/\pi=211/128$；该端点完整包络高于起点。$\alpha=0$ 的当前最大分支则在 fine group0/flat36839，$t=33/200,\theta/\pi=743/384$。本次观察的端点包络浮点斜率分别为 −0.00000606918086643744 和 +0.00003212240427156504。

这些数据实际展示了端点不改善与内部可改善同时发生。最终小区间及浮点斜率不是精确 active-set 证书、解析最优性证明或区间误差界。程序和本记录均不声称算出了精确全局最小值；所需的已付事实是观察到的模型下降超过原 floor，然后真实原门确实接受了对应点。

新点的真实两网最大 $\eta$ 比该仿射模型值高 **1.3985376134950656e−7**。这只是同一实际试点的完整模型/真实值差，未被改称跨中心误差上界或新曲率学习样本。

## 6. 唯一真实试点、原门和新增池行

原 source52 的 $\eta$ 为 0.2660182947853381；新 true53 的数据如下：

| 实际量 | 粗网 | 细网 |
|---|---:|---:|
| 最大 $\eta$ | 0.2660148711293937 | 0.26601514422985384 |
| 最大绝对主曲率 | 57.99818235899948 | 57.9992694544513 |
| 球半径平方归一最大值 | 0.9905306565108914 | 0.9905306565551374 |
| inner strip absolute margin | 1.0962807588943413e−6 | 1.0962834945393851e−6 |
| mirror radius 最小有限值 | 0.09760887491225302 | 0.09760887491249544 |
| 最小 signed height | 0.02 | 0.02 |
| 新目标 13/50 | false | false |
| 原 167/625 metric budget | true | true |

原 14 个判定逐一保留，没有合并成单一笼统 pass：

| 原判定 | 粗网 | 细网 |
|---|---|---|
| cap_and_box_eligible | true | true |
| curvature_lambda_bound_pass | true | true |
| curvature_scaled_PSD_row_pass | true | true |
| hard_ball_pass | true | true |
| hard_strip_pass | true | true |
| independent_direct_curvature_pass | true | true |
| independent_direct_mirror_radius_pass | true | true |
| mirror_polynomial_pass | true | true |
| outer_strip_pass | true | true |
| previous_metric_budget_pass | true | true |
| regularity_screen_pass | true | true |
| signed_height_pass | true | true |
| single_grid_admissible_recovery_point | true | true |
| single_grid_hard_gate_pass | true | true |

原 163 维精确物理盒零违例，实际 height 比较使用 exact affine values，不以四舍五入九向量替代。固定总高度积分改变准确为 0，物理 height c4/c5 不变。affine height margin 为 −2.7755575615628914e−17，重构 margin 为 −5.551115123125783e−17；二者在原 $10^{-9}$ 高度容差内通过，**不称二者非负，也不称连续严格正性证书**。

原 stdout 保存本次真实 scaled paid direction159、rounded actual total step159、新 independent point159、physical163；实际列表长度逐一为 159/159/159/163。native TRIAL 与 COMPLETE 中同一 trial 完全相同，末 selected point 与 checkpoint 的物理 SHA 和 accepted index 一致。未硬编码“保存成功”代替实际列表存在性。

实际共同 body radius norm 为 0.00013541272475936506，共同 height radius norm 为 0.0005416508990374602；physical normalized height infinity 为 0.00014263559834526776，tail 为 0.00001688181866484062。这些是原定义下实际 rounded step 的观测，不把旧模型的 $B=0.00025$ 或旧 raw norm 资格重新授予该新方法。最终接受依据是本任务约定的原精确盒、14 门和真实严格下降。

粗网 omitted rows/hard rows 为 0/0；细网为 5/0。原 value-only learning 实际加入 fine IDs **86919, 87033, 87303, 87417, 210297**，全部属于 soft metric 观察，无新 hard violation。粗池保持 4448/version13，细池从 4544/version13 变为 **4549/version14**。原 fine159001 继续保留。accepted trial 可以同时真实学习这些新 soft 行；failed-new-row 停止条件不被反过来当作接受否决。本次在首个真实接受点停止，没有试 half/quarter。

## 7. 实际成本与两个时钟

权威 P32_LINE_FINAL_CLOCK 位于大 CACHE、COMPLETE 和 OUTPUT_METADATA 输出之后，并实际执行末 600 秒检查：

| 账目 | 实际 |
|---|---:|
| 新科学单调终钟（含 dev、输入、准备、建造、查询、真实评价、序列化/emit） | 81.44572784500001 s |
| 新科学上限 | 600 s |
| scope_exhausted | false |
| 进程秒数（同一末记录） | 81.445749598 s |
| 原祖先科学终钟 | 1324.8055252469999 s |
| 祖先加本轮权威总钟 | **1406.2512530919998 s** |
| 旧 cone task 单独历史，不再次加到总和 | 968.6757049859999 s |
| Linux peak RSS | 498216 KiB |
| 后置只读 report 函数秒数（与科学分开） | 3.2410574210000007 s |

主要实测阶段：

| 分项 | 秒数 | 范围 |
|---|---:|---|
| development phase | 0.04155341800000656 | 已含在新科学钟 |
| 唯一原付费日志读取 | 1.3856425840000028 | 不含另一次旧日志 |
| 必要 24 输入 prepare | 8.763211887000004 | 一次恢复 |
| value-only constructor | 0.10297814399999794 | 无普通几何 |
| 完整线系数建造 | 14.261769182000002 | 一粗、一细 |
| CACHE 序列化及 stdout 调用 | 0.30450030299999753 | 原 instrumented 调用 |
| 生产 scalar session | 0.6305761680000046 | 62 query |
| 真实粗网调用 | 53.755303643 | 计 1 value |
| 真实细网调用 | 0.38152225499999304 | 计 1 value |
| 普通 adapter 几何两调用内部总和 | 54.00788737999999 | 上两调用的子范围，不能再加总 |

真实粗网 adapter 首次 fixed-height primitive 是 prefix-miss，53.580497472 秒；随后的细网同一进程命中该 prefix，0.00018339599999706024 秒。两次普通 scalar grid 与 reference height jets 均命中本进程已有对象。此实测支持“first-jet 查询不必先付 center/position prefix；只有实际候选才付原完整几何”的调用事实，不把它夸大成跨机器速度保证，也不追认旧某次 205 秒全部为冗余。

新真实 values 为 2，预算 debit 为 2，adapter started/completed 为 2、failed 为 0；source124 加本轮2 得 **126**。没有独立 initial/final geometry。新 build1/grid2、生产 scalar1/query62、实际 point1；新 selected159 J、primary factory、LP、SOC、cone 全为0。新dev的3人工session单列，旧64/32不变。

checkpoint 的科学时间 **81.313210678 s / 累计1406.118732711 s** 和较早 COMPLETE ledger **81.315323902 s** 都是早于最终输出的快照。后继必须继承 **FINAL_CLOCK 81.44572784500001 / 1406.2512530919998**，不能用较早 checkpoint 少计输出成本。UTC job 墙钟与这些单调计数分别列于§2，不据二者差额虚构未报告的科学阶段。

## 8. 真末态与后继使用边界

| 状态 | 末记录 |
|---|---|
| true accepted index / physical SHA | 53 / 9ffba0f1400c504343f9b0b8847be7f14745144f66b3cd89dfe698f45d81548e |
| coarse/fine pool | 4448/4549，versions13/14 |
| coarse pool 规范 JSON SHA | d136adf8b2dd0989828c305aa7101ba7ecdfc1197fbf02f02e0229cce0c1289a |
| fine pool 规范 JSON SHA | 0552979556355c404e3668dcd6c5a3491a22885ea26f6b553a179e0e2198a809 |
| norm bank | 512，233b2e81fdd0ab36f3306d2d901e8708bb103ea34c9c20ef006537d371634527 |
| learning | 62 events / 61 commits / pending0 |
| learning SHA | b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76 |
| coarse/fine gamma | 57.187653029922444 / 67.42701956990882 |
| passive B / legacy streak / covered streak | 0.00025 / 0 / 0 |
| 新 value-only objective SHA | fa4757cdc16c284e47cec422bbccea6abfa379e36c456d7bec453559c93b8e77 |
| 原 affine objective SHA（来源身份） | e101bd909dbdb5fb2c7f839b2d416b66e473bf7326dfb80e7af396f3f97a26b6 |

bank、supplemental normals、gamma、controller/streak 和旧历史被动保留，没有从缺失的本次参数 J 或 primary 模型伪造 feedback。新真实接受不自动授普通 growth/covered/SOC 资格。future checkpoint 明确要求下一新模型使用真实53和新池，重新绑定其数学与评价上下文。

缓存仍绑定旧 true52 及原 $p_{32}$，不能当作 true53 的完整新线性化。既有单线科学问题已经完成，不利用剩余查询/试点/秒数重跑 62 次查询或这个已接受点。下一待解决的是从真实53生成更有效的新下降方向/模型，而不是继续调这个已求毕的标量。

有实际依据的新方向是：在新53与五条新细网 soft witnesses 上，研究把**完整两网线包络作为候选方向的全局下降筛选层**接入下一次方向生成，而不是仅凭 $\alpha=1$ 完整修复 gain 拒绝整个方向。本轮给出一个严格的实际动机：同一个已付方向在 $\alpha=1$ 的完整模型不改善，却在内部子步产生原门认可的下降。下一工作必须另立完整输入、候选资格、计费和后继真门合同；不会借此重开旧64/32，也不会把旧52缓存重标为53或把一次成功推广成收敛保证。

## 9. 实际规则读取

研究 public actual git pull --rebase：04:31:17.416142–04:31:17.788643Z，before=after ab1ba331a1d376d61e6e9f9b7f29f2bb9221a1e2。根 README blob21bd547f56590b7f2dd279d0297efb289a9b2783、题 README blobd0432faff569c8e9af7ed4809847e12880976c11 均空差、expected match、returncode0。private 04:31:19.914235–04:31:20.853156Z，before=after92b77224d77ea6e9b87c9dec2a61bea963ace042，根5ba164843b1f5802184178a82d786264404873a3、题不存在；规则无差，QUEUE unique ongoing。

report public actual pull：04:40:07.438983–04:40:10.489559Z，ab1ba331→27a479dece2256eea19b86be85080c4a91963fd5，两 README 仍空差。private 04:40:13.846911–04:40:14.699739Z，before=after441751f3124e5f8c23a8896c01c28c687306c20e，规则不变，QUEUE unique ongoing。后置读取是同一次已付研究的只读报告，不是新研究或重跑。

## 10. 原记录指纹

下表均为原研究 stdout 内的 JSON 字节，不含日志时间戳或 tag 前缀；no-LF 与 JSON+LF 分别明确。本文仅保存来源、参数、元数据与人读结论，不把原数组、向量或 checkpoint payload 写入 Git。

| 原 tag | JSON B | JSON SHA256（无LF） | JSON+LF B | JSON+LF SHA256 |
|---|---:|---|---:|---|
| PUBLIC_PULL | 1482 | f7a53f91f52513ad7ef832123b5f6e309c3c18ff428f8581a6bffd5c3848b11d | 1483 | 974e9557a30b3f779efea08062f82baf6236814ab1ef413ea41eaf9a7b3c9493 |
| PRIVATE_PULL | 583 | b8d5e70f46db995fd6c8c1a6d15a6107b0e2aa35667714163dcd274238888214 | 584 | 2c90d03de97b82514358376c4cfb0cb3badbce163a215d2df1ea9626633cae5d |
| REQUEST | 32511 | fe43ae96dba05b4ce17c2175eadfcdc014220ffebfcaf17e77f9bc0c3797fdd6 | 32512 | 4b75275d37b3710f83c885e38d3187e1e4548c7e27e0f77a7ce2906a4e370b5d |
| DEVELOPMENT | 8623 | 17800909147e785afe42983dd59d24186eded053f3a78a44ef91bbeb9b973042 | 8624 | 42cb7da3793a49e5a7d8ea9cfbdd0203ddfae9f51cff5d6c4e4e66e884ca2fbe |
| PRIOR_WORK_REUSED | 2776 | d7cc352883f3f5a90edf84988c8bb7dcf6048cb873f74c69c32cf24d1f02f668 | 2777 | 342913c8dea3512af31b92122f5c5ac09b12ce2b204769d797c558dcae25106c |
| CACHE | 15234254 | 778f27a58df90e21b8e542d0bb5f26560ba33b373022411d2aeee995efb5c664 | 15234255 | fea965f210f9af45917461a56b6ea7719fa83495f15005c699cf8d4564d6b54e |
| ADAPTER_REPLAY | 7054 | a7abec75a7d04c04426f28cc7cca932ecf889b188525be928fac95fc2685cbe1 | 7055 | e989108fb6f19e4f56ccc8488c7ab364bab9027b57d9f27100e9ea7f9875a343 |
| SCALAR_RESULT | 8524 | ccfead3e0570761557ed7e5f1e69bede9ffe4dfec8c9b0bfd7e8575fb05c742c | 8525 | 061f3c4c3e9d70d1b95a740de44c786afc0c58718b66e0bf79e26ed36363fbef |
| TRIAL | 67924 | 07925b2b255a3b9ee9c29308c1142279f50a9939fc13c1870d1f9f181a58e1d9 | 67925 | a6f3e5be139c80a5fd3f6761e6919882bbc8a48312c7561133c7cdbaf5512968 |
| COMPLETE | 3717686 | 016d9e37561c7e43899746ba3fc073f548d056115c76b0bd8224692ebaa5deee | 3717687 | 9302b47c2845c83707992aad2bcd91cf32dc07b1105a771337c17c9cf23e5023 |
| OUTPUT_METADATA | 185 | 73189bb5bb5df6932045dcc16185a0e761b2623d41f887728a221665a5dc25fc | 186 | 0e62f47ce737bf838c4db6420b0ba1acba148f55621299c23318f8382b0d2414 |
| FINAL_CLOCK | 1848 | a0950a56b3c828a22c6dcef231709dabb85663b21de7161b8b31d4123944a018 | 1849 | 9e72ed720c8b05c38647a6da07e1ffb3caf56636ce814ee7eaf58708672e2b95 |

全部 62 条 QUERY 的顺序与编号一致、cache binding一致。以下逐条给 JSON+LF 指纹；无 LF 指纹同时完整保存在后置 report 的 record_fingerprints，不另拷贝成数据文件：

| QUERY编号 | JSON+LF B | SHA256 |
|---|---:|---|
| 1 | 3048 | 4a3a0afe3e30cce77ec8bc1dc657eb04154a3c524f2119e6e80904b3450fe25d |
| 2 | 3059 | 79c0e08c37fd9b1e6cb6628c72b41f6fda20c20f09b1c4f80f0defe1f3384a6b |
| 3 | 3097 | 732e11fb493ea95538c6f69443dfee4a950eb4e1ec21c0276a2c53968bf73e18 |
| 4 | 3099 | e87c10c953bd6ba6d4f542db6ff9a16dcebb5b7c634d01b1e04af12b057dc784 |
| 5 | 3112 | 5ca9a87de4feea37a2648d56b1ccf5d4a87e62036f04f2bb5c1fc3a08b6ccb83 |
| 6 | 3102 | 23d019f6b7833ebde68da55a02f3164972e13cf320be0e5a81e392ae172e9b2d |
| 7 | 3110 | bfe44a72de34b1cec41e5127d4079bbad2dac7c889e7c38a89f2ef2c4369b110 |
| 8 | 3101 | ca1c76969b54e59fa53adc8866c6863de5c222081f87a0d0be0e00c161779f23 |
| 9 | 3116 | 8ac848b65afe20d3a244581c3411df93c176510067dfaee4a73c3ac8235a2a44 |
| 10 | 3106 | 9fdf4076212d9abce83090d783313c6a3e031dd088f348292bef2a431a463d8a |
| 11 | 3109 | 4f528a5499e68201bc6ce7a4e5b2054574eec77a5eb33873b16b77b51e5932d2 |
| 12 | 3106 | 7d35e2e38da6028f327d72fde7ddedda7c9d57d89a61134c71d7fb77952ed727 |
| 13 | 3104 | 74efd14e23bc4302461f4c06c244780638914ce8906f1e2086c2f157bba6b2e8 |
| 14 | 3116 | 5bf328c9932acf8eb33429813f598fdd5ac39aa5c734f7a1d0a20f807564a9ca |
| 15 | 3107 | 0e8b4a2640dab03c4514e4f316719a9e225a37556c66ea19fd279418ec3d2289 |
| 16 | 3103 | 94df824ce397c2f9cbb9b576a2113daa6b9342f8b55bfac28d39415340e0772b |
| 17 | 3104 | 6575e92d070205b3cc1976446706984e4d8f1f8476116a60ded944f349b3cb4a |
| 18 | 3099 | 41c34689e6acdd8842dcf68be167e41e284e0c4723d335f17f2c1f6fdd0ec286 |
| 19 | 3106 | 5f508a6180267094dcadfef7f5b4f350a47aa59cd2fa34611244697d6d8cc27b |
| 20 | 3101 | d16128811613ffcc08a947fa77c70aa0f9be8b3eedb6115db947bf1bbbfa4785 |
| 21 | 3111 | 748a7fd9a51fdeb207b8011645984777e6fd104af784dbc24eb747eb177444b6 |
| 22 | 3116 | 27e335b903ec6ff68344ee5ca5c0a6b4074baff557114064dc9cefa08a84dbce |
| 23 | 3116 | 973a05a7e66d858a500f9fa29f9159fdedbab6220f9752852fddd407c3042344 |
| 24 | 3112 | 14cca9917e61f465f76e90b6cfdeddbce42f45c6ab6cfabb9c8c66cf210635e2 |
| 25 | 3103 | ee3c4a674270354050f08aec72978037be525014eeffea7c6f76c102fd739d21 |
| 26 | 3103 | b5d9b752407824f5e7044986c7a8c724408d3ac9ba43a33de654e865a3ba64d2 |
| 27 | 3103 | 788d6f273f7dd7315388793f5ac8e5b1e355d8a4655730f417b928e510eaa681 |
| 28 | 3103 | 963870d81ca81c83603e7035443d7396aef9dcf388daf43b84b138221c360382 |
| 29 | 3107 | 0e8ff4bb6d20f21850ce90d9ccfe795d1443face78acc3539524b5b160acd39a |
| 30 | 3102 | c8fd6d28b7b15d1eede5fe03d1cafd0b4f3dd88a74890153200b93ceafc28e95 |
| 31 | 3111 | 8678415a28698f24f3c8779c4ef9c192c349256e1996b68dca86d9aeb40fa1d4 |
| 32 | 3100 | cb1a77321890195083b94e602d5d9fb378ef8255bc7ba44c5bf9c09cd1727ef0 |
| 33 | 3113 | b5a3d9e06b626856def98edec4b9dbcd6b0d78383faeffd52674be3a89af77ed |
| 34 | 3113 | fc09a5376897de61ebcfa6e079d4a8845dbf980d1874120cca979f12b59e9894 |
| 35 | 3100 | 80e76c0b7f76dd9c62851de84d8cc3178337b1ecb6136f13699825e2fe6133f5 |
| 36 | 3107 | 99a97241a2991cc5c72791e0e9f8eb29e10d2aa8f05e96dc705fe06594e0ae7c |
| 37 | 3109 | 9949a3fc1fa18d3c7feeae921b0a32d54dd7f84fd5694a853641ae74f51d8978 |
| 38 | 3099 | 0e204cc72a13a7a37a9ef5580f3d38c05da708fecc02da71a2692e1266dc5a0a |
| 39 | 3100 | b64bb68d11ca6e7c75c65f7c6d4d698e62dfc6eef2a439e9481f9ce33ce27f51 |
| 40 | 3109 | 8297b0c3d362c5896fbaf80ee129fda06aa4e3b45472e82c6a2104ca7411cb66 |
| 41 | 3101 | 64553f8fc91b99dbc5dfaf030b03537d0479fc53b1f545c405ad31e2aae40412 |
| 42 | 3110 | 276e5c5917d33fc8cd00560b8a9efab055e9ef7b312fb0c1514408c8ad6ccf99 |
| 43 | 3113 | 3a200c18b15da62365c60cfd934a13f27a7ddfcb57f064e40b56a4f050f69d81 |
| 44 | 3096 | a1964c979d1a30986fdfe9cbc12cba4b4013fb83c3770cdecd5fd2187c491c02 |
| 45 | 3110 | 085c6ebf72292013da19e037faf25bb004406817e226e7f8c238e8f484521265 |
| 46 | 3107 | c42b16b8c1abbd4dff9feca08d158985a40eeb7e4fa955f7996899556ca64e54 |
| 47 | 3104 | f176a3a27cbd8a4a793dd6df2286750dcc9a41318ad7d8e25ef8ab32bea3d862 |
| 48 | 3106 | 68aa37e720c2ac3df7339452430de8d1d68adcdd314995854f9f1f07ac4be715 |
| 49 | 3105 | 66f8a4525aecbe83485799656a837958ca7127f8fde1f5585bef48f011c51ada |
| 50 | 3099 | 0d2245a0ef55414e06f46879fcbde31ed3895ea7f557f01e0ab50bcb2082f50e |
| 51 | 3112 | 00918adc90d1575d4e94a428a02527e2c9b03112352a531b6bca351bb3198f05 |
| 52 | 3114 | 66dac5e1112286c992e71d20b40a0df6cb559ab726b4b90572ed993226eb75ab |
| 53 | 3116 | ecd79da1ac5ce110aabbe392ffab0256d8280ba437846bc207dc45ebf33ba114 |
| 54 | 3096 | 2300cbb355ab298ad4e0f94281aded47413962517be81da3486eec60b2a027ef |
| 55 | 3096 | c39e51dc3268a804653fa9dbe8bb52cf4f9cdae8e41cb935d8e959fa09a73c05 |
| 56 | 3110 | 0c92030573aa0bdbb27b5c02909c5656d21fa4990e0741cdb1043d6a4c0c16f1 |
| 57 | 3118 | e50d366772f80489036dc12de995ffd156123bcfd009cbb9b2283ad9dda863d3 |
| 58 | 3108 | 141012138690e5412f25b03ee3c1fef77dca549d59e0fe22ce4ff61dfcb883ea |
| 59 | 3107 | b572da723ec81188f4fd3a998488c67e056810114f436990444181fad49b87dd |
| 60 | 3109 | 6bf037a7fa50898869562593116a29088d997a5416d7652da0458bb11efb9438 |
| 61 | 3110 | c6312d01bcf739e2ff1b0d858fa174b3a5cd57e18c8e5b5189dfae4d8d75ee3e |
| 62 | 3112 | 53515b539072491993666f57f59cd6d046749a79f3cebea90a93f53d6a6abe76 |

后置 report 自身的两条规则记录 JSON+LF：

| tag | B | SHA256 |
|---|---:|---|
| P32_LINE_REPORT_PUBLIC_PULL | 3877 | dccc3e3b9bcd54ef4ee40d9eef669a8d223d7446f6e3d92fdfea120102f49d99 |
| P32_LINE_REPORT_PRIVATE_PULL | 584 | f2a82323e3cfc3a84775ad01e24b3e39b08acb7b3b255656460b3d038e06a49d |

源码与预算依据为已发表的 [凸包络纸证](paid-p32-complete-grid-line-envelope-convexity-20261116.md)、[first-jet 方法设计](paid-p32-first-jet-line-envelope-method-design-20261116.md) 及本次固定 request。所有结果来自本轮唯一 Actions 实际输出的消费；本文写作未新增任何科学执行。
