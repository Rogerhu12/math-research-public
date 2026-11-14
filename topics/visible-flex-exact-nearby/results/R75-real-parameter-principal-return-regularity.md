# R75：同一真实参数族的两腿主特征返回存在与正则性

2026-11-12，constructive-route。

**已证明并绑定实际证书：** 对下述整个准确实参数区间，R37 修改主算子
的两腿特征返回是实际存在的保向圆微分同胚；它对角变量解析，对真实参数
为 \(C^2\)。证明包括移动 spline knot 的匹配、真实 turn 的消根及统一
存在角带。这里得到的显式存在带极小，不能替代 R31 所需的有效共同
复带、实际残差、横截或参数 Taylor 常数。

这不是把辅助参数变化称为精确等距曲面族：参数变化时径向输出 target
\(g_0(p)\) 同步变化，所有 \(K_0\) 参数导数都属于同一真实 target 家族。
本结果只处理 R37 的主特征圆映射，未处理完整 Darboux 传输的低阶幅度、
相位、PDE 反馈或闭曲面非线性问题。

## 1. 准确家族与已完成的输入

令

\[
 p_0=-\frac{7789843107295549}{4611686018427387904},\qquad
 I=\left[p_0-\frac1{2000000},p_0+\frac1{2000000}\right].
 \tag{75.1}
\]

原始输入、方向和显式对称 R33 定义与 R73 相同；原始 binary64 控制点
按准确 dyadic 解释，先取准确 affine 控制点，再作固定 base 权重、偶奇
对称化和真实无限 primitive。保存的准确定义文件为
[data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json](../data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json)，
SHA256 为
91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848。

需要的三个完成证书如下。

| 证书 | 当前 SHA256 | 本文使用的内容 |
|---|---|---|
| R73 全小参数管复角报告 | 30001c1a7e7de13e89924163cdbf79c95a5a1e2269430d9f5ee93038c12f2e80 | 全 \(|r|\le\operatorname{binary64}(.24)\)、物理角带 \(1/56\) 内原始分母一致非零及两个系数商界 |
| 整个 affine 家族的实核心 target 类型报告 | 33385f661f1ab87cac0533343baafad5d80c3516c6f2d2d7858e58f74852b436 | 对 \(|p|\le\operatorname{binary64}(.01)\)，只有两条简单 target 根，内部 \(K_0<0\)，\(a,E>0\) |
| 共同真实根区间报告 | b5900c391667b2a1be90912f2abaf58eaea66dfc51c082a8db39ea582b4b94a8 | 根在共同严格单调 collar 内，对同一参数家族成立 |

第二、三个文件分别为
[data/phase_ring_continuation/type_fixed_step02_d5_affine_core_target_type.json](../data/phase_ring_continuation/type_fixed_step02_d5_affine_core_target_type.json)、
[data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json](../data/phase_ring_continuation/type_fixed_step02_d5_parameter_root_interval.json)。
这些是环境恢复后实际重算的当前字节；未把丢失前报告的旧哈希充当当前文件。

记正根为 \(t(p)\)。全部 \(p\in I\) 满足

\[
 0<t(p)<\operatorname{binary64}(.2384)<\frac14,\qquad
 K_0(r,p)<0\quad(|r|<t(p)).
 \tag{75.2}
\]

根区间严格落在一个共同实际 scalar span 内。全核心已付
\(a,E>0\)，R73 在物理复角带 \(S=1/56\) 上给

\[
 |n|>\frac{2259}{10000},\qquad
 \left|\frac mn\right|<9,\qquad
 \left|\frac Gn\right|<7.
 \tag{75.3}
\]

这里 \(n=N_{\rm raw}\)、\(m=M_{\rm raw}\)，
\(G=(F_r\times F_\theta)\cdot(F_r\times F_\theta)\) 是实际图的面积平方。
复角下使用双线性解析延拓，不能引入共轭或换成 target 面积 \(Ea^2\)。

## 2. 全实核心的统一曲率界

完成的 target 类型报告对 collar 外每个闭单元保存 \(K_0\) 区间。
其绝对值最大端点为准确 binary64
\(1.1629701853235304\)。共同 collar 是准确保存端点的区间

\[
 [\operatorname{binary64}(.238152859375),
  \operatorname{binary64}(.23864114062500003)],
\]

其中 \(53<K_{0,r}<68\)，且每个 \(t(p)\) 都在该 collar 内。
由 \(K_0(t(p),p)=0\) 和中值定理，整个 collar 上

\[
 |K_0(r,p)|\le
 \sup_{\rm collar}|K_{0,r}|\,
       (\text{collar 右端}-\text{collar 左端})<1.
\]

因此在整个实核心及整个 \(I\) 上，有安全的统一结论

\[
 |K_0(r,p)|<2.
 \tag{75.4}
\]

有限核查脚本以 Fraction 解释所有保存的 binary64 区间端点，独立检查
外侧闭单元的唯一缺口恰是该已证明 collar，并准确比较 (75.4)。
这不是用浮点显示值进行没有方向的比较。

## 3. 固定物理转向时间的真实场

对每条腿使用

\[
 r=t(p)\sin\tau,\qquad -\frac\pi2\le\tau\le\frac\pi2.
 \tag{75.5}
\]

在 R59 frame 中令 \(n=-a^2D,\ m=-a^2M,\ G=a^2W\)。
采用 R65 native 场的分支命名，定义

\[
 f_\sigma(\tau,\theta,p)=
 -t(p)\cos\tau\,
 \frac{M+\sigma\sqrt{-K_0}\,W}{D},
 \qquad \sigma\in\{-1,1\},
 \tag{75.6}
\]

其中各几何量均在同一个 \((r,\theta,p)\) 取值，实内部的平方根为正。
若用 raw 二型的另一符号约定，只将 \(\sigma\) 换成 \(-\sigma\)；
本文对两种分支同时成立，实际返回仍须保持对应保存 runner 的命名。

由 (75.2)–(75.4)，整个实 \(\tau,p\) 域和复角带
\(|\operatorname{Im}\theta|\le S\) 上，

\[
 |f_\sigma|
 \le\frac14(9+7\sqrt2)
 <\frac14(9+7\cdot\tfrac32)=\frac{39}8<5.
 \tag{75.7}
\]

每个分支以物理角 \(\pi/2\) 为周期，满足实共轭对称。
对内部实 \(\tau\)，复角解析性来自同一真实无限 R33 primitive 和 (75.3)。
两端点的解析定义由下节给出。

## 4. 移动 knots 不产生一、二阶参数界面跳跃

原始 base、raw phase、radius shift 与 mean radius 的内部 spline 连续阶
至少为 \(C^4\)；height primitive 至少为 \(C^5\)。实际
\(\beta=b^3\beta_{\rm raw}\)、\(\gamma=b^2\gamma_{\rm raw}\)
之后再作偶奇对称化，因此它们一般不是五次多项式，但仍保持 \(C^4\)。
参数只以准确 affine 控制点和 mean 参数进入，固定 knot 不随 \(p\) 改变。

在每个固定有限角带上，所有有限阶 \(p\) 导数与前四阶 \(r\) 导数
有连续一致包络。于是 R33 的真实无限角原函数可与这些导数交换，得到
\(F\) 对 \(r\) 为 \(C^4\)、\(F_r\) 为 \(C^3\)。同时

\[
 E(r,p)=\langle F_r\cdot F_r\rangle_\theta
\]

对 \(r\) 为 \(C^3\)，其所需混合参数导数连续。
在 \(a,E>0\) 上，

\[
 K_0=\frac{a'E'}{2aE^2}-\frac{a''}{aE}
 \tag{75.8}
\]

对 \(r\) 为 \(C^2\)，并具有连续的全部二阶混合 \(r,p\) 导数。
在严格负曲率和 \(n\ne0\) 的普通区，(75.6) 因而联合 \(C^2\)
依赖实 \((\tau,p)\)，同时对 \(\theta\) 全纯。

更明确地，某个固定 scalar knot \(r_k\) 在固定时间坐标中的 crossing 是

\[
 \tau_*(p)=\arcsin(r_k/t(p)).
\]

它可以移动，但左右场在该曲线上的零、一、二阶真实 jet 准确匹配。
左右同一个角函数恒等相等，其角导数也相等。
若把积分按 moving crossing 拆开，一阶边界项是
\(\tau_*'(f_- -f_+)\)，故为零；二阶边界项由
\(f_--f_+\)、其固定参数导数差和其时间导数差组成，也全部为零。
对沿同一解复合的场，链式项同样相消。

因此真实参数变分不是在每个分片重新设零初值，且不需要添加虚构的
delta 型界面源。对不准确的单 germ 延拓近似，仍须支付另一个
[caps 证明](../notes/2026-11-12-exact-germ-matching-and-cubic-caps.md)
中的实际小段误差；本段只证明准确场本身的匹配。

## 5. 真实 turn 的固定端点正规化

共同根 bracket 严格位于一个实际 scalar span 内；在该 span 中，
所有输入、真实无限 primitive、\(E\) 与 \(K_0\) 都对 \(r,p\) 实解析。
共同根的 \(K_{0,r}>0\)，故由解析隐函数的局部幂级数构造，
每个参数点附近的根为解析函数。根的唯一性使这些局部分支相同，
给出整个 \(I\) 上同一个 \(t(p)\)；特别地它为 \(C^2\)，与 R58 的
真实根参数 jet 一致。

在任一根附近，写
\(\eta=\pi/2-\operatorname{side}\tau\)，则
\(r=\operatorname{side}\,t(p)\cos\eta\)。
由 target 的准确径向反射，令

\[
 J(\rho,p)=-\frac{K_0(t(p)-\rho,p)}{\rho},\qquad
 Q(\eta,p)=\frac{t(p)J(t(p)(1-\cos\eta),p)}{1+\cos\eta}.
 \tag{75.9}
\]

\(J\) 在 \(\rho=0\) 可去奇，值为 \(K_{0,r}(t(p),p)>0\)；
\(Q\) 在端点附近解析且为正。真实物理支内

\[
 -K_0=\sin^2\eta\,Q,\qquad
 \sqrt{-K_0}=\sin\eta\sqrt Q,\qquad
 r_\tau=t(p)\sin\eta.
\]

因此 (75.6) 的准确端点表达是

\[
 f_\sigma
 =-t(p)\sin\eta\,
   \frac{M+\sigma\sin\eta\sqrt Q\,W}{D}.
 \tag{75.10}
\]

这在固定的 \(\eta=0\) 处解析，取值为零；它联合 \(C^2\) 依赖真实参数，
并对复角保持解析。没有对未消根的 \(\sqrt{-K_0}\) 形式求导后留下伪奇项。
两腿连接处允许时间导数有单侧值；每腿的参数变分和其后复合均准确成立。

本节只需根附近一个真实共同 germ；不把普通 germ 延拓穿过根。
需要有效复时间域时仍必须使用 R65 的实际 \(Q\) 与非零分母证书。

## 6. 两腿真实圆返回及其参数变分

在物理圆 \(\mathbb R/(\pi/2)\mathbb Z\) 上，(75.6) 是连续时间的
周期向量场，状态导数连续，且参数二阶导数在每个真实分片及接缝上匹配。
圆为紧集，局部 ODE 唯一解可以延拓到整条腿；也可以用 (75.7)
在实 lift 上直接排除有限时间逃逸。逆向时间方程同样成立。

将先前腿从 \(-\pi/2\) 到 \(+\pi/2\)，再将返回腿从
\(+\pi/2\) 到 \(-\pi/2\) 的两个实际流复合，得到
\(R_{\rm phys,p}\)。对归一角定义

\[
 R_p(x)=4R_{\rm phys,p}(x/4).
 \tag{75.11}
\]

于是

\[
 R_p(x+2\pi)=R_p(x)+2\pi.
 \tag{75.12}
\]

每腿的状态导数满足 \(J'=g_\theta J,\ J(0)=1\)，其中 \(g\)
已包含该腿的有符号时间方向。因此 \(J>0\)，两腿复合仍保向。
结合周期 lift 关系，它是圆微分同胚。

为明确真实参数导数，使用跨两腿递增的时间 \(s\)，令 \(y'=g(s,y,p)\)。
固定初始角的参数变分满足

\[
 \begin{aligned}
 z'&=g_\theta z+g_p,\qquad z(0)=0,\\
 v'&=g_\theta v+g_{\theta\theta}z^2
                 +2g_{\theta p}z+g_{pp},\qquad v(0)=0.
 \end{aligned}
 \tag{75.13}
\]

这些方程可由真实积分方程的差商得到：紧时间、参数和状态域上的
连续一、二阶导数给一致差商余项；积分 Gronwall 估计先证明一阶差商
收敛，再对一阶积分方程作同样操作得到二阶收敛。
有限时间接缝逐段保留前段终值，第四节说明 moving knot 不添加边界源。
所以整个准确返回对 \(p\) 为 \(C^2\)。
归一角的 \(R_p\) 参数导数为物理终值 \(z,v\) 的四倍；这是实际流导数，
没有用径向作用量导数代替。

## 7. 一个统一而极小的存在角带

设 \(S=1/56\)。在状态带 \(S/2=1/112\) 上，(75.7) 的 Cauchy 估计给

\[
 |g_\theta|\le\frac{5}{S/2}=560=:L.
 \tag{75.14}
\]

反向腿的时间符号不改变模长。两腿的总递增时间为 \(2\pi\)。
取任一实初始角及相应实解；若初值改为复数，令其与实解之差为 \(w\)。
在 \(|w|<S/2\) 的范围内，整条状态线段仍在该带中，故

\[
 |w(s)|\le |w(0)|+L\int_0^s|w(v)|\,dv
          \le |w(0)|e^{Ls}.
\]

因此选择

\[
 \varepsilon_\theta=\frac{e^{-1120\pi}}{224}
\]

时，在两腿全过程均有 \(|w(s)|<S/4\)，从而不存在离开
\(S/2\) 状态带的首次时刻。局部 Picard 迭代在较小初始带上一致收敛，
各迭代对初始角全纯，故完整流全纯。此论证对所有 \(p\in I\) 使用同一常数。

归一角返回因此至少在共同开带

\[
 \boxed{|\operatorname{Im}x|<
       s_{\rm exist}:=\frac{e^{-1120\pi}}{56}}
 \tag{75.15}
\]

上有实际解析定义。它对 \(p\) 的前两阶导数在每个严格更小闭带上
连续、对 \(x\) 全纯；这由 (75.13) 和同一局部一致收敛得到。
对实 \(x\)，还可给出极保守的实际导数界

\[
 e^{-1120\pi}\le\partial_xR_p(x)\le e^{1120\pi}.
 \tag{75.16}
\]

这些常数只是一个完整的统一存在证明。它们极其保守，不能代付
当前数值验证使用的标签带，也不提供任何有用的 KAM 小量门。

## 8. 有限输入核查与可用边界

[scripts/fourfold_phase_principal_return_regularity.py](../scripts/fourfold_phase_principal_return_regularity.py)
执行以下有限核查：

- 同一原点、方向、对象及共同根证书哈希；
- 准确有理参数区间在三个已证明参数域中的包含；
- 实核心、根 bracket、collar 的准确嵌套与外侧闭单元覆盖；
- 保存曲率端点和 collar 导数给出的全核心 \(|K_0|<2\)；
- R73 全部单元的 \(n,m/n,G/n\) 界；
- 全部十个实际 scalar profile 的 knot 精确重数与最低连续阶，
  包括正负反射的公共 root span；
- \(39/8<5\)、\(L=560\) 及 (75.15) 所用准确常数。

报告保存在
[data/phase_ring_continuation/type_fixed_step02_d5_step5_real_parameter_return_existence.json](../data/phase_ring_continuation/type_fixed_step02_d5_step5_real_parameter_return_existence.json)。
重跑入口：

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
    python scripts/fourfold_phase_principal_return_regularity.py \
      --out data/phase_ring_continuation/type_fixed_step02_d5_step5_real_parameter_return_existence.json

此接口把“实际圆返回族究竟是否存在且 \(C^2\) 依赖真正参数”的问题
从浮点探索中分离并证明。仍需以同一对象计算可用共同复域、真实
\(R_p,R_{xp},R_{pp}\) 上界、实际横截、共轭残差和 R31 的全部小量条件。
全传输的低阶相位与幅度、PDE 反演、非线性修正、闭合和最终可见性/
reach 标准继续，不因本结果而授予完成。

