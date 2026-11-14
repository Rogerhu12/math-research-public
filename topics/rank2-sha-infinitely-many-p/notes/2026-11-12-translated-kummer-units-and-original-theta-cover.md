# 原 256 点 Kronecker theta 的平移补偿、固定同源覆盖与完整范数

日期：2026-11-12。状态：本文的二变量恒等式、固定有理函数模型、
平移后的全部 norm 常数及比值的同源分配均已证明。
它们尚未证明指定中央系数或完整中央导数对无穷多个 $p$ 非零。

本文接续
[全部同源邻点的准确 norm](2026-11-12-all-isogeny-neighbors-kummer-norms.md)。
这里始终使用原来的 $256$ 点轨道，而不是换成一个方便的挠点和。
新得到的正面接口是：原 theta 的全部轨道依赖，
可由同一个固定 $[68]$ 覆盖上的有理函数比值承载；
同一个二挠点参考 Kronecker theta 必须保留。

## 1. 两变量的意义与不能直接替换的挠点标签

固定原曲线及微分
\[
E:y^2=x^3-17x,\qquad \omega=dx/(2y),\qquad
\Gamma=\Omega_E\mathbb Z[i],\qquad N=68.
\]
令 $F=K(E[f])$、$f=34(1+i)$，$\mathcal S$ 为原 $256$ 点轨道，
并取固定参考二挠点
\[
T=(0,0).
\]
对 $P\in\mathcal S$ 选代表 $z_P\in N^{-1}\Gamma$。
记
\[
A_\Gamma=\operatorname{area}(\mathbb C/\Gamma)/\pi,\qquad
\eta_P=\eta(Nz_P)/N=\bar z_P/A_\Gamma .
\]
后一等式使用原方格 $s_2(\Gamma)=0$。设
\[
F_P(z)=e^{-\eta_P z}\frac{\sigma(z_P+z)}{\sigma(z_P)},\qquad
F_P(0)=1.
\tag{1}
\]
原来的两变量函数准确是
\[
\Theta_P(z,w):=\Theta_{z_P,0}(z,w)
 =\frac{F_P(z+w)}{F_P(z)\sigma(w)},\qquad
\mathscr K(z,w)=\sum_{P\in\mathcal S}\Theta_P(z,w)-\frac{256}{w},
\]
\[
d_m=[z^mw^m]\mathscr K(z,w).
\tag{2}
\]
因此第一变量 $z$ 移动的是原挠点附近的点，第二变量 $w$
是原 Poincaré/theta 变量；它们都不是模参数 $t$。

这里的 $P+z$ 不可直接改称一个新的 reduced-translation 标签：
若对非挠点 $P+z$ 重新使用 BK 的平移定义，
还会出现 $e^{w\bar z/A_\Gamma}$ 的差。
(2) 固定了原标签 $P$ 的指数补偿，因而是原问题的全纯二变量 germ。

沿用原整形式参数 $Z=-x/y$ 和除法函数
\[
\Psi_N(z)=\sigma(Nz)/\sigma(z)^{N^2},\qquad
d_P=D\Psi_N(P),\qquad
r_P(R)=\frac{\Psi_N(P+R)}{d_P Z(R)},\qquad r_P(O)=1.
\tag{3}
\]
不能直接把 $P$ 改成非挠点 $P+W$ 后仍除以 $Z(R)$：
此时 $\Psi_N(P+W)$ 不为零，原点的零相消已经失效。

## 2. 正确的平移单位及其全部 norm 常数

在同一条曲线上，用两个形式点 $W,R$ 定义
\[
\widetilde r_P(W,R)
 =\frac{r_P(W+R)}{r_P(W)}
 =\frac{\Psi_N(P+W+R)}{\Psi_N(P+W)}
       \frac{Z(W)}{Z(W+R)}.
\tag{4}
\]
最后的表达式有可去的表面零极点；第一式证明它在 $(O,O)$
是一个真实正则单位，且
\[
\widetilde r_P(O,R)=r_P(R),\qquad
\widetilde r_P(W,O)=1.
\]
在所有 $p\nmid N$ 的原好整模型上，同样是整单位。

令 $\varphi:E\to E'$ 为次数 $n$、与 $N$ 互素的奇次数同源，
所有 level 标签照原样运输。前篇已证
\[
\operatorname{Norm}_\varphi r_P
       =\kappa_{\varphi,P}r'_{\varphi P}.
\]
对第二变量 $R$ 取范数，保留 $W$ 不动：
\[
\operatorname{Norm}_{\varphi,R}\widetilde r_P(W,R)
=\kappa_{\varphi,P}(W)
 \frac{r'_{\varphi P}(\varphi W+R')}
      {r'_{\varphi P}(\varphi W)},
\quad R'=\varphi R,
\]
\[
\boxed{\quad
\kappa_{\varphi,P}(W)
 =\prod_{Q\in\ker\varphi}
       \frac{r_P(W+Q)}{r_P(W)}
 =\kappa_{\varphi,P}
       \frac{r'_{\varphi P}(\varphi W)}{r_P(W)^n}.
\quad}
\tag{5}
\]
这准确计算了平移标签引入的非恒定项，而不假设它仍是原固定数。

对全部 $p+1$ 个阶 $p$ 子群 $G$，非零 $p$ 挠点的分拆仍给
\[
\prod_G\kappa_{\varphi_G,P}(W)=\kappa_{[p],P}(W),
\]
\[
\boxed{\quad
\kappa_{[p],P}(W)
 =\kappa_{[p],P}
       \frac{r_{pP}([p]W)}{r_P(W)^{p^2}}.
\quad}
\tag{6}
\]
在加法局部参数中，对每个 $k\ge1$，
\[
\left.D_W^k\log\kappa_{[p],P}(W)\right|_O
=p^kD^k\log r_{pP}(O)-p^2D^k\log r_P(O).
\tag{7}
\]
将 (7) 对原 $\mathcal S-i\mathcal S^{\rm rot}$ 作相同线性组合，
由于 $p\mathcal S=\epsilon_p\mathcal S$、
$r_{-P}(R)=r_P(-R)$，其中 $\epsilon_p=(-1/p)$，右侧恰为
\[
(\epsilon_p^kp^k-p^2)D^kh_e(O).
\tag{8}
\]
(8) 中的 $h_e$ 包括前篇的原 $-c_e/(2N^2)$ 因子。

所以平移后的 $\kappa(W)$ 确实有新变量，但其所有正导数
已经是原归一单位的导数，未得到一个独立已知的非零对数。
更直接地，(5) 的 $\log\kappa(W)$ 仍不依赖第二变量 $R$，
故所有同时含正 $R$ 阶的 mixed derivatives 都杀掉它。
把 $W=R$ 代入后再看一个单变量系数，并不等于原来的
$[z^mw^m]$ 对角系数；后者不能以这种代入替换。

归一 norm 后的完整二变量恒等式为
\[
\prod_G
 \frac{r'_{\varphi_GP}(\varphi_G(W+R))}
      {r'_{\varphi_GP}(\varphi_GW)}
 =
 \left(\frac{r_P(W+R)}{r_P(W)}\right)^p
 \frac{r_{pP}([p](W+R))}{r_{pP}([p]W)}.
\tag{9}
\]
它由前篇整个 germ 恒等式分别在 $W+R$、$W$ 取值相除得到；
没有丢弃一个只在模 $p$ 才出现的项。

## 3. 原 theta 与平移单位之间的准确公共补偿

定义原点值为一的公共 germ
\[
T_N(z)=\frac{\sigma(Nz)}{N Z(z)}.
\tag{10}
\]
由 sigma 准周期和 $Nz_P\in\Gamma$，将 (3) 的分子在 $P+z$
展开并以一次项规范，准确得到
\[
\boxed{\qquad r_P(z)=T_N(z)F_P(z)^{-N^2}.\qquad}
\tag{11}
\]
例如 $\sigma(Nz_P+Nz)$ 的指数是 $N\eta(Nz_P)z$；
它等于 $N^2\eta_Pz$，正是 (1) 的 $-N^2$ 次幂。
常数由 $r_P(0)=T_N(0)=F_P(0)=1$ 唯一确定。

于是 (2) 给出
\[
\boxed{\quad
[\sigma(w)\Theta_P(z,w)]^{N^2}
 =\frac{C_N(z,w)}{\widetilde r_P(z,w)},\qquad
C_N(z,w)=\frac{T_N(z+w)}{T_N(z)}.
\quad}
\tag{12}
\]
也可以写成
\[
C_N(z,w)=
 \frac{\sigma(N(z+w))}{\sigma(Nz)}
 \frac{Z(z)}{Z(z+w)}.
\]
此式在 $z=0$ 的准确可去值为
$\sigma(Nw)/(N Z(w))$，不是一。

在非 CM 周期格上，若仍用普通 Weierstrass $\sigma$，
则 reduced theta 是
$\theta(z)=e^{-s_2z^2/2}\sigma(z)$。
因此 (12) 的右侧必须另乘 $e^{-N^2s_2zw}$。
本文的简式 (12) 仅在原方格纤维使用；
对下面两个 $P,T$ 的 theta 比值，这个公共因子恰好消去，
所以比值公式可沿所有邻点运输。

(12) 的 $N^2$ 次根取在 $w=0$ 值为一的唯一正式分支。
原 $\mathscr K$ 是每个根恢复以后再相加：
\[
\mathscr K(z,w)
 =\frac{C_N(z,w)^{1/N^2}}{\sigma(w)}
      \sum_{P\in\mathcal S}\widetilde r_P(z,w)^{-1/N^2}
       -\frac{256}{w}.
\tag{13}
\]
这已是对原 $256$ 点的准确公式，不能把右侧的和改成
$\sum\log\widetilde r_P$，也不能丢掉公共 $C_N$。

## 4. 同一个固定 [N] 覆盖上的有理函数

对参考点 $T$，(1) 给
\[
F_T(z)=\theta_T(z)
=e^{-\eta_Tz}\frac{\sigma(z_T+z)}{\sigma(z_T)},\qquad
\theta_T(0)=1.
\]
本曲线上 $\theta_T(z)^2=x(z)\sigma(z)^2$；
这就是已经使用的同一二挠点 theta 参考，未换曲线或角色。

### 4.1 一个由除子和原点值唯一确定的真实函数

存在唯一
\[
B_P\in F(E)^\times,\qquad
\operatorname{div}B_P=N(-P)-N(-T),\qquad B_P(O)=1.
\tag{14}
\]
存在性由椭圆曲线的 degree-zero divisor 判据：
$N((-P)-(-T))$ 的点和是 $N(T-P)=O$。
除子定义于 $F$，且 $O$ 在其支撑外。
任何代数闭包上的函数经 $O$ 值规范后都被
$\operatorname{Gal}(\overline F/F)$ 固定，故确属 $F(E)$。
唯一性是同除子函数仅差常数。

前篇的完整除子含共同 $D_N$，因此恰有
\[
\boxed{\qquad B_P^N=r_T/r_P.\qquad}
\tag{15}
\]
证明是两侧除子均为 $N^2(-P)-N^2(-T)$，且在 $O$ 都为一。
用 (11)，再取原点根一，得到
\[
\frac{F_P(z)}{F_T(z)}=B_P(z)^{1/N}.
\tag{16}
\]
没有在这里任意选择一个对数常数或 $N$ 次根单位。

### 4.2 同一个覆盖同时消掉所有根

更具体地，
\[
\boxed{\qquad
A_P(z):=\frac{F_P(Nz)}{F_T(Nz)}
       =B_P([N]z)^{1/N}\ \in F(E)^\times .
\qquad}
\tag{17}
\]
其准确除子及规范为
\[
\operatorname{div}A_P=[N]^*(-P)-[N]^*(-T),\qquad
A_P(O)=1.
\tag{18}
\]

完整证明可直接检验周期。对于 $\gamma\in\Gamma$，
\[
\frac{(F_P/F_T)(z+\gamma)}{(F_P/F_T)(z)}
=\exp\{\eta(\gamma)(z_P-z_T)-(\eta_P-\eta_T)\gamma\}.
\tag{19}
\]
由于 $N(P-T)=O$，把 $\gamma$ 换成 $N\gamma$ 后，
指数是 $2\pi i$ 的整数倍。
故 $F_P(Nz)/F_T(Nz)$ 是 $\Gamma$-椭圆函数。
它的除子恰为 (18)；或在 Picard 群中看，
$[N]^*((-P)-(-T))$ 的类为 $N(T-P)=O$，所以该除子 principal。
再以 $O$ 值规范，和 (14) 一样下降到原 $F$。

因此不需要随 $p$ 增大覆盖，也不需要把系数域增到
$F(E[N^2])$。零极点确实落在 $E[N^2]$ 上，
但这个完整除子本身已定义于 $F$，这与所有点逐点有理是不同的。

还可给一个直接联系原除法函数的幂公式：
\[
A_P(z)^{N^2}
 =\frac{d_P}{d_T}
     \frac{\Psi_N(T+[N]z)}{\Psi_N(P+[N]z)}.
\tag{20}
\]
在原点按可去值取一。它说明 (17) 不是只存在一个
不带规范的抽象 elliptic function。

### 4.3 好位整性

在任何 $p\nmid2\cdot17$ 的好位，全部 $N$ 及 $N^2$ 挠点
都在有限 étale 好模型上保持互异。由已证 $r_P,r_T$ 的整单位性质，
(15)、(20) 在原点都为整单位，且其常数是一。
因为 $N$ 是 $p$-单位，多项式 $X^N-u$ 在根 $X=1$ 的导数为单位；
逐系数 Hensel 唯一性给
\[
B_P,\quad F_P/F_T,\quad A_P
 \in\mathcal O[[Z]]^\times
\]
在各自的整形式参数中成立。

这里对 $F_P/F_T$ 只断言其正式 germ 整，
不把它在原 $E$ 上误称为有理函数；
其完整有理性是在共同 $[N]$ 覆盖上由 (17) 得到的。
原 $F_P$ 自身及公共 theta 参考的半径/分母并未因此消失。

## 5. 完全恢复实际中央对角

由 (2)、(17)，逐个原标签都有
\[
\boxed{\quad
\Theta_P(Nz,Nw)
 =\Theta_T(Nz,Nw)\frac{A_P(z+w)}{A_P(z)}.
\quad}
\tag{21}
\]
所以原中央系数准确等于
\[
\boxed{\quad
N^{2m+1}d_m
 =[z^mw^m]\left\{
 N\Theta_T(Nz,Nw)
       \sum_{P\in\mathcal S}\frac{A_P(z+w)}{A_P(z)}
          -\frac{256}{w}\right\}.
\quad}
\tag{22}
\]
这里的 $N^{2m+1}$ 包括 theta 本身的一次伸缩，
不是只乘 $N^{2m}$。

(22) 在复域是准确恒等式；两边的正式系数属于同一个固定代数域，
因而也给每个目标 $p$ 的相同代数系数关系。
由于 $p\nmid N$，所显示的尺度是单位。
原旋转轨道及 $c_e$ 投影可对同一式逐项执行，全部标签保持不变。

这个接口的意义是将所有原轨道数据落到一个固定有限同源覆盖上的
有理比值之和，而不是把原 theta 的普通平方当成 Hadamard 对角。
它仍有真正二变量的 $\Theta_T$，并没有变成一个固定代数单位的对数。

## 6. 完整 neighbor 分配在真实 theta 比值中的形式

对任意上述同源，把参考 $T$ 一并运到 $\varphi T$，定义
\[
\mathcal R_{P,T}(z,w)
 =\frac{\Theta_P(z,w)}{\Theta_T(z,w)}
 =\left(\frac{B_P(z+w)}{B_P(z)}\right)^{1/N}.
\tag{23}
\]
右侧在 $w=0$ 为一；前述非 CM 的公共 $s_2zw$ 因子在比值中消失。

$B_P$ 的准确同源 norm 为
\[
\operatorname{Norm}_\varphi B_P
  =k_{\varphi;P,T}B'_{\varphi P,\varphi T},\qquad
k_{\varphi;P,T}=\prod_{Q\in\ker\varphi}B_P(Q),
\]
\[
k_{\varphi;P,T}^{\,N}
   =\kappa_{\varphi,T}/\kappa_{\varphi,P}.
\tag{24}
\]
这是 (14) 的除子范数及原点规范；(15) 核定了常数的方向。

令 $\varphi_G^*\omega_G=c_G\omega$，则全部 cyclic neighbors
满足准确的原点 germ 恒等式
\[
\boxed{\quad
\prod_G
 \mathcal R^{E/G}_{\varphi_GP,\varphi_GT}(c_Gz,c_Gw)
 =
 \mathcal R^E_{P,T}(z,w)^p\,
 \mathcal R^E_{pP,T}(pz,pw).
\quad}
\tag{25}
\]
证明先对 (24) 使用所有非零 $p$ 挠点的分拆，
得到 $B_P$ 的对应式；再分别在 $z+w$、$z$ 取值相除。
两边的 $N$ 次幂相等，且在 $w=0$ 都为一，
所以可能的根单位准确为一。这里 $pT=T$，因为 $p$ 为奇数。

(25) 给真实 theta 比值的完整乘法分配；
它不是对原 $256$ 项求和的同一个线性等式。
其中也没有漏掉一个可重新加入的 $\log k$：
(24) 的常数已在 $z+w$ 与 $z$ 的比值中准确抵消。

## 7. 哪个非线性步骤仍然保留着中央问题

写 $H_P(z)=\log F_P(z)$。由 (2)，
\[
\log\{\sigma(w)\Theta_P(z,w)\}
       =H_P(z+w)-H_P(z).
\tag{26}
\]
其 mixed derivatives 是同一个 $H_P$ 的单指标导数。
但是原 $\Theta_P$ 必须把 (26) 指数化，再除以 $\sigma(w)$；
原 $d_m$ 是这些每点结果相加后的对角。

这种差别在第一个非平凡中央系数已出现。
令 $U_P=H'_P(0)$。由原曲线的微分系统
\[
H''_P(0)=-x(P),\qquad H'''_P(0)=-2y(P),\qquad
w/\sigma(w)=1+O(w^4),
\]
得到
\[
\boxed{\qquad
[z\,w]\Theta_P(z,w)=-U_Px(P)-y(P).
\qquad}
\tag{27}
\]
线性对数数据在这一系数只给 $-y(P)$；
另一个项 $-U_Px(P)$ 来自指数化的乘积。
因此连 $d_1$ 都不是某个轨道对数导数直接相加。
这并不说 (26) 不包含足够数据，而是说必须保留每个标签的完整数据
及其非线性组合，不能仅保留 norm 的对数和。

类似地，(5) 的 $\kappa(W)$ 能重新携带 $W$ 导数，
但其准确式 (7) 已将这些导数写回原数据；
没有证明它们的完整中央组合非零。
(13)、(22)、(25) 是可继续研究的实际固定对象和完整关系。
要推进原 Sha 问题，仍须在这个原参考、原和及原对角上
取得无穷多个 $p$ 的非零控制；固定单位 $\log w_{\mathcal S}\ne0$
自身不能替代这一额外比较。

## 来源及规范

- 原 $256$ 点、$F_P$、$\Theta_P$ 和 $d_m$：
  [原反圆分 theta 对角](2026-11-12-anticyclotomic-theta-diagonal.md)，
  §§1–3；本文逐式使用其原规范。
- Kenichi Bannai, Shinichi Kobayashi,
  *Algebraic theta functions and the p-adic interpolation of
  Eisenstein–Kronecker numbers*, Duke Math. J.153(2010),229–295：
  Example1.9 的 reduced sigma、§1.3 式(15) 的准确平移、
  Theorem1.17 的双变量系数。
  [作者原文](https://arxiv.org/pdf/math/0610163)，
  所核 arXiv 版印刷 pp.10–11、15、17。
  本文没有把其 ordinary 整性定理套到 inert；
  §4.3 的比值整性由 (15)、(20) 的整 Kummer 根直接证明。
- 同源 norm、共同参考除子、全部 $\kappa$：
  [前篇完整证明](2026-11-12-all-isogeny-neighbors-kummer-norms.md)。
  (4)–(25) 的补偿、覆盖和 norm 比值由本文直接推导；
  没有用数值吻合替代固定函数恒等式。
