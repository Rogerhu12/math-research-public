# R437 — 原独立 sigma 伴随因子的合法约去与 degree52 真正原函数

日期：2026-11-14。**状态：已证明。** 在 R431 的同一完整
$(W,Q_*)$ 联合中，R432 的指定 sigma 输入 $c$ 只进入 $Q_*$。
准确剥去它后，得到整来源
$\mathcal L\in\mathcal S_{52}\boxtimes\mathcal S_{7280}$，
其完整 $W$-core 仍是 $-\lambda=\lambda_\sigma$。
这个结论通过真正有界来源及 Amice 非零因子约消证明，不把零质量
sigma 当成可逆测度。

新的完整 $W$ 边际是明确的 Wronskian 来源 $J_{52}$，首项
$-8z^5/3$；它的移动负矩
$I_{-(p-6)}(J_{52})$ 对原固定 ray 上每个素数都是单位。
原 sigma 的 Amice 线性因子又给一个完整有限差分原函数。
原 rank-two 条件中央变成保留全部单位边界的差分行，而非新来源
中央已经为零的断言。R432 的真实隐藏非零域及其补域在下面保留。

## 1. 原坐标、实际除子和新的整来源

保持 R430、R431 的同一固定 ray，包括 $\pi_0\equiv2\bmod13$，
$p>19$、原周期 $\Omega$、$b=17$。写
$$
\lambda=-\bar\pi_0^{-1},\qquad
\lambda_\sigma=\bar\pi_0^{-1}=-\lambda,\qquad
\kappa=p/\bar\pi_0^2,\quad d=p-1.
$$
原小核及正交输出为
$$
\mathcal K(y,v)=G_{16}(y)\sigma(y-v)\sigma(y+v)\mathcal R(y,v),
$$
$$
W=Y+X,\quad Q_*=9Y-17X,\qquad
Y=(17W+Q_*)/26,\quad X=(9W-Q_*)/26.
\tag{1}
$$
这里 $\mathcal R$ 是 R424、R435 的同一个完整整联合。
用 $(w,q)$ 表示 $(W,Q_*)$ 的生成函数变量，则
$$
\widetilde{\mathcal K}(w,q)=\mathcal K(w+9q,w-17q).
$$
因为 $y-v=26q$，真实全函数因式为
$$
\boxed{\widetilde{\mathcal K}(w,q)=\sigma(26q)\mathcal L(w,q),}
\tag{2}
$$
其中
$$
\boxed{\begin{aligned}
\mathcal L(w,q)=\frac1{4\delta}\,
&\sigma(2w+18q)\sigma(2\delta w+18\delta q)
 \sigma(2w-8q)\\
&{}\cdot\mathcal R(w+9q,w-17q).
\end{aligned}}
\tag{3}
$$
(3) 是明确的原整测度卷积，分母 $4\delta$ 为单位，
所以它给有界整联合。这里没有在 log 级数中逐项除以 $q$。

它的完整 degree 恰为
$$
\boxed{\mathcal L\in\mathcal S_{52}\boxtimes\mathcal S_{7280}.}
\tag{4}
$$
第一轴 degree 是 $4+12+4+16+16=52$；
第二轴是 $18^2+3\cdot18^2+8^2+16(9^2+17^2)=7280$。
交叉项为
$$
2\cdot18+(2\delta)\overline{18\delta}+2(-8)
                 +16\cdot9-16\cdot17
=36+108-16+144-272=0.
$$
这里使用同一 CM 极化的范数配对；系数均为显示的整数或原 CM
整数。三个 sigma 的各轴系数都是偶格倍数，另两个 degree16
因子也没有残余半特征，所以无平坦 twist。
原 $\widetilde{\mathcal K}$ 的第二 degree $7956$ 减去
$N(26)=676$ 同样给 $7280$。

令 $\nu_{\mathcal L}$ 的两个输出记为 $(W,Q^\circ)$，
另取原独立 sigma 输入 $c$。完整测度身份是
$$
\boxed{\nu_{\widetilde{\mathcal K}}
=(W,Q^\circ+26c)_*
                  (\nu_{\mathcal L}(W,Q^\circ)\otimes\nu_\sigma(c)).}
\tag{5}
$$
由 (1)，它的原物理输出准确为
$$
\boxed{Y=c+(17W+Q^\circ)/26,\qquad
       X=-c+(9W-Q^\circ)/26.}
\tag{6}
$$
这就是 R432 中的同一个指定 $c$，不是另接一个具有相同边际的输入。

## 2. 只在 W 方向合法约去独立 sigma 因子

R431 已付同一来源的完整核
$$
\nu_{\widetilde{\mathcal K}}|_{W\in p}
=\lambda_\sigma[\kappa,1]_*
                            \nu_{\widetilde{\mathcal K}}.
\tag{7}
$$
在 (5) 中，第二轴的独立卷积既不改变 $W$，也与
$[\kappa,1]_*$ 交换。因此 (7) 给
$$
[26]_*\nu_\sigma *_Q
 \left\{\nu_{\mathcal L}|_{W\in p}
          -\lambda_\sigma[\kappa,1]_*\nu_{\mathcal L}\right\}=0.
$$
所有括号内对象是已经由 (3) 支付的有界整测度。
原 Amice 环 $\mathcal O[[T_W,T_Q]]$ 是整环，且
$\sigma(26\Omega\log(1+T_Q))$ 是非零元。
乘法单射和 Amice 单射性允许准确约消，得到
$$
\boxed{\nu_{\mathcal L}|_{W\in p^N}
=\lambda_\sigma^N[\kappa^N,1]_*\nu_{\mathcal L}
\qquad(N\ge0).}
\tag{8}
$$
在 theta 来源层，这也等价于
$(K_{52}\otimes I)\mathcal L=-\mathcal L$：
第一轴 division trace 与纯第二轴因子 $\sigma(26q)$ 相交换，
而 (2) 的同一非零因子可以全函数约消。

(8) 保全部 $Q^\circ$ 测试。给任何连续 $h(c)$，将 (5) 的
独立 sigma 输入改为 $h(c)\nu_\sigma(c)$，同样仍有 $W$-core
$\lambda_\sigma$。尤其可以保留 $c$ 单位或任何指定的 $c$ 隐藏域。

这里没有给 $\mathcal L$ 的 $Q^\circ$ 核赋值。
R431 对 $\widetilde{\mathcal K}$ 的第二轴 core 不能用上述方式
约去 sigma，因为它与**同一轴**的卷积一般不交换。

## 3. 完整 W 边际的 Wronskian 与确切多项式

沿 R424 的同一个记号，设 $X=x^3$，
$$
f_b(x)=x^7-\frac{4b}7x^4+\frac{16b^2}7x,\qquad
g_b(x)=x^9-30bx^6-144b^2x^3-32b^3,
$$
$$
F_{18}=\sigma^{18}f_b(x),\qquad G_{18}=\sigma^{18}g_b(x).
\tag{9}
$$
原实际小核是
$$
\mathcal K(y,v)=-\frac23G_{16}(y)
                 \{F_{18}(y)G_{18}(v)-G_{18}(y)F_{18}(v)\}.
$$
在 (2) 对 $q$ 求一阶导数再取 $q=0$：
原 sigma 首导数为一，$y$、$v$ 的系数差为 $9-(-17)=26$，
且对角上的交替积为零。因此完整第一边际为
$$
\boxed{J_{52}(w):=\mathcal L(w,0)
=-\frac23G_{16}(w)
       \{F_{18}'(w)G_{18}(w)-G_{18}'(w)F_{18}(w)\}.}
\tag{10}
$$
导数都是对原 sigma 自身变量求导；没有加入一个 $\Omega$。
该 $\Omega$ 只在之后的测度矩中出现。

令
$$
V_b(X)=7X^4+88bX^3+2112b^2X^2-2816b^3X+256b^4.
$$
直接展开 (9) 的原有理多项式给完整恒等式
$$
\boxed{f_b'g_b-g_b'f_b=-\frac27(X+b)V_b(X).}
\tag{11}
$$
使用 $x'=2y$、$y^2=x^3+b$ 以及
$G_{16}=\sigma^{16}x(X+b)(X-8b)$，(10) 变成
$$
\boxed{J_{52}
=\frac8{21}\,y\,\sigma^{52}x(X+b)^2(X-8b)V_b(X).}
\tag{12}
$$
(11) 是固定的一条有限多项式身份；比较 $X^0,\ldots,X^5$ 六个系数即可直接
核定，不依赖取样值或目标素数扫描。

从 $G_{16}=z^2+\cdots$、$F_{18}=z^4+\cdots$、
$G_{18}=1+\cdots$，或者从 (12) 的 $y=-z^{-3}+\cdots$，得到
$$
\boxed{J_{52}(z)=-\frac83z^5+O(z^{11}).}
\tag{13}
$$
所以 $J_{52}\ne0$，质量为零，原 $\mu_6$ 权为五。
由 (8) 取完整第一边际，其实际原测度仍满足
$$
\boxed{\nu_{J_{52}}|_p
=\lambda_\sigma[\kappa]_*\nu_{J_{52}}.}
\tag{14}
$$

## 4. 一个无需猜测的移动负五型单位矩

(13) 给同一个原周期中的确切正矩
$$
\mu_5(J_{52})=\int W^5d\nu_{J_{52}}(W)
=5!\left(-\frac83\right)\Omega^5=-320\Omega^5.
\tag{15}
$$
它对当前全部 $p>19$ 都是单位。由 (14)，单位部分的五次矩是
$$
\int_{\mathbf Z_p^\times}W^5d\nu_{J_{52}}
=(1-\lambda_\sigma\kappa^5)\mu_5(J_{52}).
$$
在单位上 $W^{-(p-6)}\equiv W^5\pmod p$，故完整原负矩满足
$$
\boxed{
I_{-(p-6)}(J_{52})
\equiv-320\Omega^5\pmod p,\qquad
I_{-(p-6)}(J_{52})\in\mathcal O^\times.}
\tag{16}
$$
负指数与原 CM 权相配，因为 $p\equiv1\bmod6$ 给
$-(p-6)\equiv5\bmod6$。
这里使用随 $p$ 改变的指定负矩，没有声称固定
$I_{-1}(J_{52})$ 或某个 rank-two 中央导数已非零。

## 5. R432 的原非零域在剩余来源中的准确位置

为保全部原输入，使用 R432 的同一平衡表示
$$
G_{16}(y)=\frac{\delta^{2m}}4\sigma(q_my)^2\mathcal B_m(y),
\qquad q_m=2\delta^{-m},\quad
\mathcal B_m=\Theta(2\cdot)\mathcal E_m^2,\quad M=2m+1.
$$
在 (3) 的剩余来源中，保原 $\mathcal R$ 输出 $(r_0,s_0)$、
全部 Theta 原 sigma 对的加权输出 $\tau$，以及三个原 sigma
输入 $a,b,e$。完整输出准确是
$$
\boxed{\begin{aligned}
W&=r_0+s_0+\tau+q_m(a+b)+2e,\\
Q^\circ&=9r_0-17s_0+9\tau+9q_m(a+b)-8e.
\end{aligned}}
\tag{17}
$$
底层系数仍为 $\delta^{2m}/4$，全部 Theta 二次权原样保留。
与独立 $c$ 按 (5) 相加后，(6) 恰还原 R432 的原 $Y,X$。

取 R432 已付的 $n\in4\mathbf Z_{\ge1}$、$r\ge n$，
在这一**指定卷积表示**中保真实域
$$
\boxed{\mathscr D_{m;n,r}
=\{r_0,s_0,a,b,e\in p^n,\quad
               \text{全部 }2M\text{ 个 Theta sigma 输入}\in p^r\}.}
\tag{18}
$$
令其完整剩余输出测度为 $\ell_{m;n,r}$。直接由 (17)，
$$
\operatorname{supp}\ell_{m;n,r}
\subset p^n\mathbf Z_p\times p^n\mathbf Z_p.
\tag{19}
$$
与独立的 $\nu_\sigma^\times(c)$ 按 (6) 相加后，正是 R432
的真实隐藏域，不更换联合。其完整第一边际是
$-2\nu^{\mathrm{bal}}_{m;n,r}/3$。因此该篇所选的 $m,n,r$ 给
$$
\boxed{
\int\!\!\int d\log_p
 \left\langle c+\frac{17W+Q^\circ}{26}\right\rangle
 d\ell_{m;n,r}(W,Q^\circ)d\nu_\sigma^\times(c)
=-\frac23(J^{\mathrm{bal}}_{m;n,r})'(0)\ne0.}
\tag{20}
$$
这里输出单位由 (19) 自动成立。
原全输出满足 $W\in p^n$、$Q_*=Q^\circ+26c$ 为单位；
完整物理 $Y,X$ 也为单位。独立单位 $c$ 没有被删掉。

在全部剩余输入同深的特殊情形 $r=n$，完整 core 可以逐因子计算。
R435 给原 $\mathcal R$ 双轴标量 $\lambda^{2n}$；
三个 sigma 给 $\lambda_\sigma^{3n}$；
全部 Theta 原对及二次权给
$\lambda_\sigma^{2Mn}\kappa^{2Mn}$。
各参数全部缩放 $\kappa^n$ 后，(2) 的平衡身份仍是原 $\mathcal L$。
所以准确有
$$
\boxed{\ell_{m;n,n}
=\lambda_\sigma^{(5+2M)n}\kappa^{2Mn}
                  [\kappa^n,\kappa^n]_*\nu_{\mathcal L}.}
\tag{21}
$$
这里使用 $\lambda^{2n}=\lambda_\sigma^{2n}$。
本篇没有从 (20) 的两深度非零推断 (21) 加上单位 $c$ 后的
第一中央一定非零，也没有把 (21) 认成整个双输出深度限制。

### 5.1 保留完整 W 深输出域的真实补集

设 $\Lambda_m$ 是 (17) 中的原带权输入测度，
$\mathscr W_n=\{W\in p^n\}$ 是其完整输出条件。由 (18)、(19)，
$\mathscr D_{m;n,r}\subset\mathscr W_n$，故准确有
$$
\nu_{\mathcal L}|_{W\in p^n}
=\ell_{m;n,r}+
 (W,Q^\circ)_*\bigl(\mathbf1_{\mathscr W_n\setminus\mathscr D_{m;n,r}}
                                      \Lambda_m\bigr).
\tag{22}
$$
左侧可使用 (8)；右侧第二项仍是真实补域，含所有没有同时满足
各个隐藏条件的原输入。全 $W$-core 不会把它删除。
也可在左侧另限 $Q^\circ\in p^n$，相应把补集换成完整双输出
深域中的补集；(19) 只是包含关系，不是两个事件相等。

## 6. 原 sigma 的整单位部分与纯 Q 有限差分

第二轴的原 sigma Amice 变换为
$$
A_{26}(T)=\sigma(26\Omega\log(1+T))\in\mathcal O[[T]].
$$
其常数为零，一次系数为 $26\Omega$。而
$((1+T)^{26}-1)/T$ 的常数 $26$ 是单位。
因此准确有
$$
\boxed{A_{26}(T)
=\Omega\bigl((1+T)^{26}-1\bigr)U_{26}(T),\qquad
U_{26}(T)\in\mathcal O[[T]],\quad U_{26}(0)=1.}
\tag{23}
$$
这给一个质量一的整有界测度 $\nu_{U_{26}}$，且它有整有界卷积逆：
幂级数逆逐项递推保持整系数。
这里只除 $T$ 和一个常数为单位的幂级数，没有除
$\log(1+T)$ 的非整展开。

定义完整有界联合
$$
\nu_{\mathcal P}=\nu_{\mathcal L}*_Q\nu_{U_{26}}.
\tag{24}
$$
由 (23)，在原 $(W,Q_*)$ 坐标中，
$$
\boxed{\nu_{\widetilde{\mathcal K}}
=\Omega\{\tau_{(0,26),*}\nu_{\mathcal P}-\nu_{\mathcal P}\}.}
\tag{25}
$$
$\tau_{(0,26)}$ 表示只在第二输出加二十六。
它在原物理坐标 (1) 中正是
$$
(Y,X)\longmapsto(Y+1,X-1).
\tag{26}
$$
所以 (25) 是一个完整、明确的有限差分原函数，不是仅在若干
Taylor 矩上的差分拟合。

第二轴独立卷积与 $W$ 限制及 $W$ 缩放交换，所以
$$
\boxed{\nu_{\mathcal P}|_{W\in p^N}
=\lambda_\sigma^N[\kappa^N,1]_*\nu_{\mathcal P},\qquad
W_*\nu_{\mathcal P}=\nu_{J_{52}}.}
\tag{27}
$$
第二式使用 $U_{26}$ 质量一。因此 (16) 的单位负矩在这个实际
有限差分原函数的完整第一边际中也保留。

## 7. 原完整条件中央变成什么差分行

把 $\nu_{\mathcal P}$ 按 (1) 的逆坐标式推回物理 $(Y,X)$，记为
$\mu_{\mathcal P}$。对任意连续完整测试 $f(Y,X)$，(25)、(26) 给
$$
\boxed{\int f\,d\nu_{\mathcal K}
=\Omega\int\{f(Y+1,X-1)-f(Y,X)\}\,d\mu_{\mathcal P}.}
\tag{28}
$$
尤其令
$$
k_u(Y)=\mathbf1_{Y\in\mathbf Z_p^\times}
                       \langle Y\rangle^{du},\qquad
\ell(Y)=\mathbf1_{Y\in\mathbf Z_p^\times}d\log_p\langle Y\rangle.
$$
R430 的同一个完整 principal 返回准确成为
$$
\boxed{\begin{aligned}
\Omega\int\{k_u(Y+1)h(X-1)-k_u(Y)h(X)\}\,d\mu_{\mathcal P}
=-\frac23J_S(u)\int h\,d\nu_{G_{18}}.
\end{aligned}}
\tag{29}
$$
对原中央求导，
$$
\boxed{
\Omega\int\{\ell(Y+1)h(X-1)-\ell(Y)h(X)\}\,d\mu_{\mathcal P}
=-\frac23J'_S(0)\int h\,d\nu_{G_{18}}.}
\tag{30}
$$
这里 $h$ 是任意连续测试，不对它作未付的 Taylor 展开。
若原 $J'_S(0)=0$，则准确已知的是 (30) 的**差分行**为零；
不能把其两个项、$\mathcal L$ 的中央或 $J_{52}$ 的负矩分别置零。
$k_u(Y+1)$ 的单位条件也保留原样，不能改成 $Y$ 为单位后省掉
$Y\equiv-1$ 或 $Y\equiv0$ 的真实 carry。

(24) 的测试转置同样必须保两个物理输出：
$$
\int f(Y,X)\,d\mu_{\mathcal P}
=\int\!\!\int
 f(Y+t/26,X-t/26)\,d\nu_{U_{26}}(t)\,d\mu_{\mathcal L}(Y,X).
\tag{31}
$$
所以它不是 R430 的纯第二输出反卷积，不能把 (31) 对
$\ell(Y)h(X)$ 的作用简写成只修改 $h$。这一完整混合转置是本篇
保留的原算术中央与新原函数之间的关系。

## 依赖与已付范围

- [R431：同一完整 degree52 总和 core 与正交坐标](R431-original-degree52-full-core-and-fixed-thirteen-ray.md)。
- [R424：原 Bezout 核、两条 degree18 来源及其固定多项式](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。
- [R430：原整小核和全部第二输出条件中央](R430-original-integral-second-output-division-and-degree18-mixed-rows.md)。
- [R432：同一平衡来源的实际隐藏非零管及其真实补支](R432-original-balanced-two-depth-source-and-three-actual-hadamard-tubes.md)。
- [R435：原内层双轴完整 core 与真实深度限制](R435-original-degree16-square-core-and-exact-two-axis-depth-transfer.md)。

本篇新增的是原残余来源、真正保完整伴随的 $W$-core、明确
Wronskian 边际及其单位负矩，以及原算术条件中央的准确有限差分行。
完整 $Q^\circ$ 核、隐藏深条件到全输出深条件的识别、(22) 的补域
以及 (30) 差分行到实际非零管的零传播仍未被预支。

