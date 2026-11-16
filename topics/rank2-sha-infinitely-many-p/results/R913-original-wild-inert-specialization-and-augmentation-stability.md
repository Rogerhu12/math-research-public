# R913. 原有限 wild 角色的惰性特殊化与增广除法的局部稳定性

日期：2026-11-16。**状态：同来源局部定理；保留一次固定 p 的比较尺度。** 本篇保留 R885/R897 的原一侧 ordinary ray、完整 determinant section、self-dual half-norm，以及原 $q/q^4$ 两端点。它把 R908 附录 A 的惰性局部计算推广到同一有界 wild 系统的全部有限层，并明确这类局部零在实际存在的整增广除法下保持。wild 格只按固定 p 统一校准，不宣称这个校准由一个跨 p 的固定整数控制。

结论仍是新增惰性位的局部结论。它不证明原端点底类非零，不推出其普通 p 位局部化非零，也不令 R893 的增广阶 s 自动为0。以下所有计算都是符号证明，无数学程序执行。

## 1. 同一原来源与结论

固定原普通 $p>211$、原三个有序对
$$
(j,k)=(10,16),(16,4),(4,10),
$$
以及 R885 的
$$
f=\theta_{\psi_{17}},\qquad
g=\theta_{\eta_j^{-2}\psi_0},\qquad
h=\theta_{\eta_k^{-2}\psi_0}.
$$
实际 tame 向量仍是 $f(Q),g(Q),4h(Q^4)$。原最高角色为
$$
\rho_i=\eta_i^{-1}\psi_0^3/\mathbf N;
$$
普通局部条件仍为 $\mathfrak p$ 全、$\bar{\mathfrak p}$ 零。

令 n 是 R897/R900 已允许的、与 p 互素的平方自由 tame 旧模数，
令 q 是新的惰性素数，满足
$$
q\nmid30\cdot34pn,\qquad
h_q=p^{v_p(q+1)}>1,\qquad u_q=(q+1)/h_q.
\tag{1}
$$
记原 raw 类为
$$
\widetilde{\mathbf D}_{i,nq}\in
H^1_{\rm Iw}(K[nq]_\infty,\mathcal T_i).
$$
这里 $\mathcal T_i$ 是 R897 固定一次的同一有界格；所有 finite Artin、
CM 符号、X₀/X₁、old-copy 与 period 校准一并保留。

**定理。** 令 D 是 R908 附录 A 的固定 tame/CM 尺度。对每个固定的原 p，可取一次整数 $c_p\ge0$，置
$$
D_p=p^{c_p}D,
$$
其 $c_p$ 不依赖 n、q 或 wild 深度，使
$$
\boxed{
D_p\operatorname{loc}_{q}
 \widetilde{\mathbf D}_{i,nq}=0
}
\tag{2}
$$
成立于全部 q 上方素点组成的局部 Iwasawa 模中。对每个有限 wild 层，该式也给逐点的完整群环等式；不是仅取 wild 增广或某个角色平均。

因此，R900 的任意有限惰性新集合 S 的同一 Möbius 全新项满足
$$
D_p\operatorname{loc}_{q_i}\mathbf N_{m,S}=0
\quad(q_i\in S).
\tag{3}
$$
在已选择的原比较为 p 整、且 $p\nmid D$ 时，(2)–(3)是原格中的真零。一般情形，只宣称其阶被一次固定的
$p^{c_p+v_p(D)}$ 杀掉。这里“固定”是固定 p 后与辅助层和 wild 深度无关；并未证明 $c_p=0$。R908 附录 A 的纯 tame 结论仍保原跨 p 固定 D，未被本篇弱化。

更精确地，若按 R897(A16) 的实际同格条件，某个原全新类存在
$$
\mathbf N_{m,S}=T^a\mathbf N'_{m,S},
\qquad a\ge0,\quad T=\gamma-1,
\tag{4}
$$
则同样有
$$
\boxed{
D_p\operatorname{loc}_{q_i}\mathbf N'_{m,S}=0.
}
\tag{5}
$$
(4)是前提；不从(2)–(3)反推出(4)的全局存在。

## 2. 一侧 ray、nebentypus 和 half-norm 必须同时保留

令
$$
\Lambda_b=\mathcal O[\Gamma/\Gamma^{p^b}],\qquad
v_q=[\langle q\rangle]\in\Lambda_b^\times .
\tag{6}
$$
先在这个整有限群环中工作，之后再取 b 的逆极限。第一槽使用 ACR
Theorem 3.3 对原一侧理想 $\mathfrak f(n)\mathfrak p^{b+1}$ 的
CM 商；该理想与 $\bar{\mathfrak p}$ 互素。它不是完整
$(p^{b+1})$ ring-class 理想。

在原权2 Hida 分支上，有限 wild 字符 $\epsilon$ 的一侧 theta
形式带 nebentypus
$$
\nu_\epsilon=\epsilon
\tag{7}
$$
（原固定 tame nebentypus 是1）。原(6)中的 $v_q$ 同时记录所有
$\nu_\epsilon(q)$。第一槽的完整 first-CM 商及其对偶仍采用
ACR §5–6 的 primed Hecke 规范；不把 $\langle q\rangle'$ 与
$\langle q\rangle$ 当成同一 cohomology 算子。

对 primitive p-adic 向量 $(x,y,z)$，第二、三权均为2时，原
determinant section 在其 unit 支持上准确为
$$
\operatorname{Det}_\epsilon(x,y,z)
 =\epsilon^{1/2}\!\left(
   \frac{\det(x,y)\det(x,z)}{\det(y,z)}
                    \right).
\tag{8}
$$
在 $\det(y,z)\notin\mathbf Z_p^\times$ 的补集为0；
另外两个 determinant 在规定的 $T'\times T\times T$ 域上本来是单位。
平方根是 pro-p 角色的唯一平方根；原 tame 权2分支没有另添
Teichmüller 半角色。

式(8)有两条直接可核的协变：
$$
\begin{split}
\operatorname{Det}_\epsilon(a x,y,z)
 &=\epsilon(a)\operatorname{Det}_\epsilon(x,y,z),\\
\operatorname{Det}_\epsilon(xM,yM,zM)
 &=\epsilon^{1/2}(\det M)
                      \operatorname{Det}_\epsilon(x,y,z).
\end{split}
\tag{9}
$$
分别缩放 y 或 z 则不改变(8)。在原定义域内，unit 支持被
$M\in\Gamma_0(p\mathbf Z_p)$ 保持。一般 $\mathrm{GL}_2(\mathbf Z_p)$
仍保 determinant 的单位条件，但(9)只在两端均属于原定义域时使用。

ACR 的 Galois系数中同时保留 $\kappa^{-1/2}$。
故共同 degree-q isogeny在三个 p-Tate 向量上产生的
$\kappa^{1/2}(q)$，与该 half-norm 的系数运输准确相消。
此外，原 asymmetric 来源定义本身带
$$
\kappa(n)^{-1},
\tag{10}
$$
所以在新增 q 时还带 $v_q^{-1}$。这些因子都在原公式中；
不能先把(7)置1，或只用最后的 anticyclotomic 角色来倒猜一侧模曲线。

在全部操作之后，ACR(6.4)于原 k=2给整模同构
$$
H^1(\psi,n)\otimes_\Lambda\Lambda_b
 \simeq
\operatorname{Ind}_{K[n]}^{\mathbf Q}
 \Lambda_b(\psi_{\mathfrak P}^{-1}
                    \kappa_{\rm ac}^{-1}).
\tag{11}
$$
这才是从一侧 ray 返回原 anticyclotomic 有限层的步骤。

## 3. 真实退化映射的 diamond 表

本节从 moduli 定义核定符号，而不是沿用平凡 nebentypus 的简表。

把原 cyclic $q^2$ 来源经 $z\mapsto qz$ 写成中心椭圆曲线的
两条不同 q 直线 x,y。若原椭圆曲线及旧 level 点为
$(E_{\rm old},Q_{\rm old})$，中心为 $E_c=E_{\rm old}/C_q$，
则 ACR §2.1 的定义给
$$
Q_c=\text{image of }q^{-1}Q_{\rm old}.
$$
沿 x 的对偶 quotient 把 $Q_c$ 送回 $Q_{\rm old}$；
沿 y 的第二个 quotient则还要把旧生成元除 q。因此
$$
\pi_0:(E_c,Q_c)\mapsto(E_c/x,\ \overline Q_c),
\qquad
\pi_2:(E_c,Q_c)\mapsto(E_c/y,\ q^{-1}\overline Q_c).
\tag{12}
$$
这里 $q^{-1}$ 是在全部旧、素于 q 的 level 上的逆；包括 p-power level。

在 exotic Igusa 呈示中写中心 $E_c=E_b^{(q)}$，
且旧点由 $Q_b$ 的 q 幂 Frobenius 运输得到。
connected quotient给 $E_b^{(q^2)}$；其它 quotient经 Verschiebung
给 $E_b$，旧点是 $qQ_b$。故真正的表为
$$
\begin{array}{c|ccc}
 &L=x&L=y&L\ne x,y\\ \hline
\pi_0&\operatorname{Fr}_{q^2}&\langle q\rangle&\langle q\rangle\\
\pi_2&1&\langle q\rangle^{-1}\operatorname{Fr}_{q^2}&1 .
\end{array}
\tag{13}
$$
在平凡 nebentypus 上，它退化为 R908(A14)；在非平凡
finite wild 层上，(13)中的两个 diamond 不可省略。

用完整一侧 CM 商的 Hom 向量记为 F。对有限角色分量，
$$
F\langle q\rangle=\nu_\epsilon(q)F,\qquad
F\operatorname{Fr}_{q^2}=-q\nu_\epsilon(q)F.
\tag{14}
$$
第一式来自 primed diamond的实际 Tate 商；第二式也可以直接由
$\psi_\epsilon((q))=-q\nu_\epsilon(q)$ 核定。若将 F 实现为到
$E_{17}$ 的映射，须先过杀掉其有限一侧角色的域；
其 Galois共轭为 $\nu_\epsilon(q)^{-1}F$，与
$E_{17}$ 上 $\operatorname{Fr}_{q^2}=[-q]$ 合成，恰给(14)。
因此没有把 $F$ 在原剩余域上误认成一个不带角色的单独映射。

整群环版本将 $\nu_\epsilon(q)$ 换成 $v_q$。
CM norm 的真实 first-slot Hom 等式为
$$
\sum_{\sigma\in G_q}F_{nq}^{\sigma}
 =F_n\pi_0+q^{-1}v_qF_n\pi_2 .
\tag{15}
$$
它来自 ACR Theorem 3.3 的 inert norm；
在 $v_q=1$ 时正好是 R908(A11)。

EP 的算术惯性 h 部分在每个 Igusa 分量上点态固定。
由(13)–(15)，在其 Jacobian Hom 群中
$$
h_q F_{nq}|_{I_L}
 =
v_q\,r_L F_n\pi_I,
\qquad
(r_x,r_y,r_o)=
\left(-\frac{q^2-1}{q},\,0,\,\frac{q+1}{q}\right).
\tag{16}
$$
这些 Hom 群无 p 挠，故可且仅在此处约 $h_q$：
$$
F_{nq}|_{I_L}
=v_q a_LF_n\pi_I+C_L,\qquad
(a_x,a_y,a_o)=\frac{u_q}{q}(-(q-1),0,1).
\tag{17}
$$
保留全部常数 $C_L$。朴素地将两个 diamond 都漏掉，会在
$L=y$ 处得到错误的 $1-\nu_\epsilon(q)^2$；(16)表明实际该项精确为0。

## 4. 原有限配置的整评价与同一有界格

### 4.1 不用 wild 角色幂等元

上述计算在 $\Lambda_b$ 上进行，不先分解有限 wild 角色再除
$|\Gamma/\Gamma^{p^b}|$。对有限精度 $\Lambda_b/p^v$，原连续
determinant section 通过一个有限 p-level 配置集。取能够读取它的
level 即可；不要求该配置集的次数为 p 单位。

ACR §5.6 使用的准确有限模型，是分布模与有限 induced 模的同构
$$
\varphi\longmapsto
 \left(f\longmapsto\sum_{r}\varphi(r)f(r)\right).
\tag{18}
$$
右边是求和评价，没有除配置数。该同构与 Hecke、
restriction/corestriction 和原 Gysin 对应相容。
我们用(18)评价原 CM 商的每个 regular 群环坐标；不是先把
函数系数上同调 restriction 到一个 p 次 cover，再由那个
restriction 后的零断言原类零。

具体说，按原 $s_{f,n*}$ 的定义，先把函数系数与分布上同调作
(5.8)的整评价，再经 ordinary 完美配对(5.7)及 CM 商得到目标。
将(18)的 coset 基逐项代入这个评价，得到在相应真实有限配置
cover 上的 weighted Gysin 类。每项权正是(8)在该配置上的值。
因此后续的特殊纤维计算是**原评价映射本身**的计算；
不是给一个未证明忠实的 cover 上同调附加左逆。
ACR 的 $s_{f,n*}$、其 $-\kappa$ 扭曲及它对两退化映射的交换，
均保持在这份配对定义内。

在这个计算中，(12)–(17)采用 R897(A.1)已经付清的原 DR
有限配置/CM-Hom 呈示。R897 的整条自然性把它送到原 ACR
来源；不在计算结束后再次施一遍孤立的“交换 $\pi_1,\pi_2$”。
若改用对偶呈示，必须把该交换、系数对偶和 $-\kappa$ 同时运输。
本文不把某一个孤立对偶表的标量当作新的原归一。

### 4.2 保留完整原运输，只读 q+1 因子

在固定 full-p 配置的连通 cover 上，(8)为常数：
全部 determinant/Weil-pairing 标签已经固定。
新增 q 与这些 p-配置互素，所以 EP 的稳定模型及(12)–(13)
逐配置适用。共同 degree-q isogeny在所有配置之间给双射；
(9)给其精确因子 $\kappa^{1/2}(q)$，与原
$\kappa^{-1/2}$ 系数运输相配。

为避免把对偶规范拆开后误算一次 scalar，本文保留完整算子
$$
\mathfrak U_{nq,n,b}:=
\text{R897(A.1)步骤3–5的实际有限系数运输}.
\tag{19}
$$
它是由上述步骤诱导的**比较映射**：其定义保新增 $v_q^{-1}$、
完整 determinant/half-norm、原 ordinary 双对偶 $s_{f,n*}$、
一侧 CM 商和(11)。其中已经用于选取 Hom 坐标的步骤只用于
规定这份比较，绝不再次作用一遍；
所有原 tame/Artin、二处 $q_0/q_2$及第三槽4同步保留。
(19)不是一个另选的未知 $C_p$ 标量，也没有被归一为1。

计算在(18)中的 finite CM–Hom 评价呈示上进行。
未对偶呈示给(17)的共同 $v_q$。
换成实际 $s_{f,n*}$ 所用的对偶呈示时，必须同时运输
系数对偶、$-\kappa$和两退化映射的交换。
由于所用模曲线/系数对应均与 proper push、整数倍及
原 q-local specialization相容，这个完整运输保留
“为 q+1 倍”的性质。这里不用只交换 $\pi_0,\pi_2$所得
某张未校准的单表。

第二、三槽在权2的 homogeneity为0，原 nebentypus亦为1；
在未对偶 Hom 呈示中的两旧轴系数是
$$
(b_L,c_L)=(-q,1),(1,-q),(1,1).
\tag{20}
$$
交换两个特殊 Igusa 标签不会改变其乘积：
两个特殊标签都给 $b_Lc_L=-q$。
因此以下计算可先在(17)的呈示中做，得到整个
$\Lambda_b$ 上的 q+1 因子，再经(19)送回原类。
我们不需要、也不宣称其余共同 unit在某个独立点坐标中等于1。
### 4.3 原 CM regular 坐标及有界分母

第一槽用 ACR Theorem3.3 与(6.4)给的整 CM 商系统。
在固定有限层保留它的整个 regular 模；不使用
$p^{-b}\sum_\epsilon e_\epsilon$。
为将其各坐标写成几何映射，可扩域杀掉有限 ray 角色。
整 Faltings 的 Hom–Tate 同构（R908附A的饱和证明）随后把这些
坐标实现为同一有限模曲线 Jacobian 到 $E_{17}$ 的
p-adic Hom 矩阵。所有有限精度可由真正整 Hom 逼近，
故(15)的整矩阵等式可在这些逼近上使用，再取极限。
同样处理第二、三槽；后两槽仍是原固定 CM 曲线的 Hom，
没有引入新的高权对象。

这个实现仅使用原 CM 商的整同构、有限 free 群环坐标和整
Hom–Tate 饱和。为写坐标而扩大的域次数可以含 p，
但没有取那个次数的倒数。原固定 tame 对应及 R885/R897
n=1 校准至指定 Tate/period 格，可一次带来 p 分母。
普通投影是整算子的有界极限；$(5.7)$只使用 ordinary 完美配对，
不使用一般 finite-slope 完美性的过宽断言。
因此可在开始时取同一个 $p^{c_p}D$，
使整个评价、原 CM 比较及其固定反向比较在
所有 n、q、b 上整。此处只得到固定 p 的统一 $c_p$；
未声称它由一个跨 p 固定整数控制。

还需说明在辅助域验证后的返回。令 $L/F$ 是本计算在新增 q
处为杀掉有限 p 角色而采用的有限扩张。它在 q 不分歧。
原反循环 Shapiro 返回后，目标格的 Frobenius 特征值为
$-q$乘有限阶根；在任何有限扩张后均不等于1。
所以
$$
H^0(L,\mathcal T_i)=0,\qquad
H^1(F,\mathcal T_i)\longrightarrow H^1(L,\mathcal T_i)
\quad\text{为单射}.
\tag{20a}
$$
第二式直接由 inflation–restriction 得到，绝非用
corestriction 乘扩张度数后约去 p。
我们只对完整 $\mathbf Z_p$ 格使用(20a)，
不把它误写成模 $p^v$ 的 $H^0=0$；
后者在 $q\equiv-1\pmod p$ 时一般为假。
有限模数用于构造/逼近，先取其相容极限后才用(20a)返回。

## 5. 全 special fibre 的原局部读数

在每个配置 cover 上，保 R908 的真实两旧 CM 轴 G,H。
其特征零 Hom 组合 $H_*G^*$ 属于 K，故用
$$
D_\varphi=\Gamma_\varphi-E_0\times O-q(O\times E_0),
\qquad \varphi^2=-q,\quad\varphi^\dagger=-\varphi
$$
收缩时有
$$
\deg(G,H)^*D_\varphi
=\operatorname{Tr}((H_*G^*)\varphi)=0.
\tag{21}
$$
证明仍是用 $\delta\varphi=-\varphi\delta$ 共轭反号。
每个配置上的 coefficient为常数，故(21)逐项杀掉(17)中的
$C_L$，包括其可能的 p-primary 部分。这里没有使用一般
supersingular 纤维上的平移不变性。

full-q固定 Weil pairing cover的次数仍为 q−1，
每组 Igusa 向原旧配置的总次数也为 q−1，二者按 proper push准确返回。
一般位置有 q−1个。于是完整 ordinary 部分为
$$
\begin{aligned}
\mathscr S_{\rm ord}^{\rm Hom}
&=v_q\left(a_x(-q)+a_y(-q)+(q-1)a_o\right)
                                  \mathscr S_{n,b}^{\rm Hom}\\
&=v_q\frac{(q-1)u_q(q+1)}q\,\mathscr S_{n,b}^{\rm Hom},\\
D_p\,\mathscr S_{\rm ord}^{\rm orig}
&=(q+1)\,
 D_p\mathfrak U_{nq,n,b}
 \left(v_q\frac{(q-1)u_q}q\,
                         \mathscr S_{n,b}^{\rm Hom}\right).
\end{aligned}
\tag{22}
$$
这里 $\mathscr S_{n,b}^{\rm Hom}$ 是(18)的实际旧有限配置评价。
式(22)只把整数 $q+1$ 从原比较映射中提出；即便某个系数约定
使(19)对 $\Lambda_b$ 作反演，它仍是 $\mathbf Z_p$ 线性并保该整数。
最后一行的括号经(19)后，是原目标局部格中的类；共同尺度 $D_p$
已经同时保证这一步整。没有把一个有限字符下的裸点先乘
$q+1$后宣称零，也没有把(19)认成标量1。

在各 Drinfeld 分量上，第二、三条旧映射都是常值；
故 $(G,H)^*D_\varphi$ 为平凡线束。所有解消链同理为零。
节点、cusp及 modified-diagonal 基点项按 R908(A26) 的完整
proper-push论证处理；有限配置与 coefficient twist不增加未记的一维分量。

最后才使用(11)。有理惰性理想(q)在所有原 prime-to-q
ring-class 层及 anticyclotomic p塔中完全分裂，因此原旧局部模为
$$
\bigoplus_{w\mid q}H^1(K[n]K_b{}_w,\mathcal T_i)
 \simeq
\mathcal O[G_n][\Gamma/\Gamma^{p^b}]
       \otimes_{\mathcal O}\mathcal T_i/(q+1)\mathcal T_i.
\tag{23}
$$
在 $K[nq]K_b$ 的 q 上方局部域中，新增 q 部分全分歧、剩余域不变，
原目标格不分歧，所以上式的同一个局部计算仍成立。
在固定最高符号中 Frobenius 是−q。换到共轭符号时仍保实际
互反，所得同一 annihilator不变。式(23)可直接由不分歧
cocycle和 $F-1=-q-1$ 得到；pure-weight部分没有额外 singular直线。

所以(22)最后一行为零。这里不能在未施(11)的一侧 ray点向量中，
先声称(q)完全分裂或先用 q+1杀点：其一侧 Frobenius本有 $v_q$。
上述运算是先保(13)–(20)，再到原 anticyclotomic module使用(23)。

Frobenius收缩在最高局部块上的行列式为 q，是 p单位；
用固定的反向比较尺度，得到经共同尺度后的局部恒等式。在辅助实现域中，该恒等式对每个有限精度相容成立。
先在每个 b 取模 $p^v$ 的相容极限，并用(20a)返回原 q-local 格；再取 b 的 corestriction 逆极限，即得原有界 Iwasawa 模中的(2)。

## 6. 全新项及实际增广除法

先从原 raw 局部零转到 Möbius全新项。
含 $q_i$ 的项用(2)；不含 $q_i$ 的旧 restriction项带原系数
$$
c_{q_i}=-\frac{(q_i+1)^2}{q_i h_i}
       =-\frac{u_i}{q_i}(q_i+1).
\tag{24}
$$
该旧项在 $q_i$不分歧，且 $q_i$在其全部旧 wild/tame ring-class层
完全分裂，故(23)使(24)的局部像为零。这证明(3)，保全部其它群环坐标。
R908的整 $j_i:A_i\hookrightarrow\mathcal O[G_i]$ 及其模 $h_i$
饱和性，还将此式传给所有原增广坐标。

固定一个 $q_i$，完整局部 Iwasawa 模准确是有限个
$$
(\mathcal T_i/(q_i+1)\mathcal T_i)[[T]]
\tag{25}
$$
的直和，并保其它有限群环因子。其 T乘法为单射：
对任意系数环 M，$T\sum_{r\ge0}m_rT^r=0$逐系数迫全部$m_r=0$。
这里不需要 M无 p挠；(25)通常确有 p挠。

若(4)实际存在，局部化与 T交换，由(3)得到
$$
T^aD_p\operatorname{loc}_{q_i}\mathbf N'_{m,S}=0.
$$
由(25)约去 $T^a$即得(5)。
因此，新增惰性位的原几何局部零不会因一次合法的全系统除 T
而突然变成非零。相反，它不是全局除 T 的充分条件：
R897(A17)仍要求**所有 tame有限底类**为零。

## 7. 对原 s 门的实际含义

本篇给出了非平凡 finite wild 层的 moduli/nebentypus 相位与原全系数返回，
所以 R908 的局部零不再只停在增广点。此前不能省略的一侧
nebentypus、$\pi_2$的 divided old level、determinant支持、
half-norm和有限Shapiro均在原来源内保留；(19)的完整比较并未被当作标量1。

但所有这些结论发生在新增惰性位。
R893的普通 $\mathfrak p$映射、原端点 $c_1$及
$\mathscr D_{i,p}(T)$的零阶不是(23)中的映射。
特别，(5)说明不能把这些新增惰性位的局部零当成阻止
$\mathscr D_{i,p}$有正增广阶的理由。
本篇没有证明全新类全局为零，也没有给偶数全新块新的
$h_1\cdots h_t$ scalar整除。

## 原文与同来源依据

- R885、R897：原 CM Hida 分支、同一有界源、有限层整 CM/Shapiro、
  完整 determinant/ordinary对应、原固定校准及全部 tame/wild相容。
- R908附录A：完整 q稳定模型、整 Hom、常数、两旧 CM轴的
  degree-zero收缩、所有 Drinfeld/节点/cusp项及 fixed-source尺度。
- Alonso–Castella–Rivero, *The diagonal cycle Euler system for GL₂×GL₂*,
  J. Inst. Math. Jussieu (2023), DOI
  [10.1017/S1474748023000221](https://doi.org/10.1017/S1474748023000221),
  [发表全文](https://web.math.ucsb.edu/~castella/ACR1-print.pdf)：
  §2.1–2.2 的 $\varphi_q$及(2.2)的旧生成元，
  Theorem3.3的 inert norm，
  §5.5(5.7)和§5.6有限函数/分布的真实Shapiro，
  §6(6.2)–(6.5)、Lemmas6.1–6.2与Proposition6.3。
- Bertolini–Seveso–Venerucci, *Reciprocity laws for balanced diagonal classes*,
  Astérisque434 (2022),77–174，
  [作者全文](https://www.esaga.uni-due.de/f/massimo.bertolini/publications/Ast-BSV1.pdf)，
  §8.1，作者稿printed p58的 determinant section及(154)；
  (8)–(9)是把两个固定权2直接代入该显示式。
  ordinary pairing使用上述ACR的整完美性；不使用其一般
  finite-slope完美性的过宽版本。
- Edixhoven–Parent, *Semistable Reduction of Modular Curves Associated
  with Maximal Subgroups in Prime Level*, Documenta Math.26 (2021),231–269，
  [发表全文](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)，
  §2.1、§2.2.4(12)–(13)；所用的是算术惯性在Igusa上的点态固定。
