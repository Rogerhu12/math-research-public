# R572 从起点通量全零母：自然、环境 self 与全部实际微包总通量

日期：2026-11-26。**已证明。**本文不重开 R567–R570 已闭合的八矩、scalar、第三、pose 证明，也不把以下完整总通量零当成整个第四 period 零。

## 1. 一个母，同时支付三种准确的有限读出

R521 §2.1 对母函数的要求是任意非零实紧光滑 $u$。它不要求 $u$ 正、单峰，也不要求旧 R410–R455 的简单退化点、共同 cap 或十九／二十目标。利用这个准确的自由度，可以在 R521 的第一次母选择时，同时支付以下三项：

1. 对完整真实成本空间 $U$ 的所有 $V$，母及其全部正仿射副本的修正自然通量 $\Lambda$ 为零。
2. 对一个覆盖所有有限 canonical 路径的仿射稳定有限环境 $E$，所有环境系数的 raw self 通量 $\Omega$ 为零。
3. 在预先固定的 R521 整个真实复制图上，每个最细微包、全部相位的 raw period 总通量为零；这项直接从原完整模板读出，不假设 whole pure 已零。

三项分别定义和证明，不将一种读出偷换成另一种。

所得同一个母可以准确取成
$$
u(x)=\psi(x)P(x),\qquad
\psi(x)=
\begin{cases}
e^{-1/(1-x^2)},&|x|<1,\\
0,&|x|\ge1,
\end{cases}
\tag{1}
$$
其中 $P$ 是非零实偶多项式，且 $\int(u'')^2=1$。
因此 $u$ 在内区解析、两端真正全平，支撑是一个连通闭区间。
内部没有开放零 collar。这不是将一个母拆成不交小包，再把其中的总通量彼此抵消。

## 2. 两个成本空间及完整五次读出

### 2.1 原真实 $U$ 上的自然收缩

$U$ 是 R105 §5 定义的完整 canonical 第四成本真实有限空间。
其定义使用同一常 scalar germ、闭 frame、零低阶端口的真实成本取实跨度。
本文不将 R570 的偶 germ 自动称为常 germ。

对 $V\in U$，使用 R352(23)的完整定义
$$
\begin{aligned}
\Lambda_u(V)={}&\int u'''V(u^2,0)
-\frac{16}{5}\int u'''\pi V(u)\\
&-\frac{32}{15}\int u'''\mathscr G_{V,u}(\mu(u)).
\end{aligned}
\tag{2}
$$
原 pure 及全部有序三矩尾均保留。
R352 §7 已证明：它对 $V$ 线性、对 $u$ 为连续齐次五次泛函。
特别
$$
\Lambda_{-u}(V)=-\Lambda_u(V).
\tag{3}
$$

### 2.2 覆盖任意有限 canonical 路径的环境 $E$

R105 §3 在给任何实际几何系数赋值之前，由原完整分子恢复给出有限模板
$$
\Psi_1,\ldots,\Psi_q,
\qquad
V_B^0=\sum_{\alpha=1}^q c_\alpha(B)\Psi_\alpha
\tag{4}
$$
用于任意有限 canonical 几何路径 $B$。
这里不要求 $B$ 的 germs 常值、低阶端口零或内部 ruling 已零；
这些模板只表示其完整 canonical characteristic 累计。
各模板对原第一 profiles 为四次齐次，保所有右锚原函数、两尾及有序 history。

把(4)的模板连同 $U$，对全部正仿射作用取有限 Laurent 系数闭包。
所得空间记为 $E$。它仍有限维：逐个模板的有限语法树中，profile jet 给
$a^{-j}$、右原函数给 $a$、坐标幂给 $(ax+c)^j$；展开后只有有限个
$a$ 的整数幂和 $c$ 的非负整数幂。将这些系数向量全部加入即可。
这个轨道跨度对仿射群稳定，因为再作用一次只是把两个正仿射变换复合。
故
$$
U\subset E,\qquad
\mathsf P_{a,c}E=E,\qquad
V_B^0\in E
\quad\text{对每个有限 canonical }B.
\tag{5}
$$
不声称 $E=U$，也不把 $E$ 中的任意有号系数当成一条实际正时长路径。

对每个 $\Psi\in E$ 定义没有 natural 修正的 raw self 读出
$$
\Omega_u(\Psi):=\int u'''(x)\Psi(u^2,0)(x)\,dx.
\tag{6}
$$
它对 $\Psi$ 线性、对 $u$ 连续且齐次五次。
这里没有在 $E$ 上强行延拓 $\mathscr G$ 或假设 $U$ 的有序因子化定理
已覆盖每个环境模板；(6)直接使用已有的完整四次模板。

右锚取在共同支撑右方。R105 的正 profile 次数保证在右空区移动锚
不加新常数。由真实仿射作用或直接换元，准确有
$$
\begin{aligned}
\Lambda_u(\mathsf P_{a,c}V)
 &=a^2\Lambda_{C_{a,c}u}(V),\\
\Omega_u(\mathsf P_{a,c}\Psi)
 &=a^2\Omega_{C_{a,c}u}(\Psi),\\
(C_{a,c}u)(x)&=u((x-c)/a).
\end{aligned}
\tag{7}
$$
第二式也可逐式核对：在 $y=ax+c$ 下，外三阶导数给 $a^3$，
积分给 $a^{-1}$，其余正是完整模板的 pullback，故总因子为 $a^2$。

## 3. 先固定 R521 复制图，再定义真实微包读出

### 3.1 这个有限图不依赖待选母

先在一个参考窗口内，为支撑 $[-1,1]$ 的输入预留足够小的实际宽度，
并固定以下全部资料：

- R521 的四个等距不交微包及系数 $(1,\sqrt3)$；
- 八个等距完整副本及原实幅权
  $(-1)^j\binom7j^{1/3}$；
- 原有限 $O(2)$ 旋转、反射列表；
- 原十一位置的正权匹配及全部实际安置位置。

四微包的三矩有限差分身份只依赖平移多项式次数；
八复制的第三消去也只依赖三次幅权及原六次平移界。
$O(2)$ 列表固定在两输入系数平面中，与母形无关。
十一位置匹配使用预选参考位置测度的零至十次矩，
其正节点／权重先由该参考测度选定，也与 $u$ 无关；
它匹配的是原完整 ruling 对块位置的十次多项式，
不是先评价某个母的 forcing 后才拟合位置。
因此这一整张图可以在选(1)的多项式 $P$ 之前固定。

记最细微包的个数为 $K$，相应互不交区间为 $J_i$，
固定线性输运为 $L_i$，实际幅度／方向为 $a_i,b_i$。
对任意支撑于 $[-1,1]$ 的 $u$，图给
$$
u_i=L_i u,\qquad
f_u=\sum_{i=1}^K a_i u_i,\qquad
g_u=\sum_{i=1}^K b_i u_i.
\tag{8}
$$
$L_i$ 保真实固定宽度、中心；所有共同幅度已明确放进
$a_i,b_i$，不能在之后改用绝对值。
特别 $u\mapsto(f_u,g_u)$ 是同一个固定实线性映射。
有些 $a_i$ 可以为零，这不妨碍以下使用 $u_i'''$ 作为外因子。

### 3.2 全部相位只有有限个四次模板通道

将 $\Psi\in E$ 作用在
$$
F=f_u^2,\qquad
\phi_\theta=\cos\theta\,f_u+\sin\theta\,g_u.
$$
这里平方按原对称二次槽解释，保原双线性恢复。其整个 canonical 第四输出是四次齐次相位多项式。
用一个允许冗余的实列表
$$
1,\ \cos2\theta,\ \sin2\theta,\ \cos4\theta,\ \sin4\theta
$$
记各函数系数为 $\Psi_m[f_u,g_u]$。
不把五个生成元说成五维真实秩。

为每个 $i,m,\Psi$ 定义原 raw total
$$
\mathcal T_{i,m}(u;\Psi)
 :=\int_{J_i}(L_i u)'''(x)\,
       \Psi_m[f_u,g_u](x)\,dx.
\tag{9}
$$
所有 Volterra 左尾、右 suffix、跨包历史都留在 $\Psi_m$ 中；
没有先将它局部化为一个 self 公式。

因为(8)线性、$\Psi_m$ 四次而外因子一次，
(9)也是关于同一 $u$ 的连续齐次五次泛函，准确满足
$$
\mathcal T_{i,m}(-u;\Psi)=-\mathcal T_{i,m}(u;\Psi).
\tag{10}
$$
其积分区间在选母前已经固定，所以不存在随根移动产生的未付导数项。

原母在每个 $J_i$ 端点全平，故分部积分准确给
$$
\int_{J_i}u_i'\,\Psi_m[f_u,g_u]''
 =\int_{J_i}u_i'''\,\Psi_m[f_u,g_u].
\tag{11}
$$
端项不要求 $\Psi_m$ 左右平台本身为零。
又因 $f_u'''|_{J_i}=a_i u_i'''$、
$g_u'''|_{J_i}=b_i u_i'''$，
(9)的零同时支付以实际 $f_u'''$ 或 $g_u'''$ 为外因子的
两类原总通量。它不依赖 R409 的 whole-pure-zero 假设。

## 4. 一个球面共同零点支付全部三项

取 $U$ 的一组真实基 $V_1,\ldots,V_N$ 和 $E$ 的一组基
$\Psi_1,\ldots,\Psi_M$。只使用有限维性，不新计算或猜测实际秩。
全部下列坐标共有一个有限上界
$$
d=N+M+5KM:
$$
$$
\begin{gathered}
\Lambda_u(V_j)\quad(1\le j\le N),\\
\Omega_u(\Psi_k)\quad(1\le k\le M),\\
\mathcal T_{i,m}(u;\Psi_k)
\quad(1\le i\le K,\ 1\le k\le M,\ 1\le m\le5).
\end{gathered}
\tag{12}
$$
冗余坐标可以照留；$d$ 不是任何已算出的研究秩。

取
$$
\mathscr P_d
 =\operatorname{span}_{\mathbb R}
  \{\psi,x^2\psi,\ldots,x^{2d}\psi\}.
\tag{13}
$$
这些函数线性无关，故维数为 $d+1$。
二次型 $\|u\|_*^2=\int(u'')^2$ 在此空间正定：
若它为零，则光滑 $u''=0$，真紧仿射函数只能恒零。
所以
$$
\Sigma=\{u\in\mathscr P_d:\|u\|_*=1\}
$$
是一个带反足作用的 $d$ 维球面。

(12)定义连续奇映射 $\mathcal F:\Sigma\to\mathbb R^d$。
奇映射形式的 Borsuk–Ulam 定理给 $u_*\in\Sigma$ 使
$\mathcal F(u_*)=0$。这里所用拓扑命题是：
连续奇映射 $S^d\to\mathbb R^d$ 必有零。
若无零，归一化会给奇映射 $S^d\to S^{d-1}$；
对 $d\ge2$，其射影空间映射把一次生成元拉回到一次生成元，
但目标中该元的 $d$ 次幂为零、源中非零，矛盾。
$d=1$ 由介值定理，$d=0$ 无待付坐标。
这只应用固定有限维的存在定理，不以数值近零替代准确零点。

由各读出对成本系数的线性性，同一个 $u_*$ 因而满足
$$
\boxed{
\begin{aligned}
\Lambda_{u_*}(V)&=0&& (V\in U),\\
\Omega_{u_*}(\Psi)&=0&& (\Psi\in E),\\
\mathcal T_{i,m}(u_*;\Psi)&=0
 && (\Psi\in E,\ 1\le i\le K,\ 1\le m\le5).
\end{aligned}}
\tag{14}
$$
$u_*$ 非零、实、偶且有(1)的形式。
非零多项式不可能在开区间恒零，所以没有内部开放零 collar。
这些是同一点的全部准确方程，不是为不同成本或不同微包另选母。

## 5. 正仿射输运、真实图及规范相容

### 5.1 全仿射自然与 self 零

由(5)(7)，把(14)分别用于
$\mathsf P_{a,c}V\in U$ 和 $\mathsf P_{a,c}\Psi\in E$，得到
$$
\boxed{
\Lambda_{C_{a,c}u_*}(V)=0,\qquad
\Omega_{C_{a,c}u_*}(\Psi)=0
}
\tag{15}
$$
对全部 $a>0,c$、$V\in U,\Psi\in E$ 成立。
再用五次齐次性，任何实幅度也保持零。

对(9)的整张复制图作共同正仿射输运，同一换元给
$$
\mathcal T^{\,\mathrm{transported}}_{i,m}(u_*;\Psi)
 =a^{-2}\mathcal T_{i,m}
      (u_*;\mathsf P_{a,c}\Psi),
\tag{16}
$$
其中右侧按同一实际坐标约定输运图和锚。
因 $E$ 稳定，(16)仍为零。
因此可将整个预定图共同压入或平移到最终合法窗口；
不是冻结以后逐包另改中心、宽度或形状。

式(15)强于只设 $M_5(u)=0$ 或只设 R406 的 $n_2$ 全仿射为零。
它不把 $\mathcal N:U\to\{\text{所有紧输入上的函数}\}$ 置零。
其他形状上的自然函数仍然保留，所以与
R406 的 $\ker\mathcal N\subseteq\ker\lambda_+$ 没有矛盾：
这里选的是所有这些五次函数的共同零输入，
不是令一个正字符非零的 $V$ 落进 $\ker\mathcal N$。

### 5.2 原 R521 与已闭真实词可在此新初选上顺序执行

固定(14)的母及整张图，再按 R521 作原三矩圆、第三 ruling 和完整
$O(2)$ 合成。这些步骤仅使用已固定幅权／位置、有限次数及
非零实紧母，不要求母正单峰。
R521 最后的共同正幅归一可在这个母选定后执行：模板输出乘共同幅度的四次幂，连同外因子则为五次幂，已为零的全部读出仍零；无需为不同成本重选母。
原 $C_k>0$ 证明仍成立：
它的正积分若消失，相应 $F$ 必恒零，
原二阶方程和双端全平会迫 $u_*=0$，与归一矛盾。
大 $\Omega$ 的严格号和比例使用原非零平方范数与完整积分，
亦未调用旧正单峰或 cap 假设。

几何参数仍按原顺序选择：
$H,H_0$ 固定，$\Omega$ 足够大，随后取 $R$、
固定有限几何词，最后小 $\delta$。
所有依赖母的常数和最终参数均重新在这一套同母上选择一次。
R564、R567、R568、R570 的结构证明按原顺序适用，
整词使用同一次初选的 profiles 与同一个 $\chi$。
这不是把旧冻结几何或 Gram 数值换母后原封不动沿用，
也不在不同母的轨道间拼接。

### 5.3 当前非零 χ 的完整周期为何等于 canonical 周期

在新初选上执行 R570，记真实四段闭词
$$
\mathcal W=(PP^R)^2.
$$
其 scalar 全 jets、frame、位置以及原完整 $A,T$ 均返回，
$A_{\mathcal W}=T_{\mathcal W}=0$，
且同一 $\chi$ 下的逐段完整第四 ruling 为零。

当前第二 gauge 为 $w=0$，第三 gauge $\chi_\theta$ 一般非零。
不能仅把这个非 canonical 场的成本叫作 $U$ 中元素。
R83 的完整输入历史 transfer，或 R184(7)–(9)，给准确全函数差
$$
V_{\mathcal W}^{\chi}(x,\theta)
 -V_{\mathcal W}^{0}(x,\theta)
 =-2A_{\mathcal W}(\phi_\theta,\chi_\theta)=0.
\tag{17}
$$
这里保留同一个真实右锚与全词起点。
更一般的合法独立 $w$ 所产生的另两项
$2T_{\mathcal W}(w;D)-4T_{\mathcal W}(\phi;\phi,w)$
也因完整 $T_{\mathcal W}=0$ 消失，
而平方项为 $-A_{\mathcal W}(w,w)=0$。
所以相等的是整个 $x,\theta$ 周期函数，不是仅一个 ruling 积分。

由(4)(5)，该同几何的 canonical 成本
$V_{\mathcal W}^{0}$ 确实属于 $E$。
这一成员性不要求端 germ 常值；
本文不额外断言它属于原较窄定义的 $U$。

## 6. 对实际第四 period 已付和未付的内容

R570 给
$$
V_{\mathcal W}^{\chi}(x,\theta)=4V_P^\chi(x,\theta).
\tag{18}
$$
由(17)，它等于 $V_{\mathcal W}^0$ 在当前第一圆上的值。
将这个实际 canonical 系数代入(14)，再重组有限相位通道，得到
$$
\boxed{
\begin{aligned}
\int_{J_i} f'''(x)V_{\mathcal W}^{\chi}(x,\theta)\,dx&=0,\\
\int_{J_i} g'''(x)V_{\mathcal W}^{\chi}(x,\theta)\,dx&=0
\end{aligned}
\quad\text{对每个实际 }J_i,\ \theta.}
\tag{19}
$$
等价的 $f'V''$、$g'V''$ 形式由(11)给出。
这些是原真实复制图的 raw totals：
全部微包、全部真实右 suffix、平台尾、相位和 history 都已进入。
不用 whole pure 零，也不用将 natural correction 擅自删掉。
另由(15)，该 canonical 环境系数的全部母仿射 raw self 收缩亦零。
自然 $\Lambda(U)$ 的全零结论独立保留，但不为使用(19)而虚授
$V_{\mathcal W}^0\in U$。

以下接口仍必须实际支付：

- (19)不使 $V_{\mathcal W}^{\chi}(x,\theta)$ 逐点为零。
  原内部部分通量、平台仿射项、退化点的完整相容及 cap 匹配仍保留。
- 当前 $A=T=0$ 的同一实际几何上，(17)及其一般 $w$ 形式表明
  独立二、三阶 gauge 不能再改变第四 period。
  因而不能在保持几何不变时用一个新 $w$ 或 $\chi$ 抹掉(18)。
- 旧 R70／R333／R518 的 unconstrained 真实成本截面没有自动满足
  R521 的同一固定 $\chi$ ruling；response span 不能代替实际受约束可达性。
- 本母可能改号且有多个普通内部零或临界点。
  旧正单峰母的简单退化对、固定 cap、十九／二十根和十三规范收据
  均未由本稿继承。

因此下一端图可以在已经准确满足全部实际总通量(19)的
同一初选上，继续读取和控制完整有限 profile period 系数。
若采用非零但当前圆上不可见的第三 hook 方向，
仍须实际支付同一二阶 gauge、全 ruling 与十三行。
本稿付清三组有限五次目标和实际全微包 totals，
没有把有限积分零升级为整个 period、有限等距族或主课题完成。

## 7. 直接来源

- [R105](../results/R105-finite-canonical-fourth-cost-space-and-response-quotient.md)，共同有限第四模板、真实 $U$、逐模板正仿射次数。
- [R352](../results/R352-ordered-three-moment-tail-map-and-natural-total-flux-quotient.md)，完整修正自然收缩、有序尾、五次齐次性与仿射关系。
- [R406](../results/R406-complete-weight-zero-natural-fluxes-and-canonical-joint-obstruction.md)，自然全函数与单个输入的区别、原正字符。
- [R521](../results/R521-finite-positive-orthogonal-copies-and-nondegenerate-full-history-acceleration-control.md)，任意非零实紧母、与母形无关的有限正复制及非退化 full ruling。
- [R83](../results/R83-true-fourth-transfer-and-zero-lower-history-variations.md)、[R184](../results/R184-affine-linear-fixed-circle-fourth-range-with-second-gauge.md)，完整同锚 gauge transfer 与其周期项。
- [R570](../results/R570-neutral-residence-pose-and-real-four-piece-return.md)，真实四段全部低阶及 pose 返回，保留 $4V_P$。
