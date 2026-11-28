# R149 DCP：原 Θ particular 的直接密度逆作用及完整异号 leakage

2026-11-28。**本文证明新算术目标的完整公式；尚无 DCP actual。**
配套 source 对 BFP 的同一个完整512-mode reference 计算一条新的
signed particular，不重算 IR96、ASR、UACT 或 BFP 的已成目标。
本证书的作用是替换 BFP.22 中由96条旧行统一估计产生的
$E_V B_{\rm model}+E_M B_x+E_{\rm pair}$；它不把低96误差用于
完整高频，也不将 finite coordinate inverse 当成 physical Schur。

## 1. 同一个原算子的全部顺序

沿 [DC](R149-supplement-same-sign-density-compression-and-finite-Theta-rows.md)、
[DT](R149-supplement-original-same-sign-source-Toeplitz-and-Theta-row-action.md)
与 [TQ](R149-supplement-original-Theta-restriction-and-joint-Schur-row-consumer.md)，
记 $\mathscr H=\dot H^{-1/2}_0$、$N=|\partial_x|$、$G=N^{-1}$，
物理周期 $\pi/2$，归一测度及物理频率 $4n$ 均保持。

$$
 S=U_\psi,\quad p=\psi^{-1}=\mathcal H\circ X_-^{-1},
 \quad C=\Pi_+S\Pi_++\Pi_-S\Pi_-,\quad
 D=\Pi_+S\Pi_-+\Pi_-S\Pi_+ .                 \tag{DCP.1}
$$

$\dagger$ 是 **$\mathscr H$ adjoint**，不是普通 $L^2$ adjoint。
准确地

$$
 C^\dagger=\Pi_+U_p\Pi_++\Pi_-U_p\Pi_-,\qquad
 D^\dagger=-(\Pi_+U_p\Pi_-+\Pi_-U_p\Pi_+),
 \qquad CC^\dagger-DD^\dagger=Id .             \tag{DCP.2}
$$

DC 的两条 Krein 恒等式已证明 $C$ 在整个 $\mathscr H$ 上有真
双侧逆，且 $\|C^{-1}\|\le1$；以下直接使用这份 onto 结论。
原完整坐标恒等式为

$$
 \Theta=E_{96}^*D_+^{-1}C^{-1}A\overline G,
 \quad A=Id-\mathcal T_\alpha I,
 \quad D_+=e^{-i\pi/4}\Pi_++e^{i\pi/4}\Pi_- .    \tag{DCP.3}
$$

若从原 adjoint rows 推导，正确的普通配对是
$\Theta x=B^*G C^{-1}A\overline Gx$，其中 $B=ND_+E_{96}$。
不能把 $G$ 移到 $C^{-1}$ 右边。

## 2. 已成实际导数界使异号双作用严格小

[SDI](R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md)
给同一个真 $p$ 的完整界

$$
 m={9749\over10000}<p'<{10251\over10000}=M.       \tag{DCP.4}
$$

对完整非mean $f$，密度换元给 $\|U_pf\|_2\le\sqrt M\|f\|_2$。
准确 primitive 恒等式为
$I U_pf=\Pi_0[(If)\circ p]$，其中 $\Pi_0=Id-\Pi$ 的 $L^2$
norm 为1。因此 $\|U_p\|_{\dot H^{-1}}\le1/\sqrt m$。
同一 Fourier Hilbert scale 的 constant-one 插值给

$$
 \|U_p\|_{\mathscr H}\le(M/m)^{1/4},\qquad
 \|S\|_{\mathscr H}\le(M/m)^{1/4}.              \tag{DCP.5}
$$

第二式对 $p^{-1}$ 用相同推导，其 derivative 范围为 $[1/M,1/m]$。
同号压缩 $\|C\|\le\|S\|$，而 (DCP.2) 给

$$
 \|D\|^2=\|DD^\dagger\|=\|CC^\dagger-Id\|
         =\|C\|^2-1\le\sqrt{M/m}-1<(4/25)^2.    \tag{DCP.6}
$$

最后是有理比较：
$9749\cdot641^2-10251\cdot625^2=1381994>0$。
所以对任何完整 $v\in\mathscr H$，

$$
 C^{-1}v-C^\dagger v=-C^{-1}DD^\dagger v,
 \qquad
 \boxed{\|C^{-1}v-C^\dagger v\|_{\mathscr H}
          \le {4\over25}\|D^\dagger v\|_{\mathscr H}.} \tag{DCP.7}
$$

这是同一真 inverse 上的实际有理系数，不是假设新的 finite
Neumann 门成立。负号在 signed identity 中保留；下述 leakage
只取其范数。

## 3. BFP 的同一完整 reference 和新 finite source

必须先准入 **全部成功 BFP19 actual/execution**，其完整512 trial、
8192 $f,G,G'$ points、true-phase target coordinates 和原2240 model
carrier 都必须按原全 SHA 恢复。仅必要 coefficient/grid carrier
恢复不调用任何 BFP residual、norm、quadrature、alias 或 pairing target。

令原 $\widehat X=Q_a\widehat x$，其完整真实 target coordinates
为 $\beta_n$，$1\le n\le512$，mean 为0。保持原
$u_n^b=\sqrt2\cos(4nx-2nb-\pi/4)$、$b=a+\Omega$ 和全部
true Cayley multipliers $\gamma_n$，于是

$$
 u=\overline G\widehat X,\qquad
 u_n={\gamma_n\beta_n\over\sqrt2}
             e^{-i(2nb+\pi/4)},\quad1\le n\le512.  \tag{DCP.8}
$$

这里的 $u_n$ 是 complex positive Fourier coefficients。
$\gamma_n=1$ 对 $n\le96$；97–512 从完整原2240 carrier 读取。
所有 true phase balls 原样保留，不用 midpoint reflection 替代。

用原全2048 signed $\widehat\alpha$，定义新的完整2560-mode source

$$
 \widehat v=\widehat A u,
 \quad \widehat A=Id-\mathcal T_{\widehat\alpha}I,
 \quad
 \widehat v_n=u_n-\sum_{\ell=1}^{512}
       \widehat\alpha_{n-\ell}{u_\ell\over4i\ell},
 \qquad1\le n\le2560.                            \tag{DCP.9}
$$

$u_n=0$ 对 $n>512$，$\widehat\alpha_0=0$，负频取 conjugates。
正输出中只含正输入 $\ell$；这是原 same-sign normalizer 的
**minus** forward 符号，不是 $A^*$ 的 plus。

保存全部2560 coefficients 后首次计算其完整 $V_0\ge\|\widehat v\|_2$、
$V_1\ge\|\widehat v'\|_2$，以及

$$
 W_v=\sum_{n=1}^{2560}{|\widehat v_n|\over4n},\quad
 I_{u,2}=\left(2\sum_{n=1}^{512}{|u_n|^2\over(4n)^2}\right)^{1/2},
 \quad W_u=\sum_{n=1}^{512}{|u_n|\over4n}.          \tag{DCP.10}
$$

这些是新的 particular 输入范数，不是 IR 的整96列范数重算。

## 4. 完整上下半 strip、8192 samples 与所有 aliases

同一个 $\widehat p=K_{48}\circ A_-$ 保留原129 terminal coefficients
和 real mean，以及全部48对 postcomposition coefficients。
设 $\sigma=1/256$。先从这些全系数计算

$$
 a_1\ge\|A_-'-1\|_{\mathcal A_\sigma},\quad
 w_A=\sigma(1+a_1),\quad
 k_1\ge\|K_{48}'-1\|_{\mathcal A_{w_A}},\quad
 \eta=a_1+(1+a_1)k_1 .                           \tag{DCP.11}
$$

第一条新 actual 目标必须验证 $\eta<1$，否则保存失败，不预报通过。
因为实轴上 lift 为实，垂直积分 $\widehat p'$ 给整个 strip 上

$$
 (1-\eta)y\le\Im\widehat p(x+iy)\le(1+\eta)y
                    \quad(0\le y\le\sigma).    \tag{DCP.12}
$$

所以新 positive primitive

$$
 h(x)=\sum_{n=1}^{2560}{\widehat v_n\over4in}
                         e^{4in\widehat p(x)}      \tag{DCP.13}
$$

在上半 strip 的 supremum 不超过 $W_v$；下半 strip 的全界为

$$
 M_-:=\sum_{n=1}^{2560}{|\widehat v_n|\over4n}
                      e^{4n\sigma(1+\eta)} .      \tag{DCP.14}
$$

原4096 grid 的全 SHA 对应偶数节点；新增4096奇数节点的原完整
compound values。全部8192 new primitive samples 使用有向 unit-disk
power residual，保存读回后才做完整 directed DFT。
对输出频率 $k$，包含**两条** alias rays 的准确上界为

$$
 a_k={M_-e^{-4\sigma(N+k)}+W_ve^{-4\sigma(N-k)}
                    \over1-e^{-4\sigma N}},
 \qquad N=8192 .                                  \tag{DCP.15}
$$

即使 $k<0$，positive aliases 的 $M_-$ 也不能删除。
把整个 alias disk 加到 DFT/$N$ 后乘 $4ik$，得完整 density
coefficient。保留正频1–96和负频−1至−2048。

负频 head 和未求整个 tail 的 $\mathscr H$ 界为

$$
 L_h^2=2\sum_{k=1}^{2048}{|4ik h_{-k}|^2\over4k},
 \quad
 L_t^2=8W_v^2\sum_{k>2048} k e^{-8\sigma k},
 \quad L_f=(L_h^2+L_t^2)^{1/2}.                   \tag{DCP.16}
$$

所有频率符号及 full infinite geometric moment 保留；不能把
negative-grid samples 的某个 maximum 当成 $L_f$。

## 5. 真 p 与 alpha 的独立完整费用

同一 IL actual 给整个 $\|p-\widehat p\|_{\mathcal A_\sigma}\le E_p$。
SDI.2–4 保留两完整 derivative sums 的准确分解
$A_-'=1+a$、$K_{48}'=1+k$，以及确定常数1和
$|\widehat p'-1|\le K_1A_1-1\le P_1-1$。
因此原 finite $P_1<1.024974$ 同时给
$2-P_1\le\widehat p'\le P_1$；此处没有从未知 norm 的 upper
减去未知 mean。连同 (DCP.4)，两个端点和它们的 real homotopy
都有同一 $m,M$。直接对 density 求变分，
所有项为 $\delta'v(p_t)+p_t'\delta v'(p_t)$。
完整换元、Cauchy first derivative 及
$\|L^2_0\hookrightarrow\mathscr H\|=1/2$ 给

$$
 e_p={E_p\over2\sqrt m}(V_0/\sigma+M V_1).       \tag{DCP.17}
$$

此界同时适用于 $C^\dagger$ 和 $D^\dagger$ 的整作用差；两个
sign blocks 输出正交，不再额外乘 $\sqrt2$。故真正完整 leakage
$L\le L_f+e_p$。

alpha 作用不能使用旧 ASR 巨大 scalar 之外的未经证明替代值。
这里消费 UACT 已保存的两个 **complete inverse-error products**

$$
 P_{E,\infty}\ge D_\infty H/2,\qquad
 P_{E,2}\ge D_2 S/3,
 \quad H=\epsilon_H,\quad
 S={51\over50}(\epsilon_0+10\epsilon_H/9).        \tag{DCP.18}
$$

$D_\infty,D_2$ 是原 UDR 全2048 mode 加整个 infinite tail 的确定
coefficient-error majorants，不是 actual unknown error 的 lower。
原保存球的有理比较 $H>.14$、$\epsilon_0>.435$ 给 $S>3/5$。
所以 (DCP.18) 的 **已知正配权常数** 允许完整新候选

$$
 P_{\alpha,\infty}={100\over7}P_{E,\infty}I_{u,2},\qquad
 P_{\alpha,2}=5\sqrt2 P_{E,2}W_u,
 \quad P_\alpha=\min(P_{\alpha,\infty},P_{\alpha,2}). \tag{DCP.19}
$$

两者都界 $\|\mathcal T_{\alpha-\widehat\alpha}Iu\|_2$；先保存
两个完整候选才选。其 $\mathscr H$ 费用是 $P_\alpha/2$。
没有从未知 norm 的 upper 反推出未知输入，也没有恢复缺失 modes。

## 6. 新96维 signed readout 和真正 ν 列

若 $(C^\dagger_{\widehat p}\widehat v)_j=q_j$ 是完整正 Fourier
coefficient，则 source/root readout准确为

$$
 d_j=\operatorname{Re}((1+i)q_j),\qquad1\le j\le96.
                                                               \tag{DCP.20}
$$

这是原 $D_+^{-1}$ 和 normalized root even basis；没有额外未知
reflection shift。每条整球取 exact dyadic center $\widehat d_j$，
96个完整 rounding/true-phase radii 的平方和给 $E_d$。
由 (DCP.7)、(DCP.17–19) 及
$\|E_{96}^*D_+^{-1}:\mathscr H\to\ell^2\|=\sqrt{384}$，

$$
 \boxed{\|\Theta\widehat X-\widehat d\|_2
  \le E_X:=\sqrt{384}\,[{4\over25}L+e_p+P_\alpha/2]+E_d.}
                                                               \tag{DCP.21}
$$

这是 full signed particular 的新认证。它既没有使用旧 $E_V
B_{\rm model}$，也没有重复 BFP 的96×2240 row pairing。

从 whole successful BFP19 复制原 $\delta_X\ge\|x_\nu-\widehat X\|_2$
与 $B_{\widehat\Theta}\ge\|\widehat\Theta\|$，同时保留原完整
global $E_\Theta$，即可给

$$
 \boxed{\|\Theta x_\nu-\widehat d\|_2
      \le E_X+(B_{\widehat\Theta}+E_\Theta)\delta_X.} \tag{DCP.22}
$$

现已完整成功的 [WMA](R149-supplement-actual-complete-weighted-model-Theta-receiver.md)
run46122573619/1 给同一对象的 complete global candidate<6.957962。
本 owner 强制全部 WMT14 actual、execution、manifest 及原 validator
准入，保留原850.945862…与新整候选后只改善 (DCP.22) 的此**唯一**
误差槽；不能使用未结束 run 的 prefix 或 low96 bound。
两独立 physical density means 从 BFP 原完整 signed conclusion 复制。
本 receiver 仍不声称已有完整 physical homogeneous96、高逆、
mean/phase/height finite border、regular defect 逆或最终 nonlinear 族。

## 7. 新实际目标与 no-replay 边界

[纯公式](../scripts/fourfold_codazzi_particular_density_Theta_math.py)
实现新的半 strip、finite source norms、两个 alpha products、
全 signed C-dagger action、opposite leakage head/tail、true-map fee
及两层96维 signed conclusion。全部来源必须先通过原 whole actual
validators；相同 IR grid、AS grid/alpha、DWT w 和 BFP trial 恢复
只核原全 SHA。IR trial矩阵与 DWT row trial不为本 receiver 所需，
不能顺手重建它们；旧 scientific reducers 全部禁用。
本条没有预先声称任何新 target 或 (DCP.22) 精度门已成功。
