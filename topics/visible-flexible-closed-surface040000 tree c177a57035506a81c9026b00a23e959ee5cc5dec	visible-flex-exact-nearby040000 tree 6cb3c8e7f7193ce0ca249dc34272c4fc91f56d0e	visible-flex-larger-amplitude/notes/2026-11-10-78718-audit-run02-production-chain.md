# run02 条件生产链的独立接线复核

2026-11-10；Astra-visible-flex-78718bd0 / independent_audit。

**结论：所读版本与已审最终独跑协议及真 M14/W14 入口之间，没有发现实质身份链差异。**
这是静态接线复核，尚未接收成功候选，未执行 solver、导出、转包、连续后端或网格。
它不把首次 DN、原种子或活动进程计作成功候选，也不支付最终独立重跑。

所读对象为 `notes/2026-11-10-78718-numerical-post-csc-chain.md`，13690 字节，
SHA256 `769c1ecf2a3432216d34bd0bb382224253404f5f0e5affd60c082c6f380f7471`。
若该工作清单以后更新，本记录仅绑定以上版本。

全文阅读全部七节，与此前全文读过的
`2026-11-09-db6f-audit-final-independent-pipeline.md` 及本轮重新全文阅读的
`2026-11-09-db6f-root-final-m14-w14-entry-and-export.md` 逐阶段比较。
另回看 exporter、exact-bridge、common-cut、whole 的相关参数解析和实际输出名，
并全文阅读新增纯资源包装 `scripts/78718-run-file-cap.py`。
本次没有声称重新全文审查全部四十份已冻结旧源码；其前次实际 SHA 核对
记录仍在 `2026-11-10-78718-audit-final-replay-readiness.md`。

## 1. 入口和有限表示身份

必须先有 run02 自己的自然退出、真实观察及冻结 direct-CSC final auditor 通过，
再从该次 CP 的 `tail_seam.tail_record` 解析自己的最后真实尾响应。
完整 prefix CP 不是 tail exporter 的首位置参数，也不能用本次首 DN 替代末包。
当前仓库用于生产导出、重建旧绝对路径用于原求解，这种来源区分已明写，不能倒记。

尾导出 depth8、steps32、flow-steps32、N512、degree192、critical/0、
base64、ratio .05、endpoint .025、差分 .00005、诊断128及三个分数，
逐项与原 M14 初档相同。它定义新的有限图，需要自己的全部证书；
局部导出积分路径改变没有被误称为原生 S64 联解。
实际 Z/3 系数模式和公共接缝必须完整，这不新增 C³ 正则性或普遍对称性完成门。

## 2. 自己的目标、公共接缝和连续证书

prefix M24、angular768、quadrature8、subdivide1 是 Cartesian 有限表示设置，
没有被混同为 source M14 未知量数目。新基础图先产生自己的目标和基础 metric，
exact-bridge 正确消费基础 metric 报告，common-cut 使用该桥及实际新尾。
完整 signed modes 由公共图生成器扩槽，不能截回旧图模式。

公共图的 geometry、metric、moment 都实际重算。完整 baseline 已过原目标时
无需额外 angular；否则只能采用本次完整 angular 认证，不能用局部 intervals。
源目标界由 closed-budget 转移一次，不能重复转移；common-cut metric 不消费
共享 parser 的 angular/radial 旗标，这点已正确记载。

固定 M8 背景的 tight/lowmetric 两包只提供冻结背景值界，必须经真实
`--new-manifest` 转到新网格；首 DN 参数预检不能代替正式转包。
新尾 full、必要的 metric-only、collar 和全部跨的覆盖，均属于本次新图。
full 中阈值 8.5 是算法分流参数，没有冒充新图已证曲率。

若 full 本身已达到原 metric 目标，可以省去 metric-only。
**该分支实际执行 whole 时同时省略 `--tail-metric-certificate`**，
不能照粘示例而指向一个未产生的 tail-metric.json。
whole 源码明确将此选项定义为可选，原最终协议也已有这条分支说明。
这属于执行时选对既有分支，不是新的数学验收条件。

## 3. 原终门与同图交付

whole 的 1e-6 普通门不等于原 2e-9 终门；正常 terminal 必须以本次 whole
及本次 prefix target 运行，并使用旧 M12 真点下界证明实际下降。
采用 M8 背景转包不会消除 terminal 对其固定 M12 参考数据的真实哈希读取。
目前尚未在本审查中取回或重哈希那 24 个 M12 raw，也没有运行 terminal。

三个新网格须来自本次 closed-map/whole，经 plan、真实背景高度、build 和
逐件实际 audit；再读回共同面表、固定 mask 和固定顶点位模式。
同 plan 的字节对照可以补充构建复核，但不能替代原种子至 solver、有限表示、
全部连续后端及网格的独立完整执行。时间对称性仍使用既有全时证明，不从三帧外推。

## 4. 单文件资源包装的准确范围

包装只设置 `RLIMIT_FSIZE`，保留工作目录、环境和原 argv，随后 `execvpe`
同一个原命令；没有改数学源码、离散设置或浮点运算。
有效上限取请求值及已有有限软硬限制的最小值，不尝试抬高原限制。
这不能限制总磁盘、预存文件或内存，也不能保证原程序成功。
实际超限导致写入或进程失败时，部分文件不构成完整图。

本审查只读包装源码，未独立复跑其合成资源测试；原作者的两次 1KB 试验不
被记成实际大几何产物。若真单容器超限，后续启用无损分片仍须绑定实际格式、
恢复器和消费者；当前条件清单没有预先宣称该存储分支已完成。

## 5. 独跑仍待的实际对象

独立执行必须等到明确冻结的成功原始种子入口和成功候选交付。
其后使用未用过输出目录及 fresh 进程；共享已冻结输入可只读复用，不需复制全部旧数据。
每一运行只以自己真实自然退出及自己的输出回执记账，不接管或复用 root 的活动会话。
若独跑产生不同有限系数，就对独跑自己的图重新认证，不能拷贝作者系数来制造相同哈希。

本审者一直未参与主数值候选的构造、初值选择或调参，仍具最终全链独跑资格。
