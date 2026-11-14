# R119 续篇：新真实第四尾方向、重调 connector 与不变的尾尺度参数

2026-11-13，visible-exact / tail_connector。

**状态：已证明。** 对每个已构造的实际无限参数 $\Gamma$，真实
第四尾方向仍在 $14<d_4(\Gamma)<15$，并可用同一个有限
connector 的最后 $q=-1$ 主段的唯一停止长度准确匹配。该段的
$H\omega$ 恰为不变量，因此重调后调用真实非线性尾的
$\epsilon_{\rm tail}$ **准确不变**；只发生已明确记录的整体
等比尺度变化。前篇的实际相位 KAM 因而不与这个接合产生循环。

重调后，双 bump 的第四模保持曲线也是原来的同一条曲线。
全部高模的好参数集合须对新真实尾重新选取，但同一测度下界
仍适用。因此每个最终 $\Gamma$ 都有实际全频 regular 选择，
并且同一相位轨道可以使用一个固定的完整目标度量。

本篇不声称高模好参数的最小元在任意 $\Gamma$ 邻域连续，也不
以 ray KAM 代替完整高度/flux 的强反馈逆。

## 1. 真正更新的第四模线，而不是原方向的近似代入

沿用
[统一参数尾图](R119-supplement-uniform-tail-chart-for-actual-metric-parameters.md)
的复参数盒 $\|\Gamma\|_\infty<2^{-15}$。零标签线性化的每个
角频仍独立；下面只计算第四模，但其来源是完整内部标签空间。
源 R72 的实际九段第四矩阵记为 $B_{4,j,\Gamma}$。它满足
$$
 \det B_{4,j,\Gamma}=1/64,\qquad
 \|B_{4,j,\Gamma}-B_{4,\infty}\|_\infty\le e_j,
 \quad e_j=2^{31}\sqrt{\delta_j}.
 \tag{C.1}
$$
这里实际矩阵随 $\Gamma$ 更新，行列式来自 trace-zero canonical
流和末端准确因子 $1/64$。理想矩阵为
$$
 B_{4,\infty}=
 \begin{pmatrix}-1299&325/16\\1235/64&-309/1024\end{pmatrix}.
 \tag{C.2}
$$
设其大特征值为 $-\Lambda_4$，相应斜率为
$s_4=(1299-\Lambda_4)/(325/16)$。R11 §2 的准确二次根计算给
$$
 -1/64<s_4<-7/480,
 \qquad 69<20\sqrt{12}<70.
 \tag{C.3}
$$

在复圆盘 $|s-s_4|\le1/1024$ 上，$|s|<1/32$。实际 Möbius
map
$$
 T_{j,\Gamma}(s)=
 \frac{(B_{4,j,\Gamma})_{21}+(B_{4,j,\Gamma})_{22}s}
      {(B_{4,j,\Gamma})_{11}+(B_{4,j,\Gamma})_{12}s}
$$
具有分母模长大于1298，且
$$
 |T_{j,\Gamma}'(s)|<2^{-26},\qquad
 |T_{j,\Gamma}(s_4)-s_4|<e_j/1000.
 \tag{C.4}
$$
第一式使用准确行列式；第二式在分子中保留
$\delta B_{21}+s_4\delta B_{22}-s_4(\delta B_{11}+s_4\delta B_{12})$，
其模至多 $(1+|s_4|)e_j$。这些界对整个复参数盒成立。

从任意深层 $N$ 的 $s_N=s_4$ 往外逐层传播。因为
$e_{j+1}=e_j/\sqrt2$，(C.4) 的几何和给固定浅层的完整极限
$$
 |s_{n,\Gamma}-s_4|<e_{n+1}/999,\qquad n\ge128.
 \tag{C.5}
$$
极限对整个参数盒一致；它没有保留一个未控制的有限深截断误差。
这条线确是原内部标签的真实线：在该 cone 上，规范第一分量的
向外倍率大于
$$
 2^{-39/4}e^{-4h_j}\,1298>33/32.
 \tag{C.6}
$$
这里使用 R72 的全层界 $h_j\le9/100$：$129\le j\le4096$
时恰取 $9/100$，$j\ge4097$ 时 $h_j=8\delta_j^{1/256}$
递减，且首项小于 $1/8192<9/100$。
因此向深端归一的整个状态有界并趋0。它满足同一真实递推及
同一内部标签，强 Green 的唯一性将其与 $\mathcal H_\Gamma$
给出的第四线识别。没有把有限矩阵积当成真实无限尾。

由于 $e_{129}<2^{-35}$，在 cut128 归一高度为1后，真实物理
斜率满足
$$
 d_4(\Gamma)=16+20\sqrt{12}\,s_{128,\Gamma},
$$
$$
 |d_4(\Gamma)-d_4^{\rm ideal}|<2^{-38},
 \quad d_4^{\rm ideal}=16+20\sqrt{12}s_4,
 \qquad \boxed{14<d_4(\Gamma)<15}\quad(\Gamma\text{ real}).
 \tag{C.7}
$$
这个方向与尾的整体幅度参数 $\epsilon$ 无关：其准确高度方程
只含 $w_r/w$，而 $w=\epsilon\delta_j^6p_\Gamma/r^7$ 中的
$\epsilon$ 在该比值中相消。

全纯极限及实盒距复边界的 $2^{-16}$ 余量还给
$$
 \|D_\Gamma d_4\|_{\ell^\infty\to\mathbb R}<2^{-22}.
 \tag{C.8}
$$
真实 Sturm 目标必须重新取为
$$
 R_*(\Gamma)=\frac{1-d_4(\Gamma)}{16-d_4(\Gamma)}
 \in(-14,-13/2),\qquad
 \|D_\Gamma R_*\|<2^{-18}.
 \tag{C.9}
$$
这不是把旧 $R_*(0)$ 当成已经匹配；(C.9) 中的 $R_*$ 是新
实际无限尾的准确输出。

## 2. 只重调一个真实主段的停止长度

采用 R69 的实际 $u$ 坐标和归一 $z_u=a^2/4$，仍固定
$T=2^{24}$、$\Omega=2^{360}$。从 $u=T$ 开始，前准备段、
$q=2,R=-1/2$ 放大段及随后到 $q=-1$ 的固定短过渡全部保持。
它们终止于同一个
$$
 q=-1,\qquad -1/2-1/3000<R_b<-1/2,
$$
以及同一个 $H_b,\omega_b$。

最后从 $q=-1$ 到 $q=-8$ 的短过渡也保持原 quintic 函数及
长度 $\eta_c=2^{-24}$，其真实 Riccati flow 记为 $\Phi$。
按新真实目标选择唯一
$$
 R_e^{\rm in}(\Gamma)\in(R_*(\Gamma),R_*(\Gamma)+1/1000),
 \qquad \Phi(R_e^{\rm in}(\Gamma))=R_*(\Gamma).
 \tag{C.10}
$$
R11 §§4–5 的 $|F|\le4233$、$4233\eta_c<1/3000$ 以及
$\Phi'>0$ 对整个目标区间适用，故该根存在唯一。
在这里的严格负盒中更有 $1<\Phi'<2$，所以逆导数小于1。

中间的 $q=-1$ 主段满足 $P_v=P+16P^2$，其中 $P=-R$。
取准确停止长度
$$
 \ell(\Gamma)=
 \log\frac{P_e(\Gamma)(1+16P_b)}
                 {P_b(1+16P_e(\Gamma))},
 \quad P_b=-R_b,\quad P_e=-R_e^{\rm in}.
 \tag{C.11}
$$
这使末端第四线严格命中新尾目标，背景末端仍严格有 $q=-8$。
所有 endpoint 二 jet 按同一个实际方程接合；不在命中方向后再
任意平滑。

由 $P_e>6$，
$$
 0<\ell(\Gamma)<\log(9/8),\qquad
 \left|\frac{\partial\ell}{\partial R_*}\right|<1/512,
 \qquad \|D_\Gamma\ell\|<2^{-27}.
 \tag{C.12}
$$
这些 functions 对实参数连续，事实上是同一复邻域上的全纯
functions。有限短流在 $|R|<16$ 的固定复管上解析，
$|\Phi'-1|<e^{520\eta_c}-1<1$，可直接用局部解析逆；所有
$R_*(\Gamma)$ 都在 (C.7) 给出的同一个极小复圆盘内。
(C.11) 的两个 log 分母均离0，故不引入 branch 选择问题。

特别，对原 $\Gamma=0$，
$$
 |\ell(\Gamma)-\ell(0)|<2^{-43}
 \quad\text{于整个实盒 }\|\Gamma\|_\infty\le2^{-16}.
 \tag{C.13}
$$

## 3. 准确抵消：$\epsilon_{\rm tail}$ 不随重调变化

在主段 $q=-1$ 上，
$$
 (\log H)_v=1,\qquad(\log\omega)_v=-1,
 \qquad (H\omega)_v=0.
 \tag{C.14}
$$
其后短过渡的 $q(v)$ 和长度均固定，所以它给 $H\omega$ 乘
同一个常数。最终点满足
$$
 H_e(\Gamma)=H_e(0)e^{\ell(\Gamma)-\ell(0)},\qquad
 \omega_e(\Gamma)=\omega_e(0)e^{-[\ell(\Gamma)-\ell(0)]},
$$
$$
 \boxed{\quad H_e(\Gamma)\omega_e(\Gamma)=H_e(0)\omega_e(0).
 \quad}                                                         \tag{C.15}
$$

令 $b=r_{128}$、$\bar W_b=\delta_{128}^6/b^7$，实际 R69 缩放
现在准确为
$$
 \rho(\Gamma)=\frac1{H_e(\Gamma)b},\qquad
 \epsilon_{\rm tail}(\Gamma)
       =\frac1{4H_e(\Gamma)\omega_e(\Gamma)\bar W_b}.
$$
于是
$$
 \boxed{\quad
 \epsilon_{\rm tail}(\Gamma)=\epsilon_{\rm tail}(0),\qquad
 \rho(\Gamma)=\rho(0)e^{-[\ell(\Gamma)-\ell(0)]}.
 \quad}                                                         \tag{C.16}
$$
以这个固定 $\epsilon$ 调用完整非线性参考尾，然后整体等比
缩放 $\rho(\Gamma)$。这没有对一个已有非线性解作各向异性
拉伸。末端准确有
$$
 w_e=\frac{1}{4H_e\omega_e}
     =\epsilon_{\rm tail}\bar W_b,\qquad
 a_e=\rho b=H_e^{-1},\qquad a_e(w_e)_a/w_e=-7.
 \tag{C.17}
$$
所以实际切口高度斜率和二阶背景 jet 一起匹配。

相对四态在这个整体等比缩放下准确不变：物理高度扰动
$v^{\rm phys}=\rho v^{\rm ref}$、$a=\rho r$、$w^{\rm phys}=w^{\rm ref}$
给
$v_\theta/(aw),v_a/w,v_{\theta\theta}/(aw),v_{a\theta}/w$
相同的数值。时间 $\log a$ 只平移一个常数。
因此前篇实际 tail chart、hodograph、所有 negative return 和
联立 KAM **就是同一套相对方程**，不需要在新的 $\epsilon$
上重新求一个相互依赖的参数固定点。

## 4. 几何、mean 和新目标族的源列

本篇把先前固定物理缩放的候选 $g_\Gamma$ 升级为包括完整
connector 和真实尾缩放的 $\widehat g_\Gamma$。这发生在构造
最终目标度量的过程中，不是一个声称固定 $g_0$ 的 Newton 步。

R69 的所有有限盒仍成立：$-8\le q\le2$，末段长度小于
$\log(9/8)$，$4\Omega/5<\omega_e<5\Omega/4$。整个 connector
曲率小于 $5/6$，高度费用小于 $5a_T^2/36$。尾部额外的尺度
因子至多 $e^{2^{-43}}$；与 profile bump 的完整费用合并，
$$
 \max\{w/a,|w_a|\}
 <e^{2r_R}(1+8r_R)\frac{9375}{131072}<1/8,
 \qquad r_R=2^{-16}.
 \tag{C.18}
$$
这里仍覆盖全部无限层。flat 圆处的 $C^2$ 零 jet 和平盘保持。
在固定的物理径向圆盘上比较这些径向图：移动的接缝两侧有相同
完整 jets，flat 侧的 jets 一致趋0，所以参数的乘积拓扑连续性
仍给真实 $C^2$ 连续参考面。正支持的原覆盖论证继续给闭参考
嵌入。

所有高度用 $z_u=a^2/4$ 和 $z_a=-w$ 积分，接缝只选择一次
必要的高度平移。平盘的 mean 高度继续是输出，不能再另行固定。
具体地，以真实移动切口 $a_e(\Gamma)$ 及其高度 $Z_e(\Gamma)$
写
$$
 Z_\Gamma(a)=Z_e(\Gamma)
      -\int_{a_e(\Gamma)}^a w_\Gamma^{\rm phys}(s)\,ds.
$$
所以固定物理 $a$ 的完整变分是
$$
 \delta Z(a)=\delta Z_e+w_e\,\delta a_e
          -\int_{a_e(\Gamma)}^a\delta w^{\rm phys}(s)\,ds.
$$
移动切口端项 $w_e\delta a_e$ 与接缝高度变化一并保留。

由于物理尺度现在依赖 $\Gamma$，参数源列也必须更新。在固定
物理 $a$ 的尾内，写 $r=a/\rho(\Gamma)$、
$\delta\ell=D\ell[\delta\Gamma]$，准确有
$$
 \delta w^{\rm phys}
 =w_\Gamma\left(\sum_i\psi_i\delta\gamma_i
                          +A_\Gamma\delta\ell\right),
$$
$$
 \delta\widehat g_{aa}
 =2w_\Gamma^2\left(\sum_i\psi_i\delta\gamma_i
                          +A_\Gamma\delta\ell\right),
 \quad\delta\widehat g_{a\theta}
      =\delta\widehat g_{\theta\theta}=0.
 \tag{C.19}
$$
第二项是实际整体尺度变化在固定物理坐标中的项，不能遗漏。
connector 中还须对其真实停止长度及 profile 作同样的几何
微分；mean 高度是对应 $\delta w$ 的完整积分，没有自由删除的
常数行。这些是 metric-change 源，仍不能自动称作固定目标的
齐次 Jacobi 变化或假定已属于强空间 $\mathcal T_{224}$。

## 5. 同一条第四模双 bump 曲线

在本次重调后的 $u=T$，真实第四尾线严格为
$$
 (y_4,y_4'/4)\in\operatorname{span}(1,-\omega),
 \qquad\omega=\omega_*.
 \tag{C.20}
$$
这是 connector 的准确匹配结果。$T$ 以前的长段和双 bump
背景本身与 $\Gamma$ 无关。故 R74 的两个真实 bump
$$
 \psi=s\phi_1+\gamma_0t\phi_2,
 \quad \gamma_0=2^{-17},\quad
 |s|\le\gamma_0,\quad0\le t\le1,
 \quad B=T-25/8
$$
所看到的第四右线、第四变分密度及左端稳定目标都完全不变。
保持第四稳定线的唯一匹配曲线
$$
 s=s(\gamma_0t),\qquad -\gamma_0/64<s\le0
 \tag{C.21}
$$
因此是原 R74 的**同一个函数**，不只是具有同一个粗界。
其 $K_{4,2}/K_{4,1}<1/64$ 和 $K_{4,1}>\ell_b/2$ 不需重新
猜测，$\ell_b=1/16$。

但是其他频率的真实右线 $\Lambda_m(T;\Gamma)$ 会改变。
它们准确来自每个模自己的完整内部标签，再通过本篇真正的
connector 回传。每条都非零，否则二阶 ODE 唯一性与其非零
内部标签矛盾。它们与 $(s,t)$ 无关，因为两个 bump 的右端
半径、$\omega$ 和二 jet 保持，之后只发生参考高度平移。

## 6. 重新选取所有高模的共同好参数

对每个固定实 $\Gamma$，定义
$$
 G_\Gamma=\left\{t\in[0,1]:
 \left|\sin\angle\bigl(\Lambda_m(B;\Gamma,t),(1,\omega)\bigr)\right|
       \ge2^{-39}\ \text{对全部 }m\in4\mathbb N\right\}.
 \tag{C.22}
$$
R11 附录 A 的坏集估计只要求：真实非零右线与 bump 参数独立、
第四线 (C.20)、同一第四保持曲线、正区系数盒。以上均已逐项
保留，故其全频证明对这里的**新真实输入线**原样成立：
$$
 |G_\Gamma|\ge1-83/16384>0.
 \tag{C.23}
$$
这里每个坏角区间的单调穿越、$n^3$ 横截费用和所有 $m$ 的
可和测度都保留；不是只检查某个最大频率。负帽是同一个参考
对象的反射，可取同一个参数。可准确令
$t_\Gamma=\min G_\Gamma$，并使用 $s(\gamma_0t_\Gamma)$。

本篇只据此作逐点选择。闭好集的非空与测度下界本身不证明这个
最小元在任意参数邻域连续，也不构成原固定 bump 对所有新
$\Gamma$ 都好的声明。

## 7. 与实际负型 KAM 的无循环共同选择

双 bump 两端的 $h,\omega$ 以及全部二 jet 不变，故它不改变
本篇 connector 的输入、$\rho(\Gamma)$ 或固定
$\epsilon_{\rm tail}$；它只改变后续整体参考高度的加法值。
而 tail principal、完整相对状态及其 ray return 都不依赖这个
参考高度平移。因此可以按准确依赖关系同时完成：

1. 用前篇联立 KAM 得到全部 $\Gamma^*(a)$；
2. 用 (C.10)–(C.17) 接上新真实第四方向并作整体等比缩放；
3. 对这个完整新右尾取 $t\in G_{\Gamma^*(a)}$，再用同一个
   $s(\gamma_0t)$。

第三步不会反过来改变第一步的方程，第二步也没有改变它的
$\epsilon$。这是一套真实共同选择，不是先后使用不一致的尾。

前篇已准确证明 $\Gamma^*(e^{im\varphi}a_m)=\Gamma^*(a)$。
因此对最终选定的 $a_*$，同一个 $t_{\Gamma^*(a_*)}$、同一个
停止长度和同一个尺度适用于整个相位轨道。它们定义一个固定的
完整目标 $\widehat g_{\Gamma^*(a_*),t_{\Gamma^*(a_*)}}$。
这里仍未断言存在满足主体和 regular 全非线性匹配的 $a_*$；
选择最终标签是尚待完成的全局方程。

## 8. 新真实 regular 线及全部两迹的已付结论

固定任何 (C.22) 的好参数。长未改区 $0\le u\le B$ 仍为
R74 的原精确指数段，其入口 $a_*,z_*,\omega$ 均未改变。
完整新尾的齐次方向给
$$
 |c_+/c_-|\le2^{39}e^{-2m\omega B},\qquad
 |\lambda_m+m\omega|\le2^{41}m\omega e^{-2m\omega B},
 \qquad \lambda_4=-4\omega.
 \tag{C.24}
$$
这里 $\lambda_m=y_m'(0)/y_m(0)$。原 R74 (74.18) 的较松
常数 $2^{41}$ 来自 $4\epsilon_*^{-1}=2^{41}$，并保持真实
指数反射项。

对真实 grounded 两迹仍使用同一个准确矩阵
$$
 v=A_0y-4y'/m^2,\qquad p=-y+4y'/A_0,
 \quad A_0=4\omega+a_*^2/z_*.
$$
于是新实际 homogeneous DN 仍有
$$
 \frac m7<\gamma_m<\frac m5,\qquad
 \left\||D_\theta|^{-1/2}
       (\Gamma_{\rm ext}-|D_\theta|/(4\omega))
       |D_\theta|^{-1/2}\right\|<2^{-36}.
 \tag{C.25}
$$
这是重新选择后的新真实全尾 DN，不是原 DN 的未经证明的
连续延拓。全部 $m\ne0$ 都在其中；mean 通量行另保留。

在 $u=B$ 的完整 raw 两迹，原准确矩阵
$\mathsf J_m$ 与新的 (C.22) 同样给
$$
 |k_B/m+\coth(mL)f_B|
 \ge2^{-40}(|f_B|^2+|k_B/m|^2)^{1/2},\qquad L=\omega B.
 \tag{C.26}
$$
不除以可能为0的高度。普通源出现时，R74 (74.16) 的真实
$J,R_m$ 两个端点项必须同时带入；仅 (C.25) 的齐次斜率
不能替代普通源的完整响应。

## 9. 新共同目标上的完整非线性匹配式仍保留

新的实 connector 满足原 balanced224 的同一 $q,A,w/a$ 盒与
逐段长度预算；双 bump 也满足原统一盒。因此对每个固定
$(\Gamma,t)$，真实全标签尾可以在同样已付角宽上前推至 $B$，
输出完整 $(f_B^{\Gamma,t}(a),k_B^{\Gamma,t}(a),\lambda_B^{\Gamma,t})$。
原长径向非线性 Dirichlet map 完全未变，因为 $[0,B]$ 的
参考几何没有改变。

准确非mean匹配仍是
$$
 k_B^{\Gamma,t}(a)+\mathsf C_Lf_B^{\Gamma,t}(a)
       -\mathsf S_Lf_*
       -\mathcal E_D(f_B^{\Gamma,t}(a),f_*)=0.
 \tag{C.27}
$$
内端平均高度从 $\lambda_B^{\Gamma,t}$ 开始积分；一旦完整
非mean两迹相等，同一个 holonomy-one 小根使 mean 斜率相等。
外端平均高度与有源 holonomy 负荷仍是主体需消费的输出。

若把 $\Gamma=\Gamma^*(a)$ 和选定的 bump 一并纳入构造迭代，
那么 (C.27) 的导数必须包含 (C.19) 以及对应有限段的参数列。
它不再是原固定 $g_0$ 的纯标签导数。另一方面，一旦真正求得
一个最终匹配点，§7 保证其整条相位轨道使用同一个目标。

本篇完成了新真实第四方向、有限 connector、物理尺度和双
bump 的共同合法选择。全 mixed turning 幅度、实际高输入相对
逆以及非线性匹配点的存在仍须继续证明。

## 10. 准确预算程序

`scripts/fourfold_retuned_fourth_connector_20261113.py` 核对实际
Möbius cone、无限深倍率、真实斜率盒、停止长度微分、尺度
抵消和全部几何/双 bump 常数门，输出
`notes/2026-11-13-R119-retuned-fourth-connector-budget.json`。
真实全频矩阵、无限标签图和所有参数的量词依赖已在正文明确。
