# 自然单帽初场、主体度量设计与直接实际度量审计

日期：2026-11-14。状态：**接口与人工开发检查；实际初态尚待本公开仓库 Actions**。

本文件对应三个独立新脚本：

- `scripts/frame_body_metric_design.py`；
- `scripts/polygonal_tail_natural_extension.py`；
- `scripts/frame_collar_natural_body_audit.py`。

既有 ellipse/frame/enriched/六帽/饱和热源文件均保持原字节。新 runner 没有非线性优化调用，也不在本地评价真实 `c0`、`c1`。这里没有构造完整闭曲面，没有等距、嵌入或整体 reach 结论。

## 1. 本次改变的依据

真实 run `43612971265` 的 GH 初门通过，且只有一个固定 GH32 的 250 次求解。最终同参数 GH32/64 的 R 差约 `1.26e-5`，不能解释主体约 `1.47` 的纯切向 R 缺口及补丁约 `2.55` 的 R_W 缺口。主体的实际 `E−1` 峰约 `1.91`，也不是辅助 frame 正交性已经解决的量。完整数字及范围见 [实际几何审计](saturated-heat-actual-geometry-audit-20261114.md) 和 [独立来源审计](saturated-heat-provenance-audit-43612971265-20261114.md)。

所以本次不是再增加同模型迭代，而是把两个变化分别显式化：

1. 主体允许一个正半径的有限度量设计空间，但完整尾补丁仍采用原种子半径；
2. 尾部初场采用六个真实单圆柱帽的自然标量延拓，替换具有已知三阶 Cauchy 缺项的饱和反射初场。

另外新增直接审计实际重构 `X` 的两项度量方程。原 R 仍完整保留，不把不同目标的成本混作一次迭代下降。

## 2. 主体度量的准确身份

令原种子为 `a_seed(t)`，核心缓冲终点为 `t_c`，平尾起点为 `t_f`，补丁宽 `h=1/10`。控制区间为

\[
I_b=[t_c,t_f-h].
\]

默认有 5 个系数，令

\[
\ell(t)=\sum_{j=1}^{5}c_j B_j(t),\qquad
a(t)=a_{\rm seed}(t)e^{\ell(t)}.
\]

`B_j` 是准确节点定义的五次 clamped B 样条，首末各丢弃三列，再乘 `16 x²(1−x)²`。因此在控制区间两端均为 `O(distance^5)`，区间外准确零。

这保证：

- 核心常半径、核心入口的 `a′` 三次首项保持；
- 整个 `[t_f-h,L]` 的半径及所有本次所需 jets 保持原种子；
- 半径始终为正；
- **种子的中段负曲率符号或总积分不随设计继承**，每个设计必须重新审计。

完整参数导数为

\[
\partial_j a=a B_j,\qquad
\partial_j a'=a'B_j+aB_j',
\]

\[
\partial_j a''=a''B_j+2a'B_j'+aB_j'',\qquad
\partial_jK=-B_j''-2\frac{a'}aB_j'.
\]

准确 family 身份包含原 seed 的准确定义、支撑端点、完整有理节点、列选择及权函数。系数按 `Fraction.from_float` 记录为准确 binary64 有理数。`replay_coefficients` 拒绝不属于这一写出格式的有理数，避免把例如 `1/3` 静默换成新的浮点身份。

`frozen_definition` 与独立的冻结构造器支持先设计再冻结：冻结后参数维度从 `234+5` 回到 `234`，但仍使用原先的 5 个度量基及原节点，不把旧系数解释到新基上。人工检验中冻结前后 `X,X_s,X_θ,X_ss,X_sθ,X_θθ,R` 重放差均为 0。

零控制在数学定义上准确给原 `a_seed`，网格上也逐位相同；不过新 family 字典本身与旧 frozen-g 字典不同。报告明确区分“同一个半径函数的零控制表示”和“同一个完整身份字典”，不会伪造字典相等。

## 3. 自然单帽标量源

准确尾帽保持 [R44](../results/R44-S9-six-cap-exact-embedding-and-normal-chord.md) 的物理定义：

\[
R=137/500,\quad d=R\sqrt3/2,\quad w=R-d,
\]

法向为 `jπ/3`，六个角幅为

\[
(3/16,1/8,1/8,3/16,1/8,1/8).
\]

每帽的弯角仍为全局夹断的 S9：负输入为 0，单位输入以上为所选角幅。没有将 S9 多项式继续外推到大参数。

对任意非负源半径 `r`，令

\[
a_j=e_r\cdot n_j,\quad b_j=e_\theta\cdot n_j,
\quad u_j^{\rm exc}=r a_j-d,\quad
\alpha_j=A_j S_9(u_j^{\rm exc}/w).
\]

单帽的三个周期标量增量为

\[
U_j=\arctan\frac{(1-\cos\alpha_j)a_jb_j}
 {1-(1-\cos\alpha_j)b_j^2},
\]

\[
V_j=-\varsigma\frac{b_j\sin\alpha_j}
 {\sqrt{1-b_j^2\sin^2\alpha_j}},\qquad
B_j=\varsigma\arctan(a_j\tan\alpha_j).
\]

这里 `varsigma=side`，大写 `V_j` 是标量增量，不能与空间中的目标单位向量 V 混淆。

取 `G(r,θ)=Σ_j(U_j,V_j,B_j)`，再在 β 分量加固定 lift `−side·π`。

在 `r≤R` 时各外弓形不重叠，所以它准确等于原帽的标量 frame。`r>R` 时各单帽可能重叠，**仅把这些增量的和当作目标正交 frame 的标量初场**；不把六个位置映射相加后声称等距。

各分母都有由 `|α|≤3/16` 给出的正下界。源标量全局 C4；其每一光滑分支更光滑。由标量构造的目标 T,V 始终正交单位，但这不证明实际重构的 `X_s=V`。

## 4. 端点全平的无限 Gaussian 定义

设 `δ=t_f−t`，`τ_0=1/128`，准确物理标准差为

\[
\sigma(\delta)=
\begin{cases}
\frac18\exp(1-h^2/\delta^2),&\delta>0,\\
0,&\delta=0.
\end{cases}
\]

定义

\[
\mathcal H(t,\theta)=\mathbb E_{Z\sim N(0,1)}
 G(a_{\rm seed}(t),\theta+\sigma(t)Z).
\]

这是无限 Gaussian 积分，即周期热半群；GH32、GH64 等只是同一数学函数的评价器。它们的阶数不进入物理、模型、空间或准确系数身份。

对 `δ>0`，σ 的 t 导数为

\[
\sigma_t=-\frac{2h^2}{\delta^3}\sigma,\qquad
\sigma_{tt}=\left(\frac{4h^4}{\delta^6}
 -\frac{6h^2}{\delta^4}\right)\sigma.
\]

实现直接在 Jet22 中组合 `r=a_seed(t)` 与 `θ+σZ`。这样得到完整 `t²θ²` jets，不用对移动数值节点另作差分。σ 很小时用对数公式评价；浮点指数下溢只记为评价现象，准确身份没有人为截断阈值。

σ 及其每阶 t 导数在 `δ=0` 为零，源已有统一 C4 jets，所以本轮所需 value/s/ss/theta/st/ss_theta 均连续回到准确帽端口。`δ=0` 在代码中直接调用零热的准确组合，不依靠有限 GH 权重求和来制造端点。

“保持所有自然径向 jets”只指**固定非退化单帽开角**：`0<u_j^exc<w`、`b_j≠0`，避开顶点及帽中心。在这些点，δ 足够小时只有同一个光滑单帽分支；全平 σ 不改变任何有限径向 jet。顶点及中心的全角高阶 jets 不在此论断内，不能因为 S9 已夹断而声称它们全阶解析。位置 C2 的拼接有独立的低阶连续性保证。

## 5. 只改固定基场，保持原自由列

令原 enriched 的 234 维系数为 `c0`；无论审计 `c0` 还是已公开饱和模型的 `c1`，基场锚点均固定为原 `c0`。

设 χ 在 `δ≤h/3` 为 1，在后面 `2h/3` 区间按 `1−S9` 退到 0。新标量场定义为

\[
f_{\rm new}(c)=f_{\rm old}(c)+
 \chi\,[f_{\rm natural\,heat}-f_{\rm old}(c_0)].
\]

注意自由列 `f_old(c)−f_old(c0)` 不乘 χ。补丁以外原 enriched 空间完整保留。χ 在支撑左端的前四阶导数均为零；准确开尾单独采用原 R44 帽，匹配完整位置二jet所需的标量与混合 jets。

全部自然源半径取 `a_seed`。主体度量控制在整补丁为零，因此不存在误把新主体参数外推到 tail source 后又漏算参数导数的问题。

角向的二重旋转与反射保持：水平 mean(T)=0 由半周符号反转，垂直 mean(T)=0 由反射奇性。不能把整个空间 T 都说成半周反号。相应重构仍是

\[
X=z_c e_z+a\Pi T,\qquad
z_c'=\langle V_z\rangle,\quad z_c(0)=\text{原核心高度}.
\]

帽高使用同一个 `h_cap=side·z_c(L)`，没有逐圈重新平移。

## 6. 直接实际度量目标及 Jacobian

数学上 `X_θ=aT`，`|T|=1`，故 G 准确等于 `a²`。实际等距只需要

\[
E=|X_s|^2=1,\qquad F/a=X_s\cdot T=0.
\]

本次独立输出直接残差

\[
r_g=(E-1,\sqrt2\,F/a),
\]

和相对于目标正交单位基的准确二维 operator 误差公式

\[
\|g^{-1/2}(g_X-g)g^{-1/2}\|_{op}
=\frac{|E-1|+\sqrt{(E-1)^2+4(F/a)^2}}2.
\]

原 R 方程确保 `X_s=V`，是充分条件。直接度量方程没有要求单位向量 `X_s` 恰落入原有限 β 空间。不过当前参数化仍通过 `mean(V_z)` 控制中心高度；本次没有另外增加独立高度导数基。

固定 g 的场参数变化满足

\[
dX_s=a'\Pi(dT)+a\Pi(dT_s)+\langle dV_z\rangle e_z.
\]

主体度量参数对 T,V 和中心高度没有直接导数，另加

\[
dX_s=(da')\Pi T+(da)\Pi T_s.
\]

因此

\[
dE=2X_s\cdot dX_s,\qquad
d(F/a)=dX_s\cdot T+X_s\cdot dT.
\]

代码同时保留与原 R 目标完全相同的 ball/strip 三项软形状约束和权重。两种成本分别记录，不混为一次优化下降。

初态审计会做两类**只读线性方向**：

- 固定所有场参数，只给主体 metric 列；
- 给当前完整 `u,v,β` 与主体 metric 列。

它们只求线性最小二乘预测并保存梯度、秩、奇异值和未应用步长。没有把该步长施加到非线性模型，也没有因此宣称找到新 g 或可行曲面。

## 7. 人工开发检查

所有本地检验使用人工椭圆 `(A,B)=(.9,.72)`、不同长度与较小自由空间；没有评价原真实核心或 `c0/c1`。

对应输出为：

- `notes/frame-body-metric-design-check-20261114.json`；
- `notes/polygonal-tail-natural-extension-check-20261114.json`；
- `notes/frame-collar-natural-body-audit-check-20261114.json`。

已见的主要误差：

| 检验 | 正侧 | 负侧 |
|---|---:|---:|
| R/形状全参数 Jacobian 相对差 | `3.00e-9` | `4.20e-9` |
| 直接实际 metric/形状全参数 Jacobian 相对差 | `6.86e-9` | `8.54e-9` |
| 直接 metric 的主体列相对差 | `4.80e-9` | `4.16e-9` |
| metric 设计后冻结的全部位置二jet及 R 回放差 | 0 | 0 |

另检查了自然源的 Jet22 链式、两侧符号、准确端口、二重/反射对称、GH 加密身份不变、零控制回放种子、补丁所有 metric Jacobian 为零。核心位置 Π 在 24/48/96 角上另存误差，不通过放宽阈值隐去截断。

`passed` 只说明这些开发检查通过，不是 GH 连续误差界、实际等距、嵌入、reach 或任务完成证明。

## 8. 公开 Actions 初态审计命令

真实入口必须同时满足 `GITHUB_ACTIONS=true` 与 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。输入仅允许本公开课题 notes。以下只审计两个已保存系数，没有求解器预算参数：

```bash
python topics/visible-flex-new-mechanism/scripts/frame_collar_natural_body_audit.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43604231319-1-ellipse_enriched/frame-ellipse-enriched-fixed.json \
  --compare-saturated-input topics/visible-flex-new-mechanism/notes/actions-43612971265-1-ellipse_saturated_heat/frame-ellipse-six-cap-saturated-heat-fixed.json.gz \
  --metric-free 5 --support-width 1/10 --plateau-fraction 1/3 --tau0 1/128 \
  --heat-order 32 --radial-nodes 61 --angular-nodes 192 --quadrature-order 4 \
  --audit-radial-nodes 121 --audit-angular-nodes 384 \
  --out "$RUNNER_TEMP/frame-natural-body-initial-audit.json"
```

每个 case 的主体 metric 初值全为零，锚点均是原 `c0`；第二 case 仅换成已公开 `c1` 的 234 个准确系数。loader 核旧来源集、每个实现 SHA、模型/空间/物理身份、准确 binary64 有理数、完整 seed-g 与 anchor。当前源码若与记录不相同直接拒绝回放，不用新实现悄悄替换旧模型。

主网格保持已有准确身份的 61 个非均匀径向层和 192 角。每个 case 先保存初态、同网格未动前缀和原 R 线性主体方向，再保存直接实际 metric 诊断；之后才作同系数 GH 加密、121×384/768 空间审计。文件原子写入，第二 case 不覆盖第一 case。

GH 与 Π 误差继续分账。角加倍、GH 加倍和线性方向均不修改系数。完整模型与身份不含 GH 档；每次变更评价档都断言 model/space/anchor/heat/g/准确系数逐项一致。

内存主项仍是解析 Jacobian：`61×192×239` 个标量约 22 MB，三坐标块约 67 MB；帧偏导、径向中心求积和线性代数临时空间会再增加。GH 使用既有逐径向小块及八节点累计，避免同时展开全部 GH 维。这里只给数组规模，真实 peak RSS 和耗时由 Actions 输出，不在本地评价实际候选估时。

## 9. 未付条件

自然标量延拓加全平热，只移除某些已识别的反射 Cauchy 缺项；没有证明与主体可接。主体设计改变 g，最终须冻结完整准确定义后再做同 g 精化。直接实际 metric 目标也只在准确零时给等距；网格残差和线性预测都不足以给极限、单射或 reach。

全曲面的握持、位移、尺寸、接缝和近远法弦证书仍须在实际可行候选上完成。没有把 R44 的准确局部帽证书移用成完整闭面的证书。
