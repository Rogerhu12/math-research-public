# R133 补充：四格完整 193 方阵的实际连续证书

## 实际运行

公开 Actions [43645186441](https://github.com/Rogerhu12/math-research-public/actions/runs/43645186441) 的 matrices job 实际执行新数学，11 门全部通过，child return code 为 0。科学用时 163.68048967200002 秒；原过程的子进程用时 165.00496372499998 秒。实际新算旧索引 $0,76,3300,5969$ 的四对完整 $193\times193$ 局部多项式，所有原 target、候选、projector 和原 Green 计算均为 0 次重算。

输入是原 run 43591378059 的四份完整已证系数行摘要。本次从这些准确定义恢复原参考多项式，另选并保存新的准确 dyadic 矩阵。原全部真实生成元误差保留，新矩阵舍入费用另加。原 $Q$ 锚的 96 列没有被充作 193 列传播子；新矩阵确从 $I_{193}$ 出发。

## 完整连续门

采用 [完整方阵与方向 Green 合同](../notes/2026-11-14-R133-cached-full193-matrix-directional-Green-contract.md) 的 (M.1)–(M.9)。每个方向都保 degree 24 的全部准确 binary64 矩阵系数，并对每次递推舍入后的整个 degree 27 残差重新作有向上界。

以下数值均严格向上放宽原 Arb 上端。$\epsilon_{\rm new}$ 是原完整真实误差加新 reference 选择误差；后两列对应正向多项式 $F$，覆盖整个原闭格。

| 原格索引 | $\epsilon_{\rm new}$ | $\|\widetilde A_F-A_{\rm true}\|_\infty$ | $\|F^{-1}\|_\infty$ |
| --- | ---: | ---: | ---: |
| 0 | $1.980870537156\,10^{-8}$ | $1.980886062882\,10^{-8}$ | 1.237420934073 |
| 76 | $9.952631256090\,10^{-5}$ | $9.952631592431\,10^{-5}$ | 5.905848431654 |
| 3300 | $5.052101813071\,10^{-6}$ | $5.052101823953\,10^{-6}$ | 1.007749102690 |
| 5969 | $1.806516246646\,10^{-7}$ | $1.806516599964\,10^{-7}$ | 1.085520454916 |

反方向同样实际通过。对应整格 inverse 上界分别小于
$1.237447960083,\ 5.915817269394,\ 1.007919350858,\ 1.085528978405$；
反向生成元差分别小于
$1.980886196977\,10^{-8},\
9.952631583838\,10^{-5},\
5.052101823946\,10^{-6},\
1.806516621358\,10^{-7}$。

整格可逆性来自严格正的
$$
 e^{-hM}-h e^{hM}d_F,
$$
不是端点抽样。两个端点 inverse proposal 也分别通过左右完整矩阵 Banach 恒等式门。两方向端点乘积的完整误差均通过小于 $1/1000$ 的一致性门。

这些结果证明四个局部方阵可用，并给出了后续真实缺陷验证所需的完整误差。两个独立舍入的正反向多项式仍只是近似互逆；它们不自动成为同一个准确有理生成元的两向解。后继全局 Green 必须使用同一个 patched $F$ 及其真逆，或显式支付全部算子差和真实跳。

## 频率和均值

完整 193 槽按下列两个正交子空间保存：

- 65 槽：odd $1\ldots32$、独立 even mean、even $1\ldots32$；
- 128 槽：odd 和 even 的 $33\ldots96$。

它们恰好覆盖所有输出；mean 槽始终位于第一组。原完整 128 个 primitive 中间模、真实物理 Gram、准确正权 $\rho$ 及 $R'R^{-1}$ 均保留。记录中的四个 endpoint block 是新准确多项式的局部矩阵 block；不能把它们直接称成全区间的 source Green 常数。

## 原字节与过程

目录为
[notes/cached_full193_matrix_pilot_ci/run-43645186441-1-cached-full193-local-matrix-pilot](../notes/cached_full193_matrix_pilot_ci/run-43645186441-1-cached-full193-local-matrix-pilot)。

| 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| native/complete-four-cached-full193-matrix-polynomials.json.gz | 29,342 | 4328b19228049235aded13355585a6d9093a3621daa8d2018f84bc169437d317 |
| process.json | 6,991 | 7198cd349d5403757728ba641cbc9bf501c6bc2dc2aebafd17c81a62fd95fbdd |
| evidence/complete-cached-full193-matrix-pilot-summary.json | 20,275 | e595e2457d765e61052370032f7095643e0715f8d07fe4eeeabf8a087d912727 |
| evidence/complete-matrix-array-origin-inventory.json | 8,604 | a9314ab0b6a69a694fcb45b14d45c7466ef01ef177e8b1dff0efa47402332290 |

完整大数组只位于公开 Actions artifact
visible-exact-full193-matrix-pilot-43645186441-1，
artifact ID 14133504273，实际 61,752,830 字节，
digest 为 4a5d39286cc9aec7cd6bc8a8d1e9dd04e723e1a2178beb0d1ae8420444e6d970。
它的四个 matrices 文件保持如下原字节：

| matrices 文件 | 字节 | SHA256 |
| --- | ---: | --- |
| full193-local-matrix-00000.npz | 15,378,083 | 064fceafd9c5c03b3bb98b578e58afdb076b618b04af5d32b2f3c7a29dc59245 |
| full193-local-matrix-00076.npz | 15,388,441 | 013442412c03e893a4fba053da30ac26a6e069e0e81a3b991b8a9d291588ed79 |
| full193-local-matrix-03300.npz | 15,463,443 | 2c24c5b57a8dc201a05ed38969e3340ce721863f94a37e4a075c3e0b00d45b0a |
| full193-local-matrix-05969.npz | 15,467,589 | 2595add1aa51f2f665ea5c0884173f3a9e3626e3db9711e3cc2f9784e91e7afd |

每个文件分别保存 generator_forward_power、正反两个 full fundamental power 和两个 endpoint inverse proposal；逐数组 shape、dtype、原始字节 SHA 也在小收据中。其来源始终是上述真实 run/attempt，后继不得重算这四格或改写为新的来源。

科学 source SHA 为 c8fb7a4ea178fd7415848e36336995149fdfa8959f7cc0700a3efe48d8512b06，
worker SHA 为 dcdf2ae60435d942cc3139920214d9b071b7b54c60b79a97b6616df250dcfed9，
105-file manifest SHA 为 e15a4e56df96b96bdd8f2bd8628f6985518b140978912fa3d45aad7e6c265936。
原 97 个闭包文件 pin 无变化。

过程内 4 次真实 pull 的 README 差异均为空；after 顺序为
7d615390cf35c88dbf85159873a807df4eff5154、同一提交、
65960193d61ee81885c8e102f2189429f7014efa、
8ab16ca804845b340d537c5067ae1f679a5e8325。
人工已读规则版本仍为 ee26c0a65a2e63c15f2ccfba6714181584416542。

## 范围与接续

本条只完成四格全方阵的实际连续证书。它不宣称完整 5970 方阵覆盖、方向 source 的全径向 controllability 积分、完整双端矩阵 Green、未知高 BVP、全低高 Schur 或真正无限维 $\nu$ 响应。

后继方向计算保留完整 128 个 $33\ldots96$ source 方向及所有径向 $L^2$ 输入；不能以 128 个固定径向 load 取代该源空间。真实帽 97 行、独立 mean 和全部低高 cross-block 继续保留，最终由已有真实有限逆支付新矩阵 kernel 的全部连续残差、两端边界差和真实接口跳。
