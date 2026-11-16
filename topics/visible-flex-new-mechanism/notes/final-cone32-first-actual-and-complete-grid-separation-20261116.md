# 最后 cone32 的实际结果：完整网格分离否定了有限锥候选，原第 52 点保留

日期：2026-11-16（UTC）。

## 1. 已完成的唯一新动作与结论

本次只消费原有限锥任务尚未启动的第 32 次调用。公开运行 [43800505444](https://github.com/Rogerhu12/math-research-public/actions/runs/43800505444)，job [133079366251](https://github.com/Rogerhu12/math-research-public/actions/runs/43800505444/job/133079366251)，科学源提交为 `8dfe5272b6d4f4fb752c8962689b22a95c61f78a`。这次恢复的是此前实际保留的第 52 个接受点、两池版本 13/13 和已经学得的 fine 159001；没有重试旧 MaxTime31 的方向，也没有重新求任何已付 cone 或 HiGHS。

**第 32 次真实调用返回 AlmostSolved，原有限模型的线性行、盒与已纳入锥的原单位残差均通过；完整两网仿射求值发现一条尚未纳入该锥集合的 fine 行，把 rho 上调后，模型改善量为负。因此没有物理 trial，没有新接受点。** 实际两网非线性验收并未失败，因为此次候选没有进入该环节。原第 52 点的 $\eta=0.2660182947853381$ 保留。

这不是后端 MaxTime 的重演，也不是关于完整凸模型驻点或几何不可行的结论。唯一真实末槽在第一次完整分离之后已用尽；新增 finite cone tag 尚未参与任何第二次求解。阶段原标签为 `finite-cone-model-no-returnable-step-not-stationarity`，没有将 success 状态解释成科学目标完成。

本次执行数：

| 动作 | 本次新增 | 累计或保留状态 |
|---|---:|---|
| Clarabel cone 调用 | 1 | 原有限锥任务 32/32 |
| HiGHS 主 LP / SOC | 0 / 0 | 原 63 主 LP + 1 SOC = 64 封存 |
| 新普通模型 | 1 | 编号 28，基点为接受点 52 |
| 必要两网普通值恢复 | 2 | 粗、细各 1 |
| 物理候选 trial / 接受 | 0 / 0 | 接受点仍为 52 |
| 独立末次全网验收值 | 0 | 原点收据引用；另保本次恢复值 |
| 新开发检查 / 旧检查重跑 / tiny cone | 0 / 0 / 0 | 只读已付 6、12、11、9 条收据 |

## 2. 完整 161 维实际返回已保存

本次新增记录补全了此前 MaxTime31 未保存两个辅助坐标的边界。没有反推旧返回；新记录直接取本次真实 `solution.x`，发生在状态过滤、原线性门和完整模型修复之前。

原生 `FINAL_CONE32_MODEL` 的
`finite_cone_primary.cone_calls[0].actual_complete_solver_vector_record`
完整保留：

- 161 个原求解变量的 binary64 精确有理字符串；
- 159 个原 step scale，以及实际缩放后的 p159；
- 原 rho、原 norm 辅助坐标及其精确有理字符串；
- 当前完整模型 binding、向量指纹和“在 filter 前捕获”的来源说明。

逐字段消费确认数组长度为 161/159/159；rho 与 norm 字符串分别等于原 161 的最后两项。该 event 与 COMPLETE 的 `all_current_cone_events[0]` 逐 JSON 相同。保存证据为 finite return 1、完整保存 1、`all_finite_returns_saved_in_full=true`。完整向量只在 runner 临时文件和原 Actions stdout；本笔记不复制数组，不将其提交 Git、artifact 或 cache。

| 原返回字段 | 实际值 |
|---|---:|
| backend / version | Clarabel 0.11.1 |
| backend status | AlmostSolved |
| 原 rho | 0.00601227823232846 |
| 原 norm auxiliary | 0.2700481333050534 |
| 原 rho 精确 binary64 | `3465842432865561/576460752303423488` |
| 原 norm 精确 binary64 | `2432377345049473/9007199254740992` |
| 原 161 array SHA256 | `b0e02cfc169219be1709155bcb9c0e50b771655632fc767194394ba69444e79f` |
| 原有限模型 objective | 0.006012548280461764 |
| 记录的最大独立 / 物理分量绝对值 | 0.003996019317473696 / 0.003996019317473696 |

最后一行是分量大小，不是统一 trust 半径。原真实 step-cost 诊断另给 common-body norm $0.000249751207342106$，trust utilization $0.9990048293684239$，height utilization $0.2630728608407475$，tail utilization $0.9963623967932412$。这些是本次原模型记录，不能混同原 norm 辅助变量，也不能据保存了向量而宣布实际几何可行。

## 3. 有限锥校验通过，完整网格修复撤销了改善

本次 Solved/AlmostSolved 的原候选名单不变。状态只允许进入后续校验；原 linear/box、完整 affine rho 修复、included-cone 半残差和实际几何门均没有豁免。

### 3.1 有限模型与原单位残差

实际组装为 161 变量、33,212 条 conic 标准式行，其中 10,168 条 nonnegative-cone 行与 5,761 个四维 Lorentz cone。原线性行 9,327、有限盒行 321；保留的 520 条支持由原 bank 512 条与原 supplements 8 条构成。同 row 的不同法向没有被替换删除。

| 校验量 | 原返回 | 完整 rho 修复后 |
|---|---:|---:|
| 最大原线性行 violation | 0 | 0 |
| 最大原盒 violation | 0 | 0 |
| included cone 最大 signed residual | −1.0360385915841874e−7 | −3.494965341310774e−5 |
| included cone 最大 signed 半残差 | −5.180192957920937e−8 | −1.747482670655387e−5 |
| 直接 metric signed residual | −5.180192956706631e−8 | −1.747482670655387e−5 |
| metric violation（原报告正部） | 0 | 0 |
| direct 与 half-cone 最大差 | 9.8879238130678e−17 | 8.326672684688674e−17 |

半残差与 metric 单位的因子 2 是原组装规范。表中的 signed 浮点量原样保留；没有将微小负数裁为“精确零”，也没有把浮点残差门称为连续或符号证明。

曲率 proposal guard 保留同一冻结学习状态：粗 $\gamma=57.187653029922444$，细 $\gamma=67.42701956990882$，$B=0.00025$。本模型实际改动 4 条 fine group 8 target，粗网 0 条；原 SOC RHS 未改。本次没有 SOC 调用。不能从本次停因倒推这四条 guard 是下降失败的原因。

### 3.2 完整两网四分支的实际读出

原完整两网 affine oracle 对这个真实新方向执行一次方向求值、两次完整网格扫描。四个分支的最大值如下：

| 网格 / group | 原 flat row | 原位置 | 完整 affine $\phi$ |
|---|---:|---|---:|
| coarse / 0 | 26651 | $t=3/10,\ \theta=155\pi/192$ | 0.26601216360578817 |
| coarse / 1 | 78136 | $t=57/400,\ \theta=23\pi/24$ | 0.26601218098704726 |
| fine / 0 | **87417** | **$t=3/5,\ \theta=211\pi/128$** | **0.26602970125710546** |
| fine / 1 | 162463 | $t=39/200,\ \theta=415\pi/384$ | 0.26601222014309517 |

fine 87417 是实际新分离行。其原点索引为 87417，radial index 113、theta index 633，group 0；affine $e=0.15395072547750757$、$f=-0.17267407577238905$。这些是本次已付 oracle 的原输出，不是额外重算。

| 完整模型量 | 实际值 |
|---|---:|
| 基点 complete slack | 0.0060182947853382185 |
| 原求解 rho | 0.00601227823232846 |
| 完整网格所需 rho | 0.0060297012571054465 |
| raw epigraph gap | 0.000017423024776986804 |
| gap tolerance | 0.000000001 |
| gap met | false |
| 修复后 objective | 0.006029971305238751 |
| 完整模型 gain | **−0.000011406471767227977** |
| positive above original floor | false |

完整值把 rho 上调，保留原 norm auxiliary，原修复行/盒残差仍为 0。outer 依旧执行 `no-evaluated-affine-model-improvement-above-original-floor`，没有把负改善候选送入普通值验收。

本模型随后登记新的 finite cone tag 87417，使 distinct cone rows 从 5,761 增到 5,762。原第 32 次调用已收费，故没有对扩展后的集合再求解。原状态记录为：

- `new-cone-total-or-per-model-call-limit-after-new-row-observation`；
- `returned_candidate=false`；
- `returned_epigraph_gap_met=false`；
- `returned_inexact_cut_model=true`；
- `returned_inexact_finite_cone_model=true`。

这是完整网格覆盖未合的直接证据，不是已经获得完整凸模型最优解，也不是实际非线性曲率或下降门失败。

## 4. 原物理点、全部实际门与信息状态

### 4.1 同一个真实第 52 点

恢复保留原 g、b0、固定参考、九物理高度与五 null 坐标、159→163 映射、原 quadrature 和两网。没有重新初始化池，也没有自动加入另外的 minima rows。

| 身份 | SHA256 |
|---|---|
| 第 52 点 physical | `0c03e09059cac846ec5ab6a246236c52b42d28394930aa35759953ea2ce1fc21` |
| configuration | `1c8a50e50f7428e61e5fc6aedb258c857afff72c1819b2f7950677f014964e19` |
| ordinary direct-reference field | `8e77c49888fce6d8abe6b02f2e9a0a7651d4b76ef83328b3d134a2adde697ab1` |
| factorization | `b6cc198b6b58ec0484438c910a1e05a1273bc0cec81715415b8f538d31661963` |
| 恢复的 affine objective | `e101bd909dbdb5fb2c7f839b2d416b66e473bf7326dfb80e7af396f3f97a26b6` |

上一 value-only objective 身份 `d6008a66f2939258d1b5b3f752e4f3f5235f242ca83b52bcd2b44479b376e336` 只作来源。新完整模型以当前基点、当前两池 13/13、真实新 J 与两 observable factories 建立 binding；没有拿旧 value-only policy hash 冒作 affine 模型证明。该 affine SHA 的权威原字段为 COMPLETE.actual_definition_hashes；它没有被 value-only 身份替换。

实际同过程恢复的粗/细值分别为：

| 量 | coarse | fine |
|---|---:|---:|
| 最大 $\eta$ | 0.26601808038739305 | 0.2660182947853381 |
| 最大绝对 principal curvature | 57.997683374142156 | 57.999249547251196 |
| 最大归一 ball radius squared | 0.9905298063857301 | 0.9905298064299818 |
| 最小 direct mirror radius | 0.09760999647422229 | 0.09760999647446612 |
| inner strip absolute margin | 0.000001439579471518293 | 0.0000014395822110491174 |
| minimum signed height | 0.02 | 0.02 |

全部 14 原门在两网均为 true：cap/box、curvature lambda、curvature scaled PSD、hard ball、hard strip、independent direct curvature、independent direct mirror radius、mirror polynomial、outer strip、previous metric budget、regularity screen、signed height、single-grid admissibility、single-grid hard gate。原精确 163 盒 violation 为 0。旧 $167/625$ metric budget 通过；新 $13/50=0.26$ 目标未达到。

affine 与重构 cap 高度 margin 分别为 −2.7755575615628914e−17、−5.551115123125783e−17，按原 $10^{-9}$ height tolerance 合格；不能称两项当前浮点 margin 都非负。精确物理盒与这项浮点高度容差严格分开。

最终收据引用未改变的第 52 点原两网完整实际门，本次新恢复的两网门另保留；没有增加独立 final audit 值。逐 JSON 消费确认源与末端完整159、完整163、两池数组、学习 checkpoint 和8条 supplements 完全相同。

### 4.2 新 finite cone tag 不等于新 actual pool row

最终 coarse/fine 池仍为 **4448/4544，版本13/13**，fine 159001 保留。B 仍为 0.00025，legacy/covered 两 streak 都为 0。因为没有任何物理 trial，本次没有实际 pool learning、没有曲率 defect 新样本、没有半径增长或 hold 成功。

学习保持 62 events、61 commits、pending0；原 SHA
`b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76`
不变。模型前的 pending commit 记录是空变更；没有重放旧样本或伪造更新。

bank 的变化来自本次真实完整 affine 方向的四分支观察：

| bank 量 | 来源 | 本次末端 |
|---|---:|---:|
| entries | 512 | 512 |
| insertions（含更新） | 4962 | 4966 |
| evictions | 73 | 74 |
| inward binary64 adjustments | 2562 | 2565 |

来源 bank SHA `b240dfd9aad4ea6052eec24590b7147102d1f180be1e9c364f5ba996ed1a47cb` 已核同。末 bank SHA 为
`233b2e81fdd0ab36f3306d2d901e8708bb103ea34c9c20ef006537d371634527`。
这不是把四条新几何约束加到实际池。旧 512 支持与 8 supplements 在本次已组装的 A/b 中保持，bank 淘汰没有回头删除当前有限模型的原行。

## 5. 真实费用与两个终钟

所有新增输入读取、必要24输入 prepare、冷普通值、J、模型与后端调用都计入原批准的累计科学钟。没有把冷恢复费用改名排除，也没有重开原 64 HiGHS 或恢复旧耗尽 m7 epoch。

| 权威最终账目 | 实际值 |
|---|---:|
| 本次新增科学秒 | **195.33557086899998** |
| 累计 finite-cone task 科学秒 | **968.6757049859999 / 1200** |
| 累计原独立 task 科学秒 | **1324.8055252469999 / 1800** |
| 双钟交集剩余科学秒 | 231.32429501400009 |
| 本进程总秒 | 196.619314745 |
| 峰值 RSS（Linux KiB） | 977984 |
| 本次 full value | 2：粗1、细1 |
| 累计原 full value | **124 / 160** |
| 累计 cone task full value | **62 / 96** |
| 粗/细累计计数 | 62 / 62 |
| cone task solver | **32 / 32** |
| 本次 legacy LP / SOC | 0 / 0 |

钟与 value 尚有余额，但 solver 调用限额真实耗尽，不能用余额自动授权 cone33。旧64也没有再次可用槽。

| 当前 attempt 的观测段 | 秒 |
|---|---:|
| 最新已付日志读取及验证 | 2.66186871699999 |
| 必要24输入 prepare | 14.390490995999997 |
| 新恢复 constructor | 0.1591614149999998 |
| 同过程恢复/J/cone/outer | 177.89031182800002 |
| coarse ordinary wrapper component | 110.422912532 |
| fine ordinary wrapper component | 19.229492125000007 |
| direct adapter 两次 geometry 合计 | 129.486163084 |
| coarse selected J，1 refresh / 10 batches | 8.432646029000011 |
| fine selected J，1 refresh / 27 batches | 25.74874843699999 |
| 全网方向求值，1次 / 2 scans | 0.636909151999987 |
| 新请求原 metric J，24行 | 0.8813601470001231 |
| finite-cone row preparation | 0.15900152799997613 |
| conic assembly | 0.30490199600001233 |
| 原520支持恢复 | 0.9106050689999847 |
| backend constructor | 0.45767019900000605 |
| backend 自报 solve time | 10.225351891 |
| event 的返回前 elapsed | 10.394972719000009 |
| 完整 call + repair elapsed | 11.260506270999997 |

这些是各自原有作用域，部分包含于更大段内，不应相加再收一次费。settings.time_limit 实际为10秒；backend自报及完整调用观测值大于10，不能声称严格 wall≤10。实际费用全部进入累计账。

粗调用中 reference fixed-height primitive 首次 prefix-miss 101.695936018秒，reference height jets miss 8.502939232999992秒；细调用复用二者，当前 scalar grid 的 miss 为18.772040916999998秒。这些是本次直接记录，不是对旧205秒冷调用的因果分摊，也不用于编造受控加速结论。

COMPLETE.continued_science_account 是最终权威双钟。ledger 当时的968.6255583899999/1324.755378651，以及更早 stage/checkpoint 时间均只是早拍快照，不能用来少计后续报告工作。组件计时以“本 cone32 attempt”标记；此前 value-only 未导出的内部组件总数不补猜，历史收据单列。

## 6. 输入闭包、已付收据与公开规则读取

本次 REQUEST 文件为40,422 UTF-8字节，
SHA256 `39458fd2dff42510a5719491e2402ce37ef69663986eecf11896b10a21c2e332`。
189个绑定逐key等于冻结请求，组成170 Python、12 workflow、5人类MD和2 JSON；170 Python与COMPLETE源码表完全一致。原182依赖逐项保持，原98 CLI 参数保持。只恢复必要24输入一次，没有执行旧开发、旧求解或原 trial。

来源唯一原日志为已完成的 `43798128882 / 133071559203`；原字节/hash及其 REQUEST、DEVELOPMENT、PRIOR、COMPLETE 的 JSON+LF 指纹都按请求核对。6条已付 actual-only 检查、12条 cone 检查、11条 terminal 检查、9条 geometry 检查传递复用，本次执行数全部为0。源实际结果的人类正式出处为 [上一实际笔记](paid-MaxTime-vector-first-actual-and-new-soft-row-20261116.md)。

真实公共 pull：
03:50:48.715598→03:50:51.529447Z，
`8dfe5272b6d4f4fb752c8962689b22a95c61f78a`
到
`063c8643c68fe6a8b2fe0b7ef3f65cba666dd047`。
根 README blob `21bd547f56590b7f2dd279d0297efb289a9b2783`、本题 README blob `d0432faff569c8e9af7ed4809847e12880976c11`，均 empty diff、匹配预期。拉取后按冻结 scientific source 继续；main 的其他课题更新没有代替本题计算源。

真实私有 pull：
03:50:53.796482→03:50:54.369582Z，
before=after `997ba691fad6ae531d0ada2deee68c7039d98aac`。
根 README blob `5ba164843b1f5802184178a82d786264404873a3`，本题私有 README 不存在；原记录为规则未变、QUEUE对本会话唯一且进行中。私有内容不发表。

## 7. 原始证据指纹与保存范围

原 decoded stdout 被只读消费一次，UTF-8为 **3,503,842字节**，
SHA256 **`445108ab5e8b15822331bcf080388969a51dc3021d0eda6937759fedae20306f`**。
下表统一为原tag JSON子串加一个LF；不能与无LF字段混用。

| tag | JSON+LF字节 | SHA256 |
|---|---:|---|
| PUBLIC_PULL | 1945 | `b1b8a74552765df58ba9007f08f35c5ac291a3c9f963c2d62c077f31b41d42cb` |
| PRIVATE_PULL | 584 | `897dfa439ea0dd8bb776f78deeab48503341e623b1c89cc5777d274df00e63e1` |
| REQUEST | 29716 | `f8e22d359d911ee1075e08041f19a1ca966e75707cb93711c7f4f6d22acaf13f` |
| PRIOR_WORK_REUSED | 5185 | `641f4b9933fd82c0587d75fe00c473254aed58b357222d2b409640ad8028d083` |
| MODEL | 122226 | `c10a67934b49edeb0b87b1612cb281f59b26449470b4fb54eb8e85ceac9e6d8b` |
| COMPLETE | 3251685 | `1f029b442de75b27baec55352d0dee72d3d4fc753f8202f2291f99a18da08e1f` |

runner临时完整audit文件16,661,048B，
SHA `f9ce82469d308ec3137c4bf0a5eec7a6e779dea59af0ccc380b3fe47a0b4e201`；
临时summary文件5,844,046B，
SHA `496b72d851cdd0340784cf9582ff3d7973ec3e7bc48a3d08fcba4a4191b322c1`。
文件均未提交仓库、上传artifact或跨run缓存。原native MODEL、COMPLETE足以保本次161和未来真实checkpoint；本笔记只保存人类结论和来源元数据。

权威 affine objective SHA 为
`e101bd909dbdb5fb2c7f839b2d416b66e473bf7326dfb80e7af396f3f97a26b6`。
该身份与原状态、当前新factory binding必须分别使用。

## 8. 已定位的下一问题

新的、已证实的障碍是：**有限锥候选在已纳入集合内通过原残差，但完整两网有未覆盖的 fine 87417；rho修复使方向丧失模型改善。** 新行被观察并登记时，32次真实求解配额已耗尽。因此后继若另立新方法，必须针对完整网格覆盖与有限模型分离效率，明确新的方法、费用与恢复合同；不能以本轮success、剩余墙钟或一个新增tag为由原样续33，也不能把64旧LP重新打开。

一个具体尚未做的问题是：本次已付 p32 在 $0<\alpha<1$ 上的完整两网仿射谱包络，是否仍有严格下降区间。$\alpha=1$ 被 fine 87417 抬高不证明整段都不可用；这与旧 p31 已试的三个尺度不同。先纸面核原沿线凸性、必要输入与当前单方向 JVP 接口，再决定是否另立标量包络方法。若要实际求解或采样，必须单列其调用和费用，不能以“无新大维求解”将标量求解记为0。

当前没有实际非线性 trial，故不能归因于实际曲率失败、实际学习失败或目标下降门本身。完整161虽已保存，也不使这个负complete-gain方向自动成为合格物理提案。后继从真实第52点、当前512 bank、8supp、4448/4544池13/13、62/61/pending0学习状态与最终968.6757049859999/1324.8055252469999双钟出发；具体新方法另行成文，本笔记不授权任何新执行。
