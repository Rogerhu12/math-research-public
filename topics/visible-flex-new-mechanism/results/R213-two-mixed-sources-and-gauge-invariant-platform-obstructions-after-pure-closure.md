# R213：pure 已付后的两个真实 mixed 源、平台不变量与八矩二阶 gauge

日期：2026-11-15。**完整纸面推导；没有新的研究编译、profile 求积、函数消元或几何计算。**

本稿接 [R210 的真实整 pure 支付](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md) 和 [R211 的固定圆 Green 接口](R211-finite-range-conditions-and-Green-inverse-for-fixed-circle-period-gauges.md)。不再把两个 mixed 目标当作未指明的任意函数：它们可以直接从原三阶圆的三个已存在场读出。还证明两项具体事实：最右纯 g 段的旧 period 门在 universal pure 已付后自动消失；共同左 collar 的二次尾系数则是一个真正的 ruling 商泛函，对全部允许的二阶 gauge 不变。

最后给出 R183 圆上一个完整合法的二阶 gauge 子族。它由任意八矩算子作用于原二阶 forcing profile 得到，六个交叉矩由原八包有限差分准确支付，其整个第四 period 变化恰落在已知 hook 响应空间中。这个子族不提供一个新的、可不受 canonical 泛函约束的函数方向。

没有声称下述未评估的 mixed 源或 ruling 矩已经为零，也没有把两个 period 方程和逐 ruling 方程分别用不同的 gauge 求解。

## 1. 固定几何、固定圆与 pure 身份的强度

取 R210 已经真实构造的有限闭 hook 几何，保同一 scalar/frame 端口、真实空间闭合及全部拼接成本。记其整个 second、third 算子为

$$
M=0,\qquad T=\kappa\mathfrak H,\qquad \kappa\ne0,
\qquad \pi V=0.
\tag{1}
$$

最后一个等式是对所有共同右 collar profiles 的 universal pure 函数身份，不是只在本文选定圆上或一个幂尾上成立。几何固定后，取其共同合法物理区间 $I=[\ell,r]$，所有右原函数均锚在同一 $r$，所有 $s$ 历史均从同一实际起点累计。

在 I 内放入 [R183](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md) 的八完整 packet 圆。记

$$
\phi_\theta=c f+s g,\qquad c=\cos\theta,\quad s=\sin\theta,
$$

$$
F=f^2,\qquad d=f^2-g^2,\qquad e=2f\odot g,
\qquad D_\theta=F-\phi_\theta^2=s^2d-cs e.
\tag{2}
$$

这里 $f^2,f\odot g$ 是对称平方槽记号；例如 $\Phi_E(f\odot g)=\Phi_E(f,g)$。所有 profiles 双 collar 为零。原目标仍是同一个

$$g_\varepsilon=g_X+\varepsilon^2(dY_f)^2.$$

R183 已经支付完整二、三阶 range，并给原同锚场

$$
Z_\theta=s^2Z_d-csZ_c,
$$

$$
W_\theta=s^2(cW_{fd}+sW_{gd})
-cs(cW_{fc}+sW_{gc}).
\tag{3}
$$

它们是真实周期、双 collar 的向量场。特别是 $Z_c$ 恢复的是 $2H(Y_f,Y_g)$，$W_{fc}$ 恢复的是 $-2H(Y_f,Z_c)$；本文保持这个系数规范。

## 2. 两个剩余目标有三个已存在场的准确来源

用 $\mathscr P_B(H)$ 表示 R56 的整个 $\xi$ 周期函数，用
$\mathscr K_B(H)(s)=\int H_{uu}\,du$ 表示真实逐 ruling 积分。定义

$$
\boxed{\begin{aligned}
V_d&=\mathscr P_B\{-H(Z_d,Z_d)-2H(Y_g,W_{gd})\},\\
V_e&=\mathscr P_B\{H(Y_f,W_{fc})\}.
\end{aligned}}
\tag{4}
$$

这些式子不把中间 second/third 历史置零；$Z_d,W_{gd},W_{fc}$ 就是 (3) 中的原场。它们已具有所需的周期和两个 collar，因此 (4) 的 forcing 均直接满足 R56 第 1 节的输入假设。

**命题 1。** 在 (1) 下，原完整 canonical 第四 period 准确为

$$
\boxed{V^0_\theta=s^2V_d+2csV_e.}
\tag{5}
$$

**证明。** 原第四 forcing 是

$$H^0_{4,\theta}=-H(Z_\theta,Z_\theta)-2H(Y_{\phi_\theta},W_\theta).$$

由 (3)，其 period 在 $\theta=\pi/2$ 恰为 $V_d$。在 $\theta=0$，

$$Z_0=W_0=0,\qquad \partial_\theta W_\theta|_0=-W_{fc},$$

故

$$\partial_\theta V^0_\theta|_0=2V_e.$$

R159 的 universal pure 消去及种子条件使整个相位函数只有 $s^2$ 和 $cs$ 两个独立项；上述两个准确值决定 (5)。也可用该文的唯一表

$$B=2K-L^T,\qquad V^0_\theta=B(F,D_\theta)$$

直接核对：

$$
\boxed{V_d=B(f^2,f^2-g^2),\qquad
V_e=-B(f^2,f\odot g).}
\tag{6}
$$

由 pure 极化，$Q(f^2,f\odot g)=0$，所以第二式也等于
$V_e=-L(f^2,f\odot g)$。这与 $W_{fc}=-4U_B(f;f\odot g)$ 的真实第三恢复式一致。证毕。

R180/R184 的 hook period 变化是 $2\kappa L_f(w_\theta)$。因此 R211 中的两个准确目标不是任意新数据，而是

$$
\boxed{G_c=-\frac{V_d}{4\kappa},\qquad
G_s=-\frac{V_e}{2\kappa}.}
\tag{7}
$$

完整 period 方程写成

$$
L_f(w_\theta)=(1-\cos2\theta)G_c+\sin2\theta G_s.
\tag{8}
$$

若取两个相位系数 $w_c,w_s$，则对应方程恰为
$L_f(w_c)=G_c$、$L_f(w_s)=G_s$；仍须同时付合法第三 range 以及 R184 的同一个 ruling 商方程。这里没有把“可分别求这两个方程”冒称为所有相位 gauge 的完整分类。

## 3. 右因果已经消掉最后一个纯 g 段，但不消掉内部平台门

R56 的 profile 运算只用局部导数、乘积与同一右锚积分；沿 $s$ 的真实历史积分不会扩大其 $\xi$ 方向的右依赖范围。于是若

$$f|_{[x_0,r]}=0,$$

则 R159 的原表 $B(f^2,D)$ 在该整个右带为零：每项都含两个 f 槽，且局部值和右侧的全部 f 原函数贡献均为零。故

$$
\boxed{V_d|_{[x_0,r]}=V_e|_{[x_0,r]}=0.}
\tag{9}
$$

这不是删除 $s$ 历史，也不需要 g 在该右带为零。对于 R183 的最右基本 packet，f 在第三下降段之后恒零，而 g 仍有第四下降段。R198 在这个最后纯 g 段发现的 period 门，现在由 (1) 的 universal pure 身份准确支付；不是靠改变原已冻结 step 或把右尾重锚。

相反，若只知 f 在一个内部开平台 J 为常数，平台右方仍有 f 的变化，则不能应用 (9)。真实 $B$ 仍可含来自平台右方的全部 f 尾。R181 给对任意全 I 光滑 w 的原式身份

$$f'|_J=f''|_J=0\quad\Longrightarrow\quad L_f(w)''|_J=0.$$

因此完整第四 period 可解的必要条件是两个明确的新源满足

$$
\boxed{V_d''|_J=0,\qquad V_e''|_J=0.}
\tag{10}
$$

这里 w 可以支撑跨越平台，也可以有任意允许的右尾；(10) 并不限制 w 为局部支撑。它对全部 R184 允许的二阶 gauge 都不变。不能由 $f'|_J=0$ 把 (4) 本身宣称为零，因为 $Y_f$ 的值以及原恢复的右尾通常非零。

## 4. 左二次尾是一个真实 ruling 商泛函

下面先对任意由周期、双 collar 已知场生成的 R56 forcing H 论证。记

$$\mathcal K_H(s)=\mathscr K_B(H)(s).$$

R56(2)–(4) 给：在共同左 collar，$B_H=0$，$T_{s,H}=0$，且

$$P_H(s,x)=\frac12\mathcal K_H(s).$$

这里 $P_H$ 是真实右积分的左端值，不人为置零。由 R56(5)，该 collar 上的整个 period 是

$$
\begin{aligned}
\mathscr P_B(H)(x)
&=\frac12\int_B\{K_0(s,x)\mathcal K_H(s)
-\lambda(s,x)\partial_s\mathcal K_H(s)\}\,ds\\
&=\frac12\int_B\{K_0(s,x)+\partial_s\lambda(s,x)\}
\mathcal K_H(s)\,ds.
\end{aligned}
\tag{11}
$$

分部积分的端项为零，因为几何和已知场都按真实全周期相接。$K_0$ 关于 x 二次，二次项为 k；$\lambda$ 关于 x 至多一次。因此 (11) 是真实的二次多项式尾，且

$$
\boxed{[x^2]\mathscr P_B(H)=\frac12\int_B k(s)\mathcal K_H(s)\,ds.}
\tag{12}
$$

方括号只抽取左 collar 上该唯一多项式的系数，不是把活动区间内的整函数作多项式截断。

现在记 (4) 两个 forcing 的 ruling 为

$$
\boxed{\begin{aligned}
K_d(s)&=-\int (Z_d)_u\cdot(Z_d)_u\,du
-2\int(Y_g)_u\cdot(W_{gd})_u\,du,\\
K_e(s)&=\int(Y_f)_u\cdot(W_{fc})_u\,du.
\end{aligned}}
\tag{13}
$$

其全 $s$ 历史仍由原场保留。(12) 直接给两个固定圆必要条件

$$
\boxed{\int_B kK_d\,ds=0,\qquad
\int_B kK_e\,ds=0.}
\tag{14}
$$

理由是 R181 的 $L_f(w)$ 在共同左 collar 至多是仿射函数，故任何二阶 gauge 都不能改变 (12) 的二次系数。两条件在 (7) 中也分别表现为 $G_c,G_s$ 必须具有仿射而非二次的左尾。这在应用 R211 的 Green 接口前就是一个明确可检查的门。

### 4.1 为什么它确实定义在 ruling 商上

R184 的第三 gauge 与二阶平方项落在

$$
\mathcal W=\{s\mapsto\mathbf w(s)\cdot v:v\in\mathbb R^3\},
\qquad
\mathbf w=\left(\frac{1+d^2}{4h},\frac d2,\frac h4\right).
$$

由 R73 的真实矩阵坐标

$$p_0=-\frac{k(1+d^2)}{2h},\qquad p_1=-kd,\qquad p_2=-\frac{kh}{2},$$

以及全周期 $M=0$，有

$$
\boxed{\int_B k(s)\mathbf w(s)\,ds=0.}
\tag{15}
$$

所以 $\mathfrak q_k([K])=\int_B kK\,ds$ 是
$C^\infty(S^1_s)/\mathcal W$ 上良定义的真实线性泛函。

对任意合法二阶 gauge，R184 的完整 ruling 变化包括
$\mathcal B_\theta(w)$、平方项及第三齐次项。后两项由 (15) 被杀；另一方面其完整 period 变化为 $2\kappa L_f(w)$，没有左二次项。将 (12) 用于完整 forcing 差，准确得到

$$
\boxed{\int_B k(s)\mathcal B_\theta(w)(s)\,ds=0.}
\tag{16}
$$

因此 (14) 不是能用另外一条 ruling 校正随后支付的遗留数值：若其中一个原值非零，全部允许的二、三阶 gauge 都不能消掉它。本文没有评价它的值，也没有把 k 视为非负权或把这个泛函与 R196 的 universal 正字符等同。

pure 身份只说明 $\int kK^0_\theta$ 的相位四次谐波已为零；它不由自身推出 (14) 中剩余两个 mixed 数值为零。

## 5. 原八 packet 使八矩生成的二阶 gauge 全部合法

令 E 为任意固定实八矩算子，采用 R73 的规范

$$
\Phi_E(a,b)=A_0ab+\frac{A_1}{2}(ab'+a'b)+A_2a'b'
+B_0J_0+B_1J_1+B_2J_2^*.
\tag{17}
$$

其系数满足

$$\deg A_0\le1,\quad\deg A_1\le2,\quad\deg A_2\le3,
\quad\deg B_i\le2.$$

取

$$\boxed{w_{E,\theta}=\Phi_E(D_\theta).} \tag{18}$$

**命题 2。** 对 R183 的同一八完整 packet 圆，(18) 光滑、双 collar 为零，随相位光滑周期且两个种子为零，并准确满足

$$\mathbf m(f,w_{E,\theta})=\mathbf m(g,w_{E,\theta})=0.$$

**证明。** 先看一个三矩配平的基本 pair。$D_\theta$ 的三个总矩为零，故 (17) 的三个右尾在该基本 packet 左方全零；右方由锚也为零。局部项本来支撑于该 packet。因此 $\Phi_E(D_\theta)$ 真正紧支撑于其完整包络。

对平移 $t$ 的 packet 写回原坐标 y。局部系数的 t 次数至多三；
$J_0$ 不新增 t，$J_1$ 至多一次，$J_2^*$ 至多二次。连同 $B_i(y+t)$，(17) 的完整 t 次数至多四。求 y 导数不增 t 次数。

于是 $m_0(f_t,\Phi_ED_t)$、$m_1$、$m_2^*$ 分别是 t 次数至多四、五、六的多项式；g 同样。对八包的准确幅度

$$a_j=(-1)^j\binom7j^{1/3},\qquad t_j=t_*+jL,$$

各矩按 $a_j^3=(-1)^j\binom7j$ 相加。第七有限差分同时消掉全部六个矩。不同完整 packet 的交叉项为零，正是因为上一步已经支付了 $\Phi_ED_t$ 的完整左尾；不是凭导数分包删除历史。最终共同仿射坐标或统一幅度仍保持这些零条件。相位和种子性质由 (2) 的线性性直接给出。证毕。

## 6. 这一合法 gauge 子族恰是 hook 响应的固定圆像

R83(11) 的完整原响应为

$$
\begin{aligned}
K_{E,\mathfrak H}(F,\phi)={}&
2\mathfrak H(\Phi_ED;D)
-4\mathfrak H(\phi;\phi,\Phi_ED)\\
&+4\Phi_E(\phi,\mathfrak H(\phi;D)).
\end{aligned}
\tag{19}
$$

R183 已证明 $\mathfrak H$ 在 f、g 平面的三个槽上全零。特别地
$\mathfrak H(\phi;D)=0$，但不能在涉及 $\Phi_ED$ 的槽上直接置零。
对这些槽用 R180 的准确循环身份，前两项恰化为

$$
2\mathfrak H(\Phi_ED;f,f)=2L_f(\Phi_ED).
$$

所以

$$
\boxed{K_{E,\mathfrak H}(F,\phi_\theta)
=2L_f(w_{E,\theta}),\qquad
\Delta V_\theta=\kappa K_{E,\mathfrak H}(F,\phi_\theta).}
\tag{20}
$$

任意有限实线性组合可直接在同一固定几何和同一第一圆上用相应 w 的线性组合实现；这里不需要另加带未知第四基准的几何控制词。维数至多八，没有声称八个方向在这个圆上独立。

另一方面，(19) 的 universal 响应本来属于 R105 的 $\mathcal R$，其 pure 由 $\mathfrak H(q;q,q)=0$ 恒为零。故本节这族独立二阶 gauge 的 period 恰有一个 canonical 响应代表；任何已良定义且杀 $\mathcal R$ 的 universal 泛函都杀这个代表。不能借 (20) 宣称该泛函对所有其他独立 w 自动延拓，也不能把它直接当作单个固定圆上的评价泛函。

由 (20)，平台门 (10)、左二次尾门 (14) 和 R181 的通量门对这一整个八矩子族均准确不变。这里的通量门仅指 R181 对全部合法全 I gauge 的端点／退化通量恒等，不指 R211 人为限定 J 支撑后附加的所有局部矩对全局 w 都不变。这说明单纯加入这些已经可表示为 hook 响应的 gauge 不会修复其原值若有的违例。

## 7. 下一真正未付的数据

现在的固定圆任务可以直接使用 (4)、(13) 的真实已付三阶场：先确定内部 f 常值平台上的 $V_d''、V_e''$，以及两个全周期数 $\int kK_d、\int kK_e$。这些是具体原 forcing 的函数或积分，不是一次新的 universal pure 分类，也无需恢复旧响应列来定义。

若任一门严格失败，则 R184 的全部二阶/三阶 gauge 不能使该固定几何、同一目标和同一圆通过完整第四 range。若这些门通过，仍须求同一 w 的完整 period 与 ruling 商方程；R211 只在其已说明的支撑和退化范围内提供准确 Green 右逆。

本文没有从“最后一个右段自动为零”推到内部重叠段为零，没有从合法八矩子族推到全部 period 像，也没有从一个 ruling 商泛函消失推到整个 ruling 商消失。R210 的整 pure 支付是这里的已付起点，完整 mixed、逐 ruling、更高阶及有限等距族仍分别保留。
