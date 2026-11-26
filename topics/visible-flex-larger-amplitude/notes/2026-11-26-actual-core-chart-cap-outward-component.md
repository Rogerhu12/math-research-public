# 同一实际 SO(3) 场的全角 core 正性、真实逆图与 cap 六 jet 误差

本稿给出一个完整的条件性区间消费器及其证明。它不把尚未执行的源当成实际证书，也不把有限角节点的费用当成全域 metric 或 reach 证明。执行对象限于已刊 `606e0048…` 完整 driver 与 `7f26ff35…` 完整 operator 所定义的同一实际 independent-axisymmetric $h\Delta$ 场；不是 zero-closure 分支的来源适配。

源码为 `so3_axisymmetric_core_cap_outward.py`。它严格消费 `a846d373…` 的 `ActualInput` 和 `1371e493…` 的完整 `NodeOutwardEvaluator`，继续核全部 report、checkpoint、原参考输入、固定标量目标、完整 core、omega、H、原模型及实际 operator 源。本文所列科学算法尚未在本组件上运行；当前完成的是源码、代数证明及静态解析核查。

## 1. 实际数学对象和角变量

记完整当前 core 系数为 $c=(c_1,\ldots,c_M)$，完整原固定图系数为 $c^0$，

$$
 p_c(u)=1+\sum_{m=1}^M c_m\cos(2mu),\qquad
 \rho_c(u)=p_c(u)+p_c''(u)
 =1+\sum_{m=1}^M(1-4m^2)c_m\cos(2mu),
$$

$$
 \Theta_c(u)=u+\sum_{m=1}^M\frac{1-4m^2}{2m}c_m\sin(2mu),
 \qquad \Theta_c'=\rho_c.
$$

这些 $c_m$ 是实际 checkpoint 的每一个 binary64 字的精确有理值；首三个固定系数和其余全部自由系数都保留。固定图为

$$
 \theta_0(\phi)=\Theta_{c^0}(\phi),\quad
 \rho_0(\phi)=\rho_{c^0}(\phi),\quad
 \rho'_0(\phi)=\rho'_{c^0}(\phi).
$$

当前逆图是唯一实数 lift $u=u(\phi)$ 满足

$$
 \Theta_c(u)=\theta_0(\phi).
$$

`chart_for_core(core,phi)` 返回的 `er/et` 是在 **$\Theta_{core}(\phi)$** 的 frame。因此当前曲线 $\Gamma$ 必须另用 `normal_frame(u)` 的普通 $e_r(u),e_t(u)$。cap 才使用 `fixed_chart(phi)` 返回的 $e_r(\theta_0),e_t(\theta_0)$。源码明确分开这两次调用。

## 2. 全角正下界，包含完整覆盖而非样点最小值

对任一完整 core，先计算精确有理数

$$
 L_c=1-\sum_{m=1}^M |(1-4m^2)c_m|,
 \qquad U_c=1+\sum_{m=1}^M |(1-4m^2)c_m|.
$$

三角函数绝对值至多一，故对所有实 $u$ 有 $L_c\leq\rho_c(u)\leq U_c$。只有 $L_c>0$ 时才使用此捷径。

否则精确分割有理区间 $x\in[0,2]$，每一片代表真实角区间 $u=\pi x$。真实 $\pi$ 用已刊 e091 整数区间包住；乘以每片的精确有理端点后，再对全部有限 Fourier 项使用该来源的完整正弦/余弦区间。每次先把两个子片都完整算出，再替换父片。因此无论自然预算在何时停止，已存分区都仍完整覆盖 $[0,2\pi]$，没有删去困难角片。

各片 lower 的最小值与精确 $L_c$ 取较大者，给出全角 lower；各片 upper 的最大值与 $U_c$ 取较小者，给出全角 upper。源码还核分区的首末端点及每对相邻片的精确相接。有限整数 Fourier 模式的周期性将此证书延伸到整个实轴。

`all_circle_complete` 表示上下界的覆盖完整；`certified_positive` 才表示已经证得严格正 lower。若预算结束且 lower 仍非正，这既不证明真正有负 $\rho$，也不允许后续 `evaluate` 输出已认证的逆图。当前 core 和固定图分别执行此证明，二者均正后才能消费六 jet。

## 3. 单一实数 lift 的存在、唯一性及初始根盒

若全实轴 $\rho_c\geq\delta>0$，则 $\Theta_c$ 严格递增。又 $\Theta_c(u)-u$ 是有界有限三角多项式，所以其在两端趋向 $\pm\infty$。因此它是实轴到实轴的双射；逆函数光滑。

对任意候选实数 $\widehat u$，以完整整数区间计算真方程残差

$$
 [r]=\Theta_c(\widehat u)-\theta_0(\phi).
$$

平均值定理给出

$$
 |u-\widehat u|\leq \frac{\max|[r]|}{\delta}.
$$

由此得到同一个唯一实根的初始闭盒。候选可以很差，或者与正确根差一个周期，此论证仍成立。实现比较 literal $\phi$ 与从实际 `Gammaphi` 提议的一个 plain `atan2` 字的认证残差界，采用较小者。这里不假设 `atan2` 的精度，也不使用浮点 wrap 把不同 lift 自动视为相同。

特别地，候选生成不参与数学正确性的前提：真正支付候选误差的是独立重读的完整 $\Theta_c-\theta_0$ 区间。

## 4. 区间 Newton 与严格保持同一根

设当前闭盒 $I$ 包含该唯一根，取精确有理中点 $m$。对整个 $I$ 的 $\rho_c$ 做完整区间求值，再与已证明的全实区间 $[\delta,U_c]$ 相交，得到正区间 $D$。则

$$
 u\in m-\frac{[\Theta_c(m)-\theta_0]}{D}.
$$

与旧 $I$ 取交保留同一根。若真残差盒严格为正，根在 $m$ 左侧；若严格为负，则在右侧，可再取相应单调 bracket。源码每轮保存旧盒、真残差、完整正导数区间、Newton 像与新盒。

所有除法以 exact Fraction 端点先作有理运算，再向外舍入到整数 SCALE。因此即使一个已证明的极小正 lower 被固定 SCALE 向下舍入为零，也不以零作分母或伪称失去数学正性。

迭代预算或当前整数精度不能继续缩小时，结果仍是包含真根的完整盒；`tolerance_reached` 独立报告是否达到请求半径。宽盒可以给出较大的真误差费用，不能被改成零。

## 5. 当前曲线和 cap 的六个真 jet

令 $e_r(u)=(\cos u,\sin u,0)$，$e_t(u)=(-\sin u,\cos u,0)$。完整当前曲线是

$$
 \Gamma=p_c(u)e_r(u)+p'_c(u)e_t(u).
$$

对普通法向角 $u$ 有 $\partial_u\Gamma=\rho_c e_t$，而

$$
 u_\phi=\rho_0/\rho_c(u).
$$

因此

$$
 \Gamma_\phi=\rho_0 e_t(u),\qquad
 \Gamma_{\phi\phi}=\rho'_0e_t(u)-\frac{\rho_0^2}{\rho_c(u)}e_r(u).
$$

完整 $p_c,p'_c$ 在真根盒上逐 Fourier 项求值，分母使用同盒正 $\rho_c$ 的完整区间与全角正界。没有遗漏当前自由 core 链，也没有把 $u$ 换成 $\Theta_c(u)$。

cap 半径 $R$ 直接消费实际完整 `4e65` 参考模型的 `radius_complete_enclosure`，其准确字串端点与固定目标、全部来源身份一起绑定；不重跑尾积分，也不将 numerical $q.R$ 当作真半径。当前 $H$ 是实际自由量的 exact binary64 字。

$$
 P=R e_r(\theta_0)+H e_z,
 \qquad P_\phi=R\rho_0 e_t(\theta_0),
$$

$$
 P_{\phi\phi}=R\bigl(\rho'_0 e_t(\theta_0)-\rho_0^2 e_r(\theta_0)\bigr).
$$

故以上六组整数向外盒都是真对象的完整包围。原半径积分是否达到它曾请求的更小 tolerance 与本论证不同：只要其已绑定完整真盒有效，整个盒宽都会进入当前费用，不因 `tolerance_reached=False` 自动变成无效或自动当成零误差。

## 6. 对实际完整工作重读支付误差

本组件实际调用 byte-bound `7f26` 的完整 `_core_and_cap`，输入当前全部自由向量及同一 literal $\phi$，读取每个 $(A,3)$ 工作数组。它不复制或简化这个工作函数，也不宣称先前 solver 的 BLAS 批次逐字重现。

若某个真实分量在 $[a_j,b_j]$，实际 reread 工作字为 $w_j$，则

$$
 \epsilon_j=\max(|a_j-w_j|,|b_j-w_j|),\qquad
 \epsilon=\sqrt{\sum_{j=1}^3\epsilon_j^2}.
$$

这里 $w_j$ 也被转换为它本身的精确 binary64 有理值，平方根使用已刊 exact-rational 上界算法。故 $\epsilon$ 支付完整真六 jet 对该实际重读数组的 Euclidean 误差。当前逆图、真固定图、全部 Fourier 项、真实 $R$ 对 numerical carrier、当前 $H$、三角函数、除法和逐分量浮点运算都已经包含在这一整输出差额中。

若实际工作函数的 Newton 未通过其原检查，或工作值非有限，组件记录失败，不输出零费用。此处没有假设浮点三角函数正确舍入，也没有把一个浮点残差当成真残差。

## 7. 调用合同与剩余责任

构造 `CoreCapOutward(actual, node_evaluator)`，先 `certify_charts()`，再 `evaluate(phi)`。主要返回值如下。

| 字段 | 完整语义 |
|---|---|
| `working` | 六键 `Gamma`, `Gammaphi`, `Gammaphiphi`, `P`, `Pphi`, `Pphiphi`，每个为 actual float64 $(A,3)$ |
| `intervals` | 同六键，每个为 `(lower, upper)` 两个 SCALE 整数 object 数组，形状 $(A,3)$ |
| `component_error_upper` | 同六键，每个为 exact Fraction $(A,3)$ |
| `norm_error_upper` | 同六键，每个为 exact Fraction $(A,)$ |
| `fixed_chart.rho0` | 真 $\rho_0$ 的 `(lower, upper)` 整数数组，形状 $(A,)$；另有 `theta0`、`rho0_phi` |
| `inverse_certificates` | 每个 literal $\phi$ 的同一全实唯一根盒、真残差、Newton 历史和 tolerance 状态 |
| 两份 whole-circle certificate | 当前 core 与固定图各自完整覆盖/严格正性/准确 lower、upper 及全部分区 |

命令行默认完整消费原实际工作角数组；显式请求只能按 canonical binary64 hex 给出，并不冒称覆盖原全角节点。完整原始费用、根盒和区间留在 runner 的逐块 journal；自然预算返回只把已处理节点的 maxima 当作局部 maxima。

这个组件尚不支付 $\int T$、$\int T_\phi$、$\int T_{\phi\phi}$ 的 quadrature，也不支付它们与 $\Gamma,P,h\Delta$ 组合时的工作算术、真实 $h,h',h''$ carrier 差异或最终 Gram 运算。将有限角费用延伸到连续角区间、全域 metric、全 $t$ 几何和同固定目标的实际精化仍是后继完整消费者的责任。

这些未付责任保留在每份输出中。不存在以当前组件退出、全角 $\rho>0$ 或六 jet 有限节点误差为本课题完成的声明。

完整源 SHA256 `69c5aae0dea9c15645a4484b3e4bfe9d6809f2a922763ca91c623774fd1e4bb2`，35220B；root完整审读、construction核实际工作接口与六数组、geometry核全角覆盖和真逆根链。完整600秒参数仅ready，尚未执行科学，不能预填任何正性或误差数值。
