# n4：移根 A 加最终 state carry 的单次三段对照

维护：Astra-held10-7322d0de-20261118 / n4_round_core，2026-11-18（UTC+8）。

## 结论

在原 stage 43、38、175 上，只给已经审查的 root-only A 臂加上既有 Kahan 最终 state 累加，三个最大物理归一 MP90 误差分别为 $1.580881526\times10^{-9}$、$4.777443010\times10^{-9}$、$1.691637881\times10^{-9}$。第三段保留了 carry 的主误差改善；前两段都比 A 单独更差，收益不能简单相加。

这是一项单次、完整终态的三段算术诊断。没有修改生产库，没有计算完整流 Jacobian，没有运行全尾 DN，也没有新的实际尾、prefix、连续 ODE 或闭合接受。MP90 仍是原冻结 binary64 系数和原 RK/点根阈值下的有限读数，不能当作严谨误差界。

## 唯一改动及冻结范围

执行源 `scripts/resume_n4_tail/probe_shifted_root_with_state_carry.py` 的 SHA256 为 `a6ba43427659cbef9ecdd0fcae2529088bde7820471a2dec91e0f05c2a75d839`；执行前计划 `n4_work/parts32-shifted-root-statecarry-plan-v1.json` 的 SHA256 为 `a55177ef64dcb4f02d4760d7b6ea482433af34fd3ea98bbdfccf18213a515fce`。二者在独立只读源审通过后才运行。

新类继承冻结 `ShiftedRootEngine`，把 arm 固定为 `root-only`。它不覆写点根或 RHS；只在每步最终状态累加时使用

$$
\Delta=h(a+2b+2c+d)/6,\quad
y=\Delta-c,\quad x_{\rm new}=x+y,
$$
$$c_{\rm new}=(x_{\rm new}-x)-y.$$

四项斜率和仍是普通原求和，$b,c,d$ 的中间 RK 状态仍按原 `state + h * rhs` 构造。辅助 carry 在每个 stage 的全部 42 分量上从 0 开始，不进入任何中间 RK 输入或 RHS，不在末尾加回物理 state。实数算术下 carry 恒为 0，因此恢复 A 的原实数公式；有限算术下它只记录最终累加误差，不增加物理未知量。

原 A 的独立 $\ell=L-\mathrm{target}$ 根、稳定残差 `ell + quad`、所有域门和停止阈值常数完整继承。稳定残差与原 binary64 `moments - target` 不同，这项停止算术差异已在 A 的独立结论中支付；本条不声称原浮点停止路径逐位相同。没有夹带 B 臂线性拆分，也没有夹带 Neumaier 四项和补偿。

三段初值、完整目标 H、spacing 4、M20、parts32、N512、周期独立求积 128 点、原 RK16 与原物理系数均保持。计划同时绑定原 float 字节基线、既有 MP90、既有 A 和独立 Kahan 输出；本次没有重跑这些基线。

## 对完整 MP90 输出的比较

| stage | 原流 | A 单独 | 原根加 Kahan | A 加 Kahan |
|---:|---:|---:|---:|---:|
| 43 | $3.371978088\times10^{-9}$ | $1.308286582\times10^{-9}$ | $1.993619827\times10^{-9}$ | $1.580881526\times10^{-9}$ |
| 38 | $9.592101763\times10^{-9}$ | $2.444545121\times10^{-9}$ | $4.777443010\times10^{-9}$ | $4.777443010\times10^{-9}$ |
| 175 | $1.352022000\times10^{-8}$ | $1.352022000\times10^{-8}$ | $1.691637881\times10^{-9}$ | $1.691637881\times10^{-9}$ |

表中都是完整 40 个物理分量的最大原尺度归一误差；两个 mean 分量另作完整比较。新组合的完整 42 分量最大绝对误差依次为 $8.7089286843\times10^{-13}$、$2.7073938119\times10^{-12}$、$9.8770069464\times10^{-17}$；最大 mean 误差为 $2.4705127628\times10^{-21}$、$6.6350914202\times10^{-21}$、$4.9692599572\times10^{-20}$。主误差分量仍为 mode 76、mode 76、mode 4 的动量。

新组合相对原流的三个最大误差均减小，但并不逐项优于已经完成的两个独立候选。stage 38、175 的最大误差与独立 Kahan 相同也不表示其完整输出相同；记录保留各自完整输出哈希。

## 原阈值与 carry 的完整记录

每段完成 64 次点根，前两段每次更新数为 2，第三段为 1，无 fallback。每段 16 个最终 RK 更新、每次 42 分量，共保存并复核 672 条 carry 操作记录；两 mean 包含在内。三个 stage 改变普通最终 state 更新的次数分别为 171、173、134；最大辅助 carry 分别为 $1.1146639167\times10^{-13}$、$2.1604940059\times10^{-13}$、$4.1633363423\times10^{-16}$。这些是保存的有限运算量，不是全流误差界。

对原固定 target node 的归一残差分别为 $2.4764298067\times10^{-9}$、$4.0122156279\times10^{-9}$、$1.5211857880\times10^{-8}$。它们没有用于选择精度方案；特别是第三段仍然更接近 MP90 而离固定 target 更远。本条没有以三段数据替代原 $2\times10^{-9}$ 完整 DN 停止及最终审计。

## 真实终态及来源

observer session 52719 记录真实 child exit 0，结束于 2026-11-18 01:39:32 UTC，墙钟约 8.007 秒。完整输出在 `n4_work/parts32-shifted-root-statecarry-v1`；summary SHA256 为 `6b15264d21af2ceb8b2d02241cde27a47000ad9bf32d561941f339d2e8a7d431`。原输出和生产 checkpoint 均未覆盖。

只读 collector `scripts/resume_n4_tail/record_shifted_root_with_carry.py` 核对计划与实际命令、所有冻结来源、三段完整初值、完整 42 输出、两个 mean、全部 2016 条最终 carry 递推，以及点根双残差/迭代记录；它不重新调用数学流。紧凑记录为 `scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_shifted_root_state_carry.json`。原始场、节点与完整 RK/root/carry trace 保留在 scratch，Git 只收来源、命令、标量和哈希。
