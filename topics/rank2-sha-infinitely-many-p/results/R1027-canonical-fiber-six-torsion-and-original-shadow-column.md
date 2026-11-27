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
