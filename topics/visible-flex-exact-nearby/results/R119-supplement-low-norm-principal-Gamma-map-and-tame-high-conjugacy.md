# R119 续篇：低阶小球中的真实第一 Γ 值图与高阶 tame 共轭

2026-11-15，visible-exact / tail_connector。

**状态：解析证明，低阶入口、完整 dyadic 共轭和高阶实角 tame 常数已逐段核对。** 本篇保原 fixed-stop simple-root
对象、完整指标、第二参数、实际 metric bumps、目标旋转、
两 mean 和真实高度。它关闭一个此前确实不同的量词：
第一 $\Gamma$ 的值图只需一个低阶物理状态小球，
较高角范数可以仅有限。高共轭是同一个由低门构造的真共轭，
不是为每个高阶 norm 另选一个解。

本篇不以此删除全网络背景条件，也不把高阶有限性称为角解析。
受控 residual 的径向 jets、第二 scalar 相位、全网络 tame inverse
及 nonlinear smoothing 仍须各按其实际方程继续支付。

## 1. 同一物理对象上的低阶开放域

采用
[有限角 principal 与第一参数](R119-supplement-finite-Sobolev-principal-KAM-and-true-first-metric-counterterm.md)
P.1--P.16、
[完整 mean/height 图](R119-supplement-finite-Sobolev-nonlinear-holonomy-charge-and-height-chart.md)
M.1--M.18，以及
[低方向第一 Γ](R119-supplement-low-direction-first-Gamma-projected-metric-source-and-linear-Schur.md)
G.1--G.10 的原定义。所有 $i=(j,k)$ 和外行 $o=(129,2)$
仍在原 $\mathcal I_+$ 中，第二参数固定为原给定完整变量；
不能把外行替换为一个新的自由 rotation。

在同一参考 $w_0$ 和固定物理 $t,\theta$ 上，对非mean高度 $u_\perp$
记四态
$$
 Z_0(u)=
 \left(\frac{u_\theta}{a_{\rm ph}w_0},
       \frac{u_t}{a_{\rm ph}w_0},
       \partial_\theta\frac{u_\theta}{a_{\rm ph}w_0},
       \partial_\theta\frac{u_t}{a_{\rm ph}w_0}\right).
$$
对每个有限整数 $s\ge2$，定义
$$
 \mathcal D_s(u)=\max\left\{
    \sup_{j\ge129}C_j^{-1}\sup_{I_j}\|Z_0(u)\|_{H^s},
    \quad2^{440}\sup_{\mathrm{cut128}\to e_0}\|Z_0(u)\|_{H^s}
                         \right\}.
 \tag{L.1}
$$
依然要求来自真实分片 $C_t^1$ 高度，保所有原一阶 traces
和运动学。$\mathcal D_s$ 不含独立高度常数，也不把独立
holonomy 荷当作零 Fourier mode 删除。

新的开放域只取
$$
 \epsilon=\mathcal D_{20}(u)<2^{-2097152}.
 \tag{L.2}
$$
对于高阶结论，可以另给 $\mathcal D_r(u)<\infty$，
$20\le r\le8196$；这个高 norm 不要求小于 (L.2) 的半径。
指标 $\mu_j,\zeta_j,h_j,C_j$ 均不变。

对每个 $\|p\|_{\mathcal P}\le1/4$，仍用 P.3--P.4 的真实曲线
$w_p=w_0e^{\Psi_p}$。所有非mean四态准确乘 $e^{-\Psi_p}$，
没有改变物理角。用 M.9 的同一个唯一根补
$$
 \Phi_{w_p^2}(P,K_\perp+\kappa)=0,
 \qquad
 H_0(t)=\lambda+\int_{t_f}^{t}a_{\rm ph}w_p(1+\kappa)\,ds .
 \tag{L.3}
$$
M.4 的 $\sup C_j<2^{-12}$、P 的有限 connector 小门和 (L.2)
使全部 $D,J,B$ 分母保持原余量。
高阶范数很大也不改变这些低阶点值门。
$\lambda$ 和积分的真实外端值仍独立保留。

## 2. 一个由低门构造、由高 norm 估计的圆周共轭

固定 P.2 的目标与
$|e^{in\omega}-1|\ge\gamma/|n|$，$0<\gamma\le1$。
设实周期 $u\in H^{16}$，且
$$
 \epsilon_{16}=\|u\|_{H^{16}}
                         \le2^{-524288}\gamma^2 .
 \tag{L.4}
$$
则 P.17--P.26 的 dyadic 过程给唯一反项 $\tau(u)$ 和
归一化 $C^{12}$ 共轭 $h$，满足
$$
 (x+\omega+u+\tau(u))\circ h=h\circ T_\omega,\qquad
 \langle h-\mathrm{id}\rangle=0,\quad |h'-1|<1/8.
 \tag{L.5}
$$
如果同一 $u$ 还属于 $H^s$，$16\le s\le8192$，
不论 $\epsilon_s=\|u\|_{H^s}$ 大小，都有
$$
 \boxed{\quad
 \|h-\mathrm{id}\|_{C^{s-4}}
             \le2^{262144}\gamma^{-1}\epsilon_s .
 \quad}                                                   \tag{L.6}
$$
低阶界仍为
$\|h-\mathrm{id}\|_{C^1}\le2^{64}\gamma^{-1}\epsilon_{16}$。
同一解析构造始终保持低复一导门；不能将 (L.6) 的粗高界
反灌进这个小量条件。

证明如下。取 P 的 $N_n=2^n$、$u_n=P_{\le N_n}u$ 和
$w_n=(128N_n)^{-1}$。新频带造成的同一实际误差同时满足
$$
 \varepsilon_n\le4\epsilon_{16}N_{n-1}^{1/2-16},
 \qquad
 \varepsilon_n\le4\epsilon_sN_{n-1}^{1/2-s}.
 \tag{L.7}
$$
第一个上界支付 P.20 的
$2^{-80}\gamma^2w_{n-1}^6$、新 $f_n''$、
全部复一导增量和 Taylor 路径域。
它足以定义整个无限构造，所以这里没有使用 $\epsilon_s$ 小。

对这个已经合法的同一解析子迭代，P.21 的校正界是关于
初误差的真实线性上界。以 (L.7) 的第二项代入其 Cauchy 估计，
$$
 \|h_n-h_{n-1}\|_{C^k}
 \le2^{37+22k}\gamma^{-1}\epsilon_s
                      N_{n-1}^{k+5/2-s},
            \qquad0\le k\le s-4.
 \tag{L.8}
$$
指数至多 $-3/2$，完整 dyadic 和即给 (L.6)。
这里没有因为高界可能大于解析门而重新运行解析迭代；
实际误差已由第一项满足门，两条上界同时属于同一个残差。

唯一性仍是 P 的 irrational lift 次序和共轭交换论证。
所以不同高阶 $s$ 给出的极限全部是 (L.5) 的同一个 $h$。
同样，P.27--P.31 的真实微分论证只使用低六导和 $H^6$ 方向：
$\tau$ 在 (L.4) 的严格 $H^{16}$ 球上是 $C^1$，
$$
 D\tau(u)[v]=-
 \frac{\langle v(h)/(h'\circ T_\omega)\rangle}
      {\langle1/(h'\circ T_\omega)\rangle},
 \qquad |D\tau(u)[v]|\le\|v\|_{C^0},
 \tag{L.9}
$$
并有原 $2^{64}\gamma^{-1}\|v\|_{H^6}\|v\|_{C^0}$
Fréchet 余项。此式里的方向、平均和共轭都属于同一个实物理变量。

## 3. 真实 return 的低阶入口不需要最高阶小量

完整 principal 流仍为 P.9--P.11：
$$
 (F_\sigma)_t=-d(t,F_\sigma)-\sigma\sqrt Q(t)v(t,F_\sigma),
 \qquad \mathcal R_i=F_-^{-1}\circ F_+ .
 \tag{L.10}
$$
该式对非解背景成立；不使用 $K_t=F$。
两个根的可积平方根、两真实 mean 和外行都仍在其中。
先移出准确径向平移，标准角 $x=4\theta$ 给
$\mathcal R_i(x)=x+\omega_i+p_i+f_i(p,u,x)$。

令
$$
 C_j^{\rm P}=C_j+\mathbf1_{j\ge130}C_{j-1},\qquad
 E_i^\ell=2^{4096}(j+5)C_j^{\rm P},\quad
 E_o^\ell=2^{4096}.
 \tag{L.11}
$$
这里的两项和不是 G 源预算中的完整六邻胞 $C_j^\#$。
按照 P 的实 ODE 及 G.3--G.5 的低阶收费，在 (L.2) 上有
$$
 \|f_i\|_{H^{16}}\le E_i^\ell\epsilon,\qquad
 \|D_pf_i[\dot p]\|_{H^{16}}
                    \le E_i^\ell\epsilon\|\dot p\|_{\mathcal P},
$$
$$
 \|D_uf_i[v]\|_{H^{16}}\le E_i^\ell\mathcal D_{20}(v),\qquad
 \|D_u^2f_i[v,w]\|_{H^{16}}
                    \le(E_i^\ell)^2\mathcal D_{20}(v)\mathcal D_{20}(w).
 \tag{L.12}
$$
mixed $p,u$ 和两次 $p$ 变分沿 P.13 的同一实积分支付。

为说明这不是对 G 的低方向 $C^1$ 窗作无偿升阶：
这里的方向确实给 $\mathcal D_{20}$。
P.14 在 $s=16$ 的 reciprocal/mean 费为768 bits，
$C^{16}$ composition 为338 bits，二次变分需背景/方向到
18角导，20阶输入足够；双乘积16 bits、
完整真实径向积分、邻胞132 bits和四倍角仍在4096之内。
只在下文另读 $\mathcal D_8$ 方向时，才回到 G 的
一次 $C^1$ / mixed $C^0$ 低窗。

P/O 的原算术和完整外行预算准确给
$$
 B_\ell=\sup_i E_i^\ell/(\gamma_i^{\rm D})^2<2^{4416}.
 \tag{L.13}
$$
(L.2) 因而使每一行同时满足 (L.4)：
$E_i^\ell\epsilon/(\gamma_i^{\rm D})^2
 <2^{-2092736}<2^{-524288}$。
深层目标的小除数不会使某一行逃出低门。

## 4. 真正低阶开放域中的无限第一参数值图

定义同一个
$\mathfrak T_i(p,u)=\tau_i(f_i(p,u))$。
由 (L.9)、(L.12)--(L.13)，
$$
 \|\mathfrak T(p,u)\|_{\mathcal P}\le B_\ell\epsilon,\qquad
 \|D_p\mathfrak T\|_{\mathcal P\to\mathcal P}
                                  \le B_\ell\epsilon<1/2 .
 \tag{L.14}
$$
因此原完整 weighted $\ell^\infty$ 盘上存在唯一
$p^*(u)=\mathfrak T(p^*(u),u)$。真实 metric 第一参数仍由
P.3 的曲线读出，不另添一个自由常角。

P.30 的统一余项与 (L.12) 的二次 ODE 费给
$2^{65}B_\ell^2\mathcal D_{20}(v)^2$ 的完整参数余项；
所有交叉参数行先取真正 operator norm，再求固定点。
故这是一个真实
$$
             p^*:\{\mathcal D_{20}<2^{-2097152}\}
                         \longrightarrow\mathcal P
             \quad\hbox{的 }C^1\hbox{ 值图}.
 \tag{L.15}
$$
没有依赖全层 uniform norm 中错误的 Fourier 稠密性。

在径向点，M 的完整 mean 小根使 P.36 的两个速度变分平均
都为0。沿真实径向旋转搬运后
$\langle D_uf_i|_0[v]\rangle=0$。
用 (L.9) 的低共轭正权误差及 G.4 的 mixed 低窗，
现在可在整个 (L.15) 开放域直接定义 G.6 的
$\mathcal D_8$ 有界切向 functional；在真实
$\mathcal D_{20}$ 方向上它就是 (L.15) 的导数。
原完整 inverse $(I-D_p\mathfrak T)^{-1}$ 仍小于2，得到
$$
 \|Dp^*[v]\|_{\mathcal P}\le2^{8960}\epsilon\mathcal D_8(v),
 \qquad
 |Dp_i^*[v]|\le2^{4512}E_i^\ell\epsilon\mathcal D_8(v).
 \tag{L.16}
$$
这不宣称值图已定义在 $\mathcal D_8$ 开球。

乘实际 P.3 metric 曲线导数，所有真实行满足
$$
 |D\gamma_{1,i}^*[v]|
 \le2^{8960}(j+5)^2\delta_j^{-1}C_j^\#
                       \epsilon\mathcal D_8(v)\quad(i\ne o),
$$
$$
 |D\gamma_{1,o}^*[v]|
              \le2^{8960}\epsilon\mathcal D_8(v).
 \tag{L.17}
$$
沿 $\lambda u$ 积分给同 profile 的二次值界。
该路径始终处于 (L.2)；无须最高阶 norm 很小。
第二参数、形状、$\nu$ 和给定外方向并不由此删除。

## 5. 实角 tame composition 的有限常数

为支付真正高阶 return，下面给一个只用低 Lipschitz 门的
完整实角估计。它不把高 norm 小写进隐含条件。

在标准圆上，对 $1\le j\le r\le8196$，
$$
 \|D^jz\|_{L^{2r/j}}
 \le2^{32j}(r+1)^{2j}\|z\|_\infty^{1-j/r}
             \bigl(\|D^rz\|_2+\|z\|_\infty\bigr)^{j/r}.
 \tag{L.18}
$$
$j=r$ 是直接不等式。下面说明 $1\le j<r$ 的常数来源。
取偶的频率 cutoff，在 $[1,2]$ 用
$1-10s^3+15s^4-6s^5$，$s=\xi-1$，连接1与0；
其前两导在两端匹配，二阶导绝对值小于 $2^9$。
两次 Fourier 分部给低频 $D^j$ kernel 的
$L^1$/递减包络费用不超过
$2^{j+16}(j+1)^2R^j$。
对高频用 $D^{j-r}D^rz$ 并逐 dyadic 环带作同样两次分部，
费用不超过
$2^{r-j+16}(r-j+1)^2R^{j-r}\mathcal M(D^rz)$。
这里 $\mathcal M$ 是圆周 Hardy--Littlewood maximal function；
周期化的 $(1+R^2x^2)^{-1}$ 包络直接受它控制。
区间覆盖给 weak $(1,1)$ 常数3，再对截断层积分给
$\|\mathcal Mz\|_2<16\|z\|_2$。

令 $R$ 为不小于1的 dyadic 数，将低项与高项平衡，
并在高项加入 $\|z\|_\infty$ 以覆盖最优 $R<1$ 的情形。
dyadic 舍入只多 $2^j$。
将所得点值估计取 $L^{2r/j}$，上述 maximal 门和
$j\ge1$ 给 (L.18)；所显示的 $2^{32j}(r+1)^{2j}$
还保留充足固定余量。复值函数用分量及模长处理，再至多乘2。
没有把一个高阶常数按因子个数反复乘 $r$ 次。

具体地，令 $F=x+\alpha+\eta$，$|\eta'|\le1/4$。
对 $k\ge2$ 展开
$$
 D^k(a\circ F)=
   \sum_{p=1}^k(a^{(p)}\circ F)
             B_{k,p}(F',F'',\ldots).
$$
给 $a'$ 的导阶 $p-1$，给每个高于一阶的 $F$ 因子
$\eta'$ 的导阶 $\alpha_\ell-1$，总和准确为 $k-1$。
在 (L.18) 取 $r=k-1$，Hölder 各指数的倒数之和是 $1/2$。
这些插值 exponent 的和为1；Young 只产生
$\|a\|_{H^k}$ 或 $\|a\|_{H^2}\|\eta\|_{H^k}$，
不产生两个最高 norm 的乘积。
Jacobian 读出小于2，$F'$ 因子最多给 $2^k$。

所有 GN 常数的乘积为
$2^{32(k-1)}k^{2(k-1)}$，不是其 $k$ 次方。
Faà 的非负整数系数总和小于 $k^k$，
Bessel norm 的完整二项式和及各低导再付 $2^{2k+10}$。
因 $k\le8192$，这些费用严格被
$$
 \boxed{\quad
 \|a\circ F\|_{H^k}
 \le2^{90(k+4)}
        \{\|a\|_{H^k}+\|a\|_{H^2}\|\eta\|_{H^k}\}.
 \quad}                                                   \tag{L.19}
$$
覆盖。$k=0,1$ 由 change of variables 和一阶链式直接处理。
可先对光滑函数证明，再在单个真实圆上逼近；
不需要全层最高 norm 的强稠密性。

## 6. 高阶实际 ODE 只需一次 Gronwall

对 P 的完整实路径，先准确移出径向标量平移。
非径向速度 $a(t,x)$ 是 $-d$ 与
$-\sigma\sqrt Q(v-1)$ 的实际有序组合。
反向负支按时间反向作为同一条分段 ODE 的后半段；
不先把两个粗 inverse-map norm 相乘。

M 的 mean 根和 P.14 的完整 reciprocal 级数给，对于
$k+4\le8196$，
$$
 \int\|a(t)\|_{H^k}\,dt
 \le2^{32(k+8)+256}
       \begin{cases}
        (j+5)C_j^{\rm P}\mathcal D_{k+4}(u),&i\ne o,\\
        \mathcal D_{k+4}(u),&i=o .
       \end{cases}
 \tag{L.20}
$$
只在一个真实因子上放最高角阶：
$\|z^n\|_{H^k}\le n^k(2\|z\|_{H^1})^{n-1}\|z\|_{H^k}$。
级数的低 norm 由 (L.2) 支付，因而高 norm 可以仅有限。
径向积分仍为内部 $32(j+4)$、外行 $2^9$；
实际六邻胞与两项 $C^{\rm P}$ 的比较132 bits在256内。
当前 $p^*$ 只改变径向量，所有式子对原 $p$ 盘统一。

设位移为 $g$。低 ODE 门已给 $|g'|<1/4$。
(L.19) 在每个真实 $t$ 给
$$
 \frac d{dt}\|g\|_{H^k}
 \le2^{90(k+4)}
       \{\|a\|_{H^k}+\|a\|_{H^2}\|g\|_{H^k}\}.
 \tag{L.21}
$$
这是范数积分不等式，亦可直接用 Duhamel 写出；
不假设未知范数处处可微。
由 (L.11)--(L.13)，
$\int\|a\|_{H^2}\le2^{4416}\epsilon$。
即使 $k=8192$，(L.2) 仍使
$2^{90(k+4)+4416}\epsilon<1/8$。
所以同一 Gronwall 因子小于2；不以高 $\mathcal D_{k+4}$ 来支付它。

(L.20)--(L.21)、真实四倍角及完整 Sobolev norm 读出合计小于
$124(k+8)+4096<1048576$ bits。因此得到
$$
 \boxed{\quad
 \|f_i(p,u)\|_{H^{r-4}}
 \le2^{1048576}
       \begin{cases}
        (j+5)C_j^{\rm P}\mathcal D_r(u),&i\ne o,\\
        \mathcal D_r(u),&i=o ,
       \end{cases}
 \quad20\le r\le8196 .
 \quad}                                                   \tag{L.22}
$$
其中高范数完全未要求小于任何固定门。
此处只给所需的实际值 map tame 界；
未把高阶参数微分自动归入相同常数。

## 7. 同一个 principal 共轭的高阶 tame 结论

先由低 (L.12) 和 (L.4) 构造实际 $p^*$ 与 $h_i$，
随后将 (L.22) 代入同一个共轭的 (L.6)。
得到
$$
 \boxed{\quad
 \|h_i-\mathrm{id}\|_{C^{r-8}}
 \le2^{1310720}(\gamma_i^{\rm D})^{-1}
       \begin{cases}
        (j+5)C_j^{\rm P}\mathcal D_r(u),&i\ne o,\\
        \mathcal D_r(u),&i=o ,
       \end{cases}
 \quad20\le r\le8196 .
 \quad}                                                   \tag{L.23}
$$
低 $C^1$ 门仍由 (L.2) 的同一个小量给出。
高常数不会被重新用作该低门，也不会把一个
$C^{r-8}$ 的很大上界误称为 Jacobian 很大。

在旧 P.5 高小球与新 (L.2) 的交集上，真实 flows、metric 方程
和目标完全相同；原唯一反项和归一共轭的唯一性使新旧图准确一致。
本篇因此是同一对象的量词扩张，不是新造一套代用 $\Gamma$。

第一参数及其物理导数均按 (L.16)--(L.17) 的低因子收费。
高阶 source 若另消费 G 的 projected metric 公式，
仍必须用实际高背景 norm 和真实径向 residual；
本篇不将 G 的2114阶源窗或完整 Schur 常数自动扩大。

## 8. 真 mean、height 与后继 inverse 的范围

(L.3) 中 $q=w_p^2$ 会随第一参数变化。
其准确微分仍为
$$
 \dot\kappa=
 \frac{\psi D_{(P,K_\perp)}\Phi[P,K_\perp]
                          -2q\psi\,\partial_q\Phi}
      {\langle A_0\rangle},
 \qquad
 (H_p)_t=a_{\rm ph}w_p\{\psi(1+\kappa)+\dot\kappa\}.
 \tag{L.24}
$$
完整 $2q\psi\partial_q\Phi$、有向 height 积分、两端常数和 mean flux
都保留；不能在每个胞元重新设置积分常数。
带独立 holonomy 荷 $\chi\ne0$ 的一般方向仍是另一值域。
(L.15) 是 holonomy-one 子图上的真实第一参数，
不会由一个 projected 线性解自动延拓至任意 charged 值图。

本篇关闭的实际门是：低物理 $\mathcal D_{20}$ 开球中的
无限第一参数值图、同一个真共轭、明确一次高范数的
实际 flow 与 conjugacy tame 界，以及原低方向 functional
对真实低值图切向的识别。它允许在后继证明中分开
“低 norm 保持很小”和“高 norm 仅有限”的要求。

它不单独授权把旧附近全网络 inverse 的所有高小门删掉。
下一步仍须对真实余网络、高部、深低首迹、外 DN/Poisson
及完整 sources 给同样的两层估计，并支付可保持的
径向 residual-jet 域。第二 scalar 相位与 finite good 参数、
真实帽/外部行和 $\nu$ 保原实际列。
在这些量词与具体 smoothing 递推闭合前，不能仅凭 (L.23)
宣称已得到 nonlinear 存在性或原 analytic224 标签。
