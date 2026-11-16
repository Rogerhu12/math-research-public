# R150：实际五次 Koszul 核259、稳定交换子模60与最少120列原梯度呈示

作者：Astra-ISP-789f / normal_annihilator，与 /root。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

本篇使用已经完成的原五次常数小门，证明原六十列交换子模稳定，并将完整原十七梯度的参数关系模确定为最少120个 $B$ 生成元。加入 Bell 归一方程后，得到至多130列完整参数呈示。这里“最少120”指十生成参数呈示的关系模；原多项式理想仍由原十七梯度生成，不是声称需要120条原梯度。

实际门为：完整 $D_5$ 秩126，原275条线性 Koszul 来源秩259，原259阶子式在合法模127处的行列式为45；全部300个二次低来源右端和全部16条核关系均逐原坐标乘回。本次没有求出 Bell 单位来源，也没有把有限域坐标直接提升成特征零坐标。

## 1. 同一原环、来源与已付入口

固定此前的匹配三次域 $E$ 和合法 place $(127,d-100)$，令

$$
B=E[y_0,\ldots,y_5,w_0,\ldots,w_5],\qquad
S=B[u_0,\ldots,u_4].
$$

权为 $\operatorname{wt}y=1$、$\operatorname{wt}w=\operatorname{wt}u=2$。这是原全部17变量经已付可逆保权坐标运输后的环；未固定任何 mean 或 moment 参数。

原十一条 $H$ 方向方程记为

$$
G_g=q_g(u)+\ell_g(y,w;u)+c_g(y,w),\qquad 0\le g<11,
$$

其中 $q_g$ 是固定 $E$ 系数普通齐次二次式，$\ell_g$ 的 $u$ 次数至多一。保留其全部原梯度来源。其余六条完整梯度记为 $Y_j$ 的原正常形，$1\le j\le6$。

设 $\mathcal F=B^{10}$，原正常单项式行为

$$
\mathbf m=
(1,u_0,\ldots,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4).
\tag{1.1}
$$

轴权为 $(0,2,2,2,2,2,4,4,4,4)$。原五个边界作用 $N_i$ 及真实十一方程来源矩阵 $\Sigma_i$ 满足

$$
\mathbf m(u_iI-N_i)=G\Sigma_i.
\tag{1.2}
$$

本篇复用下列同原结论：

- [原低交换子通过二十条三次来源因子化](R150-appendix-original-characteristic-zero-low-commutators-factor-through-twenty-cubic-sources.md)及[实际两个四维单位的精确低20坐标](R150-appendix-actual-exact-low20-coordinates-from-two-four-dimensional-units.md)：原低20列 $C_s$ 有真实来源 $\sigma_s$，$u$ 次数至多一，线性最高部为原 $z_s$；并有完整 canonical-source 降次唯一性。
- [原四次核95](R150-appendix-original-quartic-syzygies-rank95-and-characteristic-zero-twohundredseventy-presentation.md)：原三次矩阵满35、四次矩阵满70，原 $u_i z_s$ 张满其95维核。
- [实际混合95及原40列选择](R150-appendix-actual-original-koszul-fiftyfive-mixed95-unit-and-forty-source-selection.md)：55条真 $G$-Koszul 零像来源加40条原 $N_iC_s$ 来源消掉全部二次最高来源。
- [原特征零200列呈示](R150-appendix-original-koszul-fiftyfive-quotient-and-characteristic-zero-twohundredten-presentation.md)及[原权九准确维数](R150-appendix-original-weight-nine-dimension-and-weight-ten-koszul-rank-ceiling.md)：完整关系模 $\Gamma_E$ 的权九维数为4552。

以下40列始终取实际 mixed95 的同一原选择。若原100列按 $20\ell+s$ 编号，则

$$
J_{40}=\{0,\ldots,33,\ 40,\ldots,44,\ 60\},\qquad
W_j=N_{\ell(j)}C_{s(j)}.
\tag{1.3}
$$

原低20的 seed 标签为 $10\lfloor s/5\rfloor+1+(s\bmod5)$。没有把此前另一有限域换源选择与(1.3)混同。

## 2. 原五次来源核与全部300右端

令 $R=E[u_0,\ldots,u_4]$，所有单项式均为普通单项式。构造原映射

$$
D_5:E^{11}\otimes R_3\longrightarrow R_5,\qquad
(d_g)\longmapsto\sum_gq_gd_g.
$$

完整尺寸是

$$
\dim R_2=15,\quad \dim R_3=35,\quad \dim R_5=126,
\qquad D_5:E^{385}\longrightarrow E^{126}.
$$

已付原三次单位给 $qR_1=R_3$。乘遍 $R_2$ 得 $qR_3=R_5$，因此在原特征零域中

$$
\operatorname{rank}_E D_5=126,\qquad \dim_E\ker D_5=259.
\tag{2.1}
$$

完整原来源矩阵为

$$
K_5=
[\,u_\ell(q_a e_b-q_b e_a)\,]_
 {0\le\ell<5,\ 0\le a<b<11}
 \in E^{385\times275}.
\tag{2.2}
$$

完整目标矩阵保留所有十五个二次乘子：

$$
H_5=[\,m z_s\,]_
 {m\in\operatorname{Mon}_2(u),\ 0\le s<20}
 \in E^{385\times300}.
\tag{2.3}
$$

原多项式交换性及已付 $\sum_gq_gz_{g,s}=0$ 分别给出

$$
D_5K_5=0,\qquad D_5H_5=0
\tag{2.4}
$$

的原 $E$ 恒等式。后文的特征零结论使用这些原身份；不是从模127零乘积推出特征零零乘积。

## 3. 实际原单位、全部行列及完整门

实际 run 为 **43924670391**，job 为 **133500854331**。完整日志确认四个数学步骤全部退出0。

五次步骤实际得到

$$
\operatorname{rank}_{127}D_5=126,\qquad
\operatorname{rank}_{127}K_5=259,\qquad
\det\overline{(K_5)_{I,J}}=45\ne0.
\tag{3.1}
$$

这里45是实际原子式的模127剩余，不是原 $E$ 行列式值。

原385行按 $(g,m)$ 排列，其中 $g$ 先行、$m$ 遍全部35个普通三次单项式；单项式按非降变量指标组合排序。原275列按 $(\ell,a,b)$ 排列，$\ell$ 先行，随后 $a<b$ 字典序。实际所选原列恰为

$$
J=\{0,1,\ldots,258\}.
$$

实际原259行的紧凑规则为以下区间的并，所有编号从0开始：

~~~text
0–139, 141–154, 156–164, 166–170, 172–173, 175–233,
246–248, 250–258, 261–262, 264, 281–282, 285–291,
296, 316, 320–323
~~~

全部16个自由列为259至274。源码以其自由坐标为单位矩阵构造完整关系，并核全385行；它们没有被抽样或删去。

实际硬门如下：

| 完整原门 | 坐标数 | 实际结果 |
|---|---:|---|
| $D_5K_5=0$ | 34650 | 全真 |
| $D_5H_5=0$，全部300右端 | 37800 | 全真 |
| 原259单位的两侧逆 | 134162 | 全真 |
| 原选259列表示全部275列 | 105875 | 全真 |
| 原选259列表示全部300右端 | 115500 | 全真 |
| 全部16条原关系乘回 | 6160 | 全真 |
| 所选259列坐标为单位矩阵 | 67081 | 全真 |

因此 $\ker D_5/\operatorname{im}K_5$ 的维数为0，而 $\ker K_5$ 的维数为16。这是两个不同的核，不得将0与16混写。

原系数在此前同一 place 可约化，(3.1)认证同一原 $E$ 子式非零。结合(2.1)、(2.4)，严格得到

$$
\boxed{\operatorname{im}_E K_5=\ker_E D_5.}
\tag{3.2}
$$

需要的 $E$ 系数可用这个原子式的伴随公式定义。实际保存的场坐标只是场证书，本篇没有把这些剩余系数直接当作 $E$ 坐标。

## 4. 二次低交换子作用的完整来源降次

对任一具有真来源 $\mathbf m v=G\sigma(v)$ 的十向量，(1.2)给出

$$
\sigma(N_i v)=u_i\sigma(v)-\Sigma_i v.
\tag{4.1}
$$

所以每个有序 $N_pN_qC_s$ 的原来源 $u$ 次数至多三，三次最高部是 $u_pu_qz_s$。其原像仍为十个正常单项式的 $B$ 组合，$u$ 次数至多二；故该最高部确属于 $B\otimes_E\ker D_5$。

由(3.2)用同原 $K_5$ 展开最高部，并减去同系数的真正完整来源

$$
u_\ell(G_a e_b-G_b e_a).
\tag{4.2}
$$

(4.2)的原像恒为零，而最高部恰是(2.2)相应列。因此减后来源次数至多二，原十向量保持不变。

再按实际 mixed95 分解其二次最高部：减去原(1.3)四十条 $W_j$ 的真实来源及真正 $G_a e_b-G_b e_a$ 零像来源。剩余来源次数至多一，像仍是十正常形，故由已付 canonical-source 唯一性归入 $B\langle C_{20}\rangle$。

记

$$
\mathcal C=
B\langle C_0,\ldots,C_{19},W_j\ (j\in J_{40})\rangle.
$$

得到全部有序作用的原来源包含：

$$
\boxed{N_pN_qC_s\in\mathcal C
\quad(0\le p,q<5,\ 0\le s<20).}
\tag{4.3}
$$

程序核全部300个普通对称最高部；两个算子次序虽有同一最高部，但(4.1)至(4.3)分别适用于每个有序的完整来源。没有预先假定五个 $N_i$ 在自由十轴上交换。

全部降次仅用固定 $E$ 常数单位；不倒 $y,w$ 参数，也不丢 mean 或 moment 参数的例外集。

## 5. 六十列交换子模稳定，且给完整十一方程商

此前 mixed95 已给全部 $N_iC_s\in\mathcal C$。对每条所选 $W_j=N_{\ell(j)}C_{s(j)}$，(4.3)又给 $N_iW_j\in\mathcal C$。因 $N_i$ 对 $B$ 线性，

$$
\boxed{N_i\mathcal C\subset\mathcal C\qquad(0\le i<5).}
\tag{5.1}
$$

原全部低、高交换子都属于 $\mathcal C$，因此 $N_i$ 在 $\mathcal F/\mathcal C$ 上交换。原十一二次方程的字面 $e_0$ 关系和九条保留单项式路径给出

$$
\boxed{\mathcal F/\mathcal C
\simeq B[u]/(G_0,\ldots,G_{10}).}
\tag{5.2}
$$

证明两方向都保留原来源。由 $\mathbf m$ 定义正向映射，因为 $\mathcal C$ 每列都有真 $G$ 来源。反向用 $1\mapsto e_0$ 和商上可交换的 $N_i$ 定义，原 $G_g(N)e_0=0$ 保证因子化。字面路径使两复合分别固定十轴和循环元，故互逆。

这里没有断言 $\mathcal F/\mathcal C$ 对 $B$ 自由，也没有从十生成误推稳定性；稳定性先由完整源降次(4.3)证明。

## 6. 原十七梯度的120列完整呈示与 Bell 的130列上界

(1.1)的十个单项式生成(5.2)的整个商作为 $B$ 模。因此其中六条 mean 方程所生成的理想，只需十个字面词作用于每条 $Y_j$，共60列。

取固定顺序的十个词

$$
\mathcal W=\{1,N_0,\ldots,N_4,N_1N_4,N_2N_3,N_2N_4,N_3N_4\}.
$$

原完整关系模为

$$
\boxed{
\Gamma_E=
\mathcal C+
B\langle W Y_j:W\in\mathcal W,\ 1\le j\le6\rangle.
}
\tag{6.1}
$$

每个右侧列都保原十一或原十七梯度来源；反包含由(5.2)中 mean 理想的全部十单项式倍给出。因此(6.1)是完整原关系模等式，非受限候选来源空间。

相应完整序列为

$$
B^{120}_{\mathrm{shifted}}\longrightarrow
\mathcal F\longrightarrow S/J_{17}\longrightarrow0.
\tag{6.2}
$$

五组原生成权为

$$
5^6,\quad6^{20},\quad7^{30},\quad8^{40},\quad9^{24}.
\tag{6.3}
$$

原 Bell 在这些坐标中为 $b=y\cdot w$。再加十条原 $(b-1)e_a$，得到

$$
\mathcal F/\bigl(\Gamma_E+(b-1)\mathcal F\bigr)
\simeq S/(J_{17},b-1),
$$

故有至多130列完整 Bell 参数呈示。这里尚未判断该商是否为零，也不声称130最少。

## 7. 最少性：120与60是原 $B$ 模的准确生成元数

此处使用新已付的[原权九准确维数](R150-appendix-original-weight-nine-dimension-and-weight-ten-koszul-rank-ceiling.md)，而非额外运行。

先钉住集合一致性：本篇的120列恰是原特征零200列构造中全部权不超过9的列；低20、(1.3)实际40及同一原六 mean、十词顺序均未改变。原200构造还允许80条权10二字低来源；本篇证明它们可降入这120列。此前 finite-field 200 的另一换源集合不用于这个最少性论证。

原200呈示在权九的全部单项式来源数为

$$
6\cdot273+20\cdot92+30\cdot27+40\cdot6+24=4552.
$$

它张满完整 $(\Gamma_E)_9$，后者已证维数4552，所以这个权九来源映射单射。较低来源权 $d\le9$ 的非零齐次关系同乘 $y_0^{9-d}$，在自由来源模中仍非零，便会违反权九单射。因此本篇120列不存在来源权不超过9的非零关系。

令 $B_+=(y_0,\ldots,y_5,w_0,\ldots,w_5)$。120列在 $\Gamma_E/B_+\Gamma_E$ 的像生成该 $E$ 空间。若存在非零常系数关系，按总权拆成齐次部分，取某个非零权 $d\le9$ 部分。把其属于 $B_+\Gamma_E$ 的表达式取齐次权 $d$，所有正权系数只能乘更低权生成列。移项后得到来源权 $d\le9$ 的非零关系；其中原权 $d$ 生成列仍有非零常系数，不能被低权项抵消。这与上一段单射矛盾。

所以

$$
\boxed{\dim_E\Gamma_E/B_+\Gamma_E=120.}
\tag{7.1}
$$

(6.1)已给120个生成元；任何 $B$ 生成集的像必须张满(7.1)，故原参数关系模的最少 $B$ 生成元数准确为120。该结论也适用于不预设齐次的生成集。

同理，$\mathcal C$ 的60列是这个同一120集合的子集，权为 $6^{20},8^{40}$。任何它们模 $B_+\mathcal C$ 的非零常系数关系都会给权至多8的原来源关系，故

$$
\boxed{\dim_E\mathcal C/B_+\mathcal C=60.}
\tag{7.2}
$$

因此 $\mathcal C$ 的最少 $B$ 生成元数准确为60。这里的60与120均不代表 $B$ 秩，也不代表自由性。

完整权十在新120列中的来源数为13728；结合已付 $\dim_E\Gamma_{E,10}\le13697$，新呈示在权十仍至少有31维来源关系。未声称恰31，亦未算出这些关系坐标。原13808列的完整权十任务仍有自身明确来源范围，本篇不替它预填目标结果。

## 8. 四步执行身份与原字节范围

五次步骤实际执行源码提交为

~~~text
3870ce0fc8856b0f8a61abd1d9e4009491a6715e
~~~

实际数学计时为0.5167087129999999秒，observer计时1.0182344799999896秒，外层1.2168194089999957秒，数学峰值RSS47440 KiB。没有将外层安装或恢复时间混作新矩阵耗时。

四步全部小raw在完成日志中逐字重构并核完整SHA：

| 步骤 | raw字节数 | 完整raw SHA256 |
|---|---:|---|
| 原116模型重建 | 30919 | 0cc1c085f3d154733ca39d8ad70ac996f7535f196aabef83a46259e3858b1360 |
| 原high95重建 | 8430 | 3573e27fc32a541752d1b9b637eb593d5a3dfaa80f2cd70c184db0acaeb31916 |
| 原mixed95重建 | 9336 | c88c84117c852f8b81bcf3da1f838b46d8e11024a3e8e76b039c3a65ff3d47fb |
| 本次quintic259 | 8827 | c5298003adaa92487b53a2dac9b4f5d430f18ea035674b7c459daaaba8e88eba |

模型仍是 Python3.12.14 / python-flint0.9.0 的原完整118相位，模型manifest仍为30466字节、SHA 9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2。两个high95相位、一个mixed95相位与旧paid物理及逻辑字节全部匹配；quintic consumer 在本次新job实际重新读并核两个父manifest和全部父相位。没有假设上一个已关闭job的TMP仍存在。

新binding为

~~~text
c01cdd8fe8f2613e559aad696115d0c64bd2286af592c4ce8efab7512c5a977c
~~~

新两个完整相位的身份为：

| 相位 | stored字节数／SHA256 | logical字节数／SHA256 |
|---|---|---|
| whole-original-quintic259-input.json.gz | 31593 / d568e2f1c69665cde146254c856359a9fd2618dd3046b8a9c06eeece38314151 | 585248 / a20789bd216f27f64d5a50ba6d4d9dbe0c7b7b8082048b5068daa0fdec28271e |
| complete-original-quintic259-unit.json.gz | 210163 / c61c8ca5eea4cc3161d59f2e48272f3f57e846068dbe4203f833fe125c775efe | 620647 / 43b4093e9a0f33065ca58254972c06c46c41bd3864b4fe5b3925a0d031e18a06 |

完成日志为111428字节，SHA f4dee885fa1a3d6e1a91b8386be8c7a8439cb8df6b5ed40494635fe6c5b4a9c3。由真实相位描述符和原writer规则重构的manifest为896字节，SHA c23d40650d8291252c6de50b3e96e852066dd164a153a88c1fa4118838d7a39f；这个末项是重构身份，不冒称job关闭后独立重开了该物理文件。

## 9. 可复现源码及独立日志审计范围

| 文件 | Git blob | 字节数 | SHA256 |
|---|---|---:|---|
| 原quintic源码 | 17dc94b23638b15672461fa47206688caad3374f | 17017 | 5242360ddf86729c271ea55559c5a84870b7fb92ef73cc653f0cf6f64165d48c |
| 冻结inputs | de2b7b0c5fb0e873b116b108182b97f0e750ad4e | 12321 | 8b320e59d2154adb051d22105db38637afd948931c5842c6ac38186ebb80b7cb |
| 冻结interface | 828898b83b130004fd1e8a854f6008f96c53cb00 | 9961 | a64c5e237dccbd37ee8d45ec21231ff922bc9c1dfacc768e5dbf503fd67ebc76 |
| 独立完成日志reader | 5bbee369c50360c4d778386b92cad4eee6d2f776 | 17356 | 1df5983d758813ce1b4bde066b6cf0b12e56f4d957a68f1478792ec87943443a |

准确路径为：

~~~text
notes/2026-11-16-r150-original-quintic-koszul-span259-unit127-789f.py
notes/2026-11-16-r150-original-quintic-koszul-span259-unit-inputs-789f.json
notes/2026-11-16-r150-original-quintic-koszul-span259-unit-interface-789f.md
notes/2026-11-16-r150-original-quintic259-completed-log-audit-789f.js
~~~

冻结reader已在这份实际完成日志上运行通过；/root 与 normal_annihilator 分别执行并得到同一结果。它独立重建385个来源、275条Koszul与300个目标的字典、semantic/binding、所有原标签和完整raw字节，并核实际生产者全部产品门。它没有重复矩阵算术，也没有独立读回job关闭后的大相位数组；算术事实来自冻结生产者本次执行的全部原乘回。

全部数学数组、原逆、全坐标与核仅留临时目录；仓库保存源码、参数、证明、执行身份及SHA。本篇付清原 $E$ 的稳定60关系模及最少120列梯度呈示，仍不据此宣称 Bell 归一理想为空或得到新的 Bell 自然幂来源。
