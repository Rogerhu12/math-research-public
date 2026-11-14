# R85：完整 Darboux 残差、周期发展修正与尾部 metric 的频率公式

状态：**完整的中间解析结论，以及实际固定状态数值定位。** 本文证明连续周期发展中的精确 metric 恒等式、有限角数组中的代数恒等式及其频率权。它不构造新的闭曲面，不把零补高模的局部评价当作高模联解，也不把 source-jet 采样当作最终 XYZ/Hermite 图的连续证书。

作者：Astra-visible-flex-78718bd0，`/root/independent_audit`，2026-11-10。按根 README §13 直接登记完成的数学结论，不另设独立审查或重跑门。

## 1. 记号和命题范围

设径向材料度量为

$$
g=E(r)\,dr^2+r^2\,d\theta^2,\qquad E>0,
$$

在一个开径向区间上给定实高度 $u(r,\theta)$。先假设 $E\in C^2$、$u\in C^3$，且 $u$ 关于 $\theta$ 为偶函数，并具有周期 $2\pi/m$，其中整数 $m\ge2$。这包含当前有限尾的余弦间隔 $m=3$；分段光滑的物理背景上逐开段应用本文恒等式。

记

$$
S=r^2-u_\theta^2>0,\qquad
\Delta=ES-r^2u_r^2>0,\qquad
\rho=\sqrt S,\quad \alpha=\frac{\sqrt\Delta}{\rho},
\quad\beta=-\frac{u_ru_\theta}{\rho}.
\tag{1}
$$

以下所有傅里叶系数均使用 $2\pi$ 周期，
$\widehat f_k=(2\pi)^{-1}\int_0^{2\pi} f(\theta)e^{-ik\theta}\,d\theta$。
零均值周期原函数算子 $P$ 满足

$$
\widehat{Pf}_0=0,\qquad
\widehat{Pf}_k=\frac{\widehat f_k}{ik}\quad(k\ne0),\qquad
\partial_\theta Pf=f-\langle f\rangle.
\tag{2}
$$

本文的连续结论是：从同一个高度二 jet 得到的完整 Darboux 残差，经过下面明确的两个角向原函数，恰好决定周期发展相对于理想一阶标架的径向修正；实际 metric 的 RR、RT、TT 项由这个修正精确给出。

## 2. 连接 curl 与 Darboux 残差：完整符号和归一化

定义角连接和径向连接

$$
\omega=\frac{r^2(r+u_ru_{\theta\theta}-u_\theta^2/r)}{S\sqrt\Delta},
\qquad
\mathfrak b=\frac{r^2u_r(u_{r\theta}-u_\theta/r)}{S\sqrt\Delta}.
\tag{3}
$$

材料度量的 Gauss 曲率是

$$
K_g=\frac{E'}{2rE^2}.
$$

把源程序中的 Darboux 残差写成明确的协变 Hessian 公式：

$$
\mathcal D=
\frac{(u_{rr}-\frac{E'}{2E}u_r)(u_{\theta\theta}+\frac rE u_r)
 -(u_{r\theta}-\frac1r u_\theta)^2}{Er^2}
-K_g\left(1-\frac{u_r^2}{E}-\frac{u_\theta^2}{r^2}\right).
\tag{4}
$$

则

$$
\boxed{\quad
\Omega:=\partial_r\omega-\partial_\theta\mathfrak b
 =\frac{\mathcal D E^2r^4}{\Delta^{3/2}}.
\quad}
\tag{5}
$$

为避免把归一化或符号藏在简称中，令
$a=u_r,b=u_\theta,c=u_{rr},d=u_{r\theta},e=u_{\theta\theta}$。
将 (3) 直接求导、约去共同分母后，两边共同的分子为

$$
\begin{aligned}
\Delta^{3/2}\Omega={}&Er^2(ce-d^2)+r^3ac
-\frac{E'r^2}{2}ae+2Erbd-Eb^2
-\frac{E'r}{2}(r^2-b^2).
\end{aligned}
\tag{6}
$$

求导中 $u_{r\theta\theta}$ 的两项相消，没有剩余三阶项。另一方面，把 (4) 乘以 $E^2r^4$ 并使用 $\Delta=E(r^2-b^2)-r^2a^2$，所得正是 (6)。这证明 (5)，也核定了源函数 `actualMetricFromDarbouxJets` 使用的因子。

恒等式 (5) 在 $E\in C^1,u\in C^2$ 且 (1) 严格成立时仍可作为分布恒等式使用：在任意紧子区间对 $E,u$ 平滑逼近并保持正间隙，连接 (3) 一致收敛，右边 (4)–(5) 一致收敛，弱导数极限即给 (5)。后面的经典推导在光滑开段上足够适用于本次数值定位；本文不借此断言任意保存的分段多项式自动满足全局 C² 接合。

## 3. 实际周期发展的精确径向修正

令

$$
\zeta=\langle\omega\rangle-1,
\qquad \psi=\theta+P\omega,
\qquad e_r=(\cos\psi,\sin\psi),\quad e_t=(-\sin\psi,\cos\psi).
\tag{7}
$$

定义理想水平径向向量和真实水平角向向量

$$
A=\alpha e_r+\beta e_t,\qquad T=\rho e_t.
\tag{8}
$$

因为 $u$ 具有 $2\pi/m$ 周期，$\rho,\alpha,\beta,\omega,P\omega$ 亦具有这个周期；$A,T$ 在角平移 $2\pi/m$ 后旋转同一角度。因此

$$
\langle A\rangle=\langle T\rangle=0.
\tag{9}
$$

高度为偶函数还使 $\mathfrak b$ 为奇函数，故其均值为零。由 (5) 和 (2)，

$$
\psi_r=P\omega_r=\mathfrak b+P\Omega,
\qquad \psi_\theta=\omega-\zeta.
\tag{10}
$$

下列两条只用高度一、二 jet 的恒等式是关键：

$$
\rho_r=\alpha\omega+\beta_\theta,
\qquad \alpha_\theta-\beta\omega=-\rho\mathfrak b.
\tag{11}
$$

第一条可直接展开为
$\rho_r=(r-u_\theta u_{r\theta})/\rho$。例如
$\alpha\omega=r/\rho+r^2u_ru_{\theta\theta}/\rho^3$，
而 $\beta_\theta=-(u_{r\theta}u_\theta+u_ru_{\theta\theta})/\rho-u_ru_\theta^2u_{\theta\theta}/\rho^3$，两式相加便得到它。
第二条在共同分母下化为
$-r u_r(r u_{r\theta}-u_\theta)/(\rho\sqrt\Delta)$，即右边。

设 $J$ 是水平平面的逆时针直角旋转。由 (8)–(11) 逐项求导得

$$
T_r-A_\theta=-\rho(P\Omega)e_r+\zeta JA=:C.
\tag{12}
$$

现在实际定义周期发展

$$
F(r,\theta)=\bigl(PT(r,\theta),u(r,\theta)\bigr).
\tag{13}
$$

由 (9) 和 (12)，其两个导数恰是

$$
\boxed{
F_\theta=(T,u_\theta),\qquad
F_r=(A+v,u_r),\qquad
v=PC=-P\{\rho(P\Omega)e_r\}+\zeta P(JA).
}
\tag{14}
$$

这不是把一个理想径向向量指定成导数，而是对实际定义 (13) 求导所得。尤其完整残差 (5) 在 $\zeta=0$ 时通过两个角向原函数决定径向修正。若 $\Omega=0$ 且 $\zeta=0$，则 $v=0$。

## 4. 完整 metric 公式及直接误差界

由 (1) 可直接核对

$$
|A|^2+u_r^2=E,\qquad A\cdot T+u_ru_\theta=0,
\qquad |T|^2+u_\theta^2=r^2.
\tag{15}
$$

因此在材料正交标架 $(E^{-1/2}\partial_r,r^{-1}\partial_\theta)$ 中，实际归一化 metric 误差矩阵是

$$
\boxed{
\mathsf E=
\begin{pmatrix}
\displaystyle \frac{2A\cdot v+|v|^2}{E}&
\displaystyle \frac{v\cdot T}{r\sqrt E}\\
\displaystyle \frac{v\cdot T}{r\sqrt E}&0
\end{pmatrix}.
}
\tag{16}
$$

特别地，若把两项分别记为 $a_*=\mathsf E_{rr}$、$b_*=\mathsf E_{r\theta}$，则其精确谱范数为

$$
\boxed{\quad
\|\mathsf E\|_{op}=\frac{|a_*|+\sqrt{a_*^2+4b_*^2}}2.
\quad}
\tag{17}
$$

令 $\eta=|v|/\sqrt E$。矩阵
$Q=((A,u_r)/\sqrt E,(T,u_\theta)/r)$ 的两列正交归一，而实际归一化导数矩阵是 $Q+D$，其中 $D=((v,0)/\sqrt E,0)$。所以

$$
\mathsf E=Q^TD+D^TQ+D^TD,
\qquad
\boxed{\ \|\mathsf E\|_{op}\le2\eta+\eta^2.\ }
\tag{18}
$$

这给出由完整 curl 修正控制实际一阶度量的直接界。反过来，$\|\mathsf E\|_{op}\ge |a_*|$ 且不小于 $|b_*|$。不能只观察 Darboux 残差的未加权最大值来推断 metric 大小；必须通过 (14) 的角向原函数及实际系数。

## 5. 频率公式：为什么当前遗漏模主要显在 RR

将水平向量视作复数，令

$$
G=\rho e^{i\psi},\qquad A_c=(\alpha+i\beta)e^{i\psi}.
$$

由 (14) 的卷积公式，对于 $n\ne0$，

$$
\boxed{
\widehat v_n=
\sum_{k\ne0}\frac{\widehat G_{n-k}\widehat\Omega_k}{nk}
+\frac{\zeta\widehat{A_c}_n}{n}.
}
\tag{19}
$$

$\Omega$ 的频率是 $m\mathbb Z$，$G,A_c,v$ 的频率属于 $1+m\mathbb Z$，后者不含 0。因此没有被省略的零频共振。只要右边绝对可和，就有可直接使用的上界

$$
\|v\|_\infty\le
\sum_{n\ne0}\sum_{k\ne0}
\frac{|\widehat G_{n-k}|\,|\widehat\Omega_k|}{|n|\,|k|}
+|\zeta|\sum_{n\ne0}\frac{|\widehat{A_c}_n|}{|n|}.
\tag{20}
$$

这条式子保留全部卷积，不能无条件把它简化为“每个遗漏频率都恰除以频率平方”；低频混合仍由 $\widehat G$ 决定。

在旋转背景的一阶线性化中，$G_0=r e^{i\theta}$、$A_{c,0}=e^{i\theta}$、$\zeta=0$。对一个连接残差 $\Omega=a_k\cos(k\theta)$，$k\ge2$，(19) 精确给这个线性化算子的响应

$$
e^{-i\theta}v^{lin}
=\frac{r a_k}{k^2-1}\cos(k\theta)
-i\frac{r a_k}{k(k^2-1)}\sin(k\theta).
\tag{21}
$$

把它代入 (16) 并只取一阶项，得到

$$
\boxed{
\begin{aligned}
\mathsf E_{rr}^{lin}&=\frac{2r a_k}{E(k^2-1)}\cos(k\theta),\\
\mathsf E_{r\theta}^{lin}&=-\frac{r a_k}{\sqrt E\,k(k^2-1)}\sin(k\theta),\\
\mathsf E_{\theta\theta}^{lin}&=0.
\end{aligned}}
\tag{22}
$$

因此在接近旋转背景时，遗漏高角频率的 RR 响应自然具有约二阶频率衰减，RT 还多一阶。这解释本次实际尾的“完整 Darboux 残差约 1e-5、RR metric 约 1e-9、RT 约 1e-10”的比例。式 (22) 是明确的线性化公式；本文没有在非线性候选上偷换成严格误差界，后者应使用 (16)、(19) 或 (20)。

## 6. 原有限动量方程为何消去已保留连接残差

这里先讨论精确积分、精确求根的有限 M 系统。令 $w=\sqrt{E-1}>0$、$W=w^2$，使用原尾变量

$$
u_r=w(1+K),\quad u_\theta=rwP,\quad
L=K+P_\theta,\quad U=K_\theta-P,
$$

以及 $S_0=1-WP^2$、$D_0=1-W(2K+K^2+EP^2)$。由 (3)，

$$
\omega=\frac{1+W(1+K)P_\theta/S_0}{\sqrt{D_0}},
\qquad
\mathfrak b=\frac Wr\frac{(1+K)U}{S_0\sqrt{D_0}}.
\tag{23}
$$

源 `general_root_tail_momentum.mjs` 的稳定分解 $\omega-1=W(L+q)$ 是 (23) 的代数改写。设 $\ell_j=mj$，$\varepsilon\in\{1,-1\}$，单个物理 cell 的 $\mu>0$ 固定。其角 root 强制

$$
\Pi_M(\omega-1)
=\sum_{j=1}^M\frac{\varepsilon\sqrt{12}\mu}{r^4}\pi_j\cos(\ell_j\theta),
\qquad \langle\omega-1\rangle=0,
\tag{24}
$$

这里 $\Pi_M$ 保留常数及这些余弦，$\pi_j$ 是程序里的普通余弦动量系数。定义

$$
f=\frac{(1+K)U}{S_0\sqrt{D_0}},\qquad
f_j=\langle f\sqrt2\sin(\ell_j\theta)\rangle.
$$

原方程除去径向参数速度后为

$$
\pi_j'-\frac4r\pi_j
=\frac{\varepsilon\sqrt2\,r^3W}{\sqrt{12}\mu}\ell_j f_j.
\tag{25}
$$

对 (24) 的普通余弦系数求 $r$ 导数，(25) 给
$\sqrt2(W/r)\ell_j f_j$。而 (23) 中 $\mathfrak b$ 的普通正弦系数正是 $\sqrt2(W/r)f_j$，它的角导数给同一个余弦系数。常数项由 (24) 为零，故

$$
\boxed{\quad \Pi_M\Omega=0.\quad}
\tag{26}
$$

所有高于 $mM$ 的频率仍在完整 $\Omega$ 中。减小 shooting 残差或把同一有限 ODE 积分得更准，不会使 (26) 自动扩展到遗漏频率。

实际程序使用 N 点梯形投影。即使这套离散 root 和 ODE 在精确实数算术中求解，严格成立的也是保留模中
$Q_N(\omega_r)=Q_N(D_N\mathfrak b)$，其中 $D_N$ 是离散 Fourier 导数。因此采样的连续连接残差满足

$$
\Pi_{M,N}\Omega
=\Pi_{M,N}(D_N\mathfrak b-\partial_\theta\mathfrak b).
\tag{27}
$$

右边是角采样 aliasing 项；实际浮点 root/隐式微分还有其数值误差。不能把观测到的约 1e-16 保留频率误差称作一个无需估计的精确零。当前 N 加密的实际比较正用于区分 (27) 和真正遗漏的高模。

## 7. N 点数组版本：精确代数与实际图的界限

令 $P_N$ 是源函数 `periodicPrimitiveReal` 的离散原函数：零频与 Nyquist 频置零，其余频率除以 $ik$。对同一组高度二 jet，在各节点定义 (1)、(3)、(7)、(8)，并按原程序计算

$$
v_N=P_N[-\rho(P_N\Omega)e_r+\zeta JA],
\qquad \overline T_N=\frac1N\sum_j T_j.
\tag{28}
$$

代码用于 Gram 计算的两个三维向量为
$(A+v_N,u_r)$、$(T-\overline T_N,u_\theta)$。由 (15) 的逐点代数，归一化三项准确为

$$
\begin{aligned}
a_N&=\frac{2A\cdot v_N+|v_N|^2}{E},\\
b_N&=\frac{v_N\cdot T-A\cdot\overline T_N-v_N\cdot\overline T_N}{r\sqrt E},\\
c_N&=\frac{-2T\cdot\overline T_N+|\overline T_N|^2}{r^2}.
\end{aligned}
\tag{29}
$$

其谱范数是
$\max\{|(a_N+c_N\pm\sqrt{(a_N-c_N)^2+4b_N^2})/2|\}$。
进一步令

$$
\eta_N^2=\frac{|v_N|^2}{E}+\frac{|\overline T_N|^2}{r^2},
$$

相同的 Gram 扰动证明给 $\|\mathsf E_N\|_{op}\le2\eta_N+\eta_N^2$。

即使输入具有三重对称，N512 的网格也不在 $2\pi/3$ 平移下保持不变，所以这里不删去 $\overline T_N$。其小的实际值与 TT 近舍入量级一致。

式 (28) 的 DFT 频率公式与 (19) 相同，但卷积索引按 N 循环、并使用实际零频/Nyquist 删除规则。这是原数组算法的有限代数描述。**它本身不证明这两个向量数组恰是某个所选有限 XYZ 插值图的两个导数。** 要得到实际曲面的连续 metric 结论，仍须对该图自己的导出、端点补偿和 Hermite/Fourier 多项式使用其真实导数。本文未把这一必要的数学区别变成额外流程门。

## 8. 本次实际定位：原生节点不代表内部峰

两个脚本均不运行 shooting/BVP，不改变物理层或 taper：

- [固定状态节点及局部径向加密](../scripts/78718-tail-fixed-state-metric-research.mjs)；
- [第一物理 cell 内部峰、公共角点及零补高模局部评价](../scripts/78718-tail-metric-location-research.mjs)。

M14 输入是 root 成功联解的最后尾包 `2026-11-10-78718-numerical-m14-restart8000-02_tail_0003.json.gz`；M15 输入是当前首次真正 N512 尾响应 `2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz`，尚不是完成 outer 的最终候选。参数数组只在终端内读取，报告只保存有限诊断标量。

| 固定输入 | 全部 1728 原生端点峰 | cell0 的全部 2376 个原 S32 节点峰 |
|---|---:|---:|
|M14 最后尾|6.0040053252682555e-9|8.563817432971632e-9|
|M15 首次尾|4.876884175358421e-9|1.4909764312065477e-8|

这两列说明不能从原生节点较小推断段内部也较小，亦不能把不同联解阶段的 M 值直接解释成单调误差序列。

M14 内部峰位于 cell0、stage40、rawSegment3、part7、局部 $x=0.375$，$r\simeq0.4351210262850741$。它完整复现原包 audit 的最大值；RR 为 8.563817432971632e-9、RT 最大值约 9.19e-11、TT 约 4.44e-16，径向修正长度约 4.28208e-9。在相同角点上 N512、N1024、N2048 的 metric 差不超过约 2.7e-15。

该峰的 $\Omega$ 频谱中，保留的 0 至 42 频率最大幅度约 1.50e-16；遗漏频率 45、48 的余弦幅度分别约 1.19086e-5、7.71515e-6。式 (19)–(22) 解释其主要 RR 误差及较小 RT 项。该数值频谱使用到 180 的频率定位，没有把有限频谱列表当作无限剩余项证书。

M15 首次尾内部峰位于同一 stage40、$x=0.40625$、$r\simeq0.4351418479524458$。保留至 45 的频谱幅度约 1.62e-17，遗漏 48、51 约为 2.32871e-5、2.12691e-5；同角点 N 加密差约 2.5e-15。这仍显示有限 M 来源，而非目前 N512 的角积分瓶颈。

对各自峰值的保存状态补零到更高 M，仅重算原角 root 和其局部 ODE 二 jet，得到：

| 局部 M | M14 峰状态的 metric | M15 首次峰状态的 metric |
|---|---:|---:|
|16|1.11766296e-9|9.85458604e-9|
|18|2.02009524e-10|3.40341511e-9|
|22|7.43822781e-11|2.20345746e-10|
|26|8.98925379e-12|8.68811728e-11|

补零改变新 root 解出的 $u_r$：M14 例变化达到约 1.7e-6，M15 首次例约 3.9e-6。因此这些行是**下一次数值升频的局部预测**，没有付新尾的径向连续演化、深 Robin 条件或 prefix–tail 联解。它们支持以同 g 的实际较高 M 延续为主要方向；不保证任何一行单独构成通过 2e-9 的完整候选。

## 9. 实际回执、报告和当前剩余问题

本次数值研究已经真实完成：

- M14 原生/局部加密：d79833/session67953 → 687a08，exit0，13.15 秒；[报告](../notes/2026-11-10-78718-tail-fixed-state-metric-research-01.json)。
- M15 首次原生/局部加密：c010c2/session40833 → 623300，exit0，8.215 秒；[报告](../notes/2026-11-10-78718-tail-fixed-state-metric-m15-first-01.json)。
- M14 cell0 完整原 S32 采样：cfbc92/session46139 → 014eef，exit0，17.927 秒；[报告](../notes/2026-11-10-78718-tail-metric-location-m14-01.json)。
- M15 首次 cell0 同类采样：fc528e/session27364 → c15c22，exit0，17.715 秒；[报告](../notes/2026-11-10-78718-tail-metric-location-m15-first-01.json)。

式 (5)–(6) 的代数在工具 791d61 中还实际符号化计算为两项恒等零；证明已在正文展开，这个有限计算不代替它。第一条诊断曾因缺 `CLOSING_TAIL_CACHE` 在初始化前真实 exit1（ebccce），补上已有源目录后才有上述成功运行。

更详细的径向固定初值比较及旧 M12 已有数字见[持续研究记录](../notes/2026-11-10-78718-tail-metric-error-research.md)。旧 M12 的来源只读取已有结果，没有为流程重新跑旧 solver。

现在尚需真正求出并评价同 g 的较高 M 联解，并分别控制其 source 截断和最终实际 XYZ 表示误差。本文的完整恒等式及实际频谱已明确为什么仅收紧 shooting residual、增加角求积 N 或单独加密原局部 S32 积分不能自动消掉当前遗漏角频率。
