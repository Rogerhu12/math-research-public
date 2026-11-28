# B030：从真实 430 接受点及关停前已执行的新库继续

会话 `Astra-new-mechanism-8cdb3418-20261128`。本范围承接
`2026-11-28-r566-55be-to-430-runner-shutdown-terminal.md` 的真实终态，原 run
`46127678618` / job `140925787595` 没有 FINAL；完整接受 checkpoint 与其后
实际尾事件共同定义输入。不是从 55be 或原部分定位入口重新开始。

## 已付状态与库恢复

实际保留 81 维 \(q\) 的 SHA 为
`43015466eb4f1818628178bf8f900cba2304fcd74753bab5759f214ff188dd23`，
已接受 \(\eta=0.1929414276608794\)，原几何标量保存为精确 binary64 零。
原 2810 峰中 904 已付前缀复用，新 1906 全部完成，未完成候选为零；完整
coarse、fine、nested、原工作/物理盒、局部峰、原严格改善及实际 trust 决策
已经完成。原 1810 × 3072 资格完整保留，不重新定位或重扫这一旧 fine 基线。

接受后的 5 physical、11 working pending 在 source 尾部已实际应用。新输入
以旧库和精确 pending 坐标调用**相同原合并函数**恢复 906 coarse、2025
physical，再直接载入真实 backend-start 打印的全部 631 working 行。它包括
原 601 行及实际后续选出的工作行，不用新的峰搜索重建工作集合。
新 fine 仍按原公式取旧 1810、已保留 coarse 和新增中点的并集，真实结果为
1814；旧 fine 的每个 binary64 坐标永久保留。只以实际已保存的原 1810
网标识已获资格，1814 是以后必须满足的要求网。

尾部已为同一个 430、新完整库付过 coarse 全值及选行，标量要求行数
3221196，phase 为 metric，extra 为 `0.1929414376608794`，trust 为
`0.45050811767578125`。新入口复用这些真实已付全值证据，跳过同一 coarse
选行重放；第一次实际新 J 直接用于原 native QP。

source 将完整接受 checkpoint JSON 原文、实际 backend-start JSON 原文、
native build/J/Powell/native-QP 五个尾事件与各自 SHA、字节数、UTC 一起绑定。
最后 checkpoint 中 pending 的原样记录不会删除；在新运行状态中明确标成
已被 source 执行的交换，不能让它们再次记成一笔新科学工作。

## H、原 trust 和关停尾段

最后完整 checkpoint 保存了原 82 维 H 的 3403 项 packed 数组及 23 个
pending 冻结乘子。尾部后来确实完成一个 631 × 82 J、90 blocks，并实际
更新了 H，但只打印新 H 哈希，未打印其数组或完整 J。因此新入口：

1. 保存 source 那一个完整 J、90 blocks、`56.86794274199997 s`、一个工作
   value key、`0.7267829660000302 s` 及 native build、Powell 更新和真实
   QP 观察记录。它们不在较早 checkpoint counts 中，另列额外已付尾事件。
2. 只将最后**完整保存的** H/pending 按原同语义启发式规则载入，不冒称已恢复
   尾部最新 H、J 或 native 工作区。新必要 J 的重建费用再次如实计入，并直接
   服务下一次原求解；既没有旧资格重放，也没有另开审计或科学 probe。
3. 源最后已完成的 430 接受/trust 决策保持不动。其后的新 backend 外部关停，
   没有自然 return 或 callback 结果，不能假造一次后处理 trust 缩放；续用其
   实际原 trust。

同语义 H 只决定局部原 QP 的启发式初值，phase/行函数语义改变仍由原 helper
重置 H/pending。新 source 不将旧 raw backend 点写成实际已接受点。

为修复此次真实暴露的续接状态丢失，新的 driver 在原 helper 已经观察实际
native QP 后，同步输出该真实小型 H/pending checkpoint。输出从已拥有的
数组序列化，不产生新科学点/J，不添加接受门，也不保存完整 J/native 大工作区。
原 native 算法、完整 callback、自然回退、资格、交换、费用退休、post-backend
trust 和整段正常 `for outer` AST 与已执行的 6482/55be 正常循环完全相同。

## 原接受要求和费用继续完整保留

本范围所有 20 个原物理/求解参数不变，仍至多 2400 秒、保留 30 秒收尾。
新实际候选必须满足原物理盒、工作行、完整 coarse、所要求 fine、nested
quadrature、全部当前局部峰、几何 margin 与实际 \(\eta\) 严格改善。仅提升
辅助 epigraph 不算实际改善；未表示的新违反照原规则拒绝并进入库。

最后完整 checkpoint 的 `73.869879295 s` 及完整 prior ledger 原样保留。
尾部已知串行 native build、J 及其他已打印费用另列；没有 FINAL，最终精确
elapsed 与未打印的 oracle 累计计数保持未知，不能填零或推造精确总数。
总费用下界只加互不重叠的 checkpoint elapsed、后继 native build 和后继 J，
并明确仍不含所有未打印尾段。新范围的实时费用独立累计，所有来源保存在
prior ledger 中。

历史 rejected `309b8…` 的 4465 已闭和 8635 未执行仍由绑定原 gzip 输入
保存，8635 不重做、不删除、不写成已闭。本次 430 的 2810 已闭属于另一
明确候选，不能与历史队列混算。

## 入口与发布

- driver：`scripts/r566_native_430_shutdown_resume_20261128.py`。
- request：`computations/request-r566-native-430-shutdown-resume-20261128.json.gz`。
- workflow：`visible-r566-native-430-shutdown-resume-20261128.yml`。
- lane：`rounded-core-B030-native-430-shutdown-resume`。

必要完整源状态经 stdin 传入，不写科学中间文件；原日志留在 scratch。
本地只做原已完成日志解析、源编写、AST/字节绑定和 JSON 元数据处理，没有
执行科学模块或原科学积分。该范围为原静态设计真实继续，不声称固定度量
柔性族、连续 reach 或 README 完成。
