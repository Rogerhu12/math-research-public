# R232：负秩一后的真实 regular 格与无饱和损失的辅助两矩

日期：2026-11-13。**状态：已证明的原对象比较；未证明跨素数两矩非零。**

采用 R150、R153、R156 的同一固定曲线、同一原域表和原完整点
$$
 E:y^2+y=x^3+x^2-2x,\qquad
 Q=[t_0]\operatorname{Tr}_{F[\ell]/L}P[\ell]\ne O.
$$
删去 R230 的固定有限例外后，负扭曲秩一、负号 Sha 的
$p$ 初级部分为零。先为每个原表域固定一个非挠负点
$P_-\in E(F)^-$；再删去它在该秩一格中的固定指数的素因子。
因此 $P_-$ 对此后每个 $p$ 都生成 $E(F)^-\otimes\mathbb Z_p$。
本选择由 R230 的秩一结论保证，不假设任何局部原始性。

令
$$
 \Gamma=\langle\tau\rangle\simeq C_p,\quad
 R=\mathbb Z_p[\Gamma],\quad
 \mathcal O=\mathbb Z_p[\zeta_p],\quad
 g=(p-1)/2,\quad
 \delta=\tau^g(\tau-1),\quad
 \Delta=\delta^2=\tau+\tau^{-1}-2,
$$
$$
 B=E(L)\otimes\mathbb Z_p,\qquad
 B_0=E(F)\otimes\mathbb Z_p,\qquad
 A_0=\ker(N_\Gamma:B\longrightarrow B_0)=\mathcal O w.
\tag{1}
$$
所有这些都是原 Mordell--Weil 格。除去已有有限挠点例外后
均无 $p$ 挠点。写 $Q=\delta^a\varepsilon w$。
按原完整 Heegner 共轭公式，将 $Q$ 乘一个 $\tau$ 幂后可令
$cQ=-Q$；这不改变 $a$。全文所用矩的非零性亦不受此平移影响。

**主要结论。** 对每个合法的原输入 $(F,p,\ell,Q)$，存在
一个由明确条件定义、非空的辅助素数族 $\mathcal Q(F,p,\ell)$。
它只用于观测，不改变原 $\ell,L,Q$。在每个 $q\in\mathcal Q$
的全部 $p$ 个完成上计算下文 (11) 的两条线性矩，则
$$
 \boxed{\quad
 a\le1
 \quad\Longleftrightarrow\quad
 \exists q\in\mathcal Q(F,p,\ell):
        (M_1^+(Q;q),M_2^-(Q;q))\ne(0,0).
 \quad}
\tag{2}
$$
$a=1$ 时族中每个 $q$ 的第二矩均非零；$a=0$ 时存在
Chebotarev 正密度子族使第一矩非零；$a\ge2$ 时全部两矩为零。

**必须区分：** 下文的 $\kappa_{\delta,A}(Q)$ 是原点 $Q$ 的
通常 $\delta$-Kummer 类。它不是 R156 原 Kolyvagin 族的首项。
该原首项仍为 $(\tau-1)Q$，指数仍是 $a+1$。本篇没有将
整个原族除以 $\delta$。

## 1. 真正的全局 $H^1(\Gamma)$ 与奇数指数分支

循环群上同调给
$$
 H^1(\Gamma,B)=A_0/(\tau-1)B,\qquad
 \delta A_0\subset(\tau-1)B\subset A_0.
\tag{3}
$$
所以它是零或一维 $\mathbb F_p$ 空间。R146 §2 已在每个
有限位证明真实局部群 $H^1(\Gamma_v,E(L_w))$ 为零：
在 $\ell$ 用 $p\nmid(\ell+1)^2-a_\ell^2$，其余好位用
不分歧迹与 Lang，$389$ 位用 Tate 参数估值一。无穷位
对奇 $p$ 无贡献。由全局 inflation--restriction，
(3) 因而真实注入
$$
                   \Sha(E/F)[p].
\tag{4}
$$
这里可先对有限生成的实际点群作上同调，再取 $p$ 初级部分；
与 (3) 的 $\mathbb Z_p$ 格计算相同。

必须保留复共轭作用的反号。一个 cocycle 由
$f(\tau)=x\in A_0$ 给出；其共轭在 $\tau$ 的值是
$-\,\tau cx$。模 $(\tau-1)B$ 后为 $-cx$。
R146 的原点符号给 $A_0/\delta A_0$ 的符号
$(-1)^{a+1}$，故 (3) 非零时的**上同调**符号为 $(-1)^a$。
当 $a$ 奇时，(4) 落入已由 R230 消去的负号 Sha，
所以
$$
           \boxed{\quad a\text{ 奇}\Longrightarrow
                     A_0=\delta B.\quad}
\tag{5}
$$

(5) 只对这个真实格断言一次差分可解；不说所有
Heegner 辅助节点的范数都为零。

## 2. 奇数分支上的完整 regular 分解

假设 $a$ 奇。由 (5) 取 $X_0\in B$，使 $\delta X_0$
是 $A_0$ 的 $\mathcal O$ 生成元。此生成元模 $\delta$
的点符号为正。因为 $c\delta=-\delta c$，将 $X_0$ 替换为
$(1-c)X_0/2$ 后，仍有 $\delta X_0$ 为生成元，且 $cX_0=-X_0$。

$N_\Gamma X_0$ 在 $B_0^-$ 中为 $p$ 原始。若它属于
$pB_0$，写 $N_\Gamma X_0=pY$，则 $X_0-Y\in A_0$，从而
$\delta X_0\in\delta A_0$，与生成元性质矛盾。
因此以一个 $\mathbb Z_p$ 单位缩放，可取得
$$
                       cX=-X,\qquad N_\Gamma X=P_-.
\tag{6}
$$
这是实际完备点格中的元素；不声称该 $\mathbb Z_p$ 单位
一定是一个整数或给出未证明的全局除点。

进一步有真正的 $R$ 模分解
$$
                 \boxed{\quad B=RX\oplus B_0^+,\qquad
                             A_0=\delta RX.\quad}
\tag{7}
$$
证明如下。映射
$$
 NB/pB_0\longrightarrow A_0/\delta A_0,\qquad
 NY\longmapsto\delta Y
$$
良定义且单射；(5) 使它满射。由 (6)，得到
$NB=\mathbb Z_pP_-+pB_0$。故每个 $Y\in B$ 的范数可写成
$bP_-+pZ$，其中 $Z\in B_0^+$；减去 $bX+Z$ 后余项在
$A_0=\delta RX$，证明 (7) 的满性。

若 $fX=0$，对它施加 $\delta$，由 $\delta X$ 的
$\mathcal O$ 原始性知 $f\in\mathbb Z_p N_\Gamma$；再用
$N_\Gamma X=P_-\ne0$ 得 $f=0$。所以 $RX$ 确为一个
自由秩一的 regular $R$ 模。它的 $\Gamma$ 不变部分
是 $\mathbb Z_pP_-$，为负号；与 $B_0^+$ 交零。
这证明 (7) 的直和性，没有引用未付的抽象格分类。

### 2.1 指定原点的真实范数坐标

令 $R^+=\{r\in R:r^*=r\}$，其中 $\tau^*=\tau^{-1}$。
Chebyshev 递推使 $1,\Delta,\ldots,\Delta^g$ 成为它的
$\mathbb Z_p$ 基；写
$$
 N_\Gamma=\Psi_p(\Delta),\qquad
 R^+=\mathbb Z_p[\Delta]/(\Delta\Psi_p(\Delta)),
 \qquad \Psi_p(0)=p.
\tag{8}
$$
$\Psi_p$ 为首一、次数 $g$ 的 Eisenstein 多项式。
例如模 $p$ 时，令 $T=\tau-1$，则
$N_\Gamma=T^{p-1}$、$\Delta=T^2/(1+T)$，
所以 $\Psi_p(U)\equiv U^g\pmod p$；常数项准确为 $p$。
因此 $\mathcal O^+=\mathbb Z_p[\Delta]/(\Psi_p)$，
$\Delta$ 是其素元。

由 (7)、$cQ=-Q$，原点必为 $R^+X$ 中的元素。
再用 $N_\Gamma Q=0$，得到唯一的
$f\in\mathcal O^+$（取次数小于 $g$ 的代表）满足
$$
 Q=\Delta f(\Delta)X,\qquad
 a=1+2v_\Delta(f),\qquad
 \lambda_Q:=f(0)\bmod p.
\tag{9}
$$
所以 $a=1$ 当且仅当 $\lambda_Q\ne0$。
任取真实格中的 $\Delta$-除点 $Z$，即 $\Delta Z=Q$，
都有
$$
                  NZ\bmod pB_0=\lambda_QP_-\bmod pB_0.
\tag{10}
$$
因为一个除点为 $f(\Delta)X$，其范数为 $f(0)P_-$；
两个除点之差属于 $B_0$，范数只改变一个 $pB_0$ 元素。
更换 $\Psi_p$ 模代表也只改变 $f(0)$ 的 $p$ 倍。
$\lambda_Q$ 相对于固定的 $\tau$ 定义；更换生成元乘以
一个非零平方单位，不改变非零性。

## 3. 可以支付的辅助观测素数

定义 $\mathcal Q(F,p,\ell)$ 为满足以下条件的有理素数 $q$：

- $q$ 避开 $p,\ell,389,\operatorname{disc}F$ 及已有固定坏位；
- $q$ 在 $F$ 惰性，Frobenius 在 $E[p]$ 上共轭于复共轭，
  即有特征值 $1,-1$；特别 $a_q\equiv q+1\equiv0\pmod p$；
- $P_-$ 在 $E(\mathbb F_{q^2})/pE(\mathbb F_{q^2})$ 的像非零。

该素数族非空，事实上有正 Dirichlet 密度。
$P_-$ 的通常 Kummer 类是非零负号类；R144 §4.1
的已证明 Chebotarev 引理可对这一类使用。
其证明在满剩余像中用中心元及 Sah 引理保证限制单射，
在表示核上避开一个比例至多 $1/p$ 的零集，再取反射
Frobenius。还可同时要求任意至多三个额外非零本征类
具有非零局部值，并提高辅助精度。这里仅需一个或两个类。

$q$ 自动在 $L/F$ 分裂：它在二面体
$\operatorname{Gal}(L/\mathbb Q)$ 中为反射，
其平方为一。故在 $F$ 的唯一 $q$ 位上，$L$ 有完整的
$p$ 个完成。原证明所需域交也真实成立：$L/F$ 在
$\ell$ 分歧，而 $E[p]$ 和固定点的 Kummer 域在该好位
不分歧。没有另加一个未证的“$q$ 同时分裂”密度假设。

选其中一个由 $c$ 固定的素位 $\mathfrak q_0$。
所有反射在奇阶二面体群内共轭，故总可如此选择和标号。
其剩余域为 $k=\mathbb F_{q^2}$，且 $c$ 在其上是
$q$ 次 Frobenius $\varphi$。置
$$
 W=E(k)/pE(k),\qquad
 W=W^+\oplus W^-,\qquad
 \pi_\pm=(1\pm\varphi)/2.
$$
两个本征空间各为一维；记 $\rho_-=\operatorname{red}(P_-)\in W^-$，
其非零性由观测条件保证。

### 3.1 保留全部完成的两条线性矩

对原点 $Q$ 定义
$$
 \begin{aligned}
 M_1^+(Q;q)
   &=\sum_{j=0}^{p-1}j\,
       \pi_+\operatorname{red}_{\mathfrak q_0}(\tau^{-j}Q)
          \in W^+,\\
 M_2^-(Q;q)
   &=\sum_{j=0}^{p-1}\binom j2\,
       \pi_-\operatorname{red}_{\mathfrak q_0}(\tau^{-j}Q)
          \in W^-.
 \end{aligned}
\tag{11}
$$
这些是原完整 $Q$ 在全部 $p$ 个完成的值；不是某个
非平凡角色的单标签，也没有把某一完成替代完整环类迹。

定义等变局部映射
$$
 \Phi_q:B\longrightarrow \bar R\otimes_{\mathbb F_p}W,\qquad
 \Phi_q(Y)=\sum_{j=0}^{p-1}
       \operatorname{red}_{\mathfrak q_0}(\tau^{-j}Y)\tau^j,
 \qquad
 \bar R=\mathbb F_p[\Gamma]=\mathbb F_p[T]/(T^p).
\tag{12}
$$
它对 $B$ 的 $\mathbb Z_p$ 完备格也有定义。
其增广是 $\operatorname{red}(NY)$，复共轭满足
$\Phi_q(cY)=\varphi(\Phi_q(Y)^*)$。
(11) 正是
$$
 M_1^+=[T]\pi_+\Phi_q(Q),\qquad
 M_2^-=[T^2]\pi_-\Phi_q(Q).
\tag{13}
$$
所有二分母均为单位。

由于 $NQ=0$，两个投影的常数项均为零。
由 $cQ=-Q$，负投影在 $*$ 下对称，正投影反对称。
$T^*=-T/(1+T)$，所以负投影的 $T$ 系数也为零。
由此可直接核出 (11) 对标签的循环平移不变；
更换 $\tau$ 只分别乘一个一次、二次非零单位。
原 Heegner 点为满足 $cQ=-\tau^jQ$ 的未平移代表时，
将其平移到上述规范也不改变两个非零测试。

## 4. 三种真实全局指数的完整比较

### 4.1 $a\ge2$：所有观测两矩都为零

此时 $Q=\Delta Y$，其中 $Y\in A_0$，且 $cY=-Y$。
$\Phi_q(Y)$ 的增广为零。
负投影又在 $*$ 下对称，故属于 $T^2\bar R\otimes W^-$；
正投影至少属于 $T\bar R\otimes W^+$。
用 $\Delta=T^2/(1+T)$ 得
$$
 \pi_-\Phi_q(Q)\in T^4\bar R\otimes W^-,
 \qquad
 \pi_+\Phi_q(Q)\in T^3\bar R\otimes W^+.
$$
因此两矩均零。这一步对每个合法观测 $q$ 都成立，
不依赖 regular 分支或局部单位猜测。

### 4.2 $a=1$：负秩一支付整个 regular 格的观测成本

使用 (6)--(9)。
将 $\pi_-\Phi_q(X)$ 写成 $u_q(T)\rho_-$。
它的增广为一，因为 $NX=P_-$。局部环
$\bar R=\mathbb F_p[T]/(T^p)$ 中，增广非零准确等价于单位。
所以
$$
                    u_q(T)\in\bar R^\times.
\tag{14}
$$
特别，原 $RX/pRX$ 向全部完成的负投影是同一个
$\bar R$ 自由秩一模的同构，不存在额外饱和指数。
$B_0^+$ 在这个负投影中为零。

由 (9)，
$$
 \pi_-\Phi_q(Q)=\Delta f(\Delta)u_q(T)\rho_-.
$$
其 $T^2$ 系数准确为 $f(0)\rho_-$，因此
$$
       M_1^+(Q;q)=0,\qquad
       \boxed{\ M_2^-(Q;q)=\lambda_Q\rho_-\ne0.\ }
\tag{15}
$$
这里每个 $q\in\mathcal Q$ 都有效。
没有要求 $P_-$ 在 $p$ 处的形式对数为单位，也没有把
原始全局格的局部像指数默认为一。所需单位已由 (14)
以及可支付的辅助定位严格取得。

### 4.3 $a=0$：原点 Kummer 类和负线同时定位

此时 $\kappa_{\delta,A}(Q)$ 是非零的通常 Selmer 类。
R146 的真实 $A[\delta]\simeq E[p]$ 比较使它为正号类；
$P_-$ 的 Kummer 类为非零负号类。
对这两个指定类同时使用 R144 §4.1，可选择
$q\in\mathcal Q$ 使二者的局部值均非零。
这给一个 Chebotarev 正密度子族；阈值允许依赖原 $p,L,Q$，
本篇没有声称一个关于 $q$ 的多项式上界。

为核定第一矩与原 Kummer 类的关系，在分裂局部积上
取 $Y$ 使 $\delta Y=Q$；此点存在，因为循环差分把
整个局部积满射到其范数零子群。取 $pV=NY$，
则 $Y-\operatorname{diag}V$ 是 $A$ 中的 $\delta$-除点，
其 Kummer 误差为 $-\operatorname{diag}(\sigma V-V)$。
所以原局部类准确对应 $-\kappa_E(NY)$。

另一方面，$\delta=T+O(T^2)$，故
$$
        [T]\Phi_q(Q)=\operatorname{red}(NY).
$$
正号局部类非零因而准确给
$$
                         M_1^+(Q;q)\ne0.
\tag{16}
$$
这使用的是原 $Q$ 的实际 Kummer 类，无需造一个
替代点。结合 §§4.1--4.3 即证明 (2)。

## 5. 对原 Kolyvagin 族可作、不可作的比较

R156 的每个节点仍满足
$$
 \overline c_n^A=-t_0a_\ell\,\overline c_n^{E,\mathrm{raw}},
 \qquad c_1^A=\kappa_A((\tau-1)Q),
 \qquad
 \operatorname{length}_{\mathcal O}\Sha(A/F)[p^\infty]=2(a+1).
\tag{17}
$$
本篇 $\kappa_{\delta,A}(Q)$ 与 (17) 的原首项相差的
增广因子仍然存在。尤其模 $\delta$ 后原首项为零；
不能将 (16) 直接代入原首项的有限--奇异关系，并声称
已经构造出非零的原 $c_q^A$。

若某构造真能保留相同通常局部条件及原首项 $Q$，
同时把完整族合法地除去一层，那么 Howard 的指数界
会给 $\operatorname{length}\Sha(A/F)[p^\infty]\le2a$，
与 (17) 矛盾。因此 R230 的负秩一输入不会自动提供
这种完整族除法。它实际提供的是 (5)--(10) 的整格、
真实范数坐标，以及 (14)--(16) 的无损观测。

这里的 $q$ 首先只是观测位，不是重新选择原 $\ell$。
若随后将它用作原 Kolyvagin 节点标签，节点使用的将是
完整 $P[\ell q]$ 及原辅助导数；其范数、局部条件、精度与
高度仍须逐项支付。不得把观测两矩的非零性直接等同于
原单辅助节点的非零性。

结合 R146、R230，(2) 中任何非零两矩仍推出
$\operatorname{rank}E(\mathbb Q)=2$ 及
$\Sha(E/\mathbb Q)[p^\infty]=0$。
但本篇未证明无穷多个原输入 $p$ 有这样的非零两矩，
故没有将该等价观测门登记为主问题完成。


### 5.1 已付款的原节点 $\delta^3$ 局部比较

将观测族缩小到
$$
                    a_q\equiv q+1\equiv0\pmod{p^5}.
\tag{18}
$$
R144 §4.1 允许这一提高而保留全部指定剩余定位条件；
$5=2\cdot3-1$ 是其精度 $k=3$ 所需的一个安全辅助精度。
这里不以较低精度的数值零直接代替高精度输入。

在 $q$ 处的分裂局部积中，$A$ 的点格是增广理想
$I$ 与 $E(F_q)$ 的张量。其 $p$ 初级有限部分的两个
$\mathcal O$ 循环块长度至少为 $p-1\ge6$，由 (18) 实际
还可取更长。模 $p$ 后正是 $I\otimes W$；
$pA\subset\delta^2A$，所以这一约化准确检测
$A(F_q)/\delta^2 A(F_q)$。

对 $cQ=-Q$，写 $h_\pm(T)=\pi_\pm\Phi_q(Q)$。
前文已有 $h_-(0)=h_-'(0)=0$。反对称关系
$h_+(T^*)=-h_+(T)$ 还给
$$
                  [T^2]h_+=-\tfrac12[T]h_+.
$$
故两矩同时为零，当且仅当 $\Phi_q(Q)\in I^3\otimes W$，
也就是 $Q\in\delta^2A(F_q)$。
局部循环块长度至少为六，保证乘 $\delta$ 给出的
$$
 A(F_q)/\delta^2A(F_q)
       \longrightarrow A(F_q)/\delta^3A(F_q)
$$
是单射。注意该结论使用了实际局部块长度；
没有在任意有限模上无条件声称乘 $\delta$ 单射。

原首项 $(\tau-1)Q$ 与 $\delta Q$ 相差局部整单位。
现在使用 R144 的**同一原族**有限--奇异关系，其实际算子
$-q\varphi_q^{-1}\otimes1$ 是保 $\delta$ 深度的整同构。
因此
$$
 \boxed{\quad
 (M_1^+,M_2^-)\ne(0,0)
 \Longleftrightarrow
 \operatorname{loc}_q(c_1^{(3)})\ne0
 \Longleftrightarrow
 \operatorname{loc}_q(c_q^{(3)})\ne0.
 \quad}
\tag{19}
$$
这里上标 $(3)$ 明确表示 $\delta^3$ 精度。
$a=0$ 的非零可在 $\delta^2$ 精度出现；
$a=1$ 的第二矩一般需要 $\delta^3$，不能统一少付一层。

(19) 不说 $\operatorname{loc}_q(\overline c_q)\ne0$。
事实上原 $c_1$ 在模 $\delta$ 时为零，原边关系恰给
$$
                       \operatorname{loc}_q(\overline c_q)=0.
\tag{20}
$$
全局的 $\overline c_q$ 仍可能非零；(20) 是它自身辅助位
的局部消失，而非全局消失。

### 5.2 由同一个真 core 节点取得原 $\overline c_q$ 非零

另外固定一个非挠 $P_+\in E(\mathbb Q)$，例如 R2 的
$(0,0)$，再删去它在有理点格中的固定除法指数的素因子。
在观测族中增加
$$
       \operatorname{red}_q(P_+)\ne0
       \quad\text{于 }E(\mathbb F_{q^2})/pE(\mathbb F_{q^2})\text{ 的正线}.
\tag{21}
$$
R144 的引理同时支付 (18)、(21) 及 $P_-$ 的负线非零。
$a=0$ 分支还需的 $\kappa_{\delta,A}(Q)$ 非零定位至多
再加一个类，总数三仍在该引理范围内。因此 (2) 对这个
加强观测族仍成立。

令 $\mathcal S=\operatorname{Sel}_\delta(A/F)$，通过原
局部条件比较识别为 $\operatorname{Sel}_p(E/F)$。
(21) 与负线条件使
$$
                 \operatorname{loc}_q\mathcal S=H_f^1(F_q,E[p])
\tag{22}
$$
满射；右侧正负两线各一维。
把 $q$ 处条件改为原 transverse 条件，得到的真实
$\mathcal S(q)$ 准确等于 $q$ 处 strict Selmer 群。
确实，任意 relaxed 类与 $\mathcal S$ 的全局 Tate 配对
在其他位均为零，所以它在 $q$ 的局部像位于 (22) 的正交补；
该补就是 $H_f^1$ 本身。再与互补的 transverse 子空间相交，
局部值只能为零。反向包含直接成立。因此
$$
                 \dim\mathcal S(q)^+=s_+-1,\qquad
                 \dim\mathcal S(q)^-=0.
\tag{23}
$$
这不是凭维数猜测删除负方向，而是同一自对偶局部条件的
strict、relaxed 和 transverse 比较。

若这个同一 $q$ 的两矩非零，(2) 给 $a\le1$，
R146 于是给 $r=2$、$\Sha(E/\mathbb Q)[p^\infty]=0$，
所以 $s_+=2$。由 (23)，$q$ 是原族的真 core 节点。
R144 的已证原始弱刚性在每个 core 节点给一个生成元，
再经 R156 的逐节点单位比较，得到
$$
 \boxed{\quad
 (M_1^+(Q;q),M_2^-(Q;q))\ne(0,0)
 \ \Longrightarrow\
 \overline c_q^A\ne0
 \ \Longrightarrow\
 \overline c_q^{E,\mathrm{raw}}\ne0.
 \quad}
\tag{24}
$$
这里是**同一个**辅助素数、同一个完整原 Heegner 节点；
没有用从 Mordell--Weil 格任造的候选上同调类替代它。

(24) 通过真 core 的全局原始性，而不通过把 (20) 改成非零。
反向从原 $\overline c_q$ 非零虽可经 R230 的 $\nu$ 公式
取得 $r=2$、原 Sha 的 $p$ 初级部分为零，但不控制指定
$Q$ 的指数 $a$，所以没有补写该反向箭头。

## 6. 依赖与用途

- [R230](R230-original-sixteen-negative-twists-rank-one.md)：
  原十六负扭曲的已证秩一、Sha 有限及统一有限例外。
- [R146 完整证明](../notes/2026-11-12-noncm-two-step-criterion-with-varying-heegner-field.md)：
  各位的真实 $H^1$ 消失、通常 Kummer 条件及共轭符号。
- [R144 完整证明 §4.1](../notes/2026-11-12-noncm-primitive-induced-system-and-exact-length.md)：
  同时指定有限个剩余本征类的高精度 Chebotarev 选择；
  该节已给所需独立证明。
- [R156](R156-fixed-field-primitive-system-and-exact-index.md)：
  相同完整类群族、相同首项和准确长度等式。
- [R225](R225-original-heegner-cyclic-energy-full-depth-and-gram-certificate.md)：
  原 $p$ 处形式对数、全 Gram 与能量的有限证书。
  本篇改用可选择的真实辅助位，通过固定负点定位支付
  regular 格的比较，因此 (2) 是全局 $a\le1$ 的等价门；
  未将不同观测位的矩数值彼此等同。
