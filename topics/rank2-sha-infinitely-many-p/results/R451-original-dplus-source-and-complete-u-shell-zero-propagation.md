# R451 — 原 D 正特征来源与完整 U 环带零传播

日期：2026-11-14。**状态：已证明。**

在 R446 的三个真实残余状态中取一条实际 $D$ 正特征线，
其完整第一 principal 行仍是原 $\mathcal K_0$ 的行。
保独立 sigma 后，该行在 $U$ 轴具有标量完整核心。因此原
$J'_S(0)=0$ 确实传入每个 $U$ 深域和每个 $U$ 环带，并保任意
完整第二输出测试。

同一个新来源在 R441 的真实同深管中仍严格非零；现在对每个
$n\ge1$ 都有精确赋值 $5n$，不必只取偶数深度。
该管位于 $U$ 单位域内，尚须排除的补域也准确缩到同一个
$U$ 单位域内部。这里没有删除它或把任意 $U$ 测试免费赋零。

## 1. 实际 D 正特征来源

固定 R439、R445 的同一原普通 ray、周期和
$$
\lambda=-\bar\pi_0^{-1},\quad
\lambda_\sigma=-\lambda,\quad
\kappa=p/\bar\pi_0^2,\quad
\eta=\eta_{5,p}\in\{1,-1\}.
\tag{1}
$$
所有源都是原 $b=17$ 上的实际整来源。定义
$$
\boxed{
\mathcal L_+=\mathcal L_0+
            \frac{\mathcal L_1-\mathcal L_R}{2},\qquad
\mathcal K_+=\mathcal K_0+
            \frac{\mathcal K_1-\mathcal K_R}{2}.}
\tag{2}
$$
其外部关系仍是 $\mathcal K_+=\sigma(y-v)\mathcal L_+$。
R446 已付三个残余态的整性，故
$$
\mathcal L_+\in\mathcal S_{52}\otimes\mathcal S_{7280},
\qquad
\mathcal K_+\in\mathcal S_{34}\otimes\mathcal S_{18}
$$
都给整有界测度。

由 R446 的完整实际作用
$$
D\mathcal L_0=\mathcal L_1,\quad
D\mathcal L_1=\mathcal L_0,\quad
D\mathcal L_R=-\mathcal L_0+\mathcal L_1+\mathcal L_R
$$
直接得到
$$
\boxed{D\mathcal L_+=\mathcal L_+,\qquad
K_W\mathcal L_+=-\mathcal L_+,\qquad
K_Q\mathcal L_+=\eta\mathcal L_+.}
\tag{3}
$$
测度限制时各乘公共标量 $\lambda$。
这是真正的同一来源返回，不再需要偶次作用消去两态交换。

另一方面，$\mathcal K_R=R_Y\mathcal K_1$，所以
$\mathcal K_1-\mathcal K_R$ 对第一输入反射为奇。
对任意连续 $h(X)$ 和原 principal 权参数，整条函数满足
$$
\boxed{
\int\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}
                    h(X)\,d\nu_{\mathcal K_+}
=-\frac23J_S(u)\int h\,d\nu_{G_{18}}.}
\tag{4}
$$
右侧是 R430 的同一个 $S,G_{18}$，没有新增算术零假设。

## 2. 保独立 sigma 的完整 U 核心

保留原独立 sigma 输入 $c$，令
$$
\rho_+=\nu_{\mathcal L_+}(W,Q)\otimes\nu_\sigma(c),
\qquad A=Q+26c,\qquad U=Q-280c.
\tag{5}
$$
物理输出仍是
$$
Y=(17W+A)/26,\qquad X=(9W-A)/26.
\tag{6}
$$
相应三变量整 theta 源记为 $\Phi_+$。
R445 的完整格及全深比较，结合 R448 的保 $U$ 几何实现，给
$$
K_A\Phi_+=R_Y\Phi_+,\qquad
\boxed{K_U\Phi_+=-\eta R_Y\Phi_+.}
\tag{7}
$$
第二式也直接来自
$K_WK_AK_U\Phi_+=\eta\Phi_+$、
$K_W=-1$、$K_A^2=1$ 和 (3)。
这里 $R_Y$ 在保 $U$ 的完整物理坐标中只反射 $Y$，固定 $X,U$。

定义真正的条件测度
$$
\mathcal G_+(u;dX,dU)
=(X,U)_*\!
 \left(\mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}
                                    \nu_{\Phi_+}\right).
\tag{8}
$$
第一 principal 测试对 $Y\mapsto-Y$ 固定。
因为 (7) 的反射保持另外两个输出，得到完整测度身份
$$
\boxed{
\mathcal G_+(u)|_{U\in p}
=-\eta\lambda[1,\kappa]_*\mathcal G_+(u).}
\tag{9}
$$
这保任意连续 $h(X,U)$，不只是遗忘 $U$ 后的边际。
原测度整有界，权函数和中央导数也有界，因此可在中央求导。

记 $q=-\eta\lambda$。由 (4)，遗忘 $U$ 后准确为
$$
\boxed{(X)_*\mathcal G_+(u)
       =-\frac23J_S(u)\nu_{G_{18}}.}
\tag{10}
$$

## 3. 原中央向全部 U 深域和环带传播

迭代 (9)，对每个 $r\ge0$ 得
$$
\mathcal G_+(u)|_{U\in p^r}
=q^r[1,\kappa^r]_*\mathcal G_+(u).
\tag{11}
$$
缩放 $U$ 不改变 $X$，所以对任意完整 $h(X)$，
$$
\boxed{
\int_{\{U\in p^r\}}
 \mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}h(X)\,d\nu_{\Phi_+}
=-\frac23q^rJ_S(u)\int h\,d\nu_{G_{18}}.}
\tag{12}
$$
相邻深域相减，准确得到每个真实环带
$$
\boxed{
\int_{\{v_p(U)=r\}}
 \mathbf1_{Y\ {\rm unit}}\langle Y\rangle^{du}h(X)\,d\nu_{\Phi_+}
=-\frac23q^r(1+\eta\lambda)J_S(u)\int h\,d\nu_{G_{18}}.}
\tag{13}
$$
所有显示比例都是同一原 ray 上已付的单位。
因此若原 $J'_S(0)=0$，两式的中央导数对每个 $r$、
每个连续 $h(X)$ 都为零。特别，
$$
\boxed{
\int_{\{Y,U\ {\rm unit}\}}
 d\log\langle Y\rangle\,h(X)\,d\nu_{\Phi_+}=0
 \quad\text{若 }J'_S(0)=0.}
\tag{14}
$$

这个结论只对所示 $U$ 原点深域、环带和不依赖 $U$ 的测试成立。
它没有推出任意 $h(X,U)$ 的中央为零，特别没有删除
$U-280X$ 的移动斜管条件。

取 R441 的同一测试 $h(X)=X^6$，由
$\int X^6d\nu_G=-22464b\Omega^6$，
$$
\boxed{
\int_{\{Y\ {\rm unit},\,v_p(U)=r\}}
 d\log\langle Y\rangle X^6\,d\nu_{\Phi_+}
=14976b\Omega^6q^r(1+\eta\lambda)J'_S(0).}
\tag{15}
$$
这与原算术中央准确差一个单位。

## 4. 同一个来源的真实非零管

写残余物理坐标为 $(Z,H)$：
$$
W=Z+H,\qquad Q=9Z-17H.
$$
加回独立 sigma 后，
$$
Y=Z+c,\qquad X=H-c,\qquad U=9Z-17H-280c.
\tag{16}
$$
对每个 $n\ge1$，取真实同深域
$$
\mathscr D_n=\{Z,H\in p^n\mathbf Z_p,\ c\in\mathbf Z_p^\times\}.
\tag{17}
$$
行列式 $-26$ 为单位，所以残余两输出同时深等价于 $W,Q$ 同时深。
由 (3)，
$$
\boxed{
\nu_{\mathcal L_+}|_{\{Z,H\in p^n\}}
=(-\eta)^n\lambda^{2n}[\kappa^n,\kappa^n]_*\nu_{\mathcal L_+}.}
\tag{18}
$$
这对所有 $n$ 成立。

定义同一个有界测度的解析函数
$$
\mathcal A_+(T)
=d\int\log\langle c+TZ\rangle\,(-c+TH)^6\,
 d\nu_{\mathcal L_+}(Z,H)\,d\nu_{\sigma,{\rm unit}}(c).
\tag{19}
$$
当 $T\in p\mathcal O$ 时，$c+TZ$ 是单位。
因此原真实管中央准确为
$$
\boxed{
C_n^+:=\int_{\mathscr D_n}
 d\log\langle Y\rangle X^6\,d\rho_+
=(-\eta)^n\lambda^{2n}\mathcal A_+(\kappa^n).}
\tag{20}
$$

## 5. 完整第五项、消失的 log c 项及全部尾项

R441、R446 的完整来源多项式给
$$
[\deg5]\mathcal L_0
=-\frac23(Z^5+Z^4H+Z^3H^2+Z^2H^3),
$$
$$
[\deg5](\mathcal L_1-\mathcal L_R)
=\frac2{21}ZH(Z+H)(5Z^2+H^2).
$$
所以
$$
\boxed{
[\deg5]\mathcal L_+
=-\frac23Z^5-\frac37Z^4H-\frac37Z^3H^2
 -\frac{13}{21}Z^2H^3+\frac1{21}ZH^4.}
\tag{21}
$$
更强，$\mathcal L_+(0,H)$ 整个函数为零。
R441 已付 $\mathcal L_0(0,H)=0$；
$\mathcal K_1-\mathcal K_R$ 的第一输入奇性则给它在 $Y=0$ 恒零，
消去共同非零 $\sigma(Y-H)$ 后仍得到
$(\mathcal L_1-\mathcal L_R)(0,H)=0$。
所以 (19) 中来自 $\log\langle c\rangle$ 的整条项严格消失，
不是仅第五系数为零。

写
$$
I_{1,\sigma}
=\int_{\mathbf Z_p^\times}c\,d\nu_\sigma(c)
=\Omega(1-\lambda_\sigma\kappa)\in\mathcal O^\times.
\tag{22}
$$
将 (21) 的系数按 $Z^{5-j}H^j$ 记为
$$
(\ell_0,\ldots,\ell_5)
=\left(-\frac23,-\frac37,-\frac37,-\frac{13}{21},\frac1{21},0\right).
$$
从 $\log(1+TZ/c)$ 的真实 Taylor 展开取第五项，
$$
\begin{aligned}
[T^5]\mathcal A_+
 &=d\Omega^5I_{1,\sigma}
 \sum_{j=0}^4\frac{\binom6j}{5-j}(5-j)!\,j!\,\ell_j\\
 &=720d\Omega^5I_{1,\sigma}
             \sum_{j=0}^4\frac{\ell_j}{(6-j)(5-j)}\\
 &=\boxed{-\frac{800}{7}d\Omega^5I_{1,\sigma}}.
\end{aligned}
\tag{23}
$$
它在当前每个普通处是单位，原 $c$、周期、阶乘和 $d$ 全部保留。

整个 $\mathcal L_+$ 的同时 $\mu_6$ 型为 $5$，所以 (19)
只有次数 $k\equiv5\pmod6$。低于五次的矩全零，高于五次的首个
可能次数为十一。整有界测度及对数分母给完整高系数下界
$$
v_p([T^k]\mathcal A_+)\ge-\lfloor\log_p k\rfloor.
\tag{24}
$$
对 $p>19$、$n\ge1$ 和每个 $k\ge11$，
$kn-\lfloor\log_p k\rfloor>5n$。
结合 $v_p(\kappa)=1$ 和 (23)，全部高尾不能抵消首项：
$$
\boxed{v_p(C_n^+)=5n\qquad\text{对每个 }n\ge1.}
\tag{25}
$$
没有用数值采样或有限 Taylor 多项式代替全尾。

## 6. 同一个 U 单位域内的准确补域

在 (17) 上，$Y,X,U$ 都是单位：
$U\equiv-280c\pmod p$，而原 $p>19$ 已排 $2,5,7$。
同一个域还准确写成
$$
\boxed{
\mathscr D_n
=\{X\ {\rm unit},\ W\in p^n,\ U-280X\in p^n\}.}
\tag{26}
$$
因为
$U-280X=9Z-297H$，
它与 $W=Z+H$ 的行列式为 $-306$，仍为单位。
所以 (26) 是同一三输入域，不只是包含关系。

若原 $J'_S(0)=0$，(14)、(20)、(25) 给确切约束
$$
\boxed{
\int_{\{Y,U\ {\rm unit}\}\setminus\mathscr D_n}
 d\log\langle Y\rangle X^6\,d\rho_+
=-C_n^+,\qquad v_p(C_n^+)=5n.}
\tag{27}
$$
补域现在全部位于同一个 $U$ 单位域内部，但仍含 $W$ 外域、
斜管外域及其完整交叠。本篇尚未排除它们的准确抵消。

R448 的真实 $R_Y$ 把 (26) 送到
$$
\{X\ {\rm unit},\ V=X-Y\in p^n,\ U-280X\in p^n\}.
$$
反射保持 $X,U$ 和 principal 测试，却把来源换成
$R_Y\Phi_+$。要在同一个来源上分离两条管，仍须保这个来源变化；
不能只凭完整中央行相同删除它。

## 7. 本条新增接口

R446 的有限实际闭包中存在一个保原中央的 $D$ 正方向。
这把原算术失败真正传入独立 $U$ 的全部原点深域与环带；
同一来源的非零同深管和全部尾项同时保留，奇数深度也已合法。
后续仍须处理同一个 $U$ 单位域中的真实斜管和 $W/V$ 补域，
但不再需要未知 $\mathcal K_1$ 中央来处理 $U$ 非单位分支。

## 依赖

- [R441：原第六矩行及严格同深非零](R441-original-sixth-moment-row-and-uniform-same-depth-nonvanishing.md)。
- [R445：保原 sigma 的三轴完整核心](R445-original-sigma-retained-three-coordinate-core-and-four-state-carry.md)。
- [R446：实际三态及 D 作用](R446-original-three-state-quarter-closure-and-one-layer-full-carry.md)。
- [R448：保 U 的真实第一输入反射](R448-original-retained-companion-reflection-and-joint-principal-carry.md)。

