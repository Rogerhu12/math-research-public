# R445：已付有理顶层杀两个最高规范方向与剩余 d 通道的完整原式

日期：2026-11-16。**只读原式并作完整纸面分部积分；没有执行新的研究、符号、profile、积分、秩或开发计算。**

沿 [R444](R444-original-hook-response-action-and-the-highest-second-period-blind-row.md) 固定当前真实圆，记
$$
d_f(X)=I_2\{Y(f,f),X(f^2-g^2)\},\qquad Y=\Phi_{p_2}.
$$
本稿证明当前已付的两个完整端口系数准确给
$$
\boxed{d_f(B_\varepsilon)=d_f(Y)=0.}
\tag{1}
$$
第一式来自最高单反正切门；第二式来自整个有理余式的最高 $h^4$ 系数。都不是只比较 principal，也不使用十二副本的奇次差分。

另外，给出 $d_f(P)$ 的完整逐微包局部公式，保所有原二次尾。十二副本对此量使用正四次幅权；它没有 R444 第二通道的交替差分消去。这仍不判定当前冻结圆的 $d_f(P)$ 非零，也不从新的形式主项宣布一个真实正锥或 actual 截面。

## 1. 同一真实端口及记号

全部参数、原右锚、profiles、宽度、顺序和实际副本均与 R431/R444 相同。原二次高度端口是
$$
h=H(1+\varepsilon\sigma^2),\quad
H>0,\quad \varepsilon>0,\quad k=\kappa\ne0,\quad \omega=0,
$$
$$
K=1+\kappa^2,\quad
Q_{\rm g}=K-2\kappa hx+h^2x^2,\quad
\gamma=2H\varepsilon\sigma,\quad
\sigma^2=\frac{h-H}{H\varepsilon}.
\tag{2}
$$
$h$ 在原实际开段非常数；下面都是原有限 Laurent 系数，不取物理 $h\to\infty$。

采用原 E8 名称
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\
V=\Phi_{p_1},\ T=\Phi_{t_1},\ Y=\Phi_{p_2}.
$$
R318/R321 中的 $V=\Phi_{p_2}$ 在本文统一写作 $Y$；本文 $V$ 仅指 $\Phi_{p_1}$。

沿 [R321(1)](R321-complete-single-arctangent-gates-and-ten-dimensional-joint-control.md)，
$$
B_\varepsilon=aR-2eL+eU+\beta T,\quad
a=\frac{K(\varepsilon-2K)}{32H^2},\quad
e=\frac{\kappa K}{4H},\quad
\beta=-\frac{\varepsilon}{4}\ne0.
\tag{3}
$$
令
$$
\phi_\theta=f\cos\theta+g\sin\theta,\quad
D_\theta=f^2-\phi_\theta^2,\quad
\Delta=f^2-g^2.
$$
实际三矩给所有 $XD_\theta$、$X\Delta$、$X(f,g)$ 真紧。$Y(f,f)$ 自身的左二次尾仍保留。

当前十九个完整值为
$$
q_0,q_1,q_2,\quad\rho_{-4},\ldots,\rho_2,\quad
Z_{-7},\ldots,Z_{-2},Z_2,Z_3,Z_4 .
\tag{4}
$$
它们在 R324 后续 R403/R412/R431 的同一点实际构造中均为零。这里不重新求它们的秩或根。

## 2. 最高单 E 行准确给 d(Bε)=0

[R318 §6(22)—(26)](R318-complete-local-log-residue-and-a-first-single-arctangent-gate.md) 的完整原式给
$$
\rho_2(\theta)
=-\frac{\kappa}{24}H_{Y,2}(\theta),
$$
$$
H_{Y,2}(\theta)
=-I_2(YD_\theta,B_\varepsilon D_\theta)
+2I_2\{\phi_\theta,Y(\phi_\theta,B_\varepsilon D_\theta)\}.
\tag{5}
$$
原 cubic 身份
$$
I_2(u,Y(u,u))\equiv0
$$
在真紧方向 $w$ 的变分为
$$
2I_2\{u,Y(u,w)\}=-I_2\{w,Y(u,u)\}.
\tag{6}
$$
对(5)使用 $w=B_\varepsilon D_\theta$，准确得到
$$
H_{Y,2}(\theta)
=-I_2\{Y(f,f),B_\varepsilon D_\theta\}.
$$
故
$$
\boxed{
\rho_2(\theta)
=\frac{\kappa}{24}I_2\{Y(f,f),B_\varepsilon D_\theta\}.
}
\tag{7}
$$
这包含原 local、chain 和所有非紧 self 边界；(6)只对已经由三矩证明真紧的方向使用，没有将 $Y(f,f)$ 也置成紧函数。

取 $\theta=\pi/2$，由 $\rho_2=0$ 及 $\kappa\ne0$ 即得
$$
\boxed{d_f(B_\varepsilon)=0.}
\tag{8}
$$

## 3. 完整有理 h4 系数准确给 d(Y)=0

### 3.1 只有两项可能贡献最高幂

沿 [R312(23)](R312-quadratic-height-ports-and-rational-arctangent-logarithmic-ruling.md)，整个纯有理项是
$$
\mathscr R_{\rm rat}
=-\mathfrak b(Z_0,Z_0)
+4\mathfrak b(Y_\phi,C_0)
-4\mathcal E_h(\phi,U_{\rm rat}).
\tag{9}
$$
其中
$$
Z_0=K(D)-Y_{\mathsf QD},\qquad
\mathsf Q=\sigma\mathsf A(h),\qquad
\mathsf A(h)=\sum_{p=-3}^1h^pA_p,\qquad
A_1=-\frac{\kappa}{6}Y.
\tag{10}
$$
这里 $Y_\phi$ 是原一阶场，$Y=\Phi_{p_2}$ 是二次算子；两种记号按原来源分开。

[R324 §2—3](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md) 从完整 R56 恢复证明：

- $4\mathfrak b(Y_\phi,C_0)$ 的最高幂不超过 $h^2$；
- $\mathscr C_\sigma/\gamma$ 的最高幂不超过 $h^0$；
- $E'[\mathsf Q,B_\varepsilon]/\gamma$ 的最高幂不超过 $h^0$；
- $U_{\rm rat}$ 的最高幂至多 $h^3$，且其积分初值只经 $1,h,h^{-1}$ 能量权进入；
- $-\mathfrak b(Z_0,Z_0)$ 的 $h^4$ 项只来自 $-\mathcal E_h(\mathsf QD,\mathsf QD)$ 中两个最高 history。

这些界包括原 $P_\sigma$、chain、非紧 self 和全部中心常数，不是只对三阶平方作的界。因此其余真实 $C^2$ 项也不能漏入 $h^4$。

原能量为
$$
\mathcal E_h(a,b)
=\frac K{4h}I_0(a,b)-\frac\kappa2I_1(a,b)+\frac h4I_2(a,b).
\tag{11}
$$
由(2)、(10)，第一个最高贡献为
$$
[h^4]\{-\mathfrak b(Z_0,Z_0)\}
=-\frac1{4H\varepsilon}I_2(A_1D,A_1D).
\tag{12}
$$

### 3.2 第三原函数的完整最高项

原第三式为
$$
U'=\mathscr C_\sigma(\phi;D)
-\mathsf Q'(\phi,\mathsf QD)
+E'[\mathsf Q,B_\varepsilon](\phi;D),\qquad U(0)=0.
$$
因为 $\partial_\sigma h=\gamma$，
$$
\mathsf Q'=\mathsf A+2(h-H)\mathsf A_h,\qquad
\frac{\mathsf Q'(\phi,\mathsf QD)}{\gamma}
=\frac{(\mathsf A+2(h-H)\mathsf A_h)(\phi,\mathsf AD)}
{2H\varepsilon}.
\tag{13}
$$
最高 $h^2$ 系数只有
$$
[h^2](U'/\gamma)
=-\frac3{2H\varepsilon}A_1(\phi,A_1D).
$$
按原锚积分到 h 后，
$$
[h^3]U_{\rm rat}
=-\frac1{2H\varepsilon}A_1(\phi,A_1D).
\tag{14}
$$
在 $h=H$ 减去的真实中心常数仍保留，但由(11)它不能贡献 $h^4$。

所以第二个最高贡献是
$$
[h^4]\{-4\mathcal E_h(\phi,U_{\rm rat})\}
=\frac1{2H\varepsilon}I_2\{\phi,A_1(\phi,A_1D)\}.
\tag{15}
$$

### 3.3 完整 h4 门

把(12)、(15)合起来，得到完整而非仅 principal 的式子
$$
Z_4(\theta)=\frac1{4H\varepsilon}
\{-I_2(A_1D_\theta,A_1D_\theta)
+2I_2(\phi_\theta,A_1(\phi_\theta,A_1D_\theta))\}.
$$
代入 $A_1=-\kappa Y/6$，再用(6)及真紧 $YD_\theta$，
$$
\boxed{
Z_4(\theta)
=-\frac{\kappa^2}{144H\varepsilon}
I_2\{Y(f,f),YD_\theta\}.
}
\tag{16}
$$
因此已付 $Z_4(\pi/2)=0$ 且显示因子非零，给
$$
\boxed{d_f(Y)=0.}
\tag{17}
$$
该证明只消费已付完整系数，没有把 R324 的十九维 principal 证明延伸成额外的隐含等式。

## 4. 原八支路只剩六个未判真值

(3)、(8)、(17)给
$$
\boxed{
d_f(T)
=-\frac a\beta d_f(R)
+\frac{2e}{\beta}d_f(L)
-\frac e\beta d_f(U),\qquad d_f(Y)=0.
}
\tag{18}
$$
所以 R444 的第一通道 $d_f(E_8)$ 由以下六个真实数决定：
$$
d_f(P),\quad d_f(R),\quad d_f(S),\quad
d_f(L),\quad d_f(U),\quad d_f(V).
\tag{19}
$$
这里的“六个”是一个完整生成清单，不是它们的秩，更不是六个可自由指定的 profile 参数。

R444 的准确 signed 最高行条件仍为
$$
b_e=0,\qquad \tau b_d\in d_f(E_8).
\tag{20}
$$
本稿将(20)的未知第一通道缩成(19)，没有证明其中某个数非零。

## 5. 十二副本在 d 通道使用正权，不能移用 e 的差分

R444 证明了：每个完整 base 的 $X\Delta$ 真紧，另一完整 base 的 $Y(F,F)$ 为真实二次左尾；完整 $I_2$ 对这对输入为零。因此 $d_f(X)$ 也在整个合法 base 之间准确相加。

但 $D=f^2-g^2$ 对 $g\mapsto-g$ 为偶。R259 的十二副本
$$
(\gamma_jT_{t_j}F,\ \epsilon_j\gamma_jT_{t_j}G),\quad
\gamma_j^4=\binom{11}{j},\quad
\epsilon_j=(-1)^j,\quad
t_j=t_0+j\Delta_c
$$
对此配对给
$$
d_f(X)=\sum_{j=0}^{11}\binom{11}{j}
\,\mathscr D_X(t_0+j\Delta_c),
\quad
\mathscr D_X(t)=I_2\{Y(T_tF,T_tF),X(T_t\Delta)\}.
\tag{21}
$$
所有项都用固定正宽度、整个 base 和原锚。与 R444 相同的原 E8 次数计算给 $\deg\mathscr D_X\le10$。

在 $\operatorname{Pol}_{\le10}$ 上，(21)定义的正权平移平均保持最高次数，最高项乘
$$
\sum_{j=0}^{11}\binom{11}{j}=2^{11}.
$$
所以它是三角可逆算子。它不是第十一差分，不能使一个非零多项式在所有共同位置上恒零。

这个事实也不证明某个已经冻结的位置的(21)非零：实际多项式可以在该点恰好为零。不能移动已经完成十九门的最终圆来躲开这个可能的零点；任何这样的新选择仍须与原十九门共同支付。

## 6. d(P) 的全部跨微包项为零

这一节只用真紧的单个微包，不要求其自身三矩为零。

记
$$
P(u,u)=J(r^2),\qquad
Y(u,u)=-xu^2+x^2up-\frac{x^3p^2}{2}
-\frac{x^2}{4}J(x^2r^2+2p^2),
$$
$$
p=u',\quad r=u'',\quad t=u''',\qquad
Jq(x)=\int_x^{r_*}q(y)\,dy .
\tag{22}
$$
单包 $P$ 在左侧是真常数，$Y$ 在左侧是
$-\mu_2x^2/4$，没有线性项。

对右侧单包的 $P_u$，其一、二导都真紧。任意纯二次函数 $Ax^2$ 满足
$$
I_2(Ax^2,P_u)
=2A\int x^2P_u''+4A\int xP_u'=0,
\tag{23}
$$
只用 $\int x^2P_u''=-2\int xP_u'$。另一方向的常数尾导数为零；右零尾也保留。因此对两个严格不交微包，
$$
I_2(Y(u_i,u_i),P(u_j,u_j))=0\qquad(i\ne j).
\tag{24}
$$
这里不先把 $P_u$ 的左常数设零。

在当前逐包比例圆
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2
$$
中，原二次算子的交叉输入因支撑不交为零。由(24)，
$$
\boxed{
d_f(P)=\sum_i a_i^2R_i\,I_2\{Y(u_i,u_i),P(u_i,u_i)\}.
}
\tag{25}
$$
所有八/十二 copy、最后块、宽度和幅度都在这同一个真实微包列表中，没有略掉副本权。

## 7. 一个完整单包 self 公式

令
$$
C=u-xp+\frac{x^2r}{2},\qquad W=x^2C^2.
$$
原 $Y$ 式给
$$
x^2Y'''+2xY''-2Y'=W'',\qquad C'=x^2t/2.
\tag{26}
$$
由 $P'=-r^2$ 真紧，第一次分部的边项为零；$W$ 与其端 jets 真紧又支付后两次。因此即使 $P$ 有左常数，
$$
I_2(Y,P)=-\int W P'''
=2\int W(t^2+rt').
\tag{27}
$$
一次完整分部积分后，
$$
I_2(Y,P)
=-2\int x^4Cr\,t^2
+2\int C^2r^2+2\int x^3Cr^2t.
\tag{28}
$$
最后的单 t 项用准确原函数
$$
\partial_x\left\{
\frac23x^3(u-xp)r^3+\frac14x^5r^4
\right\}
=2x^3Cr^2t+2x^2(u-xp)r^3+\frac7{12}x^4r^4
$$
消去，得到
$$
\boxed{
I_2(Y(u,u),P(u,u))
=-2\int x^4Cr\,t^2
+2\int(u-xp)^2r^2
-\frac1{12}\int x^4r^4 .
}
\tag{29}
$$
所有边项由实际紧 $u$ 的原 flat jets 支付，不需要左尾紧，也不除以物理 x。

结合(25)，其完整三阶平方为
$$
\sum_i\lambda_i\int 2x^4C_i r_i(u_i''')^2,\qquad
\lambda_i=-a_i^2R_i,
\tag{30}
$$
其余两项是明确的连续 $C^2$ 四次函数。式(29)没有给整体符号：$C_ir_i$ 与真实 signed 系数 $a_i^2R_i$ 都不能删掉。

即使(30)与某个已付 principal 列空间独立，也还必须另证同一个 q 约束流形、受限 $F^\star$ 纤维、真实 copy、严格正核和有限频率完整根，才可得到保持十九门的新 $d_f(P)$ 取值。本稿不将这一步当作已经完成。

## 8. 本次结论的边界

当前圆已由完整端口两行证明(1)，所以最高规范第一通道只剩(19)六个未判值。原十二复制对第一通道是准确的正权平均，不能与第二通道的四次奇差分混用。式(25)、(29)给下一真实 profile 或响应研究可直接消费的完整 $P$ 方向。

这些结论不改变 R444 的范围：八个原 hook 响应保持 whole $J^+$、全部内部通量与 $C$，但其它响应方向、真实 period 特解、余九个端口系数及实际 prototype 基准仍须同时处理。没有宣称当前冻结圆的第一通道可调，没有把 signed 方向称为原固定几何上的免费路径，也没有宣布整个第四 joint 或主课题完成。
