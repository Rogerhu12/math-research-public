# R861 — Hasse 对齐的完整 Gaussian 运输与三个真实 Hurwitz 除 p 行

日期：2026-11-16。**状态：下列整规范、同矩阵运输和原零角左行的三个 whole Hurwitz 读取已证明。原指定组合的非零仍未证明。**

本注接[原零角左行](../notes/2026-11-16-r828-native-zero-angle-reader-and-central-newton-value.md)，把其真实 native 系数接到 [R856](R856-original-full-hurwitz-frobenius-recurrence-and-universal-divisibility.md)(39)。所有除 $p$ 都保准确的 Hasse 项；不会把物理最低阶七十八误用成 $j_{p+79}/p$ 已整。

## 1. 原 Hasse 多项式与可用的准确 Gaussian

保持原超奇异模型
$$
g_2=0,\qquad g_3=-4b,\qquad p=6s-1>211.
$$
为免与 R828 的顶轴标量 $H_p$ 混淆，本注把 Hasse 多项式写作
$\mathscr H_p$，并置
$$
\mathcal C_p=(L_2\mathscr H_p)|_{\rm CM}\in\mathcal O^\times.
\tag{1}
$$
这里使用完整特征零多项式的值，不只取其模 $p$ 剩余类。
事实上
$$
\mathscr H_p|_{\rm CM}=0,\qquad
\mathcal C_p=(p+1)\binom{3s-1}{2s-1}b^s.
\tag{2}
$$
因子 $p+1$ 在高位不能删掉。

令
$$
c_\sigma=[z^{p+1}]\log(\sigma/z),\qquad
\kappa=34c_\sigma+\Delta,\quad
a=p\kappa,\quad\Delta\in\mathcal O.
$$
R856 对原 $\sigma^2$ 取 $k=3$，给
$j_{p+3}(\sigma^2)\equiv12\mathcal C_p\bmod p$。
原首 Gaussian 的唯一非整项和
$(p+3)!/p\equiv-3!$ 则给
$j_{p+3}(\sigma^2)\equiv-12p c_\sigma\bmod p$。
因此
$$
\boxed{p c_\sigma\equiv-\mathcal C_p\pmod p.}
\tag{3}
$$
可合法取
$$
\boxed{
\Delta^\flat=-34(c_\sigma+\mathcal C_p/p)\in\mathcal O,
\qquad
\kappa^\flat=-34\mathcal C_p/p,\qquad
a^\flat=-34\mathcal C_p.
}
\tag{4}
$$
这是原 Gaussian 的整重标，不是给其首 residue 另赋值。
记
$$
\delta=\kappa^\flat-\kappa=(a^\flat-a)/p\in\mathcal O.
\tag{5}
$$

## 2. 完整 g、参考与原 M 同时运输

**规范范围。** 上节(1)–(5)的局部 Hasse 等式对显示的一般单位 $b$ 成立。
从本节起，$H_p,B$、原四中央 family 和整个 $M$ 均固定在 R821/R828 的
共同模型 $E_1:y^2=x^3+1$，即 $b=1$。本文没有把一般 $b$ 的局部式
直接当作未重标的 R828 矩阵。

原
$$
g=d\Theta^{17}e^{-\kappa w^s},\qquad
g_{\Theta,\circ}=g e^{-h_\Theta}
$$
准确变为
$$
g^\flat=g e^{-\delta w^s},\qquad
g_{\Theta,\circ}^\flat=g_{\Theta,\circ}e^{-\delta w^s}.
\tag{6}
$$
$h_\Theta$ 的四个 $t^{s-r}$ 系数未变，因为该重标从 $t^s$ 才开始。
所以
$$
\boxed{h_\Theta,\ H_p,\ B(w)\text{ 全部保持原值}.}
\tag{7}
$$
原低卷积同时改为
$$
\mathcal R_p^\flat=\mathcal R_p+\delta,\qquad
a^\flat=\frac{6(p-3)}{p+1}H_p+p\mathcal R_p^\flat.
\tag{8}
$$
不允许保持旧 $\mathcal R_p$ 而仅替换 $a$。

每个实际总 charge $Q_\Phi$ 的参考普通列须变为
$$
A_\Phi^\flat(w)=A_\Phi(w)e^{-Q_\Phi\delta w^s}.
\tag{9}
$$
在同一个原 $\Gamma$ 中，$w^s=p\epsilon$，故逐列准确有
$$
w^{13}A_\Phi^\flat e^{a^\flat Q_\Phi\epsilon}
=w^{13}A_\Phi e^{-pQ_\Phi\delta\epsilon}
                         e^{(a+p\delta)Q_\Phi\epsilon}
=w^{13}A_\Phi e^{aQ_\Phi\epsilon}.
\tag{10}
$$
所有指数在原有限目标中按实际需要截断。乘回相同
$e^{Q_\Phi H_pw^{s-4}B}$ 后，(10) 仍逐字成立。
因此
$$
\boxed{M_0^\flat=M_0,\qquad M_H^\flat=M_H}
\tag{11}
$$
在同一来源、同一目标的完整评价意义下成立。
三条十三行 carry、$P_{134}/U_0$ 的总四十和末端四次项全部被运输，
不是另作无成本列基变换。

[R342](R342-original-gaussian-recalibration-and-miller-adjoint-residue.md)§2 的全 Newton 重标（包括同一圆盘收敛及零质量）给：
使用下降阶乘 $(u)_h$，完整卷积给
$$
J_\nu^\flat(u)=(\kappa/\kappa^\flat)^uJ_\nu(u).
\tag{12}
$$
原来源质量为零，故 $J_\nu^{\flat\,\prime}(0)=J_\nu'(0)$。
这对同一个高轴计算 family 同样成立，因此其归一多项式满足
$$
\mathfrak F^\flat(H)=(a^\flat/a)\mathfrak F(H)\pmod{p^4}.
\tag{13}
$$
在同一个固定初值处，中央 Newton 比值 $C/D$ 完全不变。
若改用新自然初值 $-a^\flat/18$，须同时重新计算 $C,D$；
中央零假设仍使所得 Newton 值与实际 $H_p$ 相差 $p^3$。

原零角整左行在新规范中必须使用 $\Lambda_0(a^\flat)$。
它与 $\Lambda_0(a)$ 模 $p$ 相同，但高位不同：
$$
\Lambda_0(a^\flat)-\Lambda_0(a)\in p\Gamma^\vee.
\tag{14}
$$
因此后文给的是这条真实整 lift 的完整必要式；
不能把旧 lift 的高位留下后只删 Gaussian 项。

## 3. 原 canonical 列的 whole Hurwitz 行

暂记 $a^\flat$ 为 $a_*$。对每个原 canonical 列 $\Phi$，
总 charge $Q=40+n$、theta degree
$$
m=34Q
$$
均为真实原值。它是原 whole 截面 $\sigma^mR_\Phi$，
包含既有公共多项式和全部固定角因子。
保 $D_{\rm src}<p-40$，使全部 $m$ 在 $p$ 为单位；
此门在原大 $p$、$D_{\rm src}\asymp\sqrt p$ 范围内成立。

使用同一个实际整参数提升，记
$$
J_k(\Phi)=D_z^k\Phi(0).
$$
R856 给唯一整行
$$
\mathcal D_{m,p,k}(R_\Phi)
=\left.
\frac{J_{p+k}-\mathscr H_pJ_{k+1}-mk(L_2\mathscr H_p)J_{k-1}}p
\right|_{\rm CM}.
\tag{15}
$$
这里必须先在完整参数环中作这个指定整商，再特化；
所有原系数和热连接保持。由 (2)，在 CM 点准确有
$$
\boxed{
J_{p+k}=m\mathcal C_p\,k\,J_{k-1}
                +p\mathcal D_{m,p,k}(R_\Phi).
}
\tag{16}
$$
尤其 $k=79$ 的第一项通常非零。
最低物理阶七十八没有许可将它删掉。

定义
$$
n_j=j(p+1)+78,\qquad
k_j=(j-1)p+78+j,\qquad
U_j=\frac{n_j!}{p^j}\in\mathcal O^\times,
\quad0\le j\le3.
\tag{17}
$$
其中 $U_0=78!$；$p>211$ 保证 $v_p(n_j!)=j$。
因 $n_j=p+k_j$、$k_j-1=n_{j-1}$，重复 (16) 得到原三步整式
$$
J_{n_j}=A_j(m)J_{78}
 +p\sum_{\ell=1}^j A_{j,\ell}(m)
                         \mathcal D_{m,p,k_\ell}(R_\Phi),
\tag{18}
$$
$$
A_j(m)=(m\mathcal C_p)^j\prod_{h=1}^jk_h,\qquad
A_{j,\ell}(m)=(m\mathcal C_p)^{j-\ell}
                        \prod_{h=\ell+1}^jk_h.
\tag{19}
$$
空积为一。因此真正需要的是
$$
\boxed{k_1=79,\qquad k_2=p+80,\qquad k_3=2p+81,}
\tag{20}
$$
而不是三个自由高 jet。

## 4. 原左行的三个实际除 p 读取

仍令 $r(Q)=(Q-40)(Q-41)(Q-42)=\sum_{j=0}^3r_jQ^j$。
这里始终取完整物理矩阵 $M=M_{\rm act}^{\rm orig}$。
其实际列的来源可直接由
[R365](R365-whole-original-conductor-carrier-and-total-charge-connection.md)§1(1)–(2)、
[R657](R657-original-long-ordered-prefix-and-quadratic-contact-bound.md)(3)、(18)–(19)
及 [R821](R821-original-four-central-axes-and-complete-four-block-carries.md)§8(34)读出：
$$
\Phi_{n,k}=G_0\mathscr R^nq_n(t)t^k,\qquad
\mathscr R=\Theta^{17}d,\quad G_0=\mathscr R^{40}h_0,\quad
h_0=\frac{P_{134}t^{13}(t-1)^{15}h_7^{13}}{d^{17}}.
$$
保这些来源的原固定单位归一，由 $\Theta=x\sigma^2$ 得
$$
\Phi_{n,k}=\sigma^{34Q}R_\Phi,\qquad
R_\Phi=x^{17Q}d^Qh_0q_n(t)t^k,\quad Q=n+40.
$$
这也直接核实 whole 性：$d$ 的剩余指数为
$Q-17-\lfloor n/2\rfloor\ge0$；全 $t$ 多项式次数至多
$215+n+\lfloor9n/2\rfloor$，故代 $t=-x^{-3}$ 后最低 $x$ 次数至少
$35+17n-3n-3\lfloor9n/2\rfloor\ge0$，最高极阶至多 $34Q$。
原固定单位若在上述来源表达中单列，也始终留在 $\Phi$ 内，未规范为一。

R657(19)的同一个准确分解是
$$
G_0=c_*w^{13}U_0e^{40aw^s/p},\qquad
\mathscr R=ge^{aw^s/p}.
$$
所以 $M$ 的 $[\epsilon^jw^{13}]$ 行准确为
$$
p^j[w^{js+13}]\Phi
=\frac{J_{j(p+1)+78}(\Phi)}{(j(p+1)+78)!/p^j}.
$$
全部 $P_{134}$ 和 $c_*U_0$ 已在这个 $\Phi$ 中；
这里没有作用于 $U_0^{-1}M$ 或裸相对 $J$。
因此准确有
$$
\boxed{
\Lambda_0(a_*)M(\Phi)=
 \sum_{j=0}^3
 \frac{r_jj!}{a_*^jU_j}\,J_{n_j}(\Phi).
}
\tag{21}
$$
这是前注 regular 公式的同一个实际行，没有改变来源。

令
$$
v_{j,p}=\frac{r_jj!}{a_*^jU_j},\qquad
\mathscr P_p(Q)=
\sum_{j=0}^3
 \frac{r_j(-1)^jj!\,Q^j\prod_{h=1}^jk_h}{U_j}.
\tag{22}
$$
因为 $a_*=-34\mathcal C_p$，
(18) 中 $J_{78}$ 的系数正是 $\mathscr P_p(Q)$。
且
$$
U_j\equiv(-1)^jj!(78+j)!\pmod p,
$$
遂有
$$
\boxed{\mathscr P_p(Q)\equiv r(Q)/78!\pmod p.}
\tag{23}
$$

只有 $Q=40,41,42$ 的原列可能有非零 $J_{78}$；
其它原列的 $J_{78}$ 在特征零已经为零。
因此定义
$$
\rho_{Q,p}=
\begin{cases}
\mathscr P_p(Q)/p,&Q=40,41,42,\\
0,&\text{其它原 charge},
\end{cases}
\tag{24}
$$
是完全明确的整读取。第一种情形的整性由 (23) 支付，
不能将一般 $Q$ 的 $\mathscr P_p(Q)/p$ 都当整数。

再令
$$
\gamma_{\ell,p}(Q)
=\sum_{j=\ell}^3 v_{j,p}A_{j,\ell}(34Q)\in\mathcal O,
\qquad1\le\ell\le3.
\tag{25}
$$
把 (18) 代入 (21)，准确得到
$$
\boxed{
\frac{\Lambda_0(a_*)M(\Phi)}p
=\rho_{Q,p}J_{78}(\Phi)
+\sum_{\ell=1}^3\gamma_{\ell,p}(Q)
             \mathcal D_{34Q,p,k_\ell}(R_\Phi).
}
\tag{26}
$$
对任意同格 $X$，按其原列线性组合 (26) 即得完整公式。
一条来源若有多个实际 charge 项，仍按原给定组合求和，
不把它们另计为新列。

为核对绝对因子，模 $p$ 的三个系数为
$$
\boxed{
\begin{aligned}
\gamma_{1,p}(Q)&\equiv
-\frac{Q^2-123Q+5042}{a_*\,79!},\\
\gamma_{2,p}(Q)&\equiv
 \frac{Q-123}{a_*^2\,80!},\\
\gamma_{3,p}(Q)&\equiv
-\frac1{a_*^3\,81!}.
\end{aligned}}
\tag{27}
$$
特别最后一个系数为单位；这只说 (26) 是一个真实读取，
不预言该三个实际除 $p$ 行的组合非零。

原 $\bar P\in K_1$ 的三条常数行还逐个杀掉 charge
$40,41,42$ 的常数组合。因此 (26) 的 $J_{78}$ 项在首位对
这样的 $P$ 消失。但在后两位仍须保它以及同一 $R,S$，
不能据此把 $\rho_{Q,p}$ 从整式中删除。

## 5. 同一提升与完整热连接的边界

定义 (26) 的线性整行 $\mathcal H_{\rm nat}(X)$。
原实际提升
$$
M(P+pR+p^2S+p^3T)\in p^4\Gamma
$$
必要地满足
$$
\boxed{
\mathcal H_{\rm nat}(P)
+p\mathcal H_{\rm nat}(R)
+p^2\mathcal H_{\rm nat}(S)\in p^3\mathcal O.
}
\tag{28}
$$
这正是前注的同一零角必要式，现由三个真 whole Hurwitz 除 $p$
读取和明确低项计算。其它 normal、十三带、末短行及四次 carry
仍使用同一 $P,R,S,T$。

(15) 的三个 $\mathcal D$ 不能由模 $p$ 的通用 Frobenius 式恢复。
它们可按 R856(41) 的完整非齐次热递推计算，必须保
$\mathcal R=(L_2^2\mathscr H_p+g_2\mathscr H_p/12)/p$、
全部原初始 jet 和参数导数。

例如，实际奇序列的第一步已经是
$$
\boxed{
\mathcal D_{m,p,3}
=2m\nabla_m^\vee\mathcal D_{m,p,1}
+2m^2\mathcal R\,J_0
-\frac{m^2g_2(p+1)}{12}J_{p-1}.
}
\tag{29}
$$
它由 R855 的 $J_{p+3}$、$J_4$ 热递推逐项相减得到；
$L_2C_p=-g_2\mathscr H_p/12+p\mathcal R$
准确抵消其余低项。末项不能因在 CM 点暂时为零而在后续
$\nabla_m^\vee$ 中删除。

同样，原列的低物理消失不允许先冻结来源系数，
再把 (29) 反复当普通常系数微分。
更不能从四个固定算术来源的
$\mathcal D_{m_\nu,p,1}(R_\nu)=0$
给本注各 $m=34(40+n)$ 的三个 $\mathcal D$ 添中央零。

本次付清了原指定左行到真正整 Hurwitz 除 $p$ 信息的完整运输。
现在要判的是 (26)/(28) 在原同源高前缀、normal 和四个实际中央约束下的值；
最后系数为单位或 Gaussian 可对齐均不替代这个非零问题。
无新增数值运行。
