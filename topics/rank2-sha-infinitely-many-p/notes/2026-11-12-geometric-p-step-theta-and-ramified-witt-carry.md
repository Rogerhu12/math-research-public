# 完整 theta 的真实 p 同源分解：二次补偿、ramified 单位与平方 Frobenius

日期：2026-11-12。状态：以下 reduced-theta 同源公式、全部邻点乘积、
负对偶的两步分解及原轨道和的一步 Witt 公式均已证明。
它们没有证明实际中央行在无穷多个素数上非零。

本文接续
[原 theta 的平方 Frobenius](2026-11-12-original-theta-square-frobenius-and-witt-trace.md)
以及[真实同源邻点](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)。
主要新增是将完整两变量平方 Frobenius 分解到每一个真实 $p$ 同源，
保留目标非方格的 reduced-theta 二次补偿。
单个邻点只得到 ramified 极大理想中的深度，不能免费除以 $p$。

## 1. 任意奇次数同源的规范

令 $\varphi:E\to E'$ 为奇次数 $n$ 的可分同源，取不变微分
$\omega,\omega'$ 并记
\[
\varphi^*\omega'=c_\varphi\omega .
\]
在复均匀化中，$\varphi$ 是 $z\mapsto c_\varphi z$，
且 $c_\varphi\Gamma\subset\Gamma'$ 的指数为 $n$。
记格面积除以 $\pi$ 为 $A,A'$，则
\[
A'=|c_\varphi|^2A/n.
\tag{1}
\]

两端都使用真正的 reduced theta
\[
\theta_E(z)=e^{-s_2(E)z^2/2}\sigma_E(z),\qquad
\theta_E'(0)=1,
\tag{2}
\]
以及相应的平移 Kronecker theta。
即使源是方格，目标的 $s_2(E')$ 一般也不为零。

定义
\[
\boxed{\qquad
\psi_\varphi(z)=
 \frac{\theta_{E'}(c_\varphi z)}{\theta_E(z)^n}.
\qquad}
\tag{3}
\]
它是 $E$ 上的有理函数，准确有
\[
\operatorname{div}\psi_\varphi
=\sum_{Q\in\ker\varphi\setminus O}(Q)-(n-1)(O),\qquad
\psi_\varphi(z)=c_\varphi z^{1-n}+\cdots .
\tag{4}
\]

**证明。** reduced theta 的指数变换因 (1) 完全相同。
对 $\gamma\in\Gamma$，半特征 $\alpha(\gamma)$ 在非零
$\Gamma/2\Gamma$ 类取 $-1$，在零类取 $1$。
奇指数包含使
$c_\varphi\Gamma/2c_\varphi\Gamma\to\Gamma'/2\Gamma'$
为同构，所以
$\alpha'(c_\varphi\gamma)=\alpha(\gamma)=\alpha(\gamma)^n$。
故 (3) 对所有 $\gamma$ 双周期。零极点及首项给 (4)。
同除子且同首项的有理函数唯一；除子、$c_\varphi$ 定义于同源的
代数定义域，因此这个函数也在该域，不留下未指定的复常数。$\square$

用普通 $\sigma$ 改写 (3) 时，准确需要
\[
\psi_\varphi(z)
=e^{-(c_\varphi^2s_2(E')-ns_2(E))z^2/2}
 \frac{\sigma_{E'}(c_\varphi z)}{\sigma_E(z)^n}.
\tag{5}
\]
如果 $\wp_E$ 是相对于 $\omega$ 的 Weierstrass 函数，
比较 $z^2$ 项还给
\[
\boxed{\qquad
c_\varphi^2s_2(E')-ns_2(E)
=\sum_{Q\in\ker\varphi\setminus O}\wp_E(Q).
\qquad}
\tag{6}
\]
确实 (4) 可写成
$c_\varphi\prod_{\{Q,-Q\}}(\wp_E(z)-\wp_E(Q))$，
其相对 $z^2$ 系数是 $-\sum_{\{Q,-Q\}}\wp_E(Q)$；
普通 sigma 比值无这个二次项。
(6) 也直接证明本题目标 CM 邻点的这项补偿是代数的。

## 2. 原完整 Kronecker theta 的一步公式

本节另取 $(n,N)=1$，所以原非零 $N$ 挠点 $P$ 不在同源核中。
对该 $P$，写
\[
F_P^\theta(z)=
 e^{-z\bar z_P/A}\frac{\theta_E(z_P+z)}{\theta_E(z_P)}.
\]
那么
\[
\Theta_P(z,w)
=\frac{F_P^\theta(z+w)}
       {F_P^\theta(z)\theta_E(w)}.
\tag{7}
\]
由 (1)、(3)，$\varphi P$ 使用运输后的同一标签，准确有
\[
F_{\varphi P}^{\theta'}(c_\varphi z)
=(F_P^\theta(z))^n
      \frac{\psi_\varphi(P+z)}{\psi_\varphi(P)}.
\]
所以
\[
\boxed{\quad
\Theta'_{\varphi P}(c_\varphi z,c_\varphi w)
=\Theta_P(z,w)^n
 \frac{\psi_\varphi(P+z+w)}
      {\psi_\varphi(P+z)\psi_\varphi(w)} .
\quad}
\tag{8}
\]
指数补偿、目标 $s_2$ 和有限标签都在 (8) 中；
没有先把目标识别成源方格再删去一个二次指数。

固定源的三个有序二挠点 $T_0,T_1,T_2$。
取奇函数 $Z$ 满足
\[
\operatorname{div}Z=(O)+(T_0)-(T_1)-(T_2),\qquad DZ(O)=1.
\tag{9}
\]
在目标上运输同一除子，以 $D'Z'(O')=1$ 规范。
例如在带同一有序二级结构的 Legendre 模型中就是 $Z=-x/y$。
原曲线 $E_{17}$ 也可取 $Z=-x/y$，此时 $T_0=(0,0)$。

令 $U_P=Z(w)\Theta_P(z,w)$，则 (8) 成为
\[
\boxed{\quad
U'_{\varphi P}(\varphi z,\varphi w)
=U_P(z,w)^nD_{\varphi,P}(z,w),
\quad}
\tag{10}
\]
\[
D_{\varphi,P}=
J_\varphi(w)\frac{\psi_\varphi(P+z+w)}{\psi_\varphi(P+z)},\qquad
J_\varphi(w)=\frac{Z'(\varphi w)}
                 {Z(w)^n\psi_\varphi(w)}.
\tag{11}
\]
这里 $\varphi z$ 指加法参数 $c_\varphi z$；
作为有理函数则按真实同源拉回。

### 2.1 与已经固定的 Legendre 中心的明确换元

若需把原 $E_{17}$ 的坐标改成 $E_\lambda$、$\lambda=1/2$，
取 $s=\sqrt{17}$、$a=\sqrt{2s}$，则
\[
x_E=2s x_{\rm Leg}-s,\qquad y_E=(2s)^{3/2}y_{\rm Leg},\qquad
z_{\rm Leg}=a z_E .
\]
准确有
\[
Z_{\rm Leg}(az)=aZ_E(z)(1+s/x_E(z)),\qquad
\Theta_{\rm Leg}(az,aw)=a^{-1}\Theta_E(z,w).
\]
因此
\[
U_{\rm Leg}(az,aw)=(1+s/x_E(w))U_E(z,w).
\tag{12}
\]
这是固定有理单位 gauge，在所有目标素数处整且原点值一。
原参考 $T=(0,0)$ 在 Legendre 模型变成 $(1/2,0)$；
它不能被无说明地改成 Legendre 的 $(0,0)$。
(8)–(11) 在任一种规范中成立，只要全部二级标签及 (12) 一起运输。

## 3. 实际 p 邻点的整性只有 ramified 深度

现在取本题惰性 $p\ge7$，源为 canonical CM 曲线。
由真实邻点证明，所有 $p+1$ 个商在共同驯扩张
$B_1/B$ 上定义，$e(B_1/B)=p+1$。记其整环极大理想为 $\mathfrak m$。
源、目标微分均取各自良模型的整基。
对任一个 $p$ 商，
\[
v_p(c_\varphi)=1/(p+1).
\tag{13}
\]

首先，(11) 的公共因子有准确除子
\[
\operatorname{div}J_\varphi
=\varphi^*((T_0')-(T_1')-(T_2'))
       -p((T_0)-(T_1)-(T_2)).
\tag{14}
\]
$\ker\varphi$ 的全部点已消掉。
$\bar\varphi$ 是纯不可分的 relative Frobenius；
剩余支撑全部约化到非零二挠点，远离形式原点。
(14) 连同 $J_\varphi(O)=1$ 消去可能的整纤维竖直除子，
给
\[
J_\varphi\in\mathcal O_{B_1}[[Z_2]]^\times.
\tag{15}
\]

还须核定 $\psi_\varphi$ 在原 $P$ 及参考二挠点附近为单位。
源的非零 kernel 参数满足
$v_pZ(Q)=1/(p^2-1)$，故
$v_p\wp(Q)=-2/(p^2-1)$。
利用 §1 的准确多项式表达，对任一约化不为 $O$ 的 $P$，
\[
v_p\psi_\varphi(P)
=v_pc_\varphi-\frac{p-1}{p^2-1}=0.
\tag{16}
\]
其特殊纤维除子为零，所以约化是某个非零常数。
在有序二级标签的 Frobenius 识别下，
$Z'\circ\bar\varphi$ 与 $Z^p$ 有相同除子，因而差一个常数；
(15) 的原点值一核定该常数恰好等于 $\overline{\psi_\varphi}$。
故 $J_\varphi$ 的约化为一，而两个 $\psi_\varphi$ 之比也约化为一。
最终
\[
\boxed{\quad
D_{\varphi,P},D_{\varphi,T}
 \in1+\mathfrak m\,\mathcal O_{B_1}[[Z_1,Z_2]].
\quad}
\tag{17}
\]
这里 **没有**把 $\mathfrak m$ 换成 $p\mathcal O_{B_1}$。

即使取正式对数，也不能把深度直接写成 $\mathfrak m$。
取一致参数 $\varpi$、$v_p\varpi=1/(p+1)$，由 (17) 所能普遍保证的是
\[
\log D_{\varphi,P}\in
\varpi^{-1}\mathcal O_{B_1}[[Z_1,Z_2]].
\tag{17a}
\]
确实，对数第 $k$ 项的系数赋值至少
$k/(p+1)-v_p(k)$，其最小值是 $-1/(p+1)$，
在 $k=p$ 达到；$v_p(k)\ge2$ 时下界反而为正。
例如 $1+\varpi Z_2$ 的第 $Z_2^p$ 次对数系数就达到该下界。
这个例子只说明 (17) 本身的格代价，不声称实际 $D_{\varphi,P}$
必达到它。因 $D_{\varphi,P}(Z_1,0)=1$，这种可能的第一处分母
至少从垂直 $p$ 阶起。

同一个证明适用于后续负对偶：对于任一纯不可分约化的 degree-$p$
商，Weierstrass preparation 给
\[
v_pc_\varphi=\sum_{Q\in\ker\varphi\setminus O}v_pZ(Q).
\]
在 §1 的成对乘积中，$\wp(Q)$ 的赋值恰为 $-2v_pZ(Q)$，
所以 (16) 的相消仍然成立。无需把两步 kernel 的参数赋值误认为相同。

本节没有断言目标 $U'_{\varphi P}$ 自身整；
只有准确有理修正 (17) 在所指整环中整。

## 4. 全部 p+1 个邻点：公共常数精确相消

令 $G$ 跑遍源的所有阶 $p$ 子群，记 $c_G=c_{\varphi_G}$，
并置
\[
C_p^{\rm geom}=\frac{\prod_Gc_G}{p}.
\tag{18}
\]
非零 $p$ 挠点被这些 kernel 分拆，§1 的除子及首项给
\[
\boxed{\quad
\prod_G\psi_{\varphi_G}
       =C_p^{\rm geom}\Psi_p.
\quad}
\tag{19}
\]
由于 $v_p\prod_Gc_G=1$，这里 $C_p^{\rm geom}$ 是单位；
但其准确值仍保留，未任意设成一。

对运输后的 $Z_G$，同样有
\[
\boxed{\quad
\prod_G Z_G(\varphi_G W)
 =C_p^{\rm geom}Z(W)^pZ([p]W).
\quad}
\tag{20}
\]
证明对 (9) 的每个点分别计算拉回除子。
对任意二挠点 $T_j$，$\varphi_G^{-1}(\varphi_GT_j)=T_j+G$；
所有非零 kernel 元素各出现一次，零元出现 $p+1$ 次。
因 $pT_j=T_j$，得到
$\sum_G\varphi_G^*(\varphi_GT_j)=[p]^*(T_j)+p(T_j)$。
$O$ 亦同。故两侧除子相等；原点首项之比正是 (18)。

将 (19)、(20) 代入 (11)，两个 $C_p^{\rm geom}$ 准确相消：
\[
\boxed{\quad
\prod_G D_{\varphi_G,P}=D_{p,P}=D_{-p,P}.
\quad}
\tag{21}
\]
最后一个等式使用 $Z(-W)=-Z(W)$、$\Psi_{-p}=-\Psi_p$。
因此原完整 theta 的准确乘积式是
\[
\boxed{\quad
\prod_G U^{E/G}_{\varphi_GP}(\varphi_Gz,\varphi_Gw)
 =U_P(z,w)^p U_{-pP}(-pz,-pw).
\quad}
\tag{22}
\]
等价的未乘 $Z$ 形式为
\[
\prod_G\Theta^{E/G}_{\varphi_GP}(c_Gz,c_Gw)
 =(C_p^{\rm geom})^{-1}
       \Theta_P(z,w)^p\Theta_{pP}(pz,pw).
\tag{23}
\]
其 $w=0$ 的最高极部两边都为
$(\prod c_G)^{-1}w^{-p-1}$，再次核定常数。

(21)、(22) 包含公共参考本身，强于只对
$\Theta_P/\Theta_T$ 给乘法关系。
但它们仍是对邻点的乘积，不能把原 $256$ 标签的和改成这个乘积。

## 5. 任一 p 商与负对偶准确合成平方 Frobenius

固定一个 $\varphi:E\to E'$，令
\[
\psi=-\widehat\varphi:E'\longrightarrow E,\qquad
\psi\varphi=[-p],\qquad c_\psi c_\varphi=-p.
\]
全部 level 标签先随 $\varphi$、再随 $\psi$ 运输。
由 reduced-theta 比值 (3) 立即得到
\[
\boxed{\quad
\psi_\psi(\varphi R)\psi_\varphi(R)^p=\Psi_{-p}(R).
\quad}
\tag{24}
\]
源是原方格，且 $p^2$ 为最终次数；中间目标的 $s_2(E')$
在此确切相消，而不是被预先忽略。

同理，(11) 给
\[
\boxed{\quad
D_{-p,P}
 =D_{\varphi,P}^{\,p}
    \cdot(\varphi\times\varphi)^*D_{\psi,\varphi P}.
\quad}
\tag{25}
\]
这是完整两变量正式级数的准确分解，所有深度均保留。
每个实际 neighbor 都给同一个原 $D_{-p,P}$ 的这种分解。

两步各自只在 $1+\mathfrak m$ 中；
平方 Frobenius 已证明的
$D_{-p,P}\in1+p\mathcal O[[Z_1,Z_2]]$
是两步组合及其下降的结论，不是单步的免费整除。
本篇用实际代数同源和目标函数，不在 ramified 中间域上
另外假设一个 canonical Witt $\sigma$。

## 6. 固定参考后的原轨道和：一步的 Witt 公式

取同一参考 $T$，令
\[
\mathcal R_P=\Theta_P/\Theta_T,\qquad
\mathcal R'_{\varphi P}=\Theta'_{\varphi P}/\Theta'_{\varphi T},\qquad
C_{\varphi,P}=D_{\varphi,P}/D_{\varphi,T}.
\]
由 (10)，
\[
\mathcal R'_{\varphi P}\circ(\varphi\times\varphi)
   =\mathcal R_P^p C_{\varphi,P},\qquad
C_{\varphi,P}\in1+\mathfrak m\mathcal O_{B_1}[[Z_1,Z_2]].
\tag{26}
\]
所有这些比值在共同 $[N]$ 覆盖上是已固定的有理函数。

令 $\mathcal A=\sum_{P\in\mathcal S}\mathcal R_P$、
$\mathcal A_\varphi=\sum_{P\in\mathcal S}\mathcal R'_{\varphi P}$。
保持原全部标签相加，得到
\[
\boxed{\quad
\mathcal A_\varphi\circ(\varphi\times\varphi)
=\mathcal A^p+
   \sum_{P\in\mathcal S}\mathcal R_P^p(C_{\varphi,P}-1)
 -p\,\mathfrak C_p((\mathcal R_P)_P),
\quad}
\tag{27}
\]
其中
\[
\mathfrak C_p(X)=\big((\sum X)^p-\sum X^p\big)/p
\]
是同一个整数 Witt 交叉多项式。

(27) 不授权把中间那一项逐点除以 $p$ 后称为整：
$C_{\varphi,P}-1$ 一般只知属于 $\mathfrak m$。
先使用真实负对偶的 (25)，或对完整 Galois 轨道使用 (21)，
才得到前篇准确的平方 Frobenius 整公式。
前篇的
\[
\mathfrak C_{p^2}(X)
\equiv\mathfrak C_p(X^p)
  +p(\sum X^p)^{p-1}\mathfrak C_p(X)\pmod{p^2}
\]
正保留了两次 $p$ 次幂求和所产生的 carry。
没有因为两步最后落回原曲线，就消掉中间的非线性交叉项。

对固定 $P$，(21) 还给真正的域范数和对数迹：
\[
\operatorname{Norm}_{B_1/B}D_{\varphi,P}=D_{-p,P},\qquad
\operatorname{Tr}_{B_1/B}\log D_{\varphi,P}
       =\log D_{-p,P},
\tag{28}
\]
在把 $B$ 扩大到包含原标签且令全部邻点形成同一完整轨道后成立。
系数随真实邻点作 Galois 运输；对数取 $Z_2=0$ 为零的正式分支。
目标的 $\mathcal R$ 版本同样成立。

(28) 解释了为什么 $p+1$ 个单步 $\mathfrak m$ 修正的完整轨道
可以合成 $p$ 深度的平方修正。
若要求带权迹或除第二次 $p$，仍必须使用已固定的 ramified 整格，
不能由无权 norm 推出。

## 7. 对实际中央问题保留的内容

(10)、(21)、(25)、(27) 把三件事放进同一套规范：

1. 每一条真正 $p$ 同源及目标的 reduced-theta 二次补偿；
2. 公共参考的完整有理修正和所有邻点的准确乘积；
3. 原 $256$ 标签求和时不可省去的 Witt carry。

这允许把几何邻点的带权域迹与原 theta 的第二及更高 Witt 层
作实际比较。它没有把 cusp 的 $U_p$ 当成原点形式级数算子，
也没有把归一原函数在每个邻点重新任取一个积分常数。

原中央仍须按前篇
$N\Theta_T(Nz,Nw)\sum A_P(z+w)/A_P(z)-256/w$
取指定对角；本篇没有以 (21) 的乘积代替那个和。
若从 (28) 得到一个非零 norm 对数，还须证明它进入了这一
完整参考及真实 carry 所指定的中央行，才能用于原 Sha 判据。

## 来源

- Reduced theta 的半特征、面积变换和准确平移：
  K. Bannai, S. Kobayashi (2010),
  *Algebraic theta functions and the p-adic interpolation of
  Eisenstein–Kronecker numbers*，Example1.9、§1.3 式(15)，
  [作者原文](https://arxiv.org/pdf/math/0610163)。
  §1–2 的同源公式、二次补偿及常数均在上文直接核定。
- 实际全部 $p$ 邻点、共同驯扩域、微分和 kernel 参数估值：
  [真实同源邻点原证明](2026-11-12-critical-gauss-period-map-and-canonical-neighbors.md)；
  其中正式商模型依据 Jiu-Kang Yu (1995),
  *On the moduli of quasi-canonical liftings*，§3。
- 原固定 cover、参考与所有平方层：
  [固定 cover](2026-11-12-translated-kummer-units-and-original-theta-cover.md)、
  [平方 Frobenius](2026-11-12-original-theta-square-frobenius-and-witt-trace.md)。
  本篇没有援用目标 theta 的普通整性来证明 (17)。
