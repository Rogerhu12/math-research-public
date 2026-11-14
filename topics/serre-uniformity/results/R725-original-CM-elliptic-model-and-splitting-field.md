# R725：原正 CM 因子的显式椭圆系数、最小分裂域与真实 p 处微分格

日期：2026-11-14。状态：**下述代数公式、原正角色识别、域次数及 p 处最小模型已证明。** 它们生成一个与原 CM 因子匹配的椭圆分量；尚未生成原商映射 $q$ 到这个模型的同源、$\beta$ 的坐标或实际高度首项。

本篇继续 R724 的代数输入，不把“几何上是椭圆幂”当作已给出原模参数化。新增的是一个只使用固定椭圆曲线的 $p$-除法多项式、有限乘法和一个三同源的具体系数公式。其非零性和赋值由原正 CM 标签严格决定。

## 1. 固定原角色与一个有准确有限角色的基曲线

令
$$
p\ge41,\qquad p\equiv2,5\pmod9,\qquad
K=\mathbb Q(s),\quad s=\sqrt{-3},\quad
\zeta=(-1+s)/2,\quad n=p+1,\quad m=n/6.
\tag{725.1}
$$

固定同一 $p$ 进嵌入及正 CM 型。保留 R616 的原指定本原角色
$$
\theta=\theta_{-1},\qquad
\theta(\zeta)=\zeta^{-1},\qquad\theta(s)=-1.
\tag{725.2}
$$
它平凡于 $\mathbb F_p^\times$，在其商上阶为 $n$。
本篇的六阶投影只用显示的两项原标记；因此也适用于同一个正 CM
Galois 轨道的全部嵌入。若用复根表示 $\theta$，仍按原 Teichmüller
标签输送该根，不另取相反角色。

取
$$
E_{27}:\quad Y^2=X^3+16,\qquad \omega_{27}=\frac{dX}{2Y},
\qquad t=-X/Y.
\tag{725.3}
$$
它通过 $X=4x,\ Y=8y+4$ 与 $y^2+y=x^3$ 同构。
后一整模型的判别式是 $-27$。正 CM 算子为
$[\zeta](X,Y)=(\zeta X,Y)$，故 $[\zeta]^*\omega_{27}=\zeta\omega_{27}$。

每个与 $3$ 互素的理想有唯一生成元 $a\equiv1\pmod3$：
$K$ 类数为一，且 $\mu_6\to(\mathcal O_K/3)^\times$ 是同构。
$E_{27}$ 的正 CM Hecke 角色准确为
$$
\psi_0((a))=a,\qquad a\equiv1\pmod3,
\tag{725.4}
$$
导子为 $(3)$。可以直接核其有限规范：其全部 $3$-挠点在 $K$ 上，
非零点的 $X$ 坐标为 $0$ 和 $-4\zeta^j$，相应 $Y$ 坐标为
$\pm4$ 和 $\pm4s$。因此 CM Frobenius 的生成元在模 $3$ 上为 $1$；
这在六个单位倍数中唯一确定 (725.4)。导子不能降低到 $(s)$，
因为 $\zeta\equiv1\pmod s$ 而 $\zeta\ne1$，与无穷型一的定义不相容。
这也与 Schütt 的 Example II.5.2、Remark II.10.7 的同一曲线和角色一致。

令 $\alpha=\sqrt[3]4>0$，保留 R616 的算术 Artin 规范
$$
\kappa(\sigma)=\frac{\sigma\alpha}{\alpha}.
\tag{725.5}
$$
对 primary $a\equiv1\pmod3$，原 $\epsilon_3(a)=1$，故 R575/R616 的
实际正 Hecke 角色满足
$$
\psi=\Psi_\theta\kappa=\psi_0\varepsilon,\qquad
\varepsilon((a))=\theta(a\bmod p)\kappa((a)).
\tag{725.6}
$$

这里 $\varepsilon$ 是有限角色。$\theta(a)$ 单独写在任意生成元上会有单位
歧义，(725.6) 始终先取 (725.4) 的 primary 生成元。它也是下面实际
$p$-挠点表示与 $\kappa$ 的乘积，因此没有凭空指定一个不同的 ray 角色。

## 2. 全部域由固定曲线的 p-挠点给出

令
$$
\mathcal M=K(E_{27}[p]),\qquad
\rho_p:\operatorname{Gal}(\mathcal M/K)
             \longrightarrow(\mathcal O_K/p)^\times .
\tag{725.7}
$$
所有 CM 自同态在 $K$ 上定义；$E_{27}[p]$ 是一个秩一的
$\mathcal O_K/p$-模，因此 $\rho_p$ 单射。其像实际上是整个
$\mathbb F_{p^2}^\times$。

说明满射及所需局部规范。$p$ 在 $K$ 中惰性，$E_{27}$ 在 $p$ 好超奇异；
其形式群的模 $p$ 乘法首个非零次数为 $p^2$。因此对任一非零 $p$-挠点 $P$，
$[p](T)/T$ 的 Weierstrass 多项式为次数 $p^2-1$ 的 Eisenstein 多项式：
常数为 $p$ 乘单位，其他非首项系数被 $p$ 整除，首项为单位。
全部非零 $p$-挠点都在形式群中，故
$$
v_p(t(P))=\frac1{p^2-1},\qquad
[K_p(P):K_p]=p^2-1.
\tag{725.8}
$$
上面的全局单射给反向次数上界，于是
$$
\operatorname{Gal}(\mathcal M/K)=\mathbb F_{p^2}^{\times}.
\tag{725.9}
$$
特别地，$\mathcal M/K$ 在 $p$ 处完全、温和分歧，只有一个 $p$ 上方的素理想。

也可由 (725.4) 和 CRT 核准同一 Galois 标记：对与 $3p$ 互素的
理想 $(a)$，其算术 Artin 在 $E_{27}[p]$ 上是 $[a\bmod p]$。
取 $a\equiv1\pmod3$ 并任意指定 $a\bmod p$，得到全部剩余类。
这里是算术 Frobenius，不把这个作用换成其逆。

定义
$$
H_0=\mathcal M^{\mathbb F_p^\times},\qquad
G=\operatorname{Gal}(H_0/K)\simeq
            \mathbb F_{p^2}^\times/\mathbb F_p^\times\simeq C_n .
\tag{725.10}
$$
令 $G_6\subset G$ 为唯一六阶子群。它由 $[\zeta]$ 和 $[s]$ 的
projective classes 生成：前者阶三，后者阶二，因为 $s^2=-3\in\mathbb F_p^\times$，
而 $s\notin\mathbb F_p$。置
$$
L=H_0^{G_6},\qquad [H_0:K]=n,\qquad [L:K]=m.
\tag{725.11}
$$
同样，$H_0/K$、$L/K$ 在 $p$ 完全分歧，剩余域仍为 $\mathbb F_{p^2}$。

为同时记录原正有限角色，令 $H$ 为 (725.6) 的 $\ker\varepsilon$
对应的域。它包含在 $\mathcal M K(\alpha)$ 内，并且
$$
[H:K]=n,\qquad H^{\ker(\varepsilon^6)/\ker\varepsilon}=L,\qquad [H:L]=6.
\tag{725.12}
$$
不能把 $\theta$ 与 $\kappa$ 的阶机械相乘。严格理由是：
$\kappa$ 取值于 $\mu_3\subset\mu_n$，故 $\varepsilon$ 的像包含于 $\mu_n$；
给任意 $u\bmod p$，用 CRT 取 $a\equiv1\pmod6$、$a\equiv u\pmod p$。
由于 $\kappa$ 的导子为 $(6)$，此时 $\kappa((a))=1$，故
$\varepsilon((a))=\theta(u)$。于是其像恰为 $\mu_n$。
再由 $\varepsilon^6=(\theta\rho_p)^6$，即得同一个 $L$ 及 (725.12)。

此外 $L/K$ 的导子仅支持于 $p$：$\theta^6$ 平凡于全部六个单位，
所以不再需要 primary 选择，其理想角色按模 $p$ 定义。
这项说明没有要求 $H_0$ 与 $K(\alpha)$ 在 $3$ 处不相交，也没有把它们
在 $3$ 的可能角色抵消略去。实际上 $K(\alpha)/K$ 在 $2$ 分歧，
而 $\mathcal M/K$ 在 $2$ 未分歧；这也独立保证两域交为 $K$。

## 3. 一个只含两个有限乘积的非零系数

固定任一 $P\in E_{27}[p]\setminus\{0\}$，并定义
$$
w(P)=\prod_{a\in\mathbb F_p^\times}t([a]P)\in H_0,\qquad
r_0=\frac{w(P)-w([s]P)}2,\qquad b=r_0^6.
\tag{725.13}
$$
整数代表的选择不影响 $[a]P$。所有因子有定义且非零：
$X=0$ 是 $3$-挠点，$Y=0$ 是 $2$-挠点，均不可能是非零 $p$-挠点。

**定理 725.1。** 上式满足
$$
\sigma(r_0)=\theta(\sigma)^{-1}r_0\quad(\sigma\in G_6),\qquad
b\in L,
\tag{725.14}
$$
$$
v_p(w)=v_p(r_0)=\frac1n,\qquad v_p(b)=\frac1m,\qquad
K(r_0)=H_0,\quad K(b)=L.
\tag{725.15}
$$
特别地，$r_0$ 与 $b$ 对所有允许的 $p$ 均严格非零。

证明。标量乘法重排 (725.13) 的乘积，所以 $w\in H_0$。
由于 $t([\zeta]Q)=\zeta t(Q)$，有
$$
w([\zeta]P)=\zeta^{p-1}w(P)=\zeta w(P).
$$
而 $[s]^2=[-3]$ 是标量，故 $w([s]^2P)=w(P)$。
于是 $r_0$ 在 $[\zeta]$、$[s]$ 下分别乘以 $\zeta$、$-1$，
正是 (725.14)；第六次幂下降到 $L$。等价地，
$$
r_0=\frac16\sum_{\sigma\in G_6}\theta(\sigma)\sigma(w).
\tag{725.16}
$$
此处投影到 $\theta^{-1}$，所以求和的权重是 $\theta$；没有把两个逆号交换。

由 (725.8)，乘积的赋值为 $(p-1)/(p^2-1)=1/n$。
对剩余单位 $u$ 的 CM 作用，在同一整数形式参数中
$t([u]Q)=u\,t(Q)+O(t(Q)^2)$。因此
$$
\frac{\sigma_u w}{w}\equiv u^{p-1}
       \pmod{\mathfrak m_{\mathcal M,p}} .
\tag{725.17}
$$
对 $u=s$，右侧是 $-1$。因为 $p>3$，(725.13) 给
$r_0/w\equiv1$，所以 $v_p(r_0)=1/n$，并非只给一个可能相消的下界。
随后 $v_p(b)=6/n=1/m$。

$K_p(r_0)/K_p$ 的分歧指数必须被 $n$ 整除，因为其中出现赋值 $1/n$；
但它包含于次数 $n$ 的 $H_{0,p}$，故二者相等。同理
$K_p(b)=L_p$。局部次数已达到全局次数上界，得到最后两式。$\square$

改变 $P$ 为 $[u]P$ 只使 $r_0,b$ 作相应的 $G$ 共轭，不换一个无关模型。
若在复数实现中取正实周期上的 $P$，则 $w(P)$ 为实数，
$w([s]P)$ 也为实数，因为复共轭把 $[s]P$ 送到 $-[s]P$，
而乘积遍历所有非零标量。因此 $r_0\in\mathbb R$、$b>0$。
这里 $H_0/\mathbb Q$ 是二面体扩张：复共轭在
$\mathbb F_{p^2}^\times/\mathbb F_p^\times$ 上作用为逆。
实 $p$-挠点构成唯一的循环子群；其中任取非零 $P$ 都只重排乘积，
所以这项实选择也固定了同一个 $b$。这时
$$
L^+=\mathbb Q(b),\qquad [L^+:\mathbb Q]=m,\qquad L=L^+K.
\tag{725.18}
$$
这里“实子域”指这一个复共轭的固定域；不声称它是 Galois 或全实域。

## 4. 具体除法多项式／resultant 形式

(725.13) 不是必须先枚举一个未知 Jacobian 上的点。
令 $d=(p-1)/2$，取这个循环核的 monic 多项式
$$
k_P(T)=\prod_{a\in\mathbb F_p^\times/\{\pm1\}}
          (T-X([a]P)).
\tag{725.19}
$$
它是 $E_{27}$ 的原 $p$-除法多项式的一个循环核因子，所有群运算都在固定
模型 (725.3) 上。

正 CM 三同源 $[s]$ 的准确公式是
$$
X([s]Q)=-\frac{X^3+64}{3X^2},\qquad
Y([s]Q)=-\frac{Y(X^3-128)}{3sX^3},
\tag{725.20}
$$
且 $[s]^*\omega_{27}=s\,\omega_{27}$。
可将标准三同源
$(X,Y)\mapsto((X^3+64)/X^2,\ Y(X^3-128)/X^3)$
到 $Y^2=X^3-432$ 与缩放 $s^{-1}$ 复合，逐项验证上述公式及微分。
因此
$$
t([s]Q)=s\,t(Q)\frac{X^3+64}{X^3-128}.
\tag{725.21}
$$

于是全部所需数由有限 resultant 给出：
$$
w=(-1)^d\,\frac{k_P(0)^2}{\operatorname{Res}_T(k_P(T),T^3+16)},
\qquad
R_P=\frac{\operatorname{Res}_T(k_P(T),T^3+64)}
           {\operatorname{Res}_T(k_P(T),T^3-128)},
\tag{725.22}
$$
$$
\boxed{\quad
b=\left\{\frac{w}{2}
       \left[1-(-3)^d R_P^2\right]\right\}^{6}.
\quad}
\tag{725.23}
$$
所有 resultant 分母非零：$Y(Q)=0$ 或 $Y([s]Q)=0$
都会使一个非零 $p$-挠点成为 $2$-挠点。$[s]$ 在 $E[p]$ 上可逆。
式 (725.23) 只用固定椭圆群的确切代数坐标，不用复浮点识别或有限窗口猜测。

其定义域多项式还可准确写为
$$
F_p(T)=\prod_{\sigma\in G/G_6}(T-\sigma(b))\in K[T].
\tag{725.24}
$$
它次数恰为 $m$，是 $b$ 的最小多项式。
在 $K_p$ 上，它是 Eisenstein 多项式：每个根赋值 $1/m$，
每个非首项系数的赋值为正整数，常数项赋值恰为 $1$。
若按 (725.18) 选择实 $P$，复共轭重排此共轭集合，
因此实际上 $F_p(T)\in\mathbb Q[T]$。
本文给出其全部系数的有限精确代数表达；尚未声称已展开某个大 $p$ 的系数表。

## 5. 原正 κ4 的椭圆方程与缩放逆号

定义
$$
\boxed{\quad C/L:\quad y^2=x^3+b,\qquad
\omega_C=\frac{dx}{2y}.\quad}
\tag{725.25}
$$
取
$$
r=r_0/\alpha .
\tag{725.26}
$$
因为 $\alpha^6=16$，有 $16r^6=b$。
对 $G_L$ 的元素，$\theta\rho_p$ 取值于 $\mu_6$，
(725.14) 与 (725.5) 给
$$
\sigma r=\varepsilon(\sigma)^{-1}r.
\tag{725.27}
$$
所以 $r\in H$。其赋值仍为 $1/n$，由 (725.12) 的次数上界可进一步得
$K(r)=H$；在 $L_p$ 上 $r$ 满足的 $T^6-b/16$ 为 Eisenstein 多项式。
在 $H$ 上有准确同构
$$
\varphi:E_{27}\longrightarrow C,\qquad
(X,Y)\longmapsto(r^2X,r^3Y),\qquad
\varphi^*\omega_C=r^{-1}\omega_{27}.
\tag{725.28}
$$

**定理 725.2。** $C/L$ 的正 CM Tate 角色是
$$
\psi_0|_{G_L}\,\varepsilon|_{G_L}=\psi|_{G_L}.
\tag{725.29}
$$
特别地，对原 $A=A_{\theta,1}$、$g=[F:\mathbb Q]$，
$$
A_L\sim_L C^g.
\tag{725.30}
$$

证明。将 $C$ 的 Tate 模通过 $\varphi$ 识别到 $E_{27}$。
其下降因子是 $\varphi^{-1}\sigma(\varphi)$，即按
$\sigma r/r=\varepsilon^{-1}$ 作坐标缩放。
在正 CM 规范中，单位 $u$ 的 CM 乘法 $[u]$ 是
$(X,Y)\mapsto(u^{-2}X,u^{-3}Y)$，其微分乘 $u$。
所以这一个缩放是 $[\varepsilon]$，不是 $[\varepsilon^{-1}]$。
由此得到 (725.29)。

原 CM 型的全部 $K$-嵌入固定 $\mu_6\subset K$。
在 $G_L$ 上它们的有限角色值都等于同一个 $\varepsilon$，
故原 $A_L$ 的正 CM 特征全部为 (725.29)，共轭特征也分别相同。
CM Hecke 角色／Tate 表示的同源判据给 (725.30)。
等价地，可直接应用 González–Lario Theorems 1.1–1.2 的一般 CM 部分。
这里未使用该文只针对 $K=\mathbb Q(\sqrt{-p})$、水平 $p^2$ 的后半部特例。$\square$

这个逆号也给一个交叉核查：若改用相反扭向 $\kappa^{-1}$，
所需缩放变成 $r_0\alpha$，椭圆方程的常数变为 $256b$，
而非 (725.25)。本题使用的是 $b$，保持原正 $\kappa_4$。

$L$ 不只是一个足够的域，还是原 $A$ 的几何自同态的最小定义域。
由 González–Lario Theorem 1.2，它对应
$$
\{\mathfrak a:\psi(\mathfrak a)\in K^\times\}.
\tag{725.31}
$$
(725.6) 将此条件准确变为 $\varepsilon(\mathfrak a)\in\mu_6$，
即 $\varepsilon^6=1$，故它就是 (725.11)。
若自行用特征核查，同一个结论来自所有 $K$-嵌入的比
$\varepsilon^{a-1}$：$\ a\in(\mathbb Z/n)^\times,\ a\equiv1\pmod3$；
这些 $a-1$ 与 $n$ 的最大公因数恰为 $6$。
除 $2,3$ 外的素数可用 CRT 令 $a\not\equiv1$ 排除，
$2$ 的高次可令 $a\equiv3\pmod4$ 排除，而 $v_3(n)=1$。
复共轭不固定几何 CM 中心 $K$，所以最小域在 $\mathbb Q$ 上也必须包含 $K$。

## 6. 真实 p 处最小模型与微分，不把它当成原 q 的格

由 (725.15)，在 $L_p$ 的整数赋值 $v_L$ 下有
$$
v_L(b)=1,\qquad v_L(\Delta_C)=v_L(-432b^2)=2.
\tag{725.32}
$$
因为 $p>3$，(725.25) 是整且最小的 Weierstrass 模型：
判别式赋值已经小于 $12$，不可能再作整模型的判别式降低。
Tate 算法给类型 II；$\omega_C$ 是该模型的 Néron 微分。
在 $H_p$ 上，(725.28) 将它送到固定好约化模型的微分，准确尺度为
$$
v_p(r)=\frac1n,\qquad
\varphi^*\omega_C=r^{-1}\omega_{27}.
\tag{725.33}
$$
这里 $\alpha$ 是 $p$ 单位；由于 $p\equiv2\pmod3$，
$4$ 在 $\mathbb Q_p$ 中有唯一立方根，$\kappa_p=1$，
所以没有额外的 $p$ 处分歧或隐藏立方尺度。

若需与 R592 的 $E_0:y^2=x^3-1$ 比较，可取 $u^6=-16$，
令 $E_0\to E_{27}$ 为坐标缩放 $u$。复合到 (725.25) 的尺度是 $ur$，
微分尺度是 $(ur)^{-1}$，且 $v_p(u)=0$。
这只是两个明确椭圆模型间的同构；它**不是**原
$q^*\omega_\sigma=c_\sigma\mathcal F_\sigma\,dz_{\rm flat}$
中的 KS／模参数化常数 $c_\sigma$。后者的赋值仍须通过真正的
$J_X\to A\to C$ 同态核对，不能由 (725.33) 直接宣布为单位。

## 7. 一个已给具体值的 isogeny cocycle

对与 $6p$ 互素的理想 $\mathfrak a$，令 $a=\psi_0(\mathfrak a)$
为 primary 生成元，用同一算术 Artin 作用于 $r_0$。
定义
$$
\boxed{\quad
\lambda(\mathfrak a)
=a\,\kappa(\mathfrak a)\,
        \frac{r_0}{\mathfrak a(r_0)}\in L^\times .
\quad}
\tag{725.34}
$$

商 $r_0/\mathfrak a(r_0)$ 的确在 $L$：$G$ 交换，
而 $G_6$ 在分子和分母上的同一 $\theta^{-1}$ 因子相消。
它满足
$$
\lambda(\mathfrak a\mathfrak b)
 =\lambda(\mathfrak a)\,
   \mathfrak a\bigl(\lambda(\mathfrak b)\bigr),\qquad
\lambda(\mathfrak a)=\psi(\mathfrak a)
   \quad\text{若 }\mathfrak a|_L=1.
\tag{725.35}
$$
因此这是 González–Lario 的原 CM 同源类所需的 cocycle，
其值由 (725.13) 或 (725.23) 明确计算，不再留作未知的 norm 方程解。

对整理想，它还由真实椭圆同源给出；对分式理想则是清分母后的
quasi-isogeny。在 $H$ 上令
$$
\mu_{\mathfrak a}
  ={}^{\mathfrak a}\varphi\circ[a]\circ\varphi^{-1}
  :C\longrightarrow{}^{\mathfrak a}C .
\tag{725.36}
$$
其坐标比例均在 $L$，且
$$
\mu_{\mathfrak a}^*({}^{\mathfrak a}\omega_C)
  =\lambda(\mathfrak a)\omega_C.
\tag{725.37}
$$
这是因为 $r/\mathfrak a(r)=
\kappa(\mathfrak a)r_0/\mathfrak a(r_0)$。
所以这里也没有仅写一个抽象 cohomology class 而不指定微分方向。

该 cocycle 可代入 González–Lario §4 的有限 Gauss sums 与
$K$-线性 projector，生成标准 newform 空间中的椭圆方向。
但其规范化是一个 Fourier 首系数条件；即便方向已给出，也仍要确定原
六水平/Cartan 向量与该方向之间的实际同态和微分比例。
本文没有把标准 $\Gamma_1(108p^2)$ 的形式自动当成原 $X_1$ 上已归一的
$q^*\omega$。

## 8. 对当前高度任务新增和仍缺的输入

已获得的实际代数数据是：

1. 固定的有理曲线 (725.3) 及完全核定的 primary Hecke 角色。
2. 原最小分裂域 $L$、次数 $(p+1)/6$、全局定义式
   (725.11)、原正有限角色域 $H$ 及准确的 $H/L$ 六次扩张。
3. 自动非零的两个有限乘积 (725.13)，或者单个核多项式的
   resultant 公式 (725.23)；它给 $L$ 的生成元和原正 CM 椭圆系数。
4. 原正 $\kappa_4$ 的准确模型 $C:y^2=x^3+b$，真实的 $p$ 处
   最小模型、微分尺度及已指定值的同源 cocycle (725.34)。

这些结论不需要 R616 的秩或非挠前提。它们描述原阿贝尔簇的 CM
几何及其椭圆分量。用于 R724 的高度计算时，仍须提供原
$J_X\to A\to C$ 同态、$\beta=q[c_1-c_0]$ 的该模型坐标、完整 NS/Picard
线丛运输及原局部刚性化。本篇尚未算出任一真实 $E_{ij}$ 的首个高度系数，
也不由类型 II、椭圆幂或有限公式宣布候选排除。

没有运行新的长计算，也没有重跑封存的 $p=41$ 原挠点轨道。
上式是有限精确代数构造；若以后展开某个 $F_p(T)$ 或计算实际 $q/\beta$，
应在公开 Actions 保存原参数、完整多项式、同态校验与全部规范常数。

## 来源

- J. González, J.-C. Lario, *Modular elliptic directions with complex
  multiplication*, Comment. Math. Helv. 86 (2011), 317–351；
  作者稿 <https://arxiv.org/pdf/0810.4224>，
  Theorems 1.1–1.3、§3、§4，特别 cocycle 的限制与最小分裂域。
  本文只使用一般 CM 部分，不套该文后面的不同 CM 域特例。
- M. Schütt, *Hecke eigenforms and the arithmetic of singular K3 surfaces*
  (2006)，Example II.5.2、Remark II.10.7：
  <https://webdoc.sub.gwdg.de/ebook/dissts/Hannover/Schuett2006.pdf>。
  同一基曲线的有限角色也已在 §1 用完整 $3$-挠点独立核准。
- 本仓库
  [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)、
  [R588](R588-actual-toric-norm-and-CM-normalization.md)、
  [R616](R616-original-CM-point-difference-and-explicit-height-basis.md)、
  [R724](R724-original-Chow-Heegner-height-matrices-and-canonical-jet-evaluation.md)。
