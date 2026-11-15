# 原单位曲率缺陷提案 guard：首次完成的实际结果

日期：2026-11-15（UTC）。

**本轮从已核对的当前最佳点继续一次，六个普通全步被真实双网门接受，最大 metric 值由 0.2662701215525791 降到 0.26623355613853394。七个 guard 模型都进入实际启动的 LP。第七模型只完成一次内部 LP 就碰到本模型的配额上限，凸 epigraph 分离尚未闭合；它没有接受点，也不构成驻点或无下降方向证明。** 原共享总额只用了 10/12 次 LP，剩余两次没有执行。

策略 same159-observed-curvature-defect-primary-guard-v1 只把此前实际观测的原单位曲率线性化缺陷用于下一普通提案的 target；原几何、坐标、目标函数、真实门、SOC RHS 和总预算保留。本稿消费原公开输出及只读观察器摘录，没有重跑科学、旧开发或旧优化。

## 1. 原运行与输入闭包

科学 run **43767357527**，job **132975354666**，于 **22:12:04 UTC** 成功完成；计算 source 为 6f886c385bdc12c8963d451369c9250fa19a45a0。[原 Actions 运行](https://github.com/Rogerhu12/math-research-public/actions/runs/43767357527)。

request 为 computations/request-curvature-defect-guard.json，36,687 B，SHA-256：

f85013ec1af5d3e14881412708f14228252d160953f9eddebd78cca281164cc4。

原 request 的 **146 项**绑定为 **140 个 Python 源文件和 6 个 workflow**；原 DEV 与 COMPLETE 自报的 140 个 Python 源与该 request 一致。旧输入及开发只按已付来源消费，不冒充本轮新执行。

唯一新继续点来自 run43762868037/job132961344492/source4f1365300b70831550d544df119d738b2531eff5 的完整 future checkpoint；原其他已完成输入仍按协议消费。初始 375 项 norm bank 原顺序与 SHA 470bf8bb51da18007e90e1c8bd11d3ca4fd7e5f3487a5bec375860b184d2fbad 准确恢复，没有事件重放、旧 optimizer 重跑或重选 reference。初始 coarse/fine 的 $\eta,\kappa$ 与来源差均为零。

source configuration SHA 保持 b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6。原 $g,b_0$、永久 anchor、159 自由坐标与完整 163 物理重构不变；新增策略经独立 policy 接口声明，不改冻结 configuration。

## 2. 开发失败、最小修补与真实执行数

首轮 run43766593534/job132972995287 在新开发第 4 组失败，科学尚未开始。人工 stub 对只读 property 赋值 self.fixed_zeta=shell.fixed_zeta，产生：

“AttributeError: property 'fixed_zeta' of 'CurvatureDefectGuardObjective' object has no setter”。

前三组 5、5、4 项，共 **14 项已经通过**。修补只删除第 4 组的假赋值，并加入严格读取原失败回执的复用入口；生产 core、recovery 和旧科学源不因该修补改变。

| 开发组 | 完整 verdict | 本轮实际执行 |
|---|---:|---:|
| 原 RHS 范围及两 factory 最终绑定 | 5 项全过 | 0，复用首轮已过记录 |
| 实际总步与延迟学习 | 5 项全过 | 0，同上 |
| 原 SOC 与提案不可行范围 | 4 项全过 | 0，同上 |
| 375 项入口与已付样本连接 | 4 项全过 | **4 项新检查** |

因此 18 项 verdict 全真，本轮只执行第四组 4 项。恢复核对包括原失败 run/job/source、log/DEV hash、无 MODEL/COMPLETE 的科学零执行边界，以及仅 audit/dev 两份变化、其余 138 Python 源与 6 workflows 保持。首失败日志 170,214 B，SHA-256 746f42b542f9d424b9fc2287238f925b2437290b72733e5ee0b95b2c6bd06043；该失败事实保留。

## 3. guard 的准确作用范围

对已绑定原中心 $x$ 与第一次真实普通全步 $y$，使用实际 $d=y-x$，共同块范数为

$$
b_{\rm actual}=\max\{\|d_{\rm body}\|,\;8\|d_{\rm tail}\|,\;\|d_{\rm height}\|/4\}.
$$

在同一历史 row mapping、同一中心 base/J 与同一 coarse/fine selected group 8 上，读取

$$
\delta_{\min}=\min_i\{m_i(y)-m_i(x)-J_i(x)d\},\qquad
\gamma_{\rm obs}=\max(0,-\delta_{\min})/b_{\rm actual}^{\,2}.
$$

只有有限、严格正的实际范数可以更新，原带符号缺陷保留。下一普通模型冻结已提交最大系数，只改相应 target：

$$
t_i^{\rm guard}=\max\{t_i^{\rm original},\;10^{-7}+\gamma_{\rm grid}B^2\}.
$$

这里三个范数均按对应原物理宽度归一化并取无穷范数；height 使用九个真实重构系数，不取五个独立高度坐标的范数。

这是经验提案规则，**不是跨中心误差上界、连续曲面证书或所有未选行的误差界**。原 A、目标系数、boxes、trust、J、行顺序及实际门容差不变；rebound/SOC 仍用原 selected model 和原 RHS。历史样本的旧池版本在其原绑定内部核同，并不要求等于当前已重新初始化的池。

七模型均报告 both-observable-factories-final-bound，最终绑定在两次 observable factory 更新之后形成。每模型 eligible C/F 行数为 243/411，零 J 行计数均为 0。更严格的原 target 保留，所以 eligible 不等于实际修改。所有七模型在建模后都启动了 LP；总 52 次 target 修改是跨模型的计数和。

## 4. 七模型与原控制器

所有模型 $B=0.00025$。前六个均在第一次普通 $\alpha=1$ 试验通过真实双网门，没有 backtracking 或 SOC 接受。

| 模型 | primary LP | guard 修改 C/F | 重装 memory 行 | 真正新 cut 行 | 完整 ratio | 结果 |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 2 | 4/8 | 375 | 12 | 0.7904412065310875 | 普通全步接受 |
| 2 | 1 | 4/8 | 375 | 0 | 0.36968573367341134 | 普通全步接受 |
| 3 | 2 | 4/8 | 375 | 298 | 0.850856641542943 | 普通全步接受 |
| 4 | 1 | 0/4 | 437 | 0 | 0.642676308926799 | 普通全步接受 |
| 5 | 2 | 0/4 | 437 | 1 | 0.6796866772352804 | 普通全步接受 |
| 6 | 1 | 0/4 | 438 | 0 | 0.7486474513153537 | 普通全步接受 |
| 7 | 1 | 0/4 | 438 | 0 | 未作物理试验 | scoped ceiling，未取得改善提案 |

前六模型 returned gap 达标、returned inexact=false。第七 gap 未达标、inexact=true。原字段 total_new_cut_rows 含 memory 重装，逐模型为 387、375、673、437、438、438、438；扣除重装后，真正新 cut **311**，memory 累计重装 **2,875**，报告总计 **3,186**，后者不能全称新 cuts。

六个实际 trial 的 coarse/fine 学习行数均为 0。fine pool 初始化由 4,451 增至 4,525，不是六次接受 trial 新学到 74 行。

legacy 与 covered streak 同步为 $0\to1,1\to0,0\to1,1\to0,0\to0,0\to0$；只有模型 1、3 合格且各累计一次。没有 pair、没有实际半径增长。SOC 启动/接受、same-layout hold 接受和 expanded hold 接受本轮均为 0，不能用本次结果验证这些未触发分支。

## 5. 学习与提交次序

两个已付样本来自来源运行的模型 2、6，其 C/F 系数为：

- paid m2：$(8.04055201441574,\;7.87327242334797)$；
- paid m6：$(3.743864819491791,\;4.672718505013483)$。

初始最大值取 paid m2，首次消费于模型 1。两个已付样本和六个新样本的实际 $b_{\rm actual}$ 都为 **0.0002500000000000835**。

| 新样本来源 | $\gamma_C$ 观测 | $\gamma_F$ 观测 | 首次提交/消费模型 |
|---:|---:|---:|---:|
| 1 | 4.571398664051929 | 7.7035490710867975 | 2 |
| 2 | 4.446585115222363 | 5.511132054710416 | 3 |
| 3 | 2.2994261081861387 | 7.259910434593434 | 4 |
| 4 | 15.933091523468352 | 18.064283125328743 | 5 |
| 5 | 17.022353404161095 | 17.82455190467633 | 6 |
| 6 | 14.563037818317293 | 15.595113578282382 | 7 |

模型 1–4 冻结初始系数。m4 样本在模型 5 同时抬高两网；m5 样本在模型 6 只抬高 coarse。m6 不再抬高最大值，但仍于模型 7 正确提交。

最终 $\gamma_C=17.022353404161095$、$\gamma_F=18.064283125328743$。初始 C/F allowance 为 $5.025345009009838\times10^{-7}$、$4.920795264592481\times10^{-7}$；模型 5 为 $9.95818220216772\times10^{-7}$、$1.1290176953330466\times10^{-6}$；模型 6、7 为 $1.0638970877600683\times10^{-6}$、$1.1290176953330466\times10^{-6}$。

共 8 个事件全 committed，7 条完成的提交记录，pending=0，没有只在最终化入账而未被模型消费的样本。本模型 targets、cut 模型及原 SOC 预算不被当轮观测追改。学习仅消费已算诊断，不新增值/JVP/J/LP 调用。

## 6. 第七模型不是驻点证明

进入 m7 时 ledger 已启动 9 次 LP、余 3 次；pair allocation 给 primary 配额 1，临时绝对 ceiling=10。唯一 inner LP 完成后：

| 原字段/数值 | 实际 |
|---|---|
| status | new-pair-allocation-primary-ceiling-reached |
| inherited stop | original-shared-LP-budget-after-inner-call |
| returned candidate / gap met / inexact | false / false / true |
| global exhausted | false；10/12，余 2 |
| relaxed slack | 0.006225515688006198 |
| 全原网格浮点 affine slack | 0.00625028436741315 |
| gap / 原容差 | $2.4768679406952238\times10^{-5}$ / $10^{-9}$ |
| 模型 base | 0.0062335561385340466 |
| repaired predicted improvement | −0.000016728228879103746 |
| repaired objective | 0.0062505343674131505 |
| 原行 residual / bound violation | 约 $2.1938\times10^{-19}$ / 0 |
| 物理评价前拒绝 | no-evaluated-affine-model-improvement-above-original-floor |

本模型只有 438 行 memory 重装 cut round，没有新分离 cut round。cut 下界与全原网格浮点 affine 值仍有缺口；rho 修复后该方向不改善，因此没有真实几何试验。outer 的 affine-spectral-finite-model-stalled 是这条返回路径的状态名，**不是完整凸子问题驻点、guard 不可行或真实无下降方向的证据**。

后继必须先核是否能从原报告恢复同一 $x$、冻结 guard/B、两 factory 最终绑定、已付候选、完整 oracle、memory/cuts 与原 LP 返回状态。若可恢复，可研究只释放 **1 次剩余 LP** 给这个已启动且尚未物理评价的模型，仍留 **1 次 SOC**、每模型至多 3 次、全局至多 12 次。不能重新调用已付第十次 LP，也不能重置 epoch 后把同一阶段再跑一次。该续算尚未发生。

## 7. 最终真实门与可继续状态

| 指标 | 初始 | 最终 |
|---|---:|---:|
| 最大双网 $\eta$ | 0.2662701215525791 | **0.26623355613853394** |
| coarse $\eta$ | 按来源 exact 恢复 | 0.2662325332209649 |
| fine $\eta$ | 按来源 exact 恢复 | 0.26623355613853394 |
| coarse $\kappa_{\max}$ | 按来源 exact 恢复 | 57.99651016191997 |
| fine $\kappa_{\max}$ | 57.99998346840656 | 57.99982504159888 |
| $B$ | 0.00025 | 0.00025 |
| norm bank | 375 | 438 |
| C/F pool | 4432/4451 | 4432/4525 |
| legacy/covered streak | 0/0 | 0/0 |

真实 $\eta$ 下降量为 **0.00003656541404517544**。末两网 14 项原门全部通过，旧 metric 门 $167/625$、精确原 163 物理盒，以及既定容差下的 affine/reconstructed 高度门通过。新 0.26 目标与 reach 所需曲率目标仍未通过；原网格门不等于连续曲面最终构造。

affine cap margin 为 $-2.7755575615628914\times10^{-17}$，reconstructed 为 $-5.551115123125783\times10^{-17}$，按旧容差通过；它们不是“两网各一项”，也不能称都非负。

bank 容量 512，末 438 项，insertions=626（含更新，不等于新增数），evictions=0；pool versions 为 1/2。末身份：

- physical：e0ab278d1525c90a2be30db12c78e6faac369a8b8d01f0236f4fe6fd02e79f83；
- bank：1a1d55857ed7ae7734054126cec38c9d99e72ce144ab321152c3f5fab8fd10fd；
- coarse pool：2960646cf6cb902c0bd7a7169b969289d2b2209b88405c517df5998f5da938b4；
- fine pool：63a4841131b6b8c93b26b3b894f1d059a5621b6f549f4bf1033846ec80f68122。

后继应保真实最佳 checkpoint 和全部已提交学习状态；末 checkpoint 本身不能替代 m7 同模型续算额外需要的候选/cut 状态。

## 8. 费用与预算

| 原费用字段 | 本轮实际 |
|---|---:|
| prepare / audit / total | 19.541142686 / 302.426617314 / **321.967762679 s** |
| active | **35.542398458 s** |
| initial ordinary audit | 230.773521914 s |
| recovery，含 pre-active 首次 J | 69.926718499 s |
| snapshot init | 264.864081096 s |
| ordinary value geometry | 212.695708700 s |
| coarse selected J | 70 batches、7 refresh、11.426430244 s |
| fine selected J | 189 batches、7 refresh、32.190080708 s |
| primary / SOC LP | 10 / 0；10 次 LP elapsed 合计 5.200563002 s |
| 完整普通值 | shared14 + independent final2 = **16**，cap40 |
| 峰值 RSS | **2,292,208 KiB** |

这些计时起止边界不同且有嵌套，不能相加成另一份总耗时；active 35.54 s 也不是整次成本。原预算保持共享 LP12、值40、active120 s、每次 LP10 s。

逐模型完整 oracle 新方向为 3、2、3、2、3、2、1，合 16；原两网扫描合 32，方向缓存命中合 19。新 metric J 行为 1、1、2、2、3、3、3，合 15；对应秒数 .055909207、.014816953、.069893936、.028922774、.083451936、.043038296、.042970068。新方向秒数为 1.933801726、1.294872796、1.945274607、1.295897721、1.946642515、1.301584060、.647895134。

六次接受且无 SOC 只是本轮观察，不能单独归因为 guard，也不能推出旧 SOC 不再需要。不同起点、pool、memory 与提案没有受控反事实比较；不为比较重跑已付阶段。

## 9. 原日志与只读观察器

原 decoded-log 传输两次关闭，后续观察器只读同一已完成日志。首次观察器 run43768982932/job132980381937 取得日志并核 146/140 来源，但语义输出 589,111 B 超过 180,000 B cap，按设计输出 LIMIT；这是观察输出限制，不是科学失败。

第二观察器 run43769144830/job132980891310/sourceb9e9a4db978f3acc4910171c96176e9d03b9364f 仅把 cap 调至 660,000 B，并强制核原 raw log hash，完成回传；没有重算数学、开发或优化。payload 只在 runner 内存与读取会话处理，未入 Git、Release 或 artifact。

| 对象 | 字节 | SHA-256 |
|---|---:|---|
| 原科学完整 job log | 7,918,876 | 8ce149f015b3139625e9a3ee887b407977ca4c7ca94387379e98dc986fe730af |
| COMPLETE JSON，不含 LF | 1,700,301 | c306ca6368fe7fb4f777858b566f81c801afb2debc6e059df0e2676fc3bedd47 |
| COMPLETE JSON + LF | 1,700,302 | 6208d8519e766141b46a70a329fb9ae84b9ddbfb8617016b85304a50b9a26194 |
| 本次 DEV JSON，不含 LF | 19,970 | 82e5f40f00bb2e3f2191b6a13fcaa7a98ed60ce381f42a06b497e23d7255998c |
| 本次 DEV JSON + LF | 19,971 | 3ebcbca7879e037789654972d7b45d5b2ea793de1a58fab9113170e54c4de39a |
| 第二观察器完整 job log | 661,449 | ce508cd8fe6731b6d9f6d8537603277b190b7a9d1ea0541c14d7f7fc1d027e6b |

## 10. 实际规则读取与后继边界

原科学 public pull：22:06:29.231742–22:06:29.655622，前后均 6f886c385bdc12c8963d451369c9250fa19a45a0，根/topic README 差为空。private：22:06:32.193424–22:06:32.670915，前后均 dd689fa33c46c0286d5eddddc2bfe105d9687a48，无规则差。

第二观察器 public pull：22:24:53.429013–22:24:53.746489，前后均 b9e9a4db978f3acc4910171c96176e9d03b9364f。private：22:24:57.511497–22:24:58.201128，前后均 a34d073f4953f813941665f1156d432f492dbaab，无新差，QUEUE 保持本会话 ongoing。

已核规则 blob 为：public 根 21bd547f56590b7f2dd279d0297efb289a9b2783、题 d0432faff569c8e9af7ed4809847e12880976c11；private 根 5ba164843b1f5802184178a82d786264404873a3。

下一项工作已授权为 m7 精确恢复与同模型有限续算接口。需要的数据缺口应明确列出，不能通过重跑旧 primary、改目标、放宽门或增加总预算掩盖。原六次接受、真实最佳点、首开发失败、观察器 LIMIT、未合模型与未用额度均保留。
