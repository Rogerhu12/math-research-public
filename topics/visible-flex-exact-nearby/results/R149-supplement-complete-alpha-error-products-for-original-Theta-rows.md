# R149 TP：原 Theta 全96行的两个完整 alpha 误差乘积

**已证明。** 会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

本条接 [DT](R149-supplement-original-same-sign-source-Toeplitz-and-Theta-row-action.md)
及 [TM](R149-supplement-original-model-adjoint-on-complete-finite-Theta-rows.md)。
它使用同一完整 [AS](R149-supplement-original-source-alpha-signed-carrier-and-complete-errors.md)
的 $L^\infty$、$L^2$ 误差；不会把后一种误差直接代入前一种单位。
所有空间采用原周期 $\pi/2$ 的 normalized measure 和频率 $4n$。

## TP1. 同一完整有限列上的两个不同范数

令 $\widehat Z:\mathbb R^{96}\to L^2_0$ 是完整 IR trial，
每列的正频系数为 $z_{j,n}$，$1\le n\le M=192$；负频是其共轭。
置 $G=|D_x|^{-1}$，$F=G\widehat Z$，并定义

\[
 f_j^+(x)=\sum_{n=1}^{M}\frac{z_{j,n}}{4n}e^{4inx},
 \qquad f_j=f_j^++\overline{f_j^+}.
 \tag{TP.1}
\]

从同一完整 finite carrier 的全部系数可计算两个新上界

\[
 Z_G=\left(2\sum_{n=1}^{M}\sum_{j=1}^{96}
                    \frac{|z_{j,n}|^2}{(4n)^2}\right)^{1/2},
 \qquad
 B_Z=\sum_{n=1}^{M}\left(\sum_{j=1}^{96}
                    \frac{|z_{j,n}|^2}{(4n)^2}\right)^{1/2}.
 \tag{TP.2}
\]

第一个是整个 $F$ 的 Hilbert--Schmidt norm，故 $\|F\|\le Z_G$。
第二个由向量值三角不等式给

\[
 \sup_x\left(\sum_j|f_j^+(x)|^2\right)^{1/2}\le B_Z.
 \tag{TP.3}
\]

两者均包括96条完整列；没有将 IR approximate columns 当正交基。
它们是首次针对同一新 finite trial 的范数，不是旧 IR residual、
旧 SN error、旧 cohomological budget 或旧 transport norm 的重跑。

## TP2. 必须保持的同号投影

令 $\delta\alpha=\alpha-\widehat\alpha$，并取 AS 给出的两个完整数

\[
 \|\delta\alpha\|_\infty\le e_\infty,
 \qquad\|\delta\alpha\|_2\le e_2.
 \tag{TP.4}
\]

原 source operator 是

\[
 \mathcal T_{\delta\alpha}
 =\Pi_+M_{\delta\alpha}\Pi_+
   +\Pi_-M_{\delta\alpha}\Pi_-.
 \tag{TP.5}
\]

这是两个同号 block，而不是 $P M_{\delta\alpha}P$。两个输出正交。
因此对所有单位向量 $c\in\mathbb R^{96}$，完整 $L^\infty$ 候选给

\[
 \|\mathcal T_{\delta\alpha}Fc\|_2
 \le e_\infty\|Fc\|_2\le e_\infty Z_G.
 \tag{TP.6}
\]

另一候选先用每一个输出投影的 $L^2$ contraction，再用 TP.3：

\[
 \begin{aligned}
 \|\mathcal T_{\delta\alpha}Fc\|_2^2
 &\le \|\delta\alpha\,(Fc)^+\|_2^2
        +\|\delta\alpha\,(Fc)^-\|_2^2\\
 &\le e_2^2\big(\|(Fc)^+\|_\infty^2
                   +\|(Fc)^-\|_\infty^2\big)
 \le 2e_2^2B_Z^2.
 \end{aligned}
 \tag{TP.7}
\]

实 $c$ 的两个输入互为共轭；分别使用 TP.3 也给同一界。
于是以下两个完整候选界定同一 joint operator：

\[
 P_\infty=e_\infty Z_G,
 \qquad P_2=\sqrt2\,e_2B_Z,
 \qquad P_\alpha=\min(P_\infty,P_2).
 \tag{TP.8}
\]

实际计算先保存并读回两个完整有向上界，再选择整个候选。
不能逐 mode 混选不相容的 remainder，也不在最后再乘 $\sqrt{96}$。

## TP3. 新 finite alpha carrier 的完整 A norm

AS trial 的 mean 精确为零，负频与正频共轭，正频为
$\widehat\alpha_n$，$1\le n\le K=2048$。因而

\[
 A_{trial}=2\sum_{n=1}^{K}|\widehat\alpha_n|,
 \qquad A_0=A_{trial}+e_\infty\ge\|\alpha\|_\infty,
 \qquad K_A=1+A_0/4.
 \tag{TP.9}
\]

这是同一原 $\alpha=v_i-w$ 的一个新完整上界；未用两个旧上界相减，
未假定 trial 自身满足精确 $R_b$ parity。真实相位误差已经在完整
AS error 中支付，真实 $\alpha$ 的 source parity 仍是 WBN 的原恒等式。
旧 $v_i,w$ 的 successful budgets 保持原记录且不重复计算。

## TP4. 接原 VQ 与真正 Theta

IR 的两个完整 joint residual 记作 $\epsilon_H,\epsilon_0$，分别在
$\dot H^{-1/2}_0$ 和 $L^2_0$；它们包括全部 Fourier head、aliases、
无限 tail 和真实 map error。固定其原 finite trial，不另造或重跑 IR。
在源行中使用 $\widehat A^*=Id+I\mathcal T_{\widehat\alpha}$，则

\[
 \|V_Q-\widehat V_Q:L^2_0\to\mathbb R^{96}\|
 \le K_A\epsilon_H/2+P_\alpha/4.
 \tag{TP.10}
\]

其中 $I$ 的 mean-zero $L^2$ 范数为 $1/4$。
完整原 model 满足 TM 的
$K_G=\|\overline G:Y_a^0\to X_b^{-1}\|\le512$。
[SDI](R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md)
给同一真实 inverse-density map 的 one-loss bootstrap；再用
$\|I:L^2_0\to H^1_0\|=\sqrt{17}/4<21/20$，得

\[
 E_{DT}:=K_G\left[
     \frac{1071}{1000}K_A
               (\epsilon_0+\tfrac{10}{9}\epsilon_H)
          +\frac{21}{20}P_\alpha\right].
 \tag{TP.11}
\]

将同一次完整 finite DT 行作用到原 $\overline G$，在真实 target
orthonormal basis $v_n^a$ 中保留全部 $96\times2240$ coefficients。
若 TM.8 的整个 model-action rounding error 为 $E_{model}$，则

\[
 \boxed{\|\Theta-\widehat\Theta:Y_a^0\to\mathbb R^{96}\|
               \le E_{DT}+E_{model}.}
 \tag{TP.12}
\]

这是完整原 $\Theta=V_Q\overline G$ 的误差，不是仅 finite-input
或 C-only 的替代算子。$a,b,\Omega,\mu$ 均保持原定义和整区间，
low model reference 保持1，两条独立 physical mean slots 未被消去。
本条没有断言 TP.12 已小到足以通过一个实际 finite matching gate。
高/低 cross、真实 PDE finite columns、nu/phase、physical means 和
full Schur 仍由各自实际有向矩阵和整体准入处理。

## TP5. 实际载体恢复与新目标边界

后继首次 owner 只有在整 IR/AS actual 及其 execution/manifest 到齐，
SDI 的四个完整 IL balls 与原 CYA full-scope 实际结论准入后才能运行。
IR finite matrix 必须在其原 immutable runtime/Haswell 下重新物化并
匹配原完整 grid 与 trial SHA；AS 的原 SN endpoint、raw trial、完整
grid 和全2048 trial coefficients 分别必须匹配首次 actual 的全 SHA。
恢复只执行必要 finite-carrier 公式，禁用旧 residual、norm、tail、
cohomological budget 和 IL 科学入口。两种原 runtime 以独立进程保留。

新 scientific targets 仅为 TP.2、TP.9 中新 finite-carrier norms、
TP.8 的两个完整产品，以及 DT/TM 的首次完整 signed row action 和
TP.10--12 的新组合。每条整行先存盘读回再参与 norm；完整 private
carriers 仅保 SHA/长度/shape 和 recipe，所有小的 whole conclusions
及实际失败均公开，不上传可重建数组。
