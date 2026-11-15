# R133 补篇：四个有序真腰接收映射与完整强误差装配

本篇给出物理 sign $\epsilon=\pm1$ 与波分支 $\sigma=\pm1$ 的四个真腰 receiver。它把已经实际完成的 WT 腰部 normalizer、WX 真腰角变换、FA 截面首遗漏界与 AW/PC/PW 接在同一个 primitive-plus-mean 状态上。SF 的区间残差与接缝费用仍按其完整公式保留；本篇不编造这些尚未评估的数值。

新增的两个具体点是：SF 试探外的 $P=1-\Pi$ 在撤销腰部 normalizer 后留下一个真实腰部有限秩项；而实际状态误差进入 IC 主角坐标时，可以精确消去一对相邻真角算子，从而只对该项收费 $U_{\mathcal H^{-1}}$ 的 $L^2$ 范数。共同根输入因子和共同输入角始终留在右侧。所有旧有限块、两个物理均值和独立 PW 端口保留。

**2026-11-15 共同输入次序补正。** [MS](R133-supplement-exact-Maslov-sign-operator-and-common-input-outgoing-order.md)证明：本文各支先各自除以$\Lambda_\sigma$的费用保持原义；若两支统一使用incoming右归一化，实际out为$U_{R_\Omega}\mathcal B_-Z^{\mathcal S}$，$Z^{\mathcal S}$是无限算子。已付WE费用转为这个common-input out须按MS.34支付右侧同窗因子。完整degree192和$J_F=1024$使实际$T_F^{\pm1}$与原sign投影精确对易，但不能据此跨过$\mathcal S^{-1}$或分支。所有两mean/finite/第二参考输入保留。

## 1. 固定对象、空间与四种标签

采用 AW/SF 的同一已知连续参考
$$
Q_\delta=Q_0+\delta Z_{\rm can},\qquad
|\delta|\le10^{-8},\qquad \eta_{\rm intrinsic}=\eta_0 .
\tag{WY.1}
$$
特征系数 $\eta=-\gamma\langle v\rangle$ 另记，不与固定内禀参数混同。这里没有把已知参考声明为非线性真解。所有主角 $\mathcal H$ 的后继结论只用于原已接受的同一个 selected member。

P22 截面与原输入空间为
$$
r_c=\frac{76285779072683}{320000000000000},\qquad
\mathcal X^s_{97}
=\left\{a:\sum_{|j|\ge97}(1+16j^2)^s|a_j|^2<\infty\right\}.
\tag{WY.2}
$$
写 $\Pi_\epsilon$ 为这个原输入圆上的两个物理 sign 投影。$\sigma$ 是负区间的两个 wave 分支；terminal-Ai/growing 是另一对径向参考列。AW 的 $\iota_{\rm dec}$ 选择 terminal-Ai 输入列，仍保留两种 $\epsilon$、两种 $\sigma$ 和根矩阵产生的 growing 分量。

完整物理密度坐标为
$$
\mathfrak D_rh=(Iw,\Pi w),\quad
w=n_gT(q)h,\quad n_g=\frac{a_{\rm phys}^2}{m^2},\quad
q=\sqrt{-K},\quad m=\langle v\rangle .
\tag{WY.3}
$$
其目标为
$$
\mathcal Y_r=L^2_{\phi,0}(\mathbb C^2)\oplus\mathbb C^2 .
\tag{WY.4}
$$
这不是 raw curvature 的 $L^2$ 窗。原反算
$T(q)^{-1}n_g^{-1}(\partial_\phi u+z)$ 恢复 raw $H^{-1}$ 状态。两个独立 mean 坐标 $z$ 始终存在。

定义一个明确的编码等距同构
$$
\mathscr J(u,z)=u+z\in L^2(\mathbb T;\mathbb C^2),
\qquad
\mathscr J_\sigma(u,z)=u_\sigma+z_\sigma .
\tag{WY.5}
$$
它只把两个 mean 作为常函数附回 primitive 圆，不把 primitive 当作 raw 状态。$\|\mathscr J\|=1$，每个 $\mathscr J_\sigma$ 范数至多一；$\Pi\mathscr J(u,z)=z$，故所有 mean 可原样读回。

## 2. 已有实际输入与尚不相乘的新标量

本篇只读取下列小回执。数值乘积如以后需要单一有向球，应由新的公共 scalar consumer 组合，本篇不重算旧成功科学。

| 输入 | 确切已有用途 |
|---|---|
| [WTA](R133-supplement-actual-right-waist-normalizer-and-complete-two-window-inverse.md)，run43763134339 | 真腰同一个 $T_{J_s}^{-1}$ 在 $L^2,H^{-4/3}$ 的界；两个 fixed 门和独立 dyadic 均完整保存。 |
| WX run43763424840 的 [execution](../notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json) | 真腰 $U_{X_\pm}^{\pm1}$、selected $U_{\mathcal H}^{\pm1}$、共同输入 $\mathcal S^{\pm1}$ 的实际窗口；完整 primitive 两秩项的 unit-multiplier 费用。 |
| FA run43763658978 的 [science](../notes/free_Airy_first_omitted_cut_scalars_ci/run-43763658978-1/actual-scientific-conclusion.json) | 完整 corrected $B_{\rm free}^{[1]}$ 的负窗、SF26 的 $K_c^-$、已经乘同一 TN forward 的实际 raw-cut error。 |
| [AW](R133-supplement-complete-P22-anchored-free-trial-strong-comparison.md) | 同一实际 Poisson 列相对于 P22-anchored free trial 的完整状态误差 $C_{\rm PC}+C_{{\rm ST},4}$。 |
| [PW](R133-supplement-actual-seven-positive-ports-to-complete-waist-density.md) | 七类独立 positive 输入，以及负根区间、finite head、mean、strict-source/jump 的完整腰部密度列。 |
| [SF](R133-supplement-complete-strict-first-symbol-propagation-defect.md) | 精确区间 defect、全部接缝跳和同类型源接收；新积分/跳费尚须实际支付。 |
| [IC](R133-supplement-individual-branch-first-coefficients-and-common-root-normalization.md) | 共同根输入归一化、主角坐标、两秩项及完整有限 border 的有序恒等式。 |

WTA 最终理论原件为 blob `93b5c208f1c4c8b0abae5d256b74a2d1a09ef677`，15465 bytes、SHA256 `f90ba8a15255ec5326b0680f436e8f8ff25dcadad60188a9ecbc3a24bbbb4e39`。其 science 为 `b742d3167f68c05ef197450a3112eb5b8edcacac`，27619 bytes、`2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d`。

WX execution 为 `5121a599896025d90e2861450756a256aaba659d`，43753 bytes、`e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12`；FA science 为 `2001f4e2eeece1cda56b18b90dccab04b7f6d336`，35718 bytes、`2985b74e314f39fc52d587dae193fd5eacb12d75ea42c45bc88fe73848dc64f2`。两者各自成功结论不能扩充为 full incoming inverse。

以下符号代表这些已有球的有向上端，只有名称发生缩写：

- $K_{W,t}$：WTA 中 **固定** $J_s=268435456$ 的同一 inverse 在 $t=0,-4/3$ 上的界。
- $B_{X,0}$：WX 真腰 inverse density 的 $L^2$ 界。
- $B_{H,0}$：WX selected inverse-$\mathcal H$ 输出的 $L^2$ 界。
- $K_{\mathcal S,0},K_{\mathcal S^{-1},-}$：WX 共同输入的正向 $L^2$ 与反向 $H^{-4/3}$ 界。
- $C_c$：FA 的 `complete_same_TN_forward_L2_times_free_cut_upper`，已经恢复同一个 TN forward，不能再乘第二次。
- $K_c^-$：FA 的 `complete_SF26_Kc_minus_corrected_Bfree1_divided_by_ng_once`，它已经除同截面 $n_g$ 一次。

WX 的这些范数均对应真实腰部或真实共同输入，不能用 TC 的 P22 值代替。WX 的 primitive rank 标量只是 multiplier 为一的预算；实际系数范数还须按其定理乘入。

## 3. 非零 leading 因子必须与同一密度对应

[PF20a/b](R133-supplement-pointwise-root-finite-part-and-complete-true-ray-first-coefficient.md) 使用的密度恰为 (WY.3)。原 Airy/root 归一化后的 leading 常数为
$$
\ell_{\sigma,\epsilon}^*
=\frac{\sigma\sqrt2}{i\epsilon}\,
 n_{g,*}\kappa_{\sigma,\epsilon}
 \left(\frac{k_*}{\lambda_*}\right)^{1/4},
\qquad
\lambda_*=(\eta_*^2k_*)^{1/3}.
\tag{WY.6}
$$
原 $n^{7/6}$ 和 nonzero Airy 常数 $\kappa_{\sigma,\epsilon}$ 都在这条原式中。令
$$
E(r)=\exp\!\left(\int_{r_*}^{r}-\frac{2R_0}{m}\,ds\right),\qquad
\ell_{\sigma,\epsilon}=\ell_{\sigma,\epsilon}^*E(0).
\tag{WY.7}
$$
$R_0$ 是完整参考 mean residual，不能令其为零。PF 的 leading 密度方程给出的真腰 leading map 为
$$
\ell_{+,\epsilon}U_{X_-},\qquad
\ell_{-,\epsilon}U_{X_+}.
\tag{WY.8}
$$
$X_\pm$ 是同一原固定腰 convention 的真 root-label maps。两 leading 常数的比是原 Maslov sector，按 $\epsilon$ 保持原位置。

SF 的 ungauged $k(r_c)=1,\ k_r=\ell_0k$ 与 (WY.7) 满足精确关系
$$
E(0)=E(r_c)\frac{n_g(0)}{n_g(r_c)}k(0).
\tag{WY.9}
$$
这是两条实际 leading 密度方程的同初值恒等式。它不是把参考 mean 当真解。WX 给出了该 strict $k$ 的适当方向界、SP/ST 给出 endpoint $n_g$；若尚未支付 root-to-cut 的 $E(r_c)$ 或整个 $\ell_{\sigma,\epsilon}^{-1}$，应单独保留。已有 endpoint $n_g$ 不能重复乘进下面的 density receiver。

定义原 root 输入上的 sign-diagonal 因子
$$
\Lambda_\sigma a=\sum_{\epsilon=\pm1}
                     \ell_{\sigma,\epsilon}\Pi_\epsilon a,
\qquad
K_{\Lambda_\sigma}=\max_\epsilon|\ell_{\sigma,\epsilon}|^{-1}.
\tag{WY.10}
$$
它只作用于原 $\mathcal X_{97}$ 输入；任何补充低频定义都须另列在完整 finite block。非零性已由原 Airy 定义给出，数值 $K_{\Lambda_\sigma}$ 仍需要同对象的严格 lower bound，不能由 unnormalized amplitude 的 upper bound 反推。

## 4. 四个腰部 receiver 的精确次序

采用 SF19 的同一 $J_s$，在 $\mathcal Y_0$ 上定义
$$
\widehat T_0^{-1}
=\operatorname{diag}(T_{J_s}(0)^{-1},1_{\mathbb C^2}).
\tag{WY.11}
$$
两个 normalizer 因子的次序不变。$T_{J_s}$ 保持原 mean-zero 圈，且在有限补空间和两个 mean 上保持身份。

对 $\sigma=\pm$，以 $X_{-\sigma}$ 表示 $X_-$、$X_+$，定义四个原输入 sector 的 receiver
$$
\boxed{\quad
\mathcal R_{\sigma,\epsilon}^{\rm root}
=\ell_{\sigma,\epsilon}^{-1}
 U_{X_{-\sigma}}^{-1}\mathscr J_\sigma\widehat T_0^{-1}:
 \mathcal Y_0\longrightarrow L^2 .
\quad}
\tag{WY.12}
$$
实际 branch 列是
$\mathcal R_{\sigma,\epsilon}^{\rm root}\mathfrak D_0\Psi\Pi_\epsilon$。
$\mathscr J_\sigma$ 必须在完整矩阵 $T^{-1}$ 之后；不能先取 wave row 再撤销矩阵 normalizer。由编码等距性，
$$
\|\mathcal R_{\sigma,\epsilon}^{\rm root}\|
 \le |\ell_{\sigma,\epsilon}|^{-1}B_{X,0}K_{W,0}.
\tag{WY.13}
$$
物理 mean 并未丢失：
$$
\Pi\mathcal R_{\sigma,\epsilon}^{\rm root}(u,z)
       =\ell_{\sigma,\epsilon}^{-1}z_\sigma .
\tag{WY.14}
$$
如选用 mean-identity extension 而非这里明确的 full $U_X$，须同时使用 WX/IC 的
$(X'-1)\Pi$ 或 inverse 对应秩项。两种 realization 不能无代价互换。

这是四个 receiver 的完整定义；没有把 root sign projector 移到腰部，也没有假定真实 circle map 与 Fourier projector 交换。组合两个输入 signs 时使用完整 block operator 或明确的三角/Cauchy 费用；不能凭 sector 数目猜测输出正交。

## 5. 同一个强状态误差及独立端口

SF27 的真实试探为
$$
n_g(0)\mathbb Y_{\rm app}(0)
=n_g(0)\binom{PT_{J_s}(0)V(0)\mathcal B_c}{0},
\qquad
\mathcal B_c=n_g(r_c)^{-1}B_{\rm free}^{[1]} .
\tag{WY.15}
$$
其零 mean 只定义试探；真解的两个 mean、cut discrepancy 和区间 mean source 仍在完整误差中。

AW20 与 SF45 给同一个 operator difference
$$
E_*=\mathfrak D_0\Psi-n_g(0)\mathbb Y_{\rm app}(0),
\tag{WY.16}
$$
$$
\|E_*\|_{\mathcal X_{97}^{-4/3}\to\mathcal Y_0}
\le C_*:=
 C_{\rm PC}+C_{{\rm ST},4}
 +G_{0c}C_c+
 G_1\left(\int_0^{r_c}f_{\rm app}\,dr+\sum_\ell j_\ell\right).
\tag{WY.17}
$$
$C_{\rm PC}$ 和 $C_{{\rm ST},4}$ 是原完整实际球。$C_{{\rm ST},4}$ 已含四个 RR 组成及一次 ST；$G_{0c}C_c$ 只对不同的 FA free-cut error 收一次 ST。$G_1$ 通过 SF39–41 的实际正算法消费一般 primitive/mean source，不把 raw $H^{-1}$ 当作 $L^2$。接缝项没有径向长度因子。

截至本篇，$C_c,K_c^-$、WT、WX 已有完整新实际回执。式 (WY.17) 的 SF 积分与全部 $j_\ell$ 仍须实际收齐；本篇没有评估 $C_*$ 的单一数值。

若有独立端口 $p$，完整式为
$$
\mathfrak D_0\Psi[a,p]
=n_g(0)\mathbb Y_{\rm app}(0)a+E_*a+\mathcal G_{\rm PW}p .
\tag{WY.18}
$$
每个 receiver 的端口列为
$\mathcal R_{\sigma,\epsilon}^{\rm root}\mathcal G_{\rm PW}p$，
按 (WY.13) 乘同一原 PW 列。PW 的七列
$(s,F_c,F_b,B,J_c,J_s,J_u)$ 保持原来源和窗口，此外仍有有限根 head/两 mean 的 $B_F$、负根区间 ordinary/impulse、strict ordinary/impulse。PW 的旧中间截面可以不同于 P22，因为其独立列已直接输出相同 $\mathcal Y_0$；这不允许将其旧 cut fee 替换 SF 的同 P22 cut fee。

actual Poisson 中已存在的非零 $S_{\rm tr}^Y$ 属于 $\Psi$，不能再用一个任意 $L^2$ stable 输入费重复估它，也不能令其为零。只有 IN 的完整 natural-domain 恒等式允许在相应 homogeneous ratio 中取消；WT/WX 的 endpoint inverse 不提供该 stable-factor inverse。

## 6. 把完整 cut first symbol 转成腰部 root first symbol

这一节只作精确有序代数。对某一 $\sigma$ 写
$$
\Phi=\Phi_\sigma(r_c),\qquad
\psi=\psi_\sigma(0),\qquad
X_{-\sigma}=\Phi\circ\psi .
\tag{WY.19}
$$
FA28 的 $B_{\rm free}^{[1]}$ 是明确的两 phase 幅度，经原 other-row 一阶抵消后，own-branch 根输入系数为 P24 的 $C_{\sigma,c}$。这里 $\sigma$ 按 P23a 的实际特征速度标记；FA21 中打印的 plus/minus phase 如需交换，必须先完成这次原有重标。按 PF 的同一 leading 约定，它可写为
$$
n_g(r_c)(\mathcal B_c)_\sigma
=\ell_{\sigma,\epsilon}^*E(r_c)
  U_\Phi(1+M_{C_{\sigma,c}}I)
\quad\hbox{在原 }\epsilon\hbox{ sector 上}.
\tag{WY.20}
$$
这里没有加入 FA26 的 primitive mean rank；该 cut rank 和 first-frame 余项已经在 FA31–32 的完整 cut error 中收费。若改成保留该 cut rank 的 exact-map 版本，应同步从其 norm budget 中移出同一项，不能双收或双删。

令 SF24 的 cut-chart 积分为 $\mathfrak c_\sigma(0)$，并记
$$
g_\sigma=U_\Phi^{-1}\mathfrak c_\sigma(0),\quad
p_\sigma=p_{\Phi^{-1}},\quad
F_\sigma=g_\sigma\otimes p_\sigma
                -(g_\sigma p_\sigma)\otimes1 .
\tag{WY.21}
$$
IC16 的 full-circle primitive 恒等式给
$$
U_\Phi^{-1}(1+M_{\mathfrak c_\sigma}I)U_\Phi
       =1+M_{g_\sigma}I+F_\sigma .
\tag{WY.22}
$$
因此，先不加 SF 外层的 $P$，
$$
\begin{split}
\ell_{\sigma,\epsilon}^{-1}U_{X_{-\sigma}}^{-1}
 n_g(0)(V\mathcal B_c)_\sigma
&=1+M_{C_\sigma}I+R_{\sigma,\rm alg},\\
C_\sigma&=C_{\sigma,c}+g_\sigma,\\
R_{\sigma,\rm alg}
&=M_{g_\sigma}I M_{C_{\sigma,c}}I
                    +F_\sigma(1+M_{C_{\sigma,c}}I).
\end{split}
\tag{WY.23}
$$
径向等式恰为 (WY.9)。原完整 transport 初值识别出这里的 $C_\sigma$ 就是 PF/CT/IC 的同一 first coefficient。它保留 $F_*$，尚未进行共同根输入改变。

给出一个明确足够的强预算。写 $m_{c,t}$ 为 $C_{\sigma,c}$ 在 $H^t$ 的完整乘法范数，$C_I=\sqrt{17}/4$，则
$$
\begin{split}
R_{\sigma,\rm alg}^*
={}&C_I^2\|g_\sigma\|_\infty m_{c,-1/3}\\
&+\left(\|g_\sigma\|_2\|p_\sigma\|_{H^{4/3}}
                         +\|g_\sigma p_\sigma\|_2\right)
                           (1+m_{c,-4/3}/4)
\end{split}
\tag{WY.24}
$$
界住 $H^{-4/3}\to L^2$。第一个 summand 通过两个真实 primitives 的中间窗，第二个是两条完整有限秩行乘右侧同阶因子；没有假定未知最高导数或输出仍然高频。这些系数/行范数仍应由同 cut/transport 对象支付，不能从 terminal coefficient 的一个 upper bound 反解成 cut 组成界。

## 7. SF 外层投影留下的独立腰部 mean rank

因为 $T_{J_s}^{-1}PT_{J_s}=P$，(WY.12) 作用于 (WY.15) 后仍有 $P$。令
$$
v_\sigma=U_{X_{-\sigma}}^{-1}1,\qquad
\rho_\sigma=\Pi(1+M_{C_\sigma}I+R_{\sigma,\rm alg}) .
\tag{WY.25}
$$
利用 $\Pi U_X=\Pi$，精确得到
$$
U_X^{-1}P U_X
 (1+M_{C_\sigma}I+R_{\sigma,\rm alg})
=1+M_{C_\sigma}I+R_{\sigma,\rm alg}
                         -v_\sigma\otimes\rho_\sigma .
\tag{WY.26}
$$
$\rho_\sigma$ 是完整行 functional，最后一项保留其 true transported output。对原 $\mathcal X_{97}$，$\Pi a=0$，且
$$
\Pi(C_\sigma Ia)=-\Pi((IC_\sigma)a).
\tag{WY.27}
$$
所以
$$
\|\rho_\sigma|_{\mathcal X_{97}}\|_{H^{-4/3}\to\mathbb C}
 \le \|IC_\sigma\|_{H^{4/3}}+R_{\sigma,\rm alg}^*,
\qquad \|v_\sigma\|_2\le B_{X,0}.
\tag{WY.28}
$$
这给出了确切可消费的腰部 projection fee
$$
C_{\sigma,\rm proj}
=(1+B_{X,0})R_{\sigma,\rm alg}^*
                   +B_{X,0}\|IC_\sigma\|_{H^{4/3}} .
\tag{WY.29}
$$
它不同于 FA 的 cut primitive rank，也不同于 SF25 的区间 conjugation rank，不能相互删除。对完整低频/mean 输入，(WY.25) 中的 $\Pi a$ 还必须保留在有限 border，而不能继续使用原高输入的简化。

同一根输入归一化后的完整 branch 在 $\mathcal X_{97}$ 上因此为
$$
L_\sigma=1+M_{C_\sigma}I+E_\sigma,\qquad
\|E_\sigma\|\le
 B_{X,0}K_{W,0}K_{\Lambda_\sigma} C_*+C_{\sigma,\rm proj},
\tag{WY.30}
$$
这里 $K_{\Lambda_\sigma}$ 是 (WY.10) 的标量逆界。真实 mean 输出来自实际 (WY.14)，并未由试探的零 mean 设为零。

## 8. 共同根输入和主角：只对状态项作精确取消

沿 IC4–12 选择一个 **root-circle** $J_F\ge97$，
$$
F_*=-\ell_*/(2\eta_*),\quad
A_F=P_FM_{F_*}IP_F,\quad T_F=1+A_F .
\tag{WY.31}
$$
必须实际支付 $m_{F,t}/(4J_F)<1$，$t=0,-4/3$，得到同一 $T_F^{-1}$。根有限项
$$
F_J=M_{F_*}I-P_FM_{F_*}IP_F
\tag{WY.32}
$$
以及 $-M_{\widetilde C_\sigma}I A_F$ 保持 IC9 的有序式，$\widetilde C_\sigma=C_\sigma-F_*$。它们的费用分别为 IC11 和 IC10；不是已经由 WT 的 moving $J_s$ 门支付。

令
$$
\mathcal S=U_{\mathcal H^{-1}}U_{X_-},\qquad
U_{\mathcal H^{-1}}U_{X_+}=U_{R_\Omega}\mathcal S .
\tag{WY.33}
$$
两支采用同一个右因子 $T_F^{-1}\mathcal S^{-1}$，原 Airy/Maslov sector 因子继续按原 sign 顺序保留。任何 $\Pi_\epsilon$、原 $P_{97}$ 都不穿过 $\mathcal S^{-1}$；全 sign block 和原 finite complement 随此坐标一起转换。

只对 (WY.30) 中的实际状态误差，有精确左侧取消：
$$
\begin{split}
\mathcal S U_{X_-}^{-1}
 &=U_{\mathcal H^{-1}},\\
\mathcal S U_{X_+}^{-1}
 &=U_{R_\Omega^{-1}}U_{\mathcal H^{-1}} .
\end{split}
\tag{WY.34}
$$
旋转在这些窗口等距。于是经过原右因子后，这部分完整强费用可以直接取
$$
C_{\sigma,\rm state}^{\rm principal}
=
B_{H,0}K_{W,0} C_* K_{\Lambda_\sigma}
 K_{F,-4/3}K_{\mathcal S^{-1},-4/3}.
\tag{WY.35}
$$
这里没有额外的 $B_{X,0}K_{\mathcal S,0}$。这个取消只作用于实际状态误差；(WY.24)–(WY.29)、IC 的双 primitive 输入修正、根 finite rank 和 primitive conjugation rank仍逐项保留。

例如，若 IC11 的根 finite 项按 norm 收费，一个完整的声明型上界为
$$
\begin{split}
C_{\mathcal E_\sigma}\le{}&
 C_{\sigma,\rm state}^{\rm principal}\\
&+K_{\mathcal S,0}K_{F,-4/3}K_{\mathcal S^{-1},-4/3}
 \left\{C_{\sigma,\rm proj}
 +\alpha_{J_F}\|\widetilde C_\sigma\|_\infty m_{F,-1/3}
 +2C_I\|F_*\|_\infty\Lambda_{J_F+191}^{1/3}\right\}\\
&+\|c_\sigma\|_2\|p_{\mathcal S}\|_{H^{4/3}}
                   +\|c_\sigma p_{\mathcal S}\|_2
 +C_{\sigma,\rm retained}.
\end{split}
\tag{WY.36}
$$
$\alpha_{J_F}$ 和 $\Lambda_j$ 完全按 IC10，$c_i,c_o$ 按 IC23。$C_{\sigma,\rm retained}$ 是尚未纳入前项的原 finite/physical-mean realization/反 sign 行费用，不能默认为零；若这些行保留为 exact border，则不把它们伪装成已付数值。式 (WY.36) 是同一完整对象的若干正预算相加，不从旧 upper bounds 中减出某个分量。

在 IC 声明的 sector/输入 convention 下，得到其
$B_i=1+M_{c_i}I+\mathcal E_i$ 和
$B_o=\zeta U_{R_\Omega}(1+M_{c_o}I+\mathcal E_o)$。
$\zeta$ 保持原 Maslov sector；不把一个依 sign 的 Fourier multiplier 作为全局常数穿过 circle map。完整四个原 sign/branch maps 与全部交叉块才是实际 transformed relation。

## 9. 有限补空间与 mean 的具体位置

原定量 AW/SF 差界定义在 $\mathcal X_{97}$。右乘 $T_F^{-1}\mathcal S^{-1}$ 后，它自然消耗
$$
P_{97}T_F^{-1}\mathcal S^{-1},
\tag{WY.37}
$$
而
$$
(1-P_{97})T_F^{-1}\mathcal S^{-1}
\tag{WY.38}
$$
是完整旧 finite 输入列。不能把 (WY.38) 置零，也不能把它认作新主角的普通 Fourier head。低输入列和 leading finite correction 必须在同一次坐标改变后保留；需要它们进入 high compression 时，使用真实 smooth dual $H^{4/3}$ 行范数。

至少下列各块必须继续存在：

1. 原两个 physical mean 输入/输出及 positive/outer 独立 mean 荷；本篇的 scalar $\Pi$ 不能代替这些匹配行。
2. 原 root/head 和两种 physical sign 的完整交叉块，含 actual stable factor 与 growing 参考分量。
3. TN/SF 的 $F_T,\mathcal F_J$：原 moving 支持界 $J_s+575$；FA 已按 norm 收费的 $F_S$ 只在原 cut 项中收费一次。
4. IC 的 $F_JT_F^{-1}$：原 root $J_F+191$ 的 finite span，右乘后不再声称 finite input support。
5. (WY.25) 的腰部 projection rank、IC16 的两个 primitive ranks，以及 full-density/mean-identity realization 的差秩。
6. 原 $P_{97}$ 被真实坐标运输后的有限行列，和最终 principal cut $J$ 的 high/finite、finite/high、mean 全部 Schur 块。

这些是完整关系的行列，不是“有限所以可以忽略”的余项。WT 在同一 moving $J_s$ 的 inverse、root $J_F$ 和最终 principal $J$ 是不同门。

## 10. 下一次最小输入清单

| 尚需或可直接复用的量 | 最小来源与严格类型 |
|---|---|
| $K_{W,t},B_{X,t},B_{H,t},K_{\mathcal S^{\pm1},t}$ | 直接复制 WTA/WX 成功小回执，不重 endpoint/phase/normalizer。 |
| $C_c,K_c^-$ | 直接复制 FA2 成功同 P22 完整字段，分别用于 (WY.17) 与 SF source；不重复 forward 或 $n_g^{-1}$。 |
| $K_{\Lambda_\sigma}$ | PF20b 原 $\kappa_{\sigma,\epsilon}$、root $n_g,k,\lambda$ 和真实 $E(0)$ 的同族 lower bound；可按 (WY.9) 分解已付 strict 因子，但 root-to-cut 部分仍独立。 |
| $\int f_{\rm app}\,dr+\sum j_\ell$ | SF31–43 的同原 pieces/真实 $dr$/全部 one-sided derivatives、两 mean 源、finite maps 与 genuine joins；不能由腰部 WT 单点 $S_r$ 扩成区间界。 |
| $C_{\sigma,c},g_\sigma,C_\sigma$ 的所需范数 | 同一 FA/P24 cut first coefficient、SF24 完整 transport，或严格证明的同对象重读；保 full mean。SN terminal 单独界不能反推 cut 与 transport 两项。 |
| $J_F,m_{F,0},m_{F,-1/3},m_{F,-4/3}$ | 同 root finite field $F_*$ 的完整乘法费和两 strict tests；不借 $J_s$。 |
| 完整旧 finite/mean/opposite-sign rows | 原 PW/PC/IC 的真实 source/trace 对应和同一变换；norm-paid 与 exact-border 两种记账须一致。 |
| 最终 incoming 与 finite Schur | 只有完整 $C_{\mathcal E_i}$、两个实际 IC33 门和全部 transformed finite rows 之后才可检验；本篇不作该结论。 |

该清单没有请求重算任何旧成功 producer、ray、QR、Green 或既有源积分。新内容是四个 receiver 的确定有序定义、cut first symbol 到 waist first symbol 的完整有限代数，以及 (WY.35) 的真正同坐标取消。每个尚未付量都保留在对应输入位置。


## 11. FA 幅度与 CT、IC、LN 首系数的精确同一性

本节补全 (WY.20)–(WY.23) 的对象识别。沿全实族先保留原频率符号 $\epsilon=\pm1$ 和物理 wave $\sigma=\pm1$；只有最后使用 $\mathcal H$ 时才限制到 WX/IC 的同一 selected parameter。这里不增加任何数值结论。

### 11.1 同一个 cut quotient，没有第二次 primitive 近似

FA21 使用打印的 phase $X+\tau\,2t^{3/2}/3$。PF2 的物理标记是
$\Phi_\sigma=X-\sigma\,2t^{3/2}/3$，故先令 $\tau=-\sigma$。令
$\alpha_{\sigma,\epsilon}^{(0)}$、$\alpha_{\sigma,\epsilon}^{(1)}$
分别为 FA28 在物理 $\sigma$ 行的完整零阶和 $n^{-1}$ 幅度：
$$
\begin{split}
\alpha_{\sigma,\epsilon}^{(0)}
 &=\mathscr J_\sigma A_{-\sigma,0},\\
\alpha_{\sigma,\epsilon}^{(1)}
 &=\mathscr J_\sigma
 \left(A_{-\sigma,1}
       -\frac{S A_{-\sigma,0}}{i\epsilon\,\partial_\phi\Phi_\sigma}\right).
\end{split}
\tag{WY.39}
$$
这里只在两分量幅度上使用行选择 $\mathscr J_\sigma$，不再作用于 adjoined mean 坐标。P23a/FA28 已证明另一行的首阶幅度精确抵消；两波各自的完整 remainder 仍留在 FA31–32。

记 $L_{\sigma,\epsilon,c}=\ell_{\sigma,\epsilon}^*E(r_c)$。PF20a–b 的同一 density leading 方程和 root 初值给
$$
\begin{split}
\alpha_{\sigma,\epsilon}^{(0)}
 &=L_{\sigma,\epsilon,c}\,\partial_\phi\Phi_\sigma,\\
d_{\sigma,\epsilon,c}
 &=i\epsilon\,
       \frac{\alpha_{\sigma,\epsilon}^{(1)}}
            {\alpha_{\sigma,\epsilon}^{(0)}},\\
C_{\sigma,\epsilon,c}
 &=d_{\sigma,\epsilon,c}\circ H_{\sigma,c},
 \qquad H_{\sigma,c}=\Phi_\sigma(r_c)^{-1}.
\end{split}
\tag{WY.40}
$$
这些是已知函数的等式，不是从范数上界相除。第一行的 nonzero scalar、真实正 Jacobian 和原 phase 标记均不能删除。PF11 的 $d_\sigma^{(1)}$ 正是第二行：原 $n^{-1}$ 幅度必须乘 $i\epsilon$，原高度重构、$\kappa_{\sigma,\epsilon}$、$\partial_\phi\Phi_\sigma$ 和 logarithmic primitive 项均在同一 quotient 中。

对原输入基 $e_j(x)=e^{i\epsilon n x}$，$n=4|j|$，有精确的
$Ie_j=(i\epsilon n)^{-1}e_j$。所以
$$
\begin{split}
e^{i\epsilon n\Phi_\sigma}
 \left(\alpha_{\sigma,\epsilon}^{(0)}
             +n^{-1}\alpha_{\sigma,\epsilon}^{(1)}\right)
 =L_{\sigma,\epsilon,c}
 U_{\Phi_\sigma}(1+M_{C_{\sigma,\epsilon,c}}I)e_j .
\end{split}
\tag{WY.41}
$$
这证明 (WY.20) 对 FA28 定义的 finite first-amplitude map 是逐基精确重写。此处的 $I$ 在原输入圆上；并未再把输出 $I(e^{i\epsilon n\Phi}a)$ 作一次渐近替换。FA26 原输出 primitive 的 mean/tail、原 $J$ 的 finite/mean 部分以及 TN 的 $F_S$ 都仍在其已经声明的完整误差或 exact border 中。

### 11.2 两种输入符号给同一实函数

将 PF/CT 的 root-input 系数暂记为 $C_{\sigma,\epsilon}(\rho)$。对每个 $\epsilon$，同一完整 S12 系数满足
$$
\partial_\rho C_{\sigma,\epsilon}
 =-U_{H_\sigma(\rho)}a_\sigma(\rho).
\tag{WY.42}
$$
这是 CT4 的个别 branch 方程，$a_\sigma$ 正是 SF15，不是仅其均值。其右端是同一个实函数，与 $\epsilon$ 无关。PF15、PF18 和固定的 P8 root normalization 分别给
$$
C_{\sigma,\epsilon}(\rho)
 =\frac{\sigma g_0}{3\rho^{3/2}}
  +\frac{\sigma\widehat g_1}{\sqrt\rho}
  +F_*+O_{H^s}(\sqrt\rho)
\quad(\rho\downarrow0)
\tag{WY.43}
$$
对每个固定有限 $s$ 成立。尤其两符号没有可任意再选的不同 finite root 函数。两解之差由 (WY.42) 为径向常数，由 (WY.43) 趋于零，因此
$$
C_{\sigma,+}=C_{\sigma,-}=:C_\sigma.
\tag{WY.44}
$$
同样对复共轭使用 (WY.42)–(WY.43)，得到 $C_\sigma$ 为实函数。Airy/Maslov 的符号依赖仍完整保留在 $\ell_{\sigma,\epsilon}^*$，没有转成一个可越过 circle map 的全局标量。这里的结论不是由两个上界相等或 scalar finite part 相等推得。

### 11.3 SF 的 signed transport 正是 CT 的个别系数

对 $0\le r\le r_c$，同一真特征方程给
$$
\Phi_\sigma(r)=\Phi_\sigma(r_c)\circ\psi_\sigma(r),
\qquad
H_\sigma(r)=\chi_\sigma(r)\circ H_{\sigma,c},
\qquad
U_{H_\sigma(r)}=U_{H_{\sigma,c}}U_{\chi_\sigma(r)}.
\tag{WY.45}
$$
这里使用 $U_\alpha U_\beta=U_{\beta\circ\alpha}$ 的原顺序。
由 $\partial_r=-\partial_\rho$，(WY.42) 在 $r$ 坐标的右端为正。
因此 SF24 的完整有向积分恰给
$$
\begin{split}
C_\sigma(r)-C_\sigma(r_c)
 &=\int_{r_c}^{r}U_{H_\sigma(s)}a_\sigma(s)\,ds\\
 &=U_{H_{\sigma,c}}
       \int_{r_c}^{r}U_{\chi_\sigma(s)}a_\sigma(s)\,ds .
\end{split}
\tag{WY.46}
$$
在 $r=0$，这就是 (WY.23) 的 $C_{\sigma,c}+g_\sigma$。
真实 piece joins 按 PF26/CT4 的连续 first-symbol 规范接合；更高导数跳和 SF 的 trial 跳源保持在原 remainder，不另给一阶常数。径向 $E$、$n_g$、$k$ 通过 (WY.9) 连接 leading；它们不改变 (WY.46) 的 first coefficient，也不获准把其端点逆界设为一。

### 11.4 合并两符号时的实际算子和范数

在原高输入上定义
$$
\Lambda_\sigma
  =\ell_{\sigma,+}\Pi_+
       +\ell_{\sigma,-}\Pi_-,
\qquad
\|\Lambda_\sigma^{-1}\|_{H^t\to H^t}
  =K_{\Lambda_\sigma}.
\tag{WY.47}
$$
两个 $\Pi_\epsilon$ 是原正、负 Fourier 输入投影。
由 (WY.44)，未投影 trial 的两个 first-amplitude sectors 可以写成
$U_{X_{-\sigma}}(1+M_{C_\sigma}I+R_{\sigma,\mathrm{alg}})
\Lambda_\sigma$，恰按 (WY.23) 的原顺序。
因此 (WY.30) 中合并后的完整实际状态误差是
$$
U_{X_{-\sigma}}^{-1}\,
 \mathscr J_\sigma\widehat T_0^{-1}\,
 E_*\,\Lambda_\sigma^{-1}.
\tag{WY.48}
$$
$\mathscr J_\sigma$ 作用于完整 $\mathcal Y_0$；这是先对两个输入符号组成同一算子，再使用同一个完整 $C_*$，不是两个独立 norm 上界相加。于是这一步只收费 $K_{\Lambda_\sigma}$，无需额外 $\sqrt2$。两个 physical wave 输出仍按原共同状态范数或分别指定的 receiver 使用，未声称任意 pair-sum 等于单个分量范数。

后续精确顺序为
$$
\mathcal S U_{X_{-\sigma}}^{-1}
 \mathscr J_\sigma\widehat T_0^{-1}E_*
 \Lambda_\sigma^{-1}T_F^{-1}\mathcal S^{-1}.
\tag{WY.49}
$$
$\Lambda_\sigma^{-1}$ 位于原输入上。对于TF已成的实际双高投影normalizer，完整degree192与$J_F=1024$给$[T_F^{-1},\Lambda_\sigma]=0$，证明见MS.10–12；这个特例不准把sign因子越过$\mathcal S^{-1}$、分支或transported finite rows。应用 (WY.34) 只取消左边相邻的角算子，正好给各自$\Lambda_\sigma$归一后的 (WY.35)。两支同一incoming归一后的实际out必须按MS.16保留右$Z^{\mathcal S}$。

### 11.5 最后才成为 IC、LN 的 signed 系数

先实行 IC9 的完整右输入变换，再令
$\widetilde C_\sigma=C_\sigma(0)-F_*$。
CT6、CT18、PF27 给
$\widetilde f_\sigma=U_{X_{-\sigma}}\widetilde C_\sigma$。
因此同一 selected 角下
$$
\begin{split}
c_i&=\mathcal S\widetilde C_+
    =U_{\mathcal H^{-1}}\widetilde f_+,\\
c_o&=\mathcal S\widetilde C_-
    =U_{R_\Omega^{-1}}U_{\mathcal H^{-1}}\widetilde f_- .
\end{split}
\tag{WY.50}
$$
旋转逆的位置固定。SN20–21 对完整的 selected $\mu$、真实 $j=\mathcal H'$ 给
$$
\begin{split}
\widetilde f_\sigma&=q_\sigma-\frac{\sigma\mu}{2}j,
 \qquad \langle q_\sigma\rangle=0,\\
c_i&=-\frac{\mu}{2}+U_{\mathcal H^{-1}}q_+,\qquad
c_o=+\frac{\mu}{2}
      +U_{R_\Omega^{-1}}U_{\mathcal H^{-1}}q_- .
\end{split}
\tag{WY.51}
$$
这正是 IC23；LN6 使用的是 $c-\mu$，其中 $c=c_o-c_i$。
$q_\sigma$、cut $d_\sigma$、root $C_\sigma$ 和 $c_i,c_o$ 因而不是可以互换名称的四个范数输入。$\langle c_i\rangle=-\mu/2$、$\langle c_o\rangle=\mu/2$ 是这些 scalar functions 的真积分，不代替 $\mathcal Y_0$ 的两个 physical mean ports。

同一函数的 $H^0$、$H^{-1/3}$、$H^{-4/3}$ 乘法预算须分别由其已验证的 $L^\infty$、完整 $\mathcal W_{1/3}$、$\mathcal W_{4/3}$ 输入支付；两个 primitive 的中间窗仍为 $-1/3$。IC26–29/LN8–22 能消费的只是**完成的**同一 SN terminal 四导数列及真实角误差，不能由一个尚未完成的 prefix、单个 $H^3$ 上界反除，或仅差 $c_o-c_i$ 的上界得到两支个别范数。$C_{\sigma,c}$、$g_\sigma$ 和根 $F_*$ 的费用仍对应本篇第10节；当前同一性不补出任何未算数值。

原 $P_{97}$、$\Pi_\epsilon$ 和两个 physical means 全按第9节运输。最终 principal-angle 的 finite/high、high/finite 与 mean Schur 块、完整 incoming inverse 和 complete strong return 仍是独立义务。此次新增证明仅把 FA 的实际 cut coefficient、SF 的 actual transport、CT 的 root-normalized target、IC 的两个个别系数和 LN 的差系数精确接成同一对象。

本节新增 primary 均为已有正文：CT（blob c60256f55e88f985e73ea1881bf5c766c95d3467，17825B，SHA256 341a9463f267d95896d38f5500240e875077b6e6afedbdc1c0625ea24ad10a35），SN（blob 18724d878156db3f57a7d45f98ac49bc071d7092，19046B，SHA256 6e90617095bfea61a916dcba2a5bd5ad162c696e50b03ee15f7fefd40079679c），LN（blob e0ffc101b096d5216cdf690ee84a624310ded477，13407B，SHA256 53a3dd1dd637a61aec843262d51a2686ef9cf13f5478df4c62b93437db1c6da6）。不重复它们的 source、ray、angle、mean 或任何已成功数值。
