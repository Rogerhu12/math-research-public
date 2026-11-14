# 原 w389、Cartan 反射与两个 CM 方向的极点 jets

日期：2026-11-12。**已证明。** 本篇在 R154 的原曲线、
完整迹和原 Cartan 标记上计算实际 involutions。
结论是判别式及其商均不变，原两个 CM 方向的极点同步。
没有推出这些极点一定存在。

## 1. w389 在原参数化和互反函数上严格反号

保留
$$
 E=389\mathrm a1,\quad
 \pi:X_0(389)\to E,\quad \pi(\infty)=O,\quad
 \Psi_D=[t_0]\sum_{d\mid D_0}\pi d_d
 \tag{1}
$$
及 R154 的 $W_R$ 商 $Y_D$。令 $w=w_{389}$。
它与每个 $w_r$、$r\mid D_0$ 交换，故也作用于 $Y_D$。

原新形式的 $a_{389}=1$，且 Fricke 特征值准确为 $-1$。
可在本例直接核这个符号：weight two 的 prime-level coset
迹公式为
$$
 \operatorname{Tr}_{\Gamma_0(389)}^{\operatorname{SL}_2(\mathbb Z)}f
                         =f+U_{389}(f|w_{389}).
 \tag{2}
$$
右侧第二项来自 $S T^a$ 的 389 个陪集，因为
$w_{389}\begin{pmatrix}1&a\\0&389\end{pmatrix}$
是 $S T^a$ 的标量倍。左侧在 $S_2(\operatorname{SL}_2(\mathbb Z))=0$
中。Fricke 保持新形式的共同 Hecke 特征线，故
$f|w_{389}=\varepsilon f$；(2) 给
$1+\varepsilon a_{389}=0$，即 $\varepsilon=-1$。

因此 $\pi w+\pi$ 微分恒零，是常值 $\pi(0)$。
Manin–Drinfeld 给 $\pi(0)$ 为有理挠点，而直接有限域点数为
$$
                    \#E(\mathbb F_3)=6,\qquad
                    \#E(\mathbb F_7)=13.
 \tag{3}
$$
两处均为好约化，prime-to-residue-characteristic 挠点的
约化单射已足以排掉每个素数的挠点。因此
$E(\mathbb Q)_{\mathrm{tors}}=0$，得到真正的映射等式
$$
              \pi w=-\pi,\qquad
              \Psi_D w=-\Psi_D.
 \tag{4}
$$
第二式用 ell 无关的退化图交换；没有留下尖点常数。

R153 的权零函数满足同样严格的等式
$$
                 g_{D,p}w=-g_{D,p},\qquad
                 \widetilde g_{D,p}w=-\widetilde g_{D,p}.
 \tag{5}
$$
一个不漏原函数常数的证明是使用 Buium–Poonen（2009）
式 (4.76)–(4.77)：在实际 canonical-lift 点，
$\Phi^\dagger(P)=\psi(\Phi(P))$，且 $\psi$ 为加法
$\delta$-character。由 (4) 得其取值严格反号。
素于 p 的 389 同源保持 canonical lifts；每个普通几何点
都有唯一的 canonical lift，并可提升原 prime-to-p 层结构。
所以这些约化点在 ordinary 开集稠密，推出 (5) 的有理函数
等式。原 Manin 微分单位在两边相同。
这个证明没有只比较导数后丢掉一个未知常数。

在 R154 的辅助进程中 $\ell\equiv-1\bmod389$，故
$(389/\ell)=1$。取 $\lambda^2=389\bmod\ell$，按 R154
将 w 的 full ell lift 归一为 $\lambda^{-1}\phi_{389}$。
它的平方真为恒等，与 $W_R$ 及 projective level 群交换；
标量在 projective level 上消失。

## 2. 保原 U 轨道的 Cartan 反射

在原 nonsplit 环面
$$
 T=\mathbb F_{\ell^2}^{\times}/\mathbb F_\ell^\times,\qquad
 U\subset T,\quad |T/U|=p
 \tag{6}
$$
内保留 R154 的实际 $U$ 轨道、两条 $U_0$ 半轨道及生成元
$\tau$。nonsplit Cartan 的 normalizer 为
$T\rtimes\langle\nu\rangle$，$\nu^2=1$，
$\nu t\nu^{-1}=t^{-1}$。在 projective 线模型中可取
$x\mapsto x^\ell$，再乘一个 T 元素，使所选 U 轨道保持不变。
这只是同一个原轨道的反射，不是换一个可自由选择的 CM 纤维。

标准反射 $x\mapsto x^\ell$ 的 determinant 为 $-1$，
因 $\ell\equiv3\bmod4$ 而交换两个几何分量。乘以 T 元素
后，determinant 平方类可能改变；这里所有这些选择都在
R154 的完整 $\mathrm{PGL}_2$ 模型中有定义。它们保 U、T
并诱导
$$
                 \nu\tau\nu^{-1}=\tau^{-1}.
 \tag{7}
$$
原分支函数只按实际循环子群排列，故对保持原 U 轨道的这个
反射，$B=\sum_{v\in Uv_0}h_v$ 满足 $\nu B=B$。

若保留另一预定反射而不重新选择轨道原点，则有唯一
$r\in\mathbb F_p$ 使
$$
                         \nu_r B=\tau^rB.
 \tag{8}
$$
$r$ 记录真实标记差异，不是可调的权重。下面保留这个一般式，
所以原环类生成元不必为了简化公式而改变。

## 3. 原四条矩与二次不变量的完整作用

令
$$
 \begin{gathered}
 n=N_\Gamma B,\quad
 A=D_1B,\quad F_2=D_2B,\\
 D_1=\sum_{j=0}^{p-1}j\tau^j,\qquad
 D_2=\sum_{j=0}^{p-1}\binom j2\tau^j,\\
 \mathscr D=A^2-nA-2nF_2,\qquad C=\mathscr D/n^2.
 \end{gathered}
 \tag{9}
$$
所有以下系数等式在特征 p 中，$p\ge7$。对任意
$r\in\mathbb F_p$，直接换指标给
$$
 \begin{aligned}
 D_1\tau^rB&=A-rn,\\
 D_2\tau^rB&=F_2-rA+\binom{r+1}{2}n,\\
 D_1(\tau^{-1})B&=-A,\\
 D_2(\tau^{-1})B&=F_2+A.
 \end{aligned}
 \tag{10}
$$
由 (5) 和 w 对 level 群的交换性，
$$
                 w(B,n,A,F_2)=(-B,-n,-A,-F_2).
 \tag{11}
$$
由 (7)–(10)，一般 Cartan 反射的准确式为
$$
 \begin{aligned}
 \nu_r B&=\tau^r B,&\nu_r n&=n,\\
 \nu_r A&=-A+rn,&
 \nu_r F_2&=F_2+(1-r)A+\binom r2 n.
 \end{aligned}
 \tag{12}
$$
逐项代入 (9)，所有 $nA$、$n^2$ 修正相消，得到
$$
 \boxed{\quad
       w\mathscr D=\mathscr D,\quad wC=C,\qquad
       \nu_r\mathscr D=\mathscr D,\quad\nu_r C=C .
       \quad}
 \tag{13}
$$
特别，w 对原行的负号没有变成 C 的负号。
同样 (10) 表明 $\mathscr D$、C 对改变同一纤维的 U 轨道
原点不变。

(13) 还给一个实际下降：$\mathscr D$、C 下降至
$\mathcal P_\ell/N(T)$，再下降至它的 w 商。这里仅下降二次
不变量；若把有向 $C_p$ 覆盖也取 normalizer 商，一般得到
非 Galois 的 p 次覆盖，不能仍把它当作原有生成元的
$C_p$ 挠子。

## 4. 两个原 CM 方向及其真实共轭关系

保留最大阶 CM 格及原 389 理想 $\mathfrak n$。在
$X_0(389)$ 上，CM 点写成
$$
         \mathbb C/\mathfrak a
            \longrightarrow \mathbb C/\mathfrak a\mathfrak n^{-1}.
 \tag{14}
$$
复共轭把两个格同时共轭，并把 $\mathfrak n$ 换成
$\bar{\mathfrak n}$；w 是对偶同源，也翻转这个 389 方向，
并改变一个理想类。该理想类在 R154 的 $W_R$ 商中被消去。
分歧核唯一，故全部 $D_0$ 标记仍是原标记。
由此，在固定源商 $Y_D$ 上
$$
                         y_-=w y_+=\overline{y_+}.
 \tag{15}
$$

在有向 Cartan 商 $Z_T$ 上还需保留 CM 作用的方向。
w 是 CM 线性同源，复共轭则对
$\mathcal O_F/\ell$ 作非平凡自同构；这个差别准确由
normalizer 反射实现。因此原有向 CM 点满足
$$
                         z_-=\nu w z_+.
 \tag{16}
$$
在原 $Z_U$ 纤维选择具体 lift 后，(16) 可以多出
$\tau^r$；这个 r 由原 $\mathfrak n$ 的 Artin 作用及所选
纤维原点决定。它恰是 (8)、(12) 已保留的 r，并非新输入。

若把 (16) 在纤维上的作用记为 $\iota$，则其函数作用是
$w\nu_r$。准确有
$$
 \begin{aligned}
 \iota n&=-n,&
 \iota A&=A-rn,\\
 \iota F_2&=-F_2-(1-r)A-\binom r2n,&
 \iota\mathscr D&=\mathscr D,\qquad \iota C=C .
 \end{aligned}
 \tag{17}
$$
于原中心 $n=0$，整个纤维的二阶矩为零等价于
$A=F_2=0$。式 (17) 证明这个条件在两个原 CM 方向之间
严格等价。原 Q 的比较单位和 $s=\operatorname{Art}_p$
也随同一个实际共轭被运输；$\tau$ 的反演保持增广理想
$(\tau-1)^3$，所以没有把这一等价换成另一个测试。

## 5. 无固定点与准确的极点同步

在特征零，$y_+\ne y_-$：$W_R$ 由 CM 线性同源产生，
不可能把两个不同的 389 理想核相互交换。删固定有限个
素数后，它们的约化仍不同。

Cartan 反射也不固定原 CM 点。原源不是 $j=0,1728$ 的
椭圆稳定点，且 $W_R$ 在其固定 CM 轨道上自由。
若 $\nu$ 在 $Z_T$ 的原点有固定点，提升回原源后就必须
由源的一个自同构把 $\mathcal O_F/\ell$ 的作用共轭为其
非平凡自同构。源自同构只有标量 $\{\pm1\}$，做不到
这一点。等价地，普通 CM 的交换自同态代数不提供这种
反向共轭。$\ell$ 素于 D，两个 residue-field 嵌入确实不同。

w 与 $w\nu$ 均改变源的 389 方向，所以也不固定原点。
因此 $\{1,w,\nu,w\nu\}$ 的四点轨道在原 CM 处自由；
所有相应二次商在这些点 étale。这一论证只针对原 CM
轨道，不宣称 involutions 在整条曲线上无固定点。

R153、R154 给 n 在两个原点为简单零，可在各点都取
$t=n$ 为局部参数。由 (17)，准确有
$$
                            C_-(t)=C_+(-t).
 \tag{18}
$$
例如若
$$
 C_+(t)=c_{-2}t^{-2}+c_{-1}t^{-1}+c_0+c_1t+\cdots,
$$
则
$$
 C_-(t)=c_{-2}t^{-2}-c_{-1}t^{-1}+c_0-c_1t+\cdots.
 \tag{19}
$$
所以双极点首系数相同，单极点首系数反号；
正则、单极点、双极点三种情形在两个原方向同步。
这里没有“某个点被 involution 固定”的前提，不能把
(18) 当成同一个 germ 的偶性来令其奇次系数消失。

在完整 normalizer 与 w 商上，原两方向连同反向 Cartan
标记被识别。式 (16) 及 $Z_T$ 原点的 F 有理性表明它的像
在特征零为 $\mathbb Q$ 有理点；$\mathscr D$、C 的下降
在这个点仍保留原极点阶，因为上述商在原四点处 étale。
这只给实际极点问题的另一准确模型。

因此本次对称性检查没有给新的非零或正性：
$C$ 是不变的二次比值，原两个方向的失败同步，
而 R142 的 $\operatorname{ord}\mathscr D\ge2$ 条件仍需
一个真正的算术输入来排除。

## 6. 已独立核对的一手来源

- A. Buium、B. Poonen（2009），
  *Independence of points on elliptic curves arising from special
  points on modular and Shimura curves, II: Local results*，
  [作者全文](https://math.mit.edu/~poonen/papers/local.pdf)，
  Remark 3.6、Theorem 3.17(2)、式 (4.76)–(4.77)，作者版
  印页 6、9、28。这里实际使用加法
  $\delta$-character 的点值等式，以支付 (5) 的常数。
- B. Gross、D. Zagier（1986），*Heegner points and derivatives
  of L-series*，Invent. Math. 84, 225–320，
  [作者全文](https://people.mpim-bonn.mpg.de/zagier/files/doi/10.1007/BF01388809/fulltext.pdf)，
  II §1，印页 235–236 的 CM 理想对及 Atkin–Lehner 作用。
  本篇 (14)–(16) 另保留 R154 的分歧类群商和 Cartan 方向。
- K. Ribet、W. Stein（2017 年作者版），
  *Lectures on Modular Forms and Hecke Operators*，
  [全文](https://wstein.org/books/ribet-stein/main.pdf)，§9.1，
  印页 74–75 的新形式共同特征线与 Atkin–Lehner 算子。
  本篇 (2) 直接补出了本例所需的 prime-level 符号计算。
- [R154 完整商及原纤维](2026-11-12-ramified-class-quotient-and-actual-cm-fiber.md)
  给本篇的实际覆盖、两个 determinant 分量和完整迹；
  [R142 整正规形](2026-11-12-actual-as-basepoints-and-hecke-discriminant.md)
  给共同零与 $\mathscr D$ 二重零的等价。
