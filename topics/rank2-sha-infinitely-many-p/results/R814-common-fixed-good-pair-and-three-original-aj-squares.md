# R814 — 三个原十八阶角色的共同固定 good pair 与同一几何来源的 AJ 平方

日期：2026-11-15。**状态：已证明。** R804／R806 的三个角色可以同时使用一条固定的 weight4 CM 模形式、一个固定的有限层几何来源和三个固定的有限角色。选择这些对象时不需要知道随后采用的普通素数 p。本文还保留原负二矩与这些固定 generalized Heegner cycles 的 Abel–Jacobi 配对之间的准确平方恒等式，包括两个不同的 ordinary Euler、原 30 平滑、Artin/CM 周期和真实 de Rham 基变换。

这里的新结论是固定共同来源及其比较。本文没有证明任一指定 cycle 的 p-adic AJ 值、原全局特殊化类或原负二矩非零；也不将 weight4 的 Hodge-level-3 来源解释为椭圆曲线点。

## 1. 三个原角色及其具体比值

沿用 [R804](R804-original-order-eighteen-soule-classes-and-negative-two-localization.md)、
[R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md) 的原规范：
$$
K=\mathbf Q(\omega),\qquad \delta=1+2\omega,\qquad
j\in\mathcal J=\{4,10,16\},
$$
$$
\eta_j((a))=
\left[
 \operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
 (a\bmod17)^{16(j-9)}
\right]^{-1}.
\tag{1}
$$
有限值的提升及系数嵌入均取原来的选择。置
$$
\lambda_j=\eta_j^{-1}\psi_0^3,\qquad
\nu_j=\eta_j\psi_0^{-1}\bar\psi_0^2,\qquad
\phi_j=\lambda_j\mathbf N^{-2}.
\tag{2}
$$
在原理想角色约定中，$\phi_j=\nu_j^{-1}$。
在 Castella 的几何互反约定中，$\lambda_j$ 的 infinity type 为
$(-3,0)$，$\phi_j$ 为 $(-1,2)$；其 p-adic 表示与原表示的对应严格按
[R811 §2](R811-canonical-soule-classes-and-global-heegner-comparison.md)。
不在同一互反约定下把 $\nu_j$ 和 $\nu_j^{-1}$ 相认。

R806 已付：
$$
\mathfrak f_{\lambda_j}=(34\delta),\qquad
\varepsilon_{\lambda_j}=\eta_K,\qquad
w(\phi_j)=-1.
\tag{3}
$$
特别是 $\delta$ 在导子中恰出现一次。

定义固定的三次角色
$$
\epsilon((a))=(a\bmod17)^{96}\in\mu_3.
\tag{4}
$$
它在有理对角上平凡，导子恰为 $(17)$，且 $\epsilon(\delta)=1$。
直接从(1)相减指数得
$$
\eta_{10}=\eta_4\epsilon^{-1},\qquad
\eta_{16}=\eta_4\epsilon^{-2},
$$
$$
\boxed{\lambda_{10}=\lambda_4\epsilon,\qquad
       \lambda_{16}=\lambda_4\epsilon^2.}
\tag{5}
$$
此处 $\epsilon$ 是三次角色；它不是原十七处的二次角色
$\kappa_{17}$，也不是曲线 sextic twist 的全部角色。

## 2. 一个显式的固定起始角色

取
$$
\mathfrak q=(3+\omega),\qquad \mathbf N\mathfrak q=7.
$$
约化 $\mu_6\to(\mathcal O_K/\mathfrak q)^\times$ 是同构。
由于 $K$ 的类数为1，每个与 $\mathfrak q$ 互素的分式理想
$\mathfrak a$ 都有唯一生成元 $a_{\mathfrak q}$ 满足
$a_{\mathfrak q}\equiv1\bmod\mathfrak q$。定义
$$
\psi_{\rm b}(\mathfrak a)=a_{\mathfrak q}^{\,3}.
\tag{6}
$$
若 $\varepsilon_{\mathfrak q}(a)\in\mu_6$ 是与
$a\bmod\mathfrak q$ 相同的唯一单位，则
$$
\psi_{\rm b}((a))=a^3\varepsilon_{\mathfrak q}(a)^{-3}.
\tag{7}
$$
生成元的唯一性说明(6)可乘。(7)的有限因子是
$\mathbf F_7^\times$ 上非平凡的二次角色，故导子恰为
$\mathfrak q$。其 infinity type 在 [Ca] 中为 $(-3,0)$。

先置
$$
\chi_{{\rm b},j}=\lambda_j/\psi_{\rm b}.
\tag{8}
$$
这些是有限角色。其导子恰为
$$
(34\delta)\mathfrak q:
$$
在 $2,3,17$ 处来自(3)，在 $\mathfrak q$ 处来自
$\psi_{\rm b}^{-1}$，各处没有导子相消。
三个角色的比值已是 $\epsilon,\epsilon^2$。

接下来只用一个固定辅助塔使三个伴随值同时非零；此时还没有选择目标普通素数 p。

## 3. 同一个十三处塔与 Finis 的有限并例外

固定
$$
\mathfrak l=(4+\omega),\qquad
13=\mathfrak l\bar{\mathfrak l}.
\tag{9}
$$
让 $\alpha$ 遍历只在 $\mathfrak l$ 分歧的 pro-13 有限 ray class
角色；它在 tame 部分平凡，导子为 $\mathfrak l^n$，$n\ge2$。
这样的角色有无限多个。定义
$$
\psi_\alpha=\psi_{\rm b}\alpha,\qquad
\chi_{\alpha,j}=\chi_{{\rm b},j}\alpha^{-1},\qquad
\alpha^-=\alpha^\tau/\alpha .
\tag{10}
$$
因此
$$
\psi_\alpha\chi_{\alpha,j}=\lambda_j,\qquad
\psi_\alpha^\tau\chi_{\alpha,j}
 =\psi_{\rm b}^\tau\chi_{{\rm b},j}\alpha^-.
\tag{11}
$$

这里 $\alpha\mapsto\alpha^-$ 是单射。事实上，若
$\beta=\alpha_1/\alpha_2$ 满足 $\beta^\tau=\beta$，
则它一方面只可能在 $\mathfrak l$ 分歧，另一方面只可能在
$\bar{\mathfrak l}$ 分歧。因此它处处有限未分歧；类数1迫 $\beta=1$。
所以(11)真的给一个无限的伴随角色族，不是有限族的重复写法。

### 3.1 S1–S3 及 root 的完整适用范围

对每个 $\alpha$，$\mathfrak f_{\psi_\alpha}
=\mathfrak q\mathfrak l^n$ 是 cyclic 理想，且其 norm 与
$3\cdot34$ 互素。对满足
$p\nmid 6\cdot34\cdot7\cdot13$ 的普通 p，
[Ca, Lemma 5.1.2 的证明，第一段] 可直接用于每个原 $\lambda_j$：
它支付 $\chi_{\alpha,j}\in
\Sigma_{\rm cc}(34,\mathfrak d_K\mathfrak f_{\psi_\alpha},
\varepsilon_{\theta_{\psi_\alpha}})$，
包括所有有限位的 Rankin 局部 sign $+1$。
这一步只用导子、中心特征及(3)，不使用伴随值非零。

于是整个 Rankin sign 是 $-1$，而原 $\lambda_j$ 的 sign 已是
$-1$。由真实因子分解
$$
L(\theta_{\psi_\alpha}/K,\chi_{\alpha,j},s)
 =L(\lambda_j,s)
  L(\psi_{\rm b}^{\tau}\chi_{{\rm b},j}\alpha^-,s)
$$
得
$$
\boxed{
 w(\psi_{\rm b}^{\tau}\chi_{{\rm b},j}
           \alpha^-\mathbf N^{-2})=+1
 \quad(j=4,10,16).
}
\tag{12}
$$
这不是在伴随 \(L\) 值非零以后反推 root，也没有漏掉某个
$\alpha$ 的 self-duality 条件。

### 3.2 对 Finis 原定理的逐参数匹配

使用 [Fi, Theorem 1.1(1)]，其“tower prime”固定为13，
其用于测量代数值的另一素数固定为19。两者都在 $K$ 分裂，
且19既不是13也不是3。原定理涉及
$K=\mathbf Q(\sqrt{-3})$、估值素数3的例外因此不出现。

定义
$$
\vartheta_{\alpha,j}
 =\psi_{\rm b}^{\tau}\chi_{{\rm b},j}
     \alpha^-\mathbf N^{-2}.
\tag{13}
$$
[Ca] 称其 infinity type 为 $(2,-1)$；
[Fi] 的相反记号称其为 $(-2,1)$。
所以 [Fi] 中的固定整数是 $k=2$。
它满足 [Fi] 的 conjugate-self-dual 条件，root 为(12)的 $+1$，
且其导子恰为
$$
(34\cdot7\cdot13^n)\delta,
\tag{14}
$$
因而除于固定整数 $238$、判别式3与 $13^\infty$ 所给的模数。
所有参数都位于同一个 [Fi] 完整族中。

Finis 的结论使每个 $j$ 的(13)中仅有有限多个角色具有零中心值。
其右端的局部 $\mu_{19}$ 均有限；这里实际上只有 inert 位2、17
可能贡献，而它们的非平凡 finite 部分阶数为3、18，均与19互素，
故该右端为0。我们只使用所得复 \(L\) 值非零，
不把它称为目标普通素数 p 的单位。

由上面的单射，每个 $j$ 在原 $\alpha$ 集中也只有有限多个例外。
把三份例外作有限并后，固定一次 $\alpha$，使
$$
\boxed{
L(\psi_{\rm b}^{\tau}\chi_{{\rm b},j}\alpha^-,2)\ne0
\quad\text{同时对三个 }j\text{ 成立}.
}
\tag{15}
$$
这次选择与目标 p 无关。没有使用固定 p 塔中的渐近非消失去断言
另一个 p 的首层；辅助塔始终是固定的十三处塔。

## 4. 共同 good pair 的实际模数表

从现在起固定上一步的 $\alpha$ 和其导子指数 n，简写
$$
\psi=\psi_{\rm b}\alpha,\qquad
\chi_j=\chi_{{\rm b},j}\alpha^{-1},\qquad
g=\theta_\psi,\qquad M=7\cdot13^n.
\tag{16}
$$

| 对象 | 实际模数或类型 |
|---|---|
| $\psi$ | infinity type $(-3,0)$，$\mathfrak f_\psi=\mathfrak q\mathfrak l^n$ |
| $g$ | weight4，$N_g=3M=21\cdot13^n$ |
| Heegner level 理想 | $\mathfrak N_g=\delta\mathfrak q\mathfrak l^n$，$\mathcal O_K/\mathfrak N_g\simeq\mathbf Z/N_g\mathbf Z$ |
| $\varepsilon_g$ | conductor $N_g$；其7部分为(7)的二次角色，13部分为 $\alpha|_{\mathbf A_\mathbf Q^\times}$，3部分为 $\eta_K$ |
| 三个 $\chi_j$ | $\mathfrak f_{\chi_j}=(34)\mathfrak N_g$，$\varepsilon_{\chi_j}=\varepsilon_g^{-1}$ |
| 原 target $\psi\chi_j=\lambda_j$ | conductor $(34\delta)$，root $-1$ |
| companion $\psi^\tau\chi_j$ | conductor $(34M\delta)$，中心2，root $+1$，中心值非零 |
| BDP 的整数 c | $c=34$，与 $pN_g$ 互素 |

$\varepsilon_g$ 的三个有限部分支撑不交，故其 conductor 确为
$N_g$，从而 $\mathfrak N_{\varepsilon_g}=\mathfrak N_g$；
表中 $\chi_j$ 的 conductor 也正是
$\Sigma_{\rm cc}$ 定义要求的 $(c)\mathfrak N_{\varepsilon_g}$。

全部 good-pair 条件现在是：

- S1：第一行的 infinity type 和 cyclic conductor；
- S2：表中的中心特征、精确导子和第3.1节已付的全部 finite signs；
- S3：$\psi\chi_j=\lambda_j$；
- S4：同一次选择所得的(15)。

这里只有 $r=2$；不调用仅为 $r=1$ 另外规定的 S5–S8。
三个实际有限角色为
$$
\boxed{
\chi_4=\eta_4^{-1}\psi_0^3\psi_{\rm b}^{-1}\alpha^{-1},
\qquad
\chi_{10}=\chi_4\epsilon,\qquad
\chi_{16}=\chi_4\epsilon^2.
}
\tag{17}
$$
因此三对使用同一 $g$，而不是三个随 p 重新选出的 CM 模形式。

以后只须删掉固定几何、系数和分母的有限坏集，并维持原 ordinary
ray。特别是无需随着 p 增大而提高 $N_g$ 或 $\mathfrak f_\chi$。

## 5. 三份 cycle 的几何来源可以先于 p 固定

固定(16)、CM 曲线
$$
A_0=E_0:y^2=x^3+1,\qquad
\omega_{A_0}=dx/(2y),
$$
以及 BDP 构造中同一个有限 CM isogeny orbit、level
$\mathfrak N_g$ 的结构和 conductor $c=34$。
取一个共同有限数域容纳这些结构、三个有限角色与 $g$ 的系数；
其选择只依赖上述固定数据。

BDP generalized Heegner cycles 的构造由该有限 isogeny orbit 的图、
固定的代数投影子以及有限 $\chi_j$ 权重组成。
所以三份实际 cycle $\Delta_j$ 可以在选择 p 以前固定。
保持标准构造中的 norm 权重及有限 level 向量，不把它们替换成
只由(17)猜出的不加权轨道和。
它们处于同一个固定几何来源，例如 weight4 的 Kuga–Sato
三维族与 $A_0^2$ 的标准乘积及其固定投影中；
三个有限角色只改变这一来源的有限对应。

令
$$
\mathcal Z_{j,p}=\operatorname{AJ}_{p}(\Delta_j)
 \in H_f^1(K,V_{g,\chi_j})
\tag{18}
$$
表示 [Ca, Theorem 3.2.1] 的实际 Heegner 类，
包括标准的 descent 和有限角色投影。
这里 p 只进入 étale realization、所选嵌入、ordinary 根与局部
比较映射；cycle 和(16)–(17)不随 p 重选。

其原 target 分量有 weight4 的 Hodge-level-3：
相应 Tate 调整后的 Hodge 指数差仍是3。
所以固定几何来源不把它变成
$H^1$ 型的代数点表示；某个 intermediate Jacobian 的外观也不支付
椭圆点对数或点因子投影。

## 6. 原周期、两种 Euler 与 BDP 配对

固定一个原好 ordinary p，仍记 [Ca] 的 $v=\mathfrak p$、
$\bar v=\bar{\mathfrak p}$，并保持 R804 的
$$
\theta=17^{1/6},\qquad
\Omega_{p,0}=\theta\Omega_p,\qquad
\pi_0\bar\pi_0=p,\quad v_p(\pi_0)=1.
$$
以同一个 $A_0$ 及其原微分选 CM 周期；实际 de Rham 基变换在第7节
明确保留，不通过更改周期把它定为1。

记
$$
\mathcal A_{j,p}=
\left\langle
 \log_{V_{g,\chi_j}}
       (\operatorname{loc}_{\bar v}\mathcal Z_{j,p}),
 \omega'_g\wedge\omega_{A_0}\eta_{A_0}
\right\rangle .
\tag{19}
$$
取 $a_p(g)$ 的普通单位根 $\alpha_p$，另一根记 $\beta_p$，
于是
$$
\alpha_p\beta_p=\varepsilon_g(p)p^3,\qquad
v_p(\alpha_p)=0,\quad v_p(\beta_p)=3.
$$
两个不同的真实 Euler 是
$$
E^{\rm BDP}_{j,p}
=1-a_p(g)\chi_j(\bar v)p^{-2}
  +\varepsilon_g(p)\chi_j(\bar v)^2p^{-1}
=\prod_{\rho\in\{\alpha_p,\beta_p\}}
       \left(1-\rho\chi_j(\bar v)p^{-2}\right),
\tag{20}
$$
$$
E^{\rm Iw}_{j,p}
=\left(1-\frac{\chi_j(v)p}{\alpha_p}\right)
 \left(1-\frac{\chi_j(\bar v)p}{\alpha_p}\right).
\tag{21}
$$
前者 $v_p=-2$，后者属于 $1+p\mathcal O$；两者都非零。
它们不能互换，也不能因第二个是单位就删去第一个。

置
$$
B_{j,p}(T)=\mathscr L_v(g,\chi_j).
$$
按 [Ca, Theorem 3.2.1] 的实际规范，$r=2,c=34,\Gamma(2)=1$ 给
$$
\boxed{B_{j,p}(0)=34^{-2}E^{\rm BDP}_{j,p}\mathcal A_{j,p}.}
\tag{22}
$$
若 $\mathbf Z_j$ 是 R811 使用的 Iwasawa Heegner 类的 target 分量，
则 [Ca, Theorem 3.2.2] 给
$$
\mathbf Z_j(0)=E^{\rm Iw}_{j,p}\mathcal Z^{\rm tar}_{j,p}.
\tag{23}
$$
第二个 companion 分量在 $\bar v$ 的有限局部群为零；
因此(19)只读取(23)中的 target 分量，不是任意删去另一项。

同时定义
$$
C_{j,p}=\mathscr L_v(\lambda_j\mathbf N^{-2}),\qquad
A_{j,p}=\mathscr L_v(\psi^\tau\chi_j\mathbf N^{-2}).
$$
真实两个 Katz 模数分别为 $(34\delta)$ 和 $(34M\delta)$。
共同 good pair 给 $A_{j,p}(0)\ne0$：此点在 companion 的经典插值锥中，
(15)及两个不同赋值的 ordinary 因子排除了例外零。
[Ca, Proposition 2.3.1] 的完整式保持为
$$
B_{j,p}^2=u_{j,p}\,C_{j,p}A_{j,p},
\qquad u_{j,p}\in(\Lambda^{\rm ur})^\times.
\tag{24}
$$
$u_{j,p}$ 是该固定规范实际产生的因子，不在本文定为1。
$A_{j,p}(0)\ne0$ 也不表示它对每个目标 p 都是整数单位。

## 7. 不对可能为零的值取比：原负二矩的准确 AJ 平方

原 canonical 类保持不变：
$$
z_j=\frac1{30}\operatorname{pr}_K
           \operatorname{tw}_{\nu_j}(e_{\eta_j}u_\infty).
\tag{25}
$$
R804 的真实局部标量式是
$$
\ell_{j,p}(\operatorname{loc}_v z_j)
=-34^2 c_j\theta^9\Omega_p^4
   E^{\log}_p I_{j,-2,p}^{\,2},
\qquad
E^{\log}_p=
 \frac{1+\pi_0/\bar\pi_0^2}{1+\bar\pi_0/\pi_0^2}.
\tag{26}
$$
这里 $\ell_{j,p}$ 使用 R804 的
$\sqrt{17}$ Artin 基及原 Tate/CM 基；
$v_p(E^{\log}_p)=2$。$c_j$ 是 R806 固定截面的常数。
(25)的30平滑及(26)的符号、$\theta^9\Omega_p^4$ 均未重新归一。

以第4节这一个共同 good pair 重做 R811 的原比较，得到
$$
\boxed{
\tau z_j=\mathfrak u_{j,p}(0)\,
 B_{j,p}(0)\,\mathbf Z_j(0),
\qquad \mathfrak u_{j,p}(0)\ne0.
}
\tag{27}
$$
$\tau$ 是真实共轭上同调映射，不是对 $\mathbf C_p$ 任意作用。
为使(27)的因子完全可追，其定义仍是 R811 的
$$
\mathfrak u_{j,p}(T)=
 \frac{r_{j,p}(T)\,d_{j,p}^{\,\iota}(T)\,
       (C_{j,p}^{\,\iota}/C_{j,p})(T)}
      {u_{j,p}(T)A_{j,p}(T)}.
\tag{28}
$$
这里 $d_{j,p}=s_{5,j}/30$ 为实际椭圆单位平滑，
$r_{j,p}$ 是两个局部 Coleman 同构之间的唯一比例，
$\iota(T)=-T/(1+T)$。
$C^\iota/C$ 是整个非零 Iwasawa 函数的比例，定义于增广完成环，
不是用 $C(0)$ 作分母。由(24)，$\operatorname{ord}_T C$ 是偶数，
故 $(C^\iota/C)(0)=1$，即使 $C(0)=0$ 仍成立。
这些是增广完成环中的单位；这里“单位”不声称其常数是 p 整数单位。

还须显示原 $\ell_{j,p}$ 与(19)的 de Rham 配对关系。
把 $\ell_{j,p}$ 经 $\tau$ 输送到
$H_f^1(K_{\bar v},T_{\phi_j}\otimes E)$，
记为 $\ell^\tau_{j,p}$。这个空间是一维。
(19)在其 target 分量上的泛函记为 $\mathfrak a_{j,p}$。
两者都是指定 de Rham 基给出的非零泛函。后一个非零性也可直接从 R811 §4 的局部 Coleman 同构在增广点的特殊化读取：其 Bloch–Kato 特殊化乘数是(20)–(21)的非零因子，且 target 有限局部空间是一维。因此这一步不以某个 cycle 值非零为依据。故存在唯一
$$
\mathfrak d_{j,p}\in\mathbf C_p^\times,\qquad
\ell^\tau_{j,p}=\mathfrak d_{j,p}\,\mathfrak a_{j,p}.
\tag{29}
$$
具体可用该 de Rham 直线的任一非零基向量 $\mathbf e$ 定义
$\mathfrak d_{j,p}
=\ell^\tau_{j,p}(\mathbf e)/\mathfrak a_{j,p}(\mathbf e)$，
把两泛函理解为 Bloch–Kato 对数后的直线泛函。
因而(29)不涉及任何可能为零的 cycle 或 \(L\) 值，
并且保留原 $\sqrt{17}$、$\Omega_{p,0}$ 和 $\omega'_g$ 的全部换基。
不宣称 $\mathfrak d_{j,p}$ 是代数数或在不同 p 之间为同一个数。

对(27)施(29)，依次代入(23)、(22)、(26)，得到
$$
-34^2 c_j\theta^9\Omega_p^4E^{\log}_p I_{j,-2,p}^{\,2}
=\mathfrak d_{j,p}\mathfrak u_{j,p}(0)
 E^{\rm Iw}_{j,p}\,34^{-2}E^{\rm BDP}_{j,p}
 \mathcal A_{j,p}^{\,2}.
\tag{30}
$$
等价地，
$$
\boxed{
\mathcal A_{j,p}^{\,2}
=-\frac{34^4c_j\theta^9\Omega_p^4E^{\log}_p}
        {\mathfrak d_{j,p}\mathfrak u_{j,p}(0)
          E^{\rm Iw}_{j,p}E^{\rm BDP}_{j,p}}\,
 I_{j,-2,p}^{\,2}.
}
\tag{31}
$$
每个显示因子都已定义且非零，(31)在两边为零时同样成立。
这就是原三个负二值在同一固定几何来源上的真实 AJ 平方表达；
没有从平方值选择一套未经证明的全局相容符号。

特别地，
$$
\boxed{
I_{j,-2,p}\ne0
\ \Longleftrightarrow\
\mathcal A_{j,p}\ne0
\ \Longleftrightarrow\
z_j\ne0,
}
\tag{32}
$$
最后一个等价使用 R811。这里没有增加一个非零前提。

## 8. 固定来源带来的准确收益及剩余问题

(16)–(18)是一组可以在所有原好 ordinary p 上同时采用的固定对象。
因此研究原三个特殊化类非零时，不必再处理随 p 变化的 good pair、
CM 模形式 level 或有限角色。三条角色只相差(4)的固定三次扭曲。

但是(31)没有给出 $\mathcal A_{j,p}\ne0$。
非零 Iwasawa 函数、固定代数 cycle、甚至另一个实现中的非零，
均不单独排除该指定局部 AJ 配对为零。
本文未证明原 $\lambda_j$ 的解析秩恰1；
即使另付解析秩1，高权的实际 p-adic AJ 比较仍须按适用定理处理。

原 R801／R804 的真实线性行仍是
$$
\lambda^{2N}\Omega_p^2
       \sum_{j=4,10,16}\alpha_{j,N}I_{j,-2,p}.
\tag{33}
$$
(31)不是这个线性和的 AJ 公式：
它保留逐角色的平方、真实基变换和(28)的单位，
未把这些量认作同一组代数线性系数。
所以本篇不调用椭圆点对数的代数线性独立，
不删除 R807／R809 的完整联络或原 W 补域，
也未排除原三个中央导数同时为零。

## 9. 精确来源

- [Ca] F. Castella,
  *Tamagawa number conjecture for CM modular forms and Rankin–Selberg convolutions*，
  [固定 v3 全文](https://arxiv.org/html/2407.11891v3)、
  [固定 v3 PDF](https://arxiv.org/pdf/2407.11891v3)：
  Definition 2.1.2、Proposition 2.3.1、Theorems 3.2.1–3.2.2、
  Definition 5.1.1、Lemma 5.1.2 及其逐参数证明。
- [Fi] T. Finis,
  *Divisibility of anticyclotomic L-functions and theta functions with complex multiplication*，
  Annals of Mathematics 163 (2006), 767–807，
  [期刊全文](https://annals.math.princeton.edu/wp-content/uploads/annals-v163-n3-p02.pdf)，
  Theorem 1.1(1)。本文的 tower prime=13、valuation prime=19，
  type $(-2,1)$、固定导子界及 root 已在第3节逐项匹配。
- R804、R806：三个原 finite 角色、$34\delta$ 椭圆单位来源、
  30平滑、$\sqrt{17}$ Artin 基及(26)。
- R811：同一指定类的全局比较(27)–(28)及 augmentation 完成环中的
  全部真实同构；本篇没有把其结论扩到任意 Selmer 类。

本文无新增数值计算、无素数扫描、无可重算数据文件。
