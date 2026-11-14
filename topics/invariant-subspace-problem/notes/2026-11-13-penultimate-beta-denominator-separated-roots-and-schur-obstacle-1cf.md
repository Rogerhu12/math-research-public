# 工作接口：倒数第二出生块的 Beta 分母、严格分离实根与矩阵分子障碍

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / kernel_resume_1cf。

本文是后续相邻比较的工作接口，不登记一般 primitive 上界。并发去重：R239 原稿的新 §8 已独立证明全部外实根及归一化倒数的正矩。本文 §2 保留另一条自足递推和额外根间隔信息作为工作记录，不重新登记已有外实根；新增障碍与矩阵亏损明确列于 §§3–4。使用 [R239 倒数第二出生块](../results/R239-appendix-penultimate-primitive-fixed-block-exact-one-parameter-inverse.md) 的真实一参数最小逆。该稿已经付清全部 Hilbert 最小解和两端，下面只研究其内部标量分母；不重计原 MP 公式。

## 1. 与真实积分的准确对应

头数为 $q$，$z_i=a_i^2>0$，池大小为 $L\ge q$，令
$$
h=L-q+2,\qquad 0<n<h,\qquad d=h-n.
$$
定义上升阶乘 $(x)_r=x(x+1)\cdots(x+r-1)$ 和有限多项式
$$
P_q^h(n;z)=\sum_{R\subseteq[q]}z_R(n)_{|R|}(h-n)_{q-|R|}.
\tag{1.1}
$$
真实最小逆中消去标量参数的分母为
$$
M_n=\sum_R\frac{z_R}{\binom L{n+|R|-1}}
=\frac{\Gamma(n)\Gamma(h-n)}{\Gamma(L+1)}P_q^h(n;z).
\tag{1.2}
$$
(1.2) 在真实整数内部阶成立，也给实开区间中的正积分延拓；后者只用来讨论这个标量函数，不替代任何算子域。

在原积分中作 $p=t/(1+t)$，其正测度（除共同正因子外）准确变为
$$
p^{n-1}(1-p)^{d-1}
\prod_i(1-p+z_i p)\,dp,\qquad 0<p<1.
\tag{1.3}
$$
在实际内部整数 $n,d\ge1$，其 log 密度是凹函数。条件独立 Bernoulli 概率为
$$
r_i(p)=\frac{z_i p}{1-p+z_i p},
\qquad
r_i(1-r_i)=p(1-p)r_i'(p).
\tag{1.4}
$$
这些恒等式保留原 Schur 极小化；正测度本身不自动给相邻矩阵序。

## 2. 分母的严格实根结构

**有限多项式引理。** 取任意实 $h>1$ 和任意正 $z_i$。删去等于一的 $z_i$ 后，$P_q^h$ 恰有

- $\#\{i:z_i>1\}$ 个负实根；
- $\#\{i:z_i<1\}$ 个大于 $h$ 的实根。

所有根都为单根，任意相邻两根的距离严格大于一。特别 $[0,h]$ 上没有零点。等于一的头参数只贡献一个准确正因子，不贡献有限根。

### 2.1 两个递推

按最后一个头是否入选分组，直接由上升阶乘得到
$$
P_q^h(n;z',z)
=(h-n)P_{q-1}^{h+1}(n;z')
+znP_{q-1}^{h+1}(n+1;z').
\tag{2.1}
$$
若 $z=1$，同样逐项有
$$
P_q^h(n;z',1)=(h+q-1)P_{q-1}^{h}(n;z').
\tag{2.2}
$$
所以可先删去所有单位参数，余下只需考虑 $z\ne1$。其最高系数是 $\prod_i(z_i-1)$，次数恰为余下头数。

### 2.2 有单位间隔的旧根给准确正留数

对头数归纳。设
$$
P(n)=P_{q-1}^{h+1}(n;z')
$$
的全部根为 $r$。归纳假设给它们在 $(-\infty,0)$ 或 $(h+1,\infty)$，且相邻距离大于一。于是
$$
\frac{P(n+1)}{P(n)}
=1+\sum_r\frac{w_r}{n-r},
\qquad
w_r=\frac{P(r+1)}{P'(r)}
=\prod_{r'\ne r}\frac{r+1-r'}{r-r'}>0.
\tag{2.3}
$$
这里所有因子的正性正是旧根间隔严格大于一；没有另设交错性。

令 $Q$ 为 (2.1) 的右侧。则
$$
\frac{Q(n)}{P(n)}
=h+(z-1)n+z\sum_r\frac{w_r n}{n-r}.
\tag{2.4}
$$
在负根处该有理函数的留数为负，在正根处为正；并且
$$
\frac{Q(r-1)}{P(r-1)}=h-r+1.
\tag{2.5}
$$
$P(r-1)\ne0$ 仍由旧根间隔保证。另有
$$
Q(0)/P(0)=h>0,\qquad
Q(h)/P(h)=zh\,P(h+1)/P(h)>0.
\tag{2.6}
$$

### 2.3 全部根的位置、数目与新间隔

把负旧根记为 $r_1<\cdots<r_m<0$。

对每个 $i<m$，(2.4) 在 $r_i$ 的右侧趋于 $-\infty$，而 (2.5) 在 $r_{i+1}-1$ 为正。因此每个区间
$$
(r_i,r_{i+1}-1)
$$
内至少有一个新根。另在 $(r_m,0)$ 内有一个新根。若 $z>1$，还在 $(-\infty,r_1-1)$ 内有一个；$m=0$ 时这最后一个区间直接换成 $(-\infty,0)$。

把正旧根记为 $s_1<\cdots<s_l$，它们全部大于 $h+1$。由 (2.5)–(2.6)，在
$$
(h,s_1-1),\qquad
(s_i,s_{i+1}-1)\quad(i<l)
$$
各有一个新根。若 $z<1$，另在 $(s_l,\infty)$ 内有一个；$l=0$ 时直接换成 $(h,\infty)$。

这些区间互不相交，总共给恰好 $\deg Q=q$ 个根。因此所有根都已列出、每个都是单根、每个区间内只有一个；没有余下非实根。由各根严格位于这些开区间，相邻新根的距离严格大于一。跨越负、正两群的距离大于 $h>1$。这完成归纳，也给所述负根和正根的准确个数。常数初始情形直接成立。

这一证明是有限差分的明确符号论证，不依赖数值根求解或浮点谱计算。

## 3. 这仍不是矩阵相邻序：一个准确分子障碍

本节的分子实根测试取实源坐标 $x$。写真实 Schur 矩阵的标量测试为
$$
H_n[x]=A_x(n)-\frac{b_x(n)^2}{M_n}.
$$
移去共同 Beta 因子后，分母是 (1.1)，但分子
$$
C_x(n)=P(n)\,\mathcal A_x(n)-\mathcal b_x(n)^2
$$
并不一般具有全实根。已经在两个头时出现准确反例。

取
$$
q=2,\quad h=4,\quad (z_1,z_2)=(2,1/3),\quad x=(-2,-1).
$$
把全部子集质量共同乘三，直接展开得
$$
\widetilde P(n)=60+3n-2n^2,
$$
$$
\widetilde{\mathcal b}_x(n)=7n^2-58n,
\qquad
\widetilde{\mathcal A}_x(n)=118n-7n^2.
$$
故
$$
\boxed{
\widetilde P\,\widetilde{\mathcal A}_x
-\widetilde{\mathcal b}_x^2
=5n(4-n)(7n^2-83n+354).
}
\tag{3.1}
$$
最后二次因子的判别式为
$$
83^2-4\cdot7\cdot354=-3023<0.
$$
所以不能把 §2 延伸为“所有 covariance 分子也全实根”，再按 Gamma 极点逐一配对来免费得到矩阵上界。

本例不反相邻序；两个头的真实相邻序已有完整证明。它仅排除这一更强的分子实根入口。

### 3.1 完整协方差分子也不能独立当作正矩

上述复根现象只谈多项式根。另有一个更直接、只用四个位的真实有限反例，排除“先证明完整分子 $P(n)H_n$ 为正矩，再乘已知的 $1/P(n)$ 正矩”这一入口。

取
$$
q=2,\quad L=2,\quad h=2,\quad z_1=z_2=z>0.
$$
用源显示坐标 $x_i=f_i/a_i$，取 $x=(1,-1)$。源是合法非零 primitive 向量。原零阶、内部一参数方差及最高阶三式直接给
$$
H_0[x]=2z,\qquad H_1[x]=z,\qquad H_2[x]=2z.
$$
例如中间阶的两个单头质量各为 $z/2$，而空头、全头上的 $x$ 和都为零；平均也为零。因此中间式没有被试探上界代替。

同一真实分母多项式为
$$
P(0)=6,\qquad P(1)=2(1+z+z^2),\qquad P(2)=6z^2.
$$
对完整分子序列 $B_n=P(n)H_n[x]$，准确有
$$
\frac{B_1^2}{B_0B_2}
=\frac{(z+1+z^{-1})^2}{36}.
$$
取 $z=10$，其二阶 Hankel 块就是
$$
\begin{pmatrix}120&2220\\2220&12000\end{pmatrix},
\qquad
\det=-3488400<0.
$$
所以完整分子本身连相邻正块都不满足。使用归一化 $Z_A=P/(h)_q$ 只把所有 $B_n$ 共同除六，仍为反例。

原真实 $H_n[x]$ 的相邻比却恒为 $1/4$，所以本反例不否定原相邻比较；它要求分子与 $1/P$ 必须被整体处理，不能给二者分别赠送正矩。

## 4. 两个秩一损失的准确二维写法

所需结论仍是同一源坐标上的
$$
H_nH_{n+1}^{-1}H_n\le C H_{n-1}.
$$
只在三个阶都为内部阶的 $2\le n\le h-2$，使用下面的概率写法。联合变量为原正积分中的 $(T,I)$，其中 $T=t>0$，$I$ 是头子集的指标列。若使用原 $f$ 坐标，把 $I_i$ 换成 $I_i/a_i$ 即可；以下固定这种同一真实线性坐标，仍记该 $q$ 维列为 $I$。

把第 $n$ 个联合测度除以其质量 $M_n$，记
$$
u=I-\mathbb EI,\quad
p_0=\mathbb ET,\quad q_0=\mathbb ET^{-1},
\quad v=\mathbb E(Tu),\quad w=\mathbb E(T^{-1}u).
$$
三个真实 Schur 矩阵只除以同一个质量 $M_n$ 后准确为
$$
\widehat H_{n+1}=\mathbb E(Tuu^*)-vv^*/p_0,\quad
\widehat H_n=\mathbb E(uu^*),\quad
\widehat H_{n-1}=\mathbb E(T^{-1}uu^*)-ww^*/q_0.
\tag{4.1}
$$
帽号并不是分别按各阶质量归一化。

令 $2q$ 维随机列和二维常数测试列分别为
$$
Y=\begin{pmatrix}T^{-1/2}u\\T^{1/2}u\end{pmatrix},
\qquad
c=\begin{pmatrix}T^{-1/2}\\T^{1/2}\end{pmatrix}.
$$
置
$$
G=\mathbb E(YY^*),\quad
K=\mathbb E(cc^*)=
\begin{pmatrix}q_0&1\\1&p_0\end{pmatrix},\quad
B=\mathbb E(Yc^*)=
\begin{pmatrix}w&0\\0&v\end{pmatrix}.
\tag{4.2}
$$
这里 $G$ 为 $2q$ 阶矩阵，$K$ 为二阶，$B$ 为 $2q$ 行二列；两个零块的准确性用的是 $\mathbb Eu=0$。

当 $p_0q_0>1$ 时，联合 Gram 的 Schur 补
$$
S=G-BK^{-1}B^*
$$
为正。直接取二阶逆，所求相邻块准确等于
$$
\boxed{
\begin{pmatrix}
\widehat H_{n-1}&\widehat H_n\\
\widehat H_n&\widehat H_{n+1}
\end{pmatrix}
=
S+\frac1{p_0q_0-1}
B\begin{pmatrix}1/q_0&-1\\-1&1/p_0\end{pmatrix}B^*.
}
\tag{4.3}
$$
中间二阶矩阵只有一个负符号方向；因此亏损确已集中，而未被省去。

若 $p_0q_0=1$，Cauchy--Schwarz 等号迫 $T$ 几乎处处为常数。这时 $v=w=0$，
$$
\begin{pmatrix}
\widehat H_{n-1}&\widehat H_n\\
\widehat H_n&\widehat H_{n+1}
\end{pmatrix}
=
\begin{pmatrix}
q_0\widehat H_n&\widehat H_n\\
\widehat H_n&p_0\widehat H_n
\end{pmatrix}\ge0,
$$
不对奇异 $K$ 取逆。本实际 Beta 密度在整个正轴为正，故真实内部情形总有 $p_0q_0>1$。

端点 $n=1$ 或 $n=h-1$ 仍须用原 R239 的固定参数公式；发散的质量 $M_0$、$M_h$ 不能代入 (4.1)–(4.3)。

一般正矩的 Schur 不自动保持 (4.3) 的正性。特殊 Beta/Bernoulli 恒等式若能付清其唯一负方向，才会得到系数一的界。[已发表的双复制正矩附录](../results/R271-appendix-penultimate-primitive-interior-adjacent-uniform-bound.md) 已支付任意头数的内部系数至多四；它不支付这里的系数一，也不支付两个端点。

## 5. 文献位置与去重

有限差分保持实根及根间隔的一般背景可见 Brändén--Krasikov--Shapiro, *Elements of Pólya--Schur theory in the finite difference setting*, Proceedings of the AMS 144 (2016), 4831--4843, DOI [10.1090/proc/13115](https://doi.org/10.1090/proc/13115)，[作者公开全文](https://staff.math.su.se/shapiro/Articles/FiniteDifference.pdf)。本稿 §2 给与实际分母、两侧根数及合法区间相符的自足递推，不以该文标题代替具体证明。

[三异权全出生证明](../results/R271-appendix-three-exceptional-weights-full-birth-one-primitive-gram-bound.md) 的负参数多项式证书已完成三个头的真矩阵序；这里不重新登记它，也不把 (2.3) 的标量正留数认成整个 Schur 矩阵的正留数。
