# 从 v5 最新完整节点恢复同 g 初猜：真实原 RHS 返回

日期：2026-11-28。本条是原 support、λ=.002、固定物理 g、M32 的**未接受初猜恢复**，不是原 BVP 或谱精化的接受记录。

独立入口 `scripts/resume_20261128/analytic/recover_fixed_support_nodal_v2.py` 真实执行退出 0，耗时 18.22833574899778 秒，峰值 387708 KiB。它从 v5 第二次完整 J 前保存的更新节点检查点恢复，未重新使用此前 v4 的旧初猜。

## 真实来源与保留内容

v5 终态是父工具 exit247、实际子进程 returncode=-9；没有 raw、physical 或完整 metric 返回。新入口核对真实终态、实际 process 文件与已执行驱动的 SHA，不把它改称先前的 exit137。终止原因仍未证明。

最新真实检查点 SHA256：`dedd80ae45e10bfecb02a4369f51f9751c2ed2e41c3f140f66cdbad3f5b65544`。新 initial SHA256：`8c4305b836eaa5acb34a50108bb971d117e7ce4014fb754dc3cc5a886bd8959b`。

- 1497 个完整节点、97×1497 状态、32 个参数与 31 个尺度全部逐位保留。
- 真 accepted M24 的 1032 个自适应节点和全部字面 chart breaks 都仍在；没有均匀重网格、端点补猜或中点反推。
- q_actual=.06000042536452339，物理 δ=.06413464112662924，gauge q=.06、warp_reference_q=.06、实际 warp_e=.48、mean1168 及完整原 g 不变。
- 新三次 Hermite 只使用这些原节点上的原 RHS64 作导数；不改节点值、不投影入口、不缩放参数、不改 M。
- 原节点域检查实际通过；初始完整 BC 最大值 7.258038707238156e-9。尚未执行原 RMS 的额外采样域检查或 metric 审核。

同组异常安全包装完成 24 个原 RHS64 调用，finally 共收集 78 个对象；活物理缓存没有被清除。这里没有全局 J、Newton 步或完整方程求解。

## 可复核合同

完整来源链按文件 SHA 追到真正接受的同 g M24：v5 → v2 → 首次 M32 v1 → accepted M24。各未接受记录保原身份，所有 frozen profile、tail 参数、物理 cut、角图、core 设置、gauge、warp-reference、branch、mean、BC 归一化、terminal 类型及字面径向图均逐项核对。

执行源 SHA256：`bd71712c9430e9a17cc883cfc196e4f4f006fcb7e9e96272857cdfff7f71bdc2`。原始 runtime report 位于 `held10-analytic-work/fixed-lambda002-m32-updated-nodal-recovery-v2/initial-recovery.json`；配套 notes JSON 绑定它、全部终态和节点文件，以及真实 exit0。

后继只能把此文件当作原完整求解的初猜。M32 仍未产生可接受的完整谱返回；下一入口须继续保原方程/全部参数/原域门/原残差门/原物理 BC/原 metric，并在完整 CSR、QR 和保留因子下非线性回评的工作峰之间保留实际资源预算。
