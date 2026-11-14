# R119 续篇：固定标量正常形、斜率单位全余项与新高网络阈值

2026-11-14，visible-exact / tail_connector。

**状态：已证明（固定背景的完整标量正常形及无层权高网络；移动中间系统仍待闭合）。** 本篇继续
[完整负散射及正负网络算子乘积](R119-supplement-complete-negative-scattering-and-network-word-in-slope-units.md)，
在同一个实际 $\Gamma^*(a,\Omega)$ 上支付 KAM、首次相位同调、
完整两行预条件和全部 ordering 差。没有改变原已固定的
$\omega_i,\beta_i^0$。

令 $g=4/3$，较深胞元为 $j$，仍置

$$
J=j+5,\qquad \delta=\delta_j,\qquad
\lambda_i=2^{32}\sqrt J\,\delta_j^{-9/4}.
\tag{Z.1}
$$

结论是在第6节的准确完整波表示中，所有非mean内部行有

$$
(\mathcal D+\mathcal E)z=\mathfrak g,\qquad
(\mathcal D_i)_n=
 [1+e^{i(n\omega_i+\beta_i^0/n)}]I_2,\quad n\ne0,
\tag{Z.2}
$$

$$
\boxed{\quad
\|\mathcal E_i:H^s(\text{相邻全部端口})\to H^{s+g}\|
 <2^{20000}\lambda_i^g,\qquad -g\le s\le0.
\quad}
\tag{Z.3}
$$

全部实际 mean 行仍按原完整方程保留，未被 (Z.2) 的记号覆盖。
输入的 mean 列、全部低模、外端口、ordinary/weak 源及两列
$D\Gamma^*$ 进入同一准确 $\mathcal E$ 或 $\mathfrak g$。

在

$$
T_i^{\rm new}=2^{65536}\lambda_i^4
       =2^{65664}J^2\delta_j^{-9},\qquad
P_{H,i}=\mathbf1_{\{|m|\ge T_i^{\rm new}\}},\quad m=4n,
\tag{Z.4}
$$

上，真正完整高反馈 norm小于 $2^{-1024}$。这里的 Fourier 标签
是下文共轭后的固定角，周期仍为 $\pi/2$；原物理两迹通过准确
波表示恢复。这个高块仍不等于全网络 inverse；完整低系统、
外响应、移动混频簇与原强标签权的最终闭合继续保留。

## 1. 两个尺度预算和完整基础窗

前篇 (W.2)、(W.50) 给实际酉 $S_-$、明确酉模型 $S_-^{(1)}$
及完整正负网络的两个基础窗

$$
H^0\to H^g,\qquad H^{-g}\to H^0,
\qquad C_{\rm word}<2^{9020}\lambda_i^g.
\tag{Z.5}
$$

原 controlled 角费用是

$$
\epsilon_i^c=2^{8192}J^{16}\delta_j^{-16}
                  (N_j^c)^\#\mathcal X,\qquad
\sum_i\epsilon_i^c<2^{-102096}.
\tag{Z.6}
$$

它包含实际各端角、26阶角导和首次相位 cohomological 逆；
依据是第51束 (H.5) 的逐项组成及第55束 (N.16) 的同对象重付。
这些是角导数，未对径向 $C^4$ profile 索取额外高导数。

本篇还用前篇已完整证明的

$$
\sum_{j\ge129}2^{5000}J^{20}\delta_j^{-30}
                       (N_j^c)^\#\mathcal X<2^{-22144}.
\tag{Z.7}
$$

因为

$$
\frac{\lambda_i\epsilon_i^c}
 {2^{5000}J^{20}\delta_j^{-30}(N_j^c)^\#\mathcal X}
 =2^{3224}J^{-7/2}\delta_j^{47/4}<2^{3224},
$$

包括每层有限两个分量的固定因子后，安全地有

$$
\sum_i\lambda_i\epsilon_i^c<2^{-18918}.
\tag{Z.8}
$$

这条门支付在大径向首相位之后搬移实际小角图产生的角非mean。
不能仅以 $\epsilon_i^c<1$ 推测所有大相位共轭仍同阶有界。

所有算子采用标准角 $x=4\phi$，$x\in\mathbb T_{2\pi}$，
但 Sobolev norm仍为物理权 $(1+16n^2)^{s/2}$。
记 $D=-i\partial_x$、$\Lambda=|D|$、$\Pi_0=\langle\cdot\rangle$、
$P=I-\Pi_0$，$\Pi_\epsilon$ 投到 $\epsilon n>0$。
$D^{-1}$ 与 $\Lambda^{-1/2}$ 在 mean 上为0；两个实际 mean
状态绝不以此定义删除。

## 2. signed-density 坐标下的准确 phase 换元

令 $K$ 为同一个已付实际角微分同胚，记

$$
C_Kf=f\circ K,\qquad \mathcal D_Kf=K'f\circ K,\qquad
T_K=\Lambda^{-1/2}\mathcal D_K\Lambda^{1/2}
\quad\text{于 }PH^0 .
\tag{Z.9}
$$

mean 上另取恒等。原 signed-Green 恒等式给
$T_K^{-1}=T_{K^{-1}}$。直接链式法则还给准确恒等式

$$
D C_K=\mathcal D_KD,\qquad
D^{-1}\mathcal D_K=P C_KD^{-1}.
\tag{Z.10}
$$

第二式中的 $P$ 不能删除。对实系数 $a$，在某个固定角锥定义
自伴 order-minus-one 算子

$$
A_\epsilon(a)
 =\Pi_\epsilon\Lambda^{-1/2}M_a\Lambda^{-1/2}\Pi_\epsilon .
\tag{Z.11}
$$

在这个锥上，$\Lambda^{-1}=\epsilon D^{-1}$。跨出该锥的部分
先保持为原真实跨锥 operator。于是

$$
T_K^{-1}A_\epsilon(a)T_K
 =A_\epsilon(a_K)+R(a,K),
\qquad
a_K=(a\circ K^{-1})(K^{-1})',
\tag{Z.12}
$$

其中 $R$ 由明确的两类项组成：跨锥项，以及 (Z.10) 中的
mean projection。若暂不写锥投影，后者准确为

$$
-\Lambda^{-1/2}\mathcal D_{K^{-1}}a\;
             \Pi_0 C_K\Lambda^{-1/2}\Pi_\epsilon .
\tag{Z.13}
$$

该式是向量乘线性泛函，外侧所有 $\Lambda^{-1/2}$ 仍带 $P$。
它不是把物理常高度当作某个被删掉的方向。
为核 (Z.12)，用 (Z.10) 展开

$$
\Lambda^{-1/2}\mathcal D_{K^{-1}}M_a
       \Lambda^{-1}\mathcal D_K\Lambda^{1/2},
$$

主项恰为
$\Lambda^{-1/2}M_{(a\circ K^{-1})(K^{-1})'}\Lambda^{-1/2}$；
两个 $\epsilon$ 相消。余下正是 (Z.13) 及已保留的跨锥块。

原 unitary $U_K$ 是 $\Pi_\epsilon T_K\Pi_\epsilon$ 的 polar
校正，未用裸 pullback。前篇 (W.18) 及其真实 adjoint 给
cross/polar 的20阶门。mean 泛函的 Fourier 系数来自
$(K^{-1})'-1$，有同一实际解析条带和角小量。
因此只需前三阶 $a$ 界和原26阶 $K$ 界，就得到

$$
\|U_K^{-1}A_\epsilon(a)U_K-A_\epsilon(a_K):
                         H^0\to H^2\|
 <2^{6144}\lambda_i\epsilon_i^c
\tag{Z.14}
$$

于本篇各实际 $a$。同一式反向使用 $K^{-1}$ 也成立。

具体费用如下。cross/polar 先付前篇的 $2^{4096}\epsilon_i^c$
20阶门，取其中3阶即可；外乘、真实复合和两个半阶 Fourier
权的全部前三阶费用小于 $2^{1024}$。系数 $a$ 的实际前三阶和
相应 Fourier 加权和在下一节小于 $2^{512}\lambda_i$。
mean 输出向量的 $H^2$ norm同样小于 $2^{1024}\lambda_i$；
mean 泛函及其两阶 adjoint 小于 $2^{1024}\epsilon_i^c$。
最坏的指数和 $4096+1024+512$，加有限项计数，仍严格小于6144；
所以全部项落在 $2^{6144}\lambda_i\epsilon_i^c$ 中。
这里没有用未定义的通用 pseudodifferential 常数。

unitary 角表示的群关系也只差同一 cross/polar 平滑项：
$T_KT_H=T_{H\circ K}$ 在完整 signed 表示准确成立，
压缩与 polar 后其差在 $H^0\to H^2$ 小于
$2^{6144}\epsilon_i^c$。mean 上群关系准确，因为模型取恒等。
这明确支付后面全部有限 principal 组合的误差。

## 3. 每个真实首 phase 的自然尺度

下列都是前篇算子乘积中的同一准确 phase，先列物理频率 $m$
的系数；换成 $n=m/4$ 只再除4。

* root 的系数为
  $a_{\sigma\epsilon}=(b/2)\int_0^H
   V(q,\phi-\sigma\epsilon\,2q^{3/2}/(3b))q^{-1/2}dq$，
  其固定复角条带 supremum小于 $17b/8<3b$。
* 自由两行的次首系数是
  $-5b/(48H^{3/2})=-(160/3)b$。它径向，不消耗角导。
  $M\,2H^{3/2}/(3b)$ 和 $\pi/4$ 保留在 principal/Maslov 因素。
* graph 的系数是其完整真实
  $\frac12\int H_\sigma'\kappa_s\circ H_\sigma\,ds$，
  $\kappa_s=(g-H)\kappa$。由 $|g-H|<2^{13}n_i$、
  $|\kappa|<2^{17}b$ 及原角 Jacobian 门，sup小于
  $2^{32}bn_i$。
* strict 的径向系数积分小于
  $\frac12 I_1<2^{255}\lambda_i$。
  实际系数仍为完整
  $\frac12\int H_\sigma'\kappa\circ H_\sigma\,dt$；
  非径向差与其所需角导由 (Z.6) 支付，因此可统一取
  $2^{258}\lambda_i$。

每一个都保留其真正两个 wave 号和两个角锥，不是用其平均
替代函数。所有 inverse phase 只改符号。
沿至多32个实际 principal 角图搬移，用 (Z.12) 的准确 density
换元。每个图相对于其真正径向平移的 $C^1$ 差由 (Z.6) 支付，
故这有限次复合的虚部放大仍小于2；可共同使用原物理角的
固定宽 $1/1024$，不按次数重复缩窄角域。
在此共同条带上，每个 Jacobian 和逆的乘积小于 $2^{32}$；
Cauchy 到四阶以及 Fourier moment 费用小于 $2^{160}$。因此对全部搬移后的 phase，足以取

$$
\|A_k:H^r\to H^{r+1}\|<2^{512}\lambda_i,
\qquad r=0,1,\qquad
\|\exp(itA_k)^{\pm1}:H^r\to H^r\|<2,\quad 0\le r\le2,
\tag{Z.15}
$$

$|t|\le1$。第二门的理由是：真正径向大平均与 Fourier 权准确
交换；剩余角部分及其四阶同阶 commutator 小于
$2^{2048}\lambda_i\epsilon_i^c<2^{-16800}$，由 (Z.8) 支付。
准确 Duhamel/能量再给 $<2$，不把径向大平均的绝对值放进指数。

以上数字来源也说明径向大首系数本身只有 $C\lambda_i$：
新的 strict $I_1$ 是实际各坡积分，不是原
$J^2\delta^{-5}$ supremum 粗包络。原两根首项、normal shear
及完整 graph phase 均参加了这个改进。

将 symmetric 约定换成第49束的右置 $a(x)/n$ 约定时，其差
同样有明确两阶门。在可比同号频率上，

$$
\big||k|^{-1/2}-|n|^{-1/2}\big|\,|n|^{-1/2}
 \le 4|k-n|\,|n|^{-2},
\tag{Z.16}
$$

其余频率使用实际解析 Fourier 尾。乘输出两阶权并求完整行、
列和，得到该 ordering 差小于 $2^{512}\lambda_i$。
mean 和跨锥列按前节保留。这不会改变已经识别的第一
$1/n$ 系数或它的平均。

## 4. 从有限 unitary word 到完整首符号

取前篇 $M=(0,M_B;M_C,0)$。为固定与原算术相同的号数，
在正角锥使用

$$
V_i=-M_C^*M_B.
\tag{Z.17}
$$

在负角锥使用 $-M_B^*M_C$；它是正锥的真实共轭约定。
这是一个准确的满射 unitary。两个 mean 上把 $V_i$ 定义为
$-I$，只用于模型；实际 mean 行不在本节被消元。

径向核对可直接确定号数。原完整两根模型为
$\operatorname{diag}(e^{-i\Phi},e^{i\Phi})P$，
$\Phi=MS+\pi/2+b/M$。因此正锥 (Z.17) 恰为

$$
-e^{-2i\Phi}
 =e^{-i(2MS+2b/M)}
 =e^{i(n\omega_i+\beta_i/n)},\qquad
\omega_i=-8S,\quad\beta_i=-b/2.
\tag{Z.18}
$$

负锥采用上面相反的消元方向，得到此式的真实共轭。
这保留原两个 $\pi/4$ 和外面的负号，没有重新选择 Maslov 号。

按 (Z.14) 将全部 principal 角图移到同一端，并用其群关系
逐次合并。phase 因素数和所需 principal 操作都小于32。
每一次换元的 exponent 差由准确 Duhamel 支付：
若生成元差为 $R$，则

$$
e^{i(A+R)}-e^{iA}
 =i\int_0^1 e^{i(1-t)(A+R)}R e^{itA}\,dt .
\tag{Z.19}
$$

在真正的 $H^0\to H^2$ 窗中按原次序消费 (Z.14) 与
(Z.15)，所有这类项及 principal 群差的和小于
$2^{6400}\lambda_i\epsilon_i^c$；这里6144位的单项费用之外，
至多32项及原模型的有限 $H^2$ 乘积最多再收 $2^{128}$。

实际 principal return 与 KAM 端图满足第55束 (N.15) 的

$$
R_i\circ K_i=K_i\circ T_{\omega_i}.
\tag{Z.20}
$$

这是标准角 $x$ 的式子。因为 $T_KT_H=T_{H\circ K}$，正确的
unitary 表示共轭方向是
$U_{K_i}U_{R_i}U_{K_i}^{-1}$。在该共轭后，principal 恰为
$e^{i\omega_iD}$ 加上述已付平滑项；mean 的 $-I$ 独立保留。

剩下是有限个 $\exp(iA_k)$ 的有序乘积。令
$F(t)=\prod_k\exp(itA_k)$，两次微分后每项恰含两个 $A_k$
及原有序 exponent 因素。第一个 $A$ 消费 $H^0\to H^1$，
第二个消费 $H^1\to H^2$；所有中间指数均在同一窗
$0\le r\le2$，由 (Z.15) 支付。
项数小于 $32^2$，所以

$$
\|F(1)-I-i\sum_kA_k:H^0\to H^2\|
 <2^{1200}\lambda_i^2.
\tag{Z.21}
$$

$\exp(i\sum_kA_k)$ 的二次余项也满足同一个门；其角非mean
仍由 (Z.8) 的有限和控制。该证明既不假设各 phase 对易，也
不把两个 $H^0\to H^1$ 界错误地放在相同输入窗。

每次 density 换元的平均准确保持：
$\int(a\circ K^{-1})(K^{-1})'=\int a$。
于是完整一次系数恰是
[第49束 (B.5)–(B.10)](R119-supplement-actual-nonradial-first-density-phase.md)
的同一个实际 $B_i(x)$，而不是另造的近似系数。具体包括两个
root potential 积分、完整 $-5/48$ 自由项、graph 的首项、
整个 strict 的真实密度项及所有原角 Jacobian。
这里的首系数还可直接对照[完整两行自由Airy勘误](R119-supplement-complete-free-Airy-two-row-frame-and-low-frequency-erratum.md)的 A.5、A.7、A.14–A.15：完整 normal shear 仍给同一个 $-5b/(48H^{3/2})$；勘误修正低非mean的同阶范数，不改变该首系数。第49束 B.7–B.10、B.13、B.15–B.18、B.21–B.23 保留了 Piola、变图密度、两根和 positive 的对应项；本处不借旧 H.17 的错误中间界。

第55束联合参数行已经准确保证

$$
\langle B_i\rangle=\beta_i^0.
\tag{Z.22}
$$

由 (Z.16) 支付两种量子化的差后，全部有限操作因此给

$$
U_{K_i}V_iU_{K_i}^{-1}
 =e^{i\omega_iD}\exp(iA(B_i))+R_i^{(2)},
\qquad
\|R_i^{(2)}:H^0\to H^2\|<2^{6600}\lambda_i^2.
\tag{Z.23}
$$

这里 $A(B_i)$ 在正锥是 (Z.11)，负锥带对应的负号，准确
首符号为 $B_i/n$；mean 上为0。
$e^{i\omega_iD}$ 在本模型的 mean 上读作 $-I$。
有限个 cross/polar/mean-rank-one 项全部在 $R_i^{(2)}$ 中。

## 5. 同一个首相位同调及输出插值

原 cohomological 方程是

$$
q_i-q_i\circ T_{-\omega_i}=\beta_i^0-B_i,
\qquad \langle q_i\rangle=0.
\tag{Z.24}
$$

它的存在、实际 Diophantine divisor、固定角余宽及26阶角导
已经由 (Z.6) 支付。选择完整自伴 signed symmetric 算子

$$
Q_i=\sum_{\epsilon=\pm1}
 \epsilon\Pi_\epsilon\Lambda^{-1/2}
          M_{q_i}\Lambda^{-1/2}\Pi_\epsilon,\qquad Q_i\Pi_0=0.
\tag{Z.25}
$$

其所需降一阶范数及同阶能量远小于1，
$e^{\pm iQ_i}$ 是真正 unitary，$H^r$ 正逆 norm小于2。
没有用任意复杂 operator 的逐矩阵共轭小除数取代原已证标量同调。

令 $Q_{i,-}=e^{-i\omega_iD}Q_i e^{i\omega_iD}$。
准确平移使它的系数为 $q_i(x-\omega_i)$。
因此

$$
e^{-iQ_i}e^{i\omega_iD}e^{iA(B_i)}e^{iQ_i}
 =e^{i\omega_iD}e^{-iQ_{i,-}}e^{iA(B_i)}e^{iQ_i}.
\tag{Z.26}
$$

用同一两次有序 Duhamel，三个 exponent 的一次和准确为
$A(B_i)+Q_i-Q_{i,-}=\beta_i^0D^{-1}$ 于非mean；
其余项降两阶，费用不超过 $2^{1200}\lambda_i^2$。
和 (Z.23) 相加，定义完整 unitary

$$
\mathcal W_i=U_{K_i}^{-1}e^{iQ_i},\qquad
\mathcal U_i^0=
 \Pi_{\ne0}e^{i\omega_iD}e^{i\beta_i^0D^{-1}}-\Pi_0,
$$
$$
\widetilde V_i=\mathcal W_i^*V_i\mathcal W_i,\qquad
\boxed{\quad
\|\widetilde V_i-\mathcal U_i^0:H^0\to H^2\|
 <2^{6700}\lambda_i^2 .
\quad}
\tag{Z.27}
$$

$\mathcal W_i$ 的 $H^r$ 正逆 norm小于4，$|r|\le2$，
且它准确保持 mean。实际 mean 并未被 $\mathcal U_i^0$ 取代。

两个被比较的完整算子都真正 unitary，所以其差在 $H^0$
上的 norm至多2。固定输入 $H^0$，对输出0阶和2阶作 Hilbert
插值，得到

$$
\|\widetilde V_i-\mathcal U_i^0:H^0\to H^g\|
 \le2^{1/3}(2^{6700}\lambda_i^2)^{2/3}
 <2^{4500}\lambda_i^g .
\tag{Z.28}
$$

反向基础窗不需再粗乘真实 $H^g$ Cauchy：
若 $R=\widetilde V_i-\mathcal U_i^0$，则准确有

$$
R^*=-(\mathcal U_i^0)^*R\,\widetilde V_i^*.
\tag{Z.29}
$$

左侧 Fourier 对角的 $(\mathcal U_i^0)^*$ 在所有 Sobolev 窗
是 norm1，右侧只消费 $H^0$ unitary。因此 $R^*$ 也满足
(Z.27)–(Z.28)。对偶给相同 $H^{-g}\to H^0$ 界。

## 6. 准确两行预条件、mean 与原源

先在正角锥写 $B=M_B,C=M_C$。前篇完整散射模型为
$S_-^{(1)}=(0,B^*;C,0)$。定义两个准确 unitary 矩阵

$$
\mathcal R_i=\operatorname{diag}(I,C^*),\qquad
\mathcal C_i=\operatorname{diag}(I,B)
                      \begin{pmatrix}0&I\\I&0\end{pmatrix}.
$$
$$
\mathcal R_i(I+S_-^{(1)})\mathcal C_i
 =\begin{pmatrix}I&I\\C^*B&I\end{pmatrix}
 =\begin{pmatrix}I&I\\-V_i&I\end{pmatrix}.
\tag{Z.30}
$$

负角锥改取
$\mathcal R_i=\operatorname{diag}(I,B^*)$、
$\mathcal C_i=\operatorname{diag}(I,B)$，得到同样形式，
其中 $V_i=-B^*C$，正是 (Z.17) 后指定的真实共轭约定。
mean 上 $\mathcal R_i,\mathcal C_i$ 均取恒等，保原两个方程。

再对两行共同使用
$\mathbf W_i=\operatorname{diag}(\mathcal W_i,\mathcal W_i)$。
其模型下左块是 $-\widetilde V_i$。把
$\widetilde V_i-\mathcal U_i^0$ 按 (Z.28) 保留为真余项。
最后仅在非mean行上乘明确 Fourier 矩阵

$$
\mathcal A_i^0=
 \begin{pmatrix}I&-I\\\mathcal U_i^0&I\end{pmatrix},
\qquad
\mathcal A_i^0
 \begin{pmatrix}I&I\\-\mathcal U_i^0&I\end{pmatrix}
 =\operatorname{diag}(I+\mathcal U_i^0,I+\mathcal U_i^0).
\tag{Z.31}
$$

其同阶 norm小于2。原算术保证非mean的每个
$I+\mathcal U_i^0$ 都非零，因此这个行操作在分布意义下不增加
或删除非mean方程；并未预先使用其全空间有界逆。
mean 上保留单位行操作，从不使用 (Z.31) 的奇异模型 mean 块。

如果原实际 incoming 向量为 $a_i$，新未知恰定义为

$$
a_i=\mathcal C_i\mathbf W_i z_i .
\tag{Z.32}
$$

原完整源 $\gamma_i=q_{+,i}+(R_+q_-)_i$ 及所有外端口列，
按真正顺序变为

$$
\mathfrak g_i=
 [\Pi_{\ne0}\mathcal A_i^0+\Pi_0 I]\,
       \mathbf W_i^*\mathcal R_i\gamma_i .
\tag{Z.33}
$$

同一行矩阵作用全部相邻真实耦合。physical trace 仍由
$F_e\operatorname{diag}(U_K,U_K)F_e^{-1}$、原
$\alpha_e^{-1/2}$、normal shear 和总通量恢复；
这不是将模型角变换当作裸高度 pullback。

前篇 (Z.5) 的完整网络余项在两基础窗都小于
$2^{9020}\lambda_i^g$。上述 row/column 模型因素在输出窗
至多各收 $2^{64}$，$\mathbf W_i$ 至多4，最后行矩阵至多2。
forward 窗右侧只用真正 $H^0$ unitary，adjoint窗反过来；
不需要两边同时按高阶粗乘。
连同 (Z.28)、邻胞至多8倍的尺度、每行/列至多8个端口，
总费小于 $2^{10000}\lambda_i^g$，足以取 (Z.3) 的更宽
$2^{20000}\lambda_i^g$。两个端点窗的 Hilbert 插值给
$-g\le s\le0$，不声称未付的正 $s$ 窗。

ordinary、weak 的完整源和两列 $D\Gamma^*$ 在 (Z.33) 中
原样参加。若微分背景或选参图，$\mathcal R_i,\mathcal C_i,
K_i,Q_i$ 的真实微分也必须进入对应仿射列；
本篇不以固定背景的酉性把这些微分源设为0。
mean 行仍保原 total-flux 积分及物理平均，和高未知的反馈未删。

## 7. 真正高于有限算术截止的统一除法

[原完整两相位算术 (Q.7)–(Q.14)](R119-supplement-actual-two-parameter-complete-phase-arithmetic.md)
在同一固定目标给一个有限 $N_i$，并且

$$
N_i<2^{160}J^3\delta_j^{-13/2}.
\tag{Z.34}
$$

更关键的是其完整整数范数证明 (Q.9)–(Q.10)：
当 $|n|>N_i$ 时，到任一奇数倍 $\pi$ 的相位距离至少为
$1/(128|n|)$。于是取最近奇格点并用
$2\sin(x/2)\ge2x/\pi$，有

$$
|1+e^{i(n\omega_i+\beta_i^0/n)}|^{-1}
 \le64\pi|n|=16\pi|m|<2^{10}\langle m\rangle .
\tag{Z.35}
$$

这个高于有限截止的门没有原低频坏集的 $N_i$ 因子。
它已经由整数恒等式证明全部频率，并非只验证有限 n。
负锥由真实共轭得到同界。

(Z.4) 确实处在这个范围，因为

$$
\frac{T_i^{\rm new}}{4N_i}
 >2^{65502}J^{-1}\delta_j^{-5/2}>1.
\tag{Z.36}
$$

因此不能把 (Z.35) 偷用于仍在有限中频的模式，但每个新的
$P_{H,i}$ 都准确满足其条件。这里没有使用外部 finite head 的
旋转数或其四次根间隙；所用仍是本尾原有的固定两相位目标。

## 8. 完整高反馈、全部低输入和实际源

对 $-g\le s\le0$，由 (Z.3)–(Z.5) 及 (Z.35)，有对全部邻居
输入的准确高输出门

$$
\begin{split}
\|P_{H,i}\mathcal D_i^{-1}\mathcal E_i z\|_{H^s}
&<2^{10}2^{20000}
       (T_i^{\rm new})^{-1/3}\lambda_i^{4/3}
                       \|z_{\rm neighbors}\|_{H^s}\\
&=2^{-5506/3}\|z_{\rm neighbors}\|_{H^s}.
\end{split}
\tag{Z.37}
$$

$\langle m\rangle$ 与 $|m|$ 的固定比较、两行、邻胞及有限端口
计数即使共同宽放 $2^{16}$，仍小于 $2^{-1024}$。
所以对任一明确的

$$
\mathcal Z_s=\ell^p_i((H^s)^2),\qquad
p\in\{1,2,\infty\},
$$
$$
\boxed{\quad
\|P_H\mathcal D^{-1}\mathcal E P_H\|_{\mathcal Z_s\to\mathcal Z_s}
 <2^{-1024},\qquad
\|P_H\mathcal D^{-1}\mathcal E P_L\|<2^{-1024}.
\quad}
\tag{Z.38}
$$

必要时将有限个真实外端口按其原 $H^s$ norm作直和，并在这些
端口上定义 $P_H=0$；不为它们补齐一个虚构的内部方程。
行列度数至多8给相应 Schur/行和/列和；每一局部余项早已是
完整 Hilbert 空间算子，包含所有 Fourier lag，不能在此改成
仅逐模正型论证。有限度数使算子先逐行定义，再由上述一致界
作用全部序列；对 $\ell^\infty$ 没有使用有限支撑序列稠密。
$P_L=I-P_H$ 包括 mean、所有中频、原外端口
以及保留的有限外部分量；未给它们指定虚假的方程或反射。

给定整个低向量 $z_L$ 及原实际源，唯一高解准确为

$$
z_H=
 [I+P_H\mathcal D^{-1}\mathcal E P_H]^{-1}
 P_H\mathcal D^{-1}(\mathfrak g-\mathcal E z_L).
\tag{Z.39}
$$

一个直接充分源 norm 是

$$
\|\mathfrak g\|_{\mathcal Y_s}
 =2^{10}\|(\|\mathfrak g_i\|_{H^{s+1}})_i\|_{\ell^p}.
\tag{Z.40}
$$

若这个原有序变换后的真实 norm 有限，则

$$
\|z_H\|_{\mathcal Z_s}
 <2\left(\|\mathfrak g\|_{\mathcal Y_s}
                 +2^{-1024}\|z_L\|_{\mathcal Z_s}\right).
\tag{Z.41}
$$

这里没有从任意 raw 体源免费授予 (Z.40)：其 Piola、图迹、
ordinary/weak 源转换和全部 mean/端点荷仍按原实际合同给出。
高块解也未被宣称自动满足原指数角宽、层权和最终 $C^2$ 重建。

## 9. 尚未关闭的原问题量词

本篇新阈值把已付实际高块的径向幂从原
$\delta_j^{-320}$ 改为 $\delta_j^{-9}$，包括自由低端架勘误、
整个负散射、两端正片 cross、真实角正常形和全源 wiring。
没有调整公共度量、参数域或原相位目标来取得这个结论。

然而所有 $|m|<T_i^{\rm new}$ 的实际混频低系统、三个外响应、
真实 near-kernel 的频率定位及同一公共控制的同时选参仍然存在。
全高块只能为这些低未知给出准确 Schur 反馈；它不构成独立的
完整存在证明。最后非线性方程、固定约束、原单位源权与周期
重建还必须在课题原完成标准下同时闭合。
