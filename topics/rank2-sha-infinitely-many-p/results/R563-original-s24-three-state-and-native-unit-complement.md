# R563 — 原六度轴的完整 S24 三态、连续单位逆与 D12 两互补行

日期：2026-11-14。**状态：已证明。**

在 R559 的同一完整六变量来源中，真实两个输出
$H=\delta(c-C)$、$K=\delta(c+C)$ 对原 $\rho_0$ 给六度核，
对第三来源 $h$ 则需要共同覆盖后的整个
$\mathcal S_{24}\otimes\mathcal S_{24}$。
本篇支付其准确三态核心、所有独立深度矩形与完整连续单位逆。

对原 native carry 测试，单位逆还有实际支撑上的简化：
$C$ 为单位使双重缩小项整条消失，最终得到**同一 $H,K$ 双单位域**
内 $D_{12}$ 为单位与 $D_{12}$ 深的两个互补行。
浅环带、深尾、原 $Y,W$ 权、全部单位条件及常数 log 质量均显示保留。
没有把新第三态认作旧两输入小格，也未由此给原余域赋零。

## 1. 来源与完整框架

沿用 [R559](R559-original-plane12-square-core-and-native-one-sided-carry.md)
的全部射线、原周期、固定坏集和实际输入，特别
$$
\omega^2+\omega+1=0,\quad\delta=1+2\omega,\quad
b=17,\quad\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad p\ge71 .
\tag{1}
$$
原源 $\rho_0=-\nu_\sigma^{\otimes6}/84$，
$\eta=\omega^2\mathsf H_*\rho_0$，
$h=\eta+\rho_0/2$ 中的 $\mathsf H$ 是 R541 的原二输入矩阵。
本篇字母 $H$ 以下专指真实输出，不指 $\mathsf H$。

记 R559 的
$$
H_0=\xi_1-\xi_3+x=\delta C,\qquad
D=\mathscr D=F-c,\qquad N(D)=12,\qquad R=2\delta D .
$$
$D$ 与 $D_0=F-C$、$D_j=F-\omega^{2j}C$ 不同。
使用同一个真实 $C$ 投影 $\mathcal P_C$，定义
$$
\mu_0=\mathcal P_C\rho_0,\qquad \mu_+=\mathcal P_Ch .
\tag{2}
$$
两个物理输出是
$$
H=\delta c-H_0=\delta(c-C),\qquad
K=\delta c+H_0=\delta(c+C).
\tag{3}
$$
它们各范数 $6$、互相正交，并正交于完整四个伴随
$R,T_1,T_2,T_3$。此处 $T_i$ 是 R559 (14)–(15) 的原三个实际行，
没有遗忘任何一个。

对 $\mu_+$ 取共同覆盖 frame
$$
(2H,2K,R,2T_1,2T_2,2T_3).
\tag{4}
$$
它相对 R559 的 $(c,H_0,R,T_1,T_2,T_3)$ 行列式因子为 $64\delta$，
完整行列式与范数为
$$
\det=-2639609856-465813504\omega,\qquad
N(\det)=2^{28}3^{12}13^3\,19 .
\tag{5}
$$
故在当前处是完整同一格的可逆坐标变换。

$2H,2K$ 的原两态整数行分别为
$$
\begin{array}{c|rrrrrr}
&\xi_1&\xi_2&\xi_3&x&c&d_0\\ \hline
2H&-2&0&2&-2&2+4\omega&0\\
2K&2&0&-2&2&2+4\omega&0\\
(2H)\mathsf H&-2&0&2&-2&1-\omega&3\\
(2K)\mathsf H&2&0&-2&2&1-\omega&3 .
\end{array}
\tag{6}
$$
原两行模 $2$ 没有奇因子，后两行各有两个；其半特征均为
standard even，不出现未付 flat twist。

更具体地，$\mu_+$ 在旧 $(2c,H_0)$ 上有
$$
\mathcal S_4^{\rm even}\otimes
\operatorname{span}\{B_0,B_3\},\qquad
B_0=-y_\wp\sigma^3,\quad B_3=\sigma^3
$$
的六个实际系数，全部仍取值于 $(R,T_1,T_2,T_3)$ 来源。
$\mathcal S_4^{\rm even}$ 整基为
$U_a=\sigma^4x_\wp^a$，$a=0,1,2$。
换到 (4) 的六条核是
$$
U_a(\delta(s+t))B_j(2(t-s)),\qquad
a=0,1,2,\quad j=0,3.
\tag{7}
$$
两轴度数均为 $4N(\delta)+3N(2)=24$，交叉项为 $12-12=0$。
所以它们确属整个 $\mathcal S_{24}\otimes\mathcal S_{24}$。
(7) 只描述原 $\mu_+$；下文施加 $K_H$ 后不假设新源仍在这六维小格内。

## 2. whole S24 平方与完整三态

$K_H,K_K$ 表示已提出外部 $\lambda$ 的完整 theta 核。
当前射线上
$$
g_\pi\equiv43+24\omega\pmod{48},\qquad
g_\pi^2\equiv25\pmod{48}.
$$
$25=1+24$ 的完整中心满足
$$
(25^2-1)/24=26\in2\mathbb Z .
\tag{8}
$$
因此平方与恒等在全 Heisenberg 群上的交织相同，包括 Weyl 中心。
用真实锚
$\Theta(2\delta z)\in\mathcal S_{24}$：它的实际核心为
$\beta=-\lambda$，归一特征为 $-1$，平方为 $+1$。
于是付清绝对标量：
$$
\boxed{K_{24}^2=I\quad\text{在整个标准 even }\mathcal S_{24}\text{ 上}.}
\tag{9}
$$
这不是从有限谱样本推得。

$\mu_0$ 的两个输出是 R559 的原整个 $\mathcal S_6$ 核，
所以两核均为归一 $-1$。对 $\mu_+$，原 $2c$ 的 whole 核为
$R_c$，$H_0$ 的 whole odd3 核为 $-1$，外部总量为 $\lambda^2$。
又 (3) 的行列式 $2\delta$ 为单位，故
$$
H,K\in p\mathcal O
\quad\Longleftrightarrow\quad c,H_0\in p\mathcal O .
$$
两坐标同时缩放也一致。因此在原 $\mu_+$ 上准确有
$$
K_HK_K\mu_+=-R_c\mu_+=-\mu_+ .
\tag{10}
$$
各算子在完整张量格中作用不同轴，所以它们交换。

现在定义真实第三态
$$
\boxed{\mu_-=K_H\mu_+.}
\tag{11}
$$
这是整个 (4) 来源上的实际操作，仍保四伴随。
由 (9)–(10) 得
$$
K_H\mu_-=\mu_+,\quad K_K\mu_+=-\mu_-,\quad K_K\mu_-=-\mu_+.
$$
记 $\boldsymbol\mu=(\mu_0,\mu_+,\mu_-)^t$，则
$$
\boxed{
A_H=
\begin{pmatrix}-1&0&0\\0&0&1\\0&1&0\end{pmatrix},\qquad
A_K=
\begin{pmatrix}-1&0&0\\0&0&-1\\0&-1&0\end{pmatrix}.
}
\tag{12}
$$
这是完整源矩阵，不是只对 $Y$ 或 $W$ 边际成立。

原反射的实际几何是
$$
R_c:(H,K,D,T)\longmapsto(-K,-H,D,T).
$$
所以 $R_cK_HR_c=K_K$，并得到
$$
R_c=\operatorname{diag}(-1,1,-1)
\quad\text{在 }\boldsymbol\mu\text{ 上}.
\tag{13}
$$

R559 的 $D$ 两层核心与 $H,K$ 核因正交而交换。因此
$$
\boxed{
B:=K_D^2=\operatorname{diag}(1,-1,-1)=A_HA_K=A_KA_H
\quad\text{在 }\boldsymbol\mu\text{ 上}.
}
\tag{14}
$$
这里 $K_D^2$ 指实际 $\mathcal S_{144}$ 的两层归一算子。
(14) 的外部标量是 $\lambda^2$。
**它在新 $\mu_-$ 上不是 $-R_c$。**
R559 的 $K_D^2=-R_c$ 只在原两态成立；把那一式延到 $\mu_-$
会把 (14) 的末个 $-1$ 错改成 $+1$。

### 2.1 三态的整性与非退化

$\mu_0,\mu_+$ 都是整来源，$K_H$ 是 (9) 的整自同构，故 $\mu_-$
也是整来源。三者均非零。一个直接原输入检查是把前四解析参数取为
$(t,s,-t,t)$。它在纯 $C$ 旋转下已经不变，原 $\mu_0$ 的
$t^3scd_0$ 系数为 $1/84$，$\mu_+$ 的 $t^3sc^2$ 系数为
$(2+\omega)/336$。这是原 $\mathsf H$ 的二次项直接相乘所得；
两个数及所需阶乘在当前处均为单位。故两原态是 primitive，
而 $\mu_-$ 的 primitive 性由整自同构 $K_H$ 保留。

$B$ 与 $R_c$ 的三个不同共同特征
$(+,-),(-,+),(-,-)$ 使三态线性独立。投影
$$
\frac{I+B}{2},\qquad
\frac{(I-B)(I+R_c)}4,\qquad
\frac{(I-B)(I-R_c)}4
$$
是整算子，逐个提取三态。连同 primitive 性，这证明三态张成
完整 theta 格内的饱和自由 $\mathcal O$ 子格。
没有以 $\mu_-$ 的反射奇性认定它可因式为原 $\sigma(c)$；
它仍只按已付的整个 $\mathcal S_{24}\otimes\mathcal S_{24}$ 使用。
同样，未给 $\mu_-$ 免费添加 $C$ 旋转不变性或旧 odd3 单轴核心。

## 3. 所有实际深度矩形及同源异域运输

令 $P_{H,s}$ 只把物理 $H$ 乘 $s$，固定 $K,D,T$；其他轴同理。
由完整独立轴的限制，任意 $r,t,m\ge0$ 都有
$$
\boxed{
\boldsymbol\mu|_{\{H\in p^r,\ K\in p^t,\ D\in p^{2m}\}}
=\lambda^{r+t+2m}
(P_{H,\kappa^r}P_{K,\kappa^t}P_{D,\kappa^{2m}})_*
A_H^rA_K^tB^m\boldsymbol\mu .
}
\tag{15}
$$
每个深条件独立保留，四伴随全部不动。
这里只支付 $D$ 的偶深，不把未知的一层 $D$ 来源当三态闭合。

特别 $H,K$ 同深 $r$ 与 $D$ 深 $2r$ 的归一来源均为
$\lambda^{2r}B^r\boldsymbol\mu$。因此存在真实全域运输
$$
\mathcal T_r=P_{H,\kappa^r}P_{K,\kappa^r}P_{D,\kappa^{-2r}},
$$
$$
\boxed{
\boldsymbol\mu|_{\{H,K\in p^r\}}
=(\mathcal T_r)_*
\bigl(\boldsymbol\mu|_{\{D\in p^{2r}\}}\bigr).
}
\tag{16}
$$
$\mathcal T_r$ 在其显示源域上整且可逆到目标域。
它改变原 $Y,W$；不是两域原积分不换测试就相等。

原物理行的完整转置可统一写成：把 $(H,K,D)$ 乘 $(s,t,e)$ 时，
$$
\begin{aligned}
c_{s,t}&=(sH+tK)/(2\delta),&
C_{s,t}&=(tK-sH)/(2\delta),\\
(D_0)_{s,t,e}&=eD+sH/\delta,&
(E_0)_{s,t,e}&=eD+(-6sH+7tK)/\delta,\\
Y_{s,t,e}&=Y_0+(sH+tK)/(2\delta)-eD/12,\\
W_{s,t,e}&=W_0+\tfrac32(sH+tK)-e\delta D/4,\\
G_{s,t,e}&=G_0+(3-2\omega)(sH+tK)/(2\delta)
-(3-2\omega)eD/12 .
\end{aligned}
\tag{17}
$$
设 $d_*=d_0+(1+3\omega)D/12$，它属于固定三伴随空间，则
$$
\begin{aligned}
u_{s,t,e}&=\frac{\omega(sH+tK)}{4\delta}
+\frac{1-\omega}{2}d_*-\frac{4+5\omega}{24}eD,\\
L_{s,t,e}&=\frac{(1+3\omega)(sH+tK)}{2\delta}
+d_*-\frac{1+3\omega}{12}eD .
\end{aligned}
\tag{18}
$$
原 carry 支撑始终为
$$
\{eD+sH/\delta\in p^n,\ (tK-sH)/(2\delta)\text{ 为单位}\}.
\tag{19}
$$
其多项式的第一参数仍除以原 $\kappa^n$；
第二、第三参数逐项用 (17)，原 $Y,W$ 的单位条件也分别用 (17)。
(16) 正是 $(s,t,e)=(\kappa^r,\kappa^r,\kappa^{-2r})$；
分母不能省略。

## 4. 全连续测试的完整单位逆

对连续三列测试 $f$，记
$$
S_Hf=f\circ P_{H,\kappa},\quad
f_{H,0}=f|_{H=0},\qquad
\mathcal U_H=(I-\lambda A_HS_H)^{-1},
$$
$K$ 同理。所有其他坐标在 $f_{H,0}$ 中原样保留。

先支付常数部分的整逆。当前 $\pi_0$ 的迹为偶数。
若 $1+\lambda$ 或 $1-\lambda$ 非单位，分别迫
$\operatorname{Tr}(\pi_0)\equiv1$ 或 $-1\pmod p$。
Hasse 界 $|\operatorname{Tr}(\pi_0)|\le2\sqrt p<p-1$，
结合偶性排除两种情况。因此
$$
1+\lambda,\ 1-\lambda,\ 1-\lambda^2\in\mathcal O^\times,\qquad
(I-\lambda A)^{-1}=\frac{I+\lambda A}{1-\lambda^2}
\quad(A=A_H,A_K).
\tag{20}
$$

对任意整连续测试，准确公式是
$$
\boxed{
\mathcal U_Hf
=(I-\lambda A_H)^{-1}f_{H,0}
+\sum_{r=0}^{\infty}\lambda^rA_H^r
\{f\circ P_{H,\kappa^r}-f_{H,0}\}.
}
\tag{21}
$$
收敛由连续函数在紧空间上的一致连续性给出：
括号一致趋于零，矩阵及 $\lambda$ 均整且有界。
(20) 支付常数极限，不能用不收敛的常数几何级数替代。
直接望远镜相消证明 (21) 为双边逆，且算子范数不超过 $1$。
$K$ 的同式完全成立；两逆交换。

以 $\langle f,\boldsymbol\mu\rangle=\sum_i\int f_i\,d\mu_i$ 记配对。
由于 (12) 为对称矩阵，完整单位行准确为
$$
\boxed{
\langle f,\boldsymbol\mu\rangle
=\left\langle\mathcal U_H\mathcal U_Kf,\
\boldsymbol\mu|_{\{H,K\text{ 为单位}\}}\right\rangle .
}
\tag{22}
$$
它对原单位指标延零的 log、真实 carry、多项式及其任意组合均适用。
每个逆项的实际切集按 (17)–(19) 运输。
负幂只在其单位支撑上延零后使用 (21)，不把它当全空间多项式
并随意使用 $\kappa^{-j}$ 的形式逆。

## 5. 同一个 native 测试：交叉项严格消失

取 R559 (11) 的原完整三列测试
$$
\begin{aligned}
f_0&=\tfrac32\,1_{\mathcal E_n}q_0\ell
(1_{\mathcal B}+1_{\mathcal B^c}),\\
f_+&=1_{\mathcal E_n}q_0\ell
(1_{\mathcal B^c}-1_{\mathcal B}),\qquad f_-=0 ,
\end{aligned}
\tag{23}
$$
其中 $\mathcal E_n=\{D+H/\delta\in p^n,\ C\text{ 为单位}\}$，
$q_0=\widehat P_p(D_0/\kappa^n,E_0,G)/(b\Omega^6)$，
$\ell$ 是原 $Y,W$ 中央差，$\mathcal B=\{u\in p,L\text{ 为单位}\}$，
$\mathcal B^c=R_c\mathcal B$。这就是原 $I=h(\Phi_1-\Phi_2)$：
$$
2\lambda I=\langle f,\boldsymbol\mu\rangle .
\tag{24}
$$

$f$ 的每一列都支撑于 $C=(K-H)/(2\delta)$ 为单位。
同时缩放 $H,K$ 把 $C$ 变为 $\kappa C$，故
$$
S_HS_Kf=0
$$
是整个实际函数恒等式。令 $T_H=\lambda A_HS_H$、
$T_K=\lambda A_KS_K$，二者交换。将
$(I-T_H)(I-T_K)$ 乘到两边即可证明
$$
\boxed{\mathcal U_H\mathcal U_Kf=\mathcal U_Hf+\mathcal U_Kf-f.}
\tag{25}
$$
这里已经使用 (21) 的真实连续逆；不是丢弃不收敛级数中的交叉项。
于是 (22)–(25) 将原 $I$ 完整搬到同一个双单位域，只有两条
单轴转置。新 $\mu_-$ 行仍保留，未按奇性或旧小格删除。

## 6. 实际 D 单位与深两互补行

记 $\mathcal U=\{H,K\text{ 为单位}\}$。
在此域内，原 $\mathcal E_n$ 迫 $D$ 为单位。
$K$ 缩放不改变 $D_0=D+H/\delta$，因此
$$
\mathcal U_Kf\text{ 在 }\mathcal U\text{ 内仍支撑于 }D\text{ 为单位}.
$$
相反，$H$ 缩放 $r\ge1$ 的支撑是
$$
D+\kappa^rH/\delta\in p^n .
\tag{26}
$$
它迫 $D$ 深。若 $D$ 为单位，则 $f_{H,0}=0$，(21) 只有
$r=0$ 项，所以 $\mathcal U_Hf=f$。若 $D$ 深，则 $f=0$、
$\mathcal U_Kf=0$。结合 (25)，得到完整分区
$$
\boxed{
(\mathcal U_H\mathcal U_Kf)|_{\mathcal U}
=1_{\{D\text{ 为单位}\}}\mathcal U_Kf
+1_{\{D\in p\}}\mathcal U_Hf.
}
\tag{27}
$$
因此同一个原 residual 的准确表达是
$$
\boxed{
2\lambda I=
\left\langle1_{\mathcal U\cap\{D\text{ 为单位}\}}\mathcal U_Kf,
\boldsymbol\mu\right\rangle+
\left\langle1_{\mathcal U\cap\{D\in p\}}\mathcal U_Hf,
\boldsymbol\mu\right\rangle .
}
\tag{28}
$$
两项确实覆盖全部，不另删 $D$ 单位补域。

### 6.1 全部浅环带都是一个准确项

若 $1\le j<n$，在 $\mathcal U\cap\{v_p(D)=j\}$ 上，
(26) 仅可能由 $r=j$ 满足。$f_{H,0}=0$，故
$$
\boxed{
\mathcal U_Hf
=\lambda^jA_H^j f\circ P_{H,\kappa^j}
\quad\text{在 }\mathcal U\cap\{v_p(D)=j\}\text{ 上}.
}
\tag{29}
$$
其剩余条件仍是
$D+\kappa^jH/\delta\in p^n$，原 $Y,W,C,u,L$ 全按 (17)–(19)。
这并不是整条环带不带条件的返回。

### 6.2 深尾含准确常数质量

在 $\mathcal U\cap\{D\in p^n\}$ 上，$r<n$ 的 $f\circ
P_{H,\kappa^r}$ 全为零。记 $f_r=f\circ P_{H,\kappa^r}$、
$f_\infty=f_{H,0}$。从 (21) 得
$$
\boxed{
\mathcal U_Hf=
\lambda^nA_H^n\left\{
(I-\lambda A_H)^{-1}f_\infty+
\sum_{r=0}^{\infty}\lambda^rA_H^r(f_{n+r}-f_\infty)
\right\}.
}
\tag{30}
$$
$f_\infty$ 支撑于真实 $D\in p^n$，且 $C=K/(2\delta)$ 为单位。
它仍含完整 $q_0$、原 log 质量和两个 strip 指标。
未使用 R557 的另一原网格零质量来删它。

在该域，$r\ge1$ 时所有 mod $p$ 单位/深指标已经等于极限指标。
第一 carry 参数的差是 $\kappa^rH/\delta$，其余参数与
原 $Y,W$ 的差有至少深度 $n+r$。准确多项式整性和
单位 log 属于 $p\mathcal O$ 给
$$
f_{n+r}-f_\infty\in p^{r+1}\mathcal O^3,\qquad r\ge1 .
\tag{31}
$$
这给深尾严格误差，但不把其 $r=0$ 行或常数项赋零。

在 (28) 的 $K$ 逆一侧，支撑 $D+H/\delta\in p^n$ 完全不变。
对 $r\ge1$，$C=(\kappa^rK-H)/(2\delta)$ 自动为单位；
其余 mod $p$ 指标亦等于 $K=0$ 的极限指标。
第一 carry 参数没有变化。多项式差乘原单位 log 属于
$p^{r+1}\mathcal O$，但 $Y,W$ 的 log 差一般只有 $p^r$，故准确界为
$$
\boxed{f\circ P_{K,\kappa^r}-f_{K,0}\in p^r\mathcal O^3.}
\tag{32}
$$
更明确地，在该真实支撑上写
$Y_\infty=Y_{1,0,1}$、$W_\infty=W_{1,0,1}$，
$q_\infty=q_0|_{K=0}$，并令
$$
v_\infty=
\left(\tfrac32(1_{\mathcal B|K=0}+1_{\mathcal B^c|K=0}),
1_{\mathcal B^c|K=0}-1_{\mathcal B|K=0},0\right)^t .
$$
所有这些指标对 $r\ge1$ 都已稳定。保原
$\mathcal E_\infty=\{D+H/\delta\in p^n,\ -H/(2\delta)\text{ 为单位}\}$，
实际首项为
$$
\boxed{
\begin{aligned}
f\circ P_{K,\kappa^r}-f_{K,0}
={}&1_{\mathcal E_\infty}\,q_\infty(p-1)\kappa^rK
\left\{
\frac{1_{Y_\infty\text{ unit}}}{2\delta Y_\infty}
-\frac{3\,1_{W_\infty\text{ unit}}}{2W_\infty}
\right\}v_\infty\\
&\hspace{3em}+p^{r+1}\mathcal O^3,\qquad r\ge1 .
\end{aligned}}
\tag{32a}
$$
分母只在对应单位指标内使用。二阶 log 余项有深度
$2r\ge r+1$；多项式差乘一次 log 变化也有此深度。
(32) 已足以保证 (21) 的一致收敛，没有使用未付的首项抵消。
常数项仍是 $(I-\lambda A_K)^{-1}f_{K,0}$。它一般不为零，
并仍在 (28) 的 $D$ 单位补域。

## 7. 与原算术行及负矩接口的准确界限

原已知算术返回仍是 R556/R557 的
$$
\langle(3\,1_{\mathcal E_n}q_0\ell,0,0)^t,\boldsymbol\mu\rangle
=3\beta^n(J'_S-6\delta J'_T).
\tag{33}
$$
对 (33) 也可用同一 (22)–(27)，无需更换来源或归一。
但 (23) 另含真实 strip 指标及 $\mu_+$ 行，因此 (33) 的零
不自动使 (28) 两项归零。若用原两中央同时零，可以且仅可以把
(23) 第一列改写为
$$
-\tfrac32\,1_{\mathcal E_n}q_0\ell
(1-1_{\mathcal B}-1_{\mathcal B^c})
$$
而保留其余两列。该式显示的是实际补域，不能将它删去。

$\mu_0$ 的完整核可直接用 R559 §6 与
[R533](R533-original-degree-six-two-variable-kernels-and-negative-moment-interface.md)
的 $F_B,F_P$，其第二输出和四伴随仍完整。
新 $\mu_+,\mu_-$ 则按整个 $\mathcal S_{24}\otimes\mathcal S_{24}$
使用，不能把 R533 的两条六度负矩零免费延到它们。
同样，(15) 对 $D$ 只支付偶深；若用它归一 (29) 的奇环带，
必须保归一后剩余的一层条件。

本篇把原 residual 变成同一实际三态、同一双单位域上的两个
完整互补积分，并支付全部浅环带与准确深尾。还需证明这些
实际行与原算术条件的进一步关系；本篇未完成主目标。

## 8. 精确证书

- [check-r563-original-s24-three-state-and-native-unit-complement.js](../scripts/check-r563-original-s24-three-state-and-native-unit-complement.js)
- [check-r563-original-s24-three-state-and-native-unit-complement.json](../scripts/check-r563-original-s24-three-state-and-native-unit-complement.json)

脚本仅用 BigInt 有理数及 $\mathbb Q(\omega)$ 运算，检查完整
覆盖 frame、原两态半特征、whole24 中心、三态全矩阵、
不能延长的 $-R_c$ 身份、原 primitive 系数，以及 (17) 的
全部原物理行。正文 (21)–(32) 另给完整连续证明和实际切集，
不是用有限采样替代这些函数恒等式。
