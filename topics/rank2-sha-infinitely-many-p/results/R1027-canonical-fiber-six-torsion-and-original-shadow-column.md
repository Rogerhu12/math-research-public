# R1027 — 原 canonical fiber 上的统一六挠限制与54图中的准确零列

日期：2026-11-27。会话：Astra-rank2-Sha-0b097461-20261127。

**已证明。** 对原 full9 曲面的每个好约化素数 $q\ge5$，任意几何
Mordell–Weil 截面在原光滑 canonical fiber 上的值都被6杀掉。
这一结论不假设该约化满足 Tate，不假设新截面存在，也不使用
Guo–Yang 预印本。它来自同一个实际三同源的图 push、甲板自同构的
图 pull 与无穷极小模型之间的准确符号差。

因此，在 R1014 的原54图交公式中，约化基点恰为无穷点 $O_B$
的那些项在固定倒6系数中逐项为零。这里只删除这个确切的零列；
其余有限 CM fiber、原最高投影和完整 Galois trace 仍须实际处理。
本篇没有声称完整 shadow、全局 AJ 或指定普通局部值已非零。

## 1. 同一模型、两个操作及其方向

固定
$$
 K=\mathbf Q(\delta),\quad \delta^2=-3,\quad
 \omega=(-1+\delta)/2,
$$
以及 R991、R1014 的原曲面
$$
 B:\ v^3=t(1-27t),\qquad
 S:\ y^2+xy+t y=x^3.
 \tag{1}
$$
原基坐标是
$$
 X=-3v,\qquad Y=-27t,\qquad Y^2+Y=X^3.
$$
用 $O_B$ 表示基曲线的原点，用 $\mathcal O$ 表示椭圆曲面的零截面。
两个坏基点是 $T=(0,0)$ 与 $-T=(0,-1)$，相应纤维为 $I_9,I_3$。

R1014 §1 已逐图支付对全部 $q\ge5$ 的同一光滑、射影、相对极小
约化模型；无穷没有附加坏纤维。以下可在任意包含 $\delta$ 的
代数闭常数域上讨论截面。

实际甲板自同构是
$$
 \tau_S:(t,v,x,y)\longmapsto(t,\omega v,x,y),
 \quad \tau_B(X,Y)=(\omega X,Y).
 \tag{2}
$$
本篇对截面使用它的 **pull** 操作
$$
 \mathcal T Q(b)=Q(\tau_B b),
 \tag{3}
$$
其中使用(1)的原仿射纤维坐标比较两点。换言之，$\mathcal T Q$
的除子类是 $\tau_S^*[Q]$，不是 $\tau_{S*}[Q]$。

实际次数三有理自映射 $F:S\dashrightarrow S$ 是已付的
Vélu 三同源再接原 $\delta$ 缩放，覆盖
$$
 \iota_B:(t,v)\longmapsto(1/27-t,v),
 \qquad \iota_B(X,Y)=(X,-1-Y)=[-1](X,Y).
 \tag{4}
$$
见 [原实际三同源笔记](../notes/2026-11-27-congruence-i9-i3-surface-and-correspondence-scope.md)
§2 与 R995。写 $F_b:S_b\to S_{\iota_Bb}$。
本篇对截面使用它的 **push** 操作
$$
 \mathcal FQ(b)=F_{\iota_Bb}\bigl(Q(\iota_Bb)\bigr).
 \tag{5}
$$
图的严格像是这个截面；基上的 $[-1]$ 次数是1，所以没有把
$F_*[Q]$ 错乘一个3。

若以解消图定义 $F_*$，严格变换与 total transform 的差支撑在
坏纤维，推出后仍是垂直除子。故模掉平凡格时，$F_*[Q]$ 的
Mordell–Weil 类准确是(5)。这些异常曲线不产生另一个水平截面。
在光滑纤维，尤其下文的 $O_B$ 处，三挠核为有限 étale 子群，
三同源直接延拓为光滑椭圆族之间的同源，无需这个垂直修正。

## 2. 在整个秩二纯实现上，差确实落入旧平凡格

令
$$
 \Omega=\frac{dt}{v^2}\wedge
       \frac{dx}{2y+x+t}.
 \tag{6}
$$
它是原二形式，唯一零纤维为 $O_B$。直接从(2)得到
$$
 \tau_S^*\Omega=\omega\Omega.
 \tag{7}
$$
原规范 Vélu 商保持不变微分，随后 $\delta$ 缩放使
$$
 F_b^*\omega_{\iota_Bb}=\delta\,\omega_b.
 \tag{8}
$$
式(4)在基上把 dt 取负。因此**曲面图 pull**的准确符号为
$$
 F^*\Omega=-\delta\Omega.
 \tag{9}
$$
F 的 generic degree 为3，故在超越二形式上
$F_*F^*=3$，从而**曲面图 push**为
$$
 F_*\Omega=\frac{3}{-\delta}\Omega
          =\delta\Omega.
 \tag{10}
$$
不能把(9)与(10)互换。

特征零中，原旧平凡格由 $\mathcal O$、纤维及 $I_9,I_3$ 的
非恒等分量生成，秩为12，等于 $h^{1,1}$；原完整超越部分
$T(S)_{\mathbf Q}$ 因而秩2，复化就是 $H^{2,0}\oplus H^{0,2}$。
式(7)、(10)及其复共轭，同时给
$$
 \boxed{F_*=1+2\tau_S^*
        \quad\text{on }T(S)_{\mathbf Q}.}
 \tag{11}
$$
因为 $1+2\omega=\delta$、$1+2\omega^2=-\delta$，
这里不是只在一条 holomorphic line 上核一个标签后忽略另一条线。

三个对应都保持旧平凡子空间。对 $F_*$，零截面仍到零截面，
垂直曲线仍到垂直曲线；其 pull 的零截面原像是原三挠截面，
这些在有理 NS 中也属于旧平凡格。因此(11)同样描述
$H^2/T_{\rm old}$ 上的操作。

选择任意 $\ell\ne q,2,3$。Betti–étale 比较与 R1014 §1 已付的
光滑适当基变换，把这些**同一有限图对应**和旧除子类一起运输
到 $S_{\overline{\mathbf F}_q}$。旧类的交矩阵非退化，仍保持秩12。
因此
$$
 (F_*-1-2\tau_S^*)H^2_{\rm et}
       \subset T_{{\rm old},\ell}
 \quad\text{on every }q\ge5.
 \tag{12}
$$
这只使用原纯实现上的对应恒等式，不调用约化的除子 Tate 满射，
也不假设混合 AJ 的跨素数保真。

## 3. 实际截面的三挠修正，不能删去

Kummer 列给 NS 的 $\ell$-adic cycle map 单射；
相对 Shioda–Tate 列把 NS 模平凡格识别为实际 Mordell–Weil 群。
原 $j$ 非常数，故常数 trace 为零。由(12)，对于任意几何截面 Q，
$$
 A(Q):=\mathcal FQ-Q-2\mathcal TQ
 \quad\text{是一个 torsion 截面。}
 \tag{13}
$$
R1014 §4 对 torsion 的完整证明适用于所有 $q\ge5$，独立于该文
§2 的条件 Tate 输入：零高度式与 $I_9,I_3$ 的全部分量贡献迫
非零 torsion 只落在 $I_9$ 分量3或6，且分量映射的核为零。
原 $(0,0)$ 已给 order3，故整个几何 torsion 准确为
$$
 \langle P_3\rangle,\qquad P_3=(0,0),\qquad
 \operatorname{ord}(P_3)=3.
 \tag{14}
$$
因此真正得到的是
$$
 \boxed{\mathcal FQ=Q+2\mathcal TQ+\epsilon(Q)P_3,
       \quad\epsilon(Q)\in\mathbf Z/3.}
 \tag{15}
$$
本篇保留 $\epsilon(Q)$；纯实现不决定它为零。
(15)是截面的群等式，所以在下文的光滑纤维上可以真实求值，
不只是有理 NS 类的形式关系。

## 4. 无穷极小纤维上的两个准确作用

置
$$
 r=t^{-1},\quad z=v/t,\quad z^3=r^2-27r,
 \qquad u=z^2x,\quad w=z^3y.
$$
原好模型是
$$
 w^2+zuw+(r-27)w=u^3,\qquad
 \omega_{\rm old}=z\,\omega_{\rm min}.
 \tag{16}
$$
在 $O_B:r=z=0$，纤维
$$
 C_\infty:\ w^2-27w=u^3
 \tag{17}
$$
经 $(u,w)=(9X,-27Y)$ 与原 $B:Y^2+Y=X^3$ 同构。
在这个同构中
$$
 [\omega](u,w)=(\omega u,w),\qquad
 P_3(O_B)=(0,0)\in\ker[\delta].
 \tag{18}
$$
事实上整个(14)在此纤维的像恰为 $\ker[\delta]$：
它们被 $[\omega]$ 固定，所以 $[1+2\omega]=[\delta]$ 作用为[3]，
而该核次数恰为3。

先核 $\mathcal T$。实际自同构 $\tau_S$ 把 z 变为 $\omega z$，
故在(17)上的**直接**作用为
$(u,w)\mapsto(\omega^2u,w)=[\omega^2](u,w)$。
但(3)是图 pull。对其截面坐标，
$$
 u_{\mathcal TQ}(b)=z(b)^2x_Q(\tau_Bb)
        =\omega\,u_Q(\tau_Bb),
 \qquad
 w_{\mathcal TQ}(b)=w_Q(\tau_Bb).
$$
因此准确有
$$
 \boxed{(\mathcal TQ)(O_B)=[\omega]Q(O_B).}
 \tag{19}
$$
把直接 fiber 作用 $[\omega^2]$ 填进(19)会把关键方向翻反。

再核 $F$。由(4)，
$$
 r'=\frac{27r}{r-27},\qquad
 z'=\frac{27z}{r-27},\qquad
 \frac{z'}z\bigg|_{O_B}=-1.
 \tag{20}
$$
结合(8)、(16)给
$$
 z'F^*\omega_{\rm min}'=\delta z\,\omega_{\rm min},
 \qquad
 F_{O_B}^*\omega_{\rm min}=-\delta\,\omega_{\rm min}.
 \tag{21}
$$
所以**实际光滑纤维同源**是 $[-\delta]$，而不是 $[\delta]$。
这里不能仅在正特征用微分相同推出同源相同：
先在同一特征零好模型上确定该恒等式，再约化。
也可从原 Vélu x 式直接核其有理表达：
$$
 x_F=-\frac13\left(x+\frac t x+\frac{t^2}{x^2}\right)-\frac19,
$$
在(16)、(20)中取 $O_B$ 得
$$
 u_F=-\frac13\left(u+\frac{729}{u^2}\right),
 \qquad
 X_F=-\frac{X^3+1}{3X^2}.
 \tag{22}
$$
这是原 $\pm\delta$ 同源的 x 坐标；(21)在特征零固定负号。
该有理恒等式定义在 $\mathbf Z[1/6,\delta]$，其光滑纤维同源
于是对每个 $q\ge5$ 保留相同符号。

由于 $\iota_B$ 固定 $O_B$，式(5)的截面 push 求值为
$$
 \boxed{(\mathcal FQ)(O_B)=[-\delta]Q(O_B).}
 \tag{23}
$$
(10)是曲面二形式上的图 push 值 $\delta$；
(23)是光滑 fiber 上同一个实际同源的值 $-\delta$。
两者不同的原因正是基 $[-1]$ 和(16)的一阶微分缩放，
不能把曲面二形式的符号直接搬到 fiber。

## 5. 统一六挠结论及除子形式

把(19)、(23)代入真实等式(15)，得到
$$
 [-\delta]Q(O_B)-[1+2\omega]Q(O_B)
       =\epsilon(Q)P_3(O_B).
$$
即
$$
 [-2\delta]Q(O_B)=\epsilon(Q)P_3(O_B).
$$
右侧被 $\delta$ 杀掉；左侧再作用 $\delta$ 是
$[-2\delta^2]=[6]$。故
$$
 \boxed{[6]Q(O_B)=O
 \quad\text{对全部 }q\ge5\text{、全部几何截面 }Q.}
 \tag{24}
$$
没有假定 Q 非零，没有由秩预测 Q 存在，也没有漏掉(15)的三挠项。

还可把(24)写成原交公式需要的除子版本。
若 $D\in\operatorname{Pic}(S_{\overline q})$ 且 $D\cdot\mathfrak f=0$，
其一般纤维上的 degree0 线丛由一个实际点 Q 表示。
$D-[Q]+[\mathcal O]$ 在一般纤维平凡，故可用垂直除子及基的
线丛表示。它们在光滑纤维 $C_\infty$ 上限制平凡：
坏分量与它不相交；纤维自身的法线丛平凡；基线丛拉回也平凡。
因此 R1014 的 restriction 点满足
$$
 r_{O_B}(D)=Q(O_B),\qquad
 \boxed{[6]\,r_{O_B}(D)=0.}
 \tag{25}
$$
这也包括由原有限 Chow projectors 对 D 作用后得到的 degree0
除子。系数为有理代数数时先保留固定整系数表达，再作线性延拓。

## 6. 对原54图逐项使用，完整 trace 不变

保持 R1011、R1014 的固定系数
$R=\mathcal O_{\mathbf Q(\zeta_9)}[1/d]$，其中可以且必须包含原
$1/18$ 平均和 projector 的分母，所以6已经可逆。
仍只删掉这些固定分母及原图模型的有限坏约化素数。

对任何实际同源图 $\varphi:A=E_{27}\to S_b$，R1014(24)的完整
交理论等式是
$$
 \mathcal S_D(\Delta_\varphi)=\widehat\varphi(r_b(D)).
 \tag{26}
$$
若其约化基点满足 $b=O_B$，则(25)使右侧被6杀掉，所以
$$
 \boxed{\mathcal S_D(\Delta_\varphi)=0
       \quad\text{in }A(\overline{\mathbf F}_q)\otimes R.}
 \tag{27}
$$
这对每张 degree34 图分别成立，保留原 CM 模型及同源方向；
不需要把原图改成一个随意的 j=0 同构。

在原完整公式
$$
 (e_A^-)_*\frac1{18}
 \sum_{\gamma\in\operatorname{Gal}(L/K)}
  \eta_j(\gamma|_H)^{-1}
  \sum_{i=1}^{54}c_i\,
   \widehat{\gamma\varphi_i}
     \bigl(r_{\gamma b_i}(D^+)\bigr)
 \tag{28}
$$
中，$D^+=(e_S^+)_*D$ 仍是 R1014 的正确转置投影。
仅对满足 $\gamma b_i=O_B$ 的实际项应用(27)。
零项的 Galois 共轭、原 $\eta_j^{-1}$ 权、最高 $e_A^-$ 及
$\operatorname{Cor}_{L/H}$ 全部保留并线性作用；没有删去非零项，
也没有把分解群平均冒充全域 trace。

结论(24)是整个几何 MW 的统一 canonical-fiber 限制。
它不声称有限 CM fibers 的值也被6杀掉；原剩余54图求和、跨
普通 p 的非零和局部比较仍须继续支付。


## 7. 实际 Fricke 对应把54图配成27对，且两项相加

本节在(28)的同一有限系数表达中工作，仍排除它的固定坏素数，
并令辅助约化素数素于34。原54个核写成
$C=C_2\oplus C_{17}$；每个 $\varphi_C:A\to S_{b_C}$ 都是
R1006(20)的实际 degree34 商，携带原306级结构。

### 7.1. 完整级结构上的交换图及唯一基 lift

R991 的模群为
$$
 \Gamma=\left\{\begin{pmatrix}a&b\\3c&d\end{pmatrix}
 \in\Gamma_1(3):b-c\equiv0\pmod3\right\}.
$$
令
$$
 D_3=\begin{pmatrix}0&-1\\3&0\end{pmatrix}.
$$
直接乘法给
$$
 D_3^{-1}\begin{pmatrix}a&b\\3c&d\end{pmatrix}D_3
 =\begin{pmatrix}d&-c\\-3b&a\end{pmatrix}.
 \tag{29}
$$
因此 $D_3$ 正规化这个**实际** $\Gamma$，且保持
$b-c\bmod3$，不是只正规化一个忘掉该角色的 $\Gamma_0(3)$。
同时 $D_3^2=-3$ 是中心元，所以它在模基上的平方为恒等。

在 $X_1(3)$ 上，此对应就是对标记三挠子群取商再取对偶标号。
实际 Vélu 商及式(8)的同构已给其参数
$t'=1/27-t$。在原三重覆盖上，所有可能 lift 都是
$$
 (t,v)\longmapsto(1/27-t,\omega^r v),\qquad r=0,1,2.
$$
其平方把 $v$ 乘 $\omega^{2r}$。由(29)的中心平方，唯一允许的
lift 是 $r=0$，即原 $\iota_B=[-1]$。这里同时付了 full9
分量，不能任选另一个三次根。

通用纤维上的 Fricke 同源与原 $F_b$ 有相同的核和靶。
一般纤维的 $j$ 非常数，保零自同构只有 $\pm1$，故两者至多差
一个在连通基上固定的整体符号。这个符号不影响下述交换图：
在3处的同源与素于3的实际商逐项交换，若更换整体符号，图的
左右两条3同源同时变号。最后以已付的实际
$F_{O_B}=[-\delta]$ 固定规范。此论证没有把 $D_3$ 的列矩阵
直接当作 row/adjugate 约定下的几何同源，因而不再翻一次号。

源 $A$ 是 R1006 第3节的 canonical fiber，故得到准确的图
$$
 \boxed{
 b_{\delta C}=-b_C,\qquad
 F_{b_C}\circ\varphi_C
   =\varphi_{\delta C}\circ[-\delta]_A.
 }
 \tag{30}
$$
可以直接看核来核(30)：$F_{b_C}$ 的核为
$\varphi_C(A[\delta])$，而 $[-\delta]$ 把 $C$ 送到 $\delta C$；
两边均为次数102的同源。完整级结构的相等来自(29)及上述
素于3的商的自然性，而非仅由次数与同一个 $j$ 推出。
在完整9级覆盖上同源图唯一；再下降至原 $\Gamma$ 保持该等式。
约化后使用同一图及同一商，不另选一个同 $j$ 的模型。

### 7.2. 核的27对与实际系数的负号

在2处，$\delta=1+2\omega\equiv1\pmod2$，所以
$\delta C_2=C_2$。在17处，$\delta^2=-3$ 是标量，而
$-3$ 在 $\mathbf F_{17}$ 中不是平方。因此 $\delta$ 没有
$\mathbf F_{17}$ 特征线，它在全部18个循环17子群上是无不动点
的对合。于是全部54个核恰分成27对
$$
 \{C,\delta C\}.
 \tag{31}
$$

R1006(18)使用 $C_{r,t}=\bar t C_{r,0}$ 及
$c_{r,t}=\chi_{j,r}(t)^{-1}$，所以核乘 $\delta$ 对应标签乘
$\bar\delta$；不能在一般角色下把这个共轭省略。
这里 $\bar\delta=-\delta$ 与 $\delta$ 在
$\mathbf F_{r^2}^{\times}/\mathbf F_r^\times$ 中相同。
2处该类平凡；17处为唯一的 order2 类。原
$l_j=-5,1,7$ 都是奇数，因此完整原角色在它上的值均为 $-1$。
所以对三个原 $j$ 都有
$$
 \boxed{c_{\delta C}=-c_C.}
 \tag{32}
$$
这用的是原 fixed coefficients，未对 $c_C$ 再作 Galois 或复共轭。

### 7.3. Picard 拉回的对偶方向使评价也取负

令 $D^+=(e_S^+)_*D$ 如(28)，并定义
$$
 u_C=\widehat\varphi_C(r_{b_C}(D^+)),\qquad
 z_C=(e_A^-)_*u_C.
 \tag{33}
$$
在 relative Picard 的 degree0 部分，旧垂直除子及基的线丛限制
为零；原 $P=\pi_2^{\rm tr}$ 与完整 $e_S^+$ 的定义给
$$
 \widehat F_b\bigl(r_{-b}(D^+)\bigr)
      =-\delta\,r_b(D^+).
 \tag{34}
$$
具体地，R995 的 $f=PF^*P$ 在 $e_S^+$ 上等于 $-\delta$；
将图 pull 限制到光滑纤维正是左边的对偶同源。
夹入 $P$ 所减的旧 degree0 类只含垂直类及基的 Picard 类，
不改变这个限制。也可由(15)的真实三挠修正得到同一 relative
Picard 等式；在本节固定倒6系数中该三挠项准确为零。

对(30)取对偶，注意 $[-\delta]^\vee=[\delta]$，得
$$
 \widehat\varphi_C\circ\widehat F_{b_C}
   =[\delta]_A\circ\widehat\varphi_{\delta C}.
$$
与(34)合并便是
$$
 [\delta]_A u_{\delta C}=-\delta\,u_C.
 \tag{35}
$$

最后必须明确原 $e_A^-$ 在点群中的实际作用。
R995 定义 $g=[\delta]^*$，所以在
$\operatorname{Pic}^0(A)=A$ 上，$g$ 作用为**对偶**同源
$[-\delta]$。因此
$$
 (e_A^-)_*=\frac12(1-g/\delta)
          =\frac12(1+[\delta]_A/\delta)
 \quad\text{on }A\otimes R.
 \tag{36}
$$
它选择 $[\delta]_A=+\delta$，不是负号。将(36)作用到(35)，
再用 $3$ 可逆，准确得到
$$
 \boxed{z_{\delta C}=-z_C,\qquad
 c_Cz_C+c_{\delta C}z_{\delta C}=2c_Cz_C.}
 \tag{37}
$$
若漏掉 Picard 拉回中的对偶，会把这里的正重数2误写成零。

### 7.4. 每个 Galois 共轭中均成立，原总迹完整保留

取核对合(31)的任意代表集 $\mathcal R$，$|\mathcal R|=27$。
每个 $\gamma\in\operatorname{Gal}(L/K)$ 都固定几何的 $\delta$、
原 $F$、源 $A$ 及所有这些对应。对(30)先作真正的 $\gamma$
共轭，再约化，故(34)–(37)逐个适用于
$$
 z_{\gamma,C}
  =(e_A^-)_*\widehat{\gamma\varphi_C}
       (r_{\gamma b_C}(D^+)).
$$
不需要 $\gamma$ 属于所选约化素位的分解群。系数始终固定，
并且 $\gamma(\delta C)=\delta\,\gamma C$，所以原(28)准确成为
$$
 \boxed{
 \mathcal S_D(Y_{j,0,R})
 =\frac{2}{18}
  \sum_{\gamma\in\operatorname{Gal}(L/K)}
    \eta_j(\gamma|_H)^{-1}
    \sum_{C\in\mathcal R}c_C\,
       (e_A^-)_*\widehat{\gamma\varphi_C}
           (r_{\gamma b_C}(D^+)).
 }
 \tag{38}
$$
所有 $\operatorname{Cor}_{L/H}$ 项、54图的真实重数及原有限角色
都保留；唯一变化是用(37)逐对相加。它既不证明总和非零，也不
将完整迹改成一个未经支付的分解群平均。

### 7.5. 有限固定纤维的范围与实际剩余对象

原基曲线的三个非零二挠点满足 $Y=-1/2$，故 $t=1/54$。
从原不变量直接算
$$
 j(1/54)=54000.
 \tag{39}
$$
这些点被 $\iota_B=[-1]$ 固定、被 $\tau_B$ 循环排列。
在该实际纤维上 $F_b^*\omega_b=\delta\omega_b$，所以特征零
中 $F_b$ 是已指定的 $[\delta]$，并按同一好模型约化。
其特征零 CM 环恰为 $\mathbf Z[\delta]$：该环已包含在 End 中；
若更大，只可能是 $\mathcal O_K$，但后者的 $j$ 为0，与(39)
不同。此处的 $\omega=(\delta-1)/2$ 只在倒2的 End 中使用。
式(15)于是给
$$
 2Q(\tau_Bb)=([\delta]-1)Q(b)-\epsilon(Q)P_3(b).
 \tag{40}
$$
倒6后这只是三个实际评价的 $\omega$ 关系，没有强迫它们为零。
有限处的原微分无需 canonical fiber 的 $z'/z=-1$ 缩放，
故不能把第4节的 $[-\delta]$ 纤维作用搬到这里。

此外，这两种特殊纤维只影响原54图的一个**固定有限约化集**。
证明如下。源 $A$ 的 CM 环是 $\mathcal O_K$。在
$r=2,17$，该素数均 inert；一条循环 $r$ 核给局部格的一条
$\mathbf F_r$ 直线。$\mathcal O_{K,r}$ 中保持这条线的元素，
模 $r$ 恰为 $\mathbf F_r$，所以商格的乘子环是
$\mathbf Z_r+r\mathcal O_{K,r}$。其它素数不变。因此每一个
原 degree34 目标的特征零 End 都准确为
$$
 \mathcal O_{34}=\mathbf Z+34\mathcal O_K,\qquad
 \operatorname{disc}(\mathcal O_{34})=-3468.
 \tag{41}
$$
完整9级只细化标号，不改变这个 End 环。

令 $H_{-3468}(J)\in\mathbf Z[J]$ 为该整环的环类 $j$ 多项式。
其次数为18；由原 CM 类群的标准精确列也可直接数出：
2、17处的核共有 $3\cdot18=54$ 个，除以
$\mathcal O_K^\times/\{\pm1\}$ 的自由 order3 作用，恰为18。
原54目标的 $j$ 均为这些根，每根按标号保留三次。
不同特征零 CM 环不会有同一个 $j$，故固定整数
$$
 N_{\rm sp}=H_{-3468}(0)\,H_{-3468}(54000)
 \quad\text{严格非零}.
 \tag{42}
$$
除去原坏素数及 $N_{\rm sp}$ 的有限多个素因子后，全部实际目标
及其 Galois 共轭的约化均不在 canonical fiber，也不在
$B[2]\setminus\{O_B\}$。这里没有进行素数扫描，也不需要将可重算的
环类多项式表存进仓库。

所以(24)、(40)不能代替剩余一般有限 CM 纤维的评价。
(38)保留的27对仍是真实需要计算的对象；跨普通 $p$ 的局部非零
门槛未因这些对称关系而删除。


## 8. 真实三挠修正、反 Frobenius 截面的端点及整个最短极除子

本节首先对任意惰性 $q\ge5$ 的实际反 Frobenius 截面给公式，
不假设 Tate。随后仅在 R1014 已证明的**充分大** $q$ 范围内
选用最短生成元。小素数不能因这些必要条件自动获得新截面；
$q=5$ 已由 R1017 的实际点另行支付，三个 $q=11$ 固定极除子
的负回执亦不改变。

### 8.1. 两个分量群的定向，及原 $P_3$ 的位置

继续用 $T,-T$ 标记 $I_9,I_3$。在 $I_9$ 的原节点曲线上取
$$
 u_9=\frac{y}{y+x},\qquad
 x=\frac{u_9}{(1-u_9)^2},\qquad
 y=\frac{u_9^2}{(1-u_9)^3}.
 \tag{43}
$$
由直接微分，$\omega_9=du_9/u_9$。
以趋向 $u_9=0$ 的分支定正的 Tate 分量编号。

为确定原 $P_3=(0,0)$ 到底是分量3还是6，不能只用其 order3。
置 $w=y+(x+t)/2$，则
$$
 w^2=x^3+x^2/4+tx/2+t^2/4.
$$
令 $\beta(t)$ 为右端在 $t=0$ 时等于 $-1/4$ 的单根。隐函数
定理及逐项代入给
$$
 \beta=-1/4+2t+12t^2+O(t^3),\qquad A=\beta+1/4.
$$
右端分解为 $(x-\beta)(x^2+Ax+B)$，其中
$B=-t^2/(4\beta)$。在节点附近选
$\sqrt{x-\beta}$ 的常数项为 $1/2$，并取
$$
 U=\frac{w}{\sqrt{x-\beta}}+x+A/2,\qquad
 V=\frac{w}{\sqrt{x-\beta}}-x-A/2.
$$
则 $UV=B-A^2/4$，其 $t$ 阶为3。
在(43)的 $u_9=0$ 分支上，$U$ 的首项为 $2u_9$，所以它给
上述正编号。在 $P_3$ 上，
$$
 U(P_3)=2t+O(t^2),\qquad V(P_3)=-2t^2+O(t^3).
$$
原基变换使 $\operatorname{ord}_v(t)=3$，于是
$$
 \operatorname{comp}_{I_9}(P_3)=3,\qquad
 \operatorname{comp}_{I_9}(-P_3)=6.
 \tag{44}
$$
这些首项在全部 $q\ge5$ 非零，标签不会在小好特征翻转。

在 $I_3$ 置
$$
 s=x+1/9,\qquad w=y+(x+t)/2,\qquad a_0=\delta/6.
$$
其节点方程为 $w^2=s^2(s-1/12)$，取
$$
 u_3=\frac{w-a_0s}{w+a_0s}.
 \tag{45}
$$
若 $m=w/s$，则 $s=m^2-a_0^2$，从而直接得到
$$
 \omega_3=\frac{ds}{2w}
          =-\delta\,\frac{du_3}{u_3}.
$$
用 $u_3=0$ 分支定 $I_3$ 的正 Tate 编号。原三挠点此时在
恒等分量，且
$$
 u_3(P_3)=\frac{1-\delta}{1+\delta}=\omega^2.
 \tag{46}
$$

原 $F$ 从 $I_9$ 到 $I_3$ 的核落在非恒等分量，故恒等环面
上的次数为1；反向的核是(46)的 $\mu_3$，故环面次数为3。
结合 $F^*\omega=\delta\omega$，或先在同一特征零 Tate 模型中
计算再约化，实际映射准确为
$$
 \begin{array}{c|c|c}
 \text{方向}&\text{恒等环面}&\text{分量群}\\ \hline
 I_9\longrightarrow I_3&u_3=u_9^{-1}&n\mapsto-n\pmod3\\
 I_3\longrightarrow I_9&u_9=u_3^3&a\mapsto3a\pmod9 .
 \end{array}
 \tag{47}
$$
例如第二行对应 Tate 参数 $q_9=q_3^3$，原基参数 $v$ 保持，
所以分量的正号与(44)、(45)一致。这里不只凭正特征微分相等
猜一个可能多出 $q$ 倍的环面同态。

### 8.2. 原三挠修正恰等于 $I_3$ 分量

令 $\sigma$ 为常数域 $q$-Frobenius，取实际截面满足
$$
 \sigma Q=-Q,\qquad
 a=\operatorname{comp}_{I_3}(Q)\in\mathbf Z/3.
 \tag{48}
$$
$I_9$ 是 $\mathbf F_q$ 分裂纤维，故其分量 $n$ 满足
$n=-n$ 于 $\mathbf Z/9$，只能是0。
$\mathcal T$ 只把基参数乘 $\omega$，保持分量编号。
把(15)在 $T$ 处取分量，并用(44)、(47)，得
$$
 3a=0+0+3\epsilon(Q)\pmod9,
 \qquad
 \boxed{\epsilon(Q)=a\quad\text{于 }\mathbf Z/3.}
 \tag{49}
$$
这是原实际 torsion correction 的确定值，不是用有理实现把它删掉。

还需要原三个共轭的准确和。$\mathcal T$ 的固定域是
$\overline{\mathbf F}_q(t)$；原有理 Tate 曲面在这里的纤维是
$I_3,I_1,IV^*$。它是有理曲面，平凡格秩10且判别式绝对值9，
所以 Shioda–Tate 及有理曲面的 unimodular NS 给几何 MW 恰为
$\langle P_3\rangle$。此结论对全部 $q\ge5$ 保留，不用本曲面的
条件 Tate。因而
$Q+\mathcal TQ+\mathcal T^2Q$ 属于该三挠群。
另一方面 $\sigma\mathcal T\sigma^{-1}=\mathcal T^{-1}$，(48)使
这个和反 Frobenius，而 $P_3$ 是 $\mathbf F_q$ 有理的。
故
$$
 \boxed{Q+\mathcal TQ+\mathcal T^2Q=0.}
 \tag{50}
$$

在 $I_3$ 用(45)的 Tate 参数表示 $Q$。若分量用 $a=0,1,2$
代表，则参数有形状 $c\,v^a(1+O(v))$，$c\ne0$。
Tate 模型的系数是 $t$ 的函数，故将 $v$ 换成 $\omega v$
准确描述 $\mathcal T$。因此
$\mathcal TQ-\mathcal T^2Q$ 在恒等环面上的值为 $\omega^{-a}$。
由(50)，
$Q+2\mathcal TQ=\mathcal TQ-\mathcal T^2Q$。
把(15)、(46)、(47)、(49)在 $-T$ 处求值，得到
$$
 u_9(Q(T))^{-1}=\omega^{-a}(\omega^2)^a=\omega^a,
 \qquad
 \boxed{u_9(Q(T))=\omega^{-a}.}
 \tag{51}
$$
当 $a=0$ 时，这是恒等点；当 $a\ne0$ 时，它是明确的非平凡
三挠环面点，不是零截面。

### 8.3. canonical fiber 的四个可能值

将(49)代入第5节已经证明的实际等式，得
$$
 [-2\delta]Q(O_B)=aT
 \quad\text{在 }C_\infty\simeq B.
 \tag{52}
$$
这里沿用(17)–(18)的同一个有理同构，右侧的
$T=(0,0)$，不是另选一个三挠生成元。
R1023 的实际点
$$
 S_3=(-1,\omega^2),\qquad [\delta]S_3=T,\qquad
 \sigma S_3=-S_3
$$
满足 $[-2\delta](aS_3)=aT$。
令
$$
 P_2=(c,-1/2),\qquad c^3=-1/4,\quad c\in\mathbf F_q.
$$
$q\equiv2\pmod3$ 使立方映射在 $\mathbf F_q$ 上为双射，所以
$P_2$ 是唯一非零的 $\mathbf F_q$ 有理二挠点。
因为 $\ker\delta=\langle T\rangle$ 是 Frobenius 固定的，
它与反固定点的交为零。将 $\ker(2\delta)$ 分为互素的
2与3部分，遂得
$$
 \boxed{Q(O_B)=aS_3+eP_2,\qquad e\in\{0,1\}.}
 \tag{53}
$$
特别当 $a=\pm1$ 时，该点永不为零。没有决定未知的 $e$，
也没有由(53)声称其它有限 CM fiber 的值已知。

### 8.4. 充分大惰性 $q$ 的整个最短极除子

现在才使用 R1014 的已付 Tate 范围：取充分大惰性 $q$，令
$Q_q$ 为反 Frobenius 自由直线的最短生成元。
该文给
$$
 \langle Q_q,Q_q\rangle=2q/3.
 \tag{54}
$$
可以并且唯一地调整三挠平移，使
$\sigma Q_q=-Q_q$：若一个自由生成元的
$\sigma Q+Q=\epsilon P_3$，加一个适当的 $kP_3$ 即可，因为2在
$\mathbf Z/3$ 中可逆。高度不变。

由(48)，$I_9$ 分量是0。高度公式于是为
$$
 \frac{2q}{3}
  =2+2(Q_q\cdot\mathcal O)-\frac{a(3-a)}3,
 \qquad a=0,1,2.
$$
左侧非整数，因此 $a\ne0$，并且
$$
 a=\pm1,\qquad
 \boxed{\deg D_q=(q-2)/3,\quad D_q=(Q_q\cdot\mathcal O).}
 \tag{55}
$$
此处 $D_q$ 是**未知的实际交除子**，不是 R1019 中已被
$q=11$ 回执否定的某个同名候选；本节绝不将二者相认。

(51)在 $I_9$ 是非恒等环面点；$I_3$ 分量非零；
(53)在 canonical fiber 非零。因此
$$
 \boxed{\operatorname{Supp}(D_q)\cap\{T,-T,O_B\}=\varnothing.}
 \tag{56}
$$
整个极除子均在有限好纤维，不能再为取得方程解而任添无穷极点。
由 $\sigma Q_q=-Q_q$ 及反演保持零截面，$D_q$ 是
$\mathbf F_q$ 有理的有效除子。

令
$$
 W_q=\frac{2y_q+x_q+t}{\delta},\qquad
 -3W_q^2=4x_q^3+(x_q+t)^2.
 \tag{57}
$$
则 $x_q,W_q\in\mathbf F_q(B)$。在 $D_q$ 的每个点，纤维光滑，
标准零点局部参数使 $x_q,W_q$ 的极阶分别是交重数的2、3倍。
在 $T,-T$ 两处坐标有限，由(56)没有极点。
在 $O_B$，(53)的非零3部分保证 canonical fiber 的 $X$ 坐标
非零，也不是二挠点：若 $X=0$，点在 $\ker\delta$；
若 $2Y+1=0$，点是二挠，均与(52)的非零右侧矛盾。
式(16)遂给恰为2、3的原坐标极阶。故是准确等式
$$
 \boxed{
 \operatorname{div}_\infty(x_q)=2D_q+2O_B,\qquad
 \operatorname{div}_\infty(W_q)=3D_q+3O_B.
 }
 \tag{58}
$$
相应的全 Riemann–Roch 空间维数为
$2\deg D_q+2$ 与 $3\deg D_q+3$。
(55)–(58)约束整个未知极除子；没有将它缩到某个核、某个平移
或某个集中重极点上。

### 8.5. 原共线方程的四个准确端点

对非零的 $Q_q$，(50)使其三个共轭在同一原纤维上共线。
泛型 x 坐标互异：若 $\mathcal TQ=\pm Q$，由
$\mathcal T^3=1$ 及原 torsion 群，只会得到已排的 torsion。
故可写唯一的原共线式
$$
 W_q=M(Y)x_q+N(Y),\qquad M,N\in\mathbf F_q(Y),\qquad Y=-27t.
 \tag{59}
$$
$\mathcal T$ 固定整条线，$\sigma$ 只排列三个共轭，故系数确在
显示的基域；不是任意另选一条 Cardano 线。

把 $a$ 写成 $+1$ 或 $-1$。由(43)、(51)直接计算，
在 $T$ 的实际仿射值是
$$
 x_q(T)=-1/3,\qquad
 W_q(T)=a/9,\qquad
 y_q(T)=\frac{3+a\delta}{18}.
$$
该点是节点三次曲线的光滑 flex，三个共轭的弦线趋于它的切线。
在(57)中固定 $t=0$ 求导，
$-6WM=12x^2+2x$，遂得
$$
 \boxed{M(0)=-a,\qquad N(0)=-2a/9.}
 \tag{60}
$$

在 $-T$，非恒等分量经 Weierstrass 收缩都落在实际节点
$(x,y)=(-1/9,1/27)$，故 $W=0$。
(45)定向的分量 $a=1$ 趋于 $w=(\delta/6)s$ 分支；
分量 $a=-1$ 趋于另一个分支。可直接由 Tate 参数的阶1与2
核定：主项分别来自 $u_3$ 与 $q_3/u_3$，两者的 w 符号相反。
三个共轭处于同一分支，弦线趋于其切线；
由 $W=2w/\delta$，斜率分别为 $+1/3,-1/3$。
因此
$$
 \boxed{M(-1)=a/3,\qquad N(-1)=a/27.}
 \tag{61}
$$
这不是只对端点清分母后的平方方程选任意一个符号。

例如，若沿此前的原规范写 $M=m/H$，$H(0)=-1$，
$m(0)=1$，且两个端点都非极，则(60)固定 $a=1$。
于是实际要求是
$$
 \boxed{m(-1)=H(-1)/3,}
 \tag{62}
$$
不是独立的正负选择。旧三个 $q=11$ 作业完整枚举了两个符号，
所以其无解结论当然保留；本篇不重跑它们，也不据此排除
满足(55)–(62)的真正未知极除子。

这些边界条件是从同一个实际 $F$、原 Tate 编号及完整共线式
推出的。它们为一般构造提供了整个极除子的有限好支撑、准确
次数与端点，但尚未构造一般 $Q_q$，也尚未计算(38)中其余
有限 CM fibers 的原带权值。后继仍须支付该实际求和及其所需
普通局部比较。
