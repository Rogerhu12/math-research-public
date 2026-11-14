# R619 — 原 Cartier 稀疏行、唯一二阶极部与完整第二 Newton 块

日期：2026-11-14。**状态：已证明。**

本篇在原整坐标中付清 $X_{s+ap}$ 的全部稀疏行，再把 R616 的首坏带扩展到整个 $n<2L$ 窗口。原 log sigma 在此窗口只有一条二阶极部，位置准确为 $ps$。完整指数与原 theta 多项式的二阶极部因此返回同一来源的低段；原 S/T 的首项因子 $w$ 保留后，中央块的合法末端是 $p+h$、$h=p-2$。

## 1. 原参数窗口与 Cartier 常数

保持
$$
p=6s-1>71,\qquad L=\frac{p^2-1}{6}=s(p-1),\qquad
b=17,\quad w=z^6,
$$
$$
A(w)=z^2x(z)=\sum X_nw^n,\quad
Y(w)=-z^3y(z),\quad
F(w)=\log(\sigma(z)/z).
\tag{1}
$$
原 $u=x^{-1/2}$ 参数满足
$$
t=bu^6,\quad z=uH(t),\quad
\omega_E=C(t)du,\quad
C(t)=(1+t)^{-1/2},\quad H_n=\frac{C_n}{6n+1}.
\tag{2}
$$
R587 的整个原微分空间已付
$$
\boxed{
\mathcal C(\omega_E)=0,\qquad
\mathcal C(x\omega_E)=c_p\omega_E,\qquad
c_p=\binom{3s-1}{2s-1}b^s\in\mathbf F_p^\times.
}
\tag{3}
$$
这里 $\mathcal C$ 是真正的 Cartier 算子；下文用的是原 $b=17$ 尺度。

## 2. 全部稀疏行 X_(s+ap)

取实际整坐标
$$
z_0(u)=\sum_{n<L} b^nH_nu^{6n+1}.
\tag{4}
$$
R615 的二项式进位证明给 $H_n$ 对全部 $n<L$ 整。该证明到 $L-1$ 仍只有同一数位条件；$L$ 才首次有 $6L+1=p^2$。因此 (4) 模 $p$ 是原点的真正局部参数，且
$$
dz_0=\omega_E+O(u^{p^2-1})du.
\tag{5}
$$
由于 $x$ 有二阶极，
$$
x\omega_E-x\,dz_0=O(z_0^{p^2-3})dz_0.
$$
对其施 Cartier 后，误差从 $z_0^{p-1}dz_0$ 才开始：满足 Cartier 指数条件的第一个可能指数是 $p^2-1$。

在 $n<L$ 时，原 $x(z)$ 与 $x(z_0)$ 的所取系数相同；第一次参数差从 $u^{p^2}$ 才出现。原指数
$$
6(s+ap)-2=(6a+1)p-1
$$
经 Cartier 变成 $6a$。若 $s+ap<L$，则 $0\le a\le s-1$，所以
$6a\le p-5<p-1$，完全位于已控制误差之前。将 (3) 在坐标 $z_0$ 中比较，得到

**定理 1。**
$$
\boxed{
X_s=c_p,\qquad
X_{s+ap}=0\quad
(1\le a,\ s+ap<L)
\quad\text{于 }\mathbf F_p.
}
\tag{6}
$$
这不是把形式 sigma 当成有理函数；整个证明只使用原有理微分和一个确已整的局部坐标。

## 3. H 的单一极部扩展到 n 小于 2L

在 $0\le n<2L$ 写 $n=pa+r$。此时 $a\le2s-1$，仍有 $2a+1<p$，所以 R615 的单次二项式进位公式保持。若 $6n+1$ 含 $p$，则 $r=p-s$；其中只有 $a=s-1$ 使分母再多一个 $p$。故整个 $n<2L$ 窗口仍只有
$$
\boxed{H_L\text{ 不整},\qquad pH_L=-1\quad\text{于 }k.}
\tag{7}
$$
没有第二个 $p^2$ 分母混入这个窗口。

于是可在同一截断内写
$$
H=H_{\rm int}+H_Lt^L,\qquad H_{\rm int}\in\mathcal O[t]/(t^{2L}).
$$
R616 的原留数变分原样适用于全部 $0\le r<L$：二次 $H_L$ 项从 $2L$ 才出现，而低 $r<L<p^2$ 中的 $H_{\rm int}^{-p^2}$ 为一。因此
$$
\boxed{
pX_{L+r}=b^L(6r-2)X_r,\qquad
pY_{L+r}=b^L(6r-3)Y_r
\quad(0\le r<L)
}
\tag{8}
$$
在模 $p$ 意义下完整成立。特别 $A,Y$ 的全部 $n<2L$ 系数估值至少为 $-1$。

## 4. 原 log sigma 只有一个二阶极部

令
$$
c=[w^s]F,\qquad c'-c\in\mathcal O,\qquad
F^\circ=F-c'w^s,\qquad U=e^{F^\circ}.
\tag{9}
$$
对于 $n>0$，
$$
F_n=-\frac{X_n}{6n(6n-1)}.
\tag{10}
$$
R614 的 $n<L$ 指数整性说明这些低 log 系数至多有一次分母；也可直接由其整对数导数读取。现在令 $n=L+r$、$0\le r<L$。

在这个窗口，(10) 的分母至多再含一次 $p$，而只有两类位置：

- 若 $p\mid n$，则 $r=s+ap$。式 (8) 与 (6) 说明，只有 $a=0$ 可能给二阶极部；
- 若 $p\mid6n-1$，则 $r\equiv2s\pmod p$。式 (8) 的因子 $6r-2$ 已为零，所以原 $X_n$ 在该行整；这里没有二阶极部。

唯一留下的位置是
$$
n=L+s=ps.
$$
原 $pc=-X_s/(p+1)$，故由 (8)、(10) 得

**定理 2。**
$$
\boxed{
p^2 F^\circ_n\equiv
\begin{cases}
b^Lpc,&n=ps,\\
0,&0\le n<2L,\ n\ne ps
\end{cases}
\pmod p.
}
\tag{11}
$$
右端 $pc$ 是原 Gaussian 单位，不是自由常数。$c'$ 的整重标不改变 (11)。

## 5. 整个指数及固定原 theta 来源的第二极部块

取 $U_{\rm int}=[U]_{<L}\in1+w\mathcal O[w]$，并令
$$
\Delta=F^\circ-\log U_{\rm int}.
$$
它从 $L$ 开始。在 $n<2L<p^2$ 时，
$\log U_{\rm int}$ 的系数估值至少为 $-v_p(n)\ge-1$，所以其二阶极部为零。式 (11) 因此仍是 $\Delta$ 的二阶极部。

又 $\Delta^2$ 从 $2L$ 开始，故同一窗口中
$$
U=U_{\rm int}(1+\Delta).
$$
得到完整的第二块
$$
\boxed{
p^2 U_{ps+r}=b^Lpc\,U_r
\quad(0\le r<2L-ps),
}
\tag{12}
$$
且 $n<ps$ 的 $p^2U_n$ 为零。右端读取的是 $r<L$ 的原整系数。

对于 R616 的固定原 theta 来源
$$
B_{\mathcal F}(w)=z^{-d}e^{-mc'w^s}\mathcal F(z),
\qquad
\mathcal F=\sigma^mP(x,y),
$$
先将 $y$ 次数约至至多一，并保原各项 $w^jA^\alpha Y^\beta U^m$ 的 $j\ge0$。在 $n<2L$ 内两个坏因子仍不能同时出现，$A,Y$ 又只有一阶极部。因此其全部二阶极部只来自同一个 $U^m$，准确为
$$
\boxed{
p^2[w^{ps+r}]B_{\mathcal F}
\equiv mpc\,b^L[w^r]B_{\mathcal F}\pmod p,
\quad0\le r<2L-ps.
}
\tag{13}
$$
这一块由真正的 sigma 次数 $m$ 控制；R616 的一阶首坏带则由原点阶数 $d$ 控制。两个数不能互换。

## 6. 原 S/T 的完整第二中央块

取原 $c'=c$，对 $X=S,T$ 保
$$
m=34,72,\quad
G_m(w)=e^{-mcw^s}X(z)=wB_X(w),
$$
$$
g_{m,h}=[w^{hs}]G_m,\qquad
\gamma_m=mpc.
\tag{14}
$$
原 $w$ 因子必须保留。若 $1\le h\le p-2$，则
$$
(p+h)s-1=ps+(hs-1)<2L.
$$
所以 (13) 准确给出整个块
$$
\boxed{
p^2g_{m,p+h}\equiv
\gamma_m b^L g_{m,h}\pmod p,
\qquad1\le h\le p-2.
}
\tag{15}
$$
末端 $h=p-2$ 合法，因为归一系数的实际指标是 $2L-1$，并未越过窗口。

$h=0$ 的一阶项不能由 (15) 补造；R616 已另行支付
$$
\boxed{p g_{m,p}\equiv b^L g_{m,1}\pmod p.}
\tag{16}
$$
因此第一带、唯一二阶极部和完整第二中央块是在同一个原来源中接合的。

## 7. 全 Newton 和式的准确下一位

记原完整 Newton 项
$$
T_{m,h}=
\frac{(-1)^{h-1}(h-1)!\,p^h}{\gamma_m^h}g_{m,h},
\qquad j_m=\sum_{h\ge1}T_{m,h}.
\tag{17}
$$
式 (15) 及
$$
\frac{(p+h-1)!}{p}\equiv-(h-1)!\pmod p
$$
给逐项的真实 leading 比较
$$
\boxed{
T_{m,p+h}\equiv
p^{p-1}b^L\gamma_m^{\,1-p}\,T_{m,h}
\pmod{p^{p+h}},
\quad1\le h\le p-2.
}
\tag{18}
$$
这是各项的一位同余，不是把整个高块无精度损失地换成低块。

特别，所有 $h\ge p+2$ 的原完整尾都在 $p^{p+1}\mathcal O$ 中。对
$p+2\le h\le2p-2$，由 (13) 的 $v_p(g_{m,h})\ge-2$ 和阶乘中的一个 $p$ 直接得到。对 $h\ge2p-1$，R602 的全 Hurwitz 界给
$$
v_p(T_{m,h})\ge h-v_p((hs-1)!)
\ge h-\frac{hs-1}{p-1}>p+1,
$$
在当前 $p>71$ 范围成立。因而原完整和式满足
$$
\boxed{
j_m\equiv
\sum_{h=1}^{p}T_{m,h}
+\frac{p^p b^L}{\gamma_m^p}\,
 \overline{g_{m,1}}
\pmod{p^{p+1}}.
}
\tag{19}
$$
这里第 $p$ 项保其完整原值；R616 仅付其首 residue，不能在更高精度将它截成一个模 $p$ 常数。

若原 $j_m=0$，则首层 $\overline{g_{m,1}}=0$。此时 (16) 使 $g_{m,p}$ 整，(15) 的 $h=1$ 使 $g_{m,p+1}$ 的估值至少为 $-1$，并且得到同源精度改进
$$
\boxed{\sum_{h=1}^{p}T_{m,h}\equiv0\pmod{p^{p+1}}.}
\tag{20}
$$
这保全部原低项和未付的高精度第 $p$ 项，没有由块自相似构造新的中央零或非零。

## 8. 独立证书与边界

[check-r619-second-pole-block-and-newton-return.mjs](../scripts/check-r619-second-pole-block-and-newton-return.mjs) 及[完整输出](../scripts/check-r619-second-pole-block-and-newton-return.json) 在既有 $(p,b)=(17,1),(23,1),(23,17)$ 三个纤维上通过 **8363 项**精确检查。这些小素数只核本篇显示恒等式，不代替正文 $p>71$ 的完整尾界；$p=17$ 的 $m=34$ 为零 charge，证书保其多项式同余但不对零 $\gamma$ 作 Newton 除法。

证书：

- 用原 Weierstrass 递推及逐步显示的 $p$ 精度算到完整 $2L-1$，没有用待核的带同余填系数；
- 以足精度 Hurwitz 递推构造原 Gaussian 后 sigma、$f_4,f_1$ 及原 S/T 全多项式；
- 核全部稀疏 $X$ 行、唯一二阶 log 极部、完整 $p^2$ 块和 $h=p-2$ 的实际端点；
- 保普通系数的真实阶乘约去及全部原来源尺度。

一般证明由原 Cartier、参数变分和完整指数乘法给出。R587 的有理 sigma 连接曲率并未在此被置零；这里使用的是原有理微分的有限坐标比较，随后才在已付窗口运输特征零 theta 来源。

式 (15)、(18) 仍不是原真前缀的稳定算子，也不是对全局来源添加依赖 $p$ 的自由列。原指定 forcing 与主中央的非消失仍需继续。
