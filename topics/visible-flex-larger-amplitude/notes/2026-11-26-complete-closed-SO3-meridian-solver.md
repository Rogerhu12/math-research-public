# 固定 deep 标量度量的完整 SO(3) meridian 求解入口

本入口是 R692 的一个独立、可实际求解的闭场表示。它没有给出非圆准确解的存在证明，也不把条件性旋转重建当作课题完成。实际父取公开 Actions 当次完整返回的 fixed-deep 报告与 bundle；可以是原完整 d3 driver 或完整 329e SOC driver，不能拿 moving-mean 父的目标当作 $ds^2+a^2d\theta^2$。当次真实 bundle 字节、carrier、nodes、scalar、完整 canonical definition 与 profile identity 都必须一致。

固定标量是已登记的 R690 profile `383168fbd269d52a16586fca626632c28243bf230df62a5882e7ed2048625d7d`。本文不重证其无限尾结论。原完整正权 legacy/Gauss 测度、全部角点、完整永久地点、原曲率工作行选择算法及幅度预算均保留。新字段的所有数值要重新读取，不能继承父的连续 metric、embedding、reach 或幅度结论。

## 1. 固定的是材料坐标图，当前 core 仍自由

设冻结父的完整 core 系数为 $c^0_m$，$\nu_m=2m$。固定域角 $\phi$ 及材料角图

$$
\theta_0(\phi)=\phi+\sum_m\frac{1-\nu_m^2}{\nu_m}c^0_m\sin(\nu_m\phi),
\qquad
\rho_0(\phi)=1+\sum_m(1-\nu_m^2)c^0_m\cos(\nu_m\phi).
$$

目标在此固定图中为

$$g=ds^2+a_{\rm deep}(s)^2\rho_0(\phi)^2d\phi^2.$$

当前 $c_m$ 的前三项保持原合同的固定值，其余每一项都是自由变量，$H$ 也自由。当前 normal angle $\phi_c$ 由

$$\Theta_c(\phi_c)=\theta_0(\phi)$$

确定。记支持函数 $p_c=1+\sum_m c_m\cos(\nu_m\phi_c)$，$\rho_c=p_c+p_c''$。当前 core 是

$$\Gamma_c=p_c e_r(\phi_c)+p_c'e_\phi(\phi_c).$$

在固定材料角下，全部自由系数的变分为

$$
\delta\Gamma_c=\sum_m\delta c_m\left(
\cos(\nu_m\phi_c)e_r(\phi_c)
-\frac{\sin(\nu_m\phi_c)}{\nu_m}e_\phi(\phi_c)\right).
$$

对固定域角的两个导数为

$$
\Gamma_{c,\phi}=\rho_0 e_\phi(\phi_c),\qquad
\Gamma_{c,\phi\phi}=\rho_0' e_\phi(\phi_c)
-\frac{\rho_0^2}{\rho_c}e_r(\phi_c).
$$

推导使用 $\Gamma_{c,\phi_c}=\rho_c e_\phi$ 和
$\delta\phi_c=-\delta\Theta_c/\rho_c$，不能把当前 $\phi_c$ 或 $\rho_c$ 当常量。实现使用完整 differentiable Newton 迭代；每次求值都读取实际方程残差与实际 root 处 $\rho_c$，超出声明的根容差或失去正性即拒绝该实际数值查询。J 与 J* 是同一个完整离散前向图的导数与转置，包含这条逆图链。有限 Newton 误差没有被冒充为零；稠密 core 正性筛也没有被冒充为连续区间证明。

## 2. 完整单位 meridian 与闭合修正

从一个真正冻结的完整父场定义

$$T_0(s,\phi)=\frac{F^0_s(s,\phi)}{|F^0_s(s,\phi)|}.$$

独立 `so3_parent_meridian_jet.py` 保留父的所有 shared-quintic $q$、所有 core、$H$、完整 $hH+k$ 项和解析 reference。它返回 world Cartesian 中的 $T_0,T_{0,s},T_{0,\phi},T_{0,\phi\phi}$。旧 six-jet 例程是在旋转 $\phi$ 架中表达物理导数，故先支付全部连接项，再统一旋到 world；不能把旋转架分量误作 world 导数。

令

$$T=\exp([\omega]_\times)T_0.$$

$\omega$ 的完整角基是

$$
\omega_x=\sum_{m=0}^M x_m(s)\sin((2m+1)\phi),\quad
\omega_y=\sum_{m=0}^M y_m(s)\cos((2m+1)\phi),\quad
\omega_z=\sum_{m=1}^M z_m(s)\sin(2m\phi).
$$

这些是旋转轴向伪向量在原两次 reflection 和半周旋转下的正确奇偶性。每个径向系数都有原完整网格上的共享 $C^2$ 五次 node value/slope/acceleration 自由 jets，仅固定

$$\omega(0,\phi)=0,\qquad \omega(S,\phi)=\omega_s(S,\phi)=0.$$

当前 core 的位置没有因此被冻结。径向 free 槽数为 $3J-3$，角通道数为 $3M+2$，另有 $M-3$ 个 free core 系数与一个 $H$。没有删除高频，也没有把自由 core 改为前三项之外的常量。

令

$$
P(\phi)=R e_r(\theta_0(\phi))+H e_z,
\qquad
G(s,\phi)=P(\phi)+\int_S^s T(r,\phi)\,dr,
$$

$$
\Delta(\phi)=\Gamma_c(\theta_0(\phi))-G(0,\phi),\qquad
h(s)=1-10(s/S)^3+15(s/S)^4-6(s/S)^5,
$$

并定义真实新场

$$F=G+h\Delta.$$

其完整六 jet 是

$$
F_s=T+h'\Delta,\qquad F_\phi=G_\phi+h\Delta_\phi,
$$

$$
F_{ss}=T_s+h''\Delta,\qquad
F_{s\phi}=T_\phi+h'\Delta_\phi,\qquad
F_{\phi\phi}=G_{\phi\phi}+h\Delta_{\phi\phi}.
$$

这里 $\Delta$ 同时依赖全部 $\omega$、全部 free core 和 $H$。尤其当前 $H$ 的真导数为 $(1-h)e_z$，不是全域 $e_z$。实际 meridian 不再是单位向量：$F_s=T+h'\Delta$。因此不允许使用 $E\equiv1$，也不允许直接套 R692 仅由连接缺陷得到的 $\eta$ 估计去认证最终修正场。

实现使用稳定的同值式。设 $I(s)=\int_0^sT$ 和 $I_*=\int_0^S T$，则

$$F=(1-h)P+h\Gamma_c+I(s)-(1-h)I_*.$$

同样公式用于两个角导数；所有积分和 endpoint correction 都在 J/J* 的前向图中。

## 3. 结构性端口和准确解类的范围

$h$ 在 core 的三 jet 为 $(1,0,0)$，在 cap 为 $(0,0,0)$。固定父满足原 closed 模型的端口，因此

$$T_0(0,\phi)=e_z,\qquad T_0(S,\phi)=-e_r(\theta_0),\qquad T_{0,s}(S,\phi)=0.$$

由于单位向量的导数垂直于自身，core 的 $T_{0,s}$ 水平。给定 $\omega(0)=0$，$T_s(0)=T_{0,s}(0)+\omega_s(0)\times e_z$ 仍水平。因此新场有

$$F(0)=\Gamma_c,\qquad F_s(0)=e_z,\qquad F_{ss,z}(0)=0.$$

这支付了 core 镜接所需的全部三项，而不仅是 $F_z=0$。cap 的 $\omega=\omega_s=0$ 与 $h=h'=h''=0$ 给

$$F(S)=P,\quad F_s(S)=-e_r(\theta_0),\quad F_{ss}(S)=0,$$

连同正确的角混合 jets，匹配同一固定 $R$ 的 R661 $p^4$ cap。周期性由完整三角基和固定图直接给出。当前 $\rho_c>0$ 的连续责任、嵌入、全像幅度、reach、含 reflection 的 E3 非平凡性仍需同场证明；有限点筛不能替代它们。

在连续 $\omega$ 空间中，这个表示包含一个有明确范围的准确等距局部类：若一个满足同一 core/cap 合同的准确等距场 $F_*$ 具有所需的经典 mixed angular derivatives，且 $F_{*,s}$ 与 $T_0$ 处处不反平行，则把 $T_0$ 送到 $F_{*,s}$ 的最短旋转给一个局部连续旋转向量。若需要本文六 jet 的经典计算，可采用足够的更强正则性，例如相应 piecewise smooth 及所用跨胞一阶 meridian jets 连续；不能仅从任意 $C^2$ 推出 $F_{s\phi\phi}$ 存在。准确等距时 $|F_{*,s}|=1$，由同一帽锚点积分得 $G=F_*$，故 $\Delta=0$，没有给准确解额外强加错误的径向位置条件。

有限 $M$/共享五次 $\omega$ 只是所选 trial space 的完整参数，不是原 $q$ 空间的双射，也不是“所有 $C^2$ 闭曲面”定理。一个条件性的逼近说明是：对具有连续 $\omega,\omega_s,\omega_\phi,\omega_{\phi\phi}$ 的对称局部图，保持奇偶性的角 Fejér 截断及保持端口的径向平滑/共享五次加密可逐次逼近这些所需 jets。场公式对这些 jets、严格正 $\rho_c$ 的 core 及正父 meridian 范数连续，因而相应六 jet 也收敛。该条件性密度说明不产生准确非圆解，不替代实际固定目标的数值精化，也不允许把零方向或阈值退出称作下降。

旋转规范没有被删除。一般 $\omega$ 处的无效 infinitesimal chart 方向由右 Jacobian 的 pullback 给出；只有 $\omega=0$ 才简化为字面 $\delta\omega\parallel T_0$。源码保留这些方向，完整正定坐标范数及正 $\mu^2 I$ 支付线性子问题的核。

## 4. 实际 residual、完整自动微分与新范数

实际 residual 全部三分量为

$$
e=|F_s|^2-1,\qquad
b=\frac{F_s\cdot F_\phi}{a_{\rm deep}\rho_0},\qquad
d=\frac{|F_\phi|^2}{a_{\rm deep}^2\rho_0^2}-1.
$$

原正角 orbit 仅乘一次。不存在 moving-mean 投影；所有角零模和非零模都保留。原 R664 正残差 Hessian 接口仅使用新的完整 `residual/jvp/vjp`，不借用旧 $q$ 或旧 current-mean Jacobian。谱参数明确为本分支的 $p,\epsilon,\mathrm{scale}$，原始和 centered Phi 都据同一实际 raw residual 与同一正权计算。默认 $p=4,\epsilon=.001,\mathrm{scale}=.05$。

默认新范数为明确的正节点-jet $H^2$-type 范数：

$$
\sum_{j,m}w_j\sigma_m^2\bigl(
\omega_{jm}^2+\ell^2\omega_{s,jm}^2+\ell^4\omega_{ss,jm}^2\bigr)
+\sum_{m>3}(1-\nu_m^2)^2(\delta c_m)^2+(\delta H)^2,
$$

其中 $w_j$ 是正 Voronoi node mass。每个实际旋转通道频率 $k$ 的权为 $\sigma(k)^2=1+(k/24)^2$，$x/y$ 通道的 $k=2m+1$，$z$ 通道的 $k=2m$，且 $\ell=.05$。它不被称为原 $q$ 的物理母范数，也不被称为精确 Sobolev 积分。所有对角项正，所有声明自由变量保留，实际 $\mu$ 与完整 norm identity 都记录。

另提供显式 `integral` variant：每个 mode 的精确五次多项式积分 $\int(\omega^2+\ell^2\omega_s^2+\ell^4\omega_{ss}^2)$。六点正 Gauss 支付最高十次积；共享五次组装为 bandwidth 5。为 graded mesh 做 $D K D=L L^T$ 平衡，lift 是 $D L^{-T}\sigma^{-1}$，transpose 是 $\sigma^{-1}L^{-1}D$。若普通数值 Cholesky 失败，源码诚实返回错误，不静默改范数。首运行不额外制造 norm fixture。

## 5. 全 C 和共松弛 Phase I

旧 `fullclosed_point_inequalities_v2.py` 的完整选行算法保持原字节身份。它的六 jet 值与 full-free covector 由独立新 world-field adapter 提供，不冒称原 R671 point source。曲率必要行仍是

$$g_i=.03 D_i|\kappa_i|-.992\le0,$$

含所有当前受保护代表和原完整永久点真筛；首版原 selector 的工作行上界固定 192。原行前缀之后追加同 $D_{\rm marked}=4.2,L=.9,H_{\min}=1.01$ 的幅度行。world 见证是 $p=(0,1+\sum c_m,0)$，其依赖支付所有 free core，$\pm p$ 两支都保留。帽半径与 $H$ 行继续保留。每个地点的记忆按 binary64 精确地址，不能 round13 合并。历史 old-normal-angle 的字面数值现在作为固定父 chart 的 $\phi_0$ 地址重新读取；这不声称跨模型的同一物理点。新的极值和永久地点都是固定 $\phi_0$，不是内部随 core 变化的 $\phi_c$。

每一行记录物理有号超量 $g_i$、实际 coordinate gradient norm、正 row normalization scale $s_i$。当前有限场不可行时，不把负 bound 送给要求零点可行的原 QPv3；改解完整共松弛问题

$$g_i+dg_i[Tz]\le\tau_0+\delta\tau\quad\text{对每一个原 typed 行},\qquad \tau_0+\delta\tau\ge0,$$

$$\min\ \tfrac12(\tau_0+\delta\tau)^2+\tfrac12\mu_{\rm rest}^2(\|z\|^2+\delta\tau^2).$$

$\tau_0$ 覆盖真实 selected $\max g_i$，仅加已明确记录的极小正数以初始化数值 slack；这不是物理接受容差。设原行 $C_i=dg_iT/s_i$，则增广行为 $(C_i,-1/s_i)$，右端 $-g_i/s_i+\tau_0/s_i$。正行缩放同时作用两边。源码虚拟提供列块，不复制多 GB 全 C；零物理梯度幅度行也保留，不能借此删除难约束。

Phase I 的线性 slack 不代表新场可行。每个可能接受的 trial 都用真实新场重读完整 metric/domain、全 grid、全部永久曲率/radius 地点、两支幅度和帽条件。只有真实完整 $\max(0,\max g)$ 严格下降才接受 restoration；真实超量降到零后才返回固定标量 Phi 方向。Metric phase 需要真正 Phi 下降且完整几何幅度筛全过。拒绝 trial 新发现的地点永久保留；每个下一方向重新用扩大的全部记忆读取当前父。预算用尽而超量仍正只是一条真实未恢复记录，不能称几何可行或不存在。

## 6. 计算精度、运行和来源边界

数值 meridian 积分按每原胞完整正 Gauss 节点算整胞及 Lagrange partial integral。它是精确积分定义场的普通求值，不是已经证明的积分误差包围。$F_s,F_{ss}$ 等读精确公式的直接 jets，而 $F,F_\phi,F_{\phi\phi}$ 包含数值积分；这些求值的微小微分一致性缺陷也没有被声称为零。root residual、父 meridian 归一化、Rodrigues 的小参数 series、符号物理节点的浮点载体及实际外场全部还需要同场误差预算。后继提升 integration order 不改变固定 $g$ 或场的精确积分定义，但不能用换求值规则后的 Phi 和旧规则的 Phi 直接相减。

CPU runtime 固定 PyTorch 2.5.1，float64，最多四线程。官方 previous-versions 页给出的 CPU 安装形式可重建为：

```sh
python -m pip install --disable-pip-version-check --no-input torch==2.5.1 --index-url https://download.pytorch.org/whl/cpu
```

本入口不需要 torchvision 或 torchaudio。官方 wheel 目录有 Python 3.12 Linux CPU wheel；新 Actions 可明确用 Python 3.12。源码记录实际 torch build、numpy/scipy 版本和线程数。依据是官方 [previous versions](https://pytorch.org/get-started/previous-versions/) 与 [wheel index](https://download.pytorch.org/whl/torch/)；没有本地科学执行。

全部科学初始化、父 jet 读取、线性化、QP、非线性真筛和数值报告只在公开 `Rogerhu12/math-research-public` Actions。源码本地只做文字、AST/compile、来源及参数检查。不增加独立 verification fixture，不把编译成功当作公式或真实场成功。生成的大数组、cache、direction 和 checkpoint 只留 runner。公开结果须由实际报告读取器给 source commit、bundle/report SHA、完整 scalar identity、全记忆计数、Phi/max、QP实际驻定量、restoration slack 与真实超量、实际几何幅度筛和未支付的连续范围。

## 7. 完整源和实际运行接口

六件完整源码如下；每件都低于 100 KB。来源哈希在 driver/launcher/reader 内闭合，不依赖旧 worktree 的绝对源码路径。

| 文件 | SHA256 |
|---|---|
| `so3_parent_meridian_jet.py` | `d3f25bb74e179865b20f7759bc1ee8dcdf2c2771f062ac096ee4d5398a8be4b9` |
| `so3_closed_meridian_operator.py` | `234ac8db3ebc34fc1c146c56bec810f1c777cf6e2689858c7234124eece7ea42` |
| `so3_closed_meridian_geometry.py` | `72f3825913c9ac07b30dcbc47f34e4d8ad901c2f6b6cab0cdc50f35ab99a3cc6` |
| `fullclosed_so3_meridian_qp.py` | `9cf5c8259426cc6130651d60728e96a9c26820baaa10e5c23f22440c5a0a7b4b` |
| `launch_so3_closed_meridian_actions.py` | `9b770c78813ca081beb903d81dad0426110003ac4ec2ee89e1e5d5f4a8816f26` |
| `read_so3_closed_meridian_report.py` | `32bdbb6e60f60ed169bfccae64bd90d20dc17cd9ee3f38fd03a62e1c907a6361` |

`so3_closed_meridian_queue_steps.json` 给完整两步 argv/outputs/summary。首步默认从当次真实 `deep-fixed-scalar-amplitude-first/{report.json,final.npz}` 创建新场，使用同次 `deep-fixed-scalar-prepare-first/{observations.npz,nodes.json,locations.json}`。它不硬指定历史 b788 字节为本次已经复现的结果，而是从当次完整报告核对真正输入。也允许明确改为真实 329e SOC 父及其完整报告；该分支由原 d80 binder 全体重建后绑定，不能仅改报告 schema。

首预算默认一个 metric 方向、16 个 Hessian advances，以及最多四个 64-advance 共松弛 restoration 方向。方向预算可显式提高，所有变量、观测和筛不随预算缩减；到达 iteration limit 只记录实际返回，不解释为能力极限。Phi 门槛在参数文件中为 $10^{-9}$，仍不是 README “原求解容差”或精化完成的替代定义。首版只允许保持父的 full angular count，不把历史 indexed angle 按另一个 $N$ 重解释；跨网格改动需要独立明确的地址迁移。

如 workflow 已安装 CPU torch，直接运行 launcher；否则追加 `--install-torch` 会在同一个公开 Actions 中执行上列明确安装命令。`--print-command` 只作标准库 argv 准备，不读取场或运行 fixture。主运行的控制参数包括 `--directions`、`--maxiter`、`--restoration-directions`、`--restoration-maxiter`、`--damping` 和 `--restoration-damping`。不依赖一个旧 job 的剩余时长来定义算法。

真正同表示续接必须同时提供 `--restart-checkpoint` 和 `--restart-report`，并继续提供原冻结 parent 的完整输入。完整数学 model identity 包含冻结父/T0/chart，不能悄悄换一个更晚父而把它当同一 checkpoint。每次新的数值初值和全部永久地点会重新读取。若换 integration order 或其他明确求值参数，旧保存 Phi 不被借来作新测度差；最终精化声明仍须另给真实共同父测度、固定问题和下降证据。

实际报告先保存完整 source/model/参数，再开始新场的全 metric/geometry 读取。每个 QP advance 输出真实进度；记录 setup/read、完整 row/linearization、QP 和全部 trial 的实际秒数，以及 J/J*、point covector、父 jet 点数和峰值 RSS。Phase I 的 $A$ 只含 slack 分量，所以其实际 J/J* 调用应与 metric phase 区别记录；这不意味着它跳过全 C 或真几何筛。所有连续误差/closure/isometry 声明在当前有限报告中保持未认证。
