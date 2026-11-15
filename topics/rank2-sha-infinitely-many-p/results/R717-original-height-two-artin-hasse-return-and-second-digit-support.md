# R717 — 原高度二 sigma 的完整 Artin–Hasse 返回与第二位输入支持

日期：2026-11-15。**状态：以下原有限来源、精确输入精度、共同 Frobenius 分解及完整 Cartier 返回已证明。**

R714 已把整个原高度二整参数窗放回一个指定有理参数。
本篇进一步恢复该窗中的原 sigma 来源本身。
全部模 $p$ 系数只需要原 Weierstrass 系数的第一位，以及两组
各 $s-1$ 个指定指标的第二位。
这两组数据属于原曲线的实际系数，不是可以任意调整的 Frobenius 参数。

构造同时适用于原 $m=34,72$，以及另保原门的第三来源 $m=136$。
全局有理极帽会增大；没有把这个有限来源返回当成旧预算中的免费列，
也没有从原中央零推出逐行零。

## 1. 原整窗及对数系数

保持
$$
p=6s-1>101,\qquad q=p^2,\qquad
L=(q-1)/6=s(p-1),\qquad w=z^6,\qquad b=17.
$$
用同一个原规范
$$
X(w)=z^2x(z)=1+\sum_{n\ge1}X_nw^n,\qquad
F(w)=\log(\sigma/z),
$$
$$
c=F_s,\qquad
U(w)=(\sigma/z)e^{-cw^s},\qquad
f(w)=\log U=\sum_{n\ge1}f_nw^n.
$$
第三来源 $m=136$ 另保 $p>136$；其算术中央假设仍独立。
R614 的完整 addition 证明给
$$
X_n,u_n\in\mathcal O\quad(0\le n<L),
$$
而原微分恒等式准确给
$$
\boxed{
f_s=0,\qquad
f_n=-\frac{X_n}{6n(6n-1)}\quad(n\ne s).
}
\tag{1}
$$
这里 $f_s=0$ 是同一个原 $c=F_s$ 的准确消去，不只模 $p$。

在 $n<L<p^2$ 范围内，$n$ 与 $6n-1$ 不可能同时被 $p$ 整除，
各自也不可能含 $p^2$。因此 (1) 的显示分母至多有一个 $p$。
不过 $f_n$ 本身不全整；不能直接在特征 $p$ 使用无限通常指数。

## 2. 使用真正的整 Artin–Hasse 指数

定义
$$
E_p(T)=\exp\left(T+\frac{T^p}{p}
                    +\frac{T^{p^2}}{p^2}+\cdots\right).
\tag{2}
$$
本篇需要其全部有限系数的整性，先给完整证明。

设 $\mu(r)$ 为 Möbius 函数。形式对数逐项给
$$
\boxed{
E_p(T)=
\prod_{\substack{r\ge1\\p\nmid r}}
 (1-T^r)^{-\mu(r)/r}.
}
\tag{3}
$$
因为 $T^n$ 的对数系数为
$$
\frac1n\sum_{\substack{r\mid n\\p\nmid r}}\mu(r),
$$
它只有在 $n$ 为 $p$ 幂时等于 $1/n$，其余为零。
每个指数 $-\mu(r)/r$ 属于 $\mathbf Z_p$；
其二项式系数由整数指数的 $p$ 进连续逼近知均在 $\mathbf Z_p$。
对每个次数只用有限个乘积因子，所以
$$
\boxed{E_p(T)\in1+T\mathbf Z_p[[T]].}
\tag{4}
$$
因而约化 $\overline E_p(T)$ 有确切意义。
(4) 不允许把 (2) 中某个不整分项独立约化。

## 3. 原整单位的唯一有限 p-典型因子

对全部 $1\le n<L$ 定义实际系数 $a_n$：
$$
\boxed{
a_n=f_n\quad(p\nmid n),\qquad
a_{pk}=f_{pk}-\frac{f_k^p}{p}
\quad(1\le k\le s-1).
}
\tag{5}
$$
$pk<L$ 的全部正 $k$ 正好是 $1,\ldots,s-1$；
特别这些 $k<p$、$k<s$，没有再次出现 $p$ 倍或 Gaussian 例外。

取对数，并用 $L<p^2$，可准确比较每个次数：
$$
\boxed{
U(w)=\prod_{1\le n<L}E_p(a_nw^n)
             \pmod{w^L}.
}
\tag{6}
$$
对 $p\nmid n$，右侧对数在次数 $n$ 只有 $a_n$；
对 $n=pk$，只有 $a_{pk}+a_k^p/p$，正是 (5)。
不存在第三个 $p$ 幂层。

全部 $a_n$ 都整。这可以直接归纳而不假设 (5) 的商自动整：
假定 $a_j\in\mathcal O$ 对 $j<n$ 已知。
用 (4) 除去 (6) 的全部低因子，所得仍为整单位，
其第一个尚未消去的 $w^n$ 系数准确是 $a_n$。
所以 $a_n\in\mathcal O$，完成整个有限归纳。

因此
$$
\boxed{
a_n\in\mathcal O\quad(1\le n<L),
}
\tag{7}
$$
且所有约化只依赖这些实际 $a_n\bmod p$。
这不是选择一个新的整 lift，而是原 $U$ 的唯一因子系数。

## 4. 第二个 p 进位仅出现在两组指定指标

由 (1)、(5) 分三种情形。

### 4.1 单位分母与准确 Gaussian 例外

若 $p\nmid n(6n-1)$，则
$$
\bar a_n=-\bar X_n/(6n(6n-1)).
\tag{8}
$$
只用 $\bar X_n$。原 $n=s$ 处则准确有 $a_s=0$，
不需要为已消去的 $c$ 再指定一个第二位。

### 4.2 真正的 p 倍指标

对 $n=pk$、$1\le k\le s-1$，
$$
\boxed{
\bar a_{pk}
=\overline{
\frac1p\left\{
-\frac{X_{pk}}{6k(6pk-1)}-f_k^p
\right\}}.
}
\tag{9}
$$
大括号确被 $p$ 整除，这是 (7) 的原整性。
它也与 R615 的
$X_{pk}\equiv-X_k^p/(6k-1)\bmod p$ 逐项相容。

为读取 (9)，需要实际 $X_{pk}\bmod p^2$，
但 $f_k^p\bmod p^2$ 只需 $\bar f_k$。
事实上任何两个整 lift 相差 $pt$，二项式展开给
$$
(a+pt)^p\equiv a^p\pmod{p^2}.
$$
因此此处没有隐藏另一个低系数的第二位要求。
分母 $6k(6pk-1)$ 在模 $p^2$ 中按它的原值取逆，不能先降模 $p$ 后除 $p$。

### 4.3 真正的 zeta 共振指标

剩下 $p\mid6n-1$ 的全部 $n<L$ 为
$$
n=s+pk,\qquad 0\le k\le s-1.
$$
$k=0$ 已由 $a_s=0$ 支付。
对 $1\le k\le s-1$，准确有
$$
6n-1=p(1+6k),
$$
所以
$$
\boxed{
\bar a_{s+pk}
=-\frac{\overline{X_{s+pk}/p}}
        {\overline{6(s+pk)(1+6k)}}.
}
\tag{10}
$$
分母是单位，且 $X_{s+pk}\in p\mathcal O$：
后者由 $p\nmid n$、(1)、(7) 得到。
这里的 $X_{s+pk}/p\bmod p$ 是原实际除商，不能因 $\bar X_{s+pk}=0$
就把它置零。

因此全部额外第二位输入的支持准确包含于
$$
\boxed{
\mathcal I_2=
\{pk:1\le k\le s-1\}
\ \sqcup\
\{s+pk:1\le k\le s-1\}.
}
\tag{11}
$$
两组不交，总数 $2s-2=(p-5)/3$。
(8)–(10) 给完整恢复算法；不要求其它 $n<L$ 的第二位。
这里证明的是一个充分且逐项指定的输入范围，
不声称每个第二位都在任何给定较短输出中必然独立出现。

R714 还直接给所有第一位的有理读取：
$$
\boxed{
\bar X_n=[Z_1^{6n}](xZ_1^2)\qquad(0\le n<L),
}
\tag{12}
$$
因为 $Z_1=z+O(z^q)$，乘回 $z^2$ 后的首参数误差在次数 $q-1$。
(12) 只到 $6n<q-1$，不越过原首坏系数。

## 5. 全首块共享的实际 Frobenius 因子

在 $k[[w]]/(w^L)$ 中定义
$$
U_{\rm np}(w)=
\prod_{\substack{1\le n<L\\p\nmid n}}
 \overline E_p(\bar a_nw^n),
$$
并在 $k[[w]]/(w^s)$ 中定义
$$
V(w)=\prod_{k=1}^{s-1}
 \overline E_p\bigl(\bar a_{pk}^{\,1/p}w^k\bigr).
\tag{13}
$$
剩余域完美，根唯一；本题有理系数的 $\mathbf F_p$ 约化下根即自身。
由于 $\overline E_p$ 的系数在 $\mathbf F_p$，(6) 给
$$
\boxed{
\bar U(w)=U_{\rm np}(w)V(w)^p\pmod{w^L}.
}
\tag{14}
$$
$V\bmod w^s$ 已足够，因为 $ps>L$。
$U_{\rm np}$ 仍保 (10) 的原共振除商；
不能把它称作只需要第一位的模型。

令原三来源的完整有限多项式为 R647 的 $P_m$，并写
$$
\mathcal P_m(w)
=\sum_j(P_m)_j b^j w^j
                 X(w)^{(m-6)/2-3j}.
\tag{15}
$$
对 $m=34,72,136$，所有显示的 $X$ 幂均非负；
固定分母仍按原好素数门取单位。
原规范化来源准确为
$$
A_m^\circ=wU(w)^m\mathcal P_m(w).
$$
记
$$
B_{m,n}=[w^n]\{U_{\rm np}^m\overline{\mathcal P_m}\},
\qquad
v_{m,j}=[w^j]V^m.
$$
对全部 $1\le h\le p-1$，得到完整有限卷积
$$
\boxed{
\bar g_{m,h}
=\sum_{j=0}^{\lfloor(hs-1)/p\rfloor}
 v_{m,j}^{\,p}\,B_{m,hs-1-pj}.
}
\tag{16}
$$
这里 $g_{m,h}=[w^{hs}]A_m^\circ$。
所有右侧次数均小于 $L$，且 $j\le s-1$。
三个 $m$ 使用同一个 $U_{\rm np},V,X$，
没有对每个来源另选一个有利的 Frobenius 因子。

对 R708 的较短前缀 $h\le J$，
令 $N=sJ-1$。只需 (11) 中 $n\le N$ 的指标：
第一组有 $\lfloor N/p\rfloor$ 个，
第二组有 $\max(0,\lfloor(N-s)/p\rfloor)$ 个。
这只是原实际数据的截断，并不增加新的算术零。

## 6. 原 sigma 的完整有限有理模型

令 $U_{\rm AH}(w)$ 为 (6) 约化后在次数 $<L$ 的唯一多项式代表。
定义同一原曲线上的有理函数
$$
\boxed{
\Sigma_{\rm AH}=Z_1\,U_{\rm AH}(Z_1^6).
}
\tag{17}
$$
这一次已输入 (9)、(10) 的全部实际除商。
由 (6)、R714，准确有
$$
\Sigma_{\rm AH}=\sigma^\circ+O(z^q)
$$
于原已付整局部窗口，进而
$$
\boxed{
\Sigma_{\rm AH}^m\phi_m
=A_m^\circ+O(z^{q+5}).
}
\tag{18}
$$
后一式使用 $\phi_m$ 的原极阶恰为 $m-6$。
所读取的 $h(p+1)\le q-1$ 全部安全地在 (18) 内。

极点成本不能略去。
因为 $\deg U_{\rm AH}\le L-1$，(17) 是 $Z_1$ 的次数至多 $q-6$ 的多项式。
R714 因而给
$$
(\Sigma_{\rm AH})_\infty
\le(q-6)(p^3-p^2)\mathcal D_2,
$$
$$
\boxed{
(\Sigma_{\rm AH}^m\phi_m)_\infty
\le m(q-6)(p^3-p^2)\mathcal D_2.
}
\tag{19}
$$
$O$ 处的极已由 (18) 的六阶零相消。
这是随 $p$ 增长的真正成本，通常大于 R647 低窗模型的成本。

## 7. 全部首 Cartier 行不再留未展开的模型差

置
$$
\beta_{m,h}=Z_1^{-h-1}\Sigma_{\rm AH}^m\phi_m\omega_E,
\qquad
r_{m,h}=\operatorname{Res}_O\beta_{m,h}.
$$
对 $1\le h\le p-1$，它在 $O$ 的阶至少为 $5-h>-p$。
用 R714 的同一个有限部，准确有
$$
\boxed{
\bar g_{m,h}
=\left[
\frac1{(h-1)!}D^{h-1}
 \left\{
 \frac{\mathcal C(\beta_{m,h})}{\omega_E}
 -\frac{r_{m,h}^{\,1/p}}{Z_1}
 \right\}(O)
\right]^p.
}
\tag{20}
$$
括号中的函数正则；$\omega_E=dZ_1$。
因此 Cartier 取出的恰是次数 $h(p+1)$，
再由 (18) 直接回到原 $g_{m,h}$。
所有其它 $Z_1$ 零点以及 (19) 的全局极仍须保留。

R711 的 $\eta_p$ 在本模型中没有作为一个未指定误差出现，
原因是 (9)、(10) 已实际支付原来源的相应提升数据。
这不等于证明旧 $P_2$ 的 $\eta_p$ 为零，也不许可在未读这些数据时
把 R714 的 $\Delta_{m,h}$ 删掉。

## 8. 对原非零问题的准确意义

本篇给两种等价的完整有限入口：
原固定第二位数据下的 (16)，以及同一曲线的指定有理 Cartier 行 (20)。
原首迹零的 R708 判据可在全部这些真实行上使用。

但原 $j_m=0$ 仍只给 R710 的真实进位关系；
它没有被本篇改成 $g_{m,h}\equiv0$ 的逐行条件。
两个实际除商族 (9)、(10) 也不能作为任意可调参数，
或仅按参数个数代替实际相容性证明。
下一步必须在这些原指定值、固定 $\phi_m$ 和完整算术进位之间
证明新的关系，才会得到目标中央非零。

原固定曲线、无穷不同素数、全 $\Sha[p^\infty]$ 有限三个要求不变；
主目标尚未完成。

依赖：
[R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)；
[R615](R615-original-weierstrass-zeta-cartier-and-p-multiple-congruence.md)；
[R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)；
[R708](R708-original-mod-p-prefix-and-integral-gaussian-return.md)；
[R710](R710-original-all-order-central-kernel-and-exact-boundary-remainder.md)；
[R714](R714-original-height-two-rational-parameter-and-full-first-cartier-window.md)。

本篇为完整一般证明，无新增数值执行或目标素数扫描。
