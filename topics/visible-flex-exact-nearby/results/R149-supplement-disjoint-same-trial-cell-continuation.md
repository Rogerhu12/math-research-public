# R149 TCX：同一完整 trial 的互斥 cell 续算与全源合并

**已证明。** 会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

本条只改变原 TC 剩余 exact certificate cells 的调度。原
[separated-grid trial](../notes/2026-11-27-TC-proposal-grid-separation.md)
及 [whole-prefix continuation](R149-supplement-same-trial-prefix-continuation-after-input-restoration.md)
的数学对象保持不变。一次恢复全部原输入和四个完整 endpoint arrays
后，最多三个同一 runner 内的 arithmetic children 共享只读载体；
每个 cell 的96列、完整来源分量和真正 radial integration 仍全部计算。

## TCX1. 完整 cell 目标与已经证明的旧 prefix

固定原实际完整 certificate plan $C_0,\ldots,C_{N-1}$，保留全部原
exact cuts、同一 selected $Q_\delta$、true-root Hermite length、两侧
相同 root value、原 cutoff，以及全部 ordinary/jump/mean 约定。
所有 input SHA、原8个 mathematical source SHA 和四个完整 private
trial-array SHA 必须先匹配。改变 owner 的调度源码不重新选择数学对象。

令 $j=1,\ldots,96$，来源标签为

\[
 \mathscr S=\{\mathrm{positive\_low},
 \mathrm{positive\_high\_collar},\mathrm{positive\_high\_body},
 \mathrm{negative\_root},\mathrm{negative\_strict}\}.
 \tag{TCX.1}
\]

对每个 $i,s,j$，原完整 residual/integration formula 给非负上界
$F_{i,s,j}$，覆盖 $C_i$ 上该来源的整个 squared norm integral。
标签不作用于该 cell 时，对应贡献是结构性零。原两个 residual
components、full angular support、全部96列和原 source windows 均不变。
没有将完整 pair 分拆为未付相关项的单个来源，也没有改成 sampled norm。

设真实已结束的前驱有完整 saved prefix $[0,k)$，其正式精确
binary64 hexadecimal upper 为 $A_{s,j}$。其含义是

\[
 0\le\sum_{i<k}F^{\rm true}_{i,s,j}\le A_{s,j}.
 \tag{TCX.2}
\]

前驱整个 actual、execution、manifest 和所有自然结论先准入；仅有
进度数字、正在运行时的 snapshot 或一个输出文件片段不能启动续算。
已经完成的 signed matrix、waist96、negative/positive conclusions
按原完整 bytes 继承，原 producer manifest 保持原值。

## TCX2. 至多三个固定互斥区域

在 $k<N$ 时，首次 parallel continuation 将 $[k,N)$ 按 exact integer indices 分成
至多三个非空连续区间

\[
 [a_1,b_1),\ldots,[a_p,b_p),\qquad
 a_1=k,\ b_\ell=a_{\ell+1},\ b_p=N,\quad 1\le p\le3.
 \tag{TCX.3}
\]

若 $k=N$ 而原 formal source conclusion 尚未写完，则 partition 为空，
不启动任何 arithmetic child；只从已经完整的原 upper 生成尚缺结论。
下面的空和均为零，此时 $K=N$、$P=U=A$。

这只分配积分工作，不限制 trial 的定义域。每个 child 读相同的
whole arrays、background、offsets、intrinsic rows 和 Hermite polynomials；
不会在分片端点增加边界条件、将解置零或形成新 jump。
完整 cell evaluator 使用原源码中的相同所有算式和同一有向 backend。

第 $\ell$ 个 child 的正式状态是接受到 $u_\ell$ 的整个初段
$[a_\ell,u_\ell)$，$a_\ell\le u_\ell\le b_\ell$，以及全部
$5\times96$ 非负 squared-sum uppers $S_{\ell,s,j}$。初态为零。
一个 cell 的所有声明来源均形成后，才同时更新全部相应上界和 cursor。
正式记录通过 atomic write/readback 持久化，故

\[
 \sum_{a_\ell\le i<u_\ell}F^{\rm true}_{i,s,j}
                      \le S_{\ell,s,j}.
 \tag{TCX.4}
\]

每个记录保留原 plan/proposal/source identities、区间、cursor、全部
hex uppers 和 complete 判定。自然有向和的每个 floating upper 先转为
其精确十六进制表示；读回不能用 midpoint，也不能把十进制打印精度当误差。

child 的下一次调用只积分 $[u_\ell,b_\ell)$。此前完整接受的区间
和完整上界直接复用。中断或失败保留最后一个原子记录；尚未接受的 cell
不伪装成已成结论。重新物化原 trial 仍只发生于 parent，一次完整全 SHA
验证通过之后才 fork；children 既不再次 QR，也不重新运行旧矩阵目标。

## TCX3. 两个用途不同的合并，均不减 upper

所有已接受的区域互斥。因此完整当前 union 的 upper 为

\[
 U_{s,j}=\operatorname{up}
       \left(A_{s,j}+\sum_{\ell=1}^{p}S_{\ell,s,j}\right).
 \tag{TCX.5}
\]

每次合并都从同一完整 seed $A$ 和当前各 $S_\ell$ 重新作有向非负和。
不能把上一次已合并的 $U$ 再加一次 $S_\ell$；也不能用两个 upper
相减来剥离已完成部分。parent 先读回完整 child records，再合并全部
来源和全部96列，没有仅合并一个最小或最大列。

另一个需要保持的对象是原接口的连续 prefix。取首个尚未完成的分片
$q$；则当前连续覆盖端点为 $K=u_q$，其 upper 是

\[
 P_{s,j}=\operatorname{up}
          \left(A_{s,j}+\sum_{\ell\le q}S_{\ell,s,j}\right).
 \tag{TCX.6}
\]

若所有分片完成，则 $K=N$，$P=U$。首个未完成分片之后的独立接受
区域只在 TCX.5 的 union 中，不能冒充 TCX.6 的连续 prefix。
原 `complete-radial-integration-prefix.json` 始终只表达 TCX.6。
其整个 receipt 和完整 disjoint ledger 一起存在同一 stable checkpoint；
worker 不发布两者更新中间的混合状态。

若后续 job 开始时仍有缺口，完整 seed 和固定 partition 一并保留；
各分片仅从自己的原 accepted cursor 继续。不能把刚得到的连续 prefix
当作新 seed 后再加旧分片总和。parent 比较原 trial、plan 和来源身份，
并以原 seed 验证完整 ledger 的所有整数和 hex records 后才开始新工作。

## TCX4. 何时可以生成完整 negative/positive 结论

原 plan 按同一径向顺序排列。设 $i_-$ 是最后一个 negative cell。
只有连续端点 $K>i_-$ 时，完整 negative 来源才全部接受；此时
TCX.5 的 negative components 与全负区积分同域，后来 positive cells
对这两个标签为结构性零。于是可立即按原公式取平方根并发表全部
96列的两个 negative source records，同时逐字继承原 waist96 和两 means。

完整 positive source conclusion 仍要求 $K=N$，即全部分片完成。
只有此时，原三个 positive windows 的每列 squared sum 都覆盖其
整个声明区域；再使用原有向 square root 得到原 full source norm。
全96列、五种来源、两边和所有原 boundary/jump exact-zero 身份均保留。

将每个 nonnegative cell sum regroup 为 TCX.5--6 可能增加少量有向
roundoff，但不改变被包围的同一原积分。所有取根仍在完整 positive sum
之后，没有从 partial scalar 倒推完整源或将 run count 充当认证。

## TCX5. 真正的执行边界

metadata generator 要求一个实际已经结束且仍缺目标的前驱，包含真正
integer return code、整个执行记录和最后完整对象；原全部目标完成时
禁止再造新的 scientific launch。运行中的 TC 不取消、不分叉重复同域。
第一次 parallel partition 由该真实终态的 seed $k$ 定义，而不是预猜
当前 job 最后会停在哪里。

每一后续 parent 在原 immutable Python/Haswell/thread schedule 下
恢复同一四个全数组并严格核 SHA，随后在 Linux fork 内共享只读 pages。
最多三个 arithmetic children 各自计算互斥剩余单元；其 cache 属于各进程，
不修改 shared mathematical carriers。deadline 只使本次 finite prefix
不完整，不能将其变成数学成功或结束整个研究任务的理由。

TCX 仍只证明有限 trial 的 signed matrices 和 complete PDE residual
source norms。真正96列的 inverse-based conversion、两 physical means、
Theta、nu/phase 和 full Schur 保持原先各自的完整前置条件。
本条没有声明当前 TC 已结束，也没有生成新 numerical 值或新 workflow。
