# R59. 固定同源参考与真实惰性归一行

日期：2026-11-12。**状态：所列恒等式、整性和全精度比较已证明；
实际加权行在无穷多个惰性素数的非零性未证明。**

## 1. 实际目标商已经在原曲线上

在 $E_0:y^2=x^3-x$ 上取 $T=(0,0)$、$\alpha=4-i$、$a=4+i$。
令 $f_S(z)=\varphi_{T+S}(\alpha z)$，$S\in E_0[a]$，
其中 $\varphi_R(z)=\sigma(R+z)\exp(-\bar Rz/\mathcal A)/\sigma(R)$。
则 $f_0(z)=\theta(\alpha z)$，而
$$
r_S=f_S/f_0\in L(E_0),\quad L=\mathbb Q(i,E_0[17]),\qquad
r_S(O)=1.
$$
准确全 jet 恒等式为
$$
\varphi_R(z)^{17}=\frac{\theta(az)}{h_{a,R}(z)},\quad
r_S(z)^{17}=\frac{h_{a,T}(\alpha z)}{h_{a,T+S}(\alpha z)},\quad
h_{a,R}(z)=\frac{\Psi_a(R+z)}{\Psi_a(R)}.
\tag{1}
$$
代表元的准周期指数在(1)中完全相消；两个截面有相同自动因子，
所以 $r_S$ 本身有理，不需要新根覆盖。

记 $V=x^{-2}$，则 R51 的实际 $D=1$ 截面满足
$$
A_1=f_0R_*,\quad R_*=
\frac{V+3V^2/5-V^3/5+V^4/5}
{1+(12-20i)V+(-10+28i)V^2+(-20-12i)V^3+(1+4i)V^4}
=\sum_S a_Sr_S.
\tag{2}
$$
$\sum a_S=0$，$R_*(O)=0$ 为四阶零；它恰在
$[\alpha]^{-1}T\setminus\{T\}$ 有十六个简单极点。

## 2. 每个目标惰性素数的完整解析行

对 $p\ge7$、$p\equiv3\pmod4$，令 $d=p+1$、
$c=[t^d]\log(\sigma(\log_Et)/t)$，故 $v_p(c)=-1$。
写 $G_S=e^{-17cz^d}f_S$ 并定义
$$
J_S(u)=\sum_{h\ge0}[z^{dh}]G_S\,(17c)^{-h}(u)_h,\qquad
K_S=J_S/J_0.
\tag{3}
$$
固定域 $L$ 在这些 $p$ 处未分歧：曲线良好且17挠点的阶素于p。
R54的半径估计和(1)的整有理商给
$$
J_S\in1+pu\mathcal O\langle u\rangle,\quad J_0(0)=1,
\quad K_S(0)=1,\quad K_0=1,
$$
以及准确插值 $J_S(k)=k!(17c)^{-k}[z^{dk}]f_S$。
这里的商在解析变换之后取得，没有交换函数乘法和 Mellin 乘法。
特别地，R54的实际半因子满足
$$
\boxed{\mathcal J_p'(0)=\sum_Sa_SK_S'(0).}
\tag{4}
$$
由 R54，(4)非零足以给 $\Sha(E_{17}/\mathbb Q)[p^\infty]$ 有限；
本结果未声明惰性反向。

若 $Z_{S,p}=(C_d(T+S)+\kappa_p)/p$，则
$$
\frac{K_S'(0)}p\equiv-\frac{Z_{S,p}-Z_{0,p}}{pc}\pmod p,
\qquad
\frac{\mathcal J_p'(0)}p\equiv\frac{\beta_d}{17pc}\pmod p.
\tag{5}
$$
差行的第h个下降阶乘系数赋值至少
$\lceil(h(p-1)+4)/(2p)\rceil$，因此导数截到H项的误差至少为
$$
\left\lceil\frac{(H+1)(p-1)+4}{2p}\right\rceil+v_p(H!).
\tag{6}
$$
这既保留全部 Bell 交叉项，也给出真正趋于无穷的尾界。

## 3. 通常上同调还缺少的比较

令 $\mathcal D=[\alpha]^{-1}T\setminus\{T\}$、$U=E_0\setminus\mathcal D$。
简单极点空间到 $H^1_{\rm dR}(U)$ 的映射单射：
若 $R\omega=dH$，则H的任何极点会给至少二阶极点，故H只能为常数。
这保留了实际 $R_*$ 的有限维输入。

但完整自然行 $\ell_p(R)=(J_{f_0R}/J_{f_0})'(0)$ 并不在整个
$\mathcal O(U)$ 上通过通常 de Rham 类分解。
取 $H=-yR_*$，则 $dH$ 在同一U上恰当，而精确计算给
$$
[z^8]f_0(\delta H-1)=-\frac{4909}{5}-\frac{6307}{3}i\equiv1\pmod7,
\qquad \frac{\ell_7(\delta H)}7\equiv3\pmod7.
\tag{7}
$$
(6)证明(7)没有遗漏可影响模7值的无限尾。
真正的分部积分是
$J_{zF'/d}(u)=uJ_F(u)$，其参考连接含有 $z$ 和 $\delta\log f_0$；
不能直接换成裸 $dH$ 的积分。

完整证明见[固定同源全jet与归一行](../notes/2026-11-12-inert-fixed-isogeny-jets-and-normalized-rows.md)
及[真实行的分部积分与恰当微分检查](../notes/2026-11-12-actual-laplace-row-and-exact-forms.md)。
两篇已根端独立审核，(7)的有理展开与模7规范已独立复算。
已发表的 Coleman theta 对数公式不自动给(4)的比较；仍须证明实际等式或直接非零。

## 4. 实际简单极点微分的纯对数分解

对每个 $P\in\mathcal D$，令 $\rho_P=\operatorname{res}_P(R_*\omega)$，
取固定 Miller 函数 $g_P$ 满足
$\operatorname{div}g_P=17(P)-17(T)$、$g_P(O)=1$。
因 $P-T\in E_0[\alpha]$，此函数存在于同一固定域 $L(E_0)$。
有准确恒等式
$$
\boxed{R_*\omega=\frac1{17}\sum_{P\in\mathcal D}\rho_Pd\log g_P.}
\tag{8}
$$

这里整体 holomorphic 项不能仅从留数省去。设
$B_P=(y+y(P))/(x-x(P))-y/x$、
$U_P=-D\log\Psi_\alpha(P)/17$，完整sigma规范给
$B_P\omega=d\log g_P/17+U_P\omega$。
再对 $R_*d\log\Psi_\alpha$ 用全局留数定理，剩余常数准确为
$$
c=\sum_P\rho_PU_P=\frac1{17}\sum_{Q\in E_0[\alpha]}R_*(Q).
$$
非零核点的四个 $\mu_4$ 轨道由以下四次多项式参数化：
$$
K(X)=(4-i)X^4+(-12+20i)X^3+(28+10i)X^2+(-20-12i)X-i.
$$
在 $K[X]/(K(X))$ 中对实际 $R_*=Q(X)/U(X)$ 作精确求逆，
Newton迹给 $\operatorname{Tr}(Q/U)=0$，故 $c=0$，证明(8)。
完整余式、Miller加法链及所有规范见
[纯对数分解与零迹证书](../notes/2026-11-12-actual-rational-reference-pure-logarithmic-form.md)，
[精确脚本](../scripts/check-inert-rational-reference-trace.py)已根端复跑。

(8)给全精度改写
$\mathcal J_p'(0)=\frac1{17}\sum_P\rho_P\ell_p(D\log g_P)$。
尚须实际证明这些 $\ell_p(D\log g_P)$ 与指定代数端点、切向或周期的比较；
它们不因出现 $d\log$ 就自动成为某个固定代数数的普通 $p$ 进对数。
