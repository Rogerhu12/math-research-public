# 把 ASQ18 的真实坐标误差用于原两组完整物理列

这是两个新数值接收目标的首次公开入口。输入为原 UACT21、WMA14、BFP19、DCP18 与 WBN1 的完整 manifest、actual 和 execution，共 15 件；每组全部结果、旧 current/historical receipts、事件/checkout、全部目标和零旧目标重算约定均逐项绑定。

[ASQ18](R149-supplement-actual-signed-Theta-trial-and-finite-inverse-by-primitive-residual.md) 已证明同一全 Theta 的 trial 误差小于 .26，原 finite96 误差小于 .025，真有限逆小于 2.694。这里只在原 BFP 和 DCP 公式的同一正项中替换已经支付的完整坐标误差；保留原 VQ、preimage、rounding、reference、pairing 与 DCP finite Theta 误差，不挪动任何投影。

若 t 为原 BFP 的 trial Theta norm，e 为原 whole target error，两个原公式仍为

- BFP：`(t+.26)e + VQ_error*model_preimage + model_rounding*reference_norm + pairing`；
- DCP：`finite_Theta_error + (t+.26)e`。

每个输出保自己原先的全部 96 个精确有理有符号中心。两组中心是不同的物理观测，不能互相替换；原两独立 density means 和独立 physical border 同时保留。只形成新的联合误差球，不重解任何旧正反积分、不恢复旧 native 数组、不假称完整 physical Schur 已逆。

[根纯元数据核验](../notes/2026-11-28-ASQ18-physical-receiver-root-admission.json) 已通过五组所有整件和引用一致性；根未调用两个新数值目标。首次工作流 `visible-exact-asq18-signed-physical-column-receivers.yml` 在自身首次新增事件上核源码与全部现行已读规则，再用精确 Fraction 运算两个新目标，并输出一份完整自然结论。实际成功另按真实 API 与整日志登记。
