# 已证明：两个真标签在整个实际根片上距恒等提升的 $H^1$ 范数小于 $1/90000$

对与 [WUA.4–6](R133-supplement-global-real-genuine-Airy-trial-and-complete-two-row-source.md) 相同的真根、真实选定 $\delta_*$ 与两方向 $\sigma=\pm1$，在 $c\le r\le r_*$ 有
$$
 \sup_r\|P_\sigma(r,\cdot)-\phi\|_{H^1(d\phi/(\pi/2))}<1/90000.
$$
这里 $P_\sigma$ 使用原始一致提升，$c=76285779072683/320000000000000$。更具体地，
$$
 |P_\sigma-\phi|<1/4000000,\qquad
 |\partial_\phi P_\sigma-1|\le 1/93750 .
$$
若 $H^1$ 使用未归一化的 $d\phi$，第一式右端乘 $\sqrt{\pi/2}$。这些是两方向的同一完整实角估计。

令 $\rho=r_*-r$。在原实际根片 $2549$ 的已付解析延拓上，$X=\phi+\chi$，两个解析函数 $\chi,T$ 在 $\rho=0$ 对所有角都为零。由真根流归一化和 $T=-(3\omega/2)^{2/3}$ 得此零值；原径向级数也分别核验了 $\chi_0=0$、$T_0=0$。已成功的相邻片原 majorants stage 为
`notes/correlated_adjacent_piece_first_Airy_sources_ci/run-43676926141-1/consumers/stages/complete-original-reference-holomorphic-majorants.json.gz`，自然整件 4501 bytes，SHA256 `29ee1093b7644143c693283f774294c176a7f0989b42c004d384a856d5be5144`。它与原执行、publication 的绑定详见 [GCS](R149-supplement-whole-signed-root-seed-at-the-physical-strict-cut.md)。原 $\chi,T$ 两槽的半径和角带分别为 $R=3/8000$、$s=3/128$。两个原有向上界分别小于 $1/80000$、$1/500$（原 balls 的中心分别为 $1.1203080571\ldots\times10^{-5}$、$0.0017399837830\ldots$，半径小于 $5\times10^{-94}$）。

原根上端 $r_*\le2383968743003/10^{13}$，直接交叉相乘给 $(r_*-c)/R<1/90$。整个 $[c,r_*]$ 落在同一实际多项式片内。固定复角对半径 $R$ 的圆盘用 Schwarz 引理，于是该根片的整角带内
$$
 |\chi|\le 1/7200000,\qquad |T|\le 1/45000 .
$$
由实角处半径小于 $s$ 的 Cauchy 圆周，并令半径增至 $s$，两者一阶角导上界分别是上式除以 $s$。只对解析的 $\chi,T$ 使用此论证。实轴上
$$
 \omega=\tfrac23(-T)^{3/2},\quad |\omega_\phi|=\sqrt{-T}\,|T_\phi|,
 \qquad P_\sigma=\phi+\chi-\sigma\omega .
$$
在 $T=0$ 的边界这些角公式连续成立。由于 $\sqrt{1/45000}<1/200$，得
$$
 |P_\sigma-\phi|\le\frac1{7200000}+\frac1{13500000}<\frac1{4000000},
 \quad |P_{\sigma,\phi}-1|\le\frac{128}{3}
 \left(\frac1{7200000}+\frac1{200\cdot45000}\right)=\frac1{93750}.
$$
归一化 $H^1$ 不超过上述两个一致上界之和；$1/90000-1/93750=1/2250000>1/4000000$ 即得结论。若将这个根片与 $[0,c]$ 的带符号数值试函数一同作为全负侧的比较，$c$ 处真实相位从同一 GCS 根数据传入，比较函数可以分别列示。无界率的 $e^{inP_\sigma}$ 始终保留原真相位。
