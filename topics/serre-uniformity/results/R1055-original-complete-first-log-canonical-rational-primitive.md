# R1055：原完整首 log 向量的规范有理原函数

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；global_route / root，o2_high_coefficient 独立纸核。

**已证明：原完整 $\bar v=(1-Q)\lambda$ 在全部超奇异点上的值，有一个明确、唯一规范化的有理原函数。** 本篇保留原 $Q$ 的整个 quotient，并严格区别有理代表、完整 polynomial quotient 与模 $A$ 的低次代表。它给继续计算原 $Q^2$ 和最低泛函的输入，不宣称指定值非零。

## 1. 原记号和精确公式

对全部 $p=6N+5\ge41$，置
$$
\ell=2N+2=(p+1)/3,\quad r=1-b^3,\quad A(b)=bQ(b^3),
\quad A_1=A(1)=Q(1)\ne0,
$$
其中 $Q$ 是 R1045 的原单首有限多项式。本文的线性算子记作 $Q_{\rm op}$，避免与这个多项式混淆。由原反射恒等式，
$$
q(r)=\frac{Q(r)}{Q(0)}=\frac{Q(1-r)}{Q(1)},\qquad
A(b)=A_1bq(r).
\tag{1055.1}
$$
$q$ 正是 R1050 所用超几何级数在安全范围内的归约。令
$$
j(r)={}_2F_1(1/2,1/2;2/3;r)\pmod{r^\ell},
\qquad J(r)=j(r)/q(r)\pmod{r^\ell}.
$$
所有 $j$ 系数仅使用 $0\le i<\ell$，不跨第一个共振分母。定义两个次数小于 $\ell$ 的多项式
$$
U_1(r)=\big[(1-r)^{-1/3}J(r)\big]_{<\ell},\qquad
U_2(r)=\big[(1-r)^{-2/3}J(r)\big]_{<\ell}.
\tag{1055.2}
$$
结论为
$$
\boxed{\quad
\mathcal V(b)=\frac{6}{A_1^2r^\ell}
 \bigl(bU_1(r)+b^2U_2(r)\bigr),
\qquad \mathcal V'(b)=v_{\rm can}(b).
\quad}
\tag{1055.3}
$$
$v_{\rm can}$ 是下面精确定义的原 $\bar v$ 的有理代表；它在 $A=0$ 全部正则。$\mathcal V$ 只在三个 $r=0$ 点有至多 $\ell<p$ 阶极，且 $\mathcal V(\infty)=0$。这些极阶及无穷归一化使它唯一。

## 2. 原算子的有理代表与完整商

置 $f=r^{4N+2}=r^{2\ell-2}$。对在 $A=0$ 正则的 $\mathbf F_p$ 有理函数 $a$，令 $a^\flat$ 为其唯一次数小于 $\deg A$ 的代表。写
$$
a-a^\flat=Ah,\qquad h\text{ 在 }A=0\text{ 正则}.
$$
所有外部系数保持固定，所以
$$
\frac{f\,a(b^p)}{A^2}
-\frac{f\,a^\flat(b^p)}{A^2}
=fA^{p-2}h(b^p).
\tag{1055.4}
$$
右侧在 $A$ 的每一个简单根至少有 $p-2$ 阶零。两项具有完全相同的全部超奇异 principal parts。

令 $\operatorname{PP}_S$ 表示在全部 $A$ 根的完整 principal parts 之和，并定义
$$
R_a(b)=\frac{f\,a(b^p)}{A^2}
-\operatorname{PP}_S\frac{f\,a(b^p)}{A^2}.
\tag{1055.5}
$$
对 polynomial 代表 $a^\flat$ 作完整除法：
$$
\frac{f\,a^\flat(b^p)}{A^2}
=P_{a^\flat}(b)+\frac{\operatorname{rem}(f\,a^\flat(b^p),A^2)}{A^2}.
$$
最后一项为真分式，正好等于其全部有限 principal parts。因此
$$
\boxed{\quad
R_a-P_{a^\flat}=fA^{p-2}h(b^p),\qquad
R_a|_S=Q_{\rm op}a.
\quad}
\tag{1055.6}
$$
这里 $P_{a^\flat}$ 是**完整 quotient**。若再将它模 $A$ 取低次代表，所得多项式只在 $S$ 上相等，不能把 (1055.6) 继续当作两个全局有理函数的恒等式。这一差别在后继 $Q^2$ 和 $b=0$ 的 pole 比较中必须保留。

## 3. 原 $\lambda$ 的全部 CM 极部

始终使用 R1045 的
$$
\lambda=-\frac{6(b+1)}r
=\frac4{b-1}-\frac2{b-\zeta}-\frac2{b-\zeta^2}.
\tag{1055.7}
$$
其原 Frobenius 源为
$$
\mathfrak F_\lambda=\frac{f\,\lambda(b^p)}{A^2}
=-\frac{6(b^p+1)}{r^{\ell+1}A^2}.
\tag{1055.8}
$$
原 $\mathcal LA=0$ 给 $f'/f=A''/A'$ 于每一个 $A$ 根，而 $\lambda(b^p)'=0$，故这些点的简单极部全为零。于是
$$
R_\lambda=\mathfrak F_\lambda-\operatorname{PP}_S\mathfrak F_\lambda
$$
只在三个 CM 点有极，且在无穷为 $O(b^{-2})$；因为 $\mathfrak F_\lambda=O(b^{-p-1})$，所有被扣除的 $S$ 极部都是双极。由 (1055.6)，这是原 $Q_{\rm op}\lambda$ 的规范有理代表，符号为 R1045 的 $R_\lambda=-R$。因此
$$
v_{\rm can}=\lambda-R_\lambda
\tag{1055.9}
$$
准确代表原 $(1-Q_{\rm op})\lambda$。

在任意 $a^3=1$ 的 CM 点，使用实际局部参数
$$
b=a(1-r)^{1/3},\qquad db=-dr/(3b^2).
$$
因为 $b^p=a^p+O(r^p)=a^2+O(r^p)$，且 $\ell+1<p$，其 $O(r^p)$ 不贡献任何极部。由 (1055.1)、(1055.8)，
$$
\operatorname{PP}_{a}(\mathfrak F_\lambda\,db)
=\frac{2(a+a^2)}{A_1^2}
 \operatorname{PP}_{r=0}\left(r^{-\ell-1}W(r)\,dr\right),
\qquad
W(r)=(1-r)^{-4/3}q(r)^{-2}.
\tag{1055.10}
$$
R1045 §4 的完整留数恒等式 $S_0=1$，经 $Q(1-r)^2=Q(r)^2$ 和 $\ell$ 偶，准确给
$$
[r^\ell]W(r)=A_1^2.
\tag{1055.11}
$$
所以 $R_\lambda\,db$ 在三个点的留数依次为 $4,-2,-2$，与原 $\lambda\,db$ 完全相同。$v_{\rm can}\,db$ 的三个简单极部均为零。这一步保留整个高极部，未只比较首项。

## 4. 安全 Wronskian 与原函数的全部 principal parts

同一个原 Picard–Fuchs Wronskian（R1050、R1052）在所需安全范围给
$$
J-3rJ'=W\pmod{r^\ell}.
\tag{1055.12}
$$
也可从
$$
\left(r^{1/3}\frac qj\right)'
=\frac13r^{-2/3}(1-r)^{-4/3}j^{-2}
$$
直接消去 $J=j/q$ 得到。只比较 $i<\ell$，各 $1-3i$ 均为单位；没有把 $J$ 当成跨共振的无限特征 $p$ period。

因 $\ell\equiv1/3\bmod p$，(1055.12) 逐项等价于
$$
d\operatorname{PP}\bigl(r^{-\ell}J\bigr)
=-\frac13\operatorname{PP}_{\ne-1}
 \bigl(r^{-\ell-1}W\,dr\bigr),
\tag{1055.13}
$$
下标表示排除已在 (1055.11) 单独支付的简单极部。

由 (1055.2)，在 $b=a(1-r)^{1/3}$ 处
$$
bU_1+b^2U_2=(a+a^2)J\pmod{r^\ell}.
$$
所以 (1055.3) 的全部 principal part 正好是
$$
\operatorname{PP}_a\mathcal V
=\frac{6(a+a^2)}{A_1^2}
 \operatorname{PP}\bigl(r^{-\ell}J\bigr).
\tag{1055.14}
$$
结合 (1055.10)–(1055.13)，其微分等于
$v_{\rm can}\,db$ 在三个 CM 点的全部 principal parts，简单极部也同为零。

## 5. 全局相等、无穷归一化与唯一性

$\mathcal V$ 的分子次数至多 $3\ell-1=p$，分母次数为 $3\ell=p+1$，故 $\mathcal V=O(b^{-1})$、$\mathcal V'db$ 在无穷正则。$v_{\rm can}=O(b^{-2})$，其微分也在那里正则。

$\mathcal V'db-v_{\rm can}db$ 在三个 CM 点的完整 principal parts 已消；在所有其它有限点也正则。它是 $\mathbf P^1$ 上的全局正则微分，因而为零。这证明全有理式 (1055.3)，并非仅在 $A=0$ 的一次插值相等。

若另有同样极阶限制、无穷值零的原函数，其差导数为零，因而属于 $k(b^p)$。一个非恒定 $p$ 次有理函数的每个极阶均为 $p$ 的倍数，而允许的全部有限极阶至多 $\ell<p$，无穷也无极；故差为常数，再由无穷归一化等于零。这里显式排除了特征 $p$ 的 $p$ 次有理函数歧义，没有误用“同导数只差常数”。

## 来源及使用范围

- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md)：系数固定的原算子、原 $\lambda$ 与完整 MW 消去向量。
- [R1045](R1045-original-MW-annihilator-nonzero-reduction.md) §§1、4：原 $A$、反射、$\mathcal LA=0$、完整 $\lambda+R$ 和 $S_0=1$。
- [R1050](R1050-actual-CM-parameter-short-PD-and-Picard-Fuchs.md) §§4–5 及 [R1052](R1052-original-complete-CM-profile-and-actual-lowest-functional.md) §8：同一 $q,j$、安全阶数与 Wronskian。

本篇为纸面证明，没有执行数学计算，没有重跑窗口。global_route 给原构造，root 逐项核对完整商、有理差、三 CM 符号、全部极部和无穷度数，o2_high_coefficient 独立核原函数。后续仍需在完整原 $Q^2$ 中求实际指定泛函；本篇不把任一新原函数值、核范数或参考列值冒作其单位结论。
