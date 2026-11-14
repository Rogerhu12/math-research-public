# R62：多素数短关系与显式变化商域界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明的无条件必要条件。** 本篇继续 R58、R61 的 $p\equiv1\pmod{12}$ 分支。通过一个平方类空间中的选择论证，解决三个以上 Frobenius 二次域的合成可能包含商域的问题；再用多个非主分裂素理想的短关系，得到
$$
\log p<\frac52\log(8D^{5/2})
\exp\!\bigl(2\sqrt{\log18\,\log h}\bigr),
\qquad D=|D_K|,\quad h=h_K>1.
$$
特别地，所有这些实际异常均须满足
$$
\boxed{D>\exp\!\left(\frac{(\log\log p)^2}{36}\right).}
$$
这里是商域判别式的**下界**。它最终强于任意固定次幂的 $\log p$ 下界，但仍允许 $K$ 随 $p$ 增长；没有给绝对异常素数界，也未处理类数一分支。

## 1. 假设及定量陈述

设 $E/\mathbb Q$ 无 CM，
$$
p>37,\qquad p\equiv1\pmod{12},\qquad
\operatorname{Im}\bar\rho_{E,p}=N_{\rm ns}(p).
$$
令 $K$ 为正规化子的二次商域，并假定 $h=h_K>1$。由 R5，$K$ 虚二次且 $p$ 惰性；由 R58，有 $\mu=\lambda^2$ 及主理想公式
$$
\mu((\alpha))\equiv\alpha^2\pmod{p\mathcal O_K}.
\tag{62.1}
$$
本文的对数均为实自然对数。

置
$$
D=|D_K|,\qquad \mathcal B_D=8D^{5/2},\qquad
m_t=\lfloor h^{1/t}\rfloor\quad(t\ge1).
$$
非平凡虚二次类群有 $D\ge15$。此处只需有限小判别式检查：基本判别式绝对值小于十五的情形是 $3,4,7,8,11$；前四个的 Minkowski 界小于二，最后一个只有范数一的理想类代表，因为 $2$ 在 $\mathbb Q(\sqrt{-11})$ 惰性。

**定理 62.1。** 对每个正整数 $t$，都有
$$
\boxed{
\log p<2^{t-1}\log4+
2^{t-3}(9^t-1)m_t\log\mathcal B_D.
}
\tag{62.2}
$$
因此
$$
\boxed{
\log p<\frac52\log\mathcal B_D\,
\exp\!\left(2\sqrt{\log18\,\log h}\right).
}
\tag{62.3}
$$
用 Minkowski 界消去 $h$，得到完全显式的
$$
\boxed{
\log p<\frac52\left(\log8+\frac52\log D\right)
\exp\!\left(
2\sqrt{\log18\left(\frac12\log D+\log\log D\right)}
\right).
}
\tag{62.4}
$$
一个较粗但可直接反演的后果是
$$
\boxed{\log\log p<6\sqrt{\log D}.}
\tag{62.5}
$$
所有常数都明确，不使用 GRH、Chebotarev 或未知有效常数。

## 2. 避开任意已选素数的非主分裂素数

下面把 R61 的两素数 CRT 构造写成可反复使用的版本。

**引理 62.2。** 给定 $h>1$ 的虚二次域 $K$，可以构造任意多个不同的**奇**素数 $q_1,q_2,\ldots$，使每个 $q_i$ 在 $K$ 分裂、其上方素理想非主，并且若
$$
P_k=\prod_{i=1}^kq_i,\qquad P_0=1,
$$
则
$$
q_{k+1}<\mathcal B_D P_k^2,\qquad
P_k<\mathcal B_D^{(3^k-1)/2}\quad(k\ge1).
\tag{62.6}
$$

**证明。** 固定一个非主理想类的原始约化正定二元二次型
$$
Q(X,Y)=aX^2+bXY+cY^2,
\qquad b^2-4ac=-D,\qquad |b|\le a\le c.
$$
有 $a\le\sqrt{D/3}<\sqrt D$、$|b|<\sqrt D$、$c\le D$。

先固定 $y\in\{1,2\}$，使模二条件可解。如果 $Q(x,1)$ 在 $\mathbb F_2$ 上不是零函数，取 $y=1$，选取一个使它为奇数的 $x\bmod2$。如果它是零函数，则 $c$ 偶且 $a+b$ 偶；由原始性排除 $a,b$ 同为偶数，故恰是 $a,b$ 奇、$c$ 偶。此时取 $y=2$、$x$ 奇，便使 $Q(x,2)$ 为奇数。这个选择只依赖固定的型，与随后已选素数无关。

设 $P=P_k$。对每个奇素数 $\ell\mid DP$，$y$ 是模 $\ell$ 单位。由于型原始，多项式
$$
Q(x,y)=ax^2+byx+cy^2\pmod\ell
$$
不恒为零。它次数至多二，故在 $\ell\ge3$ 时总有一个非零值。这个论证对新选的、未必除 $D$ 的素数同样成立。

中国剩余定理给
$$
0\le x<\operatorname{rad}(2DP)\le2DP,
\qquad (Q(x,y),2DP)=1.
$$
由于 $y\le2$，
$$
\begin{aligned}
Q(x,y)
&<4D^{5/2}P^2+4D^{3/2}P+4D\\
&<8D^{5/2}P^2=\mathcal B_D P^2.
\end{aligned}
\tag{62.7}
$$
最后一个严格不等式对 $D\ge15,P\ge1$ 成立，因为
$1/(DP)+1/(D^{3/2}P^2)<1$。

为保证所找到的素数真的非主，置
$$
\theta=(-b+\sqrt{-D})/2,\qquad
\mathfrak a=(a,\theta),\qquad
\gamma=ax-\theta y.
$$
这里 $\mathfrak a$ 代表已选非主类，且
$$
\gamma\in\mathfrak a,\qquad
N_{K/\mathbb Q}\gamma=aQ(x,y).
$$
故
$$
\mathfrak b=(\gamma)/\mathfrak a
$$
为范数 $Q(x,y)$、类 $[\mathfrak a]^{-1}\ne1$ 的整理想。其范数与 $2DP$ 互素，因此没有分歧素理想、没有已选素数上方的因子、也没有二进因子。惰性素理想为有理素数生成的主理想。如果所有其余素理想因子也主，$\mathfrak b$ 就会主，矛盾。因此至少有一个非主分裂素理想因子；其下方奇素数取作 $q_{k+1}$，有
$$
q_{k+1}\le N\mathfrak b<\mathcal B_D P_k^2.
$$
于是 $P_{k+1}<\mathcal B_D P_k^3$。从 $P_0=1$ 归纳得 (62.6)。证毕。

这个证明使用的是非主整理想的实际因子，不是从某个数被二次型表示便直接声称其所有素因子都非主。构造有效，但未宣称其数域计算高效。

## 3. 从两倍的 Frobenius 域中选出一半，避开 K

**引理 62.3。** 设 $K$ 是二次域，$F_1,\ldots,F_{2t}$ 为二次域，且 $F_i\ne K$。允许 $F_i$ 之间重复。则至少可选出 $t$ 个指标组成集合 $S$，使
$$
K\cap\left(\prod_{i\in S}F_i\right)=\mathbb Q.
\tag{62.8}
$$

**证明。** 在 $\mathbb Q^\times/\mathbb Q^{\times2}$ 中令 $\kappa$、$f_i$ 表示相应非零平方类，并令 $V$ 为这些类生成的有限维 $\mathbb F_2$ 空间。取所有满足
$$
\ell:V\to\mathbb F_2,\qquad \ell(\kappa)=1
$$
的线性泛函。

对每个 $i$，$f_i\ne0,\kappa$，因此 $f_i$ 与 $\kappa$ 线性独立。条件 $\ell(\kappa)=1$ 下，恰有一半泛函使 $\ell(f_i)=0$。线性期望给出：某个泛函至少使 $t$ 个 $f_i$ 落入 $\ker\ell$。从中选取 $t$ 个，则其生成的平方类空间不含 $\kappa$，因为 $\ell(\kappa)=1$。多二次扩张的子域对应给出 (62.8)。证毕。

这里不要求所列 $F_i$ 互不相同，也不要求它们在平方类空间中线性独立。直接由每个 $F_i\ne K$ 推出全部合成不含 $K$ 是错误的；本引理通过舍弃至多一半指标来取得真正需要的条件。

## 4. 实际局部根与类群短关系

固定 $t\ge1$，由引理 62.2 选取 $2t$ 个不同的非主分裂素数，记其乘积为 $P=P_{2t}$。先定义随后比较的最终上界
$$
\mathscr U=4^{2^{t-1}}P^{m_t2^{t-2}}.
\tag{62.9}
$$
当 $t=1$，$m_t=h\ge2$，所以 $\mathscr U\ge4P$。当 $t\ge2$，$m_t\ge1$，同样 $\mathscr U\ge4P$。

若 $p\le4\max_iq_i$，则 $p<4P\le\mathscr U$，所需不等式已经成立。特别地，如果其中某个素数是潜在乘法约化，R58 §5.1 的 $q_i\equiv1\pmod p$ 也属于这个已处理分支。注意这里比较的是 $P$ 所定义的最终上界，不能与尚未选出的某条关系的较小范数混淆。

以下假设
$$
p>4\max_iq_i.
\tag{62.10}
$$
R58 §5.2 使每个局部二次扭曲在 $q_i$ 好约化。令其真正整数迹为 $a_i$，并取
$$
\pi_i^2-a_i\pi_i+q_i=0,\qquad F_i=\mathbb Q(\pi_i).
$$
因为 $q_i$ 为素数，$a_i^2<4q_i$，所以 $F_i$ 虚二次。又
$$
0<4q_i-a_i^2<p.
$$
非分裂 Cartan 条件使 $a_i^2-4q_i$ 模 $p$ 为非平方，故 $p$ 在 $F_i$ 惰性。

还有 $F_i\ne K$：若相等，$\pi_i\in\mathcal O_K$ 的范数为 $q_i$，其主理想就是 $q_i$ 上方某一个素理想，另一个为其共轭，也主。这违反 $q_i$ 的选取。这个论证不假定整个类群由所选素理想生成。

应用引理 62.3，选出 $t$ 个指标，重新记为 $1,\ldots,t$，使
$$
K\cap F=\mathbb Q,\qquad F=F_1\cdots F_t.
$$
记 $F^+=F^{\langle c\rangle}$。每个 $F_i$ 虚二次，所以复共轭在 $F$ 上非平凡，且
$$
[F^+:\mathbb Q]\le2^{t-1}.
\tag{62.11}
$$

对每个已选素数固定一支 $\mathfrak q_i\mid q_i$。因为
$$
(m_t+1)^t>h,
$$
类群中的 $(m_t+1)^t$ 个元素
$$
\prod_{i=1}^t[\mathfrak q_i]^{e_i},
\qquad 0\le e_i\le m_t
$$
有两个相同。因此存在一个非零有向关系，指数 $u_i$ 满足
$$
|u_i|\le m_t,\qquad
\prod_i[\mathfrak q_i]^{u_i}=1.
\tag{62.12}
$$
负指数转为共轭素理想，得到整理想
$$
\mathfrak r=\prod_i\mathfrak q_i^{\max(u_i,0)}
\bar{\mathfrak q}_i^{\max(-u_i,0)}=(\alpha),
\qquad \alpha\in\mathcal O_K.
$$
它的范数为
$$
N=\prod_{i=1}^tq_i^{|u_i|}\le P^{m_t}.
\tag{62.13}
$$
每个有理素数只占一支，且关系非零，所以 $\mathfrak r\ne\bar{\mathfrak r}$；特别地 $\alpha$ 非实。

R61 §2 的实迹范数引理给
$$
p<(4\sqrt N)^{[F^+:\mathbb Q]}
\le4^{2^{t-1}}P^{m_t2^{t-2}}
=\mathscr U.
\tag{62.14}
$$
为使这次调用的实际性明确：在 $KF$ 的一个共同 $p$ 进剩余嵌入下选择每个 $\pi_i$ 或其共轭，使它的约化是对应 $\mu(\mathfrak q_i)$ 的平方根。对有向乘积 $z$，(62.1) 给 $z\equiv\epsilon\alpha$，其中只有一个共同 $\epsilon=\pm1$；剩余 Frobenius 同时为复共轭，因此
$$
z+\bar z\equiv\epsilon\operatorname{Tr}\alpha.
$$
两边之差是 $F^+$ 的代数整数。如果差为零，同和同积迫使 $z=\epsilon\alpha$ 或 $\epsilon\bar\alpha$，与 $K\cap F=\mathbb Q$、$\alpha$ 非实矛盾。其范数是被 $p$ 整除的非零整数，各嵌入绝对值严格小于 $4\sqrt N$，正给 (62.14)。这一步同时处理局部扭曲的符号和负指数，没有假设存在一个全局 CM 提升。

## 5. 任意 t 的界与最优数量的选择

将 (62.6) 的 $k=2t$ 代入 (62.14)，有
$$
\log P<\frac{3^{2t}-1}{2}\log\mathcal B_D
=\frac{9^t-1}{2}\log\mathcal B_D.
$$
因此
$$
\log p<2^{t-1}\log4+
2^{t-3}(9^t-1)m_t\log\mathcal B_D,
$$
即 (62.2)。此式在第 4 节已经单独处理的平凡分支也成立。

现在置
$$
H=\log h>0,\qquad a_0=\log18,
\qquad t=\left\lceil\sqrt{H/a_0}\right\rceil\ge1.
$$
记 $S=18^t h^{1/t}$。从 (62.2) 删除一个负项，且用 $m_t\le h^{1/t}$，得
$$
\log p<2^t\log2+\frac S8\log\mathcal B_D.
\tag{62.15}
$$
若 $u=\sqrt{H/a_0}$，则
$$
a_0t+H/t-2\sqrt{a_0H}
=\frac{a_0(t-u)^2}{t}\le a_0,
$$
从而
$$
S\le18\exp\!\left(2\sqrt{\log18\,\log h}\right).
\tag{62.16}
$$
此外
$$
\frac{2^t}{S}=9^{-t}h^{-1/t}\le\frac19.
$$
联立得
$$
\begin{aligned}
\log p
&<\left(2\log2+\frac94\log\mathcal B_D\right)
\exp\!\left(2\sqrt{\log18\,\log h}\right)\\
&<\frac52\log\mathcal B_D\,
\exp\!\left(2\sqrt{\log18\,\log h}\right).
\end{aligned}
$$
最后一步使用 $\mathcal B_D>256$，它由 $D\ge15$ 保证。证明 (62.3)。

## 6. 消去类数与显式反演

R58 §7 从 Minkowski 界及理想计数证明
$$
h\le B(1+\log B),\qquad B=2\sqrt D/\pi.
$$
当 $D\ge15$，有 $B<\sqrt D$、$1+\log B<\log D$，所以
$$
h<\sqrt D\log D,\qquad
\log h<\frac12\log D+\log\log D.
\tag{62.17}
$$
将其代入 (62.3) 给出 (62.4)。

下面核对 (62.5) 的常数，避免把可反演性只留为定性陈述。令 $x=\log D>5/2$。因为 $\log x\le x/2$ 在该区间成立，
$$
\log h<x/2+\log x\le x.
$$
又 $\log\mathcal B_D=\log8+(5/2)x<4x$。函数
$$
\frac52\sqrt x-\log(10x)
$$
在 $x\ge5/2$ 为正且递增：其导数是
$5/(4\sqrt x)-1/x>0$，左端点的值亦为正。因此
$$
\log\!\left(\frac52\log\mathcal B_D\right)
<\log(10x)<\frac52\sqrt x.
$$
同时 $2\sqrt{\log18}<7/2$。对 (62.3) 取对数，遂有
$$
\log\log p
<\frac52\sqrt x+2\sqrt{\log18\,\log h}
<6\sqrt x.
$$
因为 $p>37$，$\log\log p>0$，平方反演即得
$$
D>\exp\!\left(\frac{(\log\log p)^2}{36}\right).
\tag{62.18}
$$

若保留 (62.4) 的主项，对任何假想 $p\to\infty$ 的本分支异常序列，先由 (62.18) 得 $D\to\infty$，再得
$$
\boxed{
\liminf\frac{\log D}{(\log\log p)^2}
\ge\frac1{2\log18}.}
\tag{62.19}
$$
准确的有效量词是：对每个 $0<\epsilon<1/(2\log18)$，由 (62.4) 可计算一个阈值，阈值之后有
$$
D\ge\exp\!\left[
\left(\frac1{2\log18}-\epsilon\right)(\log\log p)^2
\right].
$$
这不是等价渐近，也不声称下界能被实际异常达到。

## 7. 与主目标的距离

本篇增加的是一个跨变化商域的无条件必要界，不能从中删除 $D$：

- (62.3) 比逐个固定 $K$ 的有效例外集合更具体，但右端仍随 $K$ 的类数和判别式增长。
- (62.18) 对充分大 $p$ 强于任意预先固定次幂的 $\log p$，但没有与任何已证明的判别式上界冲突。
- 假设仍是 $p\equiv1\pmod{12}$、$h_K>1$。平方特征的主理想公式及真实局部二次好约化扭曲均来自这一同余类；不得不经重证直接推广其他剩余类。
- 类数一商域、固定或可变 CM 同余的最终整性、以及 O5 的实际 QC 有限靶逆像均未由本篇解决。

引用接口：[R58](R58-ring-class-splitting-and-small-split-primes.md) 的平方惯性型、主理想公式和 Minkowski 计数；[R61](R61-two-prime-relations-and-discriminant-growth.md) §2 的实迹范数引理。Minkowski 定理的原始参考为 J. S. Milne, *Algebraic Number Theory*, v3.08 (2020), Theorem 4.3，[作者原文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)。其余选择、CRT、短关系及常数估计均在本文展开证明。
