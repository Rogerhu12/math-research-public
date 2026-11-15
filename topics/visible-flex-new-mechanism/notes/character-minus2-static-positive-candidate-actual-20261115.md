# 指定静态正外点的公开实际回执：68 行与完整十四族均准确通过

日期：2026-11-15。消费已经完成的公开 Actions 输出；没有本地重跑研究、求根、LP、路径积分或旧函数表达式。

## 1. 本次准确结论

公开 run [43669803169](https://github.com/Rogerhu12/math-research-public/actions/runs/43669803169)、源提交 `7d29631406407408e7fed52fdbc014e036d5a6ab` 的 `character_minus2_static_positive_candidate` lane 已完整完成。

只将上一公开外点的自由坐标 $y_{12}$ 从 $-11/48$ 改为 $-1/2$，其余自由坐标不动。本次准确有理检查得到：

- 全部 68 条已存必要半空间满足；没有负行。
- 零行恰为零基编号 $64,65,66,67$。其余 64 行严格为正。
- 所有已存 $F_0$ 次数均被检查；经旧变换后非零支撑只在 $0,2,4,6$。没有按预期删去奇次或高次项。
- 十四族全部与指定系数吻合；十三个非静态族与上一公开点逐系数相同，包括已存零系数。
- 同一个规范化八矩乘子及两个 cocycle 的值准确吻合。

主报告 `completion=complete`、`explicit_outer_point_verified=true`。实际新计算耗时 **0.007691300 秒**，峰值 RSS **25.4296875 MiB**。这些是本次 consumer 的运行数据，不是整个既有理论或所有前序实际的总成本。

这给 [R173](../results/R173-explicit-positive-complete-scalar-action-and-remaining-real-head-question.md) 中明确外坐标点的原归档接口核验。**没有证明该点在真实原函数空间上良定义，因而没有构造真实正字符。**

## 2. 原输出与身份

输出目录：

`notes/actions-43669803169-1-character_minus2_static_positive_candidate`。

| 原文件 | 字节 | SHA-256 |
|---|---:|---|
| [主报告](actions-43669803169-1-character_minus2_static_positive_candidate/character-minus2-static-positive-candidate.json) | 5876 | `49e0688acfc139a9d4dc36dc468638a6d63986c0a3eeeec69717fbb988192127` |
| [publication receipt](actions-43669803169-1-character_minus2_static_positive_candidate/receipt.json) | 40792 | `68525fb0a9e9afb381f6998e1771b10bba5b08841e746695548c4ec688ebf3db` |
| [人工开发报告](actions-43669803169-1-character_minus2_static_positive_candidate/character-minus2-static-positive-candidate-development.json) | 4437 | `6a11f3f4ef9cfdf5044a4842367e95fc87a26e66295ba4bc939efb09695a0ae5` |
| [完整 certificate gzip](actions-43669803169-1-character_minus2_static_positive_candidate/character-minus2-static-positive-candidate-certificate.json.gz) | 9305 | `b5b3dacf8d8078c069f73567e82fc8bcbe2bb411bf1bbe057ac0c360a9f49122` |
| certificate 解压 JSON | 34719 | `fdc79bfb8f7300912bab7ea29071a163c49afd82d22acc1a328adec54c7ce822` |

冻结 consumer 是 `literature_character_minus2_static_positive_candidate.py`，35719 字节、SHA-256 `644b2897d142964fea9e6b0a11348d6c1eef9be93af1514e06a4d10ae652fa45`。

本次已完整读取主报告、receipt 和开发报告，并对两个输出小文本重核原字节长度/SHA；其四项直接来源绑定与 receipt 一致。receipt 共列 196 项源码来源，不能把本次对四项直接依赖的核验误称为再次独立核过全部 196 个源码文件。root 终端物化完整 gzip 后，本稿也只读其原内容并核两层 SHA：完整 68 个有理值、107 个 normal 值、两套十四族及 `complete_point_evaluation_saved=true` 均已保存，未重新评价任何原行。

发布回执记录真实 pull 从研究源提交到 `844033b0748666cbe80a8a0ef67a4050a15b7b7e`，两份 README 未变，`readmes_read_commit` 为该提交。原始研究源身份仍是上述 `7d296314…`，没有随发布 pull 改写。

## 3. 指定点与共同乘子

继承的 23 个自由 normal 编号为

~~~text
[2,3,14,23,26,28,38,43,58,63,67,69,73,90,91,94,96,97,99,100,101,103,104].
~~~

实际核验的点是

~~~text
[1,1,-1,1,0,1,-1,-1,1,1,0,1,-1/2,1,1,-1,1,-1,-1,1,-1,1,1].
~~~

自由编号 12 对应 normal 编号 73；没有新增归一化坐标或修改旧 $x=B y$。

在 $(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1)$ 次序下，实际存储线性行给

$$
\mu=(0,1,2,0,0,0,0,4),\qquad c=0,
$$

$$
d=(0,2,6,0,0,0,0,8).
$$

这是对同一个点、同一个乘子定义的完整检查，没有逐路径调整乘子。

## 4. 全十四族结果

| 修正标量族 | 实际准确多项式 |
|---|---|
| $F_0$ | $\tfrac12-\tfrac32 k^2+k^4+k^6$ |
| $Q2_0$ | $1+k^2$ |
| $Q2_1$ | $-k-k^3$ |
| $Q2_2$ | $1+k^2+k^4$ |
| $\bar A_{hh}$ | $1+k^2$ |
| $\bar A_{hk}$ | $-k$ |
| $\bar A_{kk}$ | $1$ |
| $H_1$ | $-k$ |
| $H_2$ | $-1$ |
| $Q4_0$ | $0$ |
| $Q4_1$ | $0$ |
| $Q4_2$ | $1$ |
| $Q4_3$ | $-k$ |
| $Q4_4$ | $1+k^2$ |

主报告另外保留 $Q2_0$ 的奇次零项、$Q2_1$ 的二次零项、$Q2_2$ 的一次和三次零项。它们没有在旧输入检查前被删去。

由已证明的 [R172](../results/R172-exact-highest-and-quadratic-certificates-for-the-updated-outer-point.md) 与 [R173](../results/R173-explicit-positive-complete-scalar-action-and-remaining-real-head-question.md)，这组完整系数给

$$
\mathcal A[h,k]\ge\frac1{16}\int h^{-2}\,ds>0
$$

对正时长、正 $h$、真实水平、两端平坦的路径成立。这里最高层的全部面积项、速度四次项及端势都已由对应纸证保留。本次仅检查新点完整系数确属那一已证情形，没有重复 Gram 求解、SOS 推导或新路径积分。

## 5. 实际支付与未支付的工作

本次消费 run 43668125602 的主报告、receipt、完整 68 行证书，以及 run 43665971895 的原完整系数证书。既有 124 条外等式、旧 RREF、107-to-23 变换、六条路径积分、63 行旧前缀和后增五行均没有重建。原等式通过已证且原字节绑定的 $x=B y$ 继续适用；这里没有重新宣称真实函数秩等于外坐标秩。

开发阶段的七项检查、18 个发明多项式例及近重根人工例全部通过。可复用的精确三次半轴 oracle 只用于这些人工例；本次 actual 的 `real_static_oracle_called=false`。主报告亦明确 `LP_or_RREF_or_path_integrals_called=false`。

完整 certificate 保存所有 68 行值、107 个 normal 值、两点的完整十四族、共同乘子和来源绑定。因此后继原函数关系消费者可直接读取同一确切候选，不需要再次生成这个有限系统或重新搜索外点。

这个点的完整标量路径正性已经支付，继续给它增加合法静态、时长或路径必要行不会解决剩余问题。下一真实门是原 107 个 normal 与 40 个响应列的两模式原函数关系：若某条准确原关系在此点非零，就排除它的泛函良定义性；若有限批关系都满足，仍需完整关系空间或足够的真实独立性证据。

本次不声称真实正字符存在，不排除或完成全几何等距族，不支付完整周期/ruling，也不改变这些边界。
