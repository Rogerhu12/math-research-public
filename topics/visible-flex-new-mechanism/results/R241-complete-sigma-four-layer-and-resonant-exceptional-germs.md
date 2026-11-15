# R241：完整 h²σ⁴ 层、真实循环缺陷与一个共振端芽消去

日期：2026-11-15。完整纸面推导；没有执行新的 profile 积分、符号目标、参数求根或几何计算。

本稿继续 [R237](R237-complete-next-mixed-layer-after-exceptional-leading-cancellation.md)。在 R231、R237 的四个能量门已经支付后，确定整个第四 ruling 的 $h^2\sigma^4$ 层，再证明 [R239](R239-nonseparable-third-order-circles-paying-four-exceptional-energy-gates.md) 的新圆可在一个明确的共振参数下同时消掉这一层。循环身份只用于真正紧槽；非紧的 $\mathcal G(f,f)$ 与 $\mathcal D(f,f)$ 的实际左尾全程保留。

来源：[R56](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R227](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)、[R229](R229-p2-energy-boundary-identity-for-exceptional-germs.md)、[R231](R231-complete-mixed-leading-gate-for-the-exceptional-even-port.md)、R237、[R238](R238-scalar-reduction-of-the-next-two-energies-for-complete-blocks.md)及 R239。

## 1. 原约定与结论

固定 $b=0$ 例外 germ

$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=k_e(1-2\varepsilon\sigma^2),\qquad
\omega=k_e/h,
\quad \varepsilon>0, h_e>0, k_e\ne0.
\tag{1}
$$

I 是同一个正活动区间，且 $x+k_e/h_e>0$。取同锚三矩圆 $(f,g)$，置

$$
\phi=\cos\theta f+\sin\theta g,\qquad D_\theta=f^2-\phi^2,
$$

$$
\mathcal G=-\Phi_{p_2}/2,\qquad
\mathcal D=\Phi_{p_1}-\Phi_{t_1}/8,\qquad
\mathcal T=\Phi_{t_1},\qquad A_f=\mathcal G(f,f).
\tag{2}
$$

所有二次槽均按对称双线性解释。能量为

$$
E(U,V)=\frac14\int_I(x^2U''V''+2U'V'),\qquad
E_1(U,V)=\frac12\int_Ix U''V''.
\tag{3}
$$

假设 R231 的 $L_c=L_s=0$ 和 R237 的 $M_c=M_s=0$ 都已成立。后一个条件等价于

$$
E(A_f,\mathcal D D_\theta)=0\quad\text{对全部 }\theta.
\tag{4}
$$

对普通 profile u 记 $r_u=(u/x)''$。若 B 是二次槽，记
$\mathcal R(u,v)=r_ur_v$ 并按线性扩展定义 $\mathcal R(B)$。只对三矩为零的 B 定义本稿所需的线性泛函

$$
\begin{aligned}
\Lambda_f(B)={}&4E\{\mathcal D(f,f),\mathcal G B\}
-2E_1(A_f,\mathcal G B)
-\frac18\int_Ix^7r_{A_f}\,\mathcal R(B)\\
&-\eta_*E(A_f,\mathcal T B),
\qquad \eta_*:=\frac{1+2\varepsilon/k_e^2}{6}>\frac16.
\end{aligned}
\tag{5}
$$

这里 $\eta_*$ 是一个常数，不是 R56 的局部恢复系数。B 的零三矩保证 $\mathcal G B,\mathcal D B,\mathcal T B$ 都是真正紧槽；第一能量中的 $\mathcal D(f,f)$ 和其余的 $A_f$ 可以有左尾。

**完整层定理。** R224/R231 的中心化完整 ruling 满足

$$
\boxed{
\lim_{\sigma\to+\infty}
\frac{\widehat{\mathscr K}_\theta}{h^2\sigma^4}
=\varepsilon k_e^3\Lambda_f(D_\theta).
}
\tag{6}
$$

因此全部第四 ruling 可解还必须有

$$
\boxed{
N_c:=\Lambda_f(g^2-f^2)=0,\qquad
N_s:=\Lambda_f(fg)=0.
}
\tag{7}
$$

本稿后半证明：对于 R239 的完整 block 及其不可分离双 block 合成，若另取

$$
\boxed{\varepsilon=k_e^2/4,}
\tag{8}
$$

则 (7) 也准确成立。这仍不等于整个第四 ruling 或 period 可解。

## 2. 第三 history 余项的准确首系数

沿用 R237 的

$$
\beta=\int_0^\sigma hk,\qquad O=\beta\mathcal G+C,\qquad
c_5=4\varepsilon^2k_e^2/5.
$$

其完整式为

$$
C=c_5\sigma^5\mathcal D+\sigma^3\mathcal C_3+O(\sigma),
$$

$$
\mathcal C_3=-\frac{2\varepsilon k_e^2}{3}\Phi_{p_1}
-\frac{\varepsilon^2}{6}\mathcal T
=-\frac{2\varepsilon k_e^2}{3}\mathcal D
-\frac{\varepsilon(k_e^2+2\varepsilon)}{12}\mathcal T.
\tag{9}
$$

最后的 O 项包含真实负 h 层的有限极限，没有重置。由 $\beta=2k_e\int_0^\sigma h-k_e\sigma h$，

$$
\beta=-k_e h\sigma+O(h/\sigma).
\tag{10}
$$

置

$$
A=\mathcal G D_\theta,\qquad B=\mathcal D D_\theta,\qquad
\tau_\theta=\mathcal D(\phi,A)-\mathcal G(\phi,B).
\tag{11}
$$

这些 A、B 紧；$\tau_\theta$ 保留两个不同嵌套次序，不先称其为零。R237 准确写

$$
W_3=\beta^2\mathcal G(\phi,A)
+2\beta\mathcal G(\phi,C D_\theta)+V,
$$

$$
V'=2\beta\{r_0(\phi,A)-\mathcal G(\phi,r_0D_\theta)\}
+2r_0(\phi,C D_\theta)-2\ell
+2\Psi(\phi,r_\sigma D_\theta),\qquad r_0=C'.
\tag{12}
$$

代入 $r_0=5c_5\sigma^4\mathcal D+O(\sigma^2)$、(10)，并使用 R237 已付的
$\ell,\Psi=hO(\sigma^3)+\operatorname{poly}$，得

$$
V'=-10k_ec_5 h\sigma^5\tau_\theta
+hO(\sigma^3)+\operatorname{poly}.
\tag{13}
$$

其中 $r_0 C$ 只为多项式增长，真实负 h 部分与 $\beta$ 的乘积也已保在该余项中。准确积分关系

$$
\int_0^\sigma h\tau^5\,d\tau
=\frac{h\sigma^4}{2\varepsilon}+O(h\sigma^2)
$$

因而给

$$
\boxed{
V=-4\varepsilon k_e^3 h\sigma^4\tau_\theta
+hO(\sigma^2)+\operatorname{poly}.
}
\tag{14}
$$

这是原中心初值下的真实积分，不用形式流代替 history。

## 3. 完整 h²σ⁴ 层的三个来源

R237 的 $h\beta^2$ 项由两个领先门准确消失。交叉项仍准确是

$$
-2h\beta E(A_f,C D_\theta).
$$

由 (4)，其中整个 $c_5\sigma^5\mathcal D$ 部分为零，连同 $\beta$ 的所有低阶展开一起消掉。故它在本次尺度下贡献

$$
2k_e E(A_f,\mathcal C_3D_\theta).
\tag{15}
$$

第二来源是 (14) 在 $2hE(\phi,V)$ 中的贡献

$$
-8\varepsilon k_e^3 E(\phi,\tau_\theta).
\tag{16}
$$

第三来源不能遗漏：原第一场能量为

$$
\mathcal E_\sigma=hE+jE_1+
\frac{1+j^2}{4h}\int_Iu''v'',\qquad j=2\varepsilon k_e\sigma^2.
$$

$j\beta^2/(h^2\sigma^4)\to2\varepsilon k_e^3$，所以其完整主项是

$$
2\varepsilon k_e^3J_\theta,\qquad
J_\theta=-E_1(A,A)+2E_1\{\phi,\mathcal G(\phi,A)\}.
\tag{17}
$$

所有其他来源都严格低阶：

- R237 的全部第三局部恢复及第二局部交叉至多 $h^2O(\sigma^2)+h\operatorname{poly}+\operatorname{poly}$；
- (14) 的余 history 经第一场配对后仍只到 $h^2O(\sigma^2)$；
- $j$ 层的 C 交叉以及最后 $h^{-1}(1+j^2)$ 层只为 $h\operatorname{poly}+\operatorname{poly}$；
- C 的线性余项在 (15) 之前只给 $h^2O(\sigma^2)$。

因此完整原 ruling 的极限已经确定为

$$
\boxed{
2k_e E(A_f,\mathcal C_3D_\theta)
-8\varepsilon k_e^3E(\phi,\tau_\theta)
+2\varepsilon k_e^3J_\theta.
}
\tag{18}
$$

这里没有把 $E_1$ 当作 E 的零循环能量；下面给出它的真实缺陷。

## 4. 两个准确循环缺陷

对三个紧 profile u、v、w，记

$$
\mathcal J_7(u,v,w)=\int_Ix^7r_ur_vr_w.
$$

则

$$
\boxed{
\sum_{\rm cyc}E_1\{u,\mathcal G(v,w)\}
=-\frac18\mathcal J_7(u,v,w),
}
$$

$$
\boxed{
\sum_{\rm cyc}E\{u,\mathcal D(v,w)\}
=-\frac3{32}\mathcal J_7(u,v,w).
}
\tag{19}
$$

**证明。** 只需核对对角，再作普通实多项式极化。令 $q=xy$、$r=y''$、$m=y-xy'$，则 $m'=-xr$。R229/R238 给

$$
r_{\mathcal G(q,q)}=-\frac{x^4r(3r+xr')}{4},
$$

$$
r_{\mathcal D(q,q)}
=2x^3r^2+\frac34x^4rr'-\frac34xmr-\frac14x^2mr'.
\tag{20}
$$

原边界式为

$$
E_1(U,V)=\frac12\int_Ix^3r_Ur_V
+[x^2(U/x)'(V/x)']_\ell^r.
\tag{21}
$$

当第一个输入 q 紧时，(21) 和 R229 的 E 边界项均为零，即使第二输入 $\mathcal G(q,q)$ 或 $\mathcal D(q,q)$ 有左尾。于是

$$
E_1\{q,\mathcal G(q,q)\}
=-\frac18\int_Ix^7r^2(3r+xr')
=-\frac1{24}\int_Ix^7r^3,
$$

$$
E\{q,\mathcal D(q,q)\}
=\frac14\int_Ix^4r\,r_{\mathcal D(q,q)}
=-\frac1{32}\int_Ix^7r^3.
\tag{22}
$$

第二式中 $x^8r^2r'$ 消掉 $x^7r^3$ 的前两项，$x^6mrr'$ 用 $m'=-xr$ 积分后只余所示系数。全部端项由 q 的紧 collar 支付。极化得 (19)。

还需要一个准确的自项恒等式：

$$
\boxed{\mathcal J_7(q,q,\mathcal G(q,q))=0.}
\tag{23}
$$

它直接来自
$-\frac14\int(3x^{11}r^4+x^{12}r^3r')=0$。
该式的证明只用 q 紧；不要求 $\mathcal G(q,q)$ 自身紧。

## 5. 两个谐波与非紧背景尾

现在只在 (19) 中放入真正紧的 $\phi,A,B$。R229 的原 E、$\mathcal G$ 零循环也只用于这些紧输入。设

$$
I_\theta=\mathcal J_7(\phi,\phi,A).
$$

准确得到

$$
J_\theta=-E_1(A_f,A)-I_\theta/8,
$$

$$
E(\phi,\tau_\theta)
=-E\{\mathcal D(f,f),A\}/2
+E(A_f,B)/2-3I_\theta/64.
\tag{24}
$$

因此 (16)、(17) 合为

$$
\varepsilon k_e^3\left[
4E\{\mathcal D(f,f),A\}-4E(A_f,B)
-2E_1(A_f,A)+I_\theta/8\right].
\tag{25}
$$

其中 $E(A_f,B)=0$ 正是已付的 (4)。再由 (23)，

$$
I_\theta=\int_Ix^7r_\phi^2r_{A_f}
=-\int_Ix^7(r_f^2-r_\phi^2)r_{A_f}.
\tag{26}
$$

这一步没有把 $A_f$ 放进未经支付的紧槽循环；它只用两次已证的局部自项 (23)。

最后 (9)、(4) 使 (15) 等于

$$
-\frac{\varepsilon k_e(k_e^2+2\varepsilon)}6
E(A_f,\mathcal T D_\theta).
\tag{27}
$$

合并 (25)–(27) 得 (5)、(6)。由于

$$
D_\theta=-\sin^2\theta(g^2-f^2)-\sin2\theta\,fg,
$$

完整本层仍只有两个谐波，(7) 是其准确零条件。

R224/R237 的真实偶 gauge 商仍为
$\operatorname{span}\{h,\sigma^2,(1+4\varepsilon^2k_e^2\sigma^4)/h\}$。
其所有函数除以 $h^2\sigma^4$ 都趋零。由同一正支上的解析延续，任一 (7) 非零会排除 germ 中的完整 ruling membership。所有传入 histories 已由该原比较处理，没有重锚或删前缀。

## 6. 一个新的准确 bulk 恒等式

对紧微包 u，沿用 R238 的 $\mathfrak T(u)$，再定义

$$
S_1(u)=\frac12\int_Ix^3r_{\mathcal G(u,u)}^2,\qquad
U_T(u)=\frac14\int_Ix^4r_{\mathcal G(u,u)}r_{\mathcal T(u,u)}.
\tag{28}
$$

它们仍是 bulk，不冒带尾场的单独真实自能量。令 $r=(u/x)''$、$m=u/x-x(u/x)'$、$a=3r+xr'$。除 (20) 外，直接微分原 $\mathcal T$ 给

$$
r_{\mathcal T(u,u)}=2x(m-x^2r)a.
\tag{29}
$$

置 $I_0=\int x^{11}r^2a^2$、$I_1=\int x^9mra^2$。由于
$\int x^{11}r^3a=0$ 是完整总导数，逐项有

$$
S_1=I_0/32,\qquad
\mathfrak T=(I_1-3I_0)/64,\qquad
U_T=(I_0-I_1)/8.
$$

因此

$$
\boxed{U_T=-8(\mathfrak T+S_1).}
\tag{30}
$$

这里没有使用 $\mathfrak T$ 的符号，也没有执行新的积分。

## 7. R239 的完整 block 在共振参数下消掉本层

取 R238/R239 旋转前的完整三矩 block

$$
f_0=\sum_i a_i u_i,\qquad
g_0=\sum_i s_i a_i u_i,\quad s_i=\pm1,
$$

各微包不交。已选角满足 $t=\sin2\alpha=-P/Q$，且 R239 准确支付

$$
Z=\sum_i a_i^4(s_i+t)\mathfrak T(u_i)=0.
\tag{31}
$$

令 $f_\alpha=\cos\alpha f_0+\sin\alpha g_0$。在第 i 个微包，第一 profile 的平方幅度因子为 $1+ts_i$。

对本稿 $\Lambda_{f_\alpha}$ 的全部项，完整总体边界在三矩交叉槽 $f_0g_0$ 中为零；(21) 同样保留后再消去。不同微包的共轭二阶导数支撑不交。局部 $\mathcal J_7$ 对每个自微包由 (23) 为零。因此

$$
\Lambda_{f_\alpha}(f_0g_0)
=\sum_i a_i^4(s_i+t)
[4\mathfrak T(u_i)-2S_1(u_i)-\eta_*U_T(u_i)].
\tag{32}
$$

用 (30)，并记 $Z_1=\sum_i a_i^4(s_i+t)S_1(u_i)$，得到

$$
\boxed{\Lambda_{f_\alpha}(f_0g_0)
=(4+8\eta_*)Z+(8\eta_*-2)Z_1.}
\tag{33}
$$

所有二次原算子和局部 $r\otimes r$ 对 $f_0^2$、$g_0^2$ 的像相等。因此旋转后的两目标槽在 (5) 中给

$$
N_c=-2t\,\Lambda_{f_\alpha}(f_0g_0),\qquad
N_s=\cos2\alpha\,\Lambda_{f_\alpha}(f_0g_0).
\tag{34}
$$

这里不是声明抽象 $\operatorname{Sym}^2$ 中 $f_0^2=g_0^2$，只使用 (5) 已列出的真实二次映射具有相同像。

当 $\varepsilon=k_e^2/4$，有 $\eta_*=1/4$，所以 (33) 恰为 $6Z=0$。这证明 (7)，不需要知道 $Z_1$ 的值。

对 R239 最终两个完整 block 的合成，本层仍准确相加。新增的尾检查是：右方 $\mathcal D(f,f)$ 在左方为 $a x^2+b x$，而另一槽紧，故

$$
E(x^2,Z)=E(x,Z)=E_1(x^2,Z)=0
\quad\text{对双 collar 为零的 }Z.
\tag{35}
$$

其余局部共轭二阶导数在 block 外为零。故非紧背景尾不产生未计的跨 block 成本。正伸缩下 (5) 的各项都是零次；两个互补旋转的同构 block 均保持本层为零，不可分离性照 R239 保留。

## 8. 共振 germ 的真实安装与选择范围

式 (8) 本身给原水平方程的准确解析偶 germ，并保持全部端速度为零。若 $k_e$ 被预先固定，不能仅因 R227 对该固定值有一个小 $\varepsilon$ 邻域，就擅自认为 $k_e^2/4$ 已在其中。

一个可以支付的选择是把共同端值作为外参数：令 q 表示 $k_e$，规定

$$
(h,k,\omega)\big|_{\sigma=0}=(h_e,q,q/h_e).
$$

在 $(q,\varepsilon)=(0,0)$ 选定一次 R70/R227 允许的有限正则原语库及固定重复次数。R227 的三式及真实 ODE 对两个参数都光滑，不含 $1/q$ 或 $1/\varepsilon$；其原三维 frame 导块、八矩导块和 omega 末值导块在该基点不退化。将 q 同时纳入 R70 的端点外参数，frame 方程的校正导块是 $I_3$；消该块后，九约束的导块仍为 $\left(\begin{smallmatrix}D_aM&*\\0&c_\omega\end{smallmatrix}\right)$，其中 $D_aM$ 可逆、$c_\omega\ne0$ 来自固定内部辅助族，不要求 q 非零。完整有限成本坐标的原导数为 $I$（闭 hook 装配为 $4I$），故其后 IFT 也在同一基点适用。联合 IFT 因而给一个真正的二维开邻域，而非一族未经统一的逐 q 阈值。分析 $\mathcal W_e$ 时出现的 $1/(\varepsilon q)$ 不进入这些安装方程或 Jacobian。

在这个共同邻域内选足够小的 $q>0$，再令 $\varepsilon=q^2/4$，便准确落在 (8)。全部共享副本采用同一所选 germ；R227 的完整第三结构与已选有限控制目标照原真实 composition 保留。共同物理 I 在有限紧包络后选定，或者保持已有严格正余量。

若还需全域 Morse，须在所选非零 q、正 $\varepsilon$ 后使用原 masked 自由扰动与受约束横截；不声称基点 $q=0$ 已 Morse，也不声称 $h_{ss}$ 的正下界一致延至 q=0。

这段安装保留的是原先固定的有限观测。R239 重新选择 profile 圆，所以旧圆的 F8 值不能自动改称新圆的 F8 值。这里的六能量结论只用已选几何的完整低阶结构、可保留的 universal pure 控制与新圆自身的准确能量身份，不作这个观测偷换。

本段也不宣称所有未经纳入该共同参数族的其他接口都自动共振，更不宣称原完整闭几何的全部 ruling 已消失。

## 9. 剩余工作的位置

现在存在真实可选的例外端芽及不可分离的完整三阶圆，准确消掉 R231、R237、本稿三层的六个能量条件。下一 $h^2\sigma^2$ 层开始与 R237 已定位的完整局部恢复、$\ell$ 和 $\Psi$ 贡献同阶，不能再只取 history 项或重用一个领先能量猜测。

本稿没有运行或要求重跑已付四门，没有评价新圆的任何未付低层，也没有将有限多层的零升级为完整 ruling、period 或第四阶解。
