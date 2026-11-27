# R149 BGR：同一 target B trial 的完整 signed Gram 与联合行误差改进

2026-11-27，`visible-exact-astra-fb31ed6-20261127 / trial_restore`。

**新增已证明的可计算界。** [DBRA](R149-supplement-actual-direct-target-w-and-complete-B-inverse-rows.md)
的真正全96行已经完成，其原完整 $e_R$ 保持有效。当前产品使用
$IY$ 的 Hilbert–Schmidt upper，尚没有计算这同一个 $IY$ 的完整
operator Gram。本条给一个确切新目标及其完整消费公式。
它不重算旧 DWT2/BR7，也不由旧 HS upper 反推较小 operator norm。

## BGR1. 原全空间、原整个 trial 与 Gram

沿 [BR.1–12](R149-supplement-target-normalizer-low-rows-by-whole-energy-residual.md)
固定物理周期 $\pi/2$、归一 $L^2$ 实内积、频率 $4n$。
DWTB run45935081577/1 的原 complete y trial、
complete exact rational r rows 分别具有全 SHA

- $[192,96,2]$ little-endian binary64 y：
  `b12281fc1b7419662c67b1bc44a94745481bab16e202fde1418ae7cacaa6d160`；
- $[96,192]$ full exact rational r：
  `a55176484d67a63e7ecf74d2eff287bd3d45b796746e6917f92f969d4518e1d3`。

取这同一
$\widehat r_j=G_{\rm abs}\widehat y_j$，
$G_{\rm abs}=|\partial_\phi|^{-1}$，并记

$
 Z:\mathbb R^{96}\to L^2_0,\qquad
 Zc=\sum_{j=1}^{96}c_j\widehat r_j,\qquad
 \widehat R=Z^* .
 \tag{BGR.1}
$

所有 r 的 mean 精确为零，负 Fourier coefficients 是正系数的
conjugates。它们不被当成正交行。$IY$ 与 $G_{\rm abs}Y=Z$ 只差
完整输出上的 unitary sign multiplier，所以

$
 \|IY\|_{\ell^2\to L^2}=\|Z\|=\|\widehat R\|.
 \tag{BGR.2}
$

新 Gram 的所有9216项准确为

$
 \Gamma_{jk}
   =\langle\widehat r_k,\widehat r_j\rangle_{L^2}
   =2\operatorname{Re}\sum_{n=1}^{192}
            \overline{(\widehat r_j)_n}(\widehat r_k)_n .
 \tag{BGR.3}
$

每条项在取绝对值以前先作完整 signed sum。完整 real Gram 自伴且
positive semidefinite，不需要任何 trial rank、conditioning、
pairwise orthogonality 或 sampled residual 假设。

设 $\mathbb G_{jk}$ 为 (BGR.3) 的整 formal ball，必须保96×96全部
entries 并完整保存读回。对每行定义

$
 s_j=\operatorname{up}\left(
       \sup\mathbb G_{jj}+\sum_{k\ne j}\sup|\mathbb G_{jk}|\right),
 \qquad g=\operatorname{up}\sqrt{\max_{1\le j\le96}s_j}.
 \tag{BGR.4}
$

Gershgorin 或自伴矩阵的完整 $\ell^\infty$ norm 给
$\lambda_{\max}(\Gamma)\le\max_j s_j$，从而

$
 \boxed{\ \|IY\|=\|\widehat R\|\le g.\ }
 \tag{BGR.5}
$

$g$ 是一个尚未计算的新 operator-norm 目标。原完整 HS upper
$J_{\rm HS}$ 只复制既成 DWTB 第3条，不能再次运行该 reducer。
两 whole bounds 正式存在后可选择
$J_{\rm op}=\min(g,J_{\rm HS})$ 的**整个** saved upper。
本条不预报哪一个更小。

## BGR2. 保持全 w 与全部有限残差的整行界

DBRA 已实际保存全部
$e_{w,\infty}$、$e_{w,2}$、$F_H$ 以及两 whole products

$
 P_{\rm HS}=e_{w,\infty}J_{\rm HS},\qquad
 P_2=\sqrt2 e_{w,2}B_I.
 \tag{BGR.6}
$

不重算任何这些旧目标。对任意实 $c\in\mathbb R^{96}$，
两个 same-sign blocks 的正交性给

$
 \|\mathcal T_{w-\widehat w}IYc\|_2
 \le e_{w,\infty}\|IYc\|_2
 \le e_{w,\infty}g\|c\|_2 .
 \tag{BGR.7}
$

所以第二个新自然目标为完整
$P_g=e_{w,\infty}g$。必须保存其整球，并与 (BGR.6) 两个
原 whole products 一起保存选择记录，再取整候选

$
 P_*=\min(P_g,P_{\rm HS},P_2).
 \tag{BGR.8}
$

系数误差仍覆盖完整2048模式、其后全部 infinite tail、
true source、moving phase、cohomological divisor 和 alias。
$F_H$ 仍是 DBRA 原96×2240 whole signed residual 上界；
其中193–2240不曾删除。BR.6、12 因而立即给第三个新目标

$
 \boxed{\quad
 \|R-\widehat R\|_{L^2_0\to\ell^2_{96}}
 \le e_R^{\rm Gram}:=\frac12F_H+\frac14P_*,
 \qquad R=E_{96}^{a*}\mathcal B^{-1}.
 \quad}
 \tag{BGR.9}
$

这是同一个 whole true inverse、同一个 whole row trial 的另一完整
bound。原 $e_R$ 与新 (BGR.9) 都须保留，选择只按完整 saved upper。
没有从旧上界相减或使用 Gram 的某个局部通过子矩阵；
也没有增加 $\sqrt{96}$。$a=2\mathcal H(0)$ 的整 ball、mean-zero
域和两 independent physical means 的外部义务继续完整保留。

## BGR3. 已启动 BNC7 的显式后继保全部旧目标

[BNC](R147-supplement-target-normalized-strict-parameter-column.md)
所需有限行常数实际上只是 $\|\widehat R\|=\|Z\|$ 的 upper：
对任意实 unit $c$，$r_c=Zc$ 满足

$
 \|r_c\|_2\le J_{\rm op},\qquad
 \|r_c'\|_2\le4M J_{\rm op},\qquad M=192 .
 \tag{BGR.10}
$

后者是**同一个完整有限多项式**的 Bernstein，未把单行误差当成
正交，也未将 true infinite inverse 限制为192模式。
BNC 的 compound proof、finite strip alias proof、disk-vector
contraction 分别只用 (BGR.10) 和 (BGR.5)，故全五费可准确改成

$
 \begin{aligned}
 E_{\rm row}&=e_R^{\rm chosen}B_HN_0,\\
 E_{\rm PDE}&=\sqrt{96}\,B_HD_b/\sqrt2,\\
 E_{\rm comp}&=4ME_HJ_{\rm op}N_0/\sqrt m,\\
 E_{\rm alias}&=2\sqrt{LM}J_{\rm op}N_0
    \exp(4L\sigma+4M(\sigma+G_0)-4N\sigma),\\
 E_{\rm disk}&=J_{\rm op}\sqrt{2\sum_{n=1}^M\rho_n^2},
 \end{aligned}
 \tag{BGR.11}
$

其中 $L=96,N=8192,\sigma=1/128$，
所有其他球、192个 complete disks、96个 exact signed contractions
和两 physical mean observations 全部仍是 BNC 的原完整对象。
$e_R^{\rm chosen}$ 是原 DBRA 与 (BGR.9) 的整候选选择。

由 BNC.14 的完整算子差分，
$\|E_{96}^{a*}\mathcal B^{-1}F_\nu-d\|_{\ell^2}$
不超过 (BGR.11) 五个**先各自保存**的完整费用之和。
这里新常数被明确称为 operator upper；
没有把 $g$ 冒称为原 $J_{\rm HS}$ 的改值。

原 BNC7 已由事件 `798a2fcde21a3dead70df87192a28f9ca2060472` 启动
唯一 run45941963989/1；保持原7目标与全部 frozen inputs，不能因本条
改变在跑入口。待它实际完整完成，其自然192 observations/配对不能再跑。
后继可复制其全部96 exact signed centers、五个原完整 fees、
全部父身份和两 mean；使用新的 $e_R^{\rm chosen}$ 从原完整
$B_H,N_0$ 形成新 row fee，再与原其他四费完整相加，得一个新
whole joint candidate。此做法不用重复 quadrature，也不从旧
total upper 中减掉 row upper。若要使用新的
$J_{\rm op}$ 于其它三费，须有原192整 disks 的完整可复原载体，
或保留旧整个候选；不能从只显示的原乘积 upper 除出其缺失输入。

## BGR4. 明确首次执行合同

纯模块
[fourfold_codazzi_target_B_complete_Gram_math.py](../scripts/fourfold_codazzi_target_B_complete_Gram_math.py)
只实现完整 Gram 的有符号构造、(BGR.4)、新的完整产品及 row bound，
以及完整 BNC7 之后的新 row fee/whole column bound。
它不导入数值库、不做 IO、不调用旧 DWT/BR/BNC producer。
实际 owner 需完整准入 DWTB9 的 whole actual/execution/manifest，
恢复原 entire2048 w、entire y/r 及其原 SHA；不得重新选择 trial。
新 target order 为 Gram operator upper、完整新 infinity product、
完整同一96行 error。全部原 product 候选与选择元数据也完整保留。

本条没有这些三个新目标的 actual；DWTB9 的旧结果和原 BNC7 的
first-run 身份不被改写。Gram 与 finite coordinate Θ 的实际逆也不
提供完整 physical forward column、高频 forcing、同一 mean/phase
Schur 或最终非线性族。
