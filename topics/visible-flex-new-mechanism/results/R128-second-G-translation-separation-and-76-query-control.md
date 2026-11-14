# R128：N²G 的原式分离、权负一响应 29 维及至少 76 个真实联合查询

日期：2026-11-14。**已证明。** 本稿消费一个新权块的公开 Actions 原式证书。R126 的旧权零块及先前 G 分离均未重新研究。

准确结论为

$$
\boxed{
\dim\mathcal R_{8,-1}=29,\qquad
N^2G\notin\mathcal R_8,\qquad
3\le s\le10.
}
\tag{1}
$$

结合已经完成的真实 pure 尾投影和其他完整权块，

$$
\boxed{
\dim\mathcal R_8\ge73,\qquad
\dim\mathcal U_4\ge76.
}
\tag{2}
$$

R120 的闭成本锥 lineality 也至少 76 维；R122 的实际有限构造给至少 76 个可在同一合法光滑三矩圆上联合支付的独立实查询。它们不是完整第四成本已经全部可付的结论。

## 1. 实际研究身份

本次实际：

- 仓库：Rogerhu12/math-research-public；
- run：43651413950；
- source：ba3a19be3ef851fbeb29ff491618e18622064f12；
- lane：g_second_translation；
- 驱动：[literature_G_second_translation.py](../scripts/literature_G_second_translation.py)，24396 B，SHA256 为 3c37aeae4b39ecf68932a069878b41d890afbe2fd4ee9d8675195edc4e5d6bc1。

[主报告](../notes/actions-43651413950-1-g_second_translation/G-second-translation.json) 41062 B，SHA256 为

~~~text
2828278fa8f881fbb53a2c6518a63d3067521c9860f07652c7e0080696cc5723
~~~

[发布回执](../notes/actions-43651413950-1-g_second_translation/receipt.json) 33699 B，SHA256 为 3abf0890dd897cfb2d4b1fa6ec2daef7c3f26a230613a48827cf7e2a8018ac68。

[完整报告 gzip](../notes/actions-43651413950-1-g_second_translation/G-second-translation-complete-report.json.gz) 保留全部有理依赖、原式身份与评价：

| 内容 | 字节数 | SHA256 |
|---|---:|---|
| gzip | 31107 | e390fb2ddde8718f4f1482d7d832c4f7c6ffe0c85dfe8f4eb04d3c5749543768 |
| 原始 JSON | 126586 | 0c4787f12c84b566f0d5183325fd7e189e4d7b6b3859c6e3e7cecf0783760891 |

研究正常完成，耗时 25.36639755600001 秒，峰值 RSS 124.4453125 MiB，不是预算退出。公开人工检查先通过十项接口门，耗时 0.0016130969999892386 秒；该人工报告为 5585 B，SHA256 为 5b87c903db7b9611da1958112c950af3694b744a8650cebac55db66ee8780253。

冻结输入包括 R118 的原 G、R126 的完成主报告/receipt，以及旧公开 W36 和局部原式导出。旧 forcing、局部密度、W 编译器没有运行；旧权零 20 列、16 列评价和 4 条关系未重算。驱动只从冻结 G 重建 NG，核对 R126 原哈希，再作下一次真实 N。

## 2. 目标与真权

采用 [R126](R126-first-G-translation-separation-and-52-query-control.md) 的同锚真实平移生成元：

$$
N(\xi)=1,\qquad
N(q^{(j)})=N(\bar q^{(j)})=0,\qquad
N(I_rF)=I_r(NF).
\tag{3}
$$

共同右端锚与输入同步搬移；N 不是固定 profile 下的完整 $\partial_\xi$。G 真权一，所以 N²G 真权负一。

两模式的新原式 SHA256 为：

| 模式 | N²G 原式 SHA256 | 原项数 |
|---|---|---:|
| $-4$ | 2f4985b03d739f86dfb97a6aa688afcb4c52a21a8c632ab3950cd36900d81c8e | 433 |
| $-2$ | c40b69eef9041cf7c381c95a1d6061910d9cbc99c82f541db576ff6c4f69abd3 | 1895 |

重建的 NG 哈希逐模式与 R126 完全相同。全过程采用相同实系数的完整 $-4,-2$ 两模式，不只计算对角或 pure 输出。

## 3. 完整权负一响应的真实上界

使用 R126 已明确的 E8 顺序与权、W36 冻结顺序。按二阶索引优先、第三索引次之，枚举全部满足

$$
w(P_i)+w(T_j)=-1
$$

的 E8×W36 原响应，恰有 36 列。这里使用全部 E8；没有代换成 R89 的物理七维子空间。

有声 word 消元提出 29 个保留原列，索引为：

~~~text
0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,
21,23,25,26,27,29,33,34,35
~~~

其余七列每一条有理依赖均重新在原始两模式表达式上组成差，并证明真零。七条完整证明的规范 JSON SHA256 为

~~~text
6fbb7b8bdc9ca95c8e524f52538a189db580e40c7723e6a12fd5935846e1b184
~~~

具体原列标签、系数和零差身份全部保存在上述完整 gzip。由这些真实关系严格得到

$$
\dim R_{-1}\le29,\qquad R=\mathcal R_8.
\tag{4}
$$

不完备正规形的非零目标余项没有被用来宣布非成员。下面的下界和分离来自原式有理积分。

## 4. 29/30 阶原式分离证书

取与 R118/R126 相同的固定实 profile 对

$$
f=t^8(1-t)^8,\qquad
g=f(1+2t+3t^2+5t^3),\qquad
t=\xi-2,\quad0\le t\le1,
$$

并在外侧零延拓。令 $q=f+ig$；所有右原函数从 3 积至查询点。本次可达原式最大输入 jet 为 4，所以该 $C^7$ 延拓足够定义全部评价，并可作保持所需 jets 的光滑逼近。

对 24 个 $t=j/25$，依次取两模式实/虚，共 96 行。所有原响应列和目标共用同一输入、同一锚、同一组查询。评价器直接对原式作有理多项式积分，不评价 word 代表。

令 A 是 29 个保留原列的有理矩阵，b 是 N²G 的同一评价列。控制行集为

~~~text
J = (0,1,2,3,4,5,6,7,8,9,10,11,14,15,18,19,22,23,
     26,27,30,31,34,35,38,39,42,43,46)
~~~

额外行是 $e=47$。行的完整约定为：每个 j 对应四行，依次是 $-4$ 实、$-4$ 虚、$-2$ 实、$-2$ 虚。所选增广 30 行可以简写为：

- $j=1,2,3$ 的全部四行；
- $j=4,\ldots,12$ 的 $-2$ 实、虚两行。

控制行从这 30 行中删去最后的 $j=12,-2$ 虚部，亦即第 47 行。

实际素数 $p=2147483647$ 下，

$$
\det A_J\equiv567957958\ne0\pmod p,
$$

$$
\det
\begin{pmatrix}
A_J&b_J\\
A_e&b_e
\end{pmatrix}
\equiv581835661\ne0\pmod p.
\tag{5}
$$

素数性质、$p\equiv3\pmod4$ 及本块全部 81 个有理分母可逆性已核；实际最高多项式次数为 76。因而这些是原有理实矩阵的合法非零约化。

定义真正的有理查询泛函

$$
\Lambda_0(V)=\operatorname{ev}_e(V)
-A_eA_J^{-1}\operatorname{ev}_J(V).
\tag{6}
$$

它对全部 29 个保留原列严格为零，由七条原式依赖也对其余原列为零。另一方面，

$$
\Lambda_0(N^2G)\equiv1662767392\ne0\pmod p.
\tag{7}
$$

(6) 使用原有理矩阵的逆，不能把报告中的模 p 泛函系数直接当作 Q 系数。模值只证非零，没有实数符号含义。

(5) 证明 A 的真实实秩也为 29，增广实秩至少 30；因此与 (4) 合并，

$$
\boxed{\dim R_{-1}=29,\qquad N^2G\notin R_{-1}.}
\tag{8}
$$

真实缩放给 $R=\bigoplus_wR_w$，而目标纯权负一，所以

$$
\boxed{N^2G\notin R.}
\tag{9}
$$

这里对完整 R 的推论来自 universal 真分权。没有声称 (6) 在这个固定测试 profile 上也杀掉所有其他权的评价列。

## 5. 轨道商至少三维：继续链，不停在 s=2

R118、R126 与本稿分别给

$$
G\notin R,\qquad NG\notin R,\qquad N^2G\notin R.
$$

三者的权依次为 $1,0,-1$，故它们在真实商中独立。R122 中

$$
s=\dim\left(R+\operatorname{span}\operatorname{Orb}(G)\right)/R
$$

因此至少为 3。R126 已证原 G 的有限显式坐标次数不超过 9，故 $N^{10}G=0$，仍得

$$
\boxed{3\le s\le10.}
\tag{10}
$$

本次只研究 order2，没有执行更高阶。实际结果为 nonmember_certified，所以不能按阳性成员分支宣布 s=2 或结束链。下一步只需要 N³G 的新权负二块；已完成的权一、零、负一证据保持冻结。

## 6. 同一个真实 pure 映射给 73 与 76

按 [R125](R125-complete-response-dimension-at-least-48-and-cost-49.md)、R126 与 [R116](R116-full-m8-tail-response-rank-and-finite-query-control.md)，pure $m=8$ 尾投影是定义在同一真实 R 上的线性映射 $\Pi$，且

$$
\operatorname{rank}\Pi=31.
$$

已完成分权像维数及本次完整维数为：

| 真权 | 完整 $\dim R_w$ | $\dim\Pi(R_w)$ | 核维数 |
|---:|---:|---:|---:|
| $1$ | 7 | 1 | 6 |
| $0$ | 16 | 3 | 13 |
| $-1$ | 29 | 6 | 23 |

三个核子空间位于不同真权，和为直和。因此

$$
\dim\ker\Pi\ge6+13+23=42,
$$

$$
\boxed{\dim R\ge31+42=73.}
\tag{11}
$$

这是同一真实函数空间上的秩—零化度计算，不是把不同 profile 测试矩阵的秩直接相加。R116 的 pure 投影会丢掉完整信息，正是这些核维数产生了加强。

三个 G 链方向在 $U/R$ 中独立，故

$$
\boxed{\dim U\ge\dim R+3\ge76.}
\tag{12}
$$

R120 已把整个 G 仿射轨道与 R 放进真实闭成本锥的 lineality，故其维数同样至少 76。闭锥 lineality 自身仍不授实际有限成本逆元。

实际有限路径层使用 [R122](R122-affine-G-orbit-and-real-joint-query-control.md)，其构造保留所有基准、偶项、矩阵补偿、共同物理区间和有限复制次数，支付 $r+s$ 个查询。由 (10)、(11)，至少为 76。按 R96，可在固定有限辅助控制族之后选共同物理区间及一个合法光滑三矩圆，忠实表达这些查询。

没有据此对任意预先给定的 profile、窄区间、总长限制或几何控制盒作普遍保证。

## 7. 没有被本次证书支付的内容

本稿没有确定准确的 s、完整 R 或 U 的维数，也没有证明 $U=R+\operatorname{span}\operatorname{Orb}(G)$。新的三个商方向是实际控制构造可用的有限维增量，并非完整第四函数成本已经为零。

全部第四 ruling、双 collar、高阶与收敛、非平凡有限等距族及闭嵌入、reach、握持区和宏观运动要求仍须继续处理。
