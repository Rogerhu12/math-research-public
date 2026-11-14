# R119 续篇：真实负型往返的全参数联立 KAM 与单一目标度量选择

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对前两篇已经构造的真实度量族和全部内部标签，
可以同时选择每个内部负型分量的度量参数，使其**实际非径向两
射线往返**在真实圆周坐标中解析共轭于预先选定的 Diophantine
旋转。所有分量、全部角频和参数之间的交叉依赖在同一个迭代中
保留；没有逐层假定其余参数固定。

关键实际预算为
$$
 \frac{\varepsilon_{j,k}}{\gamma_{j,k}^{\rm D,2}}<2^{-764},
 \qquad
 \varepsilon_{j,k}=2^{80}(j+4)\delta_j^{443/256}e^{-896},
 \quad \gamma_{j,k}^{\rm D}=\kappa_{j,k}/64.
 \tag{K.1}
$$
这里 $\kappa_{j,k}^2\asymp\delta_j^{3/2}/j$ 是已付的真实度量
相位窗。余量的径向指数恰为 $443/256-3/2=59/256>0$。

所得参数对标签连续、局部全纯，并在角平移轨道上保持同一个值。
因此最终选定一个标签后，其整个相位轨道使用同一个选定目标
度量。本文没有证明正型 Airy/幅度 connection 的完整强逆，也
没有完成 core、双 bump 和 regular 帽的最终匹配。

## 1. 真实对象、全部参数和端点约定

依赖已完整证明的
[实际负段参数](R119-supplement-actual-negative-band-metric-parameters.md)
及
[统一全标签图](R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md)。
固定 $\beta=224$、$\|a\|_{\ell^1_{224}}<1/4$，并记
$$
 \overline X(a)=\frac{13}{4}\|a\|_{\ell^1_{224}}<1,
 \quad \alpha=443/256,
 \quad \delta_j=(2/25)2^{-j},\quad
 \eta_j=\delta_j^{3/2}/(4\sqrt2).
 \tag{K.2}
$$
对两端都是真正 $A=0$ 转向点的内部负型分量，使用指标集
$$
 \mathcal I=\{(j,1):j\ge129\}\ \cup\ \{(j,2):j\ge130\}.
 \tag{K.3}
$$
第一类在胞元 $j$ 内；第二类跨过 $j$ 与 $j-1$ 的接缝。
每个分量 $I_i$ 恰含一个已定义的下降段参数。最外的 $(129,2)$
分量在 cut128 截断，本文固定其参数为0，不把这个 cut 的人为
支交换当作已证的 regular 反射。它仍在完整尾图、mean 和所有
端口中保留，后续有限接合须处理它。

实几何参数盒为 $|\gamma_i|\le2^{-16}$，解析证明使用整个复盒
$|\gamma_i|<2^{-15}$。在任一 $I_i$ 内，参考
$$
 q_\Gamma(t)=\sqrt{-A_\Gamma(t)}
$$
取原正实平方根的解析分支。参数仅支撑在严格负型的内部小段，
故所有转向邻域的 $q_\Gamma$ 与原函数准确相同；端点本身不移动。

两射线往返是在同一个真实端点角上把两支接起来的圆周 map。
这一定义完整使用两支实际 ray flow；它本身不宣称 PDE 的 Airy
connection 振幅也是恒等。

## 2. 真正非径向 principal 与完整 return map

在统一完整尾上使用
[实际速度 hodograph](R119-supplement-actual-speed-hodograph-and-quadratic-scalar-phase.md)
的同一个 $\xi=\chi(t,\theta)$。准确 principal 为
$$
 [b(t,\xi)I+c(t)B_0(t)]\partial_\xi,
 \qquad B_0=\begin{pmatrix}0&1\\-A_\Gamma&0\end{pmatrix}.
 \tag{K.4}
$$
其中 $c=\langle J/\sqrt D\rangle^{-1}$，共同漂移 $b$ 没有删除。
全部公式及完整 mean 使用 $w_\Gamma$。它们在上述复盒全纯，并
满足原已付的绝对界
$$
 |c-1|\le256n^2,\quad
 \|b\|_{\mathcal A_2}\le32(1+|A_\Gamma|)n,\quad
 \|b_\xi\|_{\mathcal A_2}\le16(1+|A_\Gamma|)n.
 \tag{K.5}
$$
这里不存在复 $E^{-1}$ 的隐性退化。例如准确恒等式
$$
 \frac{1-v^2}{E}
 =\frac{2K+K^2+2(1+K)U+EU^2+w^2P^2}{J^2}
$$
使原 $H$ 的绝对证明只需 $|E|\le2$ 和同一个 $J$ 小球。

两个真实 ray 方程是
$$
 \dot\xi=-b(t,\xi)\mp c(t)q_\Gamma(t).
 \tag{K.6}
$$
记 $F_+$、$F_-$ 为两支从左端到右端的真实流。完整往返为
$$
 R_i=F_-^{-1}\circ F_+.
 \tag{K.7}
$$
若换回物理角，其准确 map 是
$\chi_-^{-1}\circ R_i\circ\chi_-$。所以两种 map 的旋转相位
相同；没有把端点不同的 hodograph 当成同一个恒等坐标。

## 3. 每个完整负型分量的实际误差

统一图给每胞 $n_j\le2^{64}\delta_j^\alpha e^{-896}\overline X$。
因为 $2^\alpha<4$，跨胞的第二类分量也有
$$
 N_i:=\sup_{I_i}n
 <2^{66}\delta_j^\alpha e^{-896}\overline X.
$$
每胞的 $(1+|A_\Gamma|)$ 积分仍小于 $8(j+4)$；复参数只加
两个 bump 的总绝对变差，已由原严格余量吸收。因此
$$
 I_i^n:=\int_{I_i}(1+|A_\Gamma|)n\,dt
 <2^{70}(j+4)\delta_j^\alpha e^{-896}\overline X,
$$
$$
 D_i:=2^{75}(j+4)\delta_j^\alpha e^{-896}\overline X
 \quad\text{满足}\quad
 \int\|b\|_{\mathcal A_2}dt<D_i,\qquad
 \int\|b_\xi\|_{\mathcal A_2}dt<D_i/2.
 \tag{K.8}
$$
这些积分覆盖两条相邻实际胞元中落在该负型分量的所有平台、
转接及接缝。

设 $S_i=\int_{I_i}c q_\Gamma dt$，$S_i^0=\int_{I_i}q_\Gamma dt$。
完整 mean 的二阶抵消给
$$
 |S_i-S_i^0|\le256N_i I_i^n< D_i/16.
 \tag{K.9}
$$
对任意部分积分，参考复相位的虚部也明确很小。由
$|q_\Gamma-q_0|\le|\gamma\psi_t|/q_0$ 和
$q_0\ge(\sqrt{12}\Delta/\eta)^{1/2}$，
$$
 \int|q_\Gamma-q_0|dt
 <2r_C\sqrt{\eta_j/\Delta_i}<2^{-14}.
 \tag{K.10}
$$
这是实际复 ray 流的角域预算；没有让复参数产生一个未经支付的
大虚平移。

从 (K.6) 中先准确减去标量平移 $\mp\int c q_\Gamma$，其余
Volterra 映射在 $\mathcal A_{7/4}$ 的位移球中收缩：复平移的
虚部与未知位移之和小于 $1/8$，所以所有 $b$ 都在已付宽2内
求值，Lipschitz 积分小于 $D_i/2$。正向和反向都得到真实流，
减去各自准确标量平移后，位移 norm 小于 $D_i$。

将两条完整流按 (K.7) 复合，在宽 $3/2$ 上剩下至少 $1/8$ 的
复合余量。连同 (K.9)，
$$
 \boxed{\quad
 R_i(\xi)=\xi+\Theta_i(\gamma_i)+E_i(\Gamma,a)(\xi),\qquad
 \|E_i\|_{\mathcal A_{3/2}}
 <2^{78}(j+4)\delta_j^\alpha e^{-896}\overline X.
 \quad}                                                         \tag{K.11}
$$
$\Theta_i=-2S_i^0$ 是前篇的真实零标签两射线角。
$E_i$ 对整个 $\Gamma$ 及全部标签联合全纯，不只依赖本层参数。
实数据下 (K.7) 是真实圆周微分同胚。

## 4. 真实参考角可作解析参数坐标

前篇给实导数
$\Theta_i'\in(1/512,1/2)\sqrt{\eta_j/\Delta_i}$。
为作联立解析迭代，还需复逆门。令 $a_i^0=\Theta_i'(0)>0$。
在 $|\gamma|<2^{-15}$ 上，前篇准确积分式的两个相对变化满足
$$
 |\gamma\psi_{tt}/A_t|<1/16,\qquad
 |\gamma\psi_t/A|<1/256.
$$
因为 $|(1+z)^{-3/2}-1|<2|z|$ 于 $|z|<1/256$，逐项积分给
$$
 |\Theta_i'(\gamma)/a_i^0-1|<1/8.
 \tag{K.12}
$$
固定点
$$
 \gamma=\lambda/a_i^0-
       [\Theta_i(\gamma)-\Theta_i(0)-a_i^0\gamma]/a_i^0
$$
于是构造真正的全纯逆 $\gamma_i=G_i(\lambda_i)$，满足
$$
 \Theta_i(G_i(\lambda_i))=\Theta_i(0)+\lambda_i,
 \qquad |\lambda_i|<2\kappa_i,\qquad
 \kappa_i=2^{-25}\sqrt{\eta_j/\Delta_i}.
 \tag{K.13}
$$
理由是 $a_i^0>2^{-8}\sqrt{\eta_j/\Delta_i}$，故
$a_i^0r_C/2>2\kappa_i$。整个逆的像仍在 $|\gamma|<r_C$；
实 $|\lambda_i|\le\kappa_i$ 时甚至有
$|\gamma_i|<(4/7)2^{-16}$。
对全部指标，这定义从加权 $\ell^\infty$ 圆盘
$\sup_i|\lambda_i|/\kappa_i<2$ 到原 $\ell^\infty$ 参数盒的
联合全纯 map。这里没有按 $i$ 丢掉变小的相位尺度。

## 5. 一次选定的全部 Diophantine 目标

把四重商圆写为标准 $2\pi$ 圆，令 $x=4\xi$，
$\Omega_i^0=4\Theta_i(0)$。一次选取
$$
 |\omega_i-\Omega_i^0|\le\kappa_i/2,
 \qquad
 |e^{in\omega_i}-1|\ge\gamma_i^{\rm D}|n|^{-2}
 \quad(n\in\mathbb Z\setminus\{0\}),
$$
$$
 \gamma_i^{\rm D}:=\kappa_i/64.
 \tag{K.14}
$$
每个目标都确实存在，证明如下。若一个正整数 $n$ 违反后式，
则 $\operatorname{dist}(n\omega,2\pi\mathbb Z)<2\gamma_i^{\rm D}/n^2$。
其在整个标准圆上的坏集长度小于 $4\gamma_i^{\rm D}/n^2$。
由 $\sum_{n\ge1}n^{-2}<2$，全部坏集长度小于
$8\gamma_i^{\rm D}=\kappa_i/8$，小于允许区间的长度
$\kappa_i$。补集闭且非空，可以例如准确取允许闭区间中满足
所有不等式的最小实 lift。这样所有 $\omega_i$ 在标签改变前
已经固定，不在迭代中改变小除数目标。

定义真正的全部相位参数
$$
 p_i=4\lambda_i-(\omega_i-\Omega_i^0),\qquad
 \|p\|_{\mathcal P}=\sup_i|p_i|/\kappa_i.
 \tag{K.15}
$$
当 $\|p\|_{\mathcal P}<4$，(K.13) 的逆仍全部合法。
(K.11) 变成一族真实 maps
$$
 \mathcal R_{i,p,a}(x)=x+\omega_i+p_i+f_i(p,a,x),
 \qquad
 \|f_i\|_{\mathcal A_6}<\varepsilon_i\overline X(a),
$$
$$
 \varepsilon_i=2^{80}(j+4)\delta_j^\alpha e^{-896}.
 \tag{K.16}
$$
$f_i$ 依赖所有 $p$；整个族在 weighted $\ell^\infty$ 参数圆盘
上全纯，原函数与所有参数导数均采用完整角 Fourier 和。

## 6. 实际小除数平方预算覆盖全部层

由前篇 $\kappa_i^2>2^{-55}\delta_j^{3/2}/j$，
$$
 \mu:=\sup_i\frac{\varepsilon_i}{(\gamma_i^{\rm D})^2}
 <2^{147}e^{-896}\sup_{j\ge129}
       j(j+4)\delta_j^{59/256}.
$$
最后的序列递减，因为
$$
 \left(\frac{130\cdot134}{129\cdot133}\right)^{256}<2^{59},
$$
而后续多项式比值更小。又
$129\cdot133<2^{15}$、$\delta_{129}<2^{-132}$、
$132\cdot59/256>30$，所以该上确界小于 $2^{-15}$。
使用 $e>2$，得到
$$
 \boxed{\quad \mu<2^{132}e^{-896}<2^{-764}<2^{-64}.\quad}
 \tag{K.17}
$$
这不是只验证有限若干层。完整 $(j+4)$ 费用、相位窗的 $j^{-1}$
及参数之间的联合选择都已进入同一个无限层上确界。

## 7. 全部参数联立的解析圆周 Newton 引理

下面给出本次使用的完整迭代，避免把一个未付常数的 KAM 定理
作为黑盒。设任意可数指标集上的 maps 满足 (K.14)–(K.16)，
$0<\kappa_i<1$，且 $\mu\le2^{-64}$。则存在同一个参数向量
$p^*$ 及解析圆周微分同胚 $h_i(x)=x+u_i(x)$，使
$$
 \mathcal R_{i,p^*,a}\circ h_i=h_i\circ T_{\omega_i}
 \quad\text{对全部 }i,
$$
$$
 |p_i^*|<16\varepsilon_i\overline X,\qquad
 \|u_i'\|_{\mathcal A_{3/2}}<2^{18}\mu<1/8.
 \tag{K.18}
$$
并且 $p^*,u_i$ 对辅助标签局部全纯、实数据下为实。

### 7.1 完整联立平均行

初值 $p^{(0)}=0,h_i^{(0)}=\mathrm{id}$。记第 $n$ 步误差
$$
 E_i=\mathcal R_{i,p,a}\circ h_i-h_i\circ T_{\omega_i},
 \qquad \|E_i\|_{\mathcal A_{s_n}}\le e_n\varepsilon_i,
$$
$$
 s_0=2,\quad d_n=2^{-n-4},\quad s_{n+1}=s_n-4d_n,
 \qquad s_n\downarrow3/2.
 \tag{K.19}
$$
在迭代内保持 $\|h_i'-1\|<1/8$、$\|p\|_{\mathcal P}<1$。
写 $H_i=h_i'\circ T_{\omega_i}$。对参数方向 $q$，准确的当前
复合点参数列为
$$
 \mathsf C_i^h[q]:=(D_pf_i(p,a,\cdot)[q])\circ h_i,
 \qquad
 (D_p\mathcal R_i[q])\circ h_i=q_i+\mathsf C_i^h[q].
$$
原参数盘与宽6角域均留有固定余量，且 $h_i$ 的像仍在该角域，
故参数 Cauchy 和真实复合给
$\|\mathsf C_i^h[q]\|\le\varepsilon_i\|q\|_{\mathcal P}$。
令
$$
 d_i^0=\langle H_i^{-1}\rangle,\quad
 B_i(q)=\langle H_i^{-1}\mathsf C_i^h[q]\rangle,
 \quad r_i=-\langle E_i/H_i\rangle.
$$
所有参数同时解
$$
 d_i^0 q_i+B_i(q)=r_i\qquad(i\in\mathcal I).
 \tag{K.20}
$$
因为 $|d_i^0-1|\le1/7$、$\|H_i^{-1}\|<2$，
在 $\mathcal P$ 中的非对角部分 norm 至多
$4\nu$，其中 $\nu=\sup_i\varepsilon_i/\kappa_i\le\mu$。
故 Neumann 逆严格存在。完整 row bound 给
$$
 \|q\|_{\mathcal P}\le8e_n\nu,\qquad
 |q_i|\le8e_n\varepsilon_i.
 \tag{K.21}
$$
后一个逐行界需要保留：先用 weighted 逆得到第一式，再代回
(K.20)，得
$|q_i|\le4e_n\varepsilon_i+32e_n\nu\varepsilon_i
 <8e_n\varepsilon_i$。因此没有用浅层误差替代每个深层自己的
小误差。

### 7.2 全频非平均行及真实修正

准确求解
$$
 v_i-v_i\circ T_{\omega_i}
 =-E_i/H_i-(q_i+\mathsf C_i^h[q])/H_i,\qquad \langle v_i\rangle=0.
 \tag{K.22}
$$
(K.20) 保证右侧的完整平均恰为0；不是删掉一个未满足的源行。
右侧 norm 小于 $20e_n\varepsilon_i$。所有非零 Fourier 模
直接除以 $1-e^{im\omega_i}$，由 (K.14) 得
$$
 \|v_i\|_{s_n-d_n}
 \le20e_n\varepsilon_i(\gamma_i^{\rm D})^{-1}d_n^{-2}.
 \tag{K.23}
$$
这里使用 $\sup_{m\ge1}m^2e^{-d_nm}<d_n^{-2}$。
更新
$$
 p^{\rm new}=p+q,\qquad h_i^{\rm new}=h_i+h_i'v_i.
$$
在再缩小一个 $d_n$ 后，
$$
 \|\delta h_i\|\le32e_n\varepsilon_i(\gamma_i^{\rm D})^{-1}d_n^{-2},
 \quad
 \|\delta h_i'\|\le32e_n\varepsilon_i(\gamma_i^{\rm D})^{-1}d_n^{-3}.
 \tag{K.24}
$$

### 7.3 真实二次误差和无穷步闭合

微分当前误差有准确恒等式
$$
 (\mathcal R_{i,p,a}'\circ h_i)h_i'
       =H_i+E_i'.
$$
因此 (K.22) 消去线性项后，剩余恰为 $E_i'v_i$ 加真实 Taylor
二阶余项。前者至多
$20e_n^2\varepsilon_i^2(\gamma_i^{\rm D})^{-1}d_n^{-3}$。
函数 $f_i$ 在宽6、参数盘4上已有统一界；在当前宽度和参数球
中，空间/weighted 参数联合二阶导的 norm 至多 $4\varepsilon_i$。
所以 Taylor 余项至多
$$
 4\varepsilon_i
 (\|\delta h_i\|+\|q\|_{\mathcal P})^2.
$$
所有比较与复合均在 (K.19) 留出的余宽内进行；
$\|h_i-\mathrm{id}\|<1/8$ 使原宽6还留有超过3的额外余量。
(K.21)、(K.24)、$\varepsilon_i/\gamma_i^{\rm D}\le\mu$ 给
$$
 e_{n+1}\le2^{14}\mu d_n^{-6}e_n^2.
 \tag{K.25}
$$
例如两类项的常数可分别取20和6400，和小于 $2^{14}$。

$e_0\le\overline X\le1$ 且 $\mu\le2^{-64}$ 时，直接归纳
$$
 e_n\le\overline X\,2^{-8n}.
$$
确实，(K.25) 的右端至多
$\overline X^2 2^{-26-10n}\le\overline X 2^{-8(n+1)}$。
全部参数修正和一阶角导修正的和分别小于
$$
 16\varepsilon_i\overline X,\qquad
 2^{18}\mu<1/8.
$$
这些界同时验证所有迭代球和复合域前提。于是完整序列在
$\mathcal P$ 和宽 $3/2$ 的解析角空间中收敛，误差趋0，证明
(K.18)。每步都使用全 Fourier inverse 和全参数平均行。
其局部一致收敛也证明辅助标签的全纯依赖。此引理证毕。

## 8. 真无限参数、真实 $C^2$ 目标及同一相位轨道

将引理用于 (K.16)，定义
$$
 \lambda_i^*(a)=\frac{\omega_i-\Omega_i^0+p_i^*(a)}4,
 \qquad \Gamma_i^*(a)=G_i(\lambda_i^*(a)),
 \quad\Gamma_{129,2}^*(a)=0.
 \tag{K.26}
$$
$|\omega_i-\Omega_i^0|\le\kappa_i/2$ 且
$|p_i^*|\ll\kappa_i$，所以所有最终实参数严格落在
$|\gamma_i|<2^{-16}$。若 $\Gamma_i^0=G_i((\omega_i-\Omega_i^0)/4)$，
还可记录
$$
 |\Gamma_i^0|<2^{-19},\qquad
 |\Gamma_i^*(a)-\Gamma_i^0|
 <2^{-14}\frac{\varepsilon_i}{\kappa_i}\overline X(a).
 \tag{K.27}
$$
第二式使用真实逆导数 $512\sqrt{\Delta_i/\eta_j}$，未把相位
参数和 log-profile 参数混作同一单位。

所有分量同时选定，且前篇已证明任意无限参数的 $C^2$ 参考
profile 与联合真实尾。故 (K.26) 定义实际单个目标
$g_{\Gamma^*(a)}$ 和它的全标签尾，没有留下“取有限参数以后
再猜一个极限”的步骤。

整个参数选择还具有重要的准确等变性。将输入标签按物理角平移
$\varphi$ 变为 $a_m\mapsto e^{im\varphi}a_m$。真实方程、mean
小根和 hodograph 都与此平移交换，所以各 $f_i$ 只被标准圆上的
同一个平移共轭。迭代从 $h_i=\mathrm{id},p=0$ 开始；平均读取、
同一个 Fourier cohomological inverse、(K.20) 的完整参数逆都
与角平移交换。逐步归纳得到参数增量 $q$ 完全不变。因此
$$
 \boxed{\quad
 \Gamma^*((e^{im\varphi}a_m)_m)=\Gamma^*(a).
 \quad}                                                         \tag{K.28}
$$
一旦某个标签 $a_*$ 被最终全局问题选定，它的整个相位轨道都
对应同一个 $g_{\Gamma^*(a_*)}$。这不等于已经找到满足全局
core/帽匹配的 $a_*$；它支付的是联合构造中的固定目标要求。

## 9. 实际圆周 return 的全频逆及其正确 mean

在 hodograph 角中置 $H_i(\eta)=h_i(4\eta)/4$，再用实际左端
逆 hodograph 得物理角图
$$
 K_i=\chi_{i,-}^{-1}\circ H_i.
$$
它们是真实解析微分同胚，至少在角宽 $3/8$ 上有已付定义域，
其一阶导与1的差小于 $1/8$ 加已付的 hodograph 极小量。
物理两射线 map 准确满足
$$
 R_i^{\rm phys}\circ K_i=K_i\circ T_{\omega_i/4}.
 \tag{K.29}
$$

因此圆周标量方程 $u\circ R_i^{\rm phys}-u=f$ 的真实可解
平均条件是
$$
 \langle f\circ K_i\rangle=0.
 \tag{K.30}
$$
不是原角上的 $\langle f\rangle=0$。在此条件下，用所有
$m=4n\ne0$ 的 Fourier 系数及 (K.14) 求逆，取
$\langle u\circ K_i\rangle=0$。若定义实际 pullback norm
$\|f\|_{K_i,s}=\|f\circ K_i\|_{\mathcal A_s}$，则
$$
 \|u\|_{K_i,s-h}
 \le(\gamma_i^{\rm D})^{-1}h^{-2}\|f\|_{K_i,s}
 \quad(0<h<s<3/8).
 \tag{K.31}
$$
这是全频、实际相位下的圆周 inverse。它只反演这个圆周
cohomological 因子，不是已反演整个两场 mixed radial 系统。
常数行仍由 (K.30) 明确显示，不能顺便当作 holonomy 行已满足。

## 10. 两个真实迹、positive DN、ordinary source 与 mean

所有角共轭都作用在完整函数上，不要求同宽 pullback 与恒等的
算子差小。对任何实际端点角图 $\theta=K(\eta)$，高度是函数，
原始 conormal flux 是密度：
$$
 f^{\rm new}=f\circ K,\qquad
 p^{\rm new}=K'\,p\circ K.
 \tag{K.32}
$$
准确地
$$
 \int p^{\rm new}f^{\rm new}d\eta=\int pf\,d\theta,
 \qquad \langle p^{\rm new}\rangle=\langle p\rangle=\dot M.
 \tag{K.33}
$$
最后一个等式针对固定已选 $g_\Gamma$ 的 Jacobi 高度变化；若还
微分度量参数，则须连同背景 $w_\Gamma$ 的变化微分完整 $M$，
不能只取这个高度偏导。
高度平均一般改变，必须读出 $\langle f\circ K\rangle$；没有
将两个 mean 高度同时设为0。独立轴向平移和完整 normal/shear
重建始终由原两迹及同一 holonomy 输出确定。

相邻正型分量的两端可能使用不同的 $K_-,K_+$。原
[真实两端 weak DN](R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md)
必须对两个端点整体使用 (K.32)，其完整 $2\times2$ Fourier
参考矩阵中的非对角 $-1/\beta_m$ 不删除。将参考 trace norm
与实际 DN 同时按这两个端图传输，原相对 form 估计原样保持，
因为这是准确双端 dual pairing 的坐标变化。传输后的参考 DN
一般不再对原 Fourier 基对角，不能另换回旧对角乘子。

普通径向 source 在任何完整角坐标变化下也按密度 Jacobian
传输，其作用在测试高度上的积分准确不变。于是原
$\dot M_t=w^2\langle D^{-3/2}J e\rangle$ 及 positive 区
完整 outward-flux/source 电荷关系仍成立。本文没有将 ordinary
source 改称端口跳量，也没有假设任意 metric-source 已属于前篇
的强空间 $\mathcal T_{224}$。

本次只把 KAM 图固定在端口及实际 ray return 上。若要在整个
radial 系统中推广为时间依赖 frame，还必须保留该 frame 的
$t$ 导数、退化 Airy 权及完整 lower-order 矩阵；(K.31) 不会
自动消去这些项。

## 11. 与最终全局问题的准确关系

本篇已经支付了先前未知的实际主相位问题中的一块：全部内部
负型分量、实际非径向 ray flow、无穷互相耦合的度量参数及
全频小除数同时闭合，并且最终参数在相位轨道上不变。

仍须处理的完整对象有：正型两端 DN 与已安装 strong Airy
端口空间的统一比较、turning 的两分支幅度/源连接、最外
cut128 分量的真实 regular 条件，以及对新 $\Gamma^*$ 重新
选定 connector 停止位置、物理尺度、双 bump 和 critical-fourth
匹配。旧 R11/R74 的真实第四方向不会因端 jets 未变而自动
保持；新图必须与这些有限条件联合选取。

如果后续 Newton 迭代把 $\Gamma$ 也作为构造未知量，最后目标
是它收敛后的 $g_{\Gamma_\infty}$。本文没有在一个声称固定
$g_0$ 的 Newton 步中更换它，也未证明任意原度量附近已有同样
的强逆。课题的闭面、可见幅度和 reach 完成标准仍由最终全局
构造支付。

## 12. 准确预算脚本

`scripts/fourfold_joint_negative_return_kam_20261113.py` 核对实际
角窗、复参数 inverse 门、全部层的小除数平方余量、联立平均行
Neumann 门、每步二次余项和无穷步收敛预算。输出为
`notes/2026-11-13-R119-joint-negative-return-kam-budget.json`。
完整 Fourier、无限参数和真实两支流的证明在本文，程序不使用
有限谱或浮点 ray 采样代替它们。
