# R696 — 原绝对根的共同 p² 除点域、显式 Hilbert 90 因子与线性高度界

日期：2026-11-15。**状态：已证明。** 主目标仍未完成。

R694 已把所有原相对根降到 F。本篇进一步证明：原 a_T 本身的全部
p 次根都属于 F₂=K₀(E[p²])，对所有非零 T 只生成同一个至多 p 次扩张。
由原根乘积得到无需辅助选择的 Hilbert 90 因子。

另一个实质改进是用固定倍点递推付清绝对根的统一高度。
原边界和由此成为唯一 p 位数域中的一条高度 O(p) 的迹；
它若非零，其 p 进赋值至多 O(p/log p)。这里没有由这个上界
预支原 j=0 的下界或中央非零。

## 1. 原数据与唯一使用的有限根

固定 R688/R694 的
$$
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad
K_0=\mathbf Q(\omega),\quad E:y^2=x^3+17,
$$
$$
F=K_0(E[p]),\quad G=\operatorname{Gal}(F/K_0)=\mathbf F_q^\times,
\quad H=\ker\operatorname{Norm},\quad F^H=K_0(\mu_p).
$$
保原 $a_T=\psi_\alpha(T)^{2s}/\psi_{p+1}(T)^{2s-1}$、
$r_{h,T}=\zeta_hP_{\zeta_h}(u_T)$、$G_T=T_g(u_T)$ 及原有限 jet 分支。
R694 已付
$$
r_{h,T}\in F,\quad r_{h,T}^{\,p}=a_T/a_{hT},\quad
r_{hk,T}=r_{h,T}h(r_{k,T}),\quad
G_T^d=-\prod_{h\in H}r_{h,T}.
\tag{1}
$$

对复周期格 $\Lambda$，仅为有限代数比较使用 R694 的
$$
\mathfrak k(z)=e^{-\eta_z z/2}\sigma(z),\qquad
a_T=\xi_T\mathfrak k(z_T)^{-p},\quad \xi_T\in\mu_{6p}.
\tag{2}
$$
其完整根单位包含 p 部分，未作删除。

令
$$
A=K_0(E[12p^2]),\qquad F_2=K_0(E[p^2]).
$$
R694 已证明 A/$K_0$ 阿贝尔，且任意两个非零 p 挠点的
$\mathfrak k$ 比属于 A。该断言含任意格代表的准周期相位。

## 2. 绝对 Klein 值以及全部 a_T 的根都在 F₂

定义固定的原倍点函数
$$
\Psi_2(P(z))=\frac{\sigma(2z)}{\sigma(z)^4}\in K_0(E).
\tag{3}
$$
这是原 sigma 归一的倍点除点函数；其符号由该定义固定。
在固定 Weierstrass 模型中它是 $2y$ 的固定正负号，
所以不会增加高度常数或新的角根。由于 $p>2$，$\Psi_2(T)\ne0$。

实线性准周期在整数倍下满足
$\eta_{2z}\,2z=4\eta_z z$，从而准确有
$$
\frac{\mathfrak k(2z_T)}{\mathfrak k(z_T)}
=\Psi_2(T)\mathfrak k(z_T)^3.
$$
左边由 R694 的同一 Siegel 比论证属于 A，右侧的 $\Psi_2(T)$ 在 F。
所以
$$
\mathfrak k(z_T)^3\in A.
$$
同时 (2) 给 $\mathfrak k(z_T)^p=\xi_T/a_T\in A$。
因 $6s-p=1$，
$$
\boxed{
\mathfrak k(z_T)
=\frac{(\mathfrak k(z_T)^3)^{2s}}{\mathfrak k(z_T)^p}
\in A.}
\tag{4}
$$
这一步不需要给一个周期的十二次根另选全局分支。

取任一 $\rho_T\in\mu_{6p^2}$ 满足 $\rho_T^p=\xi_T$。
则
$$
w_T=\rho_T/\mathfrak k(z_T)\in A,\qquad w_T^p=a_T.
\tag{5}
$$
$\mu_p\subset F$，故 (5) 的全部根也都在 A。

$\mathbf Z[\omega]/12$ 的单位群阶为 72：
模 4、模 3 的阶分别为 12、6。
因此
$$
[A:F_2]\mid[K_0(E[12]):K_0]\mid72.
$$
而 $F_2(w_T)/F_2$ 是次数为 1 或 p 的 Kummer 扩张，
又包含于 A/$F_2$；因 $p>101$，只能为 1。于是
$$
\boxed{\{w:w^p=a_T\}\subset F_2.}
\tag{6}
$$
这里下降的是全部代数根，不将某个新绝对根冒充原 $G_T$。
原相对根的具体分支仍按 (1) 保持。

## 3. 所有 T 共享至多一个 p 次扩张及一个实际字符

置
$$
W_T=F(w_T).
$$
$W_T$ 是 A 的含 $K_0$ 子域；A/$K_0$ 阿贝尔，所以
$W_T/K_0$ 也阿贝尔、Galois，且 $[W_T:F]\in\{1,p\}$。

任意 $g\in G$ 都可延拓到 A，并有 $g(a_T)=a_{gT}$。
A 的子域在其阿贝尔 Galois 群下稳定，所以
$g(W_T)=W_T=W_{gT}$。原 G 在 $E[p]\setminus0$ 上传递，故
$$
\boxed{W_T=W\text{ 与 }T\ne0\text{ 无关},\qquad [W:F]\le p.}
\tag{7}
$$
这个结论是全部原绝对根的共同域；它没有把它们称为相互独立的 p 次根。

在 $F^\times/F^{\times p}$ 中，$D=\langle[a_T]\rangle_{\mathbf F_p}$
为 G 稳定的零维或一维空间。
Kummer 配对的 G 等变性、W/$K_0$ 的阿贝尔性，以及 Weil pairing
给的 cyclotomic 字符 $\chi(g)=\operatorname{Norm}(g)$，准确给
$$
\boxed{[a_{gT}]=\chi(g)[a_T]\quad
\text{于 }F^\times/F^{\times p}.}
\tag{8}
$$
具体地，G 对 $\operatorname{Gal}(W/F)$ 的共轭为平凡；
配对值 $\mu_p$ 却乘 $\chi(g)$，故 D 必按同一字符变化。
这也在 $\chi|_H=1$ 上恢复 R694 的实际 $J=H$。

若 W/F 非平凡，$\operatorname{Gal}(W/K_0)$ 是阶 $p(q-1)$ 的阿贝尔群。
其唯一阶 $q-1$ 的 Hall 子群所固定的域记为 $B_p$，则
$$
[B_p:K_0]=p,\qquad W=FB_p,\qquad F\cap B_p=K_0.
\tag{9}
$$
这是由原 $a_T$ 确定的共同域。尚未辨认它是 CM p² 除点域的哪条 p 次方向。
由于 $(\mathbf Z[\omega]/p^2)^\times$ 的 p 部分为
$(\mathbf F_q,+)$，其至多有 p+1 条这样的方向；
本篇没有从方向有限推出任何跨 p 非零。

## 4. 原 p² 除点域在 p 处也是全局唯一位

沿 R663 的同一整 Lubin–Tate 坐标
$$
g(v)=-pv+v^q.
$$
对一个 primitive $p^2$ 挠点，其 $v_2$ 满足
$$
\boxed{\bigl(-pv_2+v_2^q\bigr)^{q-1}-p=0.}
\tag{10}
$$
(10) 是首一的 $q(q-1)$ 次多项式；
常数项为 $-p$，其余非首系数全被 p 整除。
所以它在 $K_p=\mathbf Q_p(\omega)$ 上 Eisenstein，
且其根生成完全分歧的 $q(q-1)$ 次扩张。

原 $u\leftrightarrow v$ 的整收敛逆在这个挠点仍适用，
故局部 p² 除点域包含上述根域。
另一方面，所有 CM 在 $K_0$ 定义，$E[p^2]$ 是自由秩一
$\mathbf Z[\omega]/p^2$ 模，给全局上界
$$
[F_2:K_0]\le|(\mathbf Z[\omega]/p^2)^\times|=q(q-1).
$$
局部下界与全局上界相等，因此
$$
\boxed{
[F_2:K_0]=q(q-1),\quad
\operatorname{Gal}(F_2/K_0)=(\mathbf Z[\omega]/p^2)^\times,
\quad p\text{ 在 }F_2/K_0\text{ 唯一且完全分歧}.}
\tag{11}
$$
不由收敛坐标声称 $v_2$ 本身在全局 $F_2$；
(10) 只用于完成域次数的下界，已足够推出 (11)。

W 及其任意含 $K_0$ 的子域因而也只有一个 p 位。
由于 p 在 $K_0/\mathbf Q$ 惰性，该 p 位的局部次数等于相应数域的
整个绝对次数。这个事实将在第8节准确消去高度比较中的全局次数损失。

## 5. 无辅助选择的原 Hilbert 90 因子

记
$$
U_T=\prod_{h\in H}r_{h,T}\in F^\times,\qquad
N_T=\operatorname{Norm}_{F/F^H}(a_T).
$$
由原完整 cocycle，
$$
h(U_T)=U_T/r_{h,T}^d,\qquad h(a_T)=a_T/r_{h,T}^p.
$$
由于 $d-p=1$，显式定义
$$
\boxed{
b_T=\frac{U_T}{a_T}=-\frac{G_T^d}{a_T}\in F^\times
}
\tag{12}
$$
就得到
$$
\boxed{
r_{h,T}=\frac{b_T}{h(b_T)},\qquad
b_T^p=\frac{a_T}{N_T},\qquad
\operatorname{Norm}_{F/F^H}(b_T)=N_T^{-1}.}
\tag{13}
$$
最后一式用 $\operatorname{Norm}_H(U_T)=1$。
这些等式保原偶除点负号；b 不再依赖 Hilbert 90 构造中的任意 c。

(12) 对整个 G 等变。确实，F 在 p 处只有一个位，
每个 $g\in G$ 在完成域中固定 $K_p$；原 $P_{\zeta_h}$ 的系数在 $K_p$，
且 G 与 H 交换，所以
$$
g(r_{h,T})=r_{h,gT},\qquad g(b_T)=b_{gT}.
\tag{14}
$$
这里不需要将 $\zeta_h$ 单独放进 F。

因而原指定迹
$$
C_{m,T}=\operatorname{Tr}_{F/F^H}(b_T^{-m}\phi_m(T))\in F^H
$$
满足 $C_{m,gT}=g(C_{m,T})$。
一个轨道的迹为零即迫全部轨道为零。
这是一个实际 Galois 传播证明，不是无依据地丢掉 R663 的其余 p−2 个轨道。

## 6. 在共同 W 中使用高度较小的同一根

取 $\widetilde H$ 为
$\operatorname{Gal}(W/F^H)$ 中唯一阶 d 的 Hall 子群。
它限制到 F 上准确为 H。对于 (5) 的任一根 w，
$$
c_h=w/h(w)
$$
是 $a_T/a_{hT}$ 的 p 次根，故由 R694 属于 F。
$c_h$ 和原 $r_{h,T}$ 都是同一 H 作用下的 cocycle；
它们的比值在 $\mu_p$ 中。H 固定 $\mu_p$，所以这个比值是
$H\to\mu_p$ 的群同态。因 $p\nmid d$，该同态平凡：
$$
\boxed{r_{h,T}=w/h(w)\quad(h\in\widetilde H).}
\tag{15}
$$
这一步付清了绝对根与原相对根之间的完整相位。

令
$$
E_W=W^{\widetilde H},\qquad
\mathcal T_{m,T}
=\operatorname{Tr}_{W/E_W}(w^{-m}\phi_m(T)),
\qquad m=34,72.
\tag{16}
$$
由 (11)，$E_W$ 只有一个 p 位。
$[E_W:K_0]=(p-1)[W:F]$，其绝对次数至多 $2p(p-1)$。
原完整边界式准确成为
$$
\boxed{
v_T^{d-m}\mathcal B_m(v_T^d)
=\frac{G_T^{-m}w^m}{d}\,\mathcal T_{m,T}.
}
\tag{17}
$$
没有减少任何 H 项或更改 $\phi_m$。

置 $L_T=\operatorname{Norm}_{W/E_W}(w)$，则
$$
b_T=w/L_T,\qquad
\mathcal T_{m,T}=L_T^{-m}C_{m,T}.
\tag{18}
$$
所以这与 (12) 的原 F 迹是同一个零判定；
采用 W 只是为了较小的绝对高度。
把 w 换成 $\epsilon w$、$\epsilon\in\mu_p$，
(16) 只乘 $\epsilon^{-m}$；(17) 和零判定完全不变。

## 7. 固定倍点递推给绝对根的统一高度

仍以 h 表示绝对对数 Weil 高度。
R684 的固定倍点证明给所有代数挠点一致的
$$
h(x(T))\le C_E,\qquad
h(y(T))\le C_y:=\frac{3C_E+\log17+\log2}{2}.
$$
由 (3)，可取
$$
C_2=C_y+\log2,\qquad
h(\Psi_2(T))\le C_2.
$$
定义固定常数
$$
\boxed{\mathscr H=C_2/3.}
\tag{19}
$$

设 $r=\operatorname{ord}_{(\mathbf Z/p)^\times}(2)$。
沿同一原 sigma 倍点关系反复使用
$$
\mathfrak k(2z)=\Psi_2(P(z))\,\mathfrak k(z)^4
$$
得到
$$
\mathfrak k(2^rz_T)
=\mathfrak k(z_T)^{4^r}
 \prod_{j=0}^{r-1}\Psi_2(2^jT)^{4^{r-1-j}}.
$$
因为 $2^rT=T$，左端与 $\mathfrak k(z_T)$ 只差 R694 已付的
$\mu_{2p}$ 准周期相位。所有量已由 (4) 证明代数。
根单位高度为零，所以
$$
(4^r-1)h(\mathfrak k(z_T))
\le\sum_{j=0}^{r-1}4^{r-1-j}h(\Psi_2(2^jT))
\le\frac{4^r-1}{3}C_2.
$$
约去正数 $4^r-1$，得对每个 p、T 一致的
$$
\boxed{
h(\mathfrak k(z_T))\le\mathscr H,\quad
h(w_T)\le\mathscr H,\quad
h(a_T)\le p\mathscr H,\quad
h(r_{h,T})\le2\mathscr H,\quad
h(G_T)\le2\mathscr H.
}
\tag{20}
$$
其中前两个高度相等；$a_T$ 的高度准确为
$p\,h(\mathfrak k(z_T))$。最后一项也可由
$G_T^d=-\prod_h r_{h,T}$ 直接读出。
不依赖 r 的大小、数域次数或某个有限 p 扫描。

这是原除点商在组合后的实际高度。
若分开对 $\psi_\alpha^{2s}$ 与 $\psi_{p+1}^{2s-1}$ 粗估，会丢失这个消去；
不能把那个较大的上界当成原 a_T 的必然增长率。

## 8. 原边界非零时的 O(p/log p) 赋值上界

原 $\phi_{34},\phi_{72}$ 为固定多项式。沿 R684，可固定
$C_{\phi,m}$ 使全部代数挠点有
$$
h(\phi_m(T))\le C_{\phi,m}.
$$
由 (16)、(20) 及完整 d 项求和，
$$
\boxed{
h(\mathcal T_{m,T})
\le d(m\mathscr H+C_{\phi,m})+\log d.
}
\tag{21}
$$
这是 O(p)，没有把单值次数界用于未确定的合成域。

若 $\mathcal T_{m,T}\ne0$，用
$h(\mathcal T)=h(\mathcal T^{-1})$。
在 $E_W$ 唯一的 p 位，其局部度等于整个绝对次数，
故绝对高度定义直接给
$$
v_p(\mathcal T_{m,T})\log p
\le h(\mathcal T_{m,T})
\tag{22}
$$
（本题该赋值为正；一般可在左边取正部）。
没有再乘 $[E_W:\mathbf Q]$。

原首挠点有 $v_p(u_T)=v_p(v_T)=1/(q-1)$。
原除点首项和 Bezout 指数给
$$
v_p(a_T)=-\frac{p}{q-1},\qquad
v_p(w)=-\frac1{q-1},\qquad v_p(G_T)=0.
$$
将这些**原**赋值代入 (17)，准确得到
$$
\boxed{
v_p(\mathcal T_{m,T})
=\frac1{p-1}+v_p(\mathcal B_m(v_T^d))
}
\tag{23}
$$
（零时双方同时为无穷）。

于是有一个明确二择：
$$
\boxed{
\mathcal B_m(v_T^d)=0
\quad\text{或}\quad
0\le v_p(\mathcal B_m(v_T^d))
\le
\frac{(p+1)(m\mathscr H+C_{\phi,m})+\log(p+1)}{\log p}
-\frac1{p-1}.
}
\tag{24}
$$
下界零来自原 $\mathcal B_m\in\mathcal O[[W]]$。
所有常数只依固定 E 和原固定 $\phi_m$；
(24) 对两个 m、所有首挠点和全部 H 轨道均适用。

由 (14)、(17)–(18)，若一个实际边界值为零，则全部值为零，
故仍准确等价于 R663 的完整 $Q\mid\mathcal B_m$。
这只是把所有原轨道的共同零判定放进一个明确的全局迹域；
并未省去其 Galois 关系的证明。

## 9. 对原中央问题的准确新门槛

(24) 给一个可直接用的接口：
若某个另已证明的原中央条件能对同一边界给
$v_p(\mathcal B_m(v_T^d))\ge c p$，其中 c>0 固定，
则在所有充分大的 p 上，该边界必为零。
更一般，只要下界超过 (24) 的显示右边，就必为零。
这由固定常数和 $\log p\to\infty$ 直接得到。

**目前没有证明原 $j_m=0$ 给这样的下界。**
也没有证明 (16) 的迹在无穷多个 p 非零。
不能把“非零时有上界”写成“所有 p 上非零”。

即使将来得到 $Q\mid\mathcal B_m$，它首先支付 R663 同一 Y 的闭边界；
原 X 下降仍保 $j_m=0$、$Q^{d-m}\mid\mathcal B_m$ 等较高条件。
本篇不为正阶 Hermite 余数、全部 p 幂边界或随 p 新造的来源
免费赋予 (21)–(24) 的相同高度界。

后续继续同一原连接、原中央、这个实际迹和完整高 Q 条件，
不重新引入已由 R694 排除的“稳定子最小”分支。

## 依赖

- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  同一整 LT 坐标、原完整边界、Q 及 Y/X 的区别。
- [R684](R684-original-division-orbit-phase-and-uniform-height.md)：
  固定曲线的绝对挠点高度证明、原 $\phi_m$ 的统一高度。
- [R688](R688-full-division-field-phase-cancellation-and-original-kummer-sums.md)：
  原全除点域、准确偶除点负号、完整轨道积和原边界和。
- [R691](R691-original-unit-kummer-field-and-stabilizer-trace-criterion.md)：
  原 cocycle、Kummer 配对与实际迹。
- [R694](R694-original-cm-kummer-descent-and-full-norm-one-trace.md)：
  原 Klein/Siegel 规范、完整相位、阿贝尔包含及全部相对根下降。
- 固定 sigma 倍点函数亦可核
  [NIST DLMF §23.10](https://dlmf.nist.gov/23.10)；
  本文始终用 (3) 的定义，未任意改其符号。

本篇为一般 p 的符号证明；没有辅助数值扫描，也没有可重算输出文件。
