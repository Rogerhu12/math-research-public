# 投影诊断的第4个输入：完整 M14/N512 的预选端点

状态：**局部数值输入提取已完成，不是新增全尾求解或证书。** 2026-11-09，coupled_prefix。

按 tail_theory 指定，仅取完整 M14/N512 真联解的最终 `tail_0002`，stage37、raw0/segment4、profile x=0，即 raw x=.25。直接复制原 `states[38]` 的28个 shape 分量，并追加两个初始零 mean 槽。使用原冻结配置、原 weighted factory 与原 subdivision，调用一次原 `createMomentumTailEngine.root`；没有调用 RK、flow、全尾 DN 或全 stage Jacobian。

实际成功执行 exit 0。原 root 用5次 Newton 迭代，relative residual 约 $2.21681\cdot10^{-16}$，离散 minA 约 $.1179156034$、minD 约 $.9999264425$、minS 约 $.9999993723$，没有 roundoff fallback。该位置是预选对照，不称为全局最坏点；这里的角向最小值也是原 N512 离散值，不冒充连续区间证。

输出 `prefix-m14-q512-stage37-projection-input.json.gz`，SHA256 `62076b6b944cd1665fde25f3d4858322c5019af8b916e8e13ec663004781af4f`，113244 bytes。包内有完整 Q/L/state/geometry/target、原 p/pt/U 系数、原 moments/quad/B/pointwise rows、rounded cs/sn 表，以及49个输入和来源文件的 hash。全部数据只供已约定最多四点的局部比较；本轮总计与 peer 的一次控制 root 合为两次局部 root。

生成脚本是 `scripts/db6f-prefix-one-m14-root-packet.mjs`，实际 argv 绑定在输出中。其前两次 setup 曾因过严的物理参数比较而拒绝：原 DN 会把 `physical.parameters.depth` 和 `linearMethod` 等数值元数据覆盖为 stage 计数及求解表示标识。两次拒绝均发生在原 angular root 调用之前，实际 exit 1、angular root calls=0。保存了这两版 source snapshots 和 `one-m14-root-setup-rejection*.json`；最终比较器只排除原 DN return 表达式明确覆盖的数值键，并另核 M/N/depth/parts/steps/floor 与整个状态分区。没有放松任何真实几何参数匹配。

后续 `tail-local-projection-values.mjs` 读这个包的独立 adapter 已逐值重建其原点态公式与投影输出。原输入提取的独立审查由 independent_geometry 完成；本人只对未参与实现的纯浮点比较器另作审计，范围见 `prefix-review-local-projection-values.md`。

本文所有 notes 短名带 `2026-11-09-db6f-`。这次局部调用不改变当前活动 continuation、已审闭图或 README 完成状态。
