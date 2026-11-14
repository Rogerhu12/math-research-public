# 同一 cell12 的 canonical 强迫端点两材料核

作者：geometry_audit（GPT-6 Astra Pro，AI 辅助），2026-11-13。

## 结论及对象

本结果只消费原 R33/R42 几何与连续条带：cell12 的全部 1,873 个原始 panels、原 `positive-highband-38` 的 9 个正比较矩阵、原 ready 的真实端点公式和原强规范。没有新增 ODE、径向积分、源场求值或固定点。本核可供同一旧 g 的完整 R100 场或已独立证明的较小参数域消费；它不迁移到 strong q098/q106/q122 的新 g。

已正式完成的主包为 `2026-11-13-inner-cell12-canonical-forced-r2.json`，SHA256 `5e03915b960e6ebdfa6847d155a82af5e54866e2bd0fde3e177815d7ea821133`。主 producer `inner_cell12_canonical_forced_endpoint_kernels_v2.py` 的 SHA256 为 `edaca1021dd6d0118ca50e71b5900f270e8c2987e8899fdedd2578bade0d43e6`。主作业正式 exit0，19.8258 秒、38,288 KiB，30,052 个门通过。独立 Python Fraction 保存产品检查另正式 exit0，181 个门通过；它不替代下述比较系统和材料证明。

输出的 11 行采用新频窗 `[94,94],[96,96],[98,104],[106,112],[114,128],[130,184],[186,192],[194,256],[258,512],[514,1024],[1026,2048]`。94 与 96 都使用原 `[94,96]` 矩阵；130–184 与 186–192 都使用原 `[130,192]` 矩阵。没有宣称保存了独立的 94 或 96 基本矩阵。2050–4096、4098–8190 及无穷带继续使用各自原核。

## 整胞元矩阵为什么控制任意源位置

冻结原源 `closure_positive_linear_band_enclosure.py` 明确采用变量

\[
Y=(Q,\Xi/\nu_m),\qquad \nu_m=m^2(m^2-1)/12,
\]

的正比较生成器

\[
M_m(r)=\begin{pmatrix}d_m&\nu_m a\\b_0&d_m\end{pmatrix},
\quad d_m=(m^2-4)r_x/r\ge0,\quad a,b_0>0.
\]

它的每个条目均非负，且随模式增加的条目单调。此处不能仅根据最终矩阵条目非负作推断：关键是**完整连续比较生成器**非负。因而其每段转移矩阵非负，且任意前缀满足 `Phi(y,a) >= I`。对 `a <= y <= b`，

\[
\Phi_m(b,a)=\Phi_m(b,y)\Phi_m(y,a)\ge\Phi_m(b,y)
\]

逐项成立。原文件中的正 Peano–Baker 界逐片相乘，再支付完整非负对角因子 `(r_out/r_in)^(m_hi^2-4)`，所以保存的 `A` 控制该窗所有模式的整个 `Phi_m(b,a)`，也就同时控制每个真实 suffix。

这与冻结 `tail_r33_middle_causal_box.py` 中原 `own_i=A[i,1]*I/nu_lo` 的构造相同。没有对真实带符号基本解作相位抵消，也没有把 `local-scalar` 的坐标转换误当新的独立积分核。

## 两种物理源材料及规范

令 `Vq` 为原 panel 的正包络，`Vstrong` 为 R42 包络，

\[
S=257/256,\quad \sigma_{12}=\overline X_{\rm strong}/\overline X_q,
\quad V'=S\sigma_{12}V_q.
\]

两种物理 kappa 方程材料为

\[
d_1=\frac{V'^2}{rw},\qquad
d_\lambda=\frac{|w_r/w|V'^2}{w}.
\]

输入是乘这些材料的逐模式正负 Fourier pair 弱质量，在原连续 `tau(r)` 上计权；角导数产生的 DQ 系数、完整 Q/T/mean/逆等均由各自源消费者另付。本核不省略这些源，也不代替它们的估计。

原 canonical 方程把物理 kappa 源乘 `r^4*w/(sqrt(12)*mu12)`。于是去掉本次已单独支付的 `(S*sigma12)^2` 后，两种非负 canonical 源积分为

\[
I_1=\int\frac{r^4V_q^2}{\sqrt{12}\mu_{12}}\,d\log r,
\qquad
I_\lambda=\int\frac{r^4V_q^2}{\sqrt{12}\mu_{12}}\,|d\log w|.
\]

对每个原 panel，以保存的 `r.upper^4*V.upper^2/(sqrt(12)*mu_lower)` 乘完整 `radial_log_increment.upper` 或 `log_w_variation.upper` 给严格上界。每种材料还可与该 panel 已保存的完整正 `canonical_source_integral.upper` 相交，因为后一项包含两种材料的和。所有 panels 按原 segment 和 dyadic x 顺序消费，严格核九段覆盖及 1,873 行，没有移除任何源位置。

原两个独立 mu 包络相差一个最低 dyadic 单位。本次保留二者的并集，分母取更小的下界，出口系数取更大的上界；不存在缩小旧包络的免费操作。r1 首试因错误要求其中一个包完全包含另一个而在源循环之前退出1。原失败源/资源记录保留；r2 只纠正此身份包络关系。

## 剩余条带的支付

对第 j 个 panel，记保存的 `tau_range.lower` 为 `tau_j^-`，真实端点宽为 `tau_b`。定义

\[
\Delta_j=\max(0,\tau_j^- -\tau_b).
\]

对任意该 panel 中的真实源位置 y 和本窗模式 m，

\[
e^{m(\tau_b-\tau(y))}\le e^{-m_{\rm lo}\Delta_j}\le1.
\]

因此主输出使用 `I_mat_weighted=sum_j exp(-lo*Delta_j)*I_mat_j`；不带角宽的完整 `I_mat` 也保存供复核。**没有给胞元内新生成的源统一乘整个 cell 的角宽衰减。** 靠近端点生成的源只获得其确实剩余的角宽。源位置依赖被这一正权保留，suffix 矩阵仍使用同一个完整 A。

## 真端点读出

设本窗上下限为 lo、hi。原点态转换的正行向量可取

\[
c_Q=(B_{12}hi+hi^2)r_b^3,
\qquad
c_\Xi=\frac{\sqrt{12}\mu_{12}\nu_{hi}}{r_b^4w_b}.
\]

程序使用最后原 panel 的真实半径上/下界，`closed_port_w(ready,12)` 的真实 `w_b` 下界和原 `mu12` 上界。这里节点12 的 w 按原 physical node 公式计算，不能误换为 cell12 内端的 w。

每材料的 absolute balanced 强量核为

\[
K_{\rm abs}=2(1+hi)(S\sigma_{12})^2
\frac{c_QA_{01}+c_\Xi A_{11}}{\nu_{lo}}I_{\rm mat,weighted}.
\]

输出 `source_two_material_to_cut=K_abs/w_b`，故与原 scalar 两材料 source cut 核单位一致；`source_two_material_to_absolute_endpoint` 则只省略最后这个 w 除法。强因子 `(1+hi)` 支付一次，`(S*sigma12)^2` 支付一次，原 conservative 因子2保留。没有新增输入 frame jump，因为这是 cell12 自身源；传入项仍由原独立 homogeneous 核支付。

前两行的 cut 核约为：

|输出窗|d1|d_lambda|
|---|---:|---:|
|94|1.22069777656e-37|7.72568163531e-33|
|96|8.24899360898e-38|7.36605554513e-33|

十进制只供显示，消费应使用完整 `[integer_mantissa,binary_exponent]` 向上 dyadic。可与任何独立、同源、同材料、同输出单位的原 scalar 核逐项取 min；不可从总预算中相减。对共享一条窗质量的消费者，先对各选定列取 max 后只支付该质量一次；两种不同材料质量仍各自完整支付。

## 可复现与未宣称事项

manifest 固定五个原输入、所有源 SHA、主包、正式资源记录、独立保存产品检查以及首试失败记录。主输出只有约37KB，按原规则归档。重放命令保存在正式 resource 中；scratch 的硬链接输入来自同一仓库内容，未复制大数据。

本结果没有改变低频源、无穷尾、true far、mean 或逆因子，也没有证明任何新的联合自映、收缩、完整 truecut 或闭曲面。其作用是给这些既有对象的后续源消费者提供额外严格正核。
