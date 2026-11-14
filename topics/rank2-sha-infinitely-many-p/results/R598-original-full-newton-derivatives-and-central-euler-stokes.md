# R598 — 两原完整 Newton 导数的中央 Euler 原函数与准确 Stokes 条件

日期：2026-11-14。**状态：已证明。**

本篇使用 R303/R402/R409 的两个原完整 Newton 函数，不只取其第一对角。
对每个原来源，完整中央导数准确等于一个明确一阶方程的唯一大圆盘解析解在原点的值。
因此原导数为零，等价于同一零初值 Euler 原函数的**实际中央投影**在去 Gaussian 后延拓到大圆盘。

中央投影在此必须保留。未投影的原函数始终有一条单位非中央 Stokes 行；两个未投影原函数甚至在原 wild Kummer 域上代数独立。这与两个中央投影可能同时延拓并不矛盾。
本篇没有把依赖 \(p\) 的旋转平均当成原全局列格中的免费操作。

## 1. 两个原来源与固定 Euler 原函数

取
\[
 p\equiv5\pmod6,\qquad p>71,\qquad d=p+1,
\]
并在 R409 的共同 \(E_1:y^2=x^3+1\) 模型中使用原
\[
 A_{34}=S_1,\qquad A_{72}=T_1,\qquad A_m=z^6+O(z^{12})
 \quad(m=34,72).
 \tag{1}
\]
R303/R402 的实际物理缩放、常数及 Gaussian 均已支付；
这里的完整导数是否为零，与各自固定物理曲线 \(E_{17},E_{24}\) 的原导数一致。

置
\[
 c=[z^d]\log(\sigma/z),\qquad
 \mathscr E=e^{cz^d},\qquad
 \alpha_m=mc,
\]
\[
 S=p^{-p/(p^2-1)},\qquad \rho=p^{-1/(2p)}.
 \tag{2}
\]
这里 \(v_p(c)=v_p(\alpha_m)=-1\)。R301/R402 的真实原分子给
\[
 G_m=A_m\mathscr E^{-m}\in\mathcal T_\rho
 :=\mathbf C_p\langle z/\rho\rangle,\qquad
 \|G_m\|_\rho\le\rho^6 .
 \tag{3}
\]
没有把单独的 \(\mathscr E\) 当作在整个 \(\rho\) 圆盘解析。

定义两个与 \(p\) 无关、零初值的原 Euler 原函数
\[
 \boxed{
 U_m(z)=\int_0^z\frac{A_m(t)}t\,dt
       =\sum_{k\ge1}\frac{[z^k]A_m}{k}z^k .
 }
 \tag{4}
\]
因 \(A_m(0)=0\)，这是原点正则的真实原函数，不含任意 log 项。
它在每个半径严格小于 \(S\) 的盘上收敛；除以整数 \(k\) 只增加次指数分母。

本篇不将 (4) 擅自加入任何既有 \(E_{D,9}\) 或十九角来源格。
这里先证明它们与原完整算术导数的准确关系。

## 2. 真中央投影与完整 Newton 函数

取实际 \(d\) 次单位根平均
\[
 \boxed{
 \Pi_0 f(z)=\frac1d\sum_{\zeta^d=1}f(\zeta z).
 }
 \tag{5}
\]
\(d\) 为 \(p\) 单位，所有 \(\zeta\) 的绝对值为一，
故 (5) 保 \(\mathcal T_\rho\) 的范数。
它选择原 \(z\) 次数为 \(d\) 倍数的部分，并满足
\(\Pi_0(\mathscr E^q f)=\mathscr E^q\Pi_0f\)。

写 \(X=z^d\)，令
\[
 G_{m,0}(X)=\Pi_0G_m=\sum_{h\ge1}g_{m,h}X^h .
\]
R303/R402 的同一个完整 Newton 半因子为
\[
 \boxed{
 J_{m,p}(u)=\sum_{h\ge1}g_{m,h}\alpha_m^{-h}(u)_h,
 \qquad
 j_m:=J'_{m,p}(0)
 =\sum_{h\ge1}(-1)^{h-1}(h-1)!\alpha_m^{-h}g_{m,h}.
 }
 \tag{6}
\]
原下降阶乘、全部 \(h\) 和真实 Gaussian 均在 (6) 中。
其收敛与有限严格尾证书由 R303/R402 已支付。

对同一个 (4) 定义
\[
 \boxed{H_m(X)=d\,\mathscr E^{-m}\Pi_0U_m.}
 \tag{7}
\]
由 \(zD_zU_m=A_m\)、\(zD_z=dX D_X\)，准确得到
\[
 \boxed{
 H_m'+\alpha_m H_m=G_{m,0}/X,\qquad H_m(0)=0.
 }
 \tag{8}
\]
特别这里的 \(d\) 因子不能漏掉。

## 3. 唯一大盘解析解与全部 Stokes 尾

设 \(V=\rho^d=p^{-d/(2p)}\)。
从 (3) 得
\[
 v_p(g_{m,h})+\frac{hd}{2p}\ge\frac3p,
\]
而左边随着 \(h\to\infty\) 趋于无穷。
定义
\[
 \boxed{
 \mathcal R_m(X)=\sum_{n\ge0}r_{m,n}X^n,\qquad
 r_{m,n}=\sum_{j\ge0}
 (-1)^j\frac{(n+j)!}{n!}\alpha_m^{-j-1}g_{m,n+j+1}.
 }
 \tag{9}
\]
每个显示阶乘比都是整数。
其第 \(j\) 项在 \(V\) 范数中的加权赋值至少为
\[
 (j+1)\frac{p-1}{2p}+\frac3p .
 \tag{10}
\]
故 \(j\) 尾一致收敛；固定 \(j\) 时，(3) 的 Tate 尾使
\(r_{m,n}V^n\to0\)。于是
\[
 \boxed{\mathcal R_m\in\mathbf C_p\langle X/V\rangle.}
 \tag{11}
\]
(9) 是完整尾和，不是只保第一个非零项。

直接相邻消项给
\[
 (n+1)r_{m,n+1}+\alpha_m r_{m,n}=g_{m,n+1}.
\]
因此 \(\mathcal R_m\) 是 (8) 方程的解析解，且由 \(n=0\) 的 (9)
\[
 \boxed{\mathcal R_m(0)=j_m.}
 \tag{12}
\]
所有同一方程的形式解之差为常数乘 \(e^{-\alpha_mX}\)，所以零初值解准确为
\[
 \boxed{
 H_m(X)=-j_m e^{-\alpha_mX}+\mathcal R_m(X).
 }
 \tag{13}
\]
等价地，在原 \(z\) 参数中
\[
 \boxed{
 d\,\Pi_0U_m(z)=\mathscr E(z)^m\mathcal R_m(z^d)-j_m.
 }
 \tag{14}
\]
这给完整中央导数一个准确的积分常数解释，而非只给必要首层。

## 4. 完整中央零与中央原函数延拓的等价

指数 \(e^{-\alpha_mX}\) 的准确半径为
\[
 S^d=p^{-p/(p-1)}.
\]
在该闭边界，其第 \(n\) 项的加权赋值为
\[
 -n-v_p(n!)+\frac{np}{p-1}
 =\frac{s_p(n)}{p-1},
\]
其中 \(s_p(n)\) 为 \(p\) 进数字和。
取 \(n=p^a\) 时恒为 \(1/(p-1)\)，故它不是闭 \(S^d\) 的 Tate 元。
特别 (11) 的更大盘解析项不能抵消一个非零的该指数项。

因此，对任意 \(S\le R\le\rho\)（半径取在 \(|\mathbf C_p^\times|\) 中），
\[
 \boxed{
 j_m=0
 \iff H_m\in\mathbf C_p\langle X/\rho^d\rangle
 \iff H_m\in\mathbf C_p\langle X/R^d\rangle
 \iff H_m\in\mathbf C_p\langle X/S^d\rangle.
 }
 \tag{15}
\]
若 \(j_m\ne0\)，则 \(H_m\) 准确半径为 \(S^d\)，且在该闭边界非 Tate。
若 \(j_m=0\)，则 \(H_m=\mathcal R_m\)，完整延拓由 (9) 给出。

(11) 也是这个一阶方程在任何所述大盘上的唯一解析解：
两个解析解的差若为非零常数乘指数，会与闭 \(S^d\) 非 Tate 矛盾。

由原完整 Selmer 桥，(15) 的失败——即对应中央零初值原函数
在闭 \(S\) 去 Gaussian 后非 Tate——足以给相应固定曲线的完整
\(\Sha[p^\infty]\) 有限。
要达到主目标，仍须对无穷多个不同 \(p\) 证明至少一个
\(H_{34},H_{72}\) 具有该性质。本篇尚未证明这一无穷性。

## 5. 未投影原函数始终有单位非中央行

中央投影不能从 (15) 中删除。
令
\[
 V_m=\mathscr E^{-m}U_m.
\]
整个未投影方程是
\[
 \boxed{
 (zD_z+\alpha_m d z^d)V_m=G_m.
 }
 \tag{16}
\]
在真正的 \(6\bmod d\) 部分，
\[
 P_6G_m=z^6\sum_{l\ge0}g_l z^{dl},\qquad g_0=1.
\]
这里 \(P_6\) 是 \(d\) 个角中的第六角，不是此前普通来源的纯 \(C\) 群投影。

写 \(x=6/d\)，R580 的同一完整递推给 Stokes 和
\[
 \mathfrak s_m
 =\sum_{l\ge0}(-1)^l(x)_{\overline l}\alpha_m^{-l}g_l .
 \tag{17}
\]
由 (3)，对 \(l\ge1\)
\[
 v_p(\alpha_m^{-l}g_l)\ge \frac{l(p-1)}{2p}>0,
\]
而所有 Pochhammer 因子整。
于是
\[
 \boxed{\mathfrak s_m\equiv1\pmod{\mathfrak m_{\mathbf C_p}}.}
 \tag{18}
\]
完整解为单位 \(\mathfrak s_m\) 乘
\[
 \frac1d z^6\sum_{h\ge0}
 \frac{(-\alpha_m)^hz^{dh}}{(6/d)_{\overline{h+1}}}
 \tag{19}
\]
加一个 \(\mathcal T_\rho\) 元。

为保整个尾，余项第 \(h\) 系数来自 (17) 的 \(l>h\) 尾；
约去前 \(h+1\) 个 Pochhammer 因子后，令 \(u=l-h\ge1\)，
每项在 \(\rho\) 范数中的加权赋值至少为
\[
 \frac{u(p-1)+6}{2p}.
\]
随 \(u\) 趋于无穷；固定 \(u\) 的系数则由 (3) 的 Tate 尾趋零。
因此这里确是整个大盘解析余项。

模型 (19) 在闭 \(S\) 非 Tate。
取 \(h=p^a\)，有
\[
 v_p((6/d)_{\overline{p^a+1}})=\frac{p^a-1}{p-1}.
\]
对 \(p^j\)、\(j\le a\)，等差列中准确有 \(p^{a-j}\) 项；
更高次整除要求 \(6\equiv\pm1\pmod d\)，本篇范围排除它。
所以模型的对应 \(S\) 加权赋值恒为
\[
 \frac1{p-1}+\frac{6p}{p^2-1}.
\]
由 (18)，完整解也非 Tate。

任意积分常数 \(C\) 只增加
\(-C e^{-\alpha_mz^d}\)，属于中央角，不能改变这条第六角。
故
\[
 \boxed{
 \mathscr E^{-m}(U_m-C)\notin\mathcal T_S
 \quad\text{对每个 }C\in\mathbf C_p.
 }
 \tag{20}
\]
它们的准确 \(z\) 半径均为 \(S\)，不论原 \(j_m\) 是否为零。
(20) 与 (15) 是不同的、兼容的命题。

## 6. 两个未投影原函数在同一 wild 域上独立

保持 R588 已支付的实际
\[
 K_R=F_R(\mathscr E),\qquad
 F_R=\operatorname{Frac}\mathcal T_R,\qquad S\le R\le\rho.
\]
这是常数域为 \(\mathbf C_p\) 的 degree \(p\) Kummer 扩张，
其 Galois 群按 \(\mathscr E\mapsto\zeta\mathscr E\) 作用；
原完整 \(A_{34},A_{72}\) 属于 \(K_R\)。

原两个被积函数
\[
 A_{34}/z=\mathscr E^{34}(G_{34}/z),\qquad
 A_{72}/z=\mathscr E^{72}(G_{72}/z)
\]
分别在特征 \(34,72\bmod p\) 中。
\(p>71\) 的惰性素数实际至少为 83，故两特征非零且互异。

若它们的一个非零常数组合在 \(K_R\) 有原函数，
取一个非零系数对应的真实 \(\mu_p\) 特征投影，就给
\(\mathscr E^m u\)、\(u\in F_R\) 的原函数。
其方程为
\[
 u'+mcdz^{d-1}u=G_m/z.
\]
右边在 \(\mathcal T_R\) 中，且原点正则。
R588 的闭盘 no-pole 引理迫 \(u\in\mathcal T_R\)。
但常数域给
\(u=\mathscr E^{-m}(U_m-C)\)，与 (20) 矛盾。
若先在有限代数扩张中有原函数，取迹再除以扩张次数同样矛盾。

R575/R588 已用的加性积分引理于是得到
\[
 \boxed{U_{34},U_{72}\text{ 在每个 }K_R\text{ 上代数独立。}}
 \tag{21}
\]
因此任何真正含这些原函数的原多项式——其 \(S,T\) 系数按实际函数先收集——
乘任意整数 Gaussian 幂，也准确半径 \(S\) 且闭 \(S\) 非 Tate。
上界由 (21) 排除它属于 \(K_S\)，下界由每个 \(<S\) 的真实收敛给出。
域中的特征投影含 \(1/p\)；这不是对整数来源格的免费操作。

## 7. 原算术输入与尚需保持的投影范围

本篇把两条完整原导数零，准确转成两个
\[
 d\,\mathscr E^{-m}\Pi_0U_m\in\mathcal T_\rho
 \qquad(m=34,72)
\]
的解析条件。完整 Newton 尾已经在 (9)、(13) 中，未退化成
R595/R596 的首对角条件。

但 (5) 是随 \(p\) 变化的实际 \(z\) 旋转平均。
除原 \(\mu_6\) 子群外，这些旋转没有被证明是原 CM 同源、原
Schwartz 来源操作或十九角/九来源格中的同预算列。
把 (15) 用于真实有限前缀时，必须保 (5) 的全部角向选择及
原 Gaussian，另证它在该前缀上的作用。

未投影的单位第六角 (18) 被 \(\Pi_0\) 准确杀掉。
因此 (20)、(21) 不能反过来宣称 \(j_{34}\) 或 \(j_{72}\) 非零。
原完整中央到实际投影的桥已付；从这两个投影的解析条件得到
原饱和格的额外限制，仍需继续。

## 依赖

- [R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
  [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)：
  两个原完整 Newton 函数、实际 Gaussian/物理缩放、原 Selmer 比较及全部尾。
- [R409](R409-two-actual-sources-shared-first-diagonal-recurrence.md)：
  两条共同 \(E_1\) 来源的准确身份。
- [R580](R580-same-charge-primitive-towers-and-unit-noncentral-stokes-matrix.md)：
  原全 Stokes 递推；本篇显示中央和第六角各自的完整尾。
- [R588](R588-actual-wild-kummer-disc-and-nonlinear-primitive-radius.md)、
  [R575](R575-fixed-primitive-towers-and-complete-ordinary-dirac-defects.md)：
  实际 wild 域、no-pole、常数域及加性积分论证。

本篇为全参数证明，没有新增素数扫描。
