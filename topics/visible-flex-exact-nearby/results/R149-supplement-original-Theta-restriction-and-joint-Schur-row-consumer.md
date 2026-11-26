# R149 TQ：原 Θ 的有限限制与完整 Schur 辅助行消费

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**新增解析结论及可执行纯合同。** OT 的整个96行、2240模式 exact
dyadic carrier 和完整联合误差，给出真正 $\Theta Q_{97}$ 的 signed
方阵，而不需要再次计算 IR/AS/OT 的旧范数。该方阵的逆门与 SC 的两个
physical/incoming 方阵是不同目标。本文还给出同一个 OT 对象在
[WGB.32](R133-supplement-exact-graph-parameterization-and-physical-finite-border.md)
中首96条辅助行的完整联合误差公式，保留所有 high feedback 和正确符号。

这里没有 OT 数值成功或有限逆的预报。实际消费者必须先取得 OT 的完整
10目标、whole actual/execution/manifest 和全 source closure；仅一条
误差球、prefix、trial hash 或 SC 的一个矩阵不能启动这个新目标。

## TQ1. 输入和输出不是 SC 的同一张矩阵

沿 [WFI](R133-supplement-graph-domains-and-finite-index-ledger-for-the-reflected-waist-row.md)、
[DT](R149-supplement-original-same-sign-source-Toeplitz-and-Theta-row-action.md)、
[TM](R149-supplement-original-model-adjoint-on-complete-finite-Theta-rows.md)
和 [TP](R149-supplement-complete-alpha-error-products-for-original-Theta-rows.md)，固定

\[
Y=Y_a^0=P\operatorname{Fix}(R_a)\cap L^2(\mathbb T;\mathbb R),
\quad \ell=\pi/2,\quad d x/\ell,
\quad v_n^a(x)=\sqrt2\cos(4nx-2na),
\quad a=2\mathcal H(0),\ b=a+\Omega.
\tag{TQ.1}
\]

所有 $v_n^a$ 在同一个真实 $Y$ 中正交归一。令
$E_N^a:\mathbb R^N\to Y$ 插入前 $N$ 个这样的模式。
原 $E_{96}$ 则插入 source/root 的真实 normalized even96 modes；
两种 injection 不按名称混用。完整坐标行是

\[
\Theta=V_Q\overline G
 =E_{96}^*D_+^{-1}\mathcal C^{-1}\mathcal A\overline G:
       Y\longrightarrow\mathbb R^{96}.
\tag{TQ.2}
\]

$\mathcal A=Id-\mathcal T_\alpha I$ 保留 same-sign Toeplitz，
$\overline G$ 的 low96 reference 为1，high 使用原 CYA multiplier；
物理频率4、signed $\mu$ 和真实相位均保留。source row 的输出坐标
是原 root96 Euclidean 坐标。它不是一个 physical density mean。

OT 所保存的全部 exact dyadics $t_{jn}$ 定义一个确切有限算子

\[
\widehat\Theta u
 =\left(\sum_{n=1}^{L}t_{jn}\langle v_n^a,u\rangle\right)_{j=1}^{96},
\qquad L=2240,
\qquad \|\Theta-\widehat\Theta\|_{Y\to\ell^2}\le e_\Theta.
\tag{TQ.3}
\]

$e_\Theta$ 必须是 OT 最后一条完整误差 upper，含 IR 全频残差、AS 全
cohomological divisor/alias/tail、原 $A^*$、model one-loss、所有相位
及 formal ball 到 exact dyadic 的 rounding；不能拿前一条未含 rounding
的数代替它。有限 trial 仅在 $n>L$ 精确为零，真正 $\Theta$ 没有这种
零尾结论。

[JF.1–4](R149-supplement-joint-signed-finite-matrix-error.md) 中 SC 的矩阵是
$\langle v_i^a,A_\partial Y_j\rangle$ 或声明型 incoming cosine 配对。
其第 $j$ 列是物理解的腰部数据；(TQ.3) 的第 $n$ 列则是 $\Theta$
对图域目标基向量 $v_n^a$ 的作用。二者的 source、target 和 normalizer
均不相同。特别地，WGB 的物理列还含原 target $\mathcal B^{-1}$，而
SC 只存96个低配对；这既不恢复整个 $Y$ 列，也不恢复它的第97–2240
坐标。不能把那些未观测坐标设零来使用 (TQ.3)。

## TQ2. 第一张实际可消费的新方阵

定义

\[
T=\Theta E_{96}^a:\mathbb R^{96}\longrightarrow\mathbb R^{96},
\qquad \widehat T=(t_{jn})_{1\le j,n\le96}.
\tag{TQ.4}
\]

这完整包含96行96列。由 $E_{96}^a$ 是等距 injection，立即有

\[
\|T-\widehat T\|_2\le e_\Theta.
\tag{TQ.5}
\]

这里没有逐行再乘 $\sqrt{96}$，也没有把 root/source 基和 target 基
认作相同函数来宣称 $T=Id$。它们的全部关系已经在 OT 的 signed
coefficients 中。两项 physical mean 与其它 finite border 也不在
这96维空间里。

新 public target 可以从整个原 OT carrier 只读提取 $\widehat T$，
选择完整 exact dyadic trial inverse $B$，再作完整 signed 乘法

\[
E_0=Id-B\widehat T,\qquad
r_0\ge\|E_0\|_2,\quad b\ge\|B\|_2,
\qquad \rho=r_0+b e_\Theta.
\tag{TQ.6}
\]

整个 $E_0$ 必须在取绝对值之前形成。完整矩阵的 row/column absolute
sums 给 $\|M\|_2\le\sqrt{\|M\|_1\|M\|_\infty}$，完整 Frobenius
bound 是另一 whole candidate；每个候选先保存读回，再选择整个上界。
只有正式保存的 upper 严格满足 $\rho<1$ 才有

\[
\|T^{-1}\|_2\le \frac b{1-\rho}.
\tag{TQ.7}
\]

inverse proposal 不存在或此充分门失败，也必须保留完整方阵、其所有
bound 和明确 false outcome。失败不证明 $T$ 奇异。即便通过，
(TQ.7) 也只是一张坐标方阵的逆，不是 physical low96 inverse 或完整
Schur 逆。

## TQ3. 该方阵通过后，原96条约束有准确的新坐标

本节仅在 (TQ.7) 已成立时使用。令
$Q=E_{96}^a(E_{96}^a)^*=Q_{97}$，$P=Id-Q$。定义

\[
R=P-E_{96}^a T^{-1}\Theta P,
\qquad J(c,p)=E_{96}^a T^{-1}c+Rp,
\quad c\in\mathbb R^{96},\ p\in PY.
\tag{TQ.8}
\]

则精确地

\[
\Theta R=0,\quad PR=P,\quad
\Theta J(c,p)=c,\quad PJ(c,p)=p,
\quad J(\Theta u,Pu)=u.
\tag{TQ.9}
\]

这证明 $J$ 是 $\mathbb R^{96}\oplus PY$ 到 $Y$ 的同一真实 bounded
坐标同构，并将原约束 $\Theta u=0$ 变成 $c=0$。若
$\tau\ge\|\Theta P\|$，则两个输出频带正交给

\[
\|Rp\|^2=\|p\|^2+
 \|T^{-1}\Theta Pp\|^2
\le (1+\|T^{-1}\|^2\tau^2)\|p\|^2.
\tag{TQ.10}
\]

这只改变原高图的表示，不供应任何 Poisson 列。对 WGB.27 的实际
已实现方程 $(Id+K)u+U\Theta u=f$，真正代回后仍是

\[
(Id+K)Rp+\big((Id+K)E_{96}^aT^{-1}+U\big)c=f.
\tag{TQ.11}
\]

括号中的完整有限列不能改写成没有证明的 $H_{\rm phys}$，而

\[
P(Id+K)R=Id_P+PKP-PKE_{96}^aT^{-1}\Theta P
\tag{TQ.12}
\]

仍有真实有限反馈。原 $Id_P+PKP$ 的逆门不能不付最后一项就移给
(TQ.12)；也可将该项按原 exact finite-factor algebra 完整保留。
所有 independent mean/height/phase/$\nu$ 列保持原方程。

## TQ4. 原 Θ 对一整组真正目标列的联合消费

令 $F=\mathbb R^m$ 带声明的 Euclidean coordinates，
$D_s=\operatorname{diag}(s_1,\ldots,s_m)$，$s_k>0$，
而 $X:F\to Y$ 是一个已经完整定义的列算子。假设有限 trial
$\widehat X$ 已按同一个真实基 (TQ.1) 给出全部 signed coefficients，
并有整个无限域误差

\[
\|(X-\widehat X)D_s^{-1}\|\le d_X,
\quad \|\widehat X D_s^{-1}\|\le b_X,
\quad \|\widehat\Theta\|\le b_\Theta.
\tag{TQ.13}
\]

只有该 finite trial 的 $n\le L$ 部分进入确切配对
$\widehat M=\widehat\Theta\widehat X$；这是 (TQ.3) 的有限定义，
并不是省略真正 $X$ 的高频。完整相乘保留所有96行和全部 $m$ 列。
由准确差分

\[
\Theta X-\widehat\Theta\widehat X
 =(\Theta-\widehat\Theta)\widehat X
       +\Theta(X-\widehat X)
\]

得到 whole joint bound

\[
\boxed{\quad
\|(\Theta X-\widehat M)D_s^{-1}\|
 \le e_\Theta b_X+(b_\Theta+e_\Theta)d_X .
\quad}
\tag{TQ.14}
\]

若另有整个真列算子 bound $b_X^{\rm true}$，另一合法 whole candidate
是 $e_\Theta b_X^{\rm true}+b_\Theta d_X$，由相反次序的准确差分得到。
只比较完整保存的候选；不能从其中减去某个 upper。

这里的 $d_X$ 是 source-weighted 整个列算子误差，已经包含全部列。
若只有各列 norm $d_k$，可用
$d_X=(\sum_k(d_k/s_k)^2)^{1/2}$；不假设不同列误差正交。
若还有 target weights $D_t$，直接使用
$\|D_t(\Theta X-\widehat M)D_s^{-1}\|\le\|D_t\|$ 乘 (TQ.14)，
或在完整 signed preconditioner 后使用 $\|BD_t\|$。这不把
source weights 和 target weights 互换。

例如 SC 的 $D_j$ 控制完整 waist 空间
$\mathcal Y_0=L_0^2(\mathbb T;\mathbb R^2)\oplus\mathbb R^2$。
若某列确为 $X_j=\mathcal B^{-1}A_\partial Y_j$，则 trial 必须先经过
同一个全 receiver 和真正 target inverse，才成为 (TQ.13) 的
$\widehat X_j\in Y$。可用 WBP.9 的完整 $K_{B,0}$ 和 JF.4 的
$B_{H,0}/\sqrt2$ 接收 $D_j$，但两个 unsigned norms 不产生该 signed
trial 列。其 inverse-trial residual、角误差、完整 tail 和有符号配对
都须另实际形成。独立 physical means 的 matching rows 不因此消失。

## TQ5. WGB.32 中首96条辅助行的正确整体算子

保持 WGB.29 的已实现完整 square、原有限 factors 和实际 high gate。
写 $U=[U_{\rm phys},U_{\rm aux}]$，
$V=(\Theta,V_{\rm aux})^t$；只有首96个 factor coordinates 对应
$U_{\rm phys}=H_{\rm phys}-\overline MC_Q$ 和 $\Theta$。
其它 root/head/coefficient finite factors 仍有自己的真实 rows，不能
用 OT 代替。若完整物理 space 另含有限 mean slots，采用 WGB.28 的
$Y\oplus\mathbb F$；$\Theta$ 在该**声明的 reference coordinate**
上是 $(\Theta,0)$，其所有 mean cross maps 保留在 $K,U,g,\ell$ 中。
未经消去的未知径向 function 不能被算作有限 $\mathbb F$。

令 $P=P_J\oplus0_{\mathbb F}$、$Q=Id-P$、
$H=Id_P+PKP$，以及 $h\ge\|H^{-1}\|$。将同一 source
$Q(Y\oplus\mathbb F)\oplus\mathbb R^r\oplus\mathbb R$ 的全部列一起写为

\[
B_H=[PKQ,\ PU,\ Pg],\qquad
W=H^{-1}B_H,
\qquad X=[-Q,0,0]+PW.
\tag{TQ.15}
\]

这里最后一维是原 metric variation $\varkappa$，不是 coefficient
mean。原96个辅助 equations 的整行块准确为

\[
S_\Theta=[0,J_{96},0]+\Theta X,
\qquad
J_{96}(z_{\rm phys},z_{\rm aux})=z_{\rm phys}.
\tag{TQ.16}
\]

这同时给出 $-\Theta Q+\Theta PH^{-1}PKQ$、
$J_{96}+\Theta PH^{-1}PU$ 和**正号**的
$\Theta PH^{-1}Pg$，不逐块交换算子次序。
第二 right side 是同样**正号**的 $\Theta PH^{-1}Pf$。
原零约束 WGB.22 的 right side 是负号；两者不能混用。

若 $\widehat W$ 是完整有限 high trial，并已经认证

\[
\|(H\widehat W-B_H)D_s^{-1}\|\le\rho_H,
\tag{TQ.17}
\]

则取 $\widehat X=[-Q,0,0]+P\widehat W$，有 $d_X\le h\rho_H$。
把它代入 (TQ.14) 即得**整个**首96辅助行的误差；不分别按96行放大，
也不把各项 marginal upper 伪作相互独立的 signed coefficients。
(TQ.17) 必须包围完整 $K\widehat W-B_H$ 的所有 Fourier 输出、
mean/finite cross、真输入模型差和无限 tail。仅 finite Galerkin residual
不能充当它。

若 $J>L$，(TQ.3) 准确给 $\widehat\Theta P_J=0$。此时有限 high
trial 配对为零，但真正 high feedback 仍须支付
$\|\Theta P_J\|\,\|H^{-1}B_H\|$ 或上述完整误差。
可独立选用 WGB.20/SDI 的完整 tail bound；不能因此把真正反馈设零。
OT 的有限带宽也不把 $Q_J$ 从 $J-1$ 维改为2240维。

## TQ6. 首次实际输出合同

配套纯模块是
[fourfold_codazzi_original_Theta_finite_consumer_math.py](../scripts/fourfold_codazzi_original_Theta_finite_consumer_math.py)。
它没有 IO、没有数值库 import，不执行旧 finite-row、cohomology 或
norm producer。

第一项可独立执行的新对象是 (TQ.4) 的**完整**96×96 true matrix
enclosure 和 (TQ.6–7) 的明确 true/false 门。其 owner 必须：

1. 完整准入 OT 的10条记录、parent actual/execution/manifest、同源
   selected member 与源/目标 phase；其中每一 false full-Schur flag 原样保留。
2. 只恢复 OT 原 finite carrier，要求整个96×2240 byte count/SHA、
   little-endian dyadic encoding 和 true-basis identity 一致；不重新计算
   IR/AS/OT 任何已成 norm/residual。不能只核将要使用的96×96前块。
3. 保存整个新 signed square、exact inverse trial、signed preconditioned
   residual 和全部 whole norm candidates 的 private hashes；公共输出
   保存完整新 bounds、严格 gate outcome、原10目标和载体的全身份。
4. 每个依赖球都先完整保存读回；全门失败也保存，并保持
   `full_physical_Schur_proved=false`。未来实际 Schur 仍须完整
   $K/U/g/\ell/\omega$、两 mean、真 phase/$\nu$、high inverse 和
   (TQ.17) 的整个域，不能由这个坐标 inverse 代替。

这个合同不改变当前冻结的 OT 或 SC 源码，也不生成先验占位 actual、
workflow 或新数值结果。后继直接消费真正完整对象，不增加一次旧成功目标。
