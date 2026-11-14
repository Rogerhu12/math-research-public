# 当前工作记录：原 ordinary ST p 层的完整 trace

日期：2026-11-13。范围：O4、R161/R142 的同一个 E389 完整 Heegner 迹及原 $\ell$ 层标签。这是一项已闭合的比较，不是无穷非零结果。主目标仍未完成。

## 1. 原整函数的 p 分支迹为零

R161 的规范整提升在原 ordinary 形式域上为
$$
 \widehat G_{p,\Psi}
 =p^{-1}\log_E\bigl(\Psi\varphi_{\rm can}^2
                -[a_p]\Psi\varphi_{\rm can}+[p]\Psi\bigr).
$$
其整性来自括号内的群值映射在特殊纤维恒为 $O$，不要求单个
$\log_E\Psi/p$ 整。除去固定好位单位后，其准确尖点展开是
$$
 \widehat g(q)=\sum_{d\mid D_0}\sum_{p\nmid m}\frac{a_m}{m}q^{dm},
 \qquad p\nmid D_0 .
$$
因此 $p$ 个非 canonical $p$ 同源分支上的**未归一化**总迹为零。
在 Tate 盘上直接对 $q^{1/p}\zeta_p^a$ 求和即可核查；各模 $p^N$
的 q 展开原则把它提升为原 ordinary 形式域的恒等式。
这里没有对一个可能非整的 trace 先除 $p$。

原 $\ell$ 层的所有 prime-to-$p$ 退化图、完整 $U$ 迹及 deck
标签与这个同源对应相容。按照 R161/R154 运输全部 determinant
分量，Weil 配对随 $p$ 同源一同运输，不固定一个错误的配对分量。
所以原
$$
 \widehat B,\qquad
 \widehat F_2=\sum_{j=0}^{p-1}\binom j2\tau^j\widehat B
$$
也有相同的零 trace。这里 $\tau$ 是原 $\ell$ 环类 $C_p$ 的生成元；
它没有被换成 $p$ 层 Galois 生成元。

## 2. 两条 horizontal 分支与 primitive p 层

在原 split ordinary CM 中心 $c$，非 canonical 的 $p$ 个分支
包括另一条 horizontal CM 分支 $c^-$，以及以 $c^-$ 为中心的
$p-1$ 个 primitive conductor-$p$ quasi-canonical 分支。
以同一个 ST 坐标 $q_{\rm ST}=1+t$ 写后者为
$t=\zeta_p^a-1$、$a\in(\mathbb Z/p)^\times$，并保留原标记，则
$$
 \boxed{\quad
 \operatorname{Tr}_{\text{primitive }p}\widehat F_2
                         =-\widehat F_2(c^-).
 \quad}
$$
完整类群迹后，$c^-$ 只给原 $\mathfrak p$-Artin 置换；它不是一个
独立目标方向。对 conductor $p^n$、$n\ge2$，每个非 canonical
$p$ 步恰是全部 $p$ 个 descending 分支，因此其完整下降 trace
准确为零。原 $\ell$ 标签和原全类群迹始终保留。

这与原未经 p-depletion 的 Heegner 点 norm 递推不同；不能把
两种函数的 trace 公式混用。

## 3. 真实首正规 jet 与同精度的长 jet 和

在 $c^-$ 的相应 ordinary 完备环中写
$$
                  \widehat F_2(t)=\sum_{j\ge0}b_jt^j,\qquad b_j\in O .
$$
$O$ 为原全部标签所需的未分歧系数环（或相应有限 étale 代数）。
若原整个 CM 纤维的二阶行失败，则 $b_0\in pO$。
在 R142 的简单总迹情形，首正规 jet 是
$$
 b_1(y)=\frac{n_1}{2}y^2+
                \left(\frac{n_1}{2}-a_1\right)y+g_1,\qquad n_1\ne0
 \quad\bmod p .
$$
所以它在至少 $p-2$ 个几何分支为单位；若原剩余纤维为次数 $p$
的域，次数小于 $p$ 的这个多项式在该域中的值为单位。
故在这些**实际**邻点上，积分级数的第一项严格支配：
$$
             v_p\widehat F_2(\zeta_p-1)=\frac1{p-1}.
$$
保全部完成时，对整个向量取最小赋值也得到这个值。
这证明邻近分支非零，但尚未返回原二阶测试。

返回原目标必须使用完整 trace。对 $1\le j\le p-1$，
$$
 \operatorname{Tr}_{\mathbb Q_p(\zeta_p)/\mathbb Q_p}
                 ((\zeta_p-1)^j)=p(-1)^j .
$$
对于 $j\ge p$，不同理想给
$$
 \operatorname{Tr}((\zeta_p-1)^jO_{\mathbb Q_p(\zeta_p)})
                      \subset p^{\lceil j/(p-1)\rceil}\mathbb Z_p
                      \subset p^2\mathbb Z_p .
$$
因此准确有
$$
 \operatorname{Tr}\widehat F_2(\zeta_p-1)
 \equiv(p-1)b_0+p\sum_{j=1}^{p-1}(-1)^jb_j\pmod{p^2}.
$$
与上一节的实际 trace 等式比较，得到
$$
 \boxed{\quad
 b_0+\sum_{j=1}^{p-1}(-1)^jb_j\equiv0\pmod p .
 \quad}
$$
特别在原失败中心，首正规 jet 的单位贡献必由同一真实
$p-1$ 长度的 jet 和抵消。无需猜测 Igusa/ST 导数之间的
$\Omega$ 比例；这个关系直接由保标记的原 p 同源 trace 推出。
不能只取 $b_1$ 或只取一个 quasi-canonical 分支来声明原
$D_2$ 非零。

此分支已得到实际普通层的完整比较，尚未取得原 $a\le1$ 的新
跨素数输入。继续转到 O6 的原 S 单位格、完整 Fitting 值理想
及第二次中心除法的 primitive 关系。
