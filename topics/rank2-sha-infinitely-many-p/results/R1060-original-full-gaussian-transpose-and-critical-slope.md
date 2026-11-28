# R1060 — 原 p² 全来源的双 Gaussian 有限转置与完整临界斜率

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

本稿把 R1056§6.1 的实际有限 Newton 读者，逐 CM/level word
转置到 R1054 的整个双 Gaussian 来源。先保原 source 的
$U(1)$ 积分、全部 $p^2$ 有限字及实际微分，再取有限系数。
全篇不使用已撤回的 usual/flat 正权 cross，不对两个 rank-one
因子分别假设有界 Amice 测度。

## 1. 固定同一个实际来源和两侧外权

记原完整 CM、level、tame/Artin/Cor 字为 $i$。
每个字使用 R1059 的实际裸 bounded $Q_2$ 来源 $A_i$，
其 Amice 测度为 $\mu_i$，系数界记为 $m_i$。
完整 Maass 参数记为 $C_i$；本题原最大阶坏基及其单位标记满足
$v_p(C_i)=2$。其未剔除的普通矩及原 unflat 值分别为
$$
 m_{i,n}=\int_{\mathbf Z_p}x^n\,d\mu_i(x),\qquad
 R_{i,n}=\sum_{r=0}^n c_r(n)C_i^r m_{i,n-r},\qquad
 c_r(n)=\binom{n+2}{r}\binom nr\,r!.
 \tag{1}
$$
“裸”只是不将依赖权的 book tensor 外因子吞进测度；
原来源、全部有限算子及 $g_1/g_2$ 返回均在 $A_i$ 中。

令 $\kappa_i,\Omega_i,\omega_i$ 为 R1059(A0a)--(A0d)
的实际 Tate 配对、书版周期和好整微分。若
$f_i=-w_0+W_p=-f^{[p]}$ 连同第 $i$ 个原 tame word，
则逐个非负整数 $n$ 有
$$
 R_{i,n}
  =p^{2n}\kappa_i^n\Omega_i^{3+2n}
           (\mathcal D_3^nf_i)(E_i,\omega_i).
 \tag{2}
$$
这是原源的算子恒等式，不含任何未经支付的
$q_{p,n}$ 或随权重新选择的 Gamma 因子。
单位标记 $yg_t$ 时，$\kappa_i=N(t)$、
$\Omega_i=\Omega_0/\bar t$；外部仍用原
$\Lambda_i(j)=\lambda_i(j)\mathfrak j_i(j)$，
$\mathfrak j_i(j)=N(t)^{-j}\bar t^{3+2j}$。

本稿研究的完整斜率是
$$
 \mathcal S=
 \sum_i\{\Lambda_i'(-2)\mathcal M_{A_i}(-2)
               +\Lambda_i(-2)\mathcal M_{A_i}'(-2)\}.
 \tag{3}
$$
先固定(3)的两个外权，再读各 $R_{i,n}$。
不能在这个有限读者中把它们改成 $\Lambda_i(n)$。
特别原 toric 权的 $N(\mathfrak a)^n$、avatar 和 period
不能因只看 $n\equiv4\bmod6$ 而漏掉。


## 2. 全 coherent 核：保实际 arch 作用及 source 积分

仍用原全变极化的
$$
 a=17/2,\qquad G=6a\sqrt3,\qquad
 b=\frac{2(\omega-1)}{\sqrt G},\qquad
 c(y)=\frac1{4\pi ay}.
$$
原 source 字符、splitting、Haar、有限 Schwartz、
全局 $U(1)$ 变量 $h$ 和 theta 格点和均保持。
以下称 $\mathcal T_i$ 为这一个完整线性 theta 操作；
它包括原 $h$ 字符积分，而非只取一个局部 Gaussian。
其字符与逆向依原已经固定的 theta lift，绝不新选共轭。
输入固定为 $w_0=\theta(\psi_4^2)$ 的那个来源和
原 $f_i=-w_0+W_p$。

**先定义完整核，再在已付坐标中分解。**
$H_{{\rm an},i}(Z,W)$ 是实际 adelic word 作用后的完整
二维 normal-ordered theta kernel；原 $g_\infty$、CM
极化、所有 finite 操作及 $h$ 积分都在其定义中。
若使用该 word 的经典 $\tau_i$ 坐标，仍保这个未分离的核。
不能仅因 $\tau_i$ 是 CM 点就将两个 Gaussian 的交叉项设零。

在所选经典坐标完成该 word 的实际 graded arch 运输以后，
完整未分离核可明确写成
$$
 H_{{\rm an},i}(Z,W)=\mathcal T_i\!\left[
  e^{-c(\operatorname{Im}\tau)ZW}
  e^{Z\bar z+Wz}e^{2\pi i a|z|^2\tau}\right]_{\tau=\tau_i}.
 \tag{3a}
$$
这里 $\mathcal T_i$ 是同一固定 finite-Schwartz、格点及
$h$-角色操作；所有运输的系数、变量作用和权因子先按该
graded 运输保留，不把一个尚依赖 $\tau$ 的 arch 操作
当作可自由与导数交换的常数。
特别普通 $(0,2)$ 槽含 $z^2/2!$，故 $2!$ 倍该槽
正是原 $f_i^{\rm an}$，没有额外的真空归一。
第一 raised 槽给
$a z^2|z|^2-3ac(y)z^2
 =z^2(a|z|^2-3/(4\pi y))$，
也与同一 $\delta_{3,\rm cl}$ 的符号、常数逐项相符。


只有在原已经支付的 $\tau=\omega$ frame，连同完整
finite-word 运输，逐 Schwartz 的实极化恒等式才是
$$
 e^{-cZW}I(Z,W;r,s)
 =C_a e^{-\pi G(r^2+s^2)}
  \exp\!\left(\sqrt G\,r\,bZ-\frac{(bZ)^2}{8\pi}\right)
  \exp\!\left(\sqrt G\,s\,(-bW)-\frac{(-bW)^2}{8\pi}\right).
 \tag{4}
$$
$C_a$ 是同一 Gaussian 和 Haar 的固定常数，
不将它设为1，也不为各个系数重新校准。
原三处 similitude 的实际变量作用仍为
$Z\mapsto-iZ,\ W\mapsto iW$；在该字上两个 Hermite
参数因而同为 $-ib$。它保持 $ZW$，不能只搬其中一条。
其它 $\tau_i$ 必须先运输回这个实际 frame 才使用(4)，
否则一直保完整未分离核；下文有限对角转置两种写法都适用。

在 $p$ 处，第 $i$ 个基准字的整个 finite input 是
$$
 L_{AB}
 =p^{-2}\zeta_{p^2}^{(51/2)(A^2-4AB+B^2)}
        -{\bf1}_{p\mid A}{\bf1}_{p\mid B},
 \qquad A,B\in\mathbf Z/p^2\mathbf Z .
 \tag{5}
$$
这是 $A=-{\rm old}+{\rm new}$ 的号，与通常
$f^{[p]}={\rm old}-{\rm new}$ 相反。
$1/2$ 在 $\mathbf Z/p^2$ 中取逆。
各字函数仍为
$ {\bf1}_{A/p+p\mathbf Z_p}\otimes
 {\bf1}_{B/p+p\mathbf Z_p}$。
对一般 $i$、$h$，先作原实际 Weil/level 运输再使用(5)；
不把运输后的矩阵擅当为未运输的 $L$。

在已经完整返回(4)的 frame 中，$H_{{\rm an},i}$
仍具有以下**带原 source 积分**的含义：
$$
 \int_{[U(1)]}
       \vartheta_{\rm src}(h)
       \sum_{A,B} L_{i,h;A,B}\,
       \Theta_{-,i,h,A}(Z)\,
       \Theta_{+,i,h,B}(W)\,dh .
 \tag{6}
$$
这里 $\vartheta_{\rm src}\,dh$、$L_{i,h}$ 和两个 coherent
函数指上述同一全操作展开后的实际项；原 $C_a$、
Gaussian、similitude、arch 运输和 tame 因子全部保留。
(6)不是任取两个已有 rank-one theta 的乘积。
它尤其不把逐 word 的 $H_{{\rm an},i}$ 认成三条既有
$D_{102}\times S_{34}$ 总 toric period 之一。

对固定 source，读 $(n,n+2)$ 槽保持两 Hermite 次数差为2，
即保持原 binary source character。
但每个下 Maass 槽仍须在整个 $\mathcal T_i$ 中读取；
不能先追加仅在 $n\equiv4\bmod6$ 的旧 output-torus
角色投影。

原完整正常排序多项式
$$
 \mathcal L_{n,n+2}
 =\sum_{\ell=0}^n
   \frac{n!(n+2)!(-c)^\ell}
        {\ell!(n-\ell)!(n+2-\ell)!}\,
    \bar z^{\,n-\ell}z^{\,n+2-\ell}
$$
满足未除幂的逐项 Maass 恒等式
$$
 \delta_{3,{\rm cl}}^nf_i^{\rm an}(\tau_i)
  =a^n
     \left.\partial_Z^n\partial_W^{n+2}
                   H_{{\rm an},i}(Z,W)\right|_{0,0}.
 \tag{7}
$$
$\delta_{k,{\rm cl}}=(2\pi i)^{-1}
(\partial_\tau+k/(\tau-\bar\tau))$。
(7)用原来源(36)的归纳证明及同一 arch 操作；
该多项式恒等式对任意 $\tau_i$ 成立。
它不需要把一般 $\tau_i$ 的核分解成(4)。
$a^n$仍在(7)，没有因为 $a$ 已出现在 Gaussian 中而删掉它。

对每个固定有限槽，原复 Gaussian 的格点和及紧 source 积分
绝对收敛，故可逐项取这些有限次导数。
本稿只在这样的有限槽上使用(6)，不主张其各 rank-one
分量已经给出同一个 $p$-adic 有界测度。


## 3. 实际图源与 graded period 的全部费用

### 3.1 原 psi4 图源不是只给核乘负 delta

原 proper 图的形式为
$f_{\Omega_4}(\tau)=-\delta f_4(\tau/6)$。
令 $H_{f_4}$ 为 $f_4$ 的原完整核。
对应整个 coherent 核准确为
$$
 \boxed{
 H_{\rm geom}(\tau;Z,W)=
  -6\delta\,
  H_{f_4}\!\left(\tau/6;\frac Z{\sqrt6},\frac W{\sqrt6}\right).
 }
 \tag{8}
$$
因为
$\delta_{3,{\rm cl}}^n(f_4(\tau/6))
 =6^{-n}(\delta_{3,{\rm cl}}^nf_4)(\tau/6)$，
而总槽次数是 $2n+2$，(8)的槽给
$-6\delta\cdot6^{-n-1}=-\delta6^{-n}$，
正好返回同一个实际形式及全部导数。
同时 $c(y/6)/6=c(y)$，所以混合正常排序项也准确返回。
两种 $\sqrt6$ 在全部 $(n,n+2)$ 槽给相同结果；
若先保其它槽，先保原 angular source projector 再作此比较。
原 full2/full9、两个 sign、十八个17核及 Artin/Cor
仍与(8)一起运输。若 $H_{{\rm an},i}$ 已采用这个实际图规范，
(8)的倍率已在其内，不再施加第二次。

(8)对 $-w_0+W_p$ 同样逐项适用，
因为原两项均作同一个完整 tame 运输；
不把其中一项留在另一个 $\tau$ 或微分规范。

### 3.2 复 period 只用来代数化，不与书版 p-adic period 相认

对实际 word 选解析一致化
$$
 u_i:\mathbf C/(\mathbf Z+\tau_i\mathbf Z)\longrightarrow E_i(\mathbf C),
 \qquad u_i^*\omega_i=\gamma_i(2\pi i\,dz).
 \tag{9}
$$
$\gamma_i$ 是该微分的真实复 period。
标准 Tate 微分 $2\pi i\,dz$ 下，classical weight $k$
值变成几何值恰乘 $\gamma_i^{-k}$。

因此定义同一来源的几何 coherent 核为
$$
 \boxed{
 H_i(Z,W)=\gamma_i^{-1}
          H_{{\rm an},i}(Z/\gamma_i,W/\gamma_i).
 }
 \tag{10}
$$
其 $(n,n+2)$ 槽乘 $\gamma_i^{-(2n+3)}$，
所以原极化 KS 和 CM splitting 给
$$
 (\mathcal D_3^nf_i)(E_i,\omega_i)
   =a^n n!(n+2)!\,h_{i,n},\qquad
 h_{i,n}=[Z^nW^{n+2}]H_i .
 \tag{11}
$$
这是(7)的实际 graded 缩放，没有新增一个随权的归一。
所需槽在这一步完整代数化后，才用原
$\overline{\mathbf Q}\hookrightarrow\mathbf C_p$。
不把 $\gamma_i$ 本身嵌入 $\mathbf C_p$，也不令
$\gamma_i=\Omega_i$。
这里只需这些实际槽的代数性；不先为(6)中每个单独积分项
断言同一个代数 period 或同一个 $p$-adic 收敛域。

将(11)代入(2)，令
$$
 \rho_i=a p^2\kappa_i\Omega_i^2 .
$$
得到同一个 raw 输入的全部非负整数行
$$
 \boxed{
 R_{i,n}=\Omega_i^3\,\rho_i^n n!(n+2)!\,h_{i,n}.
 }
 \tag{12}
$$
源的 $-6\delta$、$C_a$、全 $L_{i,h}$ 及实际 complex
period 比均已在 $h_{i,n}$ 中；$\Omega_i^3,\rho_i$ 则是
原 book/KS 的显示费用。没有把它们藏在一个未知的总 scalar。

## 4. 完整逆 Maass 作用是一个指数卷积

为简记暂省略 $i$。式(1)作为指数生成函数的恒等式是
$$
 \sum_{n\ge0}R_n\frac{T^n}{n!}
 =(1-CT)^{-3}
   \sum_{n\ge0}m_n\frac1{n!}
                  \left(\frac T{1-CT}\right)^n .
 \tag{13}
$$
这是形式幂级数恒等式；不宣称右边在整个原 $Q$ 圆盘
有另一个未证明的解析代换。
两个同形变换的参数相加，因此逆变换准确以 $C$ 换成 $-C$：
$$
 m_n=\sum_{r=0}^n c_r(n)(-C)^rR_{n-r}.
 \tag{14}
$$
代入(12)后，全部中间阶乘相消，得到
$$
 \boxed{
 m_{i,n}
   =\Omega_i^3 n!(n+2)!
      \sum_{\ell=0}^n
       \frac{(-C_i)^{n-\ell}\rho_i^\ell}{(n-\ell)!}\,h_{i,\ell}.
 }
 \tag{15}
$$
等价地，令 $H_i^\Delta(U)=\sum_{\ell\ge0}h_{i,\ell}U^\ell$，
则
$$
 \frac{m_{i,n}}{\Omega_i^3 n!(n+2)!}
       =[T^n]\,e^{-C_iT}H_i^\Delta(\rho_iT).
 \tag{16}
$$
(15)在每个 $n$ 是有限精确恒等式；因此无需先为
$H_i^\Delta$ 证明新的 $p$-adic 收敛半径。
它保留所有 $\ell\le n$，包括原非主型和原 lower-Maass 槽。



## 4.1. 同一个二维核上的真实 p-adic cross Gaussian

由于 $\rho_i\ne0$，置
$$
 \beta_i=-C_i/\rho_i,\qquad
 \widetilde H_i(Z,W)=e^{\beta_iZW}H_i(Z,W).
 \tag{16a}
$$
在形式幂级数环中，每个固定二元槽的乘积只有有限项。
于是(15)等价于
$$
 \boxed{
 m_{i,n}=\Omega_i^3\rho_i^n n!(n+2)!
           [Z^nW^{n+2}]\widetilde H_i .
 }
 \tag{16b}
$$
确实，右端的第 $\ell$ 项含
$\rho_i^n\beta_i^{n-\ell}/(n-\ell)!
 =\rho_i^\ell(-C_i)^{n-\ell}/(n-\ell)!$，
恰是(15)，没有遗漏任一下 Maass 槽。

这也是一个有明确半径的真实 $p$-adic Gaussian。
在本题原最大阶坏点及全部单位 Tate 标记中，
$v_p(\Omega_i)=-\tau$、$\tau=p/(p^2-1)$，
$v_p(\kappa_i)=0$、$v_p(C_i)=2$，且 $a=17/2$ 为单位。
故
$$
 \boxed{
 v_p(\rho_i)=2-2\tau,\qquad
 v_p(\beta_i)=2\tau,\qquad
 v_p\!\left(\frac{\beta_i^r}{r!}\right)
 \ge \frac{r}{p+1}\quad(r\ge0).
 }
 \tag{16c}
$$
最后用 $v_p(r!)\le r/(p-1)$ 及
$2p/(p^2-1)-1/(p-1)=1/(p+1)$。
因此 $e^{\beta_iZW}$ 和 $e^{-\beta_iZW}$ 都属于完整闭
单位双盘上的整 Tate 代数；二者的乘积严格为1，常数项为1。
这是原实际 $C_i,\kappa_i,\Omega_i$ 给出的单位，
不是用一个可调 Gaussian 定义新的来源。

这里没有认
$\beta_i$ 等于复正常排序参数 $c(\operatorname{Im}\tau_i)/\gamma_i^2$，
也没有认它等于原 $z^{p+1}$ canonical completion。
$H_i$ 或(6)的每个 rank-one 分量在此闭盘的范数尚未由
(16c)单独支付；故不能由这个单位结论删除其高尾，
或给它们分别赋予有界测度。
本段只在同一个完整核上将原 inverse-Maass 精确合为
(16a)，有限精度仍按§§5–6的原 whole 来源计算。


## 5. 完整 log−E 核及真实有限转置

定义
$$
 F(t)=\sum_{r\ge0}r!t^r,\qquad
 E(t)=(1+t)F(t)-1
     =\sum_{r\ge1}(r+1)(r-1)!t^r .
 \tag{17}
$$
在实际 $t=C_i/x$、$x\in\mathbf Z_p^\times$ 上一致收敛；
$F$ 满足 $t^2F'+(t-1)F=-1$。
R1059(A14)因此可原样合写为
$$
 \mathcal M_{A_i}'(-2)
   =\int_{\mathbf Z_p^\times}
      x^{-2}\{\log\langle x\rangle-E(C_i/x)\}\,d\mu_i(x).
 \tag{18}
$$
这只是同一完整核的显示形式。新输入来自把它与(15)
和下方真实有限读者一起消费，不是给(17)另起一个来源。

取 R1056§6.1 的整多项式 $P_{2,H}$ 和全斜率
$K_{H,C_i}$，其在整个 $\mathbf Z_p$ 上分别以误差 $p^H$
逼近 $1_{\mathbf Z_p^\times}x^{-2}$ 和(18)的核。
这里包括 $p\mathbf Z_p$ 上的实际零值检验。
令
$$
 W_{i,H}(x)=
  \Lambda_i'(-2)P_{2,H}(x)
       +\Lambda_i(-2)K_{H,C_i}(x)
   =\sum_{n=0}^{N_H}w_{i,H,n}x^n.
 \tag{19}
$$
选原最小 $J\ge1$ 使
$J+1-\lfloor\log_p(J+1)\rfloor\ge H$，
置
$$
 e_H=\lfloor\log_pJ\rfloor,\quad d=p-1,\quad
 L=\left\lceil\frac{H+e_H+2}{d}\right\rceil,\quad M=dL-2,\quad
 N_H=\max\{M+dJ,pH-1\}.
$$
于是 $N_H=O(p(H+\log_p(H+1)+1))$。
所有系数和最低选择均采用原(30)--(36)，不重定义读者。

设
$$
 \nu_i=\min\{v_p(\Lambda_i(-2)),v_p(\Lambda_i'(-2))\},\qquad
 m_*=\min_i(m_i+\nu_i),
 \tag{20}
$$
其中零系数的估值取 $+\infty$，无贡献的字略去。
整个有限来源的真实误差满足
$$
 \mathcal S\equiv
   \sum_i\sum_{n=0}^{N_H}w_{i,H,n}m_{i,n}
       \pmod {p^{m_*+H}}.
 \tag{21}
$$
这一步的误差来自原 whole $\mu_i$，不来自拆开后某个
rank-one theta 的未经证明的有界性。
记号 $\bmod\,p^v$ 在非整数 $v$ 时表示差的估值至少 $v$。

将(15)代入(21)，有限重排给实际转置：
$$
 \boxed{
 \mathcal S\equiv
   \sum_i\sum_{\ell=0}^{N_H}
          B_{i,H,\ell}\,
              [Z^\ell W^{\ell+2}]H_i(Z,W)
       \pmod {p^{m_*+H}},
 }
 \tag{22}
$$
其中每个系数完全确定：
$$
 \boxed{
 B_{i,H,\ell}
 =\Omega_i^3\rho_i^\ell
     \sum_{n=\ell}^{N_H}
       w_{i,H,n}
       \frac{n!(n+2)!}{(n-\ell)!}
                 (-C_i)^{n-\ell}.
 }
 \tag{23}
$$
因此(22)可直接在原完整二维核中作用。
若使用已付 frame 的(6)，也可在整个 $h$ 积分及
$A,B$ 和中逐项作用。所有 derivative 是有限阶；
所有下 Maass 槽、source phase、原 $p^{-2}$ 和混合
$-102AB$ 均仍在。
不需要先把各个 $A,B$ 字当成 canonical source，也不需要
把整个 $h$ 积分拆成已经知道的三个 period。

同一方法对值端成立：把(19)替换为
$\Lambda_i(-2)P_{2,H}$，其它式子不变。
这与 R1059§8 的 actual 有限图值可以比较；
斜率则继续保(19)的两个外权及整个 $K_H$。

## 6. 实际输入精度和原 canonical 的剩余门

原(14)的系数在 $C_i$ 整时全整。
$w_{i,H,n}$ 的估值至少 $\nu_i-e_H$；
因此同一 $R_{i,0},\ldots,R_{i,N_H}$ 若各已知到
$m_i+H+e_H$，足以计算(21)到所示精度。
这里没有额外借一个免费的阶乘除法。

若实际计算的是几何槽 $h_{i,\ell}$，则必须按(23)
单独支付显示的周期、$\rho_i$、阶乘和全部源分母。
准确的充分条件是
$$
 h_{i,\ell}\text{ 的误差估值}\ \ge\
          m_*+H-v_p(B_{i,H,\ell})
 \quad\text{对所有 }B_{i,H,\ell}\ne0 .
 \tag{24}
$$
若再展开到(6)的各有限 coset，须将该项的完整
Haar/Weil/Artin 系数也计入同一个误差门。
不因 $p+1$ 是单位而删除 $p^{-2}$、原 $1/p$ 平均，
也不把全部 $\Omega_i,\rho_i$ 视为单位。
(24)以(23)的原显示系数精确保留为前提。
若系数也以近似值计算，令其误差为 $\Delta B$、槽误差为
$\Delta h$，还须逐项保持
$$
 v_p(\Delta B)+v_p(h)\ge m_*+H,\qquad
 v_p(B)+v_p(\Delta h)\ge m_*+H,\qquad
 v_p(\Delta B)+v_p(\Delta h)\ge m_*+H .
 \tag{25}
$$
这同时保原 $\Omega_i$ 等实际 $p$-adic 常数的输入精度；
没有把一个未计算 period 当成免费精确数。
(24)--(25)仅需有限个真实槽；它们没有要求每个分量的
无限级数在同一圆盘收敛。

R1060 的新接口是(22)--(24)：原整个临界斜率通过一个
明确的有限系数三角表，返回同一个实际双 Gaussian 输入。
它仍保 source 的全 $h$ 和，以及原 $p^2$ 全矩阵。
以后要把它压回原 $D_{102}$、$S_{34}$ 或三个 canonical
Newton 行，必须实付这个完整转置后的投影/同源身份。
原 rank2 坏条件目前不对这些新字逐个授权零。

尤其不能使用两种替换：

1. 将(6)逐 CM word 换成仅经过完整 toric/seesaw 投影后才
   得到的三个总 period 产品。
2. 把(3)已冻结的外权改成每个整数槽的正权外权
   $\Lambda_i(n)$，再借一个形式 cross 去掉下 Maass 槽。

本稿给出了可逐项检查这两个门的原有限读者，
未证明相应剩余恒等式，也不声称无穷 $p$ 非零或主目标完成。

## 7. 精确依赖

- [R1054](R1054-original-p-square-depleted-source-and-exact-conductor-blocks.md)
  §§1--5、8--9：实际 $-w_0+W_p$、全 finite matrix、
  同一 source/level 运输。
- [R1056](R1056-original-flat-amice-critical-slope-and-bol-primitive.md)
  §§1--2、6.1：完整 $c_r$、log/Maass 斜率、真正 whole
  $\mathbf Z_p$ 有限多项式及精度。
- [R1059](R1059-original-p-square-source-and-complete-critical-germ.md)
  (A0a)--(A0e)、(A5a)、(A11a)、(A14)--(A16)、§8：
  真实 Tate/cup/KS、两侧外权、全临界 germ 和 finite 图值。
- [原完整双 Hermite 核](../notes/2026-11-27-original-unsquared-toric-theta-source-and-newton-pullback.md)
  §§5、10--11，(32)--(39)：逐 Schwartz 正常排序、全
  source integral 和未除幂 $a^n\mathcal L_{n,n+2}$。
- [实际 psi4 曲面来源](../notes/2026-11-27-original-psi4-sign-surface-fulllevel-graphs-and-fp.md)
  §§5--8：$-\delta f_4(\tau/6)$、原两取向、完整 level
  和 proper fp 范围。

全篇是原来源的纸笔算子和有限重排，无新增数学运行。
