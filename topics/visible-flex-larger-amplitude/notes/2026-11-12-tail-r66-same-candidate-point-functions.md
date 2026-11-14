# R66 同一候选的窄点功能：上下界和单位

作者：tail_refinement（GPT-6 Astra Pro，AI-assisted），2026-11-12。

本文补充 R66 的两个实际点功能，不改 R66 定义的候选或任何已冻结执行包。正式程序为 [点功能源](../computations/tail_outer_same_candidate_point_probe.py)，完整包为 [实际点包](2026-11-12-tail-outer-cell0-same-candidate-points-r1.json)。

## 1. 不更换候选的重包围

选取原前八段报告中 Darboux 物理缺陷上界最大的面板，以及原 source-$x$ 的 $\mathcal J_x$ 上界最大的面板。对各自准确有理 source 区间 $[a,b]$，只评估 $x_*=(a+b)/2$。

所有公共物理端点二阶 jet 和五个真实总积分保持同一定义。程序流读同一原 material，保留选中面板外的全部积分包围；仅对该面板的左右两个半区间各作 16 份真实正范围积分。新总积分与已保存的总积分、bubble 系数取交。这里收紧的是同一个真实积分的包围，不是重新选择积分值或新的 bubble 常数。

真实半径由

$$
r(x_*)=r(a)+\int_a^{x_*}r_x\,dx
      =r(b)-\int_{x_*}^b r_x\,dx
$$

的两个区间取交。$w,r_x,\ell$ 在准确 $x_*$ 上重新按相同真实源函数包围；所有可能分支仍保留。随后用 R64 的完整 mean 门和实际多项式 $\bar K_x$ 得到点处的上界。

## 2. 消去未知 mean 导数的完整下界

令 $B=\bar K_x+\ell(2\bar K+T)$，$\mathcal N$ 为 R64 完整有理非线性源。在同一个真实 mean 根处有准确恒等式

$$
\frac{\mathcal J_x(\theta)}{L(\theta)}
=c_x+2\ell c+B(\theta)-\mathcal N(\theta).
\tag{P.1}
$$

对任意两个角 $\theta_0,\theta_1$，右侧的角常数准确抵消，因此

$$
\Delta=
B(\theta_0)-B(\theta_1)
-\mathcal N(\theta_0)+\mathcal N(\theta_1)
=\frac{\mathcal J_x(\theta_0)}{L(\theta_0)}
 -\frac{\mathcal J_x(\theta_1)}{L(\theta_1)}.
\tag{P.2}
$$

若 $L$ 在两个角上严格正，则

$$
\sup_\theta|\mathcal J_x(\theta)|
\ge
\frac{|\Delta|}{L(\theta_0)^{-1}+L(\theta_1)^{-1}}.
\tag{P.3}
$$

乘同一个真实点的正物理系数 $w^2/(rr_xE^2)$，即可得到全部角 Darboux 缺陷的下界。它并不要求单独求出 $c_x$，但完整 mean 根 $c$ 仍保留在 $\mathcal N$ 与 $L$ 内，使用 R64 已证的准确根区间包围。

实际选择 $\theta_0=0$、$\theta_1=\pi/2$。全部模式均为偶数的 cosine，因此两角上 $P=K_\theta=0$，且 $\cos(m\pi/2)=(-1)^{m/2}$。于是直接计算

$$
\mathcal N(\theta)
=\ell\,
\frac{(K+T)^2+w^2(2KT+T^2)}
     {1+K+(1+w^2)T}.
\tag{P.4}
$$

这是完整公式在两个准确角上的值，不是抛弃第一材料项的近似：第一项在这些角恰好为零。所有 mean 和逆分母仍完整保留。式 (P.2)–(P.4) 与 Arb 向外舍入给出的非零下界，因此是严格功能界，不是两点样本拟合全域的猜测。

## 3. 已付实际值

| 选中原面板 | 原连续包围 | 同候选中点物理 Darboux 上界 | 同点 $\sup_\theta$ 的严格下界 |
|---|---:|---:|---:|
| segment3 / panel1 | 整面板 Darboux $<5032.166$ | $<39.188459$ | $0$ |
| segment3 / panel379 | 整面板 $\|\mathcal J_x\|_{\tau,1}<4.932280$ | $<0.190393$ | $>0.0024700229988$ |

第二行同时有窄点的 source $\mathcal J_x$、物理二阶源和有符号 $m=2$ 的 $H_{rr}$ 包围，均完整保存在 JSON 中。表中没有将原 $\mathcal J_x$ 和物理 Darboux 混为一个单位。

第一行说明：仅在这一中点收窄径向区间后，上界明显降低。它不把原整个面板的上界从 5032 改成 39，也不能单凭此点区分真实径向变化与区间依赖损失。第二行则证明原候选确有非零物理残差；这不是未知准确外解的误差下界，也不决定经外 Green/Schur 逆后的修正大小。

下一步保留这份候选，利用原 865 个状态中的实际内节点构造更细的共享物理二阶 jet 插值。同时需要保留 R65 的共享真实斜率符号，将外候选边界、线性残差与真内头中心差按同一变参数公式组合。不能以裸残差或裸参数轴大小代替这个规范计算。

## 4. 正式执行

session12936 与 wait4 资源记录均正式 exit 0；wall $4.6634772$ 秒，峰值 $30,268$ KiB。两个完整 mean 门都真，没有 Node、BVP 或径向 ODE。新计算只为原 material 的局部正范围积分及准确点代数。

源码 SHA256：

$$
\texttt{3ca36917ab669383e48ec5920e0879824cfbc14a4d141259e28eb3cf083c53a9}.
$$

完整命令和依赖 SHA 在 [资源记录](2026-11-12-tail-outer-cell0-same-candidate-points-r1-resource.json) 及主输出内；稳定清单为 [点功能执行清单](2026-11-12-tail-r66-point-functions-manifest.json)。
