# R95：原 seg7 全连续候选的曲率余量与明确五导数误差门

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted）
日期：2026-11-12

## 1. 已完成结论及其量词

固定 R26 同一个真实背景 $g=E\,dr^2+r^2d\theta^2$、$E=1+w^2$，
取已经发布的 cell 0 / seg7 八段 R48 候选高度 $\widehat h$，
包括其完整 mean 根和一个贯穿全段的 mean 高度常数。
对应原审计完整覆盖 **8 个 substage、1,740 个连续叶和全部 20 个非均值模式**。

对这个实际候选，形式矩阵
$\operatorname{Hess}_g\widehat h/\sqrt{1-|\nabla_g\widehat h|^2}$
的全段全角算子范数已经由本记录的精确有理消费证明

$$
 \widehat K_{\rm formal}<8.161217922208365.
 \tag{95.1}
$$

这不称为一个尚未实现的等距曲面的实际主曲率。

**条件定理。**
设 $F$ 是相同真实 $g$ 上的实际 $C^2$ 等距浸入，
高度为 $h$。若在同一整个 seg7、全部真实角上，五个实际物理极坐标导数满足

$$
 \max\bigl(
 |h_r-\widehat h_r|,
 |h_\theta-\widehat h_\theta|,
 |h_{rr}-\widehat h_{rr}|,
 |h_{r\theta}-\widehat h_{r\theta}|,
 |h_{\theta\theta}-\widehat h_{\theta\theta}|
 \bigr)\le \frac1{8192},
 \tag{95.2}
$$

则该段的所有实际主曲率满足

$$
 \boxed{\max|\kappa_i|
 <8.233700409770135<\frac{33}{4}.}
 \tag{95.3}
$$

到 $33/4$ 的余量严格大于 $0.016299590229865437$。
(95.2) 中 $r$ 是真实物理半径、$\theta$ 是源角弧度；五种导数各自支付，
不把该数解释成未经换元的 Cartesian Hessian 范数。
完整高度值及其竖直常数不影响本曲率结论，但位置、held 与 reach 接口仍须
保留它们。本记录**没有**证明所述浸入存在，也没有证明 (95.2) 已满足。
它不把当前候选的非零 Darboux 残差删除。

## 2. 已付输入与同背景身份

本次直接消费以下原已发布文本的精确内容：

| 输入 | SHA256 |
|---|---|
| 原 seg7 完整审计 | 806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4 |
| 原正式 resource | 912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820 |
| R31 真背景账本 | 27e9cac085dd4913cdf14526fec847613bede8fae5367ae72cc143f25b254083 |

原审计为
[seg7-span2-centeredJ-r2.json](../notes/2026-11-12-tail-outer-cell0-seg7-span2-centeredJ-r2.json)，
其 wait4 resource 的 child exitcode 为 0、termination_signal 为 null。
全部原连续 mean、真实导数、完整有限 J、同候选和同背景门均为 true。
这次未重新计算它的 1,740 个叶，也不依赖尚未恢复的 seg7 R77 小重权结果。

[R31](R31-complete-height-curvature-transfer.md) 第 4.2 节和相同真背景账本已付

$$
 K_{\rm bg}\le8,\qquad
 0<w<\frac3{25},\qquad r>\frac1{20}
 \quad\hbox{在整个 cell 0 / seg7}.
 \tag{95.4}
$$

其中 $w$ 的原实际全段上界为
$0.103740139967422856$ 的严格以下值；这里故意采用较宽但准确的 $3/25$。
真实 node12 半径严格大于 $0.05002$，故 $r>1/20$ 不使用略小于 $0.05$
的 binary cuff 半径。背景账本与原候选的完整 ready SHA 精确一致。

源语义也已核对：
tail_outer_substage_span_refinement.py 的 SHA 为
85bf30e818e7ab92107a5f5a537225afb9273877327bf6e0092b303b01a1b5d8；
tail_outer_general_mean_bounds.py 的 SHA 为
4b16b860eb89d7b8f19d7f8ff05642ea0122b0a2016d4be623d5483430023a5c。
前者先构造同模式的实际 $H_{rr}$ 再取完整 cosine $\ell^1$，
后者保存完整 mean 的实际二阶差。没有用 PDE 二阶值替换候选自身导数。

## 3. 将原完整范数转为真实极坐标输入

写原候选

$$
 \widehat h_r=w(1+c+\overline K),\qquad
 P=\frac{\widehat h_\theta}{rw},\qquad T=P_\theta,\qquad
 U=\overline K_\theta-P .
$$

对每个完整 substage，原审计给出非负上界：

- $c_*$：完整 $|c|$；
- $R_*=\|P\|_{\tau,1}+\|\overline K\|_{\tau,1}$；
- $T_*=\|T\|_{\tau,1}$、$U_*=\|U\|_{\tau,1}$；
- $H_*=\|\widehat h^\perp_{rr}\|_{\ell^1}$，先同模组合的实际物理导数；
- $M_*=|\widehat h^0_{rr}-w_r|$，完整 mean 二阶差。

这里原权为 $(1+m)e^{\tau m}$，$\tau\ge0$，最小非零模式为 $m=2$。
$P,\overline K,T,U$ 都零均值，因此准确有

$$
 \|P\|_\infty,\ \|\overline K\|_\infty\le R_*/3,\qquad
 \|T\|_\infty\le T_*/3,\qquad
 \|U\|_\infty\le U_*/3.
 \tag{95.5}
$$

这只使用完整 Fourier 质量；没有交换点态角和与逐模径向 supremum。
原 $H_*,M_*$ 已覆盖整个 substage，不额外除以 3。

置固定的有理常数

$$
 w_*=\frac3{25},\quad r_*=\frac1{20},\quad
 E_*=1+w_*^2,\quad e_*=1+\frac{w_*^2}{2},\quad
 C_g=8w_*e_*.
 \tag{95.6}
$$

由 $|w_r|/E^{3/2}\le8$ 得
$|E'/(2E)|=|ww_r/E|\le C_g$，且 $\sqrt E\le e_*$。

对 [R31](R31-complete-height-curvature-transfer.md) 的梯度偏差和三个
Hessian 组合量，可取

$$
\begin{aligned}
 d_0&=w_*(c_*+R_*/3),&
 e_0&=w_*R_*/3,\\
 A_0&=H_*+M_*+C_gd_0,&
 B_0&=\frac{w_*}{r_*}\frac{U_*}{3},\\
 C_0&=\frac{w_*}{r_*}(c_*+R_*/3+T_*/3).
\end{aligned}
\tag{95.7}
$$

证明：$d_0$ 控制 $|\widehat h_r-w|$，$e_0$ 控制
$|\widehat h_\theta/r|$；
$A_0$ 控制
$|\widehat h_{rr}-w_r-(E'/2E)(\widehat h_r-w)|/E$；
$B_0$ 使用准确组合
$\widehat h_{r\theta}-\widehat h_\theta/r=wU$。
最后

$$
 \frac{\widehat h_{\theta\theta}}{r^2}
  +\frac{\widehat h_r-w}{rE}
 =\frac{w}{r}\left(T+\frac{c+\overline K}{E}\right),
$$

给 $C_0$。所有除 $E$、$\sqrt E$ 的项用 $E\ge1$ 作保守包围。
各项仍指同一个完整高度；完整 mean 没有遗漏。

## 4. 任意真实两 jet 误差的非均匀门

更一般地，设五个误差分别不超过
$\eta_r,\eta_\theta,\eta_{rr},\eta_{r\theta},\eta_{\theta\theta}$。
不要求它们相等。可用

$$
\begin{aligned}
 d&=d_0+\eta_r,& e&=e_0+\eta_\theta/r_*,\\
 A&=A_0+\eta_{rr}+C_g\eta_r,\\
 B&=B_0+\eta_{r\theta}/r_*+\eta_\theta/r_*^2,\\
 C&=C_0+\eta_{\theta\theta}/r_*^2+\eta_r/r_*.
\end{aligned}
\tag{95.8}
$$

于是

$$
 \epsilon=2w_*d+d^2+E_*e^2,\qquad
 \Lambda=\max(A,C)+B.
$$

若 $\epsilon<1$，R31 的完整矩阵证明及
$\sqrt{1-\epsilon}\ge1-\epsilon$ 给

$$
 \nu^2\ge\frac{1-\epsilon}{E_*}>0,\qquad
 \boxed{K\le\frac{8+e_*\Lambda}{1-\epsilon}.}
 \tag{95.9}
$$

这证明 (95.1) 时取所有 $\eta=0$，证明 (95.3) 时取所有
$\eta=1/8192$。每个操作都是正有理算术；最终比较不使用浮点数。

## 5. 全部八段的实际精确结果

下表每个显示值均由精确分数**向上**舍入至小数点后 18 位。
它们是整个相应连续 substage 的上界：

| substage | 原连续叶数 | 候选形式矩阵上界 | 条件真解曲率上界，五误差各 $\le1/8192$ |
|---:|---:|---:|---:|
| 0 | 37 | 8.161217922208364475 | 8.233700409770134563 |
| 1 | 53 | 8.121423556926447505 | 8.225139796769198909 |
| 2 | 125 | 8.084796565777580413 | 8.188466414167282587 |
| 3 | 208 | 8.048541162490569058 | 8.152165447547168454 |
| 4 | 304 | 8.030985719656522817 | 8.134588143599069092 |
| 5 | 257 | 8.029879771540119777 | 8.133480876332117983 |
| 6 | 256 | 8.033730731075303156 | 8.137336735484873459 |
| 7 | 500 | 8.034542117989999673 | 8.138149211970952261 |

全部八段两个门均通过；最坏为 substage 0，覆盖其原 37 个连续叶。
这没有在候选之间取逐点最小值，也没有只挑选原点样本。
总连续覆盖仍为原来的 1,740 叶。

实际计算为
[tail_r95_seg7_curvature_budget.js](../computations/tail_r95_seg7_curvature_budget.js)
的纯 JavaScript BigInt 消费，已在 functions.exec V8 中执行完成。
该源内置 SHA-256 并直接对三个原 JSON 文本校验，再解析完整输入；
所有判定使用整数交叉乘法。小数只作为有方向的显示。
没有 Node 进程、Arb、新积分、ODE 或 BVP，也没有 OS 子进程退出码或
RSS 测量可冒称。原输入自己的正式 exit 0 单独核销并保留。

完整精确分数、各 part 的 $d,e,A,B,C,\epsilon,\nu^2$ 与九个通过门在
[实际账本](../notes/2026-11-12-tail-r95-seg7-curvature-budget.json)。

## 6. 与现有全量差界的准确连接

若未来外侧误差以归一场给出，必须用同一个真实背景转换：

$$
\begin{aligned}
 \delta h_r&=w(\delta c+\delta\overline K),&
 \delta h_\theta&=rw\,\delta P,\\
 \delta h_{r\theta}&=w\,\delta\overline K_\theta,&
 \delta h_{\theta\theta}&=rw\,\delta P_\theta,\\
 \delta h_{rr}&=w_r(\delta c+\delta\overline K)
                  +w(\delta c_r+\delta\overline K_r).
\end{aligned}
\tag{95.10}
$$

source-$x$ 的 $\delta\overline K_x$、$\delta c_x$ 还须除以相同严格正的
$r_x$；不能把其数值直接当物理径向导数误差。
对于完整 mean，已付
[同根差](../notes/2026-11-12-tail-two-complete-mean-roots-rational-difference.md)、
[同根径向差](../notes/2026-11-12-tail-two-complete-mean-radial-difference.md)
可接实际同位置全场输入。
只有一阶强范数时，$\delta\overline K_r$ 仍未自动支付；
必须由实际候选导数和真方程的差或另外完整径向估计得到，保留候选残差项。

PA/CF v3 mean 账本给的是两个新候选之间的实际五导数差。
R95 的参考却是原 source-$x$ R48 候选；因此还需付原候选到 PA 的同位置
完整差，再与 PA→CF、CF→真解逐项相加，或直接对最终参考重付 (95.7)。
不得把 PA/CF 之间的小差直接当作原候选到真解的误差。
端点两 jet 相同不补足内部全连续差；mean 高度常数及水平框架偏移仍由
各自账本继续，不由本曲率定理归零。

本结果是同真实背景、明确 reference、明确导数单位的曲率预算。
它没有支付外 $0..9$ 真解、真实内外 DN 接合、中窗全频解、完整时间域、
全空间点对、reach 或 held 位移下界。
