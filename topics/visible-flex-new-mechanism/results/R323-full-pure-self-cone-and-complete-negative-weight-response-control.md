# R323：pure 与完整 universal self 的联合闭锥、负权完整响应及真实十坐标控制

日期：2026-11-15。**完整纸面证明；没有执行新的原式程序、求积、秩计算、人工检查或科学运行。** 本文读取已经发表的原式，手写有限微分、同右锚分部积分和八列的准确消元。mechanism 独立手核第 4 节的全部八列、真实尾项和消元。

本文从 [R316](R316-complete-weight-zero-self-membership-and-positive-character-representative.md) 的新真实代表出发，证明：
\[
\boxed{\overline{\operatorname{cone}\{(\pi V_B,\mathcal Q V_B):
M_B=\mathbf T_B=0\}}=(\pi,\mathcal Q)(U).}
\]
这里 \(\mathcal Q V\) 保留对**所有**实紧 profiles 的完整 self 函数。这个结论不是只对一个母包、有限中心或 principal 成立。

证明的新增原式部分是：权 \(-6\) 的两个完整 self 坐标、权 \(-4\) 的八个完整 self 坐标，均由明确的 pure-zero 真实响应覆盖。后八列保留 \(\mu _0^2/2\) 的非局部尾；不是用主符号秩代替整个 self。它们还给 whole pure 与这十个普适低权坐标的真实有限同时支付。

**联合闭锥满尚不等于整个联合实际半群已满。** 第 8 节把 R206 精确有限实现所欠的零权接口缩到 \(C_4,C_6\) 两个既有完整成本。完整 mixed 的两张实际目标函数及同一 gauge 下的 ruling 也仍未支付。

主要来源：[R127](R127-positive-affine-character-of-the-fourth-cost-cone.md)、[R145](R145-true-curvature-reflection-and-even-positive-characters.md)、[R159](R159-balanced-mixed-faithfulness-after-pure-cancellation.md)、[R188](R188-no-nonzero-positive-affine-character-at-weight-minus2.md)、[R190](R190-complete-weight-plus2-quotient-vanishes-and-remaining-even-weights.md)、[R196](R196-complete-weight-zero-character-head-positive-ray-and-strict-canonical-cost.md)、[R203](R203-general-pure-lowest-two-weights-vanish.md)、[R207](R207-complete-weight-minus6-pure-image-equals-three-dimensional-response.md)、[R210](R210-complete-weight-minus4-pure-image-and-finite-pure-closure.md)、[R222](R222-simultaneous-real-pure-and-eight-flux-control.md)、[R255](R255-explicit-third-diagonal-kernel-and-complete-hook-response-formula.md)、[R261](R261-eight-local-self-adjoint-hook-operators-and-full-third-kernel.md)、[R302](R302-regular-chi-prototypes-shared-reversal-and-enhanced-Morse-control.md)、[R303](R303-complete-self-degree-nine-and-all-translation-control.md)、[R313](R313-complete-five-dimensional-J-self-module-and-fifteen-dimensional-image.md)、[R314](R314-ordered-matrix-defect-localization-and-faithful-Euler-self-coordinates.md)、R316、[R322](R322-full-self-scaling-shift-and-exact-reduction-to-the-matching-response-weight.md)。

## 1. 原空间、新代表及完整 self 的准确含义

沿用真实完整 canonical 成本空间 \(U\)、完整响应空间 \(\mathcal R\) 和 universal pure 投影 \(\pi\)。记
\[
U_{\rm p0}=U\cap\ker\pi,\qquad
\mathcal R_{\rm p0}=\mathcal R\cap\ker\pi.
\]
粗体 \(\mathbf T_B\) 表示第三算子；\(\mathsf T(V)\) 表示 R297 的有序三矩矩阵，二者不混用。

对每个共同双 collar 内的实紧 profile \(u\)，采用原查询
\[
\mathfrak q_u(V)=\frac14[x^2]_{\rm left}V(u\odot u,0),
\qquad
\mathcal Q(V):u\longmapsto\mathfrak q_u(V).
\tag{1}
\]
所有原函数使用同一真实右锚。式 (1) 在整个 \(U\) 上是线性映射；它的目标是有限维实际函数像，而不是任意四次泛函的空间。

R316 的公开实际已经证明
\[
\begin{aligned}
H_*={}&C_2+\frac{649}{768}R_2-\frac{73}{3072}R_3
+\frac{649}{1536}R_4-\frac{821}{768}R_5\\
&+\frac1{64}R_7+\frac{187}{1024}R_9,
\end{aligned}
\tag{2}
\]
\[
\boxed{\pi H_*=0,\qquad \mathcal Q(H_*)=0,\qquad
\lambda_+(H_*)=1.}
\tag{3}
\]
式 (2) 的 \(R_j\) **全部采用 R126 的 old 原列号**，不是十六列压缩下标。本文直接使用该公开完整原差结果，不恢复这些根、不重跑十三比较列、也不重算已付秩七。

定义联合投影及其实际像
\[
E=(\pi,\mathcal Q):U\longrightarrow\mathscr P:=E(U).
\tag{4}
\]
式 (3) 表明完整正字符 \(\lambda_+\) 不能经 \(E\) 下降。它没有说明 \(H_*\) 已由一条实际路径实现，也没有说明其完整 mixed 函数为零。

## 2. self 权移及三个负权的有限完整上界

### 2.1 分级必须包含积分与左二次系数的权移

R322 已证明真实正缩放满足
\[
\mathfrak q_u(\mathsf P_{H,0}V)
=H^2\mathfrak q_{C_Hu}(V),\qquad
(C_Hu)(x)=u(x/H).
\tag{5}
\]
因此对 \(V\in U_\sigma\)，
\[
\mathfrak q_{C_Hu}(V)=H^{\sigma-2}\mathfrak q_u(V).
\tag{6}
\]
缩放比较只须在使全部支撑和共同 collars 合法的 \(H=1\) 附近开区间进行。有限 Laurent 身份随后是 universal 身份；不需要把实际支撑送到无穷远。

R314 给 \(V\in U_{\rm p0}\) 的完整表示
\[
\mathfrak q_u(V)=
\mathcal N_{\mathsf T(V)}(u)+\int L_V(x,u,u',u'',u''')\,dx,
\tag{7}
\]
其中
\[
\mathcal N_A(u)=\int_{x<y}j_u(x)^{\mathsf T}A\,j_u(y)\,dx\,dy,
\quad
j_u=(r^2,xr^2,x^2r^2+2v^2)^{\mathsf T},
\tag{8}
\]
并记 \(v=u',r=u'',s=u'''\)。密度是系数关于 \(x\) 为多项式的四次 jet 多项式；保留 \(s^2\) 后，其余项可取 jet 不超过二。这里已经包括 R314 逐生成成本延拓、真实左端常数和双重积分正规化，不能仅凭抽象加性使用该表示。

有序矩阵坐标 \(\mathsf T_{ij}\) 的成本真权为 \(i+j-4\)，\(0\leq i,j\leq2\)。一个局部单项
\[
\int x^a\prod_{\ell=1}^4u^{(j_\ell)}\,dx
\]
在 \(C_H\) 下的权为 \(a+1-\sum j_\ell\)。因此对成本权 \(\sigma\)，准确条件是
\[
\boxed{a=\sum j_\ell+\sigma-3,\qquad a\geq0.}
\tag{9}
\]
这里减三同时包含输出左二次系数和积分权，不能直接用成本权代替 self 权。

若 (7) 初选的密度尚未同权，取其中满足 (9) 的部分即可：其余有限权由 (6) 在开 \(H\) 区间的独立性给零泛函。这一操作只选择已有有限多项式的同权部分，不删真实端项或把不完备正规式当成函数独立。

### 2.2 权 \(-8\) 全 self 为零

在局部式 (7) 中，最多含两个三阶 jet，另两个 jet 至多二阶，所以总 jet 次数至多十。权 \(-8\) 的 (9) 要求 \(a=\sum j_\ell-11\geq0\)，不可能。该权也没有任何 \(\mathsf T_{ij}\)。故
\[
\boxed{\mathcal Q(U_{\rm p0}^{(-8)})=0.}
\tag{10}
\]
R203 已证明 \(\pi U_{-8}=0\)，所以此处实际上
\[
E(U_{-8})=0.
\tag{11}
\]

### 2.3 权 \(-6\) 至多两个完整局部量

权 \(-6\) 要求总 jet 次数至少九。无矩阵项，jet 至多二的密度也不可能贡献。唯一两个类型为
\[
J_0(u)=\int vr s^2,\qquad I_1(u)=\int xr^2s^2.
\tag{12}
\]
因此
\[
\boxed{\mathcal Q(U_{\rm p0}^{(-6)})
\subseteq\operatorname{span}\{J_0,I_1\}.}
\tag{13}
\]
这包括完整 self，而不止最高 jet 主项。

### 2.4 权 \(-4\) 的八个完整坐标

此权只有矩阵项 \(\mathsf T_{00}\)。其真实非局部项为
\[
Z(u)=\mathcal N_{e_{00}}(u)
=\frac12\left(\int r^2\right)^2.
\tag{14}
\]
不把它当作零或局部密度。

局部部分的 (9) 给五个 \(s^2\) 项和两个 jet 二项：
\[
\begin{array}{lll}
A=\int uv s^2,&B=\int xu r s^2,&C=\int xv^2s^2,\\
D=\int x^2vr s^2,&F_3=\int x^3r^2s^2,&\\
F=\int vr^3,&G=\int xr^4.&
\end{array}
\tag{15}
\]
下文 \(F_3\) 是第三矩型，不是种子 \(f^2\) 或成本投影 \(E\)。准确上界是
\[
\boxed{\mathcal Q(U_{\rm p0}^{(-4)})
\subseteq
\operatorname{span}\{A,B,C,D,F_3,F,G,Z\}.}
\tag{16}
\]

这八个真实泛函独立。先在两个严格分离的非零实包上比较混合幅度：局部积分可加，而 \(Z\) 的交叉项为两个严格正 \(\int r^2\) 的乘积，故一个零关系中的 \(Z\) 系数为零。余关系取 Euler 导数；最高 \(u^{(6)}\) 系数是
\[
-2(a\,uv+b\,xu r+c\,xv^2+d\,x^2vr+e\,x^3r^2),
\]
所以五个系数全零。最后 \(fF+gG\) 的 Euler 最高 \(u^{(4)}\) 系数为
\[
6f\,vr+12g\,xr^2,
\]
再迫 \(f=g=0\)。紧支扰动可在允许开区间内任取 jet，以上比较是局部多项式身份。

## 3. 权 \(-6\) 的两个真实响应已经覆盖整个 self 像

R313 给真实 \(\mathfrak J\in Z_{71}\) 及完整原式
\[
\pi\mathcal B_P(\mathfrak J)=0,\quad
\mathsf T(\mathcal B_P(\mathfrak J))=0,\quad
\mathcal Q(\mathcal B_P(\mathfrak J))=2J_0.
\tag{17}
\]
它的成本真权是 \(-6\)。

再取 R303 的
\[
\mathcal K_{\rm top}=\mathcal B_{p_2}(\mathfrak H_6),\qquad
G_l=-\frac{N^{9-l}\mathcal K_{\rm top}}{1080\cdot9!}.
\tag{18}
\]
已有完整身份
\[
\pi G_l=\mathsf T(G_l)=0,\qquad
NG_1=G_0,\qquad
\mathcal Q(G_0)=I_0:=\int r^2s^2.
\tag{19}
\]
真权给 \(G_1\in\mathcal R_{\rm p0}^{(-6)}\)。由 (13)，写
\(\mathcal Q(G_1)=aI_1+bJ_0\)。同锚平移下
\[
I_1(u_c)=I_1(u)+cI_0(u),\qquad J_0(u_c)=J_0(u).
\]
用 (19) 得 \(a=1\)。这里不必新求 \(b\) 的值；\(\mathcal Q(G_1)\) 与 (17) 已独立并张满 (13)。\(J_0\) 真非零的紧母包存在已由 R310 的原 Euler 证明支付，\(I_0(u)>0\) 对每个非零实紧 \(u\) 成立。

因此
\[
\boxed{\mathcal Q(U_{\rm p0}^{(-6)})
=\mathcal Q(\mathcal R_{\rm p0}^{(-6)})
=\operatorname{span}\{J_0,I_1\}.}
\tag{20}
\]
这不是再次评价 R303 的十列或 R313 的五列。

## 4. 权 \(-4\) 的八条完整原式

### 4.1 来源、右尾与完整 self 公式

采用 R255 的原二次方向
\[
P=\Phi_{r_0},\quad R=\Phi_{r_1},\quad S=\Phi_{s_0},
\quad L=\Phi_{p_0},\quad U_1=\Phi_{s_1},
\quad V_1=\Phi_{p_1},\quad T_1=\Phi_{t_1}.
\tag{21}
\]
为免与空间 \(U\)、完整成本 \(V\) 混淆，这里将二次方向原 \(U,V,T\) 添下标 1。正右积分记
\[
J_0(x)=\int_x^{r_*}r(y)^2dy,\qquad
J_1(x)=\int_x^{r_*}y r(y)^2dy.
\]
它们是同一个真实 \(u\) 的尾，不是独立参数。

R258/R261/R297 给任意完整第三对角核 \(\tau\in Z\) 的完整 self：
\[
\boxed{\mathfrak q_u(\mathcal B_E\tau)
=-\frac14\int c_{\tau,u}\,\Phi_E(u,u).}
\tag{22}
\]
该式包括真实三次右积分常数与 Green 端项。本文只用它已经证明的完整函数范围。

R313 与 R261 的已发系数准确给
\[
c_{\mathfrak J}=4D_x^3(vr)-2D_x^2(r^2),\qquad
c_{30}=\frac3{512}D_x^3(r^2),
\tag{23}
\]
\[
256c_{32}=-3D_x^3(xr^2)-2D_x^2(vs),
\tag{24}
\]
\[
256c_{37}
=D_x^2\{16xr^2+36x^2rs-16xvs-8vr\}.
\tag{25}
\]
(24)–(25) 可直接逐项微分回 R261 的显示系数；它们保全部项，未调用新程序。

使用 (22)，同锚分部积分给以下四个统一原式：
\[
\begin{aligned}
\mathfrak q_u(\mathcal B_E\mathfrak J)
&=-\int(vs+r^2/2)\Phi_E(u,u)'',\\
-\frac{1024}{3}\mathfrak q_u(\mathcal B_E\chi_{30})
&=\int rs\,\Phi_E(u,u)'',\\
1024\mathfrak q_u(\mathcal B_E\chi_{32})
&=\int\{3r^2+(6xr+2v)s\}\Phi_E(u,u)'',\\
1024\mathfrak q_u(\mathcal B_E\chi_{37})
&=-\int\{16xr^2-8vr+(36x^2r-16xv)s\}\Phi_E(u,u)'' .
\end{aligned}
\tag{26}
\]
积分中含 \(u,v,r,s\) 的转移因子全在真双 collar 为零；\(\Phi_E(u,u)\) 的左尾却不设为零，下一步保留它。

原二导为
\[
\begin{aligned}
\Phi_L(u,u)''&=(u-xv)s-\tfrac12(xr^2+J_0),\\
\Phi_{U_1}(u,u)''&=(2xv-3x^2r)s+2vr-2xr^2,\\
\Phi_{V_1}(u,u)''&=(xu-x^2v+x^3r/2)s
+ur-xvr+x^2r^2/4-J_1/2,\\
\Phi_{T_1}(u,u)''&=(2x^2v-2x^3r)s-2v^2+4xvr-2x^2r^2,\\
\Phi_R(u,u)''&=2(v-xr)s,\qquad
\Phi_S(u,u)''=-r^2-2xrs.
\end{aligned}
\tag{27}
\]
这些式子直接由 R255(4) 的完整二次算子得出，特别 \(L,V_1\) 的 \(J_0,J_1\) 没有丢掉。

### 4.2 全部准确尾项与普通积分改写

本节所需的普通改写只有
\[
\begin{gathered}
\int ur^2s=-F/3,\qquad
\int v^2rs=-F,\qquad
\int xvr^2s=-(F+G)/3,\\
\int x^2r^3s=-G/2,\qquad
\int rsJ_1=G/2,
\end{gathered}
\tag{28}
\]
以及三个必须保留真实右尾的式子
\[
\boxed{
\int r^2J_0=Z,\qquad
\int vsJ_0=F-Z,\qquad
\int xrsJ_0=(G-Z)/2.}
\tag{29}
\]
第一式来自 \(J_0'=-r^2\)、\(J_0(r_*)=0\) 和真实左值 \(J_0=\mu_0\)。它准确等于 \(\mu_0^2/2\)，不能由“profile 紧”删去。其余式子用一次普通分部积分，所有局部 jet 端项才由紧性消失。

### 4.3 八列完整表

定义八个真实响应
\[
\begin{array}{lll}
K_1=\mathcal B_L(\mathfrak J),&
K_2=\mathcal B_{U_1}(\mathfrak J),&
K_3=-\dfrac{1024}{3}\mathcal B_{T_1}(\chi_{30}),\\
K_4=-\dfrac{1024}{3}\mathcal B_{V_1}(\chi_{30}),&
K_5=1024\mathcal B_{U_1}(\chi_{32}),&
K_6=1024\mathcal B_L(\chi_{32}),\\
K_7=1024\mathcal B_R(\chi_{37}),&
K_8=1024\mathcal B_S(\chi_{37}).&
\end{array}
\tag{30}
\]
全部 \(\tau\) 是已证的完整第三对角核，故 \(K_i\in\mathcal R_{\rm p0}\)。真权逐项为
\[
\mathfrak J:-3,\quad\chi_{30}:-4,\quad
\chi_{32}:-3,\quad\chi_{37}:-2,
\]
\[
L,U_1:-1,\quad V_1,T_1:0,\quad R,S:-2,
\]
所以每个 \(K_i\) 都有成本真权 \(-4\)。这些是完整算子权：也可从 R261 的全部局部 \(D^3K\) 系数和真实右三常数直接检查，不能仅凭一个 self 单项猜权。

将 (27) 代 (26)，只用 (28)–(29)，得到
\[
\boxed{
\begin{array}{c|l}
i&\mathfrak q_u(K_i)\\ \hline
1&-A+C+F/3-G/12-Z/4\\
2&-2C+3D+2F/3-G/12\\
3&2D-2F_3+2F/3-G/3\\
4&B-D+F_3/2-G/24\\
5&4C+6D-18F_3-8F/3-G/6\\
6&2A+6B-2C-6D-2F/3-G/6+Z\\
7&32C-104D+72F_3\\
8&-32D+72F_3+8F/3-22G/3
\end{array}}
\tag{31}
\]
这是 whole self 的准确表。第 1 列的 \(-Z/4\) 和第 6 列的 \(+Z\) 说明只看局部最高 jet 会漏掉完整矩阵方向。按 R314 的唯一有序矩阵，只有这两列分别有
\[
\mathsf T_{00}(K_1)=-1/4,\qquad
\mathsf T_{00}(K_6)=1;
\tag{32}
\]
其他列整 \(\mathsf T\) 为零。本权其他八个矩阵坐标由真权已经为零。

### 4.4 不运行秩程序的完整可核消元

设一个线性泛函在 (16) 的坐标值为
\((a,b,c,d,e,f,g,z)\)，并杀掉 (31) 的八列。由第 2、3、4、5、7 列依次得到
\[
g=\frac{17}{7}f,\quad d=-\frac17f,\quad
e=-\frac3{14}f,\quad c=\frac1{56}f,\quad
b=\frac{11}{168}f.
\tag{33}
\]
为便于检查，前两步可写为
\[
c=\tfrac32d+f/3-g/24,\qquad
e=d+f/3-g/6,
\]
而第 5、7 列分别给
\[
-18d-22f+8g=0,\qquad 6d+13f-5g=0.
\]
第 8 列在 (33) 下恰为 \(-26f\)，所以 \(f=0\)，继而
\(b=c=d=e=g=0\)。第 1、6 列最后变成
\[
-a-z/4=0,\qquad 2a+z=0,
\]
故 \(a=z=0\)。因此八列在八个真实完整坐标中满秩。

结合 (16) 的完整上界，
\[
\boxed{
\mathcal Q(U_{\rm p0}^{(-4)})
=\mathcal Q(\mathcal R_{\rm p0}^{(-4)})
=\operatorname{span}\{A,B,C,D,F_3,F,G,Z\},
\quad\dim=8.}
\tag{34}
\]
本节不声称成本空间 \(U_{-4}\) 或 \(\mathcal R_{\rm p0}^{(-4)}\) 的维数是八。

## 5. 三个负权的联合 pure/self 像准确等于响应像

R207 已给 \(\pi U_{-6}=\pi\mathcal R_{-6}\)，R210 已给
\(\pi U_{-4}=\pi\mathcal R_{-4}\)。对其中任一权和任意 \(V\in U_\sigma\)，先选同权 \(R\in\mathcal R_\sigma\) 使 \(\pi V=\pi R\)。差 \(V-R\) 在真实 pure 核。由 (20) 或 (34)，再选
\(K\in\mathcal R_{\rm p0}^{(\sigma)}\) 使
\[
\mathcal Q(K)=\mathcal Q(V-R).
\]
于是 \(E(V)=E(R+K)\)。这一步保同一个 pure 校正的 self；没有在两次成员门中使用不相容的代表。

连同 (11)，得到
\[
\boxed{
E(U_\sigma)=E(\mathcal R_\sigma)
\quad(\sigma=-8,-6,-4).}
\tag{35}
\]
特别，(35) 不要求这些权的完整成本本身都在 \(\mathcal R\)。

## 6. 联合实际闭锥为整个联合像

### 6.1 闭包与仿射表示

固定原共同端口与 frame，令
\[
\mathcal S=\{V_B:B\text{ 有限真实同端口， }M_B=\mathbf T_B=0\},
\quad C=\overline{\operatorname{cone}(\mathcal S)}.
\]
定义
\[
C_E=\overline{\operatorname{cone}(E\mathcal S)}
=\overline{E C}\subseteq\mathscr P.
\tag{36}
\]
最后等号用连续线性映射与两边闭包，不能删掉闭包而假定闭锥线性像仍闭。

pure 与原仿射作用交换；Q 的共同坐标平移及 (5) 给
\(\ker E\) 在全部正仿射作用下稳定。R322 的有限 Laurent 投影还使该核在真实反号 \(\mathsf S=\mathsf P_{-1}^{\rm alg}\) 下稳定。因此原作用下降到 \(\mathscr P\)，且由 R120/R145
\[
\mathsf P^E_{H,d}C_E=C_E,\qquad \mathsf S_EC_E=C_E.
\tag{37}
\]
这里不把 \(h\) 取负，不改右锚；反号使用 R145 已付的实际几何反号。

\(\operatorname{span}\mathcal S=U\) 使 \(\operatorname{span}C_E=\mathscr P\)，所以正对偶尖。R127 的单权提取证明可以在这个真实有限商上完整应用。

### 6.2 所有可能字符逐项排除

若 \(C_E\ne\mathscr P\)，R127 给非零正仿射字符
\(\ell\)；其拉回
\[
\lambda=\ell E
\]
是 U 上非零、单一整权、平移不变的真实正泛函，而且
\[
\lambda(\mathcal R)=0,\qquad \lambda(\ker E)=0.
\tag{38}
\]
第一式来自 R120 的 \(\mathcal R\subset C\cap(-C)\)，第二式由定义。

R190 的权支撑 \([-9,3]\) 与 R145 的真实反号把候选权限为
\(-8,-6,-4,-2,0,2\)。

* \(-8,-6,-4\)：由 (35)，杀 \(E(\mathcal R_\sigma)\) 就杀整个 \(E(U_\sigma)\)，与非零单权矛盾。
* \(+2\)：R190 已证整个 \(U_2=\mathcal R_2\)。
* \(-2\)：R188 已排除该权全部非零完整正仿射字符。
* \(0\)：R196 对**完整实际闭锥**的权零正字符分类给
  \(\lambda=c\lambda_+\)，\(c>0\)。但 (3) 给 \(H_*\in\ker E\) 和
  \(\lambda(H_*)=c\ne0\)，违反 (38)。

所以不存在所需 \(\ell\)，准确得到
\[
\boxed{C_E=\mathscr P=E(U).}
\tag{39}
\]
这是整个 universal pure 和整个 universal self 的联合结论。它不是从“λ 看不到单个 self 查询”推来的；权零使用 (3)，三个负权使用完整 (35)，其余权各有独立的真实来源。

## 7. 已能严格升级为实际有限控制的十个普适坐标

(39) 本身只关闭锥。本节给一个无需等待整个联合半群问题的实际推论。

对 \(\sigma=-6,-4\)，由已付 pure 像等号选一个真实线性截面
\[
s_\sigma:\pi U_\sigma\longrightarrow\mathcal R_\sigma,
\qquad \pi s_\sigma=\mathrm{id}.
\]
对任意 \(V\in U\) 定义
\[
h_\sigma(V)=\Pi_\sigma V-s_\sigma(\pi\Pi_\sigma V)
\in U_{\rm p0}^{(\sigma)}.
\tag{40}
\]
令 \(F_{-6}\) 取 \(\mathcal Q(h_{-6}(V))\) 在 (12) 的两个坐标；
令 \(F_{-4}\) 取 \(\mathcal Q(h_{-4}(V))\) 在 (15)、(14) 的八个坐标。于是
\[
F=(F_{-6},F_{-4}):U\to\mathbb R^{10}
\tag{41}
\]
是一个固定真实线性观测。不同截面改变其在非零 pure 上的延拓，不改变本文用到的 pure-zero 响应表，也不改变最终 pure 零时的含义。

第 3 节两列与第 4 节八列全在 \(\mathcal R_{\rm p0}\)，真权分开给 (41) 的块对角满射。因此 R222 的一般有限联调定理可直接应用：
\[
\boxed{
\forall p\in\pi U,\ z\in\mathbb R^{10},\quad
\exists\text{有限真实 }B:
M_B=\mathbf T_B=0,\quad
\pi V_B=p,\quad F(V_B)=z.}
\tag{42}
\]
紧目标集具有固定有限词的 \(C^1\) 截面。基准、最终 whole-pure 校正带来的全部 self/mixed 成本、有限大重复数和物理端口桥由 R222 原证明保留；负 z 不是负路径。

这些观测可由有限真实观测承载：(40)–(41) 经有限维实际联合像 \(E(U)\) 因子化。pure 的原坐标与全部 self 评价 \(\mathfrak q_u\) 在该联合像上分离，故其对偶由有限个此类评价张成；保留有限 Laurent 谱投影和固定截面的复合后，每个 (41) 坐标仍是有限个 pure 坐标及真实 profile 查询的线性组合。这里不称 self 评价族单独分离 U。也可在已付 pure 核上沿 R314 的 faithful Euler 坐标取有限 profile 插值。对几何内部扰动，R302 的真实 Duhamel/分部积分密度因此适用，不把“有限维”直接当作几何光滑密度。

选择顺序保 R222/R302：先固定这十列的原型、原 whole-pure 有限库及端口桥，再选共同合法 I 和其有限查询，最后确定参数盒与有限重复数。后续重复不扩大该 scalar 包络。

所用第三原型只有旧 hook/J 结构与 \(\chi_{30},\chi_{32},\chi_{37}\)；它们的完整真实原型、共享倒行和正则族已在 R302 支付。因而可以从起点纳入这些十观测，使用同一增强 IFT 安装其所述共同偶 germ 与 Morse 性；不自动保另一个未纳入的 Gaussian/profile 观测系统。

加入背景 hook 和原 Klein 四块校正，(42) 特别给实际闭 hook：
\[
\pi V_X=0,\qquad
\mathcal Q(\Pi_{-8}V_X)=
\mathcal Q(\Pi_{-6}V_X)=
\mathcal Q(\Pi_{-4}V_X)=0.
\tag{43}
\]
式 (43) 对所有真实紧母包同时成立。它没有支付其他权的全部 self，也不是只在一个固定母包上的十个采样值。

## 8. 整个联合实际半群还缺哪一项

记
\[
\mathscr L=E(\mathcal R),\qquad
\mathscr C=\mathscr P/\mathscr L.
\tag{44}
\]
这是实际函数像的商，不是全 U/\(\mathcal R\)。R206/R212 从满闭锥到有限真实截面的关键是该商上缩放生成元可逆；准确要求
\[
\mathscr C_0=0.
\tag{45}
\]
本文没有从 (39) 自动获得 (45)。

R196 已给 \(U_0=\mathcal R_0+\operatorname{span}\{C_2,C_4,C_6\}\)。
R316 的 (2)–(3) 使 \(E(C_2)\in E(\mathcal R_0)\)，所以
\[
\boxed{\mathscr C_0=
\operatorname{span}\{[E(C_4)],[E(C_6)]\},
\quad \dim\mathscr C_0\le2.}
\tag{46}
\]
这里不是将二者宣成独立或非零。R196 还给 \([C_6]\in N(U_1/\mathcal R_1)\)，故其像是一个真实平移像；单凭这一点仍不能说缩放在 (44) 的零权上可逆。

因此最小的剩余同权成员门是：先用 R201 已付 pure 坐标把 \(C_4,C_6\) 各减去同权响应，再分别比较其完整 Q 与 R316 已付的十三列 pure 核 self 像。不能重新比较 \(\lambda\) 代表 H，也不必重做旧 pure 秩、整个 H0、3974 forcing 或 rank7。

若这两个准确成员关系成立，则 (45) 成立。R206 的证明只用有限仿射投影、完整 R101 传递、真实缩放桥、满闭锥和 (45)，故可将其中 \(\pi\) 逐处替换为 E：
先以严格正配平与 floor 整数取得真实商截面，付各响应原型的商基准，最后保全部剩余基准作有限大 n 的收缩/IFT。届时才可得到
\[
E(\mathcal S)=E(U)
\]
及任意紧联合目标集的真实有限截面。这个句子是**明确的条件后果**，不是本稿已经宣布的实际结论。

若其中某一成员门不成立，也不能从它推出实际不可达；只能说明 R206 的这个纯缩放接口仍有零权缺口，需要直接处理该真实有限商。闭锥结论 (39) 不受影响。

## 9. 完整 mixed 还保留的两函数与实际控制边界

R159 对 pure-zero 成本给唯一的完整函数值双线性表
\[
B_V:\operatorname{Sym}^2\mathcal P\times
\operatorname{Sym}^2\mathcal P\longrightarrow\mathcal F,
\quad
V(f^2,\phi)=B_V(f^2,f^2-\phi^2).
\tag{47}
\]
对固定真实 \(f,g\)，
\[
V_\theta=\sin^2\theta\,D_V-\sin(2\theta)\,G_V,
\tag{48}
\]
其中
\[
D_V=B_V(f^2,f^2)-B_V(f^2,g^2),\qquad
G_V=B_V(f^2,f\odot g).
\tag{49}
\]
这两个量是整个输出函数，含全部原尾与累计历史。

\(\mathcal Q(V)=0\) 只给
\[
[x^2]_{\rm left}B_V(u^2,u^2)=0
\quad\text{对全部 }u.
\tag{50}
\]
极化后 (50) 杀掉该**左二次系数**的完全四对称部分；它不消掉 \(B_V\) 的换槽反对称部分、其余四槽部分，也不消掉整个输出函数的低次左尾或内部函数值。R314 同时使 \(\mathsf T(V)=0\)，但依旧不把 (49) 置零。

特别，\(\lambda_+(H_*)=1\) 已证明 \(H_*\ne0\)，而 R159 的 balanced 忠实性给
\[
\Xi H_*\ne0.
\tag{51}
\]
所以再做一个“完整 \(\Xi H_*\) 是否进入完整响应”的 universal 成员门没有意义：若它进入，R159 会迫 \(H_*\in\mathcal R\)，与 \(\lambda_+(\mathcal R)=0\) 矛盾。真正可支付的是某个固定合法圆、同一 gauge 下 (49) 的准确观测商，不是盲求这个已知不能成立的完整响应身份。

R225 将固定圆的完整 period 范围限制到有限 U 后，确给一个有限观测商。但有限性本身没有证明响应满射。应用 R222/R302 时必须证明**同一个**完整观测系统的响应覆盖，保两 mixed 目标、全平台、内部退化、两端 germ、通量与右锚常数；若同时要求 self 恒零，还需在同一核上作联合比较。不能把多个分开满秩的系统拼成未证明的共同满秩。

最后，R196 对每条非空实际零矩路径仍给
\[
\lambda_+(V_B)=L_B+\int(h_s/h)^2ds>0.
\tag{52}
\]
因此任意 signed **whole universal 成本**的实际支付本身不可能；(39)、(42) 只能是所写投影的支付。完成所有 self 或有限 cross 观测，也不会自动消掉 (52) 中被投影遗失的方向。固定圆/gauge 是否继续遗失它，需要真实原式或完整商的证据。

## 10. 本稿已完成的下一步入口

本稿已经完成：

1. 权 \(-8\) 的完整 self 为零，权 \(-6\) 的二维完整 self 响应覆盖；
2. 权 \(-4\) 含真实 \(\mu_0^2/2\) 尾的八维完整 self 上界、八条明确真实响应及全部准确原式；
3. 三个负权的联合 pure/self 像等于响应像；
4. 整个 universal pure 与整个 universal self 的实际联合闭锥满；
5. 两个负权共十个 universal self 坐标与 whole pure 的真实有限联合截面；
6. 整个联合实际半群的剩余零权缩放接口缩到 \(C_4,C_6\)，并明确其与完整 mixed/gauge 商是不同的未付问题。

这些是纸面原式结论，不需要为八列重复开 Actions。后续若确需新的 \(C_4,C_6\) 原 self 消费，应仅消费两条必要原根与已经公开的比较来源，所有新人工/科学执行仍在公共 Actions。本文没有改变任何旧源、运行或输入。

作者责任：新增显示式均由已发表同锚原式及本文列出的手写分部积分得到；独立核读限于实际收到的数学式。未把非零 sound NF 当成真实非零，也未把闭锥、线性 span、paired 成本差或有限查询控制替换为未经支付的 whole canonical 成本可达性。
