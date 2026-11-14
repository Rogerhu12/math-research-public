# 完整实参数正区逆：原 M32 主块与小 M96 差分开支付

本篇对同一个 $Q_\delta=Q_0+\delta Z$、实 $|\delta|\le10^{-8}$ 给新的有限数值合同。$Q_0$ 是完整连续 M32 修补，$Z$ 是 full193 的 degree96 连续方向，均保独立 even mean。全未知状态含任意高 Fourier 模；背景的带宽不限制未知解。

原完整正区的4650格、3594个接口，以及原源项的7721格只读复用。新计算只有系数增量、真实新 Riccati reference 的标量下比较和两个 Volterra sweep。以下每项收缩门必须由新公开 Actions 真正通过；不能沿用旧 $\delta=0$ 的数值许可。

## 1. 完整原数据如何给同一个 $Z$

使用原 positive native eefb94952a409473fed7f9c34afc9214a3346d8c3b19ed7e0a7fc6fd06f48a68 的全部 inflated_rows；它已保原 intrinsic、完整修补中心系数和原接口。使用原 repair-source native 05e0493dbe55490adec8fb6603e0ec431d1bc03f051aec86be8a78741f60f0a4 的全部7721格。

后一个原 producer 准确先对完整 raw cubics 取 Bernstein pair 范数 $H_0,H_1$，再把 $H_0$ 更新为 $H_0+|e_z|$。其字段 complete_mean_corrected_response_pair_A0 因而合法控制 raw；complete_response_angular_derivative_pair_A0 是 raw 的真实角一阶。这里没有从抽象的 $q^*$ 范数反推 raw。

在每一原 positive 格内，对覆盖它的所有原7721格取这些合法上界的最大值，再加原全 $[0,25/8]$ 连续方向 offset 的角零/一阶费：
$$
Z_0=H_0+E_{\mathrm{off},0},\qquad
Z_1=H_1+E_{\mathrm{off},1}.
$$
每次都检查准确有理区间从左至右无空隙。offset 的一阶是角导；它在每个原片内的正阶径向导数准确为零。新全球费用取
$$
e=10^{-8}Z_0,\qquad e_1=10^{-8}Z_1,\qquad e_m=e. \tag{B.1}
$$
$e_m$ 是保守完整 mean 费，不把它删除或只借负区小窗。

## 2. 真新 reference，全部频率与全部接口

正区为
$$
r\in[1192029371497/5000000000000,25/8],\quad N=97,\quad M_{\min}=388.
$$
内禀 $K$ 不变，$1/2000\le K\le4$；但
$$
a_\delta=-\gamma m_\delta
$$
真实改变。必须逐格重新证明 $a_\delta>0$、$m_\delta<0$ 和物理逆角 gap 为正。主项 $\delta a\,\partial_\phi$ 没有作为有界 $L^2$ 小算子处理。

用真实正则外图的频率无关 $p_M(R)=q_*/(-m_\delta(R))\in(1/8,1/5)$，以及 genuine root 初值 $g_M(r_*)=M^{-1/3}$。在本正区左端令 $g=0$ 只作下比较，绝不改真正根初值。全局 $p_M,g_M\le2$；正区 $p_M\ge1/45$。

[相对全局 Riccati 证明](R133-supplement-relative-global-Riccati-reference-and-frequency-derivatives.md) 的变分与单调比较适用于任意此种正、频率无关的 $a_\delta$。每格用实际新速度下界和 $M_{\min}$ 重新作原 lower_flow，获得所有频率的 $W_M=p_M+g_M$ 下界。框架
$$
F_M=M^{-1/6}W_M^{-1/2}
 \begin{pmatrix}p_M&-g_M\\1&1\end{pmatrix}
$$
仍有原全频率对数导数界。原 M32 主块的所有旧证明常数因而适用，只须支付新的 $W$ 分母。

全部3594原接口原样保留。$Q_0$ 与 $Z$ 的值和全部角导连续，故 $Q_\delta$ 同样连续；这不使未知状态或试算误差的 affine jump 为零。原 ordinary、divergence、mean 和任意 prescribed jumps 都按原合同保留。

## 3. 全系数与独立 mean 的增量

令 $U,V,U_1,V_1,V_{\ne0}$ 是该格原完整修补中心的角 Wiener 范数，$\beta=|b|$、$K_+$ 为原 $K$ 上界。设置
$$
\Delta u^2=2Ue+e^2,\quad \Delta v^2=2Ve+e^2,\quad
\Delta(uv)=(U+V)e+e^2,\quad
\Delta S=\Delta u^2+K_+\Delta v^2.
$$
完整局部矩阵增量上界为
$$
d_a=\beta(3\Delta u^2+K_+\Delta v^2),\quad
d_e=\beta(\Delta u^2+3K_+\Delta v^2),\quad
d_b=2\beta\Delta(uv). \tag{B.2}
$$
由于 $d_\phi=-bP_{\ne0}(u^2+Kv^2)$，取
$$
d_{\phi,\Delta}=\beta\Delta S,\qquad d_\Delta=d_{\phi,\Delta}/4.
$$
投影在完整 Wiener 范数中收缩，所以没有把真实 mean 当成零。

新 $U,V,U_1,V_1,V_{\ne0}$ 依次以 $e,e,e_1,e_1,e$ 膨胀；真实 mean 以对称半径 $e_m$、主速度以 $\gamma e_m$ 膨胀。mean own-rate 还加
$$
\beta[\Delta S+2K_+(2|m|e_m+e_m^2)].
$$
完整 primitive、mean rank 和 mean/nonmean feedback 分别保
$$
\frac{\beta}{2}(U_1+V_1)(U+K_+V),\quad
\gamma(U_1+K_+V_1),\quad
2\beta|m|(U+K_+V_{\ne0}), \tag{B.3}
$$
其中此处各量使用新上界。实现直接使用冻结的原 inflation 算术，不重做任何旧目标。

## 4. 大 M32 主块仍保原费用

原主块真实 degree32，局部带宽64。以原中心上界和新 $W_-$ 定义
$$
B_{\sup}=a_{\sup}+e_{\sup}+(K_+/W_-+4)b_{\sup},\qquad
B_A=a_A+e_A+(K_+/W_-+4)b_A,
$$
$$
F_N=U_1U+K_+V_1V+(K_+/W_-)U_1V+4V_1U.
$$
对 order $s=0,1$，原完整费用为
$$
E_{\mathrm{base},s}
=(c_s+\tfrac12)\|d_{0,\phi}\|_{A^0}
 +2B_{\sup}+\frac{8d_s32}{97}B_A+\frac{n_s\beta}{65}F_N, \tag{B.4}
$$
$$
(c_s,d_s,n_s)=(6,3,4)\ \text{或}\ (18,9,8).
$$
不能把原整个大背景冒称 M96 后无谓扩大这个完整已证主块；只有下面真实差项用新宽带。

## 5. 小 M96 差的两行、符号与 primitive

新差的局部支撑为192。若输入、输出都在 $|j|\ge97$，相反符号的距离至少194，不能被这条带连接；同号物理频率比严格小于3。新框架比 $R(M,N)=F_M^{-1}F_N$ 满足
$$
\|R\|<3^{5/3}<7,\qquad N\|R-I\|\le12|M-N|. \tag{B.5}
$$
由此 real transport 的 $\tfrac12 d_{\phi,\Delta}$ 与 frame commutator 在 $s=0$ 共小于 $12.5d_{\phi,\Delta}$，取16。$s=1$ 使用
$$
MR-NI=M(R-I)+(M-N)I
$$
得到37.5，取40。没有留下 $N\tau$ 无界费用。

令
$$
\Delta B_A=d_a+d_e+(K_+/W_-+4)d_b.
$$
同频两行的局部矩阵界为 $2\Delta B_A$。乘完整 frame ratio，小于 $14\Delta B_A$；$s=1$ 再付频率比3。各再留一倍余量，取28和84。

primitive 差必须按原次序分开：
$$
-2b\left[
 (\delta Q_\phi)\,I(Q_\delta h)
       +Q_{0,\phi}\,I(\delta Qh)\right]. \tag{B.6}
$$
每个背景因子的带宽不超过96。高输入 $|j|\ge97$ 的所有 signed intermediate 都有物理频率绝对值至少4，所以 $I$ 收费 $1/4$，且这里不生成 primitive mean。两个 frame 的 rank-one 乘积可取
$$
\frac{2\,3^{2/3}}{W_-}
 (U_1+2V_1)(2U+K_+V).
$$
因此定义
$$
\Gamma=
3e_1[2(U+e)+K_+(V+e)]
 +(U_1+2V_1)(2+K_+)e, \tag{B.7}
$$
其中 $U,V,U_1,V_1$ 是原中心量。完整差 primitive 费用可取
$$
\frac{3\beta\Gamma}{W_-}\quad(s=0),\qquad
\frac{9\beta\Gamma}{W_-}\quad(s=1). \tag{B.8}
$$
已包含两符号的 Wiener 和、两条原曲率行及所有 intermediate。mean-rank 的输出至多96，在 high-high 块准确为零；它仍进入完整 head 与独立 mean 方程。

新的总费用为
$$
E_{\delta,s}=E_{\mathrm{base},s}
 +(16,40)_s d_{\phi,\Delta}
 +(28,84)_s\Delta B_A+(3,9)_s\beta\Gamma/W_- . \tag{B.9}
$$

## 6. 完整源、正区 sweep 与外端

阻尼仍取真实新速度的
$$
\mathrm{gap}=388\,a_{\delta,-}W_-/2.
$$
按原 forward/backward 两支分别积分 scalar affine_decay，再将两支平方和开根，而不是把频率各自的点值最大虚当统一逆。ordinary source 使用同一个完整 frame 的平方、双倍阻尼 sweep。原 Bessel 权和两端 trace 费不变。

新 head-to-high 支撑到 $96+192=288$，必须付物理频率1152上的 $H^{s+1/3}$ 壳权。head-to-high、high-to-head、head generator 由新完整字段计算；primitive 与 mean rank 按 (B.3) 保留。这里没有宣称 high-to-head 反馈已经小。

order0 的高外 feedback 来自新实际 full-$\delta$ 物理外图。order1 继续保独立右 high port，不继承一个未证明的 $H^{7/6}$ exterior。对每个 order 都须重新核真正 interior 加 exterior 的总反馈小于1，之后才给 resolvent、ordinary source、所有 affine jump 与两端 raw trace 上界。

原 ordinary 合同为 order0 的 $L^2_rH^{1/3}_\phi$ 和 order1 的 $L^2_rH^{4/3}_\phi$；各接口 jump 使用其实际 $H^{s+1/3}$ 标签范数，完整 mean/head 另保。本证书完成后仍只授给定完整 finite head 的全 high 正区逆。完整 finite head、negative return、参数 Schur、非线性分支及最终闭等距族仍必须继续，不能由上述局部数值门直接宣称。
