# n4：新主宽度原真尾的单峰初值恢复终态

维护：Astra-held10-7322d0de-20261118；2026-11-18（UTC+8）。

## 结论与范围

在已经通过完整前缀采样 metric 门的
`raw-lam002-primaryb016-m20-v2.json.gz` 对应的第一份
$0.2H$ 真尾上，声明的单峰 flow-relaxation 初值确实降低了完整射击残差，
但随后原始 nonlinear DN 仍在
$8.024431255867547\times10^{-9}$ 处线搜索失败。
原门仍为 $2\times10^{-9}$，因此本次没有接受的真尾，也没有新的联立前缀。
保存的完整终态是新的失败初值，不是成功证书。

本条独立于最初 $1.1391523014166158\times10^{-8}$ 的冷初值失败，
也不改写已发布的新主宽度前缀 metric 通过记录。
全部物理参数、20 个 cut-height 分量、M20/N512/parts16、原解析 Jacobian、
原 DN 求解和 audit 请求均保留。

## 实际执行

复用已冻结的
`scripts/resume_transfer/probe_tail_residual_initializers.mjs`。
`make_relaxation_provenance.py` 只把已保存的失败态、完全一致的
full-Jacobian 重放和原源码绑定到该入口要求的元数据；它不生成新的数学状态。
该适配记录 SHA-256 为
`e354cd51cd880bbcb6809876b92b870ab8517c7cc8fbe09d794ab85ac6e60273`。

原完整重放残差为 $1.1391523014166158\times10^{-8}$。
按预先声明的 $\alpha/\beta$ 列表和分支规则，本次实际评估 13 个局部候选，选中
$\alpha=1/8,\ \beta=0$：仅在进入原求解器之前，
把 stage 18 的 component 38（mode 76 动量）从
$-751.0491913098218$ 改为 $-751.0491913098215$，即增加 3 ULP。
局部预测与随后原完整重放都为
$1.1033592976817877\times10^{-8}$。
这次严格下降只授权调用原求解器，不替代其停止门。

| 原求解器迭代 | 完整归一化残差 |
|---|---:|
| 0 | $1.1033592976817877\times10^{-8}$ |
| 1 | $9.39372467698491\times10^{-9}$ |
| 2，线搜索失败 | $8.024431255867547\times10^{-9}$ |

保存失败态时 $\min A=0.9922920982513689$、
$\min D=0.9999779687391528$。本次尚未产生接受尾的最终完整 audit。
“初始单分量增加 3 ULP”只描述进入 Newton 之前的候选；
不能把经过原迭代后的整个保存状态也描述成仅改一个分量。

## 来源、终态和资源语义

紧凑可再生记录：
[`raw_primaryb016_lam002_m20_single_relaxation_terminal.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_single_relaxation_terminal.json)。
完整状态和候选表保留在 scratch，不进入 Git。

- 原失败态 SHA-256：
  `e8afa8dd44d14d7671ba8575bd43aed63add5e1ba55f09d19146bb3b5b91da5d`。
- 本次完整失败态 `relaxed-tail.json.gz` SHA-256：
  `886a67f6cc8932873fefb350ed533bbff1a75a4bc282adcd1481eef48515d31d`。
- 执行目录：
  `/workspace/scratch/7322d0dee069/n4_work/raw-primaryb016-lam002-actual-m20-v1`。
- owner session 76025 的 observer 于
  2026-11-17 23:19:26 UTC 记录真实 terminal；子命令返回码 0 表示
  异常被程序记录后正常退出，不表示数学接受。
- 原求解与候选脚本耗时约 718.40 秒，外层观测耗时约 730.74 秒。
  `RUSAGE_CHILDREN.ru_maxrss` 与命名空间进程采样值分别保留，
  不把它们称作整个进程树或整个主机的内存峰值，也不据此推测 OOM。

原完整尾仍未通过；精确圆弧、真正联立前缀、闭合映射及几何下界均未由本条支付。
后继恢复必须从这份新的完整失败态重新定位，保留原门，不能借用旧态的主导行。
