# R150 附录：任意固定复直线骨架、粗射线条带与全部有界相伴限制

日期：2026-11-13（UTC）。normal_resume_1cf；根代理独立核查旋转因式、粗条带几何和固定左半面界。根代理已全文核验。

状态：完整证明。把实骨架扩展到任意固定复直线，并在无限计数分支去掉相伴算子的有限谱假设。主行仍容复加权误差；一般有两个独立复方向的受控骨架未因此解决。

## 1. 全部普通点态幂的结论

设
$$
a\ge0,\quad a\in\ell^2\setminus\ell^1,\qquad
b\in\ell^2(\mathbb R),\quad |b_j|\le C_0a_j,
\qquad \psi\in\mathbb R.
$$
对 $\nu=0,1$ 取复行 $d^\nu$，满足
$$
d^\nu_j=0\quad(a_j=0),\qquad
K_\nu^2=\sum_{a_j>0}|d^\nu_j|^2/a_j<\infty,
$$
并取任意复 $e^0,e^1\in\ell^1$、$u_*,v_*,\gamma\in\mathbb C$。
定义原函数
$$
u=u_*+\sum_j(a_j+d^0_j+e^0_j)\chi_j,
$$
$$
v=v_*+\sum_j(e^{i\psi}b_j+\gamma a_j+d^1_j+e^1_j)\chi_j.
\tag{1.1}
$$
若 $G(x,s)$ 关于 $s$ 首一，$\deg_sG=m\ge1$ 且
$\deg_{\rm tot}G\le m$，则对任意 $\lambda\in\mathbb C$、
整数 $r\ge1$ 和任意复 $\ell^2$ 第一阶指数权 $e^w$，
$$
\boxed{[G(u,v-u^2)-\lambda]^r e^w\text{ 循环。}}
\tag{1.2}
$$

$\psi=0$ 是[复加权主行与实骨架主定理](R150-appendix-weighted-complex-main-real-controlled-skeleton-and-all-shear-powers.md)。
本稿不通过旋转主行来改变 $\psi$：非可和主行的有限相位缺陷方向唯一，
而剪切在主行旋转时要求辅助作双倍角旋转。
所以一般 $\psi$ 是旧内禀坐标重述没有覆盖的新范围。

## 2. 一个不要求有限谱的抽象排除引理

设 $\mathcal K\ne0$ 为 Hilbert 空间，$X$ 最大增生，
其收缩半群 $S(t)$ 具有以下实际好时间预算：

对任意 $k'>0$，存在 $\tau_n\to\infty$、$r_n=k'\log\tau_n$，
使整个左半平面有
$$
\sup_{\operatorname{Re}z\le r_n}\|(X-z)^{-1}\|
\le 2e^{r_n\tau_n}/r_n.
\tag{2.1}
$$
还假设其预解在整个复平面存在，并且对每个固定实 $B$，
$$
M(B):=\sup_{\operatorname{Re}z\le B}\|(X-z)^{-1}\|<\infty.
\tag{2.2}
$$
这里的 (2.2) 是固定常数；它不能仅由一个随 $n$ 增长的 (2.1) 常数来替代。
在实际应用中，两者均由同一真实 Laplace 积分给出。

令 $J\in B(\mathcal K)$ 与 $X$ 的全部预解交换，
$\alpha\in\mathbb C$、$|\alpha|=1$，$c\ge0$。
假设两个自然二次式
$$
T_\pm=cX\pm\alpha(X^2+JX),\qquad
\operatorname{Dom}T_\pm=\operatorname{Dom}X^2
\tag{2.3}
$$
均最大增生。

**引理2.1。** 上述条件不可能同时成立。

它不要求 $J$ 正规、有限谱、标量加拟幂零，也不改变原 Hilbert 范数。

### 2.1 旋转因式与条带外的统一界

写 $z=x+iy$、$R=|z|$，并置
$$
q_\pm(z)=cz\pm\alpha z^2,\qquad
G_\pm(z)=X+z+J\pm c/\alpha.
$$
在准确域 $\operatorname{Dom}X^2$ 上有
$$
\boxed{
F_\pm(z):=T_\pm-q_\pm(z)I\mp\alpha zJ
=\pm\alpha(X-z)G_\pm(z).
}
\tag{2.4}
$$
所有有界 $J$ 都保持 $X$ 的各自然幂域，并与相应算子交换，
因为它与全部预解交换。

固定
$$
B>\|J\|+c+1,\qquad d>\|J\|.
$$
当 $x\ge B$ 时，最大增生预解和有界扰动给
$$
\|G_\pm(z)^{-1}\|
\le\frac1{x-\|J\|-c}\le1.
\tag{2.5}
$$
若另有
$$
-\operatorname{Re}q_\pm(z)\ge d(R+1),
$$
则 $T_\pm$ 的最大增生预解与扰动 $\mp\alpha zJ$ 给
$$
\|F_\pm(z)^{-1}\|
\le\frac1{d(R+1)-R\|J\|}
=\frac1{(d-\|J\|)R+d}.
\tag{2.6}
$$
这是全域有界逆；因式中的两个自然一阶域也已由 (2.4) 识别。

准确的有界预解差恒等式为
$$
\boxed{
(X-z)^{-1}
=G_\pm(z)^{-1}
\pm\alpha(2z+J\pm c/\alpha)F_\pm(z)^{-1}.
}
\tag{2.7}
$$
例如将 $G_\pm-(X-z)=2z+J\pm c/\alpha$ 代入通常预解差，
再用 $F_\pm^{-1}=\pm\alpha^{-1}G_\pm^{-1}(X-z)^{-1}$ 即得。
因此在 (2.5)—(2.6) 的区域，
$$
\|(X-z)^{-1}\|
\le1+\frac{2R+\|J\|+c}{(d-\|J\|)R+d},
\tag{2.8}
$$
右侧有固定统一上界。

$x\le B$ 则已由固定的 $M(B)$ 控制。
故未控制的大点只能位于
$$
\mathcal U=
\{x\ge B:\ |\operatorname{Re}(\alpha z^2)|
\le cx+d(R+1)\}.
\tag{2.9}
$$

### 2.2 全部右向、左向与竖直射线

写 $\alpha=e^{-i\psi}$。
二次主部的四条零射线满足
$$
\theta=\psi/2+\pi/4+k\pi/2,\qquad k=0,1,2,3.
\tag{2.10}
$$
由 (2.9)，当 $R\to\infty$ 时
$$
|\cos(2\arg z-\psi)|=O(R^{-1}).
$$
因此每个未控制大点距四条射线之一有统一有界距离。

对任意一个相应角度，写
$$
z=e^{i\theta}(t+is),\qquad t\ge0.
$$
在该射线附近 $s=O(1)$、$R/t\to1$，并且准确有
$$
|\operatorname{Re}(\alpha z^2)|=2t|s|,
\qquad
x=t\cos\theta-s\sin\theta.
$$
所以 (2.9) 迫
$$
|s|\le\frac{c\cos\theta+d}{2}+o(1).
\tag{2.11}
$$
所有余项均针对固定 $\psi,c,d,B$ 统一。

若 $\cos\theta<0$，则该射线的固定宽带在足够远处满足 $x<B$，
故不会含未控制大点。
若 $\cos\theta=0$，任何固定宽带都满足固定的
$x\le h$，由 (2.2) 的 $M(h)$ 控制。
这里用的是实际 Laplace 在一个固定左半平面上的有限常数，
不是令 (2.1) 的常数随好时间增大。

只剩有限条 $\cos\theta>0$ 的右向射线。
对每条固定选择
$$
h_\theta>\frac{c\cos\theta+d}{2}.
\tag{2.12}
$$
于是除固定圆盘外，未控制点全部落在半条带
$$
z=e^{i\theta}(t+is),\qquad t\ge t_0,\quad |s|\le h_\theta.
\tag{2.13}
$$
在两长边 $s=\pm h_\theta$ 上，
$$
|\operatorname{Re}(\alpha z^2)|-cx-d(R+1)
=(2h_\theta-c\cos\theta-d)t+O(1)>0
$$
对充分大的 $t$ 成立，故长边由 (2.8) 控制。
短边紧致，预解连续，亦有固定界。
两个或更多带的有限重叠不会改变这些边界界。

也可统一取较粗的 $h=c+d+2$，
完全不需要任何趋零角度或最优宽度的讨论。

### 2.3 好时间矩形压住每条右向带

固定一条 $\cos\theta>0$ 的带。
利用 (2.1) 允许任意大 $k'$，选
$$
k'>\frac{2h_\theta\cos\theta}{\pi},
\qquad
\frac{\cos\theta}{k'}<\beta<\frac{\pi}{2h_\theta}.
\tag{2.14}
$$
同一个足够大的 $k'$ 也可以对所有右向带同时使用。
令
$$
L_n=\frac{r_n-h_\theta|\sin\theta|-1}{\cos\theta}.
\tag{2.15}
$$
则 $L_n\to\infty$，在远边 $t=L_n$、$|s|\le h_\theta$ 上，
实际 $z$ 始终满足 $\operatorname{Re}z\le r_n$。
因此
$$
\log\|(X-z)^{-1}\|
\le r_n\tau_n+O(\log r_n+1).
\tag{2.16}
$$

对任意单位 $f,g\in\mathcal K$，矩阵元
$$
p(w)=\langle(X-e^{i\theta}w)^{-1}f,g\rangle
$$
在半条带解析。
对 $\varepsilon>0$，乘上障碍
$$
\exp[-\varepsilon\cosh(\beta(w-t_0))].
$$
在闭带上，
$$
\operatorname{Re}\cosh(\beta(w-t_0))
\ge\cos(\beta h_\theta)
\cosh(\beta(\operatorname{Re}w-t_0)),
$$
其中 $\cos(\beta h_\theta)>0$。
由 (2.15)，远边障碍至少按
$$
c_\beta\tau_n^{\beta k'/\cos\theta}
$$
增长；(2.14) 使其指数严格大于1，故压过
$r_n\tau_n=k'\tau_n\log\tau_n$。
在有限矩形用最大模原理，先沿 $L_n\to\infty$，再令
$\varepsilon\downarrow0$，得到整个半条带的同一固定矩阵元界。
该界与单位 $f,g$ 无关，所以也是算子范数界。

所有右向带如此处理，竖直带与其余区域已在 §2.2 控制。
整个预解函数于是全平面有界。
负实轴上的最大增生预解界使其趋于零；
逐矩阵元 Liouville 迫 $(X-z)^{-1}=0$，和 $\mathcal K\ne0$ 上的真实逆矛盾。
引理2.1得证。

## 3. 实际主锚与旋转的两个第一阶

沿用主定理的真实对象：
$$
X_0=X_a,\quad U=X_{a+d^0},\quad
Z=U+\omega I,\quad L=Z^{-1},\quad
Y=e^{i\psi}X_b,\quad \alpha=e^{-i\psi}.
$$
取主定理 §3 的同一个
$$
\omega=1+K_0^2+
8\sum_j(|a_j+d_j^0|+a_j)\eta_j.
$$
则
$$
Z,\qquad cZ+\alpha Y,\qquad cZ-\alpha Y
$$
对全部 $c\ge2C_0+1$ 都是最大增生的原完整第一阶，
因为 $\alpha Y=X_b$ 恰为原实骨架。
共享 $\omega$ 的证明不受 $\psi$ 影响。

$Z$ 空谱，全部预解属于 $A'$，$L$ 拟幂零。
主定理 §4 的复局部指数、相位补偿和有限集合分解给
$$
\|e^{-tZ}\|
\le
\exp\!\left[-\kappa T
\sum_{j\ge J}\left\lfloor t|a_j+d_j^0|/T\right\rfloor\right]
$$
其中 $\kappa<1$ 任意固定，$T,J$ 适当固定。
原加权误差只使计数损失 $O(t)$。
因此若
$$
\Lambda_a=\limsup_{t\to\infty}
\frac{\Theta_a(t)}{t\log t}=\infty,
$$
就有引理2.1要求的全部 (2.1) 好时间预算。

还要单独支付 (2.2)。
真实半群对每个固定 $B$ 都满足
$$
\int_0^\infty e^{Bt}\|e^{-tZ}\|\,dt<\infty,
$$
因为不可和 $|a+d^0|$ 使上述计数除以 $t$ 趋于无穷。
故
$$
M(B)\le\int_0^\infty e^{Bt}\|e^{-tZ}\|\,dt<\infty.
\tag{3.1}
$$
该 Laplace 公式是已经与原预解识别的真实算子公式。

## 4. 任意实际闭不变空间上不存在有界完整相伴限制

令
$$
W=(Y-Z^2)_{\rm can},\qquad
\mathscr T=WL,\qquad
\operatorname{Dom}\mathscr T
=\{h:Lh\in\operatorname{Dom}W\}.
\tag{4.1}
$$
$W$ 为 R186 的规范闭多项式；$L$ 有界，所以 $\mathscr T$ 闭。
其图与全部有界 $A'$ 交换；在共同深域上
$$
\mathscr T=YL-Z.
\tag{4.2}
$$

**定理4.1。** 对任意有限对角放大，
不存在非零闭空间 $\mathcal M$ 同时满足
$$
\mathcal M\text{ 对全部对角 }A'\text{ 不变},\qquad
\mathcal M\subseteq\operatorname{Dom}\mathscr T^{(q)},
$$
$$
\mathscr T^{(q)}\mathcal M\subseteq\mathcal M,\qquad
J:=\mathscr T^{(q)}|_{\mathcal M}\in B(\mathcal M).
\tag{4.3}
$$
这里不要求 $J$ 有限谱。

先处理 $\Lambda_a=\infty$。
所有相关原第一阶的预解都保持 $\mathcal M$。
由实际 Yosida 逼近，$Z_\mathcal M$ 和
$(cZ\pm\alpha Y)_\mathcal M$ 的部分最大增生，
$Z_\mathcal M$ 仍空谱，(2.1)、(3.1) 的范数界直接限制到它。
$J$ 与这些共同有界正则器及 $L_\mathcal M$ 交换。

以下核自然二次域，不能把一个形式自然和直接当成闭算子。
R186 的有限族共同正则器保持 $\mathcal M$；
在共同深域上 (4.2) 给
$$
Y_\mathcal M f
=Z_\mathcal M^2f+JZ_\mathcal M f.
\tag{4.4}
$$
对任意 $f\in\operatorname{Dom}Z_\mathcal M^2$，
用同一正则器在 $Z_\mathcal M^2$ 图中逼近。
右侧收敛，原 $Y$ 的闭性给 $f\in\operatorname{Dom}Y$ 和 (4.4)。
同一正则向量的
$(cZ\pm\alpha Y)f_\varepsilon$ 也收敛；
原完整第一阶的闭性进一步给
$$
Q_\pm:=cZ_\mathcal M
\pm\alpha(Z_\mathcal M^2+JZ_\mathcal M)
\ \subseteq\
(cZ\pm\alpha Y)_\mathcal M,
$$
$$
\operatorname{Dom}Q_\pm=\operatorname{Dom}Z_\mathcal M^2.
\tag{4.5}
$$

这个自然多项式 $Q_\pm$ 闭且空谱。
准确地，将 $Q_\pm-\lambda$ 乘 $L_\mathcal M^2$，
得到最高常数 $\pm\alpha I$ 加上由
$L_\mathcal M$ 和有界交换 $J$ 组成的拟幂零项；
因为 $L_\mathcal M$ 拟幂零且与 $J$ 交换，所得有界因子是单位。
其逆乘 $L_\mathcal M^2$ 正好给全域有界实际逆，域为
$\operatorname{Dom}Z_\mathcal M^2$。
取一个负实 $\lambda$，
$Q_\pm-\lambda$ 满射而右侧最大增生部分减 $\lambda$ 单射，
于是包含关系迫准确相等。
这付了引理2.1的自然域和最大增生假设。
引理排除非零 $\mathcal M$。

若 $\Lambda_a<\infty$，
主定理 §§6—7 的实际复中心全柱证明已允许任意复受控骨架，
并且从未使用 $J$ 有限谱。
将那里的 $b$ 换成 $e^{i\psi}b$，其头绝对系数和尾 $\ell^2$ 成本均不变。
同一 $F_n$、复 $\sigma_n$、伴随深域配对和
$(I+J^*/\overline{\sigma_n})^{-1}\to I$ 的估计直接排除 (4.3)。
两个分支合并，证明定理4.1。

也因此，只要 $F\in A'$ 有界，
$\mathscr T+F$ 在任何这样的非零 $\mathcal M$ 上也不可能有有界完整限制：
否则减去保持 $\mathcal M$ 的有界 $F$ 就违反定理4.1。

## 5. 一个无需局部谱信息的自然单首多项式推论

设 $B_0,\ldots,B_{d-1}\in A'$，$d\ge1$。
在实际自然域 $\operatorname{Dom}\mathscr T^d$ 上定义
$$
P(\mathscr T)
=\mathscr T^d+\sum_{j=0}^{d-1}B_j\mathscr T^j.
\tag{5.1}
$$
则
$$
\boxed{\ker P(\mathscr T)=\{0\}.}
\tag{5.2}
$$
未在此断言 (5.1) 的整个自然图自动闭合；
排核只用以下真正闭的相伴核图。

若核非零，置
$$
\Gamma=
\{(h,\mathscr Th,\ldots,\mathscr T^{d-1}h):
h\in\operatorname{Dom}\mathscr T^d,\ P(\mathscr T)h=0\}.
$$
$\Gamma$ 是闭空间：
若这些坐标收敛，由 $\mathscr T$ 闭性逐层识别前 $d-1$ 次作用，
而
$$
\mathscr T^dh=-\sum_{j<d}B_j\mathscr T^jh
$$
的右侧随坐标收敛，最后再用一次闭性识别最高作用。
$\Gamma$ 对全部对角 $A'$ 不变。

每个最高作用还属于 $\operatorname{Dom}\mathscr T$：
右侧各 $B_j$ 保持该域，而且各
$\mathscr T^jh$ 在 $j<d$ 时都属于该域。
故 $h\in\operatorname{Dom}\mathscr T^{d+1}$，
并由域交换得 $P(\mathscr T)\mathscr Th=0$。
所以对角 $\mathscr T$ 保持 $\Gamma$，
其作用是有界的标准相伴矩阵
$$
(h_0,\ldots,h_{d-1})
\longmapsto
(h_1,\ldots,h_{d-1},-\sum_{j<d}B_jh_j).
$$
这与定理4.1矛盾。
(5.2) 因而成立，且所有 $B_j$ 只需在 $A'$ 中，
不需要局部代数字符或有限谱信息。
一般更大的规范闭扩张需另付图核心，不能由 (5.2) 免费替代。

## 6. 回到原 Bell 图与原普通点态向量

对 (1.1) 的原全部系数以及原 $w$ 先构造完整 Bell 多项式。
保持原 cumulant、常数、加权误差、可和误差及复倾斜。
与主定理 §5 相同，在同一个共同深域上有
$$
x_{\rm old}=Z+H,\qquad
y_{\rm old}=Y+RZ+K,
$$
其中 $H,K\in\mathcal A$、$R$ 属原局部有界系数代数。
若 $s=Y-Z^2$，则
$$
s_{\rm old}=s+(R-2H)Z+K-H^2.
$$
首一最高剪切项和总次数限制保持不变。

R186 的同一有限族共同正则器和
$\mathbb C[A]e^w$ 图核心识别的仍为最初原 Bell 闭实现。
若其核非零，原相伴深图构造产生一个非零闭图
$\mathcal M$，满足 (4.3)；
这一构造只用首一性、完整词域与有界系数，不以有限谱为先决条件。
定理4.1直接排除它。
所以原 Bell 最大核为零，
原 $C$ 自伴性和循环指数的图核心给其像稠密，
也就是 (1.2)。

这里明确使用深图构造来处理原规范最大图，
没有用 §5 的自然域排核偷换该最大图。

## 7. 新范围与剩余边界

本稿允许独立骨架沿任意固定复直线，
而主、副误差及仿射斜率仍可任意复。
例如任一正非可和 $a$ 与实受控 $b$，
$v=i\sum b_j\chi_j$ 的全部所述剪切幂也已覆盖，
即使 $b$ 不属于 $\mathbb C a+\mathscr J_a$。

在主行已有有限相位缺陷的内禀坐标中，
§1 的条件可准确写成
$$
e^{-2i\theta}\nu
\in e^{i\psi}\{b:\ b\text{ 实},\ |b|\le C|\mu|
\text{ 对某 }C<\infty\}
+\mathbb C|\mu|+\mathscr J_{|\mu|}.
$$
权重替换理由仍为前稿 §10 的 Hellinger 比较。
$\psi$ 可自由选择；它与被主行确定的 $\theta$ 是不同参数。

无限计数分支的全 $J$ 排除，是使用任意大的好时间预算后得到的更强结论。
它不声称有限计数值下原最优窄条带常数仍与相位无关。
一般复受控骨架若不能模去
$\mathbb C a+\mathscr J_a$ 后落在一条固定复直线，
本稿的两个最大增生 first 尚未构造。
超总次数剪切、一般真正常见证聚合上界和普通 Hilbert ISP 仍保持原缺口。
