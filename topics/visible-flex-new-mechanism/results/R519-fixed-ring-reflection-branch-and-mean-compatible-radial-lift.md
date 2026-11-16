# R519：固定整圈的反射支、真实一阶径向lift与直接有限候选

2026-11-16。本文只作原源码和数学恒等的纸面推导，没有执行新几何、方向、求积、符号程序、rank、求解器或检查，也没有重开已经结束的 ring17。唯一当前点仍是原实际接受58。

**主结论。** 纯 $R_1$控制若要在整个固定圈逐点保持原 $E,F$，在通常非退化处只有原支和一个明确的反射支。反射支不是任意可选的法向：它必须满足零均值和原角列归属，才能在固定高度的原51族内实现。满足这些条件时，原 $T_u,T_v$给出完整、有限而非一阶近似的lift；沿其共同幅度，原metric门可缩成一个显式标量区间，并能直接生成原盒内有限候选。若反射差非零均值，原 $\Pi$只能实现减去该均值的另一个方向；本文完整保其不同的metric公式和新表示范围。

## 1. 来源、固定量与实际G

本稿接续：

- [R514：完整51控制](R514-complete-fifty-one-ring-controls-and-conditional-seventeen-variable-curvature-fibers.md)；
- [R516：共同一阶17域与原盒分离](R516-common-first-radial-jet-quartic-domain-and-original-box-curvature-separation.md)；
- [R504：完整非线性场与二阶jets](R504-complete-168-parameter-line-second-metric-jets-and-curvature-PSD-remainders.md)；
- [真实接受58收据](../notes/true57-nonlinear168-original-two-grid-accepted58-20261116.md)；
- 原 [frame](../scripts/frame_collar_bvp.py)、[角列](../scripts/frame_collar_enriched.py)、[完整168场](../scripts/frame_complete_body_extension168.py) 和 [原Q列](../scripts/frame_entry_single_q.py)。

固定原径向行 $s=\sigma$，取同一个真实原角圈。记当前

$$
U=X_s,\qquad T=X_\theta/a,\qquad
E=U\cdot U,\quad F=U\cdot T,\quad G=T\cdot T>0,\quad
q=|U\times T|>0 .
\tag{1}
$$

下面的正交反射和metric代数保 $G$，不把实际记录的 $G$静默改成1。连续原frame的规范是
$T=c(v)H+vc(v)e_3$、$c=(1+v^2)^{-1/2}$；该实数函数单位长度以及 $T_u,T_v$的正交关系用于证明真实lift。binary64点积或FFT中的小差别不是新的数学恒等，未来实现必须保其实际值与新求值身份。

第1–10节的纯 $R_1$问题冻结所有高度坐标、$b_*,b_{*,s}$、永久参考、$g,a,a_s,a_{ss}$及已有新增九坐标的背景值。第11节另明确使用一个原允许高度方向，不把它冒作纯 $R_1$。原 $R_1$取末三条样条的完整延拓，满足

$$
R_1(\sigma)=0,\qquad R_1'(\sigma)=1,\qquad R_1''(\sigma)=0.
\tag{2}
$$

不能把它在最后结点片以外截掉。原51族还允许独立 $R_2$最高jet，但它不改变本稿的 $U,T,E,F$。

## 2. 保持整圈原metric迫出的两支

纯 $R_1$改变标量径向导数而不改变本圈的标量值。若其 $U$增量为 $D(\theta)$，则

$$
D=a\Pi(\delta T_s),\qquad
D_\theta=a\,\delta T_s,\qquad T\cdot\delta T_s=0 .
\tag{3}
$$

这里已使用原完整角闭合与同一零均值 $\Pi$，不是将某个离散差分当作原空间导数。

假设候选还逐点保持 $F$。于是 $D\cdot T=0$，对它求导并用(3)，得到

$$
D\cdot T_\theta=0 .
\tag{4}
$$

再假设保持 $E$，则

$$
2U\cdot D+|D|^2=0 .
\tag{5}
$$

令

$$
\mathfrak h=T\times T_\theta .
\tag{6}
$$

在 $\mathfrak h\ne0$处，(4)和 $D\cdot T=0$迫 $D$为 $\mathfrak h$的倍数。式(5)准确给出两个可能：

$$
\boxed{
D=0\quad\hbox{或}\quad
D_{\rm ref}=-\,2\,\frac{U\cdot\mathfrak h}{|\mathfrak h|^2}\,\mathfrak h .
}
\tag{7}
$$

非平凡目标

$$
U_{\rm ref}=U+D_{\rm ref}
$$

是关于 $\operatorname{span}(T,T_\theta)$平面的真实正交反射。它不是在原点近似旋转一个normal，也不是从只保持 $G$推出来的自由度。

式(7)对一般 $G>0$成立，因为该反射固定 $T$和 $T_\theta$。它直接保持

$$
|U_{\rm ref}|^2=E,\quad U_{\rm ref}\cdot T=F,\quad
|U_{\rm ref}\times T|=q .
\tag{8}
$$

若将 $W=U-(F/G)T$及
$k=T_\theta-(T\cdot T_\theta/G)T$写出，同一公式是

$$
U_{\rm ref}=\frac FG T+
 2\frac{W\cdot k}{|k|^2}k-W .
\tag{9}
$$

因此没有漏掉实际 $G$。法向满足
$n_{\rm ref}=-\mathsf H_{\mathfrak h}n$，其中
$\mathsf H_{\mathfrak h}=I-2\mathfrak h\mathfrak h^{\mathsf T}/|\mathfrak h|^2$。
原正交形算子的 $C$变为 $-C$，但混合项 $B$一般不只反号，径向项更不能据此判定。原完整曲率目标仍须用R516的共同门和最高层。

## 3. $T_\theta=0$、两支合并及切支正则性

### 3.1 非退化处的合并

在 $\mathfrak h\ne0$处，两支合并恰在
$U\cdot\mathfrak h=0$。这也正是原 $C=0$。若只逐角看(7)，会误以为可以任意切换原支和反射支；真实角函数的正则性不允许这样省事。

若一个切换点处 $D_{\rm ref}$有有限非零阶 $m$，把一侧取零、另一侧取反射，至多自然接成 $C^{m-1}$，不能未经证明声称更高正则。对原解析角列，任何解析候选若在一个开弧等于原支，就由解析延拓在整连通圈等于原支；若在一个开弧等于反射支，则同理延拓该支。不能把有限节点分支选择当作新的原17角函数。

### 3.2 真退化点

若 $\mathfrak h=0$，式(7)不作除法。在一个完全孤立的点，$E,F$只限制垂直于 $T$的向量在一个圆上，点值分类比两支多；但它仍须与相邻角点的真实场接合，不能单独任意赋值。

当前原角函数由正椭圆相位、原正弦/core/Q列及有限实系数组成，固定径向位置后为实解析周期函数。$T,U$和其完整角原函数亦如此。在此范围内，$\mathfrak h$不是恒零：连续单位 $T$若 $\mathfrak h\equiv0$便恒定，而原闭角圈要求 $\int T\,d\theta=0$，与恒定单位向量矛盾。

故其零点是有限阶、孤立的。在局部坐标 $t=\theta-\theta_0$写

$$
\mathfrak h(t)=t^m\widetilde{\mathfrak h}(t),
\qquad \widetilde{\mathfrak h}(0)\ne0,
$$

则反射式准确化成

$$
D_{\rm ref}(t)
=-2\frac{U(t)\cdot\widetilde{\mathfrak h}(t)}
 {|\widetilde{\mathfrak h}(t)|^2}\widetilde{\mathfrak h}(t).
\tag{10}
$$

因此该解析反射支有明确的局部解析延拓，不是把 $0/0$设成零。符号改变 $t^m$不改变反射。未来数值入口如遇该分支，仍须有真实延拓数据或不退化界；本稿没有在当前58上查找或计数零点。

若离开此解析源，只假设一般 $C^\infty$或低阶正则，可能出现平坦退化或更宽的切支行为，不能照搬上述分类。本文也不排除一个另行定义并付清的较低正则新族。

## 4. 零均值是固定高度下不能省的门

任何真正的纯 $R_1$控制都满足

$$
\frac1{2\pi}\int_0^{2\pi}D\,d\theta=0,
\tag{11}
$$

因为 $D=a\Pi\delta T_s$且中心高度固定。记

$$
\mu=\frac1{2\pi}\int_0^{2\pi}D_{\rm ref}\,d\theta .
\tag{12}
$$

若 $\mu\ne0$，完整反射目标不能由**任何**固定高度的纯 $R_1$角函数lift实现；这不仅是原17列太少。不能将缺少的均值塞进新的center常数，也不能改 $b_*$来冒同一问题。

但是，反射式还给

$$
T\cdot D_{\rm ref}=T_\theta\cdot D_{\rm ref}=0
\quad\Longrightarrow\quad
T\cdot(D_{\rm ref})_\theta=0 .
\tag{13}
$$

因此总能以该导数定义一个不同的、center保持的候选增量

$$
D_{\rm corr}=D_{\rm ref}-\mu .
\tag{14}
$$

注意 $D_{\rm corr}\cdot T$一般不为零；这不妨碍其真实 $R_1$lift，但已经失去反射支逐点保持 $E,F$的结论。两者必须分别命名。

在完全圆平面角曲线、$U=a_sN+b_*e_3$的特例，原反射差是常向量 $-2b_*e_3$，所以(14)恒零。此时没有一个可执行的非零新方向；不能为零函数增加参数。当前58是否有这种退化或 $\mu=0$，本文均未计算。

## 5. 原 $T_u,T_v$给出的完整真实lift

令

$$
W(\theta)=D_{\rm ref}(\theta)-\mu,\qquad
Z(\theta)=\frac{(D_{\rm ref})_\theta}{a}=\frac{W_\theta}{a}.
\tag{15}
$$

由(13)，$Z\perp T$。原frame的偏导满足

$$
T_u\perp T_v,\quad |T_u|^2=c^2,\quad |T_v|^2=c^4,\quad
\operatorname{span}(T_u,T_v)=T^\perp,\qquad c>0 .
$$

所以反解准确为

$$
\boxed{
A_1(\theta)=\frac{Z\cdot T_u}{c^2},\qquad
D_1(\theta)=\frac{Z\cdot T_v}{c^4},\qquad
T_uA_1+T_vD_1=Z .
}
\tag{16}
$$

取原完整 $R_1$，从起点冻结这两个角函数，定义任意有限幅度 $\tau$的完整场

$$
\boxed{
u_\tau(s,\theta)=u_*(s,\theta)+\tau R_1(s)A_1(\theta),\qquad
v_\tau(s,\theta)=v_*(s,\theta)+\tau R_1(s)D_1(\theta).
}
\tag{17}
$$

高度与其原锚均不变。在选定圈，

$$
T_\tau=T,\qquad
(T_\tau)_s=T_s+\tau Z,\qquad
U_\tau=U+\tau a\Pi Z=U+\tau W .
\tag{18}
$$

这是对全部有限 $\tau$的准确恒等，不是 $\tau=0$的JVP。若 $\mu=0$，$\tau=1$给原反射 $U_{\rm ref}$；若 $\mu\ne0$，它给 $U_{\rm ref}-\mu$，绝不能说同一个反射目标。

(16)、(18)的正交反解及均值边界已由另一代理窄纸核，范围不扩大为当前角列成员、原盒或任何实际门通过。

### 5.1 不用数值差分的必要导数

设 $\nu=(U\cdot\mathfrak h)/|\mathfrak h|^2$。在非退化点，

$$
\begin{aligned}
(D_{\rm ref})_\theta&=-2(\nu_\theta\mathfrak h+\nu\mathfrak h_\theta),\\
\mathfrak h_\theta&=T\times T_{\theta\theta},\\
\nu_\theta&=
\frac{(U_\theta\cdot\mathfrak h+U\cdot\mathfrak h_\theta)|\mathfrak h|^2
 -2(U\cdot\mathfrak h)(\mathfrak h\cdot\mathfrak h_\theta)}
 {|\mathfrak h|^4}.
\end{aligned}
\tag{19}
$$

其中 $U_\theta=a_sT+aT_s$，而

$$
\begin{aligned}
T_{\theta\theta}={}&T_u u_{\theta\theta}+T_v\,v_{\theta\theta}\\
&+T_{uu}(1+u_\theta)^2
 +2T_{uv}(1+u_\theta)v_\theta
 +T_{vv}v_\theta^2 .
\end{aligned}
\tag{20}
$$

式(20)中的 $T_v\,v_{\theta\theta}$是乘积，二阶frame偏导仍写 $T_{vv}$。完整相位的1必须保留。

原圈二jets存了 $X_{\theta\theta}=aT_\theta$，不等于已经存了 $T_{\theta\theta}$。后者要从同一当前 scalar 的原二阶角导数实际取得；不靠重算ordinary，也不能冒已付数组。退化点沿(10)求真实导数，不能直接套奇异商或人为截断。

## 6. 何时属于原51族，何时必须声明新角方向

令原角基仍为 $a_1,\ldots,a_9$与 $d_1,\ldots,d_8$。式(17)在原纯 $R_1$17列中，当且仅当存在**与角点无关**的常数

$$
A_1=\sum_{i=1}^9x_i^{\rm ref}a_i,\qquad
D_1=\sum_{j=1}^8x_{9+j}^{\rm ref}d_j
\quad\text{作为完整原角函数恒等成立}.
\tag{21}
$$

此时 $x_1=\tau x^{\rm ref}$，原物理嵌入是
$W_{\cdot1}\tau x^{\rm ref}$，可再加入原共同 $R_2$系数。所有172盒、范数和原字段身份都沿R514/R516处理。

在有限角点拟合成功或很小残差，不等于(21)的完整函数身份。本文没有在58上作成员测试，也没有假设一般非线性反射恰落九个/八个固定角列。

若(21)不成立，(17)仍可作为一个从起点冻结的**新成对角函数方向**来定义数学族，但必须同时声明：

- 原完整背景点和(16)的来源固定；后续不能随候选重新生成 $A_1,D_1$却仍称一个固定列；
- 新field/evaluation/coordinate身份以及该新参数的真实范围和规范；
- 原172盒只约束仍属原172的系数，不能约束一个不在其映射中的新函数幅度；
- 没有新参数约束时，不能称候选已经通过“完整物理盒”；也不能把未修改的168状态对象冒作这个更大族的完整坐标；
- 若 $W=0$，该lift给 $Z=A_1=D_1=0$，根本没有新增方向。

是否采用这个新族，以及新增幅度如何受物理规范约束，是未来独立任务的决定。本稿不把它并入正在使用的原51或原168实例。

## 7. 原角对称、闭合与径向接口

原 $u_*,v_*$及允许角列具有 $\pi$周期、反射奇性；原Q的定义也明确保留这两项。固定新方向必须保这些真实对称，而非仅在网格上强制均值零。

令

$$
P=\operatorname{diag}(-1,-1,1),\qquad
S=\operatorname{diag}(-1,1,-1).
$$

原场满足

$$
\begin{aligned}
T(\theta+\pi)&=PT(\theta),& U(\theta+\pi)&=PU(\theta),\\
T(-\theta)&=ST(\theta),& U(-\theta)&=-SU(\theta).
\end{aligned}
\tag{22}
$$

这里 $U$的高度项也正确，因为 $-Se_3=e_3$。由叉积和导数，

$$
\mathfrak h(\theta+\pi)=P\mathfrak h(\theta),\qquad
\mathfrak h(-\theta)=-S\mathfrak h(\theta).
$$

所以 $D_{\rm ref}$和 $W$具有与 $U$相同的变换律。其均值自动为
$\mu=\mu_3e_3$，但 $\mu_3$并不自动为零。

进一步，$Z(-\theta)=SZ(\theta)$，而
$T_u(-\theta)=-ST_u(\theta)$、$T_v(-\theta)=-ST_v(\theta)$。
结合(16)，得到

$$
A_1(\theta+\pi)=A_1(\theta),\quad A_1(-\theta)=-A_1(\theta),
\qquad
D_1(\theta+\pi)=D_1(\theta),\quad D_1(-\theta)=-D_1(\theta).
\tag{23}
$$

因此对任何有限 $\tau$，(17)仍保原 scalar 的对称。新的 $T_{\tau,xy}$在 $\theta\mapsto\theta+\pi$下反号，$T_{\tau,3}$在反射下反号；完整角平均准确为零，原闭合和同一零均值 $\Pi$合法。不能将此数学对称宣成不同浮点路径逐位相同。

径向使用的是原 $R_1$全区延拓，其支持及接口零jets正是R510/R514已给的原三样条关系。它没有在最后片左端突然截断；在真正原端口保持所需值、一、二jets。固定 $g$、所有高度背景及原锚不变，原样条正则性保留，不扩大成原表示未有的全局 $C^\infty$径向断言。

## 8. 零均值支的直接共同幅度区间

现在额外假设 $\mu=0$且(21)已作为完整函数身份成立。记

$$
d_2(\theta)=|D_{\rm ref}(\theta)|^2 .
$$

由反射恒等 $2U\cdot D_{\rm ref}=-d_2$，式(18)给

$$
\boxed{
F_\tau=F,\qquad
E_\tau=E-\tau(1-\tau)d_2 .
}
\tag{24}
$$

对 $\tau\in[0,1/2]$，令共同变量

$$
s=\tau(1-\tau)\in[0,1/4].
\tag{25}
$$

这不是每个角点各选一个幅度。固定原metric目标 $\varepsilon\in(0,1)$，记

$$
E_{\rm low}=1-\varepsilon+\frac{F^2}{\varepsilon},\qquad
E_{\rm high}=1+\varepsilon-\frac{F^2}{\varepsilon}.
\tag{26}
$$

先保 $|F|\le\varepsilon$。每个 $d_2>0$角点对共同 $s$给准确区间

$$
\frac{E-E_{\rm high}}{d_2}\le s\le
\frac{E-E_{\rm low}}{d_2}.
\tag{27}
$$

若 $d_2=0$，就检查原常数
$E_{\rm low}\le E\le E_{\rm high}$，不能除以零。任一常数行失败即排除这一整条方向。

原物理盒在R516中给共同低阶投影
$x_1\in\prod_jJ_j$。因原58在盒内，沿
$x_1=\tau x^{\rm ref}$的非负可用幅度是包含零的闭区间。与 $[0,1/2]$及任何另行声明的准确物理norm上限相交，记为 $[0,\tau_{\rm box}]$。若 $\tau_{\rm box}=0$，没有正幅候选。

设 $\Theta$为真正声明的有限两网或连续角圈，则全部原metric和盒要求共同化为

$$
\begin{aligned}
s_-&=\max\left\{0,\ \sup_{\theta:d_2>0}
                  \frac{E-E_{\rm high}}{d_2}\right\},\\
s_+&=\min\left\{\tau_{\rm box}(1-\tau_{\rm box}),\
                 \inf_{\theta:d_2>0}
                  \frac{E-E_{\rm low}}{d_2}\right\}.
\end{aligned}
\tag{28}
$$

无正 $d_2$点的上/下确界按无该约束处理，先前的常数行仍保。若 $s_->s_+$或 $s_+<0$，没有该方向上的候选。若非空且含正数，可明确选一个 $s_*\in[s_-,s_+]$并取

$$
\boxed{\tau_*=\frac{1-\sqrt{1-4s_*}}2,\qquad
 x_1=\tau_*x^{\rm ref}.}
\tag{29}
$$

例如取 $s_*=s_+>0$给最大允许的这段幅度；若后续需要严格舍入余量，应从真实有余量的内部选取，不能假设区间必有内点。

这已经给一个直接有限低阶候选，而非一般51变量搜索。每个原角模式再取R516的真实剩余区间
$y_j\in[L_j(x_1),U_j(x_1)]$，如取中点，就得到一个明确的原盒内完整51系数候选。**这个中点只保证盒，不保证目标曲率。** 若要选择满足共同曲率的 $y$，仍须R516原线性纤维的真实新问题；不能把存在盒内 $y$写成曲率已可完成。

式(28)–(29)没有在当前58执行。有限网的最大最小不是连续角圈证书；一个闭式幅度公式也不意味着未来读取/收缩所有角数组是零成本。原 $R_2$的已结束实例没有被重新调用。

## 9. 非零均值时仍有完整、但不同的有限metric模型

若 $\mu\ne0$，真实lift是 $W=D_{\rm ref}-\mu$。其准确metric为

$$
\boxed{
\begin{aligned}
F_\tau&=F-\tau\,T\cdot\mu,\\
E_\tau&=E+2\tau U\cdot W+\tau^2|W|^2 .
\end{aligned}}
\tag{30}
$$

特别在 $\tau=1$，

$$
F_1=F-T\cdot\mu,\qquad
E_1=E-2U_{\rm ref}\cdot\mu+|\mu|^2 .
\tag{31}
$$

不能沿用(24)的等距端点或(28)的单调公共 $s$区间。但是，沿这一个明确方向，R516两条原metric门

$$
\varepsilon(1+\varepsilon-E_\tau)-F_\tau^2\ge0,\qquad
\varepsilon(E_\tau-1+\varepsilon)-F_\tau^2\ge0
\tag{32}
$$

仍是显式的单变量二次不等式；给定有限角网和真正声明的幅度域，可按各二次式的完整符号区间求交，不需要把它改造成任意51维优化。所有退化二次、线性、常数行和空域都须保留。

(32)只产生同圈metric资格；R516四次列门沿同一方向仍为有限四次式，最高层与全body门继续独立。当前没有授予任何幅度、查询次数或实际验收。

## 10. 全body变化与有限幅度的真实范围

即使在(24)的分支，整圈以外也不是metric中性。用固定 $A_1,D_1$和真实 $R_1(s)$，

$$
\begin{aligned}
\Delta u&=\tau R_1A_1,&
\Delta u_s&=\tau R_1'A_1,&
\Delta u_{ss}&=\tau R_1''A_1,&
\Delta u_\theta&=\tau R_1 A_{1,\theta},\\
\Delta v&=\tau R_1D_1,&
\Delta v_s&=\tau R_1'D_1,&
\Delta v_{ss}&=\tau R_1''D_1,&
\Delta v_\theta&=\tau R_1 D_{1,\theta}.
\end{aligned}
\tag{33}
$$

对全部body必须把它们直接代入

$$
\psi_\tau=\theta+u_\tau,\quad
c_\tau=(1+v_\tau^2)^{-1/2},\quad
T_\tau=c_\tau H(\psi_\tau)+v_\tau c_\tau e_3,
$$

再沿原完整链式取得 $T_{\tau,s},T_{\tau,ss},T_{\tau,\theta}$。相对位置和二jets准确为

$$
\begin{aligned}
X_\tau-X_*&=a\Pi(T_\tau-T_*),\\
U_\tau-U_*&=a_s\Pi\Delta T+a\Pi\Delta T_s,\\
X_{\tau,ss}-X_{*,ss}
 &=a_{ss}\Pi\Delta T+2a_s\Pi\Delta T_s+a\Pi\Delta T_{ss},\\
X_{\tau,s\theta}-X_{*,s\theta}&=a_s\Delta T+a\Delta T_s,\\
X_{\tau,\theta\theta}-X_{*,\theta\theta}&=a\Delta T_\theta .
\end{aligned}
\tag{34}
$$

这保全部角原函数、真实 $c(v)$和径向/角向导数，没有把 $(U,T)$的同圈线性式外推到中段。高度函数不变，并不意味着 $X_3$在中段不变。

在选定圈，$T_{ss}$的完整改变量仍有

$$
\begin{aligned}
\Delta T_{ss}={}&
2\tau\big[(T_{uu}u_s+T_{uv}v_s)A_1
 +(T_{uv}u_s+T_{vv}v_s)D_1\big]\\
&+\tau^2\big[T_{uu}A_1^2+2T_{uv}A_1D_1+T_{vv}D_1^2\big],
\end{aligned}
\tag{35}
$$

加上真正选择的 $R_2$项。R516的有限二次表因此直接适用，不能只以反射 $U$或相同 $E,F$宣布曲率目标达到。

整个真实候选还需原两网14门、strict eta下降、原盒与声明的新参数约束。前102列与末三样条的中段耦合不被本稿删除；任何新增角函数族更不能绕过这些门。

## 11. 原允许γ高度列可有条件补均值，但这是另一个真实族

本节解除纯 $R_1$对当前高度坐标的冻结，仍保持同一个原 $g,b_0$ reference和原允许的完整场。由第7节，反射差均值确只有

$$
\mu=\mu_3e_3 .
$$

现有新增高度列的原源码为

$$
L=\frac{81}{100},\qquad
x=\frac{s-9/250}{L},\qquad
P_8(x)=x^8e^{-x/(1-x)}\quad(0<x<1),
$$

$$
\delta z=L\,\delta\gamma P_8(x),\qquad
\delta b=\delta\gamma P_8'(x),\qquad
\delta b_s=\frac{\delta\gamma}{L}P_8''(x),
\tag{36}
$$

沿原定义在区间外延为零。这里改变的是原已允许的 $\gamma$系数，不是改 immutable $b_0$。

原完整末片 $\sigma\in(153/200,423/500)$对应
$x_\sigma\in(9/10,1)$，而

$$
P_8'(x)=x^7e^{-x/(1-x)}
 \left(8-\frac{x}{(1-x)^2}\right)<0\qquad(9/10<x<1).
\tag{37}
$$

所以该列在本文的每个真实末片圈上都非零。这是原显式函数的纸面事实，不依赖采样max或新的rank观察。若数学上取 $\sigma=39/50$，则 $x_\sigma=124/135$，括号为 $-15772/121$；实际binary64行仍按自身真实 $x_\sigma$用(37)，不偷换成该有理标签。

因此可明确取

$$
\delta\gamma_{\rm ref}=\frac{\mu_3}{P_8'(x_\sigma)} .
\tag{38}
$$

将(17)的角lift与幅度 $\tau\delta\gamma_{\rm ref}$同时应用，得到

$$
U_\tau=U+\tau(D_{\rm ref}-\mu)+\tau\mu=U+\tau D_{\rm ref}
\quad\text{在选定圈}.
\tag{39}
$$

于是即使 $\mu\ne0$，联合族也准确恢复(24)的共同metric公式。第8节的幅度区间可沿用，但物理盒必须同时纳入这条原γ坐标的范围。

这不是免费补一个常数。环上的位置和径向二jet同时增加

$$
\Delta X_3=\tau L\delta\gamma_{\rm ref}P_8(x_\sigma),\qquad
\Delta X_{ss,3}
=\frac{\tau\delta\gamma_{\rm ref}}L P_8''(x_\sigma).
\tag{40}
$$

所以ring高度、ball/strip、mirror以及形算子第一个对角元都必须保真实变化；不能从(39)宣称原14门保持。其全body变化仍是原完整(36)，两真实端口的零原函数与所需零jets照原 $P_8$保持，并未改变原高度锚。

原γ物理盒为既有的 $[-1/4,1/4]$。若当前系数为 $\gamma_*$，幅度须满足

$$
-\frac14\le\gamma_*+\tau\delta\gamma_{\rm ref}\le\frac14.
\tag{41}
$$

$\delta\gamma_{\rm ref}$可能很大，特别在接近真正右端时(37)趋零；非零列本身不授盒内可行。将(41)与第8节的 $\tau_{\rm box}$相交，零方向与零宽情况按原常数行处理。若任务另有限制物理norm，必须对包含此γ增量的完整172向量计算。只有(21)也是完整成员身份时，角方向和这一高度列才全部属于原172映射。

若采用两网L2投影而非准确(21)，则同一原17列的 $V_j$在每网真零均值。因此在各网均匀角权下，投影 $D_{\rm ref}$与投影 $D_{\rm ref}-\mu$给同一角系数；未补height时均值只能留在残差中。投影后一般不再保持 $F$或(24)，必须回到R516的完整二次metric和四次列门。若同时加高度，也只允许一个共同物理系数，不能给粗细网各补不同高度。

这个投影可以产生一个明确的新原17射线，但残差不能冒准确lift；可能得到零射线或仅 $\tau=0$可用，此时没有理由再次调用原 $R_2$实例。本文不实现或执行这个新LS，也不决定其预算。

## 12. 输入、数值身份和未支付事项

反射公式使用完整当前 $U,T,T_\theta$，全部是同一当前点、同一原角网/连续场的量。原 ring17成功记录保存了对应圈的一、二jets，可按其身份直接消费，但本稿没有读取大原输出或计算反射差。

式(19)另需要真正 $T_{\theta\theta}$或等价的原 scalar 二阶角导数；未保存部分仍是未来新模型的必要工作。完整零均值、解析角列成员、退化点延拓、原盒区间和共同metric区间也均未在58上数值支付。不同目标不能通过重命名已经结束的ring17账户获得新调用。

若原角列成员只有近似拟合，则产生的是另一个原17系数方向，其metric应直接用R516完整有限式，不能沿用反射等式。若采用新的冻结角函数，必须建立独立数学/浮点评估身份和新参数范围，不把旧哈希冒其绑定。

实际生成168候选时，各个系数独立舍入可能破坏准确的 $R_1$零值/二阶jet关系；原51路径需要保未舍入嵌入、实际168/172、舍入差及真实物理norm/盒。新角函数族则必须保其完整新坐标和对应函数定义。任何预测通过只产生候选，最后仍按真正实际字段的原普通路径验收。

## 13. 本稿得到的具体前进点

本稿给出了一个明确几何目标，而非任意低阶参数：

1. 原metric精确保留迫出完整的反射支(7)，含退化、合并和切支边界；
2. 零均值是固定height下的真实可实现性门，非零时只能取另一个准确的center保持方向(14)；
3. 原正交frame给完整lift(16)–(18)，并证明新角函数的原对称、闭合和径向接口；
4. 若lift落原9/8列，原盒与metric可缩成共同一维区间(28)，直接给有限候选(29)，但共同曲率最高层和全部body仍须真实解决；
5. 不落原列时，只有明示的新冻结角方向可继续，原172盒不能移用到新坐标；
6. 原γ列在末片圈处严格非零，可以有条件补反射均值，但必须同时保其原盒、真实位置/二jet变化和全部实际门。

当前58是否满足零均值、原列成员或后续曲率/实际门，本文没有宣称已经成立。它把下一实际尝试缩到一个确定的几何方向与明确可审的分支，不把数值状态、未存输入或同圈恒等升级成全局几何结论。
