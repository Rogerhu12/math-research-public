# 已证明：实际作用量一阶矩的正权接收及方向 cubic 的尖一侧费用

沿共同漂移 $L=\partial_\rho+d\partial_\phi$ 考察 $\rho Ly+a y=c f$，$a,c>0$。这包括真实 $A_1=LA$，此时 $a=5/2,c=3/2$，$f=B_\rho x+B(bv_\phi-d_\phi x)$；亦包括径向 $k_1$，此时 $d=0,a=2,c=1,f=-K_{rr}$。用上标 $(m)$ 表示真实归一化角导 $\partial_\phi^m/m!$。取原物理格 $h>0$，$\rho_0=r_*-r_R>0$，$S\ge\max(0,\sup(-d_\phi))$，$D_j\ge\sup|d^{(j)}|$，$Y_m\ge\sup|y^{(m)}|$ 于入端，$F_m\ge\sup|f^{(m)}|$ 于全格。置 $N_{mj}=jD_{m-j+1}$ 当 $1\le j<m$，其余为零，
$$
 w=(1+h/\rho_0)^{-a},\qquad V=wY+(1-w)(c/a)F,\qquad H_m=\max(Y_m,V_m).
$$
有向出端和全格分别由
$$
 |y^{(m)}|_{\rm end}\le e^{mSh}(e^{hN}V)_m,\qquad
 |y^{(m)}|_{\rm within}\le e^{mSh}(e^{hN}H)_m                      \tag{1}
$$
包围。因 $N$ 严格下三角，指数是有限多项式。特别在接续多格时保留出端的 $w$，无需每步都用无衰减的全格值。

证明：对 $m$ 阶角导沿同一真实公漂特征作常数变易。将 $e^{-mSt}(\rho_0+t)^a$ 乘到各阶绝对值的不等式，低阶权的比 $e^{-(m-j)St}\le1$。下三角比较系统的正核为 $e^{(t-s)N}$。入端得到 $w e^{hN}Y$，强迫中 $e^{(h-s)N}\le e^{hN}$，径向核积分质量为 $(c/a)(1-w)$；还原 $e^{mSh}$ 即得第一式。对于任一子步，径向混合 $w(t)Y+(1-w(t))(c/a)F$ 对每个分量都处于入端和全步混合的区间，矩阵指数与前因子逐项随时间单调，故第二式成立。不确定真根在 $w$ 中只经同一比值 $h/\rho_0$；取 $z=a\log(1+h/\rho_0)$，$1-e^{-z}\le\min(1,z)$，极短格也可安全包住损失质量。每个角格还可把 (1) 与同一真实有符号值 $A_1^{(m)}=3(Bx^{(m)}-A^{(m)})/(2\rho)$ 交取。实际 $A_1$ 穿过修复接缝连续，因为 $A,B,x$ 连续；$B_\rho$ 的一侧跳仍在相应源内。数值核在 `fourfold_codazzi_true_damped_radial_moments.py`。

## 第一阶方向只付 $18/|I|$

在 [原完整方向 native 的 193 坐标](R149-supplement-true-ray-speeds-from-the-saved-complete-direction-envelopes.md) 中，任一真实修复后坐标 $z$ 在一个原 cubic 与已付值界域的交 $I$ 为不超过三次的多项式，设 $|z|\le M$。则
$$
                   |z_r|\le 18M/|I|.                                \tag{2}
$$
这是精确最优的一般常数。给出三次的直接证明：将 $I$ 仿射归一化为 $[-1,1]$，以 $-1,-1/2,1/2,1$ 四点的值作 Lagrange 插值。四个基导数在 $x\in[0,1]$ 是二次多项式。把四个导值作为整行写入同一二次 Bernstein 基，三个控制行分别为
$$
 (1/6,-4/3,4/3,-1/6),\quad (5/6,-2,2/3,1/2),\quad
 (-1/2,4/3,-4,19/6).
$$
它们由四个三次插值基直接求导得到，行绝对和分别为 $3,4,9$。二次 Bernstein 权正且和一，故全半区行绝对和不超过 $9$；反射给负半区。乘 $2/|I|$ 导数转换得 (2)。$4x^3-3x$ 在端点达到 $9$。此处没有读取插值点的未知数值，插值恒等式只证明完整原值包络如何限定真实同一 cubic 的导数。先取最大的已付同一 $I$ 再限制到子格；两侧值分别使用各自的 $I$。物理 $\delta_*$ 已乘一次。原中心的 piecewise 常数修复在开片与单侧导数中为零。

`fourfold_codazzi_true_ratio_first_raw.py` 从原176自然文件恢复的模型直接生成 [首比值一阶体强迫](R149-supplement-first-order-genuine-ray-ratio-by-signed-wave-integration.md) 所需整格或原单侧端点的 $d,b,b_\rho,\eta,\eta_r,\beta\Pi S,T_0,V_0,\vartheta$ 等。原 $K_\delta=e^{-\delta w}(K+\delta T_{\rm met}w')$、$\gamma_\delta=\gamma e^{\delta w/2}$ 分别求一次真实导数；原 $\Pi v$ 和 $\Pi v_r$ 保持独立物理坐标。角向积仍是全 Laurent 非循环卷积。$T_0,V_0,\vartheta$ 的有符号式逐项取自 RCS，不再做此前完整 RCS 的 72 槽最大化。本结果给出正权矩的全步及出端定理和可直接使用的一侧系数；真实全域首强迫数值仍由其独立新消费者接收。
