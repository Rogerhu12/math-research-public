# R133：伴随提案的相邻浮点结点恢复

公开 run [43662395328](https://github.com/Rogerhu12/math-research-public/actions/runs/43662395328) 的新伴随提案在 QR 开始之前停止。原 outcome 的两个科学输入门已通过：全部 7908 个 whole scalar jet 域、全部 7908 个现成原生 midpoint（其中 64 个来自已完成补齐）以及原八份 range receipts 均已核。没有重算旧 target。

## 1. 实际失败和原字节

原 source SHA256 是
`5cdff6d9f51db3e99a3a89738001856182b155ae46819c6c796acdceb8480a89`，
worker 是
`f83b29bcf559820a685f3cc66686126a08ac7ed0b1e2e0fc4a45f7cf6d70d19b`，
manifest 是
`a5260c946c731d3b50c3bdb2a76fa7aec7b653ad3bec6c9eb844b8bb37be982d`。

原 child 实际 return code 为 1，wall time 15.000784156 秒；原 producer 报 13.895752974 秒、0 个新 QR blocks，尚无 case/factor。原 ValueError 为：

> a new collocation interval crosses an actual original candidate cubic join

原 native SHA256 为
`f6cdd51f5776ea66435212188cd5db2518f225c24c240823ee7f726e389757d0`。
原小摘要 1813 bytes，SHA256
`1106b191a1b8a1cad45d7279804b811033463912601b252bf14cfa761635676a`。
原已发布 process 15114 bytes，SHA256
`cfd808d4045b774a2b7b9d615c208ddff5ee70bd872d8417f71aebc3ba9f6748`。
它们在
`notes/cached_cap_adjoint_proposal_ci/run-43662395328-1-cached-cap-adjoint-proposal/`。

该原 process 的最后真实 pull 是 2026-11-15 01:18:50.875059 UTC，
提交 `a3bc3b87272f50aa5688b433d9e52fa71705ac82`；两份 README diff 都为空。
原失败记录不修改，也不把已经通过的输入门称为伴随解或完整矩阵完成。

## 2. 唯一数值选择问题

所有原 candidate knots 已逐个包含在浮点提案节点集合中。旧代码用
$\operatorname{float}(a+(b-a)/2)$ 选择所在 candidate cubic。
当 $a,b$ 是相邻浮点数时，这个中点可能舍入为右端 $b$；
若 $b$ 正好是原 knot，side=`right` 会选择下一片。因此原检查会拒绝
这一格，即使它的两端本来属于正确的左片。

v2 只改为按格的左节点 $a$ 使用原 side=`right` 选片。由于每个原 knot
仍是格节点，该选择是这一格的准确单侧片。原两端检查
$k_p\le a<b\le k_{p+1}$ 原样保留；如失败，新的诊断会保存格号与两端
及两个原 knot 的 binary64 hex，直接停止。没有放宽网格、germ、背景或
首段外推权限，也没有使用近似容差忽略不一致。

真实 $L=9/10$ 仍由首 Hermite 多项式的原授权极短延拓读取；不能直接
把 $\operatorname{float}(L)$ 的 state 当作真实内端。

## 3. 原成功选点完整复用

旧 artifact
`visible-exact-cached-cap-adjoint-proposal-43662395328-1`
已经保存
`proposal-state/selected-intrinsic-proposal.npz`
和
`proposal-state/selected-intrinsic-proposal.json`。
v2 先核旧 run/source/worker/manifest、上述准确失败 native、两门通过和
0 QR blocks，再核原 receipt 指定的 NPZ SHA，并原字节复制这两个文件。

新 producer 还会把 receipt 的完整 7908 jet 身份与本次按原 receipts
恢复的原行重新比对。它不会重新选择这些已成浮点标量，也不依赖不同
runner 的 BLAS 输出逐位相同。只会开始原本尚未执行的完整 257 状态、
97 输入 QR，后续有限动作和连续残差的义务仍按原提案合同。

v2 使用独立的新 source、worker、manifest、workflow 路径；原 247 pins
全部保留。原五件和全部失败字节不修改。所有新数值只在本公开仓库
Actions 执行；恢复大数组仍只在 runner 下载原 artifact，小摘要上限
仍是 60000 UTF8 bytes。
