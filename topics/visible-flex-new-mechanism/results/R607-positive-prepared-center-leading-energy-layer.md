# R607 prepared 中心两侧最高能量的正四阶相容层

日期：2026-11-26。**已证明：有限阶真实相容；原式纸证，没有科学或符号程序执行。**
本文接 [R603](R603-prepared-leading-energy-and-speed-two-guide.md)、[R605](R605-real-memory-coordinates-and-leading-energy-local-flow.md)，给 prepared 中心的一条显式正支四阶选择。
它支付两条最高能量方程到相同的首个非零阶，并消去下一奇阶差。
不把有限阶相容性称为实际原 ruling 解，也不授中心到 R605 内部正则流的可达性。

## 1. 同一个真实中心与奇偶输入

取 $H>0$，在中心附近令 h 为光滑偶函数、k 为光滑奇函数，
并写物理时间 s 的展开
$$
h=H(1+s^2/2+a_4s^4)+O(s^6),\qquad
k=2s+b_3s^3+O(s^5).
\tag{1}
$$
$\eta$ 始终由同一个原运动学
$$
\eta_s=k_s/(2h),\qquad \eta(0)=0
\tag{2}
$$
取得。A 始终由原 $A_s=M$，使用 R601/R603 的 prepared 中心
$$
A_c=(1/(6H),0,0,0,0,1/(12H),0,1/(8H^3))
\tag{3}
$$
（次序为 $p_0,p_1,p_2,t_1,r_1,s_1,s_0,r_0$）。
所以 $h_{ss}(0)=H,\ k_s(0)=2,\ k_{ss}(0)=0$，
没有把八个历史系数独立选成方便的多项式。

积分(2)给
$$
\eta=\frac1H\left(s+\left(\frac{b_3}{2}-\frac16\right)s^3\right)+O(s^5),
$$
$$
d=h\eta-k=-s+D_3s^3+O(s^5),\qquad
D_3=\frac13-\frac{b_3}{2}.
\tag{4}
$$
于是 R605 的真正坐标满足
$$
\theta=-s+\left(\frac23-\frac{b_3}{2}\right)s^3+O(s^5),
$$
$$
R=H(1+cs^4)+O(s^6),\qquad
c=a_4+\frac{11}{24}-\frac{b_3}{2},
$$
$$
m=h^2-H^2(1+d^2)=2H^2cs^4+O(s^6).
\tag{5}
$$
这里 c 是几何的四阶系数，不是旧 guide 的单调积分参数。

## 2. 真 M 的必要展开

以下都是把(1)(4)代入已付原密度再积分所得；
常数项由(3)固定。
为使计算可逐项核对，列出构成 $C_A$ 所需的全部分量：
$$
\begin{aligned}
p_1&=\frac23s^3+O(s^5),&
p_2&=-\frac H2s^2+O(s^4),\\
t_1&=-\frac18s-\frac1{24}s^3+O(s^5),&
r_1&=-\frac1{8H^2}s-\frac1{24H^2}s^3+O(s^5),\\
s_1&=\frac1{12H}+\frac1{4H}s^2+O(s^4),&
s_0&=-\frac1{4H^2}s+\frac1{H^2}
       \left(\frac13-\frac{b_3}{4}\right)s^3+O(s^5),\\
r_0&=\frac1{8H^3}+O(s^4).
\end{aligned}
\tag{6}
$$
未进入 $C_A$ 的 $p_0$ 同样是真历史，
$p_0=1/(6H)-s^2/(2H)+O(s^4)$，没有丢掉该方程。

例如原辅助量的头几项是
$$
q_g=1+s^2+O(s^4),\qquad
a_1=-H^{-1}+\frac{s^2}{2H}+O(s^4),\qquad
d_s=-1+3D_3s^2+O(s^4),
$$
$$
\gamma=H(s+4a_4s^3)+O(s^5),\qquad
\operatorname{common}=-s+
 (4a_4+\tfrac12+8D_3)s^3+O(s^5),
$$
$$
a_0=-\frac{s}{H^2}
 -\frac1{H^2}\left(\frac{b_3}{2}+\frac43\right)s^3+O(s^5).
\tag{7}
$$
将这些代入
$$
r_{0,s}=\frac{a_0q_g+d_s\operatorname{common}/h^2}{8h}
$$
时，一阶的 $-s/H^2$ 与 $s/H^2$ 准确相消，故(6)没有遗漏 $r_0$ 的二阶项。
其余各行分别由原八密度直接得到；特别
$s_{0,s}=-1/(4H^2)+(1-3b_3/4)s^2/H^2+O(s^4)$，
与(6)一致。

## 3. 真实最高系数到三阶

记
$$
Q_c(y)=1+H^2y^2,
$$
$$
C_A(y)=r_0+(r_1+s_0)y+\frac32s_1y^2
 +(t_1-p_1/4)y^3-\frac14p_2y^4 .
$$
由(6)，
$$
\begin{aligned}
C_A(y)={}&\frac{Q_c}{8H^3}
 -\left(\frac{3y}{8H^2}+\frac{y^3}{8}\right)s\\
&+\left(\frac{3y^2}{8H}+\frac{Hy^4}{8}\right)s^2\\
&+\left[\frac{y}{H^2}\left(\frac7{24}-\frac{b_3}{4}\right)
 -\frac{5y^3}{24}\right]s^3+O(s^4).
\end{aligned}
\tag{8}
$$
在固定有限 y 窗口上，余项一致。

原完整最高系数仍是
$$
V_2=-2C_A-\frac{Qe_s}{4h^3},\qquad
Q=1+(hy+d)^2,\qquad e_s=\gamma y+d_s.
\tag{9}
$$
为核(9)中的乘积，而不是只核 $C_A$，分别有
$$
Q=Q_c-2Hy\,s+(H^2y^2+1)s^2
 +Hy(2D_3-1)s^3+O(s^4),
$$
$$
e_s=-1+Hy\,s+3D_3s^2+4Ha_4y\,s^3+O(s^4).
\tag{10}
$$
相乘再乘 $h^{-3}=H^{-3}(1-3s^2/2)+O(s^4)$，
与(8)相减，常数项及一阶项准确为零。结果是
$$
V_2=U_2(y)s^2+U_3(y)s^3+O(s^4),
\tag{11}
$$
$$
U_2=\frac{Q_c}{8H^3}
       \left(3(b_3-1)-2H^2y^2\right),
$$
$$
U_3=\frac{y}{H^2}
       \left(\frac7{6}-b_3-c+H^2y^2
          \left(1-\frac{b_3}{2}-c\right)\right).
\tag{12}
$$
等价地，(12)第二式的两项系数是
$(17/24-b_3/2-a_4)/H^2$ 与 $13/24-a_4$。
这保留了全部真 M；没有把 $p_2$ 或正平方的四次 y 项消去。

## 4. 一个显式正的四阶选择

用 R605 同一组**正**参考位置 $c_i>0$ 与权 $w_i>0$，
并记 $z_i=H^2c_i^2$、$Q_i=1+z_i$。
现在固定
$$
\boxed{b_3=1,\qquad k'''(0)=6.}
\tag{13}
$$
从(12)，
$$
U_2(y)=-\frac{Q_cy^2}{4H},\qquad
U_3(y)=\frac{y}{H^2}
 \left(\frac16-c+H^2y^2\left(\frac12-c\right)\right).
\tag{14}
$$
因此真实能量
$$
B_+(s)=\sum_iw_iQ(s,c_i)V_2(s,c_i)^2
$$
的四阶、五阶系数分别是
$$
B_4=\frac1{16H^2}\sum_iw_iQ_i^3c_i^4>0,
$$
$$
B_5=-\frac1{2H^3}\sum_iw_iQ_i^2c_i^3
 \left\{\frac16-c+z_i\left(\frac34-c\right)\right\}.
\tag{15}
$$
式(15)的五阶项包括了 $Q$ 自身的一阶变化；
不能只令 $\sum Q_c U_2U_3=0$。

选择
$$
\boxed{
c_*^{\rm geom}=
\frac{\sum_iw_iQ_i^2c_i^3(1/6+3z_i/4)}
     {\sum_iw_iQ_i^3c_i^3}.
}
\tag{16}
$$
这里上标 geom 用来区分 R603 的母系数 $c_*$。
分子分母都严格正。
(16)是函数
$$
\frac{1/6+3z/4}{1+z}
$$
对正权 $w_iQ_i^3c_i^3$ 的加权平均，所以
$$
\boxed{\frac16<c_*^{\rm geom}<\frac34.}
\tag{17}
$$
令 $c=c_*^{\rm geom}$，
即令 $a_4=c+1/24$，便准确有 $B_5=0$，
并且
$$
h^{(4)}(0)=H(1+24c)\in(5H,19H).
\tag{18}
$$
这给一个真实、正的 R 四阶系数；不是从非正的形式解中选支。

## 5. 同一个常数同时支付两侧首层

原负侧的 JPAR 为
$(+,-,+,-,-,+,-,+)$，
几何为 $(h,-k,-\eta,-\gamma,\upsilon)$。
对于当前 h 偶、k 奇的真输入，由(2)和原 M 的唯一性，
$A(-s)=JA(s)$，故
$$
B_-(s)=B_+(-s).
\tag{19}
$$
因此(15)的四阶系数两侧相同，五阶系数互为相反数；
(16)将两个五阶系数同时清零。

由(5)(17)，$m=2H^2cs^4+O(s^6)>0$ 对充分小的非零 s 成立。
选择整个小区间上的**同一个**正数
$$
\boxed{
\lambda=\frac{B_4}{2H^2c}
 =\frac{\sum_iw_iQ_i^3c_i^4}{32H^4c}>0,
}
\tag{20}
$$
便得到
$$
\boxed{B_+(s)-\lambda m(s)=O(s^6),\qquad
       B_-(s)-\lambda m(s)=O(s^6).}
\tag{21}
$$
其相对首阶差是 $O(s^2)$，因为 $m\asymp s^4$。
全程只用(20)一个常数，未按每一点另取规范。

这些 jets 可以由(1)的显式偶/奇多项式在小区间实现，
$\eta$、A 分别按(2)和原 M 积分。
若 H 位于 R598 原严格高度盒内部，则取区间足够短，
原 k/eta/速度和 Ch/Ck 合法域都保持。
所以(21)有真实的运动学与矩历史实现，而不只是抽象系数表。

## 6. 尚未支付的部分

(21)仍然只是有限阶剩余。它没有证明
$B_\pm=\lambda m$ 在一个正长区间上准确成立，
也没有证明 R605 的内部正则流可从这个退化中心到达。
剩余 $s^6$ 及以后系数不能视为自动可解。

更没有据此解有限 $\varepsilon=1/12000$ 的原两条 ruling、
C² rho、固定 $\chi$、八个末矩、pose、第四period、
同13或全程 reach/diameter。
当前全程 R605 guide 与原 hard-boundary mass 包已独立完成，
不等待这个更高阶局部条件，也不为(21)另开一次局部科学任务。

本文的正面用途是：
R603 必要的 $v=2$ 与 $a=H$ 之后，
$m>0$ 支在两侧最高能量的第一个非零阶和下一个奇阶确有显式真实相容输入。
它没有把目前仍欠的全程连接转换成一个“已经完成”的返回。

