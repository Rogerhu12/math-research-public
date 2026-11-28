# R87 新剖面首个原完整数值场：$\lambda=0$，$M=8$

2026-11-28，/root/design_continuation。新单级温和上行剖面在
$q=\mathrm{warp}=.012$ 下，**首次原完整有限前缀 BVP 已通过全部原门**。
这是新的物理剖面，不是给旧两级剖面的接受场改标签；当前 $\lambda=0$，
仍非 README 所要求的准确圆弧终态。

| 原验收量 | 实际返回 |
|---|---:|
| Fourier 模态数 $M$ / 求解角点 | 8 / 256 |
| 自适应节点 | 415 → 580 |
| 最大原 RMS | $9.752325126135993\times10^{-7}$ |
| 原 metric L1 | $2.159654640222197\times10^{-8}$ |
| 原 physical BC | $1.454002168819062\times10^{-16}$ |
| 原 audit 角点 / 径向采样 | 512 / 1308 |
| 真正求得的 $\delta$ | .06809573111069138 |
| 原完整 BVP 与 audit 用时 | 282.96787747399503 s |
| joined child 的核计最大 RSS | 147128 KiB |

原门仍为 RMS $\le10^{-6}$、metric $\le10^{-6}$、physical BC
$\le2\times10^{-9}$、BC tol $10^{-7}$、max-nodes 6000；
原 mean 下限 $16(3M+1)=400$ 由 512 覆盖。
已逐项复核所有原 source/input SHA，以及 raw 和 physical 两个完整文件 SHA。
本条的 $\delta$ 仍位于 R87 新扩盒 $[.063,.069]$；这不把该首片证明自动扩展到
完整前缀/桥/尾。

## 新初猜和实际求解

[prepare_single_gentle_linear_seed.py](../scripts/resume_20261128/design/prepare_single_gentle_linear_seed.py)
先读取真实新线性根 profile 和来源链。它采用原 BackwardLine、原完整 25 分量
seed 公式和原入口三次 cutoff，只将 2048 角点的 seed 投影分为至多 16 个径向点
一批，以免原整网格临时数组占用。初猜含全部 415 个节点、8 个参数及7个尺度，
初始参数全零；原节点域通过，初始 physical BC 约 $2.956\times10^{-6}$，
因此**初猜本身没有通过最终门**。

此准备过程于 15:39:59.388383–15:40:01.584087 UTC 真正执行、join，exit 0，
2.194959519 s，核计峰 81820 KiB；没有组装完整 J 或运行 BVP。
它没有重做线性根的旧五点，也没有调用旧剖面的接受场作为新解。

随后 15:41:05.511163 UTC 真正启动原 BVP。
使用已核 complete CSR / streaming block QR / 全解析 $\delta$ 列 /
异常安全径向释放入口，RHS/Jac 分批16；
完整原状态、所有参数列、原域、Newton 线搜索、mesh规则、BC和audit都保留。
新增已发布的 accepted-Newton 检查点只在原 tuple 接受后保存全部 $x,Y,p$；
首次实际用它取得完整更新，不增加 RHS/J 调用，也不把中间步称为接受场。

实际进行了 5 次原自适应 Newton 调用、7 次完整 QR，
9 步接受，2 次 merit 拒绝，0 次域拒绝，最小 $\alpha=.5$。
每次原 J 前及每次接受步后的完整未接受节点状态都已存于本次独立工作目录。
最后原 solver 收敛后继续完成物理 C2 导出和全原 audit。
观察者于 15:45:49.058856 UTC 观察到终态并随后 join，exit 0。
源中的 cgroup/rlimits 观察仍没有读到 memory.* 文件，因此没有把缺失数据解释为
无限容额；本次没有资源或数学失败。

## 可复查来源

工作目录为
/workspace/scratch/7c4e33ee17de/held10-design-work/R87-single-gentle-design-20261128/lambda000_m8。

| 文件或源 | SHA-256 |
|---|---|
| 新未接受线性 seed 入口 | 671256347e9964d88e0e5bb22b5f5028287297f71678b377c0fa7066d3fb75ca |
| 初始完整 raw | f368c3ad25af89f7ed518f3d81473be08ddcec888463ae2eff4a2bffb8f3116b |
| 实际命令记录 | ee58fd2db0e57f5d64e8a5567ac1056954fa1c8c4efa2b773477e40329a0ff00 |
| 完整 run.json | 601f7af14559076463ad89fe3c925b24db20e08155274e60d7fbe5407d142aa3 |
| 原返回 inner-00.npz | 9ffcdabaf5bcad86b67911a7d1136c56aaaddf6d0ddaa216dfda13e72cab0881 |
| 原 physical.npz | d3f33bd128d8a4742d352437d876ee4e0c5f9f7c02af35461c4a7e50c6cd0462 |

[同名 actual JSON](2026-11-28-design-single-gentle-lambda000-m8-actual.json)
记录完整 argv、35 项执行绑定、原实际源/input、参数、全部接受检查、
初猜及进程来源和 QR 小摘要。数组留在 scratch，未上传仓库。

后继从这个**同新剖面真正接受的场**继续正 $\lambda$。$\lambda=1$、完整非线性
DN、同一最终 $g$ 的精化、闭合、连续全域几何和10%目标仍未由本条支付。
