# R938 — 原完整来源的有限偏移、真实交点像及实际 carry 读取

日期：2026-11-20。**状态：以下同一来源的有限类定位、完整核和实际左行下降已证明；没有判定全部给定陪集的有限类，也没有把选定行的通过认成完整 p³。无数学数值执行。**

本注接 R928、R934、R936、R937 及其 full-J／相继水平附录。
它将 R936/R937 的已指定自然陪集扩大到原全来源中的准确平方／立方偏移，
并把其余偏移定位到原十九角曲面上的完整有限交。
R750 已付全来源的单个曲线值及残余除子主部；
R787 已付全平方／立方来源和逐角乘法帽；
R888 已付合法 quartic 因子提升的差属于全立方来源。
这里不重复那些结论，也不把旧范围的原 r_src=3、tau=1 搬到当前负 fringe。

## 1. 固定原输入与同一给定基点

保 R934 的同一个原整 M、P134、实际 g、四十 charge、十九角和完整来源。
在 R495 的光滑有理曲面 X 上记

\[
 C=(F),\quad \kappa=C^2,\quad
 \mathcal H_i=H^0(X,\mathcal O_X(iC)),\quad
 \mathcal W=H^0(X,\mathcal O_X(\mathcal B_D))
             =\overline{\mathcal W}_D,\quad
 d_D=\mathcal B_D\cdot C.                                      \tag{1}
\]

等号采用 R680 §2 的原显示来源平凡化，保全部固定分母和每个角帽。
C 是几何整 Cartier 曲线，物理点 P_C=(0,1) 光滑；
e=EF 是同一 H1 截面，e(P_C) 非零。H_i 及 W 始终是完整原空间。

仍取

\[
 \bar P=t^{r_{\rm src}}F^4q,\qquad
 \jmath(G)=qt^2G\in\mathcal W\quad(G\in\mathcal H_3),             \tag{2}
\]

其中 q(P_C) 非零，q 和 F 只带原已付的固定 d 分母。
返回指数是 2，不改成源指数 r_src。窗口是

\[
 \begin{gathered}
 s=2h+d_0+2,\quad 1\le d_0\le13,\quad
 J=s-2=2h+d_0,\quad T=J-13,\quad L=\ell-2,\\
 h>21,\quad h<T\le2h,\quad T-h>\kappa,\quad
 T-h\le L\le h,\quad 2h+L>J,\\
 \tau=r_{\rm src}+2h-s\ge2 .
 \end{gathered}                                                \tag{3}
\]

需要 R936 的非零行时另保其低 tau 门；
需要 R937 时另保其高 tau、m 和端点门，本注不扩大这些精度范围。

对同一个整 P 取 R491/R932 已合法返回原预算的 factor lift

\[
 P^{\rm fact}=t^{r_{\rm src}}\widetilde F^4\widetilde q,\qquad
 \Delta=(P-P^{\rm fact})/p\in\mathcal W_{D,\mathcal O}.            \tag{4}
\]

固定给定陪集 R_b+jmath H3，定义

\[
 R^\flat_b=\overline{R_b+\Delta}\in\mathcal W,\qquad
 B=R^\flat_b/(qt^2).                                          \tag{5}
\]

P+pR=P^fact+p(R+Delta) 是完整整恒等式；Delta 的下一位没有删掉。
B 只先在 P_C 邻域取 Laurent germ，不预设其属于 H3。
R_b 从始至终不因想消掉偏移而改成另一个陪集。

## 2. 返回乘子给真正有效的全球除子

将同一 qt² 看作两个原截面线束之间的有理乘子：

\[
 j\in k(X)\otimes
       \mathcal O_X(\mathcal B_D-3C).
\]

**引理 1。** j 是原线束的非零全球正则截面，且

\[
 E_j=\operatorname{div}(j)\ge0,\qquad
 E_j\sim\mathcal B_D-3C,\qquad C\not\subset E_j.                 \tag{6}
\]

在 P_C 的原框中，E_j 的方程是 q t²，故其局部理想为 (t²)。

**证明。** F³ 与 e³ 都属于 H3。由完整返回 (2)，jF³ 和 je³
都是 W 的全球截面。F 的零除子是 C；
C 几何整且 e|_C 不恒零，所以 F³、e³ 没有共同素因子。
在任一 X 的素除子上，至少一个 H3 截面的消失阶为零。
其 j 倍正则便迫 j 在该素除子上无极。
X 光滑、因而正规，有理线束截面无余维一极即为全球正则。
q(P_C) 是单位，t 不在 C 的泛点为零，所以 C 不包含于 E_j。
所有这里的乘法都是原截面乘法，不将 qt² 当作无角帽的函数。证毕。

于是

\[
 E_j\cdot C=d_D-3\kappa.                                      \tag{7}
\]

这不是以 P 的 residual divisor 直接替代 E_j。
原 P 含四个 C，而当前返回空间是 H3；其线束差恰为 (6)。

## 3. 全平方／立方原来源及其零角

对 m=2,3 定义

\[
 \mathscr D_m
   =F^mH^0(X,\mathcal O_X(\mathcal B_D-mC))
   =\{R\in\mathcal W:\operatorname{div}_{\mathcal B_D}(R)
                                  \ge mC\}.                  \tag{8}
\]

它们是原全来源的准确子空间；不只取 jF²H1 或一组 native 列。
在原固定 d 清分母后，(8) 等价于被同一个 primitive F^m 整除，
同时保剩余因子的全部真实 Gauss 帽。
此处不对物理 M 的像作饱和，也不从模 p 的成员性免费宣称任意
特殊整 factor lift 可用。

只需重读 R787 的零角机制。当前 v0(F)=-3，原 W 有 v0(R)>=-2。
若 R=F^mH，则

\[
 v_0(H)\ge3m-2,\qquad
 v_0\!\left(\sum_{n\ge0}H_n(t)Y^n\right)
       =\min_n(4\operatorname{ord}_tH_n-n).                    \tag{9}
\]

所以在原 t=0 正则的系数环中，

\[
 \mathscr D_2:\quad H=tH_1,\qquad
 \mathscr D_3:\quad H=t^2H_2.                                 \tag{10}
\]

这一步使用 n>=0 的真实多项式来源；不是从物理支的一阶零推出
整条纤维整除。固定 d 分母在 t=0 是单位，不改变结论。
其它十八个角继续由 (8) 保留，未放宽到只满足 (9) 的大空间。

相应的原归一化偏移满足：

\[
 \begin{array}{c|c|c}
 R & B_R=R/(qt^2) & \text{在 }C\text{ 上的准确消失}\\ \hline
 \mathscr D_2 & F^2H_1/(qt) & B_R|_C=(EB_R)|_C=0\\
 \mathscr D_3 & F^3H_2/q & B_R|_C=(EB_R)|_C=(E^2B_R)|_C=0 .
 \end{array}                                                 \tag{11}
\]

第一行至多一阶 t 极；第二行在 P_C 的整个二维邻域正则。
这一区别在高 normal 的末位不能丢。

## 4. 两个完整有限交及真正来源像

定义完整闭子概形

\[
 Z_m=E_j\cap mC\quad(m=2,3).                                  \tag{12}
\]

因 E_j 与 C 没有共同分量，Z_m 是 X 上的零维完整交，且

\[
 \operatorname{length}_k Z_m=m(d_D-3\kappa).                  \tag{13}
\]

长度按剩余域次数计，保重数、奇点、非约化交点、
全部有限点、无穷点及十九角的例外分量。

**定理 1。** 原全来源的限制映射具有准确核

\[
 \boxed{\quad
 \ker\{\mathcal W\longrightarrow
       H^0(Z_m,\mathcal O_X(\mathcal B_D)|_{Z_m})\}
    =\jmath\mathcal H_3+\mathscr D_m .\quad}                   \tag{14}
\]

**证明。** j 与 F^m 是正则序列。扭入 B_D 的完整 Koszul 列为

\[
 0\longrightarrow\mathcal O_X((3-m)C)
 \longrightarrow
 \mathcal O_X(3C)\oplus\mathcal O_X(\mathcal B_D-mC)
 \xrightarrow{(G,H)\mapsto jG+F^mH}
 \mathcal I_{Z_m}(\mathcal B_D)\longrightarrow0.               \tag{15}
\]

R495 的 H1(X,O(aC))=0 对 a=1 和 a=0 均已付。
取全球截面，(15) 的最后映射满射。
再用 I_Z(B_D) 是限制映射的核即得 (14)。证毕。

因此

\[
 \mathcal W/(\jmath\mathcal H_3+\mathscr D_m)
 \simeq
 \operatorname{im}\{\mathcal W\to H^0(Z_m,\mathcal O(B_D)|_{Z_m})\}.
                                                                    \tag{16}
\]

右侧是全部原列的实际像，**没有换成 Z_m 的全截面空间**。
没有在此假设 H1(B_D-mC)=0、任意主部可赋或各闭点坐标独立。
特别，有限长度 (13) 不等于已经证明的商维数。

## 5. 原四个低门消掉物理点的整个厚分量

令 W_low 为原四个 t² 低行通过的线性来源空间。
在 tau>=2 时，R934(11) 的自然四目标均为正则级数。
将同一公共 U、q 的 Euler 三角单位及 charge 四十完整逆回后，
给定 R_b^flat 通过这四个低门，当且仅当

\[
 (E^iR_b^\flat)(t,g(t))\equiv0\pmod{t^2}
 \quad(0\le i\le3).                                         \tag{17}
\]

这里在取低行之前没有除 t²。q(P_C)、U(0) 非零确保原三角变换
在该短窗口可逆，所以 (17) 仍是原低行门，不是另加条件。

g 与同一 C 分支 psi 的差从 t^h 起，h>2，
故 (17) 等价于沿 psi 的四式。在完成局部环

\[
 \widehat{\mathcal O}_{X,P_C}\simeq k[[t,F]]
\]

中，E(t)=0，EF 为单位。按 F 次数至三的导数矩阵是三角矩阵，
对角为 1,e,2e²,6e³，均可逆。因此

\[
 \boxed{\quad
 R\in W_{\rm low}
 \ \Longleftrightarrow\
 R\in(t^2,F^4)\widehat{\mathcal O}_{X,P_C}.\quad}              \tag{18}
\]

只用了有限四阶 Taylor；没有在正特征使用无限 log/exp。

由引理 1，Z_m 在 P_C 的完整局部代数为

\[
 \mathcal O_{Z_m,P_C}
      \simeq k[[t,F]]/(t^2,F^m),\qquad
 \operatorname{length}_k\mathcal O_{Z_m,P_C}=2m.               \tag{19}
\]

m=2,3 时，(18) 在 (19) 上为零。
记 Z_m^away 为有限概形 Z_m 去掉这一个完整 P_C-primary 分量后的
开闭子概形，则

\[
 \boxed{\quad
 \operatorname{length}_k Z_m^{\rm away}
      =m(d_D-3\kappa-2).\quad}                                \tag{20}
\]

物理原点以外的全部分量均留在这里；不能只取普通有限根，
也不能删去其它零纤维点、无穷分量或角点上的 nilpotents。

jH3 本来属于 W_low。由 (10)，D3 全部属于 W_low；
D2 则仍须交回 W_low。将 (14) 限制到低门来源得到

\[
 \boxed{\quad
 \ker\{W_{\rm low}\to
 H^0(Z_m^{\rm away},\mathcal O(B_D)|_{Z_m^{\rm away}})\}
 =\jmath H_3+(\mathscr D_m\cap W_{\rm low}).\quad}             \tag{21}
\]

相应目标仍只取实际像

\[
 \mathcal A_m^{\rm low}
  =\operatorname{im}\{W_{\rm low}\to
        H^0(Z_m^{\rm away},\mathcal O(B_D)|_{Z_m^{\rm away}})\}.
                                                                    \tag{22}
\]

旧 R872 后继已讨论首 t 多项式的全有限类刚性；
本注不将 (18) 的局部三个剩余系数重新登记为自由参数。

## 6. 固定 P 的准确有限类及合法提升不变性

本节 beta_m 是下述几何限制类，不是旧首 Bockstein 的页编号。

对已通过低门的原给定陪集，定义

\[
 \boxed{\quad
 \beta_m(P;R_b+\jmath H_3)
     =R_b^\flat|_{Z_m^{\rm away}}\in\mathcal A_m^{\rm low}.
 \quad}                                                       \tag{23}
\]

它确实来自同一原 R_b+Delta 的完整来源截面。
换陪集内基点 R_b→R_b+jG 不改变 (23)。
由 (21)，

\[
 \beta_m=0
 \ \Longleftrightarrow\
 R_b^\flat=jG_b+V_m,\quad
 G_b\in H_3,\quad V_m\in\mathscr D_m\cap W_{\rm low}.           \tag{24}
\]

这是准确的全球分解，不只是物理支的 F^m 整除。
m=3 时交 W_low 可省，m=2 时不可省略。

再比较两种已经合法返回原整来源的 factor lifts：

\[
 \widetilde F'=\widetilde F+pA,\qquad
 \widetilde q'=\widetilde q+pQ_1 .
\]

完整整商 D_fact=(P'^fact-P^fact)/p 属原整 W；
约化后

\[
 \overline{D_{\rm fact}}
 =t^{r_{\rm src}}
      (4F^3q\,\bar A+F^4\bar Q_1)
 \in\mathscr D_3\subset\mathscr D_2.                           \tag{25}
\]

这里完全沿用 R888 的原格整除论证；r_src 保当前实际值。
(10) 也给此差在 W_low 中。两 lift 的 F、q、j、E_j、Z_m 模 p 相同，
而 R_b^flat 相差 (25)，所以

\[
 \boxed{\beta_2,\ \beta_3
        \text{ 均与合法 factor lift 的选择无关。}}            \tag{26}
\]

未断言任意 A、Q1 可实现；xi 的同步变化和完整 p²S 仍按 R888 保留。

## 7. 已有真实非零行下降到这两个实际有限像

### 7.1 R936 的完整双 jet 行只看 beta2

在 R936 的
2<=tau<=d0+1、K=2h+tau−2<J 及 K+e+>3kappa 门内，
实际 lambda+ 来自完整 H0(C,N³(−Z+)) 的真实列。
对任意通过低门的 R，令 B_R=R/j，并定义

\[
 \ell_2(R)=\lambda_+\big((E-3b)B_R|_C\bmod t^J\big).           \tag{27}
\]

该式的两个前缀正是 R934 的完整逆 Taylor 读取。
B_R 至多二阶 t 极，3h−2>J 已付，不能只用齐次差公式。

lambda+ 杀 jH3 的 (27)。由 (11)，(27) 也杀 D2∩W_low。
故 (21) 给一个由原真实行唯一下降的函数

\[
 \bar\ell_2:\mathcal A_2^{\rm low}\to k,\qquad
 \bar\ell_2(\beta_2)=\ell_2(R_b^\flat).                         \tag{28}
\]

不是在 Z2^away 上另任选一个局部 left row。
R936 对当前固定输入的实际行值准确为

\[
 \boxed{-11\,U_*(0)/a-\bar\ell_2(\beta_2).}                    \tag{29}
\]

特别，beta2=0 已足以使原固定 forcing 真非零；
不再必须要求 R_b^flat 本身属于 jH3。
非零 beta2 仍可能落在 bar-ell2 的核，或准确抵消 (29)，
本注没有把这些可能性删掉。

R937 附录的 J>3kappa 低 tau 行同理：使用该附录实际 lambda0、lambda1
对 B_C、EB_C 的读取，(11) 仍将全部 D2 偏移杀掉。

### 7.2 R937 的完整 normal 行只看 beta3

保 R937 的
d0+2<=tau<min(h+2,ell)、n=h+tau−2、m=n+1<=min(2h,h+L)
及 n+2e+>3kappa。
它的真正全四行函数 Lambda2 已证明杀整个 jets(H3)。

对一般 R∈W_low，仍定义

\[
 \ell_3(R)=
 \Lambda_2\big(
 B_R(t,g),EB_R(t,g),E^2B_R(t,g),E^3B_R(t,g)
 \big),                                                       \tag{30}
\]

前三项只取原 J，末项只取原 L。
**对一般 B_R 不将 (30) 替成 Q+B_R|C**；
尤其 tau=h 或 h+1 的末位仍可能读到其二阶极带来的 Taylor 项。

若 R∈D3，则 (11) 给 B_R 在 P_C 整个邻域正则。
因此 R937 对正则来源的同一有限逆 Taylor 合法到 m<=2h，
(30) 等于其 lambda2 对

\[
 \big(E^2-(6b-1)E+3b(3b-1)\big)B_R|_C
\]

的读取。三个限制由 (11) 全为零，所以 ell3(D3)=0。
它也杀 jH3，故得到真正下降

\[
 \bar\ell_3:\mathcal A_3^{\rm low}\to k.
\]

原固定输入的实际值为

\[
 \boxed{\ c_2-\bar\ell_3(\beta_3),\qquad
 c_2=\frac{28}{a}\zeta_0^{-s}\widehat u_0^{\,3}e_0\ne0.\ }     \tag{31}
\]

于是 beta3=0 即足以保留 R937 的实际非零；
原条件 B∈H3 和已付 native F4 尾方向是其子情形。

附录的 successive 门
J+e+>3kappa、n+e+>2kappa 也适用同一 D3 扩张：
其 Pi 的输入来自 B_C、EB_C，故对 D3 为零，
剩下的 normal 读取由 (11) 为零。
附录 J>3kappa 的高 tau 门则在零双 jet 后使用同一 e²H1 行；
D3 偏移既不改双 jet，也不改该 normal 行。
每个兼容 G0 的同 H1 自由仍被原已付行杀掉，没有挑一个方便的 G0。

## 8. 与原 p／p² 方程、beta1 和受限 S 的准确关系

(23) 是给定 P、R_b 的类；它没有先假定存在一个完整解。
如果当前给定陪集包含完整 p³ 解，则在相应真左行门下，
原选定行的必要条件准确为

\[
 \bar\ell_2(\beta_2)=-11U_*(0)/a
 \quad\text{或}\quad
 \bar\ell_3(\beta_3)=c_2.                                     \tag{32}
\]

所以该给定类不能为零，其抵消必须发生在 (20) 的全部非物理分量中。
这不是把物理高轴或 factor lift 当作可自由调节的输入。

进一步的实际问题是：原第一／第二页方程允许的 R_b^flat，
在 (22) 的真正来源像中是否能满足 (32)。
两组完整同 P 的 p³ 解之差仍须落在原 ker beta1，
并由同一个允许的 S 差补偿；只有这个完整条件支付后，
才能把其有限类之差拿来讨论。
单独的低门、(23)、(24) 或 (32) 都不提供 beta1=0 的充分性。

对一个已经确定的 R，剩下的完整下一页继续逐字为 R928(31)：

\[
 y_{P,R}=-M(P+pR)/p^2\bmod p
          \ \in\ \bar M(\text{原允许的 }S\text{ 来源}).       \tag{33}
\]

全部未选的行、三十九 carry、原 theta 高尾以及受限 S 留在 (33)。
本注只将其前面已经出现的真实 affine 偏移，准确定位到 (22)；
未以有限商的识别替代其实际评价。

## 9. 实际第一修正已如何决定这两个有限行

[完整原页读取证明](../notes/2026-11-20-original-finite-offsets-actual-affine-carry.md)
继续同一个实际整 P、R 及合法因子提升。假定已经通过
M(P0+pR0)∈p²Γ；原三条十三尾 C0、C1、C2 正是原 affine carry
残差 U1、a⁻¹U2、2a⁻²U3，没有自由添加新尾。
以 q0,q1,q2 为同一 charge40 读取，r1=q1/q0、r2=q2/q0，
beta=U(w(t))⁻¹(w(t)/t)^(s−13)/q0，完整三角单位逆给

\[
\begin{aligned}
e_0&=t^T\beta\widetilde C_0,\\
e_1&=t^T\beta(\widetilde C_1-r_1\widetilde C_0),\\
e_2&=t^T\beta\{\widetilde C_2-2r_1\widetilde C_1
 +(2r_1^2-r_2)\widetilde C_0\}\pmod {t^J},\qquad
e_3=0\pmod {t^L}.
\end{aligned}
\]

原真实待实现目标为 f=−e，所以低 tau 的 (29) 恰为
−λ₊[t^T beta{C1−(r1+3b)C0}]；只读前两条实际带各
12+tau−d0∈[1,13]位。高 tau 的 (31) 恰为

\[
-\lambda_2\!\left[t^T\beta\left\{
\widetilde C_2-(2r_1+6b-1)\widetilde C_1+
(2r_1^2-r_2+(6b-1)r_1+3b(3b-1))\widetilde C_0
\right\}\right],
\]

每条带只读 max(0,m−T)=max(0,tau−h−d0+12)≤12位。
这里的 beta 是实际单位，与前节几何 beta_m 分清；
全部 q 导数、w/t 幂、xi、U0/P134 和真正除p输入仍保。

**若 m≤T，第一修正的 p² 方程自身已经迫
bar-ell3(beta3)=c2≠0、beta3≠0（条件是第一修正确实存在）。**
故这段不能再期待同一页方程把 away 类消成零；它已准确给出
抵消 R937 自然单位的值。若另由全原来源证明 beta3=0，才得到矛盾。
此结论没有证明第一修正存在或完整p³存在。

完整证明还付这两行在全 K2=ker(beta1) 上不变；m≤T 时高行甚至
在整个K1的实际有限像上为零。一般范围不把K1赋成K2，
原 S 不能改变此三 carry，但其完整后页和受限差格仍须联立。
继续处理的是这些真实 carry 行与全来源/下一页条件的联合，
并非重复自然陪集的单位非零。

审阅：deep推导，root/theta全文核全源Koszul、所有低门厚分量、
实际行下降，并回查R928完整三carry尺度、charge单位逆和精度端点。
无数学执行。整合前主稿SHA256
`b3957c6a0322913459fbbd349aa10b297b9d0279de59a3c788134e975a6bd6fc`；
完整原页读取稿SHA256
`b1c8ca84d9c293d35d33b8832e7f9b20bf2ffd1c8f15b2694da00e509dcda554`。

