# R688 — 原全除点域、相位完全消去与轨道比的准确 p 次根

日期：2026-11-15。**状态：已证明。** 主课题仍未完成。

R684 保留的 \(\mu_p\) 相位在本原对象上实际上恒为一。
关键不是擅自对 log 取逆，而是 R663 的真实局部除点域恰有全部
\(\mathbf F_{p^2}^{\times}\) 作用；范数一子群固定 \(\mu_p\)，
而原完整规范在同一轨道上的乘积严格为一。

再用原整数 \(n=p+1\) 的除点函数，得到
\(T_g(T)^{p(p+1)}\) 的明确全局除点域系数。
同一原 \(P_\zeta(T)\) 更满足一个准确 \(p\) 次幂方程。
全部根均保持原有限 jet 的分支，原边界余数可回成完整的有限 Kummer 和。

## 1. 原记号和实际局部除点域

保
\[
p=6s-1>101,\quad q=p^2,\quad d=p+1,\quad
K_0=\mathbf Q(\omega),\quad K_p=\mathbf Q_p(\omega),\quad
F_p=K_0(E[p]),
\]
及固定 \(E:y^2=x^3+17\)、同一 \(\overline{\mathbf Q}\hookrightarrow\mathbf C_p\)。
本篇写 \(G(T)=T_g(u_T)\) 仅为缩短记号，不改变 R639/R681 的规范。

R663 的严格整可逆坐标
\[
v=h_{\rm LT}(u),\qquad
[-p]v=-pv+v^q,\qquad h_{\rm LT}\in u+u^2\mathcal O_{K_p}[[u]]
\tag{1}
\]
给全部非零 \(p\)-挠点
\[
v_T^{q-1}=p.
\tag{2}
\]
令 \(L=K_p(E[p])\) 为真正的局部除点域。
原 \(u=x^{-1/2}\) 是标准形式参数的整可逆级数；
故在给定分支上 \(u_T\in L\)，并由 (1) 的整收敛有 \(v_T\in L\)。
这里不把一个任意平方根扩张算入或删出 \(L\)。

因为 \(\mu_{q-1}\subset K_p\)，
\(X^{q-1}-p\) 是 Eisenstein 多项式，其一个根已经生成分裂域，
次数为 \(q-1\)。因此
\[
[L:K_p]\ge q-1.
\]
另一方面，全部 CM 在 \(K_0\) 及 \(K_p\) 上定义，
Galois 在一维 \(\mathbf F_q\) 模 \(E[p]\) 上的作用给
\[
[L:K_p]\le q-1,\qquad [F_p:K_0]\le q-1.
\]
所以准确有
\[
\boxed{
L=K_p(v_T),\qquad
[L:K_p]=[F_p:K_0]=q-1,\qquad
\operatorname{Gal}(F_p/K_0)\simeq\mathbf F_q^\times.}
\tag{3}
\]
\(F_p\) 在 \(K_0\) 的 \(p\) 位上只有一个素位，完成化就是 \(L\)；
该局部扩张全分歧，所有全局自同构都保持这个素位及其估值。

设
\[
H=\ker(\mathrm N_{\mathbf F_q/\mathbf F_p})
\subset\operatorname{Gal}(F_p/K_0).
\tag{4}
\]
它的阶为 \(d\)，对 \(E[p]\) 的作用准确是 R681 的范数一轨道。
Weil pairing 给模 \(p\) 圆分特征等于该二维作用的行列式，
即 \(\mathrm N_{\mathbf F_q/\mathbf F_p}\)。
因此
\[
\boxed{\mu_p\subset F_p,\quad H\text{ 逐点固定 }\mu_p,\quad
F_p^H=K_0(\mu_p).}
\tag{5}
\]
最后一式也由两边次数均为 \(p-1\) 得到；\(p>3\)，
\(K_0\cap\mathbf Q(\mu_p)=\mathbf Q\)。

(3) 不依一个未检查的全局 CM 大像定理；
它是原整 LT 坐标、Eisenstein 和显然的 CM 上界的准确比较。

## 2. 同一原完整规范的轨道乘积为一

原
\[
P_\zeta(u)=\frac{h(\zeta z(u))}{h(z(u))},\qquad h=\sigma/z,
\quad
T_g(u)=\exp(F_{\rm c}(z^d)-F(z)),\quad F=\log h
\]
均按 R639/R681 的完整整规范读取。
在正式级数中有
\[
T_g([\zeta]u)=T_g(u)/P_\zeta(u).
\tag{6}
\]
因为 \(F_{\rm c}\) 在 \(z\mapsto\zeta z\) 下不变，(6) 是准确式，
没有额外常数或根单位。
乘过全部 \(\zeta^d=1\)，用 \(T_g^d=\prod_\zeta P_\zeta\)，得到
\[
\boxed{\prod_{\zeta^d=1}T_g([\zeta]u)=1.}
\tag{7}
\]
(6)–(7) 的各因子都是开 \(u\) 单位盘上收敛的整单位。
故在首挠点可准确评价：
\[
\boxed{\prod_{h\in H}G(hT)=1.}
\tag{8}
\]
这里没有在边界分别评价可能不收敛的 \(h=\sigma/z\)，
只使用已付的整比值及正式恒等式的解析延续。

所有 \(G(T)\) 同时属于局部完成域 \(L\)，
因为它们是 \(K_p\) 系数的收敛整级数在 \(u_T\in L\) 的值。
对 \(\tau\in\operatorname{Gal}(L/K_p)\)，因此
\[
\boxed{\tau(G(T))=G(\tau T).}
\tag{9}
\]
R681 又给它们是代数数。必须分清“属于完成域 \(L\)”与“属于全局域 \(F_p\)”；
(9) 不预先断言后者。

## 3. R684 的 μp 相位严格为一

仍取
\[
\alpha=\omega^2+p\omega,\qquad \nu_\alpha=p^2-p+1,
\]
以及首系数为 \(\alpha\) 的原 \(\psi_\alpha\)。
R684 已付
\[
C_{\alpha,T}
=\frac{\psi_\alpha(T)^d}{\prod_{h\in H}\psi_\alpha(hT)}
\in F_p^\times,
\]
\[
G(T)^{d p(p-1)}=\epsilon_T C_{\alpha,T},
\qquad\epsilon_T\in\mu_p.
\tag{10}
\]
由 (3)–(5)，现在可将分母准确写为
\(\mathrm N_{F_p/K_0(\mu_p)}(\psi_\alpha(T))\)。

对每个 \(h\in H\)，(9)、CM 系数在 \(K_0\) 中及 (10) 给
\[
\epsilon_{hT}=h(\epsilon_T)=\epsilon_T.
\tag{11}
\]
最后等号用的是 (5)，不是把局部 Teichmüller 根误认成全局系数。
另一方面，
\(\prod_h C_{\alpha,hT}=1\) 是这个完整轨道比的直接恒等式。
将 (10) 乘过 \(h\in H\)，并用 (8)，得到
\[
1=\epsilon_T^d.
\]
与 \(\epsilon_T^p=1\)、\((d,p)=1\) 联立，故
\[
\boxed{\epsilon_T=1,\qquad
G(T)^{d p(p-1)}=C_{\alpha,T}.}
\tag{12}
\]
这完全消去原相位，仍是同一个实际值，未改 R684 的正确根条件。

## 4. 整数 p+1 的同一除点函数，保偶数情形的符号

令
\[
n=p+1,\qquad \nu_n=n^2.
\]
使用原整数除点函数
\[
\psi_n(P(z))=\sigma(nz)/\sigma(z)^{n^2}.
\tag{13}
\]
为明确 (13) 的偶数规范，给出所需性质。
sigma 的准周期式使该比值在格平移下不变：
分子和分母的指数因子相同，符号之商为
\((-1)^{n-n^2}=1\)。
其除子为全部非零 \(n\)-挠点的单零与
\(-(n^2-1)[O]\)，在原参数的首系数为 \(n\)。
因此它是 \(\mathbf Q(E)\) 中唯一这样归一的有理函数。

本处 \(n\) 偶，准确的成对公式是
\[
\boxed{
\psi_n(P)=n\,y(P)
\!\!\!\prod_{U\in(E[n]\setminus E[2])/\{\pm1\}}
(x(P)-x(U)).}
\tag{14}
\]
其中 \(y^2=\prod_{V\in E[2]\setminus0}(x-x(V))\)；
(14) 保三个二挠零点及首系数，不把偶数 \(\psi_n\) 当作 \(x\) 的多项式。

\(p\nmid n\)，故所有非零 \(n\)-挠点在 \(p\) 处不落入形式群。
于是
\[
\psi_n(P(u))=n u^{1-\nu_n}P_n(u),
\qquad P_n\in1+u^2\mathcal O[[u]].
\tag{15}
\]
同 R684 的核阶互素论证，\(\psi_n(T)\ne0\) 对所有非零 \(p\)-挠点成立。

令原乘 \(n\) 分子为 \(\phi_n=x([n]P)\psi_n^2\)，
\(B_n=u^{2\nu_n}\phi_n\)。
其同一个 sigma 身份给
\[
\Theta(f_n(t))=B_n(t)\Theta(t)^{\nu_n}.
\]
\(B_n\) 在开形式盘为常数一的整单位。
在 \(E[p]\) 上 \([n]T=T\)，所以 \(f_n(t_T)=t_T\)，并且
\[
B_n(t_T)=u_T^{2(\nu_n-1)}\psi_n(T)^2.
\tag{16}
\]
R676 的原 \(\log\Theta\) 已在整个开盘解析，
故 R681 的 log 比值论证及额外 \(p\) 的单射盘仍完整适用。

定义
\[
C_{n,T}=\frac{\psi_n(T)^d}{\prod_{h\in H}\psi_n(hT)}.
\tag{17}
\]
和 R684 一样，完整 \(A\) 系数恰为 \(C_{n,T}^2\)。
但现在 \(\nu_n-1=p(p+2)\) 为奇数；由 (15) 及 \(\prod_{\zeta^d=1}\zeta=-1\)，
\[
C_{n,T}\in-1+\mathfrak m,\qquad
D_{n,T}:=-C_{n,T}\in1+\mathfrak m.
\tag{18}
\]
这个负号不能省。

先由 R681 同样的 \(2p\) 幂单射盘得到
\[
G(T)^{d p(p+2)}=\epsilon_{n,T}D_{n,T},
\qquad\epsilon_{n,T}\in\mu_p.
\]
(17) 的完整轨道积为一，且 \(d\) 偶，故 \(\prod_hD_{n,hT}=1\)。
同 (11)–(12) 的 Galois 和范数论证消去相位，得到
\[
\boxed{G(T)^{d p(p+2)}=-C_{n,T}.}
\tag{19}
\]
(19) 仍保原全部 \(\mu_d\) 轨道与 \(T_g\) 高尾，不是另一条比较规范。

## 5. 指数降至 p(p+1)，系数为单个实际轨道比

因 \(p=6s-1\)，有准确 Bezout 式
\[
2s(p-1)-(2s-1)(p+2)=1.
\]
组合 (12)、(19)，定义原实际有理函数在挠点的值
\[
\boxed{
a_T=\frac{\psi_\alpha(T)^{2s}}{\psi_n(T)^{2s-1}}
\in F_p^\times,\qquad
N_T=\prod_{h\in H}a_{hT}\in K_0(\mu_p)^\times.}
\tag{20}
\]
由于 \(2s-1\) 为奇数，得到
\[
\boxed{
G(T)^{pd}=-\,\frac{a_T^d}{N_T}.}
\tag{21}
\]
右边完整属于 \(F_p\)，且其 \(H\) 范数为一。
它不再含未定相位。

正确根仍由 R681/R684 的同一个 \(\tau_d\) 指定：
\[
v_p(G(T)-\tau_d(u_T))>1/(p-1).
\tag{22}
\]
(21) 的指数 \(pd\) 的 \(p\) 部分仅一个 \(p\)，
故两个不同根之比是 \(pd\) 次单位根，最大非平凡根距为 \(1/(p-1)\)。
所以 (22) 对 (21) 仍唯一选定原值。

单值全局次数相应加强为
\[
\boxed{
[\mathbf Q(G(T)):\mathbf Q]
\le 2p(p+1)(p^2-1).}
\tag{23}
\]
没有将这个单值界移用于多点合成域。

R684 的高度界仍保留原较强表达
\[
h(G(T))\le2C_E+\log2+\frac{\log(p^2-p+1)}{p^2-p}.
\tag{24}
\]
不通过 (20) 中较大的 Bezout 幂重新引入多余的高度损失。
由 (21)，整个右端的实际高度准确为 \(pd\,h(G(T))=O(p^2)\)，
即使对 (20) 分别粗估会给更差的界。

## 6. 原每条 Pζ 的准确 p 次幂

式 (20) 在形式参数中有
\[
a(P(u))=c_pu^{-p}A_p(u),\qquad
c_p=\alpha^{2s}/n^{2s-1}\in\mathcal O^\times,\quad
A_p\in1+u^2\mathcal O[[u]].
\tag{25}
\]
\(u^{-p}\) 的指数来自同一个 Bezout 式；不是一个新选的首型。

对 \(h\leftrightarrow\zeta\in\mu_d\)，
(21) 的两个点之比给
\[
\left(
\frac{G(hT)^p/G(T)^p}{a_{hT}/a_T}
\right)^d=1.
\tag{26}
\]
原 \(G\) 值均在 \(1+\mathfrak m\)；
由 (25)、\(u_{hT}/(\zeta u_T)\in1+\mathfrak m\)，
括号内模 \(\mathfrak m\) 恰为 \(\zeta^p=\zeta^{-1}\)。
不同 \(\mu_d\) 根在剩余域中不同，因此 (26) 准确为
\[
\boxed{
\frac{G(hT)^p}{G(T)^p}
=\zeta^{-1}\frac{a_{hT}}{a_T}.}
\tag{27}
\]
再用原 (6)，得到
\[
\boxed{P_\zeta(u_T)^p=\zeta\,\frac{a_T}{a_{hT}}.}
\tag{28}
\]
这里没有遗漏 \(\mu_p\) 相位：
先有准确 (26)，再用 prime-to-\(p\) 的 \(d\) 次根距离确定它，
不是从 (28) 反向任取一个 \(p\) 次根。

令
\[
R_{\zeta,T}=\zeta P_\zeta(u_T).
\]
因 \(\zeta^{p+1}=1\)，
\[
\boxed{R_{\zeta,T}^p=a_T/a_{hT}.}
\tag{29}
\]
各 \(R_{\zeta,T}\) 仍是原 \(P_\zeta\) 的实际值。
若只用有限代数输入计算它们，应先由原 \(P_\zeta\) 至 \(u^d\) 的整 jet
按同一个 \(1/(p-1)\) 阈值唯一选根，再乘 \(\zeta\)。
仅知道 (29) 和模 \(\mathfrak m\) 首项不足以区分 \(p\) 个根；
本文并未删掉这个正确分支条件。

## 7. 原全部首边界零判定成为有限 Kummer 和

仍取 \(m=34,72\)，原
\(F_m(u)=T_g(u)^{-m}\phi_m(x(u),y(u))\)。
R681/R663 的同一个完整投影在 \(T\) 上为
\[
\Phi_m(u_T)=\frac1d\sum_{\zeta^d=1}
\zeta^mG(hT)^{-m}\phi_m(hT).
\]
由 (6)、(29)，准确化为
\[
\boxed{
\Phi_m(u_T)=\frac{G(T)^{-m}}d\,
\mathscr S_{m,T},\qquad
\mathscr S_{m,T}:=
\sum_{\zeta^d=1}R_{\zeta,T}^{\,m}\phi_m(hT),
\quad R_{\zeta,T}^p=a_T/a_{hT}.}
\tag{30}
\]
整个共同规范成为一个非零标量，不影响零判定。
全部 \(d\) 个原项和全部实际根都保留，不另加独立 \(p\) 次根。

因为 \(\Phi_m=v^{d-m}\mathcal B_m(v^d)\)，每个非零 \(v_T\) 给
\[
\boxed{
\mathcal B_m(v_T^d)=0
\iff\mathscr S_{m,T}=0.}
\tag{31}
\]
选每个 \(H\) 轨道一个代表，(31) 对全部 \(e=p-1\) 个代表同时成立，
恰等价于 R663 的 \(Q\mid\mathcal B_m\) 及全部首余数为零。
因此这里确实是原完整无限高尾的有限零判定，不只首模 \(p\)。

(30) 不自动非零。
不同 \(a_T/a_{hT}\) 的 Kummer 类是否相同、原 \(\phi_m\) 系数是否导致相消，
都仍是实际算术问题；不能在未证明独立时把这些根当成形式独立变量。
更没有由原 \(j_m=0\) 推出 (31)。
这个中央与边界之间的接口仍按 R663/R684 保持开放。

## 8. 已付范围与继续点

本篇付清：

- 原全局 \(p\) 除点域的实际完整群、唯一 \(p\) 位及范数一固定域；
- 同一原 \(T_g\) 轨道积为一及 R684 相位严格为一；
- 偶整数除点函数的必需负号和指数 \(p(p+1)\) 的明确方程；
- 原每条 \(P_\zeta\) 的准确 \(p\) 次幂与完整有限分支；
- 原全部首边界值的有限 Kummer 和，保所有轨道和无限高尾。

下一步须研究 (20)、(29)、(30) 的实际代数关系或原中央的传播。
单值次数、局部 Galois 作用、范数一和有界高度均不能单独替代这一步。
本篇没有宣称 \(G(T)\in F_p\)，也没有把 \(P_\zeta\) 的根自由更换。

## 依赖

- [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  原严格 LT 坐标、完整 \(\mu_{q-1}\) 作用及边界轨道。
- [R681](R681-original-torsion-gauge-and-finite-algebraic-residues.md)：
  原 \(P_\zeta,T_g\)、整分支与原全部余数。
- [R684](R684-original-division-orbit-phase-and-uniform-height.md)：
  原除点轨道比、\(\mu_p\) 相位、有限选根和统一高度。
- [R639](R639-complete-original-central-gauge-and-full-formal-disc-stokes.md)、
  [R676](R676-original-unit-cm-numerator-and-three-digit-lift.md)：
  同一 sigma 归一、CM 除点函数及整个开盘的原 log 身份。
- A. V. Sutherland, *18.783 Elliptic Curves*, Fall 2025,
  Lecture 23, Theorem 23.23：
  [MIT 官方正文](https://ocw.mit.edu/courses/18-783-elliptic-curves-fall-2025/mit18_783_f25_lec23.pdf)。
  使用 Weil pairing 的非退化性、Galois 等变性及行列式作用。
- sigma 准周期式使用 [DLMF 23.2](https://dlmf.nist.gov/23.2)，
  Equations 23.2.15–23.2.17；偶数除点函数的所需推论在第4节完整重写。

本篇无新数值扫描、可重算证书输出或新源列。
