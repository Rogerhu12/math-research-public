# R521：有限正副本的全相位平均与完整第三历史下处处非退化的加速度控制

日期：2026-11-16。**新的从起点构造及原式纸证；没有执行 profile 求积、符号程序、秩计算、原根恢复、开发检查或科学任务。**

本文改变 R505–R515 所用的第一 profile 库，但不改变原几何、右锚恢复或完整第四 ruling。新库先支付三个二阶矩及全部第三 ruling，再用有限个真实、互不交、正幅的旋转与反射副本将整个第四相位合成一条 $\sin^2\theta$ 方程。它**保留**原 $Y$–third 项及全部真实第三累计，不采用会把这些项全部消掉的十矩／五块消元。

该方程的 $k_{ss}$ 系数有一个严格正的完整积分式。在从起点选定、满足 $h>0$、$x+\omega>0$、$h(x+\omega)-k>0$ 的任意合法紧几何域内，此系数一致远离零。因此可以对任意真实 $h_{ss}$ 控制直接解出 $k_{ss}$，连同原八矩和完整第三历史组成一套光滑有限维实际 ODE。这里无需在速度能量面上另找非零导数，亦无参考正割处的那个速度退化。

这是一个**全域非退化的完整 ruling 控制接口**。它尚未给出该 ODE 的周期轨道、完整 $M=0$、frame／位置返回、第三目标或第四 period。新库也不继承旧 R455/R480/R459 的十九／二十目标、十三规范及成本截面收据。

## 1. 原几何、固定锚和全部历史

全程采用同一个 profile 区间 $I=[\ell,r_*]$ 和右积分
$$
Jf(x)=\int_x^{r_*}f(y)\,dy.
$$
原实际几何及水平关系为
$$
\alpha_s=h^2T,\qquad
T_s=kN,\quad N_s=-kT-B,\quad B_s=N,\qquad
\omega_s=\frac{k_s}{2h}.
\tag{1}
$$
记
$$
z=x+\omega,\quad e=hz-k,\quad Q=1+e^2,\qquad
\gamma=h_s,\quad \upsilon=k_s.
\tag{2}
$$
在构造 profile 前固定一个合法紧几何域 $\mathcal D$ 及共同窗口，使
$$
h\ge h_*>0,\qquad z\ge z_*>0,\qquad e\ge e_*>0
\quad\text{在 }\mathcal D\times I.
\tag{3}
$$
这是从起点的共同窗口前提，不是把一个已冻结的任意窗口事后移走。对于预先给定的有限 $h,k,\omega$ 盒，可以在原允许的正支上共同选择足够靠右的 $x$ 窗口来满足(3)；若另有一个已经固定的物理窗口，则须直接核其(3)，不能据本稿自动授予。

两条第一 profiles 记为 $f,g$，并置
$$
\phi_\theta=f\cos\theta+g\sin\theta,\qquad
D_\theta=f\odot f-\phi_\theta\odot\phi_\theta.
\tag{4}
$$
$\odot$ 表示原对称二次输入，不先作普通乘积再误取导数。

本文固定第二规范 $w_\theta=0$，先固定第三规范 $\chi_\theta=0$。第8节另说明怎样一次加入一个允许的固定第三 Gram；没有沿路径或逐副本更换规范。

原第二累计必须满足
$$
\mathsf m_s=M_{\rm raw}(h,k,\omega,\gamma,\upsilon),
\qquad A_s=\Phi_{\mathsf m(s)}.
\tag{5}
$$
完整第三算子累计按 R73(17) 保留：
$$
\frac{d}{ds}\mathsf T_s(a;b,c)
=-\Phi_{M_{\rm raw}}\{a,\Phi_{\mathsf m}(b,c)\}
+\mathcal C_s(a;b,c).
\tag{6}
$$
$\mathcal C_s$ 是 R73(16) 的真实局部三次密度，包含变化-profile chain，局部 second 场的真 $s$ 导数，以及全部同锚原函数。它一般不为零，也没有被假设为全导数。

本文可从同一个原起点取 $\mathsf m=\mathsf T=0$。若使用非零入值，只能使用同一原恢复产生的、在本节有限原算子空间中的真实入值。不能为不同旋转副本分别指定一个第三 profile 常量。

R56 §6 给有限分离闭合：至第三阶，有限次 profile 微分、乘积、乘 $x$ 及同锚积分只产生一个固定有限生成空间；其几何系数保留真实 $s$ 积分。因此(6)可用一个固定有限向量 $\mathbf t$ 表示。允许该表示冗余，本文不宣称其维数或秩；真实初值及原递推保持所有算子关系，不把各块或各相位的第三系数释放为独立控制。**这里不取模 $W$，也不调用 R480 的全部第三 outer 矩为零。** 后面的状态必须保留 $\mathbf t$，不是直接沿用 R482 消掉第三历史后的十三维状态。

## 2. 一个完整、可旋转的二三阶基本块

### 2.1 四个原微包给准确三矩圆

取一个非零实 $u\in C_c^\infty$，在四个等距、互不交的位置放其字面平移 $u_0,u_1,u_2,u_3$。定义
$$
F_*=u_0+\sqrt3\,u_2,\qquad
G_*=\sqrt3\,u_1+u_3.
\tag{7}
$$
原三个矩为
$$
\boldsymbol\mu(v)=
\left(\int v''{}^2,\ \int xv''{}^2,\
\int\{x^2v''{}^2+2v'{}^2\}\right).
\tag{8}
$$
一个字面平移的各分量对其中心分别为零、一次、二次多项式；第三项保含原 $2v'{}^2$。故三阶有限差分权 $(1,-3,3,-1)$ 准确给
$$
\boldsymbol\mu(F_*)=\boldsymbol\mu(G_*),\qquad
\mathbf I(F_*,G_*)=0.
\tag{9}
$$
后一式由实际支撑分离逐项成立。两者非零且线性独立。

### 2.2 八个完整副本支付全部第三 ruling

在八个等距、互不交的完整包络内放置(7)，共同实幅度取
$$
a_j=(-1)^j\binom7j^{1/3},\qquad 0\le j\le7,
$$
$$
F=\sum_{j=0}^7a_jF_*(x-t_j),\qquad
G=\sum_{j=0}^7a_jG_*(x-t_j).
\tag{10}
$$
每一个(7)本来满足(9)，所以正的二次幅度权 $a_j^2$ 保留三矩圆。原 R46/R52 和 R183 §5 的**完整**第三 ruling 在整体搬回一个基本块后，对该块平移位置的次数至多六；其四条通道包括两个不同 second forcing，不能只保 pure 一条。原权 $a_j^3=(-1)^j\binom7j$ 使全部四条第三 ruling 精确为零。

这是原八副本消元的直接使用，不重新执行研究，也不把三次交替权误作二次矩闭合。后者已经逐(7)支付。

在(10)的整个包络外，原二阶 forcing 的三矩零使其 canonical second 场双 collar 为零。全部第三 ruling 零又由 R56(2)–(7)使完整第三场双 collar 为零：其真 characteristic 密度在外部为零，从同一零入值积分后仍为零。此为局部 $s$ 区间的真实恢复，不要求已付 $s$ 周期。

同一事实对 $(F,G)$ 的任意常数正交换基和任意共同实幅度成立。原四个三次通道已经同时为零，故换基后不需要再次选二阶规范。所有最细微包仍具有
$$
(F,G)|_{J_i}=(a_i,b_i)u_i
\tag{11}
$$
的固定方向形式。因此 R183 §§1–2 也给第三 hook 在这个第一平面上不可见；这不等于完整第三累计 $\mathsf T_s$ 已经消失。

把(10)称为一个**完整基本块**。其内部八组与四个微包的所有原尾、gap 和第三累计均保留。

## 3. 完整基本块之间的准确可加性与十次界

最终使用的完整基本块包络两两不交。每块自己的 $D_\theta$ 三矩为零，second 场支撑于该整块包络；第三 ruling 也已在每块内完整支付，故 third 场同样支撑于该整块包络。

因此不同完整块之间的原二阶和三阶 forcing 交叉为零；到第四阶，
$$
(dZ_\theta)^2+\mathcal S(Y_\theta,W_\theta)
$$
的跨块项也逐点为零。其完整 ruling 准确是各块 ruling 之和。这里依靠的是**整个下阶场在整块外为零**，不是把单个最细微包的右积分左尾删掉。

若将一个完整块共同平移 $t$，再搬回它的固定内部坐标，R56 原分子恢复给完整次数界
$$
\begin{array}{c|ccc}
& T\text{分量}&N\text{分量}&B\text{分量}\\ \hline
V_Y&0&-\infty&1\\
V_Z&4&3&5\\
V_W&8&7&9 .
\end{array}
\tag{12}
$$
这是 R505 §2 的原式证明：$P_s,B_s,\nabla_s$、变化-profile chain 和全部 $s$ 历史都保留；真实 $s$ 微分或积分不增加平移次数。同一右锚位于所有块的右零 collar，换元不重设任何常数。整块两 collar 为零，故对整个物理区间取 ruling 不增加移动端项。

于是，固定实际几何与其真实历史，对任意正交换基 $R$，
$$
t\longmapsto \mathscr K_{t,R}(s,\theta)
\quad\text{是次数至多十的真实多项式。}
\tag{13}
$$
这包括 second square、完整 $YC$、第三累计及其所有内部有序项。没有使用其 full-period pure 值或某个 natural flux 为零。

原 R56 的未加 $\chi$ 第四式对两个第一输入是齐次四次的。因此共同幅度 $\lambda$ 把(13)准确乘以 $\lambda^4$。

## 4. 正权、互不交的有限平移矩实现

以下小引理保证旋转平均不是一个不允许的重叠或有符号混合。

**正矩节点引理。** 给定一个开位置区间及有限整数 $q$，可为每个 $a=1,\dots,q$ 选择十一点
$t_{a,0},\dots,t_{a,10}$ 和严格正权 $w_{a,j}$，使全部 $11q$ 个点互异，且
$$
\sum_{j=0}^{10}w_{a,j}t_{a,j}^\nu
=\sum_{j=0}^{10}w_jc_j^\nu=:m_\nu,
\qquad 0\le\nu\le10,
\tag{14}
$$
其中 $c_j$ 是十一不同参考点、$w_j>0$。

证明：先固定这些参考点及正权。矩阵
$(c_j^\nu)_{0\le\nu,j\le10}$ 是可逆的 Vandermonde 矩阵。把每组十一节点作足够小的相互不同位移，对该组的权重解同一个十一阶线性系统，令其矩恰等于原 $m_\nu$。逆矩阵和所得权连续，故有限多组都可保权严格正。节点可以逐组选到全部互异；有限集合于是有严格正的最小距离。证毕。

在所有节点选定后，把(10)作一次共同正仿射缩窄，使它的整个包络小于这些节点之间的最小空隙，并留共同双 collar。三矩和完整第三 ruling 由原正仿射输运保留；位置多项式界(13)也保留。**先定节点和窗口，再一次选块宽度；不在已经冻结的库上移动某些包。**

每个实际块的共同幅度取
$$
\lambda_{a,j}=w_{a,j}^{1/4}>0.
\tag{15}
$$
于是(14)对任意原十次多项式都给相同的真实四次加权读出。参考点 $c_j$ 只用来表示共同矩；不同旋转块从未在实际物理空间重叠。

## 5. 有限 $O(2)$ 平均准确只剩 $\sin^2\theta$

取十六个正交矩阵组成的二面体群
$$
\mathcal G=\{R_{\alpha_j},\,R_{\alpha_j}S:
\alpha_j=j\pi/4,\ 0\le j\le7\},\qquad
S=\operatorname{diag}(1,-1).
\tag{16}
$$
对每个 $R\in\mathcal G$ 使用(14)的一组十一真实节点，把同一个完整块 $(F,G)$ 换基为 $R(F,G)$ 后按(15)安放。全部包络互不交。对整个最终圆再作一次共同正幅归一，即可令 $\int f''{}^2=\int g''{}^2=1$；下文暂把这个非零共同因子收入 $F,G$。

由可加性、(13)(14)，最终实际 ruling 满足
$$
\mathscr K_{\rm all}(s,\theta)
=\sum_{j=0}^{10}w_j\sum_{R\in\mathcal G}
\mathscr K_{c_j,R}(s,\theta).
\tag{17}
$$
右式是有限原多项式的准确表达，不是新定义一个同时重叠十六块的几何。

下面说明为何必须保反射。对一个块的两个输入，把任意二次槽写作 $X\in\operatorname{Sym}^2\mathbb R^2$。原 fourth 式可写为
$$
\mathscr K=B_s(D_\theta,D_\theta)+L_s(C_\theta,D_\theta),
\quad
C_\theta=v_\theta v_\theta^{\,t},\quad
D_\theta=e_1e_1^{\,t}-C_\theta,
\tag{18}
$$
其中 $v_\theta=(\cos\theta,\sin\theta)^t$，$B_s$ 对称，$L_s$ 只是一个双线性型。其系数包含真实 $A_s,\mathsf T_s$ 及当前二阶几何 jet。$L_s$ 没有被假定对称，也没有被置零。

$\mathcal G$ 对二次槽的作用为 $X\mapsto RXR^t$。因为原式对第一 inputs 是四次的，八个旋转恰好积分掉关于 $\alpha$ 的非零 Fourier 次数 $\pm2,\pm4$。再加反射后，平均双线性型准确具有
$$
\overline B(X,Y)=b_0\operatorname{tr}X\,\operatorname{tr}Y+
b_1\operatorname{tr}(XY),
$$
$$
\overline L(X,Y)=l_0\operatorname{tr}X\,\operatorname{tr}Y+
l_1\operatorname{tr}(XY).
\tag{19}
$$
也可在 traceless 平面的两个坐标 $(X_{11}-X_{22},2X_{12})$ 逐项核验：旋转平均只剩标量矩阵和一个反对称矩阵，反射恰杀后者。只取 $SO(2)$ 平均时不能跳过这一步，原反对称型可能留下 $\sin\theta\cos\theta$。

现在
$$
\operatorname{tr}D_\theta=0,\quad
\operatorname{tr}(D_\theta^2)=2\sin^2\theta,\quad
\operatorname{tr}(C_\theta D_\theta)=-\sin^2\theta.
$$
故(17)准确给
$$
\boxed{\mathscr K_{\rm all}(s,\theta)
=\sin^2\theta\,
\{\mathcal F(S,\gamma,\upsilon,\mathsf m,\mathbf t)
+C_h(S)h_{ss}+C_k(S)k_{ss}\}.}
\tag{20}
$$
这里 $\mathcal F$ 是原完整值的无加速度部分，不是 principal approximation。$YC$ 和全部 $\mathsf T_s$ 一般仍非零，都进入同一个 $\mathcal F$。

## 6. 原 $k_{ss}$ 行的完整单包身份

本节暂取一个非零真紧微包 $u$，记
$$
p=u',\quad r=u'',\quad t=u''',\quad
F=Qr-2hep+2h^2u,\qquad F'=Qt.
\tag{21}
$$
$t$ 在本节是导数记号，不是第3–5节的平移参数。

R482(29)(30)由原 R221 second 局部恢复给
$$
a_k[u^2]=\frac{Qr^2+2hJ(er^2)}{32h^2},
\qquad
a_k'=\frac{Qrt}{16h^2},
\tag{22}
$$
$$
a_h'=\frac{Q(p-zr)t}{8h^2}.
\tag{23}
$$
左侧的 $a_k$ 一般有非零常尾；本文完整保留它。

原 R482 **未消第三历史的(24)**，或直接 R56 的 forcing
$-2H(Y_\phi,K_s(D))$，给加速度系数
$$
\mathcal C_k(\phi,D)
=-\frac1{4h^4}\int F_\phi Q\phi'''a_k[D].
\tag{24}
$$
其来源只涉及当前 second 局部场的 $s$ 导数，不需要 R480 的 $W$ outer 零。原第三历史作为一个当前状态值进入(24)之外的完整 ruling；其演化仍按(6)，不能把它删掉。

具体地，某个加速度对 $\partial_s\eta_D$ 的系数为 $a$ 时，原分子为 $(a/h,0,ea/h)$，R56 恢复给
$$
\eta_{-,{\rm acc}}=\frac1{4h^2}J(Q\phi'''a).
$$
紧 outer 的真实配对即为(24)。这个推导也说明没有遗漏来自 $P_s,B_s$ 的加速度或另造一个 $k_s,\omega_s$ 独立方向。

取同包 $\phi=u,D=u^2$，逐次分部积分得
$$
\begin{aligned}
c_k(u)
&=-\frac1{4h^4}\int FF'a_k\\
&=\frac1{8h^4}\int F^2a_k'
=\frac1{128h^6}\int F^2Qr\,t\\
&=-\frac1{384h^6}\int tF^3\\
&=\boxed{-\frac1{768h^5}
\int\frac{eF^4}{Q^2}.}
\end{aligned}
\tag{25}
$$
第二次使用 $(F^3)'=3F^2Qt$，最后使用
$$
\int tF^3=\frac14\int\frac{(F^4)'}Q
=\frac14\int\frac{Q'F^4}{Q^2}
=\frac h2\int\frac{eF^4}{Q^2}.
$$
全部边界由真紧 $u$ 使 $F$ 两端为零而消；并未假定 $a_k$ 左紧。

若 $F\equiv0$，则 $F'=Qt$、$Q>0$ 给 $u'''\equiv0$，再用真紧性得 $u=0$，矛盾。因此在(3)上
$$
\boxed{c_k(u)<0.}
\tag{26}
$$

为同时固定另一行的完整规范，同样的 IBP 给
$$
\boxed{
c_h(u)=-\frac1{768h^6}
\int\frac{(1-e^2-2ke)F^4}{Q^2}.
}
\tag{27}
$$
这里用 $(p-zr)'=-zt$ 及
$(z/Q)'=(1-e^2-2ke)/Q^2$。本稿不需要宣称(27)固定符号。

对不同微包，$a_h[u_j^2]$、$a_k[u_j^2]$ 在其左方只是真常数，右方为零。故所有 cross 加速度项都含
$$
\int F_iQu_i'''=\int F_iF_i'=0.
\tag{28}
$$
这准确支付完整微包分解；没有只取 diagonal 后遗漏原右包尾。

## 7. 有限旋转后 $C_k$ 严格正，且全紧域统一

在完整基本块(11)内记
$$
\rho_i^2=a_i^2+b_i^2>0.
$$
对任意微包系数向量，十六正交变换的准确四次平均为
$$
\frac1{|\mathcal G|}\sum_{R\in\mathcal G}
c_{i,R}(\theta)^2d_{i,R}(\theta)
=-\frac{\rho_i^4}{4}\sin^2\theta.
\tag{29}
$$
这里 $c_{i,R}$ 是该旋转后的 $\phi_\theta$ 系数，
$d_{i,R}$ 是其 seed 平方减 $\phi_\theta$ 平方。直接积分
$\cos^2(\alpha+\theta)\{\cos^2\alpha-\cos^2(\alpha+\theta)\}$
即得(29)，有限群对这些四次项准确。

由(14)(24)(28)(29)，(20)的真实系数为
$$
\boxed{
C_k(S)=
\frac{|\mathcal G|}{3072h^5}
\sum_{j=0}^{10}w_j
\sum_i\rho_i^4
\int\frac{eF_{i,j}^4}{Q^2}
>0,
}
\tag{30}
$$
其中 $F_{i,j}$ 取参考位置 $c_j$ 的完整微包。它们是(17)的共同多项式读出；对应的实际库仍在全部不同 $t_{R,j}$ 上。加速度原式对平移至多六次，故已付的0…10矩当然足够。所有参考微包也从起点置于(3)的共同窗口内。

若最后整体归一第一圆，(30)只再乘该共同正幅的四次幂，严格号不变。全部权重、宽度、微包、窗口均已固定。$C_k$ 对 $S$ 连续，而每个 $S\in\mathcal D$ 都严格正，因此
$$
\boxed{\inf_{S\in\mathcal D} C_k(S)=c_*>0.}
\tag{31}
$$
这是一个真实紧性下界，不是浮点最小值或一个未核 minor。

(30)不依赖 $\mathsf m,\mathbf t,\gamma,\upsilon$。因此第三历史变大或当前速度经过参考正割值，都不会使这个 $k_{ss}$ 系数退化。

## 8. 同一固定规范下的完整实际反馈系统

取任意预定光滑真实控制 $a(s)=h_{ss}$。由(20)(31)定义
$$
b(s)=k_{ss}
=-\frac{\mathcal F(S,\gamma,\upsilon,\mathsf m,\mathbf t)
+C_h(S)a(s)}{C_k(S)}.
\tag{32}
$$
若一次选择非零固定第三 Gram，也可用 R47/R56 的同一个合法右逆令
$\mathbf I(\phi_\theta,\chi_\theta)=\sin^2\theta\,\nu$，
其中 $\nu\in\mathbb R^3$ 一次固定。此时仅把(32)的分子再减去
$2\mathbf w(S)\cdot\nu$，其中
$$
\mathbf w(S)=
\left(\frac{1+(h\omega-k)^2}{4h},
\frac{h\omega-k}{2},\frac h4\right).
$$
整条路径使用同一个 $\chi_\theta$。本文的存在结论已可取 $\nu=0,\chi=0$，不依赖额外 Gram 自由度。

实际系统为
$$
\boxed{
\begin{aligned}
h_s&=\gamma,& k_s&=\upsilon,&
\omega_s&=\upsilon/(2h),\\
\gamma_s&=a,&\upsilon_s&=b,\\
\mathsf m_s&=M_{\rm raw}(S,\gamma,\upsilon),&
\mathbf t_s&=\mathbf C_{\rm orig}
(S,\gamma,\upsilon,\mathsf m,a,b).
\end{aligned}}
\tag{33}
$$
$\mathbf C_{\rm orig}$ 是(6)在固定有限原算子生成空间中的完整系数式。它保 $-\Phi_M\circ\Phi_m$ 与 $\mathcal C_s$；局部 second 场对 $s$ 求导只使它对 $(a,b)$ 仿射。因此把(32)代入后，(33)是一套通常的光滑有限维 ODE，没有未解的更高导数或独立第三控制。

从一个真实初始状态出发，普通局部存在唯一性给正长度实际路径。再按(1)恢复原 frame 和中心线。二阶三矩、第三四通道与(20)(32)在整个局部区间同时成立，故 R56 原恢复给二、三、四阶真正双 collar 场；它们的周期条件仍须另付。

更强的是，对上述同一原有限递推的真实历史状态，(32)在整个(3)域中是一个显式光滑图，而非仅在某个入口点成立的 IFT 分支。只要某条实际解在有限时间内保持合法紧几何域、有限速度和有限真实历史，且控制保持光滑有界，就可按普通 ODE 延拓。不能把这一条件延拓说成“所有控制都不会爆破”或“已经存在周期轨道”。

这使原完整 $K=0$ 约束不再限制为一个固定速度能量面。在同一新圆和同一规范上，$h_{ss}$ 是真实自由控制，$k_{ss}$ 由完整方程连续决定，且其求解分母在全域不退化。它给有限幅值长程路径问题一个不同于 R505–R515 的实际控制系统。

## 9. 该新入口能用在哪里，哪些闭合尚未完成

本文严格支付：

1. 有限真实三矩圆、完整八副本第三 ruling，及一个可在共同窗口安放的有限正旋转库；
2. 全部 fourth $YC$、second square、真实有序尾与完整第三历史参与的准确有限 $O(2)$ 平均；
3. 同一整个圆的完整 $k_{ss}$ 系数(30)严格正，并在预定合法紧域统一；
4. 同一固定规范下以原二阶、三阶 history 演化的真实反馈系统(33)。

这些结论不需要先制造一条有符号负路径，也没有把相同位置的虚拟平均当成实际重叠字段。实际幅度全为实数，最终四次权全部严格正。

仍欠的是(33)中一条满足原全部端点要求的实际轨道：完整 $M=0$、scalar/frame/位置返回、第三目标、第四整个 period 和同一个十三规范。不能在中途重置 $\mathsf m$ 或 $\mathbf t$，不能用原 R70 无约束桥替代其内部 ruling，也不能只令两个 $h,k$ 端值相等就称全词闭合。实际 prototype、倒行、Klein 及其第四成本若以后使用，必须在同一个整词中保账。

本文也没有让新库同时满足旧 R455/R480/R459 的 cap、十九／二十目标、全外第三矩及相应实际成本截面。要联合这些条件，需在本稿**同一个**新旋转库上再证明相容性，不能拼接两份分别存在的母库。

即使后续完整第四词闭合，真正有限等距族、嵌入、厚度、宏观幅度与固定数值曲面的主门仍是后继问题。本稿新增的是一个已完整定义、无加速度退化的实际非 secant 路径控制机制。

### 原来源及独立窄核

- R56(2)–(8)、§6：同一右锚、双 collar、完整局部恢复及有限分离；
- R73(12)(16)(17)：原八矩与完整第三累计，含变化-profile chain；
- R46/R52、R183 §5：完整基本块的二阶三矩与八副本第三四通道；
- R505 §§2–3：包括所有真实历史的十次位置界与原尾范围；
- R482 未消历史的(24)、(29)–(33)：原单位加速度系数；本文不使用其 $W$ 外矩消去结论；
- R47/R56 §8：仅用于可选的一次固定第三 Gram。

tail_cost 仅独立纸核了(25)的全部分部积分、号、$768$ 因子和边界范围。有限正节点、完整正交复制、第三历史状态及反馈系统由本文显示证明负责；没有把该窄核扩大为其它新范围。
