# 任意几何点、负界 QP 修复与真实回溯（2026-11-20）

维护会话：`/root/geometry_path`。本文件对应完整小源
`scripts/resume_20261120_curvature_qp_v4a.py`，SHA256
`d3ee2f2dce84ba9401f6a993109741564c65f9317356bd2a9431b489d0a633de`。
这是原 Gauss 加权 QP 的后继；本文说明数学映射、数值方法和已执行的必要导数检查，批次终态另记。

## 改动所解决的实际问题

第二批 v3 的 12 步输出在所有原 1845 个观察位置和新 5532 个 Gauss 位置通过 $0.03D_{\rm lb}K_{\max}\le0.98$，但其真实五次 Hermite 场在 cell 821 的胞内点有 $K=8.09521095710513$，与当时采样直径下界相乘得 $0.9936530964723217$。它只超过人为设置的 $0.98$ 数值余量，尚不能推出真实 reach 不足。

v4a 继续使用完全相同的标量、同一场、原仿射端口和原 Gauss/Simpson 加权 Gram 行；额外任意点仅用于几何约束与接受检查。它不把采样曲率插值成新曲率，也不在未知点插值标量 $a$。几何六 jet 由真实参数化直接给出，不需要该处 $a$ 的新 oracle。

## 任意位置的真实六 jet

令 $h=s_{i+1}-s_i$、$s=s_i+hu$，$0\le u\le1$。使用已发布的显式五次 Hermite 权
$$
(Y,U,A)=W(h,u)(Y_i,U_i,A_i,Y_{i+1},U_{i+1},A_{i+1}).
$$
$W$ 的三行分别给函数值、一阶导、二阶导，带原有 $h$ 尺度，不作拟合或逆矩阵。

所有向量均以当前 $\phi$ 的旋转正交标架表示。令
$$
\delta(\phi)=\sum_m\frac{1-(2m)^2}{2m}c_m\sin(2m\phi),
\quad
\rho=1+\delta',\quad \rho_\phi=\delta'',
$$
$$
e_r=(\cos\delta,\sin\delta,0),\qquad
e_t=(-\sin\delta,\cos\delta,0).
$$
原密算子的 `synth` 和 `angular(order=1/2)` 包含旋转标架本身的导数。因此任意点按原式精确到浮点算术读取
$$
F=\operatorname{synth}(Y)+f e_r+\chi H e_z,
$$
$$
F_s=\operatorname{synth}(U)+f'e_r+\chi'H e_z,\quad
F_{ss}=\operatorname{synth}(A)+f''e_r+\chi''H e_z,
$$
$$
F_\phi=\operatorname{angular}(Y)+f\rho e_t,
\quad
F_{s\phi}=\operatorname{angular}(U)+f'\rho e_t,
$$
$$
F_{\phi\phi}=\operatorname{angular}(Y,2)
 +f(\rho_\phi e_t-\rho^2e_r).
$$
$\cos\delta$、$\sin\delta$ 未截断。$f,\chi$ 仍由原算子 `_lift_scalar(s)` 给出。

接口：

- `ArbitraryField(dense_source, observed_module, npz_data)`；
- `set_state(full_free_x)`，再 `fields((cell,u,phi))` 返回六 jet；
- `read(point)` 返回两条主曲率及 $2|F|$；
- `ArbitraryCoarseGeometry(field,basis).row(point,cotangent)` 将六 jet 余向量精确拉回本轮粗基。

最后一个接口不含 core 形状系数变化：本轮粗基冻结同一个 core。任意场读出本身使用传入完整自由向量的当前 core；若后继拉回完整自由空间，须继续原 core 的 $\delta,\rho,\rho_\phi$ 链，而不能把本轮粗基限制当作完整模型限制。

## 粗基的任意点导数

各粗基径向列使用相同 $W(h,u)$ 作用于其 literal nodal 三 jet；高度列再补入 $(\chi,\chi',\chi'')$，使补偿后的物理变化确为规定的平滑高度函数。

对 $\nu=2m$，三个角列的 $(h,h',h'')$ 为
$$
h_R=(\cos\nu\phi,0,0),\quad
h_R'=(-\nu\sin\nu\phi,\cos\nu\phi,0),
$$
$$
h_R''=(-(\nu^2+1)\cos\nu\phi,-2\nu\sin\nu\phi,0),
$$
$$
h_T=(0,\sin\nu\phi,0),\quad
h_T'=(-\sin\nu\phi,\nu\cos\nu\phi,0),
$$
$$
h_T''=(-2\nu\cos\nu\phi,-(\nu^2+1)\sin\nu\phi,0),
$$
$$
h_Z=(0,0,\cos\nu\phi),\quad
h_Z'=(0,0,-\nu\sin\nu\phi),\quad
h_Z''=(0,0,-\nu^2\cos\nu\phi).
$$
于是任意列的六 jet 为 $(Yh,Uh,Yh',Ah,Uh',Yh'')$。与已登记的主曲率六 jet 余向量收缩，即得该点 $d\kappa$ 的完整粗基行；$d(2|F|)=2F\cdot dF/|F|$ 同理。两个主曲率分支及各自当前符号在每个新父点重新计算。

本次真实检查用第二批 v3 输出 SHA
`3a3f77c9363ec866c4f8e12d294d226ef2f9d7bbabfbe258819a009177c8477c`，
在 cell 821、$u=0.4222489175317334$、$\phi=0.016682618776082153$，分支 0。complex-step 为 $10^{-25}$：

- 粗基 $d\kappa$ 相对误差 **3.012468273305693e-16**；
- 粗基 $d(2|F|)$ 误差 **0**；
- 当前 $\kappa=-8.095210957105094$、主曲率间隔 **6.816330826902875**；
- 与根会话已有同一 arbitrary witness 的曲率差 **0**。

该检查实际穿过完整 `basis.free_direction`、原 `unpack`、任意点六 jet 和主曲率读出，未用实现自身的线性式冒充独立验证。

## 含负界的 QP 与一般半空间修复

对每个当前曲率分支与直径下界点组合，线性行仍为
$$
Q_{ij}p=0.03\bigl(D_j\operatorname{sgn}(\kappa_i)d\kappa_i[p]
                  +|\kappa_i|dD_j[p]\bigr)
\le b_{ij}.
$$
本次方向使用 $b_{ij}=0.9798-0.03D_j|\kappa_i|$；真实接受仍要求 $0.98$。$0.0002$ 是明确的线性方向余量，不是科学完成门槛的替换。

令 $N=J^TWJ$、$g=J^TWr$。按 $s_j=\sqrt{N_{jj}}$ 的正则化尺度，$z=\operatorname{diag}(s)p$，
$$
C=\operatorname{diag}(s)^{-1}N\operatorname{diag}(s)^{-1}+\mu I.
$$
把每行 $Q\operatorname{diag}(s)^{-1}$ 归一化为 $r_i$，右端同除行范数。先对标准非负双对偶用 L-BFGS-B 求近似 QP 方向。由于本批初始已知点超过余量，部分 $b_i<0$，零方向不可行；旧版向零收缩的修复不适用。

v4a 对当前违反的半空间逐次作 $C$ 范数正交投影：
$$
z\leftarrow z-C^{-1}r_i^T
  \frac{r_i z-b_i+\epsilon}{r_iC^{-1}r_i^T}.
$$
右端的微小正 $\epsilon$ 提供向内余量。这一公式不假设 $b_i\ge0$。利用已算的 $G_{ij}=r_iC^{-1}r_j^T$ 更新全部行残差，避免重复解大系统。设置有限修复预算；最后显式重算原尺度 $Qp-b$，仅在最大值不超过 $2\times10^{-8}$ 时尝试非线性回溯。不能修复时记录失败并提高 $\mu$。投影后的方向只声称是数值可行的近似 QP 方向，不声称已证明凸 QP 的最优性。

首次实际方向有 **1111** 行，其中 **27** 行右端为负；经过 **119** 次投影，原尺度最大 $Qp-b$ 为 **-3.3729625342759917e-10**。这证明本次负界修复实现已实际用于真实模型。真实满步几何仍不合格，已被回溯拒绝；线性可行不替代真实非线性接受。

## 动态点与接受条件

保留原固定网格的拒绝峰记忆上限 32 和半径记忆上限 4。任意点另保留 12 个曲率位置和 2 个半径位置；不保留旧曲率值、旧特征向量或旧符号。每个新父点都重新读取两个分支。最多 4 个曲率起点在所属真实 cell 的 $(u,\phi)$ 闭矩形内作局部数值极值优化，并从最远点种子作一次真实半径局部优化。旧峰及当前网格峰均提供种子，靠近同一位置的记忆合并。

这些局部优化得到的是新的真实点见证，不是全胞或全域上界。每个可能接受的候选必须同时满足：

1. 完整原加权 Gram SSE 严格下降；
2. 全部保留和新增 metric 观察点的相对度量行列式为正；
3. 全部 7377 个径向位置与全角点的必要曲率乘积不超过 $0.98$；
4. 所有当前记忆任意点和本次局部优化所得点的必要乘积也不超过 $0.98$。

最初已不可行的父点只在实际恢复到上述条件后才可接受。若指定的恢复尝试次数用完，记录 `restoration_failed`，不把未恢复父点标成可行后继。

## 阻尼与模型检验

本次记录的数据目标预测下降为
$$
\Delta E_{\rm pred}(\alpha)
=-2\alpha g^Tp-\alpha^2p^TNp.
$$
这里 $N$ 不含 LM 步罚。实际比率为
$\rho=(E_w(x)-E_w(x+\alpha p))/\Delta E_{\rm pred}$，仅在分母为正时定义。

真实全步接受且 $\rho>0.75$ 才将 $\mu$ 减半；接受 $\alpha<1/4$ 则将 $\mu$ 乘 4；中间步通常保持；模型比率差时也乘 4；整条方向拒绝乘 10。这样小回溯步不会自动放大下一方向。该调整只改变求解策略，同一 $g$、原目标和真实接受条件保持不变。

此前最初的 v4 试运行在首个 trial 因 `round(phi,12)` 将 $\pi/2$ 推出闭区间约 $10^{-13}$ 而中止，未产出接受终态。v4a 对位置键的舍入结果限回原闭区间，并提前保存实际初态和导数检查；上述完整 SHA 是这份实际运行源。旧 v3 与已执行 v4 均未覆盖。

**范围**：这些是数值算法和必要条件检查。连续度量、嵌入、reach、握持振幅及所有 $t$ 的完成证明仍未获得。

