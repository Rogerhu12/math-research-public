# R564：穿过高度耦合零点的真实桥、负交叉回路与七矩联合零

日期：2026-11-26。原式纸证；本稿依赖已登记的 R521、R544、R556、R557、R559 原式及真实入口，不执行数值试验。

**结论。** 在 R559 同一 R521 母库、同一原右锚和一次固定第三规范允许的从起点选择中，可以进一步取同一个中心足够大，然后构造一条完整第四 ruling 为零的有限光滑实际词，使

$$P_0=P_1=P_2=T_1=R_1^y=S_0^y=R_0^y=0.$$

只有 $S_1^y$ 一个第二矩阵槽尚未清零。第三、第四 period，scalar/frame/位置的完整返回，十三规范，以及主课题宏观幅度、reach、有限等距族，均不在本结论内。本稿不涉及数值点 58，也不把七个矩的闭合称为完整闭曲面构造。

新机制是允许原高度加速度的耦合系数 $B$ 改号。$B=0$ 不是原 R521 方程的奇点；真正解加速度的系数始终是 $C_k>0$。R562 的反交叉费用门假定 $\beta=B/(2C_k)>0$，不能用于下面的负 $\beta$ 回路。

## 1. 同一个母库中确有一个可穿越的简单零点

用固定中心 $\Omega=\omega_c$ 和 $y=x+\Omega$，记

$$\eta=\omega-\Omega,\quad d=h\eta-k,\quad e=hy+d,\quad Q=1+e^2.$$

R521／R535 的原积分给

$$
C_k=\frac{|\mathcal G|}{3072h^5}\mathcal I_{h,d}[e]>0,
\qquad
B:=-(C_h+2\eta C_k)
=\frac{|\mathcal G|}{3072h^6}\mathcal I_{h,d}[h^2y^2-1-d^2],
\tag{1}
$$

其中

$$
\mathcal I_{h,d}[v]
=\sum_j w_j\rho_j^4\int v\frac{F_j^4}{Q^2},
\quad
F_j=Q u_j''-2he u_j'+2h^2u_j,
\quad w_j>0.
\tag{2}
$$

**参数顺序。** 先冻结原 R521 的所有 $u_j$、位置、宽度、幅度、正交副本和物理区间 $I$，以及原 $H_+=H>0$、$H_0>\sqrt3H$。这些量不随 $\Omega$ 缩放。随后只在 R550／R552 从起点选大中心的同一个步骤中，把 $\Omega$ 一次取大；此后整条实际词从不换中心或规范。下面仅用局部变量 $h=q/\Omega$ 寻找新增低高度 $H_c,H_-$，**不把原 $H_+$ 改成 $q_+/\Omega$**。

令

$$W=\frac{|\mathcal G|}{3072}\sum_jw_j\rho_j^4\int(u_j'')^4>0.$$

在任意固定 $q$ 正紧区间，把 $h=q/\Omega,d=0$ 代入(1)(2)。由于物理 $x$ 和各 profile 已冻结，逐项除去 $\Omega$ 的幂得到一致 $C^2_q$ 极限

$$
\frac{C_k(q/\Omega,0)}{W\Omega^5}
\longrightarrow\frac{(1+q^2)^2}{q^4},
\qquad
\frac{B(q/\Omega,0)}{W\Omega^6}
\longrightarrow\frac{(q^2-1)(1+q^2)^2}{q^6}.
\tag{3}
$$

具体地，$e=q+O(\Omega^{-1})$、$Q=1+q^2+O(\Omega^{-1})$、$F_j=(1+q^2)u_j''+O(\Omega^{-1})$，且这些误差的前两阶 $q$ 导数一致。有限个真实积分的分母在该紧区间统一正，故可逐项微分积分。这给出(3)，无浮点判号。

右边第二函数为 $1+q^{-2}-q^{-4}-q^{-6}$，在 $q=1$ 有正导数，并在例如 $q\in[0.9,1.1]$ 上严格递增。故取大而有限的同一个 $\Omega$ 后，$B(h,0)$ 在 $h\simeq\Omega^{-1}$ 有一个简单零点 $H_c$，且在其两侧为负／正。选一个固定 $q_-<0.9$，用这个已经固定的 $\Omega$ 定义 $H_-=q_-/\Omega>0$。增大 $\Omega$ 的先验下界后，可保

$$H_-y_{\max}<1,\qquad H_+y_{\min}>1.$$

局部单调区间以上，$hy_{\min}>1$ 使(1)的权重逐点正，一直到原固定 $H_+$；局部区间以下到 $H_-$，$hy_{\max}<1$ 使权重逐点负。因此 $[H_-,H_+]$ 只包含这个简单零点。

这里仍有 $h>0$、$y+\eta>0$、$hy+d>0$ 的共同严格余量，只要 $|d|+|\eta|$ 足够小。低高度没有原 profile 极点，$C_k$ 在整个固定紧域一致正。

R550／R552 所用 $Q_0,Q_2,B_{21},D_*$ 的严格号也是在同一冻结 profiles 上由一次足够大的有限 $\Omega$ 支付；(3)只增加同方向的中心下界要求。没有分别构造两个不相容的母库。

## 2. 完整真实入口与两类不同费用

消费 R556／R559 的共同 core，使用其原参数 $\theta$、原最后 $P_2$ 停止坐标 $v$ 及

$$
R=L_h/\sqrt\lambda,\quad M=(1+\log R)^6,\quad
\delta=\lambda^2\zeta,\quad
a_R=M/R^{3/2},\quad g_R=M/R^2.
\tag{4}
$$

同一规范始终是

$$\nu=\delta^{-2}(-H_0^2\lambda,2c,\lambda),\qquad c=C_k(H_+,0)>0.$$

在真实末高尾之后，R559 已付的有限下降与开放反馈入口满足

$$
\mathsf A=\delta A=O^1(a_R),\qquad
\mathsf Z=\delta^2\widetilde T=O^1(g_R),\qquad
|k|+|\eta|+|d|+|j|=O^1(g_R)+o_\delta(1),
\tag{5}
$$

其中 $j=\eta/h+d/h^2$，上标 $1$ 包括原共同参数盒上的一阶导数。所有历史都是真正从原零起点取得的 incoming。

有效 Gram 仍用 R544 原式，因此

$$\Gamma_1=2c+O^1(g_R),\qquad \Gamma_0,\Gamma_2=O^1(g_R).$$

它的稳定根 $q_\Gamma(h)$ 在整个 $[H_-,H_+]$ 上光滑，且

$$
q_\Gamma,\partial_hq_\Gamma,\partial_h^2q_\Gamma=O^1(g_R),
\qquad \Psi_{\Gamma,d}>c>0.
\tag{6}
$$

须区分两类费用。

- 固定 $R$ 后的慢高度桥和开放准备，其原八矩及一阶参数导数有一个与 $\delta$ 无关的有限界 $C_R$；最后一次小 $\delta$ 可以压低它们的归一费用。
- 新快跨越和长快回路有真实的 $1/\delta$ 费用，不能收入 $C_R$；其 $R$ 次数下文逐项给出，系数对大 $R$ 统一。

## 3. 耦合零点两侧的真实补偿反馈与有限桥

原正频率与高度耦合为

$$
\alpha=\Psi_{\Gamma,d}/(2C_k)>\alpha_0>0,
\qquad \beta=B/(2C_k).
$$

以 $d-q_\Gamma(h)$ 为法向变量，真正加速度耦合为 $\beta+q_{\Gamma,h}$。由(3)(6)，它也有简单零点 $h_0(\Gamma)=H_c+O^1(g_R)$。固定

$$\epsilon_R=R^{-15/8},\qquad L_b=\sqrt R.$$

因为 $g_R/\epsilon_R=M/R^{1/8}\to0$，在离该点至少 $\epsilon_R$ 的两侧，耦合绝对值不小于 $c_0\epsilon_R$。

### 3.1 固定参考函数，反馈仍使用当前真实 Gram

先固定一个充分大的有限 $R$。在本侧慢桥入口记真实有效 Gram 为 $\Gamma_{\rm in}$，并计算 $h_{0,\rm in}=h_0(\Gamma_{\rm in})$。选有限光滑参考高度 $\bar h(s)$，从原 $H_+$ 下降到 $h_{0,\rm in}+\epsilon_R$，两端各有开放恒参考段。负侧则从已过零点的实际入口到固定 $H_-$。参考函数暂冻结；原 governing ODE 内的 $\Gamma$ 从不冻结。

把实际高度误差和当前零点漂移都限制为 $\epsilon_R/10$ 的 bootstrap 盒。盒中参考路径到当前零点的距离至少 $4\epsilon_R/5$。反馈中的 $q,\alpha,\beta,\ell,b$ 全在当前 $\Gamma,j,h$ 上按 R544(31) 计算。简单根及稳定根对 $\Gamma$ 的导数一致有界，故下面真实历史的 $O(C_R\delta)$ 变化会严格改善这个盒。

### 3.2 每侧使用常数 $\kappa$ 和原补偿因子

取与 $R$ 无关的充分大常数 $K$，令

$$\kappa_+=Ka_R/\epsilon_R,\qquad \kappa_-=-Ka_R/\epsilon_R.$$

每侧的 $\kappa_\pm$ 是常数，不是状态函数；因此微分时没有省略 $\kappa$ 的状态导数。由 $|b|+|\ell|\le Ca_R$ 及侧带余量，

$$
d_n=\kappa_\pm(\beta+q_h)-b\ge c_1a_R>0,
\qquad
a_n=\alpha-\kappa_\pm\ell
\ge\alpha_0-Ca_R^2/\epsilon_R\ge\alpha_0/2.
\tag{7}
$$

这里 $a_R^2/\epsilon_R=M^2/R^{9/8}\to0$。阻尼上界可随固定 $R$ 增大；不预设统一的大 $R$ 衰减率。

固定 $\kappa_h>0$，准确使用 R544 的补偿反馈

$$
v_*=\bar h_s-\kappa_h(h-\bar h),\qquad
V=(1-\kappa_\pm\ell/\alpha)v_*,
\qquad
\gamma=h_s=V+\kappa_\pm(d-q_\Gamma(h))/\delta.
\tag{8}
$$

它是原单个高度加速度控制的状态约束，不是新增第二个几何控制。负 $\beta$ 侧仅 $\kappa$ 为负，而(7)仍是正刚度、正阻尼。

### 3.3 真实质量因子、跟踪和全部 incoming

保原缩放历史 $\bar Z=(\mathsf A,\mathsf Z)$ 的准确方程

$$
\bar Z_s=Z^0+\delta^2Z^1a,\qquad
a=h_{ss},\qquad Z^1=(0,2\mathcal A k_s).
$$

微分(8)，质量因子正好是 R544(33)

$$
\mathfrak m
=1-\delta^2V_{\bar Z}Z^1+\kappa_\pm\delta q_{\bar Z}Z^1
=1+O(C_R\delta).
\tag{9}
$$

固定 $R$ 及有限状态盒后，最后小 $\delta$ 使其非零。先求真实 $h_{ss}$，再由原 $C_k>0$ 求 $k_{ss}$，原 $M_0,M_2$ 和第三有序项始终原样演化。

令

$$
r=(d-q_\Gamma(h))/\delta,\quad
w_n=d_s-q_h\gamma,\quad
r_*=\ell v_*/\alpha,\quad E=r-r_*.
$$

准确关系 $(\alpha-\kappa\ell)r_*=\ell V$ 把原法向系统化为

$$
E_\tau=w_n+O(C_R\delta),\qquad
(w_n)_\tau=-a_nE-d_nw_n+O(C_R\delta),
\quad \tau=s/\delta.
\tag{10}
$$

当前 $\Gamma$ 变化、$q_{\bar Z}\bar Z_s$、原速度势和全部第三累计均在余项内。系数的快时间导数为 $O(C_R\delta)$。固定 $R$ 后，按真实 $\inf a_n,\inf d_n>0$ 及其有限上界选择交叉能量常数，得到

$$\mathcal E_\tau\le-c_R\mathcal E+C_R\delta^2,\qquad c_R>0.$$

入口接同一反馈的开放 germ；更换 $\kappa$ 时，先在原强准备盒内用平坦 cutoff 和端控支付其小误差。原耗散估计给 $|E|+|w_n|\le C_R\delta$。由(8)还有准确抵消

$$h_s=v_*+\kappa E,\qquad |h-\bar h|\le C_R\delta.\tag{11}$$

不能省略补偿因子 $1-\kappa\ell/\alpha$。末恒参考段上 $v_*=O(C_R\delta)$，故

$$d-q=O(C_R\delta^2),\qquad h_\tau,k_\tau=O(C_R\delta^2).$$

同一能量和质量方程给固定 $R$ 时的真实速度、加速度及一阶参数变分的有限 $\delta$ 无关界；可能的 $\epsilon_R^{-1}$ 因子明确属于这个固定 $R$ 常数。

### 3.4 历史盒和慢桥费用同时闭合

真实几何、速度和加速度界代入原历史式，在有限参考桥上给

$$
\Delta\mathsf A=O^1(C_R\delta),\qquad
\Delta\mathsf Z=O^1(C_R\delta).
\tag{12}
$$

这里特别保留 $-\delta M_{\rm raw}\circ\mathsf A$ 和全部第三速度／加速度项；$\mathsf A_{\rm in},\mathsf Z_{\rm in}$ 从未置零。最后选 $C_R\delta\ll\min(g_R,\epsilon_R)$，既保持(5)盒，又使零点漂移小于 $\epsilon_R/10$，与(11)一起严格改善第3.1节的侧带盒。正、负侧相同。

**慢桥没有隐藏 $C_R/\delta$ 费用。** $M_0$ 在固定 scalar 紧域有界，$M_2$ 为真实有界速度的二次式，参考桥实际时长固定有限，故全部原八矩及其一阶参数导数积分至多 $C_R$。完整未缩放 $A,T$ 可以很大，但它们已通过真实反馈影响轨道，不能据此再把同一有界速度的八矩积分变成 $1/\delta$。端部快准备中速度仍有界，实际时长为快时长的 $\delta$ 倍，其积分也有 $\delta$ 无关上界。

实际末高度仅与参考相差 $O(C_R\delta)$。若小带快跨越需要准确起点，使用第5节的原四端图，目标取

$$
h=h_0(\Gamma_{\rm out})+\epsilon_R,\quad h_\tau=0,\quad
d=q_{\Gamma_{\rm out}}(h),\quad d_\tau=0.
$$

目标含当前真实末 $\Gamma$，其控制线性项在静态零速度基值为零，故端图逆界仍为 $O(\epsilon_R^{-1})$。入口残差 $O(C_R\delta)$，端控幅至多 $C_R\delta/\epsilon_R$；其物理速度至多 $C_R/\epsilon_R$，快段实际长度 $O(\delta)$，所以八矩费用至多 $C_R'\delta$，而非 $C_R'/\delta$。第三缩放增量也是最后可压的 $O(C_R'\delta)$。

这一步后，把真实 $h_0(\Gamma_{\rm out})$ 作为小带跨越的固定中心。该跨越内 $\Gamma$ 继续变化，其 $O(\epsilon_R^2)$ 变化只使根移动 $O(\epsilon_R^2)\ll\epsilon_R$。

## 4. 不除以 $B$ 的完整快跨越

在上一节真实强准备入口，平滑关掉上一反馈，规定

$$
h(\tau)=h_0+\epsilon_R\chi(\tau/L_b),\qquad 0\le\tau\le L_b,
\tag{13}
$$

其中 $\chi$ 是从 $+1$ 到 $-1$ 的固定平滑函数，端邻域为常值。端部使用原平坦 cutoff；误差先保为 $o_\delta$。$k_{\tau\tau}$ 仍由 R521 完整方程解出，分母是 $C_k$，不是 $B$。

此段 $h-h_0=O(\epsilon_R)$、$h_\tau=O(\epsilon_R/L_b)$、$h_{\tau\tau}=O(\epsilon_R/L_b^2)$，且 $\beta=O(\epsilon_R+g_R)$。以 $e_n=d-q_\Gamma(h)$ 为法向变量，保全部真实累计后，R559 §4 的原式整理给

$$
e_{n,\tau\tau}-b(\tau)e_{n,\tau}+\alpha(\tau)e_n
=F_{\rm slow}+\mathcal K[e_n].
\tag{14}
$$

这里 $\alpha\ge\alpha_0/2$；$\mathcal K$ 是完整第三历史和原 $\mathsf A$ 产生的因果差，不是新自由 forcing。没有步骤除以 $\beta$。

由 R559(22)(23)的完整快历史方程，把原项分别代入规定高度与 $e_n=0$ 的比较路径，可得 $F_{\rm slow},L_bF_{\rm slow}',L_b^2F_{\rm slow}''$ 的共同界

$$
\mu_R=C\left\{
\frac{a_R\epsilon_R}{L_b}
+\frac{\epsilon_R^2}{L_b^2}
+\frac{g_R\epsilon_R}{L_b^2}
\right\}+o_\delta(1).
\tag{15}
$$

三组来源依次是原 $L_{\rm vel}(\mathsf A\Delta)$、$\beta h_{\tau\tau}$ 与全部速度二次项、$q_\Gamma$ 的真实二次导数。原 $-M_2\circ\mathsf A_{\rm in}$、$2\mathcal A h_{\tau\tau}k_\tau$、三次速度、当前有效 Gram 和 $YC$ 均保留，不是只用静态振子。

R559(32a)(32b) 的历史差推导仅用给定高度幅度、导数和原(22)(23)，不使用 $\beta>0$ 或 $\beta\ne0$。这里代入 $\sigma=\epsilon_R,L=L_b$，其因果算子范数由

$$C(a_R\epsilon_R+\epsilon_R/L_b+\epsilon_R^2)$$

控制，乘以 $L_b$ 仍趋零。正频率系数及阻尼的总变差／总量由 $C(\epsilon_R+a_RL_b)+o_\delta$ 控制，且

$$a_RL_b=M/R\to0,\qquad g_RL_b^2=M/R\to0.$$

因此可用 R559 §4.3 的一次缓变修正 $F_{\rm slow}/\alpha$；代回残余为 $O(\mu_R/L_b^2)$，正振子能量积分为 $O(\mu_R/L_b)$，完整因果差在大 $R$ 时吸收入左边。得到

$$
|e_n|\le C\mu_R+o_\delta,\qquad
|e_{n,\tau}|\le C\mu_R/L_b+o_\delta.
\tag{16}
$$

初端强准备误差由最后小 $\delta$ 吸收。相同因果估计适用于原参数的一阶变分。放大盒、先控制历史、再用(16)、最后回到水平式的 bootstrap 给完整区间实际解，不先假定长期存在。

关键比较为

$$
\mu_R=O(MR^{-31/8})+o_\delta,\qquad
\frac{\mu_R}{\epsilon_R^2}
=O(M/R^{1/8})+o_\delta\longrightarrow0.
\tag{17}
$$

因此快跨越到达真实负耦合侧，末法向误差小于下节端控所需的二次尺度。

## 5. 四端图的实际退化次数和开放 germ

在快跨越末端 $h=h_0-\epsilon_R$ 附近，记 $b_*=\beta+q_h\le-c\epsilon_R$。在快时钟中取 $\delta=0$ 的当前静态基值。原历史的线性变分没有新常 forcing：$\mathsf A_\tau=M_2$ 为速度二次，$\mathsf Z_\tau$ 的原速度面积和有序项也至少二次。消去固定端高度后的线性系统准确具有

$$
E''-b_0E'+\alpha_*E=-b_*f''+\ell_0f',
\tag{18}
$$

其中 $|b_0|+|\ell_0|\le Ca_R$，$\alpha_*$ 在固定正紧区间，$b_*$ 是原实际耦合。

选两条固定紧高度测试函数，使其在正频率 $\sqrt{\alpha_*}$ 的正弦／余弦矩构成可逆矩阵。$b_0\to0$，所以当前阻尼频率下仍一致可逆。对(18)作真正分部积分，端点复读出是这些 Fourier 矩乘以

$$-b_*r^2+\ell_0r,$$

其中 $r$ 是 $r^2-b_0r+\alpha_*=0$ 的非实根。因 $b_*,\ell_0$ 实，

$$|-b_*r+\ell_0|\ge |b_*|\,|\operatorname{Im}r|\ge c\epsilon_R.$$

所以消去高度和高度速度后的两个真实法向端点控制逆界为 $O(\epsilon_R^{-1})$。另两条高度控制给高度／高度速度的普通可逆块；完整四端图有相同逆界。这来自原方程导数，并非仅说形式振子可控。

固定快长度内，完整缩放 ODE 在原合法紧域的二阶导数统一有界，目标函数中的 $q_{\Gamma_{\rm out}}$ 及原历史导数均在该 ODE 内。由(17)，残差为 $o(\epsilon_R^2)$，定量 IFT 给修正幅

$$O(\mu_R/\epsilon_R)=O(g_R)=o(\epsilon_R).\tag{19}$$

非线性余项为 $O(g_R^2)=o(\epsilon_Rg_R)$，退化逆界后仍有有效小量。实际 $\delta$、小 incoming 法向误差与一阶参数变分均按同一估计处理。

末端准确付 $h=h_0-\epsilon_R,h_\tau=0,d=q_{\Gamma_{\rm out}}(h),d_\tau=0$。再用固定快长度的平坦 cutoff 接本侧真实反馈。该 cutoff 在 $\delta=0$ 基态上静止；非零扰动为 $O(C_R\delta^2)$，即使反馈系数依赖 $R$，也只是最后可压的 $o_\delta$ 费用。随后恒参考准备得到真实开放 germ，再按第3节下降至固定 $H_-$。

因此支付的是光滑控制切换后的开放反馈 germ，不把四个端值相同直接当作全部 jets 匹配。

## 6. 快跨越和两侧桥的完整账

快跨越上，原八矩的速度二次部分积分连同(19)的端控为

$$O^1(\epsilon_R^2/\delta).\tag{20}$$

这是统一界，涵盖较小的真实 $S_0,R_0$ 项。快段原静态成本为 $O^1(\delta L_b)$；缩放历史增量 $\Delta\mathsf A,\Delta\mathsf Z=O^1(\epsilon_R^2)$，远小于(5)盒，原有序项保留。端控 $g_R^2/\delta$ 因 $g_R/\epsilon_R\to0$ 也被(20)覆盖。

最细的已有矩尺度是 $S_0$ 的 $M/(\delta R^{7/2})$，而

$$
\frac{\delta R^{7/2}}M\frac{\epsilon_R^2}{\delta}
=\frac{R^{-1/4}}M\longrightarrow0.
\tag{21}
$$

对 $R_0$ 的 $\sqrt M/(\delta R^{5/2})$ 及所有较粗尺度同样低阶。这些判断没有使用未知的随 $R$ 常数 $C_R$。

两侧慢桥费用另为 $O^1(C_R)$。固定全部有限 $R$ 和参数紧盒后，从第3节真实能量界取有限 $B_R$，支配所有慢桥八矩、端图一阶导数、cutoff 和准备常数。最后一次选择

$$
0<\delta\le\lambda^2,\qquad
\delta B_R\frac{R^{7/2}}M\le R^{-1},\qquad
\delta B_R\frac{R^{5/2}}{\sqrt M}\le R^{-1},
\tag{22}
$$

并令 $\delta B_R\ll\min(g_R,\epsilon_R^3)$，所有 $o_\delta$ 入口和端控误差小于 $\epsilon_R^4$ 及后文各明确尺度。有限个要求可由一次正 $\delta$ 同时满足。这沿用原先固定 $R$、最后固定 $\delta$ 的参数次序，既不假定 $B_R$ 多项式增长，也不把 $B_R/\delta$ 当可压费用。

原完整 core 因而可以在同一次 $\chi$ 下到达 $H_-$ 的真实强准备入口；所有新增桥在已有六矩端图和下面交叉首项中都是已证明的 $C^1$ 低阶项。

## 7. 负耦合处的长快闭振子和全部交叉费用

在两个固定高度记

$$
c_j=C_k(H_j,0)>0,\quad \omega_j^2=c/c_j>0,\quad
\beta_j=B(H_j,0)/(2c_j),\qquad j\in\{+,-\}.
$$

$\beta_+>0>\beta_-$，但两频率均正。原规范中的 $c=C_k(H_+,0)$ 从未换成 $c_-$。

固定同一个非零 $\psi\in C_c^\infty$，令 $I_m=\int(\psi^{(m)})^2>0$，并置

$$
\varepsilon=R^{-3/4},\quad L=\ell\sqrt R\,M^{-1/4},\quad
\psi_L=\sqrt L\,\psi(\tau/L),\quad D_L=\psi_L'',\quad
f_{j,L}=-(\psi_L''+\omega_j^2\psi_L)/\beta_j.
\tag{23}
$$

于是准确有 $D_L''+\omega_j^2D_L=-\beta_jf_{j,L}''$，全部端 jets 零，且

$$
\begin{aligned}
\int f_{j,L}'{}^2
&=(\omega_j^4I_1-2\omega_j^2I_2/L^2+I_3/L^4)/\beta_j^2,\\
\int D_L'{}^2&=I_3/L^4,\\
\int f_{j,L}'D_L'
&=(\omega_j^2I_2/L^2-I_3/L^4)/\beta_j.
\end{aligned}
\tag{24}
$$

对原唯一高度加速度输入使用领先高度 $H_j+\varepsilon a_jf_{j,L}$。R559 §4 的完整历史、正能量证明只需正频率和固定非零 $\beta_j$，不需 $\beta_j>0$。将单位频率改为固定 $\omega_j^2>0$ 后，原四个小参数、真实因果核和四端控估计原样成立；第3节已给负侧真实准备及末反馈。因此完整实际费用为

$$
\begin{aligned}
\delta\Delta R_1^y&=\varepsilon^2a_j^2C_{1j}(1+o^1(1)),\\
\delta\Delta T_1&=-\varepsilon^2a_j^2H_j^2C_{1j}(1+o^1(1)),\\
\delta\Delta S_0^y&=-\varepsilon^2a_j^2C_{3j}L^{-4}(1+o^1(1)),\\
\delta\Delta R_0^y&=\varepsilon^2a_j^2C_{2j}L^{-2}(1+o^1(1)),\\
\delta\Delta S_1^y&=-2H_j^2\varepsilon^2a_j^2C_{2j}L^{-2}(1+o^1(1)),
\end{aligned}
\tag{25}
$$

其中

$$
C_{1j}=\frac{\omega_j^4I_1}{8H_j^4\beta_j^2}>0,\quad
C_{3j}=\frac{I_3}{4H_j^2}>0,\quad
C_{2j}=\frac{\omega_j^2I_2}{8H_j^4\beta_j}.
\tag{26}
$$

特别 $C_{2-}<0$。负 $R_0$ 的真实费用包括负 $T_1,S_0$ 和正 $S_1$，并非只摘取一个符号。

仅在负侧代替原最后回路，R559 六矩端图的两个正常数 $C_1,C_3$ 改为 $C_{1-},C_{3-}$，分块结构仍可逆。因此存在实际六零族，其完整 $R_0$ 在 $\delta R^{5/2}/\sqrt M$ 归一后趋于严格负数。原 R562 core 正 $R_0$ 为 $O(1/\sqrt M)$，全部桥由(21)(22)核算，所以这确为总 $R_0$ 的负号。

## 8. 一条实际双回路词的七个准确零

用一个共同 core，先在 $H_+$ 做正耦合回路，接第3—6节完整桥，再在 $H_-$ 做负耦合回路。第二回路保第一回路及桥的完整 incoming。第一回路对缩放历史的增量仍在(5)盒内，故(25)的两份 $C^1$ 估计可用于同一实际词，不是两条零历史词输出的形式相加。

取 $X>0,0<s<1$，参数化实际幅度

$$a_+^2=X(1-s)/C_{1+},\qquad a_-^2=Xs/C_{1-},$$

两回路使用同一个长度参数 $\ell$。记

$$r_j=C_{3j}/C_{1j}>0,\qquad q_j=C_{2j}/C_{1j},\qquad q_+>0>q_-.$$

原最后高尾停止坐标 $v$ 仍是真正横截 $P_2$ 坐标。新增路径光滑依赖 $v$，其 $P_2$ 增量仅来自原静态 $p$ 密度；与 R559 §7 相同的实际停止 IFT 先给总 $P_2=0$，保全部后继和停止时间的一阶导数。

在准确清 $P_2$ 的真实族上，取六参数 $(\theta_1,\theta_2,\theta_3,X,s,\ell)$。按原前三个归一坐标，再加 $\delta R^{3/2}R_1$、$\delta R^{5/2}R_0/\sqrt M$、$\delta R^{7/2}S_0/M$，完整端图的共同 $C^1$ 极限是

$$
\left(
F_1^\infty(\theta),F_0^\infty(\theta),F_t^\infty(\theta),
-r(\theta)+X,
\frac{X[(1-s)q_++sq_-]}{\ell^2},
K(\theta)-\frac{X[(1-s)r_++sr_-]}{\ell^4}
\right).
\tag{27}
$$

$r(\theta)=(\ell_1+\ell_2)/(8\xi)>0$，$K(\theta_*)>0$ 是 R559 已含最早负费的完整 core 正 $S_0$ 系数。新增负 $T_1$ 的真实费用在第三归一坐标为 $O(1/M)$；在实际映射中保留，由原三参数准确支付。

令 $\theta_*$ 为原 R556 三参数共同零，取

$$
X_*=r(\theta_*),\qquad
s_*=\frac{q_+}{q_+-q_-}\in(0,1),\qquad
\ell_*^4=\frac{X_*[(1-s_*)r_++s_*r_-]}{K(\theta_*)}>0.
\tag{28}
$$

这是(27)的真正内点共同零。按显示顺序，Jacobian 分块下三角：原三维块可逆；第四行对 $X$ 的导数为1；第五行对 $s$ 的导数为

$$X_*(q_--q_+)/\ell_*^2\ne0;$$

第六行对 $\ell$ 的导数为

$$4X_*[(1-s_*)r_++s_*r_-]/\ell_*^5>0.$$

在围绕(28)的固定正参数盒上，先取大而有限的 $R$，再按(22)及全部原门一次取小正 $\delta$，有限维 IFT 给六个准确端点零。与真实停止的 $P_2=0$ 合并，得到本稿七矩结论。

原 R562 正 core $R_0$，两回路负 $T_1$ 费用，两侧桥、四端控、全部有序第三和原 $\delta$ 项，都属于(27)已控制的 $C^1$ 余项，实际 IFT 同时支付它们；没有分别在不同冻结末历史上使用根。

## 9. 尚余一个第二矩阵槽，主课题仍未完成

七零实际词的中心第二矩阵为

$$
\begin{pmatrix}
0&0&0\\0&2S_1^y&0\\0&0&-2S_1^y
\end{pmatrix}.
$$

不能写成 $M=0$。两回路给 $S_1$ 的领先贡献，在交叉 $R_0$ 配平后是

$$-\frac{2X_*(1-s_*)q_+(H_+^2-H_-^2)}{\ell_*^2}$$

乘以 $\sqrt M/(\delta R^{5/2})$，严格为负。本稿没有把原 core 在联合参数位移后的 $S_1$ 次阶账设为零，也不据回路项单独断完整 $S_1$ 的符号。下一实际任务是保七个已清目标的同词端图，处理该槽和原未清 periods。

低高度桥解决 O4 的真实可达性问题，没有保证最终几何 reach。$H_->0$ 是从起点固定的有限常数，本稿不把它随加密送到0。真正完整闭面及其主曲率、非局部距离、握持区、宏观幅度仍须随后实现。

## 来源和新增范围

- R521：同一有限正交母、完整 $C_k>0$ 积分和有限维实际 ODE。
- R535：完整 $C_h+2\eta C_k=-B$ 与原积分权重。
- R544：同一个 $\chi$、完整有效 Gram、准确补偿阻尼反馈、无 $k_{ss}$ 的第三变量。
- R550／R552：同一冻结 profiles 上一次选大中心的共同严格号、真实 $P_2$ 停止。
- R556：完整共同 core 和三个真实端参数。
- R557／R559：四端控、开放反馈 germ、长快区间正能量、完整历史因果核、六矩端图。
- R562：完整正 core $R_0$ 尺度、五个速度费用和 $\beta>0$ 障碍的适用边界。

新增步骤是(3)的简单零、(7)—(22)保完整历史的两侧补偿桥及跨越、负耦合真实回路，以及(27)(28)的七矩共同根。不以这些结果替代课题 README 完成标准。

