# R430 — 原第二输出的整反卷积与 degree18 小核的完整中央行

日期：2026-11-14。**状态：已证明。** 在 R424 的同一实际联合中，
可以沿第二输出整有界地除掉质量一因子
\(E_{20}=J_{12}\Theta(2\cdot)\)。得到未扭曲的
\(\mathcal S_{34}\boxtimes\mathcal S_{18}\) 来源
\[
\mathcal K=-\frac23\{S\otimes G_{18}-C_{34}\otimes F_{18}\}.
\]
原 principal 中央对任意第二输出测试的返回仍准确成立；完整
\(X,W,V\) 三个推前仍为零。本文同时给第二输出反卷积的真实测试转置、
保留的第一输出 core、准确的两个混合矩族及新的正交输出坐标。
反卷积不与混合输出限制交换，故没有把旧六方向 core 免费移到新来源。
主目标未完成。

## 1. 固定来源与允许的普通素数

保持 R423、R424 的同一普通周期 \(\Omega=\Omega_p\)、ray、
\(b=17\)、\(p>19\) 及
\[
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad d=p-1.
\]
令 \(\mathcal O\) 为原完整系数赋值环。所有测度和卷积都在同一个
原加法群 \(\mathbf Z_p\) 中，不改变周期或改用另一个 Schwartz 来源。

R424 的完整实际因子为
\[
G_{16}(z)=\frac{\sigma(2z)\sigma(2\delta z)}{4\delta},\quad
J_{12}(z)=\frac{\sigma(4z)}{2\sigma(2z)},\quad
\Theta=x\sigma^2,
\]
\[
F_{18}=\sigma^{18}xP_2(x^3),\qquad
G_{18}=\sigma^{18}(x^9-30bx^6-144b^2x^3-32b^3),
\]
\[
S=G_{16}F_{18},\qquad C_{34}=G_{16}G_{18}.
\tag{1}
\]
其中 \(P_2(X)=X^2-4bX/7+16b^2/7\)。它们全部在原整 theta 格中，
且
\[
S=z^6+\cdots,\quad C_{34}=z^2+\cdots,\quad
F_{18}=z^4+\cdots,\quad G_{18}(0)=1.
\tag{2}
\]
设
\[
E_{20}=J_{12}\Theta(2\cdot),\quad
B_{38}=E_{20}G_{18},\quad D_{38}=E_{20}F_{18}.
\]
同一个实际来源是
\[
H=-\frac23(S\otimes B_{38}-C_{34}\otimes D_{38}).
\tag{3}
\]
这里 \(E_{20}(0)=1\)，是以下整反卷积的关键；没有仅凭一个
复解析无零小圆盘声称测度可逆。

## 2. 质量一的整 Amice 因子确有有界卷积逆

用原正式群坐标 \(z=\Omega\log(1+T)\)，记 \(\nu_E\) 的 Amice 变换为
\[
\mathcal A_E(T)=E_{20}(\Omega\log(1+T))
               =1+\sum_{n\ge1}a_nT^n\in\mathcal O[[T]].
\tag{4}
\]
令 \(b_0=1\)，逐项定义
\[
b_n=-\sum_{i=1}^n a_i b_{n-i}.
\]
每个 \(b_n\in\mathcal O\)，所以 \(\sum b_nT^n\) 不仅是形式逆，
还是有界整测度 \(\iota_E\) 的 Amice 变换。准确有
\[
\boxed{\nu_E*\iota_E=\iota_E*\nu_E=\delta_0,
\qquad \|\iota_E\|\le1.}
\tag{5}
\]
\(\delta_0\) 是原加法群零点的 Dirac 测度。
唯一性来自幂级数逆的唯一性及 Amice 单射。由于 \(E_{20}\) 为偶且
\(\mu_6\) 权零，\(\iota_E\) 也被同样的单位推前固定：对 (5)
作该群自同构后，仍是同一逆。

对任意有界联合 \(\mu(Y,X)\)，定义只在第二输出卷积
\[
\mu*_X\iota_E=(Y,X+t)_*(\mu(Y,X)\otimes\iota_E(t)).
\tag{6}
\]
这是整有界算子，范数至多一；其逆为 \(*_X\nu_E\)。对任意连续测试
\(f(Y),h(X)\)，真正转置是
\[
\int f(Y)h(X)\,d(\mu*_X\iota_E)
=\int f(Y)\,h_E(X)\,d\mu,
\quad h_E(X)=\int h(X+t)\,d\iota_E(t).
\tag{7}
\]
连续性、整有界性及紧群上的测度乘积保证这一 Fubini 式。
它保留的是全部第二输出测试，不把 \(X\) 的深度指示函数原样传过卷积。

## 3. 真正的较小来源与三个完整零边际

定义
\[
\nu_{\mathcal K}=\nu_H*_X\iota_E.
\]
(3)、(5) 的 Amice 恒等式准确给
\[
\boxed{\mathcal K(y,v)
=-\frac23\{S(y)G_{18}(v)-C_{34}(y)F_{18}(v)\}
\in\mathcal S_{34}\boxtimes\mathcal S_{18}.}
\tag{8}
\]
其整性既由 (6) 保证，也可直接从 (1) 的整张量看出。
R424 的同一对称核 \(\mathcal R\in\mathcal S_{16}\boxtimes\mathcal S_{16}\)
进一步给
\[
\boxed{\mathcal K(y,v)=G_{16}(y)
          \sigma(y-v)\sigma(y+v)\mathcal R(y,v).}
\tag{9}
\]
两个轴的 degree 分别是 \(16+2+16=34\)、\(2+16=18\)；这里没有
新增覆盖或未写出的平坦 twist。

令 \(W=Y+X,V=X-Y\)。由 (1)、(2)、(8)，准确有
\[
\boxed{Y_*\nu_{\mathcal K}=-2\nu_S/3,\qquad
X_*\nu_{\mathcal K}=W_*\nu_{\mathcal K}=V_*\nu_{\mathcal K}=0.}
\tag{10}
\]
其中 \(X\) 边际使用 \(S(0)=C_{34}(0)=0\)；\(W\) 边际使用
\(SG_{18}=C_{34}F_{18}\)；\(V\) 则还用分别偶性。
最后两条必须这样从 (8) 重新证明，不能只说除去第二输出因子会
自动保持旧 \(W,V\) 零。

## 4. 全部 principal 条件中央和真正保留的 core

记 \(K_{0,u}(Y)=\mathbf1_{Y\in\mathbf Z_p^\times}
\langle Y\rangle^{du}\)。由 R424 的完整条件测度式和 (7)，
\[
\boxed{\int K_{0,u}(Y)h(X)\,d\nu_{\mathcal K}
=-\frac23J_S(u)\int h\,d\nu_{G_{18}}.}
\tag{11}
\]
也可直接由 (8) 证明：\(C_{34}\) 的 \(\mu_6\) 权为二，故 principal
第一输出测试精确杀掉该项；\(S\) 权为零。
对任意连续 \(h\) 在原中央求导，得到
\[
\boxed{\int\mathbf1_{Y\in\mathbf Z_p^\times}
d\log_p\langle Y\rangle h(X)\,d\nu_{\mathcal K}
=-\frac23J'_S(0)\int h\,d\nu_{G_{18}}.}
\tag{12}
\]
所以原 \(J'_S(0)=0\) 合法控制新小核的任意完整第二输出测试。
反向取 \(h=1\)，因 \(G_{18}(0)=1\)，也准确恢复原条件。
没有为 \(G_{18}\) 的单位质量或中央导数额外预设值。

R424 已付原两条第一轴来源 \(S,C_{34}\) 的相同 core。
它与只在 \(X\) 的卷积交换，因此新小核仍有整个联合身份
\[
\boxed{\nu_{\mathcal K}|_{Y\in p^N\mathbf Z_p}
=\lambda^N(\kappa^NY,X)_*\nu_{\mathcal K}\qquad(N\ge0).}
\tag{13}
\]
这里也可以从 (8) 的两张量逐项证明。
旧 \(W,Q\) 条件核不与 (6) 交换，因为第二输出平移同时改变这些
混合输出及其域指示函数；\(X\) 限制一般也不与卷积交换。
不过 R426 已独立证明实际 \(F_{18},G_{18}\) 在原 ray 的完整 core
同为 \(-\lambda\)。因此从 (8) 逐项得到另一条真实联合式
\[
\boxed{\nu_{\mathcal K}|_{X\in p^N\mathbf Z_p}
=(-\lambda)^N(Y,\kappa^NX)_*\nu_{\mathcal K}.}
\tag{13a}
\]
这是直接使用新 degree18 来源的已证 core，而不是把限制穿过反卷积。
特别 \(G_{18}\) 的完整单位质量为 \(1+\lambda\)，是原 ray 的单位；
(12) 在双方输出均为单位时与原 \(J'_S\) 相差准确单位
\(-2(1+\lambda)/3\)。混合输出的 core 仍须另作同样完整的计算。

还可合法保留已除因子的全部独立输入。设 \(\mu(Z)\) 是一个固定
有界测度，\(Z\) 可以有多个原输入，并与 \(\nu_{\mathcal K}\) 独立。
由 (12) 对任意连续 \(\Phi(X,Z)\) 作 Fubini，准确有
\[
\boxed{\int\mathbf1_{Y\text{单位}}d\log_p\langle Y\rangle
\Phi(X,Z)\,d\nu_{\mathcal K}\,d\mu
=-\frac23J'_S(0)\int\Phi(X,Z)\,d\nu_{G_{18}}\,d\mu.}
\tag{13b}
\]
所以若原中央失败，该明确独立第二轴表示中的隐藏域确实可任意测试。
例如取 \(\mu\) 为原 \(J_{12}\) 与 \(\Theta(2\cdot)\) 的实际输入
乘积，恢复 \(H\) 时仍能保这些输入的全部独立深度条件。
这不包含 \(\mathcal K\) 第一轴内部的 sigma 条件，也不包含未经
证明替换 \(\mathcal R\) 整个联合后得到的输入。

## 5. 深层总和的准确两个混合矩族

设
\[
\mu_j(A)=\int t^j\,d\nu_A(t),\qquad
I_{-j}(A)=\int_{\mathbf Z_p^\times}t^{-j}\,d\nu_A(t).
\]
它们均在同一个原周期中，整有界性给所有这些值的范数至多一。
从 (8) 得实际混合观察
\[
M_j:=\int_{X\in\mathbf Z_p^\times}Y^jX^{-j}\,d\nu_{\mathcal K}
=-\frac23\{\mu_j(S)I_{-j}(G_{18})-
                 \mu_j(C_{34})I_{-j}(F_{18})\}.
\tag{14}
\]
四来源的 CM 权依次为 \(0,0,2,4\)，故只有
\[
\boxed{\begin{aligned}
M_{6a}&=-\frac23\mu_{6a}(S)I_{-6a}(G_{18})&& (a\ge1),\\
M_{6a+2}&=\frac23\mu_{6a+2}(C_{34})I_{-(6a+2)}(F_{18})&& (a\ge0),
\end{aligned}}
\tag{15}
\]
可能非零，其余全部 \(M_j\) 为零。这里使用了负指数的真实 CM
权：例如 \(-(6a+2)\equiv4\pmod6\)，与 \(F_{18}\) 一致。

取真正的域 \(\mathcal D_N=\{Y\in p^N\mathbf Z_p,
W\in\mathbf Z_p^\times\}\)、\(N\ge1\)。由 (13)，缩放后
\(W=\kappa^NY+X\) 为单位等价于 \(X\) 为单位。
在该域展开完整 log，常数项由 (10) 的整个 \(X\) 推前零消失，
奇数项及另一偶余类由 (15) 消失。准确得到
\[
\boxed{\begin{aligned}
\int_{\mathcal D_N}d\log_p\langle W\rangle\,d\nu_{\mathcal K}
=\frac{2d}{3}\lambda^N\bigg\{
&\sum_{a\ge1}\frac{\kappa^{6aN}}{6a}
       \mu_{6a}(S)I_{-6a}(G_{18})\\
-&\sum_{a\ge0}\frac{\kappa^{(6a+2)N}}{6a+2}
       \mu_{6a+2}(C_{34})I_{-(6a+2)}(F_{18})\bigg\}.
\end{aligned}}
\tag{16}
\]
第 \(j\) 项赋值下界是 \(Nj-v_p(j)\)，所以全部尾收敛，允许逐项
积分。最早候选项是
\[
-\frac d3\lambda^N\kappa^{2N}\mu_2(C_{34})I_{-2}(F_{18})
=-\frac{2d}{3}\lambda^N\kappa^{2N}\Omega^2 I_{-2}(F_{18}).
\tag{17}
\]
本文没有由 \(F_{18}\ne0\)、其首正矩或 CM 本征性预付
\(I_{-2}(F_{18})\ne0\)。即使 (16) 的某个深域非零，(10) 仍使
\(\{Y\notin p^N,W\text{单位}\}\) 的完整中央贡献为其负数。
这份补域不能从原 \(Y\) 中央条件中删除。

## 6. 新 degree 的完整正交坐标

新来源的输入 Gram 是 \(\operatorname{diag}(34,18)\)。若要另行
计算总和的真实 prime core，准确的正交伴随为
\[
W=Y+X,\qquad Q_*=9Y-17X,
\]
\[
\boxed{Y=(17W+Q_*)/26,\qquad X=(9W-Q_*)/26.}
\tag{18}
\]
其行列式为 \(-26\)，在当前全部 \(p>19\) 处为单位，且
\[
\begin{pmatrix}1&1\\9&-17\end{pmatrix}
\begin{pmatrix}34&0\\0&18\end{pmatrix}
\begin{pmatrix}1&9\\1&-17\end{pmatrix}
=\begin{pmatrix}52&0\\0&7956\end{pmatrix}.
\tag{19}
\]
因此真正的双变量生成函数
\(\mathcal K(w+9q,w-17q)\) 在
\(\mathcal S_{52}\boxtimes\mathcal S_{7956}\) 中，全部伴随输出保留。
整数拉回与交叉项相消支付这里的 theta 身份；它本身不计算新的
\(W\)-core 相位或有限群。

R429 的两深度域仍是原 sigma 的隐藏输入条件。沿第二输出反卷积
是一个已付的有界操作，但它的转置是 (7)，并非保持每个原输入域
不变的坐标替换。后续若借较小 degree 或 (18) 作运输，仍须逐项
保原二次权、原尺度及完整补域。

## 依赖

- [R424：真实二源 Bezout 核与完整条件中央](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。
- [R423：原 H 与完整第一轴 core](R423-original-four-state-signed-group-and-untwisted-half-period-source.md)。
- [R426：原 degree18 完整 core 与实际单位质量](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R429：同一原目标的两深度非零域](R429-original-two-depth-grid-and-reciprocal-sigma-nonvanishing.md)。

本篇的反卷积、测试转置、边际和两混合矩族均由显示的原整恒等式
直接证明，不依赖额外数值核验或未完成的 U72 谱计算。
