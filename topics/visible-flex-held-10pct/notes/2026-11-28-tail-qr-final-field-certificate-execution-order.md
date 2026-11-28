# 真 λ1 返回后的同场完整认证执行次序

这是现有已冻结源码的执行依赖说明，不是新的数学结论、阳性输入或调度框架。当前尚无真正 λ1/full-DN fixed anchor；所有下述路径必须从实际终态读取。

## 1. 一次真实完整尾响应，只生成一次同场定义

`run_lambda_one_actual_dn_qr.py` 先读取真实设计终态，再由 `continue_original_actual_dn_qr.py` 做原完整 native4/chord3/8outer。真正来源是后者 summary 的 `result.run`、`result.full_height_binding`、`result.full_height_packet`，不是外层 launcher 的 summary。由 `qr_actual_coupled_prefix.accepted_coupled` 完整验收最终 saved physical endpoint-H；raw endpoint 仍保留单独身份。

随后 `qr_complete_tail_geometry_chunks.py` 直接消费该真实包，不为导出重求 fullH。它原样完成 stage0、整个 native mean、全部原谱、小块其余段、全部公共两阶 jet、完整 index 与原连续证书。真实 own fixed-g 后继改用 `qr_fixed_complete_tail_geometry_chunks.py`，读取自己的 packet/runtime/native-runs；不能继续冒用 anchor 的 schema。

两种入口均可先 `--phase stage0` 再同目录 `--phase all --resume`；完整定义、stage0 及其已完成证明不重复生成。只有实际未完成部分继续。使用原逐次写入资源门，不因进度缓慢删谱、删段、改均值或降低数学门。

## 2. 同一份前缀定义表服务后续证明

对真实 QR anchor，`qr_coupled_prefix_continuous.py` 的 `tables` 只生成一次当前场的完整 exact defining jets 和角区间表；同份表供 `metric`、实际 full bundle 的 `cut`、第三活动矩和后续 finite C² 比较使用。其 source、physical、mean count/GL6、whole H 与各自证明中的哈希必须一致。

真正 own fixed 后继用 `analytic/qr_fixed_actual_prefix_continuous.py` 的独立来源门。不能把不同 q、不同 final physical-H 或不同有限图的旧角表拿来当同一份表。源参数与有限 mean 规则一经作为最终完整 g 冻结，后续精化继续保留。

完整 tail bundle 返回后，再跑 `qr_complete_tail_radius_identity.py` 与完整 cut 认证。stage0 单独成功不代替完整 bundle 验证。每个新场都要实际核其 literal cut radius 与物理 rCut；旧 c=Rc 的数值观察不继承。

## 3. 尾部 metric 只补真实未付 span

原完整逐段 certifier 同时记录 metric、曲率、全谱、共享节点和深 collar。保留这一份逐段输出，不为统一格式再跑一次。

`tail_metric_complete_supplement_v2.py` 的 `--original-certificate-dir` 可分别传实际 stage0 和其余段证书目录。其主循环原样复用同场已经通过的每个 span，只对原实际未过 metric 门的 span 付 true-w Taylor/细分；全部模和高次余项仍在。`--reuse-taylor-summary` 也只能接该真实同场、同 mean、同完整 packet 的已经付过的叶。

原内部 K<10、metric 或 deep 门若未过，仍保留其 false。上界超预算不是实际误差下界。新的全图 12.3 预算须由实际 placement 和全图程序独立支付，不能更改旧门的名字或真假。

## 4. 同源绝对位置、整闭图与全相位

`qr_tail_actual_placement.py` 读取实际 cut 的 defining zero mode、整个尾 mean、真背景 primitive/integral 与全部逐段/深 collar，付绝对支撑、半径和曲率；不能用 query 中点高度替代。

`qr_closed_map_numeric_report.py` 只给样本诊断；真正全图由 `qr_closed_map_marker_cylinder_geometry.py` 读取当前 cut、placement、完整原 certificate 和实际闭图 query，再付同一正短柱/固定帽的 C²、支撑和 reach。相位必须显式 `--phase-end 4/5`，R87 网格的 held 窗用 `--held-width 27/50`。柱长、帽和 cut 设计一旦选为最终 g，后续固定度量比较保持这些选择。

`closed_map_complete_metric.py --closed-geometry ... --finite-tail-metric ...` 最后核同一 bundle/whole mean/全部 span 库存并合并前缀、cut、尾、深 collar、柱和固定盘的 metric 门。原完整全角证明以及已实现的材料角复参数/空间旋转协变给全部相位；不需为连续 metric/reach 门把相同角证书在许多 t 上重算。README 所需 t 加密诊断仍单独执行，并不替代此连续全时范围。

## 5. 活动矩、精化与网格

只在当前完整几何真的通过后，用 `qr_cartesian_third_activity_moment_durable.py` 的同 bundle/实际 cut、`qr_tail_third_activity_flux_bound.py` 和 `qr_combine_closed_third_activity.py` 合并当前活动矩。若三阶区间未排零，保留实际结果并使用 R93 的更高阶有限证据路线，不搬旧 λ=.002 的正数。

own fixed 精化后的完整尾差使用 `qr_fixed_complete_tail_c2.py`：两个真实源、各自完整 bundle/certificate、真实切口零模及共同 g；该一对有限差不自动证明 Cauchy。上列 `qr_...` anchor 专属绝对 placement/全图 wrapper 仍有各自 source_kind，不能把 own fixed 返回传入后改标签；若选择 own fixed 场作为新的最终几何场，须用其独立来源适配或严格同图差界传递。

最后用已发布的显式相位 mesh 入口生成若干 t 的完整闭面，单文件 <5 MB。可再生网格和科学数组继续只留 scratch；真正完成还包括同一个完整 g 下径向、频率和 t 加密的真实下降记录。

本说明只连接已经发布的实际 API 和原数学责任，没有启动新数值、重算旧 q=.06 场或产生新的条件阳性。

源码依据：[真正 QR final-H 门](../scripts/resume_20261128/tail/qr_actual_coupled_prefix.py)、[原小块完整流水线](../scripts/resume_20261128/tail/qr_complete_tail_geometry_chunks.py)、[own fixed 完整入口](../scripts/resume_20261128/tail/qr_fixed_complete_tail_geometry_chunks.py)、[原 span 复用与 Taylor 补证](../scripts/resume_20261128/tail/tail_metric_complete_supplement_v2.py)、[整闭图全部 metric 汇总](../scripts/resume_20261128/tail/closed_map_complete_metric.py)、[当前 QR 全图 source/phase 门](../scripts/resume_20261128/tail/qr_closed_map_marker_cylinder_geometry.py)、[两场完整尾 C² 比较](../scripts/resume_20261128/tail/qr_fixed_complete_tail_c2.py)。各入口的真实 scope 和验收条件均以这些冻结源码为准。
