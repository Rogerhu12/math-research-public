# δ5：完整物理角圆与整个普通时间段的复外域

2026-11-12，constructive_route。

**已完成的有限证书：δ5 的整个第 419 时间段、所有必需 scalar germs，
物理角全圆及 \(|\operatorname{Im}\theta|\le1/64\)、复时间 \(|u|\le3\)。**
每个 germ 都严格分离 D 和 −K，证明实际特征场全纯并给出完整模数。
这是一项完整域输入；没有宣布参考残差、累计流误差或 KAM 已通过。

## 1. 准确对象、时间与所有 germs

真实场使用

\[
 \delta_5=-7789843107295549/4611686018427387904,
\]

对象与根证书分别为
`type_fixed_step02_d5_exact_affine_step5_object.json`、
`type_fixed_step02_d5_exact_affine_step5_root_tight.json`。
原点 inputs SHA 为 `0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b`，
方向 SHA 为 `8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab`。
本次重新细化的是 δ5 自身的真实无限 primitive 根；完整有向 Newton 轨迹保存在报告。

时间网格来自 δ4 共享 1032 条参考的第 419 段，仅作为新参考的已选网格：

\[
 \tau_a=4466727694628647/9007199254740992,
 \qquad
 \tau_b=282639970307159/562949953421312.
\]

这与旧 δ3 shared516 的第 419 段不是同一对时间端点。
写 \(\tau=\tau_c+h u\)，其中 \(\tau_c=(\tau_a+\tau_b)/2\)、
\(h=(\tau_b-\tau_a)/2\)，并令 \(r=t(\delta_5)\sin\tau\)。
从真实根包和全部准确原始/反射 knots 计算的实径向像要求三个闭 common spans。
下表的所有端点共同以 \(2^{56}=72057594037927936\) 为分母：

| germ | 左端分子 | 右端分子 |
|---|---:|---:|
| 0 | 8106479329266893 | 8173936700574839 |
| 1 | 8173936700574839 | 8173936700574847 |
| 2 | 8173936700574847 | 8286623314361713 |

中间 span 长度准确为 \(2^{-53}\)。没有将它删去或并入旁边的 knot。
每个 span 的准确径向多项式都分别解析延拓到整个复时间盘。
这些延拓只控制实际场落在其本 span 内的那一部分，不宣称实际跨 knot 函数解析。
覆盖列表和闭区间相接按 Fraction 检查；全部三个延拓均通过后，才给整个实际段的结论。

## 2. R59 的适用范围与分母比例

使用已完成的
`type_fixed_step02_d5_parameter_modulus_complex_angle_1over64.json.gz`。
它覆盖同一原点/方向产生的**独立控制点盒**，准确参数区间为 JSON 中 binary64
\([-.01,.01]\)，实径向 \(|r|\le.24\)，物理角宽度为准确 \(1/64\)。
程序把参数端点和 δ5 都转换为 Fraction，核对 δ5 在盒内，并核对输入和方向 SHA。
准确 affine 曲线是该独立盒的子集；这里没有用盒的任意点继承共同 target 根。
当前真实根和 K 始终来自明确的 δ5 affine 点。

移动 frame 的量与 R59 完全相同：

\[
 D=PcQ-uv=-n/a^2,\quad M=pcQ-qv=-m/a^2,
 \quad W=Q^2+v^2=G/a^2.
\]

这里的 frame 投影 Q 与退化目标商 Q 不同。全部点积均按复双线性延拓。
在程序保存的 `sign` 约定下，实际场是

\[
 f=\frac{d\theta}{d\tau}
   =-r_\tau\frac{M+\operatorname{sign}\sqrt{-K}\,W}{D}.       \tag{1}
\]

u 是构造解析盘的归一时间，报告中的 f **没有再乘 h**。
R59 的另一支命名可与这里相差一个 sign；D、模数和不为零结论不受支名影响。

R59 对所需实径向闭单元给出直接 D 模长下界，以及 n 模长下界和 a 上界。
后者还给 \(|D|\ge |n|_-/a_+^2\)。两种已证明下界可以取较大者。
整个实锚径向包若与多个闭单元相交，则取覆盖这些单元的共同下界。

## 3. 外推 germ 必须回到自己的真实实锚

不能无条件使用 \(|D_g(0,\theta)|\) 的 R59 下界：共同时间中心可能在
另一个 span，当前 germ 在该中心只是多项式外推，未必等于实际图。

若真实 \(r(0)\) 的整个根包位于所选闭 span 内，取 \(u_a=0\)，并用
R59 覆盖这个真实径向包。否则选本 span 内离中心最近的准确有理端点
\(r_a\)，按同一个真实根定义

\[
 u_a=\frac{\arcsin(r_a/t(\delta_5))-\tau_c}{h}.             \tag{2}
\]

该点属于所选 span 的闭包。原样条的 C² 拼接保证这里的 Fr、Fθθ 等
实际几何 jet 与本 germ 相同，因此 R59 的真实图 D 下界确实适用于
\(D_g(u_a,\theta)\)。式 (2) 用 Arb 有向计算，且全包严格位于较大时间盘。
随后才支付整个复盘上 \(D_g(u,\theta)-D_g(u_a,\theta)\) 的变化量。

这样覆盖了两个左侧 germs 的外推中心问题；没有把真实轴对称或实际径向
中心的结果默认移给另一个解析延拓。

## 4. 真系数与两个独立的外域模数

本次设置：内部时间半径 R=3，较大时间半径 S=4；内部物理角条带
\(\Sigma=1/64\)，较宽物理角条带 \(\Sigma_*=1/32\)；时间次数 40，
即 m=41 个系数；物理角一周期 N=1024 个准确等距节点，保留 \(|k|\le255\)。
primitive 的 quarter Fourier 节点为 512，Arb 精度为 192 bits。

`uniform_primitive` 先生成真无限 Fr 的各时间系数包。它在有限 Fourier
原函数系数上加入已付的无限 primitive 误差，随后才形成 D/M/W；没有把
有限 primitive 的角导数替代真实切向量。有限相位及其角导数用严格 FFT
在同一网格求值。`f_invariants` 只形成 D/M/W，不除以 D，也不取曲率平方根。

对每个 F=D,M,W 的 germ，在
\(|u|\le S, |\operatorname{Im}\theta|\le\Sigma\) 和
\(|u|\le S, |\operatorname{Im}\theta|\le\Sigma_*\)
分别计算上界 \(M_{F,\rm time}\)、\(M_{F,\rm Fourier}\)。前者支付时间尾，
后者支付 Fourier alias 和遗漏模。两者不混用一个不必要地宽的大常数。

这些外模来自 `coarse_outer_invariants`：取完整一周期实角区间及复角宽度，
在整个较大复时间盘上用真正无限 X 的 Fourier 衰减界、有限相位和移动
frame 的无分母恒等式形成。区间 FFT 产生的宽盒高频噪声不被当作真实谱。
同一较大时间盘还分别检查实际 a 和 E 的非零门，取得真实 K 的全纯性与模数。

## 5. 完整 Fourier 误差与时间尾

令归一角 \(z=4\theta\)，内部/外部角宽分别为 \(s=4\Sigma\)、
\(s_*=4\Sigma_*\)。若

\[
 F(u,z)=\sum_{i\ge0}F_i(z)u^i,\qquad
 |F(u,z)|\le M_{F,\rm Fourier}\quad(|u|\le S,|\Im z|\le s_*),
\]

则 \(|\widehat F_{i,k}|\le M_{F,\rm Fourier}S^{-i}e^{-s_*|k|}\)。
N 节点的 DFT 对 \(|k|\le K<N/2\) 的 alias 绝对费用为

\[
 A_{N,K}=\sum_{|k|\le K}e^{s|k|}
   \frac{e^{-s_*(N-|k|)}+e^{-s_*(N+|k|)}}{1-e^{-s_*N}}.       \tag{3}
\]

遗漏的真实 Fourier 模费用为

\[
 T_K=\frac{2e^{-(s_*-s)(K+1)}}{1-e^{-(s_*-s)}}.             \tag{4}
\]

所以每个真实时间系数的完整 Wiener 范数都有严格上界

\[
 A_{F,i}=\sum_{|k|\le K}|\widetilde F_{i,k}|e^{s|k|}
      +\frac{M_{F,\rm Fourier}}{S^i}(A_{N,K}+T_K).           \tag{5}
\]

第一项使用已含所有有向舍入和无限 primitive 费用的系数球上界。
(3) 来自所有非零 l 的 \(k+lN\) 几何和；(4) 来自所有 \(|k|>K\) 的几何和。
不存在只检查有限频率后把其余真实模设为零的步骤。

对于 \(|u|\le R<S\)，全部未知时间项另由较窄角域支付：

\[
 B_F(R)=M_{F,\rm time}\frac{(R/S)^m}{1-R/S},\qquad
 |F(u,\theta)|\le\sum_{i=0}^{m-1}A_{F,i}R^i+B_F(R).       \tag{6}
\]

顺序是先完整支付每个已保留时间系数的全部 Fourier 模，再对真实 F 支付全部
未知时间系数。因此没有遗漏“时间高阶且角高阶”的角落。
本次 (3) 小于 \(1.751\times10^{-34}\)，(4) 小于 \(3.715\times10^{-6}\)。
D 的 (6) 时间尾在三个 germs 中均小于 .003071。

令 \(\alpha\ge|u_a|\)。因为常数时间项准确相消，完整锚点变化量满足

\[
 \Delta_D=\sum_{i=1}^{m-1}A_{D,i}(R^i+\alpha^i)
   +M_{D,\rm time}\left\{
        \frac{(R/S)^m}{1-R/S}+\frac{(\alpha/S)^m}{1-\alpha/S}
     \right\}.                                             \tag{7}
\]

这是比较同一个真实 germ 在 u 和 u_a 的表达，不是把独立中心误差相减。
若 R59 真实锚的下界为 d_a，则 \(|D|\ge d_a-\Delta_D\)。
本次每一个差都严格为正。

## 6. 曲率平方根与完整场模数

K 没有角变量。对其真实时间系数及较大时间盘模数应用 (6) 的普通标量版本，
包住整个内部时间盘，并证明 \(\Re(-K)>0\)。因此其中有与实双曲片的正
平方根一致的单值解析 \(\sqrt{-K}\)。这项费用独立于 D 门。

\(r_\tau=t\cos\tau\) 在复盘上满足
\(|r_\tau|\le t_+\cosh(|h|R)\)。将此界、\(\sqrt{|K|_+}\)、
M/W 的完整 (6) 模数和 D 的正下界代入 (1)，给出整个物理角/时间域的
真实 f 模数。程序也用准确商微分形成 fθ、fθθ 的保守上界；它们仍较大，
不用于猜测真流的放大率。较小角带上的导数也可直接从本次 f 全纯模数
使用 Cauchy 取得。

各 germ 的严格共同域结果如下；表中下界向小取整、上界向大取整。

| germ | \(|D|\) 下界 | \(\Re(-K)\) 下界 | \(|f|\) 上界 |
|---|---:|---:|---:|
| 0 | .16273449 | .57694455 | 5.952020 |
| 1 | .16564287 | .57694477 | 5.846591 |
| 2 | .22500614 | .57694499 | 4.303428 |

因此对这整个实际段及所有 physical θ，可共同使用
\(|D|>.1627\)、\(\Re(-K)>.57694\)、\(|f|<5.953\)。
尤其得到真正的联合 Cauchy/Fourier 输入

\[
 |\widehat f_{i,k}|\le 5.953\,3^{-i}e^{-|k|/16},          \tag{8}
\]

其中 k 是归一角 \(z=4\theta\) 的 Fourier 频率，i 是归一时间 u 的次数。
(8) 可供同一对象、同一时间段的整圆 Fourier 验证使用；不能移到别的时间段、
δ4 或旧 δ3 的第 419 段。对于活跃 germ 不同的实际时间子集，使用相应解析
延拓的界；不把实际跨 knot 函数整体展开为一个解析级数。

## 7. 源、重放与准确范围

源码：`scripts/fourfold_phase_full_angle_time_domain.py`。
完成报告：
`data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json`，
SHA `414a8cd3f1704c0abe7aee3b0b90a33c19e44ed425912898f4293c5a79487dcd`。
报告保存全部输入/依赖 SHA、准确控制参数包含关系、完整根细化、所有 spans、
每个真实锚、保留 DFT 范数、完整真系数范数、两个外模、所有尾费和接受条件。

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_full_angle_time_domain.py \
  --retarget data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --segment 419 --time-radius 3 --larger-time-radius 4 \
  --theta-strip 1/64 --wider-theta-strip 1/32 \
  --time-order 40 --angles 1024 --cutoff 255 --primitive-nodes 512 --bits 192 \
  --out data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json
```

本次不读取大型参考 shards；只从已哈希的定义 manifest 取准确时间网格。
场、根、几何 jets 全部按新 δ5 对象重新计算。
执行约 105 秒。没有把粗 fθ、fθθ 界用作真实流指数，也没有由本域证书
推断整个 reference 的复像或真实累计误差已付。
