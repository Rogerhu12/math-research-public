# R726 — 球面端层的转向速度、强单调均值及条件存在

2026-11-28（UTC）。**已证明：将端层的归一化线段改成最短球面弧，可以在固定物理宽度下把显式转向速度从 \(2\tan(\theta/2)\) 改成 \(\theta\)；在明确的共同急角域内，完整端层均值有弦距离强单调性、非扩张性及可逆的切向 Jacobian。本文给出可直接检验的球冠条件来保证正均值根存在，继而证明唯一性、完整两角导数与根扰动界。**

这是一个新的端层机制及其完整条件证明，不是把 R725 改名。它改变了端层的准确均值函数，因此不能直接继承旧归一化 blend 的 R709 全局凸势、旧均值根、原校准词或 R722 的专用后验公式。本文没有宣称当前任何运行已满足新的球冠条件，没有改动已经运行的25或准备中的26，更没有得到课题 README 要求的完整闭面、全时间 reach 或固定参数精化。

已有 [R725](R725-fixed-width-boundary-cutoff-and-curvature-decomposition.md) 的三片 cutoff 和全部高阶代价、[R724](R724-paired-halfwave-central-seed-and-complete-source-identity.md) 的成对中央半波以及 [R711](R711-smooth-triangle-central-profile-and-geometric-comparison.md) 的准确幅度反解仍作为已证明的对象使用，不在本文重做。

## 1. 固定对象、准确方程及作用域

沿用 R725 的同一物理材料坐标 \(s\in[0,S]\)、固定度量及两个支撑

\[
 U/S=[1/32,15/32]\cup[17/32,31/32],\qquad |U|=L=7S/8.
 \tag{1}
\]

固定四端层总长 \(b\in(0,L)\)，各长 \(\Delta=b/4\)；端层之并记为 \(E\)，中央总长为 \(L_c=L-b>0\)。本文比较时 \(S,U,E,b,\Delta,L_c\) 都不变。固定准确单位参考切向

\[
 u(s,\phi)=T_0(s,\phi),\qquad |u|=1,
 \tag{2}
\]

以及原准确 core、帽高、补集积分与目标

\[
 K(\phi)=P(\phi)-\Gamma_0(\phi)
                  -\int_{U^c}T_0(s,\phi)\,ds.
 \tag{3}
\]

固定 \(0<\epsilon<1/2\)。在每个左端层使用 R725 的
\(\chi=C_\epsilon(t)\)，右端层使用 \(\chi=C_\epsilon(1-t)\)，其中
\(t\) 是该物理端层上的准确仿射坐标。这里 \(\chi\) 与待解方向及角度 \(\phi\) 无关。R725 已证明

\[
 0\le\chi\le1,\quad
 \int_E\chi\,ds=b/2,\quad
 \|\chi_s\|_\infty=\frac4{b(1-\epsilon)},
 \tag{4}
\]

以及外侧值0、内侧值1、端口前三阶零导数、八个准确内部切点和 \(C^3\) 接合。后面的均值结论也适用于任何满足
\(0\le\chi\le1\) 及 \(\int_E\chi=b/2\) 的固定可测 cutoff；光滑拼接结论另外使用 R725 的正则性。

中央沿 R724 的两个等长相反半波，其合并准确积分为 \(L_c r d\)，其中
\(d\in\mathbb S^2,\ 0<r<1\)。置 \(\alpha=L_c r\)，端层更换后须真正重新求解

\[
 \alpha d+B(d,\phi)=K(\phi),\qquad
 B(d,\phi)=\int_E {\cal S}_{\chi(s)}(u(s,\phi),d)\,ds,
 \qquad 0<\alpha<L_c.
 \tag{5}
\]

本文所有积分均是整个物理 \(E\) 上的准确积分，不是有限节点工作求和。提出任何已支付的数值界，都还要有完整原分片、角域、尾项和算术费用。

## 2. 球面插值及零夹角的光滑延拓

对单位 \(u,d\) 且 \(u\ne-d\)，令
\(\theta=\arccos(u\cdot d)\in[0,\pi)\)，定义

\[
 {\cal S}_{\chi}(u,d)=
 \frac{\sin((1-\chi)\theta)}{\sin\theta}\,u
 +\frac{\sin(\chi\theta)}{\sin\theta}\,d.
 \tag{6}
\]

当 \(\theta=0\) 时取连续值 \(u=d\)。若 \(\theta>0\)，写

\[
 d=\cos\theta\,u+\sin\theta\,e,\qquad
 e\perp u,\quad |e|=1.
\]

代入(6)立即得到

\[
 {\cal S}_{\chi}=\cos(\chi\theta)u+\sin(\chi\theta)e.
 \tag{7}
\]

故 \(|{\cal S}_{\chi}|=1\)，两端值分别为 \(u,d\)，并且(7)是从 \(u\) 到 \(d\) 的最短球面弧的比例 \(\chi\) 参数。

**零夹角不是导数奇点。** 置 \(z=u\cdot d,\ w=\theta^2\)。
函数 \(q(w)=1-\cos\sqrt w\) 在零附近为实解析函数，
\(q(0)=0,q'(0)=1/2\ne0\)，所以逆函数定理给出
\(w=w(1-z)\) 的实解析延拓。任意实数 \(a\) 附近都有

\[
 \frac{\sin(a\theta)}{\sin\theta}
 =a\,\frac{\operatorname{sinc}(a\sqrt w)}
              {\operatorname{sinc}(\sqrt w)},\qquad
 \operatorname{sinc}(x)=\frac{\sin x}{x},\quad
 \operatorname{sinc}(0)=1.
 \tag{8}
\]

右端是 \(a,w\) 的联合光滑函数，分母在 \(w=0\) 非零。取
\(a=\chi,1-\chi\) 即证明(6)在 \(u=d\) 的联合光滑性。远离零夹角时由普通公式成立。因此 \({\cal S}\) 在
\([0,1]\times\{(u,d)\in\mathbb S^2\times\mathbb S^2:u\ne-d\}\)
上联合光滑。只有反足 \(u=-d\) 没有本文定义的唯一最短弧，必须以真实假设排除。

若需要把导数作用到含法向分量的二阶变化，统一使用以下已定义的光滑零次齐次延拓：

\[
 \widehat{\cal S}_{\chi}(x,y)
 ={\cal S}_{\chi}(x/|x|,y/|y|).
 \tag{9}
\]

(9)在单位球附近且没有反足的开集光滑。后文所有外在一、二阶微分均指(9)，不把只定义在切空间的微分误用到二阶法向分量。

对任意正交矩阵 \(Q\in O(3)\)，点积与范数不变，因而

\[
 {\cal S}_{\chi}(Qu,Qd)=Q{\cal S}_{\chi}(u,d).
 \tag{10}
\]

此处包括反射；这是一条插值协变性质，尚不是完整曲面在不标记刚体商中的分离证明。

## 3. 固定宽度下的显式转向速度

由(7)对 \(\chi\) 微分，

\[
 \partial_\chi{\cal S}_{\chi}
 =\theta[-\sin(\chi\theta)u+\cos(\chi\theta)e],
 \qquad
 |\partial_\chi{\cal S}_{\chi}|=\theta.
 \tag{11}
\]

固定 \(d,\chi\)，把 \(u\) 向 \(d\) 的球面极坐标作为自变量。
对径向单位变化，\(D_u{\cal S}\) 的长度因子为 \(1-\chi\)；
对方位单位变化，其因子为

\[
 \frac{\sin((1-\chi)\theta)}{\sin\theta}.
 \tag{12}
\]

这是把(7)改写成以 \(d\) 为极点、比例为 \(1-\chi\) 的同一球面极坐标式后分别微分所得，两个像方向正交。零角由(8)取极限。

因此在共同急角界 \(0\le\theta\le\theta_*\le\pi/2\) 下，两个因子均不超过1。实际 \(d=d(\phi)\) 不随 \(s\) 变化，于是

\[
 \begin{split}
 T_s&=D_u{\cal S}_{\chi}[u_s]
                       +\chi_s\partial_\chi{\cal S}_{\chi},\\
 |T_s|&\le |u_s|+\theta_*|\chi_s|
       \le |u_s|+\frac{4\theta_*}{b(1-\epsilon)}.
 \end{split}
 \tag{13}
\]

更一般，若只有 \(\theta\le\theta_*<\pi\)，因
\(\theta/\sin\theta\) 在 \((0,\pi)\) 单调增加、且
\(\sin((1-\chi)\theta)\le(1-\chi)\theta\)，有

\[
 |T_s|\le
 \frac{\theta_*}{\sin\theta_*}|u_s|
       +\frac{4\theta_*}{b(1-\epsilon)}.
 \tag{14}
\]

\(\theta_*=0\) 时该比值取1。本文后续强单调及存在定理使用急角假设，不能把(14)的较大范围移植到那些定理。

对 R725 的固定选择 \(\epsilon=1/8\)，(13)中的显式转向项为

\[
 \boxed{\frac{32\theta_*}{7b}}.
 \tag{15}
\]

R725 对同宽度、同 cutoff、同一已成立角度上界的归一化线段给出的对应项为
\(64\tan(\theta_*/2)/(7b)\)。当 \(\theta_*>0\) 时，

\[
 \frac{32\theta_*/(7b)}
      {64\tan(\theta_*/2)/(7b)}
 =\frac{\theta_*}{2\tan(\theta_*/2)}<1,
 \tag{16}
\]

因为 \(\tan x>x\) 对 \(0<x<\pi/2\) 成立。等角极限的比值是1。

(16)仅比较显式 cutoff 转向项。两个机制的准确 \(d,r\) 和中央幅度根会改变；不同场之间没有自动共有的 \(\theta_*\)。完整 \(T_s\)、位置、角导数、normal32 修正、shape operator 及整面最大曲率均不能由(16)直接排序。

**定理1（固定端向量的近最优速度）。**
固定单位 \(u,d\) 和夹角 \(0<\theta<\pi\)。任意连接它们的 \(C^1\) 单位球曲线 \(v:[0,\Delta]\to\mathbb S^2\) 满足

\[
 \sup |v_s|\ge\theta/\Delta.
 \tag{17}
\]

若另要求 \(v_s(0)=v_s(\Delta)=0\)，则不等式严格；该类的下确界仍为 \(\theta/\Delta\)。R725 cutoff 的球面弧满足

\[
 \sup |({\cal S}_{C_\epsilon(s/\Delta)})_s|
       =\frac{\theta}{\Delta(1-\epsilon)}.
 \tag{18}
\]

**证明。** 球面曲线长度至少是两端的球面距离 \(\theta\)，故
\(\theta\le\int_0^\Delta|v_s|\,ds\le\Delta\sup|v_s|\)。
若端速度为零且最大值等于 \(\theta/\Delta>0\)，连续性使端部一个正长度区间的速度严格小于该最大值，于是积分严格小于 \(\theta\)，矛盾。(18)由(11)和 R725 精确峰值直接成立，且 \(\epsilon\downarrow0\) 给出所述下确界。证毕。

这是固定端向量的速度结论，没有把真实 \(u_s\ne0\) 的场或完整曲率优化缩成该特例。R725 的二、三阶导数分别含 \(\epsilon^{-1},\epsilon^{-2}\) 成本，仍全部存在；不以令 \(\epsilon\to0\) 代替固定参数的全域计算。

## 4. 急角域内的强单调与非扩张

**定理2（单端点映射的弦界）。**
固定 \(u\in\mathbb S^2,\ \chi\in[0,1]\)。若
\(\theta_i=\arccos(u\cdot d_i)\le\theta_*\le\pi/2\)，则

\[
 \begin{split}
 [ {\cal S}_{\chi}(u,d_1)-{\cal S}_{\chi}(u,d_0)]
           \cdot(d_1-d_0)
 &\ge \chi\cos((1-\chi)\theta_*)\,|d_1-d_0|^2\\
 &\ge \chi^2|d_1-d_0|^2,
 \end{split}
 \tag{19}
\]

以及

\[
 |{\cal S}_{\chi}(u,d_1)-{\cal S}_{\chi}(u,d_0)|
       \le |d_1-d_0|.
 \tag{20}
\]

**证明。** 当两角非零时写
\(d_i=\cos\theta_i\,u+\sin\theta_i\,e_i\)，令
\(c=e_0\cdot e_1\in[-1,1]\)，
\(h=(\theta_1-\theta_0)/2\)，
\(\bar\theta=(\theta_1+\theta_0)/2\)。
由(7)展开两向量差的内积，得到准确恒等式

\[
 \begin{split}
 ({\cal S}_1-{\cal S}_0)\cdot(d_1-d_0)
 ={}&4\sin(\chi h)\sin h
               \cos((1-\chi)\bar\theta)\\
 &+(1-c)\{
     \sin(\chi\theta_1)\sin\theta_0+
     \sin(\chi\theta_0)\sin\theta_1\}.
 \end{split}
 \tag{21}
\]

同时

\[
 |d_1-d_0|^2=4\sin^2h+
                  2(1-c)\sin\theta_0\sin\theta_1.
 \tag{22}
\]

正弦在 \([0,\pi]\) 的凹性给
\(\sin(\chi x)\ge\chi\sin x\) 对
\(x\in[0,\pi/2]\) 成立。若 \(h<0\)，(21)中的两个正弦同时变号，其乘积仍不小于 \(\chi\sin^2 h\)。
又
\(\cos((1-\chi)\bar\theta)\ge\cos((1-\chi)\theta_*)\ge0\)。
故(21)第一项至少为(22)第一项乘
\(\chi\cos((1-\chi)\theta_*)\)，第二项至少为(22)第二项乘 \(\chi\)，从而得到(19)第一行。最后

\[
 \cos((1-\chi)\theta_*)\ge
 \cos((1-\chi)\pi/2)=\sin(\chi\pi/2)\ge\chi,
\]

得第二行。

另由(7)直接展开

\[
 |{\cal S}_1-{\cal S}_0|^2
 =4\sin^2(\chi h)
  +2(1-c)\sin(\chi\theta_0)\sin(\chi\theta_1).
 \tag{23}
\]

急角范围中 \(\sin(\chi|h|)\le\sin|h|\)，
\(\sin(\chi\theta_i)\le\sin\theta_i\)，故(23)不超过(22)。
零角、\(\chi=0,1\) 由连续延拓包含，证明完毕。

对固定 \(\phi\)，定义共同急角域

\[
 {\cal A}_{\phi}
 =\{d\in\mathbb S^2:\ u(s,\phi)\cdot d\ge0
                         \text{ 对几乎处处 }s\in E\}.
 \tag{24}
\]

对连续数据可以把几乎处处改成全部 \(s\)。把(19)–(20)在整个 \(E\) 积分，得

\[
 \begin{split}
 [B(d_1)-B(d_0)]\cdot(d_1-d_0)
   &\ge m_B|d_1-d_0|^2,\\
 |B(d_1)-B(d_0)|&\le b|d_1-d_0|,\qquad
 m_B=\int_E\chi(s)^2\,ds\ge b/4,
 \end{split}
 \tag{25}
\]

其中最后一步是
\((\int_E\chi)^2\le b\int_E\chi^2\) 和(4)。两点只须都在
\({\cal A}_{\phi}\)；证明不需要把两点的欧氏弦段当成单位方向，也没有省去沿弦的径向正则性问题。

若已有更小共同 \(\theta_*\)，可以把 \(m_B\) 提高到
\(\int_E\chi\cos((1-\chi)\theta_*)\,ds\)；(25)采用对全急角域都成立的简明下界。

## 5. 可检验的正均值根存在条件

强单调性本身不能保证目标 \(K\) 落在值域。以下单独支付存在性。

固定一个角度，写 \(K=k e\)，其中 \(k=|K|>0,\ |e|=1\)。
选择 \(0<\eta<\pi/2,\ \beta\ge0\)，满足

\[
 \arccos(u(s)\cdot e)\le\beta\quad(s\in E),\qquad
 \theta_*=\beta+\eta\le\pi/2.
 \tag{26}
\]

考虑闭球冠
\({\cal C}_{\eta}=\{d\in\mathbb S^2:d\cdot e\ge\cos\eta\}\)。
由球面距离三角不等式，球冠内任意 \(d\) 对所有 \(u(s)\) 都满足夹角不超过 \(\theta_*\)。

定义两个准确单维端层量

\[
 c_*=\int_E\cos((1-\chi(s))\theta_*)\,ds,\qquad
 s_*=\int_E\sin((1-\chi(s))\theta_*)\,ds.
 \tag{27}
\]

**定理3（球冠存在、正性和上界）。**
若(26)成立，并有三个严格余量

\[
 \boxed{\quad k>b,\qquad k\sin\eta>s_*,
                     \qquad k-c_*<L_c,\quad}
 \tag{28}
\]

则(5)有一个球冠内部的解，且

\[
 0<k-b\le\alpha\le k-c_*<L_c.
 \tag{29}
\]

它是在共同急角域 \({\cal A}_{\phi}\) 内所有 \(\alpha>0\) 解中的唯一解。

(27)不必用粗总长代替；若只使用显式解析量，以下更保守条件已足够：

\[
 k>b,\qquad
 k\sin\eta>b\sin(\theta_*/2),\qquad
 k-\frac b2(1+\cos\theta_*)<L_c.
 \tag{30}
\]

**证明。** 对 \(z\in[0,1]\) 定义

\[
 f_{\chi}(z)=
 \begin{cases}
 [\cos((1-\chi)\arccos z)-1]/(1-\chi),&\chi\ne1,\\
 0,&\chi=1.
 \end{cases}
 \tag{31}
\]

在 \(\chi=1\) 的延拓光滑，因为分子对 \(1-\chi\) 二阶消失；
在 \(z=1\) 的光滑性由(8)的同一平方角参数证明。直接微分得

\[
 f_\chi'(z)
 =\frac{\sin((1-\chi)\arccos z)}
        {\sqrt{1-z^2}},
 \tag{32}
\]

零角取极限。令球冠上的势函数为

\[
 V(d)=\int_E f_{\chi(s)}(u(s)\cdot d)\,ds-K\cdot d.
 \tag{33}
\]

由(6)、(32)，其球面梯度恰为

\[
 \nabla_{\mathbb S^2}V=P_d[B(d)-K],\qquad
 P_d=I-dd^T.
 \tag{34}
\]

这里(6)中乘 \(d\) 的项在球面投影后为零。因此(33)确实产生所需切向方程。本文没有宣称它是 R709 原闭单位球上的欧氏凸势。

\(V\) 在紧球冠连续，必有极小点。若 \(d\) 位于球冠边界，取向内切向

\[
 w=e-\cos\eta\,d,\qquad |w|=\sin\eta,\qquad
 w\cdot e=\sin^2\eta>0.
 \tag{35}
\]

由(7)，\({\cal S}_\chi(u,d)\) 与 \(d\) 的夹角是
\((1-\chi)\theta\)，故

\[
 |P_dB(d)|\le
 \int_E\sin((1-\chi)\theta(s))\,ds\le s_*.
\]

于是

\[
 DV(d)[w]=(B-K)\cdot w
 \le s_*\sin\eta-k\sin^2\eta<0.
 \tag{36}
\]

沿 \(w\) 的小球面位移进入球冠，因此边界点不可能是极小点。
极小点在内部，由(34)有
\(K-B(d)=\alpha d\) 对某实数 \(\alpha\) 成立。

沿 \(e\) 点积，因 \(|B|\le b\)，

\[
 \alpha(d\cdot e)=k-B\cdot e\ge k-b>0.
\]

\(d\cdot e>0\)，故 \(\alpha>0\)；又 \(d\cdot e\le1\)，得到
\(\alpha\ge k-b\)。沿 \(d\) 点积，并使用(26)–(27)，得到

\[
 \alpha=k(d\cdot e)-B(d)\cdot d
 \le k-\int_E\cos((1-\chi)\theta(s))\,ds
 \le k-c_*<L_c.
\]

这证明存在和(29)。

若 \((\alpha_i,d_i)\) 是共同急角域的两个正解，相减后与
\(d_1-d_0\) 点积，使用(25)和单位长度恒等式，得

\[
 0\ge
 \left(\frac{\alpha_0+\alpha_1}{2}+m_B\right)|d_1-d_0|^2.
 \tag{37}
\]

括号严格为正，所以 \(d_1=d_0\)，再由方程得
\(\alpha_1=\alpha_0\)。这也排除了球冠外但仍在同一共同急角域内的其他正根；对急角域外的根不作断言。

最后，余弦在 \([0,\theta_*]\) 凹，位于端点弦之上，故

\[
 \cos((1-\chi)\theta_*)\ge
                  \chi+(1-\chi)\cos\theta_*.
\]

积分给 \(c_*\ge b(1+\cos\theta_*)/2\)。正弦在该区间凹，Jensen 不等式及(4)给
\(s_*\le b\sin(\theta_*/2)\)。于是(30)蕴含(28)。证毕。

这一定理的 \(k,\beta,\eta,c_*,s_*\) 都属于当前准确输入及整个端层，不能用某个角节点的工作值代替。若(28)未通过，结论只是本充分条件未支付，不是方程不存在；可以改用更紧的完整界或另一种完整存在证明，不能把条件失败当作任务结束。

## 6. 完整切向 Jacobian 与逆界

**定理4（正根处的全三维可逆性）。**
在共同急角域内，令 \(\alpha>0\)。对
\(\delta\alpha\in\mathbb R,\ v\in T_d\mathbb S^2\)，定义

\[
 {\cal J}(\delta\alpha,v)
   =d\,\delta\alpha+\alpha v+D_dB[v].
 \tag{38}
\]

则 \({\cal J}:\mathbb R\times T_d\mathbb S^2\to\mathbb R^3\)
是同构。对 \({\cal J}(\delta\alpha,v)=f\) 有

\[
 |v|\le\frac{|f|}{\alpha+m_B},\qquad
 |\delta\alpha|
 \le\left(1+\frac b{\alpha+m_B}\right)|f|.
 \tag{39}
\]

**证明。** 固定一个 \(u\)，在 \(T_d\mathbb S^2\) 内取朝向
\(u\) 的经线单位方向及正交的方位方向。由(7)微分再投影到
\(T_d\mathbb S^2\)，线性映射
\(P_dD_d{\cal S}_\chi\) 在该正交基中为对角阵，其两个特征值是

\[
 \chi\cos((1-\chi)\theta),\qquad
 \frac{\sin(\chi\theta)}{\sin\theta}.
 \tag{40}
\]

零角时两者都取 \(\chi\)。第一个在急角域不小于 \(\chi^2\)，第二个由正弦凹性不小于 \(\chi\ge\chi^2\)。每个积分项因此自伴且下界为 \(\chi^2 I\)，积分后

\[
 P_dD_dB|_{T_d\mathbb S^2}\succeq m_B I.
 \tag{41}
\]

未经投影的 \(D_d{\cal S}\) 的两个长度因子分别是
\(\chi\) 及(40)的第二项；急角下均不超过1，故
\(\|D_dB|_{T_d\mathbb S^2}\|\le b\)。这里法向分量没有被当成零。

将(38)投影到切空间，得到正定方程

\[
 [\alpha I+P_dD_dB]v=P_df.
 \tag{42}
\]

它有唯一解并给出(39)第一界。随后由径向分量唯一恢复

\[
 \delta\alpha=d\cdot f-d\cdot D_dB[v],
 \tag{43}
\]

得到第二界。没有未支付的第三方向，证明完成。

(39)是 \((\alpha,d)\) 方程的逆界，不是完整 normal 解的 \(C_u\) 或全场 Jacobian 逆界。已有准确 normal 费用仍须对其自己的全部32阶段支付。

## 7. 完整两角导数、幅度反解与对称

假设在一个角区间，\(K\) 为 \(C^2\)，\(u\) 及其两角导数联合连续并在整个固定 \(E\) 上有共同可积控制。假设第5节条件逐角成立且所用反足排除与三个严格余量局部保持。则积分可两次求导，定理4和普通隐函数定理给出唯一 \(C^2\) 分支
\((\alpha(\phi),d(\phi))\)。若数据在紧角圆上满足共同严格余量，局部分支由唯一性拼成整个角圆上的 \(C^2\) 分支。

下面给出全二阶方程，以免把隐函数定理当成省略费用的口号。把

\[
 B(\phi,y)=\int_E\widehat{\cal S}_{\chi(s)}(u(s,\phi),y)\,ds
 \tag{44}
\]

延拓到单位球附近。其关于 \(y\) 零次齐次，因而
\(B_d[d]=0\)。下标 \(\phi\) 表示固定 \(d\) 的偏导，撇表示真实分支的全导数。第一阶方程为

\[
 {\cal J}(\alpha',d')=K'-B_\phi,\qquad d'\perp d.
 \tag{45}
\]

具体地

\[
 \begin{split}
 B_\phi&=\int_E D_u\widehat{\cal S}[u_\phi]\,ds,\\
 B_{\phi\phi}
 &=\int_E\big\{
 D_u\widehat{\cal S}[u_{\phi\phi}]
 +D_{uu}^2\widehat{\cal S}[u_\phi,u_\phi]\big\}\,ds,\\
 B_{d\phi}[v]
 &=\int_E D_{du}^2\widehat{\cal S}[v,u_\phi]\,ds,\qquad
 B_{dd}[v,v]=\int_E D_{dd}^2\widehat{\cal S}[v,v]\,ds.
 \end{split}
 \tag{46}
\]

所有偏导在真实的 \(u(s,\phi),d(\phi),\chi(s)\) 处取值。
固定端层和固定 cutoff 使这里没有移动积分端点或 \(\chi_\phi\) 项；若另行改变该假设，必须重新加入那些项。

令 \(q=|d'|^2\)，\(w=P_dd''\)。单位约束给
\(d''=w-q d\)。再次对(5)求导，并保留每项，得到

\[
 \begin{split}
 {\cal J}(\alpha''-\alpha q,w)
 ={}&K''-2\alpha'd'
       -B_{dd}[d',d']-2B_{d\phi}[d']-B_{\phi\phi},\\
 d''={}&w-q d.
 \end{split}
 \tag{47}
\]

推导中 \(B_d[-q d]=0\) 来自(44)的齐次性，而
\(-\alpha q d\) 已移入(47)第一分量；没有丢掉球面的法向加速度。
先用同一个可逆 \({\cal J}\) 解(47)，再恢复
\(\alpha''=(\alpha''-\alpha q)+\alpha q\)，即得到完整二阶分支。
(39)可分别作用于(45)和(47)的完整右端。准确界必须包括
\(B_{dd},B_{d\phi},B_{\phi\phi}\) 的全部积分与算术误差，不可只付均值值误差。

端层的两角导数也完整为

\[
 \begin{split}
 T_\phi={}&D_u\widehat{\cal S}[u_\phi]
                 +D_d\widehat{\cal S}[d'],\\
 T_{\phi\phi}={}&D_u\widehat{\cal S}[u_{\phi\phi}]
   +D_d\widehat{\cal S}[d'']
   +D^2_{uu}\widehat{\cal S}[u_\phi,u_\phi]\\
 &+2D^2_{ud}\widehat{\cal S}[u_\phi,d']
   +D^2_{dd}\widehat{\cal S}[d',d'].
 \end{split}
 \tag{48}
\]

这里使用(9)，因此 \(u_{\phi\phi},d''\) 的法向部分确实进入正确全导数。

令 \(r=\alpha/L_c\)，有
\(r'=\alpha'/L_c,\ r''=\alpha''/L_c\)。
在 R711 已证明的准确反解支上取 \(A_\delta(\lambda)=r\)，
其 \(A_\delta'\ne0\)，则

\[
 \lambda'=\frac{r'}{A_\delta'(\lambda)},\qquad
 \lambda''=
 \frac{r''-A_\delta''(\lambda)(\lambda')^2}
      {A_\delta'(\lambda)}.
 \tag{49}
\]

第5节给 \(0<r<1\)；紧参数域的共同余量使其留在该开区间的紧子集。
原辅助十二片、幅度值与两阶幅度费用仍必须全部计算。不能继承旧端层下同名 \(r,d,\lambda\) 的工作数值。

如果数据具有周期或反射协变
\(u(s,\sigma\phi)=Q u(s,\phi)\)、\(K(\sigma\phi)=QK(\phi)\)，且端层/cutoff在相应变换下保持，(10)把一个正根变成另一角的正根。共同急角域与球冠同样被 \(Q\) 映射，唯一性给
\(\alpha(\sigma\phi)=\alpha(\phi)\)、
\(d(\sigma\phi)=Qd(\phi)\)。若材料端层也被重排，只要该重排保测度、原方向和完整 cutoff，换元给同一结论。中央还须使用 R724 的完整框架协变约定，不能靠端层(10)免去它。

这些结论关于准确种子的角变量。全 flex 时间的强 \(C^2\) 连续性还需原场、全部后续 normal/core/lift、帽与接缝的相应统一正则性；本文没有把一个角分支等同于完整时间族。

## 8. 两个正根的稳定性与跨机制变化账

设 \((\alpha_i,d_i)\) 分别满足

\[
 \alpha_i d_i+B_i(d_i)=K_i,\qquad \alpha_i>0,\quad i=0,1.
 \tag{50}
\]

假定 \(d_0,d_1\) 都位于 \(B_1\) 的共同急角域，且 \(B_1\) 满足
(25)，其常数为 \(m_1>0\)、总端长为 \(b\)。定义准确残差

\[
 E=K_1-K_0-[B_1(d_0)-B_0(d_0)],\qquad e=|E|.
 \tag{51}
\]

**定理5（两个真实正根的条件稳定界）。**

\[
 \boxed{\quad
 |d_1-d_0|\le
 \frac{2e}{\alpha_0+\alpha_1+2m_1},\qquad
 |\alpha_1-\alpha_0|\le e+b|d_1-d_0|.
 \quad}
 \tag{52}
\]

若两边的 \(L_c\) 相同，则
\(|r_1-r_0|\le(e+b|d_1-d_0|)/L_c\)。

**证明。** (50)相减并把 \(B_1(d_0)-B_0(d_0)\) 移入右端，得

\[
 \alpha_1d_1-\alpha_0d_0+
       [B_1(d_1)-B_1(d_0)]=E.
\]

与 \(d_1-d_0\) 点积，(25)和(37)给
\([(\alpha_0+\alpha_1)/2+m_1]|d_1-d_0|^2
 \le e|d_1-d_0|\)，即第一界。反三角不等式与
\(|\alpha_i d_i|=\alpha_i\) 给

\[
 |\alpha_1-\alpha_0|
 \le|\alpha_1d_1-\alpha_0d_0|
 \le e+|B_1(d_1)-B_1(d_0)|
 \le e+b|d_1-d_0|.
\]

证毕。该结果以两个根的真实存在为前提；不能把(52)单独用作缺失的存在证明。

若只改变球面 cutoff、保持 \(u,d_0,K\) 不变，由(7)可准确写出

\[
 |{\cal S}_{\chi_1}(u,d_0)
       -{\cal S}_{\chi_0}(u,d_0)|
 =2\left|\sin\frac{(\chi_1-\chi_0)\theta}{2}\right|
 \le\theta|\chi_1-\chi_0|.
 \tag{53}
\]

在整个 \(E\) 积分给 \(e\) 的上界；有共同角上界时可用
\(\theta_*\int_E|\chi_1-\chi_0|\,ds\)。这仍不免去根变化导致的
\(d,r,\lambda\) 与全部角 jet 变化。

若 \(B_0\) 是 R725 的归一化线段、\(B_1\) 是本文球面弧，且使用同
\(u,\chi,K\)，令

\[
 n=\sqrt{(1-\chi)^2+\chi^2+2\chi(1-\chi)\cos\theta}.
\]

两单位向量的准确点积为

\[
 N((1-\chi)u+\chi d_0)\cdot{\cal S}_{\chi}(u,d_0)
 =
 \frac{(1-\chi)\cos(\chi\theta)
       +\chi\cos((1-\chi)\theta)}{n}.
 \tag{54}
\]

因此其准确距离是

\[
 \left[
 2-2\frac{(1-\chi)\cos(\chi\theta)
       +\chi\cos((1-\chi)\theta)}{n}
 \right]^{1/2}.
 \tag{55}
\]

该表达式在准确数学中非负，零角为零；工作浮点实现不得用未声明的裁剪掩盖误差。(54)来自旧线段的两个系数与新弧对
\(u,d_0\) 的内积，故没有省略投影。把(55)在完整端层积分给(51)的
\(e\) 上界，再使用(52)，就有跨机制的完整条件根变化账。
旧根是否落在新急角域、两个真实根是否存在都必须另行满足。

## 9. 端口拼接、完整位置及保留区域

在外端口 \(\chi=0,\chi_s=0\)，有
\(T=u,\ T_s=u_s\)；在内端口 \(\chi=1,\chi_s=0\)，有
\(T=d,\ T_s=0\)。由(6)的恒等端值，全部 \(\phi\) 一、二阶导数也分别等于
\(u_\phi,u_{\phi\phi}\) 和 \(d',d''\)。R725 的 \(C^3\) cutoff、(8)的光滑性及真实 \(u,d\) 正则性保证所有内部八切点的相应接合。R724 中央 profile 仍须满足其原端口条件；这些条件下，一阶切向与位置二阶拼接相容。

若两种**准确、同端点闭合**的 seed 使用同一 primitive 起点
\(\Gamma_0\)，则

\[
 F_i(s,\phi)=\Gamma_0(\phi)+\int_0^sT_i(\xi,\phi)\,d\xi
\]

满足

\[
 |F_1(s,\phi)-F_0(s,\phi)|
 \le
 \min\!\left\{
 \int_0^s|T_1-T_0|\,d\xi,\
 \int_s^S|T_1-T_0|\,d\xi
 \right\}.
 \tag{56}
\]

第一界来自共同起点；第二界使用两种完整准确均值闭合，故
\(\int_0^S(T_1-T_0)=0\)。中央段的 \(d,r,\lambda\) 都可能改变，
(56)中的积分必须包含这些段，不能只积端层。两角位置导数的变化同理需要积分完整的(48)及中央两角导数。

如果实现还有原 raw-defect lift，比较公式必须再包含那个 lift 的完整系数、实际全长缺陷和全部相应导数。仅在已经证明准确缺陷为零时，它才从准确比较式消失；有限工作词上的非零缺陷和其舍入不得丢弃。

尤其，\(T_1=T_0\) 在 \(U^c\) 只说明 primitive 差在每个补集分量为常向量，**不说明该常向量为零**。完整均值闭合保证终点闭合，却不自动保证两个支撑之间的保留区域没有平移。若该区间属于固定 \(H\)，必须对它的真实前缀积分或原局部化构造另行证明零位移；不能把导数的支撑性质误写成曲面的固定区域性质。

因此，固定 \(H\)、整像无对齐位移、闭面直径、全时间嵌入及 reach 都还是完整曲面的独立责任。第3节速度系数与第5节均值存在不替代这些责任。

## 10. 对当前求解路线的精确结论

本文已经完整证明以下数学事实：球面端层的联合光滑定义及正交协变；固定宽度的显式转向速度和端向量固定时的近最优性；共同急角域的强单调与非扩张；有实际可检验余量的正均值根存在与唯一性；完整三维逆界和两角导数；两真实正根的跨机制稳定与完整位置变化账。

当前25已经实际返回的有限曲率位置 \(s=2.1573631007205925,\ \phi=\pi/2\)、cell885及 \(K=12.32709940409259\)，只属于其原半波归一化 blend 场。它不是本文球面端层的结果；缺少实际 \(S\) 或完整准确材料地址映射时，也不能仅凭 cell 编号把热点归给某一物理片。26改变的是 R725 的 cutoff，仍保原归一化 blend；本文没有把26重命名成球面弧。

要把本文机制接入完整候选，必须真正更换端层、完整均值求解及两角导数；保原固定目标、全部自由变量、原各域、中央十二片、bubble/lift、normal32及原科学预算。新的 source/model/校准/缓存/纯消费者/准确后验必须描述实际新机制，不能只换旧文件的 SHA 或删除旧适用条件。尤其 R709 的欧氏凸势和旧 R722 的归一化分母界不能被假称为本文公式的证明。

源码的正常实现、完整源参数公开和授权的原科学计算可继续推进；本文不增加 AST、fixture、机器回放、独立审核或预演准入门。准确全域费用仍须实际支付，包括完整积分误差、零角稳定公式、端层八切点、两角分支、全部 normal 阶段和全场六jet/Gram/曲率/支撑/闭相位，以及同固定 \(g\)、参数和时刻的空间/频率/时间精化。

课题完成标准尚未满足。本文提供一个确切的新方向及其全条件论证，后续继续真正求解，不能停在该定理、某次有限改善或阶段报告上。
