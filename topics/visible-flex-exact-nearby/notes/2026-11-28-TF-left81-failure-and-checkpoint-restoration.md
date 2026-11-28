# TF run46120139018/1：第82个 left 图枢轴失败及完整载体恢复

2026-11-28，visible-exact-astra-b0d5a16-20261128 / cap_world。
**实际失败的只读诊断；新图表数学另列。** 本条没有运行任何新数值目标，
没有重做原81个成功的检查，也没有把失败称为真实算子奇异。

## 实际完成范围

原完整文件均在 `notes/true_low193_direct_flow_ci/run-46120139018-1/`：

| 文件 | bytes | SHA256 |
|---|---:|---|
| `actual-scientific-conclusion.json` | 57359 | `5f1b15db26e603d9718ca9798ec704cc081b5b64d3ff22ff3cfcaaded030d65d` |
| `execution.json` | 63045 | `2dbb23e378379a185e7e8abce731d87dc77881e585742c67849d5f95dfbc087a` |
| `report.md` | 528 | `78e619e12c601edc7b995d0d54c6bc58b0db60b3f7a3ebfed531e456eca4c649` |

原 manifest SHA256 为
`9bee97cd5e7a16d6535184ab0bfdd32c6c4c3ee14be32084a5ec6ed33ed84d13`。
本次 metadata 核对完整86个 current inputs 的 bytes/SHA256/Git blob、
actual/execution/manifest 三份完整输入清单、全 source binding、runtime
参数和21个实际通过的门。全81个 left pivot 记录的顺序 hash 为
`80e7f82630d6f9ce83beeee726212d5282dce48a7b1ab125ef41008a292e740a`；
已从所有记录的原顺序重新核对。这些都是字节与格式检查，科学目标为零。

科学进程从07:13:29 UTC到08:31:30 UTC，数学计时4669.906695433秒，
child计时4681.066264018001秒。`child_timeout=false`。这是实际 finite
inverse 失败，不是时间预算、publication 或 wrapper-only 失败。

原 left97 的 index0至80成功；right96、node transversality 和 source
map完整目标均未开始。两项自然目标的 `completed_targets` 都为空。
第82格 index81 的实际97维矩阵在4、8、16、32、64子盒都不能由 Arb
证明可逆。只在这一个未完成格内加密，已完成的81格在原job中没有重做。
该格是 parent81 的唯一 refined slice；旧完整 plan 的真实固定长度为
`.001152`。不能把旧 midpoint plan 的范数当作本次 actual proof。

成功 left inverse 的原向外上界指数满足：index0至76为1，随后
index77、78、79、80依次为2、3、4、10。每个指数 $e$ 的语义是完整
induced-2 inverse norm不超过 $2^e$。最后失败矩阵的完整2范数上界约
823.788。它不是最小奇异值下界，亦不证明真实矩阵奇异。

这说明固定 graph chart 接近坏条件或矩形区间传播恶化；仅凭这些
public scalars不能区分真正的图表极点与 enclosure wrapping。
继续把同一格64改成128既没有消除前置graph的不确定性，也没有提供
这种区分。因此新的计算必须真的改变 graph 表示或全边值算法。

## 原私有数据的准确地位

原job保存了全97×97最后失败矩阵和全96×97的 $Z_{81}$：

| 完整原载体 | bytes | SHA256 |
|---|---:|---|
| canonical未压缩checkpoint | 4955126 | `3916928e630d814f8ec7e0d22b1470d0a9caa4f34150d1d7ccef8f185843d105` |
| `gzip.compress(...,mtime=0)` | 842453 | `c0718447c4ef8e8d50c11561eb24947903090a5db2306223ec56399ba4629f33` |
| 原完整PackedMatrices顺序payload | 314059632 | `0be16da1dc652f830389b496eb87bb300a07dddcb564167fdbf9ef650b9ea8b6` |

这些大载体没有发布到git、Release或artifact，原回执明确记录
`complete_private_payload_durable_after_runner_exit=false`。因此只靠公开
81个指数不能直接继续矩阵运算；不能把一个新从头认证伪称为已有状态续算。

不过载体本身有确定的完整恢复recipe。checkpoint只含固定的manifest
SHA、run/attempt、原完整ledger、原preparation字段和两完整矩阵的48位
decimal balls；没有time、随机数或机器路径。原压缩使用 `mtime=0`。
原所有矩阵都来自固定Python3.12.14、python-flint0.9.0、384bit、单线程、
原完整输入和逐entry有向binary64 packing。已有图表是同一reference的
确定性exact-dyadic proposal，不依赖重新选出的QR。

配套 `fourfold_codazzi_true_low193_checkpoint_carrier_restore.py` 仅恢复
这些必要载体。它复制原81个验收记录，不发出新的旧结论；保留原
Peano/图递推、每步packing/readback、五个raw moment数组及原键顺序。
index81只恢复原最后64子盒矩阵，不再调用其失败inverse，也不重做
4/8/16/32失败候选。完整private-prefix顺序SHA、未压缩checkpoint SHA
和完整gzip SHA **三者实际一致后**，才返回可用载体。

完整prefix的19,628,727个entry恰为初始 $Z_0$ 的9312个，加上81组
$(C_i,\widetilde E_i,Z_{i+1},M_i^{out},M_i^{in,1},\ldots,M_i^{in,4})$。
恢复不能仅凭最后 $Z_{81}$ 的SHA就接受其他prefix matrices；三重完整
校验正是为了保留整个有序场。此恢复不计算原四个完整 source-map
norms，不计算 old HS/signed trace，不重新选择候选，也不重发81个
成功pivot的证明门。

**当前尚未执行该恢复recipe，三重科学载体hash是否重现仍为待实测。**
如果有任何不一致，必须停止导入该载体、保留原完整结果并记录差异；
不降低hash要求，不选择性导入一个子矩阵。后继实际图表目标将从
验收后的81格prefix接着处理index81及所有尚未完成的右图/横截/源图。

## 新图表必须保留的对象

后继仍是同一原WVC hybrid、full-family principal eta、repaired lower
coefficients、原独立even mean、普通dr、真实root和原97/96边界。换计算
chart不改变物理 $S$、$\Theta$、full $\Delta A_L$、high/CFB或TP链的接口。
新chart的浮点QR只能选exact-dyadic193 frame；它不能授予严格正交。
必须支付其完整inverse、condition与adjoint转换。

一般中心 $Z_c$、联合误差 $\|Z-Z_c\|_2\le r$ 下，分块传递
$E=\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)$ 的新graph
中心 $\widehat Z'$ 必须用完整量

$$
A_c=A+BZ_c,\quad
R_c=C+DZ_c-\widehat Z'A_c,\quad L=D-\widehat Z'B.
$$

若 $g\ge\|A_c^{-1}\|_2$ 且 $g\|B\|_2r<1$，则

$$
\|Z'-\widehat Z'\|_2
\le \frac{g(\|R_c\|_2+\|L\|_2r)}{1-g\|B\|_2r}.
$$

只有已经严格把中心化成零时才可用简写 $A_c=A$。完整误差以一个
operator-norm球传递，避免每一步把它重新当成96×97个独立自由误差。
这是一条新算法的输入约束；本失败诊断没有声称它已经数值通过，
也没有把low hybrid资格升级为full positive或README完成。
