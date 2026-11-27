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

## 9. 把全部原 $\eta$ 一起吸入三列，而不删任何 $\gamma$

本节不是从三个完整 trace 为零推逐 $\gamma$ 为零。
先对一个固定 $\gamma$ 置
$$
 V_{\gamma,j}=\sum_{r=0}^8
       \zeta_9^{-l_jr}z_{\gamma,0,s^{2r}}.
$$
写 $r=a+3b$，可将它分成三列；但(32)的外部 $\eta_j$ 随 $j$
改变，所以仅作这个分组不足以处理三个完整 shadow。

原角色还有一个由 R806(8)、R1019(6)的完整主理想规范确定的关系：
$$
 \boxed{\eta_j=\eta_{10}^{\,l_j},\qquad l_j=-5,1,7.}
 \tag{33}
$$
确实对原所有素于34的主理想，$\mu_3$ 因子因
$l_j\equiv1\pmod3$ 保持，17处则有
$\vartheta_{l_j}=\vartheta_1^{\,l_j}$。$K$ 的类数为一，
故这核对了整个有限 Hecke 角色，而不只是一个剩余类。

对每个原 $\gamma\in\operatorname{Gal}(L/K)$，定义
$n_\gamma\in\mathbf Z/18$ 为
$$
 \eta_{10}(\gamma|_H)=\zeta_{18}^{\,n_\gamma}.
$$
因 $\zeta_{18}=-\zeta_9^5$，且 $l_j$ 为奇数，原(32)的一个系数
准确等于
$$
 \eta_j(\gamma|_H)^{-1}\zeta_9^{-l_jr}
 =(-1)^{n_\gamma}\zeta_9^{-l_j(r+5n_\gamma)}.
 \tag{34}
$$
现在才在**每个原 $\gamma$ 内**作循环换标
$r+5n_\gamma=a+3b\pmod9$，并置
$$
 t_{\gamma,a}=s^{\,2a-10n_\gamma},\qquad a=0,1,2,
$$
$$
 \boxed{
 C_a=
 \sum_{\gamma\in\operatorname{Gal}(L/K)}(-1)^{n_\gamma}
   \sum_{i=0}^2\omega^i z_{\gamma,i,t_{\gamma,a}}.
 }
 \tag{35}
$$
定义与 $n_\gamma$ 的整数提升无关。内层用到了原(31)：
令 $i=-b\pmod3$，就有
$z_{\gamma,0,t_{\gamma,a}\omega^b}
 =z_{\gamma,i,t_{\gamma,a}}$，而 $\omega^{-b}=\omega^i$。
因此(34)逐项给完整公式
$$
 \boxed{
 J_j:=\mathcal S_D(Y_{j,0,R})
 =\frac13\sum_{a=0}^2\zeta_9^{-l_ja}C_a.
 }
 \tag{36}
$$
所有原 $\gamma$ 仍出现一次。$(-1)^{n_\gamma}$ 是原
$\eta_{10}^9$ 的二次符号；其余角色已经变成显示的真实17核平移，
而不是被删掉。

按 $j(0)=10,\ j(1)=4,\ j(2)=16$ 排序，
$l_{j(k)}\equiv1+3k\pmod9$。三阶 Fourier 逆给
$$
 \boxed{
 C_a=\zeta_9^a\sum_{k=0}^2\omega^{ka}J_{j(k)}.
 }
 \tag{37}
$$
故在原系数群及任何仍使3可逆的商中，
$$
 J_{10}=J_4=J_{16}=0
 \quad\Longleftrightarrow\quad C_0=C_1=C_2=0.
 \tag{38}
$$
这是三个**完整**原 shadow 的等价条件，已把全部 $\eta$ 和 Cor
放进(35)。它不等价于每个 $\gamma$ 的三列分别为零，也没有声称
(35)中的任意一列已非零。

## 10. 原二商的全迹为零，有直接的原谱域证明

在第2节的 $C$ 上，对任意原 degree0 截面类 $Q$ 定义
$$
 R_0(Q)(P)=
 \widehat{\phi_{2,P}}\bigl(Q(f\iota P)\bigr)
       \in S_{fP}.
 \tag{39}
$$
先对真正的点定义，再对原 $R$ 系数线性延拓。
这里 $\omega$ 等系数从不充当一般纤维的几何 CM 自同源。

以 $p_C:S\times_BC\to S$ 为源投影，以 $\Phi_2$ 为第2节的
实际二同源到靶 $S$，对应 $p_{C*}\Phi_2^*$ 在相对 Picard 上
就是(39)的三支群迹。其在原二形式上的作用可直接算出。

原基微分为
$$
 \omega_B=\frac{dX}{2Y+1}=-\frac{dt}{v^2},
 \qquad \Omega_S=-\omega_B\wedge\omega_t.
$$
由 R1029 的实际两映射，
$$
 f^*\omega_B=6\,dz/w,\qquad
 (f\iota)^*\omega_B=-3z\,dz/w.
$$
由(7)或 R1031(4)，还有
$$
 6u-1=-\frac{(2Y+1)z}{z-2X}.
$$
所以 $\Phi_2^*\Omega_S$ 相对于 $p_C^*\Omega_S$ 的准确乘子是
$$
 H_2=\frac{(2Y+1)z^2}{2(z-2X)}.
 \tag{40}
$$
这保留(9)的实际微分倍率，没有用一个未经换算的 Hecke 归一化。

令
$$
 P(Z)=Z^3+\frac3X Z-4,\qquad d_0=2X.
$$
则
$$
 P(d_0)=2(2Y+1)^2,\qquad
 P'(d_0)=\frac{3(2Y+1)^2}{X}.
$$
因 $\operatorname{Tr}(z)=0$，在原三次谱域中准确有
$$
 \operatorname{Tr}\frac{z^2}{z-d_0}
 =3d_0-d_0^2\frac{P'(d_0)}{P(d_0)}
 =6X-6X=0.
 \tag{41}
$$
故 $\operatorname{Tr}(H_2)=0$。同一有理对应也杀复共轭二形式。
原 $T(S)_{\mathbf Q}$ 恰为这两维，所以该对应在整个 $T(S)$ 为零。

原特征零 NS 恰是秩12的旧平凡格，因此这个代数对应把它仍送入
旧 NS。沿同一图和光滑模型作 Betti–étale 比较、光滑适当基变换，
其在约化 $H^2$ 上的像仍在旧平凡子空间中。Shioda–Tate 与
cycle-map 单射遂说明，(39)的完整群迹是几何 torsion 截面。
原全部 torsion 是 $\langle P_3\rangle$，故准确结论为
$$
 \operatorname{Tr}_{C/B}R_0(Q)\in\langle P_3\rangle,\qquad
 \boxed{\operatorname{Tr}_{C/B}R_0(Q)=0
        \quad\text{在倒6的原系数群中}.}
 \tag{42}
$$
没有把整点群中的可能三挠修正先设为零。
对奇异纤维的图作解消，只增加旧垂直类；在本式的相对 degree0
群中不增加另一水平截面。式(41)也没有在 $2Y+1=0$ 删除纤维，
它是函数域的恒等式，随后由同一完整对应延拓。

## 11. 真正的 $S_3$ 全盖、两个加权截面及仅倒6的显式左逆

使用 R1029§6 已给的原完整二谱盖
$$
 \mathcal D:\quad 4h^3=A^6-1,
$$
$$
 X=h^2/A^2,\quad Y=(A^3-1)^2/(4A^3),\qquad
 z=(A^2-1)/h,\quad w=3A(A^4-1)/h^3.
 \tag{43}
$$
其实际 deck 为
$$
 \sigma(A,h)=(\omega A,\omega h),\qquad
 \epsilon(A,h)=(A^{-1},-h/A^2),
$$
$$
 \sigma^3=\epsilon^2=1,\qquad
 \epsilon\sigma\epsilon=\sigma^{-1}.
 \tag{44}
$$
$\epsilon$ 固定原 $(z,w)$，所以
$C=\mathcal D/\langle\epsilon\rangle$。两式的源基 $B$ 均固定。
将(39)拉到 $\mathcal D$，令
$$
 R_i=\sigma^{i*}R_0,\qquad
 \mathscr R_\omega=R_0+\omega R_1+\omega^2R_2,\qquad
 \mathscr R_{\omega^2}=R_0+\omega^2R_1+\omega R_2.
 \tag{45}
$$
(42)正是 $R_0+R_1+R_2=0$。同时
$\epsilon^*R_0=R_0$、$\epsilon^*R_1=R_2$，因而
$$
 \epsilon^*\mathscr R_\omega=\mathscr R_{\omega^2},\qquad
 \boxed{\mathscr R_\omega+\epsilon^*\mathscr R_\omega=3R_0.}
 \tag{46}
$$

这给比单纯非零向量更明确的左逆。令
$g_1=f\iota\circ(\mathcal D\to C):\mathcal D\to B$，其次数为6。
对 $\mathcal D$ 上源纤维的任意系数截面 $V$，定义
$$
 \mathcal L(V)=
 \frac1{36}\operatorname{Tr}_{g_1}
       \left(\phi_2\bigl(V+\epsilon^*V\bigr)\right).
$$
这里 $\phi_2$ 始终取(39)同一个标记核；$\epsilon$ 固定该核和
$g_1$，所以两项可在同一源纤维上相加。由
$\phi_2\widehat\phi_2=[2]$ 及(46)，
$$
 \boxed{\mathcal L(\mathscr R_\omega(Q))=Q.}
 \tag{47}
$$
确实括号给 $3R_0$，二同源给 $6g_1^*Q$，再作六度迹给 $36Q$。

因此 $Q\mapsto\mathscr R_\omega(Q)$ 是原 MW 系数群的一个
**分裂单射**，左逆只除2、3。它同时保任何好系数素位
$\mathfrak p\nmid6$ 的全球不可除性：
$$
 \mathscr R_\omega(Q)\in\mathfrak p^n MW(\mathcal D)\otimes R
 \ \Longrightarrow\
 Q\in\mathfrak p^n MW(B)\otimes R.
 \tag{48}
$$
这不依赖先猜一个饱和子格。尤其原非零 $Q^+$ 给非零
$\mathscr R_\omega(Q^+)$。若只想核非零，反射也已足够：
一个加权和为零使另一个也为零，再由全迹迫 $3R_0=0$；
而对 $R_0$ 先作用 $\phi_2$ 再取 $g_1$ 迹会迫 $12Q^+=0$。

## 12. 加权截面实际下降到一个明确的椭圆基曲面

下面给真实几何下降，不由纯表示同型猜一个新曲面。
在 $\mathcal D$ 上再取
$$
 \kappa(A,h)=(A,\omega^2h).
$$
它覆盖原 $B$ 上的 $\tau_B$；在 $C$ 上为
$(z,w)\mapsto(\omega z,w)$。由(13)，其靶基 $f\iota$ 则改变为
$\tau_B^{-1}f\iota$。二同源(8)–(9)只依赖 $u$，
而 $u(\omega z,w)=u(z,w)$。对原 $Q^+$ 用(25)遂得
$$
 \kappa^*R_0(Q^+)=\omega^{-1}R_0(Q^+).
$$
$\kappa$ 与 $\sigma$ 交换；(45)又给
$\sigma^*\mathscr R_\omega=\omega^{-1}\mathscr R_\omega$。
所以
$$
 \boxed{(\kappa\sigma^{-1})^*\mathscr R_\omega(Q^+)
             =\mathscr R_\omega(Q^+).}
 \tag{49}
$$

这个 order3 商的实际坐标是
$$
 \boxed{
 X'=-h/A^2,\qquad Y'=(A^{-3}-1)/2,\qquad
 Y'^2+Y'=X'^3.
 }
 \tag{50}
$$
$\kappa\sigma^{-1}$ 在 $(A,h)$ 上为
$(\omega^2A,\omega h)$，所以(50)确实不变。
反向 $A^3=(2Y'+1)^{-1}$、$h=-X'A^2$ 说明扩张次数正是3。
原纤维参数严格变成
$$
 \boxed{
 t=-\frac{Y'^2}{27(2Y'+1)}.
 }
 \tag{51}
$$
于是定义一个固定曲面
$$
 \mathscr S'/B':\quad
 y^2+xy-\frac{Y'^2}{27(2Y'+1)}y=x^3,\qquad
 B':Y'^2+Y'=X'^3,
 \tag{52}
$$
并取其原光滑相对极小模型。(49)以实际群迹除3下降，给
$$
 P_Q\in MW(\mathscr S'/B')\otimes R,\qquad
 q_-^*P_Q=\mathscr R_\omega(Q^+),
 \tag{53}
$$
其中 $q_-$ 就是(50)。一般纤维没有 CM，(53)是**系数 MW 截面**：
把它按 $1,\omega$ 展开并清固定2、3分母，得到两个真正有理截面。
这里没有把 $\omega$ 写成一般纤维上的一个未经存在证明的同源。

反射给另一个实际商
$$
 q_+(A,h)=\bigl(h,(A^3-1)/2\bigr),\qquad
 q_+=q_-\epsilon.
$$
它也满足(51)，且
$$
 q_+^*P_Q=\mathscr R_{\omega^2}(Q^+),\qquad
 3R_0=q_-^*P_Q+q_+^*P_Q.
 \tag{54}
$$
所以两个加权方向来自(52)上的同一个系数截面，
不是两个独立、未比较的输入。

为固定模型的实际边界，可直接由(51)读出其全部纤维。
$Y'=0$ 与 $Y'=-1$ 在 $B'$ 的局部阶都是3，
而
$$
 t=-Y'^2/[27(2Y'+1)],\qquad
 t-1/27=-(Y'+1)^2/[27(2Y'+1)].
$$
因此这两处分别为 $I_{18},I_6$。
三个非零二挠点 $2Y'+1=0$ 是 $t$ 的单极，保原 $IV^*$；
无穷点为三重极，原 $IV^*$ 经三次分歧后极小化为好纤维。
所以
$$
 \operatorname{Fib}(\mathscr S')=
 I_{18}+I_6+3IV^*,\qquad
 \chi(\mathcal O_{\mathscr S'})=4,\quad p_g=4,\quad q=1.
 \tag{55}
$$
这些是同一个明确方程的纤维，并未把 $\mathscr S'$ 叫作 K3，
也未宣称它与 $S$ 的完整 Chow 动机相同。
(47)、(53)给的是所需系数截面的实际对应和左逆。

## 13. 三列正是这个截面在原17标记点的值

对任意 $t\in\mathcal C_{18}$，令
$$
 \psi_t:A\longrightarrow S_{b_{17,t}}
$$
为原 kernel $C_{17,t}$ 的 degree17 商，携带由(3)运输的完整9级。
它处于第3节已说明的共轭 $K$ 分量；随后二商返回原分量。
在原完整二谱盖上选择 $d_t$，按原 full2 标号要求
$\sigma^i d_t$ 所标的核恰为
$$
 \psi_t(C_{2,i}),\qquad i=0,1,2.
 \tag{56}
$$
三个二挠根的完整 $S_3$ 模问题使这个有序 lift 唯一；
改变为相反的次序必须同时改变 $\sigma$ 和权，不在本篇实施。
所有这些点已经在原 full306 的 $L$ 中。

商同源的自然性给真正的图等式
$$
 \varphi_{i,t}=\phi_{2,\sigma^id_t}\circ\psi_t.
 \tag{57}
$$
该式保完整9级和标记三挠点，故也保第4节的微分规范。
对偶的顺序于是准确为
$\widehat\psi_t\circ\widehat\phi_{2,\sigma^id_t}$，
不多乘17或2。由(39)、(45)、(53)，
$$
 \boxed{
 \sum_{i=0}^2\omega^i z_{\gamma,i,t}
 =(e_A^-)_*\widehat{\gamma\psi_t}
       \left(\mathscr R_\omega(Q^+)(\gamma d_t)\right)
 =(e_A^-)_*\widehat{\gamma\psi_t}
       \left(P_Q(\gamma q_-d_t)\right).
 }
 \tag{58}
$$
这里的 $\gamma$ 共轭先在原 $L$ 上进行，随后约化；
$q_-$、实际二同源等均是已指定的代数映射。
式中源、靶的有限坐标按(50)–(52)识别，
没有把共轭 $K$ 分量重置为另一个同 $t$ 的 level 点。

因此(35)的完整三列可以严格写成
$$
 \boxed{
 C_a=\sum_{\gamma\in\operatorname{Gal}(L/K)}
 (-1)^{n_\gamma}\,
 (e_A^-)_*\widehat{\gamma\psi_{t_{\gamma,a}}}
 \left(P_Q(\gamma q_-d_{t_{\gamma,a}})\right).
 }
 \tag{59}
$$
这是同一原最高 shadow 的三个**实际有标记评价**；
不是把所有 CM 点平均成无权 Norm。
(47)已经给 $P_Q$ 的全球来源非零及仅倒6的分裂回收，
但固定评价映射仍可能有核。
所以(59)中至少一列非零、原普通局部比较及无穷不同 $p$
仍是尚须真正支付的步骤，不能由全球本原性直接填写。

## 依赖定位

- [R991](R991-three-cubic-twists-and-explicit-level-nine-toric-input.md)
  §1、§5、§6：原角色、full9 模群及有理模型。
- [R1006](R1006-actual-full-nine-trace-and-original-katz-square.md)
  §3–5：原 row/adjugate 基、canonical 极小微分、54图及固定系数。
- [R1027](R1027-canonical-fiber-six-torsion-and-original-shadow-column.md)
  §1–4、§7：同一实际 $F,\tau$、Picard 对偶方向、原 $\delta$ 配对。
- [R1029](R1029-original-two-torsion-cm-genus-two-and-norm-classes.md)
  §1–3、§6：原二挠谱盖、完整S3盖与已指定双椭圆 involution。本篇另外支付它在
  原模问题中的二同源含义和完整级结构运输。

## 14. 新曲面的 canonical fiber 是准确的 $E_4$，并保原全有限角色

本节只对(52)和已经给出的图作规范转换。
不把 $\mathscr S'$ 的完整八维超越部分叫作原二维表示；
所用部分始终是(39)、(45)、(53)从原 $S$ 实际送来的部分。

在 $B'$ 的无穷点置
$$
 \zeta=X'/Y',\qquad r=1/Y',\qquad
 \zeta^3=r+r^2,\qquad x=\zeta^{-2}u,\quad y=\zeta^{-3}w.
$$
代入(51)–(52)得原好模型
$$
 w^2+\zeta uw-\frac{1+r}{27(2+r)}w=u^3.
$$
因此无穷纤维和其准确的标准坐标为
$$
 w^2-\frac1{54}w=u^3,\qquad
 \boxed{x_4=36u,\quad y_4=216w-2,\quad y_4^2=x_4^3+4.}
 \tag{60}
$$
记这条曲线为 $A_4=E_{(4)}$，并取
$\omega_4=dx_4/(2y_4)$。这里的模型在2、3之外有好约化；
它不是一个仅凭 $j=0$ 选出的同构。

取(43)中与原 $C_{2,0}$ 相符的 $A=\infty$ 支，令
$h/A^2\to c$，故 $c^3=1/4$。固定 $a=c^{-1}$，
正是第4节 $a=-1/x_A(u_2)$ 的同一个三次根。
源 $B$ 的 canonical 参数和 $q_+$ 的参数分别有首项
$$
 v/t=36c^2/A+\cdots,\qquad
 X'_+/Y'_+=2c/A+\cdots.
$$
使用 R1006 的源好模型和(60)，直接相消这些首项给
$$
 \boxed{
 I:A=E_{27}\longrightarrow A_4,\qquad
 I(x_A,y_A)=(a^2x_A,\,-4y_A-2),
 \qquad I^*\omega_4=-\frac{a^2}{4}\omega_A.
 }
 \tag{61}
$$
例如源 $x_A=36cA^{-2}x+\cdots$，
而(60)给 $x_4=144c^2A^{-2}x+\cdots$；
两者之比 $4c=a^2$。
同样源 $y_A=-108A^{-3}y+\cdots$，
而 $y_4=432A^{-3}y-2+\cdots$，固定了(61)的负号。

原标记 $P_3=(0,0)$ 因而送到 $(0,-2)$；
完整9级基就是 $I\boldsymbol\beta$，不改为以 $(0,2)$ 起头的另一
标准基。$I$ 与几何 $\mathcal O_K$ 作用交换，所以该基中的
$\delta$ 矩阵仍是 $-D_3$。所选普通 CM 素位也未共轭。

这里可直接核与第13节17同源的层相容性。
同一个 $A=\infty$ 支在 $q_+$ 下是 $O_{B'}$，
在 $q_-$ 下是 $(-c,-1/2)$。
沿本篇(12)–(14)同一个几何级结构约定，令
$D_{17}=\operatorname{diag}(17,1)$，则
$$
D_{17}^{-1}
\begin{pmatrix}a&b\\3c&d\end{pmatrix}D_{17}
=\begin{pmatrix}a&b/17\\51c&d\end{pmatrix}.
$$
原三处角色 $\theta=\omega^{b-c}$ 因而变成
$\omega^{b/17-17c}=\theta^{-1}$（模3），准确给 $\kappa$ 取逆。
在2处，靶的完整有序基定义为 $(\psi_tP_2,\psi_tQ_2)$；
17为奇数使此为完整二挠同构，且
$\psi_t(P_2+Q_2)=\psi_tP_2+\psi_tQ_2$，
所以原三个核的循环标号 $\sigma$ 不变。
这说明同一实际17商把
$\langle\kappa\sigma\rangle$ 送到
$\langle\kappa^{-1}\sigma\rangle
 =\langle\kappa\sigma^{-1}\rangle$。
这正是 $q_+$ 到 $q_-$ 两个 quotient；没有把其中一个强行重置。
所以每条第13节的图可等价写成准确的 degree17 图
$$
 \boxed{
 \Psi_t:A_4\longrightarrow
 \mathscr S'_{q_-d_t},\qquad
 \Psi_t=\psi_t I^{-1}.
 }
 \tag{62}
$$
靶的原 $(x,y)$ 方程相同，源、靶的全级结构由上述同一商运输。

再核整个有限 twist。令 $\vartheta^3=2$，
取 $a=\vartheta^2$，并记
$\kappa_2(\gamma)=\gamma(\vartheta)/\vartheta$。
由(61)严格有
$$
 \gamma I=[\kappa_2(\gamma)]I.
 \tag{63}
$$
这是 R991 的同一个
$\psi_4=\kappa_2\psi_{27}$，并不因为(61)有负号而另改其角色。
对(62)取真正的 $\gamma$ 共轭与对偶，
再用原 $e_A^-$ 选择几何 $[\omega]=\omega$，得到
$$
 I\,(e_A^-)_*\widehat{\gamma\psi_t}(P)
 =
 \kappa_2(\gamma)^{-1}
 (e_{A_4}^-)_*\widehat{\gamma\Psi_t}(P).
 \tag{64}
$$
所以若把原外部椭圆曲线由 $A$ 换成这个规范 $A_4$，
原 Artin 权必须且恰好换成
$$
 \boxed{\eta'_j=\eta_j\kappa_2.}
 \tag{65}
$$
这里不需扩大 $L$：R1006§1、§3 已令 $L$ 包含原 $A[306]$，
所以 $u_2$ 及 $a=-1/x_A(u_2)$ 属于同一个 $L$。
取 $\vartheta=2/a$，因 $a^3=4$，有
$\vartheta^3=2$、$\vartheta^2=a$；
(61)及其全部共轭皆已在 $L$ 中，不增加任何trace次数。
(64)逐个作用于原完整
$\operatorname{Gal}(L/K)$ 求和，原 $1/18$ 不变。
这里不是仅给一个同构后漏掉其下降 cocycle。

全部有限位可以逐项核回：在2处，
$\eta'_j=\epsilon_2$、$\psi_4=\epsilon_2^{-1}$；
在3处 $\eta'_j(\omega)=\omega$、
$\eta'_j(-1)=1$、$\eta'_j(\delta)=-1$；
17处的 $\vartheta_{l_j}$ 完全不改。
因 $\psi_4=\kappa_2\psi_{27}$，实际 toric 角色严格相同：
$$
 \boxed{
 \eta'_j(\psi_4N_K^{-1/2})^{-1}
 =\eta_j(\psi_{27}N_K^{-1/2})^{-1}.
 }
 \tag{66}
$$
尤其不能把这一构造改成 R991 已排的
$\pi_4=\operatorname{AI}(\psi_4^2)$ 输入；
曲面端仍是原对应实际送来的 $\psi_{27}^2$ 部分。
其最高角色准确是
$$
 \boxed{
 \psi_{27}^2\psi_4(\eta'_j)^{-1}
 =\psi_{27}^3\eta_j^{-1}
 =\psi_0^3\eta_j^{-1},
 }
 \tag{67}
$$
原混合部分也随同一对应保留，而不是被另一个未核的 weight2
因子替换。

式(61)的微分倍率在 $p\ge5$ 为单位，并且 $I$ 保指定 CM 方向。
因此这个规范转换本身保普通子空间、局部有限条件和相应的非零
等价；它不证明(59)的指定评价非零，也不把该评价与普通 AJ 的
尚未支付部分视为已经完成。

## 15. 原最高曲面微分在新曲面上的准确像

本节计算第10–13节实际对应对二形式的作用；仍保
$\Omega_S=-\omega_B\wedge\omega_t$，
$\omega_B=dX/(2Y+1)$。在 $C$ 上由(7)、(9)、(10)直接得
$$
 6u-1=-\frac{w}{z^3-4},\qquad
 f^*\omega_B=\frac{6\,dz}{w},\qquad
 (f\iota)^*\omega_B=-\frac{3z\,dz}{w}.
$$
故给出 $R_0$ 的同一图（源在 $f$ 上、靶在 $f\iota$ 上）对形式的
拉回准确为
$$
 \Phi_2^*\Omega_S
 =-\frac{3z\,dz}{z^3-4}\wedge\omega_t
 =\frac{A^4-1}{2Ah^2}\,dA\wedge\omega_t .
 \tag{68}
$$
最后一步只用 $z=(A^2-1)/h$、$4h^3=A^6-1$：
$z^3-4=-3A^2(A^2-1)/h^3$，
$dh=A^5dA/(2h^2)$。这里图的点群作用是对偶同源，而其
上同调作用是显示的微分拉回，两者来自同一个图，并未互换源靶。

在 $D$ 上 $\sigma(A,h)=(\omega A,\omega h)$，且原 $t$、
$\omega_t$ 不变。因此按(45)的同一个系数序作和，
$$
 \begin{aligned}
 \sum_{i=0}^2\omega^i\sigma^{i*}\Phi_2^*\Omega_S
 &=\frac{3A^3}{2h^2}\,dA\wedge\omega_t,\\
 \sum_{i=0}^2\omega^{2i}\sigma^{i*}\Phi_2^*\Omega_S
 &=-\frac{3}{2Ah^2}\,dA\wedge\omega_t .
 \end{aligned}
 \tag{69}
$$
例如第一式中 $A^4$ 项的三个系数均为1，而常数项系数和为零。
这保留了 $R_\omega$ 的原顺序，不把它换成共轭和。

对 $q_-$ 的实际坐标(50)，有
$$
 2Y'+1=A^{-3},\qquad
 q_-^*\omega_{B'}=-\frac{dA}{2h^2},\qquad
 \omega_{B'}=\frac{dX'}{2Y'+1}.
$$
于是置
$$
 \boxed{\;
 \Omega'_1=\frac{\omega_{B'}\wedge\omega_t}{2Y'+1},
 \qquad
 \mathcal T_\omega(\Omega_S)=-3\Omega'_1 .
 \;}
 \tag{70}
$$
$\mathcal T_\omega$ 是上面原图之和在 $q_-$ 下降后的对应。
式(70)在函数域中逐式成立；两边均为光滑射影曲面的正规二形式，
故通过所有坏纤维的相同极小解消延拓。下降没有另乘一个3：
(69)本身就是 $q_-^*(-3\Omega'_1)$；
若用 trace 实现下降，须取 $\operatorname{Tr}_{q_-}/3$。

还可由原极小模型检查整个空间及 canonical 点的准确零阶。
令 $D_2$ 是 $B'$ 上 $2Y'+1=0$ 的三个点之和。
在三个 $\mathrm{IV}^*$ 点，原 $\omega_t$ 等于一个局部参数乘
极小不变微分；在 $O_{B'}$ 由第14节也有
$\omega_t=\zeta\omega_{\min}$。
故原 Hodge 线丛是
$\mathcal O_{B'}(D_2+O)$，且
$\operatorname{div}(2Y'+1)=D_2-3O$。
全空间的四个正规形式为
$$
 \boxed{
 \Omega'_1,\quad X'\Omega'_1,\quad
 Y'\Omega'_1,\quad X'^2\Omega'_1 .
 }
 \tag{71}
$$
确实 $L(4O)$ 的基是 $1,X',Y',X'^2$；
式(71)在全部极小模型上正则，并且维数为
$h^0(\mathcal O_{B'}(4O))=4=p_g(\mathscr S')$。

在 $O$ 用第14节的 $\zeta=X'/Y'$。
$X'=\zeta^{-2}+\cdots$、$Y'=\zeta^{-3}+\cdots$、
$\omega_{B'}=-d\zeta+\cdots$，所以
$$
 \Omega'_1
 =-\frac12\zeta^4(1+O(\zeta))
       d\zeta\wedge\omega_{\min}.
 \tag{72}
$$
式(71)的零阶依次为 $4,2,1,0$。
更全局地，$\Omega'_1$ 的零除子正是好纤维 $4F_O$：
三个 $\mathrm{IV}^*$ 处的分母各恰消原微分的一个零，
其余没有新增零或极。极小 Weierstrass 模型的有理双点解消
保正规二形式，故此陈述也包含全部纤维组件。

原 $\tau':(X',Y',x,y)\mapsto(\omega X',Y',x,y)$
对四式的特征依次是
$\omega,\omega^2,\omega,1$。
特别第14节 canonical 纤维上的非零形式
$X'^2\Omega'_1$ 不是(70)的原对应像。
仅因该纤维已经写成 $E_4$，不能把该形式代替
$\Omega'_1$ 来评价原最高 Abel–Jacobi 类。
式(70)和(72)同时给出了后继真实负二阶/标记评价应使用的
形式与其延拓；它们不把(59)三个完整列的非零作为已知。

## 16. 完整 Galois 作用逐图重标记：三列各严格等于一个固定值

本节进一步计算(59)中的全部 $\gamma$。
所作等式先在原有限数域内的实际商图上成立，再在同一选定的
约化嵌入下使用；不把一个不在 decomposition group 中的
$\gamma$ 当作剩余域的 Frobenius。

### 16.1 原 full9 的完整 determinant 下降

沿 R1006(24)–(25) 的算术 reciprocity。
令 $L_0\subset L$ 为由原 $H$、全部306级点及规范商图生成的域。
这些对象的 Galois 作用来自 CM torsion 的阿贝尔商。
对任意 $\gamma\in\operatorname{Gal}(L/K)$，在此阿贝尔商中选择
有限单位 idèle $u$ 表示其限制；$h_K=1$ 保证可如此选择。
记 $\epsilon(u)\in\mu_6$ 为 $u_3\bmod3$ 的唯一单位提升。
则原 $A=E_{27}$ 上
$$
 \rho(\gamma)=\epsilon(u)u^{-1},\qquad
 \rho_3\equiv1\pmod{3\mathcal O_{K,3}}.
 \tag{73}
$$

不能仅由最后的模3同余就跳到 full9 结论。
写 $\rho_3=A_3+B_3\omega$；这里
$A_3\equiv1\pmod3$、$B_3\equiv0\pmod3$。
在原 $\boldsymbol\beta$ 基中，(20)给准确矩阵
$$
 G_\gamma=A_3I+B_3M_\omega
 =\begin{pmatrix}
 A_3-B_3/2&B_3/2\\
 -3B_3/2&A_3-B_3/2
 \end{pmatrix}\pmod9.
 \tag{74}
$$
下左项实际上被9整除，且在(12)的记号中
$b-c=B_3$。所以 $G_\gamma$ 满足(14)的全部条件，而不只其
$\mathrm{SL}_2$ 投影。
它的 determinant 是
$d_\gamma=A_3^2-A_3B_3+B_3^2\in(\mathbf Z/9)^\times$，
$ d_\gamma\equiv1\pmod3$。
准确分解
$G_\gamma=\operatorname{diag}(d_\gamma,1)G_\gamma^0$
中，$G_\gamma^0$ 的 determinant 为1，并仍满足(12)的
$b-c\equiv0\pmod3$；第一因子属于(14)的 determinant 下降部分。

原 Weil pairing 在 $\gamma$ 下恰变为其 $d_\gamma$ 次幂，
这正是(14)内的 cyclotomic 下降，不要求
$d_\gamma=1\pmod9$。因此原 $\Gamma$ 级对象在其既定
$\mathbf Q$ 模型上被固定，没有漏掉 $\zeta_9$ 的内在共轭，
也没有再乘一个不明的三次根。
这与系数环中的 $\zeta_9$ 是两件事：
本篇全部 $\gamma$、$e_{\eta_j}$ 都是点/循环因子作用
$\gamma\otimes1$，在已经固定的代数系数上不再作 semilinear
共轭。

源曲线 $A$、标记 $P_3$ 及 $\omega_A$ 均在 $K$ 上。
其非平凡 CM 自同构不能保持这个 $\Gamma$ 级对象：
$[-1]$ 改变 $P_3$，而 $[\omega]$ 的(21)矩阵有非平凡
$\theta$。所以上述 full9 识别没有一个剩余源自同构。

### 16.2 全部54图的严格置换与原角色

定义 $r_\gamma\in\mathbf Z/3$ 和
$h_\gamma\in C_{18}$ 为
$$
 \rho_2(\gamma)=\omega^{r_\gamma},\qquad
 h_\gamma=[\rho_{17}(\gamma)].
$$
于是原核的标号严格变为
$$
 \gamma C_{2,i}=C_{2,i-r_\gamma},\qquad
 \gamma C_{17,t}=C_{17,h_\gamma^{-1}t}.
$$
第二式使用的是原 $C_{17,t}=\bar t C_{17,0}$，
以及 $\overline{h_\gamma}=h_\gamma^{-1}$，不能把这个逆省掉。
由§16.1的源 full9 固定及规范商的函子性，
$$
 \boxed{
 \gamma\varphi_{i,t}
   =\varphi_{i-r_\gamma,h_\gamma^{-1}t}.
 }
 \tag{75}
$$
此式包含靶的全9点和原模型，不仅是两曲线的 $j$ 值相等。
两边的微分均由同一个固定的 $\omega_A$ 拉回规范唯一确定；
$\gamma\omega_A=\omega_A$，故商微分的倍率也被正确运输。
规范减项中的34、两个零截面与同一个最高 projector 均与此置换
交换。

置 $Z_j=\sum_{i,t}\omega^i\vartheta_{l_j}(t)^{-1}
\Delta_{\varphi_{i,t}}$，系数全部固定。
重新标号(75)逐项给
$$
 \gamma Z_j=
 \omega^{r_\gamma}\vartheta_{l_j}(h_\gamma)^{-1}Z_j
 =\eta_j(\gamma)Z_j.
 \tag{76}
$$
最后一个等号可以直接核全有限角色，不仅凭 infinity type：
若 $\epsilon(u)$ 的三次部分为 $\omega^e$，则
$\omega^{r_\gamma}=\omega^e\epsilon_2(u_2)^{-1}$，
而
$\vartheta_{l_j}(h_\gamma)
 =\omega^e\vartheta_{l_j}(u_{17})^{-1}$。
相消后正是原
$\eta_j(u)=\epsilon_2(u_2)^{-1}\vartheta_{l_j}(u_{17})$。
所有 $\gamma$ 都已有单位 idèle 代表，所以这也包含原在3处
不分歧但可能非平凡的 uniformizer 值；
没有把它另设为1。

因此 full corestriction 和 $1/18$ 投影在同一循环上准确给
$[L:H]Z_j$。这一步是实际循环的等式，不再只在复形式或
$p$-adic形式的评值上读取一个特征。

### 16.3 每一完整列中的所有项都返回同一个固定值

对同一个原 $Q^+$ 定义
$$
 A(t)=\sum_{i=0}^2\omega^i z_{1,i,t},\qquad
 B_a=A(s^{2a})
 =(e_A^-)_*\widehat{\psi_{s^{2a}}}
       P_Q(q_-d_{s^{2a}}),\quad a=0,1,2.
 \tag{77}
$$
后一式就是(58)，全2加权、同一 $q_-$ 和 degree17 图均保留。
由(26)和 R1027§7的原 $\delta$ 配对，
$A(\omega t)=\omega A(t)$、
$A(\delta t)=-A(t)$。
两式是在相同点群及 coefficient module 中的等式，不是
把一般纤维上的系数 $\omega$ 误作 CM 端同态。

令 $h_\gamma=s^{k_\gamma}$。
(76)对 $j=10$ 给
$n_\gamma\equiv6r_\gamma-k_\gamma\pmod{18}$。
而(75)在(35)的整项中给
$$
 \sum_i\omega^i z_{\gamma,i,t}
   =\omega^{r_\gamma} A(h_\gamma^{-1}t).
$$
代入原
$t=t_{\gamma,a}=s^{2a-10n_\gamma}$，准确有
$$
 h_\gamma^{-1}t_{\gamma,a}
   =s^{2a-6r_\gamma-9n_\gamma}
   =s^{2a}\omega^{-r_\gamma}\delta^{-n_\gamma}.
$$
所以(35)中这个 $\gamma$ 的整项是
$(-1)^{n_\gamma}\omega^{r_\gamma}
 \omega^{-r_\gamma}(-1)^{n_\gamma} B_a=B_a$。
没有跨 $\gamma$ 的剩余抵消。于是
$$
 \boxed{
 C_a=[L:K]B_a,\qquad
 J_j=6[L:H]\sum_{a=0}^2
             \zeta_9^{-l_ja}B_a .
 }
 \tag{78}
$$
这也独立核回(36)的 DFT 常数。
degree17 单独商满足
$\gamma\psi_t=\psi_{h_\gamma^{-1}t}$；
其目标有序二挠基同时循环移位 $-r_\gamma$，
即 $\gamma d_t=\sigma^{-r_\gamma}d_{h_\gamma^{-1}t}$。
因而(77)的 $S'$ 表示与(75)使用的是同一实际 lift，
不需要另选 full2 基或重新归一微分。

所有身份先在特征零的规范图上证明，再在原好约化处逐图约化。
$Q^+$ 是该特征中的固定截面；只把上述相等图对它评价，
不对它附加一个未经定义的 $\gamma$ 作用。
由(78)，除原固定有限次数因子的损失外，三个完整原值是否全为零的
问题已经准确回到这三个指定 $B_a$ 是否全为零。
式(78)不证明其中任何 $B_a$ 非零；同样不能从全局
$P_Q$ 本原而越过其固定标记评价的核。


### 16.4 实际最小级点域的完整次数

可在原许可范围内准确选取 $L_0=K(E_{27}[306])$。
原 $H$、所有规范商图、$a$ 与 $\vartheta=2/a$ 均在其中；
$\zeta_9$ 由原 Weil pairing 已在该域。
式(73)的 mod9 像准确是
$1+3\mathcal O_K/(9)$，阶9；
mod2、mod17 的像分别是阶3的全单位群、
阶288的全单位群。
它们独立：分别只改变 $u_2$、取 $u_3\in1+3\mathcal O_{K,3}$、
或只改变 $u_{17}$，其它局部分量均取1，
就在另外两个模数上保持恒等。
所以
$$
[L_0:K]=3\cdot9\cdot288=7776=6^5,\qquad
[L_0:H]=432.
$$
这是同一原级点域的完整像计算，不是只给一个上界。
因而在此最小选择下，(78)的次数不损失任何 $p\ge5$ 的部分。
若原实现使用额外扩大的 $L\supset L_0$，仍须保留实际的
$[L:L_0]$ 因子，不能把它默删。

## 17. 新曲面的真实 Fricke 反交换及 canonical 点值

本节仍只运输已给的同源，不能把新 canonical 点的存在当作非零。
令 $F$ 是 R995/R1027 的原三同源；在原 Tate 参数中
$t\mapsto1/27-t$，且
$F^*\omega_{1/27-t}=\delta\omega_t$。
相同的三同源在(52)上给 $F'$，其基映射是
$(X',Y')\mapsto(X',-1-Y')$，因为
$$
 \frac1{27}+\frac{Y'^2}{27(2Y'+1)}
 =\frac{(Y'+1)^2}{27(2Y'+1)}.
$$

完整二核的方向也可直接在原方程中核定。
三 Vélu 商在进行目标平移缩放前的 $x$ 坐标是
$x_3=x+t/x+t^2/x^2$；
其与目标 Tate 坐标的关系是 $x_3=-3x_F-1/3$。
在原二挠根 $x=-u^2$、$t=u^2(1-2u)$ 上，这给
$$
 x_F=-(u-1/3)^2.
$$
而 $C$ 的双曲 involution $(z,w)\mapsto(z,-w)$ 恰将
$u$ 换成 $1/3-u$。所以原3同源运输二核的真正 lift 是
$$
 \widetilde F:\mathcal D\longrightarrow\mathcal D,
 \qquad (A,h)\longmapsto(-A,h).
 \tag{79}
$$
它固定 $z$、改变 $w$ 的符号，并且在 $q_-$、$q_+$ 上都诱导
$[-1]$。它与 $\sigma,\kappa,\epsilon$ 交换；没有另作一次
有序二核的排列。

因此(9)的二同源倍率 $6u-1$ 在(79)下恰取负。
先二后三的 degree6 复合与先三后二的复合具有相同的完整核
$C_2+\langle P_3\rangle$、相同的靶 Tate 方程，
但其微分倍率分别为 $\delta(6u-1)$ 和
$-\delta(6u-1)$。在特征零中同核商的唯一靶同构因此为 $[-1]$，
所以得到实际图恒等式
$$
 F_{f\iota P}\circ\phi_{2,P}
   =-\phi_{2,\widetilde F P}\circ F_{fP}.
 \tag{80}
$$
然后约化这个同源恒等式；不在正特征仅凭微分来猜两个同源相等。

对(80)取真正的对偶，并使用(39)的 Picard 拉回定义，
$$
 F'^*\mathcal T_\omega(Q)
       =-\mathcal T_\omega(F^*Q).
$$
原 $Q^+$ 的 $F^*$ 特征是 $-\delta$，故
$$
 \boxed{F'^*P_Q=+\delta P_Q.}
 \tag{81}
$$
该式保全相对 Picard 中的原系数；此前需减去的垂直/基类仍在
同一群中为零。它也逐式核回(70)的 holomorphic 方向：
$F'^*\Omega'_1=+\delta\Omega'_1$。

在第14节的 canonical 好模型，源参数为 $\zeta=X'/Y'$，
目标参数满足
$\zeta_F=-\zeta/(1+r)$，$r=1/Y'$。
由于原 raw 微分是 $\omega_t=\zeta\omega_{\min}$，故
$$
 F'^*\omega_{\min}
  =\delta\frac{\zeta}{\zeta_F}\omega_{\min}
  \longrightarrow-\delta\omega_{\min}.
$$
它在 $E_4$ 上的真实特化因此是几何 $[-\delta]$，
而其 Picard pull 为对偶 $[+\delta]$。
所以(81)说明
$$
 P_Q(O)=(e_{E_4}^-)_*P_Q(O),
 \tag{82}
$$
与原 $e_A^-$ 一样选择几何 $[\delta]=+\delta$。
这里特征相同，不出现原 $S$ canonical 点证明中的相反特征；
不能把 R1027 的 $6Q(O)=0$ 无证搬到 $P_Q(O)$。

这个点还能准确回到一个已标记的原有限纤维。
取第14节的 $A=\infty$ 支 $h/A^2\to c$，$a=c^{-1}$，
以及原 $b_{2,0}=(-a^2/4,-1/2)$。
此时 $q_+=O$，第12节给
$q_+^*P_Q=\mathscr R_{\omega^2}$。
$\sigma^i$ 对这三个支的标号正是 $a\mapsto\omega^i a$，
故由(19)、(25)有
$$
 R_i(O)=\omega^{-i}[\omega^{-i}]R_0(O),\qquad
 R_0(O)=\widehat\phi_{2,0}Q^+(b_{2,0}).
$$
将它代入 $\mathscr R_{\omega^2}$，
原几何单位 projector 给
$\sum_i\omega^i[\omega^{-i}]=3(e_A^-)_*$。
最后使用(61)中同一个 $I$，得到
$$
 \boxed{
 P_Q(O)=
 3I\,(e_A^-)_*\widehat\phi_{2,0}Q^+(b_{2,0}).
 }
 \tag{83}
$$
这保留原 $-3a$ 微分倍率、$P_3\mapsto(0,-2)$ 和 $I$ 的下降，
没有只凭 $j=0$ 更换源模型。

同时必须区分另一个商的坏点：
这个 $A=\infty$ 支在 $q_-$ 下是
$(-c,-1/2)\in B'[2]$，属于(52)的 $\mathrm{IV}^*$ 纤维，
不是原 $S$ 在 $t=1/54$ 的好 CM 纤维。
在 $\mathcal D$ 的三重好化后，其稳定子
$\kappa\sigma^{-1}$ 固定这一个支，并在原 canonical 好纤维上
作用为几何 $[\omega^2]$。
因(49)的真正下降不变性，$\mathscr R_\omega$ 在这个好化纤维的
值被 $[\omega^2]-1$ 杀，因而被3杀；在原倒6系数群中为零。
这是好化纤维中的点值结论，不把 $\mathrm{IV}^*$ 的整个
Néron 加性部分称为零。

式(83)是下一步可实际使用的 canonical 基值。
原三个 $B_a$ 则仍须由同一 $P_Q$ 在(77)的 degree17 标记纤维评价；
本节没有由一个全局截面或这个基值自动推出其中某一项非零。

## 18. 三个完整影子同时为零，确实给两个 CM 方向的全 $p$ 整除

本节的前提是原三个完整值
$J_{10},J_4,J_{16}$ 在同一个系数素位为零。
R804/R806/R811 的中央关系目前只给带完整外项的线性行，
尚未从原通常全 $\Sha$ 条件推出这三个值分别为零；
本节不补写这个未付前提。

固定一个满足前述好约化条件的惰性辅助素数 $q\equiv-1\pmod6$，
以及 R1027§8 的规范最短反 Frobenius 截面 $Q_{\min}$。
在原倒6点群中，取
$$
 Q^+=\frac13(1+\omega^2\tau^*+\omega\tau^{2*})Q_{\min},
 \qquad Q^-=c_E Q^+ .
 \tag{84}
$$
这里 $c_E$ **只共轭代数系数**，
$c_E(\omega)=\omega^2$、$c_E(\delta)=-\delta$，
固定所有实际点、几何映射和基坐标。
若作用到整个 Fourier 系数域，取
$c_E(\zeta_9)=\zeta_9^{-1}$。
这与下面真实剩余域映射
$\mathrm{Fr}:\alpha\mapsto\alpha^q$ 严格区分；
后者作用于点、截面方程和几何 CM 端同态，
在系数张量因子上按线性作用延拓。

### 18.1 原截面的下降及实际 Frobenius 方向

规范 $Q_{\min}$ 来自原反 Frobenius twist；
在倒6后准确有
$\mathrm{Fr}_{\rm coeff}Q_{\min}=-Q_{\min}$。
由于原 $S,\mathcal D,q_-$ 及二商公式都在 $\mathbf F_q$ 上，
而
$\mathrm{Fr}\tau\mathrm{Fr}^{-1}=\tau^{-1}$、
$\mathrm{Fr}\sigma\mathrm{Fr}^{-1}=\sigma^{-1}$，
(39)、(45)、(53)、(84)逐项给
$$
 \mathrm{Fr}_{\rm coeff}Q^+=-Q^-,
 \qquad
 \mathrm{Fr}_{\rm coeff}\mathscr R_\omega(Q^+)
       =-\mathscr R_{\omega^2}(Q^-),
 \qquad
 \boxed{\mathrm{Fr}_{\rm coeff}P_Q=-c_E P_Q.}
 \tag{85}
$$
最后一个等式仍在同一个 $q_-$ 商上：
$c_E$ 同时共轭 $Q^+$ 的系数及(45)的权，
所以 $q_-^*c_EP_Q=\mathscr R_{\omega^2}(Q^-)$。
这里没有把 $q_-$ 换成 $q_+$，也没有把一般纤维的
$\omega$ 系数冒作几何自同源。
由实际三度下降的单射性，拉回后的等式给(85)。

### 18.2 全9下降、规范二核及全部17标号

先固定原源 $A=E_{27}$ 的真正 $\mathbf Q$ 模型及
$P_3=(0,0)$，即 R1006(15)–(16) 的
$X=9x_A,\ Y=-27y_A$。
它在 canonical 纤维的 full $\Gamma$ 级对象也有该下降。
一个直接的矩阵核验如下：令 $\Omega_R$ 为其正本原实周期，
用与这个模型及 $P_3$ 相容的周期生成元
$\Omega=\Omega_R/(1-\omega)$。
它满足 $\bar\Omega=-\omega\Omega$；
R1006(14) 的原基因此满足
$$
 c\boldsymbol\beta=h\boldsymbol\beta,\qquad
 h=\operatorname{diag}(-1,1)\in G_\Gamma .
 \tag{86}
$$
第二个3级点是 $-\Omega_R/3$，正对应 $(0,0)$。
这只是显写既有 canonical 模型的下降；
若原 CM 生成元采用另一个合法单位标号，
须对原两核和全部权同时作§16的重标记，
不能只改这个 $h$ 而留下其它图不动。

任一惰性 $q$ 的分解群 Frobenius 在原有限级域上写成
$\gamma c$，$\gamma\in G_K$。
§16的矩阵 $G_\gamma$ 与(86)给其完整矩阵
$G_\gamma h\in G_\Gamma$。
其 determinant 正是 $q\bmod9$，故原 Weil pairing 的
$q$ 次幂共轭也被保留；没有把 determinant 置为1，
亦没有遗漏一个 mod9 相位。
源微分 $\omega_A$ 与 $P_3$ 在 $\mathbf F_q$ 上；
规范商的 full9、微分及图均沿这个固定源运输。

在同一原有限域中可取好约化嵌入，使
$a^3=4$ 的规范根约化为 $\mathbf F_q$ 的唯一立方根。
确实 $q\equiv2\pmod3$ 使立方映射在 $\mathbf F_q$ 可逆，
而§16的原 CM Galois 作用可循环三个二核。
因此这只是一次已有的完整标号重排；
三个 $J_j$ 同时为零、以及三个 $B_a$ 同时为零均不改变。
此后 $C_{2,0}$ 在 $\mathbf F_q$ 上，准确有
$$
 \mathrm{Fr}(C_{2,i})=C_{2,-i}.
$$
定义 $h_q\in\mathcal C_{18}$ 为
$\mathrm{Fr}(C_{17,0})=C_{17,h_q}$。
原 $C_{17,t}=\bar t C_{17,0}$ 与
$\mathrm{Fr}[\alpha]=[\bar\alpha]\mathrm{Fr}$ 给
$$
 \mathrm{Fr}(C_{17,t})=C_{17,h_qt^{-1}},\qquad
 \mathrm{Fr}(\psi_t)=\psi_{h_qt^{-1}} .
 \tag{87}
$$

关键是不能在(87)后再无故插入 $\epsilon$。
原有序 lift $d_t$ 的定义是(56)：
$\sigma^i d_t$ 标记 $\psi_t(C_{2,i})$。
真实 Frobenius 一方面把 $\sigma^i$ 变为 $\sigma^{-i}$，
另一方面把源 $C_{2,i}$ 变为 $C_{2,-i}$。
所以两次反号抵消；由完整有序二核模问题的唯一性，
$$
 \boxed{\mathrm{Fr}(d_t)=d_{h_qt^{-1}}.}
 \tag{88}
$$
也可用全盖的三根直接核定：
$u_i(A)=(1+\omega^iA+\omega^{-i}A^{-1})/6$，
满足
$\mathrm{Fr}(u_i(d))=u_{-i}(\mathrm{Fr}(d))$。
式(88)在同一个 $\mathcal D$ 和同一个 $q_-$ 内成立。

所有这些实际点与图都在 $\mathbf F_{q^2}$ 上。
因为 $A/\mathbf F_q$ 的真实端同态满足
$\mathrm{Fr}^2=[-q]$，其在2核和17核的作用分别是恒等及
投影标量；在原 full9 基上的标量 $-q$ 也属于 $G_\Gamma$，
因为 $-q\equiv1\pmod3$。
它固定有序二核与原完整 quotient 对象，故也固定 $d_t$。
原 $Q_{\min}$ 和(85)同样在 $\mathbf F_{q^2}$ 上定义。

### 18.3 三个指定值的真实半线性交换公式

延伸(77)的记号为
$$
 B(t)=(e_A^-)_*\widehat{\psi_t}\,
                P_Q(q_-d_t),\qquad B_a=B(s^{2a}).
$$
真实 Frobenius 共轭几何 CM 端同态，因而
$\mathrm{Fr}\,e_A^-=e_A^+\,\mathrm{Fr}$；
系数共轭则给 $c_Ee_A^-=e_A^+$。
由(85)、(87)、(88)，得到准确的有限点群等式
$$
 \boxed{\mathrm{Fr}\,B(t)=-c_E B(h_qt^{-1}).}
 \tag{89}
$$
该式的两个共轭来源已分别支付，不使用一个不存在的
$\mathbf C_p$ 连续自同构。

写 $h_q=s^k$，并令
$\zeta_6=\zeta_{18}^3=-\omega^2$。
由§16的两个真实关系，
$B(\omega t)=\omega B(t)$、$B(\delta t)=-B(t)$，
准确有 $B(s^3t)=\zeta_6B(t)$。
对每个 $a\in\{0,1,2\}$，唯一选择
$a'\in\{0,1,2\}$ 和 $m_a\bmod6$ 使
$$
 k-2a\equiv2a'+3m_a\pmod{18};
 \qquad a'\equiv2k-a\pmod3 .
$$
所以(89)在三个固定值上成为
$$
 \boxed{\mathrm{Fr}\,B_a
       =-\zeta_6^{-m_a}\,c_EB_{a'}.}
 \tag{90}
$$
这包含全部 $\mu_6$ 相位；$a\mapsto a'$ 是一固定点加一对交换。
这里的 $c_E$ 对系数的作用不是
$\zeta_9\mapsto\zeta_9^q$；内在 Weil pairing 的后者已在
(86)–(87)的 full9 下降中单独处理。

### 18.4 同一系数素位的三个零，推出实际点的全 $p$ 整除

原 $P_Q$ 的系数只在 $\mathbf Z[1/6,\omega]$；
$\zeta_9$ 只用于三个值之间的 Fourier 权。
令
$$
 U_a=\widehat{\psi_{s^{2a}}}\,P_Q(q_-d_{s^{2a}})
       =U_{1,a}+\omega U_{2,a},
 \qquad
 U_{i,a}\in A(\mathbf F_{q^2})\otimes\mathbf Z[1/6],
$$
并定义真正的点群元素
$$
 T_a:=U_{1,a}+[\omega]U_{2,a}
          \in A(\mathbf F_{q^2})\otimes\mathbf Z[1/6].
 \tag{91}
$$
这里只在固定 CM 曲线 $A$ 上使用真正的 $[\omega]$。
由于 $e_A^-$ 选择几何 $[\omega]=\omega$，
而 $e_A^+$ 选择几何 $[\omega]=\omega^2$，准确有
$$
 B_a=(e_A^-)_*T_a,\qquad
 c_E B_a=(e_A^+)_*T_a,\qquad
 T_a=B_a+c_EB_a .
 \tag{92}
$$
这给两个方向的同一个实际点；并未把另一个 mixed motive 的
未付值替代为所需最高值。

现令 $p\ge5$ 在 $K$ 分裂，$p\mid q+1$，并避开原固定分母。
取原系数域中任一 $\mathfrak P\mid p$，其下的
$K$ 素位记为 $\mathfrak p$。
使用原最小有限级域 $L_0$：
§16的 $[L_0:K]=6^5$，所以其完整 trace 常数是 $p$ 单位。
若使用更大 $L$，以下同样适用，但须要求
$p\nmid[L:L_0]$，或先准确除掉原已显示的重复 trace 因子。

假设
$$
 J_{10}\equiv J_4\equiv J_{16}\equiv0\pmod{\mathfrak P}.
 \tag{93}
$$
(37)、(78)及完整 trace 常数立即给
$B_0=B_1=B_2=0$ 于同一个模 $\mathfrak P$ 点群。
因为 $B_a$ 本身的系数在 $K$，
剩余域扩张的忠实性给其模 $\mathfrak p$ 也为零。
真实 Frobenius 在这个系数张量群上线性作用，故(90)迫
$c_EB_0=c_EB_1=c_EB_2=0$ 于同一 $\mathfrak p$。
最后(92)给
$$
 \boxed{
 T_a\in p\bigl(A(\mathbf F_{q^2})\otimes\mathbf Z[1/6]\bigr),
 \qquad a=0,1,2.
 }
 \tag{94}
$$
换言之两个 CM 方向确实同时为零。
这不是把一个 $\mathfrak p$ 同余形式地改名为
$\bar{\mathfrak p}$ 同余，而是使用原辅助素数处的真实
Frobenius、原完整标记和同一个 $T_a$ 证明的全 $p$ 整除。
清原固定2、3分母后，(94)也按同样方式给真正有限群中的
$p$ 除点。

### 18.5 $p^2$ 个除点与最小 Frobenius 核的准确交数范围

因为 $\mathrm{Fr}^2=[-q]$，
$$
 A(\mathbf F_{q^2})=A[q+1],\qquad
 \#A(\mathbf F_{q^2})=(q+1)^2 .
$$
由 $p\mid q+1$，全 $A[p]$ 都在 $\mathbf F_{q^2}$ 上。
因此一旦(94)成立，每个 $T_a$ 确有 $p^2$ 个
$\mathbf F_{q^2}$-有理 $p$ 除点（先清固定分母）。
但是这并不自动给一个次数 $O(q)$ 的交函数的 $p^2$ 个零。

准确地说，(90)与其系数共轭在实际点群上合成
$$
 \mathrm{Fr}\,T_a=[-\zeta_6^{m_a}]T_{a'}.
 \tag{95}
$$
在唯一固定的指标 $a=a'$ 处，记
$u=-\zeta_6^{m_a}\in\mu_6$，
则 $T_a\in\ker(\mathrm{Fr}-[u])$。
真实对偶恒等式
$\mathrm{Fr}^{\dagger}=-\mathrm{Fr}$、
$[u]^\dagger=[u^{-1}]$、
$\mathrm{Fr}[u]=[u^{-1}]\mathrm{Fr}$ 给
$$
 (\mathrm{Fr}-[u])^\dagger(\mathrm{Fr}-[u])=[q+1],
 \qquad
 \deg(\mathrm{Fr}-[u])=q+1 .
 \tag{96}
$$
其 $p$-主部分只有一个 $\mathbf Z_p$ 方向的长度：
在 $A(\mathbf F_{q^2})[p^\infty]$ 上，
$[u^{-1}]\mathrm{Fr}$ 是平方为1、交换两条 CM 线的 involution；
$p$ 为奇数使其正负特征群均为秩一。
所以(94)给的 $p^2$ 个除点中，恰有 $p$ 个仍满足
同一个 $\mathrm{Fr}-[u]$ 关系。
在另外两个交换指标处，(95)给的是两个标记点之间的关系，
并不使它们每一个都落入这个固定指标的同一核。

若改用完整 $\mathrm{Fr}^2-1$，它确实包含全部 $p^2$ 个除点，
但次数是 $(q+1)^2$；不能把这个次数偷换成(96)的 $q+1$。
因此本节支付了全 $p$ 整除及其实际两个 CM 方向，
而从两个独立标记取得一个新的 $p^2$ 级交数下界、
与截面高度比较并迫使某个完整 $J_j$ 非零，
仍需额外的真实几何关系。
