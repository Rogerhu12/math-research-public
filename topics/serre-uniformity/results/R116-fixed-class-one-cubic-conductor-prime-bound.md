# R116：固定类数一商域与三次导子的全素数界

日期：2026-11-12；会话：serre-uniformity-resume2。

**状态：已证明。** 本篇把实际同一个好约化迹的障碍与已发表的二次有限域 Burgess 界接起来。先证明固定商域、固定三次导子时的有效素数界，再于 §7 展开变化导子的全部常数，证明八个允许的类数一底域上一致有效的 $c>p^{1/1000}$。两者都不要求整 $j$，也不要求先排除 exceptional 分母。

## 1. 定理与适用范围

固定类数一虚二次域 $K\ne\mathbb Q(\sqrt{-3})$，以及正整数 $c$。设实际椭圆曲线 $E/\mathbb Q$ 和素数 $p>37$ 满足本课题的完整非分裂正规化子设置，商域为 $K$，且
$$
\bar\rho_{E,p}(I_p)=C^3.
$$
记 R66 的实际三阶环类角色为 $\eta$，其准确导子为 $c\mathcal O_K$。

**定理 116.1。** 存在仅依赖 $(K,c)$ 的有效常数 $C_{K,c}$，使每个上述实际曲线均满足
$$
\boxed{p\le C_{K,c}.} \tag{116.1}
$$
这里不附加 $j(E)\in\mathbb Z$、半稳定性、固定导子支撑或有限条二次扭曲的假设。曲线的新四阶惯性素数可以变化。

九个类数一虚二次域中排去 $\mathbb Q(\sqrt{-3})$ 后只剩有限个域，所以固定 $c$ 时亦可取对这些域统一的 $C(c)$。特别，对 R90/R97 的五个组合
$$
(D,c)=(11,2),(19,2),(43,2),(67,2),(163,2)
$$
可取同一个绝对常数。故环类数三、类数一底域的实际异常序列若满足 $p\to\infty$，最终只能落在 $K=\mathbb Q(\sqrt{-3})$、$c=6$ 或 $9$。

常数在证明中有效，但本篇不计算一个实用数值。$c$ 随曲线变化时，(116.1) 没有给绝对常数；$K=\mathbb Q(\sqrt{-3})$ 也不能套用下面的非零范数论证。

## 2. 实际差角色及准确的变化模数

为固定的 $K$ 选一条在 $\mathbb Q$ 上定义、以 $\mathcal O_K$ 为复乘整环的曲线 $A$。类数一保证这样的有理 CM 曲线存在。它的有限坏素数只依赖 $K$；把这些素数以及 $2,3,D,c$ 的素因子收入一个固定有限集 $S$。若 $p\in S$，将它吸收到常数即可；以下 $p\notin S$。

令 $\lambda$ 为实际 $E$ 的 Cartan 特征，$\psi$ 为 $A$ 的一个 CM 特征。R21 的精确比较允许选择同一取向，使
$$
\nu=\lambda/\psi,\qquad
\nu^{12}=1,\quad \nu^{p+1}=1,\quad \nu^{\mathsf c}=\nu^{-1},
\tag{116.2}
$$
其中 $\mathsf c$ 表示复共轭。定义
$$\chi=\nu^4.\tag{116.3}$$
把残余三次单位根按任一固定识别提升到复数三次单位根，从此把 $\chi$ 视为复值有限 Hecke 角色；是否为一及所有整数同余均不受这个识别影响。

R66 给
$$p\equiv2,5\pmod9,\qquad u=(p^2-1)/3,\qquad3\nmid u,\quad4\mid u.$$
取 $v\in\{1,2\}$ 满足 $uv\equiv1\pmod3$。由于 $4\equiv1\pmod3$，亦有 $(u/4)v\equiv1\pmod3$。由 $\eta=\lambda^u$，准确得到
$$
\boxed{\chi=\eta^v\psi^{-uv}.} \tag{116.4}
$$
这里没有把 R66 的三次商角色 $\eta$ 与差角色 $\chi$ 混为一谈。

在 $p$ 处，$A$ 好超奇异且 $\psi$ 的惯性为一个第二层基本特征，所以 $\psi^u$ 的惯性恰为阶三。$\eta$ 在 $p$ 不分歧。因此 $\chi$ 在 $p$ 有非平凡温和三次分量，准确导子为 $p\mathcal O_K$。

在 $p$ 之外，$A$ 的 CM 惯性取值于 $\mathcal O_K^\times$：所有 CM 端同态已在 $K$ 定义，有限惯性在好约化纤维上与其交换；该二次域在自同态代数中的中心化子仍为自身，而所取 CM 序是极大序。因为 $K\ne\mathbb Q(\sqrt{-3})$ 且 $h_K=1$，这个单位群的阶为二或四，故 $\psi^u$ 在 $p$ 外不分歧。由 (116.4)，$\chi$ 在 $p$ 外的准确导子为 $c\mathcal O_K$。因此
$$
\boxed{\mathfrak f(\chi)=cp\mathcal O_K,\qquad
\chi^{\mathsf c}=\chi^{-1},\qquad\chi^3=1\ne\chi.}
\tag{116.5}
$$

类数一使每个整素理想有生成元。在 $S$ 外的主理想 $(\alpha)$ 上，CM 主理想公式给 $\psi((\alpha))=\epsilon_\alpha\alpha$ 的模 $p$ 约化，其中 $\epsilon_\alpha\in\mathcal O_K^\times$。取 $u$ 次幂杀死这个单位。因此 (116.4) 写成
$$
\boxed{\chi((\alpha))=\rho_c(\alpha\bmod c)\,
\vartheta_p(\alpha\bmod p),}\tag{116.6}
$$
其中 $\rho_c$ 是模 $c$ 的固定有限角色权，$\vartheta_p$ 是 $\mathbb F_{p^2}^\times$ 上非平凡三次角色（等于 $\alpha\mapsto\alpha^{-uv}$ 后作复值识别）。$\rho_c$ 可以随实际 $\eta$ 取值，但模数 $c$ 固定，且每个权的绝对值不超过一。下面的估计对所有这些权一致。

在理想与 $S$ 互素的求和中，可选择一个固定整数 $m$，使 $c\mid m$ 且 $m$ 含 $S$ 中全部素因子；逐个 $\alpha\bmod m$ 分班后，(116.6) 的第一个因子和互素条件都是常数。

## 3. 非平凡小分裂素数的真实迹障碍

**引理 116.2。** 若有理素数 $q\notin S$ 在 $K$ 分裂，$q<p$，并且对一个 $\mathfrak q\mid q$ 有 $\chi(\mathfrak q)\ne1$，则
$$\boxed{p<256q^2.}\tag{116.7}$$

**证明。** 因 $h_K=1$，取 $(\alpha)=\mathfrak q$，$N_{K/\mathbb Q}\alpha=q$。在 $q$ 处实际残余局部像落在 Cartan 中。若 $E$ 潜在乘法，R63 §3.1 会给 $q\equiv1\pmod p$，与 $q<p$ 矛盾。故它潜在好约化。

R63 §§3.2–3.4 构造一个真实的全分歧循环好约化扩张，剩余域仍为 $\mathbb F_q$；其所选 Frobenius 给实际整数
$$a\in\mathbb Z,\qquad |a|<2\sqrt q.$$
记该 Frobenius 的 $\lambda$ 特征值为 $\beta$。$A$ 在 $q$ 好约化，因此 $\psi$ 不受 Frobenius 提升的改变影响，其值为某个单位乘 $\alpha$。由 (116.2)，
$$
\beta=\zeta\alpha\pmod{\mathfrak P},\qquad
\zeta\in\mu_{12},\qquad\zeta^4=\chi(\mathfrak q)\ne1.
\tag{116.8}
$$
这里选取 $K(\zeta_{12})$ 上方的一个 $p$ 素理想使约化相容。$\mathcal O_K^\times$ 的阶整除四，所以将 CM 单位并入 $\zeta$ 不改变最后的四次幂。$\chi$ 在 $q$ 不分歧，故最后一个值也不依赖所用 Frobenius 提升。

同一个实际整数迹满足
$$a\equiv t:=\zeta\alpha+\zeta^{-1}\bar\alpha\pmod{\mathfrak P}.\tag{116.9}$$
这是因为行列式为 $q$，所以第二个特征值是 $q/\beta$。没有分别给模三条件和模 $p$ 条件选择不同的好约化曲线。

断言 $t\notin\mathbb Q$。否则 $t$ 为有理代数整数，$\beta_0=\zeta\alpha$ 是 $T^2-tT+q$ 的根。它不可能为实数：若为实，则 $\beta_0^{12}=q^6=\alpha^{12}$，而主理想 $\mathfrak q^{12}$ 与其共轭不同，矛盾。故 $F=\mathbb Q(\beta_0)$ 为虚二次域。又 $\alpha^{12}$ 非实，生成 $K$，且属于 $F$；于是 $F=K$。这迫使 $\zeta=\beta_0/\alpha\in K$，但 $K$ 中单位的阶仅为二或四，与 $\zeta^4\ne1$ 矛盾。

设 $L^+=K(\zeta_{12})^+$ 为最大实子域，其次数 $d\le4$。$t-a$ 是 $L^+$ 中非零代数整数；(116.9) 使其有理范数被 $p$ 整除。每个实嵌入下 $|t|\le2\sqrt q$，所以
$$
p\le\bigl|N_{L^+/\mathbb Q}(t-a)\bigr|
<(4\sqrt q)^d\le256q^2.
$$
证毕。

这个论证容许 $q$ 是实际 $E$ 的四阶惯性素数；所需不分歧性仅用于 $\chi=\nu^4$ 和固定参考 $A$。因而变化的四次扭曲支撑没有被隐藏进固定集合 $S$。

## 4. 从有限域短箱到整理想和

以下使用 Chang 的已发表 Theorem 5：给定 $\varepsilon>0$，存在 $\delta>0$，使非平凡乘法角色 $\vartheta$ 和任意 $\omega\in\mathbb F_{p^2}\setminus\mathbb F_p$ 在边长 $p^{1/4+\varepsilon}$ 的两个整数区间上满足
$$
\left|\sum_{x\in I,y\in J}\vartheta(x+\omega y)\right|
\le p^{-\delta}|I||J|
\tag{116.10}
$$
（$p$ 充分大）。估计对 $\omega$ 和区间的位置一致。准确来源及页码见末节。

置
$$X=p^{51/100},\qquad H=\lfloor p^{101/400}\rfloor.$$
于是 $H=p^{1/4+1/400+o(1)}$，而 $\sqrt X=p^{1/4+1/200}$；对 (116.10) 可固定取稍小的 $\varepsilon=1/800$。定义
$$
S_\chi(X)=\sum_{\substack{\mathfrak a\subset\mathcal O_K\\
N\mathfrak a\le X,\ (\mathfrak a,S)=1}}\chi(\mathfrak a).
$$
由于 $X<p$，特别不包含 $p\mathcal O_K$ 的倍数。

**引理 116.3。** 当 $p\to\infty$ 时，对全部实际角色一致地有
$$\boxed{S_\chi(X)=o_{K,c}(X),}\tag{116.11}$$
且误差有效。

**证明。** 写 $\mathcal O_K=\mathbb Z+\mathbb Z\omega$，$w_K=|\mathcal O_K^\times|$。每个整理想有恰好 $w_K$ 个生成元，而每个生成元的复绝对值平方等于理想范数。因此理想和等于生成元格点和除以 $w_K$。

按照 (116.6) 将生成元逐个模固定 $m$ 分班。每班可写
$$\alpha=\alpha_0+m(x+y\omega).$$
范数条件是 $(x,y)$ 平面中一个固定形状、直径 $O_{K,m}(\sqrt X)$ 的椭圆区域。角色的可变部分为
$$\vartheta_p(m)\,
\vartheta_p\bigl(x+y\omega+\alpha_0/m\bigr).$$
模 $p$ 时 $\alpha_0/m$ 仍有唯一的两个坐标，所以每个边长 $H$ 的轴平行小方框都由 (116.10) 控制。可把方框细分成边长 $\lfloor p^{1/4+1/800}\rfloor$ 的方框；边缘条带的相对大小趋于零。区间的任意平移由该定理的均匀性覆盖。

完全位于椭圆内部的方框总面积 $O_{K,m}(X)$，其角色和为 $o_{K,m}(X)$。遇到边界的方框中格点总数为
$$O_{K,m}(H\sqrt X+H^2)=o_{K,m}(X),$$
因为 $H/\sqrt X=p^{-1/400+o(1)}$。模 $m$ 的班数固定，权的绝对值至多一。合并即得 (116.11)。所有格点边界估计和 (116.10) 的阈值均有效。$\square$

注意这里只对 $\mathbb F_{p^2}$ 的角色调用 Burgess；没有直接假定一个未核准的、任意 Hecke 导子都适用的数域 Burgess 公式。固定的模 $c$ 部分已显式分班。

## 5. 大素因子的计数：把 $X$ 降到 $\sqrt p/17$

令
$$A_S(T)=\#\{\mathfrak a\subset\mathcal O_K:N\mathfrak a\le T,
(\mathfrak a,S)=1\}.$$
类数一的复格点计数及固定有限容斥给
$$
A_S(T)=\kappa_ST+O_{K,S}(\sqrt T+1),\qquad
\kappa_S=\frac{2\pi}{w_K\sqrt D}
\prod_{\mathfrak q\mid S}\left(1-\frac1{N\mathfrak q}\right)>0.
\tag{116.12}
$$
各容斥项的理想是主理想，直接把范数范围改为 $T/N\mathfrak d$ 即可；不需要对 $K$ 的素理想定理或 Siegel 零作任何假设。

先给所需的初等素数估计。由二项式系数的整除性，
$$\theta(2^n)-\theta(2^{n-1})\le2^n\log2.$$
求和并包住任意 $t$，得 $\theta(t)\le4(\log2)t$。将不超过 $\sqrt t$ 的素数单独估计，得到
$$\pi(t)\le\sqrt t+\frac{2\theta(t)}{\log t}
\le\frac{8t}{\log t}\qquad(t\ge2),\tag{116.13}$$
其中用了 $\log t\le\sqrt t$。分部求和因而给
$$
\sum_{Y<q\le X\atop q\ {m prime}}\frac1q
\le8\log\frac{\log X}{\log Y}+O\left(\frac1{\log X}\right),
\tag{116.14}
$$
以及
$$\sum_{q\le X\atop q\ {m prime}}q^{-1/2}
\ll\frac{\sqrt X}{\log X}.\tag{116.15}$$
后式也由 (116.13) 分部求和，或将 $q\le\sqrt X$ 与其余区间分开得到。所有常数都是绝对有效常数。

置
$$Y=\sqrt p/17.$$
引理 116.2 使每个 $S$ 外、范数 $\le Y$ 的分裂素理想都满足 $\chi(\mathfrak q)=1$：否则
$$p<256q^2\le(256/289)p,$$
矛盾。惰性素理想被复共轭固定，其 $\chi$ 值既等于自己的逆又是三次单位根，所以也恒为一。分歧素数已包含在 $S$。

因此，若 $N\mathfrak a\le X$、$(\mathfrak a,S)=1$ 且 $\chi(\mathfrak a)\ne1$，则 $\mathfrak a$ 至少含一个 $S$ 外的分裂素理想因子，其范数为有理素数 $q>Y$。记这样的坏理想数为 $B(X)$。同一个坏理想可以被重复计数，故安全的上界为
$$
\begin{aligned}
B(X)&\le2\sum_{Y<q\le X\atop q\ {\rm prime}}A_S(X/q)\\
&\le2\kappa_SX\sum_{Y<q\le X}\frac1q
+O_{K,S}\left(\sqrt X\sum_{q\le X}q^{-1/2}+\pi(X)\right).
\end{aligned}\tag{116.16}
$$
这里将实际分裂素数放宽到全部有理素数，每个至多两支，因而无需假设分裂素数的密度。由 (116.12)–(116.15)，
$$
\limsup_{p\to\infty}\frac{B(X)}{A_S(X)}
\le16\log\frac{51}{50}<\frac23.
\tag{116.17}
$$
确切地，$\log X/\log Y\to(51/100)/(1/2)=51/50$；而 $\log(51/50)<1/50$，所以右端甚至小于 $8/25$。这个严格余量足以吸收所有有效误差。

对复三次单位根，非一的两个值实部都等于 $-1/2$，因此
$$
\operatorname{Re}S_\chi(X)
=A_S(X)-\frac32B(X).
\tag{116.18}
$$
(116.17) 使充分大的 $p$ 满足
$$\operatorname{Re}S_\chi(X)>\frac12A_S(X)\gg_{K,S}X,$$
与引理 116.3 矛盾。这样对每个固定 $(K,c)$ 排除了全部充分大的 $p$，证明定理 116.1。

## 6. 有效性与真正剩下的情形

证明的阈值依赖于固定 CM 参考、有限集合 $S$、模 $c$ 分班、一个显式椭圆格点边界，以及 Chang Theorem 5 的有效短箱估计。没有使用 Siegel 的无效类数下界，也没有调用仅在 GRH 下的最小素理想界。因此可以有效选择 $C_{K,c}$；本篇不优化它或给出数值表。

有效性也可直接从原文证明读取：其参数取 $\kappa=1/k$、$\rho>1/4+2/k$，并允许任意 $\delta<1/(4k^2)$。对边长 $\lfloor p^{1/4+1/800}\rfloor$，充分大时可用稍小的阈值指数 $\rho=1/4+1/1000$，取 $k=3200$ 和 $\delta=1/(8\cdot3200^2)$；这样也保留了取整所需的严格余量。原文剩余的 $\exp(C\log p/\log\log p)$ 因子及本文所有格点、素数误差都能被一个有效阈值吸收。这不依赖于将“充分大”三个字本身解释为有效。

新输入关闭了固定 $K\ne\mathbb Q(\sqrt{-3})$、固定三次导子下“有限迹窗口可能一直漏掉更大的 $p$”这一量词缺口。固定窗口确实不能完成这个任务；上面的辅助素数范围随 $p$ 增长，短箱抵消与大素因子计数迫使其中出现非平凡的实际角色值。

当 $K=\mathbb Q(\sqrt{-3})$，$\zeta\alpha$ 可以仍属于 $K$，(116.9) 的 $t$ 可以是整数，非零范数论证确实失效。变化 $c$ 的量词不能只从固定模数证明推出；下一节另行控制全部依赖。一般变化商域、快速增长的导子和完整 Cartan 惯性仍在主问题中保留。

## 7. 一致加强：不排除 exceptional 的导子幂次下界

下面把所有依赖于 $c$ 的常数展开，并改变大素因子计数的求和顺序。这一步允许导子在一个幂次范围内变化，不能仅由固定 $c$ 的量词推出。

**定理 116.4。** 存在有效绝对常数 $P_0$，使每个实际小惯性曲线在
$$h_K=1,\qquad K\ne\mathbb Q(\sqrt{-3}),\qquad p>P_0$$
时都满足
$$\boxed{c>p^{1/1000},\qquad
h(\mathcal O_c)>\frac{p^{1/2000}}{3\sqrt2}.}\tag{116.19}$$
常数同时适用于全部八个允许的类数一域；不要求整 $j$、非 exceptional 分母或预先的中心值非消失。特别，$c$ 和 $h(\mathcal O_c)$ 都最终超过任意固定的 $\log p$ 幂，阈值有效。

### 7.1 互素理想计数的全部导子依赖

固定 $K$ 后，令 $S_A$ 为 §2 中只由 CM 参考及 $2,3,D$ 决定的素数集，置
$$S=S_A\cup\{q:q\mid c\},\qquad
m=\operatorname{lcm}\left(c,\prod_{q\in S_A}q\right)\le C_Kc.$$
有限集 $S_A$ 中可能的 $p$ 先收入有效阈值；实际 $p\nmid c$ 已由 R66 保证。
取 $S$ 上方全部不同素理想的乘积 $\mathfrak s$，记
$$J_S=2^{\omega(\mathfrak s)},\qquad
E_S=\prod_{\mathfrak q\mid\mathfrak s}
\left(1+(N\mathfrak q)^{-1/2}\right)\le J_S.$$
每个有理素数上方至多两支，所以
$$J_S\le C_K4^{\omega(c)},\qquad
\kappa_S^{-1}\le C_K\prod_{q\mid c}(1-1/q)^{-2}.$$
逐个将充分大的 $q$ 的局部因子界为 $q^\epsilon$，把有限个小素数收入常数，给出有效估计
$$\boxed{J_S,\ \kappa_S^{-1}\ll_{K,\epsilon}c^\epsilon
\quad(\epsilon>0).}\tag{116.20}$$
特别，$J_S,E_S,\kappa_S^{-1}\ll_Kc$。这里可直接用
$4^{\omega(c)}\le(8/3)c$ 及 $\prod_{q\mid c}(1-1/q)^{-2}\le2c$。

令 $\kappa_K=2\pi/(w_K\sqrt D)$。未加互素条件的理想数满足
$$A_K(t)=\kappa_Kt+O_K(\sqrt t+1).$$
对 $\mathfrak d\mid\mathfrak s$ 逐项准确容斥，得到
$$\boxed{A_S(t)=\kappa_St+O_K(E_S\sqrt t+J_S),\qquad
\kappa_S=\kappa_K\prod_{\mathfrak q\mid\mathfrak s}
(1-(N\mathfrak q)^{-1}).}\tag{116.21}$$
此式对所有 $t>0$ 成立；小于一的自变量由 $O_K(1)$ 覆盖。

### 7.2 变化支集的加权理想上界

定义
$$H_S(T)=\sum_{N\mathfrak b\le T\atop(\mathfrak b,\mathfrak s)=1}
\frac1{N\mathfrak b},\qquad
L_S=\sum_{\mathfrak q\mid\mathfrak s}
\frac{\log N\mathfrak q}{N\mathfrak q-1}.$$
所需的有效统一界为
$$\boxed{L_S\ll_K1+\log\log(c+3).}\tag{116.22}$$
确实，每个 $q\mid c$ 的贡献不超过 $2\log q/(q-1)$。在
$V=\max(2,\log(c+3))$ 处切分：$q\le V$ 的总和由 §5 的
$\vartheta(t)\le4(\log2)t$ 和分部求和界为 $O(1+\log V)$；
$q>V$ 的总和不超过 $4\log c/V=O(1)$。固定 $S_A$ 只贡献固定常数。

对 $0<s\le1/2$，理想 Dirichlet 级数的绝对收敛 Euler 乘积给
$$\zeta_{K,S}(1+s)=\zeta_K(1+s)
\prod_{\mathfrak q\mid\mathfrak s}
(1-(N\mathfrak q)^{-1-s}).$$
从 $A_K(t)$ 的上述格点界分部积分直接得
$$\zeta_K(1+s)=\frac{\kappa_K}{s}+O_K(1).$$
不需要调用一个对变化域有效性不明的 Laurent 常数。对每个 $n=N\mathfrak q$，
$$\log\frac{1-n^{-1-s}}{1-n^{-1}}
\le\frac{1-n^{-s}}{n-1}\le\frac{s\log n}{n-1}.$$
令 $s=1/\log T$，正项 Rankin 上界因此给
$$\boxed{H_S(T)\le T^s\zeta_{K,S}(1+s)
\le e\kappa_S\log T\,
\bigl(1+O_K(1/\log T)\bigr)
\exp(L_S/\log T).}\tag{116.23}$$
这里只上界所有理想的正权和，不对角色值使用正性。

### 7.3 坏理想的比例仍与抵消不相容

反设 $c\le p^{1/1000}$。这一节改取
$$X=p^{101/200},\qquad Y=\frac{\sqrt p}{17},\qquad
T=X/Y=17p^{1/200}.$$
由 (116.21) 和 $J_S,E_S,\kappa_S^{-1}\ll_Kc$，一致有效地有
$$A_S(X)=\kappa_SX(1+o_K(1)).\tag{116.24}$$
例如相对误差不超过 $O_K(c^2X^{-1/2}+c^2X^{-1})$，在本范围趋于零。

由 §3 的 $p<256q^2$，每个 $q\le Y$、$q\notin S$ 的分裂素理想上的
$\chi$ 都等于一；惰性素理想上的值也为一。故每个被 $B(X)$ 计数的坏理想
$\mathfrak a$ 必含一个范数为分裂素数 $q>Y$ 的素理想 $\mathfrak q$。
写 $\mathfrak a=\mathfrak q\mathfrak b$，就有 $N\mathfrak b\le T$。
允许重复计数并忽略 $q$ 的分裂及互素限制，得到
$$B(X)\le2\sum_{N\mathfrak b\le T\atop(\mathfrak b,\mathfrak s)=1}
\pi\bigl(X/N\mathfrak b\bigr)
\le\frac{16X}{\log Y}H_S(T).\tag{116.25}$$
第二步用 §5 已自证的 $\pi(t)\le8t/\log t$；每个自变量至少为 $Y$。

在 $c\le p^{1/1000}$ 上，(116.22) 给
$L_S/\log T=O_K(\log\log p/\log p)=o_K(1)$。结合
(116.23)–(116.25)，一致有效地得到
$$\limsup_{p\to\infty}\frac{B(X)}{A_S(X)}
\le16e\lim_{p\to\infty}\frac{\log T}{\log Y}
=\frac{16e}{100}<\frac12.\tag{116.26}$$
末个严格不等式只需 $e<3$。所以充分大的 $p$ 满足
$$\operatorname{Re}S_\chi(X)
=A_S(X)-\frac32B(X)>\frac14A_S(X).\tag{116.27}$$

### 7.4 全部剩余类上的短箱抵消

设 $h_0=\lfloor p^{1/4+1/800}\rfloor$、$R=\sqrt X$。在每个模 $m$ 的班上，
以生成元写成 $\alpha=\alpha_0+m(x+y\omega)$，并在 $(x,y)$ 坐标中按边长
$h_0$ 分框。模 $m$ 的有限角色及互素指示权在每班恒定，绝对值不超过一。
全部 $m^2$ 个班中，完整框内的格点总数为 $O_K(X)$；边界框格点总数为
$$O_K(mh_0R+m^2h_0^2).$$
这是每班椭圆周长 $O_K(R/m)$ 的框边界估计乘以班数，已保留全部模数依赖。
模 $p$ 时 $m$ 可逆，故 §6 的 Chang 短箱界对这些平移和同一非平凡三次角色统一适用，给
$$|S_\chi(X)|\ll_K Xp^{-\delta}
+mh_0\sqrt X+m^2h_0^2,\qquad
\delta=\frac1{8\cdot3200^2}.\tag{116.28}$$
完整框的贡献没有额外的 $m^2$ 因子，因为它们的格点总数已是 $O_K(X)$。

现在
$$\frac{mh_0}{\sqrt X}\ll_K
p^{1/1000+1/4+1/800-101/400}=p^{-1/4000}.$$
在 (116.20) 中取固定 $\epsilon=500\delta$，则
$\kappa_S^{-1}\ll_K p^{\delta/2}$。所以 (116.28) 除以 $\kappa_SX$ 后，
三个上界分别为
$$O_K(p^{-\delta/2}),\qquad
O_K(p^{-1/4000+\delta/2}),\qquad
O_K(p^{-1/2000+\delta/2}),$$
均有效趋于零。这与 (116.24)、(116.27) 矛盾，证明 $c>p^{1/1000}$。

最后，环类数公式及 $\varphi(c)^2\ge c/2$ 给
$$h(\mathcal O_c)\ge\frac{\varphi(c)}3\ge\frac{\sqrt c}{3\sqrt2},$$
得到 (116.19) 的第二个不等式。对八个底域取有效阈值的有限最大值，完成证明。

本节覆盖 exceptional 情形，仍然只给导子下界。R84 在非 exceptional 分母分支的近线性下界更强，其假设也不同；两个结论都没有给变化导子上界或 Serre 一致性的绝对常数。

## 来源与可核查位置

1. M.-C. Chang, **Burgess Inequality in $\mathbb F_{p^2}$**, *Geometric and Functional Analysis* **19** (2009), 1001–1016，DOI [10.1007/s00039-009-0031-5](https://doi.org/10.1007/s00039-009-0031-5)，[期刊原文 PDF](https://link.springer.com/content/pdf/10.1007/s00039-009-0031-5.pdf)。Theorem 5 在刊页1001及1007，证明在1007–1008；统一控制 $\omega$ 和平移区间。本文使用这一已发表结果，固定剩余类、椭圆边界和理想因子计数在上文另行证明。
2. [R21](R21-twelfth-power-signature-and-cm-twists.md) §6：类数一的准确 CM 差角色；[R63](R63-all-prime-classes-and-quotient-discriminant-growth.md) §3：真实总分歧好约化扩张及同一个 $q$ 迹；[R66](R66-cubic-conductor-nonvanishing-and-tate-primes.md)：实际小惯性、准确三次导子和模九条件。
3. [R97](R97-level41-class-three-exclusion-by-certified-thue-equations.md) §2–3：类数一三次角色与四次幂角色的有限精确比较；本篇改变的是全素数量词，不替换该处已经完成的小层有限计算。
