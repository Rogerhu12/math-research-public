# 有限参考的完整复标签带非零导数门

2026-11-12，reproduce_newton。对应 R68 第 4 节。

**当前范围：算法、证明和已知有限多项式的独立预检已经完成；实际 δ₄/δ₅
参考分片的全域扫描尚未完成。** 本文不能作为当前真实参考的非零证书。
丢失的 δ₄ shared1032 原始轨迹正在用冻结入口重新积分；须先比较重新生成的
原始分片、准确时间和参考系数身份，之后才能调用本文入口。

冻结实现为 `scripts/fourfold_reference_derivative_gate.py`，SHA256
`a947f3b6bb93f254c22f8d9f526964899a4708cd4286b6029ddda0d5a1dcaa65`。
它读取已定义的有限 Fourier/Bernstein 参考，不调用真实场，不把有限参考的
导数自动认作真实流的 Jacobian。

## 1. 准确对象和坐标

初值标签记作 (x)，周期为 (2\pi)。物理角参考为

\[
 Y(v,x)=\frac{x}{4}+\sum_{j=0}^{7} B_j^7(v)U_j(x),\qquad 0\le v\le1.
\]

每个 (U_j) 是保存的有限实对称 Fourier 多项式：

\[
 U_j(x)=u_{j,0}+\sum_{k=1}^{K}
       \bigl(u_{j,k}e^{ikx}+\overline{u_{j,k}}e^{-ikx}\bigr).
\]

输入的 binary64 实部和虚部直接解释为准确 dyadic 数；均值虚部必须严格为零。
入口拒绝非 binary64 数组，避免在转成 Python float 时把较高精度输入无费用舍入。
这里的 (S) 总是 **归一化初值标签 (x) 的带宽**。
它与 R67 的物理角带宽不是同一个量；使用真实场证书仍须另付 (Y) 的复像包含。

定义

\[
 q=\partial_xY,\qquad q_j=\frac14+U_j',\qquad d_{j,k}=ik u_{j,k}.
\]

常项为 (1/4)，没有把归一化标签导数误写成物理角导数。
时间可正向或反向；只要准确时间段的定向与 manifest 一致，实插值坐标仍为
(v\in[0,1])，以下凸性门完全相同。

## 2. 两条复边界化为同一个实三角多项式

由准确实共轭对称性，(q_j(x-iS)=\overline{q_j(x+iS)})。因此两边界实部相同，
并且准确等于

\[
 g_j(x):=\operatorname{Re}q_j(x+iS)
   =\frac14+2\operatorname{Re}\sum_{k=1}^{K}
                    d_{j,k}\cosh(kS)e^{ikx}.
\tag{1}
\]

选择 (N>2K) 个等间距节点 (x_l=2\pi l/N)，令 (h=\pi/N)。所有节点的
闭邻域 ([x_l-h,x_l+h]) 覆盖实圆。取 Taylor 阶数 (p\ge2)，用完整有限频谱
同时计算

\[
 c_{j,l,r}=\frac{h^r}{r!}g_j^{(r)}(x_l),\qquad 0\le r<p.
\]

其正频率输入准确为

\[
 d_{j,k}\cosh(kS)\frac{(ikh)^r}{r!},
\]

负频率取该数的共轭。零频率仅在 (r=0) 为 (1/4)，其他阶严格为零。
`NativeSeriesFFT` 用有向复球 DFT 计算这些值。因为 (N>2K)，有限多项式没有
频率混叠；DFT 中所有舍入已在返回球内，没有以浮点节点值代替证明。
真值为实数，所以可以使用返回球的实部区间；实现同时检查虚部包含零。

## 3. 每个闭角格的完整余项

对任意实 (x)，有

\[
 |g_j^{(p)}(x)|
 \le 2\sum_{k=1}^{K}|d_{j,k}|\cosh(kS)k^p.
\]

因此每个半径 (h) 的闭角格，完整 Taylor 余项统一由

\[
 R_j=2\sum_{k=1}^{K}|d_{j,k}|\cosh(kS)
                         \frac{(kh)^p}{p!}
\tag{2}
\]

控制。设球运算给出各 (c_{j,l,r}) 的下端或模上界，则

\[
 m_{j,l}=\underline c_{j,l,0}
           -\sum_{r=1}^{p-1}\overline{|c_{j,l,r}|}-\overline R_j
 \le g_j(x),\qquad |x-x_l|\le h.
\tag{3}
\]

取全部节点的最小值 (m_j=\min_lm_{j,l})，即得到完整边界圆下界。
这一步包含节点间的变化，不是仅检查 DFT 节点。

若全部控制多项式的 (m_j>0)，在周期圆柱带上使用调和最小值原理，得到

\[
 \operatorname{Re}q_j(z)\ge m_j
       \quad (|\operatorname{Im}z|\le S).
\]

再由实时间 Bernstein 基的非负性和分割统一性质，

\[
 \boxed{\operatorname{Re}Y_x(v,z)\ge\min_jm_j>0}
       \quad(0\le v\le1, |\operatorname{Im}z|\le S).
\tag{4}
\]

所以 (|Y_x|\ge\min_jm_j)，可直接供 R68 使用。模上界用完整有限 Wiener 和：

\[
 |q_j(z)|\le\frac14+2\sum_{k=1}^{K}|d_{j,k}|e^{kS},
\]

取八个控制的最大值即可。此上界不要求参考与真实流相近。

如果 (3) 尚不为正且没有确认负的边界控制值，程序可增大 (N) 直到指定上限。
若某个控制节点的有向上界已经为负，增密不会使本项控制变正，程序记录该事实
并停止这个充分门。**一个 Bernstein 控制不通过，不能一般性地推出插值参考
的 (Y_x) 有零点。** 换用时间细分、其他零点自由 witness 或更窄带仍可能成功。

## 4. δ₅ retarget 的准确乘积费用

已定义的 retarget 不是只添加 ((H_5-H_4)/4)。准确初值修正为

\[
 a(x)=h_5(x)/4-U_{4,f,\mathrm{start}}(x).
\]

其中 (h_5=H_5-x)，所以它保留旧有限初值相对旧 (H_4/4) 的全部误差。
它由 `initial_correction.json` 中的整数和 (2^{122}) 分母准确规定。
定义还指定有限 (Q_f,Q_b)，并令

\[
 Y_{5,f}=x/4+U_{4,f}+Q_fa,\qquad
 Y_{5,b}=x/4+U_{4,b}+Q_b(Q_{f,\mathrm{end}}a).
\tag{5}
\]

这些是准确符号乘积；程序不对乘积做 Fourier 截断。对任意完整有限实对称
多项式 (P)，计算

\[
 W_0(P)=|P_0|+2\sum_{k>0}|P_k|e^{kS},\quad
 W_1(P)=2\sum_{k>0}k|P_k|e^{kS}.
\]

前腿静态因子 (b=a)。后腿 (b=Q_{f,\mathrm{end}}a)，使用

\[
 W_0(b)\le W_0(Q_{f,\mathrm{end}})W_0(a),
\]

\[
 W_1(b)\le W_1(Q_{f,\mathrm{end}})W_0(a)
                    +W_0(Q_{f,\mathrm{end}})W_1(a).
\]

对每个时间控制 (Q_j)，其完整导数费用为

\[
 F_j=W_1(Q_j)W_0(b)+W_0(Q_j)W_1(b).
\tag{6}
\]

以 (m_j-F_j) 代替 (4) 的控制下界，并把 (F_j) 加到模上界。
因为 (b) 与实时间无关，整个 retarget 仍是 degree-seven Bernstein 多项式，
这正好覆盖 (5) 的每一项。这里没有宣称有限 (Q) 是真实 Jacobian。

## 5. 身份、准确时间与连续性门

每个输入分片先检查 SHA256、字节数、形状、有限值、真实均值、源定义和准确时间
元数据。时间端点沿用 manifest 的有理数或有理倍数 \(\pi\)，不默认二进制近似
\(\pm\pi/2\) 就是准确端点。

顺序扫描时，前段的最后 Bernstein 控制与后段的第一个控制逐位相等才继续；
base 的 (U,L) 和 retarget 的 (Q) 都各自检查。resume 时也读取已完成区域的
最后一段作同样接缝检查。于是所读取有限函数在段内边界准确相接，相应初值导数
也相接。两腿之间的准确 lift 接合仍由 retarget 定义及其独立接缝证书负责。

每段结果立即原子保存，可使用 gzip 把报告保持在仓库单文件 5 MB 上限以内。
resume 要求完整身份相等；曾因未证明充分门而停止的报告不能直接跳过失败段
续跑，必须以新设置、新报告重新开始。源 hash 变化同样不能无声续接。

报告 `full_branch_nonzero_proved` 只有在覆盖该腿全部段、全部声明带宽且均通过时
才为真。局部扫描成功不转授完整腿；前腿成功不转授后腿。

## 6. 已完成的独立预检

入口 `scripts/fourfold_reference_derivative_gate_preflight.py` 做了三类校验：

1. 两模已知家族。其边界实部为
   (1/4+A\cos x+B\cos2x)，(B>0)，用二次式
   (1/4-B+At+2Bt^2)、(t=\cos x\in[-1,1]) 独立计算准确最小值包络。
   Taylor 门给出的连续下界没有超过这个真实最小值，并全部保持正。
2. 把一个第一频率系数改为 (-i/4)，确认已知负边界控制被检出，同时保持
   “充分门失败”口径；非 binary64 输入被拒绝。
3. 用准确给定的 dyadic 公式生成 degree 516、八个时间控制的完整有限多项式，
   在 (N=2048,p=6,S=1/512,160\) bits 下得到连续正下界
   (>0.23901098617)。此全尺寸计算 CPU 约 0.723 秒。

最终报告 `notes/2026-11-12-reference-derivative-gate-known-family-preflight.json`
SHA256 为 `3cea4fdb55b4650477a890e7f877636f934977bfe6edc00726da6f5592522e9e`。
它绑定本文冻结源。这里的人工 dyadic 家族不是 δ₄/δ₅ 的参考系数，成本数据
不能替代实际参考的非零输入。

精确重放预检：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_reference_derivative_gate_preflight.py \
  --out notes/2026-11-12-reference-derivative-gate-known-family-preflight-replay.json
```

在实际分片恢复并核对身份之后，完整 retarget 前腿入口为：

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_reference_derivative_gate.py \
  --retarget-descriptor data/phase_ring_continuation/step5_retargeted_reference/descriptor.json \
  --leg forward --widths 1/512 --nodes 2048 --max-nodes 8192 \
  --taylor-order 6 --bits 160 --resume \
  --out notes/2026-11-12-step5-forward-reference-derivative-gate.json.gz
```

后腿单独指定 `--leg backward` 和独立输出。若只验证旧有限 base，改用
`--manifest` 指向已核身份的单腿 manifest。若原始恢复导致参考系数或准确时间
改变，先建立新参考定义及新 retarget，不能沿用上述旧 descriptor 的身份。

## 7. 未付的后续输入

本文只解决 R68 中有限参考 (Y_x\ne0) 的一个可重放充分门。目前实际系数仍在
恢复，故本题全参考非零结论尚欠。真实场的全时间复域、(Y) 的像域、完整连续
缺陷 (Y_t-f(t,Y))、两腿总积分、Hardy/Wiener 端点和参数源均须分别支付。
R67 已有的单个实际时间段场多项式不会因本门存在而变成全返回证明。
