# R813 — 同一原修正的带权二类误差与首共振 Cartier 单位

日期：2026-11-15。**状态：下述原同源、原精度下的实际 Cartier 非零已证明；它尚未被识别为杀全部原 $\mathcal W_D$ 像的左行，主目标仍未完成。**

本篇使用 R808 的同一个首修正 $R$，没有增添来源或改选法向数据。
在原因子曲线与原等谐椭圆曲线的纤维积上，构造一个明确的代数微分。
其阶恰为 $p-1$，首系数是原 $q_0,u_0,e_0,a$ 的显示单位。
因此它的 Cartier 像在指定点非零，且该微分不是全局恰当微分。

这一步没有把非恒定因子提出 Cartier 算子。
也没有把这个辅助微分自动认作原剩余空间的 Serre 对偶行：
它的全部分歧极、边界极和同源返回条件仍须保留。

## 1. 原同一个 R 与精度范围

保持 R808 的原数据
$$
p=6s-1>101,\qquad f_D<p,\qquad
s=2h+r,\qquad 1\le r<h,\qquad
1\le\ell<s-13,\qquad \ell\le r+h.
\tag{1}
$$
特别 $k_{\rm carry}=0$。取合法原来源
$$
P^{\rm fact}=t^r\widetilde F^3\widetilde q\in\mathcal W_D,
\qquad
F(0,1)=0,\quad
e_0=(\mathcal EF)(0,1)\ne0,\quad q_0=q(0,1)\ne0,
$$
$$
\mathcal E=Y\partial_Y.
\tag{2}
$$
$F$ 不可约，$C=(F=0)$ 为原十九角曲面上的严格变换，
$P=(0,1)$ 为光滑原点。实际 regularized 接触为
$$
\widetilde F(t(w),g(w))=w^h u(w)+p\xi(w),\qquad
u_0=u(0)\ne0,
$$
$$
e(w)=(\mathcal E\widetilde F)(t(w),g(w)),\qquad
C_0=\left(\frac tw\right)(0)^r q_0=(-1)^r q_0.
\tag{3}
$$
原 $t(w)=-w+O(w^2)$，原 Gaussian 单位记为 $a$。

假设同一个 $R$ 满足原相对精度
$$
J(P^{\rm fact}+pR)\in p^2\Gamma_{2s+\ell}.
\tag{4}
$$
例如原真正 primitive 第三精度
$$
M^{\rm orig}(P^{\rm fact}+pR+p^2T)\in p^3,\qquad
M^{\rm orig}=c_*U_0m_{13}J
\tag{5}
$$
按 R808 精度引理推出 (4)。这里只能使用那个完整引理：
$J_A$ 与两条十三行 $J_B$ 的原权分别为一与 $p$；
原第一次 $M\in p^2$ 本身不足以推出 (4)。

下文 $R$ 表示 (4) 中同一个修正的约化。
R808 已证明其实际法向首项为
$$
\boxed{
(\mathcal ER)(t(w),\psi(t(w)))
=\frac{5C_0u_0^3}{a}\,w^h+O(w^{h+1}),
}
\tag{6}
$$
其中 $F(t,\psi(t))=0,\ \psi(0)=1$。
因 $r>0$，native $\xi$ 在此首项中不出现；
没有把它从后续完整块中删掉。
本篇只用 (6)，不要求短块增补的额外 $\ell\le r$ 条件。

## 2. 真实代数覆盖与指定有理点

先采用原无量纲角规范
$$
E_0:\ y^2=x^3+1,\qquad
t=-x^{-3},\qquad
\omega_0=\frac{dx}{2y}.
\tag{7}
$$
$\omega_0$ 在 $E_0$ 上为非零全纯微分。
原 $t$ 正是这份角坐标；这不是把新的 theta 来源加入 $\mathcal W_D$。

令 $\widetilde C$ 为 $C$ 的正规化，并取
$$
\widetilde C\times_{\mathbf P^1_t}E_0
$$
中通过 $(P,O)$ 的分量，再作正规化，记为 $\mathscr C$。
它的指定点记为 $\mathscr P$。

这份局部构造没有分裂或常数域问题。
因为 $F_Y(P)\ne0$，$\widetilde C$ 在 $P$ 的完成局部环为 $k[[t]]$。
在 $E_0$ 的 $O$ 处，真实参数
$$
z_0=-x/y
$$
满足
$$
x=z_0^{-2}+O(z_0^4),\quad
y=-z_0^{-3}+O(z_0^3),\quad
t=-z_0^6+O(z_0^{12}),\quad
\omega_0=(1+O(z_0^6))\,dz_0.
\tag{8}
$$
故纤维积在该点的完成环就是 $k[[z_0]]$。
指定分量唯一，并由此下降到原 $k$；$\mathscr P$ 为 $k$ 有理光滑点。
即使整个纤维积可约，也不将其它分量丢入或混入本分量。
其函数域的常量域仍为 $k$：任何代数常量扩张都嵌入该有理点的剩余域。

两份函数域扩张都可分。
$E_0/k(t)$ 的次数为六，$p>3$；
$k(C)/k(t)$ 可分由 $F_Y\not\equiv0$ 给出。
所以 (7) 的导子 $D$、由
$$
df=(Df)\omega_0
$$
定义，唯一扩张到 $k(\mathscr C)$。
$\omega_0$ 的拉回在 $\mathscr P$ 非零；在其它分歧点可有零，
那些零不能在后续全局极点计算中忽略。

以下允许把原有限 $w$ 前缀搬到此完成环。
只需
$$
w=z_0^6+O(z_0^{12}).
\tag{9}
$$
这里 $w$ 是原有限轴记号，不被声称为 $\mathscr C$ 上的全局有理函数。
所有用到的 reference theta 系数都严格低于首共振 $w^s$。

## 3. 沿原因子的代数 zeta 逼近及实际二类误差

将 $Y$ 看作 $k(\mathscr C)$ 中原因子的径向函数，并记
$$
e=\mathcal EF=YF_Y,\qquad d=1+8t.
$$
定义完全代数的函数
$$
\boxed{
\zeta_F
=\frac1{34}\left(
\frac{DY}{Y}-\frac{Dd}{d}-17\frac{Dx}{x}
\right).
}
\tag{10}
$$
在 $C$ 上微分 $F(t,Y)=0$，得
$$
\frac{DY}{Y}=-\frac{F_t}{e}\,Dt,\qquad
Dt=\frac{6y}{x^4}.
$$
因此 (10) 的明确有理式为
$$
\boxed{
\zeta_F
=-\frac yx-\frac{Dt}{34}
       \left(\frac{F_t}{e}+\frac8d\right)
=-\frac yx-\frac{3y}{17x^4}
       \left(\frac{F_t}{e}+\frac8d\right).
}
\tag{11}
$$
$F_t$ 在此是固定 $Y$ 的偏导。
所有 $e=0,d=0,x=0$ 以及其它边界处的实际极点都保在 (11)；
只在 $\mathscr P$ 使用 $e_0\ne0$。

若把因子方程乘以任意不恒为零的底函数，
$(uF)_t/\mathcal E(uF)$ 在 $F=0$ 上仍为 $F_t/e$。
所以 (10) 不依赖这种因子框的选择。

定义原二类误差微分
$$
\boxed{\omega_F=d\zeta_F+x\omega_0.}
\tag{12}
$$

**引理 1。** 在 $\mathscr P$，
$$
\boxed{
\omega_F
=-\frac{(6h)(6h-1)}{34}\frac{u_0}{e_0}
\,z_0^{6h-2}\,dz_0
+O(z_0^{6h-1})\,dz_0.
}
\tag{13}
$$
特别其阶准确为 $6h-2$。

**证明。** 原未共振的角恒等式为
$$
\rho=d\Theta^{17},\qquad \Theta=x\sigma^2.
$$
因此在原整有限前缀内
$$
\frac1{34}\left(
D\log(\rho/d)-17D\log x
\right)=\zeta,\qquad d\zeta=-x\omega_0.
\tag{14}
$$
这里只使用次数到 $6h$ 的 reference 恒等式。
由于 $h<s$，这些系数严格在首个 $p$ 分母／Gaussian 共振之前。
可以先在特征零使用 $\sigma'/\sigma=\zeta$，
再把这段整系数约化；不在特征 $p$ 中虚构一个完整的原函数
$\zeta$ 或完整椭圆对数。

由 (3)、$e_0\ne0$ 以及因子分支的有限 Taylor 反解，
$$
\bar g/\psi-1
=\frac{u_0}{e_0}w^h+O(w^{h+1}).
$$
对这一个有限单位比值取到所需阶的对数，故
$$
\eta=\log(\bar g/\psi)
=\frac{u_0}{e_0}z_0^{6h}+O(z_0^{6h+1}).
\tag{15}
$$
首项只用 $\log(1+v)=v+O(v^2)$；
所有实际用到的分母均小于 $p$。
(14) 与 (10) 在该有限段给
$$
\zeta_F-\zeta=-\frac1{34}D\eta.
$$
再微分一次，因 $D=(1+O(z_0^6))^{-1}\partial_{z_0}$，
得到 (13)。reference 的其余误差在所读阶之后：
这里 $6h-2<p-1$，没有使用首共振系数本身。

最后 $0<6h-1<6h<p$，
故两个整数因子在 $k$ 中均为单位。
$34,u_0,e_0$ 同样为单位，因此 (13) 的首项非零。证毕。

## 4. 同 R 指定带权类的 Cartier 单位

现在使用原全修正的实际函数
$$
R_E=(\mathcal ER)|_C\in k(\mathscr C).
$$
定义
$$
\boxed{\Omega_R=t^rR_E\,\omega_F.}
\tag{16}
$$
这是同一个 $R$ 的明确有理微分。
$R_E$ 本身来自原 $\mathcal E$ 对来源的作用；
但不把乘 $t^r$ 或微分 (16) 自动当成同预算的新来源列。

**定理 2。** 在 $\mathscr P$，
$$
\boxed{
\Omega_R
=\gamma_R z_0^{p-1}\,dz_0
+O(z_0^p)\,dz_0,
\qquad
\gamma_R=
-\frac{5(6h)(6h-1)q_0u_0^4}
       {34\,a\,e_0}\in k^\times.
}
\tag{17}
$$
因此其全局 Cartier 像在指定点满足
$$
\boxed{
\mathcal C(\Omega_R)|_{\mathscr P}
=\gamma_R^{1/p}\,dz_0|_{\mathscr P}\ne0.
}
\tag{18}
$$
特别 $\Omega_R$ 不是全局恰当微分。

**证明。** (6)、(8)、(9) 给
$$
t^rR_E
=(-1)^r\frac{5C_0u_0^3}{a}\,
z_0^{6r+6h}+O(z_0^{6r+6h+1}).
$$
与 (13) 相乘，其指数恰为
$$
6r+12h-2=6s-2=p-1.
$$
未经合并的首系数是
$$
-\frac{5(-1)^rC_0(6h)(6h-1)u_0^4}
       {34\,a\,e_0}.
\tag{19}
$$
由于原 $t/w$ 的首系数为 $-1$，
$C_0=(-1)^rq_0$，两个符号准确抵消，得 (17)。
原 $q_0,e_0$ 与 Gaussian $a$ 均没有被规范成一。

在完美常量域上的一元可分函数域内，
任一局部参数是一个 $p$ 基。
Cartier 算子可由其标准展开直接定义：
$$
\mathcal C\!\left(\sum_j c_jz_0^j\,dz_0\right)
=\sum_n c_{pn+p-1}^{1/p}z_0^n\,dz_0.
\tag{20}
$$
这是全局 Cartier 在完成局部环的限制；
它杀 $df$，并满足
$\mathcal C(f^p\omega)=f\mathcal C(\omega)$。
由于 (17) 的所有更低项都为零，
(20) 的常数项正是 $\gamma_R^{1/p}$，得 (18)。
而全局恰当微分的 Cartier 像为零，故最后断言成立。证毕。

式 (18) 只需微分的首项。
它不要求原椭圆对数在特征 $p$ 中延长到 $p$ 阶：
$z_0=-x/y$ 是真实有理参数，(13) 只读取严格低于共振的有限段，
再由阶的加法使 (16) 的首项准确到达 $p-1$。

### 原物理尺度的单位因子

若在物理曲线 $E_b:y^2=x^3+b$ 上直接计算，
使用 $t=-b/x^3$、原 $w=bz_0^6+O(z_0^{12})$，
则 (10)–(12) 的形式不变，$Dt=6by/x^4$。
(17) 的准确首系数改为
$$
\boxed{\gamma_{R,b}=b^s\gamma_R.}
\tag{21}
$$
这是因为两次接触各贡献 $b^h$，而 $t^r$ 贡献 $b^r$，
总指数 $2h+r=s$。原固定 $b$ 为 $p$ 单位，故 (18) 的非零保持。
这也显式保留了从原物理尺度转到 (7) 的单位代价；
不将不同局部参数下的首系数不加缩放地相认。

对同一 $P^{\rm fact}$ 改因子框
$F\mapsto cF,\ q\mapsto c^{-3}q$，
首项 $u_0,e_0$ 同乘 $c(P)$，
故 $q_0u_0^4/e_0$ 不变。
因此显示单位与同一真实基准相容，不来自随意选取因子首系数。

## 5. 明确的全局带权恒等式与尚未付的左行

不能把 (18) 改写为“某个单位函数乘原全纯 Cartier 类”。
对同一个全局微分有准确恒等式
$$
\boxed{
\mathcal C(\Omega_R)
=\mathcal C\!\left(
t^rR_E\,x\omega_0-\zeta_F\,d(t^rR_E)
\right),
}
\tag{22}
$$
因为从 (16) 减去右端括号内微分，恰为
$d(t^rR_E\zeta_F)$。
右端仍保完整 $R_E$、(11) 的 $e$ 分歧极和所有十九角边界。

同样，若使用 $e^3$ 清极，只有
$$
\mathcal C(e^3\omega_F)
=\mathcal C\!\left(e^3x\omega_0-3e^2\zeta_F\,de\right),
\tag{23}
$$
不能把它换成 $e^3\mathcal C(x\omega_0)$。
(22)–(23) 都是实际有理式，未赋它们同 $\mathcal W_D$ 的来源帽。

原 Serre／Grothendieck 留数接口可能使用 $dt/e$，
并在 $t$ 分歧点由 $dt$ 的零抵消 $e$ 的零。
若沿此继续，仍须证明以下具体事项：
所造行确实杀全部原 $\mathcal W_D$ 列，
满足原 $K_X|_C$ 和各角框，
保低行右逆的高尾，
且对同一个 $R$ 同时保留剩余 normal、两条十三行及原 $d_2$。
本篇没有把 (16) 属于一个辅助函数域等同于这些条件。

因此 (18) 是同原第三精度假设推出的实际非零 Cartier 观测，
不是已经与该假设矛盾的原左余核。
它也不说 $\Omega_R$ 应当全局恰当；
相反，定理2已证明它不恰当。
需要另证原全矩阵或实际对偶会迫其恰当／Cartier 为零，
才能把这条单位变成原指定 forcing 的非零障碍。

依赖：
[R808](R808-original-third-precision-corrector-split-branches-and-near-normal-jet.md)；
[R459](R459-actual-angular-content-and-padded-cubic-first-lift.md)；
[R790 真实可动因子／两短块增补](../notes/2026-11-15-r790-moving-factor-and-two-short-blocks.md)。
全证明只用原实际低轴、同一 $R$ 的已付 normal、代数覆盖和 Cartier 的局部定义，
无新增数学计算或生成数据。
