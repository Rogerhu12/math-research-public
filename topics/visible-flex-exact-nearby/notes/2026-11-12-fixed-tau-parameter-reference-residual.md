# 固定 τ 参数参考：完整两腿残差恒等式

2026-11-12，constructive_route。本文针对已保存的准确 affine 几何族，
推导由旧三行参考 `Y,L,Z` 构造实际固定 τ 参数参考的方法。
它不把有限多项式参考当作真实轨迹，也不假设其第三行已经是固定 τ 参数导数。

## 1. 精确设定与恒等式

固定一个实际参数 p。令正转折根为 t(p)，径向坐标为

\[
 x(\tau,p)=t(p)\sin\tau,\qquad
 A=x_p=t'(p)\sin\tau,\qquad
 x_\tau=t\cos\tau.
\]

一腿的真实特征速度写成 v(x,θ,p)，完整固定 τ 速度为
`f(τ,θ,p)=x_τ v(x(τ,p),θ,p)`。Y、L、Z 是任意可微参考函数，
令 q=exp L，并定义三个真实残差

\[
 e_0=Y'-x_\tau v,\qquad e_1=L'-x_\tau v_\theta,
 \qquad e_Z=Z'-x_\tau(v_\theta Z+v_p).
 \tag{1}
\]

这里 v、v_θ、v_p 均沿 `(x(τ,p),Y(τ),p)` 取值；v_p 是固定 x、固定 θ
的真实参数导数。选任意不随 τ 变化的 d，定义

\[
 z_{\rm ref}=Z+A v+q d.
 \tag{2}
\]

则其实际固定 τ 参数方程残差满足精确恒等式

\[
 \boxed{z_{\rm ref}'-f_\theta z_{\rm ref}-f_p
      =e_Z+A v_\theta e_0+q d e_1.}
 \tag{3}
\]

证明：固定 τ 微分给
`f_p=A'v+x_τ(v_p+v_x A)`，沿 Y 的 τ 微分给
`(v(x(τ),Y,p))'=v_x x_τ+v_θY'`。将这两个式子与
`q'=qL'` 代入 (2) 的导数，并减去 `f_θ zref+f_p`，
`A'v`、`A v_x x_τ`、`x_τv_p` 以及 `x_τv_θZ` 四类项全部抵消。
余下正是 (3)。这个计算没有将任何参考残差设为零。

## 2. 初值与两腿衔接

若给定本腿入射参数值 z_in，取

\[
 d=\frac{z_{\rm in}-Z(\tau_0)-A(\tau_0)v(\tau_0)}{q(\tau_0)}.
 \tag{4}
\]

则 (2) 在起点准确等于 z_in。旧 trace 的参考初态为 Z=0、q=1，
于是 `d=z_in−A0 v0`；第一腿可取 z_in=0，第二腿须接入第一腿完整参数列。
若第二腿的旧 Z 仍从零开始，(4) 自动补入正确的齐次传播项。
把两腿都独立设 z_in=0 再声称得到完整参数导数是不正确的。

若 Y、L、Z 恰是相应真实解，(3) 右侧为零，因而 zref 正是有该初值的
真实固定 τ 变分；在一般参考上，(3) 则给真实误差源的可验证分解。
恒等式对每条初始角分别成立，d 可以依赖初始角。

## 3. 转折端点：先抵消，再取连续值

在本课题的准确对称对象上令

\[
 Q(\tau,p)=-K_0(t(p)\sin\tau,p)/\cos^2\tau>0,
 \quad v=b+\sigma w\cos\tau\sqrt Q,
 \quad b=-m/n,\quad w=G/n.
 \tag{5}
\]

两腿都在 `−π/2≤τ≤π/2`，因此 cosτ 非负。Q 用 R58/R62 的真实根积分
公式连续延拓到两个端点。于是 v 沿 τ 的导数可直接写为

\[
 \begin{aligned}
 \frac{d v}{d\tau}={}&x_\tau b_x+b_\theta Y'
 +\sigma(x_\tau w_x+w_\theta Y')\cos\tau\sqrt Q\\
 &+\sigma w\left(-\sin\tau\sqrt Q
              +\frac{\cos\tau Q_\tau}{2\sqrt Q}\right).
 \end{aligned}
 \tag{6}
\]

式 (6) 没有 `1/√(−K0)`。同样，(1) 中需要的组合而非裸 v_p 为

\[
 x_\tau v_p=t\cos\tau b_p+
 \sigma t\cos^2\tau\sqrt Q\,w_p
 -\frac{\sigma t w(K_0)_p}{2\sqrt Q}.
 \tag{7}
\]

这里 b_p、w_p、(K0)_p 仍是固定 x 导数。R62 的 f_p 则在固定 τ 下取值。
式 (3) 在开区间已证；(5)–(7) 和 Q 的连续导数使两边都有有限端点极限，
所以恒等式延拓到端点。不得先分别估计伪奇的 `A v_x` 与 v_p 再引入
无穷大损失。

实际实现还可令 s=|sinτ|，
`I(s)=∫_0^1 K_x(t[1−u(1−s)],p)du`。
则 `Q=tI/(1+s)`、`I_s=t∫_0^1 u K_xx du`，据此算 Q_τ；
这在端点同样无须除以消失的 cos²τ。

## 4. 分段参考的跳跃

同一腿内两个相邻时间多项式在同一 τ 的单侧值可能不同。由于 A、d 不变，
准确的跳跃等式是

\[
 [z_{\rm ref}]=[Z]+A\,[v(x,Y,p)]+d\,[q].
 \tag{8}
\]

若两侧 Y 间的整条复线段已在所验证域内，便有
`|[zref]|≤|[Z]|+|A| sup|v_θ| |[Y]|+|d| |[q]|`。
必须使用各段保存多项式的实际端点，不能只看 accepted_state 数组相等便删去跳跃。
两腿交界时支号改变，但转折点 v=b；第二腿按 (4) 接入第一腿完整参考终值，
便可令所定义的 zref 交界值准确连续。若采用另一浮点保存初值，差异仍须另计。

## 5. 如何供连续认证使用

在一段完整时间区间与完整初始角域上，若有严格界，则 (3) 直接给

\[
 \left|\frac{e_z}{q}\right|
 \le \left|\frac{e_Z}{q}\right|
      +|A v_\theta|\left|\frac{e_0}{q}\right|+|d|\,|e_1|.
 \tag{9}
\]

同式适用于复角域，用复模取界。q 必须在所用域无零点，参考 q 的实际
上下界、eZ、e0、e1 的连续界及端点跳跃仍分别支付。
若只在有限点代入浮点数，(9) 不能升级为连续误差界。

配套诊断源 `scripts/fourfold_dense_fixed_tau_parameter_probe.py` 将直接解析微分
保存的 dense 多项式，再以 (6) 形成左侧，以 (3) 形成右侧，并对两腿和端点核对。
它也与旧 trace 已保存的移动端点参数列比较。输出必须明确标为浮点探针；
不能据此宣称参数管、真实返回或 KAM 已认证。

## 6. 同一 δ₃ shared516 实际探针及其浮点缺陷归因

已对原 δ₃ 的两腿共用时间网格作实际重放。每腿选 7 个 accepted segments
`0,1,130,274,419,548,549`，每段左端、中点、右端各取值，并在 8 个原始射线
`0,64,129,193,258,322,387,451` 上解析微分真实保存的 dense 多项式。
第二腿从第一腿保存的完整参数列入射，未重新置零。

原始两种表达的最大差分别为 `4.6325787829432367e−14`、
`6.838117678509123e−14`，而完整终点参数列复原差均为
`4.662069341687669e−17`。前两个差不能删掉，也不是连续误差界。

为定位代数与数值两种可能原因，源码另外计算

\[
 d_p=\cos^2\tau Q_p+K_p+A K_x,\qquad
 d_\tau=\cos\tau Q_\tau-2\sin\tau Q+tK_x.
\]

准确根与准确导数下二者均为零。若对这些量使用独立浮点评价，直接残差与
抵消式的差应额外含有

\[
 \frac{\sigma w}{2\sqrt Q}\{A d_\tau-t d_p\}.
 \tag{10}
\]

将 (10) 作为**诊断项**比较后，剩余差分别只有 `2.181989022196888e−18`、
`4.3785986305312215e−18`。实际浮点 `|d_p|` 最大约 `9.43e−13`、
`|d_τ|` 最大约 `2.97e−9`，指出近转折曲率导数的浮点消减才是前述差的来源。
报告仍完整保留原始差与原始残差，没有把 (10) 从认证预算中悄悄扣除。
真正的连续证明应使用准确根关系与有向场评价，而非把浮点恒等关系误差视为零。

从课题目录重放第一腿：

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python scripts/fourfold_dense_fixed_tau_parameter_probe.py --object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_object.json --root-certificate data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step3_root_tight.json --trace data/phase_ring_continuation/exact_affine_step3_shared_knot_dense516/block_0000_forward.trace.json --out notes/2026-11-12-D5-shared516-fixed-tau-forward-parameter-probe.json

第二腿将 trace 改成 `block_0000_backward.trace.json`、输出改成 backward，
并加 `--incoming-branch data/phase_ring_continuation/exact_affine_step3_shared_knot_dense516/block_0000_forward.trace.json`。
这些大型 trace 作为可重复中间数据保留在本地，源、准确对象和完整 endpoint 报告已存档；
全部 trace 的哈希与重跑入口在既有 shared516 manifest 中。
