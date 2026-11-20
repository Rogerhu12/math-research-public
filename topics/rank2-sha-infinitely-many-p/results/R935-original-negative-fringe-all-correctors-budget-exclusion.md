# R935：原负 fringe 固定 quartic 的全修正交数与预算排除

日期：2026-11-20。状态：以下必要条件与其明确预算反门已证明；未执行数学计算。

本注接 R895 的同修正交数方法与 R934 的整个固定双 jet。
新的输入是 R934 的负 fringe、全部 1≤τ≤d₀+1，而非 R895 的
r_src=3、τ=1、s=2h+2 特例。
结论作用于同一个原完整 WD 中的所有 R、S，不要求 B∈H3，
不预设 R 或其余类位于任何 F 倍子格。没有扩充中央零条件。

## 1. 原来源、不同的两个指数及实际整提升

沿用 R920、R928、R934 的同一十九角曲面 X、几何整的非边界
Cartier 曲线 C=(F)、原光滑点 P₀=(0,1) 及原 WD。设

\[
p=6s-1>211,\qquad b=\deg_YF\ge5,\qquad
C\cdot f_0=3,\qquad 3b<p,
\tag{1}
\]
\[
\mathcal E=Y\partial_Y,\quad e=\mathcal EF,\quad
e(P_0)\ne0,\quad F(t,0)\ne0,\quad q(P_0)\ne0.
\]

原返回为已经完整支付的

\[
\jmath:\mathcal H_3=H^0(X,\mathcal O_X(3C))
 \longrightarrow\overline{\mathcal W}_D,\qquad
G\longmapsto qt^2G.
\tag{2}
\]

这里返回指数是 2。原 quartic 本身的 t 指数另记 r_src：

\[
\bar P=t^{r_{\rm src}}F^4q\in\overline{\mathcal W}_D.
\tag{3}
\]

保持 R934 的整原方程、d=1+8t 的固定分母框与 primitive 规范。
特别 F、q 在原 k[t,Y,d^{-1}] 中，F 没有整体 t 因子；
F(0,1)=0 而 q(0,1)≠0。同一原 Y 帽给 D≥4b≥20。
另保原 p>D+40、f_D<p 和原固定单位的好素数门。

写实际轴及真实长度

\[
F(t,\bar g(t))=t^h\widehat u(t),\quad\widehat u(0)\ne0,
\quad
J=s-2,\quad T=J-13,\quad L=\ell-2,
\]
\[
h<T\le2h,\qquad T-h>\kappa=C^2,\qquad
T-h\le L\le h,\qquad 1<\ell<s-13.
\tag{4}
\]

本注使用负 fringe 参数

\[
s=2h+d_0+2,\qquad1\le d_0\le13,\qquad
\tau=r_{\rm src}+2h-s,\qquad
\boxed{1\le\tau\le d_0+1.}
\tag{5}
\]

所以

\[
r_{\rm src}=\tau+d_0+2,\quad J=2h+d_0,\quad
2h+\tau\le s-1.
\tag{6}
\]

R815 的完整 nef 界与 C·f₀=3 给

\[
\kappa\ge6b-9\ge21,\qquad h>\kappa,\qquad L>\kappa.
\tag{7}
\]

这些都是同一原分支已经支付的门，不用一个泛型接触假设替代。

取 R491/R932 支付全部 Gauss 帽的同一整因子提升

\[
P^{\rm fact}
 =t^{r_{\rm src}}\widetilde F^{\,4}\widetilde q
 \in\mathcal W_D,\qquad
\overline{P^{\rm fact}}=\bar P.
\tag{8}
\]

若原固定 P 的提升并非 (8)，则定义真整来源

\[
\Delta=(P-P^{\rm fact})/p\in\mathcal W_D,\qquad
R^\natural=R+\Delta\in\mathcal W_D.
\tag{9}
\]

这是同一原自由来源格内的除 p，非只在完成局部环中除 p。
字面恒等式

\[
P+pR+p^2S=P^{\rm fact}+pR^\natural+p^2S
\tag{10}
\]

保留同一个完整物理矩阵、原 P134/U₀、三个十三行带及同一个 S。

以下假定存在原整 R、S，使

\[
\boxed{
M^{\rm orig}(P+pR+p^2S)\in p^3\Gamma_4.
}
\tag{11}
\]

记 \(\mathcal R=\overline{R^\natural}\)。
(9)–(11) 没有把实际修正另投到 H3 或 F 倍理想。

## 2. 全部同 R 的确定分支值

在 P₀ 邻域置

\[
B=\frac{\mathcal R}{qt^2}.
\tag{12}
\]

B 只在这里作为实际有理局部表达式使用；允许其原 t^{-2}
主部，不要求 B 是 H3 截面。全 (11) 先支付 R928 的低行门，
再支付三个长度 s 的实际 Wi 行及第四长度 ell 的行。
因此 R934 的完整逆 Taylor 可直接用于 (12)，给

\[
B|_C=0\pmod{t^J},\qquad
(\mathcal EB)|_C=\mathcal T_P\pmod{t^J},
\tag{13}
\]
\[
\mathcal T_P=
-\frac{11}{a}\,
t^{r_{\rm src}-2}w(t)^{-s}F(t,\bar g(t))^4,
\qquad a\in k^\times.
\tag{14}
\]

这是将 R934 用于原 P^fact 与实际基点 R^natural；无需在
WD/H3 中选择有利的陪集。等价地，在 R934 的表示中取 G=0，
整个 B 仍是 (12) 的真实值，而非把 B 赋零。

记 \(\zeta(t)=w(t)/t\in k[[t]]^\times\)。
将 (13) 乘回原 qt²，并对同一来源作一次完整 Euler 乘积法则：

\[
\boxed{
\mathcal R|_C\in t^s k[[t]],\qquad
(\mathcal E\mathcal R)|_C
=t^{2h+\tau}\,A_P(t)\pmod{t^s},
}
\tag{15}
\]
\[
\boxed{
A_P(t)=
-\frac{11}{a}\,q|_C\,\zeta(t)^{-s}\widehat u(t)^4,
\qquad A_P(0)\in k^\times.
}
\tag{16}
\]

确实，

\[
\mathcal E(qt^2B)
=qt^2\mathcal EB+(\mathcal Eq)t^2B.
\]

第二项由 (13) 消到 t^s，而第一项的准确次数是
r_src+4h−s=2h+τ。这里没有把 r_src 换为返回指数 2。

首系数 −11 来自同一原源完整逆 Taylor 中的
−1+8−18。两份二次 eta 项均须保留；
根修正 xi 的合项从 J+τ 起才退出。
短 f3 之所以足够，是原 2h+L>J；
B 的 t^{-2} 主部所生三次 Taylor 余项从 3h−2>J 起。
这些精度门都是 (4)、(5)、(7) 的原已付范围，不能以首项猜测替代。

由 (6)，(15) 中的单位首项实际落在读窗内，故

\[
\boxed{
\operatorname{ord}_{P_0}
 ((\mathcal E\mathcal R)|_C)=2h+\tau<s.
}
\tag{17}
\]

特别 \(\mathcal R\ne0\)。

### 原 epsilon 行的位置与两个端点

原物理 P 的第二 Euler 矩 Wi 首阶是 s+τ；
完整载体另有 w¹³。因此其一次折回的首项位于

\[
\epsilon^3w^{13+\tau},
\tag{18}
\]

系数为原单位
\(6a^2C_0u_0^2e_0^2\)，其中
\(C_0=\mathcal U(0)t_1^{r_{\rm src}}q(0,1)\)。
同源 R 的第四 Euler 行用于消这个实际项。
除 qt² 之后，R934 的自然第四目标从 w^{τ−2} 起；
这是 (18) 的同一项，不能另减一次十三行，也不能将两种标号混同。

(7) 给 ell=L+2>23，而 τ≤14，故 (18) 严格在第四块
长度 ell+13 内。其含 xi 的直接低项从 13+r_src 起，
严格晚于 13+τ。

在 τ=1 时，(17) 的实际首阶是 2h+1=s−d₀−1，
不是旧 R895 的 s−1；仍由整段 J 读取。
在 τ=d₀+1 时，(17) 恰是最后已知的 t^{s−1} 行。
τ=d₀+2 时首项进入 t^s 的未知尾，本证明不再断言它非零。

τ=0 的整个原来源排除已经由 R824 的原零角第十三行增补支付；
它不作为本注的新结论重登。

## 3. 原零角二次帽迫同一修正包含严格 f₀

先在原点读取同一 \(\mathcal R\) 的前三个相对 Euler 值。
R934 的完整自然 f0、f1、f2 在乘回 qt² 后，最低可能阶分别为
s、2h+τ、h+τ；含 xi 的第三行项还要更晚。
因此

\[
\mathcal R(0,1)
=(\mathcal E\mathcal R)(0,1)
=(\mathcal E^2\mathcal R)(0,1)=0.
\tag{19}
\]

原 R335 canonical 列的 t 因子是
\(t^{\lfloor(n+1)/4\rfloor+j}\)。
在 t=0 时只有 n=0、1、2，且 j=0，可能存活。
固定 d 分母在 t=0 为单位，故同一原来源的真实限制为

\[
r_0(Y)=\mathcal R(0,Y)\in k[Y]_{\le2}.
\tag{20}
\]

对二次多项式，
\(r_0(1)=\mathcal Er_0(1)=\mathcal E^2r_0(1)=0\)
迫 \((Y-1)^3\mid r_0\)，从而 \(r_0=0\)。
这里 p>211 保所用 2 为单位。因此

\[
\mathcal R\in t\,k[t,Y,d^{-1}].
\tag{21}
\]

令 \(D_{\mathcal R}\sim\mathcal B_D\) 是该非零原截面的全零除子。
在严格零纤维 f₀ 的一般点，原框中的 t 是 f₀ 的局部方程，
d 为单位；(21) 准确给

\[
D_{\mathcal R}\ge f_0.
\tag{22}
\]

这只减去原严格 f₀ 的一个有效分量。没有说整个总纤维被删除，
没有把 raw R/t 当作仍属于 WD，也没有省去任何吹起中心。
所有十九角仍在同一个 \(\mathcal B_D\) 与有效剩余除子中。

## 4. 两个全局分支均迫 d_D≥s+2

置

\[
d_D=\mathcal B_D\cdot C.
\tag{23}
\]

以下均使用 (15)、(17)、(22) 中的同一 \(\mathcal R\)。

**分支一：C 不在 \(D_{\mathcal R}\) 中。**
此时 \(D_{\mathcal R}-f_0\) 有效且不含 C。
在 P₀，t 是 C 的参数，局部交数至少为 s−1。
其它局部交数均非负，故

\[
d_D-3=(D_{\mathcal R}-f_0)\cdot C\ge s-1,
\qquad d_D\ge s+2.
\tag{24}
\]

**分支二：C 在 \(D_{\mathcal R}\) 中。**
由 (17)，C 在该除子中的重数恰为一：重数至少二将迫
\((\mathcal E\mathcal R)|_C=0\)，与单位首项矛盾。
因此

\[
D'=D_{\mathcal R}-f_0-C
\]

有效且不含 C。在 P₀ 的原单位框中写
\(\mathcal R=tFH\)；这是对两个已知有效分量作局部 Cartier
除法，H 的全局截面意义是 D'，不声称 H 属于 H1 或 H2。
限制到 C：

\[
(\mathcal E\mathcal R)|_C=t\,e|_C\,H|_C.
\]

e(P₀) 为单位，故 (17) 给

\[
\operatorname{ord}_{P_0}(H|_C)=2h+\tau-1.
\tag{25}
\]

于是

\[
d_D-3-\kappa=D'\cdot C\ge2h+\tau-1,
\]
\[
d_D\ge\kappa+2h+\tau+2
=s+\kappa+\tau-d_0.
\tag{26}
\]

由于 \(\kappa\ge21\)、\(d_0\le13\)、\(\tau\ge1\)，
右端至少 s+9，特别也至少 s+2。

所以对原完整 (11) 的任何同源 R、S，

\[
\boxed{d_D\ge s+2.}
\tag{27}
\]

分支二保留了 (26) 的更强门；证明没有先假定或强迫所有修正
进入这个分支，也不要求 R934 的 B∈H3 或任何有限类为零。

## 5. 同一个 quartic 的有效除子预算

令 j 为同一原 \(\bar P\) 的剩余有效除子
沿严格负水平 H₋ 的准确重数。只需 j≥0；
本注不将旧 r_src=3 特例的 j≤2 无证搬来。

由 (3) 和原 fixed frame，

\[
\operatorname{Div}(\bar P)
 \ge4C+r_{\rm src}f_0+jH_-.
\tag{28}
\]

C、f₀、H₋ 是不同的素除子；在它们交点处系数仍真实相加。
q(P₀) 为单位、F 无整体 t 因子，确保 r_src 确实是该表达式
在严格 f₀ 一般点贡献的 t 阶。

原 \(\mathcal B_D\) 对 D≥3 为 nef。
R680 的完整十九重数表给

\[
\mathcal B_D\cdot f_0
 =D-\sum_{\nu=1}^4\mu_{0,\nu}(D)=2,
\qquad
\mathcal B_D\cdot H_-
 =u_D-2c_D=4.
\tag{29}
\]

因此与同一 \(\mathcal B_D\) 相交，并保全部剩余有效分量，

\[
\mathcal B_D^2
 \ge4d_D+2r_{\rm src}+4j.
\tag{30}
\]

代入所有同修正均满足的 (27)，得到

\[
\boxed{
\mathcal B_D^2\ge4s+8+2r_{\rm src}+4j.
}
\tag{31}
\]

若恰属分支二，还可将 (26) 代入 (30)；
(31) 是两个分支共有的必要门。

原 canonical 维数和十九角的准确身份是

\[
N_D=\dim\overline{\mathcal W}_D
 =\sum_{n=0}^D(e_{n+1}+1),\qquad
\mathcal B_D^2=2N_D-2D-17.
\tag{32}
\]

由 (31) 得

\[
2(N_D-2s)\ge2D+25+2r_{\rm src}+4j.
\]

左侧为偶整数，故

\[
\boxed{
N_D-2s\ge D+r_{\rm src}+13+2j
 =D+d_0+\tau+15+2j.
}
\tag{33}
\]

常数 13 来自对 25/2 的准确上取整，不能写成 12。

因此以下是原全部同 R、S 的实际排除：

\[
\boxed{
N_D-2s\le D+r_{\rm src}+12+2j
\quad\Longrightarrow\quad
\text{不存在满足 (11) 的原 }R,S.
}
\tag{34}
\]

未先求 j 时可安全使用 j=0 的较强充分反门。
D、s、ell 及原旗标须已固定；本注不授权事后换成一个便利的
最小 D 或改变原来源范围。

## 6. 两长、三长预算及未覆盖范围

若沿用旧两长松弛

\[
\delta_D=N_D-(2s+\ell),
\]

则 (33)、(34) 分别是

\[
\ell+\delta_D\ge D+r_{\rm src}+13+2j,
\qquad
\ell+\delta_D\le D+r_{\rm src}+12+2j
\ \Longrightarrow\ (11)\text{ 不可解}.
\tag{35}
\]

\(\delta_D\) 可以为负。
若当前采用三个长块的
\(\delta_D^{(3)}=N_D-(3s+\ell)\)，则必须改写为

\[
\boxed{
s+\ell+\delta_D^{(3)}
 \ge D+r_{\rm src}+13+2j.
}
\tag{36}
\]

不能删去左端的 s。
所以 (34) 不自动排除所有三长临界输入，更不证明整个 K1
或指定普通／无穷素数主门。

与 R895 的关系准确是：保相同的全 R 交数方法，但 (15) 的
确定首项在 R934 负 fringe 中给 1≤τ≤d₀+1 的全范围。
r_src=3 代入 (33) 的常数正好是 R895 的 D+16+2j；
旧 r_src=3、τ=1、s=2h+2 本身是 d₀=0 的另一端点，
不被本注冒称为负 fringe。

本注既没有给 τ≥d₀+2 的未知 t^s 尾赋首项，
也没有从局部 −11 单位直接宣称 R928 全局余核非零。
当 (34) 不成立时，原双 jet 兼容、同一 H1、完整受限 S
及其它后页仍须继续判定。

依赖：R335 原 canonical 列；R491/R932 同预算整因子提升；
R680 全十九角 nef 与交数；R815 全 Mori/nef 界；
R895 同修正交数方法；R928 真实选定行；R934 整段固定双 jet。


审阅记录：deep 完整推导，root/global 全文逐式核过同原 WD、合法提升、三条低行、严格纤维与两支交数及准确整数预算；没有数学执行。原定稿 SHA256 `115cac1f3d0c1002bc97e2b8303e4ff669e526cf06e2aa65a29cd212a4a44b8f`。
