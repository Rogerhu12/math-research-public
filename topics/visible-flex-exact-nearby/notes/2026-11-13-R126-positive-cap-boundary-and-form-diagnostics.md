# R126 续记：正侧 Cauchy 放大、实际帽切口和未删减的源接口

2026-11-13。本文延续同一固定目标 $g_0=E(r)dr^2+a(r)^2d\theta^2$、
同一准确仿射中心和原来的腰圈初值。**数值部分全是浮点有限模型诊断，
不是正帽存在或连续 PDE 证书。** §3–4 的代数恒等式是准确的。
R127 对短负曲率段的连续验证不使用本篇未经验证的正侧端点。

## 1. 实际续算及明确失败量

旧 R88/R105/R111 的正帽物理接口是 $c=1/4$，graft 终点是 $25/8$。
本次从已经保存的 $r=.239$、1024 点两场/框架状态出发，继续同一
去混叠 Codazzi 系统至 $r=.25$。正侧仍使用

$$
B_r=\frac{\sqrt E}{a}\partial_\theta\frac{K_0+B^2}{C}
       -2\frac{a'}aB,
\qquad
C_r=\frac{\sqrt E}{a}B_\theta
       +\frac{a'}a\left(\frac{K_0+B^2}{C}-C\right).
$$

没有除以 $K_0$，但正曲率区不适用 R126 的负曲率对称化能量。
`fourfold_phase_codazzi_resume_probe.py` 的本次参数为
`--right .25 --samples 45 --max-step .00005`，其余容差沿用冻结脚本。
计算实际完成，不等于连续解通过。

第二次计算把**同一个** $.239$ 的 1024 点状态先投影为512点后再续算。
原 $B,C$ 被删除的 $256\le |k|<512$ 系数绝对和分别约为
$5.82312\times10^{-5}$、$6.88208\times10^{-5}$。这不是零尾；
投影脚本和报告把14个状态列的删除量全部保存。

| 端点/模型 | $K_0$ | 采样 $\min|C|$ | 实际位置度量残差 | 实际位置 $\|q\|_\infty$ |
|---|---:|---:|---:|---:|
| $.239$,1024 | $.0330822361$ | $.420759913$ | 约 $8\times10^{-12}$ | $1.15475\times10^{-8}$ |
| $.25$,1024 | $.1718274660$ | $.167877867$ | $5.67182\times10^{-7}$ | $.021260698$ |
| $.25$,先截到512 | 同上 | $.240975229$ | $4.46409\times10^{-6}$ | $.098063422$ |

本表源的末列采用端点状态的**双倍角格**和真实位置导数。
512模型自己原角格的最大源约为 $.0497018$，双倍格已经观察到
$.0980635$；这直接说明不能将角节点最大值授予整个圆。
原续算的45个径向节点也没有连续径向误差证书。

1024模型的 $B,C$ 在 $256\le |k|<512$ 带的系数绝对和，到 $.25$
分别增长至 $.54830422$ 和 $.50531721$。512/1024两个模型在公共
$128\le |k|<256$ 带的差分别约 $.29428220$、$.24422549$。
低带差较小：$1\le |k|<4$ 的 $B,C$ 差约
$1.58383\times10^{-5}$、$3.61490\times10^{-7}$；但这不补偿未闭合的高角尾。

因此，原初腰圈 Cauchy 诊断虽能有限维穿过首根，当前 forward 端点
**不提供**可认证的 $.25$ 帽迹。观察结果既不证明 $C$ 真正到零，
也不证明目标度量或附近精确闭面的不存在。

## 2. 放大的精确主符号来源

令 $\gamma=\sqrt E/a$、$A=(K_0+B^2)/C$。两场系统的角主矩阵是

$$
\gamma\begin{pmatrix}2B/C&-A/C\\1&0\end{pmatrix}.
$$

在 $K_0>0$ 时其特征值为
$\gamma(B\pm i\sqrt{K_0})/C$。
冻结系数并取物理角频率 $\mu=4k$，$\partial_\theta$ 变为 $i\mu$，
于是两个径向指数中有一个实部为
$|\mu|\gamma\sqrt{K_0}/|C|$。这是正侧初值演化的局部高频放大率；
它是主符号的准确结论，**不是**变系数非线性解的一个已证增长下界。
$.239$ 和 $.25$ 的1024状态上，此倍率的采样上确界分别约
$.484064$、$2.770836$。正侧去混叠不能消除这个初值问题的主符号。

## 3. 实际 principal form 的比较不能只看位移小

对任一旧/新浸入，在固定材料坐标记

$$
Z=F_\theta\times F_r,\quad G=|Z|^2,\quad S=F\cdot Z,
\quad (L,M,N)=Z\cdot(F_{rr},F_{r\theta},F_{\theta\theta}).
$$

当 $S>0,N<0,F_z>0,K_0>0$，同一目标改型的 grounded 密度矩阵准确为

$$
\widehat{\mathsf B}
=\frac{F_z^2}{S^2}
\begin{pmatrix}
-N&M\\ M&-(M^2+K_0G^2)/N
\end{pmatrix}
=\begin{pmatrix}\alpha&\alpha b\\
\alpha b&\alpha b^2+\kappa\end{pmatrix},
$$

$$
\alpha=-\frac{F_z^2N}{S^2}>0,\quad
b=-M/N,\quad
\kappa=-\frac{F_z^2K_0G^2}{NS^2}>0.
$$

真实未改型矩阵的右下项是 $-F_z^2L/S^2$。两者在真实等距
$g_F=g_0$ 时相等；对浮点候选须分别记录，不能预先等同。

对两个上述正定矩阵，准确令

$$
T_0=\begin{pmatrix}\alpha_0^{-1/2}&-b_0\kappa_0^{-1/2}\\
0&\kappa_0^{-1/2}\end{pmatrix},\qquad
T_0^t\widehat{\mathsf B}_0T_0=I.
$$

新矩阵的相对广义特征值由 $Q=T_0^t\widehat{\mathsf B}_1T_0$ 给出，且

$$
\operatorname{tr}Q=
\frac{\alpha_1}{\alpha_0}+\frac{\kappa_1}{\kappa_0}
+\frac{\alpha_1(b_1-b_0)^2}{\kappa_0},
\qquad
\det Q=\frac{\alpha_1\kappa_1}{\alpha_0\kappa_0}.
$$

这由直接相乘得到。尤其近共同简单根，若其他几何量有非零有限极限，
$\kappa_0$ 与 $K_0$ 同阶；当 $b_1-b_0$ 的极限非零时，最大相对特征值
以 $K_0^{-1}$ 的量级发散。故共同型别/共同根本身不支付原角图中
更新算子的相对 form 比较。此处的帽证书从 $c=.25$ 开始；上述根邻域
现象不是给 R111 原证明添加一个不存在的错误。

在本次双倍格上，旧改型到新改型的相对特征值范围约为

| 端点/模型 | 相对特征值范围 | 相对 form 差 |
|---|---:|---:|
| $.239$,1024 | $[.15962275,6.23086200]$ | $5.23086200$ |
| $.25$,1024 | $[.16168155,6.11103368]$ | $5.11103368$ |
| $.25$,512 | $[.16125260,6.11425413]$ | $5.11425413$ |

$.239$ 的新实际矩阵和新改型矩阵在显示精度内一致，与其小曲率残差相符；
相对差仍为5.23。因此该差不是仅由 $.25$ 的坏高频残差制造。
$.239$ 的材料位移 $C^0$ 仅约 $.000233724$，原诱导 $C^1$ 约 $.010947541$；
小位移不推出旧 principal form 的小相对变化。表中的5倍量完全不能
代替 R111/R121 已支付的、仅比较原仿射参数族的约 $.0114$ 预算。
本篇也没有计算新表面在整个 $[.25,25/8]$ 上的 form。

## 4. 带全部源与 regular 端口的正确边界等式

令 $F_1=F_0+V$，$f_0=g_0-g_{F_0}$。若 $F_1$ 真等距 $g_0$，准确有

$$
Dg_{F_0}V=f_0-dV\cdot dV.
$$

令 $u_0=F_0/|F_0|$、$\rho_0=1/|F_0|$，在旧球面材料图定义线性源
$q_0(f)=-\tfrac12\mathcal C_{\sigma_0}(\rho_0^2f)$，径向面积密度为
$j_0$。R32 的完整真实算子满足

$$
P_0w=j_0q_0(f_0-dV\cdot dV),
\qquad w=u_0\cdot V.
$$

在正帽取 $Y=F_{0,z}/|F_0|>0$、$U=w/Y=F_0\cdot V/F_{0,z}$。
令 $\omega_0=c_0-\widehat c_0$ 为 R37/R88 的实际角主系数修正，
$\ell=Y_\theta/Y$。直接展开可得

$$
Y(P_0-\widehat P_0)(YU)
=\partial_\theta(Y^2\omega_0U_\theta),
$$

因为 $Y(\omega_0Y_\theta)_\theta
=Y^2[(\omega_0\ell)_\theta+\omega_0\ell^2]$，所有零阶项准确相消。
因此正确的旧参考强制帽方程是

$$
\boxed{
\operatorname{div}(\widehat{\mathsf B}_0\nabla U)
=Yj_0q_0(f_0-dV\cdot dV)
-\partial_\theta(Y^2\omega_0U_\theta).
}
$$

在 $r=c$ 进入正帽的外法向是 $-\partial_r$，其准确 grounded 外流为

$$
p_{\rm out}=-\widehat{\mathsf B}_{0,rr}U_r
            -\widehat{\mathsf B}_{0,r\theta}U_\theta.
$$

若 $F_1$ 还有度量误差 $e_1=g_{F_1}-g_0$，强制项须再加
$Yj_0q_0(e_1)$。这说明本次浮点有限差的 $(U,p_{\rm out})$ 不是一个
无源 Jacobi 帽迹。忽略 $dV\cdot dV$、固定型别修正或 $e_1$ 都会
改变实际问题。

给定完整强制密度 $S_U$ 后，设 $H_z$ 是旧帽相同真实尾的齐次延拓，
其输入 $z=(g,\xi)$ 包含内端完整角迹和外端 regular mean。若
外端规则写为真实非均值 Robin 加独立 mean 共轭流，Green 恒等式给

$$
\langle (p_{\rm out},\lambda),z\rangle
=\langle S_{0,\Gamma}(U(c),\xi_U),z\rangle
+\int_{\mathrm{cap}}S_UH_z.
$$

证明是把实际 $U$ 分解为相同增广边界输入的齐次延拓及零输入强制解，
再用对称能量 form；零输入解与任意 $H_z$ 的能量配对为零。
若源用分部积分后的两迹写法输入，R74 的端点项仍必须一并保留。
所以完整强制 particular 和 regular 输入未给出时，不能只拿一个
有限旧帽 DN 矩阵与当前内端高度比较。

本次后处理保存全部采样角谱、$U_r,U_\theta,p_{\rm out}$，并保留均值：
1024模型在 $.25$ 有

$$
\langle U\rangle\approx-3.465883\times10^{-5},\qquad
\langle p_{\rm out}\rangle\approx1.902769\times10^{-4}.
$$

regular trace/flux 字段明确为 `null`，强制 particular 明确未计算。
这些值没有被擅自设为零或授予无源 DN。

## 5. 文件和重放范围

新脚本：

- `scripts/fourfold_phase_codazzi_endpoint_projection.py`；
- `scripts/fourfold_phase_codazzi_cap_trace_probe.py`。

续算使用已经冻结的 `scripts/fourfold_phase_codazzi_resume_probe.py` 和
`scripts/fourfold_phase_codazzi_evolution_probe.py`，没有修改它们。

新报告/状态：

- `notes/2026-11-13-codazzi-to-cap-cut-n1024-floating.json`；
- `notes/2026-11-13-codazzi-to-cap-cut-n1024-endpoint-floating.npz`；
- `notes/2026-11-13-codazzi-at-r0239-projected-n512-floating.json`；
- `notes/2026-11-13-codazzi-at-r0239-projected-n512-endpoint-floating.npz`；
- `notes/2026-11-13-codazzi-to-cap-cut-projected-n512-floating.json`；
- `notes/2026-11-13-codazzi-to-cap-cut-projected-n512-endpoint-floating.npz`；
- `notes/2026-11-13-codazzi-positive-cap-traces-floating.json`；
- `notes/2026-11-13-codazzi-positive-cap-traces-spectra-floating.npz.gz`。

完整文件 SHA256、字节数及所消费原对象/旧端点的 SHA256 记在
`notes/2026-11-13-R126-positive-cap-diagnostic-manifest.json`。
源报告也各自记录直接依赖。频谱压缩包是全体所列**采样**字段的 DFT；
有理字段的未见无限尾不因保存了整个数组而变成已知。

这批文件冻结。后续两端边值候选若调整腰圈曲率，须另立文件并标明
改变的初值，不能替换当前固定腰圈分支或 R127 的原输入合同。
