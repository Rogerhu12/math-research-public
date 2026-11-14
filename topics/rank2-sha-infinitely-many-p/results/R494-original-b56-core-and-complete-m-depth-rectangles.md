# R494 — 原 B56 的绝对核心与同一三态的完整 W/Q/U 深度矩形

日期：2026-11-14。**状态：已证明。**

在 R488 的原三个实际来源中，新增混合轴
$B=A+3\delta c$ 的完整核心准确是 $R K_W R$。
这个等式以整个 degree $56$ 的 Heisenberg 中心和
$\Theta(2\gamma z)$ 的原绝对锚证明。
由同一完整输入的两个整坐标变换，原 $Q,U$ 核也随即确定。
于是 R465 的原坐标 $(W,Q,U,R_1,R_2,R_3)$ 中，
三个轴的任意独立深度及后三轴的共同深度全部在同一个三态中返回。

本篇给出每个真实物理管、完整乘积标量和一个不同像格的返回身份。
没有把来源算子相同误写成物理域相同，也没有删去任何补域。

## 1. 同一个原联合的两次正交变换

沿用 R488 的固定 ray、$\chi=\chi_{29,p}\in\{1,-1\}$，
以及
$$
\lambda=-\bar\pi_0^{-1},\qquad
\kappa=p/\bar\pi_0^2,\qquad
A=t_1+t_2+t_3+t_4.
\tag{1}
$$
原独立输入是 $(t_1,t_2,t_3,t_4,c,d_0)$，
$\mathbf R=(R_1,R_2,R_3)$ 保 R465、R488 的原定义。
令
$$
\boxed{B=A+3\delta c,\qquad Q=3\delta A+29c.}
\tag{2}
$$
真实两轴矩阵满足
$$
\begin{pmatrix}1&3\delta\\3\delta&29\end{pmatrix}
\operatorname{diag}(29,1)
\begin{pmatrix}1&3\delta\\3\delta&29\end{pmatrix}^{\!*}
=\operatorname{diag}(56,1624),\qquad\det=56.
\tag{3}
$$
所以 $B,Q$ 同时深与 $A,c$ 同时深是同一个完整整域。

在对偶变量 $(b,q)$ 中，原前五输入来源为
$$
\mathcal F(b,q,\mathbf r)
=\mathcal C(b+3\delta q,\mathbf r)\sigma(3\delta b+29q),
\tag{4}
$$
其中 $\mathcal C$ 是 R488(8) 的完整四变量来源，未将
$\mathbf r$ 置零。两轴都恰有平凡半特征：原 $\mathcal C$ 的
odd 特征与第五个 sigma 的 odd 特征相乘为一。
式 (3) 消掉 Gaussian 交叉，故
$$
\mathcal F\in
\mathcal S_{56}\otimes\mathcal S_{1624}
\otimes\mathcal S_{60}\otimes\mathcal S_{2310}\otimes\mathcal S_{4466}.
\tag{5}
$$
与独立 $\sigma(z_d)$ 相乘，再保原 $-1/84$，就是原 $\rho_0$。
所有格在当前处整；这使用原整变换及首阶单位张量基，
不从边际函数猜完整归属。

原两个输出进一步是
$$
W=B+4d_0,\qquad U=B-14d_0,
\tag{6}
$$
$$
\begin{pmatrix}1&4\\1&-14\end{pmatrix}
\operatorname{diag}(56,1)
\begin{pmatrix}1&1\\4&-14\end{pmatrix}
=\operatorname{diag}(72,252),\qquad\det=-18.
\tag{7}
$$
因此 $W,U$ 同时深与 $B,d_0$ 同时深也是同一个完整整域。
(3)、(7) 都保 $Q$ 或 $d_0$ 及全部 $\mathbf R$，没有遗忘
任一原独立事件。

## 2. 整个 degree56 的四挠算子

固定 R416 的 canonical lift
$$
(\mathsf T_t^{(N)}F)(z)
=e^{-N\eta_t(z+t/2)}F(z+t).
$$
在 $\mathcal S_{56}$ 上取
$$
X=\mathsf T_{1/56}^{(56)},\qquad
Z=\mathsf T_{\omega/56}^{(56)},\qquad
Xe_j=\zeta_{56}^je_j,\quad Ze_j=e_{j+1}.
\tag{8}
$$
有 $X^{56}=Z^{56}=I$、$XZ=\zeta_{56}ZX$。
对 $t=(s+r\omega)/4$，完整中心直接给
$$
\boxed{\mathsf T_t^{(56)}e_j
=i^{\,s(j+7r)}e_{j+14r}.}
\tag{9}
$$
这与 degree72 的 $i^{s(j+r)}$ 不同；不能沿用后者的相位。

记
$$
J_{56}=\frac14\sum_{t\in E[4]}\mathsf T_t^{(56)},\qquad
H_{2,56}=\sum_{t\in E[2]}\mathsf T_t^{(56)},\qquad
B_{2,56}=H_{2,56}/2-I.
\tag{10}
$$
对固定 $r$ 先求 (9) 的 $s$ 和，只在
$j+7r\equiv0\pmod4$，即 $r\equiv j\pmod4$ 时留下。
因此
$$
\boxed{
J_{56}e_j=e_{15j},\qquad
B_{2,56}e_j=(-1)^je_{29j+28}.}
\tag{11}
$$
第二式也可直接由 $r,s\in\{0,2\}$ 得到。
两算子交换、平方为一，而且
$$
D_{56}:=J_{56}B_{2,56},\qquad
D_{56}e_j=(-1)^je_{43j+28}.
\tag{12}
$$
特别四挠和 $J_{56}$ 是这里的真实可逆算子，
不是一个可自由删除中心的平凡平均投影。

## 3. 完整 ordinary 核的绝对相位

当前 ray 在 $2\cdot56=112$ 上为
$$
g=\pi_0/\bar\pi_0\equiv43+56\omega\pmod{112}.
\tag{13}
$$
按 (8) 的同一对称 lift，
$$
\mathsf T_{g/56}^{(56)}=-X^{43},\qquad
\mathsf T_{g\omega/56}^{(56)}=-Z^{43}.
\tag{14}
$$
第一式的格周期交叉指数是 $(-1)^{43}$；
第二式用 $g\omega=-56-13\omega$，给同一个负号。
(12) 准确满足
$$
D_{56}XD_{56}^{-1}=-X^{43},\qquad
D_{56}ZD_{56}^{-1}=-Z^{43}.
$$
所以整个真实 $K_{56}$ 与 $D_{56}$ 只差一个标量。
这里比较的是完整 lift，不是仅比较 $g\bmod56$。

绝对标量用原非零来源
$$
F_{\rm an}(z)=\Theta(2\gamma z)\in\mathcal S_{56}
\tag{15}
$$
确定。$[2]^*\mathcal S_{14}$ 的标准基由
$$
e_{2j}+e_{2j+28},\qquad 0\le j<14
$$
张成。由 (11)，$J_{56}$ 和 $B_{2,56}$ 都逐个固定这些向量；
$F_{\rm an}$ 属于这个真实拉回空间。另一方面 $\Theta$ 的原
完整 core 是 $-\lambda$，而 $2\gamma$ 是当前处单位，
故 $K_{56}F_{\rm an}=-F_{\rm an}$。
这严格支付整个空间的绝对式
$$
\boxed{K_{56}=-J_{56}B_{2,56},\qquad K_{56}^2=I.}
\tag{16}
$$
也得到 $J_{56}H_{2,56}=H_{2,56}$。整个证明没有使用未知中央导数。

## 4. quarter 中独立 sigma 的格半特征

记 R488 的三个实际来源为
$$
e_0=\rho_0,\quad e_1=\rho_1=K_We_0,\quad
e_2=-\frac14\sum_{t\in E[4]}\mathsf T_{t,W}^{(72)}e_0.
\tag{17}
$$
在 (6) 的完整正交变换下，每个真实 $W$ 平移准确分成
$$
\mathsf T_{t,W}^{(72)}e_0
=-\frac1{84}
(\mathsf T_{t,B}^{(56)}\mathcal F)
(\mathsf T_{4t}^{(1)}\sigma).
\tag{18}
$$
$Q,\mathbf R$ 的 Gaussian 交叉为零，
$U$ 轴的交叉是 $56-56=0$。所以 (18) 保全部伴随。

设 $t=(m+n\omega)/4$。最后一个因子是
$$
\mathsf T_{4t}^{(1)}\sigma
=(-1)^{m+n+mn}\sigma
=\begin{cases}
+\sigma&t\in E[2],\\
-\sigma&t\in E[4]\setminus E[2].
\end{cases}
\tag{19}
$$
该负号不能省略。将 (19) 代入 R416 的
$K_W=(G_{4,W}-2H_{2,W})/4$，恰得完整来源关系
$$
\boxed{
e_1=-J_{56}e_0,\qquad
e_2=(J_{56}-H_{2,56}/2)e_0.}
\tag{20}
$$
这同时证明三个状态全部仍在 (5) 乘独立 $\mathcal S_1$
的同一个整张量格中。特别每态都保独立 $\sigma(d_0)$ 因子；
没有把一个只在边际相等的来源拿来交换限制。

对 $t\in E[2]$，$4t$ 是偶格点，(19) 为正，因而
$H_{2,B}=H_{2,W}$ 在这个三态空间上准确相同。
由 R488 的 $K_WH_2=-H_2$，可逐项求出
$$
\begin{aligned}
B_2e_0&=-e_0-e_1-e_2,&
B_2e_1&=e_2,& B_2e_2&=e_1,\\
J_{56}e_0&=-e_1,&
J_{56}e_1&=-e_0,&
J_{56}e_2&=e_0+e_1+e_2 .
\end{aligned}
\tag{21}
$$
这里 $B_2$ 表示 (10) 在实际三态上的限制。

结合 (16)，得到真正的混合 $B$ 核
$$
\boxed{
K_Be_0=e_2,\qquad K_Be_2=e_0,\qquad
K_Be_1=-e_0-e_1-e_2.}
\tag{22}
$$
在 R488 的记号 $R=K_A^2$ 下，这就是
$$
\boxed{K_B=R K_W R.}
\tag{23}
$$
两个来源算子在同一三维空间上满足
$$
K_BK_W=K_WK_B=B_2,\qquad B_2^2=I.
\tag{24}
$$
按 $e_0,e_1,e_2$ 列基，
$$
K_B=\begin{pmatrix}0&-1&1\\0&-1&0\\1&-1&0\end{pmatrix},
\qquad
B_2=\begin{pmatrix}-1&0&0\\-1&0&1\\-1&1&0\end{pmatrix}.
\tag{25}
$$
(23) 是实际 normalized core 的相等；其物理域仍须区别，见 §8。

## 5. 原 Q、U 核由同一个完整双深域确定

R488 的四态给
$$
K_AK_c=-\chi I
$$
在 $e_0,e_1,e_2$ 上成立。对 $e_1,e_2$，这是
$\chi\tau_{k+1}$ 与 $-\tau_{k-1}$ 的准确抵消；
对原 $e_0$ 是原 odd29 与独立 sigma 标量的乘积。

由 (3)，$A,c$ 同时深和 $B,Q$ 同时深是同一个域。
两个坐标系中的共同缩放都是 $\kappa$，
其外部标量同为 $\lambda^2$，故
$$
K_BK_Q=-\chi I.
$$
整个 $K_{56}$ 已由 (16) 支付平方一，且 $B,Q$ 是独立张量轴，
因此可严格消去它，得到
$$
\boxed{K_Q=-\chi K_B.}
\tag{26}
$$
这只对本文的完整三态断言，不把整个
$\mathcal S_{1624}$ 核误称为同一个小矩阵。

同样，三态都保独立 sigma，故 $K_d=-I$。
由 (7) 的同一完整双深域，
$$
K_WK_U=K_BK_d=-K_B.
$$
原整个 $K_{72}^2=I$，遂得
$$
\boxed{K_U=-K_WK_B=-B_2.}
\tag{27}
$$
这保原 $W,Q,\mathbf R$，不是从 $W$ 边际倒推 $U$ 核。
三算子 $K_W,K_Q,K_U$ 在实际三态中彼此交换，
也与三个 $R$ 的共同核心 $\chi$ 交换。

这里每一条都是完整来源限制：
$$
\nu|_{Q\in p\mathbf Z_p}=\lambda(P_Q)_*\nu_{K_QF},\qquad
\nu|_{U\in p\mathbf Z_p}=\lambda(P_U)_*\nu_{K_UF}.
\tag{28}
$$
相应真实 $P_Q,P_U$ 在下一节明确给出。

## 6. 同一三个来源的完整标量基

取
$$
f_+=e_0+e_1,\qquad f_-=e_0+e_2,\qquad h=e_1+e_2.
\tag{29}
$$
换基行列式为 $-2$，故在当前处是整自同构。
三态的真实 normalized core 表为
$$
\begin{array}{c|ccccc}
 &K_W&K_B&K_Q&K_U&K_{R_1}K_{R_2}K_{R_3}\\ \hline
f_+&+1&-1&\chi&+1&\chi\\
f_-&-1&+1&-\chi&+1&\chi\\
h&-1&-1&\chi&-1&\chi .
\end{array}
\tag{30}
$$
最后一列只表示三个 $R$ 同时深的完整返回。
其外部标量是 $\lambda^3$，不写成一个单轴的 $\lambda$。

R488 的另一个改基是
$$
u=(f_++f_-)/2,\qquad v=(f_+-f_-)/2.
$$
因此更贴近原算术行的公式为
$$
\begin{array}{c|cccc}
 &K_W&K_B&K_Q&K_U\\ \hline
u&v&-v&\chi v&u\\
v&u&-u&\chi u&v .
\end{array}
\tag{31}
$$
原 $Y$ 新线和参考行在 $u$ 上为零，在 $v$ 上分别为
$S_{\rm new}\otimes\Lambda_{\rm old}$、
$H_{\rm ref}\otimes\Lambda_{\rm ref}$；$T$ 行在 $u,v$ 上相同。
完整未投影边际仍按 R488(41b)：
$Y_*u=(3-\delta)\nu_{S(2\cdot)}/4$，
$Y_*h=-(1+\delta)\nu_{S(2\cdot)}/2$；
$Y_*v$ 保 $\Xi$ 的全部正谱。
没有由 (30) 给这些外谱增加中央零。

## 7. 原 M 上任意独立三轴深度的完整公式

仍用 R465 的整坐标
$$
M(t_1,t_2,t_3,t_4,c,d_0)^t=(W,Q,U,R_1,R_2,R_3)^t,
$$
$$
\det M=3215520,\qquad
\operatorname{Gram}(M)=\operatorname{diag}(72,1624,252,60,2310,4466).
\tag{32}
$$
给任意非负整数 $n_W,n_Q,n_U,r$，定义真实矩形
$$
\mathcal D_{\mathbf n,r}
=\{W\in p^{n_W},\ Q\in p^{n_Q},\ U\in p^{n_U},\
       (R_1,R_2,R_3)\in p^r\mathbf Z_p^3\},
\tag{33}
$$
及完整物理变换
$$
\boxed{
P_{\mathbf n,r}
=M^{-1}\operatorname{diag}
(\kappa^{n_W},\kappa^{n_Q},\kappa^{n_U},
 \kappa^r,\kappa^r,\kappa^r)M.}
\tag{34}
$$
其像准确是 (33)，因为 $\kappa/p$ 是单位。
记
$$
N=n_W+n_Q+n_U+3r,\qquad
c_{\mathbf n,r}=\chi^{n_Q+r}\lambda^N.
$$
用 (30) 中彼此交换的实际核心，整个测度等式为
$$
\boxed{
\begin{aligned}
\nu_{f_+}|_{\mathcal D_{\mathbf n,r}}
 &=c_{\mathbf n,r}(P_{\mathbf n,r})_*\nu_{f_+},\\
\nu_{f_-}|_{\mathcal D_{\mathbf n,r}}
 &=(-1)^{n_W+n_Q}c_{\mathbf n,r}(P_{\mathbf n,r})_*\nu_{f_-},\\
\nu_h|_{\mathcal D_{\mathbf n,r}}
 &=(-1)^{n_W+n_U}c_{\mathbf n,r}(P_{\mathbf n,r})_*\nu_h.
\end{aligned}}
\tag{35}
$$
完整乘积标量包括原奇符号 $\chi$、每个轴的 $\lambda$，
及三个 $R$ 的 $3r$；没有只保符号矩阵而漏掉尺度。

等价地，在 $u,v$ 中，若 $n_W+n_Q$ 为偶，两态不换；
若为奇，两态交换，统一乘 $c_{\mathbf n,r}$ 并按 (34) 推前。
$h$ 仍按第三式。对一般三态列向量，也可写成
$$
\lambda^N(-1)^{n_Q+n_U}\chi^{n_Q+r}
(P_{\mathbf n,r})_*
K_W^{n_W+n_U}K_B^{n_Q+n_U}.
\tag{36}
$$

式 (35) 对任意原六输入连续测试、单位事件和进一步隐藏条件成立，
测试均按同一个 $P_{\mathbf n,r}$ 转置。
相应各轴环带或单位补域由这些完整等式作有限容斥得到。
不能因为 (35) 返回同一标量状态，就将一个未出现的混合 $Y$ 管
设为零。

准确的第一输出变化尤其简单：
$$
\boxed{
Y_s=\frac{37-3\delta}{72}W+
     \frac{1-3\delta}{56}Q+
     \frac{1-3\delta}{252}U.}
\tag{37}
$$
三个 $R$ 不出现。因此 (34) 将它变成
$$
\frac{37-3\delta}{72}\kappa^{n_W}W+
\frac{1-3\delta}{56}\kappa^{n_Q}Q+
\frac{1-3\delta}{252}\kappa^{n_U}U.
\tag{38}
$$
只有三深度相等时它才是 $\kappa^nY_s$。
一般完整中央测试中的单位指示和
$\log\langle Y_s\rangle$ 必须用 (38)，不能改成一个常数尺度 log。

对读者需要的原单轴物理式，设
$\mathcal D_0=\operatorname{diag}(3,12,7,7,1,1)$。
若 $q,u$ 是 $M$ 的第二、第三行，则
$$
P_Q=I+\frac{\kappa-1}{1624}\mathcal D_0\bar q^{\,t}q,\qquad
P_U=I+\frac{\kappa-1}{252}\mathcal D_0\bar u^{\,t}u.
\tag{39}
$$
各自逐个固定其他五个 $M$ 输出。具体加到 $Y_s$ 上的量分别为
$$
\frac{1-3\delta}{56}(\kappa-1)Q,\qquad
\frac{1-3\delta}{252}(\kappa-1)U.
\tag{40}
$$
这两条是真正混合第一输出的操作。

## 8. 一层 B 与 A²-W-A² 的两个不同像格

在原六输入中，定义
$$
b=(1,1,1,1,3\delta,0),\qquad
v_B=(3,12,7,7,-3\delta,0)^t,
$$
$$
\boxed{P_B=I+\frac{\kappa-1}{56}v_Bb.}
\tag{41}
$$
它逐个固定 $Q,d_0,\mathbf R$，把 $B$ 乘 $\kappa$。
真实限制是
$$
\boxed{\mu|_{B\in p\mathbf Z_p}=\lambda(P_B)_*K_B\mu.}
\tag{42}
$$
它将原两个目标输出变成
$$
Y_s\longmapsto Y_s+\frac{29-3\delta}{56}(\kappa-1)B,\qquad
W\longmapsto W+(\kappa-1)B.
\tag{43}
$$
其余原输入也由 (41) 全部确定。

令
$$
P_{\rm awa}=P_{A,2}P_WP_{A,2},\qquad
\mathcal D_{\rm awa}=P_{\rm awa}\mathbf Z_p^6,
$$
其中 $P_{A,2},P_W$ 是 R488 的原物理变换。
R488 的完整词域公式与 (23) 给
$$
\mu|_{\mathcal D_{\rm awa}}
=\lambda^5(P_{\rm awa})_*K_B\mu.
\tag{44}
$$
故归一后的两个完整限制准确比较为
$$
\boxed{
(P_B^{-1})_*\bigl(\mu|_{B\in p\mathbf Z_p}\bigr)
=\lambda^{-4}(P_{\rm awa}^{-1})_*
                    \bigl(\mu|_{\mathcal D_{\rm awa}}\bigr).}
\tag{45}
$$
所有逆推前都只施于所示像格上的受限测度，因而是整有界的；
没有将 $P_B^{-1}$ 当作全 $\mathbf Z_p^6$ 自同构。

这是真正不同的两个物理域。例如 R488 的
$D=4c+3\delta d_0$ 被 $P_{\rm awa}$ 固定，
而 (41) 给
$$
D\longmapsto D-\frac{3\delta}{14}(\kappa-1)B.
\tag{46}
$$
两者行列式分别是 $\kappa$ 与 $\kappa^5$。
所以来源等式 $K_B=R K_WR$ 绝不表示
$\mathcal D_{\rm awa}=\{B\in p\}$，也不许可删去两域的补集。
式 (45) 的任意测试必须分别经过两套实际转置。

## 9. 与后续原几何来源的接口

(35) 已把原 $M$ 的各深度矩形付在固定三个实际来源上，
无需另扩有限来源池。特别 $h$ 同时有
$W$ 核 $-\lambda$、$Q$ 核 $\chi\lambda$、
$U$ 核 $-\lambda$，以及三个 $R$ 共同核 $\chi\lambda^3$。
若使用一条已经证明的完整输入几何恒等式将 $h$ 拉回原
$\rho_0$，这些核心可连同它们的全部伴随和物理域一并拉回；
单独一个相同 $Y$ 边际不够完成此操作。

三条原 rank-two 中央同时失败所控制的行仍是 R483、R488 中的
完整算术行。这里提供 (38)、(40)、(43)、(45) 的真实混合管；
将已知非零参考差接入这些管的完整补域仍须继续证明。
没有把 $h$ 或 $u$ 的一个零中央扩成任意伴随条件下的零。

## 10. 精确证书

- [check-r494-original-b56-core-and-complete-m-rectangles.py](../scripts/check-r494-original-b56-core-and-complete-m-rectangles.py)
- [check-r494-original-b56-core-and-complete-m-rectangles.json](../scripts/check-r494-original-b56-core-and-complete-m-rectangles.json)

脚本在完整 $56$ 维 Schrödinger 基中验证两生成元的中心、
四挠求和和真实锚子空间；在原三态中验证全部核心表；
并精确验证 (3)、(7)、(32)、(37)、(39)–(43) 的物理坐标。
它不使用小素数采样。全来源归属、绝对 trace 比较及测度等式
已在正文证明。

直接依赖：

- [R488：共同 A odd29、真实四态及 D8](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)。
- [R465：原六 sigma、W 两态及完整坐标](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R416：原完整四挠中心](R416-original-four-torsion-core-and-exact-second-state-marginals.md)。
- [R426：degree18 绝对核心](R426-original-degree18-cm7-eigenlines-and-moving-inverse-fourth-branch.md)。
- [R483：三个原曲线的完整条件行](R483-original-six-sigma-cm-transfer-and-complete-three-curve-rows.md)。

