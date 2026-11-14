# 同一 P1 场的 cell12 真单模端点：1873 原片的 log r 常矩阵指数

作者：exact_closure（GPT-6 Astra Pro，AI 辅助），2026-11-13。

## 1. 已完成结论与量词

本结论消费已存在、已与原场识别的 P1 内场。P1 是 `R156_actual_full_cut_posterior`：原六个 S 坐标的乘积半径为 3/8，T 共同 l1 半径为 1/64，另有原保存的全部逐坐标帽。完整准确域在主包 `domain`，不将这些帽扩大到原单位域。全部角宽同移 2/5，Vprime、真实几何与物理规范不变。

在原 node12（内 cell12 的外端，外 cell11 的输入端），本次给出物理频率 94,96,…,184 的 46 个真端点帽。与既有 7 个余窗及完整无限尾相交后的三带共同强质量为：

| 物理频带 | 同移 2/5 后的已证上界（近似显示） |
| --- | ---: |
| 94…184 | 2.8012823127044167e-68 |
| 186…8190 | 9.564859311943682e-59 |
| 8192…无穷 | 7.648557022519089e-220 |

准确数均为主包的向上 dyadic；显示小数不参与证书。新单模帽中，m=166 为 7.58061740296593e-71，m=184 为 3.2189567346722234e-84。余带和无限尾沿用同一已证场的旧合法帽，未截断。8192…无穷仍保留原 34816 分割及同一个父质量约束。

读出角宽为原准确 `head_strip` 加 2/5，约 0.54443583074826767。输出仍是原 SHA `617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9` 的物理 balanced P/K 头强质量；不换成 canonical 范数，不增减 w。新结论是同一场的有限读出收紧；不在此宣称新的固定点、外 9…0 延拓或闭面完成。

## 2. 原片、真实系数与不同于几何 Peano 级数的新比较证明

全部 1873 个原 cell12 面板按原物理 r 递增次序使用，9 段片数为

`[1,334,1,640,1,614,1,280,1]`。

原 positive canonical 系统的非负比较系数满足

\[
a\,dr=\sqrt{12}\,\mu r^{-8}w^{-1}dr,\qquad
b\,dr=\sqrt{12}\,\mu^{-1}r^6w\,dr,\qquad
d=(m^2-4)d\log r,
\]

状态为 `(Q, Xi/nu)`，其中 \(\nu=m^2(m^2-1)/12\)。在一原片令 \(t=\log r\)，原真实 r 严格递增。用该片已有的严格 r、w 包和 \(J\ge\Delta\log r\) 定义

\[
A_0=\sqrt{12}\,\mu_+ r_-^{-7}w_-^{-1}J,\quad
B_0=\sqrt{12}\,\mu_-^{-1}r_+^7w_+J,\quad
d_m=(m^2-4)J.
\]

这里 **A0 不含 nu**。逐点生成矩阵在 t 坐标被常非负矩阵支配，故整片传播及任意后缀均被

\[
\mathcal A_m
=\exp\begin{pmatrix}d_m&\nu A_0\\B_0&d_m\end{pmatrix}
=e^{d_m}
\begin{pmatrix}
\cosh q&\nu A_0\,\sinh(q)/q\\
B_0\,\sinh(q)/q&\cosh q
\end{pmatrix},\quad q=\sqrt{\nu A_0B_0},
\]

支配。后缀的 t 长度不超过整片，非负矩阵指数逐项单调，所以同一整片矩阵也包任意源点到片末的传播。

这是常系数正系统的指数比较，没有使用 `(I-C)^-1`。因此本证明不要求 \(\nu A_0B_0<1\)。实际最大值约 5.3297501865 被原样保存；没有修改旧 Peano 证明中的门，也没有把旧证明在门外使用。

全部 cosh/sinh/exp 在 256 bit Arb 进行；每个量均核有限、非负和真实正除数。没有新 ODE、径向积分或物理细分。

## 3. 源位置、条带和两材料完整计费

原 moving-strip 的每片损失下界直接由原 `btau_integral`、`btau_total` 和原首末宽度获得。若其下界为 \(\delta\tau_i\)，已进入片首的状态付

\[
Y_{i+1}^{\rm carry}\le e^{-m\delta\tau_i}\mathcal A_{m,i}Y_i.
\]

当前片内源使用完整正后缀，不乘该片的整片角宽衰减：

\[
Y_{i+1}^{\rm source}\le
\mathcal A_{m,i}(0,I_{i,p}/\nu)^T.
\]

源材料为原物理 kappa 方程中的

\[
d_1=V'^2/(rw),\qquad
d_\lambda=|w_r/w|V'^2/w.
\]

原参考 Vq 与真实 Vprime 的比例平方 `(S sigma12)^2` 付一次。每片材料积分用原严格帽与 canonical common 积分帽相交：

\[
I_{i,1}\le\min\{r_+^4 V_{q,+}^2J/(\sqrt{12}\mu_-),I_{i,\rm common}\},
\]

\[
I_{i,\lambda}\le\min\{r_+^4 V_{q,+}^2\operatorname{TV}(\log w)/(\sqrt{12}\mu_-),I_{i,\rm common}\}.
\]

片末状态经原 canonical 到真实物理出口的协向量读出，保留源强权 `(1+m)`、原保守两分量费用 2、真实出口 w 的正下界及 `(S sigma12)^2`。各材料单独与旧完整合法 source kernel 取 min。所有角宽同移 2/5 时，片间差及 source-to-output 的权差不变，故此几何核可消费新宽场。

## 4. 齐次输入：同一个物理双分量质量

片首输入写为 \(U=|B_{13}p_m|\)、\(V=|\kappa_m|\)。沿原真实端点坐标，

\[
Q\le U/(B_{13}m r_{\rm in}^3),\qquad
|\Xi/\nu|\le
\frac{r_{\rm in}^4w_{\rm in}}{\sqrt{12}\mu\nu}
\left(\frac{m}{B_{13}}U+V\right).
\]

这两列分别经完整已计角权的 1873 片矩阵积，再经真实物理出口协向量读出。取两列系数之最大，消费同一 `U+V` 质量。此处无需重复 frame jump，也不再付 whole-cell 双径向 supremum 的额外 2；它是同一端点的两个分量和。

输入 cell13 的 whole-cell Vprime 范数仅在该真实端口用已证 `Vprime13(boundary)_upper` 消费。不将端点帽除以上界而冒作 whole-cell 范数。新的单模齐次列与原覆盖该模的旧父窗真点态列取 min，仍为合法上界。

## 5. 完整非线性源与共享质量的读出顺序

固定 \(C=C_S+\Lambda\)，\(F=C+e\)。本次直接复用成功 fine53 全场包、完整 reference Laurent 源、213 个 DQ 源块和已付 Q/T 源帽。每个近频输出保留

\[
N(C)+DQ(C)e+Q(e)+[T(C+e)-T(C)].
\]

`N(C)` 包括完整均值根、有限逆多项式和严格正无限逆尾；T 差分保完整均值及逆；Q(e) 保所有低、中、高互作。只有有限中心对有限目标的 DQ 无限输入列因准确支持为零；没有据此删除完整非线性高尾。

在本数据 B_floor>=120、物理输入频率>=2 的原逐对公式中，s 材料正卷积逐系数支配 ell 材料。故同一 `common_d` 质量可乘两材料核之和；这不是将两个独立源范数的最大值当共同逐模 majorant。

对一个单模，先付 cell13 真输入，随后付 reference、DQ、Q、T 的完整正项，再与旧同模头帽取 min。对近带共同质量，则先把 46 个真实输出列合权，再消费每个共享输入质量：

- cell13 输入保 53 子窗、原 13 父窗与 near/rest 共同帽的嵌套 support；
- reference 有限多项式逐模合权，无穷逆尾只乘最大读出核一次，再与整个 reference 近带共同帽相交；
- DQ 低 46 列先按输出合权，再以逐低模帽和同一个低共同帽做正 support；
- DQ 近 46 与余 7 列分别保原父窗及 near/rest 质量，完整无限输入按其实际列付；
- Q(e) 的近带共享正帽和完整 T 共享帽各只乘最大 source kernel 一次。

最终近带帽是旧近带帽、新完整合权像和新单模帽之和三者的 min。完整合权像约 5.942855784247824e-66，单模相交后的和更紧，故最终共同帽为 2.8012823127044167e-68。没有将合权 support 的最优质量分配重复给每个输出。

## 6. 原始描述字段的下界序列化勘误

heavy producer 的每条核公式使用的 `woutlo` 是两个原严格 w 下界的 min，数值计算正确；但原主包的单个描述字段 `true_w_out_lower` 误用了通用向上 serializer。原文件、源和资源全部保存，不修改。

fresh exact normalizer 仅将该字段改成原两条准确 dyadic 下界的 min，并绑定原 SHA、原 owned resource、全部 numerical rows 的 canonical SHA。原字段明确标记不得作为下界消费。46 行 numerical rows 在修正前后完全不变，其 canonical SHA 是

`2021e3973fb8d78c71b50f66a446477ed30e7c9acca4c528e96f202a796c23c7`。

点头消费者要求 normalized-v2 schema，另实际核原 heavy resource 成功及峰值。此勘误没有重跑核、改变任何积分或放宽数学门。

## 7. 实际执行、完整输入与剩余任务

| 实际阶段 | owned exit | 耗时 | 峰值 KiB |
| --- | ---: | ---: | ---: |
| 原 1873 片、46 单模 log r 核 | 0 | 381.6372688 s | 27032 |
| 准确下界描述字段规范化 | 0 | 0.3383989 s | 12544 |
| 同一 fine53 场完整点头消费 | 0 | 0.7621989 s | 43516 |

原核主包保存 266044 个成功门；其打印计数还包含最终小文件门。规范化包增加一个 numerical-rows 身份门，保存计数为 266045。点头主包 114 门全部成功。均保持原 96 MiB 资源门。输入包、helper、原 1873 片、完整源与原结果的 SHA 和准确命令见 manifest、primary 及 owned resources。

原核 SHA：`54e027cee79695f01ba8101ab8a33c7a4788e294da582f59d02b745f4390c8ac`。

规范核 SHA：`4b0f610c31dd332c54ebaebe50400a5c4303bbbc0f2bdcbd82fbbd581cdda2be`。

新真点头 SHA：`1905c047655b246283c3374eff763566c8e707e5bd5fc084b480e5d2dc0b2f69`。

该新输入可继续消费原外 11/10 的 186 窗全部正算子和完整固定 LF 源，并从已有成功八轮同场状态做有限 min 代入。它尚未单独证明外 9…7 的非线性留管、外 6…0 延拓、闭面全 t 家族或本课题完成标准。
