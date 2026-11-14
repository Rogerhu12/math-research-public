# δ5 的准确初值、连续符号参考与直接 jet 接口

2026-11-12，constructive_route。

**状态：已定义一个新的、可单独验证的有限参考族，并证明其准确初值和全部接缝；
没有把 δ4 的数值轨迹转授为 δ5 的真实流。**
这一构造服务于 R60/R61 的连续残差验证，不需要再启动一整轮低精度射线。

## 1. 两个不同的准确对象

原始共享 1032 射线、两个 U/L 参考的参数为

\[
 \delta_4=-7789866024620307/4611686018427387904.
\]

新目标参数为

\[
 \delta_5=-7789843107295549/4611686018427387904,
 \quad \delta_5-\delta_4=11458662379/2305843009213693952.
\]

二者均使用同一条**先做准确 affine 加法、再显式径向奇偶化的无限 R33 图**，
及同步变化的真实输出目标度量。新参数不是控制点四舍五入后的一张 NPZ 图。
新对象文件 `type_fixed_step02_d5_exact_affine_step5_object.json` 的 SHA 为
`91040c2271fa32c42e79d2af1ee706d4362683ecbc18f1000de2521b8c136848`。
它自身的有向根证书 SHA 为
`489268d254c2a9454ccbee32a4821d9bf577279490f76c9cc6f8d902a5e64e0b`，给出

\[
 t(\delta_5)\in[.23839687429986203,.2383968742998687].
\]

当前 H5 是准确 dyadic Fourier 多项式，次数 516，系数公共分母为 \(2^{120}\)，
文件 SHA 为 `0439d88f10f46d367e44a984db661ac3806a7bd052f46eca14e71594fa8eb2c2`。
H5 的定义来自准确旧 H 加所选二进有理 Newton 修正；辅助浮点导出 NPZ 不是其定义。

## 2. 作为输入保留的旧有限参考

旧 δ4 每腿有 550 个共享时间段。`fourfold_shared_dense_reference.py` 选取
时间七次 Bernstein、多项式角次数 516 的实 Fourier 系数，保存的 binary64
数随后作为准确 dyadic 系数定义

\[
 Y_{4,f}(\tau,x)=x/4+U_{4,f}(\tau,x),\qquad q_{4,f}=e^{L_{4,f}},
\]

返回腿同理。首末时间端点是准确 \(\pm\pi/2\)，内部端点是保存的准确二进有理数。
每一腿内相邻段的 U、L 端控制系数准确共享。返回腿的首 U 准确等于前腿末 U；
L 在两腿之间可以重新定义，故不假设两腿参考权相等。

两个 manifest 分别为：

- `step4_shared1032_reference_forward/manifest.json`，SHA
  `43cbffb2e0b924b6d69608df54e0acf3cf8ecd66c030b7343e84864ad6eb81a0`；
- `step4_shared1032_reference_backward/manifest.json`，SHA
  `0ad615a077a0c313d0700c3a6392f39250617257b93197ba1f5f766716191a07`。

这两个函数是由旧数据选定的新准确多项式。浮点 DFT、时间重参数化或 Bernstein
转换的精度不是证明假设；必须直接验证最终保存函数的真实微分方程残差。

## 3. 修正传播多项式及准确初值差

每腿另选一个次数 128、时间七次的实 Fourier/Bernstein 多项式 \(\widetilde Q\)。
八个 Bernstein **控制值**来自旧 dense L 的八个 \(\exp L\) 取值；不称其为准确插值。
将每腿首控制多项式设为常数 1，并准确共享同腿所有相邻端控制系数。
因此

\[
 \widetilde Q_f(a,x)=\widetilde Q_b(b,x)=1,
\]

且两腿各自连续。这里不需要 \(\widetilde Q\) 处处为正或无零点，也不声称它
接近真实 Jacobian。R60 使用的非零参考权仍是 \(q=e^{L_4}\)。

令 \(H_5(x)=x+h_5(x)\)。用 Fraction 运算逐 Fourier 系数定义

\[
 a(x)=H_5(x)/4-Y_{4,f}(a,x)=h_5(x)/4-U_{4,f}(a,x).       \tag{1}
\]

保存的 a 次数为 516，公共分母为 \(2^{122}\)。这个差没有经过一次新的浮点减法，
包括完整初始 U 的全部系数；提升项 \(x/4\) 准确相消。
独立验证器读回保存的全部 1034 个实有理系数，逐项核对 (1)。

## 4. 新参考的定义与连续性证明

记 \(q_e(x)=\widetilde Q_f(b,x)\)，定义

\[
 \begin{aligned}
 Y_{5,f}&=x/4+U_{4,f}+\widetilde Q_f a,& L_{5,f}&=L_{4,f},\\
 Y_{5,b}&=x/4+U_{4,b}+\widetilde Q_b(q_e a),& L_{5,b}&=L_{4,b}.
 \end{aligned}                                                   \tag{2}
\]

所有乘积保留为有限函数的准确符号乘积，没有重新投影至原 1032 点网格。
前腿角次数至多 644，返回腿至多 772；时间次数仍为 7，因为 a、q_e 与时间无关。
保存正频率及其负频共轭，故在实 x 上取实值。归一化角周期为 \(2\pi\)，
物理角提升仍是 \(Y(x+2\pi)=Y(x)+\pi/2\)。

在前腿起点，\(\widetilde Q_f=1\)，所以 (1) 立即给
\(Y_{5,f}(a,x)=H_5(x)/4\)，对所有复 x 都准确成立。
同腿每个 U、Q 端控制系数相同，故 (2) 在每个内部接缝连续。
在两腿交界，旧 U 相同且 \(\widetilde Q_b(b,x)=1\)，两侧都等于

\[
 x/4+U_{4,f}(b,x)+q_e(x)a(x).
\]

因此新 Y 的全部段跳跃与换腿跳跃准确为零。这不是仅在有限角节点成立的等式。
参考在时间上连续且分段 \(C^1\)，满足 R61 所需的参考正则性。
若两腿的 L 不同，真实误差从一腿传入下一腿时仍要保留
\(|q_-|/|q_+|\) 的权重比例；Y 跳跃为零不允许清空累计误差。

`fourfold_retarget_reference_identity.py` 独立重读四套全体 shards，核对 SHA、
准确时间列表、维数、实均值、有限系数、各接缝的准确系数相等，以及 (1) 的
Fraction 等式。它不使用构造器已输出的布尔结果作为通过依据。

## 5. 不经重采样的直接 jet 与完整有限尾界

`fourfold_retarget_reference_jets.py` 直接读取上述准确系数；它在
\(\tau=\tau_c+h u,\ x=x_c+h_x v\) 上给出 `TimeAngleJet`。
对每个 Bernstein 基的有理变换与全部 Fourier 模作 Arb 有向运算，再在
矩形 Taylor 商代数中乘 \(\widetilde Q a\) 或 \(\widetilde Q(q_ea)\)。
没有对这些乘积进行 Fourier 截断，时间多项式的全部七次系数都保留。
时间导数准确为

\[
 \partial_\tau Y_{5,f}=\partial_\tau Y_{4,f}
                       +(\partial_\tau\widetilde Q_f)a,
\quad
 \partial_\tau Y_{5,b}=\partial_\tau Y_{4,b}
                       +(\partial_\tau\widetilde Q_b)(q_ea).       \tag{3}
\]

矩形 jet 不代表全部无限角 Taylor 系列。因此接口另给整个有限函数在外双圆盘
上的界。对一个有限因子 f，分别记其中心角外时间界 C_f、整个外双圆盘界 O_f、
角变化界 V_f、实时间外角界 A_f，以及实时间导数界 D_f。由完整有限 Fourier
求和直接取得这些量。对乘积，恒等式

\[
 f(x)g(x)-f(x_c)g(x_c)
 =(f(x)-f(x_c))g(x_c)+f(x)(g(x)-g(x_c))
\]

给出准确可用的预算

\[
 \begin{aligned}
 C_{fg}&\le C_f C_g,& O_{fg}&\le O_f O_g,\\
 V_{fg}&\le V_f C_g+O_f V_g,& A_{fg}&\le A_f A_g,\\
 D_{fg}&\le D_f A_g+A_f D_g.
 \end{aligned}                                                   \tag{4}
\]

对静态因子 D 为零。将 (4) 加到原 U 的完整界，并保留原 L 的界，正好返回
现有 `finite_reference_bounds` 的三个字段。随后的 Cauchy 尾费用必须仍使用
这些外域界，不得将 jet 截断后的高阶系数当作零。

两个已执行的小范围有向求值均取 segment 419、归一子段
\([31/64,33/64]\)、\(x_c=1/2+i/512\)、\(h_x=1/4096\)，外半径
\(R_t=8,R_x=4\)。在这一声明范围，完整修正的实时间外角大小上界分别约
\(8.146844\times10^{-11}\) 与 \(3.872030\times10^{-10}\)。
这只是新有限参考修正的界，完全不是 δ5 真流误差或其残差。

另作了不同求值顺序的核对：先在固定复标签直接求完整 Fourier 值，再作准确
Bernstein 时间变换，与该接口“先变换所有系数、再形成角 jet”的两条输出相比较。
前、后腿各 16 个 Y/L 时间系数的有向差均包含零，差包络分别低于
\(2.9320\times10^{-55}\)、\(2.8920\times10^{-55}\)。这是实现的一致性检查；
完整尾界仍由上述解析有限求和与 (4) 取得，不能以区间重叠替代真实残差证明。

## 6. 重放、存储和仍须验证的输入

从课题目录执行：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_shared_dense_reference.py \
  --trace-dir data/phase_ring_continuation/exact_affine_step4_shared_knot_dense1032 \
  --leg forward --rays 1032 --degree 516 --segments-per-file 24 \
  --out-dir data/phase_ring_continuation/step4_shared1032_reference_forward

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_shared_dense_reference.py \
  --trace-dir data/phase_ring_continuation/exact_affine_step4_shared_knot_dense1032 \
  --leg backward --rays 1032 --degree 516 --segments-per-file 24 \
  --previous-reference data/phase_ring_continuation/step4_shared1032_reference_forward/manifest.json \
  --out-dir data/phase_ring_continuation/step4_shared1032_reference_backward

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_shared_reference_retarget.py \
  --forward-reference data/phase_ring_continuation/step4_shared1032_reference_forward/manifest.json \
  --backward-reference data/phase_ring_continuation/step4_shared1032_reference_backward/manifest.json \
  --target-object data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json \
  --target-root data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_root_tight.json \
  --target-H data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_dyadic_H.json \
  --Q-degree 128 --segments-per-file 48 \
  --out-dir data/phase_ring_continuation/step5_retargeted_reference

OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_retarget_reference_identity.py \
  --descriptor data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --out notes/2026-11-12-step5-retarget-exact-identities.json
```

构造器拒绝覆盖已有定义，应在缺失后的原路径或另一个明确新输出目录运行。
原始 δ4 234.7MB 轨迹、125.6MB U/L shards、15.4MB Q shards 暂作可重建本地数据；
本批只保存源码、定义 manifest、初值差、准确恒等式报告与输入哈希。
重建后只有匹配全部冻结哈希，才是同一个准确参考。若环境中的浮点选择重放未匹配，
必须记录新参考身份并重新验证其完整残差，不能把旧证书挂到新系数上。

新的 δ5 真实场 e0/e1、真实根和径向样条 germ、全部时间/角覆盖、复像、非零分母、
R60 累计管、真实参数源以及最终 Wiener/KAM 门都仍须直接验证。
此处有意没有添加 \(\Delta\delta\,Z\) 修正：参数改变本身应由新真实残差支付。
