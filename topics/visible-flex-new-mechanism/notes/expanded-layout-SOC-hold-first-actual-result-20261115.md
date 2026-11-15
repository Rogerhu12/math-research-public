# 扩池小校正保半径策略的首次实际：七个接受模型，策略未触发

日期：2026-11-15。作者责任：tail_cost 消费本次公开 Actions 的已完成原日志；root 负责独立读取与正式发布。本稿没有执行新的科学计算、人工测试、旧优化重播或检查复跑。

本次从已发表的 current-best m7 完整检查点继续，双网最大实际 metric 误差由 **0.26634752076125723** 降至 **0.26632415509189855**，下降 **0.00002336566935867701**。七个模型均产生一个新的实际接受点；前六个接受全步，第七个先拒绝全步，再接受半步。最终两网物理与曲率门、原物理盒和旧 metric 预算均通过；新目标 13/50 仍未达到。

**本次没有执行 SOC：accepted expanded SOC、符合新保 B 条件、下一个模型实际使用被保留 B，三项计数全部为零。** 因此只能确认新接口公开通过、准确检查点接入与这一段真实进展，不能将下降归因于新保半径规则，也不能据七次接受宣称该规则改善收敛。本阶段不因策略未触发而原样重跑。

## 1. 唯一公开运行及准确来源

- Run：43753280651；job：132931742484。
- 计算 source：52a48854e30ddc3d2351ec24274dbe222ef05d9a。
- [原 job](https://github.com/Rogerhu12/math-research-public/actions/runs/43753280651/job/132931742484) 于 19:41 UTC 成功结束。
- 工作流：.github/workflows/visible-expanded-layout-hold.yml。
- 主 schema：same159-current-best-covered-expanded-layout-SOC-hold-v1。
- 实际状态：complete-two-grid-covered-expanded-layout-SOC-hold-audit。
- 科学阶段退出：shared-primary-plus-SOC-LP-budget-exit；error 为 null。
- 新 policy：same159-covered-expanded-pool-small-SOC-retains-model-radius-v1。

请求原件为 31,451 B，SHA256 为 c9d4d2ead7efd0ecd0fbbccc3b53bdbefedce431d772f46bf7becd2906b22346。请求绑定 128 个文件，即 125 份脚本和 3 份 workflow。逐项把 COMPLETE 中 125 个 basename 转回 topic/scripts 路径后，全部源码 SHA 与请求吻合，没有不匹配项。

五份本次新入口的实际 SHA256：

| 文件（scripts/ 下） | SHA256 |
| --- | --- |
| frame_metric_expanded_layout_hold.py | 69ce5f724b6642d094537c36a9778834e8ef6ec2911feb663cd752c1c6cd2ae8 |
| frame_metric_expanded_layout_hold_recovery.py | f16d7803c37f85e558cf58587af907e278726551aee4fac7dbade7a5d6363cbc |
| frame_metric_expanded_layout_hold_development.py | 960c59aea0ca64a3b1993553415ce49b43592e1297cfe2bec2d41a1e0df6f88c |
| frame_metric_expanded_layout_hold_transfer.py | db9fc9ca1b6995a81c009268bf5ad53690ccd60e842b66518479a001a86743a7 |
| frame_metric_expanded_layout_hold_audit.py | cde42fcbaff2a47fd1f74d92cb1cbc7e6595571d4b70facccfaf50e98663c841 |

原 configuration 保持不变；新算法声明独立记入 evaluation/request。沿用 159 独立坐标、163 原物理系数、原 g、不可变 b0、原 reference163 与五维 exact-null 高度模型。没有重新锚定高度或改变实际门、容量和预算。

## 2. 实际 pull 与旧工作复用

公开 actual pull 完成于 19:35:53.405501 UTC，读到 ce9445471fd45aead121fa0f66bb62683e532712。随后科学仍使用上节冻结 source。根 README blob 为 21bd547f56590b7f2dd279d0297efb289a9b2783，topic README blob 为 d0432faff569c8e9af7ed4809847e12880976c11；两份差异均空。

私有规则 actual pull 完成于 19:35:55.990199 UTC，读到 2af11d3b276dac878c1fb643cc432eaf12888198。规则未变，本会话 QUEUE 唯一且 ongoing；不公开私有内容。

输入来自已经完成的 run 43744903357 / job 132905938795 / source 5fa2424a6316b1daa8453864ce223b128a43d72f 的最终原生 m7 检查点。旧原日志为 3,194,767 B，SHA256 14cafc198a1df4e7de2882994b37b9dffcf4284daacc49c670a9f65240926c3d；其 COMPLETE JSON+LF 为 829,044 B，SHA256 664b1bc5ddf7d278d61a78a36c712395f850109bfb967f5fe1df6a769b224b07。

本次旧优化器调用为 0，旧历史 m10 trial 重播为 0，旧十项、七项与缓存正负例的新执行均为 0。原十项开发通过件及原 m10 缓存证据仅按已发源/hash读取复用；117 冻结源码一致。24 份原输入与两个已完成日志只是必要的只读恢复输入，没有重新生成旧数学或求解旧轨迹。

输入点原物理 SHA：

981e092c54a5a7059bc75ffaea2f2c8bfa47c0b4c2f5932a67bd3fc74cee5376

初始同点普通值与源记录相比：coarse eta 差 2.7755575615628914e-16，fine eta 差 0；两网曲率差均为 0。该浮点差异如实保留，不宣逐位几何值一致。

## 3. 四组新接口实际通过；不以人工替代科学触发

EXPANDED_HOLD_DEVELOPMENT 的 passed 与 all_passed 均为 true，共 4 组、26 个布尔检查：

| 新组 | 检查数 | 实际结果与范围 |
| --- | ---: | --- |
| covered_expanded_context_and_radius | 6 | 同 x/y 完整 selected 域、两新 soft IDs、两 factory 后最终 binding、旧 hold 保 false、新独立保 B 判断及原学习记录均通过 |
| new_policy_rejects_incomplete_evidence | 9 | 错配置/签名/布局、缺 live context、新硬 ID、过大校正、无效完整预测分母等均回原 controller |
| exact_checkpoint_bank_and_first_model | 8 | 精确 11 条有序 normal、真实首模型 binding、拒绝伪 9 条/重复/改序/改 hash，不重算 normal、不携旧数值 cuts |
| ordinary_fallback_and_public_entry | 3 | 普通模型完整旧返回不变、已付缓存函数原样 import、公开 recovery 参数名不变 |

开发输出 geometry_calls=0、optimizer_calls=0、scientific_inputs=0、old_developer_suite_executions=0。其正向人工覆盖只证明新接口能表达这条分支；本次科学轨迹没有接受的 expanded SOC，不能把人工 qualified 当作真实 qualified。

## 4. 七个模型与全部八个 trial

所有模型沿用原共享 12 LP / 40 ordinary-value / 120 active-second 上限。表中 eta 与曲率是最终接受 trial 的细网值，也是该点双网最大值；B 是当前 body 半径。新增行保留实际学习计数，没有因不影响本次接受而删除。

| 模型 | 当前 B | 主 inner LP 数（共享序号） | 接受 alpha | 接受后 eta | 接受后 fine 曲率 | 新 coarse/fine 行 | 接受比值 | 下一 B |
| --- | ---: | --- | --- | ---: | ---: | --- | ---: | ---: |
| 1 | 0.000125 | 1（1） | 1 | 0.26634407380803315 | 57.999995032728485 | 0 / 0 | 0.9021840860435366 | 0.000125 |
| 2 | 0.000125 | 2（2–3） | 1 | 0.266340472270558 | 57.99998603281487 | 1 / 5 | 0.9678890381654421 | 0.000125 |
| 3 | 0.000125 | 1（4） | 1 | 0.26633745929632235 | 57.999988223720266 | 0 / 1 | 0.8659542981786444 | 0.000125 |
| 4 | 0.000125 | 1（5） | 1 | 0.2663337143475639 | 57.99999592610618 | 0 / 1 | 0.9621224019718447 | 0.000125 |
| 5 | 0.000125 | 3（6–8） | 1 | 0.26633035224621 | 57.99998591671167 | 0 / 0 | 0.9408361222713836 | 0.000125 |
| 6 | 0.000125 | 3（9–11） | 1 | 0.26632731019063527 | 57.99998709337268 | 0 / 0 | 0.8606253007899055 | 0.00025 |
| 7 | 0.00025 | 1（12） | 1/2 | 0.26632415509189855 | 57.999989993517644 | 0 / 0（两个 trial 均为 0） | 0.8708455831940738 | 0.000125 |

模型 1 的原 growth 条件合格但只积累一次 streak；模型 2–4 因实际新行清掉 growth streak。模型 5、6 连续满足原 growth 条件，所以 **旧 growth 规则**在模型 6 后把 B 从 0.000125 提至 0.00025，模型 7 确实使用了这个增大的 B。这不是本次新增 expanded-SOC 保 B 规则的触发。

模型 7 的全步先给：

- coarse eta 0.2663216645541745，fine eta 0.26632196212813597；
- coarse 曲率 57.99998205270985，通过；
- fine 曲率 **58.00000238313349**，超过原 58 加直接门容差，直接曲率门与 scaled-PSD 门失败；
- 两网 new rows=0，omitted hard rows=0；
- 完整实际/预测比值 0.8433004092667811，metric 下降本身足够。

该 full trial 因真实 fine 曲率失败而拒绝。第 12 个共享 LP 已用于这次 primary，剩余 LP 为 0，故没有启动 correction LP。原无新增 LP 的半步回退 alpha=1/2 随后通过两网门，形成表中第七个接受点。最终原 controller 把 B 降回 0.000125，success streak=0。

模型 1–6 返回的完整仿射模型 gap 标记为满足；模型 7 因共享 LP 用尽返回准确评过的 repaired incumbent，returned_inexact_cut_model=true、returned_epigraph_gap_met=false。其 gap=9.309170504795058e-7，而 gap_tolerance=7.927279593450409e-7。该数值模型标签没有被改写为严格凸最优，也没有代替实际两网验收。

## 5. 新策略观察结论

真实输出明确为：

- expanded_pool_rebound_records：0；
- correction LP 调用：0；
- accepted_expanded_SOC_count：0；
- qualified_retention_count：0；
- retained_B_used_by_following_model_count：0；
- new_policy_decision_records：空；
- status：no-accepted-expanded-SOC-new-policy-not-observed。

前六个模型没有失败的 primary，模型 7 虽有 fine 曲率失败，却没有扩池且没有剩余 LP。故本次没有走同 failed-y 的 expanded rebound 路径，更未到新增 small-correction 保 B 的决策点。旧 hold 报告、原学习记录、原 growth 与回退事实均保持原样。

这是一份“新 policy 的首次完整运行但分支未触发”的实际记录。不能把 status success 解读为新规则已经产生科学收益，也不以再次启动同一阶段等待触发。

## 6. 终端状态、池、bank 与真实门

终态原物理 SHA：

1275ae1da1bdf0779ff143e90b7177613b8011aa56a1781e3c31363ba1996be7

坐标定义 SHA 保持 b37cadb78c9b9e70a6359bbf81d3debbd4089104ce5758105739c9278752a580；完整 metric SHA 保持 fd5bc5fe2c114bdbe82c266a5e816ba22ed58f1f486f5bc3241ddaac95de88b6；b0 SHA 保持 d61fb298989834c9eb2b4fe3bbff1fb5983d1bb3b3980cb6441f14e6c0299bb5。

输入完整池为 coarse 4418、fine 4188。原初始化在不删输入 ID、不改固定容量的条件下使首模型池为 4418 / 4270；随后真实 trial 学习再增加 coarse 1、fine 7，终态为：

| 项 | count / version | SHA256 |
| --- | --- | --- |
| coarse 原池 | 4419 / 2 | ffc553680147ab6b5faffd5e984e7e204941169ab6f67f70f3441bd40d271461 |
| fine 原池 | 4277 / 5 | c1c7bea517e9c8a7f4ce3ba7a68fceea42017733ee9dba97daa319345e2054d1 |
| 输入 ordered normal bank | 11 | d5b1b9d6128f05e0003baa1c22b109d0d9d4fb6598bfa0ba93f0ec969c127cb8 |
| 终端 ordered normal bank | 22 | c952c53a45396f3cdfef89853eb856ffa26f45089703a884e63c1a57956d97f9 |

输入 11-entry bank 在首完整模型处严格匹配 context、原 grid tags、顺序及 hash；不是把它重播成旧 9-entry bank。终端 bank 的原记录是 insertions=42、evictions=0、inward binary64 adjustments=13；42 是实现记录的插入/更新事件计数，不等于 42 个不同存活条目。七个新中心均重新形成当时的 cuts，没有携带旧数值 A/b。

末点独立双网复核：

| 量或门 | coarse | fine |
| --- | ---: | ---: |
| eta | 0.26632396014848225 | 0.26632415509189855 |
| 最大绝对主曲率 | 57.999969638529414 | 57.999989993517644 |
| inner strip 绝对余量 | 4.0986327554115576e-8 | 4.098280803610521e-8 |
| 最小有限 sampled mirror radius | 0.10065344661966166 | 0.10065344662013435 |
| scaled plus-determinant 最小值 | 1.829298972753034e-7 | 6.028974062826861e-8 |
| 原物理硬门与旧 metric 预算 167/625 | 通过 | 通过 |
| 新 metric 预算 13/50 | 未通过 | 未通过 |

signed height、ball、inner/outer strip、regularity、mirror polynomial、直接 mirror、curvature lambda、scaled PSD 与直接 curvature 各项均通过。针对 13/50 的 fixed metric / direct eta / divided metric 标记为 false，不能把它们混入“全门均真”。

原 163 物理盒无 clipping，exact box violation=0；exact-null 高度总积分变化准确为 0，物理 c4/c5 不变。浮点 cap 报告的 affine margin=-2.7755575615628914e-17、重构 margin=-5.551115123125783e-17，均按原 height_tolerance=1e-9 处理；“两高度余量在当前算术非负”的字段实际为 false。不得据此宣浮点正余量或新的连续积分证书。

终端 B=0.000125，tail radius=0.000015625，height radius=0.0005，success streak=0。完整 reference163、exact159/physical163、全部有序池、bank context/22 entries、controller 均在 future_direct_checkpoint 的 runner 输出中，未提交这些可重算 payload。

## 7. 费用与计数：共享 LP 先耗尽

| 费用或调用 | 实际值 |
| --- | ---: |
| 新阶段调用 | 1 |
| 旧优化器、旧 trial 重播 | 0 |
| 新 primary inner LP | 12 |
| 新 correction LP | 0 |
| 新 nonlinear minimize | 0 |
| 主模型 / 实际 trial / 新接受点 | 7 / 8 / 7 |
| 共享普通完整值调用 | 18 |
| 独立末态两网调用 | 2 |
| 本 driver 总计完整值 | 20 |
| 12 次 LP 报告时长之和 | 6.468290453000009 s |
| 新 active optimization | 54.926908440999966 s |
| 必要只读输入 prepare | 17.821281669 s |
| run_audit elapsed | 282.518657269 s |
| process total | 300.339942435 s |
| Linux peak RSS | 2,391,564 KiB |

18 个共享值是初始化两网加八个 trial 的两网；末态另 2 个。停止来自 12 次共享 LP 上限，没有耗满 40 次值或 120 active-second 上限。

计时原字段另外保留：initial ordinary audit before recovery=188.545110542 s；recovery wall including pre-active first J=92.01769030100002 s；初始化累计计时=225.378535801 s。它们作用域不同且有包含关系，不与 active 相加制造总费用，也不猜测未分解的系统等待原因。

coarse/fine selected-J 分别报告 12.89235133599999 / 37.13664597999997 s，7 / 7 次 refresh、70 / 189 个批次；其中含各自实际初始化范围，不把这两个累计数全部称作 active 之外或之内。新完整方向 oracle 共 20 个方向评价、40 次两网扫描，directional_seconds 合计 20.29468859600007 s；补充原 row-J 36 次，合计 0.8852173710001807 s。oracle 内普通 geometry 调用、完整 159/163 参数张量均为 0。

七模型累计重建 inherited support 105 行，另加真实新支持 cuts 22 行（模型 2 为 2，模型 5 为 9+1，模型 6 为 8+2）。各模型字段 total_new_cut_rows 的总和为 127，**该字段包含重建 memory support**，不能把 127 全算作新的切平面，也不能拿这些计数证明相对另一阶段节省了多少 LP。

## 8. 公开原件的精确字节身份

以下 raw log 包含 GitHub timestamp、原 BOM 与换行。语义记录则先剥去 timestamp/tag，保留原 JSON 子串并加一个 LF；没有重新序列化 JSON。

| 原件 | bytes | SHA256 |
| --- | ---: | --- |
| 完整 job log | 3,366,573 | 5215dbbd84e122f445ad188168b8a72f7316e0cd31e4b5bfdcfb1f42f1b25b3a |
| EXPANDED_HOLD_DEVELOPMENT JSON+LF | 18,695 | 9e8342f4995ed67ccf413d15fdabd8f9a4e06201959699711994738690d5ecbf |
| EXPANDED_HOLD_COMPLETE JSON+LF | 895,932 | 834cd800038c9d93f5619f17b2c901ee2085633e4393591cd41ebf3e915aef9c |
| runner 临时 audit.json（原输出器声明） | 14,580,404 | 80db5142261eb197d91f754c7fba3dc1738d988e8113adfae94e93d1ab850522 |

七个 MODEL JSON+LF 按序为：

| model | bytes | SHA256 |
| --- | ---: | --- |
| 1 | 228,684 | b4e10cbd51485f5b808b0ae00753bf0fa1954dcf2bde3f2cffe6d87a561560b5 |
| 2 | 360,799 | ed44e017c8cd8b5dcc7944ff433b68498eab881e5eb943b8b516280a91525a27 |
| 3 | 233,930 | 88b7ff96809e2d5f76472d89fa3e95ccffb4a1b4c4f6f2d9a3d19afa7facb782 |
| 4 | 234,271 | 1ddd4608ce19c53134b80d2281818fcedc114f92c9cd81dd341409b613f09c64 |
| 5 | 512,690 | 93e15637e3b0d646d1e605cd2fd5e0167ac253d4c9f15799406b9acf0cdc9dcc |
| 6 | 514,598 | 236d08a830fcf7a8840205a2124191e92d96384b2b124fe025b622f5ec3aeb0c |
| 7 | 273,314 | d38ce2c274e826fe50c784922e5bd30a4a1bddab243dede429ecc89be443f352 |

本稿只消费这些已完成的公开结果，不保存/上传上述可重算 payload；原 source、请求、run、hash 与人读结论足以定位结果。

## 9. 后继仅推进新的可判定子问题

本次证据给出一个具体资源与非线性冲突：模型 5、6 各花三次 inner LP；模型 7 在仅剩一次共享 LP 时用了增大的 B，完整预测比值并不差，但 fine 曲率全步失败，只能无 LP 地回退半步。此事实不能归因为新保 B 规则失效，因为那条规则根本没有被调用。

可下一步研究的是**原 12 次总 LP 内的 primary-inner / correction 配额分配**：已有经全网完整仿射模型准确重估的 incumbent 时，是否应以显式、预先声明的规则保留一次 correction 机会，避免最后一次 primary refinement 用尽整个账本。其必要合同应保完整 repaired rho、原模型/池/中心 binding、原 SOC RHS、40 值/120 active-second/单 LP 时限及全部真实门。任何收益仍须在新的唯一公共运行观察，不能从本次未执行的 SOC 推断。

本稿没有更改这种分配规则，也不预定原样再延长阶段；若后继选择不同原式模型或真实自由度，应另给准确设计。当前最好的实际点已经保存，metric 距 0.26 仍远；有限双网的曲率与 mirror 检查也不授连续嵌入或 whole-surface reach。
