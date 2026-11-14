# 文献与精确机制核查（2026-11-08）

研究会话：Astra-visible-flex-effcccee 的 literature-mechanisms 子任务。本文仅是文献与候选机制核查；没有声称达到本题完成标准。根目录协调由主会话负责。

## 已核实、应立即写入 HANDOFF 的事项

1. Ghomi 的 *Open Problems in Geometry of Curves and Surfaces*（2019-09-02 版本，Problem 1.1）仍把 R³ 中闭 C² 曲面的连续等距柔性列为开放问题；文中提到的可弯曲平坦环面位于 S³。这只能说明该文献日期的状态，不能代替本仓库 R520 的独立审计。
2. Payne 的 2023-11-16 UCSD 报告 *Flexible Smooth Immersions of Cylinders in R³* 明确给出的是非极小、非可展的柔性浸入圆柱；其闭曲面讨论仍称为 speculative approaches。此报告不能提供可直接复用的闭嵌入例子。
3. 网上可搜到 Anderson 的 *Local rigidity of surfaces in space forms* 的旧 PDF，含很强的闭嵌入曲面刚性声称，但其 arXiv:0709.3202 在 2009-09-06 的 v3 明确标记撤稿。**不得把该旧 PDF 当成当前有效的不可能性定理。** arXiv 页面没有给出可核实的详细撤稿原因，本记录不猜测原因。
4. Nassar 的平移曲面有限弯曲给出显式精确局部解，然而把两条正交平面闭曲线相加必有秩退化点，不是可用的光滑闭环面。其论文也明确区分闭合保持、周期保持与新折痕出现。
5. Bobenko–Hoffmann–Sageman-Furnas 于 2025 年正式发表首个紧致实解析 Bonnet 环面对。它是两个精确等距浸入；论文仍把两者均嵌入列为开放问题。其构造参数 ε 的连续变化会改变度量，不能当作本题连续柔性。
6. 本次独立推导排除了若干具体封口捷径：全局单张无折痕 Goursat/moulding 直接周期化；父会话的常挠率 ruled strip 沿固定 s 边界接刚性帽片；对称法向偏移加厚。它们都是特定构造类别的限制，不是一般闭曲面刚性定理。
7. 旧 R34 的四口片确有正负曲率与精确 C² 镜像拼接能力，但其中只有两个内口是圆柱口；两个外口是随横向坐标改变母线方向的可展平台。旧 R7、R30–35 都没有给出全部端口闭合的嵌入曲面；增大亏格不能免去固定材料配对、二阶接缝及所有回路的 SE(3) 周期方程。

主要来源：

- Ghomi: https://ghomi.math.gatech.edu/Papers/op.pdf
- Payne 2023 官方报告摘要: https://math.ucsd.edu/seminar/flexible-smooth-immersions-cylinders-r3
- Anderson 撤稿记录: https://arxiv.org/abs/0709.3202
- Nassar 原稿: https://arxiv.org/abs/2310.08505 ，正文 https://arxiv.org/html/2310.08505v1 ，正式出版 DOI https://doi.org/10.2140/memocs.2024.12.1
- Bobenko–Hoffmann–Sageman-Furnas 2025 正式论文: https://doi.org/10.1007/s10240-025-00159-z ，作者全文 https://arxiv.org/html/2110.06335v2


## 追加：Goursat / moulding / T-surfaces 的快速关键结论

已找到直接主文献：I. Izmestiev, A. Rasoulzadeh, J. Tervooren, *Isometric deformations of discrete and smooth T-surfaces*, Computational Geometry **122** (2024), 102104, DOI [10.1016/j.comgeo.2024.102104](https://doi.org/10.1016/j.comgeo.2024.102104)，[作者 arXiv 2302.08925](https://arxiv.org/abs/2302.08925)、[公式 HTML](https://arxiv.org/html/2302.08925v1)。这篇有精确有限形变公式，但没有闭嵌入曲面例子；其第5节把高度导数非零作为光滑双侧形变条件，明确说明高度局部极值会在单侧形变后产生折痕。

以下闭合障碍是本次独立推导，不是文献中的全局刚性定理。

### Moulding 曲面的平面闭曲线周期障碍

写
$$
X(u,v)=(\gamma(u)+f(v)n(u),z(v)),\quad
\gamma'=g(u)(-\sin\psi,\cos\psi),\quad n=(\cos\psi,\sin\psi),\quad g>0.
$$
直接计算得到
$$
I=(g+f\psi')^2du^2+(f'^2+z'^2)dv^2.
$$
令 $\lambda>0$，$f_\lambda=f/\lambda$、$\psi_\lambda=\lambda\psi$、$\gamma_\lambda'=g(-\sin(\lambda\psi),\cos(\lambda\psi))$，并令
$$
z_\lambda'^2=z'^2+(1-\lambda^{-2})f'^2,
$$
则局部严格等距。**但是不能凭此把任意闭合平面 $\gamma$ 弯成另一条闭曲线。** 若同一个周期 $L$ 对一个非退化连续 $\lambda$-区间都闭合，则
$$
H(\lambda)=\int_0^L g(u)e^{i\lambda\psi(u)}du=0
$$
在一个区间成立。因为 $\psi$ 在紧区间有界，$H$ 是整个函数；恒等定理推出 $H(0)=\int_0^Lg>0$ 也应为零，矛盾。更简单地，简单闭 $\gamma$ 的法向总转角 $\pm2\pi$ 被乘上 $\lambda$，首先已失去法向周期。因此这一**全局单张 moulding 公式族**不提供闭环面；它没有排除分片精确拼接或其他全局等距形变。

### 闭合高度剖面产生折痕，不是数值误差

对上述公式，若 $v$ 为周期且 $(f,z)$ 是正则闭剖面，则在非退化高度极值 $v_0$ 有 $z'(v_0)=0$、$f'(v_0)\ne0$。$\lambda<1$ 使根号负；$\lambda>1$ 使 $|z_\lambda'(v_0)|>0$。为保留原来的上升/下降两支，必须在 $v_0$ 改变符号，导致切向跳跃。若不改符号，则剖面失去原本的闭合转向。文献 Thm5.4 后的讨论正是这个局部折痕机制。它不能靠增加网格分辨率修好。

### Goursat seedpod 的准确文献

E. Couturier, *Folded Goursat surface and banana-shaped seedpod*, [arXiv:1604.05467](https://arxiv.org/abs/1604.05467)，期刊题目 *Folded isometric deformations and banana-shaped seedpod*, Proc. R. Soc. A **472** (2016), 20150760, DOI [10.1098/rspa.2015.0760](https://doi.org/10.1098/rspa.2015.0760)。这里通过沿坐标平面镜面对称引入 $\theta$-fold 和 $z$-fold；rest state 可光滑，不代表整个形变中光滑。无折痕子族的精确公式与直接周期化障碍见下一节。


### Goursat 精确公式及更直接的周期障碍（独立重写与验证）

令 $U=(U_1,U_2)$，$A=\det(U,U')$、$B=|U'|^2>0$、$r^2=|U|^2$。在无折痕正则区间取
$$
q_h=\sqrt{r^2+h}(\cos\theta_h,\sin\theta_h),\qquad
\theta_h'=\frac{\sqrt{A^2+hB}}{r^2+h}.
$$
令 $\Gamma_h'=U_3q_h'$ 及 $z_h'^2=V_2'^2-hV_1'^2$，则
$$
S_h(u,v)=(V_1(v)q_h(u)+\Gamma_h(u),z_h(v))
$$
严格保持
$$
E=(V_1+U_3)^2B,\quad
F=(V_1+U_3)V_1'\langle U,U'\rangle,\quad
G=V_1'^2r^2+V_2'^2.
$$
这是 Couturier 的局部 Goursat 族的等价重写；等距性可直接代数核验，因为 $|q_h|^2=r^2+h$、$|q_h'|^2=B$、$\langle q_h,q_h'\rangle=\langle U,U'\rangle$。这些公式适合精确曲面拼块，不能直接称闭曲面。

若把同一 $u$-区间的端点识别，并要求至少两个不同 $V_1$ 值上的 $S_h$ 都闭合，就必须同时有 $q_h(L)=q_h(0)$ 与 $\Gamma_h(L)=\Gamma_h(0)$。对无折痕的全局正号支，第一条件已要求
$$
\Theta(h)=\int_0^L\frac{\sqrt{A^2+hB}}{r^2+h}\,du\in2\pi\mathbb Z.
$$
$\Theta$ 在 $h>0$ 实解析且严格正，$h\to+\infty$ 时 $\Theta(h)\to0$。所以它不可能在任何非退化 $h$-区间恒等于固定的非零整数倍 $2\pi$；实解析恒等定理给出矛盾。全局负号支同理。改变根号符号在 $h>0$、$B>0$ 时只能产生切向跳跃，因为根号严格正；若 $B=0$，$S_u=0$ 又使该全局坐标正则性失效。**因此，直接把无折痕 Goursat 单张公式周期化，不能得到所需闭嵌入族。** 此结论只排除这个参数化方式；不排除不同块经移动刚体作精确 $C^2$ 拼接。

Couturier 文中的“rest state surface is closed”与“opens”是种荚壳的贴合／开口状态；不能理解为每个形变时刻都是固定无边界流形的嵌入。该文§3b自称闭合初态以定义体积，同时用 opening area 衡量后续张开，恰需区别这些概念。原始 arXiv PDF已核对，其§2.1给出上述公式，§2.4用分段符号引入fold，§3与图2讨论smooth-rest／folded-deformed。


## 对主会话新 ruled-strip 候选的直接计算（优先同步）

主会话提出 $X(s,\theta)=\gamma(\theta)+s d(\theta)$，$|d|=|d'|=1$，$\gamma'=c(d\times d')$，常数 $c\ne0$。以下验证说明它有很好的精确局部柔性，但**不能直接接上刚性帽片**。

令 $e=d'$、$n=d\times e$、$\kappa$ 为球面曲线 $d$ 的测地曲率，则
$$
d'=e,\quad e'=-d+\kappa n,\quad n'=-\kappa e.
$$
令 $\rho=\sqrt{s^2+c^2}$。曲面的单位法向取 $N=(s n-c e)/\rho$，直接计算
$$
I=ds^2+\rho^2d\theta^2,\qquad
II=-\frac{2c}{\rho}\,ds\,d\theta+\kappa\rho\,d\theta^2,
$$
所以 $K=-c^2/\rho^4$、$H=\kappa/(2\rho)$。$\kappa$ 是此局部族的弯曲自由度。

然而固定边界 $s=s_0$ 的空间曲线 $\beta=\gamma+s_0d$ 满足
$$
|\beta'|=\rho_0,\qquad
\beta''=-s_0d+\kappa\rho_0N,\qquad
k_\beta^2=\frac{s_0^2+\kappa^2\rho_0^2}{\rho_0^4}.
$$
若帽片是刚性的，则它的附着边界在族中必须与初始边界全等；按固定材料弧长参数，$k_\beta$ 固定，故 $|\kappa|$ 固定。连续路径不能在非零处改变 $\kappa$ 的符号，因此 $\kappa$ 本身固定，球面曲线基本定理迫使 $d$ 仅作刚体旋转，整个 ruled strip 也只作刚体运动。若允许边界材料作等速相位滑动，最多引入 $\theta\mapsto\theta+\phi(t)$，strip 的像仍全等。结论只针对这一具体常数 $c$、边界 $s=\mathrm{constant}$ 的族，未排除柔性帽片、非坐标边界或其他 ruled 模型。

因此该候选下一步应明确求出**同样可柔性变形、且接缝二阶 jet 精确匹配的帽片**，或者设计非坐标边界来避开上述曲率约束。仅解 $\oint d\times d'=0$ 可以闭合环带，但不会解决封帽。上面全为直接微分计算，可作独立解析检查。

## 闭球面曲线／常挠率曲线：可用作 ruled strip 的明确初值

L. M. Bates 与 O. M. Melko 的 [*On curves of constant torsion I*, arXiv:1206.7086](https://arxiv.org/abs/1206.7086)，正式发表 DOI [10.1007/s00022-013-0166-2](https://doi.org/10.1007/s00022-013-0166-2)，确实构造了处处正曲率、常非零挠率的闭合非结空间曲线。这提供主会话 ruled-strip 的位置闭合初值，未给闭曲面。

其 Koenigs–Darboux 构造是从球面曲线 B 作
$$
\gamma=\tau^{-1}\int B\times B'\,du.
$$
球面向量面积为零即使位置闭合。文中一个有限旋转公式为：令
$$
U=(1,1,1)/\sqrt3,\quad V=(-1,-1,2)/\sqrt6,\quad W=(1,-1,0)/\sqrt2,
\quad C=(U,V,W),
$$
令 $Q_U(\phi)$ 为绕 U 的 Rodrigues 旋转，$R_x,R_z$ 为标准坐标旋转，则
$$
B(u)=Q_U(mu)C R_z(\alpha)R_x(nu)R_z(\beta)e_1.
$$
取 $m=1,n=-3,\alpha=\pi/4$、
$$
\beta=\tfrac12\arccos\frac{67-24\sqrt2}{71},
$$
得到作者的闭合常挠率非结例子。三重对称把向量面积的三个分量化为同一个标量，其零条件可写成
$$
2\sin^2\alpha\cos^2\beta+(\cos^2\alpha-6\cos\alpha+1)\sin^2\beta=0.
$$

**下一步还须保持球面长度。** 只沿上述面积零曲线改变 $\alpha,\beta$，不能直接推出主会话的共同材料度量：归一为 $|d'|=1$ 后，周期长度 $L(B)$ 可能变化。应增加至少一个有限形状参数，并同时解“向量面积零＋球面长度固定”；三重对称下通常是两个标量约束。即便该射击成功，也仅给精确闭环带，前节刚性帽片障碍仍在。

## Monge 闭环面文献：闭合几何可复用，等距柔性没有随之成立

D. Brander 与 J. Gravesen，[ *Monge surfaces and planar geodesic foliations*, arXiv:1707.05109](https://arxiv.org/abs/1707.05109)，[作者机构版 PDF](https://orbit.dtu.dk/files/142989706/Monge_postprint.pdf)，给出很多真实闭 Monge 环面与 Klein 瓶浸入。该文的闭合判据包括旋转最小标架的总挠率为 $2\pi\mathbb Z$，以及位置的三个周期积分。**它研究的是闭曲面构造与平面测地线叶状结构，没有声称这些闭环面组成等距弯曲族。**

以下是可用于筛选的独立限制，范围仅限形变保持同一材料 Monge 网格。写
$$
X(u,v)=r(v)+x(u)q_1(v)+y(u)q_2(v),\qquad |(x',y')|=1,
$$
其中 $q_1,q_2$ 是旋转最小标架，
$$
X^*\delta=du^2+[\lambda(v)-\kappa_1(v)x(u)-\kappa_2(v)y(u)]^2dv^2.
$$
假设剖面 $p=(x,y)$ 是正则闭曲线，且全曲面正则。若 $\kappa(v)$ 的线性张成是二维，则固定度量中分离变量核的秩为二，任何保持同一网格的另一 Monge 表示必有 $p_t=A_t p_0+b_t$。因为剖面仍按同一材料弧长参数，$p_0'{}^T(A_t^TA_t-I)p_0'=0$。闭平面曲线的切线经过每一个无向方向，故 $A_t^TA_t=I$。这只改变标架规范与整体刚体位姿。

若 $\kappa(v)$ 只张成一维，则化为 $x_t=a_t x_0+b_t$。在闭剖面的 y 极值，$|x_0'|=1$，实数性迫 $|a_t|\le1$；若 $|a_t|<1$，则 $y_t'^2=1-a_t^2x_0'^2>0$ 处处，y_t 不可能周期。于是仍只能 $|a_t|=1$；连续族中的导数符号固定，仍为刚体。若 $\kappa\equiv0$，固定直轴平移不可能给正则闭 v 周期。这个限制不排除改变材料 Monge 网格的等距变形，也不覆盖该文中剖面不闭、靠圆形对称产生稠密平行曲线的所有商空间情形。

## 更强的平移曲面闭合限制（独立代数证明）

设 $F_i(u,v)=\alpha_i(u)+\beta_i(v)$，i=0,1，是同一材料双圆周期上的正则平移曲面，两个度量相同。则两曲面必全等。这里只断言**保持同一平移网格**的两族，不排除离开平移类别的弯曲；Nassar 的普遍无穷小扭转场通常正会离开此类别。

证明如下。若某一生成闭曲线是平面的，它的切线经过该平面的所有无向方向；另一闭曲线到此平面的高度在极值处有切线落入该平面，因此某对生成切线平行，违背曲面的处处正则。所以正则双周期情形的两条生成曲线之切向张成都为三维。

由交叉度量 $\alpha_1'(u)\cdot\beta_1'(v)=\alpha_0'(u)\cdot\beta_0'(v)$ 的秩三分解唯一性，存在固定可逆矩阵 A，使
$$
\alpha_1'=A\alpha_0',\qquad\beta_1'=A^{-T}\beta_0'.
$$
去掉 A 极分解的刚体部分，只须考虑正定对称 U。两个长度条件分别是
$$
a^T(U^2-I)a=0,\qquad b^T(U^{-2}-I)b=0.
$$
若 $S=U^2-I$ 半正定或半负定且非零，则 a 只在至多二维核中，矛盾。若 S 非退化不定，则其非零零锥分为两个连通分支，每个分支在某线性坐标上严格同号；连续正则闭曲线的 a 不能离开一个分支，于是该坐标严格单调，矛盾。剩下的非零可能是秩二不定 S，其零锥为两个平面之并，交线为 $\ker S$。a 为了张成三维必须从一平面切换到另一平面，故某处沿交线。$U^{-2}-I$ 也为秩二不定且具有同一个核；b 同样在某处沿此交线。这又给一对平行切线，违背正则。故 S=0，A 正交，积分后 F_1 只是 F_0 的欧氏等距。

## 不能靠双面等距“加厚”环带来自动封闭

对任一共同度量族 $F_t$，取单位法向 n_t 及固定材料函数 h>0，尝试两张平行面 $F_t^\pm=F_t\pm h n_t$。其度量为
$$
g_t^\pm=g\mp2hII_t+h^2III_t+dh^2.
$$
若这两张面也各自严格等距，则相减得 $g_t^--g_t^+=4hII_t$，故 II_t 固定。第一、第二基本形式同时固定，局部基本定理使 F_t 刚性；连通延拓后仍只能整体刚体。这个简单限制针对对称法向加厚，不能推广为所有柔性帽片不可能，但足以排除最自然的“复制—偏移—封边”方案。

## 既有 R7、R30–R35 端口核查：高亏格网络尚不能自动闭合

**结论性质：仓库结果的范围核查；不是对这些局部结果的独立数值重跑。** 本节只读 `topics/explicit-flexible-closed-surface` 对应结果文件与 HANDOFF，没有改变该课题。文件链接均指其原始结果；不能把局部 FULL PASS 扩大解释成已闭合、已嵌入的整体曲面。

| 结果 | 真正已给出的几何 | 可复用内容 | 本题仍缺什么 |
|---|---|---|---|
| [R7](../../explicit-flexible-closed-surface/results/R7-visible-continuous-embedded-annulus-family.md) | 有两个边界圆的精确连续嵌入环带；12 单元的全 SE(3) 单值性由两个有限射击约束获得 | 一套固定共同度量的有限 Fourier–ODE 曲面，以及严格的非全等量证书 | 旧证书为 δ/D > .022608，低于本题 .05；两条边界未封闭；未给本题 reach |
| [R30](../../explicit-flexible-closed-surface/results/R30-triple-pass-axis-return-annulus.md) | 三次转向的精确 T-strip，输入、输出两端真实圆柱口；12 块与旧 R8 拼成一个矩形环带 | 全刚体位姿回归、整边圆柱参数、参数转换 $t\mapsto 2t/(1-t)$ | 环带仍有两条边；无 δ 和 reach 的本题证书 |
| [R31](../../explicit-flexible-closed-surface/results/R31-double-contact-two-cylinder-corner.md) | 相邻两轴边为真实圆柱口的双接触 Moutard 角片 | 沿边的完整二阶 jet；$p=\kappa x^3,q=\kappa y^3$ 保证二阶贴合；与 R30 的参数转换一致 | 远侧边尚未回归成可直接配对的真实圆柱口 |
| R32、R33 | R31 的 T-strip 续接及真实外侧可展平台 | 可展口的具体法向和位置积分；R33 的实际速度不为零 | 外可展口通常不是圆柱口；没有新增闭合圆，也未形成闭 atlas |
| [R34](../../explicit-flexible-closed-surface/results/R34-controlled-four-port-mixed-curvature.md) | 两个内圆柱口、两个外可展口、四个平坦角；正负 Gauss 曲率片能沿内轴同参数精确 C² 拼合 | 四端口的真实位置微分及相同 $\tau$ 的反射配对；可以把混合曲率区域做大 | 四个外边尚未全部配对；不存在已证闭 atlas。四口不能都按圆柱口处理 |
| [R35](../../explicit-flexible-closed-surface/results/R35-large-turn-double-contact.md) | 基态转向可达 $135^\circ$ 的正则角片，$|\tau|\le .1$ 的窄域经固定斜投影证嵌入 | 处理大基态转向时避免速度退化的 source 控制；四个真实口和四个平坦角 | $135^\circ$ 是基态转向，不是族的形状振幅；输出口和下一片全 jet 匹配仍有工作稿成分，未闭合 |

其中 R7 的公式可直接作为新数值候选的环带核：
$$
e_0'=k e_1,\quad e_1'=-ke_0+\kappa e_2,\quad e_2'=-\kappa e_1,
\quad c'=kp(e_2-e_0)-q e_1,\quad Y=c+\sqrt2s e_0,
$$
$$
I=[p^2+(s-q)^2]dt^2-2p\,dt\,ds+2ds^2.
$$
只改变 $\kappa$ 而保持 k,p,q，度量完全固定。旧例取 $k=1/\sqrt2$、$\kappa=k+\alpha+\rho\cos(12t-\phi)$，$\rho\in[6,8]$。单胞旋转角固定为 $\pi/6$ 以及螺旋轴方向平移为零，是旧射击的两个标量约束。这比纯近似弹性形变强，但全部封口仍是独立问题。

### 为什么增加亏格不会自动消掉边界

给每个片编号 a，给定一个**固定材料**边界参数 $s\mapsto F_{a,t}(s,0)$。一条候选接缝至少须同时满足：

1. 存在与 t 无关的材料配对 $\phi_e$，及随 t 连续的刚体 $(Q_e(t),b_e(t))$，使两条真实边界全曲线重合。
2. 在选定跨缝材料坐标后，一阶与二阶 jet 完全一致。仅空间切线、法向或边界第一基本形式一致均不够；第二基本形式在跨缝法向方向的分量也须匹配。
3. 沿片的邻接图每一条基本回路，全部相对刚体乘积严格为 SE(3) 单位元。它必须对整个 t 区间成立，不能只在几个样本时刻为零。
4. 角点的材料邻域确实为圆盘，且总角为 $2\pi$，二阶 jet 存在；配对后的拓扑无剩余边界。
5. 配对后的不同片内部在空间不相交，并有统一的法向管状邻域。

边数都为偶数，只证明抽象配对有可能；它既不保证上述循环位姿，也不保证三维嵌入。提高亏格通常还会增加须关闭的基本回路。R34 的两条外侧平台上，真实 $H_x=A_x(p_*,q)$ 随 q 变；把它替换成固定平行母线的圆柱口会直接改变曲面，不能沿用原来的等距证明。

旧 HANDOFF 特别记录过一个六词非零斜率网络：全 SE(3) 回归已实现，但内部有 11 对片相交。其建议交叉切点
$$
u_*(t)=7-\frac{2(L_{-t}-L_t)}{h_B}
$$
依赖 t。因此沿这个位置切开再重配会改变材料分割，不能作为一个固定 M 上的等距族。这个失败不是任意亏格的普遍不可能性，却是“有局部端口＋闭位姿就能闭嵌入”的具体反例。

### 对本题尺度预算的含义

R31 原始横向尺度 .01，R34 使用 $\epsilon=10^{-4}$，R35 已证横向宽度约 .006；这些是局部存在／嵌入证书的范围，不是全曲面归一化 reach 的证明。不能仅把它们按比例放大：局部横宽与全曲面直径的比值在整体相似缩放下不变。也不能从“平台平坦”推出全局 reach 大，因为两片间距可能先成为法向单射半径的瓶颈。

主会话给出的两椭圆宏观模块（R=1、r=.3、$h^2=91/150$）若其独立相位确能由精确闭合柔性接头实现，则已有很有用的 δ 与局部曲率预算。当前文献与这些旧局部结果都没有提供那个接头的完整闭合证明。应保留其宏观形状，单独攻克端口问题，避免为接头引入相对 D 极细的颈部而损失 reach。


## 可把端口问题缩成边值问题的有限反射群方案

**性质：条件构造引理与后续研究路线；没有找到满足条件的非平凡柔性片。** 这比任意邻接图的逐口配对更容易检查全局位姿，但也更严格。

选有限欧氏反射群 W 的一个基本锥室 C，例如三坐标镜面生成的八分体。固定一张紧致材料片 P，要求其每条边都有固定的镜面标签 i。若精确等距族 F_t 满足下列条件，则取 W 的全部镜像可消除所有这些边界：

- 每条边始终落在其固定镜面中，片内部始终落在锥室内部。
- 边界的固定材料法向坐标 u 在 u=0 处满足 F_u 垂直镜面；在该坐标中还有反射相容的二阶 jet。
- 角点的曲面切平面与二阶 jet 对所在镜面稳定子相容；镜像后的材料邻域为圆盘，没有角亏。
- 各镜像内部互不相交；这在 F_t 的内部严格位于不同锥室、且边界仅按指定配对接触时可直接检查。

更精确地，把镜面平移到原点并记其线性反射为 R。镜像扩展定义为
$$
\widetilde F_t(u,v)=
\begin{cases}F_t(u,v),&u\ge0,\\ RF_t(-u,v),&u\le0.\end{cases}
$$
其 C² 条件恰是
$$
RF=F,\quad RF_v=F_v,\quad RF_u=-F_u,
\quad RF_{vv}=F_{vv},\quad RF_{uv}=-F_{uv},\quad RF_{uu}=F_{uu}
$$
在 u=0 成立。这里边界的切向两式由 RF=F 微分得到，混合项由 RF_u=-F_u 微分得到；最后一式须在同一跨缝坐标中检查。若已用沿曲面的测地法向坐标，正交相交的几何条件会给出所需反射二阶相容性。为避免坐标规范的歧义，实际证书仍应直接输出上列 jet。

有限群的全部群关系自动使片间刚体回路闭合；共同度量通过反射保持。每个镜像的等距性因此完全精确，不靠将折痕磨平。达到上述条件仍只给 C² 闭嵌入族的条件定理；非刚性、δ 与 reach 都须另证。

这条路线的限制很具体：有限欧氏等距群有固定点，因此可把所有反射镜面放成经过同一中心的线性镜面。两平行镜面会生成非零平移，产生无限群，不能直接用空间中的有限块闭合；不能把平移商得到的抽象三维环面误当 R³。对于三个镜面的有限 Coxeter 情形，夹角固定，随 t 改变其夹角也会破坏群关系。R34 已有的两个内侧镜像轴满足部分边界 jet，但外侧两个平台没有提供第三个固定镜面的对应边界。真正有价值的新问题是：在保持精确局部度量的自由函数中，能否同时求出“第三镜面边＋全程正交接触”的固定材料边界，而不把片做得相对全曲面直径极薄？

这为 Gauss–Codazzi 数值方案提供了清楚的边界条件：在边 i 上强制 n_i·F_t=0，材料单位余法向的空间像与 n_i 平行，并强制角点稳定子条件。可先取球面型拓扑验证闭合，再允许基本片自身带手柄或多边界以试高亏格；亏格不是这些边界条件的替代品。

## Connelly 1993 原始出处已核对

Robert Connelly，*Rigidity*，收于 *Handbook of Convex Geometry*，1993，Vol. A，pp. 223–271；作者的 May 1991 预印本可由 [UC Davis 托管原文](https://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Connelly/Connelly1.pdf) 读取。扫描 PDF 的内部页 9–11（§2.3 *Some Counter-Examples and Flexes*）明确区分：刚面多面体 flex、移动折痕 flex、C¹ Nash–Kuiper 柔性、C² 情形。内部页 11 说明当时作者不知道闭曲面留在 C² 范畴的非平凡 flex，甚至浸入情形也不知道。上下文是闭曲面；不能把这句话误写成“任何带边 C² 曲面都不能弯”。

这与 Connelly 1977 [IHÉS 原始论文](https://www.numdam.org/item/PMIHES_1977__47__333_0.pdf) 末页的开放问题相一致，也与 Ghomi 2019 问题清单相一致。Bricard 或 Connelly 多面体本身当然给出精确内在等距的连续机构，但其边与顶点是折痕／锥点。现有资料没有一个普适的“先精确 flex，再 C² 平滑且仍保持同一度量”的定理可用；仅得到小应变平滑壳不满足本题第 5 条。

## 更近的曲折痕与 pillow-box 文献的准确用途

Marcelo Dias、Levi Dudte、L. Mahadevan、Christian Santangelo，[*Geometric Mechanics of Curved Crease Origami*](https://arxiv.org/abs/1206.0461)，*Physical Review Letters* **109** (2012), 114301，DOI [10.1103/PhysRevLett.109.114301](https://doi.org/10.1103/PhysRevLett.109.114301)。该工作研究圆形折痕与周围可展环带，能产生宏观的三维几何响应。它的几何保持内在长度，但折痕两侧切平面不同，而且环带仍有边界。其有限折角不可以当作本题 C² 接缝。

Atsufumi Honda 与 Miyuki Koiso，[*Isometric deformations of pillow boxes*](https://arxiv.org/abs/2509.02049)，2025 年 9 月预印本。它把双矩形的 pillow-box 等距运动与折痕变化联系起来，适合提供闭折纸的拓扑／机构启发；文中允许折叠结构，未给出一族 C² 闭嵌入曲面。2026 年检索中出现的 flat origami tori 也属于分片仿射等距嵌入，不能因“torus”或“closed”字样而升级为 C² 结果。



## 一条可计算、但尚无解证书的闭曲面方案

**性质：研究方案，不是已经实现的构造。** 比起先猜能闭合的外形、再用弹性正则化压应变，更干净的未知量是固定全局度量 g 上的第二基本形式 $b_t$。它把“精确等距”放在解析方程中，而把闭合和嵌入留作明确约束。

1. 选取一个真正闭嵌入的光滑基态 $F_0$，固定 $g=F_0^*\delta$，并以其第二基本形式 $b_0$ 起步。若想保留主会话的椭圆模块，就把待求接头纳入一个有限 atlas；没有接头时不能先声称已有闭基态。
2. 在每张材料坐标图上求对称二阶张量 $b_t$，解 Gauss–Codazzi：
$$
\det(g^{-1}b_t)=K_g,\qquad \nabla_i(b_t)_{jk}=\nabla_j(b_t)_{ik}.
$$
Codazzi 在 b 中是线性的，Gauss 是二次的；这不同于只让离散三角形边长近似不变。
3. 用正交标架积分 Cartan 系统恢复 $F_t$。Gauss–Codazzi 只保证局部可积；在闭 M 上还需对每一个基本回路检查适配标架的旋转 holonomy 为 I，以及位置的平移 period 为 0。对亏格 g 的通常生成系，可对 2g 条回路直接施加 SE(3) 单值性；这些约束之间可能有关系，不要把数量误当作已知独立秩。
4. 固定一个点及该点的适配标架以消除刚体自由度，以弧长 continuation 跟踪非平凡解支。每次扩大参数区间同时做全部 period 与跨图二阶 jet 的检验。若离散核只有刚体场，不能仅靠改变 t 的标度宣称得到了 flex；若出现非平凡无穷小场，还要解二阶以及更高阶的可积条件。

在具有固定全局等温双周期坐标的环面上，令 $g=e^{2\omega}|dz|^2$，定义
$$
H=\tfrac12\operatorname{tr}_g b,\qquad
Q=\tfrac12(b_{uu}-b_{vv}-2i b_{uv}).
$$
系统可写成三个实方程
$$
H^2-e^{-4\omega}|Q|^2=K_g,
\qquad \partial_{\bar z}Q=e^{2\omega}\partial_z H.
$$
可在固定材料周期格上对 H 与复 Q 作 Fourier 配点，并额外积分两条基本回路的 SE(3) period。这个三未知量系统比直接对所有三维顶点优化更容易保留几何约束。它仍是无限维方程的数值近似；目前没有具体闭合非平凡解，也没有收敛／可逆性证书，不能作为完成标准第 5 条的现成保证。

建议将两个不同任务分开验证：先在已知 R7 或主会话 ruled strip 上恢复其解析 b_t，以检查实现的符号、Codazzi 与回路积分；然后才把同一代码应用于真实闭 atlas。前一个验证即使通过，也不会代替后一个存在性证明。

### 与幅度、reach 的可认证接口

对任何紧集，直径在 Hausdorff 距离下是 2-Lipschitz，且刚体不改变直径，故
$$
\min_{A\in E(3)}d_H(AF_t(M),F_0(M))
\ge \tfrac12\left|\operatorname{diam}F_t(M)-D\right|.
$$
因此若某时刻严格证出直径改变至少 .1D，就自动得到本题 δ≥.05D，无需在整个刚体群中做不可靠的局部配准最优化。反向不成立：直径不变的曲面仍可能有大 Hausdorff 变化。

reach 可用 Federer 的精确全局判据，而不是仅报告主曲率。Herbert Federer，*Curvature Measures*，*Transactions of the AMS* **93** (1959), pp. 418–491，Theorem 4.18，给出闭集的切锥判据；对本题的闭 C² 曲面化为
$$
\operatorname{reach}(S)^{-1}
=\sup_{p\ne q\in S}
\frac{2|\langle q-p,n(p)\rangle|}{|q-p|^2}.
$$
[原文 Theorem 4.18](https://static1.squarespace.com/static/5cb91b1c70468025fd21e98b/t/5d37d6d2e6603300016d83dc/1563940577696/federer-curvature-measures-transAMS-1959.pdf)。接近对角线的部分由曲率与高阶余项界处理，远离对角线的片对用区间包围盒细分界处理，再对 t 作区间细分。这提供了从一个解析／收敛数值解到全时刻 reach≥.03D 的具体检查路线。有限采样只能给该 supremum 的下界，即 reach 的上界；除非附上未采样区域误差界，不可把采样最小比值当成严格 reach 下界。

## 对“全由负曲率环带组成高亏格闭曲面”的额外限制

**独立初等证明。** 每一个紧 C² 浸入曲面在 $\mathbb R^3$ 中都至少有一个严格正 Gauss 曲率点，与亏格无关。取原点在像外，令 $|F|^2$ 在材料点 p 达到全局最大，$|F(p)|=R>0$。临界条件使 F(p) 垂直切平面。取 $n=F/R$，最大值的 Hessian 条件给出
$$
0\ge \tfrac12\operatorname{Hess}_M|F|^2=g+R b.
$$
故 b 的两个特征值均 ≤−1/R，K(p)≥1/R²>0。若第二基本形式采用相反号，两个特征值同时换号，K 结论不变。

所以主会话的 $K=-c^2/(s^2+c^2)^2$ 环带无论做多少圈或选多高亏格，不能只靠同类片在光滑接缝处拼成紧曲面；必须引入有正曲率区域的真正柔性帽片／角片。R34 的混合曲率模块至少满足这一必要方向，但其周期与嵌入问题仍需解决。

## 本次核查的可执行优先级

- **优先保留** R7／常挠率 ruled strip 的解析环带核，以及主会话已有宏观幅度和曲率预算；新的计算集中在柔性封口与真实端口 matching。
- **最具体的现有接头候选** 是 R31–R35 的 Moutard 混合曲率角片，其局部整边 jet 比一般“平滑铰链”完整。下一步须指定一个有限邻接图、每条固定材料配对、每个回路的 SE(3) 恒等式以及不相交域；目前无任何一组数据已满足这些要求。
- **不能直接升级** 全球单张 Goursat／moulding 公式、固定 Monge 网格闭管、固定平移网格双周期曲面、S³ Hopf tori、曲折痕壳或多面体平滑为本题答案；上文分别给出精确适用范围与障碍。
- 现检索到的原始文献并未给出满足本题两个无量纲阈值的 C² 闭嵌入等距族。这个检索结论不构成不存在定理，亦不替代对仓库 R520 的独立核查；该核查由主会话另行安排。


## 2025 年紧致 Bonnet 环面对：最新且重要，但仍不是连续 flex

Alexander I. Bobenko、Tim Hoffmann、Andrew O. Sageman-Furnas，[*Compact Bonnet pairs: isometric tori with the same curvatures*](https://doi.org/10.1007/s10240-025-00159-z)，*Publications Mathématiques de l’IHÉS* **142** (2025), 241–293；[arXiv:2110.06335v2 全文](https://arxiv.org/html/2110.06335v2)。已核对 §1.1、§2、§4.2–4.3 及 §9。这是值得主会话记录的较新进展：两张不全等、同度量同平均曲率的实解析紧环面**浸入**已存在。§9 Question 1 仍问是否可使两张都嵌入；结果没有给固定度量的连续闭 flex。

其 §4.2 的四元数微分公式为
$$
df^\pm=(\pm\epsilon-f)df^*(\pm\epsilon+f),
$$
f 为等温曲率线曲面，f* 为 Christoffel 对偶。由四元数范数的乘法性可直接算出
$$
g_\epsilon=(\epsilon^2+|f|^2)^2g_*.
$$
所以对于固定 f，改变实参数 ε 通常改变度量；只有 ±ε 配对自动等距。不能把公式里“每个 ε 都给一对”读成“所有 ε 属于同一等距族”。§4.3 还要分别消灭真实位置 period；局部微分闭合不足以得到环面。该文的精确 Gauss–Codazzi 约定也核对了上节 PDE：本笔记的 Q 是该文 Hopf 系数的两倍，故上节 Codazzi 右侧没有 1/2。

可复用之处是周期积分和几何保结构离散的思路；两个端点不能替代本题的整条 C² 嵌入路径。
