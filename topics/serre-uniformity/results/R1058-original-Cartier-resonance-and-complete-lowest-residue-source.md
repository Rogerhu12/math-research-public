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

## 来源和独立纸核

- [R1037](R1037-original-Hodge-graph-operator-and-primitive-MW-annihilator.md) §§3–6、[R1040](R1040-original-p5-Hodge-graph-and-primitive-MW-annihilator.md)：两行原算子、原 $q_s$、完整商、$D$ 和插值规范。
- [R1045](R1045-original-MW-annihilator-nonzero-reduction.md) §§1、4：原有限 Gauss 方程、反射与完整 $S_0=1$。
- [R1052](R1052-original-complete-CM-profile-and-actual-lowest-functional.md) §§7–8、[R1055](R1055-original-complete-first-log-canonical-rational-primitive.md)：实际最低极部、完整 $\mathcal V$ 及有理代表与全商的接口。

global_route 推导规范 primitive、全 Cartier 和 $T_\lambda/A$；o2_high_coefficient 独立核 $p$ 次修正，并给全反射及完整 $D$ 后总留数；root 逐式核所有残数、无穷次数、primitive 唯一性、角色运输和半线性。本文全部为纸面证明，没有执行数学程序，没有重复旧窗口。
