# CM Frobenius 在固定四次模型上的第一除法层

**可信度：下述公式及证明已完成。** 日期：2026-11-12。本文继续 R18、R19、R21，给出一个实际的低层计算，而非把整个 Katz 测度假设为有限原子。结果只控制第一层；末节明确说明它尚未提供所需的无穷次赋值上界。

## 1. 记号与主公式

固定
$$
E:y^2=x^3-17x,\qquad K=\mathbb Q(i),
$$
并采用四次模型坐标
$$
X=\frac yx,\qquad Z=x+\frac{17}{x}.
$$
于是
$$
Z^2=X^4+68,\qquad \omega=\frac{dX}{Z},
\qquad\delta X=Z,\quad\delta Z=2X^3.
\tag{1}
$$
这里 $\omega=dx/(2y)$，$\delta$ 是其对偶不变导子。四次模型在无穷远有两个点，分别对应原模型的 $O$ 和 $T=(0,0)$；记 $D_\infty=O+T$。函数 $X$ 在这两点各有一个单极点。

取 $p\equiv1\pmod4$、$p\ne17$，选择 $\mathfrak p\mid p$，并将 $K_\mathfrak p$ 识别为 $\mathbb Q_p$。令
$$
\pi=\psi_E(\mathfrak p),\quad \pi\bar\pi=p,
\quad h_p=\bar\pi\pmod{\mathfrak p}\in\mathbb F_p^\times,
\quad r=\frac{p-1}{4}.
$$
CM Frobenius 定理给出 $[\pi]\bmod\mathfrak p=\operatorname{Frob}_p$。因而 $[\pi]$ 在 $\mathfrak f$-torsion 上的作用就是 R18 所用的算术 Frobenius。这里使用的是已在 R6、R18 固定的 Hecke 字符规范，不能任意把 $\pi$ 乘以单位。

定义
$$
q_p(68)=\frac{68^{p-1}-1}{p}\pmod p
$$
以及显式奇多项式
$$
J_p(X)=h_p^{-1}
\sum_{\substack{0\le k\le2r\\k\ne r}}
\binom{2r}{k}68^{2r-k}\frac{X^{4k+1}}{4k+1}
\in\mathbb F_p[X].
\tag{2}
$$
其中所有分母均非零：$1\le4k+1\le2p-1$，唯一可能被 $p$ 整除的项恰为已删除的 $k=r$。

**第一层公式。** 在四次模型仿射部分的 $p$-进形式完备化上，
$$
\boxed{\quad
X\circ[\pi]
\equiv X^p+p\left(J_p(X)-\frac{q_p(68)}4X^p\right)
\pmod{p^2}.
\quad}
\tag{3}
$$
式中将 $J_p$ 与 $q_p(68)$ 任意整提升即可；不同提升不改变模 $p^2$ 的表达式。特别地，式 (3) 可在约化不等于 $O,T$ 的任意整点处求值，包括 R18 的固定 $\mathfrak f$-torsion 点。

还成立
$$
\boxed{\quad
h_p=\binom{2r}{r}68^r\pmod p,
\qquad X(X^4+68)\mid J_p(X).
\quad}
\tag{4}
$$

## 2. 除以 $p$ 后的极点界

令
$$
B_p=\frac{X\circ[\pi]-X^p}{p}.
\tag{5}
$$
不能仅从分子在一个仿射开集上约化为零，就假定 $\overline B_p$ 仍具有原来的特征零极点界。这里需实际控制合并到无穷远的核点。

在 $\mathbb Z_p$ 上的光滑 proper 模型上，$[\pi]$ 固定 $O,T$。对于 $T$，这由 $T\in E[1+i]$ 及 $\pi$ 在 $\mathbb Z[i]/(1+i)$ 中等于 $1$ 得出。因此
$$
[\pi]^*D_\infty-D_\infty
$$
是有效 Cartier 因子。置
$$
\mathcal D_p=pD_\infty+[\pi]^*D_\infty-D_\infty.
$$
$X\circ[\pi]$ 和 $X^p$ 都是 $\mathcal O(\mathcal D_p)$ 的整截面。其差在特殊纤维上为零，因为 $[\pi]$ 的约化是 $p$ 次 Frobenius。由整线丛的正合列
$$
0\longrightarrow\mathcal O(\mathcal D_p)
\xrightarrow{\ p\ }\mathcal O(\mathcal D_p)
\longrightarrow\mathcal O(\mathcal D_p)|_{\mathbb F_p}
\longrightarrow0
$$
在全局截面处的正合性，$B_p$ 也是该线丛的整截面。

特殊纤维上，Frobenius 的因子拉回给出
$$
\overline{\mathcal D_p}=(2p-1)D_\infty.
\tag{6}
$$
因此 $\overline B_p$ 只可能在 $O,T$ 有极点，且极点阶均至多 $2p-1$。

自同构 $\tau(P)=T-P$ 在四次模型上为
$$
\tau(X,Z)=(X,-Z).
$$
因 $[\pi]T=T$，$[\pi]$ 与 $\tau$ 交换。因此 $B_p$ 是 $\tau$-不变函数，约化后属于 $\mathbb F_p(X)$。唯一允许的极点在 $X=\infty$，故
$$
\overline B_p\in\mathbb F_p[X],\qquad
\deg\overline B_p\le2p-1.
\tag{7}
$$
又因 $[-1]$ 将 $X$ 送到 $-X$，$B_p$ 及其约化都是奇函数。

这也解释式 (3) 的求值范围：特征零下 $X\circ[\pi]$ 仍在非零核点等处有极点；这些点在特殊纤维中全部落到 $O,T$。我们没有声称它是整个特征零仿射曲线上的多项式，而是在去掉 $O,T$ 后的 $p$-进形式完备化中作模 $p^2$ 的计算。

## 3. 微分唯一确定除一个 $X^p$ 项以外的修正

链式法则给
$$
\delta B_p=\frac\pi p(Z\circ[\pi])-X^{p-1}Z.
$$
约化后，$\pi/p=\bar\pi^{-1}$，$Z\circ[\pi]\equiv Z^p$，故
$$
\frac{d\overline B_p}{dX}
=h_p^{-1}(X^4+68)^{(p-1)/2}-X^{p-1}.
\tag{8}
$$

现直接核对这里 $X^{p-1}$ 的系数确实抵消。设 $a_p=p+1-\#E(\mathbb F_p)$。四次模型有两个有理无穷远点，因而
$$
a_p=-1-\sum_{x\in\mathbb F_p}
\left(\frac{x^4+68}{p}\right).
$$
在模 $p$ 的求和中，Euler 判据及
$\sum_{x\in\mathbb F_p}x^m=-1$ 当 $m>0$ 是 $p-1$ 的倍数、否则为 $0$，给出
$$
\sum_x(x^4+68)^{2r}
\equiv-\binom{2r}{r}68^r-1\pmod p.
$$
因此
$$
a_p\equiv\binom{2r}{r}68^r\pmod p.
$$
另一方面 CM 特征多项式给 $a_p=\pi+\bar\pi$，所以该值就是 $h_p$。这证明式 (4) 的第一个等式，并说明 (2) 的 $J_p$ 满足 (8)。

由 (7)、(8)，$\overline B_p-J_p$ 是次数至多 $2p-1$、导数为零的多项式，故只能是 $c+\kappa_pX^p$。奇性消去常数项：
$$
\overline B_p=J_p+\kappa_pX^p,
\qquad\kappa_p\in\mathbb F_p.
\tag{9}
$$

## 4. 四个分支点给出准确的固定底数 Fermat quotient

在四个分支点 $Z=0$，有 $X=b$、$b^4=-68$。这些点是 $\tau$ 的不动点，也就是满足 $[2]P=T$ 的四个点。$[\pi]$ 置换这四点，且其约化是 Frobenius。

所有四点都在 $p$ 处不分歧，$b$ 为单位。若 $b'=X([\pi]P)$，则
$$
(b')^4=b^4=-68,\qquad b'\equiv b^p\pmod p.
$$
写 $b'/b^p=1+pB_p(P)/b^p$，取四次方模 $p^2$：
$$
1+4p\frac{B_p(P)}{b^p}
\equiv(-68)^{1-p}
\equiv1-pq_p(68)\pmod{p^2}.
$$
故
$$
\frac{\overline B_p(P)}{b^p}
=-\frac{q_p(68)}4.
\tag{10}
$$

式 (2) 在 $b$ 处还有一个准确相消。因为 $p=4r+1$，
$$
\frac{J_p(b)}{b^p}
=h_p^{-1}68^r
\sum_{\substack{0\le k\le2r\\k\ne r}}
\frac{(-1)^{k-r}\binom{2r}{k}}{4k+1}.
\tag{11}
$$
将 $k=r+j$ 与 $k=r-j$ 配对。两项的二项式系数相同，符号同为 $(-1)^j$，而分母模 $p$ 分别为 $4j$ 与 $-4j$，所以每对之和为零。这证明 $J_p(b)=0$。四个分支根互异，又因 $J_p$ 是奇多项式，得到式 (4) 的第二个整除。

将 (10)、(11) 代入 (9) 得
$$
\kappa_p=-\frac{q_p(68)}4.
$$
主公式 (3) 至此全部证明，没有留下随 $p$ 变化的未定积分常数。

## 5. 固定 $\alpha$ 的 trace 及已知第一层相消

沿用 R18 的 $P_f=(u,v)$、$\alpha=v/u$、$M=K(\alpha)$，有
$$
X(P_f)=\alpha,\qquad
\operatorname{Tr}_{M/K}\alpha=0,
\qquad\alpha\in\mathcal O_M[1/34]^\times.
$$
CM reciprocity 给
$$
B_p(P_f)=\frac{\sigma_{\mathfrak p}\alpha-\alpha^p}{p}
=-\mathcal F_{\mathfrak p}(\alpha).
$$
所以 (3) 在此处求值，得到完整的首层公式
$$
\mathcal F_{\mathfrak p}(\alpha)
\equiv-J_p(\alpha)+\frac{q_p(68)}4\alpha^p
\pmod{\mathfrak p}.
\tag{12}
$$
对 $M/K$ 取 trace。由于
$\operatorname{Tr}\alpha^p\equiv
\operatorname{Tr}\sigma_{\mathfrak p}\alpha=0\pmod{\mathfrak p}$，固定底数 $68$ 的 Fermat quotient 项在 trace 中消失。因此
$$
\boxed{\quad
\frac{b_0(p)}p
\equiv-\operatorname{Tr}_{M/K}J_p(\alpha)
\pmod{\mathfrak p}.
\quad}
\tag{13}
$$
结合 R17 的已知秩二整除 $b_0-pb_1\in\mathfrak p^2$，也可写为
$$
b_1(p)\equiv-\operatorname{Tr}_{M/K}J_p(\alpha)
\pmod{\mathfrak p}.
\tag{14}
$$

## 6. 已获得的约束和仍需计算的层

式 (3) 证明，第一 Frobenius 除法层确实可由一个明确的二项式多项式和一个固定整数的 Fermat quotient 控制。它不把 $[\pi]$ 降为一个固定度数的特征零函数：$\deg J_p=2p-1$ 仍随 $p$ 增长。

更关键的是，式 (12) 中唯一单独出现的 $q_p(68)$ 在目标 trace 中恰好消失。因此即使知道无穷多个 $p$ 是底数 $68$ 的非 Wieferich 素数，也不能仅凭本公式推出目标 $a_{(p-3)/2}\notin\mathfrak p^4$。需要继续计算模 $p^2,p^3$ 的 Frobenius 商，并同时保留 R17 的 $b_2,b_3$ 或 R21 的后两个 tame 系数。

这不是 R20 截断赋值比较的重复证明：本文实际计算了一个原先未显式给出的同源第一除法层及其积分常数。但在已有结论的逻辑上，(13)、(14) 只解释最低两层的相消，尚未给出新的无穷性输入。固定 $\Phi$ 的范数分布也不能单独替代原始椭圆单位生成元条件；对 $\Phi$ 人为施加中心因子仍可保留范数关系而使所有 $p$ 的深度增加。

## 依赖与来源

- 本题 R18：固定域 $M$、$\alpha$ 的零 trace、单位性及其 Frobenius–Fermat quotient。
- 本题 R17：四层表达式及已知秩二整除。
- CM Frobenius 在 good split 素位的标准识别采用本题 R6/R18 的 Hecke 字符规范；可见 K. Rubin，*Elliptic Curves with Complex Multiplication and the Conjecture of Birch and Swinnerton-Dyer*，[1999 讲义](https://swc-math.github.io/notes/files/99RubinCM.pdf)，CM reciprocity 与 Hecke 字符章节。本文其余微分、极点及分支点计算均已给出完整证明。
