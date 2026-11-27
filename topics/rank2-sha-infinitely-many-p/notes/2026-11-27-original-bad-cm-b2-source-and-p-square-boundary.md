# 原坏 CM 点的 b=2 读者、实际同源来源及 p² 向外边界

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。
状态：下列坐标、算子及有限对应身份均为手证；§5只消费已完成的公开回执，
不运行新数学。本篇不把 Kriz 书中尚待核的连续性接合当作已付，也不称其
原定理为假。

本篇保同一原 finite level、微分、Kodaira–Spencer 基及全部图权。
$b=2$给出一个真实可运输的读者，但其 source 也必须一起运输；
单独改变形式变量不能证明它就是原 fixed-base 图的读数。

## 1. 好点读者的准确 b=2 拉回

设 $p>2$，使用书中的右作用与拉回约定。写
$$
g_1=\begin{pmatrix}p&0\\0&1\end{pmatrix},\qquad
g_2=\begin{pmatrix}1&0\\0&p\end{pmatrix},\qquad
y'=yg_1,\qquad
Q_b=\exp\!\left(\frac{z_{\rm dR}-\theta(z_{\rm dR})}{p^b}\right).
\tag{1}
$$
原惰性 CM 点及其好点满足 $|\hat z(y)|=1$、$|\hat z(y')|=p$。
由真实 period 变换及 $g_1g_2=pI$，
$$
g_1^*Q_b=Q_{b+1},\quad g_2^*Q_b=Q_{b-1},\qquad
g_1^*\omega_{\rm can}=\omega_{\rm can},\quad
g_1^*dz_{\rm dR}=p^{-1}dz_{\rm dR}.
\tag{2}
$$
最后两式使用同源拉回的实际基。等价地，$g_2^*$在
$\omega_{\rm can}$与$dz_{\rm dR}$上都乘$p$；中心$pI$在
$\omega_{\rm can}$上乘$p$，在 period 比值上不动。
因此这里没有用$\omega^{k+2j}$错误代替
$\omega^k\otimes(dz_{\rm dR})^j$来省去 determinant 费用。

设 $F$在$y'$的$Q_1$展开有界，并满足 Theorem6.21 的其余假设。
记$\flat_b$为在$Q_b$上减去完整$\mu_p$平均。将系数、定义域和来源
一同拉回，令$\widetilde F=g_1^*F$。则
$$
g_1^*(\flat_1F)=\flat_2\widetilde F,\qquad
g_1^*(\theta_k^jF)=p^j\theta_k^j\widetilde F .
\tag{3}
$$
第一式逐个$\mu_p$字成立；第二式可以由完整 Maass–Shimura
连接或由$z_{\rm dR}$及其 horizontal 伴随同时缩放$1/p$逐项核得。
因此
$$
\bigl((p\theta_k)^j\flat_1F\bigr)(y')
=
\bigl((p^2\theta_k)^j\flat_2(g_1^*F)\bigr)(y).
\tag{4}
$$
左边已付的连续性确实运输到右边。若左族在$U$上已付，则右族在
$Ug_1^{-1}$上已付；仅在 stalk 上使用时，亦须拉回相应 stalk。

(4)的来源是$g_1^*F$：它是原$y$出发的真实 cyclic $p$邻点来源。
它并非原$F$在同一点仅换了一个变量名。

## 2. 回原 source 的缺口不能由坐标等式删除

若要回到一个预先固定的原来源$F_0$，则必须在好点支付实际
$g_2^*F_0$的$Q_1$有界展开及其$\flat_1$。
此时
$$
g_1^*g_2^*F_0=(pI)^*F_0
\tag{5}
$$
才返回原 source 的中心同源拉回。这个额外有界性与$\flat$身份
不由$F_0$在$y'$的有界性推出；它正是原点位/定义域门的一部分。

根坐标还给出一个有用的严格核对。若
$A(Q_1)\in\mathcal O_{\mathbf C_p}[[Q_1-1]]$全有界，则
$$
\flat_{Q_2}\bigl(A(Q_2^p)\bigr)=0.
\tag{6}
$$
因为对每个$\zeta\in\mu_p$均有$(\zeta Q_2)^p=Q_2^p$，
且有界性保证这个平均确实可以作用到全级数。
(6)不能扩大到一个仅在更小圆盘收敛的$Q_1$展开。
例如$A(Q_1)=Q_1^{1/p}$的选定局部分支在代入$Q_1=Q_2^p$后
在$1$附近成为$Q_2$；其$Q_2$上的$\flat$非零。
不能将$\zeta$平移移过该未在整个所需圆盘收敛的旧展开。
所以$b=2$的真实用途应是证明新的全系数与实际对应，
不是从形式根关系自动得到通常$p$剔除。

## 3. 同一 p² 分支上的 incoming/outward 完整边界

以下只使用原实际$\mathcal H=H^1_{\rm dR}$-值 Coleman primitive
$G$，以及真正 degree$p^2$同源
$\lambda_D:E\to E_D$和对偶$\widehat\lambda_D$。
所有原 full level 标签沿这两个同源运输。
定义
$$
I_D=G(E_D)-\frac{\widehat\lambda_D^*}{p^2}G(E),
\qquad
O_D=G(E)-\frac{\lambda_D^*}{p^2}G(E_D).
\tag{7}
$$
这里$I_D$是高导子底曲线$E_D$的 canonical incoming 剔除；
$O_D$是固定原$E$加$D$以后，向外退化映射定义的剔除。
本题实际中心$p^2$的 diamond 为$1$。
由于$[p^2]^*$在$\mathcal H$上是$p^2$，逐支有
$$
\boxed{\quad
O_D=(1-p^{-2})G(E)-\frac{\lambda_D^*}{p^2}I_D .
\quad}
\tag{8}
$$
证明只需展开右边，并保留
$\lambda_D^*\widehat\lambda_D^*/p^4=p^{-2}$。
特别，Fricke/对偶同源没有把 incoming 与 outward 无成本互换：
它准确留下原$G(E)$的边界项。

原全$p^2$范数笔记已经支付（和不除以项数）
$$
\sum_D\frac{\lambda_D^*}{p^2}G(E_D)=\frac{p+1}{p}G(E),
\qquad
\sum_D\frac{\lambda_D^*}{p^2}I_D=0,
\quad \#D=p(p+1).
\tag{9}
$$
其中使用完整
$\mathsf B_1^2=\mathsf B_2+(p+1)\langle p\rangle/p$、
$\mathsf B_1G=0$、$\langle p\rangle G=-G$。
于是(8)给
$$
\sum_DO_D=p(p+1)(1-p^{-2})G(E).
\tag{10}
$$
(8)比只比较两个和的 Euler 因子更精确：每条相同的$D$与同一
level/微分均已保留。

## 4. 全有限图读者真正保留的项

令$\varphi_i:A\to E_i$是原 prime-to-$p$图，并保原修正图、外系数、
Artin 权、corestriction及最高 projector。因为每个式子在
$\mathcal H(E_i)$中成立，对它施同一
$\langle\varphi_i^*(-),\omega_A\rangle$及所有既有有限和，仍为等式。
实际修正图推前的 degree 也须从$c$改成$cp^2$，不能只移动未修正图。

因此，原 full54 情形的 fixed-base 读数严格仍是
$$
\mathcal A^{\rm out}_{j,p}
=(p^2-1)\mathcal I_{j,p},\qquad
a_{j,p}^{-1}\mathcal A^{\rm out}_{j,p}
=(p^2-1)h_{j,p}.
\tag{11}
$$
这是原 proper 自然性给出的身份，不需要当前重审的全权插值。
相反，将好点 incoming 连续读者作完整 imprimitive 范数只得到(9)的零；
若要由它得到(11)，必须支付(8)的原$G(E)$项。
本篇不把(11)再与某个 Newton regularization 相认。
对新 psi4 的18×2图亦须保其实际图权和杯积基，不能复制旧full54的
Artin常数。

## 5. 当前正权审计已经不是空非零假设

公开单次审计的真实回执为：

- source：`38d4107ce0fa11b0fdf5c99a6df6596d6c3c32f5`；
- run/job：`46073583710 / 140756005342`；
- $p=227,\ u=1,\ n=51526,\ n+2=51528$，两$q=z^6$读数均在$q^{8587}$；
- 固定辅助域$\mathbf F_{65537}$中，两个完整来源系数均非零；只引用原run，不另存可重算结果表；
- 全 Weierstrass 一阶恒等、两指数的全窗重构均 PASS；
- script：7527 B，SHA256
  `95c9e8892f8b6b834cb6ecc1ad64bd38775cfce8eb719c4e0061eb3bed8f30b2`；
- stdout：1239 B，SHA256
  `b74f221e90348e596670facaa5d0f0e868ee0e7c4351565d8ed477725ee8019f`。

两个辅助域残余证明相应有理系数在特征零非零；没有把它们当成模227
单位。所有所用形式分母的正因子均小于65537，来源固定分母亦素于65537。
所以纯 Newton 来源的$R_{{\rm can},227}(226)\ne0$已真实支付。

这使此前 digit lemma 的“存在一个非零正整数值”不再是空条件。
仍须精确核验实际$q_{p,n}$、原toric sum和连续读者的接合；
本篇不由辅助域证书宣布书中定理为假，也不据此恢复已暂停的cross消费。

## 来源与范围

- 本课题
  [digit audit](2026-11-27-original-psi4-common-factor-digit-and-continuity-audit.md)；
  原未平方双核来源及新 psi4 coherent/Newton 笔记。
- [原全p²范数](2026-11-27-original-inert-p-square-full-norm-and-endpoint-zero.md)
  §§3–6，完整$\mathsf B_1/\mathsf B_2$、两CM微分及各旧项；
  [原fixed-base向外剔除](2026-11-27-original-inert-fixed-base-p-square-depletion-and-fp-parameter.md)
  §§2–5，proper图与原整参数。
- D. J. Kriz, AMS212 (2021), Proposition7.7、(7.13)、Theorem6.21、
  Definition7.19及Corollary7.21。坐标缩放亦可直接核作者
  [2018全文](https://arxiv.org/pdf/1805.03605) (184)–(185)；
  不使用该旧版的不同period估值替代书版。
