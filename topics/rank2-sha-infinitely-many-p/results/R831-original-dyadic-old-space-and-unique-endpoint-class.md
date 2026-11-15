# R831 — 原二处三维旧空间的完整 Chow 测试矩阵与唯一端点类

日期：2026-11-15。**状态：已证明。**

本篇保持 R830 的原 $f,g,h$、三条原有序角色和全部坏位。
不再改变局部表示，只计算二处整个三维 old 空间的实际对角来源。
结论是：移到共同的 $h^1(f)\otimes h^1(g)\otimes h^1(h)$ 目标后，
九项类矩阵只有两个可能非零的端点，且准确互为相反数。
任意旧向量组合因而只乘同一个端点类，不产生新的独立来源。

这个结论不证明端点类或其 $p$-adic Abel–Jacobi 值非零。
R830 的全部有限局部 test-vector 非零与这个未决全局门继续区分。

## 1. 先在真实 $X_0$ 曲线上固定共同目标

固定 R826/R830 的一个有序对 $(g,h)=(g_j,g_k)$，其中
$$
(j,k)=(10,16),(16,4),(4,10).
$$
它们分别对应原 $\lambda_4,\lambda_{10},\lambda_{16}$。
记
$$
M=2601,\quad N=4M=10404,\quad
X=X_0(N),\quad C=X_0(M),\quad C_2=X_0(2M).
\tag{1}
$$
$f=\theta(\psi_{17})$ 在2处 conductor exponent为2；
$g,h$ 是 level $M$ 的原平凡 nebentypus 新形式。

对 $a=0,1,2$，令
$$
q_a:X\longrightarrow C,\qquad \tau\longmapsto2^a\tau .
\tag{2}
$$
模解释是依次 quotient 原 cyclic4部分的 order $2^a$ 子群，
并保留原 cyclic $M$ 子群。三个映射的次数均为6。
取 $Q=e^{2\pi i\tau}$，原几何微分为
$$
\omega_{g,a}=q_a^*\omega_g
=2^a g(Q^{2^a})\,\frac{dQ}{Q},
\qquad
\omega_{h,b}=2^b h(Q^{2^b})\,\frac{dQ}{Q}.
\tag{3}
$$
尤其中间向量是 $2g(Q^2)$，不是裸 $g(Q^2)$。

所有曲线使用 cusp 支撑的 degree1 基点循环。
Manin–Drinfeld 给每个实际映射的
$q_*o_X=o_Y$、$q^*o_Y=(\deg q)o_X$，有理系数下成立。
因此它们与各曲线的 $h^1$ Chow–Künneth 投影相容。
以后所有等式均在一个固定包含原 CM 幂等元及 cusp 数据的系数域 $L$
上解释。

用 $\Delta_X$ 表示 modified diagonal，定义**共同目标**中的类
$$
\boxed{
Z_{ab}
=(e_f\otimes e_g\otimes e_h)_*
  (\mathrm{id}_X\times q_a\times q_b)_*\Delta_X
\in CH^2(X\times C\times C)_{\mathbf Q}\otimes L.
}
\tag{4}
$$
它已在三份 $h^1$ 因子上，且 homologically trivial。
需要时再施原(2,2,2)张量的 $\lambda_\ell$ CM 幂等元。

(4)的共同目标很重要：
$X^3$ 上不同 old 副本的投影类本来位于不同嵌入；
不能不作运输就将它们直接相等。
其准确返回为
$$
\boxed{
\Delta^{(a,b)}_X
=\frac1{6^2}
(\mathrm{id}_X\times q_a^*\times q_b^*)Z_{ab}.
}
\tag{5}
$$
这里各 old projector 是 $6^{-1}q_a^*e_g(q_a)_*$。
它们未被当成彼此正交的 projector。

## 2. 七个共同低层项在 Chow 群中为零

令
$$
r_0:X\to C_2,\quad\tau\mapsto\tau,\qquad
r_1:X\to C_2,\quad\tau\mapsto2\tau .
$$
二者次数均为2。令 $s_0,s_1:C_2\to C$ 分别为
$\tau\mapsto\tau,\tau\mapsto2\tau$，次数均为3，则
$$
q_0=s_0r_0,\quad q_1=s_1r_0=s_0r_1,\quad q_2=s_1r_1.
\tag{6}
$$
因此 $a,b\in\{0,1\}$ 时，两因子通过同一个 $r_0$；
$a,b\in\{1,2\}$ 时，通过同一个 $r_1$。

原 $f$ 的新空间性质给准确的 motive 等式
$$
e_f r_0^*=e_f r_1^*=0
\quad\text{于 }\operatorname{Hom}(h^1(C_2),h^1(X)).
\tag{7}
$$
可在局部新向量上核定：$C_2$ 的二处有 $K_0(2)$ 固定向量，
$f$ 的 conductor为2，故没有该固定向量；
共轭 $K_0(2)$ 对应 $r_1$，同样没有。
在 Jacobian 的 $h^1$ 对应上，该 cohomological 零通过同态忠实性成为(7)，
不是将任意高余维 cohomology 零冒认为 Chow 零。

R829 的有限平坦图形身份在这两个实际 cusp 映射上同样成立：
$$
(\mathrm{id}\times r_\epsilon\times r_\epsilon)_*
[\Delta_X^{\rm sm}]
=(r_\epsilon\times\mathrm{id}\times\mathrm{id})^*
[\Delta_{C_2}^{\rm sm}].
\tag{8}
$$
所有基点项因 Manin–Drinfeld 与 CK 相容而消去。
再推前 $s_a,s_b$ 并用(7)，得到
$$
\boxed{Z_{ab}=0\qquad (|a-b|\le1).}
\tag{9}
$$
这是七个完整 Chow 等式，不只某一个 de Rham 槽为零。

## 3. 显式 partial $W_4$ 与绝对 old 反射

取 determinant4 的整数矩阵
$$
\mathcal W=
\begin{pmatrix}4&-1\\4M&1-M\end{pmatrix}
=
\begin{pmatrix}4&-1\\10404&-2600\end{pmatrix}.
\tag{10}
$$
它定义 $X_0(4M)$ 的实际 partial Atkin–Lehner 对合 $w_4$。
可直接核验
$$
\mathcal W\Gamma_0(4M)\mathcal W^{-1}=\Gamma_0(4M),
\qquad \mathcal W^2/4\in\Gamma_0(4M).
$$
其代数模解释是 quotient 原 cyclic4子群，
把 dual cyclic4核与所保留的 $M$ 子群合成新的 cyclic $4M$ 子群；
故该对合定义于 $\mathbf Q$。

置 $B_a=\operatorname{diag}(2^a,1)$。因为 $M\equiv1\bmod4$，
以下三个都是整矩阵：
$$
C_a=
\begin{pmatrix}
2^a&-1\\M&(1-M)/2^a
\end{pmatrix}\in\Gamma_0(M).
$$
准确的矩阵等式为
$$
\boxed{B_a\mathcal W=2^a C_a B_{2-a}\qquad(a=0,1,2).}
\tag{11}
$$
于是实际曲线映射和微分分别满足
$$
\boxed{
q_aw_4=q_{2-a},\qquad
w_4^*\omega_{g,a}=\omega_{g,2-a},\qquad
w_4^*\omega_{h,a}=\omega_{h,2-a}.
}
\tag{12}
$$
在权二 slash 约定
$F|_2A=\det(A)(c\tau+d)^{-2}F(A\tau)$ 下，
(11)中的中心 scalar $2^a$ 作用为1。
因此(12)没有额外 $2$、$4$ 或未确定相位。
这也是为何必须使用(3)的几何倍率。

## 4. 原 $f$ 的 partial $W_4$ 特征严格为 $-1$

该符号不能仅由全局 root number 猜测。
原 $f$ 在2处是 conductor2、中心特征1的 depth-zero supercuspidal。
其 finite cuspidal type 是
$$
GL_2(\mathbf F_2)\simeq S_3
$$
的 sign 表示：维数 $q-1=1$，
且上 unipotent 的非平凡元素作用为 $-1$，故为cuspidal。
R826 的原 dyadic cubic inducing character正给这唯一类型。

令 $K_2=GL_2(\mathbf Z_2)$，
$v$ 为 compact-induction 中支撑在 $\mathbf Q_2^\times K_2$ 的该类型向量，
$\gamma=\operatorname{diag}(2^{-1},1)$。
如 R830 §4 的新向量证明，原新线由 $\gamma v$ 生成。

设
$$
W_{\rm loc}=\begin{pmatrix}0&-1\\4&0\end{pmatrix},\qquad
w=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$
则
$$
\gamma^{-1}W_{\rm loc}\gamma=2w.
\tag{13}
$$
中心 $2$ 的作用为1，而 $w\bmod2$ 是 $S_3$ 的 transposition，
故 $W_{\rm loc}(\gamma v)=-\gamma v$。
同时
$$
\mathcal W=W_{\rm loc}
\begin{pmatrix}M&(1-M)/4\\-4&1\end{pmatrix},
\tag{14}
$$
右矩阵在 $K_0(4)$ 中，因而固定原新向量。
在奇数有限位，(10)属于原 $K_0(\ell^{v_\ell(N)})$，平凡中心/nebentypus 不添相位。
因此
$$
\boxed{w_4^*\omega_f=-\omega_f.}
\tag{15}
$$
对全部系数域嵌入及其共轭相同。
曲线 $h^1$ 对应对 Jacobian 实现忠实，遂有完整 motive 恒等式
$$
\boxed{e_f(w_4)_*=(w_4)_*e_f=-e_f.}
\tag{16}
$$
这里使用 $w_4^2=1$，所以 push 与 pull 同号。
并未以形式的负号代替 actual finite dyadic type。

## 5. 完整 $3\times3$ 类矩阵

对合 $w_4$ 把 cusp 基点送至另一个 cusp。
Manin–Drinfeld 使两基点在 $CH_0(X)_{\mathbf Q}$ 中相等，
故
$$
(w_4\times w_4\times w_4)_*\Delta_X=\Delta_X.
\tag{17}
$$
在(4)中用(17)、(12)、(16)，得到
$$
Z_{ab}=-Z_{2-a,\,2-b}.
\tag{18}
$$
没有置换三因子，故此处的负号只来自原 $f$ 的(16)，不是另添 Koszul 号。

结合(9)，令 $Z=Z_{02}$，则
$$
\boxed{
(Z_{ab})_{0\le a,b\le2}
=
\begin{pmatrix}
0&0&Z\\
0&0&0\\
-Z&0&0
\end{pmatrix}.
}
\tag{19}
$$
(19)在 $CH^2(X\times C\times C)_{\mathbf Q}\otimes L$ 中成立，
并在原 $\lambda_\ell$ 等全部进一步 CM 投影后仍成立。

更一般，令 $\mathbf c=(c_0,c_1,c_2)$、
$\mathbf d=(d_0,d_1,d_2)$ 为固定代数系数。
使用线性 correspondence
$\sum c_a e_g(q_a)_*$、$\sum d_b e_h(q_b)_*$ 定义共同目标的类。
则
$$
\boxed{
Z(\mathbf c,\mathbf d)=(c_0d_2-c_2d_0)Z.
}
\tag{20}
$$
中间系数 $c_1,d_1$ 没有贡献。

(20)说的是共同目标中的线性 extraction；
它不是声称“投影到向量 $\sum c_aq_a^*\omega_g$ 的归一 rank-one projector”
随 $\mathbf c$ 线性。那些 projector 需要实际 Gram/dual 规范。
若要回到某个单独 old 副本，应使用(5)，而不是省去其拉回与 $6^{-2}$。

## 6. 返回原 $X_1$ 呈示及全部次数因子

记原曲线
$$
X^{(1)}=X_1(N),\qquad C^{(1)}=X_1(M),
$$
并令
$$
a:X^{(1)}\to X,\qquad b:C^{(1)}\to C
$$
为遗忘点生成元、只保 cyclic 子群的映射。
在粗 modular 曲线上准确有
$$
D_X=\deg a=\varphi(N)/2=1632,\qquad
D_C=\deg b=\varphi(M)/2=816.
\tag{21}
$$
因 $N,M>2$，该除2来自 $\pm P$。
这两个次数仅含2、3、17因子，在原 $p>17$ ray 上均为单位。

令 $q_a^{(1)}:X^{(1)}\to C^{(1)}$ 为原 $\tau\mapsto2^a\tau$
的三个 degree12 映射。它们满足
$$
bq_a^{(1)}=q_aa,\qquad
12D_C=6D_X.
\tag{22}
$$
特别 R830 两个端点正是这里 $a=0,2$，没有改变向量或微分。

原平凡 nebentypus 幂等元都在 diamond-trivial 部分。
若 $A=a\times b\times b$，并以 $Z^{(1)}_{ab}$ 表示(4)在原
$X^{(1)}\times C^{(1)}\times C^{(1)}$ 中的对应类，
则
$$
\boxed{
A_*Z^{(1)}_{ab}=D_X Z_{ab},\qquad
Z^{(1)}_{ab}=D_C^{-2}A^*Z_{ab}.
}
\tag{23}
$$
证明：将(22)代入原小对角推前，
$(a\times a\times a)_*\Delta_{X^{(1)}}=D_X\Delta_X$；
各 cusp/CK 项相容。
再使用 diamond-trivial projector
$D_X^{-1}a^*a_*$ 和 $D_C^{-1}b^*b_*$，
给第二式。不能将三个不同层级的次数全部换成12。

因此(19)、(20)在原共同目标中不变：
$$
\boxed{Z^{(1)}(\mathbf c,\mathbf d)
=(c_0d_2-c_2d_0)Z^{(1)}_{02}.}
\tag{24}
$$
原 $X_1(N)^3$ 中的单副本投影类准确是
$$
\boxed{
\Delta^{(a,b)}_{X^{(1)}}
=\frac1{12^2}
(\mathrm{id}\times(q_a^{(1)})^*\times(q_b^{(1)})^*)
Z^{(1)}_{ab}.
}
\tag{25}
$$
这正恢复 R830 的两个 normalized old 幂等元，
以及单位根基的各 $1/12$。

(23)还说明：对同一 $X_0$ de Rham 测试的实际拉回，
原 $X_1$ Abel–Jacobi 标量等于 $D_X$ 乘下层标量。
这是 projection formula，不是自由选择的 CM period。
由于系数非零，所有零、反号和(24)均按原规范传回。

## 7. 原第四槽的九个完整杯积代表

保留 R830 的普通位及 $\pi,\bar\pi$，下层原函数满足
$$
\theta G_g=g-\bar\pi Vg,\qquad
\theta G_h=h-\bar\pi Vh,\qquad \theta=Q\,d/dQ.
$$
对于(3)，实际原函数是
$G_{g,a}=G_g(Q^{2^a})$、$G_{h,b}=G_h(Q^{2^b})$，
没有额外 $2^a,2^b$。
完整 finite-polynomial 代表为
$$
\boxed{
\Xi_{ab}=
\left(
2^bG_g(Q^{2^a})h(Q^{2^b})
-
2^a\bar\pi G_h(Q^{2^b})g(Q^{2^ap})
\right)\frac{dQ}{Q}.
}
\tag{26}
$$
所以对共同目标的类，Besser 公式准确给
$$
\boxed{
AJ_p(Z^{(1)}_{ab})(\omega_f\otimes\omega_g\otimes\omega_h)
=
\frac{\langle\omega_f,[\Xi_{ab}]\rangle_{X^{(1)}}}
 {1+\bar\pi/\pi^2}.
}
\tag{27}
$$
左侧的 $\omega_f,\omega_g,\omega_h$ 分别是共同目标上的原拉回规范；
右侧已经由 projection formula 把后两者拉到上层。
(27)也等于对 $\Delta^{(a,b)}_{X^{(1)}}$
使用实际 $\omega_f\otimes\omega_{g,a}\otimes\omega_{h,b}$ 的值。

由(19)、(24)，完整分子满足
$$
\langle\omega_f,[\Xi_{ab}]\rangle=0\quad(|a-b|\le1),
\qquad
\langle\omega_f,[\Xi_{20}]\rangle
=-\langle\omega_f,[\Xi_{02}]\rangle.
\tag{28}
$$
因此若
$g_{\mathbf c}=\sum c_a\,2^ag(Q^{2^a})$、
$h_{\mathbf d}=\sum d_b\,2^bh(Q^{2^b})$，则
$$
\boxed{
AJ_p(\Delta_{X^{(1)}})
(\omega_f\otimes\omega_{g_{\mathbf c}}\otimes\omega_{h_{\mathbf d}})
=
(c_0d_2-c_2d_0)
\,AJ_p(Z^{(1)}_{02})(\omega_f\otimes\omega_g\otimes\omega_h).
}
\tag{29}
$$
这保留全部两项、真实倍率和同一非零 Frobenius 分母。
没有以 ordinary-forms projection 删除(26)第二项。

## 8. 实际约束及未付门

R830 已证两个端点所用的全部有限局部 test vectors 非零；
R831 说明在这整个二处三维 old 空间中，它们仍只产生同一条
可能非零的全局 Chow 来源。两个端点相反，中间向量不能另造一条独立关系。

若 $c_0d_2-c_2d_0=0$，共同目标的类严格为零。
若该行列式非零，类是否非零准确等价于 $Z^{(1)}_{02}$ 是否非零；
同一个固定 $p$ 上的指定 AJ 值也只有这一条非零问题。
即使允许在不同 $p$ 选择不同的有限系数，
(29)也不能把已为零的端点 regulator变成非零。

这不等同于 R814 的固定 canonical cycle，
也不提供它们之间尚未支付的非零比例。
原三条 $\lambda_\ell$ 的全部 finite 角色、Hodge gap、period及原中央门不变。
本篇没有新增数值计算；全部矩阵、次数和类恒等式由上述符号证明给出。

## 9. 依据

- [R829](R829-same-degeneracy-diagonal-chow-vanishing.md)：
  实际 cusp 的 Manin–Drinfeld、CK 相容与同一低层映射的 Chow 零；
  本篇(8)逐项使用相同 scope。
- [R830](R830-distinct-degeneracy-test-vectors-and-fourth-slot.md)：
  原不同退化向量、全有限坏位测试、微分倍率和完整第四槽。
- [R826](R826-fixed-low-weight-cm-triple-and-fourth-de-rham-slot.md)：
  原三条有序对、全部 CM 张量与 ordinary/critical 规范。
- A. O. L. Atkin–J. Lehner, *Hecke operators on $\Gamma_0(m)$*,
  Math. Ann. **185** (1970), 134–160：
  <https://link.springer.com/article/10.1007/BF01359701>。
  本篇的特定 partial involution、三条 old 反射和绝对符号
  另由(10)–(16)自含支付，不依赖未显示的全局 root 推断。
- D. Prasad, *Trilinear forms for representations of GL(2) and local
  epsilon-factors*, Compositio Math. **75** (1990), 1–46，
  Theorem6.1 的 compact-induction 描述；
  <https://www.numdam.org/article/CM_1990__75_1_1_0.pdf>。
- A. Besser, *On the regulator formulas of Bertolini, Darmon and Rotger*,
  Res. Math. Sci. **3** (2016), article26，
  Proposition2.1/2.2及§4；
  <https://link.springer.com/article/10.1186/s40687-016-0073-x>。
