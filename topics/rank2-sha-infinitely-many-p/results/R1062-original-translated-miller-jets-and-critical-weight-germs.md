# R1062 — 原 translated Miller jets 的完整 Newton 族与临界权 germ

日期：2026-11-28 UTC。会话 Astra-rank2-Sha-0b097461-20261127。

按根 README 第8条登记完整证明。主目标仍未完成。

本文的(C1)–(C19)、D/E/F编号及第21、22节，均指[R1061](R1061-original-p-square-antilinear-gluing-and-full-theta-descent.md)；这里保留G编号以便接续实际全来源。

本节接(C1)--(C19)、§21的真实野字，以及§22的 marked whole
germ。先证明每个真实 translated section 的全阶解析恒等式；
再在已经完成实际 graded 运输的双槽中使用。这里的参数解析
不是旧 usual/flat factorial cross，也不把单项的非零直接传给
原 $\mathfrak T_{\rm orig}$ 或 canonical $J'_S$。

## 1. 固定 $Z_Q$ 的指数与全部连接高项

写
$$
 \Delta=p^2-1,\qquad \tau=\frac p\Delta,\qquad
 \eta=1-\frac1{p-1}.
$$
取(C2)的同一原 section $s_N=\sigma^N R_N$，假设 $R_N$
仅在原点有极，且在当前 good 模型的全部系数整；原 section $s_N$ 的首项为 $a_0z^a$，
$a_0$ 在当前位为单位，且 $p\nmid N$。
对本篇 canonical 两源分别是 $(N,a)=(102,4),(34,6)$。
原固定 raw 幅度始终另按其实际值乘入。
取非零 $Q\in E[p]$ 和同一原 theta lift，置
$$
 B_{N,Q}=b_{N,\widetilde Q}R_N(Q),\qquad
 A_{N,Q}=N Z_Q.
$$
$B_{N,Q}$ 保全部原中心；$Z_Q$ 仍是(C1)的实际代数值。
物理参数 $z$ 中的原 translated germ 唯一写为
$$
 \boxed{\quad
 {\cal S}_{N,Q}(z)
    =B_{N,Q}e^{A_{N,Q}z}V_{N,Q}(z),\qquad
 V_{N,Q}(0)=1 .
 \quad}                                                     \tag{G1}
$$
这是特征零形式恒等式，并在原足够小的 Lie 盘成立。
其非指数部分有不含未定 quasi-period 的完整表达
$$
 V_{N,Q}(z)=
 \frac{R_N(Q+z)}{R_N(Q)}
 \exp\!\left(
   -N\sum_{r\ge2}\frac{D^{r-2}x(Q)}{r!}z^r
 \right).
 \tag{G2}
$$
这里 $Q+z$ 指原不变微分的局部 Taylor 展开。
由于 $D(\zeta(q+z)-\eta_Q)=-x(q+z)$，
(G2)保留所有 $DZ=-x$ 及其后继；没有在(C2)中把 $Z$
当作导数为零的函数。只是(G1)抽出了在中心取值的那个常数
$NZ_Q$。原 $p$ 覆盖参数仍是 $z=pz'$。

## 2. 完整 Bell 极帽及 Tate 收敛

记 $v_k=D_z^kV_{N,Q}(0)$，所以 $v_0=1$。
在求值于 $Q$ 以前，$D^jR_N$ 的极阶至多 $N-a+j$，
而 $D^{r-2}x$ 的极阶至多 $r$。
指数的第 $k$ 个未除幂导数是这些量的整 Bell 多项式：
每项各输入次数之和恰为 $k$，系数为整数。
Leibniz 公式再与 $R_N(Q+z)$ 相乘，因此
$$
 \boxed{\quad v_p(v_k)\ge-\frac k\Delta\qquad(k\ge0).\quad}
 \tag{G3}
$$
这里用到原 good 参数 $w=x^{-1/2}$ 下
$v_p(R_N(Q))=-(N-a)/\Delta$。
其首 Laurent 系数为单位，较低极阶项严格较深，故此分母
的估值准确；没有由仅上界倒推相等。
所有微分在求值前完成，所以不在 reduced torsion 代数中
非法继续求导。整数 Bell 系数也说明(G3)对任意大的 $k$
成立，不受 $k!$ 中的 $p$ 进位限制。

定义
$$
 a_{N,Q,k}=A_{N,Q}^{-k}v_k,\qquad
 {\cal F}_{N,Q}(X)=
    \sum_{k\ge0}\binom Xk\,a_{N,Q,k}.
 \tag{G4}
$$
由(C13)，$v_p(A_{N,Q})=-1+\tau$，故
$$
 v_p(a_{N,Q,k})
 \ge k\left(1-\tau-\frac1\Delta\right)
 =k\eta.
 \tag{G5}
$$
以 $X$ 的 ordinary monomial Gauss 范数计算，
$\binom Xk$ 的系数估值至少 $-v_p(k!)$。于是
$$
 k\eta-v_p(k!)\longrightarrow+\infty,\qquad
 k\eta-v_p(k!)\ge\eta\quad(k\ge1).
$$
最后不等式可直接用 $v_p(k!)\le(k-1)/(p-1)$；
当前 $p>211$。
因此在包含原 division-field 数据的完备赋值域 $L$ 中，
$$
 \boxed{\quad
 {\cal F}_{N,Q}\in1+\mathfrak m_L^{\ge\eta}
                    \mathcal O_L\langle X\rangle,\qquad
 {\cal F}_{N,Q}^{-1}\in
          1+\mathfrak m_L^{\ge\eta}\mathcal O_L\langle X\rangle .
 \quad}                                                     \tag{G6}
$$
记号 $\mathfrak m_L^{\ge\eta}$ 表示估值至少 $\eta$，
不要求 $p^\eta$ 已选在域中。
这里是真正 unit Tate 盘上的一致收敛，不只是
$X\in\mathbf Z_p$ 时二项式值整。
同一 Gauss 界还控制 $\mathcal F'$ 的全部系数。

对所有整数 $m\ge0$，(G1)的有限 Leibniz 和准确给
$$
 \boxed{
 \begin{aligned}
 D_z^m{\cal S}_{N,Q}(0)
   &=B_{N,Q}A_{N,Q}^m{\cal F}_{N,Q}(m),\\
 D_{z'}^m{\cal S}_{N,Q}(pz')(0)
   &=p^m B_{N,Q}A_{N,Q}^m{\cal F}_{N,Q}(m).
 \end{aligned}}
 \tag{G7}
$$
这是(C5)的全阶重写；没有只留下最高 $Z^m$ 项。
特别
$$
 \begin{split}
 {\cal F}_{N,Q}(0)&=1,\\
 {\cal F}_{N,Q}(-2)
   &=1+\sum_{k\ge1}(-1)^k(k+1)a_{N,Q,k}
      \in1+\mathfrak m_L^{\ge\eta}.
 \end{split}                                                \tag{G8}
$$
因此这个明确的局部负二函数值是单位。
它尚未被命名为原全局 Coleman primitive：
局部二次积分的常数与一次项、以及实际 whole 读者的
归一，仍须由同一原来源返回确定。


## 3. 两槽先合并，再支付 period 和单位底数

以下精确记录一个已经回到同一物理 frame 的代数双字。
记负、正 section 为 $\mathcal S_{-,Q}$、
$\mathcal S_{+,\gamma Q}$，其中 $\gamma=\gamma_{102,p}$ 是
原反线性图；两条三挠词已完整包含在负102源中。
若该实际 graded 运输给
$$
 c_0\,{\cal S}_{-,Q}(\ell_-Z)
              {\cal S}_{+,\gamma Q}(\ell_+W),
$$
则 $c_0,\ell_\pm$ 必须是该运输已经支付的非零常数；
系数为零的字直接保为零，不套下方非零结论。
复 $\gamma_i$、Hermite 参数和 rank-one 复周期先按
R1060(9)--(11)完成整槽代数化，不能分别嵌入 $\mathbf C_p$
来定义这些数。不能给尚未完成此运输的 $h$ 被积函数
自由添一组 $c_0,\ell_\pm$。

仍用该原基字的
$\Omega,\kappa,\rho=(17/2)p^2\kappa\Omega^2$，
并保(C18)的真实 $p^{-2}$。
这个字的完整未除幂双槽是
$$
 {\cal R}_{Q,n}
 =\frac{c_0}{p^2}\Omega^3\rho^n\ell_-^n\ell_+^{n+2}
 D^n{\cal S}_{-,Q}(0)
 D^{n+2}{\cal S}_{+,\gamma Q}(0).
 \tag{G9}
$$
若先在 $p$ 覆盖上计算，则两个导数多
$p^{2n+2}$；R1060(12)、(45)给同一个 unflat reader 的
额外变量因子 $p^{-2}(\rho/p^2)^n$。
这是(46)在完整 Maass 变换以前的同一变量缩放。
两者准确恢复(G9)，不多乘或少乘一次 graph Haar $p^{-2}$。

令 $A_\pm,B_\pm,\mathcal F_\pm$ 表示上述真实两点的
(G1)--(G4)，置
$$
 \begin{aligned}
 {\cal C}_Q
   &=p^{-2}c_0\Omega^3 B_-B_+
                     (\ell_+A_+)^2,\\
 {\cal U}_Q&=\rho\,\ell_-\ell_+A_-A_+ .
 \end{aligned}
$$
于是(G7)完整给
$$
 \boxed{\quad
 {\cal R}_{Q,n}
   ={\cal C}_Q{\cal U}_Q^n
          {\cal F}_-(n){\cal F}_+(n+2)
       \qquad(n\ge0).
 \quad}                                                     \tag{G10}
$$
这一步才合并全部非单位 period。
在原 maximal-CM/单位标记的范围
$v_p(\Omega)=-\tau$、$v_p(\kappa)=0$，有
$$
 \begin{split}
 v_p({\cal U}_Q)&=v_p(\ell_-\ell_+),\\
 v_p({\cal C}_Q)
  &=v_p(c_0)+2v_p(\ell_+)-4
                    +\frac{a_-+a_+-p}{\Delta}.
 \end{split}                                                \tag{G11}
$$
对指定 canonical seed，$a_-+a_+=10$。
因此若实际运输已给 $v_p(\ell_-\ell_+)=0$，
底数 $\mathcal U_Q$ 是单位，即使两个单独 slot 的 period
都不是单位。若实际 frame 不是这一范围，保(G9)--(G10)
及其真实估值，不套(G11)或偷偷将 $\ell_\pm$ 置一。

## 4. 同一个合法子列、全部根单位与解析盘

固定有限个已经按(G9)支付的实际字，且其
$\mathcal U_Q$ 都是单位。它们可以在 $\mathbf C_p^\times$
中，未必在 $\mathbf Z_p^\times$；这里不构造一份新的
$\mathbf Z_p$ bounded measure。

每个单位的 residue 属于 $\overline{\mathbf F}_p^\times$，
阶有限且与 $p$ 互素。取一个共同的 prime-to-$p$ 整数 $D$，
同时倍于这些阶和 R1059 原合法有限/Teich 分量的
prime-to-$p$ 周期。
再取一个共同 $e$，支付原有限分量的全部 $p$ 部分，
并使每个 $\mathcal U_Q^{Dp^e}$ 都进入 exponential 收敛盘。
这一步同时处理 principal part 中可能存在的 $p$ 幂根单位；
只清 residue 的 Teich 部分不够。

在 $j+2\in p^e\mathbf Z_p$ 上，按当前 $-2$ 分量定义
$$
 {\cal U}_Q^{[-2]}(j)
  ={\cal U}_Q^{-2}
       \exp\bigl((j+2)\log{\cal U}_Q\bigr).
 \tag{G12}
$$
必要时共同增大 $e$，使
$e+v_p(\log\mathcal U_Q)>1/(p-1)$ 对所有非零 log 成立。
这里 $\log$ 杀全部根单位，但外面的
$\mathcal U_Q^{-2}$ 保实际整数基点的值。
对任意这个盘中的 $j$，可选同一合法分量的非负整数
$n_\ell\to j$，并在所有有限字上共同取子列，使
$\mathcal U_Q^{n_\ell}\to\mathcal U_Q^{[-2]}(j)$。
在 $j=-2$ 可取 $n_\ell=-2+Dp^\ell$，$\ell$ 足够大；
一般 $j$ 用同时模 $p^\ell$ 和模 $D$ 的整数逼近。
根单位部分以及足够深的 principal-power 部分分别稳定。
没有为每个 $Q$ 选择互不相容的权分量，也不插值 $p^n$。

故(G10)给该实际字的明确解析 germ
$$
 \boxed{\quad
 {\cal R}_Q(j)
  ={\cal C}_Q{\cal U}_Q^{[-2]}(j)
      {\cal F}_-(j){\cal F}_+(j+2).
 \quad}                                                     \tag{G13}
$$
该式是同一正整数 jet 的合法极限，而非定义一个不相干的
权函数。在基点，
$$
 \begin{aligned}
 {\cal R}_Q(-2)
  &=\frac{c_0\Omega^3}{p^2\rho^2\ell_-^2}\,
       B_-B_+ A_-^{-2}{\cal F}_-(-2),\\
 {\cal R}'_Q(-2)
  &={\cal C}_Q{\cal U}_Q^{-2}
    \left[
       {\cal F}'_-(-2)
       +{\cal F}_-(-2){\cal F}'_+(0)
       +{\cal F}_-(-2)\log{\cal U}_Q
    \right].
 \end{aligned}                                             \tag{G14}
$$
正槽确实回它的实际 translated value $B_+$，
因为 $\mathcal F_+(0)=1$；负槽保全部收敛的(G8)。
$\log\mathcal U_Q$ 的估值未假为非负。
实际外权的导数、$c_0$ 或 slot 随已指定标记运输产生的
解析外权也须逐项求导，不能只留第一行。


## 5. 指定 seed 的 Norm 纤维：准确非零与其范围

本小节仅对(G9)的同一指定 seed、同一固定
$c_0,\ell_\pm,\Omega,\kappa$ 使用，并保(G11)的单位底数
条件；不将它代替 $\mathfrak T_{\rm orig}$ 之后的 whole
来源。

首先有一个不要求根属于 tame 域的 residue 等式。
由(C8)在 $Q$ 求一阶导数，
$Dr_p(Q)=pU(w_Q)/w_Q^{p^2}$。
结合(C4)、$U\equiv1\bmod p$，准确得到
$$
 \left(\frac{b_{N,\widetilde Q}}{w_Q^N}\right)^{p^2}
       =U(w_Q)^{-N},\qquad
 \overline{b_{N,\widetilde Q}/w_Q^N}=1 .
 \tag{G15}
$$
后式只用剩余域中 $p^2$ 次 Frobenius 的单射性。
它没有选择新的 $p^2$ 次根，也不把实际
$\zeta_p$ 中心高项删掉。与(C13)合并，
$B_{N,Q}$ 的 leading 为 $a_0w_Q^a$，
$A_{N,Q}$ 的 leading 为 $N(p+1)\kappa_\sigma w_Q^p/p$，
与(C13)一致；$p+1$ 的剩余类为1。

固定一个 $Q_0\ne O$，用
$\alpha=\overline{w_Q/w_{Q_0}}\in\mathbf F_{p^2}^\times$
标记其它点。原 $\gamma_{102,p}$ 反线性且范数为3，所以
$$
 \overline{w_{\gamma Q}/w_{\gamma Q_0}}=\bar\alpha .
$$
不能把它换成同向 $\alpha$。
$\gamma Q_0$ 相对 $Q_0$ 的共同倍率仍保留；
它的范数为3而非1，但在下面两个同点比中准确消去。
由(G10)、(G15)逐项有
$$
 \boxed{
 \overline{{\cal U}_Q/{\cal U}_{Q_0}}=N(\alpha),\qquad
 \overline{{\cal C}_Q/{\cal C}_{Q_0}}=N(\alpha)^6,\qquad
 \overline{
 \frac{{\cal R}_Q(-2)}{{\cal R}_{Q_0}(-2)}
 }=N(\alpha)^4 .
 }
 \tag{G16}
$$
例如第二个指数来自
$\alpha^4\bar\alpha^6\bar\alpha^{2p}
 =\alpha^{6+6p}=N(\alpha)^6$；
第一个来自 $\alpha^p\bar\alpha^p=N(\alpha)$。
所有实际原中心都已经包含在(G15)，不是假定它们相同。

对§21/§22的一个非零 Norm 纤维，取其中一点作 $Q_0$。
其余 $p$ 个点的 $N(\alpha)=1$。因此完整 $p+1$ 项满足
$$
 \boxed{
 \sum_{Q\text{ 在该 Norm 纤维}}{\cal R}_Q(-2)\ne0,\qquad
 v_p\!\left(\sum_Q{\cal R}_Q(-2)\right)
   =v_p(c_0)+2v_p(\ell_+)-4+\frac{10-p}{\Delta}.
 }
 \tag{G17}
$$
证明是除以其中一项后，整个和的 residue 为
$p+1=1$ 于特征 $p$；(G8)确保所有负二修正的 residue
仍是1。这里没有另除 $p+1$，也没有增加一次野 Haar $1/p$：
§22的真 projector 已把原来源返回为
$p^{-2}$ 乘这个 Norm 纤维和，而此 $p^{-2}$ 已在(G9)。
这是指定 seed 的真正临界数值，非仅正整数估值的猜想。
它不声称其完整 tame/Artin/source 投影仍非零，更不声称
这个数就是原 canonical $J'_S(0)$。

## 6. 返回原 whole 读者时必须保留的操作

§22(F8)--(F11)已给每个实际 Norm 纤维的合法 bounded-source
临界 covector。其来源是相同有限 Weyl 和经过
$\mathfrak T_{\rm orig}$，不是(G17)中任选的单个 seed。

对任意固定的 R1060 有限 Newton 精度，(G7)可直接代入
(C18)及 R1060 的完整有限转置。全部 $h$、三挠词、
graded period、有限 Haar、Artin/Cor、冻结
$\Lambda(-2),\Lambda'(-2)$ 都仍作用于该整和。
这给同一有限 reader 的准确重写，不需要逐 rank-one
有界性，也不需要给未取角投影的复被积函数逐项指定
$p$-adic 模型。

若某一完整有限 source 返回已经逐字给出
$$
 R_{i,b,n}^{\rm full}
   =\sum_{\alpha,Q}w_{i,\alpha,Q}(n)\,
                       {\cal R}_{\alpha,Q,n}
 \tag{G18}
$$
且所有 $w_{i,\alpha,Q}$ 是该实际运输在同一分量上已付的
解析外权，则可以共同使用(G12)的子列。
原 R1059 全 Maass 一致尾和§22的实际 bounded 输入保证
$$
 {\cal F}_{i,b}(j)=
   \sum_{\alpha,Q}w_{i,\alpha,Q}(j)
                       {\cal R}_{\alpha,Q}(j).
 \tag{G19}
$$
先在盘中每个 $\mathbf Z_p$ 点以合法正整数逼近证明，
再由已付 Tate 解析性得到 germ 等式。
其导数包含 $w'\mathcal R+w\mathcal R'$ 的全部项；
原 $\log-E$ Maass 费用已经由同一 unflat 极限运输，
不能再删一次或重复补入。

(G18)的实际逐字 graded 返回不是本节凭空增加的假设事实。
在它未被支付的部分，保原 $\mathfrak T_{\rm orig}$ 和
R1060 的有限转置，不能从(G17)跳到(G19)的 whole 非零。
特别原 $h_\infty$ 的差2投影可逐有限槽使用，但未投影
被积函数不因此成为一列已代数化的有限 CM 点。
同样，原 canonical 的 tame-zero 输出是额外明确的投影，
不能因每个 Norm 纤维的指定 seed 非零而略去它。
本节已付的是完整 normalized jets、唯一单位底数的全部费用、
同分量解析极限以及指定 seed 的准确非零；没有新增
canonical 坏条件或恢复已撤回的 usual/flat cross。


## 7. 同一 book period 的真实 Galois 下降与导数中的周期项

本节继续(G9)--(G19)已实际代数化的那些字。这里固定一个有限
完备扩域 \(F/K_p\)，其中包含这些字的模型、代数微分、全部
\(p^2\) 除点及中心、\(\kappa,c_0,\ell_\pm\) 和所有代数
source 系数。尚未证明某个 \(h\) 被积项的单独代数化时，不把
它加入这个集合。特别不将 book period \(\Omega\) 放入 \(F\)。

我们证明：原规范下的非零临界值，确实迫原始权导数非零；
但将周期项正确除去以后，不再有这个自动结论。这为下一步
同 canonical 斜率比较给出一个准确、可检验的下降条件。

### 7.1. 深 Galois 元素确来自同一个完整 Tate 标记

取原 CM Tate 基 \(\alpha\)，并将 \(F\) 增大为有限 Galois
扩域，不改变上述范围。CM Tate 作用的像是
\(\mathcal O_{K_p}^{\times}\) 的开子群。

这里所需的开像可直接沿 R1061(E1)--(E2)证明到所有层，
不靠模 \(p^2\) 的作用猜无限 lift。在原严格整 LT 坐标中，
\[
 [-p](v)=-pv+v^{p^2}.
\]
第一层的 primitive 点满足 \(v_1^{p^2-1}=p\)，为 Eisenstein。
若 \(v_{m-1}\) 已是上一层的均匀元，则
\[
 X^{p^2}-pX-v_{m-1}
\]
在上一层上仍 Eisenstein，给下一层次数 \(p^2\)。
原整坐标和整逆在每个这些点收敛，所以它给的正是同一
除点域。一个 primitive 点生成自由秩一
\(\mathcal O_{K_p}/p^m\) 模，全部点均由原 CM 乘法取得；
次数与 \(|(\mathcal O_{K_p}/p^m)^\times|\) 相同。
因此在原曲线的局部 CM 基中，完整单位像成立；固定任意有限
\(F\) 后，像仍是有限指数开子群。

故存在 \(h\ge2\)，使每个
\[
 a\in (1+p^h\mathcal O_{K_p})^1
\]
都由某个 \(\sigma_a\in G_F\) 在完整 Tate 模上的作用实现。
这些 \(a\) 固定已经列入 \(F\) 的全部有限字。
可以让 \(a\) 取无限多个非挠值，例如充分深的
\(\exp(p^h\delta t)\)、\(t\in\mathbf Z_p\)。
它们的范数为1，且 \(\log a\) 取无限多个值。

原 Tate 基及 CM 点的真实关系是
\[
 \alpha^{\sigma_a}=\alpha g_a,\qquad
 \sigma_a y=yg_a .
\]
模型和所选 \(\omega_E\) 定义在 \(F\) 上；
canonical differential、比较映射和评价均对 Galois 自然。
结合 R1061(E16)在**同一个** marked 点的公式，
\[
 \boxed{\quad
 \sigma_a(\Omega(y))
   =\Omega(yg_a)=\frac{\Omega(y)}{\bar a}
   =a\Omega(y).
 \quad}                                                    \tag{P1}
\]
末等号仅在当前范数一子群使用。
这是完整 Tate 标记的自然性；没有选一个固定 \(\Omega\) 的
连续 \(\mathbf C_p\) 自同构，也没有因估值相同就把
\(\Omega^{-1}\) 认成另一个命名的 LT period。
以下简记 \(c_a=a\)。

### 7.2. 完整 germ 的半线性变换

(G1)--(G8)全部 \(\mathcal F_{N,Q}\) 的系数在 \(F\)：
每项由同一有限代数除点数据得到，而 \(F\) 完备。
(G9)已经支付的其它代数尺度也在 \(F\)。
由 \(\rho=(17/2)p^2\kappa\Omega^2\) 及(G10)，逐项严格有
\[
 \sigma_a(\mathcal C_Q)=c_a^3\mathcal C_Q,\qquad
 \sigma_a(\mathcal U_Q)=c_a^2\mathcal U_Q,\qquad
 \sigma_a(\mathcal F_\pm)=\mathcal F_\pm.                    \tag{P2}
\]
仍使用(G12)的同一个足够小的共同权盘。
\(\sigma_a\) 连续且等距，故与已付的收敛 log、exp 及
Tate 系数极限可交换。
\(c_a\) 已在深主单位群；其 Teich 部分为1。
(G13)遂准确给
\[
 \boxed{\quad
 \sigma_a\bigl(\mathcal R_Q(j)\bigr)
   =c_a^{-1}\exp\bigl(2(j+2)\log c_a\bigr)\mathcal R_Q(j).
 \quad}                                                    \tag{P3}
\]
这里是对固定参数 \(j+2\) 的系数作 Galois 作用；
并不把任意 \(\mathbf C_p\) 参数点视为 Galois 不动点。
在原整数权，显示因子正是 \(c_a^{3+2n}\)。

若 \(\mathcal R(j)\) 是这些实际字连
\(F\)-系数解析外权的一个有限和，则(P3)逐项给同一公式。
例如(G17)的指定 Norm 纤维和，正是这种情况。
尚未支付的全 \(h\)/graded 返回仍不在此断言内。

设 \(R_k=\mathcal R^{(k)}(-2)\)。
逐次对真正的 Tate germ 求导，得到所有 \(k\ge0\) 的准确式
\[
 \boxed{\quad
 \sigma_a(R_k)=c_a^{-1}
       \sum_{r=0}^{k}\binom kr
          (2\log c_a)^{k-r}R_r .
 \quad}                                                    \tag{P4}
\]
特别，
\[
 \sigma_a(R_0)=c_a^{-1}R_0,\qquad
 \sigma_a(R_1)=c_a^{-1}(R_1+2\log c_a\,R_0).                 \tag{P5}
\]
(G14)的全部 \(\mathcal F'\)、\(\log\mathcal U_Q\) 以及已有
解析外权导数均在(P4)内；没有删去 Maass 修正后重命名导数。

### 7.3. 非零 raw 值确实迫全部 raw 权 jets 线性独立

若 \(R_0\ne0\)，则
\[
 \boxed{\quad R_0,R_1,R_2,\ldots
           \text{ 在 }F\text{ 上线性独立。}\quad}            \tag{P6}
\]
证明如下。若有有限非平凡关系
\(\sum_{k=0}^m b_kR_k=0\)、\(b_k\in F\)、\(b_m\ne0\)，
对所有上述 \(\sigma_a\) 作用并乘 \(c_a\)，由(P4)得到
一个在无限多个 \(t=2\log c_a\) 处为零的多项式。
其最高 \(t^m\) 系数为 \(b_mR_0\ne0\)，矛盾。
这只是有限次多项式的根数论证；不需要假设抽象的
\(p\)-adic Schanuel 猜想。

所以(G17)已经证明非零的那个指定 Norm 纤维，其原始
\(\mathcal R'(-2)\) 也真非零，所有更高 raw 权导数同样非零。
这一结论的对象是(G9)完整保留 \(\Omega^3\rho^n\) 的原规范。
它尚未成为 canonical \(J'_S\) 的非零结论。

### 7.4. 去除周期后，真正剩下的有限域导数

为精确说明这个范围，固定同一有限和中的一个非零 \(Q_*\)，
置
\[
 U_*=\mathcal U_{Q_*},\qquad
 u_Q=\mathcal U_Q/U_*\in F^\times .
\]
各 \(u_Q\) 是单位；其 \(p\)-adic log 也在完备有限域 \(F\)
中。仍按(G12)共同锁定全部有限相位。若外权记为 \(w_Q(j)\)，
定义
\[
 V(j)=\sum_Q w_Q(j)\,
        \frac{\mathcal C_Q}{\Omega^3}\,
        u_Q^{-2}\exp((j+2)\log u_Q)\,
        \mathcal F_{-,Q}(j)\mathcal F_{+,\gamma Q}(j+2).
\]
于是 \(V\) 是该共同小盘上的 \(F\)-系数 Tate 函数，并且
\[
 \boxed{\quad
 \mathcal R(j)=
      \Omega^3U_*^{-2}\exp((j+2)\log U_*)V(j).
 \quad}                                                    \tag{P7}
\]
因为 \(U_*/\Omega^2\in F^\times\)，有
\(\Omega^4U_*^{-2}\in F^\times\)。所以在端点，
\[
 \boxed{\quad
 \Omega R_0\in F,\qquad
 \Omega\bigl(R_1-(\log U_*)R_0\bigr)\in F .
 \quad}                                                    \tag{P8}
\]
这不是把非单位 \(\Omega\) 单独作权幂解析化；
\(U_*\) 是(G11)先合全部费用得到的真实单位。
换另一个 \(Q_*\) 时，两个 \(\log U_*\) 只差
\(\log u\in F\)，(P8)的有限域范围保持。

(P2)也给
\[
 \sigma_a(\log U_*)=\log U_*+2\log c_a .
\]
其 \(G_F\) 轨道无限，因此 \(\log U_*\) 在 \(F\) 上超越：
若代数，固定其最小多项式便只能有有限多个共轭。
此处的超越性由实际 CM period 作用证明，非对任意
\(p\)-adic 单位的 log 作同样断言。

反过来，若一个声称已回原代数 frame 的 raw 斜率满足
\(\Omega R_1\in F\)，那么(P5)迫
\[
 \boxed{\quad R_0=0.\quad}                                  \tag{P9}
\]
因为 \(\Omega R_1\) 的 Galois 差准确是
\(2\log c_a\,\Omega R_0\)，而可取 \(\log c_a\ne0\)。

因此，将一个 \(R_0\ne0\) 的 raw ramified 斜率同原 canonical
斜率相认时，必须显式支付(P8)的周期导数项或相同的外权取消。
若原完整读者的临界值已经为零，(P8)本来就退化为
\(\Omega R_1\in F\)，本节不再排斥 \(R_1=0\)。
这正是原固定 canonical 目标仍须处理的范围，不能以(P6)绕过。
下一小节另在原 whole Amice 来源上写出同一作用，不要求先完成(G18)的单字分解。


### 7.5. 原 whole bounded 测度上的准确 Maass 变换

固定 R1059/R1060 的一个真实 whole bounded 来源 \(A_i\)，
其普通矩为 \(m_n\)、完整 unflat 矩为 \(R_n=T_Cm\)。
将其模型、有限 level/source、CM splitting 及全部固定代数
系数包含在上述有限 \(F\) 中。内在连接及其任意次迭代在
这个同一域上定义，所以 R1060(2)中的全部内在 CM jet 都在
\(F\)。取足够深的上述 \(\sigma_a\)，则同一 period 自然性给
\[
 \sigma_a R_n=c_a^3(c_a^2)^n R_n,\qquad \sigma_a C=C .
\]
这一陈述使用原 whole jet 的代数化，不把未积分的
\(h_\infty\) 单项另建成代数来源。

令 \(D_\kappa m_n=\kappa^n m_n\)，其中 \(\kappa=c_a^2\)。
R1060(13)--(14)的有限三角变换满足
\[
 T_C T_D=T_{C+D},\qquad D_\kappa T_C=T_{\kappa C}D_\kappa .
\]
故原测度本身的精确 Galois 矩公式是
\[
 \boxed{\quad
 \sigma_a m_n
   =c_a^3\sum_{r=0}^{n}c_r(n)
        ((c_a^2-1)C)^r(c_a^2)^{n-r}m_{n-r}.
 \quad}                                                    \tag{P10}
\]
因而它一般不是只将 \(x\) 乘 \(c_a^2\) 的 pushforward。

若以 \(\mathscr A(Q)=\int Q^x\,d\mu_i(x)\) 记同一个 Amice
函数，则在形式原点、从而在共同足够小的 \(L\) 盘上，
\[
 \boxed{\quad
 \sigma_a\mathscr A(e^L)
  =c_a^3(1-(c_a^2-1)CL)^{-3}
    \mathscr A\!\left(
       \exp\frac{c_a^2L}{1-(c_a^2-1)CL}\right).
 \quad}                                                    \tag{P11}
\]
左边已经是原实际 bounded 测度的 Galois 共轭；
(P11)的全盘延拓由这个左边给出。
本式不把右边的形式复合对任意新输入宣布为全单位盘
bounded 算子。若用 LT 角色盘上的真实 \([\kappa]\) 来运输
原源，(P10)的全部 Maass 三角费用仍须一并携带，
不能只移植其中 \(D_\kappa\) 一项。

本节所有结论均为同一原来源的纸笔推导，无新增数学执行。
