# R442：七余量的二阶历史三次式与最高规范门的真实有限部分

日期：2026-11-16。**完整原式纸面证明；没有执行新的求积、profile、符号程序、秩、原根恢复或研究计算。**

[R439](R439-diagonal-current-quotient-and-exact-simultaneous-cap-criterion.md)把已付 144 响应的七个缺失 current 坐标合成一个六次多项式 $\mathfrak D_V(x)$，并从原第四 forcing 得到它的真实 $\beta/\tau$ 表达。[R437](R437-highest-rational-gauge-row-vanishes-on-the-complete-period-kernel.md)则证明，最高有理规范行在完整周期齐次核上恒零。

本稿给这两个仍未支付的量各一个更直接的原式接口，并证明它们之间的一条局部多项式身份：

1. $\mathfrak D_V$ 不必再恢复第三交叉 history $\beta$；它是一个只含真实第二累计尾的三次矩型，在矩抛物线上的限制。
2. 最高规范行的特解类值可以直接由原目标 $G$ 的累计通量计算。公式保留所有简单 $f'$ 零点的准确双极有限部分，没有把 $f'$ 预设为有正下界。
3. 该规范行的局部伴随通量在每个 $A_f=0$ 点，恰为 R439 最高剩余代表 $-\Theta_4$。这不把两个全局兼容条件判为等价。

来源为 [R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R181](R181-degenerate-self-adjoint-equation-for-fixed-circle-period-gauges.md)、[R292](R292-zero-platform-periods-and-ordered-second-history-matrix.md)、[R327](R327-analytic-packet-period-kernels-and-a-finite-same-gauge-joint-system.md)、[R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md)、R437 与 R439。以下全部积分使用原锚和原完整路径，不删除单包左尾。

## 1. 几何、原初值与两种不同的通量

先固定 R439 使用的同一实际闭几何：
$$
M_{\rm total}=0,\qquad
T_{\rm total}=\tau_{\rm hook}\mathfrak H,\qquad
\tau_{\rm hook}\ne0.
\tag{1}
$$
对七余 current 的解释同时保留 R439 的 $E(V)=(\pi V,\mathcal QV)=0$ 与 $O_{\rm all}(V)=0$。下文不把这些假设当成七余值已经为零。

沿路径记
$$
z=x+\omega,\qquad e=hz-k,\qquad Q=1+e^2,\qquad
\gamma=h_s .
$$
几何的路径参数是 $s$；下面 profile 导数仍用 $x$。

对任意固定三矩 $n=(n_0,n_1,n_2)$，原第二左尾为
$$
\Pi_n=(\mathfrak a_n z+t_n,\ p_nz,\ \eta_nz+q_n),
$$
$$
p_n=\frac{(1+d^2)n_0+2hdn_1+h^2n_2}{8h},
\qquad d=h\omega-k,
\tag{2}
$$
且
$$
(\mathfrak a_n)_s=kp_n,\qquad
\tau_n=(t_n)_s-\gamma t_n/h .
\tag{3}
$$
$\mathfrak a_n$ 是真实累计第二矩阵所给的二次左尾首系数。canonical 起点 $m(s_0)=0$ 给
$\mathfrak a_n(s_0)=0$；总 $M=0$ 给
$\mathfrak a_n(s_1)=0$。这两个结论不要求 $p_n,t_n,q_n,\tau_n$ 在端点各自为零。

原第三交叉恢复为
$$
W_C=\beta_n u'-\partial_x\beta_n\,u,\qquad
\beta_n(s_0,x)=0,
$$
$$
(\beta_n)_s=
\frac14\left[
\left(t_n-kq_n-\frac{\gamma\tau_n}{h}\right)\frac Q{h^2}
-\tau_n\partial_s\!\left(\frac Q{h^2}\right)
\right].
\tag{4}
$$
R439 的 current 系数 $c_V(x,n)$ 是局部 $u\,u''$ 的系数；在(1)下，
$$
c_V(x,n)=
\int\left(\frac{kQ}{4h}\beta_n+
\frac{kQ^2}{16h^3}\tau_n\right)ds .
\tag{5}
$$
一般未闭路径还须保留
$$
\left[\frac{\gamma e\alpha_n}{2h^2}\right]_{s_0}^{s_1},
\qquad
\alpha_n=\frac{\beta_n}{2}+\frac{\tau_nQ}{8h^2}.
\tag{6}
$$
在(1)下，两个不交真实包的二、三阶交叉场真正周期；三个真实右矩基把这一事实线性延伸到任意 $n$。几何端 jets 也周期，所以(6)是两端相同而相消，不是把它单端设为零。

以下的第二种通量是原退化周期算子的 $x$ 累计量，与(2)中的 $p_n$ 不同。为避免混淆，在第4节后统一写 $p=f'$。

## 2. 七余值只需第二累计 history

固定物理 $x$，在整个 $s$ 积分中把
$$
n_x=(1,x,x^2)
\tag{7}
$$
作为一个固定三向量代入。它是 R439 已定义的代数代入，不声称存在具有这些矩的点质量微包。

此时
$$
p_{n_x}=\frac Q{8h}.
\tag{8}
$$
略去下标 $n_x$，令
$$
a=\mathfrak a_{n_x},\quad p_{\rm tail}=p_{n_x},\quad
H=\frac Q{h^2},\quad
y=\frac{t_{n_x}}h,\quad w=\frac{q_{n_x}}h .
$$
由 $a_s=kp_{\rm tail}$，R439 的对角多项式为
$$
\mathfrak D_V(x)
=2\int a_s\beta\,ds+\frac12\int a_s\tau H\,ds .
\tag{9}
$$
逐项代入(4)、保留边界做分部积分：
$$
\begin{aligned}
\mathfrak D_V(x)
={}&
\left[2a\beta+\frac12a\tau H\right]_{s_0}^{s_1}\\
&-\frac12\int aH
\left(\tau_s-\frac{\gamma\tau}{h}+t-kq\right)ds .
\end{aligned}
\tag{10}
$$
这里用的是
$$
\frac12\int(a\tau H_s+a_s\tau H)\,ds
=\left[\frac12a\tau H\right]
-\frac12\int aH\tau_s\,ds .
$$
因此没有漏掉 $\tau_s$，也没有将 $\tau$ 当作紧 profile。

原 $a(s_0)=a(s_1)=0$ 准确杀掉(10)的显示边界。又
$$
\tau=h y_s,\qquad
\tau_s-\frac{\gamma\tau}{h}+t-kq
=h(y_{ss}+y-kw).
$$
结合(8)，得到
$$
\boxed{
\mathfrak D_V(x)
=-4\int_{\rm path}
\mathfrak a_{n_x}p_{n_x}
\left[
\left(\frac{t_{n_x}}h\right)_{ss}
+\frac{t_{n_x}}h-k\frac{q_{n_x}}h
\right]ds .
}
\tag{11}
$$

(11)只使用 R73 的真实第二累计矩阵及原几何。它没有任何待恢复的第三 $\beta$。若取消(1)或改动 canonical 初值，必须同时恢复(6)和(10)的边界，不能直接沿用盒中公式。

这条降层本身不证明(11)为零、正或可独立调节。特别，既有 whole $\mathcal Q$ 的三个矩二次型与这里的表达不能仅按名称或维数互相替代。

## 3. 一份真实三次矩张量与七个限制系数

对任意固定 $n$ 定义
$$
\mathcal C_{\rm path}(n)=
-4\int
\mathfrak a_n p_n
\left[
\left(\frac{t_n}h\right)_{ss}
+\frac{t_n}h-k\frac{q_n}h
\right]ds .
\tag{12}
$$
所有因子对 $n$ 线性，因此这是一个真实齐次三次多项式：
$$
\mathcal C_{\rm path}(n)
=\sum_{i+j+k=3}c_{ijk}n_0^i n_1^j n_2^k .
$$
无需为每个 $n$ 另选几何或原初值。式(11)准确等价于
$$
\boxed{\mathfrak D_V(x)=\mathcal C_{\rm path}(1,x,x^2).}
\tag{13}
$$
若 $\mathfrak D_V=\sum_{\ell=0}^6d_\ell x^\ell$，则
$$
\begin{array}{c|c}
\ell&d_\ell\\ \hline
0&c_{300}\\
1&c_{210}\\
2&c_{201}+c_{120}\\
3&c_{111}+c_{030}\\
4&c_{102}+c_{021}\\
5&c_{012}\\
6&c_{003}
\end{array}
\tag{14}
$$
所以七余多项式恒零的准确第二历史条件是
$$
\boxed{
\mathcal C_{\rm path}(n)
=(n_0n_2-n_1^2)
(\alpha n_0+\beta n_1+\gamma_0 n_2)
\quad\text{对某三个实数 }\alpha,\beta,\gamma_0 .
}
\tag{15}
$$
证明只需按(14)比较十个三次单项式：其限制核由
$n_0(n_0n_2-n_1^2)$、$n_1(n_0n_2-n_1^2)$、
$n_2(n_0n_2-n_1^2)$ 生成。

(15)不是对当前实际路径已支付的等式，也不是新响应秩。它给的是原七余值的一份完全保尾、只依第二历史的有限记录方式。R439 对实际全部根求值的商仍须保留；非零 $\mathfrak D_V$ 也不能单独代替那个求值商的非零证明。

## 4. 最高规范行的原局部密度

现在固定同一真实
$$
f=\sum_i a_i u_i,\qquad a_i\ne0,
\tag{16}
$$
所有最细包严格不交。采用 R431 的已构造类：每包内 $f'$ 的零点有限且简单，$A_f$ 的零点有限且简单，所有 $A_f$ 根上 $f'\ne0$；端 collar 是固定正解析 prefactor 乘 $\psi_3$，其中原 $\psi_3(y)=\exp[-3/(1-y^2)]$。零点数可以是任意原构造得到的有限数，不限定为一对。

以下定理也可在别的 profile 类中使用，但须单独验证这些假设或相应的更高阶极点条件。本稿不把多重 $f'$ 零点、非简单 $A_f$ 零点自动纳入。

写
$$
p=f',\qquad r=f'',\qquad t=f''',\qquad
A=6pt-2r^2,
$$
$$
a_f=f-xp+\frac{x^2r}{2},\qquad
\mathcal W=x^2a_f^2 .
\tag{17}
$$
原 $Y=\Phi_{p_2}$ 为
$$
Y(f,f)=-xf^2+x^2fp-\frac{x^3p^2}{2}
-\frac{x^2}{4}J(x^2r^2+2p^2).
\tag{18}
$$
它有真实纯 $x^2$ 左尾；不截断这一输出。

直接微分原(18)：
$$
Y'=-f^2+x^2fr-x^3pr+\frac{x^4r^2}{4}
-\frac x2J(x^2r^2+2p^2),
$$
$$
Y'''=4xa_f t+\frac{x^4t^2}{2}+x^2a_f t'.
$$
利用 $a_f'=x^2t/2$，恰得
$$
\boxed{x^2Y'''+2xY''-2Y'=\mathcal W''.}
\tag{19}
$$
因另一个输入 $k$ 真紧，原两次分部积分支付全部端项：
$$
\boxed{
\ell_f(k):=I_2(Y(f,f),k)
=-\int_I\mathcal W k'''
=-\int_I\mathcal W'' k'.
}
\tag{20}
$$
这些式子没有要求 $k$ 在每个包端或间隙为零。全局紧性和(18)的真实二次尾足够。

定义一个完全局部的原函数
$$
\boxed{
\mathfrak F_f=-p\mathcal W'+r\mathcal W-\frac23a_f^3 .
}
\tag{21}
$$
由于 $t\mathcal W=2a_f^2a_f'$，
$$
\boxed{\mathfrak F_f'=-p\mathcal W''.}
\tag{22}
$$
这是下文所有有限部分的来源，不能用任意积分常数替代(21)。

## 5. 原目标的累计通量与适用域

原完整周期算子满足
$$
L_f(k)''=(Ak'')'-6(rt)'k',
$$
$$
pL_f(k)''=\{A(pk''-rk')\}'.
\tag{23}
$$
先假设一个真实全目标 $G$ 确在同 collar 紧像中：
$$
L_f(k)=G,\qquad k\in C_c^\infty(I).
\tag{24}
$$
这是本节等式的适用域，不是由下面积分式推出的存在性。

在每包 $J_i=(\ell_i,r_i)$ 定义
$$
J_{G,i}(x)=\int_{\ell_i}^{x}p\,G''.
\tag{25}
$$
在真实平端，$p,r,A$ 的全部 jets 为零而 $k$ 光滑，故(23)的左端通量确为零。因此
$$
\boxed{
J_{G,i}=A(pk''-rk')
}
\tag{26}
$$
是原锚的结论，不是逐包另设自由常数。它同时给每包总通量零。

在 $pA\ne0$ 的开段，
$$
\left(\frac{k'}p\right)'=\frac{J_{G,i}}{Ap^2}.
\tag{27}
$$
在简单 $A$ 根 $b$ 上，由(26)有 $J_{G,i}(b)=0$。因为该处 $p\ne0$，商 $J_{G,i}/A$ 按真实光滑解延拓，(27)无极点。

对一个尚未证明属于像的目标，可以先检查 $J_{G,i}(b)=0$ 等必要条件，也可在满足显示除法条件时定义下面的数值泛函。但该定义本身不支付右 collar、平台仿射尾、平端逆 germ、$k'$ 总积分或其余 range 条件；不能用“有限部分存在”代替(24)。

## 6. 每个简单 p 零点的准确双极

取包内一个 $p$ 的零点 $c$。令 $s=x-c$，
$$
r_0=r(c)\ne0,\qquad t_0=t(c).
$$
原 Taylor 展开给
$$
p=r_0s+\frac{t_0}{2}s^2+O(s^3),\qquad
A=-2r_0^2+2r_0t_0s+O(s^2),
$$
所以
$$
\boxed{Ap^2=-2r_0^4s^2+O(s^4).}
\tag{28}
$$
三次项准确为零。由 $J_{G,i}'=pG''$ 与(22)，
$$
J_{G,i}(x)=J_{G,i}(c)+O(s^2),\qquad
\mathfrak F_f(x)=\mathfrak F_f(c)+O(s^2).
$$
故
$$
\boxed{
\frac{\mathfrak F_fJ_{G,i}}{Ap^2}
=-\frac{\mathfrak F_f(c)J_{G,i}(c)}{2r_0^4s^2}
+O(1).
}
\tag{29}
$$
这里没有 $s^{-1}$ 项。注意 $A(c)=-2r_0^2<0$，所以这些点与 $A$ 根严格分离。

令
$$
q_c=-\frac{\mathfrak F_f(c)J_{G,i}(c)}{2r(c)^4}.
$$
本稿采用准确的对称有限部分
$$
\operatorname{FP}\!\int_{J_i}
\frac{\mathfrak F_fJ_{G,i}}{Ap^2}
=
\lim_{\epsilon_c\downarrow0}
\left[
\int_{J_i\setminus\bigcup_c(c-\epsilon_c,c+\epsilon_c)}
\frac{\mathfrak F_fJ_{G,i}}{Ap^2}
-\sum_c\frac{2q_c}{\epsilon_c}
\right].
\tag{30}
$$
不同零点可独立取小半径；它们之间和与端点之间都有固定正距离。$A$ 根按第5节的光滑商处理，不增加新的有限部分。

式(30)的系数全部由已固定 $f$ 和真实 $G$ 给出，不需要先读取某个特解的 $k'(c)$。对于(24)，(26)也可核为
$J_{G,i}(c)=2r(c)^3k'(c)$。

## 7. 平端、内点与完整积分身份

在一个真实平端，以到端点的距离 $\zeta>0$ 表示原 profile：
$$
f(\zeta)=a(\zeta)e^{-c_0/\zeta},\qquad
c_0>0,\quad a(0)\ne0,
\tag{31}
$$
允许吸收原仿射宽度与有限解析因子。因而 $p$ 在靠端的内部非零；所有固定阶导数是 $f$ 乘至多有限阶负幂，并有
$|p|\asymp |f|\zeta^{-2}$。由(17)、(21)，对某个固定有限 $N$，
$$
|\mathfrak F_f|\le C|f|^3\zeta^{-N},\qquad
\left|\frac{\mathfrak F_f}{p}\right|
+\left|\frac{\mathfrak F_f r}{p^2}\right|
\le C|f|^2\zeta^{-N}.
\tag{32}
$$
因此对任何允许的光滑紧解，$k',k''$ 有界，且
$$
\frac{\mathfrak F_fk'}p\longrightarrow0,\qquad
\mathfrak F_f\left(\frac{k'}p\right)'
\quad\text{在平端绝对可积}.
\tag{33}
$$
这不是假设 $p\ge\delta$，也不要求 $k$ 在单包端比 $f$ 更快衰减。即使 $k$ 在该包边界有非零平台值或非零有限阶导数，(32)仍支付所需边项。

在删去各 $p$ 零点的小区间上，用(20)、(22)、(27)：
$$
\begin{aligned}
-\int\mathcal W''k'
&=\int\mathfrak F_f'\frac{k'}p\\
&=\left[\mathfrak F_f\frac{k'}p\right]
-\int\frac{\mathfrak F_fJ_{G,i}}{Ap^2}.
\end{aligned}
\tag{34}
$$
平端项由(33)为零。若 $k'/p=b_{-1}/s+O(1)$，则每个内点的两侧显示边界为
$-2\mathfrak F_f(c)b_{-1}/\epsilon_c+o(1)$；
而(29)的 $q_c=-\mathfrak F_f(c)b_{-1}$。这恰是(30)所扣除的双极项。原左边在该点光滑，没有余留常数或对数。

逐包相加，间隙上 $\mathcal W=\mathfrak F_f=0$，得到
$$
\boxed{
\ell_f(k)=
-\sum_i\operatorname{FP}\!\int_{J_i}
\frac{\mathfrak F_f(x)J_{G,i}(x)}{A_f(x)(f'(x))^2}\,dx,
\qquad G=L_fk .
}
\tag{35}
$$

这是原最高规范泛函在真正像上的显式因子化。所有包幅、中心、宽度均在实际 $f$ 中；没有用一个标准母代替这些物理函数。

对非简单 $p$ 零点需要重新保留相应 Laurent 项；对不具有(31)的端类需要重新支付(33)；对非简单 $A$ 点需要原光滑除法条件。本文不把(30)无条件推广到这些情形。

## 8. 同一 period 的最高规范兼容，不另选特解

在原真实像上定义
$$
\mathfrak P_f(G)=
-\sum_i\operatorname{FP}\!\int_{J_i}
\frac{\mathfrak F_fJ_{G,i}}{A_fp^2}.
\tag{36}
$$
由(35)，它等于任何紧特解的 $\ell_f(k)$，与 R437 的
$\ell_f|_{\ker L_f}=0$ 一致。有限部分及其扣除系数都对 $G$ 线性。

原两个 incoming 清理后的目标是
$$
G_d^c=-V_d^c/(2\tau_{\rm hook}),\qquad
G_e^c=-V_e^c/(2\tau_{\rm hook}).
$$
一旦两者的完整 range 条件确实支付，最高端口行的准确必要条件便是
$$
\boxed{\mathfrak P_f(G_d^c)=\mathfrak P_f(G_e^c)=0.}
\tag{37}
$$
因为
$$
P_{2,\theta}(k)=\frac{\kappa}{24}\ell_f(k),
$$
非零 $\kappa$ 不能改变(37)。

同一个真实 incoming 矩阵 $X=\Phi_{\mathsf m_*}$ 不能省去。R326/R437 给
$$
G_d^c=G_d^0+L_f(X\Delta),\qquad
G_e^c=G_e^0-L_f(X(f,g)).
$$
这些 $X\Delta,X(f,g)$ 由原三矩条件真紧。若原目标在像内，(35)准确保留
$$
\mathfrak P_f(G_d^c)
=\mathfrak P_f(G_d^0)+I_2(Y(f,f),X\Delta),
$$
$$
\mathfrak P_f(G_e^c)
=\mathfrak P_f(G_e^0)-I_2(Y(f,f),X(f,g)).
\tag{38}
$$
不能把同一个 $\mathsf m_*$ 当成免费控制参数，也不能用新的齐次规范改变(37)。

## 9. 与七余最高 current 的精确局部连接

R439 的完整形式代表为
$$
\begin{aligned}
\Theta_4={}&
\frac23 f^3-2x^2fp^2+2x^3fpr-\frac{x^4fr^2}{6}\\
&+\frac43x^3p^3-2x^4p^2r+\frac23x^5pr^2 .
\end{aligned}
\tag{39}
$$
此处保留全部 $p$-only 项，而不是只取三个含 $f$ 单项式。它是 R439 右逆中 $d_6n_2$ 对应的 $K/4$ 代表，不将 formal 代表宣称为已实现成本。

由(21)与 $a_f'=x^2t/2$，
$$
\mathfrak F_f=\frac43a_f^3-2fa_f^2-x^4pa_ft.
$$
展开 $a_f=f-xp+x^2r/2$，恰得全 jets 身份
$$
\boxed{
\mathfrak F_f=-\Theta_4-\frac{x^4a_f}{6}A_f .
}
\tag{40}
$$
因此在每个真实内部退化点，
$$
\boxed{\mathfrak F_f|_{A_f=0}=-\Theta_4|_{A_f=0}.}
\tag{41}
$$
这把最高规范行的原局部伴随通量，接到七余 current 的最高代表；所有真实宽度、位置、jet 和规范因子均已保留。

但(35)仍依赖整个包上的 $J_{G,i}$，包括 $p$ 零点的准确扣除项；R439 的七余求值条件只读取一批 $A_f$ 点。因此(40)—(41)不证明两种条件等价，也不证明一个条件自动支付另一个。更不能从某个 $\Theta_4$ 的形式坐标非零推出当前实际点商非零。

## 10. 已付结论与下一实际条件

本稿给出：

- 原七余多项式的第二历史公式(11)，以及真正三次矩型限制(13)—(15)；
- 最高规范泛函在原紧像上的准确目标公式(35)—(38)；
- 其局部伴随通量与原最高七余代表的全多项式身份(40)。

当前实际路径是否满足(15)、R439 全点求值商是否为零、两原目标是否属于完整 $L_f$ 像，以及(37)是否成立，均仍是未付问题。本稿不把原 144 响应像升级为整个 $\mathcal R$ 的像，也不把 signed current 修正当作 actual 同基准正时间控制。

式(11)提供只需第二累计历史的真实目标；式(35)提供不依赖特解选择的最高规范读出。下一步可以分别作用于原实际路径或已证允许的响应，但所有新结论必须保同一 $f,g,w_\theta$、原平台与端点、十三行剩余兼容和完整路径基准。
