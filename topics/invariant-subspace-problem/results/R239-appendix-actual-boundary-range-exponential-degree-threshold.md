# R239 附录：实际慢边界算子的指数次数值域阈值

日期：2026-11-12（UTC）。独占作者：literature。

**状态：本稿给出两个真实边界算子的值域障碍。**
令
$$
\gamma_0=\frac32+\frac12\log3=2.049306\ldots.
$$
对每个 $0\le\kappa<\gamma_0$，本稿构造同一个非零向量 $v$，
它具有有限的 $\kappa$ 指数孔次数范数，却同时不属于两个规范慢符号
$T_N,T_Y$ 的实际值域。因此，“任意小的正指数次数权都足以保证真实可解”
这一候选不成立。

证明先构造纯尾上的精确小奇异向量，再将它张量到真实有限头的最高整数基向量上。
该头向量被有限头伴随准确杀去；全算子进位误差另行支付。
本稿不从纯模型直接推断实际值域，也不把这个障碍移到 Haar 表示。

## 1. 空间、真实算子与结论

本稿始终在负整数边界表示
$$
\mathcal H_-=\ell^2(\mathbb N_0)
$$
中工作。标准基 $e_n$ 的孔次数为二进制中 $1$ 的个数 $\nu(n)$。
令
$$
\mathcal H_p=\overline{\operatorname{span}}\{e_n:\nu(n)=p\},
\qquad \mathsf P_p:\mathcal H_-\to\mathcal H_p
$$
为正交次数层及其投影。对于 $\kappa\ge0$，定义
$$
\mathscr X_\kappa
=\left\{v\in\mathcal H_-:
\|v\|_{\mathscr X_\kappa}
=\sum_{p\ge0}e^{\kappa p}\|\mathsf P_pv\|<\infty\right\}.
\tag{1.1}
$$
把权写成 $e^{\kappa(p+1)}$ 只改变一个固定常数，不改变下述结论。

实际后移为
$$
Be_n=\alpha_{v_2(n)}e_{n-1}\quad(n\ge1),\qquad Be_0=0.
$$
沿用归一化幂及 Cayley 项
$$
\mathsf N_j=B^{2^j}/d_j,\qquad
\mathsf Y_j=\mathsf N_j(I+\mathsf N_j)^{-1},
$$
并取
$$
a_j=(j+1)^{-2},\qquad
T_N=\sum_{j\ge0}a_j\mathsf N_j,\qquad
T_Y=\sum_{j\ge0}a_j\mathsf Y_j.
\tag{1.2}
$$
两级数在算子范数中绝对收敛。

**定理 1.1。** 对每个 $0\le\kappa<\gamma_0$，有
$$
\boxed{
\mathscr X_\kappa
\not\subset\operatorname{Ran}T_N,\qquad
\mathscr X_\kappa
\not\subset\operatorname{Ran}T_Y.
}
\tag{1.3}
$$
更强地，可选择一个共同的非零 $v\in\mathscr X_\kappa$，同时满足
$$
v\notin\operatorname{Ran}T_N\cup\operatorname{Ran}T_Y.
\tag{1.4}
$$
因此不存在以整个 $\mathscr X_\kappa$ 为输入、对任一 $T_\bullet$ 给出真实解的右逆；
这个排除甚至不需要预设右逆线性或有界。

第 7 节还给出规范逐孔层原像在整个 $N^\perp$ 上必须支付的指数成本。
那一结论不等同于真正缺陷空间 $M\ominus N$ 上的最优成本。

## 2. 真实有限头截断与全算子误差

令 $E_j$ 为纯孔删除，$E_j^*$ 为其通常伴随，即纯孔创建。
实际递推及权预算为
$$
\mathsf N_j=E_j+\eta_jE_j^*\mathsf N_{j+1},\qquad
\|\mathsf N_j\|=1,\qquad
\mathsf N_j^2=\eta_j\mathsf N_{j+1},
$$
$$
0<\eta_j\le\epsilon_j:=e^{-770\,16^j}.
\tag{2.1}
$$
因此
$$
\|\mathsf N_j-E_j\|\le\eta_j,\qquad
\|(I+\mathsf N_j)^{-1}\|<3,\qquad
\|\mathsf Y_j-E_j\|\le4\eta_j.
\tag{2.2}
$$
第二式可由
$(I+\mathsf N_j)^{-1}=(I-\mathsf N_j)(I-\mathsf N_j^2)^{-1}$
直接得到。第三式使用
$\mathsf Y_j=\mathsf N_j-\mathsf N_j^2(I+\mathsf N_j)^{-1}$。

对 $m\ge1$，记
$$
\mathcal F_m=\operatorname{span}\{e_0,\ldots,e_{2^m-1}\}.
$$
两个 $T_\bullet$ 都保持 $\mathcal F_m$，记其限制为 $H_{\bullet,m}$。
在低 $m$ 位与其余尾位的张量分解下，
$$
T_\bullet^{[m]}
=H_{\bullet,m}\otimes I+I\otimes D_m,
\qquad D_m=\sum_{j\ge m}a_jE_j.
\tag{2.3}
$$
这里 $H_{\bullet,m}$ 是**真实**有限头限制，而不是把整个低头替换为纯删除。

有限链误差给，对每个 $i<m$，
$$
\|\mathsf N_i-\mathsf N_i^{[m]}\otimes I\|
=\alpha_m/\alpha_i\le\eta_{m-1}\le\epsilon_{m-1}.
\tag{2.4}
$$
截断逆同样有范数小于 $3$；逆差恒等式因而给
$$
\left\|\mathsf Y_i-
\mathsf N_i^{[m]}(I+\mathsf N_i^{[m]})^{-1}\otimes I\right\|
\le9\epsilon_{m-1}.
\tag{2.5}
$$
因 $\sum_ja_j<2$、$\epsilon_m\le\epsilon_{m-1}$，头部与尾部误差分别相加得
$$
\|T_N-T_N^{[m]}\|
\le2\epsilon_{m-1}+2\epsilon_m\le4\epsilon_{m-1},
$$
$$
\|T_Y-T_Y^{[m]}\|
\le18\epsilon_{m-1}+8\epsilon_m\le26\epsilon_{m-1}.
$$
故对两个模型统一有
$$
\boxed{\|T_\bullet-T_\bullet^{[m]}\|
\le26e^{-770\,16^{m-1}}.}
\tag{2.6}
$$
这也是 R234 §2(2.7) 的全空间估计。
它控制整个算子范数，因而可直接应用于随后构造的移动单位向量及其伴随。

每个 $\mathsf N_i^{[m]}$ 严格降低整数索引；其 Cayley 项也是无常数项的有限多项式，
仍严格降低整数索引。因此，最高整数头基向量
$$
e_{\mathrm{top},m}:=e_{2^m-1}
$$
满足
$$
\boxed{H_{\bullet,m}^*e_{\mathrm{top},m}=0.}
\tag{2.7}
$$
这个向量在前 $m$ 位恰有 $m$ 个孔。式 (2.7) 是准确恒等式，
没有任何低头相似条件数。

## 3. 纯尾的精确对称消去

现在只在位集合 $[m,\infty)$ 上构造向量。令
$$
C_m=D_m^*=\sum_{j\ge m}a_jE_j^*,\qquad
I=\{m,\ldots,m+q-1\},\qquad q\ge1.
$$
写
$$
y_j=a_jE_j^*,\qquad
C_I=\sum_{j\in I}y_j,\qquad
C_{\rm tail}=\sum_{j\ge m+q}a_jE_j^*.
$$
令 $e_\ell(y)$ 为 $q$ 个平方零交换变量 $y_j$ 的基本对称多项式，
$e_0(y)=I$。平方零关系给
$$
C_Ie_\ell(y)=(\ell+1)e_{\ell+1}(y).
\tag{3.1}
$$
记
$$
A_I=\prod_{j=m}^{m+q-1}a_j
=\left(\frac{m!}{(m+q)!}\right)^2
$$
并定义
$$
u_{m,q}
=A_I^{-1}\sum_{k=0}^q
(-1)^k\frac{(q-k)!}{q!}
e_{q-k}(y)C_{\rm tail}^{\,k}\Omega,
\tag{3.2}
$$
其中 $\Omega$ 是该尾空间的无孔真空。

每项总孔数都是 $q$；不同 $k$ 的头孔数不同，彼此正交。
$k=0$ 项恰为 $e_I$，所以
$$
u_{m,q}\in\mathcal H_q^{(m)},\qquad \|u_{m,q}\|\ge1.
\tag{3.3}
$$
由 (3.1)，相邻项准确消去，只剩
$$
\boxed{
C_mu_{m,q}
=\frac{(-1)^q}{q!\,A_I}C_{\rm tail}^{\,q+1}\Omega.
}
\tag{3.4}
$$
所有尾幂均作用于 Hilbert 真空；这是有限和的真实向量恒等式，不是形式级数运算。

令
$$
\sigma_{m+q}^2=\sum_{j\ge m+q}a_j^2
\le\frac1{3(m+q)^3}.
$$
基本对称和估计给
$$
\|C_{\rm tail}^{\,q+1}\Omega\|
\le\sqrt{(q+1)!}\,\sigma_{m+q}^{q+1}.
$$
于是单位向量
$$
z_{m,q}=u_{m,q}/\|u_{m,q}\|
$$
满足
$$
\boxed{
\|C_mz_{m,q}\|\le U_{m,q}:=
\frac{\sqrt{(q+1)!}}{q!}
\left(\frac{(m+q)!}{m!}\right)^2
[3(m+q)^3]^{-(q+1)/2}.
}
\tag{3.5}
$$

本节也完整说明了纯尾附录中所用的向量。
这里只使用它的上界；不需要知道它是否达到最小奇异值。

## 4. 放进真实头以后，仍有明确指数小量

取
$$
m(q)=\lceil\log_2(q+1)\rceil+3,\qquad
p(q)=q+m(q),
$$
$$
\boxed{
w_q=e_{\mathrm{top},m(q)}\otimes z_{m(q),q}.
}
\tag{4.1}
$$
由孔次数的张量加法，
$$
\|w_q\|=1,\qquad w_q\in\mathcal H_{p(q)}.
\tag{4.2}
$$
整数函数 $m(q)$ 非减，所以 $p(q)$ 严格递增。特别地，所有 $w_q$ 两两正交。
这里不要求不同 $q$ 的位支撑互不相交；正交性来自准确不同的总孔次数。

由 (2.3)、(2.7)，
$$
(T_\bullet^{[m(q)]})^*w_q
=e_{\mathrm{top},m(q)}\otimes C_{m(q)}z_{m(q),q}.
$$
结合 (2.6)、(3.5)，得到同时适用于两个真实模型的估计
$$
\boxed{
\|T_\bullet^*w_q\|
\le U_{m(q),q}+26e^{-770\,16^{m(q)-1}}.
}
\tag{4.3}
$$
这是纯向量进入实际算子的唯一搬运步骤：
有限头伴随准确为零，剩下的是已支付的全算子进位误差。

## 5. 指数常数 $\gamma_0$ 与极限次序

先在 $m=0$ 计算 (3.5)：
$$
U_{0,q}=q!\sqrt{(q+1)!}\,[3q^3]^{-(q+1)/2}.
$$
用阶乘积分界
$$
n\log n-n+1\le\log(n!)
\le n\log n-n+1+\log n
$$
及 $(1+1/q)^{(q+1)/2}\le e$，可得
$$
U_{0,q}\le\frac{e^2}{\sqrt3}\sqrt{q+1}\,e^{-\gamma_0q},
\qquad \gamma_0=\frac32+\frac12\log3.
\tag{5.1}
$$
对一般 $m$，直接相除而不重新引入非统一的 Stirling 余项：
$$
\frac{U_{m,q}}{U_{0,q}}
=\binom{m+q}{m}^{\!2}
\left(\frac q{m+q}\right)^{3(q+1)/2}
\le(m+q)^{2m}.
\tag{5.2}
$$
因此本稿的 $m(q)=O(\log(q+1))$ 给
$$
\log U_{m(q),q}
\le-\gamma_0q+2m(q)\log p(q)
+\tfrac12\log(q+1)+\log(e^2/\sqrt3)
$$
$$
=-\gamma_0p(q)+O((\log(p(q)+1))^2).
\tag{5.3}
$$
这里的隐含常数绝对固定。

另一方面，
$$
16^{m(q)-1}
=16^{\,\lceil\log_2(q+1)\rceil+2}
\ge256(q+1)^4.
\tag{5.4}
$$
所以 (4.3) 的实际误差不超过
$26e^{-197120(q+1)^4}$，远小于 (5.3) 所需的指数尺度。
故存在绝对常数 $C$，使两个模型均满足
$$
\boxed{
\|T_\bullet^*w_q\|
\le\exp\left[-\gamma_0p(q)+C(\log(p(q)+1))^2\right]
}
\tag{5.5}
$$
对充分大的 $q$ 成立。

更方便的量词形式是：对任意 $\mu<\gamma_0$，存在一个共同的 $q_0(\mu)$，
使
$$
\|T_N^*w_q\|,\ \|T_Y^*w_q\|
\le e^{-\mu p(q)}\qquad(q\ge q_0(\mu)).
\tag{5.6}
$$
先固定 $\mu$，再取 $q$ 大；本稿没有交换不一致的头深度极限。

## 6. 一个共同的、确实不在实际值域中的向量

固定 $0\le\kappa<\gamma_0$，选择
$$
\kappa<\lambda<\mu<\gamma_0.
$$
按 (5.6) 固定 $q_0$，定义
$$
\boxed{
v_\lambda=\sum_{q\ge q_0}e^{-\lambda p(q)}w_q.
}
\tag{6.1}
$$
因 $p(q)\ge q$ 且严格递增，该级数在 $\mathcal H_-$ 中收敛，
并且
$$
\|v_\lambda\|_{\mathscr X_\kappa}
=\sum_{q\ge q_0}e^{-(\lambda-\kappa)p(q)}<\infty.
\tag{6.2}
$$
它非零；每个被选中的次数层的分量准确为
$e^{-\lambda p(q)}w_q$。特别地，
$$
\langle v_\lambda,w_q\rangle=e^{-\lambda p(q)}.
\tag{6.3}
$$

假设对任一 $\bullet\in\{N,Y\}$ 存在 $y\in\mathcal H_-$ 满足
$T_\bullet y=v_\lambda$。由于 $T_\bullet$ 是有界算子，
其通常伴随恒等式对这里所有向量均合法。于是
$$
e^{-\lambda p(q)}
=|\langle T_\bullet y,w_q\rangle|
\le\|y\|\,\|T_\bullet^*w_q\|
\le\|y\|e^{-\mu p(q)}.
$$
即
$$
e^{(\mu-\lambda)p(q)}\le\|y\|
$$
对所有 $q\ge q_0$ 成立，矛盾。
因此同一个 $v_\lambda$ 同时不属于两个值域，证明定理 1.1。

这个证明没有依赖闭图定理，也没有从“某类右逆范数太大”间接推测不可解。
它给出了真实 Hilbert 输入上的必要伴随配对估计，并直接违反该估计。

## 7. 整个 $N^\perp$ 上的规范原像成本也不能任意小

本节固定其中一个模型 $T$。令
$$
M=\ker T,\qquad N=\overline{BM}.
$$
因 $B$ 与 $T$ 交换，$N\subset M$。
由已有边界构造 $e_0\in N$；这里只用此事实来采用规范有限列原像。

令 $J$ 为有限整数支撑输入上的规范有限三角右逆：
$$
TJv=v.
\tag{7.1}
$$
它可由 $T$ 的非零首阶系数逐列求得，规范取输出的 $e_0$ 系数为零。
每个 $Jv$ 都是有限整数支撑向量。
不同有限规范若只差有限核向量，差属于 $\mathbb Ce_0\subset N$，
所以模 $N$ 的映射不受该选择影响。

在第 $p$ 孔层的有限支撑输入上，定义
$$
A_pv=P_{N^\perp}Jv.
\tag{7.2}
$$
即使暂不使用 R239 所给的有界延拓，也可把 $\|A_p\|$ 理解为这个稠密定义映射
在单位输入上的上确界，允许值为无穷。
它的对偶配对就是 R239 中规范逐孔层形式原像的映射
$J_p^*:N^\perp\to\mathcal H_p$，在已验证的有界延拓范围内
$$
\|A_p\|=\|J_p^*|_{N^\perp}\|.
\tag{7.3}
$$

对 (4.1) 的 $w_q$，置
$$
f_q=T^*w_q.
$$
则
$$
f_q\in M^\perp\subset N^\perp.
\tag{7.4}
$$
对任意有限支撑 $v\in\mathcal H_{p(q)}$，
$$
\langle f_q,A_{p(q)}v\rangle
=\langle T^*w_q,Jv\rangle
=\langle w_q,TJv\rangle
=\langle w_q,v\rangle.
\tag{7.5}
$$
由有限支撑向量在该次数层中稠密，
$$
\boxed{\|A_{p(q)}\|\ge\frac1{\|T^*w_q\|}.}
\tag{7.6}
$$
同样，$T^*$ 的逐行三角系统单射，所以 $f_q$ 的唯一规范形式原像恰是
实际 Hilbert 向量 $w_q$，从而
$$
J_{p(q)}^*f_q=w_q.
\tag{7.7}
$$
结合 (5.5)，得到
$$
\boxed{
\|P_{N^\perp}J_{p(q)}\|
=\|J_{p(q)}^*|_{N^\perp}\|
\ge
\exp\left[\gamma_0p(q)-C(\log(p(q)+1))^2\right].
}
\tag{7.8}
$$
在尚未引用有界延拓时，只取左端的稠密定义上确界，
同一不等式仍成立。

因此，整个 $N^\perp$ 上不可能有常数 $C_\kappa$ 使
$$
\|J_p^*f\|\le C_\kappa e^{\kappa p}\|f\|
\quad\text{对全部 }p,\ f\in N^\perp
$$
成立，若 $\kappa<\gamma_0$。

**这不是缺陷空间专属的下界。**
上述 $f_q$ 实际属于 $M^\perp$，而真正未知的缺陷是
$D=M\ominus N\subset M$。非零 $f_q$ 与 $D$ 正交。
所以本节不排除只在 $D$ 上存在更好的指数估计，
也不证明 $D\ne0$，更不解决 $N=M$。

## 8. 与已有正向右逆及后续问题的边界

- 已有 R234/R239 的较大指数权右逆，与本稿无冲突。
  本稿给出的必要阈值是 $\kappa\ge\gamma_0$；
  它不声称 $\gamma_0$ 是准确可解阈值。
- 在临界值 $\kappa=\gamma_0$，本稿的次指数余项不足以作决定；
  该点以及上下界之间的间隙保留。
- 输入 $v_\lambda$ 是真实的边界 Hilbert 向量，具有指定指数次数矩，
  但通常含无限孔次数。这里不否定每个固定孔次数层具有真实右逆。
- 本稿没有构造 Haar 正常湮灭态，也没有把边界孔次数与 Haar 的 Walsh 次数混同。
- 对 $f\in M\ominus N$ 的形式关系 $T^*h=f$、$Tf=0$，
  仍可尝试利用这两个方程共同提供的额外结构。
  第 7 节只排整个 $N^\perp$ 上无差别地把指数常数降到任意小的路线。

## 9. 可核验来源

1. [纯尾创建指数上下界完整稿](../notes/2026-11-12-pure-tail-creation-exponential-singular-bounds-0c-agent.md)，
   完整源 blob：`d7186a61618a97cd19c68419ac0c0decf7d4cd27`。
   本稿第 3 节重新给出所用向量、准确消去式和范数上界。
2. R234《两个实际慢边界符号在超三次孔次数空间上的有界右逆》§2(2.7)，
   完整源 blob：`d3dea3fc3440afa5c1f78867807f34746d61f716`。
   本稿第 2 节重新付清 $26\epsilon_{m-1}$ 的全算子误差。
3. R239 的逐孔层规范形式原像及指数权右逆附录用于第 7 节的既有有界延拓解释；
   第 6 节的实际不可解结论完全不依赖形式原像或该延拓。
