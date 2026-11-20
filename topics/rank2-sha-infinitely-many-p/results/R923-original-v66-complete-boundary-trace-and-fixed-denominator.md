# R923 — 原 V66 的完整首边界迹、固定小分母与三分之四前缀

日期：2026-11-20。**状态：以下第四原来源的全局迹、固定整数分母、全部共轭高度及首边界模 $p$ 充要判据已证明。未证明原中央导数非零，亦未证明中央零迫使这些前缀为零。**

本篇补的是 HANDOFF 第三门中尚未支付的 V66 全迹接口。始终使用 R816/R820 的同一第四来源；不把它换成一个 degree66 的任意截面。计算放在已有共同曲线 $E_{17}$ 上，最后用 R820 的准确单位缩放返回物理曲线 $E_-:y^2=x^3-11$。

## 1. 原第四来源及完整归一

固定
$$
p=6s-1>211,\qquad q=p^2,\quad d=p+1,\quad e=p-1,
$$
$$
K_0=\mathbb Q(\omega),\qquad E_b:y^2=x^3+b,\qquad b=17,
\qquad dz=\frac{dx}{2y},\qquad X=x^3.
$$
使用 R879(2) 的完整因式分解
$$
\begin{aligned}
\phi_{66}(x)=\frac1{7}&X(X+b)(X-8b)^2(X+4b)\\
&\cdot(7X^2-4bX+16b^2)
(X^3+228bX^2+48b^2X+64b^3),
\end{aligned}
\tag{1}
$$
以及
$$
A_{66}(z)=\sigma_b(z)^{66}\phi_{66}(x(z))=V_{17}(z).
\tag{2}
$$
因式相乘正是 R816(42)–(43)、R820(1)–(3) 的原多项式，而不是新选的系数。下文 $c_j$ 由 $\phi_{66}=\sum_{j=0}^{10}c_jb^{10-j}x^{3j}$ 唯一确定，即 R820(2) 的原有理数。$7\phi_{66}\in\mathbb Z[x]$；它只在 $O$ 有极，极阶恰为 $60$，最高项为 $x^{30}$。因此 $A_{66}=z^6+O(z^{12})$，在每个复格点恰有六阶零，是固定偶 degree66 的全纯 theta 截面。

若 $J_{66,p}^{(1)}$ 为 R820(21) 在 $b=1$ 上的原 Gaussian Newton 半因子，且 $J_{V_{17},p}$ 使用 (2) 与同一缩放后的 Gaussian，则齐次身份逐个 Newton 系数给
$$
J_{V_{17},p}=\frac1{17}J_{66,p}^{(1)},\qquad
J_{\Phi_-,p}=-\frac1{11}J_{66,p}^{(1)}
=-\frac{17}{11}J_{V_{17},p}.
\tag{3}
$$
这里没有冻结 Gaussian 而仅缩放 Taylor 系数。所有当前 $p$ 上 (3) 的因子为单位。

## 2. 同一个绝对根域与真正全 Hall 迹

沿用 R696/R705 的原对象
$$
F=K_0(E_b[p]),\qquad F_2=K_0(E_b[p^2]),\qquad
H=\ker\bigl(\mathbf F_{p^2}^{\times}\to\mathbf F_p^\times\bigr).
$$
对非零 $T\in E_b[p]$，保持原
$$
\alpha=\omega^2+p\omega,\qquad
a_T=\frac{\psi_\alpha(T)^{2s}}{\psi_{p+1}(T)^{2s-1}},
\qquad w_T^p=a_T.
$$
这批根及其相对 cocycle 的构造与来源 degree 无关。R696 的原完整相位比较使全部根属于 $F_2$，所有 $T$ 给同一域 $W=F(w_T)$；R705(15)–(16) 给 $[W:F]=p$。令 $\widehat H$ 为 $\operatorname{Gal}(W/F^H)$ 中阶 $d$ 的唯一 Hall 子群，并置
$$
E_W=W^{\widehat H},\qquad
\mathcal T_{66,T}=\operatorname{Tr}_{W/E_W}
\bigl(w_T^{-66}\phi_{66}(T)\bigr).
\tag{4}
$$
这是全部 $p+1$ 项的原迹。没有增添新根或取新的独立 Kummer 方向。

所有根 $w_T$ 换成 $\epsilon w_T$、$\epsilon\in\mu_p$ 时，(4) 只乘 $\epsilon^{-66}$。原 Hall 比较仍准确有
$$
\frac{w_T}{h(w_T)}=r_{h,T}
\quad(h\in\widehat H),
\tag{5}
$$
因为两边的比值为 $H\to\mu_p$ 的同态而 $p\nmid|H|$。所以后面使用的边界与 (4) 具有同一原分支。

共同域 $E_W$ 在有理素数 $p$ 上只有一个位；其绝对局部次数等于绝对全局次数。这一性质仅来自原域，和 $66$ 无关。

## 3. 小固定分母 $D_{66}=154224$

本篇可取
$$
\boxed{D_{66}=7\cdot2^4\cdot3^4\cdot17=154224.}
\tag{6}
$$
将证明
$$
\boxed{D_{66}w_T^{-66}\phi_{66}(T)\text{ 在所有有限位整},\qquad
D_{66}\mathcal T_{66,T}\in\mathcal O_{E_W}.}
\tag{7}
$$
这比只按 $66$ 套用 R700 的粗极帽分母小；改进使用的是 (1) 的全部原因子。

全部有限位赋值统一为 $v_\ell(\ell)=1$。R700 的固定倍点循环及同一潜好模型给
$$
v_2(w_T)=\frac13,\quad v_3(w_T)=\frac14,\quad
v_{17}(w_T)=\frac16,
$$
$$
v_\ell(w_T)=0\quad(\ell\notin\{2,3,17,p\}),\qquad
v_p(w_T)=-\frac1{q-1}.
\tag{8}
$$
这些是每个有关数域有限位上的陈述。以下逐位保留多项式分母。

### 3.1 二处

用 R700 的潜好模型
$$
x=c_2^2x',\qquad y=c_2^3(y'+1/2),\qquad
c_2^6=4b=68,\qquad y'^2+y'=x'^3.
$$
非零 $p$ 挠点的 $x',y'$ 均整。令 $U=x'^3$，则 $X=4bU$。直接将 (1) 的全部因子代入，得到
$$
\begin{aligned}
\phi_{66}(T)=\frac{2^{18}b^{10}}7
&U(4U+1)(U-2)^2(U+1)\\
&\cdot(7U^2-U+1)(U^3+57U^2+3U+1).
\end{aligned}
\tag{9}
$$
所以 $v_2(\phi_{66}(T))\ge18$。由 (8)，
$$
v_2(w_T^{-66}\phi_{66}(T))\ge18-22=-4.
\tag{10}
$$
不要求 (9) 的剩余因子均为单位。

### 3.2 三处

保持原潜好变换
$$
x=r+c_3^2x',\qquad y=c_3^3y',\qquad
r^3=-b,\quad c_3^4=3r^2,
$$
其中 $r$ 为单位、$v_3(c_3)=1/4$，且 $x',y'$ 整。置
$$
\tau=X+b=y^2,\qquad v_3(\tau)\ge\frac32.
$$
在同一个完整多项式里准确有
$$
7X^2-4bX+16b^2=7\tau^2-18b\tau+27b^2,
$$
$$
X^3+228bX^2+48b^2X+64b^3
=\tau^3+225b\tau^2-405b^2\tau+243b^3.
\tag{11}
$$
因此 (1) 的各非单位因子具有下界
$$
\begin{array}{c|ccccc}
\text{因子}&X+b&(X-8b)^2&X+4b&7X^2-4bX+16b^2&X^3+228bX^2+48b^2X+64b^3\\\hline
v_3\text{ 下界}&3/2&3&1&3&9/2.
\end{array}
$$
此外 $X$ 为单位，$7$ 为单位，故
$$
v_3(\phi_{66}(T))\ge13,\qquad
v_3(w_T^{-66}\phi_{66}(T))\ge13-\frac{66}4=-\frac72.
\tag{12}
$$
一个整数因子 $3^4$ 已足够。式 (11) 的可能相消只会提高赋值。

### 3.3 十七处与其余有限位

十七处用 $x=c_{17}^2x'$、$y=c_{17}^3y'$、$c_{17}^6=b$。原 $\phi_{66}$ 在 $X,b$ 中齐次次数十；所以
$$
v_{17}(\phi_{66}(T))\ge10,
\qquad
v_{17}(w_T^{-66}\phi_{66}(T))\ge10-11=-1.
\tag{13}
$$
其他非 $p$ 位，原 $x(T)$ 整，$w_T$ 是单位，$7$ 清掉 (1) 的唯一固定多项式分母。

在 $p$ 位，原参数 $u_T=x(T)^{-1/2}$ 满足 $v_p(u_T)=1/(q-1)$。$\phi_{66}$ 的唯一最高极项 $x^{30}$ 是单位首项；其他各项极阶更小、系数整，因此
$$
v_p(\phi_{66}(T))=-\frac{60}{q-1},\qquad
v_p(w_T^{-66}\phi_{66}(T))=\frac6{q-1}>0.
\tag{14}
$$
(10)、(12)–(14) 对每个共轭成立，证明 (7)；取迹保整性。

## 4. 完整第四首边界与迹的准确身份

继续 R663 的严格整参数
$$
v=h(u),\qquad[-p]v=-pv+v^q,\qquad
W_{\mathrm f}=v^d,\qquad H(W_{\mathrm f})=\mathcal H_p(W_{\mathrm f}^e).
$$
$W_{\mathrm f}$ 是形式变量，区别于上节数域 $W$。保持同一个完整整单位 $T_{\mathrm g}$。定义原完整投影
$$
\Phi_{66}(u)=\frac1d\sum_{\zeta\in\mu_d}\zeta^{66}
T_{\mathrm g}([\zeta]u)^{-66}\phi_{66}([\zeta]P(u)).
\tag{15}
$$
原极阶 $60<d$，且 $d>66$；整坐标与全部 $\mu_d$ 字符投影于是准确给
$$
\Phi_{66}(u(v))=v^{d-66}\mathcal B_{66}(W_{\mathrm f}),\qquad
\mathcal B_{66}\in\mathcal O[[W_{\mathrm f}]],
\tag{16}
$$
其中 $\mathcal O=\mathbb Z_{p^2}$。原完整中央 Gaussian 来源满足
$$
G_{66,c,0}(W_{\mathrm f}H^d)
=W_{\mathrm f}H^{66}\mathcal B_{66}(W_{\mathrm f}).
\tag{17}
$$
这逐项使用 (1)，没有省去低极项或 $T_{\mathrm g}$ 高尾。

把 (5) 代入 (15) 的全部 $H$ 项，原有限迹身份为
$$
\boxed{
v_T^{d-66}\mathcal B_{66}(v_T^d)
=\frac{T_{\mathrm g}(u_T)^{-66}w_T^{66}}d\,
\mathcal T_{66,T}.}
\tag{18}
$$
因 $T_{\mathrm g}(u_T)$ 和 $d$ 为单位，(8) 与 $v_p(v_T)=1/(q-1)$ 立即给
$$
\boxed{v_p(\mathcal T_{66,T})
=\frac1{p-1}+v_p(\mathcal B_{66}(v_T^d)).}
\tag{19}
$$
全 Galois 群在非零 $p$ 挠点上传递；原根差仅为单位根。因此一个 (4) 为零，恰等价于所有原首边界值为零。这保留全部 $e=p-1$ 个范数一轨道。

## 5. 全部共轭的三分之四高度

R704/R707 的 Gaussian–Weil 证明在此需要核对的输入是：固定的偶 degree、格点六阶零、$p$ 不整除 degree，以及全部原根相位。这四项已分别由 (1)–(2)、$p>211$ 和 (5) 支付。

为明确同一来源在估计中的位置，令
$$
A_{66}^{\mathrm{an}}(z)=\mathfrak k(z)^{66}\phi_{66}(P_z),\qquad
\mathfrak k(z)=e^{-\eta_z z/2}\sigma_b(z).
$$
在原格 $\Omega(\mathbb Z+\omega\mathbb Z)$ 上，它的磁全纯 Fourier 展开具有固定的 66 个系数 $d_0,\ldots,d_{65}$。R704 的绝对酉 Zak 变换后，归一向量准确为
$$
f_{66,p}(n)=q^{-1/4}\sum_{k\in\mathbb Z}
d_{[pk]_{66}}
\exp\!\left(-\pi66\frac{\sqrt3-i}{2}
\frac{(n-qk/66)^2}{q}\right).
\tag{20}
$$
这些 $d_j$ 由 (2) 的固定全纯截面决定，不能逐 $p$ 另选。

同一 Heisenberg 重叠完成平方给
$$
|\langle f,\mathsf D_t f\rangle|
\le C\Gamma_{q,c}(66t),
$$
而 R707 增补的完整 Eisenstein gcd 计数给
$$
\sum_{N(U)\equiv N(V)\ (q)}
e^{-c(N(U)+N(V))/q}\ll q(1+\log q).
$$
因为 $66$ 在 $\mathbb Z[\omega]/q$ 中为单位，可用 $u=66t$ 重标。非零非单位的 Hall 作用仍自由，零向量仍贡献 $p+1$；不能将这两部分删去或把 Hall 改为整个 $p^2$ 范数一群。全空间 Weyl 正交与 Cauchy–Schwarz 因而给
$$
\|\mathsf P_Hf_{66,p}\|^2\ll p^{-1/2}(1+\log p)^{1/2}.
\tag{21}
$$
原样本在零剩余类的值为零，故 R705 的旧一维分量为零。保留样本与 (20) 间的真实 $p^2$ 范数因子，对原完整 torus 和 $\mathscr S_{66,p}(r)$ 有
$$
\boxed{\sum_{r\in\mathbf F_p^\times}|\mathscr S_{66,p}(r)|^2
\ll p^{5/2}(1+\log p)^{1/2}.}
\tag{22}
$$
wild 角色仍是 R705(5) 的 $\chi_{m,r}$，此处 $m=66$；它在 $1+p\delta t$ 上的值是 $e_p(66rt)$，故导子恰 $p^2$。没有使用物理导子66去替换这一原局部 wild 角色。

同一全 Galois 运输使每个 $r\ne0$ 的绝对值在 $E_W/K_0$ 的嵌入中出现 $p$ 次。$\phi_{66}$ 为实有理系数，$K_0$ 的另一个嵌入同时共轭 Klein 相位与角色，仍给同一绝对值组。故 (7)、(22) 和 Jensen 不等式证明
$$
\boxed{h(\mathcal T_{66,T})
\le\frac34\log p+\frac14\log(1+\log p)+C_{66},}
\tag{23}
$$
其中 $C_{66}$ 是与 $p,T$ 无关的常数，含固定 $\log154224$。

对非零 $D_{66}\mathcal T_{66,T}$ 取绝对整数范数。唯一 $p$ 位的次数权重为一，其他有限位整，且 $p\nmid D_{66}$。于是
$$
\boxed{\mathcal T_{66,T}\ne0\Longrightarrow
v_p(\mathcal T_{66,T})
\le\frac34+
\frac{\frac14\log(1+\log p)+C_{66}}{\log p}.}
\tag{24}
$$
这是一条“非零时”上界，不把范数论证倒过来当作非零性证明。

## 6. 原第四首边界的短模 $p$ 充要判据

写 $\mathcal B_{66}(W_{\mathrm f})=\sum_{i\ge0}b_iW_{\mathrm f}^i$。其除以
$$
Q(W_{\mathrm f})=W_{\mathrm f}^e-p
$$
的完整余数系数为
$$
r_i=\sum_{k\ge0}p^k b_{i+ek}\in\mathcal O,
\qquad0\le i<e.
\tag{25}
$$
对 $\xi^e=p$，不同 $i$ 的 $v_p(r_i\xi^i)$ 有不同小数部分。因此非零时
$$
v_p\mathcal B_{66}(\xi)=
\min_{0\le i<e}\left(v_p(r_i)+\frac ie\right).
\tag{26}
$$
固定任意 $\alpha\in(3/4,1)$，并令
$$
J_\alpha(p)=\lceil\alpha(p-1)\rceil-1.
$$
由 (24)，充分大的 $p$ 上每个非零原迹的赋值严格小于 $\alpha$。若 $b_i\equiv0\pmod p$ 对 $0\le i<J_\alpha(p)$ 成立，则 (25)–(26)、(19) 给原迹赋值至少
$$
\frac{J_\alpha(p)+1}{p-1}\ge\alpha,
$$
故原迹必为零。反之，一个原迹零由全 Galois 传播迫全部 $\xi$ 上的值零，即 $Q\mid\mathcal B_{66}$；其模 $p$ 前 $e$ 个系数均为零。于是准确得到
$$
\boxed{\mathcal T_{66,T}=0
\Longleftrightarrow Q\mid\mathcal B_{66}
\Longleftrightarrow b_i\equiv0\pmod p\ (0\le i<J_\alpha(p)).}
\tag{27}
$$

令原首 Gaussian 系数为
$$
g_{66,h}=[z^{dh}]\bigl(A_{66}(z)e^{-66c z^d}\bigr),
\qquad c=[z^d]\log(\sigma_b/z).
$$
(17) 和 $H=1+O(W_{\mathrm f}^e)$ 使 $b_{h-1}=g^{\mathrm c}_{66,h}$ 对 $1\le h\le e$ 准确成立。R708(14) 的完整乘法平均
$$
\exp\{-66(F_c(X)-cX)\}
=\left(\prod_{\zeta^d=1}
\frac{\sigma_b(\zeta z)}{\zeta z}e^{-c(\zeta z)^d}\right)^{-66/d}
$$
在 $X$ 次数 $<e$ 给整单位下三角变换，逆亦整，因为 $-66/d\in\mathbb Z_p$。其所用 Gaussian 整窗为同一 R614 的 $z$ 次数 $<q-1$。所以 (27) 也准确等价于
$$
\boxed{g_{66,h}\equiv0\pmod p\qquad1\le h\le J_\alpha(p).}
\tag{28}
$$
全单模 $p$ 判据可取 $J=e-1=p-2$；上述短门的实际输入窗口为 $dJ-6=\alpha p^2+O_\alpha(p)$。完整有限来源可直接按原系数计算：
$$
z^{-6}A_{66}(z)e^{-66cz^d}
=\left(\frac{\sigma_b(z)}z e^{-cz^d}\right)^{66}
\sum_{j=0}^{10}c_jb^{10-j}z^{60-6j}(z^2x(z))^{3j}.
\tag{29}
$$
全部指数非负，最低为零；没有额外的有限极或任意 lift。

## 7. 与主目标的准确距离

(3) 保物理曲线、完整通常 Selmer 和 R820 的全部周期、Euler、固定平方常数。此篇只新增同一个 V66 的 (7)、(18)、(24)、(27)–(29)，使四个原来源现在都具有完整的首边界迹工具。

原 $j_{66}=J'_{V_{17},p}(0)$ 仍含 R710/R915 的全部真实进位、正则补项及高尾。没有从 $j_{66}=0$ 得到 (28)，没有由 $\mathcal T_{66,T}\ne0$ 自动得到 $j_{66}\ne0$，也没有证明四个原首中央在无限多个 $p$ 上不能同时为零。

依赖：R816、R820、R879 的原 V66 身份与物理缩放；R696、R700、R705 的共同根、完整相位、潜好模型及域；R704、R707 及其 Eisenstein gcd 增补的完整 Gaussian–Weil 估计；R663、R708 的同一严格坐标、完整余数和整 Gaussian 返回。以上为手证，无数学执行或新可重算数据。
