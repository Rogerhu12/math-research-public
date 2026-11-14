# R348：实际六层的 CM 秩零商与统一正的一阶矩

**现行范围更正（R575）**：实际六层的甲板作用应为 δζ*ω=ζω，正 CM 型的真实家族为 Ψθκ4，根号−1且中心值恒零。原 §§1、5、8 将 Ψθκ4^-1 放入该实际曲线并推出秩零商的结论撤回。§7 的正平均仅保留为相反扭向家族自身的解析结论。完整证明见 [R575](R575-correct-actual-sixfold-CM-deck-and-cubic-twist.md)。

## 更正前正文（保留供复核，受上述范围更正约束）

**状态：已证明。** R263/R266 实际整数参数所给的六层，在每个 $p\ge41$、$p\equiv2\pmod3$ 上都有正维的 $\mathbb Q$ 秩零商。证明从甲板自同构对微分的作用确定固定三次扭曲，证明 CM 成分实际出现，并以显式一阶矩严格证明中心值非零。尚未证明所需的特征 $p$ 形式浸入；原统一性目标仍未完成。

## 1. 结论与范围

令 $p\ge41$ 为素数，$p\equiv2\pmod3$，并令

$$
X_p=X_{\mathrm{ns}}^+(p),\qquad
Z_p=\operatorname{Norm}\!\left(
X_p\times_{\mathbb P^1_j}\mathbb P^1_a\right),\qquad
j=6912a^3(1-a^3).
\tag{348.1}
$$

这里取光滑射影规范化。则 $Z_p$ 几何连通，并且有一个正维的 $\mathbb Q$ 上商

$$
J_{Z_p}\longrightarrow A,\qquad \#A(\mathbb Q)<\infty.
\tag{348.2}
$$

该商可以取为下面显式 CM 新形式之一的模 abelian variety。置

$$
K=\mathbb Q(s),\quad s=\sqrt{-3},\quad
\zeta=\frac{-1+s}{2},\quad
\mathcal O=\mathbb Z[\zeta],\quad
T_p=(\mathcal O/p)^\times/\mathbb F_p^\times.
\tag{348.3}
$$

在复数中取 $\operatorname{Im}(s)>0$。固定集合

$$
\Theta_p=\left\{
\theta:T_p\longrightarrow\mathbb C^\times:
\theta(\zeta)=\zeta^{-1},\quad \theta(s)=-1
\right\},\qquad
|\Theta_p|=h_p=\frac{p+1}{6}.
\tag{348.4}
$$

对 $(\alpha)$ 与 $3p$ 互素，定义无穷型为 $(1,0)$ 的 Hecke 角色

$$
\Psi_\theta((\alpha))
=\alpha\,\epsilon_3(\alpha)\,\theta(\alpha\bmod p),
\tag{348.5}
$$

其中 $\epsilon_3:(\mathcal O/s)^\times=\mathbb F_3^\times
\to\{\pm1\}$ 为非平凡角色。令

$$
\kappa_4(\sigma)=\frac{\sigma(\sqrt[3]4)}{\sqrt[3]4}
\quad(\sigma\in G_K),\qquad
g_\theta=f_{\Psi_\theta\kappa_4^{-1}}.
\tag{348.6}
$$

Artin 互反约定是局部 uniformizer 对应算术 Frobenius。则：

1. 每个 $g_\theta$ 是权 $2$、平凡 nebentypus、准确层 $108p^2$ 的 CM 新形式，其相应 $\mathbb Q$ 模因子实际出现在 $J_{Z_p}$ 中。
2. 每个 $g_\theta$ 的全局根号为 $+1$。
3. 有完全显式、对所有上述 $p$ 一致的估计

$$
\frac1{h_p}\sum_{\theta\in\Theta_p}L(g_\theta,1)
>
\frac{5393}{6150}>0.
\tag{348.7}
$$

所以至少一个实际出现的 CM 因子具有非零中心值；Kato 的秩零定理给出 (348.2)。

本结论不依赖实际参数 $a,d,b$ 的大小。R263/R266 已进入的共同二、三除域分支满足
$a^3+db^3=1$，其实际 $p$ 水平点连同 $a$ 给出 $Z_p(\mathbb Q)$ 的点。特别地，本结论适用于该分支的 $p\equiv2,5\pmod9$；证明本身只需要 $p\equiv2\pmod3$。

这里尚未证明从 $Z_p$ 到 (348.2) 的 Abel–Jacobi 商映射在相关特征 $p$ 特殊点处为形式浸入，也未识别所有异常点与 CM 点在非分裂水平稳定模型上的同一分支。因此 (348.2) 不是 Serre 统一性的完成证明。

## 2. 固定的六层及其扭曲

Brau–Jones 的模曲线 $X'(6)$ 对应以下群。令

$$
\vartheta:\mathrm{GL}_2(\mathbb F_3)
\longrightarrow \mathrm{GL}_2(\mathbb F_2)\simeq S_3
\tag{348.8}
$$

为核 $Q_8$ 的满射，令 $H_6$ 为其图像图式

$$
H_6=\{(\vartheta(g),g):g\in\mathrm{GL}_2(\mathbb F_3)\}.
\tag{348.9}
$$

Brau–Jones Theorem 1.4 给出一个有理坐标 $u$，使

$$
X'(6)\simeq\mathbb P^1_u,\qquad
j=2^{10}3^3u^3(1-4u^3).
\tag{348.10}
$$

令 $Z'_p$ 为 $X_p$ 与 (348.10) 的规范化纤维积。若 $\alpha^3=4$，则

$$
\iota:Z_p\longrightarrow Z'_p,\qquad u=a/\alpha
\tag{348.11}
$$

是在 $\mathbb Q(\alpha)$ 上的同构。两边都在 $K$ 上有甲板自同构

$$
\delta_\zeta:u\longmapsto\zeta u
\quad\text{或}\quad a\longmapsto\zeta a.
\tag{348.12}
$$

对任意 $\sigma\in G_{\mathbb Q}$，把
$\kappa_4(\sigma)=\sigma(\alpha)/\alpha$ 视为取值于带自然 Galois 作用的 $\mu_3$ 的 cocycle，则

$$
\sigma(\iota)\iota^{-1}
=\delta_{\kappa_4(\sigma)^{-1}}.
\tag{348.13}
$$

这固定了曲线扭曲本身；其在 CM Tate 模上的方向仍须计算，见 §5。

在几何上，
$H_6\cap(\mathrm{GL}_2(\mathbb F_2)\times
\mathrm{SL}_2(\mathbb F_3))$ 除去 $Q_8$ 后是
$S_3\times C_3$ 中的对角 $C_3$。所以 (348.10) 的几何 Galois 闭包是可解群 $S_3\times C_3$ 的覆盖。另一方面，$X_p$ 的 Galois 闭包群为简单群 $\mathrm{PSL}_2(\mathbb F_p)$。二者没有非平凡共同商，故纤维积几何连通。

实际 $a$ 层包含 R330 的判别式二层，因为

$$
j=1728-3t^2,\qquad t=24(2a^3-1).
\tag{348.14}
$$

因此本稿新增的 CM 成分必须来自图式 $H_6$ 的标准表示部分。它不能来自 R330 已证明中心值恒零的二层部分。

由于 $p$ 在 $K$ 中惰性，$j=0$ 椭圆曲线的 $\mathcal O/p$ 作用给一个非分裂 Cartan；$G_{\mathbb Q}$ 正规化此作用，故给出
$c\in X_p(\mathbb Q)$。$(c,a=1)$ 在 $Z_p$ 上给出有理点 $c_1$。确实

$$
\left.\frac{d}{da}\bigl(6912a^3(1-a^3)\bigr)\right|_{a=1}
=-20736\ne0,
\tag{348.15}
$$

故规范化在该支不增加剩余域。对 $p>3$，此导数还是 $p$ 进单位。可以用 $c_1$ 作为 Abel–Jacobi 基点；这只说明所加六层在该支 étale，不识别 $X_p$ 的特征 $p$ 分支。

## 3. 原始 CM 角色及 $p$ 处的符号

$\mathcal O$ 是类数一的环，单位群为 $\mu_6$。在 $T_p$ 中，$\zeta$ 的类有阶 $3$，$s$ 的类有阶 $2$；两者生成阶 $6$ 的子群。因此 (348.4) 的角色恰有 $h_p$ 个。

(348.5) 与生成元的选择无关：乘以 $\zeta$ 时三个因子的乘积改变量为
$\zeta\cdot1\cdot\zeta^{-1}=1$；乘以 $-1$ 时为
$(-1)\cdot(-1)\cdot1=1$。中国剩余定理还说明有限导子准确为

$$
\mathfrak f(\Psi_\theta)=(s)(p).
\tag{348.16}
$$

在 $s$ 处的剩余二次角色与在 $p$ 处的非平凡 $\theta$ 都不能删去。对与 $3p$ 互素的有理整数 $n$，

$$
\Psi_\theta((n))=\chi_{-3}(n)n.
\tag{348.17}
$$

由 Hecke–Shimura theta 构造，

$$
f_\theta(z)=
\sum_{\mathfrak a\subset\mathcal O}
\Psi_\theta(\mathfrak a)q^{\mathrm N\mathfrak a}
\in S_2^{\mathrm{new}}(\Gamma_0(9p^2))
\tag{348.18}
$$

为归一化新形式，nebentypus 平凡。与导子不互素的理想项取零。由于 $K$ 中与 $3$ 互素的理想范数模 $3$ 为 $1$，有

$$
a_n(f_\theta)=0\quad\text{除非 }n\equiv1\pmod3.
\tag{348.19}
$$

特别地 $f_\theta\otimes\chi_{-3}=f_\theta$。在惰性素数 $2$ 处，

$$
a_2(f_\theta)=0,\qquad a_4(f_\theta)=-2.
\tag{348.20}
$$

下面采用单位化的局部角色 $\nu_{\theta,v}$。在 $p$ 处，其在单位上的限制是 $\theta^{-1}$，而由有理主元 $p$ 的全局乘积公式得

$$
\nu_{\theta,p}(p)=-1.
\tag{348.21}
$$

令 $e_p(x)=\exp(2\pi i x/p)$。对 $T_p$ 的任意非平凡角色 $\theta$，

$$
G_p(\theta)=
\sum_{u\in\mathbb F_{p^2}^{\times}}
\theta(u)e_p(\operatorname{Tr}(u))
=p\,\theta(s).
\tag{348.22}
$$

证明：迹为零的非零元素恰为 $\mathbb F_p^\times s$，其角色和为
$(p-1)\theta(s)$。由于 $\theta$ 在 $\mathbb F_p^\times$ 上平凡，任意固定非零迹纤维的角色和相同，记为 $S$。总角色和为零，故 $S=-\theta(s)$。再用
$\sum_{t\in\mathbb F_p^\times}e_p(t)=-1$ 即得。

本族中 $\theta(s)=-1$，所以未分歧二次诱导的局部根号为

$$
\epsilon_p(f_\theta)
=\nu_{\theta,p}(p)\frac{G_p(\theta)}p
=+1.
\tag{348.23}
$$

平凡中心角色的新向量的 Atkin–Lehner 符号等于其局部 epsilon 符号，因此

$$
W_{p^2}f_\theta=f_\theta.
\tag{348.24}
$$

该符号等式使用 Schmidt Theorem 3.2.2；(348.22)–(348.23) 给出本处所需的全部具体 Gauss 计算。

## 4. $f_\theta$ 确实出现于未扭曲六层

先保留整个模六结构，再在模 $p$ 上用 Chen 关系。取全级 $6p$ 曲线所有几何分量的 Jacobian，在有理同源范畴内取 $H_6$ 不变对象，记为 $M$。它仍有交换的
$G_p=\mathrm{GL}_2(\mathbb F_p)$ 作用。de Smit–Edixhoven Theorem 2(2) 给出

$$
M^{N_{\mathrm{sp}}}\oplus M^{G_p}
\simeq M^{N_{\mathrm{ns}}}\oplus M^{B_p}.
\tag{348.25}
$$

$M^{G_p}=J_{X'(6)}=0$，且
$M^{N_{\mathrm{ns}}}=J_{Z'_p}$。

把有序互补 $p$ 子群变为 $p^2$ 循环同源时，沿同源运输全部模六标记。交换两个 $p$ 子群、再用对偶同源运输，标记上的复合是 $[p]$。这里 $p\equiv5\pmod6$，故模六的复合为 $-I_6$；它属于 $H_6$，也由椭圆曲线的自同构 $[-1]$ 消去。因此交换子群确实给通常 $W_{p^2}$，没有额外的模六图式变换。单个 $p$ 同源会更换 Weil 配对的值；上述构造在所有配对分量上进行并在 $H_6$ 商后下降到 $\mathbb Q$，没有把它误认成保持某个固定配对分量的映射。该构造同时保留 (348.12) 的甲板作用。

下面精确核算 $f=f_\theta$ 在模六结构中的位置。令
$D_6=\operatorname{diag}(6,1)$。有

$$
D_6\Gamma_0(36p^2)D_6^{-1}
=(\{\pm I\}\Gamma(6))\cap\Gamma_0(p^2).
\tag{348.26}
$$

因为共轭后两个非对角元都被 $6$ 整除，而行列式一迫使两个对角元模 $6$ 同为 $1$ 或同为 $-1$。于是 $f$ 的三个二旧向量，在右侧曲线上可写为

$$
h_0(z)=f(z/6),\qquad
h_1(z)=f(z/3),\qquad
h_2(z)=f(2z/3).
\tag{348.27}
$$

省去的 weight-$2$ slash 常数均非零，不影响以下表示。

也可以直接核对这里的部分 Fricke 规范。层 $36p^2$ 的 $W_{p^2}$ 可取
$\left(\begin{smallmatrix}p^2A&B\\36p^2C&p^2D\end{smallmatrix}\right)$，
其中 $p^2AD-36BC=1$。以 $D_6$ 共轭后为
$\left(\begin{smallmatrix}p^2A&6B\\6p^2C&p^2D\end{smallmatrix}\right)$，
在模六水平上为 $\pm I$。它对应运输模六标记的 $p^2$ 同源，并在各个二旧向量上保持同一局部 $p$ 新向量符号。

三维空间 $V_f=\langle h_0,h_1,h_2\rangle$ 在模六有限群下稳定。可以直接由新旧理论与 CM 自扭曲确认这一点：有限水平群与所有 $\ell\equiv1\pmod6$ 的 Hecke 算子交换；若另一个新形式在这些素数与 $f$ 同迹，Chebotarev 给出其 Galois 表示限制到 $G_K$ 后为
$\psi_\theta\oplus\psi_\theta^c$。两个角色不同，故不可约的二维扩张必为
$\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\psi_\theta$。它与 $f$ 相同；其唯一可能的二次自扭曲正是 $\chi_{-3}$，也仍是 $f$。在层 $36p^2$ 的该 isotypic 空间因而准确是三维的二旧空间 (348.27)。

令 $T=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)$。在
$\Gamma_0(p^2)$ 的模六商中，$T^{3p^2}$ 只给模二换位，$T^{2p^2}$ 只给模三非平凡幺幂元。由 (348.19)，

$$
T^{2p^2}:
\quad h_0\mapsto\zeta h_0,\quad
h_1\mapsto\zeta^2h_1,\quad
h_2\mapsto\zeta h_2.
\tag{348.28}
$$

模二的全群为 $S_3$，其不变空间恰为
$\mathbb C h_1$：忘去模二结构后，由
$D_3\Gamma_0(9p^2)D_3^{-1}
=(\{\pm I\}\Gamma(3))\cap\Gamma_0(p^2)$，
只剩 $f$ 的一个新向量。

还可直接排除两个 sign 的可能性。由 $a_2=0$ 的 Hecke 递推，
$f$ 的偶数指标部分为 $-2f(4z)$，因此

$$
T^{3p^2}:
\quad h_0\mapsto-h_0-4h_2,\quad
h_1\mapsto h_1,\quad h_2\mapsto h_2.
\tag{348.29}
$$

该换位的迹是 $1$。三维且恰有一个平凡成分的 $S_3$ 表示只能是
$1\oplus\mathrm{Std}$ 或 $1\oplus\mathrm{sgn}^{\oplus2}$；
后者的换位迹是 $-1$。所以

$$
V_f\simeq1\oplus\mathrm{Std}
\quad\text{作为模二表示}.
\tag{348.30}
$$

模三作用与模二交换；Schur 引理使它在两个不可约成分上分别为一维角色，因而通过
$\mathrm{SL}_2(\mathbb F_3)/Q_8=C_3$。由 (348.28)，平凡模二成分的模三角色为 $\zeta^2$，标准模二成分的模三角色为 $\zeta$。

在几何 $H_6$ 的对角 $C_3$ 下，前者没有不变量；而
$\mathrm{Std}|_{C_3}$ 是两个非平凡角色之和，故后者恰有一个不变向量。因此每个 $f_\theta$ 在 $H_6$ 商上实际出现一次，并且出自
$\mathrm{Std}\otimes\mathrm{Std}$ 图式成分。

由 (348.24)，这个向量在 $p^2$ 处的 Fricke 符号为正。其在 $p$ 处导子指数为 $2$，故不会出现在 (348.25) 的 Borel 项：Borel 项只有 $p$ 导子指数至多 $1$ 的表示。于是该向量通过 (348.25) 给出 $J_{Z'_p}$ 的真实 CM 成分。整个论证是带模六交换作用的函子性 Chen 关系；不是从仅有素数层的同源直接推断混合层结果。

## 5. 甲板微分确定实际三次扭曲的方向

仍用 $T^{2p^2}$。在 (348.10) 的尖点，

$$
u(z)=c\,q^{-1/6}+\text{较高项},\qquad c\ne0.
\tag{348.31}
$$

它在模二为恒等、在模三为 $C_3$ 元素，因而正规化 $H_6$ 并给一个甲板变换。由首项及 $p^2\equiv1\pmod3$，

$$
u(z+2p^2)=\zeta^{-1}u(z);
\tag{348.32}
$$

即该矩阵给 $\delta_\zeta^{-1}$。§4 的实际 $H_6$ 不变向量位于标准模二成分，所以 (348.28) 表明

$$
(\delta_\zeta^{-1})^*\omega_\theta=\zeta\omega_\theta,
\qquad
\delta_\zeta^*\omega_\theta=\zeta^{-1}\omega_\theta.
\tag{348.33}
$$

这里作用于曲线微分的是 pullback；在 Jacobian 上使用与映射协变的除子 pushforward。后者在微分上的 pullback 正是 (348.33)，避免把 Picard 的逆作用混入扭曲计算。

把 $f_\theta$ 的 $K$-CM 作用规范为无穷型 $(1,0)$：$\lambda\in K$ 在该 holomorphic CM 型上的微分特征为 $\lambda$。由特征零中 endomorphism 在切空间上的忠实性，$\delta_\zeta$ 在这一 CM 成分上就是 $[\zeta^{-1}]$。

令 $\rho_{\rm can}$ 表示未扭曲 CM 成分的 Tate 表示。由 (348.13)，在通过 $\iota_*$ 识别的 Tate 空间上，

$$
\iota_*\rho_{\rm act}(\sigma)\iota_*^{-1}
=\delta_{\kappa_4(\sigma),*}\,\rho_{\rm can}(\sigma).
\tag{348.34}
$$

因此在所选 $K$-CM 特征上，实际表示是

$$
\psi_\theta\kappa_4^{-1},
\tag{348.35}
$$

而不是 $\psi_\theta\kappa_4$。对整个有理 CM isotypic 部分作上述扭曲并取其有理简单因子，得到由
$\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}
(\psi_\theta\kappa_4^{-1})$ 描述的成分。Hecke theta 对应及 Faltings 同源定理把它识别为 $g_\theta$ 的模 abelian variety。因此每个 $g_\theta$ 的有理 Galois orbit 因子确实是 $J_{Z_p}$ 的商。

这一取向来自实际曲线同构及微分特征，未用任何固定小素数的例子校准。

## 6. 全部有限导子及准确根号

先记录 $\kappa=\kappa_4$。其复共轭满足 $\kappa^c=\kappa^{-1}$，故在任意不分裂局部处，它在 $\mathbb Q_v^\times$ 上平凡：这些元素在共轭下不变，而角色同时满足 $\kappa^2=1$ 与 $\kappa^3=1$。

角色 $\kappa$ 只在 $2,3$ 处分歧，准确导子为

$$
\mathfrak f(\kappa)=(2)(s)^2.
\tag{348.36}
$$

一个直接验证是用同一 Galois 闭包中的纯三次域
$F=\mathbb Q(\sqrt[3]2)$。其整数环为
$\mathbb Z[\sqrt[3]2]$、判别式为 $-108$：在 $2$ 处用 Eisenstein 多项式 $X^3-2$，在 $3$ 处令 $Y=X+1$，得到 Eisenstein 多项式
$Y^3-3Y^2+3Y-3$；两处都由 uniformizer 生成局部整数环，其他素数没有判别式因子。三次置换表示除去平凡成分就是
$\operatorname{Ind}_{K}^{\mathbb Q}\kappa$。conductor–discriminant 及诱导导子公式于是分别给出
$2a_{K_2}(\kappa)=2$、
$1+a_{K_3}(\kappa)=3$，即 (348.36)。

在 $2$ 处，算术互反的 tame 公式给

$$
\kappa_2(\zeta)=\zeta^{-v_2(4)}=\zeta.
\tag{348.37}
$$

主元 $\zeta$ 的全局乘积公式，以及所有其他局部单位处的平凡性，给

$$
\kappa_3(\zeta)=\zeta^{-1}.
\tag{348.38}
$$

又因 $1+s=-2\zeta^2$，有

$$
\kappa_3(1+s)=\zeta,\qquad
\kappa_3(s)=1.
\tag{348.39}
$$

第二式由 $s^2=-3\in\mathbb Q_3^\times$ 和角色阶 $3$ 得到。在 $p$ 处 $\kappa_p$ 未分歧且在 uniformizer $p$ 上为一，故整个 $\kappa_p$ 平凡。

原角色 $\Psi_\theta$ 在 $3$ 处的单位化角色记为 $\nu$。它的导子指数为一，且

$$
\nu(-1)=-1,\qquad \nu(1+s\mathcal O_3)=1.
\tag{348.40}
$$

其无穷分量是 $z\mapsto z^{-1}|z|$，在 $s$ 上为 $-i$；在 $p$ 处 $s$ 的单位值为
$\theta(s)^{-1}=-1$。主元 $s$ 的乘积公式遂给

$$
\nu(s)=-i.
\tag{348.41}
$$

所以 $\xi=\nu\kappa_3^{-1}$ 的导子指数准确为二，并满足

$$
\xi\bigl(\varepsilon(1+ts)\bigr)
=\varepsilon\zeta^{-t}
\quad
(\varepsilon\in\{1,-1\},\ t\in\{0,1,2\}).
\tag{348.42}
$$

在 $2$ 处，原角色未分歧而 $\kappa_2$ 是非平凡 tame 三次角色，故实际导子指数为一；在 $p$ 处则仍为一。因此

$$
\mathfrak f(\Psi_\theta\kappa^{-1})
=(2)(s)^2(p),\qquad
N(g_\theta)=|D_K|\,
\mathrm N\mathfrak f(\Psi_\theta\kappa^{-1})
=108p^2.
\tag{348.43}
$$

$\kappa$ 在有理主理想上平凡，所以 nebentypus 仍为一。共轭理想给共轭角色值，因此全部 Fourier 系数均为实数。

为核根号，取 $\mathbb Q_q$ 上的标准加性角色
$\psi_q(x)=\exp(2\pi i\{x\}_q)$；在扩张中复合迹。若单位化角色 $\eta$ 的导子指数为 $a>0$、加性角色恰在
$\varpi^{-n_\psi}\mathcal O$ 上平凡，则所用 Gauss 公式为

$$
\epsilon(1/2,\eta,\psi)
=\eta(\varpi^{a+n_\psi})\,q^{-a/2}
\sum_{u\in(\mathcal O/\varpi^a)^\times}
\eta(u)^{-1}\psi(u/\varpi^{a+n_\psi}).
\tag{348.44}
$$

对二次诱导，再乘
$\lambda(K_v/\mathbb Q_v,\psi_v)$。在 $2,p$ 的未分歧二次扩张中该常数为一；在 $3$ 处为
$\epsilon(1/2,\chi_{-3,3},\psi_3)=i$，这是模 $3$ 的二次 Gauss 和。

**$p$ 处。** 由 (348.21)–(348.23)，实际角色没有变化，故
$\epsilon_p(g_\theta)=+1$。

**$2$ 处。** 原角色在 uniformizer $2$ 上的值为 $-1$，因为
$\Psi_\theta((2))=-2$；$\kappa_2(2)=1$。剩余域
$\mathbb F_4$ 中任一非平凡三次角色的 Gauss 和都是

$$
1-\zeta-\zeta^2=2.
\tag{348.45}
$$

式 (348.44) 因而给

$$
\epsilon_2(g_\theta)=-1.
\tag{348.46}
$$

**$3$ 处。** 扩张的 different 为 $(s)$，故 $n_\psi=1$。对原角色 $\nu$，取 $a=1$、$c=s^2$；Gauss 和为
$\zeta-\zeta^{-1}=i\sqrt3$，而 $\nu(s^2)=-1$，故
$\epsilon_K(\nu)=-i$，诱导后为 $+1$。

对实际角色 $\xi$，取 $a=2$、$c=s^3$。由 (348.41)，$\xi(s^3)=i$。又

$$
\operatorname{Tr}_{K_3/\mathbb Q_3}
\frac{\varepsilon(1+ts)}{s^3}
=-\frac{2\varepsilon t}{3},
\tag{348.47}
$$

所以其完整 Gauss 和为

$$
\sum_{\varepsilon=\pm1}\sum_{t=0}^2
\varepsilon\zeta^{t}\zeta^{\varepsilon t}
=-3.
\tag{348.48}
$$

因此

$$
\epsilon_K(\xi)=i\frac{-3}{3}=-i,\qquad
\epsilon_3(g_\theta)=i(-i)=+1.
\tag{348.49}
$$

若错误地取 $\Psi_\theta\kappa_4$，(348.48) 将是 $+3$，在 $3$ 处的诱导根号将为 $-1$。所以本处的方向决定结论，不能仅从某个三次扭曲的正根号代替 §5。

权二的无穷根号为 $-1$，其余有限处均未分歧。综合得

$$
w(g_\theta)=
(-1)_\infty(-1)_2(+1)_3(+1)_p=+1.
\tag{348.50}
$$

## 7. 固定角色族的精确中心值平均

这一节单独证明非零；正根号本身不保证中心值非零。

置

$$
c=\frac{2\pi}{\sqrt{108}}
=\frac{\pi}{3\sqrt3}.
\tag{348.51}
$$

权二、准确层 $108p^2$、根号正的 Mellin 函数方程给出精确的指数和

$$
L(g_\theta,1)
=2\sum_{n\ge1}\frac{a_n(g_\theta)}n
\exp(-cn/p).
\tag{348.52}
$$

可将 $2\pi\int_0^\infty g_\theta(iy)\,dy$ 在
$y=1/\sqrt{108p^2}$ 分开，再用 Fricke 函数方程把低区间变成高区间，直接得到 (348.52)。右侧绝对收敛；这不是省略误差项的近似函数方程。

以理想展开重写 (348.52)，对 $\Theta_p$ 取平均。设

$$
U=\langle[\zeta],[s]\rangle\subset T_p,\qquad |U|=6.
\tag{348.53}
$$

$\Theta_p$ 是 $U$ 上某个固定角色的全部延拓。因此角色正交性表明：理想
$\mathfrak a=(\beta)$ 的平均项除非
$[\beta\bmod p]\in U$ 否则为零。

任何 $\beta\in\mathcal O$ 都可写成

$$
\beta=\frac{A+Bs}{2},\qquad
A,B\in\mathbb Z,\quad A\equiv B\pmod2,\qquad
\mathrm N(\beta)=\frac{A^2+3B^2}{4}.
\tag{348.54}
$$

若 $[\beta]\in U$，可先乘一个单位 $\zeta^j$，使其模 $p$ 为有理方向或 $s$ 倍有理方向。

在第一种情形，$p\mid B$。若 $B\ne0$，则
$\mathrm N\mathfrak a\ge3p^2/4$；若 $B=0$，理想就是有理整数理想 $(n)$。
在第二种情形，$p\mid A$。若 $A\ne0$，则
$\mathrm N\mathfrak a\ge p^2/4$；若 $A=0$，则 $\beta$ 是整数倍 $s$，理想与 $3$ 不互素，已经由导子项排除。

所以所有存活而非有理整数理想的项都满足

$$
\mathrm N\mathfrak a\ge p^2/4.
\tag{348.55}
$$

对整数理想 $(n)$，$\kappa_4((n))=1$，且
$\Psi_\theta((n))=\chi_{-3}(n)n$。得到精确分解

$$
\frac1{h_p}\sum_{\theta\in\Theta_p}L(g_\theta,1)
=
2\sum_{\substack{n\ge1\\(n,6p)=1}}
\frac{\chi_{-3}(n)}n e^{-cn^2/p}
+R_p.
\tag{348.56}
$$

令 $a_K(m)$ 为范数 $m$ 的整数理想数。初等因子分解给

$$
a_K(m)=\sum_{d\mid m}\chi_{-3}(d)
\le d(m)\le2\sqrt m.
\tag{348.57}
$$

另一方面，每个 $\Psi_\theta(\mathfrak a)\kappa_4^{-1}(\mathfrak a)$
的绝对值为 $\sqrt{\mathrm N\mathfrak a}$。故

$$
\begin{aligned}
|R_p|
&\le4\sum_{m\ge\lceil p^2/4\rceil}e^{-cm/p}\\
&\le
\frac{4e^{-cp/4}}{1-e^{-c/p}}\\
&<
4\left(1+\frac{5p}{3}\right)e^{-3p/20}.
\end{aligned}
\tag{348.58}
$$

最后一步只用 $c>3/5$ 与
$(1-e^{-x})^{-1}\le1+x^{-1}$。这里的常数与 $p$、$\theta$、实际整数参数及其导子都无关。

主项也有统一的严格正下界。对任意 $x>0$，

$$
S(x)=\sum_{\substack{n\ge1\\(n,6)=1}}
\frac{\chi_{-3}(n)}n e^{-xn^2}
=
\sum_{k\ge0}
\left(
\frac{e^{-x(6k+1)^2}}{6k+1}
-
\frac{e^{-x(6k+5)^2}}{6k+5}
\right)>0,
\tag{348.59}
$$

因为 $e^{-xt^2}/t$ 对 $t>0$ 严格递减。由于
$\chi_{-3}(p)=-1$，删除 $p$ 的倍数反而增加主和：

$$
\sum_{\substack{n\ge1\\(n,6p)=1}}
\frac{\chi_{-3}(n)}n e^{-cn^2/p}
=S(c/p)+\frac1pS(cp).
\tag{348.60}
$$

保留 (348.59) 的第一对并用 $c<61/100$、$p\ge41$，有

$$
\begin{aligned}
2\sum_{\substack{n\ge1\\(n,6p)=1}}
\frac{\chi_{-3}(n)}n e^{-cn^2/p}
&>
2\left(e^{-c/p}-\frac15\right)\\
&>
2\left(1-\frac{61}{4100}-\frac15\right)
=\frac{3219}{2050}.
\end{aligned}
\tag{348.61}
$$

而 (348.58) 的最后一个函数在 $p\ge41$ 单调下降，故

$$
|R_p|
<
\frac{832}{3}e^{-123/20}
<
\frac{52}{75}.
\tag{348.62}
$$

最后的不等式可全用有理算术核准：
$e^3>\sum_{j=0}^8 3^j/j!>20$，故 $e^6>400$，
进而 $e^{123/20}>400$。
把 (348.61)–(348.62) 代入 (348.56)，即得

$$
\frac1{h_p}\sum_{\theta\in\Theta_p}L(g_\theta,1)
>
\frac{3219}{2050}-\frac{52}{75}
=\frac{5393}{6150}.
\tag{348.63}
$$

这同时证明 (348.7) 与至少一个 $g_\theta$ 的中心值为正。

## 8. 从非零中心值到实际有理秩零商

取 (348.63) 中一个 $L(g_\theta,1)\ne0$ 的形式，令 $A_{g_\theta}$ 为其
$\mathbb Q$ 模 abelian variety。§§4–5 已证明它是 $J_{Z_p}$ 的同源因子；Poincaré 完全可约性将有理同源范畴的商乘以一个非零整数，给出实际满射同态

$$
J_{Z_p}\twoheadrightarrow A_{g_\theta}.
\tag{348.64}
$$

应用 Kato（2004）Theorem 14.2(2)，取权 $k=2$、$r=1$、基域为
$\mathbb Q$、平凡扭曲。该定理包括 CM 形式；其 CM 证明在同一论文 §15 完成。它给任意有限系数域位 $\lambda$ 的相应 Selmer 群有限。
平凡 nebentypus、权二时，Kato 所记 $V(g_\theta)(1)$ 由极化识别为 $A_{g_\theta}$ 的相应 Tate 分量。

也可不另引所有复嵌入下非消失的代数性来得到 Mordell–Weil 结论。
令 $F_g$ 为 $g_\theta$ 的 Hecke 系数域。$A_{g_\theta}(\mathbb Q)\otimes\mathbb Q$
是有限维 $F_g$ 向量空间。若其维数正，则张量任何
$F_{g,\lambda}$ 后仍非零；Kummer 映射把它注入对应的有理 Selmer 空间，与 Kato 的有限性矛盾。因此

$$
\operatorname{rank}A_{g_\theta}(\mathbb Q)=0.
\tag{348.65}
$$

Mordell–Weil 有限生成性即给有限群 (348.2)。这里没有删除
$\Sha$ 项，也没有把根号正等同于算术秩零。

在实际分支中，$a\ne0,1$ 的非 CM 整数参数给出
$P\in Z_p(\mathbb Q)$，从而

$$
[P-c_1]\longmapsto A_{g_\theta}(\mathbb Q)_{\mathrm{tors}}.
\tag{348.66}
$$

这是已经得到的全局限制。要由此排除 $P$，仍需控制所选同态在相应整数模型上的延拓、特殊纤维分支、微分整性及首项，并处理可能的有理扭点像。仅有 $v_p(a-1)$ 的既有高精度或 (348.65)，都不能替代这些条件。

## 9. 使用的原文与可复核范围

- J. Brau–N. Jones, *Elliptic curves with 2-torsion contained in the 3-torsion field*, Proc. Amer. Math. Soc. 144 (2016), 925–936，DOI 10.1090/proc/12786。作者稿式 (7)–(10)、Theorem 1.4、其证明，PDF pp.3–5，给出 (348.8)–(348.10) 的准确群与 $j$ 映射。[作者 PDF](https://homepages.math.uic.edu/~ncjones/2tin3t.pdf)；[arXiv:1406.1262](https://arxiv.org/abs/1406.1262)。
- B. de Smit–B. Edixhoven, *Sur un résultat d'Imin Chen*, Math. Res. Lett. 7 (2000), 147–154，Theorem 2(2)，作者稿 pp.2–3。这里用其任意对象的函子性恒等式，保留全部模六作用。[作者 PDF](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。
- M. Schütt, *CM newforms with rational coefficients*, Ramanujan J. 19 (2009), 187–205，§1，Theorem 1.4（Hecke–Shimura），作者稿 p.3。所用是对任意代数 Hecke 角色成立的 theta 构造、准确层及 nebentypus 公式；不使用该文后来关于有理系数分类的特殊假设或 ERH 条件。[作者稿](https://arxiv.org/pdf/math/0511228)。
- R. Schmidt, *Some remarks on local newforms for GL(2)*, J. Ramanujan Math. Soc. 17 (2002), 115–147，§1.1 的式 (5)、§2.3 Theorem 2.3.2、§3.2 Theorem 3.2.2，作者稿 pp.3、17、26–27。用于 Gauss 公式、诱导导子与局部新向量符号的规范；本稿逐项计算实际局部角色，没有从未扭曲符号猜测扭曲符号。[作者 PDF](https://www.math.uni-sb.de/ag/schulze/rschmidt/papers/gl2.pdf)。
- K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*, Astérisque 295 (2004), 117–290，Theorem 14.2(2)、Corollary 14.3，printed pp.235–236；§15 明确完成 CM 情形。这里只用中心值非零推出相应 Selmer 群有限、进而 Mordell–Weil 秩零。[Numdam 原刊](https://www.numdam.org/item/AST_2004__295__117_0/)；[PDF](https://www.numdam.org/article/AST_2004__295__117_0.pdf)。

其他使用的是标准新旧形式理论、CM 形式的诱导 Galois 表示、Chebotarev、Faltings 同源定理及有限维表示的完全可约性。新的具体内容为实际 $\sqrt[3]4$ 取向、混合层上该 CM 成分的出现、全部局部根号，以及 (348.55) 所产生的统一指数误差。本文为纯证明，没有以有限数值扫描代替 (348.63) 的全素数估计。

