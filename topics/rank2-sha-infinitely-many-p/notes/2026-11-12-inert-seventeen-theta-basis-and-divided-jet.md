# 惰性目标的十七维 theta 基与必须保留的除 $p$ jet

日期：2026-11-12。状态：固定 theta 基、精确系数公式及整性已证明；
尚未把其中随 $p$ 变化的除 $p$ jet 变成固定有限 Frobenius 表示。

本文从已经认证的实际截面出发，不再使用数值候选。
由[准确的 $D=1$ 缩放](2026-11-12-inert-theta-romik-interface.md)，
只需研究

$$
 E_0:y^2=x^3-x,\qquad
 A(z)=\theta_T(z)^{17}q(x(z)^{-2}),
 \quad q(V)=V+\frac35V^2-\frac15V^3+\frac15V^4,
 \quad A(z)=\sum b_mz^m.
 \tag{1}
$$

这里 $T=(0,0)$、$\theta_T^2=x\sigma^2$、$\theta_T(0)=1$。
目标仍是 $b_{p+1}\not\equiv0\pmod p$ 在无穷多个 $p\equiv3\pmod4$
上成立。

## 1. 十七个固定的代数 theta germs

记 $\Gamma=\Omega_0\mathbb Z[i]$、
$\mathcal A=\Omega_0^2/\pi_{\mathbb C}$，并固定

$$
 \alpha=4-i,\qquad \alpha\bar\alpha=17.
$$

平方格的准周期是 $\eta_\lambda=\bar\lambda/\mathcal A$。
在这套规范下

$$
 \theta_T(z+\lambda)=\chi_T(\lambda)
   \exp\!\left(\frac{\bar\lambda(z+\lambda/2)}{\mathcal A}\right)
   \theta_T(z),\qquad
 \chi_T(m\Omega_0+ni\Omega_0)=(-1)^{mn}.
 \tag{2}
$$

对每个 $S\in E_0[\bar\alpha]$，定义

$$
 f_S(z)=
  \exp\!\left(-\frac{\alpha\bar S z}{\mathcal A}\right)
       \frac{\theta_T(\alpha z+S)}{\theta_T(S)}.
 \tag{3}
$$

$S$ 改变格代表元时，(2) 中的指数与 (3) 的指数准确相消；
所以 (3) 只依赖挠点本身。
分母非零，因为 $S$ 的阶除 $17$，而 $\theta_T$ 的零点是 $T$。

由于 $\bar\alpha S\in\Gamma$，对任意 $\lambda\in\Gamma$，
额外的平移因子是

$$
 \exp\!\left(
 \frac{\bar\alpha S\bar\lambda-\alpha\bar S\lambda}{\mathcal A}
 \right)=1.
$$

这里指数是 $2\pi_{\mathbb C}i$ 的整数倍。
又 $\alpha\equiv i\pmod2$，所以
$\chi_T(\alpha\lambda)=\chi_T(\lambda)=\chi_T(\lambda)^{17}$。
因此所有 $f_S$ 与 $\theta_T^{17}$ 有相同的自动因子，
属于同一个次数 $17$ 的线丛 $\mathcal L^{17}$，且 $f_S(0)=1$。

更具体地，令 $R_S=T+S$，并记

$$
 U_S=E_1^*(R_S)=\zeta(R_S)-\frac{\bar R_S}{\mathcal A},
 \qquad X_S=x(R_S),\qquad Y_S=y(R_S).
$$

因为 $E_1^*(T)=0$，(3) 亦为

$$
 f_S(z)=\frac{\sigma(R_S+\alpha z)}{\sigma(R_S)}
             \exp\!\left(-\frac{\bar R_S\alpha z}{\mathcal A}\right).
 \tag{4}
$$

设

$$
 \mathcal DU=-X,\quad \mathcal DX=2Y,\quad
 \mathcal DY=3X^2-1,\qquad
 C_0=1,\quad C_{n+1}=(\mathcal D+U)C_n .
 \tag{5}
$$

则准确的 Taylor 展开为

$$
 \boxed{\quad
 f_S(z)=\sum_{n\ge0}\frac{\alpha^n}{n!}
                        C_n(U_S,X_S,Y_S)z^n.
 \quad} \tag{6}
$$

所有 $U_S$ 都是代数数，而不只是带未知周期的复数。
事实上，任选 $a\equiv1\pmod{34}$ 的正整数，整数乘法的
sigma 除法公式给

$$
 U_S=-\frac{\delta\log\Psi_a(R_S)}{a(a-1)},
 \qquad \delta=2y\partial_x.
 \tag{7}
$$

右边属于固定的数域 $L=\mathbb Q(i,E_0[17])$。
因此 (6) 是一个定义在固定数域上的 germ，不含随 $p$ 变化的挠点。

## 2. 基与 Fourier 系数都是固定的

对 $P\in E_0[\alpha]$，写 $\lambda=\alpha P\in\Gamma$。
由 (2)–(3)，

$$
 \frac{f_S(P)}{f_0(P)}
    =e_\alpha(P,S):=
        \exp\!\left(\frac{\bar\lambda S-\lambda\bar S}{\mathcal A}\right).
 \tag{8}
$$

这是 $E_0[\alpha]\times E_0[\bar\alpha]\to\mu_{17}$ 的完美配对。
例如其完美性可直接从格的对偶性看出：若右边对所有
$\lambda\in\Gamma/\alpha\Gamma$ 都为 $1$，则 $S\in\Gamma$。

矩阵 $(e_\alpha(P,S))_{P,S}$ 是一个可逆的有限 Fourier 矩阵。
所以十七个 $f_S$ 线性无关；Riemann–Roch 给
$h^0(\mathcal L^{17})=17$，故它们确为完整基。

于是实际截面有唯一展开

$$
 A(z)=\sum_{S\in E_0[\bar\alpha]}a_Sf_S(z),\qquad
 a_S\in L,
 \qquad \sum_Sa_S=A(0)=0.
 \tag{9}
$$

这些系数不必从复近似认定。令 $V=x^{-2}$，有准确的固定有理函数

$$
 \frac{\theta_T(\alpha z)}{\theta_T(z)^{17}}
 =u_\alpha(V),
$$

$$
 \boxed{\quad
 u_\alpha(V)=1+(12-20i)V+(-10+28i)V^2
                      +(-20-12i)V^3+(1+4i)V^4.
 \quad} \tag{10}
$$

证明这个恒等式只需有限的精确计算：比值是 $i$ 不变椭圆函数，
唯一极点在 $T$，阶至多 $16$，所以是 $V$ 的四次多项式。
常数项是 $1$；其余四项由 $z^4,z^8,z^{12},z^{16}$ 唯一确定。
可使用

$$
 \theta_T(z)=1+\frac{z^4}{12}-\frac{z^8}{10080}
             +\frac{17z^{12}}{19958400}
             +\frac{283z^{16}}{435891456000}+O(z^{20})
$$

及 $x''=6x^2-2$ 直接代入验证，给出 (10) 的四个高斯整数。
这不是只检查有限项就推断任意解析函数恒等；前面的四次多项式界
是有限核验足够的理由。

将 (8) 作 Fourier 逆变换，得到完全代数的固定系数公式

$$
 \boxed{\quad
 a_S=\frac1{17}\sum_{P\in E_0[\alpha]}
       e_\alpha(P,S)^{-1}
       \frac{q(x(P)^{-2})}{u_\alpha(x(P)^{-2})}.
 \quad} \tag{11}
$$

在 $P=O$，约定括号中的比值为 $q(0)/u_\alpha(0)=0$。
在其他核点，$x(P)\ne0$，且 $u_\alpha(x(P)^{-2})\ne0$，
因为 $\alpha P=O\ne T$。

## 3. 对全部目标惰性素数的整性

以下固定 $p\ge7$、$p\equiv3\pmod4$ 及 $L$ 中的一个 $p$ 进位。
这些素数自动不等于 $2,5,17$。

曲线、次数 $17$ 同源及所有有关的 $2$、$17$ 挠点都有良好且可分的
约化，互异的这些挠点仍互异。
所以在 (11) 的非零核点处，$x(P)$ 和 $u_\alpha(x(P)^{-2})$
均为局部单位：后者的零点除子是 $\alpha$ 下 $T$ 的逆像，
除了在 $T$ 约去的重数，而这些点与 $\ker\alpha$ 不交。
由 (10) 的整系数、$q$ 的唯一分母 $5$ 及 $17$ 可逆，得

$$
                             a_S\in\mathcal O_{L,p}.
 \tag{12}
$$

在 (7) 中可以从固定集合 $a\in\{69,103,137\}$ 中选一个使
$p\nmid a(a-1)$。这是因为这三个 $a(a-1)$ 的最大公因数为 $34$。
$\Psi_a(R_S)$ 也是局部单位：$a$ 与 $34$ 互素、$p\nmid a$，
而 $R_S$ 是非零的阶除 $34$ 的挠点，不能落入 $E_0[a]$。
所以 $U_S,X_S,Y_S$ 以及全部 $C_n(U_S,X_S,Y_S)$ 均整。

## 4. 模 $p$ 的先导项为何准确相消

写 $p=4r-1$，并取如下特征零提升：

$$
 \kappa_p=-\frac12(-1)^r\binom{2r}{r}\in\mathbb Z_{(p)}^\times.
 \tag{13}
$$

[惰性 Cartier 计算](2026-11-12-central-diagonal-inert-shift.md)
在参数 $D=1$ 时给

$$
 \delta^p=0,\qquad \delta^{p-1}X=\kappa_p,\qquad
 \mathcal D^p=-\kappa_p\partial_U
                         \quad\pmod p.
$$

令 $B=U^p-\delta^{p-2}X$。Bell/Jacobson 恒等式给

$$
 (\mathcal D+U)^p=-\kappa_p\partial_U+B,
 \qquad
 C_{p+1}=-\kappa_p+BU\pmod p.
 \tag{14}
$$

还须核对这里的实际挠点满足 $B(R_S)=0$；不能只由 $U_S$ 代数就假定。
令 $h_a=\delta\log\Psi_a$，并使用上一节选出的 $a$。
整数乘法公式及 $aR_S=R_S$ 给

$$
 h_a(R_S)=(a-a^2)U_S,
 \qquad
 \delta^{p-1}h_a(R_S)=(a^p-a^2)\delta^{p-1}U(R_S).
$$

由于 $h_a$ 是有理函数的对数导数，$\delta^p=0$ 给
$\delta^{p-1}h_a=-h_a^p\pmod p$。
利用 $a^p\equiv a$ 并除去可逆的 $a-a^2$，得到

$$
 \delta^{p-1}U(R_S)=-U_S^p,
 \quad\text{即}\quad
 \delta^{p-2}X(R_S)=U_S^p.
$$

因此所有十七个挠点都满足

$$
 \boxed{\qquad C_{p+1}(U_S,X_S,Y_S)\equiv-\kappa_p\pmod p.
 \qquad} \tag{15}
$$

这十七个相同的先导项由 (9) 的 $\sum a_S=0$ 精确消去。
它是 $b_{p+1}$ 整性的实际几何解释，并没有给出其模 $p$ 非零。

## 5. 真正目标是模 $p^2$ 的哪一项

由 (6) 与 (9)，在特征零有准确恒等式

$$
 b_{p+1}=\frac{\alpha^{p+1}}{(p+1)!}
       \sum_Sa_SC_{p+1}(U_S,X_S,Y_S).
 \tag{16}
$$

根据 (12)、(15)，下面十七个除 $p$ 后的数都整：

$$
 Z_{S,p}:=\frac{C_{p+1}(U_S,X_S,Y_S)+\kappa_p}{p}
                    \in\mathcal O_{L,p}.
 \tag{17}
$$

因为 $\sum a_S=0$，加入的 $\kappa_p$ 不改变 (16) 的总和。
Wilson 定理给 $(p+1)!/p\equiv-1\pmod p$；
在惰性位，$\alpha^p\equiv\bar\alpha$，故
$\alpha^{p+1}\equiv17$。因此目标准确成为

$$
 \boxed{\qquad
 b_{p+1}\equiv-17\sum_{S\in E_0[\bar\alpha]}a_SZ_{S,p}\pmod p.
 \qquad} \tag{18}
$$

此式右侧的点集、系数 $a_S$ 和数域均固定。
仍随 $p$ 变化的是必须计算到模 $p^2$ 的 Bell jet (17)。
$\kappa_p$ 换成另一个同余提升只给每个 $Z_{S,p}$ 加同一个数，
所以 (18) 的总和与这个提升选择无关。

## 6. 为什么十七个点还不能直接作为导数矩阵

令 $\mathcal R$ 是固定点集 $\{T+S:S\in E_0[\bar\alpha]\}$
的坐标代数。它在特征零，以及所有上述目标特征中，都是有限 étale 代数。
这样的代数上每个基域线性导数都是零：可以在分裂域中把它写成
十七个域的直积，幂等元的导数及各坐标的导数都为零。

但曲线上的 $\delta x=2y$ 在这十七个点中并非处处为零。
除 $S=O$ 给 $R_S=T$ 外，其余点不是二挠点。
所以 $\delta$ 不保持该点集的定义理想，不能下降为
$\mathcal R$ 上的一个固定十七阶线性矩阵。

换言之，知道所有 $X_S,Y_S,U_S$ 在固定数域中，
并不能通过对它们的取值逐次求导来计算 $C_n$。
必须保留邻域的 jet；先在点集上取商再求导会丢失该信息。
同样，模 $p$ 的 Frobenius 置换只解释 (15) 的先导层，
它没有给出 (17) 除 $p$ 后的剩余值。

本篇不否定存在另一个真正保留连接和整格的固定 crystalline 对象。
它给出了任何这种新比较必须满足的准确接口 (18)，并排除了
仅凭有限 theta 基或固定挠点集就直接调用 Chebotarev 的跳步。
