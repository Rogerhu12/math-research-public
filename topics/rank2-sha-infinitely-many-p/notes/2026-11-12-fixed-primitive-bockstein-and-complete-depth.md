# 固定原函数的局部 Bockstein 与完整中央深度

日期：2026-11-12。状态：本文的截断 Euler 复形、准确 Bockstein
坐标、整 Frobenius 坐标兼容及完整导数判据的系数转译均已证明。
它们仍未给出无穷多个素数上的非零性。

沿用[固定周期 torsor 原函数](2026-11-12-fixed-period-torsor-primitives-and-residues.md)
的实际对象

$$
\mathcal B_1(u)=\sum_{m\ge4}C_mu^m,\qquad
C_m=\frac{h_m^2}{24\,17^{m-4}m!}\quad(4\mid m),\qquad
h_m=m![z^m]A_1(z)\in\mathbb Z .
\tag{1}
$$

其他 $m$ 的 $C_m$ 为零。这里 $A_1$ 是已认证的次数十七实际
截面的 $D=1$ 缩放，不能换成秩零参考截面。
所有目标素数都不整除 $24\cdot17$。以下约定 $v_p(0)=+\infty$。

固定原函数为

$$
\mathcal H_i(u)=\sum_{m\ge4}\frac{C_m}{m-1}u^{m-1},
\qquad
\mathcal H_o(u)=\sum_{m\ge4}\frac{C_m}{(m+1)^2}u^{m+1}.
\tag{2}
$$

它们分别从 $u^3/3$、$u^5/25$ 开始，不随 $p$ 重新选择。
在固定 GM torsor 上，它们由

$$
\delta\mathcal H_i=\frac{M_1K}{sL^2},\qquad
\delta\mathcal E=\frac{M_1}{sK},\qquad
\delta\mathcal H_o=\frac{\mathcal E}{sKL}
\tag{3}
$$

定义，其中 $u=L/K$、$s=1-4t^2$。

## 1. 一个实际且完全可计算的局部偏上同调复形

对每个目标素数取

$$
\mathcal A_p=u\mathbb Z_p[u]/(u^{p+1}),\qquad
\mathscr E=u\partial_u .
\tag{4}
$$

去掉常数项是为了不混入与中央问题无关的常数核。
有两个两项复形

$$
\mathcal C_i=[\,\mathcal A_p\xrightarrow{\mathscr E}\mathcal A_p\,],
\qquad
\mathcal C_o=[\,\mathcal A_p\xrightarrow{\mathscr E^2}\mathcal A_p\,].
\tag{5}
$$

因为 $\mathscr E(u^n)=nu^n$，准确有

$$
\begin{aligned}
H^0(\mathcal C_i)&=H^0(\mathcal C_o)=0,\\
H^1(\mathcal C_i)&=(\mathbb Z/p\mathbb Z)\,u^p,\\
H^1(\mathcal C_o)&=(\mathbb Z/p^2\mathbb Z)\,u^p.
\end{aligned}
\tag{6}
$$

这些是从同一固定原函数方程取得的有限 jet 复形。
$\mathcal A_p$ 的秩仍为 $p$；(6) 的单个余核并不意味着完整
GM 或 Kummer 对象已经下降为一个固定秩的 cohomology 群。

### 1.1 第一和第二 Bockstein 的准确规范

模 $p$ 后，两个复形的 $H^0,H^1$ 都由 $u^p$ 张成。
对 $\mathcal C_i$，提升 $u^p$ 后

$$
\frac{\mathscr E(u^p)}p=u^p,
$$

所以第一 Bockstein 是两条线之间的恒等映射。
对 $\mathcal C_o$，

$$
\frac{\mathscr E^2(u^p)}p=pu^p,\qquad
\frac{\mathscr E^2(u^p)}{p^2}=u^p,
$$

故第一 Bockstein 为零，第二个为恒等映射。

这也可以不使用谱序列语言：先对每个 $n<p$ 以单位
$n$ 或 $n^2$ 唯一求解。剩下的方程只有
$px=g_p$ 或 $p^2x=g_p$，其归一化剩余就是 $x\bmod p$。

## 2. 实际输入已经消去初级 obstruction，留下的不是任意 lift

固定原函数准确满足

$$
\mathscr E\mathcal H_i=\mathcal B_1/u,\qquad
\mathscr E^2\mathcal H_o=u\mathcal B_1.
\tag{7}
$$

对惰性 $p\equiv3\pmod4$、$p\ge7$，R66 已证明
$C_{p+1}\in p\mathbb Z_p$。对普通 $p\equiv1\pmod4$、
$p\ge13,p\ne17$，R58/R66 已证明
$C_{p-1}\in p^2\mathbb Z_p$。
所以 (7) 的实际输入在 (6) 中的类均为零，存在唯一的
特征零原函数，而且其截断到 $u^p$ 已经整。

后一整性也可直接逐项检查。非共振项的分母 $m-1$ 或 $m+1$
都不被 $p$ 整除；相应 $m!$ 在这个范围也不含 $p$。
唯一的惰性共振项 $m=p+1$ 及普通共振项 $m=p-1$
正由上述实际整除消去。

先解出次数 $<p$ 的部分，再将 (7) 的剩余除以 $p$ 或 $p^2$，
由 §1.1 的 Bockstein 逆像得到的实际坐标为

$$
\boxed{\quad
\Gamma_{i,p}=[u^p]\mathcal H_i=\frac{C_{p+1}}p,\qquad
\Gamma_{o,p}=[u^p]\mathcal H_o=\frac{C_{p-1}}{p^2}.
\quad}
\tag{8}
$$

因此这里不是从模 $p$ 原函数的自由项中随意选一个 $u^p$ 系数：
特征零方程、零常数及完整实际输入固定了该系数。
模 $p$ 的齐次解可以任加 $cu^p$，但若在特征零也这样改，
(7) 的输入就会相应改变 $pcu^p$ 或 $p^2cu^p$。

写 $\beta_m=[z^m]A_1$，由 Wilson 定理和 (1)，

$$
\begin{aligned}
\Gamma_{i,p}
&\equiv-\frac{\beta_{p+1}^2}{24\,17^{p-3}}\pmod p,\\
\Gamma_{o,p}
&\equiv-\frac{(\beta_{p-1}/p)^2}{24\,17^{p-5}}\pmod p.
\end{aligned}
\tag{9}
$$

所以 (8) 的非零正是此前的首层充分判据。
这些坐标是实际平方乘单位；特别其精确赋值若为正，
必至少为 $2$，而不是任意的一阶正赋值。

## 3. 与真实整 Frobenius 坐标的完全精度兼容

R68 的真实整函数 $U_p,V_p$ 给

$$
u_F=V_p/U_p=t+O(t^3)\in t\mathbb Z_p[[t]],
\qquad u_F-u=O(t^p)
\tag{10}
$$

作为特征零级数的准确阶数断言。
普通情形最后的差可以带 $p^{-1}$ 系数；
本段不把它误说成完整的整坐标变换。

两原函数分别从 $u^3,u^5$ 开始，所以在替换 $u$ 与 $u_F$ 时，
$\mathcal H_i$ 的首个可能变化次数是 $p+2$，
$\mathcal H_o$ 的首个可能变化次数是 $p+4$。
由此

$$
\boxed{\quad
[u_F^p]\mathcal H_i(t(u_F))
 =[u^p]\mathcal H_i,\qquad
[u_F^p]\mathcal H_o(t(u_F))
 =[u^p]\mathcal H_o .
\quad}
\tag{11}
$$

这是 $\mathbb Q_p$ 中完全相等，而不只是模 $p$。
因此 (5)–(8) 可用实际整 Frobenius 坐标的这个有限截断实现。
它没有授权把 $\mathcal H_i$ 的全级数整性推到全部次数，
也没有把原周期坐标的源格变换当作全盘单位变换。

同样，(8) 只是沿实际形式曲线的共振坐标。
ambient period torsor 在 $L=t=0$ 的原有理方程带 apparent pole；
它在实际曲线上因 $M_1$ 的四阶零点而正则。
这不能单凭一个坐标的消失，就推出整个 ambient $p$-curvature
或全部非中央余类消失。

## 4. 普通完整导数条件在同一固定原函数中的准确转译

令 $J'_{o,p}(0)$ 表示 R40/R51/R56 的实际普通中央导数。
R56 的无周期完备证书给

$$
J'_{o,p}(0)=0
\quad\Longleftrightarrow\quad
v_p(h_{m_n})\ge2n+2\ \text{对每个 }n\ge0,
\qquad m_n=(p-1)p^n.
\tag{12}
$$

从 $D=17$ 改到 (1) 的 $D=1$ 只乘 $17$ 的整数次幂，
故不改变任何目标位的赋值。

对 $n\ge1$，$m_n+1$ 是 $p$ 单位，并且

$$
v_p(m_n!)=\frac{m_n-(p-1)}{p-1}=p^n-1.
\tag{13}
$$

由 (1)、(2) 得

$$
v_p([u^{m_n+1}]\mathcal H_o)
=2v_p(h_{m_n})-p^n+1\qquad(n\ge1).
\tag{14}
$$

$n=0$ 时分母另有 $(m_0+1)^2=p^2$。所以 (12) 完全等价于

$$
\boxed{
\begin{array}{l}
v_p([u^p]\mathcal H_o)\ge2,\\
v_p([u^{(p-1)p^n+1}]\mathcal H_o)
      \ge4n+5-p^n\qquad\text{对每个 }n\ge1 .
\end{array}}
\tag{15}
$$

因此，只要在这个**同一固定原函数**中找到一项违反 (15)，
就准确得到 $J'_{o,p}(0)\ne0$，继而得到本题普通初级有限性；
反向也由 R56 成立。没有把某个首层失败误当成完整导数为零。

## 5. 惰性完整导数条件的准确转译

令 $J'_{i,p}(0)$ 表示 R54/R62 的实际惰性半因子导数。
记

$$
m_n=(p+1)p^n,\qquad b_n=\frac{p^n-1}{p-1}.
$$

R62 的完整相邻比证书给

$$
J'_{i,p}(0)=0
\quad\Longleftrightarrow\quad
v_p(h_{m_n})\ge b_n+2n+1
       \quad\text{对每个 }n\ge1 .
\tag{16}
$$

这里从 $n=1$ 开始；没有将已证只在这些层使用的参考邻项赋值
擅自外推到 $n=0$。
由于 $m_n$ 的 $p$ 进数字恰有两个 $1$，

$$
v_p(m_n!)=\frac{m_n-2}{p-1}=p^n+2b_n.
\tag{17}
$$

且 $m_n-1$ 是 $p$ 单位，故

$$
v_p([u^{m_n-1}]\mathcal H_i)
=2v_p(h_{m_n})-p^n-2b_n.
\tag{18}
$$

于是 (16) 完全等价于

$$
\boxed{\quad
v_p([u^{(p+1)p^n-1}]\mathcal H_i)
      \ge4n+2-p^n\qquad\text{对每个 }n\ge1 .
\quad}
\tag{19}
$$

任一项违反 (19) 就准确得到 $J'_{i,p}(0)\ne0$，
由 R50/R54 推出本题该惰性初级有限。
目前惰性一侧没有把这个非零判据宣称为 Sha 有限性的必要条件。

另外 R54 的首层展开
$J_{i,p}(w)\equiv\beta_{p+1}w/(17c_p)\pmod{p^2}$、
$v_p(c_p)=-1$ 表明：若完整 $J'_{i,p}(0)=0$，
则 $\beta_{p+1}\in p\mathbb Z_p$，所以
$v_p([u^p]\mathcal H_i)\ge2$。
这是 (19) 的一个必要首层后果，并非其替代品。

## 6. 非零时的实际渐近与全局问题

还可准确看出这些界与普通半径估计的区别。
若 $j_o=v_p(J'_{o,p}(0))<\infty$，R56 的收敛式在充分大 $n$ 给

$$
v_p([u^{(p-1)p^n+1}]\mathcal H_o)
=2n+3+2j_o-p^n.
\tag{20}
$$

若 $j_i=v_p(J'_{i,p}(0))<\infty$，R62 的相邻比极限在充分大
$n$ 给

$$
v_p([u^{(p+1)p^n-1}]\mathcal H_i)
=2n+2j_i-p^n.
\tag{21}
$$

各处已知的归一单位不改变 $j_o,j_i$。
从 (15)、(19) 到 (20)、(21) 的差是沿指定稀疏指标的精确深度。
注意 (15)、(19) 的右端最终仍为负，主项是 $-p^n$；
因此完整中央消失并没有由这些公式自动变成“该固定原函数的
全部 Taylor 系数整”，也不自动改善整个收敛半径。

当前真正的全局任务可以表述为：对无穷多个普通或惰性素数，
在同一固定 torsor 原函数中证明至少一项违反相应的完整界。
本文给出了准确的局部偏上同调/Bockstein 坐标和所有深度门槛，
没有假定尚未证明的有限秩下降或跨素数非零定理。

## 7. 两种素数也可合并成一个固定原函数

令

$$
\mathcal H=\mathcal H_i+\mathcal H_o.
\tag{22}
$$

因为 $C_m$ 只在 $4\mid m$ 时非零，$\mathcal H_i$ 只含
$u^{4r-1}$，$\mathcal H_o$ 只含 $u^{4r+1}$。
因此对所有上述目标素数，

$$
\boxed{\quad
[u^p]\mathcal H=
\begin{cases}
C_{p+1}/p,&p\equiv3\pmod4,\\
C_{p-1}/p^2,&p\equiv1\pmod4.
\end{cases}\quad}
\tag{23}
$$

而 (15)、(19) 的完整指标也各自始终落在相应的模 $4$ 余类，
所以可把其中的 $\mathcal H_o,\mathcal H_i$ 统一替换为
$\mathcal H$，不发生交叉项。
这给出一个固定有理偏连接对象，同时包含两类 prime diagonal
及完整深度。它的首层系数在所有目标位都整。

这个和本身仍非 D-finite，不能只从两个加数的非 D-finite
性断言这一点。准确证明如下。在固定 torsor 的记号下，

$$
sKL\,\mathcal H'
=\frac{M_1K^2}{L}+\mathcal E,
\tag{24}
$$

所以

$$
\delta(sKL\,\mathcal H')
=-\frac{M_1K}{sL^2}
 +\frac{M_1'K^2+M_1KQ}{L}
 +\frac{M_1}{sK}.
\tag{25}
$$

取不保持 $L$ 线的 cusp unipotent 的不同整数幂。
固定 torsor 稿已证明其 $L_n$ 两两不成比例，以及实际周期域
就是 torsor 函数域。(25) 的第 $n$ 个分支沿 $L_n=0$
有真正双极点。第二项在该处至多简单极点；
第三项即使某个 $K_m=0$ 恰与该除子相同，也至多给简单极点。
因此有限线性组合中，独有的双极首项不能消掉，分支线性独立。
故 (25) 非 D-finite。

若 $\mathcal H$ 在固定代数基底上是 D-finite，
因 $K,L$ 本来是 D-finite，乘积 $sKL\,\mathcal H'$ 及其导数
也会是 D-finite，与上段矛盾。
这仍只排除整条固定原函数的有限秩线性下降，
不排除 (23) 或完整指标另有可用的有限几何解释。

## 已证输入

- [R56](../results/R56-ordinary-period-free-hurwitz-limit.md)：
  普通完整无周期证书及其误差界。
- [R62](../results/R62-actual-euler-primitive-stokes-constants.md)：
  惰性相邻整数比证书及完整导数极限。
- [R66](../results/R66-full-weight-one-and-fixed-division-unit-model.md)：
  实际系数 (1)、两类首层整除及全权一规范。
- [R68](../results/R68-integral-crystalline-frobenius-and-exact-critical-comparison.md)：
  真实整 $U_p,V_p$ 和 (10) 的准确阶数。
- [固定 torsor 原函数](2026-11-12-fixed-period-torsor-primitives-and-residues.md)：
  (2)–(3) 的固定有理偏连接及范围。
