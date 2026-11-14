# 冻结数值批次 950f-tail-02：分段射击与角加密

状态：已计算、独立数值一致性核查推进中；不是闭曲面完成。
所有本批次计算冻结同一 K6/width .45/rCut .6/wCut .5/六谷/加权物理metric。
每旧profile分2射击段，每段32步=原profile64步；physicalDepth10，stageDepth180。
内部momentum保持mu，只有原cell出端除2^a，cutJet再乘回2^a。
新core与原只读 f6tail_compact_dn.mjs 的主要差别仅为数值节点和稳定线性预处理，
完整物理ODE、mean、holonomy、Galerkin root保留。独立代理已静态逐项核实。

|幅度|模式|物理 fullD|实际 metric operator|shoot|
|---:|---:|---:|---:|---:|
|.0001|4|3.207842004e-7|5.343738785e-10|1.10793e-11|
|.0001|8|1.307856023e-11|7.56107e-15|2.76861e-11|
|.0003|4|7.311443845e-5|1.181837873e-7|4.91325e-11|
|.0003|8|2.104157717e-7|1.086206680e-10|2.46099e-11|

M4新旧射击算法的fullD/metric在所示精度吻合，故M4→M8的下降确由角分辨率。
旧whole-cell M8即使minA≈.9608仍曾卡在shoot≈.00178；最终502秒后在
shoot=1.4162424e-4发生line-search失败，未接受，完整响应/trace已保留。
新M8条件数约13945，最初初始化由131秒降至9秒。
新core在Newton失败时也保留last state和minA/minD，用于诊断，不把失败当解。

独立重构全部180 stage的Cartesian重放已确认a=.0001的一致性：
shoot2.76861358e-11、实际metric6.79e-15、实际κ6.01814605（抽样）、
物理fullD1.30786e-11；完整Cartesian tensor2.65e-9主要受rr数值微分影响。
独审报告位于同目录 2026-11-09-950f-audit-cartesian-k6-m8-stage2-a0001.json。
这不是整个连续域、全部时间或无限尾的证书。

注意旧 normalizedFullDefect 含 drdx，会随每段x缩放改变；跨stage数比较必须
用物理fullD或恢复到原profile单位，本批表仅用物理量。

真正目标仍为prefix cut幅度约.001270458并含非零高模。后续正在对这组完整向量
做实际DN延拓，以及M12角加密。本批次不包含正在变化的输出。
