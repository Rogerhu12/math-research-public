# R1058　原 CM 主单位的居中 Q2 Möbius 作用、完整张量与根平均

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

本注从原 GL2 周期变换出发，计算局部 CM 主单位对同一居中
$Q_2$ 展开的真实作用。结论是一个有完整系数运输的互绕关系：
该作用可在包含全部 $\mu_p$ 的明确圆盘上延拓，并与完整根平均
交换。它不等于根平移，不把有限 torus 的阶数相同当作几何识别，
也不由此赋给任何新字中央零或非零。

## 1. 原基、实际 CM 矩阵与全部中心

固定原好惰性 $p>211$，$\delta^2=-3$。使用已经支付的
AMS212 Proposition7.7 原 CM 基，记
$$
 z=z_{\rm dR},\qquad
 z_0=\theta(z)(y)=\frac{2}{1+\delta}=\frac{1-\delta}{2},
 \qquad
 \widehat z_0=\frac{1+\delta}{2}.
 \tag{1}
$$
两数都是 $Z^2-Z+1$ 的根，差为 $-\delta$，在当前 $p$ 为单位。
所有 prime-to-$p$ 图、tame 标记和系数嵌入沿原规范运输。
若在另一个已指定基书写，下面全部矩阵和两个周期须一起共轭，
不能只改一个 torus 标签。

原右作用的完整变换是
$$
 M_g(z)=g^*z=\frac{dz+b}{cz+a},\qquad
 g^*\widehat z=\frac{d\widehat z+b}{c\widehat z+a},
 \qquad
 J_g(z)=\frac{\det g}{cz+a},\qquad
 g^*\omega_{\rm can}=J_g(z)\omega_{\rm can},
 \tag{2}
$$
其中 $g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)$。
$\omega_{\rm can}$ 使用书版正号规范；(2)在 $g=1$ 时是恒等。
同时
$$
 g^*dz=\frac{\det g}{(cz+a)^2}\,dz.
$$
这些式与原 $g_1=\operatorname{diag}(p,1)$、
$g_2=\operatorname{diag}(1,p)$ 的变换完全一致。

取一个真正的 CM 主单位
$$
 t=A+B\delta\in 1+p\mathcal O_{K_p},\qquad
 A\in1+p\mathbf Z_p,\quad B\in p\mathbf Z_p,
$$
并定义
$$
 g_t=
 \begin{pmatrix}
 A+B&2B\\-2B&A-B
 \end{pmatrix}.
 \tag{3}
$$
这里 $\delta$ 的矩阵是
$\left(\begin{smallmatrix}1&2\\-2&-1\end{smallmatrix}\right)$，
其平方为 $-3I$。因此(3)是乘法嵌入，而非单独选择的
阶 $p$ 置换。直接代入给
$$
 a+cz_0=t,\qquad a+c\widehat z_0=\bar t,\qquad
 \det g_t=t\bar t,\qquad
 M_{g_t}(z_0)=z_0,\quad M_{g_t}(\widehat z_0)=\widehat z_0.
 \tag{4}
$$

若需有限 norm-one torus 的主单位商
$T_1=(1+p\mathcal O_{K_p})^1/(1+p^2\mathcal O_{K_p})^1$，
可以取真正 norm-one 的 lift
$$
 t_\lambda=
 \frac{1+(p\lambda/2)\delta}{1-(p\lambda/2)\delta}
 \equiv1+p\lambda\delta\pmod {p^2},
 \qquad \lambda\in\mathbf Z_p.
 \tag{5}
$$
于是 $A^2+3B^2=1$，$\lambda\bmod p$ 参数化 $T_1$。
这些 lifts 在无限级并不组成一个阶 $p$ 的子群；较深主单位仍
对周期 germ 有实际作用。下文对一般(3)成立，特别适用于(5)。

对一般 $g$，若 $h=z-z_0$，必须同时变换中心
$z'_0=M_g(z_0)$，完整差为
$$
 M_g(z_0+h)-M_g(z_0)
 =\frac{\det g}{(a+cz_0)^2}
       \frac{h}{1+\dfrac{c}{a+cz_0}h}.
 \tag{6}
$$
这来自两分式直接相减。只变 $z$ 而固定一个未经运输的中心，
会丢掉本式的常数和分母。

## 2. 居中 Q2 的确切 formal germ

在(1)的同一系数评价后令
$$
 Q=Q_2,\qquad L=\log Q,\qquad h=p^2L,\qquad
 \kappa_t=\frac{\bar t}{t},\quad \beta_t=-\frac{2B}{t},
 \quad D_t(L)=1+\beta_t p^2L.
 \tag{7}
$$
这里 $z_0$、$\widehat z_0$ 是水平系数；系数的实际 pullback
将在下一节保留。由(4)、(6)，完整居中 logarithm 为
$$
 L\longmapsto L_t=\frac{\kappa_t L}{D_t(L)}.
 \tag{8}
$$
所以在 $Q=1$ 的 formal germ 中
$$
 \Phi_t(Q)=\exp\!\left(\frac{\kappa_t\log Q}{D_t(\log Q)}\right),
 \qquad
 \Phi_t(1)=1,\quad \Phi_t'(1)=\kappa_t.
 \tag{9}
$$
(9)目前只是 formal germ，不能在包含根号点的大盘上
逐点代入 $\log\zeta_p=0$。

同一规范下，Hodge 和余切因子分别是
$$
 J_t(L)=\frac{\bar t}{D_t(L)},\qquad
 M_{g_t}'(z)=\frac{\kappa_t}{D_t(L)^2}.
 \tag{10}
$$
还可由原 Legendre 式
$y_{\rm dR}=\widehat z_0/(\widehat z_0-z)$ 直接核出
$$
 g_t^*y_{\rm dR}=D_t(L)y_{\rm dR}.
 \tag{11}
$$
在(11)中 $\widehat z$ 也已按(2)运输，再使用其实际 CM 值
固定为 $\widehat z_0$。没有将两个不同中心的连接系数相等。

## 3. 完整系数运输及权 3+2n 的费用

令 $\mathbf A_{yg_t}(Q_{yg_t})$ 表示实际标记点 $yg_t$ 处
整个有限字向量的展开；它包括原 $p$ 处有限矩阵、全部 tame
词、Artin/Cor 和所选外权。用 $\sigma_t$ 表示这些水平系数沿
真实标记点和原系数嵌入的运输。若选基使有限字行动表现为常矩阵，
该矩阵也属于 $\sigma_t$，不能先删去。

纯 scalar germ 的 pullback 是
$$
 \mathscr P_t\mathbf A(Q)
  =\sigma_t(\mathbf A)\bigl(\Phi_t(Q)\bigr).
 \tag{12}
$$
这不声称 $\sigma_t(\mathbf A)=\mathbf A$。
尤其 $p^2$ 来源通常随 $t$ 改变其实际循环核。

若 $\mathbf A$ 是 $\omega_{\rm can}^{\otimes k}$ 的系数，
真实张量 pullback 的系数为
$$
 \mathscr T_{t,k}\mathbf A
 =J_t(L)^k\,\sigma_t(\mathbf A)(\Phi_t(Q)).
 \tag{13}
$$
反向的 $J_t^{-k}$ 只在已经证明某一完整 section 不变后，
将该不变等式解成 scalar automorphy 时出现。
对新 wild 向量，不能先把不变性当作定义。

对原实际
$\omega_{\rm can}^{\otimes3}\otimes(dz_{\rm dR})^{\otimes n}$，
全部因子是
$$
 J_t^3(M_{g_t}')^n
 =(\det g_t)^{-n}J_t^{3+2n}
 =\bar t^{\,3}\kappa_t^nD_t(L)^{-(3+2n)}.
 \tag{14}
$$
因此仅写 weight $3+2n$ 而删掉 determinant 线，会改变原
KS 规范。norm-one lift 时 $\det g_t=1$，这只是(14)的特例。

还可直接检查连接的两端一致。记
$\mathfrak d_k=\partial_z+k/(z-\widehat z)$；
目标的 $\widehat z$ 也按(2)变换。利用
$$
 M_g(z)-M_g(\widehat z)
  =\frac{\det g\,(z-\widehat z)}
         {(a+cz)(a+c\widehat z)}
$$
和 $\partial_zJ_g^k=-kcJ_g^k/(a+cz)$，逐项得到
$$
 \mathfrak d_k\mathscr T_{g,k}
 =(\det g)^{-1}\mathscr T_{g,k+2}\mathfrak d_k,
 \qquad
 \mathfrak d_3^n\mathscr T_{g,3}
 =(\det g)^{-n}\mathscr T_{g,3+2n}\mathfrak d_3^n.
 \tag{15}
$$
这里 $\mathfrak d_3^n$ 表示权逐次增加 $2$ 的迭代。
(15)保留完整连接，不是把普通导数当作 CM 横向导数。
它与(14)是同一个 tensor 账本。

## 4. 一个确实包含全部 μp 的解析圆盘

以下在 $\mathbf C_p$ 中令 $v_p(p)=1$。取
$$
 r=\frac1{2(p-1)},\qquad
 \mathcal D_r=\{Q:|Q-1|\le p^{-r}\},\qquad
 \ell_0=-\frac{p-2}{2(p-1)}.
 \tag{16}
$$
因为 $r<1/(p-1)$，$\mathcal D_r$ 包含全部 $\mu_p$，
并且在 $Q\mapsto\zeta Q$ 下稳定。

$\log Q$ 在该闭盘为 Tate 解析函数。对其每一项，
$$
 v_p((Q-1)^m/m)\ge mr-v_p(m)\ge\ell_0 .
$$
准确的最小值出现在 $m=p$：写 $m=p^ju$，$u$ 为正整数且
$p\nmid u$，只需比较 $p^jr-j$。从 $j=1$ 往后的差为
$p^j/2-1>0$，而 $pr-1=r-1/2<r$。这证明
$v_p(\log Q)\ge\ell_0$，也证明所用整个 log 尾一致收敛。

由(3)有
$v_p(\beta_t)\ge1$、$v_p(\kappa_t-1)\ge1$。
令
$$
 E_t(L)=\frac{\kappa_t L}{1+\beta_t p^2L}-L
       =\frac{(\kappa_t-1)L-\beta_t p^2L^2}
              {1+\beta_t p^2L}.
 \tag{17}
$$
在整个 $\mathcal D_r$，分母为单位，并且
$$
 v_p(E_t(L))
 \ge\min\{1+\ell_0,\,3+2\ell_0\}
 =\frac p{2(p-1)}>\frac1{p-1}.
 \tag{18}
$$
因此下面的表达式在整个闭盘严格收敛：
$$
 \boxed{\ \Phi_t(Q)=Q\exp(E_t(\log Q)).\ }
 \tag{19}
$$
它在足够小的 $Q=1$ 邻域等于 formal 式(9)，所以是该 germ
的真正解析延拓。且
$v_p(\Phi_t(Q)-Q)\ge p/(2(p-1))>r$，
故它保持 $\mathcal D_r$。对 $t^{-1}$ 作同样估计，形式复合为恒等；
解析唯一性遂给该盘上的逆。没有假设
$\kappa_t\in\mathbf Z_p$，也没有把 $Q^{\kappa_t}$ 断成整个
开单位盘上的有界函数。

式(19)中特意保留外面的 $Q$。在包含 $\mu_p$ 的盘上，
$\exp(\log Q)$ 不能被逐点当作 $Q$ 来使用；原(9)的内层
exponential 不在整个该盘收敛。把 $\log\zeta_p=0$ 直接代入(9)
并得 $1$，不是(9)的解析延拓。

## 5. 与根平均的真正互绕

对 $\zeta\in\mu_p$，有
$\log(\zeta Q)=\log Q$。由(19)、(10)、(14)严格得到
$$
 \boxed{
 \Phi_t(\zeta Q)=\zeta\Phi_t(Q),\qquad
 J_t(\log(\zeta Q))=J_t(\log Q).
 }
 \tag{20}
$$
所有(14)中的 tensor 因子及其倒数也根不变。
特别 $\Phi_t(\zeta)=\zeta$：主单位延拓固定每一个根号点。

在两个实际标记点各自的解析展开空间中定义
$$
 \mathcal R_p A(Q)=\frac1p\sum_{\zeta\in\mu_p}A(\zeta Q),
 \qquad \flat=1-\mathcal R_p.
 \tag{21}
$$
设一个完整运输算子为
$$
 \mathscr U_t A(Q)=m_t(\log Q)\,
                    \sigma_t(A)(\Phi_t(Q)),
$$
其中 $m_t$ 是已经显示的 Hodge/KS 因子或其有限乘积，且全部
水平系数仍由 $\sigma_t$ 运输。若系数运输含 Galois 标记，
它将 $\mu_p$ 置换；真正 norm-one CM lift 更固定该 cyclotomic
层。若含有限字矩阵，该矩阵作为常系数矩阵完整保留。
则从(20)逐项换指标得到
$$
 \boxed{
 \mathcal R_{p,y}\mathscr U_t
   =\mathscr U_t\mathcal R_{p,yg_t},\qquad
 \flat_y\mathscr U_t
   =\mathscr U_t\flat_{yg_t}.
 }
 \tag{22}
$$
这也是 vector-valued 恒等式。其证明只用实际完整平均：
若 $\sigma_t(\zeta)=\zeta'$，$\zeta\mapsto\zeta'$ 置换整套根，
故不必将每个根的系数单独固定。

有界 $Q$ 来源在 $\mathcal D_r$ 上均可评价，(19)保持该盘，
所以(22)适用于本题实际有界输入。这里只证明这个明确圆盘上的
互绕，不加强成任意半径的 Gauss 范数不变。

(22)可以在已经识别的整个有限字空间上与原 torus 投影共同使用，
前提是实际点、系数和 tensor 行动都如(12)--(15)保留。
它没有证明根平均就是 torus 平均，也没有证明每个有限字
经过 flat 后仍非零。任何新增的非水平乘子若不根不变，
须留在整个输入中，不能移过(21)。

## 6. 为何它不是根平移；缺的是哪个实际 branch

非平凡的 $\zeta$ 平移把 $Q=1$ 送到 $\zeta$。
主单位的 centered germ 则由(9)固定 $1$，其线性项为
$\kappa_t=\bar t/t$。对 norm-one 主单位 $t\ne1$，
$\kappa_t=t^{-2}\ne1$。此外(20)还表明该主单位延拓逐点固定
$\mu_p$，而根平移循环这些点。因此两者不能直接相认。
有限商 $T_1$ 的阶数为 $p$ 没有改变这个结论；
不同深层 lifts 对 centered germ 的作用也不同。

实际几何上可以把需要补的图精确定位。这里第一轴正是原
$g_2=\operatorname{diag}(1,p)$ 商核，不是任取后尚待对齐的模型：
书 §3.3 的 (3.5)--(3.6) 取
$g^\vee=\det(g)g^{-1}$，商核由其在 torsion 上的核给出；
Proposition7.18 的证明（印页 211）明确以
$H=\langle\alpha_{\infty,1}\bmod p\rangle$ 书写 $yg_2$。
同一式在作者 2018 原稿 §2.4、印页 18 的 (27) 完整显示。
于是 $(g_2^2)^\vee=\operatorname{diag}(p^2,1)$，所以
$yg_2^2$ 的原循环核恰为
$\langle\alpha_{\infty,1}\bmod p^2\rangle$。
对单位矩阵，真实 right action 是 $\alpha_\infty\mapsto\alpha_\infty g$，
故新第一基向量为 $a\alpha_{\infty,1}+c\alpha_{\infty,2}$。

固定原 $C_1=\langle\alpha_{\infty,1}\bmod p\rangle$；
先作用(3)，再作原 $g_2^2$ 商，给出的循环 $p^2$ 核为
$$
 C_\lambda=
 \left\langle
 (A+B)\alpha_{\infty,1}-2B\alpha_{\infty,2}
          \pmod {p^2}
 \right\rangle .
 \tag{23}
$$
当 $\lambda$ 跑遍 $\mathbf F_p$，$B\equiv p\lambda\bmod p^2$，
这些核两两不同、都有同一个 $C_1$。在
$E_1=E/C_1$ 上，它们是全部 $p$ 条 outward 次级商；
另外一条 degree-$p$ 商是 dual/backtracking 分支。
故这是 conductor-$p^2$ 在固定 conductor-$p$ block 上的
真实野 $p$ 轨道。原完整 finite character 标签可以作用于该轨道，
但其每个自己的 centered $Q$ 都以 $1$ 为中心。

要把这条实际 $p$ 分支迹送成(21)，必须另外构造、规范化并核对：
固定 $C_1$ 的这条 degree-$p$ 对应，在所用 rigid/period
邻域上到一个
$$
 U^p=Q_1
 \tag{24}
$$
Kummer 覆盖的实际映射，连同选择的 branch
$U(C_\lambda)=\zeta_p^{\,\ell(\lambda)}$、
CM reciprocity 的标签 $\ell$、原 level、微分与 coefficient
transport。不能只从阶数判断 $\ell$，也不能令各 centered
coordinate 同时等于这个未居中的 $U$。

等价的可消费要求，是对全部实际来源证明形如
$$
 m_\lambda(Q)\,
 \sigma_\lambda(A_{C_\lambda})(\Phi_\lambda(Q))
   =A_{C_0}(\zeta_p^{\,\ell(\lambda)}Q)
 \tag{25}
$$
的完整回乘恒等式，其中 $m_\lambda$ 保所有真实 Hodge/KS、
有限权和必要的 source 费用。只有在这种同一来源的全式成立后，
其实际加权 CM 迹才能改写为原 root 读者。
若采用另一共同变量消去 $\Phi_\lambda$，其变坐标和
非水平费用同样须支付，不能由(8)只记 log 而删去。

本文不主张(24)--(25)已经构造。已完成且可直接消费的是
(8)--(15)的全部 centered 变换、(19)的合法解析延拓，
以及(22)的完整 root-average 互绕。它们保持 exact-$p^2$
有限字的真实行动，却不替代其临界值的算术比较。

## 7. 原文与已付规范

- D. J. Kriz, *Supersingular p-adic L-functions, Maass-Shimura
  Operators and Waldspurger Formulas*, AMS212 (2021)，
  §4.8--4.9 的 GL2 与 canonical differential 变换，
  (1.7)、(4.44)、(4.48)，Proposition7.7 的实际 CM 基，
  Definitions6.17--6.18 的完整 root 平均。
  [书版原文转录](https://dokumen.pub/supersingular-p-adic-l-functions-maass-shimura-operators-and-waldspurger-formulas-ams-212-9780691225739.html)。
- [2018 原稿](https://arxiv.org/pdf/1805.03605)，
  §2.4、(27) 给 right-action 商核与新基 convention；
  (35)、Proposition3.20 (91) 给同一两个 period 的 Möbius 式。
  本文只从那里核这两个 period 的方向；canonical differential
  与 KS 一律取上面的书版正号规范。
- [原 good/bad 完整来源](../notes/2026-11-27-original-good-pullback-and-bad-source-return.md)
  §§1--3：原 $g_1,g_2$、中心和 raised tensor。
- [实际 flat 与 Bol 读者](R1056-original-flat-amice-critical-slope-and-bol-primitive.md)
  §§1--4：实际 bounded-source、完整根平均与正号 KS。
- [全部循环 CM 层](../notes/2026-11-12-all-cyclic-cm-layers-and-period-newton-polygons.md)
  §§1--3：循环限定、真实 CM 阶与分支运输。

全部为纸笔推导；没有新增数学执行或工作流。
