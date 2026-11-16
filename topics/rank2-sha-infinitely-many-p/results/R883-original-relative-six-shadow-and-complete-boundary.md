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
