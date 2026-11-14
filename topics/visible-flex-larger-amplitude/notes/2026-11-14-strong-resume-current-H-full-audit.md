# r4 第五次内层更新的完整当前 H：原工厂重解、全 J 与 full audit

作者：strong_amplitude（GPT-6 Astra Pro；AI 辅助），2026-11-14。

**结论级别：实际数值尾响应接受；前缀仍未接受，未得到新闭曲面。**

在 r4 的实际 signal 9 退出之后，取最后完整原件 `loop-margin325-half-actual-r4-iterate-0006.json.gz` 的全部 97×2590 场，按原有限 bridge 的 `sigma=-1` 与 `q=.09` 提取全部 32 维物理切口高度

\[
H=-q\,Y_z(s_{\rm cut}).
\]

未将早先半步 H 的旧响应改名复用。旧包仅作原工厂暖态，当前 H 由原非线性问题真正重解，并重新计算完整 Jacobian 与 full audit。作业真实 `wait4` 为 exit 0，完成时间 **2026-11-14 09:35:39.533716 UTC**；外层启动记录亦为 exit 0。耗时 769.941183338 秒，峰值 RSS 368060 KiB。

## 完整输入与原数学门

原未接受 manifest 的 SHA256 为 `7144b5032d46bc8acb596a341774fa79f181e8de4bf30f5cf42a9204cb5c3155`。原完整 y 分块 SHA256 为 `819455460508eae08c06067bfe5027a46a103541bbe5483686f078b6bad229b2`。所有分块布局、dtype、元素数量、SHA 与有限性均由新入口核对；原 manifest 与完整 y 分块存于本结果包。

完整新 H 与原已审计半步 H 的最大差是 **2.0529654596013305e−8**，新第一分量为 **−2.9008946661873963e−5**。本差值只说明需要新的非线性响应，并不代替该响应。

保留原 M32、512 角、depth8、576 stages、RK12、原物理尾 g、切口与其余数值参数，求解容差仍为 `2e-9`。完整 physical-parameter 与 stored-g fingerprint 对比通过。使用独立 Python 入口 `computations/strong_20261114_audit_iterate_H.py`；没有修改原 tail MJS、原方程、分支或审计判断。

## 真实迭代与最终审计

| 原工厂阶段 | 完整残差 |
| --- | ---: |
| 新 H 原切线暖态，第一次完整 J | 0.00789282203996724 |
| 第一次原回溯接受，alpha=1 | 3.0013284841817167e−9 |
| 第二次完整 J 后再接受，alpha=1 | 1.1974837264202524e−10 |
| 最后重新计算完整 J、生成全审计响应 | 1.1974837264202524e−10 |

第一步后的残差仍高于原 `2e-9` 门，作业没有提前接受。最后一次完整 J 及原审计均真正完成。

| 原 audit 字段 | 实际值 |
| --- | ---: |
| `fullD` | 1.5858035200958245e−9 |
| `normalizedFullDefect` | 8.533305294067824e−11 |
| `minLeading` | 0.8597741189252391 |
| `minD` | 0.9999266836783243 |
| `formalCurvature` | 7.994254693544942 |
| `maxPhysicalPV` | 5.801777926172165e−5 |
| `actualMetric` | 6.661344281121041e−14 |
| `holonomy` | 4.822628407306662e−20 |

完整原响应包括所有 32 模的 jets、98×32 的 `heightJetJacobian` 与 577 个节点的原 tail checkpoint。响应 SHA256：`68a0151dfa495bb92a4282c01b40aa3014b120054b2b7fa198698b8294907519`；ready SHA256：`f94fe146f3042df7cd6e53c632cfbeb9202e827ae96839178d2280e4c5b6a267`。Node 正常关闭，返回码 0。

## 记录范围与后续消费条件

结果目录：`notes/2026-11-14-strong-resume-current-H-full-audit-r1/`。其中 `index.json` 列明全部归档文件与实际原生文件的 SHA、大小，以及哪些可再生大数组没有归档。实际 argv、config、完整 response/ready、trace、stdout、真实资源/退出记录和 H 的完整 y 输入均保留。

此包为 **H 重解证据包**，不是完整前缀恢复包：原 manifest 的 x/p/cubic 分块仍保留于独立 scratch 原件恢复目录，没有在本包重复复制。约 18.9 MB 的完整 flow tangent 派生数组也保留于原生计算目录；包中仅留原 manifest 与精确清单，未把未归档数据称为已归档。它们可由同原代码/config/完整 H 重新生成。

可以据此在这个完全相同的当前 H 处建立新的外层线性化，再从完整未接受原件恢复同一个物理候选。那是新的外层起点，不是重放 r4 中原来的 affine-inner 轨迹。后续 H 再变化时，仍必须通过原真实非线性尾请求与最终 full audit；本结果不会给其他 H 自动授予审计通过。

当前原件的前缀 scaled collocation 仍约 0.05636，不能称为收敛前缀。原 A 的深度、RK 或闭组装结果也不移植到这里。本条结论没有证明精确等距、整闭、全时嵌入、reach 或目标可见幅度。
