# B030：原已付违反直接拒绝旧 trial，再从 d59fa 应用真实交换

会话：`Astra-new-mechanism-8cdb3418-20261128`。消费
[cc117 自然终态](2026-11-28-r566-native-cc117-natural-terminal.md)；这是明确登记的
新求解策略，后续所有新接受仍支付全部原完整资格。本地仅解析日志、元数据和源码。

## 1. 旧 trial 的接受已经被一个原数值门否定

原 `run 45930250772 / job 140280968908` 保留 d59fa，末 trial309b8 尚未接受。
在该 trial 的 restoration `e=0` 上，已完成的真实局部峰给出

$$
\mathrm{curvature\_plus}(.7612792968749998,\pi/2)
=4.805549391305973\times10^{-6}>e+10^{-8}.
$$

这个峰属于已付费的 4465 个已闭峰，也是两份原 pending 各 1 条的来源。
原接受条件包含所有相应行都不超过 `e+1e-8` 的合取。一个实际已付违反足以
否定该候选的原数值接受条件，剩余 8635 个括号的结果不能把这个违反撤掉。
因此本策略立即拒绝该 trial，保留 d59fa，直接应用已有 pending 后进入原外循环。
不将 `eta` 小幅减少或相对旧 `g` 改善当作替代接受理由。

这并非旧 partial 续接循环原样执行：旧代码在 partial 尚未闭合时先返回，下一段
本可继续余队列以收集更多交换峰。这里选择不再为已明确拒绝的旧候选支付这部分
工作。尚未发现的峰可能改变以后工作库的扩张顺序，故不宣称与穷尽余队列的未来
迭代逐步相同。

## 2. 保留什么，哪些工作明确没有执行

必要请求完整保留原 FINAL literal、全部 4465 个已闭峰、原 8635 个未执行括号、
coarse/fine/nested 证据及旧完整成本。余队列 canonical SHA256 为
`293358a9cbe347606c181be21fc06a4f22e7d9250ec8566a54c37df6ef38773e`。
新段不构造旧 trial 的 oracle/FFT，不重算任何旧括号；`full_localization_completed`
继续为 false，8635 继续标成未执行，不算已闭或被删除。最终 checkpoint 保存
必要输入及原 FINAL 的 hash 和明确处理记录，可回到请求中的完整原队列。

原 81q、840/1682 当前径向库、1882 个物理峰轨道、380 个 working 行、两条
pending、精确 `g` 及其 origin、真实 restoration 语义的 H/pending secant 均保留。
已合格的 1672 fine 网格不自动变成当前 1682 的资格。应用 pending 后，当前库
改变所需的新值、Jacobian、FFT、native 构建及优化全部计入新科学成本。

## 3. 完成旧 outer 的真实 trust 后决策

原 outer15 的 `WORKING_ROWS_OUTER_COMPLETE` 和末 outer16 的 checkpoint
均记录累计 5 个 metric、1 个 restoration 接受，且保留 q 均为 d59fa。
因此 outer16 的实际接受数为零。outer15 literal 为 354863 字节，SHA256
`2e9c47261b0172004bdc5a390c7eaa19412fe7347c6644a6e72752325fb94b95`。

旧 outer16 没有自然 backend return，且已有两份 pending。原 trust 规则的
接受增长分支不适用，要求无 pending 的缩小分支也不适用，故应执行原最终分支：
`proposed_trust = actual_trust = .45050811767578125`。新范围明确完成这次后决策，
不假定发生了接受，不虚构缩小或增大；原 FINAL 中“当时尚未完成”的事实仍保存。

## 4. 后续完整资格与实现

后续沿原 normal 外循环从真实 d59fa 应用两份 pending。每个新接受仍要求 working
及物理盒、全部 coarse 行、fine、nested 积分、完整真实局部峰与原 margin 门；
局部工作矩阵没有删除任何已知物理必需行。restoration 仍使用原几何规则，H 的
原语义变更重置仍保留。原 20 个通用参数、2400 秒单段时钟及全部旧费用不变。

新文件是 `scripts/r566_native_d59fa_known_violation_resume_20261128.py`、
`computations/request-r566-native-d59fa-known-violation-20261128.json.gz` 和
`.github/workflows/visible-r566-native-d59fa-known-violation-20261128.yml`。
复用原 gzip stdin runner。此前未发布的“继续 8635”草稿四件移出仓库，避免
两个不同范围同时触发。本范围不宣称固定 `g` 连续族、连续 reach 或 README 完成。
