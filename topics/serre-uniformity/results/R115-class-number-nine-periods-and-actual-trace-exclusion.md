# R115：环类数九的全部素数覆盖，以及实际小惯性周期非消失

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明，附完整严格证书。** 本篇安全地枚举所有环类数九的序，不预先把类群当成循环群，也不错误沿用 R113 的 $C_6$ 原始性判据。类多项式的必要立方条件把所有素数同时压到有限表；两个准确的 $C_9$ 判定和最后一条实际 Frobenius 迹矛盾完成排除。

## 1. 主结论和覆盖范围

设 $E/\mathbb Q$ 是本课题的实际曲线，$p>37$，满足
$$
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p),\qquad
\bar\rho_{E,p}(I_p)=C^3.
$$
令 $K$ 为正规化子商二次域，$D=|D_K|$；令 $\eta$ 为 R66 的实际原始三次角色，准确环类导子为 $c$，并写
$$M=Dc^2,\qquad \mathcal O_c=\mathbb Z+c\mathcal O_K.$$

**定理 115.1。** 若 $h(\mathcal O_c)=9$，则
$$
\boxed{P_\eta\ne0,\qquad
\exists g\in S_2(\Gamma_0(p))^{\rm new}:
L(\tfrac12,\pi_{g,K}\otimes\eta)\ne0.} \tag{115.1}
$$
本结论覆盖全部 $p>37$，不假设 $j(E)$ 整，不要求 $M<3p$，也不限制其他坏素数支撑。

结合 R90、R113，实际小惯性分支若全部相应三次中心值共同为零，就必须满足
$$\boxed{h(\mathcal O_c)\ge12.} \tag{115.2}$$
这里 $3\mid h(\mathcal O_c)$ 来自非平凡三次角色的存在。

更精确的中间结论如下。对任意虚二次序 $\mathcal O_c$，假设 $h(\mathcal O_c)=9$，$\eta$ 为准确导子 $c$ 的原始三阶角色，$p>37$ 惰性于 $K$ 且 $p\nmid M$。若进一步
$$p\equiv2,5\pmod9,\qquad P_\eta=0,$$
则唯一未被一般类域条件排除的候选是
$$\boxed{D=M=5443,\quad c=1,\quad p=83.} \tag{115.3}$$
本文不声称这个候选对的周期确实为零。定理 115.1 的最后一步使用实际椭圆曲线条件把该候选排除。

在四层 $p=41,47,59,83$，还可接 R92、R69/R72、R109，排除实际环类数九的整个小惯性分支。一般层的 exceptional 分母、更大环类数及完整 Cartan 惯性，不由本篇关闭。

## 2. 任意三次核都给一个必要的立方关系

类群阶为九时，群结构可能是
$$C_9\quad\text{或}\quad C_3\times C_3.$$
任一非平凡三次角色的核都有三个元素，三种颜色 $1,\zeta_3,\zeta_3^2$ 各有三个类。

使用 R90 §2、R113 §2 已核的最优 CM 约化及 Deuring **右理想类**对应。任意超奇异 $j$ 纤维中的三色计数为 $n_0,n_1,n_2$；对应周期系数为零，当且仅当三者相等。因此，周期共同为零迫使每个非空约化纤维的大小为三、六或九。

对完整类多项式
$$
H_{-M}(X)=\prod_{[\mathfrak a]\in\operatorname{Pic}(\mathcal O_c)}
(X-j(\mathfrak a))\in\mathbb Z[X],
$$
这给
$$
\boxed{P_\eta=0\quad\Longrightarrow\quad
H_{-M}(X)\bmod p=Q(X)^3
\text{，其中 }Q\in\mathbb F_p[X]\text{ 首一三次}.} \tag{115.4}
$$
首一立方根的唯一性保证它被 Frobenius 保持，故系数在 $\mathbb F_p$。本篇只使用这个方向，不把一个大小为三的根纤维自动当成三色平衡纤维。

这一必要条件对两种类群结构、每一个三次角色都成立。若某个角色其实降至更小导子，把它纳入后续有限计算也只会扩大候选集，不会漏掉真正的原始角色。

同样，由 $\sum\eta=0$ 及完整 Brandt 尖点谱，Cai–Shu–Tian Theorem 1.2 给
$$
P_\eta=0\quad\Longleftrightarrow\quad
L(\tfrac12,\pi_{g,K}\otimes\eta)=0
\text{ 对所有层 }p\text{ 的权二新形式 }g. \tag{115.5}
$$
非极大序最优性、不同基准序之间的传输以及非零归一化因子，均与 R90/R113 的已证接口相同。

## 3. 全部五十五个环类数九序：不预筛群结构

自然满射 $\operatorname{Pic}(\mathcal O_c)\twoheadrightarrow\operatorname{Cl}(\mathcal O_K)$ 迫使
$$h_K\in\{1,3,9\}.$$
Watkins 的已发表无条件分类给

| $h_K$ | 基本判别式绝对值最大值 | 域的数量 |
|---:|---:|---:|
| 1 | 163 | 9 |
| 3 | 907 | 16 |
| 9 | 10627 | 34 |

这些是全局完备界；区间内的基本判别式和类数由本篇重新枚举 primitive 约化正定二元型得到。

对 $c>1$，令 $u_K=[\mathcal O_K^\times:\{\pm1\}]\le3$。环类数公式给
$$
9=\frac{h_Kc}{u_K}\prod_{q\mid c}
\left(1-\frac{\chi_K(q)}q\right),
$$
所以
$$
\varphi(c)\le\frac{9u_K}{h_K}\le27,\qquad
\varphi(c)^2\ge c/2,
\qquad\boxed{c\le1458.} \tag{115.6}
$$
后一初等下界的逐素数证明见 R113 §3。本界不是经验截断，也不依赖原始性。

完整枚举得到五十五个序，其中：

- $h_K=1$：$D=3$，$c=18,27$，共两个。
- $h_K=3$：$c=2$，且
  $$D=59,83,107,139,211,283,307,331,379,499,547,643,883,907,$$
  共十四个。
- $h_K=9$：下面三十四个域的极大序，以及 $c=2$、$D=199,367,823,1087,1423$ 的五个非极大序，共三十九个。

三十四个 $h_K=9$ 的基本判别式绝对值为
$$
\begin{gathered}
199,367,419,491,563,823,1087,1187,1291,1423,1579,2003,2803,\\
3163,3259,3307,3547,3643,4027,4243,4363,4483,4723,4987,5443,\\
6043,6427,6763,6883,7723,8563,8803,9067,10627.
\end{gathered} \tag{115.7}
$$
每个序的全部九个约化型都在证书中，且类数公式与型数逐项相等。

特别，本列表**故意保留可能不原始的导子表达**。在 $C_9$ 中唯一的三次商可能已从较小类群拉回；在 $C_3\times C_3$ 中，则可能只有一部分三次角色拉回。不能单凭某个真因子导子的类数被三整除，就删除这个序的所有三次角色。本篇没有作这种删除。

## 4. 六个准确整数条件，覆盖任意大的素数

写
$$H_{-M}(X)=X^9+a_8X^8+\cdots+a_0.$$
若它是首一三次式的立方，比较最高三项强迫
$$
u=\frac{a_8}{3},\qquad
v=\frac{a_7}{3}-u^2,\qquad
w=\frac{a_6-u^3-6uv}{3},
$$
$$Q_0(X)=X^3+uX^2+vX+w. \tag{115.8}
$$
$u,v,w$ 的分母都是三的幂。写
$$
H_{-M}(X)-Q_0(X)^3=\sum_{i=0}^{5}r_iX^i,
\qquad r_i\in\mathbb Z[1/3],
$$
并令 $b_i$ 为每个 $r_i$ 约成既约分数后的分子。定义
$$G_M=\gcd(b_0,\ldots,b_5)>0.$$
正性来自特征零类多项式无重根：所有 $b_i$ 不可能同时为零。具体计算还逐项核验了正性。

对任何 $p>3$，分母都可逆，因此
$$
\boxed{
H_{-M}\bmod p\text{ 为首一三次式的立方}
\quad\Longleftrightarrow\quad p\mid G_M.
} \tag{115.9}
$$
这里在确定 $p$ 之前，已经得到固定非零整数 $G_M$。所以后续完整因子分解真正覆盖所有素数，而非只扫描某个小素数区间。

## 5. 严格计算及全部立方化候选

对每个 $M$，使用全部 primitive 约化型
$$
H_{-M}(X)=\prod_{[a,b,d]}
\left(X-j\left(\frac{-b+i\sqrt M}{2a}\right)\right).
$$
4096 位 Arb 复数球包住每个系数。每个系数的实部球隔离唯一整数，半径小于 $2^{-200}$；虚部球含零且绝对值上界小于 $2^{-200}$。复乘理论给系数属于 $\mathbb Z$，故隔离出的整数是准确系数。

随后对 (115.8) 和六个残差仅作准确分数及整数运算。每个分母都验证只含素因子三；每个 $G_M$ 都以不超过一百的素数逐个试除，最后严格断言余因子为一。因此不存在未经证明的更大余因子；所有实际因子都不超过八十三。

在五十五个序上，同时要求 $p>37$、$p\nmid M$、$\chi_K(p)=-1$，得到以下完整必要候选表：

| $M$ | $D$ | $c$ | 所有惰性立方化候选 $p>37$ | 其中 $p\equiv2,5\bmod9$ |
|---:|---:|---:|---|---|
| 1291 | 1291 | 1 | 43 | 无 |
| 1423 | 1423 | 1 | 43 | 无 |
| 1516 | 379 | 2 | 43 | 无 |
| 2572 | 643 | 2 | 41 | 41 |
| 3163 | 3163 | 1 | 43 | 无 |
| 3532 | 883 | 2 | 47, 59 | 47, 59 |
| 3643 | 3643 | 1 | 61 | 无 |
| 4483 | 4483 | 1 | 61 | 无 |
| 5443 | 5443 | 1 | 83 | 83 |
| 5692 | 1423 | 2 | 43 | 无 |
| 8563 | 8563 | 1 | 43 | 无 |

表外四十四个序没有合条件的素因子。表内每个候选另以独立多项式乘法检查其首一三次立方根的十个系数。这里仍未把立方化称为周期消失的充分条件。

全表的类多项式、分数立方根、六个准确残差、完整 $G_M$ 分解和全部模 $p$ 立方根都在 JSON 证书中。独立 PARI/GP 类多项式计算也已实际完成，五十五个九次多项式逐系数与 Arb 认证整数一致。

R66 的实际小惯性条件现在只留下
$$
\boxed{(D,c,p)=(643,2,41),(883,2,47),(883,2,59),(5443,1,83).} \tag{115.10}
$$

## 6. 两个真实 $C_9$ 类群，使前三个导子不可能原始

下面只对两个具体序证明循环性，不对其余类数九序作推断。

### 6.1 $D=643,c=2$

此时 $h_K=3$，$h(\mathcal O_2)=9$，且
$$\mathcal O_2=\mathbb Z[\sqrt{-643}].$$
素数七分裂，并与判别式及导子互素；例如
$$\mathfrak q=(7,\sqrt{-643}-1)$$
是范数七的可逆素理想。

若 $[\mathfrak q]^3=1$，则 $\mathfrak q^3=\alpha\mathcal O_2$。由于该理想包含于 $\mathcal O_2$，必有 $\alpha\in\mathcal O_2$；主理想的格指数等于 $|N\alpha|$，故
$$\alpha=x+y\sqrt{-643},\qquad x^2+643y^2=7^3=343.$$
若 $y\ne0$，左边至少为643；若 $y=0$，343不是平方。因此没有这样的生成元。

群阶为九而 $[\mathfrak q]^3\ne1$，故 $[\mathfrak q]$ 阶恰为九，
$$\operatorname{Pic}(\mathcal O_2)\simeq C_9. \tag{115.11}$$

### 6.2 $D=883,c=2$

同样有 $h_K=3$、$h(\mathcal O_2)=9$ 和
$$\mathcal O_2=\mathbb Z[\sqrt{-883}].$$
取范数十三的可逆分裂素理想
$$\mathfrak q=(13,\sqrt{-883}-1).$$
若其三次方主，则存在
$$x^2+883y^2=13^3=2197.$$
此时 $|y|\le1$；$y=0$ 或 $|y|=1$ 分别要求 $x^2=2197$ 或 $x^2=1314$，两者都不是平方。故此类也阶九，
$$\operatorname{Pic}(\mathcal O_2)\simeq C_9. \tag{115.12}$$

### 6.3 原始性的结论

两个例子中，自然满射
$$
\operatorname{Pic}(\mathcal O_2)\simeq C_9
\twoheadrightarrow\operatorname{Cl}(\mathcal O_K)\simeq C_3
$$
的核都是唯一的阶三子群。任何非平凡三次角色的核也恰是这个子群，所以它必经 $\operatorname{Cl}(\mathcal O_K)$ 分解，准确导子为一。

因此 $(D,c)=(643,2)$ 与 $(883,2)$ **没有任何准确导子二的三次角色**。这与 R66 中 $c$ 已定义为实际角色的原始导子矛盾，排除 (115.10) 的前三对。这一步不是仅凭目标类数被三整除，而是先明确证明源群是 $C_9$。

## 7. 最后 $(5443,83)$：真实整数迹在二十三处矛盾

现在设实际曲线给
$$D=5443,\quad c=1,\quad p=83.$$
素数 $q=23$ 在 $K$ 分裂，且
$$
\alpha=82+\sqrt{-5443},\qquad
N_{K/\mathbb Q}(\alpha)=82^2+5443=12167=23^3.
$$
两个坐标不同时被23整除，故 $(\alpha)$ 只支撑在23上方的一支，即可选
$$\mathfrak q^3=(\alpha). \tag{115.13}$$

令 $\lambda:G_K\to\mathbb F_{83^2}^\times$ 为实际 Cartan 特征，$\mu=\lambda^{12}$。R63 给准确主理想公式
$$\mu((\alpha))=\widetilde\alpha^{12}. \tag{115.14}$$
由于23在 $K$ 分裂，局部残余像在 Cartan。潜在乘法约化会强迫 $23\equiv1\pmod{83}$，这是不可能的。R63 的局部构造因而给一个循环总分歧好约化扩张，其剩余域仍为 $\mathbb F_{23}$。

在该实际好约化上，存在真正的整数迹 $a$ 和 Frobenius 根 $\beta$，满足
$$
|a|\le2\sqrt{23}<10,\quad
\beta+\beta^{83}=a,\quad
\beta^{84}=23,\quad
\beta^{12}=\mu(\mathfrak q).
$$
这里的迹不是任意模83元素，也没有假设原曲线在23处已经好约化。由 (115.13)–(115.14)，
$$\beta^{36}=\widetilde\alpha^{12}.$$
换二次方向只共轭该等式，不改变下一步的迹。

记整数递推
$$
S_0(t,n)=2,\quad S_1(t,n)=t,\quad
S_{r+1}(t,n)=tS_r(t,n)-nS_{r-1}(t,n).
$$
若两根的迹为 $t$、范数为 $n$，则 $S_r$ 为它们 $r$ 次幂之和。取二次迹得到必要条件
$$
\boxed{S_{36}(a,23)\equiv
S_{12}(164,23^3)\pmod{83}.} \tag{115.15}
$$
右边准确为80。左边在 $a=0,1,\ldots,9$ 时依次为
$$
\boxed{66,\ 78,\ 53,\ 66,\ 27,\ 4,\ 12,\ 21,\ 81,\ 55.} \tag{115.16}
$$
没有80；又 $S_{36}$ 关于 $a$ 是偶函数，因此已经覆盖全部负迹。实际椭圆曲线所需的整数迹不存在，最后候选被排除。

结合 (115.4)、全部素因子的完整性、§6 的原始性及 (115.15) 的实际矛盾，定理 115.1 得证。

## 8. 证书及复算

- [完整验证器](../scripts/verify_class_number_nine_periods.py)。
- [全部整数证书](../scripts/data/class_number_nine_periods.json)：254987 字节，SHA256 为
  **84fef5fd77a975ed1c492ee464615d15954b8683798707102eb4f86a68d2c5da**。
- [独立 PARI/GP 类多项式计算](../scripts/class_number_nine_polynomials.gp)。

在仓库根目录运行：

~~~sh
python3 -B topics/serre-uniformity/scripts/verify_class_number_nine_periods.py
gp -q -s 268435456 topics/serre-uniformity/scripts/class_number_nine_polynomials.gp
~~~

验证器依赖 python-flint/Arb，并复用 R113 的基本判别式、约化型和环类数公式等准确整数函数。多项式、立方根、六个残差、完整分解、两个无范数生成元的类群证明，以及最后十个实际迹值，都重新计算并与保存证书核对。独立 GP 文件另行计算全部五十五个多项式，已逐项比较一致。

这完成的是环类数九的实际周期共同零问题。它没有把抽象类域数据视作实际椭圆曲线，也没有把一般类群中的一个三次角色与某条曲线的真实整数迹脱开使用。剩余共同零分支已被推进到环类数至少十二。

## 原始来源与已核接口

1. M. Watkins, *Class numbers of imaginary quadratic fields*, Mathematics of Computation **73** (2004), no.246, 907–938，DOI [10.1090/S0025-5718-03-01517-5](https://doi.org/10.1090/S0025-5718-03-01517-5)；[作者全文](https://magma.maths.usyd.edu.au/~watkins/papers/smallcn.pdf)，作者 PDF 第23页末表，尤其 $h_K=9$ 的34个域和最大判别式10627。本篇只引用其已发表全局完备性。
2. L. Cai, J. Shu, Y. Tian, *Explicit Gross–Zagier and Waldspurger formulae*, Algebra & Number Theory **8** (2014), 2523–2572，[Theorem 1.2 的期刊全文](https://msp.org/ant/2014/8-10/ant-v8-n10-p05-p.pdf)；Deuring 对应及周期共同零等价的准确应用见 [R90 §2](R90-class-number-three-periods-and-actual-frobenius-exclusions.md) 和 [R113 §2](R113-class-number-six-cubic-period-nonvanishing.md)。
3. [R63](R63-all-prime-classes-and-quotient-discriminant-growth.md) §§2–3：$\lambda^{12}$ 主理想公式、分裂素数处潜在乘法的必要同余、保持剩余域的循环总分歧好约化扩张及实际整数迹。
4. [R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际小惯性 $p\equiv2,5\bmod9$ 与准确原始三次导子；[R109](R109-four-small-level-integral-points-by-complete-real-covers.md)：四小层整点分类，供额外排除推论使用。
