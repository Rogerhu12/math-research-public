# R266 — 普通真实 theta 迹的整有限闭合、参考质量符号及付费返回原源

日期：2026-11-13。**状态：以下特征零真实抽取算子的有限 theta 迹公式、整格闭合、两个参考质量的实际符号、二挠不变块、返回原三源的准确次数成本及带 frame 的 Cartier 公式均已证明。原三条完整中央零仍未控制全部乘法列。**

本篇继续 R263 的原测度算子
$$
T_p=b_{17}[b_0^2]_*\psi_p,\qquad
\psi_p\nu=(x\mapsto x/p)_*(\nu|_{p\mathbb Z_p}).
\tag{1}
$$
证明它在真实固定 theta 次数中闭合；不是先假定它在三源代数上保持乘法。
R263 的非零余类卷积项仍然存在。

## 1. 特征零 CM 迹公式

仍在
$$
E_0:y^2=x^3-x,\qquad \omega=dz=\frac{dx}{2y}
$$
上工作。设 $p\equiv1\pmod4$ 为普通好素数，选与原正式群一致的
$$
\alpha=\pi_0,\qquad \beta=\bar\pi_0=b_0,\qquad
\alpha\beta=p,\quad v_p(\alpha)=1,\quad v_p(\beta)=0.
\tag{2}
$$
两者均为真正的 Gaussian CM 整数。令
$$
r_\gamma(z)=\frac{\sigma(\gamma z)}{\sigma(z)^p},
\qquad \gamma\in\{\alpha,\beta\}.
\tag{3}
$$
它是原 CM division 函数，并满足
$$
r_\gamma\in\mathbb Q(i)(E_0),\qquad
\operatorname{div}(r_\gamma)=[\gamma]^*(O)-p(O),\qquad
r_\gamma(z)=\gamma z^{1-p}+\cdots.
\tag{4}
$$
这里的次数是 $N\gamma=p$。式 (3) 的椭圆性可由原 sigma 自动因子直接检查：
平方格的 quasi-period 作用把 $\gamma$ 变成 $\bar\gamma$，所以分子与
$\sigma^p$ 的指数相同；奇 norm 的半特征也相同。除子及首项唯一确定 (3)。
这保留了 sigma frame，不把 sigma 函数当作椭圆有理函数。

对 $N\ge1$ 定义实际正 theta 空间
$$
\mathcal S_N=\sigma^N L(N O),\qquad
L(N O)=\{f\in\mathbb Q(i)(E_0):\operatorname{div}_\infty f\le N(O)\}.
\tag{5}
$$
其维数是 $N$。所有元素在原点全纯，其普通 Amice 测度均由 R263 的同一
正式周期 $\Omega_0$ 定义。

**定理 1。** 对 $G=\sigma^Nf\in\mathcal S_N$，(1) 的真实 Amice 变换对应
$$
\boxed{
T_pG(z)=\frac{b_{17}}p\,\sigma(z)^N
\operatorname{Tr}_{[\alpha]}
\left(\left(\frac{r_\beta}{r_\alpha}\right)^N
             f\circ[\beta]\right)(z).
}
\tag{6}
$$
其中迹对 $[\alpha]:E_0\to E_0$ 的全部 $p$ 个点求和，不作除以 $p$ 的归一。
因此
$$
\boxed{T_p(\mathcal S_N)\subset\mathcal S_N.}
\tag{7}
$$

**证明。** 先在 Amice 坐标读取抽取，不把挠点的正式对数代成零。若
$\mathcal A_G(T)$ 为实际变换，则
$$
\mathcal A_{T_pG}(T)
=\frac{b_{17}}p\sum_{\zeta^p=1}
 \mathcal A_G\!\left(\zeta(1+T)^{\beta^2/p}-1\right).
\tag{8}
$$
正式同构把 $\mu_p$ 送到连通的 CM 核 $E_0[\alpha]$。
因为 $[\beta]$ 在该核上可逆，(8) 中的点可准确写为 $[\beta]P$，
其中 $[\alpha]P$ 为输出点。

设 $\Sigma$ 为 sigma 的实际整正式级数。CM division 恒等式是
$$
\Sigma([\gamma]P)=\Sigma(P)^p r_\gamma(P).
$$
因此在每条逆像支上
$$
\frac{G([\beta]P)}{\Sigma([\alpha]P)^N}
=\left(\frac{r_\beta(P)}{r_\alpha(P)}\right)^N f([\beta]P).
$$
对全部支求和正是 (6)。这个等式先在穿孔正式圆盘成立，再延拓到原点；
其证明完全使用正式群恒等式与有理 division 函数。

最后，括号中函数的极点除子至多为
$$
N[\alpha]^*(O).
\tag{9}
$$
因为 $f\circ[\beta]$ 的极点由 $r_\beta^N$ 的零准确支付。
特征零同源 $[\alpha]$ 处处无分歧，故迹的极点只在 $O$，阶至多 $N$。
于是 (6) 属于 (5)，证明 (7)。$\square$

式 (6) 是同一个原测度的恒等式；并没有把一个独立构造的代数迹算子
仅凭维数相同就当作 $T_p$。

## 2. 原整数格也严格闭合

令 $\mathcal O$ 为普通测度的整数环。在好素位使用原基
$$
1,\quad x^a\ (a\ge1,\ 2a\le N),\quad x^a y\ (a\ge0,\ 2a+3\le N)
\tag{10}
$$
给出 $L(N O)$ 的 $N$ 个基向量。设 $\mathcal S_N(\mathcal O)$ 为乘
$\sigma^N$ 后的原格。

**定理 2。**
$$
\boxed{T_p\mathcal S_N(\mathcal O)\subset\mathcal S_N(\mathcal O).}
\tag{11}
$$

**证明。** 在原正式参数 $\tau=-x/y$ 中，
$\Sigma=\tau\cdot\mathcal O[[\tau]]^\times$，
$x=\tau^{-2}\cdot\mathcal O[[\tau]]^\times$，
$y=-\tau^{-3}\cdot\mathcal O[[\tau]]^\times$。
(10) 乘 $\Sigma^N$ 后具有互异首阶，首系数为单位；
其首阶从 $0$ 到 $N$，只缺 $N-1$。因此，一个属于
$\mathcal S_N$ 的级数若全部正式系数整，则其 (10) 基系数整：
从最低非零阶起逐一消元即可。

每个原格元素给整 Amice 测度。限制到 $p\mathbb Z_p$、支撑除以 $p$、
乘 $b_{17}$ 及按单位 $\beta^2$ 缩放都保持测度整性。
正式同构与其逆也整，故 $T_pG$ 的 $\tau$ 级数整。
再用定理 1 和上述单位三角消元，得到 (11)。$\square$

因此 (6) 中表面的 $1/p$ 分母已经由真实测度支付。
这不是仅在函数域中成立的闭合，也不需要一个随 $N$ 增长的额外分母集合。

## 3. 两个参考的原点项消失，实际符号得到确定

R263 只使用了两个参考质量的平方，并保留实际符号。
现在可以严格确定符号：
$$
\boxed{
M_\vartheta(0)=1-b_0^{-1},\qquad
M_{S_8}(0)=1-b_8^{-1}.
}
\tag{12}
$$

首先把两个参考放到确切的正 theta 空间。原 duplication 公式给
$$
\vartheta(2z)=\sigma^4(U+1),\qquad U=x^2,
\tag{13}
$$
而
$$
\boxed{S_8(2z)=\sigma^{16}(U+1)^2(U^2-6U+1).}
\tag{14}
$$
后一式由
$$
\sigma(2z)=-2y\sigma^4,\quad
\vartheta(2z)=(U+1)\sigma^4,\quad
y(2z)=\frac{(U+1)(U^2-6U+1)}{8y^3}
$$
逐项代入 $S_8=-y\vartheta\sigma^3$ 得到。
故两个实际参考分别属于 $\mathcal S_4$、$\mathcal S_{16}$，常数项都是一。
新参考的二挠半特征已经由真实 $[2]$ 拉回消去，没有混用两个不同线丛。

对参考的全 ray 比较，R63/R263 的非平凡 tame 分支证明原样成立；
在平凡分支保留原点项，得到
$$
\nu_S|_{p\mathbb Z_p}
-b_D^{-1}[p/b_D^2]_*\nu_S=\gamma_D\delta_0,
\qquad
(S,D)=(\vartheta(2z),0),(S_8(2z),8).
\tag{15}
$$
这一步只用各参考真实有限向量的全部正权平方，仍未假定原点项为零。
因为 $S$ 为 $i$ 不变，$b_D/b_0\in\mu_4$，(15) 准确化为
$$
T_pS=(b_{17}/b_D)S+b_{17}\gamma_D\cdot1.
\tag{16}
$$
由 (7)，左侧与第一项都在同一个正 theta 空间。
常函数一不属于任何 $\mathcal S_N$，$N>0$：否则
$\sigma^{-N}$ 为椭圆函数，与其非恒定自动因子矛盾。
亦可用 R190 的正 Gaussian 最高次数论证。因此 $\gamma_D=0$。

对 (15) 取零次矩，并用两个参考常数项一，得 (12)。
单位变量 $2$ 的缩放不改变单位质量，因此 (12) 正是未缩放的参考质量。
这补出了符号与原点项的证明；没有逐个素数挑选平方根。
R263 的非异常性证明继续给两者为 $p$ 单位。

## 4. 实际二挠与四次旋转块：维数准确为 $34m+1$

为把原三源放在同一个无扭转线丛，统一作真实 $[2]$ 拉回，记
$$
A^\sharp(z)=A(2z)=A_{17}(4z)/16,\quad
B^\sharp(z)=B(2z),\quad H^\sharp(z)=H(2z).
\tag{17}
$$
三者都在 $\mathcal S_{272}$；其完整普通中央导数与原列相差实际单位
$2^{p-1}$ 的解析缩放，零条件相同。

令 $T_0=(0,0)$，写 $\tau(P)=P+T_0$，有
$$
x\circ\tau=-1/x,\qquad U\circ\tau=1/U,\qquad \tau^*\omega=\omega.
$$
当 $4\mid N$ 时，其原归一 theta 作用在 (5) 上是
$$
\mathcal T_{0,N}(\sigma^N f)=
\sigma^N x^{N/2}(f\circ\tau).
\tag{18}
$$
这个作用的平方为一。式 (18) 由 sigma 二挠加法公式给出；
所取归一消去共同非零常数，$4\mid N$ 使余下根单位相位为一。

**定理 3。** $T_p$ 与 (18)、以及实际 $z\mapsto iz$ 作用交换。

**证明。** 两个 CM 同源都固定 $T_0$。由 (4) 的除子，
$$
\epsilon_\gamma=
\frac{r_\gamma^2(x\circ[\gamma])}
     {x^p(r_\gamma\circ\tau)^2}
$$
为常数。再以 $\tau$ 平移上式，利用 $p$ 为奇数与 $x\circ\tau=-1/x$，
得到 $\epsilon_\gamma=\epsilon_\gamma^{-1}$，故 $\epsilon_\gamma=\pm1$。
令 $k=r_\beta/r_\alpha$，便有
$$
k^N(x\circ[\beta])^{N/2}
=(x\circ[\alpha])^{N/2}(k\circ\tau)^N
\qquad(4\mid N).
\tag{19}
$$
将 (19) 代入 (6)，并用 $\operatorname{Tr}_{[\alpha]}$ 与平移 $\tau$ 交换，
即得与 (18) 交换。另一方面
$r_\gamma(iz)=i^{1-p}r_\gamma(z)=r_\gamma(z)$，
两同源与 $i$ 交换，故 (6) 也与四次旋转交换。$\square$

取 $m\ge1$、$N=272m$。四次旋转不变的 $f$ 准确为
$P(U)$、$\deg P\le68m$；(18) 的 $+1$ 条件是
$$
P(U)=U^{68m}P(1/U).
\tag{20}
$$
定义实际共同角参数及 frame
$$
t=t_0(2z)=\frac{U^2-6U+1}{(U+1)^2},\qquad
\Xi=\sigma^{272}(U+1)^{68}=\vartheta(2z)^{68}.
\tag{21}
$$
于是这个共同块准确是
$$
\boxed{
\mathcal V_m=\Xi^m\mathbb Q(i)[t]_{\le34m},\qquad
\dim\mathcal V_m=34m+1,\qquad T_p\mathcal V_m\subset\mathcal V_m.
}
\tag{22}
$$
这是等式而非维数上界。证明可令
$q=U/(U+1)^2=(1-t)/8$；对 (20) 的空间，
$$
U^j(U+1)^{68m-2j},\qquad0\le j\le34m
$$
在低 $U$ 次数上为单位三角基。以 $t=1-8q$ 换基只需倒转二。
故在奇好素位也有原整格等式
$$
\mathcal V_m(\mathcal O)=\Xi^m\mathcal O[t]_{\le34m}.
\tag{23}
$$
定理 2、3 因而证明这个 $34m+1$ 维格的真实整闭合。

## 5. 公共基除子仍有十次，返回原源要支付线性成本

R243/R244 的三角多项式仍记作 $a,b,h$，其次数为 $23,23,24$，
共同基因子为
$$
g(t)=t(t^2-1)(t^2-2)(t^4+4),\qquad \deg g=9.
$$
由 (21) 和原 duplication 恒等式，
$$
\vartheta(4z)^{17}=\Xi(2-t^2)^{17}.
$$
因此三个真正的原来源准确为
$$
\boxed{(A^\sharp,B^\sharp,H^\sharp)=\rho^\sharp(a(t),b(t),h(t)),
\qquad \rho^\sharp=\Xi g(t).}
\tag{24}
$$
共同 $34$ 次线性系的有限公共零是 $g$ 的九次除子，无穷点还至少一阶；
总公共基除子次数为十。原源在次数 $m$ 时含它的 $m$ 倍。
于是 (22) 不是原三源齐次代数 $\mathcal A_m$：
$$
\mathcal A_m\subset
(\rho^\sharp)^m\mathbb Q(i)[t]_{\le24m}
\subset\mathcal V_m.
\tag{25}
$$
第一包含还保留 R249 的固定平面奇点导子。
这里没有删除 $\rho^\sharp$，也没有把多出的 $10m$ 个角方向当作免费来源。

不过，可以用原来源中的明确乘子把整个闭合块返回原有限次数源。
令 $C_0^\sharp=C_0(2z)$ 为 R249 已付的固定次数二十二导子，并设
$$
\ell_m=\left\lceil\frac{5m}{12}\right\rceil,\qquad
K_m=C_0^\sharp(\rho^\sharp)^{\ell_m}g(t)^m.
\tag{26}
$$
所有固定的五次归一单位均吸收入 R249 的同一个固定坏集合。则准确有
$$
\boxed{
K_m\in\mathcal A_{\ell_m+22},\qquad
K_m\mathcal V_m(\mathcal O)
\subset\mathcal A_{m+\ell_m+22}(\mathcal O).
}
\tag{27}
$$
而且右侧所列 $34m+1$ 维子格是 primitive 的。

**证明。** R249 给所有 $j\ge0$ 的完整包含
$$
C_0^\sharp(\rho^\sharp)^j\mathcal O[t]_{\le24j}
\subset\mathcal A_{j+22}(\mathcal O),
\tag{28}
$$
且其原商格无扭。由于 $9m\le24\ell_m$，第一式成立。
若 $G=\Xi^m q(t)$、$\deg q\le34m$，则
$$
K_mG=C_0^\sharp(\rho^\sharp)^{m+\ell_m}q(t).
\tag{29}
$$
$34m\le24(m+\ell_m)$ 正好等价于 $\ell_m\ge5m/12$，
所以 (28) 给第二式。多项式次数不超过 $34m$ 的子格是完整角多项式格的
直接和因子；结合 (28) 的 primitive 性，得到最后断言。$\square$

成本 (27) 的线性主项是准确的。在忽略固定奇点导子、只要求落到归一化源时，
若一个非零原齐次乘子 $K\in\mathcal A_\ell$ 使
$K\mathcal V_m\subset(\rho^\sharp)^{m+\ell}\mathbb Q(i)[t]_{\le24(m+\ell)}$，
写 $K=(\rho^\sharp)^\ell k(t)$。对 $G=\Xi^m$ 先得 $g^m\mid k$；
令 $k=g^mv$。再对 $G=\Xi^m t^{34m}$ 得
$$
34m+\deg v\le24(m+\ell),
\qquad\boxed{\ell\ge5m/12.}
\tag{30}
$$
所以不存在一个固定次数乘子，可对全部 $m$ 免费完成这个返回。
(27) 在这个必要线性成本之外只支付 R249 的固定二十二。

在原点 $t=1-8z^4+\cdots$、$g(t)=80z^4+\cdots$、
$\rho^\sharp=80z^4+\cdots$，而
$C_0^\sharp=16^{22}z^{88}+\cdots$。
故 $K_m$ 的真实零阶为 $4(m+\ell_m+22)$，首系数为固定二、五单位的幂。
返回原源时必须保留这个行移位、原 theta charge 与全部 Mellin 卷积；
不能把 (27) 的乘子当作单位函数删除。

## 6. 一个直接可计算的实际 Cartier 矩阵

下面给 (6) 的准确模 $p$ 公式，仍保同一 frame。
写 $p=4r+1$。因 $r_\beta$ 为 $i$ 不变、有唯一 $p-1$ 阶极，
$$
r_\beta=R_p(U),\qquad \deg R_p=r,\qquad
R_p^*(U)=U^rR_p(1/U).
$$
其最高系数为 $\beta$，在选定普通素位是单位。
系数也在 $\mathcal O$ 中：由
$r_\beta=\Sigma([\beta]\tau)/\Sigma(\tau)^p$
先得其 $\tau^{p-1}$ 倍为整正式级数，再用
$1,U,\ldots,U^r$ 的互异单位首极阶逐项消元。
由定理 3 证明中的常数恒等式，平方后有
$$
\boxed{U\circ[\beta]=U\left(\frac{R_p^*}{R_p}\right)^4.}
\tag{31}
$$
这个式子保留真正的 CM division 多项式，而不是以 Hasse 常数替代同源。

当 $N=272m$、$P\in\mathcal O[U]_{\le68m}$ 时，令
$$
\mathcal H_P(U)=R_p(U)^N
P\!\left(U\left(\frac{R_p^*(U)}{R_p(U)}\right)^4\right).
\tag{32}
$$
因为 $4\deg P\le N$，(32) 是整多项式，且
$\deg\mathcal H_P\le Np/4$。
在 $\mathbb F_p$ 系数上，(6) 的约化准确为
$$
\boxed{
T_p(\sigma^NP)
=\frac{b_{17}}{b_0}\,\sigma^N
\sum_{j=0}^{N/4}
[U^{jp+r}]\bigl((U-1)^{2r}\mathcal H_P(U)\bigr)\,U^j
\quad\bmod p.
}
\tag{33}
$$
扩张剩余系数域时，Cartier 系数需施 $p$ 次根；
在本文原 $\mathbb Q(i)$ 系数的选定 split 素位上，系数就在 $\mathbb F_p$ 中。
式 (33) 可在 (20) 的 palindromic 基中给一个准确
$(34m+1)\times(34m+1)$ 矩阵，无目标素数扫描或无限形式截断。

证明分两步。Cartier 的自然性及真实 CM frame 给
$$
\left(\frac{\mathcal C(G\omega)}{\omega}\right)\circ[\beta]
=\sigma^N\frac{\mathcal C(\mathcal H_P\omega)}{\omega}.
\tag{34}
$$
R263 已识别左侧乘 $b_{17}/b_0$ 正是实际 $T_p$ 的约化。
另一方面，利用 $y^2=x^3-x$，
$$
\frac{\mathcal C(H(U)\omega)}{\omega}
=\sum_{j\ge0}[U^{jp+r}]\bigl((U-1)^{2r}H(U)\bigr)U^j.
\tag{35}
$$
这是 $dx/(2y)=y^{-p}(x^3-x)^{(p-1)/2}dx/2$ 的普通 Cartier 系数抽取；
把 $x$ 的偶幂换成 $U$ 即得所列指标。次数界使 $j\le N/4$，所以得到 (33)。

## 7. 完整中央转置与原 de Rham 方向：必须保留的项

有限闭合可以与完整测度逐环带相连，但它没有把原三零扩成整个空间的零。
对任意 $G\in\mathcal S_N$，定义
$$
M_G^{[n]}(u)=
\int_{p^n\mathbb Z_p^\times}
\langle x/p^n\rangle^{(p-1)u}\,d\nu_G(x).
$$
由 (1) 的定义与单位缩放，有完整恒等式
$$
\boxed{
M_G^{[n]}(u)
=b_{17}^{-n}(b_0^{-2n(p-1)})^u M_{T_p^nG}(u).
}
\tag{36}
$$
特别，真实单位质量是有限 theta 评价
$$
\boxed{M_G(0)=G(0)-b_{17}^{-1}(T_pG)(0).}
\tag{37}
$$
对 (36) 求导必须保留
$-2n(p-1)\log_p b_0$ 乘 $M_{T_p^nG}(0)$；
只有质量已经为零时，该项才可删除。
对三条一次来源，R263 的准确特征方向使 (36) 回到已证的环带零；
对乘法列则仍需要其自己的完整 $M_G$，不能由三条一次值替代。

最后，给出与 R264/R268 的裸 de Rham 分解相容的准确带权接口。
设一个原有限有理微分已写成
$$
\eta=dR+c\,x\omega,
\tag{38}
$$
并用实际 theta 权 $G=\sigma^Nf$ 乘它。
把 $[\beta]$ 拉回，令
$$
w=r_\beta^N(f\circ[\beta]),\quad
R_\beta=R\circ[\beta],\quad x_\beta=x\circ[\beta].
$$
由同一个 frame 恒等式，在本文的 $\mathbb F_p$ 系数规范有
$$
\boxed{
[\beta]^*\mathcal C(G\eta)
=\sigma^N\left\{-\mathcal C(R_\beta\,dw)
+c\beta\,\mathcal C(w x_\beta\omega)\right\}.
}
\tag{39}
$$
这里所有量在剩余域中读取；一般系数需保留 Cartier 的半线性。
证明是
$[\beta]^*(G\eta)=\sigma^{Np}w(dR_\beta+c\beta x_\beta\omega)$，
提取 $p$ 次幂 frame 后，再用
$$
\mathcal C(w\,dR_\beta)
=\mathcal C(d(wR_\beta)-R_\beta\,dw)
=-\mathcal C(R_\beta\,dw).
$$
所以即使裸 $\eta$ 的 Cartier 只检测一个已知 de Rham 系数，
真实 theta 权下还存在 (39) 的第一项。
它是明确的原连接项；不能用 $\mathcal C(\eta)=0$ 删除它。

本篇没有将 (39) 当作原中央泛函为零的结论。
其作用是把下一步需要比较的东西固定为：真实有限 theta 矩阵 (33)、
实际乘法列的完整环带函数 (36)，以及原连接项
$-\mathcal C(R_\beta\,dw)$。这些对象已在同一原 frame 和 charge 中，
并可通过 (27) 付费返回原三源；还须从真正的三中央约束取得新的关系。

## 8. 依赖及范围

本篇只使用已确定的原 CM sigma、正式群与测度：
R51 的整正式因子、R63 的全 tame Euler 比较、R239/R243 的真实第三来源、
R244/R249 的原源与固定导子、R263 的普通全测度规范。
(6)、(11)、(12)、(22)、(27)、(33)、(36)、(39) 的证明均在正文给出。

没有新增数值素数样本。固定次数 theta 闭合不等于原三源代数乘法闭合，
更不等于三条中央零控制全部闭合空间；两者之间的真实非零缺项由 R263 (41) 保留。

