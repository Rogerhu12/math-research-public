# 两条 Codazzi 方程遗漏角模的实际有限消费者

状态：**公式已推导；实现仅是有限求解辅助残差，数值检查另列。**
本件不修改原 Gauss/Codazzi 方程，不把增加的有限行当成连续角向或径向证书。
强目标的实际 Cartesian 图、连续误差和闭接合仍按 R119/R124/R129 支付。

源：`scripts/fd2d_gc_codazzi_complement.py`。
检查入口：`scripts/fd2d-metric-codazzi-complement-check.py`。

## 1. 同一个实际场与原有限方程

设计算径向坐标为 $x$，物理坐标为 $s=S(x)$，$J=S_x>0$；
物理材料角为 $u=U(x,\xi)$，$\omega=U_\xi>0$，
$v=U_x/U_\xi$。本消费者所支持的两类外参数均保持 $U$ 固定：

- `positive_clock` / `legacy_coast` 的物理 coast 参数 $T$；
- `physical_bumps` 的固定物理 $s=x$、$J=1$ 及半径扰动参数 $\delta$。

目标为 $ds^2+a(s)^2du^2$，$c=a_s/a$。独立第二形式场顺序一直是
$(n,m,l)$；本件在任何地方都不由 $n$ 除出 $l$。
令有限 Fourier 修正为 $(\nu,\mu,\lambda)$，实际准确函数 lifting 为
$L=(L_n,L_m,L_l)$，于是
$$
(n,m,l)=(\nu,\mu,\lambda)+L.
$$
$\nu,\lambda$ 用偶基 $E=(1,\cos2\xi,\ldots,\cos2K\xi)$，
$\mu$ 用奇基 $O=(\sin2\xi,\ldots,\sin2K\xi)$；
$E_\xi,O_\xi$ 是它们的真实角导。
令 $P_E,P_O$ 是同一个已保存角网格上的 Fourier 投影，
$H_E=I-EP_E$、$H_O=I-OP_O$。

修正的完整节点右端是
$$
\begin{aligned}
f_n&=\frac{J}{a\omega}(\mu_\xi+L_{m,\xi})
       +Jc(\lambda+L_l-\nu-L_n)
       +v(\nu_\xi+L_{n,\xi})-L_{n,x},\\
f_m&=\frac{J}{a\omega}(\lambda_\xi+L_{l,\xi})
       -2Jc(\mu+L_m)
       +v(\mu_\xi+L_{m,\xi})-L_{m,x}.
\end{aligned}
$$
原程序对 $P_Ef_n,P_Of_m$ 作每格端点梯形平均。
修正的径向差商本身完全在原有限基空间内，故其遗漏角模为零。
因而在 $[x_j,x_{j+1}]$ 上新增的准确有限补充行是
$$
\mathcal C_{n,j}=-\tfrac12 H_E(f_n(x_j)+f_n(x_{j+1})),\qquad
\mathcal C_{m,j}=-\tfrac12 H_O(f_m(x_j)+f_m(x_{j+1})).
$$
这里没有额外的格长因子：原方程已使用除以格长的径向差商。
这保留原两条方程的全部分量；它不重求原 ODE，也不改变网格上场的定义。

## 2. 先消准确保留项，再作高模投影

记 $p=J/a$、$\gamma=Jc$、$z=1/\omega-1$。将右端写成
$$
\begin{aligned}
f_n &=p\mu_\xi+\gamma(\lambda-\nu)+B_n,\\
f_m &=p\lambda_\xi-2\gamma\mu+B_m,
\end{aligned}
$$
其中
$$
\begin{aligned}
F_n&=\frac p\omega L_{m,\xi}+\gamma(L_l-L_n)
           +vL_{n,\xi}-L_{n,x},\\
F_m&=\frac p\omega L_{l,\xi}-2\gamma L_m
           +vL_{m,\xi}-L_{m,x},\\
B_n&=pz\mu_\xi+v\nu_\xi+F_n,\\
B_m&=pz\lambda_\xi+v\mu_\xi+F_m.
\end{aligned}
$$
上式中 $p,\gamma$ 与角无关，且微分将奇基送到偶基、偶基送到奇基。
所以严格有 $H_Ef_n=H_EB_n$、$H_Of_m=H_OB_m$。
实现使用此恒等式，未设任何删去“小系数”的阈值。
当 $U=\xi$ 时 $z=v=0$，所有修正场的高模 Jacobian 列准确为零。
这省去由浮点 $P_EE-I$ 舍入制造的大量稠密非零存储。
检查器仍另外构造完整 $f_n,f_m$，记录直接投影与先消项投影的舍入差。

## 3. 修正场的完整稀疏 Jacobian

每个节点的高模导数，以 $(\nu,\mu,\lambda)$ 系数为列块，是
$$
\begin{aligned}
D_y(H_E f_n)&=
 \bigl[H_E(vE_\xi),\ pH_E(zO_\xi),\ 0\bigr],\\
D_y(H_O f_m)&=
 \bigl[0,\ H_O(vO_\xi),\ pH_O(zE_\xi)\bigr].
\end{aligned}
$$
每个节点只进入左右相邻格，系数均为 $-1/2$。
代码逐节点组装 COO 后转 CSC；不会构造全局稠密 Jacobian。
中央参数在独立原生节点变量下的这些列为零；若 caller 强制中央边界
$y_0=Cc$，应由其原有边界消元把 $D_{y_0}C$ 加到中央参数方向，不能
误解为中央几何变化没有影响。

## 4. 尾和物理目标参数的完整导数

对任一尾参数、$T$ 或 bump 参数 $\theta$，固定 $x,\xi,U$ 和修正系数。
实际 profile/lifting 提供
$a_\theta,c_\theta,J_\theta,L_\theta,L_{x\theta},L_{\xi\theta}$。
定义
$$
p_\theta=\frac{J_\theta}{a}-\frac{Ja_\theta}{a^2},\qquad
q_\theta=p_\theta/\omega,\qquad
\gamma_\theta=J_\theta c+Jc_\theta.
$$
则
$$
\begin{aligned}
(F_n)_\theta={}&q_\theta L_{m,\xi}
 +\frac p\omega L_{m,\xi\theta}
 +\gamma_\theta(L_l-L_n)+\gamma(L_{l,\theta}-L_{n,\theta})
 +vL_{n,\xi\theta}-L_{n,x\theta},\\
(F_m)_\theta={}&q_\theta L_{l,\xi}
 +\frac p\omega L_{l,\xi\theta}
 -2\gamma_\theta L_m-2\gamma L_{m,\theta}
 +vL_{m,\xi\theta}-L_{m,x\theta},\\
(B_n)_\theta={}&p_\theta z\mu_\xi+(F_n)_\theta,\\
(B_m)_\theta={}&p_\theta z\lambda_\xi+(F_m)_\theta.
\end{aligned}
$$
施加同一 $H_E,H_O$ 和相邻格平均即得参数列。
尾参数有 $a_\theta=c_\theta=J_\theta=0$；物理 bump 有 $J=1$、
$J_\theta=0$。两者不与 $T$ 混用。

### 4.1 冻结的旧 T provider 缺少两个暴露字段时

原 provider 已定义真实尾参数 jets，只未暴露 $L_{x\theta},L_{\xi\theta}$。
新 helper 可以按完全相同的 lifting 公式计算它们，不修改原源。
设尾曲率 $\kappa(y;b)$、$y=a\sin U$，
$$
V=(\cos^2U,-\sin U\cos U,\sin^2U),\qquad
W_\theta=V\kappa_\theta(y).
$$
则
$$
\begin{aligned}
(W_x)_\theta&=V\kappa_{y\theta}y_x+V_U\kappa_\theta U_x,\\
(W_\xi)_\theta&=V\kappa_{y\theta}y_\xi+V_U\kappa_\theta U_\xi.
\end{aligned}
$$
若实际 lifting 权为 $w(x)$，则
$L_\theta=wW_\theta$、
$L_{x\theta}=w_xW_\theta+w(W_x)_\theta$、
$L_{\xi\theta}=w(W_\xi)_\theta$。
已暴露这些 jets 的 `RawBumpDAE` 直接读取原值。

## 5. 调用及参数身份

```python
from fd2d_gc_codazzi_complement import codazzi_complement

F, J, data = problem.evaluate(vector, jacobian=True)
extra = codazzi_complement(problem, vector, weight=0.3, data=data)
# F 和 J 仍由原求解器单独记录；extra 只供候选分支 merit/方向使用。
```

返回 `residual`, `jacobian` (CSC), `info`，另有有限节点诊断数组
`node_rhs`, `omitted_node_rhs`, `omitted_codazzi_cells`。
残差按“径向格、n 方程全部角、m 方程全部角”排列，乘
`weight*sqrt(2/angular_work)`，与原 Gauss complement 的角向缩放一致。

普通 coast 模型必须由 `AnalyticTRawLiftedDAE` 或提供等价明确
`analytic_T(vector,data=...)` 的对象给出解析 T jets；没有时直接说明缺字段，
不回退到可能离开物理域的 T 差分。
物理 bump 模型读取明确的 `tail_parameter_slice`、
`profile_parameter_slice`，以及实际 `a_parameters/c_parameters` 和
`profile_parameters/profile_x_parameters/profile_xi_parameters`。
它支持未知数与原方程数不同的矩形原生系统，Jacobian 列数采用实际
`problem.size`；不会假定最后一个参数是 $T$。

## 6. 可信度边界

这里补的是同一有限角网格遗漏的 Fourier 投影分量。全部角之间的函数、
节点之间的实际 residual、实际积分位置图的 Gram/曲率和完整闭缝都未由此得到界。
梯形格的低模和高模同时小仍不是连续证书；径向积分可能有自己的漏算。
外参数 $T$ 或 $\delta$ 改变物理度量，只能称外几何设计；之后的真正
同 $g$ 加密必须固定这些参数。代码不新增曲率光滑性或验收标准。

## 7. 本次实际执行

以下均实际退出 0，检查期间 helper/provider 源字节未变，原完整 $F$ 和
独立三场变化逐位为 0。没有重新求 BVP 或积分 body，也没有把输入初猜称为解。

| 输入与执行 | 节点 / 模数 | 非零方向 | $h=10^{-6}$ 时真实相对 $L^2$ JVP 误差 |
|---|---:|---|---:|
| 原 K15 输入 `...local-recovery01-k15.npz`；43283 / f9ac44；13.727 s | 113 / 15 | 独立 $(n,m,l)$ 节点 | $3.310\cdot10^{-9}$ |
| 同上 | 同上 | 尾参数 | $8.183\cdot10^{-9}$ |
| 同上 | 同上 | 实际物理 $T$ | $1.171\cdot10^{-8}$ |
| `...raw-bump-jvp01-warm.npz`；58332 / 2aa5f1；30.234 s | 100 / 15 | 独立 $(n,m,l)$ 节点 | $3.886\cdot10^{-9}$ |
| 同上 | 同上 | 尾参数 | $2.155\cdot10^{-8}$ |
| 同上 | 同上 | 物理 $\delta$ | $4.919\cdot10^{-9}$ |

前者准确绑定原 `a92b...` 候选和 $T=.02$；后者准确绑定新的
`7c3f...` 物理候选与自身 supports，并另明示诊断点
$\delta_j=.0003\cos(.7+1.3j)$。这不是求解器 accepted 状态。
两个输入没有交叉转借候选或把最后一个 bump 参数误当成 $T$。

完整节点 RHS 投影重现原 `codazzi_cells`，最大差分别
$8.882\cdot10^{-15}$、$1.066\cdot10^{-14}$；先消准确 retained 项与
直接浮点高模投影差分别 $3.991\cdot10^{-14}$、$2.977\cdot10^{-14}$。
实际六个方向都非零。检查报告同时给绝对、除以
$\max(1,\|Jd\|_2)$ 的 scaled 和真实 relative 误差，未混用这两种归一。
稀疏 Jacobian 分别有 3,621,457 和 2,383,304 个非零项。

复现命令在各退出回执；报告：

- `notes/2026-11-12-fd2d-metric-codazzi-complement-T-check-01.json`；
- `notes/2026-11-12-fd2d-metric-codazzi-complement-bump-check-01.json`。


