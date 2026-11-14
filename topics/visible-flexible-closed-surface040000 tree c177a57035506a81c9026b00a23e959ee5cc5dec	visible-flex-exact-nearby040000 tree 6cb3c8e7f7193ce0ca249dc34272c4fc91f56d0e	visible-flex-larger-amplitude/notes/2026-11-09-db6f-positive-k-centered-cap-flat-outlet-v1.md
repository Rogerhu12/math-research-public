# 具有正则中心的实际正曲率帽：显式共度量族及逆向有限平坦领

**状态：完整作者推导，待全文独立审查。** 2026-11-09至11-10，独立几何分工。
本文构造真正的有心圆盘帽，而非只写一条边界或形式第二基本形式。
它有一个显式的非刚体连续参数、共同光滑度量、完整圆周、正则中心，
并能在共同材料上向外延到有限平坦领。

它不与当前固定H圆柱族自动匹配。
本稿没有闭曲面、指定全局握持区或宏观像幅度；
只把一个真实帽子及其可供匹配的全部端口数据固定下来。
不修改旧稿，不读主优化数组，不运行BVP、tail、RK、PDE或网格。

## 1. 固定参数和显式母曲面

取 A属于[4/5,1]，并定义

$$
h_A(s)=\sqrt{1-A^2\sin^2s},\qquad
z_A(s)=\int_0^s h_A(v)\,dv .
\tag{1}
$$

在 |s|<pi/2、适当短的实phi区间上定义

$$
X_A(s,\phi)=
\bigl(A\cos s\cos(\phi/A),\
      A\cos s\sin(\phi/A),\
      z_A(s)\bigr).
\tag{2}
$$

(1) 是确定积分，不含可随参数调整的常数。
直接微分有

$$
(X_A)_s=(-A\sin s\cos(\phi/A),-A\sin s\sin(\phi/A),h_A),
$$

$$
(X_A)_\phi=(-\cos s\sin(\phi/A),\cos s\cos(\phi/A),0).
\tag{3}
$$

因此所有A共享

$$
I=ds^2+\cos^2s\,d\phi^2.
\tag{4}
$$

选择单位法向

$$
N_A=(-h_A\cos(\phi/A),-h_A\sin(\phi/A),-A\sin s).
\tag{5}
$$

它等于 (X_s×X_phi)/cos s。
两个主曲率和第二形式为

$$
k_s=\frac{A\cos s}{h_A}>0,\qquad
k_\phi=\frac{h_A}{A\cos s}>0,\qquad k_s k_\phi=1,
$$

$$
II=k_s\,ds^2+k_\phi\cos^2s\,d\phi^2 .
\tag{6}
$$

故K恒为1。A=1时(2)是标准单位球面的一片；
A<1时中心附近两个主曲率不等，绝非只把同一球片换参数。

## 2. 真正的有心圆盘、共同材料及中心正则

取rho_0=1/4。对0<=rho<=rho_0、u属于R/(2piZ)，令

$$
s=\arcsin(\sin\rho\cos u),\qquad
\phi=\arctan\!\left(\frac{\sin\rho\sin u}{\cos\rho}\right).
\tag{7}
$$

arctan选在(-pi/2,pi/2)的连续实支。
这里交换了通常随意命名的两个极向轴，
使(rho,u)与(s,phi)同向；这一选择保证下面的C分量为正。

定义共同材料圆盘上的实际位置

$$
F_A^{\rm cap}(\rho,u)=X_A(s,\phi)-(A,0,0).
\tag{8}
$$

rho=0处的所有u是同一个材料点，不是内边界。
设材料Cartesian坐标
xi=rho cos u、eta=rho sin u。
那么

$$
s=\arcsin\!\left(\frac{\sin\rho}{\rho}\xi\right),\qquad
\phi=\arctan\!\left(\frac{\tan\rho}{\rho}\eta\right).
\tag{9}
$$

sin(rho)/rho和tan(rho)/rho在rho=0是rho^2的解析函数。
因此(9)、(1)–(2)在整个闭材料圆盘及其一个开邻域内真实解析。
特别地，

$$
F_A^{\rm cap}(0)=0,\qquad
(F_A^{\rm cap})_\xi(0)=e_z,\qquad
(F_A^{\rm cap})_\eta(0)=e_y.
\tag{10}
$$

中心为正则点，位置和一阶切向框架对全部A相同。
不存在锥顶、折痕或只在极坐标中“看起来有限”的奇点。

(7)把材料点送到单位球上的
(cos rho,sin rho sin u,sin rho cos u)，故(4)回拉为

$$
g_{\rm cap}=d\rho^2+\sin^2\rho\,du^2 .
\tag{11}
$$

它是中心光滑的同一个球面度量。
(7)对u真正2pi周期，故(8)完整圆周位置闭合。
这里没有把旋转母面中的phi/A误当成一个必须单独2pi闭合的角坐标：
材料圆周是在一个短(s,phi)图内的一条闭曲线。

## 3. 全参数嵌入与正 C边界的完整公式

事实上(8)在更大的rho<=3/10上仍联合光滑且嵌入。
由(7)，|s|<=rho、|phi|<=rho。
后一个不等式也由cos rho=cos s cos phi直接得到。
所以|phi/A|<=3/8<pi。

若两个(2)的位置相同，z_A严格递增先给s相同；
A cos s>0，再由水平角所在区间长度<2pi给phi相同。
(7)是球面半径<pi/2的正常坐标图，故材料点相同。
因此整个紧A区间上的圆盘是真正的全时间嵌入。

在rho<=rho_0，cos s>=cos(1/4)>31/32，h_A<=1且h_A>=cos s。
由(6)，

$$
31/40<k_s\le1,\qquad 1\le k_\phi<40/31.
\tag{12}
$$

为列出真正的Cauchy数据，记c_s=cos s，则

$$
s_\rho=\frac{\cos\rho\cos u}{c_s},\qquad
s_u=-\frac{\sin\rho\sin u}{c_s},
$$

$$
\phi_\rho=\frac{\sin u}{c_s^2},\qquad
\phi_u=\frac{\sin\rho\cos\rho\cos u}{c_s^2}.
\tag{13}
$$

其Jac为sin rho/c_s>0。
在rho=rho_0的实际位置、框架为

$$
\Gamma_A=F_A^{\rm cap}(\rho_0,u),\quad
e_{1,A}=X_s s_\rho+X_\phi\phi_\rho,\quad
e_{2,A}=\frac{X_s s_u+X_\phi\phi_u}{\sin\rho_0},\quad N=N_A.
\tag{14}
$$

这些公式的每个分量均已明确，且e_1×e_2=N。
二次型的三个Cauchy分量为

$$
\begin{aligned}
L_A&=k_s s_\rho^2+k_\phi c_s^2\phi_\rho^2,\\
M_A&=k_s s_\rho s_u+k_\phi c_s^2\phi_\rho\phi_u,\\
C_A&=k_s s_u^2+k_\phi c_s^2\phi_u^2 .
\end{aligned}
\tag{15}
$$

因此L_A C_A-M_A^2=sin^2rho_0，正好是K=1的Gauss恒等式。
并且(12)给

$$
C_A\ge(31/40)\sin^2(1/4)>1/25,\qquad
|M_A|<10/31,\qquad L_A<40/31 .
\tag{16}
$$

最后的C下界可用sin(1/4)>1/4-(1/4)^3/6=95/384后作纯有理比较。
边界是完整的正 C非特征圆周，不含尚未处理的C角零点。

## 4. 角解析与统一存在时间：只使用已核的解析定理

使用已完整独审的角解析Gauss–Codazzi存在接口：
[正C有限平坦领固定0239fffd6e5206dfadb778db4ba5a057e01cfc5a，§8](https://github.com/Rogerhu12/math-research/blob/0239fffd6e5206dfadb778db4ba5a057e01cfc5a/topics/visible-flexible-closed-surface/notes/2026-11-09-db6f-positive-epicycle-finite-flat-collar-v1.md)，
全文独审e927f688421290880733e8de0ddc2d017ef8c574。

其外部主来源是Nishida作者讲义：
[Chapter III §2，Hypothesis 2.1与Theorem 2.1，印刷pp.64–65；拟线性应用pp.72–73](https://bibliotheque.imo.universite-paris-saclay.fr/media/filer_public/bb/b2/bbb2303a-1e17-4807-a319-290a5b030b2f/n_nishida-102.pdf)。
该接口允许径向变量仅连续，寿命由解析尺度、函数值界与Lipschitz界决定，
不要求截止高阶径向导数有统一界。

本稿逐项支付其输入：
(1)、(7)、(13)–(15)在实u和紧参数A属于[4/5,1]附近解析；
平方根、arcsin、arctan都远离实支奇点，A也远离0。
紧性给共同复u条带及A的一个共同复邻域，
其中M_A,C_A有界，且由(16)缩小邻域后|C_A|>=1/50。
取一个足够小的共同解析球，保持|C|>=1/100。
因此所有分母界均是真正的共同界，不是逐A另外挑条带。

选固定非增光滑psi，psi=1于x<=1/4、psi=0于x>=3/4，
0<=psi<=1，且在中间严格介于0与1。
例如取上一类标准E函数构造的1-S。
对delta>0在rho>=rho_0定义

$$
a_\delta''(\rho)=-\sin\rho\,
                  \psi((\rho-\rho_0)/\delta),\qquad
a_\delta(\rho_0)=\sin\rho_0,\quad
a_\delta'(\rho_0)=\cos\rho_0 .
\tag{17}
$$

在固定窗rho_0<=rho<=rho_0+1/20中，

$$
a_\delta\ge\sin\rho_0>95/384,\quad
a_\delta<3/10,\quad
9/10<a_\delta'\le1,\quad |a_\delta''|\le1 .
\tag{18}
$$

例如a'>=cos rho_0-1/20>31/32-1/20>9/10；
因此a单调为正，其他界由一次积分给出。
所有界均不依delta。

令Q=a a''、mu=a'/a、beta=aa'。
在解析尺度中写

$$
M_\rho=\partial_u((M^2-Q)/C)-\mu M,\qquad
C_\rho=M_u+\mu C+\beta(M^2-Q)/C .
\tag{19}
$$

更明确地，(19)的角主矩阵与零阶项是

$
\mathcal A(M,C)=
\begin{pmatrix}2M/C&-(M^2-Q)/C^2\\1&0\end{pmatrix},
\qquad
\mathcal B(M,C)=(-\mu M,\ \mu C+\beta(M^2-Q)/C).
$

若初始解析范数为B_0、球半径R<=1/100，令B_1=B_0+R、c=1/100。
在这个球上，矩阵、零阶项及其未知量导数都可统一粗界为
Lambda=100(1+B_1)^3(1+c^{-3})；这里由(18)有|Q|<1、|mu|<5、|beta|<1。
固定初值在双宽条带中的导数用B_0/sigma_0控制，
所以平移未知量U=U_0+V后满足来源中同一解析尺度的Lipschitz与初始源假设。
这些界均独立于delta。

(18)控制a,a',Q和所有所需分母；a、Q均不依u。
Cauchy条带估计给唯一的一阶角导数损失
1/(sigma-sigma')，有限有界解析球上其Lipschitz常数
只依(16)、(18)和初始解析范数，不依a'''或delta的更高导数。
故Nishida接口先给一个与delta无关的共同T_*>0。
**现在才**取

$$
0<\delta<\min(1/20,T_*/2).
\tag{20}
$$

整个截止及其后的开平坦领因此处于已证明的存在窗。
M,C对u及A解析，对固定rho的全部变量光滑，C保持严格正。
这里Q最初为负；没有错误调用仅适用于Q>=0的单调能量定理。

## 5. 从真实圆盘位置重构并保留全部 jet

以(14)为实际径向初值，用(19)的解重构

$$
F_\rho=e_1,\quad(e_1)_\rho=LN,\quad
(e_2)_\rho=(M/a)N,\quad N_\rho=-Le_1-(M/a)e_2,
\qquad L=(M^2-aa'')/C .
\tag{21}
$$

Gauss–Codazzi是它与
F_u=ae_2、
(e_1)_u=a'e_2+MN、
(e_2)_u=-a'e_1+(C/a)N、
N_u=-Me_1-(C/a)e_2
的完整相容条件。角误差为零初值齐次径向系统，
所以诱导度量确为

$$
g_\delta=d\rho^2+a_\delta(\rho)^2du^2 ,
\tag{22}
$$

在原rho<=rho_0圆盘中仍取a=sin rho。
实际初始位置和标架均周期，径向ODE唯一性使二者继续真正周期，
没有另一个平移monodromy可事后选择。

在[rho_0,rho_0+delta/4]，(17)与a=sin rho具有同一个ODE和初值，
所以a严格相同。显式(8)在这一开领内也是同一个角解析Cauchy问题的解。
唯一性先给相同II，(21)再给相同空间位置。
因此新旧图在开重叠上完全一致，全部Cartesian jet匹配。

保留rho<=rho_0的整个圆盘后，
材料域是一个真实闭圆盘rho<=rho_0+delta，只有外面一条边界。
中心的光滑度与正则性由(9)–(10)已付，不用极坐标极限猜测。
族A(t)=1-t/5给整个[0,1]上的共同C-infinity族。

在rho>=rho_0+3delta/4，a''=0、a为正斜率仿射，
且C>0，所以这是实际有限平坦领，II为非零秩一。
出口的B=a'满足9/10<B<1，锥角在(9pi/5,2pi)中；
它不是平面环域，也不是当前圆柱核的小锥角。

## 6. 完整新帽的全时间嵌入

以显式(8)在固定材料圆盘rho<=3/10上的延伸为共同参考B_A。
§3证明每张B_A嵌入，且A的区间紧；
它们在材料Cartesian(xi,eta)中有共同正的全局弦长下界gamma>0。
具体理由是：微分的最小奇异值有统一正下界，
二阶导数有统一上界，从而近对角点对有统一弦长界；
远离对角线的点对连同A参数组成紧集，单射性给正距离下界。

在新增外领rho>=rho_0，两图从同一位置和框架起步。
(19)的共同解析球与(18)给L,M,C的统一界L_max,M_max,C_max。
参考图在rho<=3/10的两个主曲率均小于4/3。
由(21)和角方程积分，可取与delta无关的常数K，使

$$
|F_\rho-(B_A)_\rho|+|F_u-(B_A)_u|\le K\delta .
\tag{23}
$$

例如径向一项只需L_max+2，
角向一项只需3+M_max。
转成(xi,eta)导数时，rho>=rho_0=1/4，
坐标系数有共同有限上界。
内圆盘差为0，且开重叠使全图差光滑；
故存在K'使整个材料圆盘上的一阶差<=K'delta。
把delta再缩小使K'delta<gamma/2，
沿材料Cartesian圆盘中的直线段积分差，
便得新完整帽的全局空间弦长下界gamma/2。
因此所有A的整个新帽都嵌入。

同样，中心原图解析有有限Hessian；
外领由(21)及角方程给实际二阶导数的统一界，
不含截止高阶径向导数。
材料Cartesian圆盘凸，边界最近点采用可行方向的一侧极小条件，
所以Taylor与弦长界给整个新帽某个统一正reach。
本稿未把该常数算成0.03D或其他归一比例，也不把旧环带reach移过来。

## 7. 全E(3)非全等及接口的真实位置

整个原圆盘K=1。
由(17)可知a_delta>=sin rho；
在rho>rho_0+delta/4时psi<1，故

$$
K=\frac{\sin\rho\,\psi}{a_\delta}<1 .
\tag{24}
$$

因此完整新帽中的K=1集合，恰是半径rho_0+delta/4的共同球面度量圆盘。
其中心是到该集合边界的内在距离达到最大值的唯一点：
距离等于rho_0+delta/4-rho。
任意两个完整帽之间的欧氏全等都必须映这一个内在中心到中心。

在中心，两个主曲率绝对值的无序集合是{A,1/A}。
A属于[4/5,1]时该集合唯一确定A，
所以不同A的完整帽不可能全E(3)全等，包括反射。
这没有提供任何固定开H；
(10)只固定一个点和一阶框架，不能充作握持区。

端口的实际位置由(14)、(21)确定，完整II和材料对应也已固定。
本稿没有把某个A的端口平移到期望高度后宣称已经匹配其他时间。
任何随后使用的整体位置或材料角翻向，都必须纳入真实接合数据。

## 8. 与当前固定H圆柱族之间仍存在的匹配缺口

当前固定H圆柱-鞍领-平坦领实例的末端斜率为小正数；
本帽向外的斜率为B_cap>9/10。
若连接面从外部进入帽的中心，径向坐标反向，
目标斜率应为-B_cap，而不是+B_cap。
即使整体缩放帽来匹配端口周长，这个斜率符号和数值仍不改变。

在相同2pi材料周期下，该径向桥的Gauss曲率积分应为

$$
\int_{\rm bridge}K\,dA=2\pi(B_{\rm core}+B_{\rm cap}) .
\tag{25}
$$

所以它必须包含净正总曲率和径向斜率转折；
纯平坦或仅Q>=0的负曲率延拓不能代付。
选择角翻向来保持整体法向定向也不能改变这个径向事实。

此外，还必须匹配整个圆周每个时间的真实位置、框架和两jet。
当前固定H核的局部bump是非解析角数据，
本帽的输入族及其(19)延拓则是角解析。
本稿没有证明两组边界函数相等，
也没有把有限参数A自由度冒充解决一个全函数边值问题。
需要一个真正的中段、可控逆向边值机制或新的退化接口才能完成该步。

这一新接口支付的是：正则中心、实际正K有心帽、
同一材料度量、全圈位置与全jet有限平坦外领。
它仍不能宣布当前有边模型已经闭合，未付宏观位移或整体reach。

## 9. 证据身份

本稿只有显式微分、已审解析存在接口的逐项应用和完整几何证明，
没有新的数学程序运行声明。
中心正则、全圈闭合、正C条带及两类单值性均须独立全文审查。
旧稿的程序回执不充作本帽的执行记录；后续修订另存新文件。
