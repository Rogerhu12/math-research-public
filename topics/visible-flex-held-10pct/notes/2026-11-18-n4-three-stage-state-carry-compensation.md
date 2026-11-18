# n4：逐 RK 增量补偿有混合效果，未形成可安装的流算法

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

状态：**三个既定 stage 的第二个独立算术对照已完成**。
仍使用失败态 `b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e`
及[四项和对照](2026-11-18-n4-three-stage-rk-sum-compensation.md)已冻结的
stage 43、38、175 输入、目标、几何、网格及 trig 常数。
没有完整尾重放、DN 求解、CP 回写或生产 worker 修改。

## 唯一变动及表示约定

恢复原普通四项斜率和，令每个 RK 步的原增量为

$$d_j=h(a_j+2b_j+2c_j+d_j^{\rm RK})/6.$$

仅在最终 state 加法中使用每分量 Kahan 变量：

$$
y_j=d_j-c_j,\qquad t_j=v_j+y_j,\qquad
c_j\leftarrow(t_j-v_j)-y_j,\qquad v_j\leftarrow t_j.
$$

每个 stage 开始时全部 42 个 $c_j$ 清零；它们在该 stage 原有 RK 步间保留。
原 RHS 和中间 RK 式仍只读舍入后的 Float64 $v$，不读 $v-c$ 或其他扩展表示。
在精确实数算术中 $c$ 始终为零，故是同一 RK 公式的加法补偿，
不是额外物理未知量。点根、投影、所有原阈值、中间 RK 更新和分段保持原式。

重新验证原普通 RK 回放与原 `flowStateWithJacobian` 的
**3×42 个输出逐字节相同**，包含两个 mean 输出。
输入 fixture 与前一对照的全部数值身份相同。
参考数组和每个 derivative 均立即复制，并检查后调用没有覆写参考 state。

## 固定输入上的实际结果

| stage | 原最大归一残差 | 补偿后最大归一残差 | 补偿后主峰 |
|---:|---:|---:|---:|
| 43 | $7.429289420154656\times10^{-9}$ | $2.0636915055985155\times10^{-9}$ | mode 76 动量 |
| 38 | $6.419545004694028\times10^{-9}$ | $5.215880316313898\times10^{-9}$ | mode 80 动量 |
| 175 | $9.507411175182884\times10^{-10}$ | $1.5211857880292614\times10^{-8}$ | mode 4 动量 |

原门仍为 $2\times10^{-9}$。stage 43 的 mode 76 残差从 $+18$ 个原记录 ULP
变为 $+5$ 个，flow 移动 $-13$ 个。stage 38 原 mode 76 的残差从 $-8$ 个
变为 $-2$ 个 ULP，但新的最大值转到 mode 80。两处最大值均仍高于原门。
stage 175 原 mode 8 分量不变，mode 4 flow 的一个 ULP
（$8.881784197001252\times10^{-16}$）变化使这个原先过门的 stage 超门。
这些 ULP 只描述当前有限数值，不是机器精度下界。

三个 stage 完整 42 输出中分别有 33、39、39 个分量改变；最大绝对差分别为
$2.9558577807620168\times10^{-12}$、
$2.7284841053187847\times10^{-12}$ 和
$8.881784197001252\times10^{-16}$。
两个 mean 输出也已纳入比较，最大差分别约为
$6.46\times10^{-27}$、$1.36\times10^{-20}$ 和 0。
最大辅助 carry 分别约为
$1.13243\times10^{-13}$、$2.18492\times10^{-13}$、$4.16334\times10^{-16}$；
它们是数值加法账目，不是解或残差的误差界。

有限结论是：**最终 state 累加算术会明显移动这些残差，但本次效果不一致**。
没有安装该变体的依据。对固定有限目标残差较小，也不能单独证明流映射更准确；
此处没有更高精度真值、有限离散误差界或连续 ODE 误差界。

## 来源和后续边界

执行句柄 60547 于 `2026-11-18 00:38:58 UTC` 真实 exit 0。
observer 总计 $12.008678$ 秒；对照循环约 $.645102$ 秒，后者不含原模型准备。
采样 namespace RSS 与 `RUSAGE_CHILDREN` 的峰值语义分开保留，均不称全主机峰值。

冻结运行源 `scripts/resume_n4_tail/probe_frozen_stage_rk_state_carry.mjs`，SHA-256：
`0f57aa60fe9b76f47ecf949d661998a0fbfff05fd6a7e5e1954f959b51f13221`。
原始文件在 `n4_work/parts32-rk-statecarry-v1/`；
[`raw_primaryb016_lam002_m20_parts32_rk_state_carry_comparison.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_rk_state_carry_comparison.json)
只收来源哈希、三处标量、全部输入/输出与 carry 身份。
`record_stage_rk_state_carry.py` 仅核已存文件，不重跑流。

下一项应先设计固定原 binary64 系数的较高精度流读数，以分清加法敏感性和实际数值误差。
不继续叠加无法单独辨认的算术 patch，不用这个对照替代完整原 DN/Jacobian/audit 接受。
