# R624：自由中心的全程首层常数相容与唯一支明式输入

2026-11-27。**已证明：真记忆首层的完整返回给出全程常数的必要符号与准确端关系；一族明列、全程合法且动能有严格余量的曲线，具有唯一、稳定的标量参数，使其真实中心 jets 与这条首层端常数关系相容。**

这是一条用于原有限宽度 BVP 的新输入，不是该 BVP 的根。
它保留自由奇中心、原 $d=h\eta-k$、真 $\eta$ 积分和完整 $B_{ss}$ 交叉项。
下文的首层常数相容既不使试验曲线沿途满足首层能量，也不支付 $A(L)=0$；
更不支付固定 $\varepsilon=1/12000$ 的两原 ruling、六个 rho、闭 pose 或主 README 完成标准。
本稿只有纸面推导，没有本地科学执行或新 Actions 数值结论。

## 1. 量词、真实记忆与全程必要条件

使用 [R619](R619-free-center-leading-energy-and-true-memory-local-flow.md) 第 2 节的同一条件极限：
R598 同形缩微母、共同正长时间区间、原合法紧盒中的 $C^2$ 几何收敛、
真实自由奇中心有界收敛、原 $\rho_\pm(0)=0$，以及
$\varepsilon^2\widehat\nu_\varepsilon$ 收敛为一个常向量。
这些是条件，不能由一个数值初猜推出。
在该极限下，沿真实首层轨道有

$$
B_\pm=C_0(1+d^2)\ \pm\ 2C_1hd+C_2h^2,
\qquad d=h\eta-k,
\tag{1}
$$

其中 $C_0,C_1,C_2$ 在全程固定，且

$$
Q(y)=1+(hy+d)^2,
$$
$$
C_A(y)=r_0+(r_1+s_0)y+\frac32s_1y^2
 +(t_1-p_1/4)y^3-\frac14p_2y^4,
$$
$$
V(y)=-2C_A(y)-\frac{Q(y)}{4h^3}
            \left[\gamma(y+\eta)-\frac\upsilon2\right],
\qquad B_\pm=\sum_i w_iQ(\pm c_i)V(\pm c_i)^2.
\tag{2}
$$

全部八个 $A$ 满足原 $A_s=M$，原运动学为
$\gamma=h_s,\upsilon=k_s,\eta_s=\upsilon/(2h)$。
中心仍为

$$
h_c=H>0,\quad k_c=\eta_c=\gamma_c=0,\quad \upsilon_c=v\ne0,
\quad A_{\mathcal E,c}=0,
\tag{3}
$$

四奇中心按 $(p_{0c},p_{2c},s_{1c},r_{0c})$ 可变。
于是

$$
Q_c(y)=1+H^2y^2,
\qquad
V_c(y)=-2r_{0c}-3s_{1c}y^2+\frac{p_{2c}}2y^4
                         +\frac{vQ_c(y)}{8H^3},
$$
$$
B_c=\sum_iw_iQ_c(c_i)V_c(c_i)^2,
\qquad C_0=B_c-H^2C_2.
\tag{4}
$$

若一条真实首层轨道在 $L>0$ 满足原八端和末双速度

$$
A(L)=0,\qquad\gamma(L)=\upsilon(L)=0,
\tag{5}
$$

则 (2) 给 $V(L,y)=0$，因此 $B_\pm(L)=0$。两行相减和相加给

$$
\boxed{C_1d_L=0,\qquad C_0(1+d_L^2)+C_2h_L^2=0.}
\tag{6}
$$

这里 $h_L>0$。特别，若 $B_c>0$，则 $C_2\ne0$，并且

$$
R_L:=\frac{h_L}{\sqrt{1+d_L^2}},\qquad R_L^2\ne H^2,
$$
$$
\boxed{C_2=-\frac{B_c}{R_L^2-H^2},\qquad
C_0=-C_2R_L^2,\qquad C_0C_2<0.}
\tag{7}
$$

证明只需把 (4) 代入 (6)，得到
$B_c+C_2(R_L^2-H^2)=0$。因此 R619 中 $B_c>0,C_2=0$ 的例子确实只是局部输入；
它们不能在这些同一首层量词下同时达到 (5)。
这不排除原固定宽度 BVP，更不排除改变自由中心和中心 jets 后的根。

## 2. 完整真中心二阶式：不能从 $V_{ss}$ 单独推符号

设真实反射 germs 给

$$
a=h_{ss}(0),\quad j=k_{sss}(0),\quad
h_{sss}(0)=k_{ss}(0)=0,
\qquad \beta=a-\frac{Hv^2}{4}\ne0.
\tag{8}
$$

本节微分的是准确的光滑首层流；R619 在 $S_0S_1\ne0$ 时由隐函数定理给出这样的流。
没有对第 1 节仅 $C^0$ 收敛的余项求导，也没有从原几何的 $C^2$ 收敛擅自推出三阶收敛。
对后面的明式试验曲线，则只是在它的真实 $M$ 历史上计算中心 jets。

从 [R609](R609-true-integral-histories-and-kinetic-input.md) 所列原八密度逐项微分，中心有关的偶多项式槽满足

$$
p_{2,ss}(0)=-\frac{Hv}{2},
\qquad
s_{1,ss}(0)=\frac{v}{8H}+\frac{av}{8H^2},
$$
$$
r_{0,ss}(0)=-\frac{v}{16H^3}-\frac{av}{16H^4}
                              +\frac{v^3}{32H^3}.
\tag{9}
$$

其余出现在 $C_A$ 中的奇多项式槽的二阶导数由反射为零。
例如原 $d_s=\gamma\eta-\upsilon/2$ 与
$C=\gamma(1+d^2)/h-2dd_s$ 给
$d_s(0)=-v/2$、$C_s(0)=a/H-v^2/2$；代入原 $M_{r_0}$ 就得 (9) 的第三项。
真实运动学还给

$$
d_s(0)=-v/2,\qquad d_{ss}(0)=0,\qquad
d_{sss}(0)=av/H-j/2,
$$
$$
Q_s(0,y)=-Hvy,\qquad Q_{ss}(0,y)=v^2/2+2Hay^2.
\tag{10}
$$

由 (2)、(9)、(10)，完整微分结果为

$$
V_{s,c}(y)=\frac{(H-a)Q_c(y)y}{4H^3},
\tag{11}
$$
$$
\boxed{
V_{ss,c}(y)=
\frac{H(j+v)-4av}{8H^4}
+\frac{H(j-3v)-2av}{8H^2}y^2
-\frac{Hv}{4}y^4.}
\tag{12}
$$

为清楚显示导数来源，令 $G=\gamma(y+\eta)-\upsilon/2$。
在中心有 $G=-v/2,G_s=ay,G_{ss}=av/H-j/2$，而
$(Qh^{-3})_{ss}=Q_{ss}/H^3-3aQ_c/H^4$。
将这些和 (9) 代入
$V_{ss}=-2C_{A,ss}-\{(Qh^{-3})_{ss}G+2(Qh^{-3})_sG_s+Qh^{-3}G_{ss}\}/4$
便逐项得到 (12)。

因此真正需要使用的能量二阶式是

$$
\boxed{B''_c=\sum_iw_i\left[
Q_{ss,c}V_c^2+4Q_{s,c}V_cV_{s,c}
+2Q_cV_{s,c}^2+2Q_cV_cV_{ss,c}\right](c_i).}
\tag{13}
$$

全部四项均保留。$V_{ss,c}$ 的符号本身不决定 $B''_c$，也不决定 $C_0,C_2$。
定义原有限和

$$
S_0=\sum_iw_iQ_c(c_i)^2V_c(c_i),\quad
S_1=\sum_iw_ic_iQ_c(c_i)^2V_c(c_i),\quad
T_1=\sum_iw_ic_iV_c(c_i)^2.
\tag{14}
$$

一阶式与 R619 完全一致，而二阶式由 (1) 直接给出：

$$
\boxed{C_1=T_1+\frac{(a-H)S_1}{2H^4v},\qquad
C_2=\frac{B''_c-(v^2/2)B_c}{2H\beta},\qquad
C_0=\frac{2HaB_c-H^2B''_c}{2H\beta}.}
\tag{15}
$$

在固定 $H,v,A_c,a$ 时，(12) 给

$$
\boxed{\frac{\partial B''_c}{\partial j}=\frac{S_0}{4H^3},
\qquad \frac{\partial C_2}{\partial j}=\frac{S_0}{8H^4\beta}.}
\tag{16}
$$

因此当 $V_c<0$ 且 $\beta>0$ 时，提高真实中心三阶导数 $j$ 会严格降低 $C_2$。
这里提高 $j$ 必须来自一条明列曲线，不能把它独立指定后假定全程仍合法。

## 3. 原未发布明式输入的准确诊断

原 R620 全反馈草稿曾取 $H=a=1,v=-1/2$，四奇中心
$(-7/5,-10/3,-1/7,1/6)$，以及

$$
j_b=\frac{\pi^2}{8}-\frac{8\pi^3}{135}\in(-1,0).
\tag{17}
$$

其完整中心 profile 为

$$
Q=1+y^2,\qquad -V_c=W_o(y)=\frac53y^4-\frac{41}{112}y^2+\frac{19}{48}>0.
$$

这时 $V_{s,c}=0$，但必须保留 (13) 里的 $Q_{ss}V_c^2$。由 (12)

$$
V_{ss,c}=\frac{Q(y)(y^2+j_b+3/2)}8>0.
$$

于是

$$
2B_c-B''_c=
\sum_iw_i\left[\frac{15}{8}V_c^2-2QV_cV_{ss,c}\right](c_i)>0,
$$

所以 (15) 给 $C_0>0$。另一方面，在 $4\le y\le6$ 上有
$W_o\ge(3/2)y^4$、$Q\le(17/16)y^2$ 和 $V_{ss,c}<y^4/6$，故

$$
\frac{(15/8)y^2W_o^2-2QW_oV_{ss,c}}{W_oy^2}
>\left(\frac{45}{16}-\frac{17}{48}\right)y^4
=\frac{59}{24}y^4>0.
$$

这正是 $B''_c-B_c/8$ 的逐项正性，因而 $C_2>0$。
原试验 jets 所对应的首层常数同号，与 (7) 的完整返回必要条件不相容。
**这只是更换初猜的依据**：原固定 $\varepsilon$ 求解的十参数本来可变，
该诊断不意味着原有限宽度无根，也不使先前尚未运行的草稿成为失败实跑。

## 4. 新中心与真实参考权的精确比值界

现在固定

$$
H=1,\quad v=-\frac12,\qquad
(p_{0c},p_{2c},s_{1c},r_{0c})=
\left(-\frac75,-1,-\frac17,\frac16\right).
\tag{18}
$$

它属于 R619 的负 profile 中心盒。
在这一中心

$$
Q(y)=1+y^2,\qquad
W(y):=-V_c(y)=\frac12y^4-\frac{41}{112}y^2+\frac{19}{48}>0.
\tag{19}
$$

因此 $B_c>0,S_0<0,S_1<0$。取

$$
r=\frac{T_1}{-S_1}
=\frac{\sum_iw_ic_iW(c_i)^2}{\sum_iw_ic_iQ(c_i)^2W(c_i)},
\qquad a=1-r.
\tag{20}
$$

分母每一项严格正；$r$ 是 $W(c_i)/Q(c_i)^2$ 在正权
$w_ic_iQ(c_i)^2W(c_i)$ 下的平均。由 (15)，选择 (20) 准确给 $C_1=0$。

### 4.1 参考区间是 $[4.01,5.99]$，不是整个窗口 $[4,6]$

[R598](R598-three-rotations-wide-eighteen-block-mother.md) 第 2 节的真实代数定义是
$c_i=5+(99/100)x_i$，其中参考组 $x_i$ 是 $P_6$ 的六根。
同三组正权对次数不超过 10 的多项式均满足共同矩身份；已发表的
`r598_wide_mother_prepared_mass_bvp_agent.py` 中
`WideReferenceGrid.block_weights=copy_weights[1]` 使用的正是这组 $\tau=0$ 参考权。
故对 $\deg P\le10$，准确有

$$
\boxed{\sum_iw_iP(c_i)=\frac{50}{99}
\int_{401/100}^{599/100}P(y)\,dy.}
\tag{21}
$$

这里 $c_i\in(401/100,599/100)\subset(4,6)$。
(20) 的分子、分母被积多项式次数都是 9，因此 (21) 完全适用，
不是采样近似。令 $z=y^2$，并把 $W$ 记成

$$
W(z)=\frac{z^2}{2}-\frac{41z}{112}+\frac{19}{48},
\quad z_a=(401/100)^2,\quad z_b=(599/100)^2.
$$

因 $y\,dy=dz/2$，同一正因子相消，得到

$$
\boxed{r=\frac{\int_{z_a}^{z_b}W(z)^2\,dz}
                   {\int_{z_a}^{z_b}(1+z)^2W(z)\,dz}.}
\tag{22}
$$

### 4.2 完整有理界 $9/20<r<7/15$

$W(z)/(1+z)^2$ 在 $16\le z\le36$ 严格递增，因为导数分子的正因子是
$(1+41/112)z-(41/112+2\cdot19/48)>0$。
又

$$
W(36)=648-\frac{369}{28}+\frac{19}{48}<636,
\qquad \frac{636}{1369}<\frac7{15}
\quad(9540<9583).
$$

由 (20) 的正加权平均，$r<7/15$。

下界令

$$
P(z)=W(z)-\frac9{20}(1+z)^2
=\frac{z^2}{20}-\left(\frac{41}{112}+\frac9{10}\right)z-\frac{13}{240}.
$$

在 $z\ge16$ 上，$P,W$ 均严格递增；并有 $0<W(z)\le z^2/2$。
$z_a=16.0801<21$、$z_b=35.8801>35$。
以下逐段界给完整积分的符号，未把实际端点偷换成 16 和 36：

| 子区间 | 使用的下界或上界 | $\int WP$ 的严格下界 |
|---|---|---:|
| $[z_a,21]$ | 长度 $<5$，$W\le441/2$，$P>-8$ | $-8820$ |
| $[21,26]$ | $W\le338$，$P>-5$ | $-8450$ |
| $[26,28]$ | $W>328$，$P>1/2$ | $328$ |
| $[28,30]$ | $W>381$，$P>10/3$ | $2540$ |
| $[30,35]$ | $W>438$，$P>20/3$ | $14600$ |
| $[35,z_b]$ | $W>0,P>0$ | $0$ |

所有表项都是有理代入。比如用 $41/112<3/8$，
$P(26)>143/240>1/2$、$P(28)>827/240>10/3$、
$P(30)>1607/240>20/3$；$P(16)>-8,P(21)>-5$ 同样直接成立。
六项总和为 $198>0$，故 $\int WP>0$。由 (22) 的严格正分母，

$$
\boxed{\frac9{20}<r<\frac7{15},\qquad
\frac8{15}<a<\frac{11}{20},\qquad
\frac{113}{240}<\beta=a-\frac1{16}<\frac{39}{80}.}
\tag{23}
$$

特别 $\beta>7/16>0$，原 R620 中心图的两个分母
$-v/2=1/4$、$\beta$ 均有明确正余量。

## 5. 一条低于原拟议频率、全程有严格盒余量的新曲线族

固定 $L=3$，令 $x=s/3\in[0,1]$、$u=\pi x/2$，并设

$$
b=\frac{8/5-3/\pi}{3},\qquad A=\frac{9a}{\pi^2},\qquad m=41,
\qquad 0\le q\le\frac1{15}.
$$

$3<\pi$、$9<\pi^2<10$ 及 (23) 给

$$
b>\frac15,\qquad \frac{12}{25}<A<\frac{11}{20}.
\tag{24}
$$

定义全程曲线

$$
\boxed{h(x)=1+A(1-\cos\pi x),}
$$
$$
k_b(x)=-\frac85\sin u+b\sin3u,
\qquad
\psi(x)=\sin41u-\sin39u-2\sin u=-4\sin u\sin^2(20u),
$$
$$
\boxed{k_q(x)=k_b(x)-q\psi(x),\qquad
\eta_q(x)=\int_0^x\frac{k_{q,x}(t)}{2h(t)}\,dt.}
\tag{25}
$$

这里的 $q$ 是一个试验曲线参数，不能与原 $1+d^2$ 混淆。
增量 $-q\psi\ge0$，并在两端为零；其一阶导数也在两端为零。
实际中心物理 jets 为

$$
\boxed{v=-\frac12,\quad a_0=a,\quad
j(q)=j_b+\lambda q,\quad \lambda=\frac{400\pi^3}{9},\quad
f_0=-\frac{a\pi^2}{9}.}
\tag{26}
$$

其中 $j_b$ 为 (17)，并且
$h_s(0)=h_{sss}(0)=k_q(0)=k_{q,ss}(0)=k_{q,ssss}(0)=0$。
例如
$\psi_{uuu}(0)=-41^3+39^3+2=-6\cdot40^2$；
乘 $-q(\pi/6)^3$ 就得 (26) 的 $\lambda q$。
全部 $s=3x$ 因子已包含，没有任意借 prepared 的三阶或四阶值。

### 5.1 原 $h,k,\eta$ 盒

$h_x\ge0$，且

$$
1\le h(x)\le h_L=1+2A,
\qquad \frac{49}{25}<h_L<\frac{21}{10}<3.
\tag{27}
$$

写 $t=\sin u$，则

$$
k_b=-\frac3\pi t-4bt^3.
$$

它单调不增，末值为 $-K_e$，其中

$$
K_e=\frac{32}{15}-\frac1\pi<\frac{11}{6}<2.
$$

又 $4q\le4/15<3/\pi$，故 $k_b\le k_q\le0$，因而

$$
|k_q(x)|\le K_e<2.
\tag{28}
$$

令 $\Delta k=k_q-k_b\ge0$。真实积分分部给

$$
\Delta\eta(x)=\frac{\Delta k(x)}{2h(x)}
+\frac12\int_0^x\frac{\Delta k(t)h_x(t)}{h(t)^2}\,dt.
\tag{29}
$$

所以 $0\le\Delta\eta\le\|\Delta k\|_\infty/2\le2q$。
由于 $k_{b,x}\le0,h\ge1$，还得 $-K_e/2\le\eta_b\le0$，因此

$$
\boxed{-\frac{11}{12}<\eta_q(x)\le\frac2{15},\qquad |\eta_q(x)|<1.}
\tag{30}
$$

### 5.2 原速度盒和双末速度

$$
|h_s|\le\frac{3a}{\pi}<\frac{11}{20}<6,
\qquad |k_{b,s}|\le\frac{8\pi}{15}-\frac12<\frac{23}{18}.
$$

由 $\psi=-4\sin u\sin^2(20u)$，有
$|\psi_u|\le4+80=84$，故

$$
|k_{q,s}-k_{b,s}|\le14\pi q\le\frac{14\pi}{15}<\frac{28}{9}.
$$

于是

$$
\boxed{|k_{q,s}|<\frac{79}{18}<6.}
\tag{31}
$$

同时 $h_s(L)=k_{q,s}(L)=0$ 是准确三角身份。
全段原 $4/5<h<3,|k|<2,|\eta|<1,|h_s|,|k_s|<6$ 均已用明式支付，
不是只在观察点验证。

### 5.3 原动能必要式有严格正余量

令 $K(q)=\int_0^1k_q^2dx$、$U=\int_0^1(h_x/h)^2dx$。
奇半波 $1,3,39,41$ 两两正交，准确给

$$
K(q)=K(0)-\frac{16}{5}q+3q^2,
\qquad K(0)=\frac12\left[(8/5)^2+b^2\right]>\frac{13}{10}.
$$

右边的增量在 $0\le q\le1/15$ 递减，末增量为 $-1/5$，所以
$K(q)>11/10$。
对 $h=1+A-A\cos\pi x$ 的准确积分给

$$
\frac U{L^2}=\frac{\pi^2}{9}
       \left(\frac{1+A}{\sqrt{1+2A}}-1\right).
$$

括号中的比率随 $A>0$ 递增；在 $A<11/20$ 时

$$
\left(\frac{1+A}{\sqrt{1+2A}}\right)^2
<\frac{961}{840}<\frac{11449}{10000}
=\left(\frac{107}{100}\right)^2.
$$

故 $U/L^2<7/90$，并且

$$
\boxed{K(q)-1-U/L^2>\frac1{45}>0.}
\tag{32}
$$

这不支付四偶端条件；它明确排除了这个新初猜自身的动能不足。

## 6. 原 $d_L=h_L\eta_L-k_L$ 的定量端几何

以下始终使用原 $d$。$k_L=-K_e$ 不随 $q$ 变，由 (29) 和两端 $\Delta k=0$，

$$
d(q)=d_b+qD,\qquad
D=\frac{h_L}{2}\int_0^1\frac{[-\psi(x)]h_x(x)}{h(x)^2}\,dx,
\qquad 0<D<2(h_L-1)<\frac{11}{5}.
\tag{33}
$$

所以 $qD<11/75$。这里 $D>0$，并非把 $k_L-2h_L\eta_L$ 当作原 $d_L$。
特别不能据后一个不同的量错误判断 $R_L$ 的单调性。

为控制 $d_b$，用 $t=\sin u$ 写

$$
k_b=-\alpha t-\beta_k t^3,
\quad\alpha=3/\pi,\quad\beta_k=4b,
\quad K_e=\alpha+\beta_k.
$$

则

$$
|\eta_b(L)|=\frac{K_e}{2}\,\mathbb E\frac1{1+2At^2},
\qquad d\mathbb P(t)=\frac{\alpha+3\beta_kt^2}{K_e}\,dt,
\quad 0\le t\le1.
\tag{34}
$$

这是真实正概率密度，因为它的积分为1。
其二阶均值

$$
\mu=\mathbb E(t^2)=\frac{\alpha/3+3\beta_k/5}{\alpha+\beta_k}
<\frac{129}{275}
$$

由 $\alpha>9/10,\beta_k<14/15$ 得到：该比值随 $\beta_k$ 增、随 $\alpha$ 减，
端比值为 $(43/50)/(11/6)=129/275$。
函数 $z\mapsto(1+2Az)^{-1}$ 严格凸，Jensen 不等式给

$$
d_b=K_e-h_L|\eta_b(L)|
\le K_e\left[1-\frac{1+2A}{2(1+2A\mu)}\right].
$$

方括号随 $A$ 减、随 $\mu$ 增；用 (24) 得

$$
d_b<\frac{11}{6}\cdot\frac{6467}{19942}
=\frac{71137}{119652}<\frac35.
\tag{35}
$$

若该方括号为负，上界 $d_b<3/5$ 立即成立；若为非负，则上面的正数乘法合法。
另一方面 $|\eta_b(L)|\le K_e/2$，从而
$d_b\ge K_e(1-h_L/2)>-11/120$。
结合 (33)(35)，全 $q$ 区间满足

$$
-\frac{11}{120}<d(q)<\frac35+\frac{11}{75}
=\frac{56}{75}<\frac34,
\qquad |d(q)|<\frac34.
$$

定义

$$
G(q)=R_L(q)^2-1=\frac{h_L^2}{1+d(q)^2}-1.
$$

由 (27) 及上述严格界，得到

$$
\boxed{G(q)>\frac{(49/25)^2}{1+(3/4)^2}-1
=\frac{22791}{15625}>\frac{29}{20}.}
\tag{36}
$$

## 7. 全部交叉项给出的两端异号

在 (18)(20) 的中心，(11)(12) 化为

$$
Q_s=y/2,\quad Q_{ss}=1/8+2ay^2,\quad V_c=-W,
\quad V_{s,c}=rQy/4,
$$
$$
V_{ss,c}(y;j)=\frac{y^4+(j+3/2+a)y^2+j-1/2+2a}{8}.
\tag{37}
$$

令 $C_{20}=C_2(j_b)$。由 (13)(15)，

$$
N:=B''_c(j_b)-B_c/8
=\sum_iw_i\left[
(2a-1/8)y^2W^2-\frac r2Qy^2W
+\frac{r^2}{8}Q^3y^2-2QWV_{ss,c}(y;j_b)
\right]_{y=c_i},
\tag{38}
$$

并且 $C_{20}=N/(2\beta)$。
四项分别包含 $Q_{ss}$、$4Q_sV_cV_s$、$2QV_s^2$ 和 $2QV_cV_{ss}$，
没有以 $V_s\ne0$ 的新中心冒用旧 $V_s=0$ 式。

在 $4\le y\le6$ 上，(17)(23) 直接给

$$
\frac{15}{32}y^4<W\le\frac12y^4,\qquad
Q\le\frac{17}{16}y^2,\qquad
\frac{y^4}{8}<V_{ss,c}(y;j_b)<\frac{y^4}{6}.
\tag{39}
$$

例如 $j_b>-1,a>1/2$ 使 (37) 的 $y^2$ 系数大于1、常数项大于 $-1/2$，
故左侧 $V_{ss}$ 下界成立；上界可用 $j_b<0,a<1$ 后的
$[y^4+(5/2)y^2+3/2]/8<y^4/6$。
$j_b\in(-1,0)$ 也只需 $3<\pi<10/3$、$\pi^2<10$，无需小数评价。

将 (38) 的单项除以 $Wy^2>0$，舍去正的 $V_s^2$ 项，得

$$
\frac{N\text{ 的单项}}{Wy^2}
>\left(\frac{105}{256}-\frac{17}{1024}-\frac{17}{48}\right)y^4
=\frac{121}{3072}y^4>0.
$$

这里用了 $a>1/2,r<1/2,y^2\ge16$。所以 $C_{20}>0$。

为得上界，将 (38) 按正权 $w_iQW^2/B_c$ 归一。
第一项小于 $2\beta$，第二项负，第三项满足

$$
\frac{r^2Q^2y^2}{8W^2}
<\frac{289}{28800}<\frac1{80},
$$

第四项由 (39) 不大于 $-1/2$。
故 $N/B_c<2\beta-39/80$。又 $2\beta<39/40$，从而

$$
\boxed{0<\frac{C_{20}}{B_c}<\frac12.}
\tag{40}
$$

再由 (16)，$C_2$ 随 $j$ 严格仿射下降。
$-S_0/B_c$ 是 $Q/W$ 在正权 $w_iQW^2$ 下的平均。
$(1+z)/W(z)$ 在 $16\le z\le36$ 严格递减，因其导数分子为
$-z^2/2-z+(41/112+19/48)<0$。
所以

$$
-\frac{S_0}{B_c}>\frac{37}{636},
\qquad
-\frac1{B_c}\frac{\partial C_2}{\partial j}
>\frac{37}{636}\cdot\frac{10}{39}
=\frac{185}{12402}>\frac{119}{8000}.
\tag{41}
$$

在 $q=1/15$，由 (26) 有
$j-j_b=80\pi^3/27>80$。结合 (40)(41)，

$$
\boxed{\frac{C_2(1/15)}{B_c}<\frac12-80\frac{119}{8000}
=-\frac{69}{100}.}
\tag{42}
$$

于是连续标量函数

$$
\Phi(q)=B_c+C_2(q)G(q)
\tag{43}
$$

在左端严格正；由 (36)(42)，在右端满足

$$
\Phi(1/15)<B_c\left[1-\frac{69}{100}\frac{29}{20}\right]
=-\frac{B_c}{2000}<0.
\tag{44}
$$

故至少有一个 $q_*\in(0,1/15)$ 使 $\Phi(q_*)=0$。
此时 $C_1=0,C_2(q_*)<0,C_0=B_c-C_2(q_*)>0$，且

$$
C_0(1+d_L^2)+C_2h_L^2=(1+d_L^2)\Phi(q_*)=0.
\tag{45}
$$

新曲线的真实中心 jets 因此与首层全返回的两条常数关系 (6) 相容。

## 8. 唯一性与稳定选支：使用原 $d$ 的定量导数

写

$$
C_2(q)=C_{20}-\kappa q,
\qquad \kappa=-\frac{\lambda S_0}{8\beta}>0.
$$

由 (33)，$d'=D$，故

$$
G'(q)=-\frac{2h_L^2d(q)D}{(1+d(q)^2)^2}.
$$

不预设 $d$ 的符号；(27)(33)(36) 直接给

$$
|qG'(q)|<2\frac{441}{100}\frac34\frac{11}{75}
=\frac{4851}{5000},
$$
$$
\boxed{G(q)-|qG'(q)|>\frac{2399}{5000}>0.}
\tag{46}
$$

在 $C_2(q)\ge0$ 的区间，$\Phi(q)>0$，不可能有根。
在 $C_2(q)<0$ 的区间，置
$P(q)=(\kappa q-C_{20})G(q)$，则 $\Phi=B_c-P$。
若 $G'\ge0$，有 $P'\ge\kappa G>0$；若 $G'<0$，由 $C_{20}>0$ 得

$$
P'=\kappa G+(\kappa q-C_{20})G'
>\kappa(G+qG')>\kappa\frac{2399}{5000}>0.
$$

所以 $\Phi$ 在唯一可能有根的区间严格递减，结合 (44) 得到

$$
\boxed{\text{(43) 在 }[0,1/15]\text{ 中恰有一个根 }q_*.}
\tag{47}
$$

而且 $\lambda=400\pi^3/9>1200$，由 (41) 得
$\kappa/B_c>357/20$，于是根处乃至整个 $C_2<0$ 区间都满足

$$
\boxed{-\frac{\Phi'(q)}{B_c}
>\frac{357}{20}\frac{2399}{5000}
=\frac{856443}{100000}>8.}
\tag{48}
$$

这给出固定的、稳定的选支规则：原数值输入只评价和求解这个同一闭区间中的唯一纸证根，
可以用带括号二分或 Brent 法；不能在数个数值根中另挑较好 residual 的支。
(48) 是该标量相容图的界，不是原十九态端图或完整 Newton 算子的逆界。

## 9. 进入原有限宽度求解时必须保留的工作

新初始参数是完整的十元组

$$
\boxed{p_*=(1,-1/2,-7/5,-1,-1/7,1/6,
             a,j_b+\lambda q_*,-a\pi^2/9,3).}
\tag{49}
$$

四奇中心为 (18)，四偶中心和六 rho 中心仍为0；
初始 $\eta,A,\rho$ 必须由 (25)、原八 $M$ 与完整六 rho 更新实际积分。
不能把初始 $A(L)$ 强置零，也不能因为 (45) 就把原势删成首层项。
三常规范仍由已发表 R620 原有限宽度中心图、完整正势和真实中心 jets 产生。
原十九条 ODE、全部十条末条件与实际 C² 曲线重装的两原 ruling 门保持原单位。
本稿的 $C_j$ 不替换原 $\zeta_j$，也不把它们当作每点可变的自由控制。

相对未发布旧输入，真正改变的是 $p_{2c}=-10/3\to-1$、
$a_0=1\to a$、相应全程 $h$，以及两端/初速不变的 $m=41$ 三角增量。
其真实 $j_0$ 由 (26) 同步变化；全部原物理盒未扩大，母、正势系数和单位未更换。
频率 41 对应全 $x$ 区间 $41/4$ 个周期，低于先考虑的 81；
65 个等距 Lobatto 观察节点只有约 6.24 个区间/最高周期，不能宣称其 C² quintic 重建准确等于明式 seed。
该网格可作为明确的初猜表示，但它的误差必须由原实际 C² 曲线、真历史及 ruling 读数支付。
配点本身收敛而实际曲线门未过时，按已声明的第二网格正常精化，保同物理参数和真实重新积分费用；
不得继续在已解粗配点上作无效迭代，也不得降低实际门。

本稿没有证明试验曲线沿途满足 (1)，也没有证明它的真尾积分等于 (18)。
对应的首层局部真流由 R619 的 $S_0S_1\ne0$ 得到，拥有这里指定的 $a,j$，
但它的全程与四阶导数不因此等于 (25)。
原有限 $\varepsilon$ 全反馈 BVP 必须自行解决这些剩余条件。
之后仍须完整 period、规范、frame/位置、闭 pose、全域全时嵌入/reach 与宏观握持幅度，
本结论只作为一个确实不同且已支付上述必要相容性的输入继续推进。
