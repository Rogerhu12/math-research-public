# R673. 完整正谱方向的阻尼能量、活动面误差界与真实射线后继

日期：2026-11-20。会话：Astra-larger-resume-24b2ab87-20261120 / fullclosed_solver。

状态：下面的线性代数与下降命题已证明；具体数值来自[已经返回的首完整方向](../notes/2026-11-20-fullspace-inequality-first-result.md)中已有标量。两份新读取源只完成 AST 静态检查，尚未科学执行；没有新本地场计算、fixture 或加长旧预算。当前公开 Actions replay、.992/.998 pair 及其源字节均不改变。

## 1. 当前二次式的单位

使用 [R664](R664-positive-spectral-residual-Hessian-and-true-gradient-pullback.md)的真半梯度与正残差 Hessian，令 A 和虚拟 v 已同乘 $\sqrt{k/(\sigma^2C_0)}$。完整步坐标 z 包含 DI 与同范数粗列，物理原自由量增量为 Tz。当前子问题为

$$
q(z)=\tfrac12\|Az+v\|^2+\tfrac{\mu^2}{2}\|z\|^2,
\qquad Cz\le b.
$$

记 $g_0=A^Tv$、$H=A^TA+\mu^2I$。无阻尼的真实 Phi 二次模型变化是

$$
\Delta\Phi_{\rm model}(z)=2g_0^Tz+\|Az\|^2.
$$

$2(q(z)-q(0))$ 还包含 $\mu^2\|z\|^2$，不能当成上述无阻尼变化。虚拟右端平方也不能当实际 Phi。后面所有能量比、射线最优值和误差界都按这个明确单位解释。

## 2. 正谱块的跨度不是完整场条件数

设 R664 在 Frobenius 正交残差坐标中给出 $mI\preceq Dh(E)\preceq MI$，J_F 是包含归一化径向正权、角轨道和 Frobenius cross 因子的完整导数，则直接由 Loewner 合同变换得到

$$
\frac{k}{\sigma^2}mJ_F^TJ_F
\preceq A^TA\preceq
\frac{k}{\sigma^2}MJ_F^TJ_F.
$$

因此

$$
\lambda_{\min}(H)\ge\mu^2,\qquad
\lambda_{\max}(H)\le\mu^2+\frac{k}{\sigma^2}M\|J_F\|^2.
$$

没有实际 $\|J_F\|$ 或受约束有效谱信息时，不能由 M/m 直接宣称完整 Hessian 的条件数。首完整方向已返 m=6.4e−11、M=.002559261845803203，块跨度约4.0e7；这是残差空间的实际跨度，而不是完整 H 的已测条件数。

此外，当前 T 保全部原自由变量但使用冗余坐标。若 $n_z>n_x$，则 $\ker T$ 非零，且

$$
Az=0,\qquad Cz=0\quad(z\in\ker T).
$$

所以名义 H 确有特征值 µ²；每个活动面的切空间也包含这个核。但从 z=0 出发，$g_0\in\operatorname{ran}T^T$，所有几何工作行也属于该空间。CG 的 H 乘积、行投影和 R668 的释放方向均保持 $\operatorname{ran}T^T$，因为

$$
H(\operatorname{ran}T^T)\subseteq\operatorname{ran}T^T.
$$

这个不变性由逐步线性组合直接归纳成立。因此冗余核产生的名义最小特征值不自动成为精确算术中 Krylov 的有效最慢模；也不能仅据名义条件数决定追加256次内迭代。浮点计算另有舍入误差，本命题不把数值正交误差改写成严格证书。

## 3. 从已有三个标量识别阻尼的实际作用

定义

$$
E_A=\|Az\|^2=\Delta\Phi_{\rm model}-2g_0^Tz,
\qquad E_\mu=\mu^2\|z\|^2.
$$

这两个量不需要新 J/Jᵀ：原报告已经保存模型变化、半梯度配对、µ 和坐标步范数。首完整方向给出

$$
g_0^Tz=-5.081817560164752\times10^{-9},
$$

$$
E_A=2.366273098726827\times10^{-9},\qquad
E_\mu=2.715468504406358\times10^{-9}.
$$

所以 $E_\mu/E_A\approx1.15$；沿这个具体完整方向，阻尼能量甚至稍大于数据曲率能量。它提供检查 µ 的依据，但不证明其它方向也如此，更不证明降低 µ 后几何一定允许大步。

同一已付方向的一维二次式可以精确最小化。若 $s=g_0^Tz<0$、$E_A>0$，无阻尼数据模型沿 αz 的最优 α 为

$$
\alpha_{\rm data}=-s/E_A,
\qquad
\alpha_{\rm reg}=-s/(E_A+E_\mu).
$$

已有数值给 $\alpha_{\rm data}\approx2.15$、$\alpha_{\rm reg}\approx1$。与此同时，原工作行限制

$$
\alpha\le\min_{(Cz)_i>0}\frac{b_i}{(Cz)_i}
$$

可能截断这条射线。这个上限只是原点处的一阶工作模型，既不替代所有永久位置的实际筛选，也不是接受点处重新线性化后的必要上限。新的 .992/.998 pair 应读其实际 E_A、E_µ、选行界和真实回溯，再决定 µ 或一维延伸；不能照旧值预设结果。

## 4. 固定活动面已经解到什么程度

令 I 是当前活动集合，z 是该仿射面上的点，P 是 $\ker C_I$ 的正交投影，$p=P\nabla q(z)$。记该整个仿射面上的极小值为 $q_I^*$，则

$$
0\le q(z)-q_I^*\le\frac{\|p\|^2}{2\mu^2},
\qquad
\|z-z_I^*\|\le\frac{\|p\|}{\mu^2}.
$$

**证明。** 对任意切向 d，

$$
q(z+d)=q(z)+p^Td+\tfrac12d^THd
\ge q(z)+p^Td+\tfrac{\mu^2}{2}\|d\|^2
\ge q(z)-\frac{\|p\|^2}{2\mu^2}.
$$

限制 H 到切空间仍至少为 µ²I，解其一阶方程便得距离界。若还保留非活动不等式，其可行面内改善只会更少，所以同一上界仍有效。

首方向末 $\|p\|=4.232443743733279e-11$、µ²约1.45522e−4。把这些普通浮点读数代入理论式，仅给约6.2e−18的剩余固定面二次改善，而本轮已经付出的正则二次下降约2.54e−9。这个固定面已经非常充分；为了把面内梯度继续降过旧9.63648e−12的形式阈值而延长旧迭代，缺少相应的收益依据。

该界**不限制释放活动行后的改善**，也不限制换工作集后的改善。首方向仍有负乘子，不能据此称全 QP 最优。R668 正好提供不等面内形式阈值即可按单位可行下降率释放的机制。

更一般地，对任意真正可行 z 和任意 $\lambda\ge0$，有

$$
q(z)-q^*\le
\lambda^T(b-Cz)+\frac{\|\nabla q(z)+C^T\lambda\|^2}{2\mu^2}.
$$

证明是对拉格朗日函数使用同一个强凸下抛物面：其全空间极小值至少为 $q(z)+\lambda^T(Cz-b)-\|\nabla q+C^T\lambda\|^2/(2\mu^2)$，并且它是原问题的对偶下界。负的 raw 乘子不能直接放入此式冒充可行对偶变量。当前两份新读取源没有额外计算这个完整对偶残差，也没有宣称取得全 QP 的严格最优性界。

## 5. 有限预算方向本身何时有下降保证

若 z≠0 且 $q(z)\le q(0)$，则

$$
g_0^Tz\le-\tfrac12(\|Az\|^2+\mu^2\|z\|^2)<0.
$$

因此真实 Phi 在原父沿 Tz 的方向导数 $2g_0^Tz$ 严格为负；无需先声称 QP 已全局最优。若父处每个保留的域/几何点约束都具有严格正余量，有限性和连续性保证足够小的正步保持这些点约束，Phi 的可微性则保证足够小的实际 Armijo 步下降。这是针对所声明有限点模型的存在命题，不保证预设15个回溯步一定已经找到它，也不证明连续曲率或 reach。

若 pair 的新满步真正接受、其后 metric 仍约 .013，最便宜的一个有据后继是重用已经支付的完整方向 d，而不是直接增加另一个256次求解预算。在实际接受点 x 上只付一次 Jv，可读出真正的

$$
D\Phi(x)[d]=\frac{2k}{\sigma^2C_0}
\sum_{j,\ell}w_jm_\ell
\left\langle T_{\rm raw}^*h(E_{j\ell}),
       J_{\rm raw}(x)d_{j\ell}\right\rangle.
$$

所有 cross/orbit 因子按 R664 原约定保留，不再补一个√2。用同一 Jv 还可得到正残差 Hessian 射线量

$$
c=\frac{k}{\sigma^2C_0}\sum w_jm_\ell
       \xi_{j\ell}^TL(E_{j\ell})\xi_{j\ell}\ge0.
$$

它不是完整 x-Hessian。如果新的真导数为负，且实际接受点所有已知有限余量严格为正，那么在 $x+\eta d$ 上存在实际可行的小正 Armijo 步。可用 $-D\Phi/(2c)$ 或加入原射线阻尼后的正模型步长提出首个 η，但实际 Phi 和所有永久几何位置仍须逐试读取；不能把原父的模型斜率当接受点的真斜率。若新导数不负，这条已经支付的射线就没有该局部下降依据，不继续盲延伸。

## 6. 停止阈值和目标缩小时的单位

固定的 qp_atol=1e−12 不是目标缩放不变的量。若同时将 A、v、µ 乘 a>0，则整个 q 乘 a²，最优物理步不变，而梯度与 R668 的单位释放下降率均乘 a²。保持同一停止规则需要 atol 同乘 a²；rtol 项自然随初始梯度缩放。单独缩放残差而不缩放 µ 会改变问题。

当前首方向的 atol 约占声明梯度阈值10%，尚不能把它说成当前 .013 plateau 的主因。另一方面当实际误差继续缩小时，固定 eps 下的局部数据 Hessian 系数可接近 $\frac{k}{\sigma^2}(\epsilon/\sigma)^{p-2}$；绝对停止阈值与 µ 的相对作用应在真实新父上重新读取。不能沿用旧固定梯度数量级来判定已达到1e−6 metric。

## 7. 可直接接公开 runner 的两份小源

1. `scripts/resume_20261120/full_phi_qp_scalar_diagnostics.py`，SHA256 `9124229786200659f1c9dc73620eecd75dda6493990f684149471d7003263b9d`。仅标准库处理已经返回的报告标量；0次场求值、0次J/Jᵀ、0个新fixture。记录本条能量比、固定面界、atol占比、块跨度、射线模型及工作行上限，明确普通浮点诊断范围。
2. `scripts/resume_20261120/full_phi_saved_ray_slope.py`，SHA256 `add40e2d9b667ff3dc0ee413516d3ec14887f593b0b4d7a5f5f85563219c207e`。只消费真实完成且接受的单方向报告、对应 final bundle/step/carrier 与源 SHA；1次接受场 residual、1次Jv、0次VJP、0次QP。它只返回上述真正当前导数和射线残差曲率，不执行新的回溯，也不接受新场。

两个源都要求公开 Actions 环境。当前只有 AST 静态检查，没有任何新科学结果。示例：

```bash
python "$topic/scripts/resume_20261120/full_phi_qp_scalar_diagnostics.py" \
 --report "$pair/margin-0992/report.json" \
 --report "$pair/margin-0998/report.json" \
 --out "$work/pair-scalar-diagnostics.json"

python "$topic/scripts/resume_20261120/full_phi_saved_ray_slope.py" \
 --report "$chosen_actual_single_direction_report" \
 --out "$work/chosen-saved-ray-true-slope.json"
```

后一个调用由新 pair 的实际结果决定，不是启动前必须经过的流程；旧候选数值、旧场证书和旧余量不移用新父。全域 metric、精化收敛、完整 reach 和最终比例仍须继续推进。

上述保存射线读取器绑定本次旧lift完整QP所记工厂和源；R671新h/f/k场须使用其明确的新factory上下文，不能用这个旧入口默默按旧lift重建。

执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
