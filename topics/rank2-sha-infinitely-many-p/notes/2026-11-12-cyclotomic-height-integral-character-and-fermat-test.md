# 实际 cyclotomic 高度的整角色、different 与两个全局 Fermat 商测试

日期：2026-11-12。**已证明；测试的无穷非零性仍未证明。**

本篇固定 R120 的 ordinary 输入：
$E:y^2=x^3-17x$，$F=\mathbb Q(\sqrt{-15})$，
$p\ge13$ 在 $F$ 与 $\mathbb Q(i)$ 均分裂，
$\ell$ 在这两域均惰性且 $v_p(\ell+1)=1$。
令 $L/F$ 为实际环类域中的次数 $p$ 子扩张，
$\Gamma=\langle\tau\rangle$，$Q$ 为 R119 的非挠范数一
Heegner 迹点。记
$$
\mathcal K=\mathbb Q_p(\zeta_p),\quad
\mathcal O=\mathbb Z_p[\zeta_p],\quad
\delta=\zeta_p^{(p-1)/2}(\zeta_p-1),\quad
\vartheta=\delta^2=\zeta_p+\zeta_p^{-1}-2.
                                                               \tag{1}
$$
bar 将 $\zeta_p$ 送到其逆；$\bar\delta=-\delta$。
R119 给实际饱和格
$$
W=A(F)\widehat\otimes\mathbb Z_p=\mathcal O w,
\qquad Q=\delta^a\varepsilon w,
\quad\varepsilon\in\mathcal O^\times.                \tag{2}
$$

本篇另排除固定有限多个整除 $\#\Sha(E^{(-15)}/\mathbb Q)$
的素数；其有限性已由 R103 证明。R123 直接为本篇分裂
ordinary 子族提供相对密度一的合法实际 $Q$；尚未证明
其中无穷多个满足下面的高度矩测试。
R126 的另一组无穷素数不必 ordinary，本篇不假设两组的
交集无穷，也不再需要 R126 的 $a$ 为偶数条件。

## 1. 明确 global norm 与 degree 的高度规范

对 $P\in E(L)$，取与 $p$ 互素的整数 $M$，使 $MP$ 在所有
$v\mid p$ 属于 formal group，并在坏位属于 Néron 恒等组件。
可以用同一个 $M$ 对整个 $E(L)$ 作此操作：$L/F$ 在 $p$
不分歧，$v\mid p$ 的剩余次数是 $1$ 或 $p$；
$$
\#E(\mathbb F_{p^f})\equiv1-a_p^f\equiv1-a_p\not\equiv0\pmod p.
$$
最后一个非零由 $a_p$ 为偶数和 Hasse 界给出。坏位的组件
指数只含 $2,3$ 因子，所以也不需要乘 $p$。

以 $t_E=-x/y$ 为原点参数。对 $v\mid p$，令
$\sigma_v(t_E)\in t_E\mathcal O_{L_v}[[t_E]]$ 为 canonical
ordinary sigma。令 $\mathfrak d(P)$ 为最小模型上
$x(P)$ 的分母理想的平方根，$d_w(P)=\operatorname{ord}_w\mathfrak d(P)$。
本曲线的给定模型在所有有理素数均最小；$L$ 在 $2,17$
不分歧，故这些局部最小模型可兼容使用。

我们使用 raw $\log_p$、再除绝对域次数的二次高度：
$$
H(P)=\frac1{2pM^2}
\left\{
\sum_{v\mid p}\log_p N_{L_v/\mathbb Q_p}\sigma_v(MP)
-\sum_{w\nmid p}d_w(MP)\log_p\#k_w
\right\}.                                           \tag{3}
$$
这里 $[L:\mathbb Q]=2p$，且 $\log_p(p)=0$。
Mazur--Stein--Tate（2006）§§2.7–2.8 的二次高度先用
$\log_p/p$，没有再除域次数。因此其 $h_p$ 与 (3) 准确满足
$H=\tfrac12h_p$，不是相差一个未经计算的 $p$ 因子。
该文的双线性 pairing 与下面的 $h$ 相差 $-4$。

定义
$$
h(P_1,P_2)=\frac{H(P_1+P_2)-H(P_1)-H(P_2)}2.         \tag{4}
$$
这是实际对称、$\Gamma$-不变的双线性高度，且
$h(P,P)=H(P)$。公式 (3) 在改变 $M$ 时不变；这是 global
二次性，不是逐个局部项的二次性。

所有 (3) 花括号中的单项都在 $p\mathbb Z_p$：
对 $v\mid p$，任何 $\mathbb Q_p^\times$ 的 Iwasawa log
属于 $p\mathbb Z_p$；对 $w\nmid p$，$\#k_w$ 是
$p$-单位，$d_w$ 是整数。于是
$$
H(E(L))\subset\mathbb Z_p,\qquad h(W,W)\subset\mathbb Z_p.
                                                               \tag{5}
$$
这已经包括 $[L_v:F_v]=p$ 的不分歧情形。该处 norm 的
log 可以只含一层 $p$，除 (3) 中的 $p$ 后可以是单位；
不能把所有 $p$ 处贡献误删成 $p\mathbb Z_p$。

## 2. 保留所有地方的实际整行

令 $R=MQ$，取上节共同的 $M$，并记 $R_j=\tau^jR$。
$R+R_j$ 均非零：否则 $1+\zeta_p^j$ 会杀掉 (2) 的非零点。
令
$$
U_{v,j}=N_{L_v/\mathbb Q_p}
 \frac{\sigma_v(R+R_j)}{\sigma_v(R)\sigma_v(R_j)},
\qquad
\kappa_{w,j}=d_w(R+R_j)-d_w(R)-d_w(R_j).
$$
对 $x\in\mathbb Q_p^\times$，$\langle x\rangle$ 指删去
$p$ 的幂及 Teichmüller 单位后的 $1+p\mathbb Z_p$ 部分。
则精确公式为
$$
\boxed{
b_j:=h(Q,\tau^jQ)
 =\frac1{4M^2}\left\{
 \sum_{v\mid p}\frac{\log_p\langle U_{v,j}\rangle}{p}
 -\sum_{w\nmid p}\kappa_{w,j}
     \frac{\log_p\langle\#k_w\rangle}{p}
 \right\}.}                                        \tag{6}
$$
每个括号内的量是 $\mathbb Z_p$ 整数。这里没有只保留一个
$p$ 上素位，也没有用 $\operatorname{Tr}\log_E Q=0$ 替换
$\operatorname{Tr}\log\sigma(Q)$。

由实际全局双线性、对称性及 $N_\Gamma Q=0$，
$$
b_j=b_{p-j},\qquad\sum_{j=0}^{p-1}b_j=0.            \tag{7}
$$
这些等式对全局行成立；各地方的部分不必分别满足第二式。

## 3. 原辅助位的单位项在非平凡角色中准确消失

现在另用 R114/R123 对所选实际 $\ell$ 的首 jet：
$$
v_\ell t_E(2Q)=1/p.
$$
令 $M=2m$。在 $L_\lambda$ 中采用整数值赋值 $v_\lambda$，
$v_\lambda(\ell)=p$，则
$$
n:=v_\lambda t_E(R)=1+p\,v_\ell(m).                 \tag{8}
$$
这里可以使用 formal log：$1/p>1/(\ell-1)$，乘整数时
log 与参数保持同赋值。$L_\lambda/F_\lambda$ 为 tame
次数 $p$ 扩张，惯性在一致化元上的首特征是一个 primitive
$p$ 次根 $\xi$。因为 $n\equiv1\pmod p$，
$$
t_E(R_j)\equiv\xi^j t_E(R)
 \pmod{\mathfrak m_{L_\lambda}^{n+1}}
$$
（同时改变生成元只置换 $j$）。$p$ 为奇数，所以
$\xi^j+\xi^k\ne0$，包括 $j=k$。formal group 的整加法给
$$
d_\lambda(R_j)=d_\lambda(R_j+R_k)=n
\qquad\text{对所有 }j,k.                            \tag{9}
$$

固定上述 $M$，将 (3) 在这个地方的局部函数写为
$\Lambda_\lambda(S)=-d_\lambda(S)\log_p\#k_\lambda/(2pM^2)$。
注意 $S$ 取已经乘过 $M$ 的 $R_j$ 及其和。由 (9)，
这些局部函数值都等于
$$
\lambda_0=-\frac{n\log_p\ell}{pM^2},
\qquad v_p(\lambda_0)=0.                             \tag{10}
$$
用的是 $\#k_\lambda=\ell^2$ 及
$v_p\log_p\ell=v_p(\ell+1)=1$。

但实际极化局部矩阵是
$$
\frac{\Lambda_\lambda(R_j+R_k)-\Lambda_\lambda(R_j)-\Lambda_\lambda(R_k)}2
 =-\lambda_0/2,                                     \tag{11}
$$
即一个常数矩阵。因此对每个非平凡 $\chi$，其 Fourier
系数准确为零，特别是
$$
\sum_{j=0}^{p-1}b_j^{(\lambda)}\zeta_p^j=0.          \tag{12}
$$
(11) 是对全局极化公式的逐位分解，不是断言单个 Néron
局部函数已经定义在 Mordell--Weil 群上且双线性。
这正说明为什么 (10) 的单位不能直接当成目标 regulator
的首单位项。所有 $p$ 处及其余位仍须保留在 (6) 中。

## 4. different 与准确的整角色高度

R120 的秩一迹形式给唯一的 $c_Q\in\mathcal K^+$，使
$$
h(xQ,yQ)=\operatorname{Tr}_{\mathcal K/\mathbb Q_p}
             (c_Qx\bar y).                          \tag{13}
$$
由 Fourier 正交性直接得到
$$
\sum_{j=0}^{p-1}b_j\zeta_p^j=p c_Q.                 \tag{14}
$$
这不是把未正规化角色和除 $p$ 后仍称为整格。

对饱和基 $w$ 定义同样的 $c_w$。由 (5)，
$c_w\in\mathfrak D^{-1}_{\mathcal K/\mathbb Q_p}$。
$\Phi_p'(\zeta_p)=p\zeta_p^{-1}/(\zeta_p-1)$ 给
different 的 $\delta$ 指数 $p-2$。另一方面
$c_w\in\mathcal K^+$ 的 $\delta$ 赋值为偶数，所以
$$
v_\delta(c_w)\ge-(p-3).
$$
因此准确的整对象是
$$
\boxed{\quad
\mathcal R_Q=\frac{\sum_jb_j\zeta_p^j}{\delta^2}
            =\frac{p c_Q}{\delta^2}\in\mathcal O^+.
\quad}                                               \tag{15}
$$
它与真实点指数满足
$$
\mathcal R_Q=(-1)^a\delta^{2a}\varepsilon\bar\varepsilon
                  \mathcal R_w,
\qquad
v_\delta\mathcal R_Q=2a+v_\delta\mathcal R_w.         \tag{16}
$$
R120 给 $\mathcal R_w\ne0$，并未给它是单位。

若在 $\mathcal O$ 的标准 $\mathbb Z_p$ 基上计算 Gram
determinant，trace discriminant 的赋值为 $p-2$，bar
在整基上的 determinant 是单位，而 norm 的赋值为
$v_pN(c_w)=v_\delta(c_w)$。故
$$
v_p\operatorname{Reg}_h(W)=1+v_\delta\mathcal R_w,
\qquad
v_p\operatorname{Reg}_h(\mathcal OQ)
 =1+2a+v_\delta\mathcal R_w.                          \tag{17}
$$
这个规范下 regulator 至少含一层 $p$ 是 different 与
对称性的必然结果，不能把“regulator 是单位”当成正确门槛。

## 5. 两个实际低矩检测 δ 指数是否小于二

令 $d=(p-1)/2$。由 (7)，
$$
\mathcal R_Q=
 \sum_{j=1}^{d} b_j
 \frac{\zeta_p^j+\zeta_p^{-j}-2}{\vartheta}.          \tag{18}
$$
分式是 $\vartheta$ 的整系数多项式。由
$C_0=2,C_1=2+\vartheta$、
$C_{j+1}=(2+\vartheta)C_j-C_{j-1}$，或直接归纳，有
$$
\frac{C_j-2}{\vartheta}
 =j^2+\frac{j^2(j^2-1)}{12}\vartheta+O(\vartheta^2).
                                                               \tag{19}
$$
因为 $p\ge13$，$12$ 是单位，且
$p\in\vartheta^{d}(\mathcal O^+)^\times$，$d\ge3$。
因此 (18) 模 $\vartheta^2$ 的前两系数可以分别模 $p$
读取。定义
$$
S_2=\sum_{j=1}^{d}j^2b_j\pmod p,
\qquad
S_4=\sum_{j=1}^{d}j^4b_j\pmod p.                     \tag{20}
$$
则严格有
$$
(S_2,S_4)\ne(0,0)
\quad\Longleftrightarrow\quad
v_\delta\mathcal R_Q<4.                             \tag{21}
$$
结合 (16)，它给 $a\le1$。事实上，这已经足以消去原曲线
的 $p$ 初级 Sha，**不必先知 $a$ 为偶数，也不必假设
$r_-=1$**。给出完整证明如下。

记 $S=\Sha(A/F)[p^\infty]$，
$d_p=\dim_{\mathbb F_p}\Sha(E/\mathbb Q)[p]$。
删去开头的固定有限集后，R122 给
$$
s_-=1,\qquad s_+=2+d_p,\qquad
\dim S[\delta]^\pm=s_\pm+1-2r_\pm
                     -\mathbf1_{\{\pm=(-1)^a\}}.
$$
R125 则给 $\operatorname{length}_{\mathcal O}S\le2a$。

- 若 $a=0$，则 $S=0$。负号公式迫使 $r_-=1$；正号公式
  为 $0=2+d_p-2r_+$，所以 $r_+=1$、$d_p=0$。
- 若 $a=1$，实际 Mordell--Weil Kummer 线是负号。
  负号公式为 $\dim S[\delta]^-=1-2r_-\ge0$，故
  $r_-=0$，该维数为 $1$。正号维数为
  $3+d_p-2r_+\ge1+d_p$，所以
  $$
  2+d_p\le\dim_{\mathbb F_p}S[\delta]
          \le\operatorname{length}_{\mathcal O}S\le2.
  $$
  因而仍有 $d_p=0$、$r_+=1$。这个分支允许
  $S\simeq(\mathcal O/\delta)^2$；没有错误地声称
  $\Sha(A/F)[p^\infty]=0$。

两种情形均给 $\Sha(E/\mathbb Q)[p]=0$，从而
$$
\Sha(E/\mathbb Q)[p^\infty]=0.                       \tag{22}
$$
其中 **$a\le1\Rightarrow(22)$ 本身只用 R122、R125**，故在
删去同一固定有限集后，对任意充分大的好素数均成立；
ordinary 及 $p$ 在 $F$ 分裂仅用于本篇前面的高度测试。
结合 R128 的完整整数像比较，实际条件
$Q\notin(\sigma_{\mathfrak b}-1)^2A(F)$ 已经充分，
不需要先排除一次差分像。
这是充分测试。即使 $a=0$，$\mathcal R_w$ 也可能有更高
赋值，因而不能把 (21) 反向写成主目标的必要条件。

## 6. 前两矩只需实际有理范数的 Fermat 商

本节保留全部 $p$ 处 norm，把 (20) 写成纯有限精度数据。
先令 $P$ 在全部 $p$ 处 formal、在坏位属于恒等组件。
因为 $L/\mathbb Q$ 在 $p$ 不分歧，
$t_E(P)\in p\mathcal O_{L_v}$。ordinary sigma 是奇的整
级数，故
$$
\sigma_v(t_E(P))/t_E(P)\in1+p^2\mathcal O_{L_v}.
$$
所以其 log norm 属于 $p^2\mathbb Z_p$，除 (3) 中的
$2p$ 后是 $p\mathbb Z_p$。

定义实际有理数
$$
\nu(P)=\frac{N_{L/\mathbb Q}t_E(P)}
                 {N_{L/\mathbb Q}\mathfrak d(P)}\in\mathbb Q^\times.
                                                               \tag{23}
$$
在 $p$ 上，$v_wt_E(P)=d_w(P)$，故 $\nu(P)$ 是
$p$-单位。所有 $v\mid p$ 的 norm 的乘积等于全局 norm；
分母理想的 $p$ 因子在 Iwasawa log 中为零。于是准确有
$$
H(P)\equiv\frac1{2p}\log_p\nu(P)\pmod p.           \tag{24}
$$
该公式没有把某个 $p$ 上素位单独当成全局 norm。

对 $R=MQ$，$\nu(R_j)=\nu(R)$，所以
$$
b_j\equiv\frac1{4M^2p}\log_p
 \left(\frac{\nu(R+R_j)}{\nu(R)^2}\right)\pmod p.
                                                               \tag{25}
$$
若 $z\in\mathbb Q^\times$ 为 $p$-单位，记
$$
q_p(z)=\frac{z^{p-1}-1}{p}\pmod p.
$$
此式按分子、分母均模 $p^2$ 计算。因
$\log_p z/p\equiv-q_p(z)\pmod p$，(25) 等价于
$$
\boxed{\quad
b_j\equiv-\frac1{4M^2}
 q_p\!\left(\frac{\nu(R+R_j)}{\nu(R)^2}\right)\pmod p.
\quad}                                               \tag{26}
$$
从而 (20) 是两个明确的有理数 Fermat 商加权和，不需先
近似整条 sigma 级数。式 (23) 的点和数域随 $(p,\ell)$
变化；本篇没有将这些数说成固定底数。

## 7. 用真实 Frobenius 群环单位避免巨大整数倍

可以不用 $\#E(\mathbb F_{p^p})$ 这样的巨大整数来使点
在 $p$ 处 formal。令 $s\in\Gamma$ 为 $F$ 中一个
$p$ 上素位的算术 Frobenius，另一素位的符号为 $s^{-1}$。
置
$$
D=(s^2-a_ps+p)(s^{-2}-a_ps^{-1}+p)\in\mathbb Z[\Gamma].
                                                               \tag{27}
$$
在第一个 $p$ 上素位，$s$ 在约化点上就是算术
$\mathbb F_p$-Frobenius；其特征多项式
$X^2-a_pX+p$ 给第一因子杀约化。第二个素位用第二因子。
因此 $DQ$ 在所有 $p$ 处 formal。

此外
$$
D\equiv(1-a_p)^2\ne0\pmod{(p,\tau-1)},
$$
故 $D$ 在 $\mathbb Z_p[\Gamma]$ 及 $\mathcal O$ 中均为
单位。潜在好约化的几何组件指数被 $12$ 杀掉，所以
$$
R=12DQ                                                  \tag{28}
$$
同时满足全部 formal／恒等组件条件，且它在实际
$\mathcal O$ 格中的指数仍准确为 $a$。
此处使用了真正的有限域 Frobenius 作用，没有把 $D$
冒充一个特征零局部 Frobenius 同源。

因此可以直接用 (23)、(26) 对点 $R$ 取 $M=1$，再将
(20)–(21) 应用于 $R$。它的整角色高度与 $Q$ 的关系为
$$
\mathcal R_R=12^2D(\zeta_p)D(\zeta_p^{-1})\mathcal R_Q,
$$
右边乘的是 $\mathcal O^+$ 单位，所以赋值和 $a\le1$
测试不变。具体而言，令
$$
z_j=\frac{\nu(R+\tau^jR)}{\nu(R)^2}.
$$
删去开头的固定有限集后，下面的有限数据条件已经足以推出
(22)，不需额外的奇偶或 $r_-$ 假设：
$$
\boxed{\quad
\left(\sum_{j=1}^{d}j^2q_p(z_j),
       \sum_{j=1}^{d}j^4q_p(z_j)\right)\ne(0,0)
       \quad\text{于 }\mathbb F_p^2.\quad}            \tag{29}
$$

这一替换也有可控的 archimedean 成本：
$\|D\|_1\le(p+|a_p|+1)^2\le(\sqrt p+1)^4$，故
$$
\widehat h(R)\le144(\sqrt p+1)^8\widehat h(Q).
$$
这里只声称多项式成本和准确的整格单位，不声称 (29)
会自动非零。

## 8. 固定 61 进非零与真正剩余条件

R116 的固定 $q=61$ Mellin 非恒零给一族固定代数 jet 的
非零性及其在辅助 $\ell$ 处的单位证书。它没有给 (29)
中的 $p$ 进 Fermat 商非零。

一个准确的整格区别是：对 $p\ne61$，
$$
N_{\mathbb Q(\zeta_p)/\mathbb Q}(\zeta_p-1)=p
$$
为 $61$-单位。因此 $\delta$ 在
$\mathbb Z_{61}[\zeta_p]$ 的每个局部因子中可逆；指数
$a$ 的整个 $p$-初级差别在这个固定局部完成中消失。
所以单凭该处的非零或单位性，不能将 (16) 的 $a$
判成零。这不排除一个新的全局可除性比较，但这样的比较
尚未由 R116 构造。

本篇的实际剩余输入已具体化为 (29) 的两个全局有理数
Fermat 商和在无穷合法 ordinary $p$ 中至少一个非零。
$a=2$ 时 (16) 允许两者同为零；高度非退化、
$\widehat h(Q)=o(p)$ 及原辅助位的单个单位项都没有排除它。

## 一手来源

- B. Mazur, W. Stein, J. Tate, *Computation of p-Adic Heights and Log
  Convergence*, Documenta Mathematica, Extra Volume Coates (2006),
  585–622；[作者全文](https://wstein.org/papers/pheight/pheight.pdf)。
  Theorem 1.3 给 ordinary sigma 的奇整规范；§§2.3–2.8，
  印页 592–595，给全部地方的 norm、分母项及 $\log_p/p$
  规范。本篇 (3)–(6) 已逐项转换其 degree 与 polarization 因子。
- R119、R120：实际秩一 $\mathcal O$ 格和 cyclotomic 高度非退化。
- R122、R125：真实局部符号及统一指数界，联合给 $a\le1$
  已足以消去原曲线 $p$ 初级 Sha。
- R114、R123：实际辅助位的首 jet 及本篇 ordinary 子族中
  相对密度一的合法输入；本篇不假设 R126 的无穷素数自动
  落入 ordinary 子族。
