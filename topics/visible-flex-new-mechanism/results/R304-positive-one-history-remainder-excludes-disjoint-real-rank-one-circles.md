# R304：完整一层的低阶正余量排除不交实 rank-one 微包圆

日期：2026-11-15。**完整纸面原式推导；没有执行求积、符号程序、profile 扫描、人工测试或研究计算。**

本稿从 [R300](R300-one-history-tail-compensation-and-thirty-eight-dimensional-principal-space.md) 尚未支付的 $C^2$ annihilator 中提取一条准确身份。它不是又一个主秩：在三个旧 Gaussian 对称／面积条件以及一个旧完整面积已经为零后，真实 $E_{-3}$ 一层的 $\sigma h^{-2}j^0$ 系数仍严格为正。这个余量排除**所有由有限个支撑不交的实紧 rank-one 微包组成的非退化圆**在本稿小共振偶端芽上通过完整 ruling 偶部门。

结论不要求等平方背景，不要求各微包有相同形状、宽度、四次积分或低阶观察；也不依赖包的排列。旧等背景／同纤维构造只是其特例。已经分别支付的面积、二层、能量、第三 range 及若干新主观察仍是准确成果，但它们不能把下述低阶正余量变成零。

本稿不把结论推广到一般重叠的局部 rank-two profiles，不判断其他几何端芽，也不证明原主课题无解。对合法二阶及第三 gauge 的限定，使用的是原 [R243](R243-finite-jet-criterion-for-the-complete-even-exceptional-ruling.md) 的**同一偶部商**，没有把静态 gauge 一律禁止。

主要来源：[R221 完整局部配对](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R259 原 self 与三外矩](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R267 非紧单包 self](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R282 完整平方 history](R282-symmetric-Gaussian-products-and-an-independent-square-history-gate.md)、[R249 真实词独立](R249-Gaussian-word-independence-and-complete-resonant-fourth-harmonic-obstruction.md)、[R296 完整一层原式](R296-complete-zero-one-Gaussian-layers-and-the-full-principal-square.md)及 R300。

## 1. 真实对象与严格结论

从实际几何的初始安装选择
$$
h=h_eH,\quad H=e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\qquad
\varepsilon=\kappa^2/4,\quad 0<\kappa^2<1/100,\quad h_e>0.
\tag{1}
$$
这是 R241/R293 允许的初始小参数选择；不是在一个已冻结的任意几何上换参数。记
$$
j=2\varepsilon\kappa\sigma^2,\quad e=hx+j,\quad
\mathcal Q=1+e^2,\quad
\gamma=h_\sigma,\quad \delta=j_\sigma=\kappa^3\sigma.
$$
共同 profile 区间及右锚保持不变：
$$
I=[\ell,r_*],\qquad Jq(x)=\int_x^{r_*}q(t)\,dt.
$$

令 $u_i$ 为有限个非零实光滑紧 profiles，其闭支撑两两不交，全部位于共同零 collar 内。允许任意有限正间隙、任意实际宽度、中心与形状。取任意实数 $a_i,b_i$，
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad g\ne0.
\tag{2}
$$
零 profile 可以删除。所有原真实三矩圆条件及所需低阶 range 均按原问题施加。写
$$
\phi_\theta=\sum_i c_i(\theta)u_i,\quad
c_i=a_i\cos\theta+b_i\sin\theta,\quad
d_i=a_i^2-c_i^2,\quad D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
$$
$\odot$ 是原二次算子槽，不能把 $D_\theta$ 当作一个先求普通乘积再微分的函数。置
$$
C_i=\int_I(u_i'')^4>0,\qquad
\lambda_i(\theta)=-a_i^2d_i(\theta).
\tag{3}
$$
$C_i>0$ 来自实性及双零 collar：若 $u_i''\equiv0$，紧支撑迫 $u_i=0$。

沿原规范设
$$
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},\quad
L=\Phi_{p_0},\quad U=\Phi_{s_1},
$$
$$
W=aR+bS,\qquad Z=dL+e_-U,\qquad B_{-3}=c_P P.
$$
共振系数为
$$
\begin{aligned}
a&=-\frac{51t^2+2t+8}{64h_e^2},&
b&=-\frac{17t^2+4t}{32h_e^2},\\
d&=\frac{6\kappa^3}{h_e},&
e_-&=-\frac{\kappa(15t+1)}{4h_e},&
c_P&=-\frac{\kappa(41t^2+27)}{216h_e^3},\qquad t=\kappa^2.
\end{aligned}
\tag{4}
$$
其中 $a,d,c_P,d+7e_-$ 都非零；本稿不令 $\kappa=0$。

**定理。** 假设这个真实圆已经支付全部 Gaussian 二层条件，特别包括第2节明确的完整 $A_{-1,-3}$ 面积和第3节的三个 directed 行。则原完整一层满足
$$
\boxed{
[\sigma h^{-2}j^0]\,
\mathscr R_{-3,\pi/2}
=
\frac{(41t^2+27)
(16+184t-1713t^2-2475t^3-4590t^4)}
{15552h_e^3(51t^2+2t+8)}
\int_I(g'')^4
>0.
}
\tag{5}
$$

方括号是 R300 的真实有限 Laurent–多项式呈示中**指定独立函数系数**，不是在 $\sigma=0$ 取值，也不是只取某个未分离的 Taylor jet。于是 $\mathscr R_{-3,\pi/2}$ 不是零函数。R249/R296 的完整词独立性使它不能由零层或其他 Gaussian 层抵消；故本族不能通过原偶部 $\mathcal W_e$ 商门。

下面完整证明(5)，并明确何处使用全角条件。

## 2. 一个旧完整面积已经给真实正平方量

R267 的非合法单包原 self 表保留真正左尾，给
$$
2I_0\{u,[P,L](u;u^2)\}=\frac16 C(u),\qquad
2I_0\{u,[P,U](u;u^2)\}=\frac76 C(u).
\tag{6}
$$
$P$ 的左尾是常数；$L,U$ 的左尾分别是二次或一次多项式。R259 的完整跨包核对 $(Z,P)$ 准确为零。因此
$$
\boxed{
2I_0\{\phi_\theta,[Z,P](\phi_\theta;D_\theta)\}
=-\frac{d+7e_-}{6}
\sum_i c_i(\theta)^2d_i(\theta)C_i .
}
\tag{7}
$$
没有假定单包三矩为零，也没有忽略相邻包的左尾。

原 Gaussian 面积是 $(B_{-1},B_{-3})=(Z,c_PP)$。由
$$
d+7e_-=-\frac{\kappa(81t+7)}{4h_e}\ne0,\qquad c_P\ne0,
$$
这个完整面积的 $I_0$ 门准确迫
$$
\boxed{\mathcal A_\theta:=
\sum_i c_i(\theta)^2d_i(\theta)C_i=0
\quad\text{对所有 }\theta.}
\tag{8}
$$
这是旧面积的必要条件，不是本稿新增的母形假设。

定义三个实际四次和
$$
A_4=\sum_i a_i^4C_i,\qquad
C_{22}=\sum_i a_i^2b_i^2C_i,\qquad
E_4=\sum_i b_i^4C_i=\int_I(g'')^4 .
$$
在 $\theta=\pi/2$，(8)给 $C_{22}=E_4$。再取(8)的整角平均；其平均值是
$(A_4-2C_{22}-3E_4)/8$，所以
$$
\boxed{A_4=5C_{22},\qquad E_4=C_{22}.}
\tag{9}
$$
因此
$$
\boxed{
\sum_i(a_i^2-b_i^2)^2C_i=4E_4>0.
}
\tag{10}
$$
严格性只需 $g\ne0$。允许某些 $a_i$ 或 $b_i$ 为零，不要求每一条斜率有限或非零。

这里**确实用了全角面积**。若只有 $\theta=\pi/2$ 的一个面积门，只能得到 $C_{22}=E_4$，不能凭它推出(9)第一式或(10)的严格下界。

对任意角，(8)还给
$$
\boxed{
\sum_i\lambda_iC_i
=-\sum_i d_i^2C_i-\mathcal A_\theta
=-\sum_i d_i^2C_i.
}
\tag{11}
$$

## 3. 三条旧 directed 行与真实 whole-to-micro 归约

沿 R300 记
$$
\mathscr H^{Y\to X}_{j_0,\theta}
=-I_{j_0}(YD_\theta,XD_\theta)
+2I_{j_0}\{\phi_\theta,Y(\phi_\theta,XD_\theta)\}.
\tag{12}
$$
全部二层为零包含
$$
\mathscr P_\theta:=\mathscr H^{P\to P}_{2,\theta}=0,\quad
\mathscr W_\theta:=\mathscr H^{W\to P}_{1,\theta}=0,\quad
\mathscr Z_\theta:=\mathscr H^{Z\to P}_{0,\theta}=0.
\tag{13}
$$
解释如下：重复 $P,P$ 的对称平方直接给第一条；对 $P,W$ 及 $P,Z$，完整对称乘积给两个 directed 行的和，完整面积给它们的差。因此不能只由对称乘积擅自删除其中一个 directed 行。实际 Gaussian 系数的非零因子可除掉。

以下所用的六个原接口，其有序跨包核在指定外矩上都准确为零。单包表中的 $k$ 是
$$
k^{Y\to X}_{j_0}(u)=
I_{j_0}(Yu^2,Xu^2)+2I_{j_0}\{u,Y(u,Xu^2)\}.
$$

| 原接口 | 有序核 | 准确单包 $k$ |
|---|---:|---:|
| $L\to P,\ I_0$ | $0$ | $-C/6$ |
| $U\to P,\ I_0$ | $0$ | $-7C/6$ |
| $R\to P,\ I_1$ | $0$ | $C/6$ |
| $S\to P,\ I_1$ | $0$ | $C/2$ |
| $P\to P,\ I_2$ | $0$ | $4C/3$ |
| local $P$ 的 $\sigma h^{-2}j^0$ 行 | $0$ | $\kappa^3C/16$ |

前五行可直接代 R300(22) 的 $\beta$ 与 sl2 真尾表。特别，$P(u,p)$ 对常数／一次尾为零；$L(u,p_{\rm const})$ 只给 $u'$，其 $I_0$ 自配对为零。所有有关 $\beta$ 项在这些指定外矩上也为零。最后一行的 local 核是
$-2\eta_-(\mathbf m)n_0$；代原 $\eta_-$ 后只有 $h^{-1},h^0,h^1$，没有 $h^{-2}$ 项。

表中的 self 不靠主符号猜测。例如
$$
F_{L,0}(u)=-\frac12\int u'(u'')^2,\qquad
F_{U,0}(u)=\int\{u'(u'')^2-x(u'')^3\}.
$$
沿真实 $P(u,u)=J((u'')^2)$ 的密度变化分别为 $-C/6,-7C/6$。其他三行同样由 R259 原 cubic 密度或其真实二导得到；$I_2$ 的一阶项没有省略。最后一行在第5节从 R221 原式另给直接证明。

故对这些接口，完整 whole 值恰为
$$
\mathscr H^{Y\to X}_{j_0,\theta}
=\sum_i\lambda_i I_{j_0}(Yu_i^2,Xu_i^2)
+\text{表中常数}\cdot\mathcal A_\theta .
\tag{14}
$$
这里 $\lambda_i=-a_i^2d_i$，来自
$-d_i^2 B+c_i^2d_i C
=\lambda_i B+c_i^2d_i(B+C)$。
用(8)，所有 self 补偿准确消去，**不需要等背景、同形或同 $C_i$**。

因此(13)等价于本稿所需的三个有符号能量和为零：
$$
\sum_i\lambda_i E_{PP,i}=0,\quad
\sum_i\lambda_i E_{PW,i}=0,\quad
\sum_i\lambda_i E_{PZ,i}=0,
\tag{15}
$$
其中
$$
E_{PP}=I_2(Pu^2,Pu^2),\quad
E_{PW}=I_1(Pu^2,Wu^2),\quad
E_{PZ}=I_0(Pu^2,Zu^2).
$$
这些是**有符号 whole 聚合**。下文不会把某个有符号和的负值误解为单包正能量为负。

## 4. 权二所需的全部原能量

对单个实紧 $u$，记
$$
v=u',\quad r=u'',\quad t_1=u''',\qquad C=\int r^4,
$$
$$
H_a=\int x^2r^2t_1^2,\quad
H_b=\int xvr\,t_1^2,\quad
H_d=\int ur\,t_1^2.
$$
原二导是
$$
\begin{aligned}
(Pu^2)''&=-2rt_1,\\
(Ru^2)''&=2(v-xr)t_1,\\
(Su^2)''&=-r^2-2xrt_1,\\
(Lu^2)''&=(u-xv)t_1-\tfrac12(xr^2+Pu^2),\\
(Uu^2)''&=(2xv-3x^2r)t_1+2vr-2xr^2 .
\end{aligned}
\tag{16}
$$
$Pu^2$ 的非零左常尾在第四行保留。真实 IBP 给
$$
\int xr^3t_1=-C/4,\qquad
\int vr^2t_1=-C/3,\qquad
\int (Pu^2)rt_1=C/2.
\tag{17}
$$
因而准确有
$$
\begin{aligned}
I_0(Pu^2,Lu^2)&=-2H_d+2H_b+C/4,\\
I_0(Pu^2,Uu^2)&=6H_a-4H_b+C/3,\\
I_1(Pu^2,Ru^2)&=4H_a-4H_b,\\
I_1(Pu^2,Su^2)&=4H_a-C/2,\\
E_{PP}&=4H_a+2C.
\end{aligned}
\tag{18}
$$
这些是完整等式，尤其最后一式的 $2C$ 来自原 $I_2$ 的 $2(P')^2$。

令
$$
r_b=b/a,\qquad \eta=e_-/d.
$$
由(18)直接整理，
$$
\begin{aligned}
E_{PW}&=4(a+b)H_a-4aH_b-bC/2,\\
E_{PZ}&=d\,I_0(Pu^2,Lu^2)+e_-\,I_0(Pu^2,Uu^2),\\
I_0(Pu^2,Uu^2)
&=\frac1aE_{PW}
+\left(\frac12-r_b\right)E_{PP}
+\left(\frac52r_b-\frac23\right)C .
\end{aligned}
\tag{19}
$$
后面只用这些原能量，不把 $\int r^4$ 设成一个自由控制。

## 5. 从完整 local 配对提取指定一层行

R221(17)在 $j^0h^2$ 分子层，仅 $\delta$ 的两项有贡献。对合法 whole first 槽 $c$，准确为
$$
\boxed{
[\sigma h^{-2}j^0]\,\mathcal T(c;a,b)
=-\frac{\kappa^3}{16}
\int a''b''(x^2c'''+xc'').
}
\tag{20}
$$
对单包 $c=Pu^2$，此式指 R300 明确定义的 formal 局部表达 $\widetilde{\mathcal T}$。它不是将非紧单包偷偷当作合法 whole；第3节已经按原 Green 和有序核完整收集区别。

特别，
$$
\int\{x^2r^2(Pu^2)'''+xr^2(Pu^2)''\}
=4H_a-C/2,
$$
故 local bilinear self 的指定行是
$$
\boxed{
[\sigma h^{-2}j^0](-2\widetilde{\mathcal T}(Pu^2;u,u))
=\frac{\kappa^3}{2}H_a-\frac{\kappa^3}{16}C.
}
\tag{21}
$$
同时 $\mathcal T(u;u,u)$ 的该 cubic 系数是
$-\kappa^3\int xr^3/48$。沿 $Pu^2$ 作原密度变化并乘 $-2$，正好给第3节的 $\kappa^3C/16$。这单独核清了 local self 补偿。

原 elementary history 写成 R300 的 $\mathsf Q_\sigma$，不要与 $\mathcal Q=1+e^2$ 混淆。其有关常数项为
$$
\begin{aligned}
[\sigma h^{-1}j^0]\mathsf Q&=\ell_0L+m_0U,\\
[\sigma h^{-3}j^0]\mathsf Q&=p_0P,\\
\ell_0&=-\kappa/2-6\kappa^3,\qquad
m_0=\kappa(15t+1)/4,\qquad
p_0=41\kappa^5/216 .
\end{aligned}
\tag{22}
$$
它们是原 $M_{\rm raw}$ 积分后的 elementary 部分；不能用 R300 的 $\alpha_{\mathsf Q}+2\beta$ 表替代 $\mathsf Q$ 本身。例如该表的 $h^{-3}j^0$ 还含 $\kappa^3/8$，恰是 $2\beta$，不是(22)的 $p_0$。

以 $\mathscr R^P_\theta=\mathscr R_{-3,\theta}/c_P$ 记去掉非零 Gaussian 常数的原一层，并令
$$
\mathscr O_\theta=[\sigma h^{-2}j^0]\mathscr R^P_\theta .
$$
R296/R300 的完整原式给该行的 history 部分
$$
\frac{\ell_0}{2}\mathscr H^{L\to P}_{0,\theta}
+\frac{m_0}{2}\mathscr H^{U\to P}_{0,\theta}
+\frac{p_0}{2}\mathscr H^{P\to P}_{2,\theta}.
\tag{23}
$$
$R,S$ 的 $I_1$ 部分另带显式 $j$，所以本行不含它们，但消元时要使用旧 $E_{PW}$。结合(8)、(14)、(21)，得到完整有符号和：
$$
\boxed{
\mathscr O_\theta=
\sum_i\lambda_i\left[
\frac{\ell_0}{2}I_0(Pu_i^2,Lu_i^2)
+\frac{m_0}{2}I_0(Pu_i^2,Uu_i^2)
+\frac{p_0}{2}E_{PP,i}
+\frac{\kappa^3}{2}H_{a,i}
-\frac{\kappa^3}{16}C_i
\right].
}
\tag{24}
$$
这是在原面积(8)上成立的**完整行身份**，不是模 $C^2$ 的式子。

## 6. 准确 annihilator 与非零低阶基线

定义
$$
u_0=m_0-\eta\ell_0
=-\frac{1+15t}{48\kappa}.
\tag{25}
$$
用(19)及 $H_a=(E_{PP}-2C)/4$，把(24)整理为
$$
\boxed{
\begin{aligned}
\mathscr O_\theta={}&
\frac{\ell_0}{2d}\,\mathscr Z_\theta
+\frac{u_0}{2a}\,\mathscr W_\theta\\
&+\left\{
\frac{u_0}{2}\left(\frac12-r_b\right)
+\frac{p_0}{2}+\frac{\kappa^3}{8}
\right\}\mathscr P_\theta
+D_\kappa\sum_i\lambda_iC_i ,
\end{aligned}}
\tag{26}
$$
在(8)上准确成立，其中
$$
\begin{aligned}
D_\kappa
&=\frac{u_0}{2}\left(\frac52r_b-\frac23\right)
-\frac{5\kappa^3}{16}\\
&=\boxed{\frac{16+184t-1713t^2-2475t^3-4590t^4}
{288\kappa(51t^2+2t+8)}} .
\end{aligned}
\tag{27}
$$
(26)明确给出了该一层行对三个旧行的完整 annihilator。其 principal 为零，但剩下的 $C^2$ 基线不是零。

在 $0<t<1/100$，(27)分子严格大于
$$
16-\frac{1713}{10^4}
-\frac{2475}{10^6}
-\frac{4590}{10^8}>15.
$$
故 $D_\kappa\ne0$，且其符号与 $\kappa$ 相同。没有把 $\kappa$ 事后调到根，也没有在 $\kappa=0$ 处除零。

用三个旧行(13)和面积(11)，
$$
\boxed{\mathscr O_\theta=-D_\kappa\sum_i d_i(\theta)^2C_i.}
\tag{28}
$$
再用全角面积推出的(10)，
$$
[\sigma h^{-2}j^0]\mathscr R_{-3,\pi/2}
=-4c_PD_\kappa E_4 .
$$
代(4)、(27)即为(5)。$c_P$ 与 $\kappa$ 反号，所以最终实际系数对正、负非零 $\kappa$ 都严格为正。定理证毕。

## 7. 原函数、gauge、已付结果与真正的适用边界

首先，(5)不是一个近似或只有低 $\sigma$ 阶的检验。R300 的原一层呈示是有限和
$$
\sigma\sum_{n=-4}^{2}h^nP_n(j),
$$
其中各 $\sigma h^n j^m$ 作为真实解析函数独立。R249 的 Gaussian 词独立性进一步将四个一层同零层、对称及反对称二层分开。因此指定系数非零就使整个原一层非零，不可能靠另一个未取出的幂层抵消。

其次，R243(2)已经证明实际全路径传入的二、三阶历史，连同任意合法二阶 gauge 的偶部响应，在本端芽上只改变同一个
$$
\mathcal W_e=\operatorname{span}\{h,\sigma^2,(1+j^2)/h\}.
$$
本稿未重置真实入值，也没有忽略原 gauge。由 R296 的同商分解，(5)是这个既定偶端芽上的真实必要障碍。它仍不授权把其他端芽或其他第一阶参数轨道替换进来后保留同一结论。

第三，所有相邻 tails 和 collars 都保在第2–5节的原接口里。只有指定外矩的真实核算出零，才逐包相加；没有由“微包支撑不交”直接断言所有 Volterra history 局域。正是这个权二组合的核为零，才使最终余量成为正的局部四次和。

最后，本稿没有撤销 R280/R293/R294/R299/R300 中各自已付的有限条件或 principal 空间。它说明当前全部这些必要条件之外，还有一个不能在该 rank-one 类内支付的完整低阶兼容。继续同一族增加高频、改变包序、改变斜率、混合正幅 block、改变每包低阶观察目标或增加 principal 维数，都不能消掉(28)：一旦旧完整面积和三个旧行仍保，余量已由 $\sum d_i^2C_i$ 固定。

## 8. 下一机制必须改变什么

本稿严格排除的是(2)的结构：在每个活动微区间，$f$ 与 $g$ 是同一个实 profile 的常数倍。它没有证明一般真实重叠 profiles 的同一 annihilator 仍是(28)。若选择一个活动区间上局部 rank-two 的 $(f,g)$，完整原式会出现 $f'',g''$ 及它们三阶导的交叉项；必须重新推其真正 mixed 余式，不能凭参数增加宣称该方向已可行。

另一类未被本文判断的改变是从最初采用不同的合法几何端芽或非圆第一阶轨道；这会改变原安装、完整 range 和函数独立性的具体接口，需要另行支付。当前小共振端芽下不能靠改一次数值预算、换母包宽度或不改变(2)的第三斜率修复此障碍。

因此本稿给出的下一具体任务是：对一般局部 rank-two 圆，从(20)、(23)的完整 mixed 槽重新计算同一个低阶 annihilator，判定它是另一条正障碍，还是出现可真正控制的新低阶项。该任务与本稿已证 rank-one 结论分开，不预授建设性结果。
