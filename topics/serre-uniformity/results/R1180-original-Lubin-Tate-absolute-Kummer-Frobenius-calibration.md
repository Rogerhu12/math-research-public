# R1180 — 原 Lubin–Tate 根的绝对 Kummer–Frobenius 校准

日期：2026-11-28。  
会话：Astra-serre-24b8836b-20261126。  
状态：已证明，纸面；没有数学程序执行。

## 1. 原两条局部线的准确单位

固定 $p>37$，取原同一个
$$
\varpi^{p^2-1}=p,\qquad
K=\mathbb Q_p(\zeta),\qquad
\gamma=\overline{(\zeta-1)/\varpi^{p+1}}.
$$
$\zeta$ 是原实际 Weil/Miller 根，不能换成一个只满足同样幂关系的任意根。
令
$$
j=1,2,\qquad
R_j=p-1-2j,\quad N_j=(p+1)R_j,\quad r_j=2j+1.
\tag{1180.1}
$$
沿 R1153 的同一正 Kummer 与 Tate tensor，把
$\xi\in H^1(\mathbb Q_p,\mathbb F_p(r_j))$ 写为
$$
\operatorname{res}_K\xi
 =\kappa(u_\xi)\otimes\zeta^{\otimes2j},\qquad
[u_\xi]\in(K^\times/K^{\times p})_{\omega^{-2j}}.
$$
原 leading 读数是
$$
\ell_{j,\zeta}(\xi)
 =\overline{\varpi^{-N_j}\log u_\xi}.
\tag{1180.2}
$$
这里的 log/character filtration 和取代表的不变性保持
R1071、R1153 §1 的原定义。

记 $\mathcal F_j$ 为 R1151 的实际正向 finite
Fontaine–Laffaille Frobenius 一次坐标。
本篇证明
$$
\boxed{\qquad
\mathcal F_j=\gamma^{2j}\ell_{j,\zeta},
\qquad j=1,2 .
\qquad}
\tag{1180.3}
$$
这是同一整格上完整局部直线的比较，不只比较某个非零 global class。

特别，R1153 的单位全部准确为
$$
\boxed{\quad
U_\star=\gamma_\star^2,\qquad
U_E=\gamma_E^2,\qquad
\eta_\star=U_\star\gamma_\star^{-2}=1.
\quad}
\tag{1180.4}
$$
它不要求 $B_{p-3}$ 或 $B_{p-5}$ 非零，
也不需要先找到一个 generic supersingular $\mathbb F_p$ 校准点。
因此本篇的局部比较本身没有 $C_{\rm SS}$ 门；
R1153 其余几何 statements 仍保持各自原有范围。

关键输入是原正 $\mu_p$ 的实际 syntomic $H^0$ 代表。
下面连同 $\gamma_p(g)$ carry、normalized corestriction、
Tate generator 和 R1177 的负号一起计算。

## 2. 同一个高度一 LT 群与同一个原 $\zeta$

令
$$
F=\mathbb Q_{p^2},\quad \mathcal O=W(\mathbb F_{p^2}),\quad
e=p^2-1,\quad L=F(\varpi).
$$
由原 cyclotomic Eisenstein 方程的最低项，
$$
\gamma^{p-1}=-1,\qquad \gamma^p=-\gamma .
\tag{1180.5}
$$
因此 $\gamma\in\mathbb F_{p^2}^\times$，而
$\gamma^2\in\mathbb F_p^\times$。
取其 Teichmüller lift $\widetilde\gamma\in\mathcal O^\times$；
准确有
$\widetilde\gamma^p=-\widetilde\gamma$，
$\widetilde\gamma^{p-1}=-1$。

取高度一 Lubin–Tate formal group $\mathcal G$，其
$p$-endomorphism 为
$$
[p]_{\mathcal G}(T)=pT+T^p .
$$
Lubin–Tate 的原 coefficient theorem 给唯一 strict
isomorphism
$$
h:\mathcal G\longrightarrow\widehat{\mathbb G}_m,\qquad
h(T)=T+O(T^2),\qquad h\in T\mathbb Z_p[[T]] .
$$
此处 strict 整性也可直接自证，而不另假设一个 period。
在 $h(T)=T+\sum_{n\ge2}a_nT^n$ 中递推解
$(1+h(T))^p-1=h(pT+T^p)$。
第 $n$ 项的未知系数为 $(p-p^n)a_n$；
已有低项给出的差模 $p$ 是
$\overline h(T)^p-\overline h(T^p)=0$，
所以待除的分子含 $p$。
由于 $1-p^{n-1}$ 为单位，$a_n$ 唯一且整。
首项一使逆级数也整，pullback 乘法 formal group 即给
$[p]_{\mathcal G}=pT+T^p$。
同一递推允许指定 derivative $a\in\mathbb Z_p$；
对 Teichmüller $a$，$a^p=a$，
比较 $h(aT)$ 与 $(1+h(T))^a-1$ 就给下面的 (1180.7)。
因此这里需要的 strict map、整性和 Teichmüller 作用均已在本篇自证。

它满足准确身份
$$
(1+h(T))^p=1+h(pT+T^p).
\tag{1180.6}
$$
这里的导数为 $1$，没有另保一个未求的 period unit。
因为 $a^p=a$ 对 $a\in\mu_{p-1}$ 成立，
同一唯一性还给
$$
[a]_{\mathcal G}(T)=aT,\qquad
1+h(aT)=(1+h(T))^a .
\tag{1180.7}
$$
特别 $1+h(-T)=(1+h(T))^{-1}$。

在原实际 PD ambient 中置
$$
\begin{gathered}
S_L=\mathcal O[z,\Gamma_n(g):n\ge1]^\wedge_p,\qquad
g=z^e-p,\quad\Gamma_n(g)=g^n/n!,\\
\psi|_{\mathcal O}=\sigma,\qquad \psi z=z^p,\qquad
\rho=\widetilde\gamma z^{p+1}.
\end{gathered}
\tag{1180.8}
$$
$\Gamma_n$ 在本文专指 divided powers，避免与原 $\gamma$
混用。原 specialization 是 $z\mapsto\varpi,\ g\mapsto0$，
绝不在 $\psi$ 或 divided Frobenius 之前令 $g=0$。

准确有
$$
\rho^{p-1}=-(g+p),\qquad
p\rho+\rho^p=-\rho g .
\tag{1180.9}
$$
所以
$$
f_\zeta(z):=1+h(\rho),\qquad
f_\zeta(z)^p=1+h(-\rho g).
\tag{1180.10}
$$
这些 series 在 $S_L$ 收敛。
例如 $g^n=n!\Gamma_n(g)$，故 $(g+p)^n\to0$ 于 $p$-adic
topology；(1180.9) 使 $\rho$ topologically nilpotent。
原 $h$ 的全部系数整，右式又在 $1+(g)$ 中。

在 $g=0$，$\rho$ 是 $\mathcal G$ 的非零 $p$-torsion point，
故 $f_\zeta(\varpi)$ 是非平凡 $p$ 次根。
其 leading 是
$$
f_\zeta(\varpi)-1
 =\widetilde\gamma\varpi^{p+1}
       +O(\varpi^{2p+2}).
$$
原所有非平凡 $p$ 次根是 $\zeta^a$，
其 leading 分别为 $a\gamma$，$a\in\mathbb F_p^\times$。
因此这个根准确是原来的 $\zeta$：
$$
\boxed{\quad f_\zeta(\varpi)=\zeta.\quad}
\tag{1180.11}
$$
这用实际 leading 固定根，而不是仅用
$\gamma^{p-1}=-1$ 猜 root phase。

同时 $\rho(\varpi)=h^{-1}(\zeta-1)\in K$，
且 $K=\mathbb Q_p(\rho(\varpi))$。
这也明确了下面 local units 的实际源域。

## 3. 正 $\mu_p$ 的完整第一层 $H^0$ 代表

Tsuji (2.7) 和 Lemma 2.12 将正根 $\zeta$ 送到
$$
\Xi_\zeta=\log_{\rm PD}(f_\zeta^p)
 \in H^0(S_1(1)).
\tag{1180.12}
$$
这里取的是 $1+(g)$ 上定义的 PD logarithm，
没有对不属于 $1+J$ 的 $f_\zeta$ 本身取 PD log。
本式也没有除以 $p$。

令 normalized formal logarithm 为
$$
\mathscr L_{\mathcal G}(T)
 =\log(1+h(T))=\sum_{n\ge1}\ell_nT^n .
$$
由 $\mathscr L_{\mathcal G}(pT+T^p)=p\mathscr L_{\mathcal G}(T)$
逐项比较，得到
$$
\ell_1=1,\qquad
\ell_n=0\ (2\le n<p),\qquad
\ell_p=\frac1{p(1-p^{p-1})}.
\tag{1180.13}
$$
另外，formal group 的 normalized invariant differential
$\mathscr L_{\mathcal G}'(T)dT$ 是整的：
它是
$\bigl(\partial_Y\mathcal G(T,Y)|_{Y=0}\bigr)^{-1}dT$，
分母在 $\mathbb Z_p[[T]]$ 中为单位。
所以
$$
n\ell_n\in\mathbb Z_p,\qquad
v_p(n!\ell_n)\ge v_p((n-1)!).
\tag{1180.14}
$$
由此 $n>p$ 的每一项在 PD ring 中都含 $p$，
并且全部尾项 $p$-收敛。
这支付完整尾部，不是只截 formal logarithm 到次数 $p$。

由 (1180.10)，
$$
\Xi_\zeta=\mathscr L_{\mathcal G}(-\rho g).
$$
$n=1$ 项是 $-\rho g$。
$n=p$ 项使用
$p!\ell_p\equiv-1\bmod p$、$p$ 奇数及
$\rho^p=-\rho(g+p)$，准确为
$$
p!\ell_p(-\rho)^p\Gamma_p(g)
 \equiv \rho^p\Gamma_p(g)
 \equiv-\rho g\Gamma_p(g)\pmod p .
$$
所以
$$
\boxed{\qquad
\Xi_\zeta
 =-\gamma z^{p+1}g(1+\Gamma_p(g))
 \quad\bmod pS_L.
\qquad}
\tag{1180.15}
$$
$\Gamma_p(g)$ 这一项必须保留。

也可在原复形中直接检查：
$N_z\Xi_\zeta=0\bmod p$，
$\varphi_1\Xi_\zeta=\Xi_\zeta\bmod p$，
其中
$\psi(g)/p\equiv-1-\Gamma_p(g)$。
因此 (1180.15) 是原 $H^0$ coefficient，
不是取值后丢失 normal 方向的近似。

### 3.1. Tate generator 没有额外归一

取 compatible cyclotomic roots $\varepsilon$，第一层为原 $\zeta$，
令 $t_{\rm per}=\log[\varepsilon]$。
同一正 Tate basis $e_\varepsilon$ 给
$e_\varepsilon/t_{\rm per}$ 这一原 de Rham generator，
其 Frobenius 为 $p^{-1}$。
若把根系换为 $\varepsilon^a$，
分子、分母同时乘 $a$，这个 generator 不变。

(1180.12) 的 comparison 正好把 $\Xi_\zeta$ 送到
$\zeta\in\mu_p$；所以其普通 tensor power
$\Xi_\zeta^{2j}$ 对应
$\zeta^{\otimes2j}$，没有再加一个阶乘、$p-1$ 或 period。
下面所有乘法都在这个相同的 Tate tensor identification 下进行。

## 4. 构造一个不依赖 Bernoulli 的实际局部测试类

取 $c\in\mathbb F_p$，用其 Teichmüller lift $\widetilde c\in\mathbb Z_p$，
在原 $S_L$ 上置
$$
U_c(z)=1+\widetilde c\,z^{N_j}.
\tag{1180.16}
$$
在 $L$ 中，
$$
\varpi^{N_j}
 =\widetilde\gamma^{-R_j}\rho(\varpi)^{R_j}.
$$
$R_j$ 是偶数且 $\widetilde\gamma^\sigma=-\widetilde\gamma$，
所以 $\widetilde\gamma^{R_j}\in\mathbb Z_p^\times$。
因而 $U_c(\varpi)$ 实际属于 $K$，
并在 $\zeta\mapsto\zeta^{-1}$ 下不变。

令 $\Delta=\operatorname{Gal}(K/\mathbb Q_p)$，
其 cyclotomic character 为 $\omega$。
定义真正的局部 cohomology 类
$$
\xi_c=
 \frac1{p-1}\operatorname{Cor}_{K/\mathbb Q_p}
 \left(\kappa(U_c(\varpi))\otimes\zeta^{\otimes2j}\right).
\tag{1180.17}
$$
这是一次 prime-to-$p$ 的 normalized corestriction，
不是未经证明的 field-norm identification。

restriction 准确给
$$
\operatorname{res}_K\xi_c
 =\kappa\left(e_{\omega^{-2j}}[U_c(\varpi)]\right)
       \otimes\zeta^{\otimes2j},
\quad
e_{\omega^{-2j}}
 =\frac1{p-1}\sum_{\delta\in\Delta}\omega(\delta)^{2j}\delta .
\tag{1180.18}
$$
方括号中是 $K^\times/K^{\times p}$ 的加法记法。

对 $\delta$ 的 Teichmüller 代表 $a$，
(1180.7) 给
$\delta\rho(\varpi)=a\rho(\varpi)$。
因此 $\log\delta U_c$ 的 leading 系数乘 $a^{R_j}=a^{-2j}$；
与 projector 中的 $a^{2j}$ 准确抵消。
由此
$$
\boxed{\quad \ell_{j,\zeta}(\xi_c)=c.\quad}
\tag{1180.19}
$$
普通 logarithm 的所有后项在实际 valuation 中更深：
$N_j/e=R_j/(p-1)>1/(p-1)$，
所以对 $n\ge2$ 有
$nN_j/e-v_p(n)>N_j/e$。
故这里没有被 $p$ 分母降回 leading 的 log 尾项。

特别 $c=1$ 给一条有明确 leading 的测试类。
它不来自一个可能局部化为零的 global Soulé class。

## 5. 同一 normalized trace 的两个 cone 槽

$L/F$ 的 tame Galois 群为 $\mu_e$，作用
$\tau_\xi(z)=\xi z$。
因为 $\sigma(\xi)=\xi^p$，
这个作用与 ambient $\psi$ 严格相容。
这里 $\psi(z)=z^p$ 是 PD ambient Frobenius；
没有在 ramified field $L$ 上假造 Frobenius 自同态。

原 $U_c$ 和 $\zeta$ 属于 $K$。
$FK/F$ 的 degree 是 $p-1$，$L/FK$ 的 degree 是 $p+1$。
因此 (1180.17) 在 $F$ 的 base change 可准确用
$$
\frac1e\operatorname{Cor}_{L/F}
 \bigl(\kappa(U_c)\otimes\zeta^{\otimes2j}\bigr)
\tag{1180.20}
$$
计算；上层的 $p+1$ 与 $e=(p-1)(p+1)$ 消成 (1180.17)
的原 $1/(p-1)$，没有遗漏倍数。

设 $u=z^e$，则原 trace 把
$S_L$ 的第零 $e$-block送到
$$
S_F=\mathcal O[u,\Gamma_n(u-p)]^\wedge_p .
$$
若 $a_0(u)$、$y_0(u)$ 分别是两个输入函数的第零 block，
normalized trace 的准确两槽是
$$
\frac1e\operatorname{Tr}
       \bigl(a(z)d\log z,\ y(z)\bigr)
 =\left(\frac{a_0(u)}e\,d\log u,\ y_0(u)\right).
\tag{1180.21}
$$
这是 $d\log u=e\,d\log z$ 的实际尺度。
不能把两个槽都机械乘同一个 $e$。
第二槽的 normalized trace 则正好保留第零 block。

同一 positive Kummer symbol 为
$$
C_\psi(U_c)
 =\left(d\log U_c,\ 
       L_c:=\frac1p\log\frac{U_c^p}{\psi U_c}\right).
$$
因为 $U_c^p/\psi U_c\in1+p\mathcal O[[z]]$，
$L_c$ 是 ordinary integral power series，
并且
$$
L_c=\widetilde c\,z^{N_j}+\text{更高的 }z\text{ 次数}.
\tag{1180.22}
$$
不能把其两个含 $1/p$ 的普通 log summands 分别当成整式；
这里使用的是整个比值的整 log。

原 external product 的 coefficient $\Xi_\zeta^{2j}$
是 degree zero。
所以产品第二槽准确为
$L_c\Xi_\zeta^{2j}$，没有本次需另加的 product homotopy。
同根 positive Kummer、positive $\mu_p$ 和 trace
均已固定，不能将该式另换成 inverse root。

## 6. 保全部 PD carry 的实际常数读取

由 (1180.15)，模 $p$ 的 second 槽是
$$
L_c\,
 \gamma^{2j}z^{2j(p+1)}
    g^{2j}(1+\Gamma_p(g))^{2j}.
$$
因为
$$
N_j+2j(p+1)=e,
$$
normalized trace 的最低 ordinary block 准确为
$$
c\gamma^{2j}\,u\,g^{2j}.
$$
所有其它 surviving ordinary blocks 含 $u^m$、$m\ge2$；
原 $\Gamma_p$ 因子只产生 normal degree 至少为 $p+2j$ 的项。
在完成 actual trace 之后，模 $p$ 才用 $u=g+p\equiv g$。
因此若 $(a\,d\log u,y)$ 是原 normalized cone cocycle，
就有
$$
\begin{gathered}
a,y\in J^{[r_j]},\\
y=c\gamma^{2j}g^{r_j}
       +\text{normal degree }>r_j,\qquad r_j=2j+1.
\end{gathered}
\tag{1180.23}
$$
这里 $g^{r_j}=r_j!\Gamma_{r_j}(g)$；
这个 $r_j!$ 后面会被真正的 divided-Frobenius reader 抵消，
不能预先省略。
(1180.23) 是原模 $p$ 复形中的 statement：以下把 $y$ 按其
normal 系数取为 $J_1^{[r_j]}$ 中的同一代表。它不是对尚含
$p g^{r_j-1}$ 的整 ordinary 表达式直接施 $p^{-r_j}\psi$；
合法 divided Frobenius 只施于这个实际 gauge 的过滤定义域。

本处可以直接写出 R1168 scalar 收缩。
由于 $a$ 的 normal degree 至少为 $r_j$，
$$
\varphi_{r_j-1}a=0\pmod p .
$$
cocycle closed 条件遂给 $a=N_u y$。
先减去合法的 coboundary $d_{\rm syn}y$，
得到
$$
(0,\varphi_{r_j}y).
$$
normal degree $>r_j$ 的全部项在此 divided Frobenius 后
都含 $p$；包括 degree $\ge p$ 的整个尾部。
其一般估值是
$n-r_j-v_p(n!)\ge1$，$n>r_j$，
这里 $r_j\le5<p-2$。
故
$$
\varphi_{r_j}y
 =(-1)^{r_j}\sigma(c\gamma^{2j})
        (1+\Gamma_p(g))^{r_j}\pmod p .
\tag{1180.24}
$$

令 $F$ 为 (1180.24) 右端，$F_0$ 为其 constant term。
$F-F_0$ 的各项都是 positive $\Gamma_{hp}$，$h\ge1$。
它们属于 $J^{[r_j]}$，并满足
$$
N_u(F-F_0)=0,\qquad
\varphi_{r_j}(F-F_0)=0\pmod p .
$$
再减 $d_{\rm syn}(F-F_0)$，准确得到同一个类的常数代表
$$
(0,F_0),\qquad
F_0=-\sigma(c\gamma^{2j})=-c\gamma^{2j}.
\tag{1180.25}
$$
最后一步使用
$c\in\mathbb F_p$ 和
$\sigma(\gamma^{2j})=(-\gamma)^{2j}=\gamma^{2j}$。
所有 $\Gamma_p$ carry 都先经过了原合法 gauge，
并没有在 source 中被直接设为零。

(1180.25) 是 **syntomic** 常数。
R1177 的原 positive Kummer/left twist/forward Frobenius
字典给 physical 一次坐标为其负值，故
$$
\boxed{\quad
\mathcal F_j(\xi_c)=c\gamma^{2j}.
\quad}
\tag{1180.26}
$$
由于 (1180.20) 是原 $\xi_c$ 的 base change，
且该输出属于 $\mathbb F_p$，
它就是原 $\mathbb Q_p$ 的 finite FL 值。
未分歧 quadratic restriction 在这里单射，
不产生一个额外的 $2$ 或 $\sigma$ 因子。

取 $c=1$，(1180.19)/(1180.26) 给一个实际非零测试类。
原 $H^1(\mathbb Q_p,\mathbb F_p(3))$ 和
$H^1(\mathbb Q_p,\mathbb F_p(5))$ 各一维，
且原 (1180.2) 是其完整 leading 同构。
因此线性性把这个实际计算延伸到整条局部线，
证明 (1180.3)。
这里被校准的是一条不依赖 Bernoulli 的非零 local class；
没有从两个都可能为零的数值倒除。

## 7. 所有根相位、bad 分支及原 profile 的直接后果

若将根换为同一个实际 $\zeta'=\zeta^a$，
$a\in\mathbb F_p^\times$，则
$$
\gamma'=a\gamma .
$$
对于固定的 descended class $\xi$，
其 Kummer unit 坐标同时乘 $a^{-2j}$，所以
$$
\ell_{j,\zeta'}(\xi)=a^{-2j}\ell_{j,\zeta}(\xi),
\qquad
(\gamma')^{2j}\ell_{j,\zeta'}(\xi)
 =\gamma^{2j}\ell_{j,\zeta}(\xi).
\tag{1180.27}
$$
这使 (1180.3) 与原 Tate frame 相容。
它没有把不同曲线的实际 Miller phase 设成相同。

在 R1153 的校准点存在的原范围内，
其 (1153.18) 已给
$U_\star=4\delta c_{g,\star}^2\beta_\star^2$。
与 (1180.3) 比较同一条完整局部线，得到
$$
4\delta c_{g,\star}^2\beta_\star^2=\gamma_\star^2.
\tag{1180.28}
$$
这是真正的原 polarization/Cartier/Miller 单位比较。
不需要 $B_{p-3}$ 非零来测定它，
也不从 $\gamma^{p-1}=-1$ 单独猜出它。

对任何已付的原 reference $E$，实际 phase
$a_E=\gamma_E/\gamma_\star$ 保持 R1153 原式。
因此原完整两槽的出口现在是
$$
\boxed{\begin{aligned}
\mathsf a_E(t)
 &=\gamma_E^2\,\widehat Q_{1,E}(t),\\
\mathsf b_E(t)
 &=\gamma_E^4\,\widehat Q_{2,E}(t)
       +\frac{8\delta^2}{11}s .
\end{aligned}}
\tag{1180.29}
$$
这里 $s$ 已是原实际 $\gamma_5$ 的 physical Frobenius 坐标；
没有再取一次 R1177 的负号。
$\gamma_E^2,\gamma_E^4\in\mathbb F_p^\times$，
并保留同一个实际根和全 profile 的原参数/标记。

R1153 (1153.23) 现直接给
$$
r=\frac23B_{p-3},\qquad
s=\frac{24}{5}B_{p-5}\quad\bmod p.
\tag{1180.30}
$$
这只是两个指定 cyclotomic classes 的局部读数，
对所有 $p>37$ 成立；它不要求这些 global classes
生成整个 global cohomology。
若要使用 R1148/R1152 的全局生成结论，
仍保持其原充分大 $p$ 范围。

更重要的是，(1180.3)/(1180.29) 在
$B_{p-3}=B_{p-5}=0$ 时仍完整成立。
R1152 §13.3 留下的 $\eta_\star$ 双坏分支至此被关闭：
不是由该处两个零等式推得 $\eta_\star=1$，
而是由本篇新造的 local 测试类证明。

## 8. 来源、精度与仍保留的输入

本篇新增并核读的 primary：

1. Jonathan Lubin and John Tate,
   *Formal Complex Multiplication in Local Fields*,
   Annals of Mathematics **81** (1965), 380–387，
   [原文扫描](https://math.bu.edu/people/jsweinst/AWS/Files/LubinTateFormalCMinLocalFields.pdf)，
   [另一原文扫描](https://people.math.rochester.edu/faculty/doug/otherpapers/lubin-tate.pdf)。
   Lemma 1（印刷381–382页）及 Theorem 1、式 (5)、(8)–(11)
   （印刷382–383页）给本文 strict $h$ 与各 $[a]$；
   两个 $p$-series 使用同一个 uniformizer $p$。
   本篇没有将换 uniformizer 时仅在未分歧扩张存在的
   非 strict 同构搬到这里。

2. Takeshi Tsuji,
   *On p-adic nearby cycles of log smooth families*,
   Bulletin de la SMF **128** (2000), 529–575，
   [正式 PDF](https://www.numdam.org/article/BSMF_2000__128_4_529_0.pdf)。
   式 (2.7)（印刷543页，含封面的 PDF第16页）给
   $\zeta\mapsto\log(\widetilde\zeta^{\,p})$；
   Proposition 2.11（印刷545页，PDF第18页）、
   Lemma 2.12（印刷546页，PDF第19页）
   固定 positive Kummer 与 positive $\mu_p$ 的兼容。
   原 product、base change 和 actual ramified PD 比较
   均沿 R1163/R1166 的既付同一模型。

本仓实际输入：

- R712、R978 与 R1162 的原严格 LT 参数、$z^e=p$ 和 honest PD normal；
- R1071 与 R1153 的原偶角色局部 filtration、实际 Miller phase；
- R1166 §9 的真实 tame trace，保两个 cone 槽不同的 $e$ 因子；
- R1168 的 scalar normal 收缩；本文 §6 还把本次所需两个 gauges 直接写出；
- R1177 的 actual Frobenius 一次负号。

本篇只读取原第一层两个局部直线的准确单位。
它不把 (1180.3) 外推成所有 $p^n$ 的相同常数，
不把一个 finite $\mathbb F_p$ 标签条件当作 whole $p$-disc 的唯一性，
也没有给任何尚未证明非零的中央 $z_{12}$、
global-subtracted polynomial 或 harmonic combination 赋单位值。
它完成的是一个此前独立保留、且在双坏分支不能由
global localization 检测的实际比较输入。
