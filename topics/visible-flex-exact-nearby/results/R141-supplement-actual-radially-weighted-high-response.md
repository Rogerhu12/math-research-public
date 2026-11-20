# R141 补篇：实际完成径向加权的完整高频 head 响应

2026-11-20，visible-exact-astra-ac637-20261120 / positive_inverse。

**已证明（公共有向计算）：** 同一原实际 given-head 高逆 $G_H$、完整真实 family 与同一固定 WVC 输入 $S$ 下，[径向加权源合同](R141-supplement-radially-weighted-actual-high-source-response.md) 的五个新目标已在 public run **44746534556/1** 全部完成。它们给出一个新 body source 常数及完整 head 到 high 的 body、body-$Z$、root-$Z$ 与真正外 even trace 上界。本次未调用旧 GH5 五源率、旧 GH4 四响应、旧 Riccati/ordinary-source sweep 或低193传播。

## 1. 实际运行、源码及完整结果

workflow event commit 为 `856a7af4513cdb3f771da82e8b39a1225669d52e`，实际科学 checkout 为 `cbffb49f57d36f2e2e1cf586daf41b5c4f84e181`。以下文件均按完整 bytes 与 SHA-256 核对：

| 对象 | bytes | SHA-256 |
|---|---:|---|
| [frozen manifest](../notes/2026-11-20-actual-GH-weighted-response-inputs.json) | 70834 | `f544cf42442f81c2c2edcd0e4e5f5c5402161d10640c2be43a394ae534b4f0a1` |
| [whole scientific conclusion](../notes/actual_GH_weighted_response_ci/run-44746534556-1/actual-scientific-conclusion.json) | 56554 | `6e32b9ef4cafc6517670c9de76e3041ba35ee7454e70cf2ccc3aaef34916f36c` |
| [whole execution](../notes/actual_GH_weighted_response_ci/run-44746534556-1/execution.json) | 57850 | `d96bd1137d6e6f3f49ee5613402a9bd6b3763b096c3f4be9613437bddd1cbedc` |
| [mathematical module](../scripts/fourfold_codazzi_actual_GH_radially_weighted_math.py) | 17375 | `6bb32619998f8cdeb428a88faf021afab6fe92409a216bee9ebca439ac7cfa30` |
| [public owner](../scripts/fourfold_codazzi_actual_GH_radially_weighted_owner.py) | 28755 | `a97d50766135ad9954c4fd84b77f3bb8590acafea1b5305fe701571bd563a762` |
| [unchanged shared worker](../scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py) | 40772 | `98ef3773eab06178df086c5dcf551103c7cd3e00a5eca1c73cbfee089af84b1c` |

runtime 为 Python3.12.14、python-flint0.9.0、320bits，三个线程环境均为1。科学结果记录数学时间98.15656063199998秒；execution 的 child wall time 为108.93323121400002秒。child returncode 为0，无超时或异常；scientific `complete=true`、`proved=true`，execution `scientific_complete=true`。

这次完成全部153 reference definitions、155原 comparison panels，包含154个 body source panels与152个不同的 body parents。实际共同细分为 **4802** 格；两个标量方向各完整走过4802格，全部原4650 closed gap/frame 行和3594 interfaces先只读准入，原上下文4801 intersections身份保持。共同细分数没有被原上下文的intersection数替代。

## 2. 完整准入、身份和保存资格

39个科学字段、25个按原次序通过的门、79个 current receipts以及9个科学模块绑定，均逐项与 frozen manifest相同。79份当前文件的完整 UTF-8 bytes、SHA和Git blob均核对；execution 的28条Python AST receipts完整匹配实际文件。原50目标配方参数只作为同对象身份保留，本次 operation明确只有五个新目标，未重新进入已排除的 small-$K$ 图。

scientific 与 execution保留同一个完整21项历史恢复对象：原19项，加 signed germ与原root budget两项。所有manifest字段与实际恢复标志逐项相同；本次后验审读只检查公开metadata，没有本地恢复原科学数组。其canonical whole对象15033B、SHA

`8213b004a48508c580440cb7a38239d796c7afc9eece83bbd3f5a02e5b2d7ed4`

及原WVC恢复对象13771B、SHA

`4705f2c3a093724ed7e21bfee9ed30d481105e1aec8446da55a14fb0a764d7ac`

均与已成GH5完整execution相同。原native的25507783B整连接SHA仍为
`1f3e5fa630f39a667a96102f103ac8977d00e580f698a83904f361c5a05c6f3c`。

actual `reference_identity` 与GH5及GH4逐项相同：153项original-reference chain 为
`6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac`，153项selected-diagonal chain 为
`b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2`。原24480 fine cells、$p_0=13/80$、$S$、真root和finite-$\rho^2$规则都只作原身份保留。

原29同对象记录完整等于已成GH5中的副本。已成L、centre exclusion、GH5、GH4和base0/negative-one两份完整高图均保留whole-object references；其余端口和scope没有被提取某条标量时删除。执行的4次完整README receipts显示两个README差异均为空，累积SHA链为
`18134e757dcd1007a27fa66601a5f606faeaeec3e8ef471adedd0d7d22ea8c71`。

owner每次保存一个whole decimal ball后，实际读回该记录，检查 `saved.contains(original_upper)`，才把读回upper交给后续公式。第一条 $G_B$ 因而先保存再用于原反馈正公式；第三条 $H_Z^{\rm rad}$ 先保存再用于最后的外迹转换。下表只逐字抄录这些完整已存球，没有后验重算任何科学量。

## 3. 完整五条已存有向球

| 记录字段 | 数学资格 | whole saved ball |
|---|---|---|
| `actual_GH_body_weighted_unperturbed_source_upper` | (W.7) 的 $G_B$ | `[8.13066460190862514076471465851478574444828912653706325607508279558973300498 +/- 1.62e-75]` |
| `actual_GH_weighted_raw_L2_from_complete_head_upper` | (W.11) 的 $H_B^{\rm rad}$ | `[29.4312937768741884149094703978009481991927236145936333029976894014697591015 +/- 2.96e-74]` |
| `actual_GH_weighted_body_Z_sup_from_complete_head_upper` | (W.13) 的 $H_Z^{\rm rad}$ | `[11.6931388927010654432321119964737470019542808363593236067742775684206959089 +/- 1.41e-74]` |
| `actual_GH_weighted_root_outgoing_Z_from_complete_head_upper` | (W.13) 的 $H_{\rm root}^{\rm rad}$ | `[11.6931388927010654432321119964737470019542808363593236067742775684206959089 +/- 1.41e-74]` |
| `actual_GH_weighted_outer_even_Hminus5over6_from_complete_head_upper` | (W.13) 的 $t_X^{\rm rad}$ | `[0.150684779545116822722063298923630760334462381911846953695544814026039895733 +/- 4.30e-76]` |

后继消费资格是每个保存球的**有向上端点**，不是表中的展示中心或其截短小数。body-$Z$与root-$Z$的两个已存球恰相同，只表示这两条完整比较返回相同上界；不声明两个实际观察算子的范数相等。

## 4. 这些上界作用于哪个完整对象

沿用(W.1)，输入是普通径向 $L^2(I;E_L)$ 中完整193维transformed head $x$，并且

$$
B=(B_{HL,c}+\Delta B_{HL})S^{-1}.
$$

原 $S^{-1}$仅作用一次；角频率为真实 $4j$、角测度为原normalized real basis。centre source到160、family source到288，只是源支集，**没有截断无限高未知量**。centre mean列的准确零不被延伸成实际family mean列的零。

对body的每个固定 $r$，两个diagonal source支分别使用 $[r_b,r]$ 和 $[r,R]$ 的输入，输出属于原 $Z_s\oplus Z_u$。因此(W.6)的两支平方可以用(W.7)的最大值合并。完整4802格的两次有向递推支付该 $G_B$，所有coefficients仍取原parent whole balls；细分没有把区间球当点值，也没有新增窄球资格。

随后(W.9)继续使用原已成实际高feedback、原exterior high reflection和原collar/body接口resolvent。它不是对feedback再次套用径向半区正交，也不重算原resolvent门。collar完整head source从GH5已存球只读接入；root stable、外部独立mean/head、affine和两个cut外端口在**本head-response**中取零，其完整原高图列仍保留。

由(W.10)–(W.13)，完整高解的collar与body输出按真实径向直和组合；2×2正比较矩阵取其完整2范数，保留两输入区域的共同相关性。真正外trace通过原high frame的 $5/388$ 因子恢复，而不是从任意body-$L^2$赋予端点迹。因此新 $H_B^{\rm rad}$ 与 $t_X^{\rm rad}$ 可以用于[参考边界提升与实际外块合同](R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md)中的对应接收位置，其余low source/receiver、family return及joint193 atoms公式全部不变。

## 5. 冻结和仍未结清的部分

本次所有旧完成目标、旧五源率、旧四响应、旧无权source sweeps、旧Riccati/feedback、$G_f/G_H$ actions、low inverse actions、endpoint/atom目标和原small-$K$50图的调用计数均为0；没有发布新数组、artifact或Release。这五条新成功现按完整原JSON和execution冻结，后继只读消费。

`weighted_response` 明确保留以下false scope：actual low-high inverse、actual physical outer rows、原finite-$\rho$桥、原七输入端口的完整低高闭合、任一原WPN RHS以及课题完成标准。原rough ports没有升级成raw-$L^2$，旧WJK有限trial $F$没有免费改成真实 $G_H$。若以后消费旧finite-$\rho$结论，仍须支付 $C(F-G_H)B$ 或完成同一实际对象的新桥。

R141低193的完整四source receiver与whole-interval实际逆是单独目标；本次不生成任何尚未存在的low bound，也不从浮点endpoint条件数推得它们。以上五球只结清本篇所列完整高head响应，并为该实际逆路线提供可消费的新上界。
