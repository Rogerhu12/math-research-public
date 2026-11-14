# Poisson 双帽的正向接缝模板：全点对法向管、固定圆领与待解连接边值问题

作者：/root/independent_geometry，2026-11-09。状态：本文的辅助包围、显式局部模板、模板的全域 reach、保留片之间的法向点对界均有完整证明；纯 Fraction 账本已实际退出 0。尚待另一代理全文独立审查。

**没有构造连通闭曲面族，没有解共同度量，也没有证明未来完整曲面的 reach。** 本文不读取当前 M15 候选、参数优化态或求解输出，不运行求解器、RK、源积分或几何后端。原 Poisson 双帽 v2 和所有旧账本保持原字节。

本文的正面结果是一个可明确写出的 $C^2$ 鞍形接缝片，以及它与两固定帽片、两真正固定平面圆领之间已支付的几何预算。该接缝回接到原柱面的相同两阶数据，尚未完成转弯到圆领的连接。最后给出所缺连接的具体方程、边界数据和验收不等式，不把“局部可接”替换成“全闭族已存在”。

## 1. 冻结核心与新辅助包围

沿用已审 Poisson 双帽 v2 的全部物理核心与标记：

$$
q=\frac{99}{100},\qquad r=\frac1{10},\qquad
b=\frac1{100},\qquad z_*=\frac3{10},\qquad a=\frac1{10}.
\tag{1}
$$

这里 $b$ 是实际保留活动柱带的半高，$a$ 是固定球面帽的半径；$z_*$ 是两个球心的高度绝对值。平面严格凸体及其边界为 $K,\Gamma$，支持函数为 $h$，且

$$
H=\max h=\max_{x\in K}|x|,\qquad
m_0=\min h,\qquad \Delta=H-m_0,\qquad d=\operatorname{diam}K.
\tag{2}
$$

R27 已审有理端点给出

$$
\begin{aligned}
.655688007298&\le m_0\le .655710884848,\\
.530966669770&\le\Delta\le .530967110151,\\
2.083520966968&\le d\le2.083520975612,\\
1.186654677068&\le H\le1.186677994999.
\end{aligned}
\tag{3}
$$

平面曲率半径全角满足

$$
\rho(\phi)\ge m:=\frac{104}{995}.
\tag{4}
$$

记 $Z_b=z_*+b$ 和 $L_b=\sqrt{4H^2+Z_b^2}$。固定球心、帽轴和旧大帽仍为

$$
P_\pm=(-H,0,\pm z_*),\qquad
v_\pm=\frac{(-2H,0,\pm Z_b)}{L_b},\qquad
C_\pm=\{P_\pm+a\omega:|\omega|=1,\ \omega\cdot v_\pm\ge1/2\}.
\tag{5}
$$

轴点 $q_\pm=P_\pm+a v_\pm$ 不变。特别地，后文放宽包围时，**帽轴仍用 $z_*+b$，没有改成新包围高度**。

新引入的量只是辅助包围的半高

$$
B=\frac9{100},\qquad
E_\alpha^B=
\operatorname{conv}\bigl((R_\alpha\Gamma\times[-B,B])\cup C_+\cup C_-\bigr).
\tag{6}
$$

实际必须保留的活动片仍是 $R_\alpha\Gamma\times[-b,b]$，其共同柱度量未变。$B$ 是后续完整像可以占用的位置范围，既不是新物理活动柱带，也不是当前数值问题的参数修改。

### 1.1 更宽包围仍支付两个强比例

令 $T_0,T_1$ 是未来初始、半相位的两个完整非空紧像。所需假设只是一侧完整包围和实际点见证：

$$
T_0\subset E_0^B+\varepsilon_0\overline B_3,\qquad
T_1\subset E_{\pi/3}^B+\varepsilon_1\overline B_3,\qquad
\varepsilon_0=\varepsilon_1=\frac1{200}.
\tag{7}
$$

初始 $T_0$ 中须有分别距
$x_+=(H,0,-b)$、$q_+$ 不超过 $\varepsilon_0$ 的两个实际点；半相位 $T_1$ 中须有距 $(Hu,0)$ 不超过 $\varepsilon_1$ 的实际点，其中
$u=(1/2,\sqrt3/2)$ 或 $(1/2,-\sqrt3/2)$。若原活动柱带与轴点被精确保留，这些误差可取零；下文仍保留较宽预算。

设

$$
L_B=\sqrt{4H^2+(z_*+B)^2},\qquad
U_B=\sqrt{d^2+(z_*+B)^2}.
\tag{8}
$$

初始见证点距仍为 $L_b+a$，所以真实初始直径 $D_0$ 满足

$$
L_b+a-2\varepsilon_0\le D_0\le L_B+a+2\varepsilon_0.
\tag{9}
$$

初始上界使用全角 $|x|\le H$。半相位时 $(-H,0)\in R_{\pi/3}\Gamma$，每个核心点与该点的水平距离不超过 $d$。全部点对的上界分别为

$$
\sqrt{d^2+4B^2},\qquad 2z_*+2a,\qquad U_B+a.
\tag{10}
$$

前一项不超过 $U_B$，因为 $z_*\ge B$；账本另严格核对中间项小于 $U_B+a$。取凸包不增加直径，于是

$$
D_1:=\operatorname{diam}T_1\le U_B+a+2\varepsilon_1.
\tag{11}
$$

采用向外的有理平方根端点，账本得到

$$
\begin{aligned}
&D_0<2.51518578393841< D_*:=\frac{63}{25}=2.52,\\
&D_1<2.22970744580831,\\
&9L_{b,\mathrm{lo}}-10U_{B,\mathrm{hi}}
  >a+18\varepsilon_0+20\varepsilon_1.
\end{aligned}
\tag{12}
$$

任意刚体，包括平移和反射，保持直径；又
$|\operatorname{diam}X-\operatorname{diam}Y|\le2d_H(X,Y)$。因此

$$
\frac{\inf_{A\in E(3)}d_H(A T_1,T_0)}{D_0}
\ge\frac12\left(1-\frac{D_1}{D_0}\right)
>0.05109026903944>\frac1{20}.
\tag{13}
$$

这里分母用真实 $D_0$。验证下界时使用
$\frac12(1-U/D)$ 随 $D>0$ 增大而增大，故代入初始直径的下界；没有把 $D_*$ 放进这个错误方向的分母。

水平支持见证不受 $B$ 改变。初始包围在 $u$ 方向的支持为 $m_0$，因为两帽的该方向支持至多 $-H/2+a<m_0$；半相位实际点给

$$
d_H(T_1,T_0)\ge\Delta-\varepsilon_0-\varepsilon_1.
$$

用 (9) 的初始上界，得到

$$
\frac{d_H(T_1,T_0)}{D_0}>0.20712850442174>\frac15.
\tag{14}
$$

两轴点的竖直间距大于 $2z_*=.6>.2D_*$。若以它们为内点的两个实际帽片在所有相位逐点固定，握持区尺寸也够用。该材料固定要求不能由像集合不变代替。

这些结论是完整像的条件式转移。没有要求完整像双向靠近三个分离片；小误差的双向入口已由旧 v2 的连通性反证排除。

## 2. 为什么不能把原窄包围直接交给保留竖直切线的闭面

本节只解释辅助高度 $B$ 的用途，不改变旧条件定理。旧包围把 (6) 的 $B$ 换成 $b$，记为 $E_\alpha^b$。

### 2.1 一般切向出发的支持平面余量

设 $S$ 是闭 $C^2$ 嵌入曲面，$\operatorname{reach}S\ge\rho_*>0$，
$p\in S$，$v\in T_pS$ 为单位向量，$u$ 为单位空间向量，
$d_*=u\cdot v\in[0,1]$。若整个 $S$ 位于半空间

$$
u\cdot(x-p)\le\eta,
$$

则必要地

$$
\boxed{\eta\ge
\rho_*\bigl(1-\sqrt{1-d_*^2}\bigr).}
\tag{15}
$$

证明：reach 的标准切平面刻画推出各主曲率绝对值不超过 $1/\rho_*$；也可在 Federer Theorem 4.18 的点对式中令第二点沿切线趋近。取从 $p$ 以初速 $v$ 出发的单位速内蕴测地线。闭曲面的紧性保证它至少可延续到以下有限长度；$C^2$ 正则性使空间加速度为连续法向量并满足
$|\gamma''|\le1/\rho_*$。令 $\theta=\arccos d_*$。单位切向量在球面上的转角速度至多 $1/\rho_*$，所以在
$0\le s\le\rho_*(\pi/2-\theta)$ 上

$$
u\cdot\gamma'(s)\ge\cos(\theta+s/\rho_*).
$$

积分至右端得到投影增量至少
$\rho_*(1-\sin\theta)$，即 (15)。这个论证不选择曲面“内侧”，不借未经检查的内切球方向。

### 2.2 在旧 Poisson 包围的应用

半相位取

$$
u=\frac{(9,0,40)}{41},\qquad p=(m_0,0,b),\qquad v=e_z.
$$

有理账本验证

$$
9(m_0+H)+40(b-z_*)-41a>0.
\tag{16}
$$

因此在方向 $u$，活动柱的支持严格压过两个完整标记球的支持；旧完整包围满足

$$
h_{E_{\pi/3}^b}(u)=\frac{9m_0+40b}{41}=u\cdot p.
$$

若真实完整面保留该柱带端点及其竖直切向，且包含于
$E_{\pi/3}^b+\varepsilon_1\overline B_3$，可用余量只有
$\eta=\varepsilon_1=.005$。而 (15) 要求

$$
\eta\ge\frac{32}{41}\rho_*.
\tag{17}
$$

由初始点对，README 的 reach 门本身已要求
$\rho_*\ge .03 D_{0,\mathrm{lo}}$；这是约 $.07450$ 的实际下界，不能以直径上界替代。账本精确核实 (17) 大于 $.005$。即使只保留中央曲线上的竖直切向，余量增至
$40b/41+\varepsilon_1$ 仍不足。

新包围在柱带端点增加的支持余量为

$$
\frac{40}{41}(B-b)+\varepsilon_1,
$$

它严格大于 $(32/41)\rho_{\mathrm{goal}}$，其中统一使用稍强的目标

$$
\rho_{\mathrm{goal}}=.03D_*=\frac{189}{2500}=.0756.
\tag{18}
$$

这里只说明这一局部必要障碍已移除，不说明闭合存在。

## 3. 一个完整写出的 $C^2$ 鞍形接缝

以法向角参数化平面核心：

$$
x(\phi)=h(\phi)n(\phi)+h'(\phi)t(\phi),\qquad
x'(\phi)=\rho(\phi)t(\phi),\qquad
n'(\phi)=t(\phi).
$$

取

$$
\delta=\frac1{10^6},\qquad \ell=\frac1{200},\qquad
p(\tau)=64\tau^3(1-\tau)^3.
\tag{19}
$$

定义偶函数

$$
f(z)=
\begin{cases}
\delta\,p\bigl((|z|-b)/\ell\bigr),&b\le|z|\le b+\ell,\\
0,&\text{其余}.
\end{cases}
\tag{20}
$$

$p,p',p''$ 在 $0,1$ 都为零，故 $f\in C^2(\mathbb R)$，没有把三阶端点跳跃误称为 $C^3$。写 $y=\tau(1-\tau)\in[0,1/4]$，则

$$
p'=192y^2(1-2\tau),\qquad
p''=384y(1-5y).
\tag{21}
$$

第一式的平方最大值为 $192^2/5^5<16$；第二式的最大、最小值为 $96/5,-24$。所以

$$
0\le f\le\delta,\qquad
\|f'\|_\infty\le A:=\frac1{1250},\qquad
\|f''\|_\infty\le M:=\frac{24}{25}.
\tag{22}
$$

显式曲面为

$$
\mathcal F(z,\phi)=\bigl(x(\phi)+f(z)n(\phi),z\bigr),
\qquad z\in\mathbb R,\quad \phi\in\mathbb R/(2\pi\mathbb Z).
\tag{23}
$$

每个固定 $z$ 截面是 $\Gamma$ 的外平行曲线，其曲率半径为 $\rho+f\ge m>0$。高度坐标区分不同截面，因此 (23) 是 proper 的 $C^2$ 嵌入，其像 $\Sigma$ 是欧氏空间中的闭子集，拓扑为非紧圆柱。

在 $|z|\le b$，它精确保留原柱带。在 $|z|=b+\ell$，位置、一阶和二阶 Cartesian 数据又恰好返回原柱面；特别地
$\mathcal F_z=e_z,\mathcal F_{zz}=0$。它是一个可接入的完整局部桥片，但还没有使外端转向固定帽。

外法向和两主曲率（约定第二基本形式为 $N\cdot\mathcal F_{ij}$）为

$$
N=\frac{(n,-f')}{\sqrt{1+(f')^2}},\qquad
k_\phi=-\frac1{(\rho+f)\sqrt{1+(f')^2}},\qquad
k_z=\frac{f''}{(1+(f')^2)^{3/2}}.
\tag{24}
$$

于是

$$
K_\Sigma=-\frac{f''}{(\rho+f)(1+(f')^2)^2}.
\tag{25}
$$

在上接缝的 $\tau=1/10$，有
$p''=2376/125$、$f''=2376/3125>0$；因此存在真实开邻域满足 $K_\Sigma<0$。这不是凸平滑，也不是只在拼接线出现符号不确定的曲率。

同时

$$
\max(|k_\phi|,|k_z|)
\le\max\left(\frac1m,M\right)=\frac{995}{104}<10.
\tag{26}
$$

在有限保留部分 $|z|\le b+\ell=.015<B$，对应柱带点属于 $E_\alpha^B$，水平法向位移不超过 $\delta<\varepsilon_i$，故旋转后的每个有限接缝片都属于 (7) 所允许的包围邻域。

## 4. 全点对 reach 引理：不把曲率界当成 reach

以下证明不仅适用于本多项式。设 $\Gamma$ 是闭 $C^3$ 凸平面曲线，曲率严格为正，按法向角参数化且曲率半径 $\rho\ge m>0$；$f\in C^2(\mathbb R)$ 满足 (22)。这里稍强的平面曲线正则性保证 (23) 本身就是 $C^2$ 参数图；本题的解析 Poisson 曲线满足它。则完整非紧曲面 (23) 有

$$
\boxed{\operatorname{reach}\Sigma\ge
\tau_*:=
\left[
\left(\frac1m+\frac{\delta}{m^2}\right)(1+A^2)+M
\right]^{-1}.}
\tag{27}
$$

### 4.1 同一截面的两个全局几何不等式

支持函数 $h-m$ 是某个凸紧集 $K_0$ 的支持函数，允许 $K_0$ 有退化部分。可直接验证：令
$y(\phi)=x(\phi)-mn(\phi)$，则
$y'=(\rho-m)t$；对固定法向 $n(\phi_0)$，函数
$n(\phi_0)\cdot y(\phi)$ 在离开 $\phi_0$ 的前半圈不增、后半圈不减，故不超过它在 $\phi_0$ 的值。于是这些支持线确实包围 $y$ 的凸包，且各接触值就是 $h-m$。因此

$$
K=K_0+m\overline B_2.
$$

固定 $z$，该截面的凸体是
$K_0+(m+f(z))\overline B_2$。记同层点
$p_\phi=x(\phi)+f(z)n_\phi$、
$p_\psi=x(\psi)+f(z)n_\psi$，弦为 $a_0=p_\psi-p_\phi$。内部半径为 $m+f(z)$ 的切圆盘和凸支持半空间共同给出

$$
|n_\phi\cdot a_0|\le\frac{|a_0|^2}{2m}.
\tag{28}
$$

另一条需要的界是

$$
|n_\psi-n_\phi|\le\frac{|a_0|}{m}.
\tag{29}
$$

为证 (29)，写
$a_0=(y_\psi-y_\phi)+(m+f(z))(n_\psi-n_\phi)$。
凸体 $K_0$ 的两条支持不等式相加给
$(y_\psi-y_\phi)\cdot(n_\psi-n_\phi)\ge0$。
与法向差点乘并用 Cauchy 不等式，立即得到 (29)。这里控制的是整个闭截面任意两点，不只局部角弧。

### 4.2 不同高度的全点对界

取任意
$P=\mathcal F(z,\phi)$、$Q=\mathcal F(w,\psi)$，设

$$
t=w-z,\quad \Delta f=f(w)-f(z),\quad
d_0=Q_{xy}-P_{xy}=a_0+\Delta f\,n_\psi.
$$

直接展开未归一化法向分量：

$$
\sqrt{1+f'(z)^2}\,(Q-P)\cdot N_P
=n_\phi\cdot a_0+
  (\Delta f-f'(z)t)+
  \Delta f(n_\phi\cdot n_\psi-1).
\tag{30}
$$

由 Taylor 积分余项、
$|\Delta f|\le\delta$、(28)–(29) 和
$1-n_\phi\cdot n_\psi=|n_\psi-n_\phi|^2/2$，得到

$$
|(Q-P)\cdot N_P|
\le\frac12\left[
 \left(\frac1m+\frac{\delta}{m^2}\right)|a_0|^2
 +M t^2
\right].
\tag{31}
$$

分母 $\sqrt{1+f'(z)^2}\ge1$ 只会改善上界。又

$$
|a_0|\le|d_0|+A|t|,\qquad
|a_0|^2\le(1+A^2)(|d_0|^2+t^2).
$$

因此

$$
\boxed{|(Q-P)\cdot N_P|
\le\frac{|Q-P|^2}{2\tau_*}}
\quad\text{对所有 }P,Q\in\Sigma.
\tag{32}
$$

### 4.3 从全点对式直接证明法向单射半径

这一步可以自足证明，不必把外部定理当作黑箱。设空间点 $X$ 距 $\Sigma$ 为 $d<\tau_*$。由于 $\Sigma$ 闭且非空，最近点存在。若有两个不同最近点 $P,Q$，在无边界的 $C^2$ 曲面上，一阶极值条件给 $X-P$ 垂直 $T_P\Sigma$，所以 $X-P=\pm dN_P$。等距条件给

$$
|Q-P|^2=2(X-P)\cdot(Q-P)
\le2d\,|(Q-P)\cdot N_P|
\le\frac d{\tau_*}|Q-P|^2.
$$

因 $d<\tau_*$，矛盾。故距离小于 $\tau_*$ 的所有点均有唯一最近点，证明 (27)。该证明同时说明全点对界如何排除远处不同片的近接。

本例精确账本给

$$
\tau_*>0.09499016774462>\rho_{\mathrm{goal}}=.0756.
\tag{33}
$$

这是整条非紧模板的真正 reach 下界。它不是整个未来闭面的 reach，也不声称有限截断带有边界时仍可原样使用无边界切平面。

模板还具有正径向支持：

$$
\mathcal F\cdot N
=\frac{h+f-zf'}{\sqrt{1+(f')^2}}
\ge
\frac{m_{0,\mathrm{lo}}-(b+\ell)A}{1+A^2/2}
>0.65567579748174.
\tag{34}
$$

在 $f=0$ 的其余高度，该支持就是 $h\ge m_0$。旋转不改变 (27) 或 (34)，所以这些界对所有相位一致。

## 5. 两个固定小帽在新包围里仍可暴露

本节真正保留的是旧大帽内部的小闭帽

$$
\widehat C_\pm=
\{P_\pm+a\omega:|\omega|=1,\ |\omega-v_\pm|\le\chi\},
\qquad\chi=\frac1{100}.
\tag{35}
$$

它们各有非空相对内点并含轴点 $q_\pm$。由
$\omega\cdot v_\pm\ge1-\chi^2/2>1/2$，它们确实是 (5) 中的同一球面片，不是另外换了球心或法向。

以上帽为例，在轴方向 $v_+$，活动包围柱的支持至多
$2H^2/L_b+B Z_b/L_b$，球帽支持等于
$(2H^2+z_*Z_b)/L_b+a$。差至少

$$
a+(z_*-B)\frac{Z_b}{L_b}.
$$

对 $|\omega-v_+|\le\chi$，球心线性支持的 Lipschitz 常数不超过 $H+z_*$，活动柱支持的常数不超过 $H+B$。故全相位支持差不小于

$$
g_A=
a+(z_*-B)\frac{Z_b}{L_{b,\mathrm{hi}}}
-\chi(2H_{\mathrm{hi}}+z_*+B).
\tag{36}
$$

相对另一帽，使用包含它的整球，其支持差至少

$$
g_C=2z_*\left(\frac{Z_b}{L_{b,\mathrm{hi}}}-\chi\right).
\tag{37}
$$

两者的有理下界满足

$$
\min(g_A,g_C)>0.07170994764003>\frac7{100}.
\tag{38}
$$

因此每个小帽点均以自己的球面法向，成为每个 $E_\alpha^B$ 的支持点；这给出了可保留的真实固定帽片。下帽由镜像同证。这里只证帽片的可容纳与暴露，不证其边界已有连接。

帽片的外法向径向支持还有

$$
(P_\pm+a\omega)\cdot\omega
\ge
\frac{2H_{\mathrm{lo}}^2+z_*Z_b}{L_{b,\mathrm{hi}}}
+a-(H_{\mathrm{hi}}+z_*)\chi>1.
\tag{39}
$$

同一球面上任意两点对 $P,Q$，有
$|(Q-P)\cdot N_P|=|Q-P|^2/(2a)$。该精确式以后可以用于闭面中保留的球面片；没有把带边界帽本身的切锥忽略。

## 6. 所有相位共同包围内的两个明确固定圆领

由于半径 $m_0$ 的原点圆盘包含于全部 $R_\alpha K$，

$$
W=\operatorname{conv}\bigl(
\overline B_2(0,m_0)\times[-B,B]\ \cup C_+\cup C_-\bigr)
\subset\bigcap_\alpha E_\alpha^B.
\tag{40}
$$

这是真正固定连接片可使用的共同位置范围；不能只在某一个相位检查固定桥的位置。

取

$$
Z_c=\frac1{10},\qquad
c=\frac25,\qquad
w_c=\frac1{100}.
$$

我们证明整个轴向小厚片

$$
\overline B_2(0,1/2)\times
[Z_c-1/200,Z_c+1/200]
\subset W,
\tag{41}
$$

以及它的上下镜像。对任意该区间中的高度 $s$，连结
$\overline B_2(0,m_0)\times\{B\}$ 与固定点 $q_+$。
由于 $(q_+)_z\ge z_*=.3$，所需凸组合权重为

$$
\lambda=\frac{s-B}{(q_+)_z-B}
\le\frac{.105-.09}{.3-.09}=\frac1{14}.
$$

此截面含中心为 $\lambda(q_+)_{xy}$、半径为 $(1-\lambda)m_0$ 的圆盘。又 $|(q_+)_{xy}|\le H+a$，它必含原点圆盘，半径至少

$$
\frac{13m_{0,\mathrm{lo}}-H_{\mathrm{hi}}-a}{14}
=0.51694757856250>\frac12.
\tag{42}
$$

于是可以明确保留两个固定平面环片

$$
J_\pm=\{(r\cos\theta,r\sin\theta,\pm Z_c):
c-w_c\le r\le c+w_c\}.
\tag{43}
$$

它们位于所有相位的共同包围内部；外法向取 $\pm e_z$ 时，径向支持恰为 $.1>\rho_{\mathrm{goal}}$，主曲率为零。这是新条件模型中的真正固定圆领，不是把 R29 或当前 M15 的数值 cut 当作固定平面圆领。

### 6.1 保留片之间的非局部距离

令 $A_\alpha^{\mathrm{seam}}$ 为 (23) 的有限部分
$|z|\le b+\ell$ 经相位旋转后的像。我们已明确给出五个保留片：
$A_\alpha^{\mathrm{seam}},J_+,J_-,\widehat C_+,\widehat C_-$。

它们不同组之间的距离有下列全相位下界：

| 两组 | 距离下界 |
|---|---:|
| 活动带及鞍领 / 任一帽 | $z_*-a-b-\ell=37/200=.185$ |
| 活动带及鞍领 / 任一圆领 | $m_{0,\mathrm{lo}}-(c+w_c)>.24568$ |
| 任一圆领 / 任一帽 | $H_{\mathrm{lo}}-a-(c+w_c)>.67665$ |
| 两圆领 | $2Z_c=.2$ |
| 两帽 | $2z_*-2a=.4$ |

第一、第四、第五行用竖直距离。第二行用
$|x+fn|^2=|x|^2+2fh+f^2\ge m_0^2$ 的水平半径界；第三行用球心的水平半径减去 $a$ 和圆领外半径。每行都严格大于 $2\rho_{\mathrm{goal}}=.1512$。

若 $|Q-P|\ge2\tau$，单位法向总满足
$|(Q-P)\cdot N_P|\le|Q-P|\le|Q-P|^2/(2\tau)$。
所以结合 (32)、球面点对式和平面点对式，全部已保留片之间的法向点对式统一成立，半径可取

$$
\tau_{\mathrm{retained}}
=\min\left(\tau_*,a,\frac12\min\{\text{表中下界}\}\right)
=\frac{37}{400}=.0925>\rho_{\mathrm{goal}}.
\tag{44}
$$

这些片的径向支持统一至少为 $.1$。

**(44) 不是分离片并集的无边界 reach 结论。** 它的精确意义是：未来若有闭 $C^2$ 面精确保留这些片及其切平面，则所有两个点都落在已保留片中的法向点对门已经支付。新连接片上的点，以及它们与旧片的混合点对，仍须另证。

## 7. 共同度量缺口不能由接缝的小振幅隐藏

把 $\Gamma$ 改用单位弧长材料参数 $\theta$，写 $\gamma'(\theta)=t$、$n'(\theta)=\kappa_0(\theta)t$。按 R29 的旋转与材料移位方式尝试

$$
\mathcal F_\alpha(z,\theta)=
\bigl(R_\alpha[\gamma(\theta-\alpha)+f(z)n(\theta-\alpha)],z\bigr).
$$

直接计算得到诱导度量

$$
(1+f'(z)^2)\,dz^2+
\bigl(1+f(z)\kappa_0(\theta-\alpha)\bigr)^2\,d\theta^2.
\tag{45}
$$

Poisson 曲线的 $\kappa_0$ 非常数；在 $f>0$ 的接缝上，第二系数随相位改变。因此本显式模板**不能直接当作 R29 轴对称共同度量的解**。重新参数化经线只能调整第一系数，不能消除这个角向相位项。

这没有排除孤立模板通过整体刚体旋转而等距，也没有证明所有可能的材料重参数化都失败；它只准确指出所需的“核心相位运动加固定外边界”机制尚未接通。本文没有以 $\delta=10^{-6}$ 很小为理由宣称误差满足 G5。该缺陷是构造式中的项，不能靠加密自动消失。

## 8. 明确待解的连接边值问题

下面区分两个问题。第一个只补几何闭合；第二个才补共同度量。两者均未求解。

### 8.1 保留已证模板的纯几何连接

上侧未知活动连接片 $X_\alpha:[0,S]\times S^1\to\mathbb R^3$ 从鞍领外端开始，其两阶边界数据为

$$
\begin{aligned}
X_\alpha(0,\theta)&=(R_\alpha\gamma(\theta-\alpha),b+\ell),&
(X_\alpha)_s(0,\theta)&=e_z,&
(X_\alpha)_{ss}(0,\theta)&=0,\\
X_\alpha(S,\theta)&=((c+w_c)\cos\theta,(c+w_c)\sin\theta,Z_c),&
(X_\alpha)_s(S,\theta)&=-e_r(\theta),&
(X_\alpha)_{ss}(S,\theta)&=0.
\end{aligned}
\tag{46}
$$

参数在边界邻域按这些速度与已有片相接；角向和混合两阶数据由对应的整圈边界函数一并确定。末端匹配固定平面圆领的外圈，后接同一平面环片。要求 $X_\alpha$ 对 $\alpha$ 在 $C^2$ 中连续、周期闭合、正则且全域无自交，并满足完整包围
$X_\alpha\subset E_\alpha^B+\varepsilon\overline B_3$。

固定圆领内圈半径 $c-w_c=.39$ 再通过一个**与相位无关**的固定环形桥 $Y_+$ 连接到 $\widehat C_+$ 的边界圆。$Y_+$ 在内圈附近等于平面环带的继续部分，在帽端附近等于该球面的继续部分，因而两端全 $C^2$ 接合。要求
$Y_+\subset\bigcap_\alpha(E_\alpha^B+\varepsilon\overline B_3)$。
下侧由整 $z$ 镜像构造相同问题；不能只反射某个平均高度槽。

假如这些环形桥都是嵌入并按所述边界配对，中心柱带、两侧活动环带、固定环片、固定桥和两个帽盘在拓扑上组成 $S^2$。但这些“假如”仍是待解边值问题，不是本文已生成的完整像。

全 reach 的一个自足验收门是对完成后的任意点对证明

$$
|(Q-P)\cdot N_P|\le
\frac{|Q-P|^2}{2\rho_{\mathrm{goal}}}.
\tag{47}
$$

第 4.3 节便给全 reach。可只对距离小于 $2\rho_{\mathrm{goal}}$ 的新点对处理，因为其余自动满足；短距离混合点对须落在一个已经认证的共同延伸片中，不能把相邻两块各自的 reach 界直接取最小。

另一可用验收门是已审 R10 的完整正径向支持与曲率组合：完成闭嵌入 $S^2$ 后，若全域
$F\cdot N\ge\rho_{\mathrm{goal}}$ 且
$|\kappa_i|\le1/\rho_{\mathrm{goal}}$，则 R10 给 reach 门。本文只在明确保留片上支付了这些量；未知桥上的全局条件没有被省略。

### 8.2 真正共同度量的活动连接

若要使用 R29 的相位机制，必须另求一条真实活动图；不能先固定 (20) 再假装 (45) 已与共同度量相等。可从原柱带端 $z=b$ 开始，以未知母图 $F_0(s,\theta)$ 和一次冻结的径向 profile $a_g(s)>0$ 求

$$
|F_{0,s}|^2=1,\qquad
F_{0,s}\cdot F_{0,\theta}=0,\qquad
|F_{0,\theta}|^2=a_g(s)^2.
\tag{48}
$$

入口是 $F_0=(\gamma(\theta),b)$、$F_{0,s}=e_z$、$F_{0,ss}=0$，
$a_g(0)=1,a_g'(0)=a_g''(0)=0$。可在内侧另要求 R29 的平顶四阶入口；没有在此选择或优化其系数。

出口若取 (46) 的真正固定平面圆领，则

$$
a_g(S)=c+w_c,\qquad
a_g'(S)=-1,\qquad a_g''(S)=0
\tag{49}
$$

并须满足整个圆周的 Cartesian 两阶边界数据，而不仅是平均半径或高度。母图存在后，才可定义

$$
F_\alpha(s,\theta)=R_\alpha F_0(s,\theta-\alpha);
\tag{50}
$$

轴对称的 (48) 保证其活动区有共同度量，(46) 的圆领两阶旋转等变性才保证与固定外部逐点相接。

为使待解问题不仅是口头“找连接”，也可把 (48) 写成明确的 Gauss–Codazzi 与框架系统。令
$e_1=F_s,e_2=F_\theta/a_g$，第二基本形式在此正交框架中为 $L,M,N$。在足够光滑的内部，

$$
\begin{aligned}
LN-M^2&=-a_g''/a_g,\\
M_s&=a_g^{-1}L_\theta-2(a_g'/a_g)M,\\
N_s&=a_g^{-1}M_\theta+(a_g'/a_g)(L-N),
\end{aligned}
\tag{51}
$$

而位置、框架满足

$$
\begin{aligned}
F_s&=e_1,&F_\theta&=a_g e_2,\\
(e_1)_s&=Ln,&(e_2)_s&=Mn,&n_s&=-Le_1-Me_2,\\
(e_1)_\theta&=a_g'e_2+a_gMn,&
(e_2)_\theta&=-a_g'e_1+a_gNn,&
n_\theta&=-a_gMe_1-a_gNe_2.
\end{aligned}
\tag{52}
$$

入口外法向取核心平面外法向时 $L=M=0,N=-\kappa_0(\theta)$。还要满足 $2\pi$ 周期闭合及零位置/框架单值障碍；局部基本形式相容并不自动支付圆周的全局闭合。

R29 的正 Frenet 分支可作为正则内部的另一表达，但 (49) 的平面圆领在出口有退化边界量，不能擅自声称一个有限正则分支必能到达。若必须借无限层闭合，仍须另付该机制的实际端点、两阶极限和定量几何界。本稿没有证明有限或无限 BVP 的存在，也没有修改当前被冻结的 M15 共同度量。

新解即使满足 (48)–(52)，仍须同时满足第 8.1 节的完整包围、固定帽、嵌入、支持/曲率或全点对 reach 条件。因此这里是一个明确可审的待解系统，而非从基本形式方程直接跳到最终强目标。

## 9. 本次实际计算、来源与结论范围

纯有理脚本为 scripts/db6f-audit-positive-collar-budget.py；正式输出为 notes/2026-11-09-db6f-audit-positive-collar-budget.json。从仓库根目录可执行：

~~~bash
python topics/visible-flexible-closed-surface/scripts/db6f-audit-positive-collar-budget.py \
  --out topics/visible-flexible-closed-surface/notes/NEW-independent-positive-collar-budget.json
~~~

脚本以 SHA-256 绑定 R27、R29、旧双帽 v2 与已审标量报告，输出用排他创建，不能覆盖原报告。平方根由整数 isqrt 得到 $2^{-120}$ 向外有理盒，并用精确平方逐端核对。所有上述十进下界向下显示，上界向上显示；推断使用原 Fraction，不把显示值当作新的精确几何常数。

原始理论来源：

- 本题 results/R27-poisson-c3-core-and-conditional-held-transfer.md：Poisson 核、全角支持极值、曲率半径及已审区间。
- 本题 results/R29-c3-mechanism-interface-and-convex-held-envelope.md：相位机制、径向共同度量、真正圆领两阶接口与未支付的闭合。
- notes/2026-11-09-db6f-audit-poisson-twin-marker-model-v2.md 及其纯 Fraction 账本：旧双帽位置、单向包围与实际点见证。
- 本题 results/R10-positive-support-offset-reach.md：仅在未来完整闭嵌入上可调用的正支持 reach 门。
- Herbert Federer, *Curvature measures*, Transactions of the American Mathematical Society 93 (1959), 418–491, Theorem 4.18：reach 的切平面距离刻画。本稿 §2 用其局部曲率推论；§4.3 的充分性另给自足最近点证明。[原文文本来源](https://static1.squarespace.com/static/5cb91b1c70468025fd21e98b/t/5d37d6d2e6603300016d83dc/1563940577696/federer-curvature-measures-transAMS-1959.pdf)。

**已支付：** 新辅助包围仍留两个强比例；显式保留柱带的 $C^2$ 非凸接缝；其完整非紧延伸的全点对 reach；固定小帽的全相位暴露；共同包围中的具体固定平面圆领；这些保留片之间的支持和所有法向点对预算。

**未支付：** 从鞍领转向圆领、从圆领转向偏轴帽的完整嵌入连接；未知连接片上的曲率、支持与混合点对；共同度量的真实解；全闭族存在与其加密/独立复跑。因此本稿是新的正向几何中间结论，不满足 README 的最终完成标准。
