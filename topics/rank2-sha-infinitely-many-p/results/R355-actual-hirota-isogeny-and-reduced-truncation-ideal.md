# R355 — 原 Hirota 截断理想的实际同源、唯一单根与完整 norm-three 归属

日期：2026-11-13。**状态：以下真实核的几何分类、带原 $\mu_3$ 条件的
双数刚性，以及 R354 截断理想的准确饱和与 Jacobian 非零均已证明。
本篇没有证明两指定 Faber 观察至少一项非零；主目标未完成。**

本结果把 [R354](R354-original-hirota-bottom-unit-recursion-and-complete-truncation.md)
的一变量理想实际求出。证明必须固定原曲线并保留 $\mu_3$ 核稳定性；
一般 étale $p$ 子群确有 $\mu_p$ 图形变形，不能将其笼统称为无形变。

## 1. 原截断理想与结论

保持
$$
E_b:y^2=x^3+b,\quad b=17,\quad p=6s+1>7,\qquad
H=\binom{3s}{s}b^s,\quad \epsilon_3=b^{3s}.
$$
令 $r_n(t)\in\mathbf F_p[t]$ 是 R354 (15)–(17) 的全部原递推多项式，
$$r_0=1,\quad r_1=t,\quad \deg r_n\le n,\quad 0\le n\le2s.$$
置
$$
I=(r_{s+1},r_{s+2},\ldots,r_{2s})\subset\mathbf F_p[t],
\qquad f(t)=t\,r_s(t),
$$
$$
\boxed{t_*=-H^3\epsilon_3/24.}
\tag{1}
$$
R336 的实际可分核保证 $t_*$ 是这些条件的真实解，而且 $f(t_*)\ne0$。

**定理。** 完整原截断理想满足
$$
\boxed{I:f^\infty=(t-t_*).}
\tag{2}
$$
这是理想本身的等式，不只是一组几何点相同。特别可取一致的
有限饱和指数：
$$
\boxed{f(t)^{2s}(t-t_*)\in I.}
\tag{3}
$$

R354 的完整 norm-three 多项式的每个系数 $N_j(t)$ 都满足
$$
\boxed{f(t)^{2s}N_j(t)\in I.}
\tag{4}
$$
因此在 $f\ne0$ 的真实 degree-$s$ 开集上，完整 norm-three 已由
Hirota 截断理想支付，不再给一个额外自由参数。这里包括原相位与
monic 规范，仍是同一个实际核。

还得到一条真正的 Jacobian 非零输入：
$$
\boxed{\text{至少一个 }r_n'(t_*)\ne0,\qquad s+1\le n\le2s.}
\tag{5}
$$
这个导数是实际底部参数的变形导数。它尚未被认作两原 Faber 行。

## 2. 任意非退化截断解产生真正的椭圆同源

先在代数闭域 $k=\overline{\mathbf F}_p$ 上取任一解
$t_0$，满足 $I(t_0)=0$、$f(t_0)\ne0$。R354 的完整截断定理给
$$
R(U)=\sum_{n=0}^{s}r_n(t_0)U^n
$$
满足整个原 Hirota。按准确的 monic 规范置
$$
P(X)=\frac{b^s}{r_s(t_0)}R(X/b).
\tag{6}
$$
它 degree 恰为 $s$，$P_0\ne0$，且
$$q=P_1/P_0=t_0/b\ne0.$$

令 $D$ 为原曲线的不变导子，并在函数域定义
$$
u=-D^2\log P,\qquad v=\frac12Du.
\tag{7}
$$
Hirota 的对数形式给
$$D^2u=6u^2,\qquad Dv=3u^2.$$
因此
$$D(v^2-u^3)=0.\tag{8}$$
在特征 $p$ 中，(8) 本身只说明一个 $p$ 次幂函数，不能直接
宣布它是常数。这里必须逐处支付极阶。

$D\log P$ 仅在 $P$ 的零点和 $O$ 可能有一阶极，故 $u$ 至多二阶、
$v$ 至多三阶。因此 $v^2-u^3$ 在每个可能极点的阶至多六。
局部不变导子为单位乘形式参数导数；被它杀掉的 Laurent 级数
只有指数为 $p$ 倍数的项。因为 $p>7$，六阶以内不可能有负的
$p$ 倍数指数，所以 (8) 没有任何极点。曲线完备，故
$$v^2-u^3=B\in k.\tag{9}$$

该常数不是零。取原 $Q=(0,\beta)$、$\beta^2=b$。
因 $P=P_0(1+qx^3+\cdots)$，
$$
u(Q)=0,\qquad v(Q)=-24\beta^3q.
$$
这是由 $D^3(x^3)(Q)=48\beta^3$ 直接计算，因而
$$
\boxed{B=576b^3q^2\ne0.}
\tag{10}
$$
所以 (7) 给一个到光滑椭圆曲线
$$E_B:v^2=u^3+B$$
的非恒有理映射。

## 3. 每处极阶、零点重数与同源次数

$P(x^3)$ 在原点有极阶
$$6s=p-1.$$
它的零点总重数为 $p-1$，所以每个零点重数 $m$ 都满足
$1\le m<p$。在这样的零点，以原微分的局部参数核定首项，得
$$u\sim m z^{-2},\qquad v\sim-m z^{-3}.$$
(9) 的最高极系数是 $m^2(1-m)$。因 $m\not\equiv0\pmod p$，
它只能在 $m=1$ 时消失。故 $P$ 的全部零点都为单根。

在 $O$，$P\sim z^{-(p-1)}$，所以
$$u\sim-(p-1)z^{-2}=z^{-2},\qquad v\sim-z^{-3}.$$
因此 $u$ 恰有 $p$ 个二阶极：$O$ 及 $P$ 的 $p-1$ 个不同零点。
由 $E_B$ 上的坐标 $u$ 本身是二次函数，映射
$$
\varphi:E_b\longrightarrow E_B,\qquad P\longmapsto(u(P),v(P))
$$
的次数正好是 $p$。有理映射在光滑完备曲线上延拓为态射，且
$\varphi(O)=O$。保持原点的椭圆曲线态射是同态，故它是一条同源。

它的原微分完全归一：
$$
\boxed{\varphi^*\frac{du}{2v}=\frac{dx}{2y}.}
\tag{11}
$$
因此它可分，核是 $p$ 阶 étale 子群。由于原 $E_b$ 普通，
$E_b[p]$ 的几何点群只有一个阶 $p$ 子群，其约化子群正是整个
étale 部分。于是 $\ker\varphi$ 就是原 $V$ 的核。

monic $P$ 的 divisor 是
$$\sum_{Q\in\ker\varphi\setminus\{O\}}(Q)-(p-1)(O).$$
这个 divisor 与 monic 首项唯一决定 $P$，所以 (6) 必为 R336
的原实际核多项式。特别
$$\boxed{t_0=t_*.}\tag{12}$$
到此证明了 $f\ne0$ 中几何解唯一；还没有证明它是单根。

## 4. 为什么必须保留原 μ3 条件

若只知道某个 $p$ 阶核是 étale，不能据此排除它在双数上的变形。
为核定单根，以下始终固定原曲线 $E_b$，取
$$A=k[\epsilon]/(\epsilon^2).$$
假定 $t_A=t_*+\epsilon h$ 满足整个截断理想，且 $f(t_A)$ 为单位。
R354 的递推和最高阶消去都是环上的代数恒等式，所以仍给一个
degree-$s$ monic 多项式 $P_A(x^3)$ 满足全部 Hirota。

其模 $\epsilon$ 的零点由 §3 已知都是单根，故各零点在 $A$ 上
是 étale Cartier 截面。在这些移动截面附近，取该截面的局部参数；
$D\log P_A,u_A,v_A$ 的相对极阶仍至多为 $1,2,3$。
因此 §2 的论证继续成立：$D(v_A^2-u_A^3)=0$，局部负指数必须为
$p$ 的倍数，六阶以内没有这样的极。于是差是全局常数
$$B_A=576b^3(P_{A,1}/P_{A,0})^2\in A^\times.$$
这里使用移动零点的真实局部参数，不能在固定坐标中把展开产生的
额外 nilpotent 极项单独删除。

由同一个 $u_A,v_A$ 得到
$$\varphi_A:E_b\times A\longrightarrow E_{B_A}.$$
在各 pole 附近的原 Laurent 首项保证映射延拓；(11) 在 $A$ 上仍
准确成立。故它是 étale 的，特殊纤维次数为 $p$，所以是有限 étale
degree-$p$ 态射。它保持原点，仍是椭圆曲线同态。
也可直接核定最后一句：其群律交换差约化为零，故取值在目标的
一阶 Lie 方向；它是完备 $E_b\times E_b$ 上的全局函数，所以为常数，
而在两坐标轴上为零。

现在使用未曾改变的 $P_A(x^3)$ 形状。对原 $\omega\in\mu_3$，
$$[\omega]^*P_A=P_A.$$
由 (7) 得
$$[\omega]^*u_A=\omega^{-2}u_A,\qquad
[\omega]^*v_A=\omega^{-3}v_A.$$
所以 $\varphi_A$ 与源、目标的原标准 $\mu_3$ 作用相容，其核是
一个真正的 $\mu_3$ 稳定子群。这个条件不能省略。

## 5. 原 μ3 两个不同特征杀掉图形变形

在代数闭基域上，固定普通曲线的 $p$-torsion 分解为
$$E_b[p]\simeq\mu_p\oplus\mathbf Z/p\mathbf Z.$$
将这个固定分解基变换到 $A$。
任何约化为原 étale 核的 finite étale 阶 $p$ 子群，其投影到
$\mathbf Z/p\mathbf Z$ 是同构，因而是一个同态
$$h:\mathbf Z/p\mathbf Z\longrightarrow\mu_p$$
的图形。这正是一般情况下确实存在的变形。

设原 $\omega$ 在 connected 部分的特征为 $\lambda_c$，在 étale
部分的特征为 $\lambda_e$。connected 的切向给一个 primitive 三次根；
Weil 配对及 $N(\omega)=1$ 给
$$
\lambda_c\lambda_e=1,\qquad
\lambda_c\ne\lambda_e.
\tag{13}
$$
二者都在 $\mathbf F_p^\times$ 中，因为 $p\equiv1\pmod3$。

图形的 $\mu_3$ 稳定性要求
$$h([\lambda_e]x)=[\lambda_c]h(x).$$
写 $h(1)=1+\epsilon a$，则该式准确给
$$(\lambda_e-\lambda_c)a=0.$$
由 (13) 得 $a=0$。所以这个图形是平凡图形：
$$\boxed{\ker\varphi_A=(\ker V)\times A.}\tag{14}$$

$P_A$ 与固定 monic $P$ 有相同的相对 divisor；它们的比值是
原完备曲线上的全局单位，即 $A^\times$ 的一个常数。
monic 首项使该常数为一。因此 $P_A=P$，从而 $h=0$。
这证明 $t_*$ 没有非平凡的双数切向。

(14) 的证明同时说明适用边界：若删去 $P(x^3)$ 的原 $\mu_3$
条件，$(1+\epsilon a)$ 给出的 $\mu_p$ 图形就不能如此排除。

## 6. 准确饱和理想与有限指数

$\mathbf F_p[t]$ 是主理想整环。令 $g$ 是 $I$ 的 monic 最大公因子。
§§2–3 证明：在 $f\ne0$ 的代数闭开集里，$g$ 只有根 $t_*$。
§§4–5 又证明该根不能有重数大于一；否则
$t_*+\epsilon$ 就给一个非平凡双数解。

因此所有其他根都在 $f=0$，且
$$g=(t-t_*)g_{\rm bad},$$
其中 $g_{\rm bad}$ 的全部根都是 $f$ 的根。这恰证明 (2)，包括
其非约化信息。

$I$ 非零，否则上述开集会有无限多个解。各生成元的次数至多 $2s$，
故 $\deg g\le2s$。因而
$$g_{\rm bad}\mid f^{2s}.$$
所以 $g\mid f^{2s}(t-t_*)$，即 (3)。
这是一个统一的可执行 Bézout 接口：用 R354 的明确递推生成有限多项式，
再作单变量 Euclidean 算法，就能给相应系数；不存在未指定的核选择。

## 7. 完整 norm-three 的真实理想归属与 Jacobian

R354 的完整规范为
$$
r_s(t)^2U^{2s}R_s\!\left(-\frac{(U+4)^3}{27U^2};t\right)
-R_s(U;t)\mathcal T_{R_s}(U;t)=\sum_jN_j(t)U^j.
$$
这些 $N_j$ 是实际多项式，不只是一条局部 principal-part 行。
在 $t_*$ 上，它们全为零，因为 §3 识别出的正是原可分核，
而 R336 已证明同一个原核的完整 norm-three。
因此 $t-t_*$ 整除每个 $N_j$。结合 (3) 即得 (4)。

同样地，原 $r_s^3+24t$ 也在这个饱和理想中。
本篇并不把它的立方根重新指定为一个任意角色；原相位仍由
R343、R345 支付。

把 (3) 写为
$$
f^{2s}(t-t_*)=\sum_{n=s+1}^{2s}A_n(t)r_n(t)
$$
并在 $t_*$ 求导，得到完整 Jacobian 关系
$$
\boxed{
f(t_*)^{2s}=\sum_{n=s+1}^{2s}A_n(t_*)r_n'(t_*).
}
\tag{15}
$$
左边为单位，所以证明 (5)。这里是同一个真实 kernel 的变形
检测，不是从一个任意环境矩阵的满秩推出非零。

## 8. 对原两行实际解决了什么

R354 已把两指定原观察写成
$$
\mathcal L=\frac{b^{s-1}}{r_s}\beta_1(t),\qquad
\mathcal Q=\frac{b^{s-1}}{r_s^2}Q_\beta(t).
$$
本结果把它们所在的完整非退化截断商环准确识别为
$$
\mathbf F_p[t,f^{-1}]/I\simeq\mathbf F_p,\qquad t\mapsto t_*.
$$
所以原 norm-three 没有留下可任意调节的另一个支，也没有隐藏的
nilpotent kernel 参数。

但是 (15) 目前只保证某个实际截断导数非零，并没有证明
$\beta_1(t_*)$、$Q_\beta(t_*)$ 就检测这条切向。
要由 R349 的新三次型单位性得到两行联合非零，仍须证明它们与
(15) 或同一商环中的指定三次行之间的实际关系；本篇不跳过此步。

本证明是从原多项式、极阶和固定曲线的群方案结构直接得到的，
不依赖额外素数扫描。提交使用 GitHub Contents API 小文本接口，
不是本地 git pull。
