# R432：十八个原第三核的零阶零子空间与全部内部退化点的共同响应矩阵

日期：2026-11-16。**只读已付原式并作手工证明；没有执行新的符号消元、profile 评价、积分、秩、零点或开发检查。**

本文完整分类原十八维第三对角核中局部自伴算子的零阶系数恒零的方向。该子空间准确为五维；给出五个真实原算子的全部 $a,b,c$，并从原十八个生成元证明没有遗漏。它不是整个第四 whole-$E$ 核的分类。

对当前逐包比例圆，五个方向产生的全部内部 partial 有准确同锚公式。其中一方向在每个 $A_f$ 点恒零，其余方向给三十二个原响应标签。两通道中的 ordered 残差 $C$ 又准确归为七个 jet 函数与三个真实 suffix 矩的共同乘积，即二十一个生成函数。这些数目不是某个实际圆的矩阵秩。

最后消费已发表 [R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md)：所有实际 $A_f$ 点的矩阵可以由同一个参考母在全部外根上的六项数据、真实幅宽中心和 suffix 读取。根的数目仍是任意有限数；“六项”指每根的数据项数。

直接来源：[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R258](R258-self-adjoint-hook-green-operator-and-complete-period-interface.md)、[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R297](R297-ordered-platform-matrix-surjective-pure-zero-responses-and-real-control.md)、[R345](R345-local-whole-E-kernel-orbit-and-eleven-corresponding-degenerate-fluxes.md)、[R394](R394-conditional-complete-period-and-finite-same-gauge-interface.md)、[R399](R399-new-whole-E-natural-kernel-and-four-ordered-internal-period-controls.md)、[R408](R408-independent-second-gauge-invariant-fluxes-and-natural-character-extension.md)、[R429](R429-complete-kk-minus4-values-and-actual-common-joint-sections.md)、[R430](R430-complete-packet-partial-fluxes-a-new-joint-kernel-and-the-remaining-internal-quotient.md)。

## 1. 原十八维空间和本稿分类的对象

原第三空间的最后两槽对称。令
$$
Z=\{\tau:\tau(u;u,u)=0\ \text{对全部允许真紧 }u\},
\qquad K_u^\tau(w)=\tau(w;u,u).
$$
R255/R261 的完整原生成元为
$$
Z=\operatorname{span}\{
H_j=\delta^j\mathfrak H:0\le j\le6;\
J_j=\delta^j\mathfrak J_0:0\le j\le2;\
\chi_{30},\chi_{32},\chi_{34},\chi_{37},
\chi_{40},\chi_{100},\chi_{104},\chi_{109}\},
\quad\dim Z=18.
\tag{1}
$$
其中
$\mathfrak H=C(P,S)-3C(P,R)$，$\mathfrak J_0$ 为 R255(5)—(6)的完整五交换子组合。
$\delta$ 是输出和全部输入槽同时作用的原导子，不是只对固定 profile 输出求交换子。

记
$$
p=u',\quad r=u'',\quad t=u''',\quad
A=6pt-2r^2,\qquad \mathcal L=(rt)'=t^2+r u^{(4)}.
$$
每个 $\tau\in Z$ 的完整原式都满足
$$
D^3K_u^\tau=\mathscr A_{\tau,u},\qquad
\mathscr A_{\tau,u}=D^2(a_\tau D^2)+D(b_\tau D)+c_\tau,
\qquad \mathscr A_{\tau,u}u=0,
\tag{2}
$$
并且形式自伴。原右锚为
$$
Jv(x)=\int_x^{r_*}v(y)\,dy,\qquad
K_u^\tau=-J^3\mathscr A_{\tau,u}.
\tag{3}
$$
右端三个零常数由原恢复支付；左二次尾保留。R261 已证明 $\tau\mapsto\mathscr A_{\tau,\cdot}$ 在 universal 原空间单射。

本稿分类的是
$$
Z_{c0}=\{\tau\in Z:c_{\tau,u}(x)\equiv0
\ \text{为全部 }x,u\text{ 的原 jet 多项式身份}\}.
\tag{4}
$$
这比在某一母、某些点或某个 self 积分上为零严格。也不能把(4)等同于
$\mathcal R\cap\ker E$：后者允许不同响应间的 whole self 相消及第三对角非零来源。

## 2. 五个准确原方向及全部局部系数

沿 R399 记
$$
\tau_*=64(\chi_{34}-3\chi_{32})-\mathfrak J_0/2 .
$$
定义以下五个完整原算子：
$$
\begin{aligned}
\sigma&=\tau_*/2,\\
\tau_0&=\mathfrak H,\\
\tau_1&=-\frac18(H_1+1024\chi_{30}),\\
\tau_2&=\frac1{20}(H_2+5120\chi_{32}+16J_0),\\
\tau_3&=-\frac1{40}(H_3+5120\chi_{37}-4J_1).
\end{aligned}
\tag{5}
$$
R430 的新方向正是 $\tau_1$。全部五项都在原 $Z$ 中；没有新增模板或假设整个补空间对 $\delta$ 闭合。

其完整系数为：

| 方向 | $a$ | $b$ | $c$ |
|---|---|---|---|
| $\sigma$ | $p^2$ | $-2r^2-pt$ | $0$ |
| $\tau_0$ | $A$ | $-6\mathcal L$ | $0$ |
| $\tau_1$ | $xA+2pr$ | $-6x\mathcal L-10rt$ | $0$ |
| $\tau_2$ | $x^2A+4xpr-4p^2$ | $-6x^2\mathcal L-20xrt+4r^2+4pt$ | $0$ |
| $\tau_3$ | $x^3A+6x^2pr-4xp^2$ | $-6x^3\mathcal L-30x^2rt-4xr^2+4xpt+4pr$ | $0$ |

此表给的是自伴夹心形式(2)的 $b$；不是展开算子的 $D^2$ 系数。

统一写为
$$
a=GA+2G'pr+Fp^2,
\tag{6}
$$
则五行的 $(G,F)$ 分别是
$$
(0,1),\quad(1,0),\quad(x,0),\quad(x^2,-4),\quad(x^3,-4x),
$$
且
$$
\boxed{
b=-6G(rt)'-10G'rt-2G''r^2-F'pr-F(2r^2+pt),\qquad c=0.
}
\tag{7}
$$
直接微分给
$$
(ar)'+bp=0.
\tag{8}
$$
因此表中每一行都满足完整 $\mathscr A u=0$。以下另从原生成元核 $c=0$，不以(8)反向猜测一个未获准的原算子。

### 2.1 原递推与真正的 $c$ 消项

令 $\mathscr D=x^2D-2x$。由 R258(19)—(21)，在完整自伴系数上，
$$
\begin{aligned}
a_{\delta\tau}&=x^2Da_\tau-2xa_\tau-D_u a_\tau[\mathscr Du],\\
b_{\delta\tau}&=x^2Db_\tau+2xb_\tau+2Da_\tau-D_u b_\tau[\mathscr Du],\\
c_{\delta\tau}&=x^2Dc_\tau+6xc_\tau+2Db_\tau-D_u c_\tau[\mathscr Du].
\end{aligned}
\tag{9}
$$
这里 $D$ 微分显式 $x$ 和全部 jets；$D_u$ 同时微分两个内槽。不能省掉(9)的最后一项。

记
$$
\mathcal R=(rt)''=r u^{(5)}+3t u^{(4)},\qquad
\bar c_j=256c_{\chi_j}.
$$
原系数逐次给
$$
\begin{aligned}
c_{H_1}&=-12\mathcal R,\\
c_{H_2}&=120x\mathcal R-24p u^{(5)}
 +248r u^{(4)}+272t^2,\\
c_{H_3}&=-720x^2\mathcal R+288xp u^{(5)}
 -2976xr u^{(4)}-3264xt^2
 +768p u^{(4)}-1536rt,\\
c_{J_0}&=4p u^{(5)}+12r u^{(4)}+8t^2,\\
c_{J_1}&=-8xp u^{(5)}-24xr u^{(4)}-16xt^2
 -8p u^{(4)}+16rt .
\end{aligned}
\tag{10}
$$
R261 的原表为
$$
\begin{aligned}
\bar c_{30}&=3\mathcal R,\\
\bar c_{32}&=-2p u^{(5)}-22r u^{(4)}-20t^2-6x\mathcal R,\\
\bar c_{34}&=2p u^{(5)}-42r u^{(4)}-44t^2-18x\mathcal R,\\
\bar c_{37}&=-40p u^{(4)}+80rt
 -16xp u^{(5)}+144xr u^{(4)}+160xt^2+36x^2\mathcal R .
\end{aligned}
\tag{11}
$$
于是完整地有
$$
\begin{gathered}
\bar c_{34}-3\bar c_{32}=2c_{J_0},\qquad
c_{H_1}+4\bar c_{30}=0,\\
c_{H_2}+20\bar c_{32}+16c_{J_0}=0,\qquad
c_{H_3}+20\bar c_{37}-4c_{J_1}=0 .
\end{gathered}
\tag{12}
$$
这逐项支付(5)全部 $c$，包括非最高 jet 项。

原 $a$ 表直接给第2节的五个 $a$。原 $\mathscr A u=0$、$c=0$ 和右 collar 迫(8)，从而给唯一多项式 $b$，恰为(7)。因此没有只比较 $a$ 或某个 principal 后宣称完整局部算子相同。完整 $a,b,c$ 相同再由(3)的右三常数，才给原 $K$ 相同。

## 3. 原十八方向中的穷尽性：恰为五维

### 3.1 一个必要的 universal 多项式条件

原十八个 $a$ 均是 $u,p,r,t$ 的二次多项式，其 monomial 只可能为
$$
u^2,\ up,\ ur,\ ut,\ p^2,\ pr,\ pt,\ r^2
\tag{13}
$$
乘显式 $x$ 多项式。

若 $c=0$，原 $\mathscr A u=0$ 和右平端给(8)。
把(8)作为 universal jet 身份，在自由 jet $p=0$ 上评价，不能以某个实际 profile 恰有 $p=0$ 代替这个代数论证。

写(13)的系数依次为 $A_0,\ldots,A_7$。在 $(ar)'|_{p=0}=0$ 中：

- $u^2t$ 迫 $A_0=0$；
- $ur u^{(4)}$ 迫 $A_3=0$；
- $urt$ 迫 $A_2=0$；
- $ur^2$ 再迫 $A_1=0$；
- 余下 $r^3,r^2t$ 分别给 $A_5=-A_7'$、$A_6=-3A_7$。

因此任何 $c=0$ 原方向必有(6)，其中 $G=-A_7/2$、$F=A_4$。特别，**其 $a$ 的全部含 $u$ 项必须消失**。

这只是必要条件。下面使用全部十八原方向限制它，再用(12)的五个真解给充分性，因而不遗漏相同 $a$、不同 $c$ 的可能。

### 3.2 原七链、三链的有限 $a$ 呈示

由(9)逐项递推，可将原七条 $a_{H_j}$ 写成同一个有限多项式：
$$
\begin{aligned}
\sum_{j=0}^6\frac{z^j}{j!}a_{H_j}
={}&(1-zx)^6A
+z(1-zx)^5(12ut-8pr)\\
&-8z^2(1-zx)^4(ur+p^2)
-16z^3(1-zx)^3up
-8z^4(1-zx)^2u^2 .
\end{aligned}
\tag{14}
$$
原三条 $a_{J_j}$ 为
$$
\sum_{j=0}^2\frac{z^j}{j!}a_{J_j}
=-4\{(1-zx)^2(p^2+ur)+6z(1-zx)up+6z^2u^2\}.
\tag{15}
$$
(14)—(15)是原有限递推的系数恒等，不是新采样或形式维数假设。例如
$$
a_{H_1}=-6xA+12ut-8pr,\quad
a_{H_2}=30x^2A-120xut+80xpr-16ur-16p^2,
$$
与(9)直接一致。

### 3.3 其余八条原 $a$，不遗漏整个补空间

记 $\bar a_j=256a_{\chi_j}$；下列矩阵中的 $\bar\chi_j=256\chi_j$ 只是同一原列的非零常数归一。R261 完整表给
$$
\begin{aligned}
\bar a_{30}&=-3ut-2pr+x(-3pt+r^2),\\
\bar a_{32}&=4ur+6xut+x^2(-3pt+r^2),\\
\bar a_{34}&=4ur+18xut+x^2(-9pt+3r^2),\\
\bar a_{37}&=-8xur+x^2(-36ut+12pr)+x^3(24pt-8r^2),\\
\bar a_{40}&=4x^2ur+x^3(12ut-4pr)+x^4(-6pt+2r^2),\\
\bar a_{100}&=-32up+64xur+x^2(48ut-32pr)+x^3(-48pt+16r^2),\\
\bar a_{104}&=96u^2-64xup-32x^2(ur+p^2)
 +x^3(-192ut+96pr)+x^4(120pt-40r^2),\\
\bar a_{109}&=-64x^2up+64x^3(ur+p^2)
 +x^4(192ut-96pr)+x^5(-96pt+32r^2).
\end{aligned}
\tag{16}
$$

这些原方向按真实仿射权分组如下。表中最后一列仅是“所有含 $u$ 的 $a$ 系数消失”这一必要条件的解空间维数，随后由真解填满。

| 真权 | 原方向 | 必要条件核维数 |
|---:|---|---:|
| $-5$ | $H_0$ | $1$ |
| $-4$ | $H_1,\chi_{30}$ | $1$ |
| $-3$ | $H_2,J_0,\chi_{32},\chi_{34}$ | $2$ |
| $-2$ | $H_3,J_1,\chi_{37},\chi_{100}$ | $1$ |
| $-1$ | $H_4,J_2,\chi_{40},\chi_{104}$ | $0$ |
| $0$ | $H_5,\chi_{109}$ | $0$ |
| $1$ | $H_6$ | $0$ |

真实不同权不能在 universal 齐次 jet 恒等式中互消。下列手写小矩阵完整验证最后一列；没有执行新矩阵计算。

权 $-4$ 只需比较 $ut$，系数为 $12,-3$，故核一维。

权 $-3$ 按列 $(H_2,\bar\chi_{32},\bar\chi_{34},J_0)$，行 $(xut,ur)$，矩阵为
$$
\begin{pmatrix}
-120&6&18&0\\
-16&4&4&-4
\end{pmatrix}.
\tag{17}
$$
两行独立，核恰二维。

权 $-2$ 按列 $(H_3,\bar\chi_{37},\bar\chi_{100},J_1)$，行 $(x^2ut,xur,up)$，矩阵为
$$
\begin{pmatrix}
720&-36&48&0\\
192&-8&64&8\\
-96&0&-32&-24
\end{pmatrix}.
\tag{18}
$$
后三列的行列式为 $36864\ne0$，故核一维。

权 $-1$ 按列 $(H_4,\bar\chi_{40},\bar\chi_{104},J_2)$，行 $(x^3ut,x^2ur,xup,u^2)$，矩阵为
$$
\begin{pmatrix}
-2880&12&-192&0\\
-1152&4&-32&-8\\
1152&0&-64&48\\
-192&0&96&-48
\end{pmatrix}.
\tag{19}
$$
若系数为 $(h,a,b,c)$，四行归一后是
$$
a-16b=240h,\quad a-8b-2c=288h,\quad
c-\frac43b=-24h,\quad c-2b=-4h .
$$
后两式给 $b=-30h,c=-64h$，第一式给 $a=-240h$；第二式变为 $128h=288h$，所以全零。

权0时，$a_{H_5}$ 含 $1920xu^2$，而 $\bar a_{109}$ 无 $u^2$；先迫 $H_5$ 系数零，再由 $192x^4ut$ 迫另一系数零。权1时，$a_{H_6}$ 含 $-5760x^2u^2$，故无解。

所以必要条件空间至多五维。式(5)给五个真 $c=0$ 方向；其不同权已经分开，权 $-3$ 的 $\sigma,\tau_2$ 又由 $p^2$ 与 $x^2A$ 独立。于是得到准确结论
$$
\boxed{
Z_{c0}=\operatorname{span}\{\sigma,\tau_0,\tau_1,\tau_2,\tau_3\},
\qquad\dim Z_{c0}=5.
}
\tag{20}
$$

若担心同一个 $a$ 携带不同 $c$，上述证明已经排除：任何 $c=0$ 原方向必在(17)—(19)等必要条件的五维核里，而整个核已由(5)的真 $c=0$ 方向填满。另若 $c=0,a=0$，则(8)迫 $bp=0$ 的 universal 身份，故 $b=0$；由原右三常数和内槽极化，$\tau=0$。因此不是只对最高系数作了非忠实分类。

## 4. 真仿射闭包与完整响应核

原平移导子 $N$ 在(2)的系数上等于只对显式 $x$ 求导；输入 jets 的导数在完整输入/输出作用中相消。原锚与零 collar 同时输运。由完整系数表及(3)的唯一性，
$$
\boxed{
N\sigma=N\tau_0=0,\quad
N\tau_1=\tau_0,\quad
N\tau_2=2\tau_1,\quad
N\tau_3=3\tau_2+8\sigma.
}
\tag{21}
$$
真实正伸缩权依次为 $-3,-5,-4,-3,-2$。
因此(20)在原平移和正伸缩下稳定。这里不声称它在 $\delta$ 下稳定；(9)的 $2b'$ 一般会重新产生零阶项。

对任意 $\tau\in Z_{c0}$、$E\in E_8$，原响应
$\mathcal B_E\tau$ 有 universal pure 零。R297 的完整 self 左二次尾为
$$
\mathfrak q_u(\mathcal B_E\tau)
=-\frac14\int c_{\tau,u}\Phi_E(u,u)=0.
$$
完整自然总通量也为零：
$$
2\int u'''K_u^\tau(\Phi_E(u,u))
=-2\int u\,\mathscr A_{\tau,u}\Phi_E(u,u)
=-2\int(\mathscr A_{\tau,u}u)\Phi_E(u,u)=0 .
\tag{22}
$$
紧 outer $u$ 与紧局部系数支付所有分部边界；inner $\Phi_E(u,u)$ 的真实左二次尾没有删去。故
$$
\boxed{
\mathcal B(E_8,Z_{c0})
\subset\mathcal R\cap\ker E\cap\ker\Lambda_{\rm all}
\subset\ker J .
}
\tag{23}
$$
这里 $J$ 是 R429 当前实际共同的 whole-$E$ 加 finite-natural 查询，不是新的全自然实际满射声明。

## 5. 同一圆全部内部点的完整两通道矩阵

沿 R430 固定
$$
f=\sum_i a_i u_i,\quad g=\sum_i b_i u_i,\quad
u_i(x)=U_i((x-\xi_i)/w_i),\quad w_i>0,\ a_i\ne0,
$$
所有幅度已进入 $a_i,b_i$，支撑闭包不交。
记
$$
R_i=a_i^2-b_i^2,\quad T_i=a_ib_i,\quad
n_{R,i}=\sum_{j>i}R_j\mu_j,\quad
n_{T,i}=\sum_{j>i}T_j\mu_j,\quad
n_i=T_i n_{R,i}-R_i n_{T,i}.
\tag{24}
$$
$\mu_j$ 是原全部三矩，次序、宽度、幅权、八/十二复制均真实保留。

令
$$
q_E(u)=\Phi_E(u,u),\qquad
\mathscr D_E[u]=p\,q_E(u)''-r\,q_E(u)' .
$$
原 $q_E$ 可带左尾。原多项式左尾记为 $p_E(n)$，不是独立可指定的函数。

对任何 $c=0$ 的原 $Z$ 方向，(2)—(3)给
$$
(K_uw)''=(aw'')'+bw',\qquad
\boxed{\int_{\ell_u}^x p(K_uw)''=a(pw''-rw').}
\tag{25}
$$
第二式由(8)直接微分，左平端使原函数零；不要求 $w$ 左紧。

在逐包比例圆上，局部算子杀每个本包比例输入，且原右三常数均零，故完整 $K_f^\tau(g)=0$。因此 R255 全响应的另一 history 项准确消去，
$$
\mathcal B_E\tau(f^2,\phi_\theta)=2K_f^\tau(\Phi_E D_\theta).
\tag{26}
$$
这不是仅靠不交支撑删掉 $\Phi_E(\phi,K_f^\tau\phi)$。

原 $V_d,V_e,H_d,H_e$ 仍按 R430 定义。对包 $i$ 中每一个实际点 $x$，(25)—(26)给
$$
\boxed{
\begin{aligned}
H_{d,i}( \mathcal B_E\tau)(x)
&=2a_i^3 a_\tau[u_i](x)
\{R_i\mathscr D_E[u_i](x)
+p_i p_E(n_{R,i})''-r_i p_E(n_{R,i})'\},\\
H_{e,i}( \mathcal B_E\tau)(x)
&=-2a_i^3 a_\tau[u_i](x)
\{T_i\mathscr D_E[u_i](x)
+p_i p_E(n_{T,i})''-r_i p_E(n_{T,i})'\}.
\end{aligned}}
\tag{27}
$$
左方 inner 包处于准确右零区；右方 inner 包给(24)的真实二次左尾。同包 self 和右尾的全部系数仍在(27)中。

在全部实际 $A_i=0$ 根上，$\tau_0$ 的 $a=A_i$ 使两行都为零。其余四方向乘全部八个 $E$ 给 **32 个非盲原成本标签**。这是全点矩阵的明确列清单，不保证标签独立，也没有把每一包的系数分别自由化。若另加入 R345 十一条完整局部轨道，可用43个标签记录更大的已知核；仍不由此宣称全点像满。

R430 的两通道组合
$$
C_i=R_iH_{e,i}+T_iH_{d,i},\qquad
D_i=R_iH_{d,i}-T_iH_{e,i}
$$
始终可逆，因为 $R_i^2+T_i^2>0$。其中 self 在 $C_i$ 精确消掉，
$$
\boxed{
C_i(\mathcal B_E\tau)(x)
=2a_i^3 a_\tau[u_i](x)
\{p_i p_E(n_i)''-r_i p_E(n_i)'\}.
}
\tag{28}
$$
式(28)不能替代(27)的另一个通道。

## 6. $C$ 像的准确七函数乘积与二十一个共同生成式

在实际 $A_i=0$ 点，$p_i\ne0$。置
$$
s=\frac{r_i}{p_i},\qquad t_0=xs-1 .
$$
这里 $t_0$ 是无量纲 jet 比值，不是 $u'''$。四个非盲 $a/p_i^2$ 依次为
$$
1,\qquad 2s,\qquad 4t_0,\qquad 2x(3t_0+1).
\tag{29}
$$
若 $p_E(n)=\alpha x^2+\beta x+\gamma$，则
$$
\frac{p_i p_E(n)''-r_i p_E(n)'}{p_i}
=-\beta s-2\alpha t_0.
\tag{30}
$$
常数尾 $\gamma$ 仍是真实原值，只在此导数表达中自然消失。

因此单一矩分量的乘积空间准确为
$$
\boxed{
\mathscr G=
\operatorname{span}\{1,s,t_0,s^2,st_0,t_0^2,\ x t_0(3t_0+1)\}.
}
\tag{31}
$$
前六个非恒常乘积先给 $s,t_0,s^2,st_0,t_0^2$，且
$$
xs(3t_0+1)=(t_0+1)(3t_0+1)=3t_0^2+4t_0+1
$$
给常数，最后保留 $xt_0(3t_0+1)$。
等价的显式多项式基是
$$
1,\ s,\ xs,\ s^2,\ xs^2,\ x^2s^2,\
3x^3s^2-5x^2s+2x.
\tag{32}
$$
按最高 $x^3s^2$ 等 monomial 可逐项证明这七个函数在自由 $(x,s)$ 上独立。这不证明它们在已经固定的有限根集上仍秩7。

原八尾导数给三个矩的两套独立列。可取
$$
E_j^s=(-R,-U,-T)_j,\qquad
E_j^t=(2L,2V,2Y)_j,\qquad j=0,1,2.
\tag{33}
$$
R259 原左尾分别使(30)为 $n_j s$ 和 $n_jt_0$；例如 $2L$ 另带 $n_2/2$ 常数，完全不影响此身份。于是对于每个矩，七个(31)都由真实响应线性组合取得。常数列可明确取
$$
\frac12\mathcal B_{E_j^s}\tau_3
-\frac34\mathcal B_{E_j^t}\tau_2
-4\mathcal B_{E_j^t}\sigma .
\tag{34}
$$
其余列直接由 $\sigma,\tau_1,\tau_2,\tau_3$ 与(33)取得并除相应非零常数。

所以在**同一个整个实际圆**上，这个模块的 $C$ 向量准确是
$$
\boxed{
C_{i,\alpha}
=2a_i^3p_{i,\alpha}^3
\sum_{j=0}^2(n_i)_j
\,Q_j\!\left(x_{i,\alpha},\frac{r_{i,\alpha}}{p_{i,\alpha}}\right),
\qquad Q_j\in\mathscr G .
}
\tag{35}
$$
同一组三个 $Q_j$ 必须用于全部包、全部根。因此这是二十一个**共同生成函数**的评价像，不是每包二十一自由度，更不是每点可独立选尾。

若 $n_i=0$，(35)当然为零；R430 的完整 ordered 分解事实上已使该包的 $C$ 对全部 whole-$E=0$ 成本自动为零，不只是本模块盲。若 $n_i\ne0$，实际列也可能因为根 jets、镜像、宽度或 suffix 关系降秩。

本分类并未证明任意 actual 成本的目标 $C$ 满足(35)。若后继找到一个读出杀(35)但不杀真实目标，只能先称它是此明确 $c=0$ 模块的剩余条件，不能扩成整个 $\mathcal R\cap\ker E$ 的障碍。

## 7. 用同一共同外区表读取全部实际矩阵

R431 已从起点在同一个 $q=0$、同 $F^\star=(\mathcal F_{\rm rat},D,E_5)$、同十九根构造中取得所有最终母 $U_i$，它们在中心小区间之外与同一个 $u_0$ 完全相同，且整个纤维保持真实三矩。

令 $u_0$ 正半轴上的全部内部 $A$ 根为
$$
0<b_1<\cdots<b_m<1 .
$$
$m$ 是构造所得任意有限数，不预设为1、3或11。全部真实根是
$$
x_{i,\alpha}^{\pm}=\xi_i\pm w_i b_\alpha.
\tag{36}
$$
在每个参考根 $y=\pm b_\alpha$，记录六项真实数据
$$
\boxed{
u_0(y),\quad p_0(y),\quad r_0(y),\quad
J_0(y),\quad J_1(y),\quad J_2(y),
}
\tag{37}
$$
其中
$$
J_0=J(r_0^2),\quad
J_1=J(yr_0^2),\quad
J_2=J(y^2r_0^2+2p_0^2).
$$
这里是每根六项数据、合计 $2m$ 行；不是六个根。
第三 jet 由真实 $A=0$ 给
$t_0(y)=r_0(y)^2/(3p_0(y))$。

原三个 $J$ 值在所有最终母的这些根上准确共同：

- 对右根，其到右端的整个 profile 不变，原右积分直接相同；
- 对左根，用“原全矩减左 cap”表达，两个部分都准确不变；
- 没有把 $J_0,J_1,J_2$ 置零或作为独立自由常数。

对实际 $x=\xi_i+w_i y$，需要代入的原数据是
$$
u_i=u_0,\quad p_i=w_i^{-1}p_0,\quad
r_i=w_i^{-2}r_0,\quad t_i=w_i^{-3}t_0,
\tag{38}
$$
$$
\boxed{
\begin{aligned}
J_0^{\,i}&=w_i^{-3}J_0,\\
J_1^{\,i}&=w_i^{-3}(\xi_iJ_0+w_iJ_1),\\
J_2^{\,i}&=w_i^{-3}(\xi_i^2J_0+2\xi_iw_iJ_1+w_i^2J_2).
\end{aligned}}
\tag{39}
$$
原八个 $q_E',q_E''$ 只用 $u,p,r,t,J_0,J_1,J_2$ 和显式物理 $x$，由 R255(4)直接求导可见。故(37)—(39)足以读取(27)的全部 self 列。完整 suffix 则使用同样输运后的全三矩、实际 $a_j,b_j$ 和原左右次序，按(24)求取。

这给出了全部32列的同一有限原数据接口。显式 $x$ 必须代入真实 $\xi_i\pm w_i b_\alpha$；不能先把各根重标到0而继续使用同一个未经输运的响应。

这个简化只用于原响应列。对任意 actual whole-$E$、finite-$A$ 为零的成本，R431/R407 给的是完整 cap 积分表。它不把一般 actual cap 的密度变成 universal Euler 零，也不证明一般 self 由(37)六项 jets/二次矩决定。一般目标是否属于(27)/(35)仍须原式比较。

## 8. 对 actual 全点和同一十三规范的准确边界

(20)完成原十八维 $Z$ 内的一个完整分类；(27)给它对所有内部点的真实两通道矩阵；(35)给 $C$ 的准确共同21生成式。三个结论都不需要把根数截成一对，不使用虚拟点或采样秩。

令 $\mathcal P$ 为全部实际内部 $H_d/H_e$，$\mathcal R_0=\mathcal R\cap\ker E$。对于已经固定的 $J(V)=0$，保 $J$ 的 signed 响应支付仍恰要求
$$
-\mathcal P(V)\in\mathcal P(\mathcal R_0).
\tag{40}
$$
本稿只显式扩大其中一部分列，没有证明整个(40)。

若能证明全部 $\mathcal P(\ker J)$ 落在同一个真实响应像，R430 §7 的实际原型方案才可以在其独立像坐标中使用：每个 prototype 的 full-$J$ 清零成本也按复制整数乘入 leading 基准；先固定参数盒和后置 full-$J$ 截面，再把所有有界 $C^1$ 余项放入同一次有限整数收缩。仅某个投影满射不能删除像外基准，也不能把 signed span 直接叫实际可达。

更大核仍包括可能的 $c_\tau\ne0$ 响应组合，以及 R247/R255 明确保留的第三对角非零、第四 pure 零来源。它们可能改变(35)的像外读出，本稿没有排除。

即使全部内部 partial 已付，同一个独立二阶规范仍需满足 R394/R408 的真实平台仿射 gluing、两个 period particular、原 seed 和完整十三行相位兼容。式(25)的 current 不增加独立锚常数，R431 的共同 cap 也不授各点可独立选 $w$。本稿不把这些未付条件改写成新的秩宣称。
