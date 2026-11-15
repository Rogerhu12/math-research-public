# R657 增补 — 原多个 Euler 输出的真实连续前缀

日期：2026-11-15。**状态：以下同来源连续前缀、Smith 上界及固定特征零接触常数均已证明。** 三个完整 Euler 输出的常数可降到 \(25/27\)，四个以上固定输出可降到 \(3/4\)。这些输出没有由原三块或三个不同来源的中央零自动提供；本文不据此关闭 R637。

## 1. 同一原来源与精确行长

沿用 [R657](../results/R657-original-long-ordered-prefix-and-quadratic-contact-bound.md) 和其[两输出增补](2026-11-15-r657-original-two-euler-prefix.md)。保持
\[
p=6s-1>101,\qquad f_D=\lfloor9D/2\rfloor+4<p,
\]
同一个 \(\mathcal W_D\)、全部 \(q_n\) 及十九角、同一个完整 \(\mathcal C_p\)，以及
\[
\Phi(P)=c_*w^{13}U_0e^{40a\epsilon}
P(t(w),g(w)e^{a\epsilon}).
\]
原来源上的算子始终是
\(\mathcal E=Y\partial_Y\)；它对列 \(Y^nq_n(t)t^k\) 乘整数 \(n\)，确实保持同一来源及全部次数帽。

令 \(q\ge1\) 是固定输出数，并观察同一向量的联合评价
\[
\mathcal F_q(P)=
\bigl(\Phi(P),\Phi(\mathcal EP),\ldots,
       \Phi(\mathcal E^{q-1}P)\bigr).
\tag{1}
\]
取 \(p>q\)。原列首阶、余类和补齐数仍是
\[
r_{n,k}=13+A_n+k,\quad
J_n(u)=\left\lfloor\frac{b_n+13-u}{s}\right\rfloor,\quad
C_u=\sum_n(J_n(u)+1)_+,\quad 0\le u<s.
\]
对 \(j,d\ge0\) 定义
\[
N_j(u)=\#\{0\le n\le D:J_n(u)\ge j\},\qquad
C_d(u)=\sum_n(J_n(u)+1-d)_+.
\tag{2}
\]
所以 \(C_0(u)=C_u\) 及 \(C_d-C_{d+1}=N_d\)。

置 \(d=q-1\)，定义
\[
\boxed{
H_u^{(q)}
=\max\left(
\{N_j(u)+j:0\le j<d,\ N_j(u)>0\}
\cup
\{C_d(u)+d:C_d(u)>0\}
\cup\{0\}
\right).
}
\tag{3}
\]
空余类给 \(H_u^{(q)}=0\)。特别
\[
H_u^{(1)}=C_u,\qquad
H_u^{(2)}=\max\{N_0(u),C_1(u)+1\},
\]
其中后式的空尾项按 (3) 删除。

每个非空项都不超过 \(C_u\)，因而
\[
1\le H_u^{(q)}\le C_u\le p
\]
于非空余类。又 (3) 随 \(u\) 不增。令
\[
\boxed{
k_q=1+\max_{H_u^{(q)}>0}
\{u+s(H_u^{(q)}-1)\}.
}
\tag{4}
\]
则
\[
1+s(H_0^{(q)}-1)\le k_q
\le sH_0^{(q)}\le sp.
\tag{5}
\]

**定理 1。** 将 (1) 每个分量都限制到原有序普通行
\[
\gamma_0,\ldots,\gamma_{k-1},
\qquad \gamma_m=p^{-\lfloor6m/p\rfloor}w^m,
\]
若 \(k_q\le k\le ps\)，则此同源 \(qk\times\dim\mathcal W_D\) 矩阵全列单射，其所有 Smith 因子非零，且
\[
\boxed{
e\le\left\lceil\frac{b_D+13}{s}\right\rceil.
}
\tag{6}
\]
这里并未断言 \(\mathcal E\) 保持任何原核，也没有改变 \(\Phi\) 的来源或目标规范。

## 2. 多次导出族的单位消元

取 \(\pi^s=p\)、\(w=\pi z\)。R646/R657 的整缩放已经支付所有 \(t,g,q_n,U_0\) 高尾；固定余类 \(r=u+js\) 的联合列模 \(\pi\) 准确是一个非零列单位乘
\[
\left(
n^iX^j e^{a(n+40)X}
\right)_{0\le i<q},
\qquad X=z^s.
\tag{7}
\]
补齐缺失的较低 \(j\) 只用于独立性证明，不增加实际来源列。

设在这组补齐列中有关系，记各输出
\[
F_i(X)=\sum_{n,j}n^i c_{n,j}X^j e^{a(n+40)X}.
\]
假设它们都消失到 \(X^{H_u^{(q)}}\)。对 \(h\le q-1\)，用这些已有输出组成
\[
\mathcal L^hF_0
:=\sum_{v=0}^{h}\binom hv(-a)^v
\partial_X^{h-v}
\left(\sum_{i=0}^{v}\binom vi40^{v-i}F_i\right).
\tag{8}
\]
完整低阶身份是
\[
\boxed{
\mathcal L^hF_0
=\sum_{n,j\ge h}(j)_h c_{n,j}
X^{j-h}e^{a(n+40)X},
}
\tag{9}
\]
其中 \((j)_h=j(j-1)\cdots(j-h+1)\)。它至少消失到
\(X^{H_u^{(q)}-h}\)。

这里的 \(\mathcal L\) 是 (8) 的显示组合，不是一个已经下降到原物理像上的自由算子。特别它没有从 \(\Phi(P)=0\) 单独推出任何 \(\Phi(\mathcal EP)=0\)。

若原补齐族的最高 \(j\) 小于 \(d\)，将第一步的 \(d\) 换成这个最高 \(j\) 即可，(3) 的值不变。因而可假设第一步的尾非空。由
\[
H_u^{(q)}-d\ge C_d(u),
\]
(9) 在 \(h=d\) 时的首 \(C_d(u)\) 行是完整合流 Vandermonde 单位矩阵：各节点 \(a(n+40)\) 不同，各节点的连续多项式次数为 \(0,\ldots,J_n-d\)。故所有 \(j\ge d\) 的系数消失。

随后逐个处理 \(j=d-1,d-2,\ldots,0\)。高次数系数已经为零，(9) 的 \(h=j\) 式变成至多 \(N_j(u)\) 个不同节点的常系数指数和。条件
\[
H_u^{(q)}-j\ge N_j(u)
\]
使普通 Vandermonde 迫这一层所有 \(c_{n,j}=0\)。因此全部关系系数为零。

**特征 \(p\) 端点。** 每一非空合流族的大小不超过 \(C_u\le p\)，节点的原多项式次数满足 \(j<p\)，所以所有实际使用的 \((j)_h\) 非零。求 \(h\) 次导数时只读取次数
\[
< H_u^{(q)}-h\le p-h.
\]
截断指数的导数误差最低出现在次数 \(p-h\)，正好在读取范围之外。故 (8)、(9) 没有使用 \(p!\)，也不把 \(D(e^{aX})=ae^{aX}\) 无条件延至特征 \(p\) 的不可读端点。

这证明固定余类在首 \(H_u^{(q)}\) 行上独立，而这些行全在 (4) 的连续原前缀内。

最后对 (1) 的 \(q\) 个输出各复制原行权
\[
\omega_m=m-s\lfloor6m/p\rfloor,\qquad
1-s\le\omega_m\le s-1.
\]
同一个单位列满秩矩阵的整左逆作用于 primitive Smith 向量，仍给
\[
se+1-s\le \max r_{n,k}=b_D+13,
\]
取整恰为 (6)。全部高尾在第一步已按实际缩放处理，未在特征零中把不同余类强行拆成直和。

## 3. 固定特征零接触：三个与四个输出

令
\[
F_i(P)=G_0(w)(\mathcal E^iP)(t(w),\mathscr R(w)).
\]
这些是同一个固定特征零原空间中的函数；改变辅助素数不改变它们。由定理 1 的非零有理子式，对每个非零 \(P\) 有
\[
\min_{0\le i<q}\operatorname{ord}_wF_i(P)<k_q.
\tag{10}
\]
恒零输出的阶记为无穷。

取辅助惰性素数满足
\[
p_D/D\longrightarrow\alpha,\qquad \alpha\ge9/2.
\]
固定模数六的算术级数素数定理保证可取最小满足门槛的素数；使用的仍是 Kedlaya, *Notes on analytic number theory*, §4.4, Theorem 4.12，
[作者原文](https://kskedlaya.org/ant/chap-primes-in-ap.html)，不涉及增长模数。

因为 \(b_n=25n/6+O(1)\)，在 \(u=0\) 有
\[
\frac{N_j(0)}D\longrightarrow(1-\alpha j/25)_+,\qquad
\frac{C_d(0)}D\longrightarrow
\sum_{j\ge d}(1-\alpha j/25)_+.
\tag{11}
\]
对固定 \(q\ge2\)，(3)–(5) 的主系数因而是
\[
\boxed{
\frac{\alpha}{6}
\max\left\{1,\ 
\sum_{j\ge q-1}(1-\alpha j/25)_+
\right\}.
}
\tag{12}
\]
其中常数一来自真实 \(N_0(0)=D+1\)，不是免费增加的观察。

### 三个完整输出

取 \(q=3\)。在 \(\alpha=50/9\) 时，
\[
\sum_{j\ge2}(1-\alpha j/25)_+
=\sum_{j=2}^{4}(1-2j/9)=1.
\]
因此
\[
\boxed{
\sup_{P\ne0}\min_{0\le i\le2}\operatorname{ord}F_i(P)
\le\left(\frac{25}{27}+o(1)\right)D^2.
}
\tag{13}
\]

这一常数在本篇消元界 (12) 的允许辅助比例中最优。对
\(9/2\le\alpha\le5\)，尾和为 \(4-14\alpha/25\)；对
\(5\le\alpha\le50/9\)，为 \(3-9\alpha/25\)。乘以 \(\alpha/6\) 后均为凹二次式，故最小值在区间端点。三个端点依次给
\[
111/100,\qquad 1,\qquad25/27.
\]
对 \(\alpha\ge50/9\)，(12) 至少为 \(\alpha/6\ge25/27\)。这只优化显示的估计，不声称是原三输出的最优接触定理。

### 四个及更多固定输出

取任意固定 \(q\ge4\)，并选 \(\alpha=9/2\)。已经在 \(q=4\) 时有
\[
\sum_{j\ge3}(1-\alpha j/25)_+
=(1-27/50)+(1-36/50)+(1-45/50)
=\frac{21}{25}<1.
\]
更大的 \(q\) 只减少该尾和。所以
\[
\boxed{
\sup_{P\ne0}\min_{0\le i<q}\operatorname{ord}F_i(P)
\le\left(\frac34+o(1)\right)D^2,\qquad q\ge4\text{ 固定}.
}
\tag{14}
\]
(12) 本身的下界为 \(\alpha/6\ge3/4\)，故这是本消元界的最小主系数。

各已付常数如下；所有行都属于同一固定未正规 \(G_0\mathcal W_D\)：

| 完整 Euler 输出数 | 所用辅助 \(p_D/D\) | 共同接触主系数 |
|---:|---:|---:|
| 1 | \(9/2\) | \(99/40\) |
| 2 | \(25/3\) | \(25/18\) |
| 3 | \(50/9\) | \(25/27\) |
| 任意固定 \(q\ge4\) | \(9/2\) | \(3/4\) |

## 4. 原旧截止为什么尚不能用第三输出

数值上
\[
\frac{25}{27}<\frac{47}{48},\qquad
\frac34<\frac{47}{48}.
\tag{15}
\]
但 (15) 不是原 R637 的核排除。必须分别保留以下两个范围。

首先，旧相对 \(J\) 的原三块只给
\[
P(t,g)\equiv0\pmod{w^s},\qquad
(\mathcal EP)(t,g)\equiv0\pmod{w^s},\qquad
(\mathcal E^2P)(t,g)\equiv0\pmod{w^\ell}
\]
这一类实际约化条件；在旧 \(J_A\) 中前两个长度还须减十三。第三块的长度是原 \(\ell\)，不是 \(s\)。本文 (13) 则要求同一个 \(P\) 的三个**完整联合输出**具有共同前缀。单凭 \(\mathcal E\mathcal W_D\subset\mathcal W_D\) 不能扩大第三块。

在本消元机制中，这个差别可直接看到：若前两输出长度为 \(H\)，第三输出只有长度 \(H_2\)，则 (8) 的二次组合只能保证消失到
\[
\min\{H-2,H_2\}.
\tag{16}
\]
要杀掉大小 \(C_2(u)\) 的真实尾，仍必须
\(H_2\ge C_2(u)\)。原固定低 \(\ell\) 没有提供这个随 \(D\) 增长的完整观察。式 (16) 本身也只是对应联合指数模型的精确读取规则，不能将旧第三块免费识别成新的全 \(\Phi(\mathcal E^2P)\)。

其次，(13)、(14) 是由可选择辅助素数的有理非零子式得到的**特征零**接触界。某个实际目标素数处的模 \(p\) 原核，不因此在另一个辅助素数处或特征零中消失。实际局部使用必须回到定理 1 的同一 \(p\)、准确 \(k_q\) 及 Smith 权；不能只比较 (15) 的数值常数。

三个原 \(S,T,U\) 的完整中央零也不是同一 \(P\) 的
\(F_0(P),F_1(P),F_2(P)\) 共同高接触。它们属于三个指定算术来源，现有证明没有把它们变成这里的 Euler 输出，也未给任何原核的 \(\mathcal E\) 稳定性。

因此本增补支付的是可明确检验的额外输出条件及其精确收益；它没有支付这些额外条件。原同一 \(R\)、全部十九角、两个十三行带、完整 \(P_{134}/U_0\)、Padé 高尾及指定第二余类仍按 R651/R637 保持。
