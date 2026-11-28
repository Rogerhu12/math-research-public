# 2026-11-28：真实单 ULP 初猜及完整原离散残差

这次得到的是**新的、明确未接受的完整初猜**。其 55,344 条原离散残差已用实际原 native 输出算得 `3.652377088977401e-10 < 2e-9`；原 fresh full J、完整 heightJetJacobian 和 audit 尚待新原 worker 实付，不能把这份初猜或残差计算记为原 full-H 返回、闭图或课题完成。来源仍是当前真实 λ=.002/M24 设计。

## 字面状态和原始数据边界

E 的真实 `0027-state-input.bin` 保存节点 1..1152 的全部 48 分量，未保存 node0。其可见残差仅 node86/Pi/harmonic12 一分量超过门：state `519.6180251866067`，原 flow 输出 `519.6180251866068`，差恰为 `2^-43 = 1/8796093022208`，按原 scale `2.999686544393854e-5` 归一化为 `3.7899572518364145e-9`。原 α=1 试探没有严格降低 merit。

新初猜保留原 55,296 个下游分量中的 55,295 个，只将该分量上调一个字面 ULP。node0 是明示的新初猜定义：Q 取完整原 `desiredTarget`，Pi 取真实 0027 stage0 输出除以原 portRatio；没有声称恢复或保留未知的旧 node0 位模式。完整 H 的全部 24 系数、尺度递推、deep Robin 条件、模式/深度/步数及容差均不改。H/r^4 与原 desiredTarget 逐位相等。全部 1153×48 个未知量均保存。

原 cell n 只积分 state[n+1]。因此改变 node86 只改变 stage85 的 native 输入；它也直接修正残差 row86 的减项。node0 的新定义不改变任何 native 输入。旧真 0024 J85 只作可行性预估，预测邻段残差约 `5.476335739287853e-11`，未用预测代替实际检验。

## 唯一受影响段已真实支付

原 production executable SHA `1b47ed47e70e35a08f11173b1f17a5d1c2ee046f59f54f235ee5fa56de07af94` 实际执行完整 stage85 state 计算，exit0、用时 `0.9279225140016933 s`，64 个原 RK root calls、149 个更新、0 fallback。实际新邻段残差为 `5.920433066120782e-11`。不是 JVP、截模、局部线性残差或新降精度核。

其余 1151 段复用的是 0027 的真实完整原输出。每段全部初值（含两个零 mean）、系数、所有步/索引/x/h，完整公共 trigonometric/halving/容差/模式/精度/flag 字节及 native 源、binary、runtime 绑定均检查一致。1152 个原/候选完整 key 的分类和所有引用保存在 scratch preflight 中。生产 C++ 每次 vf_run_stage 新建 Engine；batch 数量与 opaque token 仅是外壳字段，循环编号只用于输出标记。复用段的 kernel_seconds 仍是旧实际时长，不冒称新的计算耗时。

## 完整残差及尚待门

| 项 | 实际值 |
|---|---:|
| 全部原残差，含 node0 | `3.652377088977401e-10` |
| node0 Q 行 | `5.179014456859017e-24` |
| node0 Pi 行 | `0` |
| 完整 H 边界 | `0` |
| deep Robin 行 | `2.663947909512669e-42` |
| 重算 stage85 行 | `5.920433066120782e-11` |
| 已修 row86 全分量最大 | `8.882712308991597e-11` |
| 全段 minA / minD | `.5559990629241173 / .9991573250502112` |

55,296 个 flow 行加 24 个 deep 行和 24 个 H 行均进入同一原最大范数。最大行现在位于 stage91/Pi/harmonic12；不存在以缺失 node0 的下界冒充全范数的问题。新 checkpoint 标记 accepted=false，原完整响应、全 J 和 audit 标记均保持 false。下一步只能将该真实完整初猜交给 unchanged 原 worker，并实际取得全部原门；本记录本身不构成那个终态。

全部大原场、单段原输入/输出及初猜留在 scratch；本目录只登记源码、小标量和真实 SHA。对应 JSON 为 `2026-11-28-tail-one-ulp-initializer.json`。
