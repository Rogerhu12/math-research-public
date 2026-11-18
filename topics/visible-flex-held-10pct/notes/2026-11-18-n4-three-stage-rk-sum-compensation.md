# n4：只补偿 RK 四项和未改变三个具名残差峰

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

状态：**已完成的三个 stage 算术对照**，没有完整尾重放、DN 求解或 CP 回写。
使用[新六个超门 stage 的失败态](2026-11-18-n4-parts32-neighbor-multistage-residual.md)
`b4356eabf97014127a364ef34b7951a930f4b184d8c6f4c4db83c161b2cbbb5e`，
预先指定主峰 stage 43、次峰 stage 38，以及已过局部门的 stage 175。
不是再次运行旧的初值候选，也没有改生产 worker。

## 单一改变与完整基线

先冻结三处原输入的全部 42 个分量、原目标节点的 40 个分量、
原 cell/profile、cusp-aware RK16 分段，以及原 state 和 Jacobian
代码所用的 trig 常数公式与数值身份。两个附加 mean 状态的输入均为原值 0。
原始 fixture 保存输入、每个 RK 采样点的原几何值、网格及 trig 数组；
这些有限采样身份不充作连续 profile 证书。

通过原 `rhsWithJacobian` 返回的 derivative 逐式重走普通 RK 状态更新，
与原 `flowStateWithJacobian` 的 **3×42 个完整输出逐字节相同**，
包含两个 mean 输出。每个 derivative 与参考 state 都在下一次 engine 调用前复制，
并检查后续调用没有覆写原参考数组。

唯一对照把最终斜率组合

$$a+2b+2c+d$$

的四项普通加法替为 Neumaier 补偿加法。RK 网格、步长、中间状态表达式、
点根与其所有阈值、投影、几何、原 source 和最终
`state += h * sum / 6` 写回全部不变。
这只补偿四项和的加法，不是全流程更高精度，不控制真 ODE 误差。

## 实际有限结果

| stage | 原最大归一残差 | 补偿后最大归一残差 | 原主峰 flow 改变量 |
|---:|---:|---:|---:|
| 43 | $7.429289420154656\times10^{-9}$ | 相同 | 0 |
| 38 | $6.419545004694028\times10^{-9}$ | 相同 | 0 |
| 175 | $9.507411175182884\times10^{-10}$ | 相同 | 0 |

每个 stage 的 16 个 RK 步分别有 186、189、192 个加权斜率和发生了
binary64 数值变化，因此这是实际执行的算术变化。
最终全部 42 个输出中，发生数值变化的分量数分别为 2、2、37；
最大绝对差分别约为
$1.69407\times10^{-21}$、$3.46945\times10^{-18}$、
$4.33681\times10^{-19}$。两个高模原主峰均完全没有改变。
stage 175 的两个 mean 输出最大差约为 $1.08420\times10^{-19}$；
这些分量已纳入完整比较，没有省略。

三处原/新 `minA` 与 `minD` 的显示值相同。
两个高模原点根的最大报告相对残差约为 $1.8\times10^{-16}$；
该数是原 root 算法自己的有限报告，不是其真实代数误差界。

有限结论是：**这一个最终四项和补偿不足以改善所选的两个超门高模 stage**，
没有把它安装到实际尾 worker 的依据。没有据此排除最终 state 增量加法、
投影累和或其他算术步骤的影响，也没有得到机器精度下界。

## 来源及继续边界

执行句柄 27233 于 `2026-11-18 00:33:55 UTC` 真实 exit 0。
observer 总计 $12.050533$ 秒；仅三处对照循环约 $.522917$ 秒，
后者不包括创建原物理模型和线性 stage 图的准备时间。

运行源 `scripts/resume_n4_tail/probe_frozen_stage_rk_sum.mjs`，SHA-256：
`d6312e79aa156f116f8673e0eb76b9b02711b689091759b1c69e6e05534d5023`。
原 fixture、普通算术输出和补偿算术输出分别保存在
`n4_work/parts32-rk-sum-compare-v1/` 的三个独立 gzip 文件。
紧凑复现记录
[`raw_primaryb016_lam002_m20_parts32_rk_sum_comparison.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_parts32_rk_sum_comparison.json)
含各自哈希、全部 source 绑定、三处完整输入/输出身份和标量结果；
`record_stage_rk_sum.py` 只读取这些记录，不重跑 flow。

下一独立单项可恢复原普通四项和，仅给最终 state 的逐 RK 增量加法
加入每分量误差累积；补偿变量只属于数值加法，不增加物理未知量。
仍须保持原 profile、点根、投影、网格和中间 RK 式，并只先比较上述三处。
本条到此未执行下一对照，没有全尾或前缀接受结论。
