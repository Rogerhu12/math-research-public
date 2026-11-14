# R307 — 三条原 sextic 来源、两个精确秩零中央值与完整一阶伴随

日期：2026-11-13。**状态：三条实际原来源的有理多项式、全 CM13 身份、两个秩零参考的精确中央值与全权常数、同一连接的一阶伴随及全部原点/挠点边界、普通卷积和惰性完整移权式均已证明。原目标仍是 $E_{17}$ 的无穷多个素数；本篇没有把秩零中央值非零等同于其中央导数已知。**

R306 已支付三个 Hecke 角色的全部有限局部数据、同一个 $\alpha=17$、原 Schwartz 向量和全权 Yang 平方。本篇实际识别其三条截面，得到
$$
\boxed{\frac{L(E_{4913},1)}{\Omega_{4913}}=3,
\qquad \frac{L(E_{1419857},1)}{\Omega_{1419857}}=6.}
\tag{1}
$$
这里 $E_D:y^2=x^3+D$，$\Omega_D>0$ 始终是微分 $dx/(2y)$ 的正实 primitive period。两式由完整导子 $2\delta\cdot17$ 的原 Kronecker 和精确算出，不依赖高精度认数或 BSD。它们给两条真实秩零参考；只有 $E_{17}$ 是本篇的秩二目标。

## 1. 同一个原 degree 34 模中的三条实际线

固定
$$
\delta=\sqrt{-3},\quad\omega=(-1+\delta)/2,
\quad\gamma=4+\omega=(7+\delta)/2,
\quad E_b:y^2=x^3+b,
$$
并用 $x=z^{-2}+\cdots$、$y=-z^{-3}+\cdots$、$\sigma=z+\cdots$ 的规范。写 $X=x^3$。实际六维 $\mu_6$ 不变截面空间是
$$
\mathcal H^+=\sigma^{34}x^2\mathbf Q[X]_{\le5}.
\tag{2}
$$
这是 R292、R297 的原 $\mathcal O(34O)$，包含第六列的原点质量。

三条来源是 $H_{k,b}=\sigma^{34}x^2P_{k,b}(X)$，其中
$$
\begin{aligned}
P_{1,b}={}&X^4-\frac{53b}{7}X^3-\frac{12b^2}{7}X^2
-\frac{80b^3}{7}X-\frac{128b^4}{7},\\
P_{3,b}={}&X^5-208bX^4+400b^2X^3+8128b^3X^2
+12032b^4X-2048b^5,\\
P_{5,b}={}&X^5+272bX^4-272b^2X^3-14912b^3X^2
-6784b^4X+1024b^5.
\end{aligned}
\tag{3}
$$
全部系数均为精确有理数。其质量和实际 CM13 特征如下：

| 原曲线 | 共同框中的来源 | 原点首项 | 原 $M_\gamma=[\gamma]_*[\bar\gamma]^*$ 特征值 |
|---|---|---|---|
| $E_{17}$ | $H_{1,17}$ | $z^6$ | $-\gamma$ |
| $E_{17^3}$ | $H_{3,17}$ | $1$ | $-\gamma\omega^2=1+2\delta$ |
| $E_{17^5}$ | $H_{5,17}$ | $1$ | $-\gamma\omega=(5-3\delta)/2$ |

**原来源识别。** R306 的真实十七处角色依次为 $g^{12},1,g^6$，而
$\gamma/\bar\gamma\bmod17=g_0^{14}$。二、三处向量及整个 Heisenberg 交织子的公共定标相同，所以相对特征值准确为 $\omega^{k-1}$。R297 的完整六维矩阵给第一条 $-\gamma$；将 (3) 的三个列向量代入同一个矩阵，分别得到表中三个特征值，且三个特征空间都恰为一维。原 Schwartz 向量非零，故这些列就是其真实像。没有仅凭角函数形状识别曲线。

表中第二、三行已经作了固定尺度变换。若 $D=17^k$、$\nu_k=17^{(k-1)/6}>0$，则
$$
H_{k,17}(z)=H_{k,D}(z/\nu_k),\qquad
\Omega_D=\Omega_{17}/\nu_k\quad(k=3,5).
\tag{4}
$$
这是 $x_b(z)=b^{1/3}x_1(b^{1/6}z)$、$\sigma_b(z)=b^{-1/6}\sigma_1(b^{1/6}z)$ 作用于完整齐次截面的结果。后面的共同连接全部用 $b=17$。使用各曲线自己的 Euler 因子时仍须用其实际 $\psi_k$；(4) 不把它们换成 $\psi_1$。

## 2. 完整导子上的零权 Kronecker 和

先在 $E_1$ 上计算。令
$$
s=(1-\omega)^{-1},\quad \varpi=\Omega_1s,
\quad \Gamma_1=\varpi\mathcal O_K,
\quad A=\operatorname{area}(\mathbf C/\Gamma_1)/\pi,
$$
以及 $\xi(z)=\zeta(z)-\bar z/A$。R298、R302 已用实际 period 分支确定
$$
P=\varpi/17,\qquad Q=\varpi/(2\delta)=(2\omega,3),
\qquad \xi(Q)=-\omega^2.
\tag{5}
$$
零权 Kronecker 展开给 $e^*_{0,1}(R)=\xi(R)$。记
$\chi_{17}(a)=(a\bmod17)^{48}\in\mu_6$；这里是约化，不是复共轭。
记 $\varepsilon_{\rm base}$ 为 R302 中 $y^2=x^3+1$ 的有限角色（区别于本篇 $k=1$ 的目标）。原完整有限角色是
$$
\varepsilon_k(a)=\varepsilon_{\rm base}(a)\chi_{17}(a)^k,
\qquad \psi_k((a))=a\varepsilon_k(a)^{-1}.
\tag{6}
$$
和 R298 一样，先在绝对收敛区间作陪集分解，再解析延拓到零权，得到
$$
\frac{L(\psi_k,1)}{\varpi}
=\frac1{6\cdot34\delta}
\sum_{a\in(\mathcal O_K/(34\delta))^\times}
\varepsilon_k(a)\,\xi(\varpi a/(34\delta)).
\tag{7}
$$
取 CRT 坐标 $a\equiv2\delta c\pmod{17}$、$a\equiv u\pmod{2\delta}$，其中 $u\in\mu_6$。由于 $k$ 为奇数，三条角色都满足
$$
\varpi a/(34\delta)=[c]P-[u]Q,
\qquad \varepsilon_k(a)=-u\chi_{17}(c)^k.
$$
又 $\xi(uR)=u^{-1}\xi(R)$、$\chi_{17}(u)=1$。原六个二、三处平移准确消掉 (7) 的 $1/6$，所以
$$
\frac{L(\psi_k,1)}{\varpi}
=-\frac{\mathscr R_k(P)}{34\delta},\qquad
\mathscr R_k(P)=\sum_{c\in\mathbf F_{289}^\times}
\chi_{17}(c)^k\xi([c]P-Q).
\tag{8}
$$
这里保留了全部 $288$ 个原十七处分量和原小坏位的符号。

### 2.1 六个单位的迹只有一个简单有理函数

令 $t=x(P)^3$。由 $\zeta$ 加法式，
$$
\xi([u]P-Q)=u^{-1}\xi(P)+\omega^2+
\frac{u^{-3}y(P)+3}{u^{-2}x(P)-2\omega}.
$$
在 $u$ 和 $-u$ 间配对，$\xi(P)$ 与 $y(P)$ 项全部准确抵消。余下
$$
\boxed{R_0(t):=\sum_{u\in\mu_6}\xi([u]P-Q)
=6\omega^2+\frac{72\omega^2}{t-8}
=6\omega^2\frac{t+4}{t-8}.}
\tag{9}
$$
这一步消掉的是已完整求和的六个分支；没有把单个 $\xi$ 的非恒定部分当成常数。

### 2.2 真 CM7 轨道与精确中央值

标准除法递归给
$$
\Psi_{17}(x)=17P_{48}(x^3),\qquad\deg P_{48}=48.
$$
此多项式无重根。取 $\gamma_7=2-\omega=(5-\delta)/2$，它在 $\mathbf F_{289}^\times$ 中的准确阶为 $288$，而 $\chi_{17}(\gamma_7)=-\omega^2=:\lambda$。设
$$
c=-\frac{2+6\delta}{7},\quad
B(t)=t^2+(12-28c)t+7c^2-24c,
\quad
\Phi(t)=\frac{tB(t)^3}{\gamma_7^6(t+c)^6}.
\tag{10}
$$
这是 $[\gamma_7]$ 的实际 Weber 作用，由真实 $\sigma(\gamma_7z)/\sigma(z)^7$ 推出；它保 $P_{48}=0$。因此 (8) 正好是原四十八项
$$
\mathscr R_k(t)=\sum_{j=0}^{47}\lambda^{kj}R_0(\Phi^j(t))
\quad\text{in }K[t]/(P_{48}).
\tag{11}
$$
全部分母都由精确 gcd 证明可逆。按 (10) 做四十八次 Horner 复合，得到原有限代数中的恒等式
$$
\boxed{\mathscr R_1=0,\qquad
\mathscr R_3^6=\frac{3^6\,102^6}{17^3},\qquad
\mathscr R_5^6=\frac{6^6\,102^6}{17^5}.}
\tag{12}
$$
证书从除法递归重建 $P_{48}$，并重建 (10)，不读取暂存工作结果；另外核对四十八项闭合及
$\mathscr R_k\circ\Phi=\lambda^{-k}\mathscr R_k$。

因为 $\Omega_{17^k}=\Omega_1/17^{k/6}$，(8) 给
$$
\frac{L(E_{17^k},1)}{\Omega_{17^k}}
=-\frac{17^{k/6}s}{34\delta}\mathscr R_k,
\qquad -34\delta/s=102\omega^2.
\tag{13}
$$
故其六次方依次为 $0,729,46656$。R306 的真实实 Schwartz 平方在 $m=0$ 有正常数，且后两条非零。因此实值取正的六次根，恰为 (1)。这同时给 $L(E_{17},1)=0$ 的独立零权核定。

Coates–Wiles 关于 CM 椭圆曲线的已发表非零中央值定理，于是给
$$
\operatorname{rank}E_{4913}(\mathbf Q)
=\operatorname{rank}E_{1419857}(\mathbf Q)=0.
\tag{14}
$$
这不是以数值解析秩代替代数秩，也没有借用 BSD。

## 3. 两参考的全权常数与共同 period

将 $H_{k,17^k}(z)=\sum h_{k,m}z^m$ 规范成 $h_{k,0}=1$。R306 的 Hermite 变量、Gaussian 和同一个 $h=\sqrt{51\sqrt3}/(204\pi i)$ 全部固定。令 $\kappa_3=3$、$\kappa_5=6$。把 $m=0$ 的 (1) 代入原 Yang 正常数，便将其唯一尺度定标；对每个 $6\mid m$ 有
$$
\boxed{
\frac{(2\pi/\sqrt3)^m L(\psi_k^{2m+1},m+1)}
{m!\Omega_{17^k}^{2m+1}}
=\kappa_k\,102^{-m}h_{k,m}^2,\qquad k=3,5.}
\tag{15}
$$
写 $\varpi_k=s\Omega_{17^k}$，因 $s^{2m}=3^{-m}$，完整 CM period 版本为
$$
\boxed{
\frac{(2\pi/\sqrt3)^m L(\psi_k^{2m+1},m+1)}
{m!\varpi_k^{2m+1}}
=(1-\omega)\kappa_k\,34^{-m}h_{k,m}^2.}
\tag{16}
$$
换到 (4) 的共同 $b=17$ frame，系数乘 $\nu_k^{-m}$，period 乘 $\nu_k$。所以 (15)、(16) 的中央常数分别变为
$$
\frac{\kappa_k}{\nu_k},\qquad
(1-\omega)\frac{\kappa_k}{\nu_k},
\tag{17}
$$
权因子仍是 $102^{-m}$ 和 $34^{-m}$。不能只换权而漏掉中央质量的 (17)。目标第一条 $H_{1,17}(0)=0$，其全权常数仍是 R298 的 $48940416$，不是本节的零权值零。

## 4. 同一原点连接与真实全纯域

以后所有来源都放在共同 $E_b$，最后取 $b=17$。固定
$$
\Theta=x\sigma^2,\qquad F=\Theta^{17}=\sigma^{34}x^{17},
\qquad \nabla_F=\partial_z-F'/F.
\tag{18}
$$
$F(0)=1$；它作为共同 frame 保留，尚未被声称是另一条秩零原来源。

令 $\rho=-\omega^2$。$\sigma(\rho z)=\rho\sigma(z)$、$x(\rho z)=\rho^{-2}x(z)$、$y(\rho z)=\rho^{-3}y(z)$。$\rho$ 型的整个六维奇截面空间准确为
$$
\mathcal H^{\rm odd}=\sigma^{34}y\mathbf Q[X]_{\le5}.
\tag{19}
$$
对一般 $C_P=\sigma^{34}yP(X)$，直接微分完整商 $C_P/F=yx^{-17}P(X)$，得到
$$
\boxed{\nabla_FC_P=\frac{\sigma^{34}}x
\{6X(X+b)P'(X)-(31X+34b)P(X)\}.}
\tag{20}
$$
设 $T_\pm=(0,\pm\sqrt b)$。若 $P(0)\ne0$，(20) 在这两个点各有真实简单极，主部为
$$
-\frac{34bP(0)\sigma(z)^{34}}{x(z)}.
\tag{21}
$$
其他来源项不能无条件替它付掉这两个极。

所以 (20) 的准确全纯域是 $P=XR$、$\deg R\le4$。记
$$
C_R=\sigma^{34}x^3yR(X),\qquad
\mathcal L_bR=6X(X+b)R'-(25X+28b)R.
$$
则
$$
\boxed{\nabla_FC_R=\sigma^{34}x^2\mathcal L_bR.}
\tag{22}
$$
$C_R$ 在两个 $T_\pm$ 至少三阶零，正好支付 (18) 的连接极；在原点则一般从一次项开始。这个原点质量必须进入完整 Mellin 移权。

## 5. 三个实际余类、全部伴随和原点质量

先取 $b=1$。$\mathcal L_1$ 的第 $j$ 列只有两项：
$$
\mathcal L_1(X^j)=(6j-28)X^j+(6j-25)X^{j+1},
\qquad0\le j\le4.
\tag{23}
$$
故此 $6\times5$ 矩阵秩五。其原始整余核为
$$
\ell=(-6175,6916,-8008,9856,-14080,56320).
\tag{24}
$$
具体地，对 $\eta_P=x^{-15}P(X)\,dz$，唯一约化为
$$
\eta_P=d(yx^{-14}R(X))+c(P)\,dz,
\qquad c(P)=\frac{\ell(P)}{56320}.
\tag{25}
$$
这是已经相乘后的同一原来源 $H_P/F$；不是把某个裸微分当成 $H_P$。余类方向是实际 $dz$。其两个 $T_\pm$ 留数均为零，也可由 $x$ 的指数模三直接看出。

三条来源的准确数据为

| $k$ | $c_{k,1}$ | $R_{k,1}$ 的升幂系数 $R_0,R_1,R_2,R_3,R_4$ |
|---:|---|---|
| $1$ | $-8991/12320$ | $32/49,-120/539,801/2156,5911/21560,-8991/12320$ |
| $3$ | $73629/110$ | $512/7,-48512/77,18492/77,-135598/385,73519/110$ |
| $5$ | $11664/11$ | $-256/7,26944/77,39768/77,-49604/77,11653/11$ |

一般 $b$ 时，
$$
\begin{aligned}
R_{1,b}(X)&=b^3R_{1,1}(X/b),&c_{1,b}&=-\frac{8991}{12320b},\\
R_{k,b}(X)&=b^4R_{k,1}(X/b),&c_{k,b}&=c_{k,1}\quad(k=3,5).
\end{aligned}
\tag{26}
$$
令 $C_k=\sigma^{34}x^3yR_{k,b}(X)$。全部关系准确为
$$
H_k=\nabla_FC_k+c_{k,b}F,
\qquad C_k'(0)=H_k(0)-c_{k,b}.
\tag{27}
$$
特别，(27) 中 $F$ 的质量和完整导数均还在。

两种完全消去同一个 $F$ 的真实选择是
$$
\begin{aligned}
a_{13}&=-\frac{37}{33936b},&C_{13}&=C_1-a_{13}C_3,\\
a_{15}&=-\frac{37}{53760b},&C_{15}&=C_1-a_{15}C_5.
\end{aligned}
$$
它们满足
$$
\boxed{H_1-a_{1j}H_j=\nabla_FC_{1j},\qquad
C_{1j}'(0)=-a_{1j},\quad j=3,5.}
\tag{28}
$$
此外 $160H_3-101H_5$ 也有实际全纯一阶伴随，其原点质量是 $59$，不是零。

整性也可直接读出：表中的分母只含 $2,5,7,11$ 和固定 $b$；$c_3=3^6\cdot101/(2\cdot5\cdot11)$、$c_5=2^4\cdot3^6/11$。因此所有普通 $p>7$ 的这套约化都整，且两个参考余类都是单位。惰性 $p>17$ 时 $a_{15}$ 始终整；$a_{13}$ 在 $p=101$ 必须改用另一行，不能掩盖该分母。

## 6. 真奇 CM13 块与两个不能省去的边界

为检查 (28) 能否在真实有限图中闭合，我们计算了 (19) 的整个 $M_\gamma$，没有只投影其中五列。规范 $b=1$。设
$$
q_\gamma(x)=\frac{\sigma(\gamma z)}{\sigma(z)^{13}}
=\gamma\left(x^6+(2+6\delta)x^3+\frac{40+24\delta}{13}\right),
$$
并令 $x_\gamma=x(\gamma z)$、$x_{\bar\gamma}=x(\bar\gamma z)$。真实纤维迹中完整的 $y$ 比是
$$
\frac{y(\bar\gamma z)}{y(\gamma z)}
=\frac{\gamma}{\bar\gamma}
\frac{x_{\bar\gamma}'(x)}{x_\gamma'(x)}.
\tag{29}
$$
这同时支付了微分尺度；不能只用其平方。

若 $x_\gamma=N/D$，在目标 $x=a$ 的全十三点纤维
$f_a=N-aD$ 上，每个基列的准确有理迹为
$$
\operatorname{Tr}_{K[x]/(f_a)}\left[
\left(\frac{q_{\bar\gamma}}{q_\gamma}\right)^{34}
\frac{\gamma}{\bar\gamma}\frac{x_{\bar\gamma}'}{x_\gamma'}
x_{\bar\gamma}^{3j}\right],\quad 0\le j\le5.
\tag{30}
$$
六个固定 $a=2,\ldots,7$ 的 Vandermonde 因 (19) 的已证维数唯一确定整矩阵；第七个 $a=8$ 的全纤维单独核定六列。整个 $\sigma^{34}$ 比和 (29) 均保留。生产证书保存矩阵、两条观察行行列式和所有精确检验。

计算结果是
$$
\boxed{\det(t-M_\gamma^{\rm odd})
=t^6-\gamma^3t^3+\gamma^6
=\gamma^6\Phi_{18}(t/\gamma).}
\tag{31}
$$
原三条来源的特征值满足 $\lambda_k^3=-\gamma^3$，代入 (31) 得 $3\gamma^6\ne0$。因此不能把这个一阶奇块未经连接修正便认作那三条原 even 线。

更具体，若 $C=\sigma^{34}yP(X)$，其原点一阶质量为 $-P_5$，两个 $T_\pm$ 的值为 $\sigma(T_\pm)^{34}y(T_\pm)P_0$。对矩阵 (31)，两组实际观察
$$
\bigl(e_0(M_\gamma^{\rm odd})^n\bigr)_{n=0}^5,
\qquad
\bigl(e_5(M_\gamma^{\rm odd})^n\bigr)_{n=0}^5
\tag{32}
$$
都秩六。故任一非零奇 companion 的真实 CM13 轨道最终会读到每种边界。尤其 $P_0=0$ 的五维全纯连接域不受这个原 CM13 保持；需要保 (21) 的极修正。这个结论只定位实际图的边界，不把有限矩阵非退化声称为原中央泛函非零。

## 7. 普通处的完整一阶 Mellin 转置

设 $p>7$ 为普通素数，取共同 $E_{17}$ 的原形式周期 $\Omega_p$。对一个实际形式截面 $T$，写 $\nu_T$ 为 Amice 变换
$$
T\bigl(\Omega_p\log(1+Z)\bigr)
$$
对应的测度。R300 的原整 theta 格和本篇有限分母保证 $H_k,C_{1j}$ 都给有界测度。$F(0)=1$，故其 Amice 变换是整单位；$q=F'/F$ 的变换也整。于是可对 (28) **完整** 使用
$$
\boxed{\nu_{H_1}-a\nu_{H_j}
=\Omega_p^{-1}x\nu_C-\nu_q*\nu_C,\qquad
C=C_{1j},\ a=a_{1j}.}
\tag{33}
$$
星号是加法卷积。其总质量等式是 $-a=C'(0)$，因为 $q(0)=0$；这里的总质量不是单位群质量。

令 $d=p-1$，$\tau_p$ 为 Teichmüller 角色，定义
$$
M_T(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^{du}\,d\nu_T(x),
\qquad
M_{C,1}(u)=\int_{\mathbf Z_p^\times}\tau_p(x)\langle x\rangle^{du}\,d\nu_C(x).
$$
那么全部原单位群行是
$$
\boxed{M_{H_1}(u)-aM_{H_j}(u)
=\Omega_p^{-1}M_{C,1}(u+1/d)-\mathcal K_{q,C}(u),}
\tag{34}
$$
其中
$$
\mathcal K_{q,C}(u)=\iint_{\mathbf Z_p^2}
\mathbf1_{x+y\in\mathbf Z_p^\times}\,
\langle x+y\rangle^{du}\,d\nu_q(x)d\nu_C(y).
\tag{35}
$$
因此中央导数准确为
$$
M_{H_1}'(0)-aM_{H_j}'(0)
=\Omega_p^{-1}M_{C,1}'(1/d)-\mathcal K_{q,C}'(0).
\tag{36}
$$
这保留了真正 tame-one 分支及 $1/d$ 移权；(35) 包括所有原 $p$ 环带，不能写成两个乘法 Mellin 的积。各自 Euler、实际 $\psi_k$ 与 (4) 的形式 period 识别须另用完整 prime-core 运输支付；(33)–(36) 没有预设它们相同。

## 8. 惰性处保全部 Gaussian 的完整负移权式

设 $p>17$、$p\equiv5\pmod6$。用共同 $E_{17}$ 的同一个局部展开，置
$$
d=p+1,\quad c=[z^d]\log(\sigma/z),\quad\kappa=34c,
\quad V=C/z,\quad W=zF'/F.
$$
R301 的高度二估计经固定单位同次缩放仍给 $v_p(c)=-1$。取 (28) 中的整行：通常可取 $j=3$；在 $p=101$ 用 $j=5$，也可始终用后者。由于 $C$ 是真实 $\rho$ 型，$V$ 是原 $\mu_6$ 不变函数，且
$$
H_1-aH_j=(D+1-W)V,\qquad D=z\partial_z,
\qquad V(0)=-a.
\tag{37}
$$
现在共同删去的就是 $\kappa z^d$：
$$
\widehat F=e^{-\kappa z^d}F,\quad
\widehat V=e^{-\kappa z^d}V,\quad
\widehat W=z\widehat F'/\widehat F,
\quad W=\kappa d z^d+\widehat W.
$$
$\widehat F$ 是 R301 较大圆盘上的解析单位，$\widehat V$ 解析，$\widehat W$ 从六次项开始。对这个固定 charge 34 定义
$$
\mathcal J_T(u)=\sum_{h\ge0}
[z^{dh}](e^{-\kappa z^d}T)\,\kappa^{-h}(u)_h.
\tag{38}
$$
同一 Gauss 界给这些级数在包含 $\mathbf Z_p$ 的圆盘解析；$\mathcal J_{H_j}(0)=1$，$\mathcal J_V(0)=-a$，$\mathcal J_{\widehat WV}(0)=0$。

对任意这样的真实 $T$，全部 Gaussian 项合并后有
$$
\mathcal J_{DT}(u)=du\,\mathcal J_T(u),\qquad
\mathcal J_{z^dT}(u)=\kappa^{-1}u\,\mathcal J_T(u-1).
\tag{39}
$$
可先在非负整数权用有限系数卷积证明，再用解析性延拓；或逐个 Newton 基使用
$h(u)_h+(u)_{h+1}=u(u)_h$。不能只对 $\widehat T$ 微分而漏掉原 Gaussian。

代入 (37)，得到同一个原伴随的完整等式
$$
\boxed{
\mathcal J_{H_1}(u)-a\mathcal J_{H_j}(u)
=(du+1)\mathcal J_V(u)
-du\,\mathcal J_V(u-1)-\mathcal J_{\widehat WV}(u).}
\tag{40}
$$
最后一项是实际整个乘积 $\widehat W V$ 的原变换，不是两个中央系数的乘积。其中央导数为
$$
\boxed{
\mathcal J_{H_1}'(0)-a\mathcal J_{H_j}'(0)
=\mathcal J_V'(0)+d\{\mathcal J_V(0)-\mathcal J_V(-1)\}
-\mathcal J_{\widehat WV}'(0).}
\tag{41}
$$
这同时保留非零质量 $\mathcal J_V(0)=-a$、实际负权 $-1$ 和全部连接卷积。$\mathcal J_{H_j}(0)=1$ 与 (1) 的秩零性不使 $\mathcal J_{H_j}'(0)$ 自动为零；复函数方程也不在此固定 tame 分支上给未经证明的 $u\leftrightarrow-u$。

因此 (1)、(3)、(28)、(34)、(40) 已把两个真实参考接到同一原点连接；要由它们控制目标中央导数，仍需控制 (36) 或 (41) 中的同一个完整 companion 观察。原奇 CM13 图的真实边界已由 (20)、(21)、(31)、(32) 给出，后继必须在这张图内支付它们，不能由三条有限特征线或两个非零中央值直接跳到目标完成。

## 9. 证明、证书与文献

两份生产证书为

- `scripts/check-jzero-three-original-sources-and-central-constants.py/.json`：读取 R297 已发表的完整 CM13 定标矩阵，精确验证三条真实线和单重性；重建原 $17$ 除法多项式及 CM7 作用，计算全部四十八项原零权和，证明 (12)；验证一般 $b$ 的连接、全部质量、余核、两个伴随以及完整 Newton 移权。
- `scripts/check-jzero-odd-cm13-companion.py/.json`：从实际两条 CM13 除法函数重建七个全十三点纤维，包含整个 $\sigma^{34}$ 和 $y$ 比，确定完整六维奇矩阵、特征多项式、两类边界的满秩观察及 (20)–(22)。

这些是固定有限代数恒等式；没有扫描目标素数。本文依赖的已付原来源和解析界为
[R290](R290-jzero-original-schwartz-local-weil-and-full-weight-square.md)、
[R292](R292-jzero-actual-minimal-theta-degree-and-cubic-source-module.md)、
[R297](R297-jzero-actual-cm13-mass-kernel-cm7-product-and-angular-source.md)、
[R298](R298-jzero-exact-central-constant-and-original-kronecker-resolvent.md)、
[R300](R300-jzero-full-theta-prime-core-and-single-euler-measure.md)、
[R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)、
[R302](R302-jzero-original-degree-two-reference-and-exact-full-weight-square.md)、
[R306](R306-jzero-three-sextic-original-local-data-and-full-weight-squares.md)。

外部定理使用 Bannai–Kobayashi, *Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers*, Duke Math. J. 153 (2010), Theorem 1.17（[作者预印本](https://arxiv.org/abs/math/0610163)）的原 Kronecker 展开；Yang 的已发表全权平方及实际 splitter 规范已逐项在 R290、R306 支付。代数秩零使用 Coates–Wiles, *On the conjecture of Birch and Swinnerton-Dyer*, Invent. Math. 39 (1977), 223–251（[DOI](https://doi.org/10.1007/BF01402975)）。
