# R157：D0 的一般 pure 恒等与权负二至少三十四维 pure 核

日期：2026-11-15。**已证明。** 本稿消费唯一公开 Actions 目标：D0 的一般 pure 分量对 R151 已发表九个真基的有理成员门。没有重跑旧40基、31条依赖、完整 mixed 原式或任何 profile 评价。

准确结论是

$$
\boxed{(\mathcal D_0)_{-4}=(K_D)_{-4}\quad\text{对任意同右锚光滑 profile 成立},}
\tag{1}
$$

其中 $K_D\in\mathcal R_{8,-2}$ 为下面的九项准确有理组合。结合 R153 的完整非成员，D0 的新商类可取 pure 恒零代表，且权负二的真实 pure 核至少34维。完整成本符号、lineality 与真实联调下界不因此增加。

## 1. 唯一原目标与九个真实基

记

$$
U=\mathcal U_4,\qquad R=\mathcal R_8,\qquad
\pi V=V_{-4}.
$$

这里 $\pi$ 是任意光滑输入上的一般 pure 投影，不是有限节点或 $m=8$ 幂尾代入。目标 $\mathcal D_0\in U_{-2}$ 是 [R153](R153-D0-original-separation-beyond-response-G-and-J.md) 的完整轴速度四次系数，包含全部未归约 $N_2$ 和真实正规化势；该文已证明

$$
\mathcal D_0\notin
R+\operatorname{span}\operatorname{Orb}(G)+\mathbb RJ.
\tag{2}
$$

相位模式 $-4$ 与仿射权 $-2$ 分开记录。

沿用 [R151](R151-general-pure-J-identity-nine-dimensional-range-and-kernel.md) 的完整响应编号

$$
C_{8j+a}=\mathcal B_{P_a}(W_j),\qquad
(P_0,\ldots,P_7)=(p_0,p_1,p_2,r_0,r_1,s_0,s_1,t_1).
$$

$C_i$ 本身是完整两模式响应。九个已发表 pure 真基和本次系数为：

| 本次索引 | R151 消费原位置 | R131 块内原列 | R116 全局列 | 二次/第三模板 | 系数 |
|---:|---:|---:|---:|---|---|
| 0 | 0 | 0 | 0 | $p_0/W_0$ | $1/16$ |
| 1 | 1 | 1 | 48 | $p_0/W_6$ | $1/64$ |
| 2 | 2 | 2 | 88 | $p_0/W_{11}$ | $5/96$ |
| 3 | 3 | 3 | 112 | $p_0/W_{14}$ | $1/96$ |
| 4 | 8 | 8 | 41 | $p_1/W_5$ | $1/48$ |
| 5 | 9 | 9 | 73 | $p_1/W_9$ | $5/48$ |
| 6 | 10 | 10 | 81 | $p_1/W_{10}$ | $1/16$ |
| 7 | 12 | 12 | 193 | $p_1/W_{24}$ | $1/384$ |
| 8 | 19 | 19 | 170 | $p_2/W_{21}$ | $1/768$ |

定义完整响应

$$
\begin{aligned}
K_D={}&
\frac1{16}C_0+\frac1{64}C_{48}+\frac5{96}C_{88}
+\frac1{96}C_{112}+\frac1{48}C_{41}\\
&+\frac5{48}C_{73}+\frac1{16}C_{81}
+\frac1{384}C_{193}+\frac1{768}C_{170}.
\end{aligned}
\tag{3}
$$

全部相位归一化已在 $C_i$ 原根中，(3) 不再外乘 $1/16$、$1/128$ 等因子。这些系数是在 $\mathbb Q$ 上新求得，不来自 R153 的模整数 lifts。

## 2. 从已存代表提出关系，再从原式独立证明

D0 的 pure 原根来自公开 run43657526246 已完成的完整轴导出。它有100个原项，SHA256 为

~~~text
1236f94a788454870d655dda499714eacccfee730cba582e22fb2c0b4d892f7f
~~~

R151 的公开证书同时保存九个真基的原式及其准确 word 代表。本次只选对应九条，分别核原根 hash、原位置/全局号、代表摘要与来源；其余31个已依赖的原列和31条依赖原差没有重新归约。

R151 的九维**真实** span 上下界来自该文已发布的原式依赖与原有理子式，不是本次再次把代表秩当真实函数秩。

本次只对新的 D0 pure 原根作同右锚 sound 归约，得到36项代表；在九个已存代表上作有理消元提出 (3)。随后用一个独立的新 normalizer，从原 D0 与原九列重新形成

$$
\Delta_D=(\mathcal D_0)_{-4}-(K_D)_{-4}.
\tag{4}
$$

这个完整原差有 **402项**，SHA256 为

~~~text
faf4f97b6f649405443e510ec152ed8e15c7399372c05e07faaf88dbacd41cdd
~~~

原差独立归约得到零项，零代表 SHA256 为

~~~text
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945
~~~

新目标和原差两条归约均没有 cycle fallback。所有运算使用普通准确有理系数；没有原多项式取模、profile 测点、幂尾代入或独立指定原函数值。

每一步使用已证明 sound 的同右锚分部积分、word shuffle 与精确有理运算。所有 primitive 具有正 profile 次数，零右 collar 使对应边界项准确消失；左尾始终保留，未重新重置。所用输入最高 jet 为四阶。因而 (4) 的零证明给任意同零右 collar 光滑复 profile 的真实函数恒等式 (1)。

normalizer 不完备不会削弱这个明确的正身份；本稿没有使用“非零代表所以非成员”的逆向断言。

## 3. 一个新的 complete pure-zero 成本类

令

$$
H_D=\mathcal D_0-K_D.
\tag{5}
$$

由 (1)、(3)，

$$
H_D\in U_{-2},\qquad \pi H_D=0,\qquad
[H_D]=[\mathcal D_0]\text{ 于 }U/R.
\tag{6}
$$

若 $H_D\in R+\operatorname{span}\operatorname{Orb}(G)+\mathbb RJ$，加回 $K_D\in R$ 就与 (2) 矛盾。因此

$$
\boxed{H_D\notin
R+\operatorname{span}\operatorname{Orb}(G)+\mathbb RJ.}
\tag{7}
$$

这不是说其单独 mixed 分量不属于某个任意扩大的 mixed 投影空间；(7) 指完整算子子空间中的非成员。pure 精确消去与完整新商独立性可以同时成立。

[R138](R138-general-pure-G-identity-and-affine-orbit-kernel.md) 已给 G 的一般 pure 响应表示，R151 已给 J 的一般 pure 响应表示。记该文的完整 $K_J\in R_{-2}$，则

$$
H_J=J-K_J,\qquad \pi H_J=0.
$$

在同一权上，$N^3G$ 也可减去其已付响应而取 pure 零代表。R131、R136、R153 依次保证这三个新类在模 $R_{-2}$ 后独立。

## 4. 权负二的 pure 核准确增至三十四维

定义已经完整证明独立的子空间

$$
E_D=R_{-2}+\operatorname{span}_{\mathbb R}
      \{N^3G,J,\mathcal D_0\}.
\tag{8}
$$

R153 给 $\dim E_D=43$。R151 给 $\dim\pi(R_{-2})=9$。由 R138、R151 和 (1)，新增三列的 pure 像全部已经属于 $\pi(R_{-2})$，所以

$$
\pi(E_D)=\pi(R_{-2}).
$$

秩—零化度定理于是严格给出

$$
\boxed{\dim E_D=43,\qquad
\dim\pi(E_D)=9,\qquad
\dim(E_D\cap\ker\pi)=34.}
\tag{9}
$$

特别

$$
\boxed{\dim(U_{-2}\cap\ker\pi)\ge34.}
\tag{10}
$$

其中 $R_{-2}\cap\ker\pi$ 原有31维，另外三维可由 G³、J、D0 的上述 pure 零代表取得。旧纯幂尾测试还会丢掉一般 pure 像中的额外方向；不能把 (9) 与 R116 的幂尾核混为一谈。

(9) 没有增加 $U$ 的总维数下界：R153 的 $\dim U\ge239$ 已包含 D0。本次准确确定的是这个新方向可以放进 pure 核。实际 lineality 与已付真实共同查询仍至少237维；没有给 J 或 D0 的有符号实现。

## 5. 仿射轨道和 sharp 轴组合

R89/R105 的真实正仿射作用保持 $R$，并且不混合相位模式：

$$
\pi\mathsf P_{H,d}=\mathsf P_{H,d}\pi.
$$

把 (1) 整体输运，得到

$$
\boxed{\pi(\mathsf P_{H,d}\mathcal D_0)
=\pi(\mathsf P_{H,d}K_D)\in\pi R
\quad(H>0,\ d\in\mathbb R).}
\tag{11}
$$

所以 D0 的整个仿射轨道的一般 pure 部分都属于响应像；这里未确定它在完整商中的轨道维数，也不启动一条新的逐次平移计算链。

更一般，置

$$
Z_D=R+\operatorname{span}\operatorname{Orb}(G)
+\operatorname{span}\operatorname{Orb}(J)
+\operatorname{span}\operatorname{Orb}(\mathcal D_0).
$$

全部这些轨道的 pure 像都在 $\pi R$ 中，故

$$
\pi(Z_D)=\pi R,\qquad
\boxed{(Z_D\cap\ker\pi)/(R\cap\ker\pi)\simeq Z_D/R.}
\tag{12}
$$

证明是每个 $z\in Z_D$ 都可减去一个 $r\in R$ 匹配其 pure 像；该映射到 $Z_D/R$ 的核恰为 $R\cap\ker\pi$。未声称 $Z_D=U$。

R148 的 sharp 轴组合

$$
K_0=\mathcal D_0+\frac{25}{9}J
$$

也有准确 pure 表示

$$
\pi K_0=\pi\left(K_D+\frac{25}{9}K_J\right).
\tag{13}
$$

对任何杀 $R$ 的实泛函 $\lambda$，其尚未付的正性门可以写成

$$
\lambda J=\lambda H_J,\qquad
\lambda K_0=\lambda\left(H_D+\frac{25}{9}H_J\right).
$$

这只是完整原式代表的改写，不给予任一实数的符号；尤其不能从 pure 恒零就推闭成本锥的反号、输入相位平均或真实可控性。

## 6. 公开实际与输入身份

[公开 run43659795254](https://github.com/Rogerhu12/math-research-public/actions/runs/43659795254)，source
ce6c80bfbde6158e38c0e74e26fba3f352201658，lane general_pure_D0_membership。

实际 complete，耗时 **0.138208048秒**，峰值 RSS **34.28125 MiB**。生产者为
[literature_general_pure_D0_membership.py](../scripts/literature_general_pure_D0_membership.py)，25604 B，SHA256

~~~text
c296f72becff4366297e3b9f00db97425b1aa5b15c10ba7625932966ae7c8f1f
~~~

输入严格固定为：

| 输入 | 公开 run/source | 实际使用 |
|---|---|---|
| 完整 D0 原导出 | 43657526246 / 0d5df1843fd829e7c09b17afdead930ec4395f34 | pure 原目标；mixed仅只读来源 hash |
| R151 完整原基与代表证书 | 43657785023 / c606688a842bd811106ff2844e1161a4f34c159e | 九个原根和九个存储 word 代表 |

旧40基重新归约、31条依赖重算、原响应构造、N2/v4/forcing 编译、研究 profile 评价、mixed 归约、幂尾代入均为 **0**。R153 的模整数列表没有进入这个新有理求解。

同 job 的六项新增小人工全部通过，用时0.004102807秒。这些人工只核新存储接口、原差和失败边界，未读取研究原件。

## 7. 可复查完整证书

目录：notes/actions-43659795254-1-general_pure_D0_membership。

| 文件 | bytes | SHA256 |
|---|---:|---|
| [主报告](../notes/actions-43659795254-1-general_pure_D0_membership/general-pure-D0-membership.json) | 39342 | e78475ec38bed8057dc40d18979167ae2c4d5b5909f73fa3142a28cc38231c3d |
| [完整原式证书](../notes/actions-43659795254-1-general_pure_D0_membership/general-pure-D0-membership-certificate.json.gz) | 15463 | f5355a03cbdb076c9d33900930f0cad5e5c86abf4713f6b59b3acbd9b875037e |
| [发布回执](../notes/actions-43659795254-1-general_pure_D0_membership/receipt.json) | 36637 | d773b41d6deebf782fc386fb4b0198c42f242ef05b7ea62fccc5d679f4d76fe2 |
| [新增人工结果](../notes/actions-43659795254-1-general_pure_D0_membership/general-pure-D0-development.json) | 25375 | d5ffc94d1ce463fa573e7badc9055980789e792a927d2242fab36e5d6b5f41b8 |

证书原文88545 B，SHA256
117a4bf88cedd3a85ccfc26e6c80324bd67f3ce07aaf19b1837e434b0c7173cc。
它保存11个完整原根：D0 pure、九原基和一个新原差；同时保存九个原存储代表、新目标代表、准确有理系数与原差核零记录。publisher receipt 记录176个来源文件，所有输入都绑定原主报告、receipt、producer 源和 packed/raw 双 SHA。

本门至此结束。没有必要重新评价已经付清的 D0 pure 或扫描同一个幂尾。下一未付对象仍是完整 mixed 商的真实成本、全部作用量正性、全周期和 ruling，以及后续有限等距族与闭嵌入。
