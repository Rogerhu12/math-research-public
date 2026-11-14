# R483 — 原六 sigma 的双 CM 转移与三曲线完整条件行

日期：2026-11-14。**状态：已证明。** 本篇在 R465 的同一个六输入
联合中，把原 $S$、$T$、$S_{\rm new}$ 的实际算术投影移到原伴随轴，
完整保留被观察轴的单位条件。关键是以 norm $13$ 代替与原坐标
行列式不互素的 norm $7$，并支付奇 sigma 的绝对相位。
同时，$E_{668168}$ 参考行留在这个原联合内；其真实环带差消去
未知参考导数后非零。还没有把混合两轴的管域当作独立伴随条件，
故主目标仍未完成。

## 1. 原两态、两套坐标和同一规范

沿用 R465 的原六个独立 sigma、共同 $b=17$ 及普通周期：
$$
\delta^2=-3,\quad \omega=(-1+\delta)/2,\quad
\gamma_7=(5+\delta)/2,\quad
\gamma_{13}=(7+\delta)/2,\quad \gamma_{19}=4+\delta,
$$
$$
N_a=\mathscr M_a/a,\qquad
\lambda=-\bar\pi_0^{-1},\quad \kappa=p/\bar\pi_0^2,\quad d=p-1.
\tag{1}
$$
R465 的原物理变量为 $(t_1,t_2,t_3,t_4,c,d_0)$，其中
$t_i=(\delta,2\delta,\gamma_7,\bar\gamma_7)_i\xi_i$，
$A=t_1+\cdots+t_4$。保
$$
Y_s=A+c+2d_0,\qquad W=A+3\delta c+4d_0.
\tag{2}
$$
$d_0$ 是物理输入，(1) 的 $d$ 是 Mellin 权指数。

第一套坐标及其全部 degree 为
$$
(W,\mathbf Q)=(W,Q,U,R_1,R_2,R_3),\qquad
(72,1624,252,60,2310,4466).
\tag{3}
$$
第二套为
$$
(Y,\mathbf Z)=(2Y_s,2Q_s,2U_s,R_1,R_2,R_3),\qquad
(136,3480,1020,60,2310,4466).
\tag{4}
$$
所有线性式、矩阵、Gaussian 交叉项和半特征已在 R465 完整给出。
记相应生成函数为 $\mathcal F_i^M$、$\mathcal F_i^L$，$i=0,1$。
两套坐标表示的是同一实际 $\rho_i$。原 $W$ 核在 (3) 中满足
$$
\mathcal F_1^M=K_{72,W}\mathcal F_0^M,\qquad
K_{72,W}\mathcal F_1^M=\mathcal F_0^M.
\tag{5}
$$
两条完整 $W$ 边际均为 $6\delta T$；两条完整 $Y$ 边际分别为
$S(2z)$ 和 R465 的 $\Xi(2z)$。

R465 两个物理矩阵的行列式是
$$
\det M=3215520,\qquad \det L=-13015200.
\tag{6}
$$
回到六个未缩放的原 sigma 变量时，两个行列式再乘
$$
\delta\cdot2\delta\cdot\gamma_7\bar\gamma_7=-42.
\tag{7}
$$
(6)、(7) 都与 $13\cdot19$ 互素。这一点是下面完整纤维转移的
输入，不能用“同一边际”来替代。

## 2. 原奇 sigma 的两个绝对小 norm 相位

原奇 theta 空间 $\mathcal S_1$ 只有 $\sigma$ 一条线，其半特征
是固定的奇半特征。奇 norm 的 CM 乘法在模二上可逆，保持该唯一
奇特征；R370 的 odd lift 与这里的 canonical division trace 相同。
准确有
$$
\boxed{N_{\gamma_{13}}\sigma=-\sigma,\qquad
       N_{\gamma_{19}}\sigma=\sigma.}
\tag{8}
$$
因此原六输入的同时特征都是 $+1$，不能把第一个单输入的负号省略。

给出 (8) 的特征零短证书。先取 $b=1$，定义
$$
q_a(x)=\frac{\sigma(az)}{a\sigma(z)^{Na}}.
$$
由原 $(\log\sigma)''=-x$、$x''=6x^2$ 及有限极点空间，完整多项式为
$$
q_{13}=x^6+(2+6\delta)x^3+\frac{40+24\delta}{13},
$$
$$
q_{19}=x^9+(-24+12\delta)x^6+(-24+24\delta)x^3
       -\frac{224+96\delta}{19}.
\tag{9}
$$
若 $q'=dq/dx$，则
$$
a^2x(az)q_a(x)^2
=Na\,xq_a^2-4(x^3+1)(q_a''q_a-(q_a')^2)-6x^2q_a'q_a.
\tag{10}
$$
令右边为 $n_a(x)$，在完整纤维
$f_a=n_a-a^2q_a^2=0$，即目标 $x(az)=1$，计算
$$
N_a\sigma/\sigma
=\frac1a\operatorname{Tr}_{K[x]/(f_a)}
 \left(\frac{\bar a}{a}\frac{\bar q_a}{q_a}\right).
\tag{11}
$$
脚本实际求出 $q_a$ 的逆并核其乘积为一，再取全 $13$ 或 $19$
个根的 Newton trace；结果依次为 $-1,+1$。
由于整个目标 $\mathcal S_1$ 只有一维，一个这样的完整精确纤维
已经确定全函数标量。这里没有用一个原像代替 trace，也没有只凭
projective Heisenberg 交织猜相位。一般 $b$ 的 (8) 由原齐次缩放
原样成立。

## 3. 原六轴同时 CM 与全部旧伴随的转移

对 $a=\gamma_{13},\gamma_{19}$ 及其共轭，(6)、(7) 保证两个
原输出变换在 $E[a]^6$ 上为双射。把 canonical trace 的六重和
按该双射重排，每一项原来源值准确相同。平移指数的交叉项由
R465 的完整 Gram 恒等式消掉，奇半特征的乘积也正是该篇已核的
标准输出特征；每边的总规范都是 $a^{-6}$。

所以 (8) 的六次方给两个坐标系的完整身份
$$
\boxed{
N_{a,Y}\prod_{\ell=1}^5N_{a,Z_\ell}\mathcal F_i^L
=\mathcal F_i^L,\qquad
N_{a,W}\prod_{\ell=1}^5N_{a,Q_\ell}\mathcal F_i^M
=\mathcal F_i^M.
}
\tag{12}
$$
先对原 $\rho_0$ 逐项得到 (12)。对 $\rho_1$，原 $K_{72,W}$
与同时 CM trace 交换：它们是在相同完整线丛上的 CM pull/trace
对应，$p$ 与 $13,19$ 互素，且原所有中心规范保留。
因而 (5) 把 (12) 传到第二态。这个证明没有把整个 degree72
的形式对应擅自延伸到一个丢失半特征的联合。

这里的交换绝对标量也可直接定标。完整 Heisenberg 的 CM ratio
可交换，故第一 $\mathcal S_{72}$ 上的交换子先是标量。
取同一个非零锚 $\Theta(6z)$：$\Theta$ 是
$\mathcal S_2$ 中唯一的 principal 线；$6$ 与 $13,19,p$ 互素，
完整 CM trace 与这个单位拉回相容，所以三个算子都在该锚上为
非零标量。交换子因而为一。这样没有留下 projective 的交换相位。

两态都是六个奇 sigma 的总角型零，故
$$
\mathcal F_i^L(\zeta Y,\zeta\mathbf Z)=\mathcal F_i^L(Y,\mathbf Z),
\qquad
\mathcal F_i^M(\zeta W,\zeta\mathbf Q)=\mathcal F_i^M(W,\mathbf Q).
\tag{13}
$$
因此第一轴 principal 平均等于其余五轴的同时 principal 平均。
记后者为 $\Pi_{\mathbf Z}$、$\Pi_{\mathbf Q}$。

### 3.1 支付逆 trace 的绝对标量

在整个 $\mathcal S_{136}$ 上，$N_aN_{\bar a}$ 实现恒等的完整
Heisenberg 自同构，故是标量。原非零、有理系数的 $S(2z)$ 给
$$
N_{13}S(2z)=-S(2z),\qquad N_{19}S(2z)=\omega S(2z).
$$
对 canonical trace 共轭，两个相反 CM 方向的特征分别为
$-1,\omega^2$，所以标量均为一。
在整个 $\mathcal S_{72}$ 上需要的 norm19 逆，以下第 4 节的
真实 $T$ 锚给 $N_{19}T=\omega T$，同样确定标量为一。
这里均只使用非零来源，不使用其中央导数。

定义真正的旧伴随算子
$$
B_{13}^{L}=\prod_{\ell=1}^5N_{\bar\gamma_{13},Z_\ell},
\qquad
B_{19}^{L}=\prod_{\ell=1}^5N_{\bar\gamma_{19},Z_\ell},
\qquad
B_{19}^{M}=\prod_{\ell=1}^5N_{\bar\gamma_{19},Q_\ell}.
\tag{14}
$$
对共轭 $a$ 用 (12)，再乘已定标的第一轴逆，便得
$$
\boxed{
N_{13,Y}^jN_{19,Y}^k\Pi_{0,Y}\mathcal F_i^L
=(B_{13}^{L})^j(B_{19}^{L})^k
 \Pi_{\mathbf Z}\mathcal F_i^L
}
\tag{15}
$$
及
$$
\boxed{
N_{19,W}^k\Pi_{0,W}\mathcal F_i^M
=(B_{19}^{M})^k\Pi_{\mathbf Q}\mathcal F_i^M.
}
\tag{16}
$$
这些是完整六变量来源身份。右边只动旧伴随，分别保 $Y$ 或 $W$。

第一 principal 空间上的 $N_{13}^{18}=N_{19}^{18}=I$，
以及 degree72 principal 的 $N_{19}^6=I$，使相应的有限周期
在两态实际伴随系数所张空间上成立。本篇不把这些周期强加到
整个巨大伴随 theta 空间。

## 4. 原 T72 的完整一维投影及两态平均

在整个 degree72 principal 格
$\sigma^{72}K[X]_{\le12}$ 中，R480 的完整 CM19 矩阵与原 CM7
矩阵给
$$
N_7^6=N_{19}^6=I,\qquad K_{72}=-N_7^9=-N_7^3.
\tag{17}
$$
准确的一维空间是
$$
\boxed{\ker(K_{72}-I)\cap\ker(N_{19}-\omega I)
       =\langle T\rangle.}
\tag{18}
$$
其唯一线的实际特征为 $N_7=-1,N_{19}=\omega$。
在 $N_{19}=\omega$ 空间中另外还有一条 $N_7=+1$ 的线，
其 $K_{72}=-1$；所以不能省掉 (18) 中的核心符号。

定义整个第一轴算术投影
$$
P_T=\left(\frac{I+K_{72}}2\right)
       \left(\frac16\sum_{k=0}^5\omega^{-k}N_{19}^k\right)\Pi_0.
\tag{19}
$$
完整十三列证书验证 $P_T^2=P_T$、$\operatorname{rank}P_T=1$，
以及 R398 的准确 $T$ 多项式确实固定于此投影。
由 (5) 和 $P_TK_{72}=P_T$，存在唯一完整五变量来源 $\Lambda_T$
使
$$
\boxed{
P_{T,W}\mathcal F_0^M=P_{T,W}\mathcal F_1^M
=T(W)\Lambda_T(\mathbf Q),\qquad \Lambda_T(0)=6\delta.
}
\tag{20}
$$
原 $T=z^6+\cdots$ 首项为单位，按 $T_W^6$ 的 Amice 系数提取
证明 $\nu_{\Lambda_T}$ 整有界；质量 $6\delta$ 也是单位。

令
$$
\mathcal F_+^M=(\mathcal F_0^M+\mathcal F_1^M)/2,\qquad
\mathcal D_T=\frac16\sum_{k=0}^5\omega^{-k}(B_{19}^{M})^k
 \Pi_{\mathbf Q}.
$$
(16)、(19) 准确给
$$
\boxed{\mathcal D_T\mathcal F_+^M=T\otimes\Lambda_T.}
\tag{21}
$$
这是保持原 $W$ 单位观察的旧伴随实现。
$\mathcal D_T\mathcal F_0^M$ 或 $\mathcal D_T\mathcal F_1^M$
单独还含 (18) 中的另一核心符号，不能把它们分别认成 (21)。

## 5. norm13 替换及同一原 Y 轴的三条真实算术行

R466 已在整个 $\mathcal S_{136}$ 定标
$N_{13}=R_{-1}N_7^{23}$。在 principal 空间上，准确为
$$
N_{13}=N_7^5,\qquad N_7=N_{13}^{11},
\tag{22}
$$
其中 $5\cdot11\equiv1\bmod18$。
这保留全十八项投影，避开了原坐标行列式中 norm7 的因子。

定义三个只作用于旧五伴随的整算子：
$$
\boxed{
\begin{aligned}
\mathcal C_S&=\frac1{18}\sum_{j=0}^{17}(-1)^j
                 (B_{13}^{L})^j\Pi_{\mathbf Z},\\
\mathcal C_{\rm new}&=\frac{I-\omega B_{19}^{L}}{36}
                 \sum_{j=0}^{17}\omega^{2j}(B_{13}^{L})^j
                 \Pi_{\mathbf Z},\\
\mathcal C_H&=\frac{I-\omega^2 B_{19}^{L}}{36}
                 \sum_{j=0}^{17}(B_{13}^{L})^j\Pi_{\mathbf Z}.
\end{aligned}}
\tag{23}
$$
(15) 将它们逐字对应到第一轴的实际投影。完整二十三列证书给
三个像分别恰为
$$
\langle S(2z)\rangle,\qquad
\langle S_{\rm new}\rangle,\qquad
\langle H_{\rm ref}\rangle.
\tag{24}
$$
这里 $H_{\rm ref}$ 是 R476 的质量一 $E_{668168}$ 来源，
不是 $E_{-136}$，也没有把它的导数预先赋零。

因此两态的完整条件行是
$$
\boxed{
\begin{array}{c|cc}
 &\mathcal F_0^L&\mathcal F_1^L\\ \hline
\mathcal C_S&S(2Y)\,A_0(\mathbf Z)&S(2Y)\,A_1(\mathbf Z)\\
\mathcal C_{\rm new}&0&S_{\rm new}(Y)\Lambda_{\rm old}(\mathbf Z)\\
\mathcal C_H&0&H_{\rm ref}(Y)\Lambda_{\rm ref}(\mathbf Z).
\end{array}}
\tag{25}
$$
$Y$ 在这里表示生成变量；其物理输出仍是 (4) 的 $2Y_s$。
$\Lambda_{\rm old}$ 是 R465 的完整五伴随，
$\Lambda_{\rm ref}$ 是 R476 八维分解的参考伴随。
准确质量为
$$
\boxed{
A_0(0)=1,\quad A_1(0)=-\frac{1+\delta}{4},\quad
\Lambda_{\rm old}(0)=\frac{52}{3},\quad
\Lambda_{\rm ref}(0)=-\frac{1+\delta}{2016b}.}
\tag{26}
$$
后面三项来自 R465、R476 的完整二十三坐标身份。
两个零来自第一态的整个 $N_7^9=-1$ 块，与新线和参考线的
$N_7^9=+1$ 块互斥，不是由某个零质量推出来的。

(23) 全部只用 prime-to-$p$ canonical trace、角平均及单位分母，
故保持原整张量格。$S(2z)$、$S_{\rm new}$ 的首 $z^6$ 系数分别为
$64,1$，$H_{\rm ref}(0)=1$，逐条提取原 Amice 系数便支付
$$
\nu_{A_0},\nu_{A_1},\nu_{\Lambda_{\rm old}},
\nu_{\Lambda_{\rm ref}}\in\mathcal O[[\mathbf Z_p^5]].
\tag{27}
$$
(26) 的四个质量都在当前射线上为单位，故它们均为完整整卷积单位。
本篇不在混合 $Y,W$ 管里免费使用这些逆；相加测试仍须转置。

## 6. 三个原中央零实际给的所有完整条件零

对单轴来源 $G$ 记
$$
J_G(u)=\int_{\mathbf Z_p^\times}\langle x\rangle^{du}\,d\nu_G(x).
\tag{28}
$$
(20)、(21)、(25) 均给整个 $u$ 的函数身份，而不仅给某个导数。
例如
$$
\int_{W\ {\rm unit}}\langle W\rangle^{du}h(\mathbf Q)\,
 d\nu_{\mathcal D_T\mathcal F_+^M}
=J_T(u)\nu_{\Lambda_T}(h),
\tag{29}
$$
$$
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}h(\mathbf Z)\,
 d\nu_{\mathcal C_{\rm new}\mathcal F_1^L}
=J_{\rm new}(u)\nu_{\Lambda_{\rm old}}(h).
\tag{30}
$$
原 $S$ 行中的第一函数是
$$
J_{S(2\cdot)}(u)=\langle2\rangle^{du}J_S(u).
\tag{31}
$$
由于 $J_S(0)=0$，它的中央导数准确为 $J'_S(0)$；
没有遗留未知质量乘 $\log\langle2\rangle$。

故若固定三条秩二曲线的反证输入为
$$
J'_S(0)=J'_T(0)=J'_{\rm new}(0)=0,
\tag{32}
$$
则 (29)、(30) 以及 (25) 的两条 $S$ 行，对于**任意完整连续旧
伴随测试**都给中央导数零。允许实际紧开伴随条件乘连续测试。
这个范围来自已识别的实际曲线与完整张量分离，绝非从核心符号
或质量零擅自赋给一个辅助来源。

### 6.1 保所有第一环带与全部伴随共同深度

原六 sigma 同时深的完整标量是 $(-\lambda)^6=\lambda^6$；
(3)、(4) 在当前 $p$ 都是整自同构，故等价于六个输出同时深。
这条身份经 (5)、(15)、(23) 保留。与各实际第一来源的 scalar
core 比较，在整 Amice 环中约消非零第一因子，得到准确的
五伴随共同深度核心：
$$
\begin{array}{c|c}
\text{伴随}&\nu_\Lambda|_{(p\mathbf Z_p)^5}\\ \hline
A_0,A_1,\Lambda_T&
 \lambda^5[\kappa,\ldots,\kappa]_*\nu_\Lambda\\
\Lambda_{\rm old},\Lambda_{\rm ref}&
 -\lambda^5[\kappa,\ldots,\kappa]_*\nu_\Lambda .
\end{array}
\tag{33}
$$
不要求单独一个伴随具有该 scalar core。

第一来源 $G=S(2\cdot),T$ 的 scalar 为 $c_G=\lambda$；
$G=S_{\rm new},H_{\rm ref}$ 的 scalar 为 $c_G=-\lambda$。
于是对任意 $n\ge0$，
$$
\boxed{
\int_{x\in p^n\mathbf Z_p^\times}
 \langle x/p^n\rangle^{du}\,d\nu_G(x)
=c_G^n\langle\kappa/p\rangle^{ndu}J_G(u).
}
\tag{34}
$$
这里 $\kappa/p=\lambda^2$。给 (34) 另附任意完整伴随测试，
或按 (33) 另限全部伴随共同深度，都仍是完整测度身份。
因此 (32) 也消掉三条原秩二来源的所有这些第一环带中央行。
第一轴按 $p^n$ 归一时的尺度项已在 (34) 保留。

## 7. 同一原联合内的参考行：未知导数与已知非零差

(25) 的参考行准确为
$$
\int_{Y\ {\rm unit}}\langle Y\rangle^{du}h_u(\mathbf Z)\,
 d\nu_{\mathcal C_H\mathcal F_1^L}
=J_H(u)\nu_{\Lambda_{\rm ref}}(h_u).
\tag{35}
$$
由于 $H_{\rm ref}(0)=1$、其真实 core 为 $-\lambda$，
$$
J_H(0)=1+\lambda,
$$
所以完整导数为
$$
\boxed{
J'_H(0)\nu_{\Lambda_{\rm ref}}(h_0)
+(1+\lambda)\nu_{\Lambda_{\rm ref}}
 \left(\left.\partial_uh_u\right|_{u=0}\right).
}
\tag{36}
$$
不能因为测试在一个边际上质量零而丢掉第二项。

更具体地，令 $\mathcal L_{H,n}$ 是 (35) 改限
$Y\in p^n\mathbf Z_p^\times$、第一权取
$\langle Y/p^n\rangle^{du}$、伴随测试为一后在 $u=0$ 的导数。
由 (26)、(34)，完全消去未知 $J'_H(0)$ 得
$$
\boxed{
(-\lambda)^{-n}\mathcal L_{H,n}-\mathcal L_{H,0}
=-\frac{1+\delta}{2016b}\,
 n\,d\,\log\langle\lambda^2\rangle(1+\lambda).
}
\tag{37}
$$
对每个正 $n$，右边非零。原固定因子及 $1+\lambda$ 都是单位。
而 $\log\langle\lambda^2\rangle\ne0$：若它为零，普通嵌入中
$\lambda^2$ 是根单位，作为同一个代数数也必须是根单位；
但它的全局 norm 为 $p^{-2}$，矛盾。

(37) 是同一原六 sigma 第二态经过 (23) 的**旧伴随**算子后，
两个完整第一环带的实际非齐次差。它不是某个新辅助来源的
无来源数值，也不宣称其中任一未知导数已为零。
要与 (32) 矛盾，还须把同一个真实混管关系送入这些已付行；
本篇没有省掉这一步。

## 8. 完整分支测试与原 W 管的准确形状

(14)、(23) 的每项都可完全展开为真实伴随 CM 纤维。
例如 $\alpha=\gamma_{13}^j\gamma_{19}^k$，对五个旧伴随作
$N_{\bar\alpha}$，完整测度形式为
$$
\nu_{(B_{13}^{L})^j(B_{19}^{L})^kG}
=\bar\alpha^{-5}
 [I_Y,\bar\alpha^{-1}I_5]_*
 \sum_{\mathbf t\in E[\bar\alpha]^5}\nu_{G_{\alpha,\mathbf t}},
\tag{38}
$$
其中每个 $G_{\alpha,\mathbf t}$ 保相应
$\mathsf T_{\alpha t_\ell}^{(N_\ell)}$ 的完整中心以及生成变量
$\mathbf z\mapsto\alpha\mathbf z$。也可逐次展开 $13,19$ 的
小 norm trace 得到同一式；没有删支。
附角分支 $\zeta$ 时，真实测试为
$$
h(Y,\mathbf Z)\longmapsto
h(Y,\zeta\mathbf Z/\bar\alpha).
\tag{39}
$$
第一输出和其单位条件原样不动，所以没有第一轴 CM 尺度
$\langle\alpha\rangle^{-du}$；若 $h$ 自身依赖 $u$，它的实际
导数仍须保留。

旧 $T$ 输出在 (4) 中为
$$
W=cY+r(\mathbf Z),\qquad
c=\frac{37+3\delta}{68},\qquad
r=\frac{1-3\delta}{60}Z_1+
  \frac{-31+3\delta}{510}Z_2.
\tag{40}
$$
因而每条实际伴随分支的旧 $W$ 深条件必须读作
$$
\boxed{cY+\frac{\zeta}{\bar\alpha}r(\mathbf Z)
              \in p^n\mathbf Z_p.}
\tag{41}
$$
它不同于 R465 直接在第一轴展开时的
$c(\zeta/\alpha)Y+r(\mathbf Z)$。
两个表达若要在同一原域比较，仍须用 (12) 的完整联合纤维重排，
保角相位、全部来源和测试；只比较斜率不够。

原 $W$ core 在 (4) 的精确物理矩阵也可直接写为
$$
\boxed{
C_W=I+\frac{\kappa-1}{72}\,u\,w,\qquad
u=(74-6\delta,58+174\delta,-62-6\delta,0,0,0)^t,
}
$$
$$
w=\left(\frac{37+3\delta}{68},
         \frac{1-3\delta}{60},
         \frac{-31+3\delta}{510},0,0,0\right),\qquad wu=72.
\tag{42}
$$
它确实改变 $Y$，并同时改变前两个旧伴随；后三个 $R_i$ 固定。
(38) 的伴随缩放与 (42) 不自动交换。
即使当前 ray 在模 $13,19$ 上的 CM ratio 都为一，也不能据此
把所有高次 trace 的 torsion 支当成已与原核心交换。
因此本篇支付了原三曲线的完整旧伴随行、参考非零环带差及确切
移动管族，但没有把 (41) 免费塞进 (29)、(30) 的独立伴随测试中。

## 证书与依赖

- [本篇精确脚本](../scripts/check-r483-original-six-sigma-cm-transfer.py)；
  [完整矩阵、奇相位与投影数据](../scripts/check-r483-original-six-sigma-cm-transfer.json)。
- [R465：原共同六输入、两态和两套整坐标](R465-original-common-six-sigma-core-and-new-conditional-central-row.md)。
- [R466：完整 norm13 身份及固定曲线角色](R466-fixed-two-division-sources-and-new-rank-two-sextic-curve.md)。
- [R476：整个 Xi 桥、八维基与正确参考](R476-original-complete-xi-normtwo-bridge-and-integral-eight-source-basis.md)。
- [R480：实际 CM19 完整矩阵与两输入同时 trace](R480-original-simultaneous-cm-companion-transfer-and-two-arithmetic-rows.md)。
