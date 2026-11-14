# R298 — 原 j=0 中央常数的精确 Kronecker 计算与完整周期换算

日期：2026-11-13。**状态：以下固定整数、全权平方归一、正实周期和 CM 生成周期之间的换算，以及用于支付该整数的原四十八项 Kronecker resolvent 已证明。没有用高精度认数替代恒等式。尚未得到无穷多个 p 的原中央导数非零；主目标未完成。**

本篇接 R290 的原 Schwartz 和 R297 已识别的原截面，消去其最后一个未指定的非零常数。结论是
$$
\boxed{\kappa_0=48940416=2^7\,3^3\,7^2\,17^2.}
\tag{1}
$$
所有周期都对应不变微分 $dz=dx/(2y)$；下面同时保留正实周期和 $\mathcal O_K$ 生成周期，不能只替换权因子而漏掉中央常数的变化。

## 1. 原来源和要支付的唯一常数

记
$$
K=\mathbf Q(\delta),\quad \delta=\sqrt{-3},\quad
\omega={-1+\delta\over2},\qquad
E_b:y^2=x^3+b.
$$
R297 识别的、首项为 $z^6$ 的实际来源为
$$
\begin{aligned}
S_b(z)=\sigma(z)^{34}x(z)^2\big(&x(z)^{12}
-\tfrac{53b}{7}x(z)^9-\tfrac{12b^2}{7}x(z)^6\\
&-\tfrac{80b^3}{7}x(z)^3-\tfrac{128b^4}{7}\big),
\qquad S_b(z)=z^6+O(z^{12}).
\end{aligned}
\tag{2}
$$
本篇目标曲线始终是 $b=17$。设 $\Omega>0$ 为 $E_{17}$ 的正实 primitive period，并置
$$
s=(1-\omega)^{-1}={3+\delta\over6},\qquad
\Lambda=\mathbf Z+s\mathbf Z=s\mathcal O_K,
\qquad \Gamma_{17}=\Omega\Lambda.
\tag{3}
$$
这是 R290 中实际 theta 格的同一尺度。写
$$
S_{17}(z)=\sum_{m\ge0}s_mz^m,\qquad s_6=1,
\qquad s_m=0\quad(6\nmid m).
\tag{4}
$$
这些是普通 Taylor 系数，不是除幂系数。

R290 的真正 Hermite 生成函数满足
$$
\mathcal B(T)=C\,S_{17}(\Omega hT),\qquad
h={\sqrt{51\sqrt3}\over204\pi i},
\tag{5}
$$
其中 $C$ 为固定非零实数。实性来自原有限向量、$S_{17}$ 的实系数和 $h^6\in\mathbf R^\times$；非零性来自原 Fourier 向量非零及 R297 的实际一维识别。
令 $C_{17}^{(0)}>0$ 为 R290 (35) 的全部已付正常数，则
$$
\kappa_0={C_{17}^{(0)}C^2\over\Omega}>0.
\tag{6}
$$
将 $b_m=Cm!(\Omega h)^m s_m$ 代入 R290 的全权平方公式，并用
$$
{2\pi\over\sqrt3}\,4\pi h^2=-{1\over102},
$$
得到对每个 $m\ge0$、$6\mid m$ 的准确身份
$$
\boxed{
\mathcal E_m^{\mathbf R}:=
{(2\pi/\sqrt3)^m L(\psi_{17}^{2m+1},m+1)
 \over m!\Omega^{2m+1}}
=\kappa_0\,102^{-m}s_m^2.}
\tag{7}
$$
因此只须准确支付 $m=6$ 的一个原值，便能确定整个原全权族的同一个常数。不能逐权重选归一。

## 2. CM 生成周期的全部变化

实际 $\mathcal O_K$ 生成周期是
$$
\Omega_{\rm CM}=\Omega s.
$$
直接有
$$
s^2=-\omega^2/3,\qquad s^6=-1/27,
\qquad s^{2m}=3^{-m}\quad(6\mid m).
\tag{8}
$$
所以 (7) 换成这个生成周期后，完整公式是
$$
\boxed{
\mathcal E_m^{\rm CM}:=
{(2\pi/\sqrt3)^m L(\psi_{17}^{2m+1},m+1)
 \over m!\Omega_{\rm CM}^{2m+1}}
={\kappa_0\over s}\,34^{-m}s_m^2
=(1-\omega)\kappa_0\,34^{-m}s_m^2.}
\tag{9}
$$
其中中央常数也乘 $s^{-1}$。以下有限计算使用 (9)，最后再由 (8) 返回正实周期。

## 3. 直接与 Hecke L 值相接的 Kronecker 系数

先在基曲线 $E_1:y^2=x^3+1$ 上计算。记其正实周期为 $\Omega_1$，CM 生成周期为 $\varpi=\Omega_1s$，period lattice 为 $\Gamma_1=\varpi\mathcal O_K$。令
$$
A={\operatorname{area}(\mathbf C/\Gamma_1)\over\pi}
={\sqrt3\over2\pi}|\varpi|^2.
$$
由于此格有三次 CM 自同构，reduced theta 恰为规范 $\sigma$，没有额外的 holomorphic 二次指数。对 $P\in\mathbf C/\Gamma_1$ 的一个代表，定义
$$
\Theta_P(z,w)=
e^{-\bar P w/A}\,
{\sigma(P+z+w)\over\sigma(P+z)\sigma(w)},
\qquad c_{66}(P)=[z^6w^6]\Theta_P(z,w).
\tag{10}
$$
表达式及系数与代表的选择无关。

Bannai–Kobayashi 的已发表 Kronecker 展开（Theorem 1.17）在本指标准确给
$$
c_{66}(P)={e_{6,7}^*(P,0;\Gamma_1)\over6!A^6}.
\tag{11}
$$
此处正号为 $(-1)^{6+7-1}=1$。$e_{6,7}^*$ 是
$\sum_{\gamma\in\Gamma_1}\overline{P+\gamma}^{6}/(P+\gamma)^7$
的 Eisenstein–Kronecker 解析延拓。下面的有限陪集分解先在绝对收敛区间成立，再继续到所需值；没有对一个条件收敛和作未经支付的重排。

取完整导子生成元
$$
f_1=2\delta,\qquad f=17f_1=34\delta.
$$
对素于 $f$ 的 $a\in\mathcal O_K$，R290 已付的有限角色为
$$
\varepsilon(a)=\varepsilon_1(a)\chi_{17}(a),
\quad\varepsilon_1(a)=\chi_2(a)\chi_3(a)\in\mu_6,
\quad\chi_{17}(a)=(a\bmod17)^{48},
\quad\psi_{17}((a))=a\varepsilon(a)^{-1}.
\tag{12}
$$
这里 $(a\bmod17)^{48}$ 取其 $\mu_6$ 提升；模 $17$ 约化不是复共轭。
下文的 $\bar a$、$\bar\gamma$ 则始终表示 $K/\mathbf Q$ 的复共轭。
因此，使用 $L(\psi_{17}^{13},7)$ 的实性，或等价地对理想取共轭，其原格和可写成
$$
L(\psi_{17}^{13},7)
={1\over6}\sum_{a\ne0,\ (a,f)=1}^{*}
 \varepsilon(a){\bar a^6\over a^7}.
\tag{13}
$$
星号表示由相应 Eisenstein–Kronecker 级数解析延拓，而不是额外删项。

设 $\theta=17^{1/6}>0$。$E_1\to E_{17}$ 的同构
$(X,Y)\mapsto(\theta^2X,\theta^3Y)$ 将微分乘 $\theta^{-1}$，故
$\Omega_{\rm CM}=\varpi/\theta$。又 $\psi_{17}=\psi_1\rho$、$\rho^6=1$，所以 $\psi_{17}^{13}=\psi_1^{13}\rho$，(13) 的有限角色仍正是 (12)。将 (13) 按 $a\bmod f$ 分解，并应用 (11)，得到
$$
\mathcal E_6^{\rm CM}
=\theta^{13}{\bar f^6\over6f^7}
 \sum_{a\in(\mathcal O_K/f)^\times}
 \varepsilon(a)c_{66}(\varpi a/f).
\tag{14}
$$
这里的 $A^{-6}$、$6!$、单位群的 $1/6$ 和 $\theta^{13}$ 均由 (11)–(13) 保留下来。

## 4. 先完整支付二、三处的六个平移

设
$$
P=\varpi/17\in E_1[17],\qquad
Q=\varpi/(2\delta)\in E_1[2\delta].
$$
由正实 period 的实际分支，
$$
Q=(2\omega,3),\qquad
\xi(Q):=\zeta(Q)-\bar Q/A=-\omega^2.
\tag{15}
$$
可不靠数值核定它：$2Q$ 等于正实 period 的 $2/3$，是 $(0,1)$；$\delta Q=\Omega_1s/2$ 的横坐标为 $-\omega$。点 $(2\omega,3)$ 满足这两个等式。它也等于 $(-\omega,0)+(0,-1)$；后两点的 reduced $\zeta$ 值都为零，$\zeta$ 加法式即给 (15)。

全部 primitive $2\delta$ 挠点是 $(2\omega^j,\pm3)$，其 reduced $\zeta$ 值为 $\mp\omega^{-j}$。这一步使二、三处的平移完全留在 $K$ 中。

中国剩余分解中令
$$
a\equiv f_1c\pmod{17},\qquad a\equiv u\pmod{f_1},
\quad c\in\mathbf F_{289}^\times,\quad u\in\mu_6.
$$
因为 $17\equiv-1\pmod{f_1}$，准确有
$$
\varpi a/f=[c]P-[u]Q,
\qquad
\varepsilon(a)=-u\chi_{17}(c).
\tag{16}
$$
最后的负号来自 $\chi_{17}(2\delta)=-1$。此外
$$
c_{66}([u]R)=u^{-13}c_{66}(R)=u^{-1}c_{66}(R),
\qquad \chi_{17}(u)=1\quad(u\in\mu_6).
$$
因此在 (14) 中先作 $c\mapsto u^{-1}c$，六个 $u$ 的和恰好付掉外面的 $1/6$，得到
$$
\boxed{
\mathcal E_6^{\rm CM}
=-{\theta^{13}\over34\delta}\,
\mathscr R(P),\qquad
\mathscr R(P)=\sum_{c\in\mathbf F_{289}^\times}
 \chi_{17}(c)c_{66}([c]P-Q).}
\tag{17}
$$
用了 $\bar f^6/f^7=1/f$。这是真正完整的原 ray 和；没有用只含十七处的局部 resolvent 代替它。

## 5. 所需 Kronecker 系数只有十四项

在 $E_1$ 上写 $r=\xi(R)$、$x=x(R)$、$y=y(R)$。由 (10) 得到的所需系数是以下固定有理式：
$$
\begin{aligned}
H(r,x,y):=c_{66}(R)=-{1\over3600}\big[&
5x^2yr^6+(18x+30x^4)r^5+(15y+75x^3y)r^4\\
&+(80x^2+100x^5)r^3+(30xy+75x^4y)r^2\\
&+(4+30x^3+30x^6)r+3x^2y+5x^5y\big].
\end{aligned}
\tag{18}
$$
**推导。** 使用
$$
Dr=-x,\qquad Dx=2y,\qquad Dy=3x^2,\qquad y^2=x^3+1,
$$
以及 $\log(\sigma(w)/w)=w^6/210+O(w^{12})$。若
$$
\exp\left(rw+\sum_{j=2}^7{D^{j-2}(-x)\over j!}w^j
-{w^6\over210}\right)=\sum E_jw^j+O(w^8),
$$
则因 (10) 外面有 $w^{-1}$，
$$
H=D^6E_7/6!.
$$
按 $E_n=n^{-1}\sum_{j=1}^n ja_jE_{n-j}$ 展开，并约去 $y^2-x^3-1$，正好得到 (18)。这也单独支付了原 $\sigma(w)$ 的六阶项，不能删掉它。

## 6. 十七挠点的 reduced ζ 全部代数化

令 $\Psi_{17}(x)$ 为 $E_1$ 的标准奇除法多项式，定义首一多项式 $P_{48}$：
$$
\Psi_{17}(x)=17P_{48}(x^3),\qquad \deg P_{48}=48.
\tag{19}
$$
其系数由通常的除法多项式递归生成；完整系数放在本篇 JSON，而不在正文堆列大整数。

对非零十七挠点 $P$，设 $t=x(P)^3$。由
$$
\Psi_{17}(x(z))={\sigma(17z)\over\sigma(z)^{289}}
$$
在 $z=P$ 的对数导数常数项，得到准确的 reduced 值
$$
\xi(P)=-{1\over289}
 \left(y{\Psi_{17,xx}\over\Psi_{17,x}}+{3x^2\over2y}\right)
={y\over x}\,a(t),
$$
$$
\boxed{
a(t)=-{1\over289}
 \left(2+3t{P_{48}''(t)\over P_{48}'(t)}
          +{3t\over2(t+1)}\right).}
\tag{20}
$$
证明中，若 $17P=\lambda\in\Gamma_1$，则 $17\zeta(17z)$ 的常数项是 $17\eta_\lambda$，而 $\eta_\lambda=\bar\lambda/A$；所以产生的恰是 $-289\xi(P)$，没有留下未指定的 quasi-period。

为了计算 (17)，先付六次单位轨道。令
$$
R(t)=\sum_{u\in\mu_6}H\bigl(\xi([u]P-Q),x([u]P-Q),y([u]P-Q)\bigr).
\tag{21}
$$
它是 $K(t)$ 中的有理函数。实际计算只用下面的加法公式，不需解出任何挠点：
$$
\ell={y+3\over x-2\omega},\quad
x_R=\ell^2-x-2\omega,\quad
y_R=-y+\ell(x-x_R),\quad
r_R={y\over x}a(t)+\omega^2+\ell.
\tag{22}
$$
把 (18) 的 $(r,x,y)$ 换成 $(r_R,x_R,y_R)$，在
$$
K(t)[x,y]/(x^3-t,\ y^2-t-1)
$$
上取六次迹，就是 (21)。证书保存了其分子对一个形式变量 $a$、$t$ 的两列（$1,\delta$ 列），共同分母可取 $\{t(t-8)\}^{13}$；再代入 (20)，全部在 $K[t]/(P_{48})$ 中读取。所有出现的分母均由精确 gcd 检查可逆。

## 7. 真 CM7 轨道与精确六次方恒等式

选择实际 CM 整数
$$
\gamma=2-\omega={5-\delta\over2},\qquad N\gamma=7.
$$
它在 $\mathbf F_{289}^\times$ 中的阶准确为 $288$，模 $\mu_6$ 的阶为 $48$，且
$$
\chi_{17}(\gamma)=\gamma^{48}=-\omega^2=:\lambda.
\tag{23}
$$
因此 (17) 的 288 项由 (21) 完整压成 48 项。

令
$$
c=-{2+6\delta\over7},\qquad
U(t)=t^2+(12-28c)t+7c^2-24c.
$$
真实 $[\gamma]$ 对 Weber 坐标的作用为
$$
\Phi(t)=t\,{U(t)^3\over\gamma^6(t+c)^6}.
\tag{24}
$$
它可由真实七次除法式
$\sigma(\gamma z)/\sigma(z)^7=\gamma(x^3+c)$
求两阶对数导数得到，或由 CM 群法得到。这里不是任取一个同阶的有限域自同构。

定义原加权轨道和
$$
\mathscr R(t)=\sum_{j=0}^{47}\lambda^j
 R\bigl(\Phi^{\circ j}(t)\bigr)
\quad\text{in }K[t]/(P_{48}).
\tag{25}
$$
它正是 (17) 的 $\mathscr R(P)$ 在 $t=x(P)^3$ 的值。精确多项式运算给出
$$
\boxed{
\mathscr R(\Phi(t))=\lambda^{-1}\mathscr R(t),\qquad
\mathscr R(t)^6={15876^6\over17^{31}}.}
\tag{26}
$$

这是一条在原除法商环中的恒等式，所以适用于每一个非零十七挠点，不需要先猜中它的复嵌入。证书从标准除法递归开始，逐次执行 (18)、(20)–(25)，最后把六次方除以原 $P_{48}$；余式准确为 (26) 的有理常数、$\delta$ 列为零。所用全过程只含有理数及 $\delta^2=-3$，没有小数或数值重构。

为便于检查算法，递归的具体规范是 $\Psi_{2n}=2yF_{2n}$、$\Psi_{2n+1}=F_{2n+1}$：
$$
F_1=F_2=1,\quad F_3=3x^4+12x,\quad
F_4=2(x^6+20x^3-8),
$$
$$
F_{2n}=F_n(F_{n+2}F_{n-1}^2-F_{n-2}F_{n+1}^2),
$$
$$
F_{2n+1}=
\begin{cases}
16(x^3+1)^2F_{n+2}F_n^3-F_{n-1}F_{n+1}^3,&n\text{ 偶},\\
F_{n+2}F_n^3-16(x^3+1)^2F_{n-1}F_{n+1}^3,&n\text{ 奇}.
\end{cases}
\tag{27}
$$
这些是普通除法递归的约去 $2y$ 版本。$P_{48}=F_{17}/17$，在 $t=x^3$ 中读取。脚本同时核实 $P_{48}$ 可分、(24) 保持它，以及 (23) 的原有限剩余阶。

## 8. 用正实平方选择唯一常数

由 (9)、$s_6=1$ 和 (17)，
$$
{\kappa_0\over s\,34^6}
=-{17^{13/6}\over34\delta}\mathscr R(P).
\tag{28}
$$
取六次方，用 $s^6=-1/27$、$\delta^6=-27$ 及 (26)，得到
$$
\kappa_0^6
={34^{30}17^{13}\over3^6}\,
 {15876^6\over17^{31}}
=\bigl(2^7 3^3 7^2 17^2\bigr)^6.
\tag{29}
$$
R290 的原实平方及 (6) 已给出 $\kappa_0>0$。因此没有剩余的六次单位歧义，(29) 唯一推出 (1)。

综上，最终的两种完整规范分别是
$$
\boxed{
{(2\pi/\sqrt3)^m L(\psi_{17}^{2m+1},m+1)
 \over m!\Omega^{2m+1}}
=48940416\cdot102^{-m}s_m^2,
\qquad 6\mid m,}
\tag{30}
$$
$$
\boxed{
{(2\pi/\sqrt3)^m L(\psi_{17}^{2m+1},m+1)
 \over m!\Omega_{\rm CM}^{2m+1}}
=(1-\omega)48940416\cdot34^{-m}s_m^2,
\qquad 6\mid m.}
\tag{31}
$$
特别，固定中央常数在所有 $p\notin\{2,3,7,17\}$ 处都是单位；$s_m$ 的原系数、原 Euler 因子及后续 Mellin 参数仍须各自保留。本篇没有从这个固定单位推出一个随 $p$ 变化的中央导数非零。

## 9. 证书、依赖与文献

生产脚本 `scripts/check-jzero-exact-central-kronecker-constant.py` 自包含地重建 (18)、(19)、(21)、(24)、(25)。同名 `.json` 保存原 $P_{48}$、六次单位迹的分子、真实 CM7 有理映射、原 resolvent、其准确六次方和全部周期换算。无需任何 scratch 工作文件。

- [R290 — 原 Schwartz 与全权实平方](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)。
- [R297 — 实际次数 34 来源与首项规范](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- K. Bannai and S. Kobayashi, *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*, Duke Math. J. **153** (2010), no. 2, 229–295，Theorem 1.17 及 §1 的规范；DOI: 10.1215/00127094-2010-024。作者全文：<https://arxiv.org/pdf/math/0610163>。原论文中的 $A$ 是实际不变微分 period 格的面积除以 $\pi$，正是 (10)–(14) 使用的尺度。

这里新付清的是原来源的完整常数，而非一条额外的中央消失关系。后续可直接把 (30) 或 (31) 接到明确采用同一 period 规范的原 p-adic 插值式。
