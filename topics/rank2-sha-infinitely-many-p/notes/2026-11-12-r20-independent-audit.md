# R20 独立核查：范数控制、辅助单位、字符中心与截断边界

**可信度：已证明的补充核查。** 本文独立核查 R20 的三个易产生指数误差的环节，并给出形式比较的精确边界。固定 R16/R20 的
$$
E:y^2=x^3-17x,\quad K=\mathbb Q(i),\quad
p\ge13,\quad p\equiv1\pmod4,\quad p\ne17.
$$
结论是 R20 的比较成立；没有发现非平凡 $\chi$ 分量中残留的范数修正。本文不重新编辑 R20，也不声称已解决跨素数的非消失问题。

## 1. 范数控制中的两个修正确实被消去

采用 R20 记号 $F_n=K(E[\mathfrak p^n])_{\mathfrak P}$、
$\Delta=\operatorname{Gal}(F_1/\mathbb Q_p)$、$\Gamma=\operatorname{Gal}(F_\infty/F_1)$，以及在 $E[\mathfrak p]$ 上作用的非平凡 Teichmüller 字符 $\chi$。

有限层的乘法群范数余核由局部 Artin 映射识别为
$$
F_1^\times/N_{n,1}F_n^\times
\simeq\operatorname{Gal}(F_n/F_1).
$$
因 $F_n/\mathbb Q_p$ 阿贝尔，$\Delta$ 在右边的共轭作用平凡。另一方面，赋值映射的目标 $\mathbb Z$ 也有平凡 $\Delta$ 作用。因此，取 $\chi$ 分量后，范数余核和从乘法群限制到单位群时的赋值修正都消失。这给出
$$
N_{n,1}:U_n^\chi\twoheadrightarrow U_1^\chi.
$$
相同理由适用于每个相邻层。不能只说“扩张全分歧，所以单位范数满射”：未取字符时，这个断言通常是错的。这里真正起作用的是非平凡 $\chi$ 与阿贝尔扩张的结合。

Hilbert 90 同样给出
$$
\ker(N_{n,1}:U_n^\chi\to U_1^\chi)
=(\gamma-1)U_n^\chi.
$$
若先在 $F_n^\times$ 中找到一个原像，取 $e_\chi$ 后其赋值自动为零。过渡到 pro-$p$ 完成没有引入新的 $p$ 群上同调误差：素于 $p$ 的剩余域单位对有限 $p$ 群的上同调为零，赋值群的完成仍只出现在平凡字符中。

最后，用各层原像集合的紧性取得相容原像，便得精确同构
$$
U_\infty^\chi/(\gamma-1)U_\infty^\chi
\simeq U_1^\chi.
$$
本题非异常性给出 $\mu_p\not\subset F_1$。因为 $F_n/F_1$ 的次数是 $p$ 幂，而 $F_1(\mu_p)/F_1$ 的次数整除 $p-1$，所有 $F_n$ 也不含 $\mu_p$。因此没有单位的 $p$ 挠干扰。结合 R16 的首层自由秩一、Rubin Proposition 11.4 的有限生成和无挠性，Nakayama 引理确实把首层生成元提升成整个 $\mathbb Z_p[[\Gamma]]$ 的基底。

这也与 Coates–Wiles 1978 Theorem 1 在非异常、非平凡字符下的精确有限层控制一致；无需将一个伪同构误当作同构。

## 2. 辅助单位的生成性与第一层的识别

Rubin Definition 8.1 的 $\eta_n^{(\mathfrak a)}(\mathcal O_K)$ 使用完整的固定导子范数。取 $\mathfrak a=(7)$ 后，其定义与 R16 的 $\eta_p$ 在第一层吻合；Proposition 8.2(iii) 给出同一系统的准确范数相容性。

关键是辅助因子在整个 Iwasawa 代数中可逆，而不仅是在某个权点非零。在 $\chi$ 分支的局部环
$$
\mathcal A=\mathbb Z_p[[T]],\qquad T=\gamma-1,
$$
中，其剩余值为
$$
\sigma_{(7)}-N(7)\equiv\psi((7))-49=-56\pmod{(p,T)}.
$$
所列素数均不整除 $56$。Rubin Proposition 11.6 的交换辅助理想关系因而把其他所有辅助单位写成这个单位系统的 $\mathcal A$ 倍数。故
$$
C_\infty^\chi=\mathcal A\eta_\infty.
$$
若 $U_\infty^\chi=\mathcal A u_\infty$ 且 $u_\infty$ 的首层是 R16 的标准生成元，则
$$
\eta_\infty=h_p(T)u_\infty,
\qquad \nu_p=v_p(h_p(0)),
\qquad\operatorname{char}(U_\infty^\chi/C_\infty^\chi)=(h_p).
$$
这里无须替换为全部全局单位，亦没有多取一次固定导子范数。

## 3. 高度一中心为 $T=p$，权 $p$ 的参数却在 $p^2\mathbb Z_p$

Rubin Proposition 12.2 使用
$\operatorname{Hom}_\Gamma(X_\infty^\chi,E[\mathfrak p^\infty])$。
选 $\rho_E(\gamma)=1+p$ 后，一个同态满足的关系是
$$
f(\gamma x)=(1+p)f(x).
$$
故相应高度一素理想为 $(T-p)$，不是 $(T)$，也不是把 $\chi$ 取逆后得到的另一个中心。秩二 Kummer 子群使相应特殊化有至少二维，因此特征理想至少有二重因子：
$$
h_p(T)=(T-p)^2g_p(T),\qquad g_p(T)\in\mathbb Z_p[[T]].
$$
另一方面，权 $p$ 仍处于同一个 tame 分支，且参数是
$$
x_p=(1+p)^p-1\in p^2\mathbb Z_p^\times.
$$
这里的记号 $p^2\mathbb Z_p^\times$ 表示赋值恰为 $2$。因此 $v_p(x_p-p)=1$，而
$g_p(x_p)-g_p(0)\in p^2\mathbb Z_p$。这正好给出 R20 的截断比较。

### 插值归一化的使用范围

独立读到的 Rubin Theorem 12.10 印刷式没有 $(k-1)!$；CLS 2009 Proposition 2.4(28) 明确含有 $(k-1)!$。不应由此无条件断言两套全权精确公式仅相差一个单位级数：当 $k>p$ 时，阶乘一般不是 $p$ 进单位。

R20 已收窄到真正需要的权 $k=p$。在这个权点，$(p-1)!$、$\Omega_p$ 及
$$
1-\frac{\pi_E^p}{p}
$$
均为单位；CLS 以最小正实周期定义 $\Omega_E^+$，且对 $D=17>0$ 有周期系数 $\alpha(E)=1$。$p\equiv1\pmod4$ 又保证 $\psi^p$ 的有限导子不变。因此所需的赋值识别
$$
v_p(h_p(x_p))=v_p(c_p^+(E))
$$
不依赖对全权归一化差异作额外推断。

## 4. 为什么这里确实能排除有限的 $p$ 部分

R16 的论证实际上给出更一般的有限层不等式
$$
\boxed{\quad\dim_{\mathbb F_p}\operatorname{Sel}_p(E/\mathbb Q)
\le\nu_p.\quad}
$$
为避免和临界值 $c_p^+$ 混淆，写
$c=\dim_{\mathbb F_p}\operatorname{Cl}(K_1)[p]^\chi$，
$m$ 为辅助单位在全局单位格中的深度，$a$ 为全局单位格局部化后的指数。
R16 已给 $c\le m$、$\nu=m+a$ 以及
$s:=\dim\operatorname{Sel}_p=2\lceil c/2\rceil$。

若 $c$ 偶数，则 $s=c\le m\le\nu$。若 $c$ 奇数，则 $s=c+1$；而 $a=0$ 时，R16 的 idèle 比较会给 $s=c$，与偶性矛盾。因此 $a\ge1$，从而 $s=c+1\le m+a=\nu$。

于是当临界值赋值至多 $3$ 时，R20 给 $\nu\le3$，故 $s\le3$。已知秩二与 Selmer 偶性强迫 $s=2$，所以 $\Sha[p]=0$。任何非零的 $p$ 幂挠群都有非零的 $p$ 阶元，因此整个 $\Sha[p^\infty]$ 为零。

这个加强控制的是有限层 Selmer 维数；它包含有限 Sha 的 $p$ 阶元。CLS 原文在赋值 $3$ 时使用的余秩论证只排除可除部分。两种结论之间的数学差别由此得到说明，无须推测作者当时采用某种论证的原因。

## 5. 截断点 $4$ 在这套形式论证中已经最优

以下只说明一般整系数级数不能给出更强比较，不构造任何实际椭圆曲线反例。

固定上述 $p$ 和 $x_p$，任取整数 $N\ge3$，置
$$
g(T)=T-x_p+p^N,\qquad h(T)=(T-p)^2g(T).
$$
则 $g\in\mathbb Z_p[T]$，且
$$
v_p(g(0))=2,\qquad v_p(g(x_p))=N.
$$
于是
$$
v_p(h(0))=4,\qquad v_p(h(x_p))=N+2.
$$
两者截断到 $4$ 后相同，但之后可以相差任意大。因此，若要把 R20 的等式提升到完整赋值相等，必须增加关于实际 $g_p$ 的新算术约束。

同一证明给出一般形式：若 $h(T)=(T-p)^r g(T)$ 且 $v_p(x)=2$，则
$$
\min\{v_p(h(0)),r+2\}
=\min\{v_p(h(x)),r+2\}.
$$
把上面的二重因子改为 $r$ 重因子，就得到截断 $r+2$ 的同样最优性例子。

## 一手来源

- K. Rubin, [*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*](https://swc-math.github.io/notes/files/99RubinCM.pdf)：Definitions 8.1、10.7；Propositions 8.2、11.4、11.6、12.2；Theorems 12.9–12.10；Lemma 10.9。已独立读取相关原文。
- J. Coates and A. Wiles, [*On p-adic L-functions and elliptic units*](https://doi.org/10.1017/S1446788700011459)，J. Austral. Math. Soc. (Series A) **26** (1978), 1–25：Theorem 1 及 §§1–2 的非异常条件、Theorems 20–22。已独立读取相关原文。
- J. Coates, Z. Liang and R. Sujatha, [*The Tate-Shafarevich group for elliptic curves with complex multiplication*](https://arxiv.org/abs/0901.3832)：Theorem 2.2、Proposition 2.4(28)、§3 的周期选择。已独立读取相关原文。
- 本题 R4、R7、R12、R16、R20。本文仅补充独立核查与第 5 节的形式最优性结论。
