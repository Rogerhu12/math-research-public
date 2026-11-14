# R133 续篇：高根点真实完成前缀、Nyquist 精确投影与严格续算

2026-11-14，phase_inverse。

**真实执行记录与已证明的实现修正合同。**
公开 [run43650466853](https://github.com/Rogerhu12/math-research-public/actions/runs/43650466853)
已完成同一真根上的12列有限 primitive 求值并保存全部数组；
随后第8个门失败。没有完成新的高阶 energy 或 intrinsic 列。
本篇保留 child1 与原全部记录，说明为何应先验证区间包含精确零，
再依据原有限规则取准确 Nyquist 零值。
新 v2 是否通过剩余计算，只能由它的实际公开执行另报。

## N.1 原执行身份和真实已成部分

原科学源为
`beaf8a8d2b6a9534f4659ccd7b2a74d15c145be8ec1efe0778920ff1c90bb88b`，
原52输入 manifest 为
`568633a69fbe761fb5247f1fa665c6efdf49536d81f52c83fc44298f4b8c6ea8`。
workflow event 是
`74f0e1e365102d93bbb5a531572cece8099335ec`，
真正科学 checkout 是
`7e66b837168d42793134751d430ab98aac5787b4`。
原 Python3.12.14、python-flint0.9.0、numpy2.3.5、
scipy1.17.0 与320bit 均通过。

原 [process](../notes/true_root_high_intrinsic_jets_ci/run-43650466853-1/consumers/process.json)
记录真实 child return1、数学子进程时间3.0210725999999966秒。
source 自身最后 checkpoint 记录1.6865137630000007秒；
两个计时的起止位置不同，不能互换。
实际通过的前7门包括原对象/根/固定 $\eta_0$、两个完整辅助域、
原 finite primitive 的输入以及新的12列根点数组身份。
`finite_root_stage.complete=true`，全部原始数组都在 native。

新的实际完成计数是：

- 新真根有限点求值1次，12个普通径向导数列；
- 新高阶完整误差、有限范数、mean product、energy、intrinsic 均为0；
- 原辅助域、原无限尾、原65/193 cubic 域重算均为0。

失败原文是
`new true-root gate failed: the complete finite Nyquist column is exactly zero`。
这不是某个正性或小除数数学门失败。

## N.2 原小文件与完整 native

以下全部保持原字节：

| 原记录 | 字节数 | SHA256 |
|---|---:|---|
| `consumers/true-root-high-intrinsic-jets.json.gz` | 552891 | `6cd2e5bf334aa056b8ff401d246965d3f2d5109e481440186cc527477a1a60dd` |
| `consumers/process.json` | 6196 | `0cc5b063dbaf8138fb6b5df97b6a578831bf4f98cb99de7bf4967a24a829dc01` |
| `worker-process.json` | 2390 | `431c08080c2e3da9962ebc704c89c035bca4f15ac04460b4db9165dee6cb53a9` |
| `consumers/true-root-high-intrinsic-jets.stdout.log` | 1326 | `ed0abcff9c7244ad9f5deff4f302053e9459db0283f3a64413a8e6ffddb854e0` |

共同目录是
`notes/true_root_high_intrinsic_jets_ci/run-43650466853-1/`。
原 [worker](../notes/true_root_high_intrinsic_jets_ci/run-43650466853-1/worker-process.json)
确实在前后两次 `git pull --rebase` 后核两 README：
第一次从 `e3aa052a53471e292f42a0b227567640d41f106f` 到
`7e66b837168d42793134751d430ab98aac5787b4`，
第二次保持后者，两个实际 README diff 都为空。
这些事实不把原作业改成成功。

## N.3 精确有限规则与区间表示是两件事

原 `fourfold_codazzi_cubic_target_jets.py` 及新 count12 的同一规则，
在构造 unit primitive 时明确设置
$$
 P_j(N/2)=0,\qquad N=512 .
 \tag{N.1}
$$
这是一项原有限 Fourier 定义，所有 $j$ 都准确成立。
物理有限列为
$$
 (F_N)_j
 =\sum_{h=0}^j\binom jh a_{j-h}P_h
                    +a_j e_1+z_j e_3 .
 \tag{N.2}
$$
$a_j,z_j$ 只加入 Fourier mean。所以
$$
                         (F_N)_j(N/2)=0
                         \quad(0\le j\le11)
 \tag{N.3}
$$
也是同一有限函数的准确恒等式。

原 `Box` 运算对每次乘法、加法向外舍入。
即使它运算的是数学上为零的乘积，输出也可以是包含零的窄区间，
并非必须两个存储端点都恰为机器零。
因此原第8门检查
`all(endpoints==0)` 比 (N.3) 所需的严格区间验证更强；
它失败并不能否定 (N.3) 或已经完成的全部点值数组。

正确消费步骤是：

1. 读取原数组的真实 binary64 上下端，核形状、有限性和端点顺序；
2. 对全部12列、3个分量的 Nyquist real/imag 区间核 `lo<=0<=hi`；
3. 用原定义 (N.1)--(N.3)，只在一个新消费视图中把这些项设为准确零；
4. 原保存数组、原 false gate、原 failed process 和原 child1 一字不改。

若第2步不成立，v2必须失败并保存实际原区间，不能继续设零。
新的 native 应保原 Nyquist 区间和所使用的准确投影理由，
从而该实现修正可逐项复核。

## N.4 不删除完整无穷 Fourier 误差

(N.3) 只约束原有限函数 $F_N$。
它不声称真正完整 $F$ 的相应高模为零。
$F-F_N$ 的全部 Fourier 误差仍由原两个完整辅助域及
[高根合同](R133-supplement-true-root-high-intrinsic-jets-from-complete-auxiliary-errors.md)
(H.3)--(H.4) 付清。

在消费视图中使用 (N.3) 后，反向频率配对的有限零卷积准确无
Nyquist alias；同一 (H.8) 的三个分量误差和完整 mean 继续加入。
所有普通导数、阶乘、固定 $\eta_0$ 与真实根身份不变。

## N.5 仅对这个固定失败前缀授权迁移

新 v2 必须将本篇 N.2 的原 native/process、原科学源和原52输入
manifest 都作为精确输入。除了原第8个表示门失败，前7个门必须
逐项保真；原 point stage 必须完整，且原后续成功计数均为0。
原12列点数组的规范 JSON payload SHA 必须在迁移前后相同。

普通 resume 仍只允许同一个 v2 source、manifest、runtime 和原输入
身份。此次迁移只接受 N.2 指定的原失败记录，
不开放任意跨源或跨参数前缀。

v2 中不提供 finite target/FFT 求值分支；原 point 缺失或不匹配
就报错。它从该完整点直接接新的 Cauchy error、有限范数、
mean product、energy 和 intrinsic stage，每个成功阶段立即保存。
以后若有失败，不能再次计算本次已接受的阶段。

本篇只证明消费修正并准确记录已完成前缀。
高阶 $K,\beta,\gamma,s$、第一修正 Taylor 系数、
完整 old-circle $I/J$、独立 mean、所有物理 seam 与最终 strong
return 仍按各自实际完成状态逐项推进。
