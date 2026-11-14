# 两条固定秩二曲线的负方向局部化与 E510 的严格证书

日期：2026-11-12。**状态：下述秩、分母乘积和联合密度一选择已证明。**

固定
$$
E_1=E_{17}:y^2=x^3-17x,\qquad
E_2=E_{34}:y^2=x^3-1156x,\qquad
F=\mathbf Q(\sqrt{-15}).
\tag{1}
$$
两条曲线均已严格证明秩二（R4、R118）。本篇证明：
对 R116 的输入素数集合
$$
\mathcal P_F=\{p\ne17:p\equiv1,17,49,53\pmod {60}\}
$$
中的相对密度一的 $p$，可以选取同一个合法小辅助素数 $\ell$，
使两条曲线的完整 Heegner 迹都非扭且不可 $p$ 除，两个正方向
局部像都非零，而**至少一个**负方向局部像非零。
采用 R123，辅助同余可准确取为 $\ell\equiv-1\pmod{1020p}$。

这个有限双曲线结论使用两个固定代数点的真正全局分母。
没有证明指定 Heegner 点在 $\delta=\sigma-1$ 商中的原始性，
因而不把主课题改为完成。

## 1. 第二条曲线的负扭曲解析秩恰一

第二条曲线的 $-15$ 二次扭曲为
$$
E_2^{(-15)}:y^2=x^3-260100x=x^3-510^2x.
\tag{2}
$$
其导子和根数为
$$
N_2'=4161600=2^6\,3^2\,5^2\,17^2,\qquad w(E_2^{(-15)})=-1.
\tag{3}
$$

这里可以避免重新做一个未说明的二进最小模型计算。
$-15\equiv1\pmod8$，故 (2) 在 $\mathbf Q_2$ 上与 $E_2$ 同构，
继承 R118 的导子指数 $6$ 和局部根数 $-1$。
在 $17$ 处，$-15\equiv2$ 是平方，仍与 $E_2$ 局部同构；
导子指数为 $2$，根数为 $+1$。在 $3,5$ 处，(2) 的短模型
$v_q(a_4)=2$、$v_q(\Delta)=6$，Tate 算法为 $I_0^*$，导子
指数均为 $2$。这两处也可以视为原好约化曲线的分歧二次扭曲；
局部根数分别是 $(-1/3)=-1$、$(-1/5)=+1$。
无穷处根数 $-1$，得到 (3)。坏位的局部 $L$ 因子均为 $1$。

写 $L(E_2^{(-15)},s)=\sum a_n n^{-s}$，并令
$c=\sqrt{N_2'}/(2\pi)$。权二模形式的 Mellin 变换及根数 $-1$
给出准确公式
$$
L'(E_2^{(-15)},1)
=-2\sum_{n\ge1}\frac{a_n}{n}\operatorname{Ei}(-n/c).
\tag{4}
$$
这与 R103 的同一规范一致：先在 $t=1/\sqrt{N_2'}$ 分开
Mellin 积分，利用函数方程，再在 $s=1$ 求导即可。

用 Hasse 界、Hecke 递推得到 $|a_n|\le d(n)\sqrt n\le2n$。
又 $-\operatorname{Ei}(-x)\le e^{-x}/x$，所以截断到 $M$ 的
绝对尾项不超过
$$
\frac{4c}{M+1}
\frac{\exp(-(M+1)/c)}{1-\exp(-1/c)}.
\tag{5}
$$

[可复算脚本](../scripts/check-e510-minus15-twist.py) 使用两套独立
整数系数算法：有限域点数，以及 $E_0:y^2=x^3-x$ 的 Gaussian
CM 字符乘二次角色 $(510/q)$。后者在 $q=a^2+b^2$、
$a$ 奇、$b$ 偶、$a+b\equiv1\pmod4$ 时给 $a_q(E_0)=2a$；
在 $q\equiv3\pmod4$ 时为零。两套 $a_n$ 至 $M=16000$
逐项相等，随后以 Arb 的 160-bit 球算术计算 (4)。
结果为
$$
\begin{aligned}
L'(E_2^{(-15)},1)
&\in 13.6418894779226046206
       +[-5.53,5.53]\cdot10^{-20},\\
\text{(5)}&<1.043\cdot10^{-20}.
\end{aligned}
\tag{6}
$$
特别地 $13<L'<14$。这是包含无限尾项的严格非零证书，
不是将一个近似小数当成解析秩。

因此 (3)、(6) 和 Gross--Zagier--Kolyvagin 定理给
$$
\operatorname{rank}E_2^{(-15)}(\mathbf Q)=1,\qquad
\Sha(E_2^{(-15)}/\mathbf Q)\text{ 有限}.
\tag{7}
$$
R103 已给 $E_1^{(-15)}$ 的同样结论。所以除固定有限多个 $p$ 外，
两条曲线在 $F$ 上的负号 $p$-Selmer 维数都为 $1$。

## 2. 两个实际负点与固定共同曲线

直接代入可核
$$
(121,1144)\in E_1^{(-15)}(\mathbf Q),\qquad
(960,25200)\in E_2^{(-15)}(\mathbf Q).
\tag{8}
$$
第一个点在好素数 $11$、第二个在好素数 $7$ 约化为非零二挠点，
但本身的 $y$ 坐标非零；好约化的 $\mathbf Q_q$ 正式群在
$q>2$ 没有挠点，故有理挠点的约化在这里单射。
于是 (8) 都非扭。等价地，可直接应用 Nagell--Lutz：
两个 $y$ 分别含不整除曲线判别式的素数 $11$、$7$。

令 $d=\sqrt{-15}$。将 (8) 经二次扭曲同构映回 (1)，得到
$$
R_1=\left(-\frac{121}{15},\frac{1144d}{225}\right)\in E_1(F)^-,
\qquad
R_2=(-64,112d)\in E_2(F)^-.
\tag{9}
$$
取一个固定 $\eta$ 满足 $\eta^4=68$，令 $K=F(\eta)$。同构
$$
\jmath:E_2\longrightarrow E_1,\qquad
(x,y)\longmapsto(x/\eta^2,y/\eta^3)
\tag{10}
$$
把 $R_2$ 送到
$$
R_2^*=\left(-\frac{64}{\eta^2},\frac{112d}{\eta^3}\right).
\tag{11}
$$
$X^4-68$ 在 $F$ 上仍不可约：其分裂域只在 $2,17$ 分歧，
而 $F$ 在 $3,5$ 分歧，所以 $F$ 与该分裂域不相交。
特别地 $K/F$ 有固定 $F$ 的自同构 $\eta\mapsto-\eta$；
它固定 $R_1$ 并把 $R_2^*$ 变成其负点。
若 $aR_1+bR_2^*$ 为挠点，对它施加此自同构后加减，得
$2aR_1$ 和 $2bR_2^*$ 都为挠点。由 (8) 得 $a=b=0$。
因此
$$
R_1,\ R_2^*\quad\text{在 }E_1(K)/E_1(K)_{\rm tors}
\text{ 中整数独立}.
\tag{12}
$$

## 3. 同一辅助位的两个负方向确实进入同一小群

令 $\ell\equiv-1\pmod {1020}$ 为好素数。它在 $F$、
$\mathbf Q(i)$ 都惰性。又
$$
\left(\frac{68}{\ell}\right)
=\left(\frac{17}{\ell}\right)
=\left(\frac{-1}{17}\right)=1.
\tag{13}
$$
因为 $\ell\equiv3\pmod4$，$\mathbf F_\ell^\times$ 中四次幂的
像恰等于平方的像，故可在 $\mathbf F_\ell$ 选择一个
$\eta^4=68$ 的根。选择 $K$ 上与这个根相容的 $\ell$-上方素位。
这一步允许素位随 $\ell$ 选择；后面的全局范数包含所有这些素位。

在这个约化中，(10) 在 $\mathbf F_\ell$ 上定义，而 $d$ 被
$\operatorname{Frob}_\ell$ 反号。因此 $\overline R_1$、
$\overline R_2^*$ 同时属于
$$
H_\ell=\ker\bigl(1+\operatorname{Frob}_\ell:
 E_1(\mathbf F_{\ell^2})\to E_1(\mathbf F_{\ell^2})\bigr).
\tag{14}
$$
$H_\ell$ 是非平方二次扭曲的 $\mathbf F_\ell$ 点群。
由于 $a_\ell(E_1)=0$，其阶恰为 $\ell+1$。

假设 $\ell+1=pu$、$p\nmid u$。则 $pH_\ell$ 的阶恰为 $u$。
若 (9) 的两个局部模 $p$ 像都为零，它们在 (14) 中均属于
$pH_\ell$。这里从全群的 $p$ 倍点到负群的 $p$ 倍点没有遗漏：
若 $pT=R$ 且 $\operatorname{Frob}R=-R$，取整数 $a,b$ 使
$2a+pb=1$，则
$$
T_-=a(T-\operatorname{Frob}T)+bR\in H_\ell,\qquad pT_-=R.
\tag{15}
$$

准确地，若 $r_{j,-}$ 表示 $E_j/F$ 的负号通常 $p$-Selmer 群
在 $\lambda\mid\ell$ 的局部像维数，则 $r_{j,-}\in\{0,1\}$，
并且
$$
r_{1,-}=r_{2,-}=0
\quad\Longrightarrow\quad
\overline R_1,\overline R_2^*\in pH_\ell.
\tag{16}
$$
反过来，只要这两个固定点之一的模 $p$ 像非零，对应
$r_{j,-}=1$；不需要它预先是整个 Mordell--Weil 群的基。

## 4. 一个非零固定整数吸收全部同时消失的辅助素数

取 $N_u=\lceil\sqrt u\rceil$。若 (16) 成立，
$(N_u+1)^2>u$ 个点
$$
a\overline R_1+b\overline R_2^*,\qquad 0\le a,b\le N_u
$$
都在阶 $u$ 的群 $pH_\ell$ 中。鸽巢原理给一个非零整数向量
$(a,b)$，满足
$$
|a|,|b|\le N_u,\qquad
\overline{aR_1+bR_2^*}=O.
\tag{17}
$$
由 (12)，$T_{a,b}=aR_1+bR_2^*$ 是非扭、非零的实际全局点。

令 $\mathfrak d_{a,b}$ 为 $x(T_{a,b})\in K$ 的分母理想，即
其在素理想 $\mathfrak q$ 的指数为
$\max(0,-v_{\mathfrak q}x(T_{a,b}))$。写
$$
D_{a,b}=N_{K/\mathbf Q}(\mathfrak d_{a,b})\in\mathbf Z_{>0}.
\tag{18}
$$
在所选好位，(17) 强迫 $x(T_{a,b})$ 有负赋值，所以
$\ell\mid D_{a,b}$。没有把局部正式群除法当成全局点除法：
这里的 $T_{a,b}$ 是由两个固定点的整数线性组合定义的。

固定曲线上的 Weil 高度与典范高度比较，以及典范高度的二次性，
给一个不随 $a,b,\ell,p$ 变化的常数，使
$$
\log D_{a,b}\le[K:\mathbf Q]h(x(T_{a,b}))
\ll a^2+b^2+1.
\tag{19}
$$
对 $U\ge1$ 定义真正非零的整数
$$
\mathscr D(U)=
\prod_{\substack{|a|,|b|\le\lceil\sqrt U\rceil\\(a,b)\ne(0,0)}}D_{a,b}.
\tag{20}
$$
求和 (19) 得
$$
\log\mathscr D(U)\ll U^2.
\tag{21}
$$
因此，对任意 $u\le U$，两个负方向同时消失都强迫
$$
\ell\mid\mathscr D(U).
\tag{22}
$$
这是两个不同曲线的真实点经固定同构合并所得的全局整数；
没有在秩一群中虚构第二个独立点。

## 5. 相对密度一的联合选择

固定 $32/17<L<2$，取 $p\in(X,2X]\cap\mathcal P_F$，
以及 R110、R123 的候选
$$
\ell\in(X^L,2X^L],\qquad
\ell\equiv-1\pmod {1020p}.
\tag{23}
$$
充分大 $X$ 时，$\ell+1<p^2$，故 $v_p(\ell+1)=1$，并且
$$
\tfrac12X^{L-1}<u\le U_X:=\lceil2X^{L-1}+1\rceil.
\tag{24}
$$
一个这样的 $\ell$ 至多对应本区间一个输入 $p$。

由 (21)、$\log\ell\ge L\log X$，两个固定负点同时消失的
候选总数至多
$$
O\left(\frac{X^{2L-2}}{\log X}\right).
\tag{25}
$$
Fouvry（2013），Lemma 7 给除 $o(X/\log X)$ 个输入外，
每个 $p$ 有 $\gg X^{L-1}/\log X$ 个候选。因此全部候选
都满足 (16) 的输入至多 $O(X^{L-1})=o(X/\log X)$。

同一结论可与两条曲线的下列坏集合同时相交后保留。

### 5.1 两个正方向

R121 对 $E_1$ 的两个固定独立有理点给出
$O(X^{2L-2}/\log X)$ 的正方向零像坏候选。
对 $E_2$ 使用 R118 式 (2) 的两个独立有理点，完全相同的
整数分母证明给同阶界。有限并不改变 (25) 的数量级。
故可同时要求
$$
r_{1,+}=r_{2,+}=1.
\tag{26}
$$

### 5.2 两条曲线的真实完整 Heegner 迹

R116、R123 对 $E_1$ 已给指定非零的固定普通 Mellin 分支、
稀疏零指标和非零系数乘积。对 $E_2$，其证明有如下完整接口，
不能照搬旧曲线的挠群指数：

1. **实际固定挠群。** 有
   $$
   E_2(F^{\rm ab})_{\rm tors}=E_2[4].
   \tag{27}
   $$
   对 prime-to-$61$ 挠点，取 $F(i)$ 中 $61$ 的 Frobenius；
   $61$ 在 $F$ 中分裂，$E_2$ 的 CM Frobenius 为
   $-5\pm6i$。与一个固定 $F$、交换 $i,-i$ 的 Galois 元作
   交换子，因 $F^{\rm ab}/F$ 阿贝尔，得到 $[12i]T=0$。
   在 $41$ 处，$41$ 在 $F$ 惰性，在 $\mathbf Q(i)$ 分裂；
   $E_2$ Frobenius 为 $-5\pm4i$，故其平方属于 $G_{F(i)}$。
   同样得到 $[80i]T=0$，适用于 prime-to-$41$ 挠点。
   两式的 gcd 为 $4$；$41$、$61$ 初级部分分别被另一式排掉。
   因而所有挠点被 $4$ 杀掉。反向，
   $E_2[4]\subset\mathbf Q(i,\sqrt2,\sqrt{34})\subset F^{\rm ab}$，
   可由 $E_2$ 是 $E_0$ 的 $34$ 二次扭曲及其二分点公式直接验证。

2. **固定映射与原始点。** 在 $X_0(3N_{E_2})$ 上取
   $\Phi_2=\pi_2d_1+\pi_2d_3$，$\pi_2(\infty)=O$。
   R105 的分歧理想恒等式只依赖 $F$，仍给
   $\Phi_2(z_c)=(1+\tau_3)P_2[c]$、$\tau_3^2=1$。
   最大阶类群迹为扭点，否则原始 Heegner 点定理将迫使
   $\operatorname{rank}E_2(F)=1$，与 R118 矛盾。
   由 (27)，取
   $$
   \Psi_2=[4]\Phi_2
   \tag{28}
   $$
   即在全部八个最大阶 CM 中心为零。这里使用 $4$，不是旧证明的 $2$。

3. **同一 Cornut/ST 机制。** 仍固定 $q=61$。
   它与 $3N_{E_2}\cdot15$ 互素、在 $F$ 主分裂，
   且 $a_{61}(E_2)=-10$，为普通约化。
   R116 的固定 ST 证明因而给整有界测度及精确矩
   $\kappa_c^m m!b_{2,c,m}$，其原始 Gauss 公式是实际
   $4(1+\tau_3)P_2[61^n]$ 的全 tame/类群迹。
   若指定 $x^{-1}$ 分支恒零，整数投影 $61-N$ 迫每个新层
   全迹扭性；旧层用原始递推逐层消去。初层系数分别为
   $a_{61}-2=-12$ 和 $61-1=60$，以后是
   $\operatorname{Tr}Z_n=a_{61}Z_{n-1}-Z_{n-2}$。
   于是全部全迹为扭，违反 Cornut（2002）的原始主定理。
   所以每个实际中心的指定分支非零。

4. **真实零指标与高度。** R123 的完整解析引理逐个应用于上述
   非零分支。对 $60\mid m$，若 $h_{2,c,m}=m!b_{2,c,m}=0$，
   则指定分支在 $62^m-1$ 的赋值至少 $m-1$。所以每个固定比例
   区间中，任一中心的零指标只有 $O(1)$ 个；与 $E_1$ 的有限
   中心取并仍是 $O(1)$。
   对其余指标，固定有限多项式 GM/period 逆变换/椭圆对数
   系统给共同 $A,d$，使 $A^{dm+1}h_{2,c,m}$ 为固定数域整数，
   范数对数 $O(m\log(m+2))$。这正是 R116 的直接微分系统证明，
   对新的固定映射 (28) 不增添随 $p,\ell$ 变化的变量。
   R114 的真实 $U$ 迹在辅助位以 $[4]Q_{2,p,\ell}$ 代替 $[2]Q$，
   首系数仍为 $u\,b_{2,c,u}$，故其为单位时 $Q_{2,p,\ell}\ne O$。

由于 (23) 自动给 $60\mid u$，现在不再加入未知的 $61$ 次幂。
由 (24)，零指标的 $O(1)$ 种 $u$ 至多贡献 $O(X)$ 个坏候选。
其余指标取两曲线全部有限中心的非零范数乘积，仍只有
$O(X^{2L-2})$ 个首项非单位候选。因 $L>32/17>3/2$，
$O(X)$ 被这个界吸收。把两曲线全部固定坏位加入例外集，有限并
后的坏候选仍为 $O(X^{2L-2})$。
排去全部候选坏的输入只损失
$O(X/(\log X)^2+X^{L-1}\log X)=o(X/\log X)$。
因此可同时要求
$$
Q_{j,p,\ell}:=\operatorname{Tr}_{U}(1+\tau_3)P_j[\ell]\ne O
\qquad(j=1,2).
\tag{29}
$$
两个点都满足 $N_pQ_j=0$。由 R107、(27) 的挠群界及奇数 $p$，
它们均非扭。实际高度仍为
$\widehat h(Q_j)\ll u^2\log\ell=o(p^2)$；Baker 的固定
$F^{\rm ab}$ 正高度下界分别应用于两曲线，遂给
$$
Q_{j,p,\ell}\notin pE_j(F[\ell])\qquad(j=1,2).
\tag{30}
$$

综上，对相对密度一的 $p\in\mathcal P_F$，可以同时得到
(26)、(29)、(30)，并且
$$
\boxed{\max\{r_{1,-},r_{2,-}\}=1.}
\tag{31}
$$
所有常数、曲线、点和数域在让 $p,\ell$ 变化之前固定。

## 6. 对 δ 层的准确作用

对 (31) 选中的那条曲线，(7)、R103 使 $s_-=1$（删去固定有限
多个 $p$）；R119 的 Nekovář 整角色证明也同样适用于 $E_2$，
因为其 CM 域仍是 $\mathbf Q(i)$，不在 $F[\ell]$ 中。
于是实际范数为零阿贝尔簇的 Mordell--Weil 完成是
$\mathbf Z_p[\zeta_p]$ 秩一，整个 Sha 有限。
实际 Heegner 点写为
$$
Q_j=\delta^{a_j}\epsilon_jw_j,\qquad 0\le a_j\le p-2.
$$
已证的局部符号与有限 Cassels--Tate 分层计算遂对选中曲线给
$a_j$ 为偶数，以及相应有限 Sha 的偶长度、偶重数限制。

本篇没有推出 $a_j=0$。两个曲线的负方向不能同时消失，
也不表示两个实际 Heegner 点不能同时有正的偶数增广指数。
新增的全局整数预算支付的是 (31) 的联合局部化条件，
不是以局部正式群的大小替代 $\delta$ 原始性。

## 来源与已证明接口

- 解析秩证书的 Mellin 规范与双系数算法：R103 及其完整证明；
  本篇 (2)--(6) 已对新曲线重新计算，并有独立脚本。
- J. Desjardins（2020），*Root number of twists of an elliptic curve*，
  JTNB **32**, 73--101，Proposition 3.1、Lemma 3.8：
  [原文](https://www.numdam.org/item/JTNB_2020__32_1_73_0.pdf)。
- C. Cornut（2002），*Mazur's conjecture on higher Heegner points*，
  Invent. Math. **148**, 495--523，引言主定理、§4.1 Lemma 4.2：
  [作者发表版](https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf)。
  已重新核对其对 $E_2,\pi_2,F,q=61$ 的全部输入。
- E. Fouvry（2013），*On binary cyclotomic polynomials*，
  ANT **7**, 1207--1223，Lemma 7：
  [原文](https://msp.org/ant/2013/7-5/ant-v7-n5-p07-p.pdf)；
  其量词和固定模数因子已在 R110 核定。
- R114、R116 给真实 period jet、ST、Cornut 分支和微分系统高度；
  §5.2 逐项列出新曲线所需的变动。
- [R123 完整稀疏零指标证明](2026-11-12-sparse-zero-moments-and-explicit-auxiliary-modulus.md)
  使 §5 可采用明确模数 $1020p$，并完整控制零指标。
- R118 给 $E_2$ 的两个独立有理点；R121 给正方向分母乘积；
  本篇 (17)--(25) 是固定共同数域上两条负方向的新整数论证。
- R119 与[有限范数一 Sha 的实际分层](2026-11-12-finite-norm-sha-delta-layers-and-local-signs.md)
  给 §6 的整系数结论。整个主问题仍须指定的 $a_j=0$。
