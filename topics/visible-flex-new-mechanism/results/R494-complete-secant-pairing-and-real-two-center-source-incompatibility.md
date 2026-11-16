# R494：完整正割三槽恒等式、真实双中心规范不变量与非零矩阵桥

日期：2026-11-16。**完整原式纸面证明；没有执行新的符号、profile、积分、原根恢复、rank、开发检查或科学计算。**

[R492](R492-the-original-thirteen-row-gauge-locks-secant-odd-ruling-and-real-prefix-compatibility.md) 已把当前偶母库的正割奇行在整个 period 核上识别为原四个端口行的组合。它仍留下两个不同的问题：任意真 particular 的 source 商如何进入；真实连接桥改变二阶前缀时，完整 source 是否总会自动补偿。

本稿给出一个不需要重新求 particular 的严格推进。原 secant 的三槽 pairing 对任意紧输入有一个完整低阶式，而不只在对角母列上成立。由此，两个具有同一物理平移参数 \(\omega\)、可以有不同高度 \(H\) 的真实正割中心，其奇 ruling 之差准确消去同一个第二规范、整个 period source 和任意真实第三 incoming。余量只读两中心之间的原 \(M_{\rm raw}\) 积分。

对 \(P=\Phi_{r_0}\) 方向，该不变量可以完全计算。全部单包左常数与跨包有序尾合成原合法矩的平方，先保留再准确抵消；在当前全 \(W\) outer 库上，余量对 \(\omega\) 的导数是一个非负四次幅和，且在 \(\theta=\pi/2\) 严格等于 \(\int(g'')^4>0\)。因此这条真实前缀读出并非自动为零。原 R70 的有限矩阵桥能实际产生两号的前缀差；后续完整成本基准并不被删除，也不能补掉这个双中心差。

这是对一类明确真实路径的必要兼容与非零见证。它没有排除单正割段、不同 \(\omega\) 的一般路径、其它受约束状态族或整个主问题。

## 1. 同一个真实场、规范与原积分

使用 [R488](R488-real-secant-height-patches-and-complete-same-gauge-ruling.md) 的真实正割段：
\[
 k=0,\qquad \omega=\omega_0,\qquad
 y=x+\omega_0>0,\qquad
 h=H\sqrt{1+v^2},\qquad v_s=1+v^2,\qquad h_s=hv .
 \tag{1}
\]
其中 \(H>0\)，原物理区间 \(I=[x_-,x_+]\) 和 profiles 不动。
\(y\) 只是同一物理坐标的一次记号替换。右积分为
\[
 Jb(y)=\int_y^{x_++\omega_0}b(t)\,dt.
 \tag{2}
\]
不能对不同微包另置右锚，不能删除真实左尾。

沿该段的完整二阶历史为
\[
 \mathsf A_s=\mathsf A_*+\mathsf A_{\rm sec},\qquad
 \mathsf A_{\rm sec}=-\frac{v}{8h^2}R_y-\frac v8 T_y .
 \tag{3}
\]
若段内包含 \(v=0\)，\(\mathsf A_*\) 就是该中心从整个实际词起点累计而来的原值。它没有被重新设成零。

原二次方向按 R259/R469：
\[
 P(u,u)=J((u'')^2),\quad
 R_y(u,u)=(u')^2+yJ((u'')^2),
\]
\[
 T_y(u,u)=y^2(u')^2+yJ(y^2(u'')^2+2(u')^2).
 \tag{4}
\]
此处 \(T_y=\Phi_{t_1}\) 是一个二次基方向，不是整个第三 period。

完整 physical 配对为
\[
 \mathcal E_s(a,b)=\frac{I_0^y(a,b)}{4h}+\frac h4 I_2^y(a,b),
 \quad I_2^y(a,b)=\int(y^2a''b''+2a'b').
 \tag{5}
\]
尤其不省去 \(2a'b'\)。

固定一个真实圆
\[
 \phi_\theta=f\cos\theta+g\sin\theta,\qquad
 D_\theta=f\odot f-\phi_\theta\odot\phi_\theta .
 \tag{6}
\]
所有 profiles 及下文另称紧输入的函数均在同一两个 collars 上平零。任意单个 \(P,R_y,T_y\) 输出则可以有真实左多项式尾。

## 2. 任意外槽的完整三次恒等式

设 \(u,c\) 为任意真实紧 profiles，记
\[
 p=u',\qquad r=u'',\qquad t=u''',\qquad L=p-yr,
\]
\[
 P_u=J(r^2),\qquad C_u=J(y^2r^2+2p^2).
 \tag{7}
\]

**定理 1。** 在(1)的整个真实段上，
\[
 \boxed{
 \mathcal T_s(c;u,u)
 -\mathcal E_s\{c,\mathsf A_{\rm sec}(u,u)\}
 =-\frac{v}{4h}\int c(p-yr)t .
 }
 \tag{8}
\]
它适用于任意外槽 \(c\)，不要求 \(c=u\)，不要求 \(c\in\ker L_f\)，也不使用偶母、三矩闭合或原十三行。原 \(\mathcal T_s\) 是 R221/R469 的完整同锚 local pairing；(8)不是 principal 近似。

### 2.1 原式分成三个准确幂层

把 R469(26) 直接代入 \(e=hy,\gamma=hv,e_s=hvy\)，提出公共因子 \(v/(32h^3)\)。原 local 项按 \(1,h^2,h^4\) 的三个积分依次记为 \(A_0,A_2,A_4\)。在本节此下标与 cap 的八个 \(A_j\) 无关。直接得到
\[
 A_0=\int\{c'''(2pr-yr^2)+c''r^2\},
 \tag{9}
\]
\[
 A_2=\int\{c'''W_2-2p^2c''-2yr^2c'+2r^2c\},
 \quad
 W_2=4y^2pr-2y^3r^2-2yp^2,
 \tag{10}
\]
\[
 A_4=\int\{c'''W_4-(y^2c''-2yc'+2c)(y^2r^2+2p^2)\},
\]
\[
 W_4=2y^4pr-y^5r^2-2y^3p^2.
 \tag{11}
\]

另一方面，(3)(5)给出完整能量项
\[
 -\mathcal E_s(c,\mathsf A_{\rm sec}u^2)
 =\frac{v}{32h^3}
 \{I_0^y(c,R_yu^2)+h^2[I_2^y(c,R_yu^2)+I_0^y(c,T_yu^2)]
   +h^4I_2^y(c,T_yu^2)\}.
 \tag{12}
\]
因此只需分别相加这三个原层，不从 diagonal 极化猜外槽。

### 2.2 零次与四次项完整抵消

原 derivatives 为
\[
 (R_yu^2)'=2pr+P_u-yr^2,\qquad
 (R_yu^2)''=2Lt,
 \tag{13}
\]
\[
 (T_yu^2)'=2y^2pr-y^3r^2+C_u,
\]
\[
 (T_yu^2)''=4ypr-2y^2r^2-2p^2+2y^2Lt.
 \tag{14}
\]
由 \((2pr-yr^2)'=2Lt+r^2\)，一次紧外槽 IBP 给
\[
 A_0=-I_0^y(c,R_yu^2).
 \tag{15}
\]

四次项同样保留 \(C_u\)。直接微分
\[
 W_4'=4y^3pr-3y^4r^2-6y^2p^2+2y^4Lt .
\]
把 \(c'''W_4\) 分部一次后，与(14)中的
\(I_2^y(c,T_yu^2)\) 相加，余式准确为
\[
 \int\{2y^2p^2c''+(4yp^2+4y^2pr+2C_u)c'
        -(2y^2r^2+4p^2)c\}.
\]
先对第一项分部，再用
\(C_u'=-(y^2r^2+2p^2)\)，剩余积分为零。因此
\[
 A_4=-I_2^y(c,T_yu^2).
 \tag{16}
\]
这里仅紧外槽 \(c,c'\) 支付端项；没有要求 \(C_u\) 左常数为零。

### 2.3 二次项只有一个完整局部余量

直接有
\[
 W_2'=4ypr-2y^2r^2-2p^2+4y^2Lt
      =y^2(R_yu^2)''+(T_yu^2)''.
\]
故(10)与(12)的二次层相加后为
\[
 \int\{-2p^2c''+(4pr+2P_u-4yr^2)c'+2r^2c\}.
\]
再对第一项和 \(c'\) 项分部，使用 \(P_u'=-r^2\)，得到
\[
 \boxed{
 A_2+I_2^y(c,R_yu^2)+I_0^y(c,T_yu^2)
 =-8\int cLt .
 }
 \tag{17}
\]
式(15)(16)(17)代回公共因子即证(8)。整个推导的每个边项含紧 \(c\) 的 jets；单包 \(P_u,C_u,R_yu^2,T_yu^2\) 的真实左值均被保留。

作为原已付对角的核对，
\(\int uLt=-\tfrac12\int(u-yp)r^2\)，所以(8)在 \(c=u\) 时准确回到 R492(23) 的 \(v\mathfrak m_y(u)/(8h)\)。这不是本稿证明任意外槽时所依赖的假设。

## 3. 完整奇行对任意紧输入的局部式

对(8)的 inner 两槽极化，由(13)的一般双线性版本得到
\[
 (R_y(a,b))''
 =(a'-ya'')b'''+(b'-yb'')a''' ,
\]
\[
 \boxed{
 \mathcal T_s(c;a,b)
 -\mathcal E_s\{c,\mathsf A_{\rm sec}(a,b)\}
 =-\frac{v}{8h}\int c(R_y(a,b))'' .
 }
 \tag{18}
\]
极化只涉及紧输入；输出 \(R_y(a,b)\) 仍按原锚定义。

从 R492(15) 的原 \(\beta\) 定义，可先写成
\[
 \boxed{
 \beta_\theta^\omega(\eta)
 =-\frac14\int\eta(R_yD_\theta)''
  +\frac12\int\phi_\theta(R_y(\phi_\theta,\eta))'' .
 }
 \tag{19}
\]
这同时证明：**对任意紧 \(\eta\)，\(\beta\) 不依赖正割段的 \(H\)**。R492 原来的 \(H_s,\omega_s\) 标注在此可准确缩为 \(\omega\)；不是只在 period 核上作缩减。

令 \(p_\phi=\phi'\)、\(r_\phi=\phi''\)、\(t_\phi=\phi'''\)。第二项转置时的完整 identity 为
\[
 \int\phi(R_y(\phi,\eta))''
 =\int\eta\{-p_\phi t_\phi+3yr_\phi t_\phi
                    +(yp_\phi-\phi)\phi''''\}.
\]
因此(19)准确等价于
\[
 \boxed{
 \beta_\theta^\omega(\eta)
 =\frac12\int\eta\left[
 (y\phi_\theta'-\phi_\theta)\phi_\theta''''
 +2y\phi_\theta''\phi_\theta'''
 -(f'-yf'')f'''
 \right].
 }
 \tag{20}
\]
原有的三阶/四阶 profile jets 没有称为新的 \(C^2\) 观察；这里只给完整 pairing 的准确呈示。

(20)对 \(\omega\) 仿射，并且
\[
 \partial_\omega\beta_\theta^\omega(\eta)
 =\frac12\int\eta
 \{\phi_\theta'\phi_\theta''''+
   2\phi_\theta''\phi_\theta'''+f''f'''\}.
 \tag{21}
\]
本稿没有把(20)在所有紧输入上等同于 R492 的四行组合 \(\ell_\theta\)；该行关系仍只在原完整 period 核上按其前提使用。

## 4. 两个真实中心的 source 与共同规范准确相消

假设同一真实路径含两条实际包含中心的正割段，二者使用同一 \(\omega\) 及原物理坐标、右锚和 profile 圆，允许不同 \(H_1,H_2>0\)。记其真实中心累计算子为
\[
 A_j=\Phi_{\mathsf m(s_j^*)},\qquad
 A_2-A_1=\Phi_{\int_{s_1^*}^{s_2^*}M_{\rm raw}(s)\,ds}.
 \tag{22}
\]
没有把这个积分替成删除端项的分部积分矩。

对任意同一个全局第二规范 \(w_\theta\)，各中心的真实 second characteristic 为
\[
 q_j^*=w_\theta+A_jD_\theta .
 \tag{23}
\]
原三矩合法性使 \(A_jD_\theta\) 真紧。由 R488 的中心场奇偶证明及 R492(43)，该段完整奇 ruling 系数为
\[
 b_{j,\theta}=\beta_\theta^\omega(q_j^*).
 \tag{24}
\]
(24)保任意真实第三 incoming。其贡献、第三齐次规范和完整 second gauge 平方在每条 secant 上均为 even；不能以改变它们修复下面的差。

**定理 2：双中心真实不变量。** 对任意同一个允许的 \(w_\theta,\chi_\theta\)，
\[
 \boxed{
 b_{2,\theta}-b_{1,\theta}
 =\beta_\theta^\omega\{(A_2-A_1)D_\theta\}.
 }
 \tag{25}
\]
这个身份先于第四 period 的求解，不需要选择 particular，不要求 protected rational germ 已付，也不要求给两条段各取一个规范。其证明只是(20)(23)(24)的准确相减。

若使用 R492 的 protected-germ source 表示，则两个段的
\(\mathfrak b_{\theta;H,\omega}(G_\theta^c)\) 因本稿的完整 \(H\) 无关性相同，于(25)中消去。所有桥/prototype 对整个 \(V\) 以及 \(G_\theta^c=-V_\theta^c/(2\tau)\) 的改变也进入这个同一个共同 source，不能留下一个自由“source 补偿”来改两者之差。

因此两条段全 ruling 同时为零的一个准确必要条件是
\[
 \boxed{\beta_\theta^\omega\{(A_2-A_1)D_\theta\}=0
        \quad\text{对全部 }\theta.}
 \tag{26}
\]
它不取代两个 even 系数、原 period、十三行或连接桥自身的全 \(s\) 条件；它是在这些条件之前已经存在的规范不变量。

若两条段的 \(\omega\) 不同，则(21)给出的
\((\omega_2-\omega_1)\partial_\omega\beta_\theta(w_\theta)\)
一般仍在，不能直接套(25)。若一个实际子段不包含中心，本稿也不为了使用(24)而插入新几何或重置历史。

## 5. \(P\) 前缀的完整四次式：先保全部有序常尾

现在采用当前严格不交 rank-one 库：
\[
 f=\sum_i a_i u_i,\qquad
 \phi_\theta=\sum_i c_i u_i,\qquad
 c_i=a_i\cos\theta+b_i\sin\theta,\quad
 d_i=a_i^2-c_i^2 .
 \tag{27}
\]
从左至右编号。写
\[
 p_i=u_i',\quad r_i=u_i'',\quad
 \mu_i=\int r_i^2,\quad
 C_i=\int r_i^4>0,\quad B_i=\int p_i r_i^3,\quad
 C_{i,1}^{\,\omega}=\int(x+\omega)r_i^4 .
 \tag{28}
\]
\(\mu_i\) 在本节只表示零阶矩，不冒称完整三矩向量。

原 \(P=\Phi_{r_0}\) 给
\[
 PD_\theta=\sum_i d_iP_i,\qquad P_i=J(r_i^2).
\]
在第 \(i\) 包上准确为
\[
 (PD_\theta)|_i=d_iP_i+n_i,\qquad
 n_i=\sum_{j>i}d_j\mu_j .
 \tag{29}
\]
这是实际有序 suffix，不把各 \(P_i\) 当成左紧。原 circle 的零阶合法矩给
\[
 \sum_i d_i\mu_i=0,
 \tag{30}
\]
所以完整 \(PD_\theta\) 在两外 collars 真零。

从(20)出发，仅在紧 \(u_i\) 的槽上分部，得到两个真实单包积分：
\[
 \int P_i(p_i-yr_i)u_i'''
 =B_i-\frac{\mu_i^2}{4}-\frac{C_{i,1}^{\,\omega}}2,
 \tag{31}
\]
\[
 \int P_i\{(yp_i-u_i)u_i''''+2yr_i u_i'''\}
 =\frac{C_{i,1}^{\,\omega}}6-\frac{\mu_i^2}{4}.
 \tag{32}
\]
其中用了
\[
 \int P_ir_i^2=\mu_i^2/2,\qquad
 \int yP_ir_i u_i'''=-\mu_i^2/4+C_{i,1}^{\,\omega}/2 .
\]
它们明确保留 \(\mu_i^2\)，不是对非紧 \(P_i\) 错置边项。

常数 suffix \(n_i\) 对(20)的贡献为
\[
 \beta_\theta^\omega(n_i\text{ on packet }i)
 =n_i d_i\mu_i/4 ;
\]
可直接积分(20)，也准确等于 R492 平台列(27)。
因此所有单包平方和有序项合为
\[
 \frac18\sum_i d_i^2\mu_i^2+
 \frac14\sum_{i<j}d_i d_j\mu_i\mu_j
 =\frac18\left(\sum_i d_i\mu_i\right)^2=0.
 \tag{33}
\]
只有在这一步才用(30)。

由(31)—(33)得到完整公式
\[
 \boxed{
 \beta_\theta^\omega(PD_\theta)
 =\sum_i\left[
 -\frac{a_i^2d_i}{2}B_i+
 \frac{d_i(3a_i^2+c_i^2)}{12}C_{i,1}^{\,\omega}
 \right].
 }
 \tag{34}
\]
原幅度、宽度、位置和包序已逐项进入；不存在被隐藏在 \(O(1)\) 中的 primitive 常数。

在当前各自关于中心 \(\xi_i\) 偶对称的母库中，
\[
 B_i=0,\qquad
 C_{i,1}^{\,\omega}=(\xi_i+\omega)C_i.
\]
所以可进一步写成
\[
 \boxed{
 \beta_\theta^\omega(PD_\theta)
 =\frac1{12}\sum_i
 d_i(3a_i^2+c_i^2)(\xi_i+\omega)C_i .
 }
 \tag{35}
\]
式(34)本身不需要偶母；(35)才使用该原构造前提。

## 6. 全 \(W\) outer 给出的严格非零斜率

当前 R480 库已经支付所有第三外矩。特别，R486(18)从原
\([P,L]\) 的完整 self 与零有序核得到
\[
 \sum_i c_i^2d_iC_i=0\quad\text{对全部 }\theta .
 \tag{36}
\]
这不是另加的新 cap 门。对(34)按同一个几何参数 \(\omega\) 求导，得到
\[
\begin{aligned}
 \partial_\omega\beta_\theta^\omega(PD_\theta)
 &=\frac1{12}\sum_i d_i(3a_i^2+c_i^2)C_i\\
 &=\frac14\sum_i d_i^2C_i+
   \frac13\sum_i c_i^2d_iC_i .
\end{aligned}
\]
故
\[
 \boxed{
 \partial_\omega\beta_\theta^\omega(PD_\theta)
 =\frac14\sum_i d_i(\theta)^2C_i\ge0 .
 }
 \tag{37}
\]
这不是从 signed self 单包正性猜全角号：准确删除的项由已付(36)给出。

R486(20)还给
\[
 \sum_i d_i(\pi/2)^2C_i=4\int(g'')^4.
\]
于是
\[
 \boxed{
 \partial_\omega\beta_{\pi/2}^\omega(PD_{\pi/2})
 =\int(g'')^4>0.
 }
 \tag{38}
\]
非退化真圆 \(g\ne0\) 和双零 collars 保最后严格号。
本结论不需要新增任何 profile 观察或计算积分值。

更明确地，在固定 profile 圆上定义一个已有真实实数
\[
 \omega_{\rm blind}
 =-\frac{\beta_{\pi/2}^{\,0}(PD_{\pi/2})}{\int(g'')^4}.
 \tag{39}
\]
则对所有合法 \(\omega\)
\[
 \boxed{
 \beta_{\pi/2}^{\,\omega}(PD_{\pi/2})
 =(\omega-\omega_{\rm blind})\int(g'')^4 .
 }
 \tag{40}
\]
所以最多一个 \(\omega\) 对该相位的 \(P\) 前缀盲。若要在新的路径初选中选择共同 \(\omega\)，可取
\(\omega>-\min I\) 并避开这个单值；这是合法有限选择，不要求把某个旧冻结几何改掉。
在已经固定的 \(\omega=\omega_{\rm blind}\) 情形，本稿不推其它相位也零，更不推其它 E8 前缀都盲。

## 7. 一个实际可产生、不能被同规范消去的双中心残差

先从起点固定同一个 profile 库及共同物理窗口，选两个实际含中心的正割小段，使用同一合法 \(\omega\ne\omega_{\rm blind}\) 和任意固定正 \(H_1,H_2\)。两段的 scalar/frame germs 和所有连接 collars 作为实际几何数据固定。

原 R70 与 R469 §10 已支付如下有限前缀接口：在真实常 scalar collars 之间，给定完整 frame/scalar 端点以及一个有限八矩目标，可以用正长度实际路径准确实现该目标；参数落固定紧盒时，先固定有限圈数得到光滑截面。非平 collar 至中心的固定短段则使用原 \(M_{\rm raw}\) 完整积分。

因此可对一个有限实参数 \(t\) 精确指定
\[
 \boxed{A_2-A_1=tP.}
 \tag{41}
\]
实施时，先保两正割段从入口至中心和从中心至出口的原实际积分，再把它们从桥目标中扣除；不能只给连接桥本身 \(tP\) 而忽略两个半段。负的 \(t\) 是原矩阵桥实现的负目标，不是负时间。

若需总 \(M=0\)，在所有标记中心之后接原真实矩阵复位桥。若还要求指定的总第三 period，可按原 R80 在这些标记段之外加入零矩第三控制块，补其真实已产生的第三成本。所有第四基准、时长、窗口与 later incoming 均保原值。这里仅消费这些原已付层；不声称新桥的内部 ruling 自动为零，亦不由此授予完整增强成本、空间嵌入或主几何。

现在由(25)(40)(41)，对**任意同一个**全局允许规范，
\[
 \boxed{
 b_{2,\pi/2}-b_{1,\pi/2}
 =t(\omega-\omega_{\rm blind})\int(g'')^4 .
 }
 \tag{42}
\]
所以：

- 只要 \(t\ne0\)，这两个实际正割段不可能同时具有全零第四 ruling；
- \(t\) 在一个固定有限小盒内取正负，可以产生两号的真实双中心奇 residual；
- 真实桥引起的 entire period source、third incoming 或 fourth baseline 不会把(42)改为零，因为它们按(25)准确相消，而不是被省略；
- 后置一个不穿过两个标记中心的 \(M=T=0\) 成本控制，仍不能改变(42)。即使它另行准确付了总成本条件，也不能支付这个固定前缀差。

这就回答了一个明确的自动相容问题：**真实 center+bridge forcing 不因来自同一原恢复、总 \(M=0\) 或指定第三 period，就自动满足全部 secant 奇行兼容。** 非零见证来自一个实际矩阵桥目标和完整原场差，不来自一个任意形式 F0 系数或旧 rank 的重算。

但(42)不是所有路径的不存在定理。设计者也可从起点指定 \(t=0\)；此时本稿这一个差门确实为零，而每段共同的 odd source 值、两个 even 行、连接段全 ruling、原 range 和同十三规范仍须继续支付。一个单 secant 段不受本双中心差的直接排除。

## 8. 与原 source 商及下一真实正向问题的关系

R492 在当前偶母库上已经定义
\[
 \mathfrak b^\omega_\theta(G)
 =(\beta^\omega_\theta-\ell_\theta)(k),\qquad L_fk=G
\]
于真正同 collar 紧像。本文(20)使它对所有正割高度 \(H\) 为同一个泛函。这里没有证明它在整个真实 source 像为零，也没有把一般形式 source 当作已有紧逆。

对同一 \(\omega\) 的有限多个实际中心，必须先满足
\[
 \beta^\omega_\theta((A_j-A_1)D_\theta)=0
 \quad(j\ge2,\ \text{全部 }\theta).
 \tag{43}
\]
这些是实际标记二阶前缀门。全部付后，各段仍共享一个未自动为零的 odd source 值。不能用更多 period 齐次母/平台列修它：R492 已证明原十三行把这些变化全部锁住。

与 R469 的多个有理端芽最高行相比，(43)读的是本文完整 quartic pairing；它不是把原 \(d_f\) 最高行换名。即便某个前缀同时杀 \(d_f\)，还须分别检查(43)。反之，本文也不宣 \(P\) 是完整八维前缀读出唯一的非零方向，或其核已被分类。

下一正向构造可以准确选择共同中心矩阵，先消(43)，再处理同一个 \(\mathfrak b^\omega_\theta(G_\theta^c)\) 与两个 even 目标及全部 bridges 的共同函数像。当前完成的是一个原始局部三槽身份与实际非自动相容见证，不以更多条件列表代替这个明确的非零值。

## 9. 直接来源和已核范围

- R221/R469：原完整 \(\mathcal T_s\)、physical 配对、全路径规范响应及真实母/平台尾；
- R259/R488：原 \(P,R_y,T_y\) 同锚算子、真实正割浸入、任意 incoming 的完整仿射场和中心奇偶；
- R492：任意紧输入的 \(\beta\) 定义、原十三行在 period 核上的作用，以及完整中心公式；
- R480/R486：同一个新母库的全 \(W\) outer 与 \(\sum c_i^2d_iC_i=0\)、\(\sum d_i(\pi/2)^2C_i=4\int(g'')^4\)；
- R70/R469 §10、R80：准确原矩阵前缀桥和标记中心之外的零矩第三控制，保所有实际成本基准。

全文是纸面有限代数与已付真实桥接口的使用，没有下载或重新计算旧科学根、没有数值评价新积分、没有把一次有限模型搜索的非零残差用于本定理。
