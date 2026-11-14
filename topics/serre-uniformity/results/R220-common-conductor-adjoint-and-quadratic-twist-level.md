# R220：共同导子的伴随表示、二次扭曲导子与实际 $j$ 支撑

日期：2026-11-13。

**状态：已证明。** 本文把 R214–R217 中变化的 $M^*=D(bc)^2$ 与同一条实际椭圆曲线的导子相连：其有限伴随 Artin 表示的导子准确等于 $p^2D M^*$；一个全局二次扭曲在 $q\ge5$ 的导子准确由 $D,b,c$ 和 Tate 分母支撑给出。因而共同导子增长可明确改写成二次扭曲后椭圆导子的增长问题，不能靠忽略新出现的四阶惯性素数取得上界。

## 1. 设置

保留实际小惯性分支：

$$\rho=\bar\rho_{E,p}:G_{\mathbb Q}\twoheadrightarrow N(C),\qquad
p>37,\quad\rho(I_p)=C^3,\quad p\equiv2,5\pmod9.$$

$K$ 为正规化子二次商域，$D=|D_K|$，$c$ 为实际三次角色的环类导子，$b$ 为 R214 的共同二阶惯性导子。令

$$a^*=bc,\qquad M^*=D(bc)^2,$$

$$R=\prod_{\substack{q\ge5,\ q\ne p\\q\mid Dbc}}q,\qquad
T=\prod_{v_q(j(E))<0}q.$$

R2、R66 已知 $2,3,p$ 不进入 $T$；$T$ 与 $pDbc$ 互素。$D,b,c$ 在 $q\ge5,q\ne p$ 的支撑两两不交且各指数为一，所以 $R=(Dbc)^{(6)}$；这里 $x^{(6)}$ 指去掉二、三因子的正整数部分。

## 2. 全部素数上的准确 Artin 导子恒等式

**定理 220.1。** 存在自然的三维有限像特征零 Artin 表示 $\mathcal A_\rho$，其模 $p$ 约化为 $\operatorname{Ad}^0\rho$，且

$$\boxed{N(\mathcal A_\rho)=p^2D^2b^2c^2=p^2D M^*.} \tag{220.1}$$

**证明。** 取 $C=\mathbb F_{p^2}^{\times}$ 到复单位根的一个忠实字符 $\gamma$，与选定的模 $p$ 剩余嵌入相容。有限群表示

$$\widetilde\rho=\operatorname{Ind}_{C}^{N(C)}\gamma$$

是二维复表示；模 $p$ 后是自然二维表示的标量扩张。令

$$\mathcal A_\rho=\operatorname{Ad}^0(\widetilde\rho)\circ\rho.$$

把对角无迹矩阵与两个非对角矩阵分别看成子空间，直接得到

$$\mathcal A_\rho\simeq\varepsilon_K\oplus
\operatorname{Ind}_{G_K}^{G_{\mathbb Q}}\Phi,\qquad
\Phi=(\gamma^{1-p})\circ\lambda. \tag{220.2}$$

其中 $\varepsilon_K$ 是二次商角色。$\gamma^{1-p}$ 在标量上平凡，在 $C/Z$ 上阶恰为 $p+1$，故是原始 projective 字符。R214 的 transfer 使 $\Phi$ 在有理 idèle 上平凡；它同时看见全部三次和二阶 projective 惯性，因此其准确 prime-to-$p$ 环类导子为 $bc$。$p$ 处惯性阶为 $(p+1)/3>2$，角色 tame 且非平凡，Hecke 理想导子指数一。故

$$\mathrm N_{K/\mathbb Q}\mathfrak f(\Phi)=p^2b^2c^2.$$

Artin 导子对直和相乘，且诱导公式给

$$N(\operatorname{Ind}_K^{\mathbb Q}\Phi)
=D\,\mathrm N\mathfrak f(\Phi)=Dp^2b^2c^2.$$

再乘 $N(\varepsilon_K)=D$，得到 (220.1)。

关于约化：$p\nmid|N(C)|=2(p^2-1)$，可取稳定整格并以半单方式约化。$\widetilde\rho$ 限制到 $C$ 的两个字符为 $\gamma,\gamma^p$，约化后正是自然二维表示的两个 Cartan 特征值；外陪集交换二者。其伴随约化因此是 $\operatorname{Ad}^0\rho$。这里是有限像特征零提升的 Artin 导子，不把它误认成所有素数上的 $\ell$ 进 $\operatorname{Ad}^0T_\ell(E)$ 导子：Tate 分母处后者仍有单幺幂分歧，而前者由 R2 已不分歧。证毕。

## 3. 三类互斥的潜在好约化支撑

**引理 220.2。** 设 $q\ge5,q\ne p$ 且 $v_q(j(E))\ge0$。真实有限惯性循环，阶属于 $1,2,3,4,6$。其 projective 像与导子支撑准确对应如下：

| projective 惯性 | 真实惯性阶 | $D,b,c$ 中出现的因子 |
|---|---|---|
| 平凡 | $1$ 或 $2$ | 均不出现 |
| 三阶 | $3$ 或 $6$ | 仅 $q\mid c$ |
| 二阶且在 Cartan 内 | $4$ | 仅 $q\mid b$ |
| 二阶且在 Cartan 外 | $4$ | 仅 $q\mid D$ |

**证明。** 剩余特征至少五，潜在好约化惯性温和循环，所列真实阶为标准椭圆自同构清单，且模 $p$ 约化忠实。阶二元只能是标量 $-I$。阶三 projective 元在指数二 Cartan 内；因 $v_3(p+1)=1$，实际三次字符在此子群忠实，故且仅故贡献 $c$。阶四惯性若落在 Cartan 内，其 projective 像是唯一二阶元，恰被 R214 的最高 $2$-primary 字符检测，所以贡献 $b$。若不落在 Cartan 内，二次商分歧，贡献 $D$；限制到 $G_K$ 后只剩标量平方，故不贡献 $b$，也不贡献 $c$。各情形互斥。证毕。

这也直接证明 $R$ 是全部不能被二次扭曲消去的、$p$ 外且大于三的潜在好约化坏素数积。它不是一个可以从已知三次导子 $c$ 删除的有限固定集合。

## 4. 一个全局二次扭曲的准确奇导子

**定理 220.3。** 存在定义于 $\mathbb Q$ 的二次扭曲 $E_0$，与 $E$ 有同一 $j$、同一 $D,b,c$，且

$$\boxed{N(E_0)=2^u3^v p^2R^2T,\qquad0\le u\le8,\quad0\le v\le5.} \tag{220.3}$$

这里使用一个全局二次扭曲，不只是分别给每个局部域选扭曲。对任意二次扭曲 $E'$ 都有

$$p^2R^2T\mid N(E')^{(6)}.$$ 

**证明。** 在 $q\ge5,q\ne p$ 分三类。

若 $q\mid R$，引理 220.2 给非平凡 projective 惯性。任何二次扭曲只乘标量，所以都仍为 additive、潜在好约化。温和 conductor 指数恰为二。

若 $q\mid T$，曲线潜在乘法。若已为乘法约化，不需扭曲；若为 $I_n^*$，选择在 $q$ 分歧的二次扭曲使其成为乘法约化。所得 conductor 指数恰为一；任何二次扭曲的最小可能指数也为一。

若 $q\nmid RT$，有限惯性只有标量。好约化时不扭曲；若不是好约化，则为 $I_0^*$，其非平凡二次惯性由一个分歧二次角色消去，扭曲后好约化。对奇 $q$，两个分歧二次局部角色只差不分歧角色，后者不改变 conductor，所以这里只需指定全局扭曲因子的 $q$ 进赋值奇偶性。

取平方自由整数 $d$，恰为上述需要消去 $I_n^*$ 或 $I_0^*$ 的 $q\ge5,q\ne p$ 的乘积；令 $E_0=E^d$。对这些奇素数，$d$ 的赋值同时给出所需奇偶性；在其余 $q\ge5,q\ne p$，扭曲至多不分歧，不改变 conductor。因 $p\nmid d$，在 $p$ 也至多作不分歧二次扭曲。小惯性分支在 $p$ 的潜在好约化指数是三或六，故 conductor 指数恰为二。于是

$$N(E_0)^{(6)}=p^2R^2T.$$

二次扭曲不改变 projective 表示，因此 $D,b,c$ 保持。二、三处的普遍 conductor 界分别为八、五，给 (220.3)。最后，$R$ 上的非平凡 projective 惯性、$T$ 上的潜在乘法以及 $p$ 上的三/六阶惯性都不能被二次扭曲消去，故每个扭曲的 $q\ge5$ conductor 指数至少为已给出的最小值。证毕。

令

$$N_{\rm tw}(E)=\min_{d\in\mathbb Q^{\times}/\mathbb Q^{\times2}}N(E^d).$$

最小值存在，因为这是一非空正整数集合。定理给

$$\boxed{p^2R^2T\le N_{\rm tw}(E)\le2^8 3^5p^2R^2T.} \tag{220.4}$$

不声称取得数值上最小 conductor 的扭曲必有奇部恰为 $p^2R^2T$；在二、三处与其他素数之间可能存在全局取舍。式 (220.4) 已完整覆盖这一可能。

## 5. 共同导子的双向有效比较

R66 给 $v_2(c)\le1$、$v_3(c)\le2$。R214 给 $v_2(b)\le3$、$v_3(b)\le1$ 及 $(b,c)=1$。若 $2\mid D$，则 $v_2(b)\le2$ 且 $2\nmid c$；二次基本判别式又有 $v_2(D)\le3$。因此

$$v_2(Dbc)\le5.$$

三处有 $v_3(D)\le1$，并且 $b,c$ 支撑不交，所以

$$v_3(Dbc)\le3.$$

由 $R=(Dbc)^{(6)}$ 得

$$\boxed{R^2\le D M^*\le2^{10}3^6R^2.} \tag{220.5}$$

结合 (220.4)，得到完全显式的变化导子比较：

$$\boxed{
\frac{p^2D M^*T}{2^{10}3^6}
\le N_{\rm tw}(E)
\le2^8 3^5p^2D M^*T.
} \tag{220.6}$$

特别当 $j$ 整时 $T=1$。同一条实际曲线的共同导子满足

$$\boxed{
\frac{N_{\rm tw}(E)}{2^8 3^5p^2D}
\le M^*
\le\frac{2^{10}3^6N_{\rm tw}(E)}{p^2D}.
} \tag{220.7}$$

因此所需的 $M^*$ 上界确实等价于同一实际曲线的最小二次扭曲导子上界，精确到两个固定的二、三幂因子；它不是由“选择一个最小模型”就自动变成关于 $p$ 的上界。

## 6. 直接从有理 $j$ 读取增长支撑

假设 $j(E)\ne0,1728$，写

$$j(E)=A/B,\qquad A,B\in\mathbb Z,\quad B>0,\quad(A,B)=1,\qquad H=A-1728B.$$

对整数 $X\ne0$ 定义

$$\mathcal R_3(X)=\prod_{\substack{q\ge5,q\ne p\\3\nmid v_q(X)}}q,\qquad
\mathcal R_2(X)=\prod_{\substack{q\ge5,q\ne p\\2\nmid v_q(X)}}q.$$

**定理 220.4。** 有准确支撑恒等式

$$\boxed{c^{(6)}=\mathcal R_3(A),\qquad
(Db)^{(6)}=\mathcal R_2(H),\qquad
R=\mathcal R_3(A)\mathcal R_2(H).} \tag{220.8}$$

若 $p\equiv1\pmod4$，还有 $b^{(6)}=1$，所以 $(D)^{(6)}=\mathcal R_2(H)$。

**证明。** 对 $q\ge5,q\ne p$，若 $q\mid B$，它在 Tate 支撑，故不进入 $D,b,c$；$A,H$ 都是 $q$ 单位。若 $q\nmid B$，曲线潜在好约化，取最小整模型的 $c_4,c_6,\Delta$。恒等式

$$j=c_4^3/\Delta,\qquad j-1728=c_6^2/\Delta$$

给

$$v_q(j)\equiv-v_q(\Delta)\pmod3,\qquad
v_q(j-1728)\equiv-v_q(\Delta)\pmod2.$$

温和好约化指数为 $12/\gcd(12,v_q\Delta)$。因而三次 projective 惯性恰当 $3\nmid v_q(j)$；四阶真实惯性恰当 $v_q(j-1728)$ 为奇数。后一断言也可直接从温和类型表核对：III、III$^*$ 的 $v_q\Delta$ 为 $3,9$，其他潜在好约化类型均为偶数。引理 220.2 将这两类分别对应到 $c$ 与 $Db$。

由于 $q\nmid B$，正的 $v_q(j)$ 等于 $v_q(A)$，正的 $v_q(j-1728)$ 等于 $v_q(H)$，给出前两式。$\gcd(A,H)$ 只含二、三素因子，故两种支撑不交，第三式成立。

最后，若 $p\equiv1\pmod4$，Cartan 中的所有四阶元素都在 $\mathbb F_p^{\times}$ 内，故为标量。真实有限惯性的四阶生成元行列式为一，而四阶标量的行列式为 $-1$，不能相等。所以四阶惯性一定在 Cartan 外，没有 $b$ 的大于三的支撑。证毕。

小惯性在 $p$ 的好约化指数为三或六，故 $3\nmid v_p(\Delta)$，从 $j$ 整于 $p$ 得 $v_p(A)>0$ 且 $3\nmid v_p(A)$。于是

$$p\mathcal R_3(A)\le|A|,\qquad\mathcal R_2(H)\le|H|.$$

(220.5)、(220.8) 进而给一条实际分子上界接口：

$$\boxed{p^2D M^*\le2^{10}3^6 A^2(A-1728B)^2.} \tag{220.9}$$

这是关于同一有理 $j$ 的分子及移位分子的界，不是关于 $p$ 的绝对上界。

## 7. 全部分母分支的全局椭圆导子下界

**推论 220.5。** 设仍为上述实际小惯性分支，且 $j(E)\notin\mathbb Z$。对每个 $\delta>0$，存在只依赖 $\delta$ 的正数 $c_\delta$，使

$$\boxed{M^*\ge c_\delta p^{2-1/\sqrt e-\delta},} \tag{220.10}$$

$$\boxed{N_{\rm tw}(E)\gg_\delta D T p^{4-1/\sqrt e-\delta}
\gg_\delta D p^{5-1/\sqrt e-\delta}.} \tag{220.11}$$

常数对变化的 $K,b,c$ 和全部 Tate 分母统一，一般无效；没有排除 exceptional 分母后再使用此式。

**证明。** 对 $p\ge2^{16}$，R181 §7 给已证明的整性接口：旧三次 Steinberg 两行与每个所需精确 Mellin 阶的实际非 CM 秩零投影同时存在时，R169/R172/R173 把有限行变成同一实际尖点的整微分，R177 的全类型单位理想排除所有分母。R217 §5 已在

$$p\ge C_\nu(M^*)^{\beta+\nu},\qquad\beta=1/(2-1/\sqrt e)$$

的范围同时提供这些准确中心值，包含阶四的非 CM 过滤。因此 $j$ 非整迫使上述不等式失败。给定 $0<\delta<2-1/\sqrt e$，选择 $\nu>0$ 使

$$\frac1{\beta+\nu}=2-1/\sqrt e-\delta,$$

取逆即得 (220.10)。若 $\delta$ 更大，较小 $\delta$ 的结论已经蕴含所求。有限范围 $37<p<2^{16}$ 可用 $M^*\ge3$ 缩小统一常数覆盖。

代入 (220.6) 的下界得到 (220.11) 的第一式。因为 $j$ 非整，$T>1$。R2 的每个 Tate 素数均满足 $q\equiv\pm1\pmod p$；$p>37$ 时 $q$ 为奇素数，故该同余式的最小可能值为 $2p-1$，而非偶数 $p-1$ 或 $p+1$。所以 $T\ge2p-1$，得到第二式。证毕。

这把此前仅限非 exceptional 分母的导子增长接口扩至全部实际分母。它仍是下界，不能反向用作排除大导子曲线的上界。

## 8. 对整 $j$ 分支的精确剩余任务

R217 的全部实际类型非消失范围为

$$p\ge C_\nu(M^*)^{\beta+\nu},\qquad
\beta=\frac1{2-1/\sqrt e}.$$

由 (220.7)，若能对实际整 $j$ 异常族证明足够强的

$$N_{\rm tw}(E)\ll p^{2+1/(\beta+\nu)}D,$$

并使常数满足对应严格比较，就能使该族落入这一非消失范围。现有的有限惯性、主模型选择、$p$ 挠点同构以及环类数条件并没有给这个上界。另一方面，即使得到全部非消失并借 R169/R172/R177/R181 排除非整 $j$，还要在整 $j$ 分支另给全局有理点排除；不能在逻辑上把非消失或整性直接当成 Serre 一致性。

本篇给出了增长控制的准确全局算术对象和固定常数，尚未完成上面的新输入。

## 来源

- R2、R66：Tate 支撑、$p$ 的三/六阶潜在好约化、准确三次导子与二三处界；R214：共同二阶导子、transfer、分歧交集；R213、R215、R217：所需非消失范围。
- J.-P. Serre, *Local Fields*, Chapter VI §3：Artin 导子的直和与诱导公式。本文已给出实际分解和全部导子因子。
- J. H. Silverman, *Advanced Topics in the Arithmetic of Elliptic Curves* (1994), Chapter IV，Tate 算法与温和 Kodaira 类型；Theorem IV.10.4 的普遍导子界 $f(E/F)\le2+6v_F(2)+3v_F(3)$，在 $\mathbb Q_2,\mathbb Q_3$ 给八、五。相同界可见由 Silverman 等撰写的 [LMFDB conductor 文档](https://www.lmfdb.org/knowledge/show/ec.conductor)。
