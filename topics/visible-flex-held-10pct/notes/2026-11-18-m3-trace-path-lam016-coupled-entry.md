# 完整有限 λ=.08 之后的唯一 λ=.16 续接

λ=.08 的实际内解、原 BC、真尾和真实接缝已完成；完整 prefix audit 为 metric=$3.329530742646296\times10^{-5}$、Darboux=$.027331801353401273$。中间 metric 短缺继续明确保留，不将其误记为最终目标已过。前两次续接内解均一层 mesh、3 次全步 Newton、域和 merit 拒绝为零，因此下一步预先选择 **λ=.16**，不增加 M、不扫描步长。

使用原 [通用 continuation runner](../scripts/resume_m3/run_m3_trace_path_continuation.py)，SHA 仍为 `4e8e4548536a0f0091910180247c1240ab49d045acbdf08a892f2809993eac57`；算法与 [λ=.08 入口](2026-11-18-m3-trace-path-lam008-coupled-entry.md) 相同。全部原 BVP、五点域、Jacobian、Newton/BC/RMS、8 次 outer、实际尾 $2\times10^{-9}$ 和完整后处理门不变。

旧实际完整 CP 为 `closed_work/m3-trace-path-lam008-resume-v1/seed.json.gz`，SHA `f4abafcac2a0e7a729a085b3462686197245d5dde60fd087e77aa8f9afd6581c`。使用其全部物理 quintic 状态回投到新参考，保留原 base profile、全部 8 参数、7 个物理控制、原 `pscale` 及 gauge/warp=.06；不再次叠加历史 `p0`，也不作 `ratio**j` 重启。

新定义核幅值由同一主矩匹配唯一给出 $q_{.16}=0.05857996100242497$。必要初猜构造的数值 core guard 为 lower=$.5076209344548709$、sample=$.5078020262086654$；有限投影参考修正最大 $4.964244657773744\times10^{-16}$、入口残差 $8.470329472543003\times10^{-22}$。前者不能界定完整未投影参考差，数值 guard 也不冒充严格连续证书。

新全部 8 项 H 逐位等于旧物理 quintic H，起始精确复用旧真实 seam 响应 `c8e5e42a6e40a8a029cb260bfac5b4a906aab71d29443dc22eb5428bafe299b1`。之后新 H 仍走原实际尾。初始 RMS 未重算，旧 mean-height 不复制；新完整图审计按本次实际 flow 积分。

119 个来源的 metadata 准备 `a66ed1` 真实 exit 0，plan SHA 为 `de97ac84ee1cee2d67040cefd2f67d9b46aae6e308594ce7e42d0856ee1cc1ca`。实际唯一 observer 为 session **49902**、启动块 `9a2486`，2026-11-18 04:25:18 UTC 已观察到 running；执行目录 `m3_work/trace-path-lam016-coupled-v1`。

[紧凑入口记录](../scripts/resume_m3/trace_path_lam016_coupled_entry.json) 给出全部必要参数、初始数组/H hash、实际命令和来源。本文件只登记这一步的定义及真实启动；内解、真尾和完整 metric 的最终结果另记，不以入口或进程状态预认成功。
