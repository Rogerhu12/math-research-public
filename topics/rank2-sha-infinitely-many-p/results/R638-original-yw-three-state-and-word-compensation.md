# R638 — 原 Y/W 三态整核、真实词交域与同一首矩补偿

日期：2026-11-15。**状态：已证明。**

本篇继续 R634 的同一 $\mu_0$、同一 $q_{+,N_0}$。
完整 $Y$ 核在原三个真实来源中闭合；把真实 $Y$ 反射放进物理
归一后，两个源矩阵生成八元二面体群。三个来源的整个 $W$
边际都由原 $T$ 控制，因此每一个真实词域的正确归一 $W$ 行
都有原算术返回。这不要求给 $\Xi$ 的整个中央赋零。

随后把 $Y^n$ 与 $W^n$ 两个真实词在同一个共同深平面比较。
共同部分、两条外部部分、各自单位 cut 和全部 $\kappa$ 归一
逐项保留。其准确差商回到 R634 的 $M_1$，继而回到原负五矩及
三个完整补偿；未知外部部分没有被当成零。
这给实际同域的有限关系，不把有限源矩阵误认成有限物理域。

## 1. 原来源、规范与三个实际状态

沿用 R634 的全部规范、ray 和固定坏集：
$$
\lambda=-\bar\pi_0^{-1},\quad\beta=-\lambda,\quad
\kappa=p\lambda^2,\quad \epsilon_p^2=1,\quad d_p=p-1 .
\tag{1}
$$
仍用原未双倍的
$$
Y=A+c+2d,\quad W=A+3\delta c+4d,\quad
\mu_0=\mathcal P_{6,C}\rho_0,\qquad
\mu_W=K_W\mu_0=\mathcal P_{6,C}\rho_1 .
\tag{2}
$$
$C$ 是 R634 的纯伴随轴，$\rho_0,\rho_1$ 为 R465 同一完整六
sigma 的两个来源。记原规范二挠和为
$$
\mathsf H_{2,W}=\sum_{t\in E[2]}\mathsf T_{t,W}^{(72)},\qquad
\boxed{h=-\frac12\mathsf H_{2,W}\mu_0 .}
\tag{3}
$$
这里的 $h$ 专指 R465/R488/R493 的二挠来源经本篇的同一
$C$ 平均；它不是 R548 的另一个 $\eta+\rho_0/2$。

R634 已付整个第一 $\mathcal S_{72}$ 及其绝对核心。
在该空间的标准基中，
$$
K_{72}e_j=-(-1)^je_{19j+36},\qquad
\mathsf H_2e_j=
\begin{cases}2(e_j+e_{j+36}),&j\ {\rm even},\\0,&j\ {\rm odd}.
\end{cases}
$$
因 $19j-j=18j$，在偶数 $j$ 上只交换或固定两个显示项，
所以整个 $K_{72}\mathsf H_2=-\mathsf H_2$。于是
$$
\boxed{K_W\mu_0=\mu_W,\qquad K_W\mu_W=\mu_0,\qquad K_Wh=-h.}
\tag{4}
$$
全部半特征和其余五个输出都保留。

R493 的实际保 $Y$ 几何 $h_{\rm old}=\omega^2T_*\rho_0$，
以及 R465、R488 的完整边际，给
$$
\begin{array}{c|ccc}
 &\mu_0&\mu_W&h\\ \hline
Y_*&\nu_S&\nu_\Xi&\omega^2\nu_S\\
W_*&6\delta\nu_T&6\delta\nu_T&0.
\end{array}
\tag{5}
$$
因为 $C$ 平均逐点保持 $Y,W$，表 (5) 不变。
$\Xi$ 的参考谱和外谱全在，不赋 $J'_\Xi=0$。

## 2. 原完整 mixed lift 付清 Y 核

在 R465 的固定双覆盖 $\mathcal Y=2Y$ 中，三个来源的整个
第一轴都在 $\mathcal S_{136}$。令
$$
P_2=\frac14\sum_{t\in E[2]}\mathsf T_{t,\mathcal Y}^{(136)},
\qquad B_2=2P_2-I .
$$
R474(23)–(24) 已付整个含中心绝对式
$$
K_{136}=R_YB_2,\qquad
B_2e_j=(-1)^je_{69j+68}.
\tag{6}
$$
这里 $R_Y$ 是实际普通 $Y$ 反射，不先假定它固定任何本篇来源。

现在计算 (6) 在本篇三个整联合上的作用。对
$t=(s+r\omega)/2$，$\mathcal Y$ 平移在原六 sigma 中是
$Y_i(s+r\omega)$ 的整周期。恰四个 $Y_i$ 在模二非零，
原 odd 半特征的乘积为正，所以
$$
\mathsf T_{t,\mathcal Y}\mu_0=\mu_0 .
\tag{7}
$$
完整交叉为
$$
\langle2Y,W\rangle=4(17-3\omega).
\tag{8}
$$
若 $u=(j+k\omega)/4$，两平移的交换号准确为
$$
(-1)^{[\omega]\{(17-3\omega)(s+r\omega)
                        \overline{(j+k\omega)}\}} .
\tag{9}
$$
$[\omega]$ 表示原整数 $\omega$ 系数，式 (9) 包括中心。
在 $s,r\in\{0,1\}$ 上求和，结果是：$j,k$ 均偶时为 $4$，
否则为 $0$。这是非退化二元角色和，因为
$17-3\omega$ 模二为非零 CM 单位。证书逐项列出全部十六列。
原 $C$ 旋转与两轴均正交，所以 (7)–(9) 对全部 $C$ 平均支
及全部其余伴随成立。

原 $K_W$ 的四挠权在 $E[4]\setminus E[2]$ 上为 $1/4$，
在 $E[2]$ 上为 $-1/4$。故严格有
$$
\boxed{
P_2\mu_0=\mu_0,\qquad P_2h=h,\qquad P_2\mu_W=h/2 .}
\tag{10}
$$
没有由某个第一边际推断这些完整张量身份。结合 (6)：
$$
\boxed{
K_Y\mu_0=R_Y\mu_0,\quad
K_Yh=R_Yh,\quad
K_Y\mu_W=R_Y(h-\mu_W).}
\tag{11}
$$
原双倍尺度二在当前是单位，故 (11) 就是未双倍 $Y$ 的完整
归一核心；不新增周期或外部 $\lambda$。

## 3. 三态矩阵、完整伴随矩形和真实新线

用有序基 $(\mu_0,\mu_W,h)$，源算子按列作用：
$$
D=
\begin{pmatrix}1&0&0\\0&-1&0\\0&1&1\end{pmatrix},\qquad
K=
\begin{pmatrix}0&1&0\\1&0&0\\0&0&-1\end{pmatrix}.
\tag{12}
$$
于是 $K_Y=R_YD$，$K_W=K$。准确有
$$
D^2=K^2=I,\qquad(DK)^4=I,\qquad(DK)^2\ne I.
\tag{13}
$$
三个实际来源线性独立，而且原整格中饱和：R634 的完整新线投影先迫
$\mu_W$ 系数为零；$W$ 边际再迫 $\mu_0$ 系数为零；(5) 最后
迫 $h$ 系数为零。因此 (12) 的八元作用不是形式上多列出来的
冗余状态。
取新线第一 $z^6$、原 $W$ 第一 $z^6$ 和原 $Y$ 第一 $z^6$
三个整线性行，其三角主对角为 $52/3,6\delta,\omega^2$，
均为单位；$6!\Omega^6$ 在当前也是单位。
这给原整来源的左逆，不仅是特征零线性无关。

记 R628–R634 的
$$
E=E_Y=R-\frac{3+3\omega}{34}Y,\quad
E_W=R-\frac{19+3\omega}{72}W .
$$
原共同平面核心在这三个来源上全部是 $\epsilon_p I$。
对 $\mu_W$，这是共同平面核心与 $K_W$ 交换的结果。
对 $h$，可用 (11) 改写
$h=\mu_W+R_YK_Y\mu_W$；共同平面限制与 $R_Y,K_Y$ 都交换，
所以同一个特征 $\epsilon_p$ 严格传到 $h$。

由此得到四个完整物理身份：
$$
\boxed{
\begin{aligned}
\mu|_{Y\in p}&=\lambda(P_{Y,-\kappa})_*D\mu,\\
\mu|_{W\in p}&=\lambda(P_{W,\kappa})_*K\mu,\\
\mu|_{E\in p}&=\epsilon_p\lambda
                  (P_{E,\kappa}R_Y)_*D\mu,\\
\mu|_{E_W\in p}&=\epsilon_p\lambda(P_{E_W,\kappa})_*K\mu,
\end{aligned}
\qquad
\mu\in\operatorname{span}\{\mu_0,\mu_W,h\}.}
\tag{14}
$$
每条保原其余四个平面正交伙伴，及任何真实逆像测试。
例如全部 $Y/E$ 矩形准确为
$$
\boxed{
\mu|_{\{Y\in p^r,E\in p^s\}}
=\lambda^{r+s}\epsilon_p^s
 (P_{Y,(-1)^{r+s}\kappa^r}P_{E,\kappa^s})_*
 D^{r+s}\mu .}
\tag{15}
$$
$W/E_W$ 的完整矩形则把物理 $Y$ 反射去掉，并把 $D$ 换成 $K$。

R634 的完整第一新线投影仍满足
$$
\mathcal P_{\rm new}\mu_0=0,\quad
\mathcal P_{\rm new}h=0,\quad
\mathcal P_{\rm new}\mu_W
 =\nu_{S_{\rm new}}\otimes\nu_{\Lambda_B},\quad
\Lambda_B(1)=52/3.
\tag{16}
$$
第二个零也直接由 $B_2h=h$ 与 (6) 证明：在第一 principal
部分，$R_Y=1$，故该部分属于 $K_{136}=+1$ 的旧负谱，
而原新线属于 $K_{136}=-1$。

$E$ 是纯第一 $Y$ 伴随，故其完整核心与 (16) 的投影逐项交换。
由 (14) 的第三式，真正得到
$$
\boxed{
\nu_{\Lambda_B}|_{E\in p}
=-\epsilon_p\lambda(P_{E,\kappa})_*\nu_{\Lambda_B},\qquad
\nu_{\Lambda_B}(E\ {\rm unit})
=(1+\epsilon_p\lambda)\frac{52}{3}\in\mathcal O^\times .}
\tag{17}
$$
这是同一旧新曲线的实际五伴随标量，不识别一个新辅助曲线。
若对 $\Lambda_B$ 的 $E$ 单位部分作整卷积逆，全部五伴随测试
必须作实际平移转置；混合的 $W$ 单位 cut 也随之移动。

## 4. 同一 q 下所有真实词的原算术行

固定任意 $N_0\ge1$，仍用 R594 的同一个
$q=q_{+,N_0}$，包括其全部 $\lambda,\kappa$ 系数和
$D_{\rm carry}/\kappa^{N_0}$。原 $C,F,G$ 与 $Y/W$ 平面正交，
所以 (14) 的四个物理变换逐点保持 $q$。

R634 已付 $\mu_0,\mu_W$ 的完整 $\pi_4$ 中性。将 $\mu_W$
的该身份限制 $Y\in p$，使用 (11)，取消在其整像上单射的
$P_{Y,-\kappa}$ 推前，得到 $h-\mu_W$ 的相同身份。
因此三态都准确满足
$$
\boxed{(\pi_4)_*(q\mu)=\beta^{N_0}(\pi_4)_*\mu .}
\tag{18}
$$
$\pi_4$ 对这些物理变换闭合，故没有删掉非 $\pi_4$ 条件。

记
$$
A=P_{Y,-\kappa},\quad B=P_{W,\kappa},\quad
A^c=P_{E,\kappa}R_Y=\kappa A^{-1},\quad
B^c=P_{E_W,\kappa}=\kappa B^{-1}
\tag{19}
$$
为平面上的四个真实映射；在另外四轴均为恒等。
后两式中的 $\kappa$ 只乘此平面，不乘其余伙伴。
相应源矩阵为 $D,K,D,K$，外部系数为
$\lambda,\lambda,\epsilon_p\lambda,\epsilon_p\lambda$。

若物理词是 $P_{\mathbf w}=P_1\cdots P_r$，完整源矩阵按相反
次序为 $C_{\mathbf w}=C_r\cdots C_1$。反复使用真限制和真逆像，
$$
\boxed{
\mu|_{P_{\mathbf w}\mathcal L}
=c_{\mathbf w}(P_{\mathbf w})_*C_{\mathbf w}\mu,\qquad
c_{\mathbf w}=\lambda^r\epsilon_p^{\,\#\{A^c,B^c\}} .}
\tag{20}
$$
$\mathcal L$ 是同一整六变量格。由于所有 $W$ 边际在 (5) 中
已完整识别，令 $\mathbf r_T=(1,1,0)$，就有
$$
\boxed{
\int_{P_{\mathbf w}\mathcal L}
q\,\mathbf1_{W P_{\mathbf w}^{-1}\ {\rm unit}}\,
 \langle WP_{\mathbf w}^{-1}\rangle^{d_pu}\,d\mu
=6\delta\,c_{\mathbf w}\beta^{N_0}
  (\mathbf r_TC_{\mathbf w}\mathbf v_\mu)J_T(u).}
\tag{21}
$$
$P_{\mathbf w}^{-1}$ 只在其真实整像上使用。
八个矩阵给的 $\mathbf r_TC_{\mathbf w}$ 都为
$(\pm1,\pm1,0)$。因此 (21) 是原 $T$ 条件的真正词域传播，
不是新来源导数的假定。

同样，先在该真实逆像中施加 (16) 的完整第一 CM 投影，
再用第一 principal 中央和任意纯伴随测试，则所得来源是
$C_{\mathbf w}\mu$ 的 $\mu_W$ 系数乘
$S_{\rm new}\otimes\Lambda_B$。这给原第三中央的完整条件行。
若附加一个混合第一 $Y$ 的域，它仍须按 R465 的每个 CM 纤维、
单位尺度和实际词逆矩阵转置，不能免费穿过该投影。

## 5. 有限源关系不使物理词域相同

在坐标 $(Y,E)$ 中，置
$$
b_Y=(20+3\omega)/17,\quad t=349/612,\quad
u_0=(17-3\omega)/18,\quad v_0=263(20+3\omega)/20808 .
$$
则
$$
A=\begin{pmatrix}-\kappa&0\\0&1\end{pmatrix},\qquad
B=I+(\kappa-1)
 \begin{pmatrix}t&u_0\\v_0&1-t\end{pmatrix}.
\tag{22}
$$
显示的秩一矩阵是真正 Hermitian $W$ 投影，平方等于自身。
$$
\operatorname{tr}(AB)=\frac{349}{612}(1-\kappa^2),
\qquad\det(AB)=-\kappa^2 .
\tag{23}
$$
所以源关系 $(DK)^4=I$ 对应的物理 $(AB)^4$ 绝不是单位或
共同 $\kappa^4$ 缩放。

这里还可给准确的像格判别。四条轴 $Y,E,W,E_W$ 的两两行列式
均为当前单位；除 $2,3,17,263$ 外只出现 $349$，而
$349\not\equiv7\pmod{64}$。具体
$$
W=b_YY+2E,\qquad
E_W=-263Y/1224+(17-3\omega)E/36,\qquad
\det((W,E_W)/(Y,E))=1 .
\tag{24}
$$
四个矩阵 (19) 模 $p$ 各为 rank one，且相邻两个矩阵的乘积
模 $p$ 为零，当且仅当二者是 $A,A^c$ 或 $B,B^c$ 的逆配对。
证书逐一检查全部十六对；逆配对的完整乘积恰为平面 $\kappa I$。

因此任一没有相邻逆配对的长度 $r$ 词，完整矩阵模 $p$ 仍为
rank one，Smith 指数准确为 $(0,r)$。不同同长 reduced words
的像格不同：不同首字已有不同模 $p$ 像；首字相同时，取消
同一可逆线性映射，再归纳。源矩阵相等不改变这一事实。

若两个同长 reduced words 的首字不同，则它们的真实交域恰为
$$
P_{\mathbf w}\mathcal L\cap P_{\mathbf v}\mathcal L
=\{\text{原平面在 }p^r\text{，其余四伙伴任意}\}.
\tag{25}
$$
证明是两个 primitive、指数 $r$ 的 rank-one 像格分别用一条
原始线性同余描述；两条同余的模 $p$ 法向量独立，故交核就是
$p^r\mathcal O^2$。有共同首段时，先把该首段完整提到交域外。
这支付了真实重叠；没有据八元源群把各词改成同一个单位域。

## 6. 两个原词的共同部分与全部外部部分

现在取最直接的两个词 $A^n,B^n$，$n\ge1$。
它们的真实域和交域为
$$
\mathcal A_n=\{Y\in p^n\},\qquad
\mathcal B_n=\{W\in p^n\},\qquad
\mathcal P_n=\mathcal A_n\cap\mathcal B_n
=\{Y,E\in p^n\}.
\tag{26}
$$
原其余四轴及 $q$ 的全部条件都保留。

对 $\mu_0$，两个**各自正确归一**的完整 Mellin 行相同：
$$
\begin{aligned}
\mathcal F_{A,n}(u)
 &=\int_{\mathcal A_n}q\,\mathbf1_{WA^{-n}\ {\rm unit}}
                 \langle WA^{-n}\rangle^{d_pu}\,d\mu_0,\\
\mathcal F_{B,n}(u)
 &=\int_{\mathcal B_n}q\,\mathbf1_{WB^{-n}\ {\rm unit}}
                 \langle WB^{-n}\rangle^{d_pu}\,d\mu_0,\\
\mathcal F_{A,n}(u)&=\mathcal F_{B,n}(u)
 =6\delta\lambda^n\beta^{N_0}J_T(u).
\end{aligned}
\tag{27}
$$
第一式使用 $D^n\mu_0=\mu_0$，第二式使用 (12) 的两个 $T$ 边际。

把两行在共同部分 $\mathcal P_n$ 的积分分别记为
$\mathcal I_{A,n},\mathcal I_{B,n}$，其余完整积分记为
$\mathcal O_{A,n},\mathcal O_{B,n}$。
共同深返回后，两个真实观察准确为
$$
WA^{-n}P_{\rm pl,\kappa^n}
=(-1)^n b_YY+2\kappa^nE,\qquad
WB^{-n}P_{\rm pl,\kappa^n}=W .
\tag{28}
$$
第一个单位 cut 等价于 $Y$ 单位；第二个仍是 $W$ 单位。
它们不相同，尤其没有删除 $Y$、$W$ 各自的失败支。

定义同一原单位矩
$$
M_k(u)=\int_{Y\ {\rm unit}}(E/Y)^k
               \langle Y\rangle^{d_pu}\,d\mu_0,\qquad M_k=M_k(0).
$$
严格且一致收敛的完整共同部分是
$$
\boxed{
\begin{aligned}
\mathcal I_{A,n}(u)
={}&\epsilon_p^n\lambda^{2n}\beta^{N_0}
 \langle b_Y\rangle^{d_pu}
 \left[J_S(u)+\sum_{k\ge1}\binom{d_pu}{k}
      \left(\frac{2(-1)^n\kappa^n}{b_Y}\right)^kM_k(u)\right],\\
\mathcal I_{B,n}(u)
={}&6\delta\epsilon_p^n\lambda^{2n}\beta^{N_0}J_T(u).
\end{aligned}}
\tag{29}
$$
这包括所有质量和尺度。原 $J_S(0)=J_T(0)=0$ 使
$\mathcal I_{A,n}(0)=\mathcal I_{B,n}(0)=0$；
故 $\log\langle b_Y\rangle$ 的质量项准确消去，而非漏写。

令
$$
L_n=\sum_{k\ge1}\frac{(-1)^{k+1}}k
       \left(\frac{2(-1)^n\kappa^n}{b_Y}\right)^kM_k .
\tag{30}
$$
由 (27)–(29)，两个外部积分的完整中央为
$$
\boxed{
\begin{aligned}
\mathcal O'_{A,n}(0)
={}&6\delta\lambda^n\beta^{N_0}J'_T(0)
-\epsilon_p^n\lambda^{2n}\beta^{N_0}
 [J'_S(0)+d_pL_n],\\
\mathcal O'_{B,n}(0)
={}&6\delta\beta^{N_0}
  (\lambda^n-\epsilon_p^n\lambda^{2n})J'_T(0).
\end{aligned}}
\tag{31}
$$
$\mathcal O_{A,n}$ 的完整域是
$\mathcal A_n\setminus\mathcal B_n$，测试仍为
$WA^{-n}$；$\mathcal O_{B,n}$ 也使用自己的真实
$\mathcal B_n\setminus\mathcal A_n$ 和 $WB^{-n}$。
没有把这些域改成单独一个 native $W$ 单位支。
在原两中央都为零的反证条件下，
$$
\boxed{
\mathcal O'_{B,n}(0)=0,\qquad
\mathcal O'_{A,n}(0)
=-\epsilon_p^n\lambda^{2n}\beta^{N_0}d_pL_n .}
\tag{32}
$$
这正是目前真实的补偿关系；右侧不是被免费杀掉的量。

## 7. 真实差商与原负五矩的完整连接

$p\ge71$、$n\ge1$ 给
$$
L_n=\frac{2(-1)^n\kappa^n}{b_Y}M_1+p^{2n}\mathcal O.
$$
所以在原两中央都为零时，(32) 给准确赋值尺度
$$
\boxed{
\mathcal O'_{A,n}(0)
=-\frac{2d_p\beta^{N_0}
       (-\epsilon_p)^n\lambda^{2n}\kappa^n}{b_Y}M_1
+p^{2n}\mathcal O .}
\tag{33}
$$
等价地，保全部外部积分的真实差商收敛：
$$
\boxed{
\lim_{n\to\infty}
-\frac{b_Y\,\mathcal O'_{A,n}(0)}
 {2d_p\beta^{N_0}(-\epsilon_p)^n\lambda^{2n}\kappa^n}
=M_1 .}
\tag{34}
$$
误差属于 $p^n\mathcal O$。这里 $p$ 固定而 $n$ 变化，
$N_0$ 为原固定 carry 深度；没有将两个不同 $q$ 混在一起。
$\mathcal O_{A,n}(0)=0$ 也由 (27)、(29) 严格成立，
所以 (34) 未遗漏任何由归一改变产生的 log 质量。

R634 已把这一同一个 $M_1$ 接回原简单极点及全部三个补偿：
$$
\boxed{
\begin{aligned}
M_1={}&(-36b_K)\Omega^5 I_{f_1,-5}+\mathcal B_1
-a\int_{\{Y,V\ {\rm unit}\}}\frac{R^2}{YV}\,d\mu_0\\
&+\int_{\{Y\ {\rm unit},V\in p\}}\frac RY\,d\mu_0
-\int_{\{V\ {\rm unit},Y\in p\}}\frac RV\,d\mu_0 .
\end{aligned}}
\tag{35}
$$
其中原 $V$ 深项属于 $p^4\mathcal O$，原 $Y$ 深项有 R634(37)
的完整有理返回；共同单位项和 $\mathcal B_1$ 仍在。
(35) 的 $\mathcal B_1$ 是 R621 已付的未加权完整 $H/V$ 补偿，
整条平面行外面的 $\beta^{N_0}$ 不能分别当成三个隐藏
$q$ 加权子域的系数；后者仍必须使用 R626 的真正转置。

因此 (33)–(35) 将真实词交域、原中央条件、实际外部补偿和
原负五矩放在同一个等式中。若另能合法控制
$\mathcal O'_{A,n}$，才可从 (34) 读出新的首矩约束。
现有八元源群、相同完整 $T$ 行和共同深平面本身，不使
$\mathcal O'_{A,n}$ 为零，也不使 $M_1$ 或
$I_{f_1,-5}$ 非零。反射输出 $W\circ R_Y$ 的未知全算术身份
没有被偷偷补入。主目标尚未完成。

## 8. 与旧 A29 核的同一真实源矩阵

这里出现的 $D$ 还有一个已付的实际实现。
R488(34)–(45) 的原 $A$ 两层核心在同一三态上正是
$$
\boxed{\mu|_{A\in p^2}
=\lambda^2(P_{A,\kappa^2})_*D\mu .}
\tag{36}
$$
原纯 $C$ 与 $A$ 正交，因此 R634 的 $C$ 平均与该完整限制、
核心和物理缩放交换，(36) 在本篇三个来源上成立。
这与 (14) 的
$\mu|_{Y\in p}=\lambda(P_{Y,-\kappa})_*D\mu$
具有**同一个**源矩阵，外部 $\lambda$ 次数和物理像格不同。

所以原 $Y/W$ 和旧 $A/W$ 给出了同一三态的两套实际限制系统。
将来比较它们时，必须在真正
$\{Y\in p,\ A\in p^2\}$ 等交域上使用两种完整逆像；
不能直接取消两个不同支持上的 $D\mu$。
本篇 (31)–(35) 已给一组原 $Y/W$ 的实际补偿，(36) 保留了
可与之进一步比较的旧六 sigma 来源，没有新增辅助算术池。

## 精确文件与依赖

- [精确脚本](../scripts/check-r638-original-yw-three-state-and-word-compensation.js)
- [精确证书](../scripts/check-r638-original-yw-three-state-and-word-compensation.json)
- [R634：完整 S72 下降、原 T 每层返回和首矩三补偿](R634-original-whole-t-companion-and-reflected-unit-comparison.md)
- [R474：整个 K136 的完整中心与绝对符号](R474-original-six-sigma-two-output-core-and-exact-riemann-domains.md)
- [R465：原完整 W 两态及五伴随算术投影](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)
- [R488：原三态二挠规范和算术张量表](R488-original-shared-a-odd-core-and-actual-even-depth-dihedral-return.md)
- [R493：原二挠六 sigma 因式和真实保 Y 几何](R493-original-half-torsion-six-sigma-factor-and-y-preserving-transport.md)
- [R628：原完整伴随返回及两来源单位算子](R628-native-arithmetic-companions-and-complete-unit-operator.md)

证书使用 BigInt 的 $\mathbb Q(\omega)$ 算术，列出全部十六个
mixed quarter 角色和、完整二挠符号、八个源矩阵、四个物理
矩阵的符号 $\kappa$ 身份、四轴全部单位行列式及十六个相邻
词判别。所有限制域、共同部分和外部部分的积分由正文证明。
