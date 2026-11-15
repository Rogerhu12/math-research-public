# R625 — 原 theta 的 p 幂完整整窗与准确首坏系数

日期：2026-11-15。**状态：已证明。**

本篇回到未去 Gaussian 的原 theta 来源。
对原 $f_4,f_1,S,T$ 的归一函数 $B=z^{-d}\mathcal F$，
证明全部
$$
1\le e\le p-2
$$
的真实 $p^e$ 次幂，在 $n<(e+1)(p^2-1)/6$ 的整个普通系数窗口内整。
其紧邻端点恰有一次分母，绝对 residue 只读原点阶数 $d$。

证明使用实际 $H$ 参数的全窗口估计、精确留数和有限
Frobenius 整性引理。$e=1$ 的特殊相消正由 R619 的原第二
Gaussian residue 支付；更高 $e$ 则保每一个坏 $H$ 因子。
这是真正的原来源幂，不是另选 Gaussian 后的替代函数。

## 1. 原归一来源与结论

固定
$$
p=6s-1>71,\qquad L=\frac{p^2-1}{6},\qquad b=17,
$$
并保持同一 $y^2=x^3+b$ 的原点参数和 sigma。
所有系数在 $\mathbf Q_p$，整性相对于 $\mathbf Z_p$。
原共同 $b=1$ frame 同样适用；物理单位运输须同时保原来源。

设
$$
\mathcal F(z)=\sigma(z)^m x(z)^\alpha(-y(z))^\beta
 Q\!\left(\frac b{x(z)^3}\right),
$$
其中 $Q\in1+t\mathbf Z_p[[t]]$ 是当前原固定多项式或原点正则单位，
$m,\alpha,\beta$ 为固定整数，且
$$
d=m-2\alpha-3\beta,\qquad
B(w)=z^{-d}\mathcal F(z),\quad w=z^6,\qquad B(0)=1.
\tag{1}
$$
所用 log 均为常数一的形式 log，允许先在 $\mathbf Q_p[[w]]$
中计算。本文应用的四条原来源为：

| 原来源 | $m$ | $\alpha$ | $\beta$ | $d$ |
|---|---:|---:|---:|---:|
| $f_4=x\sigma^6$ | $6$ | $1$ | $0$ | $4$ |
| $f_1=-xy\sigma^6$ | $6$ | $1$ | $1$ | $1$ |
| $S$ | $34$ | $14$ | $0$ | $6$ |
| $T$ | $72$ | $33$ | $0$ | $6$ |

前两条的 $Q=1$。后两条保持 R595 的完整
$$
Q_S(t)=\frac{(1+t)(1-8t)(7-4t+16t^2)}7,
$$
$$
Q_T(t)=Q_S(t)(1+4t)
(1-96t+48t^2+64t^3)(1+20t-8t^2).
\tag{2}
$$
因此全部 $Q$ 在当前素数处确为原点整单位；
没有删去 $S/T$ 的任何低项。

**主定理。** 对每个整数 $1\le e\le p-2$，置 $q=e+1$。
则
$$
\boxed{
[w^n]B(w)^{p^e}\in\mathbf Z_p
\qquad(0\le n<qL),
}
\tag{3}
$$
并且
$$
\boxed{
p[w^{qL}]B(w)^{p^e}
\equiv\frac{(-1)^e d}{e+1}\,b^{qL}\pmod p.
}
\tag{4}
$$
对表中四条原来源，$d$ 和 $e+1$ 都是 $p$ 单位，
所以 $qL$ 正是第一个非整系数，赋值准确为 $-1$。
特别 $e=1$ 时，该 residue 为 $-db^{2L}/2$。

本篇的 $B$ 没有去掉第一 Gaussian。
(3) 与 R614 对去 Gaussian 后的 $U$ 所给整窗是不同的准确结论。

## 2. H 在整个所需大窗口至多有一次分母

保持实际参数
$$
u=x^{-1/2},\quad t=bu^6,\quad z=uH(t),\quad dz=C(t)du,
$$
$$
C(t)=(1+t)^{-1/2},\qquad
C_n=(-1)^n4^{-n}\binom{2n}{n},\qquad
H_n=\frac{C_n}{6n+1}.
\tag{5}
$$
令
$$
N_*=(p-1)L.
$$
当 $0\le n\le N_*$ 时，
$$
6n+1\le(p-1)(p^2-1)+1<p^3.
$$
所以分母至多含两个 $p$。

若 $p\mid6n+1$，写 $n=pa+r$，则
$r=p-s=5s-1>p/2$。
在 $n+n$ 的最低 $p$ 进位上已有一次进位，
所以 $p\mid\binom{2n}{n}$。
这可直接由阶乘估值的进位公式读取，不要求更高位无进位。
因此一次分母必被消去，两次分母至多剩一次。
最早的 $p^2$ 分母在 $n=L$。
R616 已准确给 $pH_L\equiv-1\pmod p$。

故在整个所需截断中存在实际分解
$$
\boxed{
H=H_0+p^{-1}T,\qquad
H_0\in1+t\mathbf Z_p[t]/t^{N_*+1},\quad
T\in t^L\mathbf Z_p[t]/t^{N_*+1},\quad
T_L\equiv-1\pmod p.
}
\tag{6}
$$
例如保留全部整系数于 $H_0$，把非整系数移入 $p^{-1}T$ 即可。
后面可能还有其他一次极点，它们全在 $T$ 中，
没有假设只有 $H_L$ 一个坏系数。
只有它的首次位置和绝对 residue 用于端点。

## 3. 原 log sigma 的逐坏因子估计

令
$$
F=\log(\sigma/z),\qquad W=z^2x.
$$
原准确留数和 sigma 方程给
$$
X_n=[w^n]W=b^n[t^n]CH^{1-6n},\qquad
F_n=-\frac{X_n}{6n(6n-1)}.
\tag{7}
$$
对固定 $n\le N_*$，将 (6) 展开。
第 $j$ 个坏因子项为
$$
-\frac{b^n}{6n(6n-1)}
 \binom{1-6n}{j}p^{-j}
 [t^n]\,C H_0^{1-6n-j}T^j.
\tag{8}
$$
只有 $jL\le n$ 时才贡献。
除显示分母外，全部剩余系数均整。

两处准确消去至关重要。
当 $j=1$，外系数变成
$$
\frac{b^n}{6n}\,p^{-1}.
\tag{9}
$$
当 $j\ge2$，用整数二项式恒等式得到
$$
-\frac{1}{6n(6n-1)}
 \binom{1-6n}{j}
=-\frac{1}{j(j-1)}
 \binom{-1-6n}{j-2}.
\tag{10}
$$
所以在 $2\le j<p$ 时，这部分的赋值至少为 $-j$，
没有额外的 $6n$ 或 $6n-1$ 分母。

现在设 $2\le e\le p-2$、$n<(e+1)L$。
(8) 中 $j\le e<p$。
$j=0$ 的分母赋值至多为二，因为 $6n<p^3$ 且两个因子相邻；
$j\ge2$ 由 (10) 给至多 $e$ 次分母。
$j=1$ 的成本至多 $1+v_p(n)$：
当 $e=2$，$n<3L<p^2$，成本至多二；
当 $e\ge3$，$n<N_*<p^3$，成本至多三。
因此
$$
\boxed{
p^eF_n\in\mathbf Z_p
\quad(2\le e\le p-2,\ 0<n<(e+1)L).
}
\tag{11}
$$

此外，若 $k<L$，则 $X_k$ 整且 $6k<p^2$，从而
$$
v_p(F_k)\ge-1.
\tag{12}
$$
此处只是 log 的估计；指数整性将在 §5 完整支付。

## 4. 原椭圆单位和 Q 的全部 log 分母

由 $W=H(t(z))^2$ 和
$t=bwH(t)^{-6}$，Lagrange–Bürmann 公式给
$$
\boxed{
[w^n]\log W
=-\frac{b^n}{3n}[t^n]H(t)^{-6n}.
}
\tag{13}
$$
对 (6) 的第 $j\ge1$ 项，
$$
-\frac1{3n}\binom{-6n}{j}
=\frac2j\binom{-6n-1}{j-1}.
\tag{14}
$$
所以 $j<p$ 时只保 $p^{-j}$，没有再丢一个 $n$ 分母；
$j=0$ 的损失至多为 $v_p(n)$。

对任意显示的原 $Q$，令 $R(t)=\log Q(t)$。
$R'=Q'/Q\in\mathbf Z_p[[t]]$，所以
$$
\boxed{
[w^n]R(t(z))
=\frac{b^n}{n}[t^{n-1}]R'(t)H(t)^{-6n}.
}
\tag{15}
$$
第 $j\ge1$ 项的外系数由
$$
\frac1n\binom{-6n}{j}
=-\frac6j\binom{-6n-1}{j-1}
$$
准确消去 $n$。
同时该项至少消耗 $jL$ 的 $t$ 次数；
由于 (15) 读取 $n-1$，它在 $n=jL$ 时不能贡献。

最后，$Y=-z^3y$ 的原点常数为一，且
$$
Y^2=W^3(1+t(z)).
$$
因此
$$
2\log Y=3\log W+\log(1+t(z)).
\tag{16}
$$
$2$ 是当前单位。
(13)–(16) 对原所有椭圆因子给：
$$
\boxed{
p^e[w^n]\{\alpha\log W+\beta\log Y+\log Q(t(z))\}
\in\mathbf Z_p
}
\tag{17}
$$
对 $2\le e\le p-2$、$n<(e+1)L$ 成立。
同一证明也给 $e=1$、$n<2L$ 的结论，
因为这时 $j\le1$ 且 $v_p(n)\le1$。

在 $k<L$ 的低窗中，这些单位本身系数整；
其 log 系数估值至少为 $-v_p(k)\ge-1$。
若再有 $k<p$，则这些低 log 系数全整。

令
$$
\mathcal B=\log B
=mF+\alpha\log W+\beta\log Y+\log Q(t(z)).
\tag{18}
$$
综上，
$$
p^e\mathcal B_n\in\mathbf Z_p
\quad(2\le e\le p-2,\ n<(e+1)L),
\qquad
v_p(\mathcal B_k)\ge-1\quad(k<L).
\tag{19}
$$

## 5. 有限 Frobenius 整性引理和完整指数

为避免将 log 整误当指数整，先证明所用有限引理。

**有限整性引理。**
对 $f\in1+w\mathbf Q_p[[w]]$ 和任意 $N$，
其 $0\le n\le N$ 系数全整，当且仅当
$$
f(w^p)/f(w)^p\in1+pw\mathbf Z_p[[w]]
\pmod{w^{N+1}}.
\tag{20}
$$
正向由特征 $p$ 的 Frobenius 同余。
反向对 $n$ 归纳：若前 $n$ 项已整，
取整多项式 $f_0=[f]_{<n}$，
则 $f/f_0=1+a_nw^n+O(w^{n+1})$。
它的 Frobenius 比在第 $n$ 项为 $-pa_n$，
而 $f_0$ 已满足正向。
故 (20) 迫 $a_n$ 整。
这支付每一项，未预先假定 $f$ 是整级数。

因 $p$ 为奇数，形式 log 和 exp 在
$1+pw\mathbf Z_p[[w]]$ 与 $pw\mathbf Z_p[[w]]$
间互逆，截断后同样成立：
第 $r$ 次幂的 $r$ 或 $r!$ 分母都被其至少 $r$ 个 $p$ 吸收。
将 (20) 应用于 $f=\exp(p^e\mathcal B)=B^{p^e}$，得到准确判据
$$
\boxed{
B^{p^e}\text{ 在 }n\le N\text{ 整}
\iff
p^{e-1}\{\mathcal B(w^p)-p\mathcal B(w)\}
\text{ 在 }n\le N\text{ 整}.
}
\tag{21}
$$

若 $2\le e\le p-2$、$n<(e+1)L$，
第二项由 (19) 整。
第一项只在 $p\mid n$ 出现；
此时 $k=n/p<L$，(19) 的 $v_p(\mathcal B_k)\ge-1$
与 $e-1\ge1$ 支付它。
因此 (21) 完整证明 (3) 的所有 $e\ge2$。

还须付 $e=1$ 的真实例外。
R619 已证明在 $n<2L$ 内，
$pF_n$ 只有 $n=ps$ 可能非整，且
$$
p^2F_{ps}\equiv b^Lpc\pmod p,\qquad c=F_s.
\tag{22}
$$
在 $k<2L/p<p$ 中，$F_k$ 唯一非整项为 $k=s$。
所以 $F(w^p)-pF(w)$ 唯一需要检查的位置也是 $ps$；
其 residue 为
$$
pF_s-p^2F_{ps}
\equiv(1-b^L)pc=0\pmod p.
$$
这里 $b\in\mathbf Z_p^\times$，$L$ 为 $p-1$ 的倍数，
所以 $b^L\equiv1$。
两个项原来至多一次分母，显示相消使它们之差整。

其余椭圆和 $Q$ 的 log 部分，在 $k<p$ 的第一项整，
在 $n<2L$ 的第二项由 (17) 整。
故整个 $\mathcal B(w^p)-p\mathcal B(w)$ 整。
(21) 也支付 $e=1$，而非把第二 Gaussian 端点省略。

## 6. 唯一最高极部及原点阶数 d

现在固定 $2\le q\le p-1$，令 $n=qL$。
在 (8) 中，恰好有 $q$ 个坏因子的项只能取
$T_L^qt^{qL}$；其他因子只取常数一。
由 (10)，并用
$$
-1-6qL\equiv q-1\pmod p,
$$
得到
$$
\boxed{
p^qF_{qL}
\equiv\frac{(-1)^{q+1}}q\,b^{qL}\pmod p.
}
\tag{23}
$$
全部 $j<q$ 的项估值严格大于 $-q$：
$j\ge2$ 用 (10)，$j=1$ 用 $p\nmid qL$，
$j=0$ 至多含一次 $p$；
即便 $q=p-1$ 使 $6qL-1$ 被 $p$ 整除，这个剩余分母仍只有一次。
所以 (23) 保了全部更低坏因子项。

同理由 (13)–(14)，
$$
\boxed{
p^q[w^{qL}]\log W
\equiv\frac{2(-1)^q}{q}\,b^{qL}\pmod p.
}
\tag{24}
$$
(15) 在 $n=qL$ 无 $q$ 坏因子项，
因此该式的 $p^q$ residue 为零。
结合 (16)，
$$
p^q[w^{qL}]\log Y
\equiv\frac{3(-1)^q}{q}\,b^{qL}.
$$
最后代入 (18)，准确得到
$$
\boxed{
p^q\mathcal B_{qL}
\equiv\frac{(-1)^{q+1}}q
(m-2\alpha-3\beta)b^{qL}
=\frac{(-1)^{q+1}d}{q}b^{qL}
\pmod p.
}
\tag{25}
$$
这解释了为什么该端点读原点阶数 $d$，
而不是只读 sigma 次数 $m$。
原 $Q_S,Q_T$ 的全部项已经通过 (15) 保留，
并非因为不出现在 residue 中就被从来源删除。

## 7. 从 log 端点返回原实际幂

取 $q=e+1$。
由 §5，$f=B^{p^e}$ 的系数在 $n<qL$ 整。
令 $f_0=[f]_{<qL}$。
因 $p\nmid qL$，
$$
[w^{qL}]\log f_0\in\mathbf Z_p,
$$
这是 $w f_0'/f_0$ 整和 $qL$ 为单位的直接结果。
而形式恒等式给
$$
[w^{qL}](\log f-\log f_0)=[w^{qL}]f.
$$
因此
$$
p[w^{qL}]f
\equiv p^{e+1}\mathcal B_{qL}
=\frac{(-1)^e d}{e+1}b^{qL}\pmod p,
$$
即 (4)。
当 $d$ 为单位，该系数准确有一次分母。
这也证明前面的整窗不能向后一项免费延长。

特别，对原 $S,T$：
$$
\boxed{
[w^n]S^{p^e},\ [w^n]T^{p^e}\in\mathbf Z_p
\quad(0\le n<p^e+(e+1)L),
}
\tag{26}
$$
以及同一准确端点
$$
\boxed{
p[w^{\,p^e+(e+1)L}]S^{p^e}
\equiv
p[w^{\,p^e+(e+1)L}]T^{p^e}
\equiv\frac{6(-1)^e}{e+1}b^{(e+1)L}\pmod p.
}
\tag{27}
$$
原首项 $w^{p^e}$ 已显式保留。
对 $f_4,f_1$，同样保各自的 $z^{dp^e}$ 再读取余下 $w$ 系数。

## 8. 原来源预算与仍未解决的中央问题

(26)–(27) 确实属于原多项式来源：
$S^{p^e}$、$T^{p^e}$ 的真实来源次数是 $p^e$。
所以在 $E_{D,9}$ 中使用它们，必须有 $D\ge p^e$；
不能在 $p>D$ 的窗口把这些幂当作免费列。

它们的原首项系数在 $w^{p^e}$ 已为一。
因此 (27) 的后续非整系数并不自动位于一个非空真前缀的首行。
也不能从两条端点相同就给 $S^{p^e}-T^{p^e}$ 的后续行赋零；
更长坏带须使用完整原卷积。

本篇完全不假设原 $j_{34}$、$j_{72}$ 为零。
所以这些整窗不能重新解释成由算术失败新增的约束。
它们支付原 Frobenius 升幂的确切整性和费用，
供后续真实来源运算使用；无穷中央非零仍需继续。

## 依赖

- [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)：
  原 $Q_S,Q_T$、实际参数和完整来源规范。
- [R616](R616-original-first-bad-band-and-pth-newton-endpoint.md)：
  原 $pH_L=-1$ 与绝对尺度。
- [R619](R619-original-cartier-sparse-rows-and-second-newton-block.md)：
  $n<2L$ 中唯一二阶 log 极部及实际 $ps$ 相消。
- [R583](R583-nine-coordinate-inert-resonance-absorption-and-sharp-envelope.md)：
  原次数格与连续真前缀的量词。

全篇为原函数的全参数证明，没有新增素数扫描。
