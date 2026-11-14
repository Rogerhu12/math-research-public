# R239 附录：两组任意重数加一异常位的整个出生二首末相邻边

日期：2026-11-14（UTC）。作者：Astra-ISP-0c017065 / two_weight_general_height_1856；AI-assisted，GPT-6 Astra Pro。

状态：完整有限模型定理，新增物理出生二的第一与末第一边，普通权比及异常权均任意。一般内部高度尚未由本稿闭合。独立证书为[全参数整数证书](../notes/2026-11-14-birth-two-first-edge-uniform-certificate-0c.py)；全部计算为有限精确有理/整数多项式，未作参数抽样。

依赖：[一般出生与无排序完整源](R239-appendix-general-birth-dual-hankel-and-birth-two-full-source.md)、[已闭整个出生一全高度](R239-appendix-birth-one-two-group-singleton-all-heights-strict-bound.md)、[实际Pearson双对角](R239-appendix-actual-binomial-pearson-bidiagonal-and-full-shear-elimination.md)、[倒数权对偶](R239-appendix-primitive-gram-reciprocal-weight-duality-all-births.md)。小组分别使用[两异常头](R239-appendix-two-exceptional-weights-full-birth-one-primitive-gram-bound.md)、[三异常头全部primitive](R239-appendix-three-exceptional-weights-full-primitive-gram-bound.md)及[三等权头加一位全部出生](R239-appendix-three-equal-short-weights-one-exceptional-birth-one-and-all-births.md)。

## 1. 全空间定理及未被省略的自旋分支

两个等权组大小为 $q,L\ge1$，另有一个异常位；权归一化为 $\sqrt z,1,\sqrt w$，$z,w>0$。总物理位数为 $q+L+1$，出生二高度为 $h=q+L-3$。在整个物理 $K_2=\ker D\cap\mathcal H_2$ 上，令
$$F_j=D^j(D^*)^j/(j!)^2\big|_{\mathcal H_2},\qquad
\Gamma_j=P_{K_2}F_j^{-1}|_{K_2}.$$
所有逆先在完整物理层上取。

**定理。** 若 $h\ge2$，严格有
$$\boxed{\Gamma_1\Gamma_2^{-1}\Gamma_1\prec\Gamma_0,\qquad
\Gamma_{h-1}\Gamma_h^{-1}\Gamma_{h-1}\prec\Gamma_{h-2}.}\tag{1.1}$$
不存在内部比较的较小高度按空陈述读取。

使用一般出生互补 Hankel 稿的实际正交串分解。若两组内部出生为 $(i,j)$，物理出生二的相对出生为 $t=2-i-j$。$t=0$ 的所有重数是严格 Newton 标量分支；$t=1$ 的所有重数由新两组加一位整个出生一全高度定理支付。唯一新增的是 $i=j=0,t=2$ 的二维 primitive；其原群固定出生层是五维，须先取五维全逆再压缩。

若 $\min(q,L)\le3$，已有两、三异常权及三位等权短串加一异常位的全部出生定理支付。故只需 $q,L\ge4$ 的这个五维全逆块。本文的两个重数没有次序要求；下节明确核其短池最高源条件，因而之后可合法交换普通组。

## 2. 无次序的完整 MP、源归一与真实硬端

取 $t=2$，缺失多项式次数 $D=q-1$。将普通短权组与异常位视为 $Q=q+1$ 个头，池大小为 $L$。任意短池完整 MP 中，最高源还须在缺失秩 $r>L+D$ 上为零。但只要 $t\le L$，就有
$$L+D=L+q-t+1\ge q+1=Q.$$
所以这里没有任何额外最高源条件。更一般地，互补 Hankel 稿 §§2–5 的全部公式在 $t\le\min(q,L)$ 下都无需 $q\le L$：出生层仍有 $2t+1$ 个坐标，实际计数支撑至少 $t$ 点、内部至少 $t+1$ 点，两硬端恰为 $t$ 点。原合法值与全部最高系数约束的证明原样适用。此处 $q,L\ge4,t=2$ 满足这些条件。

具体源 $E_w$ 为该稿 (2.1) 的两列；在群固定坐标 $(r,b,l)$、$r+b+l=2$ 上准确为
$$\begin{aligned}
(E_w)_{(r,b,l),1}&=(-1)^l z^{(q-r)/2}w^{(1-b)/2}
\frac{(q-1)!\binom{q-r}{q-1}}{\binom Ll},\\
(E_w)_{(r,b,l),2}&=(-1)^l z^{(q-r)/2}w^{(1-b)/2}
\frac{(q-2)!(1-b)\binom{q-r}{q-2}}{\binom Ll}.
\end{aligned}\tag{2.1}$$
两列始终共用所有高度，真实源 Gram 是 $E_w^*E_w$，其中物理内积含各类子集重数。

令 $\nu_k(i)=\binom qi\binom L{k-i}z^i$，$\Delta_r(k)$ 为它的 $r$ 阶矩行列式，$\Delta_0=1$。定义
$$G_k=\sum_i\nu_k(i),\qquad
F_k=\frac{\Delta_2(k)}{qLz},\qquad
E_k=\frac{\Delta_3(k)}{q^2(q-1)L^2(L-1)z^3}.\tag{2.2}$$
本稿只用 $k=1,2,3,4$，其中 $F_1=E_2=1$，$E_1=0$；其他所有列出的量均严格正。

原首一范数为 $a_j=C_qG_{j+1}/\Delta_2(j+1)$、$b_{j-1}=C_q\Delta_2(j+1)/\Delta_3(j+1)$，$C_q=(q!)^2z^q$。把所有矩阵同时乘 $qLz/C_q$，再对同一源作
$$S=\operatorname{diag}(1,\sqrt{(q-1)(L-1)z})$$
的合同，所得范数准确成为
$$\boxed{a_j=G_{j+1}/F_{j+1},\qquad b_{j-1}=F_{j+1}/E_{j+1}.}\tag{2.3}$$
这里重新使用 $a,b$ 表示缩放后的范数；只作共同正缩放和共同源合同，故保持相邻序。$b_{-1}$ 不被定义成有限量；第零阶的实际更新直接是 $B_0=wb_0$。

## 3. 第一边的有限四次式，未引入无穷 Gram

为简洁写 $g_k=G_k$，并设
$$a=g_1,\quad b=g_2/F_2,\quad c=g_3/F_3,\quad d=g_4/F_4,$$
$$Q=F_2,\qquad r=F_3/E_3,\qquad s=F_4/E_4.$$
置
$$Y=(F_2E_3g_4-F_4g_3)/2,\qquad
\chi=(q-1)(L-1)z(z-1)^2.$$
实际 Pearson 身份在共同源缩放后给中心剪切差
$$x=-\frac{\sqrt\chi\,g_3}{F_2F_3},\qquad
 y=\frac{\sqrt\chi\,Y}{F_2F_3F_4}\quad(z\ge1).\tag{3.1}$$
这就是原硬端 $x=-(z-1)a_2/b_0$ 和相邻内部 $y=(z-1)(a_3/b_1-a_2/b_0)/2$ 的准确共同缩放；没有越界低范数。

消去中心 shear 后，三个实际形式有高系数
$$A_-=a+wb,\quad A_0=b+wc,\quad A_+=c+wd,$$
低系数
$$B_-=wQ,\quad B_0=\frac{wQr}{Q+wr},\quad B_+=\frac{wrs}{r+ws}.$$
令 $\mathcal K=H_0-H_1H_2^{-1}H_1$。其首主子式
$$\mathcal K_{11}=A_--A_0^2/A_++B_-x^2>0$$
由实际旧两权高范数严格 log 凸支付。

写
$$\Lambda=(ac-b^2)+w(ad-bc)+w^2(bd-c^2),$$
$$\Phi=Q(Qs-r^2)+wQrs+w^2r^2s.$$
直接展开这三个有限矩阵，得到完整四次式
$$\overline{\mathcal P}(w)=\det\mathcal K\,(Q+wr)^2(c+wd)s/w,$$
$$\begin{aligned}
\overline{\mathcal P}={}&Q\Lambda\Phi
-wQ^3r(c+wd)(r+ws)x^2\\
&-wQ^2r^2s(a+wb)y^2
-2wQ^2rs(b+wc)(Q+wr)xy\\
&-w^2Q^3r^2s x^2y^2.
\end{aligned}\tag{3.2}$$
它也等于一般内部四次先除端部参数 $p$ 后作硬端极限，但本式的定义和证明完全是有限 $B_-=wQ$ 的矩阵运算。

首末系数准确为
$$\overline{\mathcal P}_0=Q^2(ac-b^2)(Qs-r^2)>0,\qquad
\overline{\mathcal P}_4=Qr^2s(bd-c^2)>0.$$
高、低两条旧范数都是原两权完整问题，严格性由既有全部出生全部高度标量定理支付。

## 4. 三个中间分子的准确形式

将 (3.1) 代入 (3.2)，三个中间系数为 $N_i/\mathcal D_i$，其正单项式分母是
$$\mathcal D_1=E_3^2E_4F_3F_4,\qquad
\mathcal D_2=E_3^2E_4F_2F_3^2F_4,\qquad
\mathcal D_3=E_3^2E_4F_3.\tag{4.1}$$
通用单项式数目为 $9,14,6$。外侧两项完整为
$$\begin{aligned}
N_1={}&E_3F_3F_4^2(F_2^2g_1g_3-F_3g_2^2)\\
&+F_2(F_2F_3g_1g_4-F_4g_2g_3)(F_2F_4E_3^2-F_3^2E_4)\\
&+\chi(2E_3F_4g_2g_3Y-F_2E_4F_4g_3^3-g_1F_3Y^2),
\end{aligned}\tag{4.2}$$
$$\begin{aligned}
N_3={}&F_3^2(F_2F_3g_1g_4-F_4g_2g_3)\\
&+E_3F_2(F_3^2g_2g_4-F_2F_4g_3^2)
+\chi g_3^2(2Y-E_3F_2g_4).
\end{aligned}\tag{4.3}$$
最后一项用实际 $Y$ 恒等于 $-\chi F_4g_3^3$，不能当作非负省略。中间 $N_2$ 从 (3.2) 的 $w^2$ 项准确生成；证书独立重构全部 14 项，并核 (4.1)–(4.3)。

## 5. 全独立重数的整数正系数证书

置 $q=4+x,L=4+y,z=1+u$，其中 $x,y,u\ge0$，两个重数不附加次序约束。对 $1\le k\le4$，用有限下降积二项式准确生成所有 $\nu_k(i)$。再用有限 Cauchy–Binet 公式
$$\Delta_d(k)=\sum_{i_1<\cdots<i_d}
\prod_{a<b}(i_b-i_a)^2\prod_a\nu_k(i_a)$$
生成 $d=2,3$ 行列式，并按 (2.2) 精确整除正公共因子。然后把全部 $g,F,E,Y,\chi$ 代入通用分子。没有插入预先计算的表或使用有限重数样点。

先验总次数界为
$$\deg g_k\le2k,\qquad\deg F_k\le4k-4,\qquad
\deg E_k\le6k-12\quad(k\ge2),$$
$$\deg Y\le18,\qquad\deg\chi\le5.$$
例如 $\Delta_d$ 每项的次数是 $dk+\sum i_a$，互异指标使和至多 $dk-d(d-1)/2$；再减去 (2.2) 中已证可整除的公共因子次数，给上述界。对通用单项式逐项计数，准确上界为
$$\deg N_1\le54,\qquad\deg N_2\le64,\qquad\deg N_3\le38.$$

完整展开及整数化得到：

| 分子 | 公共分母倍数 | 严格正整数项数 | 负项数 | 总次数 | 最小系数 | 常数项 |
|---|---:|---:|---:|---:|---:|---:|
| $N_1$ | 71,663,616 | 7,714 | 0 | 54 | 3 | 1,859,069,183,311,872,000,000 |
| $N_2$ | 859,963,392 | 12,529 | 0 | 64 | 3 | 21,081,844,538,756,628,480,000,000 |
| $N_3$ | 248,832 | 2,870 | 0 | 38 | 3 | 3,688,629,331,968,000 |

各常数项严格正，所以 $N_i>0$ 对整个实正交象限成立，特别覆盖所有整数 $q,L\ge4$ 和 $z\ge1$。这是整个有限多项式的恒等展开与全系数证明，未遗漏任何 $z$ 次数或重数区域。

独立脚本按 QQ 多项式环从上述定义重算全部值，逐个非零系数断言严格正整数，并核项数、次数、最小值及常数项。完整展开已全部通过。脚本还先核通用清分母、$9/14/6$ 项数、两个紧式及先验次数；再对 $(q,L,a,c)=(4,4,2,3),(5,4,1/2,2)$ 的实际五维满层 Gram 先取全逆，用原共同 $E_w$ 与共同缩放验证 (3.2)。第二个例特别核 $q>L$ 的无次序范围。校准仅检查身份，普遍正性由完整多项式证书承担。

## 6. 全权、全部原源与末边

首末及三个中间系数全部严格正，故 $\overline{\mathcal P}(w)>0$ 对任意 $w>0$ 成立。清除因子严格正，所以 $\det\mathcal K>0$；与 §3 首主子式严格正合起来给完整固定二维首边。

若 $z<1$，物理交换两普通组并以原短组权归一，得到 $(L,q,z^{-1},w/z)$。§2 已证明新参数不需保持 $q\le L$，所以证书仍适用；这是实际物理置换和统一权缩放，完整 inverse 及源合同保持合法。$z=1$ 已包含在正系数证书，也可直接由两权定理支付。

物理出生二的其余所有组内分量在 §1 已付；正交直和给整个 $K_2$ 的第一式。最后，对出生二使用真实倒数权对偶的同一源合同 $j\mapsto h-j$，并用正定矩阵等价
$$AB^{-1}A\prec C\iff AC^{-1}A\prec B$$
得到末边。小组与短高度均由 §1 的完整已证范围覆盖，没有对非法范数取逆。

因此 (1.1) 完成。后续仍须支付这个实际 $t=2$ 块的一般内部边；不能把本稿或出生一的负实根相位直接外推为出生二全高度定理。

## 根代理独立桥接核验

[独立符号桥](../notes/2026-11-14-birth-two-first-edge-independent-shear-and-determinant-check-0c.py)直接由真实有限计数权构造Δ2和Δ3，以−ΘlogΔ2的次首身份重新求两个剪切，不使用本文给定的Pearson式作为输入；对无排序符号q/L/z准确验证(3.1)。同一程序另从有限B_-=wQ的三个矩阵重算通用Schur行列式，验证(3.2)，不借无穷Gram的极限。作者完整系数展开及全部通用分母/实际五维校准均已通过；这两类核验分别支付原源身份和有限正性证书的不同环节。
