# R602 — 原单 Gaussian 余项的全 Hurwitz 整性与下一完整中央 Bockstein

日期：2026-11-14。**状态：已证明。**

本篇加强 R301/R402 对同一个原 Gaussian 余项的估计。
删去唯一准确项 $cw^s$ 以后，余下对数、其指数及原规范化分子
都满足按 $w$ 次数的 Hurwitz 整性：第 $n$ 个系数乘 $n!$ 后整。
这给出所有 $n<p$ 的完整整窗口以及更大的开解析圆盘。
不是重新选择 Gaussian，也没有修改原固定曲线或积分常数。

由此，两个原完整 Newton 导数模 $p^3$ 只需前两项。
换回实际 $S/T$ 系数，得到一个保全部原来源的第二非齐次条件。
所有高阶项由新的单调尾界支付；首层失败仍不等完整失败。

## 1. 原系数、Gaussian 与高度二输入

固定
$$
p=6s-1>71,\qquad d=p+1=6s,\qquad w=z^6,
$$
在 R301/R402 同一个 $E_1:y^2=x^3+1$ frame 中写
$$
W(w)=z^2x(z)=1+\sum_{n\ge1}X_nw^n,\qquad
Y(w)=-z^3y(z)=W-3wW',
$$
$$
F(w)=\log(\sigma(z)/z)=\sum_{n\ge1}F_nw^n,\qquad
c=F_s,\qquad F^\circ=F-cw^s .
\tag{1}
$$
原系数均在 $\mathbf Q_p$；物理单位缩放可以在同一非分歧系数环
$\mathcal O$ 中实施。下面的整数赋值取 $v_p(p)=1$。

R301 §2–3 已对这个实际 $W$ 证明
$$
v_p(X_n)\ge-\frac{6n}{p^2-1},\qquad
F_n=-\frac{X_n}{6n(6n-1)},\qquad v_p(c)=-1 .
\tag{2}
$$
置
$$
L=\frac{p^2-1}{6}\in\mathbf Z.
$$
因为系数赋值为整数，(2) 给
$$
\boxed{v_p(X_n)\ge-\lfloor n/L\rfloor.}
\tag{3}
$$
这里只用 R301 已付的严格高度二圆盘及逐系数极限，
没有假定其临界边界上的形式反演仍等距。

## 2. 删去原唯一项后，对数具有全 Hurwitz 整性

**引理 1。** 对每个 $n\ge1$，
$$
\boxed{n![w^n]F^\circ\in\mathcal O,\qquad n!X_n\in\mathcal O.}
\tag{4}
$$

证明分三个准确区间。

若 $1\le n<p$，则 $n<L$，所以 $X_n$ 整。
分母 $6n$ 不被 $p$ 整除。
若 $p\mid6n-1$，写 $6n-1=ap$；因 $p\equiv-1\pmod6$，
$a\equiv1\pmod6$，而此区间 $0<a<6$，故 $a=1$、$n=s$。
这正是已经删去的唯一项。
所以 $F^\circ$ 的全部 $n<p$ 系数整。

若 $p\le n<L$，仍有 $X_n$ 整。
且 $6n<p^2-1$，所以 $6n$ 与 $6n-1$ 各自不可能有两次 $p$ 因子；
它们相邻，至多一个有一次。
因此
$$
v_p(F_n)\ge-1,\qquad v_p(n!)\ge1.
\tag{5}
$$

最后设 $n\ge L$。
记
$$
e_n=v_p(6n(6n-1)).
$$
因两因子相邻，
$$
e_n\le\log_p(6n).
$$
由 (2)–(3)，足以证明
$$
v_p(n!)\ge\lfloor n/L\rfloor+e_n.
\tag{6}
$$
实际有一个严格余量。令
$$
A=\frac1p-\frac6{p^2-1}>0,\qquad
f(n)=An-1-\log_p(6n).
$$
在左端点，
$$
f(L)=\frac{p^2-1}{6p}-2-\log_p(p^2-1)
>\frac{p^2-1}{6p}-4>0.
\tag{7}
$$
而 $AL=(p^2-1)/(6p)-1>1/\log p$，故
$$
f'(n)=A-\frac1{n\log p}>0\qquad(n\ge L).
$$
于是
$$
v_p(n!)\ge\lfloor n/p\rfloor
\ge n/p-1
>n/L+\log_p(6n)
\ge\lfloor n/L\rfloor+e_n .
\tag{8}
$$
得到 (6)，从而 $n!F_n$ 整。
已删去的 $n=s$ 系数为零，自然满足结论。

对于 $X_n$，因 $L>p$，
$$
v_p(n!)\ge\lfloor n/p\rfloor\ge\lfloor n/L\rfloor,
$$
与 (3) 合并便给 (4) 的第二式。证毕。

(4) 不声称原 $F_s=c$ 整，也不改其准确单位 $pc$。
它只作用于同一原 $F^\circ$。

## 3. 整 Hurwitz 代数与全部实际原分子

定义
$$
\mathscr H_{\mathcal O}
=\left\{\sum_{n\ge0}a_nw^n:\ n!a_n\in\mathcal O\text{ 对所有 }n\right\}.
\tag{9}
$$
此处只陈述形式级数系数，不先赋予某个边界收敛性质。

若 $f,g\in\mathscr H_{\mathcal O}$，令 $b_i=i![w^i]f$、
$c_j=j![w^j]g$，则
$$
n![w^n](fg)=\sum_{i=0}^n\binom ni b_ic_{n-i}\in\mathcal O.
\tag{10}
$$
所以它是整代数；$w\partial_w$ 也保持它。
若 $f(0)$ 为单位，其逆由 (10) 的递推同样属于此代数。

还须支付指数，而非只用普通乘法。
若 $f(0)=0$，写 $b_j=j![w^j]f$，则
$$
n![w^n]e^f
=\sum_{\substack{k_1,k_2,\ldots\ge0\\\sum jk_j=n}}
\frac{n!}{\prod_j(j!)^{k_j}k_j!}\prod_j b_j^{k_j}.
\tag{11}
$$
每个显示组合系数是将 $n$ 个带标签元素分为规定大小无序块的计数，
故为整数。于是
$$
\boxed{f\in w\mathscr H_{\mathcal O}\Longrightarrow
e^f\in\mathscr H_{\mathcal O}.}
\tag{12}
$$
这一步没有把 $1/h!$ 当成任意 $p$ 单位。

由引理 1 和 (10)–(12)，
$$
W,\quad Y=W-3wW',\quad e^{mF^\circ}\in\mathscr H_{\mathcal O}
\qquad(m\in\mathbf Z).
\tag{13}
$$

现在只使用原真实分子。令
$$
A_{34}=S_1,\quad A_{72}=T_1,\qquad
\mathscr G_m=A_m e^{-mcw^s}=wG_m(w)\quad(m=34,72),
$$
$$
G_m(w)=\sum_{n\ge0}b_{m,n}w^n,\qquad G_m(0)=1 .
\tag{14}
$$
R301 (17) 的原 $S$ 准确给
$$
G_{34}=
\left(W^{14}-\frac{53}7wW^{11}
-\frac{12}7w^2W^8-\frac{80}7w^3W^5-\frac{128}7w^4W^2\right)
e^{34F^\circ}.
\tag{15}
$$
对 $T$，保持 R402 (1)、(12) 的
$$
P(X)=XQ_4(X)P_6(X)=\sum_{i=1}^{11}P_iX^i,\qquad
P_i\in\mathbf Z,\quad P_{11}=7.
$$
则完整原分子为
$$
G_{72}=\frac17\sum_{i=1}^{11}P_iw^{11-i}W^{3i}e^{72F^\circ}.
\tag{16}
$$
所有 $w$ 幂非负，当前 $p\nmid7$，因此这些正是 (13) 中的整代数运算。

R586 的两条真实 Euler forcing 规范化余项还分别为
$$
G_4=W e^{6F^\circ},\qquad G_1=WY e^{6F^\circ};
\tag{17}
$$
原参考的余项是 $W e^{2F^\circ}$。
它们也没有任何另选的 Gaussian 项。

**定理 2。** 对 (14)、(17) 及原参考的每个系数 $g_n$，
$$
\boxed{n!g_n\in\mathcal O,\qquad v_p(g_n)\ge-v_p(n!).}
\tag{18}
$$
特别
$$
\boxed{g_n\in\mathcal O\qquad(0\le n<p).}
\tag{19}
$$
全部 $b=17$ 或实际目标曲线的已付单位伸缩，按同次幂运输 (18)–(19)；
在共同好惰性素位不改变赋值。原物理尺度与 Gaussian 必须一起缩放，
正如 R303/R402，不单独改系数。

## 4. 较大的准确可用开圆盘

置
$$
\boxed{R_*=p^{-1/[6(p-1)]},\qquad
\rho=p^{-1/(2p)},\qquad R_E=p^{-1/(p^2-1)}.}
\tag{20}
$$
有 $\rho<R_*<R_E$。
对任意 $\rho\le R<R_*$，写 $R=p^{-\tau}$，
则 $6\tau>1/(p-1)$。
由 Legendre 公式
$$
v_p(n!)=\frac{n-s_p(n)}{p-1}
$$
以及 (4)，每个非零对数项满足
$$
v_p([w^n]F^\circ)+6n\tau
\ge n\left(6\tau-\frac1{p-1}\right)+\frac{s_p(n)}{p-1}.
\tag{21}
$$
它随 $n$ 趋于无穷，且统一严格大于 $1/(p-1)$。
因此 $F^\circ(z^6)$ 是该闭盘的 Tate 元，
其范数严格小于指数收敛阈值；原 $e^{mF^\circ}$ 及其逆实际解析。

同理由 (18)，全部规范化余项都满足
$$
\boxed{
G_\ell(z^6),\,G_m(z^6)\in\mathbf C_p\langle z/R\rangle,\qquad
\|G_\ell\|_R,\|G_m\|_R\le1.
}
\tag{22}
$$
故
$$
\boxed{\mathscr G_m\in\mathbf C_p\langle z/R\rangle,\qquad
\|\mathscr G_m\|_R\le R^6.}
\tag{23}
$$
单独的 $e^{mcw^s}$ 不需要在该大盘解析；(15)–(17) 给实际解析定义。

(22)–(23) 对每个严格内闭盘成立。
本篇不由 (18) 宣称闭 $R_*$ 上是 Tate 元：
当 $n=p^a$ 时，数字和界本身并不趋于无穷。
也没有证明 $R_*$ 是余项的最大可能半径。
它是一个已经支付、比旧 $\rho$ 更大的统一开解析圆盘。

## 5. 原完整 Newton 系数与严格单调尾界

继续用两个原 charge $m=34,72$，置
$$
\alpha_m=mc,\qquad\gamma_m=p\alpha_m\in\mathcal O^\times,
$$
$$
g_{m,h}=[w^{hs}]\mathscr G_m=b_{m,hs-1},\qquad
a_{m,h}=\alpha_m^{-h}g_{m,h}\quad(h\ge1).
\tag{24}
$$
这是 R303/R402/R598 的同一原 Newton 系数，没有换另一 tame 角。

(18) 给全部 $h$ 的强化估计
$$
\boxed{
v_p(a_{m,h})\ge h-v_p((hs-1)!)
\ge\left\lceil\frac{h(5p-7)+6}{6(p-1)}\right\rceil.
}
\tag{25}
$$
第一式更精确，第二式来自 $v_p(n!)\le n/(p-1)$，
用来提供随 $h$ 不减的显示尾界。
特别 $1\le h\le5$ 时 $hs-1<p$，所以
$$
g_{m,h}\in\mathcal O,\qquad v_p(a_{m,h})\ge h
\qquad(1\le h\le5).
\tag{26}
$$
在 $h=6$ 时 $hs-1=p$，(25) 仍给 $v_p(a_{m,6})\ge5$；
不能免费延长 (26)。

完整原函数和原导数为
$$
J_{m,p}(u)=\sum_{h\ge1}a_{m,h}(u)_h,\qquad
j_m=J'_{m,p}(0)=
\sum_{h\ge1}(-1)^{h-1}(h-1)!a_{m,h}.
\tag{27}
$$
(25) 同时给更大的 $u$ 开解析盘
$$
|u|_p<p^{(5p-7)/[6(p-1)]}.
$$
这只加强原解析估计，不修改完整 Selmer 比较。

令
$$
L_{m,H}=\sum_{h=1}^H(-1)^{h-1}(h-1)!a_{m,h}.
$$
则
$$
\boxed{
v_p(j_m-L_{m,H})\ge M^*_{p,H}:=
\left\lceil\frac{(H+1)(5p-7)+6}{6(p-1)}\right\rceil+v_p(H!).
}
\tag{28}
$$
因为 (25) 的第二个下界和 $v_p((h-1)!)$ 均随 $h$ 不减，
这支付整个 $h>H$ 尾，而不是有限试算。
$M^*_{p,H}\to\infty$，所以仍有逐素位完整证书
$$
j_m\ne0\iff\exists H:\ v_p(L_{m,H})<M^*_{p,H}.
\tag{29}
$$

## 6. 下一 Bockstein：保完整尾的原两条来源条件

由 (26)、(28)，准确有
$$
\boxed{
j_m\equiv\frac p{\gamma_m}g_{m,1}
-\frac{p^2}{\gamma_m^2}g_{m,2}\pmod{p^3}.
}
\tag{30}
$$
这里 $h=3$ 及全部后续项都确实在 $p^3$ 中。
这比旧一般半径界只给 $h=3$ 在 $p^2$ 中更强。

记同一个原完整来源的中央系数
$$
A_{m,k}=[w^{ks}]A_m .
\tag{31}
$$
原 $A_m(0)=0$，所以准确有
$$
g_{m,1}=A_{m,1},\qquad
g_{m,2}=A_{m,2}-\frac{\gamma_m}{p}A_{m,1}.
\tag{32}
$$
第二式的左边由 (26) 整；右边两个原量必须一起保留。
将其代入 (30)，得到
$$
\boxed{
\frac{j_m}{p}\equiv
\frac1{\gamma_m}
\left(2A_{m,1}-\frac p{\gamma_m}A_{m,2}\right)
\pmod{p^2}.
}
\tag{33}
$$
括号内是整的真实量，不是两个自由来源行。
特别
$$
\boxed{
j_m=0\Longrightarrow
2A_{m,1}-\frac p{\gamma_m}A_{m,2}\in p^2\mathcal O.
}
\tag{34}
$$

若原首层失败 $A_{m,1}\in p\mathcal O$，则 (32) 还给
$A_{m,2}\in\mathcal O$，并可准确读取第二层：
$$
\boxed{
\frac{j_m}{p^2}\equiv
\frac1{\gamma_m}
\left(\frac{2A_{m,1}}p-\frac{A_{m,2}}{\gamma_m}\right)
\pmod p.
}
\tag{35}
$$
若 (35) 右边非零，则完整 $j_m$ 非零，
从而原 R303/R402 的完整通常 Selmer 桥给对应固定曲线
$\Sha[p^\infty]$ 有限。
本篇没有证明 (35) 对无穷 $p$ 命中，
也没有将首层失败改写为 $A_{m,1}=0$ 的特征零等式。

## 7. 所有有限精度返回原系数的准确二项式式

为了保留以后层中的完整原来源，可以直接消掉有限 Gaussian 卷积。
由
$$
g_{m,h}=\sum_{k=1}^h
\frac{(-\alpha_m)^{h-k}}{(h-k)!}A_{m,k},
$$
交换有限和并使用
$\sum_{h=k}^H\binom{h-1}{k-1}=\binom Hk$，准确得到
$$
\boxed{
L_{m,H}=
\sum_{k=1}^H(-1)^{k-1}(k-1)!\binom Hk
\left(\frac p{\gamma_m}\right)^k A_{m,k}.
}
\tag{36}
$$
因此原完整中央零对每个 $H$ 都迫
$$
\boxed{
\sum_{k=1}^H(-1)^{k-1}(k-1)!\binom Hk
\left(\frac p{\gamma_m}\right)^{k-1}A_{m,k}
\in p^{M^*_{p,H}-1}\mathcal O .
}
\tag{37}
$$
整个和的整性来自 (25)、(36)；高 $H$ 时不把各个裸 $A_{m,k}$ 先当整数。

例如 $M^*_{p,1}=2,M^*_{p,2}=3,M^*_{p,3}=4,M^*_{p,4}=5$，
所以原 $j_m=0$ 依次给
$$
A_{m,1}\in p\mathcal O,
$$
$$
2A_{m,1}-(p/\gamma_m)A_{m,2}\in p^2\mathcal O,
$$
$$
3A_{m,1}-3(p/\gamma_m)A_{m,2}
+2(p/\gamma_m)^2A_{m,3}\in p^3\mathcal O,
$$
$$
4A_{m,1}-6(p/\gamma_m)A_{m,2}
+8(p/\gamma_m)^2A_{m,3}
-6(p/\gamma_m)^3A_{m,4}\in p^4\mathcal O.
\tag{38}
$$
这些条件是同一完整 $j_m=0$ 的准确必要条件，
不是对每个乘积、每个投影或每个辅助函数另添一个中央零。
(36) 只交换有限和，未将无限 Newton 展开非法换序。

## 8. R598 的同一中央 Euler 解延拓到更大开盘

保持原固定
$$
U_m=\int_0^z A_m(t)\,\frac{dt}{t},\qquad
\Pi_0=\frac1d\sum_{\zeta^d=1}(\zeta^*),\qquad X=z^d.
$$
R598 的准确恒等式是
$$
H_m=d e^{-\alpha_mX}\Pi_0U_m
=-j_m e^{-\alpha_mX}+\mathcal R_m(X),
$$
$$
\mathcal R_m(X)=\sum_{n\ge0}\sum_{j\ge0}
(-1)^j\frac{(n+j)!}{n!}\alpha_m^{-j-1}g_{m,n+j+1}X^n.
\tag{39}
$$
使用 (23)，对任意 $\rho\le R<R_*$、$R=p^{-\tau}$，
第 $j$ 项在 $R^d$ 范数中的加权赋值至少
$$
(j+1)(1-d\tau)+6\tau.
\tag{40}
$$
因 $\tau\le1/(2p)$，$1-d\tau>0$。
所以 $j$ 尾一致趋零；固定 $j$ 时，(23) 的 Tate 尾保证
$n$ 方向趋零。故同一个 $\mathcal R_m$ 满足
$$
\boxed{\mathcal R_m\in\mathbf C_p\langle X/R^d\rangle
\quad\text{对每个 }\rho\le R<R_*.}
\tag{41}
$$
其原点值仍是完整 $j_m$，不是另选积分常数。

原指数的准确坏半径
$S^d=p^{-p/(p-1)}$ 及闭边界非 Tate 由 R598 保持。
因此
$$
\boxed{
j_m=0\iff H_m\text{ 在每个闭 }R<R_*\text{ 的中央盘解析}
\iff H_m\text{ 在原闭 }S^d\text{ 是 Tate 元}.
}
\tag{42}
$$
第一条件中的变量半径是 $X$ 的 $R^d$；原 $z$ 半径为 $R$。
原始 $\Pi_0$ 仍不可删。未投影 $U_m$ 的单位第六角正被它杀掉，
不能从 (41) 或原非中央单位宣称两个 $j_m$ 不同时为零。

## 9. 真实范围与继续接口

本篇实际加强的是同一个原余项的全部系数界、严格解析圆盘、
完整 Newton 尾以及原第二层 (33)–(35)。
R595/R596 的同参数首对角与非齐次 pole 约束仍可同时使用；
下一层现在必须使用原 $A_{m,2}$ 及 (32) 的完整整组合。

没有把这些更长整窗口认成全部 $D/k$ 的真饱和整性。
原九来源中的 Euler 分母、真实前缀、同权碰撞和原列预算仍须逐项保留。
R600 对乘积的中央低卷积也没有因 (34) 被赋为零。
两条原完整中央同时失败给两组 (37)，
从它们排除同一无限集合上的联合失败仍未完成。

## 依赖

- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)：
  同一个高度二 $X_n$ 界、准确原 sigma 分母与首 Gaussian。
- [R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
  [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)：
  两原完整 Newton 函数、物理缩放和通常 Selmer 比较。
- [R586](R586-original-euler-resonant-coefficients-and-first-square-window.md)：
  七原 Euler 来源的准确规范化分子和原首 forcing 指标。
- [R598](R598-original-full-newton-derivatives-and-central-euler-stokes.md)：
  固定零初值 Euler 原函数、完整中央 Stokes 恒等式及准确坏边界。
- [R600](R600-original-central-residue-blocks-and-true-prefix-vandermonde.md)：
  原全部余类首层与真前缀；本篇不删其中的全列条件。

本篇为全参数证明，没有新增素数扫描或依赖未执行数值证书。
