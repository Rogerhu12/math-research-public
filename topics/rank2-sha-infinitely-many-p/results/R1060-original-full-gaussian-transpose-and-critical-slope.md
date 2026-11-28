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


## 8. 原完整圆周积分给出的全部支撑

以下仍是(3a)、(6)定义的同一个完整来源。
特别，$[U(1)]$ 的无穷分量保留整个圆周；即使利用类数一
把有限部分改写成有限代表，也仍保它的角向投影。
令 $\mathsf P_2$ 是对 coherent 变量的这一投影：
$$
 \mathsf P_2F(Z,W)=
 \int_{|h|=1}h^{-2}F(h^{-1}Z,hW)\,d^\times h,
 \qquad \int_{|h|=1}d^\times h=1 .
 \tag{26}
$$
这里显示的单位 Haar 只是定义幂等投影；
原 $\mathcal T_i$ 的整体 Haar 常数仍在来源中。

在(3a)的原复核中，径向 Gaussian 和 $ZW$ 不变，
$Z^rW^s$ 项的 $h$ 角色是 $h^{s-r}$。
原 splitting 的共同标量由固定 source character 配对消掉；
剩余角色的绝对方向由原 $(0,2)$ 槽给出：
其 $2!$ 倍准确是 $z^2$ 的原 weight-three 来源，
所以所取的是 $s-r=2$，不是 $r-s=2$。
这用的是同一个 $\theta(\psi_4^2)$ 的来源字符，
不随有限字或 raised 次数另选字符。

原 modular Weil 的 $g_\infty$ 作用与这个 $U(1)$ dual-pair
作用交换，有限 Schwartz、level、Hecke 及 $p^2$ 字不改变
无穷分量的角色。正常排序中的每个 $ZW$ 因子也保持差为2。
因此先作实际 arch 运输，再作完整 source 积分，严格得到
$\mathsf P_2H_{{\rm an},i}=H_{{\rm an},i}$。
每个有限槽的格点和及积分绝对收敛，角色正交可以逐槽使用。
原(8)、(10)的两变量缩放均保持这个差，故
$$
 \boxed{
 H_i(Z,W)=W^2H_i^\Delta(ZW),\qquad
 \widetilde H_i(Z,W)=
 \Omega_i^{-3}\sum_{n\ge0}
 \frac{m_{i,n}Z^nW^{n+2}}
      {\rho_i^n n!(n+2)!}.
 }
 \tag{27}
$$
第二式用(16b)，不是另选的生成函数。
第一式也表明，§3已经代数化的全部对角槽就是整个核；
其余槽先在复来源中严格为零，故无需为它们另选 period。

(27)只在完成整个 $h_\infty$ 积分以后成立。
(6)的被积函数、单个 $A,B$ 项或任一 rank-one 因子，
通常都不具有这个支撑。特别不能在这些因子上单独施用
下面的有界性结论，或把圆周正交改成只对 $\mu_6$ 求和。
本节也没有追加旧 output-torus 的 $n\equiv4\bmod6$ 投影；
原所有 $n\ge0$ 的下 Maass 槽仍完整保留。

## 9. 同一来源的完整双变量 PD 返回

记 $X^{[r]}=X^r/r!$，定义 bounded Hurwitz 代数
$$
 \mathscr D^{\rm bd}=
 \left\{\sum_{r,s\ge0}b_{r,s}X^{[r]}Y^{[s]}:
                    \sup_{r,s}|b_{r,s}|_p<\infty\right\},
 \qquad
 \|F\|_{\rm PD}=\sup_{r,s}|b_{r,s}|_p .
 \tag{28}
$$
系数在 $\mathbf C_p$ 中，不要求原周期属于预先固定的有限扩域。
这是对显示范数完备的 Banach 代数：乘积的 $(r,s)$ 个 PD
系数是有限和，且其中的结构常数是
$\binom r a\binom s b\in\mathbf Z_p$。
因此乘法连续且范数次乘性成立。
任意有界 PD 级数的有限截断不一定按这个范数收敛；
这里的形式展开和有限系数乘法，不偷偷改成这种截断稠密性。

用原 $\Omega_i,\rho_i$ 作非对称的实际缩放，无需选择
$\sqrt{\rho_i}$：
$$
 \boxed{
 \mathscr B_i(X,Y):=
   \Omega_i^3\widetilde H_i(\rho_iX,Y)
   =\sum_{n\ge0}m_{i,n}X^{[n]}Y^{[n+2]},
 \qquad
 \Omega_i^3H_i(\rho_iX,Y)=e^{C_iXY}\mathscr B_i(X,Y).
 }
 \tag{29}
$$
第二式的符号来自 $\beta_i\rho_i=-C_i$。
它也逐项给出
$$
 [X^{[n]}Y^{[n+2]}]\,
      e^{C_iXY}\mathscr B_i
   =\sum_{r=0}^n
      \binom nr\binom{n+2}r r!C_i^r m_{i,n-r}
   =R_{i,n}.
$$
所以这里的双 PD 格确实返回(1)的原 Maass 系数，
包括 $n=0$ 的 $2!$，没有遗漏或新加阶乘。

$e^{\pm C_iXY}$ 的 $(r,r)$ 个 PD 系数是
$(\pm C_i)^r r!$，其余系数为零。
由于 $v_p(C_i)=2$，它和逆元都属于整的 bounded PD 代数，
范数都等于1。乘它们因而是等距变换，得到完整而非只逐槽的结论
$$
 \boxed{
 \|\mathscr B_i\|_{\rm PD}
 =\|\Omega_i^3H_i(\rho_iX,Y)\|_{\rm PD}
 =\sup_{n\ge0}|m_{i,n}|_p
 =\sup_{n\ge0}|R_{i,n}|_p
 \le p^{-m_i}.
 }
 \tag{30}
$$
这里差为2的子空间是闭线性子空间，不称它为乘法子代数。
等距性是在整个 $\mathscr D^{\rm bd}$ 中证明后再限制到它。
原 Haar、$p^{-2}$、finite word、两极化和全部 source 积分
都已经在 $m_{i,n}$ 与 $H_i$ 中；(29)没有重归一这些系数，
也不因改变局部基的配对而再乘一个隐藏的 $p$ 因子。

(29)--(30)是同一个 actual 来源的双 PD 返回。
它们不把两条 rank-one 来源分别认成有界测度，
也不将这个双阶乘格认成原单变量 canonical completion 的
任意乘法理想。§§5--6的原有限精度读者仍按(22)--(25)使用。

## 10. 整个核的严格闭盘范数与实际挠点半径

取 $r_Z,r_W\in\mathbf Q_{\ge0}$。
记 $\|\cdot\|_{r_Z,r_W}$ 为闭双盘
$|Z|_p\le p^{-r_Z}$、$|W|_p\le p^{-r_W}$ 的 Gauss 范数。
令
$$
 \tau=\frac p{p^2-1},\qquad
 R_{\rm crit}=2-2\tau+\frac2{p-1}
             =2+\frac2{p^2-1}.
$$
若
$$
 r_Z+r_W>R_{\rm crit},
$$
则原完整核和真实 cross-Gaussian 核均属于该闭盘的 Tate 代数，
且
$$
 \boxed{
 \|H_i\|_{r_Z,r_W}
   =\|\widetilde H_i\|_{r_Z,r_W}
   \le p^{-m_i-3\tau-2r_W}.
 }
 \tag{31}
$$

**证明。** 设 $s_p(n)$ 是整数 $n$ 的 $p$ 进数字和。
Legendre 式准确给出
$$
 v_p(n!)+v_p((n+2)!)
 =\frac{2n+2-s_p(n)-s_p(n+2)}{p-1}
 \le\frac{2n}{p-1}.
 \tag{32}
$$
在 $n=0$ 时数字和之和为2；在 $n\ge1$ 时两个整数均正，
数字和之和也至少为2。因此(32)包含原起点，不多损失常数。

用(27)、$v_p(\rho_i)=2-2\tau$ 及
$v_p(\Omega_i^{-3})=3\tau$，第 $n$ 项在该盘上的系数估值至少
$$
 \begin{split}
 &m_i+3\tau+2r_W+
  n\{r_Z+r_W-(2-2\tau)\}
      -v_p(n!)-v_p((n+2)!)\\
 &\hspace{2cm}\ge
 m_i+3\tau+2r_W+
             n(r_Z+r_W-R_{\rm crit}).
 \end{split}
 \tag{33}
$$
严格不等式使它趋于 $+\infty$，故给 Tate 收敛和所示范数界。
由(16c)，$e^{\beta_iZW}$ 及逆元在完整单位双盘都是
Gauss 范数1的单位，在当前更小闭盘亦然。
两方向相乘均不增范数，遂得(31)的范数相等。证毕。

不能只据矩有界把(31)的严格不等式改成等号。
例如有界矩序列 $m_n=1$ 来自实际有界测度 $\delta_1$。
当 $n=p^r$、$p>3$ 时，
$s_p(n)+s_p(n+2)=4$。
若 $r_Z+r_W=R_{\rm crit}$，则对应加权系数的估值恒为
$3\tau+2r_W+2/(p-1)$，不趋于无穷。
这个例子只说明“矩有界”这一假设不能支付边界 Tate 收敛；
不声称本题的具体来源一定达到这个收敛边界。

特别，对称闭盘的充分条件是
$$
 r_Z=r_W>1+\frac1{p^2-1}.
 \tag{34}
$$
原 R1054§3 在良整 height-two 形式参数中给出的非零 $p$
挠点、exact-$p^2$ 挠点估值分别为
$1/(p^2-1)$、$1/(p^2(p^2-1))$。
若某一个实际字已经核定 $Z,W$ 分别经单位切向解析同构
对应这些良整参数，则(34)保证的对称盘严格小于两种挠点盘。
一般若实际坐标为 $u_-=a_iZ+\cdots$、$u_+=b_iW+\cdots$，
必须同时保留 $v_p(a_i),v_p(b_i)$ 和这些坐标同构的真实半径；
本稿的 $\gamma_i$ 几何化本身没有支付每个 rank-one 分量或
新增 $p^2$ 字到这些参数的比例。
也不能把形式对数在挠点为零误作平移已进入当前盘。
因此(31)给出的是显示 $Z,W$ 变量的全核范数，
没有支付 $p$、$p^2$ 挠点的 Jacobi 平移，
更没有支付(6)各 rank-one 因子的此类平移。

## 11. 冻结外权后的共同 cross Gaussian 与完整 t 账本

以下在每一个固定 tame/maximal-CM 基字的 $t$ 轨道上分别取
基准标记 $0$；不同轨道不擅自共用其周期或显示常数。
只消费原单位标记的实际运输，不另外给它构造
$\mathbf Z_p$ 上的有界测度。令
$\chi_t=t/\bar t$；在 R1059 的同一 Teich 分量上，
原配对、周期及 Maass 参数为
$$
 \begin{gathered}
 \kappa_t=N(t),\qquad \Omega_t=\Omega_0/\bar t,\qquad
 \rho_t=\rho_0\chi_t,\qquad C_t=C_0,\\
 \beta_t\chi_t=\beta_0,\qquad
 \mathfrak j_t(j)=N(t)^{-j}\bar t^{\,3+2j},\qquad
 \frac{\mathfrak j_t'}{\mathfrak j_t}
       =-\log N(t)+2\log\bar t=-\log\chi_t .
 \end{gathered}
 \tag{35}
$$
对数均按所选单位分量取，固定 Teich 常数不被微分。
其中 $C_t=C_0$ 由 R1058(11)在中心 $L=0$ 的
$D_t(0)=1$ 得到：原 $y_{\rm dR}$ 的中心值不变，
所以实际 $p^2/y_{\rm dR}$ Maass 参数也不变。
这一步只用完整代数变换的中心值，不将主单位的闭盘估计
无条件搬给所有 tame 单位。
这里 $\chi_t$ 是原实际 lift 的单位，不把它先改成一个
有限 $T_2$ 角色，也不把任意 $\chi_t$ 幂当成整单位盘上的
Amice 变量代换。

对每个非负整数 $\ell$，冻结在临界点的外权给出准确式
$$
 \boxed{
 \mathfrak j_t(-2)\Omega_t^3\rho_t^\ell
       =\Omega_0^3\rho_0^\ell\chi_t^{\,\ell+2},\qquad
 \chi_t^{\,\ell+2}h_{t,\ell}
       =[Z^\ell W^{\ell+2}]H_t(Z,\chi_tW).
 }
 \tag{36}
$$
因此将(15)用于全部 $t$ 字时，
$\mathfrak j_t(-2)$ 可以完全移入实际核
$H_t(Z,\chi_tW)$，同时使用共同 $\Omega_0,\rho_0,C_0$。
并且
$$
 \boxed{
 \widetilde H_t(Z,\chi_tW)
       =e^{\beta_0ZW}H_t(Z,\chi_tW).
 }
 \tag{37}
$$
这使用的是 $\beta_t\chi_t=\beta_0$，不是把各个
$\beta_t$ 无条件认成 $\beta_0$。
故在冻结后的完整 $t$ 和中，所有字共用同一个真实 cross
Gaussian，而实际核、两极化、$L_{t,h}$、原 Haar 和
$\chi_t$ 的完整 lift 仍全部保留。
由于 $\chi_t$ 是单位，(31)的盘和范数界保持不变。

为显示斜率费用，写
$\Lambda_t(j)=\lambda_t(j)\mathfrak j_t(j)$。
(19)的整个多项式读者准确为
$$
 \begin{split}
 W_{t,H}(x)=\mathfrak j_t(-2)\big[
   \{\lambda_t'(-2)-\lambda_t(-2)\log\chi_t\}\,P_{2,H}(x)
       +\lambda_t(-2)K_{H,C_0}(x)\big].
 \end{split}
 \tag{38}
$$
因此在(22)--(23)中以 $H_t(Z,\chi_tW)$ 代替 $H_t$，
以共同 $\Omega_0,\rho_0,C_0$ 代替相应显示常数，
并以(38)方括号内的系数代替 $w_{t,H,n}$，给出同一完整斜率。
其中 $-\lambda_t\log\chi_t\,P_{2,H}$ 是真实值端补项；
不能由全 Maass 斜率或一个有限角色投影删掉。
$\lambda_t'$ 中其余 avatar、Norm 和外部权导数也仍按原式保留。

等价地，冻结后的整个 PD 来源为
$$
 \Omega_0^3e^{-C_0XY}H_t(\rho_0X,\chi_tY)
   =\sum_{n\ge0}\mathfrak j_t(-2)m_{t,n}
                   X^{[n]}Y^{[n+2]} .
$$
$\mathfrak j_t(-2)$ 为单位，所以本式继承(30)的完整 PD
范数，而没有对单个 rank-one 因子提出任何额外范数断言。
全部有限求和的误差仍由(20)--(25)的实际外权统一支付。

本次新增结论是完整 source 积分后的支撑、同来源双 PD
等距返回、严格闭盘范数以及冻结 $t$ 权的准确消费。
这些结论并不把原 rank2 canonical 坏条件扩展成新的乘法零，
也不以所得小盘代替仍待支付的实际挠点平移。


## 12. 原 canonical completion 的真实 tensor 与圆周次序

本节只在原已付 rank-one 分解及实际变量规范处使用
$D_{102}$、$S_{34}$ 的名称。原 $p^2$ 新字及其有限和
若尚未被识别成这些来源，就仍保自己的完整 theta 函数、
Miller/Weil 作用及两极化；不依据此节给这些字另赋 canonical 零。

### 12.1 两物理变量和 completion 系数一起运输

置 $d=p+1$。原
[psi4 来源](../notes/2026-11-27-original-psi4-canonical-positive-slot-and-degree102-negative-source.md)
§§7、9、10 已付：在其固定 Hermite 参数中，两条物理变量为
$$
 z_-=\ell_{\rm coh}Z/\delta,\qquad
 z_+=\ell_{\rm coh}W,\qquad
 C_-=102c_\sigma,\quad C_+=34c_\sigma .
$$
$\ell_{\rm coh}$ 是该文的实际复 Hermite/period 倍率
$\Omega_{0,\mathbf C}h_{\rm Hermite}$；
此处它不指本篇的 book $p$-adic 周期 $\Omega_i$，
也不被单独嵌入 $\mathbf C_p$。
两式对 $Z,W$ 都是复线性的，没有再取复共轭。
原两 Hermite 参数的相位、三处 similitude 和全部 raw 幅度
已经在来源中支付，不在此重新选择。

较一般地，在一个已经完整运输的 framed word 中，将实际倍率
记为 $a_-,a_+$，定义 coherent completion 系数
$$
 u=C_-a_-^d,\qquad v=C_+a_+^d .
 \tag{39}
$$
在上述原 canonical block 中，
$a_-=\ell_{\rm coh}/\delta,\ a_+=\ell_{\rm coh}$，故
$u/v=3/\delta^d=q_\delta^{-1}$。
这是原 $102/34$ 的真实差别；$u,v$ 均不是(1)的 Maass 常数 $C_i$。

以下核对它们的微分框架费用。若同一实际椭圆曲线的物理微分
改为 $\omega'=e\omega$，则在相应参数中 $z'=ez$，原 sigma
刚性化给
$\sigma_{\omega'}(ez)=e\sigma_\omega(z)$。
取 $\log(\sigma/z)$ 的第 $d$ 项，得到
$$
 c_\sigma(\omega')=e^{-d}c_\sigma(\omega),\qquad
 \bigl(Nc_\sigma(\omega')\bigr)(z')^d
       =\bigl(Nc_\sigma(\omega)\bigr)z^d .
 \tag{40}
$$
原截面的其它 frame 倍率照旧保留。
因此只搬 $c_\sigma$ 而不搬物理变量、period 的作法并不合法。

对一个已由完整 Miller 身份识别的实际 $[p]^*s_N$，在良整物理
参数 $z=pz'$ 中，原 completion 的拉回是
$p^dNc_\sigma$；而覆盖线丛次数为 $Np^2$，其标准 degree
completion 是 $p^2Nc_\sigma$。准确的两个完成源满足
$$
 \begin{split}
 s_N(pz')e^{-p^dNc_\sigma(z')^d}
 ={}&e^{-(p^d-p^2)Nc_\sigma(z')^d}\\
 &\quad\cdot s_N(pz')e^{-p^2Nc_\sigma(z')^d}.
 \end{split}
 \tag{40a}
$$
对原 $N=34,102$、$p>211$，已付
$v_p(c_\sigma)=-1$ 给
$v_p((p^d-p^2)Nc_\sigma)=1$。
故(40a)的指数及其逆在这个**良整物理参数**的闭单位盘
为整 Tate 单位。改成 coherent 参数时仍须连同实际线性
倍率运输，不能据此宣称每个新字在同一个 coherent 盘上为单位。

即使在该物理盘，这个单位也不允许相认两个 Newton 读者。
对任一实际共同槽偏移、正整数 $k$，原有限 Newton 消去显示
$J_{\rm pull}(k)=p^{(2-d)k}J_{\rm degree}(k)$；
它是两 completion 的 $C^{-k}$ 规范的准确比。
不能把这个非单位幂当成一个已定义的解析权函数。
以上只用于已付 $[p]$ 身份的字；没有把一般 cyclic-$p^2$
theta 字先认作这样的 pullback。

R1060(3a)中的 source $h_\infty\in U(1)$ 不改变固定的
modular 字 $g_i$、其 CM 曲线 $E_i$ 或(9)的 $\gamma_i$。
它在已付 coherent 参数上的实际作用是
$(Z,W)\mapsto(h^{-1}Z,hW)$。
所以在固定 base 物理微分中，真正拉回的 completion 为
$$
 \boxed{
 E_h(Z,W)=
 \exp\!\left(-u h^{-d}Z^d-vh^dW^d\right).
 }
 \tag{41}
$$
若另外采用随 $h$ 变化的物理 frame，令其倍率为 $e_\pm(h)$，
则两物理参数分别乘 $e_\pm(h)$，而两 completion 系数分别乘
$e_\pm(h)^{-d}$。由(40)这些额外变化准确抵消；
(41)中的原 $h^{-d},h^d$ 不消失。
这里没有把保持 $F(h^{-1}Z,hW)$ 的同时又令 completion
系数不随 $h$ 变的不同操作冒称为原物理 completion。

### 12.2 真正圆周投影保留完整双卷积

先固定其它实际 finite/source 变量，记未作该圆周积分的
完整 framed 核为
$F(Z,W)=\sum f_{a,b}Z^aW^b$。
如该处原分解已经支付，可写为完整两因子的乘积；
此处不凭相同 Hecke 标签代换这两个因子。
由(41)，canonical completion 的圆周返回准确为
$$
 \begin{split}
 &\int_{|h|=1}h^{-2}
  e^{-u h^{-d}Z^d-vh^dW^d}
          F(h^{-1}Z,hW)\,d^\times h\\
 &\hspace{12mm}=
  \mathsf P_2\!\left(e^{-uZ^d-vW^d}F(Z,W)\right).
 \end{split}
 \tag{42}
$$
每个固定双槽只有有限项，故只需原有限 theta jets 的收敛，
无需给单个 rank-one 函数另加 $p$-adic 范数。

展开中 $f_{a,b}$ 与第 $(r,s)$ 个 completion 项的总圆周角色是
$h^{\,b+ds-a-dr}$。因而保留的条件是
$$
 b+ds-a-dr=2 .
$$
特别对原 $(n,n+2)$ 输出，所有合法的 $r,s$ 都保留：
$$
 \boxed{
 [Z^nW^{n+2}]\mathsf P_2(e^{-uZ^d-vW^d}F)
 =\sum_{\substack{r,s\ge0\\dr\le n,\ ds\le n+2}}
  \frac{(-u)^r(-v)^s}{r!s!}
      f_{n-dr,n+2-ds}.
 }
 \tag{43}
$$
裸低槽的差是 $2+d(r-s)$；
completion tensor 的 $h^{-d(r-s)}$ 正好补回原 source 角色2。
所以 $r\ne s$ 项不被圆周投影自动杀掉，也不是凭空新增一条
可赋中央零的来源。

若先把 $F$ 换成已经投影的 $H=\mathsf P_2F$，
然后再乘两个 completion 并再次投影，才会得到另一式
$$
 \mathsf P_2(e^{-uZ^d-vW^d}H)
       =H\sum_{r\ge0}\frac{(uv)^r(ZW)^{dr}}{(r!)^2}.
$$
这是合法的 postprojection 恒等式，但一般不等于(42)。
因此不能从§8已经得到的 $H=W^2H^\Delta(ZW)$，
删除(43)中的非对角低槽或直接以这条 Bessel 型因子
替代原 canonical completion。

### 12.3 接回同一有限 Maass 读者

令
$F^{\rm can}=e^{-uZ^d-vW^d}F$，其普通系数记为
$f^{\rm can}_{a,b}$。
取负指标时该系数按零处理。
先反转这两个实际 completion，再反转原 Maass Gaussian，
由 $\mathsf P_2$ 与 $e^{\beta_iZW}$ 交换，得到每个 $n$ 的
有限精确式
$$
 \boxed{
 [Z^nW^{n+2}]
   e^{\beta_iZW}\mathsf P_2F
  =
  \sum_{\substack{q,r,s\ge0\\q+dr\le n,\ q+ds\le n+2}}
   \frac{\beta_i^q u^r v^s}{q!\,r!\,s!}\,
      f^{\rm can}_{n-q-dr,\ n+2-q-ds}.
 }
 \tag{44}
$$
这里反转 canonical completion 的符号为正，
而 $\beta_i=-C_i/\rho_i$ 保原 inverse-Maass 的负号。
出现的低槽始终满足
$b-a\equiv2\pmod d$；这不是仅保 $a=b-2$ 的单对角表。

推导(44)时，先用独立形式参数 $B$ 代替 $\beta_i$，把它视为
一个有限的 $B$ 多项式身份。对每个 $B^q$ 系数分别完成原
完整来源及(9)--(11)的 graded 几何代数化，取原 $p$ 嵌入后，
才在相应几何变量中代入 $B=\beta_i$。
这里没有把 $p$-adic 的 $\beta_i$ 当成复常数。

(44)按此意义先在原有限 theta jets 的 graded 来源中成立。
其余全部 finite 字、$h$ 的有限部分、Haar、Artin/Cor 和
frame 运输按原 $\mathcal T_i$ 作用于**整式**。
如果 $u,v$ 随这些 framed 字变化，就把它们保在同一求和项内。
完成原(9)--(11)的整体几何代数化后，再按原嵌入读为
$p$-adic 公式；不单独把一个复 period 或未代数化被积项
嵌入 $\mathbf C_p$。

具体地，将(44)的完整返回乘
$\Omega_i^3\rho_i^n n!(n+2)!$，就是(16b)的同一个 $m_{i,n}$。
再乘(19)的 $w_{i,H,n}$，只需 $0\le n\le N_H$，
便得到(21)的有限 canonical-completion 转置。
全部三重和有限；原 whole 误差仍是 $p^{m_*+H}$。
若这些输入以近似值给出，须对(44)的每个完整系数及来源项
应用(24)--(25)的同一乘积误差规则。
本式不给 $f^{\rm can}_{a,b}$ 各自一个额外有界测度或统一范数。

冻结的实际 $t$ 权也必须连这个 completion 运输：
当(36)使用 $F_t(Z,\chi_tW)$ 时，
$v$ 同时变成 $v\chi_t^d$，而负侧 $u$ 保留；
不能只缩放 theta 函数而固定其 positive completion。
原 cross Gaussian 则依(37)统一为 $e^{\beta_0ZW}$。
这两个不同的 Gaussian 运输一起保留(38)的
$-\lambda_t\log\chi_t\,P_{2,H}$ 补项。

本节给出的是原 completion 的真实 tensor、正确圆周次序，
以及可直接送入原有限读者的三重系数表。
它没有将整个 $p^2$ 新来源逐字认成 $D_{102}\times S_{34}$，
也没有由一条 canonical Newton 零给这些有限低槽分别赋零。


## 13. 共同 [p] 覆盖变量中的完整 PD 与严格盘界

本节消费原共同覆盖的实际变量关系
$z=pz'$，并始终保原 section 的首项和完整 Miller 乘子。
若某个待比较的几何表达尚未被证明等于这一实际 pullback，
以下等式不为它补上该几何身份。

在两个已识别的 coherent 变量中，定义未重归一的覆盖核
$$
 \widehat H_i(Z',W')=H_i(pZ',pW'),\qquad
 \widehat{\widetilde H}_i(Z',W')
       =\widetilde H_i(pZ',pW').
 \tag{45}
$$
整个有限 $p^2$ 字、Haar、source 积分和冻结权都仍在 $H_i$ 中。
由§8的**whole** 支撑，
$$
 \widehat h_{i,n}=p^{2n+2}h_{i,n}.
$$
因此设置
$\widehat\rho_i=\rho_i/p^2$、
$\widehat\beta_i=p^2\beta_i$ 后，实际矩准确返回为
$$
 \boxed{
 \begin{split}
 m_{i,n}={}&p^{-2}\Omega_i^3\widehat\rho_i^{\,n}
 n!(n+2)!\,
 [Z'^nW'^{n+2}]
       \bigl(e^{\widehat\beta_i Z'W'}\widehat H_i\bigr),\\
 p^{-2}\Omega_i^3
   e^{-C_iXY}\widehat H_i(\widehat\rho_iX,Y)
  ={}&\sum_{n\ge0}m_{i,n}X^{[n]}Y^{[n+2]}
   =\mathscr B_i(X,Y).
 \end{split}
 }
 \tag{46}
$$
这里 $\widehat\beta_i\widehat\rho_i=-C_i$，
所以原 Maass 常数没有改变。
第二式也可直接由
$H_i((\rho_i/p)X,pY)=p^2H_i(\rho_iX,Y)$ 核对。
显示的 $p^{-2}$ 完全来自差为2的次数缩放；
它不是再次施加 finite Haar 的 $p^{-2}$、图平均或 seed 归一。

特别，若实际几何证明以未归一 Haar coevaluation 书写
$K=p^{-2}(1\otimes\rho_+(t_0))\mathcal C_{\rm Haar}$，
这个有限 $p^{-2}$ 仍是原 $K$ 的一部分。
(46)只对整个相同核改变 coherent 变量，不修改其有限输入，
也不因改用字坐标配对而增减一个 $p$。

由(16c)，
$$
 v_p(\widehat\rho_i)=-2\tau,\qquad
 v_p(\widehat\beta_i)=2+2\tau.
$$
取 $r_{Z'},r_{W'}\in\mathbf Q_{\ge0}$，若
$$
 r_{Z'}+r_{W'}>\frac2{p^2-1},
$$
则覆盖中的两个完整核都是该闭盘上的 Tate 函数，且
$$
 \boxed{
 \|\widehat H_i\|_{r_{Z'},r_{W'}}
 =\|\widehat{\widetilde H}_i\|_{r_{Z'},r_{W'}}
 \le p^{-m_i-3\tau-2-2r_{W'}}.
 }
 \tag{47}
$$
证明直接将§10的 $r_Z,r_W$ 换成
$1+r_{Z'},1+r_{W'}$；也可由(46)及(32)逐项证明。
这里没有给两个 rank-one 因子分别作估值。

对称阈值为
$r_{Z'}=r_{W'}>1/(p^2-1)$。
因此在另已支付与良整形式参数的单位切向比较时，
本结论恰到非零 $p$ 挠点半径的严格内侧；
exact-$p^2$ 挠点仍在更外层。
如果实际 parameter 比有非单位倍率，须先按§10的完整
frame 规则运输盘；不能把该倍率省掉。
即使是单位倍率，也不能由(47)推出边界收敛：
§10的 $m_n=1,n=p^r$ 检验在这个 rescaling 后仍给固定估值，
所以这里保留严格不等式。

还可在原定义中直接返回整个 canonical Newton 函数。
对任一原实际槽偏移 $\ell$（本题为 $-2$ 或 $0$），写
$$
 J_{F,\ell}(v;C)=
 \sum_{h\ge0}C^{-h}[z^{dh+\ell}]
       (F(z)e^{-Cz^d})(v)_h .
$$
只要右边是原已付完整尾的来源，真实 $[p]$ 拉回便逐个 $h$ 给出
$$
 \boxed{
 J_{F(p\,\cdot),\ell}(v;p^dC)
       =p^\ell J_{F,\ell}(v;C).
 }
 \tag{48}
$$
证明是实际完成源
$F(pz')e^{-p^dC(z')^d}=(Fe^{-Cz^d})(pz')$
的第 $dh+\ell$ 系数恰乘 $p^{dh+\ell}$，再与
$(p^dC)^{-h}$ 相消。负指标按零处理，故 $\ell=-2,h=0$
也没有例外；全尾仅乘固定 $p^\ell$，原解析性准确继承。
这不是对 $p^{dv}$ 作解析延拓。

因此对已经完整识别的 positive $[p]^*S$，使用真实 pullback
completion 时，原 $J_S'(0)=0$ 合法原样运输；
negative 的偏移 $-2$ 则严格留下 $p^{-2}$。
这一结论依赖实际来源及 completion 同时拉回，不能只由
覆盖线丛次数或同一个有限角色得出。
相反，采用 $p^2C$ 的 degree completion，只在正整数处直接有
$J_{\rm degree}(k)=p^{(d-2)k+\ell}J_{F,\ell}(k;C)$。
(40a)的整 gauge 本身不支付这个 degree 读者在整个
$\mathbf Z_p$ 上的 Tate 收敛，也不支付将此非单位整数幂
解析化。

最后，(46)的 cross Gaussian 是 inverse-Maass 的二次项，
与(40a)的 $z^{p+1}$ canonical completion 不同。
把覆盖核继续送入原 $D_{102}/S_{34}$ completion 时，
必须使用§12的实际 tensor、完整角槽和(40a)的准确 gauge，
并保所有固定 $t$ 字中的
$\widehat\beta_t\chi_t=\widehat\beta_0$。
本节没有用共同覆盖的次数替换原实际 completion 权，
也没有以变量缩放取得新的 canonical 零行。



### 13.1 临界闭盘恰检测整个单位测度

本小节仍只使用原 whole bounded Amice 测度 $\mu_i$、
(45)--(46)的同一覆盖核及全部原 frame。
固定
$r_{Z'},r_{W'}\in\mathbf Q_{\ge0}$，现在取临界等号
$$
 r_{Z'}+r_{W'}=\frac2{p^2-1}.
$$
令 $\mathbb D_{\rm crit}$ 为对应的完整闭双盘。
则有准确的充要判据
$$
 \boxed{
 \widehat H_i\in\mathcal O(\mathbb D_{\rm crit})
 \quad\Longleftrightarrow\quad
 \widehat{\widetilde H}_i\in\mathcal O(\mathbb D_{\rm crit})
 \quad\Longleftrightarrow\quad
 \mu_i|_{\mathbf Z_p^\times}=0 .
 }
 \tag{49}
$$
$\mathcal O$ 在此指该闭盘的 Tate 代数，
不是仅在每个严格小子盘上解析。
右侧指整个单位部分的 bounded measure 为零；
不是一条 Teich 分量、一项负矩或一条 canonical $J'(0)$ 为零。

**证明。** 第一项与第二项等价，因为
$e^{\pm\widehat\beta_iZ'W'}$ 在闭单位双盘中都是
Gauss 范数1的 Tate 单位，故在 $\mathbb D_{\rm crit}$ 上亦然。
由(27)、(45)及 Legendre 的准确等号，
$\widehat{\widetilde H}_i$ 第 $(n,n+2)$ 项的加权系数估值恰为
$$
 \begin{split}
 v_p(m_{i,n})+3\tau+2+2r_{W'}
  +\frac{s_p(n)+s_p(n+2)-2}{p-1}.
 \end{split}
 \tag{50}
$$
若 $m_{i,n}=0$，相应估值按 $+\infty$ 处理。
所以 Tate 收敛等价于(50)随 $n\to\infty$ 趋于 $+\infty$。

先假设此收敛成立。固定任一整数 $j\ge0$，令
$n_r=j+p^r$。对充分大的 $r$，有 $p^r>j+2$，于是
$$
 s_p(n_r)=1+s_p(j),\qquad
 s_p(n_r+2)=1+s_p(j+2).
$$
(50)中的数字和部分因此与 $r$ 无关，
Tate 收敛迫 $m_{i,j+p^r}\to0$。

另一方面，记 $\operatorname{Teich}(x)$ 为
$x\in\mathbf Z_p^\times$ 的 Teichmüller 部分。
在整个 $\mathbf Z_p$ 上有一致极限
$$
 x^{j+p^r}\longrightarrow
 {\bf1}_{\mathbf Z_p^\times}(x)\,
          x^j\operatorname{Teich}(x),
$$
故原 bounded measure 给
$$
 \lim_{r\to\infty}m_{i,j+p^r}
 =\int_{\mathbf Z_p^\times}
       x^j\operatorname{Teich}(x)\,d\mu_i(x)=0
 \qquad(j\ge0).
 \tag{51}
$$
一致性可以直接核对：在 $p\mathbf Z_p$ 上，左边估值至少
$j+p^r$；在单位上，
$x^{p^r}=\operatorname{Teich}(x)\langle x\rangle^{p^r}$，
且 $\langle x\rangle^{p^r}\to1$ 一致成立。
这里积分换极限只使用同一个原 measure 的 bounded 范数。

令
$d\nu={\bf1}_{\mathbf Z_p^\times}\operatorname{Teich}(x)\,d\mu_i$。
(51)说 $\nu$ 杀掉所有普通多项式。
每个 Mahler 多项式 $\binom{x}{m}$ 都是有限个普通单项式的
$\mathbf Q_p$ 线性组合；这些 Mahler 多项式的有限和在
$C(\mathbf Z_p,\mathbf C_p)$ 中稠密。
因此 $\nu=0$。
在单位 clopen 集上乘回连续单位
$\operatorname{Teich}(x)^{-1}$，得到
$\mu_i|_{\mathbf Z_p^\times}=0$。

反之，若这个单位部分为零，整个 measure 仅在
$p\mathbf Z_p$ 上贡献。由原范数界，
$v_p(m_{i,n})\ge m_i+n$。
(50)的数字和修正非负，故其估值至少
$m_i+n+3\tau+2+2r_{W'}$，趋于无穷。
于是覆盖核在临界闭盘上为 Tate。证毕。

(49)给§10的边界不足一个完整而精确的解释：
对原非零单位读者，所缺的并不是把一个严格不等式草率地换成
弱不等式；同一 coherent frame 的完整边界 Tate 延拓
已经会迫整个单位测度消失。
这个结论并不否定在其它几何坐标、线丛 frame 或图册中的
正则延拓。良整形式参数中的 section 正则性、形式对数在
挠点的退化，以及本篇这个 Lie/coherent 核的 Tate 延拓，
仍是需要实付运输的不同断言。
