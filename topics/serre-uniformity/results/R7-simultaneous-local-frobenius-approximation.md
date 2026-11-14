# R7. Tate 条件、候选二次特征及任意有限 Frobenius 窗口可以同时满足

**状态：已证明。** 此结果严格限制一种从必要局部条件推出统一界的路线。下面同时安排一个窗口以外的检测素数，证明构造曲线的全局模 $p$ 像为整个 $\mathrm{GL}_2(\mathbb F_p)$。

日期：2026-11-12。会话：serre-uniformity-astra / frobenius。

## 1. 陈述与范围

令 $p>37$ 为素数，满足 $p\equiv3\pmod4$；令 $X\ge p$ 为任意实数。令 $\chi_{-4}$ 为 $\mathbb Q(i)/\mathbb Q$ 的二次特征。

**定理。** 存在素数 $r>X$、$r\equiv1\pmod{4p}$，一个辅助素数 $\ell>X$，以及无穷多两两具有不同 $j$ 不变量的无 CM 椭圆曲线 $E/\mathbb Q$，满足以下全部性质。

1. $j(E)=a/r^p$，其中 $a\in\mathbb Z$、$a\equiv1\pmod r$。特别地，$r$ 是唯一的负 $j$ 赋值素数，且
   $$
   v_r(j(E))=-p,\qquad r\equiv1\pmod p.
   $$
2. $r$ 处的 Tate 参数 $\tau_r$ 属于 $(\mathbb Q_r^\times)^p$；因此 $E[p]$ 在 $G_{\mathbb Q_r}$ 上的像由标量组成。这包括了 Tate 参数的单位部分条件，远强于只检查赋值被 $p$ 整除。
3. $v_2(j(E))=6$。因此，按 Zywina 的 $\varepsilon$ 分歧支集必要条件，$\chi_{-4}$ 是允许的候选特征：它在 $p$ 及所有不属于允许支集的素数处均不分歧。另有
   $$
   \chi_{-4}(p)=-1,\qquad \chi_{-4}(r)=1\equiv r\pmod p.
   $$
4. 对每个奇素数 $q\le X$，$E$ 有良好约化，而且其约化同构于
   $$
   E_0/\mathbb F_q:\ y^2=x^3-x.
   $$
   故每个 $q\le X$、$q\equiv3\pmod4$ 都满足整数等式 $a_q(E)=0$。
5. $E$ 在 $p$ 具有良好超奇异约化，且其实际局部模 $p$ 像是完整的非分裂 Cartan 正规化子：
   $$
   \bar\rho_{E,p}(G_{\mathbb Q_p})\simeq N_{\rm ns}(p).
   $$
6. 对每个奇素数 $q\le X$、$q\ne p$，其 Frobenius 特征多项式模 $p$ 都与一个全局像在 $N_{\rm ns}(p)$ 中、商特征为 $\chi_{-4}$ 的表示相符。固定 $p,X,r$ 后，上述曲线的高度 $h(j(E))$ 无界。
7. $\ell\equiv2\pmod p$、$\ell\equiv11\pmod{12}$；$E$ 在 $\ell$ 良好约化且 $a_\ell(E)=3$。其全局像满足
   $$
   \bar\rho_{E,p}(G_{\mathbb Q})=\mathrm{GL}_2(\mathbb F_p).
   $$
   特别地，若 $q_{\rm nz}$ 是最小的 $\chi_{-4}$ 惰性、好约化且非零迹素数，则
   $$
   X<q_{\rm nz}(E,\chi_{-4})\le\ell.
   $$

于是，即使把窗口取为 $X=p^2$，以上全部必要局部条件也不能保证在 $q<p^2/4$ 找到一个 $\chi_{-4}$ 惰性且 $a_q(E)\ne0$ 的好素数。更不能仅凭这些条件给 $h(j)$ 一个只依赖 $p$ 的上界。

这些曲线提供了已证明全局满射的实例，同时通过任意预先指定的有限检测窗口。局部基的选择不提供一个同时适用于全局所有 Galois 元素的 Cartan；窗口之外的 $\ell$ 正好检出这种失败。除明示条件外，其他坏素数处的所有剩余必要条件也未被声称已经解决。

## 2. 选择一个有理 $j$ 不变量

由 Dirichlet 算术级数素数定理，选择素数
$$
r>X,\qquad r\equiv1\pmod{4p}.
$$
再由同一定理选择
$$
\ell>X,\qquad\ell\equiv2\pmod p,\qquad\ell\equiv11\pmod{12}.
$$
两项同余相容且给出模 $12p$ 的既约剩余类；$r\ne\ell$，因为二者模 $p$ 的剩余类不同。

Waterhouse 的 Theorem 4.1(1) 保证存在 $E_*/\mathbb F_\ell$，使 $a_\ell(E_*)=3$：其条件为 $|3|<2\sqrt\ell$ 且 $\gcd(3,\ell)=1$，在此均满足。这个同源类普通。并且 $j_*=j(E_*)$ 不等于 $0$ 或 $1728$：

- 若 $j_*=0$，曲线可写成 $y^2=x^3+B$。因 $\ell\equiv2\pmod3$，立方映射是 $\mathbb F_\ell$ 上的置换，直接计数得到 $a_\ell=0$。
- 若 $j_*=1728$，曲线可写成 $y^2=x^3+Ax$，具有有理 $2$ 挠点 $(0,0)$，所以 $\#E_*(\mathbb F_\ell)$ 是偶数，$a_\ell$ 也为偶数。

两种情况都与 $a_\ell=3$ 矛盾。

令 $S=\{q:q\le X,\ q\text{ 为奇素数}\}$。对每个 $q\in S$ 定义
$$
j_q=\frac{6912}{4-27q^2}.
$$
这是局部曲线 $y^2=x^3-x+q$ 的 $j$ 不变量，且此曲线模 $q$ 的约化等于 $E_0$。若 $q\ge5$，则 $j_q$ 为 $q$ 进单位；若 $q=3$，则 $v_3(j_3)=3$。

对整数 $a$ 施加以下两两互素模数的同余条件：
$$
\begin{aligned}
a&\equiv1&&\pmod r,\\
a&\equiv1728r^p&&\pmod{2^7},\\
a&\equiv r^p j_3&&\pmod{3^9},\\
a&\equiv r^p j_q&&\pmod{q^3}\qquad(q\in S,\ q\ge5),\\
a&\equiv r^p j_*&&\pmod\ell.
\end{aligned}
$$
右端的有理数在相应局部环中都是整的；其分母均是模数的单位，所以这些是通常意义下的整数同余。

中国剩余定理给出一个非空算术级数的解。取其中任意足够大的正解，并设
$$
j=\frac a{r^p}.
$$
则 $\gcd(a,r)=1$，故 $j$ 的约分后分母正好是 $r^p$；同时 $j\ne0,1728$。在 $2$ 处，
$$
j\equiv1728\pmod{2^7}
$$
蕴含 $v_2(j)=6$。在其他指定素数处，
$$
v_q(j-j_q)\ge3\ (q\ge5),\qquad v_3(j-j_3)\ge9.
$$
沿此算术级数令 $a\to+\infty$，$j$ 两两不同，且 $h(j)=\log\max\{a,r^p\}\to+\infty$。

## 3. 为什么这些同余真的给出所需好约化模型

必须验证局部椭圆曲线，而不能仅用“$j\equiv1728\pmod q$”代替好约化。

定义有理函数
$$
s(z)=\frac4{27}\left(1-\frac{1728}{z}\right)
=\frac4{27}-\frac{256}{z}.
$$
由定义 $s(j_q)=q^2$，并有精确恒等式
$$
s(j)-q^2=\frac{256(j-j_q)}{j j_q}.
$$

当 $q\ge5$ 时，$j,j_q$ 都是 $q$ 进单位，因而
$$
v_q(s(j)-q^2)\ge3.
$$
当 $q=3$ 时，所选同余保证 $v_3(j)=v_3(j_3)=3$；因此
$$
v_3(s(j)-9)\ge9-3-3=3.
$$
所以对每个 $q\in S$ 均有
$$
s(j)=q^2 u_q,\qquad u_q\in1+q\mathbb Z_q.
$$
因为 $q$ 为奇数，Hensel 引理应用于 $T^2-u_q$ 在 $T=1$ 的单根，给出 $u_q$ 在 $1+q\mathbb Z_q$ 中的平方根。令
$$
b_q=q\sqrt{u_q}\in q\mathbb Z_q^\times.
$$
则 $b_q^2=s(j)$，局部曲线
$$
F_q:\ y^2=x^3-x+b_q
$$
的 $j$ 不变量等于 $j$。其判别式模 $q$ 等于 $64\ne0$，故它是良好约化模型，且约化确实为 $E_0$。

此处 $q=3$ 需要模 $3^9$ 的同余，原因是 $s(z)$ 中的分母在该点损失了 $6$ 个 $3$ 进精度；模 $3^3$ 不足以支持这一论证。

在辅助素数 $\ell$ 处，取 $E_*$ 的短 Weierstrass 方程 $y^2=x^3+\bar A_*x+\bar B_*$。由 $j_*\ne0,1728$，$\bar A_*,\bar B_*$ 都非零。取 $A_*\in\mathbb Z_\ell^\times$ 为 $\bar A_*$ 的提升。因为 $j\equiv j_*\pmod\ell$，
$$
\frac{4A_*^3}{27}\left(\frac{1728}{j}-1\right)
\equiv\bar B_*^2\pmod\ell.
$$
Hensel 引理给出 $B_\ell\in\mathbb Z_\ell^\times$，其平方等于左侧且 $B_\ell\equiv\bar B_*\pmod\ell$。于是
$$
F_\ell:y^2=x^3+A_*x+B_\ell
$$
的 $j$ 不变量为 $j$，且其良好约化正是 $E_*$。

## 4. 一个全局二次扭曲同时实现所有局部模型

先取显式有理模型
$$
k=\frac j{j-1728},\qquad
E_j:\ y^2=x^3-3kx-2k.
$$
直接代入 $j$ 公式可知 $j(E_j)=j$。记 $A=-3k$、$B=-2k$。

对每个 $q\in S$，令
$$
d_q=-\frac32 b_q\in\mathbb Q_q^\times.
$$
由于 $b_q^2=4/(27k)$，有
$$
A d_q^2=-1,\qquad B d_q^3=b_q.
$$
因此按约定
$$
E_j^{(d)}:\ y^2=x^3+A d^2x+B d^3,
$$
局部曲线 $E_j^{(d_q)}$ 恰好就是 $F_q$。

在 $\ell$ 处，令
$$
d_\ell=\frac{B_\ell A}{B A_*}.
$$
两条曲线的 $j$ 相同，故 $v^2=u^3$，其中 $u=A_*/A$、$v=B_\ell/B$。于是 $d_\ell=v/u$ 满足 $d_\ell^2=u$、$d_\ell^3=v$，所以 $E_j^{(d_\ell)}=F_\ell$。

现在完整说明所需弱逼近只涉及有限个平方类。令 $T=S\cup\{\ell\}$，对每个 $q\in T$ 写
$$
d_q=q^{n_q}v_q,\qquad v_q\in\mathbb Z_q^\times,
$$
令 $e_q\in\{0,1\}$ 与 $n_q$ 同奇偶，并置 $D_0=\prod_{q\in T}q^{e_q}$。选择正整数 $u$，对每个 $q\in T$ 满足
$$
u\equiv v_q\left(D_0/q^{e_q}\right)^{-1}\pmod q.
$$
所有右端非零，CRT 给出这样的 $u$，且 $u$ 与 $\prod_{q\in T}q$ 互素。令 $d=D_0u$。则
$$
\frac d{d_q}=q^{e_q-n_q}\cdot
\frac{(D_0/q^{e_q})u}{v_q}
$$
中第一因子为偶数次幂，第二因子属于 $1+q\mathbb Z_q$，亦为平方。故 $d/d_q\in(\mathbb Q_q^\times)^2$。

所以全局曲线 $E=E_j^{(d)}$ 在每个 $q\in T$ 的 $\mathbb Q_q$ 上都与 $F_q$ 同构，因而具有所需好约化，包括在 $\ell$ 处的 $a_\ell(E)=3$。具体地，若 $d/d_q=w_q^2$，缩放坐标 $(x,y)\mapsto(w_q^2x,w_q^3y)$ 给出两个扭曲模型间的同构；因此这不是仅在代数闭包上成立的同构。

$j(E)=j$ 的约分后分母为 $r^p>1$，所以 $j(E)$ 不是整数。CM $j$ 为代数整数，故 $E$ 无 CM。无穷多个 $a$ 给出无穷多个不同的 $j(E)$。

## 5. $r$ 处包括单位部分的 Tate 验证

因为 $v_r(j)=-p<0$，$E/\mathbb Q_r$ 是一条 Tate 曲线的至多二次扭曲，令该 Tate 曲线的参数为 $\tau_r$。Tate 的 $j$ 展开及其在无穷尖点的逆展开给出
$$
\tau_r=j^{-1}\bigl(1+O(j^{-1})\bigr).
$$
这里 $j^{-1}=r^p/a$，$a\equiv1\pmod r$，所以
$$
\frac{\tau_r}{r^p}\in1+r\mathbb Z_r.
$$
由于 $r\ne p$，映射 $u\mapsto u^p$ 是 $1+r\mathbb Z_r$ 的自同构；例如对每个 $v\in1+r\mathbb Z_r$，Hensel 引理在 $T=1$ 处解 $T^p-v=0$。因此
$$
\tau_r=(r\eta)^p\qquad\text{对某个 }\eta\in1+r\mathbb Z_r.
$$
又因为 $r\equiv1\pmod p$，$\mu_p\subset\mathbb Q_r$。Tate 曲线的 $p$ 挠点由 $\mu_p$ 与 $\tau_r^{1/p}$ 在 $\overline{\mathbb Q}_r^\times/\tau_r^{\mathbb Z}$ 中生成，二者此时都在 $\mathbb Q_r$ 中。故 Tate 曲线的模 $p$ 表示平凡；原曲线 $E$ 至多差一个二次特征，所以其模 $p$ 局部像由标量 $\pm I$ 组成。

因 $r\equiv1\pmod4$，$\chi_{-4}$ 在 $r$ 局部平凡，与上述标量像的 Cartan 商特征一致。

## 6. 任意长 Frobenius 窗口及 $p$ 处完整局部像

若 $q\in S$、$q\equiv3\pmod4$，则
$$
\sum_{x\in\mathbb F_q}\left(\frac{x^3-x}{q}\right)=0:
$$
变量替换 $x\mapsto-x$ 将和变为其负数。因此 $a_q(E_0)=0$，而第 4 节的局部同构给出 $a_q(E)=0$。

特别地，$p\in S$ 且 $p\equiv3\pmod4$，故 $E$ 在 $p$ 有良好约化且 $a_p(E)=0$。对 $p>3$，这是超奇异约化的标准判据。

使用 Serre 对未分歧基域上良好超奇异约化的惯性定理（原文 §1.11, Proposition 12）：对 $E/\mathbb Q_p$，$\bar\rho_{E,p}(I_p)$ 是一个完整非分裂 Cartan $C$，野惯性像平凡。因为惯性正规于分解群，整个局部像在 $N(C)$ 中。取 $C$ 的非标量元素 $t$ 及算术 Frobenius 提升 $F$，温和惯性关系为
$$
\bar\rho(F)t\bar\rho(F)^{-1}=t^p\ne t.
$$
所以 $\bar\rho(F)\notin C$。局部像既包含 $C$ 又包含其正规化子外陪集中的元素，故恰好等于 $N(C)$。这是**构造曲线的实际局部像**，并非仅一个候选群。

最后说明所有好素数处的 Frobenius 数据为什么与同一个候选全局二次特征相容。对参考曲线 $E_0/\mathbb Q:y^2=x^3-x$，有定义于 $\mathbb Q(i)$ 的自同态
$$
\iota(x,y)=(-x,iy),\qquad\iota^2=[-1].
$$
在 $E_0[p]$ 上，$J=\iota|_{E_0[p]}$ 的最小多项式为 $T^2+1$，因 $p\equiv3\pmod4$ 而不可约。其中心化子为非分裂 Cartan。任意 $g\in G_{\mathbb Q}$ 满足
$$
\bar\rho_{E_0,p}(g)J\bar\rho_{E_0,p}(g)^{-1}
=\chi_{-4}(g)J.
$$
所以 $\bar\rho_{E_0,p}$ 的像在该 Cartan 的正规化子中，商特征正是 $\chi_{-4}$。对所有 $q\in S\setminus\{p\}$，构造曲线与参考曲线的好约化相同，从而 Frobenius 特征多项式相同。这同时验证了迹、行列式以及 Cartan 内外的相容性，而不只验证了一个迹同余。

## 7. 窗口以外的明确检测与全局满射

在 $\ell$ 处，实际 Frobenius 特征多项式模 $p$ 为
$$
T^2-a_\ell(E)T+\ell
\equiv T^2-3T+2=(T-1)(T-2)\pmod p.
$$
它的两个特征值在 $\mathbb F_p$ 中互异，且迹为 $3\ne0$。这种矩阵不在任何非分裂 Cartan 正规化子中：Cartan 内非标量元素的特征多项式不可约，标量元素具有重根；外陪集元素的迹则为零。

为说明全局像确实满射，可以只用 Dickson–Serre 有限子群分类。记全局像为 $G$，它包含第 6 节已证的完整非分裂 Cartan $C$。如果 $G$ 不包含 $\mathrm{SL}_2(\mathbb F_p)$，则分类给出的可能为 Borel、分裂或非分裂 Cartan 的正规化子、射影例外群 $A_4,S_4,A_5$。其中：

- Borel 保持一条直线，而 $C$ 不保持任何 $\mathbb F_p$ 直线。
- $C$ 的射影像含阶 $p+1$ 的元素；分裂 Cartan 正规化子的射影元素阶只能整除 $p-1$ 或等于 $2$，所以它不能包含 $C$。
- $A_4,S_4,A_5$ 的最大元素阶不超过 $5$，而 $p+1>5$。
- 非分裂 Cartan 正规化子已由 $\operatorname{Frob}_\ell$ 排除。

因此 $G$ 包含 $\mathrm{SL}_2(\mathbb F_p)$。Weil 配对使其行列式像为整个 $\mathbb F_p^\times$，故 $G=\mathrm{GL}_2(\mathbb F_p)$。

同时 $\ell\equiv3\pmod4$，所以它是 $\chi_{-4}$ 的惰性素数，且 $a_\ell(E)=3\ne0$。由第 6 节在窗口内的零迹结论，得到
$$
X<q_{\rm nz}(E,\chi_{-4})\le\ell.
$$

此满射论证不使用 Faltings 定理，也不把任何逐素数有限性当成统一有限性。

## 8. 分歧支集必要条件与局限

已知异常非分裂 Cartan 情形的商特征只可能在以下素数处分歧：
$$
S(E)=\{2:v_2(j(E))\in\{3,6,9\}\}
\cup\{q\ge3:v_q(j(E)-1728)>0\text{ 且为奇数}\},
$$
并且在 $p$ 不分歧。构造中 $v_2(j)=6$，故 $2\in S(E)$。$\chi_{-4}$ 只在 $2$ 分歧，于是满足这项必要条件；它在 $p$ 不分歧且取 Frobenius 值 $-1$。

本结论只把该**支集包含条件**作为条件，未把它反过来认作全局异常像的充分条件，也未声称未知的其他坏素数处的完整局部表示已经被匹配。

定理证明完毕。特别地，假如一种论证只使用了本定理列出的条件，却推出“在小于 $p^2/4$ 的惰性好素数中必有非零迹”，则对本构造取 $X=p^2$ 即产生直接矛盾。实际异常子族仍可能满足额外的全局限制；本定理没有排除这种可能。

## 9. 外部已证输入及来源

- Dirichlet 算术级数素数定理：用于选择 $r\equiv1\pmod{4p}$ 以及指定的模 $12p$ 剩余类中的 $\ell$，没有要求有效大小界。
- W. C. Waterhouse, *Abelian varieties over finite fields*, Ann. Sci. École Norm. Sup. (4) **2** (1969), 521–560，Theorem 4.1(1)，p. 536：[原文](https://archive.numdam.org/item/10.24033/asens.1183.pdf)。用于实现在 Hasse 区间内且与特征互素的迹 $3$。
- Hensel 引理及 Tate 曲线理论：Tate 曲线的 $j$ 展开和 $p$ 挠点描述用于第 5 节。
- CM $j$ 的整性：例如 P. Habegger, *Singular moduli that are algebraic units*, Algebra & Number Theory **9** (2015), 1515–1524，[原文](https://msp.org/ant/2015/9-7/ant-v9-n7-p01-s.pdf)，引言记录此标准事实。
- J.-P. Serre, *Propriétés galoisiennes des points d'ordre fini des courbes elliptiques*, Invent. Math. **15** (1972), 259–331，§1.11, Proposition 12（好超奇异惯性），§2.6–2.7、Proposition 17（有限子群分类）：[作者原文存档](https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf)。惯性定理仅用于基域 $\mathbb Q_p$、绝对分歧指数 $1$ 的情形。
- A. Lozano-Robledo, *On the field of definition of $p$-torsion points on elliptic curves over the rationals*, [作者原文](https://alozano.clas.uconn.edu/wp-content/uploads/sites/490/2014/01/lozano-robledo_torsion_bounds_v11.pdf)，Theorem 3.1 及其证明明确定位到上述 Serre 命题，并说明一般分歧基域需额外区分 Newton 多边形情形；本证明没有使用超出未分歧情形的简化断言。
- D. Zywina, *On the surjectivity of mod $\ell$ representations associated to elliptic curves*, [作者原文](https://pi.math.cornell.edu/~zywina/papers/EffectiveModl.pdf)，Lemma 2.3（候选二次特征分歧支集）。
