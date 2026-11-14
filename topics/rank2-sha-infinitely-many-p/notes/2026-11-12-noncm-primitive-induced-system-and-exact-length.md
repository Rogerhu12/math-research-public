# E389 的实际诱导族原始性与准确 Sha 长度

日期：2026-11-12。**已证明。** 本文加强 R139 的上界为等式，
并识别实际剩余族的最小辅助素数数目；没有证明实际点的指数 $a\le1$。

## 1. 对象和结论

固定 R136、R139、R140 的
$$
 E:y^2+y=x^3+x^2-2x,\qquad F=\mathbb Q(\sqrt{-7}).
$$
记 $r=\operatorname{rank}E(\mathbb Q)\ge2$。取充分大的普通素数
$p$，使 $E[p]$ 的像为 $\mathrm{GL}_2(\mathbb F_p)$，并删去
固定参数化的指数、$7\cdot389$ 及 $\Sha(E^{-7}/\mathbb Q)$
的素因子。R138–R140 所构造的素数还满足非异常条件，但本篇
的原始性论证不额外要求 $p$ 在 $F$ 分裂。

令 $\ell$ 在 $F$ 惰性，且
$$
 \ell+1=pu,\qquad p\nmid u a_\ell(E).
\tag{1}
$$
设 $H=F[\ell]$，$L/F$ 是 $H/F$ 的唯一次数 $p$ 子域，
$\Gamma=\langle\tau\rangle$，并使用**原完整迹**
$$
 Q=\operatorname{Tr}_{H/L}P[\ell].
$$
假定 $Q$ 非扭；R140 已对无穷多个实际 $(p,\ell)$ 支付此输入。
基层点 $P[1]=O$，故 $N_\Gamma Q=0$。令
$$
 A=\ker\bigl(N:\operatorname{Res}_{L/F}E\to E\bigr),\quad
 \mathcal O=\mathbb Z_p[\zeta_p],\quad
 \delta=\tau^{(p-1)/2}(\tau-1).
$$
R139 已证明 $\Sha(A/F)$ 有限，$A(F)\otimes\mathbb Z_p=\mathcal O w$。
写
$$
 Q=\delta^a\varepsilon w,\qquad \varepsilon\in\mathcal O^\times,
 \qquad S=\Sha(A/F)[p^\infty].
\tag{2}
$$

**定理。** R139 的实际原始诱导类族在模 $\delta$ 后非零，并且
$$
 \boxed{\quad S\simeq M\oplus M,\qquad
             \operatorname{length}_{\mathcal O}M=a+1.\quad}
\tag{3}
$$
这里的等式属于同一个原点 $Q$ 和同一个原诱导族。没有重选点，
没有在 $\mathcal O$ 中除以 $p$，也没有把 $\ell$ 分歧角色冒作
反圆分 $\mathbb Z_p$ 塔的角色。

进一步，令
$$
 d_p=\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p],\qquad
 \nu_p=\min\{\nu(n):\overline c_n^A\ne0\}.
$$
最小值遍历本文实际诱导族的辅助平方自由整数，且
$$
                         \boxed{\ \nu_p=r+d_p-1.\ }
\tag{4}
$$
这是模 $p$／模 $\delta$ 的最小数目。若改取全 $p^\infty$
族，其最小数目为 $r+\operatorname{corank}_{\mathbb Z_p}
\Sha(E/\mathbb Q)[p^\infty]-1$；不能混淆这两个量。

## 2. Zhang 定理在本曲线上的全部条件

Wei Zhang（2014），*Selmer groups and the indivisibility of Heegner
points*，正式发表版 Theorem 1.1，印页 195，证明原 $E/F$
Heegner 族存在 $c^{E,\mathrm{raw}}_n\bmod p\ne0$。其条件在这里为：

- $N=389$ 在 $F$ 分裂，所以 $N^+=389,N^-=1$；
- $p\ge5$ 普通，$p\nmid7\cdot389$，剩余表示满像；
- Zhang 的 Hypothesis $\spadesuit$ 要求 $E[p]$ 在 $389$ 分歧。
  R136 给出分裂乘法型 $I_1$ 和 $v_{389}(\Delta_E)=1$。
  Tate 参数的估值不是 $p$ 的倍数，故惯性在 $E[p]$ 上的
  非平凡幺幂作用直接支付此条件；
- $N$ 平方自由，因此该假设关于非平方自由导子的第二项为空。

Theorem 1.1 不要求 $p$ 在 $F$ 分裂。固定参数化与该定理的
参数化相差固定非零整数／同源时，只排除其次数的有限多个素数。
Howard（2004）Theorem 1.7.5 的修正对原 $E$ 族在每个节点
可逆，因此 corrected 与 raw 的非零等价；本篇只使用这个
已支付的原曲线结论，不假定 $A$ 也有同样的全局修正。

## 3. 实际剩余比较，以及辅助素数集合

### 3.1 不是抽象同构的 augmentation

令 $B=\operatorname{Res}_{L/F}E$。R139 的实际点是
$$
 Y_n=\operatorname{Tr}_{F[\ell n]/LF[n]}P[\ell n],\qquad
 Z_n=(\tau-1)Y_n,
$$
并有准确整数范数关系
$$
                         N_\Gamma Y_n=a_\ell P[n].
\tag{5}
$$
先对 $Y_n$ 作 Kummer、辅助导数及唯一下降，再经 $B\to A$
取像，得到 $c_n^A$。在实际对角识别 $A[\delta]\simeq E[p]$
下，模 $\delta$ 的比较为
$$
                      \overline c_n^A=-a_\ell\,\overline c_n^{E,\mathrm{raw}}.
\tag{6}
$$

这里的反号可直接从 Kummer 图核对。给定 $Y\in B$，取
$pV=NY$，则 $Y-\operatorname{diag}V\in A$ 是 $(\tau-1)Y$
的一个差分原像，其 Galois 误差在对角核中等于
$-\operatorname{diag}(\sigma V-V)$。平衡元附带的 $\tau$ 幂
在对角核上为一。该图对域扩张、整数导数、范数和精度商均
自然；对导出 $Y_n$ 使用 (5) 即得 (6)。全局 $H^0(E[p])=0$
保证下降唯一，所以没有可任意加入的剩余类。

由于 $a_\ell$ 是单位，Zhang 的非零分量通过 (6) 保留下来。
特别地，**实际整族不能整体再除一个 $\delta$**，尽管首项
是 $(\tau-1)Q=(\text{单位})\delta Q$。

### 3.2 $L$ 分裂条件没有缩小 Kolyvagin 素数集合

$L/\mathbb Q$ 的 Galois 群为二面体群 $D_p$。每个在 $F$
惰性且不分歧于 $L$ 的有理素数 $q$，其在 $D_p$ 中的
Frobenius 是反射，平方为一。因此 $F$ 上的 $q$ 位自动在
$L/F$ 完全分裂。

若
$$
                         a_q\equiv q+1\equiv0\pmod {p^m},
\tag{7}
$$
则 $\operatorname{Fr}_q$ 在 $E[p^m]$ 上的特征多项式为
$X^2-1$。两根差二为单位，两个幂等投影将它对角化为
$\operatorname{diag}(1,-1)$。又
$L\cap F(E[p^\infty])=F$：左边可能的 $C_p$ 商来自满
$\mathrm{GL}_2$ 的行列式，而该扩张只在 $p$ 分歧，$L$
则在 $\ell$ 分歧。因而在复合域中，矩阵和反射的共轭可以
独立完成；(7) 正是 R139 所用复共轭 Frobenius 条件。

以下证明的 Chebotarev 选择可在任意高的 (7) 精度完成，
所以还支付把非零性传到高精度辅助集合的步骤。

## 4. 只用局部深度的原始族刚性

本节给 (3) 所需的完整弱版本。它使用 Howard（2004）
Lemmas 1.3.3、1.5.1、1.5.3、1.5.8 的已证局部／全局
Selmer 比较。形式与 BCGS（2026）Lemma 2.2.4 的严格族
刚性相同；下面逐步说明为什么本实际弱族也满足结论。

写 $T=T_pA$，$R_k=\mathcal O/\delta^k$，以及
$$
 H_k(n)=H^1_{\mathcal F(n)}(F,T/\delta^kT)
       \simeq R_k\oplus M_k(n)\oplus M_k(n),
 \quad \lambda_k(n)=\operatorname{length}_{\mathcal O}M_k(n),
 \quad \mathcal S_k(n)=\delta^{\lambda_k(n)}H_k(n).
\tag{8}
$$
这里的 $\mathcal F$ 是 R139 验证过的真实 Kummer 局部条件，
在辅助素数上改为 transverse。R139 已证明弱 stub 包含关系
$$
 c_n^{(k)}\in\mathcal S_k(n)
 \quad\text{当各辅助素数的精度至少为 }2k-1.
\tag{9}
$$
$\mathcal S_k(n)$ 为循环模或零。有限群张量因子的生成元
任取，改变它只乘单位，不影响以下生成子模。

本实际族的边关系在所有精度均由同一个局部整自同构给出：
$$
              -q\varphi_q^{-1}\otimes1,
 \qquad
 a_q-(q+1)\varphi_q=-q\varphi_q^{-1}(\varphi_q^2-1).
\tag{10}
$$
因此对任意 $j\ge0$，边两端的有限、奇异局部值同时被
$\delta^j$ 杀掉。模 $\delta$ 时该比较交换复共轭正负号：
在有限值上复共轭作用为 $\varphi_q$，在奇异值上还多出
对 tame 生成元取逆的负号，而 (10) 与 $\varphi_q$ 对易。
这些是下面关于类族使用的全部边性质。

### 4.1 任意高精度的四类 Chebotarev 引理

给定至多四个非零的剩余上同调类，各自取一个非零的复共轭
本征分量。对任意 $m$，存在辅助素数 $q$ 满足 (7)，并使
这四个指定类的局部值都非零。

证明：先取 $F(L,E[p^m],\mu_{p^m})$，再考虑有限个类在
此域上限制的核域。
$(-I,1)$ 是表示像中的中心元，在 $E[p]$ 上作用为 $-1$；
Sah 引理使这些剩余类向表示核的限制单射。一个非零类在
该核上的像，经满 $\mathrm{GL}_2$ 作用，是整个 $E[p]$。
将复共轭作用分解，适当的正号子群向该类的指定本征直线
有非零像，其零集的相对比例至多 $1/p$。四个零集的并集
比例至多 $4/p<1$。选并集外元素，并写成
$(c\sigma)^2$（二为单位），Chebotarev 即给所需反射
Frobenius；它在表示／$L$ 部分为 $c$。还可避开任意固定
有限个素数。这个证明不要求角色在 $p$ 分歧。$\square$

### 4.2 core 节点连通，以及同一深度

称 $n$ 为 core，若 $\dim_{\mathbb F_p}H_1(n)=1$。Cartesian
比较和 (8) 表明此时所有已有精度的 $H_k(n)=R_k$。
以 core 节点为顶点，$n,nq$ 均 core 时连一条边。

Howard 的正负局部维数公式说明，core $n$ 与 $nq$ 相邻，
当且仅当 $H_1(n)$ 在 $q$ 处定位非零；这又等价于
$H_k(n)$ 的定位单射（有限模非零核必含 socle）。所以 (10)
使相邻 core 上 $c_n^{(k)}$ 的阶完全相同。

在任意指定的高精度辅助集合内均存在 core：若剩余 Selmer
维数大于一，选择素数使两个存在的本征空间各有非零定位；
若只有一个本征空间非零，则只对它选择。局部维数公式使
两本征维数的最大值严格下降，最终达到一。

此图连通，且可只使用任意指定的高精度辅助素数。详细证明
如下。给定两个 core $n,m$，对它们素因子集合的对称差归纳。
取 $q\mid m,q\nmid n$。若 $nq$ core，则沿该边减少对称差。
否则 $H_1(nq)$ 的两本征维数为 $2,1$。应用 §4.1，选新素数
$v$，使这两个本征空间以及 $H_1(n),H_1(m)$ 的指定非零类
均在 $v$ 非零。局部维数公式给 $nv,nqv,mv$ 全为 core。
路径 $n,nv,nqv$ 和 $m,mv$ 把问题化成 $(nqv,mv)$，其
对称差少一个素数。归纳结束。

于是每个精度 $k$ 存在 $0\le d_k\le k$，使所有 core 有
$$
                \mathcal O c_n^{(k)}=\delta^{d_k}H_k(n).
\tag{11}
$$
在更高辅助精度上选同一个 core，利用类族的精度相容性，
得 $d_{k+1}\ge d_k$；若 $d_k<k$ 则 $d_{k+1}=d_k$。
因此存在 $d\in\mathbb Z_{\ge0}\cup\{\infty\}$，使
$d_k=\min(d,k)$。

### 4.3 非 core 节点的准确 stub 深度

先记录一个只属于 Selmer 模的局部事实。Howard 的四角图
给非负整数 $b_1\ge b_2,h$，使 $H_k(n)$ 与 $H_k(nq)$
对共同 strict 子模的商分别有长度对
$$
       (b_1,b_2),\qquad(k-b_1-h,k-b_2-h).
$$
由 (8) 的总长度比较，
$$
 \lambda_k(nq)=\lambda_k(n)+k-b_1-b_2-h.
\tag{12}
$$
因此对任意 $j\ge0$，
$$
 \operatorname{loc}_q(\delta^j\mathcal S_k(n))=0
 \ \Longleftrightarrow\quad
 \operatorname{loc}_q(\delta^j\mathcal S_k(nq))=0.
\tag{13}
$$
具体地，两边分别等价于
$\lambda_k(n)+j\ge b_1$ 与
$\lambda_k(nq)+j\ge k-b_2-h$，由 (12) 完全相同。

现在对 $\max(\rho(n)^+,\rho(n)^-)$ 归纳，其中
$\rho(n)^\pm=\dim H_1(n)^\pm$。若 stub 为零则 (9) 已足够。
否则选 $v$，同时使 stub 的 socle 非零定位，以及两个存在的
本征空间各一个非零类非零定位。最多需要三个类，故 §4.1
适用。局部维数公式使上述最大值下降；定位在循环 stub 上
单射。由归纳假设、(10)、(13)，对所有 $j$ 有
$$
 \begin{aligned}
 \delta^j c_n^{(k)}=0
 &\Longleftrightarrow
   \operatorname{loc}_v(\delta^j c_n^{(k)})=0\\
 &\Longleftrightarrow
   \operatorname{loc}_v(\delta^j c_{nv}^{(k)})=0\\
 &\Longleftrightarrow
   \operatorname{loc}_v(\delta^{d+j}\mathcal S_k(nv))=0\\
 &\Longleftrightarrow
   \operatorname{loc}_v(\delta^{d+j}\mathcal S_k(n))=0\\
 &\Longleftrightarrow \delta^{d+j}\mathcal S_k(n)=0.
 \end{aligned}
\tag{14}
$$
两个子模均在同一循环 stub 内，阶相同即子模相同。连同
core 情形，这证明
$$
                  \mathcal O c_n^{(k)}
                     =\delta^d\mathcal S_k(n).
\tag{15}
$$
整个论证从未要求把 (10) 延拓成全局 $\mathcal O$ 线性
cohomology 自同构。它只使用各个 $\delta^j$ 倍的局部零性，
所以适用于 R139 的原 weak 族。

## 5. 在原首项上取极限

(6) 和 Zhang 定理给 $k=1$ 某节点的类非零。(15) 因而
迫使 $d=0$。取 $k$ 大于 $S$ 的指数和 $a+1$，R139 的
Selmer 比较给
$$
 H_k(1)=R_k\oplus M\oplus M,
 \qquad H^1_{\mathcal F}(F,T)=A(F)\otimes\mathbb Z_p.
$$
后一个等式使用 **已证明有限的** $\Sha(A/F)$。首项
$c_1$ 是 $(\tau-1)Q$ 的 Kummer 像，在自由格中指数为 $a+1$。
而 (15) 说它恰生成 $\delta^{\operatorname{length}M}$ 倍自由格
的模 $\delta^k$ 像。Cartesian 注入和任意大的 $k$ 给
$\operatorname{length}M=a+1$，即 (3)。

## 6. 最小辅助数目为何仍是独立输入

Zhang（2014）Lemma 8.4（印页 236–239）对模 $p$ 原族给
$$
 \nu=\max\{\dim\operatorname{Sel}_p(E/F)^+,
            \dim\operatorname{Sel}_p(E/F)^-\}-1.
$$
R136 的负七扭曲秩一、整个 Sha 有限，删去其固定有限个
素因子后，两个维数为 $r+d_p$ 和 $1$。由 (6)，本实际
诱导族在每一个节点的模 $\delta$ 零性与该原族相同，故得到
(4)。这也说明高精度辅助集合的变更没有偷偷改变最小值：
在该引理的三角化证明中，用 §4.1 的高精度 Chebotarev
替换每一次选择即可，所有剩余配对与有限／奇异关系不变。

若只使用全 $p^\infty$ 非零，Zhang Theorem 11.2（印页 248）
对应的是 Selmer **余秩**，所以应把 $d_p$ 换成 Sha 的
$\mathbb Z_p$ 余秩。这与模 $p$ 公式不是同一断言。

结合 R139 的符号交替性，现在有准确的必要约束
$$
 2(a+1)\ge
 \begin{cases}
  2r-2+2d_p,&a\text{ 偶},\\
  2r+2d_p,&a\text{ 奇}.
 \end{cases}
\tag{16}
$$
因此 $a\le1$ 仍足以得到 $r=2$ 与 $\Sha(E/\mathbb Q)[p^\infty]=0$。
原始性已经准确给出 (3)，并不能把右边的 $a+1$ 换成 $a$：
那样会与实际非零剩余分量 (6) 以及 (15) 矛盾。
下一所需输入必须约束原 $Q$ 的首两层，或等价地证明
足够多 $p$ 的实际两矩测试非零；不能再把整族某处分量非零
当作这个输入。

## 引用与本仓库接口

- W. Zhang, *Selmer groups and the indivisibility of Heegner points*,
  Cambridge J. Math. **2** (2014), 191–253；Theorem 1.1，
  Hypothesis $\spadesuit$，Lemma 8.4，Theorems 9.3、11.2。
  [正式发表全文](https://archive.intlpress.com/site/pub/files/_fulltext/journals/cjm/2014/0002/0002/CJM-2014-0002-0002-a002.pdf)。
- B. Howard, *The Heegner point Kolyvagin system*, Compositio Math.
  **140** (2004), 1439–1472；Lemmas 1.3.3、1.5.1、1.5.3、1.5.8、
  1.6.2–1.6.4，Theorems 1.6.1、1.7.5。
  [发表全文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1BF8414258216C1575963BBDA814CB2F/S0010437X04000569a.pdf/the-heegner-point-kolyvagin-system.pdf)。
- A. Burungale, F. Castella, G. Grossi, C. Skinner,
  *Non-vanishing of Kolyvagin systems and Iwasawa theory*，
  作者 2026-01-02 稿，Proposition 2.2.1、Lemma 2.2.4、
  Theorem 2.2.2（pp.17–19）。
  [作者全文](https://web.math.ucsb.edu/~castella/Kolyvagin.pdf)。
  其陈述使用反圆分 $p$ 塔的角色；本文没有将该角色范围
  直接改写，而在 §4 给出所需的实际 weak 版本证明。
- M. Zanarella, *On Howard's main conjecture and the Heegner point
  Kolyvagin system*（2019），§§2.2–2.3 提供 core 图与原始性
  的证明思路；[原稿](https://arxiv.org/pdf/1908.09197)。
  本文所需全部弱边推广已在 §4 写明，不以该未发表稿独立
  充当未解释的证明输入。
- 本仓库 R136（曲线、辅助域和基层点）、R139（实际 raw 族、
  全局／局部格、弱 stub 与符号）、R140（原完整 $Q$ 的非扭
  和小高度）。
