# R684. 旋转度量的角均值设计、完整变分及固定目标精化

2026-11-26，Astra-larger-e4e2a2bf-20261126 / construction（AI辅助）。

**状态：下述几何与有限算子恒等式已证明；实际新父读数、求解和完成标准尚未由本条支付。** 本条明确开一个**新度量设计**方向，不将重新定义的目标称作原 FullHold 度量的精化或接受。原 R671 物理场、全部原自由坐标、同一闭合接口和所有角向观察均可保留。新的候选确定后，必须冻结一个完整的目标度量，再执行真正的同目标精化。

与 R248 的关系是：其相位恒等式只需要活动部分的目标度量关于**材料角**不变；径向系数不必恒为 1，也不必继续采用旧 FullHold 的 $a(s)$。本条补上由实际闭场选择这样的新目标、完整导数及其冻结规则，不重复认领 R248 的相位正则性或已有几何证书。

## 1. 物理角、材料角和实际 Gram

在活动部分使用旧物理表示 $F(s,\phi)$，其共同材料角为

$$
\theta=\Theta(\phi),\qquad \Theta(\phi+2\pi)=\Theta(\phi)+2\pi,
\qquad \rho(\phi)=\Theta'(\phi)>0.
\tag{1}
$$

这里 $\Theta$ 与 $s$ 无关。故在材料坐标 $(s,\theta)$ 中，实际第一基本形式为

$$
G=\begin{pmatrix}E&B\\B&C\end{pmatrix},\qquad
E=|F_s|^2,\quad B=\frac{F_s\cdot F_\phi}{\rho},
\quad C=\frac{|F_\phi|^2}{\rho^2}.
\tag{2}
$$

若 core 系数变化，$F,\rho,\Theta$ 均按原完整场公式变化；不能将 $F_\phi$ 误称为 $F_\theta$，也不能遗漏分母或角换元的导数。后文以旧完整 Gram 算子作链式法则的底层，它已经支付 R671 的解析尾、$\rho$ 分母和 $\Theta$ 变动。

### 1.1 当前对称类的交叉均值准确为零

当前 R671 表示在旋转架中使用 $R,Z$ 的偶余弦模、$T$ 的奇正弦模；$\rho$ 是偶函数，$\Theta$ 是奇函数模 $2\pi$，解析 lift 保留同样的反射。令 $J_y=\operatorname{diag}(1,-1,1)$，于是

$$
F(s,-\phi)=J_yF(s,\phi),\quad
F_s(s,-\phi)=J_yF_s(s,\phi),\quad
F_\phi(s,-\phi)=-J_yF_\phi(s,\phi).
$$

代入 (2) 得 $E,C,\rho$ 偶，$B$ 奇。因此

$$
\int_0^{2\pi}B(s,\phi)\,d\phi=0,
\qquad \int_0^{2\pi}B(s,\phi)\rho(\phi)\,d\phi=0.
\tag{3}
$$

完整对称离散网格的相应带符号和也为零。**不能把正的 quarter 重数乘在奇 $B$ 上再求平均**：quarter 上的 $B$ 并非一般为零，反射到另一半时它变号。下面保留每个交叉残差，不减掉一个伪造的 quarter 均值；端点的浮点余量也原样计入误差。

## 2. 两种分别明示的合法新度量

最自然的选择是材料角 Haar 平均：

$$
\bar E(s)=\frac1{2\pi}\int_0^{2\pi}E(s,\phi)\rho(\phi)\,d\phi,
\qquad
\bar C(s)=\frac1{2\pi}\int_0^{2\pi}C(s,\phi)\rho(\phi)\,d\phi.
\tag{4}
$$

另一种独立选择是明确固定的正权平均

$$
\bar E(s)=\sum_j\omega_j E(s,\phi_j),\qquad
\bar C(s)=\sum_j\omega_j C(s,\phi_j),\qquad
\omega_j>0,\quad\sum_j\omega_j=1,
\tag{5}
$$

其中角节点及权重是设计定义的一部分。特别可以选择均匀物理 $\phi$ 网格的完整轨道重数权。它**不是**材料 Haar 平均，却同样给出只依赖 $s$ 的两个系数；合法性不要求把它改成 (4)。

对材料 Haar 积分使用同一物理网格求积时，正确的有限权重是

$$
\omega_j=\frac{m_j\rho_j}{Z},\qquad
Z=\sum_i m_i\rho_i.
\tag{6}
$$

$m_j$ 为完整角轨道重数。若连续 $\rho$ 的均值为 1 且有限网格准确积分其有限谱，准确实算术中 $Z=N$；实现仍保留 $Z$ 及其导数，不假设浮点形成的和逐字等于 $N$。(6) 既可作为 (4) 的数值求积，也可明确选为一个**有限公式定义的精确新目标**。两种解释不得混用：前者要支付求积误差，后者在最终冻结时固定整套有限公式。

任取上述一种明示选择，定义

$$
g_F=\bar E(s)\,ds^2+\bar C(s)\,d\theta^2.
\tag{7}
$$

### 定理 684-A：正定性、闭合相容与全相位误差

若 $F$ 是当前闭合模型的 $C^2$ 浸入，$\rho>0$，且满足 R248 的准确平帽两 jet 接口，则：

1. (7) 在活动部分为正定度量；在固定帽上采用固定标记图自身的诱导度量后，得到同一个闭材料面的共同目标。
2. $g_F$ 在活动部分对材料角平移不变。对于 R248 的准确相位族，全部相位的相对算子误差上确界等于初相位的上确界。
3. 仅更换比较目标不会改变实际 $F$、其嵌入性、曲率、reach、直径或握持变化量；以后改变 $F$ 的设计迭代仍须对新场重新支付几何。

**证明。** 浸入给 $F_s\ne0$ 与 $F_\theta\ne0$，故 (2) 中 $E,C$ 处处正。正权积分或正权有限和保持严格正性。在每个紧径向区间上，连续性给正的统一下界。$F\in C^2$ 使 $E,C\in C^1$；积分、有限和及正的归一化因子保持 $C^1$。若源更光滑，得到对应更高正则性，但不从 $C^2$ 源免费宣称目标 $C^\infty$。

在准确帽口，$F,F_s,F_\theta$ 和所有二阶导数的迹与同一平帽一致。因此 $E,B,C$ 及其一阶迹与平帽目标一致；角均值保留这些共同迹，(7) 可与帽目标拼合。中央镜像缝同理，来自同一闭 $C^2$ 映射，不能分别平均不同未匹配的片。固定标记在帽口邻域为零，故不增加新接缝。

式 (7) 的系数不依赖 $\theta$，故 $\psi_\alpha^*g_F=g_F$ 于活动区。准确相位场 $F_\alpha=R_\alpha F\circ\psi_{-\alpha}$ 的实际 Gram 为 $\psi_{-\alpha}^*G$，相对误差自伴算子在对应点由切空间等距映射共轭。取遍全部点得到全相位上确界恒等式；帽上固定且相对误差为零。这正是 R248 的证明所用结构。最后一项由物理映射未变直接成立。证毕。

本定理没有声称给定场相对 (7) 的误差很小，更没有声称有限网格上为零便是连续准确等距。若需要由目标度量的二阶导数推算曲率，必须另付该正则性；本支线仍使用实际场的完整二 jet 检查曲率，不从均值目标推断几何。

**一般对称性之外。** 如果以后加入破坏 (3) 的自由模，则应同时保留 $\bar B$，使用完整平均矩阵；正定矩阵的正权平均仍正定，仍关于 $\theta$ 不变。本次代码只用于已证明的反射类，不能无说明地删掉一般情形的 $\bar B$。

## 3. 新残差的准确归一化

原目标为 $g_0=ds^2+a(s)^2d\theta^2$。令原完整残差为

$$
e=E-1,\qquad f=B/a,\qquad d=C/a^2-1.
$$

在一个径向位置，记 $\mu_e=\sum_j\omega_j e_j$、$\mu_d=\sum_j\omega_jd_j$，以及

$$
A=1+\mu_e=\bar E,\qquad D=1+\mu_d=\bar C/a^2,\qquad S=\sqrt{AD}.
$$

则相对**新目标**的实际残差恰为

$$
\widetilde e_j=\frac{e_j-\mu_e}{A},\qquad
\widetilde f_j=\frac{f_j}{S},\qquad
\widetilde d_j=\frac{d_j-\mu_d}{D}.
\tag{8}
$$

这是对角矩阵 $g_F^{-1/2}Gg_F^{-1/2}-I$ 的逐项计算。旧 $a$ 只是中间归一化：$a^2D=\bar C$，所以没有偷偷把旧标量作为新的几何约束。

真实点态算子误差是

$$
\varepsilon_j=\frac{|\widetilde e_j+\widetilde d_j|
+\sqrt{(\widetilde e_j-\widetilde d_j)^2+4\widetilde f_j^2}}2.
\tag{9}
$$

只做 $e\mapsto e-\mu_e$、$d\mapsto d-\mu_d$ 后把最大分量当作新误差是不正确的：分母和交叉归一化也变了。

### 3.1 有限均值能量恒等式及其测度

设 $\omega_j=w_j/W$、$W=\sum_jw_j$，所有 $w_j>0$。准确展开平方并用加权均值定义，得

$$
\sum_jw_j(e_j^2+2f_j^2+d_j^2)
=\sum_jw_j\big((e_j-\mu_e)^2+2f_j^2+(d_j-\mu_d)^2\big)
+W(\mu_e^2+\mu_d^2).
\tag{10}
$$

各径向位置再乘同一正径向权并相加，恒等式仍成立。它只分解**旧归一化**的 Frobenius 能量；重新归一化后的 (8) 必须另算。材料 variant 使用 $w_j=m_j\rho_j$；固定物理 variant 使用 $w_j=m_j$。前者的能量不是旧求解器原来的 $m_j$ 能量，报告中分别列出，不相减冒作同目标改善。

(10) 给出了选择新设计的实际判据：旧误差有多少是可释放的角常数约束，有多少仍是真实各向异性。释放两个均值没有删除任何非零角振荡或交叉条件；(8) 在全角为零，当且仅当 $E=\bar E,B=0,C=\bar C$ 在全角成立。

## 4. 两个平均定义的完整微分

以 $h=(h_e,h_f,h_d)$ 表示原残差的一个完整方向。在材料 variant 中，实际 core 变化给密度方向 $\dot\rho$，须用

$$
\dot Z=\sum_jm_j\dot\rho_j,\qquad
\dot\omega_j=\frac{m_j}{Z}\dot\rho_j-\omega_j\frac{\dot Z}{Z}.
\tag{11}
$$

然后

$$
\dot\mu_e=\sum_j\omega_jh_{e,j}+\sum_j\dot\omega_j e_j,\qquad
\dot\mu_d=\sum_j\omega_jh_{d,j}+\sum_j\dot\omega_j d_j.
\tag{12}
$$

固定物理 variant 中 $\dot\omega=0$，但原 $h$ 本身仍包括当前 $\rho$ 分母和 $\Theta$ 的完整变化；不能因固定平均权而冻结场的这些支路。

对 (8) 作商法则：

$$
\dot{\widetilde e}_j=
\frac{h_{e,j}-(1+\widetilde e_j)\dot\mu_e}{A},
\qquad
\dot{\widetilde d}_j=
\frac{h_{d,j}-(1+\widetilde d_j)\dot\mu_d}{D},
\tag{13}
$$

$$
\dot{\widetilde f}_j=\frac{h_{f,j}}S
-\frac{\widetilde f_j}{2}
\left(\frac{\dot\mu_e}{A}+\frac{\dot\mu_d}{D}\right).
\tag{14}
$$

这些公式没有省略均值分母的导数。通过原完整 $Jv$ 提供 $h$，并由原 core 坐标提供 $\dot\rho$，即可得到新目标的完整 $Jv$。

## 5. 完整转置及额外 core 支路

对新 raw 残差给普通 Euclidean 余切量 $y=(y_e,y_f,y_d)$。定义

$$
L_e=\frac{\sum_jy_{e,j}(1+\widetilde e_j)
+\tfrac12\sum_jy_{f,j}\widetilde f_j}{A},
\quad
L_d=\frac{\sum_jy_{d,j}(1+\widetilde d_j)
+\tfrac12\sum_jy_{f,j}\widetilde f_j}{D}.
\tag{15}
$$

收集 (13)–(14) 中每个 $h$ 的系数，得到对原 raw 残差的余切量

$$
q_{e,j}=y_{e,j}/A-\omega_jL_e,\quad
q_{f,j}=y_{f,j}/S,\quad
q_{d,j}=y_{d,j}/D-\omega_jL_d.
\tag{16}
$$

材料 variant 还得到密度余切量

$$
q_{\rho,j}=-\frac{m_j}{Z}
\left[L_e(e_j-\mu_e)+L_d(d_j-\mu_d)\right].
\tag{17}
$$

**证明 (17)。** 权重方向项为
$-L_e\sum_j\dot\omega_j e_j-L_d\sum_j\dot\omega_jd_j$。代入 (11)，将 $\dot Z$ 的系数重新分配到每个 $\dot\rho_j$，恰得到 (17)。因此该项同时包含分子 $\rho$ 权和归一分母 $Z$ 的导数。固定物理 variant 的此项准确为零。证毕。

当前 core 的实际密度为

$$
\rho(\phi)=1+\sum_{k=1}^M(1-\nu_k^2)c_k\cos(\nu_k\phi),\qquad\nu_k=2k.
$$

先将 (17) 对全部径向观察求和，然后作上式的转置，得到

$$
q_{c_k}=(1-\nu_k^2)\sum_j\cos(\nu_k\phi_j)
\sum_{\text{径向行 }i}q_{\rho,ij}.
\tag{18}
$$

只把 $k>K$ 的分量加到原 packed core 自由块。式 (18) 仅支付**均值权重**带来的新支路；原 $J^*$ 已含场、角 lift、$\rho$ 分母和 $\Theta$ 的支路，不再重复添加它们。所有其余自由变量和旧角行保持。

### 5.1 原 quarter 行权的传递

记 $W_m=\operatorname{diag}(\sqrt{m_j})$，原求解器残差和 $J$ 已含 $W_m$。新 raw 变换记作 $T$。则

$$
r_{\rm new}=W_mT(W_m^{-1}r_{\rm old}),
$$

$$
J_{\rm new}v=W_mDT\big(W_m^{-1}J_{\rm old}v,\dot\rho(v)\big).
\tag{19}
$$

对新 weighted 余切量先乘 $W_m$，通过 (16)–(17)，再将旧 raw 余切量除以 $W_m$ 交给旧 $J^*$，最后加 (18)。外部正径向权、Frobenius 权或谱 Hessian 权照旧由相应消费者乘入；不能把轨道重数重复计两次。这证明了源码 wrapper 的全部前向与转置公式。

## 6. 新目标求解的责任

可以对新残差继续使用固定参数的正谱目标，例如 R660/R664 的

$$
\Phi(x)=\sum_{i,j}\eta_{ij}
\operatorname{tr}\left(
\frac{\widetilde R_{ij}(x)^2+\varepsilon^2I}{c^2}
\right)^{p/2},\qquad \eta_{ij}>0.
$$

同一次 line search 固定 $p,\varepsilon,c$、平均 variant、角网格和径向权；每个 trial 从它**自己的新场**重新计算 (8) 和真实 $\Phi$。接受与否比较的是这个新的设计泛函，不与旧固定 $g_0$ 的 $\Phi$ 混减。谱块作用于新残差；真实梯度用新完整 $J^*$，正残差 Hessian 的拉回不是完整场 Hessian，也不是全局上界。

原物理 H² 母范数、全部旧/新永久曲率和半径位置、真正非线性几何筛可复用为**算法定义**；它们不会因为平均目标变化而自动失效或自动通过。几何 cotangent 仍来自原实际场。每改变场后，原全空间嵌入、reach、握持、非全等证书只能按同场证明的范围使用。

**不能只改 residual 名字。** 旧 full-Phi/PCG 的一些加速器直接由 $F_s,F_\phi$ 组旧 Jacobian 列或角矩；这些支路若绕过 wrapper，就遗漏 (12)–(18)。首个可执行版本应使用新 wrapper 的完整 $J/J^*$，或给每一组直接装配的列显式施加这些公式。无论哪种方式，都不能用旧 coarse 梯度/正规矩阵冒作新目标的对应量。

## 7. 最终冻结的完整定义

新设计不是完成。设未来一个候选 $F_*$、variant 和参数组合已选定。此后定义并固定以下对象：

1. 同一个闭材料面、材料角、相位范围、core/帽接口、marker 图与全部**设计常数**。
2. 一个完整径向函数 $E_*(s),C_*(s)$，由明确的 (4)、(5) 或 (6) 给出。若采用有限平均定义，固定候选 $F_*$ 的全部表示、精确节点、角规则、原 $\rho_*$ 和权重；它们以后不随精化候选变化。
3. 活动目标 $g_*=E_*(s)ds^2+C_*(s)d\theta^2$ 及固定帽目标。精化层次上的新自由系数属于待求嵌入，不反过来重新定义 $g_*$。

这使目标在**整个径向连续区间**上有确定公式，不能只保存旧观察点的两个数组并用未声明插值填新点。现有 R671 场给出了其准确共享 quintic 与解析 lift，所以有限平均可以直接在任意新径向点求值；原节点 $\alpha S+\beta$ 及其实际参数含义继续保留。

对任意精化候选 $F^{(n)}$，仍令它自己的实际材料 Gram 为 $(E^{(n)},B^{(n)},C^{(n)})$。正确残差是

$$
E^{(n)}/E_*-1,\qquad B^{(n)}/\sqrt{E_*C_*},\qquad C^{(n)}/C_*-1.
\tag{20}
$$

这里**不减 $F^{(n)}$ 自己的角均值**。目标的求值精度提高可以降低计算误差，但不能改变 (20) 的精确 $E_*,C_*$。若使用 (4) 的连续积分解释，必须支付其求积余项；若使用固定有限公式，则没有另一个“真正平均”要追逐，仍须认证该明确目标下的全角/全径向误差。

实际空间/频率精化误差持续下降至机器或原 solver 容差、全时几何及 README 的其余条件仍要全部支付。没有给出这些实际返回前，不以“均值被投影掉”“同场几何未变”或有限 $\Phi$ 小声称完成。

## 8. 本次可执行入口

小源：

- `mean_metric_design.py`：两个明示 variant 的 (8)、完整 (11)–(19) 及原全自由 $J/J^*$ wrapper；无 import 时科学执行。
- `read_mean_metric_candidate.py`：以同一实际 R671 bundle/profile/carrier 为输入，只读一次全部旧行和 Gauss 行的首 jet，同时比较两个 variant；不更新场、不运行求解、不作新的几何计算。

诊断保留：旧固定目标的实际最大误差与原 $\phi$ 正权谱目标；每个 variant 按自身正确测度的 (10)；重新归一化后的 (9)、最坏地址与完整扫描范围；两种目标均只为有限点读数。R671 的 canonical model identity 须通过原 `transfer_seed(..., source_lambda=lambda, mode='keep-q')` 的同场检查，不能悄悄迁移场或用旧无 $k$ 解析项的消费者。

科学入口同时要求 `GITHUB_ACTIONS=true` 和 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。报告用提供的 repo 中 `git rev-parse HEAD` 记录实际 step source；另保存 `GITHUB_SHA` 为 workflow trigger 身份，二者不混。当前只做源码 AST 解析，尚无新实际读数。

建议同一次公开再生 R671 真父之后直接调用：

```sh
python "$SRC/read_mean_metric_candidate.py" \
  --repo "$GITHUB_WORKSPACE" \
  --bundle "$WORK/exact-tail-full-phi-PCG-SOC-first/final.npz" \
  --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
  --node-report "$WORK/fullclosed_solver/data/fullclosed-hold-warm.json" \
  --scalar-input "$WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
  --angles 2048 --stage-block 64 --legacy-fraction .5 \
  --spectral-p 8 --spectral-epsilon .001 --spectral-scale .05 \
  --target 1e-6 --out "$WORK/postprocess/R684-mean-metric.json"
```

`$SRC` 中两小源相邻，或显式给 `--transform-source`。可重算报告/数组只留 runner，发表小源、参数、run 编号、输出哈希与紧凑真实结论。只读诊断之后继续实际新目标求解与最终固定目标精化，不在本条公式或诊断处结束课题。

## 本条入口的实际首次诊断

[2026-11-26同一实际场双variant诊断](../notes/2026-11-26-actual-new-metric-initial-diagnostics.md)已经返回：重定义均值本身未解决百分之一误差；尚须实际优化、固定最终g和同g精化，不能把新目标命名作为完成。

[首两条physical/p4实际方向与新场完整first](../notes/2026-11-26-actual-first-mean-design-and-amplitude.md)现已返回：实际下降但max仍.01429595、内层远未驻点；同场D/L及嵌入已付，完整K与固定g精化未付，继续R688真实方向。

最终目标的[完整冻结/固定g求解/准确精化五源入口](../notes/2026-11-26-frozen-mean-target-numerical-pipeline.md)已刊：目标连续公式与原角规则不变，恢复全部均值约束，实际fine目标在原冻结场上求值；显式停止精度、同父测度和零方向退出，尚无本管线科学返回。
