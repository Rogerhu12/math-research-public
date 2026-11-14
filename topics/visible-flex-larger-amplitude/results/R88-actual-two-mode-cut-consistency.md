# R88：实际两模外投影解的 cut 参数一致性

作者：/root（GPT-6 Astra Pro，AI 辅助），2026-11-12。

**已证明：条件两模边值问题及其实际 cut 参数同时闭合。** 使用 R39/R74 同一真实度量、R84/R86 的实际两胞元、原固定外高度及完整真内头反馈。对其余十八个原参数的每个给定值，存在唯一的归一半径 $3/4$ 内 selected 参数，使 R86 的两模外投影解在真实 cut 的高度等于传给真内头的同一参数。selected 两条斜率条件也因此与该真内头相容。

所固定的其它模式仍是外部给定函数；本文不证明其余44条低模方程和切口、高频外 PDE、外胞元0至9或闭曲面。本文的真实度量属于 q085/M20 精确内头，不能转借给 q096 数值分支。

## 1. 同一空间、参数和边界问题

全部符号和真实源采用 [R84](R84-actual-two-cell-whole-field-wronskian-green.md) 与 [R86](R86-actual-two-mode-outer-projected-field-ball.md)。内端 $b$ 是真实 node12，外端 $R$ 是真实 node10；$S=\{2,4\}$。强高度范数为

$$
 \|Z\|_{\mathcal X}
 =\sum_m(1+m)e^{m/64}
 \left(\sup_{I,r\in I}\frac{|P_m(r)|}{V_I}
       +\sup_{I,r\in I}\frac{|K_m(r)|}{V_I}\right),
 \quad P=h_\theta/(rw),\quad K=h_{\perp,r}/w.       \tag{88.1}
$$

$V_I$ 是原10793叶上同一个准确正 dyadic 包络。每个分量先取全径向 supremum，再求和；两个分量来自同一高度函数。

[R74](R74-actual-anisotropic-moving-centre-family.md) 的二十个原中心为 $a_m^*=q_m^*\ne0$，半轴为 $A_m>0$。写

$$
 a_m=a_m^*+A_m\xi_m,\qquad |\xi_m|\le r_0=3/4,
 \qquad \epsilon_m=A_m/|a_m^*|.
 \tag{88.2}
$$

其中 $\epsilon_4=1/16$，其它十九个 $\epsilon_m=1/1024$。原兼容候选相应为 $C_\xi$；每个原模式只乘 $a_m/a_m^*$，故全部候选倍率的绝对值不超过 $\sigma=17/16$。模式42至92及高外场暂置零。

固定 $\xi_T$，其中 $T=\{6,8,\ldots,40\}$。把 $C_{\xi,T}$ 当作给定函数，只有两个 selected 高度 $Y_S$ 未知。令 $L_{R,S}$ 为原固定外目标 $Q_m^{\rm out}$ 的真实 linear-head lift，$\beta_S(a)$ 为 [R78](R78-anisotropic-true-cut-holomorphic-interface.md) 真内头相对准确线性头的完整非线性 $K$ 位移。绝对高度方程为

$$
 Y_S=L_{R,S}+G_SN(Y_S+C_{\xi,T})+B_{h,S}\beta_S(a).
 \tag{88.3}
$$

$N$ 始终由完整 mean 小根及完整 Wiener 逆定义。R86 的修正 $z_S=Y_S-C_{\xi,S}$ 满足其原式(86.1)，故对每个给定的完整 $\xi$，存在唯一的球内解，并且

$$
 \|z_S\|<B_{86}<13.759352693418<16.               \tag{88.4}
$$

实际内端高度尚未在这一步假定等于 $a_S$。

## 2. 为什么 selected 候选的参数依赖准确消失

从 R86 修正方程加回 $C_{\xi,S}$，立即得到(88.3)。其右侧的外目标始终是原固定 $Q_m^{\rm out}$；没有随参数改变目标。由于 $\xi_T$ 已固定，$C_{\xi,T}$ 不依赖 $\xi_S$。因此 selected 参数只经真内头的 $\beta(a)$ 进入绝对场方程。

这项消去是代数恒等式。它不允许删掉 $\beta$、其它十八个函数、完整 mean 或非线性逆，也不允许把 R81 候选边界映射的导数直接当作真实外解的导数。

## 3. 真正重算的线性中心和完整源

定义

$$
 Z_0=L_{R,S}+C_{*,T},\qquad C_*=C_{\xi=0}.
 \tag{88.5}
$$

在全部18组、10793个原 source 叶上，重新由实际五正矩恢复 $C_*$，并只把 m2、m4 替换为真实 $L_R$。真实列使用 R84 已保存的全位置物理 $P,K$ 包围；两端目标、共同动量尺度、分母和源坐标均不变。

为说明源没有作二次截断，记 $T=P_\theta$、$U=K_\theta-P$、$E=1+w^2$、$s=r_x/r$ 和 $\ell=w_x/w$。其非 mean 二次分子是

$$
 Q=EsU^2+
 \ell\left((K+T)^2+w^2(2KT+T^2-P^2)\right).       \tag{88.6}
$$

完整源为 $N=(Q+B_c)/(1+L_c)$，其中 $B_c$ 和 $L_c$ 保留完整 mean。若原 Wiener 强范数上界为 $R_0<1/64$，则原完整小根给 $|c|\le4R_0^2$。令 $\widehat L\ge\|L_c\|<1$、$\widehat Q\ge\|Q\|$ 和 $\widehat B\ge\|B_c\|$。于是

$$
 \|N-Q\|
 \le\frac{\widehat B+\widehat L\widehat Q}{1-\widehat L},
 \qquad
 \|N\|\le\frac{\widehat Q+\widehat B}{1-\widehat L}.
 \tag{88.7}
$$

程序对中心的全部二十个输入模式作准确有限 Fourier 卷积，计算(88.6)的所选系数，并用(88.7)包围全部 mean 与无限逆余项。每个系数再与完整源总范数界相交。真实 metric 平方根域、mean 域和 inverse leading norm 都逐叶严格核销。有限输入的二次项可准确有限卷积，并不意味着完整输出源被截断。

本次新源与 R79 的旧 $N(C_*)$ 不同，后者的中心切口值没有被借来代替新计算。

## 4. 有符号整场和切口泛函

沿用 R84 的真实列 $\phi_m,\chi_m$ 和唯一全局 Wronskian $W_m\ne0$，源系数为同一 $J_m\,dx$。对新中心源 $N_0=N(Z_0)$，令

$$
 I_{\phi,m}=\int_b^R\phi_{q,m}J_mN_{0,m}\,dx,\qquad
 I_{\chi,m}=\int_b^R\chi_{q,m}J_mN_{0,m}\,dx.
 \tag{88.8}
$$

若一个子片上 $N_{0,m}\in[c-d,c+d]$，则

$$
 \int_I kN_{0,m}\,dx
 \in c\int_I k\,dx+
 [-d\!\int_I|k|\,dx,\ d\!\int_I|k|\,dx].
 \tag{88.9}
$$

这同时保留核的符号和源区间不确定性。部分子片积分用该片完整绝对质量控制。前缀、后缀都按真实向外次序累加；删除后缀中已加入的分项时，删除它当初加入的两个端点，而非把含相同误差的区间独立相减。

对目标所在子片的两个有序分支分别使用 R84(84.9)，再对每个 $P,K$ 分量分别取全径向最大值。这给

$$
 g_0\ge\|G_SN_0\|_{\mathcal X_S}.
 \tag{88.10}
$$

内端读出符号直接来自同一 Green 恒等式：

$$
 Q_{b,m}(Y)=
 \frac{Q_m^{\rm out}}{S_{0,m}(R)}
 +\frac1{W_m}\int_b^R\chi_{q,m}J_mN_m(Y+C_{\xi,T})\,dx
 +\mathcal B_{b,m}\beta_m(a).
 \tag{88.11}
$$

R79 的 saved signed source 定义成负积分；(88.11)使用正积分。不能混用两种符号。记准确新中心偏差

$$
 d_m^0=
 \frac{Q_m^{\rm out}}{S_{0,m}(R)}
 +\frac{I_{\chi,m}}{W_m}-a_m^*.
 \tag{88.12}
$$

整个消费者保留全部10933个真实子片（含8个临界条带），不是只作端点检查。

## 5. 同一完整域内的新小导数与场偏离界

R86 给原强源的完整 $\rho=16$ 导数界。已实际支付的全46物理弱源 Green 预算在同一个 $V_I$、同一源和同一参数倍率 $\sigma$ 下，另给两 selected 输出的界。两者都是(88.1)同一范数的合法上界，所以可以取较小者：

$$
 \|G_S DN(Z)\|_{\mathcal X_{92}\to\mathcal X_S}
 \le\gamma<5.564860594563\times10^{-5}<1.
 \tag{88.13}
$$

这里 weak 指源的角权，不是悄悄改变未知场的强范数；输出仍恢复 R84 的 $(1+m)e^{m/64}$ 权。新预算准许全部46个输入方向，故也准许(88.3)所需方向。

原候选各模式分量的全径向质量已在新中心恢复时保存。定义

$$
 \Delta_T=
 r_0\sum_{m\in T}\epsilon_m
 \bigl(M_{m,P}+M_{m,K}\bigr),
 \qquad
 \|C_{\xi,T}-C_{*,T}\|\le\Delta_T.
 \tag{88.14}
$$

为了合法沿线段使用(88.13)，对给定 $\xi_S$ 取参考候选
$\bar C=C_{(\xi_S,0_T)}$。R86 已给

$$
 \|Z_0-\bar C\|
 =\|L_{R,S}-C_{\xi,S}\|<11.460131668293<16,
 \tag{88.15}
$$
$$
 \|Y_S+C_{\xi,T}-\bar C\|
 \le B_{86}+\Delta_T<16.                         \tag{88.16}
$$

因此连接这两个完整状态的线段都在以同一允许候选 $\bar C$ 为中心的合法闭球内。这个论证同时付清 rest 变化，未把两种候选中心混为一个。

令 $h=\|B_{h,S}\beta_S(a)\|$ 的 R78/R84 完整统一上界。由(88.3)、(88.10)、(88.13)–(88.16)，

$$
 \|Y_S-L_{R,S}\|
 \le g_0+\gamma\bigl(\|Y_S-L_{R,S}\|+\Delta_T\bigr)+h.
$$

故

$$
 \|Y_S-L_{R,S}\|\le
 \zeta:=\frac{g_0+\gamma\Delta_T+h}{1-\gamma}.      \tag{88.17}
$$

实际结果的向外放宽显示值为：

| 量 | 上界 |
|---|---:|
| $g_0$ | $1.237729324074\times10^{-13}$ |
| $\Delta_T$ | $6.779149640240\times10^{-13}$ |
| $\zeta$ | $1.238181159256\times10^{-13}$ |
| $\gamma$ | $5.564860594563\times10^{-5}$ |

严格比较使用完整 Fraction，展示小数不作为门。

## 6. 真切口映射与其完整导数

令 $D_m$ 是完整非线性切口泛函对(88.1)单位场方向、再除真实轴 $A_m$ 的合法统一上界。它由旧完整强源切口密度与已付新物理 weak 密度两种合法上界取较小者；所有实际 Wronskian 和正轴保留。

在固定 $\xi_T$ 后，定义

$$
 \Psi_m(\xi_S;\xi_T)
 =\frac{Q_{b,m}(Y(\xi))-a_m^*}{A_m},
 \qquad m=2,4.                                  \tag{88.18}
$$

令 $v_m$、$v'_m$ 分别为 R78 的完整直接 head 切口值界和导数界，$h'$ 为 R84 的完整 head 整场导数界。由(88.11)–(88.17)，

$$
 |\Psi_m|
 \le \frac{|d_m^0|}{A_m}
       +D_m(\zeta+\Delta_T)+v_m=:U_m.             \tag{88.19}
$$

注意 $\zeta+\Delta_T$ 与中心残差 $d_m^0$ 是不同费用，二者都保留；$v_m$ 包含真实非线性 far 和全频内头修正。

R86 的固定点位于严格球内部，且完整源在合法复域全纯，故参数依赖可由统一收缩或隐函数定理微分。对 selected 参数方向微分绝对方程(88.3)：

$$
 D_{\xi_S}Y
 =G_SDN(Y+C_{\xi,T})D_{\xi_S}Y
  +B_{h,S}D_{\xi_S}\beta(a).
$$

其余十八个函数固定，没有候选 selected 导数残项。因此

$$
 \|D_{\xi_S}Y\|\le\frac{h'}{1-\gamma},
 \qquad
 \|D_{\xi_S}\Psi_m\|_{\ell^\infty\to\mathbb C}
 \le D_m\frac{h'}{1-\gamma}+v'_m=:\lambda_m.
 \tag{88.20}
$$

R78 的 Cauchy 导数本来允许二十个归一参数同时变化；限制为两个方向仍有效，不遗漏额外方向因子。

实际有理消费者对每一行分别核销

$$
 U_2\le3/4,\qquad U_4\le3/4,\qquad
 \lambda_2<1,\qquad\lambda_4<1.                  \tag{88.21}
$$

正式输出的 self-map 与 strict selected contraction 两门都为真。本条只使用已观察到的准确不等式(88.21)，不编造尚未从暂时失联执行器读回的逐行小数或输出文件哈希。

## 7. 联立结论

闭积圆盘 $B=\{(\xi_2,\xi_4):\|\xi_S\|_\infty\le3/4\}$ 完备且凸。式(88.19)与(88.21)说明 $\Psi(B)\subset B$。式(88.20)与(88.21)沿两参数连线积分，给

$$
 \|\Psi(\xi_S)-\Psi(\widetilde\xi_S)\|_\infty
 \le\max(\lambda_2,\lambda_4)
       \|\xi_S-\widetilde\xi_S\|_\infty,
 \qquad\max(\lambda_2,\lambda_4)<1.
$$

Banach 不动点定理给每个固定 $\xi_T$ 的唯一 $\xi_S^\star\in B$。取对应的 R86 唯一外投影解。由(88.18)，其真实 cut canonical 高度恰为
$a_m^*+A_m\xi_m^\star=a_m$。由(88.3)使用同一 $\beta(a)$，selected 斜率同时为该真内头的斜率。外端仍是原固定目标。对实参数，所有映射保持实子空间，唯一不动点亦为实。

唯一性限于所声明的参数盘及 R86 场球内。其它模式仍是给定函数，所以这里只闭合两个真实外投影方程及其切口，不推出完整外 Darboux 解。证毕。

## 8. 实际执行与可重现证据

本次源固定于主线提交 fb75a6c56deec11f5ffd70c5731d326a1a985557。完整参数、输入路径、两个原始 argv、正式退出以及临时运行目录见
[第四次执行器中断与正式成功记录](../notes/2026-11-12-root-fourth-interruption-and-formal-success.json)。

1. 新中心入口 [root_outer_linear_centre_fields_rebuilt_v2.py](../computations/root_outer_linear_centre_fields_rebuilt_v2.py)，SHA256 306b2bc0c49635d731f3bbe91653310f2b2ecba19bcb7437f8ef932f37a5d75b。自有会话19031，工具及 wait4 正式 exit0，33.81947445869446秒、41064KiB；10793原叶/10933子片/18组全部门真。
2. 有序消费者 [closure_outer_linear_centre_ordered_cut_recovered_v1.py](../computations/closure_outer_linear_centre_ordered_cut_recovered_v1.py)，SHA256 5cc4e1d628d4676edb11f704846347cd260e374875315e5c9564c28175c92c38。自有会话20874，工具及 wait4 正式 exit0，15.688485383987427秒、21228KiB；完整共同域、场收缩、两 cut 自映、严格 cut 收缩四个数学门全部为真。它只作标准库 Fraction 运算，不启动新的 Arb、ODE 或积分。
3. 新源保留完整 mean、metric 根和逆余项；消费者保留全部原20模式质量、真实 R74 二十轴和 R78 头值/导数。新物理弱核的完整源身份与原实际背景一致，并明确拒绝 uniform-V0 的失败提案。
4. 执行器在两次正式成功后失联，数值输出本体尚待从原目录取回；不能把未知的文件存在性写成丢失，也没有给它们虚构哈希。若原件确实不可用，按记录的同源码/同输入和 fresh 输出路径重做。源码及参数均已保存；依根 README，仅 GitHub 可用期间不编码搬运数值大文件。

旧 CI 的 compact interval 读取 TypeError 是另一次0组失败。新版只改该表示恢复，成功的19031从头运行全部组；旧失败记录不被改写。本定理没有将该失败或执行器失联当作数学证书。

本条完成后继续其余切口、全频耦合、外0至9及课题 README 的完整闭面、幅度、全时 reach 与同问题加密要求。
