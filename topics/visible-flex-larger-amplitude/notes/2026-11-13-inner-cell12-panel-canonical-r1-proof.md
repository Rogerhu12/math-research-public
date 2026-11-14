# 原 cell12 全 1,873 片的有序 canonical 强迫核

作者：geometry_audit（GPT-6 Astra Pro，AI 辅助），2026-11-13。

## 实际结论

本结果在同一旧 R33/R42 几何、同一完整连续条带和同一物理源单位下，给输出模式94、96新的严格两材料端点核。两模式均使用比较上频96；没有宣称重新求出了两个单模 ODE。原1,873片全部使用，未新增分片、径向求积、ODE 或源场求值。

主包 `2026-11-13-inner-cell12-panel-canonical-r1.json` 的 SHA256 为 `4ffa4e25efb846a3f54569b79b79c379db7c09e356c0561217b49f238aa29329`；producer `inner_cell12_panel_canonical_forced_near.py` 的 SHA256 为 `6e7bcf9d4b818890ba9727d0d978fa4418336ab69dfa86267ad7dacccce6bcaa`。主作业正式 exit0，7.3576秒、29,628KiB、15,008门。独立 Python Fraction 保存读出检查另正式 exit0，32门。

新列（十进制仅供显示）为：

|模式|d1 cut 核|d_lambda cut 核|
|---|---:|---:|
|94|4.09964665347e-42|2.33842205968e-41|
|96|2.74086958404e-42|1.34888132236e-41|

此处 cut 核的输出是原端点强 balanced 量再除真实 w，完全同于前件 whole-cell 和原 scalar 两材料 source 核。所有材料、强权、S归一、真实w都已支付。可逐材料与原核相交；其他频窗、无穷带、true far、mean/逆仍各自保留。本件本身不证明新的完整 truecut、固定点或闭曲面。

## 从已保存物理片恢复比较系数

原 `closure_real_linear_head_enclosure.py::PositiveKernels` 的自由与曲率两部分合起来，正是

\[
a\,dr=\sqrt{12}\mu_{12}\,r^{-8}\frac{dr}{w},\qquad
b_0\,dr=\frac{\sqrt{12}}{\mu_{12}}r^6w\,dr.
\]

这里物理半径 r 严格向外增加，mu12 在本胞元中恒定。原生产者把物理 `dr=alpha*dr_o/(1+w²)+|dw|/[8(1+w²)^(3/2)]` 分别积分；本件不重做这些积分，因为每片已经保存完整真实 `DeltaLogr`。以 `dr=r*dlogr`，对一个原片 j，

\[
\int_j a\,dr\le\sqrt{12}\mu^+ (r_j^-)^{-7}(w_j^-)^{-1}\Delta_j\log r,
\]

\[
\int_j b_0\,dr\le\frac{\sqrt{12}}{\mu^-}(r_j^+)^7w_j^+\Delta_j\log r.
\]

所有上下界、`DeltaLogr` 都直接来自原同片严格包。记上述两个量分别为 a_j、b_j，比较上频固定为96，并令

\[
A_j=\nu_{96}a_j,\quad B_j=b_j,\quad
\nu_m=m^2(m^2-1)/12.
\]

实际消费全部1,873片，严格核 `A_j B_j<1`。最大值的向上界约0.394899146365，位于原第335片（从0计数）、segment2整片。没有失败片，也没有把原变动的正量按长度比例分摊或伪造更细积分。

## 原正 Peano–Baker 上界及对角

直接调用冻结 `closure_positive_linear_band_enclosure.py::positive_peano`，其输入为上述完整积分上界 A、B。置 p=AB，原上界为

\[
P=\begin{pmatrix}1+p+\frac{p^2}{4(1-p)}&
A(1+\frac p2+\frac{p^2}{12(1-p)})\\
B(1+\frac p2+\frac{p^2}{12(1-p)})&
1+p+\frac{p^2}{4(1-p)}\end{pmatrix}.
\]

原 canonical 比较系统在 `(Q,Xi/nu_m)` 中有非负公共对角 `(m²−4)dlogr`。因此每片完整未加条带权的正转移上界为

\[
\mathcal A_j=\exp((96^2-4)\Delta_j\log r)P_j.
\]

全部对角指数之和向上界约2.75502789470。每片比较生成器逐点非负，所以其完整转移上界也包该片内部任何 suffix。这允许把**当前片全部正源**乘 `A_j[:,1]`；并非根据一个带符号原矩阵的端点值推断内部传播。

## 连续条带按原定义支付

原 panels 的定义为

\[
\tau(r)=\tau_{in}-(\tau_{in}-\tau_{out})
\frac{\int_{in}^{r}b_\tau}{\int_{cell}b_\tau}.
\]

所以第 j 片的真实条带损失有严格下界

\[
\delta_j\ge(\tau_{in}-\tau_{out})
\frac{(\int_j b_\tau)^-}{(\int_{cell}b_\tau)^+}=:\underline\delta_j.
\]

它采用原正积分包，不相减累计端点区间，避免把累计包的宽度反复丢失。程序逐片核其非负，并核下界之和未超过原完整损失。

对于已经在原 moving tau 上计权的状态 Y，上一片传入部分支付 `exp(-m*delta_j_lower)`；当前片生成的源只知道其剩余条带非负，保守支付1。这样不会把一个整片角宽免费用于该片靠外端生成的源。

## 完整两材料递推

两材料及 `V'=S*sigma12*Vq` 的规范同前件
`2026-11-13-inner-cell12-canonical-forced-r2-proof.md`。
当前片去掉全局 `(S*sigma12)^2` 后的 canonical 源上界为

\[
I_{1,j}\ge\int_j\frac{r^4V_q^2}{\sqrt{12}\mu_{12}}d\log r,
\quad
I_{\lambda,j}\ge\int_j\frac{r^4V_q^2}{\sqrt{12}\mu_{12}}|d\log w|.
\]

逐片用 r、V 的原上界与 mu 原下界支付，并与原 `canonical_source_integral` 的完整正和上界相交。两材料都保留。对 m=94或96，分别从 `Y_0=(0,0)` 实际递推

\[
Y_{j+1}\le e^{-m\underline\delta_j}\mathcal A_jY_j
+\mathcal A_j\begin{pmatrix}0\\I_{mat,j}/\nu_m\end{pmatrix}.
\]

该式保留所有先后次序；没有把不同片的源删去。所用全部矩阵由同一个 m_upper=96 生成，但各模式使用其真实 nu_m 源转换、真实条带指数及真实强权。程序同时保存完整 weighted homogeneous matrix，只供透明审阅；本结果没有擅自替换既有传入预算。

## 原真端点读出与独立保存检查

最后一片的真实 r 及原 ready 的真实 w12 给

\[
c_m=\left((B_{12}m+m^2)r_b^3,
\frac{\sqrt{12}\mu_{12}\nu_m}{r_b^4w_b}\right).
\]

每种材料的 absolute 核为 `2(1+m)(S*sigma12)^2 c_m Y_end`，cut 核再除真实 w_b。保存字段 `source_two_material_to_cut` 可直接消费；`chosen_same_material_to_cut` 是与前一完整全胞元 canonical 列的逐材料交。factor2保留，S平方与强权各一次，不增加输入 frame jump。

独立 Fraction 脚本核对完整保存状态、行向量、S平方、强权、最终真实w除法、共同材料和，以及逐材料 min 的实际输出，并确认四条新列都严格小于前一全胞元列。原比较、条带及源规范的论证仍以本证明和完整 producer 为依据。

## 范围

固定的五个原输入和全部冻结源码由manifest绑定；主包约12KB。资源、完整源、证明和独立检查均归档，未复制大中间数据。旧g与所有 strong 新g/H 身份保持独立；本结果不涉及任何 q122 数值验收。
