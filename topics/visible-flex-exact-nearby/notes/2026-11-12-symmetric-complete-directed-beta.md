# 原 sym step02 图的完整有向 beta 积分

## 1. 本文件真正完成的结论

对固定输入
[type_fixed_step02_analytic_smoothing_inputs.npz](../data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz)，
SHA256 为

    bd9b4d14b104183f80feaeea4c4c1a5d8c40b511bd58974dbca1bda842474532

的显式对称化无限 R33 primitive，采用 R37 全核心的
\(\ell=\partial_\theta\log(F_z/r)-\partial_\theta\log|F|\)
零阶口径，R50/R52 定义的物理 \(n=4j\) 完整往返一阶相位系数满足严格界

\[
\boxed{36.79967508215<\beta<36.80349990665.}
\tag{1.1}
\]

这里的 \(\beta\) 是 \(1/j\) 的系数；没有把 \(1/n\) 和 \(1/j\)
混用。完整合并报告是
[beta-symmetric-complete-enclosure.json](2026-11-12-beta-symmetric-complete-enclosure.json)。
它逐一检查全部 167 个原始径向多项式 span，由 259 个被接受子区间加腰部
小段构成无缺口、无重叠的精确覆盖。

对 R48 的 nearby D5 目标

\[
\rho_*=\frac{15121+\sqrt5}{27422},\qquad
13711\rho_*^2-15121\rho_*+4169=0,
\]

其半整数共振的 primitive norm 为奇整数 \(Q\)。同一 \(\beta\)
相对于 R34 的危险格有

\[
\operatorname{dist}\left(
 \beta,\frac{\pi}{2\sqrt5}(2\mathbb Z+1)
\right)>0.42801799599.
\tag{1.2}
\]

式 (1.2) 是本原图相位的算术结论。它不把本图的 \(\beta\)
转授给另一个 mean、D5 center 或 exact affine 图，也不声称原图实际
principal return 已被调到 \(\rho_*\)。真实参数点的相位应单独计算。
完整传递余项、低块及非线性闭合仍各需相应的输入。

## 2. 实际对象和有限部

原始保存量被解释为准确 binary64 数据。先在原始 B-spline 系数层固定数据，
再精确施加半径、beta 的偶对称及 gamma、高度的奇对称。
高度由保存的 slope 做准确原函数；不使用另存的四舍五入高度样条。
角方向使用 R33 的无限 primitive；有限 DFT 只作为其带严格尾项的计算表示。
两项对称化均在整个对象层实施。

在旋转柱坐标基中记

\[
C=F_\theta\times F_r,\quad A_2=C\cdot C,\quad
R_2=F\cdot F,\quad h=C\cdot F,
\]
\[
(l,m,n)=C\cdot(F_{rr},F_{r\theta},F_{\theta\theta}),\qquad
(a,b,c)=(-n,m,-l)/A_2.
\]

这里的 \(a,b,c\) 已把 R37 的 \(\zeta^2\) 公因子消去。
设 \(K=K_0(r)\) 为同步目标度量
\(E(r)dr^2+a_{\rm rad}(r)^2d\theta^2\) 的曲率，
\(\omega=(K_F-K)/a\)，\(\widehat c=(b^2+K)/a\)。
R50 的角分部后真实密度为

\[
J=
\frac{
d+\omega(\ell^2+\ell f_\theta)
-\frac14(af_r^2+2bf_rf_\theta+\widehat c f_\theta^2)
}{\sqrt{-K}},
\tag{2.1}
\]

其中 \(f_r=K'/(2K)-2(\log\zeta)_r\)，
\(f_\theta=-2(\log\zeta)_\theta\)。
式 (2.1) 中的 \(d\) 是实际几何 \(d\) 乘 \(\zeta^2\)，不是独立挑选的势。
精确公式和除去 \(\zeta^2\) 的恒等式见
[恢复后的根 collar 说明](2026-11-12-recovered-directed-root-collar.md)。

由径向偶对称及物理频率 \(n=4j\)，

\[
\beta=\frac12\left[
\int_0^b\langle J(r,\cdot)\rangle_\theta\,dr
+\operatorname{FP}\int_b^t
  \langle J(r,\cdot)\rangle_\theta\,dr
\right].
\tag{2.2}
\]

两项之间的加号至关重要：collar 积分是 Hadamard 有限部，
不能将其看成普通正积分再另行截断发散项。
真实唯一正根和准确固定切口满足

\[
.23836991573146337267349149754020
<t<
.23836991573146337267349149759844,
\]
\[
b=\frac{1072423152036779}{4503599627370496}.
\tag{2.3}
\]

根由已有有向唯一性证书初始化，再用含无限 primitive 尾的 interval Newton
收紧；没有用普通浮点根作为准确根。

## 3. 根 collar 已付的完整误差

以 \(\rho=t-r\) 和真根 deflation 写

\[
\langle J(t-\rho,\cdot)\rangle_\theta
=\rho^{-5/2}g(\rho),\qquad
g(\rho)=\langle G(\rho,\cdot)\rangle_\theta.
\]

采用 R52 的 24 阶 Taylor 积分、完整角 trapezoid 误差及真复域尾界。
计算参数为 Arb 192 bits、径向 series precision 72、
primitive quarter nodes 512、角 nodes 2048，
\(\rho\) 圆盘半径 \(0.0006\)，归一角 \(x=4\theta\) 宽度 \(0.02\)。
原始输入的 Cauchy 半径为 \(0.003\)、\(E\) 半径 \(0.0025\)，
输入角宽度 \(0.32\)。

结果为

\[
1305.4032588697<I_{\rm collar}<1305.4032591712.
\tag{3.1}
\]

其中径向 Taylor 尾不超过 \(1.50703912\,10^{-7}\)，
角误差不超过 \(1.334537\,10^{-13}\)；全部系数球和尾误差已合并。
证明不是对离散 \(\rho,\theta\) 的采样检查：所有分母都在完整复圆盘和
连续角覆盖上检查，\(\kappa_0^2=-K/\rho\) 用真根可去因子的积分公式处理。
细节、25 个系数球及全部域门见
[完整 collar 报告](2026-11-12-beta-recovered-full-collar-enclosure.json)。

## 4. Bulk：所有真实 knots、无限角尾和角求积

Bulk 取 \(r\in[0,b]\)。从全部冻结 scalar spline 的正、负 binary knots
生成准确有理数分区；即使两相邻 knots 在 binary64 中只差极小距离，
也保留该非空 span。每一个原始 span 明确选择同一多项式延拓。
选择器使用准确 Fraction 中点，不能将中点转成 float 后靠端点排序选侧。
最高 scalar degree 为 20，先在 21 项容量下生成完整标量多项式，
后续三 jet 由这同一多项式得到。

每次被接受的径向子区间执行下列连续门：

1. 完整无限 primitive 的 Fourier alias 和尾项经 R52 的解析预算补入。
   所有 DFT 蝶形使用 outward binary interval 运算；普通 FFT 不作为证明。
2. \(E,E',E''\) 从同一个有限 primitive 的 Parseval 表示构造，并分别补入
   含无限尾的积误差。目标 \(K,K'\) 因而来自同一个准确对象。
3. 在复积分所需的 \(r\) 域检查 \(\operatorname{Re}(-K)>0\)，
   以及 \(A_2,R_2,h,a,F_z\) 的真实除数门，采用同一解析平方根支。
   不通过的复域返回非有限值，由 Arb 积分器或外层继续细分。
4. 角求积使用 \(x=4\theta\) 上的完整 \(A=1024\) 点梯形公式。
   计算借助准确角反射只求一半节点，但其权重准确恢复全角公式。
   \(|\operatorname{Im}x|\le0.02\) 上的连续 \(J\) 界 \(M_J\)
   产生误差
   \(2M_Je^{-0.02A}/(1-e^{-0.02A})\)。
   覆盖还包括相邻节点间的 \(\pi/A\) 实角间隙。
5. 每个原始 span 的允许绝对半径为 \(0.0002\)；
   二分后的预算按准确区间长度分配。
   能用完整区间值直接积分的子段直接接受，否则用 Arb 验证复积分。
   接受前径向误差和完整角误差分别通过其预算门。

其中 \(F_\theta=a_{\rm rad}T\)，
\(F_{r\theta}=a_{\rm rad}'T+a_{\rm rad}T_r\)，
\(F_{\theta\theta}=a_{\rm rad}T_\theta\) 使用准确切向恒等式，
没有对截断 primitive 的高角导乘上虚假的 \(N^2\) 误差。
复点上的 dot/cross 均为双线性延拓，没有取复共轭。

腰部 \(0\le r\le2^{-20}\) 单独使用准确奇对称：
\(F_z/r\) 与 \(F_{\theta z}/r\) 由各自一阶径向导数的积分表示控制。
连续区间的导数范围同时控制其平均值，因此商的区间仍包含真实值。
该段总积分落在

\[
[-7.224175484\,10^{-6},\,7.224175484\,10^{-6}].
\tag{4.1}
\]

这避免在包含 \(r=0\) 的区间直接除 \(F_z\)。

## 5. 完整覆盖和加总

三个独立任务的原始 span 范围为 \(0\ldots3\)、\(4\ldots83\)、
\(84\ldots166\)，分别接受 14、123、122 个子区间。
三个任务均无失败叶片。中间的 analytic evaluation 拒绝只是积分器的
正常区间缩小过程；这些被拒绝复域没有作为证明输入接受。

每份分片报告保留 complete=false，因为它单独没有全域覆盖。
合并器重新生成准确 knot 分区，并逐个原始 span 校验：
首尾相等、每一相邻端点完全相同、每段正长度、没有遗漏或重叠。
合并器还重新检查所有输入和冻结 source 的 SHA256、
共同 collar 切口和腰部宽度。
满足这些条件后才输出完整报告的 complete=true。

不能用 JSON 中为显示而缩短中心的 ball 字符串作精确加总。
合并器将分别保存的 lower、upper 端点球取并，
再用 Arb 192 bits 加总。这样完整 bulk 满足

\[
-1231.803908705455
<I_{\rm bulk}<
-1231.796259357904.
\tag{5.1}
\]

更精确的端点球全部保留在最终 JSON 中。
式 (5.1) 与 (3.1) 按 (2.2) 合并给出 (1.1)，完整 beta
半径小于 \(0.001912413\)。原普通高精度诊断约 \(36.801611\)
被这一独立有向区间包含；该诊断不参与证明。

## 6. 危险格的实际算术检验

令 \(S=2\sqrt5\,\beta/\pi\)。合并后的 Arb 运算给出

\[
52.38526040315<S<52.39070564509.
\]

最近危险 norm 是 \(Q=53\)，其距离下界为

\[
\operatorname{dist}(S,2\mathbb Z+1)
>0.60929435491.
\]

合并器枚举包含这个区间的整数窗口内全部奇整数，并用显式距离至少 1
控制窗口外的格点，故不是只检查预先猜出的最近格点。
再乘 \(\pi/(2\sqrt5)\) 给出 (1.2)。
R34 的有限 cutoff 还需要同一真实传递的二阶余项常数及匹配的主旋转；
这里没有免去那些门。

## 7. 复放和冻结清单

计算目录为本课题目录，所有输入、命令和 SHA 对应重置后的重算，
不依赖已丢失的旧 executor 状态。

Bulk 使用：

    OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_bulk_interval.py --frozen-inputs data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz --bits 128 --quarter-nodes 256 --angles 1024 --absolute-tolerance .0002 --eval-limit 64 --cell-depth 10 --max-cells 4 --out notes/2026-11-12-beta-recovered-bulk-part00.json

第二段将 --start-cell 设为 4、--max-cells 设为 80，输出 part01。
第三段将 --start-cell 设为 84，去掉 --max-cells，输出 part02。
输出文件的耗时字段可变化，数学区间和完整覆盖须重新验证。

合并命令：

    OPENBLAS_NUM_THREADS=1 python scripts/fourfold_phase_beta_combine.py --frozen-inputs data/phase_ring_continuation/type_fixed_step02_analytic_smoothing_inputs.npz --collar notes/2026-11-12-beta-recovered-full-collar-enclosure.json --parts notes/2026-11-12-beta-recovered-bulk-part00.json notes/2026-11-12-beta-recovered-bulk-part01.json notes/2026-11-12-beta-recovered-bulk-part02.json --out notes/2026-11-12-beta-symmetric-complete-enclosure.json

冻结文件如下；表中的短名均在本课题 scripts/ 或 notes/ 下。

| 文件 | SHA256 |
|---|---|
| fourfold_phase_beta_interval.py | ff159224bc1870b7580ef6e5f0370a4fcc385ed556d947003a0bb1667e6f4b0f |
| fourfold_phase_beta_bulk_interval.py | 4b9d6bf8d4b0d0c962eb32df9051b3b58fa1e25d7612e2bcef259572a9b15a76 |
| fourfold_phase_beta_bulk_box.py | b880a940d30860ed0998509b1a29f7b1f13ac5ac646f4628d91ea87ea3ccba4a |
| fourfold_phase_beta_combine.py | 9f484b65819f010b0f31e17d489998c37161b8b83d6d0b7d65161dd8a2ef3888 |
| beta-recovered-full-collar-enclosure.json | 7a1687cc304cc29334de3e078c4ce427486f76183a517ed3b465c915802a0200 |
| beta-recovered-bulk-part00.json | e32c6678163a943dd39b6f1c084433ad36a658aa3f98d8401f898eb03039643d |
| beta-recovered-bulk-part01.json | dfe261fca6954d6fb685ecd366bf66011605d0150593a7fb6161025d47d4efa2 |
| beta-recovered-bulk-part02.json | ef84291f977513ffdf61b1f673eba217c2cf22d31fc4ba6619d187861b556d7b |
| beta-symmetric-complete-enclosure.json | da84c1a8ff5b1a5b00d33c236d37752a5ffa4d187bc88115f99db473742c52f2 |

本证明完成原图实际一阶相位的完整有向积分及上述算术距离。
当前 exact affine 参数点继续沿同一算法重算；它的输入 hash、根、cut 和
collar/bulk 报告必须全部重新匹配。
