# R223 — 对数精度的实际负范数：大素数支持、深 Smith 比例与原乘法入口

日期：2026-11-12。**状态：必要的大素数支持和深 Smith 比例、原连续像交集的比较，以及原 primitive 关系的乘法传播均已证明。尚未由双完整中央条件构造所需关系或证明所需深层比例；主课题未完成。**

本篇继续 R218、R220 的有符号范数路线。它不把真实负范数截零。主要结论是：若 $N=O(\log D)$ 的原交集提供所需主项，那么正权重的一批 $p\asymp D^2$ 上，原完整连续矩阵必须有正比例的 Smith 指数达到 $c\log D$。反过来，这种真实深层比例足以支付主项，并可通过一个明确的原多项式乘法机制得到。

## 1. 固定原源与所需主项

仍取
$$
 E_D=\mathbf Z[A,C]_{\le D},\qquad
 m=m_D=\binom{D+2}{2},
$$
以及原真实 jump
$$
 0=k_1<\cdots<k_m=K,\qquad S=\sum_i k_i.
 \tag{1}
$$
R191/R217 给固定常数 $a_0,c_0,C_0>0$，使充分大 $D$ 时
$$
 c_0D^2\le K\le C_0D^2,\qquad
                       a_0mK\le S\le mK.
 \tag{2}
$$
取完整连续前缀 $k=K+1$，以及 R218 的实际交集收益
$$
 I_{p,N}=\sum_{d_t\ge2}\iota_{d_t,k_t,N},
 \qquad k_t=k-2t,\quad d_t=D-2t.
$$
其精确输入始终是原 $E_D$、原全深权 $e_{p,j}$ 和同一个双分量目标。
记
$$
 \mathcal P_D=\{p\equiv3\pmod4:
                  7\le p\le4K-1,\ p\ne11\}.
$$
R218 给
$$
 0\le I_{p,N}\le B_N(J_{p}^{\rm cont})\le Nm,
 \qquad
 \sum_i\log\|\varphi_D^{k_i}\|_p
                    \le(E_p-I_{p,N})\log p,
 \quad E_p=\sum_i e_{p,k_i}.
 \tag{3}
$$

本篇考察固定 $C_N,\gamma>0$ 下的条件
$$
 N=N(D)\le C_N\log D,\qquad
 \mathcal I_{D,N}:=\sum_{p\in\mathcal P_D}I_{p,N}\log p
                              \ge\gamma S\log D.
 \tag{4}
$$
这不是已证明的中央后果。R218 的充分门要求某个固定
$\gamma>2$；较小的 $\gamma>0$ 也适用下面的必要规模结论。

## 2. 小于 D² 的素数段不能独自提供主项

对任意 $x\le4K$，由 (3) 和 Chebyshev 上界，
$$
 \sum_{\substack{p\in\mathcal P_D\\p\le x}}I_{p,N}\log p
               \le Nm\,\vartheta(x)=O(Nmx).
 \tag{5}
$$
因此在 (4) 的精度范围中，只要 $x=o(K)$，
$$
 \sum_{p\le x}I_{p,N}\log p=o(S\log D).
 \tag{6}
$$
特别，对每个固定 $\delta>0$，$p\le D^{2-\delta}$ 的贡献至多
$O(D^{4-\delta}\log D)$。甚至 $p\le K/\log D$ 的总贡献也只有
$O(S)$。

这些都是原交集的实际长度界，已经把全部次数步骤共同累计在
$I_{p,N}\le Nm$ 中，没有再乘一个 $D$。结论不排除小素数处存在深交集，只说明在对数精度下它们的素数权重不足以承担 (4)。

## 3. 必须有一批 p≈D² 带着正比例的深 Smith

**定理 1。** 假设 (4)。则存在只依赖 $\gamma,C_N$ 及 (2) 常数的
$\alpha,\beta,\eta,c>0$，使对所有充分大 $D$，存在
$$
                 \mathcal G_D\subset\mathcal P_D\cap[\alpha K,4K]
$$
满足
$$
                    \sum_{p\in\mathcal G_D}\log p\ge\beta K,
 \tag{7}
$$
且每个 $p\in\mathcal G_D$ 的原连续矩阵至少有 $\eta m$ 个
Smith 指数不小于 $c\log D$。

**证明。** 取常数 $C_\vartheta$ 使
$\vartheta(x)\le C_\vartheta x$。选充分小的固定 $\alpha>0$，
由 (5) 保证 $p<\alpha K$ 的贡献至多
$\gamma S\log D/4$。这可以统一做到，因为
$N\le C_N\log D$、$S\ge a_0mK$。

再选充分小的固定 $b>0$。所有满足
$I_{p,N}<bm\log D$ 的素数，其总贡献至多
$$
 bm\log D\,\vartheta(4K)
       \le4C_\vartheta b\,mK\log D
       \le\gamma S\log D/4.
$$
因而在剩余集合
$$
 \mathcal G_D=\{p\in\mathcal P_D:
                  p\ge\alpha K,\ I_{p,N}\ge bm\log D\}
$$
上，贡献至少为 $\gamma S\log D/2$。每个素数处
$I_{p,N}\le C_Nm\log D$，所以
$$
 \sum_{p\in\mathcal G_D}\log p
      \ge\frac{\gamma S}{2C_Nm}
      \ge\frac{\gamma a_0}{2C_N}K,
$$
证明 (7)。

对这样的 $p$，有
$B_N(J_p^{\rm cont})\ge bm\log D$。令
$T=\lfloor b\log D/2\rfloor$，并令 $q_p$ 为不小于 $T$ 的
Smith 指数个数。由于 $B_N\le Tm+Nq_p$，
$$
                         q_p\ge\frac{b}{2C_N}m
$$
对充分大 $D$ 成立（减小固定常数即可处理取整）。
而 $T\ge c\log D$ 对某个固定 $c>0$ 成立。这给所需
$\eta,c$。$\square$

这里的集合可依赖 $D$。定理没有把不同 $D$ 的集合交成一个未经控制的无穷素数集合，也没有据此宣称某条曲线已获得初级有限。

## 4. 这些素数确实必须贡献负范数

在定理 1 的集合上，R173/R215 的原权上界给
$$
 E_p\le\frac{4pS}{p^2-1}\le\frac{5S}{p}
                       \le\frac{5}{\alpha}m
 \tag{8}
$$
（充分大 $D$ 即可）。而 $I_{p,N}\ge bm\log D$。
所以对充分大 $D$，(3) 准确推出
$$
 \boxed{\quad
 \sum_i\log\|\varphi_D^{k_i}\|_p
                         \le-\frac b2m\log D\,\log p
               \qquad(p\in\mathcal G_D).
 \quad}                                                       \tag{9}
$$
这是真实原范数的负上界，不只是将正分母抵消到零。R220 的截零估计不能用来删除 (9)。

同时，在任意固定带 $p\in[\alpha K,4K]$ 上，充分大 $D$ 给
$r>2D$ 和 $K<R_p$。因此这些主素数全部处于 R214 的低单位范围和原第一带。对 $j\le K$，
$$
                       e_{p,j}=\lfloor j/r\rfloor\le4/\alpha.
$$
R218 的全部低 torsion 与终端项为零；其 shift 核损失准确满足
$$
 0\le\sum_t\ell_{d_t,k_t,N}
       \le D\lfloor K/r\rfloor\le4D/\alpha.
$$
故在这个大素数带，所有精度都统一有
$$
 \boxed{\quad
  B_N(J_p^{\rm cont})-\frac{4D}{\alpha}
                       \le I_{p,N}\le B_N(J_p^{\rm cont}).
 \quad}                                                       \tag{10}
$$
这证明深 Smith 比例与原交集主项之间只差 $O(D)$；
它没有依赖可能非整的小素数截面。

## 5. 一个正向的原精度层准则

下面给可直接使用的充分条件，而不只给必要界。

**定理 2。** 假设有固定 $\alpha,\beta,\eta,c>0$，并且对所有充分大
$D$ 存在
$$
 \mathcal G_D\subset\mathcal P_D\cap[\alpha K,4K],
 \qquad\sum_{p\in\mathcal G_D}\log p\ge\beta K,
$$
使每个 $p\in\mathcal G_D$ 的原连续矩阵至少有 $\eta m$ 个
Smith 指数不小于
$$
                          T_D=\lceil c\log D\rceil.
$$
取 $N\ge T_D$，则
$$
 \mathcal I_{D,N}
          \ge\beta\eta c\,S\log D-O(DK).
 \tag{11}
$$
特别，若 $\beta\eta c>2$，则这些原有限像条件支付 R218 的严格充分门。

**证明。** 每个所选素数满足
$B_N(J_p^{\rm cont})\ge\eta mT_D$。由 (10)，
$I_{p,N}\ge\eta mT_D-4D/\alpha$。对所选素数加权求和，并用
$mK\ge S$，得 (11)。由于 $DK=O(D^3)=o(S\log D)$，
严格常数余量得以保留。$\square$

若以原整化层的最少生成元数表示，该条件就是
$$
              \rho_{T_D-1}(J_p^{\rm cont})\le(1-\eta)m.
 \tag{12}
$$
也可以在同一个原源中定义
$$
 \mathcal Q_{T,p}(D,k)
   =\{P\in E_D\otimes O:J_{<k}P\in p^TO^k\}.
$$
则 Smith 形式直接给
$$
 \dim_{\mathbf F_p}
   \frac{\mathcal Q_{T,p}(D,k)+pE_D}{pE_D}
                  =\#\{i:s_i(J_p^{\rm cont})\ge T\}.
 \tag{13}
$$
因此定理 2 要求的是原完整前缀中正比例的 primitive 深核方向。
只控制一个删列循环商、一个 primitive 见证或两条方向的独立性，
都没有自动给出 (12) 的比例。

## 6. 原乘法确实能传播一个 primitive 深关系

这提供寻找 (12) 的一个具体正向入口。它保留原源和同一个完整前缀，
不假设 Hasse 偏导也满足原前缀。

**原乘法引理。** 设 $R\in E_d\otimes O$ 的原多项式系数至少一个为单位，
并且
$$
                  J_{<k}(R)\in p^TO^k.
 \tag{14}
$$
那么对任意 $Q\in E_{D-d}\otimes O$，
$$
                  J_{<k}(RQ)\in p^TO^k,
$$
而这些原源方向模 $p$ 至少有 $m_{D-d}$ 个线性独立方向。因此
$$
 \#\{i:s_i(J_{D,<k})\ge T\}\ge m_{D-d}
 \tag{15}
$$
在原 $J_{D,<k}$ 满列秩时成立。

**证明。** 写原输出
$R(w)=\sum R_iw^i$、$Q(w)=\sum Q_jw^j$。
R215 已给 $p^{e_j}Q_j\in O$，而 (14) 给
$p^{e_i}R_i\in p^TO$ 对全部 $i<k$ 成立。
对 $n<k$，逐项有
$$
 p^{e_n}[w^n](RQ)
  =\sum_{i+j=n}
       p^{e_n-e_i-e_j}(p^{e_i}R_i)(p^{e_j}Q_j)\in p^TO,
$$
因为 $e$ 超可加，且每个被读的 $R_i$ 都仍属于同一个已保留前缀。

原 $R$ 模 $p$ 是抽象多项式环 $\mathbf F_p[A,C]$ 中的非零元素。
这个环是整环，所以乘 $R\bmod p$ 在原次数至多 $D-d$ 的源上单射。
因此 $R E_{D-d}$ 在原 $E_D/pE_D$ 中的像维数为 $m_{D-d}$。
再用 (13) 即得 (15)。$\square$

若对定理 2 的那批素数，可以找到
$$
 d\le\theta D,\quad 0<\theta<1,\qquad
 T=\lceil c\log D\rceil
$$
的同一个原前缀 primitive 关系，则
$$
             m_{D-d}/m_D\ge(1-\theta)^2+o(1).
$$
于是任意固定 $\eta<(1-\theta)^2$ 都可用于定理 2。
这说明一个成本已付的原深关系可以提供正比例方向，毋须把约
$D^2$ 条 Hasse 槽当成独立算术条件。

但本篇没有构造这样的 $R$。它必须在原 $A,C$ 多项式格中 primitive，
次数不能超过显示预算，而且 (14) 必须保留全部连续行至
$K_D+1$。清分母后变成 $p$ 倍的关系、只保角向稀疏行的关系、
或对不同源列分别选的 gauge，都不满足这个入口。

## 7. 当前仍缺的原算术输入

R189 的两个完整中央条件确实给同一个原源上的 Hasse 方向族，
但现有证明将它们放在带权输入 core 中。它没有证明可从这里的
完整 scalar 前缀低损失地恢复整个 core，更没有据此证明
(12) 或 (14)。本篇不把中央零直接当作图形整性或模 $p^T$ 代数关系。

因此对数精度路线现在有一个明确的正向目标：在原双完整中央失败的
假设下，证明足够大的实际素数集合上存在 (14) 这样的低次数 primitive
深关系，或直接证明 (12) 的正比例层亏损。定理 2 和原乘法引理已经
支付其到真实负范数及 R218 严格门的连接；实际关系的构造仍未完成。

依赖：[R173](R173-full-depth-cm-carry-envelope-and-true-jets.md)、
[R189](R189-complete-central-hasse-families-and-weighted-core.md)、
[R191](R191-first-band-source-divisibility-and-global-multiplicity.md)、
[R198](R198-joint-image-saturation-and-complete-prefix-smith.md)、
[R214](R214-quadratic-pair-tail-recursion-and-deleted-c-image.md)、
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)、
[R217](R217-fixed-precision-budget-and-true-jump-scale.md)、
[R218](R218-all-degree-original-image-intersection-recursion.md)、
[R220](R220-clipped-budget-and-signed-negative-norm-gain.md)。
