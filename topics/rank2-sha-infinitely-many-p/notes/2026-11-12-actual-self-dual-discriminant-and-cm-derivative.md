# 原自对偶判别式、素于 p 的总迹及 CM 微分行

日期：2026-11-12。**已证明。** 本篇继续 R142、R145 的同一个
非 CM Hecke 行。自对偶卷积、回到源曲线的总迹、Igusa 导数及
原算术 Frobenius 都保持原标签。最后的有限模计算只限定这些
已证约束本身的效力，不把一个抽象模型称为实际 newform 的反例。

## 1. 原自对偶卷积的准确二阶系数

记
$$
 B_j=\tau^jB,\quad n=\sum_jB_j,\quad
 A=\sum_jjB_j,\quad F_2=\sum_j\binom j2B_j,\quad
                  \mathscr D=A^2-nA-2nF_2.
\tag{1}
$$
所有权都在 $\mathbb F_p$ 中，$p\ge7$。在
$k(Y)[T]/(T^p-1)$ 中取原多项式
$$
                         P_B(T)=\sum_{j=0}^{p-1}B_jT^j.
\tag{2}
$$
令 $X=T-1$，则
$$
 \begin{aligned}
 P_B(T)&=n+AX+F_2X^2+O(X^3),\\
 P_B(T^{-1})&=n-AX+(A+F_2)X^2+O(X^3).
 \end{aligned}
$$
因此
$$
             \boxed{\quad
             P_B(T)P_B(T^{-1})
                        =n^2-\mathscr D X^2+O(X^3).
             \quad}
\tag{3}
$$
这是真正的同一 $U$ 迹自对偶卷积。
由于 $\tau P_B(T)=T^{-1}P_B(T)$，完整乘积被 $\tau$ 固定。
在原 CM 点 $n=0$ 时，其二阶项本来就等于 $-A^2$；
自对偶性本身不决定 R142 所需的 $d\mathscr D$。

## 2. 素于 p 的 Cartan coset 总迹准确为零

沿用 R145 的固定配对中心商 $\widetilde X$，
$$
 G=\mathrm{PSL}_2(\mathbb F_\ell),\quad
 T_0=T\cap G,\quad
 Z=\widetilde X/T_0,\quad X_{\rm src}=\widetilde X/G.
$$
这里
$$
                    [Z:X_{\rm src}]
                      =\ell(\ell-1)\quad\text{素于 }p.
\tag{4}
$$
并未把一个带因子 $p$ 的迹恒等式除以 $p$。

在 $\mathbb P^1(\mathbb F_\ell)$ 的原 $T/U$ 标记中，
记 $j(v)\in\mathbb F_p$ 满足 $v\in\tau^{j(v)}Uv_0$。
每个值出现 $u$ 次。式 (1) 等价于
$$
 \mathscr D=\sum_{v,w}Q_{vw}h_vh_w,\qquad
                   Q_{vw}=-\frac12\bigl(j(v)-j(w)\bigr)^2.
\tag{5}
$$
矩阵 $Q$ 被 $T_0$ 固定，且
$$
 Q_{vv}=0,\qquad
 \sum_wQ_{vw}=-\frac u2\sum_{r\in\mathbb F_p}(j(v)-r)^2=0.
\tag{6}
$$
最后一步使用 $p>3$。

取矩阵的真正 coset 和
$$
                         Q^\#=\sum_{\gamma\in G/T_0}\gamma Q.
$$
它被 $G$ 固定。$G$ 在射影线上双传递，所以其全部非对角
条目等于一个常数 $c$；对角仍为零。
每行和仍为零，故 $\ell c=0$。$\ell\ne p$ 迫 $c=0$。
将这个矩阵恒等式用于原函数向量 $(h_v)$，得到
$$
 \boxed{\qquad
 \operatorname{Tr}_{Z/X_{\rm src}}\mathscr D=0,\qquad
 \operatorname{Tr}_{Z/X_{\rm src}}
                  \left(\frac{\mathscr D}{n^2}\right)=0 .
 \qquad}
\tag{7}
$$
第二式使用 $n$ 从源拉回。
这比对整个 $G$ 求和后因 $p\mid|T_0|$ 自动为零更强，
而且保留原判别式。它仍是完整 coset 迹，
不能将非原 CM Cartan 标记的项删掉。

## 3. 原 Igusa 导数与微分判别式

记 $f$ 为 $E389$ 的正规化权二 newform，$\partial$ 为源的
Igusa/ST 导数。每个真实 $\ell$ 商支选目标 Igusa 微分，
使同源拉回该微分等于源微分；记对应的权二值为 $f_v$。
Kodaira–Spencer 的同源比例及原去 $p$ 函数给
$$
       \partial h_v=\ell^{-1}(f_v-a_pf_v^p).
\tag{8}
$$
比例可以在同一 Tate 参数核定：有限支导数有 $\ell^{-1}$，
无穷支目标微分除以 $\ell$，权二值乘 $\ell^2$，
故其右边也正好给无穷支的导数倍数 $\ell$。
没有对两类支使用不同的未比较周期。

令 $H_0$ 为对应的原完整 $U$ 迹权二行，记
$$
                    v=N_\Gamma H_0,\quad
                    U_1=D_1H_0,\quad V_2=D_2H_0.
$$
式 (8) 给准确的同一行等式
$$
 \ell n'=v-a_pv^p,\qquad
 \ell A'=U_1-a_pU_1^p,\qquad
 \ell F_2'=V_2-a_pV_2^p,
\tag{9}
$$
其中撇号表示 $\partial$，$D_i$ 的权都在 $\mathbb F_p$ 中。
这不是将某个任意 étale 函数称为模形式。

在 $n,n'\ne0$ 的函数域内，定义
$$
 x=A/n,\quad
 \mathcal C=\mathscr D/n^2,\quad
 x_1=A'/n',\quad
 \mathcal C_1=
       \frac{(A')^2-n'A'-2n'F_2'}{(n')^2}.
\tag{10}
$$
直接微分 $n\mathcal C=A^2/n-A-2F_2$ 得
$$
 \boxed{\quad
       (n\mathcal C)'=
             n'\mathcal C_1-\frac{n^2}{n'}(x')^2.
 \quad}
\tag{11}
$$
这里 $x_1-x=(n/n')x'$，所以 (11) 不丢掉导数正规化项。

若在 R141 的原 CM 点 $z$，$n$ 有简单零，且实际二阶行失败，
则 R142 给 $x,\mathcal C$ 都正则；由 (11) 得
$$
                             \mathcal C(z)=\mathcal C_1(z).
\tag{12}
$$
还可选规范的整 AS 坐标 $y=-A'/n'$。
它满足 $\tau y=y+1$，且原正规形中的
$$
 a=A-nA'/n',\qquad a'=-n(A'/n')'.
$$
故在失败处 $a$ 至少有二阶零，而
$$
                          g'(z)=-n'(z)\mathcal C_1(z)/2.
\tag{13}
$$
这识别了实际失败纤维的首个正规 jet，但没有将其假定为零。

## 4. 原 CM 完成中的 Frobenius 标量不能遗漏

现在先在原 $F=\mathbb Q(\sqrt{-7})$ 的一个 split $p$ 完成上计算，
再作 fine-level 的辅助扩张。固定 CM 源曲线及其整代数微分
$\omega_0$ 的约化可在 $\mathbb F_p$ 上取值。令
$$
 A_{c,p}=H(C_c,\omega_0)\in\mathbb F_p^\times,\qquad
 \omega_{\rm ST}=\Omega\omega_0,\qquad
 \Omega^{p-1}=A_{c,p}.
\tag{14}
$$
因此原 $U$ 迹的 Igusa 权二值为 $\Omega^{-2}H_{\rm alg}$，
而不是将 $H_{\rm alg}^p$ 不加因子地识别为 Igusa 的 $p$ 次幂。
取
$$
                          \beta_p=a_p(E)/A_{c,p}^2.
\tag{15}
$$
R141 的非退化条件恰为 $\beta_p\ne1$。
在当前 ordinary 目标输入中也有 $\beta_p\ne0$。

设原 $p$-Artin 元为 $s=\tau^h$。
当它非平凡时，原剩余代数是 $\mathbb F_{p^p}$，
其中算术 Frobenius 准确为 $s$。
原代数微分规范下的完整迹 $H_{\rm alg}$ 属于该域，
所以 (8) 的完成值，除以共同的非零比例
$\ell^{-1}\Omega^{-2}$ 后，是
$$
                          (1-\beta_p\tau^h)H_{\rm alg}.
\tag{16}
$$
当 $s=1$ 时用整个分裂置换代数；此时算术 Frobenius 为恒等，
(16) 的算子为标量 $1-\beta_p$，不把 deck $\tau$ 也设为平凡。
任一种情形，
$$
                  (1-\beta_p s)^p=1-\beta_p
\tag{17}
$$
表明该算子可逆。

令 $\mathcal C_H$ 是对原 $H_{\rm alg}$ 作 (10) 同一种归一
二次不变量。其总迹为单位：由运输微分的权二 Hecke 关系，
它是 $\ell a_\ell f(c,\omega_0)$，R141 的三个因子均为单位。
共同非零比例不改变归一判别式，所以 (16) 给
$$
 \boxed{\quad
     \mathcal C_1(z)=
          \mathcal C_H(z)
            +\frac{\beta_p h^2}{(1-\beta_p)^2}.
 \quad}
\tag{18}
$$
证明不需猜测平方根周期。对任意迹 $v\ne0$ 的向量，若其
归一矩为 $X=U_1/v$、$Y=V_2/v$，则
$$
 \tau^hU_1=U_1-hv,\qquad
 \tau^hV_2=V_2-hU_1+\frac{h(h+1)}2v.
$$
施加 $1-\beta_p\tau^h$ 后，置 $r=\beta_p/(1-\beta_p)$，
新矩为 $X+rh$、$Y+rhX-rh(h+1)/2$。
代入 $X^2-X-2Y$，其变化准确为
$(r^2+r)h^2=\beta_ph^2/(1-\beta_p)^2$，即 (18)。

(18) 先在原完成及原 $\mathbb F_p$ 系数上成立。
作 $p'$ 次辅助常数扩张后可以拉回同一等式；
不能重新把一般底系数的 Frobenius 当成恒等，
或把改变后的算术 Frobenius 仍无说明地写作原 $\tau^h$。

当 $h\ne0$，(18) 的修正项已知非零。
但失败条件只是
$$
       \mathcal C(z)=
       \mathcal C_H(z)+\frac{\beta_ph^2}{(1-\beta_p)^2}.
\tag{19}
$$
前两项是实际未知值，不能从右边的一个非零加项
单独推出原 $\mathcal C$ 有极点。

## 5. 一个保留原剩余作用的精确效力界

以下只检验上述有限模约束的逻辑效力，不构造另一个 newform。
取非平凡原纤维
$\mathcal P=\mathbb F_{p^p}$，使算术 Frobenius 为 $\tau^h$、
$h\ne0$。normal basis 给
$\mathcal P\simeq\mathbb F_p[\Gamma]$，并记
$$
 I=\ker N_\Gamma=\Delta\mathcal P,\qquad\Delta=\tau-1.
$$
因为 $D_2=\tau^2\Delta^{p-3}$，有
$$
 \ker(D_2:I\longrightarrow\mathcal P)=\Delta^3\mathcal P,
                     \qquad \dim\Delta^3\mathcal P=p-3.
\tag{20}
$$
这是 $I$ 中余维 $2$ 的真子空间；其任意元素同时满足
$D_1b=D_2b=0$。它含有非恒定、非零的 $b$，所以
非平凡算术 Frobenius 并不排除二阶失败值。

一阶约束也没有自动消去它。可另选 $b_1\in\mathcal P$
具有规定的非零迹；这样的 $b_1$ 是原正则
$\mathbb F_p[\Gamma]$-模的生成元。
由 (17)，给定其相应整比例后，有唯一
$H_{\rm alg}=(1-\beta_p\tau^h)^{-1}b_1$。
所以实际一阶关系 (16)、总迹导数单位，以及 (20) 中的零阶值
可以在同一个真实剩余 $C_p$ 模上同时满足。

这甚至不与 R145 的 heart 约束冲突。
把 $\mathbb P^1(\mathbb F_\ell)$ 写成原 $\tau^jU$ 块，
在第 $j$ 块各赋值 $\tau^jb/u$，则完整 $U$ 迹为 $\tau^jb$，
且赋值与原 $\tau^h$ Frobenius 相容。
由于 $b$ 非恒定，得到的整个 $G$-几何纤维赋值在
不可约 heart 上不为零；将它及其 $G$-共轭组成评价映射，
其核在 heart 上为零。然而原 Cartan 的 $D_1,D_2$ 行仍都为零。
同样可用 $b_1$ 给第一 jet，保留非零的总迹。

这一计算不声称这些值来自固定的 $E389$ newform，
更不声称实际全部 CM 输入失败。它只准确证明：
原覆盖、完整群环矩、算术 Frobenius、source simple zero、
不可约 heart 及 (16) 的可逆性，本身没有排除原两行 annihilator。
必须继续使用固定 newform 的全 Hecke 特征系统或更强的实际 CM 值
信息。不能把其余几何 Cartan 标记的极点改作原算术点。

## 来源与当前接口

- R137、R139、R141、R142、R145：原全部标签、实际 $Q$、
  微分单位及环类覆盖。本文的所有值始终在这些对象上比较。
- Katz（1977），*A result on modular forms in characteristic p*，
  LNM **601**, 53–61，§II；R141 已核的
  $\partial g_p=f-a_pf^p$ 和 Hasse/Igusa 比例。
- Buium–Poonen（2009），Compositio Math. **145**, 566–602，
  Theorems 3.5、3.17；原去 $p$ 函数与 CM 值识别见 R134、R141。
- J. Saunders（2022），*Cohomology of $\mathrm{PSL}_2(q)$*，
  Journal of Algebra **595**, 347–379，§3；
  本文只沿用 R145 已核的不可约 heart。
- (3)、(7)、(11)、(18) 及 (20) 在本文逐式证明。
  (7) 是真实素于 $p$ 的 coset 迹零；
  尚未将其提升为指定 ordinary CM 点的极点存在。
