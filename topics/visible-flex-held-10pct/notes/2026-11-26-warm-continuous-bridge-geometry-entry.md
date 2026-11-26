# 新暖分支完整桥的连续度量、曲率与尺寸入口

日期：2026-11-26。维护会话：Astra-held10-06bbeb39-20261126。

这是新实际场的**可执行入口与数学接口说明**，不是新的已通过桥证书。
截至本记录，尚无实际 λ=1 暖场输入在本入口执行，旧 R60 数值没有迁移。
已真实执行的仅是末节的合成旋转例与接口检查。

## 1. 输入与同一张图

新增 warm_certify_bridge_geometry.py、check_warm_true_bridge_adapter.py；
实际小检查见 2026-11-26-warm-true-bridge-adapter-check.json。

入口要求对应 versioned accepted_input 接受的完整暖场、实际 physical.npz、
同场真核心 mean1168 证书/数组、同场完整 true-cut-height.json 及其逐叶记录、
同场 seam_bridge_cut_trace.py 输出。默认要求 λ=1；中间 λ 须显式
--allow-intermediate-lambda。目前支持已登记 v2、v3 和原暖 actual-DN；
尚未正式适配的新 actual-refinement KIND 会被拒绝。

直接实例化
[真高度入口](../scripts/resume_20261126/seam_certify_true_cut_height.py)
已经审过的 MeanMap。因此：

\[
 \theta(s,\psi)=\psi-\tfrac13e_*(s)\sin3\psi,\qquad
 F_*(s,\psi)=a_*(s)e_r(\theta(s,\psi))+G_*(s,\psi)+Z_*(s)e_z .
\]

\(G_*\) 的全部 \(3M+1\) 状态系数是保存场的共同右二 jet quintic
Hermite；最后节点取最后片左二 jet。\(e_*\) 是同一共同右二 jet spline
及原 late cutoff。桥上完整 core lift 恒为零，不是截去一个非零余部。
前缀与桥仍由
[动态 M 分片](../scripts/resume_20261126/seam_m3_prefix_pieces.py)
和 MeanMap 的共同定义连接。

\(a_*(s_b)=1,\ a_*'=-\sin\phi_*\)。三段 phase 的参数均按冻结二进制
常数的精确有理解释，最后一段解析延伸到实际物理终点，不把末端参数夹到 1。
\(Z_*(0)=0,\ Z_*'=M_*\)，其中 \(M_*\) 使用原 literal NumPy mean1168
节点、等正权、完整 Frenet mean 与 convection。

literal mean 节点 SHA256：
f4834f978de38046e374b020d2a928d293fc405f794159e40e2271f4ee9bd9cf。

此图没有被假称为 source GL64 radius、GL6 height 查询或浮点 PPoly 本身。

## 2. 真半径、mean 的 D2 与原全角 Gram 算法

R60 原 Fourier–Taylor 核先检查 GL64 值和指定 slope 的中间对象，再支付
真图转移。新适配层直接给出同一真原函数的 jet：

\[
 a_*'=-\sin\phi,\quad a_*''=-\cos\phi\,\phi',\quad
 a_*'''=\sin\phi(\phi')^2-\cos\phi\,\phi'' .
\]

TrueBridgeJets.profile 的 value 使用原 MeanMap.bridge 的 degree-40
真积分包围，导数使用上述恒等式。不是给另一个 GL 函数指定导数。
共同 Hermite \(Y_*,e_*\) 均取精确多项式导数；原有限 mean 和、Frenet
法向、正平方根及 convection 用原 D2 运算再微分两次。根或分母不能严格
包围为正时只二分，不能用剪裁制造域内结果。

所有 field/chart knots、cutoff、phase 拼点都入分片。拼点三阶导数可跳，
共同二 jet 不变；Taylor 余项只在各单侧片使用。

直接复用
[原 Fourier–Taylor Gram 核](../scripts/resume_m3/certify_bridge_metric_fourier_taylor.py)
的 GramVerifier：

- 状态频率仍 \(3j\)，与核心补弧控制频率分开；
- Laurent 半宽 \(\max(3M+1,3p+4)\)，不删小系数；
- 原指数 Fourier \(\ell^1\) 余项、实数卷积舍入界均不变；
- 先精确消去背景圆 Gram 项，再做区间；
- 每片中心 value/first 和整片 second 支付径向 Taylor 余项。

得到当前片相对于 \(g_*=ds^2+a_*^2d\theta^2\) 的算子上界
\(\varepsilon_*\)。全角由 Fourier 绝对和覆盖，不把采样作为连续结论。

## 3. 与原统一真尾目标相同的 \(\widehat g\)

桥和 mean 不改变。目标仍按
[已登记的统一真尾定义](2026-11-20-m24-bridge-true-tail-reference-metric.md)
在最后 \(L=1/1000\) 做一次 Hermite 校正。

True cut 的 \(R_c=.3,w_c=.08\) 均取 literal 精确有理值，
\(w_{R,c}=-7w_c/R_c,\ E_c=1+w_c^2\)。其内向弧长 radius 二 jet：

\[
 \left(R_c,-E_c^{-1/2},-\frac{w_cw_{R,c}}{E_c^2}\right).
\]

入口核当前 cut trace 的 source/physical/phase/port/background 绑定，
并调用同一 true_radius 精确有理 Taylor 积分**重算当前**
\(a_*(s_e),a_*'(s_e),a_*''(s_e)\)。旧 d0、radius 下界、尺寸与曲率
数字均不转移。

令 \(d_j\) 是该 true-tail jet 与这个唯一真 primitive 的差。在最后 L 内：

\[
 \widehat a=a_*+\sum_{j=0}^2(-L)^jh_j((s_e-s)/L)d_j;
\]

其余位置 \(\widehat a=a_*\)。
\(h_j^{(k)}(0)=\delta_{jk},h_j^{(k)}(1)=0\)，\(0\le k\le2\) 的恒等式用
有理多项式逐项验证。\(d_j\) 是唯一固定真数；interval 只包围该数，
不从 interval 任取 midpoint 再设计目标。

设片上 correction value 界为 \(D\)，且 \(a_{\min}-D>0\)，取
\(\eta=D/(a_{\min}-D)\)。目标 frame 换基
\(B=\operatorname{diag}(1,a_*/\widehat a)\)，故：

\[
 \|\widehat g^{-1/2}(F_*^*e-\widehat g)\widehat g^{-1/2}\|_{\rm op}
 \le(1+\eta)^2\varepsilon_*+2\eta+\eta^2 .
\]

这一项逐片实际支付，不设零。目标定义含 frozen profile、精确 s 域、
literal phase、true cut、L 和 Hermite 规则，并记录 canonical SHA；
定义不含 M 或未知状态系数。后续比较必须核同一目标定义，分别通过
两个场的有限证书不会自动变成 fixed-g convergence。

## 4. 曲率、全位置与外向支撑

几何复用
[原 R62 材料 frame 与二形式公式](../scripts/resume_m3/certify_prefix_metric_interval_taylor.py)。
桥上的 lift 为精确零。设：

\[
 U=F_s|_\theta,\qquad V=F_\theta/a_* .
\]

全部闭角盒包围 \(U,V\) 及导数，原 PrefixMetric.curvature 给归一二形式
算子上界。实际第一基本形式相对于 \(g_*\) 的最小特征值至少
\(1-\varepsilon_*\)，故再除该数得到实际主曲率上界。使用当前片
\(\varepsilon_*\)，没有混用另一 frame 的误差。

闭角盒从 0 无缝覆盖到真 \(2\pi\) 的外向上端点，数量至少
\(16(3M+1)\)。法向分母严格为正。外向约定：

\[
 n=-\frac{U\times V}{|U\times V|}.
\]

直接包围 \(|F_*|\) 与 \(F_*\cdot n\)。全桥 \(Z_*(s)\) 来自同场完整
真高度证书的实际逐叶 Darboux 原函数，不用旧入口高度，也不从单个 \(Z_c\)
倒推全段。

对 mean 叶 \([a,b]\)、mean 范围 \([m_-,m_+]\)、左端累计高度
\([z_-,z_+]\)，\([l,r]\subset[a,b]\) 上：

\[
 Z_*([l,r])\subset[z_-,z_+]+[l-a,r-a][m_-,m_+] .
\]

实现保留四个乘积端点，不假设 mean 正或高度单调。累计用精确有理
长度与 outward double endpoints 的精确有理解释。完整叶序列必须从
0 无缝到 \(s_e\)，不得跨 defining break；prefix、bridge、total 三组
和须与原证书逐字一致。所有叶边界再并入桥分片。

使用原充分窗口：
\(|k_i|<123/10,\ |F_*|<67/50,\ F_*\cdot n>87/1000\)。
这只支付桥，不单独推出全闭曲面、全时 reach 或全局嵌入。

## 5. 实际运行方式与覆盖门

每片通过且精确接受长度等于 \(s_e-s_b\)，才给
complete_actual_bridge_metric_geometry_certified；否则保存明确未决片、
真实失败原因和最后上界。metric gate 不大于 \(10^{-6}\)，默认
\(9.7\,10^{-7}\)。

~~~text
python warm_certify_bridge_geometry.py \
  --repo /path/to/repo \
  --source-run /runner/actual-lambda1/run.json \
  --physical /runner/actual-lambda1/physical.npz \
  --core-mean-certificate /runner/core/mean-certificate.json \
  --core-mean-intervals /runner/core/mean-intervals.npz \
  --true-height-certificate /runner/height/true-cut-height.json \
  --cut-trace-certificate /runner/cut/trace.json \
  --outdir /runner/bridge-continuous
~~~

完整逐叶数据和径向网格放 repository 外。入口不调用 BVP/DN，不改场，
不把中间 λ、linear tail 或未知 loader 版本改标为最终 actual-DN。

## 6. 已真实执行的小检查

check_warm_true_bridge_adapter.py 实际 exit 0；合成 \(M=2\) 旋转零扰动、
literal mean1168，在三段 phase 内及实际末端共五点，以独立 90 位计算检查：

- 真 \(a_*\) 的零至二阶、\(a_*'\) 的零至二阶包含；
- \(M=\cos\phi\) 及一、二导数包含；
- 256 个完整闭角盒的旋转曲率、尺寸、外向支撑包含；
- 允许负 mean 的累计 Darboux 四端点乘积。

五点最大原 Gram interval 上界：
\(6.137931484059562\,10^{-13}\)。这是合成接口结果，不是实际暖场 metric。
最后实际测试源码 SHA256：

- driver：bd471b11edbae3c1309dfbc9dd9ebab00fbae40b0e0909f78f6571c4b6ccff56；
- checker：1400618e8b8b276fc3e26ac6ce6be51c0008211f10532c782b3949d3f152b234。

两源 py_compile 也实际 exit 0。

## 7. 后继 R61 必须重新支付的预算

原 R61 Hermite 恒等式和局部再认证公式可复用；旧 M24/λ=.002 的 trace、
κ/Γ3、mean、位置和 metric 数字不能转移。后继最小输入是同场完整真核心
point/closed-box 数组、mean1168、动态 M 共同 Y/e/profile 与真高度逐叶数据。

1. 重算固定材料角的
   \(\Delta_j=\partial_s^j(F_*-\Gamma-s e_z)|_{s=0}\)，\(j=0,1,2\)，
   及各自 θ 零、一、二阶上界。保留 chart 二加速度与完整核心的相消，
   不把 \(e_{ss},Y_{ss}\) 或竖向 mean 单独清零。
2. 原入口脚本硬编码的 \(\|\Gamma''\|<2,\|\Gamma'''\|<5.3\) 必须换成
   新 true-core 实际全角界；\(e(0)-\mathrm{warp}\)、Y 与完整投影之差、
   \(M(0)-1,M'(0)\) 都重新绑定。
3. 在原第一 profile 片内固定 L，核对 profile 初端精确 jet、\(a_{\min}>0\)
   及 Hermite 两端二 jet。不复用“旧 L 已通过”的数值结论。
4. 对 \(A_j=L^jh_j(s/L)\)，用新 trace 算
   \(P=\sum|A_j|\|\Delta_j\|\)、
   \(B_0=\sum|A_j'|\|\Delta_j\|\)、
   \(B_1=a_{\min}^{-1}\sum|A_j|\|\partial_\theta\Delta_j\|\)、
   \(d=(B_0^2+B_1^2)^{1/2}\)，并**重算局部**原图误差 ε，支付
   \(\varepsilon_{\rm new}\le\varepsilon+2\sqrt{1+\varepsilon}d+d^2\)。
5. 新二阶 correction budget 要重算局部曲率、法向变化、位置与 support。
   未修补段完整 prefix position/support 也必须来自新场同一真高度，
   本桥数字不能替代。
6. 修补图可有竖向零模；修补段不再声称满足原 mean 演化式。同一显式修补
   规则必须保留到 fixed-g C2 比较、全时运动和最终 seam 中。

上述均仍待实际输入执行，不被本桥完成标志覆盖。

