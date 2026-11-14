# R162：纯虚平方可和倾斜的全交换子线性同构与首整数阶

日期：2026-11-12。作者：l2_moments。
状态：完整证明，已由根代理与 critical_kernel 全文核读。执行器失效期间先保存完整 Git blob，恢复后纳入正式结果。

本稿把纯虚 $\ell^2$ 指数权的相对符号变换扩到全部有界交换子。
它是有界线性同构，一般不是代数同态。
特别地，本稿声称 $\mathcal T_w(\mathcal A)=\mathcal A$（集合），
不声称 $\mathcal T_w(A)=A$（生成元）。
后者通常错误，正文明确给出一致性检验。

## 1. 记号与结论

设
$$
H=L^2(\mathbb Z_2,\mu),\quad
\mathcal C=\{A\}',\quad
\mathcal A=\overline{\mathbb C[I,A]}^{\|\cdot\|},
$$
$\mathcal U$ 为已有实际模型的 UHF 代数。
记
$$
N_j=A^{2^j}/W_{2^j},\quad
E_j=e_{10}^{(j)},\quad
\|N_j-E_j\|=\eta_j,\quad \|N_j\|=\|E_j\|=1,
$$
以及纯交换子代数
$$
\mathcal E=\{E_j:j\ge0\}'.
$$
R88 给以真空1为基点的双向有界线性对应
$\mathfrak F_0:\mathcal E\to\mathcal C$，
其定义特征为
$$
\mathfrak F_0(P)1=P1.
\tag{1.1}
$$
这不是代数同态。

取
$$
w=i\sum_{j\ge0}t_j\chi_j,\qquad t_j\in\mathbb R,\quad t\in\ell^2.
\tag{1.2}
$$
纯虚常数只改变无关的整体相位，故省略。
令
$$
\Omega_w=e^w,\quad D_w=M_{\Omega_w},\quad q_j=e^{-2it_j}.
$$
$|\Omega_w|=1$ 几乎处处，$D_w$ 为酉算子，
$\{\chi_J\Omega_w\}$ 是正交归一基，且
$$
D_wE_jD_w^*=q_jE_j.
\tag{1.3}
$$

置
$$
\rho=2\sum_{j\ge0}\eta_j10^{j/2}<1,\qquad
C_+=\frac{1+\rho}{1-\rho},\quad
C_-=(1+\rho)^2,\quad
K=C_+C_-.
\tag{1.4}
$$

**定理1.1。** 存在规范有界线性双射
$$
\mathcal T_w:\mathcal C\longrightarrow\mathcal C
$$
满足
$$
\boxed{
\mathcal T_w(B)\Omega_w=(B1)\Omega_w,\qquad
\|\mathcal T_w\|,\|\mathcal T_w^{-1}\|\le K.
}
\tag{1.5}
$$
右侧是单个 $H$ 向量与单位模函数的点乘。
并且
$$
\boxed{\mathcal T_w(\mathcal A)=\mathcal A,\qquad
\chi(\mathcal T_w(B))=\chi(B)\quad(B\in\mathcal A).}
\tag{1.6}
$$
因此若 $B\in\mathcal A$ 且 $\chi(B)\ne0$，则
$$
\boxed{(B1)e^w\text{ 对 }A\text{ 循环}.}
\tag{1.7}
$$
这里 $B1$ 不要求有界、连续或属于有限 chaos。

不声称一般非单位 $B$ 的核或稠密像由 $\mathcal T_w$ 保持。
这条线性同构不会自动排除零锚的慢共振核。

## 2. 以 $\Omega_w$ 为真空的 Riesz 变换

定义
$$
S_j^w=I-2q_jE_j,\qquad G_j^w=I-2q_jN_j.
\tag{2.1}
$$
则 $\|S_j^w\|,\|G_j^w\|\le3$，
$\|G_j^w-S_j^w\|=2\eta_j$，并由 (1.3) 得
$$
S_J^w\Omega_w=\chi_J\Omega_w.
\tag{2.2}
$$
这里不同位的纯因子交换。

对 $K\subset[0,j)$，令 $Q_{j,K}$ 为 R88 的局部秩一头算子
$$
Q_{j,K}
=|1_{[0,j]}\rangle\langle\chi_{K\cup\{j\}}|\otimes I_{\rm tail},
$$
并置
$$
Q_{j,K}^w=D_wQ_{j,K}D_w^*.
\tag{2.3}
$$
虽然 $D_w$ 一般不在 $\mathcal U$，其共轭对这个局部算子只使用低 $j+1$ 位相位，
所以 $Q_{j,K}^w$ 仍是有限局部算子。
对固定 $j$，
$$
\sum_{K\subset[0,j)}(Q_{j,K}^w)^*Q_{j,K}^w\le I.
\tag{2.4}
$$
它将基向量 $\chi_{K\cup\{j\}\cup L}\Omega_w$ 送为 $\chi_L\Omega_w$，
其中 $L\subset(j,\infty)$。

定义
$$
W_w(\chi_J\Omega_w)=G_J^w\Omega_w.
$$
按位排序的望远镜展开给
$$
\boxed{
W_w-I=\sum_{j\ge0}\sum_{K\subset[0,j)}
G_K^w(G_j^w-S_j^w)Q_{j,K}^w.
}
\tag{2.5}
$$
固定 $j$，用 Cauchy–Schwarz 与 (2.4)，其内和范数不超过
$$
2\eta_j\left(\sum_{K\subset[0,j)}9^{|K|}\right)^{1/2}
=2\eta_j10^{j/2}.
$$
所以 (2.5) 按算子范数收敛，
$$
\boxed{\|W_w-I\|\le\rho,\qquad
\|W_w\|\le1+\rho,\qquad\|W_w^{-1}\|\le(1-\rho)^{-1}.}
\tag{2.6}
$$
全部项属于 $\mathcal U$，故 $W_w,W_w^{-1}\in\mathcal U$。
界与 $t$ 及其 $\ell^2$ 范数无关。

对于 $J\subset[0,m)$，$G_J^w$ 为 $A$ 的次数小于 $2^m$ 的多项式，
其最高次项次数为 $\sum_{j\in J}2^j$，系数非零。
这些多项式构成相对于 $1,A,\ldots,A^{2^m-1}$ 的三角基。
由 $W_w$ 可逆，$G_J^w\Omega_w$ 的闭张成是 $H$，
所以 $\Omega_w$ 对实际 $A$ 循环。
这一点也与 R16/R147 的独立结论一致。

## 3. 纯与实际乘法的正反公式

### 3.1 正向

给 $P\in\mathcal E$，置 $f=P\Omega_w$。
由于 $P$ 与所有 $S_j^w$ 交换，在基上可定义
$$
Y_f(\chi_J\Omega_w)=G_J^wf.
$$
排序展开给
$$
Y_f
=
P+\sum_{j\ge0}\sum_{K\subset[0,j)}
G_K^w(G_j^w-S_j^w)P Q_{j,K}^w.
\tag{3.1}
$$
同一列正交估计给
$$
\|Y_f-P\|\le\rho\|P\|.
$$
因此
$$
\boxed{\mathfrak F_w(P)=Y_fW_w^{-1},\qquad
\|\mathfrak F_w(P)\|\le C_+\|P\|.}
\tag{3.2}
$$
它满足
$$
\mathfrak F_w(P)G_J^w\Omega_w=G_J^wf.
$$
由前节三角多项式基，
$$
\mathfrak F_w(P)p(A)\Omega_w=p(A)f
$$
对全部多项式成立。
在稠密多项式轨道上比较与 $A$ 的作用，便得
$\mathfrak F_w(P)\in\mathcal C$。
特别
$$
\mathfrak F_w(P)\Omega_w=P\Omega_w.
\tag{3.3}
$$

### 3.2 反向

给 $B\in\mathcal C$，置 $f=B\Omega_w$。
在纯基上先形式定义 $P^{(0)}(\chi_J\Omega_w)=S_J^wf$。
反向排序把误差位以前取纯因子、以后取实际因子，得到
$$
\boxed{
P^{(0)}
=
BW_w-\sum_{j\ge0}\sum_{K\subset[0,j)}
S_K^w(G_j^w-S_j^w)BW_wQ_{j,K}^w.
}
\tag{3.4}
$$
右边按算子范数收敛，且
$$
\|P^{(0)}\|\le(1+\rho)\|B\|\|W_w\|
\le C_-\|B\|.
\tag{3.5}
$$
这给有界延拓 $P$。
纯关系 $(S_j^w)^2=2S_j^w-I$，
连同不同位交换及基上的定义，
说明 $P$ 与所有 $S_j^w$、因而所有 $E_j$ 交换。
所以 $P\in\mathcal E$。

由 (3.3) 和 $\Omega_w$ 循环，
$\mathfrak F_w(P)=B$。
反向同样唯一，因为 $\Omega_w$ 对纯多项式 $S_J^w$ 循环。
故
$$
\boxed{\mathfrak F_w:\mathcal E\longrightarrow\mathcal C
\text{ 是线性双射},\quad
\|\mathfrak F_w\|\le C_+,\quad
\|\mathfrak F_w^{-1}\|\le C_-.}
\tag{3.6}
$$
本节既没有交换实际与纯混合因子的次序，也没有把纯代数的幂零关系下放到实际模型。

## 4. 全交换子相对倾斜

由 (1.3)，$\operatorname{Ad}D_w$ 将 $\mathcal E$ 酉同构到自身。
定义
$$
\boxed{
\mathcal T_w
=\mathfrak F_w\circ\operatorname{Ad}D_w\circ\mathfrak F_0^{-1}.
}
\tag{4.1}
$$
这是整个 $\mathcal C$ 上的有界线性同构，正反范数均不超过 $K$。

若 $P=\mathfrak F_0^{-1}(B)$，则 $P1=B1$，故
$$
\begin{aligned}
\mathcal T_w(B)\Omega_w
&=D_wPD_w^*\Omega_w\\
&=D_wP1=(B1)\Omega_w.
\end{aligned}
\tag{4.2}
$$
这证明 (1.5)。
由于 $\Omega_w$ 对 $A$ 循环，(4.2) 唯一决定有界交换子 $\mathcal T_w(B)$。

特别地，当 $B=A$，
$$
\mathcal T_w(A)e^w=(A1)e^w.
$$
一般 $Ae^w(y)$ 等于真实权乘 $e^{w(y-1)}$，
而右边用 $e^{w(y)}$，两者通常不等。
所以不能令 $\mathcal T_w(A)=A$。
若 $e^w$ 恰为一个 dyadic character 乘常相位，
(4.2) 反而给 $\mathcal T_w(B)=\gamma_\zeta(B)$，
此时 $\mathcal T_w(A)=\zeta A$。

## 5. UHF、$\mathcal A$ 与字符：分别验证

### 5.1 双向对应保持 UHF

若 $P\in\mathcal E\cap\mathcal U$，
(3.1)、(3.2) 的每个项均在 $\mathcal U$，故 $\mathfrak F_w(P)\in\mathcal U$。
反向若 $B\in\mathcal C\cap\mathcal U$，
(3.4) 给 $\mathfrak F_w^{-1}(B)\in\mathcal U$。

$D_w$ 共轭保持 $\mathcal U$：
对每个有限局部矩阵，其共轭只涉及有限多个相位，
仍为同一头部的局部矩阵；再由等距性延拓到局部矩阵的范数闭包。

### 5.2 有限纯基的真实像

对有限集合 $F$，直接计算
$$
E_F\Omega_w=q_F^{-1}1_{\{b_j=1,\ j\in F\}}\Omega_w,
\qquad q_F=\prod_{j\in F}q_j.
$$
真实局部莫比乌斯因子
$$
M_j=(I-q_jN_j)(I+q_jN_j)^{-1}
$$
满足 $M_J\Omega_w=\chi_J\Omega_w$，与 R158 §2 的计算相同。
所以
$$
\boxed{
\mathfrak F_w(E_F)=\prod_{j\in F}N_j(I+q_jN_j)^{-1}.
}
\tag{5.1}
$$
右边是实际 $A$ 的真解析芽，属于 $\mathcal A$。
因子里没有漏掉 $q_F^{-1}$；它恰好抵消物理全1柱的 $q_F$。

### 5.3 范数密度与 $\mathcal A$ 的映射

对 $P\in\mathcal E\cap\mathcal U$，
用尾部真空态作有限头条件期望，得到局部算子 $P_m$，
满足 $\|P_m\|\le\|P\|$、$P_m\to P$ 于范数。
这由有限局部矩阵在 $\mathcal U$ 中范数稠密直接得到。

每个 $P_m$ 与低 $m$ 位的全部 $E_j$ 交换，
所以属于有限线性张成
$$
\operatorname{span}\{E_F:F\subset[0,m)\}.
$$
例如这些 $E_F$ 作用于低位常真空张成整个 $2^m$ 维头空间；
任何共同交换子由其在该真空上的值唯一决定，
而上述 $2^m$ 个算子线性独立，故给出全部局部共同交换子。

由 (5.1) 和 $\mathfrak F_w$ 范数连续，
$$
\mathfrak F_w(\mathcal E\cap\mathcal U)\subseteq\mathcal A.
$$
反向若 $B\in\mathcal A$，则 $B\in\mathcal C\cap\mathcal U$，
(3.4) 使其逆像属于 $\mathcal E\cap\mathcal U$。
所以
$$
\boxed{\mathfrak F_w(\mathcal E\cap\mathcal U)=\mathcal A.}
\tag{5.2}
$$
结合 $D_w$ 共轭保持纯代数与 UHF，
得到 $\mathcal T_w(\mathcal A)=\mathcal A$。
这不是仅由 UHF 保持单独推出，而是同时使用了真实交换性和 (5.1) 的有限解析像。

### 5.4 字符保持

若 $P_m=\sum_Fc_FE_F$ 为有限纯多项式，
(5.1) 给
$$
\chi(\mathfrak F_w(P_m))=c_\varnothing.
$$
而 $D_wE_FD_w^*=q_FE_F$，只改变非空集合的系数。
因此
$$
\chi(\mathfrak F_w(D_wP_mD_w^*))
=\chi(\mathfrak F_0(P_m)).
$$
用前节的范数逼近与字符连续性，
得到 $\chi(\mathcal T_w(B))=\chi(B)$ 对全部 $B\in\mathcal A$ 成立。

若 $\chi(B)\ne0$，$\mathcal T_w(B)$ 是 $\mathcal A$ 的真实单位。
由 (4.2) 它将循环向量 $\Omega_w$ 送为 $(B1)e^w$，
证明 (1.7)。

## 6. 一般不保乘法，也不自动保核

令 $Y_j=N_j(I+N_j)^{-1}=\mathfrak F_0(E_j)$。
(4.1)、(5.1) 给
$$
\boxed{\mathcal T_w(Y_j)=q_jN_j(I+q_jN_j)^{-1}.}
\tag{6.1}
$$
若 $\mathcal T_w$ 是单一 $\mathcal A$ 上的代数同态，
由 $A=d_0Y_0(I-Y_0)^{-1}$ 与 (6.1) 必有
$$
\mathcal T_w(A)=q_0A.
$$
再将同态用于 $Y_j=A^{2^j}(d_j+A^{2^j})^{-1}$，
与 (6.1) 比较，形式首系数或 $A$ 的单射性迫使
$$
q_j=q_0^{2^j}\quad\text{对全部 }j.
\tag{6.2}
$$
任取只在第0位非零的纯虚权，并使 $q_0^2\ne1$，
就有 $q_1=1\ne q_0^2$，与 (6.2) 矛盾。
因此本变换一般不是代数同态。
真实关系 $N_j^2=\eta_jN_{j+1}$ 正是不能自由独立缩放所有 $N_j$ 的原因。

即使一个非单位 $B$ 已知单射或有稠密像，
也不能仅从线性同构 (4.1) 推出 $\mathcal T_w(B)$ 有相同核性质。
本稿只在字符非零的单位分支使用循环性。
零锚仍为零锚，后节给更精确的首阶保持。

## 7. 有界有限 chaos 的完整整数首阶公式

本节允许一般复 $c\in\ell^2$，不要求纯虚。
使用 R156 已构造的有界有限 chaos 倾斜 $\Phi_c$。
令
$$
q_j=e^{-2c_j},\qquad
q(n)=\prod_{j:\,b_j(n)=1}q_j.
\tag{7.1}
$$
每个 $q(n)$ 仅含有限乘积，即使 $\sum_jc_j$ 不收敛也定义良好。

先令 $f$ 为低 $m$ 位柱函数。
物理柱展开和
$$
\frac{I+M_j}{2}=(I+q_jN_j)^{-1},\qquad
\frac{I-M_j}{2}=q_jN_j(I+q_jN_j)^{-1}
$$
给实际有限有理恒等式
$$
\boxed{
\Phi_c(f)=
\left[\prod_{j<m}(I+q_jN_j)\right]^{-1}
\sum_{n=0}^{2^m-1}
f(n)q(n)\frac{A^n}{W_n}.
}
\tag{7.2}
$$
其中 $\prod_{j:b_j(n)=1}N_j=A^n/W_n$ 用的是二进制无重叠权积恒等式。

现在令 $f\in H_{\le d}\cap L^\infty$。
R92 给它的唯一连续代表。
取物理0锚定截断
$$
f_m(y)=f(y\bmod2^m).
$$
连续性给 $f_m\to f$ 一致。
每个 $f_m$ 的 Walsh 次数仍不超过 $d$：
可先用 R92 的有限柱一致逼近，再固定全部高位为0；
该操作保持次数上界，最后在低 $m$ 位有限维空间取极限。
所以 R156 的固定次数 $L^\infty$ 连续性给
$\Phi_c(f_m)\to\Phi_c(f)$ 于算子范数。

以 $\iota:\mathcal A\to\mathbb C[[z]]$ 记忠实连续形式系数映射。
对每个固定形式阶，(7.2) 的低阶系数在 $m$ 足够大时精确稳定，
因为 $f_m(n)=f(n)$ 对 $n<2^m$ 成立。
于是
$$
\boxed{
\iota(\Phi_c(f))(z)=
\frac{\displaystyle\sum_{n\ge0}f(n)q(n)z^n/W_n}
{\displaystyle\prod_{j\ge0}(1+q_jz^{2^j}/d_j)}.
}
\tag{7.3}
$$
这里只是合法的形式幂级数，不宣称正解析半径。
分母常数项为1。

若 $f\ne0$，非负整数在 $\mathbb Z_2$ 中稠密，
所以存在首个
$$
r=\min\{n\ge0:f(n)\ne0\}<\infty.
$$
由 (7.3)，
$$
\boxed{
\operatorname{ord}\Phi_c(f)=r,\qquad
[z^r]\iota(\Phi_c(f))
=q(r)\frac{f(r)}{W_r}.
}
\tag{7.4}
$$
因此任意允许的指数倾斜都保留首次非零整数位置，
特别保留零锚 $f(0)=0$。
这说明不能单靠选择指数参数把共振符号变成非零字符单位。

没有将 $f(n)$ 用于一般 $H$ 向量。
例如 $\sum_j(j+1)^{-1}\chi_j\in H$ 的有限柱0值发散；
$H$ 中不存在有界的0点评价泛函。
对任意未知 $L^2$ 端点，点值锚仍须先由实际正则性证明得到。

## 8. 整个 $\mathcal A$ 的形式阶保持

有限纯多项式的像 $\mathfrak F_0(E_F)=Y_F$ 是有限柱符号的实际乘子；
§5 的逼近说明这些有限柱乘子在线性空间 $\mathcal A$ 中范数稠密。

令
$$
H_1(z)=\prod_{j\ge0}(1+z^{2^j}/d_j),
\qquad
\tau_n(B)=W_n[z^n]\bigl(H_1(z)\iota(B)(z)\bigr).
\tag{8.1}
$$
每个 $\tau_n$ 是 $\mathcal A$ 上的连续线性泛函，
因为只含有限多个连续形式系数。
对有限柱乘子 $B=X_f$，(7.2) 在 $c=0$ 时给 $\tau_n(B)=f(n)$。

因此对纯虚 $w$，从有限柱逼近、(7.3) 与 $\mathcal T_w$ 的范数连续性，
得到一般 $B\in\mathcal A$ 的形式公式
$$
\iota(\mathcal T_w(B))(z)=
\frac{\displaystyle\sum_{n\ge0}\tau_n(B)q(n)z^n/W_n}
{\displaystyle\prod_{j\ge0}(1+q_jz^{2^j}/d_j)}.
\tag{8.2}
$$
如果 $B\ne0$、$r=\operatorname{ord}B$，
分母 $H_1$ 的常数项为1，故 $\tau_n(B)=0$ 对 $n<r$，
$\tau_r(B)=W_r[z^r]\iota(B)$。
由此
$$
\boxed{
\operatorname{ord}\mathcal T_w(B)=\operatorname{ord}B,\qquad
[z^r]\iota(\mathcal T_w(B))
=q(r)[z^r]\iota(B).
}
\tag{8.3}
$$
这没有给一般 $B1$ 赋予未经证明存在的连续点值；
$\tau_n$ 在这里是正式定义的有界算子系数泛函。

本稿仍未判定零锚慢共振平方的核。
它给出全交换子上的真实相对倾斜、准确的单位分支，
以及指数倾斜无法消除首整数零集的严格界线。
