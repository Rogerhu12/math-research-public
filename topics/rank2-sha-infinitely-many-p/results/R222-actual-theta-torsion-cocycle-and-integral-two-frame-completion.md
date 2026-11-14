# R222 — 实际 q 连接、高 log 系数、二挠 Frobenius 平移与可付的双端 Artin–Hasse 过渡

日期：2026-11-13。**状态：同一实际 theta 的高 log 公式、原 degree-$p$ 参数的二挠 cocycle、两个实际运输 frame 的有限整过渡，以及二次极点成本下全迹单位的准确抵消已证明。没有证明原 $K$ 的无穷非零。**

本篇继续 [R219](R219-actual-theta-full-fiber-trace-and-frobenius-residual.md)，
不再把任意参考扰动当成实际 theta。以下所有原点系数均来自
$\Theta=\vartheta(2z)^{17}$；原第一行的模 $p^2$ 始终保留。
反射作用于一个实际坏指数原函数，并不直接给有限 theta 多项式的反射。

## 1. 原 q 侧 theta 连接

保持 $p=4r-1>19$、$d=2r-1$、$O=\mathbf Z_p$。使用
$$
q=\frac{s}{(1+s)^2},\qquad s=S(q),\qquad
F_+(q)=\sqrt{1+S(q)}F(S(q)),\qquad
G_+(q)=(1-4q)^{-3/4}.
$$
这些是 R219 的严格参数，$z=q^{1/4}F_+(q)$。
令
$$
\mathcal L(q)=\log\Theta
=L(S(q))+17\log(1+S(q)),\qquad
\lambda_m=[q^m]\mathcal L(q).
\tag{1}
$$
写 $J=\mathcal L'$。原 $s$ 连接
$4s(1-s)L''+(3-5s)L'=17$ 经直接换元，准确变成
$$
\boxed{\quad
4q(1-4q)J'+3(1-8q)J=68.
\quad}
\tag{2}
$$
因此
$$
\lambda_1=\frac{68}{3},\qquad
(m+1)\lambda_{m+1}
=\frac{8(2m+1)}{4m+3}\,m\lambda_m,
$$
$$
\lambda_m=
\frac{17}{2}\frac{4^m}{m}\frac{(1/2)_m}{(3/4)_m}.
\tag{3}
$$
特别 $\lambda_m\in O$ 对 $m<r$ 成立，而
$\ell_+:=\lambda_r$ 只有一次负 $p$ 层。
由严格换参与原 $\Theta=\vartheta^{68}(1+s)^{17}$，
$$
c-\ell_+\in O,\qquad
\alpha:=\overline{p\ell_+}=\overline{pc}=68\kappa.
\tag{4}
$$
这里 $c=68k_r$ 是原 $w$ gauge，不另选周期。

令
$$
t_+(q)=q^rF_+(q),\qquad
\Gamma_+(q)=\exp(\mathcal L(q)-\ell_+t_+(q))\pmod{q^{2r}}.
\tag{5}
$$
这是一份由原 theta 直接构造的实际整参考；以下同时证明其整性和全部高半窗系数。

## 2. 实际高 log 系数的有限超几何–调和公式

沿用
$$
g(q)=\overline{F_+(q)}
=\sum_{j=0}^{r-1}
\frac{(-4)^j\binom{r-1}{j}}{4j+1}q^j.
$$
对 $0\le j\le r-1$ 定义
$$
A_0=0,\qquad
A_j=
1-\frac1{4j+1}
+\sum_{i=0}^{j-1}
\left(\frac1{4i+3}-\frac1{4i+4}\right)\in\mathbf F_p.
\tag{6}
$$
所有分母都是单位。令
$$
H_p(q)=\sum_{j=1}^{r-1}g_jA_jq^j,\qquad
E_p^{\rm low}(q)=
\exp\left(\sum_{m=1}^{r-1}\lambda_mq^m\right)
\pmod{q^{2r}}.
\tag{7}
$$
上标 low 用于区分下面的 Artin–Hasse 指数；它不是该指数。

实际参考准确满足
$$
\boxed{\quad
\overline{\Gamma_+}
=\overline{E_p^{\rm low}}\,
       \left(1+\alpha q^rH_p(q)\right)
       \pmod{q^{2r}}.
\quad}
\tag{8}
$$
特别
$$
[q^r]\log\Gamma_+=0,\qquad
[q^{r+j}]\log\Gamma_+=\alpha g_jA_j
\quad(1\le j\le r-1)
\tag{9}
$$
是实际原系数，不是自由高 jet。

证明从 (3) 的特征零准确比开始：
$$
\frac{\lambda_{r+j}}{\lambda_r}
=\frac{p+1}{p+4j+1}
 \prod_{i=0}^{j-1}
 \frac{4(p+4i+3)}{p+4i+4}.
\tag{10}
$$
若 $f_j=[q^j]F_+$，则基项正是
$f_j=(4j+1)^{-1}\prod_{i=0}^{j-1}(4i+3)/(i+1)$。
所有所见分母为单位，所以
$$
\frac{\lambda_{r+j}}{\lambda_r}
\equiv f_j(1+pA_j)\pmod{p^2}.
$$
于是
$\lambda_{r+j}-\lambda_rf_j\in O$，
且其约化为 $\alpha g_jA_j$。低于 $r$ 的项原本整，
次数 $r$ 准确消去，证明 (5) 整和 (9)。
高半窗修正从 $q^{r+1}$ 开始，其平方超出窗口，故得到 (8)。
全部指数阶乘小于 $p$。

与 R219 唯一实际 $\Xi$ 的关系也明确。置
$V(q)=\sqrt{1+S(q)}$，并记 R213 的 $\ell=[s^r]L$。
因为 $s^rF(s)=t_+(q)V(q)^p$，
$$
\boxed{\quad
\bar\Xi=
\overline{\Gamma_+}\,
 \exp\!\left(\overline{\ell_+-\ell}\,q^rg\right)
 \left(1-\alpha q^rg\log V\right)
 \pmod{q^{2r}}.
\quad}
\tag{11}
$$
其中 $\ell_+-\ell\in O$。因此 (8) 同时给原 $\Xi$ 的真正高半窗；
(11) 的固定对数校正不能省略。

## 3. 保留首行 p² 的原 K 有限式

记 R219 的原有理列为
$$
R_A^0(q)=a_0(q),\qquad
R_B^0(q)=\rho(q)b_0(q),\qquad \rho=(1-4q)^{1/2}.
$$
这是原两列，尚未作 $\rho^{-p}$ 下降。
其第一行有特征零准确表达
$$
\boxed{\quad
R_{1,F}=
[q^r]E_p^{\rm low}(q)R_F^0(q)
       G_+(q)F_+(q)^{-p-2}.
\quad}
\tag{12}
$$
它只读实际 $\mathcal L$ 的次数小于 $r$ 的系数，故可直接在 $O/p^2$ 计算。
在首行失败后，仍用真正的
$u_F=\overline{R_{1,F}/p}$，不以模 $p$ 的第一行代替它。

在 $\mathbf F_p$ 中定义同一有限泛函
$$
\mathscr L_F(\psi)
=[q^r]\bar E_p^{\rm low}\,\bar R_F^0\,
       \frac{(1-4q)^{r-1}}{g^2}\,\psi,
$$
$$
\mathscr B_F=
[q^{2r}]\bar E_p^{\rm low}\,\bar R_F^0\,
       \frac{(1-4q)^{r-1}}{g^3}.
\tag{13}
$$
则原后继坐标准确为
$$
\boxed{\quad
K_F=
\mathscr B_F-\alpha u_F+
\alpha\,\mathscr L_F\!\left(\frac{H_p}{g}-\log g\right),
\qquad F=A,B.
\quad}
\tag{14}
$$

证明：实际 $\Gamma_+$ 的第二权模 $p$ 由 (8) 给
$\mathscr B_F+\alpha\mathscr L_F(H_p/g)$。
另一方面，$t_+=w^rF_+^{-p}$，
而 $F_+^{-p}\equiv1-p\log F_+\pmod{p^2}$。
同 R213 的整比较，这个第二权在首行失败后是
$\overline{\widehat R_{2,F}}+\alpha\mathscr L_F(\log g)$。
相减并用 $K_F=\overline{\widehat R_{2,F}}-\alpha u_F$，
即得 (14)。

若改用 R219 的下降列，则第一行必须同时改为
$u_D=u-(0,L_{\rho,B})$，并保留那里相同的 $\rho$ 校正。
(14) 直接使用原 $u$，没有免费把 $\rho^{-p}$ 当成模 $p^2$ 的一。

式 (14) 已把实际高 log 写成有限超几何系数与调和和。
它仍含低 log 的有限指数和真正的 (12) 下一位；本篇没有把它冒称一个已知非零的经典 Jacobi 和。

## 4. 二挠反射的单位常数和原 Z 的全局 cocycle

令
$$
\bar t(q)=q^rg(q)\in\mathbf F_p[q].
$$
由 $g+4qg'=(1-4q)^{r-1}$ 和 $r\equiv1/4$，
$$
\bar t'(q)=\frac14q^{r-1}(1-4q)^{r-1}.
$$
这个导数在 $q\mapsto1/4-q$ 下不变，且 $\deg\bar t=d<p$，
所以准确有
$$
\boxed{\quad
\bar t(q)+\bar t(1/4-q)=C,\qquad
C=\bar t(1/4)=-\frac1{2\kappa}\in\mathbf F_p^\times.
\quad}
\tag{15}
$$
常数的计算可用有限 beta 恒等式
$$
g(1/4)=
\sum_{j=0}^{r-1}\frac{(-1)^j\binom{r-1}j}{4j+1}
=\frac{(r-1)!}{4(1/4)_r}.
$$
约化 $(1/4)_r\equiv(2r-1)!/(r-1)!$，再用
$\kappa=\binom{2r-2}{r-1}/4^{r-1}$，即得 (15)。

现在回到原固定 $E^+$，取其有理奇参数
$$
\nu=-X/Y,\qquad \nu=z+\cdots.
$$
有 $\nu^4=q(1-4q)$，且对 R207 原 $Z$，
$$
\boxed{\quad \bar t=\nu^pZ.\quad}
\tag{16}
$$
四次方由 $Z^4=qg^4/(1-4q)^p$ 立即得到；
原点首系数均为一，确定了四次根的单位。

令 $\tau$ 为平移 $T'=(0,0)$：
$$
X\circ\tau=4/X,\quad
Y\circ\tau=-4Y/X^2,\quad
q\circ\tau=1/4-q,\quad \nu\circ\tau=-\nu.
$$
因此在原函数域中有真正的 Frobenius 平移式
$$
\boxed{\quad
Z\circ\tau=Z-C\nu^{-p}.
\quad}
\tag{17}
$$
这是同一个原 degree-$p$ 参数的恒等式，不是另选一个 primitive，
也没有把特征零 $q^rF_+(q)$ 宣称为全局有理函数。

坏常数的尺度不可忽略。若 $\widehat C\in O^\times$ 为 $C$ 的任意整提升，则
$$
p\ell_+\widehat C\equiv\alpha C=-34\pmod p.
\tag{18}
$$
所以 $\ell_+\widehat C$ 的赋值准确为 $-1$。
不能直接使用不收敛的 $\exp(\ell_+\widehat C)$，
也不能把它当作一个整常数 gauge。

## 5. 原 theta 的两个 Mumford 运输 frame

原 $\Theta=\vartheta(2z)^{17}$ 在 $E^+$ 上的零除子是
$$
D=17(P_++P_-),\qquad P_\pm=(\pm2i,0).
\tag{19}
$$
可由原双倍恒等式
$\vartheta(2z)=\vartheta(z)^4(1+s)$ 直接读出：
$[2]^{-1}(0,0)$ 的四个原零点经严格二同源降为 $P_\pm$，
次数和重数均保留。于是原线丛可写为 $\mathcal O(D)$。
平移 $\tau$ 交换 $P_+,P_-$，故 $\tau D=D$。

使用这一不变除子给出的线性化：它固定实际截面的规范 section，
并且平方为恒等。将原点的实际 theta 形式 frame 沿此线性化运输到 $T'$，
在局部坐标 $q_T=1/4-q$ 下，原始 theta 系数就是同一个
$\exp\mathcal L(q_T)$。这是对实际 frame 的运输，保留 theta 自动因子；
不是宣称未经正规化的 holomorphic 标量 $\Theta(z+T')$ 等于 $\Theta(z)$。

下面仅比较这两个实际 frame 的有限 jet。原有理列仍须分别运输：
$a_0(q)$ 与 $b_0(q)(1-4q)^{-d}$ 在 $\tau$ 下会变成相应的
$1/4-q$ 代入，后者的极点也会移动。不能只运输公共 theta frame
而把两条有理列原封不动认作它们的平移。

## 6. 准确的有限 Dwork 修正与真正收敛的双端单位

这一步支付 (18)，而不使用坏常数的指数。取 $C$ 的 Teichmüller 提升
$\widehat C\in\mathbf Z_p^\times$，故 $\widehat C^p=\widehat C$。
由两个互素的整理想 $q^{2r}$ 和 $(q-1/4)^{2r}$，
存在唯一次数至多 $4r-1=p$ 的整多项式 $\widehat t(q)$，满足
$$
\begin{aligned}
\widehat t(q)&\equiv t_+(q)\pmod{q^{2r}},\\
\widehat t(q)&\equiv
\widehat C-t_+(1/4-q)\pmod{(q-1/4)^{2r}}.
\end{aligned}
\tag{20}
$$
两个端点相差单位，故 Hermite 插值不引入 $p$ 分母。
唯一性和反射给
$$
\widehat t(q)+\widehat t(1/4-q)=\widehat C,\qquad
\overline{\widehat t}=\bar t.
\tag{21}
$$
这里 (21) 的约化使用 (15) 及同一插值唯一性。

令
$$
\mathscr D(T)=T-T^p,\qquad
B_{\widehat C}(T)
=\frac{(\widehat C-T)^p-\widehat C^p+T^p}{p}\in O[T].
$$
$p$ 为奇数，因此
$$
\boxed{\quad
\mathscr D(\widehat C-T)+\mathscr D(T)
=-p B_{\widehat C}(T).
\quad}
\tag{22}
$$
原点处 $\widehat t^p$ 从 $q^{rp}$ 开始；
用 $\ell_+\mathscr D(\widehat t)$ 代替 $\ell_+t_+$，
不改变原两权所读的 theta 系数。

在 $O$ frame 中取负号 gauge
$-\ell_+\mathscr D(\widehat t)$；
在 $T'$ frame 中取正号 gauge
$+\ell_+\mathscr D(\widehat t)$。
因为 $\mathscr D(\widehat C)=0$，后者也有零初始指数。
运输回原点后，两者之比的形式对数是
$$
P(T)=-p\ell_+B_{\widehat C}(T)\in O[T].
\tag{23}
$$
它在 $T=0,\widehat C$ 都为零，且反射不变。
由于 $2$ 可逆，整不变多项式环是
$O[T(\widehat C-T)]$。写
$$
S=T(\widehat C-T),\qquad
P(T)=\sum_{j=1}^{d}a_jS^j,\qquad a_j\in O.
\tag{24}
$$
首系数准确为
$$
a_1=p\ell_+\widehat C^{\,p-2}.
\tag{25}
$$

为了支付局部收敛，使用真正的 Artin–Hasse 指数
$$
\operatorname{AH}_p(U)
=\exp\left(\sum_{n\ge0}\frac{U^{p^n}}{p^n}\right)
\in1+U\mathbf Z_p[[U]].
$$
其整性可直接由 Euler 乘积证明：
$$
\operatorname{AH}_p(U)
=\prod_{\substack{n\ge1\\p\nmid n}}(1-U^n)^{-\mu(n)/n}.
$$
每个指数属于 $\mathbf Z_p$，其二项式系数整；
每一固定次数只读有限多个因子。取形式对数，
$U^m$ 的系数为
$m^{-1}\sum_{n\mid m,\ p\nmid n}\mu(n)$，
即只在 $m$ 为 $p$ 的幂时留下 $1/m$，证明乘积式。
整系数还保证它在 $|U|_p<1$ 收敛。

于是
$$
\boxed{\quad
\mathcal E(S)=
\prod_{j=1}^{d}\operatorname{AH}_p(a_jS^j)
\in1+SO[[S]]
\quad}
\tag{26}
$$
是真正的整单位，且
$\log\mathcal E(S)-P(T)$ 从 $S^p$ 开始。
在原点和 $T'$ 的两个剩余盘，$|S(\widehat t(q))|_p<1$，
所以 (26) 在两端都收敛。其与 (23) 的形式比较在两个端点都保留原两权。
本论证没有把 $\exp(P)$ 在整个单位盘上的收敛当作事实；
收敛的是 (26)，原 theta 在这里使用的是已支付的有限 jet。

## 7. 最短双端过渡对原 K 的准确作用与极点位置

由于 $S(\widehat t)$ 在两个端点均从局部第 $r$ 次开始，
两权乘原正次列时只需 (26) 的第一项。由 (25)，
$$
\boxed{\quad
\mathcal E(S(\widehat t(q)))
=1+p\ell_+t_+(q)+O(q^{2r}).
\quad}
\tag{27}
$$
这里使用 $\widehat C^{p-1}=1$；$S=\widehat C\widehat t-\widehat t^2$，
而平方项从 $q^{2r}$ 开始。
因此把这个共同整 frame 单位作用于同一原两列时：

- 第一行及其模 $p^2$ 准确不变；
- 第二整行模 $p$ 的变化为 $\alpha\,\overline{R_1}$；
- 在原首行失败后，整个 $K$ 的变化为零。

这是对实际两权的计算，不是用一个不收敛的常数指数作形式相消。
它也不把两条有理列的二挠平移无证认成原列。
这个最短双端整修复仍没有给 $K$ 新的非零项。

全局极点的位置同样必须保留。
$\widehat t$ 是 $q$ 多项式，故其额外极点只在 $q=\infty$，
即固定 $P_\pm$，而这里 $Z=0$；$\widehat t^p$ 的二次 $p$ 规模极点仍在这两个点。
在 $T'$，$\widehat t=\widehat C$，没有极点。
任何有限 Artin–Hasse 多项式完成也在 $T'$ 正则。

因此，对这些在 $T'$ 正则的有限 $q$ 多项式完成，
R219 的完整迹仍只有常数和负四倍幂，全部正中央系数仍为零。
次数变成 $O(p^2)$ 本身不足以产生正权；极点必须到 $Z=\infty$ 的原 $T'$ 才会改变该结论。
这里没有给无限解析级数凭空定义全局函数域迹；
全局迹只对所述有限有理代表使用。

## 8. 把 p² 极点真正放到 T'：已知正权单位与非 O 项准确抵消

也可以明确支付正确位置的二次极点成本，检验它是否产生新算术收益。
令 $m=p+1$，使用 R219 的同一特征零 $\widehat Z$。
对两条原列作同一个有限参考修正
$$
\boxed{\quad
\Xi^\sharp=\Xi+p\widehat Z^{\,m}.
\quad}
\tag{28}
$$
因为 $m$ 是四的倍数，$\widehat Z^m$ 是 $q$ 的有理函数。
它在原点从 $z^m$ 开始；两条裸列均从 $z^4$ 开始，
故 (28) 不改原第一行，第二整行只改一个 $p$ 倍整向量。
原对数校正的第一权也不变。因此 (28) 保持同一实际 $K$，
并没有把修改后的全局代表冒称原 theta。

现在 $\widehat Z^m$ 的极点确实位于 $T'$，阶数 $pm=p^2+p$。
记同一覆盖下的裸迹为
$$
\operatorname{Tr}\bigl(b_0(q)(1-4q)^{-d}\bigr)=C_{b,p}\in O^\times.
$$
它在特征零就为常数：原裸列在 $P_\pm$ 正则，唯一极点在 $T'$，
迹的多项式次数至多一，再由 $\mu_4$ 只留常数。
R207 给
$$
\overline{C_{b,p}}=\kappa\,2261/81920.
\tag{29}
$$
裸 $a_0$ 的迹则只有负四倍幂，常数为零。

故 (28) 使完整迹的两条正中央行准确变为
$$
\mathcal T_1^\sharp=(0,pC_{b,p}),\qquad
\mathcal T_2^\sharp=(0,0).
$$
完整迹的归一后继行于是含有真正已知单位
$$
\boxed{\quad
\overline{\mathcal T_2^\sharp-\ell\mathcal T_1^\sharp}
=(0,-\alpha\overline{C_{b,p}}).
\quad}
\tag{30}
$$
这里 $\ell$ 是 R219 的原参考 gauge，$p\ell\bmod p=\alpha$。

但非原点聚合的变化也完全可计算。记原 $\mathcal D_j,\mathcal N_j$
为 R219 的原点、非原点两行。由局部原点首阶，
$$
\mathcal D_1^\sharp=\mathcal D_1,\qquad
\mathcal D_2^\sharp-\mathcal D_2\in pO^2.
$$
相应地，
$$
\mathcal N_1^\sharp-\mathcal N_1=(0,pC_{b,p}),\qquad
\mathcal N_2^\sharp-\mathcal N_2\in pO^2,
$$
所以在首行失败后，
$$
\boxed{\quad
\overline{
(\mathcal N_2^\sharp-\ell\mathcal N_1^\sharp)
-(\mathcal N_2-\ell\mathcal N_1)}
=(0,-\alpha\overline{C_{b,p}}).
\quad}
\tag{31}
$$
它与 (30) 是同一个单位，准确相消，原点 $K$ 没有改变。
因此这份真正的 $p^2$ 极点成本修正能够将裸单位送入正中央全迹，
却不能以它排除完整中央双零：非原点聚合同步承担了全部新单位。
要有新收益，仍须证明同一个实际非原点聚合受到额外控制。

## 9. 同一 p43 的准确校准与保留的问题

本篇只复用已有 $p=43$。在原 q 参考的实际计算中，
$\kappa=30,\alpha=19$，(6) 的 $A_j$ 为
$$
(0,36,5,5,8,11,27,0,2,35,39),
$$
而 $H_p$ 的系数为
$$
(0,13,13,33,30,24,18,0,7,16,42).
$$
由 (8) 生成的 $\Gamma_+$ 与从 R219 实际 $\Xi$ 经 (11) 恢复的
全部 $0,\ldots,21$ 次系数一致。反射常数为 $C=5$，
整条 (15) 的多项式恒等式也准确成立。

(14) 的低指数第二行是 $(5,19)$，
$\mathscr L(H_p/g-\log g)=(10,16)$。
沿此前已用的原行列式一列 $B-20A$，
真实第一行除 $p$ 为 $u=8$，所以
$$
K=(19-20\cdot5)-19\cdot8+
19(16-20\cdot10)=12\pmod{43}.
$$
这与 R213 的原有理计算及 R219 的全纤维比较一致。
这些有限域计算在 JavaScript 中准确执行，没有扩大素数列表，
也没有将原首行非双零的样本冒称双零条件下的证据。

目前真正已付的内容是：实际高 log 由 (6)–(10) 给出；
原第一行的下一位由 (12) 保留；二挠反射在同一 $Z$ 上的 cocycle
由 (15)–(17) 给出；坏 $1/p$ 常数由 (20)–(27) 的有限整双端过渡处理。
自然最短修复对首行失败后的 $K$ 不产生新项；
把极点真的移到 $T'$ 后，新全迹单位又由 (31) 的非原点项准确承担。

因此仍须控制 (14) 的实际有限表达，或同一完整 theta frame 下
R219 的非原点聚合。已有 primitive 反射、有限 Heisenberg 线性化、
局部 Artin–Hasse 收敛和全迹单位都没有单独证明该剩余非零。
