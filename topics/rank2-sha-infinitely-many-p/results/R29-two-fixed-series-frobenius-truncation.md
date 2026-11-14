# R29. 四层 CM Frobenius 只需两个固定 D-finite 级数

**状态：已证明。** 日期：2026-11-12。会话：Astra-rank2-Sha / cm_iwasawa_routes。

本结果将前述逐层 Frobenius 递推进一步化简：在达到模 $p^5$ 的范围内，整个同源在四次模型上的作用可由两个不随 $p$ 改变的级数给出。这是关于素数对角线的正向有限公式，不是关于全部 CLS 迹序列的特征零递推；它不与 R13 冲突，也没有完成无穷素数目标。

## 1. 两个固定级数和主结论

固定
$$
E:y^2=x^3-17x,\qquad
X=y/x,\quad Z=x+17/x,\qquad Z^2=X^4+68.
$$
取 $p\ge13$、$p\equiv1\pmod4$、$p\ne17$，选择 $\mathfrak p\mid p$ 并在 $K_{\mathfrak p}=\mathbb Q_p$ 中工作。令
$$
\pi=\psi_E(\mathfrak p),\quad \pi\bar\pi=p,\quad
\eta_p=\left(\frac{68}{p}\right)\in\{1,-1\},
\quad\varphi_p(X)=X\circ[\pi].
$$
采用使 $[\pi]$ 的约化为 $p$ 次 Frobenius 的 CM 规范。

定义固定的形式级数
$$
\mathscr L(X)=\int_0^X\frac{du}{\sqrt{1+u^4/68}}
=\sum_{j\ge0}
\frac{(-1)^j\binom{2j}{j}}{272^j(4j+1)}
X^{4j+1}\in X\mathbb Q[[X]].
\tag{1}
$$
这里平方根取常数项为 $1$ 的分支。第二个级数就是 $\mathscr L(X)^5$。记 $[F]_{\le N}$ 为按 $X$ 次数截断至 $N$ 的多项式。

**定理。** 对 $1\le K\le4$，置
$$
N_K=(K+1)p-K.
$$
则在四次模型仿射部分的 $p$-进形式完备化中，
$$
\boxed{\quad
\varphi_p(X)\equiv
\eta_p\left[
\pi\mathscr L(X)+\frac{\pi^5}{680}\mathscr L(X)^5
\right]_{\le N_K}
\pmod{p^{K+1}}.
\quad}
\tag{2}
$$
右边截断后的多项式在 $\mathbb Z_p[X]$ 中。若 $K=1,2$，五次项可整个删去；特别地，
$$
\boxed{\quad
\varphi_p(X)\equiv
\eta_p\pi[\mathscr L(X)]_{\le3p-2}
\pmod{p^3}.
\quad}
\tag{3}
$$
模 $p^4$ 和模 $p^5$ 时一般须保留五次项。

式 (2) 是两个项合并后的截断公式。不同项之间可能在高次系数处相消；我们不声称线性项与五次项分别满足原同源的逐层次数界。

## 2. 先证明整个仿射部分上的次数截断

令 $T=(0,0)$。involution $\tau(P)=T-P$ 在四次模型上为 $(X,Z)\mapsto(X,-Z)$，其商是 $\mathbb P^1_{\mathbb Z_p}$。由于 $\pi$ 是奇 Gaussian 整数，$[\pi]T=T$，所以 $[\pi]$ 下降为商上的 degree $p$ 态射 $\varphi_p$。

$X=\infty$ 对应 $O,T$，两点各自被 $[\pi]$ 固定，故 $\varphi_p(\infty)=\infty$。又因约化为 Frobenius，可取多项式表示
$$
\varphi_p(X)=\frac{N(X)}{D(X)},\qquad
\deg N\le p,\quad\deg D\le p-1,
$$
$$
N\equiv X^p\pmod p,\qquad
D\equiv1\pmod p,\qquad D(0)=1.
\tag{4}
$$
具体地，商上的态射由两条 $\mathcal O(p)$ 的整截面给出，约化是共同单位倍数的 $[X^p:Y^p]$；除去该单位并令分母常数项为一即可。无穷远固定使分母的最高 $X^p$ 系数准确为零。

写 $N=X^p+pN_1$、$D=1+pD_1$。于是
$$
\varphi_p=X^p+
\sum_{j\ge1}p^j
\left(N_1(-D_1)^{j-1}+X^p(-D_1)^j\right).
\tag{5}
$$
第 $j$ 项的次数至多 $(j+1)p-j$。因此
$$
\varphi_p\equiv[\varphi_p]_{\le N_K}\pmod{p^{K+1}}
\tag{6}
$$
是在整个仿射部分的形式完备化中成立的结论，而不只是在 $X=0$ 的有限形式 jet 上成立。

式 (5) 同时说明 $\varphi_p$ 的 Taylor 展开属于限制幂级数环 $\mathbb Z_p\langle X\rangle$。特别地，(6) 可以在任意整的 $X$ 值处求值，包括 $p$-进单位；分母 $D(X)$ 在这些点仍是单位。

## 3. 在两个 $X=0$ 点附近的精确形式恒等式

在不分歧扩张中取 $z_0^2=68$，并记
$$
Q_+=(0,z_0),\qquad Q_-=(0,-z_0)
$$
为四次模型的两个 $X=0$ 点。它们对应原模型的两个非零、不同于 $T$ 的 $2$-torsion 点。

$[\pi]$ 置换这两个点。由于其约化为 Frobenius，$Z$ 坐标上的置换符号为
$$
z_0^p/z_0=68^{(p-1)/2}\equiv\eta_p\pmod p.
$$
两个截面在特殊纤维中不同，故这个符号在特征零中也准确为 $\eta_p$：
$$
[\pi](0,z_0)=(0,\eta_p z_0).
\tag{7}
$$

不变微分为 $\omega=dX/Z$。在 $Q_+$ 附近，
$$
\omega=z_0^{-1}d\mathscr L(X),
$$
而在目标点 $(0,\eta_p z_0)$ 附近为
$(\eta_p z_0)^{-1}d\mathscr L(X)$。因此
$[\pi]^*\omega=\pi\omega$ 与两边在 $X=0$ 处的常数项为零给出
$$
\boxed{\quad
\mathscr L(\varphi_p(X))=\eta_p\pi\mathscr L(X).
\quad}
\tag{8}
$$
令 $\mathscr E=\mathscr L^{-1}$ 为形式复合逆。由奇性，
$$
\varphi_p(X)=\eta_p\mathscr E(\pi\mathscr L(X)).
\tag{9}
$$
这是 $X=0$ 附近的精确特征零形式恒等式，尚未把 $\mathscr L$ 在单位点代入无限和。

## 4. 只剩一次项和五次项的完整估值证明

写
$$
\mathscr E(z)=\sum_{m\ge1}e_mz^m.
$$
由 (1)，$\mathscr L(iX)=i\mathscr L(X)$，故其逆也具有相同对称性：
$$
e_m=0\quad\text{除非 }m\equiv1\pmod4.
\tag{10}
$$
比较最初两项，
$$
\mathscr L(X)=X-\frac{X^5}{680}+O(X^9),
\qquad
\mathscr E(z)=z+\frac{z^5}{680}+O(z^9).
\tag{11}
$$

考虑整的导子
$$
\mathscr D=\sqrt{1+X^4/68}\,\frac d{dX}.
$$
对所列 $p$，它的系数属于 $\mathbb Z_p[[X]]$。它是参数 $\mathscr L$ 的微分算子，因此
$$
m!e_m=(\mathscr D^mX)(0)\in\mathbb Z_p.
$$
所以有统一下界
$$
v_p(e_m)\ge-v_p(m!).
\tag{12}
$$

现在只看次数 $n\le N_K<5p$。因 $p\ge13$，还有 $N_K<p^2$。式 (1) 的二项式分子 integral，$272$ 为单位。分母 $4j+1$ 在此范围内若被 $p$ 整除，必须为 $p,2p,3p$ 或 $4p$；但非零项的次数是 $1\pmod4$，而 $p\equiv1\pmod4$，因此唯一可能的特殊项就是次数 $p$，且其分母只有一个 $p$ 因子。

在 $\mathscr L^m$ 的次数不超过 $N_K$ 的任何乘积中，特殊项 $X^p/p$ 至多出现
$$
\left\lfloor N_K/p\right\rfloor=K
$$
次。因此每个相关系数的赋值至少为 $-K$。结合 (12)，
$$
v_p\!\left([X^n]\pi^me_m\mathscr L(X)^m\right)
\ge m-v_p(m!)-K.
\tag{13}
$$
只有 $m\le n\le N_K<5p<p^2$ 才可能有贡献，所以
$v_p(m!)=\lfloor m/p\rfloor$。对所有 $m\ge9$，$p\ge13$ 给出
$$
m-\lfloor m/p\rfloor\ge9.
$$
于是 (13) 至少为 $9-K\ge K+1$，其中最后一步正使用 $K\le4$。因此所有 $m\ge9$ 的项模 $p^{K+1}$ 消失。

对 $m=5$，$e_5=1/680$ 为单位，(13) 给出下界 $5-K$。在 $K=1,2$ 时它至少为 $K+1$，所以五次项也消失；在 $K=3,4$ 时不能据此删掉。

对一次项，唯一的分母 $p$ 被 $\pi$ 抵消；对五次项，至多 $K\le4$ 个分母 $p$ 被 $\pi^5$ 抵消。因此 (2) 右侧确实是整多项式。

将上述估值代入精确形式等式 (9)，先在次数 $\le N_K$ 范围内得到 (2)，再利用已先行证明的全仿射截断 (6)，便得到定理所称的全局模同余。$\square$

## 5. 固定 D-finite 性与一个 unit-root 同余

### 5.1 两个级数都来自固定有限阶微分方程

由 (1) 直接得到
$$
(X^4+68)\mathscr L''+2X^3\mathscr L'=0.
\tag{14}
$$
所以 $\mathscr L$ 是阶至多二的 D-finite 级数。又因
$\mathscr D\mathscr L=1$，有
$$
\mathscr D^6(\mathscr L^5)=0.
$$
展开 $\mathscr D^6$ 后，除去非零最高系数
$(1+X^4/68)^3$，得到一个系数在 $\mathbb Q(X)$ 中的六阶线性微分算子。因此 $\mathscr L^5$ 也是固定的 D-finite 级数，阶至多六。

这里没有把 R17 中的 $R(\log A)^j$ 改称 D-finite。两组级数承担不同角色：本结果描述 CM 同源的有限精度截断，R17 则直接描述 CLS 素数对角矩。

### 5.2 完整证明 $C_pY_p\equiv\bar\pi\bmod p^2$

置
$$
r=(p-1)/4,\qquad
C_p=(-1)^r\binom{2r}{r}17^r,
\quad Q_p=\frac{68^{p-1}-1}{p},
\quad Y_p=(1+pQ_p)^{-1/4}\in1+p\mathbb Z_p.
$$
则
$$
\boxed{\quad C_pY_p\equiv\bar\pi\pmod{p^2}.\quad}
\tag{15}
$$

**证明。** 记 $\ell_p=p[X^p]\mathscr L$。由 (1)，
$$
\ell_p=
\frac{(-1)^r\binom{2r}{r}}{272^r}
=C_p\,68^{-2r}.
$$
因为 $\eta_p68^{-2r}\in1+p\mathbb Z_p$，且其平方为
$(68^{p-1})^{-1}=(1+pQ_p)^{-1}$，主单位中平方根唯一给出
$$
\eta_p68^{-2r}=Y_p^2,\qquad
\eta_p\ell_p=C_pY_p^2.
\tag{16}
$$
由 (2) 在 $K=1$ 的情形，$\varphi_p$ 的 $X^p$ 系数模 $p^2$ 为
$$
\eta_p\frac{\pi}{p}\ell_p
=\bar\pi^{-1}C_pY_p^2.
$$
另一方面，第一层 Frobenius 笔记已证明
$$
\varphi_p\equiv X^p+
p\left(J_p(X)-Q_pX^p/4\right)\pmod{p^2},
$$
且 $J_p$ 的 $X^p$ 系数为零。故同一个系数为
$1-pQ_p/4\equiv Y_p\bmod p^2$。比较并除以主单位 $Y_p$，得到 (15)。$\square$

因此
$$
\Theta_p=\frac{C_pY_p/\bar\pi-1}{p^2}\in\mathbb Z_p
\tag{17}
$$
是一个合法的下一层归一化量。式 (15) 消去了第一阶误差；它没有断言 $\Theta_p$ 为单位，也没有单独给出 Sha 的判据。

## 6. 在固定 $\alpha$ 处的合法有限求值

沿用 R18 的 $M=K(\alpha)$。$\alpha$ 在所有目标素位为单位，而 CM reciprocity 给
$$
\varphi_p(\alpha)=\sigma_{\mathfrak p}\alpha,
\qquad \operatorname{Tr}_{M/K}\alpha=0.
$$
因为 (2) 已证明为全仿射整同余，所以可以在 $\alpha$ 处代入其有限多项式并取 trace：
$$
\boxed{\quad
\operatorname{Tr}_{M/K}
\left(
\eta_p\left[
\pi\mathscr L+\frac{\pi^5}{680}\mathscr L^5
\right]_{\le N_K}(\alpha)
\right)
\equiv0\pmod{\mathfrak p^{K+1}}.
\quad}
\tag{18}
$$
在 $K=2$ 时，
$$
\operatorname{Tr}_{M/K}
\left([\mathscr L]_{\le3p-2}(\alpha)\right)
\in\mathfrak p^2.
\tag{19}
$$
式 (19) 的 trace 确实整：唯一可能有分母 $p$ 的项与
$\operatorname{Tr}\alpha^p=b_0(p)\in\mathfrak p$ 相乘；其他项均整。然后由 (3) 及 $v_{\mathfrak p}(\pi)=1$ 得到所称的二次整除。

这个顺序至关重要：我们先证明全仿射次数截断，再对有限多项式求值。没有把通常只在一个小圆盘收敛的 $\mathscr L(\alpha)$ 或 $\mathscr E(\pi\mathscr L(\alpha))$ 当成已定义的无限和，也没有以 torsion 的全局 $p$-进对数为零来跳过截断误差。

## 7. 与主目标的关系

本结果把同源的模 $p^3$ 计算减为一个固定二阶 D-finite 级数，把模 $p^4,p^5$ 计算减为两个固定 D-finite 级数。它补充了第一层的显式 $J_p$ 及四层递推，提供可直接与 R17、第二权有限系数公式组合的输入。

截断长度仍为 $N_K=O(p)$，而系数 $\pi$ 及截断位置都随 $p$ 改变。式 (18)、(19) 是由固定 torsion 的 Frobenius 置换强迫的同余，本身已经对全部目标素数成立。还没有证明把这些关系与 R17 或 R24 的目标矩组合后，归一化剩余量在无穷多个 $p$ 上非零。

特别地，R13 排除的是完整 $a_n$ 序列的特征零 P-recursive 递推；这里既没有给出那种递推，也没有用固定 D-finite 输入自动推断其素数对角系数非零。新的有限表达式保留了主问题真正缺少的跨素数算术估计。

## 依赖

- R18：固定 $\alpha$ 的零 trace、素位单位性与 CM Frobenius 作用。
- 第一 Frobenius 层笔记：$J_p$ 的完整公式及 $X^p$ 系数，用于 (15)。
- 四层 Frobenius 递推笔记：商模型和次数界的先前版本；本文 §2 已独立重述所需证明。
- 本文 §3–4 完整证明本次使用的形式恒等式、每一个分母估值和有限求值范围。
