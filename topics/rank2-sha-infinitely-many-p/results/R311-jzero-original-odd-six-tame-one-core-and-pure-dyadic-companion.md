# R311 — 原奇六块的 Hecke 身份、全 tame-one p-core 与纯倍点伴随

日期：2026-11-13。**状态：六条真实奇 Schwartz 来源、全部有限相位、同一原 $C_{13},C_{15}$ 的精确六线分解、完整普通测度与所有环带、同一中央导数的 Katz 比较，以及消去三条来源后的固定倍点乘积和完整四因子核均已证明。这里的高权 CM 形式不是新的 $E/\mathbf Q$ 秩二候选；非零一阶矩也不替代 $x\log_p x$ 加权导数。主目标仍未完成。**

本篇继续 R307 (36)。其中未知的是
$M_{C,1}'(1/d)$，不是 $M_{C,1}(1/d)$。下面把这个同一个原观察准确分解到六个真实全权来源，并完整保留它的连接卷积。另一个实质简化是
$$
\boxed{C_X=C_1+\frac{C_3}{336b}-\frac{C_5}{840b}
=\frac{\Theta(z)\Theta(2z)^2\sigma(4z)}{2240b},\qquad
\nabla_{\Theta^{17}}C_X=H_1+\frac{H_3}{336b}-\frac{H_5}{840b}.}
\tag{1}
$$
它准确消去三个奇来源，全部零点为固定二幂/三挠点的逆像，并将原连接的逆 $\Theta$ 从完整加法卷积中消去。所有曲线及有限模均仍是 R307 的同一个实际 $b=17$ frame。

## 1. 六个真正的有限 Schwartz 向量

保持 R290 的 $K=\mathbf Q(\delta)$、$\delta^2=-3$、
$\omega=(-1+\delta)/2$、$\alpha=17$、极化 $X=\mathbf Q\delta$。
令 $\rho=-\omega^2$、$\zeta=\zeta_{18}$，固定 $\zeta^3=\rho$、$\zeta^6=\omega$。
在 $\mathbf F_{289}=\mathbf F_{17}[\delta]$ 上仍取
$$
g_0=2+4\delta,\qquad g_0^3=\rho,\qquad g_0^6=\omega.
$$
R290 已付的原有限 Weil 算子记为 $W(g)$。对
$$
I=\{1,5,7,11,13,17\},\qquad \tau_j(g_0)=\zeta^j,
$$
定义精确投影及原向量
$$
\Pi_j=\frac1{18}\sum_{n=0}^{17}\zeta^{-jn}W(g_0^n),
\qquad f_j=18\sqrt{17}\,\Pi_je_1.
\tag{2}
$$
不是从一个未定的特征向量重新选尺度。若 $g_0^n=x_n+y_n\delta$、
$\zeta_{17}=e^{2\pi i/17}$，其全部坐标准确为
$$
\begin{aligned}
f_j(a)={}&\sqrt{17}(\mathbf1_{a=1}-\mathbf1_{a=-1})\\
&-\sum_{\substack{1\le n\le17\\n\ne9}}
\left(\frac{y_n}{17}\right)\zeta^{-jn}
\zeta_{17}^{\frac3{2y_n}\{x_n(a^2+1)-2a\}}.
\end{aligned}
\tag{3}
$$
精确计算在 $\mathbf Q(\zeta_{306})$ 中证明
$$
f_j(1)\ne0,\quad f_j(-a)=-f_j(a),\quad
\overline{f_j(a)}=f_j(a),\quad
W(g_0)f_j=\zeta^jf_j,
$$
$$
\boxed{\|f_j\|^2=18\sqrt{17}\,f_j(1)>0.}
\tag{4}
$$
实性也直接来自 $\overline{W(g)}=W(g^{-1})$，它在原投影 (2) 中与特征值共轭相消。奇性来自 $\tau_j(-1)=-1$。范数是原正交投影范数，未删任何非零陪集。

二处需要两条 **已在同一原四陪集空间中的** 线：
$$
v_\pm=(1,t_\pm,-1,t_\pm),\qquad
t_\pm=\frac{1\pm\sqrt3}{\sqrt2}.
\tag{5}
$$
R290 的完整 $M_\omega$ 给 $v_+$ 特征一、$v_-$ 特征 $\omega$；
$M_*$ 和 $-1$ 同时固定二者。所以原二处 norm-one 群的全部生成元均已支付，而不只是剩余域。其范数分别为 $3\pm\sqrt3>0$。
选择为
$$
v_+\quad(j=5,11,17),\qquad
v_-\quad(j=1,7,13).
\tag{6}
$$
三处仍是原球 $\mathbf1_{3^{-1}\mathbf Z_3}$，其余好地方为标准球。

## 2. 真 Hecke 角色与全权支

设 $a_j=1$ 对 $j=5,11,17$，$a_j=2$ 对 $j=1,7,13$，并令
$r_j=j-9$，指数均按实际字符阶读取。对素于 $34\delta$ 的 $a$ 定义
$$
\varepsilon_j(a)=
\operatorname{Teich}_{\mu_3}(a\bmod2)^{a_j}
(a\bmod\delta)\,(a\bmod17)^{16r_j}.
\tag{7}
$$
末项是模 $17$ 的约化再提升，不是复共轭。
因为 $a_j+r_j\equiv0\pmod3$，对 $u\in\mu_6$ 有
$\varepsilon_j(u)=u^3$。因此对每个 $m\ge0$、$m\equiv1\pmod6$，
$$
\Phi_{j,m}((a))=a^{2m+1}\varepsilon_j(a)^{-1}
\tag{8}
$$
给出原导子 $(34\delta)$ 的真正代数 Hecke 角色，类型为 $(2m+1,0)$。
三个坏位的统一化元值为 $-1,-i,-1$；十七处单位角色为
$z^{16(j-9)}$，二处单位角色为 Teich 的 $a_j$ 次幂，三处单位角色仍为符号。
特别，原 $\alpha=17$ 与全权有限向量不变，没有暗中换 Gaussian。

更直接地，在 R290 的 base splitting 下，十七处特征相对原 $\tau_{12}$ 为
$g^{j-12}$，二处相对特征在 $v_-$ 为 Teich、在 $v_+$ 为一。无穷处第 $m$ Hermite 型的特征为 $\rho^m$。有理 $\rho$ 的乘积关系准确为
$$
m+j+4e\equiv0\pmod6,
\quad e=0\text{ 对 }v_+,\ e=1\text{ 对 }v_-.
\tag{9}
$$
它给 (6) 的同一个 $m\equiv1$ 支。每个本地原向量都满足相应 dichotomy，故 Yang 的原全权平方适用于 (8)。这也证明生成函数只含 $1\bmod6$ 次，未用有限精度零值判断对称性。

令 $\psi$ 是 R290 的实际 $E_{17}$ 角色。存在固定有限阶角色
$$
\xi_j=\Phi_{j,1}/\psi^3,\qquad
\Phi_{j,m}=\xi_j\psi^{2m+1}.
\tag{10}
$$
它的准确阶为十八。在素于导子的主理想上，完整公式很简洁：
$$
\boxed{\xi_j((a))=
\operatorname{Teich}_{\mu_3}(a\bmod2)^{-a_j}
(a\bmod17)^{-16j}.}
\tag{11}
$$
其三处单位分量平凡、在 $\delta$ 上为 $-1$，二、十七处的统一化元值为一；在有理 idèle 上平凡。式 (11) 包含全部有限单位条件和实际理想角色方向。

### 2.1 同 degree 34 的其余三条偶线不是遗漏的椭圆曲线

在同一个原三处球和同一个 $\mathcal O(34O)$ 中，若仍要求 $m\equiv0\pmod6$，则 $v_-$ 的 (9) 只容许 $j=2,8,14$。它们的十七处单位角色为 $z^{16(j-9)}$，阶准确为十八。$E/\mathbf Q$ 的 $j=0$ 六次扭曲在该处的有限单位角色阶至多六，所以这三线不是另一批有理椭圆来源。

同一事实也见于 R300 的完整偶六块：遗漏三特征值满足
$\lambda^3=-\omega^2\gamma^3$，故 $\lambda/\gamma\notin\mu_6$。
原 $v_+$ 的 $j=0,6,12$ 则准确是 R306、R307 的三条曲线，其中只有 $E_{17}$ 是秩二。
这个分类只针对已付的同一来源空间；不同二、三处导子或不同实际线丛的候选必须重新构造原来源。

## 3. 实际六条多项式与 CM13 相位

原系数为
$v_\pm(n\bmod4)f_j(3n\bmod17)$，支撑仍是 $n/102$。
两条 (5) 都满足 R290 的平移恒等式，因此它们的 Jacobi 生成函数从矩形次数 $68$ 下降到同一最大整环格的原次数 $34$。原 Gaussian 仍精确支付 reduced sigma frame。

令 $T$ 满足
$$T^3-3T-1=0.$$
下面两套多项式按升幂 $X^0,\ldots,X^5$ 列出：

| 次数 | $P_+(T;X)$ 的系数 | $P_-(T;X)$ 的系数 |
|---:|---|---|
| $0$ | $-1024(5T^2-T-8)/17$ | $-512T(T-2)$ |
| $1$ | $-256(53T^2-133T-180)/17$ | $-256(8T^2-7T-11)$ |
| $2$ | $-256(66T^2-105T-58)/17$ | $-32(69T^2-3T-253)$ |
| $3$ | $-16(605T^2+338T-1019)/17$ | $-16(20T^2+68T-165)$ |
| $4$ | $-4(308T^2-184T-537)/17$ | $2(176T^2-208T-227)$ |
| $5$ | $-1$ | $-1$ |

设 $\gamma=4+\omega$。实际对应表为

| $j$ | dyadic 线 | $e_j$ | $T_j$ | 原 $M_\gamma$ 特征值 |
|---:|---|---:|---|---|
| $1$ | $-$ | $11$ | $\zeta^{11}+\zeta^{-11}$ | $\gamma\zeta^{11}$ |
| $5$ | $+$ | $1$ | $\zeta+\zeta^{-1}$ | $\gamma\zeta$ |
| $7$ | $-$ | $5$ | $\zeta^5+\zeta^{-5}$ | $\gamma\zeta^5$ |
| $11$ | $+$ | $13$ | $\zeta^{13}+\zeta^{-13}$ | $\gamma\zeta^{13}$ |
| $13$ | $-$ | $17$ | $\zeta^{17}+\zeta^{-17}$ | $\gamma\zeta^{17}$ |
| $17$ | $+$ | $7$ | $\zeta^7+\zeta^{-7}$ | $\gamma\zeta^7$ |

规范为
$$
\boxed{Y_{j,b}=\sigma_b^{34}y_b\,b^5P_\pm(T_j;X/b),
\qquad Y_{j,b}(z)=z+O(z^7).}
\tag{12}
$$
所有系数都在实三次域内，分母只含 $17$。对照原有限 Schwartz，
$\gamma/\bar\gamma\bmod17=g_0^{14}$，其二处分量为 $\omega^2$。
由 R297 的真实定标 $M_\gamma H_1=-\gamma H_1$，相对原十七特征以及 (5) 的两个二处特征给
$$
\lambda_j=-\gamma\omega^2\zeta^{14j}
\begin{cases}1&v_+,\\\omega^2&v_-.
\end{cases}
\tag{13}
$$
它正是表中的 $\gamma\zeta^{e_j}$。将 (12) 代入 R307 的完整奇六矩阵再核定每一列，得到全部相同的简单特征值。
因此 (12) 是 (2)、(5) 原 Schwartz 的真实像，既没有重新选择原角色，也没有按 Taylor 系数拟合来源。

R307 的原点一阶观察在每个简单特征线上非零；或者直接读 (12) 的最高系数 $-1$。这证明六个原 Hermite 一阶值非零。它只支付 (8) 的 weight-four 临界值，尚未支付任何 $p$-adic 中央导数。

## 4. 全权 period 常数的精确有限表达

固定 $b=17$，记 $Y_j=\sum y_{j,m}z^m$，$y_{j,1}=1$，并令
$\Omega=\Omega_{17}>0$、$s=(1-\omega)^{-1}$、$\varpi=s\Omega$。
所有合法权 $m\equiv1\pmod6$ 的真实 Yang 实平方为
$$
\boxed{
\frac{(2\pi/\sqrt3)^mL(\Phi_{j,m},m+1)}{m!\Omega^{2m+1}}
=\kappa_j\,102^{-m}y_{j,m}^2,\qquad \kappa_j>0.}
\tag{14}
$$
这不是给每个权另选一个常数。原 Hermite 变量仍是
$h=\sqrt{51\sqrt3}/(204\pi i)$。由于生成函数和 (12) 都在同一一维来源线上，存在一个固定纯虚非零 $c_j$，使其为 $c_jY_j(\Omega hT)$。合法 $m$ 都为奇数，$c_j^2<0$ 与 $h^{2m}$ 的负号相消；原范数 (4)、(5) 固定 (14) 的唯一正常数。

这里也可不给 $\kappa_j$ 留任何未定义的 period。沿用 R298 的基曲线 $E_1$，
$$
P=\Omega_1s/17,\quad Q=\Omega_1s/(2\delta),
\quad \xi(R)=\zeta(R)-\bar R/A,
\quad c_{11}(R)=-\xi(R)x(R)-y(R).
\tag{15}
$$
最后一式直接是原 Kronecker 函数的 $[zw]$ 系数。
设 $\vartheta_j(c)=c^{16r_j}$ 为 (7) 的十七处角色，定义 **全部原** 有限和
$$
\mathcal R_j=
\sum_{c\in\mathbf F_{289}^\times}\vartheta_j(c)
c_{11}([c]P-Q).
\tag{16}
$$
它包括原 CRT 的所有二、三处信息：$\vartheta_j(2\delta)=1$，
且 $\varepsilon_{j,2/3}(u)\vartheta_j(u)=u^3$，恰与
$c_{11}(uR)=u^{-3}c_{11}(R)$ 相消。因此原 $288\times6$ 陪集和化为 (16)，外面的 $1/6$ 也准确消去。
R298 的 Kronecker 展开在 $m=1$ 给
$$
\mathcal E_{j,1}^{\rm CM}
=-\frac{17^{1/2}}{34\delta}\mathcal R_j.
$$
因 $s^3=\delta/9$，完整常数就是
$$
\boxed{\kappa_j=-\frac{\sqrt{17}}3\,\mathcal R_j.}
\tag{17}
$$
这是一个指定固定挠点上的精确有限代数表达式。其代数性不依赖周期猜测：R298 已用原 $17$ 除法多项式的对数导数给出 $\xi(P)$ 的有理式；$Q$、其 reduced $\zeta$ 值及全部加法分支也都已付。因 (12) 的一阶值非零，Yang 平方使 (17) 正且非零。

合法奇权的 CM period 换算和 R298 的偶权不同。这里
$s^{2m}=-\omega^2 3^{-m}$，所以
$$
\boxed{
\mathcal E_{j,m}^{\rm CM}
=-\omega(1-\omega)\kappa_j\,34^{-m}y_{j,m}^2.
}
\tag{18}
$$
固定的 $-\omega$ 必须保留；不能直接套用偶权参考的常数。

## 5. 同一个 $C_{13},C_{15}$ 的全部六线分解

下面所有 $C_k,C_{13},C_{15}$ 都是 R307 中已经固定的原 companion。
定义两组系数
$$
\begin{array}{ll}
A_{13,+}(T)=-\dfrac{161T^2+1469T-4984}{12827808},
&A_{13,-}(T)=-\dfrac{17(8T^2-T-16)}{1603476},\\
A_{15,+}(T)=\dfrac{763T^2-2507T+3136}{20321280},
&A_{15,-}(T)=-\dfrac{17(8T^2-T-16)}{1016064}.
\end{array}
\tag{19}
$$
令 $A_{1k,j}=A_{1k,\pm}(T_j)$，按 (6) 取符号。原完整分解为
$$
\boxed{C_{1k,b}=\frac1b\sum_{j\in I}A_{1k,j}Y_{j,b},
\qquad k=3,5.}
\tag{20}
$$
六个系数都非零；这个断言由原列的精确求解证明，不是从 ambient 维数推出。
原点质量也直接保持：
$$
\frac1b\sum_jA_{13,j}=\frac{37}{33936b}=-a_{13},
\qquad
\frac1b\sum_jA_{15,j}=\frac{37}{53760b}=-a_{15}.
\tag{21}
$$
两个 $T_\pm$ 的极边界在这个**完整和**中相消。单条 $Y_j$ 在 $T_\pm$ 非零，故不能对它逐条应用“全纯 $\nabla_F$”后再丢掉极项。

### 5.1 真正消去一半来源的固定行

式 (19) 给 $101A_{13,-}-64A_{15,-}=0$，因此 (1) 的同一个来源准确为
$$
\boxed{C_X=-\frac1{10080b}
\sum_{j=5,11,17}(T_j^2+T_j-8)Y_{j,b}.}
\tag{22}
$$
三个 $T_j$ 是同一实三次多项式的全部根，
$\operatorname{Tr}(T)=0$、$\operatorname{Tr}(T^2)=6$，所以
$C_X'(0)=1/(560b)$，并没有因投影而变成零质量。

对原 $\mathcal L_b$ 直接计算，其多项式为
$$
R_X(X)=-\frac{(X-8b)^2(X^2+20bX-8b^2)}{560b}.
\tag{23}
$$
准确的倍点 sigma 符号为
$$
\sigma(4z)=-4y(X^2+20bX-8b^2)\sigma(z)^{16},
\qquad
\Theta(2z)=x(X-8b)\sigma(z)^8.
\tag{24}
$$
代入 $C_X=\sigma^{34}x^3yR_X$ 就得 (1)。首项 $4z$ 独立核定 (24) 的负号及 $C_X'(0)>0$。若忽略 $y=-z^{-3}+\cdots$ 的原支，会得到错误符号。

## 6. 六条原测度的完整普通 p-core

固定 $p>7$、$p\equiv1\pmod3$，仍使用 R300 的实际
$$
\pi=\psi(\mathfrak p),\quad\bar\pi=\psi(\bar{\mathfrak p}),
\quad v_p(\pi)=1,\quad\pi\bar\pi=p,
$$
以及共同 $\Omega_p$。令 $\nu_j$ 的 Amice 变换为
$Y_j(\Omega_p\log(1+Z))$。由 (12) 仅含 $17$ 分母和 R300 的完整整 $\mathcal S_{34}$，每个 $\nu_j$ 都整，且一阶矩为 $\Omega_p$。

**定理。** 对每个这样的普通素数，完整测度恒等式为
$$
\boxed{
T_p\nu_j=\xi_j(\mathfrak p)\nu_j,
\qquad
\nu_j|_{p\mathbf Z_p}
=\frac{\xi_j(\mathfrak p)}{\bar\pi}
[p/\bar\pi^2]_*\nu_j.}
\tag{25}
$$
这里 $T_p=\bar\pi[\bar\pi^2]_*\psi_p$ 是 R300 的同一个真实算子；
标量不是另选的有限矩阵规范。

**证明。** R300 (9)–(16) 已在全部 $34$ 维空间证明真实 division 迹、整性和模 $68$ 的全 Heisenberg 协变。其不可约性使真实迹与相同 Heisenberg 作用的有限 Weil 算子只差一个公共标量。R300 已由原 $H_1$ 将该公共标量定标成 $T_pH_1=H_1$。

现在取与 $H_1$ 的比。置
$u_2=\operatorname{Teich}_{\mu_3}(\pi\bmod2)$、
$t_{17}=(\pi\bmod17)^{48}$。十七处真实比是
$$
(\pi/\bar\pi)^{j-12}
=(\pi\bmod17)^{-16j}t_{17}^{4}.
$$
因为 $\pi$ 是实际 $\psi(\mathfrak p)$，R300 的原 $\varepsilon(\pi)=1$ 给
$t_{17}^4=u_2^{-1}$。二处的完整比在 $v_+$ 为一，在 $v_-$ 为 $u_2^{-1}$：这是 (5) 在 $\mu_3,-1,g_*$ 全部生成元上的比，故包含二处 pro-two 和半相位。三处原向量相同。合起来准确为
$$
u_2^{-a_j}(\pi\bmod17)^{-16j}=\xi_j((\pi)),
$$
即 (11)。这在已付的全 $34$ 维 Heisenberg 中进行，不是把裸十七维矩阵的未知标量忽略掉。
最后用 R300 的 $T_p=\bar\pi\mathscr M_\pi/p$ 与原测度定义，即得 (25)。
例如在原范数十三素理想上 $\pi=-\gamma$，完整同时 pull/trace 满足
$\mathscr M_{-\gamma}=\mathscr M_\gamma$，所以实际比是
$-\zeta^{e_j}=\xi_j(\mathfrak p)$；不能只在奇函数上加一个未付的单边负号。$\square$

因此对**所有**整数 $m\ge0$，
$$
\boxed{\int_{\mathbf Z_p^\times}x^m\,d\nu_j
=\left(1-\xi_j(\mathfrak p)
\frac{\pi^m}{\bar\pi^{m+1}}\right)\Omega_p^m m!y_{j,m}.}
\tag{26}
$$
只有 $m\equiv1\pmod6$ 的矩可非零，但测度恒等式 (25) 还保全部 tame 分支、原点和各环带，不留下未知 Dirac 项。

## 7. 原 tame-one 行、整条 Katz 平方及导数

令 $d=p-1$、$c_{j,p}=\xi_j(\mathfrak p)$，定义这个同一个移权行
$$
\mathcal U_j(u)=
\int_{\mathbf Z_p^\times}x\langle x\rangle^{du}\,d\nu_j(x)
=M_{Y_j,1}(u+1/d).
\tag{27}
$$
它的中心是实际**一阶矩**，不是常数矩：
$$
\boxed{\mathcal U_j(0)=\Omega_p
\left(1-c_{j,p}\frac{\pi}{\bar\pi^2}\right)\in\mathcal O^\times.}
\tag{28}
$$
若 $\nu_j^{[n]}=(x\mapsto x/p^n)_*(\nu_j|_{p^n\mathbf Z_p^\times})$，则 (25) 的全部环带为
$$
\boxed{\mathcal U_j^{[n]}(u)=
c_{j,p}^n\bar\pi^{-3n}
\langle\bar\pi\rangle^{-2ndu}\mathcal U_j(u),}
\tag{29}
$$
$$
(\mathcal U_j^{[n]})'(0)=
c_{j,p}^n\bar\pi^{-3n}
\{\mathcal U_j'(0)-2nd\log_p(\bar\pi)\mathcal U_j(0)\}.
\tag{30}
$$
这样 $\mathcal U_j'(0)=d\int x\log_p\langle x\rangle\,d\nu_j$ 和它的一阶质量已经准确区分；不能用 (28) 的非零替换它。

取 R295 同一 primitive Katz 规范，沿真正的角色
$$
\nu_{j,m}=\Phi_{j,m}\operatorname N^{-m},
\qquad m=1+du,
$$
记其解析函数为 $\mathscr L_j(u)$。它的无限型是 $(m+1,-m)$。原辅助理想 $(5)$ 仍可用：$\xi_j((5))=1$，且 $\nu_{j,m}((5))=-5$，原 smoothing 值仍是固定 $-30$，对所有这里的 $p$ 为单位。

把 (18) 代入 Katz 的正权插值，并保两个相等的 Euler 因子，得到整条精确平方
$$
\boxed{\mathscr L_j(u)=
\frac{-\omega(1-\omega)\kappa_j\Omega_p}{34}
\langle34\rangle^{-du}\mathcal U_j(u)^2.}
\tag{31}
$$
可以像 R295 一样用稠密的正整数权证明：在每个 $p$-进邻域内令正整数 $m$ 趋于无穷，非单位矩由有界性趋于零，Euler 项趋于一，正权公式遂延拓成 (31)。或者使用已独立由全 Heisenberg 证明的 (25)、(26) 后直接作同一解析延拓。这里没有以 (31) 猜测 (25) 的符号。

因 (28) 非零，对数导数准确为
$$
\boxed{\mathcal U_j'(0)=\frac{\mathcal U_j(0)}2
\left\{\frac{\mathscr L_j'(0)}{\mathscr L_j(0)}
+d\log_p34\right\}.}
\tag{32}
$$
式 (32) 是原 high-weight Hecke 支的完整 period 比较；它没有声称右边的 Katz 对数导数已知或为零。

## 8. 准确返回 R307 的同一中央导数

固定 $k=3$ 或 $5$，记 $C=C_{1k}$、$a=a_{1k}$，并保持
$q=F'/F$、$F=\Theta^{17}$。由 (20)，
$$
M_{C,1}(u+1/d)=\frac1b\sum_j A_{1k,j}\mathcal U_j(u).
$$
R307 的完整卷积项仍为
$$
\mathcal K_{q,C}(u)=\iint
\mathbf1_{x+y\in\mathbf Z_p^\times}\,
\langle x+y\rangle^{du}\,d\nu_q(x)d\nu_C(y).
\tag{33}
$$
于是同一个原导数准确变成
$$
\boxed{\begin{aligned}
M_{H_1}'(0)-aM_{H_k}'(0)
={}&\frac1{2b}\sum_j A_{1k,j}
\left(1-c_{j,p}\frac{\pi}{\bar\pi^2}\right)
\left\{\frac{\mathscr L_j'(0)}{\mathscr L_j(0)}+d\log_p34\right\}\\
&-\mathcal K_{q,C}'(0).
\end{aligned}}
\tag{34}
$$
所有 $H_k$ 的 Euler、共同 period 和质量仍是 R307、R308 的各自实际量。六条 $\mathscr L_j$ 是这里刚支付的原六条高权支；没有把它们当作额外的秩二曲线。

一阶质量也没有隐藏在 (34) 中。在未微分的式子中，
$$
\mathcal K_{q,C}(0)=
\frac1b\sum_jA_{1k,j}
\left(1-c_{j,p}\frac{\pi}{\bar\pi^2}\right)
-\{M_{H_1}(0)-aM_{H_k}(0)\}.
\tag{35}
$$
原 $M_{H_1}(0)=0$，但其他质量不能一起删去。

## 9. 纯倍点行的完整四因子核

对 (1) 可以进一步付清 (33) 中的逆 frame。R300 的原 Mazur–Tate sigma 整性也给
$\nu_\sigma$ 和 $\nu_\Theta$ 两个有界测度，Amice 变换分别为
$\sigma(\Omega_p\log(1+Z))$、$\Theta(\Omega_p\log(1+Z))$。
式 (1) 是完整加法卷积
$$
\nu_{C_X}=\frac1{2240b}
\nu_\Theta*[2]_*\nu_\Theta*[2]_*\nu_\Theta*[4]_*\nu_\sigma.
\tag{36}
$$
又 $q=17\Theta'/\Theta$，所以在同一个实际乘积里
$$
qC_X=\frac{17}{2240b}
\Theta'(z)\Theta(2z)^2\sigma(4z).
\tag{37}
$$
逆 $\Theta$ 已经在特征零完整来源中准确消去，不是对 Mellin 值作除法。

令
$$
\nu=\nu_\Theta\otimes\nu_\Theta\otimes\nu_\Theta\otimes\nu_\sigma,
\qquad y=x_1+2x_2+2x_3+4x_4.
$$
则 (1)、(36)、(37) 给出完整测度身份
$$
\boxed{\nu_{H_1}+\frac{\nu_{H_3}}{336b}-\frac{\nu_{H_5}}{840b}
=\frac1{2240b\Omega_p}
y_*\bigl[(y-17x_1)\nu\bigr].}
\tag{38}
$$
全部单位群 Mellin 行及中央导数是
$$
M_{H_1}(u)+\frac{M_{H_3}(u)}{336b}-\frac{M_{H_5}(u)}{840b}
=\frac1{2240b\Omega_p}
\int_{y\in\mathbf Z_p^\times}(y-17x_1)\langle y\rangle^{du}\,d\nu,
\tag{39}
$$
$$
\boxed{M_{H_1}'(0)+\frac{M_{H_3}'(0)}{336b}-\frac{M_{H_5}'(0)}{840b}
=\frac d{2240b\Omega_p}
\int_{y\in\mathbf Z_p^\times}(y-17x_1)\log_p\langle y\rangle\,d\nu.}
\tag{40}
$$
这是由四个固定低 degree 原 sigma/$\Theta$ 因子给出的精确核；求和变量 $y$ 和单位条件均保留，不能把 (39) 改成四个乘法 Mellin 的积。对应 (22) 的三条真高权来源也同时保留，因此可以在同一有限图中比较，而无需添加一条未经授权的中央零。

与 R309 的 conductor 平方根还有准确固定身份
$$
C_D=\frac14\sigma(z)^2\sigma(4z)\Theta(z)^4\Theta(2z)
=\frac{560b\,x^2}{X-8b}C_X.
\tag{41}
$$
$C_D=z^3+\cdots$，属于 $\rho^3$ 型，和本篇的 tame-one 原块不同。式 (41) 是实际共同来源接口，不会将 $C_D$ 或 $C_D^2$ 的中央行自动加入 (40)。

## 10. 可复现证书与仍需支付的原观察

`scripts/check-jzero-odd-original-schwartz-and-full-tame-one.py/.json` 给出 91 项精确检验：六个 $\mathbf Q(\zeta_{306})$ 原有限向量、完整范数/实性/奇性、实际 CM13 相位与全部多项式、实三次域表达、同一 $C_{13},C_{15}$ 的全部六线分解、三线消去、一般 $b$ 的原连接、固定倍点乘积及全部质量。实际测度/全权证明是上面的原 theta 迹、Schwartz 与 Katz 推导，不由有限样本替代。

本篇把 R307 的未知一阶观察转成 (34)，并对纯倍点行进一步得到无逆 frame 的 (40)。要推出主目标，仍须控制这些同一观察中的 Katz 对数导数或四因子原核；(28) 的非零第一矩不作这个替代。原函数方程也没有在此固定 tame-one 支上给一个未经证明的奇偶关系。

依赖：[R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)、
[R295](R295-jzero-original-ordinary-central-square-and-full-selmer-bridge.md)、
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、
[R298](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md)、
[R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
[R306](R306-jzero-three-sextic-original-local-data-and-full-weight-squares.md)、
[R307](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)、
[R308](R308-jzero-rank-zero-reference-full-pcore-and-central-masses.md)、
[R309](R309-three-original-jzero-quartic-conductor-and-paid-q2-image.md)。
Yang 1997 Theorems 2.6、2.15 和 Yang 1999 Lemma 1.1、Proposition 1.2 使用 R290 已付的同一原规范；本文重新支付了所有改变的二、十七处特征。原文为
<https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf>、
<https://people.math.wisc.edu/~tonghaiyang/rank.pdf>。
Kronecker 指标使用 Bannai–Kobayashi, Duke Math. J. 153 (2010), Theorem 1.17；
Katz 的真实晶格 period 规范使用 R295 已核的 Castella–Wan Theorem 2.4 与 Remark 2.2，未换成 $\Omega/(2\pi i)$。
