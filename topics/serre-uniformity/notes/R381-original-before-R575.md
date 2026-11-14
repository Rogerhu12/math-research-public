# R381：实际六层的非自扭曲配对与中心值障碍

**状态：已证明。** 本篇确定 R348 实际六层新增部分中、没有 $\chi_{-3}$ 自扭曲的全部表示，以及它们的准确局部导子与根号。这些表示的中心值全部为零。因此，利用普通中心值非零来选取商时，整个实际六层都只能使用 R348 的 $K=\mathbb Q(\sqrt{-3})$ CM 部分。结合 R376，对 R376 指定的源半稳定模型到目标好约化模型的映射，这类商全部收缩实际 $a=1$ 分量。这个结论不计算 R378 的真实 Taylor 首项，不排除归一化之后的局部解析方法，也不把负根号当作未经证明的算术正秩结论。

## 1. 结论与记号

设 $p\ge41$、$p\equiv2\pmod3$。沿用 R330、R348 的实际曲线

$$
X=X_{\mathrm{ns}}^+(p),\qquad
Y=\operatorname{Norm}\bigl(X\times_j\{j=1728-3t^2\}\bigr),
\qquad
Z=\operatorname{Norm}\bigl(X\times_j\{j=6912a^3(1-a^3)\}\bigr).
\tag{381.1}
$$

映射 $Z\to Y$ 由 $t=24(2a^3-1)$ 给出。记

$$
K=\mathbb Q(s),\quad s^2=-3,\quad
\chi=\chi_{-3},\quad
\zeta=(-1+s)/2,\quad
\kappa=\kappa_4,\quad
\rho=\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\kappa .
\tag{381.2}
$$

这里 $\kappa(\sigma)=\sigma(\sqrt[3]4)/\sqrt[3]4$，在 $G_K$ 上为非平凡三次角色；$\rho$ 是三次域 $\mathbb Q(\sqrt[3]2)$ 的置换表示去掉平凡分量。它是二维正交表示，行列式为 $\chi$。取实际 Prym

$$
P=\ker\bigl(J_Z\longrightarrow J_Y\bigr)^0.
\tag{381.3}
$$

下述分解是在有理同源范畴中，或等价地在任意辅助 $\ell$ 的半单 Tate 空间张量 $\overline{\mathbb Q}_\ell$ 后进行；没有对整同源分母作任何断言。

除 R348 的 $K$-CM 因子之外，$P$ 的每个绝对不可约 Tate 成分都是

$$
W_f=V_f\otimes\rho
=\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}
      \bigl(V_f|_{G_K}\otimes\kappa\bigr),
\qquad f\ne f\otimes\chi.
\tag{381.4}
$$

这里 $f$ 是权 $2$、平凡 nebentypus 的归一化新形式，准确层为

$$
N_f=9p^2\quad\text{或}\quad18p^2.
\tag{381.5}
$$

$f$ 与 $f\otimes\chi$ 给同一个块，应按无序对计数；若两者是系数域共轭，也仍按这个配对处理。所需局部类型为：

| 处 | $f$ 的局部类型 | $W_f$ 的 Artin 导子指数 | $W_f$ 的单位化局部根号 |
|---|---|---:|---:|
| $2$ | 未分歧主系列，或未分歧角色乘 Steinberg | $4$ | $+1$ |
| $3$ | 平凡中心角色、导子指数 $2$ 的唯一 tame supercuspidal 类型 | $6$ | $-1$ |
| $p$ | 导子指数 $2$，$W_{p^2}=+1$ | $4$ | $+1$ |
| $\infty$ | 两份权二离散系列参数 | — | $+1$ |

因此

$$
N(W_f)=2^4\,3^6\,p^4,\qquad
w(W_f)=-1,\qquad
L(W_f,1)=0.
\tag{381.6}
$$

$L$ 采用权一动机的算术规范，中心为 $1$；表中的局部计算采用单位化参数、中心为 $1/2$。

若一个 $\mathbb Q$ 上的非零同源商 $B$ 满足

$$
J_Z\twoheadrightarrow B,\qquad L(B,1)\ne0,
\tag{381.7}
$$

则 $B$ 在 $\mathbb Q$ 同源范畴内是 R348 所列 $A_{g_\theta}$ 的乘积的子商。特别地，在 R376 指定的源半稳定模型到目标好约化模型的映射中，它收缩整条实际 $a=1$ 分量；这两个指定模型之间的整形式浸入不能由换一个普通非零中心值商恢复。

本篇的“非自扭曲”始终指 $f\ne f\otimes\chi_{-3}$。它包含通常的非 CM 形式，也允许 $f$ 具有别的 CM 域；后者不构成遗漏的例外。没有使用 BSD 或正秩的奇偶性猜想。

## 2. 新增四维几何表示

先用 R348 的未扭曲模曲线 $Z'$：

$$
j=27648u^3(1-4u^3),\qquad
a=\alpha u,\quad \alpha^3=4.
\tag{381.8}
$$

其模六群是 Brau–Jones 图式
$H_6=\{(\vartheta(g),g):g\in\mathrm{GL}_2(\mathbb F_3)\}$，
其中 $\ker\vartheta=Q_8$。在几何分量上，去掉已经平凡作用的中心后，模二、模三群分别为 $S_3$、$A_4$。将模三的正规子群 $Q_8/\{\pm1\}\simeq V_4$ 商掉后，得到

$$
S_3\times C_3,\qquad
H_{\mathrm{geom}}=\{(c,c):c\in C_3\}.
\tag{381.9}
$$

令 $\eta$ 是 $C_3$ 的一个非平凡复角色，$\mathrm{Std}$ 是 $S_3$ 的二维标准表示。Frobenius reciprocity 给出准确的六维置换表示分解

$$
\mathbb C[(S_3\times C_3)/H_{\mathrm{geom}}]
=
(1\boxtimes1)\oplus(\mathrm{sgn}\boxtimes1)
\oplus(\mathrm{Std}\boxtimes\eta)
\oplus(\mathrm{Std}\boxtimes\eta^{-1}).
\tag{381.10}
$$

证明只需将每个 $S_3$ 不可约表示限制到 $C_3$：
$1$、$\mathrm{sgn}$ 都限制为平凡角色，而
$\mathrm{Std}|_{C_3}=\eta\oplus\eta^{-1}$。各个出现的重数为一，维数为 $1+1+2+2=6$，没有其他成分。

前两项正是二层 $Y$。后三次覆盖的非平凡部分因而准确来自最后两项。甲板作用

$$
\delta_\zeta:u\longmapsto\zeta u
\tag{381.11}
$$

在 $K$ 上定义；$G_{\mathbb Q}\setminus G_K$ 将它共轭为 $\delta_\zeta^{-1}$。其两个非平凡特征空间正是 (381.10) 的两个标准成分。实际三次扭曲不改变 $\delta$-不变的二层，故这里的 $Y$ 是 (381.1) 的同一个实际二层。

## 3. 所有可能的新形式及其局部类型

保留完整模六标记，在模 $p$ 作用上应用 de Smit–Edixhoven 的函子性 Chen 关系。R348 §4 已核准：将两个互补 $p$ 子群换成 $p^2$ 循环同源，再交换两子群并沿对偶同源搬运标记，模六标记上的复合为

$$
[p]=-I_6\in H_6
\quad(p\equiv5\pmod6).
\tag{381.12}
$$

所以该交换给通常的 $W_{p^2}$，没有额外的模六符号。这个函子性关系保留 $\delta$ 及 (381.10) 的各个投影。

在分裂侧，以 $D_6=\operatorname{diag}(6,1)$ 共轭，有

$$
D_6\Gamma_0(36p^2)D_6^{-1}
=(\{\pm I\}\Gamma(6))\cap\Gamma_0(p^2).
\tag{381.13}
$$

因此通常的新旧形式分解覆盖全部几何成分；原始新形式的层整除 $36p^2$，nebentypus 为平凡。下面的有限群条件进一步给出准确层，不能只从 R348 的 CM 例子外推。

### 3.1. 模二标准类型

在 $2$ 处，非平凡三次部分要求 $\mathrm{Std}$。未分歧主系列的主同余不变空间为

$$
\mathbb C[\mathbb P^1(\mathbb F_2)]
=1\oplus\mathrm{Std},
\tag{381.14}
$$

而未分歧角色乘 Steinberg 给 $\mathrm{Std}$。中心角色平凡且导子指数至多二的其余可能类型只有 tame supercuspidal；其有限 $\mathrm{GL}_2(\mathbb F_2)=S_3$ 类型为 $\mathrm{sgn}$，没有标准成分。

这里没有遗漏分歧主系列或分歧 Steinberg：$\mathbb F_2^\times$ 平凡，非平凡单位角色的导子指数至少二，相关导子至少四，超出 (381.13)。supercuspidal 若导子为二，其惯性不变量为零且 Swan 导子为零，所以正是上述 tame 情形。故

$$
c_2(f):=a(\operatorname{WD}_2(f))\in\{0,1\}.
\tag{381.15}
$$

### 3.2. 模三非平凡一维类型

模三必须有非平凡的
$\mathrm{SL}_2(\mathbb F_3)/Q_8=C_3$ 角色。两条共轭直线合在一起，作为 $\mathrm{GL}_2(\mathbb F_3)$ 表示，正是

$$
\tau_3=\mathrm{Std}\circ\vartheta .
\tag{381.16}
$$

这是有限 cuspidal 表示：上三角幺幂群的非恒等元在 $C_3$ 中非平凡，故 $\tau_3$ 在该群下没有不变量。它还是平凡中心角色的唯一二维有限 cuspidal 类型；通常的参数是 $\mathbb F_9^\times$ 上阶四的两个共轭角色。

可直接排除其余导子至多二的局部类型。未分歧主系列及其剩余二次行列式扭曲，限制到 $\mathrm{SL}_2(\mathbb F_3)$ 后是 $\mathbb P^1(\mathbb F_3)$ 上的四维置换表示；其分解为 $1$ 加三维 Steinberg。$Q_8/\{\pm1\}=V_4$ 在这四点上传递，所以 $Q_8$ 不变空间只有平凡直线，没有 $\eta^{\pm1}$。Steinberg 及其二次扭曲同样没有所需直线。wild supercuspidal 的导子大于二。故 $f$ 在 $3$ 处准确为 (381.16) 对应的 tame supercuspidal，导子指数二。

其单位化 Weil 参数可以写成

$$
\operatorname{WD}_3(f)
=\operatorname{Ind}_{W_{K_3}}^{W_{\mathbb Q_3}}\nu,
\quad
a_{K_3}(\nu)=1,\quad
\nu(-1)=-1,\quad
\nu(1+s\mathcal O_{K_3})=1,\quad
\nu(s)=\varepsilon i,\quad\varepsilon=\pm1.
\tag{381.17}
$$

确实，$\nu|_{\mathbb Q_3^\times}=\chi_3$ 使诱导参数的行列式平凡，且
$\nu(s)^2=\nu(-3)=-1$。这个诱导不可约，因为 $\nu^c(s)=-\nu(s)$。它是 tame、导子二，并给上述唯一有限 cuspidal 类型；两个 $\varepsilon$ 由共轭互换，诱导相同。因此 (381.17) 不附加不必要的全局符号选择。

它有局部自扭曲

$$
\operatorname{WD}_3(f)\otimes\chi_3
\simeq\operatorname{WD}_3(f).
\tag{381.18}
$$

### 3.3. 模 $p$ 的新部分

在 $p$ 处，Steinberg 的有限模型是
$\mathbb P^1(\mathbb F_p)$ 上的置换表示去掉平凡分量。非分裂 Cartan 在这些点上传递，故 Steinberg 没有 Cartan 不变向量。未分歧主系列的非分裂正规化子不变直线来自整个极大紧子群不变直线；它只给忘去 $p$ 水平的基曲线，而 $X'(6)$ 的亏格为零。

等价地，在 Chen 关系中，导子一的项由 Borel 项消去，导子零项由 $J_{X'(6)}=0$ 消去。余下的全部项因而是 $p$ 新、导子指数二，且 $W_{p^2}=+1$。结合前两小节，得到准确层 (381.5)。

二次扭曲 $f\otimes\chi$ 在 $3$ 处由 (381.18) 保持类型，在 $2,p$ 处只是未分歧二次扭曲；在 $p$ 处导子二保证 Fricke 符号不变。故它仍在同一列表中。

## 4. 同一算术配对及实际三次下降

先设 $f\ne f\otimes\chi$。新形式的特征零二维 Tate 表示 $V_f$ 绝对不可约，并且

$$
V_f|_{G_K}\text{ 绝对不可约}.
\tag{381.19}
$$

否则 Clifford 理论使 $V_f$ 从 $K$ 的一个角色诱导，从而
$V_f\simeq V_f\otimes\chi$，与假设矛盾。

完整模六空间上的有限群作用与所有
$\ell\equiv1\pmod6$、$\ell\nmid6p$ 的 Hecke 算子交换。在这些素数上，新形式及其二次扭曲有相同特征值。反过来，Chebotarev 与半单性说明，相同的这组特征值确定同一个 $G_K$ 限制；由 (381.19) 与 Clifford 理论，其二维 $G_{\mathbb Q}$ 扩张恰为

$$
V_f,\quad V_f\otimes\chi.
\tag{381.20}
$$

这里用的是完整 Eichler–Shimura 关系：在这些素数上，模六标记的行列式为一，通常的新形式 Hecke 算子与曲线上的算术 Hecke 对应一致，Frobenius 满足 $F_\ell^2-T_\ell F_\ell+\ell=0$。因此下面的二重空间上整个 Euler 多项式为 $(1-a_\ell(f)T+\ell T^2)^2$，并非只知道某个迹和。$K$ 中位于有理分裂素数之上的两条 Frobenius 都满足这个关系，而这些一次素理想在 Chebotarev 中足够稠密。没有从一个有限的迹窗口推断 (381.20)。

局部新旧维数也给出准确的重数。$2$ 处未分歧时，旧空间为 $1\oplus\mathrm{Std}$，标准成分出现一次；$2$ 处 Steinberg 时，旧空间就是一份 $\mathrm{Std}$。$3$ 处两个非平凡特征 $\eta,\eta^{-1}$ 各出现一次。每个
$\mathrm{Std}\boxtimes\eta^{\pm1}$ 在对角 $C_3$ 下恰有一维不变量。因此未扭曲 Prym 中这个配对的 Tate 块 $U_f$ 为

$$
U_f|_{G_K}
\simeq V_f|_{G_K}\oplus V_f|_{G_K},
\qquad
U_f\simeq V_f\oplus(V_f\otimes\chi).
\tag{381.21}
$$

还必须保留 $\delta$。它在 (381.21) 的 $G_K$ 二重空间上有 $\zeta,\zeta^{-1}$ 两个特征空间，各是一份 $V_f|_{G_K}$；$G_{\mathbb Q}\setminus G_K$ 互换它们。故带这个作用的准确描述是

$$
U_f\simeq\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}(V_f|_{G_K}),
\quad
\delta\text{ 在两个诱导分量上的特征为 }\zeta,\zeta^{-1}.
\tag{381.22}
$$

在 (381.22) 中不存在一个未说明的固定三次 Artin 扭曲：若有，它会改变分裂素数上的整个特征多项式，违反前面的 Hecke 与 Chebotarev 识别。

R348 已逐式固定实际曲线同构及 cocycle：

$$
\iota:Z\longrightarrow Z',\quad u=a/\alpha,
\qquad
\sigma(\iota)\iota^{-1}
=\delta_{\kappa(\sigma)^{-1}}.
\tag{381.23}
$$

对协变 Jacobian Tate 空间，通过 $\iota_*$ 运输后的实际 Galois 作用是
$\delta_{\kappa(\sigma),*}$ 乘原作用。因此 (381.22) 的两个 $G_K$ 分量分别扭以 $\kappa,\kappa^{-1}$，并仍被外陪集互换。这准确给出 (381.4)。

非自扭曲情形无需任选一个有利的三次方向，因为

$$
\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}
 (V_f|_{G_K}\otimes\kappa)
\simeq
\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}
 (V_f|_{G_K}\otimes\kappa^{-1})
\simeq V_f\otimes\rho .
\tag{381.24}
$$

该四维表示绝对不可约。若诱导可约，则两个 $G_K$ 分量同构，进而
$V_f|_{G_K}\simeq V_f|_{G_K}\otimes\kappa^2$。取行列式会给 $\kappa^4=1$，与 $\kappa$ 的阶为三矛盾。这也说明本块不能再拆出一个遗漏的二维正根号因子。

## 5. 四个局部计算

以下全部用单位化 Weil–Deligne 参数。取标准 $\mathbb Q_q$ 加性角色，其导子为 $\mathbb Z_q$；在扩张上复合迹。R348 §6 已证明同一个实际 $\kappa$ 满足

$$
\mathfrak f_K(\kappa)=(2)(s)^2,\qquad
\kappa_p=1,\qquad
\kappa_2(\zeta)=\zeta,\quad\kappa_2(2)=1,
\qquad
\kappa_3(s)=1,\quad\kappa_3(1+s)=\zeta.
\tag{381.25}
$$

### 5.1. $p$ 处

$p$ 在 $K$ 中未分歧且惰性，又 $\kappa_p=1$，故

$$
\rho_p=1\oplus\chi_p,\qquad
\chi_p(p)=-1.
\tag{381.26}
$$

若 $\pi_p=\operatorname{WD}_p(f)$，则 $a(\pi_p)=2$、中心角色平凡。未分歧扭曲公式给

$$
a(\pi_p\otimes\rho_p)=2+2=4,
\qquad
\epsilon_p(W_f)
=\epsilon_p(\pi_p)^2\,\chi_p(p)^{\,2}
=+1.
\tag{381.27}
$$

这里只用中心角色平凡所给的 $\epsilon_p(\pi_p)\in\{\pm1\}$；没有限制 $\pi_p$ 必须是某一种 supercuspidal 类型。

### 5.2. $2$ 处：包括 Steinberg

$K_2/\mathbb Q_2$ 是未分歧二次扩张，$\rho_2$ 是从非平凡 tame 三次角色诱导的二维表示。其惯性不变量为零、导子为二。由 (381.25) 及 $\mathbb F_4$ 的完整 Gauss 和，

$$
G(\kappa_2^{\pm1})=1-\zeta-\zeta^2=2,
\qquad
\epsilon_2(\rho_2)=1.
\tag{381.28}
$$

若 $\pi_2$ 未分歧，写其两个未分歧参数为 $\mu_1,\mu_2$，其中 $\mu_1\mu_2=1$。则

$$
a(\pi_2\otimes\rho_2)=2+2=4,\qquad
\epsilon_2(W_f)
=\epsilon_2(\rho_2)^2(\mu_1\mu_2)(2)^{\,2}
=1.
\tag{381.29}
$$

若 $\pi_2=\mu\otimes\mathrm{Sp}_2$，其中 $\mu$ 未分歧且 $\mu^2=1$，其底层 Weil 表示为
$\mu|\cdot|^{1/2}\oplus\mu|\cdot|^{-1/2}$。张量 $\rho_2$ 后没有惯性不变量，所以 nilpotent monodromy 的额外导子为零、epsilon 修正为一；特别地没有额外 Steinberg 负号。因此

$$
\begin{aligned}
a(\mu\rho_2\otimes\mathrm{Sp}_2)&=4,\\
\epsilon_2(W_f)
&=\epsilon(1/2,\mu\rho_2|\cdot|^{1/2})
  \epsilon(1/2,\mu\rho_2|\cdot|^{-1/2})\\
&=\epsilon_2(\rho_2)^2\,\mu(2)^4=1.
\end{aligned}
\tag{381.30}
$$

两个绝对值因子的正实数贡献相消。式 (381.30) 是不能省略的导子一分支。

### 5.3. $3$ 处的两个 Gauss 和

由 (381.17)，并利用 $\kappa^c=\kappa^{-1}$，有

$$
\operatorname{WD}_3(f)\otimes\rho_3
=
\operatorname{Ind}_{K_3}^{\mathbb Q_3}(\nu\kappa_3)
\oplus
\operatorname{Ind}_{K_3}^{\mathbb Q_3}(\nu\kappa_3^{-1}).
\tag{381.31}
$$

两个角色都准确有 $K_3$ 导子二，诱导后导子均为
$1+2=3$，故总导子为六。

令 $\xi_\pm=\nu\kappa_3^{\pm1}$。
$K_3/\mathbb Q_3$ 的 different 为 $(s)$，所以在 Gauss 公式中
$a=2$、$n_\psi=1$、$c=s^3$。取单位代表
$\epsilon(1+ts)$，其中 $\epsilon=\pm1$、$t=0,1,2$，有

$$
\xi_\pm\bigl(\epsilon(1+ts)\bigr)
=\epsilon\zeta^{\pm t},\qquad
\psi_3\!\left(\operatorname{Tr}
       \frac{\epsilon(1+ts)}{s^3}\right)
=\zeta^{\epsilon t}.
\tag{381.32}
$$

因此两个完整 Gauss 和分别为

$$
\begin{aligned}
G_+&=\sum_{\epsilon=\pm1}\sum_{t=0}^2
       \epsilon\zeta^{-t}\zeta^{\epsilon t}=3,\\
G_-&=\sum_{\epsilon=\pm1}\sum_{t=0}^2
       \epsilon\zeta^{t}\zeta^{\epsilon t}=-3.
\end{aligned}
\tag{381.33}
$$

诱导常数 $\lambda(K_3/\mathbb Q_3)=i$，且
$\xi_\pm(s^3)=\nu(s)^3$。不必选定 (381.17) 的 $\varepsilon$，直接相乘：

$$
\begin{aligned}
\epsilon_3(W_f)
&=\left(i\,\nu(s)^3\,\frac{G_+}{3}\right)
  \left(i\,\nu(s)^3\,\frac{G_-}{3}\right)\\
&=i^2\,\nu(s)^6\,\frac{G_+G_-}{9}\\
&=(-1)(-1)(-1)=-1.
\end{aligned}
\tag{381.34}
$$

R348 的单个 CM 因子只保留其中一个方向；本处真实非自扭曲块同时保留两个方向。这是两篇根号不同的原因，不存在矛盾。

### 5.4. 无穷与其余处

在实处，$\rho_\infty=1\oplus\mathrm{sgn}$，权二离散系列参数与其 sign 扭曲同构。因此

$$
\epsilon_\infty(W_f)=(-1)^2=1.
\tag{381.35}
$$

其余有限处都未分歧。由 (381.27)、(381.29)–(381.30)、(381.34)–(381.35)，得到 (381.6) 的导子及根号。

## 6. 解析延拓、真正的中心值零与不可约范围

不能只写一个形式根号而忽略相应 $L$ 函数。这里有准确恒等式

$$
L(W_f,s)=L_K\bigl(\operatorname{BC}_K(f)\otimes\kappa,s\bigr).
\tag{381.36}
$$

这是诱导相容的逐处 Euler 因子恒等式，包括 $2,3,p$ 的完整坏因子。Langlands 的二次基变换定理给出 $\operatorname{BC}_K(f)$；它在 $f\ne f\otimes\chi$ 时为 cuspidal。后一条件也可从基变换定理的纤维描述看出：若基变换为两个 Hecke 角色之和，则非平凡共轭必须互换这两个角色，原来的 cuspidal 表示便是从 $K$ 诱导的二次自扭曲表示。

有限阶扭曲 $\kappa$ 保持 cuspidality。Jacquet–Langlands Theorem 11.1 因而给右侧完整 $L$ 函数的整延拓与函数方程。又因
$\operatorname{BC}_K(f)^c=\operatorname{BC}_K(f)$、
$\kappa^c=\kappa^{-1}$ 以及 $f$ 的中心角色平凡，对偶在 $K$ 共轭后回到同一表示。因此在算术规范下

$$
\Lambda(W_f,s)=-\Lambda(W_f,2-s).
\tag{381.37}
$$

其无穷因子在 $s=1$ 有限且非零，故确实
$L(W_f,1)=0$。这是同一个实际四维表示的中心值零；不是把 $f$ 本身的中心值与三次 Artin 扭曲的中心值混淆。

没有使用“负根号推出 Mordell–Weil 正秩”。特别地，本结论不排除某个尚未由中心值证明的算术秩零商，也不处理这些块的导数或 Selmer 类。

## 7. 自扭曲例外恰为 R348，而非另一族未识别 CM 商

现在设 $f=f\otimes\chi$。它从 $K$ 的一个无穷型 $(1,0)$ Hecke 角色 $\Psi$ 诱导。$K$-CM 形式在 $2$ 处不能是 Steinberg，因为其 Weil–Deligne 参数的 monodromy 为零；所以这里必须是 (381.5) 的层 $9p^2$。

$3$ 与 $p$ 处的导子公式给

$$
\mathfrak f_K(\Psi)=(s)(p).
\tag{381.38}
$$

$K$ 类数一。取所选 holomorphic CM 型，$\Psi$ 必可写成

$$
\Psi((\beta))
=\beta\,\epsilon_3(\beta)\,\theta(\beta\bmod p),
\qquad
\theta:
(\mathcal O_K/p)^\times/\mathbb F_p^\times\longrightarrow\mathbb C^\times.
\tag{381.39}
$$

单位相容迫 $\theta(\zeta)=\zeta^{-1}$；平凡 nebentypus 迫 $\theta$ 在 $\mathbb F_p^\times$ 上平凡。R348 的 $p$ 处完整 Gauss 计算给
$\epsilon_p(f)=-\theta(s)$。本处 $W_{p^2}=+1$，于是

$$
\theta(\zeta)=\zeta^{-1},\qquad
\theta(s)=-1.
\tag{381.40}
$$

所以 $\theta$ 准确属于 R348 的 $\Theta_p$，没有额外的未分歧类群角色，也没有额外的 $2$ 导子分支。

在自扭曲情形，$V_f|_{G_K}$ 是两个不同角色的和，而不是 (381.19) 的不可约二维表示。几何 $H_6$ 不变量只给 R348 §4 的一份 CM 因子。R348 §5 已由实际尖点上的甲板微分固定其取向，(381.23) 的下降因此给

$$
g_\theta=f_{\Psi_\theta\kappa^{-1}},
\tag{381.41}
$$

不是两种三次扭曲的直和。其准确层与根号分别为 $108p^2$ 和 $+1$，并且 R348 已另外证明该族中至少一个中心值非零。本篇没有以正根号替代那个非消失证明。

## 8. 对商选择及小 CM 圆盘的后果

由 (381.10)，$J_Z$ 在有理同源范畴内是 $J_Y$ 与 $P$ 的直和。R330 已证明实际二层 $J_Y$ 的相应新形式中心值全为零；这是已包含 $\chi_{-3}$ 扭曲的实际二层，不能重新使用未扭曲二层的符号。第 4–6 节证明 $P$ 的全部非自扭曲块中心值为零，第 7 节准确列出剩余自扭曲块。因此 (381.7) 蕴含 $B$ 是 (381.41) 的 CM 因子的子商。

表示的绝对不可约性保证不能从一个负号四维块中再取出正中心值的更小因子。系数域共轭也不会帮助：每个共轭具有同样的局部类型与负根号，完整中心值的乘积仍为零，没有极点可以消去这些零点。

于是 R376 对所有这样的实际商同时适用：对 R376 指定的源半稳定模型到目标好约化模型的映射，逐点固定实际 $a=1$ 分量的源惯性 $\mu_3$ 在目标上只有零维固定部分，故以 $c_1$ 为基点的商映射在整条该分量上为零。这一现象不是 R348 某个特定同源投影选得不好的结果。

R378 的实际小盘仍是

$$
w=(a-1)/p^3,\qquad
v_p(w)\ge1\ \text{或}\ \ge2
\tag{381.42}
$$

以及从同一商产生的整函数 $G_i(w)$。本篇没有证明其首个非零系数在除去共同赋值后为单位，也没有验证 R378 的有限首项支配证书。这个真实 CM Taylor 问题继续开放；整数圆盘的进一步归一化不被分量收缩所禁止。

## 9. 原文输入与复核位置

1. **混合层的函子性 Chen 关系。** B. de Smit–B. Edixhoven, *Sur un résultat d'Imin Chen*, Math. Res. Lett. 7 (2000), 147–154，Theorem 2(2)，作者 PDF pp.2–3。其任意带群作用对象的恒等式允许保留模六与甲板作用；标记交换的准确实现使用 R348 §4。[作者原文](https://pub.math.leidenuniv.nl/~smitbde/papers/2000-de_Smit_Edixhoven.pdf)。

2. **局部新形式、诱导导子与 epsilon 规范。** R. Schmidt, *Some remarks on local newforms for GL(2)*, J. Ramanujan Math. Soc. 17 (2002), 115–147，§1.1、§1.2 的导子表、Theorem 2.3.2、Lemma 3.2.1 及 Theorem 3.2.2。此处的有限 $S_3$、$A_4$ 模型和两个三进 Gauss 和均在正文写出；不能从“同为深度零”猜测它们。[作者原文](https://math.ou.edu/~rschmidt/papers/gl2.pdf)。

3. **二次基变换及其纤维。** R. P. Langlands, *Base Change for GL(2)*, Annals of Mathematics Studies 96 (1980)，§2，pp.13–14 的全局性质 A–F，特别是 C 的二次诱导例外；证明在 §11。这里应用于 $\mathbb Q$ 到 $K$，没有从模 $p$ 表示冒作复数 Euler 参数。[作者重排原文](https://publications.ias.edu/sites/default/files/base-change-for-gl2_rpl_0.pdf)。

4. **完整标准 $L$ 函数的整延拓及函数方程。** H. Jacquet–R. P. Langlands, *Automorphic Forms on GL(2)*, Lecture Notes in Math. 114 (1970)，Theorem 11.1；作者重排 PDF 标页 176、PDF p.180，及其 cusp-form 证明 pp.178–182。应用在 $K$ 上的 cuspidal $\operatorname{BC}_K(f)\otimes\kappa$，避免只引用 Rankin–Selberg 早期论文引言中尚未在该文展开的全局公告。[作者链接的完整原文](https://sunsite.ubc.ca/DigitalMathArchive/Langlands/pdf/jl-ps.pdf)。

此外使用标准新旧形式分解、有限群表示的完全可约性、Chebotarev、Clifford 理论，以及模形式 Tate 表示的绝对不可约性。所有实际扭曲数据、$Y$ 的负中心值、CM 因子的取向与分量收缩分别引用 R348、R330、R376；它们的范围没有在本篇扩大。本文为纯证明，没有用小素数试算替代上述全素数论证。

