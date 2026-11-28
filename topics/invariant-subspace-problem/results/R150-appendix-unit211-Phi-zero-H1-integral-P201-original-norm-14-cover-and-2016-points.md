# R150 补篇：H1 的真实整 P201 与三条原结式交至 14 次

> **2026-11-28 更正：本页经旧紧凑 R2 / Rbar 导出的原必要性、有限性、点数与排除声明已撤回。** 二重点一次坐标的平方被误写为 d1²，真实值为 2d0d1；完整更正和依赖边界见[原定义更正](../notes/2026-11-28-unit211-dual-germ-compact-mean-definition-correction-and-dependency-quarantine-8542.md). 已实跑的旧定义矩阵等式、次数与失败记录保留，不能再据此推原 Gram 条件或支付新模型单位。下文保留为原记录。


日期：2026-11-28（Asia/Taipei）  
会话：Astra-ISP-8542378f-20261127

## 1. 定理与范围

沿用 [P201 的首一整性与完整平方自由约化](R150-appendix-unit211-Phi-zero-H1-P201-integral-squarefree-complete-modular-reduction.md)、[同一点的多项式来源及固定结式接口](R150-appendix-unit211-Phi-zero-H1-polynomial-v-source-and-fixed-original-norm-interface.md)，以及 [真实首一六次与规范原点有限性](R150-appendix-unit211-Phi-zero-H1-global-original-monic-six-and-finite-normalized-points.md)。

本篇范围仍为原 unit211、$\Phi=0$、物理 $D\ne0$ 的 H1 余图。这里没有处理整个 $\Phi=0$ 权面，也没有把 $D=0$ 碰撞图并入。

**定理。** 在此范围内，存在一个首一有理多项式 $H(u)$，次数至多 $14$，使每个剩余原点都满足 $H(u)=0$。因此：
$$
\#\{(u,Q)\}\le56,
$$
$$
\#\{(u,Q,\lambda,T,v)\}\le1008,
$$
$$
\#\{\text{完整固定规范的原点}\}\le2016.
$$
这些是不同点数界，不是把权覆盖多项式当作原解概形长度。原 H1 尚未排空。

在 $1009$ 进完备化的真实 $P_{201}$ 模型中，剩余只可能位于五个完整 Hensel 块，其模因子次数为 $1,1,3,4,5$，每个重数均为 $1$。这五个块不是已识别的 $\mathbb Q[u]$ 因子；下一步仍须在同一原点的完整 $Q$ 四次环境及原值关系中处理它们。

## 2. 三条固定原多项式

在同一点多项式来源中，令
$$
F_0=\det[r,M_T r,M_v r],\qquad
F_c=\det[r,M_T r,c_T],
$$
并令 $F_m,F_n$ 分别把最后一列替换为完整原 $F_6$、完整原 $N_V$ 的已清分母同点列。四者的原 $\lambda$ 次数依次为 $6,6,9,10$；它们对每个本范围的原点均为零。

令 $g_4(u,Q)$ 为原 H1 的首一 $Q$ 四次式，定义
$$
N_c=\operatorname{Norm}_{\mathbb Q(u)[Q]/(g_4)}
       \operatorname{Res}_{\lambda}(F_0,F_c),
$$
$$
N_m=\operatorname{Norm}_{\mathbb Q(u)[Q]/(g_4)}
       \operatorname{Res}_{\lambda}(F_0,F_m),
\qquad
N_n=\operatorname{Norm}_{\mathbb Q(u)[Q]/(g_4)}
       \operatorname{Res}_{\lambda}(F_0,F_n).
$$
这些都是原输入系数的固定多项式行列式，实际正则 Sylvester 阶数分别为 $48,60,64$。原参数处的最高次系数下降仍保留；没有按参数点的实际降阶式另换较小结式。

已付来源保证每个原点满足
$$
P_{201}(u)=N_c(u)=N_m(u)=N_n(u)=0. \tag{2.1}
$$
所有只剥过的参数因子都有原已付单位来源；本次没有新剥参数因子。系数逐项检查给
$$
N_c,N_m,N_n\in O[u],\qquad O=\mathbb Z_{(1009)}.
$$
它们的实际模次数为 $3179,5131,5407$。后两条的特征零 $u$ 次数是否保留，不是本篇提升的假设；承担保度作用的是已付首一 $P_{201}\in O[u]$。

## 3. 本次完整 Bézout 返回

新源先在 runner 内按精确原定义再生 $\overline P_{201}$，并核其完整身份与已付约化相同。它再生三条固定原结式的模多项式，仅作为这次新比较所需的输入，没有执行旧有理数 Dixon 求解、旧赋权次数界或无穷远提取。

实际逐次共同次数为
$$
\deg\gcd(\overline P_{201},\overline N_c)=201,
$$
$$
\deg\gcd(\overline P_{201},\overline N_c,\overline N_m)=14,
$$
$$
\deg\gcd(\overline P_{201},\overline N_c,\overline N_m,\overline N_n)=14.
$$
记最后的首一共同多项式为 $G_{14}$。每一步二项扩展 Euclid 均完整乘回；随后把系数复合，另核回
$$
a\overline P_{201}+b_c\overline N_c+b_m\overline N_m+b_n\overline N_n
=G_{14}. \tag{3.1}
$$
还直接短除核回 $G_{14}\mid\overline P_{201}$。

事实上第二步已达到最终 $G_{14}$，其返回可取 $b_c=b_n=0$；另外两个输入的真实返回仍完整保存。式 (3.1) 中非零两系数的次数分别为 $5116$、$186$，没有传送其可重算系数载荷。

$G_{14}$ 的系数身份为 $58$ 字节，SHA256：
`73fb15af460042bc0f146122553e10262c97bbf75dec28aaaa471b88ee4a411d`。
它平方自由，完整因式乘积返回五个一次重数的因子，次数为
$$
1,1,3,4,5.
$$

## 4. 从模次数得到严格有理共同次数

令
$$
H=\gcd_{\mathbb Q[u]}(P_{201},N_c,N_m,N_n)
$$
取首一。因为 $H$ 是首一 $P_{201}\in O[u]$ 的因子，其各系数整于 $O$；这些系数又属于 $\mathbb Q$，而 $O$ 整闭，故
$$
H\in O[u].
$$
首一性保证 $\deg\overline H=\deg H$。

用 $H$ 对任一 $N_i\in O[u]$ 作首一长除，其商属于 $O[u]$，余式为零。因此
$$
\overline H\mid\overline P_{201},\overline N_c,
\overline N_m,\overline N_n.
$$
由真实式 (3.1)，$\overline H\mid G_{14}$，所以
$$
\deg H=\deg\overline H\le14. \tag{4.1}
$$
这没有把模空性直接当作有理空性，也不要求三条 $N_i$ 中每一条都保留其最高 $u$ 次数。

式 (2.1) 保证所有原 $u$ 都是 $H$ 的根。每个 $u$ 的原首一 $Q$ 四次式至多给四个不同 $Q$，所以权对至多 $4\cdot14=56$。已付同点首一 $\lambda$ 六次和三个几何生成元给每个剩余权对至多 $18$ 个 $(\lambda,T,v)$；已付完整 Gram 与两矩唯一恢复只再保留 $\rho^2=1-Q$ 的至多两值。因此另两界为 $56\cdot18=1008$ 与 $2\cdot1008=2016$。

这里的恢复使用同一点真实的 $D\ne0$、$u-\ell\ne0$ 及已付原头条件，没有把某个必要结式的任意根当作已恢复原解。

## 5. 五个块的准确来源

$P_{201}\in O[u]$ 首一且模平方自由，故其 $1009$ 进完成后有已付十三块的实际分解。在其中任一模因子不整除 $G_{14}$ 的块，式 (3.1) 的右边在该块模极大理想后为非零标量，因而是该有限完全整代数的单位。

取式 (3.1) 系数的任意整提升。因 $P_{201}=0$，提升后的同一原 $N_c,N_m,N_n$ 之组合约化为单位，故其提升也为单位。于是这些块中的三个必要原结式不可能同时为零。它们作为整块被排除，不只是排除若干模点。

剩余只能是 $G_{14}$ 的五个因子所标记的实际 $P_{201}$ Hensel 块，总秩 $14$。此处仍不声称这五个局部因子分别具有有理系数；所有 $Q$ 分量和原值方程仍待处理。式 (4.1) 的有理共同次数界与这项完成后的整块解释是两个相容而有区别的结论。

## 6. 唯一新执行

- [新源](../notes/2026-11-28-unit211-Phi-zero-H1-integral-P201-three-original-norm-Bezout-8542.py)。
- [输入与整性提升说明](../notes/2026-11-28-unit211-Phi-zero-H1-integral-P201-three-original-norm-Bezout-8542.md)。
- [小执行回执](../notes/2026-11-28-unit211-Phi-zero-H1-integral-P201-three-original-norm-Bezout-execution-8542.json)。

源 blob 为 `9051857be180f334d1dec546248548e70e6f37b5`，SHA256 为
`b0bf3ee69af6e68bf305f422eddabe9de1f4c5d002092885028ef43ec4d74a64`。

实际 run `46078472089`、job `140771665814`，源提交
`9a27fcfe4b28c35aeb777b80bcdc257a3a7e77b1`。内部退出码 $0$，耗时 $13.368888226$ 秒，峰值 $81184$ KiB。标准输出 $8263$ 字节，SHA256 为
`231a145f1d0b44e386c2e7fac2da8d4afe1864fb675a67f86d766a4692de39cb`。

2026-11-27 22:44:58.935240 UTC 的真实 pull 保持同一提交，两 README blob 无变。没有新的系数载荷、编码分块或重算数据入库。下一未付对象是上述五个完整原值块；本篇没有声明普通 ISP 完成。
