# R113：环类数六的原始三次周期，在全部实际小惯性素数处非消失

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，附完整有限证书。** 这里的素数 $p$ 没有预先扫描上限。由已发表的无条件类数界、准确原始导子筛和一个整数最大公因数，先把全部可能的周期零点压到三个候选对；实际小惯性分支的模九条件同时排除它们。

## 1. 结论、量词及仍须保留的边界

设 $K$ 为判别式 $-D$ 的虚二次域，
$$
\mathcal O_c=\mathbb Z+c\mathcal O_K,\qquad M=Dc^2,
\qquad h(\mathcal O_c)=6.
$$
令 $\eta$ 为准确导子 $c$ 的原始三阶环类角色。设 $p>37$ 惰性于 $K$，且 $p\nmid M$。沿用 R76、R90 的素水平 Brandt 周期记号 $P_\eta$。

**定理 113.1。** 若 $P_\eta=0$，则必有
$$
\boxed{(M,p)\in\{(707,53),(1432,43),(2443,43)\}.} \tag{113.1}
$$
这里仅声称这些是必要候选，并未把下文的类多项式立方条件说成三色平衡的充分条件。特别，
$$
\boxed{p\equiv2,5\pmod9\quad\Longrightarrow\quad P_\eta\ne0.} \tag{113.2}
$$
相应地，至少有一个层 $p$ 的权二新形式 $g$ 满足
$$
L\bigl(\tfrac12,\pi_{g,K}\otimes\eta\bigr)\ne0. \tag{113.3}
$$

**推论 113.2（实际表示，全素数范围）。** 设本课题的实际曲线 $E/\mathbb Q$ 满足
$$
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p),\qquad
\bar\rho_{E,p}(I_p)=C^3,\qquad p>37.
$$
取 R66 的实际原始三次角色 $\eta$ 和准确导子 $c$。若 $h(\mathcal O_c)=6$，则 (113.3) 总成立。证明只需 R66 已证的
$$p\equiv2,5\pmod9;$$
不需要假设 $j(E)$ 整，不需要控制坏素数支集，也不需要先识别二除域或三除域。

结合 R90 对实际环类数三分支的非消失，任何仍满足全部三次中心值共同为零的实际小惯性分支，都必须满足
$$\boxed{h(\mathcal O_c)\ge9.} \tag{113.4}$$
这里使用 $3\mid h(\mathcal O_c)$，它来自实际非平凡三次角色的存在。

非消失本身不排除其他层的 exceptional 分母。在 $p=41,47,59,83$，R92 的无 exceptional 结论、R69/R72 的整性接口和 R109 的完整整点分类进一步排除了实际环类数六分支。其他素数、更高环类数和完整 Cartan 惯性仍不由本篇解决。

## 2. 六个类、三种颜色与必要的二次立方关系

有限阿贝尔群 $\operatorname{Pic}(\mathcal O_c)$ 的阶为六，所以它同构于 $C_6$。其两个三阶角色互为逆，核均为唯一的阶二子群；颜色 $1,\zeta_3,\zeta_3^2$ 各出现两次。

先选择一个具有 $\mathcal O_c$ 复乘的椭圆曲线，在 $p$ 上方约化，并以其最大自同态环作 Brandt 基准序。与 R90 §2 相同，Deuring 对应识别的是**右理想类与超奇异椭圆曲线的同构类**，而非仅仅左序的共轭类型。环类群的可逆理想作用与约化相容，所以六个类多项式根的约化，恰给周期中的六个 Brandt 基向量。

$p\nmid c$ 保证 CM 嵌入在 $p$ 处最优；在其他素数处，约化保持对应 Tate 格上的 CM 序。这使非极大序也能使用同一理想对应。若原来选择了其他容许的 Brandt 基准序，可通过完整特征谱及 CST 的同一个周期公式传输“全部中心值为零”这一条件，正如 R80/R90 已证明的接口。

对任一约化纤维，记三色数目为 $n_0,n_1,n_2\in\{0,1,2\}$。它在周期中的系数为
$$n_0+n_1\zeta_3+n_2\zeta_3^2.$$
若归一化包含一个依赖该超奇异点的非零权重，此权重对整个纤维相同，不影响系数是否为零。因 $1,\zeta_3$ 在 $\mathbb Q$ 上线性无关，
$$
n_0+n_1\zeta_3+n_2\zeta_3^2=0
\quad\Longleftrightarrow\quad n_0=n_1=n_2. \tag{113.5}
$$
因此 $P_\eta=0$ 时，每个非空纤维恰有三个或六个元素。设
$$H_{-M}(X)=\prod_{[\mathfrak a]\in\operatorname{Pic}(\mathcal O_c)}
 (X-j(\mathfrak a))\in\mathbb Z[X].$$
其模 $p$ 的每个根重数皆被三整除，从而
$$
\boxed{P_\eta=0\quad\Longrightarrow\quad
 H_{-M}(X)\bmod p=Q(X)^3
 \text{，其中 }Q\in\mathbb F_p[X]\text{ 首一二次}.} \tag{113.6}
$$
首一立方根在代数闭包中唯一，且被 Frobenius 保持，故其系数确在 $\mathbb F_p$。

这是本文所需的全部方向。反过来，两个大小为三的纤维未必每个都各含三色一次；只知道 $H_{-M}$ 是立方，不足以忽略颜色数据。本证明始终没有作这个逆推。

由于 $\sum\eta=0$，周期落在次数零 Brandt 模中。素水平的完整尖点谱和 Cai–Shu–Tian Theorem 1.2 给
$$
P_\eta=0
\quad\Longleftrightarrow\quad
L(\tfrac12,\pi_{g,K}\otimes\eta)=0
\text{ 对所有层 }p\text{ 的权二新形式 }g. \tag{113.7}
$$
归一化常数非零且正；这与 R90 使用的等价完全相同，不是只用 Waldspurger 公式的一个方向。

## 3. 原始环类数六序的完整枚举界

扩张理想给满射
$$\operatorname{Pic}(\mathcal O_c)\twoheadrightarrow\operatorname{Cl}(\mathcal O_K),$$
故 $h_K$ 只能为 $1,2,3,6$。Watkins 已发表的无条件分类给如下准确上界和数量：

| $h_K$ | $D$ 的最大值 | 域的数量 |
|---:|---:|---:|
| 1 | 163 | 9 |
| 2 | 427 | 18 |
| 3 | 907 | 16 |
| 6 | 3763 | 51 |

本篇使用这些**全局完备界**作为外部输入；范围内的全部基本判别式和类数重新通过 primitive 正定约化二元型枚举，不从数据库照抄序列表。

若 $c>1$，写
$$u_K=[\mathcal O_K^\times:\{\pm1\}]\in\{1,2,3\}.$$
环类数公式为
$$
6=\frac{h_Kc}{u_K}\prod_{q\mid c}\left(1-\frac{\chi_K(q)}q\right). \tag{113.8}
$$
右边的 Euler 因子逐个不小于 $1-1/q$，所以
$$\varphi(c)\le\frac{6u_K}{h_K}\le18.$$
又有初等恒等式及下界
$$
\frac{\varphi(c)^2}{c}
 =\prod_{q^e\parallel c}q^{e-2}(q-1)^2\ge\frac12.
$$
唯一可能小于一的局部因子是 $q=2,e=1$ 的 $1/2$；其他局部因子皆至少为一。因此
$$\boxed{c\le648.} \tag{113.9}$$
这是真正的证明界，不是经验截断。

### 3.1 原始性的准确判据

对每个 $c'\mid c$，自然映射
$$\operatorname{Pic}(\mathcal O_c)\twoheadrightarrow\operatorname{Pic}(\mathcal O_{c'})$$
满射。因为源群为 $C_6$，其三次角色经该商分解，当且仅当目标群阶被三整除：目标阶若为三或六，映射核含于唯一的阶二子群；目标阶为一或二则没有非平凡三次角色。

所以，类数六的两个三次角色原始当且仅当
$$
3\nmid h(\mathcal O_{c'})
\quad\text{对每个真因子 }c'\mid c. \tag{113.10}
$$
这也说明 $h_K=3$ 时没有原始候选，$h_K=6$ 时只能 $c=1$。不能把这些角色在较大序上的重复表达计成新的原始导子。

### 3.2 得到的全部八十三个序

通过 (113.8)–(113.10) 完整枚举，得到 $h_K=1$ 的十七个、$h_K=2$ 的十五个，以及 $h_K=6,c=1$ 的五十一个原始序。

$h_K=1$ 的全部非极大序如下；同一行的导子分别取值：

| $D$ | 准确导子 $c$ |
|---:|---|
| 3 | 10, 14, 15, 17, 19, 21 |
| 4 | 9, 11, 13 |
| 7 | 5 |
| 8 | 5, 9 |
| 11 | 9 |
| 19 | 7 |
| 43 | 5 |
| 67 | 5 |
| 163 | 5 |

$h_K=2$ 的全部非极大序可写成两个列表：
$$
\begin{aligned}
c=2:\quad D=35,51,91,115,123,187,235,267,403,427,\\
c=3:\quad D=15,24,51,123,267.
\end{aligned} \tag{113.11}
$$
$h_K=6,c=1$ 的全部基本判别式绝对值为
$$
\begin{gathered}
87,104,116,152,212,244,247,339,411,424,436,451,472,515,628,\\
707,771,808,835,843,856,1048,1059,1099,1108,1147,1192,1203,\\
1219,1267,1315,1347,1363,1432,1563,1588,1603,1843,1915,1963,\\
2227,2283,2443,2515,2563,2787,2923,3235,3427,3523,3763.
\end{gathered} \tag{113.12}
$$
最大的序判别式绝对值为 $4075=163\cdot5^2$。每个序的六个完整约化型及环类数公式核对记录都在证书中。

## 4. 四个整数条件，把所有素数变成有限问题

写
$$
H_{-M}(X)=X^6+a_5X^5+a_4X^4+a_3X^3+a_2X^2+a_1X+a_0,
\qquad U=a_5,\quad V=3a_4-U^2.
$$
在任意特征不为三的域中，若 $H_{-M}=Q^3$ 且 $Q$ 首一二次，则比较最高两项强迫
$$Q(X)=X^2+\frac U3 X+\frac V9.$$
继续比较其余四项，得到
$$
\begin{aligned}
B_{M,3}&=27a_3-U^3-6UV,\\
B_{M,2}&=27a_2-V^2-U^2V,\\
B_{M,1}&=81a_1-UV^2,\\
B_{M,0}&=729a_0-V^3.
\end{aligned} \tag{113.13}
$$
因此对 $p>3$，
$$
\boxed{
H_{-M}\bmod p\text{ 为首一二次式的立方}
\quad\Longleftrightarrow\quad
p\mid G_M,
\qquad G_M=\gcd_{0\le i\le3} B_{M,i}.
} \tag{113.14}
$$
这里 $G_M>0$：若四个整数皆为零，则特征零的类多项式会有重根，与六个不同 CM 理想类对应不同复 $j$ 不变量矛盾。具体整数计算也逐项验证 $G_M>0$。

这一步在寻找素数之前就给一个非零整数，所以可以真正覆盖任意大的 $p$，无需取一个人为的素数窗口。三个模九排除也不依赖任何大小比较。

## 5. 严格类多项式认证及完整因子分解

每个 primitive 约化型 $(a,b,d)$ 满足
$$b^2-4ad=-M,\quad |b|\le a\le d,\quad
\gcd(a,b,d)=1,$$
边界 $|b|=a$ 或 $a=d$ 时取 $b\ge0$。界 $a\le\sqrt{M/3}$ 保证枚举完整。计算
$$
H_{-M}(X)=\prod_{[a,b,d]}
\left(X-j\left(\frac{-b+i\sqrt M}{2a}\right)\right).
$$
2048 位 Arb 复数球包住每个系数。每个系数的实部球含唯一整数且半径小于 $2^{-200}$，虚部球含零且绝对值上界小于 $2^{-200}$。复乘理论给这些系数本来属于 $\mathbb Z$，所以所隔离的整数就是准确系数，而非浮点近似取整。

随后完全使用整数算术求 (113.13) 和 $G_M$。程序对不超过一百的素数逐个试除，并强制核验最终余因子恰为一。故没有遗留一个可能带来更大素数的余因子；实际全部素因子都不超过五十三。这一完备性断言是计算的一部分。

在所有八十三个序上，同时保留
$$p>37,\qquad p\nmid M,\qquad\chi_K(p)=-1,$$
准确得到且仅得到以下三个**立方化候选**：

| $M=D$ | $p$ | $G_M$ 的完整分解 | $Q(X)\bmod p$ | $p\bmod9$ |
|---:|---:|---|---|---:|
| 707 | 53 | $2^{46}5^9 7^3 13^3 53^2$ | $X^2+50X+39$ | 8 |
| 1432 | 43 | $2^{34}3^{18}5^9 7^6 13^3 43^2$ | $X^2+19X+16$ | 7 |
| 2443 | 43 | $2^{49}3^{23}5^9 7^4 43^2$ | $X^2+19X+16$ | 7 |

程序另以独立的多项式乘法核对三个 $Q^3$ 的七个模 $p$ 系数。其余八十个序没有合条件的素因子；它们的完整 $G_M$ 和素数幂分解均保存在证书。

此外，独立运行 PARI/GP 的类多项式算法重新计算全部八十三个六次多项式，逐系数与 Arb 隔离出的整数比较，八十三个全部一致。这个比较不代替严格球认证，但提供了不同算法的交叉核验。

现在 (113.6) 与 (113.14) 给定理 113.1 的必要候选表；表中模九余数排除所有 $p\equiv2,5\pmod9$，再由 (113.7) 得到非消失结论。推论 113.2 随即由 R66 得证。

## 6. 文件、复算与结论的准确含义

- [完整验证器](../scripts/verify_class_number_six_periods.py)：重新枚举全部二次域、导子、约化型，严格计算所有类多项式和完整因子分解。
- [整数证书](../scripts/data/class_number_six_periods.json)：130292 字节；SHA256 为
  **1d8988a8eed9f6ffd6a5fee8fa3b48b7a73f9332bcf8acf4e82eb89d4494fa1f**。
- [独立 PARI/GP 计算](../scripts/class_number_six_polynomials.gp)：输出全部八十三个准确多项式，常数项在前。

在仓库根目录复算：

~~~sh
python3 -B topics/serre-uniformity/scripts/verify_class_number_six_periods.py
gp -q -s 268435456 topics/serre-uniformity/scripts/class_number_six_polynomials.gp
~~~

验证器依赖 python-flint/Arb，不使用 Sage、PARI 的浮点近似、GRH、概率素数测试或未认证类数数据库。PARI 文件是另外的独立复核入口。

本结果关闭的是**实际小惯性分支中环类数恰为六的周期共同消失**。它不是通过将相同局部窗口继续扩大来获得，而是先用完整分类和非零整数式把所有素数同时包含进来。一般更高环类数下，三个颜色的每个纤维可以有更多元素，类多项式的必要立方关系仍成立，但不能直接套用本篇的六次系数表或有限序清单。

## 原始来源

1. M. Watkins, *Class numbers of imaginary quadratic fields*, Mathematics of Computation **73** (2004), no. 246, 907–938，DOI [10.1090/S0025-5718-03-01517-5](https://doi.org/10.1090/S0025-5718-03-01517-5)；[作者全文](https://magma.maths.usyd.edu.au/~watkins/papers/smallcn.pdf)，作者 PDF 第23页的末表列出 $h_K=1,2,3,6$ 的完整数量和最大判别式。此处只引已发表的全局完备性，所有有限清单与多项式均另算。
2. L. Cai, J. Shu, Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra & Number Theory **8** (2014), 2523–2572，[期刊全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)，Theorem 1.2 及其前的 Brandt 模和正定配对定义；同一精确接口见 [R90 §2](R90-class-number-three-periods-and-actual-frobenius-exclusions.md)。
3. J. Voight, *Quaternion Algebras*, Springer, 2021，[第42章](https://link.springer.com/chapter/10.1007/978-3-030-56694-4_42)：右理想类、超奇异椭圆曲线及 Deuring 对应。非极大序最优性和基准序传输亦见 R80、R90。
4. [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际原始三次角色及 $p\equiv2,5\bmod9$；[R90](R90-class-number-three-periods-and-actual-frobenius-exclusions.md)：环类数三的实际非消失；[R109](R109-four-small-level-integral-points-by-complete-real-covers.md)：四小层的完整整点分类。
5. [FLINT 模函数接口](https://flintlib.org/doc/acb_modular/index.html)及 [python-flint 复数球](https://python-flint.readthedocs.io/en/latest/acb.html)：严格包围和唯一整数隔离的计算入口。
