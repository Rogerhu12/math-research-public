# R131：N³G 的原式分离、权负二响应 40 维及至少 111 个真实联合查询

日期：2026-11-14。**已证明。** 本稿消费公开 Actions 的一个新权块；不重新计算已经完成的 G、NG、N²G 响应块。

本次准确结论为

$$
\boxed{\dim\mathcal R_{8,-2}=40,\qquad N^3G\notin\mathcal R_8,\qquad4\le s\le10.}
\tag{1}
$$

结合既有同一真实 pure 尾投影，

$$
\boxed{\dim\mathcal R_8\ge107,\qquad \dim\mathcal U_4\ge111.}
\tag{2}
$$

R120 的真实闭成本锥 lineality 至少 111 维；R122 的有限构造给至少 111 个可在同一合法光滑三矩圆上联合支付的独立实查询。完整第四函数成本、ruling 和有限等距族没有由此全部支付。

## 1. 实际研究与可携原式身份

实际研究唯一来源为：

- 仓库：Rogerhu12/math-research-public；
- run：43653293263；
- source：2f0add61f44365d713abf836beaa8b0be2806a3d；
- lane：g_translation_successor；
- 本次显式参数：order 3，weight −2；
- [驱动](../scripts/literature_G_translation_successor.py)：39670 B，SHA256 为 a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406。

[主报告](../notes/actions-43653293263-1-g_translation_successor/G-third-translation.json) 为 25014 B，SHA256 为

~~~text
b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3
~~~

[发布回执](../notes/actions-43653293263-1-g_translation_successor/receipt.json) 为 34619 B，SHA256 为 a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523。

研究正常完成，耗时 53.46814492200001 秒，峰值 RSS 125.30859375 MiB。此前同 job 的 19 项人工接口检查全部通过；其[报告](../notes/actions-43653293263-1-g_translation_successor/G-translation-successor-development.json)为 6337 B、SHA256 为 10a1fd8184d8fc89c6bd521545bc27ca07b61a2496cd1ae88b7c0d9b3e5aba7a，耗时 0.006451691999998843 秒。人工检查不是本节研究证书的替代。

全部原依赖、原式评价矩阵和有理定义保存在[完整报告](../notes/actions-43653293263-1-g_translation_successor/G-third-translation-complete-report.json.gz)：

| 内容 | 字节数 | SHA256 |
|---|---:|---|
| 完整报告 gzip | 34253 | ff97938a939c0e69705f1528bcf327800fb491b84a7d633b3f57f2da1f193085 |
| 完整报告原始 JSON | 146817 | 5742c042180ca9ab951d05ccc970f3e27a201d14c02156d265e3cd951906a770 |

本次还成功保存[新块可携原式](../notes/actions-43653293263-1-g_translation_successor/G-third-translation-original-expressions.json.gz)，后续消费者无需重构本块：

| 内容 | 字节数 | SHA256 |
|---|---:|---|
| 原式 gzip | 157782 | 226ea60c21cac82674cd58df491e554eb226431953f4306f0c2c630e1228358e |
| 原式原始 JSON | 889438 | eb5f3314780df65d36159083a7a498e0945822e0f06f630bc7a1accb179c42a7 |

其 schema 为 visible-flex-G-translation-successor-original-v1-original-expressions，scope 为 one-translation-target-and-complete-new-response-block。102 个根保留目标及全部 50 个新响应的两模式原式、原列标签、2089 个 profile 原子、41621 个根单项，以及来源与输入绑定。该导出不是只保存 word 代表或保留的 40 列。

## 2. 目标是同锚平移 N³G

沿用 [R126](R126-first-G-translation-separation-and-52-query-control.md) 与 [R128](R128-second-G-translation-separation-and-76-query-control.md)：

$$
N(\xi)=1,\qquad N(q^{(j)})=N(\bar q^{(j)})=0,\qquad N(I_rF)=I_r(NF).
\tag{3}
$$

输入与共同右端锚同步搬移。N 因而不是在固定 profile 下求完整 $\partial_\xi$。G 的真权为 1，N³G 的真权为 −2。

驱动从冻结的原 G 重建前一目标，只用于与 R128 的两模式原哈希核对，再作下一次 N。旧 forcing、变量几何局部密度及 W36 编译没有运行；旧三块响应和原式子式没有重算。

| 模式 | 新 N³G 原式 SHA256 | 原项数 |
|---|---|---:|
| $-4$ | eaf54253f599a51e3adf18a80753a47e8112c51051342c353f8710148d9645f9 | 385 |
| $-2$ | da946b5f1755049e1f01b3a3326046e44736710895960fdc3ffd3a932669f165 | 1689 |

全过程对完整 $-4,-2$ 两模式使用同一组实控制系数，不把 pure 结论当作 mixed 结论。

## 3. 完整权负二空间的真实上界为 40

采用已冻结的完整 E8×W36 顺序与整数权。按二阶索引优先、第三索引次之，枚举全部

$$
w(P_i)+w(T_j)=-2
$$

的原响应，恰有 50 列。这里使用全部 E8，没有代换成常态七维子空间。

有声 word 消元只负责提出候选依赖。实际保留原列索引为

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
20,21,22,23,25,27,28,29,31,32,33,35,36,39,40,41,46,47,48,49
~~~

其余 10 列的每条有理依赖均重新在原始两模式表达式上构成差，并核成真零。十条完整依赖证明的规范 JSON SHA256 为

~~~text
a6453e43e03f92bc27c9a278e8115d64ece6eed9ddf1f82febdfd12fd05a9498
~~~

由这些原式关系严格得到

$$
\dim R_{-2}\le40,\qquad R=\mathcal R_8.
\tag{4}
$$

不完备正规形中的非零目标余项没有被用来宣布非成员。下面的反向秩界与分离来自原式有理积分。

## 4. 40/41 阶原式子式与真正的有理泛函

使用前几次相同的固定实 profile 对

$$
f=t^8(1-t)^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad
t=\xi-2,\quad0\le t\le1,
\tag{5}
$$

并在外侧零延拓，令 $q=f+ig$。共同右锚为 3。本块最大输入 jet 为 4，$C^7$ 零延拓足够定义全部评价，也可作保持这些评价连续性的光滑逼近。没有将 (5) 说成已经配平三矩的 profile 圆。

对 $t=j/25,\ j=1,\ldots,24$，依次取 $-4$ 实部、$-4$ 虚部、$-2$ 实部、$-2$ 虚部，共 96 行。原式评价器直接作有理多项式积分，不评价 word 代表。所有控制和目标共用 (5)、同一锚和同一组查询。

令 A 是上述 40 个保留原列的有理矩阵，b 是 N³G 的同一评价列。控制行集为

~~~text
J = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,
     18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47,
     50,51,54,55,58,59,62)
~~~

额外行 $e=63$。增广 41 行也可写为：

- $j=1,2,3,4$ 的全部四行；
- $j=5$ 的 $-4$ 实部及 $-2$ 实、虚部；
- $j=6,\ldots,16$ 的 $-2$ 实、虚部。

控制行从这 41 行中删去最后的 $j=16,-2$ 虚部。素数

$$
p=2147483647
$$

下的实际原矩阵子式为

$$
\det A_J\equiv1476048378\ne0\pmod p,
$$

$$
\det
\begin{pmatrix}
A_J&b_J\\
A_e&b_e
\end{pmatrix}
\equiv64963154\ne0\pmod p.
\tag{6}
$$

素数性质、$p\equiv3\pmod4$ 以及全部 81 个有理分母的可逆性均已检查。实际最高多项式次数为 76。完整 41×41 模矩阵在上述 gzip 中，其规范 SHA256 为 18725247b6a196a659d0afca595d7f7edb0c93866adc376346a9792daffdff9d。因此 (6) 是原有理实矩阵的合法非零约化。

定义真正的有理查询泛函

$$
\Lambda_0(V)=\operatorname{ev}_{e}(V)
-A_eA_J^{-1}\operatorname{ev}_{J}(V).
\tag{7}
$$

它对 40 个保留原列严格为零，继而由十条原式关系对全部 50 个原列严格为零；而

$$
\Lambda_0(N^3G)\equiv1591563935\ne0\pmod p.
\tag{8}
$$

(7) 中的逆是原有理矩阵之逆。报告打印的模 p 泛函系数不能直接当作 $\mathbb Q$ 系数；模值只证明非零，不包含实数符号判断。

(6) 给出 A 的真实实秩为 40、增广实秩至少 41。与 (4) 合并，

$$
\boxed{\dim R_{-2}=40,\qquad N^3G\notin R_{-2}.}
\tag{9}
$$

真实缩放作用使 $R=\bigoplus_wR_w$，目标是纯权 −2，故

$$
\boxed{N^3G\notin R.}
\tag{10}
$$

从 (9) 到 (10) 使用 universal 算子空间的真分权；没有宣称 (7) 在固定测试 profile 上还杀掉其他权的所有列。

## 5. G 轨道商至少四维

R118、R126、R128 与本稿依次证明

$$
G,\ NG,\ N^2G,\ N^3G\notin R.
$$

它们的权分别为 $1,0,-1,-2$。真分权使四个商类线性独立。令

$$
s=\dim\left(R+\operatorname{span}\operatorname{Orb}(G)\right)/R.
$$

原 G 的有限显式坐标次数不超过 9，故 $N^{10}G=0$。因此

$$
\boxed{4\le s\le10.}
\tag{11}
$$

本次只执行 order 3，没有自动计算整个后继链。本块的结果是 nonmember_certified，不能按成员分支停在 $s=3$。下一门仅为 N⁴G 的新权负三块；已有原式和原响应保持冻结。

## 6. 同一 pure 投影给出响应至少 107 维

[R116](R116-full-m8-tail-response-rank-and-finite-query-control.md) 的 pure $m=8$ 尾投影 $\Pi$ 是同一个真实 R 上的线性映射。其总像维数为 31；各真权像与本次完整空间相比较：

| 真权 w | 完整 $\dim R_w$ | $\dim\Pi(R_w)$ | $\dim\ker(\Pi|R_w)$ |
|---:|---:|---:|---:|
| $1$ | 7 | 1 | 6 |
| $0$ | 16 | 3 | 13 |
| $-1$ | 29 | 6 | 23 |
| $-2$ | 40 | 6 | 34 |

各核子空间处于不同真权，和为直和。因此

$$
\dim\ker\Pi\ge6+13+23+34=76,
$$

$$
\boxed{\dim R\ge\operatorname{rank}\Pi+\dim\ker\Pi\ge31+76=107.}
\tag{12}
$$

这里使用同一真实函数空间上的秩—零化度定理，不是把不同测试 profile 的矩阵秩直接相加。只用 R116 的映射身份和像维数即可得到 (12)；本次同 run 的完整 pure 几何 IBP 后续强化不作为本证明的前置条件。

四个 G 轨道方向均实际属于 U，且在 U/R 中独立，故

$$
\boxed{\dim U\ge\dim R+4\ge111,\qquad U=\mathcal U_4.}
\tag{13}
$$

## 7. 111 维 lineality 与 111 个实际联合查询

[R120](R120-G-lineality-of-the-closed-fourth-cost-cone.md) 已证明整个 $R+\operatorname{span}\operatorname{Orb}(G)$ 位于真实闭成本锥的 lineality。因此该 lineality 至少 111 维。这个闭锥结论本身没有把任意线性差变成一个实际有限成本逆元。

实际有限路径层使用 [R122](R122-affine-G-orbit-and-real-joint-query-control.md)：先固定有限辅助控制族及共同物理区间，再保留所有真实基准、偶项和矩阵补偿，按已证顺序选有限尺度与复制次数，以乘积盒 Brouwer 构造支付 $r+s$ 个独立实查询。由 (11)、(12)，

$$
r+s\ge107+4=111.
$$

R96 的忠实 profile 结论使这些有限查询可在同一个合法 $C^\infty$ 三矩圆上表达。所用合法圆不是未经补偿的 (5)。没有承诺对任意预先指定的 profile、窄区间、统一总长或几何控制盒都成立。

## 8. 后续边界

本次没有确定准确的 s、R 或 U 的维数，没有证明 $U=R+\operatorname{span}\operatorname{Orb}(G)$。新可携原式只导出这个已经完成的新块，并未包含全部旧权块。

完整第四函数成本与 ruling 的同时支付、双 collar、高阶与收敛、非平凡有限等距族、闭嵌入以及课题要求的 reach、握持区和宏观运动仍未完成。新结果的用途是提供一个可直接复用的真实权负二响应空间及其额外成本方向。
