# 小辅助素数、两有理点的短关系与非零正局部化

日期：2026-11-12。状态：完整证明；R121。环境恢复后依据已独审文本重建。

固定 \(E:y^2=x^3-17x\)、\(F=\mathbb Q(\sqrt{-15})\)，以及 R4 的两个独立点
\[
 P_1=(-1,4),\qquad P_2=(9,24).
\]
令 \(\mathcal P_F\) 为同时在 \(F,\mathbb Q(i)\) 分裂、除去固定坏素数的素数集合。
本篇把 R116 的实际完整 Heegner 迹非零选择，与一个新的局部条件合并：
在相对密度一的输入 \(p\) 上，可使有理 Mordell–Weil 群在辅助位的模 \(p\) 局部化非零。
这不预先指定该局部化的核线，也不声称负符号局部化非零。

## 1. 一个完全初等的坏素数预算

设 \(\ell\) 为好素数，满足
\[
 \#E(\mathbb F_\ell)=\ell+1=pu,\qquad v_p(\ell+1)=1.
 \tag{1}
\]
其中 \(\ell\equiv3\pmod4\) 保证本 CM 曲线 \(a_\ell=0\)。
若 \(P_1,P_2\) 在 \(E(\mathbb F_\ell)/pE(\mathbb F_\ell)\) 中都为零，则其约化
都落在阶恰为 \(u\) 的群 \(pE(\mathbb F_\ell)\)。
取 \(N=\lceil\sqrt u\rceil\)。盒子
\[
 \{aP_1+bP_2:0\le a,b\le N\}
\]
有 \((N+1)^2>u\) 个标号，故有两个不同标号的约化相同。
因此存在不全为零的整数 \(a,b\)，\(|a|,|b|\le N\)，使
\[
 R_{a,b}=aP_1+bP_2\equiv O\pmod\ell.
 \tag{2}
\]
独立性保证 \(R_{a,b}\) 是非挠点，特别不是 \(O\)。

把有理横坐标写成互素形式
\[
 x(R_{a,b})=A_{a,b}/B_{a,b}^{\,2},\qquad B_{a,b}>0.
\]
好约化处 (2) 等价于 \(\ell\mid B_{a,b}\)。
典范高度的二次性，以及 \(h(x(R))=2\widehat h(R)+O_E(1)\)，给出
\[
 \log B_{a,b}\le\widehat h(R_{a,b})+O_E(1)
       \ll_E a^2+b^2+1.
 \tag{3}
\]
对 \(U\ge1\)，定义真正非零的整数
\[
 D_U=\prod_{\substack{|a|,|b|\le\lceil\sqrt U\rceil\\(a,b)\ne(0,0)}}B_{a,b}.
 \tag{4}
\]
重复的横坐标或正负点只增加重数；分母为 \(1\) 的因子也无害。
由 (3)，
\[
                      \log D_U=O_E(U^2).
 \tag{5}
\]
于是对 \(\ell\in(Y,2Y]\) 且 \(u\le U\)，两点同时模 \(p\) 局部化为零的不同素数
总数至多
\[
                  \frac{\log D_U}{\log Y}
                  =O_E(U^2/\log Y).
 \tag{6}
\]
同一个 \(D_U\) 对所有这些 \(p,\ell\) 通用；没有对每个输入重新支付一次高度。

## 2. 与实际完整迹非零的选择合并

固定 \(32/17<\theta<2\)。R110/R116 的 Mikawa–Fouvry 输入给出：
除 \(O(X/\log^2 X)\) 个 \(p\in\mathcal P_F\cap(X,2X]\) 外，每个输入有
\[
 \gg X^{\theta-1}/\log X
 \quad\text{个候选}\quad
 \ell\in(X^\theta,2X^\theta],\qquad \ell\equiv-1\pmod{1020Cp},
 \tag{7}
\]
其中 \(C\) 是 R116 固定的非零进程常数。充分大时
\[
 \ell+1<p^2,\qquad u=(\ell+1)/p\le 2X^{\theta-1}+1.
 \tag{8}
\]
一个 \(\ell\) 至多属于一个区间内的输入 \(p\)：否则两个大于 \(X\) 的不同素数之积
整除 \(\ell+1<X^2\)，矛盾。

令 \(U=\lceil2X^{\theta-1}+1\rceil\)。R116 的首 jet 坏候选总数是
\(O(X^{2\theta-2})\)；(6) 新增的双局部零候选只有
\[
                      O(X^{2\theta-2}/\log X).
 \tag{9}
\]
将两者的并集删除。全部候选都被删除的典型输入至多为
\[
 O(X^{\theta-1}\log X)=o(X/\log X).
 \tag{10}
\]
因此，对 \(\mathcal P_F\) 中相对密度一的 \(p\)，可同时选到
\[
 \begin{gathered}
 Q_{p,\ell}=\operatorname{Tr}_U(1+\tau_3)P[\ell]\ne O,\qquad
 Q_{p,\ell}\notin pE(F[\ell]),\\
 v_\ell\log_E([2]Q_{p,\ell})=1/p,\qquad
 \operatorname{im}\bigl(\langle P_1,P_2\rangle\to
             E(\mathbb F_\ell)/pE(\mathbb F_\ell)\bigr)\ne0.
 \tag{11}
 \end{gathered}
\]
逐二进区间累加 (10) 即给通常的相对自然密度一。
R123 后可把 (7) 的模数直接改成 \(1020p\)；本篇的局部预算不变。

## 3. 准确的 Selmer 符号结论

\(\ell\) 在 \(F\) 惰性，故剩余域是 \(\mathbb F_{\ell^2}\)。
限制与迹的复合是乘 \(2\)，因此对奇素数 \(p\)，
\[
 E(\mathbb F_\ell)/pE(\mathbb F_\ell)
   \longrightarrow E(\mathbb F_{\ell^2})/pE(\mathbb F_{\ell^2})
 \tag{12}
\]
单射。又因 \(a_\ell=0\)、\(\ell\equiv-1\pmod p\)，Frobenius 在 \(E[p]\) 上的
两特征值为 \(+1,-1\)，彼此不同。故 (12) 的像是 usual 局部 Kummer 空间的
一维正符号直线。

令 \(r_+\) 为全局通常 \(\operatorname{Sel}_p(E/F)^+\) 在这一局部直线的像维数。
有理点的 Kummer 类属于该全局 Selmer 群，所以 (11) 给 \(r_+\ge1\)；
局部直线一维又给 \(r_+\le1\)。因此
\[
                              \boxed{r_+=1.}
 \tag{13}
\]
这没有指定 \(E(\mathbb Q)/p\) 中哪一条线是核，也没有证明 \(r_-=1\)。
它更不把局部非零换成 \(Q\notin\delta A(F)\)：辅助位上的 \(\delta\) 形式群除法
仍然存在，剩余问题是全局整格饱和。

## 4. 来源与证明边界

- 典范高度的二次性及与横坐标高度的有界差：J. S. Milne，
  [Elliptic Curves, 2nd ed.](https://www.jmilne.org/math/Books/EC2.pdf)，IV §4，
  Lemma 4.5、Theorem 4.7、Lemma 4.11。这里只使用固定曲线、固定两点的标准高度估计。
- 小辅助素数的精确输入及不重复性：
  [R110](../results/R110-density-one-small-heegner-auxiliary-primes.md)。
- 实际完整迹、首 jet 和非 \(p\) 可除性：
  [R116](../results/R116-density-one-nonzero-full-heegner-traces.md)。
- (2)–(6) 的同时跨输入乘积预算、(11)–(13) 的合并是本篇证明。

