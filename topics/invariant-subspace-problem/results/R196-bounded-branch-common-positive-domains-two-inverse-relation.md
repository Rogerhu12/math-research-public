# R196：有界一阶分支强迫双正分量同域与真实双逆关系

日期：2026-11-12（UTC）。作者：critical_kernel。根代理预留 R196。

状态：完整精确引理与范围分析。主结论发生在原 Haar 模型，证明共同自然域、图核心、真实逆及最大核的准确关系。附录给一个更强的抽象反模型，说明准增生、空谱、通常伴随同域和有界自交换子形式仍不能单独排除双方向抵消；它不是本题实际算子的反例。

## 1. 原模型中的两个不交正方向

设
$$
b=(b_j),\quad c=(c_j)\in\ell^2,\qquad
b_j,c_j\ge0,\qquad b_jc_j=0,
$$
并假设
$$
\sum_jb_j=\sum_jc_j=\infty.
\tag{1.1}
$$
令
$$
T_+=X_{\sum_jb_j\chi_j},\qquad
T_-=X_{\sum_jc_j\chi_j}
\tag{1.2}
$$
为真实闭正系数第一阶乘子。

R128/R134 给以下准确事实：

- $T_\pm$ 为最大增生算子；
- $\sigma(T_\pm)=\varnothing$；
- $L_\pm:=T_\pm^{-1}\in\mathfrak C=\{A\}'$ 有界、单射、稠密像且拟幂零；
- $T_\pm$ 与全部有界交换子域交换；
- 对每个闭 $A$ 不变 $M$，自然限制
$$
(T_\pm)_M=T_\pm|_{\operatorname{Dom}T_\pm\cap M}
$$
闭、最大增生、空谱，且其实际逆就是 $(L_\pm)_M=L_\pm|_M$。

最后一条使用的是正系数不可和分支已经证明的满射性，不能仅从全 $H$ 稠密像推到 $M$。

令
$$
X=X_{a_*+\sum_j(b_j-c_j)\chi_j}.
\tag{1.3}
$$
它是 R125 的真实闭一阶，而不是先把两个无界算子在不明域上相减。
共同自然域上的有限线性恒等式为
$$
X=a_*I+T_+-T_-
\quad\text{在 }\operatorname{Dom}T_+\cap\operatorname{Dom}T_-.
\tag{1.4}
$$
(1.4) 可在有限柱上核对，再通过 R128/R186 的共同正则器和共同图核心识别。
也可用第一阶伴随有限柱核心的弱式直接识别。
一般不声称 $\operatorname{Dom}X$ 等于该交域。

## 2. 共同正则器是两个限制各自的图核心

置
$$
R_\pm(t)=(I+tT_\pm)^{-1},\qquad
R(t)=R_+(t)R_-(t),\quad t>0.
\tag{2.1}
$$
它们都是 $\mathfrak C$ 中的单射稠密收缩，
$R(t)\to I$ 强，并且
$$
R(t)H\subseteq\operatorname{Dom}T_+\cap\operatorname{Dom}T_-\cap\operatorname{Dom}X.
$$
两个 $T_\pm R(t)$ 及 $XR(t)$ 都是真正有界交换子。

对于 $s,t>0$，正预解的单位比率给
$$
R(s)=R(t)U(s,t),\qquad
U(s,t),U(s,t)^{-1}\in\mathfrak C.
\tag{2.2}
$$
所以对每个闭 $A$ 不变 $M$，
$$
R(s)M=R(t)M,\qquad
\overline{R(t)M}=M.
\tag{2.3}
$$

更强地，固定 $R(t)M$ 是两个限制 $(T_\pm)_M$ **各自**的图核心。
确实，对
$x\in\operatorname{Dom}T_\pm\cap M$，
$$
R(s)x\to x,\qquad
T_\pm R(s)x=R(s)T_\pm x\to T_\pm x.
$$
这些图逼近的输入全部属于同一个 $R(t)M$。
因此
$$
\boxed{
R(t)M\text{ 同时是 }(T_+)_M,(T_-)_M,X_M
\text{ 的图核心},
}
\tag{2.4}
$$
其中 $X_M$ 使用其自然限制；最后一项在需要时同样由域交换证明。
没有把两个不同 anchor 的单域结果直接拼在一起。

## 3. 仅在 M 上给定有界分支时的准确结论

设 $0\ne M$ 闭且 $A$ 不变，并假设
$$
M\subseteq\operatorname{Dom}X,\qquad
X|_M=Y_M\in B(M).
\tag{3.1}
$$
$Y_M$ 目前只是 $M$ 上的有界算子，不要求存在全空间有界交换延拓。
令
$$
Z_M=Y_M-a_*I_M.
$$

在共同核心 $R(t)M$ 上，(1.4) 给
$$
(T_+)_M=(T_-)_M+Z_M.
\tag{3.2}
$$
右侧是闭算子的有界扰动，域为 $\operatorname{Dom}(T_-)_M$。
因为 $R(t)M$ 是 $(T_-)_M$ 的图核心，也是该有界扰动的图核心；
它又是 $(T_+)_M$ 的图核心，所以取两边图闭包得到

**定理3.1。**
$$
\boxed{
\operatorname{Dom}(T_+)_M=\operatorname{Dom}(T_-)_M,
\qquad
(T_+)_M=(T_-)_M+Z_M
\text{ 在此准确共同域上}.
}
\tag{3.3}
$$

这并不表示 $M$ 的所有向量都属于两个正分量的域。
它只说明两个限制的完整定义域相同。

### 3.1 该分支与正逆真正交换

$L_\pm\in\mathfrak C$，而 $X$ 与它们域交换。
由 $M\subseteq\operatorname{Dom}X$ 及 $L_\pm M\subseteq M$，
$$
Y_M(L_\pm)_M=(L_\pm)_M Y_M.
\tag{3.4}
$$
所以 $Z_M$ 也与两个有界逆交换。

由于 $(L_\pm)_M$ 分别是 $(T_\pm)_M$ 的真实双侧逆，
(3.3) 给
$$
\boxed{
(L_+)_M-(L_-)_M
+(L_+)_M Z_M(L_-)_M=0.
}
\tag{3.5}
$$
例如，给任意 $f\in M$，共同域保证
$(L_-)_Mf\in\operatorname{Dom}(T_+)_M$。
作用 $(T_+)_M$ 得
$$
(T_+)_M(L_-)_Mf=f+Z_M(L_-)_Mf;
$$
再作用 $(L_+)_M$ 即得 (3.5)。

因为 $(L_-)_M$ 拟幂零，且与 $Z_M$ 交换，
$$
I_M+Z_M(L_-)_M
$$
是真正有界单位。
于是
$$
\boxed{
(L_+)_M
=(L_-)_M\bigl(I_M+Z_M(L_-)_M\bigr)^{-1}.
}
\tag{3.6}
$$

(3.5)—(3.6) 目前只是 $M$ 上的有界关系。
若 $Y_M$ 没有指定全空间延拓，不据此定义一个全局两逆多项式。

## 4. 全空间有界交换分支：最大核完全等价

现在另外给定
$$
Y\in\mathfrak C,\qquad Y_M=Y|_M,
\quad Z=Y-a_*I.
\tag{4.1}
$$
原 Bell 平方根分支 $Y\in\mathcal A$ 是这一情况的特例。

定义实际有界交换子
$$
\boxed{
\mathcal K_Y
=L_+-L_-+L_+ZL_-\in\mathfrak C.
}
\tag{4.2}
$$
本节证明完整核等价，不只证明一个方向。

令
$$
R_0=L_+L_-.
$$
它单射稠密，并把 $H$ 送入两个正分量的共同域。
由 (1.4)，
$$
\boxed{
(X-Y)R_0=-\mathcal K_Y.
}
\tag{4.3}
$$
每个等式中的无界作用都已经由 $R_0$ 正则化。
在 $\operatorname{Dom}X$ 上还可由域交换写
$$
R_0(X-Y)x=-\mathcal K_Yx.
\tag{4.4}
$$

### 4.1 R0 的真实参数核心

由 $T_\pm^{-1}=L_\pm$，
$$
R_\pm(t)=L_\pm(tI+L_\pm)^{-1},
$$
所以
$$
R(t)=R_0U_t,\qquad
U_t=(tI+L_+)^{-1}(tI+L_-)^{-1}.
\tag{4.5}
$$
每个 $U_t$ 及其逆都属于 $\mathfrak C$；
这里使用 $L_\pm$ 拟幂零，故 $tI+L_\pm$ 可逆。
因此
$$
R(t)H=R_0H.
$$
而 $R(t)H$ 是 $X-Y$ 的图核心：
对其完整域中的 $x$，
$R(s)x\to x$，$(X-Y)R(s)x=R(s)(X-Y)x$ 强收敛。
故
$$
\boxed{
\operatorname{Graph}(X-Y)
=\overline{\{(R_0h,-\mathcal K_Yh):h\in H\}}.
}
\tag{4.6}
$$

### 4.2 最大图与两个核的相等

若
$$
-\mathcal K_Yx=R_0y,
$$
用 (4.5) 令 $x_s=R(s)x=R_0U_sx$。
由 (4.3)，
$$
(X-Y)x_s=-\mathcal K_YU_sx=R_0U_sy=R(s)y.
$$
让 $s\downarrow0$，并用 $X-Y$ 闭，得到 $(X-Y)x=y$。
反向由 (4.4) 已知。
因此
$$
\boxed{
\operatorname{Graph}(X-Y)
=\{(x,y):-\mathcal K_Yx=R_0y\}.
}
\tag{4.7}
$$
特别
$$
\boxed{
\ker(X-Y)=\ker\mathcal K_Y,\qquad
\overline{\operatorname{Ran}(X-Y)}
=\overline{\operatorname{Ran}\mathcal K_Y}.
}
\tag{4.8}
$$
第二式直接由原参数图核心给出；
不需要假设未知限制的值域稠密。

这里 $\mathcal K_Y\ne0$。
否则 (4.7) 会给 $X=Y$ 为全域有界算子，
与 $(b-c)\notin\ell^1$ 时第一阶必无界矛盾。
而 $L_\pm$ 都拟幂零并彼此及与 $Z$ 交换，所以
$\mathcal K_Y$ 也拟幂零。

这把真正的慢分支核改写成一个明确的、非零有界交换子的核。
它不证明这个有界核已经为零。

## 5. 两条任意复射线及其正性后果

更一般取非零复数 $\rho,\sigma$，令
$$
X=X_{a_*+\sum_j(\rho b_j+\sigma c_j)\chi_j}.
$$
若 $X|_M=Y_M$ 有界，则同一个共同核心证明
$$
\boxed{
\operatorname{Dom}(T_+)_M=\operatorname{Dom}(T_-)_M,
\qquad
(T_+)_M=-\frac{\sigma}{\rho}(T_-)_M
+\frac{Y_M-a_*I_M}{\rho}.
}
\tag{5.1}
$$
原因是乘以非零标量及加有界项都保持闭性和图核心。

若有全局分支 $Y\in\mathfrak C$，则
$$
(X-Y)R_0
=\rho L_-+\sigma L_+-(Y-a_*I)L_+L_-,
$$
其最大图及核等价与 §4 完全相同。

### 5.1 数值域的真实必要扇区约束

记
$$
c=-\sigma/\rho,\qquad
D_M=(Y_M-a_*I_M)/\rho.
$$
对共同域中的单位 $x$，置
$$
z=\langle (T_-)_Mx,x\rangle.
$$
两个正分量增生，(5.1) 给
$$
\boxed{\operatorname{Re}z\ge0,\qquad
\operatorname{Re}(cz)\ge-\|D_M\|.}
\tag{5.2}
$$

若 $c=|c|e^{i\varphi}$、$0<|\varphi|<\pi$，
取
$$
t_0=\frac{\|D_M\|}{|c|\cos(\varphi/2)}.
$$
则
$$
w=e^{i\varphi/2}z+t_0
$$
满足
$$
\operatorname{Re}(e^{i\varphi/2}w)\ge0,\qquad
\operatorname{Re}(e^{-i\varphi/2}w)\ge0.
$$
因此
$$
\boxed{
|\arg w|\le\frac{\pi-|\varphi|}{2}<\frac\pi2.
}
\tag{5.3}
$$
也就是说，一个适当旋转和平移的 $(T_-)_M$ 必有严格小于半平面的数值扇区。

这是必要条件，不是矛盾。
空谱闭算子可以具有较窄的数值扇区；
本稿没有借标准半群术语跳过真正的模型限制。
实交替情形 $\rho=1,\sigma=-1$ 对应 $c=1$，(5.3) 没有严格角度改进。

## 6. 为什么单独两个正方向并不够

§§3—5 给出了能够从正性直接推出的内容：
完整同域、真实双逆关系以及在非共线相位下的必要数值扇区。
它们没有给未知 $M$ 的局部头范数下界或任何一般双逆多项式的限制稠密性。

下面的反模型表明，若只保留两方向的准增生、空谱、独立张量支持及共同域结构，抵消确实可以发生。
更强的版本还保留通常伴随同域、有界自交换子形式与一个共同的单射稠密拟幂零有界算子。

这个反模型只说明抽象结构推理的边界。
它不满足实际 odometer 的全部高位、Calkin 或一阶无点谱性质。

## 7. 加强反模型：通常伴随同域和有界自交换子也仍可抵消

### 7.1 单变量空谱最大增生算子

在 $H_0=L^2(\mathbb R)$ 上令
$$
T=\frac d{dx}+|x|,
\qquad
\operatorname{Dom}T
=\{f\in H^1(\mathbb R):xf\in L^2(\mathbb R)\}.
\tag{7.1}
$$
取
$$
\phi(x)=\frac{x|x|}{2},\qquad \phi'(x)=|x|.
$$
在 $C_c^\infty$ 上分部积分给
$$
\|Tf\|^2
=\|f'\|^2+\|xf\|^2-\int\operatorname{sgn}(x)|f(x)|^2\,dx.
\tag{7.2}
$$
所以图范数与
$\|f\|+\|f'\|+\|xf\|$ 等价。
截断和卷积逼近证明 $C_c^\infty$ 为图核心，且 (7.1) 给闭算子。

对任意 $\lambda\in\mathbb C$，定义
$$
(G_\lambda f)(x)
=\int_{-\infty}^x
e^{\lambda(x-t)-\phi(x)+\phi(t)}f(t)\,dt.
\tag{7.3}
$$
若 $r=x-t\ge0$，任何长为 $r$ 的区间都满足
$$
\int_t^x|s|\,ds\ge r^2/4.
$$
于是核的绝对值受
$$
\mathbf1_{r\ge0}\exp((\operatorname{Re}\lambda)r-r^2/4)
$$
控制；这是 $L^1(\mathbb R)$ 卷积核。
所以 $G_\lambda$ 在 $L^2$ 上有界。

对紧支撑光滑输入直接微分，得到
$(T-\lambda)G_\lambda f=f$，
且输出属于 (7.1)。
一般输入用闭性和稠密逼近处理。
另一方面，齐次解只有
$$
f(x)=c\,e^{\lambda x-\phi(x)},
$$
非零时在 $-\infty$ 端不能属于 $L^2$。
所以
$$
\boxed{(T-\lambda)^{-1}=G_\lambda\in B(H_0)
\quad(\lambda\in\mathbb C),\qquad \sigma(T)=\varnothing.}
\tag{7.4}
$$

又
$$
\operatorname{Re}\langle Tf,f\rangle
=\int|x||f(x)|^2dx\ge0.
$$
结合 $T+I$ 满射，$T$ 为最大增生。

通常伴随为
$$
T^*=-\frac d{dx}+|x|,
\qquad
\operatorname{Dom}T^*=\operatorname{Dom}T.
\tag{7.5}
$$
为核对反向域，取 $(C_0f)(x)=\overline{f(-x)}$，
令 $T^\#=C_0TC_0=-d/dx+|x|$，域仍为 (7.1)。
核心分部积分及图逼近给 $T^\#\subseteq T^*$。
对 $f\in\operatorname{Dom}T^*$，利用 $T^\#+I$ 满射，选取
$g\in\operatorname{Dom}T^\#$ 使
$(T^\#+I)g=(T^*+I)f$。
而 $\ker(T^*+I)=0$，因为 $T+I$ 满射，所以 $f=g$。
这证明完整伴随域。
完整自交换子形式为
$$
\boxed{
\|Tf\|^2-\|T^*f\|^2
=-2\int\operatorname{sgn}(x)|f(x)|^2dx.
}
\tag{7.6}
$$
故它的有界代表为 $-2M_{\operatorname{sgn}x}$。

$T^*=C_0TC_0$ 也证明上述闭算子的完整 $C_0$ 自伴。
其逆 $V=T^{-1}$ 有界、单射、稠密像且拟幂零。
最后一点可直接由所有 $I-\lambda V$ 均可逆得到。

(7.2) 的图嵌入是紧的：图范数有界集合在 $|x|>R$ 上的平方范数
至多为 $R^{-2}\|xf\|^2$；在 $[-R,R]$ 上，用细网格区间平均作有限维逼近，
误差由网格长度乘 $\|f'\|$ 控制。
先选 $R$，再选网格，便得到全有界性。
因此 $V$ 还是非零紧算子。

### 7.2 两个独立张量方向及其闭差

在 $H_0\otimes H_0=L^2(\mathbb R^2)$ 上取
$$
T_1=T\otimes I,\qquad T_2=I\otimes T.
$$
它们各自最大增生、空谱，作用在严格不交的两个张量坐标上。
有界逆
$$
V_1=V\otimes I,\qquad V_2=I\otimes V
$$
交换。

将 $T_1-T_2$ 的共同自然实现闭包记为 $\mathcal X$。
用坐标
$$
s=x+y,\qquad t=(x-y)/2
$$
识别其准确闭实现：
$$
\mathcal X_s=\frac d{dt}+p_s(t),
\qquad
p_s(t)=|s/2+t|-|s/2-t|.
\tag{7.7}
$$
对每个固定 $s$，$p_s$ 是有界实函数，
$$
|p_s(t)|\le|s|,\qquad |p_s'(t)|\le2\quad\text{几乎处处}.
$$
因此每个纤维的域为 $H^1(\mathbb R_t)$，
通常伴随为 $-d/dt+p_s(t)$。
取这些纤维的最大直积分闭算子。

这是共同自然差的闭包：
先截断 $s$，它与微分严格交换；
在有限 $s$ 区间，$p_s$ 一致有界，图范数与 $t$ 方向的 $H^1$ 范数等价；
再作紧支撑平滑逼近，得到 $C_c^\infty(\mathbb R^2)$ 是该直积分的图核心。
共同自然差含此核心，并包含于这个最大闭图。

纤维的图二次型差给
$$
\operatorname{Dom}\mathcal X
=\operatorname{Dom}\mathcal X^*,
$$
以及
$$
\boxed{
\|\mathcal X f\|^2-\|\mathcal X^*f\|^2
=-2\int_{\mathbb R^2}
(\operatorname{sgn}x+\operatorname{sgn}y)|f(x,y)|^2\,dx\,dy.
}
\tag{7.8}
$$
右侧代表有界，范数不超过4。
共同共轭 $C_0\otimes C_0$ 也给
$\mathcal X^*=C\mathcal X C$。
因此这个例子保留了通常伴随同域和有界自交换子形式，超出只用区间单侧导数的反模型。

### 7.3 一个明确的非零闭抵消空间

取 $h\in C_c^\infty((0,\infty))$，令
$$
f_h(x,y)
=e^{-\phi(x)-\phi(y)}h(x+y).
\tag{7.9}
$$
若 $s=x+y>0$，沿该直线写 $x=s/2+t,y=s/2-t$，则
$$
\phi(x)+\phi(y)
=
\begin{cases}
t^2+s^2/4,&|t|\le s/2,\\
s|t|,&|t|\ge s/2.
\end{cases}
$$
所以紧支撑于正 $s$ 区间的非零 $h$ 给非零 $L^2$ 向量，
并且它属于 $T_1,T_2$ 的共同自然域。
直接微分得
$$
T_1f_h=T_2f_h
=e^{-\phi(x)-\phi(y)}h'(x+y),
$$
从而
$$
\mathcal Xf_h=0.
\tag{7.10}
$$

更精确地，令
$$
W(s)
=\frac{e^{-s^2}}s
+e^{-s^2/2}\int_{-s/2}^{s/2}e^{-2t^2}\,dt
\qquad(s>0).
$$
映射 $h\mapsto f_h$ 是
$L^2((0,\infty),W(s)\,ds)$ 到 $L^2(\mathbb R^2)$ 的等距嵌入。
其闭像 $M_0$ 无限维，并由纤维方程 (7.7) 得
$$
M_0=\ker\mathcal X,\qquad \mathcal X|_{M_0}=0.
\tag{7.11}
$$
因此 $M_0$ 包含于所有自然 $\mathcal X$ 幂的域，且全部幂在其上为零。

两个有界逆在 $M_0$ 上事实上相等。
对上述紧支撑 $h$，由 (7.3) 计算
$$
V_1f_h=V_2f_h=f_H,\qquad
H(s)=\int_0^s h(r)\,dr.
\tag{7.12}
$$
再以有界性延拓到整个 $M_0$。
所以 $M_0$ 被 $V_1,V_2$ 保持，且
$$
(V_1-V_2)|_{M_0}=0.
$$

还可以取共同的有界算子
$$
A_0=V_1V_2.
$$
它单射、稠密像、拟幂零、$C$ 对称，并保持 $M_0$。
这表明一般的共同有界不变性也不自动排除抵消。

### 7.4 这个反模型没有包含的实际条件

这里 $A_0$ 是非零紧算子，缺少原模型的高位归一化幂弱极限和 R164 的无非零紧元 Calkin 结构。
差 $\mathcal X$ 还有非零点谱，而本题所有真实第一阶由 R125 已知无点谱。
$A_0$ 也没有被声称满足 R88 的整个交换子结构或本题权的任何精确恒等式。

因此 (7.11) 不是实际 $A$ 的核构造。
它严格说明：若尝试只依靠两个正方向的空谱、通常伴随同域、有界自交换子、共同核心及抽象不变性，论证仍会允许非零抵消空间。
继续排除原模型的慢分支，必须用到缺失的实际高位或代数条件。

## 8. 对原问题留下的准确接口

原模型现已得到：

1. 未知有界分支强迫两个正分量的限制具有真正相同的完整定义域；
2. 无全局分支时只有 $M$ 内的有界双逆关系 (3.5)；
3. 有全局 $Y\in\mathfrak C$ 时，未知核准确等于明确的非零有界交换子 $\mathcal K_Y$ 的核；
4. 两个非共线复射线还给必要的数值扇区约束 (5.3)。

没有得到：

- 一般 $\mathcal K_Y$ 单射或在全部未知限制上值域稠密；
- 把单一空谱逆的 $\mathcal G[L]$ 定理直接用于两个独立逆的抵消；
- 把新的 C* 边界作用直接施加于未知核投影；
- 慢二次单核或完整 ISP 的终结。

R197 的逐坐标高位边界可继续用于全局 $\mathcal K_Y$ 的真实代数约束；
但未知核或其投影如何合法进入该边界，仍需单独证明。
