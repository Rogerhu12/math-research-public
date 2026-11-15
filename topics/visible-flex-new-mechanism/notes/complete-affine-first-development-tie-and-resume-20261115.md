# 完整两网方向分离器：首人工结果、并列 incumbent 断言修正与继续执行

日期：2026-11-15；会话 Astra-new-mechanism-9974ea84。**首 run 只执行了新增人工检查，未进入任何恢复或研究阶段。** 本记录保留真实失败，不把工作流 failure 改写为整体通过。

## 1. 直接来源

- 公开 run：[43727663245](https://github.com/Rogerhu12/math-research-public/actions/runs/43727663245)。
- 实际 job：132853059448；source：45a12d31acd31733be329e38415766339031ebab。
- root 已直接读取封存 job stdout 中两条 DEVELOPMENT_PART 与最终 COMPLETE_REPORT。
- [原 metadata receipt](actions-43727663245-1-metric_height159_complete_affine/receipt.json)：54,673 bytes，SHA256 446e8134c6f91bd9b001ee677ed924cf12f87c9b6b9093abc187d861f44d800c。
- 54 个直接绑定均与 receipt 实际源码一致，51 个科学源码绑定均与原 error report 的实际 source map 一致；递归 source map 共106项。receipt 自己的全部脚本口径另保原件，不能混同54或106。
- 人工 error 输出临时文件13,163 bytes，SHA256 34576273b37fb4dc5d4b5cf6f83939bf07ba2c2c1d8de677ca9b6c19384d385b。没有将这个可重算 payload 保存到仓库、Release或artifact。

## 2. 已完成的原全网方向检查

complete-original-grid-direction 组的六个声明全部为 true。实际包含两侧各两个方向：混合 u/v/Q/五个非零 null-height 方向，以及仅五高度方向；每种都使用原粗/细完整角网格。

这组比较了所有点的 T、Ts、Xs，不仅比较最后最大点；独立参照是这个小人工原族的 full geometry Jacobian，生产方向路径没有调用该全参数张量或 ordinary geometry。当前159高度被明确保留，错误center上下文被拒，原点 de/df 行与完整小参照一致，原零步完整值及精确步缓存也通过。

| 实际检查 | 最大已观测误差 |
|---|---:|
| 混合方向的完整最大值及 attainer 方向值 | 6.661338147750939e−16 |
| 所有点的 T | 1.6306400674181987e−16 |
| 所有点的 Ts | 5.151784618836133e−16 |
| 所有点的 Xs | 6.535159080147722e−16 |
| 仅高度方向 Xs | 1.734723475976807e−18 |
| 新原点 de/df 行 | 0 |

每个当前人工粗网128点、细网256点，完整owned覆盖已核。该组用时1.9510285549999935秒；它是已消费的新人工结果，不是实际曲面或新优化改善。

## 3. 失败来自对冻结 incumbent 规则的错误测试预期

第二组 four-convex-maxima-and-frozen-inner-protocol 的十条声明有九条通过。唯一 false 是原测试要求“两次 stub LP 后 returned_epigraph_gap_met 为 true”。

真实记录如下：

- 两次 inner LP 都返回同一个实际数组步 p。
- 第一次 LP 的松弛辅助量为0；完整仿射模型实算 slack 为0.028679622641132108。原修复规则已将第一次候选的辅助量提高到该真实 slack。
- 该第一次修复后的 objective 是0.028879622641132106。
- 增加真实 attainer 的一个支撑 cut 后，第二次 LP 的辅助量就是0.028679622641132108，其 gap 为0，最后一次 inner 的 gap_met 确为 true。
- 第二次修复后的 objective 仍是0.028879622641132106，与第一次**准确相等**。
- 冻结求解器只在 objective 严格更优时替换 incumbent，所以 best_candidate_inner_index 与 returned_inner_index 都保持0。
- 因而返回候选的 returned_epigraph_gap_met=false、returned_inexact_cut_model=true 是原算法的准确记录。不能把最后一次 LP 的 gap 状态覆盖给返回的较早 incumbent。

真实预测仍是完整模型 slack，而非 LP 松弛量或原selected-only值。该人工点的旧selected slack 为0.004012194668567337；完整模型正确保留了二者差异。

已通过的其他声明包括：四max覆盖原遗漏点、attainer原ID及切换、切面接触与全局下界、原已选行cut字节复用、最后一次LP预算时的完整修复、较早完整修复incumbent通过后续cut、人工adapter限定及非法index拒绝。两个主stub调用加单剩余预算stub合计3次；没有调用实际HiGHS或研究优化。

该组用时0.01056749400000001秒。整个人工错误出口累计2.043199791999996秒。后续完整误差组、第九handoff、IO组、九段必要恢复及新科学阶段都尚未执行。

## 4. 精确修正与复用范围

修正只把该新断言改成准确检查：

1. 两次LP及共享ledger计数均正确，返回实际步仍为p；
2. 最后一次inner gap通过，两个修复objective准确相等；
3. 原较早incumbent编号0保持，返回gap/inexact标签保持其真实值；
4. 新cut确实存在。

生产 oracle、objective、冻结 inner/outer、普通值门、几何与科学参数均未因此改变。

按根规则12，已通过的完整方向组不机械重跑。后续入口复用 root 直接读取的原 public 观测，同时绑定：

- 原完整方向函数及其局部 _relative/_reject 文本片段 SHA256：8a5fbdd87ed8eb8ffabd219b6337bb186f7d7fff63e075bef6f3ffe29a36922b；
- 除本次修改的 developer 与 driver 外，104个实际递归源码的排序映射 SHA256：5616502af5dd600b0dc30d8349dd7d9e59bf2922722d58a84bed4ac66b4cd43b。

复用条目明确 executed_this_run=false。只继续失败组的修正以及从未执行的误差、handoff和IO组；全部通过以后才执行九段必要输入恢复各一次和首次新科学阶段。所有原12LP、120秒active、40普通值及2末验保持；没有延长失败预算或重跑一条已完成的科学搜索。

修正后的 developer 为26,730 bytes，SHA256 34694db773e3786b0e0d242bd31d90b846fbc0543e6361423ab74e6fa46de1f1；driver为73,907 bytes，SHA256 df2987eaed54d50d2c56efe2c44eddf15f1c8e68d9c9f132f844d8e7b02d095c。新请求仍54直接源码绑定，原98研究参数和24输入不变。

## 5. 实际 pull、规则与 QUEUE

公开预检在2026-11-15 15:03:23 UTC实际 pull/read 45a12d31acd31733be329e38415766339031ebab，两README无差。发布receipt在15:03:31—34 UTC之间另实际 pull同一main，原receipt记 no_rebase_in_progress 与 remote_main_is_ancestor_of_head 均true；该步未单独打印精确秒，不伪造它。

私有预检在15:03:27.388304 UTC实际 pull/read dece04bc03915d3124624a9c963d743681fc7021，根README blob5ba164843b1f5802184178a82d786264404873a3无差，本题README不存在；QUEUE唯一对应行仍为本会话进行中。没有发布私有内容。

本地执行环境15:03再试仍 unavailable；普通文本按根8小UTF8集成方式保存，API读取没有冒作本地pull。真正研究与人工执行始终在本公开仓库Actions。

课题仍未完成：没有新科学候选；完整度量误差、全时reach、固定握持及连续存在性均按HANDOFF/open保留。
