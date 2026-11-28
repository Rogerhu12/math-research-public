# R149 补充：选定两列 signed particular 与真实 high 回边的 cut 接收

取同一隐式 $\delta_*$、同一修补 $Q_\delta$ 和 $Z$。记 $i=N,\nu$，$f_i$ 是 [WSS](R149-supplement-whole-signed-selected-both-ordinary-sources.md) 原 $577\times2$ ordinary 体源，$v_i,d_i$ 是 [OHR.2–3](R149-supplement-strong-physical-outer-residuals-and-complete-independent-right-hand-sides.md) 同时给出的已知全部高态与独立 charted-right97 数据。把二者都传回正侧同一实际 low hybrid $G_c$。这里建立新受迫求解和观测公式，首次实际数值要求原完整 WSS 源及 GG 逆和四个源图均已认证。

## SAR.1 从同一组有符号方程得到全部坐标

$S_j$ 保持物理原权重。写 $H_\ell,H_r$ 为 [GBC](R149-supplement-all-signed-hybrid-boundary-columns-and-terminal-physical-preconditioner.md) 真正的 96、97 列齐次边界解。以 $\pi_L$ 将 WSS 的实正交基取前 96 个 odd、原 even mean 和前 96 个 even。对于任意两列真实外加自由数据 $\ell,r$，两列的已知非齐次项严格等于

$$
 z_i^0+H_\ell\ell_i+H_r r_i+u_i+H_r d_i,\qquad
 z_i^0=G_c\pi_L f_i,\quad u_i=G_c B_{LH}v_i .
 \tag{SAR.1}
$$

$\ell_i$ 是 root 的 96 个 nonmean even 原坐标。$r_i,d_i$ 的原 mean 无权，另外 96 行用原 $\Theta$。$r_i$ 在式中排除已单列的 $d_i$。其余实体源（包括未知 low/high 及 height 贡献）按线性叠加进入解。$z_i^0$ 的两个边界坐标为零来自线性分解。真解的边界量保留为独立 signed 变量。

每个完整原 GG 子格上，$z'=A^c z+[\pi_L f_N,\pi_L f_\nu]$ 的同一二维有向 Picard 运算产生相应零起点增量 $j_m$。在其局部平衡坐标中第一项为 $h(A^cx+f)$；更高有序单纯形迭代有 $h^k/k!$，完整尾用 GSR 的 16 阶正分母。每个固定的 $r$，参数、系数和源都取其真实共同值；区间独立取值只扩大包含。若将 $z(r_m)=L_m a_m+R_m b_m$ 投到同一节点的两个逆坐标，则

$$
 a_{1424}=0,\quad
 a_m=U_m^{-1}(a_{m+1}-\ell_{m+1}j_m),\qquad
 b_0=0,\quad b_{m+1}=V_m^{-1}b_m+\rho_{m+1}j_m .
 \tag{SAR.2}
$$

这里 $\ell_m,\rho_m$ 是 GG 节点的矩阵坐标，与边界数据 $\ell_i$ 区别。零起点的各 $j_m$ 可四格并行；式 (SAR.2) 两条有序递推均保留。完整节点 $z(r_m)$ 恢复后，局部两列重新积分得全格内部 signed 包含。按原 1424 格、所有物理子格的 $dr$ 累加三个真实 $2\times2$ Gram，分别对应 $S_mz$ 的全正 body、$Pz$ 的 $[.85,.95]$、及其 $33\ldots96$ shell；$P=\operatorname{diag}(K^{-1/4},K^{1/4})$。各 Gram 的 Newton/ν signed 交叉项和原独立均值都保留。有向积分覆盖每个格内时刻。根原 97、根 $H^{1/3}\oplus L^2$ 的全193、$r=.9$ 的原193，以及外端真实 $\Theta$-weighted96 均保完整 signed 双列。在这些点直接计算 $z_i^0+H(\ell_i,r_i)$；在两个窗口计算自由解的 $D^T\mathcal G_H D$，其中 $D$ 有两列共 193 行。整个窗中 particular 与自由解可用三角不等式相加。

## SAR.2 真 $B_{LH}v_i$ 与同一物理 $d_i$ 的接收

设 $J=B,O,A$ 标记原 $S$-body、outer96 和 raw root97。原 GG ordinary 与 centre-high0-return 两个 complete 图在 $J$ 的有向范数界分别为 $g_J,c_J$；root/outer 的值由原保存平方量单独开方。原 full-family GH5 的 $d_C$ 支配 $B_{LH}-B^c_{LH}$ 的真 raw 界。$B^c_{LH}$ 只收原 carrier97–160，但 $v_i$ 属完整无穷维 raw 空间。投至该 carrier 范数至多一。由 OHR 中原 $L_*$ 及 GH5 的同一 family 分解，

$$
 \|J u_i\|\le t_J C_i,\qquad
 t_J=\min\{g_J L_*,c_J+g_Jd_C\},\qquad C_i\ge\|v_i\|_{L^2(dr\,d\phi)} .
 \tag{SAR.3}
$$

第二项保有实际 $G_cB^c_{LH}$ 整图的 signed 传播后范数，即使 $B^c_{LH}$ 自身的裸界较大也适用。$u_i$ 的独立 root nonmean-even 为零。故全部 mixed root 的新回边至多 $\langle384\rangle^{1/3}t_A C_i$。全窗的 $P$ 加权低态和 shell 可取 $t_B C_i\sup_{[.85,.95]}\|P S_m^{-1}\|$，逐原闭行真实界为 $\max(K^{-1/4},K^{1/4}/q_m)$。另把 $\|d_i\|$ 乘 GBC 的对应整 97 列范数加至各输出；所有量都来自同一个已知 high 解和同一真实外行的像。

cut 不能对单纯 $L^2$ 态取迹。固定 $c=.9$。任选 $h=1/100,1/200,1/500,1/1000$，在完整 $I_h=[c-h,c]$ 上 $u_i\in H^1$，因 $u_i'=A^cu_i+B_{LH}v_i$，有限 193 维 $A^c$ 有界而原 $v_i\in L^2$。平均迹恒等式或 Cauchy–Schwarz 给

$$
 |u_i(c)|\le C_i\left[s_h t_B(h^{-1/2}+h^{1/2} M_h)+h^{1/2}L_*\right],
 \quad s_h=\sup_{I_h}\|S_m^{-1}\|,\quad M_h=\sup_{I_h}\|A^c\| .
 \tag{SAR.4}
$$

逐一覆盖这四个固定弧，真实全193矩阵用其原 signed 区间求谱范数界，$s_h$ 用原 $q_m$。四个有向上界可取最小。四个弧只用于同一点的迹不等式，上述全体积与原两个窗口照原域积分。右边界对 $S$-body 的增益可用 $(1+g_{\mathrm{corr},B})D_B$，来自同一真 hybrid 的 reference right lift 加 $G_c$ 上 second-kind correction。其余各物理 receiver 直接用全部 193 个自由列。

[数学实现](../scripts/fourfold_codazzi_selected_affine_response.py) 按 SAR.2 计算两个 signed particular，按 SAR.3–4 合并真实 high 与原 charted-right97，再在有真实输入向量时施加 $D$。[原整件恢复](../scripts/fourfold_codazzi_whole_signed_response_source_restore.py) 的 preflight 先核真实 WSS actual/execution/manifest、原 19 whole 与原 TCXV 184+32，含其真实 CPU 和原整件恢复身份。恢复只在公共 job 私盘以原 320 bits 逐 piece 比较所有 chunk 和完整 signed source index。允许原 terminal 在第二目标失败，只限实际第一目标已经整件落盘；其余失败或前缀不供计算。完成源匹配后，后续 384-bit GG 中只重新读取其原向外 binary64 后端点。GG 必须由同 job 真实完整模型或 [GRR 原整模型](R149-supplement-whole-signed-response-graph-carrier-recovery.md) 给出。整个 combined job 的单一 wall、实际所有进程内存、native 与私盘总量均需由 owner 执行；中途未过任何整件门均不产生上述数值结论。

这些是原物理方程在指定自由数据上的已知 affine 分量；其余 low 反馈、未定 root/height/waist/world 数据和非线性中心仍在原方程中。未对实际 $X,v$、全负窗 $.005$ 或最终曲面族登记数值完成。
