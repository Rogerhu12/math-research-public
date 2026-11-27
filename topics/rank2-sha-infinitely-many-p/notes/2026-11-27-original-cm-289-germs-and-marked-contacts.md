# 原289度 CM 图、完整级分量及三个实际标记的局部接触

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

本篇继续 [R1043](../results/R1043-original-two-isogeny-level-transport-and-weighted-orbit-reduction.md)
的同一个 $P_Q$、三个 $T_a$、原 $\rho_A$ 和全部有限图。
给出一个真正的 CM Hecke 变形，其中央值准确返回 $17T_a$；
再用已付的 Manin 自然性计算这个**实际点截面**的接触。
不把外部 $\omega$ 系数截面的零阶直接称作实际点接触。

固定 $q>5$ 惰性、$q\ne17$，并取已经存在的原
$Q_{\min}$。删去固定有限个原 CM 标记或模型不为好、非canonical
有限点的辅助素数。这个删除与目标 $p$ 无关：
这些标记在特征零为 conductor17 的 CM 纤维，
其坐标、判别式及与固定坏点的差都在同一个固定数域内，
且均非零。目标 $p$ 仍按 R1043§18满足 $p\ge5$、$p\mid q+1$，故 $p\ne q$。
以下所有点在 R1043§18 已固定的
$\mathbf F_{q^2}$ 上定义；局部接触可在严格 Hensel 完成中计算。

## 1. 外部系数展开与原实际点，不改分母

按原系数环的基 $1,\omega$，唯一写成
$$
 P_Q=P_1+\omega P_2,\qquad
 P_i\in\operatorname{MW}(S')\otimes\mathbf Z[1/6].
 \tag{1}
$$
所需分母只来自原有限次 projector、三度下降和既有倒6操作。
可固定一次一个 $M=6^e$，使 $MP_1,MP_2$ 为实际截面；
$M$ 不随 $q$、目标 $p$ 或标记增长。
以下可以始终先乘这个 $M$ 再作实际点群运算。
因为 $q,p\ge5$，它不改变这里的接触阶或模 $p$ 整除判断。

对 $t=s^{2a}$，记
$$
 b'_a=q_-d_t,\qquad
 \psi_t:A\longrightarrow E_a=S'_{b'_a},
 \qquad \deg\psi_t=17.
$$
这里的 $E_a$、$\psi_t$ 就是 R1043(77)、(91)的原对象；
没有按同一 $j$ 值另选同构。原系数实现是
$$
 \rho_A(U_1+\omega U_2)=U_1+[\omega]U_2.
$$
所以同一个实际点为
$$
 \boxed{
 T_a=\widehat\psi_t P_1(b'_a)
       +[\omega]\widehat\psi_t P_2(b'_a).
 }
 \tag{2}
$$
$\rho_A$ 只在这个固定 CM 椭圆曲线上如此解释；
一般邻近纤维不能直接把外部 $\omega$ 换成几何端同态。

## 2. degree289、full9 和有序二核的完整返回

先在特征零定义原靶曲线上的真正同源
$$
 \alpha_t=\psi_t[-\omega]\widehat\psi_t,\qquad
 \bar\alpha_t=\psi_t[-\omega^2]\widehat\psi_t.
 \tag{3}
$$
两者次数都是 $17^2=289$，
互为对偶，微分倍率分别为 $-17\omega$、$-17\omega^2$。
这些是曲线上的实际同源恒等式；然后约化同一个图。
它们分别是 $\mathcal O_{17}=\mathbf Z+17\mathcal O_K$
中的 $[-17\omega]$、$[-17\omega^2]$，
不能把 $[\omega]$ 本身称为 $E_a$ 上的几何自同源。

核确为 cyclic289。为直接核定，取源 CM 格的一组基
$e_1,e_2$，使17核由 $e_1/17$ 给出。
若 $[\omega]$ 的矩阵为
$\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$，
则 $c\not\equiv0\pmod{17}$，因为17在 $K$ 惰性，
$\mathbf F_{17}$ 中没有该单位的特征线。
在靶格基 $e_1/17,e_2$ 上，$[17\omega]$ 的矩阵是
$$
 \begin{pmatrix}17a&17^2b\\c&17d\end{pmatrix}.
$$
其 determinant 为 $17^2$，各项的最大公因数为1，
故 Smith 形是 $\operatorname{diag}(1,17^2)$。
负号和共轭不改变这个结论。

还必须保留 full9。R1043(20)–(21)的原矩阵为
$$
 M_\omega=
 \begin{pmatrix}4&5\\3&4\end{pmatrix}\pmod9.
$$
在 $\psi_t\boldsymbol\beta$ 上，
$\alpha_t$ 的几何列基矩阵是
$-17M_\omega\equiv M_\omega\pmod9$。
原 degree17 靶的 Weil pairing 指数为
$-34\equiv-1\pmod3$。
因此按 R1043§5已经支付的分量共轭，
这个矩阵读到的是 **$\tau^{-1}$**，
而不是未经分量转换的正 $\tau$。
$289\equiv1\pmod9$，所以此处也确实保留同一个
Weil pairing 值，没有另动一个 $\zeta_9$ 分量。

同时 $\alpha_t$ 在有序二核上循环一次：
$-17$ 在二挠上为1，
而 $[\omega]C_{2,i}=C_{2,i+1}$。
在同一个公共盖
$$
 D:4h^3=A^6-1,\quad
 \sigma(A,h)=(\omega A,\omega h),\quad
 \kappa(A,h)=(A,\omega^2h)
$$
上，这两项合起来准确是
$$
 g=\kappa^{-1}\sigma:
 (A,h)\longmapsto(\omega A,\omega^2h).
 \tag{4}
$$
原 $D\to B$ 的 $X=h^2/A^2$ 在(4)下乘 $\omega^2$，
而原有序根
$u_i=(1+\omega^iA+\omega^{-i}A^{-1})/6$
被送到 $u_{i+1}$，逐项核回上述两个方向。

关键是原
$$
 q_-:\quad X'=-h/A^2,\qquad
 Y'=(A^{-3}-1)/2
$$
在(4)下完全不变。
所以 $g$ 是 $q_-$ 的真实三阶 deck；
$\bar\alpha_t$ 对应 $g^2$。
因此(3)在 $S'$ 的完整级对象 $b'_a$ 上都确实返回同一点。
在所涉有限原坐标中 deck 的纤维同构为恒等，
所以没有再给微分倍率添一个 $\omega$。

这也解释为何只在粗 $j$ 线上作计算会漏掉关键内容：
在原 $B$ 上还有 $\tau^{\mp1}$，必须与有序二核的循环合成，
到原 $q_-$ 商才消掉。
作为对照，degree34 靶的指数为
$-68\equiv1\pmod3$，其 $[34\omega]$ 读到正 $\tau$；
不能把 degree17 的这一符号直接沿用到最终 degree34 图。

## 3. 真正的 CM Hecke 局部分支

在 $b'_a$ 的严格 Hensel 完成上，
$S'$ 是该带原级结构椭圆曲线的通用光滑局部变形：
R1043(99)的 KS 在这个好点为单位。
因为 $289$ 与 $q$ 互素，(3)的 kernel 是有限 étale 的，
在这个完成中有唯一的对应子群提升。
用 $\bar\alpha_t$ 的 kernel 作商，并运输同一个有限级结构，
得到真正的局部同源
$$
 \phi:\mathcal E_s\longrightarrow\mathcal E_{f(s)},\qquad
 f(0)=0,\quad \deg\phi=289,\quad
 c_\phi(0)=-17\omega^2.
 \tag{5}
$$
由§2，目标中央点是同一个 $b'_a$，而不只是同一个 $j$。
这里先支付同源自然性在这条新289图上的适用范围。
在原带有限级的好开集 $U\subset B'$ 上，cyclic289子群的模问题
$\operatorname{Cyc}_{289}(\mathcal E/U)$ 有限 étale。
包含(5)的每个非空连通分量都支配 $U$。
又 $289\equiv1\pmod{18}$，运输原 full9 和有序二级数据仍在
同一个模问题中；必要时先到原 full18 的有限 étale 覆盖证明，
再下降到同一个 $q_-$ 商，不改变原微分。
将该代数分量正规紧化，源映射在原 cusp 上方必有点；
有限扩域后源为 Tate 曲线，prime-to-$q$ 商也为 Tate 曲线。
所以在这一个代数分量的函数域中，先按 R1043§21的
$u\mapsto u^a$、$T_2=T_1^{a/b}$、$ab=289$
逐式证明 $\mu_1(\widehat\phi P)=c_\phi^q\mu_2(P)$、
$\lambda_2=c_\phi^2\lambda_1/289$ 和相应的 $r$ 公式，
再限制到当前 good germ。
这没有从仅在好点定义的一个形式倍率猜测任意同源的作用。

取同一个 raw 微分后，R1043(120)给
$$
 \lambda_{f(s)}
 =\frac{c_\phi(s)^2}{289}\lambda_s,\qquad
 \boxed{f'(0)=\omega.}
 \tag{6}
$$
最后一个导数以两端在 $b'_a$ 相同的 KS 局部坐标计。
共轭分支的导数为 $\omega^2$。
所以这个局部图与恒等图相交为简单接触；
不能把一个原 CM 端同态当作固定整个基参数的端同态。

若需要规范化这个局部参数，还可付其三次返回：
连续复合三次(5)，中央同源是 $[-17^3]$。
复合同源的 kernel 在特殊纤维是全 $E[17^3]$。
它在有限 étale 的 $E[17^6]$ 中有唯一提升，
故整个完成上的 kernel 也正是全 $E[17^3]$。
复合同源因此通过同一个 $[-17^3]$ 分解为靶同构。
$-17^3\equiv1\pmod{18}$ 保原 full9 和全部二级数据，
而该局部模问题没有剩余自同构，
所以这个靶同构给
$$
 f^3=\operatorname{id}.
 \tag{7}
$$
(6)表明它的阶恰为3。
可用三项平均取规范参数使 $f(s)=\omega s$；
这里不需要、也没有把它扩充成全曲面上的一个新自同构。

## 4. 中央值确实是原 $17T_a$ 的实际截面

在(5)的共同底上定义
$$
 \boxed{
 \mathcal R_a(s)
 =[17]P_1(s)-\widehat\phi\,P_2(f(s)).
 }
 \tag{8}
$$
先乘固定 $M$，它就是一个实际椭圆曲线点截面，
不带外部 $\omega$ 系数。
在中央纤维，
$\widehat\phi=\alpha_t=\psi_t[-\omega]\widehat\psi_t$；
故
$$
 \boxed{
 \widehat\psi_t\,\mathcal R_a(0)=17T_a.
 }
 \tag{9}
$$
这准确保留了原 $\rho_A$ 和同一个 $\psi_t$ 的真正对偶。
对目标 $p\ge5$、$p\ne17$，
$\widehat\psi_t$ 与 $[17]$ 在模 $p$ 点群上均为同构，
所以原 $T_a$ 的模 $p$ 整除与 $\mathcal R_a(0)$ 的模 $p$
整除等价；固定的 $M$ 也为 $p$ 单位。
这个等价没有制造或删除一个新的 $q$ 局部 Selmer 维数。

## 5. 原 Manin 自然性给出的实际一阶与二阶接触

令 $r_i=D\mu(P_i)/A'_q$，仍用原 $S'$ 的 raw 微分。
R1043(124)只给
$$
 r_1+\omega^2r_2=0,
$$
不能单凭这行就给(8)的实际值。
必须先对(8)逐项使用同源公式，得到
$$
 \begin{aligned}
 \mu(\mathcal R_a)(s)
 &=17\mu(P_1)(s)
    -c_\phi(s)^q\,\mu(P_2)(f(s)),\\
 r(\mathcal R_a)(s)
 &=17r_1(s)
    -\frac{c_\phi(s)^3}{289}r_2(f(s)).
 \end{aligned}
 \tag{10}
$$
此处 $c_\phi^q$ 与 $c_\phi^3/289$ 的不同正是关键。

在中央点，
$c_\phi(0)^q=-17\omega$，
$c_\phi(0)^3/289=-17$。
结合 $\omega-\omega^2=\delta$ 及 R1043(123)，准确得
$$
 \boxed{
 \begin{aligned}
 \mu(\mathcal R_a)(0)&=17\mu(P_Q)(b'_a),\\
 r(\mathcal R_a)(0)
  &=17(1-\omega^2)r_2(b'_a)\\
  &=\frac{17(1-\omega^2)\kappa_qX'(b'_a)}
          {6V'(b'_a)}
   \ne0,\qquad V'=2Y'+1 .
 \end{aligned}}
 \tag{11}
$$
非零的每个因子都已支付：
$\kappa_q\in\mathbf F_q^\times$；
$q\ne2,3,17$；
标记是有限非canonical好点，
$X'$、$V'$ 均为单位。
这不是仅用特征零的原 holomorphic form 非零。

该纤维与原 $A$ 17同源，故在惰性 $q$ 为超奇异。
R1043§19保证其 Hasse 为简单零；
(11)因此说明 $D\mu(\mathcal R_a)$ 恰有一阶零。
若 $\mu(\mathcal R_a)(0)=0$，在这个好局部模型积分一次，
因 $q>2$，得到 $\mu(\mathcal R_a)$ 的零阶恰为2。
若中央值非零，零阶为0。

现在对实际点 $\mathcal R_a(0)$ 取其 prime-to-$q$ 挠局部分支。
它存在且唯一，因为超奇异有限域椭圆曲线的点群没有 $q$ 挠。
R1043(104)的 formal 计算适用于这个实际截面：
Manin 值为单位等价于接触阶1；
Manin 零阶为2则接触阶恰为2
（更高接触的所有项阶数至少也更高，不能产生二阶首项）。
所以
$$
 \boxed{
 n(\mathcal R_a)=
 \begin{cases}
 1,&\mu(P_Q)(b'_a)\ne0,\\
 2,&\mu(P_Q)(b'_a)=0.
 \end{cases}}
 \tag{12}
$$
若使用 R1043§22的完整有限多项式，
这等价于用同一个 $N_q(V'(b'_a)^2)$ 判别，
因为其余 $c_QX'/V'^{2r-1}$ 因子在这些标记均为单位。
这给一般 $q$ 的实际 CM 变形接触判据，
不再需要重求 $Q_{\min}$ 的坐标。

每个原 $\gamma\in\operatorname{Gal}(L/K)$ 固定 $\omega$，
对原 $\psi_t$、full9 和有序二核作同一共轭即可逐式得到
(3)–(12)；完整 $\eta$ 权及 $\operatorname{Cor}$ 不删项。
这里仍不能把不同基点的接触阶当成一个未定义的共同局部接触阶
相加。

最后说明精确范围：(12)是(5)、(8)这个**指定的真实 CM Hecke
延拓**的接触，不是一个抽象纤维点在所有可能延拓下的内禀接触。
它证明这条最直接地实现原 $T_a$ 的变形没有随目标 $p$ 增长的
高接触；局部 $[p]$ 除点本身是 étale 的，也不会改变这点。
它没有由 $\mu(\mathcal R_a)\ne0$ 推出
$\mathcal R_a(0)$ 或 $T_a$ 的模 $p$ 非零。
原三个完整 shadow 的非零和无穷多个不同 $p$ 仍须通过
它们的真实点群关系继续证明。
