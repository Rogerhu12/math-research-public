# R132：完整 pure 导数成本已装配，真实尾商的新维数上界为七

日期：2026-11-14。**公开实际已完成，本文给出准确结论及纸面提升。** 本次补入此前尚未支付的全部原 $L^{[2]},L^{[4]}$，并保留 R124 的整个矩阵诱导补项。分部积分前的几何系数商秩是 24、偶总次数部分是 13；这两个数不是实际新成本维数。结合已经证明的 R85/R88、R116 与 R130，实际 pure $m=8$ 成本模响应的商满足更强的上界 **7**，其偶投影满足上界 **5**。只有 profile 权 $-1,0,1$ 还可能贡献新商，其齐次投影秩分别至多 $1,5,1$。实际准确商维数仍由后继 R129 分部积分消费确定。

## 1. 真实对象与完整因子

沿用 [R109](R109-local-density-of-the-complete-fourth-quotient.md) 的同右锚 canonical 成本和 [R124](R124-zero-matrix-static-tail-payment-and-remaining-derivative-costs.md) 的完整零矩规范化。令

$$
\mathcal T=\Pi_8((\mathcal R_8)_{-4}),\qquad
\Pi_8:q=(c-\xi)^8,\quad r=c-\xi.
$$

[R116](R116-full-m8-tail-response-rank-and-finite-query-control.md) 已给 $\dim\mathcal T=31$，偶总次数响应像维数为 15。所有原函数使用同一右锚 $c$，保持原 $I_c=-J$ 符号。这里 $\Pi_8$ 是 universal profile 算子的幂尾测试，不宣称这个单一尾测试忠实表示完整两个相位算子。

本轮完整原式是

$$
\begin{aligned}
L^{[2]}&=v^{[2]}-\mathcal B_{m^{[0]}}N^{[2]}
-\mathcal B_{m^{[2]}}N^{[0]},\\
L^{[4]}&=v^{[4]}-\mathcal B_{m^{[2]}}N^{[2]},\\
\widetilde L^{[2]}&=L^{[2]}+\Delta L^{[2]},\qquad
\Delta L^{[2]}=-\sum_i a_i(m^{[2]})F_i.
\end{aligned}
\tag{1}
$$

$N=P_{\rm acc}+P_h+F_*$ 使用实际未模 $W$ 的原代表；特别 $N^{[2]}$ 全部保留，不假设它属于 $W$。原 $N^{[0]}$ 与旧静态代表的差逐点在 $W$ 中，故只改变 $\mathcal R_8$ 响应，不改变本商。八矩坐标、固定参考值 $F_i$ 及完整 18 个诱导补项均使用 R124 已发来源。

完整因子来自 [公开原式导出](../notes/complete-original-derivative-factor-export-actual-20261114.md)。其 3974 个原根逐个核对原 SHA 后，只评价本轮新的 pure $-4$ 根；完整 mixed 因子保留在源数据中，未在本轮评价。

## 2. 新 actual 与完整 packet 身份

公开 run 为 [43652134080](https://github.com/Rogerhu12/math-research-public/actions/runs/43652134080)，source 为 `6e2f99ceda8f43e0cf5ade6ec3bbaebd1ea7f73b`，lane `derivative_m8_tail_quotient`。冻结消费器 [literature_derivative_m8_tail_quotient.py](../scripts/literature_derivative_m8_tail_quotient.py) 为 29555 bytes，SHA-256 `5c7bb457eec0b68b31b2e7250cf89eb7901660ffac289ccf7854a8c47c198705`。

对每一个完整几何系数，实际保存三元 packet $(P,A,R)$，准确核验

$$
P(c,r)=\sum_{j\in J_{31}}A_jP_j(c,r)+R(c,r).
\tag{2}
$$

$P_j$ 为 R116 的原 31 基列。$R$ 是保全部单项式的准确规范余项，不剪裁到已知响应的支撑。所有新 packet 的完整多项式差为零。

实际工作量为：

- 1901 个新 $v^{[2/4]}_{-4}$ 原根的 pure 评价；
- 885 个不同原 $N$ root/operator 对的准确响应；
- 全部 R124 诱导补项读取并相加；
- 31 个旧原响应基列的一次因式分解，仅供新目标归约。

原 $N$ 槽序保持外槽和内槽原定义。$\mathcal B$ 使用完整 pure 响应的 $1/16$ 相位因子；原 $v_{-4}$ 已包含完整相位因子，没有再除一次。旧 $W$ 响应公式重算数为零；本次所需的 885 个对均没有与旧列同 hash，因此没有冒称旧列复用成功。

## 3. 分部积分前的准确系数商

几何键完整保留

$$
(h,k,\omega,h_s,k_s,h_{ss},k_{ss},\log h,h_{sss},k_{sss}).
$$

下表的秩是这些完整几何单项式系数在多项式响应商中的秩。未分 profile 权和先按真实 profile 权分块的秩在本次恰相同。

| 完整密度 | 非零几何 packet | 非零余项 packet | 系数商秩 | 偶总次数商秩 |
|---|---:|---:|---:|---:|
| 原 $L^{[2]}$ | 828 | 583 | **15** | **9** |
| $\widetilde L^{[2]}=L^{[2]}+\Delta L^{[2]}$ | 828 | 583 | **14** | **8** |
| 原 $L^{[4]}$ | 1234 | 1234 | **20** | **10** |
| 完整剩余 $\widetilde L^{[2]}+L^{[4]}$ | 2062 | 1817 | **24** | **13** |

两组完整剩余系数空间并非直和：其商交维数是 $14+20-24=10$，偶投影的交维数是 $8+10-13=5$。这同样只是在分部积分前的系数空间中陈述。

真实 profile 权 $w$ 对应单项总次数 $a+b=32+w$。完整分块为：

| $w$ | 原 $L^{[2]}$ | $\widetilde L^{[2]}$ | 原 $L^{[4]}$ | 完整剩余 |
|---:|---:|---:|---:|---:|
| $-9$ | 0 | 0 | 1 | 1 |
| $-8$ | 1 | 1 | 2 | 2 |
| $-7$ | 1 | 1 | 2 | 2 |
| $-6$ | 1 | 1 | 2 | 2 |
| $-5$ | 1 | 1 | 2 | 2 |
| $-4$ | 1 | 1 | 2 | 2 |
| $-3$ | 1 | 1 | 2 | 2 |
| $-2$ | 1 | 1 | 2 | 2 |
| $-1$ | 2 | 2 | 3 | 3 |
| $0$ | 5 | 4 | 2 | 5 |
| $1$ | 1 | 1 | 0 | 1 |
| 合计 | 15 | 14 | 20 | 24 |

完整原 packet 的所有齐次分量亦已保存，表不是只对某个截断的余项查询。新增的实际原多项式总次数均不超过 33；其中分部积分前可有 $r^{23},r^{24}$，不能据本表将其直接认作周期项。

## 4. 首个真实提升：完整成本商至多二十四维

R124 已证明全部归一化静态 pure 系数属于 $\mathcal T$。由 [R130](R130-true-fourth-span-from-horizontal-normal-coefficients.md)，真实成本空间是已有响应与完整水平正规系数值的 span。

[R129](R129-horizontal-geometry-IBP-for-complete-fourth-costs.md) 的全部操作只对几何状态系数作真实链式微分和有理线性组合。它不创造新的 profile 系数向量。因此归一后的真实 pure 成本商是第 3 节完整系数商的子空间。这严格给

$$
\dim\bigl(\Pi_8(\mathcal U_4)/\mathcal T\bigr)\le24,
\tag{3}
$$

偶投影相应至多 13。式 (3) 是上界，不是把 24 个形式原系数赋予独立真实控制。

## 5. 结合真正尾端势与逐权实际，商上界降为七与五

这里必须从完整成本推出支撑限制，而不能把已知响应的支撑强加给 $\mathcal U_4$。

第一步，第 3 节对完整原剩余密度的评价给总次数至多 33。R124 的归一静态 pure 项在 $\mathcal T$ 中，同样至多 33。R129 几何微分不改变 $c,r$ 次数，再用 R130 的真实 span 等式，得

$$
\deg_{c,r}\Pi_8 V\le33
\quad\text{对全部 }V\in\mathcal U_4.
\tag{4}
$$

第二步，$\mathcal U_4$ 由同 scalar germ、frame I、真实 $M=T=0$ 路径的成本张成。R85 的原式给 pure 尾的最低候选阶 $4m-9$，并证明它是准确低阶 history 端势；R88 对下一阶 $4m-8$ 给出同样的端势结论。取 $m=8$，常值 germs 和真实 $M=0$ 使 $r^{23}$、$r^{24}$ 的端差为零，更低项原本不存在。因此

$$
[c^a r^b]\Pi_8 V=0\quad(b<25)
\quad\text{对全部 }V\in\mathcal U_4.
\tag{5}
$$

这两个结论按 R116 的同右锚尾测试及连续延拓范围使用；没有把内部 histories 独立赋值，也没有从局部非零密度跳到非零 period。

合并 (4)–(5)，真实成本的 pure 投影落在

$$
\mathcal H=\operatorname{span}\{c^a r^b:a\ge0,\ b\ge25,\ a+b\le33\}.
\tag{6}
$$

其维数为

$$
\dim\mathcal H=1+2+\cdots+9=45.
$$

因为 $\mathcal T\subseteq\Pi_8(\mathcal U_4)$ 且 $\dim\mathcal T=31$，先得到中间上界：

$$
\boxed{0\le\dim\bigl(\Pi_8(\mathcal U_4)/\mathcal T\bigr)\le14.}
\tag{7}
$$

再保留第 3 节已经准确计算的 profile 分权信息，可以继续加强。R116 的响应像在总次数 $25,26,\ldots,30$ 上已经分别充满全部 $r\ge25$ 的单项式空间，维数依次为 $1,2,\ldots,6$；在次数 $31,32,33$ 上，准确响应秩分别为 $6,3,1$。

R129 的几何微分不改变 profile 权。故任一真实正规系数在权 $w$ 的投影，一方面落在本轮完整 raw 系数的相应权商中，另一方面由 (4)–(5) 落在 (6) 的同次齐次片中。对这两个包含同时取秩上界，得到：

| profile 权 $w$ | 真正可能的总次数 | 本轮 raw 商上界 | (6) 的该次维数减已知响应秩 | 实际新商的齐次投影上界 |
|---:|---:|---:|---:|---:|
| $w\le-8$ | 至多 24 | 不需要 | 0 | **0** |
| $-7\le w\le-2$ | 25 至 30 | 不需要 | 0 | **0** |
| $-1$ | 31 | 3 | $7-6=1$ | **1** |
| $0$ | 32 | 5 | $8-3=5$ | **5** |
| $1$ | 33 | 1 | $9-1=8$ | **1** |
| $w\ge2$ | 至少 34 | 0 | 不需要 | **0** |

不同总次数的多项式空间直接相加，任何子空间的维数至多其各齐次投影维数之和。因此不必额外假定原几何系数已经逐权独立，即严格得到

$$
\boxed{0\le\dim\bigl(\Pi_8(\mathcal U_4)/\mathcal T\bigr)
\le1+5+1=7.}
\tag{8}
$$

这保留了 (7) 作为仅由完整次数/尾支撑所得的中间推论；从 14 到 7 的加强额外使用了本次完整权一 raw 商只有一维的实际结果，不能从旧响应支撑单独推出。

偶总次数的 (6) 只有次数 $26,28,30,32$，维数为 $2+4+6+8=20$。已有偶响应像维数 15；在上表中也只有 $w=0$ 留下新偶商。所以

$$
\boxed{0\le\dim\bigl(\Pi_{\rm even}\Pi_8(\mathcal U_4)
/\Pi_{\rm even}\mathcal T\bigr)\le5.}
\tag{9}
$$

R106 的四块 pure 作用只是该偶投影乘一个非零常数，故维数上界不变。它并不因此消去这些可能的剩余方向，也不自动给出同一有限真实设计的成本支付。

## 6. 完整输出与实际资源

目录为 `notes/actions-43652134080-1-derivative_m8_tail_quotient`。

| 文件 | bytes | SHA-256 |
|---|---:|---|
| [小主报告](../notes/actions-43652134080-1-derivative_m8_tail_quotient/derivative-m8-tail.json) | 14890 | `20157415f95817dabfda88ca3b8914dfdbec058ae8c00d89a6c0a6ac8a9fe585` |
| [人工检查](../notes/actions-43652134080-1-derivative_m8_tail_quotient/derivative-m8-tail-development.json) | 5174 | `a88c0152fd6587923e0afdaa5c1906d7bc4d234e8d5f1670d027e9c356bef2c8` |
| [完整证书](../notes/actions-43652134080-1-derivative_m8_tail_quotient/derivative-m8-tail-certificate.json.gz) | 1089774 | `68a764d03fc6f7d88a69dba624a92fa616d86b29b545777296aa7ad991b3c48d` |
| [发布回执](../notes/actions-43652134080-1-derivative_m8_tail_quotient/receipt.json) | 33607 | `192a945b561d3a37ef1a454de91292df81de90bf60e4877565f6d0bd9362ffd9` |

证书完整原文 9189672 bytes，SHA-256 `ecdc5297777ab6ae30d9ff6ca35e1e9a21b633e0e60c91da42908d5e1c78a423`。其中保留全部 1901 个新原 $v$ 多项式、885 个完整原 $N$ 响应多项式、四组所有 packet、准确依赖和原式身份，后续无需重算 profile。

公开五项人工检查全部通过，耗时 0.001098086 秒。研究实际耗时 **14.667641640 秒**，峰值 RSS **315.22265625 MiB**，1000308 次多项式运算、333046 次线性运算；最大中间多项式 55 项。主报告 completion 为 complete。

## 7. 尚未支付的准确门

下一消费仅对已发 packet 作 R129 的真实水平分部积分，保全部 $P,A,R$ 三元恒等式与端点势；然后 R130 才将所得准确正规系数商秩解释为真实成本投影商维数。

式 (5) 还给一个非阻断的语义检查：正确完整正规系数的 $r<25$ 行应为零。消费器应直接报告它们是否为零以及实际支撑；若不符则保留全部原输出并定位差异，不能按先验删掉这些项。

本稿不宣布新实际控制方向的维数下界，不判定成本符号或正锥，不证明完整 mixed 商、第四 ruling、有限等距族、闭嵌入、reach 或课题要求的宏观幅度。
