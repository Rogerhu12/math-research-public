# 全负窗普通态的反向传播与同一强正根七端口

**已证明。** 对实际修补族 $Q_\delta=Q_0+\delta Z$、$\nu_\delta=\nu_0+\delta$、原物理 $\eta_0$，严格负段上任意两点间的完整普通 $L^2_\phi$ 反向传播范数小于 $8.22$。在实际选择的 $\delta_*$ 处，整个 $[0,r_*]$ 上零根迹、零独立跳的已知 $\nu$ 普通体源分量在 $L^2(dr;L^2_\phi)$ 中小于 $2.522\,10^{-5}$。以下再把真实 $r_*\le r\le r_+$ 的正侧窄段接回同一强正侧图。所有角范数用归一化圆测度，两物理行用欧氏范数，$L^2$ 的两个积分都保留。

## 1. 严格负段的原态能量

令 $c=r_+-1/200=2333968743003/10^{13}$，$q=\sqrt{-K_\delta}$，$m=\Pi v$，$\eta=-\gamma m$，$d=-\beta I(u^2+Kv^2)$，$I=\partial_\phi^{-1}(1-\Pi)$。在 $[0,c]$ 取
$$
 U=(h_1/q,h_2), \qquad x=(u,qv),\qquad t=c-r .
$$
[SP.16–18](R133-supplement-complete-primitive-and-mean-strict-propagation-to-the-waist.md) 的 $B_{\rm rev}$ 控制两项 $-\ell_i+d_\phi/2$，其中 $\ell_1=-\beta(1+3u^2+Kv^2)$，$\ell_2=\beta(1-u^2-3Kv^2)$。对完整 moving 方程做上面逐半径的对角变换，主部为实对称的 $d\,1+\eta q\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$ 乘角导，故反向实能量的漂移费用为 $d_\phi/2$，常角部分为零。局部交叉原系数是 $K\ell,\ell$，$\ell=-2\beta uv$；变换后是 $-q\ell,q\ell$，实能量恰抵消。权的反向导数在第一对角给 $q_r/q$。因而本地项只需 $B_{\rm rev}+c_+$，$c_+=\max(0,q_r/q)$。

变换后的非局部项在正向为
$$
 -2\beta x_\phi I(uU_1-qvU_2)
       +\gamma\langle U_2\rangle(-qv_\phi,-u_\phi).
$$
原 primitive 在全四重频率上范数 $1/4$，包括投影。所以第一项范数至多原 SP.9 的 $N_z=|\beta|LR/2$，$R\ge\|x\|_\infty,L\ge\|x_\phi\|_\infty$。第二项的输出向量 $a=(-qv_\phi,-u_\phi)$ 与表示输入泛函的常向量 $b=(0,1)$ 正交，$\|b\|=1$。将 $U$ 正交投到 $a$ 与 $b$ 后用 $2AB\le A^2+B^2$，得任一时间方向上的实能量费用至多 $\gamma\|a\|_2/2\le N_\gamma/2$。这里 $\Pi h_2$ 始终是独立未知量。若 $a=0$，该项直接为零。

对任一 $0\le r\le s\le c$，$\exp\int_r^s(B_{\rm rev}+N_z)$ 至多是已付反向**非径向**比较矩阵整乘积的 $(2,2)$ 项。理由是 SP.17 的该对角为 $\max(0,B_{\rm rev}+N_z)$，其它各项非负。在该两维正系统取第二标准向量初值，第二分量至少为自身对角的标量指数；各格因子都逐项不小于恒等，包括两端不足一格的部分。这个比较直接支配新的标量指数，无须把 $Ih$ 还原成 $h$。

[实际 SP 43731464771/1](R133-supplement-actual-complete-primitive-and-mean-strict-propagation-to-the-waist.md) 给 $(P_-^{\rm nonrad})_{22}<1.164$、$\int_0^c c_+<.847$、$N_\gamma<3.844$、$.5338<q<1.03$。两端原态转换分别为 $\max(1,1/q(s))$ 和 $\max(1,q(r))$。于是同一未投影算子的真正反向 Cauchy 流满足
$$
 \|E(r,s)\|_{L^2_\phi\to L^2_\phi}
 \le {1.03\over .5338}\,1.164\exp(.847+3.844c/2)<U_0:=8.22.       \tag{NRO.1}
$$
这些参数包含原紧支 metric bump 和全部修补，原 SP 的 $|\delta|\le10^{-8}$ 范围足够。对光滑初值可沿两个实特征解对角输运，余项是以上有界算子，逐片 Duhamel 并作恒等传输。该能量不含角导损失，故按稠密性延拓到全 $L^2$。独立的真实物理跳作为其原有符号输入进入同一流。

## 2. 真根至负段和已知普通源的数值贡献

记 $R_0=1/200$，$C_0=6.531704$，$M_*=H^{1/3}_\phi\oplus L^2_\phi$，$B_*=\|h(r_*^-)\|_{M_*}$。[原完整 Cauchy 43621934843/1](R133-supplement-actual-full-real-large-root-Cauchy-energies.md) 接收 $[c,r_*]$ 上两行 $H^{1/3}_\phi$ 体源、原根迹和 $M_*$ 原子。因 $r_*\le r_+$，$r_*-c\le R_0$。对某一根区端值或一枚根区原子，$[0,r_*]$ 上全普通范数增益小于
$$
 A=C_0\sqrt{R_0+cU_0^2}<25.943.                            \tag{NRO.2}
$$
根段在每一点直接用同一 $C_0$，严格段用从 $c$ 的 (NRO.1)，两段平方相加。严格段自身一枚原子增益至多 $\sqrt c\,U_0<3.972$。严格段普通体源增益至多 $D_s=cU_0/\sqrt2$：标量反向 Volterra 核为三角形指示函数，其 Hilbert–Schmidt 范数为 $c/\sqrt2$；先对角 Hilbert 值输入逐点取范数，再用此标量不等式。

对要求的 $h=q_\nu-Z$，显式背景的真体源为 $s_\delta=F_\nu +A_\delta Z-Z_r$。在每个原侧上 $Q_\delta,Z$ 和其角/径向导数均至 quarter-index 96（独立 even mean 包括在内）。线性化的漂移/反应项为不超过三个这类场之积，$I,\Pi$ 不增支集；真实紧支的 $F_\nu$ 按 [D.17–21](R133-supplement-exact-selected-parameter-core-differences-and-finite193-transfer.md) 为 $I(v^2)Q_\phi,v^2Q$ 与 $mJ_\nu Q_\phi$ 的径向标量组合。这证明**全部已知源**至多 288，而未知响应不作任何截断。故根区源的 $H^{1/3}$ 增益为 $W=(1+1152^2)^{1/6}<10.484$。严格与根区 ordinary 源限制到不交径向区间，平方和不超过同窗 [NW 实际 45781137624/1](R147-supplement-actual-same-window-negative-nu-waist.md) 的 $F^2$，$F<1.307204\,10^{-6}$。两个输出未假定正交，三角与输入 Cauchy–Schwarz 给
$$
 D=\sqrt{D_s^2+A^2R_0W^2}<19.29,\qquad
 \|h^{\rm neg,ord}\|_{L^2([0,r_*];L^2_\phi)}<2.522\,10^{-5}.       \tag{NRO.3}
$$
零迹和零独立跳只规定这一个已知体源分量。完整 $h$ 还加 (NRO.2) 的 $B_*$ 与各真跳，正侧源与边界资料通过根数据进入。

## 3. 原强七端口接回 $[r_*,r_+]$

令 $P_L$ 是所有 193 个原物理根头，含 independent even mean；$P_H=1-P_L$。在 [43617150971/1 的强图](R133-supplement-actual-full-real-delta-positive-high-root-to-regular-graph.md) 取完整七输入
$$
 p=(s,F_c,F_b,B,J_c,J_s,J_u).
$$
这里 $s$ 为根稳定高迹范数，两个普通源需 $L^2_rH^{1/3}_\phi$，含输入的完整 head-to-high forcing；$B$ 保留外端、head、独立 mean 与 body 加权跳，$J_c,J_s,J_u$ 是原 collar 和双 cut 跳。在证书完整输出矩阵取 $u=p\cdot\texttt{full_root_outgoing_unstable_port}$ 与 $v=p\cdot\texttt{collar_Z_sup}$（逐项读各球上端）。这两个强图行不是负一窗 $M^{-1}Z$ 的端口。

置 $b=\|P_Lh(r_*^+)\|_{M_*}$ 和
$$
 X=\sqrt{b^2+(9.00002)^2(s^2+u^2)}.                        \tag{NRO.4}
$$
强图真正高根迹是稳/补两个正交坐标，齐次根转换 $(M^{1/3}h_1,h_2)$ 的范数因子小于9；对 $M\ge388$，非齐次 $H^{1/3}$ 最多再乘 $(1+388^{-2})^{1/6}$。低高正交给 $\|h(r_*^+)\|_{M_*}\le X$。如原物理根有不连续，$B_*\le X+\|[h]_{r_*}\|_{M_*}$，该原子仅计一次。独立的强图输入、未知头和根返回均要由完整边界匹配产生。

两根界差准确为 $w=9\,10^{-13}$，同时 $r_+<r_b$。在该整个正小段 [43606747196/1 的 collar](R133-supplement-actual-full-real-delta96-root-collar-certificate.md) 给 $\|P_Hh(r)\|_2\le3v$、$\|A_{LH}\|<58/5$、$\|A_{LL}\|<500$。由 low193 的原初值问题与 Duhamel，逐点
$$
 \|P_Lh(r)\|_2\le E\{b+3(58/5)wv+\sqrt w F+J_p\},\qquad E=201/200,
$$
其中 $J_p$ 是该段所有真实 low 跳的普通范数和，$e^{500w}<E$，源用同一个 NW 全窗。积分给
$$
 \|h\|_{[r_*,r_+]}\le\sqrt w\{E(b+3(58/5)wv+\sqrt wF+J_p)+3v\}. \tag{NRO.5}
$$
$F$ 仅是已知 ordinary forcing；所有强图中的高 forcing 包括物理低反馈。没有对跨根频率用负曲率权。

令 $J_r$ 是根窗口真实跳的 $M_*$ 范数和（含任何根匹配差），$J_s^{\rm raw}$ 是严格段真实物理跳的普通范数和；在 $c$ 的原子按所处一侧计一次。合并 (NRO.1–5)、$b\le X$ 和真宽，整个固定窗给
$$
 \boxed{\displaystyle
 \|q_\nu-Z\|_{L^2([0,r_+];L^2_\phi)}
 \le25.95X+2.85\,10^{-6}v+2.523\,10^{-5}
       +25.943J_r+3.972J_s^{\rm raw}+9.54\,10^{-7}J_p .}           \tag{NRO.6}
$$
例如若已解物理修正连续且实际 $X\le1.90\,10^{-4},\ v\le1$，右端严格小于 $.005$。$Z$ 自身的连续修补只消掉已知 proposal 的 value jumps。$X,v$ 在此未获所需数值；真正的 $q_\nu$ 还要求完整 regular BVP 可解。上述常数是同一显式背景的线性结论。比较非线性真背景时另需完整算子与 $F_\nu$ 的变化。
