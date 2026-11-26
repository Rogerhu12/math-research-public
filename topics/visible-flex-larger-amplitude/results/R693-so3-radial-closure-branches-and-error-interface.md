# R693. SO3 闭合 lift 的精确径向分支和连续积分误差接口

日期：2026-11-26。本文给出新 SO3 表示中可直接使用的完整解析恒等式与误差传播界；不修改已经锁定的有限求解器，不增加首跑前置测试，不宣称有实际 SO3 数值或连续证书返回。其用途是指导真实新场返回后的下一条输入/求解方向，并把后继连续验证所欠的误差写清楚。

这里的数学 S、径向节点和 h(s/S) 继承真实冻结父 canonical 的准确符号域，浮点 mesh/S 只是该域的数值载体。当前材料图固定为 theta0=Theta_parent(phi0)，当前 core 仍由 Theta_c(phi_c)=theta0 反解。所有式子均对一个固定 phi0 使用；角导数均对新 phi0 图求导。

## 1. 一个精确的径向恒等式

考虑当前新表示

$$
T(s,\phi_0)=\exp(\omega(s,\phi_0)\times)T_0(s,\phi_0),\qquad |T|=1,
$$

$$
P=R e_r(\theta_0)+H e_z,\quad
I(s)=\int_0^sT(v)\,dv,\quad
\Delta=\Gamma_c-P+I(S),
$$

$$
h(s)=1-10(s/S)^3+15(s/S)^4-6(s/S)^5,\qquad
F=(1-h)P+h\Gamma_c+I(s)-(1-h)I(S).
$$

所以

$$
F_s=T+h'\Delta,\qquad
e:=|F_s|^2-1=2h'T\cdot\Delta+(h')^2|\Delta|^2. \tag{1}
$$

Delta 对 s 是常向量；它对 phi0 和当前全部自由变量都有完整变化。不能因为 T 单位长度就删除 (1) 右端。

以下精确结论假定新表示的结构端值成立：

$$
T(0)=e_z,\qquad T(S)=-e_r(\theta_0).
$$

这来自同一个真实父的精确端 jet、omega 在 core 的 value=0、在 cap 的 value/slope=0。浮点载体是否足够精确仍是后继实际误差责任。

## 2. 精确 E=1 对闭合缺口给出的两条分支

对 $0<s<S$，$h'(s)=-30(s/S)^2(1-s/S)^2/S<0$。因此若完整连续径向误差 e 恒为零，则

$$
T(s)\cdot\Delta=-\frac{h'(s)}2|\Delta|^2. \tag{2}
$$

在两个端点取极限，因 h' 趋于零，

$$
\Delta\cdot e_z=0,\qquad \Delta\cdot e_r(\theta_0)=0.
$$

故可写 $\Delta=d\,e_\theta(\theta_0)$。积分 (2)，利用 h(S)−h(0)=−1 及 $I(S)=\Delta-\Gamma_c+P$，得

$$
I(S)\cdot\Delta=\frac12|\Delta|^2,\qquad
\Gamma_c\cdot\Delta=\frac12|\Delta|^2.
$$

这里 P 与 Delta 正交。令 $\gamma_t=\Gamma_c\cdot e_\theta(\theta_0)$，则

$$
d(d-2\gamma_t)=0. \tag{3}
$$

也就是说，每个固定材料角的精确径向解只能落在

$$
\boxed{\Delta=0\quad\text{或}\quad
 \Delta=2(\Gamma_c\cdot e_\theta(\theta_0))e_\theta(\theta_0).} \tag{4}
$$

这是一个必要结论，证明只用 (1)、端值和准确积分，没有有限截断或经验判断。它没有证明完整 isometry 存在，更没有证明不存在。它也没有说第二支总可平滑地在不同角处任选；连续性和其余 Gram 方程仍要同场解决。

第一支给出明确的后继求解条件：推动完整 closure integral $I(S)=P-\Gamma_c$，使 hDelta 精确消失。在该子分支里径向长度由 T 单位结构严格成立，剩余角向/交叉 Gram 仍全部保留。若用它作为求解辅助，必须保所有原变量和完整最终残差，不能把它当作自动成立的条件或删掉原检查。第二支同样是真实公式允许的径向分支，应依据实际 closure_delta 和当前 core 读数选择，而不是先宣告只存在第一支。

对方向 d，完整闭合差的微分为

$$
d\Delta=d\Gamma_c-dP+\int_0^S dT\,ds.
$$

全部 free core 的隐式角导数、全部 omega 的 Rodrigues 导数和最后 H 的 $dP=dH\,e_z$ 都必须在这里。当前实际 driver 的完整 J/J* 和 world point VJP 已保这些变量；本文没有偷偷换成几个模或几个 closure 参数。

### 非零分支的完整反射推论

在固定 phi0 上若 Delta 非零，令 $k=\Delta/|\Delta|$，
$Q_k=I-2kk^T$。由 (2)，

$$
Q_kT=T-2k(k\cdot T)=T+h'\Delta=F_s.
$$

Q_k 只依 phi0，不依 s，且 $G_s=T,\ F(S)=G(S)=P$。准确积分得到

$$
\boxed{F(s)=P+Q_k(G(s)-P).} \tag{4a}
$$

所以在该固定材料角上，新 F 是单位 meridian G 关于过 P、法向 k 的平面的反射。这是整个径向曲线的恒等式，不只是一阶长度相同；它没有把依角变化的 Q_k 当成保持整个二维 Gram 的固定刚体运动。

又由 (4)，非零时 $\Delta=2\gamma_t e_\theta(\theta_0)$，必有 gamma_t 非零。把 (2) 沿 e_theta 展开可得

$$
T\cdot e_\theta(\theta_0)=-h'\gamma_t.
$$

因 $P\cdot e_\theta(\theta_0)=0$、h(S)=0，积分即

$$
G(s)\cdot e_\theta(\theta_0)=-h(s)\gamma_t,\qquad
\boxed{F(s)\cdot e_\theta(\theta_0)=h(s)\gamma_t.} \tag{4b}
$$

因此第二支具有准确的径向分离切向分量。零 Delta 支不受 (4b) 的分离限制。分支相交或 Gamma_t 为零的位置仍须按完整光滑二维场处理，不能逐角任意选反射而跳过正则性与其余 Gram 行。这个推论只是说明非零支的明确结构，没有重证 R669 的既有有限表示边界，也没有把它当成新的求解准入门。

## 3. 一个可用于真实候选的近似分支界

单知道有限采样上的小 e 不能推出 (4) 的近似形式。以下给出在**完整连续** $|e|\le\varepsilon$ 及相应导数/积分界已经付款时可用的定量版本。

固定 $0<\delta<S/2$，记 $D_\Delta=|\Delta|$，
$q_\delta=|h'(\delta)|=|h'(S-\delta)|>0$。
若

$$
|T_s|\le M_0\quad\text{于 }[0,\delta],\qquad
|T_s|\le M_1\quad\text{于 }[S-\delta,S],
$$

则把 (1) 在 delta 和 S−delta 处除以非零 h'，再与端值比较，可得

$$
|\Delta_z|
\le D_\Delta M_0\delta+
 \frac{\varepsilon/q_\delta+q_\delta D_\Delta^2}{2}, \tag{5}
$$

$$
|\Delta_r|
\le D_\Delta M_1\delta+
 \frac{\varepsilon/q_\delta+q_\delta D_\Delta^2}{2}. \tag{6}
$$

这里 $\Delta_r=\Delta\cdot e_r(\theta_0)$。例如 (5) 来自
$|\Delta\cdot(T(\delta)-T(0))|\le D_\Delta M_0\delta$
以及
$|2T(\delta)\cdot\Delta+h'(\delta)D_\Delta^2|\le\varepsilon/q_\delta$；
(6) 同理，端点的负号不影响绝对值。

在开区间上 $e/h'=2T\cdot\Delta+h'D_\Delta^2$，右端向两端连续延伸。准确积分给恒等式

$$
D_\Delta^2-2\Gamma_c\cdot\Delta+2P\cdot\Delta
=\int_0^S\frac{e(s)}{h'(s)}\,ds. \tag{7}
$$

不能直接用 $\varepsilon\int_0^S|h'|^{-1}$，因为该积分发散。对中段使用 epsilon，对两个端段使用
$|2T\cdot\Delta+h'D_\Delta^2|\le2D_\Delta+|h'|D_\Delta^2$，得到

$$
\left|D_\Delta^2-2\Gamma_c\cdot\Delta+2P\cdot\Delta\right|
\le \varepsilon J_\delta+4D_\Delta\delta
       +2D_\Delta^2(1-h(\delta)), \tag{8}
$$

其中令 $a=\delta/S$，

$$
J_\delta=\frac{S^2}{30}
 \left\{2\left(\frac1a-\frac1{1-a}\right)
      +4\log\frac{1-a}{a}\right\}. \tag{9}
$$

(9) 是
$S^2/30\int_a^{1-a}dt/[t^2(1-t)^2]$
的准确原函数计算；本文没有代入任何实际候选进行本地运算。

记 d=Delta_t、gamma_r=Gamma_c·er、gamma_t=Gamma_c·et。因为 core 位于 z=0，把 (7) 的左端展开，有

$$
d(d-2\gamma_t)
=A-\Delta_r^2-\Delta_z^2
  -2(R-\gamma_r)\Delta_r-2H\Delta_z,
$$

其中 A 是 (7) 左端。所以用 (5)、(6)、(8) 的合法上界 E_r、E_z、E_A，

$$
|d(d-2\gamma_t)|
\le E_A+E_r^2+E_z^2+
      2|R-\gamma_r|E_r+2|H|E_z=:B. \tag{10}
$$

于是至少有

$$
\min\{|d|,\ |d-2\gamma_t|\}\le\sqrt B.
$$

这给出真实新场应靠近哪条径向分支的诊断。epsilon、M0/M1、Delta、Gamma、H、R 的区间身份都必须同场；有限 scalar readout 不能冒这条连续结论。

## 4. 准确积分怎样进入完整六 jet

当前数值 operator 用 Gauss 节点和分段插值积分计算 I；Fs 等项则用精确公式中的 T 的数值求值。它们是准确积分定义的近似。不能把一份数值 I 的导数恰巧等于某个插值多项式的导数，再把它当作真实 T 的全部误差已经为零。

对角阶 j=0,1,2，写 $I_j(s)=\int_0^s\partial_{\phi_0}^jT(v)\,dv$。假定已经有同一角弧上的向外误差上界

$$
|\widetilde I_j(s)-I_j(s)|\le e_{I_j(s)},\quad
|\widetilde I_j(S)-I_j(S)|\le e_{I_j(S)},
$$

$$
|\widetilde P_j-P_j|\le e_{P_j},\qquad
|\widetilde\Gamma_j-\Gamma_j|\le e_{\Gamma_j}.
$$

所有 h、h'、h'' 也用同一准确 symbolic S 包围；以下公式先写准确 scalar h，实际执行再支付其浮点载体误差。因为 0≤h≤1，

$$
e_{F_j}
\le(1-h)e_{P_j}+h e_{\Gamma_j}
   +e_{I_j(s)}+(1-h)e_{I_j(S)},\quad j=0,1,2. \tag{11}
$$

另外

$$
e_{\Delta_j}\le e_{\Gamma_j}+e_{P_j}+e_{I_j(S)}. \tag{12}
$$

完整其余三种 jet 的误差是

$$
e_{F_s}\le e_T+|h'|e_{\Delta_0},
$$

$$
e_{F_{ss}}\le e_{T_s}+|h''|e_{\Delta_0},
\qquad
e_{F_{s\phi_0}}\le e_{T_{\phi_0}}+|h'|e_{\Delta_1}. \tag{13}
$$

(11)–(13) 由当前新 F 的同一公式逐项相减并用三角不等式得到。它们同时覆盖位置、两个一阶和三个二阶 jet，不遗漏全局积分 I(S) 对每个位置和曲率的影响。

如果使用区间 hull 直接包围这些向量，也可以不拆标量 fee；但不能只把真实 T 的点误差付给 Fs，而遗漏 |h'|e_Delta。所有 scalar/mesh carrier、theta0、rho0、隐式 core root 和父归一化误差都要进入相应输入盒。

## 5. 一个不需要高阶 Gauss 导数的完整积分兜底

在已经按所有 q/omega 节点、eta、FullHold 和 deep cutoff 真实接点分割的闭段 [a,b] 上，设 W 是 T、T_phi0 或 T_phi0phi0 中任一个，逐分量或欧氏范数有完整 $|W_{ss}|\le M_2$。令 m=(a+b)/2、ell=b−a。Taylor 积分余项直接给

$$
\left|\int_a^b W(s)\,ds-\ell W(m)\right|
\le \frac{\ell^3 M_2}{24}. \tag{14}
$$

证明：$W(s)=W(m)+(s-m)W_s(m)+R(s)$，
$|R(s)|\le M_2(s-m)^2/2$；一次项在对称区间积分为零，
$\int_a^b(s-m)^2/2\,ds=\ell^3/24$。

中点值必须有准确区间；其误差乘 ell 一同支付。累加完整子段的盒即可得到 I_j(s)、I_j(S) 的合法盒，未细化的区段也必须保留原有效盒。它们可以和现有 Gauss 近似比较来给 (11)–(13) 的实际误差，而不需要把旧数值 Gauss 当作严格积分。这是一个始终有意义的兜底；有更高效的真实高阶界时可以取交集。

这里所需径向二阶 $T_{ss}$、$T_{\phi_0,ss}$、$T_{\phi_0\phi_0,ss}$ 在节点间只涉及 omega 的二阶径向导数、父 F 的三阶径向导数（即 Fs 的二阶径向导数）和至多二阶角导数。原 q 是分段 quintic，故必须在它的真实节点处分割，不能跨三阶跳跃取一个未证明的光滑高阶 Gauss remainder。新 deep cutoff 为 C² beta，参考 a/I 的所需三阶由完整 beta、beta'、beta'' 给出；准确帽端无限振荡仍须使用 R690 的完整 flat-tail 包围，不能剪掉。

(14) 是完整条件界，尚不是已经实现并运行的 SO3 连续消费者；它为该后继指出了准确输入和可返回的最小单元。实际代码若只给出六 jet 而未给所需 W_ss 的合法盒，就不能宣称这一余项已经付款。

## 6. 父归一化和当前隐式 core 的来源

固定父
$T_0=V_0/|V_0|$、$V_0=F_{0,s}$。
它的值和混合 jet 必须使用同一个真实 frozen parent bundle/model。若已登记的同父完整 first 返回确实含全域 $E_0=|V_0|^2\ge c>0$，可以把这条**固定输入自身**的正性用于除法。那不是把旧父 embedding/K/reach 移植给新的 SO3 F。若选择另一个 frozen parent，必须核它自己的实际 source 和完整 E 下界。

所有归一化 jet 都可由 $n^2=V_0\cdot V_0,\ n>0$ 和 $T_0=V_0/n$ 的有限 Taylor/interval 微分递推得到，完整分母下界不能省略。Rodrigues 中以下记 V=T0，

$$
T=V+A(z)(\omega\times V)+B(z)(\omega\times(\omega\times V)),
\quad z=|\omega|^2,
$$

$$
A(z)=\sum_{k\ge0}\frac{(-1)^kz^k}{(2k+1)!},\qquad
B(z)=\sum_{k\ge0}\frac{(-1)^kz^k}{(2k+2)!}
$$

给零附近无除零的准确整函数表达；任何截断都要为实际 omega 盒及所需 jet 给完整余项。当前数值 small-z 近似只是一份数值实现，不是外包证明。

当前 core root 同样不能只报告 Newton 迭代次数。若完整当前 rho_c≥r>0，且对同一个材料角得到准确残差界
$|\Theta_c(\widehat\phi_c)-\theta_0|\le e_\Theta$，
则均值定理立即给
$|\widehat\phi_c-\phi_c|\le e_\Theta/r$。
选定一致的 unwrapped 分支后，theta_c 为严格单调，根唯一。用这个实际 root 区间读完整 Fourier core，并使用

$$
\Gamma_{\phi_0}=\rho_0 e_\theta(\phi_c),
\quad
\Gamma_{\phi_0\phi_0}
=\rho_0' e_\theta(\phi_c)-\frac{\rho_0^2}{\rho_c(\phi_c)}e_r(\phi_c)
$$

即可给 (11) 的完整 core jet 盒。rho0 是固定父材料图密度；rho_c 是当前 core 密度，二者绝不混同。有限 sample rho>0 或一次 root residual 小都不能代替上述全角分母界。

## 7. 对实际后续工作的含义

首个完整 SO3 求解仍按已经锁定的全变量、全部 Gram 行、原 192 行和同场幅度/Phase I 真筛执行；本文不改其预算或接受条件。首版 fields_torch 返回 closure_delta，但实际 report 尚未保存这项汇总；需要诊断时须在公开Actions对同场作真实读取，不能从已有report捏造缺失值。读到实际值后可判断零闭合分支或另一条径向分支是否值得继续；有限诊断不提前宣称 (4) 的连续结论。

真正的连续消费者必须绑定完整新 SO3 model、omega/core/H、准确 frozen parent、同一个 fixed deep scalar、同一 exact mesh/eta/domain 和其 root/integration 配置来源，再按 (11)–(14) 或更强的有效同场界支付每一条六 jet 误差。达到 metric 1e−6 后仍要做自己的 D/L、embedding、K、reach、所有 t 和同固定问题精化；任何已有父的几何结论只可作为注明的固定输入事实，不作新 F 的证书。

本文没有进行本地科学数值计算，没有提出新的必过 fixture，也没有把条件误差界或一个完整解析子问题当作本课题完成。

完整已刊数值表示、全部源与初始预算见[SO3完整入口](../notes/2026-11-26-complete-closed-SO3-meridian-solver.md)，首次刊载提交 `01b98351b40385675c5cf85bdd4ea28637055a24`。本文分析其准确积分定义，不把 operator 的普通数值积分或有限Taylor近似当作准确值。
