# n4：两条真实 cut 高度约束的精确 Schur 响应与分支条件

维护：Astra-held10-1b6d88ec-20261120 / n4_continue。

**可信度：新的有限方程代数结论及解析线性机制；没有新 BVP 数值接受。**
附带实现只消去现有 Jacobian 的块；执行环境 unavailable，本条没有运行它。
旧 session18524 / session2919 的终态仍未知，不由以下推导补造终态。

## 1. 需要解决的具体问题

[恢复记录](2026-11-20-n4-recovered-environment-and-new-entry.md)中的原线性 DN 冷恢复，
第一次已接受 Newton 的 `p0=.05499534450711677`，使实际 q 相对 gauge 增约 5.6%；
其后接近 Frenet 域边界。这不是原 2026-11-18 真联合解失效的证据。

新的[两高度恢复入口](../scripts/resume_n4/recover_height_anchor.py)使用原实际尾记录的

\[
H_4=-9.422721665900606\,10^{-6},\qquad
H_8=-3.5119114617306655\,10^{-8}
\]

替换首两条线性 DN 条件，其余条件仍是原线性 DN。问题不是“高度数值很小便安全”，
而是：这两条观测是否在消去全部场与非共振控制后，仍能独立确定两个分支坐标？

这里完全固定物理 profile、raw anchor J、角图和 q 的数值 gauge。参数是

\[
p_0=\log(q_{\rm actual}/q_g),\qquad p_j=c_j/q_g\quad(j\ge1).
\]

本 raw 固定 profile 模型的 p1 是**自由 c8 控制**；它不是另一个 dual-design 模型中的 vd。
[原 coupler](../scripts/resume_n4_tail/couple_raw_actual_tail.py)使用的实际尾高度是

\[
H=\sigma q_g P_zY_{\rm cut},\qquad \sigma=\text{bridge.sigma}.
\]

本 profile 的 sigma=-1。必须使用固定 gauge qg，不能在这个公式中擅自换成
qactual(p0)。qactual 对高度的影响由求解后的场响应承担。exact lift 在 cut 恒为零，
所以固定 Ycut 时高度对 p 的直接偏导为零。

## 2. 精确有限 Schur 公式

令完整 collocation 未知为 z=(Y,p)，其中 Y 含所有节点上的 n=3M+1 个状态。
选两个分支坐标 alpha=(p0,p1)，其余未知记为 w=(Y,p2,...,p[M-1])。

将残差分为：

- E(w,alpha)：全部 collocation、全部 inlet、以及未被替换的 M-2 条高模 DN；
- F(w,alpha)：最后需要的两条低模条件。

原低模 DN 使用 F=FD；两高度恢复使用
FH=W(H-Htarget)，W=diag(1/bcweights[0:2])。对于任一同一点的精确 Jacobian，写

\[
K=E_w,\quad B=E_\alpha,\quad C=F_w,\quad D=F_\alpha .
\]

**命题 1（局部正则条件）。** 若 K 可逆，则完整线性化可逆当且仅当

\[
S=D-CK^{-1}B
\]

可逆。对原 DN 和两高度分别得到 SD、SH；两者共享 K 和 B。
因此两高度约束局部确定同一高模约束分支的正确条件是

\[
\det S_H\ne0,
\]

而不是两个目标高度非零，也不是原 DN Jacobian 的秩本身。

**证明。** 线性化为 K dw+B dalpha=-E，C dw+D dalpha=-F。
令 v=K^-1 E、Z=K^-1 B，代入即得

\[
S\,d\alpha=-F+Cv,\qquad dw=-v-Z\,d\alpha.
\]

这是可逆块消元；行列式为 det(K)det(S)。证毕。

这也明确了冷初值的重要差别。冷场一般 E≠0，正确的两高度 Newton 右端是

\[
b_H=-r_H+C_HK^{-1}E .
\]

原初猜 H4 与目标 H4 相差约 0.47%，**并不保证 dalpha 小**：
内部方程缺陷经 CH K^-1 E 反馈，可能比高度目标差大。
需要分别看这两项，才能区分“场初值不够好”与“高度坐标退化”。
上式保留原正曲率、Frenet 根和 Newton 线搜索门，没有新的接受捷径。

## 3. 两条高度作为分支坐标时的真正响应

在 E=0 的局部约束流形上，

\[
\frac{dw}{d\alpha}=-K^{-1}B,\qquad
\frac{dH}{d\alpha}=W^{-1}S_H.
\]

这里将 target 仅作为两条边界观测：profile、切点、角图、网格、qg 和其余方程均固定，
所以 E 不显含 target，且 F_target=-W。若 SH 可逆，目标高度变化引起的分支参数响应精确为

\[
\boxed{\frac{d\alpha}{dH_{\rm target}}=S_H^{-1}W}.
\]

若 target 还改变 profile、切点或网格，就必须使用一般公式
\[
\frac{d\alpha}{d\tau}=S^{-1}(CK^{-1}E_\tau-F_\tau),
\]
不能沿用上面的简式。

若另有物理或尾算子同伦 t，E、F 都可显含 t。原方程的切向量满足

\[
\alpha'(t)
=-S^{-1}\bigl(F_t-CK^{-1}E_t\bigr),\qquad
w'(t)=-K^{-1}\bigl(E_t+B\alpha'(t)\bigr).
\]

这给出保留两高度、逐步把**高模**线性 DN 接回实际非线性 DN 的正确 predictor，
并指出不能只改末端两行而遗漏内部或其他尾方程的 t 导数。
它是条件响应公式，不证明整个 t 区间存在解或保持域门。

### 量纲与缩放

SD 的行是导数/Robin 残差，SH 的行是高度残差；不能直接用其未缩放元素大小判断
哪种方法更好。给定明确的两维分支尺度 P 和物理高度尺度 L，应比较

\[
\widehat S_H=L^{-1}W^{-1}S_HP .
\]

这只是数值坐标下的条件数诊断。常数残差行缩放不改变精确 Newton 步：
若 J、r 同乘同一可逆行矩阵，则 (RJ)^-1(Rr)=J^-1r。
它会影响浮点条件数和 BC tolerance 的物理单位，不能据此放宽原 BC 门。

如果 K 本身不可逆，只说明所选两个参数列没有给出可用的补空间；
不能据此宣布原完整方程无解。可换两个独立参数列，或改用实际低阶入口矩作为
分支坐标，再核其参数映射的秩。尤其 raw/window 控制的物理单位与 Fourier
support 系数不是同一个概念，不能把参数标签当作已对角化的模态。

## 4. 线性双共振为何可以让 DN 响应退化、同时保留高度响应

以下只解释机制，不替代有限幅值 SH 的实际评价。

固定背景子午线 a(s)>0，v=a_s，b=sqrt(1-v^2)>0。原可分离线性 m 模的两场系统为

\[
\frac{d}{ds}\binom{f}{g}
=\frac1a
\begin{pmatrix}
 -(m^2-1)v&-m^2b\\
 (m^2-1)v^2/b&m^2v
\end{pmatrix}
\binom{f}{g}.
\]

其系数矩阵迹为 v/a，
故转移矩阵 Tm 的行列式精确为

\[
\det T_m(s,0)=a(s)/a(0)>0.
\]

平面 core 的线性入口是 (f,g)=(am,0)。在本类实际尾 cut，
原 Robin 条件的非零核向量可写成

\[
(C_m,1),\qquad
C_m=\sigma w_{\rm cut}
       \frac{r_{\rm cut}D_m-m^2}{m^2-1}.
\]

**命题 2（共振点的高度不消失）。**
若非零平面入口在某一 m 模恰好满足该 Robin 条件，则其 cut 高度 gcut≠0。

**证明。** 若 gcut=0，由 Robin 核=(Cm,1) 得 fcut=0；
Tm 可逆又推出 am=0，与非零入口矛盾。证毕。

更明确地，令单位入口满足
\[
T_j(1,0)^T=h_j(C_j,1)^T,\qquad h_j=(T_j)_{21}\ne0.
\]
物理入口幅度为 a_j 时，尾方向高度为 H_j=\sigma_jh_ja_j。
这里 alpha 只改变同一固定线性背景上的入口幅度，不改变 T_j 或 sigma_j。
若也改变背景，导数还含 a_j\,\partial_\alpha(\sigma_jh_j)，不能省略。
在高模 DN 补条件已消去的线性分支上，令
L_{jk}=\partial a_j/\partial\alpha_k；则
\[
\frac{dH}{d\alpha}=\operatorname{diag}(\sigma_jh_j)L.
\]
因此两维 L 满秩时，此高度响应也满秩。这一步明确使用了线性系统对入口幅度
的齐次性，不能仅由 det(T)>0 直接推出一般非线性 Jacobian 满秩。
在零振幅点应使用 a_j 坐标；log(q/qg) 只用于 q>0 的实际分支。

所以在两个独立低模同时发生线性共振时，原低模 DN 对各自振幅的响应可为零，
而 cut 高度对各自振幅的响应仍非零。若所选两个分支坐标到这两个入口振幅的
映射也满秩，线性模型中的两高度响应可逆。这是用 H4/H8 定支的机制。

该论证**不保证**真实有限幅 raw 解的 SH 可逆：非线性耦合、core 控制列混合、
高模补空间病态或实际 Frenet 边界都可能破坏数值可用性。它也不排除
R20 的精确圆弧小幅有限谐波切空间障碍。

还可得到一个不为零但可能很小的线性下界。若
Tm(1,0)=hm(Cm,1)，由行列式有

\[
h_m=\frac{\det T_m}{C_m(T_m)_{22}-(T_m)_{12}},
\qquad
|h_m|\ge
\frac{a(L)/a(0)}
 {\sqrt{1+C_m^2}\,\|T_m(0,1)\|}.
\]

因此“响应非零”和“有限精度下容易反解”是两件不同的事。
本课题的尾部衰减会使高度响应很小，必须用物理尺度及真实矩阵报告条件数。

## 5. 直接作用于原 collocation Jacobian 的实现

新增 [height_anchor_schur.py](../scripts/resume_n4/height_anchor_schur.py)。
它接受原 Jacobian 和原残差，不重建物理模型，也不替换原求解器。

原 Newton 的排列为：

\[
z=(\operatorname{vec}_F Y,p),\qquad
r=(\operatorname{vec}_F r_{\rm col},r_{\rm inlet},r_{\rm terminal}).
\]

若网格有 N 个节点，状态总数 Q=nN，则首两低模 terminal 行是 Q+[0,1]，
分支参数列是 Q+[0,1]。去掉这两行、两列就得到 K。
高度行只在末节点的 z-mode 列上非零：

\[
\partial_{Y_{z,j}(L)}(F_H)_j=\sigma q_g/\mathrm{bcweights}_j .
\]

使用一次稀疏 LU，计算一个残差 RHS 加两个参数 RHS，即可同时得到
SD、SH、两组右端，以及完整原 Newton 步和两高度 Newton 步。
保留高模 DN 的这个消元避免先构造容易爆涨的纯前向变分基本解。

实现还分别返回原低模残差、两高度残差、CD K^-1 E 和 CH K^-1 E；
这能直接诊断一次冷步的主要驱动来自哪里。
返回的大步仍必须经过原 domain-aware backtracking。
浮点 LU/SVD、行列式和条件数都是数值诊断，不是 outward 可逆性证书。

实现 SHA-256：
`e44cc2262dfbdaa97d085ab1b6bce49bad380361f9035ef3607243838945ccab`。
**本环境尚未执行此新实现，不能给它补写测试通过或新的 SH 数值。**
数组只在调用进程内/scratch 使用，Git 不保存矩阵或场。

同一实现允许 k 条高度/分支参数。对单主模的 m3 支，应取
`branch_parameters=(0,), height_modes=(0,)`，保留其余 M-1 条原 DN；
n4 默认两个坐标的选择是针对双共振。把所有 M 个高频 cut 高度都改为
Dirichlet 并无本命题提供的稳定性保证，它还会去掉高模 DN 对补块 K 的约束。

## 6. 对恢复路径的明确约束

两高度恢复即使收敛，也仍欠首两原 DN 条件和高模实际 DN。
目标高度来自历史实际解，提供的是有效分支观测；它没有自动支付尾方程。

一个更稳的条件顺序是：先把高度约束下的内部缺陷降下去；确认归一 SH 可用；
保持高度时将高模接回实际尾；然后用真实原尾重新评价**全部 M 条**原 DN、
完整 prefix metric 和原 mean/nonmean 二阶 seam。
若这些原条件已通过原门，有限方程的接受依据就是这些直接残差；
不需要为了重演旧迭代轨迹故意再作一次病态的自由 q 冷步。
若任一未过门，仍是未完成的恢复，不把 Dirichlet 条件改名成原 DN。

后续精确圆弧、全闭合、全时 reach 与固定全部参数的完整精化要求继续保留。
本条提供了一个精确消元条件和可用的分支诊断，没有把工程定支当作几何完成。
