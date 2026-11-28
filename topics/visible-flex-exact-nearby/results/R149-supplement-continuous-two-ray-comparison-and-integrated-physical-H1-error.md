# 已证明：两真射线的连续 Fourier 比较及整物理域 $H^1$ 误差

设 $P_\sigma=\phi+u_\sigma$ 为原 CRW 的真标签。以下对每个带号系数和真实参数成立，给出了直接从同一全域残差得到两种不同范数的公式。相位误差本身从不乘无界输入频率。

取 [原 193 坐标速度](R149-supplement-true-ray-speeds-from-the-saved-complete-direction-envelopes.md) 的某个物理格，$h=r_R-r_L$，$\tau=(r_R-r)/h$，$a_\sigma=h(d+\sigma b)$。试函数 $q_\sigma=\sum_{j=0}^6 q_{\sigma,j}\tau^j$ 中的系数为保留 $|k|\le128$ 的有限 Hermitian Laurent 多项式，其实虚部为确切的 binary64 dyadic。速度有端点真 Taylor 阶 $0,1,2,3$、整片四阶逐 Fourier 余项及整片的 193 坐标小差。试函数的有限投影只用于提议系数。证书使用
$$
 f_\sigma=-q_{\sigma,\tau}-a_\sigma(1+q_{\sigma,\phi}),
 \qquad
 (\partial_\tau+a_\sigma\partial_\phi)(u_\sigma-q_\sigma)=f_\sigma .
$$
每个速度余项的系数可以随 $\tau$ 变化；这不影响由同一整格区间包围每个时刻。所有时间系数先按有符号同频相加，再在 $0\le\tau\le1$ 上作区间 Horner，各角频的绝对值乘 $(4|k|)^m/m!$ 后求和。速度差最高 192 模乘比较最高 128 模要算到 320 模，原均值保留。共同漂移 $ω$ 的残差同样为 $h b(1+q_{X,\phi})-q_{\omega,\tau}-h d q_{\omega,\phi}$，其中 $q_X,q_\omega$ 分别是位移的半和、负支减正支的半差。再依 [原输运误差](R149-supplement-regularized-action-moments-and-full-circle-phase-residual.md) 加 $|hb|(m+1)(Y_{+,m+1}+Y_{-,m+1})/2$。因此本文保留两标签到九阶、同点共同间隙到八阶。原 GCS 的 2048 节点/整格均入初误差；构造多项式时的 DFT、高阶导反推和低模截断均由独立全格误差接收。

令 $v_\sigma$ 是原本要传递到下一格的 dyadic 端点。记 $j_\sigma=q_\sigma(1)-v_\sigma$，
$$
 Q_\sigma(\tau)=q_\sigma(\tau)-\tau j_\sigma.
$$
下一格以 $v_\sigma$ 作 $q_\sigma(0)$，故 $Q_\sigma$ 在全部真实接缝连续。它的两侧径向导数可以不同。若 $Y_m$ 给出原比较误差 $\partial_\phi^m(u_\sigma-q_\sigma)/m!$ 整格上界，写
$$
 E_m=Y_m+\|\partial_\phi^m j_\sigma/m!\|_\infty,\qquad
 B=\|f_\sigma\|_\infty+\|a_\sigma\|_\infty Y_1+\|j_\sigma\|_\infty .
$$
对 $u_\sigma-Q_\sigma$ 的角误差及出端误差用 $E_m$；对 $\tau$ 导直接用输运式得 $|\partial_\tau(u_\sigma-Q_\sigma)|\le B$。这里 $Y_1$ 是未加端点修正的真实角导误差，式中其余两项已含全部修正。归一化物理角测度取 $d\phi/(\pi/2)$、径向取原 $dr$。从而格内的角 $H^1$ 平方上界与空间时间 $H^1$ 平方积分费用分别为
$$
 E_0^2+E_1^2 ,\qquad h(E_0^2+E_1^2)+B^2/h .
$$
这些都是相对于同一连续比较 $Q_\sigma$ 的误差；端点跳没有作为分布源遗漏。

在 $[c,r_*]$ 用 $Q_\sigma=(\rho/\rho_c)v^c_\sigma$，$v^c_\sigma$ 是 GCS 初始的确切 dyadic 试函数，$\rho_c=r_*-c$，逐同一真实根。故根比较在 $c$ 连续接上首格，也在真根准确归零。[全根片小量](R149-supplement-small-true-root-label-H1-on-the-complete-physical-root-patch.md) 已给 $|u_\sigma|<1/4000000$、$|u_{\sigma,\phi}|\le1/93750$。取相同解析延拓的径向 Cauchy 圆周，其半径可趋于 $R-\rho\ge89R/90$，所以 $|\chi_\rho|\le3/89$、$|T_\rho|\le480/89$。因 $\sqrt{-T}<1/200$，有 $|u_{\sigma,\rho}|\le(3+480/200)/89<1/16$。于是以
$$
 A=1/4000000+\|v^c_\sigma\|_\infty,\quad
 C=1/93750+\|\partial_\phi v^c_\sigma\|_\infty,\quad
 D=1/16+\|v^c_\sigma\|_\infty/\rho_c
$$
分别包住根片三个误差。整域角 $H^1$ 取根片 $\sqrt{A^2+C^2}$ 和上述每原格上界的最大值；整物理域 $H^1$ 取各原格平方积分费用之和，加 $\rho_c(A^2+C^2+D^2)$ 后开方。因数值比较连续，逐格弱导数即全域弱导数。对不确定 $\rho_c$，分母用原根下端、长度用原根上端。

对应公开运行入口为 `fourfold_codazzi_true_phase_global_validation.py`，逐格算术在 `fourfold_codazzi_true_phase_circle_validation.py`。完整接续需要第一次成功的 GCS 整载体字节数及 SHA；若必须重物化先核对此同一原 SHA，再取两标签和相关间隙。上限 4000 格、每格保存两支各七个时间 Fourier 系数和独立的确切 dyadic 出端，各含 $129$ 个非负复频率，以及 $10+10+9$ 个有向误差，共 33256 bytes/格；约 133.1 MB 加实际分片表，硬限 140 MB。负频由严格检查的实共轭恢复。私有整件写完后独立逐格读到 EOF 并复核压缩与展开载体 SHA。每格的试函数至多 180 次时间卷积中的有限 Laurent 乘积（其中 35 次的速度因子为零模）（另有原速度的 Taylor 积），角误差作有限九阶三角传播。两个整域 $H^1$ 各有 $1/64$ 的实际通过门，未运行之前没有声称门值。此误差证书描述真相位、原 mean 和两方向；后续真 FIO 强迫、独立两端和完整归一化响应仍须沿原方程计算。
