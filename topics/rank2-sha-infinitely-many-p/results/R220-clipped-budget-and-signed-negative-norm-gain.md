# R220 — 截零规则下的更锐精度预算与真实负范数的区别

日期：2026-11-12。**状态：截零收益的统一上界及其系数二已证明。该上界只适用于主动把局部负范数截为零的记账规则，不是对 R218 原有符号范数或真实交集递推的限制。**

本篇使用 R217 的同一个原二维源和真实 jump。结论为
$$
 \boxed{\quad
 G_N^{\rm clip}
   \le 2S_D\log\!\bigl(1+\min\{N,K_D\}\bigr)+O(S_D),
 \quad N\ge1.
 \quad}
 \tag{1}
$$
常数不依赖 $D,N$。因此在截零规则下，$N=O(\log D)$ 只能产生
$O(D^4\log\log D)$ 的可见改善。R218 允许真实负范数，故不能向它套用这个更强限制。

## 1. 原源、jump 数量与统一参数范围

取原
$$
 E_D=\mathbf Z[A,C]_{\le D},\qquad
 m_D=\binom{D+2}{2},
$$
及真正的有理秩跳阶
$$
 0=k_1<\cdots<k_{m_D}=K_D,\qquad S_D=\sum_i k_i.
 \tag{2}
$$
始终使用同一个原源系数范数。R191、R217 已证明
$$
 K_D\le(1+o(1))D^2,\qquad
 \frac{m_D(m_D-1)}2\le S_D\le m_DK_D.
 \tag{3}
$$
因此对充分大 $D$，存在只依赖原固定曲线的常数 $c,C>0$，使
$$
 cD^2\le K_D\le CD^2,\qquad
 cD^2\le S_D/m_D\le CD^2,
$$
以及
$$
                  1\le\frac{m_DK_D}{S_D}\le C.               \tag{4}
$$
第一条的下界来自 $K_D\ge m_D-1$；第二条的下界来自
$S_D/m_D\ge(m_D-1)/2$；(4) 的上界来自
$2K_D/(m_D-1)$。所以后文将分界写成 $K_D/N$ 不是另加平均阶数假设。

本文取 $D\ge2$、整数精度 $N\ge1$，不要求 $N\le K_D$。
将有限多个较小的 $D$ 吸收入常数后，下述误差可同时对全部
$D\ge2,N\ge1$ 使用。

## 2. 截零规则究竟记了什么

对当前惰性素数 $p\ge7$，排除固定坏素数 $11$，记
$$
 E_p=\sum_i e_{p,k_i},
$$
其中 $e_{p,j}$ 是 R215 的全深原整化权。取原真实 jump 方阵的
Smith 指数 $s_{p,i}$，模 $p^N$ 可见的准确长度为
$$
 b_{p,N}=\sum_i\min(N,s_{p,i}),\qquad
                           0\le b_{p,N}\le Nm_D.             \tag{5}
$$
R198 的原有符号范数为
$$
 \sum_i\log\|\varphi_D^{k_i}\|_p
                       =(E_p-\sum_i s_{p,i})\log p.
 \tag{6}
$$

若只使用 (5)，随后又主动把得到的负上界截为零，则所记成本变为
$$
                      \max(E_p-b_{p,N},0)\log p.
$$
相对于原包络 $E_p\log p$，这种规则记下的改善准确是
$$
 g_{p,N}^{\rm clip}=\min(E_p,b_{p,N})\log p
                  \le\min(E_p,Nm_D)\log p.
 \tag{7}
$$
定义 $G_N^{\rm clip}=\sum_p g_{p,N}^{\rm clip}$。

式 (7) 的适用条件必须保留。若继续使用 (6) 的真实负值，或另外证明
固定精度之外的完整 Smith 尾，则不能以 (7) 上界那些新增收益。
同样，某个固定精度证书若直接证明无穷多个素数的中央非零，并不需要通过本篇的累计预算。

## 3. 从原 e 权到一个统一的素数分段

R173/R215 给
$$
 e_{p,j}\le\frac{4pj}{p^2-1},\qquad
 e_{p,j}=0\quad(p>4j-1).
$$
因此
$$
 E_p\le\frac{4pS_D}{p^2-1}
       =\frac{4S_D}{p}+\frac{4S_D}{p(p^2-1)},
 \qquad E_p=0\quad(p>4K_D-1).
 \tag{8}
$$
此处的支持结论只针对 $E_p$。原整数 minors 在更大的素数处仍可能产生正 Smith 指数；只是截零规则在 $E_p=0$ 时不给它们任何收益。

令
$$
                  A=Nm_D,\qquad B=4S_D,\qquad X=4K_D.
 \tag{9}
$$
由 $\min(A,b+c)\le\min(A,b)+c$，
$$
 G_N^{\rm clip}
 \le\sum_{\substack{p\le X\\p\equiv3\ (4)}}\min(A,B/p)\log p
       +O(S_D).
 \tag{10}
$$
因为
$$
 \sum_{p\ge7}\frac{\log p}{p(p^2-1)}<\infty,
$$
该误差与 $N,D$ 无关。加入或删去固定有限个素数仍只改变 $O(S_D)$：可以始终用 $B/p$ 控制其项，而不是使用可能随 $N$ 增长的 $A$。

令分界
$$
                     Y=B/A=\frac{4S_D}{Nm_D}.                \tag{11}
$$
由 (3)–(4)，$Y\asymp K_D/N$，两侧常数均独立于 $N,D$。

## 4. 模四 Mertens 与系数二

使用 R173 已采用的固定模数四 Mertens 输入
$$
 M_3(x):=\sum_{\substack{p\le x\\p\equiv3\ (4)}}
                   \frac{\log p}{p}
                  =\frac12\log x+O(1)\qquad(x\ge2).
 \tag{12}
$$
特别对所有 $2\le y\le x$，有统一误差
$$
                  M_3(x)-M_3(y)=\frac12\log(x/y)+O(1).
 \tag{13}
$$
另由二项式的 Chebyshev 估计，
$\vartheta_3(x)=\sum_{p\le x,\ p\equiv3(4)}\log p=O(x)$。
低素数段只需这个上界；系数二完全来自 (13) 的 $1/2$ 与 (9) 的 $B=4S_D$。

记 (10) 中的主和为 $H(A,B,X)$。

**情形一：$Y\ge X$。** 此时
$$
 H=A\vartheta_3(X)=O(AX)=O(B)=O(S_D).
 \tag{14}
$$

**情形二：$2\le Y<X$。** 准确分段为
$$
 H=A\vartheta_3(Y)+B\{M_3(X)-M_3(Y)\}.
$$
第一项是 $O(AY)=O(B)$；第二项用 (13)，得到
$$
 \begin{aligned}
 H&\le \frac B2\log(X/Y)+O(B)\\
  &=2S_D\log\!\left(\frac{Nm_DK_D}{S_D}\right)+O(S_D)\\
  &\le2S_D\log N+O(S_D),
 \end{aligned}                                               \tag{15}
$$
最后一步准确使用 (4)。另一方面，不分段的 $H\le BM_3(X)$ 同时给
$$
                         H\le2S_D\log K_D+O(S_D).             \tag{16}
$$

**情形三：$Y<2$。** 仍有 (16)，并且 (11) 给
$N>2S_D/m_D$。由 (4)，这迫 $N\ge cK_D$，于是
$\log K_D\le\log N+O(1)$。所以本情形也同时满足 (15)、(16) 的统一上界。

综合三种情形和 (10)，得到 (1)。这也说明 $N$ 任意增长时为何必须保留
$\min(N,K_D)$：超过 $K_D$ 的精度不会让截零改善大于原全部正分母包络。没有把 $N\ll K_D$ 的分段公式无证外推到所有精度。

## 5. 对截零路线的必要精度规模

R217 给
$$
 S_D=\Theta(D^4),\qquad
 \sum_p E_p\log p=4S_D\log D+O(S_D).
$$
因此：

- 若 $N=O(\log D)$，则
  $G_N^{\rm clip}=O(S_D\log\log D)=o(S_D\log D)$。
- 更一般地，若 $N=D^{o(1)}$，仍有
  $G_N^{\rm clip}=o(S_D\log D)$。
- 若希望这种截零数本身支付至少 $cS_D\log D$ 的改善，其中 $c>0$ 固定，则 (1) 必迫
  $$
                   \log(1+N)\ge(c/2)\log D-O(1).
  \tag{17}
  $$
  所以需要多项式量级的精度，而不仅是对数量级。

这里的结论是对显示的记账规则而言。特别，如果额外规定 R218 充分门中的
$(2+\varepsilon)S_D\log D$ 改善全部由 $G_N^{\rm clip}$ 支付，那么必须有
$$
                 \log(1+N)\ge(1+\varepsilon/2)\log D-O(1).
 \tag{18}
$$
**这个额外截零规定不属于 R218。** R218 使用原有符号范数，保留交集收益超过当地分母包络的部分，所以不能据 (18) 限制它的精度选择。

## 6. 对数精度路线必须保留的真实负范数

令 R218 在第 $p$ 个素数、同一原全秩前缀上得到的实际交集收益为
$$
 I_{p,N}=\sum_{d_t\ge2}\iota_{d_t,k_t,N}.
$$
由该文原整源递推，
$$
                     0\le I_{p,N}\le B_N(J_p^{\rm cont})
                                     \le Nm_D.
$$
其相对于原包络有准确分解
$$
 I_{p,N}
    =\min(E_p,I_{p,N})+(I_{p,N}-E_p)_+.
 \tag{19}
$$
第一部分满足本篇全部截零上界。第二部分则是真正可用于 (6) 的负范数收益：R218 的合法 jump 比较给
$$
 \sum_i\log\|\varphi_D^{k_i}\|_p
                         \le(E_p-I_{p,N})\log p.
 \tag{20}
$$

因此，若使用 $N=O(\log D)$ 并希望这些交集提供
$cS_D\log D$ 级的累计主项，则在 R218 的明确素数支持内必有
$$
 \sum_p(I_{p,N}-E_p)_+\log p
                    \ge cS_D\log D-O(S_D\log\log D).
 \tag{21}
$$
这没有证明主项存在；它精确指出对数精度方案必须实际获得哪一部分收益。
只证明消去正分母，然后把剩余负值丢掉，无法保留这个量。

R218 §4.1 还把其精度增长写成实际最少生成元数的差。令
$$
 \lambda_{p,t}
  =\sum_{d_s\ge2}
     \{\rho_t(\mathscr K_{d_s})+\rho_t(Y_{d_s})
                          -\rho_t(J_{d_s})\}.
 \tag{22}
$$
这些都是同一原目标中的实际有限像，不是独立可调方向。准确有
$$
                 I_{p,N}=\sum_{t=0}^{N-1}\lambda_{p,t},
 \qquad 0\le\lambda_{p,t}\le m_D.
 \tag{23}
$$
上界来自 R218 正项分解的逐精度增量：
全部交集增量之和不超过
$B_{t+1}(J^{\rm cont})-B_t(J^{\rm cont})
=m_D-\rho_t(J^{\rm cont})$。
所以它已经共同控制了全部次数步骤，不能再乘一次步骤数。

(23) 本身只是准确身份与上界，不会自动给 (21) 所需的下界。
继续对数精度路线，必须用原完整中央条件证明在足够多实际素数、足够多精度层上，(22) 的联合像生成元减少确实发生，并且累计超过 $E_p$。这是下一步的原交集问题，不能由长度单调或环境维数替代。

依赖：[R159](R159-degree-sensitive-direct-slope-boundary.md)、
[R173](R173-full-depth-cm-carry-envelope-and-true-jets.md)、
[R191](R191-first-band-source-divisibility-and-global-multiplicity.md)、
[R198](R198-joint-image-saturation-and-complete-prefix-smith.md)、
[R215](R215-full-depth-faber-transport-and-first-cross-band-carry.md)、
[R217](R217-fixed-precision-budget-and-true-jump-scale.md)、
[R218](R218-all-degree-original-image-intersection-recursion.md)。
