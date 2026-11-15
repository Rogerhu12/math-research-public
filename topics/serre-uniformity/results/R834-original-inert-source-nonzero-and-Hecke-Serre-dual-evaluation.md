# R834 — 原六项源的全局非零、Hecke 定位的 Serre 对偶与指定点泛函

**状态：已证明下文的全局非零与准确对偶接口；原 $P_0$ 配对非零仍未证明。**

对所有原允许 $p\ge41,\ p\equiv11\pmod{12}$，R833 的指定六项 supersingular 源作为全局截面非零，其 connecting class 也非零。该 Hecke 支撑中没有 tame 权六模形式，因此 connecting class 唯一决定原 supersingular 截面。最后把原 $P_0$ 评价准确写成一个 Serre 对偶配对，保留原 $B,c,d_0,\kappa_\nu$ 与原微分。

本文没有以全局非零代替指定点值非零，也没有删除原 primitive/Legendre 条件。

## 1. 原对象、有限角色与一个实际单位特征值

依赖 [R826 原 companion](R826-original-inert-companion-theta-CM-pairing.md)、[R826 实际八源运输](R826-certified-inert-Gaussian-source-transport.md)、[R830](R830-original-inert-angular-Hecke-lift-and-tame-filtration.md) 和 [R833](R833-original-inert-supersingular-weight-six-and-quaternionic-evaluation.md)。始终使用它们的同一选定 $p$ 上 place、共同 tame fine level、原点与标架。

原两个权八 Gaussian 新形式记为 $F_3,F_7$，有限角色满足
$$
 \epsilon_b(1+i)=\xi_8^b,\qquad
 \xi_8=(1+i)/\sqrt2.
 \tag{834.1}
$$
理想每个只求和一次。范数 $5$ 的两个理想可取生成元 $2+i,2-i$。在 $\mathbb Z[i]/3$ 中，它们分别为 $(1+i)^7,(1+i)^5$，而
$$
 (2+i)^7=-278-29i.
$$
所以
$$
\begin{aligned}
 a_5(F_3)
 &=\xi_8^5(-278-29i)+\xi_8^7(-278+29i)\\
 &=307i\sqrt2,\\
 a_5(F_7)&=-307i\sqrt2.
\end{aligned}
 \tag{834.2}
$$
这是纸面上两个实际理想项的计算，没有作新的素数扫描。

$\sqrt{307}<18$，而 $2,3,5,7,11,13,17$ 均不整除 $307$，故 $307$ 是素数；又 $307\equiv7\pmod{12}$。因此在本篇的全部 $p\equiv11\pmod{12}$ 下，
$$
 \gamma_p=\overline{307i\sqrt2}\ne0.
 \tag{834.3}
$$
同一符号 $i,\sqrt2$ 沿原嵌入约化；不把二者的 Frobenius 改成恒等。

R826 的 $C_{b,d,p}=d^{p-7}C_{b,p}(t^d)$，$d=1,2,4$，在 $T_5$ 下的特征值分别为
$$
 5^{-6}\gamma_p,\qquad -5^{-6}\gamma_p
 \tag{834.4}
$$
（分别对应 $b=3,7$）。两者是不同的单位；$T_5$ 与原 oldform 及 $q_*=q^{1/12}$ 的 tame 运输相容。

## 2. 原指定六项作为全局源非零

在 R826 的共同 fine level 上定义实际权 $p-5$ 形式
$$
 V_p=\sum_{\substack{b=3,7\\d=1,2,4}}
          \kappa_{b,d}\,\overline{C_{b,d,p}}(q_*).
 \tag{834.5}
$$
$\kappa_{b,d}$ 是原固定 $\widehat U M_{b,d}\widehat U^t$ 的 FG 条目，在这里作为常数系数；不是重新选择的线性组合。R826 的真实 Norm 证书证明六个系数在所有允许 $p$ 下均为单位。

将 (834.5) 分为 $V_{3,p}+V_{7,p}$。每一组都不为零：在原变量 $t=q_*$ 中，其首个 $t$ 系数为
$$
 [t]V_{b,p}=\kappa_{b,1}\ne0.
 \tag{834.6}
$$
$d=2,4$ 的项不会贡献 $t$ 项；其原 $d^{p-7}$ 因子完全保留。

如果 $V_{3,p}+V_{7,p}=0$，再施 $T_5$ 并用 (834.4)，会得到
$$
 V_{3,p}-V_{7,p}=0.
$$
因为 $2$ 与 (834.4) 的特征值均可逆，所以两组都为零，与 (834.6) 矛盾。因此
$$
 \boxed{V_p\ne0.}
 \tag{834.7}
$$

令 $\mathcal A$ 为 Hasse invariant，$Z$ 为完整 supersingular 除子。它处处简单。权 $p-5$ 的限制映射到 $Z$ 是单射：若 $V_p|_Z=0$，则 $V_p/\mathcal A$ 是全纯权 $-4$ 形式，而正次数 Hodge 线丛的负次幂没有非零全局截面。因此
$$
 V_p|_Z\ne0.
 \tag{834.8}
$$

R833 的权六截面为 $\Gamma_{\nu,p}=\beta^{6-p}(C_{\nu,p}|_Z)^p$，其中
$\beta=\overline E_{p+1}|_Z$ 处处非零。于是指定六项
$$
 W_p=\sum_{\substack{b=3,7\\d=1,2,4}}
       \kappa_{b,d}^{\,p}\Gamma_{b,d,p}
     =\beta^{6-p}(V_p|_Z)^p
 \tag{834.9}
$$
满足
$$
 \boxed{W_p\not\equiv0\quad\text{on }Z.}
 \tag{834.10}
$$
这还没有确定 $W_p(P_0)$。

## 3. 原 Hecke 特征不出现在任何 tame 权六空间中

本节排除的是**相同 Hecke eigensystem**，比只排同一 $q$ 级数更强。它不使用尚未核定的 old/new 首项选择。

对四个原 $f_\epsilon=F_3,F_7,G_1,G_5$，其权为八，level 只含 $2,3$。本篇的 $p$ 在 $\mathbb Q(i)$ 惰性，所以
$$
 a_p(f_\epsilon)=0.
 \tag{834.11}
$$
记 $\omega_{\rm cyc}$ 为模 $p$ cyclotomic character，$\omega_2$ 为 niveau-two fundamental character，约定
$\omega_{\rm cyc}|_{I_p}=\omega_2^{p+1}$。

使用 Deligne 与 Fontaine–Serre 的低权惯性定理：tame level 权 $k$、$2\le k\le p+1$ 的归一新形式，其普通情形的惯性半单化为
$1\oplus\omega_{\rm cyc}^{k-1}$；非普通情形为
$\omega_2^{k-1}\oplus\omega_2^{p(k-1)}$。
本文核对的原作者证明来源为 Christophe Breuil,
*p-adic Hodge theory, deformations and local Langlands*, Barcelona lectures (2001),
[全文](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/Barcelone.pdf)，
Theorems 8.1.4 and 8.1.5（该 PDF 的第 48--49 页）。
该处给出这两个惯性形状及 strongly divisible lattice 的证明；本篇只在 $k=8,6<p$ 使用。

由 (834.11)，
$$
 \overline\rho_{f_\epsilon}|_{I_p}
   =\omega_2^7\oplus\omega_2^{7p}.
 \tag{834.12}
$$
两字符不同，且 unramified quadratic Frobenius 交换它们；原 CM 表示在 $G_{\mathbb Q_p}$ 上不可约。特别它不是 Eisenstein 的可约表示。

R833 的原特征是
$$
 a_{\Gamma_\nu}(\ell)
   =\ell^{-1}\overline{a_\epsilon(\ell)}^{\,p}
       \qquad(\ell\nmid6p).
$$
所以其半单 Galois 表示为
$$
 \rho_{\Gamma_\nu}
   =\overline\rho_{f_\epsilon}^{[p]}
          \otimes\omega_{\rm cyc}^{-1},
 \tag{834.13}
$$
其中 $[p]$ 只表示对表示系数取 Frobenius。由 Chebotarev 和二维半单表示的 trace 判据，该式由所显示的远离 $6p$ 的全部特征值确定。其惯性字符准确为
$$
 \boxed{\quad
 \omega_2^{6-p}\oplus\omega_2^{6p-1}.
 \quad}
 \tag{834.14}
$$
系数 Frobenius 先将 (834.12) 两项交换，不改变它们的无序集合；再减去 $p+1$ 才得到 (834.14)。

这不是 tame 权六可以有的惯性：

- 普通权六的惯性字符是 niveau one；但 $6-p\equiv7\not\equiv0\pmod{p+1}$。
- 非普通权六的指数是 $\{5,5p\}$。若 $6-p\equiv5\pmod{p^2-1}$，则 $p+1\mid1$；若 $6-p\equiv5p$，则 $p+1\mid6$。两者在 $p\ge41$ 都不可能。

因此 (834.14) 排除所有 tame 权六 cuspidal eigensystems。Eisenstein eigensystem 的可约表示也已经被局部不可约性排除。

这一结论适用于 mod $p$ 的全层权六空间，不只特征零新形式。确实，在任何固定 fine tame level 上，
$$
 H^1(\omega^6)
  =H^0(\omega^{-4}(-D_{\rm cusp}))^\vee=0,
$$
故权六整空间满足基变换且无 $p$ torsion；其有限 Hecke 代数位于一个自由整模的 endomorphism ring 中。标准有限平坦 Hecke 代数的 eigencharacter 提升论证将一个 mod $p$ eigensystem 提升为特征零 eigensystem，再分到 cuspidal 或 Eisenstein 部分。上面的两种排除都适用。若假设的形式先在全 $\Gamma(N)$ level 上，可用 $g(\tau)\mapsto g(N\tau)$ 放到 $\Gamma_1(N^2)$：对 $\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\Gamma_1(N^2)$，共轭矩阵 $\left(\begin{smallmatrix}a&Nb\\c/N&d\end{smallmatrix}\right)$ 属于 $\Gamma(N)$。这是只在 $N$ 处的 tame 平移，与远离 $Np$ 的 Hecke 作用交换，保持所假设的 eigensystem；其新旧形式分解的各个新层仍与 $p$ 互素。此步骤仅用于排除假设的权六形式，不重选本篇原 $\Gamma_\nu$ 向量。

综上，对四个原特征各自的 maximal ideal $\mathfrak m_\nu$，
$$
 \boxed{M_6(\mathfrak m_\nu)=0.}
 \tag{834.15}
$$
这里表示该有限 Hecke 模的整个局部化为零；没有假设 Hecke 作用半单。若局部化非零，有限维交换代数上就会有同一 eigensystem 的非零 eigenvector，与已证排除矛盾。

## 4. 准确的 connecting class 与局部化唯一性

在共同 fine modular curve $X$ 上取
$$
 M_6=H^0(X,\omega^6),\qquad
 \mathcal S_6=H^0(Z,\omega^6),\qquad
 \mathcal Q_{p-5}
   =H^0(X,\omega^{p-5}(-D_{\rm cusp})).
 \tag{834.16}
$$
最后一个是 cusp forms 的空间；不能把 cusp 条件省掉。

Hasse 的简单零给出短正合列
$$
 0\longrightarrow\omega^{7-p}
   \xrightarrow{\ \mathcal A\ }\omega^6
   \longrightarrow\omega^6|_Z\longrightarrow0.
 \tag{834.17}
$$
因 $p\ge41$，$H^0(\omega^{7-p})=0$，且上节已证 $H^1(\omega^6)=0$。于是
$$
 0\longrightarrow M_6\longrightarrow\mathcal S_6
   \xrightarrow{\ \delta\ }H^1(X,\omega^{7-p})
   \longrightarrow0.
 \tag{834.18}
$$
Kodaira–Spencer 与 Serre duality 给出向量空间识别
$$
 H^1(X,\omega^{7-p})\simeq\mathcal Q_{p-5}^{\vee}.
 \tag{834.19}
$$

**Hecke 约定。** (834.17)--(834.18) 使用同源对应、pullback 和 trace 自然诱导的 Hecke 作用。对 (834.19) 的右侧，本篇只运输这个已经定义的作用；没有使用 Serre 给 Tate 的信中 (15) 关于对偶 Hecke 公式的猜测，也没有把它未经证明地改成某个 Satake/diamond 公式。

把 (834.18) 在任一原 $\mathfrak m_\nu$ 处局部化。由 (834.15)，
$$
 \boxed{\quad
 \delta:
   (\mathcal S_6)_{\mathfrak m_\nu}
       \xrightarrow{\ \sim\ }
   H^1(X,\omega^{7-p})_{\mathfrak m_\nu}.
 \quad}
 \tag{834.20}
$$
这保留全部重数和 generalized eigenvectors；没有偷偷取一个假定一维的 eigenspace。

(834.2)--(834.4) 也使两组 $F_3,F_7$ 的原 Hecke maximal ideals 不同。$W_p$ 位于这两个局部部分的直和中，所以由 (834.10)、(834.20)，
$$
 \boxed{\delta(W_p)\ne0.}
 \tag{834.21}
$$
因此至少存在一个真实 cusp form $u\in\mathcal Q_{p-5}$，使其与这个原 connecting class 的 Serre 配对非零。这里不将这个未知 $u$ 当作原目标中的标签 $h$。

## 5. 留数公式中的原 $12$ 与 $B$

现核 (834.19) 的准确配对常数。采用 Tate 标架归一
$$
 {\rm KS}(\omega_{\rm Tate}^{\,2})=\frac{dq}{q}.
$$
R812 的原曲线标架是
$\omega_0=\lambda^{-1}\omega_{\rm Tate}$，且 $D=\lambda^2\theta_q$，所以
$$
 {\rm KS}(\omega_0^2)
     =\lambda^{-2}\frac{dq}{q}
     =\frac{dX}{2Y}.
 \tag{834.22}
$$
这正是 MH/R812 的辅助模参数微分；原纤维仍是
$y^2=x^3-a x/4-b/4$、$dz=dx/(2y)$，在 $(a,b)=(0,4)$ 给原 $E_0$。两个导数与两种微分没有混用。

对 $v\in\mathcal S_6$，在各 supersingular 点取一个局部正则 lift $\widetilde v$。connecting class 的局部 principal part 是 $\widetilde v/A$。以 Čech convention $d(s)_{0i}=s_i-s_0$ 和正留数的 Serre trace 定义配对，则
$$
 \langle\delta(v),u\rangle
 =\sum_{P\in Z}
    {\rm Res}_P\left(
       \frac{\widetilde v\,u}{\mathcal A}
                      \right)_{\rm KS}
 \qquad(u\in\mathcal Q_{p-5}).
 \tag{834.23}
$$
这是 fine level，故每个几何点只计一次，不加入 $1/|\operatorname{Aut}(E)|$。若降到非 fine quotient，才需相应 trace/惯性处理，本篇没有这样降层。

在一个原局部标架中写帽号表示数值函数。$A$ 在 $P$ 简单消失，故由 (834.22)
$$
 {\rm Res}_P
   \frac{\widehat v\,\widehat u}{A}\frac{dX}{2Y}
     =\frac{\widehat v(P)\widehat u(P)}{DA(P)}.
$$
R833 已证明 $\widehat\beta(P)=12DA(P)$。因此
$$
 \boxed{\displaystyle
 \langle\delta(v),u\rangle
   =\sum_{P\in Z}
       \frac{\widehat v(P)\widehat u(P)}{DA(P)}
   =12\sum_{P\in Z}
       \frac{v(P)u(P)}{\beta(P)}.
 }\tag{834.24}
$$
最后一项是纤维线丛的内在商，因为权数 $6+(p-5)=p+1$。任意换局部微分标架时分子和分母以同一权缩放，所以它不依赖额外的水平标架选择。

特别在原 $P_0$，$DA(P_0)=B$，该单项是
$$
 \frac{\widehat v(P_0)\widehat u(P_0)}B.
 \tag{834.25}
$$
$B$ 是 MH33 的原 binomial 单位，不是另一个 Hasse 归一。

式 (834.24) 对所有原 $v$ 成立；(834.21) 保证它对某个 $u$ 非零。但即使取 $u=V_p$，其非零也尚未证明。不能把
$12\sum_P\beta(P)^{5-p}V_p(P)^{p+1}$
视作有限域里的正定实范数。

## 6. 原 $P_0$ 评价的准确 dual test form

(834.24) 同时给出有限集合上的一个完美配对
$$
 \mathcal S_6\times\mathcal S_{p-5}\longrightarrow k,
 \qquad
 (v,w)\longmapsto12\sum_{P\in Z}\frac{v(P)w(P)}{\beta(P)},
 \tag{834.26}
$$
其中 $k$ 是所用代数闭剩余域。它对点逐个非退化。

固定原 $P_0$ 的微分 $\omega_0=dx/(2y)$ 与原 tame level 点。定义
$\Delta_{P_0}\in\mathcal S_{p-5}$：其在其他几何 supersingular 点为零，在 $P_0$ 的原标架数值为
$$
 \widehat\Delta_{P_0}(P_0)=B.
 \tag{834.27}
$$
于是 (834.25) 给
$$
 (v,\Delta_{P_0})=\widehat v(P_0).
 \tag{834.28}
$$
这正好是原点的数值评价，不差一个 $12$ 或新 period。

令 $e$ 为 $\mathcal S_6$ 上原两个 $F_3,F_7$ Hecke primary 部分之和的 idempotent。它存在于有限维 Hecke 作用代数的 Artinian 分解中；不要求代数半单。令 $e^\#$ 为关于 (834.26) 的转置算子，定义
$$
 \Delta_{P_0,e}=e^\#\Delta_{P_0}.
 \tag{834.29}
$$
本篇不用任何未证的标准 Hecke adjoint 公式来计算 $e^\#$，只用这个准确的转置定义。

因为 $eM_6=0$，$\Delta_{P_0,e}$ 与 $M_6$ 正交。由 (834.18)、(834.23) 的对偶正合性，这个正交补恰是
$\mathcal Q_{p-5}$ 限制到 $Z$ 的像。该限制又因权 $p-5<p-1$ 为单射。因此存在唯一的真实 cusp form
$$
 u_{P_0,e}\in\mathcal Q_{p-5},
 \qquad
 u_{P_0,e}|_Z=\Delta_{P_0,e}.
 \tag{834.30}
$$
它可以为零；本篇没有假定原 Hecke 投影在这个点可见。

对于原 $W_p=eW_p$，
$$
 \boxed{\quad
 \widehat W_p(P_0)
    =\langle\delta(W_p),u_{P_0,e}\rangle.
 \quad}
 \tag{834.31}
$$
沿 R833 的全部原尺度，最终为
$$
 \boxed{\displaystyle
 \sum_{j=0}^{N-1}(-1)^j f_{N-1-j}g_j
  =(12B)^{-5}
       \left(-\frac{120c^2}{d_0}\right)^p
       \langle\delta(W_p),u_{P_0,e}\rangle.
 }\tag{834.32}
$$
$\kappa_\nu^p$ 已包含在 (834.9) 的 $W_p$ 内；共同 $c^2/d_0$ 也按原式一起取 Frobenius。没有把原点换成任意一个非零 supersingular 点。

## 7. 尚待证明的准确量

本文已证明这个**指定六项源**的全局非零及其 connecting class 的非零，且在其真实 Hecke 支撑上 connecting map 是同构。它还准确确定了原 $P_0$ 的 dual test form 和配对，没有将相同 Hecke 特征冒认作任意特征零 JL 向量。

仍须证明 (834.31) 的指定配对非零。非零 $\delta(W_p)$ 不自动保证它在 $u_{P_0,e}$ 上非零；$u_{P_0,e}$ 本身的非零以及与此 class 的非正交都未由本篇得出。

即使这一步完成，(834.32) 仍是未筛交替卷积。原主局部目标还要求同一个
$h=6i+7$、$(h,p+1)=1$，满足
$$
 P_{6i+6}(1/s)f_i g_{N-1-i}\ne0.
$$
本文不提供原高度外积或全 $p$ 有理点排除；没有新增数学执行或有限素数窗口。

## 来源

- R826、R830、R833：原 companion、Hecke 角色、全相位 Frobenius 运输与原点。
- MH33、R812 (812.1)、(812.14)--(812.17)：$B\in\mathbb F_p^\times$、真实 $E_0/dz$ 及固定 $\lambda$ 标架。
- Serre, [1987 年致 Tate 的信全文](https://aghitza.github.io/publications/translation-serre-letter-tate.pdf)，(2)--(5)、(9)、(13)：supersingular 限制序列、几何 Hecke 作用、$\beta$ 单位和正向 Tate twist。本文不使用其 (15) 的猜测。
- Breuil, [Barcelona lectures](https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/Barcelone.pdf)，Theorems 8.1.4--8.1.5：本篇所用低权惯性两种形状及证明。
