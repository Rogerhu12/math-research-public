# O6：立方分母的完整原始四次式参数化

日期：2026-11-12；会话：serre-uniformity-astra-resume2。

**状态：完整参数化与原始文献接口。** 对 R19 的 $Z=Y^3$ 支，下面给出四个四次式 $p$ 次幂方程的必要且充分参数化，覆盖所有符号和三个族。参数化本身还不是无解定理。已核查 Darmon–Merel 的定理并不直接覆盖这些四次式；直接相关的实二次 $\mathbb Q$-曲线文献还明确保留 $d=3$ 的非 CM 新形式。

## 1. 有符号的原始 $(3,3,2)$ 方程

令 $p>37$ 为素数，$Z=Y^3$，$|Y|>1$、$(Y,6p)=1$。族 I、III 令 $T=Y^p$，族 II 令 $T=2Y^p$。原方程统一为
$$
X^3-T^3=27W^2,\qquad (X,T)=1,\qquad 3\nmid XT,
\quad W\ne0.
\tag{1}
$$
$X,T,Y$ 可以为负。由实立方函数严格递增，(1) 总有 $X>T$。同时
$$
B=X^2+XT+T^2>0.
$$
模 $3$ 得 $X\equiv T\not\equiv0$，从而
$$
\gcd(X-T,B)=3,\qquad v_3(B)=1.
$$
后一式可写 $X=T+3k$ 后直接计算：
$$B=3(T^2+3Tk+3k^2),\qquad 3\nmid T.$$
在 $3$ 以外，两个因子均为正且互素，故分别为平方；在 $3$ 处，$v_3(X-T)+1=3+2v_3(W)$。于是存在唯一的正整数 $U,V$，使
$$
\boxed{X-T=9V^2,\qquad B=3U^2,\qquad W=\pm UV,}
\tag{2}
$$
并且 $(U,V)=1$、$3\nmid U$。

将 $X=T+9V^2$ 代回，得到
$$
U^2=T^2+9TV^2+27V^4.
\tag{3}
$$
设 $C=2T+9V^2$，以及
$$R=2U-C,\qquad S=2U+C.$$
则
$$
RS=27V^4,\qquad R+S=4U,\qquad S-R=4T+18V^2.
\tag{4}
$$
由于 $4U^2-C^2=27V^4>0$，**$R,S$ 都是正数**，即使 $X,T,Y$ 为负也如此。若某个奇素数同时整除 $R,S$，则它整除 $U,C$；(4) 和 $(U,V)=1$ 迫使它为 $3$，但 $3\nmid U$ 排除这一可能。所以 $\gcd(R,S)$ 是 $2$ 的幂，且 $3$ 的全部赋值只落在一侧。

## 2. $2$ 处的两个完整分支

### 2.1 $V$ 奇

此时 $C,R,S$ 都奇，故 $(R,S)=1$。式 (4) 精确给出以下两个有序分支之一：
$$
(R,S)=(a^4,27b^4)\quad\text{或}\quad(27b^4,a^4),
\tag{5}
$$
其中 $a,b>0$、$(a,b)=1$、$3\nmid a$、$a,b$ 都奇，而且
$$
V=ab,\qquad U=\frac{a^4+27b^4}{4}.
\tag{6}
$$
模 $4$ 可直接确认 (6) 为奇整数。这里 $b$ 可以被 $3$ 整除，$3$ 处的任意高赋值已包含在 $27b^4$ 中。

### 2.2 $V$ 偶

原始性迫使 $T$ 奇，否则 $X,T$ 都偶；由 (3) 有 $U$ 奇。又 $v_2(C)=1$，故 $4\mid R,S$。因为 $R+S=4U$ 的 $2$ 赋值恰为 $2$，$R,S$ 中恰有一个的 $2$ 赋值为 $2$，另一个更大。由 $v_2(RS)=4v_2(V)$，得到 $v_2(V)\ge2$，且
$$\gcd(R,S)=4.$$
对 $R/4,S/4$ 应用互素的正因子分解，完整得到
$$
(R,S)=(4a^4,108b^4)\quad\text{或}\quad(108b^4,4a^4),
\tag{7}
$$
其中 $a,b>0$、$(a,b)=1$、$3\nmid a$、$a,b$ 奇偶相反，且
$$
V=2ab,\qquad U=a^4+27b^4.
\tag{8}
$$
因为 $a,b$ 奇偶相反，$V$ 自动被 $4$ 整除。没有漏掉 $v_2(V)=1$ 的分支：上面的赋值等式已证明它不可能。

## 3. 四个原始 $p$ 次幂方程

定义
$$
F(a,b)=a^4-18a^2b^2-27b^4,\qquad
G(a,b)=27b^4-18a^2b^2-a^4.
\tag{9}
$$
由 (4)–(8)，得到完整表格：

| R19 族 | 参数奇偶及实际模 $3$ 条件 | 必须求解的方程 | $V$ | $U$ |
|---|---|---|---|---|
| I | $a,b$ 奇偶相反，$3\mid b$ | $F(a,b)=Y^p$ | $2ab$ | $a^4+27b^4$ |
| III，$X$ 奇 | $a,b$ 奇偶相反 | $G(a,b)=Y^p$ | $2ab$ | $a^4+27b^4$ |
| III，$X$ 偶 | $a,b$ 都奇，$3\mid b$ | $F(a,b)=4Y^p$ | $ab$ | $(a^4+27b^4)/4$ |
| II | $a,b$ 都奇 | $G(a,b)=8Y^p$ | $ab$ | $(a^4+27b^4)/4$ |

每行还要求 $a,b>0$、$(a,b)=1$、$3\nmid a$、$|Y|>1$、$(Y,6p)=1$。从表内数据恢复
$$
T=Y^p\ \text{（I、III）},\quad T=2Y^p\ \text{（II）},
\qquad X=T+9V^2,\quad W=\pm UV,\quad Z=Y^3.
\tag{10}
$$
$Y$ 可正可负，两个 $W$ 符号都允许；$a,b$ 为正不限制这些符号，因为它们来自 (5)、(7) 中的正四次幂，而 $F,G$ 本身可以为负。

### 3.1 反向恒等式与原始性

直接代入 (9) 和表内的 $U,V,T$，即有 (3)，继而
$$
(T+9V^2)^3-T^3=27(UV)^2.
\tag{11}
$$
因此 (10) 确实满足原方程。

任何素数若同时整除 $T$ 和 $V$，就在 $a,b$ 中整除一个；(9) 模该素数的值为 $\pm a^4$ 或 $\pm27b^4$，由 $(a,b)=1$、$3\nmid a$ 排除。$2$ 处也没有例外：异奇偶参数时 $T$ 奇，同奇参数时 $V$ 奇。因此 $(T,V)=1$，且 $3\nmid T$，从 $X=T+9V^2$ 得 $(X,T)=1$。

若素数同时整除 $T,U$，(3) 迫使它整除 $27V^4$，再次矛盾。所以 $(T,U)=1$。若素数同时整除 $X,U$，则 $X^2+XT+T^2=3U^2$ 迫使它整除 $T$，也矛盾。由此
$$
\gcd(X,W)=\gcd(X,T)=\gcd(T,W)=1.
$$
这些等式给出 R19 要求的所有两两互素性，包括族 II 的 $T=2Y^p$。

### 3.2 与 R19 模 $4$ 条件的精确对应

异奇偶参数时，$F\equiv1\pmod4$、$G\equiv3\pmod4$，而 $4\mid V$、$4\mid W$。于是第一行恰为族 I，第二行恰为 III 奇 $X$。

同奇参数时有恒等的剩余类
$$F(a,b)\equiv20\pmod{32},\qquad G(a,b)\equiv8\pmod{32}.$$
故第三行 $T\equiv5\pmod8$、$X\equiv6\pmod8$、$W$ 奇，恰为 III 偶 $X$；第四行 $T\equiv2\pmod8$、$X\equiv3\pmod8$、$W$ 奇，恰为 II。也得到第三行 $Y\equiv5\pmod8$，第四行 $Y\equiv1\pmod4$。

综上，表格连同明确列出的原始条件与 R19 的立方 $Z$ 分支等价，而不是仅给出其中一个有理参数化图。

表内两条 $F$ 行的 $3\mid b$ 来自 R19 的实际 $a_3(E)=0$ 条件：这两行 $X\equiv1\pmod3$，而 $3\mid W$ 当且仅当 $3\mid b$。这是由原始方程与 R19 已证明的全局同余推出的必要条件，已明确包含在参数表中。两条 $G$ 行则 $X\equiv2\pmod3$，不受这一附加条件限制。

## 4. Darmon–Merel 的接口与实二次的实际剩余形式

Darmon–Merel (1997) 的 Main Theorem 处理原始的
$$x^n+y^n=2z^n,\qquad x^n+y^n=z^2,\qquad x^n+y^n=z^3,$$
分别要求 $n\ge3,4,3$；最后一个原先的模性假设现已成立。上表中只有 $Y$ 被证明是 $p$ 次幂底数，不能把 $a,b$ 或 $X$ 也写成 $p$ 次幂。因此表内方程不是这些定理的一个已核验实例。该文 Theorem 8.1 所需的实际有理 $2$ 或 $3$ 同源也不存在：R19 的 $E$ 若有这种同源，就与 Lemos 的定理矛盾。模 $3$ 与固定 $A$ 同构不会传递 $A$ 的有理 $2$ 挠点。

一个更接近的恒等式为
$$
F=4a^4-3(a^2+3b^2)^2,\qquad
G=3(a^2-3b^2)^2-4a^4.
\tag{12}
$$
当 $a,b$ 都奇，设
$$h_+=\frac{a^2+3b^2}{2},\qquad h_-=\frac{a^2-3b^2}{2}.$$
这两个数为整数。第三行直接成为真正的原始方程
$$
a^4-3h_+^2=Y^p,\qquad
2h_+-a^2=3b^2,
\tag{13}
$$
其中 $\gcd(a,h_+,Y)=1$，$a$ 奇、$h_+\equiv2\pmod4$。第四行则为
$$
a^4-3h_-^2=-2Y^p,\qquad
a^2-2h_-=3b^2,
\tag{14}
$$
其中 $a,h_-$ 都奇且互素。异奇偶的两行保留
$$4a^4-3(a^2+3b^2)^2=Y^p,$$
或
$$4a^4-3(a^2-3b^2)^2=-Y^p.$$
不能用一个使三坐标有公因子的缩放，把这些系数都当作不存在。

Pacetti–Villagra Torcomian，*Q-curves, Hecke characters and some Diophantine equations II*，Publicacions Matemàtiques **67** (2023), 569–599，研究的正是 $x^4-dy^2=z^p$、$d>0$。这不是只适用于虚二次域的前篇；它给出实二次 Hecke 特征与模方法。该稿 Theorem 3.2 正文虽然要求存在 $q>3$ 在 $K$ 分歧，但其后的 **Remark 2 明确将同一结论扩展到 $K=\mathbb Q(\sqrt3),\mathbb Q(\sqrt6)$**：在分歧素数 $q=3$ 用 $5$ 挠点取代 $3$ 挠点。所以这个已处理的局部扩展不是这里的剩余缺口。真正的边界是作者稿 **§5 开头明确将 $d\in\{3,5,7,14\}$ 列为还有非 CM 新形式不能由该筛法排除的情形**。

因此 (13) 确实接到一个已经研究的实际广义 Fermat 方程，同时留下了可用于多 Frey 比较的额外关系 $2h_+-a^2=3b^2$。目前尚未证明这一额外关系排除该文的残留新形式。其他三行的 $2,4$ 系数及原始条件也需要分别保留。没有得到固定四次式的统一最大指数。

## 5. 可复验入口与来源

标准库证书 [verify_cube_denominator_parametrization.py](verify_cube_denominator_parametrization.py) 做两类相互独立的检查：从四个参数图验证原方程、原始性和模 $4$ 条件；直接遍历有符号 $(X,T)$ 的有限盒，识别所有原始平方商，再反向恢复 (5)、(7) 的四次根。完整性由本文证明，有限盒不承担无界完备性。

```sh
python3 -B topics/serre-uniformity/notes/verify_cube_denominator_parametrization.py
```

- H. Darmon, L. Merel, *Winding quotients and some variants of Fermat's Last Theorem*, J. reine angew. Math. **490** (1997), 81–100；Main Theorem 与 Theorem 8.1；[作者原文](https://www.math.mcgill.ca/darmon/pub/Articles/Research/18.Merel/paper.pdf)，[DOI](https://doi.org/10.1515/crll.1997.490.81)。
- A. Pacetti, L. Villagra Torcomian, *Q-curves, Hecke characters and some Diophantine equations II*；[作者原文](https://sweet.ua.pt/apacetti/papers/Q-curves2.pdf)，[DOI](https://doi.org/10.5565/publmat6722304)。
- 全局立方条件与实际模 $3$ 同构的等价，见[另记](2026-11-12-global-cube-and-three-congruence.md)。

原始 $(3,3,p)$ 定理不能直接作用于 $X^3-(Y^p)^3=27W^2$ 的平方项：把 $27W^2$ 写成整数立方还需要 $W$ 本身为立方。该特殊形状已经由[此前的 Kraus 定理接口](2026-11-12-fermat-literature-and-quadratic-factorization-resume2.md)排除，不能据此删除其余 $W$。
