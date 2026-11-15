# R627 — 原 theta 的完整首坏带与实际 S/T 幂的单位二行

日期：2026-11-15。**状态：已证明。**

R625 给原未去 Gaussian 的 theta 幂在 $(e+1)L$ 前的整性及首坏端点。
本篇支付紧接端点的整个长度 $s$ 的真实普通系数带。
除端点外，答案是同一原对数的低系数乘一个准确二项式，
不是一个另选 gauge 的替代来源。

在 $1\le e\le5$，原 $S,T$ 的两个实际 $p^e$ 次幂
在这个完整前缀内具有一个单位二行。
其源系数范数准确等于输出系数范数除以 $p$。
原参考 $H_{38}=T/S$ 的端点相消后，第一个坏系数也被确定，
恰在 $(e+1)L+1$。
全部来源次数仍为 $p^e$；本篇不增加中央零或全局旗标结论。

## 1. 同一来源与完整带公式

固定
$$
p=6s-1>71,\qquad L=(p^2-1)/6=(p-1)s,\qquad b=17.
\tag{1}
$$
保 R625 的原点规范
$$
\mathcal F=\sigma^m x^\alpha(-y)^\beta Q(t),\quad
t=b/x^3,\quad d=m-2\alpha-3\beta,\quad
B(w)=z^{-d}\mathcal F(z),\quad w=z^6.
$$
这里 $Q\in1+t\mathbf Z_p[[t]]$ 为原固定正则单位，
$m,\alpha,\beta$ 为整数；$B(0)=1$。令
$$
\mathscr L_B(w)=\log B(w)=\sum_{r\ge1}\ell_{B,r}w^r.
\tag{2}
$$
应用于 $f_4,f_1,S,T,H_{38}$ 时，
这是各自的原完整来源及原固定多项式，没有删除任何因子。

对
$$
1\le e\le p-2,\qquad q=e+1,
\tag{3}
$$
R625 已证明 $f_e=B^{p^e}$ 的全部 $n<qL$ 系数整。

**定理1（完整首坏带）。** 对每个 $0\le r<s$，
$$
[w^{qL+r}]f_e\in p^{-1}\mathbf Z_p.
\tag{4}
$$
端点仍为
$$
\boxed{
p[w^{qL}]f_e
\equiv\frac{(-1)^{q-1}d}{q}\,b^{qL}\pmod p.
}
\tag{5}
$$
其余整条带准确为
$$
\boxed{
p[w^{qL+r}]f_e
\equiv b^{qL}\binom{6r}{q}\ell_{B,r}\pmod p,
\qquad 1\le r<s .
}
\tag{6}
$$
右边每个 $\ell_{B,r}$ 都 $p$ 整。
当 $q>6r$ 时，显示二项式确为零；
此时 (4) 中相应实际系数又是整的。
这只支付当前带，不删除更高带或其他真实行。

## 2. 实际参数的全部坏因子

仍用
$$
u=x^{-1/2},\quad t=bu^6,\quad z=uH(t),\quad
C(t)=(1+t)^{-1/2},
$$
$$
H_n=\frac{C_n}{6n+1},\qquad
C_n=(-1)^n4^{-n}\binom{2n}{n}.
\tag{7}
$$
设
$$
N=(p-1)L+s-1.
$$
则 $6N+1=p^3-p^2-3<p^3$。
若 $p\mid6n+1$，最低 $p$ 位为 $p-s>p/2$，
所以 $\binom{2n}{n}$ 至少有一次进位。
因此在整个 $n\le N$ 窗口，$H_n$ 至多有一次分母。

与 R625 同样，将所有整系数放入 $H_0$、其余完整保留在 $T$，得到
$$
H=H_0+p^{-1}T,\qquad
H_0\in1+t\mathbf Z_p[t]/t^{N+1},\qquad
T\in t^L\mathbf Z_p[t]/t^{N+1}.
\tag{8}
$$
R619 的全 $n<2L$ 估计给
$$
\boxed{
T_L\equiv-1\pmod p,\qquad
T_{L+i}=0\quad(1\le i<L).
}
\tag{9}
$$
(8) 中 $2L$ 以后可能存在的其他坏系数全保留。
读取 $qL+r$、$r<s<L$ 时，恰有 $q$ 个坏因子的项
只能使用 (9) 的第一个系数；较少坏因子的项将在下一节严格降阶。

## 3. 原对数的整条最高分母

写
$$
F=\log(\sigma/z),\qquad W=z^2x,\qquad Y=-z^3y.
$$
原形式留数恒等式为
$$
X_n=[w^n]W=b^n[t^n]CH^{1-6n},\qquad
F_n=-\frac{X_n}{6n(6n-1)},
\tag{10}
$$
$$
[w^n]\log W=-\frac{b^n}{3n}[t^n]H^{-6n},
\tag{11}
$$
$$
[w^n]\log Q(t(w))
=\frac{b^n}{n}[t^{n-1}]\frac{Q'}QH^{-6n}.
\tag{12}
$$
另外 $2\log Y=3\log W+\log(1+t)$，且
$$
\mathscr L_B=mF+\alpha\log W+\beta\log Y+\log Q.
\tag{13}
$$

### 3.1 较少坏因子的全部项严格降阶

令 $n=qL+r$，$0\le r<s$。
在 (10) 中，第 $j$ 个坏因子的外系数为
$$
-\frac1{6n(6n-1)}\binom{1-6n}{j}p^{-j}.
$$
当 $j=1$，它等于 $p^{-1}/(6n)$；
当 $j\ge2$，准确等于
$$
-\frac{p^{-j}}{j(j-1)}
\binom{-1-6n}{j-2}.
\tag{14}
$$
对 $2\le j<q<p$，乘 $p^q$ 后至少含一个 $p$。

$j=0$ 的额外分母至多 $p^2$，因为 $6n<p^3$。
若 $q\ge3$，已经严格低于 $p^{-q}$。
若 $q=2$，则
$$
6n=2p^2+6r-2,\qquad 6n-1=2p^2+6r-3.
$$
$0\le6r\le p-5$，且 $6r$ 不等于二或三；
所以这两个数都不被 $p^2$ 整除，仍严格低于 $p^{-2}$。

$j=1$ 的损失至多三。
对 $q\ge4$ 严格低于 $q$。
对 $q=2,3$，$6r=q$ 无整数解，
而 $-p<6r-q<p$，故 $p\nmid6n$；
此项只损失一个 $p$，也严格低于 $q$。

在 (11)、(12) 中，$j\ge1$ 时分别使用
$$
-\frac1{3n}\binom{-6n}{j}
=\frac2j\binom{-6n-1}{j-1},
$$
$$
\frac1n\binom{-6n}{j}
=-\frac6j\binom{-6n-1}{j-1}.
\tag{15}
$$
所以 $1\le j<q$ 同样严格降阶。
$j=0$ 至多损失 $v_p(n)\le2$；
$q=2$ 时 $p\nmid n$，$q\ge3$ 时损失严格小于 $q$。
这支付所有较少坏因子的项，包括可能的 $p^2$ 指标；
没有只保形式上的唯一最大项而漏掉外分母。

### 3.2 恰有 q 个坏因子的原系数

由 (9)，$T^q$ 在所需普通尾内只有首项贡献。
又因
$$
6n\equiv-q+6r\pmod p,\qquad r<p,
$$
$H_0$ 的指数可在模 $p$、次数至多 $r$ 的有限环中按模 $p$ 改写：
常数一的 $H_0^p$ 在这个范围等于一。

对 (10)，于是
$$
p^qF_{qL+r}\equiv
\frac{(-1)^{q+1}b^{qL+r}}{q!}
\prod_{j=2}^{q-1}(j-6r)\,
[t^r]CH^{1-6r}\pmod p.
\tag{16}
$$
空积为一。对 $r\ge1$，用
$X_r=-6r(6r-1)F_r$，全部因子准确变成下降阶乘，得到
$$
\boxed{
p^qF_{qL+r}
\equiv b^{qL}\binom{6r}{q}F_r\pmod p
\quad(1\le r<s).
}
\tag{17}
$$
对 $r=0$，(16) 给
$$
p^qF_{qL}\equiv(-1)^{q+1}b^{qL}/q.
\tag{18}
$$

同样，(11) 的最高项为
$$
-\frac{2b^{qL+r}}q\binom{6r-1}{q-1}
[t^r]H^{-6r}.
$$
对 $r\ge1$，用 (11) 及
$(6r/q)\binom{6r-1}{q-1}=\binom{6r}{q}$，得到
$$
p^q[w^{qL+r}]\log W
\equiv b^{qL}\binom{6r}{q}[w^r]\log W.
\tag{19}
$$
其 $r=0$ 值为 $2(-1)^qb^{qL}/q$。

(12) 的最高项是
$$
\frac{6b^{qL+r}}q\binom{6r-1}{q-1}
[t^{r-1}]\frac{Q'}QH^{-6r}.
$$
故 $r\ge1$ 时仍有完全同样的式子
$$
p^q[w^{qL+r}]\log Q
\equiv b^{qL}\binom{6r}{q}[w^r]\log Q.
\tag{20}
$$
$r=0$ 时该项为零，因为还须保留 $Q'$ 的一次普通指标。
以 $Q=1+t$ 使用 (20)，也完整支付 $\log Y$。

综上，所有原对数在这条带至多损失 $q$ 个 $p$，而
$$
\boxed{
p^q\ell_{B,qL+r}
\equiv b^{qL}\binom{6r}{q}\ell_{B,r}
\quad(1\le r<s).
}
\tag{21}
$$
端点由 (13)、(18)–(20) 恰为
$$
p^q\ell_{B,qL}
\equiv\frac{(-1)^{q+1}(m-2\alpha-3\beta)}q\,b^{qL}.
\tag{22}
$$
这里仍是原 $d$，不是 sigma 次数 $m$。

## 4. 从原 log 到真实 p 幂：完整指数分母

不能直接以“指数低项不影响”代替此步：
原第一 Gaussian 的多次乘积可能带来阶乘分母。
以下在完整有限环中处理它们。

令
$$
A(w)=\sum_{n<qL}[w^n]f_e\,w^n.
\tag{23}
$$
R625 保证 $A\in1+w\mathbf Z_p[w]$。
对 $1\le i<s$，原 $B$ 的这些系数整，
且所有相关乘积次数小于 $p$，所以
$$
\boxed{A_i\in p^e\mathbf Z_p\quad(1\le i<s).}
\tag{24}
$$

当 $e\ge2$，还有所需较长的实际估计
$$
\boxed{A_i\in p^{e-1}\mathbf Z_p\quad(1\le i<L).}
\tag{25}
$$
证明使用原 R614 的
$B=U_B\exp(mc w^s)$、$U_B$ 在 $n<L$ 整且 $v_p(c)=-1$。
在 $U_B^{p^e}$ 的二项式展开中，次数 $i<L<p^2$ 只读
$1\le j<p^2\le p^e$；
$$
v_p\binom{p^e}{j}\ge e-v_p(j)\ge e-1.
$$
Gaussian 的所需幂次数最多 $p-2$，阶乘为单位，
每个正项也至少有 $e-1$ 个 $p$。
相乘得到 (25)，原 Gaussian 没有被删除。

**引理。** 对每个 $n=qL+r$、$0\le r<s$，
$$
[w^n]\log A\in\mathbf Z_p.
\tag{26}
$$

若 $p\nmid n$，这是
$n[w^n]\log A=[w^{n-1}]A'/A$。
若 $p\mid n$，由 $-p<6r-q<p$ 必有
$$
q=6r,\quad e=q-1\ge5,\quad n=rp^2.
$$
展开 $\log A=\sum_{j\ge1}(-1)^{j+1}(A-1)^j/j$。
$p\nmid j$ 的项整。
若 $p\mid j$，则 $j\ge p$；
因为 $n< pL$，每个贡献乘积至少有一个正指标 $i<L$。
它由 (25) 提供 $p^{e-1}$。
另一方面 $j\le n<p^3$，故 $v_p(j)\le2<e-1$。
所以每个这样的项仍整，得到 (26)。
这里明确支付了 $n=rp^2$ 的例外，未把它当单位指标。

$f_e/A-1$ 从 $w^{qL}$ 起，而 $2qL>qL+s-1$。
故在整个所读带中准确有
$$
f_e
=A\{1+\log f_e-\log A\}.
\tag{27}
$$
括号的差在低于 $qL$ 的所有次数均为零。
(21)–(22) 及 (26) 说明
$p(\log f_e-\log A)$ 在当前带整。
再用 (24)，(27) 的正低阶 $A_i$ 项全部在乘 $p$ 后消失模 $p$。
因此
$$
p[w^{qL+r}]f_e
\equiv p^{e+1}\ell_{B,qL+r}\pmod p.
\tag{28}
$$
这同时给 (4)，并由 (21)–(22) 得 (5)–(6)。
定理1证毕。

## 5. 同一原 S/T 的单位二行及准确有限前缀范数

原归一对象是
$$
B_S=w^{-1}S,\qquad B_T=w^{-1}T,
$$
其原始数据为
$$
(m,\alpha,\beta,d)_S=(34,14,0,6),\qquad
(m,\alpha,\beta,d)_T=(72,33,0,6).
$$
保 R625 的全部 $Q_S,Q_T$。原低行给
$$
\ell_{S,1}=-\frac{988}{105}b,\qquad
\ell_{T,1}=-\frac{2938}{35}b,\qquad
\boxed{\ell_{T,1}-\ell_{S,1}=-\frac{1118}{15}b.}
\tag{29}
$$
也可直接由 $F_1=b/210$、$[w]\log W=-b/7$、
$[t]Q_S=-53/7$、$[t](Q_T/Q_S)=-72$ 算出 (29)。
所以其差只含已排除的小素因子 $2,13,43$ 与分母 $3,5$。

现在限
$$
1\le e\le5,\qquad 2\le q=e+1\le6.
\tag{30}
$$
对两个真实列 $B_S^{p^e},B_T^{p^e}$，
读原普通行 $qL,qL+1$，并将整块乘一个 $p$。
定理1给其模 $p$ 矩阵
$$
\boxed{
b^{qL}
\begin{pmatrix}
6(-1)^{q-1}/q & 6(-1)^{q-1}/q\\
\binom6q\,\ell_{S,1} & \binom6q\,\ell_{T,1}
\end{pmatrix}.
}
\tag{31}
$$
其准确行列式为
$$
\boxed{
\frac{2236(-1)^q}{5q}\binom6q\,b^{2qL+1}
\in\mathbf Z_p^\times,
\qquad2236=4\cdot13\cdot43 .
}
\tag{32}
$$
$p>71$ 使所有显示因子为单位。
这不是自由选两条辅助来源；
两列就是原 $S,T$ 的实际幂。

令 $\|\cdot\|_{\le M}$ 为普通 Taylor 系数到 $w^M$ 的最大
$p$ 进绝对值，规范 $|p|_p=p^{-1}$。
因为 $qL$ 前每列整、随后这两行至多一次分母，
(31)–(32) 给完整的范数等式
$$
\boxed{
\|a B_S^{p^e}+c B_T^{p^e}\|_{\le qL+1}
=p\max(|a|_p,|c|_p)
\quad(a,c\in\mathbf Q_p).
}
\tag{33}
$$
上界来自定理1和 R625 的整个前缀；
下界来自 (31) 的单位二行逆，故也覆盖任意系数的相消。

原未归一来源的共同首阶不可遗漏：
$$
S^{p^e}=w^{p^e}B_S^{p^e},\qquad
T^{p^e}=w^{p^e}B_T^{p^e}.
\tag{34}
$$
因此对原两列，(33) 的截断应准确改为
$p^e+qL+1$。
这确实是这两个来源的完整普通前缀范数；
它不声称加入所有其他原列后仍保同一个二行逆。

## 6. 原参考 H38 的端点相消和首坏位置

原参考
$$
H_{38}=T/S=\sigma^{38}x^{19}Q_H(t),\qquad
Q_H=(1+4t)(1-96t+48t^2+64t^3)(1+20t-8t^2)
$$
具有 $d=0$、$H_{38}(0)=1$。
它的全部低项、质量一和原相位保持既有定义。

由 R625，$H_{38}^{p^e}$ 在 $n<qL$ 整。
定理1的端点 (5) 为零，所以 $n=qL$ 也整。
对 (30)，第一后继行由 (6)、(29) 为
$$
\boxed{
p[w^{qL+1}]H_{38}^{p^e}
\equiv
-\frac{1118}{15}\binom6q b^{qL+1}
\in\mathbf F_p^\times .
}
\tag{35}
$$
因此对 $1\le e\le5$，
$$
\boxed{
qL+1\text{ 是原 }H_{38}^{p^e}\text{ 的首个非整指标，
赋值准确为 }-1.
}
\tag{36}
$$
不能因原点阶数为零而把它的整性无限延长。
对较高 $e$，(6) 的准确二项式继续适用；
例如 $q>6$ 时第一后继行也整。
本篇没有对那些后继首坏指标作未证断言。

## 7. 实际来源预算、中央与全局边界

(31) 中每条原来源的幂次数是 $p^e$，且 (34) 有实际普通首阶。
因此它们不是原固定 $D$ 帽内的免费两列。
若在仅含 $S,T$ 的有理来源格中使用 $H_{38}^{p^e}$，
还须保 $S^{p^e}$ 的真实分母成本；
已固定参考来源也不能因此取得新的中央零。

全部结论均来自原形式级数，未假设原 $j_S,j_T$ 为零。
所以 (32)、(35) 的实际单位不是原中央非零的替代品。
本篇支付的是完整首坏带、原双来源的有限前缀范数及参考幂的准确首坏行。
若要接全局九格成本，仍须在同一实际预算下运输整来源和每个真饱和层，
不能只以这两个高行取代全局旗标。

## 依赖

- [R625](R625-original-theta-powers-integral-window-and-first-bad-coefficient.md)：
  同一原 $B^{p^e}$ 的完整前整窗、实际 $H$ 坏因子和有限 Frobenius 引理。
- [R619](R619-original-cartier-sparse-rows-and-second-newton-block.md)：
  原 $H$ 在 $n<2L$ 唯一一次极点及 $pH_L=-1$。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：
  第一 Gaussian 后的完整 $n<L$ 整窗；只用于 (25) 的实际低系数估计。
- [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)：
  原 $S,T$、全部固定多项式及低行规范。

本篇是全参数形式留数、有限指数和单位二行证明；
没有新增素数扫描，也没有以未执行代码支持结论。
