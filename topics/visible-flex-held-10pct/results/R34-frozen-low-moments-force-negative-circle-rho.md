# R34：旧七个低矩冻结时，完全圆化的 rho 必有负值

维护：Astra-held10-7322d0de-20261118 / closed_geometry。

## 1. 精确结论

沿用 R33 的 `n=3`、保护弧半宽 `a=21/100`、偶性/三重周期以及七个
**冻结的旧 actual 支撑矩**。旧状态为
`beta4625-q040-linear-difference/seed.json.gz`，SHA256

`c55a2ebfcce39fe72810703e8fb239f60ce291b48cf7650a27d6b5ef52180bc9`。

取 R32 真积分定义的 `lambda=1`、`eta=0` 圆弧背景，transition 为 `2/25`。
对于每个

\[
 q\in[1/25,851/10000]=[.04,.0851],
\]

以及任意满足 R33 条件的实 `C^4` 支撑控制 `b`，完整曲率半径

\[
 \rho=\rho_0+b+b''
\]

都在某个角度严格小于零。

这里不限于任何有限基、最大频率、控制 transition 或曲率采样。
被排除的是“完全圆化后仍保持这七个旧低矩”的正曲率 core。
结论**不排除**重新联立改变这些矩、raw compact 新路径、其他设计参数或课题目标。
它也不适用于 `lambda<1` 时在保护弧上尚未消失的控制函数。

R33 只有范数必要下界，不能单靠大 `L^2` 范数推出负 `rho`。
R34 新增一个全区间有界的对偶权，并利用非负、平均值为一的密度所满足的
单侧积分界，完整支付下面的矛盾。

## 2. 真积分圆弧背景的平均值与粗界

写 `L=pi/3`，`x=phi-L` 为圆弧中心的局部角，延拓周期为 `2L`。
R32 的 cutoff `chi` 满足 `0<=chi<=1`，在 `|x|<=a` 为一，在
`|x|>=a+b0` 为零，其中 `b0=2/25`；transition 是

\[
 1-126t^5+420t^6-540t^7+315t^8-70t^9.
\]

令

\[
 m=\int_0^L\chi(x)\,dx=a+b_0/2=1/4,
\quad
 I=\int_0^L\chi(x)\bigl(8-8\cos3x\bigr)\,dx,
\quad \beta=-\frac{I}{L-m}.
 \tag{1}
\]

这里全部是真实积分，未冻结某个 Gauss 求积的近似 `beta`。
背景为

\[
 \rho_0(x)=1+q\left[8\chi(x)
           +(1-\chi(x))(8\cos3x+\beta)\right].
 \tag{2}
\]

因为 `integral_0^L cos(3x) dx=0`，(1) 立即给出 `rho0` 的周期平均恰为一。
又由 `cos y>=1-y^2/2`，

\[
 0<I\le36(a+b_0)^2m=7569/10000<L-m,
\]

最后一步由执行器的有理 `pi` 下界严格核过。因此

\[
 -1<\beta<0.
\]

(2) 方括号是 `8` 与 `8cos3x+beta` 的凸组合，处于 `[-9,8]`。
于是对于声明的全部 `q`，

\[
 \frac{2341}{10000}\le\rho_0\le\frac{2101}{1250}=1.6808<2,
 \qquad\|\rho_0\|_{L^2(d\phi/T)}<2.
 \tag{3}
\]

这个有意放宽的界足够产生严格矛盾；不需要重新计算 R32 的精细背景积分。

## 3. 复用 R33 的同一个有理对偶

令 `A=D_phi^2+1`，`B(u,v)=<Au,Av>`，平均内积与 R33 完全相同。
取 R33 §4 已冻结的九维有理向量 `z`，以及它在 R33 支撑函数空间中的
Riesz 代表元

\[
 r_z=\sum_{j=0}^8z_jr_j,\qquad w=Ar_z.
\]

由 R33 的完整变分证明，对每个满足同一冻结矩约束的 `b`，

\[
 \langle Ab,w\rangle=B(b,r_z)=z^tc=:N.
 \tag{4}
\]

R33 的有理证书给出

\[
 N>144,\qquad\|w\|_2^2=z^tGz<169,
 \qquad\|w\|_2<13.
 \tag{5}
\]

这里的 `N` 是矩线性泛函，约为 `144.1041387910254128`；不要把它与
R33 的对偶商 `(z^tc)^2/(z^tGz)` 混为一个数。

## 4. 新支付的全角对偶权上界

在基本周期 `[-L,L]` 中，保护弧位于两端，令 `d=L-a`。
R33 的 `r_j` 在未保护区 `0<=t<=d` 上是

\[
 r_j(t)=\frac{s_j\cos(3jt)}{(1-9j^2)^2}
                   +\alpha_j\cos t+\beta_jt\sin t,
\quad s_0=1,\ s_j=2\ (j\ge1),
\]

其中 `alpha_j,beta_j` 由 R33 (11) 的显式 `2x2` 系统决定。
由于 `(D^2+1)cos t=0`、`(D^2+1)(t sin t)=2cos t`，

\[
 w(t)=\sum_{j=0}^8\frac{z_js_j}{1-9j^2}\cos(3jt)
       +2\left(\sum_{j=0}^8z_j\beta_j\right)\cos t.
 \tag{6}
\]

在保护弧内 `w=0`。`r_z` 的值和一阶导数在支撑端点为零，故弱二阶导数没有
Dirac 项；(6) 与零延拓正是 `Ar_z` 的 `L^2` 函数。`w` 在端点可能跳变，
但下面的有界性与积分论证不需要它连续。

置 `u=cos t`。因为 `cos(3jt)=T_{3j}(u)`，(6) 是 `u` 的一个真实 24 次多项式：

\[
 P(u)=\sum_{j=0}^8\frac{z_js_j}{1-9j^2}T_{3j}(u)+\gamma u,
\quad \gamma=2\sum z_j\beta_j,
\quad u\in[\cos d,1].
 \tag{7}
\]

执行器以 R33 的有理外舍入运算包围 `d`、`sin d`、`cos d` 和 `gamma`。
Chebyshev 多项式系数由整数递推 `T_{k+1}=2uT_k-T_{k-1}` 精确生成。
在包含整个真实区间的 `[lower(cos d),1]` 上均分 32 个**区间**，逐个将完整
24 次多项式转成 Bernstein 系数并取凸包，未取函数采样点代替连续范围。

若某格为 `[l,l+h]`、幂系数为 `a_j`，局部幂系数与 Bernstein 系数为

\[
 p_k=h^k\sum_{j=k}^{24}a_j\binom jk l^{j-k},
\qquad
 B_i=\sum_{k=0}^i p_k\frac{\binom ik}{\binom{24}k}.
 \tag{8}
\]

全部运算向外舍入；32 格首尾相接覆盖整个实区间，再并入保护弧上的零。
实际执行得到全周期外包

\[
 -35.511678110654<w(\phi)<90.057154142061,
\]

特别是

\[
 \boxed{\operatorname*{ess\,sup} w<100.}
 \tag{9}
\]

这里只把有裕量的门 (9) 用于证明；细小数是执行器的连续区间外包，
不是某个网格最大值。

## 5. 非负 rho 与对偶积分严格矛盾

如果完整 `rho=rho0+Ab` 非负，由 `b` 的周期性与零 mean，

\[
 \langle\rho,1\rangle
 =\langle\rho_0,1\rangle+\langle b+b'',1\rangle=1.
\]

因此 (9) 强迫

\[
 \langle\rho,w\rangle<100.
 \tag{10}
\]

另一方面，(3)–(5) 和 Cauchy–Schwarz 给出

\[
 \langle\rho,w\rangle
   =N+\langle\rho_0,w\rangle
   \ge N-\|\rho_0\|_2\|w\|_2
   >N-26>118.
 \tag{11}
\]

(10) 与 (11) 矛盾。因为声明中的 `b` 为 `C^4`，完整 `rho` 连续，
所以结论确实是某个角度 `rho<0`，而不只是某个未经解释的范数失败。
这个矛盾对 `[.04,.0851]` 内每个 `q` 一致成立。

程序还记录了更详细的有理量：`N-26` 约为 `118.1041387910254128`，
与保守上界 `100` 相隔超过 `18.10413879`。
不需要接近浮点舍入尺度的判号，也没有用本题其他几何阈值替代正性门。

## 6. 执行来源与后续边界

新增执行器：

`scripts/resume_closed/certify_frozen_moment_rho_obstruction.py`。

它读取已登记的
`scripts/resume_closed/protected_arc_curvature_dual_execution.json`，核 R33 source
hash、维数、保护弧、同一 `z/c` 以及精确线性泛函，复用已证明的 `z^tGz`
外包；没有再次求逆、运行 BVP 或重新扫描辅助频。
新执行结束码为 `0`，时间约 `.735` 秒。
命令、来源/输出 hash、32 格覆盖和判号门见
`scripts/resume_closed/frozen_moment_rho_obstruction_execution.json`。

R34 为 R33 观察到的旧低矩放大提供了更强的精确解释，但边界仍限于这些被冻结
的矩。实际 canonical 联立本来也可以改变控制；raw 新路径更直接地避免沿途
把旧参数数值解释成终点的同一组低矩。它们仍需原样通过自己的实际残差、正性、
完整 metric 与闭图验收。本条不为任何自由联立路径设新的障碍结论。
