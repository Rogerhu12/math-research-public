# 实际固定测试的全部暗对阶乘矩与平方根指数尾

作者：Astra-ISP-789f / boundary_core；AI-assisted，GPT-6 Astra Pro  
日期：2026-11-15

## 0. 同一个实际来源与结论范围

保持原连续远尾
$$
D_x=\sum_{i\ge x}(i+1)^{-2}E_i,\qquad x\ge1,
$$
及原有限 cut 的闭空间 $K_Q\subset V_Q$。独立 head 算子、全部 head 旗、远孔或原总孔 cut 均取原定义。固定有限物理测试 $f$，并取 $x$ 足够大，使 $f$ 在所有远位 $i\ge x$ 上为真空。本文始终使用
$$
v_f=P_{V_Q}f,\qquad k_f=P_{K_Q}f,\qquad
u_f=v_f-k_f.
\tag{0.1}
$$
没有将 $u_f$ 换成热平滑来源，也没有移动原 cut。

选任意一族互不相交的相邻远位对 $\mathcal I$；其左端点均至少为 $x$。每一对记
$$
\theta_i=\log\frac{i+2}{i+1},\qquad
P_i^-=\frac{I-U_i}{2},
\tag{0.2}
$$
其中 $U_i$ 是原物理交换。另令 $A_i^-$ 为该对的一孔空间中下列真 primitive 单位向量的正交投影，在零孔、双孔空间取零：
$$
d_i=
\frac{b_{i+1}e_i-b_i e_{i+1}}
     {\sqrt{b_i^2+b_{i+1}^2}},
\qquad b_i=(i+1)^{-2}.
\tag{0.3}
$$
不同对上的这些投影分别互相交换。定义两种真实暗对计数
$$
N_{\rm phys}=\sum_{i\in\mathcal I}P_i^-,
\qquad
N_{\rm prim}=\sum_{i\in\mathcal I}A_i^-.
\tag{0.4}
$$

对每个整数 $r\ge1$，本文证明
$$
\boxed{
\left\langle\binom{N_{\rm phys}}r u_f,u_f\right\rangle
\le4r!\left(\frac{16}{x}\right)^r\|f\|^2,
}
\tag{0.5}
$$
$$
\boxed{
\left\langle\binom{N_{\rm prim}}r u_f,u_f\right\rangle
\le4r!\left(\frac{25}{x}\right)^r\|f\|^2.
}
\tag{0.6}
$$
常数不含 $Q$、head 幂零阶数 $h$、对数目或其余未改动权。第一阶可继续使用既有更锐的交换行界；新增内容是全部阶乘矩及其尾推论。

这些是实际固定测试的来源约束。$A_i^-$ 不是原 $D_x$ 的约化投影，本文不将它与 $P_{\ker D_x^j}$、真 MP 或顺次 MP 交换。

## 1. 有限组相邻对的真实相似

先固定有限 $S\subset\mathcal I$，$|S|=r$。对 $i\in S$ 只保持该对的几何平均
$$
a_i=\frac1{(i+1)(i+2)}
$$
不变，把两权改成 $a_i e^{t_i},a_i e^{-t_i}$，其中 $0\le t_i\le\theta_i$。其它位的权完整保留。

设
$$
H_i=n_{i+1}-n_i,\qquad
S(t)=\exp\left(\sum_{i\in S}t_iH_i\right).
$$
这些 $H_i$ 自伴、互相交换，且 $\|H_i\|\le1$。逐位零孔、一孔、双孔矩阵直接给
$$
D(t)S(t)=S(t)D(0).
\tag{1.1}
$$
有限乘积 $S(t)$ 及其逆有界。它与独立 head 算子、物理孔 cut 交换，并将各个原 $D(0)$ 幂旗准确送至对应的 $D(t)$ 幂旗。因此，对原空间 $E=V_Q$ 或 $K_Q$，其变权版本准确为
$$
E(t)=S(t)E(0).
\tag{1.2}
$$
这里 $E(0)$ 只平衡所选的有限组对；不是删除其它位或其它 nuisance 后的空间。闭性由 $E(0)$ 闭且 $S(t)$ 有界可逆保持。

当某一个 $t_i=0$ 时，原物理 $U_i$ 与 $D(t)$、head、全部原旗和 cut 交换。故 $E(t)$ 对该自伴酉 $U_i$ 约化。由于 $U_i f=f$，
$$
P_i^-P_{E(t)}f=0\qquad(t_i=0).
\tag{1.3}
$$
这条消失身份对所有其它 $t_j$ 同时成立。

## 2. 正交投影的实参数混合导数

写 $P(t)=P_{E(t)}$。这里只用实参数。由 (1.2) 的有界可逆相似，$P(t)$ 光滑；例如将固定闭子空间 $E(0)$ 的等距嵌入记为 $i_0$，则
$$
P(t)=S(t)i_0
\bigl(i_0^*S(t)^2i_0\bigr)^{-1}
i_0^*S(t).
$$
中间是完整 $E(0)$ 上的正可逆 Gram，没有预先删去任何块。

微分投影及其移动像给
$$
\partial_iP
=(I-P)H_iP+PH_i(I-P)
=H_iP+PH_i-2PH_iP.
\tag{2.1}
$$
令 $a_r$ 为任意 $r$ 次混合导数的统一范数上界，允许先在任意有限参数族上取上确界。$a_0=1$。对 (2.1) 再作 $r-1$ 次导数，Leibniz 公式给
$$
a_r\le2a_{r-1}
+2\sum_{j=0}^{r-1}\binom{r-1}{j}a_j a_{r-1-j}.
$$
归纳得到
$$
\boxed{\|\partial_{i_1}\cdots\partial_{i_r}P(t)\|
\le4^r r!.}
\tag{2.2}
$$
事实上若此前各阶使用 $4^j j!$，右边不超过
$(2+2r)4^{r-1}(r-1)!\le4^r r!$。整个论证与参数族大小及 $S(t)$ 的环境条件数无关，也不需要复参数逆 Gram 的解析半径。

## 3. 物理暗对的多面消失与全部阶乘矩

记 $P_S^-=\prod_{i\in S}P_i^-$。由 (1.3)，向量函数
$$
P_S^-P_{E(t)}f
$$
在每一个坐标面 $t_i=0$ 上均为零。有限维参数盒上的迭代微积分基本定理及 (2.2) 因此给
$$
\|P_S^-P_Ef\|
\le4^r r!\prod_{i\in S}\theta_i\,\|f\|.
$$
对 $V_Q,K_Q$ 各用一次，并保同一个 $f$，可得
$$
\boxed{
\|P_S^-u_f\|
\le2\cdot4^r r!\prod_{i\in S}\theta_i\,\|f\|.
}
\tag{3.1}
$$

互不相交对上的投影可同时对角化，所以先对有限族有
$$
\binom{N_{\rm phys}}r
=\sum_{\substack{S\subset\mathcal I\\|S|=r}}P_S^-.
\tag{3.2}
$$
对无限不交族取有限递增极限，全部项非负，可用 Tonelli。原有限孔 cut 上 $N_{\rm phys}$ 也被远孔数支配，不存在额外无界域问题。由
$$
\theta_i\le\frac1{i+1},
\qquad
\sum_{i\in\mathcal I}\theta_i^2
\le\sum_{i\ge x}\frac1{(i+1)^2}
\le\frac1x,
$$
以及
$$
\sum_{|S|=r}\prod_{i\in S}\theta_i^2
\le\frac1{r!}\left(\sum_i\theta_i^2\right)^r,
$$
将 (3.1) 平方求和，正好得到 (0.5)。没有把每一层或每一组的界再乘 $Q$。

## 4. 真 primitive 暗对也保留

在变权参数下定义
$$
d_i(t_i)=
\frac{e^{-t_i}e_i-e^{t_i}e_{i+1}}
{\sqrt{2\cosh2t_i}},
\qquad A_i^-(t_i)=|d_i(t_i)\rangle\langle d_i(t_i)|.
$$
它在其它局部孔层取零。直接微分单位向量可得
$$
\|(A_i^-)'(t_i)\|
=\|d_i'(t_i)\|
=\frac1{\cosh2t_i}\le1.
\tag{4.1}
$$
而 $A_i^-(0)=P_i^-$。故
$$
\left(\prod_{i\in S}A_i^-(t_i)\right)P_{E(t)}f
$$
仍在每个面 $t_i=0$ 上为零。

各变量只进入其对应的局部投影一次。对这整个乘积作一次遍历 $S$ 的混合导数，Leibniz 和 (2.2) 给
$$
\begin{aligned}
\left\|\partial_S
\left[\left(\prod_{i\in S}A_i^-(t_i)\right)P_{E(t)}f\right]\right\|
&\le
\sum_{j=0}^r\binom rj4^{r-j}(r-j)!\,\|f\|\\
&=
r!\sum_{j=0}^r\frac{4^{r-j}}{j!}\,\|f\|\\
&\le5^r r!\,\|f\|.
\end{aligned}
$$
再次用混合微积分基本定理，得到
$$
\boxed{
\left\|\left(\prod_{i\in S}A_i^-\right)u_f\right\|
\le2\cdot5^r r!\prod_{i\in S}\theta_i\,\|f\|.
}
\tag{4.2}
$$
与 §3 相同的同时对角化和 Tonelli 正好给出 (0.6)。

因此原“每一指定对都取真 primitive 暗向量”的物理子空间受 (4.2) 控制。若之后再施加完整 $P_{\ker D_x^j}$，必须继续保该投影造成的返回；不能把 (4.2) 直接搬到其像。

## 5. 明确尾界和 floor 条件

统一记 $N=N_{\rm phys}$、$\sigma=4$，或 $N=N_{\rm prim}$、$\sigma=5$。对任意整数 $k\ge1$ 和 $1\le r\le k$，上述结论给
$$
\boxed{
\|\mathbf1_{N\ge k}u_f\|^2
\le
\frac{4r!}{\binom kr}
\left(\frac{\sigma^2}{x}\right)^r\|f\|^2
\le
4\left(\frac{\sigma^2r^2}{xk}\right)^r\|f\|^2.
}
\tag{5.1}
$$
最后一步只用 $r!\le r^r$ 和 $\binom kr\ge(k/r)^r$。

若 $1\le k\le x/(4\sigma^2)$，取 $r=k$：
$$
\|\mathbf1_{N\ge k}u_f\|^2
\le4k!\left(\frac{\sigma^2}{x}\right)^k\|f\|^2
\le4^{1-k}\|f\|^2.
\tag{5.2}
$$
特别，每个固定 $k$ 都有 $O_k(x^{-k})$ 的真来源尾界。

若
$$
k\ge\frac{x}{4\sigma^2},
\qquad xk\ge16\sigma^2,
$$
令
$$
r=\left\lfloor\frac{\sqrt{xk}}{2\sigma}\right\rfloor.
$$
此时 $1\le r\le k$，且 $r\ge\sqrt{xk}/(4\sigma)$；(5.1) 中的括号至多 $1/4$。所以
$$
\boxed{
\|\mathbf1_{N\ge k}u_f\|^2
\le
4\exp\left(-\frac{\log4}{4\sigma}\sqrt{xk}\right)\|f\|^2.
}
\tag{5.3}
$$
物理暗对可用 $\sigma=4$，真 primitive 暗对可用 $\sigma=5$。不满足这两个显式分段条件时，(5.1) 和 $\|u_f\|\le\|f\|$ 仍可直接使用。

任意输出孔带投影与这些暗对计数交换，故将 $u_f$ 限制到同一实际 future 带后，以上各右边仍然有效；没有声称可免费把 $\|f\|$ 改成该 future 带自身的范数。

## 6. 与当前原返回目标的准确关系

先前[实际固定测试交换行与同顶部双线性恒等式](R271-appendix-actual-fixed-test-adjacent-swap-row-and-same-top-bilinear-pairing.md)给第一阶行能量。本文保持完全相同的 $f,V_Q,K_Q,u_f$，用真实有限多参数空间变形支付全部不交暗对阶乘矩。

新的控制明显强于只用第一矩所得的 $1/(kx)$ 尾，但它仍未支付所有低暗对数或跨对称方向。原
$$
\mathscr A_n=
\sum_{\substack{1\le j\le h\\a\le n-j\le b}}
D_n^\dagger\cdots D_{n-j+1}^\dagger D^j
$$
不与这些物理计数投影一般交换。本文不据 (5.3) 声称完整 $\mathscr A_nu_{f,n}$、全部两端 partial 或普通右费用已得上界。下一步必须把保留的低暗对分量和真正 MP 返回在同一实际配对中联合支付。


## 7. 真 jet 正交投影后的同源阶乘矩

下面的增强处理“先作完整 primitive 投影”的准确次序，不使用交换投影捷径。

令 $\Pi_j(t)=P_{\ker D(t)^j}$，按实际有限孔直和作用；$j\ge1$ 任意。由 (1.1)，
$$
\ker D(t)^j=S(t)\ker D(0)^j.
$$
所以 $\Pi_j(t)$ 也满足 (2.1)--(2.2)，常数不依赖 $j$。对两个真正正交投影的乘积，混合 Leibniz 给
$$
\begin{aligned}
\|\partial_S[\Pi_j(t)P_{E(t)}]\|
&\le\sum_{\ell=0}^r
\binom r\ell4^\ell\ell!\,4^{r-\ell}(r-\ell)!\\
&=(r+1)4^r r!.
\end{aligned}
\tag{7.1}
$$
在 $t_i=0$ 面上，$\Pi_j(t)$ 和 $P_{E(t)}$ 都与原 $U_i$ 交换，故暗分量仍严格为零。将 §§3--4 原样用于 (7.1)，得到
$$
\boxed{
\left\langle\binom{N_{\rm phys}}r\Pi_j u_f,\Pi_j u_f\right\rangle
\le4(r+1)^2r!\left(\frac{16}{x}\right)^r\|f\|^2,
}
\tag{7.2}
$$
$$
\boxed{
\left\langle\binom{N_{\rm prim}}r\Pi_j u_f,\Pi_j u_f\right\rangle
\le4(r+1)^2r!\left(\frac{25}{x}\right)^r\|f\|^2.
}
\tag{7.3}
$$
其中真 primitive 暗投影的导数和至多
$$
(r+1)r!\sum_{\ell=0}^r\frac{4^{r-\ell}}{\ell!}
\le(r+1)5^r r!.
$$
这证明 (7.3) 的因子，而不是把 (0.6) 与 $\Pi_j$ 交换。

对单个真正正交 jet 差 $F_j=\Pi_j-\Pi_{j-1}$，同样界的右边可取 $16(r+1)^2$ 代替 $4(r+1)^2$。这里没有再求和全部 $j$；高阶矩的全部旗同时求和不由该逐 $j$ 结论免费得到。

例如在 §5 的大 $k$ 条件下，用同一个
$r=\lfloor\sqrt{xk}/(2\sigma)\rfloor$，(7.2)--(7.3) 给
$$
\boxed{
\|\mathbf1_{N\ge k}\Pi_j u_f\|^2
\le4(r+1)^2
\exp\left(-\frac{\log4}{4\sigma}\sqrt{xk}\right)\|f\|^2.
}
\tag{7.4}
$$
这是真正先投完整 jet、再读暗对数的估计，仍无 $j,h,Q$ 因子。

## 8. 原投影 rank-one 见证与合法下降来源的读数

设一个实际物理向量 $h_0$ 在某 $k$ 个指定不交对上都取 (0.3) 的 primitive 暗向量；其余因素任意，并令
$$
\ell=\Pi_1 h_0.
$$
于是 $h_0$ 落在 $N_{\rm prim}\ge k$ 的谱子空间；其余因素可能还含暗对，但 $\ell$ 无须保持该谱子空间。准确地，
$$
|\langle u_f,\ell\rangle|
=|\langle\Pi_1u_f,h_0\rangle|
\le\|\mathbf1_{N_{\rm prim}\ge k}\Pi_1u_f\|\,\|h_0\|.
\tag{8.1}
$$
可直接使用 (7.3) 或 (7.4)。这里完整 primitive 投影一直留在真实次序中；不需要丢掉 $h_0-\Pi_1h_0$。

还可保原实际左链。若 $u_{f,n}$ 是其第 $n$ 远孔层，在合法范围内
$$
D^a u_{f,n}=(-C)^a u_{f,n-a}.
$$
$C$ 只作用独立 head，故与 $\Pi_1$ 和这些暗对计数交换。因此对相应层的同一个 $h_0$，
$$
\begin{aligned}
|\langle D^a u_{f,n},\Pi_1h_0\rangle|
&=|\langle\Pi_1u_{f,n-a},(-C^*)^a h_0\rangle|\\
&\le
\|C^a\|\,
\|\mathbf1_{N_{\rm prim}\ge k}\Pi_1u_f\|\,
\|h_0\|.
\end{aligned}
\tag{8.2}
$$
这保持同一实际 $u_f$ 和完整原左链，不引入任意 primitive 源。

(8.1)--(8.2) 支付的是指定投影见证的实际读数。它们没有估计 $\Gamma^{1/2}\ell$、真多次 MP 提升后的见证或所有其余方向；更不能由一个 rank-one 下界中该读数很小，反推完整 $\Gamma$ 上界。原全 height mixed 返回仍需其余同源方向的联合预算。
