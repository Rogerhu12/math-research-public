# R300 — 新 j=0 原来源的完整 34 维 p-core、单 Euler 测度与全部 tame 分支

日期：2026-11-13。**状态：以下同一个原来源的完整 CM 迹、整 p-core、准确本征标量、单 Euler 测度恒等式、所有 tame 分支及中心质量均已证明。标量的确定先使用已独立证明的 Katz 正权插值与整条平方，再使用真实迹的整性；没有先假定所求的单 Euler 式。这里尚未证明原中央导数对无穷多个素数非零。**

固定 R290、R294、R297 的实际对象
$$
E:y^2=x^3+17,\qquad K=\mathbf Q(\delta),\quad
\delta^2=-3,\quad \omega=(-1+\delta)/2,
$$
$$
S=\sigma^{34}x^2P_4(x^3)=\sum_{m\ge0}s_mz^m,\qquad
P_4(X)=(X+17)(X-136)\left(X^2-\frac{68}7X+\frac{4624}7\right).
\tag{1}
$$
规范是 $x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、$\sigma=z+\cdots$。
特别地，$S=z^6+\cdots$，$S(\zeta z)=S(z)$ 对全部 $\zeta\in\mu_6$ 成立。
这是 R290 的原有限 Schwartz 来源，经 R297 完整 CM13 矩阵识别后的首项一规范。

## 1. 主结论与实际 Hecke 参数

令 $p>7$、$p\equiv1\pmod3$。选与普通正式群相容的 CM 嵌入，写
$$
\pi=\psi(\mathfrak p),\qquad \bar\pi=\psi(\bar{\mathfrak p}),\qquad
\pi\bar\pi=p,\quad v_p(\pi)=1,\quad v_p(\bar\pi)=0.
\tag{2}
$$
$\psi$ 始终是本曲线在 R290 中确定的实际 Hecke 角色。对素于
$\mathfrak f=(34\delta)$ 的 $a\in\mathcal O_K$，完整的有限角色是
$$
\begin{aligned}
\varepsilon(a)&=\chi_2(a)\chi_3(a)\chi_{17}(a),\\
\chi_2(a)&=\operatorname{Teich}_{\mu_3}(a\bmod2),\\
\chi_3(a)&=a\bmod\delta\in\{\pm1\},\\
\chi_{17}(a)&=(a\bmod17)^{48}\in\mu_6,\\
\psi((a))&=a\varepsilon(a)^{-1}.
\end{aligned}\tag{3}
$$
这里模 $17$ 的值取其 $\mu_6$ 提升，不是复共轭；上横线始终表示
$K/\mathbf Q$ 的复共轭。R290 同时支付了统一化元相位
$\chi_2(2)=-1$、$\chi_3(\delta)=-i$、$\chi_{17}(17)=-1$。
因此不能把 (2) 换成任取的范数 $p$ 生成元。
由于 $\varepsilon|_{\mu_6}$ 是恒等角色，(2) 给 $\varepsilon(\pi)=1$。

采用 R295 同一微分和普通正式周期 $\Omega_p$，令
$$
\mathcal A_S(T)=S(\Omega_p\log(1+T))
=\int_{\mathbf Z_p}(1+T)^x\,d\nu_S(x).
\tag{4}
$$
它是整 Amice 变换。记 $[c]_*$ 为变量乘 $c$ 的推前，且
$$
\psi_p\nu=(x\mapsto x/p)_*(\nu|_{p\mathbf Z_p}),\qquad
T_p=\bar\pi[\bar\pi^2]_*\psi_p.
\tag{5}
$$

**定理 1。** 对每个 (2) 中的素数，原完整测度满足
$$
\boxed{T_p\nu_S=\nu_S,\qquad
\nu_S|_{p\mathbf Z_p}=\bar\pi^{-1}[p/\bar\pi^2]_*\nu_S.}
\tag{6}
$$
特别，对全部整数 $m\ge0$，而不只对 principal 正权，
$$
\boxed{\int_{\mathbf Z_p^\times}x^m\,d\nu_S
=\left(1-\frac{\pi^m}{\bar\pi^{m+1}}\right)\Omega_p^m m!s_m.}
\tag{7}
$$
$m=0$ 给准确的单位质量零。式 (6) 是测度恒等式，不留下未知的原点
Dirac 项。证明如下。

## 2. 真实 p-core 保持完整的 34 维 theta 空间

设 $\Gamma=\operatorname{Per}(E,dx/(2y))$。对奇范数 CM 整数 $a$，置
$$
r_a(z)=\frac{\sigma(az)}{\sigma(z)^{Na}}\in K(E),\qquad
\operatorname{div}(r_a)=[a]^*(O)-(Na)(O).
\tag{8}
$$
此处 $Na=a\bar a$。这是带其首项常数 $a$ 的原 division 函数。
在六次 CM 格上，sigma 准周期满足 $\eta_{a\lambda}=\bar a\eta_\lambda$，
所以 (8) 的指数自动因子相消。奇范数时，$a$ 在 $E[2]$ 上可逆，
sigma 的奇半特征也保持，故没有遗留的平坦线丛扭转。

对偶数 $N>0$ 记
$$
\mathcal S_N=\sigma^N L(NO),\qquad \dim_K\mathcal S_N=N.
$$
用同一个 sigma frame 定义不除以 $Na$ 的真实迹
$$
\boxed{\mathscr M_a(\sigma^Nf)=\sigma^N
\operatorname{Tr}_{[a]}\left[\left(\frac{r_{\bar a}}{r_a}\right)^N
f\circ[\bar a]\right].}
\tag{9}
$$
方括号的极点至多为 $N[a]^*(O)$，因为 $f\circ[\bar a]$ 的极点由
$r_{\bar a}^N$ 支付。特征零同源处处无分歧，故迹的极点仅在 $O$、阶至多
$N$。因此 $\mathscr M_a\mathcal S_N\subset\mathcal S_N$。

在普通正式群上，R295 已证明原 Mazur–Tate sigma 就是
$$
\Sigma_p(t)=\sigma(\log_Et)\in t\mathcal O[[t]],\qquad t=-x/y.
\tag{10}
$$
三次 CM 唯一性使二次指数修正恰为零。取整正式同构
$\beta:\widehat{\mathbf G}_m\to\widehat E$，有
$\beta^*(dx/(2y))=\Omega_p\,dT/(1+T)$，且 $\Omega_p$ 是单位。
对任意 $G\in\mathcal S_N$，若 $\nu_G$ 是其原 Amice 测度，则 (5) 的变换是
$$
\mathcal A_{T_pG}(T)=\frac{\bar\pi}p\sum_{\zeta^p=1}
\mathcal A_G\left(\zeta(1+T)^{\bar\pi^2/p}-1\right).
\tag{11}
$$
右边先作为完整根单位平均读取，不能分别将其挠点的正式对数代成零。
$\beta$ 把 $\mu_p$ 送到连通核 $E[\pi]$；在该核上 $[\bar\pi]$ 可逆。
逐支使用真实 division 恒等式
$\Sigma_p([a]P)=\Sigma_p(P)^{Na}r_a(P)$，得到
$$
\boxed{T_pG=\frac{\bar\pi}p\,\mathscr M_\pi G.}
\tag{12}
$$
这是同一个原测度的公式，并非仅凭两个有限空间维数相同认定算子相等。

整个 $\mathcal S_{34}$ 的整基可取
$$
\sigma^{34},\quad \sigma^{34}x^a\ (1\le a\le17),\quad
\sigma^{34}yx^a\ (0\le a\le15).
\tag{13}
$$
它们在 $t$ 参数的首阶互异，准确覆盖 $0,\ldots,34$ 中除 $33$ 外的全部阶；
首系数都是 $\pm1$。每列由 (10) 给整测度。(5) 的限制、支撑除以 $p$、
单位缩放及乘 $\bar\pi$ 都保持整测度。结合 (9)、(12)，再按 (13) 的
互异首阶逐项消元，得
$$
\boxed{T_p\mathcal S_{34}(\mathcal O)\subset\mathcal S_{34}(\mathcal O).}
\tag{14}
$$
所以 (11)、(12) 中表面的 $1/p$ 已经由完整平均支付。

### 2.1 全 Heisenberg 中心与有限相位

为明确 (9) 所用的 theta 结构，对 $v\in N^{-1}\Gamma$ 使用对称 lift
$$
(\mathsf T_vG)(z)=e^{-N\eta_v(z+v/2)}G(z+v).
$$
偶 $N$ 时，它满足
$$
\mathsf T_{v+2\lambda}=\mathsf T_v,\qquad
\mathsf T_v\mathsf T_w
=e^{N(\eta_vw-\eta_wv)/2}\mathsf T_{v+w}.
\tag{15}
$$
两个标准 $N$ 挠生成元的交换子是 primitive 的 $N$ 次根单位；一个生成元
的特征向量由另一个循环成 $N$ 个不同特征值，证明整个表示不可约。
取 $\bar a d_a\equiv1\bmod2N\mathcal O_K$，直接在 (9) 的全部支中换元得
$$
\boxed{\mathscr M_a\mathsf T_v=\mathsf T_{ad_av}\mathscr M_a.}
\tag{16}
$$
模 $2N=68$ 而非仅模 $17$ 的选择保留 (15) 的中心和半相位。
我们在完整 34 维空间中使用 (9)、(12)、(16)，再取实际来源；没有把
裸十七维环面矩阵的标量当作 (12) 的标量。
三处原有限向量及三处相位由 R290 固定，实际 $S$ 的身份由 R297 固定，
而 (2) 中的 Hecke 参数由同一 (3) 固定。

## 3. 原 CM13 线的单重性，及任意普通 p-core 的真正标量性

由于 $p\equiv1\pmod6$，(9) 与全部 $\mu_6$ 自同构交换。
因此它保持 $\mathcal S_{34}$ 中完整的六维不变块
$$
\mathcal H=\operatorname{span}\{\sigma^{34}x^{2+3j}:0\le j\le5\}.
\tag{17}
$$
第 $j=5$ 列有非零原点质量，不能在施加迹之前删去。

令 $\gamma=(7+\delta)/2=4+\omega$。R297 已给出 $\mathscr M_\gamma$ 在
(17) 中的完整矩阵 $M$，包括质量列；其实际来源满足
$MS=-\gamma S$。从该矩阵直接计算得到
$$
\begin{aligned}
\chi_M(X)
&=X^6+\frac{89-17\delta}{2}X^3+\frac{3527-1513\delta}{2}\\
&=(X^3+\gamma^3)(X^3+\omega^2\gamma^3),\\
\chi_M'(-\gamma)&=522-1803\delta\ne0,\qquad
N(522-1803\delta)=27\cdot13^5.
\end{aligned}\tag{18}
$$
所以 $-\gamma$ 的整个本征空间恰为 $KS$，而不只是其中的零质量子空间
一维。还得到一个明确的固定投影
$$
\boxed{\Pi_S=\frac{(M^2-\gamma M+\gamma^2)\,(M^3+\omega^2\gamma^3)}
{522-1803\delta}.}
\tag{19}
$$
它幂等、秩一，像为 $KS$；在当前 $p\ne13$ 处整，因为 R297 矩阵只有
$2,3$ 分母，(18) 的范数只添 $13$。

若 $p\ne13$，真实 $\mathscr M_\pi$ 与 $\mathscr M_\gamma$ 交换。
完整证明可在双纤维中进行：原先两层逆像条件
$aP=z,\ cQ=\bar aP$，在互素核情况下唯一写成
$P=ct,\ Q=\bar at,\ act=z$。两层 sigma 比的中间项
$\sigma(\bar act)/\sigma(c\bar at)$ 准确相消，留下
$\sigma(\bar a\bar ct)/\sigma(act)$。交换 $a,c$ 后是同一个纤维和同一个
frame 比，故没有未定的 Weil 相位。应用于 $a=\pi,c=\gamma$ 即得所需交换。
结合 (17)、(18)，存在真正的标量 $c_p$ 使
$$
T_pS=c_pS.
\tag{20}
$$
由 (14)，左边整；(1)、(10) 给 $S(\log_Et)=t^6+\cdots$。所以直接读取
$t^6$ 的系数，得到
$$c_p\in\mathcal O.\tag{21}$$
这里没有用未知的中央非零，也未把有限维闭合直接当成原点质量零。

## 4. 用独立的完整平方和整性确定标量，顺序无循环

以下只对 principal 正权比较；全部 tame 分支在 §5 才由完整测度式推出。
记
$$
M_m=\Omega_p^m m!s_m,\qquad
e_m=\frac{\pi^m}{\bar\pi^{m+1}},\qquad t_m=(1+p)^m-1,
$$
并令 $G_p(T)$ 为 R295 的原单位 principal Mellin。R295 的两个已经
独立证明的等式是：正权 Katz 插值给
$$
\mathcal K_p(t_m)=\frac{\kappa_0}{s}\Omega_p34^{-m}(1-e_m)^2M_m^2,
\qquad m>0,\quad p-1\mid m;
\tag{22}
$$
整条平方给
$$
\mathcal K_p(T)=\frac{\kappa_0}{s}\Omega_p
(1+T)^{-\log_p\langle34\rangle/\log_p(1+p)}G_p(T)^2.
\tag{23}
$$
式 (23) 的证明仅用整测度的非单位矩赋值至少 $m$，以及实际正权趋向
固定 $p$ 进权的极限；它没有使用 (6)、(7) 或 (20) 的标量。
其中 $s=(1-\omega)^{-1}$，$\kappa_0=48940416$；全部周期与 (3) 相同。
在 $t_m$ 处，因为 $p-1\mid m$，固定单位缩放恰为 $34^{-m}$。
于是 (22)、(23) 相消非零固定因子，直接得到
$$
\boxed{G_p(t_m)^2=(1-e_m)^2M_m^2.}
\tag{24}
$$

另一方面，**现在才**使用已由真实迹证明的 (20)。由 (5) 准确求出
$$
\nu_S|_{p\mathbf Z_p}=c_p\bar\pi^{-1}[p/\bar\pi^2]_*\nu_S,\qquad
G_p(t_m)=(1-c_pe_m)M_m.
\tag{25}
$$
R295 的通常 Selmer/Katz 主猜想比较已证明 $G_p\ne0$。
正权点 $t_{(p-1)p^n}$ 互异并趋于零，故至少一个这样的正权点使
$G_p(t_m)\ne0$。又 (21) 与 $v_p(e_m)=m>0$ 使 $1-c_pe_m$ 是单位，
因此该处 $M_m\ne0$。将 (25) 代入 (24)，约去 $M_m^2$，得到
$$
(1-c_p)e_m\bigl(2-(1+c_p)e_m\bigr)=0.
\tag{26}
$$
最后一因子模 $p$ 为 $2$，是单位；$e_m\ne0$。所以
$$
\boxed{c_p=1.}
\tag{27}
$$
这同时支付了符号。没有在不同权处选择不同平方根，也没有先把未知
p-core 宣称为某个单 Euler 因子后再用它证明自身。

还需覆盖 $p=13$。由 (3)，对 $\gamma=4+\omega$ 有准确的三个单位因子
$$
\chi_2(\gamma)=\omega,\quad\chi_3(\gamma)=-1,\quad
\chi_{17}(\gamma)=\omega^2,\quad\varepsilon(\gamma)=-1.
\tag{28}
$$
所以实际 Frobenius 是 $-\gamma$，或在共轭嵌入下是 $-\bar\gamma$。
$S$ 是偶函数，真实 $\mathscr M_{-\gamma}$ 在 $S$ 上等于
$\mathscr M_\gamma$。R297 给 $\mathscr M_\gamma S=-\gamma S$；其共轭式
相同。因此 (12) 在 $p=13$ 也直接给 (27)。定理 1 的 (6) 得证。

## 5. 全部矩、全部 tame、各个 p 环带和中心质量

从 (6) 直接读出原 p-depletion
$$
\boxed{S^\times(z)=S(z)-\bar\pi^{-1}S(pz/\bar\pi^2).}
\tag{29}
$$
取任何非负整数次矩，得到 (7)，包含全部 tame 同余类以及 $m=0$。
因此无须另外假设非 principal 的 Katz 平方已经选定符号。
不合 $6\mid m$ 的矩两边都为零，由 $S$ 的原 $\mu_6$ 对称性严格保证。

令 $\tau_p(x)$ 为 Teichmüller 部分，$x=\tau_p(x)\langle x\rangle$。
对 $j\in\mathbf Z/(p-1)$、$u\in\mathbf Z_p$ 定义真实全 tame Mellin
$$
\mathcal M_j(u)=\int_{\mathbf Z_p^\times}\tau_p(x)^j\langle x\rangle^u\,d\nu_S(x),
$$
$$
\mathcal M_j^{[n]}(u)=\int_{p^n\mathbf Z_p^\times}
\tau_p(x/p^n)^j\langle x/p^n\rangle^u\,d\nu_S(x).
\tag{30}
$$
测度在 $\mu_6$ 缩放下不变，故 $6\nmid j$ 时 (30) 恒为零。
对允许的分支，迭代 (6) 得到整条解析关系
$$
\boxed{\mathcal M_j^{[n]}(u)=\bar\pi^{-n}\tau_p(\bar\pi)^{-2nj}
\langle\bar\pi\rangle^{-2nu}\mathcal M_j(u).}
\tag{31}
$$
尤其中心及其一阶导数是
$$
\begin{aligned}
\mathcal M_j^{[n]}(0)&=\bar\pi^{-n}\tau_p(\bar\pi)^{-2nj}\mathcal M_j(0),\\
\mathcal M_j^{[n]\prime}(0)&=\bar\pi^{-n}\tau_p(\bar\pi)^{-2nj}
\bigl(\mathcal M_j'(0)-2n\log_p\bar\pi\,\mathcal M_j(0)\bigr).
\end{aligned}\tag{32}
$$
若采用旧记号的 $u\mapsto(p-1)u$，第二行的对数项也须乘 $p-1$。
这里没有删去非 principal 分支可能非零的质量。

principal 分支则由 $S(0)=0$ 与 (6) 准确得到
$$
\boxed{\nu_S(\mathbf Z_p)=\nu_S(p^n\mathbf Z_p)=0,\quad
\mathcal M_0^{[n]}(0)=0\quad(n\ge0).}
\tag{33}
$$
所以其一阶环带式简化为
$\mathcal M_0^{[n]\prime}(0)=\bar\pi^{-n}\mathcal M_0'(0)$。
这是真正从同一个完整测度推出的零传播，不是对一般伴随使用
有限矩阵可逆性传递中央零。

还有整个测度的收敛重构。置 $\kappa=p/\bar\pi^2$、
$\nu_S^\times=\nu_S|_{\mathbf Z_p^\times}$，则
$$
\boxed{\nu_S=\sum_{n\ge0}\bar\pi^{-n}[\kappa^n]_*\nu_S^\times.}
\tag{34}
$$
等式在对所有连续函数积分的意义下成立。事实上有限 $n$ 的剩余项是
$\nu_S|_{p^n\mathbf Z_p}$；由 (6)，其对 $f$ 的积分等于
$\bar\pi^{-n}\int f(\kappa^nx)\,d\nu_S(x)$。
减去 $f(0)\nu_S(\mathbf Z_p)=0$ 后，连续函数的一致连续性使其趋于零。
这也明确说明 (6) 中没有待定的原点补偿。

## 6. 固定 CM7 乘积仍按加法卷积读取

R297 的实际乘积可写为
$$
S=\frac1{28}\sigma(z)^2\sigma(2z)^2
\sigma(\gamma_7z)\sigma(\bar\gamma_7z)\Theta(z)\Theta(2z),\qquad
\Theta=x\sigma^2,\quad\gamma_7=3+\omega.
\tag{35}
$$
对当前普通素数，每一因子都是原整正式级数，缩放 $2,\gamma_7,\bar\gamma_7$
均为单位。因而 (35) 确实给八个固定测度的**加法卷积**，并且除以单位
$28$。若把它们按顺序记成 $\mu_1,\ldots,\mu_8$，完整单位 Mellin 是
$$
\frac1{28}\int_{x_1+\cdots+x_8\in\mathbf Z_p^\times}
\tau_p(x_1+\cdots+x_8)^j
\langle x_1+\cdots+x_8\rangle^u\,d\mu_1(x_1)\cdots d\mu_8(x_8).
\tag{36}
$$
(6) 已控制这个实际卷积结果的全部 p-core；(36) 没有被拆成八个
乘法 Mellin 的乘积。寻找更小的原函数闭合行仍须在此真实加法支持上工作。

## 7. 精确证书和依赖范围

[脚本](../scripts/check-jzero-complete-pcore-and-single-euler.py) 与
[数据](../scripts/check-jzero-complete-pcore-and-single-euler.json)
在 $\mathbf Q[\delta]/(\delta^2+3)$ 中用有理运算读取 R297 的真实矩阵，
证明 (18)、(19) 的全部系数、单重性、幂等性及 (28) 的三处实际因子。
变量素数处的 (9)–(14)、(20)–(27) 和测度结论由上文完整证明；证书
没有把有限个素数的实验当作一般定理。

- [R290 — 原 Schwartz、三处 Weil 向量与全权平方](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)。
- [R295 — 原普通中央平方与全部 Selmer 桥](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)，特别 §§2–5；其整条平方和非零性独立于本篇单 Euler 结论。
- [R297 — 原 CM13 矩阵、唯一质量核及 CM7 乘积](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)。
- [R298 — 精确中央常数与原 Kronecker resolvent](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md)。
- [R266 — 旧普通真实 theta 迹](R266-actual-ordinary-theta-trace-closure-and-paid-source-return.md)、[R282 — 真 p-core 的完整转置](R282-true-prime-core-mellin-transfer-and-original-primitive-orbit.md) 提供原 trace/Amice 规范；本篇在新曲线完整 34 维原格上重新支付了相应公式。
