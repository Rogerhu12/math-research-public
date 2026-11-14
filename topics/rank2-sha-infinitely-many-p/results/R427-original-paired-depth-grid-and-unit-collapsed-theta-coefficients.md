# R427 — 原对内等深网格与完整 Theta 聚合单位系数

日期：2026-11-14。**状态：已证明。** R339 的实际非零深域可以限制到
更小的真实网格：五个无权深输入共用一个深度，每个原 Theta 对内
两个 sigma 输入共用一个深度。仍取原
$m=\lceil((p-7)/6)/2\rceil$，只需 $1+m$ 个独立深度。
每个任意深的这种完整网格中，都有原 $S$ 的真实中央导数非零域。
证明支付对内指数碰撞，包括 $13+1$ 与 $7+7$ 的完整相加；没有
假定固定负五次矩非零。原完整中央零到这些域的运输仍须另证。

## 1. 原来源和指定实际输入域

保持 R339 的 $E_b:y^2=x^3+b$、$b=17$、原 sigma、
$\Theta=x\sigma^2$、周期 $\Omega=\Omega_p$ 和普通素数
$$
p>7,\qquad p\equiv1\pmod6,\qquad p\ne17.
$$
原固定目标是
$$
S=-\frac1{84}\sigma(z)\sigma(2z)\sigma(\delta z)
 \sigma(2\delta z)\sigma(\gamma z)\sigma(\bar\gamma z),
\quad\delta^2=-3,\quad\gamma=(5+\delta)/2.
\tag{1}
$$
用原 $\sigma(\delta z)=\delta\sigma(z)\Theta(z)$ 展开指定的
$\sigma(2z)$：
$$
\sigma(2z)=\delta^m\sigma(2\delta^{-m}z)
                   \prod_{h=1}^m\Theta(2\delta^{-h}z).
\tag{2}
$$
因此以下一直是 R339 的同一个原输入表示，没有换成 R424 中一个
只有相同边际的新联合。

保留尺度一的原 sigma 输入 $x_0$ 为指定单位输入。
五个不带二次权的深输入为 $X_1,\ldots,X_5$，尺度
$$
(c_1,\ldots,c_5)=(\delta,2\delta,\gamma,\bar\gamma,2\delta^{-m}).
$$
第 $h$ 个原 Theta 对的两个 sigma 输入为 $X_{h,+},X_{h,-}$，
尺度 $q_h=2\delta^{-h}$。原二次权和系数保持为
$$
Q_m=\Omega^{-2m}\prod_{h=1}^m
 \left(X_{h,+}X_{h,-}-\frac{X_{h,+}^2+X_{h,-}^2}{2}\right),
\qquad C_m=-\delta^m/84.
\tag{3}
$$
原输出是
$$
Y=x_0+\sum_{i=1}^5c_iX_i+
                 \sum_{h=1}^m q_h(X_{h,+}+X_{h,-}),
\tag{4}
$$
其完整测度为 $C_mY_*(Q_m\nu_\sigma^{\otimes(6+2m)})$。

给整数 $n,r_1,\ldots,r_m\ge1$，只考虑准确域
$$
\boxed{\mathcal D_{m;n,\boldsymbol r}=
\{x_0\in\mathbf Z_p^\times,\ X_i\in p^n\mathbf Z_p\ (1\le i\le5),\
 X_{h,+},X_{h,-}\in p^{r_h}\mathbf Z_p\ (1\le h\le m)\}.}
\tag{5}
$$
每个深输入都保留：五输入共用 $n$，每对共用 $r_h$，不同对之间
仍可独立。$Y$ 在此域自动为单位。
令 $J_{m;n,\boldsymbol r}(u)$ 是原 principal 测试在 (5) 上的完整函数。
这些域的质量为零，因五个无权深 sigma 输入各自质量为零。

## 2. 对内等深的完整 Theta 返回

沿 R316、R339，sigma 的实际 full core 为
$$
\nu_\sigma|_p=\lambda_\sigma[\kappa]_*\nu_\sigma,\qquad
\lambda_\sigma=\varepsilon^3/\bar\pi,\quad
\kappa=p/\bar\pi^2,\quad t_\sigma=\lambda_\sigma\kappa.
$$
$\lambda_\sigma$ 为单位、$v_p(\kappa)=1$，不与 R423 的原目标
core 符号 $\lambda$ 混用。

原两 sigma 的带权恒等式为
$$
\nu_{\Theta(qz)}=\frac1{\Omega^2}\{q(X+Y)\}_*
 \left(\left[XY-\frac{X^2+Y^2}{2}\right]\nu_\sigma(X)\nu_\sigma(Y)\right).
\tag{6}
$$
若同时把这一对限制在 $p^r$ 内，sigma core 使权多项式也乘
$\kappa^{2r}$。因此完整返回准确为
$$
\boxed{t_\sigma^{2r}\,\nu_{\Theta(q\kappa^r z)}.}
\tag{7}
$$
式 (7) 指两个原 sigma 输入同时深，不是只把 Theta 的相加输出
限制在 $p^r$；两种域不能混用。

定义 $d=p-1$ 及在 $(p\mathcal O)^{1+m}$ 上的解析函数
$$
\begin{aligned}
\mathcal G_m(T,U_1,\ldots,U_m)
={}&C_md\left(\prod_h U_h^2\right)
\int_{x_0\in\mathbf Z_p^\times}\int
 \log_p\left\langle x_0+T\sum_{i=1}^5c_iX_i
                          +\sum_hq_hU_hZ_h\right\rangle\\
&\hspace{10mm}d\nu_\sigma(x_0)
       \prod_{i=1}^5d\nu_\sigma(X_i)\prod_hd\nu_\Theta(Z_h).
\end{aligned}
\tag{8}
$$
每个 Theta 输入都是完整测度；前面的 $U_h^2$ 是其原二次权的
缩放，不能省掉。(6)、(7) 给原实际域的完整公式
$$
\boxed{J'_{m;n,\boldsymbol r}(0)
=\lambda_\sigma^{5n+2\sum_h r_h}
 \mathcal G_m(\kappa^n,\kappa^{r_1},\ldots,\kappa^{r_m}).}
\tag{9}
$$
常数 $\log_p\langle x_0\rangle$ 被五个无权 sigma 的零质量杀掉。
其余 log 级数第 $R$ 项的估计为 $-v_p(R)$ 加固定常数，所有变量
在 $p\mathcal O$，故 (8) 完整收敛并允许逐项积分、求系数。
没有截断高尾或删除未选中的 Theta 对。

## 3. 对内碰撞后的两个实际单位系数

记 $\Theta(z)=\sum_{k\ge0}\theta_{6k}z^{6k}$。
实际微分方程和原 sigma 规范给
$$
x=z^{-2}-\frac b7z^4+\frac{b^2}{637}z^{10}+O(z^{16}),\qquad
\log(\sigma/z)=\frac b{210}z^6-\frac{b^2}{84084}z^{12}+O(z^{18}).
$$
完整相乘 $x\sigma^2$，得到
$$
\boxed{\theta_0=1,\qquad\theta_6=-\frac{2b}{15},\qquad
\theta_{12}=\frac{4b^2}{17325}.}
\tag{10}
$$
最后一项的完整有理计算是
$$
\frac1{637}-\frac1{735}+\frac1{22050}-\frac1{42042}
=\frac4{17325}.
$$

这也精确支付了 R339 的全部对内索引碰撞。
原权聚合因子 $B(r,t)=(r+t-(r-t)^2)/2$ 满足
$$
B(1,1)=1,\quad B(7,1)=-14,\quad B(7,7)=7,\quad B(13,1)=-65.
$$
原 sigma 对应系数为 $1,b/210,-b^2/1801800$，所以
$$
2(-14)\frac b{210}=-\frac{2b}{15},
$$
$$
\boxed{2(-65)\left(-\frac{b^2}{1801800}\right)
             +7\left(\frac b{210}\right)^2=\frac{4b^2}{17325}.}
\tag{11}
$$
后式包括 $(13,1),(7,7),(1,13)$ 三项，不能只留下 $7+7$。

由于 $17325=3^2\cdot5^2\cdot7\cdot11$，而 $11\equiv2\pmod3$
不是当前普通素数，(10) 的三个系数对全部本篇 $p$ 都是单位。
中间有理展开的 $13$ 分母已在完整 (11) 中相消，不能据中间式
错误地排除 $p=13$。

## 4. 更小真实网格的明确单位系数

置
$$
K=(p-7)/6,\qquad m=\lceil K/2\rceil.
\tag{12}
$$
选择 $k_h\in\{1,2\}$、$\sum_hk_h=K$：$K$ 偶时全部取二，
$K$ 奇时一对取一、其余取二。
更一般可取更大 $m$、允许 $k_h=0$，只须总和仍为 $K$。

考虑同一个明确系数
$[T^5\prod_hU_h^{2+6k_h}]\mathcal G_m$。
五个 sigma 正矩都从指数一开始，所以 $T^5$ 只有五个指数全为一
这一种选择。第 $h$ 个 Theta 正矩指数是 $6k_h$；没有其他项能
贡献显示的多重指数。总 log 次数准确为
$R=5+6\sum_hk_h=p-2$，是奇数。
又有
$$
C_m\prod_{i=1}^5c_i
=\left(-\frac{\delta^m}{84}\right)(-84\delta^{-m})=1.
$$
将 log 的完整多项系数和 Theta 的阶乘矩相消，得到
$$
\boxed{
[T^5\prod_hU_h^{2+6k_h}]\mathcal G_m
=d(p-3)!\,I_{-(p-2)}\,\Omega^{p-2}
                  \prod_hq_h^{6k_h}\theta_{6k_h}.}
\tag{13}
$$
对允许 $k_h=0$ 的未选对，$\theta_0=1$，但实际 $U_h^2$、原域条件
及 (9) 的完整 core 系数仍保留，没有删除这些输入。

R339 的同一个原负矩满足
$I_{-(p-2)}\equiv(1-t_\sigma)\Omega\pmod p$，所以是单位。
$d,(p-3)!,q_h,\Omega$ 都为单位，(10) 已付所有 $\theta_{6k_h}$。
因此
$$
\boxed{[T^5\prod_hU_h^{2+6k_h}]\mathcal G_m\in\mathcal O^\times.}
\tag{14}
$$
这是一条对全部显示普通素数的证明，不是扫描，也不要求固定
$I_{-5}$ 的非零假设。

## 5. 每个任意深的成对网格都有原非零中央域

**定理。** 对每个当前普通 $p$ 和 (12) 的 $m$，任意 $n_0\ge1$，
都存在 $n,r_1,\ldots,r_m\ge n_0$，使准确域 (5) 满足
$$
\boxed{J'_{m;n,\boldsymbol r}(0)\ne0.}
\tag{15}
$$

证明：否则 (9) 的非零 core 因子使 (8) 在整个笛卡尔网格
$\{\kappa^n:n\ge n_0\}^{1+m}$ 上为零。
固定其余网格坐标，第一变量的零点趋于盘内零点，故一变量解析
恒等定理使该方向恒零。依次处理其余 $m$ 个变量，得到整个
$\mathcal G_m$ 为零，与 (14) 的单位系数矛盾。证毕。

定理没有声称每一个深度选择都非零，也没有给随 $p$ 一致的有限
深度上界。它严格减少了需运输的条件：五输入整体等深，每个
Theta 对内等深，只有这些块之间仍需独立深度。
指定原 $x_0$ 始终为单位，原二次权、尺度、完整输出及全部深输入
均与 R339(7) 相同。

## 6. 与原中央及 H 接口的范围

R424 已把原 $S$ 的中央零准确传入 $H$ 上任意完整第二输出测试，
并给原 sigma／Theta 的实际卷积因子。
要用 (15) 排除原中央零，仍须将 (5) 的这些**原隐藏输入域**合法
送到该控制中；只知道相同 $Y$ 边际，不能替换完整联合。
新网格适配 Theta 对的同步深度条件，但本篇没有据此假定所有
Hadamard 或 CM 变换都保持其输出和二次权。

脚本 check-original-paired-depth-unit-grid.py 及同名 JSON 核定固定
的全部对内碰撞、(10)、(11) 和分母因式；不扫描目标素数。

- [R339：原 norm-three 输入、多深度函数及负矩单位](R339-original-normthree-depth-family-and-a-unit-negative-moment-coefficient.md)。
- [R316：同一原 sigma/Theta 测度与 full core](R316-jzero-low-degree-original-cores-and-complete-four-factor-carry.md)。
- [R424：实际 H 因式与完整第二输出条件中央返回](R424-original-half-period-bezout-kernel-and-complete-central-disintegration.md)。

