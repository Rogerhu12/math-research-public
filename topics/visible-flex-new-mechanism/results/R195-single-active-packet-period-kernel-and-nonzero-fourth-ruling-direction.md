# R195：单边活动包内的周期核给出有限且非零的第四 ruling 商方向

日期：2026-11-15。完整纸面证明；没有新研究积分、原式编译或数值采样。

来源：[R56 完整右锚恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 逐点八矩及累计历史](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R183 的导数分包圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R184 joint 判据](R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)及 [R191 共同常值平台零像](R191-constant-platform-second-gauges-are-invisible-to-fourth-ruling-quotient.md)。

R191 的双常值平台空间对 ruling 商不可见。本稿研究相邻但不同的情形：f 在一个开区间上常值，g 在其中变化。w 的支撑放在这个区间，仍不改变 hook 第四 period；再付三个 g 交叉矩即可保持完整第三 range。准确计算表明，这一空间的 ruling 商像一般不为零。

## 1. 同一固定数据与准确响应

保持 R184 的固定几何、同目标度量、同第一圆与 M=0，以及已经支付的二、三阶完整 range。使用同一个右 collar 和全局 s 起点。令

$$
z=\xi+\omega,\quad u=h/z,\quad e=h\xi+d,\quad
d=h\omega-k,\quad Q=1+e^2,\quad
\gamma=h_s,\quad \delta=d_s.
$$

取 $J\Subset I$，仅要求

$$
f|_J=C,\qquad w\in C_c^\infty(J),\qquad
\mathbf m(g,w)=0.
\tag{1}
$$

常值 C 可以非零；对 g 不作常值假设。自动有 $\mathbf m(f,w)=0$，所以这是一族合法的第三 range 定义域。

记

$$
\mathcal E_s(a,b)=\int(Y_a)_u\cdot(Y_b)_u\,du
=\frac1{4h}\int\{Q a''b''+2h^2a'b'\}\,d\xi,
\tag{2}
$$

并令

$$
\mathcal S_s(q)=\int(Y_q)_u\cdot(Z_B(q,q))_u\,du.
\tag{3}
$$

$Z_B(q,q)$ 在 (3) 中是同右锚、同全局零初值的真实 canonical 恢复。单独的 q 不必已付左 collar；(3) 仍有定义，因为 $Y_q$ 紧支撑，而其完整尾必须保留。

以 $D_w$ 表示对 profile 的准确方向导数：

$$
D_w\mathcal S_s(g)
=\left.\frac d{d\varepsilon}\mathcal S_s(g+\varepsilon w)
\right|_{\varepsilon=0}.
$$

**第一结论。** 对全部实际 s、相位 $\theta$，零初值 canonical 约定下准确有

$$
\boxed{
\mathcal B_\theta(w)
=-2\sin^2\theta\,D_w\mathcal S_s(g).
}
\tag{4}
$$

任何其他合法共同入齐次只在 (4) 两侧之差增加 $\mathcal W$ 项，所以同式在 ruling 商中与该约定无关。本文随后给出保留全部原历史的有限表示，并证明存在满足 (1) 而 (4) 不属于 $\mathcal W$ 的真实光滑 R183 圆及 w。

## 2. f 常值时的交叉恢复：保留尾而分离一个二次生成元

写

$$
\mathscr R_s(a;b,c)
=\int(Y_a)_u\cdot(Z_B(b,c))_u\,du.
$$

R191 已给 $\mathscr R_s(w;f,f)=0$。还需计算涉及 f、g 的混合项，不能因 $f'=0$ 而删除物理非零值 $Y_f=C uB$。

定义真实累计的二次多项式

$$
t(s,\xi)=-\int_{s_0}^s\frac{k(\tau)}{4h(\tau)}
\left(1+(h(\tau)\xi+d(\tau))^2\right)\,d\tau.
\tag{5}
$$

它使用同一个全局起点；不是逐几何段重置。令

$$
\mathscr D_t b=t b'-t'b.
$$

在 J 上，对任意静态 b，R56/R73 的原式给

$$
r_s(f,b)=
C\left(\frac{ke}{2}b-\frac{kQ}{4h}b'\right)
+K_0P_{fb}-\lambda_c(P_{fb})_s,
\tag{6}
$$

其中 $P_{fb}$ 在 J 内对 $\xi$ 为常数，仍是平台右方所有 profile 的真实尾。相应 $\eta_{fb}=-(P_{fb})_s/2$。由于

$$
\partial_s t=-\frac{kQ}{4h},\qquad
\partial_s t'=-\frac{ke}{2},
$$

(6) 积分后在 J 上可写

$$
W_{fb}=C\mathscr D_t b+\text{一个真实的 $\xi$ 二次多项式}.
\tag{7}
$$

R191 的恢复相消表明，后一个多项式连同 $P_{fb}$、$(P_{fb})_s$ 产生物理 u 仿射尾场。它与 $Y_w$ 的 ruling 配对准确为零。正常分量 $\rho N$ 与任何 $(Y_a)_u$ 也逐点正交。因此

$$
\mathscr R_s(w;f,g)=-C\mathcal E_s(w,\mathscr D_tg).
\tag{8}
$$

对 $b=w$，$T_\xi(f,w)$ 在整个 I 恒零，所以 $P_{fw}=0$，其余配对及累计历史真紧支撑于 J；没有左尾。于是

$$
\mathscr R_s(g;f,w)=-C\mathcal E_s(g,\mathscr D_tw),\qquad
\mathscr R_s(f;f,w)=0.
\tag{9}
$$

另一交叉恢复 $Z_B(g,w)$ 的右尾是否局部，需要用到 (1)。其三个正尾的左值正是 $\mathbf m(g,w)$，因此三矩全零使它们全紧支撑于 J。由原恢复式，$Z_B(g,w)$ 及全 s 历史也紧支撑在 J。所以

$$
\mathscr R_s(f;g,w)=0.
\tag{10}
$$

(10) 不是仅由导数支撑不交所得；若不付 (1) 的三个矩，左尾不能这样删去。

## 3. 混合相位项为何准确被三矩消掉

对任意二次以下多项式 t，令

$$
\Pi_t(\xi)=Q t'-Q't=b_0+b_1\xi+b_2\xi^2.
$$

三次最高项抵消。利用 $t'''=0$ 以及紧支撑 w 的真实端项，直接分部积分得

$$
\begin{split}
&\mathcal E_s(w,\mathscr D_tg)
+\mathcal E_s(g,\mathscr D_tw)\\
&\quad=\frac1{4h}\int
\left\{(Qt'-Q't)g''w''
+(Q't''-2h^2t')g'w'\right\}\,d\xi\\
&\quad=\boxed{\frac1{4h}
(b_0m_0(g,w)+b_1m_1(g,w)+b_2m_2(g,w))}.
\end{split}
\tag{11}
$$

最后一步使用 $Q't''-2h^2t'=2b_2$。因此 (1) 使 (8)、(9) 的和准确为零。

将 $\phi_\theta=\cos\theta f+\sin\theta g$ 展开到 R184 的完整表达式

$$
\mathcal B_\theta(w)=
2\mathscr R_s(w;f,f)
-2\mathscr R_s(w;\phi_\theta,\phi_\theta)
-4\mathscr R_s(\phi_\theta;\phi_\theta,w),
$$

用 (8)--(11) 消掉所有 f 混合项，剩下

$$
\mathcal B_\theta(w)
=-2\sin^2\theta
\{\mathscr R_s(w;g,g)+2\mathscr R_s(g;g,w)\},
$$

这正是 (4)。注意这里不是将三个 slot 全对称的完整第三算子冒作原恢复；方向导数只用于显示的标量 ruling 泛函。

## 4. 一个保留全部真实历史的有限像公式

R73 逐点八矩身份给

$$
\mathsf m(s)=\int_{s_0}^s M_{\rm raw}(\tau)\,d\tau,\qquad
W_{qq}(s,\xi)=\Phi_{\mathsf m(s)}(q,q)(\xi).
\tag{12}
$$

这是实际累计八维历史，而不是总 M=0 后把中间历史也设零。定义真实正尾

$$
J_q=h^2J_2^*(q,q)+2hdJ_1(q,q)+(d^2+1)J_0(q,q).
$$

从 R56 原式逐项代入得到

$$
\boxed{
\eta_{qq}=\frac1{16h^2}
\left[
-2h\gamma e\,q'^2+2\gamma Qq'q''
-(\gamma\xi+\delta)Qq''^2
-h\partial_sJ_q+\gamma J_q
\right].
}
\tag{13}
$$

可用以下三个中间量核 (13)：

$$
P_{qq}=\frac{J_q}{8h}+\frac e8q'^2,\qquad
b_{qq}=\frac h2q^2-\frac e2qq'+\frac Q{8h}q'^2,
$$

$$
T_{s\xi,qq}
=\frac12\left(\gamma q-\frac{e_s}2q'\right)
(hq'-eq'').
$$

完整恢复是

$$
Z_B(q,q)=\rho_{qq}N+
\frac{\eta_{qq}}{hz}(T+eB)-Y_{W_{qq}}.
$$

第一项与 $(Y_q)_u$ 正交。对第二项作一次真实分部积分，其所有 $q,q',q''$ 端值都由 q 的 collar 为零，给

$$
\boxed{
\mathcal S_s(q)=
\frac1{2h^2}\int Qq'''\eta_{qq}\,d\xi
-\mathcal E_s(q,\Phi_{\mathsf m(s)}(q,q)).
}
\tag{14}
$$

(12)--(14) 是 (4) 的准确可消费接口；包含完整 local eta 项和完整八维 history，未把其中任何一项假定为零。

还可给一个小的真实像上界。历史项的方向导数属于至多 24 个几何函数

$$
\mathbf w_i(s)\mathsf m_a(s),
\qquad i=0,1,2,\quad a=1,\ldots,8
$$

的 span。局部项中

$$
-h\partial_sJ_q+\gamma J_q
=-h^2\gamma J_2^*-2h^2\delta J_1
+\{\gamma(d^2+1)-2hd\delta\}J_0.
$$

展开 (13)、(14) 的 Q 后，其状态分子仅有 h、d 的总次数 0、2、4；除公共 $h^4$。所以局部方向导数属于至多 18 个几何函数

$$
\gamma h^{i-4}d^j,\qquad
\delta h^{i-4}d^j,\qquad
i,j\ge0,\ i+j\in\{0,2,4\}
$$

的 span。因此对固定几何、固定 g，

$$
\boxed{
\dim\operatorname{span}\{\mathcal B_\theta(w):
w\in C_c^\infty(J),\ \mathbf m(g,w)=0\}\le42
}
\tag{15}
$$

在固定相位成立，取 $\mathcal W$ 商后仍是上界。没有宣称这些函数独立、秩等于 42 或其像已覆盖原 joint 目标。无限维 w 空间可以经由有限个真实线性泛函作用，但其像不必为零。

## 5. 标准常段上的新一次项

现在仅为证明非零像，选一个含标准常状态 $(k,h,\omega)=(0,1,0)$ 开段的 R183 hook 几何。在该段取局部参数 $\sigma$，并保真实入历史。

此时 $\gamma=\delta=0$，故 $\eta_{qq}=0$。R73 给

$$
\mathcal R_0(q,q)
=-\frac18\{(1+x^2)q'^2+xJ(q,q)\},
$$

$$
J(q,q)=\int_x^r\{(1+y^2)q''(y)^2+2q'(y)^2\}\,dy.
$$

于是

$$
W_{qq}=W^{\rm in}_{qq}+\sigma\mathcal R_0(q,q),
$$

$$
\boxed{
\mathcal B_\theta(w)
=2\sin^2\theta
\left[
D_w\mathcal E_0(g,W^{\rm in}_{gg})
+\sigma D_w\mathcal C(g)
\right],
\quad
\mathcal C(q)=\mathcal E_0(q,\mathcal R_0(q,q)).
}
\tag{16}
$$

第一项是真实入历史，不置零；它在该段上不随 $\sigma$ 改变。$\mathcal W$ 在这个标准段只由常函数组成，因此只要 $D_w\mathcal C(g)\ne0$，(16) 必不属于 $\mathcal W$。

这只是一阶常段次数，不能抵消 R187/R193 已证明不可改变的二次最高项。

## 6. 完整 cubic 局部式与一个准确非零例

令 $p=q'$、$r=q''$、$Q=1+x^2$。从上式先准确求导，

$$
\mathcal R_0'=-\frac18(J+2Qpr-xQr^2),
$$

$$
\mathcal R_0''=\frac14\{(p-xr)^2-Q(p-xr)r'\}.
$$

代入 $\mathcal E_0(q,\mathcal R_0)=\frac14\int(Qr\mathcal R_0''+2p\mathcal R_0')$，再作真实分部积分，得

$$
\boxed{
\mathcal C(q)=\frac1{96}\int
\left[
4xq'^3+6Q(xq'-q)q''^2
+Q(1-x^2)q''^3-12q q'^2
\right]dx.
}
\tag{17}
$$

其中 $\int -q'J=\int qJ'=-\int q(Qq''^2+2q'^2)$，边界消去只用 q 自身的 collar；没有假设 J 的左值为零。这是完整右尾原式的局部身份。

取 R183 矩形的一条 g 上升边，f 在该边为非零常数。先使用 C7 step 原型，设其左端 c 满足 $c>1$，并在内侧写

$$
g(c+t)=a\,t^m+O(t^{m+1}),\qquad m=8,\quad a>0.
\tag{18}
$$

源码的 S 就有这个阶数；若共同物理区间需要，可在构造第一圆时作一次有限整体平移，使该边位于 c>1。平移保持原三矩及八包机制，不是改变已固定几何来适配 w。

令 $\mathscr E_g$ 是 (17) 关于 q 的 Euler 密度，所以 $D_w\mathcal C(g)=\int\mathscr E_g w$。最低阶仅来自 $Q(1-x^2)q''^3/96$，准确为

$$
\boxed{
\mathscr E_g(c+t)=
\frac{(1+c^2)(1-c^2)}{32}
[a\,m(m-1)]^2(2m-4)(2m-5)
t^{2m-6}+O(t^{2m-5}).
}
\tag{19}
$$

在 c>1、m=8 下，该系数非零。

三个矩泛函在 w 上的 adjoint 密度是

$$
L_0g=g'''',\quad
L_1g=xg''''+2g''',\quad
L_2g=x^2g''''+4xg'''.
$$

其任一非零常系数组合可写 $P g''''+2P'g'''$，P 为非零二次以下多项式。若 P 在 c 的首非零阶为 $j\le2$，则由 (18) 该组合首阶为

$$
\text{非零常数}\cdot t^{m-4+j}.
\tag{20}
$$

系数含 $m-3+2j$，所以 m=8 时不会再次抵消。(20) 的阶数仅为 4、5、6，而 (19) 为 10。因此在这条开边上，

$$
\mathscr E_g\notin\operatorname{span}\{L_0g,L_1g,L_2g\}.
$$

同一比较也证明三个 $L_i g$ 独立。有限维线性代数与测试函数分离立即给某个 $w\in C_c^\infty(J)$，满足

$$
\boxed{\mathbf m(g,w)=0,\qquad D_w\mathcal C(g)\ne0.}
\tag{21}
$$

这里不通过采样秩猜测独立性；若所有这样的 w 都杀 $\mathscr E_g$，四个连续线性泛函的核关系将迫相应密度有上述线性关系，与 (19)--(20) 矛盾。

## 7. 真实 C-infinity 圆与有符号 ruling 线

上述有限阶端点比较用于一个 C7 原型，不能原样声称 C-infinity 平端仍有 (18)。正确转移如下。

由四个测试泛函独立，可固定四个真正光滑、支撑在边内部紧子集的测试函数，使对应 $4\times4$ 矩阵可逆。对 R183 的 step 和三个左补矩形状作充分小的 C-infinity 平滑，并用新真实 A、B 准确重补三复矩；所有八包幅度保持。f 在这些固定测试函数的支撑上仍是原常值。

矩阵各项只用 g 至四阶导数及固定紧支撑积分，对 C4 收敛连续，所以平滑后仍可逆。用这四个固定测试函数的线性组合精确解三个零矩和一个非零 cubic 方向导数条件，得到真正光滑的 w。于是 (21) 对一个固定的、非退化且不可换基成不交的 C-infinity R183 圆成立。

现在整个几何和圆均已固定，再改变 w 的任意有限实倍。hook 公式给 $L_f(w)=0$，六交叉矩完整为零；第四 period 不变。由 (16)、(21)，其 ruling 商响应给一条真正的非零有符号直线。若要求种子，取 $w_\theta=\sin^2\theta\,w$，则相位光滑、周期且在 $0,\pi$ 为零，仍在非种子相位给上述非零方向。

R184 中的 gauge 平方项始终属于 $\mathcal W$，由同一单 profile 第三右逆真实支付；因此这不是只在零点的一阶线性化。有符号性来自 profile gauge 的正、负幅度，不是将实际几何路径成本半群误当向量空间。

## 8. 作用与未付范围

本稿回答了单边活动包的问题：在三个 g 矩约束下，其完整 ruling 商像有限，且存在明确 R183 光滑圆使该像非零。它和 R191 的双常平台零像严格不同。

我们没有证明任一给定 g 或任一无常段几何的该像都非零；(4)、(12)--(15) 给这些具体情形的准确接口。也没有证明 42 方向独立、全部 ruling 目标可付，或 R184 的整个 joint 方程已经可解。

对于含标准常段的上述非零例，新方向只改变 $\sigma$ 一次项。若其第一圆属于 R193 的全宽度排除类，原 $\sigma^2$ 障碍仍在，不能据本稿宣告第四延拓成功。对于 R189 无开常段几何，则需使用保留全部真实历史的 (14) 具体研究 ruling 像，不能套用 (16) 的常段斜率作为结论。
