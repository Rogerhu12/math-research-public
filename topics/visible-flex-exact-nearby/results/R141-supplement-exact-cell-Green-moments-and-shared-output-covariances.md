# R141 补篇：同格 Green 两三角的准确矩积分与输出协方差复用

2026-11-20，visible-exact-astra-ac637-20261120 / joint_kernel。

**状态：已证明（积分恒等式、逐点协方差比较及纯算法）；未执行新的科学目标。**

本篇只研究 R141 已定义的同一个 193 维 comparison BVP。当前
44730452579/1 的脚本、参数、manifest 和运行均不改变。本篇没有产生新的
defect 或 inverse 数值，也不允许重算任何已经成功保存的目标。

这里 low centre 仍是 R141 的 WVC hybrid：实际共同的 $\eta_\delta$
主部与修补中心的低阶系数。它没有变成整个真实 $DF(Q_{\rm repair})$。
见原 R141 的 G.1--G.25、exact-refinement 补篇以及 shared-scalar 补篇。
下面的全部积分都是 ordinary $dr$，root97 和 outer96 独立 atoms 均保留。

## 1. 一格上的准确核

在一个 comparison cell 上写 $r=r_i+h_i t$，$0\le t\le1$，
$h_i$ 是原同一真正长度。其已定义的常系数 comparison 方程为
$x_t=Hx$。若该格来自原 parent 的 $n$ 等分，则准确
$H=H_{\rm parent}/n$、$h_i=h_{\rm parent}/n$；不改变比较方程。

本节暂省格号。令
$$
 E(t)=e^{tH},\quad Q=S^TS,\quad
 F=[L,R],\quad F^{-1}=\binom{\ell}{\rho},\quad P=L\ell.
 \tag{GM.1}
$$
各尺寸是 $L:193\times97$、$R:193\times96$，
$\ell:97\times193$、$\rho:96\times193$。于是
$P^2=P$、$R\rho=I-P$；不假设 $P$ 正交或与 $H$ 交换。
这些恒等式属于同一个准确节点 frame，计算时只需矩阵球包含它。

对恒定源矩阵 $W$，完整同格 Green 核为
$$
 {\cal K}(t,s)
   =S E(t)\bigl({\bf1}_{t>s}I-P\bigr)E(-s)W .
 \tag{GM.2}
$$
$t<s$ 是原 $-L(t)\ell(s)$，$t>s$ 是原 $R(t)\rho(s)$。
对角集合测度为零。式 (GM.2) 合并的是这两个三角，未删除其中一个。
它保完整 193 维 identity jump，特别保独立 even mean。

## 2. 三个矩与两三角之和

令 $V=WW^T$，并定义
$$
 \begin{split}
 U&=\int_0^1E(t)^TQE(t)\,dt,\\
 Z&=\int_0^1E(-s)VE(-s)^T\,ds,\\
 Y&=\int_{0<s<t<1}
      E(t)^TQ E(t-s)V E(-s)^T\,ds\,dt .
 \end{split}
 \tag{GM.3}
$$
$U,Z$ 是 PSD；$Y$ 一般不对称，不可把它当 PSD。
四个旧 Gram 积分准确为
$$
 Q_L=hL^TUL,\quad Q_R=hR^TUR,\qquad
 P_L=h\ell Z\ell^T,\quad P_R=h\rho Z\rho^T .
 \tag{GM.4}
$$
两三角的总 Hilbert--Schmidt 平方准确是
$$
 \boxed{\quad
 T_L+T_R
 =h^2\{\operatorname{tr}(P^TUPZ)
          +\operatorname{tr}Y-2\operatorname{tr}(P^TY)\}.
 \quad}
 \tag{GM.5}
$$

证明：把 (GM.2) 写成 causal 核 $C$ 减去矩形核 $F_0$。
整个单位方形上
$$
 \|F_0\|_{\rm HS}^2=\operatorname{tr}(P^TUPZ).
$$
causal 部分的平方为 $\operatorname{tr}Y$：循环迹后
$E(-s)^TE(t)^T=E(t-s)^T$。两者的三角交叉内积是
$\operatorname{tr}(P^TY)$。展开 $\|C-F_0\|^2$ 即得。
不在展开前分别取绝对值；该有符号抵消是本恒等式的用途。

无需形成完整 $P$ 来计算最后一式：
$$
 \operatorname{tr}(P^TUPZ)
   =\operatorname{tr}\bigl((L^TUL)(\ell Z\ell^T)\bigr),
 \qquad
 \operatorname{tr}(P^TY)=\langle L,Y\ell^T\rangle_F .
 \tag{GM.6}
$$
右边只用已需的 97 维 Grams 及一次 $193\times193$ 乘 $193\times97$。

## 3. 一个有限维传播给出全部矩

考虑上三角 block 生成元
$$
 {\cal A}=
 \begin{pmatrix}
 -H^T&Q&0\\
 0&H&V\\
 0&0&-H^T
 \end{pmatrix}.
 \tag{GM.7}
$$
若 $X_{12},X_{23},X_{13}$ 为 $e^{\cal A}$ 的相应 blocks，则
$$
 \boxed{
 U=E(1)^TX_{12},\qquad
 Z=E(-1)X_{23},\qquad
 Y=E(1)^TX_{13}.
 }
 \tag{GM.8}
$$
这是 block variation-of-constants 的直接迭代。具体地，
$X_{13}$ 的积分是
$$
 \int_{0<s<t<1}
 e^{-(1-t)H^T}Qe^{(t-s)H}Ve^{-sH^T}\,ds\,dt;
$$
左乘 $E(1)^T$ 即 (GM.3)。$X_{12},X_{23}$ 的一次积分同理。
所有公式也适用于有零特征值或谱共振的 $H$。
尤其不能另假设 $H\otimes I+I\otimes H$ 可逆来解 Sylvester 方程。
本式不需要大小 $193^2=37249$ 的 Kronecker 矩阵。

### 3.1 五个 193 方阵的定向实现

无需直接求一个 579 方阵的 dense exponential。取准确正 dyadic
$a_Q\ge\max(1,\|Q\|_\infty)$、$a_V\ge\max(1,\|V\|_\infty)$，
将 (GM.7) 的邻 blocks 改成 $Q/a_Q,V/a_V$。
所得三个指数 blocks 分别乘回 $a_Q,a_V,a_Qa_V$。

选 $\delta=2^{-d}$，使
$$
 \lambda=\delta\{1+\max(\|H\|_\infty,\|H^T\|_\infty)\}\le\tfrac12 .
 \tag{GM.9}
$$
范数使用完整 directed upper，不能只读当前 refinement 的单侧行界。
用 degree $m$ 的 Taylor 多项式计算短程指数的五个非零独立 blocks。
若 $A=-\delta H^T$、$B=\delta H$、$C=\delta Q/a_Q$、
$D=\delta V/a_V$，系数递推为
$$
 \begin{split}
 B_k&=BB_{k-1}/k,\qquad A_k=(-1)^kB_k^T,\\
 X_k&=(AX_{k-1}+CB_{k-1})/k,\\
 Z_k&=(BZ_{k-1}+DA_{k-1})/k,\\
 Y_k&=(AY_{k-1}+CZ_{k-1})/k .
 \end{split}
 \tag{GM.10}
$$
初值 $A_0=B_0=I$，其余三者为零；每轮右边均用旧系数。
每个最终 entry 的遗漏项可包在 $[-\varepsilon,\varepsilon]$，其中
$$
 \varepsilon=
 {\,\lambda^{m+1}\over(m+1)!}
 {1\over1-\lambda/(m+2)} .
 \tag{GM.11}
$$
这是整个上三角 block 矩阵无穷范数的正级数尾。所有分母取正 lower，
所有上界向外；不要求正部和 signed 尾相减得到一个脆弱的小量。
下三角零 blocks 是结构恒等，保持零。

随后逐次平方五个 blocks：
$$
 \begin{split}
 A^+&=A^2,\quad B^+=B^2,\\
 X^+&=AX+XB,\\
 Z^+&=BZ+ZA,\\
 Y^+&=AY+XZ+YA .
 \end{split}
 \tag{GM.12}
$$
这里 $A,B$ 已表示短程指数的两个对角 blocks，不是 (GM.10) 的短生成元。
每次先算全部右边再替换。$d$ 次后得到 (GM.8)，且不用求数值逆
$E(1)^{-1}$：$E(-1)=A^T$ 已一并得到。

$H,Q$ 不依赖源 role，因此所有 $B_k$、$A_k$、$X$ 以及每层 doubling
的 $A,B,X$ 可在一个 parent 模板中复用。每个新 $V$ 只算 $Z,Y$。
这一复用是准确同矩阵运算，不改变数据或数学目标。

### 3.2 原 dyadic balance 与真正 $S$

实际计算宜用现有 exact dyadic 内部 balance $B_0$，置
$$
 \widetilde H=B_0HB_0^{-1},\quad
 \widetilde Q=B_0^{-T}S^TSB_0^{-1},\quad
 \widetilde V=B_0VB_0^T.
 \tag{GM.13}
$$
同时 $\widetilde L=B_0L$、$\widetilde\ell=\ell B_0^{-1}$，$R,\rho$ 同理。
式 (GM.4--8) 用这些量完全不变。$B_0$ 只作 similarity；
原真实 $S$、$q_i$、true $h_i$ 没有被 binary64 balance 替换。
原均值权重和全部非均值权重均在 $\widetilde Q$ 中。

## 4. 随径向变化的源：必须逐点比较

ordinary $W=I$ 和 transformed $W=S^{-1}$ 在一格中为恒定源，
可以直接用 (GM.3--8)，对所有原参数球统一包住。
对 defect、second-kind correction 或高返回列，$W(s)$ 通常随 $s$ 变化。
一个整格 entrywise 矩阵球并不表示同一个恒定未知 $W$：
**不能将它直接代入 (GM.8) 后宣称已积分所有 $W(s)$。**

合法方法是证明一个恒定 PSD 矩阵 $\bar V$ 满足
$$
 W(s)W(s)^T\preceq\bar V\qquad\hbox{对格内每个 }s .
 \tag{GM.14}
$$
对每个固定输出点，完整核平方是源协方差的正线性函数，
故 (GM.4) 的源 Grams、(GM.5) 的两三角之和，以及所有全域 body/atom
平方，均被将 $V$ 换成 $\bar V$ 的相应完整量支配。
该证明在合并两三角之后仍成立，因为先比较的是原核的平方，
不是把 (GM.5) 的三个有符号项分别作 Loewner 比较。

一个不需额外参数的可执行构造如下。取准确矩阵 $W_0$，
并由 whole-cell source ball 得到逐点 $|W(s)-W_0|\le R$，
$R$ entrywise 非负。令
$$
 C=|W_0|R^T+R|W_0|^T+RR^T,\qquad
 D=\operatorname{diag}(C{\bf1}),\qquad
 \bar V=W_0W_0^T+D .
 \tag{GM.15}
$$
$C$ 对称非负，且 covariance difference 的 entry 绝对值被 $C$ 支配。
对实向量 $z$，用 $2|z_i z_j|\le z_i^2+z_j^2$ 得
$z^T(W(s)W(s)^T-W_0W_0^T)z\le z^TDz$，证明 (GM.14)。
计算中 $D$ 各对角取行和 upper；$W_0W_0^T$ 仍是准确 PSD 对象的球。
这不假设不同原参数、角系数或 radial points 独立，也未改变 family 域。

也可把 source 切成 $W_0+E(s)$ 并分别控制两个完整 HS norm 再用三角；
其必要费用不能免费省略。本篇核心采用 (GM.15)，未声称它对所有
defect 都比旧 whole-box 公式更小。

如同一 parent 的所有 refined cells 使用同一 $H_{\rm parent}/n$、$S$
和同一个已证明的 parent covariance upper，则三个矩在这些 cells 完全相同，
只需做一次。节点 $L,R,\ell,\rho$ 仍逐 cell 使用各自的准确 frame，
从而没有恢复旧长 parent carrier 的病态。若仅有 child-specific source
upper，必须分别计算相应矩，不能从 parent 相同偷换出源协方差相同。

## 5. 全域递推和全部 193 atoms

将 (GM.4) 送回原 R141 的准确离格递推即可：
$$
 \begin{split}
 A_0&=0,& A_{i+1}&=C_i^T(A_i+Q_{L,i})C_i,\\
 B_m&=0,& B_i&=Q_{R,i}+D_i^TB_{i+1}D_i,\\
 J_0&=A_{\rm root}^TA_{\rm root},&
 J_{i+1}&=C_i^TJ_iC_i,\\
 K_m&=A_{\rm out}^TA_{\rm out},&
 K_i&=D_i^TK_{i+1}D_i .
 \end{split}
 \tag{GM.16}
$$
$C_i,D_i$ 是原 chart 两向传播逆，不是新 coefficient。
完整 body 和 atoms 平方为
$$
 \begin{split}
 {\cal B}^2={}&\sum_i\operatorname{tr}(A_iP_{L,i})
 +\sum_i\operatorname{tr}(D_i^TB_{i+1}D_iP_{R,i})
 +\sum_i(T_{L,i}+T_{R,i}),\\
 {\cal A}_{97}^2={}&\sum_i\operatorname{tr}(J_iP_{L,i}),\\
 {\cal A}_{96}^2={}&\sum_i\operatorname{tr}(K_iP_{R,i}).
 \end{split}
 \tag{GM.17}
$$
true $h_i$ 已在 (GM.4--5) 内，不能再乘或漏乘。
root97 包含 mean，outer96 带原 $\Theta$，两者都没有投影掉。
普通 source domain 仍是完整真实径向区间。

值得单独指出：$A_i,B_i,J_i,K_i$ 以及
$D_i^TB_{i+1}D_i$ **全部只依赖 model、$S$ 和原 atoms，不依赖 source role**。
因此可以共享同一完整球。当前实现对每个 role 重做 (GM.16)；
准确复用这些矩阵能严格减少矩阵运算，不因复用本身扩大任何球。
配套核心采用不新增 packing 舍入的版本：$A,B,K$ 按原规则只准备并保存一次；
$J$ 与 $D_i^TB_{i+1}D_i$ 保原高精度动态矩阵，每批完整角色只流过一次。
先 defect 门、成功后四源的现有次序因此只需两次 $J$/right 流，
原来为五次；$A,B,K$ 从五次降至一次。
逐 role 的 $P_L,P_R$ 与同格两三角仍各自支付。

这些完整 $P_L,P_R$ 也可送入原 defect point-source covariance 递推。
若使用 (GM.14)，其 PSD 上界性质保证原 full-cell 支配 partial-cell
的 whole-point projection 证明照用。该点观察仍需要原定向 whole-box
local factors，不能从本篇的积分矩宣称任意点都已证 transversality。
Neumann body 缺陷门、atoms 的 direct identity、second-kind 公式、
两条原 RHS 和所有后继高反馈门均保持原 R141 资格，不因本篇自动成立。

## 6. 实作、成本与后继范围

配套纯核心不导入数值库、不读文件、不在 import 时计算。它提供
有向短程 block Taylor/doubling、(GM.15) covariance upper、平衡下的
cell packet，以及一次性共享输出协方差和完整 body/root97/outer96
汇总。所有数值必须由另行公开 Actions owner 驱动。

原实现每 refined cell 有 4 integration boxes，短程 Taylor degree16。
本篇没有把它误报成旧计划的 degree128。它还保留全部 refined 节点，
故未回到已知有严重基条件损失的 155 个长 cell carrier。

对 (GM.10)，共享 $H,Q$ 部分每阶至多 3 次 $193$ 方阵乘法；
每个 source covariance 部分至多 4 次。若 $Q$ 为 diagonal，
相应左乘可精确用逐行缩放。每层 doubling 的共享部分是 4 次乘法，
每个 source 部分是 5 次。所有 dense 运算最大为 $193$ 方阵；
不创建 $579$ dense matrix，更不创建 $37249$ Kronecker matrix。
模板只留当前 parent，额外内存为 $O((m+d)193^2)$。
全域 $A,B,K$ 沿用原每 entry 明确包含的 binary64 mid/rad 储存。
root $J$ 不为复用而新增 binary64 packing；它按上述两批流保持旧式精度。

本方法准确消除恒定 covariance 的时间 quadrature/range overestimate。
但 directed rounding、原 node frame 宽度、source PSD majorant 和最终
HS-to-operator 比较仍在。因此不能在执行前宣称新数值必小于旧上界，
也不能保证 3-block 法在每种 parent/source 配置下一定更快。
确定的运算节省是 (GM.16) 的五角色共享及两批流；对 moment 模板的额外成本
须按未完成目标的实际 source covariance 重用数量判断。

当前 run 未结束前不创建重叠科学运行。若它已完整成功，不能以“优化”
名义重做旧目标；若有失败的完整门或尚未完成的目标，后继 owner 才可
将本篇作为明确不同的 whole-cell upper 配方，并保留原所有实际结果。
一个新的 scalar 仍只授其已实际完成的范围，不由本纯恒等式授予全逆。
