# R390：实际 CM 坐标的逆向惯性、最低权通道与固定 Cartier 单位

**状态：已证明。** 本篇补齐 R378 中目标整坐标的惯性取向，并证明它在任意同源整格上不变。所有实际 CM 坐标权都同余于 $1\bmod6$。指定原始角色 $\theta_{-1}$ 给最低权 $1$ 的一维形式因子，该因子的归一化展开整体至少被 $p$ 整除。另给这个角色与固定权四 CM 形式的完整 Fourier 同余，以及固定良模型的明确 Cartier／Laurent 单位。

这里没有证明 $L(g_{\theta_{-1}},1)\ne0$，也没有证明实际商的一次项在除以 $p$ 后为单位。固定 tame 层截面的简单零和固定椭圆曲线的 Laurent 系数，尚未被识别成变化 $p$ 水平商的 primitive jet。本文不关闭 Serre 一致性问题。

## 1. 记号与结论

保持 R348、R374、R378 的规范：
$$
K=\mathbb Q(s),\quad s^2=-3,\quad
\zeta=(-1+s)/2,\quad
p\ge41,\quad p\equiv2\pmod3,\quad
M=p+1,\quad e=p^2-1.
\tag{390.1}
$$
固定 $K\hookrightarrow\overline{\mathbb Q}_p$，把 $\mathcal O_K/p$ 识别为 $\mathbb F_{p^2}$。选取与这个识别一致的 Teichmüller 提升。对 $k\bmod M$ 定义
$$
\theta_k(\alpha)=
[\bar\alpha]^{(p-1)k}\qquad
(\alpha\in(\mathcal O_K/p)^\times).
\tag{390.2}
$$
它在 $\mathbb F_p^\times$ 上平凡。R348 的条件准确等价于
$$
\theta_k\in\Theta_p
\quad\Longleftrightarrow\quad k\equiv5\pmod6.
\tag{390.3}
$$
记
$$
g_k=f_{\Psi_{\theta_k}\kappa_4^{-1}},\qquad
\theta_{-1}=\theta_p,\qquad g_-=g_p.
\tag{390.4}
$$
$\theta_{-1}$ 的阶为 $M$。

令 $B/\mathbb Q_p$ 与 R348 的若干实际 CM 因子的乘积同源，允许重数和任意同源代表。在共同 tame 良约化域上，取 R378 的半线性坐标环约定，令
$\sigma(\varpi)=\xi\varpi$，其中 $\varpi^e=p$、$\xi$ 为原始 $e$ 次单位根。则目标形式坐标可以按一维完整 $p$-可除因子选取，使
$$
\sigma(Y_i)=\xi^{(p-1)\ell_i}Y_i,\qquad
1\le\ell_i\le p,\qquad \ell_i\equiv1\pmod6.
\tag{390.5}
$$
对于来自 $\theta_k$ 的选定 $p$ 进系数嵌入，
$$
\ell_i\equiv-k\pmod M.
\tag{390.6}
$$
特别地，$g_-$ 的因子在任意同源代表中都有一个 $\ell_i=1$ 的一维形式因子。这里是**坐标环**的特征；它与 transported Tate 表示的有限扭曲互逆。

令 $q:J_{Z_p}\twoheadrightarrow B$ 为 $g_-$ 因子的任意实际满射，仍以 $c_1$ 为 Abel–Jacobi 基点，并取上面的权一坐标。R378 在
$$
w=\frac{a-1}{p^3}
\tag{390.7}
$$
上给出的相应非零函数 $G(w)=\sum_{n\ge1}b_nw^n$ 满足
$$
v_p(b_n)\ge
\left\lceil\frac{3n-1}{p+1}\right\rceil\ge1,\qquad
p^{-1}G\in R_0\langle w\rangle.
\tag{390.8}
$$
这里 $R_0$ 为该构造中的未分歧整数环。因而这一坐标的实际共同赋值是有限整数，且至少为一。本文不给它的上界。

固定 Hecke 角色
$$
\Phi_4((\alpha))
=\alpha^3\epsilon_3(\alpha)\kappa_4((\alpha))^{-1},
\qquad h_4=f_{\Phi_4}
\tag{390.9}
$$
给出有理整数系数、平凡 nebentypus、准确层 $108$、权 $4$ 的 CM 新形式。若
$\Theta=q\,d/dq$ 只表示形式级数算子，则完整系数恒等为
$$
\boxed{\ \overline{g_-}=\Theta^{p-2}\overline{h_4}\ }.
\tag{390.10}
$$
没有把两侧未经补充地视为同一整模形式线丛上的截面。

最后，在固定模型
$$
E_0:y^2=x^3-1,\qquad
t=-x/y,\qquad \omega=dx/(2y),\qquad
z=\int_0^t\omega
\tag{390.11}
$$
上，形式对数到所有次数 $n<p^2$ 都 $p$ 整，且
$$
\boxed{
[z^{p-1}]\,x(t(z))
\equiv
(-1)^{(p+1)/6}
\binom{(p-1)/2}{(p-2)/3}
\in\mathbb F_p^\times.}
\tag{390.12}
$$
这条公式使用完整证明给出所有 $p\equiv2\bmod3$、$p\ge5$ 的结论，不依赖有限扫描。

## 2. 角色标签及有限扭曲的准确取向

因为 $p-1\equiv1\bmod3$，(390.2) 给
$\theta_k(\zeta)=\zeta^k$。又 $s^p=-s$，所以
$s^{p-1}=-1$，从而 $\theta_k(s)=(-1)^k$。因此
$k\equiv2\bmod3$ 且 $k$ 为奇数，正好是 (390.3)。

R374 取了同一固定参考 $E_0$ 及其无穷型 $(1,0)$ 角色 $\Psi_0$。在每个 $\ell$ 进实现，包括 $\ell=p$，有
$$
\psi_k=\psi_0\,\eta_k,\qquad
\eta_k=\Psi_{\theta_k}\kappa_4^{-1}/\Psi_0.
\tag{390.13}
$$
$\eta_k$ 为有限阶角色，在 $K_p^\times$ 的单位群上为
$\theta_k^{-1}$。该式在 $\ell=p$ 的准确性由 R374 引用的 Serre–Tate CM 角色公式保证；不是只把异特征 Tate 角色照搬到 $p$。

采用局部 uniformizer 对应算术 Frobenius 的互反约定。对于 $u\in\mathcal O_{K_p}^\times$，参考的代数修正项给
$$
\psi_0(\operatorname{rec}_{K_p}(u))=u^{-1},\qquad
\eta_k(\operatorname{rec}_{K_p}(u))
=[\bar u]^{-(p-1)k}.
\tag{390.14}
$$
因此若 $\omega_2(\sigma)=\overline{\sigma(\varpi)/\varpi}$，有限扭曲在所选嵌入上的值是
$$
\eta_k(\sigma)=\xi^{(p-1)k}.
\tag{390.15}
$$
这里把 $\xi$ 与其剩余 Teichmüller 值相容地选择。

所有系数嵌入也仍以 (390.3) 的标签描述。R374 已证明系数域在
$\mathbb Q(\mu_M)^+$ 中，且 $p$ 在该实域全分裂。给一个系数嵌入，延拓到
$\mathbb Q(\mu_M)$ 后，如有必要再合成复共轭，可以使它固定 $K$，因为复共轭固定实系数域。于是它在 $\mu_M$ 上取某个 $a$ 次幂，其中
$a\equiv1\bmod6$；新的标签仍为 $ak\equiv5\bmod6$。不同系数嵌入给不同标签：否则相应 Hecke 角色在所有与导子互素的理想上相同，两个新形式也相同，矛盾。无穷型 $(1,0)$ 与 $(0,1)$ 不同，故这里不会漏掉诱导角色互换的另一种等价。

要从 (390.15) 读目标**坐标环**，必须取逆。设在一个良模型上作泛纤维识别，transported 点的 Galois 作用为
$$
P\longmapsto[\eta_k(\sigma)]\,\sigma_0(P).
\tag{390.16}
$$
函数的半线性作用由 $\sigma(f)(P)=
\sigma\bigl(f(\sigma^{-1}P)\bigr)$ 定义，因而它在余切上的有限因子为
$\eta_k(\sigma)^{-1}$。这也可在六次扭曲上直接检验：
若 $u^6=d$、$X=x/u^2$、$Y=y/u^3$，则
$t_{\rm good}=u\,t_{\rm bad}$，坐标环权为 $\sigma u/u$，而 transported Tate 扭曲是其逆。于是 (390.6) 正是所需取向。

下两节处理尚不能从有理 Tate 空间自动推出的整格与完整良模型。

## 3. 参考完整 BT 群及任意稳定整格

### 3.1 参考对象确实存在

$E_0[p^\infty]$ 在 $\mathcal O_{K_p}$ 上有
$\mathcal O_{K_p}$ 作用：从 $\mathcal O_K$ 的代数 CM 作用取 $p$ 进完备化，每一有限 $p^n$ 层只需要系数模 $p^n$，这些作用相容。因而任意
$\mu_{p+1}\subset\mathcal O_{K_p}^\times$ 元素都是这个**完整 BT 群**的自同构，在 Lie 上通过选定的 $K_p$ 嵌入作用。这里没有把它称作单个椭圆曲线的代数自同构；后者在特征零只有 $\mu_6$。

对每个标签 $k$，在一个消去 $\eta_k$ 的有限 tame 扩张上，用
$E_0[p^\infty]$ 配上 (390.16) 的半线性下降数据，构造参考完整 BT 群
$\mathcal G_k$。外侧 Frobenius 对 $\mathcal O_{K_p}$ 的作用是非平凡共轭，并将 $\eta_k$ 变成其逆，故下降关系相容。也可由行列式逐项核对 uniformizer：两条二维表示的行列式同为 cyclotomic，局部诱导行列式公式给
$\eta_k|_{\mathbb Q_p^\times}=1$，所以 $\eta_k(p)=1$。因此这里没有遗漏一个阻碍外侧平方关系的未分歧有限因子。

这个参考 BT 群的泛纤维 Tate 表示准确是
$\operatorname{Ind}_{G_{K_p}}^{G_{\mathbb Q_p}}(\psi_0\eta_k)$，与实际 CM 系数嵌入的表示相同。这里只声称良扩张上的 BT 群及其半线性下降，不声称这些下降数据在分歧底环上已经有效地产生一个良约化的 $\mathbb Z_p$-BT 群。

### 3.2 残余类型互不相撞

R374 在实际 $E_0$ 形式参数上证明了
$E_0[p]|_{I_p}=\omega_2\oplus\omega_2^p$。因此参考二维整格的残余惯性指数为
$$
a_k=1+(p-1)k,\qquad
b_k=p-(p-1)k
\quad(\bmod e).
\tag{390.17}
$$
同类指数相等迫使 $k=l\bmod M$。交叉相等则迫使
$$
k+l\equiv1\pmod M.
\tag{390.18}
$$
这与 $k,l\equiv5\bmod6$ 矛盾。一个标签内也不能有 $a_k=b_k$，因为这会迫使 $2k\equiv1\bmod M$，而 $M$ 为偶数。

Frobenius 把 $a_k$ 与 $b_k$ 交换。因此每个参考二维格模 $p$ 在
$G_{\mathbb Q_p}$ 下绝对不可约：扩张剩余域后，任何不变直线必须是两个不同惯性特征线之一，Frobenius 又把它送到另一条。

为了得到整幂等元，可以直接取 (390.14) 中 Teichmüller 单位的**表示像**。这些矩阵组成一个有限的、阶与 $p$ 互素的循环群 $\Delta$。其每对特征值是
$\xi^{a_k},\xi^{b_k}$；两者为 $p$-Frobenius 共轭，且不同标签的对互不相交。有限群平均或互素多项式的中国剩余定理给出
$$
e_k\in\mathbb Z_p[\Delta],\qquad
e_kV_p(B)=V_k.
\tag{390.19}
$$
这是表示像中的有限群；没有在绝对 Galois 群中假定存在一个有限阶 tame 元素。等价地，也可在紧惯性像的正规 pro-$p$ 核上使用 Schur–Zassenhaus，再作同一平均。

设 $\Lambda\subset V_p(B)$ 为任意 $G_{\mathbb Q_p}$-稳定全格。因为 (390.19) 是整的，
$$
\Lambda=\bigoplus_k e_k\Lambda.
\tag{390.20}
$$
所以从有理同源到实际整格时，这里不需要先假定某个 Hecke 或 CM 投影已经饱和。

### 3.3 每个分块的格唯一性

先考虑重数一，令 $T_k$ 为参考二维格。把 $e_k\Lambda$ 乘以最小所需的 $p$ 次幂，使其包含于 $T_k$，但不包含于 $pT_k$。它在
$T_k/pT_k$ 中的像非零，绝对不可约性使这个像为全空间。于是
$e_k\Lambda+pT_k=T_k$。Nakayama 引理对有限生成商给
$e_k\Lambda=T_k$。因此原格与 $T_k$ 同伦。

有重数时也没有额外的扩张格障碍。参考二维格上的 Galois 像所生成的
$\mathbb Z_p$-代数记为 $\mathcal A_k$。模 $p$ 的绝对不可约性和有限维 Burnside 定理给
$\overline{\mathcal A_k}=M_2(\mathbb F_p)$；再对
$M_2(\mathbb Z_p)/\mathcal A_k$ 用 Nakayama，得到
$\mathcal A_k=M_2(\mathbb Z_p)$。矩阵单位遂作用于任何
$V_k^{\oplus m_k}$ 中的稳定格，迫使其具有
$$
T_k\otimes_{\mathbb Z_p}\Lambda_k
\quad\text{的形式},
\tag{390.21}
$$
其中 $\Lambda_k$ 是重数空间中的自由 $\mathbb Z_p$ 格。选取
$\Lambda_k$ 的基后，便得到到 $T_k^{\oplus m_k}$ 的
$G_{\mathbb Q_p}$-等变整同构。综合各标签可得实际 $T_p(B)$ 与参考 BT 群乘积的 Tate 格同构，不只是有理同构或残余半单同构。

## 4. Tate 全忠实性、坐标权与强制的 $p$ 因子

取共同有限 Galois 扩张 $L/\mathbb Q_p$，使 $B$ 和所有参考对象都有良模型，且包含所需的单位根和 $\varpi$。参考对象的有限惯性在此消失；实际 $B$ 的存在良约化由 R374 的 CM 惯性描述与 Néron–Ogg–Shafarevich 保证。

Tate，*p-Divisible Groups*，§4.2 Theorem 4 及其 Corollaries 1–2 说明：在整闭 noetherian 整环上，完整 $p$-可除群的泛纤维同态唯一延拓；Tate 格同构因而唯一延拓为 BT 群同构。应用于 §3 的整同构及其逆，得到
$$
B[p^\infty]_{\mathcal O_L}
\simeq\prod_k\mathcal G_k^{\,m_k}.
\tag{390.22}
$$
没有要求 $e(L/\mathbb Q_p)<p-1$。这一步使用完整 $p$-可除群，不能用一个有小分歧限制的 BT$_1$ 延拓定理替换。两边的半线性下降数据在泛纤维与该同构交换；延拓的唯一性保证在整模型上仍交换。由此，参考对象给出的余切特征准确转移到任意同源代表。

参考 BT 群连通且一维，故 Tate §2.2 Proposition 1 将各因子识别为一维形式群。每个因子的坐标环特征由 §2 为
$\xi^{-(p-1)k}$。取其模 $e$ 的最小非负代表，即
$(p-1)\ell$，其中 $\ell\equiv-k\bmod M$。
因为 $k\equiv5\bmod6$，有 $\ell\equiv1\bmod6$。按 R378 的有限平均把坐标提升为准确本征坐标，得到 (390.5)。该平均的分母整除 $e$，为 $p$ 单位，保留余切的单位一次项。

对 $g_-$，原标签是 $k=p\equiv-1\bmod M$，故
$\ell=1$。选这个一维形式因子的坐标 $Y$，在源小盘上写
$F(z)=Y(q([P(z)-c_1]))$。它不是零函数：该形式因子的非零不变微分是一条
$B_L$ 的不变余切线；满射 $q$ 使其在 Jacobian 上的拉回非零，Abel–Jacobi 又把 Jacobian 的全纯微分同构到曲线的全纯微分。若这个形式投影在一个非空盘上常值，其不变微分拉回会在该盘上恒零，从而全局恒零，矛盾。

现在可以逐字使用 R378 的**同一实际参数和同一映射**。那里
$z=(a-1)/\varpi^{3p(p-1)}$、$z=\varpi^{3(p-1)}w$，且
$G(w)=\varpi^{-(p-1)}F(\varpi^{3(p-1)}w)$。系数赋值式给
$$
v_p(b_n)\ge
\left\lceil\frac{3n-\ell}{M}\right\rceil
=\left\lceil\frac{3n-1}{M}\right\rceil.
\tag{390.23}
$$
对所有 $n\ge1$，右侧至少为一，且趋于无穷，证明 (390.8)。非零性同时说明该坐标的共同赋值有限。

如果以后证明
$$
v_p(b_1)=1,
\tag{390.24}
$$
则 $G(w)/p$ 有单位一次项，其余系数整。对 $v_p(w)\ge1$，
$(G(w)/p)/w$ 的常数项为单位，其余项在极大理想中，所以
$G(w)=0$ 只能有 $w=0$。这是一个准确的条件性接口；本文尚未证明 (390.24)。

此外，使用 $G(P)=0$ 排除有理点还需要选定的 $g_-$ 因子有秩零，或至少该形式因子的准确零像。R348 的平均只保证某个 $\theta$ 的中心值非零，不保证指定的 $\theta_{-1}$。两项缺口不能相互替代。

## 5. 固定权四形式及全部 Fourier 系数同余

$\Phi_4$ 在主元单位下不变：$\zeta^3=1$，而
$(-1)^3\epsilon_3(-1)=1$；$\kappa_4$ 是理想角色，对单位为一。
R348 已算出 $\kappa_4$ 的准确导子为 $(2)(s)^2$。
$\epsilon_3$ 的导子为 $(s)$，其阶二，不能消去 $\kappa_4$ 在
$1+s\mathcal O_3$ 上的非平凡三次角色。因此
$$
\mathfrak f(\Phi_4)=(2)(s)^2.
\tag{390.25}
$$
Hecke–Shimura theta 对应给权四、层
$|D_K|N\mathfrak f=108$ 的新形式。它的 nebentypus 是
$\chi_{-3}$ 与 $\Phi_4(n)/n^3=\epsilon_3(n)$ 的乘积，故平凡。
其理想值在 $K$ 中且为代数整数，共轭理想给共轭值，所以全部 Fourier 系数都是有理整数。

对 $p\nmid n$，取范数 $n$、与 $6$ 互素的任一理想
$\mathfrak a=(\alpha)$。在所选 $p$ 位有
$\bar\alpha=\alpha^p$，故
$$
\alpha\,\theta_{-1}(\alpha)
\equiv\alpha^{2-p}
=\frac{\alpha^3}{\alpha\bar\alpha}
=\frac{\alpha^3}{n}\pmod p.
\tag{390.26}
$$
乘以相同的 $\epsilon_3(\alpha)\kappa_4(\mathfrak a)^{-1}$ 并对理想求和，得到
$$
a_n(g_-)\equiv n^{-1}a_n(h_4)\pmod p
\qquad(p\nmid n).
\tag{390.27}
$$
在 $2,3$ 两边都取准确的分歧 Euler 因子 $1$，因此式中也包括被
$2$ 或 $3$ 整除的指标：这些系数两边均为零。没有只在好素数上核对后跳过坏 Euler 因子。

在 $p$，$g_-$ 的 Hecke 角色分歧，所以其所有被 $p$ 整除的系数为零。
$h_4$ 的局部角色未分歧且 $p$ 惰性，有
$\Phi_4((p))=-p^3$，故其 Euler 因子为
$(1+p^3T^2)^{-1}$，特别地
$$
a_{p^{2r+1}}(h_4)=0,\qquad
a_{p^{2r}}(h_4)=(-p^3)^r.
\tag{390.28}
$$
形式算子 $\Theta^{p-2}$ 则在所有 $p\mid n$ 的项上给零，在其他指标上给
$n^{p-2}=n^{-1}\bmod p$。这证明完整级数恒等 (390.10)。

这个同余是准确的全局算术输入，但它本身不比较特征零的复中心值，也不比较不同模形式线丛在超奇异点的整格。

## 6. 固定 tame 六层截面的准确简单零

此节只计算固定 tame 层，不声称它已经通过 $p$ 整 Chen 对应成为
§4 的实际 $F$ 或 $G$。

先去掉 $\kappa_4$，令
$\Phi_{4,0}((\alpha))=\alpha^3\epsilon_3(\alpha)$。其 CM 新形式为
$$
h_{4,0}(\tau)=\eta(3\tau)^8.
\tag{390.29}
$$
这里可以不用数据库核对。Dedekind eta 的变换式给
$\eta^8|_4S=\eta^8$、$\eta^8|_4T=\zeta\eta^8$，这个角色通过
$\mathrm{SL}_2(\mathbb F_3)/Q_8$，故 $\eta^8$ 在 $\Gamma(3)$ 上模。
由 $D_3\Gamma_0(9)D_3^{-1}=\{\pm I\}\Gamma(3)$ 得
$\eta(3\tau)^8\in S_4(\Gamma_0(9))$。它在各 cusp 的消失也可从
$(\eta^8)^3=\Delta$ 立即看出。两边前四项为
$q+0q^2+0q^3-8q^4$；$\Gamma_0(9)$ 的指数为十二，权四的消失阶界为四，故二者相同。这一消失阶界可直接取所有陪集的范数并应用级一 valence 公式，不依赖数值逼近。

记三个二旧向量
$$
h_0=h_{4,0}(\tau/6),\quad
h_1=h_{4,0}(\tau/3),\quad
h_2=h_{4,0}(2\tau/3).
\tag{390.30}
$$
与 R348 的混合层计算相同，模二表示是 $1\oplus\mathrm{Std}$，其中
$h_1$ 为平凡线。这里可把所需常数直接算全：
Fricke$_9$ 的特征为 $+1$，且 $a_2=0,\ a_4=-8$，所以
$$
S:\ (h_0,h_1,h_2)\longmapsto
(16h_2,h_1,h_0/16),\qquad
T^3:\ h_0\longmapsto-h_0-16h_2.
\tag{390.31}
$$
$T^3$ 固定 $h_1,h_2$，而 $T^2$ 在三条给定线上的特征分别为
$\zeta,\zeta^2,\zeta$。这些式子确定整个三维表示。

在把几何 $H_6$ 的对角三循环选成 $ST$ 的模六图式后，实际不变线由
$$
v=h_0-16\zeta h_2
=\eta(\tau)^4(B-\zeta A),\qquad
A=\vartheta_2(\tau)^4,\quad B=\vartheta_4(\tau)^4
\tag{390.32}
$$
生成。第一等式由 (390.31) 直接给 $v|_4ST=v$；模三的
$Q_8$ 核在这个标准模二成分上平凡，因此它是完整的 $H_6$ 不变线，而不只一个元素的不变向量。第二等式由 Jacobi 乘积式
$\eta(\tau/2)^8=B\eta(\tau)^4$、
$\eta(2\tau)^8=A\eta(\tau)^4/16$ 得到。

在 $ST$ 固定的 $j=0$ 标记上，有 $A=\zeta^2B$。也可不选择 theta 常数分支来确定这一点：$v$ 是权四的 $ST$ 不变向量，固定点上的自动因子非一，故 $v$ 在该点为零；由 (390.32) 且 $A,B\ne0$ 得同一等式。Jacobi 恒等式给
$$
E_4=A^2+AB+B^2
=(A-\zeta B)(A-\zeta^2B),\qquad
\Delta=\frac{A^2B^2(A+B)^2}{256}.
\tag{390.33}
$$
于是
$$
\boxed{\ \frac v{E_4}
=-\frac{\zeta\eta(\tau)^4}{A-\zeta B}\ }.
\tag{390.34}
$$
在 $p>3$ 的良 CM 模型及一个整微分平凡化下，$\Delta$ 为单位；
(390.33) 使 $A,B,A+B$ 都为单位，且 $\eta^4$ 的六次幂是
$\Delta$。分母在该 CM 点是 $(\zeta^2-\zeta)B$，亦为单位。
所以 (390.34) 是准确的整单位式。用细模参数
$y^2=x^3+t x-1$ 时，$E_4$ 与 $t$ 相差一个 $p$ 单位，故 $v$ 恰有单位系数的简单零。

这种标记给 tame 六层上 $j=0$ 的一个未分歧椭圆点；另外两个由
$\delta_\zeta$ 搬运，微分因子为单位。它们正是 $a^3=1$ 的三个点，区别于三次分歧的 $a=0$ 点。实际 $\sqrt[3]4$ 扭曲在 $p>3$ 未分歧，尺度为单位，因此同一简单零结论适用于固定 tame 曲线的 $a=1$ 支。

本节说的是 **tame 权四截面在细模参数上的简单零**。它不是
$Z_p$ 的粗参数 $w$ 上的单位一次项，也没有把权四截面直接当权二的商微分。

## 7. 固定良模型的 Cartier 单位与有限阶对数

在特征 $p$ 中，用 $x$ 作为函数域的分离变量。Cartier 的公式为
$$
C\!\left(\sum_j c_jx^j\,dx\right)
=\sum_m c_{pm+p-1}^{1/p}x^m\,dx,
\qquad C(f^p\omega)=f\,C(\omega).
\tag{390.35}
$$
因为
$$
\omega=\frac{(x^3-1)^{(p-1)/2}}{2y^p}\,dx,
\tag{390.36}
$$
而 $p-1$ 不被三整除，唯一可能产生 Cartier 项的 $x^{p-1}$ 系数为零。
其余候选次数已大于分子的次数。因此 $C(\omega)=0$，也直接证明所需超奇异性。

对于第二类微分，
$$
x\omega=\frac{x(x^3-1)^{(p-1)/2}}{2y^p}\,dx.
\tag{390.37}
$$
分子的次数为 $(3p-1)/2<2p-1$，故只有 $x^{p-1}$ 一项贡献。
相应的三次幂指标是 $(p-2)/3$，从而
$$
C(x\omega)=c_p\omega,\qquad
c_p=(-1)^{(p+1)/6}
\binom{(p-1)/2}{(p-2)/3}\in\mathbb F_p^\times.
\tag{390.38}
$$
二项式全部阶乘参数小于 $p$，所以最后的非零不是推测。

现在写 $\omega=f(t)\,dt$，其中
$f(t)=\sum_{j\ge0}f_jt^j\in\mathbb Z_p[[t]]$、$f_0=1$。
$C(\omega)=0$ 的局部公式逐项给
$$
f_{mp-1}\equiv0\pmod p\qquad(m\ge1).
\tag{390.39}
$$
因此
$$
z=\sum_{n\ge1}\frac{f_{n-1}}n t^n
\tag{390.40}
$$
的全部 $1\le n<p^2$ 次系数都整：当 $p\nmid n$ 时显然；当
$p\mid n$ 时此范围内分母只含一个 $p$，由 (390.39) 消去。
这个有限截断的线性项为一，故其反函数到同一精度也整。本文不声称完整对数整；从次数 $p^2$ 起，上述论证不能消去全部分母。

$x(t)$ 的极点阶为二。因此计算 $x(t(z))$ 的 $z^{p-1}$ 系数只需要反函数
$t(z)$ 到次数 $p+2$。对 $p\ge5$ 有 $p+2<p^2$，故这一步可以合法模
$p$。令 $Z(t)$ 为 $z(t)$ 到次数 $p+2$ 的整截断，则
$$
x(t)\bigl(\omega-dZ\bigr)=O(t^p)\,dt.
\tag{390.41}
$$
这项误差不能贡献 Cartier 输出的常数项。Cartier 的坐标不变性遂把
(390.38) 变为 $C(x(t(Z))\,dZ)=c_p\,dZ$ 的常数项等式。唯一贡献来自
$x(t(Z))$ 的 $Z^{p-1}$ 项；极项 $Z^{-2}$ 不贡献常数项。因为
$c_p\in\mathbb F_p$，取 $p$ 次根仍为 $c_p$，证明 (390.12)。

作为纯代数的可复算表达式，令
$$
x(t(z))=z^{-2}+\sum_{m\ge1}\beta_mz^{6m-2}.
\tag{390.42}
$$
由 $x'^2=4x^3-4$、$x''=6x^2$ 得
$$
\beta_1=\frac17,\qquad
\beta_m=
\frac{\sum_{a=1}^{m-1}\beta_a\beta_{m-a}}
{(m-1)(6m+1)}\quad(m\ge2).
\tag{390.43}
$$
取 $m=(p+1)/6$ 即得到 (390.12) 的另一精确计算途径。该递推只补充可复算性；全素数单位性已经由 Cartier 证明，不以有限计算替代。

## 8. 对实际首项还缺什么

已闭合的整模型部分包括：有限 Tate 扭曲与坐标环权的逆向关系；所有实际 CM 类型的模六限制；从任意有理同源代表的实际稳定格到完整良 BT 群的整同构；指定原始角色的权一因子及强制的整体 $p$ 因子。它们不依赖一个未经证明已饱和的 Hecke 投影。

但 §5 的全局 Fourier 同余、§6 的固定 tame 截面、§7 的固定良椭圆曲线系数，还没有通过一个准确的整比较被证明等于 §4 实际映射的 $b_1/p$。尤其：

- 需要保留 Chen 对应、商映射和微分整格的真实比例；非显式有理标量可能改变共同赋值。
- 需要证明所选 $\theta_{-1}$ 的非零中心值，或在 R348 已有非零中心值的因子上完成相应首项控制。
- 即使取得一个固定截面的单位，也必须证明它在同一实际 $p$ 水平、同一 CM 标记与同一归一化下给出 $b_1/p$，不能仅由 $q$ 展开归一化、正根号或 Cartier 非零推出。

主统一性目标仍然开放。下一步继续上述实际整比较，不停在本篇的局部结论上。

## 9. 原文输入与产物

- J. Tate, *p-Divisible Groups*, Proceedings of a Conference on Local Fields (Driebergen, 1966), Springer, 1967, pp.158–183；§2.2 Proposition 1，§4.2 Theorem 4 及其 Corollaries 1–2（扫描并列印刷 pp.180–181）。[原刊扫描](https://www.math.purdue.edu/~tongliu/teaching/598/p-divisible.pdf)。本篇实际使用的是完整 $p$-可除群的整全忠实性，而不是小分歧的有限平坦群延拓。
- J.-P. Serre–J. Tate, *Good reduction of abelian varieties*, Ann. of Math. 88 (1968),492–517，§7 Theorems 10–11；[扫描](https://wstein.org/papers/bib/Serre-Tate-Good_Reduction_of_Abelian_Varieties.pdf)。其在所有 $\ell$（包括 $p$）的 CM 代数修正项已由 R374 逐式使用，本篇沿用同一规范。
- R348 的 Hecke–Shimura theta 输入、实际 $\kappa_4^{-1}$ 扭向及全部有限导子；R374 的系数域与有限 Tate 角色；R378 的实际源参数、整坐标构造和系数尾估计。
- §6 的 Jacobi 乘积、变换与 theta 恒等式也可查 NIST DLMF [§20.5](https://dlmf.nist.gov/20.5)、[§20.7](https://dlmf.nist.gov/20.7)、[§23.15](https://dlmf.nist.gov/23.15)。正文给出所需向量、矩阵及单位式，没有引用一个未核的 CM 点首项表。
- §7 的 Cartier 公式、有限阶积分及 Laurent 系数证明完整写在本文。协作推导见工作笔记；没有把任何有限 sanity 表作为本结论的证明或必需数据。

本篇为纯证明，无必需数据文件或重跑脚本。

