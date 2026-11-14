# R751：原全部周期压缩到既有 280 次域的准确公式

日期：2026-11-14。状态：**本篇的周期恒等式、挠点分母压缩、原目标相位和有限矩阵接口已证明。** 下面不预称这些新周期数或线性核已经由 Actions 算出。

本篇接 R732、R735、R738、R745。保留原六个有理微分、819 条有向相对边、800 条整数闭链、原 $c_0,c_1$ 和所有绝对相位。原 87961 个端点不需要各自引入新的挠点层：全部周期可由每个系数嵌入上的 40 个分母为 $p=41$ 的加法扭曲值生成；在原目标周期规范下，更全部属于 R735 **同一个** $K(U)$，其中 $[K(U):K]=280$。

## 1. 全部固定对象与符号

沿用 R745：
$$
p=41,\quad N=6p=246,\quad n=42,\quad
\eta=e^{2\pi i/42},\quad A=\mathbf Q(\eta),\quad
\zeta=\eta^{14},\quad K=\mathbf Q(\zeta),
$$
$$
s=1+2\zeta=i\sqrt3,\quad \alpha=\sqrt[3]4>0,\quad
\beta=\eta+\eta^{-1},\quad
\mathcal H=\{1,13,19,25,31,37\}.
\tag{751.1}
$$
$\sigma_h:\eta\mapsto\eta^h$ 是 $A/K$ 的全部六个自同构。
原角色仍是
$\theta(y)=\eta^{-\log_\gamma(\bar y/y)}$，$\gamma=7+30\zeta$，
$\theta_h=\sigma_h\theta$。特别地
$$
\theta_h|_{\mathbf F_p^\times}=1,\qquad
\theta_h(\zeta)=\zeta^{-1},\qquad \theta_h(s)=-1.
\tag{751.2}
$$

固定 R732 的模型及正实周期
$$
E_0:y^2=x^3-1,\quad \omega_0=dx/(2y),\quad
\Lambda_0=\Omega_0\mathbf Z[\zeta],\quad \Omega_0>0.
\tag{751.3}
$$
令 $f_h$ 为 R745 的 primary 理想和 newform，并准确记
$$
\lambda_h(t)=\frac1{\Omega_0}\int_\infty^t2\pi i f_h(z)\,dz
=\frac{L(f_h,t,1)}{\Omega_0},\qquad\lambda_h(\infty)=0.
\tag{751.4}
$$
它以 1 为周期。以下所有有理分母的缩小均是 (751.4) 的精确恒等式，不是改选一个周期基。

## 2. 先将每条原边拉回 $\{0,\infty\}$

### 2.1 同一个完整有限表示

在原有限左模型 $V=A^{\mathbf F_p}/A\mathbf1$ 中用 $e_r$，$\sum e_r=0$。
令 $\rho_h$ 为原 cuspidal 表示。对上三角矩阵它是仿射置换；对
$w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$，
$$
\rho_h(w)e_r=-\frac1p\sum_{y\ne0}\theta_h(y)e_{rNy+\operatorname{Tr}y}.
\tag{751.5}
$$
R745 已生成原向量
$$
u=\frac1{42}\sum_{t\in\mathsf T_\zeta}\rho_1(t)e_0
=\sum_{r=1}^{40}\frac{c_r}{p(p+1)}e_r.
\tag{751.6}
$$
本篇读取这些 $c_r$，不重新枚举其环面纤维或 $N_h$。

对每个原 Manin 矩阵 $g\in\mathrm{SL}_2(\mathbf Z)$ 定义
$$
u_g=\rho_1(g_p^{-1})u
=\sum_{r=1}^{40}\frac{d_{g,r}}{p(p+1)}e_r,
\qquad d_{g,0}=0.
\tag{751.7}
$$
准确有 $d_{g,r}\in\mathbf Z[\eta]$。这是一个全局整数分母结论：
$$
u_g=\frac1{p+1}\sum_{t\in\mathsf T_\zeta}\rho_1(g_p^{-1}t)e_0,
$$
而每个单一 Bruhat 矩阵的一个列至多含一次 $1/p$。
不能把对已有 $c_r$ 再施加 Weyl 的表面 $p^2(p+1)$ 当最终分母。
用 (751.5) 从已保存向量运输时，该多出的 $p$ 必须在原商基中精确约掉。

一个便于实现、方向完整的 Bruhat 分解是：若
$g_p=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$、$c\ne0$、$\Delta=ad-bc$，则在 $\mathrm{PGL}_2$ 中
$$
g_p=
\begin{pmatrix}1&a/c\\0&1\end{pmatrix}
w\begin{pmatrix}c&d\\0&\Delta/c\end{pmatrix}.
\tag{751.8}
$$
显示矩阵的乘积为 $-g_p$，而中心在原模型上平凡。两端都是明确仿射置换。
因此所有新运输由一张原 Weyl 矩阵和已保存向量给出，不重新计算任何环面平均。

在 tame 系数基 $(H_0^\circ,4H_2^\circ)$ 上令
$$
M_2(S)=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
M_2(T)=\begin{pmatrix}-1&0\\-1&1\end{pmatrix},\qquad
v=\binom1{-\zeta^2}.
\tag{751.9}
$$
这是**右** slash 的系数反表示：$M_2(ab)=M_2(b)M_2(a)$。
设
$$
\binom{x_g}{y_g}=M_2(g_2)v.
\tag{751.10}
$$
令 $\chi_3:\mathrm{SL}_2(\mathbf F_3)/Q_8\to\mu_3$ 由
$\chi_3(T_3)=\zeta$、$\chi_3(S_3)=1$ 给出，并记 $\chi_g=\chi_3(g_3)$。

R592/R742/R745 的确切 intertwining 是：经典右 slash 的 $p$ 因子为
$\rho_h(g_p^{-1})$，纯 2 因子为 $M_2(g_2)$，纯 3 因子为 $\chi_g$。
这里保留绝对 CRT 索引
$$
0\le k_r<246,\quad k_r\equiv0\ (6),\quad k_r\equiv r\ (41),
\quad H_{0,r}=f_h((\tau-k_r)/246),\quad
H_{2,r}=f_h(4(\tau-k_r)/246).
\tag{751.11}
$$
其 Fourier 相位是 $\xi^{-mr/6}$，不是 $\xi^{-mr}$。
这与上述有限左作用兼容：把标准 $f(z/p)$ 实现改为 $z=\tau/6$ 时，矩阵同时由
$d_6=\operatorname{diag}(1/6,1)$ 共轭，基索引同时由 $r\mapsto r/6$ 改写。
二者的共轭相消，故几何 $g_p$ 仍作用为原 $\rho_h(g_p^{-1})$。
只改 Fourier 指数而不同时运输矩阵会给错误的环面和周期。

### 2.2 原相对边的压缩公式

令 $a_r\in\{0,\ldots,40\}$ 满足
$$
a_r\equiv-k_r/6\equiv-r/6\pmod p.
\tag{751.12}
$$
从 $0$ 到 $\infty$ 作变量替换，直接有
$$
\frac1{\Omega_0}\int_0^\infty2\pi iH_{0,r}(\tau)\,d\tau
=-246\lambda_h(a_r/p),
$$
$$
\frac1{\Omega_0}\int_0^\infty2\pi i\,4H_{2,r}(\tau)\,d\tau
=-246\lambda_h(4a_r/p).
\tag{751.13}
$$
负号来自从有限尖点积分到 $\infty$；第二式的 4 恰好抵消该退化映射的导数分母。
于是 R745 原六个微分在边 $e_g=\{g0,g\infty\}$ 上满足
$$
\boxed{
\frac1{\Omega_0}\int_{e_g}\omega_j
=-\frac{\alpha s}{7}\chi_g
\sum_{h\in\mathcal H}\sigma_h(\beta)^j
\sum_{r=1}^{40}\sigma_h(d_{g,r})
\left[x_g\lambda_h(a_r/p)+y_g\lambda_h(4a_r/p)\right].
}
\tag{751.14}
$$
该式是把原函数先右 slash $g$ 后沿 $\{0,\infty\}$ 积分；没有重新选边、换方向或改两树消元。
当 $g=1$ 时，$x_g=1,y_g=-\zeta^2,d_{g,r}=c_r$，与 R745.23–25 完全相同。

因为 gauge 中 $d_{g,0}=0$，只出现 $a_r\ne0$ 的 **40 个**加法值。
也可独立核 $\sum_{a\in\mathbf F_p}\lambda_h(a/p)=0$：原 $a_{pm,h}=0$，逐 Fourier 项求和即得。
全部 800 个闭周期只将 (751.14) 按 R738 已保存的整数系数求和。
因此 BFS 的大整数提升和原端点分母不再进入后面的挠点层。

## 3. $M=3p$、固定正实三挠点和逆角色

固定 $P_1=\Omega_0/p\in E_0[p]$，并令
$$
P_b=[a]P_1+[b_1][\zeta]P_1
\quad\text{当 }b=a+b_1\zeta\in\mathbf F_{p^2}.
\tag{751.15}
$$
另外取
$$
Q=2\Omega_0/3=(\alpha,+\sqrt3),\qquad
\xi=e^{2\pi i/p}.
\tag{751.16}
$$
这不是 $\Omega_0/3=(\alpha,-\sqrt3)$。两者的符号不得交换。

**定理 751.1。** 对所有 $h\in\mathcal H$、$a\in\mathbf F_p$，
$$
\boxed{
\lambda_h(a/p)
=-\frac{\sqrt3}{3p}\sum_{b\in\mathbf F_{p^2}^{\times}}
\frac{\theta_h(b)^{-1}\xi^{9aNb}}{x(P_b)-\alpha}.
}
\tag{751.17}
$$

证明。R732.9 的规范是 $L/\Omega_0=(1/M)\sum W\overline{\mathcal E}$，
其中 $\mathcal E(z)=\zeta_{\Lambda_0}(z)-\bar z/A_{\Lambda_0}$ 为完整完成化 zeta。
本题的真正有限角色导子在 primary 元素上支持于 $3p$，故取 $M=3p$；
没有删去 2-Euler 因子。因 $p\equiv2\pmod3$，全部 primary 类恰写成
$$
v=2p+3b\pmod{3p\mathcal O_K},\qquad b\in\mathcal O_K/p.
\tag{751.18}
$$
$p\nmid v$ 恰为 $b\ne0$，$\theta_h(v)=\theta_h(b)$，$Nv\equiv9Nb\pmod p$，且
$\Omega_0v/(3p)=Q+P_b$。因此
$$
\lambda_h(a/p)=\frac1{3p}\sum_{b\ne0}
\theta_h(b)\xi^{9aNb}\overline{\mathcal E(P_b+Q)}.
\tag{751.19}
$$
复共轭固定 $Q$，把 $P_b$ 送至 $P_{\bar b}$。换元 $b\mapsto\bar b$ 后
$\theta_h(\bar b)=\theta_h(b)^{-1}$，但**加法相位未被共轭**，仍是正号 $\xi^{9aNb}$。

原完成化保留通常的加法恒等式
$$
\mathcal E(P_b+Q)=\mathcal E(P_b)+\mathcal E(Q)
 +\frac{y(P_b)-\sqrt3}{x(P_b)-\alpha}.
\tag{751.20}
$$
线性非全纯项在此精确相消。
权 $\theta_h(b)^{-1}\xi^{9aNb}$ 在 $b\mapsto-b$ 下不变，故 (751.20) 中的
$\mathcal E(P_b)$ 和 $y(P_b)/(x(P_b)-\alpha)$ 两个奇项相消。
对每个非零 norm fiber，$\theta_h$ 在 $\ker N$ 上非平凡：其限制的阶为 21。
故
$$
\sum_{b\ne0}\theta_h(b)^{-1}\xi^{9aNb}=0.
\tag{751.21}
$$
这消掉 $\mathcal E(Q)$，余项恰为 (751.17)。没有丢弃任何未知完成化常数。
若 $x(P_b)=\alpha$，则 $P_b=\pm Q$，同时为非零 $p$-挠点和三挠点，矛盾；所以所有分母非零。$\square$

这也说明 R732 的正则化在本篇如何变成有限有理函数：先使用其完整、已证明的权一公式，
随后由准确字符和奇偶性消项，不能先把条件收敛级数中的完成化删去。

## 4. 六个单位的完整轨道权与 280 次旧商

令 $\mathcal B$ 是 $\mathbf F_{p^2}^{\times}/\mu_6$ 的任意一组明确代表。
它有 $(p^2-1)/6=280$ 项。若 $\varepsilon=\pm\zeta^j$，则
$$
N(\varepsilon b)=Nb,\quad
\theta_h(\varepsilon b)^{-1}=\zeta^j\theta_h(b)^{-1},\quad
x(P_{\varepsilon b})=\zeta^j x(P_b).
\tag{751.22}
$$
最后一式来自原正 CM 算子 $[\zeta](x,y)=(\zeta x,y)$；解析上
$\wp(\zeta z)=\zeta^{-2}\wp(z)=\zeta\wp(z)$。
因此**包括角色与加法项**的轨道和为
$$
\sum_{\varepsilon\in\mu_6}
\frac{\theta_h(\varepsilon b)^{-1}\xi^{9aN(\varepsilon b)}}
     {x(P_{\varepsilon b})-\alpha}
=6\theta_h(b)^{-1}\xi^{9aNb}
\frac{x(P_b)^2}{x(P_b)^3-4}.
\tag{751.23}
$$
这里使用 $\sum_{j=0}^2\zeta^j/(\zeta^j x-\alpha)=3x^2/(x^3-4)$。
只写裸分母的轨道和而不携带 (751.22) 会得到另一函数。

取
$$
u=\alpha e^{\pi i/6},\qquad u^6=-16,\qquad u^3=4i.
\tag{751.24}
$$
方向固定为
$$
D_u:E_0\longrightarrow E_{27},\quad
(x,y)\longmapsto(u^2x,u^3y),\quad D_u^*\omega_{27}=u^{-1}\omega_0.
\tag{751.25}
$$
置 $P'=D_u(P_1)$、$x_*=x(P_1)$，并取
$$
U=\frac{64}{X(P')^3}=-\frac4{x_*^3}.
\tag{751.26}
$$
这正是 R735.3 的同一商坐标及同一首一多项式 $P(U)$，不是另算一份除法多项式。
其次数 280、$41$-Eisenstein 性已由原公开证书给出；在 $K$ 上仍不可约，因 $41$ 是 $K$ 的未分歧均匀元。
因此
$$
\mathcal E=K[U]/(P(U)),\qquad[\mathcal E:K]=280.
\tag{751.27}
$$
在本篇复嵌入中，$P_1$ 是正实周期上靠近原点、$y<0$ 的点。
可用原 $E_0[p]$ 最大正实 $x$ 根及此 $y$ 符号准确隔离它；等价地固定相应负实 $U$ 根。
以下 §6 证明这一根给的 $b(U)$ 仍是 R735 原正实模型，而不是换成别的目标共轭。

对 $b\ne0$，因 $[b]$ 与 $[-1]$、$[\zeta]$ 交换，有唯一的有理函数
$R_b(U)\in K(U)$ 使
$$
x(P_b)=x_*R_b(U).
\tag{751.28}
$$
这是可直接执行的有限数据：在 $E_{27}$ 上从 $P'$ 作整数倍点、原
$[\zeta](X,Y)=(\zeta X,Y)$ 和一次加法，代入 $X(P')^3=64/U$ 后计算。
偶性消掉 $Y$，三次权重留下 $X(P')$ 乘以 $U$ 的有理函数。
所有必要逆元均在 (751.27) 中用 Euclid 求出并验乘积为一。
若一个中间加法出现 $O$，使用完整群法分支；这不允许删除相应 $b$。

由 (751.17)、(751.23)、(751.26) 得
$$
\boxed{
\lambda_h(a/p)=\frac{\sqrt3\,x_*^2U}{2p}
\sum_{b\in\mathcal B}\theta_h(b)^{-1}\xi^{9aNb}
 \frac{R_b(U)^2}{R_b(U)^3+U}.
}
\tag{751.29}
$$
分母 $R_b^3+U$ 非零，因为这与前面的 $x(P_b)^3=4$ 等价，而后者只能给三挠点。
改变轨道代表时 $\theta_h(b)^{-1}R_b^2/(R_b^3+U)$ 中两项的三次单位相互抵消；
故 (751.29) 与代表选择无关。

## 5. Weil pairing 的确切方向与 $\xi\in K(U)$

令 $e_p$ 采用如下准确函数规范。若 $f_P$ 的除子为 $p(P)-p(O)$，并在
$t=-X/Y$ 处以首项 $t^{-p}$ 归一，则对独立 $p$-挠点
$$
e_p(P,Q)=(-1)^p\frac{f_P(Q)}{f_Q(P)}.
\tag{751.30}
$$
本篇取
$$
\boxed{\xi=e_p(P',[\zeta]P').}
\tag{751.31}
$$
这准确等于 $e^{2\pi i/p}$，不是仅指定一个未知本原 $p$ 次根。

为核符号，先在 $E_0$ 的格上写 $\omega_1=\Omega_0,\omega_2=\Omega_0\zeta$，
相应 zeta 拟周期为 $\eta_1,\eta_2$。Legendre 关系是
$\eta_1\omega_2-\eta_2\omega_1=2\pi i$。
对 $P=\omega_1/p,Q=\omega_2/p$，以同一 sigma 函数写
$$
f_P(z)=\left(\frac{\sigma(z-P)}{-\sigma(P)\sigma(z)}\right)^p e^{\eta_1z},
\qquad
f_Q(z)=\left(\frac{\sigma(z-Q)}{-\sigma(Q)\sigma(z)}\right)^p e^{\eta_2z}.
\tag{751.32}
$$
这两个函数周期且首项为 $z^{-p}=t^{-p}(1+O(t))$。
由 sigma 的奇性，
$$
\frac{f_P(Q)}{f_Q(P)}=(-1)^p
\exp((\eta_1\omega_2-\eta_2\omega_1)/p)
=(-1)^p e^{2\pi i/p}.
$$
结合 (751.30) 得所称方向。$D_u$ 是同构，保持该 pairing。
R738 使用的有序周期标签是 $(\zeta,1)$；若程序按这个顺序先算
$e_p([\zeta]P',P')$，结果必须取逆才是 (751.31)。本篇不交换 R738 的原标记。

(751.30) 可用原曲线上的 monic Miller 函数准确计算。
线函数、竖线和 $t=-X/Y$ 的首项显式给出每步归一常数；所有常数同样保留。
计算须检验 $\xi^p=1,\xi\ne1$，但这两项仅检验本原性，不能替代刚才的解析方向证明。

最后由 R725，$K(E_{27}[p])/K$ 的群是 $\mathbf F_{p^2}^{\times}$。
$U=64/X(P')^3$ 的稳定子恰为六个 CM 单位：坐标相等强迫
$P'$ 只改变一个 $\mu_6$ 倍数。故 $K(U)$ 恰是其 $\mu_6$ 固定域。
每个单位范数为一，Weil pairing 的协变性给
$$
e_p([\varepsilon]P',[\varepsilon\zeta]P')
=e_p(P',[\zeta]P')^{N\varepsilon}=\xi.
$$
因此 (751.31) **属于既有 $K(U)$**，不需要再添一个次数 40 的独立圆分域。
可在辅助坐标代数中求 (751.30)，随后精确检查其只有 $K(U)$ 坐标；
该下降有上述数学证明，而不是一次数值识别。

## 6. 原正实目标的标记与全部根式的消去

令 R735 已保存的函数为
$$
W(U)=\prod_{a=1}^{20}\frac{A_a^2B_a}{4A_a^3+UB_a^3},\quad
R_3(U)=\prod_{a=1}^{20}\frac{A_a^3+UB_a^3}{A_a^3-2UB_a^3},\quad
S(U)=W(U)(1-3^{20}R_3(U)^2).
\tag{751.33}
$$
它们从原完成状态的 `wn,wd,rn,rd` 读出；不重跑旧倍点乘积、旧 $b$ 或旧迹。
原恒等式为
$$
r_0(P')=\frac{X(P')U^7S(U)}8,\qquad
b(U)=\frac{U^{40}S(U)^6}{64}.
\tag{751.34}
$$

这里必须核对 $P'$ 不是原 $E_{27}$ 的实 $p$-挠点。
因为其格是 $\Omega_0u^{-1}\mathcal O_K$，最小正实周期是
$\Omega_0(2+\zeta)/u=\sqrt3\Omega_0/\alpha$。
故原正实周期上的点是
$$
P_{27}^{\rm real}=[2+\zeta]P'=[-\zeta s]P'.
\tag{751.35}
$$
R725 的原 $r_0=(w-w\circ[s])/2$ 在 $[\zeta]$ 下乘 $\zeta$、在 $[s]$ 下乘 $-1$、在 $[-1]$ 下不变。
因此
$$
r_0(P_{27}^{\rm real})=-\zeta r_0(P'),\qquad
r_0(P_{27}^{\rm real})^6=b(U).
\tag{751.36}
$$
所以本篇选择的负实 $U$ 根仍产生 R735 的同一个正实 $b$，不是选择另一目标。
等价地，原三同源对 $U$ 的作用为 $U\mapsto-27U/(1+U)^3$，且 $b$ 在该作用下不变。

固定 R732 的原目标尺度
$$
R_C=u\,r_0(P_{27}^{\rm real})/\alpha,
\qquad R_C^6=-b,
\qquad\Lambda_C=(\Omega_0/R_C)\mathcal O_K.
\tag{751.37}
$$
由 $X(P')=u^2x_*$、$u^3=4i$、$s\sqrt3=3i$ 和 $x_*^3=-4/U$，完整相位计算给
$$
\begin{aligned}
R_C\,(\alpha s\sqrt3\,x_*^2)
&=-\zeta\frac{u^3x_*U^7S(U)}{8\alpha}
       (\alpha s\sqrt3\,x_*^2)\\
&=\boxed{-6\zeta U^6S(U)}.
\end{aligned}
\tag{751.38}
$$
此处的 $-\zeta$ 来自 (751.35)，不能在未核原实点时仅任选一个六次根。
式 (751.38) 消掉的是两个已明确模型之间的实际周期尺度；它不是未求出的模参数化/KS 常数。

## 7. 所有原归一周期的单一 280 次域公式

对 (751.7) 的精确向量和 $b\in\mathcal B$，定义
$$
T_{j,g,r,b}=\operatorname{Tr}_{A/K}
       (\beta^j d_{g,r}\theta(b)^{-1})\in\mathbf Z[\zeta],
\tag{751.39}
$$
$$
C_{j,g,b}=\sum_{r=1}^{40}T_{j,g,r,b}
\left(x_g\xi^{9a_rNb}+y_g\xi^{36a_rNb}\right)\in K(U).
\tag{751.40}
$$
所有 $\eta$ 坐标在这一步通过原六个 $h$ 的准确迹消去。
这是相对 $A/K$ 的迹，不能误用全部十二个嵌入的迹或再除一个未知因子二。

将 (751.29) 代入 (751.14)，再用 (751.38)，得到
$$
\boxed{
\frac{R_C}{\Omega_0}\int_{e_g}\omega_j
=\frac{3\zeta}{7p}\,U^7S(U)\chi_g
\sum_{b\in\mathcal B}C_{j,g,b}\frac{R_b(U)^2}{R_b(U)^3+U}
\ \in K(U).
}
\tag{751.41}
$$
本题 $7p=287$。两个负号分别来自 (751.13) 的积分方向和 (751.38) 的真实目标相位，
故最终系数为正的 $3\zeta/(7p)$。
所有有限平均、$246$ 的微分变化、$1/(3p)$ 的 primary 格点核和六单位求和均已在显示式中保留。

原每个闭链 $\gamma_i=\sum_e m_{ie}e$ 使用 R738 保存的同一整数 $m_{ie}$，于是
$$
\Pi_{ji}:=\frac{R_C}{\Omega_0}\int_{\gamma_i}\omega_j
=\sum_e m_{ie}\frac{R_C}{\Omega_0}\int_e\omega_j\in K(U),
\quad 0\le j\le5,\ 1\le i\le800.
\tag{751.42}
$$
这既保留了全部原周期，也把精确算术环境限制为已有次数 280 的字段。

## 8. 下一次公开计算的完整有限接口

只读取三次已完成公共产物：

1. R738 的原 cosets/markings 和整数闭链，两张 SHA 分别为
   `6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161`、
   `d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf`。
2. R745 run `43616027318` 的原 Hodge 表
   `original-p41-Hodge-q-expansions.json.gz`，SHA
   `a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd`。
   只复用 $c_r$、角色标签和已完成数据；新的 $g_p^{-1}$ 运输不会重算其环面平均或范数。
3. R735 run `43608152850` 的同一模数和完整状态，SHA 分别为
   `7063eacd17ffec4c68dea5d8c3a2cab278286653fd12aae07f1c955bb1ad94fb`、
   `9cd5f6731c7cfa76cd118b5f3a8ab1efb12d0d69ba95ab08817fcb80c2073427`。
   读取 $P(U)$、`wn,wd,rn,rd` 与原 $b(U)$，不重算旧除法、多项式、模型迹或 $F_{41}$。

新算术按如下有限顺序进行。

- 在 $K[U]/P$ 中建立准确运算；原 $b$ 的七次关系沿用 R735。
- 用原固定曲线群法生成 (751.28) 的 280 个轨道函数，保持每个实际 $b$ 标签。
  用按 (751.30) 归一的 Miller 算式生成 (751.31)，验证它位于 $K(U)$、阶为 41。
- 从 R745 保存的 $c_r$ 和原 Weyl 公式生成 (751.7)；精确检验整数 $d_{g,r}$ 和原反表示方向。
  从原 $g\bmod2,3$ 生成 $x_g,y_g,\chi_g$，不能依照端点大小选择别的提升。
- 算 (751.39)–(751.41)，再按原闭链算 (751.42)。可缓存有限 $p$ coset 的同一运输，
  但每条原边和闭链的系数最终仍须完整覆盖。

这时 R732 的同态核就是一个具体的有限 $K$-线性系统。
令 $L=K(b)\subset K(U)$，$[L:K]=7$，未知数写为
$$
v_j=\sum_{t=0}^6x_{jt}b^t,\qquad x_{jt}\in K.
\tag{751.43}
$$
将每个 $\sum_jv_j\Pi_{ji}$ 在 $1,U,\ldots,U^{279}$ 中展开，令全部非恒定坐标为零。
因此矩阵恰有 **42 列、至多 $279\cdot800$ 行**；第 $(i,a)$ 行、第 $(j,t)$ 列为
$$
[U^a]\bigl(b^t\Pi_{ji}\bmod P(U)\bigr),
\qquad 1\le a\le279.
\tag{751.44}
$$
可以流式消元，不必把全部大矩阵重复存入 Git。即使已达到应有秩 36，
得到的核仍需代回所有 800 个原周期等式；不能只凭先出现的一批行就删除后续条件。
R732 的证明识别该核与 $\operatorname{Hom}_L^0(A_{\theta,1},C)$，其 $K$-维数是六。
这一数学识别不等于已经获得新的数值核；实际 rank、核基和全部代回证书等待公开计算。

取核基后仍要按原周期格清除整数分母，再用 R732 的 Riemann–Roch 恒等式生成原有理函数。
本篇不把任何清分母整数预设为 $41$-单位。$c_0$ 的基点条件、$c_1$ 的原 coset 4424、
$g_*$ 的一次 $\zeta^2$ 运输和原 Poincaré/高度规范仍照原输入保留。

## 依据

- [R732](R732-original-CM-period-kernel-and-bounded-rational-function-recovery.md)：原权一完成化、$L/\Omega_0$、目标周期尺度和全部同态核。
- [R735](R735-exact-original-p41-CM-model-and-Neron-input.md)、[R725](R725-original-CM-elliptic-model-and-splitting-field.md)：同一 $E_{27}$、原 $r_0$、$U$ 商、$b$、相位及全部域次数。
- [R738](R738-certified-original-p41-period-input.md)、[R745](R745-certified-original-p41-Hodge-and-adelic-input.md)：原有向边、闭链、标记和准确微分。
- [R592](R592-actual-integral-CM-jet-lattice-and-complete-tail.md)、[R742](R742-unramified-original-first-jets-and-depth-seven-Abel-isometry.md)：原有限左作用与右 slash、tame 矩阵及绝对 CRT 索引。
- P. Mercuri–R. Schoof, *Modular forms invariant under non-split Cartan subgroups*, §§2、4、6，[作者稿](https://reneschoof.github.io/mcom3503.pdf)：原 cuspidal Bruhat 模型及其 newform intertwining。本篇的 $\pm$、$6^{-1}$、$\zeta^2$ 与实际目标相位均由显示计算固定。
