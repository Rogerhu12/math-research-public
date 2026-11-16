# R447：同一四约束纤维与十九门中的非零最高规范 P 方向

日期：2026-11-16。**完整纸面存在证明；没有执行新的符号、积分、profile、秩、零点计数、开发检查或研究运行。**

[R445](R445-two-exact-highest-gauge-null-directions-and-the-complete-P-self-formula.md) 已证明当前完整端口条件迫
$d_f(B_\varepsilon)=d_f(Y)=0$，同时给出 $d_f(P)$ 的完整局部自项。
这还没有证明剩余第一规范通道非零：不能先冻结十九门的一个零点，再移动母形或复制中心。

本稿从构造起点把 $d_f(P)$ 加入同一个完整目标向量。新主行与旧十九行具有同一实际四次幅权，经过真实偶点配对后仍独立。原十二位置正核、同一个四约束图册中的受限最大 $F^\star$ 秩，以及保持全部外区的有号集中，给出一个**有限**参数的准确解。

准确结论如下：对任意预先给定的有限实数 $\eta$，可以从起点选定同一实际母库与圆，使
$$
\boxed{\mathcal V_{19}=0,\qquad d_f(P)=\eta,}
\tag{1}
$$
同时保持 R431 的四个完整自然约束、共同 $D,E_5$、整个原 $\mathcal F_{\rm rat}$、所有真实复制及全部外侧退化邻域。特别取 $\eta\ne0$，R444 的八个原 hook 响应的第一最高规范通道便确为一维；第二通道仍为零。这里不把这个 signed 响应结论升级为消掉全部 period 或十三行的实际路径控制。

直接来源：[R324](R324-complete-rational-quotient-and-nineteen-dimensional-local-ruling-control.md)、[R431](R431-common-exterior-degeneracies-in-the-complete-four-constraint-nineteen-target-library.md)、[R444](R444-original-hook-response-action-and-the-highest-second-period-blind-row.md)、[R445](R445-two-exact-highest-gauge-null-directions-and-the-complete-P-self-formula.md)。布局与复制采用 [R277](R277-low-jet-observation-fibers-and-high-jet-energy-control-for-equal-background-circles.md)、[R280](R280-ordered-three-moment-areas-and-five-block-Gaussian-cancellation.md) 和 R259 §9 的原完整构造。

## 1. 同一个真实对象与从起点冻结的数据

固定原允许的二次高度端口
$$
h=H(1+\varepsilon\sigma^2),\quad H>0,\quad
\varepsilon>0,\quad k=\kappa\ne0,\quad\omega=0.
$$
几何参数、共同合法物理窗口、右锚及有限安装条件沿 R312/R431 先选。不在一个已固定的旧圆或旧目标度量上重解释下文母形设计。

写原严格不交微包圆为
$$
f=\sum_i a_i u_i,\qquad g=\sum_i b_i u_i,\qquad
R_i=a_i^2-b_i^2,\qquad \lambda_i=-a_i^2R_i.
\tag{2}
$$
全部八/十二副本、最终五个完整 block、真实宽度与正四次权都在这一微包列表中。

用 $\mathbf q=(q_0,q_1,q_2,q_3)$ 表示 R411/R431 的四个**零权自然平移系数**，避免与十九目标中的三个平方系数混淆。它们是连续 $C^2$、五次多项式泛函。有限低阶观察仍为
$$
F^\star=(\mathcal F_{\rm rat},D,E_5).
\tag{3}
$$
这里 $\mathcal F_{\rm rat}$ 含原三矩、raw/corrected self、Green、有序接口及所需的全部平移系数。本文不删减(3)，也不把新 $d_f(P)$ 加入 $C^2$ 观察：它是要与十九门共同求解的第20个完整 $C^3$ 目标。

令
$$
\mathbf T_{20}=(\mathcal V_{19},d_f(P)).
\tag{4}
$$
其前十九个分量正是 R324 的
$q_0,q_1,q_2$、七个 $\rho_\ell$ 与九个有理 $Z_m$。它们始终表示完整原值，而非 principal 或某个重锚后的近似。

## 2. 新行的完整原式与共同齐次性

记
$$
p=u',\quad r=u'',\quad t=u''',\qquad
W=p-xr,\qquad C=u-xp+\frac{x^2r}{2}.
\tag{5}
$$
原 $P=\Phi_{r_0}$、$Y=\Phi_{p_2}$ 的右锚输出为
$$
P(u,u)=J(r^2),\qquad
Y(u,u)=-xu^2+x^2up-\frac{x^3p^2}{2}
-\frac{x^2}{4}J(x^2r^2+2p^2).
$$
单包 $P$ 的左尾为常数，单包 $Y$ 的左尾为纯二次项。
R445 §6 已按完整
$I_2(v,w)=\int(x^2v''w''+2v'w')$
证明所有不同微包的 $I_2(Y_i,P_j)$ 为零；其关键边项是
$$
I_2(Ax^2,P_j)
=2A\int x^2P_j''+4A\int xP_j'=0.
$$
所以没有需另冻结的 $P/Y$ ordered 残量，准确有
$$
d_f(P)=\sum_i a_i^2R_i\,I_2(Y(u_i,u_i),P(u_i,u_i)).
\tag{6}
$$

R445 §7 的完整原式为
$$
I_2(Y(u,u),P(u,u))
=-2\int x^4Cr\,t^2
+2\int(u-xp)^2r^2-\frac1{12}\int x^4r^4 .
\tag{7}
$$
后三阶线性项已用真实紧 outer jets 分部积分；没有把 $P$ 的左常数或 $Y$ 的左二次尾置零。
由(2)、(6)、(7)，
$$
d_f(P)
=\sum_i\lambda_i\int \mathcal P_{20}(x,u_i,u_i',u_i'')(u_i''')^2
+\mathcal B_{20}(\mathbf u),
\qquad
\mathcal P_{20}=2x^4Cr,
\tag{8}
$$
其中
$$
\mathcal B_{20}
=\sum_i a_i^2R_i
\left\{2\int(u_i-xu_i')^2(u_i'')^2
-\frac1{12}\int x^4(u_i'')^4\right\}
$$
是明确的连续 $C^2$ 四次多项式。

R324/R431 的原完整十九行使用同一个 $\lambda_i$：
$$
\mathcal V_{19}
=\mathcal B_{19}(\mathbf u)
+\sum_i\lambda_i\int
\mathbf P_{19}(x,u_i,u_i',u_i'')(u_i''')^2 .
\tag{9}
$$
$\mathcal B_{19}$ 包括全部真实 local、chain、非紧 self、Green 和有序 history；并非把这些项设为零。(8)、(9)合成整个(4)的完整 $C^2$ 余项加三阶平方分裂。

二十个目标都对完整 $(f,g)$ 的共同幅度呈四次齐次性。各 $\mathcal P_j$ 都对 $(u,p,r)$ 为二次；再乘 $t^2$ 正是四次。四个 $\mathbf q$ 约束及 $D,E_5$ 的五次齐次性不用于复制主列的符号，它们通过同一个有限低阶 IFT 准确保持。不能把这两种幅权相混。

## 3. 新行在真实偶配对后仍独立

R324 §§4–6 已证明：原十九个 $\mathcal P_j$ 是 $x,W,C$ 的二次多项式，线性独立；作为关于实际位置 $x$ 的多项式，其次数至多10。
新行 $2x^4Cr$ 的位置次数至多6，也在这个统一次数界内。

首先明确真实偶母所产生的普遍核。若一个关于 $(u,p,r)$ 的二次多项式 $F$ 对所有开集中的 $X,b,u,p,r$ 满足
$$
F(X+b,u,p,r)+F(X-b,u,-p,r)=0,
\tag{10}
$$
则比较各二次 jet 单项式：偶于 $p$ 的系数多项式都为零；奇于 $p$ 的两个系数关于 $x$ 必须是常数。因此
$$
F=\alpha up+\beta pr,\qquad \alpha,\beta\in\mathbb R.
\tag{11}
$$
这一论证在 $b$ 的任意非空正开区间内仍成立，因为(10)是多项式恒等。没有把一个实际偶母在 $b=0$ 的 $p$ 当作自由 jet。

假定新行在旧十九行与此普遍核之和中：
$$
2x^4Cr-\sum_{j=1}^{19}c_j\mathcal P_j
=\alpha up+\beta pr.
\tag{12}
$$
作可逆代换
$$
p=W+xr,\qquad u=C+xW+\frac{x^2r}{2}.
$$
旧十九行没有 $Cr$ 项；$up$ 的 $Cr$ 系数为 $x$，$pr$ 的 $Cr$ 系数为0。比较(12)的 $Cr$ 系数就迫
$$
2x^4=\alpha x,
$$
不可能作为多项式恒等。因此新行不在旧像中。

若一个二十行组合满足(10)，先由上述比较使新行系数为零，再用 R324 已付的十九行偶配对独立性，余下系数也全零。故
$$
\boxed{\text{二十行在真实偶点对的普遍主观察中线性独立。}}
\tag{13}
$$
这里明确使用的是二阶自由 jets 的有限多项式分离，不是“多一行所以多一秩”。

固定任意正物理宽度 $w$ 后，母坐标到物理坐标的 jet 变换为
$(u,p,r)\mapsto(u,p/w,r/w^2)$，点对为 $X\pm wb$。
这是可逆缩放，故同一结论成立。以下实际宽度保持在列内。

## 4. 所有真实副本与原十二位置正核

取 R280 五个最终 block 中任意一个具有正最终权的**正布局** block。只在这个完整 block 的若干基本位置及其全部规定副本中使用新形状参数；其他 block 的完整贡献留在(9)的基线中。这样不要求每个 block 单独实现二十目标，也不省略它们之间原有的低阶项。

在所选 block 内，R277 的17进制层长为 $L=17^{11}$，二进制第二层有 $2^{11}=2048$ 个真实位置层。为至多20个形状组使用不同的第二层；容量足够，不添加或改变原编码。

每个形状组使用原十二个第一层索引
$$
j_\ell\in\{0,1,33,34,49,50,65,66,81,82,97,98\}.
\tag{14}
$$
它们的 high/low 依次交替。因为
$R_{\rm high}=8B$、$R_{\rm low}=-B/2$、
$a_i^2=B+R_i>0$，
对应 $\lambda_i=-a_i^2R_i$ 的符号为
$-,+,-,+,\ldots,+$。第二层改变 $a_i$ 的符号而不改变 $\lambda_i$。

全部八/十二副本对每个 $\pi/2$ 主行均使用正四次权。
固定所选 block 的实际平移 $d_\nu$ 与四次权 $\omega_\nu>0$，其共同算子为
$$
(\mathcal TP)(X)=\sum_\nu\omega_\nu P(X+d_\nu).
\tag{15}
$$
在 $\operatorname{Pol}_{\le10}$ 上它是三角可逆映射，主对角为
$\sum_\nu\omega_\nu>0$。十二次 $g$ 翻号对这些 even 值没有额外负号；最终 block 的正权也包含在(15)中。
共同母三矩决定的原正归一因子，选定母后一次冻结；它们只加入真实非零正因子，不更改上述符号。若原构造还要求共同 $I_0$ 归一，该一个正幅也在求(32)之前按已冻结的共同矩确定并计入列与基线；最终准确根之后不再另作幅度归一。

对一个固定的偶点形状，记其经过(15)的二十维位置多项式为
$\mathbf P(X)$。其十二个实际递增中心记作 $X_\ell$。令
$$
\beta_\ell=\frac1{\prod_{m\ne\ell}(X_\ell-X_m)}.
$$
十二点原 Vandermonde 恒等式给
$$
\sum_{\ell=0}^{11}\beta_\ell\mathbf P(X_\ell)=0,\qquad
\operatorname{sgn}\beta_\ell=(-1)^{11-\ell}.
\tag{16}
$$
这个符号与 $\lambda_\ell$ 相同。故实际列
$\mathbf v_\ell=\lambda_\ell\mathbf P(X_\ell)$ 具有严格正核
$$
c_\ell=\beta_\ell/\lambda_\ell>0.
\tag{17}
$$
若列中还有共同正的宽度、点对与集中质量因子，把它们保留或除入 $c_\ell$ 均不改变严格正性。

十二点评价张成该形状的全部位置系数空间。
由(13)，有限个形状的这些系数空间之和为 $\mathbb R^{20}$；至多20个形状组足够。它们可取不同的集中点，有限 Hermite 扰动可把相应二阶 jet 见证放在同一个母上。
将每个形状分配到不同第二层并不改变这一结论：每个组自己的十二个中心仍能张成其整个系数空间，第二层平移不能降低这个空间。

因此，在同一个实际布局上，联合所有选中列有
$$
\operatorname{span}\{\mathbf v_i\}=\mathbb R^{20},
\qquad
\ker[\mathbf v_i]\text{ 中有各分量严格正的向量。}
\tag{18}
$$
任意目标先作实线性表示，再加足够大的(17)，即可使全部系数严格正。这给的是完整有限正锥，不只是 signed span。

## 5. 四约束图册与受限最大 F 秩必须先共同选择

本节把第4节的形式见证放进 R431 的同一个真实母空间。

沿 R431 §§2–3，先选正偶解析母
$u_{\rm a}=\psi_3P_{\rm a}$，其中
$\psi_3(y)=\exp[-3/(1-y^2)]$、$P_{\rm a}>0$，满足
$$
\mathbf q(u_{\rm a})=0,\quad
\operatorname{rank}D\mathbf q(u_{\rm a})=4,\quad
D(u_{\rm a})-E_5(u_{\rm a})>0.
$$
全部非平端 $p$ 与 $A=6u'u'''-2(u'')^2$ 零点有限、简单。
选中心小区间 $[-\delta,\delta]$，使
$$
A_{u_{\rm a}}\le-c_A<0,\qquad
u_{\rm a}'(y)/y
\text{ 与 }u_{\rm a}''(0)\text{ 同号且离零。}
\tag{19}
$$
所有 $A$ 根及非中心 $p$ 根在外区。

在 $(0,\delta)$ 内取闭包不交的 $J_{\rm n},J_{\rm p}$。
R431 的解析 Euler 唯一性引理保证：
四个正常方向 $e_1,\ldots,e_4$ 可全部放在
$J_{\rm n}\cup(-J_{\rm n})$，且实际 $D\mathbf q[e_\alpha]$ 可逆。

令 $\mathscr B_\delta$ 为原偶 $C^2$ 内支撑空间，
$X=\ker D\mathbf q(u_{\rm a})$。以这些真实正常方向作图册
$$
\chi(v)=u_{\rm a}+v+\sum_{\alpha=1}^4a_\alpha(v)e_\alpha,
\qquad
\mathbf q(\chi(v))=0,\quad
a(0)=Da(0)=0.
\tag{20}
$$
所有外区在这个图册上准确不动。

在此**受限图册**中取
$$
r_\star=\max\operatorname{rank}D(F^\star\circ\chi).
\tag{21}
$$
这是整个有限观察(3)在该空间的真实最大微分秩，不是其行数，也不要求等于原全域最大秩。光滑方向的稠密性给一个真实光滑最大 minor。

第3–4节的主见证可放在 $J_{\rm p}$ 的任意有限个不同点。
偶 Hermite 扰动给独立的二阶 jets；将其投影到 $X$ 及(20)的正常纠正只改变 $J_{\rm n}$，因此不改变这些见证 jets。
于是由原位置多项式系数列选取的二十阶 minor 在同一个图册中不恒零。这里先去掉共同非零正因子及可逆的 $\mathcal T$ 来选择有限 jet minor；该 minor 是 jets 的多项式。恢复所有原复制与归一后，第4节的系数空间等式保证实际列仍满行秩，不需要额外假定某个尚未冻结的布局归一函数为多项式。

把(21)的最大 minor见证和这个二十行系数 minor 放入同一个有限维光滑参数空间。两者是非零实解析函数，有限乘积不恒零，可在原点任意近处同时非零。取固定方向上的足够小参数，得到
$$
u_0=\chi(v_0)
\tag{22}
$$
在 $C^4$ 中任意接近 $u_{\rm a}$，并同时具有：

- $\mathbf q(u_0)=0$、$D(u_0)-E_5(u_0)>0$ 和正性；
- 受限最大 $F^\star$ 秩 $r_\star$；
- 真实二十主列的满行秩；
- (19)的严格界，以及 $u_0=u_{\rm a}$ 于 $|y|\ge\delta$。

这里冻结的是新值 $F^\star(u_0)$。没有在旧十九门零点上另加目标或移动一个已经求好的圆。

取 $r_\star$ 个实际切向 $f_\ell$ 与相应输出 $F_I$。
原块三角 Jacobian
$$
D(\mathbf q,F_I)(u_0)[e_\alpha,f_\ell]
=
\begin{pmatrix}
D\mathbf q[e_\alpha]&0\\
*&DF_I[f_\ell]
\end{pmatrix}
\tag{23}
$$
可逆。由受限最大秩的局部常秩论证，保持
$\mathbf q,F_I$ 就保持**整个** $F^\star$。
全部方向固定、光滑并严格位于中心区间。

## 6. 同纤维集中保持每个外侧 A 根和全部 jets

采用 R431 的有号集中，而不使用会在中心新增退化点的无保护振荡。

对每个选定 $b_i\in J_{\rm p}$，令
$$
g_{N,b}(y)=\sqrt N
\{e^{-N^2(y-b)^2}-e^{-N^2(y+b)^2}\},\qquad
y g_{N,b}(y)\ge0.
$$
取偶原函数 $\zeta'''_{N,b}=g_{N,b}$，在0取前三个零初值。
取非负偶 cutoff $\chi_0$ 支撑于 $J_{\rm p}\cup(-J_{\rm p})$、
在全部集中点附近为1，令
$$
s_0=-\operatorname{sgn}u_0''(0),\qquad
w_{N,b}=s_0\chi_0u_0\zeta_{N,b}.
\tag{24}
$$
原直接积分估计给
$$
\|w_{N,b}\|_{C^2}=O(N^{-1/2}),\qquad
w'''_{N,b}=s_0\chi_0u_0g_{N,b}+O(N^{-1/2}).
$$

在任一预先固定的有限非负幅度盒内，以(23)解
$$
U_{i,N,z_i}=u_0+z_iw_{N,b_i}
+\sum_\alpha c_{i\alpha,N}(z_i)e_\alpha
+\sum_\ell d_{i\ell,N}(z_i)f_\ell,
$$
$$
\mathbf q(U_{i,N,z_i})=0,\qquad
F^\star(U_{i,N,z_i})=F^\star(u_0).
\tag{25}
$$
系数与一次幅度导数都是 $O(N^{-1/2})$。固定纠正方向的全部高阶范数只是有限常数，所以
$$
U_{i,N,z_i}'''
=u_0'''+s_0z_i\chi_0u_0g_{N,b_i}+e_{i,N,z_i},
\qquad
\|e_i\|_\infty+\|\partial_{z_i}e_i\|_\infty=O(N^{-1/2}).
\tag{26}
$$

正性由中心紧支撑上的 $C^2$ 小量保持；外区一字不变。
偶性及二阶小量使实际 $U_i'/y$ 保(19)的号。
保留三阶高项的**实际**一导系数，得到
$$
A_{U_i}=A_{u_0}
+6U_i's_0z_i\chi_0u_0g_{N,b_i}+O(N^{-1/2}).
\tag{27}
$$
中间项在左右整个中心都非正。
因此足够大有限 $N$ 时，整非负幅盒上有
$$
A_{U_i}<0\ (|y|\le\delta),\qquad
U_i=u_0=u_{\rm a}\ (|y|\ge\delta).
\tag{28}
$$
这使用 $U_i'$ 本身，不把 $(U_i'-u_0')g_{N,b}$ 错当作一致小误差。

所以全部外 $A$ 根的位置、邻域与任意阶 jets 都共同固定；所有非中心 $p$ 根也不动，中心 $p$ 根仍简单。根数仍是原母的任意有限 $2m$，未缩为一对。各物理包继续按真实 $\xi_i,w_i$ 输运这些相同根和 jets。

## 7. 完整二十值的统一 C1 极限

由(8)、(9)，整个目标映射具有同一原式分裂
$$
\mathbf T_{20}(\mathbf U)
=\mathbf B_{20}(\mathbf U)
+\sum_i\lambda_i\int
\mathbf P_{20}(x,U_i,U_i',U_i'')(U_i''')^2\,dx .
\tag{29}
$$
这里 $\mathbf B_{20}$ 的前十九行是原完整余项，第20行为(8)。
其他未变化的 block、原有序跨项、全部中心常数都保留在这个映射中。

(26)的高项 $L^2$ 范数有界、$L^1=O(N^{-1/2})$；与固定三阶基线的交叉趋零。二阶系数及其一次参数导数一致趋近原值，乘有界的三阶平方积分仍趋零。
$\mathbf B_{20}$ 的连续 $C^2$ 多项式性质使它及一次参数导数也有相应极限。
所以在每个固定有限幅度盒上，
$$
\boxed{
\mathbf T_{20,N}(\mathbf z)
=\mathbf b+\sum_i z_i^2\mathbf v_i+o_{C^1}(1).
}
\tag{30}
$$
$\mathbf b$ 是同一完整圆的真实基线，不是零，也不只包含活动 block。

为明确宽度和真实权，若一个形状组物理宽度为 $w$、母坐标集中点为 $b$，
其列除 $\lambda_i$ 外的共同正因子为
$w^{-5}u_0(b)^2\sqrt{\pi/2}$；其位置向量由
$$
\mathcal T\!\left[
\mathbf P_{20}(X+wb,u_0(b),u_0'(b)/w,u_0''(b)/w^2)
+\mathbf P_{20}(X-wb,u_0(b),-u_0'(b)/w,u_0''(b)/w^2)
\right]
\tag{31}
$$
给出。式(31)直接来自高项平方在两个实际点的集中质量。所有原复制权均在 $\mathcal T$ 中，没有用虚拟同中心替代原平移。
其符号和位置次数正是第4节使用的真实列。

(30)包含新 $dP$ 的全部低阶余式；不要求这些余式先为零，也不将 principal 非零误作完整函数已可取任意值。

## 8. 同一个有限 N 的准确十九零与任意 dP 值

令
$$
\mathbf y_\eta=(0,\ldots,0,\eta)\in\mathbb R^{20}.
$$
由(18)，可选有限个**严格正** $s_i^*$，使
$$
\mathbf b+\sum_i s_i^*\mathbf v_i=\mathbf y_\eta.
\tag{32}
$$
具体地，先线性表示 $\mathbf y_\eta-\mathbf b$，
再逐形状组加足够大的严格正核(17)；所有系数便为正。
取 $z_i^*=\sqrt{s_i^*}$，固定一个包含此点的有限正幅盒。

选择二十条独立列，固定其他幅度。
极限映射的这二十列 Jacobian 为
$[2z_i^*\mathbf v_i]$，可逆。
先把幅度盒固定，再以(25)—(30)选择足够大的**同一个有限** $N$。
有限维非退化零点稳定性给真实正幅 $\mathbf z_N$，
$$
\boxed{
\mathbf T_{20,N}(\mathbf z_N)=\mathbf y_\eta.
}
\tag{33}
$$
这就是(1)。没有要求 $1/N$ 构成光滑参数，也没有把一个无限集中对象当成最终 profile。

所有 $U_i$ 同时满足(25)、(28)；每个基本位置的全部实际副本同步使用该 $U_i$。
未活动位置用 $u_0$，也满足相同约束。
因为三矩及整个 $F^\star$ 恒定，原格点三矩、完整第三、corrected-self 角身份和三个真实有序面积都保持原构造的准确值。
R324 的全角还原因此仍把十九个 $\pi/2$ 零提升为同一真实圆的完整中心偶商零。

这一步是在整个最终圆上一次求解(33)，而非把五个不同解各自拼接：非活动 block 的完整值已包含在 $\mathbf b$，活动 block 的二十列覆盖整个目标空间。任何原跨项也已在(29)的完整 $C^2$ 余项内计入。

## 9. 与共同 cap、自然查询及规范响应的接口

(25)在整个 $[0,z_i^N]$ 上定义，给从 $u_0$ 到 $U_i$ 的真实同 $\mathbf q,F^\star$ 连通路径，且变化严格在中心。
因此 R431/R407 的同三矩外 cap 结论仍适用所有共同外根，不需要另造一条连接。
新库还保留共同 $D,E_5$ 与每个母的完整零权自然约束，故没有破坏 R429/R433 共同查询与实际截面所使用的 profile 前提。

这句话保留那些实际截面的原实施条件：共同合法窗口、同端口与完整 prototype 基准仍按其来源处理。它不把某个新 signed 响应自动实现为旧固定几何上的免费路径，也不宣全部内部 partial 或十三行已清。

现在固定(33)所得的一个新圆，取 $\eta\ne0$。
R445 的两条精确零仍由前十九个完整值推出：
$$
d_f(B_\varepsilon)=d_f(Y)=0.
$$
原十二副本与真尾证明也仍给
$$
e_f(X)=I_2(Yff,Xfg)=0\qquad(X\in E_8).
\tag{34}
$$
而新方向准确有 $d_f(P)=\eta$。

令原全局第三系数为 $\tau\ne0$，它不同于局部端口参数 $\kappa$。
对 R444 的原响应 $s\,B_P\mathfrak H$，其对两个真 range 特解的改变为
$$
\delta k_d=-sP(f^2-g^2)/\tau,\qquad
\delta k_e=sP(f,g)/\tau.
$$
从而
$$
\boxed{
\delta\ell_f(k_d)=-s\eta/\tau,\qquad
\delta\ell_f(k_e)=0 .
}
\tag{35}
$$
真实最高规范 $P_2$ 行还须乘 $\kappa/24$：
$$
\delta P_{2,d}=-\frac{\kappa s\eta}{24\tau},\qquad
\delta P_{2,e}=0.
\tag{36}
$$

同一个响应位于原 $\mathcal R\cap\ker J^+$，并且其改变量是原 $L_f$ 像。
所以 R444 已证的 whole $E$、有限自然与 universal ordered 零、全部内部 $A_f$ 通量及 $C$、三条规范合法矩保持不变。
这里的保护来自完整原响应身份与平端通量边界，不是只看一个主符号。

对已经真正落在原 $L_f$ range 中的两个目标，八支路的最高行 signed 判据因而简化成：第二行原值必须为零；第一行可用(35)准确修正。
尚未在 range 中的一般目标不能先套 $\ell_f(k)$，更不能用(35)宣布 range 已付。

## 10. 本次支付与仍未支付的部分

本稿完成了同一个实际母库上的(33)，并因此给出非零第一最高规范响应轴。它比“十二副本没有恒等消掉 d”更强：全部原十九门、四个自然约束、整个低阶纤维、共同外区与真实正权都在同一有限解上成立。

它没有声称原先已冻结的任意圆满足 $d_f(P)\ne0$。
这里重新从起点选择了母与种子；在选定(33)之后才冻结新的共同库和查询。

最高第二规范行对这八个支路仍盲。其余九个端口系数、所有 period range 与规范联合条件、其他几何段及实际 prototype 的完整共同基准仍须处理。即使某个 signed 修正保持 $J^+$ 和全部通量，也不能把它自动当作实际路径的零基准截面。

新结论的独核范围：literature 仅窄核了第3节 $Cr$ 系数与真实偶配对的独立性，不将该窄核扩称为已独审本稿的受限纤维、正核或有限根全过程。
