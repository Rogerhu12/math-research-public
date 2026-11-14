# 2026-11-08 独立审查：direct rotational band 的导数、Jacobian 与小配置重跑

审查会话：Astra-visible-flex-effcccee / audit_phase_bound；GPT-6 Astra Pro，AI-assisted。审查者未参与被审求解器的编写或原始搜索。

## 结论与范围

**本次中间实现核对 PASS，未发现致命公式 bug。** 我核对了实际 Cartesian 坐标、移动极坐标基中的一阶与全部二阶导数、三个度量分量、相对度量 operator norm、主曲率、$C^2$ 端点、中心 mode-2 系数消元、解析 Jacobian 和 Hessian 罚项；另在指定独立目录重跑了小配置。

**这不是完成验收。** 当前对象是带边环带，最终采样相对度量误差约 $.07750$，并非达到 $10^{-6}$ 的等距解；没有闭合、全域嵌入、全时间 reach、全刚体形变量或固定度量加密证书。代码把这些标志设为 `False` 是正确的。

尤其需要保留：**即使 `vary_mean=False`，搜索也改变 $\bar E(r)$。** 本次初始与最终平均 $E$ 的最大相对差为 $.13545239809592227$；最终解相对于初始平均度量的采样误差为 $.14181148366177054$。因此不能将不同 cells/modes 或不同搜索终点的较小缺陷排列为“同一固定 metric 的加密收敛”。

## 1. 被审版本和独立产物

被审文件：[explore_direct_rotational_band.py](../scripts/explore_direct_rotational_band.py)。SHA-256：

`00607808b109c793aa9313425b10491657551727e796246fd49ce0332ba5a2fa`

独立重跑采用 NumPy `2.3.5`、SciPy `1.17.0`，命令为：

```bash
python scripts/explore_direct_rotational_band.py --cells 10 --modes 2 --amplitude .06 --max-nfev 60 --out notes/independent_direct_band_m2n10
python notes/independent_direct_band_m2n10/independent_checks.py
```

其他参数沿用脚本默认值：$a=.25,b=.95$、基准 height$=.25$、ripple$=.025$、`vary_mean=False`、`hessian_limit=0`。默认小配置重跑未启用 Hessian 罚项；罚项分支另以独立扰动状态、`vary_mean=True`、limit$=1$、weight$=2.3$ 核对。

| 独立产物 | 作用 |
|---|---|
| [summary.json](independent_direct_band_m2n10/summary.json) | 指定小配置的完整求解器报告 |
| [checkpoint.npz](independent_direct_band_m2n10/checkpoint.npz) | 独立生成的系数和离散参数 |
| [independent_checks.py](independent_direct_band_m2n10/independent_checks.py) | 独立实际坐标差分、Jacobian、端点及矩阵特征值检查 |
| [independent_checks.json](independent_direct_band_m2n10/independent_checks.json) | 所有检查步长、误差、active-set 变化和平均度量漂移 |
| [comparison_to_root.json](independent_direct_band_m2n10/comparison_to_root.json) | 与原始小配置的只读比较 |

独立重跑的 `coefficients`、`free_variables`、`knots`、`blocks`、`radial_grid`、`theta` 与 root 的 `notes/direct-band-a006-m2-n10/checkpoint.npz` **逐项完全一致**，系数最大差为零。求解器结果完全一致，summary 中双方共有的初始/最终数值字段也完全一致。原始 summary 少了后来添加的 Hessian-component 字段，故整个字典直接比较为不同；没有共同数值字段的差异。

## 2. 实际 Cartesian 映射和所有导数

记 $e_r=(\cos\theta,\sin\theta,0)$、$e_\theta=(-\sin\theta,\cos\theta,0)$、$e_z=(0,0,1)$。脚本中的 `evaluate` 返回的是**实际 Cartesian 导数向量在当前 $\theta$ 的移动正交基中的分量**，而不是固定 $x,y,z$ 分量。位置公式为

$$F=(r+u)e_r+v e_\theta+Z e_z,\qquad Z=H+w,$$

其中可选 mean-height 块直接加进 $w$。实际三维位置是

$$F_x=(r+u)\cos\theta-v\sin\theta,\quad
F_y=(r+u)\sin\theta+v\cos\theta,\quad F_z=Z.$$

利用 $\partial_\theta e_r=e_\theta$、$\partial_\theta e_\theta=-e_r$，应有以下移动基分量：

| 导数 | $e_r$ 分量 | $e_\theta$ 分量 | $e_z$ 分量 |
|---|---|---|---|
| $F$ | $r+u$ | $v$ | $Z$ |
| $F_r$ | $1+u_r$ | $v_r$ | $Z_r$ |
| $F_\theta$ | $u_\theta-v$ | $r+u+v_\theta$ | $w_\theta$ |
| $F_{rr}$ | $u_{rr}$ | $v_{rr}$ | $Z_{rr}$ |
| $F_{r\theta}$ | $u_{r\theta}-v_r$ | $1+u_r+v_{r\theta}$ | $w_{r\theta}$ |
| $F_{\theta\theta}$ | $u_{\theta\theta}-2v_\theta-(r+u)$ | $2u_\theta+v_{\theta\theta}-v$ | $w_{\theta\theta}$ |

逐块代入 $u_m(r)\cos(m\theta)$、$v_m(r)\sin(m\theta)$、$w_m(r)\cos(m\theta)$，与 `operators` 的所有矩阵相符。特别是二阶角导数中的 $-1$、$2m$ 项和 $F_{r\theta}$ 的基准 $e_\theta$ 项都没有遗漏。可选 `('h',0)` 块只产生竖向径向导数，角导数为零，也正确。

`kron(B, angular_column)` 的行序是先径向、后角度；`repeat(r,nt)`、角平均投影与 dense-grid reshape 使用同一顺序，没有索引错位。

基准高度中的 quintic smoothstep 与 $\sin^4(\pi x)\sin(4\pi x)$ 的一、二阶导数及 $L^{-1},L^{-2}$ 链式因子也正确。

### 独立实际三维差分

复核代码不调用源 `operators` 或 `evaluate` 来生成差分位置。它把每个系数块放入独立的 scalar `BSpline`，仅求值基函数，再直接用上面的 $F_x,F_y,F_z$ 公式生成三维点。用四阶中心差分分别求 $r,\theta$ 的一、二阶与混合导数，然后与已旋转到固定 Cartesian 基的源导数比较。

测试包含两个状态：所有 Fourier 系数块都非零的扰动状态；以及额外启用 mean-height 块的独立扰动状态。每个状态检查 20 个远离径向 knots 的 $(r,\theta)$ 点，用四档步长。每种导数在这些步长中的最佳最大绝对向量误差如下：

| 项 | 普通全非零状态 | 含 mean-height 状态 |
|---|---:|---:|
| 位置 | $1.15\times10^{-16}$ | $1.25\times10^{-16}$ |
| $F_r$ | $3.97\times10^{-12}$ | $3.45\times10^{-12}$ |
| $F_\theta$ | $4.47\times10^{-13}$ | $3.41\times10^{-13}$ |
| $F_{rr}$ | $5.36\times10^{-9}$ | $4.85\times10^{-9}$ |
| $F_{r\theta}$ | $6.72\times10^{-10}$ | $7.66\times10^{-10}$ |
| $F_{\theta\theta}$ | $9.91\times10^{-11}$ | $1.13\times10^{-10}$ |

径向差分先表现为四阶误差下降，进一步缩小二阶差分步长后出现舍入放大，符合预期。这里是实现交叉核对，不是对连续域误差的区间证书。

## 3. 度量、角平均和相对 operator norm

移动基在每一点为右手正交基，因此直接对该基中的导数分量做点积可得真实

$$E=F_r\cdot F_r,\quad F_{\rm met}=F_r\cdot F_\theta,\quad G=F_\theta\cdot F_\theta.$$

独立位置差分所得三分量与解析值吻合：最佳最大绝对误差分别不超过 $6.14\times10^{-12}$、$2.15\times10^{-12}$、$6.99\times10^{-13}$。

源残差实际是

$$\left(W_E P E,\ W_F F_{\rm met},\ W_G(G-r^2)\right),$$

其中 $P$ 对每个径向行去掉角平均，$W_E=1/(1+H'^2)$、$W_F=1/(r\sqrt{1+H'^2})$、$W_G=1/r^2$ 是固定基准高度导出的**搜索权重**。它们不是每一步实际平均度量的系数，也不需要在对未知系数求 Jacobian 时微分。

diagnostic 使用当前状态的

$$g_0=\operatorname{diag}(\bar E(r),r^2),\qquad
\bar E=\frac1{N_\theta}\sum_\theta E(r,\theta),$$

并计算

$$Q=g_0^{-1/2}(g-g_0)g_0^{-1/2}
=\begin{pmatrix}
(E-\bar E)/\bar E & F_{\rm met}/\sqrt{\bar E r^2}\\
F_{\rm met}/\sqrt{\bar E r^2} & (G-r^2)/r^2
\end{pmatrix}.$$

两个对称特征值的绝对值最大值就是所需相对 operator norm；代码中的闭式 $2\times2$ 特征值公式正确。

本配置最高 Fourier 频率为 $2\,\text{modes}$，度量三分量最高频率不超过 $4\,\text{modes}$。默认均匀角点数大于这个值，所以在精确算术下离散角平均等于该有限 Fourier 函数的真实零频系数；这里没有 mean aliasing。若以后手动传更少的 `angular`，应维持这一条件。

在相同 $161\times64$ 网格，我把源向量转到实际 Cartesian 基，重建第一基本形式，再用 `numpy.linalg.eigvalsh` 独立计算相对矩阵谱范数。初始值与源 diagnostic 相同；最终最大值差仅 $9.72\times10^{-17}$。

## 4. 主曲率核对

代码使用

$$N=\frac{F_r\times F_\theta}{|F_r\times F_\theta|},\quad
\ell=N\cdot F_{rr},\quad m=N\cdot F_{r\theta},\quad n=N\cdot F_{\theta\theta},$$

$$\mathcal H=\frac{G\ell-2F_{\rm met}m+En}{2(EG-F_{\rm met}^2)},\qquad
\mathcal K=\frac{\ell n-m^2}{EG-F_{\rm met}^2}.$$

两个主曲率为 $\mathcal H\pm\sqrt{\mathcal H^2-\mathcal K}$，故它们绝对值的最大值为

$$|\mathcal H|+\sqrt{\mathcal H^2-\mathcal K}.$$

公式、法向符号约定与移动基叉乘均正确。`maximum(0,H*H-K)` 处理浮点舍入；它不是对退化或非浸入点的认证。本次检查的最小 Gram 特征值约 $.0625>0$，未出现此类采样退化。

独立核对用第一基本形式的 Cholesky 分解 $g=LL^T$，对对称矩阵 $L^{-1}\mathrm{II}L^{-T}$ 求特征值，与闭式曲率比较。$161\times64$ 网格上逐点误差不超过 $6.04\times10^{-14}$；最终最大绝对主曲率差为 $2.67\times10^{-15}$。

最终采样值为

$$\max |\kappa_i|\simeq7.214851352290911,\qquad
\min |\kappa_i|^{-1}\simeq.1386029941812277.$$

这里的后者实际是“最大绝对主曲率倒数”，即采样最小主曲率半径。它不是 reach 下界；全局自接近可能产生更小 reach，且采样可能漏掉更大的曲率。源标签 `sampled` 和 `reach_certified=False` 必须保留。

原始初始 diagnostic 用 $81\times32$ 网格，曲率最大值约 $10.98650743$；本次同网格尺寸对比使用 $161\times64$ 后，初始最大值为 $11.01957183$。这只是采样分辨率差异，不能把不同网格的两个初始数字视为实现不一致。

## 5. $C^2$ 端点与固定 mode-2 振幅

径向采用 degree-5 的 clamped open-knot B-spline。保留的基函数索引从 3 到 `nall-4`；这些基函数在两个端点的值、一阶、二阶导数都为零。因而全部 $u,v,w$ 及可选 mean-height 扰动具有零二阶 jet。

基准 smoothstep 满足 $H(a)=0,H(b)=\mathrm{height}$、$H'(a)=H'(b)=H''(a)=H''(b)=0$；ripple 在端点至少五阶消失。按解析公式，两端因此与各自的平面环领匹配 $C^2$。明确端点导数为

$$F=(r,0,H),\quad F_r=(1,0,0),\quad F_\theta=(0,r,0),$$

$$F_{rr}=0,\quad F_{r\theta}=(0,1,0),\quad F_{\theta\theta}=(-r,0,0),$$

均用移动基表示。独立检查中 B-spline 的三档端点 jet 数值均为零；完整公式最大残差约 $7.40\times10^{-47}$，来自浮点三角函数在端点对解析零的求值。这不是全曲面闭合证明；两圈仍是环带边界。

令中心 $r_c=(a+b)/2$ 的 retained B-spline 值为 $b_j$。代码挑 $b_p>0$ 最大的一个 pivot，把 mode-2 高度系数写成

$$c_p=\frac{A-\sum_{j\ne p}b_jc_j}{b_p}.$$

故解析线性关系保证

$$\sum_j b_jc_j=A.$$

稀疏仿射消元 $c=c_0+Tx$ 正确实现了它；其他块保持自由。独立检查得到中心约束行乘 $T$ 为零，初始、最终、全块扰动以及 `vary_mean=True` 状态的中心振幅误差不超过 $6.94\times10^{-18}$。这确实是硬线性消元，不是 soft penalty。

“精确”应理解为解析消元定义，而非把全部 binary64 运算都当作无舍入恒等式。checkpoint 本身没有经有理/区间重验的严格恒等证书。

此外，$A$ 只是竖向 mode-2 Fourier 系数；它不是整个闭曲面的 $\delta$，也不是已经除掉材料滑动和刚体运动的形变量。

## 6. 解析 Jacobian

令 $M_r^i,M_\theta^i$ 为对 full coefficient 的相应线性导数矩阵。三个度量分量的导数应为

$$D_cE=2\sum_i\operatorname{diag}((F_r)_i)M_r^i,$$

$$D_cF_{\rm met}=\sum_i\left[\operatorname{diag}((F_\theta)_i)M_r^i+
\operatorname{diag}((F_r)_i)M_\theta^i\right],$$

$$D_cG=2\sum_i\operatorname{diag}((F_\theta)_i)M_\theta^i.$$

代码先施加固定权重、角投影，再右乘同一个消元矩阵 $T$，顺序正确；没有漏掉 pivot 系数对其余变量的依赖。可选 mean-height 块也包含在这些矩阵中。

在初始、最终和独立全块扰动状态分别取不同随机方向，中心方向差分与解析 $Jv$ 的最佳相对 $L^2$ 误差为

$$7.14\times10^{-14},\quad5.60\times10^{-14},\quad5.55\times10^{-14}$$

量级，所有三块均吻合。因为不启用罚项时残差是未知系数的二次函数，固定方向中心差分的截断误差理论上抵消；误差由浮点舍入主导，符合实测。

## 7. Cartesian 参数域 Hessian 罚项

这里的 Hessian 是把同一映射看成圆环平面 $(x,y)=(r\cos\theta,r\sin\theta)$ 上的向量值函数。令该平面的正交方向为 $e_r,e_\theta$，则真正的 Cartesian-domain Hessian 分量为

$$Q_{rr}=F_{rr},$$

$$Q_{r\theta}=\frac1rF_{r\theta}-\frac1{r^2}F_\theta,$$

$$Q_{\theta\theta}=\frac1{r^2}F_{\theta\theta}+\frac1rF_r.$$

两个连接项及所有 $r$ 因子都正确。不能直接把 $F_{r\theta}$ 或 $F_{\theta\theta}$ 当成平面单位正交方向中的 Hessian。

独立检查在每个测试点固定其平面 Cartesian 方向 $e_r,e_\theta$，沿**直线位移**取位置差分，而不是沿圆弧或移动方向取差分。三个分量的最佳最大绝对误差分别不超过 $4.79\times10^{-9}$、$2.18\times10^{-9}$、$4.78\times10^{-10}$，包含 mean-height 分支。

对一个分量 $Q$，源罚项残差为

$$p(x)=\eta\max\{0,\|Q(x)\|^2/L^2-1\},$$

其中 $Q(x)$ 对自由变量仿射线性，$L=\mathrm{hessian\_limit}>0$。在 active 区域，正确导数为

$$Dp=\frac{2\eta}{L^2}\,Q\cdot DQ;$$

在 inactive 区域为零。代码的 `hmat`、active mask 与最后的 $T$ 链式乘积恰好给出这一公式。

独立测试使用 limit$=1$、weight$=2.3$ 和 `vary_mean=True`。三个分量分别有 $1070/210$、$88/1192$、$280/1000$ 个 active/inactive 行，故不是只测了罚项全部为零的情形。两个独立随机方向在步长 $10^{-4}$ 至 $10^{-7}$ 均保持 active set；最佳整体相对误差为 $1.68\times10^{-13}$ 和 $1.72\times10^{-13}$，三个罚项块各自也在约 $10^{-13}$ 量级。

步长 $10^{-3}$ 时部分行穿过 hinge，出现约 $.00349$ 或 $.00963$ 的整体差分差异，并记录了 active-set 改变。残差在阈值上不可微；该现象不是漏 Jacobian 项。代码在恰等于阈值处采用零分支，是一个明确的单侧/广义导数选择。

此罚项控制的是三个 Hessian **分量**的范数，并非自动把 Hessian operator norm 压到 $L$。即便三项都满足 $\|Q_{ij}\|\le L$，Frobenius 量也只得到

$$\sqrt{\|Q_{rr}\|^2+2\|Q_{r\theta}\|^2+\|Q_{\theta\theta}\|^2}\le2L.$$

此外它是离散节点上的 soft penalty，不是硬全域界，也不是主曲率或 reach 证书。

## 8. 独立重跑结果及停止条件

| 指标 | 独立结果 |
|---|---:|
| 自由未知数 | 62 |
| 度量残差行数 | 3840 |
| 函数求值数 | 36，未用满 60 |
| 终止原因 | `ftol` termination condition is satisfied |
| least-squares cost | $.5528084991108371$ |
| reported optimality | $5.039671069803475\times10^{-6}$ |
| 最终 dense-grid | $161\times64$ |
| 最终最大相对度量谱误差 | $.0774985745598186$ |
| 最终 $E-\bar E$ 相对分量 | $.03474793770416216$ |
| 最终混合分量 | $.06772476743501003$ |
| 最终角向分量 | $.05601775501830864$ |
| 最终采样最大绝对主曲率 | $7.214851352290911$ |
| 最终采样最小 Gram determinant | $.0625$ |
| 最终采样最小 polar angular Jacobian | $.0625$ |

`success=True` 在这里只表示局部优化满足停止条件，不表示残差小于任务阈值，更不表示精确方程已解。最终高度采样范围约为 $[-.0011210051,.2513179555]$；代码本身没有提供封帽、全局自交或 height-order 认证。

## 9. 为什么不能称固定度量加密

残差将 $E$ 的角平均投影掉，所以只要求它趋于某个**由当前系数决定**的径向函数 $\bar E_x(r)$。因此拟合的候选目标是

$$g_x=\bar E_x(r)\,dr^2+r^2\,d\theta^2,$$

而不是优化开始前给定并冻结的同一个 $g$。`vary_mean` 仅控制是否允许额外的平均高度形状块，不控制是否冻结 $\bar E$。

在相同 $161\times64$ 评估网格上，独立量化为：

| 量 | 值 |
|---|---:|
| 初始 $\bar E$ 范围 | $[1, 2.250912077112116]$ |
| 最终 $\bar E$ 范围 | $[.980354415495734, 2.366315385132836]$ |
| $\max|\bar E_{final}-\bar E_{initial}|$ | $.16366644997066215$ |
| $\max|\bar E_{final}-\bar E_{initial}|/\bar E_{initial}$ | $.13545239809592227$ |
| 最终相对其自身平均 metric 的误差 | $.07749857455981869$ |
| 最终相对初始平均 metric 的误差 | $.14181148366177054$ |

后续若找到更好的候选，应明确保存并冻结完整 $\bar E(r)$ 定义、几何参数及相位范围，再围绕同一个 target metric 做径向/Fourier/时间加密。当前搜索本身不能支付 README 的固定几何收敛门。

## 10. 本次审查能支持什么

可以支持：当前指定版本的导数、诊断和 Jacobian 与数学公式及独立差分吻合；小配置结果可由未参与者复现；C² 端点和中心 mode-2 消元的解析结构正确；探索所得的较大残差与可变平均度量已被如实识别。

不能支持：连续域误差界、整个环带或封闭组装的嵌入、reach 下界、宏观刚体商距离、精确等距存在或固定 metric 的收敛。若报告这次工作，应将它归为**独立复现的探索性失败/未完成候选**，继续研究，不能作为本题收尾。
