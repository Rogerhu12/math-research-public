# R169：尖点型商的饱和微分格与指定尖点的 Whittaker 行

日期：2026-11-13。

**状态：已证明的整格与指定尖点判据。** 本文延续 R166 的真实尖点型商，给出不含 Hecke 投影分母的微分构造，以及一个完全显式的有限群特征标公式。公式使用同一个实际尖点所确定的加性角色，不能将它换成另一个较有利的频率。

结论的方向需要区分：单个新形式有限类型内的交格及其指定行是精确的；指定行为单位是完整最优商形式浸入的**充分**条件。对完整 Hecke/Galois 轨道不声称反向，因为不同新形式间的同余可能产生更多整微分。实际分母排除另以相应实际商的有理点群有限为前提。R166 的正根数，甚至一个未经准确秩定理连接的非零中心值，都不代替这个前提。

## 1. 设置和结论

保留 R166 的实际曲线、完整模 $p$ 像、小惯性假设和配对分支
$$
X=X_E^\alpha(p),\qquad p>37,\qquad
r(G_{\mathbb Q})=N=C\rtimes\langle\tau\rangle,
\qquad r(I_p)=C^3.
$$
令 $d=(p+1)/3$。取 R166 构造的、平凡 nebentype、水平 $p^2$、权二归一化新形式 $f$，有限深度零尖点型为 $R_\theta$，其中
$$
\theta:C/\mathbb F_p^\times\longrightarrow\mu_d,
\qquad \operatorname{ord}\theta=d>4.
$$
阶三字符记为 $\vartheta$，并置
$$
\varphi_+=\theta\vartheta,
\quad\varphi_-=\theta\vartheta^{-1},
\quad
\mathcal P_\theta=
\{\varphi_+,\varphi_+^{-1},\varphi_-,\varphi_-^{-1}\}.
\tag{169.1}
$$
四个字符两两不同，均在 $R_\theta$ 中出现一次。

下文将中心商掉，记
$$G=\operatorname{PGL}_2(\mathbb F_p),\qquad
\overline C=C/\mathbb F_p^\times,
\qquad |\overline C|=p+1.$$
在一个实际几何尖点选 Tate 参数 $t=q_{\rm Tate}^{1/p}$ 和实际原始根 $\psi(1)=\zeta_p$。同时对所有矩阵作一次基变换后，可以使用
$$
u_x=\begin{pmatrix}1&x\\0&1\end{pmatrix},
\qquad d_s=\begin{pmatrix}s&0\\0&1\end{pmatrix}
\quad(x\in\mathbb F_p,\ s\in\mathbb F_p^\times).
\tag{169.2}
$$
尖点余切泛函 $\Lambda$ 满足
$$\Lambda(\rho(u_x)v)=\psi(ax)\Lambda(v),\qquad
a\in\mathbb F_p^\times.\tag{169.3}$$
这里的 $\overline C$ 嵌入、$u_x$ 和 $a$ 必须由同一实际基同时确定。改变坐标时三者一起变换；(169.3) 不授权在保持实际点不变时自由选 $a$。

对 $\varphi\in\mathcal P_\theta$、$a,b\in\mathbb F_p^\times$，定义
$$
\boxed{
\mathcal B_{\theta,\varphi}(a,b)
=\frac1{p(p+1)}
\sum_{x\in\mathbb F_p}\sum_{c\in\overline C}
\psi(-ax)\varphi(c)^{-1}
\operatorname{Tr}R_\theta(u_xc d_{a/b}).}
\tag{169.4}
$$
特征标的全部值在 §6 明列。这个公式不包含 $f$ 的其他 Fourier 系数。

设 $\ell\nmid p(p^2-1)$，$X$ 在 $\ell$ 为未分歧完整水平曲线扭曲。取足够大的系数离散赋值环 $\mathcal O$，包含 $f$ 系数和上述有限角色值。令
$$
\mathfrak W_{\theta,\varphi,a}
=\bigl(\mathcal B_{\theta,\varphi}(a,b):
b\in\mathbb F_p^\times\bigr)\subset\mathcal O,
\qquad
\mathfrak W_{\theta,a}
=\sum_{\varphi\in\mathcal P_\theta}
\mathfrak W_{\theta,\varphi,a}.
\tag{169.5}
$$

**定理 169.1。** 有以下结论。

1. $f$ 在该实际配对分支上生成一个维数 $p-1$ 的有限类型空间 $V_{f,\alpha}$。它与完整整微分格的交格，恰由 §2 的真实拉回微分的有限群轨道生成。没有未控制的 Hecke 同余指数。
2. 在该交格中，$\varphi$ 角色子空间的交格是一个秩一整直和项。其在指定尖点的一次系数理想，恰为 (169.5) 的 $\mathfrak W_{\theta,\varphi,a}$；四个角色的和给 $\mathfrak W_{\theta,a}$。
3. 这些微分的泛纤维都属于 R166 相应完整有理轨道商的拉回空间。对该商作最优化后，若 $\mathfrak W_{\theta,a}=\mathcal O$，则最优商的尖点余切映射满射，因而给形式浸入。
4. 若该实际最优商 $A$ 另满足 $A(\mathbb Q)$ 有限，则任何与 $E[p]$ 同余的实际椭圆曲线 $F/\mathbb Q$，在分母素数 $\ell$ 所确定的实际尖点，都必须满足
   $$
   \mathfrak W_{\theta,\varphi,a}\subset\mathfrak m_{\mathcal O}
   \quad\text{对每个 }\varphi\in\mathcal P_\theta.
   \tag{169.6}
   $$
   对每个被这样保留的完整新形式轨道都有相同必要条件。

每个指定行在特征零中均非零。这一事实证明固定 $p,\theta,\varphi$ 的行理想不是零理想；**没有**证明其在所有实际 Tate 素数上为单位。

## 2. 首系数为一的真实映射

先在完整不连通曲线上工作
$$\mathscr X(p)=\coprod_\alpha X^\alpha(p).$$
给定完整基 $(P,Q)$，令 $\phi:E\to E/\langle Q\rangle$ 为商同源，$\widehat\phi$ 为对偶。定义
$$
\nu(E;P,Q)=
\bigl(E/\langle Q\rangle,
\widehat\phi^{-1}\langle P\rangle\bigr)
\in X_0(p^2).
\tag{169.7}
$$
因为 $P,Q$ 为不同的 $p$ 直线，右边的阶 $p^2$ 子群是循环群。这个构造只依赖两条有序直线，故在完整水平基的分裂对角环面下不变。它是实际模映射，延拓到紧化曲线；在 $\ell\ne p$ 的好模型上同样整。

解析上，$\delta=\operatorname{diag}(1,p)$ 给
$$
\delta\Gamma(p)\delta^{-1}\subset\Gamma_0(p^2),
\qquad z\longmapsto z/p.
$$
确实矩阵变成 $\bigl(\begin{smallmatrix}a&b/p\\pc&d\end{smallmatrix}\bigr)$，其左下角被 $p^2$ 整除。

在标准 Tate 基
$$E_{t^p},\qquad P=\zeta_p,\qquad Q=t$$
处，(169.7) 为
$$\nu(E_{t^p};\zeta_p,t)=(E_t,\mu_{p^2}).$$
若
$$\omega_f=f(q)\frac{dq}{q},\qquad
f(q)=\sum_{n\ge1}a_n(f)q^n,\quad a_1(f)=1,$$
则
$$
\boxed{\Omega_f=\nu^*\omega_f
=\sum_{n\ge1}a_n(f)t^{n-1}dt.}
\tag{169.8}
$$
特别 $\Lambda(\Omega_f)=1$。

归一化新形式的系数为代数整数；R72 §4 的好约化 $q$ 展开证明遂给 $\omega_f$ 整。因此所有真实有限群移位 $\rho(g)\Omega_f$ 在每个分支均为整微分。

在最初的基行向量规范 $T_g(b)=b\,{}^tg$ 中，余切表示用 $\rho(g)=(T_{g^{-1}})^*$。保持 Tate 乘法线的幺幂群起初可以是下三角群。将该群、对角环面及 Cartan **同时**共轭，才得到 (169.2)；这只为统一矩阵记法，不改变 (169.8) 的原始性或实际尖点。

## 3. 有限类型及完整交格的饱和

### 3.1 同一个 $f$ 的有限类型

映射 $\nu$ 与远离 $p$ 的实际 Hecke 对应相容。因此在整个不连通曲线上，$\Omega_f$ 是同一个 $f$ 的远离 $p$ Hecke 特征向量；这里没有先投到一个可能带分母的 Hecke 幂等元。

R166 已使用的深度零局部类型对应，或将 $z\mapsto z/p$ 后的局部新向量放入 $\pi_{f,p}^{K(p)}$，给
$$
V_f:=\operatorname{span}_{\overline{\mathbb Q}}
\{\rho(g)\Omega_f:g\in G\}\simeq R_\theta.
\tag{169.9}
$$
平凡中心角色使有限作用通过 $G$。分裂对角环面固定 $\Omega_f$；$R_\theta$ 在该环面的固定子空间为一维。

有限表示 $R_\theta$ 限制到 $\operatorname{PSL}_2(\mathbb F_p)$ 仍绝对不可约。由指数二的 Clifford 理论，唯一可能障碍是
$$R_\theta\simeq R_\theta\otimes\delta_{\det},$$
其中 $\delta_{\det}$ 为非平凡二次行列式字符。这要求 $\theta^2$ 为非平凡二次 Cartan 字符，从而 $\operatorname{ord}\theta=4$；当前 $d>4$ 排除了它。

固定分支 $\alpha$ 的限制映射 $i_\alpha^*:V_f\to H^0(X^\alpha,\Omega^1)$ 是 $\operatorname{PSL}_2$ 等变的，且 (169.8) 使它非零。因此它单射；其像就是 $V_{f,\alpha}$。全部 $G$ 的作用可以通过这个单射输送到 $V_{f,\alpha}$。当 $g$ 改变配对分支时，这个输送作用并不声称是固定分支上的几何甲板变换；其每个轨道向量仍是相应真实模映射拉回的限制。

### 3.2 不使用 Hecke 格直和

令
$$
L=V_{f,\alpha}\cap H^0(\mathcal X^\alpha_{\mathcal O},
\Omega^1),\qquad
L_0=\sum_{g\in G}\mathcal O\,i_\alpha^*\rho(g)\Omega_f.
\tag{169.10}
$$
两者都是满格，$L_0\subset L$；两者在真正的几何 $\operatorname{PSL}_2$ 作用下稳定。因为 $\ell\nmid|G|$，在足够大的分裂系数环上，普通有限不可约类型的约化仍绝对不可约。故 $L_0/\mathfrak mL_0$ 是一个维数 $p-1$ 的简单 $\operatorname{PSL}_2$ 模。

包含映射 $L_0\to L$ 的约化非零：向量 $\Omega_f$ 在 (169.8) 的一次系数为 $1$，不可能属于 $\mathfrak mL$。简单性使这个约化单射；两个模维数相同，故它是同构。Nakayama 引理给
$$\boxed{L_0=L.}\tag{169.11}$$

这证明的是单个特征零有限类型与**完整**微分格的交格。它允许别的新形式与 $f$ 在 $\ell$ 同余；没有把这些不同 Hecke 空间的格认成整直和。特别，输送的整个 $G$ 作用现在保持 $L$。

## 4. 标准 Kirillov 整基

记
$$
P_b=\frac1p\sum_{x\in\mathbb F_p}\psi(-bx)\rho(u_x),
\qquad v_b=P_b\Omega_f
\quad(b\in\mathbb F_p^\times).
\tag{169.12}
$$
尖点型没有幺幂不变量。分裂对角群在非平凡幺幂字符上传递；维数为 $p-1$，所以每个非平凡幺幂字符恰出现一次。由 (169.3)、(169.8)，
$$\Lambda(v_b)=\begin{cases}1&b=a,\\0&b\ne a.\end{cases}\tag{169.13}$$

由于 $d_s\Omega_f=\Omega_f$，直接共轭 (169.12) 得
$$\rho(d_s)v_b=v_{b/s}.\tag{169.14}$$
向量 $v_a$ 的首系数为 $1$，在 $L$ 中原始。由 (169.11)、(169.14)，每个 $v_b$ 都原始。每个 $P_bL$ 为秩一整直和项，故 $v_b$ 生成它。于是
$$
\boxed{L=\bigoplus_{b\in\mathbb F_p^\times}\mathcal O v_b.}
\tag{169.15}
$$
这一步固定了基的整尺度，不能仅由一个特征零 Kirillov 同构推断。

对任意出现的 Cartan 字符 $\varphi$，令
$$e_\varphi=\frac1{p+1}\sum_{c\in\overline C}
\varphi(c)^{-1}\rho(c).\tag{169.16}$$
这是 $L$ 的整幂等元，像为秩一整直和项，且
$$
e_\varphi L=(e_\varphi V_{f,\alpha})
\cap H^0(\mathcal X^\alpha_{\mathcal O},\Omega^1).
\tag{169.17}
$$
右边任一元素先属于 $L$，再被 $e_\varphi$ 固定，即证明等式。

## 5. 真实下降和所选最优商

需要将 (169.16) 与 R166 的实际下降对齐。原来的实际下降有限群是
$$N^*=\{n^{-t}:n\in N\}.$$
对 $J=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$，整个 $\operatorname{GL}_2$ 上有
$$g^{-t}=\det(g)^{-1}JgJ^{-1}.$$
由于 $R_\theta$ 中心平凡，$g\mapsto g^{-t}$ 在本有限类型上正是这个几何共轭。$J$ 的行列式为 $1$。同时取 $\varphi$ 和 $\varphi^{-1}$，也消除了上同调与协变 Tate 模对偶所产生的逆字符。

因此，只要将 Cartan、幺幂群和实际尖点一起按该式对齐，(169.1) 的四条角色线正是 R166 完整 $N^*$ 中心投影所保留的有限子空间。没有自由改变实际配对乘子或实际根。

更具体地，设 $e$ 为 R166 在整个实际 Jacobian 上的有理投影，$B=e\mathscr J$，$B_\alpha=e(J_\alpha)$。每个 $e_\varphi V_f$ 都在对应泛纤维微分投影的像内。限制到 $X^\alpha$ 后，它属于真实满射 $J_\alpha\to B_\alpha$ 的微分拉回空间：阿贝尔子簇 $B_\alpha\hookrightarrow B$ 在特征零的余切限制满射。

将此满射最优化为 $q:J_\alpha\twoheadrightarrow A_\alpha$。R72 §2 所用 Raynaud–Mazur 正合性在未分歧 $\ell$ 处给
$$
q^*\omega_{A_\alpha}
=q^*H^0(A_\alpha,\Omega^1)
\cap H^0(\mathcal X^\alpha,\Omega^1).
\tag{169.18}
$$
先在未分歧整数环应用 $e=1<\ell-1$，随后才平坦扩张至 $\mathcal O$。由 (169.17)，所构造的每个 $e_\varphi v_b$ 都是真实最优商的整微分拉回。

这里不要求 $e$ 在 $\ell$ 整。整的是有限群投影 (169.16)；属于正确的有理商靠泛纤维识别，属于其正确整格靠 (169.18)。

## 6. 指定行的精确特征标公式

设 $E_\varphi$ 为 $e_\varphi$ 在 (169.15) 中的矩阵。由 (169.14)，$\rho(d_{a/b})v_a=v_b$，所以
$$
(E_\varphi)_{a,b}
=\operatorname{Tr}\bigl(P_a e_\varphi\rho(d_{a/b})\bigr).
\tag{169.19}
$$
展开两个整幂等元即得 (169.4)。再由 (169.13)，
$$\Lambda(e_\varphi v_b)=\mathcal B_{\theta,\varphi}(a,b),$$
证明 (169.5) 是 (169.17) 的精确余切像。

为使公式完全可复验，以下给 $\operatorname{Tr}R_\theta(g)$ 的全部四类值：

| $g\in G$ 的类型 | 特征标 |
|---|---:|
| 单位元 | $p-1$ |
| 非平凡幺幂元 | $-1$ |
| 分裂正则半单元 | $0$ |
| 非分裂正则半单元，特征值 $\gamma,\gamma^p\in\mathbb F_{p^2}^\times$ | $-\theta(\gamma)-\theta(\gamma^p)$ |

最后一行不依赖给 $g$ 选哪个标量提升，因为 $\theta|\mathbb F_p^\times=1$，也不依赖交换两个特征值。最后一行是 R166 (166.6) 的 Cartan 字符公式。幺幂行由所有非平凡幺幂字符各出现一次得 $\sum_{b\ne0}\psi(bx)=-1$；分裂正则行由 (169.14) 无不动基向量得 $0$。因此此处不需要另行猜测有限 Bessel 函数的归一化常数。

可使用 $\mathbb Z[\zeta_{p(p+1)},1/(p(p^2-1))]$ 作为公式的公共系数环，再在指定 $\ell$ 上方局部化。分母 $p(p+1)$ 在所有实际 Tate 素数上均为单位。

### 6.1 指定行在特征零非零

这一点不是把“某个频率非零”直接换成“指定频率非零”。它来自公式的独立圆分 Galois 对称。

对每个 $r\in\mathbb F_p^\times$，存在固定 $\zeta_{p+1}$、把 $\zeta_p$ 送到 $\zeta_p^r$ 的自同构 $\sigma_r$。式 (169.4) 给
$$
\sigma_r\bigl(\mathcal B_{\theta,\varphi}(a,b)\bigr)
=\mathcal B_{\theta,\varphi}(ra,rb).
\tag{169.20}
$$
若一个指定行在特征零全为零，(169.20) 会使每一行都为零。但 $E_\varphi$ 是秩一幂等元，迹为 $1$，矛盾。故每个指定行理想非零。

式 (169.20) **不**推出指定素理想下的单位性：它同时改变该素理想。即使实际 $\ell\equiv\pm1\pmod p$，也只提供相应 Frobenius 约束，不能把同一实际尖点的 $a$ 换成任意 $ra$。

### 6.2 精确的有限线性代数边界

这些矩阵满足
$$E_\varphi^2=E_\varphi,\quad
\operatorname{rank}E_\varphi=1,\quad
\operatorname{Tr}E_\varphi=1.$$
因此所有行理想的**和**为单位理想。它不保证某个预先指定行是单位。对角项 $\operatorname{Tr}(P_a e_\varphi)$ 是该行的一个元素：它为单位足够；它为零则不等价于整行消失。后续使用有限群迹或平均公式时必须保留这个区别。

## 7. 形式浸入与实际分母的必要条件

若 (169.5) 中某个指定行为单位，存在一个整微分 $e_\varphi v_b$ 的指定尖点一次系数为单位。由 (169.18)，它来自实际最优商。因此尖点余切映射满射，证明定理 169.1(3)。

不声称反向：完整 $A_\alpha$ 的泛纤维包含全部相关新形式及其 Galois 轨道。不同 $f$ 的单独交格之和未必是整个交格；Hecke 同余可能产生额外整微分。本文既不需要排除这些额外微分，也不把各单独行全部消失认作完整商不浸入。

若另有 $A_\alpha(\mathbb Q)$ 有限，R72 §§7–9 的实际分母论证可逐字应用：

- 实际分母素数满足 $\ell\equiv\pm1\pmod p$，故 $\ell>p+1$、$\ell\nmid p(p^2-1)$；扭曲在 $\ell$ 未分歧，实际有理点与一个唯一提升的尖点落在同一剩余圆盘。
- 全尖点除子次数为 $(p^2-1)/2$，为 $\ell$ 单位；次数无关基点的 Abel–Jacobi 映射可用于同一个实际最优商。
- Manin–Drinfeld 尖点挠性、有限有理点群和好约化形式群无挠性迫使该实际点与尖点具有相同像。若存在上述单位微分，形式浸入迫使两点相同，与有限 $j$ 的实际非尖点矛盾。

所以每个被实际有限商保留的行都满足 (169.6)。若同时有 R69/R72 的实际有限三次 Steinberg 商，旧三色行理想与这里的尖点型行理想必须在**同一个实际尖点和同一个剩余嵌入**下同时消失。

## 8. 未消除的两个缺口

1. **指定行单位性。** 本文给了整格、精确公式、指定行的特征零非零，却没有证明 (169.5) 在所有实际 $\ell\equiv\pm1\pmod p$ 上为单位，也没有证明它一定补掉旧三色理想的固定 $\pm a$ 共同零点。Maschke、某个频率为单位、矩阵总迹为一、或对角迹的平均非零，都不替代此项。
2. **实际有限商。** R166 目前证明实际非零商、不可约性和正根数。其权二因子与二维 Artin 因子在 $p$ 均有导子指数二。R69 所用的 squarefree level、环类导子与 level 互素的 Bertolini–Darmon 输入不能直接套到这里。即便证明一个中心值非零，还要给适用于这些准确局部数据的已发表秩零输入或独立有限性证明。本文的几何定理不依赖该步骤，算术分母结论明确依赖它。

因此 R169 提供了新的可直接验证的实际有限型整格接口，没有完成一般 exceptional 集或 Serre uniformity。

**后续接口更新（同日 R172）。** [R172](R172-cuspidal-central-values-and-actual-rank-zero-quotients.md) 已用已发表的一般新形式 Euler-system 定理补齐第二项中的条件性秩零输入：准确中心值非零推出所选实际商的有理点群有限。各条角色线须属于已证明有限的实际有理投影像；[R173](R173-rational-cuspidal-orbits-and-cube-subgroup-row-ideals.md) 随后证明同一完整有理轨道包含全部原始 $\theta$ 共轭及两个三次方向。第一项的指定行单位性和可用中心值本身仍未解决。

## 9. 输入与准确定位

- [R166](R166-small-inertia-cuspidal-positive-sign-quotients.md) §§2–5：真实非空有限类型、四个正号 Cartan 字符、完整左右作用与每个配对分支的实际商。本文另用 (169.7)–(169.11) 证明了所需整格，而不是从 R166 的特征零投影猜测整性。
- [R72](R72-optimal-quotient-cusp-immersion-and-exceptional-denominators.md) §§2、4、7–9：最优商余切交格、好约化 $q$ 展开原则、实际 Tate 剩余圆盘及全尖点除子路径。
- B. Mazur, *Rational isogenies of prime degree*, Invent. Math. **44** (1978), 129–162，Proposition 1.2，印刷 pp.135–136；Corollary 1.1，p.137：[原刊 DOI](https://doi.org/10.1007/BF01390348)，[作者全文](https://www.math.columbia.edu/~goldfeld/Mazur-Goldfeld1978.pdf)。使用的是小分歧下连通核的阿贝尔概形正合性。
- M. Raynaud, *Schémas en groupes de type $(p,\ldots,p)$*, Bull. Soc. Math. France **102** (1974), 241–280，Théorème 3.3.3、Corollaire 3.3.6(1)，p.268：[原刊](https://www.numdam.org/article/BSMF_1974__102__241_0.pdf)。先在未分歧基上使用，再扩张系数。
- C. Virdol, *Zeta functions of twisted modular curves*, J. Aust. Math. Soc. **80** (2006), 89–103，§§2.4–2.6：[原刊](https://www.austms.org.au/Publ/JAustMS/V80P1/pdf/t56.pdf)。完整等变类型与实际扭曲规范已在 R143 §2、R166 §5 逐项核定；这里的指定行及格证明自含。

全文没有数值扫描，也没有将 Studnia 的 thesis/submitted 商或整性定理作为已发表输入。
