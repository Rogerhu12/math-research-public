# R61：双素数短关系与更强的判别式增长界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的全局必要条件。** 在 R58 的 $p\equiv1\pmod{12}$ 分支，两个非主分裂素理想的短关系把单素数理想阶的指数依赖降到 $\sqrt{h_K}$。不使用 GRH 或 Chebotarev，得到更强的变化商域判别式增长下界。结论仍允许商域增长，未达到主要目标。

## 1. 假设与结论

沿用 [R58](R58-ring-class-splitting-and-small-split-primes.md) 的假设：$E/\mathbb Q$ 无 CM，
$$
p>37,\qquad p\equiv1\pmod{12},\qquad
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p).
$$
记 $K$ 为二次商域，$D=|D_K|$、$h=h_K$。R58 的特征记号保持为
$$
\mu=\lambda^2,\qquad \nu=\mu/\chi_p.
$$
特别地，$K$ 虚二次、$p$ 惰性，且对所有在 $p$ 为单位的 $\alpha\in K^\times$，
$$
\mu((\alpha))\equiv\alpha^2\pmod p.
\tag{61.1}
$$

**定理 R61。**

1. 若 $q_1,q_2$ 为不同的有理素数，均在 $K$ 分裂，且其上方素理想均非主，则
   $$
   \boxed{p<16(q_1q_2)^{\lfloor\sqrt h\rfloor}.}
   \tag{61.2}
   $$
   这里不要求预先好约化，也无 $q_i\ge5$ 的限制。

2. 若 $2,3$ 均在 $K$ 分裂，则
   $$
   \boxed{p<16\cdot6^{\lfloor\sqrt h\rfloor}.}
   \tag{61.3}
   $$
   更具体地，对任意有向主理想关系，其范数为 $N=2^{|u|}3^{|v|}$ 时有 $p<16N$；如果两个局部 Frobenius 二次域相同，则有 $p<4\sqrt N$。

3. 若 $h>1$，则存在两个第 1 条中的素数，满足 $q_1q_2<16D^{10}$。所以
   $$
   \boxed{p<16(16D^{10})^{\lfloor\sqrt h\rfloor}.}
   \tag{61.4}
   $$
   令 $B=2\sqrt D/\pi$，由 Minkowski 界还有
   $$
   \boxed{
   \log(p/16)
   <\sqrt{B(1+\log B)}(\log16+10\log D)
   <10D^{1/4}(\log D)^{3/2}.}
   \tag{61.5}
   $$
   因而沿实际 $h_K>1$ 的异常序列，得到有效的渐近必要下界
   $$
   \boxed{|D_K|\gg
   \frac{(\log p)^4}{(\log\log p)^6}.}
   \tag{61.6}
   $$

## 2. 多个分裂素数的实迹范数引理

先给可供后续使用的一般形式。取不同的分裂有理素数 $q_1,\ldots,q_s$，并假定
$$
p>4\max_i q_i.
\tag{61.7}
$$
对每个 $i$ 选择 $q_i\mathcal O_K=\mathfrak q_i\bar{\mathfrak q}_i$ 的一支。

R58 §5 表明：潜在乘法约化会强迫 $q_i\equiv1\pmod p$，与 (61.7) 矛盾。因此存在局部二次扭曲 $E_i/\mathbb Q_{q_i}$，具有好约化及真正的整数迹
$$
a_i\in\mathbb Z,\qquad |a_i|\le2\sqrt{q_i},
\qquad T^2-a_iT+q_i.
$$
此步骤覆盖 $q_i=2,3$；所需的惯性二次特征延拓已在 R58 §5.2 完整证明。

令 $F_i=\mathbb Q(\pi_i)$，其中 $\pi_i$ 是该多项式的一根。由于 $q_i$ 为素数，$a_i^2<4q_i$，所以 $F_i$ 为虚二次域。又
$$
0<4q_i-a_i^2<p.
$$
完整非分裂 Cartan 中的元素不能有两个不同的 $\mathbb F_p$ 特征值，故 $a_i^2-4q_i$ 模 $p$ 非平方。于是 $p$ 在每个 $F_i$ 中惰性。

记
$$
F=F_1\cdots F_s,\qquad F^+=F^{\langle c\rangle},
\qquad d=[F^+:\mathbb Q]\le2^{s-1},
$$
其中 $c$ 为复共轭。因为 $p$ 在各虚二次生成域的 Frobenius 都是共轭，$\operatorname{Frob}_p|_F=c$。因此 $p$ 在 $F^+$ 完全分裂。

**实迹范数引理。** 若 $K\cap F=\mathbb Q$，则对任意非零整数向量 $(e_1,\ldots,e_s)$，只要
$$
\prod_i[\mathfrak q_i]^{e_i}=1
\quad\text{于 }\operatorname{Cl}(K),
$$
便有
$$
\boxed{p<(4\sqrt N)^d,
\qquad N=\prod_iq_i^{|e_i|}.}
\tag{61.8}
$$

**证明。** 先把负指数转为共轭素理想。令 $n_i=|e_i|$；若 $e_i\ge0$ 取 $\mathfrak r_i=\mathfrak q_i$，否则取 $\mathfrak r_i=\bar{\mathfrak q}_i$。因为
$$
\mathfrak q_i^{-1}=q_i^{-1}\bar{\mathfrak q}_i,
$$
可将原主分式理想乘一个正有理整数，得到
$$
\mathfrak a=\prod_i\mathfrak r_i^{n_i}=(\alpha),
\quad \alpha\in\mathcal O_K,
\quad N_{K/\mathbb Q}\alpha=N.
\tag{61.9}
$$
每个有理素数只选其中一支，且至少有一个指数正，故 $\mathfrak a\ne\bar{\mathfrak a}$。所以 $\alpha$ 既非实亦非纯虚。记
$$
t=\operatorname{Tr}_{K/\mathbb Q}\alpha\in\mathbb Z,
\qquad 0<|t|<2\sqrt N.
$$

选择 $KF$ 的一个 $p$ 上方素理想，并将其剩余域识别为 $\mathbb F_{p^2}$，使对 $K$ 的识别与 (61.1) 相同。这样的识别存在：$p$ 在 $K$ 和所有 $F_i$ 上都不分歧，Frobenius 同时为复共轭，故剩余次数恰为二。

设 $\beta_i\in\mathbb F_{p^2}$ 是相应局部好约化扭曲的 Frobenius 根，选取与 $\mathfrak r_i$ 同一取向的根，故
$$
\beta_i^2=\mu(\mathfrak r_i),
\qquad \beta_i^p\text{ 为另一根}.
$$
在该共同剩余嵌入下，分别从 $\pi_i,\bar\pi_i$ 中选择约化为 $\beta_i$ 的一根。不同的局部二次扭曲至多将相应两根同时乘 $-1$；后面的共同符号会吸收这些改变。

令
$$
z=\prod_i\pi_i^{n_i}\in\mathcal O_F,
\qquad z\bar z=N,
\qquad S=z+\bar z\in\mathcal O_{F^+}.
$$
由 (61.1) 和 (61.9)，
$$
\left(\prod_i\beta_i^{n_i}\right)^2
=\mu(\mathfrak a)\equiv\alpha^2\pmod p.
$$
$p$ 奇且剩余环是域，所以存在一个共同的 $\epsilon\in\{1,-1\}$，使
$$
z\equiv\epsilon\alpha\pmod p.
$$
施加剩余域的 $p$ 次幂，在 $F$ 与 $K$ 上分别为复共轭，且保留同一个 $\epsilon$，因此
$$
\boxed{S\equiv\epsilon t\pmod{\mathfrak P^+},}
\tag{61.10}
$$
其中 $\mathfrak P^+\mid p$ 为 $F^+$ 的次数一素理想。

关键是 $S-\epsilon t\ne0$。若相等，则 $z,\bar z$ 与 $\epsilon\alpha,\epsilon\bar\alpha$ 有相同的和与积，故
$$
z=\epsilon\alpha\quad\text{或}\quad z=\epsilon\bar\alpha.
$$
左边属于 $F$，右边属于 $K$，而 $K\cap F=\mathbb Q$。这使非实的 $\alpha$ 成为有理数，矛盾。

所以 $N_{F^+/\mathbb Q}(S-\epsilon t)$ 是一个被 $p$ 整除的非零整数。每个复嵌入都将 $\pi_i$ 送到绝对值 $\sqrt{q_i}$ 的根，因而每个实嵌入下 $|S|\le2\sqrt N$，由此
$$
p\le\left|N_{F^+/\mathbb Q}(S-\epsilon t)\right|
<(4\sqrt N)^d.
$$
证毕。这个论证只比较实际局部 Frobenius 的特征零根，没有构造或假定一个全局有理系数的 CM 提升。

## 3. 两个非主分裂素理想：交域自动平凡

取第 1 条的 $q_1,q_2$。若 $p\le4\max(q_1,q_2)$，则因为 $h\ge2$、$\lfloor\sqrt h\rfloor\ge1$，(61.2) 已显然成立。以下假定 (61.7)。

在第 2 节的记号下，$F_i\ne K$：否则 $\pi_i\in\mathcal O_K$ 的范数为 $q_i$，其主理想为 $q_i$ 上方某一素理想，迫使选定的 $\mathfrak q_i$ 及其共轭均主，矛盾。

若 $F_1=F_2$，则 $F=F_1$，所以 $K\cap F=\mathbb Q$。若两者不同，$F_1F_2$ 的三个二次子域是两个虚二次域 $F_1,F_2$ 和一个实二次域。虚二次 $K$ 不等于其中任何一个，故仍有
$$
K\cap F_1F_2=\mathbb Q.
$$

令 $m=\lfloor\sqrt h\rfloor$。因为 $(m+1)^2>h$，以下 $(m+1)^2$ 个类中有两个相同：
$$
[\mathfrak q_1]^i[\mathfrak q_2]^j,
\qquad 0\le i,j\le m.
$$
相减给出非零关系 $(u,v)$，满足 $|u|,|v|\le m$。用引理，$d\le2$，且
$$
N=q_1^{|u|}q_2^{|v|}\le(q_1q_2)^m.
$$
所以
$$
p<16N\le16(q_1q_2)^m,
$$
证明 (61.2)。若 $F_1=F_2$，则 $d=1$，同一关系有更强的 $p<4\sqrt N$。

这里两个非主素理想可以属于相同理想类；鸽巢只使用类群有 $h$ 个元素，不要求独立生成两个循环因子。

## 4. 2、3 同时分裂时的具体接口

若 $2,3$ 都在 $K$ 分裂，则潜在乘法约化已由 $q\equiv1\pmod p$ 排除。对第 2 节的好约化扭曲，Hasse 范围与非分裂 Cartan 条件给

| 素数 | 允许的整数迹 | 对应 Frobenius 二次域 |
|---:|---|---|
| $2$ | $0,\pm1$ | $\mathbb Q(\sqrt{-2})$ 或 $\mathbb Q(\sqrt{-7})$ |
| $3$ | $\pm1,\pm2$ | $\mathbb Q(\sqrt{-11})$ 或 $\mathbb Q(\sqrt{-2})$ |

在 $2$ 处排除了 $\pm2$，因为判别式为 $-4$，在 $p\equiv1\pmod4$ 时为非零平方。在 $3$ 处排除了 $0,\pm3$，因为相应二次域为 $\mathbb Q(\sqrt{-3})$，在 $p\equiv1\pmod3$ 时分裂。

同时使 $2,3$ 分裂的 $K$ 不可能等于表中的任何域：$-2$ 域在 $2$ 分歧，$-7$ 域在 $3$ 惰性，$-11$ 域在 $2$ 惰性。因此 $K\cap F_2F_3=\mathbb Q$ 自动成立，短关系直接给出 (61.3)。

也可先验证 $2,3$ 上方理想非主，再应用第 3 节。若存在范数 $2$ 的元素，其迹的平方减 $8$ 说明 $K$ 只能是 $-1,-2,-7$ 三域之一；分别与 $p$ 惰性、$2$ 分裂或 $3$ 分裂矛盾。范数 $3$ 的元素类似，只产生 $-2,-3,-11$ 三域，均与 $2$ 分裂矛盾。特别地，这个分裂条件本身已强迫 $h>1$。

### 4.1 直接使用整数递推的双素数证书

给定一条关系 (61.9)，令 $n_1=|u|,n_2=|v|$、$Q_i=q_i^{n_i}$、$N=Q_1Q_2$，并设
$$
T_0(a,q)=2,\quad T_1(a,q)=a,\quad
T_n(a,q)=aT_{n-1}(a,q)-qT_{n-2}(a,q),
$$
$$
A_i=T_{n_i}(a_i,q_i),\quad C=A_1A_2,
\quad P=Q_2A_1^2+Q_1A_2^2-4N.
$$
两种相对根取向给出的实迹 $S,S'$ 满足
$$
S+S'=C,\qquad SS'=P.
$$
由 (61.10)，当前实际迹必满足
$$
\boxed{p\mid t^2-\epsilon tC+P,\qquad \epsilon\in\{1,-1\}.}
\tag{61.11}
$$
这个整数非零：若某个 $S$ 或 $S'$ 等于 $\epsilon t$，前面的同和同积论证仍会把非实的 $\alpha$ 放入 $K\cap F$。因而也有不含符号的证书
$$
\boxed{p\mid (t^2+P)^2-t^2C^2,}
\tag{61.12}
$$
其右边非零。该式允许用整数递推逐项核验，不必显式计算环类域。局部扭曲改变的迹符号不影响所需的二择一条件。

## 5. 无条件找到两个不同的非主分裂素数

假设 $h>1$。固定一个非主理想类的原始约化正定型
$$
Q(x,y)=ax^2+bxy+cy^2,
\qquad b^2-4ac=-D,
\qquad |b|\le a\le c.
$$
有
$$
a\le\sqrt{D/3}<\sqrt D,\qquad c\le D.
$$
令 $\theta=(-b+\sqrt{-D})/2$、$\mathfrak a=(a,\theta)$。对任何非零整数向量 $(x,y)$，
$$
\gamma=ax-\theta y\in\mathfrak a,
\quad N\gamma=aQ(x,y),
\quad \mathfrak b=(\gamma)/\mathfrak a
$$
为范数 $Q(x,y)$、类为 $[\mathfrak a]^{-1}\ne1$ 的整理想。

R58 §7 已在 $y=1$ 的情况下由 CRT 选出 $Q(x,1)$ 与 $D$ 互素且小于 $2D^{5/2}$。相应非主整理想没有分歧因子，惰性素理想又都主，因此至少含一个非主分裂素理想。记其下方有理素数为 $q_1$，所以
$$
q_1<2D^{5/2}.
\tag{61.13}
$$

### 5.1 当 q1 为奇素数

对每个 $\ell\mid Dq_1$，可以选择 $x\bmod\ell$ 使 $Q(x,1)\ne0$。对于 $\ell\mid D$，这是 R58 的判别式零及原始性论证；对于新素数 $\ell=q_1\ge3$，非零的次数至多二多项式至多有两个根，所以也有允许的剩余类。

由 CRT，取
$$
0\le x<\operatorname{rad}(D)q_1\le Dq_1,
\quad (Q(x,1),Dq_1)=1.
$$
则
$$
Q(x,1)
<D^{5/2}q_1^2+D^{3/2}q_1+D
<2D^{5/2}q_1^2.
$$
相应非主整理想至少含一个非主分裂素理想，其下方 $q_2$ 不同于 $q_1$，且
$$
q_2<2D^{5/2}q_1^2.
\tag{61.14}
$$
结合 (61.13)，
$$
q_1q_2<2D^{5/2}q_1^3<16D^{10}.
$$

### 5.2 当 q1=2：不能漏掉二次多项式的例外

因为 $2$ 分裂，$D$ 为奇数。若 $Q(x,1)$ 模二不是零函数，上一构造仍适用。

唯一需要额外处理的是 $a,b$ 奇、$c$ 偶，此时 $Q(x,1)\equiv x^2+x$ 在 $\mathbb F_2$ 上确实恒零。改取 $y=2$，并要求 $x$ 奇，于是 $Q(x,2)$ 为奇数。

对每个奇 $\ell\mid D$，仍能选 $x$ 使 $Q(x,2)\ne0$：若 $\ell\nmid a$，模 $\ell$ 判别式为零，至多一个坏根；若 $\ell\mid a$，则 $\ell\mid b$、$\ell\nmid c$，而 $Q(x,2)\equiv4c\ne0$。

CRT 给出 $0\le x<2\operatorname{rad}(D)\le2D$，并有
$$
(Q(x,2),2D)=1,
\qquad Q(x,2)<4D^{5/2}+4D^{3/2}+4D<8D^{5/2}.
$$
所得非主整理想含不同于 $2$ 的非主分裂素数 $q_2<8D^{5/2}$，所以
$$
q_1q_2<16D^{5/2}\le16D^{10}.
$$
这完成第 3 条中两素数存在性的证明，没有使用素数密度或把密度当作最小素数界。

## 6. 类数和判别式的后果

将 $q_1q_2<16D^{10}$ 代入 (61.2)，得到 (61.4)。R58 §7 已从 Minkowski 界和理想计数逐项证明
$$
h\le B(1+\log B),\qquad B=\frac2\pi\sqrt D.
$$
于是
$$
\log(p/16)
<\sqrt h(\log16+10\log D)
\le\sqrt{B(1+\log B)}(\log16+10\log D).
$$
非平凡虚二次类群有 $D\ge15$。因此
$$
1+\log B<\log D,
\qquad \log16+10\log D<12\log D,
\qquad 12\sqrt{2/\pi}<10,
$$
给出 (61.5)。

如需一个直接的无隐藏常数反演，令 $L=\log(p/16)\ge e$。将 $D\ge L^4$ 与 $D<L^4$ 分开，在后一情形使用 $\log D<4\log L$，得到
$$
\boxed{D>\frac{L^4}{80^4(\log L)^6}.}
\tag{61.15}
$$
这同时说明 (61.6) 的有效性。

如果已知 $2,3$ 都分裂，直接使用 (61.3) 而不经过第 5 节较大的素数界，则得到更强的条件性增长形式
$$
|D_K|\gg\frac{(\log p)^4}{(\log\log p)^2}.
$$
这里“条件性”只指附加分裂条件，并不指 GRH。

## 7. 适用边界与已有输入

- R58 提供 $p$ 外平方特征不分歧、主理想同余、$2,3$ 的真实局部二次好约化扭曲以及初始非主分裂素数的 CRT 构造。本文将多个局部根放在一个共同剩余嵌入中，并利用实子域取范数。
- 两个非主分裂素数时，交域条件自动成立；三个以上时不能据 $F_i\ne K$ 就断言 $K\cap\prod F_i=\mathbb Q$。一般引理 (61.8) 明确保留该条件。
- 环类群分裂没有强迫 $2$ 或 $3$ 的理想类为主；实际得到的是类群必须足够大，才能避免短关系与整数迹冲突。
- (61.4)–(61.6) 是判别式的增长下界。即使它比 R58 的下界更强，也没有排除 $D_K\to\infty$，不能被写成绝对的 Serre 一致性界。
- Minkowski 输入的原始参考为 J. S. Milne, *Algebraic Number Theory*, v3.08 (2020), Theorem 4.3，[作者原文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)；本文所需的后续计数与 CRT 估计均已展开。
