# R149 AS：原 source coefficient 的完整 signed carrier 与两种误差

**已证明的首次实际计算公式；本文件本身不声称新数值已执行。**
会话 `visible-exact-astra-fb31ed6-20261127`，2026-11-27。

本条接 [WBN](R133-supplement-exact-two-sided-reflected-waist-first-coefficient-normalization.md)、
[WPL](R133-supplement-complete-coefficient-reflection-and-physical-paired-waist-leading-row.md)
和原 [SN](R133-supplement-signed-nonmean-density-transport-and-H3-validation.md)。
目标是原 $\alpha=v_i-w$ 的**首次 signed Fourier carrier**，供原同号
$\mathcal T_\alpha$ 的有限行作用使用。旧 NW 只组合了完整导数和 Wiener
上界；其数值入口没有计算 $w_j$ 或保存 $\alpha_j$。本条不重复这些
旧上界、旧 cohomological theorem、SN residual/energy 或旧 KAM 目标。

## AS1. 原对象、完整均值和实际反射相位

圆周长 $\ell=\pi/2$，测度归一，频率 $4n$。所有对象属于 W 的同一
selected $Q_{\delta_*}$、同一真实 chart $\mathcal H$。写

$$
 \Omega={\pi\over2}{5831714953207175+\sqrt5\over21212218271020390},
 \quad a=2\mathcal H(0),\quad b=a+\Omega,
 \quad R_b f(x)=f(b-x).
 \tag{AS.1}
$$

RRF.18 固定此 $a$；它没有被重置为零。WPL 给
$c_i=\nu+v_i$、$\nu=-\mu/2$、$\Pi v_i=0$ 和
$c_o=-R_bc_i$。原 cohomology 是

$$
 (U_{-\Omega}-Id)w=-(v_i+R_bv_i),\quad \Pi w=0,
 \qquad \alpha=v_i-w.
 \tag{AS.2}
$$

其完整两符号 divisor 已证
$|e^{-4in\Omega}-1|^{-1}\le17(4|n|)$；不重算此常数。
令 $q_n=e^{-4in\Omega}$、$t_n=e^{-4inb}$，则对 $n>0$

$$
 \boxed{\alpha_n={q_n(v_i)_n+t_n\overline{(v_i)_n}\over q_n-1}},
 \qquad \alpha_{-n}=\overline{\alpha_n},\quad\alpha_0=0.
 \tag{AS.3}
$$

这是先在完整函数上作差后得到的等式。它特别给
$|\alpha_n|\le136n|(v_i)_n|$，无需再加一个 $|(v_i)_n|$。
真实 $R_b\alpha=-\alpha$ 保持不变。有限 dyadic trial 可以不精确
满足未知真实相位的奇性；其相位误差必须由下述整误差支付。
两物理 mean slots 不等于 $\alpha_0$，从未删除。

## AS2. 只重物化原 SN 的完整有限终点

完整成功 [SN run43751213826/1](https://github.com/Rogerhu12/math-research-public/actions/runs/43751213826)
保留了所有3146原 intervals、12584个完成 subcells、全部21 gates、
两支四阶 error columns 及完整原终点 identity。其两支各257个
Laurent 系数的 exact-dyadic canonical bytes 为 **245885 B**，SHA256

`3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6`。

原完整 execution 为42242 B，SHA256
`eccb4ce4e7f8c783079e4400cd7a978214817d8092f50cd2bb8f1acbcf3d6ea6`；
其整个 science object 的原 canonical bytes 为22817 B，SHA256
`8fea75ce01dd4bbd0d20532332ed458af73634a995c1dbce5c3cbac511e0e8a0`。
原 manifest 为97309 B，SHA256
`f6e5f9fe938d897c2b57d3d34e42391455fc6cea9804576d4dcc90b2021a8351`，
保留207个完整文件的13,612,391 B身份，不按内容摘取。

原算法每 interval 使用至少4、且是4的整数倍的小格。由于实际完整
计数 $12584=4\cdot3146$，每一格恰好四等分。原 degree6 proposal
仅依赖 point Taylor orders0至5；whole-cell order6、residual、
parameter fee、energy comparison、旧参考范数均不进入其 recurrence。
按原精确 interval 顺序、原两支顺序、原320-bit arithmetic 与每步
dyadic recentering 重建这些 point proposals，归纳即恢复同一终点。
最初 preparatory interval 和旧 prefix 后第一 interval 的两条
linear-mean 系数直接读完整旧 receipt；其余仅从原已成 signed scalar
积分的 endpoint records 重物化原 linear-mean proposal。

必须核上述**完整终点** SHA 后才能消费原输运 error。只核某个 mode、
某支、舍入范数或数组 shape 都不够。原源和 helper 的完整 SHA 分别为
`6c63241ae5ad865952620f68d63670604875b460e51b083ecb66127cb785b339` 和
`217a91e25ec7bb6cad5c115ddc4749f4d714c5ca47601e8ad8dd540e69ed1718`。
runtime 保持 Python3.12.14、python-flint0.9.0、NumPy2.3.5、
$\mathrm{ctx.prec}=320$、$\mathrm{ctx.cap}=9$。所有旧 numerical
validation/norm entrypoints 不被调用；恢复次数单独记录。

## AS3. 一个全均值 raw trial，及其误差的完整四列

SN.29、CT 和 IC 的原顺序给

$$
 t=V_++{\chi_\perp\over\sqrt{r_*}}-{\mu\over2},\qquad
 c_i=U_{\mathcal H^{-1}}t,\qquad
 v_i=U_{\mathcal H^{-1}}t-\nu .
 \tag{AS.4}
$$

因此对 $n\ne0$，可直接换元而不用重求 inverse map：

$$
 (v_i)_n={1\over\ell}\int_0^\ell
           t(y)e^{-4in\mathcal H(y)}\,dy .
 \tag{AS.5}
$$

完整旧原生 root scalar 和 exact finite root polynomials，连同其
全部 selected-parameter enclosures，给 $\chi_\perp/\sqrt{r_*}$ 的
有限 signed coefficient balls；完整 $\mu$ 球保持在常数项。
将其加到已恢复 $\widehat V_+$ 后，按原共轭对选一个完整实 dyadic
polynomial $\widehat t$。常数不投影掉。令 $\rho_q$ 为所有 coefficient
ball 到此 trial 的完整 $q$ 导数 Wiener 半径和，$0\le q\le3$。
读原 SN 对同一 $\widehat V_+$ 的四个完成输运误差 $E_q^{SN}$，则

$$
 \|\partial^q(t-\widehat t)\|_2\le e_q:=E_q^{SN}+\rho_q.
 \tag{AS.6}
$$

每个 $\rho_q$ 保全部负频、正频及 $q=0$ 常数。它是本次新 raw
trial 的 enclosure error，不重新计算旧 qG、transport 或 SEI norm。

读 SN 整个 true-angle conclusion 的原 $4\times4$ inverse-density
matrix $D$、以及已成 SEI 的整个 $\sqrt{j_{upper}}$ record。原
density chain rule 已逐列证明，故

$$
 e_q^H:=\sqrt{j_{upper}}\sum_{k=0}^qD_{qk}e_k
       \ \ge\|\partial^qU_{\mathcal H^{-1}}(t-\widehat t)\|_2.
 \tag{AS.7}
$$

这些是该**新 trial error** 的四个完整组合，并非重新求 $D$ 或
旧 SEI derivatives。于是其 $n$th coefficient 误差可用
$s_n=\min_{0\le q\le3}e_q^H/(4n)^q$；比较各候选的有向上端点，
并把所有完整候选保留在同一自然 mode record。

## AS4. signed quadrature、真正 chart 差与所有 aliases

固定一次 $K=2048$、$L=8192$、$\sigma=1/128$。读原 W 的完整

$$
 E_H\ge\|\mathcal H-G\|_{\mathcal A_\sigma},\quad
 G_1\ge\|G'\|_{\mathcal A_\sigma},\quad
 H_1\ge\|\mathcal H'\|_{\mathcal A_\sigma},\quad G=K_{48}\circ H_{24}.
$$

degree-one lift 的导数常数项恰为1。置
$m=2-\max(G_1,H_1)>0$。沿实轴的竖线积分得到
$\operatorname{Im}G(y-i\sigma),\operatorname{Im}\mathcal H(y-i\sigma)
\le-m\sigma$，上边界同理。仅计算一次新有限 carrier 的

$$
 T_\sigma=\sum_j|\widehat t_j|e^{4|j|\sigma}.
 \tag{AS.8}
$$

完整 grid 上定义 directed quadrature

$$
 z_n={1\over L}\sum_{\ell=0}^{L-1}
   \widehat t(\ell\pi/(2L))e^{-4inG(\ell\pi/(2L))},\quad1\le n\le K.
 \tag{AS.9}
$$

所有 real grid、$G$、两符号 $\widehat t$ 和相位计算用有向 ball。
此 finite sum 的 rounding 属于保存的 $z_n$ 球。周期 analytic
trapezoid alias 的完整几何级数给

$$
 A_n={2T_\sigma e^{4nG_1\sigma}e^{-4\sigma L}
                   \over1-e^{-4\sigma L}} .
 \tag{AS.10}
$$

对同一两个 lift 的差，在下边界作 contour shift 并在它们之间
使用指数的直线积分，得到

$$
 M_n=4nE_HT_\sigma e^{-4nm\sigma}.
 \tag{AS.11}
$$

此步使用完整 $\widehat t$，包括 $-\mu/2$ 对应常数，不能因输出是
非零频率而预先删去该常数。AS.10 保留所有 $\pm L,\pm2L,\ldots$
aliases；AS.11 是整个真实 chart 差，不把有限 $G$ 冒称 $\mathcal H$。
因此 $(v_i)_n$ 在 $z_n$ 周围半径 $A_n+M_n+s_n$ 的完整复圆盘内。

grid 的首点也给 $G(0)$。取
$b\in2G(0)+\Omega+[-2E_H,2E_H]$，并以此整个相位球代入 AS.3。
所有 $q_n$ 来自 AS.1 的 exact quadratic rotation，分母使用真正
directed positive lower。有限直接除法不重新证明原无限 divisor。
先对 $(q_nz_n+t_n\overline z_n)/(q_n-1)$ 形成整 ball，再选其
exact-dyadic midpoint $\widehat\alpha_n$；相位/rounding 整半径之外
加 $2(A_n+M_n+s_n)/|q_n-1|$，记为 $\epsilon_n$。于是

$$
 |\alpha_n-\widehat\alpha_n|\le\epsilon_n.
 \tag{AS.12}
$$

此 head 保存全部2048个自然 mode；$\widehat\alpha_0=0$，所有负频
是 exact conjugates。每个完整 mode record 和其原始 quadrature 球
先保存、读回，才入累加器。不为试另一个 $K$ 重算已成 modes。

## AS5. 完整无限尾和可消费的两种 norm error

对 $U_{\mathcal H^{-1}}\widehat t$，同一换元/contour argument 给
$|(U_{\mathcal H^{-1}}\widehat t)_n|\le T_\sigma q^n$，
$q=e^{-4m\sigma}<1$。用 AS.3 的相关表达式，解析部分的完整
Wiener tail 为

$$
 B_{an}=272T_\sigma
       {q^{K+1}(K+1-Kq)\over(1-q)^2}.
 \tag{AS.13}
$$

余下真实 source error 不假定 analytic。由 AS.7 的第三导数和
两符号 Cauchy–Schwarz、$\sum_{n>K}n^{-4}\le1/(3K^3)$，

$$
 B_\infty=B_{an}+{17e_3^H\over8}\sqrt{2\over3K^3},\qquad
 B_2=B_{an}+{17e_3^H\over8(K+1)^2}
 \tag{AS.14}
$$

分别界整个 $|n|>K$ 的 $L^\infty$ 和 $L^2$ norm。第二式中 analytic
部分安全地用其 Wiener norm；source 部分使用 multiplier
$136n/(4n)^3=17/(8n^2)$ 的全尾 supremum。没有把旧全场 norm
减去另一个 upper，也没有把有限 Galerkin residual 当无限尾。

最终对同一个完整 real mean-zero trial，有

$$
 \boxed{e_{\alpha,\infty}=2\sum_{n=1}^K\epsilon_n+B_\infty},
 \qquad
 \boxed{e_{\alpha,2}=\sqrt{2\sum_{n=1}^K\epsilon_n^2+B_2^2}}.
 \tag{AS.15}
$$

这些完整 balls 可分别接原 DT 的 $L^\infty$ product estimate，或
另外证明的 finite-$G\widehat z$ Wiener/HS product estimate；不能
未经桥梁直接把 $e_{\alpha,2}$ 当 $e_{\alpha,\infty}$。

## AS6. 实际记录与范围

所有重物化和新 arithmetic 只在公开 Actions。完整旧 SN 索引及
全部原文件 identities 保留；current inputs 使用带 role 前缀的
private snapshot 名字。大载体仅在 runner，完整 bytes/shape/SHA
进入小结果；不上传 Git、Release 或 artifact。纯 dyadic $\widehat\alpha$
另有独立完整载体 SHA，与含 mode-error 的诊断载体分开。后继只恢复
同一 grid、quadrature、相位和 coefficient midpoint 并核此整 SHA，
无须重跑已经完成的每模 error 或最终 norm。prefix 保存完整
已成 mode count、完整 private carrier hash、两种 directed 累加器
和旧输入身份，失败不抹去已成 prefix。

本条需要第一次实际成功才能给新的两球数值和 signed carrier SHA。
即使这次成功，它仍只供原 source $\mathcal A$；IR、真正 $\overline G$、
全部 physical means、真实 PDE matrices、$\nu$/phase、无限补与
非线性嵌入族义务继续保留，不声称课题完成。
