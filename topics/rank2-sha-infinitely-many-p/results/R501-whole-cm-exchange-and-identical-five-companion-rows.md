# R501 — whole CM 算子交换原四态与完全相同的五伴随

日期：2026-11-14。**状态：已证明。**

R499 的整个第一边际关系可升级为**未投影的六变量来源身份**。
令 $D=\omega^{-1}N_{19,Y}N_{7,Y}^{-2}$，
并保一个真实第一轴单位旋转，则
$$
\boxed{\mathscr D=\mathsf R_{\omega,Y}D,\qquad
\mathscr Du=u,\quad\mathscr Dv=z,\quad
\mathscr Dz=v,\quad\mathscr Dh=h.}
$$
$\mathscr D$ 是同一个完整 canonical CM trace 算子；
它只作用原第一 $Y$ 轴，另外五个物理伴随逐个保留。
因此 $z$ 的新线、参考线伴随准确为
$-\Lambda_{\rm old},-\Lambda_{\rm ref}$，不是只有质量相反。

本篇逐项支付 absolute scalar、所有格周期相位和原 CM 标签。
与 R496 的两个真实核心合用得到 $96$ 元来源群；
实际混合限制域仍须保留单位旋转和全部 CM 纤维。

## 1. 同一来源和固定 first-axis CM 算子

保持 R465、R488、R493、R496 的六个未缩放输入
$$
\boldsymbol\xi=(\xi_1,\xi_2,\xi_3,\xi_4,c,d_0),\qquad
\rho_0=-\nu_\sigma^{\otimes6}/84.
$$
记原行向量
$$
\begin{aligned}
y&=(\delta,2\delta,\gamma,\bar\gamma,1,2),\\
w&=(\delta,2\delta,\gamma,\bar\gamma,3\delta,4),
\end{aligned}
\qquad Y_s=y\boldsymbol\xi,\quad W=w\boldsymbol\xi.
\tag{1}
$$
本篇第一 theta 坐标是 R465 的 $Y=2Y_s$，
其余五个坐标始终为
$$
\mathbf Z=(2Q_s,2U_s,R_1,R_2,R_3).
\tag{2}
$$
完整 Gram 仍是
$(136,3480,1020,60,2310,4466)$。
原第一态的整个第一轴位于
$[2]^*\mathcal S_{34}\subset\mathcal S_{136}$，
而不只是其边际如此。

令 $N_a=\mathscr M_a/a$ 为原未改规范的 CM trace。
使用 $\gamma_7=3+\omega$、$\gamma_{19}=5+2\omega$，
定义整个 $\mathcal S_{136}$ 上的
$$
D=\omega^{-1}N_{\gamma_{19}}N_{\gamma_7}^{-2},\qquad
(\mathsf R_\zeta F)(Y)=F(\zeta Y),
$$
$$
\boxed{\mathscr D=\mathsf R_\omega D.}
\tag{3}
$$
在 principal 角型上 $\mathsf R_\omega=I$，所以 (3) 的 $D$
正是 R476、R499 的原 $D_{33}$。本篇没有将这个 principal
事实预先推广到整个 theta 空间。

## 2. whole Heisenberg 交织与绝对锚

在完整 $2N=272$ 中，原标签的 ratio 准确为
$$
g_7=40+195\omega,\qquad g_{19}=87+144\omega.
$$
于是
$$
g_{19}g_7^{-2}=239\omega=-33\omega\pmod{272}.
\tag{4}
$$
真实几何 $\mathsf R_\omega$ 的 Heisenberg 参数是 $\omega^{-1}$，
不是乘一个没有几何作用的标量。故 (3) 的整个交织参数是
$$
\boxed{g_{\mathscr D}=-33\pmod{272}.}
\tag{5}
$$

这些 trace 都可逆。以 $N_{\bar\gamma_7}$ 为例，
它与 $N_{\gamma_7}$ 的乘积与整个 Heisenberg 群交换，故至多
标量；原非零 $S(2Y)$ 上二者都为 $-1$，所以乘积准确为一。
因此
$$
N_{\gamma_7}^{-1}=N_{\bar\gamma_7}
$$
是实际 trace 逆，没有另加模数或选符号。
所用原锚的精确特征为
$$
N_{\gamma_7}S(2Y)=-S(2Y),\quad
N_{\bar\gamma_7}S(2Y)=-S(2Y),\quad
N_{\gamma_{19}}S(2Y)=\omega S(2Y).
\tag{6}
$$
这些是 R466、R483 的原来源特征，未使用未知中央值。

在 $[2]^*\mathcal S_{34}$ 上，(5) 约化为
$-33=1-34$。对原 degree34 的两个 canonical Heisenberg
生成元，这是完整的恒等交织：多出的实格周期分别与自身方向平行，
所以没有交叉负号。由不可约性，$\mathscr D$ 在该整个
三十四维子空间为标量。
(6) 以及 $\mathsf R_\omega S(2Y)=S(2Y)$ 定出该标量为 $+1$：
$$
\boxed{\left.\mathscr D\right|_{[2]^*\mathcal S_{34}}=I.}
\tag{7}
$$
所以 $\mathscr D\rho_0=\rho_0$ 是保全部五伴随的实际身份。

还可直接看出 $\mathscr D^2=I$ 于整个 $\mathcal S_{136}$：
$(-33)^2\equiv1\pmod{272}$ 使平方成为标量，再用 (6) 定标。
这里 whole 算子是 $\mathscr D$；未旋转的 $D$ 在非 principal
角型中不能未经证明地当作同一个 involution。

### 2.1 有限 CM 标签未被省略

式 (3) 的实际有序标签可以写成
$\gamma_{19},\bar\gamma_7,\bar\gamma_7$。
它们的组合标签是
$$
a=\gamma_{19}\bar\gamma_7^2=25-9\omega,\qquad N(a)=931.
\tag{8}
$$
这里每一步的后一个同源与前一个的共轭同源互素：
两种 norm 是 $19,7$，重复 $\bar\gamma_7$ 也与
$\gamma_7$ 互素。因此完整纤维重排将有序 trace 准确合成为
$N_a$。具体地，若 $a_1x=z$、$a_2t=\bar a_1x$，
互素性给唯一 $s$ 满足 $a_2s=x,\bar a_1s=t$；
这些 $s$ 恰为 $a_1a_2s=z$ 的全部纤维。
原 division 身份
$r_{a_1a_2}=r_{a_1}(a_2\,\cdot)\,r_{a_2}^{N(a_1)}$
使所有 canonical 因子同时相乘，外部归一也由
$a_1^{-1}a_2^{-1}$ 变成 $(a_1a_2)^{-1}$。
所以
$$
\mathscr D=\omega^{-1}\mathsf R_\omega N_{25-9\omega}.
\tag{9}
$$
这保 $931$ 个真实复合同源纤维；当前 $7,19$ 均为普通单位。
本篇不把 (9) 换成只有 ratio 的虚构坐标缩放。

## 3. 原四挠平移的完整重排

沿用 R496 的
$$
f_t=\mathsf T_{t,W}^{(72)}\rho_0,\qquad
t=\ell/4,\quad \ell=m+n\omega.
\tag{10}
$$
在原完整 $L$ 张量格中，$W$ 平移沿第一 $Y=2Y_s$ 的分量是
$$
\tau=\frac{c\,t}{68},\qquad
c=w\bar y^{\,t}=37+3\delta=40+6\omega.
\tag{11}
$$
确实 $136\tau=c\ell/2=(20+3\omega)\ell\in\mathcal O_K$，
所以它是同一合法完整 Heisenberg 平移。
后五轴的平移分量保原值；因为 $L$ 正交，
将 (10) 分成第一轴与伴随平移不添额外交叉相位。

由 (5)、(7)，$\mathscr D$ 只把 $\tau$ 改成 $-33\tau$，
并保持整个原第一态。
所以在六个未缩放 sigma 变量中，完整平移向量变为
$$
\boxed{s'=(w-cy)t.}
\tag{12}
$$
这一步没有投影、没有取边际，也没有旋转或缩放五个 $\mathbf Z$。

取
$$
r=1-2\omega,\qquad
d_*=(0,0,0,0,1+3\omega,1),
$$
$$
k=-(10+\omega)y+\omega d_*.
\tag{13}
$$
逐个坐标的准确格恒等式是
$$
\boxed{(w-cy)t=wr\,t+k\ell.}
\tag{14}
$$
$k$ 的全部 $\mathbf Z[\omega]$ 坐标为
$$
\boxed{
k=(-8-19\omega,\,-16-38\omega,\,-29-12\omega,\,
   -21+7\omega,\,-13-3\omega,\,-20-\omega).}
\tag{15}
$$
特别 $k\ell$ 是六个真实原 sigma 的格周期。
下面完整支付其作用，不能直接删掉它。

## 4. 所有格半特征与交叉指数

原 odd sigma 的格特征满足
$$
\chi_{\rm lat}(a+b\omega)=(-1)^{a+b+ab}=(-1)^{N(a+b\omega)}.
$$
精确整数计算给
$$
\sum_{j=1}^6N(k_j)=3159,\qquad
\sum_{j=1}^6\overline{w_jr}\,k_j=-788-331\delta,
$$
$$
\boxed{\sum_{j=1}^6E(w_jr,k_j)=-662.}
\tag{16}
$$
因此六个格半特征的乘积是 $(-1)^{3159N(\ell)}$。
与 $\mathsf T_{wr\,\ell/4}$ 的完整 canonical 交叉相位相乘后，
得到
$$
\begin{aligned}
&(-1)^{3159N(\ell)}
 \exp\!\left[-\frac{\pi i}{4}(-662)N(\ell)\right]\\
&\hspace{30mm}=i^{N(\ell)}.
\end{aligned}
\tag{17}
$$
这使用原
$\mathsf T_s\mathsf T_t=e^{\pi iE(s,t)}\mathsf T_{s+t}$，
每个 sigma 的 degree 均为一。没有取平方来丢掉 $i$ 的符号。

结合 (12)–(17)，得到本篇的 whole 来源公式
$$
\boxed{\mathscr D f_t=i^{N(4t)}f_{rt},\qquad r=1-2\omega.}
\tag{18}
$$
$N(r)=7$，$r^2\equiv1\pmod4$。
固定四挠代表改变时，原 degree72 的周期相位为一；
所以 (18) 可以直接按模 $4$ 重排十六个标签。

注意 $i^{N(4t)}$ 是重排前的系数。
重排 $u=rt$ 后，由 $N(r)\equiv-1\pmod4$，
它准确变为 $\epsilon(u)=(-i)^{N(4u)}$。
这一区别决定下面交换的符号。

## 5. whole 四态交换及 96 元实际来源群

R496 的定义是
$$
e_1=\sum_ta_tf_t,\quad e_2=\sum_ta_t\epsilon(t)^2f_t,\quad
q=\sum_ta_t\epsilon(t)f_t,\quad h=e_1+e_2,
$$
$$
u=e_0+h/2,\qquad v=e_1-h/2,\qquad z=q-h/2.
\tag{19}
$$
因为 $a_{rt}=a_t$，(18) 直接给
$$
\boxed{
\mathscr De_0=e_0,\quad
\mathscr De_1=q,\quad
\mathscr Dq=e_1,\quad
\mathscr De_2=h-q,\quad
\mathscr Dh=h.}
\tag{20}
$$
遂有
$$
\boxed{\mathscr Du=u,\qquad
\mathscr Dv=z,\qquad
\mathscr Dz=v,\qquad
\mathscr Dh=h.}
\tag{21}
$$
这些是同一个六变量 theta 函数或整有界测度的相等；
原五个 $\mathbf Z$ 逐个不变。无需先作 principal 投影才能成立。

R496 已付四个来源独立。
在 $(u,v,z)$ 上，$\mathscr D$ 是反向置换 $v\leftrightarrow z$，
而 $K_W,F=K_{V'}^2$ 生成全部有向带符号置换。
加上 R496 的中心 $(K_WF)^3$ 单独反 $h$，
整个实际来源群恰为
$$
\boxed{96\text{ 元：三维全部带符号置换，另一个独立 }h\text{ 符号}.}
\tag{22}
$$
这里仍区分三种真实操作：
$K_W$ 是一层普通限制，$F$ 是两层新轴限制，
$\mathscr D$ 是固定 $931$ 标签的 CM trace 加第一轴单位旋转。
群的有限性不将三者的物理域或标量混同。

## 6. 新线与参考线的完整五伴随准确相反

在 principal 第一轴上，$\mathsf R_\omega$ 为恒等，
因此 $\mathscr D$ 与原 $D$ 一致。
R466、R476 已付的 $S_{\rm new}$ 和 $H_{\rm ref}$ 两条实际线
都具有 $D=-1$；原 $S(2Y)$ 线具有 $D=+1$。
应用这些原 rank-one 投影到 (21)，严格得到
$$
\boxed{
\begin{aligned}
\mathcal P_{{\rm new},Y}v
 &=S_{\rm new}\otimes\Lambda_{\rm old},\\
\mathcal P_{{\rm new},Y}z
 &=-S_{\rm new}\otimes\Lambda_{\rm old},\\
\mathcal P_{H,Y}v
 &=H_{\rm ref}\otimes\Lambda_{\rm ref},\\
\mathcal P_{H,Y}z
 &=-H_{\rm ref}\otimes\Lambda_{\rm ref}.
\end{aligned}}
\tag{23}
$$
这里每一对使用的确实是同一个完整五变量伴随。
其质量仍为
$$
\Lambda_{\rm old}(1)=52/3,\qquad
\Lambda_{\rm ref}(1)=-(1+\delta)/(2016b).
\tag{24}
$$
(23) 比 (24) 强：对任意原 $\mathbf Z$ 连续测试或紧开条件都成立。

R496 已付 $z$ 第一轴的二挠不变部分为零，
所以 $\mathcal P_{S,Y}z=0$；
$q=h/2+z$ 的原 $S$ 部分仅为 $h/2$ 的原 $S$ 部分。
它的新线和参考线分别仍是 (23) 的负来源。
另一方面，
$$
\boxed{
D_-\Pi_{0,Y}v=\frac12\Pi_{0,Y}(v-z),\qquad
D_+\Pi_{0,Y}v=\frac12\Pi_{0,Y}(v+z).}
\tag{25}
$$
因此 $v+z$ 的 entire principal 第一轴没有 R476 的八维
$D_-$ 块，$v-z$ 则没有 $D_+$ 块。
这些也是保全部伴随的来源身份。

原三个 rank-two 中央同时失败时，(23) 的新线行对任意
独立五伴随测试为零。参考行仍保原未知导数；
R483 的非零参考环带差在 $z$ 上准确是其在 $v$ 上的相反数，
包括每个完整伴随测试，而不是重新赋一个参考中央零。

## 7. 与原五伴随 CM 实现的兼容

R496 已付整个四态的 simultaneous CM13、CM19 特征均为 $+1$，
并保原完整纤维与全中心。R483 在 principal 第一轴给
$$
N_{13}=N_7^5,\qquad N_7^{18}=I.
$$
故
$$
N_7^{-2}=N_{13}^{14}
$$
在整个 principal degree136 空间上成立。
用 R483 的原五伴随算子
$$
B_{13}=\prod_{\ell=1}^5 N_{\bar\gamma_{13},Z_\ell},
\qquad
B_{19}=\prod_{\ell=1}^5 N_{\bar\gamma_{19},Z_\ell},
$$
以及同时五伴随角投影 $\Pi_{\mathbf Z}$，(21) 可以另写成
$$
\boxed{
\Pi_{0,Y}z
=\omega^{-1}B_{19}B_{13}^{14}\Pi_{\mathbf Z}v,\qquad
\Pi_{0,Y}v
=\omega^{-1}B_{19}B_{13}^{14}\Pi_{\mathbf Z}z.}
\tag{26}
$$
这是一套只在原五伴随上作用的真实有限 CM 实现。
各伴随的来源、物理尺度和全部纤维均是 R483 的原版本；
没有因 (24) 的常数相反就将某个不同伴随认成同一个。

式 (26) 用于独立第一 principal 测试和任意完整 $\mathbf Z$
测试时严格成立。若另附一个混合第一输出的管，则仍必须用
R487 的真实分支转置；不能把管藏在“任意伴随测试”中。

## 8. 普通深域与固定 CM 域如何准确相接

从 R496、(20) 直接得到一条完整来源比较：
$$
\boxed{
\nu_{e_1}|_{V'\in p^2\mathbf Z_p}
=\lambda^2(P_{V,2})_*\nu_{\mathscr De_1}.}
\tag{27}
$$
左边是一条真实普通两层限制，右边的来源是原固定 CM trace
$\mathscr De_1=q$。同样，
$Fv=z=\mathscr Dv$，而
$Fz=-v=-\mathscr Dz$。
所以在相同物理变换下
$$
\boxed{
\nu_v|_{V'\in p^2}
=\lambda^2(P_{V,2})_*\nu_{\mathscr Dv},\qquad
\nu_z|_{V'\in p^2}
=-\lambda^2(P_{V,2})_*\nu_{\mathscr Dz}.}
\tag{28}
$$
这里没有在未知来源池中增加一个中央假设。

为了明确其范围，若 $\varphi(Y,\mathbf Z)$ 是一个混合测试，
(3)、(9) 的完整测度作用准确是
$$
\int\varphi\,d(\mathscr D\mu)
=\omega^{-1}\int
 \varphi(\omega Y,\mathbf Z)\,
 d(N_{\gamma_{19}}N_{\bar\gamma_7}^2)_Y\mu.
\tag{29}
$$
最右边须保三次实际 CM trace 的全部纤维，
或等价地保 (8) 的整个复合纤维。不能将它替换为仅有 ratio 的
一个普通坐标缩放。第一 $\omega$ 旋转虽然保 principal
Mellin 权，却改变依赖 $Y$ 的线性管。

例如 R483 中旧管
$W=c_Y Y+r(\mathbf Z)$ 在这一旋转下变成
$c_Y\omega Y+r(\mathbf Z)$；再附上 (27) 的
$P_{V,2}$，还必须使用 R496 的原
$$
Y_s\longmapsto
Y_s+\frac{37-3\delta}{36}(\kappa^2-1)V'.
\tag{30}
$$
(23)、(26) 对独立伴随条件的返回已全部付清；
(27)–(30) 仍保完整移动管和补域。
这正是后续将原非零网格、参考非齐次项送入同一中央的接口，
不是一个已经删去补域的非零定理。

## 9. 四挠差的实际分支号

为使 R499 的独立代数计算与本篇的 $\epsilon(t)$ 规范一致，
可用如下不含自由选根的短锚。令 $\sigma_-$ 是 $b=-1$ 的原
reduced sigma，$\Omega_0>0$ 是其 primitive CM 实周期。
准确缩放为
$$
\sigma_1(z)=i\sigma_-(z/i),\qquad
x_1(z)=-x_-(z/i),\qquad \Omega=i\Omega_0.
\tag{31}
$$
$\sigma_1'(0)=1$，canonical $\eta$ 同时按此缩放，
故这就是 $b=1$ 的同一原规范。
$x_-(\Omega_0/2)=1$；doubling 方程是
$$
x^4-4x^3+8x+4=(x^2-2x-2)^2.
$$
实区间上的 $x_-(\Omega_0/4)>1$，所以它为 $1+\sqrt3$。
因此
$$
x_1(\Omega/4)=-1-\sqrt3,\qquad
x_1(\delta\Omega/4)=-1+\sqrt3.
\tag{32}
$$
第二式也由原
$x(\delta z)=-(x(z)^3+4)/(3x(z)^2)$ 直接得到。

在固定 $h=x(\Omega/2)=-1$ 的纤维，
起始 $e=-1-\sqrt3$ 是 Norm1 标签，$\epsilon=-i$；
共轭 $e=-1+\sqrt3$ 是 Norm3 标签，$\epsilon=+i$。
所以若 R465 的两个完整贡献是 $c,\bar c$，
其加权差准确为
$$
\boxed{-i(c-\bar c),}
\tag{33}
$$
而不是反号。primitive CM 基的单位改变只同时轮换三条二挠
纤维，不交换固定 $h=-1$ 的这两个 Norm 类。
本篇 (18) 的 full lift 证明本身不依赖任何数值半周期采样。

## 10. 证书

- [check-r501-whole-cm-exchange-and-complete-companions.py](../scripts/check-r501-whole-cm-exchange-and-complete-companions.py)
- [check-r501-whole-cm-exchange-and-complete-companions.json](../scripts/check-r501-whole-cm-exchange-and-complete-companions.json)

脚本用精确 $\mathbf Q(\delta)$ 和 Gaussian 系数核对：
整个 CM ratio、复合标签、六个真实格周期、
$3159/-662$ 两个完整相位整数、十六项重排、
未投影四态交换、实际 $96$ 元群以及四挠分支锚。
正文给出 whole 标量、完整张量格和域运输的证明。

直接依赖：

- [R496：新 V′ 两层核心与四个实际来源](R496-original-new-axis-even-core-and-four-source-group.md)。
- [R493：实际六 sigma 几何及第一 Y 保持](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)。
- [R476：原 D33 八维块与五伴随](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [R483：原 CM13/19 完整伴随实现](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。
- [R465：同一原六变量张量格](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
