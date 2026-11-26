# R149 补篇：原 density 同号压缩的收缩逆及真正 finite Θ 行

2026-11-27，visible-exact-astra-fb31ed6-20261127 / trial_restore。

**已证明新的完整算子结论。** WIT 的同一 $C=WS$ 在原
$\dot H^{-1/2}_0$ 上双侧可逆，且 $\|C^{-1}\|\le1$；它的
Hilbert adjoint 恰是逆 density map 的同号压缩。因而原 $V_Q$ 的
全部 $L^2$ 行可由一个下界为1的正定方程及**全频**残差认证，
不必经过旧巨大 $W^{-1}$ norm。下面给出原 $\Theta=V_Q\overline G$
在有资格有限输入上的准确配对、联合误差和可恢复的原 one-leg 载体。
没有把 $V_Q$ 的 $L^2$ 行证书提升成整个 $\Theta:L^2\to\mathbb R^{96}$
证书，也没有缩掉 CG 的巨大普通 Fourier 有限补。

## DC1. 固定的算子、内积和两种 mean

所有量固定到 W/RRF 的同一 selected $(\delta_*,\mathcal H)$，原
$Q_{\delta_*}$、$\eta_0$ 和物理频率 $4j$。圈长 $\ell=\pi/2$，
积分为 $d\phi/\ell$。沿
[WIT.1–8](R133-supplement-positive-density-intertwiner-for-the-true-reflected-input.md)，
在完整非mean载体定义
\[
 S=U_\psi=U_{\mathcal H^{-1}}U_{X_-},\qquad
 \psi=X_-\circ\mathcal H^{-1},\qquad
 U_\psi f=\psi'(f\circ\psi),
\]
\[
 Z=i\Pi_+-i\Pi_-,\quad Z^2=-Id,\quad
 N=|D_\phi|,\quad I=\partial_\phi^{-1}P,\quad
 G=IZ=N^{-1},\quad P=Id-\Pi,
\]
\[
 \mathscr H=\dot H^{-1/2}_0,\qquad
 (f,g)_{\mathscr H}=\langle f,Gg\rangle_{L^2},\qquad
 \|f\|_{\mathscr H}^2=\sum_{j\ne0}\frac{|\widehat f_j|^2}{4|j|}.
 \tag{DC.1}
\]
本文 $\dagger$ **只**指此 $\mathscr H$ 的 adjoint，$*$ 指普通
$L^2$ adjoint。这里 $S$ 是完整正 density composition，$Z$ 才是
sign；不能互换这两个符号。$S^{\pm1}$ 在 $\mathscr H$ 上的资格由
原同一两-window inverse 插值得到，且在共同分布 core 上为真双逆。

WIT.7 的精确 primitive 配对及 onto 性给
\[
 S^\dagger ZS=Z,\qquad SZS^\dagger=Z.
 \tag{DC.2}
\]
第二式不是另加的 unitary 假设：由第一式及 $S$ 的真双逆，
$S^{-1}=-ZS^\dagger Z$，再直接相乘即得。$S$ 一般不在
$L^2$ 或 $\mathscr H$ 中 unitary。

原两 physical density means 没有放入 $\mathscr H$。如需辅助 mean
extension，只定义 $\widehat C=\Pi+CP$，其逆为
$\Pi+C^{-1}P$。这不能替换 WIT.28 的完整 sign mean rank，
也不能删除任何独立 physical mean 或 parameter/phase 方程。

## DC2. 两条 Krein 恒等式同时给出 lower 与 onto

取 WIT.25 的原算子及其 opposite-sign 部分
\[
 C=WS=\tfrac12(S-ZSZ)
      =\Pi_+S\Pi_++\Pi_-S\Pi_-,\qquad
 D=\tfrac12(S+ZSZ)
      =\Pi_+S\Pi_-+\Pi_-S\Pi_+ .
 \tag{DC.3}
\]
故 $CZ=ZC$，$DZ=-ZD$。对 (DC.2) 分别取同号、异号块，准确得到
\[
 \boxed{\ C^\dagger C-D^\dagger D=Id,\qquad
          CC^\dagger-DD^\dagger=Id.\ }
 \tag{DC.4}
\]
第一式给 $\|Cf\|_{\mathscr H}\ge\|f\|_{\mathscr H}$；第二式
给 $\|C^\dagger g\|_{\mathscr H}\ge\|g\|_{\mathscr H}$。
因此 $C$ 有闭值域，而其值域的正交补 $\ker C^\dagger$ 为零。
闭且稠密即整个 $\mathscr H$，所以
\[
 \boxed{\ C^{-1}\text{ 为真双侧逆},\qquad
          \|C^{-1}\|_{\mathscr H\to\mathscr H}\le1.\ }
 \tag{DC.5}
\]
同样 $(C^\dagger)^{-1}$ 存在且 norm 不超过1。这里两条恒等式
缺一不可，不能由 injectivity 单独宣称 onto。

压缩 $S^{-1}=-ZS^\dagger Z$ 的同号块，还得到可直接求值的公式
\[
 \boxed{\ C^\dagger
       =\tfrac12(S^{-1}-ZS^{-1}Z)
       =\Pi_+U_{\psi^{-1}}\Pi_+
         +\Pi_-U_{\psi^{-1}}\Pi_-.\ }
 \tag{DC.6}
\]
因此 $C^\dagger$ 的一次作用只需同一真实 inverse lift
$\psi^{-1}=\mathcal H\circ X_-^{-1}$，不需对未知 inverse matrix
取未经认证的有限截断。

RRF/WIT 的 $CR_*=R_bC$、$CZ=ZC$ 原样保留，$b=a+\Omega$。
由双逆可得相应 inverse 等式，故原实 Fourier conjugacy 与准确
reflected 子类也双向保持；这不是把整个非mean圈投影成一个不相容的
even/odd 空间。原 $D_+$ 及 transported cutoff 仍在下一节的原位置。

## DC3. 下界1的全空间正定解与残差

由 (DC.4)，
\[
 T=CC^\dagger=Id+DD^\dagger\succeq Id,\qquad
 C^{-1}=C^\dagger T^{-1}.
 \tag{DC.7}
\]
给 $y\in\mathscr H$，任意明确 trial $v$ 的完整残差为
$r=y-(Id+DD^\dagger)v$。取 $x_v=C^\dagger v$，则
\[
 \|C^{-1}y-x_v\|_{\mathscr H}
   =\|C^{-1}r\|_{\mathscr H}\le\|r\|_{\mathscr H}.
 \tag{DC.8}
\]
没有额外 $\|C^\dagger\|$。若实际存的是有限多项式
$\widehat x_v$，还须支付完整
$\|\widehat x_v-C^\dagger v\|_{\mathscr H}$。

有限 Galerkin 方程可用来选 $v$：其矩阵在诱导 $\mathscr H$ 内积
下仍有 lower1。但 $P_Mr=0$ 不使完整 $r$ 为零；
$(Id-P_M)DD^\dagger v$ 及所有 compound/DFT 尾仍在 (DC.8)。
对 adjoint inverse 可交换 $C,C^\dagger$，使用
$C^\dagger C=Id+D^\dagger D$。也可直接选择有限 $z$ 并认证
$C^\dagger z-y$ 的完整 norm；(DC.5) 同样给系数1的误差。

## DC4. 原 $V_Q$ 与 $\Theta$ 的全部顺序

沿 [WGB.5–7、18](R133-supplement-exact-graph-parameterization-and-physical-finite-border.md)
和 [CG.19](R149-supplement-positive-feedback-in-the-complete-graph-high-block.md)，
\[
 A=Id-\mathcal T_\alpha I,\quad
 \alpha=v_i-w,\quad
 D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_-,
\]
\[
 \mathcal U=A^{-1}CD_+,\quad
 V_Q=E_{96}^*D_+^{-1}C^{-1}A,\qquad
 \Theta=V_Q\overline G.
 \tag{DC.9}
\]
$E_{96}$ 是原 natural reflected space 的 $L^2$ 归一实基注入；
其第 $j$ 列记 $e_j$，$Ne_j=4j e_j$。$D_+$ 与 $N,G$ 交换，
在每个所用窗中 unitary。它不能从原 reflected source 定义中删去。
令
\[
 b_j=ND_+e_j,\qquad z_j=(C^\dagger)^{-1}b_j,
 \qquad r_j=A^*Gz_j .
 \tag{DC.10}
\]
则对原适当 core，并由有界延拓到 $L^2$，
\[
 (V_Qf)_j=(z_j,Af)_{\mathscr H}
          =\langle r_j,f\rangle_{L^2}.
 \tag{DC.11}
\]
由于 $\mathcal T_\alpha$ 在 $L^2$ 自伴、$I^*=-I$，此处准确
$A^*=Id+I\mathcal T_\alpha$。不是把 $A^{-1}$ 或
$A^\dagger$ 放到 (DC.10) 左端。

WBP 的原完整 $L^2$ bound 为
$K_{A,0}=1+A_0/4$，$A_0\ge\|\alpha\|_\infty$。物理最低频率4给
\[
 \|L^2_0\hookrightarrow\mathscr H\|\le\tfrac12,
 \quad \|G:\mathscr H\to L^2_0\|\le\tfrac12,
 \quad \|E_{96}^*:\mathscr H\to\ell^2\|\le\sqrt{384}.
\]
所以新的完整行算子结论为
\[
 \boxed{\ \|V_Q:L^2\to\mathbb R^{96}\|
       \le\sqrt{96}\,K_{A,0},\qquad
       \|r_j\|_2\le\sqrt j\,K_{A,0}.\ }
 \tag{DC.12}
\]
这是对原 $V_Q$，并非另造一个 ordinary low projector。

若有限 trial $\widehat z_j$ 的**全频**残差列为
\[
 R e_j=C^\dagger\widehat z_j-b_j,\qquad
 \|R:\ell^2_{96}\to\mathscr H\|\le\varepsilon_R,
\]
则用 $\widehat r_j=A^*G\widehat z_j$ 得
\[
 \boxed{\ \|V_Q-\widehat V_Q:L^2\to\ell^2_{96}\|
       \le\tfrac12 K_{A,0}\varepsilon_R.\ }
 \tag{DC.13}
\]
例如可用全部96残差列的 Hilbert–Schmidt norm，但若已认证联合
Gram/operator norm，(DC.13) 不另乘 $\sqrt{96}$。$A$ 系数的
有符号 trial 若尚有误差，须按 (DC.11) 另付它的完整作用误差，
不能从旧 $A_0$ norm 反推 signed coefficients。

对一个真正给定的有限输入算子 $F:\mathbb R^m\to Y_a^0$，
**若已证明** $\overline GF:\mathbb R^m\to L^2$，可计算完整
\[
 (\Theta F)_{jk}=(z_j,A\overline GF e_k)_{\mathscr H},\qquad
 \|\Theta F-\widehat V_Q\overline GF\|
 \le\tfrac12K_{A,0}\varepsilon_R
       \|\overline GF\|_{\ell^2\to L^2}.
 \tag{DC.14}
\]
若另用近似 $\widehat F$，则准确误差上界为
\[
 \tfrac12K_{A,0}\varepsilon_R\|\overline G\widehat F\|
 +\sqrt{96}K_{A,0}\|\overline G(F-\widehat F)\|,
\]
两个 norm 都是完整 $\ell^2\to L^2$ norm。普通有限 Fourier $F$
可用原逐频 $\overline G$ 精确处理；
有无限 high 尾的 physical column 必须先支付这个尾的资格和 norm。

原 $\overline G:L^2\to H^{-1}$ 有 one loss，故 (DC.13) 不允许
直接对任意 $f\in L^2$ 在右边插入 $\overline Gf$。要证明整个
$\Theta:L^2\to\mathbb R^{96}$ 的新 row approximation，需完整
$H^1$ dual row error，或单独的 qualified high-tail estimate。
CG/WGB 的既有全 $\Theta$ bound 及全部 high cross 继续有效。

## DC5. 认证 $C^\dagger z$ 时保全无限 compound 尾

写 $p=\psi^{-1}$。对任意非mean有限 Fourier 多项式 $f$，有精确式
\[
 U_pf=\partial_x\{(If)\circ p\}.
 \tag{DC.15}
\]
因此可先算 primitive 的 compound Fourier 系数，再乘 $i4k$。
它省去单独差分近似 $p'$，并准确保留 density Jacobian；输出mean
由导数恒等为零。按 (DC.6) 取所需同号输出，未取的 opposite-sign
块不冒充整个 residual。

设一个完整周期解析 primitive $a$ 在物理 strip $\sigma>0$ 的
supremum 不超过 $M$。$q=e^{-8\sigma}$，则对任何整数 $K\ge0$，
\[
 \|\partial_x P_{|k|>K}a\|_{\mathscr H}^2
 \le8M^2\sum_{k>K}kq^k
 =8M^2\frac{q^{K+1}((K+1)-Kq)}{(1-q)^2}.
 \tag{DC.16}
\]
这里两 Fourier signs 与频率4都已出现。相同公式取 $K=0$ 支付
一个完整 analytic model difference，不能仅因输出矩阵是 finite
就省掉它。

用 $L>2K$ 个准确 sample 的 DFT 时，输出 $|k|\le K$ 的完整 alias
上界可取
\[
 M\frac{e^{-4\sigma(L-|k|)}+e^{-4\sigma(L+|k|)}}
          {1-e^{-4\sigma L}}.
 \tag{DC.17}
\]
全部 head coefficient balls、(DC.16) tail、(DC.17) aliases，以及
true $p$ 对 trial $\widehat p$ 的误差须共同进入 $R$。具体地若
$\|p-\widehat p\|_{\infty,\sigma}\le E_p$，每条复线段仍在声明的
image strip，且 $\|f\|$ 在该像中不超过 $M_f$，则
\[
 \|(If)\circ p-(If)\circ\widehat p\|_{\infty,\sigma}
 \le E_pM_f .
 \tag{DC.18}
\]
将此数代入 (DC.16) 的 $K=0$ 即给完整 density error。
未知 lift 的 constant 与 finite phase 的 real mean 都保留；周期
primitive 的常数不影响 (DC.15)，但不能先改变 density map 的 lift。

## DC6. 已定位且实际读取的原 one-leg 输入

以下历史原件均可从提交
`46f127c7153f5393dcd2a00f42d4c1d3662c294d` 恢复（complete169 也可从
`d9aa8cf519115f44283bf15d9a4426ff3a31b3a9` 恢复）。已作整件 bytes、
SHA、JSON 和 source/selected identity 检查；没有运行旧 producer。

| 完整原件 | bytes | SHA256 |
|---|---:|---|
| `notes/phase_transport_complete_ci/run-43580721166-1/complete-169-cover.json.gz` | 143466 | `d2e9f2479dc677694c8e84945ac1787f6a5366446d4fd30eac5b3c3008ecc1ae` |
| `notes/phase_small_consumers_ci/run-43586895661-1/consumers/wiener.json.gz` | 109293 | `33db2c82010e619300b7c6df0b088a047cc6220de09de59ab56fb477ae4f04b4` |
| 同目录 `post48.json.gz` | 20486 | `a44d6a6b2d0bad07d60e323142fd266b8dd91a645afa9d306fe22c8794a84f60` |
| 同目录 `R31.json.gz` | 3560 | `d6e59dfa851fb7d385f6281389221408cc132f90be8c2b1577fdd2be9a348d61` |
| `notes/phase_strip_refinement_ci/run-43588332723-1/consumers/R31-strip-refinement.json.gz` | 3356 | `dfb2a174a010d399775240b2bd07a0f547dfee5fc137e12141be9fd8a46e3854` |

路径以本课题为根。原 publication/process/manifest、全 source closure、
完整 W/R31 gates 和它们的 true selected identity仍须由实际消费者
整件准入，不用本表代替资格。

complete169 与 Wiener 原件都含同一 `exact_terminal_phase_state`，
两个完整129系数实 Fourier 多项式及各自真正 phase mean。它们是
原 degree64 的整个 terminal state，不需要重积分169个 germs。
令 $A_-^0(x)$ 是第二个完整 lift（identity 加该 Fourier polynomial）。
由原 transport source 的 field 顺序 $-d+\sigma\eta q$ 和
[PF.27](R133-supplement-pointwise-root-finite-part-and-complete-true-ray-first-coefficient.md)，
它近似的是
\[
 H_{\rm fin}\circ S_-^{0}
     =H_{\rm fin}\circ(X_-^{0})^{-1},
 \qquad S_-(0)=Id.
\]
原48-mode postcomposition 是完整 $K_{48}$，故明确的新比较 lift 为
\[
 \boxed{\ \widehat p=K_{48}\circ A_-^0,\qquad
 p=\mathcal H\circ(X_-^{\delta_*})^{-1}.\ }
 \tag{DC.19}
\]
$\widehat p$ 是一个确定的 analytic compound，不被截回64或48；
所需的 Fourier 截断及所有余项按 DC5 支付。

old post48 中完整的 `multiplied_complete_true_transport_residual`
和 `multiplied_genuine_Wiener_root_sliver` 已分别含两支的全部非负
费用；它们也支配这条指定单支，而不是对两个有符号 terminal lifts
作未付相减。原 source 中 $K'$ 的完整 argument-strip 费用保持。
Wiener 的原共同 input strip 为 $1/50$。

selected 转移另付三项。记原 W 的
$E_H=\|\mathcal H-G_{\rm fin}\|_{A_{1/128}}$、
$G_1=\|G_{\rm fin}'\|_{A_{1/128}}$、$d_*\ge|\delta_*|$，其中
$G_{\rm fin}=K_{48}\circ H_{\rm fin}$。原 R31 的 complete
one-leg Lipschitz record 为 $L_\delta<1/16$，其
`complete_return_first_parameter` 为正向 majorant $Y<1$。
原 source 的准确构造是
\[
 Y=e^{2L_\delta}\,2(D_1+C_1),
\]
其中 $D_1,C_1$ 是同整条原系数的完整一阶参数积分。因此它同时
支配任一支、任一方向的 $e^{L_\delta}(D_1+C_1)$，不是从实际
return derivative 的小值倒推单支 derivative。

取物理 strip $\sigma=1/256$。真实各 real-parameter 单支 flow
满足 $|\operatorname{Im}S_-(x+iy)|\le e^{L_\delta}|y|$；由
$e^{L_\delta}<16/15$ 得像 strip 小于 $1/240<1/128$。
故在这整个 strip 有完整的新比较式
\[
 \boxed{\ E_p\le E_H+G_1Yd_*+
     E_{K,\mathrm{transport}}+E_{K,\mathrm{root}}.\ }
 \tag{DC.20}
\]
每个旧量都读取完整原球上端，尤其 $E_H$ 取 W 原整件字段；不能由
RW 每行 epsilon 或 JC 最后一个球反解。原 root、true parameter
和 real lift 全保留。此公式的新标量读取尚未实际执行。

另一个已经严格成立的真实实轴资格是：原 W/AC 的
$31/32\le\mathcal H'\le33/32$、$|\mathcal H''|<4$，同 R31
单支 $e^{-L_\delta}\le S_-'\le e^{L_\delta}$，给
\[
 \frac{465}{512}<p'<\frac{11}{10}.
 \tag{DC.21}
\]
R31 的 `complete_return_second_angular` 为完整正向 majorant
$e^{4L_\delta}2D_2<1$，同样支配单支二导；所以
\[
 |p''|<4(16/15)^2+33/32<6.
 \tag{DC.22}
\]
这些是对完整原保存球的有理后果和原正向构造的解析应用，没有新跑
旧 ray、Jacobian、norm 或 KAM 目标。若仅要定义 (DC.19) 的 trial，
不需要一个未保存的 full-flow array；原两 terminal lifts 已足够。

## DC7. 可执行的下一个数学对象及尚未付的接口

下一新对象是 (DC.19) 的 compound inverse lift、(DC.20) 的完整
strip error，和作用于明确96个 trial 的 (DC.6) 全频残差。
所需旧 terminal/K/H/W/R31 原件已经具体定位；新残差只做一维
compound、Fourier head、DFT aliases 和 infinite tails，不重旧 flow。
附带 [pure formulas](../scripts/fourfold_codazzi_density_compression_theta_math.py)
提供这些标量、全部频率4的 Hilbert tail、有限配对及联合误差；它不
作 IO、不导入数值库、不凭传入 norm 字典宣布实际准入。

在算真正 $V_Q$ signed rows 时，还需原 $\alpha=v_i-w$ 的完整
有符号 coefficient carrier 或一个付过完整误差的明确 trial。
WBP/NW 的 scalar norm 本身不确定这些 signed values。若尚未取得，
先输出 $E_{96}^*D_+^{-1}C^{-1}$ 的完整行和残差，再消费真正的 $A$；
不得给前者改名 $V_Q$。完整 $\Theta$ 后面的 one-loss 义务按 DC4
保持。

原 SC96 physical columns、两 physical means、真正 $\nu$/phase、
CG 的 coupled infinite remainder 和高低交叉继续是原对象。
本篇使其中一个原有限坐标接口成为有明确低条件数和原载体的计算，
没有证明整个 incoming inverse、完整 Schur、非线性解或课题完成。
