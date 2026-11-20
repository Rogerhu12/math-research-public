# R138 补篇：实际短根段积分排除所选 GB 的径向权根预算

2026-11-20，visible-exact-astra-ac637-20261120。

**已证明的限定路线排除。** 公开 [Actions 44758362539/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44758362539) 完成唯一新短根段积分上界，两个声明的排除门均为 true。它排除 [RS](R138-supplement-radial-weight-independent-root-budget-screen.md) 所规定、保留原 GB 体误差预算的整类径向权和自由外截段根接收器充分门。它不排真实可达根迹，不证明原边值问题奇异，也不授完整逆或本课题完成。

## 1. 完整实际结果与唯一新标量

运行事件提交为 `6329adde0dd0e885480ab178b82bae22717aafb6`，实际科学 checkout 为 `b064b78d05c52fde0eb07a78529e7651b99ba776`。

| 完整文件 | Bytes | SHA256 |
|---|---:|---|
| [科学结果](../notes/radial_weight_root_budget_screen_ci/run-44758362539-1/radial-weight-root-budget-screen.json) | 17278 | `e1b27ffa5759b9b55bc785ef17d362a67f1d370d5ae26e68b422922d9a0229d8` |
| [execution](../notes/radial_weight_root_budget_screen_ci/run-44758362539-1/execution.json) | 18290 | `ba15b1060c40e965b27cc325c7696a35202dbf54c83817dbfb508750acdf8f1c` |
| [运行报告](../notes/radial_weight_root_budget_screen_ci/run-44758362539-1/report.md) | 774 | `83ade513b55b08b93e5e731308f9b064eda2a945e809c129ca5f4b941644dd92` |

新目标是原真实 $r_*$ 上、固定长度 $ell=1/100$ 的正积分的一个完整 upper：

$$
T\ \ge\ \int_{r_*}^{r_*+1/100}
 \frac{222}{125}\min_{\epsilon\in\{+,-\}}
 \frac{|v_\epsilon(r)|}{1+K(r)v_\epsilon(r)^2}
 \left\{\frac{(26/25)^2}{\eta(r)\ell^2}
 +385^2\eta(r)K(r)\left(1-\frac{r-r_*}{\ell}\right)^2\right\}\,dr,
\tag{RA.1}
$$

其中 $v_+=v(r,0)$、$v_-=v(r,\pi/4)$，$eta=-\gamma m$ 是原真实输运速度，不是固定 intrinsic 参数 $eta_0$。原 $26/25$ 和 $385$ 是 RS 的已证解析放宽，不是本次另算的范数。

保存的完整 decimal ball 为

```json
{
  "kind": "complete_decimal_ball_v1",
  "mathematical_direction": "upper",
  "midpoint_integer": "12410400206991460480430391581646463892281227988128198130783886266804381267948029",
  "radius_integer": "2",
  "decimal_exponent": "-77"
}
```

其含义是保存的上界数 $T$ 属于 $(m+[-2,2])10^{-77}$，其中 $m$ 是上表整数；因此严格 $T<125<160<225$。显示值约为 $124.1040020699$。这个数字是积分的上界，不是原积分或最优容量的下界。

`integral_prefix` 与 `complete_test_integral` 在最终原件中逐字相同，前者只是同一目标的累计断点。程序先保存该完整球并读回，再比较上端与 225、160；两门分别为 true，没有把 partial sum 当作完整积分。

## 2. 所用旧对象与完整覆盖

新消费者始终使用同一 candidate `ac1d5b98…`、连续修补 `440866a3…`、原 $alpha,\nu_0,\eta_0$ 和 fixed point $(0,0,1/2)$。保持原 low1..96、高 $j\ge97$、独立 moving mean 和原物理角；两个反射轴上 moving 角与物理角准确相同。

真实根区间没有改成中点：

$$
r_*\in\left[
\frac{1191984371497}{5000000000000},
\frac{2383968743003}{10000000000000}\right].
$$

新积分的保守覆盖是该下端至 $2483968743003/10000000000000$。覆盖共 **327 个原共同片、10464 个完整子片**：首片保整个 root germ，其余 326 片取原 positive 交集，每片固定 32 个精确有理子片。最后一个子片右端与声明的完整右端相同。新分区的完整 metadata SHA256 是 `bb8770fda129870ef3c7e143ceb93f499a155827b51a949c8be9cc6bcb17a2fc`。

原 positive 的 **4650 个闭行和 3594 个接口**先完整准入；新目标没有将局部摘录冒成完整旧输入。四个 positive 历史分件、五个候选 cubic 分件和一个 root germ 均按原 bytes/SHA/Git blob 恢复。根对 27 个当前输入和 10 项恢复回执逐项核同公开 manifest；没有重新调用旧生产器。

两个新轴投影只读取原 exact dyadic cubic 定义。候选 mean 由原整行或完整 germ 的 signed 球提供；原全修补 $A_0<4\cdot10^{-18}$ 分别给全 $v_\pm$ 和独立 $m$ 的一次误差，不删 mean、不重复付同一轴修补。每个子片沿用原 parent 的完整 $\gamma,K,m$ 球，未因细分而无依据缩窄系数。首 germ 对真正 $r\ge r_*$ 的部分使用已证 $K\ge0$；额外覆盖只加非负 majorant，不声称根左侧也为正曲率。

全 old high41、原 signed96/97 三项、X、GB 及其 execution 仅读。嵌套的完整 two-mode、X、axis、mean 身份保留；原负方向、high 正性与全部未付范围都不改变。

## 3. 实际排除了什么

对原完整根型使用任意合法的有限低频接收器 $W$，即使以真正 $D_H^{-1}$ 消元而非统一 scalar high 下界，[RS.3–5](R138-supplement-radial-weight-independent-root-budget-screen.md) 仍给

$$
\|Wz_{96}\|^2>148.
$$

对任意正径向权、任意自由外截段，准确容量的测试函数及完整 root dual 给

$$
\alpha_E(W)^2>\frac{148\Lambda^2}{T},
\tag{RA.2}
$$

其中 $\Lambda=\Gamma$ 对应原 LC 全域转授；若替换为两项合法的双向 scalar Jacobian 比较，其平方根之积仍 $\Lambda\ge1$。特定角向接收行的非 scalar 变换不在此声明中。

原 GB 选择的已保存费用满足 $a_{EE}^{GB}>11/10$。它是该**所选上界预算**的数值事实，不是原实际误差或所有预算的下界。现在 $T<160$，故即使取 $\Lambda=1$，仍有

$$
a_{EE}^{GB}+\alpha_E(W)^2
>\frac{11}{10}+\frac{148}{160}
=\frac{81}{40}>2.
\tag{RA.3}
$$

所以该类充分门的第一条吸收条件已经失败；其余完整 $H$ source、mean 费用和交叉费用不能抵消这个非负成本。原 $\Gamma>59/50$ 的门也被排除。结论覆盖准确有限 Gram、完整 high Schur、径向权选择和自由截段，不需要继续为同一预算制作那些矩阵或容量表。

如果改变原 GB 体费用，则这是另一条预算。保存球还给一个方便的必要筛查：由 $T<125$，任何这种替代费用 $a_{EE}^{new}$ 若仍使用上述 scalar 转授并欲通过第一门，必须有

$$
a_{EE}^{new}<2-\frac{148}{125}=\frac{102}{125}.
\tag{RA.4}
$$

若保留原 $\Gamma>59/50$，更须

$$
a_{EE}^{new}
<2-\frac{148(59/50)^2}{125}
=\frac{27453}{78125}.
\tag{RA.5}
$$

这些只是不再消费新科学目标的有理必要比较，不宣称某个替代预算达到它们。更紧的体费用、原 PDE 的可达根约束、联合有符号根/体处理和直接逆仍需各自完整证明。

## 4. 复核与后继范围

本次固定 Python3.12.14、python-flint0.9.0、numpy2.3.5、320bit；唯一科学 child returncode0，数学阶段 1.9111419639999951 秒，child 共 2.041096616999994 秒。旧目标调用、新数组、artifact、Release 均为 0。公共 worker 记录 5 次 pull/README 检查；保存的 first/latest-three 回执差异为空。当前会话再次 pull 后核两个 README 仍无变化；本篇不声称独立重建未保存在 execution 中的中间 receipt。

| 入口 | Bytes | SHA256 |
|---|---:|---|
| [science](../scripts/fourfold_codazzi_radial_weight_root_budget_screen.py) | 25276 | `c411610ffc855e748c3e3d76ab880c0c0ae1503db753bde38b6f27fb3be8c102` |
| [worker](../scripts/fourfold_codazzi_radial_weight_root_budget_screen_public_worker.py) | 34548 | `157003d10ec8a48b35fb21b9f630a9ef892c01fbcdf242e19ae3f32271ce9dc7` |
| [manifest](../notes/2026-11-20-R138-radial-weight-root-budget-screen-inputs.json) | 14917 | `8a7a96d9b2ff97568f19aa0389f8ffbb2134603a7df96c23aed41eb3c4254360` |
| [合同](../notes/2026-11-20-R138-radial-weight-root-budget-screen-contract.md) | 12320 | `aeb4f0ed2432680cc450ecaa0410cdaef1d555eae401ae5cc573667523a581a6` |

这个完整新目标已完成并冻结，后继只读其整结果。不能把两个排除门改成逆的成功门；不能把这个障碍当本课题完成。R141 的实际低 Green/完整误差与物理外块、原两条 RHS、负区/germ/全 matching 和最终固定度量闭嵌入族继续是实际工作。
