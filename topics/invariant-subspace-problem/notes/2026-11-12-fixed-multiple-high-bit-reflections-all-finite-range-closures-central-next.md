# 固定多位高反射的真实幂像逼近：规范危险核包含于全部有限次闭像

日期：2026-11-12（UTC）。独占作者：central_next。
状态：下文给完整实际有限头、全域及范数证明；均为已证明的实际中间结论。
结论只针对规范行的正平方根分支，不预设该核非零，不声称 ISP 完成。

## 1. 结论及范围

沿用实际 Haar 算子，置
$$
 a_j=\frac{(-1)^j}{j+1},\qquad
 X=\sum_{j\ge0}a_jV_j,\qquad
 B=\sum_{j\ge0}a_j^2(I-V_j^2),\qquad
 Y=(I-B)^{1/2},\qquad T=X-Y.
\tag{1.1}
$$
常数项为 `a_*=0`，平方根在零点取字符 `+1` 的全纯支。
设 `M=ker T`，所有幂使用真实自然迭代域。

**定理。** 对每个固定整数 `r≥1`，
$$
 \boxed{M\subseteq\overline{\operatorname{Ran}T^r}.}
\tag{1.2}
$$
因此规范危险核的
$$
 N_r=M\cap\overline{\operatorname{Ran}T^r}
$$
全部等于 `M`，特别 `N₂=M`。不需要先假设旧中央算子单射。

更准确地，令
$$
 F_m=\{m,m+1,\ldots,m+r-1\},\qquad
 J_{F_m}=\prod_{j\in F_m}M_{\chi_j},\qquad
 p_m=\prod_{j\in F_m}a_j.
\tag{1.3}
$$
对每个 `f∈M`，都有 `J_(F_m)f∈Dom T^r`；对充分大 `m`，
$$
 \boxed{
 w_m(f)=\frac{T^rJ_{F_m}f}{(-2)^r r!p_m}
 \in\operatorname{Ran}T^r,\qquad
 w_m(f)\rightharpoonup f.
 }
\tag{1.4}
$$
归一化后的输出一致有界；输入范数可按 `m^r` 增长。
这里不是有界右逆、范数收敛，也不是无穷次实际像的共同原像。

本稿使用有限多位反射构造原算子的像向量，不借换头改变 R246 的中心差或活动根。

## 2. 实际符号翻转与其相对进位

记
$$
 N_j=A^{2^j}/d_j,\qquad
 N_j=E_j+\eta_jE_j^*N_{j+1},\qquad
 N_j^2=\eta_jN_{j+1},
$$
$$
 \|N_j\|\le1,\qquad
 \eta_j\le\bar\eta_j:=e^{-770\,16^j},\qquad
 V(z)=(I-z)(I+z)^{-1},\quad V_j=V(N_j).
\tag{2.1}
$$
令 `ell=m+r−1`，`J=J_(F_m)`，`γ(Q)=JQJ`，并置
`s_k=−1` 当 `k∈F_m`、否则 `s_k=1`。

以下实际估计是关键：
$$
 \|\gamma(N_k)-s_kN_k\|\le
 \begin{cases}
 2\alpha_m/\alpha_k,&k<m,\\
 2\eta_k,&m\le k<\ell,\\
 0,&k\ge\ell.
 \end{cases}
\tag{2.2}
$$
末行在 `k=ell` 使用 `s_k=−1`，在更高位使用 `s_k=1`。

证明第一行：低头有限链恒等式给
$$
 N_k=N_k^{[m]}+\frac{\alpha_m}{\alpha_k}
 E_k^*\cdots E_{m-1}^*N_m.
$$
反射固定整个低头，故差只发生在最后的 `N_m`，范数至多 `2`。
第二行来自
$$
 \gamma(N_k)+N_k
 =\eta_kE_k^*\bigl(N_{k+1}-\gamma(N_{k+1})\bigr).
$$
最高选中位上没有更高反射，故 `γ(N_ell)=−N_ell` 精确成立；
更高算子则完全不受反射影响。

`I−N_k` 的逆也有统一界：
$$
 (I-N_k)^{-1}=(I+N_k)(I-N_k^2)^{-1},\qquad
 \|(I-N_k)^{-1}\|\le\frac2{1-\eta_k}<3.
\tag{2.3}
$$
因此 `V(s_kN_k)`、`γ(V_k)` 范数均不超过 `6`。
实际逆差公式使 (2.2) 的各非零右端分别乘上 `18` 即控制
`||γ(V_k)−V(s_kN_k)||`。

定义原范数代数内的替代算子
$$
 \widehat X_m
 =X+\sum_{j\in F_m}a_j\bigl(V(-N_j)-V(N_j)\bigr),
$$
$$
 \widehat B_m
 =B+\sum_{j\in F_m}a_j^2
 \bigl(V(N_j)^2-V(-N_j)^2\bigr),\qquad
 \widehat Y_m=(I-\widehat B_m)^{1/2},
\tag{2.4}
$$
$$
 A_m=(\widehat X_m-\widehat Y_m)-T.
\tag{2.5}
$$
`A_m` 是有界的 `Acal` 元素，与 `T` 完整域交换。
`widehat X_m` 只对原 `X` 作有限有界扰动，未改变其常数项或闭实现。
`widehat B_m` 字符为零，平方根取同一个 `+1` 支。

## 3. 统一全纯轮廓与两个误差的精确尺度

固定一个圆 `Gamma={|z|=rho}`，`0<rho<1`，并令
$$
 R_\Gamma=\max_{\Gamma}\|(z-B)^{-1}\|,\qquad
 C_\Gamma=2\rho\max_{\Gamma}|\sqrt{1-z}|\,R_\Gamma^2.
\tag{3.1}
$$
这些都是固定实际算子的有限常数，与 `m` 无关。

直接有
$$
 V(-N)-V(N)=4N(I-N^2)^{-1},
\tag{3.2}
$$
$$
 V(-N)^2-V(N)^2
 =8N(I+N^2)(I-N^2)^{-2}.
\tag{3.3}
$$
所以
$$
 \|\widehat B_m-B\|\le32\sum_{j\in F_m}|a_j|^2
 \le\frac{32r}{(m+1)^2}.
\tag{3.4}
$$
充分大 `m` 时，真实 Neumann 逆差公式给
`max_Gamma||(z−widehat B_m)⁻¹||≤2R_Gamma`。
而 `γ(B)` 与 `B` 酉等价，轮廓上的预解式范数恰为 `R_Gamma`。
两次全纯逆差积分由此给
$$
 \|\widehat Y_m-Y\|\le C_\Gamma\|\widehat B_m-B\|,
 \qquad
 \|\gamma(Y)-\widehat Y_m\|
 \le C_\Gamma\|\gamma(B)-\widehat B_m\|.
\tag{3.5}
$$
没有把平方根 Taylor 级数无证地用到算子范数半径。

置
$$
 E_m=\gamma(T)-(\widehat X_m-\widehat Y_m),
 \qquad \Delta_m=A_m+E_m=\gamma(T)-T.
\tag{3.6}
$$
`E_m` 是全空间有界算子。由 (2.2)，以及
$$
 \sum_{k<m}|a_k|\frac{\alpha_m}{\alpha_k}
 \le\frac{\|a\|_2\eta_{m-1}}{\sqrt{1-\eta_*^2}}
 <2\bar\eta_{m-1},
$$
$$
 \sum_{k<m}|a_k|^2\frac{\alpha_m}{\alpha_k}
 \le2\bar\eta_{m-1},
$$
得到
$$
 \|\gamma(X)-\widehat X_m\|
 \le36(r+2)\bar\eta_{m-1},
$$
$$
 \|\gamma(B)-\widehat B_m\|
 \le432(r+2)\bar\eta_{m-1}.
$$
故
$$
 \boxed{\|E_m\|\le C_r\bar\eta_{m-1},\qquad
 C_r=(r+2)(36+432C_\Gamma).}
\tag{3.7}
$$

另一方面，令
$$
 P_m=4\sum_{j\in F_m}a_jN_j.
\tag{3.8}
$$
由 (3.2)、(3.5)，
$$
 \|A_m-P_m\|
 \le\frac{6r\bar\eta_m}{m+1}
       +\frac{32C_\Gamma r}{(m+1)^2}
 \le\frac{c_r}{(m+1)^2},
 \qquad c_r=(6+32C_\Gamma)r,
\tag{3.9}
$$
并且
$$
 \|P_m\|\le\frac{4r}{m+1},\qquad
 \|A_m\|\le\frac{4r+c_r}{m+1}.
\tag{3.10}
$$
`bar eta_m≤1/(m+1)` 在这里是充分宽松的实际指数界。

## 4. 完整域：进位误差确实与同一闭尾 first 交换

这一步不能只由“与全部有界高位生成元交换”代替。

设
$$
 \mathcal D=\operatorname{Dom}T=\operatorname{Dom}X,\qquad
 X_{>\ell}=X-\sum_{k=0}^{\ell}a_kV_k.
\tag{4.1}
$$
尾 first 与 `X` 相差有界算子，故其完整域仍为 `D`。
每个选中反射 `J_j` 保持该域，因而 `J` 也保持。
`J` 只作用于前 `ell+1` 位，`X_(>ell)` 仅作用更高位；
先在有限柱核心上交换，再用 `J` 的域保持和闭图逼近，得到
$$
 JX_{>\ell}=X_{>\ell}J\quad\hbox{在 }\mathcal D.
\tag{4.2}
$$

每个 `Acal` 元素均完整保持 `D` 并与 `X` 交换；
又与有界有限头和交换，因此也与 `X_(>ell)` 完整域交换。
特别，以下各算子都保持 `D` 并与同一个 `X_(>ell)` 交换：
$$
 V_k,\quad V(s_kN_k),\quad
 JV_kJ,\quad Y,\quad\widehat Y_m,\quad JYJ.
\tag{4.3}
$$
对被 `J` 共轭的项，是将 (4.2) 与原 `Acal` 域交换相继使用。

`γ(X)−widehat X_m` 只有 `k≤ell` 的有限和；
`γ(Y)−widehat Y_m` 也是 (4.3) 中两项之差。
所以由其**具体构造**可得
$$
 E_m\mathcal D\subseteq\mathcal D,\qquad
 E_mX_{>\ell}=X_{>\ell}E_m\quad\hbox{于 }\mathcal D.
\tag{4.4}
$$

置真正有界的有限头差
$$
 D_m^{\rm bd}=\sum_{k=0}^{\ell}a_kV_k-Y,\qquad
 d_m=2\|D_m^{\rm bd}\|.
\tag{4.5}
$$
`D_m^bd` 也在 `Acal` 中并与 `X_(>ell)` 域交换。
因此
$$
 [T,E_m]=[D_m^{\rm bd},E_m]\quad\hbox{于 }\mathcal D.
$$
归纳给全部固定阶的**真实域恒等式**
$$
 \delta_T^q(E_m)
 =\operatorname{ad}_{D_m^{\rm bd}}^q(E_m),\qquad
 \|\delta_T^q(E_m)\|\le d_m^q\|E_m\|.
\tag{4.6}
$$
右侧每一项都保持 `D`；归纳时只用保持 `D` 且与 `X_(>ell)` 域交换的
有界算子的和、积及交换子。因此没有在下一阶丢失域条件。

规范系数给明确增长
$$
 d_m\le12(1+\log(m+r))+2\|Y\|.
\tag{4.7}
$$
同时 `delta_T(A_m)=0`，而 `A_m` 保持全部所需自然域。

## 5. 一个带可核误差的幂展开引理

以下只使用本节已经支付的有界域算子。
若 `v∈D` 且
$$
 Tv=-(A+E)v,
\tag{5.1}
$$
其中 `A` 完整交换 `T`，`E` 及全部所需 `delta_T^q E` 保持 `D`，
则定义
$$
 Q_0=I,\qquad Q_{n+1}=\delta_T(Q_n)-Q_n(A+E).
\tag{5.2}
$$
每个 `Q_n` 都是有界域保持算子，且递归证明
$$
 v\in\operatorname{Dom}T^n,\qquad T^nv=Q_nv.
\tag{5.3}
$$
确实 `TQ_nv=Q_nTv+delta_T(Q_n)v`；这同时证明下一次入域和公式。

若 `||E||≤epsilon≤1`，`||delta_T^q E||≤d^q epsilon`，
则
$$
 \boxed{
 \|Q_n-(-A)^n\|
 \le(n+1)!\,\epsilon(1+\|A\|+d)^n.
 }
\tag{5.4}
$$
自含计数如下：将 `A` 赋权 1，`delta_T^qE` 赋权 `q+1`。
`Q_n` 每个单项式总权为 `n`、长度至多 `n`。
求导最多产生 `n` 项，右乘 `A+E` 产生两项；
系数绝对值总和从 1 递推，至多为 `(n+1)!`。
唯一不含 `E` 或其导数的单项式是 `(−A)^n`。
其余每项至少含一个 `epsilon` 因子；其它 `epsilon` 可用 1 控制，
而各阶导数和 `A` 的乘积至多再付 `(1+||A||+d)^n`。这证明 (5.4)。

现在取 `v=Jf`、`f∈M`。因为
`gamma(T)Jf=JTf=0`，(3.6) 给
`Tv=−(A_m+E_m)v`。第 4 节已支付引理的全部域假设，故
$$
 Jf\in\operatorname{Dom}T^r,
$$
$$
 \boxed{
 \|T^rJf-(-A_m)^rJf\|
 \le(r+1)!\,C_r\bar\eta_{m-1}
 (1+\|A_m\|+d_m)^r\|f\|.
 }
\tag{5.5}
$$
对充分大 `m`，`C_r bar eta_(m−1)<1`，满足引理的 `epsilon≤1`。

## 6. 固定 r 个不同位留下唯一主项

不能将 (3.9) 的二阶误差直接乘 `m^r`。
要同时使用主项本身的 `O_r(m⁻¹)` 范数。
有限乘积差公式与 (3.9)—(3.10) 给
$$
 \|A_m^r-P_m^r\|
 \le r\max(\|A_m\|,\|P_m\|)^{r-1}\|A_m-P_m\|
 =O_r((m+1)^{-r-1}).
\tag{6.1}
$$

所有 `N_j` 交换。展开 `P_m^r`，指标全不相同时恰好有 `r!` 个排列；
任何其它项都含某个 `N_j²`，因而由实际进位 (2.1) 多出 `bar eta_m`。
所以
$$
 P_m^r
 =4^r r!p_m\prod_{j\in F_m}N_j+R_m,
$$
$$
 \|R_m\|
 \le4^r\bar\eta_m
 \left(\sum_{j\in F_m}|a_j|\right)^r
 \le4^r\bar\eta_m\left(\frac r{m+1}\right)^r.
\tag{6.2}
$$
这里使用真实 `N_j²=η_jN_(j+1)`，没有用纯幂零替代实际算子。

此外
$$
 |p_m|=\prod_{j=m}^{m+r-1}(j+1)^{-1}
 \ge(m+r)^{-r}.
\tag{6.3}
$$
由 (4.7)、(5.5)，将 (5.5) 除以 `4^r r!|p_m|` 后，其误差至多固定常数乘
$$
 (m+r)^r(1+\log(m+r))^r\bar\eta_{m-1}\longrightarrow0.
\tag{6.4}
$$
(6.1) 的归一化误差是 `O_r(m⁻¹)`；(6.2) 的归一化余项也趋零。
于是对每个固定 `f∈M`，
$$
 \boxed{
 \left\|
 \frac{T^rJ_{F_m}f}{(-4)^r r!p_m}
 -\left(\prod_{j\in F_m}N_j\right)J_{F_m}f
 \right\|\longrightarrow0.
 }
\tag{6.5}
$$

## 7. 真正的高位弱极限与闭像结论

在物理位上 `E_j=e_10`，`J_j=diag(1,−1)`，所以
$$
 E_jJ_j=E_j.
\tag{7.1}
$$
不同位相互交换；且
$$
 \left\|\left(\prod_{j\in F_m}N_j\right)J_{F_m}
             -\prod_{j\in F_m}E_j\right\|
 \le\sum_{j\in F_m}\eta_j\le r\bar\eta_m.
\tag{7.2}
$$
对任意固定两个有限柱测试向量，充分高位都处于 Haar 参考因子
`Omega_+=(e_0+e_1)/sqrt2`，每个 `E_j` 的矩阵元因子为 `1/2`。
有限柱稠密、算子范数至多 1，故
$$
 \prod_{j\in F_m}E_j
 \xrightarrow{\rm WOT}2^{-r}I.
\tag{7.3}
$$
结合 (6.5)—(7.3)，
$$
 \frac{T^rJ_{F_m}f}{(-4)^r r!p_m}
 \rightharpoonup2^{-r}f.
$$
等价地就是 (1.4)。

每一项都是真实自然幂 `T^r` 的像，而
`closure Ran T^r` 是闭线性空间，因而弱闭。
所以 `f∈closure Ran T^r`。这完成定理，不需要任何未知子空间的 UHF 运输。

## 8. 无需中央单射的零阶逆域及全部广义核识别

恢复 R233/R236 的旧中央设置
$$
 K=(M\oplus CM)^\perp,\qquad S=T_K,
$$
$$
 T=\begin{pmatrix}0&F&D\\0&S&H_1\\0&0&0\end{pmatrix},\qquad
 \operatorname{Dom}T=M\oplus\operatorname{Dom}S\oplus CM.
\tag{8.1}
$$
本节先**不假设** `S` 单射。

### 8.1 全部广义核都没有末块分量

对 `h∈ker T^r` 和 `f∈M`，(1.2) 允许用 `T^r u_n` 范数逼近 `f`。
对自然幂逐次使用 `T` 的完整 `C` 自伴关系，得到
$$
 \mathcal B(f,h)
 =\lim_n\mathcal B(T^ru_n,h)
 =\lim_n\mathcal B(u_n,T^rh)=0.
$$
所以
$$
 \ker T^r\subseteq(CM)^\perp=M\oplus K
 \qquad(r\ge1).
\tag{8.2}
$$
这里不需要先把自然幂的通常伴随与伴随幂等同。

在 `M⊕K` 上，直接逐幂归纳得完整自然域和取值
$$
 \operatorname{Dom}T^r\cap(M\oplus K)
 =M\oplus\operatorname{Dom}S^r,
$$
$$
 T^r(m,k,0)=(FS^{r-1}k,S^rk,0).
\tag{8.3}
$$
又
$$
 \ker S\cap\ker F=\{0\},
\tag{8.4}
$$
因为这两个块同时为零就使 `(0,k,0)∈ker T=M`。
由 (8.2)—(8.4)，
$$
 \boxed{\ker T^r=M\oplus\ker S^{r-1}\qquad(r\ge1),}
\tag{8.5}
$$
其中 `ker S⁰=ker I={0}`。反向包含的域也已支付：
若 `S^(r−1)k=0`，则该零向量在 `Dom S` 中，因此 `k∈Dom S^r`。

### 8.2 Bell 镜像源完全避开中央实际值域

仍仅作为集合定义
$$
 D_H=\{c\in CM:H_1c\in\operatorname{Ran}S\}.
$$
若 `Sk+H₁c=0`，则 `g=(0,k,c)∈Dom T`，且 `Tg∈M`。
因此 `g∈ker T²`，(8.2) 迫 `c=0`。于是
$$
 \boxed{D_H=\{0\},\qquad
 H_1(CM)\cap\operatorname{Ran}S=\{0\}.}
\tag{8.6}
$$
取 `k=0` 又得 `H₁` 单射。由已付清的镜像关系
`H₁=C_KF*C|_(CM)`，
$$
 \boxed{\ker H_1=0,\qquad\overline{\operatorname{Ran}F}=M.}
\tag{8.7}
$$
这几项**均不需要中央单射**。它们是实际零阶逆值域的排斥结论，
不是由正幂光滑推出入域。

若 `S` 非单射，不能把 `S⁻¹H₁` 叫作单值零算子；
相应逆关系的准确全图是
$$
 \boxed{\{(c,k):Sk=H_1c\}=\{0\}\times\ker S.}
\tag{8.8}
$$

### 8.3 中央耦合关系的整个闭包

把可能多值的中央关系写成
$$
 \mathcal G=\{(Sk,Fk):k\in\operatorname{Dom}S\}
 \subset K\oplus M.
\tag{8.9}
$$
由 (8.6)、镜像关系及 `S*=C_KSC_K`，
$$
 F^*m\in\operatorname{Ran}S^*\quad\Longrightarrow\quad m=0.
\tag{8.10}
$$
若 `(u,m)⊥G`，则通常伴随定义给
`u∈Dom S*`、`S*u=−F*m`；(8.10) 迫 `m=0`、`u∈ker S*`。
反向也成立。因此双重正交补给
$$
 \boxed{
 \overline{\mathcal G}
 =\overline{\operatorname{Ran}S}\oplus M.
 }
\tag{8.11}
$$
特别对任意 `m∈M`，均存在 `k_n∈Dom S` 使
`Sk_n→0`、`Fk_n→m`。不声称这些原像 `k_n` 有界。

### 8.4 实际像中的根链与单射特例

(8.5)、(8.3) 还直接给
$$
 \boxed{
 M\cap\operatorname{Ran}T^r
 =F\bigl(S^{r-1}\ker S^r\bigr)\qquad(r\ge1).
 }
\tag{8.12}
$$
证明：若 `T^r u∈M`，则 `u∈ker T^(r+1)`，可用 (8.5) 写成
`u=(m,k,0)`、`k∈ker S^r`，再用 (8.3)。
反向对这样的 `k` 直接代入。因 (8.4)，`F` 在 `ker S` 上单射。

若额外假设 `ker S=0`，才可把 `FS⁻¹` 当作单值算子，并进一步得到
$$
 \boxed{\ker T^n=M\quad(n\ge1),\qquad
 M\cap\operatorname{Ran}T^r=\{0\}\quad(r\ge1),}
\tag{8.13}
$$
$$
 \boxed{
 \overline{\operatorname{Graph}(FS^{-1})}=K\oplus M,\qquad
 \operatorname{Dom}(FS^{-1})^*=\{0\}.
 }
\tag{8.14}
$$
原不可闭商的全部闭图都是多值部分；正则商 `Q` 的目标 `M/N₂` 为零。
`D_H` 确实闭，但原因是它等于零，不是所有 `CM` 都有原像。

中央仍可能有非零核；本稿没有排除 `M≠0`。
有核分支的实际原像问题已准确转移成 (8.5)、(8.12) 中的中央根链，
不再把已经证明的原 `N_r=M` 重新列作未知。

## 9. 未作的升级

本稿仅证明每个固定自然幂的闭像包含原核。
没有证明原核向量属于这些实际像，也没有统一有界原像；
没有把所有广义核 `ker T^s` 都放入全部闭像。
(1.2) 使规范行的 `N_r` 全部等于 `M`，但不凭此把中央非零核再免费判为全等向。

输入只包括 R125 的 `Acal` 完整域交换、R208 的有限反射域与真实链、
R233/R236 的中央域识别。第 4—5 节独立支付了这里需要的全部自然幂域，
并不把“与有界生成元形式交换”当作闭尾 first 的域结论。

本稿没有更改 R246 的中心差，也没有用任何边界奇异态冒充 Haar 正常向量。
