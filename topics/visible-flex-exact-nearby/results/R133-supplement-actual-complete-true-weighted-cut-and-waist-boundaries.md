# R133 supplement: actual complete true-weighted cut and waist boundaries

2026-11-14, visible-exact-astra-0df9.

**已证明（同一明确有限 193 态、完整 97 条低边界行）：**
公开 Actions [43594139132](https://github.com/Rogerhu12/math-research-public/actions/runs/43594139132)
的 prepare 子进程已真实完成十项检查，退出码 0。
本结论给实际加权坐标中的两端不等式，供全部连续 projector 的 signed Green 消费。
它不以端点门替代全区间 Green、未知无限高输入或真正 PDE 响应。

## 1. 原件与真实范围

原生文件为
[complete-true-weighted-boundaries.json.gz](../notes/regular_cut_validator_ci/run-43594139132-1-projectors-prepare/native/complete-true-weighted-boundaries.json.gz)，
SHA256 为
`56db8a3498494bf48de14b50418010053bb6058c722c41993c894c463786dc25`。
原完整 prepare artifact 是
`visible-exact-cut-projector-prepared-43594139132-1`，id 14113777182。
原 artifact 内最终过程 SHA256 为
`e8f975932aedf150d1a2beaaae6a05650f7983f8844b9ae488343d953a1a9184`；
仓库过程还会追加真实发布记录，不因此改写原 artifact 身份。

数学源
[true_weighted_boundaries.py](../scripts/fourfold_codazzi_regular_cut_true_weighted_boundaries.py)
SHA256 为
`32bea27df55fa79eeb29355da3f05a37d0e2eb00bf2a1a8954e193fe9b5429d9`；
公开完整驱动 SHA256 为
`3d4628235a6d48046ac2e17af75cf70ea7bcadf6d5e6856a327426faebfa84fa`。
十门均为实际通过；数学用时 0.425246019 秒，子进程墙时 5.000590607 秒。
原 candidate、连续修复定义、193 态和原全部行的身份均逐项保留。
参数仍为原 $\eta_0,\nu_0$、显式偏移 $\delta=0$。

准确腰与切口权重分别是
$$
 \rho_0=\frac{4165783535396773}{4503599627370496},\qquad
 \rho_R=\frac{3563799261220073}{9007199254740992}.
$$
使用 $R=\operatorname{diag}(I_{96},\rho I_{97})$。
完整非零模实 Fourier 范数归一化和独立 even mean 保持原约定。

## 2. 腰端完整证明

设 $P$ 为实际完整 193×96 保存 frame 的正交投影，$U$ 是腰端的
96 条 $u$ 行，$UU^*=I$。令 $S:\mathbb R^{96}\to\operatorname{ran}P$
是 $U$ 在该子空间上的逆，故 $US=I$、$SUP=P$。
对 $p=\|Py\|$、$q=\|(I-P)y\|$、$Uy=g_0$，
$$
 Py=Sg_0-SU(I-P)y.
$$
又
$$
 [SU(I-P)][SU(I-P)]^*=SS^*-P.
$$
因为 $S$ 的像正是 $\operatorname{ran}P$，得到准确关系
$$
 L_0=\|S\|,\qquad D_0^2=L_0^2-1,\qquad
 p\le D_0q+L_0\|g_0\|.
$$
实际计算保完整 $S^*S$，以有理 dyadic 近似本征基的 Gram 与
Gershgorin 余量给有向界，未用逐列最大值冒充算子范数。
原 frame 的 Gram 最小本征值大于
$0.9999999999999982$；完整腰限制最小奇异值大于
$0.0009834978065360445$。由实际 native 向外取整，
$$
 \boxed{L_0<1016.779086,\qquad D_0<1016.778594.}
$$
这里的保存腰 frame 位于虚拟 $0^-$。
最后一个真实 polynomial frame 在 $0^+$ 的投影跳必须先按
sec/tan 接口消费，之后才能使用此式与 $D_0\varrho(0^-)$ 的闭合门。
不能把两侧 frame 直接认同。

## 3. 切口完整 97 行证明

在同一加权坐标中，完整边界矩阵为
$$
 B_R=\begin{pmatrix}I&J/\rho_R\\0&M/\rho_R\end{pmatrix}.
$$
其全部 97 行（包括独立 mean 行）保留。
有限帽核原误差在 even 列上应除以 $\rho_R$，不能沿用无权费用。

令 $r$ 是 $\|B_RP\|$ 的完整上界；它由全 frame Gram、实际行作用和
$\epsilon\|Q_{\rm even}\|/\rho_R$ 组成。
原边界 mean 系数为 $m_0\ne0$，完整有限右逆可用
$$
 \ell=\left\|\begin{pmatrix}1&j_0/m_0\\0&\rho_R/m_0\end{pmatrix}\right\|
$$
控制。这里 $j_0$ 支配相应完整 mean 列，所有范数是所列实 Hilbert 规范。
于是 $B_RB_R^*\ge\ell^{-2}I$。
写 $Q=I-P$，由正交分解准确得到
$$
 (B_RQ)(B_RQ)^*
   =B_RB_R^*-(B_RP)(B_RP)^*
   \ge(\ell^{-2}-r^2)I.
$$
完整补空间与边界空间同为 97 维。若
$\sigma^2=\ell^{-2}-r^2>0$，则其限制可逆，
$$
 q(R)\le D_Lp(R)+L_R\|g_R\|,\qquad
 L_R=\sigma^{-1},\quad D_L=L_Rr.
$$
这证明了全部低行端口，不删除 mean，也不只检验 96 个 regular 列。

实际 native 给 cut frame Gram 最小本征值
$>0.9999999999999993$，
$\|Q_{\rm even}\|<0.707929710$，
完整加权核误差 $r<0.000886252275250$，
$|m_0|>0.245303698650$，
补空间最小奇异值 $>0.245287181632$。
因此可取
$$
 \boxed{L_R<4.076853888,\qquad D_L<0.003613121034.}
$$
辅助完整右逆范数为 $4.076827276857\ldots$。
原有向 low97 误差 $<0.0012518930394365$；
已付高输出费 $<0.001196826708143$，
该高输出费并非未知高输入反馈的逆界。

## 4. 与全连续格的准确连接

切口与腰保存数组 SHA256 分别为
`067ab9dfb07dc3d64733e15d70133dd6888297cedc586270c1f2d9fc9a682363`
和
`4720eff05a298b9d984615ebbe0e51dbed4b5e819deae8f796397d01733977b0`。
全部 5970 格消费者必须核对同一锚点链、所有末端跳及上述 native 身份。

物理源到加权态逐片付 $\max(1,\rho)$，加权态返回物理范数逐片付
$\max(1,\rho^{-1})$，径向算子另保 $R'R^{-1}$。
本结论只支付真实两端，尚须实际全区间 signed Riccati/正 Green、
原分布残差与全部 trial 跳、独立边界和帽源、未知 high 输入反馈、
原 ac1 到修复/显式族/真正 PDE 背景的费用。
不得把这里的 $L_R,D_L$ 单独称为完整响应或 $\nu$-Schur 证书。
