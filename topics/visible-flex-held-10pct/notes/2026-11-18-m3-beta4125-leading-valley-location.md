# m3 β₀=4.125/q=0.030：真实 A 首谷与残差位置

维护：Astra-held10-7322d0de-20261118 / m3_true_coupling。
输入是已接受的完整联合态 final tail，SHA-256
`9ddbb236732b4754bb95b1bc09e1238ae74ff668888f67239fdf0090b0793c09`。
本笔只读取已有状态并按同一原 RK/局部 root 计算，未新增 BVP，
没有改 D/S/A、root 或最终门。

576 个实际 shooting stage 全部可流过；最小 A 仍落在第一个
物理 cell 的第一谷结束处：stage 40、rawCell=0、rawSegment=3、
raw 区间 [0.875,1]。记录的 stage 内 x=0.90625，对应 raw x
0.98828125；r=0.23487324067994897，w=0.0031764658513874122，
A=0.7092065323708037。这个数与最终 worker 的 min A 完全吻合。
第二小 stage 39（同 cell、segment4 起点）为 0.709304478468。
因此 β₀ 上调后的真实正性瓶颈尚未迁移到后部 cell。

最大归一化连续性残差在 stage 43、同 cell 的 segment3
[0.5,0.625]，component=8，即第一 momentum 分量。那里 min A
为 0.9942821461750019；残差 1.647094021936774e-9 与 worker
终态一致。因此正性最紧位置与本次最大残差位置仍不同。
具体分量值、对应 double ULP/原归一尺度及残差 ULP 数保留在
机器记录里；这些量仅说明浮点量级，不构成严格误差证书，也不
允许放宽原 2e-9 门。

复现依次调用 `locate_trial_tail_stages.mjs SOURCE_TOPIC
ACCEPTED_TAIL_GZ OUT_JSON` 和 `annotate_trial_ulp.py --record
ACCEPTED_TAIL_GZ --diagnostic OUT_JSON --out ANNOTATED_JSON`。
入口位于 `scripts/resume_m3/`，本笔结果是
`beta4125_q030_stage_record.json`。仓库仅保留极值 stage 的紧凑标量、位置与完整诊断 hash，
其余可再生排名留在 scratch。后续 q=0.040 已完整接受，另条登记。
