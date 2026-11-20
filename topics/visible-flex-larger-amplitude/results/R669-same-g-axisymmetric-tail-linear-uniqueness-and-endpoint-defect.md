# R669. 同 g 旋转参考尾、固定帽的无穷小唯一性与末胞高度判据

日期：2026-11-20。会话：Astra-resume-public-20261120 / recover_evidence。尾端无穷小唯一性的积分估计由 root 提出，以下逐式证明。

**状态：已证明的解析结构和表示判据；新 Actions 数值诊断尚未执行。** 这里不证明有限非线性闭嵌入不存在，也不排除课题所要求的同一 $g$ 网格精化及 $10^{-6}$ 数值收敛。第6节的无精确根只针对当前每层末胞高度严格为五次多项式的表示。

## 1. 先区分 scalar 末端与 lift 宽度

记 $T$ 为 FullHold 的 $\cos\alpha$ 首次归零端点。当前准确源 [FullHold](../notes/2026-11-17-parallel-model-full-hold-oracle.py) 定义

$$
T=\mathrm{time}[-1],\qquad \alpha(T)=-\pi/2,
$$

闭场生成器把这个同一 $T$ 作为原 symbolic mesh 的末端 $S$。因此**本次模型中 $T=S$**。这个等式来自生成定义，不能在别的模型中仅凭字母相同而假定。

binary width=$.05$ 是解析 lift 的 $\chi$ 过渡宽度：$\chi$ 在 $[S-\mathrm{width},S]$ 从0变为1。它不是一个提前开始的平度量 collar。曲率 out ramp 的长度是另一准确 binary 数 $h_o=.02$，区间为 $[T-h_o,T]$。原 HoldProfile 仅在 $s>T$ 后才使用

$$
a=R-(s-T),\quad a'=-1,\quad a''=0
$$

并改用 Cartesian 圆盘图。下文的尾变量 $t=T-s$ 不把 lift 起点误当成 scalar 平盘接点。

此区别可直接从原 [HoldProfile](../scripts/parallel_20261117_negative_hold_profile_ivp.py) 的 meridian 与调用接口，以及 [闭端口定义](../notes/2026-11-17-parallel-model-fullclosed-hold-warm-and-oracle.md) 读取。没有重新运行旧积分或旧 IVP。

## 2. 准确轴对称参考及其真实曲率

同一材料度量为

$$
g=ds^2+a(s)^2d\theta^2,\qquad \theta=\Theta(\phi),\quad\Theta'=\rho>0.
$$

原 scalar 的符号约定是

$$
a'=\sin\alpha=:b,\qquad \alpha'=-\kappa,\qquad
c:=\cos\alpha,\qquad a''=-\kappa c,\qquad c'=\kappa b.
$$

不能把这里的 sine、cosine 交换。对 $c\ge0$ 的扩段，任取固定帽高度 $H$，定义

$$
z_*(s)=H-\int_s^T c(u)\,du,\qquad
F_*(s,\theta)=a(s)e_r(\theta)+z_*(s)e_z.
$$

于是

$$
(F_*)_s=b e_r+c e_z,\qquad (F_*)_\theta=a e_\theta,
$$

直接得到 $|F_s|^2=1,F_s\cdot F_\theta=0,|F_\theta|^2=a^2$。在原 $\phi$ 角中就是 $|F_\phi|^2=a^2\rho^2$，所以没有把 $a$ 或 $g$ 另作复合、缩放或拟合。

同一 FullHold 原报告及源中的准确盒给出 $K<2.153$、$.35<\alpha_{\rm cut}<.36$、$a_{\rm cut}>1$、$1/2<R<3/5$。三个先行小段的总长小于 $.043$，且 $|\kappa|\le5/2$。故此前 $\alpha<.36+(5/2)(.043)<1/2<\pi/2$。它们可能使角先减后增，但总正曲率积分不超过 $K h_f+(3/2)h_r<.036$，所以角始终正。正曲率平台随后严格降角，恰有一个 $\alpha=0$ 圈；平台末角为 $-\pi/2+(3/2)h_o/2<0$；out ramp 继续单调降至 $-\pi/2$。因此

$$
c>0\quad(s<T),\qquad a\ge R>1/2
$$

于整个 Hold 扩段：半径在唯一 $\alpha=0$ 圈前增加、之后减少，两个端半径中较小的是 $R$。

取 outward 法向 $n=c e_r-b e_z$。有

$$
(F_*)_{ss}=-\kappa n,\qquad (F_*)_{\theta\theta}=-a e_r,
$$

故两个主曲率为

$$
k_s=-\kappa,\qquad k_\theta=-\frac c a.
$$

于是整个 Hold 扩段的参考曲率满足

$$
\max(|k_s|,|k_\theta|)\le\frac52.
$$

这是参考面的界，**不是原非轴对称候选的曲率界**。在 $T$ 有 $b=-1,c=\kappa=0$，于是准确匹配平帽的零二阶法向 jet。

旧 scalar 段由准确 quintic 构成，其已刊 FullHold 构造逐胞以 Bernstein 控制点验证 $|a'|<1$。所以也可在旧段取 $z_*'=\sqrt{1-a'^2}$，并与扩段正 cosine 分支作 $C^2$ 接合。这个全参考把 core 改成了圆，不能代替题设非圆 core；其活动旋转也不给要求的可见幅度。本条只把它作为同 $g$ 的准确尾部目标和局部线性参考。

## 3. 内部完整纬圈固定时的无穷小唯一性

先在任意紧区间 $I$ 上假定 $a>0,c>0$。取一个 $C^1$ 径向、角向足够可微的无穷小场

$$
Y=u(s,\theta)e_r+v(s,\theta)e_\theta+w(s,\theta)e_z.
$$

令其线性化相对 Gram 分量为

$$
e=2(bu_s+cw_s),
$$

$$
f=\frac{b(u_\theta-v)+cw_\theta+av_s}{a},
\qquad
g=\frac{2(u+v_\theta)}{a}.
$$

这些式子来自直接微分欧氏内积，包含旋转角架的 $-v$ 和 $+u$ 项。无穷小等距时 $e=f=g=0$。

对任意整数材料频率 $m$ 取复 Fourier 系数。由 $g_m=0$ 得

$$
u_m=-imv_m.
$$

另两式化为

$$
v_m'=-\frac{(m^2-1)b}{a}v_m-\frac{imc}{a}w_m,
\qquad
w_m'=\frac{imb}{c}v_m'.
\tag{1}
$$

这是 $(v_m,w_m)$ 的连续系数 $2\times2$ 线性 ODE。它在 $a'=b=0$ 圈仍完全正常；只有 $a=0$ 或 $c=0$ 才使当前表示退化。

若在任意内部圈 $s_*$，完整欧氏场 $Y(s_*,\theta)=0$，则每个模式的两个初值为0。线性 ODE 唯一性给 $v_m=w_m=u_m=0$ 于 $I$。对所有 $m$ 分别成立，再由连续周期函数的 Fourier 唯一性得 $Y=0$。这个证明不要求材料 Fourier 带宽有限；也不把物理 $\phi$ 模误称成材料 $\theta$ 模。

对 $m=0$，上述式子即 $u_0=0,v_0'=(b/a)v_0,w_0'=0$，同样成立。对正负 $m$ 或两种实 parity 亦都成立。

## 4. $\cos\alpha(T)=0$ 仍不能从固定平帽启动非零线性尾

现在取最后的凸 inward 尾 $[s_0,T]$，其中

$$
a\ge R>0,\quad -1\le b=a'\le0,\quad
c>0\text{ 于 }[s_0,T),\quad c(T)=0,
$$

且 $a,c$ 都不增。这正是本 scalar 唯一 $\alpha=0$ 圈至平帽端的区间。设 $Y$ 连续至 $T$、在开尾满足线性等距方程，并在平帽端完整固定：

$$
Y(T,\theta)=0.
$$

$C^1$ 场当然满足后续积分所需正则性。对 $m\ne0$，(1) 的第一式用积分因子 $a^{m^2-1}$ 从 $s$ 积至 $T$，得

$$
v_m(s)
=im\,a(s)^{1-m^2}\int_s^T a(t)^{m^2-2}c(t)w_m(t)\,dt.
\tag{2}
$$

设 $M(s)=\sup_{t\in[s,T]}|w_m(t)|$。若 $|m|\ge2$，$a(t)\le a(s)$ 给

$$
a(s)^{1-m^2}a(t)^{m^2-2}\le1/a(s)\le1/R.
$$

若 $|m|=1$，同一左端为 $1/a(t)\le1/R$，须单独核对这个负指数情形。又有 $c(t)\le c(s)$。由 (2) 得

$$
\frac{|v_m(s)|}{c(s)}
\le \frac{|m|}{R}(T-s)M(s).
\tag{3}
$$

把 (1) 第一式代回第二式，并用 $|b|\le1$、$a\ge R$，得到

$$
|w_m'(s)|
\le m^2\left(\frac1R+
\frac{(m^2-1)(T-s)}{R^2}\right)M(s)
\le C_mM(s),
$$

其中 $C_m$ 在整个紧尾有限。由 $w_m(T)=0$，

$$
M(s)\le C_m\int_s^T M(u)\,du.
$$

反向 Grönwall 给 $M=0$，继而 (2) 给 $v_m=0$，$u_m=0$。$m=0$ 由 $v_0/a$ 与 $w_0$ 为常数直接得零。所有模式消失，故 $Y=0$ 于最后凸尾。

再应用第3节的正规 ODE，可向内延拓零解穿过所有 $c>0,a>0$ 区间，包括 $b=0$ 圈和负 Gaussian 曲率的 Hold 小段。这个论证没有把 $c(T)=0$ 处除法当作合法初值计算，而是先用 (2)–(3) 支付了奇异端点。

**结论边界。** 已证明的是准确旋转参考处、固定平帽的无穷小等距场为零。尚未证明任意有限非轴对称等距场的非线性 Cauchy 唯一性，也未给一个在目标空间可逆的非线性算子。不能据此声称本课题的有限闭面不存在。

## 5. 一个不需要 metric 导数的受迫模式判据

只分析残差而不假定 $e=f=g=0$。从 $g_m$ 得

$$
u_m=\frac a2 g_m-imv_m.
$$

令

$$
W_m=w_m+\frac{ab}{2c}g_m.
$$

准确代入第3节三式，$g_m'$ 项相消，得到

$$
\frac d{ds}
\begin{pmatrix}v_m\\W_m\end{pmatrix}
=
\begin{pmatrix}
-(m^2-1)b/a&-imc/a\\
-im(m^2-1)b^2/(ac)&m^2b/a
\end{pmatrix}
\begin{pmatrix}v_m\\W_m\end{pmatrix}
+
\begin{pmatrix}
f_m\\
im(b/c)f_m+e_m/(2c)-a\kappa g_m/(2c^2)
\end{pmatrix}.
\tag{4}
$$

相消中的唯一导数恒等式是

$$
\left(\frac{ab}{2c}\right)'-\frac{b^2}{2c}
=-\frac{a\kappa}{2c^2},
$$

它由 $a'=b,b'=-\kappa c,c'=\kappa b$ 直接推出。因而 (4) 的右端只需要相对 Gram 的线性化值，不需要它的径向导数。

在 $c\ge c_*>0$ 的紧区间上，记该矩阵的基本解为 $\Psi_m(s,t)$。变常数公式给出

$$
Z_m(s)-\Psi_m(s,s_*)Z_m(s_*)
=\int_{s_*}^s\Psi_m(s,t)B_m(t)r_m(t)\,dt.
$$

若线性化相对 Gram 的全域算子范数不超过 $\varepsilon$，则各个 Fourier 分量的 $|e_m|,|f_m|,|g_m|\le\varepsilon$。因此

$$
\|Z_m(s)-\Psi_m(s,s_*)Z_m(s_*)\|
\le\varepsilon\int_{s_*}^s
\|\Psi_m(s,t)\|
\sqrt{1+\left(\frac{|m||b|}{c}+\frac1{2c}+
\frac{a|\kappa|}{2c^2}\right)^2}\,dt
\tag{5}
$$

（逆向区间取相应绝对积分）。这给低材料模一个可实际计算的“接口差需要多少线性 Gram 缺陷”判据。高模常数可能很差，不能由此宣称统一误差地板。

对于实 parity $v=B\sin(m\theta),w=C\cos(m\theta)$，源码提供同一个实 $2\times2$ 矩阵和对 $(e_m,f_m,g_m)$ 的 forcing 矩阵 helper。它明示输入是材料角模；未对实际场执行该辅助 ODE 的新计算。原有限残差包含二次场增量项，不能把 (5) 的线性 $\varepsilon$ 直接替换成一个有限差场的非线性 Gram 值。

## 6. 当前五次高度末胞没有字面准确等距根

这条结论针对原有限表示，比第3–4节的线性结论是另一种不同的限制。仍令 $t=T-s$。在 out ramp 中，$\kappa_p=3/2$、$h_o>0$，准确有

$$
\kappa(T-t)=\kappa_p\left(
10\frac{t^3}{h_o^3}-15\frac{t^4}{h_o^4}
+6\frac{t^5}{h_o^5}\right).
$$

置 $\beta(t)=\alpha(T-t)+\pi/2$，则

$$
\beta(t)=A t^4+B t^5+C t^6,\quad
A=\frac{5\kappa_p}{2h_o^3},\
B=-\frac{3\kappa_p}{h_o^4},\
C=\frac{\kappa_p}{h_o^5}.
$$

所以

$$
c=\sin\beta=A t^4+B t^5+C t^6+O(t^{12}),
$$

$$
a(T-t)=R+t+O(t^9),\qquad
\kappa c=4A^2t^7+9ABt^8+O(t^9).
\tag{6}
$$

当前模型在 $T$ 左侧的最后一个径向 polynomial piece 中，$q_Z$ 为五次，$\chi H$ 也是五次；完整水平解析 lift 没有高度分量。末端准确 $C^2$ 端口给

$$
z(s,\theta)=H+b_3(\theta)t^3+b_4(\theta)t^4+b_5(\theta)t^5.
\tag{7}
$$

材料换元 $\theta=\Theta(\phi)$ 与 $s$ 无关，故 (7) 不因其无限材料谱而失去“径向次数至多5”。它不需要有限材料角带宽。$t<0$ 的盘内高度恒为 $H$；本论证只使用 $t>0$ 的最后非平片，没有把 $\chi=1$ 错放在 $T$ 以前。

若此场字面准确等距，则任一欧氏高度必须满足 [R623](R623-finite-material-height-and-highest-mode-defect.md) 已证明的 Darboux 恒等式

$$
z_{ss}(z_{\theta\theta}+aa'z_s)
-\left(z_{s\theta}-\frac{a'}a z_\theta\right)^2
=-aa''\left(1-z_s^2-\frac{z_\theta^2}{a^2}\right).
\tag{8}
$$

这个必要恒等式对原 $C^2$ 等距浸入成立，当前 piece 的有限径向表示允许逐次比较 Taylor 系数。

若高度首个非零项为 $b_n(\theta)t^n$，$n\ge3$，则 (8) 左边的最低可能项是

$$
R\,n^2(n-1)b_n(\theta)^2t^{2n-3}.
$$

角二导乘积和混合平方都至少高一个次数。右边由 (6) 从 $t^7$ 开始。因此比较 $t^3$ 强制 $b_3=0$；再比较 $t^5$ 强制 $b_4=0$；比较 $t^7$ 得

$$
100R b_5(\theta)^2=4RA^2,\qquad
b_5(\theta)^2=\frac{\kappa_p^2}{4h_o^6}.
\tag{9}
$$

$b_5$ 连续而其平方是严格正常数，故在连通圆周上为一个常数，等于 $\pm\kappa_p/(2h_o^3)$。于是 (7) 的全部角导数为0。

最后比较 $t^8$。由 $z_s=-5b_5t^4,z_{ss}=20b_5t^3$ 及 $aa'=-R-t+O(t^8)$，(8) 左边的 $t^8$ 系数为 $100b_5^2=4A^2$。右边的该系数为

$$
4A^2+9RAB
=4A^2-\frac{135R\kappa_p^2}{2h_o^7}.
$$

二者不相等，因为 $R,\kappa_p,h_o>0$。矛盾。故**当前固定 quintic 高度末片不存在字面准确等距根**，即使允许无限角模也如此。

该结论不提供一个统一正的 Gram 误差地板。上述不同项都乘以高次 $t$，径向精化可以减小其影响；有限阶表示也可以逐层逼近非多项式参考高度。它既不排除达到 $10^{-6}$，也不排除按 README 的同 $g$ 精化标准取得所需数值收敛。进一步增加精确轴向参考项可改变有限表示，但必须明说模型变化及实际残差读出。

### 准确末端系数的廉价读取公式

设原末胞宽为 $h$，在其左端的高度 cosine 系数 jet 为 $Y,U,A_0$；末端 q 三 jet 为0。沿 $t=T-s$ 的 q 幂系数为

$$
q_3=\frac{10Y+4hU+h^2A_0/2}{h^3},\quad
q_4=\frac{-15Y-7hU-h^2A_0}{h^4},\quad
q_5=\frac{6Y+3hU+h^2A_0/2}{h^5}.
$$

再仅对常模加上

$$
-\frac{10H}{\mathrm{width}^3},\quad
\frac{15H}{\mathrm{width}^4},\quad
-\frac{6H}{\mathrm{width}^5}
$$

便得到 (7) 的三个物理角系数列。它们准确判断是否非零，但不能只看未缩放的巨大系数就归因当前残差。源码同时输出每项在末胞的 $h^n$、$nh^{n-1}$、$n(n-1)h^{n-2}$ 量纲贡献上界，保留取消可能。是否值得把第三、四次高度作为优化方向，应由该新读取及真实目标试验决定。

这里的 $h$ **没有取 floating mesh 的相邻差再转 Fraction**。读取器使用原报告的准确 symbolic 节点，先要求末两节点的 $S$ 系数相同，再作准确常数项之差。本次既有定义为

$$
s_{J-2}=S-\frac{5764607523034235}{4611686018427387904},
\qquad s_{J-1}=S.
$$

所以非有理真 $S$ 准确抵消，$h$ 就是上式准确有理数。自由 $Y,U,A_0,H$ 及 lift 宽度本来按其准确 binary 数定义，故上述 Fraction 系数是真场在准确 symbolic 网格上的系数。新 Actions 报告逐项保存末两 symbolic 节点、零的 $S$ 系数差和“未采用 float mesh 差”标记。如果未来末两 $S$ 系数不相同，当前紧凑读取器会明确拒绝这个接口，不能再把相邻 carrier 差冒称真宽；那时须另用真 $S$ 的区间系数读取。

## 7. 一个保持同 g 的准确混合诊断

为检验当前尾误差是否适合轴对称参考方向，选择唯一 $\alpha=0$ 圈 $s_-$，以及准确 lift 起点 $s_+=S-\mathrm{width}$。设

$$
w(s)=S_5\!\left(\frac{s-s_-}{s_+-s_-}\right),\quad
S_5(u)=10u^3-15u^4+6u^5,
$$

并在区间外续为0、1。对实际父场定义

$$
F_\tau=F_{\rm parent}
+\tau w(s)(F_*-F_{\rm parent}).
\tag{10}
$$

$w,w',w''$ 在两个接点与相应常数片二阶相容；两场又使用同一 $H,R,T$ 和准确末端 jet。因此 (10) 保留 core、平帽和闭 $C^2$ 接缝。它保持作为比较目标的原 $a(s)$，没有同时修改 $g$。

若 $\Delta=F_*-F_{\rm parent}$，则完整六 jet 是

$$
\Delta_\tau F=\tau w\Delta,\quad
\Delta_\tau F_s=\tau(w'\Delta+w\Delta_s),\quad
\Delta_\tau F_\phi=\tau w\Delta_\phi,
$$

$$
\Delta_\tau F_{ss}=\tau(w''\Delta+2w'\Delta_s+w\Delta_{ss}),
$$

$$
\Delta_\tau F_{s\phi}=\tau(w'\Delta_\phi+w\Delta_{s\phi}),\qquad
\Delta_\tau F_{\phi\phi}=\tau w\Delta_{\phi\phi}.
$$

源码逐项使用这些式子。它保留全部原节点/中点/六 Gauss 观察行及 N2048 整圆等价角行，固定 $\tau=1,1/2,\ldots,1/128$，同时读取原正加权 Gram 平方和、真实正谱 $p=8,\varepsilon=.001,c=.05$ 目标、最大相对 Gram、完整六 jet 点主曲率及点直径下界。参考标量来自原 FullHold 的整数区间 oracle，记录普通 carrier 与外盒误差。

这里的场是**解析参考加混合场**，不再是原共享 quintic 空间；源码不会输出一个伪称原模型的新 npz 父。即使某一步有限目标变好，也只给模型扩展试验的理由。是否仍满足连续几何和全部原材料要求，尚需相应后续证明。若再把它重采样回原 quintic，那又是另一个明确的场，不能继承 (10) 的读出。

## 8. 代码与 Actions-only 参数

共享入口 [actions_closed_postprocess.py](../scripts/resume_20261120/actions_closed_postprocess.py) 为 59417 bytes，SHA-256：

eaa9a579eea227cbf348138295534144c39d07b669ea1c9ff494f22baa4ae599。

该版本只完成本地 AST 语法解析，没有本地科学计算。入口在本公开仓库 Actions 外拒绝科学执行，记录实际 run/commit/input/output 身份。原目录结构由公开重建链提供，历史文件名不保证与旧 SHA 相同。

无需全场扫描的末端读取：

    python topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_postprocess.py endpoint \
      --repo "$GITHUB_WORKSPACE" --work "$WORK" \
      --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-next-six.npz" \
      --out "$WORK/postprocess/a04-endpoint-height.json"

同 g 解析尾有限目标试验：

    python topics/visible-flex-larger-amplitude/scripts/resume_20261120/actions_closed_postprocess.py tail \
      --repo "$GITHUB_WORKSPACE" --work "$WORK" \
      --bundle "$WORK/geometry_path/curvature-qp-spectral-hessian-r22-next-six.npz" \
      --carrier "$WORK/recover_evidence/gauss6-current-three/same-scalar-gauss-observations.npz" \
      --scalar-input "$WORK/fullclosed_solver/data/pulse-a5-complete-base.json.gz" \
      --angles 2048 --stage-block 64 --line-trials 8 \
      --out "$WORK/postprocess/a04-exact-analytic-tail.json"

endpoint 子命令只读取一次新父末胞高度并作准确 Fraction 运算；tail 的标量盒是向外整数/Fraction，而场、Gram、曲率是普通 binary64 数值诊断。它没有连续 metric、连续 K 或 reach 证书。R670 的 direct 子命令则是另一套明确声明向外 arithmetic 的完整首 jet 几何覆盖。

三种子命令都接受自定义 bundle、carrier 和可重复的 manifest 参数。若使用公开 continue 的实际末父，可把 bundle 改为 curvature-qp-spectral-hessian-r22-union-next-four.npz，并把同名尾缀 -witnesses.json 传给 manifest。manifest 只提供永久位置，旧几何值全部丢弃；允许这些位置来自祖先，但径向 carrier 必须一致。tail 对每个未失败 trial 另实际读取所有曲率、半径、protected 位置的完整六 jet；旧7377行的目标保持不变，已知任意点的必要 reach 产品另与全部观察点合并。没有 manifest 时不伪称读了这些位置。

本条当前没有新 run 返回值，不把源已写好或语法已通过写成应用成功。


执行身份与是否已运行以正文各项状态为准，未执行准备源不冒称已有数值结果。临时数组沿原输入链再生；纯位置替代输入保计算语义，不冒称原raw报告的路径或逐字SHA。
