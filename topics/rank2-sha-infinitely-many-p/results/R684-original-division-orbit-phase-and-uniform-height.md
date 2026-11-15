# R684 — 原除点轨道比、确定的 μp 相位与完整规范的统一高度

日期：2026-11-15。**状态：以下有限代数表示及高度界已证明；主课题仍未完成。**

R681 已将同一个原完整整规范 \(T_g\) 在首 \(p\)-挠点的值变成带唯一分支的代数数。
本篇进一步消去该幂方程中所有局部 CM 单位根坐标和 \(u\) 的平方根：
系数成为原 CM 除点多项式的一个明确轨道比，落在全局 \(p\) 除点域。

得到的准确指数是 \(p(p^2-1)\)。可能的 \(\mu_p\) 相位没有删去，
而由原截至 \(u^{p+1}\) 的有限 jet 唯一确定。
同一个表示给 \(T_g\) 的绝对对数高度以不依 \(p\) 的上界，
并付原首层共振余数的 \(O_m(p^2)\) 高度成本。
这些都是原实际值；不由代数性或高度界预支中央非零。

## 1. 同一原规范与全局轨道

沿用 R676/R681 的所有规范，固定
\[
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad e=p-1,\quad
K_0=\mathbf Q(\omega),\quad b=17.
\]
取同一个嵌入 \(\overline{\mathbf Q}\hookrightarrow\mathbf C_p\)，
所有估值以 \(v_p(p)=1\) 归一。

原曲线 \(E:y^2=x^3+b\) 的 CM 均在 \(K_0\) 上定义。
设
\[
F_p=K_0(E[p]),\qquad
H=\ker\!\left((\mathbf Z[\omega]/p)^\times
             \xrightarrow{\mathrm{Norm}}\mathbf F_p^\times\right).
\]
因为 \(p\) 惰性，\(H\) 有 \(d\) 个元素。
它通过局部 Teichmüller 提升与 R681 的 \(\mu_d\) 对应。
对 \(T\in E[p]\setminus0\) 及 \(h\in H\)，令
\(T_h=[a_h]T\)，其中 \(a_h\in\mathbf Z[\omega]\) 任取提升。
该点与提升无关，并落在 \(E[p](F_p)\)。

仍取
\[
\alpha=\omega(p+\omega),\qquad
\nu=\mathrm N(\alpha)=p^2-p+1,\qquad \nu-1=p(p-1).
\]
\(\nu\) 为奇数且 \(p\nmid\nu\)。用 R639/R676 的**同一**规范
\[
\psi_\alpha(P)=
\alpha\!\!\prod_{U\in(\ker[\alpha]\setminus0)/\{\pm1\}}
       (x(P)-x(U)).
\tag{1}
\]
它的首系数为 \(\alpha\)，不是 monic 版本。
\(\psi_\alpha\in K_0[x]\)，次数为 \((\nu-1)/2\)，并有
\[
\sigma(\alpha z)=\psi_\alpha(P(z))\sigma(z)^\nu.
\]
R676 的 monic numerator 为
\(\phi_\alpha=x([\alpha]P)\psi_\alpha(P)^2\)，
\(B_\alpha=u^{2\nu}\phi_\alpha(u^{-2})\)。

对任何非零 \(p\)-挠点，(1) 的全部因子非零：
若 \(x(T)=x(U)\)，则 \(T=\pm U\)，与 \(p\nmid\nu\) 冲突。
定义明确轨道比
\[
\boxed{
C_T=\frac{\psi_\alpha(T)^d}
          {\displaystyle\prod_{h\in H}\psi_\alpha(T_h)}
\in F_p^\times.}
\tag{2}
\]
这里使用原全部 \(H\) 轨道。无需将 \(H\) 预先认作一个全局 Galois 子群，
也不把 (2) 未经证明地称作某个子扩张的场范数。

## 2. R681 的系数准确等于轨道比的平方

在 \(E[p]\) 上 \([\alpha]=[\omega^2]\)，而
\(x([\omega^2]T)=\omega^2x(T)\)。因此
\[
\boxed{
B_\alpha(t_T)
=\omega^2u_T^{\,2(\nu-1)}\psi_\alpha(T)^2.}
\tag{3}
\]
同式适用于每个 \(T_\zeta=T_h\)。

R681(13) 的完整系数是
\[
A_T=
\frac{B_\alpha(t_T)^d}{\prod_{\zeta^d=1}B_\alpha(t_\zeta)}
\left(\prod_{\zeta^d=1}\frac{u_\zeta}{\zeta u_T}\right)^{2(\nu-1)}.
\tag{4}
\]
将 (3) 逐项代入，所有 \(u\) 幂及 \(\omega^2\) 消去，
剩余 \((\prod_{\zeta^d=1}\zeta)^{-2(\nu-1)}=1\)。
故
\[
\boxed{A_T=C_T^2.}
\tag{5}
\]
这不是仅模 \(p\) 的关系；它消去了 (4) 的全部坐标根与局部 \(\zeta\)。

还需要确定 (2) 的单位邻域，而不能只知其平方。
由于 \([\alpha]\) 在 \(p\) 处为 étale，非零 \(\alpha\)-核点均不在形式群中，
故其 \(x\) 坐标在该处整。由 (1)
\[
\psi_\alpha(P(u))=\alpha u^{\,1-\nu}P_\alpha(u),
\qquad P_\alpha\in1+u^2\mathcal O[[u]].
\]
同时 R681 的
\(R_\zeta=u_\zeta/(\zeta u_T)\in1+u_T^2\mathcal O\)。
因为 \(d\) 偶、\(\prod\zeta=-1\)，而 \(\nu-1\) 偶，
\[
C_T=
\left(\prod_{\zeta^d=1}R_\zeta\right)^{\nu-1}
\frac{P_\alpha(u_T)^d}{\prod_{\zeta^d=1}P_\alpha(u_\zeta)}.
\]
所以
\[
\boxed{v_p(C_T-1)\ge \frac2{q-1}.}
\tag{6}
\]
所有结论仍使用 R681 的同一个原形式参数分支。

## 3. 缩小的准确幂方程与不能删去的相位

置
\[
M_0=d(\nu-1)=p(q-1).
\]
R681 已付的完整幂方程与 (5) 给
\[
T_g(u_T)^{\,2pM_0}=C_T^{\,2p}.
\tag{7}
\]
定义**实际**相位
\[
\epsilon_T=\frac{T_g(u_T)^{M_0}}{C_T}.
\]
(7) 给 \(\epsilon_T^{2p}=1\)，而原 \(T_g\in1+u^2\mathcal O[[u]]\)
和 (6) 给 \(\epsilon_T\in1+\mathfrak m\)。
因 \(p>2\)，其中的二阶部分只能为一；于是
\[
\boxed{
\epsilon_T\in\mu_p,\qquad
T_g(u_T)^{\,p(q-1)}=\epsilon_TC_T.}
\tag{8}
\]
这一步直接使用已付的幂方程和单位邻域，不在 log 的核中任意选相位。

\(\mu_p\subset F_p\)：取 \(E[p]\) 的一组基，由非退化、
Galois 等变的 Weil pairing 得一个 \(F_p\) 内的原始 \(p\) 次单位根。
所需定理见文末 [W] Theorem 23.23。
故 (8) 的右端**整个落在 \(F_p\)**。

### 相位的有限选择，不增加一个未知条件

沿用原有限 jet
\[
\tau_d(U)=\sum_{n=0}^{d}[U^n]T_g(U)\,U^n.
\tag{9}
\]
原 \(h=\sigma/z\) 只有 \(z^{6n}\) 项，\(d\) 被六整除，
且 \(z=uH(bu^6)\)。因此 \(T_g(u)\in\mathbf Q[[u^6]]\)，
\(\tau_d(u_T)\) 是 \(u_T^6=x(T)^{-3}\) 的有理多项式，故
\[
\tau_d(u_T)\in F_p.
\tag{10}
\]
R681 的整尾界为
\[
v_p\bigl(T_g(u_T)-\tau_d(u_T)\bigr)
\ge\frac{d+1}{q-1}>\frac1{p-1}.
\tag{11}
\]
定义完全有限的
\[
a_T=\frac{\tau_d(u_T)^{M_0}}{C_T}\in F_p.
\]
在 (11) 的 log/exp 单射盘，取 \(M_0\) 次方使误差估值再增加一；
也可逐项用二项式证明。于是
\[
v_p(a_T-\epsilon_T)>1+\frac1{p-1}.
\tag{12}
\]
不同 \(\mu_p\) 根之差的估值准确为 \(1/(p-1)\)。因此
\[
\boxed{
\epsilon_T\text{ 是唯一满足 }
v_p(a_T-\epsilon)>1/(p-1)\text{ 的 }\epsilon\in\mu_p.}
\tag{13}
\]
(13) 的输入只是原点的有限 jet、(1) 的有限除点数据和有限集合 \(\mu_p\)。

选定 (13) 后，(8) 的正确根也由
\[
\boxed{v_p(X-\tau_d(u_T))>1/(p-1)}
\tag{14}
\]
唯一指定。因为 \(M_0\) 的 \(p\) 部分只有一个 \(p\)，
两个不同根的比是 \(M_0\) 次单位根，其非平凡距离不会超过该阈值。
存在性由原 \(T_g\) 给，唯一性由上述根距给。
所以 (8)、(13)、(14) 保留原实际值及全部相位，而没有增添自由根。

## 4. 全局次数的一个明确上界

\(E[p]\) 是一维 \(\mathbf F_q=\mathbf Z[\omega]/p\) 向量空间。
因所有 CM 在 \(K_0\) 上定义，\(F_p/K_0\) 的 Galois 群
忠实嵌入 \(\mathbf F_q^\times\)。从而
\[
[F_p:K_0]\le q-1.
\tag{15}
\]
不需在这里另证全 Galois 像满射。
由 (8) 的 \(F_p\) 系数多项式，
\[
[F_p(T_g(u_T)):F_p]\le M_0.
\]
因此每个实际值有
\[
\boxed{
[\mathbf Q(T_g(u_T)):\mathbf Q]\le
2p(q-1)^2=2p(p^2-1)^2.}
\tag{16}
\]
这是单个值的上界，不是所有边界值及余数共同生成域的同一个上界。
尤其不能在后续 Liouville 估计中把 (16) 免费用于多点插值的合成域。

## 5. 原所有挠点 x 坐标的统一绝对高度

以下 \(h\) 始终表示 \(\overline{\mathbf Q}\) 上的**绝对对数 Weil 高度**，
以各地局部度除全局次数归一。不是某个随 \(p\) 变化的未归一高度。

存在只依固定 \(E\) 的有效常数 \(C_E\)，使每个非零代数挠点 \(U\) 满足
\[
\boxed{h(x(U))\le C_E.}
\tag{17}
\]
为支付其在任意次数域上的一致性，给出一个直接证明。
固定倍点有理映射为
\[
\varphi(X:Z)=
(X^4-8bXZ^3:4X^3Z+4bZ^4).
\tag{18}
\]
两个四次齐次式没有公共射影零点：
\(Z=0\) 时首项不为零；有限公共零将要求
\(x(x^3-8b)=0\) 且 \(x^3+b=0\)，与 \(b\ne0\) 冲突。
其固定系数的局部上界和 resultant Bezout 身份的局部下界
给出一个有效 \(C_{\rm dup}\)，对所有代数 \(x\) 同时有
\[
|h(\varphi(x))-4h(x)|\le C_{\rm dup}.
\tag{19}
\]
有限坏地仅由固定系数和非零 resultant 决定；
按绝对局部度相加，常数与 \(x\) 的数域无关。
这也是 [H] Theorem 25.14 的曲线特例。

对挠点 \(U\)，倍点轨道有限（允许出现 \(O\)，其射影高度为零）。
反复使用 (19) 得
\[
h(x(U))\le4^{-n}h(x(2^nU))
+\frac{C_{\rm dup}}3(1-4^{-n}).
\]
令 \(n\to\infty\) 即得 (17)，可取 \(C_E=C_{\rm dup}/3\)。
此证明没有调用“在固定数域中 Northcott 有限”来冒充全体代数挠点的一致界。

## 6. 原完整 Tg 的高度与 p 无关

(1) 中各核点都是挠点，非零因子已支付。
由 (17) 和标准绝对高度不等式
\(h(a-b)\le h(a)+h(b)+\log2\)，
\[
h(\psi_\alpha(T))
\le h(\alpha)+\frac{\nu-1}{2}(2C_E+\log2).
\]
\(\alpha\) 是代数整数，两个复嵌入的绝对值都为 \(\sqrt\nu\)，所以
\[
\boxed{
h(\psi_\alpha(T))\le H_\psi:=
\frac12\log\nu+\frac{\nu-1}{2}(2C_E+\log2).}
\tag{20}
\]
同界对每个 \(T_h\) 成立。
轨道比 (2) 遂给
\[
h(C_T)\le2dH_\psi.
\tag{21}
\]
(8) 中根单位高度为零，且 \(h(X^{M_0})=M_0h(X)\)，因此
\[
\boxed{
h(T_g(u_T))
=\frac{h(C_T)}{d(\nu-1)}
\le2C_E+\log2+\frac{\log\nu}{\nu-1}.}
\tag{22}
\]
特别对全部本题允许的 \(p,T\)，可统一取
\[
\boxed{H_*:=2C_E+\log2+1,\qquad h(T_g(u_T))\le H_*.}
\tag{23}
\]
同一界自然适用于逆值，因为 \(h(X^{-1})=h(X)\)。
此处没有使用任何“正阶 jet 也有统一高度”的未付断言；
(22) 只涉及零阶实际值。R681 全正阶 jet 仍仅按其有限代数递推处理。

结合 (16)，得到的是**高度统一而次数可增长**的实际代数族。
不能从 (23) 宣称这些值只取有限多个值，也不能将其当作固定全局来源列。

## 7. 完整原 B 的边界值与第一共振余数成本

保 R681/R663 的原 \(m=34,72\)：
\[
F_m(u)=T_g(u)^{-m}\phi_m(x(u),y(u)),
\]
\[
\Phi_m(u(v))=\frac1d\sum_{\zeta^d=1}\zeta^m
F_m(u(\zeta v))
=v^{d-m}\mathcal B_m(W),\quad W=v^d,\quad
Q(W)=W^e-p.
\tag{24}
\]
全部原多项式、投影和 \(T_g\) 高尾不变。
\(\phi_m\) 为固定原来源的多项式。
由 \(2h(y(U))=h(x(U)^3+b)\le3C_E+h(b)+\log2\)，
存在可由这两个固定多项式直接计算的 \(C_{\phi,m,E}\)，满足
\[
h(\phi_m(U))\le C_{\phi,m,E}
\]
对所有本节挠点成立。
置
\[
K_{m,E}=mH_*+C_{\phi,m,E}.
\]
(23) 给 \(h(F_m(u_T))\le K_{m,E}\)。
有限和与除以 \(d\) 的全部成本保为
\[
h(\Phi_m(u_T))\le dK_{m,E}+2\log d.
\]
原 LT 值 \(v_T^{q-1}=p\)，故
\(h(v_T)=\log p/(q-1)\)。
于是对 \(Q\) 的每个根 \(\xi\)，
\[
\boxed{
h(\mathcal B_m(\xi))\le
B_{m,p}:=dK_{m,E}+2\log d
+\frac{|d-m|\log p}{q-1}.}
\tag{25}
\]
这是 \(O_m(p)\)，所用常数仅依原固定曲线和原固定多项式。

原第一余式写成
\[
R_{m,1}(W)=\sum_{i=0}^{e-1}\mathfrak r_{m,i,0}W^i.
\]
取任一固定代数 \(\rho\) 满足 \(\rho^e=p\)。
完整 Fourier 插值准确给
\[
\boxed{
\mathfrak r_{m,i,0}
=\frac{\rho^{-i}}{e}\sum_{\eta^e=1}
\eta^{-i}\mathcal B_m(\rho\eta).}
\tag{26}
\]
这就是 R681 的全部 \(e\) 个边界值，不少取一个轨道。
由 (25) 及 \(h(\rho)=\log p/e\)，
\[
\boxed{
h(\mathfrak r_{m,i,0})
\le eB_{m,p}+2\log e+\frac{i\log p}{e}
=O_m(p^2).}
\tag{27}
\]
零值也满足此界；不通过 (27) 暗中假设非零。
R681 已证 (26) 准确等于
\[
\mathfrak r_{m,i,0}=\sum_{k\ge0}p^k b_{m,i+ek}.
\]
所以 (27) 给的是原完整无限高尾的实际代数高度，
不是其某个有限截断的高度。

## 8. 对主问题的准确接口

新结果是原除点域中的明确系数 \(C_T\)、有限且唯一的 \(\mu_p\) 相位、
较小的实际幂方程、单值次数上界、全部首挠点的统一 \(T_g\) 高度，
以及首层原共振余数的完整 \(O_m(p^2)\) 高度成本。

R663 的同一个 \(Y\) 闭边界仍等价于全部 \(\mathfrak r_{m,i,0}=0\)；
原 \(X\) 下降仍更强。
本篇没有证明原 \(j=0\) 迫这些余数为零，也没有证明它们跨 \(p\) 非零。
(25)–(27) 不把 (16) 的单值次数界误用于合成域，
更不由一个有限代数零判定自动得到无穷多个 \(p\) 的结论。

后续可以对 (2)、(13)、(26) 的同一实际数作代数关系或高度比较，
但须保正确分支、全部轨道和真正的共同数域成本。
主目标仍要求至少一条固定原完整中央在同一无限素数族上非零。

## 依赖与原定理

- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)：
  同一原完整规范与 CM sigma 归一。
- [R676](R676-original-unit-cm-numerator-and-three-digit-lift.md)：
  原 \(\alpha,\nu,\psi_\alpha,\phi_\alpha,B_\alpha\)。
- [R681](R681-original-torsion-gauge-and-finite-algebraic-residues.md)：
  真实首挠点幂方程、唯一有限分支、全部原余数。
- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  原 LT 坐标、全部 \(Q\) 轨道和无限尾。
- [W] A. V. Sutherland, *18.783 Elliptic Curves*, Fall 2025,
  Lecture 23, Theorem 23.23, printed p. 10：
  [MIT 官方讲义](https://ocw.mit.edu/courses/18-783-elliptic-curves-fall-2025/mit18_783_f25_lec23.pdf)。
  本篇只用 Weil pairing 的非退化性及 Galois 等变性。
- [H] A. V. Sutherland, *18.782 Introduction to Arithmetic Geometry*,
  Fall 2013, Lecture 25, Theorem 25.14：
  [MIT 官方讲义](https://math.mit.edu/classes/18.782/2013fa/LectureNotes25.pdf)。
  使用固定射影态射的绝对高度界；第5节另给固定倍点/resultant 证明。

本篇没有新扫描、辅助素数数值推断或未执行证书。
