# 原加权 Legendre 新探针：无条件消去式不成立

会话：Astra-serre-24b8836b-20261126。实际执行完成于 2026-11-28 09:46:48 Asia/Taipei。

## 固定输入与可复现回执

- 源提交：[d4b4b76db587abdd085d0a851c932f19ea7ade6a](https://github.com/Rogerhu12/math-research-public/commit/d4b4b76db587abdd085d0a851c932f19ea7ade6a)。
- 脚本：[legendre_weighted_probe.py](../scripts/legendre_weighted_probe.py)；参数：[legendre-weighted-probe-request.json](legendre-weighted-probe-request.json)。
- 公开 Actions [run 46094809839](https://github.com/Rogerhu12/math-research-public/actions/runs/46094809839)，job 140823622844，实际状态 success。
- 仅计算新窗口 1000<p<1100、p≡3 mod4，最多8个素数；窗口内实际7个。未重跑旧41/47或端值窗口。
- 日志结果 JSON 原字符串（不含前缀和换行）的 SHA256：`44388ce6f1491f56450072d52ff825cc28f05ec7f876d3505040d54b030b171b`。root 对实读日志重算此 metadata hash 相同。完整可重算数值留在 Actions 日志，不存仓库 raw/artifact。

脚本从同一个 Pν、Wν 的实际递推生成原五矩，核 Pν(1)=1、Wν(1)=Hν 及首矩 Qν−q_p(2)，然后读取 [R1154 §11](../results/R1154-original-Gaussian-first-profile-and-joint-finite-Gauss-moments.md) 的 Cν(Qν)、真实 D2 和两个实际条件。数学只在本公开仓库 Actions 中执行。

## 此次能够登记的结论

**无条件恒等式 Cν(Qν)=0 不成立。** 一个完整反例是 p=1019、ν=169：
q_p(2)=724，Qν=928，Cν(Qν)=828≠0；同一次读取 D2=75、Bp−3=809、Cν(Qν)+(3/8)Bp−3D2=781。

这只否定无条件消去捷径。该例 q_p(2)≠Qν，故没有满足原首标签零的前提；不能用它否定或证明条件于 H_p=0 的联合约束。实际窗口中没有原联合零例，且七个 D2 都非零，这也不是一般素数上的非零证明。

后继改为同一原 actual-good Newton 余核与 finite-log 差分，或直接处理条件联合关系；不继续追已被反例否定的无条件 Cν(Qν)=0，也不因这个小窗口扩扫。主目标仍 OPEN。
