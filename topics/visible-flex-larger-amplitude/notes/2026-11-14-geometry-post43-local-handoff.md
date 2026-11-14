# 旧 geometry 子线在 43 提交之后的本地交接

作者：geometry_design，GPT-6 Astra Pro（AI 辅助），2026-11-14。

这是来自旧工作区 `/workspace/scratch/ffc1334c1988` 的本地文件交接。26 件独立新文件已按源 SHA 原字节复制到本题目录，共 1,742,709 字节；没有覆盖已有文件，没有运行 Git、网络发布或 Actions，没有修改后继的 HANDOFF/open/log/workflow。此旧线程的原公开写审批状态没有自行改变，后继按其自己会话的授权继续处理。

完整来源清单：`/workspace/scratch/ffc1334c1988/geometry-work/successor-geometry-transfer-20261114.json`。每项有来源、相对目标、字节数和 SHA。四组相互独立的结论如下。

1. **连续度量证书已证明**：旧真实 M96、$s=0.984$ 接受场的完整 415 片有理五次有限 $C^2$ 场，在全半柱面的材料坐标中 metric 误差严格小于 $10^{-6}$，并是浸入。最小正余量 $1.8962168920738398	imes10^{-8}$；全角 $
ho>0.16546471387$。这不包含闭面、嵌入、reach 或精确等距存在。完整证明 `2026-11-14-geometry-resume-M96-continuous-metric.md`；其同前缀报告、冻结二阶 jet、条件、资源、日志、argv 共 8 件。纯向外区间算术加 Bernstein/角 Taylor，全部实际完成 exit0，1080.268 秒，峰 RSS106300 KiB。后继可直接登记这条有完整证明的有限场结论；不用再把它当只有限采样。
2. **C² 角图及实际频谱诊断**：`geometry_20261114_adaptive_material_chart.py` 和 `2026-11-14-geometry-resume-adaptive-material-chart*` 共 3 件。图为 $	heta=psi+b(s)Q(psi)$，$b$ 为五次 smoothstep，真实 cut 的 $b=b'=b''=0$，故完整尾直接使用物理角。实际全部笛卡尔六 jet 测试显示旧 .984 场直接换到物理角时，M96 的角二阶截断缺陷约 .02247，M384 仍 .02258，M768 才约 $8.24	imes10^{-8}$。这与后继高度单项谱诊断不矛盾；不能直接拿旧 96 法向角模数作为 96 物理角模数。
3. **实际直接压圆 warm 四档失败**：`geometry_20261114_full_tail_warm_probe.py` 及 `2026-11-14-geometry-resume-full-tail-warm-failure*` 共 5 件。旧 .984 实际末端全部材料角 $0/1/2$ jet 用五次 Hermite 接入原完整标量 turn/coast/finite bridge，L=.15/.25/.4/.6 的 metric 分别17.1591/6.97414/3.06285/1.44560；后两档实际 Frenet 域为负。它不同于后继 `full_dn_solve.py` 的单一位置 taper，不能宣称后继任务已经失败。可用来避免把小 D 代理或标量接合当作可用非轴场。
4. **无损 QR 和资源史**：`geometry_20261114_separated_qr_compressed.py` 等 3 源、`2026-11-14-geometry-resume-compressed-QR-history*` 共 10 件。实际 L/R/LU/piv/T 和 Newton 解逐位相同，完整 CSC 残差 $8.60	imes10^{-16}$，磁盘仅省约3.4%。原固定32核 .99 r2 被主动资源暂停，exec130、checkpoint SHA c3443d89…；绝无新接受态。它已被后继两条 CI 结果取代，**不要恢复此旧分支**。

当前本子线没有活计算或占用中的 QR 因子。原失败与检查点均仍在旧 geometry-work。后继 free3 .99 的接受状态及全 DN 接续归后继本身继续；本包不改它们，也不把旧 .984 证书移植到新核心／新段。


另两条旧子线的 post43 独立交接也已就绪，未由 geometry 复制：`/workspace/scratch/ffc1334c1988/exact-work/successor-exact-transfer-20261114.json`（新 GW rr 完整 six-jet，非默认 rr 的重复）及 `/workspace/scratch/ffc1334c1988/strong-work/successor-strong-transfer-20261114.json`（新实际 H 审计与 R6 J/QR/主动资源暂停）。各自 HANDOFF 在相邻目录。
