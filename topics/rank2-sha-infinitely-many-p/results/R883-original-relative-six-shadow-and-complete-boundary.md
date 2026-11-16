# R883 — 原 Frobenius shadow 的相对六倍实现及完整边界

日期：2026-11-16。

**状态：以下是同一原循环的完整符号恒等式和有限闭点算法。它不预报两份原特征零坐标证书已经成功，也未计算出一个非零 shadow。所有实际消费均须先具备 R878 与 R870/R874 原 PASS 回执。**

本篇把 R880(A5) 的每一条真实求交推到原中央三阶商上。它不省略 cusp、映射极点、三挠点、交点高重数或剩余域迹；这些边界在下面的精确公式中全部处理。六倍商只是原 R882 的同源实现，不改变原端点、Artin 权或 CM 符号。

## 1. 原六倍商与实际观察

令 $k=\mathbf F_{r^2}$，$r=29$ 或 $41$，$E_0:y^2=x^3+1$，固定原 $\omega\in k$。原源为
$$
X=X_0(10404)_k,\qquad B=X_0(867)_k,\qquad
q:X\longrightarrow Y=X/\langle R\rangle=X_0(3468)_k .
\tag{1}
$$
它们使用 R882 的相同 $T,U,V$ 和原 cusp。写
$$
v_s=y_s^2-1,\qquad x_s^3=v_s,\qquad R(x_s)=\omega x_s,\quad R(y_s)=y_s.
$$
则 $Y/B$ 的完整相对六次方程为
$$
\boxed{
y_s^2(y_s^2-9)^2-T(y_s^2-1)^2=0.
}
\tag{2}
$$
这里 $X/Y$ 的函数域由 $x_s^3=v_s$ 给出。始终取光滑正规化及 R882 的原分支；没有把奇异平面模型的点直接当作原曲线点。

固定 R880(A5) 的一个完整点因子 Artin 标签 $\sigma$ 和两个端点标签 $a,b$。记
$$
A=\overline{\mathcal A}_b^{\,\sigma}q_2,\qquad
B_r=\varphi_r\overline{\mathcal A}_a^{\,\sigma}q_0,\qquad
F=\overline F^{\,\sigma}.
\tag{3}
$$
为免与基曲线 $B$ 混淆，第二求交映射写作 $B_r$。
原三阶等变性准确给
$$
A R=[\omega]A,\qquad B_rR=[\omega^2]B_r,\qquad F R=[\omega]F.
\tag{4}
$$
因此存在 $L=k(Y)$ 中的真实函数 $a_0,c_0,y_1,y_2,f_0,y_F$，使
$$
x_A=x_s a_0,\quad x_{B_r}=x_s^2c_0,\quad
y_A=y_1,\quad y_{B_r}=y_2,\quad
x_F=x_sf_0,\quad y_F=y_F.
\tag{5}
$$
这里 (5) 的 $a_0,c_0$ 是函数，不是端点下标。
令
$$
g=y_1-y_2,\qquad
D=(A-B_r)^*[O].
\tag{6}
$$
原次数分别为 $\deg A=2256$、$\deg B_r=2256r$，故两映射不可能具有相同 $y$ 函数，$g\ne0$。同样 $A-B_r$ 非恒定。

## 2. 完整推前除子，不只仿射零点

在 $E_0\times E_0$ 上有 Cartier 除子恒等式
$$
\operatorname{div}(y(P)-y(Q))
=
\sum_{j=0}^2\Gamma_{[\omega^j]}
-3(\{O\}\times E_0)-3(E_0\times\{O\}).
\tag{7}
$$
一般点处，$y(P)=y(Q)$ 的三个分支恰是 $P=[\omega^j]Q$，各重数1；两个极轴上的极阶各为3。这确定整个除子，包含它们在 $(O,O)$ 和 $x=0$ 处的相交，不能只在仿射开集解释 (7)。

拉回到 $X$。这些映射不把整条源送进 (7) 的任一分量，故 Cartier 拉回合法。记 $D_j=(A-[\omega^j]B_r)^*[O]$，则
$$
\operatorname{div}_X(g)
=\sum_{j=0}^2D_j-3A^*[O]-3B_r^*[O].
\tag{8}
$$
$R$ 循环置换三个 $D_j$，所以 $q_*D_j=q_*D$。
又 $y_1,y_2,g$ 全在 $L$ 中，而
$3A^*O=q^*\operatorname{pole}_Y(y_1)$、
$3B_r^*O=q^*\operatorname{pole}_Y(y_2)$。
把 (8) 推到 $Y$ 并除以3，得到完整等式
$$
\boxed{
E:=q_*D
=\operatorname{div}_Y(g)
 +\operatorname{pole}_Y(y_1)+\operatorname{pole}_Y(y_2).
}
\tag{9}
$$
特别 $E$ 有效。虽然右侧使用两个亚纯函数的除子，但它已包括所有极点和 cusp；它不是只取 $g$ 的零除子。

由于 $y:E_0\to\mathbf P^1$ 次数为3，
$$
\deg\operatorname{pole}_Y(y_1)=\deg A=2256,\quad
\deg\operatorname{pole}_Y(y_2)=\deg B_r=2256r.
$$
因此
$$
\boxed{\deg E=2256(r+1)=67680\ (r=29),\quad 94752\ (r=41).}
\tag{10}
$$
这也是原 $D$ 的总次数。完整 $x(A-B_r)$ 极除子的次数为其两倍，各极重为偶数。实际实现可独立核 (9) 有效和 (10)，不以部分点列表代替此门。

## 3. 分歧点的真实贡献

令 $Q$ 为 $E$ 的一个闭点，$\nu=\operatorname{ord}_Q$，$e_Q=E(Q)$。
若 $3\nmid\nu(v_s)$，Kummer 覆盖 $x_s^3=v_s$ 在 $Q$ 处全分歧。每个几何剩余点上唯一的源点由 $R$ 固定。
由 (4)，
$$
[1-\omega]F(P)=O.
$$
所以这些点的像在三挠子群中。无论交重及剩余域迹为何，其全部贡献在乘6之后严格为零：
$$
\boxed{[6]\,\operatorname{Alb} F_*(D|_{q^{-1}(Q)})=O.}
\tag{11}
$$
这不是删去边界：$e_Q$ 仍计入 (9)、(10)，只是其输出像由已付原 CM 等变性消去。

## 4. 非分歧点的共同交重和唯一剩余提升

现在设 $\nu(v_s)=3s$，$s\in\mathbf Z$。任选当地参数 $\pi_Q$，写
$$
X'=x_s/\pi_Q^s,\quad v'=v_s/\pi_Q^{3s},\qquad
a'=\pi_Q^sa_0,\quad c'=\pi_Q^{2s}c_0.
$$
$v'$ 为单位，三个几何提升的 $X'$ 残值相差 $\omega$，且
$$
x_A=X'a',\qquad x_{B_r}=X'^2c'.
\tag{12}
$$
记 $\nu_a=s+\nu(a_0)$、$\nu_c=2s+\nu(c_0)$。
共同交重 $m_Q$ 精确定义如下：

1. 若 $\nu(y_1)<0$、$\nu(y_2)<0$，两映射均落在 $O$。置
   $$
   m_Q=\min\{-\nu(y_1)/3,\ -\nu(y_2)/3\}.
   \tag{13}
   $$
   两个商均为整数，因为当前覆盖非分歧且 $y$ 的极阶为3。

2. 若两映射均有限且 $\nu_a>0,\nu_c>0$，在 $E$ 的支持上它们落在同一个 $(0,\pm1)$；置
   $$
   m_Q=\min\{\nu_a,\nu_c\}.
   \tag{14}
   $$
   若两个符号不同，则 $g$ 为单位且 $e_Q=0，不会出现在本步骤。

3. 其余情形置 $m_Q=0$。

这三个数是每个几何提升上的共同最小交重。证明在 $O$ 用形式参数 $-x/y$，在 $(0,\pm1)$ 用局部参数 $x$；在后者 $dx=2y\,\omega_0$ 的系数为单位。若两首阶不同，三个提升的交重完全相同。若首阶相同，三个首系数随提升乘不同的三次根，至多一个提升发生首项相消；在那个提升上还可有任意高阶相消，下面完整保留。

令
$$
\boxed{k_Q=e_Q-3m_Q\ge0.}
\tag{15}
$$
$k_Q$ 是唯一可能的额外交重，而不只是一次横截的指标。
若 $k_Q=0$，原三个提升的共同部分经 $F$ 推前之和为
$$
[1+\omega+\omega^2]\,(\text{一个像点})=O.
\tag{16}
$$
即使三个提升在剩余域上组成不可分开的闭点轨道，完整剩余域迹仍为同一三项和；不要求这三个点各自在 $\kappa(Q)$ 中有理。

若 $k_Q>0$，则准确有 $\nu_a=\nu_c$，且额外的那个提升由
$$
\overline{X'}=\overline{a'/c'}
\tag{17}
$$
唯一确定。这个根就在 $\kappa(Q)$ 中；它满足
$(\overline{a'/c'})^3=\overline{v'}$，故该唯一提升的剩余次数为1。
在 $O$ 的情形，额外交重要求 $y_1,y_2$ 的主项相同，所以使用 $x$ 比值的 (17) 与形式参数比值的选择相同；没有在两个极点处用未定义的仿射坐标相减。

其精确高交重仍为 (15)：由 (8) 的当地长度等式，三个交重的和是 $e_Q$，另两个已等于 $m_Q$。这既证明 $k_Q\ge0$，也支付所有高阶相消而无需任意截断。

## 5. 输出点不需要再开三次域

在唯一额外提升上，由 (5)、(17) 得到实际输出点
$$
\boxed{
P_Q=
\operatorname{red}_Q\left(\frac{a_0f_0}{c_0},\,y_F\right)
\in E_0(\kappa(Q)).
}
\tag{18}
$$
若 $\nu(y_F)<0$，右侧按射影延拓定义为 $O$；否则两个坐标均整且满足原椭圆方程。
式(18)中的当地参数完全相消，因此不需要选 $\pi_Q$、另取三次根或改换原 CM 分支。

结合前三节，
$$
\boxed{
[6]\,S_r(Z_{ab}^{\sigma})
=\sum_{\substack{Q\in\operatorname{Supp}E\\
                 3\mid\nu_Q(v_s),\ k_Q>0}}
 k_Q\,
 \operatorname{Tr}_{\kappa(Q)/k}\bigl([6]P_Q\bigr).
}
\tag{19}
$$
这里 $S_r$ 和 $Z_{ab}^\sigma$ 的轴次序正是 R880(28)/(A5)。
(19) 逐个保留闭点次数与交重。输出在 $E_0(k)$，再按 $r=29$ 的真 $E_0[5]$ 基或 $r=41$ 的真 $E_0[7]$ 基取坐标。
它随后输入原18×9系数消费器；不能先将 Artin 或双轴 Fourier 平均变成几何有限域 Frobenius。

## 6. 同一六倍域中的端点函数

为了使 (19) 可直接实现，不必先构造全十八倍域再下降。
在 (2) 上置 $v_s=y_s^2-1$、
$$
N_0=5v_s+8-y_s(v_s-8).
$$
原两个 level3 端点准确为
$$
T_0=N_0^3/v_s^4-27,\qquad
T_2=(v_s-2)^3/v_s-27.
\tag{20}
$$
它们分别等于 $B_0^3-27$、$B_2^3-27$，原标签由 R882 的 cusp 固定。
用同一 $\Phi_{17}^{(3)}$ 与标准 level3 的二次 Hecke 方程 $\Phi_2^{(3)}$，
逐级取完整线性 gcd：
$$
\begin{aligned}
U_i&=\text{唯一共同根}\{
 \Phi_2^{(3)}(U,Z),\ \Phi_{17}^{(3)}(T_i,Z)\},\\
V_i&=\text{唯一共同根}\{
 \Phi_2^{(3)}(V,Z),\ \Phi_{17}^{(3)}(U_i,Z)\},
 \qquad i=0,2.
\end{aligned}
\tag{21}
$$
这是两个 coprime Hecke 边的原平行运输；一般点上原17方向和2方向独立，故只有这个共同根。CM 特殊点处出现的相撞由已先在函数域求出的原函数延拓，不重新按特殊点选根。

若使用 R882 附A 的 eta48 模型，端点 $t_i$ 用同一所选绝对方程和
$t_i^{12}=T_i/V_i$ 的完整线性 gcd 恢复。
因为 $k(B)=k(T,V)=k(t,T)$，两者给出相同原函数域嵌入；
不能仅从12次方程任取一个根。

对一条原共轭 P，在相应端点读 $Y_i,R_i,v_{\rm new},d_{\rm new}$ 后，
$$
\begin{aligned}
x(\mathcal A q_0)/x_s
 &=\frac{N_0^2}{v_s^3}\frac{R_0}{d_{\rm new}^2},\\
x(\mathcal A q_2)/x_s
 &=\frac{(v_s-2)^2}{v_s}\frac{R_2}{d_{\rm new}^2},\\
y(\mathcal A q_i)&=2Y_i/v_{\rm new}+1.
\end{aligned}
\tag{22}
$$
因此在 (5) 中
$$
a_0=x(\mathcal A_bq_2)/x_s,\qquad
c_0=v_s^{(r-2)/3}\bigl(x(\mathcal A_aq_0)/x_s\bigr)^r.
\tag{23}
$$
原第一因子仍为
$$
f_0=\frac{v_s+4}{v_s}\frac{R_F}{\theta_{17}^2},\qquad
y_F=v_F/(\varepsilon\theta_{17}^3),\qquad
\varepsilon=-\frac{T\,y_s(v_s-8)v_s^3}{(v_s+4)^6}.
\tag{24}
$$
所有目标尺度、原 $F$ 和两条独立 P 角色都在 (22)–(24) 中。
这里只降低函数域实现的次数，没有把 $F$ 的 target 或任何全局类换掉。

## 7. 可执行次序和范围

实现只需：

- 从同一成功坐标回执及 R881 64位精度恢复实际 $v_F,R_F,Y_i,R_i$；
- 在原 eta48 基上构造 (2) 的相对六次域，再做该域的真实正规化；
- 用 (20)–(24) 得原两端点，逐个原 Artin/双轴标签计算完整 (9)；
- 核其有效性和 (10)，对全部闭点执行 (11)–(19)；
- 把所得真实 $[6]$ 点坐标交给原系数域的18×9读者，保显式 CM 符号。

不存在从未完成的特征零候选或一个模 $r$ ODE 解直接宣称映射的步骤。
本篇也不由任何有限闭点数目、形式恒等式或原循环所在动机的维数预告非零。
同一实际 Artin 组合非零时，才按 R880 附A和 R859 的整比较、全局无挠性返回原 $Z_{\rm orig}$ 的 Abel–Jacobi 非零。


## 附录 A：每个闭点完整迹的直接标量读法

这里的剩余域次数不能省去，但不需要逐次计算 d 个坐标 Frobenius。令

$$
 k=\mathbf F_{r^2},\qquad \ell=(r+1)/6\in\{5,7\},\qquad
 d=[\kappa(Q):k],\qquad P\in E_0(\kappa(Q)).
$$

[R859](R859-original-supersingular-shadow-and-integral-aj-detection.md) 使用的原算术 Frobenius 满足
$\varphi_r^2=[-r]$，是整个 $E_{0,\bar k}$ 上的端同态恒等式。因此

$$
\operatorname{Tr}_{\kappa(Q)/k}P
 =\sum_{j=0}^{d-1}\varphi_{r^2}^{\,j}P
 =\left[\frac{1-(-r)^d}{r+1}\right]P,
$$
以及

$$
\boxed{
 [6]\operatorname{Tr}_{\kappa(Q)/k}P
 =\left[\frac{1-(-r)^d}{\ell}\right]P.
}
\tag{A1}
$$

商是准确整数，可以为负。由 $P\in E_0(\mathbf F_{r^{2d}})$，

$$
[1-(-r)^d]P=O.
$$

所以 (A1) 的输出被 $\ell$ 消去；同时其 $r^2$-Frobenius 为
$[-r]$，在 $E_0[\ell]$ 上等于恒等，故输出确实在 $E_0[\ell](k)$。
这同时给实际实现两条应核条件：$\ell S=O$ 及 $S$ 的坐标在固定 $k$ 中。
它们不代替完整除子或原标签的检查。

正文 (19) 因而精确成为

$$
[6]S_r(Z_{ab}^{\sigma})
 =\sum_{\substack{Q\in\operatorname{Supp}E\\
                  3\mid\nu_Q(v_s),\,k_Q>0}}
 \left[k_Q\,\frac{1-(-r)^{d_Q}}{\ell}\right]P_Q.
\tag{A2}
$$

(A2) 先在每个实际 $\kappa(Q)$ 的椭圆曲线上乘准确整数，再将得到的固定域点读回同一 $E_0(k)$ 基。它包含全部 $d_Q$ 和 $k_Q$，不是把原 $P_Q$ 预先认作 $\ell$ 挠点，也不能先把 $d_Q$ 改成模 $\ell$ 的剩余类。

例如 $d=\ell$ 时，因 $v_\ell(r+1)=1$，整数
$1-(-r)^\ell$ 的 $\ell$ 赋值为 2。取在 $k_\ell$ 中的一个准确 $\ell^2$ 阶点，
(A1) 的输出有准确 $\ell$ 阶，而以 $d\bmod\ell=0$ 替代完整迹会错误地抹去它。
这些点确实存在，因为
$E_0(k_d)=E_0[\,|1-(-r)^d|\,]$，后者为与特征互素的全挠点核。
此例只是证明保留完整闭点次数的必要性，没有声称它已经出现在本课题的实际交点列表中。


## 附录 B：六倍正规化的全部分歧位置与几何数量

本节给原六倍域的结构性核对，所有点数均为几何点数；在 $k=\mathbf F_{r^2}$ 上用闭点表示时，应取剩余次数的总和，不能把它们误当作 $k$-有理点数。

[R882 附A](R882-original-degree18-source-model-and-two-endpoint-coordinates.md) 的原 cusp 表表明，$B=X_0(867)$ 有 36 个几何 cusp。$T$ 的零、极两边各有 18 个：一处阶 289，另外 17 处阶 1；每边总阶均为 306。记任一这样的阶为 $k_0\in\{1,289\}$。原 $B$ 的属为 85。

先看 $\mathbf P^1_y\longrightarrow\mathbf P^1_T$ 的六次映射

$$
T=\frac{y^2(y^2-9)^2}{(y^2-1)^2},\qquad
T+27=\frac{(y^2+3)^3}{(y^2-1)^2}.
\tag{B1}
$$

其完整分歧表为：

| T 值 | y 点 | 分歧指数 |
|---|---|---|
| 0 | 0、3、−3 | 各 2 |
| −27 | 两个 $y^2=-3$ 的点 | 各 3 |
| ∞ | 1、−1、∞ | 各 2 |

这些指数贡献 $3+4+3=10=2\cdot6-2$，已经支付整个有理曲线 Riemann–Hurwitz 数，因而无遗漏分歧。$r>3$ 时各显示点不同且指数均与特征互素。

在 $B\to X_0(3)$ 中，$T=-27$ 是目标的三阶椭圆点，其原像全部有局部次数 3。确实，$\Gamma_0(867)$ 无三阶椭圆稳定子：模 17 后这样的矩阵为三角矩阵，其特征值将给出 $\mathbf F_{17}^{\times}$ 中的非平凡三次单位根，而该群阶为 16。因此在正规化的基变换中，(B1) 在 $T=-27$ 的指数 3 完全消去。此论证及原 cusp 阶在所选好素数 $29,41$ 处保持。

在 $T=0,\infty$ 的每一个原 cusp，$k_0$ 都为奇数，所以与 (B1) 的指数 2 互素。每个 cusp 在 $Y$ 上恰有三个几何原像，每个指数 2。故

$$
\boxed{\operatorname{Ram}(Y/B)\text{ 恰支撑于全部原 cusp，}
\quad \deg\operatorname{Ram}(Y/B)=108.}
\tag{B2}
$$

由 Riemann–Hurwitz，

$$
2g(Y)-2=6(2\cdot85-2)+108=1116,
\qquad \boxed{g(Y)=559}.
\tag{B3}
$$

$Y$ 的几何 cusp 数为 $36\cdot3=108$。

再看 $X/Y$ 的 $x_s^3=v_s=y_s^2-1$。$v_s$ 只有在 $y_s=1,-1,\infty$ 才有零或极；这些点正是上述 $T=\infty$ cusp 的原像。对应一个 $B$ 上极阶 $k_0$ 的 cusp，三个 $Y$ 点上的 $v_s$ 阶准确为

$$
k_0,\quad k_0,\quad -2k_0.
\tag{B4}
$$

三个数均不被 3 整除。其余点的阶为 0。所以

$$
\boxed{X/Y\text{ 恰在 }18\cdot3=54\text{ 个几何 cusp 全分歧，}
\quad \deg\operatorname{Ram}(X/Y)=108.}
\tag{B5}
$$

这些正是正文 §3 的全部分歧点；它们的 F 像由原等变性落在 $\ker[1-\omega]$，六倍 shadow 贡献为零，但仍须计入完整除子次数。

最后，

$$
2g(X)-2=3(2\cdot559-2)+108=3456,\qquad
\boxed{g(X)=1729}.
$$

54 个分歧 cusp 各给一个 $X$ cusp，其余 54 个非分歧 cusp 各给三个，因此原 $X$ 有 $54+3\cdot54=216$ 个几何 cusp。这同时核对了相对六倍实现确实保留原 $X_0(10404)$ 的边界，没有把另一个光滑化或部分仿射分支当作源曲线。


## 附录 C：原端点交换与六个实际除子

本节仍须同两张原特征零地图已经通过认证。以下对实际映射的等式由 R882 的已识别坐标给出，不是对一个任意形式 ODE 解作同一假设。

### C.1 固定底的完整源自同构

在原十八倍源上定义

$$
 W(y_s)=\frac{y_s+3}{y_s-1},\qquad
 W(x_s)=\frac{2x_s}{y_s-1},\qquad W|_{k(B)}=1.
\tag{C1}
$$

直接代入 $y_s^2=x_s^3+1$ 与 $T$ 的原公式，得到 $W^2=1$ 且 $W(T)=T$，所以 (C1) 是同一个光滑正规化上的自同构，并下降到相对六次域。它固定 $T,U,V,t$，在 cusp 或显示分母为零处按这个自同构延拓。

写 $v_s=y_s^2-1$，则 R882 的

$$
 A=\frac{v_s+4}{x_s^2},\quad
 B_0=\frac{N_0}{x_s^4},\quad B_2=\frac{v_s-2}{x_s},
 \quad N_0=(y_s+1)(-y_s^2+6y_s+3)
$$

准确满足

$$
W(A)=A,\qquad W(B_0)=B_2,\qquad W(B_2)=B_0.
\tag{C2}
$$

例如
$N_0(Wy_s)=16(y_s+1)(y_s^2-3)/(y_s-1)^3$，除以
$W(x_s)^4$ 后恰为 $B_2$，并无遗漏的三次根相位。
原完整线性 Hecke gcd 随 (C2) 运输，所以两个端点的全部 $T_i,U_i,V_i,t_i,Y_i,R_i$ 都相交换。保 (22) 中的 $x_s$ 因子后，得到实际映射等式

$$
(\mathcal A_a q_0)W=\mathcal A_a q_2,\qquad
(\mathcal A_a q_2)W=\mathcal A_a q_0.
\tag{C3}
$$

第一因子中 $R_F,v_F$ 在固定底上，而
$y'=y_s(v_s-8)/v_s$ 满足 $W(y')=-y'$。故原 $\varepsilon=-Ty'/A^6$ 变号，
$x_F=A R_F/\theta_{17}^2$ 不变，$y_F$ 变号，即

$$
\boxed{FW=-F.}
\tag{C4}
$$

特别，运输 $x_s f_0$ 时必须保留 $W(x_s)/x_s=2/(y_s-1)$。
单独把 $f_0$ 的函数表达式作 $W$ 而不运输这个因子，会给错端点坐标。

### C.2 归一 Poincaré 交项的准确对称性

令 $L=\mathcal O_{E_0}(O)$，对两个 $X\to E_0$ 的映射 $C,D$ 写

$$
\mathcal Q(C,D)=(C+D)^*L-C^*L-D^*L\quad\text{于 }\operatorname{Pic}(X).
$$

这是由原点刚化的 Poincaré 双线性配对。它对称且在每个变量上可加；
对任一椭圆端同态 $\alpha$ 有
$\mathcal Q(C,\alpha D)=\mathcal Q(\alpha^\dagger C,D)$。
原 $r$-Frobenius 的对偶满足 $\varphi_r^\dagger=-\varphi_r$，
因为其迹为零且 $\varphi_r^2=[-r]$。

令 $C_a=\mathcal A_aq_0,\ D_b=\mathcal A_bq_2$，并将本正文实际除子归一为

$$
\mathcal N_{ab}=(D_b-\varphi_r C_a)^*L-D_b^*L-(\varphi_r C_a)^*L
              =-\mathcal Q(D_b,\varphi_r C_a).
\tag{C5}
$$

由 (C3) 及上述对偶恒等式，完整 Picard 类满足

$$
\begin{aligned}
 W^*\mathcal N_{ab}
 &=-\mathcal Q(C_b,\varphi_r D_a)
 =\mathcal Q(\varphi_r C_b,D_a)\\
 &=-\mathcal N_{ba}.
\end{aligned}
\tag{C6}
$$

这包含全部极点与交重；使用的是整个线束类，未删掉仿射外的分量。
由 (C4)，对任何除子类 $Z$，

$$
\operatorname{Alb}F_*W^*Z=-\operatorname{Alb}F_*Z.
$$

将它用于 (C6)，得到
$\operatorname{Alb}F_*\mathcal N_{ab}=\operatorname{Alb}F_*\mathcal N_{ba}$。

还要支付 (C5) 中减去的两条轴。任一轴除子 $Z$ 在原 $R$ 下不变，
因为 $C_aR=[\omega]C_a$、$(\varphi_r C_a)R=[\omega^2]\varphi_r C_a$，
而 $O$ 被两者固定。于是
$\operatorname{Alb}F_*Z=[\omega]^{-1}\operatorname{Alb}F_*Z$。
其像被 $1-\omega$ 消去，因此被 3 消去，六倍后严格为零。
故对正文的完整点 $P_{ab}=\operatorname{Alb}F_*(D_b-\varphi_r C_a)^*O$，

$$
\boxed{p_{ab}:=[6]P_{ab}=p_{ba}.}
\tag{C7}
$$

(C7) 是原完整输出点的等式，不是宣称两个有效交点除子本身相同。
实现可只算三个对角和三个无序非对角标签；三个对角项仍然保留。

### C.3 同原角色读数的六除子形式

将 (C7) 代入 [R880(C10)](R880-original-three-artin-conjugates-and-integral-double-axis-shadow.md)，得到

$$
\boxed{
[6]\mathscr S_{jk,\chi_{jk}}
=\frac19e_\omega\left(
 \sum_{a=0}^2(\zeta_j\zeta_k)^a p_{aa}
 +\sum_{0\le a<b\le2}
   (\zeta_j^a\zeta_k^b+\zeta_j^b\zeta_k^a)p_{ab}
 \right).
}
\tag{C8}
$$

原三个有序角色对仍为 $(0,1),(1,2),(2,0)$，CM 符号和系数域照旧。
(C8) 不删原 Artin 条件，只用已证明的源自同构和归一配对消除重复的实际求交。
每个所计算的除子仍须按本正文处理全部闭点、边界和高交重。


## 附录 D：所选常数域反射与四个实际除子

本节继续假定原两份坐标证书成功，使用 R880 的同一个 \(h,\theta_{17},P,\mathcal A_0,\mathcal A_1,\mathcal A_2\)。它减少重复求交；不把有限域的反射施到角色系数上，也不截短任何闭点迹。

### D.1 必须区分复共轭和本位的常数反射

令 \(c_\infty\) 为原实嵌入所定的全局复共轭。原 \(h\) 取实值，R869 已付 \(P\) 在实嵌入的 \(F=\mathbf Q(\sqrt[3]{17})\) 上下降，所以
$$
 c_\infty(\kappa P)=\kappa P,\qquad
 c_\infty\sigma c_\infty=\sigma^{-1}.
 \tag{D1}
$$
这里 \(\sigma\) 是 R880(C1) 的真实九阶元。
全局实数 \(\theta_{17}\) 被 \(c_\infty\) 固定；不能据此给本位 \(F\) 的反射号。

在本题所选 \(r=29,41\) 的几何嵌入中，取 \(a_0^3=17\) 的唯一
\(\mathbf F_r\) 根，以及 \(h_0^3=2^{32}v(a_0)\) 的唯一
\(\mathbf F_r\) 根。两个立方根唯一是因为 \(\gcd(3,r-1)=1\)。
这正是已固定实原模型的一种好位约化，不另改原余循环。
由二次互反律，
$$
 (17/29)=-1,\qquad (17/41)=-1.
$$
而 \(a_0^3=17\) 给 \((a_0/r)=(17/r)\)，故
$$
 \theta_{17}^{\,r}=-\theta_{17}.
 \tag{D2}
$$
因此本位常数反射 \(\jmath:z\mapsto z^r\) 在原 \(H_{34}\) 的约化上对应
\(c_\infty\epsilon\)，而不是 \(c_\infty\)；\(\epsilon\) 固定 \(H_9\) 并改变
\(\theta_{17}\) 的符号。它在 \(H_9\) 上仍给(D1)的反射。

把常数反射施于实际映射的全部系数，保持源参数不动，以横线记之。
原第一因子的规范和(D2)于是给
$$
 \overline F=-F.
 \tag{D3}
$$
对三条后因子，记
$$
 i^*=(-i)\bmod3,\qquad u_0=0,\quad u_1=u_2=-1,
 \qquad -i=3u_i+i^*.
$$
由(D1)及 \(\mathcal A_{i+3}=[\omega]\mathcal A_i\)，
$$
 \boxed{
 \overline{\mathcal A}_i=[\omega]^{u_i}\mathcal A_{i^*}.
 }
 \tag{D4}
$$
即
$$
 \overline{\mathcal A}_0=\mathcal A_0,\quad
 \overline{\mathcal A}_1=[\omega^2]\mathcal A_2,\quad
 \overline{\mathcal A}_2=[\omega^2]\mathcal A_1.
 \tag{D5}
$$
所有目标的 \(h/2048\)、\(\lambda(u)\) 尺度均在这些实际映射内。
(D4)不是只把三条未定首项的形式互换。实现可在真实相对六次函数域中，对常数作 \(z\mapsto z^r\)、固定 \(t_\eta,y_s\)，逐条核对(D3)–(D5)。

### D.2 先完成全部闭点迹，再用反射

仍写
$$
 p_{ab}=[6]\operatorname{Alb}\overline F_*
       (\overline{\mathcal A}_bq_2-\varphi_r\overline{\mathcal A}_aq_0)^*[O],
 \qquad 0\le a,b<3,
$$
这里的原几何约化横线在以下不再重复；(D3)中的横线则专指常数反射。
全部 \(p_{ab}\) 均在 \(E_0[\ell](\mathbf F_{r^2})\)。

对完整闭点零循环施 \(\jmath\)，其交重和剩余次数逐一保持，
且与剩余域迹相容。输出点上的动作就是实际
\(\varphi_r:(x,y)\mapsto(x^r,y^r)\)。
这里使用的是常数域的半线性共轭，不是把不可分的绝对 Frobenius 拉回除子后漏掉其重数。

在共轭后的求交映射中用(D4)，得到相对 CM 相位
$$
 j=2u_a-u_b\pmod3,
$$
因为 \(\varphi_r[\omega]^{u_a}=[\omega]^{2u_a}\varphi_r\)。
原源 \(R\) 的完整等式 \(R^*D_j=D_{j+1}\) 及
\(F_*R^{j*}=[\omega]^{-j}F_*\)，再连同(D3)，给
$$
 \boxed{
 \varphi_r(p_{ab})
   =-[\omega]^{-2u_a+u_b}p_{a^*b^*}
   =-[\omega]^{u_a+u_b}p_{a^*b^*}.
 }
 \tag{D6}
$$
两指数模3相同，所以(D6)也与附录C的 \(p_{ab}=p_{ba}\) 相容。

这一步的每个 \(p_{ab}\) 都先由正文(19)／附录A(A2)完成其全部
\(k_Q,d_Q\) 求和。没有把 \(d_Q\) 换成模 \(\ell\) 的类，也没有把
\(P_Q\) 先当作 \(\ell\) 挠点。

### D.3 四个求交、两个真实固定线检查

把(D6)与 \(p_{ab}=p_{ba}\) 展开：
$$
 \boxed{
 \begin{aligned}
 p_{02}&=-[\omega]\varphi_r(p_{01}),\\
 p_{22}&=-[\omega^2]\varphi_r(p_{11}),\\
 \varphi_r(p_{00})&=-p_{00},\\
 \varphi_r(p_{12})&=-[\omega]p_{12}.
 \end{aligned}}
 \tag{D7}
$$
因此只需实际分解
$$
 \boxed{(a,b)=(0,0),(0,1),(1,1),(1,2)}
 \tag{D8}
$$
这四个完整有效除子，便得到全部九个有序点。
每个所计算除子的次数仍准确为 \(2256(r+1)\)，全部边界按正文处理；
另外五项由(C7)、(D7)运输，并非给它们赋零。
(D7)末两式可作为真实输出点的两项相容检查。

如果用固定 \(E_0[\ell]\) 基，令 \(M\) 为原 \([\omega]\) 的矩阵，
\(C\) 为实际 \(\varphi_r\) 的矩阵，则
$$
 C M=M^2C,\qquad C^2=(-r)I=I\quad\text{于 }\mathbf F_\ell.
 \tag{D9}
$$
最后的等号只用于已经得到的 \(\ell\) 挠点，来自 \(r+1=6\ell\)。
它从不用于提前缩短附录A的整数 \((1-(-r)^{d_Q})/\ell\)。
实现由同一目标曲线的实际两个基点逐个计算 \(M,C\)，并核(D9)；
不以角色系数域上的 Frobenius 代替 \(C\)。

最后将按(D7)填全的九个点送入 R880(C10)，或完整填回十八项
Artin 消费器。系数 \(\zeta_j,\chi_{jk}\) 始终固定，
\(e_\omega\) 的使用顺序也保持。这里没有增加一个中央零假设，
没有改变原 \(Z_{\rm orig}\)，也没有预报这四个实际除子的输出是否非零。

## 附录 E：三个原角色读数与两个实际挠点障碍

本节在附录D的同一四个完整除子输出上，进一步消去检测阶段的冗余。
不再增加求交，不改变原三角色或原九阶Artin元；所有点仍先完成正文及附录A的全部闭点迹。
两原特征零证书及真实约化映射依旧是使用这些点的前提。

### E.1 系数域的三次扩张与几何 CM 分开

记
$$
(r,\ell)=(29,5)\ \text{或}\ (41,7),\qquad
V_\ell=E_0[\ell](\mathbf F_{r^2}),
$$
并令几何算子
$$
\rho=[\omega]\big|_{V_\ell},\qquad
\Phi=\varphi_r\big|_{V_\ell}.
$$
附录D已付
$$
\rho^2+\rho+1=0,\qquad
\Phi\rho=\rho^2\Phi,\qquad \Phi^2=1.
\tag{E1}
$$
最后一个等式只作用在已经完成迹的实际 \(\ell\) 挠点上。

沿用R880的同一个系数CM符号，取
$$
k_\ell=
\begin{cases}
\mathbf F_{25},&\ell=5,\\
\mathbf F_7,&\ell=7,
\end{cases}
\qquad
\omega_\ell^2+\omega_\ell+1=0,\quad \omega_\ell\ne1,
$$
$$
e_\omega=\frac{\rho-\omega_\ell^2}{\omega_\ell-\omega_\ell^2},
\qquad
e_{\omega^2}=1-e_\omega.
\tag{E2}
$$
这些是在 \(V_\ell\otimes_{\mathbf F_\ell}k_\ell\) 上的两个互补投影；
\(\rho\) 是实际点的CM算子，\(\omega_\ell\) 是系数，二者不提前混同。

取原 \(\zeta\) 满足
$$
\zeta^3=\omega_\ell^2,\qquad
\zeta_j=\omega_\ell^j\zeta\quad(j=0,1,2).
$$
它是九阶根。因为 \(|k_\ell|=25\) 或 \(7\)，两者均为 \(7\bmod9\)，
而 \(9\nmid |k_\ell|-1\)，其最小多项式正是
$$
X^3-\omega_\ell^2.
$$
确实，若此三次多项式有 \(k_\ell\) 根，该根便有阶9，矛盾；
三次多项式没有根即不可约。因此
$$
[k_\ell(\zeta):k_\ell]=3,\qquad
1,\zeta,\zeta^2\ \text{在 }k_\ell\text{ 上线性无关}.
\tag{E3}
$$
这准确给原角色域 \(\mathbf F_{5^6}\) 或 \(\mathbf F_{7^3}\)，
没有把几何域 \(\mathbf F_{r^2}\) 认作角色域。

### E.2 同一个完整九项和的三个系数

令
$$
z_{ab}=e_\omega p_{ab}\in e_\omega(V_\ell\otimes k_\ell).
$$
由附录C，\(z_{ab}=z_{ba}\)。R880(C10)的归一原读数准确为
$$
\mathscr R_{jk}
=\frac19\sum_{a,b=0}^2\zeta_j^a\zeta_k^b z_{ab},
\qquad (j,k)=(0,1),(1,2),(2,0).
\tag{E4}
$$
这里 \(p_{ab}\) 已包含实际的6倍；完整十八项Artin和、\(1/162\)及两轴独立投影
已经由R880支付为(E4)，不再另乘或除一个6。

对 \(j\ne k\)，令 \(m=-j-k\bmod3\)，即剩余的第三指标。
定义三个同一CM线上的系数
$$
A=z_{00}-\omega_\ell^2z_{12},\qquad
B=-z_{01}+\omega_\ell^2z_{22},\qquad
C=z_{11}-z_{02}.
\tag{E5}
$$
则直接展开整个九项和得到
$$
\boxed{
9\mathscr R_{jk}
=A+\zeta\omega_\ell^m B+\zeta^2\omega_\ell^{2m}C.
}
\tag{E6}
$$

完整系数核对如下。因 \(j,k,m\) 两两不同，
$$
\omega_\ell^j+\omega_\ell^k=-\omega_\ell^m,\qquad
\omega_\ell^{2j}+\omega_\ell^{2k}=-\omega_\ell^{2m},
$$
$$
\omega_\ell^{j+k}=\omega_\ell^{2m},\qquad
\omega_\ell^{j+2k}+\omega_\ell^{2j+k}=-1.
$$
按 \(a+b=0,1,2,3,4\) 分组，前三级分别给
\(z_{00}\)、\(-\zeta\omega_\ell^m z_{01}\)、
\(\zeta^2\omega_\ell^{2m}(z_{11}-z_{02})\)。
第四级为 \(-\zeta^3z_{12}=-\omega_\ell^2z_{12}\)；
第五级为
\(\zeta^4\omega_\ell^{2j+2k}z_{22}
=\zeta\omega_\ell^{m+2}z_{22}\)。
合并恰为(E6)，包括三个对角项。

由(E3)，对任意一个原指定pair，
$$
\boxed{
\mathscr R_{jk}=0
\ \Longleftrightarrow\ A=B=C=0
\ \Longleftrightarrow\
\mathscr R_{01}=\mathscr R_{12}=\mathscr R_{20}=0.
}
\tag{E7}
$$
所以三个实际读数要么全部为零，要么全部非零。
这里用的是三次系数扩张的线性无关性，不是先将三个原角色合并。
等价地，固定 \(k_\ell\) 并令 \(\zeta\mapsto\omega_\ell\zeta\) 的系数自同构循环(E6)的三式。
这个系数自同构与几何 \(\Phi\) 是两种不同作用。

### E.3 两个真正的点，而非两个任取标量

现在只用附录D实际计算的四个点，定义
$$
\boxed{
\mathcal A=p_{00}-\rho^2p_{12},\qquad
\mathcal C=p_{11}+\rho\Phi(p_{01}).
}
\tag{E8}
$$
它们均为同一 \(E_0[\ell](\mathbf F_{r^2})\) 中的实际点。

为核完整三系数，暂记
$$
\mathcal B=-p_{01}+\rho^2p_{22}.
$$
由(D7)，
$$
p_{02}=-\rho\Phi(p_{01}),\quad
p_{22}=-\rho^2\Phi(p_{11}),\quad
\Phi(p_{00})=-p_{00},\quad
\Phi(p_{12})=-\rho p_{12}.
$$
结合(E1)，逐项得到
$$
\boxed{
\Phi(\mathcal A)=-\mathcal A,\qquad
\mathcal B=-\rho\Phi(\mathcal C),\qquad
A=e_\omega\mathcal A,\ B=e_\omega\mathcal B,\ C=e_\omega\mathcal C.
}
\tag{E9}
$$
第二式准确使用
\((\rho\Phi)^2=1\)：
\[
-\rho\Phi\bigl(p_{11}+\rho\Phi p_{01}\bigr)
=-\rho\Phi p_{11}-p_{01}.
\]
第一式使用 \(\Phi\rho^2=\rho\Phi\)，所以
\[
\Phi(p_{00}-\rho^2p_{12})
=-p_{00}+\rho^2p_{12}.
\]
所有运算都在已经完成原闭点迹的 \(\ell\) 挠点上。

(E1)还给
$$
e_\omega\Phi=\Phi e_{\omega^2},\qquad
e_{\omega^2}\Phi=\Phi e_\omega.
\tag{E10}
$$
若 \(e_\omega\mathcal A=0\)，由 \(\Phi\mathcal A=-\mathcal A\) 及(E10)，
$$
e_{\omega^2}\mathcal A=-\Phi e_\omega\mathcal A=0,
$$
所以 \(\mathcal A=0\)。反向显然。
若 \(e_\omega\mathcal C=0\) 且 \(e_\omega\mathcal B=0\)，(E9)–(E10)给
$$
0=e_\omega\mathcal B
=-\omega_\ell\Phi e_{\omega^2}\mathcal C,
$$
而 \(\omega_\ell\Phi\) 可逆，故 \(e_{\omega^2}\mathcal C=0\)，即 \(\mathcal C=0\)。
反向同样成立。这个证明也覆盖 \(\ell=7\) 的CM分裂情形；
没有误称一个单独的 \(e_\omega\) 在全部实际点上单射。

因此，完整原角色和的消失准确等价于两个实际点关系：
$$
\boxed{
\mathscr R_{jk}=0\ \text{对某个原pair}
\ \Longleftrightarrow\
\mathcal A=0\ \text{且}\ \mathcal C=0.
}
\tag{E11}
$$
非零的等价形式为
$$
\boxed{
\mathcal A\ne0\ \text{或}\ \mathcal C\ne0
\ \Longleftrightarrow\
\mathscr R_{01},\mathscr R_{12},\mathscr R_{20}\ \text{全部非零}.
}
\tag{E12}
$$
所以在实际四除子求交完成后，只需检查(E8)的两个真实挠点便可判定原读数非零。
完整十八项和与九项式仍可用同一实际基独立核对；(E11)没有替换其来源。

本节没有报告 \(\mathcal A\) 或 \(\mathcal C\) 已经算出。
若其一由同原公开执行证为非零，才可沿R859/R880的整shadow和无挠返回得到原有理类的非零。
固定 \(\ell\) 的这一步不单独证明主目标所需的无穷不同系数素数，
也不跳过后续通常全Selmer桥。

## 附录 F：按真实第一映射次数选择同一循环的较小求交

本附录仍只在两份原特征零映射证书成功后使用。不把未认证的
第一映射次数、Manin 常数或数据库线索作为输入。
所有点等式指正文已经固定的完整 $\ell$ 挠读数，
即先完成整个闭点迹、再乘6，$\ell=5$ 或7。

### F.1 缓存中已经可读的准确次数

固定一个原有序对 $(a,b)$，写
$$
f=\overline F,\qquad
g=\overline{\mathcal A}_a q_0,\qquad
h=\overline{\mathcal A}_b q_2.
\tag{F1}
$$
它们都是同一个 $X$ 到同一个 $E_0$ 的真映射，满足
$$
fR=[\omega]f,\qquad gR=[\omega]g,\qquad hR=[\omega]h.
$$
已有 $\deg g=\deg h=d=2256$。令 $d_f=\deg f$；
本附录不预先给 $d_f$ 赋数值。

正文实现已经缓存 $y_f\in k(Y)$ 的完整极除子。因为
$[k(X):k(Y)]=3$，而 $y:E_0\to\mathbf P^1$ 的次数也恰为3，
有
$$
\boxed{d_f=\deg\operatorname{pole}_Y(y_f).}
\tag{F2}
$$
等式包含全部有限点与 cusp，并按实际闭点次数计算。
它不要求另建 $X$ 的完整函数域、不用逐点数零点，
也不增加一次新的除子分解。由已认证映射在原 cusp 的
非零微分，$f$ 的约化非恒定，故 (F2) 是正整数。

### F.2 两个完整次数的精确比较

对任意满足同一三阶等变性的两个真映射 $a,b:X\to E_0$，
令 $\varphi=\varphi_r$。定义度数的整数双线性极化
$$
B(a,b)=\deg(a+b)-\deg a-\deg b.
$$
由源自同构 $R$、目标 $[\omega]$ 的度数不变性，以及
$\varphi[\omega]=[\omega^2]\varphi$，得
$$
B(a,\varphi b)=B([\omega]a,[\omega^2]\varphi b)
             =B(a,[\omega]\varphi b).
$$
再迭代一次并用 $1+\omega+\omega^2=0$，得到
$3B(a,\varphi b)=0$。因 $B$ 是整数，准确有 $B(a,\varphi b)=0$，
从而
$$
\boxed{\deg(a-\varphi b)=\deg a+r\deg b.}
\tag{F3}
$$
这里用的 Frobenius 是度数 $r$ 的真映射，不能替成常数域
反射或度数 $r^2$ 的 Frobenius。

R880(27)、(28) 已付原最高 Chow 块上三循环为 $+1$。
在同一个原 CM 符号及整 $\ell$ 读数中，它给
$$
\boxed{
p_{ab}
=[6]\operatorname{Alb}f_*(h-\varphi g)^*[O]
=[6]\operatorname{Alb}h_*(g-\varphi f)^*[O].
}
\tag{F4}
$$
同式在两个共轭 CM 符号上都成立，故为完整 $E_0[\ell]$ 的点等式。
这是同一 $p_{ab}$ 的两种计算，不是额外的中央零或另一条循环。
若在未投影的点式中先保留轴项，其差只属于原已付的
$2,3$ 初级部分；乘6后的 $\ell$ 读数按 R859/R880 正确返回。
尤其不能用有理化后挠点消失来证明 (F4)，这里使用的是
这些原结果在 $\mathbf Z[1/6r]$ 上的对应恒等式。

由 (F3)，(F4) 左、右两个 pullback 除子的完整次数分别是
$$
d(1+r),\qquad d+r d_f.
\tag{F5}
$$
因此以下选择完全由已经计算的真实数据决定：
$$
\begin{cases}
h_*(g-\varphi f)^*O,& d_f<2256,\\
f_*(h-\varphi g)^*O,& d_f\ge2256.
\end{cases}
\tag{F6}
$$
第二行保持现有实现；第一行准确把求交次数减少
$r(2256-d_f)$。它只保证除子的次数减少，不预言整个程序的运行时间。

### F.3 较小呈示仍在原相对六次域内

在 (F6) 第一行，写正文已构造的实际函数为
$$
x_g=x_s x_{a,0},\quad y_g=y_{a,0},\qquad
x_h=x_s x_{b,2},\quad y_h=y_{b,2},\qquad
x_f=x_s f_0,\quad y_f=y_F.
$$
则新的两个求交函数和输出函数准确为
$$
a_0^{\rm new}=x_{a,0},\qquad
c_0^{\rm new}=v_s^{(r-2)/3}f_0^r,\qquad
y_1^{\rm new}=y_{a,0},\quad y_2^{\rm new}=y_F^r,
\qquad
f_0^{\rm out}=x_{b,2},\quad y_{\rm out}=y_{b,2}.
\tag{F7}
$$
所以不再开任何扩域，整个有效除子就是
$$
E^{\rm new}
=\operatorname{div}_Y(y_{a,0}-y_F^r)
 +\operatorname{pole}_Y(y_{a,0})
 +r\operatorname{pole}_Y(y_F),
\quad
\deg E^{\rm new}=2256+r d_f.
\tag{F8}
$$
源 $R$ 仍在两个求交因子上分别作用 $\omega,\omega^2$，
在输出因子上作用 $\omega$。故正文(11)–(19)的全部证明
适用于 (F7)，包括三次分歧点的真实三挠输出、
共同 $O$ 或 $(0,\pm1)$ 交重、唯一额外提升及任意高相消。
该唯一提升上的实际输出为
$$
\operatorname{red}_Q
\left(
  \frac{x_{a,0}x_{b,2}}{v_s^{(r-2)/3}f_0^r},
  \ y_{b,2}
\right);
\tag{F9}
$$
输出极点按射影延拓取 $O$。每个闭点仍使用附录 A 的
完整整数 $(1-(-r)^{d_Q})/\ell$，不截掉剩余域次数。

最后，附录 C、D、E 的对称、反射与双点检测都是原完整
$p_{ab}$ 的恒等式，不依赖 (F4) 采用哪一种呈示。
因此仍只需要计算 $(0,0),(0,1),(1,1),(1,2)$ 四个完整除子，
保留原18项 Artin、双轴 Fourier、CM 符号和全部归一；
不会把 (F6) 的选择算成新的独立来源。


## 附录 G：用两个约化 Tate 读数准确恢复完整闭点 trace

本节仅替换附录 A 中每个剩余域点的大整数椭圆乘法。原四个完整除子、所有共同交重、
唯一额外提升、源上的相对三次分歧、两轴 Artin 系数以及附录 F 的可选呈示全部保持。
没有执行新的数值计算，也不预报任一原影子非零。

置
$$
(r,\ell)=(29,5)\ \text{或}\ (41,7),\qquad
k=\mathbf F_{r^2},\quad q=r^2,\qquad E=E_0:y^2=x^3+1 .
$$
正文及附录 A 已付整个几何端同态
$$
\pi=\operatorname{Frob}_{q}=[-r].
\tag{G1}
$$
故精确有
$$
E(k)=\ker(\pi-1)=E[r+1]=E[6\ell],
\qquad
E[\ell]\hookrightarrow E(k)/\ell E(k)
\ \text{是同构}.
\tag{G2}
$$
第二式使用 $\ell\nmid6$；它不是从 $\ell\mid\#E(k)$ 单独推出。

### G.1 固定底域上的配对和绝对方向

对 $T\in E[\ell]$ 取
$$
f_T\in k(E)^\times,\qquad
\operatorname{div}(f_T)=\ell[T]-\ell[O].
$$
对 $P\in E(k_d)$，其中 $k_d=\mathbf F_{q^d}$，选择辅助点
$R\in E(k)$ 使所写值均有限且非零，定义
$$
\boxed{
t_d(T,P)=
\left(\frac{f_T(P+R)}{f_T(R)}\right)^{(q^d-1)/\ell}
\in\mu_\ell\subset k^\times .
}
\tag{G3}
$$
函数的常数归一因子在比值中消掉。由 Weil reciprocity，改变同一
$[P]-[O]$ 的无交支撑代表只改变一个 $\ell$ 次幂，故 (G3) 不依赖 $R$。
这正是第一变量为挠点的约化 Tate–Lichtenbaum 规范；可核
Enge, *Bilinear pairings on elliptic curves*, §4、§5
<https://arxiv.org/pdf/1301.5520>，
以及 Galbraith 作者修订稿 §26.3、式(26.2)与 Definition26.3.4
<https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch26.pdf>。
下面对本曲线给自含的非退化和 trace 证明，不要求任意扩域上的限制配对非退化。

为固定可能的 Weil 配对逆号，直接定义以下辅助配对。除子
$$
[\ell]^*([T]-[O])
$$
次数零、群和为 $\ell T=O$，所以是主除子。取定义于 $k$ 的函数
$g_T$ 为它的函数；可用原点处首项1作 Galois 不变归一。
于是
$$
g_T^\ell=c_T\, f_T\circ[\ell],\qquad c_T\in k^\times.
$$
对 $S\in E[\ell]$ 定义
$$
\varepsilon_\ell(T,S)=\frac{g_T(Z+S)}{g_T(Z)}.
\tag{G4}
$$
其值与一般点 $Z$ 无关且属于 $\mu_\ell$，因为该比值的除子为零，
其 $\ell$ 次幂为1。它在两变量双线性。
若某 $T$ 对所有 $S$ 的比值均为1，则 $g_T$ 对整个 $E[\ell]$ 平移不变，
从而沿 $[\ell]$ 下降为一个函数，其除子为 $[T]-[O]$；这迫 $T=O$。
故 (G4) 是完美配对。此定义已经指定方向，不借用一个可能取逆的库约定。

若 $[\ell]\widetilde P=P$，同取 $[\ell]\widetilde R=R$，
将 $g_T(\widetilde P+\widetilde R)/g_T(\widetilde R)$ 的
$q^d$ 次幂与自身相除，得到
$$
\boxed{
t_d(T,P)=
\varepsilon_\ell\bigl(T,\pi^d\widetilde P-\widetilde P\bigr).
}
\tag{G5}
$$
理由是该比值的 $\ell$ 次幂恰为 (G3) 括号内的函数比值；
$\widetilde R$ 的 Frobenius 差在分子、分母完全抵消。
所以辅助点和 $c_T$ 均不产生额外倍率。

特别对底域的 $P\in E[\ell]$，由 (G1) 有
$\pi\widetilde P-\widetilde P=-(r+1)\widetilde P=-6P$，故
$$
\boxed{t_1(T,P)=\varepsilon_\ell(T,-6P).}
\tag{G6}
$$
因 $-6\in\mathbf F_\ell^\times$，固定底域上
$t_1:E[\ell]\times E[\ell]\to\mu_\ell$ 完美。
这同时给出了 (G2) 在本问题所需的真实非退化，而非只引用一个群阶条件。

### G.2 任意剩余域次数的完整相容性

取正文的某闭点 $Q$，完整剩余域为 $k_d$，实际输出点为 $P\in E(k_d)$。
令
$$
\operatorname{Tr}_dP=\sum_{i=0}^{d-1}\pi^iP\in E(k).
$$
以 $\sum_{i=0}^{d-1}\pi^i\widetilde P$ 作它的 $\ell$ 除点，
其 Frobenius 差恰为 $\pi^d\widetilde P-\widetilde P$。
(G5) 因而给
$$
\boxed{
t_d(T,P)=t_1(T,\operatorname{Tr}_dP)
\quad\text{对每个整数 }d\ge1\text{ 成立}.
}
\tag{G7}
$$
同式也可逐函数核对：
$\operatorname{Norm}_{k_d/k}(u)=u^{(q^d-1)/(q-1)}$，再乘底域的
$(q-1)/\ell$ 次幂恰是 (G3) 的指数；范数除子的类是
$[\operatorname{Tr}_dP]-[O]$。

**这里允许 $\ell\mid d$。** 此时扩域上将第二变量再限制到原
$E(k)[\ell]$ 的配对确实退化：若 $P\in E(k)[\ell]$，其 trace
为 $[d]P=O$，(G7) 的两边都是1。程序不把这个退化限制拿来恢复
$P$，而只读取原来的完整 trace。对一般 $P\in E(k_d)$，
(G3) 仍保完整指数 $(r^{2d}-1)/\ell$；不把它换成依赖
$d\bmod\ell$ 的指数，也不先将 $P$ 当作 $\ell$ 挠点。

附录 A 的大整数点乘与这里所得完全相同：
$$
[6]\operatorname{Tr}_dP
=\left[\frac{1-(-r)^d}{\ell}\right]P.
\tag{G8}
$$
本附录把 (G8) 的点乘换成两个 (G3) 的有限域幂和一次固定矩阵求解，
没有改变闭点的剩余次数。

### G.3 两个固定辅助点已足够，含 $P=-R$ 的边界

令 $T_1,T_2$ 是原消费者已经验证的 $E(k)[\ell]$ 基。
计算以 $T_i$ 为第一变量的 (G3) 时，取另一个基向量 $U_i$，
只在
$$
R=U_i\quad\text{和}\quad R=2U_i
\tag{G9}
$$
中选择。二者都不在 $\langle T_i\rangle$。若两个
$P+U_i,P+2U_i$ 都在该循环子群，其差 $U_i$ 也在该子群，
矛盾。因此至少一个 $R$ 同时满足
$$
R\notin\langle T_i\rangle,\qquad
P+R\notin\langle T_i\rangle .
\tag{G10}
$$
这个选择可用最多 $\ell$ 个已知点比较准确执行，无随机失败分支。

用 $T_i$ 的短 Miller 加法链计算 $f_{T_i}$ 时，每个线函数和竖直函数的
零极均支撑于 $\langle T_i\rangle$；所以 (G10) 连中间表达式的
$0/0$ 都排除。它比仅避开最后函数的 $O,T_i$ 更强。
若 $P=-U_i$，第一选择落在 $O$，第二选择给 $P+2U_i=U_i$，
仍安全；$P=-2U_i$ 同理。$P=O$ 时两种比值都为1。
正文认定输出为射影原点的分支直接贡献零向量，不能对其仿射坐标作未定义代入。

剩余域中的 $T_i,U_i,\mu_\ell$ 都沿该闭点的**原常数域嵌入**
$k\hookrightarrow k_d$ 输入，不能另选一个未对齐的同构。
同样原几何 $\omega$ 与 Artin 系数域中的角色在后续仍按附录 C–E 的约定处理。

### G.4 原两坐标、全部交重及四点检测保持

固定任意 $\xi_\ell\in k$ 的精确阶为 $\ell$ 的根，定义
$$
M_{ij}=\log_{\xi_\ell}t_1(T_i,T_j)\in\mathbf F_\ell.
\tag{G11}
$$
由 (G6)，$\det M\ne0$。$M$ 使用 (G3) 的同一实际 Miller 规范计算；
因此无需假定某软件的 Weil 配对方向，也无需猜定基的行列号。

将原有效除子及正文共同项、唯一提升全部处理后，设对应的完整输出为
$$
p_{ab}=[6]\sum_Q n_Q\operatorname{Tr}_{d_Q}P_Q .
$$
这里 $n_Q$ 是原完整交重；相对三次分歧已按正文处理，射影原点项为零。
令
$$
b_i=
6\sum_Q n_Q\log_{\xi_\ell}t_{d_Q}(T_i,P_Q)
\pmod\ell,\qquad
\binom{x_1}{x_2}=M^{-1}\binom{b_1}{b_2}.
\tag{G12}
$$
由 (G7) 和双线性，
$$
\boxed{p_{ab}=x_1T_1+x_2T_2.}
\tag{G13}
$$
在执行 (G3)/(G7) 后，才可在 (G12) 中将交重系数约模 $\ell$；
这不是先把未 trace 的点或闭点次数约掉。
离散对数仅在已固定的 $\ell=5$ 或7个根中查表，且每个值应断言
确在该表中。

所以同样的四个完整 $p_{00},p_{01},p_{11},p_{12}$ 被恢复，
附录 D 的常数 Frobenius、附录 E 的两点非零判据及
完整18项／九项 Fourier核验均可原样使用。
这给一个可选的严格计算替换；尚未比较实际运行时间，
也不把本配对的非退化当作原循环影子已经非零。


## 附录 H：同一相对六次源的二次层、无分歧三次层和准确整闭包

本节仍是正文的
$$
B=X_0(867),\qquad Y=X_0(3468),\qquad
k=\mathbf F_{r^2},\quad r=29\ \text{或}\ 41,\quad
\delta=1+2\omega,\quad \delta^2=-3.
$$
也可在包含 $\omega$ 的特征零常数域使用这些公式。
目标是给原 $k(Y)/k(B)$ 的整闭包一个明确构造；
不改原 $q_0/q_2$、任何 Artin 系数或有限闭点。
下述证明没有执行新的整基计算。

### H.1 原两个函数及其双向返回

R882(9) 在 $Y$ 的原坐标 $y_s$ 中是
$$
T=\frac{y_s^2(y_s^2-9)^2}{(y_s^2-1)^2}.
$$
定义两个新的源坐标
$$
\boxed{
z_2=\frac{y_s(y_s^2-9)}{y_s^2-1},
\qquad c_3=\frac{y_s-\delta}{y_s+\delta}.
}
\tag{H1}
$$
这里 $z_2$ 不是解析模参数，$c_3$ 也不是 Artin 系数。
直接消去给
$$
\boxed{
z_2^2=T,\qquad
c_3^3=\frac{z_2-3\delta}{z_2+3\delta},\qquad
y_s=\delta\,\frac{1+c_3}{1-c_3}.
}
\tag{H2}
$$
为逐项核定符号，把最后一式代入 $z_2$，得到
$$
z_2=3\delta\,\frac{1+c_3^3}{1-c_3^3},
$$
这恰与 (H2) 中间式等价。因此 (H1)/(H2) 是函数域的真实双逆；
$1-c_3$ 等分母的零点由同一光滑射影正规化保留。

设 $Z$ 是 $k(B)(z_2)$ 的光滑射影曲线。由附录 B 的原 cusp 表，
$T$ 的零极阶全部为奇数1或289，所以 $T$ 不是平方，
$[k(Z):k(B)]=2$。R882(11)/(12) 的实际 CRT 群说明
原相对源 $Y/B$ 的几何次数为6、群为 $S_3$；
(H1)/(H2) 遂准确给
$$
\boxed{
k(B)\subset k(Z)=k(B)(z_2)
\subset k(Y)=k(Z)(c_3),\qquad
[k(Z):k(B)]=2,\quad [k(Y):k(Z)]=3.
}
\tag{H3}
$$
没有把一枚任意三次根接到原源上。

还可直接看原 deck 作用。两变换
$$
s(y_s)=-y_s,\qquad
\tau(y_s)=\frac{y_s-3}{y_s+1}
$$
在这两个坐标中为
$$
s:(z_2,c_3)\longmapsto(-z_2,c_3^{-1}),\qquad
\tau:(z_2,c_3)\longmapsto(z_2,\omega^2c_3).
\tag{H4}
$$
相应矩阵 $\begin{pmatrix}1&-3\\1&1\end{pmatrix}$ 的三次幂为
$-8I$，故 $\tau$ 阶3，且 $s\tau s=\tau^{-1}$。
这两个变换来自原六次 splitting field；
不是原被商掉的中央 $R$，也不是常数域 Artin 自同构。
原端点标号仍由恢复的同一个 $y_s$ 代回 R882(5)、(17) 决定。

### H.2 全部二次分歧和属187的中间曲线

$T$ 是原模单位，在 $B$ 上的完整零极支撑恰为36个几何 cusp。
每一处阶为 $\pm1$ 或 $\pm289$，均为奇数。
在特征不为2的局部 DVR 中，$z_2^2=T$ 因而在这36处且仅在这36处
分歧指数2。非 cusp 上 $T$ 是单位，二次代数为 étale。
故
$$
2g(Z)-2=2(2\cdot85-2)+36=372,\qquad
\boxed{g(Z)=187.}
\tag{H5}
$$
每个原 cusp 在 $Z$ 上恰有一个地方，剩余域不变；
所以 $Z$ 有36个几何 cusp。这里的个数一律按闭点次数求和，
没有假定这些 cusp 全在 $k$ 有理。

为核下一层的全部分歧，必须使用原模映射而不是只看某个仿射方程。
在 $X_0(3)$ 上，$T=-27$ 是阶3椭圆点。
$X_0(867)$ 没有阶3椭圆点：若一个阶3自同构固定 cyclic $17^2$ 子群，
则它也固定其中的 cyclic17直线；但其在 $E[17]$ 上的多项式
$X^2+X+1$ 在 $\mathbf F_{17}$ 上不可约，矛盾。
因此原忘却映射 $B\to X_0(3)$ 在 $T=-27$ 的每个几何原像
都恰有分歧指数3。
此论证在 $r=29,41$ 的良好约化仍成立：2、3、17都可逆，
相关阶3稳定子 tame，而上述17挠点直线条件不变。
所以
$$
\operatorname{zero}_B(T+27)=3D_0,\qquad
D_0\text{ 约化},\quad\deg D_0=102.
\tag{H6}
$$
这里 $\deg T=306$；$T+27$ 在 cusp 的极阶与 $T$ 相同。
特别 (H6) 不是预设某个未知除子三整除。

### H.3 原三次层处处无分歧，且保所有剩余域

在 $Z$ 上，$T=-27$ 的原像分成 $z_2=3\delta$ 与
$z_2=-3\delta$ 两组，因为 $-27=(3\delta)^2$ 且 $3\delta\in k^\times$。
二次层在这些点不分歧，每个 $D_0$ 地方分别给两点，剩余域不变。
记两组约化除子为 $D_+,D_-$，则
$$
\deg D_+=\deg D_-=102,\qquad
\operatorname{div}_Z(z_2-3\delta)=3D_+-P_\infty,
$$
$$
\operatorname{div}_Z(z_2+3\delta)=3D_--P_\infty,
\qquad \deg P_\infty=306 .
$$
两个分母共享同一个完整极除子；它不能在求函数除子之前漏掉。
于是原函数
$$
f=\frac{z_2-3\delta}{z_2+3\delta}
$$
满足准确的全局等式
$$
\boxed{
\operatorname{div}_Z(f)=3D,\qquad D=D_+-D_-.
}
\tag{H7}
$$
这包括全部有限与无穷地方。

逐地方写 $f=\pi^{3a}u$，$u$ 为单位。
则 $\pi^{-a}c_3$ 满足 $X^3-u=0$，其导数
$3X^2$ 在该代数内为单位。故 (H2) 三次层在每一个地方均 étale，
包括 $D_\pm$ 上 $c_3$ 原有零极的地方。
这些地方仍可能有非平凡的剩余域扩张；“无分歧”不等于全部分裂。
由 (H3) 的原几何连通性，这是一个真正的无分歧循环三次覆盖，
从而
$$
\boxed{g(Y)=3(g(Z)-1)+1=559.}
\tag{H8}
$$
(H7) 的除子类是原 $J(Z)[3]$ 中的非零类。
若它在几何上为主除子，则 $f$ 是常数乘三次幂，
在代数闭常数域上三次层分裂，与原几何次数3矛盾。
这里只识别这一实际类，不把任意三挠类换入来源。

在 cusp 上可更明确地核全部分裂：

| 原底值 | $z_2$ 的值 | $f$ 的剩余值 | $c_3$ 的三个剩余值 | $y_s$ 的值 |
|---|---:|---:|---|---|
| $T=0$ | $0$ | $-1$ | $-1,-\omega,-\omega^2$ | $0,3,-3$ |
| $T=\infty$ | $\infty$ | $1$ | $1,\omega,\omega^2$ | $\infty,-1,1$ |

三个根均在原常数域内且互异，所以每个 $Z$ 的 cusp 在三次层
恰分裂为三个、剩余域不变。由此准确恢复
$Y$ 的108个几何 cusp 以及 $Y/B$ 每一 cusp 的分歧指数2，
与附录 B 一致。$D_\pm$ 的可能剩余域扩张没有被这张 cusp 表代替。

### H.4 原无穷支的绝对选择

继续 R882 的原参数 $Q=q^6$ 和
$$
x_s=q^{-2}+O(q^4),\qquad y_s=-q^{-3}+O(q^3).
$$
由 (H1) 得
$$
\boxed{
z_2=-q^{-3}+O(q^3),\qquad
c_3=1+2\delta q^3+O(q^6).
}
\tag{H9}
$$
取 $u=q^3=Q^{1/2}$，即
$z_2=-u^{-1}+O(u)$、$c_3=1+2\delta u+O(u^2)$。
该符号同时由
$$
f=1+6\delta u+O(u^2),\qquad c_3^3=f
$$
核定。原 cusp 是表中 $c_3=1$ 的分支；
取 $\omega c_3$ 或 $\omega^2c_3$ 会把它换到 $y_s=-1$ 或1，
所以不能把它们当无关的立方根选择。
若返回整个十八次源，再保原 $x_s^3=y_s^2-1$ 及
$x_s\sim q^{-2}$；本节没有变更那个中央三次层。

### H.5 二次层的整闭包：全正负赋值

以下环公式对原有理底的有限整环和无穷整环分别应用。
设 $\mathcal O_B$ 是 $k(B)$ 在 $k[t]$（或 $k[t^{-1}]$）上的整闭包。
对其每个素位 $\mathfrak p$，写
$$
v_{\mathfrak p}(T)=2b_{\mathfrak p}+\epsilon_{\mathfrak p},
\qquad b_{\mathfrak p}=\left\lfloor\frac{v_{\mathfrak p}(T)}2\right\rfloor,
\qquad \epsilon_{\mathfrak p}\in\{0,1\}.
$$
令可逆分式理想
$$
\mathfrak b=\prod_{\mathfrak p}\mathfrak p^{b_{\mathfrak p}}.
$$
则完整整闭包是
$$
\boxed{
\mathcal O_Z=\mathcal O_B\oplus z_2\,\mathfrak b^{-1}.
}
\tag{H10}
$$
**负指数也必须按 floor 取值。**
在局部令 $T=\pi^{2b+\epsilon}u$，第二个生成元是
$\pi^{-b}z_2$，其平方为 $\pi^\epsilon u$。
$\epsilon=0$ 时得到二次 étale 整代数；
$\epsilon=1$ 时是 tame Eisenstein 二次 DVR。
两种情形均为整闭包。乘法闭包逐位由
$v(T\mathfrak b^{-2})=\epsilon\ge0$ 给出。

例如原 $T$ 极阶289时，$b=-145$、$\epsilon=1$，
第二个生成元为 $\pi^{145}z_2$；
$T$ 零阶289时，$b=144$，生成元为 $\pi^{-144}z_2$。
这说明不能只对零除子开平方，或把 $\mathfrak b^{-1}$ 的方向倒写。
一般分式理想未必主，(H10) 不预设一个全局统一的 $\pi$。

### H.6 三次层的整闭包及完整乘法

令 $\mathcal O_Z$ 是 (H10) 的整环。对 (H7) 的同一个原函数 $f$，
每个素位都有 $v_{\mathfrak q}(f)=3a_{\mathfrak q}$。
定义
$$
\mathfrak a=\prod_{\mathfrak q}\mathfrak q^{a_{\mathfrak q}},
\qquad (f)=\mathfrak a^3 .
$$
则准确的原三次整闭包为
$$
\boxed{
\mathcal O_Y=
\mathcal O_Z\oplus c_3\,\mathfrak a^{-1}
\oplus c_3^2\,\mathfrak a^{-2}.
}
\tag{H11}
$$
这不是只给一组整元素或有限指标的子环。

逐位 $f=\pi^{3a}u$ 时，令 $v=\pi^{-a}c_3$；
右边是 $\mathcal O_{Z,\mathfrak q}[v]$，$v^3=u$。
因 $u$ 和3均为单位，该代数有限 étale，已正规且为原域的局部整闭包。
乘法也完整闭合：若两个幂指标之和小于3，分式理想指数直接相加；
若 $i+j\ge3$，用 $c_3^3=f$ 后
$$
f\,\mathfrak a^{-(i+j)}
=\mathfrak a^{-(i+j-3)}
$$
作为分式理想严格成立。这里 $a=-1$ 的极点同样使用
$\pi c_3$ 和 $\pi^2c_3^2$，没有漏负赋值。
有限、无穷两套整环各自应用同式，所以所有闭点及高交重仍在。

R882 附录 B 已给 $B/B^+$ 的
$w^2=\delta_J$、$\operatorname{div}(\delta_J)=2A+\mathcal B$。
对它先应用 (H10) 的同一二次局部证明，就能从已正规化的 degree24
$B^+$ 构造 $\mathcal O_B$；再应用 (H10)/(H11) 得到
$\mathcal O_Z,\mathcal O_Y$。
这些环作为 $k[t]$ 模的秩依次为
$$
24,\qquad48,\qquad96,\qquad288.
\tag{H12}
$$
各分式理想作为 $k[t]$ 模的整基给出相应直和的整基；
不需要再把裸 degree288 多项式送入一般正规化程序。
这只是一个准确的替代构造：理想运算和整基的实际运行成本尚未测量。

所有转换有 (H1)/(H2) 的双逆。故可以把得到的理想、地方和剩余映射
送回正文原 $y_s$ 表示，继续计算同一个
$y_1-y_2$ 完整有效除子、同一个 $f_0$ 和同一个原 Artin shadow。
分式理想方案没有给两份尚未认证的特征零映射补 PASS，
也没有从三次层无分歧推出原循环或其 trace 非零。
