# R151：J 的一般 pure 原式恒等、九维响应像与新的 pure 零代表

日期：2026-11-15。**已证明。** 本稿消费公开 Actions 的唯一新 pure 成员问题；没有本地研究归约、profile 评价、幂尾代入或新响应编译。

准确结论是：R136 的新完整成本方向 J，其一般 pure 分量属于真实响应像，且有下面的九项有理原式表示；真权 $-2$ 的一般 pure 响应像恰为九维。结合 R138，G 轨道和 J 轨道的完整新商都能取 pure 恒零代表。它们的完整 mixed 商仍可非零，本文不授 J 的实际有符号控制。

## 1. 目标、基列与准确原式

保持全部 canonical 相位因子、同一个右 collar 和共同右原函数锚。记

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad
\pi V=V_{-4}.
$$

这里 $\pi$ 是任意光滑输入上的一般 pure 投影，不是 $m=8$ 幂尾代入。目标为 [R136](R136-acceleration-coefficient-beyond-response-and-G-orbit.md) 的完整真权 $-2$ 系数

$$
J=\operatorname{gr}_{-2}[h^{-4}k^0\omega^0(\log h)^0]\bar A_{hh}\in U.
\tag{1}
$$

相位下标 $-4$ 与仿射权 $-2$ 不同。R136 已证明完整两模式 J 不在 $R+\operatorname{span}\operatorname{Orb}(G)$ 中；本稿保留这一结论。

沿用 R116 的全局列约定

$$
C_{8j+a}=\mathcal B_{P_a}(W_j),\qquad
(P_0,\ldots,P_7)=(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1),
$$

其中 $W_0,\ldots,W_{35}$ 是原已证明完整的第三外槽模板，全部索引从零开始。$C_i$ 是完整两模式响应；下面只投影其 $-4$ 模式，系数不再乘任何额外的 $1/16$ 或 $1/128$。

定义完整响应

$$
\begin{aligned}
K_J={}&-\frac3{16}C_0-\frac3{128}C_{48}-\frac7{64}C_{88}
+\frac1{64}C_{112}-\frac1{64}C_{41}\\
&-\frac18C_{73}-\frac3{64}C_{81}
+\frac3{256}C_{193}+\frac1{512}C_{170}\in R_{-2}.
\end{aligned}
\tag{2}
$$

**定理 1。** 对任意同零右 collar 的光滑复 profile q，有完整函数恒等式

$$
\boxed{J_{-4}(q)=(K_J)_{-4}(q).}
\tag{3}
$$

原列身份和九系数的精确对应为：

| 本次消费位置 | R131 块内原列 | R116 全局列 | 二次 / 第三模板 | 系数 |
|---:|---:|---:|---|---|
| 0 | 0 | 0 | $p_0/W_0$ | $-3/16$ |
| 1 | 1 | 48 | $p_0/W_6$ | $-3/128$ |
| 2 | 2 | 88 | $p_0/W_{11}$ | $-7/64$ |
| 3 | 3 | 112 | $p_0/W_{14}$ | $1/64$ |
| 8 | 8 | 41 | $p_1/W_5$ | $-1/64$ |
| 9 | 9 | 73 | $p_1/W_9$ | $-1/8$ |
| 10 | 10 | 81 | $p_1/W_{10}$ | $-3/64$ |
| 12 | 12 | 193 | $p_1/W_{24}$ | $3/256$ |
| 19 | 19 | 170 | $p_2/W_{21}$ | $1/512$ |

消费位置与块内号在这九个条目上恰相同，但一般不是同一个编号系统；全局号尤其不能与它们互换。完整原根及每个第三模板的 SHA 均在本次主报告和证书中保留。

## 2. 完整原差证明与研究范围

输入 J 来自 R136 已发表的完整五族原式导出，pure 根为 `selected_0000_-4`，也恰为整个状态根 `family_0051_-4`。原项数 80，SHA256

~~~text
2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3
~~~

其完整状态系数本来只有真权 $-2$，本次没有删除其他权来构成 (1)。

响应原根来自 [R131](R131-third-G-translation-separation-and-111-query-control.md) 的完整 50 列真权 $-2$ 导出。旧实际已证明其中 10 条完整两模式依赖，留下真实 40 维基。本次只消费这 40 个原基列的 pure 根；没有重新计算旧 50→40 关系、G³ 目标或旧两模式分离。

新 pure word 消元提出 9 列张成及 31 条新 pure 依赖。**每条新依赖都从对应原根重新形成完整原差，并以单独的同右锚 sound 归约核成零。** 全部 31 条通过，没有未决列被静默删除。准确有理依赖、各原差完整 DAG、SHA 与零证均保存在本次完整证书中；依赖证明列表 SHA256 为

~~~text
bdd01870f261b98a4f63c38789ccbe81b96084e71c25ef0831c3893718536a69
~~~

随后唯一的目标求解给出 (2)。直接从原 J 和九个原响应形成

$$
\Delta_J=J_{-4}-(K_J)_{-4}.
$$

这个原差有 **398 项**，SHA256 为

~~~text
1e12a43e130a8874e83203bbf293dea2e9208786a9299fc3b3aca7123d2b12b0
~~~

单独的原差归约得到零项，零代表 SHA256 为

~~~text
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
~~~

这不是只将若干已经归约的标签相减。所用每一步为真实分部积分、同右锚乘积/word shuffle 及精确有理运算。所有 primitive 具有正 profile 次数，右 collar 上对应 jets 与原函数为零；必要端项由此支付，左端没有重置。normalizer 不完备不影响这种明确归零的正恒等式。于是 (3) 对一般同右 collar 光滑 q 成立。

本次工作范围为：40 个已发 pure 原根的新单模式代表、31 条新 pure 原差和唯一 J 的原差。新增 pure 响应、mixed 响应、forcing/W/N/v4 编译、幂尾代入和 profile 评价均为 **0**。因为 (3) 已证明，预设的条件性原有理分离分支没有运行。

## 3. 一般 pure 响应像的准确维数为九

本次 31 条新原式关系连同 R131 已付的 10 条旧完整关系，给出真实函数上界

$$
\dim\pi(R_{-2})\le9.
\tag{4}
$$

不能仅从 word 代表的秩九推出反向不等式。下界可以直接从已发表的 R131 原有理证书读取，无需任何新评价。

R131 §4 用同一固定实 profile 对

$$
f=t^8(1-t)^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad q=f+ig,\qquad \xi=2+t
$$

得到 40 个原控制列的真实有理评价矩阵 A。其已证明非零的 40 阶控制子式满足

$$
\det A_{\mathcal J}\equiv1476048378\ne0
\pmod{2147483647}.
\tag{5}
$$

这里原有理分母的可逆性、全部原积分和原根已由 R131 支付。[旧主报告](../notes/actions-43653293263-1-g_translation_successor/G-third-translation.json) 的 SHA256 为 `b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3`；[旧完整原值报告](../notes/actions-43653293263-1-g_translation_successor/G-third-translation-complete-report.json.gz) 的压缩 SHA256 为 `ff97938a939c0e69705f1528bcf327800fb491b84a7d633b3f57f2da1f193085`。主报告 `selected_evaluation_labels` 中，控制的前 40 行恰含以下九个 pure 行：

| 原 96 行中的索引 | t | 相位模式 | 分量 |
|---:|---|---:|---|
| 0 | $1/25$ | $-4$ | 实部 |
| 1 | $1/25$ | $-4$ | 虚部 |
| 4 | $2/25$ | $-4$ | 实部 |
| 5 | $2/25$ | $-4$ | 虚部 |
| 8 | $3/25$ | $-4$ | 实部 |
| 9 | $3/25$ | $-4$ | 虚部 |
| 12 | $4/25$ | $-4$ | 实部 |
| 13 | $4/25$ | $-4$ | 虚部 |
| 16 | $1/5$ | $-4$ | 实部 |

剩余控制行均为 $-2$ 模式；第 41 个增广目标行不属于控制子式，不计入这个九行结论。

一个非零 40 阶有理矩阵的任何行子集都线性独立，因此上述九个 pure 行在同一 40 个原列上的行秩为九。这九行只作用于原列的 pure 投影，故

$$
\dim\pi(R_{-2})\ge9.
\tag{6}
$$

R131 的输入最大 jet 为四阶，测试对为零延拓的 $C^7$；有限原函数运算对相应 $C^4$ 数据连续，可用保持共同右 collar 的光滑逼近保留非零子式。这是一般光滑真实函数空间的下界，不将有限值标签冒充 universal 基。

由 (4)、(6)，严格得到

$$
\boxed{\dim\pi(R_{-2})=9.}
\tag{7}
$$

本次保留的九个原 pure 列因此恰为真实基。下界只读取旧已成原子式的行标签与非零事实，没有重新运行该子式或条件性新 profile 分支。

## 4. 精确区分一般 pure 与 m=8 幂尾的两个核

R131 已证明 $\dim R_{-2}=40$。由 (7) 及秩—零化度定理，

$$
\boxed{\dim(R_{-2}\cap\ker\pi)=40-9=31.}
\tag{8}
$$

另一方面，[R116](R116-full-m8-tail-response-rank-and-finite-query-control.md) 的同一 $m=8$ pure 尾映射在真权 $-2$ 的秩为六。将其分解为

$$
R_{-2}\xrightarrow{\pi}\pi(R_{-2})
\xrightarrow{T_8}\Pi_8(R_{-2}),
$$

就得到

$$
\boxed{\dim\ker(T_8|_{\pi(R_{-2})})=9-6=3.}
\tag{9}
$$

因此旧完整尾核的 34 维准确分成：31 维一般 pure 本来恒零的响应，加上在一般 pure 中非零但被该幂尾代入丢失的三维。这解释为何完整 m=8 已付不能自动推出一般 pure 已付。

R143 检查的固定六列差，经过本稿 (3) 后已知属于 $\pi(R_{-2})$，并由原 R133 幂尾身份落在 (9) 的三维真核中。它是否恰为零仍没有由其非零 sound 代表决定；本稿不再重跑这个已经不影响 J 成员状态的旧候选问题。

## 5. J 的整个仿射轨道以及七个已付状态条目

R89/R105 的完整正仿射表示保持 R，且不混合相位模式，所以 $\pi\mathsf P=\mathsf P\pi$。由 (3)，对任意 $H>0,d\in\mathbb R$，

$$
\boxed{\pi(\mathsf P_{H,d}J)=\pi(\mathsf P_{H,d}K_J)\in\pi R.}
\tag{10}
$$

故整个 J 仿射轨道的一般 pure 像都已由响应支付。这里的“支付”是准确函数成员，不是 J 的实际正负成本控制。

[R146](R146-acceleration-family-quotient-covariance-and-eighty-seeds.md) 进一步给模 R 的状态系数输运。令

$$
F_j=[h^{-4}k^0\omega^j(\log h)^0]\bar A_{hh}.
$$

R136 原元数据对此固定 $(h,k)$ 键恰有 $j=0,1,\ldots,6$，对应原根 `family_0051` 至 `family_0057`；没有更高 $\omega$ 幂。这里仅解析已有状态记录，不重新提取或计算这些原式。

R146 于是准确给

$$
\boxed{[F_j]=\frac1{j!}N^j[J]\quad(0\le j\le6),
\qquad N^7[J]=0\quad\text{于 }U/R.}
\tag{11}
$$

由 (10) 及 R 的平移不变性，七个完整状态系数的 pure 像均在 $\pi R$ 中：

$$
\boxed{\pi F_j\in\pi R\quad(0\le j\le6).}
\tag{12}
$$

相应的完整 J 轨道商维数至多七，但不预告每个 $N^j[J]$ 非零或相互独立于已有 G 轨道。特别 $N^7[J]=0$ 是模 R 结论，不是原 DAG 的逐项零身份。

## 6. 新完整商可取 pure 恒零代表，权负二核至少三十三维

定义

$$
H_J=J-K_J\in U_{-2}.
$$

由 (3)，$\pi H_J=0$。由于 $K_J\in R$，H_J 与 J 在 U/R 中有同一个非零类；R136 还保证这个类不在整个 G 轨道商中。于是

$$
\boxed{H_J\in U\cap\ker\pi,
\qquad H_J\notin R+\operatorname{span}\operatorname{Orb}(G).}
\tag{13}
$$

这说明新的完整障碍方向可以完全藏在 canonical 的其余相位分量中。它不自动给该余分量模某个任意扩大 mixed 投影空间的非成员；此处是完整算子子空间中的陈述。

由 R138，$N^3G$ 的 pure 像也属于 $\pi(R_{-2})$。R131 证明 $N^3G\notin R$；R136 证明 J 不在 R 加整个 G 轨道中。故

$$
E=R_{-2}+\operatorname{span}_{\mathbb R}\{N^3G,J\}
$$

是 U 的一个准确 42 维子空间，且 $\pi(E)=\pi(R_{-2})$。由 (7)，

$$
\boxed{\dim E=42,\qquad\dim\pi(E)=9,
\qquad\dim(E\cap\ker\pi)=33.}
\tag{14}
$$

特别，$\dim(U_{-2}\cap\ker\pi)\ge33$。其中新增的两个核类可分别由 R138 的 G 零 pure 代表的三次平移和 (13) 表示；它们在模 R 后独立。

更一般，令

$$
Z_J=R+\operatorname{span}\operatorname{Orb}(G)
+\operatorname{span}\operatorname{Orb}(J).
$$

R138 与 (10) 给 $\pi(Z_J)=\pi(R)$，从而有准确商同构

$$
\boxed{(Z_J\cap\ker\pi)/(R\cap\ker\pi)\simeq Z_J/R.}
\tag{15}
$$

证明是：任何 z 的 pure 像都可由某个 r∈R 匹配，故 z−r 在核中；核映到 Z_J/R 的核恰为 R∩kerπ。式 (15) 不要求已知 J 轨道商的准确维数，也不把 U 宣称为 Z_J。

R120/R122 对 G 轨道已经支付的 lineality 与有限查询控制仍有效。对 J 而言，本稿只给新的准确 pure 表示与真实 span 核方向，不能把 J 自动加进已有的可双向查询控制计数。

## 7. 公开实际身份、资源与完整证书

本次唯一新研究为：

- Run：`43657785023`，attempt 1。
- Source：`c606688a842bd811106ff2844e1161a4f34c159e`。
- Lane：`general_pure_J_membership`。
- [新源](../scripts/literature_general_pure_J_membership.py)：37092 B，SHA256 `1a84590f8b6f0c35a1df5f251a8ffa0e9f4da65ea2cc3bd777e752482ef05bcc`。
- [设计](../notes/general-pure-J-complete-response-membership-design-20261115.md)：13664 B，SHA256 `2120e027d5e2b98c709615d1ce4006b61af21f65f16d50175061aeac690c415d`。
- 完成状态 `complete`；结果 `general_pure_member_identity_proved`。

公开目录为 `notes/actions-43657785023-1-general_pure_J_membership/`。

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43657785023-1-general_pure_J_membership/general-pure-J-membership.json) | 45019 | `98442251ed15b708a70e3fcbbdb2ae6cf76c8c1873aa21345354a5a320a9cfac` |
| [发布回执](../notes/actions-43657785023-1-general_pure_J_membership/receipt.json) | 35841 | `31d6380160437b0098d33d35e4b722c79cd780d351f614a4e48901100a9d0fa4` |
| [新增小人工](../notes/actions-43657785023-1-general_pure_J_membership/general-pure-J-membership-development.json) | 17010 | `44943751a43cf6e5181637818424c7af68cf70c5e1762ef15c32d283826c5ae8` |
| [完整证书 gzip](../notes/actions-43657785023-1-general_pure_J_membership/general-pure-J-membership-certificate.json.gz) | 84283 | `af46437f676716a20051bf3bad5a96235398dcf8a45c179d1395bc1f9d84712e` |

证书原始 456216 B，SHA256
`9859368ec20e0923cc168199a7ecb82eff0beac5fa191f1b6388e67cfd1aa550`。其中有 73 个完整原根：J、40 个消费列、31 条新依赖原差、1 条 J 原差；并保存全部 40 个新 pure word 代表、准确有理系数与原式核零结果。

实际用时 **4.133837064 s**，峰值 RSS **94.234375 MiB**。最高实际输入 jet 为四阶，仅有颜色 q。原差与代表两条归约通道均无 cycle fallback。公开同 job 的八项新增人工接口全部通过，用时 0.004392828 s；这些人工没有载入研究原 DAG，不能代替本次 31+1 条真实原差。

输入仍是 R136 与 R131 两个已公开的原式导出。完整来源/main/receipt、packed/raw 字节及 SHA、648/102 全原根身份、真实 E8×W36 枚举与旧 50→40 证书均由本次 source-bound 主报告保留。本稿未通过 API 读取 gzip 二进制，也未重新运行这些输入生产者。

## 8. 已结束的门与后续范围

J 的一般 pure 成员问题已由 (2)–(3) 完整解决；该权一般 pure 响应像的准确维数为九。R143 的固定六列试验不再作为下一任务，也不需要以幂尾或有限节点重新猜 J。

R146 的其余起始条目、完整速度二次/四次族，以及新 D0 完整成本仍各有未付原式。当前结论没有证明 $\pi U=\pi R$，没有使完整 J 商消失，也没有证明 J 能取任意实际正负成本。完整 fourth period 与 ruling 同时支付、后续阶与收敛、闭嵌入、全时 reach 和宏观弯曲幅度仍须继续推进。
