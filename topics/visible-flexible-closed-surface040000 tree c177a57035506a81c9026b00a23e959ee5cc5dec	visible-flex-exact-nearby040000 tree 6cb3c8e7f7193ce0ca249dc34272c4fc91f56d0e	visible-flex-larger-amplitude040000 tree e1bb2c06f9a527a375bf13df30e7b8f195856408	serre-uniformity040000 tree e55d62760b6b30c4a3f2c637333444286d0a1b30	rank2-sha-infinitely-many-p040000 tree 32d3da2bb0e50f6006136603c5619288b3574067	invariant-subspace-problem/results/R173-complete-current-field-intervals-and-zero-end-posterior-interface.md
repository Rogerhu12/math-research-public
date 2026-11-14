# R173：准确域上完整有限场的区间包围与零端原函数后验接口

**状态：已证明；计算定义与连续包围接口已实际消费。**
2026-11-12，fd2d / metric_closure。

这里接通当前独立布局 `central31 / tail16 / physical-bumps7`、保存的 131 个
P1 节点、R149 整函数图谱、完整 affine lifting、R153 与 R155 变换、
R171 准确物理度量和 R172 准确末格。它给出了这些**完整函数**的实际区间
消费者，以及将其三个 Gauss–Codazzi 缺陷送入 R125 的接口。

这不是当前非线性候选已经满足全域误差的结论。下面实际消费的输入为
`notes/2026-11-12-fd2d-raw-bump-grouped27-trial-back00-a01-accepted.npz`，
SHA256
`2b65810c5c09985d54544e6ca697ee609f066a17ecbce4b83e89adad0b52ae6f`。
它仍是未完成的强目标候选。局部完整区间、连续全域覆盖、实际图的后验与
最终闭面几何是不同结论，本结果只在明确支付的范围内作断言。

## 1. 准确对象与声明

保存的节点、Fourier 系数、54 个参数和各窗端点均作为其 binary64 字节所
表示的**准确有理数**读取。中央、尾与物理参数的分段由保存的独立布局给出，
不重新按 `K+1` 猜测尾参数数目。原数组、原求解器和所有已经闭存的消费者
保持不变。

物理度量是 R171 准确定义的

\[
g=ds^2+a(s)^2du^2,
\qquad a=a_{\rm phase}+\sum_{j=1}^7\delta_j\psi_j.
\tag{1}
\]

这里相位原函数、准确初始半径、连续累计长度以及原始共享 Hermite 数据均由
R171 packet 绑定；\(\psi_j=1024q^5(1-q)^5\) 在准确保存支持内定义，外部为零。
R175 只用同一多项式的 Bernstein 控制点收紧区间包围，没有改变 (1) 或其
任何导数。运行时旧的 40 点浮点半径积分不被当作 (1) 的准确定义。

记原保存末端为 E、倒数第二个节点为 b、准确物理末端为 S。当前有

\[
E=1.4889731783581288\quad\text{的准确 binary64 值},
\quad b=1.4873481783581288\quad\text{的准确 binary64 值},
\]

\[
S-E\in[1.1873403225247744,1.1873403225247746]10^{-15}.
\tag{2}
\]

最后一个物理单元使用 R172 的明确新表示，见 §8；它不是把 E 静默改名为 S。
原 finite F、旧浮点 body 和旧节点误差不自动转移到这个新有限表示。

**区间接口命题。** 对每个声明的 P1 单元、实际图谱侧、径向区间和角区间，
下文消费者若返回有限 jets 并成功支付所请求除法的正下界，则每个返回区间
包含所声明完整函数在该盒上的真值或真单侧导数。角区间可以有正宽度，
不是有限角抽样。若完整集合覆盖了某个区域，逐盒上界的最大值覆盖该区域。
本命题不声称当前输入已对全部区域成功运行，也不以有限样本下界替代除法
的连续正性。证明由 §§2–10 逐项给出。

## 2. 全 seed 角函数与有限包围表示

原准确 balanced seed 的曲率半径记为 \(\rho(\xi)\)，周长归一常数为 \(a_0\)。
其完整定义为已闭矩包中的

\[
\rho=r+\frac D2\{1-\tanh[k(\cos2\xi-c)]\}
       +u_0+u_2\cos2\xi+u_4\cos4\xi .
\tag{3}
\]

\(r,D,c,k\) 是准确有理输入，\(a_0,u_0,u_2,u_4\) 由原区间矩包给出。
令 \(h=\rho/a_0\)。完整材料角 \(U_*(\xi)\) 满足

\[
U_*(0)=0,\qquad U_*'=h,
\qquad U_*(\xi+2\pi)=U_*(\xi)+2\pi.
\tag{4}
\]

消费者对值使用已闭 512 模包

\[
U_*(\xi)\in\xi+\sum_{j=1}^{512}\frac{\widehat\mu_j}{j}\sin(2j\xi)
                    +[-\varepsilon_0,\varepsilon_0].
\tag{5}
\]

这里 \(\widehat\mu_j\) 是保存准确 dyadic 区间两端的有理中点；
\(\varepsilon_0\) 是已付无限尾、离散混叠和系数代表误差的总界，
小于 \(1.331\cdot10^{-18}\)。角一、二导直接用 (3) 的
\(h,h'\)，而不把截断的 (5) 当成新的材料角。原完整 C4 chart 包与矩包的
SHA、未压缩 SHA 和全部模式顺序均被核对。因此 (5) 与导数来自同一个
准确函数，不是互不相干的近似值与近似导数。

冻结入口 \(n_c,m_c\) 使用实际保存的全部有限余弦/正弦系数。求
\(k=m_c/n_c\) 时连同其前三个 \(\xi\) 导数作准确商法则；从
\(k_t=k_\xi/h\) 再求两阶 \(\xi\) 导数。这些导数来自明确有限 Fourier
函数与 (3)，没有通过差分提供额外正则性假设。

## 3. 冻结 ruling 全函数和全角正向性

记已绑定冻结入口半径和斜率为 \(a_c>0,v>0\)，入口位置 e，出口位置 f。
它们和入口 Fourier 系数都与当前未知 \(\delta\) 无关。令

\[
\sigma=s-e,\quad r_0=a_c/v,\quad r=r_0+\sigma,
\quad \Delta=\sigma(2r_0+\sigma),
\]
\[
Q=\sqrt{r_0^2+(1+k^2)\Delta},\quad
w=\frac{\Delta}{r_0+Q},\quad
B=v(1+k^2)-k_t,\quad D=a_c+wB.
\tag{6}
\]

R139/R149 的完整 ruling 图谱与参考场是

\[
N(s,\xi)=U_*(\xi)-\frac1v\arctan\frac{kw}{r_0+w},
\qquad
n_R=\frac{a_c n_c Q^2}{Dr^2},
\tag{7}
\]
\[
q_R=\frac{k r_0}{Q},\qquad m_R=n_Rq_R,\qquad l_R=n_Rq_R^2.
\tag{8}
\]

直接微分 (6)–(7) 得到关键准确相消

\[
N_\xi=\frac{Dh}{vQ}.
\tag{9}
\]

实现先用 (9) 计算这个导数及其 \(s,\xi\) 导数，再进行区间包围；
同时保留直接微分 atan 的恒等式差供小核。它没有把 (7) 改成别的图谱。

### 3.1 准确出口与旧数值 shortcut

原数值 reader 在闭出口使用 \(\sigma=L_{\rm saved}\) 的 shortcut。
当前准确保存的标签满足

\[
(f-e)-L_{\rm saved}=2^{-54}.
\tag{10}
\]

R149 明确规定后续完整函数是 \(E(\xi)=N(f,\xi)\)。因此本消费者在闭 coast
上一律用 \(\sigma=s-e\)，并用同一个 \(N(f,\xi)\) 作出口延拓。
这给出一个共同准确角迹；(10) 作为旧数值求值误差的来源单列，不能同时
声称保留旧数值 guard 又把两者准确相等。

### 3.2 已有全角证明的准确扩展

原 R139 的 209 个闭区间无缝覆盖完整四分之一角圈，精确 D2 对称给整圈。
消费者核对全部角区间端点、入口、候选、矩包与三个标量输入。
原包已付 \(n_c\ge n_*>0\)、\(\rho\ge\rho_*>0\) 及 D 的端点下界。

对固定角，\(w\) 随 \(\sigma\ge0\) 单调，而 \(D=a_c+wB\) 关于 w 为仿射，
所以在旧段 \([0,L_{\rm saved}]\) 上

\[
D\ge\min(a_c,D(L_{\rm saved},\xi)).
\tag{11}
\]

又由 (6)

\[
w_\sigma=\frac{r}{Q}\le1+\frac{\sigma}{r_0}.
\tag{12}
\]

设 \(\epsilon=\max(0,f-e-L_{\rm saved})\)。将原 D 下界减去

\[
\epsilon\left(1+\frac{\max(f-e,L_{\rm saved})}{r_{0,\min}}\right)
          \sup_\xi|B|
\tag{13}
\]

仍是准确闭 coast 上的下界。实际输入给出的下界严格正。
再以完整有限 \(m_c\) 系数绝对和控制 k、以 (6) 控制 Q，得到 (9) 的严格
正下界。它只证明**冻结图谱与参考场**的合法性，没有推断当前未知 raw 场
的 n 为正。

所有把局部自然区间与这些全角下界相交的操作，都是与已独立证明的有效
包围相交；不是凭一个正的样本修正除零盒。

## 4. 完整 R149 atlas 的值、两jet 与侧迹

令旧完整图谱为

\[
U_o(s,\xi)=\xi+(1-\beta(s))(U_*(\xi)-\xi),
\tag{14}
\]

其中 \(\beta\) 是原保存端点上的 clamped quintic。新准确图谱依次为

\[
U=\begin{cases}
U_o,&s\le e_0,\\
(1-q_e)U_o+q_eU_*,&e_0\le s\le e,\\
N(s,\xi),&e\le s\le f,\\
(1-q_f)N(f,\xi)+q_f U_o,&f\le s\le f_1,\\
U_o,&s\ge f_1.
\end{cases}
\tag{15}
\]

\(e_0=.55,f_1=1.4\) 及 e、f、\(\beta\) 的端点都使用各自保存 binary64
有理数，不重新把十进制外观当作准确替代。\(q_e,q_f\) 为指定区间上的
clamped \(S_5(t)=t^3(10-15t+6t^2)\)。

每个角导 \(U_\xi\) 是正向旧函数的凸组合，或是 (9)。因而

\[
U_\xi\ge\min(1,h_{\min},N_{\xi,\min})>0.
\tag{16}
\]

各函数均有度数一的周期提升，所以每个 s 上 \(\xi\mapsto u=U(s,\xi)\)
是整个材料角圈的正向双射。全角 supremum 可以在 native 角上取，不需要
数值反解材料角。

在 e 处 \(\sigma=0,w=0\)，(7) 给 \(N(e,\xi)=U_*(\xi)\)；在 f 处后续
定义就是同一个 \(N(f,\xi)\)。因此 (15) 的值、一阶与二阶角导共同迹
**按完整函数恒等**匹配。\(U_s,U_{s\xi},U_{ss}\) 可以有明确的侧限差。
实现的 `left/right/coast/both` 选择返回相应一侧或并集，不把径向跳跃置零。
跨图谱界的正宽盒逐片求值再取 hull。

`TwoJet` 用
\((f,f_s,f_\xi,f_{ss},f_{s\xi},f_{\xi\xi})\)
存储真实导数。乘法与一元复合采用完整二阶链式法则。上述图谱和参考场只由
已列出的准确函数组合而成，故普通区间包含性归纳给出各 jet 的连续盒包围。

## 5. 准确 R132 尾函数及完整 affine lifting

尾几何统一采用

\[
a_{\rm cut}=4/5,\qquad c_*=17/50,\qquad w_*=23/50.
\tag{17}
\]

原浮点 `.8`、`.34` 或它们浮点相减的结果不替代这些有理常数。16 个实际
Bernstein 控制仍为原保存 dyadic。令

\[
P(q)=\sum_{j=0}^{15}b_j\binom{15}{j}q^j(1-q)^{15-j},
\]
\[
\kappa(y)=
\begin{cases}
\dfrac{630}{w_*}q^4(1-q)^4P(q),
 &c_*<|y|<a_{\rm cut},\quad q=(|y|-c_*)/w_*,\\
0,&\text{其余}.
\end{cases}
\tag{18}
\]

四阶端点零因子使扩展至少 C3；因此这里所需两jet在夹界也由两侧公式及
零函数的并集合法包围。计算不删除任何尾控制：内部用 de Casteljau 或
R172 同一个完整多项式，正负 y 支分别限制其值区间后保留全部真实链式导数。

完整尾 shape 在计算角上是

\[
T(a,U)=\bigl(\kappa(a\sin U)\cos^2U,
 -\kappa(a\sin U)\sin U\cos U,
 \kappa(a\sin U)\sin^2U\bigr),
\tag{19}
\]

分量顺序一直是 \((n,m,l)\)。这里 a 是 (1) 在**当前物理 s**的准确值。

令 \(w_c\) 为原中央 seed 窗、\(\eta\) 为原尾窗、\(w_R\) 为原两侧
clamped quintic 的 coast 窗。全部准确标签来自 native definition。
完整已知 lifting 是

\[
L=(1-w_R)\{w_c(n_*,0,0)+\eta T(a,U)\}
          +w_R(n_R,m_R,l_R).
\tag{20}
\]

balanced seed 时 \(n_*=1/\rho(\xi)\)，圆 base 时为 \(1/a_0\)。中央 seed
活动处图谱本来就是固定 seed 图，因此此式也是原完整材料函数。
实际中央变化系数已位于原 raw 数据中，不再凭新曲线重构或丢掉它们。

参考 (7)–(8) 只在其 coast 支持内求值。窗及其所需端导准确为零时，不求一个
未定义的域外参考再乘零。一般跨窗盒使用支持内参考与完整窗导的区间乘积，
得到有效包围。

## 6. 完整 raw、R153 与 R155 的条件包围

在原保存单元 \([s_j,s_{j+1}]\) 上，raw coefficients 按准确 P1 插值。
完整 31 模余弦/正弦和在区间角上求值；其径向导是这个明确单元的单侧斜率。
将它加到 (20)，得到背景三场 \((n_b,m_b,l_b)\)。

R153 是完整函数变换

\[
n_1=n_b,\quad m_1=m_b,\quad
l_1=(1-w_R)l_b+w_R\frac{K+m_b^2}{n_b},
\qquad K=-a_{ss}/a.
\tag{21}
\]

只在活动窗上要求真实 \(n_b>0\)。消费者必须从所查询的连续盒证明这个
下界；旧数值 floor 或 R164 对另一输入的结论不能代替它。

末正迹窗使用原保存 \(w_T\) 及

\[
H_T=\sqrt{(n_1-l_1)^2+4m_1^2+4K},\qquad
e_T=\tfrac12w_T(H_T-n_1-l_1),
\tag{22}
\]
\[
(n,m,l)=(n_1+e_T,m_1,l_1+e_T).
\tag{23}
\]

活动内部盒要支付 \(K\ge0\) 及 \(H_T>0\)。准确 cut 的退化例外只由 §8
的真实尾迹处理，不能用一个数值 bypass 给内部导数赋零。

完整 jets 对 (21)–(23) 使用原有商法则、乘积和开方链式法则。
一般 \(l_s,l_{s\xi}\) 真正需要 \(K_s\) 时，使用 R171/R175 的实际单侧

\[
K_s=-a_{sss}/a+a_{ss}a_s/a^2.
\tag{24}
\]

Codazzi 中 coast 的 \(l_u\) 本身不需要 \(K_s\)。给通用 jet 的 (24)
来自本题明确分片函数，而不是给完成标准追加全局 C3 要求。

若区间依赖使上述分母包含零，输出 `UnresolvedInterval`，不推断候选真的
有奇点。R175 的替代范围算法只减少这类包围宽度，不改变 (21)–(23)。

## 7. 三个完整缺陷与物理材料导数

对任一 native jet \(f(s,\xi)\)，置 \(h_U=U_\xi\)、\(v_U=U_s/U_\xi\)。
准确物理导数是

\[
f_u=f_\xi/h_U,\qquad
f_s\big|_u=f_s\big|_\xi-v_Uf_\xi,
\tag{25}
\]
\[
f_{uu}=\frac{f_{\xi\xi}-f_uU_{\xi\xi}}{h_U^2},
\tag{26}
\]
\[
f_{su}=\frac{f_{s\xi}-v_Uf_{\xi\xi}}{h_U}
 -\frac{f_\xi(U_{s\xi}-v_UU_{\xi\xi})}{h_U^2}.
\tag{27}
\]

它们由在 \(u=U(s,\xi)\) 上保持 u 求导直接得到。图谱径向跳跃时，在每个
已声明侧分别使用真 \(U_s\)，不把 coast 自然标签当作固定材料 u。

所有连接缺陷均用 (25)：

\[
G=ln-m^2-K,
\quad R_n=n_s|_u-m_u/a-(a_s/a)(l-n),
\tag{28}
\]
\[
R_m=m_s|_u-l_u/a+2(a_s/a)m.
\tag{29}
\]

R119 的完整反对称强迫向量和径向连接向量是

\[
\mathbf H=(-aR_n,\ aR_m,\ -aG),\qquad
\alpha=(m,-l,0).
\tag{30}
\]

没有因为某个窗口精确 Gauss 就删除第三分量，也没有用求解器的节点 Gauss
或单元求积残差代替 (28)–(30)。该接口只需 \(n_s,m_s,m_u,l_u\)，不会为
R119 本身强求全局 \(l_s\)。

**包围证明。** 每个输入区间包含准确常数或准确函数；三角/双曲/开方等
Arb 运算给实区间包含，有限和、乘积、已付非零分母的除法保持包含。
分片限制与并集覆盖每个实际分支。二jet逐项正是通常链式法则；(25)–(30)
为准确代数恒等式。因此输出包含每个声明点的真实 jet 和全部三缺陷。
这证明 §1 的接口命题；整个证明不使用任意有限角网格上的最大值。

## 8. 准确域末格与拼接范围

在完整最后物理单元 \([b,S]\)，R172 令

\[
s=b+(S-b)t,\qquad \sigma=b+(E-b)t,\qquad 0\le t\le1.
\tag{31}
\]

raw 和尾标量窗以旧标签 \(\sigma\) 求值，物理尾 shape 和 Gauss 量仍在 s：

\[
\mathcal B(s,u)=C(\sigma,u)+\eta(\sigma)T(a(s),u),
\qquad \text{R155 使用 }K(s).
\tag{32}
\]

整个末格的 seed/coast/bump 为零、图谱为 identity、trace 窗为一，均由实际
保存端点和 R171 准确片位置检查。特别地，(32) 不是
\(T(a(\sigma),u)\)。

在 b，\(\sigma=b\)，(32) 与左侧完整 affine 函数的值和角两jet相同，
随后同一个 R155 角函数亦相同。径向 raw 斜率含
\((E-b)/(S-b)\)，可以与左侧有真实小跳；本结果不声称径向 II 导数在 b
相同。连续 II 值和角迹足以按 R141 的分片理论继续处理实际重建。

在准确 cut，\(C(E,u)=0,\eta(E)=1,a(S)=4/5,K(S)=0\)。由真实 R132
PSD rank-one 尾得到值、\(u\)、\(uu\) 角迹。这里不赋 \(e_{T,s}=0\)，也不
给 cut 径向 II jet。一个包含 cut 的一般开方导数盒若未支付单侧退化估计，
仍明确 unresolved；R174 可另供该估计，真正 Cartesian 两jet接合仍按 R126。

新 wrapper 对所有单元提供 `cell_box(cell,tlo,thi,...)`。t 只是查询标签，
返回导数始终是物理 s 和 native 角导。最后单元使用 (31) 的真长度；之前
单元使用原准确有理 P1 长度。因此不会在 \((E,S]\) 留下隐藏域缺口。
`box(cell,slo,shi,...)` 只允许原末格之前的物理有理区间，避免两种坐标
语义混用。

## 9. R125 零端 primitive 的完整输入

取某一真物理单元 \([a_j,b_j]\)，长度 \(L_j=b_j-a_j>0\)，并以
\(t=(s-a_j)/L_j\) 定义明确有限向量多项式

\[
P(t,\xi)=\sum_{d,k}t^d\{c_{dk}\cos2k\xi+s_{dk}\sin2k\xi\},
\tag{33}
\]

其三分量对应完整 (30)，系数都是保存准确有理数。它可以由数值样本拟合
产生，但拟合过程不提供任何默认误差结论。令

\[
\bar P(\xi)=\int_0^1P(t,\xi)\,dt,\qquad
q(s,\xi)=L_j\int_0^t(P(z,\xi)-\bar P(\xi))\,dz.
\tag{34}
\]

准确有

\[
q(a_j,\xi)=q(b_j,\xi)=q_\xi(a_j,\xi)=q_\xi(b_j,\xi)=0,
\qquad q_s|_\xi=P-\bar P.
\tag{35}
\]

对原有理单元，系数原函数的恒等式由有理数算术逐项确认。对 R172 最后
单元，\(L_j=S-b\) 不是用浮点中点定义，而是由 R171 准确 S 定义的
常数；先构造单位单元准确 \(q_{\rm unit}\)，再令
\(q=L_jq_{\rm unit}\)。因此 (35) 仍是准确恒等式。区间中只用真实长度的
Arb 包围来求值，没有把“带宽度区间”当成一个任意选择的多项式系数。

将 \(\widehat q\) 用于 R125 的
\(D=F_u-FB\)、\(W=D-F\widehat q\)。沿固定物理 u，

\[
q_s|_u=P-\bar P-v_Uq_\xi.
\]

由 R125 已证明的矩阵恒等式得到完整有效强迫

\[
\boxed{\mathcal E=\bar P+(\mathbf H-P)+v_Uq_\xi+q\times\alpha.}
\tag{36}
\]

消费者对准确完整字段 (30) 与准确 P 作区间相减，实际付出 \(\mathbf H-P\)
的盒范围；漂移和交叉乘积都保留。若以后以系数层相消得到更紧余项，必须
绑定同一个完整字段和同一个 P，不能偷用旧 `NativeLogField` 包。

若完整单元上有真实连续上界
\(e_j\ge\sup|\mathcal E|\)、\(q_j\ge\sup|\widehat q e_1|\)，则 R125 给

\[
d_{j+1}\le d_j+L_je_j,\qquad
k_{j+1}\le k_j+L_jd_j+\tfrac12L_j^2e_j+L_jq_j,
\tag{37}
\]

以及 \(2(k/a)+(k/a)^2\) 的真实诱导度量界。\(q\) 在每格两端准确消失，
所以可以逐格拼接，无需额外跨格 C1 primitive。初始 \(d_0,k_0\)、全部盒
覆盖、退化 cut 的可积范围及最后真实图仍须另付；本接口不把这些设为零。

## 10. 实现与身份

完整实现分为三个已经实际执行并闭存的独立模块：

1. `scripts/fd2d_gc_current_frozen_atlas_arb.py`：准确 seed、冻结 ruling、
   完整 atlas 六jet、原全角正向性包与 (10) 的准确出口语义。
2. `scripts/fd2d_gc_current_complete_field_arb.py`：原保存内部的完整 raw、
   affine、R153/R155、物理链式和三缺陷；准确有理尾常数。
3. `scripts/fd2d_gc_current_accurate_domain_arb.py`：可选 R175 同函数范围
   backend、R172 整个准确末格，以及以真实单元长度定义的
   `ExactNormalizedCellPrimitive`。

这些模块复用已冻结的
`fd2d_gc_current_native_interval.py`、
`fd2d_gc_current_primitive_interval_v2.py`、
R171、R172、R175 与原 archive reader。实际保存 mesh、中央/尾/物理切片、
全部 window/atlas/native 定义、物理 target packet 和所有 source SHA 都进入
definition 或完整输入绑定。本层输入 identity 明确携带字节数与 SHA；已有
definition 的绑定原样保留。迁移时须保留原定义或明确重建绑定，不能仅因
新位置文件同名就判定数学输入相同。

## 11. 实际小消费与真实失败记录

第一轮检查器对恰在保存 P1 节点的实际样本取对称小盒，盒越过其声明单元，
按明确检查真实 exit1。数学源未改。失败报告和 receipt 为

`notes/2026-11-12-fd2d-metric-current-complete-arb-01-{report,completion-receipt}.json`。

另名 v2 检查器只把盒截到所选真实单元，保留正宽度和原样本。
它于 session `77341`、final chunk `9eb94f` 真实 exit0，
耗时 `0.516585870002018 s`、峰 RSS `92652 KiB`。结果

`notes/2026-11-12-fd2d-metric-current-complete-arb-02-report.json`

包含：10 个实际点共 150 项五jet比较、10 个正宽连续盒、4 个完整 atlas
共同角迹、3 个冻结 ruling 的完整 Gauss–Codazzi 恒等式、4 个准确有理
cut 角迹，以及一个实际非零 P 的完整 (36) 小盒。
准确函数区间减去旧浮点点值的最大绝对上界为
`2.349174980954546e-11`，除以 `1+|旧值|` 最大为
`7.464641120261316e-12`。这只是这些实际点的数值比较，不是旧浮点程序的
全域误差界。

准确域 wrapper 于 session `1030`、final chunk `d076db` 真实 exit0，
耗时 `0.6937043269972492 s`、峰 RSS `92796 KiB`。结果

`notes/2026-11-12-fd2d-metric-current-accurate-domain-01-report.json`

包含 3 个使用 R175 的完整内部小盒、b 处三个分量的值/角两jet共同迹、
末格内 3 个真实强迫点、准确 cut 的明确作用域，以及一个真实长度
\(S-b\) 的非零 primitive 连续小盒。两端 q 与 \(q_\xi\) 准确零已实际消费。
包含 cut 的一般导数盒按其真实未付范围返回 unresolved，没有因检查器
需要通过而删掉这个例外。

两个非零 primitive 小盒的 \(|\mathcal E|\) 上界分别约
`0.3714203541` 与 `0.9163274377`。它们是完整链路及真实大残差的可重做
实例，不是小度量证书。没有计算 whole F/J、没有求 BVP，也没有重跑 body。

## 12. 已补齐与仍未支付

已补齐的是：准确 radial target、完整 raw/affine 函数、全材料图谱、
真实窗及全部 tail 控制、R153/R155 条件两jet、完整物理三个缺陷、
准确末格域，以及保留 (36) 全部项的零端 primitive 接口。

仍需针对最终实际候选支付：活动 coast 的全域 n 下界；真实完整 forcing
polynomial 与逐盒余项覆盖；退化 cut 的单侧可积预算；准确中央曲线/标架的
初始相容缺陷；累积 R119/R124/R125 后验；实际 Cartesian 接缝与全闭面几何。
其中任何一个未付项都不以当前 finite objective、局部检查或旧场结果代替。

Arb 的 midpoint/radius 包围语义及准确包含运算依据官方
[python-flint Arb 文档](https://python-flint.readthedocs.io/en/latest/arb.html)。
本文其余等式、包含性与归一长度原函数的证明均已在上文给出；使用的既有
数学结论分别明确引用 R119、R125、R139、R149、R171、R172 和 R175。
