# R271 附录：不交未来窗的顶部投影、相容整流与全部 primitive 反馈

日期：2026-11-13（UTC）。作者：Astra-ISP-1cf8c51d / boundary_resume_2220；AI-assisted，GPT-6 Astra Pro。

状态：**已证明。** 本稿在原同一个顶部左最小者上，用一列互不相交的未来窗口定义真实总两费用度量，再作一次顶部投影。残源的所有截断因而继续组成同一条实际源流。顶部的有界廉价闭子空间已经足够，不要求未知尾衰减多付一个 $\sqrt d$，也不按指数多窗口分别累加误差。

全部真实 primitive 增量和单步完整尾 MP 反馈的改变量，由同一个顶部左范数的 Pythagoras 一起支付。准确余条件是一个总度量的正交条件，不是每个切口各自的两费用正交条件。新的余比较尚未证明；无权 $N=M$ 与普通 ISP 仍为 OPEN。

依赖：[原左最小者截断及未来带](R271-appendix-left-minimizer-truncation-source-flow-and-exact-band-budgets.md)、[完整源流像及纤维](R271-appendix-exact-left-source-flow-range-and-minimal-upward-extension.md)、[原负图与实际窗口归约](R271-appendix-negative-source-flow-joint-paid-flag-and-actual-window-reduction.md)、[完整远尾出生短回缩](R271-appendix-shifted-primitive-retractions-and-paid-actual-source-removal.md)。廉价负图旗也可选[天然四块首源旗](R239-appendix-natural-model-first-source-flag-without-angle-loss.md)。

## 1. 原同一个顶部的全部截断算子

固定原 $m\ge8,d=2^m,A=A_m,D=D_m$。在每个孔数 $p$ 的真实源空间 $\mathscr R_p$ 上，保留
\[
L_p=J_{{\rm left},p}^{-1},\qquad
B_p=J_{{\rm bare},p}^{-1},\qquad
G_p=J_{{\rm right},p},
\]
\[
\begin{aligned}
\mu_p(r)^2&=\langle L_pr,r\rangle,&
\alpha_p(r)^2&=\langle B_pr,r\rangle,\\
\lambda_p(r)^2&=\langle G_p^{-1}r,r\rangle,&
\lambda_{{\rm flat},p}(r)^2&=\langle G_pL_pr,L_pr\rangle.
\end{aligned}
\]
两已付费用及其真正度量为
\[
\boxed{\Xi_p(r)^2=\alpha_p(r)^2+\lambda_{{\rm flat},p}(r)^2
=\langle\mathfrak M_pr,r\rangle,\qquad
\mathfrak M_p=B_p+L_pG_pL_p.}
\tag{1.1}
\]
每个固定窗口中这些算子有界、严格正。尤其裸费不大于完整右费；下文不反转这两个可行集的包含方向。

固定顶部 $b$。对任意 $r\in\mathscr R_b$，令
\[
u=E_b^\dagger r,\qquad
\boxed{\Pi_{p,b}r=A P_pu\quad(0\le p\le b).}
\tag{1.2}
\]
原相容截断定理准确给
\[
\boxed{E_p^\dagger\Pi_{p,b}r=P_{\le p}E_b^\dagger r,\qquad
\Pi_{b,b}=I.}
\tag{1.3}
\]
各 $\Pi_{p,b}$ 是固定参数下的有界算子。并有
\[
\Pi_{p,s}\Pi_{s,b}=\Pi_{p,b}\quad(p\le s\le b).
\tag{1.4}
\]
因此任何一次顶部线性修改，均自动给出所有切口的一条相容源流。

若 $p<b$，(1.3) 还给
\[
\Pi_{p,b}r\in\mathscr N_p,\qquad
\mathscr N_p=\ker[\iota_0^*(L_p+B_p)].
\tag{1.5}
\]
若还需顶部属于负图，就将顶部源域取为 $\mathscr N_b$。不能由 (1.5) 将任意顶部也免费放进 $\mathscr N_b$。

## 2. 真总度量只在互不相交未来带上取和

令
\[
Q=\lfloor e^{d^3/4}\rfloor,\qquad b=Q-d,\qquad
a=b-d\left\lfloor\frac{b-4d}{d}\right\rfloor .
\tag{2.1}
\]
于是 $4d\le a<5d$。取切口列
\[
\boxed{I=\{a,a+d,\ldots,b\}.}
\tag{2.2}
\]
各物理未来带 $[p+1,p+d]$、$p\in I$ 彼此不交，其并正好是 $[a+1,Q]$。切口数满足
\[
|I|=\frac{Q}{d}+O(1).
\tag{2.3}
\]

在同一个顶部源空间定义
\[
\boxed{
\mathfrak H_b=\sum_{p\in I}\Pi_{p,b}^*\mathfrak M_p\Pi_{p,b},
\qquad
\Psi_b(r)^2=\langle\mathfrak H_br,r\rangle
=\sum_{p\in I}\Xi_p(\Pi_{p,b}r)^2.}
\tag{2.4}
\]
这是有限和；包含 $p=b$ 项，故 $\mathfrak H_b\succeq\mathfrak M_b$，在固定参数下有界且严格正。不需要各 $\Pi_{p,b}$ 具有统一算子范数；实际来源的总费用直接从同一物理向量支付。

具体地，取一个真正顶部最小者 $u_Q=E_Q^\dagger r_Q$，令
\[
r_b=A(u_Q)_b,\qquad
r_p=\Pi_{p,b}r_b=A(u_Q)_p.
\tag{2.5}
\]
因为 $b<Q$，$r_b\in\mathscr N_b$。完整未来带身份逐项给
\[
\Xi_p(r_p)^2\le
2\|P_{[p+1,p+d]}u_Q\|^2.
\]
对不交的带求和得到
\[
\boxed{\Psi_b(r_b)^2\le2\|P_{[a+1,Q]}u_Q\|^2.}
\tag{2.6}
\]
这里没有窗口数，也没有通常遍历所有相邻切口时出现的重叠因子 $d$。

## 3. 一次顶部投影及准确余条件

取一个闭顶部空间 $\mathscr D_b\subseteq\mathscr R_b$，并假设已给来源 $r_b\in\mathscr D_b$。主应用取 $\mathscr D_b=\mathscr N_b$。如果另有已经支付、并由同一个顶部来源满足的闭约束，也可取这些约束的交；逐窗独立投影得到的不同来源不能据此重新拼成一个顶部。

在 $\mathscr D_b$ 内，取一个闭子空间 $\mathscr K_b$，满足
\[
\boxed{\mu_b(s)\le c_b\Xi_b(s)\qquad(s\in\mathscr K_b).}
\tag{3.1}
\]
如需完整右费运输，再假设
\[
\boxed{\lambda_b(s)\le \ell_b\Xi_b(s)\qquad(s\in\mathscr K_b).}
\tag{3.2}
\]
这些是顶部同一源的真实费用估计，不是对某个更便宜模型源的估计。

在 (2.4) 的真正总度量中投影：
\[
\boxed{s_b=P_{\mathscr K_b}^{\mathfrak H_b}r_b,\qquad
\widehat r_b=r_b-s_b.}
\tag{3.3}
\]
两者仍在 $\mathscr D_b$。对所有 $0\le p\le b$，定义
\[
s_p=\Pi_{p,b}s_b,\qquad
\widehat r_p=\Pi_{p,b}\widehat r_b=r_p-s_p.
\tag{3.4}
\]
由 (1.3)，这是同一个新顶部 $\widehat u_b=E_b^\dagger\widehat r_b$ 的全部真正左最小前驱。特别
\[
T_{p+1}\widehat r_{p+1}=\widehat r_p
\quad(0\le p<b).
\tag{3.5}
\]
若 $\mathscr D_b\subseteq\mathscr N_b$，连顶部在内的全部这些源都保持负图。

真正总度量的 Pythagoras 是
\[
\boxed{\sum_{p\in I}\Xi_p(r_p)^2
=\sum_{p\in I}\Xi_p(s_p)^2
+\sum_{p\in I}\Xi_p(\widehat r_p)^2.}
\tag{3.6}
\]
它不声称每个切口的费用分别收缩，也不声称裸/flat 两个分量分别收缩。

令 $\iota_{\mathscr K_b}$ 为闭子空间的包含，投影准确写为
\[
P_{\mathscr K_b}^{\mathfrak H_b}
=\iota_{\mathscr K_b}
(\iota_{\mathscr K_b}^*\mathfrak H_b\iota_{\mathscr K_b})^{-1}
\iota_{\mathscr K_b}^*\mathfrak H_b.
\tag{3.7}
\]
中间逆在真实闭空间 $\mathscr K_b$ 上有界。准确余条件是
\[
\boxed{\widehat r_b\in\mathscr D_b,\qquad
\iota_{\mathscr K_b}^*
\left(\sum_{p\in I}\Pi_{p,b}^*\mathfrak M_p\Pi_{p,b}\right)
\widehat r_b=0.}
\tag{3.8}
\]
不把 (3.8) 改成每个 $p$ 的独立正交条件，更不改成物理或 primitive 坐标为零。

## 4. 整个物理前驱和全部 primitive 增量的统一费用

因 $b\in I$，由 (3.1)、(3.2)、(3.6)，
\[
\boxed{
\begin{aligned}
\|E_b^\dagger r_b-E_b^\dagger\widehat r_b\|
&=\mu_b(s_b)\le c_b\Psi_b(r_b),\\
|\lambda_b(r_b)-\lambda_b(\widehat r_b)|
&\le\lambda_b(s_b)\le\ell_b\Psi_b(r_b).
\end{aligned}}
\tag{4.1}
\]
第一式自动控制每个较低切口的左改变量，因为它们只是同一向量的截断：
\[
\boxed{\sup_{0\le p\le b}
\|E_p^\dagger r_p-E_p^\dagger\widehat r_p\|
\le c_b\Psi_b(r_b).}
\tag{4.2}
\]
若使用 (3.2)，顶部准确有限模型零源向量
$E_b^\dagger s_b-F_b^\dagger s_b$ 的平方范数不超过
$(c_b^2+\ell_b^2)\Psi_b(r_b)^2$。此核仍须按原规则支付 carry 才能用于两个实际边界。

还有比逐步三角不等式更强的反馈预算。记
\[
z=E_b^\dagger s_b,\qquad R_p=(D:\mathcal H_{p+1}\to\mathcal H_p)^\dagger.
\]
完整源流纤维定理逐层给
\[
z_{p+1}=-R_ps_p+g_{p+1},\qquad
g_{p+1}\in
\left(\bigoplus_{i=1}^{d-1}\mathbb Ce_i\right)
\otimes\ker D|_{\mathcal H_{p+1}} .
\tag{4.3}
\]
两个尾分量正交。对原流与残流，$g_{p+1}$ 恰是其真实 primitive 增量之差，因为 (4.3) 的分解唯一且线性。故对任意 $0\le u<v\le b$，
\[
\boxed{\begin{aligned}
\sum_{p=u}^{v-1}
\left(\|R_ps_p\|^2+\|g_{p+1}\|^2\right)
&=\|P_{[u+1,v]}z\|^2\\
&=\mu_v(s_v)^2-\mu_u(s_u)^2\\
&\le c_b^2\Psi_b(r_b)^2.
\end{aligned}}
\tag{4.4}
\]
所以全部真实单步尾逆及 primitive 反馈一次付清，没有乘步数。这里改变的是由顶部投影决定的整条反馈，不是保持每一步旧 primitive 不变后强行迭代一层定理。

## 5. 两类现成的原顶部闭空间

### 5.1 指数小负图旗

取原已付旗 $\mathscr X_b$，例如天然四块首源旗，且
\[
\mathscr K_b=\mathscr N_b\cap\mathscr X_b.
\]
原负图估计给
\[
\mu_b(s)\le\delta_b\Xi_b(s),\qquad
\lambda_b(s)\le
\sqrt{\delta_b^2/4+\delta_b^4}\,\Xi_b(s),
\]
\[
\mu_b(s)^2+\lambda_b(s)^2
\le\delta_b^2(1+\delta_b^2)\Xi_b(s)^2.
\tag{5.1}
\]
天然四块首源旗可取 $\delta_b\le e^{-d^4/20}$。因此 (3.1)–(4.4) 直接适用。

只要求顶部进入这个旗，已足以保持整条流和总预算；不能因此断言每个较低 $s_p$ 也在对应已付旗。若确实需要这项额外性质，可改取有限闭交
\[
\mathscr K_b^{\rm all}
=\mathscr N_b\cap
\bigcap_{p\in I}\Pi_{p,b}^{-1}(\mathscr X_p).
\tag{5.2}
\]
这样在每个选中切口均可使用 (5.1)，并对其平方求和。投影的域随之缩小；不把两种投影混同，也不承诺该交空间具有未证的覆盖性。

### 5.2 保整个远尾 primitive 出生的实际回缩

取原远尾出生短回缩稿的闭像 $\mathscr E_b$，满足
\[
\lambda_b(s)\le C_b\alpha_b(s)\quad(s\in\mathscr E_b).
\tag{5.3}
\]
由原正逆 Cauchy，
\[
\mu_b(s)^2\le\lambda_b(s)\lambda_{{\rm flat},b}(s)
\le\frac{C_b}{2}\Xi_b(s)^2.
\]
故
\[
\boxed{\mathscr K_b=\mathscr E_b\cap\mathscr N_b,\qquad
c_b=\sqrt{C_b/2},\quad \ell_b=C_b}
\tag{5.4}
\]
满足全部假设。若还须保持某个已经由同一顶部满足的闭空间 $\mathscr D_b$，以 $\mathscr E_b\cap\mathscr D_b$ 代替即可。

原参数 $k\ge1,t=k-1$、顶部孔数
$b\ge128(d+k)^2$，及远尾 primitive 出生
\[
0\le b_{\rm far}\le
\left\lfloor\frac{b}{192(d+k)}\right\rfloor
\]
给 $C_b<2$。这里 $b_{\rm far}$ 区别于本稿顶部 $b$；暗对数为
$b-b_{\rm far}-k+1$，整个原 $K_{b_{\rm far}}(D_J)$ 仍保留。
所以 $c_b<1,\ell_b<2$，没有退回远尾单个真空向量。

与前稿逐窗 $\mathfrak M_p$ 投影不同，本稿只作一次 $\mathfrak H_b$ 顶部投影。它将有界常数的实际回缩删除与相容整流同时保留，所付的正是 (3.8) 的新总余条件。

## 6. 同一个非零实际缺陷来源及无额外衰减假设

假设 $0\ne w\in W=M\ominus\overline{BM}$。原顶部构造给同一个
\[
u_Q=E_Q^\dagger r_Q,\qquad
\|u_Q-P_{\le Q}^{(m)}w\|
\le\eta_m\|w\|,
\quad \eta_m=e^{-74d^4}+e^{-75d^4}.
\]
令
\[
\tau_m=\|1_{\{\mathcal N_{\rm tot}>4d\}}w\|,
\qquad t_m=\tau_m/\|w\|\longrightarrow0,\qquad
\varepsilon_m=\tau_m+\eta_m\|w\|.
\tag{6.1}
\]
尾孔数不超过总占据数。因 $a\ge4d$，(2.6) 给
\[
\boxed{\Psi_b(r_b)^2\le2\varepsilon_m^2.}
\tag{6.2}
\]
这里没有要求 $\sqrt d\,t_m\to0$，更没有假定未知实际尾有某个速率。

对 §§3–5 的投影，若 $c_b,\ell_b$ 有统一上界，则
\[
\boxed{
\begin{aligned}
\sup_{a\le p\le b}
\|E_p^\dagger\widehat r_p-w\|
&\le(1+\sqrt2c_b)\varepsilon_m\longrightarrow0,\\
\sum_{p\in I}\Xi_p(\widehat r_p)^2
&\le2\varepsilon_m^2\longrightarrow0,\\
|\lambda_b(r_b)-\lambda_b(\widehat r_b)|
&\le\sqrt2\ell_b\varepsilon_m\longrightarrow0 .
\end{aligned}}
\tag{6.3}
\]
第一式使用原同一 $u_Q$ 的所有截断，再减去 (4.2)；第二式是总度量 Pythagoras。它们保留同一个固定 $w$，并且残源在每个相邻切口之间仍满足 (3.5)。

全部反馈改变量也准确满足
\[
\boxed{\sum_{p=a}^{b-1}
(\|R_ps_p\|^2+\|g_{p+1}\|^2)
\le2c_b^2\varepsilon_m^2\longrightarrow0.}
\tag{6.4}
\]
应用 (5.4) 的 $C_b<2$ 时，左前驱误差不超过
$(1+\sqrt2)\varepsilon_m$，顶部完整右费差不超过
$2\sqrt2\varepsilon_m$，反馈平方和不超过 $2\varepsilon_m^2$。

因为 $\widehat u_b$ 是真正同一个顶部，若还要恢复所有相邻切口的完整未来带身份，可在 $a\le p\le b-d$ 直接应用原截断定理：
\[
\Xi_p(\widehat r_p)^2
\le2\|P_{[p+1,p+d]}\widehat u_b\|^2.
\tag{6.5}
\]
因此这些密切口的总费用至多
\[
2d\,\|P_{>a}\widehat u_b\|^2
\le2d(1+\sqrt2c_b)^2\varepsilon_m^2.
\tag{6.6}
\]
这里只失去新顶部最后一个宽度 $d$ 的未来窗。不能对 $p>b-d$ 直接用 $\widehat u_b$ 支付尚不存在的未来层；那些选中切口的费用已由 (3.6) 单独支付。

## 7. 稀疏切口仍保留原比较门槛

对充分大的 $m$，置
\[
\vartheta_m=
\sqrt{1-t_m^2}-\eta_m-\sqrt2c_b(t_m+\eta_m)
\longrightarrow1.
\]
(1.3)、原顶部低层质量及 (4.2) 给
\[
\mu_p(\widehat r_p)\ge\vartheta_m\|w\|
\quad(p\in I).
\tag{7.1}
\]
定义实际残源比例
\[
C_{m,p}^{\rm coh}(w)=
\frac{\mu_p(\widehat r_p)^2}{\Xi_p(\widehat r_p)^2}>0.
\]
由 (6.3)，
\[
\boxed{\sum_{p\in I}\frac1{C_{m,p}^{\rm coh}(w)}
\le\frac{2(t_m+\eta_m)^2}{\vartheta_m^2}
\longrightarrow0.}
\tag{7.2}
\]
而 $|I|\sim Q/d$。所以若只在这一条真实相容余源族上、沿无穷头子序列付
\[
\boxed{\sup_{p\in I}C_{m,p}^{\rm coh}(w)
=O(Q/d)=O(e^{d^3/4}/d),}
\tag{7.3}
\]
则 (7.2) 矛盾。这个门槛与原密窗口求和相同：窗口数减少 $d$ 倍的同时，真实费用重叠也准确减少 $d$ 倍。

本文未证明 (7.3)。新增的是可供后续使用的同一顶部、完整相容源流、全部 primitive 反馈平方和以及准确总余条件 (3.8)。因此之后再次进行一次顶部模型运输或尾重排时，可以继续使用同一个向量；不必将逐窗独立的余源误称为一条流。新的约束仍不允许删去真实 Schur 交叉块或把原混合 flat 费用改成模型坐标范数。
