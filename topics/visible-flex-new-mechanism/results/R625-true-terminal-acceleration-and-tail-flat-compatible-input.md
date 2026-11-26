# R625：原尾端加速度必要门与保持唯一支的尾平明式输入

2026-11-27。**已证明：真 $A_s=M$ 在八矩返回和双末速度零处给出一个完整因式，
从而得到两侧首层能量的准确二阶末端方程；R624 的增量乘 $\cos^2u$ 后，
保留中心三阶控制、全程合法盒、动能余量与唯一标量支，并准确移除该增量造成的大尾加速度。**

新输入支付的是原尾二阶必要符号和 R624 的首层端常数相容；
两条完整二阶末方程、整条首层轨道、真实 $A(L)=0$ 与原有限宽度 BVP 仍须求解。
本稿不把假设的返回端重置成试验曲线的实际尾历史。

## 1. 原八密度在完整返回端的准确因式

沿用 [R624](R624-free-center-terminal-constants-and-compatible-analytic-input.md)
第 1 节和 [R619](R619-free-center-leading-energy-and-true-memory-local-flow.md)
的同一首层量词；二阶微分只作用于准确光滑首层解，不对 $C^0$ 渐近余项求导。
设在末端

$$
A(L)=0,\qquad h_s(L)=k_s(L)=0,
$$

并在本节把末端数据简写为

$$
h>0,\quad k,\quad\eta,\quad d=h\eta-k,\quad q_0=1+d^2,
\quad a=h_{ss}(L),\quad b=k_{ss}(L),\quad z=hy+d,
\quad Q=1+z^2.
\tag{1}
$$

这里 $q_0$ 是原几何量；后面的增量参数另记为 $q$。
原 $d_s=h_s\eta-k_s/2$ 在末端为0。
令

$$
e=k^2+2kd-1,\qquad c=(d+k)(kd-1).
$$

从 [R609](R609-true-integral-histories-and-kinetic-input.md) 原八密度直接得到

$$
M_{p_2}=-kh/2,\quad M_{p_1}=-kd,\quad
M_{t_1}=e/8,\quad M_{s_1}=ed/(4h),
$$
$$
M_{r_1}=eq_0/(8h^2),\quad M_{s_0}=cd/(4h^2),\quad
M_{r_0}=cq_0/(8h^3).
\tag{2}
$$

$M_{p_0}$ 仍保留在原系统，但不出现在 R619 的最高 profile 多项式 $C_A$ 中。
因此 $C_{A,s}=C_M$，且

$$
8h^3 C_M=
cq_0+h(eq_0+2cd)y+3h^2ed\,y^2
+h^3(k^2+4kd-1)y^3+kh^4y^4.
\tag{3}
$$

因 $c+q_0k=de$，右边准确因式化为

$$
(q_0+2hdy+h^2y^2)(kh^2y^2+ehy+c).
$$

再以 $z=hy+d$ 代换，第二因子为
$kz^2+(k^2-1)z-k=(kz-1)(z+k)$，所以

$$
\boxed{C_M(y)=\frac{Q(y)}{8h^3}(kz-1)(z+k).}
\tag{4}
$$

原 $V=-2C_A-Q[\gamma(y+\eta)-\upsilon/2]/(4h^3)$ 在此末端为0。
又 $y+\eta=(z+k)/h$，故真正的时间导数为

$$
\boxed{V_s(L,y)=-\frac{Q(y)}{4h^3}
 \left[(z+k)(kz-1+a/h)-b/2\right].}
\tag{5}
$$

(4)(5) 同时包含原历史和末加速度，不能只微分显式速度项而冻结 $A$。

## 2. 两条完整二阶末方程与严格符号门

固定 $C_1=0$、$B_c>0$ 和 $C_2<0$，并假设首层端常数已相容：

$$
C_0=-C_2\frac{h^2}{q_0}.
\tag{6}
$$

令

$$
P_{a,b}(z)=(z+k)(kz-1+a/h)-b/2.
$$

由于 $V(L,y)=0$，完整能量的所有含 $V$ 项在二阶式中消失，留下

$$
B''_\pm(L)=2\sum_iw_iQ(\pm c_i)V_s(L,\pm c_i)^2
=\frac1{8h^6}\sum_iw_i[1+(d\pm hc_i)^2]^3
 P_{a,b}(d\pm hc_i)^2.
\tag{7}
$$

这里消失的理由是准确的末 $V=0$，而非在一般点删去 R624 的交叉项。
另一方面 $d_{ss}(L)=a\eta-b/2$，由首层式和 (6) 有

$$
\begin{aligned}
B''_\pm(L)
&=2C_0d(a\eta-b/2)+2C_2ha\\
&=\frac{2C_2h}{q_0}\left[a(1-dk)+\frac{hdb}{2}\right].
\end{aligned}
\tag{8}
$$

两条准确二阶末方程因而是

$$
\boxed{\sum_iw_i[1+(d\pm hc_i)^2]^3P_{a,b}(d\pm hc_i)^2
=\frac{16C_2h^7}{q_0}\left[a(1-dk)+\frac{hdb}{2}\right].}
\tag{9}
$$

若 $k\ne0$，则 $P_{a,b}$ 是首项系数为 $k$ 的二次多项式，
不可能在六个不同的 $d\pm hc_i$ 处全部为零。
$w_i>0$ 和 $1+(d\pm hc_i)^2>0$ 使 (9) 两侧平方和均严格正。
于是得到严格的必要门

$$
\boxed{a(1-dk)+\frac{hdb}{2}<0\qquad(k\ne0,C_2<0).}
\tag{10}
$$

当 $k=0$ 时只能一般地推出非严格 $\le0$，必须另检查平方是否恒零。
(10) 不能替代两条 (9)：它只消除一个明显的末端二阶符号冲突。

## 3. 具体更换增量，保全部中心 jets

保留 R624 的同一准确负中心、$a_0=1-r$、$L=3$、

$$
u=\pi x/2,\quad A=9a_0/\pi^2,\quad
h(x)=1+A(1-\cos\pi x),
$$
$$
k_b(x)=-\frac85\sin u+\frac{8/5-3/\pi}{3}\sin3u,
\quad\psi(x)=-4\sin u\sin^2(20u).
$$

把 R624 的增量改为

$$
\boxed{k_q^\flat(x)=k_b(x)-q\psi(x)\cos^2u,
\qquad 0\le q\le1/15,}
\tag{11}
$$

eta 仍是这条新曲线的真实积分
$\eta_q^\flat(x)=\int_0^x k_{q,x}^\flat/(2h)\,dt$。
此处的上标只是标记新输入，不改变原状态变量。

在中心 $\psi=O(u^3)$ 且 $\cos^2u=1+O(u^2)$，所以
$\psi\cos^2u-\psi=O(u^5)$。因此原初速和真实三阶控制完全不变：

$$
v=-\frac12,\qquad a_0=1-r,\qquad
j_0(q)=j_b+\frac{400\pi^3}{9}q,
\qquad f_0=-\frac{a_0\pi^2}{9}.
\tag{12}
$$

在末端 $u=\pi/2$，有
$\sin20u=O(\pi/2-u)$、$\cos u=O(\pi/2-u)$，
故 $\psi\cos^2u=O((1-x)^4)$。
增量的值、一阶、二阶和三阶导数都在那里为零。
相较之下，原 R624 增量使

$$
\Delta k_{ss}(L)=3200q(\pi/6)^2>0\quad(q>0).
$$

新输入准确移除这一增长，末端物理加速度现在是

$$
\boxed{a_L=-a_0,\qquad
b_L=k_{b,ss}(L)=\frac{8\pi^2}{45}-\frac\pi4.}
\tag{13}
$$

末双速度仍准确为0。

## 4. 全段合法性、动能和唯一标量支的完整继承

令 $\Delta k_q^\flat=-q\psi\cos^2u$、$\Delta k_q=-q\psi$。
因 $0\le\cos^2u\le1$，R624 的全域负曲线顺序给

$$
0\le\Delta k_q^\flat\le\Delta k_q,
\qquad k_b\le k_q^\flat\le k_q\le0.
\tag{14}
$$

所以原 $h,k$ 盒不变，且逐点有 $(k_q^\flat)^2\ge k_q^2$。
在同一个 $h,L$ 下，准确得到

$$
\int_0^1(k_q^\flat)^2dx-1-U/L^2
\ge\int_0^1k_q^2dx-1-U/L^2>1/45.
\tag{15}
$$

因为新增量非负、中心为零、最大值不超过 $4q$，
R624 的真实积分分部同样给 $0\le\Delta\eta^\flat\le2q$。
于是 $-11/12<\eta_q^\flat\le2/15$ 和 $|\eta_q^\flat|<1$ 保持。
高度速度同样保持 $|h_s|<11/20$。

唯一需重写的是曲率速度界。
$|\psi_u|\le84$、$|\psi|\le4$、$|(\cos^2u)_u|\le1$，故

$$
|[\psi\cos^2u]_u|\le88,
\qquad
|k_{q,s}^\flat|<\frac{23}{18}+\frac{44\pi}{45}
<\frac{245}{54}<6.
\tag{16}
$$

全部原物理盒仍有严格余量。
乘 $\cos^2u=(1+\cos2u)/2$ 后最高半波频率是43，而非41；
它在单位 x 区间有 $43/4$ 个周期。

新原末 $d$ 准确为

$$
d^\flat(q)=d_b+qD_\flat,
\qquad
D_\flat=\frac{h_L}{2}\int_0^1
\frac{[-\psi(x)]\cos^2u\,h_x(x)}{h(x)^2}\,dx.
\tag{17}
$$

严格有 $0<D_\flat<D<11/5$；严格性来自内部正长度子区间，
不是数值积分的符号判断。
故 R624 的

$$
-11/120<d^\flat(q)<3/4,\qquad
G_\flat(q)=\frac{h_L^2}{1+d^\flat(q)^2}-1>29/20,
$$
$$
|qG_\flat'(q)|<4851/5000
\tag{18}
$$

逐项继续成立。
中心 $V_c,V_{s,c},V_{ss,c}$ 与 $C_2(q)=C_{20}-\kappa q$ 完全不变。
因此相同的两端符号、单调区间和导数论证给

$$
\boxed{\Phi_\flat(q)=B_c+C_2(q)G_\flat(q)
\text{ 在 }[0,1/15]\text{ 恰有一个根 }q_\flat,}
$$
$$
\boxed{-\Phi_\flat'(q_\flat)>8B_c.}
\tag{19}
$$

这里必须评价 (17) 的新 $D_\flat$ 并选 (19) 的同一支；
不能把 R624 的旧数值 $q_*$ 直接当成新曲线的根。
任意 $q\in[0,1/15]$ 都已经有本节严格物理盒和 (15)，
但只有准确 $q_\flat$ 支付准确首层端常数等号。
数值积分/求根的近似值只作为原 BVP 初始输入，须另外报告其评价误差限度。

## 5. 新末几何 jets 严格通过必要符号门

在新曲线末端，令 $K_e=32/15-1/\pi$，则 $k_L=-K_e$。
R624 及 (13) 给

$$
\frac8{15}<a_0<\frac{11}{20},\quad
\frac{49}{25}<h_L<\frac{21}{10},\quad
\frac95<K_e<\frac{11}{6},\quad
\frac{23}{30}<b_L<\frac{37}{36}.
\tag{20}
$$

最后的两条粗界只用 $3<\pi<10/3$ 和 $9<\pi^2<10$。
置

$$
E=\frac{h_Lb_L}{2}-a_0K_e.
$$

由 (20) 分别得到

$$
E>\frac{49}{25}\frac{23}{60}-\frac{11}{20}\frac{11}{6}
=-\frac{257}{1000},
$$
$$
E<\frac{21}{10}\frac{37}{72}-\frac8{15}\frac95
=\frac{143}{1200}.
\tag{21}
$$

原 (10) 的方括号在这组末几何 jets 上为

$$
T=a_L(1-d^\flat k_L)+h_Ld^\flat b_L/2
=-a_0+d^\flat E.
$$

若 $d^\flat\ge0$，由 (18)(21) 有 $d^\flat E<143/1600$；
若 $d^\flat<0$，则 $d^\flat E<2827/120000<143/1600$。
所以整个参数区间准确满足

$$
\boxed{T<-\frac8{15}+\frac{143}{1600}
=-\frac{2131}{4800}<-\frac25<0.}
\tag{22}
$$

因此在准确 $q_\flat$ 的 $C_2<0$ 下，把这些真实几何末 jets
作为待匹配的 $A(L)=0$ 端模板时，(8) 的右边严格为正。
新输入已避免该原尾二阶必要符号冲突。
这句话没有把试验曲线的实际 A 历史末值改成0；
该末模板的两条完整平方等式 (9) 也尚未声称成立。

## 6. 实际输入身份与仍未支付的条件

新十参数是 R624 的 (49) 中将 $q_*$ 换成 $q_\flat$；
全程 k 则按 (11)，并使用真实 $\eta,A,\rho$。
原 R620 三角规范图从这些真实中心 jets 与完整有限宽度正势构造三常规范。
同一 R598 母、$\varepsilon=1/12000$、正势系数1、原单位及所有末门保持。

65个观察节点对最高43半波只有约 $256/43$ 个观察间隔/周期。
这仍只是一份初猜表示；原 C² quintic 曲线重装的误差、真历史差和原 ruling
必须由既定 readout 与配点通过后的正常网格精化实际支付。
不能把本文的高阶尾平身份移给一条已经变更的数值插值曲线。

准确 (19) 仍只是首层端常数条件，准确 (22) 仍只是二阶必要符号。
全部八个真实尾矩、六 rho、两原 ruling 和整段合法延拓均未因此被解掉。
有原有限宽度根之后，period/pose、闭材料、全域全时嵌入/reach 与宏观幅度仍须继续，
不能以这条更好的输入结束主课题。
