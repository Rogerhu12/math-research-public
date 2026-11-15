# 完整模型覆盖的普通步扩径：实现与执行边界

日期：2026-11-15。接[已发布设计](complete-model-covered-soft-ordinary-growth-design-20261115.md)。仅源码审查；新增检查与科学计算尚未执行，均只在本公开仓库 Actions 运行。

## 已接的三个新源

| 文件 | 字节 | SHA256 |
|---|---:|---|
| scripts/frame_metric_covered_soft_growth.py | 38024 | 1e0dd68fd4cd1ab4c2e07aa91f90018d7fbe1c4af4f3afae29e50ffd6125a0fb |
| scripts/frame_metric_covered_soft_growth_recovery.py | 47755 | f51613f5fa28a2cdea2747952cf5dcb9f8e327fd778df649bded19f6473aa3df |
| scripts/frame_metric_covered_soft_growth_development.py | 32318 | a9e8772e620b70dd7a94beee139006bea13d6956ec9d7361921fafdb07caa665 |

原130个已付脚本均不修改。新 core 直接继承已付接口；恢复外层从当前 SOC-pair 源派生，原 primary/SOC/学习/接纳/回退分支保留。新增的模型字段只绑定实际接受中心的双网最大值、两次 factory 之后的完整对象和原数据，并报告两个独立 streak 及实际后继使用。

## 只读覆盖证据与原算法边界

上下文在 selected 与 complete 两次真实 factory 之后记录，保原 primary/selected/complete/oracle 引用、原接受中心、真实双网 eta、最终模型绑定、数组指纹、原有序 ID 和版本、配置及参考坐标。

末模型只读取实际舍入步 $d=y-x$ 已成功完成的完整 oracle cache。原 nominal proposal 只用于证明它确实经原 apply 产生接受的 $y$；完整预测、四个 maxima 和比率始终来自实际 $d$。cache、scan、quality 的方向和最终绑定必须一致；缺失时返回旧控制器结果，不补算 J/JVP、几何、值或 LP。

原 ID 在转成 int64 前先确认真实整数 dtype，拒绝 float、bool 与溢出；所有旧 ID 及相对顺序保留，实际差集与原学习计数一致，新增只能是原 finite grid 的0/1 soft组。全部原 hard、精确盒、曲率、旧metric及原首个全步/高比率/实际用径条件仍须通过。原 repaired inexact 返回不因为 epigraph gap 尚未达标而另加新拒绝门。

原控制器每模型只调用一次。旧 legacy 从已付检查点的1继续，新 covered 从0开始。任一旧或新成功 pair（含 at-cap）消费后清两个计数；新 pair 只在旧结果仍等于本模型半径时用原二倍及原 cap。原学习报告中的 false no-new-rows 不改写。实际后继 factory 与已启动 LP 分开报告；最后只提议增长而没有后继，不能记作已使用。

## 首次新开发检查：四组、20条

| 新组 | 断言数 | 新风险 |
|---|---:|---|
| complete_coverage_and_final_binding | 5 | 完整两网/零或一网新增、最终签名、整数ID、真实差集、缺cache/scan/绑定失效 |
| two_streaks_and_frozen_fallbacks | 7 | 两次普通成功、旧pair优先、旧/新at-cap消费、比率/收缩/SOC回退、原报告不改 |
| actual_step_repaired_return_and_identity | 4 | 实际舍入步、原inexact接受、原rho不冒完整预测、物理/中心/cfg绑定 |
| fifty_nine_checkpoint_and_explicit_entry | 4 | 直接59项构造及首次绑定、禁旧22项入口、原接口直接复用、后继factory/LP分别记账 |

这些是新的小数组接口检查，不使用真实 surface 或旧科学检查点，不运行旧开发套件。第4组仅以小数组替代父构造/factory的几何部分，真实新59入口与已付 bank 绑定仍走实际方法；不把人工标志冒作物理或 LP 成功。

## 下一唯一执行接口

两新 transfer/audit driver 正在接线，随后发布独立工作流与单独 request。只读取当前完成 run43758666042/job132948276657/source aca67097b60b7eacdcf20798395ce6d4d1ab2845 的原日志一次；原4组19条、此前26条与cache证据传递复用，不执行旧检查。

唯一科学入口保持 exact159/reference163/physical163、原 $g,b_0$、59项有序 bank、4432/4358原有序池、$B=1/8000$、legacy1/new0。新阶段仍为原12 LP/40完整值/120 active秒/10秒每LP；原 SOC 配额与原完整门不变。全部140项绑定预计由135脚本和5工作流组成。

工作流将在科学前实际 pull --rebase 公私规则，读取每次README差异，并保私有 QUEUE 为本会话进行中。新检查通过以后仅一次当前最好点延续。无论新扩径是否触发，都消费原实际结果再决定下一科学问题，不为等触发重播同阶段。

暂时只表示源码已接与待执行范围，不表示新检查通过、数值改进或连续几何完成。
