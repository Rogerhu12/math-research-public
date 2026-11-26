# R1058：原 Cartier 算子、共振修正与完整指定最低值的有理来源

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126；global_route / o2_high_coefficient / root。

**已证明：原 $Q_{\rm op}$ 可由同一 $\mathbf P^1$ 上的 Cartier 算子准确读取；其全有理 primitive 含一个必须保留的共振项。** 本篇给出规范有理 $\widehat J$、原 $T_\lambda/A$ 的全部 $p$ 次修正，以及实际 $DQ_{\rm op}(1-Q_{\rm op})\lambda$ 最低值的完整三 CM 留数。没有删掉 $Q_{\rm op}^2$，没有把非 $\mathbf F_p$ 单点的 Cartier 留数直接视作它的 $p$ 次根。

## 1. 原对象与唯一规范有理延拓

对全部 $p=6N+5\ge41$，保持
$$
\ell=2N+2,\quad r=1-b^3,\quad A=bQ(b^3)\text{ 单首},
\quad A_1=Q(1),\quad q(x)=Q(x)/Q(0).
$$
R1045 给 $Q(1-x)=(-1)^NQ(x)$，所以
$$
Q(0)^2=A_1^2,\quad q(1-x)^2=q(x)^2,\quad
A=A_1bq(r).
$$
$j$ 仍只指 R1050 的安全 $0,\ldots,\ell-1$ 次 period 系数，绝不跨首个坏分母。

置
$$
W_{\rm poly}(x)=\frac{(1-x)^{2\ell-2}}{q(x)^2},\qquad
\omega=\left(x^{-\ell-1}W_{\rm poly}(x)-\frac{A_1^2}{x}\right)dx.
\tag{1058.1}
$$
$\omega$ 的全部留数为零。具体地，在 $q$ 的任一根 $\alpha$，令
$h=x^{-\ell-1}(1-x)^{2\ell-2}$。原 Gauss 方程给
$$
\frac{h'}h(\alpha)
=-\frac43\frac{1-2\alpha}{\alpha(1-\alpha)}
=\frac{q''}{q'}(\alpha),
$$
这正使 $h/q^2$ 的双极展开中简单极部为零。在 $x=0$，
R1045 的 $S_0=1$ 和 $\ell$ 偶给
$$
[x^\ell]W_{\rm poly}=A_1^2,
$$
故减去的项准确消去其留数。$W_{\rm poly}$ 在无穷的首项为
$A_1^2x^\ell$，所以 $\omega=O(x^{-2})dx$。

$\omega$ 只在零点有至多 $\ell+1<p$ 阶极，在 $q$ 根有至多二阶极；它没有 polynomial 部。逐个完整 principal part 积分，只除以 $1,\ldots,\ell$，给唯一有理函数 $H_\omega$ 满足
$$
H_\omega'=\omega/dx,\quad H_\omega(\infty)=0,
$$
且在零点的极阶至多 $\ell$、在 $q$ 根的极阶至多一。唯一性使用 $p$ 次有理函数的非零极阶必为 $p$ 的倍数，而非误用“同导数只差常数”。规范和 Galois 不变性也给 $H_\omega\in\mathbf F_p(x)$。

定义
$$
\widehat J(x)=-x^\ell H_\omega(x)/3.
$$
则全有理恒等式为
$$
\boxed{\quad
\widehat J-3x\widehat J'
=W_{\rm poly}-A_1^2x^\ell.
\quad}
\tag{1058.2}
$$
$\widehat J$ 在零点正则、只允许 $q$ 根的一阶极、无穷增长至多 $\ell-1$；这些条件唯一确定它。由于
$2\ell-2\equiv-4/3\bmod p$，(1058.2) 的 $i<\ell$ 递推与 R1055 的安全 Wronskian 相同，故
$$
\widehat J=j/q\pmod{x^\ell}.
\tag{1058.3}
$$
在 $i=\ell$ 时 $1-3i=0$，修正项 $-A_1^2x^\ell$ 必须保留。$\widehat J$ 是此规范的有理延拓，不称作完整的特征 $p$ period。

## 2. 全 $\mathbf P^1$ 上的准确 Cartier primitive

令
$$
f=r^{2\ell-2},\quad g=f/A^2,\quad
R_{\rm can}(b)=\frac{r^{p-\ell}}{A_1^2b^{2p}}\widehat J(r),
\qquad
\omega_0=(r/b^2)^{p-1}db.
$$
直接用 (1058.2)、$dr/db=-3b^2$ 和
$p-\ell-1=2\ell-2$ 得
$$
\boxed{\qquad g\,db=dR_{\rm can}+\omega_0.\qquad}
\tag{1058.4}
$$
例如第一项中的 $(1-r)^{2\ell-2}=b^{2p-4}$，与 $b^{2-2p}$ 相乘准确给 $b^{-2}$；第二项则正好是 $-\omega_0$。

记 $\mathscr C_b$ 为 Cartier。因为
$$
\omega_0=(r/b^2)^p(b^2/r)\,db,\qquad
(b^2/r)\,db=-d\log r/3,
$$
Cartier 的乘法与对数性质给
$$
\boxed{\quad \mathscr C_b(\omega_0)=db,\qquad
\mathscr C_b(g\,db)=db.\quad}
\tag{1058.5}
$$
$b=0$ 的真实高极部和 (1058.2) 的共振项正保证这条非零 Cartier 值。将安全 $j/q$ 当成全 period、把 $g\,db$ 错写成纯 exact，会改变原算子。

## 3. 原 $Q_{\rm op}$ 的全局 Cartier 身份

对 $\mathbf F_p$ 系数的原类 $a\in\mathbf F_p[b]/(A)$，令
$$
T_a\equiv f\,a(b^p)/A'\pmod A,\quad \deg T_a<\deg A,
\qquad \mathcal F_a=T_a/A.
\tag{1058.6}
$$
始终区别 $\mathcal F_a$ 与 raw 源 $g\,a(b^p)$。原算子是 R1037/R1040 的完整 quotient：
$$
Q_{\rm op}a=\operatorname{quo}(f\,a(b^p),A^2)\bmod A.
$$
则
$$
\boxed{\qquad
\mathscr C_b(g\mathcal F_a\,db)=\mathcal F_{Q_{\rm op}a}\,db.
\qquad}
\tag{1058.7}
$$

下面验证它是全有理恒等式。$g\mathcal F_a=fT_a/A^3$ 只有 $S=\{A=0\}$ 处至多三阶极。令 $\kappa=f'/f=4b^2/r$。根处原方程及其导数给
$$
A''/A'=\kappa,\qquad A'''/A'=\kappa'+\kappa^2+9b/(4r).
$$
展开全部三阶极部，简单极部准确为
$$
\rho_s=\frac{f(s)\,\mathcal LT_a(s)}{2r(s)A'(s)^3}
=-q_s(Q_{\rm op}a)(s),
\qquad q_s=-f(s)/A'(s)^2\in\mathbf F_p^\times.
\tag{1058.8}
$$
这里使用原完整 quotient 的
$Q_{\rm op}a\equiv\mathcal LT_a/(2rA')\pmod A$；没有另取 shadow 算子。

Cartier 杀掉二阶、三阶极部，对简单极部取 $p$ 次根。因为
$S\subset\mathbf F_{p^2}$、$a$ 的外部系数在 $\mathbf F_p$，
$$
\rho_s^{1/p}=-q_s(Q_{\rm op}a)(s^p)
=\frac{T_{Q_{\rm op}a}(s)}{A'(s)}.
$$
这与右侧的全部简单极部相同，包括 $b=0$。

在无穷，$fT_a/A^3$ 的 polynomial 部次数至多
$$
(2p-4)+(\deg A-1)-3\deg A=p-2,
$$
全部被 Cartier 杀掉。右侧是真分式。两侧全部有限极部一致，且无 polynomial 部，所以 (1058.7) 成立。

## 4. 原 $\mathcal F_\lambda$ 的全部 $p$ 次修正

保持 $\lambda=-6(b+1)/r$，以及 R1055 的唯一 $\mathcal V$，其微分为
$v_{\rm can}\,db=(\lambda-R_\lambda)\,db$。定义
$$
E(b)=6\sum_{i=1}^{\ell-1}\frac{b^{1-3i}}{1-3i}
 +6\sum_{i=1}^{2\ell-1}\frac{b^{2-3i}}{2-3i}.
\tag{1058.9}
$$
两组首次零分母分别在 $i=\ell$、$i=2\ell$，均不在求和中。完整有限几何和给
$$
E'\,db=\lambda\,db-\lambda(b^p)\omega_0.
\tag{1058.10}
$$
原 raw 源为
$$
\mathfrak R_\lambda=g\lambda(b^p)
=-6(b^p+1)/(r^{\ell+1}A^2).
$$
R1055 的完整 principal-part 接口给
$$
\mathfrak R_\lambda=-\mathcal F_\lambda'+R_\lambda,
\qquad \mathcal F_\lambda=T_\lambda/A.
\tag{1058.11}
$$
故由 (1058.4)、(1058.10)，
$$
K=E-\lambda(b^p)R_{\rm can}-\mathcal V-\mathcal F_\lambda
\quad\text{满足}\quad K'=0.
$$
在三个 CM 点它的极阶至多 $\ell<p$，在 $q$ 根至多一，这些极都被 $K'=0$ 排除；在无穷它趋于零。仅 $b=0$ 可有至多 $2p$ 阶极。因此准确地
$$
K=\alpha b^{-2p}+\beta b^{-p}.
\tag{1058.12}
$$
这两个项不能省作“常数”。

又
$$
\lambda(b^p)R_{\rm can}
=-\frac6{A_1^2}(b^{-p}+b^{-2p})r^{-\ell}\widehat J(r),
$$
而 $r^{-\ell}\widehat J(r)=\widehat J(1)+O(b^3)$。$p$ 不是三的倍数，所以后一展开不能从 $b^{-2p}$ 向 $b^{-p}$ 贡献。$E$ 不含这两个 $p$ 倍指数；$\mathcal V$ 在零点正则，$\mathcal F_\lambda$ 在零点仅简单极。于是
$$
\alpha=\beta=6\widehat J(1)/A_1^2,
$$
得到准确全式
$$
\boxed{\quad
\mathcal F_\lambda=
E+\frac6{A_1^2}(b^{-p}+b^{-2p})
 \bigl(r^{-\ell}\widehat J(r)-\widehat J(1)\bigr)
-\mathcal V.
\quad}
\tag{1058.13}
$$
必须完整相加后才读取 $b=0$ 或模 $A$；$b=0$ 本在 $S$ 中，不能分别逆 $b$ 后擅自取商。$\widehat J(1)$ 未被宣为单位。

## 5. 规范延拓的有限对数反射

置 $\mathcal L_1(x)=\sum_{i=1}^{p-1}x^i/i$。准确全式为
$$
\boxed{\quad
x^{p-\ell}\widehat J(x)
 +(1-x)^{p-\ell}\widehat J(1-x)
=\widehat J(1)-\frac{A_1^2}{3}\mathcal L_1(x).
\quad}
\tag{1058.14}
$$
证明：左边记为 $Y$。对 (1058.2) 使用原反射
$q(1-x)^2=q(x)^2$ 后，含 $W_{\rm poly}$ 的两项完全相消，得到
$$
Y'=\frac{A_1^2}{3}\left(x^{p-1}-(1-x)^{p-1}\right)
=-\frac{A_1^2}{3}\sum_{i=0}^{p-2}x^i.
$$
$Y$ 只可能有 $q$ 根的一阶极；其导数是多项式，迫这些极全部消失。无穷次数至多 $p-1$，所以扣除右侧后的零导数多项式只能是常数。代 $x=0$ 固定该常数为 $\widehat J(1)$，没有遗漏一个 $p$ 次多项式。

代 $x=r$，同一个 primitive 还可写成
$$
R_{\rm can}=\frac{\widehat J(1)}{A_1^2b^{2p}}
-\frac{\mathcal L_1(r)}{3b^{2p}}
-\frac{\widehat J(b^3)}{A_1^2b},
\tag{1058.15}
$$
其中 $3(p-\ell)-2p=-1$。各项的 $b=0$ 极部仍须完整保留。

## 6. 完整原 $D,Q,Q^2$ 的实际最低值

令 $L=L_{\rm CM}$ 为 R1052 的原全部 principal-part source，并定义
$\tau F(b)=F(\zeta b)$。在原 Lie 类和 $\mathcal F$ 空间，实际作用分别是
$$
D_a=\frac{\zeta^2\tau^2-\zeta\tau}{\zeta^2-\zeta},
\qquad
D_F=\frac{\tau-\tau^2}{\zeta^2-\zeta},
\qquad \mathcal F_{D_aa}=D_F\mathcal F_a.
\tag{1058.16}
$$
核准最后一式：$a$ 的 $b^j$ 指数类在 $T_a$ 中变成 $2j$，再除 $A$ 使 $\mathcal F_a$ 的类为 $2j-1$。两侧的三个角色逐个一致。

从 $b\mapsto\zeta b,\zeta^2b$ 的实际微分换元，得到
$$
\operatorname{Res}_{b=1}(D_FF)L\,db
=\sum_{\alpha^3=1}\operatorname{Res}_{b=\alpha}F(D_aL)\,db.
\tag{1058.17}
$$
右侧 $D_aL$ 的极点实际在 $\zeta,\zeta^2$，在 $1$ 正则；不能只保一个点。

对任意 rational $\omega,h$，Cartier 留数自然性为
$$
\operatorname{Res}(h\mathscr C_b\omega)
=\left(\operatorname{Res}(h^p\omega)\right)^{1/p}.
$$
本文的完整三 CM 总和由 Frobenius 保持，所有原输入作为有理函数均在 $\mathbf F_p$，因此该**总和**属于 $\mathbf F_p$，可消去其 $p$ 次根。把 (1058.7) 应用一次和两次，再用 (1058.17)，得
$$
\boxed{\begin{aligned}
&\mathcal C_{\rm CM}
 \bigl(T_{D_aQ_{\rm op}(1-Q_{\rm op})\lambda}\bigr)\\
&\quad=
\sum_{\alpha^3=1}\operatorname{Res}_{b=\alpha}
 \mathcal F_\lambda
 \left\{g(D_aL)^p-g^{p+1}(D_aL)^{p^2}\right\}db .
\end{aligned}}
\tag{1058.18}
$$
$\mathcal F_\lambda$ 在这里准确为 (1058.13) 的 $T_\lambda/A$，
**不是** (1058.11) 的 raw $\mathfrak R_\lambda$。
第二项是完整真实 $Q_{\rm op}^2$，其负号保原 $(1-Q_{\rm op})$。这些项不能用核的一维性、短 period 或单点 Frobenius 省掉。

在 $\mathbf F_p$ 点 $b=1$，没有 $D$ 时也有直接检查式
$$
\mathcal C_{\rm CM}(T_{Q_{\rm op}a})
=\operatorname{Res}_1\mathcal F_a gL^pdb,\qquad
\mathcal C_{\rm CM}(T_{Q_{\rm op}^2a})
=\operatorname{Res}_1\mathcal F_a g^{p+1}L^{p^2}db.
$$
它们与完整三点式相容；一般 CM 点必须保留上述 $p$ 次根或整个 Frobenius 稳定总和。

## 7. 已付输入和剩余目标

(1058.18) 是原指定最低值的全源表达，其各组成有明确规范，所有真实返回均保留。R1057 的固定 $p=47$ 真值 $15$ 只支付该输入；本篇不据此外推全 $p$，也不将 $\widehat J(1)$、R1056 的核行系数或原 bare 系数自动视为同一值。后续继续求 (1058.18) 的指定非零性或其它足以排非中心深盘点的输入，O0 完整全局覆盖仍开。

## 8. 规范分子的次数与原 $D$-primitive

以下仍对全部 $p=6N+5\ge41$，置
$
x=1-r=b^3,\quad d=\ell-1,\quad M=N+d=(p-3)/2,\quad
P=q\widehat J.
$
这里的 $P$ 不是 R1048 的核 primitive 分子。原反射给单首 $Q$ 的次首系数 $-N/2$，故
$
q(r)=Q(0)^{-1}r^N(1-N/(2r)+O(r^{-2})),
$
$
W_{\rm poly}=A_1^2r^\ell(1-(3N+2)/r+O(r^{-2})).
$
(1058.2) 中 $r^d$ 的算子系数为 $1-3d=3$，而
$3N+2=(p-1)/2$。因此
$
\boxed{\deg\widehat J=d,\quad\deg P=M,\quad
\operatorname{lc}\widehat J=A_1^2/6,\quad\operatorname{lc}P=Q(0)/6.}
\tag{1058.19}
$
$\widehat J$ 在 $q$ 根至多简单极，故 $P$ 是多项式。完整一阶式为
$
Pq-3r(P'q-Pq')=\Delta,\qquad
\Delta=x^{2\ell-2}-A_1^2r^\ell q^2.
\tag{1058.20}
$
在 $q(\alpha)=0$ 处，
$3\alpha P(\alpha)q'(\alpha)=(1-\alpha)^{2\ell-2}\ne0$，
所以 $(P,q)=1$。又 $P(0)=1$。
若 $\widehat J(1)=0$，则 (1058.2) 给
$\widehat J'(1)=A_1^2/3$，所以 $P$ 在 $1$ 至多简单零；
没有假设该端点非零。

定义
$
c_H=\frac{(-3)^d}{1-\ell},\quad
H_0(r)=c_Hr^{-d}\widehat J(r)^{-2},\quad
d_0(b)=\frac{b^2-b}{3},
$
$
K_D(b)=d_0(b^p)H_0(1-b^3),\qquad
L_D(b)=K_D'(b)=d_0(b^p)\frac{dH_0(1-b^3)}{db}.
\tag{1058.21}
$
$1-\ell=2/3$ 是单位。原 $Z=-r(q/j)^3/3$ 给
$
Z^{1-\ell}/(1-\ell)=c_Hr^{-d}(j/q)^{3d}.
$
由 $3d=p-2$、$\widehat J=j/q\bmod r^\ell$、
$\widehat J^p=1+O(r^p)$，此式的全部 CM principal part 正等于 $H_0$。
这是原 $Z$ 的准确尺度。

原 $D_aL_{\rm CM}$ 在 $b=1,\zeta,\zeta^2$ 的 primitive 系数依次为
$0,-1/(\zeta-\zeta^2),+1/(\zeta-\zeta^2)$。
$p\equiv-1\bmod3$ 时它们正是 $d_0(\alpha^p)$。
又 $d_0(b^p)-d_0(\alpha^p)=O((b-\alpha)^p)$，
而 $H_0$ 的 CM 极阶为 $d<p$，故
$
\operatorname{PP}_{b=\alpha}L_D
=\operatorname{PP}_{b=\alpha}(D_aL_{\rm CM})
\quad(\alpha^3=1).
\tag{1058.22}
$

## 9. 完整最低值迁移到全部规范根

保持原 $\mathcal F_\lambda=T_\lambda/A$、$g=r^{2\ell-2}/A^2$，令
$
\mathcal I=\mathcal F_\lambda
\{gL_D^p-g^{p+1}L_D^{p^2}\}\,db.
\tag{1058.23}
$
三个 CM 点处 $\mathcal F_\lambda$ 正则、$g$ 有 $2\ell-2$ 阶零。
(1058.22) 替换的差正则，其 $p$ 次和 $p^2$ 次幂也正则；
故 (1058.18) 的完整 CM 总留数就是 $\sum_{\alpha^3=1}\operatorname{Res}_\alpha\mathcal I$。

全部其它极点如下逐一支付；次数界指微分系数，无穷另包含 $db$ 的二阶极。

1. 非零 $S$ 点是 $q(r)=0$。因 $(P,q)=1$，$H_0$ 至少二阶零、$L_D$ 至少一阶零；$\mathcal F_\lambda$ 至多简单极、$g$ 至多二阶极。两项的阶至少为 $p-3$、$p^2-2p-3$，均无极。
2. 在 $b=0$，$\mathcal F_\lambda$ 至多简单极、$g$ 至多二阶极。若 $\widehat J(1)\ne0$，$H_0(1-b^3)$ 正则、导数至少二阶零，故 $L_D$ 至少 $p+2$ 阶零。若 $\widehat J(1)=0$，该 $r$ 零至多简单，$H_0$ 的 $b$ 极阶至多六、导数极阶至多七，而 $d_0(b^p)$ 有 $p$ 阶零。最坏 $\operatorname{ord}_0L_D\ge p-7$，两项阶至少 $p(p-7)-3$、$p^2(p-7)-2p-3$，对 $p\ge41$ 为正。即使 $P(1)=0$，这里的留数仍为零。
3. 在无穷，$g=O(b^{p-1})$、$\mathcal F_\lambda=O(b^{-1})$。由 (1058.19)，$H_0=O(b^{-3p+6})$、$K_D=O(b^{6-p})$、$L_D=O(b^{5-p})$。两项系数最高次数至多 $-p^2+6p-2$、$-p^3+6p^2-2$，均至多 $-2$，所以无穷无留数。
4. 其它有限潜在极点只剩 $P(1-b^3)=0$。它与 CM 点不交，因为 $P(0)=1$；与非零 $S$ 不交，因为 $(P,q)=1$。

全局留数定理给
$
\boxed{
\mathcal C_{\rm CM}(T_{D_aQ_{\rm op}(1-Q_{\rm op})\lambda})
=-\sum_{P(1-b^3)=0}\operatorname{Res}_b\mathcal I .
}
\tag{1058.24}
$
这里保留全部根及真实重数；若包含 $b=0$，该项已证为零。
非零 $b$ 的重数 $h$ 根处，$H_0$ 极阶为 $2h$，$L_D$ 极阶至多
$2h+1\le2M+1=p-2$；§11将其改进为九阶界。
直接相乘还有全式
$
\boxed{
gK_D\,db=\frac{c_H}{A_1^2}\,
d_0(b^p)\frac{r^d}{b^2P(r)^2}\,db .
}
\tag{1058.25}
$
$q^2$ 在此准确消去到规范分母 $P^2$；没有消去 (1058.23) 的第二个 $Q_{\rm op}$。

## 10. 实际非齐次 Gauss 方程与根处留数

令
$
\mathcal L_j=r(1-r)\partial_r^2+
(2/3-2r)\partial_r-1/4.
$
原 $q$ 满足
$
r(1-r)q''+(4/3-8r/3)q'-25q/36=0,
$
所以 $y_2=r^\ell q$ 满足 $\mathcal L_jy_2=0$。由 (1058.20)，
$
P y_2'-P'y_2=\frac{r^{\ell-1}}3
\{x^{2\ell-2}-A_1^2r^\ell q^2\}.
$
第一项满足齐次 Wronskian 一阶方程，第二项是
$-A_1^2y_2^2/(3r)$。对完整 Wronskian 微分，得到
$
\boxed{
\mathcal L_jP=\frac{A_1^2}{9}r^{\ell-1}K,\qquad
K=(1-5r)q+6r(1-r)q'.
}
\tag{1058.26}
$
$P$ 因而不是齐次 period 多项式。最高次校验：$K$ 的 $r^{N+1}$
项因 $5+6N=p$ 消失，其 $r^N$ 系数为 $-3/(2Q(0))$。
右侧最高项 $-Q(0)r^M/6$ 正等于左侧
$-(M+1/2)^2\operatorname{lc}(P)r^M$。

置 $h_{\rm rat}=r^{\ell-1}(1-r)^{-\ell-1}$，则
$
h_{\rm rat}'/h_{\rm rat}
=-\frac{2/3-2r}{r(1-r)}.
$
在 $P$ 的简单根 $\alpha\ne1$，完整双极部给
$
\begin{aligned}
\operatorname{Res}_\alpha\frac{h_{\rm rat}}{P^2}\,dr
&=\frac{h_{\rm rat}(\alpha)}{P'(\alpha)^2}
\left(\frac{h_{\rm rat}'}{h_{\rm rat}}-\frac{P''}{P'}\right)(\alpha)\\
&=-\frac{h_{\rm rat}(\alpha)(\mathcal L_jP)(\alpha)}
{\alpha(1-\alpha)P'(\alpha)^3}.
\end{aligned}
\tag{1058.27}
$
重根仍取完整 principal part；$\alpha=1$ 的 $b=0$ 点使用§9。

由于 $b^{p+4}=(1-r)^{\ell+1}$、$dr=-3b^2db$，
$
\frac{r^d}{b^2P^2}\,db
=-\frac{b^p}{3}\frac{h_{\rm rat}}{P^2}\,dr.
$
Cartier 的可分换元自然性和 $p$ 次乘法性给
$
\boxed{
\mathscr C_b(gK_D\,db)
=-\frac{c_H}{3A_1^2}\,b\,d_0(b)\,
\mathscr C_r\left(\frac{h_{\rm rat}}{P^2}\,dr\right).
}
\tag{1058.28}
$
右侧是 $r$-微分在 $b$ 线上拉回的式子，不能直接等同两坐标的微分系数。
所有常数均在 $\mathbf F_p$，取 $p$ 次根后不变。

与原 bare 来源的准确差为
$
B_{\rm bare}=\frac{1-2r}{1-r}+3r\frac{q'}q,\qquad
\boxed{K/q=2(1-r)B_{\rm bare}-(1+r).}
\tag{1058.29}
$
额外的 $1+r$ 必须保留。这没有证明根处留数相消，也没有将原 bare 与实际 $DQ_{\rm op}(1-Q_{\rm op})\lambda$ 等同。

## 11. 全部规范根的固定重数界

由 (1058.20) 直接微分有
$
\Delta'-\frac4{3(1-r)}\Delta
=-\frac{A_1^2r^{\ell-1}q}{3(1-r)}K.
\tag{1058.30}
$
设 $\alpha\ne0,1$ 为 $P$ 的重数 $h$ 根。
$(P,q)=1$、$h\le M<p$ 及 (1058.20) 给
$\operatorname{ord}_\alpha\Delta=h-1$。
若 $h\ge2$，导数首系数 $h-1$ 非零，
(1058.30) 给 $\operatorname{ord}_\alpha K=h-2$。

以原 $q$ 方程微分 $K$，得
$
K'=-(1+r)q'-5q/6.
$
在 $K=0$ 处，
$
K'/q=(1-9r)/(6r(1-r)).
$
所以 $K$ 在 $r\ne0,1$ 的重根只能在 $r=1/9$。
若该点确为重根，则
$
q'/q=-3/4,\qquad q''/q=477/32,\qquad K''/q=-243/16\ne0.
$
因此 $K$ 至多双根，得到
$
\boxed{
P\text{ 在 }r\ne0,1\text{ 的根至多四重；四重只可能在 }r=1/9.
}
$
$r=0$ 非根，$r=1$ 至多简单根已证。这不是 squarefree 断言。
于是 (1058.24) 全部非零 $b$ 根处
$
\boxed{\operatorname{poleord}L_D\le2h+1\le9.}
$
完整原问题可使用固定至多九阶局部资料，但仍须结算全部根、
$\mathcal F_\lambda$ 和两个 Frobenius 项的总和。此界本身不给总和非零，也不关闭 O0。


## 12. 保留完整 $Q^2$ 的同分母单系数与七阶局部式

在§§8–11的规范下，先明确原输入：
$
\mathcal F^{(0)}=\mathcal F_\lambda,\qquad
\mathcal F^{(i+1)}db=\mathscr C_b(g\mathcal F^{(i)}db)
\quad(i=0,1),
$
$
\mathcal F=\mathcal F^{(1)}-\mathcal F^{(2)}
=\mathcal F_{Q_{\rm op}v},\qquad v=(1-Q_{\rm op})\lambda .
$
$\mathcal F^{(0)}$ 是 (1058.13) 的完整式；第二项始终保留原
$Q_{\rm op}^2\lambda$。原次数及两非平凡角色给唯一分解
$
\mathcal F=\frac{bU(r)}{A_1q(r)}
+\frac{b^2V(r)}{A_1xq(r)},\qquad
\deg U<N,\quad\deg V\le N.
$
置
$
N_*=-x^\ell U+x^{2\ell-1}V,\qquad
W_*=N_*'q-N_*q'.
\tag{1058.31}
$
则完整原最低值有以下等价式：
$
\boxed{\begin{aligned}
\mathcal C_{\rm actual}
&=\frac{c_H}{A_1}
 \sum_{P(\alpha)=0}\operatorname{Res}_\alpha
 \frac{r^{-d}W_*}{P^2}\,dr\\
&=-\frac{c_H}{A_1}[r^{d-1}]\frac{W_*}{P^2}\\
&=\frac{(-3)^d}{dA_1}[r^{d-1}]\frac{W_*}{P^2}.
\end{aligned}}
\tag{1058.32}
$

第一证明从 (1058.24) 开始。单点处 Cartier 留数式仍必须保留
$p$ 次根：
$
\operatorname{Res}(\mathcal F_\lambda gL_D^pdb)
=\bigl(\operatorname{Res}(\mathcal F^{(1)}L_Ddb)\bigr)^p,
$
$
\operatorname{Res}(\mathcal F_\lambda g^{p+1}L_D^{p^2}db)
=\bigl(\operatorname{Res}(\mathcal F^{(2)}L_Ddb)\bigr)^{p^2}.
$
全 $P(1-b^3)$ 根集由 Frobenius 保持，所写有理函数均在
$\mathbf F_p$，所以只有取完该完整总和后才可去掉 $p,p^2$ 次方。
于是
$
\mathcal C_{\rm actual}
=-\sum_P\operatorname{Res}\mathcal F L_Ddb
=\sum_P\operatorname{Res}K_D\,d\mathcal F.
$
最后一步用 $d(K_D\mathcal F)$ 的留数为零。

对 $r=\alpha\ne1$ 的三个 $b$ 原像，真实三次 trace 为
$
\operatorname{Tr}_{b/r}\bigl(d_0(b^p)\mathcal F\bigr)
=\frac{-x^\ell U+x^{2\ell-1}V}{A_1q}
=\frac{N_*}{A_1q}.
$
这是直接使用 $\operatorname{Tr}(b^e)=0$（$3\nmid e$）及
$\operatorname{Tr}(b^e)=3x^{e/3}$（$3\mid e$）。
同时 $d(d_0(b^p))=0$，故 trace 与微分交换后，
$H_0=c_Hr^{-d}q^2/P^2$ 正好消去导数的 $q^2$ 分母，给第一式。
实际 $D$ 的两个 CM 相位已包含在 $d_0$ 中，没有增删一支。

若 $P(1)=0$，其重数至多一，而 $N_*$ 含 $x^\ell$、
$W_*$ 含 $x^{\ell-1}$，所以所写微分在 $r=1$ 仍正则；
与原 $b=0$ 的零贡献一致。
又 $\deg N_*\le5N+3$、$\deg W_*\le6N+2=2\deg P$，
所以无穷为 $O(r^{-d})dr$，$d\ge13$ 使其无留数。
除 $P$ 根外唯一额外极点是 $r=0$，其留数准确为
$[r^{d-1}]W_*/P^2$。全局留数定理给第二式，
$c_H=-(-3)^d/d$ 给第三式。

这里还可逐根写出全部临界资料。若
$P=(r-\alpha)^hP_\alpha$、$P_\alpha(\alpha)\ne0$、$\alpha\ne0,1$，
则其第一式中的单点贡献（未乘 $c_H/A_1$）为
$
\frac1{(2h-1)!}
\left.
\partial_r^{2h-1}
\left(\frac{r^{-d}W_*}{P_\alpha^2}\right)
\right|_{r=\alpha}.
$
§11给 $h\le4$，故最高仅七阶，所有阶乘在 $p\ge41$ 为单位。
这保留重根的完整留数，未假设 squarefree。

独立的第二证明直接用原 Lagrange 参数。在 $r=0$ 的首 $p$ 阶，
$x^\ell\equiv b$、$x^{2\ell-1}\equiv b^2/x$，
所以
$
N_* /(A_1q)\equiv D_F\mathcal F\pmod{r^p}.
$
R1052 的原 $Z$ 系数公式给
$
\mathcal C_{\rm actual}
=\frac{(-3)^d}{d}[r^{d-1}]
\left(\frac{N_*}{A_1q}\right)'\widehat J^{3d}.
$
$3d=p-2$，在所需安全截断中
$\widehat J^{3d}\equiv\widehat J^{-2}$，故准确回到 (1058.32)。
这同时独立核准所有符号、$A_1$ 与 $d$ 因子。

(1058.32) 使实际源与原 bare 来源可以在同一 $P^2$ 分母下比较；
它本身仍是原指定值的恒等式，不证明两分子相同、总值非零或 O0。


## 来源和独立纸核

- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md) §§3–6、[R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md)：两行原算子、原 $q_s$、完整商、$D$ 和插值规范。
- [R1045](R1045-original-MW-annihilator-nonzero-reduction.md) §§1、4：原有限 Gauss 方程、反射与完整 $S_0=1$。
- [R1052](R1052-original-complete-CM-profile-and-actual-lowest-functional.md) §§7–8、[R1055](R1055-original-complete-first-log-canonical-rational-primitive.md)：实际最低极部、完整 $\mathcal V$ 及有理代表与全商的接口。

global_route 推导规范 primitive、全 Cartier 和 $T_\lambda/A$；o2_high_coefficient 独立核 $p$ 次修正，并给全反射及完整 $D$ 后总留数；root 逐式核所有残数、无穷次数、primitive 唯一性、角色运输和半线性。本文全部为纸面证明，没有执行数学程序，没有重复旧窗口。

补充§§8–11：global_route给规范P、原D源的完整迁移、非齐次Gauss式及固定重数界；o2_high_coefficient独立核forcing和重数；root逐项核CM相位、q根/b0/无穷极阶、Cartier换元、简单根留数及r1/9二阶值。全部为纸面证明，无数学程序或窗口执行。

§12由global_route给完整Cartier总和/trace/分部积分证明，o2_high_coefficient以原Z的Lagrange式独立重导，root逐式核半线性、三次trace、r1与无穷、全部次数及符号；无数学执行。
