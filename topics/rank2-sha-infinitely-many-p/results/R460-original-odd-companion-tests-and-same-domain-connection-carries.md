# R460 — 原奇伴随的正 Tc 提取、同域连接与两环带整消元

日期：2026-11-14。**状态：已证明。**

R307 的两个真实连接伴随 \(C_{13},C_{15}\) 可以在 R458 同一个
\(\sigma(c)\otimes[-2H_{33}(Z)/3]\) 联合中，用六个固定正奇
Tc 次数完整抽出。本文保其 tame-one 移权、周期、原点质量及
奇 Euler 因子。由此，原连接乘积 \(\mathfrak q C\) 的完整第一
来源也由同一联合内的明确混合测试实现。

在两条实际相消环带上，移权伴随的系数不同。一个单位行列式
准确消去同一个未知移权中央，返回 \(S-aH_j\)；再加入同域的
参考测试便得到原 \(J_S\) 的完整两域返回。全部 carry 仍保留。
只比较了完整第一推前，没有把新表示的内部事件当成原
\(\nu_{\mathfrak q}\otimes\nu_C\) 的独立隐藏事件。主目标未完成。

## 1. 同一个来源和两种完整奇偶格

保持 R455、R458 的原规范
\[
\rho=\nu_\sigma(c)\otimes\nu_H(Z),\qquad
\nu_H=\nu_{-2H_{33}/3},\quad H_{33}=S/\sigma,
\]
\[
Y=Z+c,\quad T_c=Z-33c,\quad
F(y,t)=-\frac23\sigma(y-33t)H_{33}(y+t)
 \in\mathcal S_{34}\boxtimes\mathcal S_{1122}.
\tag{1}
\]
仍取原 \(b=17\)、普通周期 \(\Omega\) 和固定 ray，
\[
\lambda=-\bar\pi_0^{-1},\quad \kappa=p/\bar\pi_0^2,\quad
q=-\chi\lambda,\quad \chi^2=1,\quad d=p-1.
\tag{2}
\]
同一完整核心是
\[
K_YF=R_YF,\qquad K_{T_c}F=-\chi R_YF.
\tag{3}
\]
原 sigma 输入的标量是 \(-\lambda\)，原 \(H_{33}\) 输入的标量
是 \(\chi\lambda\)，所以两输入同时深系数为 \(\lambda q\)。

对
\[
m_k=6k-1=5,11,17,23,29,35,\qquad1\le k\le6,
\]
令
\[
O_k(y)=m_k![t^{m_k}]F(y,t).
\]
共同 \(\mu_6\) 型为零，因此这些完整第一来源属于型一奇空间
\[
\mathcal H_1=\sigma^{34}y\,K[X]_{\le5},\qquad X=x^3.
\tag{4}
\]
这里 \(y=x'/2\sim-z^{-3}\) 是椭圆函数，不是测度第一输出。
空间的六个基向量首阶分别为 \(31,25,19,13,7,1\)；
所以六个 Taylor 坐标 \(z^{1+6\ell}\)、\(0\le\ell\le5\)，
是整个空间的可逆坐标，不是对未知函数的有限采样。

准确有
\[
\boxed{O_k(z)=\sigma_b(z)^{34}y_b(z)
       \sum_{j=0}^5M^{\rm odd}_{jk}b^{k+4-j}X_b(z)^j.}
\tag{5}
\]

## 2. 完整奇矩阵的有限精确重建

令 \(w=z^6\)，使用 R455 已从 Weierstrass 方程重建的
\[
x=z^{-2}B(w),\quad \sigma=zA(w),\quad
H_{33}=z^5\mathcal H(w),\quad
A=\sum a_iw^i,\quad\mathcal H=\sum r_iw^i.
\]
这里暂取 \(b=1\)。由 \(y=x'/2\)，
\[
y=-z^{-3}D(w),\qquad D=B-3wB'.
\tag{6}
\]
完整基矩阵是
\[
\boxed{
J^{\rm odd}_{\ell j}
=-[w^{\ell-5+j}]A^{34}DB^{3j},\qquad
0\le\ell,j\le5,\qquad \det J^{\rm odd}=-1.}
\tag{7}
\]
负下标视为零。对应来源坐标为
\[
\boxed{
V^{\rm odd}_{\ell k}
=-\frac23(6k-1)!
\sum_{i+j=k+\ell-1}a_i r_j
\sum_{h=0}^{6k-1}
\binom{1+6i}{h}\binom{5+6j}{6k-1-h}(-33)^h.}
\tag{8}
\]
所有越界二项系数为零，完整矩阵准确等于
\[
\boxed{M_{\rm odd}=(J^{\rm odd})^{-1}V^{\rm odd}.}
\tag{9}
\]
(6)–(9) 用至 \(w^{11}\) 的有理系数即足够；整条来源身份
来自 (4) 的全局成员资格与 (7) 的可逆完整坐标。

精确计算给
\[
\boxed{\det M_{\rm odd}\not=0,\qquad
       \det M_{\rm odd}\equiv43\pmod {101}.}
\tag{10}
\]
全部三十六项、精确行列式与基矩阵均附在 JSON。
模 \(101\) 只为固定有理行列式给一个短非零证书，
不是用有限目标素数推断主目标。

## 3. 原 \(C_{13},C_{15}\) 的完整测试

R307 的真实连接 frame 为
\[
F_0=\Theta^{17},\qquad
\mathfrak q=F_0'/F_0,\qquad \nabla_{F_0}=\partial_z-\mathfrak q.
\tag{11}
\]
其原伴随 \(C=C_{1j}\)、\(j=3,5\)，满足
\[
\boxed{C'-\mathfrak q C=S-aH_j,\qquad C'(0)=-a,}
\tag{12}
\]
其中
\[
a=a_{13}=-\frac{37}{33936b}\quad(j=3),\qquad
a=a_{15}=-\frac{37}{53760b}\quad(j=5).
\tag{13}
\]
这些是同一原 \(S,H_3,H_5\)，没有换参考或改其质量。

在 (4) 的完整基中，
\[
C_{1j}=\sigma_b^{34}y_b
       \sum_{h=0}^5P_{1j,h}\,b^{4-h}X_b^h,
\tag{14}
\]
两个准确向量为
\[
\boxed{
\mathbf P_{13}=
\left(0,\frac{10880}{14847},-\frac{13504}{14847},
\frac{6269}{9898},-\frac{6523}{59388},-\frac{37}{33936}\right)^{\mathsf t},}
\tag{15}
\]
\[
\boxed{
\mathbf P_{15}=
\left(0,\frac{923}{1470},\frac{107}{5880},
\frac{11399}{15680},-\frac{15919}{94080},-\frac{37}{53760}\right)^{\mathsf t}.}
\tag{16}
\]
可直接由 R307 三条 \(R_k\) 的完整多项式相减核定；
\(P_0=0\) 保留其两个三挠点全纯条件，
\(P_5=ab\) 则因基首项为 \(-z\) 给回 \(C'(0)=-a\)。

定义固定有理向量及正奇多项式
\[
\mathbf e_C=M_{\rm odd}^{-1}\mathbf P_C,\qquad
h_C(t)=\sum_{k=1}^6 e_{C,k}b^{-k}t^{6k-1}.
\tag{17}
\]
全部六项系数在 JSON 中完整显示。(5)、(9)、(14) 给整个测度身份
\[
\boxed{(Y)_*\{h_C(T_c/\Omega)\rho\}=\nu_C.}
\tag{18}
\]
因此不是将 \(C\) 的六个低阶系数替代其完整来源。

## 4. 奇 Euler、真实 tame-one 行及非零质量

第一来源 \(C\) 为奇，故 Tc 深核心 (3) 在此来源上是
\(-q\)，不是偶块的 \(q\)。定义
\[
\boxed{
E^{\rm odd}_k=1+q\kappa^{6k-1},\qquad
h_C^\times(t)=
\sum_{k=1}^6\frac{e_{C,k}b^{-k}}{E^{\rm odd}_k}t^{6k-1}.}
\tag{19}
\]
所有分母都是单位，完整有
\[
\boxed{
(Y)_*\{\mathbf1_{T_c\ {\rm unit}}h_C^\times(T_c/\Omega)\rho\}
=\nu_C.}
\tag{20}
\]
奇块若误用 R458 的 \(1-q\kappa^{6k}\)，会改变实际来源。

原移权行准确写为
\[
\boxed{
D_C(u)=\Omega^{-1}\int_{Y\ {\rm unit}}
Y\langle Y\rangle^{du}\,d\nu_C(Y)
=\Omega^{-1}M_{C,1}(u+1/d).}
\tag{21}
\]
右式是 R307、R311 的同一个 tame-one 分支，未换成质量为零的
奇 principal 行。整个 \(\mathcal S_{34}\) 核心为反射，
所以 \(\nu_C|_p=-\lambda[\kappa]_*\nu_C\)，从而
\[
\boxed{D_C(0)=(1+\lambda\kappa)C'(0)
=-a(1+\lambda\kappa).}
\tag{22}
\]
在当前 ray 以及下述固定有限坏集外，它是单位。
\(\Omega^{-1}\) 抵消的是实际一阶矩的 \(\Omega\)，
没有重置测度周期。

## 5. 原连接乘积在同一联合内的完整实现

令 R458 的偶测试分别为 \(h_S^\times,h_{H_j}^\times\)，并记
\[
G_C(u)=J_S(u)-aJ_{H_j}(u),\qquad
h_G^\times=h_S^\times-a h_{H_j}^\times.
\tag{23}
\]
在同一个 \(\rho\) 中定义明确的混合测试
\[
\boxed{
\mathcal Q_C(Y,T_c)
=\frac Y\Omega h_C^\times(T_c/\Omega)-h_G^\times(T_c/\Omega).}
\tag{24}
\]
(12)、(20) 及 R458 的完整偶提取给
\[
\boxed{
(Y)_*\{\mathbf1_{T_c\ {\rm unit}}\mathcal Q_C(Y,T_c)\rho\}
=\nu_{\mathfrak q C}=\nu_{\mathfrak q}*\nu_C.}
\tag{25}
\]
其中 \(Y/\Omega\) 的整个第一推前是 \(\nu_{C'}\)，
这正是原连接 (12)，没有丢掉微分尺度。

所以原连接的完整单位行及质量准确为
\[
Q_C(u):=M_{\mathfrak q C}(u)=D_C(u)-G_C(u),
\]
\[
\boxed{
G_C(0)=-a(1-\lambda),\qquad
Q_C(0)=-a\lambda(1+\kappa).}
\tag{26}
\]
最后一项是单位，不是零；它与 \((\mathfrak q C)(0)=0\)
的总质量不同。原连接卷积的完整第一中央也因 (25) 确实被实现。

式 (25) **只认同第一推前**。原
\(\nu_{\mathfrak q}(x)\otimes\nu_C(y)\) 的独立条件
\(x\in p^n\)、\(y\) 单位等，不能被直接认作下面在原
\(c,Z\) 表示中的事件；本篇没有作这一步。

## 6. 同一个连接测试的两条真实相消环带

沿 R458 保
\[
\mathscr N_{Y,r}=\{c,Z\ {\rm unit},\,Y\in\kappa^r\mathbf Z_p^\times\},
\quad
\mathscr N_{T,r}=\{Y\ {\rm unit},\,T_c\in\kappa^r\mathbf Z_p^\times\},
\quad r\ge1.
\tag{27}
\]
第一域自动有 Tc 单位，第二域自动有 \(c,Z\) 单位。定义
\[
\mathcal Y_{r,C}^\kappa(u)=
\int_{\mathscr N_{Y,r}}\langle Y/\kappa^r\rangle^{du}
                        \mathcal Q_C(Y,T_c)\,d\rho.
\tag{28}
\]
这里 (24) 中的 \(Y/\Omega\) 保留原物理 \(Y\)，
不再额外除 \(\kappa^r\)。

Tc 环带上须完整归一第二测试。令
\[
\mathcal Q_{C,r}(Y,T_c)
=\frac Y\Omega h_C^\times(T_c/(\kappa^r\Omega))
-h_G^\times(T_c/(\kappa^r\Omega)),
\]
\[
\mathcal T_{r,C}^\kappa(u)=
\int_{\mathscr N_{T,r}}\langle Y\rangle^{du}
                        \mathcal Q_{C,r}(Y,T_c)\,d\rho .
\tag{29}
\]
它的 \(\kappa^{-r}\) 只用在显示的实际深域中。

完整来源及域计算给
\[
\boxed{
\begin{aligned}
\mathcal Y_{r,C}^\kappa(u)
 &=(-\lambda\kappa)^rD_C(u)-\lambda^rG_C(u),\\
\mathcal T_{r,C}^\kappa(u)
 &=(-q)^rD_C(u)-q^rG_C(u).
\end{aligned}}
\tag{30}
\]

为核第一式的奇项，先用未作 Euler 调整的一个
\(Y T_c^{m_k}/\Omega^{m_k+1}\) 列。完整第一环带给
\((-\lambda\kappa)^rD_k\)。其两个原输入同时深的行是
\[
\lambda q\,\kappa^{m_k+1}(-\lambda\kappa)^{r-1}D_k
=-q\kappa^{m_k}(-\lambda\kappa)^rD_k.
\]
相减给 \((1+q\kappa^{m_k})(-\lambda\kappa)^rD_k\)；
这由 (19) 正确消掉。偶项是 R458 的
\(\lambda^rG_C\)。第二式用 Tc 核心，其第一反射使
\(Yh_C^\times\) 行变号、纯偶行不变；故两个系数分别为
\((-q)^r,q^r\)。没有把两种 parity 合并。

## 7. 单位行列式消去同一个未知移权行

令 \(\epsilon_r=(-1)^r\)，并归一
\[
\mathcal A_r=\lambda^{-r}\mathcal Y_{r,C}^\kappa,\qquad
\mathcal B_r=q^{-r}\mathcal T_{r,C}^\kappa.
\]
则 (30) 的整条两行是
\[
\mathcal A_r=\epsilon_r\kappa^rD_C-G_C,\qquad
\mathcal B_r=\epsilon_rD_C-G_C.
\tag{31}
\]
行列式为 \(\epsilon_r(1-\kappa^r)\)，是单位。完整消元为
\[
\boxed{
D_C=\frac{\epsilon_r(\mathcal A_r-\mathcal B_r)}{\kappa^r-1},
\qquad
G_C=\frac{\mathcal A_r-\kappa^r\mathcal B_r}{\kappa^r-1}.}
\tag{32}
\]
这对整条 \(u\) 函数成立，尤其同一个未知
\(M'_{C,1}(1/d)\) 已从第二式准确消去。
不能将等式中的任一 carry 单独声称为零。

参考的同域返回也已经由 R458 支付：
\[
N_{T,r,H_j}^\kappa(u)=q^rJ_{H_j}(u).
\tag{33}
\]
因此三个准确测试给原完整算术行
\[
\boxed{
\lambda^{-r}\mathcal Y_{r,C}^\kappa
-\kappa^rq^{-r}\mathcal T_{r,C}^\kappa
+a(\kappa^r-1)q^{-r}N_{T,r,H_j}^\kappa
=(\kappa^r-1)J_S.
}
\tag{34}
\]
后两个项实际在同一个 \(\mathscr N_{T,r}\) 上，
可以合成一个明确测试
\[
-\kappa^r\frac Y\Omega h_C^\times(T_c/(\kappa^r\Omega))
+\kappa^rh_S^\times(T_c/(\kappa^r\Omega))
-a h_{H_j}^\times(T_c/(\kappa^r\Omega)).
\tag{35}
\]
所以 (34) 是两个实际原域的完整返回，不只是三条抽象中央数。
测试最高总次数仍为三十六，\(r=2\) 即给固定深度的实际接口；
不需要 \(r\) 随 \(p\) 增长。

## 8. 物理 \(p^r\) 归一的完整非齐次连接项

仍令
\[
\xi=\kappa/p=\lambda^2,\qquad
\ell=d\log_p\langle\xi\rangle\ne0.
\]
将 (28) 的 principal 测试改为 \(Y/p^r\)，记
\(\mathcal Y_{r,C}^{p}\)，仍保 (24) 的原物理 \(Y/\Omega\)。
准确有
\[
\mathcal Y_{r,C}^{p}(u)
=\langle\xi\rangle^{rdu}\mathcal Y_{r,C}^{\kappa}(u).
\tag{36}
\]
归一质量完整是
\[
\boxed{
A_{r,C}:=\lambda^{-r}\mathcal Y_{r,C}^{p}(0)
=a\{(1-\lambda)-\epsilon_r\kappa^r(1+\lambda\kappa)\}.}
\tag{37}
\]
它在当前范围是单位：模 \(p\) 为 \(a(1-\lambda)\)。
因此 (32) 的中央形式必须保
\[
\boxed{
\begin{aligned}
(\kappa^r-1)G_C'(0)
={}&\lambda^{-r}(\mathcal Y_{r,C}^{p})'(0)
-\kappa^rq^{-r}(\mathcal T_{r,C}^{\kappa})'(0)
-r\ell A_{r,C}.
\end{aligned}}
\tag{38}
\]
右端最后一项确实非零；没有把已知非零质量误当成中央导数。

若要完整返回原 \(S\)，在 (34) 中第一项必须同步乘
\(\langle\xi\rangle^{-rdu}\)。微分后恰加回 (38) 的质量修正：
\[
\boxed{
\begin{aligned}
(\kappa^r-1)J'_S(0)
={}&\lambda^{-r}(\mathcal Y_{r,C}^{p})'(0)
-\kappa^rq^{-r}(\mathcal T_{r,C}^{\kappa})'(0)\\
&+a(\kappa^r-1)q^{-r}(N_{T,r,H_j}^{\kappa})'(0)
-r\ell A_{r,C}.
\end{aligned}}
\tag{39}
\]
所以若原 \(J'_S(0)=0\)，前三个实际 carry 中央之和等于
已知非零的 \(r\ell A_{r,C}\)，而不是零。这是完整非齐次
关系，没有由归一方式的差异制造一个矛盾。

## 9. 有限整性与下一实际接口

(17) 的两个固定有理向量、完整 \(M_{\rm odd}^{-1}\)，以及
R458 的偶提取只有一个固定有限分母集合。脚本给出一个明确
固定坏整数，包含原 R458 坏整数、这些分母及
\(17\cdot37\cdot101\)。排除其素因子后，所有新测试整；
新 Euler 分母是单位，(32) 的行列式也是单位。
不需要分解这个大整数，也没有有限目标素数扫描。

在原 \(\Phi_+\) 表示中附加 \(T\) 深条件，仍由 R454 的完整
核心支付，因其保整个 \(Y,T_c,Z,c\)。其他多输入表示中的
隐藏条件须使用各自已付的真实提升；本篇不将两个不同提升的
隐藏变量拼成未经定义的联合。这些运输不赋单独 carry 新零。

已付的新接口是：R307 的真实连接伴随与连接卷积观察，
现在都在 R458 同一个原两输入表示中有固定整测试；
两个真实环带单位消元严格返回原 \(S\)。
仍需控制 (34) 或 (39) 中实际 carry 的组合，不能将其中
一个完整第一推前身份当成独立输入域的身份。

## 精确证书与依赖

- [完整脚本](../scripts/check-r460-original-odd-companion-carries.py)
  从原 sigma/Weierstrass 级数重建整个奇矩阵，逐项核两原伴随、
  所有周期权、质量及任意奇偶 \(r\) 的代数消元。
- [完整有理数据](../scripts/check-r460-original-odd-companion-carries.json)
  含六维基、三十六项矩阵、行列式、两组六项测试以及固定坏整数。
- [R307：同一原算术连接及两个真实伴随](R307-jzero-three-original-sources-exact-reference-values-and-full-first-companion.md)。
- [R311：原 tame-one 分支及完整移权中央](R311-jzero-original-odd-six-tame-one-core-and-pure-dyadic-companion.md)。
- [R455：原两输入全局来源与完整六维坐标](R455-original-pure-companion-test-and-slope-core-arithmetic-return.md)。
- [R458：原两方向相消支和两个参考测试](R458-original-two-input-boundary-and-nonhomogeneous-reference-carries.md)。

