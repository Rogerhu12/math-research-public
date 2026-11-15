# R349：完整第二 self 与十目标正锥支付第四个 Gaussian 面积

日期：2026-11-15。**完整有限纸面构造。** 未执行求积、符号程序、profile 扫描、人工测试或研究计算。

[R348](R348-true-translation-and-Green-self-terms-pay-the-first-positive-minus-one-Gaussian-moment.md) 已支付 $Y$–$Z_*$ 的第零、第1外矩。本稿计算它的完整第2 self，保原非紧二次输出和全部 Green 端项，再在真实母包纤维上取得两号。新增二维方向与原八目标正锥联合，最终在同一个弱单 hook 圆上支付这个 pair 的全部三个外矩，并保留其他三个完整面积、$\Psi$ 和三条 directed 行。

所用原型均是新增的强 rank-one 完整块。原弱核心及其最终中心固定，不对它假用单包中心导数公式，也不删 R348 一般平移中的未付 $Y$–$P$、$Y$–$W_*$ 项。

来源：[R259](R259-complete-Gaussian-area-moments-and-ordered-micropacket-interface.md)、[R263](R263-ordered-Gaussian-area-81-scalar-recursion.md)、[R267](R267-amplitude-width-shapes-pay-the-complete-minus-one-minus-three-area.md)、[R270](R270-odd-mother-perturbation-pays-a-further-Gaussian-zero-moment.md)、[R291](R291-exact-positive-Gaussian-square-moment-is-the-leading-energy.md)、[R346](R346-positive-six-target-cone-pays-a-further-complete-Gaussian-zero-moment.md)、R348 及 [R293](R293-finite-frequency-zero-of-all-necessary-symmetric-Gaussian-observations.md)。

## 1. 同一规范与最后一个外矩

固定原真实几何 $M=0$、$T=\kappa_H\mathfrak H$、$\kappa_H\ne0$，及共振端芽
$$
h=h_e e^{\varepsilon\sigma^2},\quad
k=\kappa(1-2\varepsilon\sigma^2),\quad
\omega=\kappa/h,\quad \varepsilon=\kappa^2/4,\quad
0<t:=\kappa^2<1/100.
$$
仍记
$$
P=\Phi_{r_0},\ R=\Phi_{r_1},\ S=\Phi_{s_0},\
L=\Phi_{p_0},\ U=\Phi_{s_1},\ Y=\Phi_{p_2},
$$
$$
W_*=aR+bS,\qquad Z_*=dL+eU,
$$
$$
a=-\frac{51t^2+2t+8}{64h_e^2},\quad
b=-\frac{34t^2+8t}{64h_e^2},\quad
d=\frac{6\kappa t}{h_e},\quad
e=-\frac{\kappa(15t+1)}{4h_e}.
\tag{1}
$$
对 $u=f\cos\theta+g\sin\theta$、$D=f\odot f-u\odot u$，保持
$$
\mathcal M_j=I_j\{u,[W_*,P](u;D)\},\quad
\mathcal A_j=I_j\{u,[Z_*,P](u;D)\},
$$
$$
\mathcal B_j=I_j\{u,[Z_*,W_*](u;D)\},\quad
\mathcal C_j=I_j\{u,[Z_*,Y](u;D)\}.
\tag{2}
$$
原第三外矩是
$$
I_2(v,w)=\int(x^2v''w''+2v'w').
$$
本稿新增 $\mathcal C_2=0$，全部相位成立；原 Gaussian pair $(1,-1)$ 与它只差非零常数 $\kappa h_e$。

R348(4)—(7)已经给出一般真实平移。
特别 $Y^{(s)}$ 含
$s(2\Phi_{p_1}-\Phi_{t_1}/2)+s^2(L-U)-s^3(R+S)/2-s^4P/4$，
所以即使 $\mathcal C_0=\mathcal C_1=0$，也不能直接断言
$\mathcal C_2^{(s)}=\mathcal C_2$。
以下不移动原弱核心；只在新原型中从完整 self 重新得到准确的中心多项式。

## 2. 全部原第二 self

令 $u$ 为任意实紧 profile，写
$$
v=u',\qquad r=u'',\qquad t_3=u''',\qquad
C=J(x^2r^2+2v^2).
$$
$J$ 始终取原右锚。原 cubic 密度为
$$
F_{L,2}=\int(-xur^2+x^2vr^2/2-v^3/3),
$$
$$
F_{U,2}=\int(2xur^2-4x^2vr^2+x^3r^3-4v^3/3),
\qquad F_{Y,2}=0.
\tag{3}
$$
前两式来自 R267 原三外矩；最后一式是 R291 对任意紧输入的完整恒等式，不是只取 principal。

定义
$$
S_{X,Y,2}(u)=2I_2\{u,[X,Y](u;u\odot u)\}.
$$
准确有
$$
\boxed{
\begin{aligned}
S_{L,Y,2}(u)=-\int\bigg[
&2u^2v^2-\frac43xuv^3+\frac13x^2v^4\\
&+x^2(u-xv)^2r^2+\frac13x^4(u-xv)r^3
+\frac{x^6r^4}{24}\bigg],
\end{aligned}}
\tag{4}
$$
$$
\boxed{S_{U,Y,2}(u)=-5S_{L,Y,2}(u).}
\tag{5}
$$
这两式不要求单包三矩为零；所有二次输出原尾均保在下一节的推导中。

作为原式的符号核对，(4)也等于
$$
-\int\left[
\frac{v^2}{3}\{(xv-2u)^2+2u^2\}
+x^2r^2\left\{(u-xv+x^2r/6)^2+\frac{x^4r^2}{72}\right\}
\right].
\tag{6}
$$
非零实紧 $u$ 时严格为负。但圆的 self 权是 $c_i(\theta)^2d_i(\theta)$，其中 $d_i=a_i^2-c_i^2$ 可以两号，不能由这个单包符号推整圆面积同号。

## 3. 从原 Y 输出核清 local 变分和 Green 尾

原完整场为
$$
Yu=-xu^2+x^2uv-\frac{x^3v^2}{2}-\frac{x^2C}{4},
$$
$$
(Yu)'=-u^2+x^2ur-x^3vr+\frac{x^4r^2}{4}-\frac{xC}{2},
$$
$$
\begin{aligned}
(Yu)''={}&-2uv+2xur-2x^2vr
+x^2(u-xv)t_3+\frac{x^3r^2}{2}
+xv^2-\frac C2+\frac{x^4rt_3}{2}.
\end{aligned}
\tag{7}
$$
所有 $C$ 项都是真实 primitive。

采用 R259 的 local Euler 变分接口，不能把 $u+\tau Yu$ 冒称为紧输入族。
$F_{L,2}$ 三个偏导是
$$
-xr^2,\qquad x^2r^2/2-v^2,\qquad -2xur+x^2vr,
\tag{8}
$$
$F_{U,2}$ 的三个偏导是
$$
2xr^2,\qquad -4x^2r^2-4v^2,\qquad
4xur-8x^2vr+3x^3r^2.
\tag{9}
$$
把(7)代入(8)、(9)。

对 $L$，完整 $C$ 系数为
$$
xv^2/2+xur-x^2vr/2
=(xuv-x^2v^2/4)'-uv.
$$
所以此项积分准确为
$$
\int(xuv-x^2v^2/4-u^2/2)(x^2r^2+2v^2).
\tag{10}
$$
这里 $\int uvC=\frac12\int u^2(x^2r^2+2v^2)$，只用了紧 outer；
没有将 $C$ 左值设零。

对 $U$，完整 $C$ 系数为
$$
2xv^2-2xur+4x^2vr
=(2x^2v^2-2xuv)'+2uv,
$$
因此其积分准确为
$$
\int(2x^2v^2-2xuv+u^2)(x^2r^2+2v^2).
\tag{11}
$$
原 primitive 至此全部化成 local 项。

给出余下含最高导数项，便于核对全部系数。置
$A_0=u-xv$、$B_0=2u-xv$。
在 $L$ 的 local 变分中，含 $t_3$ 的部分是
$$
-x^3B_0A_0rt_3-\frac{x^5B_0r^2t_3}{2}.
$$
将它们分别写为 $(r^2)'/2,(r^3)'/3$ 后积分，连同(10)及其余 local 项，准确得到(4)右边。

对 $U$，含 $t_3$ 的部分是
$$
4x^3(u-2xv)A_0rt_3+(5x^5u-7x^6v)r^2t_3
+\frac32x^7r^3t_3.
$$
按 $(r^2)'/2,(r^3)'/3,(r^4)'/4$ 处理，连同(11)，其完整 local 结果是(4)右边的 $-5$ 倍。因此
$$
D_{\rm loc}F_{L,2}[Yu]=S^{\rm loc}_{L,Y,2},\qquad
D_{\rm loc}F_{U,2}[Yu]=-5S^{\rm loc}_{L,Y,2}.
\tag{12}
$$

还须核原 Green 端项。原 $Y$ 左尾是 $-\mu_2x^2/4$；$L,U$ 的左尾都为二次多项式。对任意
$X=Ax^2+Bx+C_0$ 和 $Y_0=Dx^2$，令
$$
g_0=XY_0'''-X'Y_0''+X''Y_0'-X'''Y_0,
$$
则 $I_2$ 的 Green 原函数是
$$
x^2g_0+2x(XY_0''-X''Y_0)-2(XY_0'-X'Y_0).
\tag{13}
$$
三项分别为
$-2BDx^2$、$4BDx^2+4C_0Dx$、
$-2BDx^2-4C_0Dx$，总和准确为零。
右端原场为零，因此 $L/Y,U/Y$ 两项 Green 皆零。
结合 $F_{Y,2}=0$ 的 local Euler 恒等式，(12)就是完整 self (4)、(5)。
没有先把两条非紧二次输出视为紧支撑。

## 4. 新中心导数与原第一 self 的关系

R348 已给
$$
S_{L,Y,1}=\int\left[
2x(u-xv)^2r^2+\frac23x^3(u-xv)r^3+\frac{x^5r^4}{12}\right]
$$
以及完整 $S_{U,Y,1}$。
直接对(4)的显式 $x$ 求导，得到准确身份
$$
\boxed{
\frac{d}{ds}S_{L,Y,2}(T_su)
=\frac12\{S_{U,Y,1}(T_su)-S_{L,Y,1}(T_su)\}.
}
\tag{14}
$$
例如其 local 密度为
$$
\frac43uv^3-\frac23xv^4-2xu^2r^2+6x^2uvr^2
-4x^3v^2r^2-\frac43x^3ur^3
+\frac53x^4vr^3-\frac14x^5r^4,
$$
正是原两条第一 self 密度之差的一半。

因此
$$
S_{Z_*,Y,2}=(d-5e)S_{L,Y,2},\qquad
\partial_s S_{Z_*,Y,2}
=\frac{d-5e}{2}S_{U-L,Y,1}.
\tag{15}
$$
原 $\Gamma_{L,Y,j}=\Gamma_{U,Y,j}=0$ 对全部三个外矩成立。故(14)、(15)可逐项用于新增真实不交 rank-one 微包的完整 self 和，包括所有原八／十二副本。
它们不被用于原弱 rank-two 核心。

## 5. 同一 Fκ 纤维对所有 L/U 组合的准确约束

取 R346 的真实 even 母小族
$$
\mathcal F_\kappa(v_\tau)=0,\qquad
\mathcal J(v_\tau)=h\tau,\quad |\tau|<\tau_*,
\tag{16}
$$
固定实际小正 $h$。写
$$
C=\int r^4,\quad X_2=\int y^2r^4,\quad
N=\int yv'r^3,\quad W=3\int(v')^2r^2+\int vr^3,
\quad\mathcal J=W-2N.
$$
所有量来自同一个 $v_\tau$。

R267 的原形状式是
$$
\lambda_\kappa(X_2-C\nu)+\frac43(d+11e)N-\frac{8e}{3}W=0,
\quad \lambda_\kappa=-5(d+7e)/6.
$$
因此在(16)上准确有
$$
\boxed{X_2-C\nu=\frac85N-\frac{16e}{5(d+7e)}\mathcal J.}
\tag{17}
$$

对任意固定 $X_{\lambda,\mu}=\lambda L+\mu U$，R270 原第零 self 的中心系数为
$$
a_4(\lambda,\mu)=5(\lambda-5\mu)/24,
$$
$$
\mathcal B_{\lambda,\mu}
=6a_4(\lambda,\mu)X_2-4(\lambda-4\mu)N+(\lambda-3\mu)W.
$$
代(17)得到
$$
\boxed{
\mathcal B_{\lambda,\mu}-6a_4(\lambda,\mu)C\nu
=\Gamma_{\lambda,\mu}\mathcal J,\qquad
\Gamma_{\lambda,\mu}
=\frac{\lambda(d+3e)-\mu(3d+e)}{d+7e}.
}
\tag{18}
$$
特别
$$
\Gamma_{-1,1}=-\frac{4(d+e)}{d+7e}\ne0.
\tag{19}
$$
这一步同时保留全部实际母积分，没有把一个新的 $L/U$ 组合当成独立 shape 值。

## 6. 第二矩的全 finite-copy 多项式

仍用 R346 的两斜率
$$
1/3<\alpha<1/2,\quad
\beta=(5-\alpha)/(1-\alpha),\quad
q_0=[16(1-\alpha)^2]^{-1},\quad n=2^{11}.
$$
原低／高宽、真实排序和方差为
$w_L=q_0\delta,w_H=\delta$、
$V_L-V_H=\nu(v_\tau)(1-q_0^2)$。
八／十二 copy 的全部实际位置和第四幅度一起固定。
记
$$
K=64na_c\mathcal W,\qquad a_c=q_0(1-\alpha).
$$

令 $E^{X,j}_{04}$ 为 $2I_j\{u,[X,Y](u;D)\}$ 的 $\sin^4\theta$ 系数。
所有这些组合均无跨微包核，故逐包两斜率关系准确给
$$
E^{X,j}_{22}=\alpha\beta E^{X,j}_{04}.
\tag{20}
$$

R346 第零式、R348 第一式对任意 $X_{\lambda,\mu}$ 都线性成立。
在(16)上，它们的全有限宽形式为
$$
E^{X,0}_{04}(\xi)
=K\delta\left[
(1-q_0^2)\Gamma_{\lambda,\mu}\mathcal J\,\xi^2
+\delta^2R_{\lambda,\mu}\right],
$$
$$
E^{X,1}_{04}(\xi)
=2K\delta\left[
\frac{(1-q_0^2)\Gamma_{\lambda,\mu}\mathcal J\,\xi^3}{3}
+\delta^2R_{\lambda,\mu}\xi\right].
\tag{21}
$$
$R_{\lambda,\mu}$ 是由 R270 原全式取线性组合所得的实际值：
$$
R_{\lambda,\mu}=
a_4(\lambda,\mu)C(\overline M_{4,H}-\overline M_{4,L})
+\mathcal B_{\lambda,\mu}(\overline V_H-q_0^2\overline V_L)
+\mathcal D_{\lambda,\mu}(1-q_0^4).
\tag{22}
$$
其中 $\mathcal D_{\lambda,\mu}$ 是 R270(11)的原线性密度；
各带横线中心矩都含全部真实副本，未被删除或独立赋值。

把(21)的 $X=U-L$ 代入(15)并对实际共同中心积分。中心零的第二矩不必为零；其完整伸缩为 $\delta^5$，因为原算子总权为0、$I_2$ 权为 $-1$、四次 profile 归一幅为 $\delta^6$。准确得到
$$
\boxed{
E^{Z_*,2}_{04}(\xi)=K\delta\left[
\Lambda_\kappa(1-q_0^2)\mathcal J\,\xi^4
+\frac{d-5e}{2}\delta^2R_{-1,1}\xi^2
+\delta^4\Theta_\tau\right],
}
\tag{23}
$$
$$
\boxed{
\Lambda_\kappa=-\frac{(d-5e)(d+e)}{3(d+7e)}
=-\frac{\kappa(99t+5)(1-9t)}
{12h_e(81t+7)}\ne0.
}
\tag{24}
$$
系数来自 $(d-5e)\Gamma_{-1,1}/12$，没有漏掉积分的 $1/4$。

$\Theta_\tau$ 是完整中心零值，不是任意常数。
例如将全部副本的 dimensionless widths/centers 固定在 $\delta=1,\xi=0$，
就有准确原式
$$
\Theta_\tau=\frac{d-5e}{K}
\sum_i b_i^2(a_i^2-b_i^2)
S_{L,Y,2}(\eta_{w_i,\xi_i}),
\tag{25}
$$
其中幅度 $a_i,b_i$ 已含真实完整 copy 因子，self 取(4)。
(25)仅定义一个实际有限积分，没有执行求积。
它随真母参数连续，并在所选有限参数邻域有界。

## 7. 新完整第二矩的两号和二维正锥

取两个不同的 $\alpha_1,\alpha_2\in(1/3,1/2)$，每个取实际
$\tau=\pm\tau_0\ne0$。先固定真实间距、全部完整副本及四个互不交的正中心区间，再选足够小的有限正 $\delta$。

由(16)、(23)，
$$
\frac{E^{Z_*,2}_{04}}{K\delta}
\longrightarrow
\Lambda_\kappa(1-q_0^2)h\tau\,\xi^4 .
\tag{26}
$$
在固定正中心严格非零且随 $\tau$ 反号。
$\delta^2$、$\delta^4$ 两个完整余项在此前固定的有限参数上有界，因此实际正宽已经给严格两个符号。

(20)使四列 $\mathcal C_2$ 向量沿
$$
\pm(\alpha_1\beta_1,1),\qquad
\pm(\alpha_2\beta_2,1).
\tag{27}
$$
它们满二维并有严格正核，故正锥为 $\mathbb R^2$。
全部 odd 相位仍由原十二完整副本支付。

每个新原型也有
$$
\mathcal M_j=\mathcal A_j=0\ (j=0,1,2),\qquad
\mathcal B_0=0,\qquad
\Psi=\psi_i\sin^2\theta,\quad \psi_i>0.
\tag{28}
$$
这些是原真 $\mathcal F_\kappa$、强 hook、quartic 张量及真实反射所给；
没有假定它们的 $\mathcal B_1,\mathcal B_2,\mathcal C_0,\mathcal C_1$ 为零。
这些整值全部进入下一节。

## 8. 与已有八目标的完整联合，而非逐项忽略代价

原全式伸缩为
$$
\mathcal B_1:H^{-5},\quad
\mathcal B_2:H^{-4},\quad
\mathcal C_0:H^{-3},\quad
\mathcal C_1:H^{-2},\quad
\boxed{\mathcal C_2:H^{-1}},\qquad
\Psi:H^{-7}.
\tag{29}
$$
$Y$ 权为 $+1$、$Z_*$ 为 $-1$，且 $I_2$ 的两项同权 $-1$。
这些是含真实 primitive 的完整原式，不是 principal 估计。

给§7四个新原型作共同大有限伸缩 $H$，第四幅度乘 $H$。
新 $\mathcal C_2$ 列保持不变，旧八目标依次成为
$O(H^{-4}),O(H^{-3}),O(H^{-2}),O(H^{-1})$。

R348 给一个实际八目标矩阵
$$
M_8:\lambda\longmapsto
(\mathcal B_1,\mathcal B_2,\mathcal C_0,\mathcal C_1)
$$
满秩并含严格正核。记其原十六列的 $\mathcal C_2$ 值为 $D_8$；
它们是固定 profiles 的真实值，不作为新自由坐标。
新十目标矩阵趋于
$$
\begin{pmatrix}
M_8&0\\
D_8&C_2^{\rm new}
\end{pmatrix},
\tag{30}
$$
其中新四列 $C_2^{\rm new}$ 有(27)的正锥。

极限满行秩10。先取 $k_8>0$、$M_8k_8=0$，
再由新四列的全平面正锥取严格正 $k_{\rm new}$，
使 $C_2^{\rm new}k_{\rm new}=-D_8k_8$。
于是极限含严格正核。固定一个非零十列子式，仅修正这十个坐标便能在足够大的有限 $H$ 把趋零残差消去，同时保持全部坐标正。
故实际有限矩阵满足
$$
\boxed{\operatorname{cone}_+(M_{10,H})=\mathbb R^{10}.}
\tag{31}
$$
这是明确原型上的实际正核与秩结论；不宣原72方程具有这个普遍秩。

## 9. 同一个最终弱圆上的完整支付

使用 R348 最后强控制器前的实际状态：
$$
\mathcal M_j=\mathcal A_j=\mathcal B_j=0,\quad
\mathcal C_0=\mathcal C_1=0,\quad
\Psi=-\Delta_0\sin^2\theta,\quad\Delta_0>0.
\tag{32}
$$
原弱部分及其宽 cutoff、补矩、旧模块和最终中心全部固定。
把当前完整 $\mathcal C_2$ even 残差记为 $r_{\rm old}\in\mathbb R^2$。

固定(31)的正核 $k>0$ 与一个实右逆 $R_{10}$。
再对这整组真实原型作共同正伸缩 $S$，第四幅度为 $S^5c_i(S)$，
$$
c(S)=k+R_{10}(0,0,0,0,-r_{\rm old}/S^4).
\tag{33}
$$
五个目标块依次是
$\mathcal B_1,\mathcal B_2,\mathcal C_0,\mathcal C_1,\mathcal C_2$，
每块二维。由(29)，其实际缩放分别为
$1,S,S^2,S^3,S^4$。
对足够大的有限 $S$，所有 $c_i(S)>0$ 且有界，所以原式准确给
$$
\Delta\mathcal B_1=\Delta\mathcal B_2
=\Delta\mathcal C_0=\Delta\mathcal C_1=0,\qquad
\Delta\mathcal C_2=-r_{\rm old}.
\tag{34}
$$
(28)中的旧零同时保留。

新增 $\Psi$ 完整成本是
$$
S^{-2}\sum_i c_i(S)\psi_i\,\sin^2\theta.
\tag{35}
$$
取有限 $S$ 使其小于 $\Delta_0/2$，并使全部新正包络位于原固定 profiles 右方。所有内部严格间隙随共同伸缩保持，没有移动已付的弱中心矩。

最后沿原 R348/R346 的同 $F^\star$ 强控制器入口，以有限 $N$ 的真实正核根支付三条 directed 行，并将 $\Psi$ 归零。控制器自身全部72面积原值为零，同纤维纠正保持它们，因此也保持(34)及其余旧外矩。全部新 cross 在完整 blocks 之间由真实 inner 三矩零消去，未把弱核心内部 rank-two 项替换为微包 self。

## 10. 最终范围与有限选择顺序

次序是：先固定几何和实际负余基线；固定真母小族及两种 $\alpha$；
固定真实间距、完整副本和最后正中心；选择有限正 $\delta$ 取得两个严格号；
固定全部原型的真实值后选择有限 $H$ 得十目标正核；
再选有限 $S$ 和(33)的严格正幅；最后在已经固定的强控制区求一个有限 $N$。

共同合法正区间按照既有 R105/R114/R271 范围，从这一全部有限构造及几何包络一次选择，保全部 collars。不把零宽、无限频率或无限正中心当成实际答案，也不扩大任意先前冻结窄区间的承诺。

最终同一个真实弱单 hook 圆满足
$$
\boxed{
\mathcal M_j=\mathcal A_j=\mathcal B_j=\mathcal C_j=0
\quad(j=0,1,2),\qquad
\Psi=F_0=F_1=F_2=0
}
\tag{36}
$$
全部相位成立。原三矩、第二／第三 range、全部 odd Gaussian 位置及原指定完整一层条件保留。

尚未支付的是 $Y$–$P$ 与 $Y$–$W_*$ 两个完整面积，即六个外矩、12个形式 even 位置；其中原 $Y$–$P$ 第一矩已有一条准确重复，不宣独立秩。整个剩余 ruling、完整第四 period 与同一个 gauge 的 joint 解仍未由本稿成立。
