# R3：从一个二次 Taylor 系数到初级有限性的严格归约

**可信度：已证明。** 本文证明一个可用的逐素数判据，并精确指出尚未证明的跨素数命题。它不把判据本身登记为主目标的证明。

## 1. 使用的经典输入与记号

设 $E/\mathbb Q$ 为椭圆曲线，$p>2$ 为好普通约化素数。令 $\mathbb Q_\infty/\mathbb Q$ 为 cyclotomic $\mathbb Z_p$-扩张，$\Gamma=\operatorname{Gal}(\mathbb Q_\infty/\mathbb Q)$，选择生成元 $\gamma$，写
$$
\Lambda=\mathbb Z_p[[\Gamma]]\simeq\mathbb Z_p[[T]],\qquad \gamma=1+T.
$$
令
$$
X=\operatorname{Sel}_{p^\infty}(E/\mathbb Q_\infty)^\vee,
\qquad f_{E,p}(T)=\operatorname{char}_\Lambda(X).
$$
下列两个经典输入适用于这个情形：

1. Mazur 控制定理：从基域 Selmer 群到无穷层 Selmer 群的 $\Gamma$-不变部分的限制映射有有限核及有限余核。因此
   $$
   \operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)
   =\operatorname{rank}_{\mathbb Z_p}(X/TX).
   \tag{1}
   $$
2. Kato 定理：$X$ 是有限生成挠 $\Lambda$-模；对不含 $p$ 的高度一素理想，代数特征理想的长度不超过相应 $p$-adic $L$ 函数的消失阶。特别地，
   $$
   \operatorname{ord}_{T=0}f_{E,p}(T)
   \le\operatorname{ord}_{T=0}L_p(E,T).
   \tag{2}
   $$

这里 $L_p(E,T)$ 取含平凡角色的通常 cyclotomic 分支；用任意非零常数改变周期正规化不影响 (2)。我们只在高度一素理想 $(T)$ 使用 Kato 的结论，故**不需要**从整系数整除中排除剩余表示不满的素数，也没有把整主猜想作为假设。

原始文献：B. Mazur, *Rational points of abelian varieties with values in towers of number fields*, Invent. Math. 18 (1972), 183–266；K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117–290，Theorem 17.4(1),(2), p.273，<https://www.numdam.org/item/AST_2004__295__117_0.pdf>。椭圆曲线记号下的对应结论亦见 W. Stein–C. Wuthrich, *Algorithms for the arithmetic of elliptic curves using Iwasawa theory*, Math. Comp. 82 (2013), 1757–1792，§6.1 和 Theorems 7.3–7.4，<https://wstein.org/papers/mcom2649-iwasawa-alg.pdf>。

## 2. 余不变量的秩与特征级数阶数

**引理。** 对有限生成挠 $\Lambda$-模 $M$，
$$
\operatorname{rank}_{\mathbb Z_p}(M/TM)
\le\operatorname{ord}_{T=0}\operatorname{char}_\Lambda(M).
\tag{3}
$$

**证明。** $R=\Lambda_{(T)}$ 是离散赋值环，统一化元为 $T$，剩余域为 $\mathbb Q_p$。局部化 $M_R$ 是有限长度 $R$-模，故有分解
$$
M_R\simeq\bigoplus_{i=1}^b R/(T^{a_i}),\qquad a_i\ge1.
$$
由特征理想的定义，右侧阶数是 $\sum_i a_i$。而
$$
(M/TM)\otimes_{\mathbb Z_p}\mathbb Q_p\simeq M_R/TM_R
$$
的维数是 $b$。于是 (3) 就是 $b\le\sum_i a_i$。空直和的情形两边为零。$\square$

这个证明解释了为何不能把特征级数的消失阶直接等同于基域 Selmer 余秩。例如 $M=\Lambda/(T^2)$ 的模 $T$ 商秩为 $1$，特征级数的阶却为 $2$；差别正是更高的 $T$-初级块。有限的伪零模在上述局部化中消失。

## 3. 二次系数判据

**定理。** 假设已经独立证明 $\operatorname{rank}E(\mathbb Q)\ge2$。对任一好普通素数 $p>2$，写
$$
L_p(E,T)=\sum_{j\ge0}c_{j,p}T^j.
$$
若 $c_{2,p}\ne0$，则
$$
\operatorname{rank}E(\mathbb Q)=2,
\qquad \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}.
\tag{4}
$$

**证明。** 写 $r=\operatorname{rank}E(\mathbb Q)$，$s_p=\operatorname{corank}_{\mathbb Z_p}\operatorname{Sel}_{p^\infty}(E/\mathbb Q)$。R1、(1)、(3)、(2) 依次给出
$$
2\le r\le s_p\le\operatorname{ord}_{T=0}f_{E,p}
\le\operatorname{ord}_{T=0}L_p(E,T).
\tag{5}
$$
特别地 $c_{0,p}=c_{1,p}=0$。若 $c_{2,p}\ne0$，(5) 最右侧恰为 $2$，所以所有不等式均为等号。由 $s_p=r$ 和 R1，得到所求初级有限性。$\square$

这里仅要求二次系数**非零**，不要求它是 $p$-adic 单位，也不先假设高度非退化。单位条件在求初级部分的精确阶或证明其为零时可能有用，但对 (4) 是过强的要求。

改变生成元使变量变成 $(1+T)^u-1$，其中 $u\in\mathbb Z_p^\times$；由于低于二次的系数已经为零，二次系数乘以 $u^2$。乘上非零常数或可逆幂级数同样不改变它是否为零。所以本判据不依赖这些正规化选择。

## 4. 可用于本题的跨素数命题——尚未证明的部分

对 R2 的曲线或 R4 的 CM 曲线，定义
$$
\mathcal P_E=\{p>2:E\text{ 在 }p\text{ 好普通，且 }c_{2,p}\ne0\}.
$$
由第 3 节，命题
$$
\#\mathcal P_E=\infty                                                    \tag{6}
$$
足以完成本题。**本文没有证明 (6)。** 以下几件事也不能代替 (6)：

- 对每个固定 $p$，$L_p(E,T)$ 不是零级数；非零级数仍可能有四阶或更高的零点。
- cyclotomic 主猜想；它识别特征级数，不决定该级数在 $T=0$ 的阶数。
- 一个或有限多个 $p$ 的有限精度非零证书。
- 各个非扭有理点的某种高度非零；二阶行列式非零是另一个断言，而且仅高度非退化也未排除额外 Selmer 类。

## 5. 抽象数据不足的一个具体模型

取
$$
M=\bigl(\Lambda/(T)\bigr)^4,
\qquad L(T)=T^4,
\qquad r=2.
$$
则 $M$ 挠，$\mu(M)=0$，其特征级数恰等于 $L$，$L$ 非零，$M/TM$ 的秩与 $r$ 都是偶数。但模论数据允许 $s=4>r=2$，对应 R1 中 $d_p=2$ 的可能性。可以把秩二的有理点部分嵌入 $\mathbb Z_p^4$，因此加入“已知两个独立点”仍不能排除此模型。

这不是实际椭圆曲线的反例，而是证明：若一个论证只使用“挠性、主猜想、$\mu=0$、偶性及两个已知点”，它尚未包含足以推出 $s_p=2$ 的信息。所缺的算术输入必须明确补上，例如 (6) 中的二次系数非零性。
