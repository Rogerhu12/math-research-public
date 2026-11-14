# R119 续篇：开放径向网络的分数矩、同一公共参数及实际全部非零模逆

2026-11-14，visible-exact / tail_connector。

**状态：已证明（开放内部非零模压缩）。** 本篇接
[浅层五盒与全部频率](R119-supplement-shallow-five-cube-family-and-all-frequency-radial-selection.md)
的同一个真实参数族。它直接反演高外与 deep-low 已消去后的
开放内部径向矩阵，再用已付完整 mixed 差取得实际非零模逆。
没有把接入某个外反射后的酉矩阵冒认为开放压缩。

证明中引入一个复数 $z$，只用于对辅助外闭合做圆周积分；
它不是新物理参数，也不改变真实外边界。原独立 mean、外输入、
$\Gamma^*$ 两列及 ordinary/weak 源留在准确方程中。
本篇尚不把这个内部逆授予完整 source-to-label 或宣布
$\mathcal F=0$。

## 1. 同一 retained 空间与真实开放矩阵

写 $J=j+5$、$\delta_j=(2/25)2^{-j}$。仍用
$$
 A_j=2^{-40}\delta_j^{-1/8},\qquad
 T_j=2^{65664}J^2\delta_j^{-9},\qquad M_*=A_{8193}.
$$
对每个 $M\in4\mathbb N$，完整 retained 窗为
$$
 \mathcal I_M=
 \{i:129\le j(i)\le8192,\ M\le T_{j(i)}\}
 \cup
 \{i:j(i)\ge8193,\ A_{j(i)}\le M\le T_{j(i)}\}.
 \tag{B.1}
$$
未完整的外端分量仍是外端口。记 $n=|\mathcal I_M|$、$d=2n$。
这正是浅篇 (P.16)，每个 $M$ 非空且有限；所有非零实际频率
都包括在内，没有只从 $M\ge M_*$ 开始。

在径向背景上，高外是有限的左侧真实前片，deep-low 是右侧
真正无限允许线。分别由
[高外及外端口修订](R119-supplement-unitary-high-exterior-Poisson-and-buffered-angular-projections.md)
(H.15)--(H.23) 与
[完整 deep-low](R119-supplement-complete-deep-low-Green-Poisson-and-mixed-elimination.md)
(L.15)--(L.28) 准确消去。对固定 $M$，高方程的逆由原算术门
保证；低方程采用原无穷强解产生的允许线及 affine 位移。
它们与直接径向传递得到同一两端关系，因而与这些 Schur
的逐频矩阵相同，不是把一段有限截尾替代原无限尾。

设剩下的真实外输入为 $u$、外输出为 $y$。
在原 root-wave 单位可写成一个有限酉 colligation
$$
 \binom{x_{\rm out}}y
 =\mathscr U(\vartheta)\binom xu,\qquad
 \mathscr U(\vartheta)
 =P\begin{pmatrix}S(\vartheta)&0\\0&I_X\end{pmatrix},
 \quad S=\bigoplus_{i\in\mathcal I_M}S_i,
$$
$$
 P=\begin{pmatrix}P_{11}&P_{12}\\P_{21}&P_{22}\end{pmatrix},
 \quad
 \mathscr U=\begin{pmatrix}A&B\\C&D\end{pmatrix}
 =\begin{pmatrix}P_{11}S&P_{12}\\P_{21}S&P_{22}\end{pmatrix}.
 \tag{B.2}
$$
$A$ 正是外输入为零时的开放内部径向压缩。
$P$ 包括真实 positive cross、高前片、deep-low 的真实外线和
接线；沿本频率的五盒方向以及这些 retained 五坐标变化时固定。
整个外端口空间有限维，所有 fixed pieces 的传递保留；
普通、weak 和外 affine 项暂从齐次矩阵分开，见第10节。

(B.2) 可直接由原各 lossless 两端口串联得到。固定正片的
cross 和负片 transmission 非零，故逐段串联没有
$1-r_1r_2=0$ 的内部除法。右端真实允许线是单位 reflection。
这也证明其所有内部未知与原两态方程双向等价。
未覆盖外输入仍未施加任何物理反射。

## 2. 辅助闭合与圆盘内的真正可逆性

只在证明中令 $u=zy$，得到
$$
 U(z)=A+Bz(I-Dz)^{-1}C
     =P(z)S,\qquad
 P(z)=P_{11}+P_{12}z(I-P_{22}z)^{-1}P_{21}.
 \tag{B.3}
$$
因 $\|D\|\le1$，在 $|z|<1$，$I-Dz$ 真正可逆。
相应外状态唯一为 $y=(I-Dz)^{-1}Cx$，所以
$$
 \|U(z)x\|^2+(1-|z|^2)\|(I-Dz)^{-1}Cx\|^2=\|x\|^2.
 \tag{B.4}
$$
特别 $U(z)$ 解析、收缩，且 $U(0)=A$。

在单位圆上只排除有限集合 $\det(I-\zeta D)=0$。
其余每个 $\zeta$ 都使 $U(\zeta)$ 酉，并给唯一恢复外状态。
因此 $(I-w^{-1}U(\zeta))x=0$ 与同一个辅助闭合后的
完整两态问题双向等价，没有外状态独自构成的隐藏核。

若 $D$ 有单位模本征向量 $e$，酉性迫使
$P_{12}e=0$ 以及其相应外子空间与 $P_{21}$ 解耦。
该纯外酉部分可以准确剥离；它不改变 $A$、$P(z)$
或任一内部源。也可以保留它并继续排除上述有限圆点。
本篇从未要求在 $z=1$ 有可逆的外闭合；排除有限集合不改变
圆周积分。

再取一个独立的正数 $0\le q<1$，令
$$
 X_q(z)=D_M^{1/2}(I-qU(z))^{-1}D_M^{1/2},
 \quad D_M=\operatorname{diag}_i(D_{i,M}I_2).
 \tag{B.5}
$$
(B.4) 使这个逆在整个开圆盘真实存在，且
$\|X_q(z)\|\le\|D_M\|/(1-q)$。
不能在此步预先令 $q=1$，也不假定开放网络没有共振。

## 3. 每个辅助外闭合的同一个真实谱流门

$D_{i,M}$ 准确取浅篇 (P.15)：
$$
 D_{i,M}=
 \begin{cases}
 2^{-31400}J^{-160}\delta^{73/2}M^5,&\kappa_i\le1/4,\\
 2^{-861000}J^{-8300}\delta^{131/4},&1/4<\kappa_i<K_*,\\
 2^{-14800}J^{-64}\delta^{61/2}M^{-3},&\kappa_i\ge K_*.
 \end{cases}
 \tag{B.6}
$$
其中 $\kappa_i=M^2/B_i$、$K_*=2^{4000}J^{40}$。
全部真实 finite-$e$ 及浅层参数权限已经由浅篇逐项支付。
由 $\kappa_i\le1/4$ 时 $M^5\le(B_i/4)^{5/2}$ 以及
$B_i<2^7J\delta^{-3/2}$，三段均有
$0<D_{i,M}<1$。置 $a=\min_iD_{i,M}>0$。

对每个固定合法 $\zeta$，$P(\zeta)$ 沿五盒方向固定，
所以原同一个常方向 $v_M$ 给
$$
 -iU(\zeta)^*D_{v_M}U(\zeta)>D_M,\qquad
                                  \|v_M\|_1\le n.
 \tag{B.7}
$$
[五盒谱选择](R119-supplement-five-local-parameter-cube-and-complete-radial-network-selection.md)
(Q.10)--(Q.18) 的局部 Cayley 图也保持。外闭合现在换为
固定 $\zeta$，但它仍只是固定自伴关系；允许其 Cayley 极点，
不强行把该关系写成处处有限的矩阵。

具体而言，把每个受控短片以外的 fixed pieces 消去后，
对每个目标圆点 $w$ 仍有
$[P_E C(s)|_E-A_w]h=0$，其中 $A_w$ 自伴，
$C'(s)>0$，$\dim E\le d$。外状态的双向等价由第2节保证。
min--max 因而仍给
$$
 \#\{s:w\in\sigma(U(\zeta,s))\}
               \text{ 按核重数计 }\le d .
 \tag{B.8}
$$
无需 $\zeta=1$，无需 $d<M$，也无需一个局部对角传递估计
去替代完整正段 cross。

这个谱流论证在原固定 root-wave 单位进行。
径向共同共轭 $H_0$ 在每个窗口的两槽上为逐 Fourier 酉，
并与 $D_M$ 及以下层权交换。因此所得 resolvent norm
可逐点转到高外所用的表示，不要求求导 $H_0$ 后的
generator 仍等于未共轭 generator。

## 4. 带权 resolvent 的弱尾，而非先损失 a 的幂

条件固定其余所有参数，对真正均匀五盒
$[-1,1]^{5n}$ 积分。沿每条 $v_M$ 弦，连续展开的 eigenphase
满足几乎处处
$$
 \phi_k'\ge d_k:=\langle w_k,D_Mw_k\rangle\ge a.
 \tag{B.9}
$$
重根按其 eigenspace 上同一正 generator 分裂。
对任意 $T\ge1$，置 $\xi=a/T\le1$。
原小弧变量代换、(B.8) 和准确 cube 入流因子
$\|v_M\|_1/2\le n/2$ 给
$$
 \mathbb P\{\operatorname{dist}(1,\sigma U)<\xi\}
                         \le2nd/T.
 \tag{B.10}
$$
在其补集，令
$H=\sum_k d_k/|1-e^{i\phi_k}|$。同一完整弦积分给
$$
 \mathbb E[\,H\,\mathbf1_{\rm gap}\,]
                     \le2nd\,[1+\log(8T/a)].
 \tag{B.11}
$$
这里 $a$ 只进入 logarithm。

若 $q\ge1/2$，准确有
$|1-qe^{it}|^2=(1-q)^2+q|1-e^{it}|^2
\ge\frac12|1-e^{it}|^2$，故 $\|X_q(\zeta)\|\le2H$。
若 $q<1/2$，由 $\|D_M\|<1$ 直接有 $\|X_q(\zeta)\|<2$。
结合 (B.10)--(B.11) 和 Markov 不等式，对全部 $q<1$、
几乎每个 $\zeta$，统一得到
$$
 \mathbb P\{\|X_q(\zeta)\|>T\}
 \le \min\left\{1,\frac{8nd}{T}
                       [1+\log(8/a)+\log T]\right\},
 \qquad T\ge1 .
 \tag{B.12}
$$
没有把逐支积分错误估为
$a^{p-1}\int|1-e^{it}|^{-p}dt$；那会引入未支付的层幂。

取
$$
 p=\frac{255}{256},\qquad L_0=1+\log(8/a).
$$
对非负随机变量使用其完整尾积分，(B.12) 给
$$
 \begin{split}
 \mathbb E\|X_q(\zeta)\|^p
 &\le1+8pnd\left[
            \frac{L_0}{1-p}+\frac1{(1-p)^2}\right]\\
 &<2^{21}ndL_0 .
 \end{split}
 \tag{B.13}
$$
这是整个带权矩阵 norm 的分数矩，不是只估一个指定方向。

## 5. 从辅助圆周严格回到开放内部

对每个固定参数点和 $q<1$，(B.5) 是有限矩阵解析函数。
在 $z=0$ 取实现其 norm 的两个单位向量 $f,g$。
标量解析函数 $\langle g,X_q(z)f\rangle$ 的
$|\cdot|^p$ 次调和平均给
$$
 \|X_q(0)\|^p
 \le\frac1{2\pi}\int_0^{2\pi}
                         \|X_q(e^{it})\|^p\,dt .
 \tag{B.14}
$$
先在半径 $r<1$ 上应用该不等式，再令 $r\uparrow1$；
(B.5) 的统一界允许支配收敛，有限个外异常圆点没有贡献。
这一步的圆盘内可逆性已由 $q<1$ 付清。

Fubini 与 (B.13) 于是给
$$
 \mathbb E\|D_M^{1/2}(I-qA)^{-1}D_M^{1/2}\|^p
                                      <2^{21}ndL_0 .
 \tag{B.15}
$$
现在才令 $q\uparrow1$。若 $I-A$ 奇异，因为 $A$ 收缩，
存在 $Av=v$；正定 $D_M$ 使上述 norm 趋于无穷。
若不奇异则收敛到真实 inverse。Fatou 因而证明开放内部
逆几乎处处存在，并满足同一个分数矩上界。

定义
$$
 K_M=(2^{37}ndL_0)^{256/255}\,M^{16/15}.
 \tag{B.16}
$$
这里 $(17/16)(256/255)=16/15$。
Markov 不等式直接给
$$
 \mathbb P\left\{ I-A\text{ 奇异，或 }
       \|D_M^{1/2}(I-A)^{-1}D_M^{1/2}\|>K_M\right\}
                                  <2^{-16}M^{-17/16}.
 \tag{B.17}
$$
辅助 $z$ 已完全积分掉。此结论没有为每个频率选择一个新的
物理外反射，更没有要求真实外边界等于 $z=0$；
$z=0$ 仅准确表示该开放内部块。

## 6. 同一个无限参数点与每窗自己的新权

(B.17) 对其余全部坐标和原外参数 $t$ 一致成立。
可以同时对原 $Q=7$ 和 root-wave 两种开放网络施加该门。
再保留浅篇已有两种闭网络条件及原 good-$t$ 条件，
由 $\sum_{M\in4\mathbb N}M^{-17/16}<5$，公共好集测度仍严格大于
$$
                       1-\frac{96}{16384}>0 .
 \tag{B.18}
$$
两份新增开放坏集总量小于 $10/65536$；
旧坏集小于 $93/16384$，相加小于所示宽界。
各频率方向保持原来的常向量，不把它们相加成不存在的
全频共同单方向。

开放 inverse 门可等价写为有限矩阵
$D_M^{-1/2}(I-A)D_M^{-1/2}$ 的最小奇异值下界，
所以是闭条件。原真实无限允许线的产品连续性使上述好集
具有非空紧的闭条件子集；按原固定坐标次序选其中一点。
负频率由实共轭取得。原 profile、外 $t$、全部参数以后均固定，
不对这个选择函数作导数。

写 $x=\log_2M$。浅篇 (P.17),(P.21)--(P.22) 逐层给
$$
 n<2^{14}J,\quad d<2^{15}J,\quad L_0<2^{18}J,\qquad
 a^{-1}<2^{1500000}(1+x)^{8300}M^{460}.
 \tag{B.19}
$$
因此
$$
 K_M<2^{85}J^{256/85}M^{16/15}
                         <2^{85}J^4M^{16/15}.
$$
定义真实逐窗权
$$
 (\mathcal W_M^{\rm op})_i^2
             =2^{-96}J_i^{-4}M^{-16/15}D_{i,M}.
 \tag{B.20}
$$
同一个公共点上，对全部 $M\ge4$，
$$
 \boxed{\quad
 \|\mathcal W_M^{\rm op}(I-A_M)^{-1}
                          \mathcal W_M^{\rm op}\|\le1 .
 \quad}
 \tag{B.21}
$$
$\mathcal W^{\rm op}D_M^{-1/2}$ 每个对角元都不超过
$K_M^{-1/2}$，这证明了最后一步；未把不同窗口先取最坏值。

方便后续的统一较小权是
$$
 \nu_j=2^{-432064}J^{-4166}\delta_j^{671/20},\qquad
 (\mathcal W_M^{\rm op})_i^{-2}
                     <\nu_j^{-2}
                     =2^{864128}J^{8332}\delta_j^{-671/10}.
 \tag{B.22}
$$
逐项核算如下。高段由 $M\le T_j$ 收
$61/2+9(3+16/15)=671/10$，
bits 为 $14896+65664(61/15)<282000$，
$J$ 幂 $68+122/15<77$。
紧段用 $M<2^{2004}J^{41/2}\delta^{-3/4}$，
bits 小于863234，$J$ 幂为 $8304+328/15<8326$，
$\delta$ 幂为 $131/4+4/5=671/20$。
低段 $M^{16/15-5}\le1$，其余幂更有利。
全部严格进入 (B.22)。

相对于浅篇已付 $\underline v$，新权准确为
$$
             \nu_j=2^{-48}J^{-1}\delta_j^{3/160}\underline v_j.
 \tag{B.23}
$$
没有悄悄重置成旧的较强层权。

## 7. 原角宽仍然成立

由 (B.19) 和 $J<2^{14}(1+x)$，
$$
 \|(I-A_M)^{-1}\|
 <2^{1500141}(1+x)^{8304}M^{460+16/15}
 <2^{1700000}M^{466}.
 \tag{B.24}
$$
第二步可用
$(1+x)^{8304}\le8304!e^{1+x}<2^{116258}M^2$，
其中 $8304<2^{14}$、$e<4$、$\log2>1/2$。

原角权
$W_{i,M}=\exp(2^{-800}Mh_i)$、$h_j=8\delta_j^{1/256}$
保持不变。深层 retained 窗仍有 $M\ge A_j$；
原 $2^{-800}Mh_j>2^{25}J$ 的门超过 (B.19)--(B.22)
所有 logarithm 费用。对于浅窗及 $M\ge M_*$，
$h_j\ge h_{8192}$ 和 $M_*>2^{984}$ 给
$2^{-800}Mh_j>2^{154}$，仍支付其全部有限费用。
其余 $M<M_*<2^{985}$ 用 (B.24)。因此
$$
 \|W_M^{-1}(I-A_M)^{-1}W_M^{-1}\|<2^{2200000}
 \tag{B.25}
$$
对全部非零四重模成立；$M\ge M_*$ 时可取右端1。
(B.25) 是径向开放逆的原角宽门，不能在尚未支付 mixed
解析卷积时直接授予实际非径向全部标签空间。

## 8. 以新权重新支付高外和 deep-low 的完整差

把 $\nu$ 定义在全部已覆盖内部层，不只在 retained 上。
其一步比
$2^{671/20}(1+1/J)^{4166}<2^{80}$；
对
$$
 F_j=2^{4096}J^4\delta_j^{-5}
$$
以及 $w=1,\nu,\nu^{-1}$，$wF^{\pm1},wF^{\pm2}$
的一步比小于 $2^{92}$，真实邻接距离至多2的比小于
$2^{184}<2^{256}$。故高外 (H.12)--(H.25) 的完整长程
Poisson 门和 deep-low 的 (L.2)--(L.3) 逐项仍成立。
不是把高消元后的差误称为有限邻接。

直接 high-Schur 差按原 (V.19)--(V.22) 重新合账，
最大实际层幂变为
$$
                    47+9+671/10=1231/10 .
 \tag{B.26}
$$
原 $2^{1000000}J^{8400}$ 仍包含新128 bits及新增两个
$J$ 次方：原未粗化的各项总 bits 小于1000000，
$40+2+8332<8400$。
深端首块、两个真实浅规范段的二进制上界分别小于
$$
 1000000+126000+(1231/10)8197-20010-8388608<-6273000,
$$
$$
 1000000+126000+400+220+
                  (1231/10-7/4)4100-8388608<-6273000,
$$
$$
 1000000+126000+400+185+6150+
               (1231/10-827/256)8197-8388608<-6273000.
$$
深端余幂为 $1767/1280>1$；在 $j\ge16384$，
$(1+1/J)^{8400}<2$，故完整无穷和仍小于 $2^{-6200000}$。

含 deep-low 两侧 Poisson 的三项必须重付原低端一次角导
$A_j$ 和最多两份 $F_j$。准确最大幂为
$$
 47+\frac18+10+\frac{671}{10}
       =\frac{4969}{40},\qquad
 \frac{31867}{256}-\frac{4969}{40}
       =\frac{327}{1280}>0 .
 \tag{B.27}
$$
原固定因素的总 bits 仍小于1200000，
$40+8+8332<8400$。因此各层可收
$2^{1200000}J^{8400}\delta_j^{-4969/40}\mathcal N_j\mathcal X$。
在 $8193\le j\le65536$ 用 $J<2^{17}$，
首端指数严格小于
$$
 1200000+8400\cdot17+\frac{4969\cdot8197}{40}
                          -20010-8388608<-6047000.
$$
保留 $\delta^{-4969/40}\mathcal N$ 的真实下降，
有限层数费用小于16 bits。
在 $j\ge65536$，多项式比小于 $2^{1/4}$，
净比至多 $2^{-7/1280}$，几何和小于 $2^9$。
8192实际邻胞继续用原 $K=64$ 和第二段规范，
不得用深层规范外推；同一个宽账仍有四万 bits 以上余量。

综合直接项和三份 low-Poisson 项，在同一真实全参数对象上，
$$
 \boxed{\quad
 \|\nu^{-1}(S_{\rm rem,a}-S_{\rm rem,0})\nu^{-1}\|
                       <\eta:=2^{-6000000}.
 \quad}
 \tag{B.28}
$$
这里 $\mathcal X\le2^{-8388608}$ 是浅篇第3节已重新取得的
真实 incoming 范围；$\mathcal N$ 仍包含 current joint、
两 $\Gamma^*$ 及真实邻片作用。
(B.28) 继续只对已覆盖内部未知的压缩收费，外源列不在该
$L^2$ 小量断言之内。

## 9. 当前 actual 的全部非零内部频率真正可逆

设 $P_N$ 为 remaining 中所有非零 canonical Fourier 槽，
$P_Z$ 为 remaining 的 canonical mean 槽。
在径向时
$$
 A_0=P_NS_{\rm rem,0}P_N=\bigoplus_{M\in4\mathbb Z\setminus0}A_M .
$$
其逐频矩阵与第1节的真正开放矩阵准确相同。
径向 $H_0$ 与 $\nu$ 交换，(B.21)--(B.22) 因而给
$\|\nu(I-A_0)^{-1}\nu\|\le1$。
对真实非径向块 $A_a=P_NS_{\rm rem,a}P_N$，
(B.28) 和真正 Neumann 级数于是给
$$
 \boxed{\quad
 R_{N,a}=(I-A_a)^{-1},\qquad
          \|\nu R_{N,a}\nu\|<(1-\eta)^{-1}<2 .
 \quad}
 \tag{B.29}
$$
其确切源/状态空间是
$\|\nu^{-1}g_N\|_{\ell^2L^2}<\infty$、
$\|\nu x_N\|_{\ell^2L^2}<\infty$。
不是声称对任意裸 $L^2$ 源有同阶有界逆。
先对有限支持源逐模用径向真实逆，再在这两个空间中取极限。

齐次唯一性也不漏另一个裸 $L^2$ 内部解：
裸 $L^2$ 包含在 $\|\nu x_N\|<\infty$ 的状态域。
对该解的每个径向频率，$I-A_{0,M}$ 是真正可逆有限矩阵，
所以按分布方程可先逐频应用；(B.28) 使右端位于上述源域，
再用收缩得到零。不假定一个任意状态已经有较强的
$\nu^{-1}$ 权。

径向 $P_NS_{\rm rem,0}P_Z=P_ZS_{\rm rem,0}P_N=0$。
因此两个 actual mean-cross 在双 $\nu^{-1}$ 权中均小于
$\eta$。令它们为 $A_{NZ},A_{ZN}$；消去非零块后的
准确 canonical-mean 算子为
$$
 S_Z^{\rm eff}
   =P_ZS_{\rm rem,a}P_Z+A_{ZN}R_{N,a}A_{NZ},
$$
$$
 \|\nu^{-1}(S_Z^{\rm eff}-P_ZS_{\rm rem,0}P_Z)\nu^{-1}\|
                                      <\eta+2\eta^2<2\eta.
 \tag{B.30}
$$
没有把 mean-cross 扔掉。下一步仍须把这个真实 mean 系统
与物理平均高度、总通量及实际外条件准确识别并解出。

## 10. 全部源、真实外口和尚未消去的物理 mean

为说明 (B.29) 如何接原源，令 $x_X$ 是真实未覆盖外输入。
高外准确源为
$$
 \widetilde g_H=g_H+C_Xx_X,\qquad
 k_L=g_L+A_{LX}x_X+F_H\widetilde g_H .
$$
按 $L=R\oplus D$ 分解 $k_L=(k_R,k_D)$，其中
$R=N\oplus Z$。真正的解公式是
$$
 \begin{split}
 x_N&=R_{N,a}\{P_N(k_R+F_Dk_D)+A_{NZ}x_Z\},\\
 x_D&=E_D(x_N+x_Z)+R_Dk_D,\\
 x_H&=E_H(x_N+x_Z+x_D)+R_H\widetilde g_H .
 \end{split}
 \tag{B.31}
$$
外输出由原完整 colligation 的最后一行读取；绝不把它另设为零。
高源 $\widetilde g_H$ 仍须满足原 $H^1$ 源门，
低源仍须提供 $\|\nu F k_D\|$，
第一行须提供其完整 $\nu^{-1}$ 加权 norm。
这些条件不能因辅助闭合平均而免费取消。

canonical mean 的最后方程为
$$
 (I-S_Z^{\rm eff})x_Z
   =P_Z(k_R+F_Dk_D)
      +A_{ZN}R_{N,a}P_N(k_R+F_Dk_D).
 \tag{B.32}
$$
它保所有当前 mean-cross 和外 affine 列。
canonical 零模不自动等于物理 mean；
原 curved-root trace、total conormal、signed density 及
端角变换产生的非零分量仍按原 (J.39)--(J.40) 保留。

在原固定物理角下，真正 mean 仍满足
$$
 \partial_t\langle\pi\rangle=\langle g\rangle,\qquad
 \partial_t\langle h\rangle
 =\langle d h_\theta+\mu^{-1}\pi-\mu^{-1}F^t\rangle .
 \tag{B.33}
$$
这里 $\pi$ 是 total flux；唯一整体高度积分常数与真实外线
须由实际边界问题决定，不能每胞另指定一个高度或把两个乘积
平均删掉。将 (B.32) 与 (B.33) 做同一物理商是下一完整门。

普通源仍含 $\mu p_*^2$，weak 源保 $F^t,F^\theta$ 和全部真实
端点 charge；没有径向求导 $F^t$。负窗 particular、正片完整
total-DN affine、所有真实 jump、根与 graph 源均按原有序
Piola/两行变换进入 $g$。当前参数导数时，两列 $D\Gamma^*$、
metric-source、端角导数以及 $\dot H^*g$ 仍分别进入同一式子。
本固定背景 inverse 不令这些列为零，也没有替它们完成最后的
联立范数收费。

本篇完成的是同一原参数族上全部非零实际频率的开放内部逆、
真实 mixed 比较、完整外输入公式和剩余 mean Schur。
证明所有原量词与新权都已显示；物理 mean 商、实际外边界闭合、
原标签空间的最终源映射及 $\mathcal F=0$ 继续作为实质工作，
不由本篇提前宣告。全篇为解析推导，没有新的本地数值实验。
