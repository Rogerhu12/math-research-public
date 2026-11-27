# R1043 — 原二同源的 full9 运输与完整54图的九项有权约简

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明。** 本篇把原二挠谱盖上的实际二同源、原 full9 基、三个
canonical 二阶核及原2、17处角色同时固定。对 R1027(28)的完整
shadow，三个二阶核的项各自与17处标签重排严格相等；再接已付的
$\delta$ 配对，原54项恰为指定九项的六倍。原 $\eta_j$、全部
$\operatorname{Cor}_{L/H}$、最高转置投影和同源图均保留。

这里的相等是原交公式中实际点值的相等，不把同一个 $t$ 当成同一个
full9 点，也不由此断言这九项非零。本篇不声称已经得到原循环之间的
Chow 相等，更不以九项约简代替跨普通 $p$ 的非零。

## 1. 固定原对象及方向

沿 R991、R1006、R1027 取
$$
 K=\mathbf Q(\omega),\quad
 \omega^2+\omega+1=0,\quad \delta=1+2\omega,\quad\delta^2=-3,
$$
$$
 A:\ y_A^2+y_A=x_A^3,\qquad
 B:\ v^3=t(1-27t),\quad X=-3v,\quad Y=-27t,
$$
$$
 S/B:\ y^2+xy+ty=x^3,\qquad
 \omega_A=\frac{dx_A}{2y_A+1},\quad
 \omega_t=\frac{dx}{2y+x+t}.
 \tag{1}
$$
所以 $B$ 的原方程是 $Y^2+Y=X^3$。实际甲板自同构为
$$
 \tau_S(t,v,x,y)=(t,\omega v,x,y),\qquad
 \tau_B(X,Y)=(\omega X,Y).
 \tag{2}
$$
在有限仿射纤维上，它保持原纤维坐标；在无穷极小纤维上的作用另见
第4节，不能把有限坐标的恒等延伸为该纤维上的恒等。

固定 R1006(14) 的完整9级基，并把它写成**列**：
$$
 \boldsymbol\beta=
 \begin{pmatrix}(1+\omega)u_9\\(\omega-1)u_9\end{pmatrix}.
 \tag{3}
$$
这是 R1006 的 row/adjugate 约定已经给出的两个实际点；本篇仅为
矩阵书写把二者竖排，没有再作一次 adjugate 或共轭。

原完整54个核与权重为
$$
 C_{2,i}=\overline{\omega^i}C_{2,0},\quad i=0,1,2,
 \qquad C_{17,t}=\bar t C_{17,0},\quad
 t\in\mathcal C_{18}:=\mathbf F_{17^2}^{\times}/\mathbf F_{17}^{\times},
$$
$$
 C_{i,t}=C_{2,i}+C_{17,t},\qquad
 \varphi_{i,t}:A\longrightarrow S_{b_{i,t}},\qquad
 c_{i,t}=c_{2,i}c_{17,t}.
 \tag{4}
$$
每个 $\varphi$ 都是真正 degree34 商同源，(3)沿它运输，随后才忘至
原 $\Gamma$。所有这些图及级点定义在 R1006 固定的 $L$ 中。

取 R1027 的固定系数环 $R$，其中2、3及原有限 projector 分母可逆。
在原好约化上，对实际 degree0 除子
$$
 D^+=(e_S^+)_*D,\qquad
 Q^+(b):=r_b(D^+),
$$
定义
$$
 z_{\gamma,i,t}
 =(e_A^-)_*\widehat{\gamma\varphi_{i,t}}
       \bigl(Q^+(\gamma b_{i,t})\bigr),
 \qquad \gamma\in\operatorname{Gal}(L/K).
 \tag{5}
$$
这正是 R1027(28)中的点，不换成低维 Prym 半类或无权 Norm。

## 2. 原二挠谱盖上的规范二同源

R1029 给原二挠谱盖及其到 $B$ 的映射
$$
 C:\quad w^2=(z^3-4)(z^3-16),
$$
$$
 X=-\frac{3z}{z^3-4},\qquad
 2Y+1=\frac{w(z^3+2)}{(z^3-4)^2}.
 \tag{6}
$$
令
$$
 u=\frac{1-w/(z^3-4)}6.
$$
直接代入(6)有
$$
 t=u^2(1-2u),\qquad x_2=-u^2.
 \tag{7}
$$
这里 $x_2$ 是原纤维的实际非零二挠点的 $x$ 坐标；$C$ 所标的是这
一个核，不能在随后三次根运输中把三个核平均掉。

置
$$
 X_f=x+u^2,\qquad W_f=y+(x+t)/2,
$$
$$
 A_f=\frac14-3u^2,\qquad B_f=u^3(3u-1).
$$
则原纤维变为
$$
 W_f^2=X_f^3+A_fX_f^2+B_fX_f.
$$
核为 $(0,0)$ 的规范二同源是
$$
 X'=X_f+A_f+\frac{B_f}{X_f},\qquad
 W'=W_f\left(1-\frac{B_f}{X_f^2}\right),
$$
$$
 W'^2=X'^3-2A_fX'^2+(A_f^2-4B_f)X'.
 \tag{8}
$$
展开右端即可核方程，且
$dX'/(2W')=dX_f/(2W_f)$。故这一步保持不变微分。

原标记三挠点 $P_3=(0,0)$ 的像是
$$
 a_3=\frac{(1-2u)^2}{4},\qquad
 b_3=\frac{u(1-2u)^2}{2}.
$$
其切线斜率为 $m=3u-\frac12$。令
$x_T=X'-a_3,\ y_T=W'-b_3-mx_T$，得到
$$
 y_T^2+(6u-1)x_Ty_T+u(1-2u)^2y_T=x_T^3.
$$
再令
$x'=x_T/(6u-1)^2,\ y'=y_T/(6u-1)^3$，便是同一个标记
三挠点的原 Tate3 模型，参数及微分为
$$
 \boxed{
 t'=\frac{u(1-2u)^2}{(6u-1)^3},\qquad
 \phi_2^*\omega_{t'}=(6u-1)\omega_t.
 }
 \tag{9}
$$
等式在函数域中推导，随后按同一同源延拓至极小模型；不因某个所写
分母为零而删掉下面的 canonical 极限。

## 3. 三次根与 full9 分量：确为原双椭圆 involution

原曲线 $C$ 上的真实 involution 为
$$
 \iota(z,w)=(4/z,\,8w/z^3).
 \tag{10}
$$
由 $w^2=(z^3-4)(z^3-16)$ 及(7)逐式计算，
$$
 u\circ\iota=\frac{1-2u}{2(1-6u)},\qquad
 t\circ f\circ\iota=t',
$$
$$
 \boxed{v\circ f\circ\iota=-\frac{z^2}{z^3-16}.}
 \tag{11}
$$
于是(11)是(9)所需三次根的一个明确解。还须支付它确实是完整
9级沿二同源运输后得到的根，而不是任选一个乘 $\omega$ 的解。

原模群及其商字符是
$$
 \Gamma=\ker\theta\subset\Gamma_1(3),\qquad
 \theta\begin{pmatrix}a&b\\3c&d\end{pmatrix}=\omega^{b-c}.
 \tag{12}
$$
素于3的商在3处由 $\operatorname{diag}(n,1)$ 表示；对矩阵共轭，
$$
 \begin{pmatrix}n&0\\0&1\end{pmatrix}^{-1}
 \begin{pmatrix}a&b\\3c&d\end{pmatrix}
 \begin{pmatrix}n&0\\0&1\end{pmatrix}
 =\begin{pmatrix}a&b/n\\3nc&d\end{pmatrix}.
$$
因 $n^{-1}\equiv n\pmod3$，其商字符把 $b-c$ 乘 $n$。
特别二同源反转这一个三次甲板字符。若
$\rho(z,w)=(\omega z,w)$，则
$$
 \iota\rho=\rho^{-1}\iota,
 \tag{13}
$$
正与这个完整级结构计算相符。

三次根的常数也能固定。原 $X_\Gamma$ 的 $\mathbf Q$ 模型来自
$\Gamma(9)$ 级的商，其模9群可写成如下条件：设
$\epsilon=\det g\bmod3\in\{\pm1\}$，则
$$
 g=\begin{pmatrix}a&b\\3c&d\end{pmatrix},\quad
 a\equiv\epsilon,\quad d\equiv1,\quad b\equiv\epsilon c\pmod3.
 \tag{14}
$$
它的 determinant1 部分就是(12)；determinant 映射满射，且
$h=\operatorname{diag}(-1,1)$ 给非平凡 $K/\mathbf Q$ 分量。
直接乘法核(14)是群；上面的 $\operatorname{diag}(n,1)$ 共轭
保持(14)。因此二阶核的选择、规范商和忘至原 $\Gamma$ 的两支映射
均在这个实际 $\mathbf Q$ 模问题上定义。R991(30)首项为1的
$v$ 正是该模型的原坐标。

实际商映射的三次根若与(11)相差 $\omega^r$，二者都是
$\mathbf Q(C)$ 中的函数。$C$ 几何整，常数域为 $\mathbf Q$；
因此 $r=0$。这把完整根固定，未在共轭分量上另选一个 $\omega$。
也可在源点 $(z,w)=(0,8)$ 作局部核对：这里 $u\to1/2$，核是
$ t=0$ Tate 纤维的光滑 $\mu_2$，而
$$
 v=-z/4+\cdots,\qquad v'=z^2/16+\cdots=v^2+\cdots.
$$
这正是 $\mu_2$ 商的 Tate 参数 $q_T\mapsto q_T^2$ 在原
width9 根上的首项；原 $\Delta=t^3(1-27t)$、$c_4=1-24t$
同时给 $q_T=t^3+\cdots=v^9+\cdots$。

在 full9 层，Weil pairing 的指数经这一步乘2，故中间目标确在
**共轭的 $K$ 分量**。随后 degree17 运输再乘17，完整 degree34
目标返回原 $K$ 分量。式(14)和(13)正是这个分量变化的实际运输；
本篇没有插入一个额外 $h$ 来重置中间基，也没有丢掉它。

## 4. 三个 canonical 核、三个 $B[2]$ 点及准确微分倍率

固定原 $u_2$，令
$$
 a=-1/x_A(u_2),\qquad a^3=4,\qquad a_i=\omega^i a.
 \tag{15}
$$
三个 $P_i=(a_i,0)\in C$ 正是 $f^{-1}(O_B)$。
在 $P_i$ 用 $w$ 作参数；从原方程得到
$$
 z=a_i-\frac{w^2}{36a_i^2}+O(w^4),\quad
 t=-16w^{-3}+O(1),\quad
 v=-12a_iw^{-2}+O(1).
$$
于是 R1006(15)的原 canonical 参数 $\zeta=v/t$ 满足
$$
 \zeta=(3a_i/4)w+O(w^3),\qquad
 6u-1=12w^{-1}+O(w).
 \tag{16}
$$
原好模型中
$\omega_t=\zeta\omega_{\rm min}$、
$\omega_{\rm min}|_A=-\omega_A/3$。将(16)代入(9)，准确得到
$$
 \boxed{\phi_i^*\omega_{1/54}=-3a_i\,\omega_A.}
 \tag{17}
$$
特别不能用未极小化的 $\omega_t$ 在无穷处直接求值；它有零，(9)
的倍率同时有极，二者的乘积才是(17)。

由(11)，三个目标基点是
$$
 \boxed{
 b_{2,i}=\left(-a_i^2/4,\,-1/2\right)
        =\tau_B^{-i}b_{2,0}\in B[2]\setminus\{O_B\}.
 }
 \tag{18}
$$
源二挠点在 R1006 的固定同构下也是
$x_A=-a_i^2/4,\ y_A=-1/2$。故它的核正是
$C_{2,i}=\bar\omega^i C_{2,0}$，不是另一个临时的二阶核编号。

三个目标的原有限纤维方程都是 $t'=1/54$。在这些原仿射坐标下，
同源有相同的标记三挠点，(17)与核一起给
$$
 \phi_i=\phi_0\circ[\omega^i].
 \tag{19}
$$
此等式先在特征零的实际同源上确定；同核同靶的两条同源至多差
靶自同构，标记点及显示的微分倍率固定它为1。然后约化同一个
有理恒等式，而不是在正特征凭微分相同猜同源相同。
按 R1006 的拉回规范，目标微分是
$\omega_{\phi_i}=\omega_{1/54}/(-3a_i)$。

式(19)用原有限纤维坐标识别两个靶。写成完整曲面上的图，它是
$\phi_i=\tau_S^{-i}\phi_0[\omega^i]$；这样包含(18)，没有把不同
full9 点误认为同一个基点。

## 5. 源 full9 基的单位矩阵，及 degree34 图的准确关系

对(3)的列基，直接乘 CM 单位得
$$
 [\delta]\boldsymbol\beta=-D_3\boldsymbol\beta,\qquad
 D_3=\begin{pmatrix}0&-1\\3&0\end{pmatrix},
$$
$$
 [\omega]\boldsymbol\beta=M_\omega\boldsymbol\beta,\qquad
 M_\omega=\frac{-D_3-I}{2}.
 \tag{20}
$$
模9可取整数矩阵
$$
 M_\omega\equiv
 \begin{pmatrix}4&5\\3&4\end{pmatrix}\pmod9.
 \tag{21}
$$
这个整数矩阵本身 determinant 为1；在(12)中的 $b-c$ 是
$5-1\equiv1\pmod3$。这里必须先说明**几何列基**怎样对应经典
$\Gamma$，不能把(21)直接当作 Hsieh 的 adelic 右矩阵。

在一个固定 Weil pairing 分量，用标准几何列基
$\mathbf e_\tau=(\tau/9,1/9)^T$。对
$\gamma=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)
\in\mathrm{SL}_2(\mathbf Z)$，同构
$$
 E_{\gamma\tau}\longrightarrow E_\tau,\qquad
 z\longmapsto(c\tau+d)z
$$
把 $\mathbf e_{\gamma\tau}$ 送到 $\gamma\mathbf e_\tau$。
所以列基左乘 $\gamma$ 对应的是经典 $\tau\mapsto\gamma\tau$
的同一 deck。R991 的原根规范给 $\theta(\gamma)=\omega$
对应 $v\mapsto\omega v$。这个推导没有使用右表示矩阵。

若 Weil pairing 相对于标准分量的指数为 $d_0$，用
$D_{d_0}=\operatorname{diag}(d_0,1)$ 归一化分量；列基作用相应变成
$D_{d_0}^{-1}M_\omega D_{d_0}$。其 $b-c$ 模3是原值的
$d_0$ 倍，因为 $d_0^{-1}\equiv d_0\pmod3$。
原(3)的指数是 $-2$，最终 degree34 目标的指数是 $-68$，
二者均为1模3；故它们读到的都是(21)的正 $\tau$。
degree2 中间指数是 $-4\equiv-1\pmod3$，其共轭
$hM_\omega h^{-1}$ 的 $b-c\equiv-1$，读到 $\tau^{-1}$。

与此严格区分：若横排同一基，(20)写成
$\boldsymbol\beta_{\rm row}\mapsto
\boldsymbol\beta_{\rm row}M_\omega^T$。R1006 的 row/adjugate
规则已经在构造(3)时用过；把该横排式重新翻译为 adelic 右操作
会涉及 adjugate 的反序及原 $g=Ph$ 的共轭，该右操作不是
$\pi(M_\omega)$。本篇不作这一替换，而是使用上面已逐式给出的
几何列基与经典 $\Gamma$ 的对应。因此没有隐含第二次 adjugate，
也没有凭列排本身省掉一个逆。

这同时核了第3、4节的二同源负号，及下面 degree34 的正号。

还可直接在 universal fiber 上核该方向：在 canonical 点，
改级基 $\boldsymbol\beta\mapsto[\omega]\boldsymbol\beta$ 后，
返回原标记对象的同构是 $[\omega]^{-1}$。
R1027(16)–(19)已在原极小模型中算出，实际 $\tau_S$ 在该纤维上
正是 $[\omega^2]$。所以(21)对应 $\tau$，不能反写成
$\tau^{-1}$；基点 $O_B$ 自身固定并不足以核这个方向，纤维作用
才把它区分出来。

对(4)置
$$
 t'=\omega^{-i}t.
$$
由核的原共轭编号，
$$
 C_{i,t}=\omega^{-i}\bigl(C_{2,0}+C_{17,t'}\bigr).
 \tag{22}
$$
因此先作 $[\omega^i]$ 再作 $\varphi_{0,t'}$ 是同一个 degree34 商。
它把目标完整基改变为 $M_\omega^i$ 作用后的基。
degree34 的 Weil pairing 指数乘34，且 $34\equiv1\pmod3$；
因此仍在原 $K$ 分量，应使用(21)的正甲板作用。
完整模问题于是给严格的交换图等式
$$
 \boxed{
 b_{i,t}=\tau_B^i b_{0,\omega^{-i}t},\qquad
 \varphi_{i,t}
 =\tau_S^i\circ\varphi_{0,\omega^{-i}t}\circ[\omega^i]_A.
 }
 \tag{23}
$$
第二式中的 $\tau_S^i$ 是所涉两纤维之间的实际同构。
这比只说靶曲线有相同 $t$ 或 $j$ 更强；它保留完整9级和三挠标记。
一般有限纤维中 $\tau_S$ 的原坐标是恒等，故可去掉坐标书写中的
$\tau_S^i$；在 canonical 极小纤维上不准去掉。

也可分两步核(23)：先 degree2 使(18)的甲板指数为 $-i$，
随后 degree17 的3处共轭再次取反，变成 $+i$；
17核在中间的真实像为
$$
 \phi_i(C_{17,t})
 =\phi_0\bigl(\omega^i\bar t C_{17,0}\bigr)
 =\phi_0(C_{17,\omega^{-i}t}).
$$
这里沿商保留全部级点，没有在中间另选一个标准17基或标准9基。

## 6. 最高转置投影下的实际点值相等

以下是原 relative Picard 中的等式，系数为上面的固定 $R$。
R1027(15)给
$$
 F_*Q=Q+2\tau_S^*Q+\epsilon(Q)P_3.
$$
原 $\epsilon(Q)P_3$ 在这里准确被3可逆消掉；不是在整点群中假定
它为零。实际同源满足
$F_{-b}=-\widehat F_b$，因为
$F_{-b}F_b=[-3]$ 而 $\widehat F_bF_b=[3]$。
所以在 degree0 relative Picard 上 $F^*=-F_*$，从而
$$
 F^*Q=-Q-2\tau_S^*Q.
$$
原 $D^+$ 的 $F^*$ 特征为 $-\delta$，故
$$
 \boxed{\tau_S^*Q^+=\omega Q^+.}
 \tag{24}
$$
其中原 projector 所减的旧垂直类和基的线丛在光滑纤维上限制为零，
正是 R1027(34)已支付的相同范围。

若 $\tau_{b}^{(i)}:S_b\to S_{\tau_B^i b}$ 表示(2)的纤维同构，
(24)的完整纤维写法是
$$
 \widehat{\tau_{b}^{(i)}}
       \bigl(Q^+(\tau_B^i b)\bigr)
   =\omega^i Q^+(b).
 \tag{25}
$$
此处左侧是 Picard 拉回，即对偶同源；不能在所有纤维上把它省去。
在有限原仿射纤维上才可把(25)写作 $Q^+(\tau^i b)=\omega^iQ^+(b)$。

原 $e_A^-$ 的点群作用由 R1027(36)给出：
它选择几何 $[\delta]_A=+\delta$，因此也选择
$[\omega]_A=\omega$。对(23)取对偶，再用(25)，得到
$$
\begin{split}
 &(e_A^-)_*\widehat{\varphi_{i,t}}
       \bigl(Q^+(b_{i,t})\bigr)\\
 &\quad=(e_A^-)_*[\omega^{-i}]
       \widehat{\varphi_{0,t'}}
       \widehat{\tau_{b_{0,t'}}^{(i)}}
       \bigl(Q^+(\tau_B^i b_{0,t'})\bigr)\\
 &\quad=\omega^{-i}\omega^i
       (e_A^-)_*\widehat{\varphi_{0,t'}}
          \bigl(Q^+(b_{0,t'})\bigr).
\end{split}
$$
所以是真正的点值相等
$$
 \boxed{z_{1,i,t}=z_{1,0,\omega^{-i}t}.}
 \tag{26}
$$
两因子来自不同位置：一个来自原 $D^+$ 的甲板 Picard pull，
另一个来自原 $e_A^-$ 选择下的源 CM 对偶。少掉任意一个都会得到
错误的三项消零。

## 7. 两个原有限角色与54项的精确约简

R991(5)、R1006(18)的角色是
$$
 \chi_{j,2}|_{\mathcal O_{K,2}^{\times}}=\epsilon_2^{-1},\qquad
 \chi_{j,17}|_{\mathcal O_{K,17}^{\times}}=\vartheta_{l_j},
 \quad l_j=-5,1,7.
$$
因为 $\epsilon_2(\omega)=\omega$、
$\vartheta_l(\omega)=\omega^{16l}=\omega$，三个原 $j$ 全部满足
$$
 c_{2,i}=\omega^i,\qquad
 c_{17,\omega^i t'}=\omega^{-i}c_{17,t'}.
 \tag{27}
$$
这里用的是有限 idèle 单位角色，未把它偷换成相反的主理想规范。
(26)、(27)逐项给
$$
 \boxed{
 \sum_{i=0}^2\sum_{t\in\mathcal C_{18}}
   c_{2,i}c_{17,t}z_{1,i,t}
 =3\sum_{t\in\mathcal C_{18}}c_{17,t}z_{1,0,t}.
 }
 \tag{28}
$$
这是重数3的相加，既非无权 Hecke 和，也非改用2处 spherical 向量。

先固定一个本原十八次单位根 $\zeta_{18}$，满足
$\zeta_{18}^{\,6}=\omega$，再利用 $\chi_{j=10,17}$ 在
$\mathcal C_{18}$ 上的忠实性，**定义**唯一的生成元 $s$：
$$
 \chi_{j=10,17}(s)=\zeta_{18},\qquad
 \zeta_9=\zeta_{18}^{\,2}.
 \tag{29}
$$
这是生成元的方向条件，不是对任意生成元的断言。
于是 $\chi_{j,17}(s)=\zeta_{18}^{\,l_j}$；
$\delta$ 的类是 $s^9$，而 $\omega$ 的类是 $s^6$。
注意 $s$ 是**商群**的生成元，不把
$\mathbf F_{17^2}^{\times}$ 中一个 order18 元素自动当成它：
后者在商去 $\mathbf F_{17}^{\times}$ 后可能仅有 order9。

固定二阶核 $C_{2,0}$，R1027(30)–(37)的同一个实际三同源给
$$
 z_{1,0,s^9t}=-z_{1,0,t},\qquad
 c_{17,s^9t}=-c_{17,t}.
$$
全部18项因此配成九个相加的对。$s^{2r}$、$0\le r\le8$ 恰是一组
完整代表，因为 order9 子群与 order2 子群的交平凡。于是
$$
 \boxed{
 \sum_{i,t}c_{2,i}c_{17,t}z_{1,i,t}
 =6\sum_{r=0}^8\zeta_9^{-l_jr}z_{1,0,s^{2r}}.
 }
 \tag{30}
$$
右侧仍有九个不同的真实 degree34 图；没有因某个未证明的有限
评价关系再删项。三个指数模9分别是 $4,1,7$，系数仍在原
$\mathbf Q(\zeta_9)$ 中，不引入新的系数扩张。

## 8. 全部 Galois 共轭与原 $\eta$、Cor 同时保留

每个 $\gamma\in\operatorname{Gal}(L/K)$ 固定 $\omega,\delta$、
$\tau_S,F$ 及源 $A$。先对(23)作真正的 $\gamma$ 共轭，再在固定
素位约化；(25)依旧是同一个 $D^+$ 的几何限制关系。
因此不需要 $\gamma$ 属于该素位的分解群，准确有
$$
 z_{\gamma,i,t}=z_{\gamma,0,\omega^{-i}t},\qquad
 z_{\gamma,0,s^9t}=-z_{\gamma,0,t}.
 \tag{31}
$$
系数保持原固定 $c_{i,t}$，没有对它另作 $\gamma$ 共轭。

把(30)逐个代入原 R1027(28)，其 $1/18$ 平均准确成为
$$
 \boxed{
 \mathcal S_D(Y_{j,0,R})
 =\frac13
   \sum_{\gamma\in\operatorname{Gal}(L/K)}
     \eta_j(\gamma|_H)^{-1}
     \sum_{r=0}^{8}\zeta_9^{-l_jr}\,
       (e_A^-)_*\widehat{\gamma\varphi_{0,s^{2r}}}
           \bigl(r_{\gamma b_{0,s^{2r}}}(D^+)\bigr).
 }
 \tag{32}
$$
这仍是全部 $\operatorname{Cor}_{L/H}$，原三个 $\eta_j$、
原最高转置投影和每个 degree34 对偶同源都显示在式中。
如果某次约化有原 R1027 的 canonical 零项，(23)、(25)仍按极小
模型解释；没有用有限坐标恒等错判它。

本篇的新输入是(9)、(11)、(17)、(23)及原有权九项公式(32)。
已关闭的无权 Pell–Norm 关系不代替这个九项和；九项本身的非零、
原普通局部检测及无穷多个不同 $p$ 仍需继续证明。

## 依赖定位

- [R991](R991-three-cubic-twists-and-explicit-level-nine-toric-input.md)
  §1、§5、§6：原角色、full9 模群及有理模型。
- [R1006](R1006-actual-full-nine-trace-and-original-katz-square.md)
  §3–5：原 row/adjugate 基、canonical 极小微分、54图及固定系数。
- [R1027](R1027-canonical-fiber-six-torsion-and-original-shadow-column.md)
  §1–4、§7：同一实际 $F,\tau$、Picard 对偶方向、原 $\delta$ 配对。
- [R1029](R1029-original-two-torsion-cm-genus-two-and-norm-classes.md)
  §1–3：原二挠谱盖与已指定双椭圆 involution。本篇另外支付它在
  原模问题中的二同源含义和完整级结构运输。
