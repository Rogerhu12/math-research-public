# 原 norm-one Heegner 直线上的高度变化非退化

日期：2026-11-12。**已证明。** 本篇在 R168 的真实点与全部
p 完成上证明：两个不同同号 Hodge splitting 所给高度的差，
在原 $C_p$-Heegner 系数直线上非退化；因此这两个高度至少一个
在该直线上非退化。结论包括 E17、E389 的已付实际输入。
这是 $\mathbb Q_p$ 上的结论，不给原 $I_1,I_2$ 的模 p 非零。

## 1. 原直线、局部代数与对数

保留 R130/R139/R146/R168 的原 $L/F$、$\Gamma=\langle\tau\rangle=C_p$、
$p\ge7$、$p\nmid\operatorname{disc}F$ 及
$$
 R=D_pQ,\quad N_\Gamma R=O,\quad
 cR=-\tau^eR,\quad
 z=\log_E(R)/p\in\mathcal O_L\otimes\mathbb Z_p .
 \tag{1}
$$
原 Q 非扭，$D_p$ 在原 norm-one 系数块可逆，故 R 非扭。
本篇只需原循环子空间
$$
 V_R=\mathbb Q_p[\Gamma]R
       \subset E(L)\otimes\mathbb Q_p,\qquad
 K_p=\mathbb Q_p(\zeta_p).
 \tag{2}
$$
因 $N_\Gamma R=0$、$\Phi_p$ 在 $\mathbb Q_p$ 不可约，
$V_R$ 是一维 $K_p$ 空间。R119 的全 Mordell–Weil
$\mathcal O$-rank one 结论与此相容，但本篇不需要先借它
断言任何高度非退化。

所有 p 局部扩张在原输入下未分歧。
$D_p$ 已使 R 在每个完成的参数属于 $p\mathcal O$。
对 $p\ge3$，整形式群的对数在这个盘上可逆，
所以 R 的对数在每个完成都非零：若一个完成中对数为零，
则该完成中的 R 为 O，从而原代数点 R 为 O，矛盾。
这一步仅使用原**实际非扭点**，无需超越性定理。

定义完整局部对数配对
$$
 T(P_1,P_2)=
  \sum_{v\mid p}\operatorname{Tr}_{L_v/\mathbb Q_p}
   \left(\frac{\log_E(P_1)}p\,\frac{\log_E(P_2)}p\right),
 \qquad P_1,P_2\in V_R .
 \tag{3}
$$
将对数与配对作 $\mathbb Q_p$ 线性延拓即可。
下面证明 $T|_{V_R}$ 非退化。

## 2. p 在 F 分裂：两个完成的贡献相加

选 F 的一个 p 完成，记其上的整个次数 p étale 代数为 M。
原环类结构给两种可能：
$$
 M=\mathbb Q_p^p
 \quad\hbox{或}\quad
 M/\mathbb Q_p\text{ 为未分歧次数 p 域扩张}.
 \tag{4}
$$
两种情形中
$$
 I_M=\ker(\operatorname{Tr}_{M/\mathbb Q_p})
$$
作为 $\mathbb Q_p[\Gamma]$ 模均为一维 $K_p$ 模。
完整迹配对 $(x,y)\mapsto\operatorname{Tr}_M(xy)$ 在 $I_M$ 非退化：
M 的迹配对非退化，$I_M$ 是常数 1 的正交补，
而 $\operatorname{Tr}_M(1)=p\ne0$。

用 c 识别另一个 F 完成上的代数与 M。
则完整 p 半局部代数可写为 $M\oplus M$，
$$
 \tau(x,y)=(\sigma x,\sigma^{-1}y),\qquad c(x,y)=(y,x),
 \tag{5}
$$
其中 $\sigma$ 是 M 上的实际生成元（split 情形为循环置换）。
由 (1)，
$$
                    z=(x,-\sigma^e x),\qquad 0\ne x\in I_M .
 \tag{6}
$$
对 $f,g\in K_p=\mathbb Q_p[\sigma]/(\Phi_p)$，
令 $f^*$ 表示 $\sigma\mapsto\sigma^{-1}$。代入 (3) 得
$$
 \begin{split}
 T(fR,gR)
  &=\operatorname{Tr}_M\bigl((fx)(gx)\bigr)
    +\operatorname{Tr}_M\bigl((f^*x)(g^*x)\bigr)\\
  &=2\operatorname{Tr}_M\bigl((fx)(gx)\bigr).
 \end{split}
 \tag{7}
$$
第二步只用 $\sigma$ 对迹配对的 adjoint 是 $\sigma^{-1}$、
配对对称，以及 $f,g$ 交换。具体而言，第一项可写为
$\operatorname{Tr}_M(x(f^*g)x)$，其值等于把
$f^*g$ 换成 $(f^*g)^*=fg^*$ 后的值。
$\sigma^e$ 的两个平移也由迹不变性准确消去。

因为 $I_M$ 是一维 $K_p$ 空间且 $x\ne0$，
映射 $f\mapsto fx$ 是 $K_p\to I_M$ 的同构。
(7) 因而非退化。两处同号 splitting 的贡献没有抵消。

## 3. p 在 F 惰性：一个未分歧二次范数

记 $F_v/\mathbb Q_p$ 为未分歧二次扩张，非平凡自同构为 $\iota$。
反循环性质迫 p 在 $L/F$ 完全分裂：其 Artin 元既被 c 固定
又被 c 反演，在奇阶 $\Gamma$ 中只能是 1。
因此
$$
             L\otimes\mathbb Q_p=F_v^p .
 \tag{8}
$$
将 R 作一次 $\tau$ 平移，可以把 (1) 中的 e 改为 0：
取 $2b\equiv e\pmod p$，以 $\tau^bR$ 代替 R 即可。
这不改变 $V_R$ 或 (3)。c 对 p 个完成作反射，因 p 为奇数
有一个固定完成；以它作指标原点，c 在其系数域上作用为 $\iota$。
在此循环指标下，以
$F_v[\Gamma]$ 表示 (8) 的向量空间，则 c 作用为
$$
          \sum_j z_j\tau^j\longmapsto
                      \sum_j\iota(z_j)\tau^{-j}.
 \tag{9}
$$
原对数向量 $z=\sum z_j\tau^j$ 的 augmentation 为零。
置
$$
 K'_p=F_vK_p,\qquad q=z(\zeta_p)\in K'_p .
 \tag{10}
$$
$K_p/\mathbb Q_p$ 全分歧，$F_v/\mathbb Q_p$ 未分歧，
故 $K'_p/K_p$ 是未分歧二次**域**扩张。
augmentation ideal 经 $\tau\mapsto\zeta_p$ 同构到 $K'_p$，
且 $z\ne0$，所以 $q\ne0$。

令 $*$ 在 $K'_p$ 上固定 $F_v$、送 $\zeta_p$ 到 $\zeta_p^{-1}$。
由 $cz=-z$ 和 (9) 得
$$
        \iota(q^*)=-q,\qquad
        q q^*=-q\,\iota(q)
            =-\operatorname{Nm}_{K'_p/K_p}(q)\ne0 .
 \tag{11}
$$
此数属于 $K_p$ 且被 $*$ 固定。

对 augmentation 为零的两个向量，
系数配对等于其 Fourier 迹除以 p；故 (3) 精确成为
$$
 \begin{split}
 T(fR,gR)
   &=\frac1p\operatorname{Tr}_{K'_p/\mathbb Q_p}
                 (f g^*q q^*)\\
   &=-\frac2p\operatorname{Tr}_{K_p/\mathbb Q_p}
          \left(fg^*\operatorname{Nm}_{K'_p/K_p}(q)\right).
 \end{split}
 \tag{12}
$$
这里 $1/p$ 是 characteristic-zero Fourier 迹公式，未声称
它为整基变换；2 则来自实际未分歧二次完成的迹。
乘上的范数非零，而 Kp 的域迹配对非退化，故 (12) 非退化。

## 4. 对两个实际全局高度的结论

R168 的同号 splitting
$[\eta_\lambda]=[\eta_0]+\lambda[\omega]$ 给未归一化
cyclotomic 全局高度
$$
             h^L_\lambda-h^L_0=-\lambda p^2 T
                    \quad\hbox{在 }V_R\times V_R\text{ 上}.
 \tag{13}
$$
因此任意 $\lambda\ne0$ 的这个变化在 $V_R$ 非退化。

为从这里得出两个高度至少一个非退化，还需要实际
$\Gamma$ 不变性；不能仅凭“两个矩阵的差可逆”作此推断。
本篇各高度在所有完成使用由 $\mathbb Q_p$ 定义的同一分裂，
故确实 $\Gamma$ 不变。
任一高度在 $V_R$ 的 radical 是 $\mathbb Q_p[\Gamma]$ 子模。
而 $V_R$ 是不可约的 $\Phi_p$ 模，故 radical 只能是 0 或全部。
所以每个这样的高度在 $V_R$ 上要么恒零，要么非退化。
(13) 排除两者同时恒零，得到
$$
 \boxed{\quad
  h^L_0|_{V_R}\ \hbox{或}\ h^L_\lambda|_{V_R}
       \quad\hbox{至少一个非退化},\qquad\lambda\ne0 .
 \quad}
 \tag{14}
$$
ordinary 时可把 $h_0$ 取为 unit-root 高度；
第二个高度仍是 R168 指定的真实全局 splitting 变化。
本篇没有将其自动识别为 critical-slope Gross–Zagier 公式中的分裂。

## 5. 两个指定循环权仍需要整非零

(12) 还保留了原权的具体形式。
在 inert 情形，以 (10) 的 q 表示原对数列，
R168 的两量准确为
$$
 \mathcal E_r(z)
   =-\frac1{p(2r)!}
       \operatorname{Tr}_{K_p/\mathbb Q_p}
       \left(K_r(\zeta_p)\operatorname{Nm}_{K'_p/K_p}(q)\right),
        \qquad r=1,2 .
 \tag{15}
$$
split 情形则由 (7) 得
$$
 \mathcal E_r(z)
     =\frac1{(2r)!}\operatorname{Tr}_M\bigl(xK_r(\sigma)x\bigr).
 \tag{16}
$$
由 R161 的实际群环式，在非平凡系数块中
$$
 D=\zeta_p+\zeta_p^{-1}-2,\qquad
 K_1(\zeta_p)=\frac{2p}{D},\qquad
 K_2(\zeta_p)=-\frac{24p}{D^2}-\frac{4p}{D}.
 \tag{17}
$$
因此 (15) 是**同一真实范数**的两个特定 trace。
特别地，惰性情形完全消去 (15) 中的 p 后得到
$$
 \mathcal E_1=-\operatorname{Tr}_{K_p/\mathbb Q_p}
                      \left(\frac{\operatorname{Nm}(q)}D\right),
 \qquad
 \mathcal E_2=\operatorname{Tr}_{K_p/\mathbb Q_p}
                      \left(\frac{\operatorname{Nm}(q)}{D^2}
                             +\frac{\operatorname{Nm}(q)}{6D}\right).
 \tag{18}
$$
令
$$
 \varpi=\zeta_p^{(p-1)/2}(\zeta_p-1),\quad
 \varpi^2=D,\quad \varpi^*=-\varpi,\qquad
 q=\varpi^k u,\quad u\in\mathcal O_{K'_p}^{\times}.
 \tag{19}
$$
原 augmentation 整格给 $k\ge1$。
记 $\overline u\in\mathbb F_{p^2}^{\times}$ 为剩余类。
由 (11)，
$$
            \overline u^{\,p}=(-1)^{k+1}\overline u .
 \tag{20}
$$
对任意 $y\in\mathcal O_{K_p}$，
$\operatorname{Tr}_{K_p/\mathbb Q_p}(y)\equiv-\overline y\pmod p$：
所有 p−1 个共轭模 $\varpi$ 相同，而迹属于 $\mathbb Z_p$。
将这一事实应用于 (18) 的整项，准确给
$$
 \begin{array}{c|c|c}
 k&\mathcal E_1\bmod p&\mathcal E_2\bmod p\\ \hline
 1&\operatorname{Nm}_{\mathbb F_{p^2}/\mathbb F_p}(\overline u)
                  =\overline u^{\,2}\ne0&\text{此行不需计算}\\
 2&0&-\operatorname{Nm}_{\mathbb F_{p^2}/\mathbb F_p}(\overline u)
                  =\overline u^{\,2}\ne0\\
 k\ge3&0&0 .
 \end{array}
 \tag{21}
$$
在 $k=1$ 行，(18) 的第二式可能含非整的单项，故没有以逐项
约化来计算它；原 $\mathcal E_2$ 的整性仍由 R161 保证。
这给原惰性完成测试的精确范数版本：
$$
   (\mathcal E_1,\mathcal E_2)\not\equiv(0,0)\pmod p
                        \iff v_\varpi(q)\le2 .
 \tag{22}
$$
它是 R130/R161 的实际第二矩判据在同一原 log-column 上的重写，
不独立证明右边。尤其不能把 (11) 的非零范数删去其整深度，
也不能把所有非平凡字符分别非零换成 (22)。

配对非退化只说明每个非零向量有某个配对方向给非零值；
不说明预先指定的 $R,K_1R,K_2R$ 给单位。
特别是 R164 仍证明：若原实际全局点 $Q=\delta^aS$ 且 $a\ge2$，
则在现有半层范围内这两量完全可能都在 $p\mathbb Z_p$。
本篇未排除这种整深度，也没有把非零范数的迹当成非零。

## 6. 分裂情形的自对偶正规整基与同一门槛

本节补齐 (16) 的整规范。记
$\mathscr R=\mathbb Z_p[\Gamma]$、
$\mathfrak m=(p,\tau-1)$。
此环为以 $\mathfrak m$ 为唯一极大理想的 complete local ring：
模 p 的群环为 $\mathbb F_p[\delta]/(\delta^p)$，
且 $\mathfrak m^p\subset p\mathscr R$，
所以 $\mathfrak m$-进与 p-进拓扑等价。

若 $M=\mathbb Q_p^p$，取一个坐标的 characteristic vector
$\beta$，其循环移位已构成自对偶正规整基，且
$\operatorname{Tr}_M\beta=1$。
若 M 为未分歧次数 p 域，先取剩余域的 normal basis generator，
任意整提升 $\beta_0$ 的 p 个共轭由 Nakayama 构成
$\mathcal O_M$ 的正规整基。
其迹是单位：剩余域 normal basis 的共轭之和若为零，
就给这组基一个系数全为 1 的非平凡线性关系。
先把 $\beta_0$ 除以其迹，使
$\operatorname{Tr}_M\beta_0=1$。

令
$$
 G=\sum_{j=0}^{p-1}
       \operatorname{Tr}_M(\beta_0\sigma^j\beta_0)\tau^j
       \in\mathscr R .
 \tag{23}
$$
则 $G^*=G$，其 augmentation 为
$(\operatorname{Tr}_M\beta_0)^2=1$，故
$G\equiv1\pmod{\mathfrak m}$。
因为 2 为单位，Hensel 引理给唯一
$$
 H\in1+\mathfrak m,\qquad H^2=G^{-1}.
 \tag{24}
$$
唯一性给 $H^*=H$；对 augmentation 再用同一唯一性给
$\operatorname{aug}H=1$。
置 $\beta=H(\sigma)\beta_0$，则其 Gram 群环元为
$HH^*G=1$，所以
$$
 \operatorname{Tr}_M(\sigma^i\beta\,\sigma^j\beta)
       =\begin{cases}1&i=j,\\0&i\ne j,\end{cases}
 \qquad \operatorname{Tr}_M\beta=1 .
 \tag{25}
$$
这一构造完全在 $\mathbb Z_p[\Gamma]$ 中，不引入 $1/p$。

现在把真实 $x\in I_M\cap\mathcal O_M$ 唯一写为
$$
 x=f(\sigma)\beta,\qquad
 f\in I_{\mathscr R}=\ker\operatorname{aug}
                       =(\tau-1)\mathscr R,\qquad
 q=f(\zeta_p).
 \tag{26}
$$
$I_{\mathscr R}\to\mathcal O_{K_p}$ 的像准确为
$(\zeta_p-1)\mathcal O_{K_p}=\varpi\mathcal O_{K_p}$，
而其核为零：$\ker(\mathscr R\to\mathcal O_{K_p})
=\mathbb Z_pN_\Gamma$，与 augmentation ideal 的交为零。
故 $q\ne0$ 且仍可写 $q=\varpi^ku$，$k\ge1$。
由 (25) 的系数配对及 characteristic-zero Fourier 迹，
对 $f_1,f_2\in K_p$ 有
$$
 T(f_1R,f_2R)
   =\frac2p\operatorname{Tr}_{K_p/\mathbb Q_p}
                       (f_1f_2^*q q^*).
 \tag{27}
$$
代入 (17) 得分裂情形的精确两量：
$$
 \mathcal E_1=\operatorname{Tr}_{K_p/\mathbb Q_p}
                         \left(\frac{q q^*}{D}\right),
 \qquad
 \mathcal E_2=-\operatorname{Tr}_{K_p/\mathbb Q_p}
                  \left(\frac{q q^*}{D^2}+\frac{q q^*}{6D}\right).
 \tag{28}
$$
此处 $q q^*=(-1)^kD^kuu^*$ 且 $*$ 在剩余域上平凡。
与 (21) 相同的 trace 约化给：
$k=1$ 时 $\mathcal E_1\equiv\overline u^2\ne0$；
$k=2$ 时 $\mathcal E_1\equiv0$、
$\mathcal E_2\equiv\overline u^2\ne0$；
$k\ge3$ 时两项均为零。
因此 (22) 对分裂、惰性两种真实输入都成立。
自对偶正规整基的另一选择仅把 q 乘以
$a(\zeta_p)\in\mathcal O_{K_p}^{\times}$，所以 k 不依赖这项选择。

## 7. 原循环整格上的准确行列式

记 $\mathcal O=\mathbb Z_p[\zeta_p]$。
下面的整格始终是原点生成的
$$
                 \mathcal O R\subset V_R ,
 \tag{29}
$$
**不是**预先饱和的 Mordell–Weil 整格。
取任意 $\mathbb Z_p$ 基。
两种局部情形都把 (3) 写成
$$
 T(fR,gR)=\frac2p\operatorname{Tr}_{K_p/\mathbb Q_p}(fg^*c),
 \quad
 c=\begin{cases}
       q q^* & p\text{ 在 }F\text{ 分裂},\\
       -\operatorname{Nm}_{K'_p/K_p}(q)
                         & p\text{ 在 }F\text{ 惰性}.
    \end{cases}
 \tag{30}
$$
在两种情形中 $v_\varpi(c)=2k$。
循环域的判别式满足
$v_p\operatorname{disc}(\mathcal O)=p-2$：
由
$\Phi_p'(\zeta_p)=p\zeta_p^{-1}/(\zeta_p-1)$
直接取范数即得。
把迹配对乘以 c，使行列式乘以
$\operatorname{Nm}_{K_p/\mathbb Q_p}(c)$，其 p 赋值为 $2k$；
自同构 $*$ 的基变换行列式为单位；
标量 $2/p$ 在 $p-1$ 个维数上贡献 $-(p-1)$。
所以
$$
 \boxed{\quad
 v_p\det\bigl(T|_{\mathcal O R}\bigr)
      =(p-2)+2k-(p-1)=2k-1 .
 \quad}
 \tag{31}
$$
原对数在所有完成整，故 (31) 所算的 T 本来就是整配对；
式 (30) 的 $1/p$ 不表示免费把 Fourier 特征基当整基。
结合 (22)、(28)，得到原两个循环量的准确判别式版本
$$
 \boxed{\quad
 (\mathcal E_1,\mathcal E_2)\not\equiv(0,0)\pmod p
   \iff k\le2
   \iff v_p\det\bigl(T|_{\mathcal O R}\bigr)\le3 .
 \quad}
 \tag{32}
$$
对 R168 的高度变化，另有
$$
 v_p\det\bigl((h_\lambda^L-h_0^L)|_{\mathcal O R}\bigr)
    =(p-1)(2+v_p\lambda)+2k-1 .
 \tag{33}
$$
这里仍取原 $\mathcal O R$ 的基，未改成任何全局饱和基。

尤其若原真实整数群中 $Q=\delta^aS$，其中
$\delta=\tau-1$，对 S 使用同一个 R130 formalizer 后，
其归一对数仍在 augmentation 整格，设对应深度为 $k_S\ge1$。
若此前采用对称规范
$\delta_{\mathrm{sym}}=\tau^{(p-1)/2}(\tau-1)$，
将其单位 $\tau$ 幂吸收到 S 后即可使用这里的 $\tau-1$；
a 与 $k_S$ 均不改变。
因为 formalizer 与 $\delta$ 交换，
$$
                         k=a+k_S\ge a+1 .
 \tag{34}
$$
故新的精确行列式同时保留**全局指数 a**与原始点的
**局部对数深度 $k_S$**。
R125 的 E17 Selmer 长度上界、R144/R156 的 E389 准确长度
本身均没有给 $k_S$ 的上界，(31) 不提供无穷多个 p 的
$k\le2$。所需的新输入现在可以准确表述为：
在已构造的原小高度 Heegner 族中，令这个指定整格的
归一 trace 判别式对无穷多个 p 至多为 $p^3$ 乘一个单位。

## 依赖与来源

- R168 的完整证明，
  [原循环二次量作为高度变化](2026-11-12-cyclic-energies-as-heegner-height-variation.md)：
  Coleman–Gross 的规范采用 Balakrishnan–Besser（2015）
  Theorem 4.1 及其直接 polarization，所有完成与域迹已保留。
- R130/R139 的实际局部结构、integer formalizer；
  R157 的实际复共轭反射关系；R161 的两个循环核；
  R164 的原全局 delta 原像和整深度。
- §§2–4、6–7 是本篇直接的局部代数、群表示及整格证明。
  不调用 rank-one $E/\mathbb Q$ 的 critical-slope 非退化定理，
  也不预设整个原 $E/\mathbb Q$ 的 p 进 regulator 非退化。
