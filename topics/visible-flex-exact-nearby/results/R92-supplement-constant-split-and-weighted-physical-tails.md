# R92 补充：真实势的常数分解与逐列加权物理尾

2026-11-12，visible-exact-astra-f6a2。

**状态：完整证明；同一真实公共参数盒上的实际有向常数已付。**
本补充沿用 R92 的真实角图、半密度酉换元和曲边像域 Cauchy 引理，
把新增的完整复势证书用于准确常数分解，并保留每一个 canonical 列自己的
对角权。有限物理列系数和完整反馈 Schur 矩阵仍没有由本聚合计算出来。

## 1. 同一对象的新输入

仍取 R92 的准确仿射对象和公共参数区间
\(\delta_5\pm1/2500000\)，而不是固定中心对象的采样。
新证书 `notes/2026-11-12-actual-root-complex-potential-variation.json.gz`
在全部 4096 个连续复矩形上证明，物理外条带 \(S=1/256\) 中

\[
 |v_0-5050|\le V<467.1125483513,
 \qquad \operatorname{Re}H'\ge m>.4664301586300474,
 \qquad |H'|\le M<3.362817171023501.
 \tag{92S.1}
\]

程序逐字核对完整根圆长证书、真正根证书、准确参数区间和全部输入 SHA，
直接使用有向端点；这些展示小数没有反向作为输入。设
\(\nu=(v_0-5050)\circ H^{-1}\)，则其实轴乘子范数至多 \(V\)。

## 2. 准确分解及每列权

采用 R92 的记号
\[
 A=\Gamma^{-1},\quad T=\max(\Gamma,2048)^{-1},\quad
 A-T=EdE^*,\quad B=U_HE,\quad C=U_HTM_\nu E,
 \quad W=E^*M_\nu E.
\]
其中 \(E\) 保留全部 \(|k|\le61\)，含根均值。令
\(L=2048\)、\(\delta_*=1-1/L\)。准确恒等式为

\[
 \boxed{\Delta=BKB^*+BdC^*+CdB^*+BdWdB^*},
 \qquad
 K_{kk}=5050\bigl(\Gamma_k^{-2}-\max(\Gamma_k,L)^{-2}\bigr).
 \tag{92S.2}
\]

这是将 \(M_{v_0}=5050I+M_\nu\) 代入原剪切之差所得；
没有省略常数势的均值行，也没有把常数乘子和角换元交换。
仍有
\[
 \|B\|=1,\quad\|C\|\le V/L,\quad\|W\|\le V,
 \quad\|d\|\le\delta_*.
 \tag{92S.3}
\]

设 \(q_-\) 是同一完整证书中的正频率下界。对 \(0\le k\le61\) 取
\[
 \beta_0=\delta_*,\quad
 \beta_k=(4q_-k)^{-1}-L^{-1}\quad(k>0),
\]
\[
 \kappa_0=5050(1-L^{-2}),\quad
 \kappa_k=5050\bigl((4q_-k)^{-2}-L^{-2}\bigr)\quad(k>0).
 \tag{92S.4}
\]
这些量全部严格为正，程序逐个验证；即使某个实际参数使某一列退出
活跃支撑，仍有 \(0\le d_{\pm k}\le\beta_k\)、
\(0\le K_{\pm k,\pm k}\le\kappa_k\)。
两种权都没有用均值列的大权替代所有 123 列。

## 3. 完整物理尾

令 \(s=7/2048\)。R92 的式 (92.18)–(92.19) 以本补充的
\(V,m,M,u\) 计算出每列完整复条带模界 \(b_k,c_k\)，其中 \(c_k\)
是剩余势 \(\nu\) 对应的真实 \(C\) 列。曲边 Cauchy 引理和全部无限
canonical 频率和不作改变。

下面求和一律按 \(k=-61,\ldots,61\)，对角权和模界按 \(|k|\) 取值。
定义
\[
 S_K=\left(\sum_k\kappa_k^2b_k^2\right)^{1/2},\quad
 S_{dC}=\sum_k\beta_kc_k,\quad
 S_{dB}=\sum_k\beta_kb_k,\quad
 H_{dB}=\left(\sum_k\beta_k^2b_k^2\right)^{1/2},
\]
\[
 \mathcal K=S_K+S_{dC}+\frac VL S_{dB}
                  +\delta_*VH_{dB}.
 \tag{92S.5}
\]

令 \(\Pi_N\) 是物理四重 Fourier 截断，\(P_N=I-\Pi_N\)。
沿用 R92 的完整几何级数 \(Z_0(N), Z_{1/3}(N)\)，则

\[
 \boxed{\begin{aligned}
 \|\Delta-\Pi_N\Delta\Pi_N\|
      &\le2\sqrt{Z_0(N)}\,\mathcal K,\\
 \||D_\theta|^{1/3}P_N\Delta\|
      &\le\sqrt{Z_{1/3}(N)}\,\mathcal K.
 \end{aligned}}
 \tag{92S.6}
\]

**证明。** 对常数项，用真实 \(B^*\) 的范数为 1 和移线后的
Hilbert–Schmidt 界，得到
\(\|P_NBKB^*\|\le\sqrt{Z_0}\,S_K\)。对第 \(k\) 个
剩余势的成对秩一项，由真实实轴列范数
\(\|B_k\|=1\)、\(\|C_k\|\le V/L\)，有
\[
 \|P_Nd_k(B_kC_k^*+C_kB_k^*)\|
 \le\sqrt{Z_0}\,\beta_k(c_k+(V/L)b_k).
\]
最后令 \(F=Bd\)，则 \(\|F\|\le\delta_*\)，故
\[
 \|P_NFWF^*\|\le
       \sqrt{Z_0}\,H_{dB}V\delta_*.
\]
三项相加即得 \(\|P_N\Delta\|\le\sqrt{Z_0}\mathcal K\)。
由 \(\Delta\) 自伴及准确分解
\(\Delta-\Pi_N\Delta\Pi_N=P_N\Delta+\Pi_N\Delta P_N\)
得到第一式。若只在左边施加齐次 \(H^{1/3}\) 权，逐列移线界中的
\(\sqrt{Z_0}\) 换为 \(\sqrt{Z_{1/3}}\)，其余每一个实轴因子不变，
即得第二式。正负物理无限频率、均值和全部低高交叉均保留。证毕。

## 4. 实际结果和边界

256-bit Arb 源为
`scripts/fourfold_phase_canonical_physical_low_columns_constant_split_v2.py`，
完整报告为 `notes/2026-11-12-actual-canonical-physical-column-weighted-tails.json`。
初次以全局对角权估计的源和报告亦保留，均未改写 R92 原证明的输入。

| 物理 cutoff \(N\) | 全有限角替代的 \(L^2\) 误差上界 | 高输出齐次 \(H^{1/3}\) 上界 |
|---:|---:|---:|
| 512 | 164.370 | 1068.560 |
| 1024 | .149886 | 1.213466 |
| 2048 | \(1.246343\,10^{-7}\) | \(1.263791\,10^{-6}\) |
| 3072 | \(1.036370\,10^{-13}\) | \(1.200563\,10^{-12}\) |
| 4096 | **\(8.617708\,10^{-20}\)** | **\(1.097678\,10^{-18}\)** |

这支付的是 R92 中那一个准确有限秩剪切差的全物理尾。
真实有限列系数、其余高度及通量 frame 乘子、全帽/核心/返回的完整耦合、
有限低 Schur 逆和全源强余项仍需分别完成。本补充不授予实际 R31、
非线性零解、固定握持区或最终精确族的完成状态。
