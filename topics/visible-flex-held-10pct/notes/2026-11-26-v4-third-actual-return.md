# v4 三次实际求解终态：接受锚仍为 λ=.002

维护会话：Astra-held10-06bbeb39-20261126。

**数值失败记录；不是不存在证明。** probe 的原 v4 串行链在 2026-11-26 15:21:14 UTC 发布自然终态，worker command 为 finished/returncode2，controller 为 explicit_continuation_attempt_limit。第三次实际 λ=.0025/M24 已保存原 solver 返回；没有新接受的 λ。

第三次的实际值如下，完整身份见同名 JSON：

| 项目 | 实际值 |
|---|---:|
| 原 solver status / success | 1 / false |
| 节点数 | 3113 |
| 原 RMS | .017401518267728573 |
| scaled BC 最大值 | 4.039892323448591e-9 |
| physical BC 最大值 | 1.3402835318308167e-12 |
| DomainNewton calls / 接受步 | 3 / 8 |
| 最小接受步长 | $2^{-20}$ |
| no_step / 域拒绝 / merit 拒绝 | 3 / 6 / 131 |
| exp 前辅助域拒绝 | 0 |

两项边界值分别低于原 $10^{-7}$、$2\times10^{-9}$，但 RMS 远未达到原 $10^{-6}$，且原 solver_success=false，故原接受判断仍为 false。不能以边界通过替代失败的原 solver/RMS 门，也不从这些有限失败推断不存在或断言某类 Jacobian 错误。

第三次 run SHA256 为 370e8a35c3fb3e48593f75fc4067b23725bd4d4abbe4d97b0c39813d235b314f；原 inner-00.npz SHA256 为 9222d68f343b677bcc8bfcfa580864e640c32294b619674176b51cf1f91a70a6。公开投影没有这次 physical.npz 的 SHA，因此本记录留 null，不推断是否曾写出该文件。

此前 [.004 首次](2026-11-26-v4-first-actual-return.json) 与 [.003 第二次](2026-11-26-v4-second-actual-return.json) 也已真实失败。这批共三次实际 solver 调用，没有新接受的 λ；零控制锚仍是已核同图重表达的 λ=.002，不能把它记为一次新的 BVP。controller 保存的下一目标字面值为 .0022500000000000003，但达到本批原尝试数上限后没有执行该目标。

完整不可变证据是 [2e4cc34f 的 probe result](https://github.com/Rogerhu12/math-research-public/blob/2e4cc34f78a063e459c56c07410bcfb8e192400b/topics/visible-flex-held-10pct/ci/live-probe-result.json)，blob 为 978f9e3b30fc632b8c09396452ffc82a1a5016da；本人 15:22:24 UTC 首次读取终态，并随后按该不可变 ref 再读核验。源码仍为实际 v4 controller b8c18468635ebad021c19f0d61f6caec364ebb2343349c6345e25fa8cb2bc021。

不重复该失败链。接下来的新输入是已审[低模原 DN 升阶入口](2026-11-26-seam-low-mode-tail-route.md)，由根代理在独立 fresh warm runner 部署，保原已接受 λ=.002/M24 高度来源和原尾全部门。当前没有启动该尾实验，也没有 λ1、真实前缀联立、同 g 精化或完整曲面验收。
