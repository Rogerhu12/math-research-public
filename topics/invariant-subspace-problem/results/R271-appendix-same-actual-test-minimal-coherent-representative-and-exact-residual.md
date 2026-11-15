# R271 附录：原同一固定测试的最小 coherent 代表及准确低阶残量

日期：2026-11-15（UTC）。作者：Astra-ISP-789f / root、boundary_core；AI-assisted，GPT-6 Astra Pro。

**状态：完整证明。** 本文在不改变原实际 $u_f=(P_{V_Q}-P_{K_Q})f$ 的条件下，将同一个远尾真空 forcing 改写为一个显式有限 coherent 列。该列的总范数不增加，完整头逆保持在同一列中；其真实 $(C+D)$ 残量在每层恰是线性占据统计对常数的正交残差。对于原连续尾及 $h\le2x$，其整个残量平方至多 $54x^{-3}\|f\|^2$。

小残量尚未通过原完整返回逆；本文不据此删除 ordinary 封口或帽投影。

依据：[真实 joined 创建来源及完整 forcing Gram](R271-appendix-joined-quotient-coherent-forcing-congruence-and-complete-source-gram.md)；[原强位并头同一顶部](R271-appendix-strong-tail-block-same-top-source-flow-and-exact-two-fee-budget.md)。

## 1. 同一 forcing 的正交代表

沿前稿取
$$
C=A_m+D_<,\quad C^h=0,\quad h=2^m+R,\quad x=m+R,
\qquad D=\sum_{i\ge x}(i+1)^{-2}E_i.
$$
$\mathfrak h$ 包含前 $m$ 个原头位与全部 $R$ 个强尾位；$i_0g=g\otimes\Omega$，其中 $g$ 可为整个 $\mathfrak h$ 中的任意向量。记
$$
\omega_j=(D^*)^j\Omega,\quad
\sigma_j^2=\|\omega_j\|^2=(j!)^2e_j(b^2),\quad
H=\sum_{j=0}^{h-1}\frac{(C^*)^jC^j}{\sigma_j^2}.
\tag{1.1}
$$
所有头矩阵均使用原物理度量；$H\ge I$。

定义完整有限列
$$
\mathcal R_{\rm coh}a
=\sum_{j=0}^{h-1}\frac{(-C)^j a\otimes\omega_j}{\sigma_j^2}.
\tag{1.2}
$$
不同 $j$ 位于正交远孔层，故
$$
\mathcal R_{\rm coh}^*\mathcal R_{\rm coh}=H,\qquad
\mathcal R_{\rm coh}^*i_0=I.
\tag{1.3}
$$
因此
$$
\boxed{
f_{\rm coh}=\mathcal R_{\rm coh}H^{-1}g
=P_{\operatorname{Ran}\mathcal R_{\rm coh}}\,i_0g.}
\tag{1.4}
$$
这是一个真正物理正交投影；$\operatorname{Ran}\mathcal R_{\rm coh}$ 因 $H\ge I$ 而闭。特别
$$
\boxed{
\|f_{\rm coh}\|^2=\langle H^{-1}g,g\rangle\le\|g\|^2,\qquad
\|i_0g-f_{\rm coh}\|^2=\|g\|^2-\langle H^{-1}g,g\rangle.}
\tag{1.5}
$$
$H^{-1}g$ 是整个头空间上的真逆结果，本文没有把它压到原 $g$ 的低头或低强孔支撑。

对前稿的 $P=P_{\mathcal M_q},P_{\mathcal K_t},P_{\mathcal K}$ 或
$P_{\mathcal M_q}-P_{\mathcal K_{q+h}}$，写 $Z=Pi_0$。
前稿已证 $P(D^*)^ji_0=(-1)^jZ(C^*)^j$，所以
$$
P\mathcal R_{\rm coh}=ZH,\qquad
\boxed{P f_{\rm coh}=P i_0g.}
\tag{1.6}
$$
因此不是近似保持 joined／完整来源，而是原物理投影与其完整零源、非零源功能全部相同。

## 2. 原 $V_Q$ 与实际 $u_f$ 的准确保持

这里特意保原总孔截断，而不是把原 $V_Q$ 换成一个新的远孔截断。

令 $N_{\rm tot}=N_<+N_>$ 只计算原第 $m$ 位以后强尾与远尾的总孔；原前 $m$ 位仍属物理头。原
$$
V_Q=\{v:\operatorname{supp}_{N_{\rm tot}}v\le Q,\
P_{N_{\rm tot}<Q}(C+D)v=0\},
\qquad K_Q=V_Q\cap\ker(C+D).
$$
因 $C+D=A_m+D_m$，$(C+D)v$ 对 $v\in V_Q$ 只可能在总孔 $Q$ 层非零。

$C^*$ 作用于强头，而 $D^*$ 作用于远尾，故二者交换。对 $j\ge1$，
$$
(D^*)^j-(-C^*)^j
=(C^*+D^*)\sum_{\ell=0}^{j-1}
(D^*)^{j-1-\ell}(-C^*)^\ell.
\tag{2.1}
$$
右边求和施于 $i_0g$ 后，强孔始终 $\le R$，远孔始终 $\le j-1$。若
$$
j\le Q-R,
\tag{2.2}
$$
它的总孔严格小于 $Q$。因此它与 $(C+D)V_Q$ 正交，得到
$$
\boxed{P_{V_Q}(D^*)^ji_0
=(-1)^j(P_{V_Q}i_0)(C^*)^j,\qquad j\le Q-R.}
\tag{2.3}
$$
此证明没有假设 $V_Q$ 在单独的强头 $C$ 或远尾 $D$ 下不变。

若
$$
\boxed{Q\ge R+h-1,}
\tag{2.4}
$$
则 (2.3) 覆盖 (1.2) 的全部列。$f_{\rm coh}$ 本身也支持在总孔 $\le R+h-1\le Q$。于是
$$
P_{V_Q}f_{\rm coh}=P_{V_Q}i_0g,\qquad
P_{K_Q}f_{\rm coh}=P_{K_Q}i_0g.
$$
所以原实际同一顶部准确保持：
$$
\boxed{
u_g=(P_{V_Q}-P_{K_Q})i_0g
=(P_{V_Q}-P_{K_Q})f_{\rm coh}.}
\tag{2.5}
$$
原 $P_{V_Q}-P_{K_Q}$ 是正交投影，故还得到完整误差平方
$$
\boxed{
\|f_{\rm coh}-u_g\|^2
=\langle H^{-1}g,g\rangle-\|u_g\|^2
\le\|g\|^2-\|u_g\|^2.}
\tag{2.6}
$$
这保留相同 $g,u_g,Q$，没有重新选一个更容易的来源。

同理，前稿的远孔左空间 $V_q^C$ 只需 $q\ge h-1$。若继续使用原内切口的 left+bare／full Riesz 公式，则仍保各自的 $q+h+R\le Q$ 等原窗口条件，不由 (2.4) 省略它们。

## 3. 完整残量的 coherent 部分严格相消

写 $a=H^{-1}g$，并令
$$
E_j=\frac{\|C^j a\|^2}{\sigma_j^2}.
$$
则
$$
\sum_{j=0}^{h-1}E_j=\|f_{\rm coh}\|^2.
\tag{3.1}
$$
在远孔层 $j-1$，$1\le j<h$，原方程残量准确为
$$
\bigl[(C+D)f_{\rm coh}\bigr]_{j-1}
=\frac{(-C)^j a}{\sigma_j^2}\otimes
\left[D\omega_j-\frac{\sigma_j^2}{\sigma_{j-1}^2}\omega_{j-1}\right].
\tag{3.2}
$$
因为
$$
\langle D\omega_j,\omega_{j-1}\rangle=\sigma_j^2,
$$
方括号就是
$$
(I-P_{\mathbb C\omega_{j-1}})D\omega_j.
\tag{3.3}
$$
最高远孔 $h-1$ 上的 $C$ 项因 $C^h=0$ 而为零；$j=1$ 的方括号也为零。这里没有两个独立大项相减后的粗估。

令 $z_i=b_i^2$、$S=\sum_i z_i$。在 $|I|=j-1$ 的物理基上，
$$
(D\omega_j)_I=j!\,b_I\left(S-\sum_{i\in I}z_i\right).
\tag{3.4}
$$
取真实固定大小分布
$$
\mu_k(I)=z_I/e_k(z),\qquad |I|=k,\qquad
W(I)=\sum_{i\in I}z_i.
$$
计数每个 $j$ 子集的 $j$ 个前驱，给
$$
\mathbb E_{\mu_{j-1}}(S-W)
=j\,e_j/e_{j-1}.
$$
故 (3.3) 的系数恰是
$-j!b_I[W(I)-\mathbb E_{\mu_{j-1}}W]$。它是线性占据特征对常数的完整正交残差。这里的低阶特征说明不等于声称原 Moore–Penrose 逆或返回投影保持这个特征空间。

由各输出孔层正交，得到整列的精确能量：
$$
\boxed{
\|(C+D)f_{\rm coh}\|^2
=\sum_{j=1}^{h-1}E_j\,
\frac{e_{j-1}(z)}{e_j(z)}
\operatorname{Var}_{\mu_{j-1}}W.}
\tag{3.5}
$$

## 4. 原连续尾的统一残量界

固定大小乘积权分布有两点负相关。为写清此处只用的范围，删去 $i,j$ 后的对称多项式记为 $a_k$，则
$$
\mathbb P(i\in I)\mathbb P(j\in I)-\mathbb P(i,j\in I)
=\frac{z_iz_j}{e_k(z)^2}
(a_{k-1}^2-a_{k-2}a_k)\ge0.
$$
末号是非负权的标量 Newton 不等式；有限截断成立，固定 $k$ 的非负和极限保留它。因此
$$
\operatorname{Var}_{\mu_k}W
\le\sum_i z_i^2\mathbb P(i\in I)
\le\min\{z_{\max}S,\ k z_{\max}^2\}.
\tag{4.1}
$$
没有使用矩阵 Newton 或跨高度逆序。

每个 $(j-1)$ 子集至多删去最强的 $j-1$ 个权，故
$$
j\,e_j/e_{j-1}
=\mathbb E_{\mu_{j-1}}\sum_{i\notin I}z_i
\ge S_{x+j-1}.
$$
对原 $z_i=(i+1)^{-4}$、$x\ge1$，
$$
S_x\le\frac1{3x^3},\qquad
S_{x+j-1}\ge\frac1{3(x+j)^3},\qquad
z_{\max}=(x+1)^{-4}.
$$
于是 (3.5) 中的系数同时满足
$$
\boxed{
\frac{e_{j-1}}{e_j}\operatorname{Var}_{\mu_{j-1}}W
\le
\min\left\{
\frac{j(x+j)^3}{x^3(x+1)^4},
\frac{3j(j-1)(x+j)^3}{(x+1)^8}
\right\}.}
\tag{4.2}
$$
特别，若 $h\le\kappa x$，则
$$
\boxed{
\|(C+D)f_{\rm coh}\|^2
\le \frac{\kappa(1+\kappa)^3}{x^3}
\langle H^{-1}g,g\rangle
\le\frac{\kappa(1+\kappa)^3}{x^3}\|g\|^2.}
\tag{4.3}
$$
原 $R=d=2^m$ 选择满足 $h=2d\le2x$，所以常数可取 $54$。这只支付真实残量平方；它不是 $\ker(C+D)$ 的距离界。

## 5. 新 forcing 的删除项保留为显式有限列

$f_{\rm coh}$ 不是远尾真空，不能令 $E_if_{\rm coh}=0$。准确公式是
$$
E_if_{\rm coh}
=\sum_{j=1}^{h-1}
\frac{j b_i(-C)^j a}{\sigma_j^2}
\otimes(D_{\ne i}^*)^{j-1}\Omega.
\tag{5.1}
$$
由不同孔层正交，另有完全明确的参考列预算
$$
\boxed{
\sum_{i\ge x}\frac{\|E_if_{\rm coh}\|^2}{i+1}
=\sum_{j=1}^{h-1}E_j\,
\mathbb E_{\mu_j}\sum_{i\in I}\frac1{i+1}
\le\frac{h-1}{x+1}\langle H^{-1}g,g\rangle.}
\tag{5.2}
$$
这是对已明确写出的参考 forcing 列的向量平方和；没有把此前实际 $u_g$ 的标量行预算升级成同样的范数行。

每个 $\omega_j$ 被原加权交换的伴随固定，通常不被交换本身固定。因此，虽然原 $u_g$ 完全相同，不能把旧 far-vac 双缺陷正 Gram 的证明自动改用新的 $f_{\rm coh}-u_g$。实际 $u_g$ 的已付全行继续沿原 $i_0g$ 和原 defect metric 使用；若要换成 (2.6) 的更小 defect，必须保 (5.1) 及所有新的混合项。

## 6. 与真实返回的边界

(2.5) 使所有原 $u_g$ 产生的顶部、内部源以及两端部分和都原样保留；本文没有选择另一条实际链。新的有限 forcing 支持远孔 $<h$，但原完整核、顺次 Moore–Penrose 逆或
$P_{\mathscr E}$ 可能把其影响传到更高孔、更多出生；(3.3) 只定位方程输入，并不宣布输出同样低阶。

尤其 $H^{-1}g$ 的全部强头分量、原普通右最小列的完整零源，以及帽返回的
$P_{\widehat{\mathscr E}}K_{\rm amb}^{-*}$ 都仍须保留。小残量 (4.3) 没有被乘上未经证明的原 Green 上界。本稿付的是相同原测试的一个明确正交代表、实际 $V_Q/K_Q$ 的逐项同余以及整列残量；后续目标仍是这个特定残量或相同测试在真实返回中的联合费用。
