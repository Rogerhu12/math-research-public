# R271 补录：一般真实头的长坏链解析 Schur 型、三个旧真幂旗与完整候选费用

日期：2026-11-20（UTC）。作者：Astra-ISP-b2a9acde-20261120 / r271_cost；AI-assisted GPT-6 Astra Pro。

状态：**本条明确范围内的完整解析 Schur 型及费用已证明。**

## 0. 范围

本条对原 N、Y 真实头的最高 carry 退化，解析计算尾链长度
$l\ge n+3$ 时的完整三次幂 Schur 型。
它精确合同于三个旧真实头的幂旗，合同中不使用 $A^{-1}$。
同时列出核参数化、合同、旧真幂逆及强尾还原的物理成本。

本条支付长坏链的最高极点方程；短坏链仍须另付，实际原源仍须估计。
合同不是物理正交分解，局部候选向量也不是未经证明的真实 MP 正交分量。
普通 Hilbert ISP 与原完整费用门仍未闭。

父结果为[完整奇高度简单极点](R271-appendix-odd-height-highest-carry-full-mp-simple-pole.md)、[883原头费用](R271-appendix-odd-height-highest-carry-explicit-883-cost-and-d-sized-budget.md)及[中位强尾尺度](R271-appendix-median-strong-tail-scaling-four-power-condition-and-full-odd-height-cost.md)。以下只添加尚未登记的一般长坏链解析型，不重做旧完整 MP 定理。

## 1. 最高真实 carry 与单位尾链

取 $m\ge4$，令
$$
n=2^{m-1},\qquad d=2n,\qquad a=16^{m-2}.
$$
旧真实头记为 $A=A_{m-1}=F(B)$，其中 $B$ 是旧 $n$ 维真实 weighted shift，
$F$ 是旧有限 N 或 Y 函数，$F'(0)=d_0^{-1}$。
最高参数取
$$
\rho=d_{m-2}^2,\qquad d_{m-1}(t)=t\rho,\qquad b=b_{m-1}.
$$
新真实头有精确块式
$$
H_t=\begin{pmatrix}A&bI+tV\\0&A\end{pmatrix}.
\tag{1.1}
$$
$H_0=A+bE$ 的 Jordan 型为 $(n+1,n-1)$，所以 $H_0^{n+1}=0$。

令 $\mathcal J_h$ 为 $h$ 维逆序矩阵，$J_l$ 为单位后移 Jordan 链。
实际二进制权满足
$v_2(n-j)=v_2(j)$（$0<j<n$），故
$$
\mathcal J_nB=B^*\mathcal J_n.
$$
实系数函数演算保持这个身份，最高块也保持 palindromic 关系。
因此
$$
\mathcal J_dH_t=H_t^*\mathcal J_d.
\tag{1.2}
$$

固定奇数
$$
l\ge n+3,
$$
考虑完整单位尾链块
$$
C_t=H_t\otimes I_l+I_d\otimes J_l,\qquad
X_t=C_t^3=X_0+tX_1.
\tag{1.3}
$$
其翻转为
$\mathcal J=\mathcal J_d\otimes\mathcal J_l$。

## 2. 完整退化核的无逆参数化

对 $p=1,2,3$ 和任意头向量 $u\in\mathbb C^d$，定义
$$
\Phi_p(u)=
\sum_{j=0}^{n}(-1)^j\binom{p+j-1}{j}
H_0^ju\otimes e_{p-1+j}.
\tag{2.1}
$$
因为 $l\ge n+3$，所有尾坐标都在链内。
逐项相消给
$$
C_0\Phi_p(u)=\Phi_{p-1}(u),\qquad \Phi_0=0,
$$
所以 $\Phi_p(u)\in\ker C_0^3$。

令
$$
\Phi(u_1,u_2,u_3)=\Phi_1(u_1)+\Phi_2(u_2)+\Phi_3(u_3).
$$
其前三个尾级分别为
$$
v_0=u_1,\quad
v_1=-H_0u_1+u_2,\quad
v_2=H_0^2u_1-2H_0u_2+u_3.
$$
因此左逆为
$$
u_1=v_0,\qquad
u_2=v_1+H_0v_0,\qquad
u_3=v_2+2H_0v_1+H_0^2v_0.
\tag{2.2}
$$
$\Phi$ 有 $3d$ 个独立列。
另一方面 $H_0$ 的每个头块长至多 $n+1$，与 $J_l$ 相加后的每条链长至少为
$l-n\ge3$，故三次幂核维数恰为 $3d$。
于是
$$
\boxed{\operatorname{Ran}\Phi=\ker C_0^3.}
\tag{2.3}
$$
这是整个退化核，不是选取的一部分核列。

原 $\|A\|<6$、$b<1$，故 $\|H_0\|<7$。
(2.2) 给
$$
\|\Phi_{\rm left}^{-1}\|\le(1+\|H_0\|)^2\le64.
\tag{2.4}
$$
由 (2.1) 的有限和及正交尾级，可粗取
$$
\boxed{\|\Phi\|\le3(n+2)^3\,7^n.}
\tag{2.5}
$$
这些是单位尾链块中真实物理范数的成本。

## 3. 有限尾生成恒等式

先取标量 $z$，令
$$
v_p(z)=\sum_{j=0}^{l-p}
(-1)^j\binom{p+j-1}{j}z^j e_{p-1+j}.
$$
直接核对
$$
(z+J_l)v_p(z)
=v_{p-1}(z)+
(-1)^{l-p}\binom l{p-1}z^{l-p+1}e_{l-1}.
\tag{3.1}
$$
又对 $q\le3$、$0\le h\le2$，二项式相消给
$$
v_q(z)^T\mathcal J_l(z+J_l)^h e_{l-1}
=\begin{cases}1,&h=q-1,\\0,&h\ne q-1.\end{cases}
\tag{3.2}
$$
例如该和等于
$$
z^{h-q+1}\binom h{q-1}
\sum_{j=0}^{h-q+1}(-1)^j\binom{h-q+1}{j}.
$$
将 (3.1) 迭代三次，再用 (3.2)，得到
$$
v_q(z)^T\mathcal J_l(z+J_l)^3v_p(z)
=c_{pq,l}\,z^{l+4-p-q},
\tag{3.3}
$$
其中
$$
c_{pq,l}=
\begin{cases}
0,&p+q\le3,\\
(-1)^{l+3-p-q}\binom l{p+q-4},&p+q\ge4.
\end{cases}
\tag{3.4}
$$

把 $z$ 换成 $\mathcal J_d$-自伴的 $H_t$。
此时各头幂通过 (1.2) 可以合并，故 (3.3) 成为算子配对恒等式。
在 $t\ne0$ 时使用截断到 $l-p$ 的 $v_p(H_t)$，并不声称它在核中。
在 $t=0$ 它恰等于 (2.1)。
微分后，参数向量的导数项都与 $X_0\Phi=0$ 相消，因而完整 Schur 型为
$$
\Phi_q^*\mathcal J X_1\Phi_p
=c_{pq,l}\,\mathcal J_d
\left.\partial_tH_t^{\,l+4-p-q}\right|_{t=0}.
\tag{3.5}
$$

由于 $l$ 奇，三块系数分别为：
$p+q=4$ 时为 $1$，$p+q=5$ 时为 $-l$，
$p=q=3$ 时为 $\binom l2$。
这些是理论生成恒等式，不是消元输出表。

## 4. 所有高幂导数共用一个真实可逆旧头因子

写
$$
g(z)=F(z)/z,\qquad U=\rho\,g(B)^n.
\tag{4.1}
$$
$g(0)=d_0^{-1}\ne0$，所以 $U$ 可逆，并与 $A$ 交换。

删除新最高 Boolean 项，参考头为
$\widehat H_1=F(B_m(\rho))$。
因为 $B_m(\rho)^n=\rho E$，对 $k\ge n$，
$$
\widehat H_1^k=
\begin{pmatrix}0&U A^{k-n}\\0&0\end{pmatrix}.
$$
而最高位只能在块乘法中通过一次，故 (1.1) 中
$$
\boxed{
\left.\partial_tH_t^k\right|_{t=0}
=\begin{pmatrix}0&U A^{k-n}\\0&0\end{pmatrix},
\qquad k\ge n.
}
\tag{4.2}
$$
这也可从
$\rho B^{k-n}g(B)^k=\rho g(B)^nA^{k-n}$
直接核对。
最高 Boolean 项 $bI$ 不与 $tV$ 同时出现于一个块路径，故不产生遗漏项。

置
$$
G=\mathcal J_nU.
\tag{4.3}
$$
$G$ 为真实自伴可逆矩阵，且 $GA=A^*G$。
因为 $\mathcal J_d$ 交换新最高位的两个块，(3.5) 的型只作用于
每个参数 $u_p$ 的最高位为 $1$ 的旧 $n$ 维部分；
最高位为 $0$ 的参数全部在根空间中。

令
$$
q=l-n\ge3,\qquad c_l=\frac{l(l-1)}2.
$$
在剩下的完整 $3n$ 维参数空间上，Schur 型恰为
$$
\mathcal B_l=
\begin{pmatrix}
0&0&GA^q\\
0&GA^q&-lGA^{q-1}\\
GA^q&-lGA^{q-1}&c_lGA^{q-2}
\end{pmatrix}.
\tag{4.4}
$$
没有把旧头换成单位 Jordan 头，也没有更换旧真核旗。

## 5. 无 $A^{-1}$ 的精确合同

作三角变换
$$
w_1=u_1,
$$
$$
w_2=u_2-\frac2{l+1}Au_1,
$$
$$
w_3=u_3+\frac2{l(l-1)}A^2u_1-\frac2{l-1}Au_2.
\tag{5.1}
$$
它的逆为
$$
u_1=w_1,\quad
u_2=w_2+\frac2{l+1}Aw_1,\quad
u_3=w_3+\frac2{l-1}Aw_2+\frac2{l(l+1)}A^2w_1.
\tag{5.2}
$$
逐项完成平方，使用 $GA=A^*G$，得到准确合同
$$
\boxed{
\mathcal B_l\cong
\frac2{l(l+1)}GA^{q+2}
\ \oplus\
\left(-\frac{l+1}{l-1}\right)GA^q
\ \oplus\
\frac{l(l-1)}2GA^{q-2}.
}
\tag{5.3}
$$
这是自伴型的合同，不是物理单位ary变换或正定能量分解。
(5.1)–(5.2) 完全不使用 $A^{-1}$。

因 $A$ 是原循环上三角头，
$$
\ker A^e=\operatorname{span}(e_0,\ldots,e_{e-1})
\qquad(0\le e\le n).
\tag{5.4}
$$
$G$ 可逆，故 $GA^e$ 的真核仍为 (5.4)；
它自伴，所以在正交尾坐标
$\operatorname{span}(e_e,\ldots,e_{n-1})$
上的限制非退化。
由 (5.3)，完整新增秩为
$$
\boxed{
(d-l+2)_++(d-l)_++(d-l-2)_+.
}
\tag{5.5}
$$
Jordan 张量和的直接链长计数给出相同的真秩差，
故没有只打开其中一部分方向。

## 6. 物理费用

已证真实参考头与旧头的条件数为
$$
\kappa(\widehat V)\le e^{441a},\qquad
\kappa(V_{\rm old})\le e^{221a}.
$$
由 $\widehat H_1^n=\begin{pmatrix}0&U\\0&0\end{pmatrix}$，
$$
\|U^{-1}\|=\|(\widehat H_1^n)^\dagger\|
\le e^{441a}.
\tag{6.1}
$$
旧头单位 Jordan 幂的非零奇值为 $1$，所以
$$
\|(A^e)^\dagger\|\le e^{221a}
\quad(0\le e<n).
$$
对 $f\in\operatorname{Ran}(GA^e)$，
$(A^e)^\dagger U^{-1}\mathcal J_nf$ 是完整真解，
故
$$
\boxed{\|(GA^e)^\dagger\|\le e^{662a}.}
\tag{6.2}
$$
$e\ge n$ 时矩阵为零，MP 亦为零。

$m\ge4$ 给 $l\ge11$，而 $\|A\|<6$；
由 (5.1)–(5.2)，合同矩阵及其逆的范数均小于 $4$。
因此完整参数 Schur 型（包括其根空间）满足
$$
\|\mathcal B_l^\dagger\|
\le8l(l+1)e^{662a}.
\tag{6.3}
$$

若局部原源 $\xi$ 满足实际最高极点兼容性，
则 $\Phi^*\xi$ 消去 Schur 根空间。
令 $u=\mathcal B_l^\dagger\Phi^*\xi$，再还原被明确列出的零参数块，
$$
\widetilde q=\mathcal J\Phi u
$$
在完整 $\ker X_0^*$ 中满足全部极点方程。
真实局部极点解在这个完整方程的解集中范数最小，
所以由 (2.5)、(6.3)
$$
\boxed{
\|q_{-1}^{(l)}\|
\le72\,l(l+1)(n+2)^6\,49^n\,e^{662a}\,\|\xi\|.
}
\tag{6.4}
$$
此处 $\xi$ 是实际局部配对源；本条不以 $\|\xi\|\le1$ 等未证断言代替它。

## 7. 嵌回完整原强尾的费用与边界

取原偶强段 $R\ge d$，中位尺度
$y=m+R/2,\ c=y^{-2}$。
归一化强尾条件数至多 $4^R$。
只把坏链 $l\le d+1$ 从标准 $cL_l$ 化为单位 $J_l$；
其附加条件数至多
$$
c^{-(l-1)}/(l-1)!\le y^{2d}.
$$
好链可以保留 $cL_l$，不应为它们支付一个无用的巨大单位链成本。
因此完整坏链还原可取
$$
\kappa(\mathcal S)\le4^R y^{2d}.
\tag{7.1}
$$

在相似坐标中，源为 $\mathcal S^*\xi$，候选解还原为
$\mathcal S^{-*}q'$，二者只合计一个 $\kappa(\mathcal S)$。
对所有 $n+3\le l\le d+1$ 的长坏链，
(6.4) 可用 $l(l+1)\le(d+1)(d+2)$ 统一相加为一个完整直和候选解；
直和范数取统一上界，不另乘链条数量。

该候选在长坏链的所有极点方程上正确，在其余块的方程上贡献为零。
短坏链 $l\le n+1$ 的源仍须另构造解并相加。
不能把非正交还原后的这个候选称作真实 MP 的一个物理正交分量。

## 8. 最长坏链的解析一维证书与 N 型孔支撑

当 $l=d+1$ 时，(5.3) 仅剩
$c_lGA^{n-1}$，秩恰为 $1$。
取原最高头坐标 $e_{d-1}$，则
$$
\Phi_3(e_{d-1})\in\ker C_0^3
$$
给出解析非零证书，其 Schur 自配对为
$$
\binom{d+1}{2}
\left\langle e_{n-1},GA^{n-1}e_{n-1}\right\rangle>0.
\tag{8.1}
$$
正性来自原第一超对角线权的正乘积及
$Ue_0=\rho d_0^{-n}e_0$。
因此该一维方向不需要任何消元表。

对 N 型，$H_0$ 的每一步最多删去一个物理孔。
(2.1) 中第 $j$ 项头孔数至少为 $m-j$，尾级为 $2+j$，
所以
$$
\Phi_3(e_{d-1})
\text{ 的最低局部物理孔级至少为 }m+2.
\tag{8.2}
$$
嵌入 primitive 起始孔 $j_0$ 后再加 $j_0$。
Y 型可能含一次删去多个孔的项，故本条不对 Y 型使用 (8.2)。

三位小头的半高孔现象不能照搬至一般 $m$：
最长坏链的自然解析门是 $m+2$，而链半高孔约为 $d/2$。
一般头后续应使用这里真实的旧幂旗和源支撑，而不是假定同一半高孔门仍成立。
