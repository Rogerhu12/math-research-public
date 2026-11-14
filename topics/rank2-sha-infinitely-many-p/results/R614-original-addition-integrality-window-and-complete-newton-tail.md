# R614 — 原完整 addition 的高度二整窗与强化 Newton 全尾

日期：2026-11-14。**状态：已证明。**

去掉原第一个 Gaussian 后，sigma 余项的整系数范围远大于 R602 的 $n<p$ 窗口。本篇用完整二变量 sigma 加法式，证明它在 $n<(p^2-1)/6$ 全整，并支付紧接着的两段真实分母界。该边界的首坏项是显示单位，不能把窗口继续当成整。

这些界应用于同一个原 $S/T$ 规范化分子，使前 $p-1$ 个完整 Newton 余项都整。所有更高项仍由本篇分段界与 R602 的无限尾共同控制；在精度 $p^p$，必须另保 $h=p$ 的实际端点。这里没有把一个高阶非中央单位当成原中央非零。

## 1. 同一原来源与高度二输入

取
\[
p=6s-1>71,\qquad
L=\frac{p^2-1}{6}=s(p-1),\qquad w=z^6,\qquad b=17.
\]
原规范为
\[
y^2=x^3+b,\quad x\sim z^{-2},\quad y\sim-z^{-3},
\quad x'=2y,\quad \sigma\sim z.
\]
记
\[
W(w)=z^2x(z)=1+\sum_{n\ge1}X_nw^n,\qquad
Y(w)=-z^3y(z)=W-3wW',
\]
\[
F(w)=\log(\sigma(z)/z),\quad c=F_s,\quad d=p+1=6s.
\tag{1}
\]
R301 的原高度二估计，按 R602 (2)–(3) 的整数赋值版本，是
\[
v_p(X_n)\ge-\lfloor n/L\rfloor,\qquad
F_n=-\frac{X_n}{6n(6n-1)},\qquad v_p(c)=-1.
\tag{2}
\]

允许已经由 R606 付清的任何整 Gaussian 改变
$c'=c+\eta$、$\eta\in\mathcal O$，并定义真实余项
\[
\boxed{U(z)=\frac{\sigma(z)}z\exp(-c'z^d)
=\sum_{n\ge0}u_nz^{6n},\qquad u_0=1.}
\tag{3}
\]
整个证明在这个同一个实际级数上进行。
尤其包括原 $c$ 和 R606 的规范 $c^\dagger$。

## 2. 完整二变量 addition 和实际整数核

原 sigma 加法式准确给
\[
\frac{\sigma(z+t)\sigma(z-t)}{\sigma(z)^2\sigma(t)^2}
=x(t)-x(z).
\]
将全部首项与同一个 Gaussian 移到两边，得到
\[
\boxed{
U(z+t)U(z-t)
=\mathcal R(z,t)U(z)^2U(t)^2\exp(\mathcal E(z,t)),
}
\tag{4}
\]
其中
\[
\mathcal R(z,t)=
\frac{z^2t^2}{z^2-t^2}\{x(t)-x(z)\}
=1-\sum_{n\ge1}X_n
 \sum_{j=1}^{3n-1}z^{6n-2j}t^{2j},
\tag{5}
\]
\[
\mathcal E=c'\{2z^d+2t^d-(z+t)^d-(z-t)^d\}
=-2c'\!\!\sum_{\substack{2\le j\le p-1\\j\ {\rm even}}}
 \binom{p+1}{j}z^{p+1-j}t^j .
\tag{6}
\]
(5) 是准确除去 $z^2-t^2$ 后的多项式齐次分块，没有分式展开的选择。

对 (6) 的每一个指标，
\[
v_p\binom{p+1}{j}=1.
\]
因为 $v_p(c')=-1$，$\mathcal E$ 的所有系数整，且其总次数为 $d$。
因此：

- 总次数 $<p(p+1)$ 时，$\exp\mathcal E$ 只使用 $k!$ 中 $k<p$ 的项，全部整；
- 总次数 $<2(p^2-1)$ 时，只使用 $k\le2p-3$，所以全部系数赋值至少 $-1$；
- 第二种范围内可能不整的项，总次数至少为 $p(p+1)$。

这些是完整指数的有限次数事实，不把所有阶乘一律当成单位。

## 3. 偶二项式中的全部例外

**引理 1。** 若 $N$ 是六的正倍数且
$N<2(p^2-1)$，则除了
\[
N=p+1,\qquad N=p(p+1),
\tag{7}
\]
总存在一个偶数 $j$，$0<j<N$，使 $\binom Nj$ 为 $p$ 单位。

证明将 $N$ 写为基 $p$ 数字。因为 $p$ 为奇数，数字和与 $N$ 同为偶数。
若数字和至少为四，可以从数字中选两个单位形成一个非零真子数 $j$；
$1,p,p^2$ 全是奇数，故此 $j$ 为偶数。
Lucas 公式给 $\binom Nj\not\equiv0\pmod p$。

若数字和为二，在该范围内的可能数仅是
\[
2,\ p+1,\ 2p,\ p^2+1,\ p^2+p.
\]
其中六的倍数恰为 (7)，因为 $p\equiv-1\pmod6$。
数字和为零只给 $N=0$，已排除。这证明引理。

在 (4) 的总次数 $6n$ 上，把含 $u_n$ 的全部项移到左边，准确成为
\[
u_n\{(z+t)^{6n}+(z-t)^{6n}-2z^{6n}-2t^{6n}\}
=\text{只含 }u_i\ (i<n)\text{ 及已知核的多项式}.
\tag{8}
\]
所以只要不在 (7)，用引理给出的单个真实偶混合系数，
便可除以单位 $2\binom{6n}{j}$。
这一步保整个 addition，而非只保一个单变量截断。

## 4. 高度二完整整窗和后两段分母

**定理 2。** 对 (3) 的全部实际系数，
\[
\boxed{
\begin{array}{ll}
u_n\in\mathcal O,&0\le n<L,\\[2pt]
v_p(u_n)\ge-1,&L\le n<ps=L+s,\\[2pt]
v_p(u_n)\ge-2,&ps\le n<2L.
\end{array}}
\tag{9}
\]
这些结论对所有 $c'-c\in\mathcal O$ 同时成立。

### 4.1 $n<L$ 的整性

由 (2)，(5) 在总次数 $<6L=p^2-1$ 全整。
(6) 的完整指数在此也整。
依 $n$ 归纳，(8) 的已知项全部整；
引理 1 除了 $n=s$ 外，给一个单位除数。

对唯一例外 $n=s$，R602 已证明
$F-cw^s$ 的全部 $n<p$ 系数整。
减去 $\eta w^s$ 后仍如此。
计算 $u_s$ 只使用阶乘 $k!$、$k\le s<p$，所以 $u_s$ 也整。
这补齐整个归纳，没有假定例外行自动可除。

### 4.2 $L\le n<ps$ 的一次分母界

此范围内 $n<2L$，所以 (2) 给 $X_n$ 至多一次分母。
完整指数仍整，因为 $6n<p(p+1)$。
所有已经可能不整的 $U$ 系数都从指标 $L$ 起，
总次数指标 $n<ps<2L$ 时，任何一个乘积至多含一个这样的系数。
同理，(5) 的一次分母项不能同时与一个不整 $U$ 项出现。
因此 (8) 全部已知项的赋值至少为 $-1$。
这里没有新的例外指标，单位除法给所需界。

### 4.3 $n=ps$ 的真实例外除法

第二个例外必须另付。置
\[
\log U=\sum_{k\ge1}f^\circ_kw^k,\qquad
h_k=kf^\circ_k.
\]
由已经证明的 $U\bmod w^L$ 整且常数项一，
\[
h_k\in\mathcal O\qquad(1\le k<L).
\tag{10}
\]
这是对整单位作真实对数导数，不声称其对数系数全整。

对于 $L\le k\le ps$，该区间的模 $p$ 余数为
$5s-1,\ldots,p-1,0$，不含 $s$。
故 $6k-1$ 是单位，且 $k\ne s$，由 (2)
\[
h_k=-\frac{X_k}{6(6k-1)},\qquad v_p(h_k)\ge-1.
\tag{11}
\]
实际指数递推为
\[
ps\,u_{ps}=\sum_{k=1}^{ps}h_ku_{ps-k}.
\tag{12}
\]
若 $k<L$，(10) 整而另一因子赋值至少 $-1$；
若 $k\ge L$，则 $ps-k\le s<L$，另一因子整。
所以右边赋值至少为 $-1$。
由于 $v_p(ps)=1$，得到 $v_p(u_{ps})\ge-2$。

### 4.4 $ps<n<2L$ 的二次分母界

现在 (6) 的完整指数系数赋值至少为 $-1$，
而其不整项只从指标 $ps$ 起。
(5) 的不整项从 $L$ 起；$U$ 的不整项也从 $L$ 起。
总指标小于 $2L$，所以乘积不能含两个 $U$ 坏项，
也不能同时含一个坏 $X$ 项和一个坏 $U$ 项。
指数的坏项更不能与这些项同时出现，因为 $ps>L$。

已经在 (12) 付清的 $U$ 二次分母可以单独出现，
所以 (8) 的所有已知项仍至少为 $-2$。
引理 1 在此没有别的例外，单位除法完成归纳。证毕。

## 5. 边界的实际非零首分母

为了给 (9) 的第一个边界定绝对值，使用 R615 的同一个
\[
C_n=(-1)^n4^{-n}\binom{2n}{n},\qquad H_n=C_n/(6n+1).
\]
其逐位进位证明直接给 $H_n$ 在 $n<L$ 整。
对唯一首坏指标
\[
L=p(s-1)+(5s-1),\qquad 6L+1=p^2,
\]
低位二项式恰有一次进位，而高位没有第二次。
R615 (10) 的同一单位阶乘计算因而给
\[
pH_L=C_L/p
\equiv\delta(2s-1)C_{s-1}
=-2s\delta C_s=-1\pmod p,
\tag{13}
\]
其中 $\delta C_s=3$、$6s\equiv1\pmod p$。

原留数
\[
X_L=b^L[t^L]CH^{1-6L}
\]
中，顶系数 $H_L$ 只出现一次。
它在 $C$ 中的系数是 $6L+1$，在 $H^{1-6L}$ 中的系数是 $1-6L$；
和为二。其余项只用整的低系数。因此
\[
\boxed{pX_L\equiv-2b^L\pmod p.}
\tag{14}
\]
原 $Y=W-3wW'$ 同时给 $pY_L\equiv-3b^L$。

再用 (10) 的整低对数导数和 $L$ 处的真实指数递推，
只有 $h_L$ 能贡献一次分母：
\[
\boxed{
pu_L\equiv-\frac{pX_L}{6L(6L-1)}
=b^L\pmod p.
}
\tag{15}
\]
$L\equiv-1/6\pmod p$，两个显示分母都是单位。
原 $b=17$ 下 $b^L=1$，因为 $L=s(p-1)$。
所以 $u_L$ 的赋值准确为 $-1$。
这既核定整窗的端点，也没有将有限整窗宣称为最大解析半径。

## 6. 全部原规范化分子的同一分段界

同一 Gaussian 下，原两 Euler forcing 的余项是
\[
G_4=WU^6,\qquad G_1=WYU^6 .
\tag{16}
\]
原算术来源记为
\[
\mathscr G_m=A_m e^{-mc'w^s}=wG_m,\quad
m=34,72,\quad A_{34}=S_b,\quad A_{72}=T_b.
\]
按 R595/R602 的完整原多项式，
\[
G_{34}=U^{34}\sum_{i=0}^4(P_S)_i\,b^iw^iW^{14-3i},
\]
\[
G_{72}=U^{72}\sum_{i=0}^{10}(P_T)_i\,b^iw^iW^{33-3i}.
\tag{17}
\]
所有 $W$ 幂非负；固定分母只含当前单位。
这与原 $b=17$ 和 $E_{24}$ 的已付物理单位运输相容。

对 (16)、(17) 的任一真实系数 $g_n$，(9) 准确给
\[
\boxed{
g_n\in\mathcal O\ (n<L),\qquad
v_p(g_n)\ge-1\ (n<ps),\qquad
v_p(g_n)\ge-2\ (n<2L).
}
\tag{18}
\]
理由是总指标 $<2L$ 的乘积至多含一个指标 $\ge L$ 的因子；
固定整数幂和原有限分子不会增加分母。
$W,Y$ 自身在同一范围内满足 (2) 给出的更强界。

由 (14)–(17)，各首坏系数还准确为
\[
\boxed{
p[w^L]G_4=4b^L,\qquad
p[w^L]G_1=b^L,\qquad
p[w^L]G_{34}=p[w^L]G_{72}=6b^L
\pmod p.
}
\tag{19}
\]
例如原 $S$ 的贡献是 $34-2\cdot14=6$，
原 $T$ 的贡献是 $72-2\cdot33=6$；
所有带正 $w$ 次数的分子项只读更低整系数。
这些是原非中央首坏行，不替代指定中央系数。

## 7. 前 p−1 个 Newton 余项和完整高尾

继续同一原 Newton 记号
\[
\gamma_m=pmc'\in\mathcal O^\times,\qquad
g_{m,h}=[w^{hs}]\mathscr G_m=[w^{hs-1}]G_m,
\]
\[
j_m=\sum_{h\ge1}(-1)^{h-1}(h-1)!
 \left(\frac p{\gamma_m}\right)^h g_{m,h}.
\tag{20}
\]
R606 保证整 Gaussian 改变不改变这个完整 $j_m$。

由 (18)，得到准确的三个区间
\[
\boxed{
\begin{array}{ll}
g_{m,h}\in\mathcal O,&1\le h\le p-1,\\
v_p(g_{m,p})\ge-1,&h=p,\\
v_p(g_{m,h})\ge-2,&p+1\le h\le2p-2.
\end{array}}
\tag{21}
\]
边界均按真实指标读取：
$(p-1)s-1=L-1$、$ps-1<ps$、
$(2p-2)s-1=2L-1$。

令 (20) 的第 $h$ 项为 $T_{m,h}$。
在中间区间，
\[
v_p(T_{m,p})\ge p-1,\qquad
v_p(T_{m,h})\ge h-1\ge p
\quad(p+1\le h\le2p-2),
\tag{22}
\]
因为后一区间 $v_p((h-1)!)=1$。

尚须控制整个无限尾。R602 的全 Hurwitz 估计仍有效，给
\[
v_p(T_{m,h})\ge
\left\lceil\frac{h(5p-7)+6}{6(p-1)}\right\rceil
+v_p((h-1)!).
\tag{23}
\]
右侧随 $h$ 不减；在 $h=2p-1$ 已至少为 $p$。
例如未取上整前减去 $p$ 的分子为
$4p^2-13p+13>0$。
所以所有 $h\ge2p-1$ 也在 $p^p\mathcal O$ 中。
(21)–(23) 支付了全部高项，不留下未估尾。

设
\[
L_{m,H}=\sum_{h=1}^H T_{m,h}.
\]
则完整结论是
\[
\boxed{
v_p(j_m-L_{m,H})\ge H+1\quad(1\le H\le p-2),
\qquad
v_p(j_m-L_{m,p-1})\ge p-1 .
}
\tag{24}
\]
因此对每个 $H\le p-2$，若
$v_p(L_{m,H})\le H$，就已严格证明同一个完整 $j_m\ne0$。

在下一精度，不能把 (24) 直接外推一阶。
由 (22)–(23)，正确的整个模 $p^p$ 式为
\[
\boxed{
j_m\equiv L_{m,p-1}
 +(p-1)!\left(\frac p{\gamma_m}\right)^p g_{m,p}
 \pmod{p^p}.
}
\tag{25}
\]
这里 $p$ 为奇数，所以第 $p$ 项的符号为正。
$pg_{m,p}$ 整；它的实际值由原来源决定，
不能在首层或完整中央失败时未经比较直接删除。

R602 的全有限二项式返回式同时保留：
\[
L_{m,H}
=\sum_{k=1}^H(-1)^{k-1}(k-1)!\binom Hk
 \left(\frac p{\gamma_m}\right)^k [w^{ks}]A_m .
\tag{26}
\]
于是 (24) 是原系数的完整有限证书，
没有换新的 tame 角或辅助中央。

## 8. 范围与后继

本篇没有把 $h=p$ 的除商认作新的独立零条件，
也没有把 (19) 的非中央单位代成原 $j_m$ 非零。
R616 可继续从同一个高度二参数提取整个首坏带，
再准确比较 (25) 的 $h=p$ 端点与原首中央系数。

(9) 是已付的有限整性和分母范围；R602 的全局开盘与无限 Hurwitz
估计继续保持。这里不由有限窗口宣称一个新的最大收敛半径，
也未证明原中央失败传播到全部次数和全部非空真前缀。

证明使用原全部 addition、所有二项式例外和真实参数分母；
无新增素数扫描。已存在的 $p=23$ 纤维只用于最初定位窗口，
一般结论完全由 §§2–7 的全参数证明给出。

## 依赖

- [R602](R602-original-gaussian-hurwitz-integrality-and-next-central-bockstein.md)：原高度二系数界、Hurwitz 整性、原完整分子和无限 Newton 尾。
- [R606](R606-original-gaussian-unit-gauge-and-canonical-second-central-row.md)：整 Gaussian 改变的完整导数不变性。
- [R615](R615-original-weierstrass-zeta-cartier-and-p-multiple-congruence.md)：原 $H$ 的二项式进位及 $\delta C_s=3$；第 5 节明确补足其窗口之后的首边界。
- [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)：同一个原 $S/T$ 分子和物理缩放。

原固定曲线、无穷素数及完整 $\Sha[p^\infty]$ 的主目标仍未完成。
