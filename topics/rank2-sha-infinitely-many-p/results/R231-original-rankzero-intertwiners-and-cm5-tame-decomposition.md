# R231 — 原行到秩零参考的单位交织、十七处准确投影与实际补偿的五块分解

日期：2026-11-13。**状态：本文的四挠交织、同线丛 norm-five 迹、完整五维矩阵、实际曲线身份和补偿分解已证明。原 A/B 的完整中心导数非同时为零仍未证明。**

本篇接续 [R229](R229-original-heisenberg-companion-projectors-and-complete-mellin.md)。
新增正输入有三项：
原 A、B 各经八项真实四挠运输得到原点值一的实际秩零 theta；
原十七处的五维空间现在有准确积分投影；
R229 的实际 $C_B^-$ 已分解成固定曲线和明确 CM 缩放，全部系数均已计算。
全文保留原公共 gauge、质量和首行模 $p^2$。

## 1. 两个真实交织算子

沿用 R229 的 $T,F,G,H$、$\Theta=T^{17}$、$t=4q$、$\xi=q(1-4q)$，
以及覆盖 $S=\Omega_0/4$、$iS$ 的 $M,N$。
本篇写
$$
\kappa_4=2^{-1/4},
$$
以区别于各素数的 supersingular 常数。
二处向量为
$$
v_0=(1,0,1,0),\qquad v_+=(1,1,-1,1),\qquad
v_-=(1,-1,-1,-1).
$$
在同一实际六十八维空间，定义 rank-one 交织
$$
Q_{w,v}=\frac{wv^*}{\|v\|^2}\otimes1_{17}.
$$
其真实 Mumford 表达为
$$
Q_{w,v}
=\frac1{4\|v\|^2}\sum_{k,j=0}^3(-1)^{k+j}
 \left(\sum_{a=0}^3w_av_{a-j}i^{-ka}\right)M^kN^j.            \tag{1}
$$
这里使用 R229 已付的两个共同负号；它们对交织的奇次项不可删去。

特别，
$$
\begin{aligned}
Q_{+,0}={}&\frac14\bigl\{
(M^2-1)(N+N^3)-(M+M^3)(1+N^2)\bigr\},\\
Q_{0,+}={}&-\frac18\bigl\{
(1+M^2)(N+N^3)+(M+M^3)(1-N^2)\bigr\}.
\end{aligned}                                             \tag{2}
$$
每式恰有八项。准确有
$$
Q_{0,+}Q_{+,0}=\Pi_0,\qquad
Q_{+,0}Q_{0,+}=\Pi_+,\qquad
Q_{-,0}=M^2Q_{+,0}.                                       \tag{3}
$$
这些算子保留整个十七处向量。
它们的分母只在二处；$\kappa_4$ 在所有奇素位都是单位。

## 2. 原 A、B 给出的两条准确秩零参考

定义
$$
\begin{aligned}
Q_{68}(t)={}&1+20t-176t^3+480t^4-1344t^5
                 +2048t^6-1280t^7+256t^8,\\
Q_{289}(s)={}&1-18s^2+16s^3+s^4,
\end{aligned}                                             \tag{4}
$$
并置
$$
S_{68}=\Theta\rho Q_{68}(t),\qquad
S_{289}=\Theta Q_{289}(16\xi).
$$
两者原点值均为一。

**准确恒等式及其反向回收：**
$$
\boxed{\quad
Q_{+,0}A=u_1S_{68},\qquad Q_{0,+}B=u_2S_{289},
\quad
u_1=-\frac{\kappa_4}{80},\quad
u_2=-\frac{\kappa_4^{-1}}{320}.
\quad}                                                     \tag{5}
$$
$$
\boxed{\quad
A=u_1Q_{0,+}S_{68},\qquad
B=u_2Q_{+,0}S_{289}.
\quad}                                                     \tag{6}
$$
注意 (6) 的系数仍是 $u_1,u_2$：由 (3) 对 (5) 作用，
$Q_{0,+}S_{68}=u_1^{-1}A$、$Q_{+,0}S_{289}=u_2^{-1}B$。

所有常数都已在原固定归一中确定，且
$$
u_1u_2=\frac1{25600}.                                     \tag{7}
$$
所以对目标 $p>19$，(5)、(6) 没有新的非单位边界。

证明用 (1) 对原 A/B 的 degree-17 齐次多项式准确代入。
例如在 $\widetilde F=\kappa_4F,\widetilde G=\kappa_4G$ 坐标中，
$Q_{+,0}A$ 的约化多项式为
$$
\begin{aligned}
\frac15\bigl(&-\widetilde F^{17}
-28\widetilde F^{15}\widetilde G^2
-168\widetilde F^{13}\widetilde G^4
-300\widetilde F^{11}\widetilde G^6\\
&-370\widetilde F^9\widetilde G^8
+428\widetilde F^7\widetilde G^{10}
+416\widetilde F^5\widetilde G^{12}
+28\widetilde F^3\widetilde G^{14}
-5\widetilde F\widetilde G^{16}\bigr).
\end{aligned}
$$
用 $F^2+G^2=T^2$、$\kappa_4^{16}=1/16$ 改回 $t=G^2/T^2$，
恰得第一式。第二式的准确结果是
$$
Q_{0,+}(\kappa_4B)=-\frac1{320}\Theta Q_{289}(16\xi).
$$
反向式又由 (3) 得到；脚本也直接复核了它们。

### 2.1 算术身份与真 Yang 非零

原 A 的有限型是 $v_0\otimes\lambda^{-1}$；
$Q_{+,0}$ 将它准确变成 $v_+\otimes\lambda^{-1}$。
所以 $S_{68}$ 是
$$
y^2=x^3-68x
$$
的实际 $m\equiv0\pmod4$ theta 行。
原 B 的型是 $v_+\otimes\lambda^{-2}$；
$Q_{0,+}$ 将它变成 $v_0\otimes\lambda^{-2}$。
所以 $S_{289}$ 是
$$
y^2=x^3-289x
$$
的实际行，放在同一个双倍 E0 微分尺度上。

这里使用的是 R112、固定四次族笔记和 R229 已核的完整有限向量：
二处 Haar 归一、十七处共同极化、其余有限处和无穷 Hermite 规范均未改变。
交织不是把逐权平方根重新选符号。

由于 (4) 的常数项为一，实际 theta 值非零。
Yang 的同一局部—全局平方公式在 $m=0$ 的比例常数非零，
故这两条曲线的中心复 $L$ 值非零，解析秩确为零。
这一步不从 Mordell--Weil 秩零倒推 $L(E,1)\ne0$。
其归一代数中心值是固定非零代数数，所以在固定有限例外集外为 $p$ 单位。
本文的完整惰性半因子直接满足 $J(S_{68};0)=J(S_{289};0)=1$；
若使用普通单位限制，仍须保留原规范中的 Euler 和周期因子。

## 3. 原 degree-17 空间上的同线丛 norm-five 迹

下面先在未双倍的变量上写公式。
令
$$
s=x(z)^{-2},\qquad
h_P(z)=\vartheta(z)^{17}P(s),\qquad \deg P\le4.
$$
这是旧 dyadic 型的全局 $i$-不变五维空间。
取
$$
\pi=2+i,\qquad \bar\pi=2-i,\qquad \eta=1-2i.
$$
原 sigma division 公式和 theta 规范给
$$
\frac{\sigma(\pi z)}{\sigma(z)^5}=\pi x^2-i,\qquad
\frac{\vartheta(\pi z)}{\vartheta(z)^5}=1-\eta s,
$$
$$
s(\pi z)=\frac{s(\pi-is)^4}{(1-\eta s)^4}.                  \tag{8}
$$
例如由第一式作两次对数微分，得到
$$
x(\pi z)=\frac{x(x^2-\eta)^2}{(\pi x^2-i)^2};
$$
再用 $\vartheta^2=x\sigma^2$ 及原点首项即得 (8)。

$[\pi]^*\vartheta^{17}$ 与 $[\bar\pi]^*\vartheta^{17}$
具有同一个 degree-85 自动因子：
范数都为五，且 $\pi,\bar\pi$ 模二相同。
所以在这个已明确的线丛同构下，可以作真正的有限平坦迹
$$
\mathcal T_\pi=[\pi]_*\,[\bar\pi]^*.
$$
没有把不同线丛的截面直接相加。

写
$$
\Phi(X,t)=X(\pi-iX)^4-t(1-\eta X)^4.
$$
则在五维空间上，$\mathcal T_\pi h_P=h_{\mathscr T P}$，其中
$$
\boxed{\quad
(\mathscr TP)(t)=
\operatorname{Tr}_{\,\Phi(X,t)=0}
 \left[
 \frac{(1-\bar\eta X)^{17}}{(1-\eta X)^{17}}
 P\!\left(\frac{X(\bar\pi+iX)^4}{(1-\bar\eta X)^4}\right)
 \right].
\quad}                                                     \tag{9}
$$
这里的迹是整个 degree-five 纤维的迹，含所有分支与正确 frame。
在 ramified 纤维上也取有限平坦迹，因而保留重数。

从线丛构造看，结果仍是整的 degree-17 截面，且 $i$-不变，
所以 $\mathscr TP$ 的次数至多四。
因此五个准确有理参数值足以确定 (9)；
这不是由五个数值样例推断一个未知函数。

## 4. 五维准确矩阵与全部实际 primitive 线

在 $1,s,s^2,s^3,s^4$ 基中，
$$
\boxed{\quad \mathscr T=\frac{R+iI}{128},\quad}             \tag{10}
$$
其中
$$
R=\begin{pmatrix}
127&1&7&9&-17\\
-1156&-224&-108&-56&108\\
1326&54&70&-66&-1314\\
884&-32&-68&-40&580\\
-221&-23&-29&-7&-61
\end{pmatrix},
\qquad
I=\begin{pmatrix}
1&3&1&-13&-31\\
102&38&-114&-98&-586\\
2448&-228&40&132&768\\
-2958&114&106&90&-670\\
-153&-39&-17&-31&87
\end{pmatrix}.                                             \tag{11}
$$

先用分歧纤维作独立符号校准：
$\Phi(X,0)=X(X-\eta)^4$，根为 $0$ 和重数四的 $\eta$。
(9) 的 frame 因子在 $\eta$ 等于
$$
\left(\frac{-1+i}{2}\right)^{17}=\frac{-1+i}{512},
$$
而 $s(\bar\pi w)=\eta$，所以对每个 $\deg P\le4$，
$$
(\mathscr TP)(0)=P(0)+\frac{-1+i}{128}P(\eta).              \tag{11a}
$$
这给完整首行
$((127+i),(1+3i),(7+i),(9-13i),(-17-31i))/128$，
并固定正迹的整体符号；没有只核矩阵的特征线。

### 4.1 θ 群等变和标量的认定

对 $P\in E_0[17]$ 的同一 Mumford lift，pullback 与 trace 给
$$
\mathcal T_\pi U_P
=U_{(\pi/\bar\pi)P}\mathcal T_\pi.                          \tag{12}
$$
可以在通用覆盖直接核对 (12)：
$[\bar\pi]^*U_P=U_{P/\bar\pi}[\bar\pi]^*$，
而 $[\pi]_*U_Q=U_{\pi Q}[\pi]_*$。
等式中的指数 frame 相同，因为 $N\pi=N\bar\pi$；
两条半特征也相同，因为 $\pi,\bar\pi$ 模二相同。
对奇数 level 17 采用同一对称 θ 结构即可得到 (12) 的准确 lifts。
即使先只作 projective 比较，潜在额外因子也是十七挠群的一个字符；
本构造与 $i$ 交换，该字符必须在 $i$ 下不变，
而 $i-1$ 在十七挠群上可逆，故额外字符为零。
这说明 (9) 的线丛同构保留了所需 θ 群作用。

十七维 Heisenberg 表示不可约，所以 (12) 将 $\mathcal T_\pi$
确定为参考 split torus 算子乘一个共同标量。
在 $i\mapsto4\bmod17$ 的分量中，
$$
a=\pi/\bar\pi=14=3^9\pmod{17}.
$$
参考自然极化作用是 $f(y)\mapsto f(ay)$。
原 primitive 线 $v_k=\lambda^{-k}\mathbf1_{\mathbf F_{17}^\times}$
上的特征值为
$$
\lambda^{-k}(14)=i^k.                                     \tag{13}
$$
准确矩阵 (10) 对已知原
$$
P_1(s)=s+\frac35s^2-\frac15s^3+\frac15s^4
$$
给 $\mathscr TP_1=-(2+i)P_1$。
这既证明 $\mathcal T_\pi\ne0$，也固定共同标量
$-(2+i)/i=-(1-2i)=-\eta$。
没有用任意 Weil 相位替换实际几何归一。

### 4.2 完整特征基与新的 λ³ 认定

置 $\beta=4-i$，并用已证 CM division 多项式
$$
P_\beta(s)=1+(12-20i)s+(-10+28i)s^2
                   +(-20-12i)s^3+(1+4i)s^4,
$$
$$
P_{\bar\beta}=\overline{P_\beta},\qquad
P_2(s)=1-18s^2+16s^3+s^4,\qquad
P_3(s)=1-7s+21s^2-5s^3-2s^4.                              \tag{14}
$$
它们满足

| 实际多项式 | $\mathscr T$ 特征值 | 十七处类型 |
|---|---:|---|
| $P_\beta,P_{\bar\beta}$ | $-\eta=-1+2i$ | 两维 trivial 类型 |
| $P_1$ | $-2-i=-i\eta$ | $\lambda^{-1}$ |
| $P_2$ | $1-2i=\eta$ | $\lambda^{-2}$ |
| $P_3$ | $2+i=i\eta$ | $\lambda^{-3}$ |

前两个对应 $\vartheta(\beta z),\vartheta(\bar\beta z)$，
保持旧有理 CM 缩放笔记中的实际 frame。
后三个特征线各只有一维。
因此 (10)、(12)、(13) **准确认定** $P_3$ 为实际 E4913 的 theta，
按原点值一归一；没有把浮点候选当成证明。

取
$$
P_{\rm re}=(P_\beta+P_{\bar\beta})/2,\qquad
P_{\rm im}=(P_\beta-P_{\bar\beta})/(2i).
$$
五个有理列
$$
P_{\rm re},P_{\rm im},P_1,P_2,P_3
$$
在单项式基中的行列式准确为
$$
\frac{65536}{5}.                                          \tag{15}
$$
所以在所有 $p>19$ 上是同一整五维空间的单位换基。
特别可用
$$
\mathcal E_k=\frac14\sum_{j=0}^3
 i^{-kj}(\mathscr T/(-\eta))^j,\qquad k=0,1,2,3                \tag{16}
$$
作实际积分投影：$\mathcal E_0$ 秩二，其余各秩一。
这里的所有除数在 $p>19$ 上均为单位。
这是原固定有限空间的投影，不是原中央泛函的投影恒等式。

## 5. 第三条相邻 dyadic 参考

令
$$
S_{4913}=\Theta P_3(16\xi),
$$
以及
$$
\begin{aligned}
Q_{19652}(t)={}&1-76t+608t^2-1456t^3+3296t^4\\
&-4928t^5+3584t^6-1280t^7+256t^8,\\
S_{19652}&=\Theta\rho Q_{19652}(t).
\end{aligned}
$$
同一个八项交织准确给
$$
Q_{+,0}S_{4913}=-\kappa_4S_{19652}.                        \tag{17}
$$
所以后者是 $y^2=x^3-19652x$ 的实际 theta 行；
前者是 $y^2=x^3-4913x$ 的双倍尺度行。
它们原点值都是一，同一 Yang 平方公式也直接给解析中心非零。
曲线身份、有限向量与比例常数均独立于目标 $p$。

## 6. 原 C_B^- 的五块系数全部明确

令 $C_B^\pm$ 为 R229 的原实际投影。
由于 $Q_{0,-}$ 杀掉 $v_+$，准确有
$$
\kappa_4Q_{0,-}C_B
=\kappa_4Q_{0,-}C_B^-=\Theta R(16\xi),                     \tag{18}
$$
其中
$$
\begin{aligned}
R(s)={}&\frac{19509103}{28114944000}
+\frac{10318337}{702873600}s
+\frac{777767}{27525120}s^2\\
&+\frac{721667}{86016000}s^3
+\frac{55879}{275251200}s^4.
\end{aligned}                                             \tag{19}
$$
这是对 R227 原 $C_B$ 的准确八项运输；未选取另一份有限代表。

在 (15) 的实际基中，
$$
R=a_0P_{\rm re}+a_1P_{\rm im}
                  +a_{17}P_1+a_{289}P_2+a_{4913}P_3,        \tag{20}
$$
全部系数为

| 系数 | 准确值 |
|---|---:|
| $a_0$ | $-16942549/30277632000$ |
| $a_1$ | $-197627103/524812288000$ |
| $a_{17}$ | $323168419/14994636800$ |
| $a_{289}$ | $244224499/1574436864000$ |
| $a_{4913}$ | $133022909/121110528000$ |

五个系数都非零，分母的素因子都不超过十三。
因此这里确实出现了三个 primitive 块与两个 CM 缩放方向；
不再只有一个抽象的五维池。
各个固定非零系数也只可能在固定有限个素位失去单位性。

令
$$
\gamma_\beta=(a_0-ia_1)/2,\qquad
\gamma_{\bar\beta}=(a_0+ia_1)/2,\qquad
\tau=M^2.
$$
写 degree-4 参考
$$
G(z)=2x(z)\sigma(z)^4=T(z)\phi(z).
$$
则 (18)–(20) 回到原 $v_-$ 坐标后，给出
$$
\boxed{\begin{aligned}
C_B^-={}&-\frac{a_{17}}5\,\tau S_{68}
         -320a_{289}\,\tau B
         -a_{4913}\,\tau S_{19652}\\
&-2\gamma_\beta G(\beta z)
 -2\gamma_{\bar\beta}G(\bar\beta z).
\end{aligned}}                                             \tag{21}
$$
这是真正原截面的完整等式。

证明中的三个 primitive 系数来自
$$
P_1(16\xi)\Theta=16A,\quad
Q_{-,0}=M^2Q_{+,0},
$$
再使用 (5)、(6)、(17)。
CM 两项使用准确的
$$
Q_{+,0}T(\beta z)=2\kappa_4F(\beta z),\qquad
Q_{-,0}T(\beta z)=-2\kappa_4G(\beta z),                      \tag{22}
$$
及其共轭。

为保留 (22) 的规范，可在 R115 的共同高斯变量中直接核对：
$h_0=c_0(4+i)$，所以 $T((4+i)z)$ 在十七处是 $\delta_0$，
二处是 $v_0$。改变二处向量为 $v_+$ 给 $F((4+i)z)$；
它在原点的 raw theta 比值是 $2\kappa_4$。
再用 $-\beta/\bar\beta\in1+8\mathcal O_{K,2}$：
$-1$ 在这里的偶向量上作用为一，而余下元素是原 $g_*$ 的偶次幂，
故它对这两个 dyadic 向量作用相同，另一方向也有同一常数。
最后 $\beta R=\bar\beta R=iR$ 模周期，而 degree-4 的
$N^2F=-G$，给第二式的负号。
所有 norm-17 CM 缩放方向和十七处 trivial 向量均因此逐个保留。

## 7. 原 C_B^- 的完整 Mellin 算术表达

以下固定目标惰性 $p>19$，令 $d=p+1$，
$c$ 为原 degree-68 公共 gauge，$c_4=c/17$ 为 degree-4 参考 gauge。
定义
$$
\begin{aligned}
H_{68}(u)&=J_c(z^{-2}\tau S_{68};u),&
H_{34}(u)&=J_c(z^{-2}\tau B;u),\\
H_{19652}(u)&=J_c(z^{-2}\tau S_{19652};u),&
H_4(u)&=J_{c_4}(z^{-2}G;u).
\end{aligned}
$$
它们都使用同一完整 Newton 插值规则；
除去的 $z^2$ 是真实零，不是改变质量的形式操作。
R227 的半径证明适用，且
$$
H_{68}(0)=H_{19652}(0)=10,\qquad
H_{34}(0)=-1/10,\qquad H_4(0)=2.                            \tag{23}
$$
其中 $Q_{68}(1)=Q_{19652}(1)=5$，而原 $b_0(1/4)=-1/20$。

置
$$
A_p=\frac{\beta^d}{17},\qquad B_p=\frac{\bar\beta^d}{17}
       \quad\in1+p\mathcal O_{K_p}.
$$
相同权重的整数插值与完整解析唯一性给
$$
J_c(z^{-2}G(\beta z);u)=\beta^2 A_p^uH_4(u),                \tag{24}
$$
以及共轭式。$c=17c_4$ 和额外的 $\beta^2$ 都不可省略。

于是 R229/R227 的实际
$\mathcal F_-(u)=J_c(z^{-2}C_B^-;u)$ 准确等于
$$
\boxed{\begin{aligned}
\mathcal F_-={}&-\frac{a_{17}}5H_{68}
                -320a_{289}H_{34}
                -a_{4913}H_{19652}\\
&-2\bigl(\gamma_\beta\beta^2A_p^u
       +\gamma_{\bar\beta}\bar\beta^2B_p^u\bigr)H_4.
\end{aligned}}                                             \tag{25}
$$
这是原 $C_B^-$ 的完整算术比较，未把邻接的 $m\equiv2$ 支改成原 $m\equiv0$ 支。

### 7.1 质量和实际 CM 对数方向

写
$$
L=15a_0-8a_1=-\frac{706011479}{131203072000},\qquad
M=8a_0+15a_1=-\frac{15941320019}{1574436864000}.              \tag{26}
$$
则 (23)–(25) 的常数项准确为
$$
-2a_{17}+32a_{289}-10a_{4913}-4L
       =-\frac{2261}{81920}=-\beta_{\mathrm B}.              \tag{27}
$$
这与 R229 的 $z^{-2}C_B^-(0)$ 一致。
所以原裸单位在算术分解中没有重复计入。

CM 乘子的实际导数是
$$
\left.\frac d{du}\right|_{0}
\bigl(\gamma_\beta\beta^2A_p^u+
      \gamma_{\bar\beta}\bar\beta^2B_p^u\bigr)
=
\frac{p-1}{2}L\log_p17
-\frac{id}{2}M\log_p(\beta/\bar\beta).                      \tag{28}
$$
两项及 $L\,H_4'(0)$ 都必须保留。
特别，(21) 的 CM 部分含有非零系数 $M$ 的范数一对数方向；
但这没有消去其余实际曲线项或连接项。

在同一真实 CM 缩放二维空间中，
$$
D_\beta(z)=\frac{G(\beta z)}{\beta^2}
                 -\frac{G(\bar\beta z)}{\bar\beta^2}
$$
有准确完整式
$$
J_c(z^{-2}D_\beta;u)=(A_p^u-B_p^u)H_4(u),\qquad
J_c'(z^{-2}D_\beta;0)=2d\log_p(\beta/\bar\beta)\ne0.         \tag{29}
$$
非零性因为 $\beta/\bar\beta$ 不是 $\mathbf Q(i)$ 的根单位，
而它在 $K_p$ 是单位，$p$ 进对数在单位上的核为根单位。
(29) 认定了实际五块分解中可见的已知非零参考方向；
不能据此删除 (25) 的其他分量。

## 8. CM 部分的连接补偿也可完全具体化

令
$$
W=z\Theta'/\Theta,\qquad E=z\partial_z,\qquad
\mathcal Q_W=W^2+EW-W.
$$
对 $\beta$ 方向置
$$
W_\beta=z\partial_z\log T(\beta z),\qquad
\Delta_\beta=W-W_\beta=-E\log P_\beta(16\xi).               \tag{30}
$$
这是固定显式有理函数；$P_\beta$ 在 (14) 中已全部给出。
没有把两个 theta frame 当成同一个 frame。

写 $g_\beta=z^{-2}G(\beta z)$、$g_4=z^{-2}G$，
$W_4=zT'/T$。除了 (24)，准确还有
$$
J_c(Wg_\beta;u)=
\beta^2A_p^uJ_{c_4}(W_4g_4;u)
       +J_c(\Delta_\beta g_\beta;u),                       \tag{31}
$$
$$
\begin{aligned}
J_c(\mathcal Q_Wg_\beta;u)
={}&\beta^2A_p^uJ_{c_4}(\mathcal Q_{W_4}g_4;u)\\
&+J_c\bigl(
(2\Delta_\beta W_\beta+\Delta_\beta^2+
                 E\Delta_\beta-\Delta_\beta)g_\beta;u
\bigr).
\end{aligned}                                             \tag{32}
$$
共轭式相同。
原点处 $P_\beta(16\xi)$ 的常数为一；
其固定 prime-to-$p$ torsion 零点不在形式剩余圆盘中。
所以这些额外项在 R227 的同一指定半径上有界。
涉及 raw $W$ 的 Mellin 可用
$W=W_0+dc z^d$ 和 $J(cz^dF;u)=uJ(F;u-1)$
化回 R227 的完整 Tate 函数。

因此 (25) 只将 $\mathcal F_-$ 的来源写成曲线和 CM 缩放；
$\mathcal G_-$、$\mathcal H_-$ 的全部补偿通过线性分配和
(30)–(32) 保留。把 (25) 单独代入后忽略这些项是不成立的。
原 $C_B^+$ 的八次 tame 部分也仍须加入 R229 的完整式。

## 9. 原两行与两秩零参考的完整中央矩阵

对任一固定原截面 $F$，记
$$
J_c(F;u)=\sum_{h\ge0}c^{-h}(u)_h
                  [z^{dh}]e^{-cz^d}F.
$$
在同一实际二处基、同一十七处两条 primitive 线上，完整矩阵是
$$
\mathcal M_p(u)=
\begin{pmatrix}
J_c(A;u)&u_2J_c(S_{289};u)\\
u_1J_c(S_{68};u)&J_c(B;u)
\end{pmatrix}.                                             \tag{33}
$$
它不是将四个无关归一的 Mellin 函数拼在一起；
两个非对角项就是 (5) 对原 A/B 的真实交织。
准确有
$$
\mathcal M_p(0)=
\begin{pmatrix}0&u_2\\u_1&0\end{pmatrix},\qquad
\det\mathcal M_p(0)=-\frac1{25600}.                        \tag{34}
$$
所以这是原点附近真正可逆的解析矩阵，中心行列式是单位。

但主问题的两个导数仍是它的两个对角导数。
令 $\mathcal N_p=\mathcal M_p(0)^{-1}\mathcal M_p$，则
$$
\mathcal N_p(u)=
\begin{pmatrix}
J_c(S_{68};u)&J_c(B;u)/u_1\\
J_c(A;u)/u_2&J_c(S_{289};u)
\end{pmatrix},\qquad \mathcal N_p(0)=1.                    \tag{35}
$$
所需的是 (35) 的某个非对角一阶系数非零。
(34) 本身不提供这一结论。

完整导数关系也保留这种区别：
$$
(\det\mathcal M_p)'(0)
=-u_1u_2\bigl(J_c'(S_{68};0)+J_c'(S_{289};0)\bigr),
$$
而目标乘积首次在二阶出现：
$$
\begin{aligned}
\frac12(\det\mathcal M_p)''(0)
={}&J_c'(A;0)J_c'(B;0)\\
&-u_1u_2\left(
\frac12J_c''(S_{68};0)+\frac12J_c''(S_{289};0)
 +J_c'(S_{68};0)J_c'(S_{289};0)\right).
\end{aligned}                                             \tag{36}
$$
本篇没有给 $\det\mathcal M_p$ 一个额外的固定常数公式。

## 10. 转置作用、质量和首行模 p²

定义完整整行
$$
\ell_h(F)=[z^{dh}]e^{-cz^d}F.
$$
有限交织的正确对偶作用是
$$
\ell_h(QF)=(\ell_h\circ Q)(F),                              \tag{37}
$$
即把原中央行实际运输到另外的 row，而不是令中央泛函与 $Q$ 交换。
在二处坐标 $v_0\otimes w_0+v_+\otimes w_+$ 上，
$Q_{+,0}$ 将 $(w_0,w_+)$ 送到 $(0,w_0)$，
$Q_{0,+}$ 将其送到 $(w_+,0)$；
(37) 的转置明确交换的是相应 row。
它不把原 A/B 的中央零传给所有八项运输。

对可能有质量的截面 $F$，必须用
$$
\begin{aligned}
\ell_0(F)&=F(0),\\
\ell_1(F)&=[z^d]F-cF(0),\\
\ell_2(F)&=[z^{2d}]F-c[z^d]F+\frac{c^2}{2}F(0).
\end{aligned}                                             \tag{38}
$$
各单项 raw 系数可以有 $p^{-1}$、$p^{-2}$；先按 (38) 合并。
R210 的同一原 gauge 第一带整性适用于这些固定 degree-68 截面，
给 $\ell_1,\ell_2$ 整。

将 (6) 写成八项行，得到准确的
$$
\begin{aligned}
R_{1,A}&=u_1\sum_s q^{0,+}_s\ell_1(U_sS_{68}),&
\widehat R_{2,A}&=u_1\sum_s q^{0,+}_s\ell_2(U_sS_{68}),\\
R_{1,B}&=u_2\sum_s q^{+,0}_s\ell_1(U_sS_{289}),&
\widehat R_{2,B}&=u_2\sum_s q^{+,0}_s\ell_2(U_sS_{289}),
\end{aligned}                                             \tag{39}
$$
其中权重就是 (2)。首式保留在模 $p^2$，第二式保留在模 $p$。
相应的质量和准确为零，恢复原 A/B 的正次数条件；
并非逐个被运输项都没有质量。

若原首行可被 $p$ 整除，则下一位必须仍按原聚合写为
$$
K_A=\overline{u_1\sum_s q^{0,+}_s\ell_2(U_sS_{68})}
-\alpha\,\overline{
\frac{u_1\sum_s q^{0,+}_s\ell_1(U_sS_{68})}{p}},
\qquad \alpha=pc\bmod p,                                  \tag{40}
$$
以及 B 的对应式。
不能对尚未证明可整除的各个运输项分别除以 $p$。
(38)–(40) 也保留了 rank-zero 参考质量在 first-row 下一位的全部贡献。

同理，(10) 是同一固定五维 source 的准确矩阵，
对每一个 $\ell_h$ 都给真正转置 row；
(16) 的积分投影可逐行计算，但不从其幂等性推中央零保持。

## 11. 证书、复核与剩余输入

[四挠交织准确脚本](../scripts/check-original-rankzero-intertwiners.js)
及 [输出](../scripts/check-original-rankzero-intertwiners.json)
直接核对 (5)、(6)、(17)–(19)。
[CM norm-five 准确迹脚本](../scripts/check-original-cm5-tame-projectors.js)
及 [输出](../scripts/check-original-cm5-tame-projectors.json)
在 $\mathbf Q(i)[X]/(\Phi)$ 中计算有限平坦迹，
核对 (10)–(16)、(20)、(26)、(27)。
两份脚本本轮均已在 V8 执行 **PASS**。
所有运算均为整数或准确有理数；没有目标素数扫描，也没有把浮点拟合认成恒等式。

(9) 的证书用 $t=0,1,2,3,4$ 的准确值。
分母 $1-\eta X$ 在这些有限代数中都可逆：
$\Phi(1/\eta,t)$ 是与 $t$ 无关的非零常数。
脚本在每个有限代数中另核线性分母与其逆元的乘积为一，
并用 (11a) 独立核整个 $t=0$ 首行；其中 $P=1$ 的正迹为 $(127+i)/128$，固定整个算子的符号。
由第 3 节已证明的次数上界，五点准确插值就是完整矩阵证明。
(15) 的单位行列式另核全部实际类型，没有遗漏 trivial 的第二维。

当前得到的是带单位系数的实际参考及原 $C_B^-$ 的全部算术分量。
要推出原中心导数非同时为零，仍需在 (25)、(30)–(32)、原八次 tame 部分
与 (39) 的实际 row 之间证明足够的封闭关系。
本篇没有将有限交织可逆、秩零质量非零或已知 CM 对数非零替代这一条件。

### 来源

- 原截面、度数、有限向量和全部 sigma 规范：R51、R112、R115、R226。
- 真实四挠 lifts、积分 finite types 与完整原矩：R229。
- 原二阶分解、完整 Mellin 收敛和普通/协变补偿：R227。
- 原 norm-five sigma 恒等式和 norm-seventeen CM theta 多项式：
  [五次 theta 与 Lucas 接口](../notes/2026-11-12-degree-five-theta-lucas-interface.md)、
  [准确 degree17 证书](../notes/2026-11-12-degree17-theta-gaussian-and-denominator-certificate.md)。
- 固定四次族的真实自然极化与角色：
  [primitive 分块](../notes/2026-11-12-seventeen-quartic-family-and-primitive-blocks.md)。
- T. Yang，*Theta liftings and Hecke L-functions*，J. reine angew. Math.
  **485** (1997)，25–53，Corollary 2.10、式 (2.28) 及完整平方公式：
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
  本篇只使用已经核定的实际局部向量，不引入新的逐权平方根规范。
