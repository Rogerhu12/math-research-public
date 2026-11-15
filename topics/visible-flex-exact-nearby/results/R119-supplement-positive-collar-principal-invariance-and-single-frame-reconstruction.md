# R119/R133 续篇：正 collar 的 principal 不变性与完整 Cauchy 数据的单一 frame 重建

2026-11-15，visible-exact / tail_connector。

**准确几何接口，全文及真实 coframe/连接/残差号已独立核对。** 本篇将两个不同事实分开证明。
第一，B 端正型 collar 内的改动不改变任何真实 principal return，
因此在固定第二参数后保同一第一参数值图。第二，若最后的真实
Darboux residual已经为0，则完整 Cauchy高度数据在 B 的匹配给出
一个可以连续重建的共同 Euclidean frame。全过程保两 mean、
holonomy、唯一高度常数以及真实角连接。

非zero residual的 graph种子只有准确 Cauchy数据，不因这些数据
已经匹配就获得等距 immersion。也不将以下唯一重建当作对未知
帽内曲率、ν 或另外给定的 height/flux条件的 Schur反演。

## 1. Principal 值图只读取真实负分量

采用已发布的
[L：低范数第一参数图](R119-supplement-low-norm-principal-Gamma-map-and-tame-high-conjugacy.md)
及[新 B collar 种子](R119-supplement-new-94-B-collar-lift-and-actual-graph-seed.md) G。
冻结同一个 $\gamma_2^\flat$、五盒 profile、fixed stop和实际物理
$t,\theta$。对每个允许第一参数 $p$，记其径向 profile为 $w_p$。

L.10 的真实返回是
$$
 (F_\pm)_t=-d(t,F_\pm)\mp\sqrt{Q(t)}\,v(t,F_\pm),
 \qquad {\cal R}_i=F_-^{-1}\circ F_+ .
 \tag{T.1}
$$
它的两条有序路径只位于相应真实负分量 $Q>0$，连同两端原根。
外行 $i=(129,2)$ 使用其新 simple-root 分量，没有替换成自由旋转。
$P,K,U,V$ 及 $w_p$ 的完整 mean都参与 $d,v$，不是只读取非mean近似。

G 的改动支持在
$$
 0\le v_B=-t\le d_B=2^{-1024},\qquad
 Q=S(v_B/2^{-24})-1<-3/4 .
 \tag{T.2}
$$
所有允许 $p$ 的径向控制支持都与此 collar分离。
给定两个非mean高度 $u,\widetilde u$，若它们之差支持在这个 collar，
则对每个允许 $p$，两者在 (T.1) 的整个路径、根和邻域逐点相同。
各自以同一个 $w_p$ 解真实 holonomy小根后，完整 mean亦逐点相同。
因此准确有
$$
 f_i(p,\widetilde u)=f_i(p,u),\quad
 {\mathfrak T}_i(p,\widetilde u)
                     ={\mathfrak T}_i(p,u)\qquad\hbox{全部 }i,p .
 \tag{T.3}
$$
由 L.14--L.15 的同一低球上的唯一固定点，
$$
                     \gamma_1^*(\widetilde u)=\gamma_1^*(u).
 \tag{T.4}
$$
这是整个非线性值图相同，不只是沿某一个方向导数为0。
不需要在更高角 norm中重新选参，也不把第二参数值图扩到
一般有荷方向。第二参数始终是冻结的原实际数。

## 2. 准确高度、metric 和两个正分母

现在独立考虑一个真实连通 annular部分，使用物理半径 $a>0$。
原目标度量是
$$
            g=(1+w(a)^2)\,da^2+a^2d\theta^2 .
 \tag{T.5}
$$
令 $z$ 是 Darboux正高度，满足
$$
 z_a=w(1+K),\qquad z_\theta=awP,\qquad
 U=P_\theta,\quad V=K_\theta .
 \tag{T.6}
$$
$\langle P\rangle=0$ 源于同一个周期高度；
$K=K_\perp+\kappa$ 包含原真正 holonomy mean。
取 $t=\log a$，$q=w^2$、$A=(\log w)_t$、$Q=-A$，
运动学准确给
$$
                        P_t=V+(Q-1)P .
 \tag{T.7}
$$
全文保
$$
 B=1-qP^2>0,\qquad
 D=1-q\{2K+K^2+(1+q)P^2\}>0,\qquad
 J=1+K+(1+q)U>0 .
 \tag{T.8}
$$
这些是已付真实分支条件，不是 $Q$ 的符号条件；
所以根处 $Q=0$ 不造成这里的除零。

考虑 horizontal metric $g_h=g-dz\otimes dz$。
准确矩阵及其 determinant是
$$
 g_h=
 \begin{pmatrix}
 1-q(2K+K^2)&-a q(1+K)P\\
 -a q(1+K)P&a^2B
 \end{pmatrix},\qquad
                  \det g_h=a^2D .
 \tag{T.9}
$$
因此 (T.8) 保 $g_h$ 正定。
全部 mean 已在 $K,P$ 中；不以平均 metric代替 (T.9)。

## 3. 一个明确的 coframe 与真实角连接

选取原径向正定向的 orthonormal coframe
$$
 \omega_1=\frac{\sqrt D}{\sqrt B}\,da,\qquad
 \omega_2=-\frac{q(1+K)P}{\sqrt B}\,da
                         +a\sqrt B\,d\theta .
 \tag{T.10}
$$
有 $g_h=\omega_1^2+\omega_2^2$，
$\omega_1\wedge\omega_2=a\sqrt D\,da\wedge d\theta$。
定义唯一实连接一形式 $\Omega$，使
$$
 d\omega_1=\Omega\wedge\omega_2,\qquad
 d\omega_2=-\Omega\wedge\omega_1 .
 \tag{T.11}
$$
在径向参考上 $\Omega=d\theta$，与原 coframe方向一致。

写
$f=\sqrt D/\sqrt B$、
$g_1=-q(1+K)P/\sqrt B$、
$h=a\sqrt B$。
从 (T.11) 逐项得到
$$
 \Omega_\theta=\frac{h_a-(g_1)_\theta}{f},\qquad
 \Omega_a=\frac{-f_\theta+\Omega_\theta g_1}{h}.
 \tag{T.12}
$$
利用 (T.7)，其中第一式准确化为
$$
 \boxed{\quad
 \Omega_\theta=
 \frac{1+q(1+K)U/B}{\sqrt D}
                     =:{\cal H}_q(P,K,U).
 \quad}                                                   \tag{T.13}
$$
例如 $B_t=2q(P^2-PV)$，故 $B+B_t/2+qPV=1$；
余下两个 $U$ 项以 $B+qP^2=1$ 合成 (T.13)。
这一步没有使用 $K_t=F$。

(T.12) 的 $\Omega_a$ 只读取同一 slice的
$P,K,U,V$、径向 $a,w$ 和角导；它不靠把径向角常数重新设0定义。
全部径向 phase就是这个一形式的径向积分。
更具体地，利用 $D+q(1+K)^2=(1+q)B$ 消去所有剩余的 $PU$ 项，
第二式准确给
$$
 \Omega_t=a\Omega_a
       =\frac{q(1+K)(V-P)}{B\sqrt D}.
 \tag{T.12a}
$$
此式直接保留真实径向角连接，并显式表明其中没有 $K_t$。

## 4. Residual、flatness 和准确 holonomy

采用原完整商式
$$
 F=\frac{Q(2K+U+K^2+KU+qP^2)+(1+q)(V-P)^2}
                       {1+K+(1+q)U},\qquad
 \mathfrak r=K_t-F .
 \tag{T.14}
$$
直接微分 (T.12)，只用 (T.7)、$q_t=2Aq$ 及
$U=P_\theta,V=K_\theta$，得到
$$
 \boxed{\quad
 d\Omega=q\,JD^{-3/2}\mathfrak r\,dt\wedge d\theta .
 \quad}                                                   \tag{T.15}
$$
其 $\mathfrak r$ 系数也可直接核：
$\partial_K{\cal H}_q=qJD^{-3/2}$，而 $\Omega_t=a\Omega_a$
不含 $K_t$；把 $K_t$ 换为完整 (T.14) 后其余项全部消去。
这是 M.16 的未取 mean版本；取圆周平均便恢复
$\partial_t\langle{\cal H}_q\rangle=q\langle JD^{-3/2}\mathfrak r\rangle$。

真实 holonomy小根始终是
$$
                         \langle{\cal H}_q\rangle=1 .
 \tag{T.16}
$$
若 $\mathfrak r=0$，则 $d\Omega=0$。
若只有 (T.16) 而 $\mathfrak r$ 非zero，
只能得到其 weighted mean兼容，不得从中推 $d\Omega=0$。
所以 G 的 off-shell种子不能在这一步被称为已经重建成等距面。

## 5. 同一个 frame、一个位置和全部周期

现在假设真实 Darboux方程成立，因而 $d\Omega=0$。
在 universal cover上从一个固定点积分
$$
              d\alpha=\Omega,\qquad
              dX=e^{i\alpha}(\omega_1+i\omega_2).
 \tag{T.17}
$$
(T.11) 使第二式闭合：
$d(\omega_1+i\omega_2)=-i\Omega\wedge(\omega_1+i\omega_2)$。
因此 (T.17) 给真正的 $X:\widetilde I\times\mathbb R\to\mathbb C$。
只选择一次初始角 $\alpha_0$ 和一次初始水平位置 $X_0$。

由 (T.16)，$\alpha(a,\theta+2\pi)-\alpha(a,\theta)=2\pi$。
四重周期使更准确的 quarter差为 $\pi/2$。
(T.10) 的系数也为四重周期，因此
$$
                  X(a,\theta+\pi/2)=iX(a,\theta)+b_0
 \tag{T.18}
$$
中 $b_0$ 是整个连通区域的同一个常数：
微分左边减右边在 $a,\theta$ 两个方向都为0。
迭代四次，$1+i+i^2+i^3=0$ 给真正的水平位置周期。
没有每层独立的平移 period，也没有按半径改动旋转中心。

对正高度取空间浸入 $(\Re X,\Im X,z)$，
对北帽的实际约定取 $(\Re X,\Im X,Z_0-z)$。
由 (T.9)--(T.10) 其第一基本形式准确为 $g$。
$g_h$ 正定保证 immersion；整个证明不除以 $Q$。
初始 $X_0,\alpha_0$ 只改变一个共同的平面刚体动作，
不是每片一个新 unknown。

## 6. B 接口的准确 frame 接续

设 B 两侧都已是真实解，目标 metric、$a,w$ 的所需 jets相同，
且使用同一个物理角。若
$$
                  z_-(B,\theta)=z_+(B,\theta),\qquad
                  (z_a)_-(B,\theta)=(z_a)_+(B,\theta)
 \tag{T.19}
$$
包含完整 mean成立，则 $P,K,U,V$ 在 B相同。
(T.10)、(T.12)--(T.13) 的 coframe及连接在 B也相同。
将尾侧的唯一初始 frame/位置取为已经确定的 cap--long侧
在一个固定角上的真实值，(T.17) 沿整个 B圆的 ODE唯一性便使
完整 B曲线、两向切向量与 frame全部相同。

这是将尚待重建的一侧安装到同一个已经给定的 frame；
不是把两个已经各自规定的物理端 frame分别重新归零。
若两个端 frame都被外问题独立指定，它们仍需比较 (T.17) 的
实际 ordered输出，并保作真实 matching行。

最后由 (T.14) 和 $J>0$，同一个 Cauchy pair确定 B的
$K_t$，所以两侧所需二阶高度迹相同；
flat coframe的对应 derivatives亦匹配。
原单侧目标/profile正则只授原来的全局阶数，
更高 derivatives仍按已经记录的 broken jets保留。

## 7. 一个高度规范与未删除的 mean跨度

(T.6) 的 mean是
$$
                 \langle z\rangle_t=aw(1+\kappa).
 \tag{T.20}
$$
所以相同 $\kappa(B)$ 只匹配 mean slope，
还必须用一次真实积分对齐 mean高度：
$$
 \langle z(t)\rangle
  =\lambda+\int_{t_f}^t a(s)w(s)(1+\kappa(s))\,ds .
 \tag{T.21}
$$
G.22--G.24 正是对其修补后的真实费用；
long 的独立 mean-height跨度不乘 $\varepsilon_L$。
一个整体 $\lambda$ 可规范一个真实端的高度；
其余端值都是 (T.21) 的实际输出。

坐标 primitive 的 mean规范、Euclidean frame角 $\alpha$、
principal Γ反项以及空间位置常数是不同对象。
(T.17) 保留完整 $\Omega_a$；不会因为 moving坐标
$\langle\Theta-\mathrm{id}\rangle=0$ 而删除这个真实径向角积分。
物理 $B_0,C_0$ 亦没有由四重周期或 (T.16) 自动置零。
在实际共同反射子类中 $B_0=0$ 是原独立反射定理的结论，
而不是本篇作 frame接续的前提。

## 8. 对当前 fixed-Γ2/Nash 工作线的准确权限

G 构造的种子保同一 $\gamma_1^*$ 与冻结 $\gamma_2^\flat$，
因为 (T.3) 是所有候选 $p$ 上的准确恒等式。
后继 Nash校正一般作用于负分量，须按 E/L 重选同一第一参数值图；
本篇不使该重选消失，也不重授第二参数的值图。

如果后继 augmented迭代真正解出 body residual和 actual
cap--long返回，使 (T.19) 包含全 mean成立，则 (T.17)--(T.21)
给同一个连续且周期的几何重建，没有额外任意的逐层 phase/reset。
所有已有平盘 $C^2$ 极限按原真实物理 jet界接回；不从一个
finite-Sobolev norm独自推新的全层几何极限。

尚未解的帽内完整 $B(L),C_0(L)$ 和设计ν仍须由实际匹配确定。
任何另外给定的独立 flux荷、两端height或frame数据也不由本定理删除。
本篇给 (T.19) 一旦成立时的准确、无新规范自由度的frame接续。
对当前只求存在的自由安放路线，第9节明确哪些位置/高度是输出，
不虚设两个已经独立规定的世界锚。

本篇也不把固定第二参数、沿 $\gamma_1^*(u)$ 的设计迭代，
称为整个族保持同一个 metric。
原[C.6--7](R133-supplement-complete-C0-state-and-nu-geometry-response.md)
给 $E_\nu=E\exp(\nu w)$，所以 $\nu$ 也是 intrinsic 设计参数。
最终须同时冻结 $\nu^*,\Gamma_1^*,\Gamma_2^*$ 和其它 metric 数据。
准确的后继见[P真实相位与固定marker](R133-supplement-frozen-metric-extrinsic-phase-and-fixed-marker-family.md)：
一张完整精确径向metric面 $G$、两真平盘上的同一材料作用
$G\circ S_\tau=R_\tau G$ 及原全域几何门一旦成立，
$R_\tau G S_{-\tau}$ 加同一四块真实静态曲率patch即给最终共同metric族。
两盘可以有不同但固定的相位offset。
未标记相位的像本来全等；真正非全等来自静态曲率峰与独立腰部见证。
因此不另要求一个变动 $\nu$ 或冻结设计参数后重新求解整族的IFT。
当前尚须完成单个 $G$ 的augmented匹配、平盘准确身份和原全域几何门；
现有 E/L/B body收敛与本frame接续不单独授这些条件。

## 9. 当前单半面路线：位置是同一次重建的输出

这里直接消费已经证明的
[M：完整物理两迹与腰反射](R133-supplement-full-physical-trace-matching-and-waist-reflection.md)，
正文blob `89a82cfabf212c0345f185b17632f337c37d5016`，
SHA256 `6ead36a196328fa51c4cde447ef59777b8621d505c3f233503efb6ffab0408e5`。
M.3--M.11已经包含所有位置/标架周期和二阶接缝的证明。
以下将它准确用于当前一个上半面及其镜像；不重算旧数值，
也不改变一般prescribed端源定理的权限。

**当前需要真正解出的上半面数据。**
先求同一个tail的完整Darboux方程、holonomy-one及真平盘极限；
其在B的非mean高度是实际$f_B$。再以同一个固定内帽输入$\gamma$
调用M32帽与long图，要求真实far条件
$$
 P_\perp K_T(B)=P_\perp\mathscr K_\gamma(f_B).
 \tag{T.22}
$$
这里采用O的normalized完整slope记号，固定metric比例与真实$t$
方向不变。两侧相同$f_B$给相同$P,U$；
(T.22)给相同非mean $K,V$，而同一holonomy小根的唯一性给相同$\kappa$。
因此完整slope及由四态给出的两条曲率mean均匹配，不是只核一条截断行。
平均高度的值尚须按下面的同一次积分初值对齐。

把long平均高度的积分初值选为tail在**同一个B截面**的实际值，
即可令(T.19)的完整高度成立。这个操作是把两份积分表示的常数接成
一个共同的物理高度，不增加第二个独立高度自由度。
之后所有mean高度仍是(T.21)的同一次有向积分输出。
两侧若使用北帽实际高度$Z_0-z$，须同时遵守M.13--M.14的符号，
不能把正高度与北帽高度混接。

实际帽在$r=R$的全部物理$B,C$本来由它的真实long图给出；
其解仍在同一修补中心、同一metric和物理角中。
内core尚须解出的准确曲率条件是
$$
 \begin{aligned}
 P_\perp C_{\rm core}(L)
     &=P_\perp\widehat C(L)+\gamma,\\
 B_{\rm core}(L)&=B_{\rm cap}(\gamma,f_B;L),\\
 \Pi_0 C_{\rm core}(L)&=\Pi_0 C_{\rm cap}(\gamma,f_B;L).
 \end{aligned}
 \tag{T.23}
$$
这些是完整函数/mean等式；并非只有97个输入或输出。
反射子类中的$B_0=0$须来自已经证明的方程对称性，
一般全周期源问题仍保其独立Bmean行。
核心的PDE、腰$u(0)=0$、物理振幅和设计$\nu$行继续保留。
(T.22)--(T.23)目前不是被假设已解的数值结果。

**完整曲率匹配之后没有另一条函数位置条件。**
$C\ne0$使Gauss公式确定$A=(K_g+B^2)/C$，所以(T.23)
也匹配整个第二形式。在同一metric jet下，从实际cap的
一个位置/Euclidean frame向内使用M.4的真实径向ODE。
M.6--M.7的平坦连接缺陷方程证明整个二维重建一致，
并继承cap的全部位置和frame周期。
M.8又给接缝全部二阶导数相同。
因此core的世界位置、其内端mean高度与frame已经由同一次重建确定。

若core此前只是用任意初始frame积分过，则只作一个整体
Euclidean刚体对齐；共同边界角ODE唯一性使全圈随之匹配。
这不是逐角或逐片重置位置。当前存在性任务没有另给两份
独立世界坐标数据，故不增加“把另一个任意锚调回原值”的Schur行。
若实际另行规定了端位置/flux/height，则原A.21--A.24和B.29
仍要求解它们；本节没有给这些一般数据一个免费逆。

**腰反射只复制已构造的同一个半面。**
当前metric在腰满足原准确$a'(0)=E'(0)=0$；
它来自原腰反射，紧支$\nu$ bump在腰邻域为0。
这只复用metric恒等式，不转授R124旧对象的数值修正范数。
腰$u=0$及$v\ne0$给完整物理$B=0$。
M.9--M.11遂给一个固定腰平面$\Pi$，并定义
$$
 G_-(r,\theta)=\mathcal R_\Pi G_+(-r,\theta).
 \tag{T.24}
$$
一阶径向的两个负号抵消；二阶径向、混合、角向迹分别满足偶、奇、偶条件。
若上半面已在真正平盘端闭成材料圆盘，(T.24)便是连通闭$C^2$浸入。
下半面没有第二组独立cap参数、height或frame方程。
这一步仍不自动给嵌入或reach，后者必须消费同一个全闭面的原全域门。

M.12还说明，腰mean的整数转角分支只在真实周期继承后确定。
在原moving图中$\langle C\rangle_{\rm physical}=1/m$，
故$a_0/m$为负整数。只要已核的真实邻域选择
$|a_0/m+1|<1/2$，便准确有$m=-a_0$。
不能在解(T.23)之前用这一几何后果删除外端Cmean方程。

**未screen的跨度仍须实际估计。**
规范一次腰平面后，上平盘高度$h_+$是完整有向积分的真实输出；
镜像下盘高度为$h_-=-h_+$。
原R112的regular常模也正是允许
$\lambda_-=-\lambda_+$，并非分别把它们设为0。
对设计参数的变化，跨端
$H_p(t_R)-H_p(t_L)$和long的$aw(L)/165$依然进入这个输出，
不得乘screening因子或由一global $\lambda$抵消两个端值。

当前所需的是这些输出满足原G.17的高度区间、同轴真盘身份，
并在同一世界规范中满足G.24的全域位置/法向/曲率界。
C0几何比较中的实际锚误差$b_F,b_Q$也仍须包含此次输出变化。
它们是必须支付的几何预算；在本节自由安放构造中，
不是另外指定的函数位置方程。

所以当前最小闭合路线是：真tail与(T.22)、完整帽/core的(T.23)、
腰/设计参数条件、真平盘正则与同一全域几何门。
先得到这一张完整$G$，再冻结全部intrinsic数据并用P的固定marker相位族。
一般独立source/charge/height接口原样保留；
当前尚未解出的上述真实方程也没有被本节设成零。


## 10. 本次 exact tail 的真实物理 jets、平面圆周及整盘延拓

本节消费新
[S：nonlinear far straightening与完整graph Nash](R119-supplement-nonlinear-far-boundary-straightening-and-complete-graph-Nash.md)
S.38--S.41，补上第8--9节以前单独保留的平端重建接口。
只对其中已经取得完整零 Darboux residual、holonomy-one和真实内部traces的解使用；
并非对任意有限角Sobolev场使用。固定该解最终选定的全部intrinsic数据。

**实际径向坐标不混用。**
深层安装坐标为 $1\le r\le2$，物理半径为 $a=\rho r$，$\rho>0$ 固定。
设累积平端为 $a_f=\rho r_f>0$。S.40--S.41已经分别保完整非mean与mean，
并准确支付
$$
 z\longrightarrow z_f,\qquad
 z_a,\ z_\theta,\ z_{aa},\ z_{a\theta},\ z_{\theta\theta}
       \longrightarrow0
 \quad\hbox{一致于真实圆周}.                         \tag{T.25}
$$
这里 $z_a=\rho^{-1}z_r$、$z_{aa}=\rho^{-2}z_{rr}$、
$z_{a\theta}=\rho^{-1}z_{r\theta}$；不以安装尺度的导数代替物理导数。
非mean与mean的净深幂分别为 $124-5/256$、$251-10/256$。
原controlled profile C.7同时给
$$
 w\longrightarrow0,\qquad
 w_a=\rho^{-1}w_r\longrightarrow0,\qquad
 w_{aa}=\rho^{-2}w_{rr}\longrightarrow0 .                \tag{T.26}
$$
其径向幂分别为 $7/2,2,1/2$，固定 $\rho$ 与真实前缀系数不删除。
有限接缝的二jet已经由S的真实方程与traces相容。
因此(T.25)--(T.26)是全层趋近平端的界，不是只沿一列切口的界。

在实际 $(a,\theta)$ 坐标，
$$
 g_h=(1+w^2-z_a^2)\,da^2
             -2z_a z_\theta\,da\,d\theta
             +(a^2-z_\theta^2)\,d\theta^2 .
 \tag{T.27}
$$
由(T.25)--(T.26)，其系数及一阶导数一致趋向
$da^2+a^2d\theta^2$ 的相应值。这里真正使用的是 $C^1$ metric极限，
不是仅有正定性。因为 $a_f>0$ 且 $B,D$ 保原正下界，
(T.10)的代数平方根和平滑商保持该 $C^1$ 极限。
沿用(T.12)的 $f,g_1,h$，准确得到
$$
 \begin{gathered}
 f\to1,\quad g_1\to0,\quad h\to a_f,\\
 f_a,f_\theta,(g_1)_a,(g_1)_\theta,h_\theta\to0,
 \qquad h_a\to1 .
 \end{gathered}                                         \tag{T.28}
$$
所以同一个真实连接满足
$$
                        \Omega_a\to0,\qquad
                        \Omega_\theta\to1 .             \tag{T.29}
$$
(T.12a)也直接给第一式；无需对未知高阶径向导数再作估计。

**同一个角积分的端值。**
由于 $d\Omega=0$，(T.17)中已选定的同一 $\alpha$ 在固定角上沿有限径向长度有极限；
(T.29)给
$$
                 \alpha(a,\theta)\longrightarrow
                         \theta+\alpha_f
                         \quad\hbox{于 }C^1 .
 \tag{T.30}
$$
严格地，先以有界 $\Omega_a$ 得到固定角处的Cauchy极限，
再用 $\alpha_\theta=\Omega_\theta\to1$ 得到全圆一致极限；
最后 $\alpha_a=\Omega_a\to0$ 给物理径向一jet。
$\alpha_f$ 是此前同一次连接积分的输出，未在平端重新选择frame。

(T.17)给 $X_a=e^{i\alpha}(f+i g_1)$、
$X_\theta=i h e^{i\alpha}$。其径向一导有界，故 $X$ 亦存在全圆端值。
由 $X_\theta\to ia_f e^{i(\theta+\alpha_f)}$，准确有
$$
                    X_f(\theta)=c+a_f e^{i(\theta+\alpha_f)}
 \tag{T.31}
$$
其中 $c\in\mathbb C$ 是一个常数。它与(T.18)的全域quarter平移满足
$b_0=(1-i)c$。所以圆心由同一已重建的连通面确定；
不是每层或每个端点新选一个平移。

**真正的二阶拼接。**
将(T.28)--(T.30)代入同一个微分式，逐项得到
$$
 \begin{array}{lll}
 X_a\to e^{i(\theta+\alpha_f)},&
 X_\theta\to ia_f e^{i(\theta+\alpha_f)},&
 X_{aa}\to0,\\
 X_{a\theta}\to i e^{i(\theta+\alpha_f)},&
 X_{\theta\theta}\to-a_f e^{i(\theta+\alpha_f)}.&
 \end{array}                                             \tag{T.32}
$$
例如
$X_{aa}=e^{i\alpha}\{i\Omega_a(f+i g_1)+f_a+i(g_1)_a\}$，
$X_{\theta\theta}=e^{i\alpha}\{-\Omega_\theta h+i h_\theta\}$；
没有把一阶极限未经微分证明地升级为二阶极限。

在 $0\le a\le a_f$ 定义
$$
             X(a,\theta)=c+a e^{i(\theta+\alpha_f)},
                  \qquad z(a,\theta)=z_f .               \tag{T.33}
$$
(T.25)、(T.31)--(T.32)证明整张空间映射在 $a_f$ 真正 $C^2$ 拼接。
在材料Cartesian坐标 $(x,y)=(a\cos\theta,a\sin\theta)$，
(T.33)就是一个固定平面仿射等距映射，因此中心 $a=0$ 也无坐标奇点。
度量在盘内为 $da^2+a^2d\theta^2$；(T.26)保证与外侧同一目标metric的相应正则性。
若空间高度约定为 $Z_0-z$，同步使用常数 $Z_0-z_f$，
不改变这些拼接恒等式。
因此本次exact tail取得一个**真实完整平盘的 $C^2$ immersion延拓**，
而非只取得标量高度的平延。盘内第二基本形式准确为0。

该盘对任意 $\tau$ 都满足
$$
       G(a,\theta+\tau)=\mathcal R_{\ell,\tau}G(a,\theta),
 \quad 0\le a\le a_f,\qquad
       \ell=\{(\operatorname{Re}c,\operatorname{Im}c,s):s\in\mathbb R\}.
 \tag{T.34}
$$
这是固定材料圆盘上的真实全圆作用；外部只需原四重周期。
本节没有把外部整个面也宣布为旋转面。

**在core和腰条件真正解出之后的同轴结论。**
此段明确条件于第9节(T.23)的完整core/cap matching和真实腰条件。
曲率、metric的同一四重周期及一次frame的唯一重建，
把(T.18)的固定quarter空间旋转从tail传到同一个core；
没有另选core的旋转轴。腰曲线因此在同一个
$\mathcal R_{\ell,\pi/2}$ 下不变。
M.9--M.11给出的腰平面 $\Pi$ 包含这条闭正则曲线。
这样的曲线不可能包含在一条直线中，
所以其平面唯一；quarter旋转必保持 $\Pi$。
绕 $\ell$ 的 $\pi/2$ 旋转只有轴向的实特征直线，
从而 $\Pi$ 的法向平行 $\ell$，即 $\Pi$ 是水平平面。

因此(T.24)的腰镜像把上平盘映到同轴的下平盘；
两盘的材料角只带各自固定的相位offset，均满足(T.34)的相同作用。
设腰高度为 $z_w$，两中心高度为 $z_f$ 与 $2z_w-z_f$。
其距离 $2|z_f-z_w|$ 是实际一次积分的输出，
不是本节能任意指定或置零的量。
两盘互异、所需正高度区间、全域无自交/reach及marker几何，
仍须原第9节已经列出的同一全域预算。

本节由S的实际强层界补齐了真平盘正则与局部action身份。
它没有解出尚缺的(T.23)、waist振幅/设计行，
也没有把已有body/far解自动称为全闭嵌入。
当这些真实方程和原全域几何门都完成后，
才可以对最终单个 $G$ 使用第8节引用的固定metric相位--marker族。
