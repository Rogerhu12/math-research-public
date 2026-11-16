# R553：真实完整前缀系数盒、Frenet 正域与全单元常数的实际消费

作者：ChatGPT（AI，geometry 协作代理）。日期：2026-11-16。

**可信度：已证明（限下述准确实条件命题、区间包含关系与明确的源码调用合同）。** 本文没有执行科学数值、取得新的 accepted450、计算实际常数，或证明原 solver 容差已经推出全闭面的误差 floor。实现仅在公开 Actions 的原后置 metric 计算中运行；原 BVP/native/FD/fullDN、全域相对度量和精化接受条件不改。

本次把 [R521](R521-complete-finite-Frenet-tube-and-cubic-residual-enclosures.md) 的一项真实输入缺口接起来：**从已绑定的完整准确五次 Hermite 前缀，真正形成全部 $3M+2$ 系数的闭盒；从同一次准确 target 返回形成 $A,\nu,\mu$；对整个系数盒、整个 scalar 盒和原角闭单元证明正域，随后调用原 R521 计算四块常数。** 调用者不再凭几个标量宣称该局部 tube 已有来源。

这只支付当前准确前缀有限参考的实际域和常数。R521 的原 cubic、真实 residual sample、形成误差和比较路径属于其它责任。本文不把五次 Hermite 改名成原 SciPy/PPoly cubic，不把 source SHA 当作原 FFT 误差，不复制 R514/R521 已付的误差传递定理。

## 553.1 既有对象与本次新增责任

| 对象 | 真实已有来源 | 本次操作 |
|---|---|---|
| 原接受父、完整节点/状态/RHS、native/FD/final 来源 | R400/R441/R451/R463 对应实际 checkpoint loader | 沿 R504 原加载器完整绑定，不造父 |
| 准确前缀定义 | 原675 的 ExactFiniteField.prefix_coefficients / prefix / registered_world | 读取同一对象的全部有理六个幂系数 |
| 完整准确 target、同 C 根族与 leaf/query 细化 | R492/R483/R500/R504 | 复用本次已返回的 radius、准确弧长导数与径向 metric |
| 全域 relative-operator-error 与闭 DFS | R459/R504 | 数学谓词、细分判断与原覆盖账保持 |
| 共同材料全 $t$ 转移 | R443/R457/R464 及原 R504 消费者 | 沿原合同，不以有限 $t$ 网格或本诊断替代 |
| 有限 Frenet 四块一阶/二阶 majorant | R521 原 helper 4217bf9a | 现在用实际形成的完整 tube 输入调用 |
| 原 cubic 到当前准确 quintic、FFT/RHS 形成差额 | R514/R521 尚待实际数据 | 本次不支付、不填零 |

正式 helper 是 [geometry_20261116_actual_prefix_coefficient_tube_majorants.py](../computations/geometry_20261116_actual_prefix_coefficient_tube_majorants.py)。独立 consumer 从 R504 的实际完整 evidence 程序按全部15条 literal 替换形成，原文件不覆盖；完整计划与调用接口见 [接口](../notes/2026-11-16-actual-prefix-tube-and-complete-metric-interface.md)。

R553 使用的底层系数方法仍是原675：
geometry_20261115_shared_active_interval_balls.py，33310B /
675ab8dffaaa86dd7a760dba8502d03d83f04fed15e88224c13da35a4151514b。
原方法从全部实际 binary64 节点0/1/2数据构造准确有理 Hermite，而不是读取 renderer 的近似值。新 helper 取 bound method 的实际 __module__，核该模块文件及完整 SHA；不从 sys.modules 找第一个同路径对象代替真实类的来源。

## 553.2 固定当前场、坐标与全系数顺序

在一个实际 prefix span $[x_i,x_{i+1}]$ 上，记
$h_i=x_{i+1}-x_i>0$，$t=(s-x_i)/h_i$。
这里 $s$ 是实际保存前缀的 numeric-length 坐标，节点 $x_i$ 是原有限字的准确有理提升。

状态按真实物理顺序

$$
y=(r_0,\ldots,r_M,\ t_1,\ldots,t_M,\ z_0,\ldots,z_M)
\in\mathbb R^{D},\qquad D=3M+2.
\tag{553.1}
$$

当前准确场的每列为

$$
Q_j(s)=\sum_{k=0}^{5} c_{jk}t^k,\qquad j=0,\ldots,D-1.
\tag{553.2}
$$

所有 $c_{jk}$ 都由当前对象的 prefix_coefficients(i) 返回。
原实现读取全 nodal 值、全一阶与全二阶数据，并调用原准确 Hermite 公式。
新源要求正好 $D$ 列、每列完整6项，没有截断高模、均值或“不会进入角导数”的列。

原 field.M 给实际 $M$；角数取已绑定 checkpoint 的实际
field_angular_quadrature。没有把要求的未来 refinement factor 当作实际维度。
当前原675实现已经动态使用 saved.M，所以新 helper 不另复制一套 M=112 核。

世界坐标表达还含实际固定 SE2 注册、完整 lower 反射以及已有材料相位解释。
这些来源仍由原 current loader 绑定。下文角导数取物理角
$\phi=2\pi q$；不是材料角 $\Phi(\phi)$，也不是把 $\Phi_q$ 代入 Fourier 频率。
原675的 evaluate 正是以 $2\pi q$ 调 prefix；材料 density 进入 target 的角 metric 和共同相位运输。

## 553.3 实际子单元的完整 Bernstein 盒

取原 DFS 给出的闭径向子区间 $I=[a,b]\subseteq[x_i,x_{i+1}]$。
归一化端点为

$$
\ell=\frac{a-x_i}{h_i},\qquad u=\frac{b-x_i}{h_i},
\qquad 0\le\ell\le u\le1.
\tag{553.3}
$$

令 $t=\ell+(u-\ell)v$，$v\in[0,1]$。对一列完整幂系数 $c_0,\ldots,c_5$，其限制后的幂系数为

$$
\widehat c_k
=\sum_{j=k}^{5} c_j{j\choose k}\ell^{j-k}(u-\ell)^k.
\tag{553.4}
$$

对应5次 Bernstein 系数

$$
b_k=\sum_{j=0}^{k}
 \frac{{k\choose j}}{{5\choose j}}\widehat c_j,\qquad k=0,\ldots,5.
\tag{553.5}
$$

因此对整个闭子单元，

$$
Q_j(I)\subseteq
\left[\min_k b_{jk},\max_k b_{jk}\right]=:\mathcal B_{I,j}.
\tag{553.6}
$$

**证明。** (553.4)是完整有限二项式展开；(553.5)是幂基到同次数 Bernstein 基的准确恒等式。Bernstein 基在 $[0,1]$ 非负且和为1，故每个值位于所有系数的凸包。端点、单点限制和所有中间值都包含。实现只用 Fraction、整数幂和 binomial 系数，不把盒中心或 float 近似作为准确系数。

定义完整独立状态盒

$$
\mathcal B_I=\prod_{j=0}^{D-1}\mathcal B_{I,j}.
\tag{553.7}
$$

这是对实际整条 $Q(I)$ 的外包；它通常比实际曲线大，不宣称盒中任意向量来自某个真实接受解。新正域判断将对整个这个较大盒成立，因此不需要先解开系数之间的相关性。

同法对准确导数幂列 $k c_k/h_i$ 和
$k(k-1)c_k/h_i^2$ 形成完整 Bernstein 界，记录

$$
Q_1=\sup_{I}\|Q'(s)\|_\infty\ \text{的上界},\qquad
Q_2=\sup_{I}\|Q''(s)\|_\infty\ \text{的上界}.
\tag{553.8}
$$

这两个量是当前准确 quintic 的界。它们没有被传给原 R521 的
literal-cubic schema，也不声称等于原 solver 保存/形成的三次多项式导数。
完整原六项系数、全部限制 Bernstein 系数及全部一/二阶盒各有实际规范 JSON 身份；全 $D$ 值盒保在本次原闭单元账中。

## 553.4 全频物理角 jet 的实际区间表达

取原角闭单元 $J=[q_-,q_+]\subseteq[0,1]$，
$\phi\in2\pi J$，频率 $\omega_j=2j$。
在随 $\phi$ 旋转的柱坐标正交基中，

$$
d=(r_\phi-t,\ t_\phi+r,\ z_\phi),\qquad
e=(r_{\phi\phi}-2t_\phi-r,\ t_{\phi\phi}+2r_\phi-t,\ z_{\phi\phi}).
\tag{553.9}
$$

实现使用完整线性和

$$
\begin{aligned}
d_1&=-\sum_{j=1}^{M}(\omega_jr_j+t_j)\sin(\omega_j\phi),\\
d_2&=r_0+\sum_{j=1}^{M}(\omega_jt_j+r_j)\cos(\omega_j\phi),\\
d_3&=-\sum_{j=1}^{M}\omega_jz_j\sin(\omega_j\phi),\\
e_1&=-r_0-\sum_{j=1}^{M}[(\omega_j^2+1)r_j+2\omega_jt_j]\cos(\omega_j\phi),\\
e_2&=-\sum_{j=1}^{M}[(\omega_j^2+1)t_j+2\omega_jr_j]\sin(\omega_j\phi),\\
e_3&=-\sum_{j=1}^{M}\omega_j^2z_j\cos(\omega_j\phi).
\end{aligned}
\tag{553.10}
$$

每个系数使用(553.7)的整个区间；每个 sin/cos 使用原 Active/Arb 在整个闭 $2\pi J$ 上的向外区间，随后将其准确有理端点交给 Fraction 区间运算。没有用网格角、中心值或旧 nominal 三角表替代。

得到的 $\mathbf D_{I,J},\mathbf E_{I,J}$ 满足

$$
d(y,\phi)\in\mathbf D_{I,J},\quad
e(y,\phi)\in\mathbf E_{I,J}
\quad
\text{对所有 }y\in\mathcal B_I,\ \phi\in2\pi J.
\tag{553.11}
$$

**证明。** 原 Fourier 展开逐项微分给(553.10)。闭区间加减乘及向外三角范围保包含；独立盒忽略了相同系数、相同角之间的依赖，只会增宽。$r_0$ 对 $d_2,e_1$ 的贡献完整保留；$z_0$ 的角导数确为零，但该状态列、径向导数和完整 DFT 均值输出没有删除。

柱坐标基到世界坐标的变换正交。固定 SE2 平移不影响角 jet，固定旋转和完整 lower 反射保持 dot、范数与 cross 范数。因此正域和绝对常数适用于原两片；没有将单片成功替代另一片的实际闭单元责任。

## 553.5 同一次准确 target 返回中的三个 scalar

令当前准确前缀长度为 $L_*$，实际 numeric 长度为 $L_{\rm num}$，置
$k=L_*/L_{\rm num}>0$。原 R400/R492/R483 target 在 numeric $s$ 下给

$$
A(s)=a(ks),\qquad
g_{ss}=k^2,\qquad
\mu=k,\qquad
\nu=A_s=k\,a_s(ks).
\tag{553.12}
$$

原 closed_range 的 jets[0], jets[1], jets[2] 是准确弧长参数上的
$a,a_s,a_{ss}$ 外包；radial_metric 是 $k^2$ 外包。
新 consumer 在本次原 target 调用后保存这些同一次返回，不另发一次 query，不取原 finite compiler 的 ap 冒准确导数。

设返回区间为 $\mathcal A,\mathcal A_s,\mathcal G$。仅当
$\inf\mathcal A>0,\inf\mathcal G>0$，用原 R521 relative dyadic sqrt 形成

$$
\mathcal M=
[\underline{\sqrt{\mathcal G_-}},
 \overline{\sqrt{\mathcal G_+}}],
\qquad
\mathcal N=\mathcal A_s\mathcal M.
\tag{553.13}
$$

于是真实同一 C 成员的 $(A,\nu,\mu)$ 属于
$\mathcal A\times\mathcal N\times\mathcal M$。
根族和依赖关系不换选；将这三个量暂视为独立区间只是充分外包。
相对平方根保严格正的准确下端点，不以绝对 dyadic 网格把已正的极小量截成零。

common public $u$ 的相位点查询仍可按原程序把 $g_{ss}$ 乘
$L_{\rm num}^2$。本诊断只挂在 base cell 的 numeric-$s$ 路径，保存的 context 明确是未乘该因子的原 numeric-$s$ metric；不混淆两个坐标的 $\mu,\nu$。

## 553.6 整个 joint 盒的正域证书

用准确区间 dot/cross 形成

$$
\mathcal Q=\mathbf D\cdot\mathbf D,\quad
\mathcal W=|\mathbf D\times\mathbf E|^2,
$$

$$
\mathcal P=
\mathcal A^2\mathcal M^2\mathcal W-\mathcal N^2\mathcal Q^3.
\tag{553.14}
$$

平方使用包含0时下界为0的真实区间平方。各项先独立向外再相减；不把相关消去、单点最小值或盒中心视作全盒证明。

若实际所得

$$
A_->0,\quad\mu_->0,\quad p_-:=\inf\mathcal P>0,
\tag{553.15}
$$

则对整个 $\mathcal B_I$、全部 $2\pi J$、全部声明 scalar 盒都有

$$
P=A^2\mu^2|d\times e|^2-\nu^2|d|^6\ge p_->0.
\tag{553.16}
$$

这正支付原 R521 调用所需的局部 joint 正域。$W$ 的完整下界和 $AW$ 外包同时保留；原 R521 可用
$\max(A_-W_-,p_-/(A_+\mu_+^2))$ 作为严格正分母界。没有要求 $\nu$、某个 normal 分量或每个 Fourier 系数非零。

若(553.15)未由当前盒证明，只输出相应
radius / radial-metric / whole-joint-P 未付原因及原单元地址。
这不是几何反例，也不是原 metric/BVP 拒收条件。宽盒可能阻止该充分证明；本次不承诺原工作深度、精度或预算一定足够。

## 553.7 原 R521 的真实四块调用

令 $b_j=\max(|\mathcal B_{I,j,-}|,|\mathcal B_{I,j,+}|)$。
实现把完整 $D$ 个 $b_j$、当前真实 $M,N$ 交给

- fourier_synthesis_majorants；
- finite_rhs_majorants。

第二调用所用域来自(553.13)—(553.15)，不是调用者填入的经验 $P_{\min}$。
第一调用提供全部频率的 $d/e$ 值界与完整系数最大范数到两角 jet 的算子界。R521 的原方向 majorant 正文不复制、不修改。

对准确均匀三角/DFT 参考 $N>4M$，输出四块上界

$$
K_y,\qquad K_A,\qquad K_\nu,\qquad K_\mu
\tag{553.17}
$$

及 state 方向二阶上界。原非均值投影绝对权和至多2、两均值至多1，全部行保留。$N>4M$ 是这套准确参考的原适用范围；不在此范围只令本诊断未付，不给原 solver 新增 acceptance gate。

$\sigma$ 沿被比较路径固定时，原 R521 的非负界对两个符号同样成立。
本实现没有辨识原 worker 的实际 root/branch，也不因某一支较小而声称它是原解。
真实 FFT/复步/字面投影和准确三角 DFT 之间的形成误差依旧单列。

## 553.8 精确说明常数适用的状态集合

局部结论是：对本叶的角范围，任何位于记录系数盒和 scalar 盒中的仿射输入路径，都满足原 R521 的相应方向界。这里“任意路径”只指真实包含在这个已证明合法盒中的路径。

对固定 $s$，取所有径向区间含 $s$、覆盖整角圈所需的 terminal prefix 叶，记其状态/scalar 盒为 $\mathcal T_\ell$。可以取共同凸域

$$
\mathcal T_s=\bigcap_{\ell:\,s\in I_\ell}\mathcal T_\ell.
\tag{553.18}
$$

这个交集包含当前准确五次状态及该同一目标的真实 scalar tuple，因为每个叶都从完整闭区间形成包含。对其中任意两个输入及它们的线段，每个角所需的叶都给合法域；有限 DFT 全部角行因而可以同时使用四块常数的最大值。

尤其，在所有 prefix 叶正域已付时，最大值是当前准确 quintic 状态沿整个前缀的完整准确有限 RHS 导数界。若另一条曲线要使用它做比较，必须实际证明其状态/scalar 与比较线段落入相应共同域；“两个端点各在某个不同盒”或“只在各自采样处合法”不够。

本次没有输入原 cubic，也没有证明这项比较路径包含。输出和接口明确保留此责任，不把(553.18)写成已经取得的原 ODE tube。

## 553.9 全角、闭端点、两反射与原 DFS

新观察器没有自己的空间网格。它接原 Measurement.base_once 已处理的完整 cell，cell 的 piece、radial、angular、lower、rank、dyadic_path 均原样保留。

原 metric 先按原 Gram/target 形成 relative_norm，再由原逻辑决定 refine。旁诊断不参与这个判断：

$$
\text{refine}=
(\text{原界缺失或原宽度超工作目标})\land
(\text{原深度仍可细分}).
\tag{553.19}
$$

若原 cell 细分，本次 tube 责任随原全部 children 保留，父诊断不当作子叶已付。
若原 cell 退休，记录该终叶的实际 tube 结果；同次 tuple 缺失、普通算术异常或正域未决均计为未付。原完整闭单元 ledger 保存其原地址、全系数盒、scalar/d/e/P、四块调用与退休记录。

汇总采用保守条件：**原整个 closed DFS 已完成、至少一个 prefix 终叶、所有 prefix 终叶 tube 已付、没有原执行/资源/关闭错误**，才给
complete_prefix_constant_cover=true 及全前缀常数。否则只给已付叶的局部极值，显式不是全局界。即使实际 prefix 可能先做完，本源也不从某个 rank 顺序猜早完成。

因此不可能用已访问的几个角、某一反射片、单个 knot 两端或非空计数替代原完整闭覆盖。原参数接缝是闭区间覆盖；相邻准确 Hermite 端点同用原 nodal 数据。集合覆盖不要求本次额外创建 seam fixture 或“对拍”门。

## 553.10 完整闭面 metric 仍按原源支付

本次 $3M+2$ 算子是前缀的有限 Fourier 参考，不是 native 全径向节点/DFT、原 cut correction、collar 或帽的统一系数模型。

这些其它区域仍由 R504 原完整 field.evaluate、同 C tail E(r)、原准确 cut/atlas 和两帽表达进入原全域 operator-norm 计算。既有 original112、resolution112、completeM、incrementalM 四族来源登记保持原值。没有把原 field 的真实调用者改成“generic source”，也没有减少全族、全参数或两均值。

全 $t\in[0,1]$ metric 上界的根据仍是原共同材料角共轭与同时拉回的广义谱不变性，加上原全角闭域和固定帽。R553没有另求 $t$ 网格；原实际嵌套 $t$ queries 照付。新的系数常数以 base-field 的物理角/随动参考解释，不声称相位后的固定角坐标仍自动具有同一个 $3M+2$ 奇偶基布局。

## 553.11 同一次求值、实际数据与失败范围

新 target context 保存本次原 closed_range 的三个 jet 区间、原 numeric 径向 metric、该返回对象身份和原径向地址；target_requeried_for_this_observer=false。

当前 field 的六 jet 求值仍按原函数执行一次；新 helper 只读取已经绑定的准确 polynomial 数据和本次 scalar return。它另外计算的是实际系数盒及所需角范围，不重复原 field 的全域扫，也不恢复/执行旧 solver。

若原 field/target 在诊断开始前抛出已知算术异常，原 cell record 保该真实异常；本叶 tube 标为同次结果未返回。若新诊断自己的普通算术/类型/字段范围出错，只将其记为具体未付，不改原 relative_norm 的 available 或上下界。

原 Budget/Bridge 资源异常不属于本 helper 吞掉的普通算术类。它们穿透到原资源停止，保留原 current_cell、未 pop 的 stack 以及全部 untouched root suffix。KeyboardInterrupt/SystemExit/MemoryError等也不会被误写为数学正域失败。

## 553.12 预算和临时全量记录

源生成只做文本/字节工作。科学 observer 没有独立时钟或子进程，每个系数列和频率循环都调用原 budget_check；R521 有限 majorant 调用前也检查同一剩余钟。所有精度、max_cells、max_depth、c_queries 和 phase 配置仍为原输入。

增加诊断工作会使用同一原 allowance。因此本源不承诺在相同 wall time 内访问和原源同样多的单元，不保证固定预算内形成完整常数覆盖；这与“不改变数学门”并不矛盾。

完整系数盒、每次实际局部结果和未付叶留在原 gzip cell ledger。必要正文给实际完整 ledger 身份、终叶计数、首末未付地址和完整原 coverage 对象的明确引用；没有声称所有退休 ledger 行已经回传。原所有当前 frontier、未访问根后缀、close errors、execution error 和 resource_stop 都保留。

每次必要正文仍单90000B。超限真实返回70，原临时完整对象和 raw 保留；没有编码分包、提高限额或为图小而删数学失败地址。comparison 引用同一新 evidence source 的真实结果，并保本新诊断摘要；不混旧 source schema 结果。

## 553.13 还没有从 solver 容差得到什么

下面各项仍不得从本次四常数推出：

1. 原 solver 的 literal cubic/PPoly 全四幂系数和实际采样 residual；
2. 原 FFT、平方根、normalization、投影及 residual norm 的形成误差；
3. 原 nominal scalar 与准确 $A,A_s,\mu$ 的真实差额；
4. 原 cubic、当前准确 quintic及二者比较线段属于同一合法状态 tube；
5. 原 root/取向分支与准确参考 $V_\sigma$ 的实际对应；
6. native 尾、cut patch、collar、帽及所有目标接缝所需的误差传递；
7. 原 RMS/BC/native tol 到完整 relative-operator-error 的可比较 floor。

R521 的 closed_cell_residual 需要前四类实际输入，quintic_residual_transfer 又需要实际 $E_0,E_1$。本源没有向这些 API 传零或假数据。记录准确 quintic 的 $Q_1,Q_2$ 为今后真正的区间残差消费提供已绑定数据，但没有调用 literal-cubic schema 充当原三次解。

继续完成 README 要求的路径仍是：同一准确目标、十参数和全 $t$ 范围下真实重新求解/精化，并实际测量完整 metric 误差；固定 $\eta$ 的重复 pass 不等于误差下降。R459原 upper/lower 与诚实未判定语义保持。本诊断若能实际支付常数，是后续完整误差传递的一项数据来源，不能把当前课题提前宣布结束。

## 553.14 实际 source 接口与结论

实际运行调用关系为：

- 原 R504完整消费者先绑定真实 checkpoint、同 C/new query、原第一材料与两帽；
- 新 helper 从当前 actual bound coefficient 方法读取全列；同次 target 返回由新 consumer直接传入；
- 原闭 DFS 每个 prefix cell 真实执行 inspect；
- 原 split/retire 决定不读取 inspect 的结果；
- 真正退休的 prefix 叶通过 commit_original_retirement 留下实际记录；
- finish 依据原完整覆盖和全部终叶结果形成局部/全局范围；
- 原 measure/readback/compare 继续原 single-body/partial/原 clock 责任。

**条件结论。** 如果这些真实来源绑定成立，并且某次实际完整覆盖满足(553.15)及上述完整终叶条件，则输出的四块常数是同一当前准确五次前缀、完整系数维度、全物理角和原两反射片的合法有限参考常数，适用范围精确如(553.18)。没有这些实际记录时，本文只是已完成的包含证明和可执行 source 组合，不是实际场证书。

新源没有创建 request、workflow、actual run 或 accepted450。没有本地科学执行、AST/compile、fixture 或额外独立审计门；发布后未来 caller仍须使用真实已接受场和同一原 deadline，而不能凭本结论预填数值成功。
