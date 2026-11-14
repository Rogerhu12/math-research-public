# 整循环二次不变量、真实二阶矩与有理参数提升

日期：2026-11-12。**已证明；未证明这些实际测试无穷次非零。**

本篇把 R142/R154 的原二阶矩改写为两个标量值，因而不再
要求源互反函数为简单零。先在原普通 canonical-lift 族上
构造规范的整刚性函数；最后另给适用于 R130/R139 原输入的
全局有理参数版本。两个版本的整性和相互比较分别证明。
有理商上的刚性函数值并不因此成为一个固定有理数。

## 1. 保留的实际曲线、覆盖和完整迹

前六节沿用 R154、R157 的
$$
 E=389\mathrm a1,\qquad
 \pi:X_0(389)\longrightarrow E,\qquad
 \Psi_D=[t_0]\sum_{d\mid D_0}\pi d_d .
 \tag{1}
$$
取固定 Néron 微分，写
$\pi^*\omega_E=c_\pi f(q)\,dq/q$。
删去固定的坏约化、层数、$t_0c_\pi$ 素因子，取 $p\ge7$。
保留 R146/R150/R154 对原 $F,p,\ell,Q_D$ 的全部输入：
原源在 $p$ 普通且为 canonical lift，$p$ split $F$，
$a_p(E)\not\equiv1\pmod p$，$\ell+1=pu$、$p\nmid u$，
以及原环类域中的指定生成元 $\tau$。对 Sha 的最后推论还
保留 R146 的全像及原整数 Heegner 系统假设。

在 R154 的完整 projective ell 层模型上，令
$T/U=\Gamma=\langle\tau\rangle=C_p$。原 U 轨道始终包含
两个 $U_0$ 半轨道；已由 $W_R$ 商吸收的类群和也始终保留。
原特征 p 行和整数群环元为
$$
 \begin{gathered}
 B=\sum_{v\in Uv_0}h_v,\qquad
 n=N_\Gamma B=a_\ell(E)\widetilde g_{D,p},\\
 D_r=\sum_{j=0}^{p-1}\binom jr\tau^j,\qquad
 A=D_1B,\qquad F_2=D_2B .
 \end{gathered}
 \tag{2}
$$
在原 CM 基点 $c$，$n(c)=0$。原纤维的完整比较是
$$
 B(c)=\epsilon_p\,s(s-\bar a_p(E))\,\bar z_{Q_D},
 \qquad
 z_{Q_D}=\log_E(Q_D)/p,\qquad
 \epsilon_p\in\mathbb F_p^\times,
 \tag{3}
$$
其中 $s=\operatorname{Art}_p$，并保全部完成上的置换。
$s(s-\bar a_p)$ 为实际 $\mathbb F_p[\Gamma]$ 单位。
式 (3) 不是任选一个点的部分迹。

以下标量判据只使用 $n(c)=0$，**不使用**
$dn(c)\ne0$，也不使用 R153 的源非分歧证书。

## 2. 原互反函数的规范整提升

### 2.1 普通族的 Frobenius 与群值差

在原模曲线的 $p$ 进普通形式域上，以商去连通 canonical
$p$ 子群定义 $\varphi_{\rm can}$。它约化为绝对 Frobenius。
Katz（1981）§4.1、Lemma 4.1.2 及其后的构造给出这个商和
Serre–Tate 坐标上的 $q_{\rm ST}\mapsto q_{\rm ST}^p$。
连通 canonical 子群在素于 p 的同源下唯一对应，故此构造
与本题全部退化图、$W_R$、$w_{389}$、ell 层映射交换。

在 full level 上这里始终**运输标记**。Weil 配对相应由
$\zeta_\ell$ 变为 $\zeta_\ell^p$；使用 R154 的全部 determinant
分量，而不把一个非 $\mathbb F_p$ 配对分量误当作固定分量。
原 $\Gamma_0$ 循环层不需附加 diamond 修正。

对定义于 $\mathbb Z_p$ 的实际映射 $\Psi$，令
$$
 {\cal R}_{p,\Psi}
  =\Psi\circ\varphi_{\rm can}^2
       -[a_p(E)]\Psi\circ\varphi_{\rm can}
       +[p]\Psi .
 \tag{4}
$$
这是椭圆曲线群中的和。由于
$$
 \operatorname{Frob}_E^2-[a_p(E)]\operatorname{Frob}_E+[p]=0
 \quad\text{于 }E/\mathbb F_p,
 \tag{5}
$$
式 (4) 的特殊纤维作为整个映射恒等于 O。因此在每个
$p$ 进平坦仿射图 $A$ 上，其形式参数属于 $pA$。

写 $\log_E(T)=\sum_{m\ge1}c_mT^m/m$，其中
$c_m\in\mathbb Z_p$，$c_1=1$。代入 $T\in pA$ 后，
$T^m/(pm)$ 的赋值至少 $m-1-v_p(m)$，非负且趋于无穷。
所以
$$
 \widehat G_{p,\Psi}
       =\frac1p\log_E({\cal R}_{p,\Psi})
             \in\mathcal O(\widehat X^{\rm ord})
 \tag{6}
$$
是规范的整有界函数。它在普通刚性管上解析。
这里不声称它是 $\mathbb Q$ 上的有理函数，也不声称它已
延到一个统一的超收敛邻域。

式 (6) 对 $\Psi$ 加法线性，并对上述素于 p 的模映射
函子性成立；这来自 (4) 的群值等式和形式对数的加法性，
没有选择原函数常数。

### 2.2 q 展开和原 canonical-lift 点值

置
$$
 \widehat g_{D,p}
       =(t_0c_\pi)^{-1}\widehat G_{p,\Psi_D}.
 \tag{7}
$$
在原尖点，$\varphi_{\rm can}$ 为 $q\mapsto q^p$，而
$$
 \log_E\Psi_D(q)
       =t_0c_\pi\sum_{d\mid D_0}\sum_{m\ge1}\frac{a_m}{m}q^{dm}.
 \tag{8}
$$
对每个 d 用 $a_{pm}=a_pa_m-p a_{m/p}$，精确得到
$$
 \widehat g_{D,p}(q)
       =\sum_{d\mid D_0}\ \sum_{p\nmid m}
                           \frac{a_m}{m}q^{dm}.
 \tag{9}
$$
因此其约化就是原 $g_{D,p}$，而非任意同余提升。
这里 $\Psi_D^*\omega_E$ 中的 d 倍已在积分时消去；
不可再在 (9) 额外乘一个 d。

若 x 为实际 canonical-lift 点，则
$\varphi_{\rm can}(x)=x^\sigma$，其中 $\sigma$ 是不分歧
系数环的 Frobenius。Buium–Poonen（2009）式 (4.8)、
(4.76)–(4.77) 的本题规范因此为
$$
 \widehat G_{p,\Psi}(x)=\psi_E(\Psi(x)),\qquad
 \psi_E=\frac1p(\sigma^2-a_p\sigma+p)\log_E .
 \tag{10}
$$
非 formal 点可直接用 (4) 的 formal 群值解释右侧；不需
逐项把不整的 $\log/p$ 当作整值。目标 E389 非 CM，
这里使用的是原 order-two character。
微分在两边均为同一个 $\omega_E$；BP 的短模型微分规范
不额外产生一个漏记的 2。

素于 p 同源保持 canonical lifts，故 (10) 对原完整 U
迹逐项适用。实际 Hecke 点值等式、$W_R$ 不变和
$\Psi_Dw_{389}=-\Psi_D$ 给出整函数等式
$$
 \widehat B=\sum_{v\in Uv_0}\widehat h_v,\qquad
 N_\Gamma\widehat B
      =a_\ell(E)\widehat g_{D,p},\qquad
 w_{389}\widehat B=-\widehat B .
 \tag{11}
$$
在原 CM 中心，$\Psi_D(c)=O$，所以
$N_\Gamma\widehat B(c)=0$ **精确成立**。没有额外类数倍数。

## 3. 两个真正整的循环核

对 $j,k\in\mathbb Z/p\mathbb Z$，以 $d(j,k)$ 表示 j-k
在 $\{0,\ldots,p-1\}$ 中的代表。令
$\widehat b_j=\tau^j\widehat B$。对 $1\le r$、$2r<p$ 定义
$$
 \widehat I_r
  =\frac1{(2r)!}\sum_{j,k=0}^{p-1}
       \{d(j,k)(p-d(j,k))\}^{r}\widehat b_j\widehat b_k .
 \tag{12}
$$
尤其
$$
 \widehat I_1=\frac12\sum d(p-d)\widehat b_j\widehat b_k,
 \qquad
 \widehat I_2=\frac1{24}\sum d^2(p-d)^2\widehat b_j\widehat b_k .
 \tag{13}
$$
这些系数属于 $\mathbb Z_p$。

循环移位不变、$d\leftrightarrow p-d$ 不变，以及两个
$\widehat b$ 的同时反号，分别给出：

- $\widehat I_r$ 对 $\Gamma$ 严格不变；
- 它对原 Cartan 反射及其真实平移 $\nu_r$ 严格不变；
- 它对 $w_{389}$ 严格不变。

于是它们是 R157 的真实 normalizer 与 w 商上的整形式
函数和有界刚性函数。在原 $C_p$ 覆盖上使用 étale 下降，
而不是除以 p 作平均；其余相应二次商的次数素于 p。
在必要的 fine 图上先作此构造再下降，保留原标记。

这些函数在原商的 $\mathbb Q$ 有理 CM 像上取
$\mathbb Z_p$ 值。由于函数本身在 p 进完成中且依赖
$p,\ell$，**这一步并不把其值识别成 $\mathbb Q$ 中的
固定数，更不使不同 p 的值成为一个共同有理数**。

## 4. 模 p 的三角公式与不需简单零的等价

记 $I_r=\widehat I_r\bmod p$，并令
$$
                  M_j=\sum_{k=0}^{p-1}k^j b_k.
 \tag{14}
$$
因为 $d(p-d)\equiv-(j-k)^2\pmod p$，二项展开准确给
$$
 I_r=\frac{(-1)^r}{(2r)!}
       \sum_{a=0}^{2r}(-1)^a\binom{2r}{a}M_{2r-a}M_a .
 \tag{15}
$$
若 $M_0,\ldots,M_{r-1}=0$，只有中项 a=r 留下，故
$$
                    I_r=\frac{M_r^2}{(r!)^2}=(D_rB)^2.
 \tag{16}
$$
两个 $(-1)^r$ 相消；右端没有另一个交替符号。
幂矩和二项式矩的三角变换在所用范围内对角为单位。

特别，$M_0=n$、$M_1=A$、$M_2=A+2F_2$，所以作为
原曲线上的函数，
$$
 \begin{aligned}
 I_1&=A^2-n(A+2F_2)=\mathscr D,\\
 I_2&=\frac{nM_4}{12}-\frac{AM_3}{3}+\frac{M_2^2}{4}.
 \end{aligned}
 \tag{17}
$$
在原 $n(c)=0$ 纤维，$I_1=A^2$。若 $I_1(c)=0$，则
$A(c)=0$，继而 $I_2(c)=F_2(c)^2$。又
$$
                (\tau-1)A=-n,\qquad
                (\tau-1)F_2=n-A.
 \tag{18}
$$
因此这里的“$F_2=0$”准确指整个原纤维上的零元素，
不是从一个完全分裂分支的零值推断其他分支。原基点在
$\mathbb F_p$ 上有理，两个不变量的值是标量，最终得到
$$
 \boxed{\quad
   D_2B(c)=0
       \quad\Longleftrightarrow\quad
           I_1(c)=I_2(c)=0 .
 \quad}
 \tag{19}
$$
这个证明也适用于完全分裂的纤维代数
$\mathbb F_p^p$；若 Artin 非平凡，则是相应不分歧次数
p 纤维。两种情形都保全部完成。

式 (3) 的群环单位与 $D_2$ 交换，故 (19) 检测的正是原
$D_2\bar z_{Q_D}$。于是，在 R146 的同一实际输入下，
$$
 \boxed{\quad
      (I_1(c),I_2(c))\ne(0,0)
        \ \Longrightarrow\ a\le1
        \ \Longrightarrow\ \Sha(E/\mathbb Q)[p^\infty]=0 .
 \quad}
 \tag{20}
$$
未声称 $a\le1$ 反过来必使这个局部测试非零。
相对于 R142 的判别式二重零准则，(19) 的加强是去掉
$dn(c)\ne0$，并以两个值代替一阶 base jet。

## 5. 原 norm-zero 点值的精确整恒等式

本节只对 (11) 的实际整点值
$b=\widehat B(c)$ 使用精确 $N_\Gamma b=0$。
令 $\mathcal R$ 为原不分歧次数 p 整环或全部完成组成的
split 代数；两者均有整正规基，因而
$$
              \ker N_\Gamma=(\tau-1)\mathcal R.
 \tag{21}
$$
取一个**加法**整元 z 使 $b=(\tau-1)z$，记
$t=\operatorname{Tr}z$。这不是椭圆曲线上的全局
$\delta$ 预像。

整数群环中有
$$
 D_1(\tau-1)=p-N_\Gamma,\qquad
 D_2(\tau-1)=N_\Gamma-D_1+\frac{p(p-3)}2 .
 \tag{22}
$$
因此 $D_1b=pz-t$，并有相应的完整 $D_2b$ 等式。
循环二阶差分核满足
$$
 \begin{aligned}
 2k_1(d)-k_1(d+1)-k_1(d-1)
        &=2-2p\,\mathbf1_{d=0},\\
 2k_2(d)-k_2(d+1)-k_2(d-1)
        &=12k_1(d)-2(p^2+1)+4p\,\mathbf1_{d=0},
 \end{aligned}
 \tag{23}
$$
其中 $k_1(d)=d(p-d)$、$k_2=k_1^2$，指标循环。
对 (12) 两次换指标，即得精确整式
$$
 \begin{aligned}
 \widehat I_1(b)&=(\operatorname{Tr}z)^2-p\operatorname{Tr}(z^2),\\
 \widehat I_2(b)&=\widehat I_1(z)
        -\frac{p^2+1}{12}(\operatorname{Tr}z)^2
        +\frac p6\operatorname{Tr}(z^2).
 \end{aligned}
 \tag{24}
$$
若 $I_1(b)=0$，则 $t\in p\mathbb Z_p$。置
$z_0=z-t/p$，于是 $\operatorname{Tr}z_0=0$；再取加法整元
w 使 $(\tau-1)w=z_0$，得到
$$
 \begin{aligned}
 \widehat I_1(b)&=-p\operatorname{Tr}(z_0^2),\\
 \widehat I_2(b)&=(\operatorname{Tr}w)^2-p\operatorname{Tr}(w^2)
                    +\frac p6\operatorname{Tr}(z_0^2).
 \end{aligned}
 \tag{25}
$$
模 p 的第二式为 $I_2=(\operatorname{Tr}w)^2$，与
(19) 一致。这里 z、w 随实际局部代数及 b 改变；(24)–(25)
没有给固定全局预像或跨 p 的非零赋值上界。

## 6. 整刚性版本的准确边界

上述 construction 保留普通 CL **源**、原完整迹以及
R154 的指定 Cartan 方向。它没有把任意普通点当作可选择的
原 CM 点，也没有以一般几何函数非零代替 (19) 的原点值。

R157 的两个方向/反射不再产生新的独立测试：两个整循环
不变量已经对这些作用不变。仍需证明在无穷多个实际输入上，
至少一个值为 p 单位。正整数核 $d(p-d)$ 不使复代数点的
乘积 $b_jb_k$ 成为正定绝对平方；本篇不使用正性。

## 7. 全局有理参数版：不要求普通 CL 源

这一节是另一个真正的提升，适用于 R130/R139 的原
dihedral 输入，而非把 §3 的刚性函数值改名为有理数。
固定其实际 $L/F$、$\Gamma=C_p$ 和整数范数零点 Q。
保留原共轭等式
$$
                       cQ=-\tau^rQ .
 \tag{26}
$$
若原 Heegner 共轭公式有固定挠点项，先用原系统中已经选择
的、素于 p 的固定整数杀掉它；不改变测试的零性及增广指数。

当 p split F 时，取原反演对称算子
$$
 D_p=(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p).
 \tag{27}
$$
当 p inert F 时，原 dihedral Cp 扩张在其上完全分裂，
取
$$
                         D_p=(p+1)^2-a_p^2 .
 \tag{28}
$$
仍要求它是原 p 进群环单位：split 情形为
$a_p\not\equiv1\pmod p$，inert 情形为
$a_p\not\equiv\pm1\pmod p$。R130 的 E17 全好素数
及 R139 的已选 E389 输入已支付相应条件。
有限域 Frobenius 特征式使 $R=D_pQ$ 在**全部** p 处
formal。反演对称性同时给
$$
                            cR=-\tau^rR .
 \tag{29}
$$

选真正奇的有理参数
$$
 u_E(P)=
 \begin{cases}
 -x(P)/y(P),&E:y^2=x^3-17x,\\
 -2x(P)/(2y(P)+1),&E:y^2+y=x^3+x^2-2x.
 \end{cases}
 \tag{30}
$$
它在 O 取值 0，且 $u_E(-P)=-u_E(P)$。
第二模型的负点是 $(x,-1-y)$，所以该奇性是精确的；
若 $t_E=-x/y$，则 $u_E=t_E+O(t_E^4)$。
在所有 p 形式盘，
$$
    b_j^{\rm rat}=\frac{u_E(\tau^jR)}p\in\mathcal O_L\otimes\mathbb Z_p,
 \qquad
    b_j^{\rm rat}\equiv\frac{\log_E(\tau^jR)}p\pmod p .
 \tag{31}
$$
这是形式对数系数 $m\,b_m\in\mathbb Z_p$ 的直接结果。
参数的有限极点是非零二挠点，故 formal 的 R 不会命中；
若 R=O 则按正则延拓取值 0。

用同一核 (12) 对 $b_j^{\rm rat}$ 定义
$I_r^{\rm rat}$。这些是全局代数数。循环性给
$I_r^{\rm rat}\in F$；由 (29)–(30)，复共轭把 b 列送为
反射、平移后的负列，故两个负号相消，得到
$$
                   I_r^{\rm rat}\in\mathbb Q\cap\mathbb Z_p.
 \tag{32}
$$
这些有理数真实依赖 $p,\ell,Q$。这里既不固定它们跨 p 的
值，也不把 $\overline{b_j}b_j$ 的总和误称为上述不变量。

式 (31) 只给
$$
                  \sum_j b_j^{\rm rat}\equiv0\pmod p ,
 \tag{33}
$$
一般不精确为零。因此 §5 的整 trace-zero 恒等式不能
原封不动套给本节的有理参数列。
但 §4 的全部模 p 证明仍然适用，且 $D_p$ 为群环单位，
所以有准确等价
$$
 \boxed{\quad
  I_1^{\rm rat}\equiv I_2^{\rm rat}\equiv0\pmod p
   \quad\Longleftrightarrow\quad
  D_2\bigl(\log_E(D_pQ)/p\bigr)\equiv0\pmod{p\mathcal P}.
 \quad}
 \tag{34}
$$
右侧是 R130/R139 的原半局部行，保全部完成。
所以左侧任一非零给它们已证的 $a\le1$ 及相应原曲线
$\Sha[p^\infty]=0$。本节不要求 p 在 $\mathbb Q(i)$
分裂，也不要求 ordinary 或源 CL；Sha 推论仍只在
所引原结果已支付其余输入的范围内使用。

R131 的有理 Fermat 矩由全局 sigma 高度构造，本节没有
调用它的非退化。这里的增强是 (34) 对原局部行的双向等价；
仍不声称 $a\le1$ 与本测试非零等价。

### 7.1 可保留的全局大小界

由于 $|a_p|\le2\sqrt p$，(27) 的系数绝对值和为 $O(p^2)$；
(28) 也为 $O(p^2)$。Néron–Tate 的 Cauchy–Schwarz 不等式给
$$
              \widehat h(D_pQ)=O_E(p^4\widehat h(Q)).
 \tag{35}
$$
固定有理函数 $u_E$ 有
$h(u_E(R))=O_E(\widehat h(R)+1)$。
把 (12) 看成 p 个共轭变量上的二次多项式，其系数大小为
p 的固定次幂，故对 r=1,2，
$$
 h(I_r^{\rm rat})
   \le 2p\,h(u_E(R)/p)+O(\log p)
   =O_E\!\left(p^5\widehat h(Q)+p\log p\right).
 \tag{36}
$$
这里若值为零按 $h(0)=0$ 处理。(36) 保留了真实全局
高度，但既没有证明有理值非零，也没有把模 p 的一次
整除与此高度界变成矛盾。不能由 $Q\ne O$ 或
$\widehat h(Q)=o(p)$ 直接完成无穷性。

## 8. 原始来源与依赖

- N. Katz（1981），*Serre–Tate local moduli*，
  Lecture Notes in Mathematics 868，pp. 138–202，
  [作者全文](https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf)，
  §4.1，印页 169–171，尤其 Lemma 4.1.2 和随后 canonical
  Frobenius 的 classifying map。已亲读原文；§2 另给出了
  本题群值差、整对数以及 prime-to-p 图的直接证明。
- A. Buium、B. Poonen（2009），*Independence of points on
  elliptic curves arising from special points on modular and
  Shimura curves, II: Local results*，Compositio 145，566–602，
  [作者全文](https://math.mit.edu/~poonen/papers/local.pdf)，
  Theorem 4.3、式 (4.8)、(4.76)–(4.77)，作者版印页
  14、16、28。已亲读；本篇保原加法点值和固定微分规范。
- [R154 实际类群商和 CM 纤维](2026-11-12-ramified-class-quotient-and-actual-cm-fiber.md)
  与 [R157 反射及两个方向](2026-11-12-actual-atkin-normalizer-and-cm-polar-jets.md)
  支付实际覆盖、完整 U 迹、标记、共轭与商点。
- [R130 原半局部测试](2026-11-12-semilocal-formal-parameter-second-augmentation-test.md)、
  [R139 非 CM 原系统](2026-11-12-noncm-norm-one-system-and-two-step-test.md)
  及 [R146 正号两步判据](2026-11-12-noncm-two-step-criterion-with-varying-heegner-field.md)
  支付本篇引用的点到 Sha 推论。

循环核的所有等式、整下降和两个实际提升在本文证明；
无固定次数关系、全局正性或未知饱和性被当作输入。
