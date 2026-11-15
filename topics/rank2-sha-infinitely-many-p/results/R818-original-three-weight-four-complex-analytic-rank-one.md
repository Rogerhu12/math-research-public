# R818 — 原三个十八阶权四角色的严格复中心导数

日期：2026-11-15。

状态：已证明。公开严格球计算已完成；三个原固定角色的复解析秩均恰为一。

本篇只处理 R806 已固定的三个完整 Hecke 角色。角色、导子、复嵌入和原二、三、十七处数据均先于任何普通素数固定。本篇的计算不选择或扫描新的研究素数，也不将复中心导数非零改写为跨素数的 Abel–Jacobi 非零。

## 1. 固定来源和解析归一化

令
$$
K=\mathbf Q(\omega),\qquad \omega^2+\omega+1=0,\qquad
\delta=1+2\omega,\qquad
\mathcal J=\{4,10,16\}.
$$
沿 R806 的原完整有限角色定义
$$
\eta_j((a))
=\left[
\operatorname{Teich}_{\mu_3}(a\bmod2)^{-1}
(a\bmod17)^{16(j-9)}
\right]^{-1},
\qquad
\lambda_j=\eta_j^{-1}\psi_0^3 .
\tag{1}
$$
有限幂按 R806 的同一个 $\mu_{18}$ 提升解释。
$\psi_0$ 是 $y^2=x^3+1$、微分 $dx/(2y)$ 的原 CM 角色。
三个 $\lambda_j$ 的理想值无穷型均为 $(3,0)$，导子均准确为
$34\delta$，中心在 $s=2$；它们的完整 root number 均为 $-1$。
对应三个正规化 weight4 cusp forms
$$
f_j(z)=\sum_{n\ge1}a_{j,n}e^{2\pi inz}
$$
的 level 均为
$$
N=|D_K|\operatorname N(34\delta)=10404=102^2 .
\tag{2}
$$
这里使用 R806 的全 2/3/17 表；不由 CM13 特征值猜角色或 conductor。

置
$$
\Lambda_j(s)=N^{s/2}(2\pi)^{-s}\Gamma(s)L(\lambda_j,s).
\tag{3}
$$
则
$$
\Lambda_j(s)=-\Lambda_j(4-s),\qquad L(\lambda_j,2)=0.
\tag{4}
$$
因 $\Gamma(2)=1$，在中心准确有
$$
L'(\lambda_j,2)=\frac{4\pi^2}{N}\Lambda'_j(2).
\tag{5}
$$
(5)中没有遗漏对完成因子求导的项：该项乘 $L(\lambda_j,2)=0$。

## 2. 从原理想角色恢复全部 Dirichlet 系数

$K$ 的 class number 为1。每个素于 $6$ 的整理想有唯一
$2\delta$-primary 生成元 $\alpha=a+b\omega$，准确条件为
$$
a\equiv1\bmod2,\qquad b\equiv0\bmod2,\qquad a+b\equiv1\bmod3.
\tag{6}
$$
确实 $(\mathcal O_K/2\delta)^\times$ 的六个类由六个单位简单传递，
所以 (6) 恰选一个生成元，并且 $\psi_0((\alpha))=\alpha$。
因此 (1)给
$$
\lambda_j((\alpha))
=\alpha^3\,\iota\bigl((\alpha\bmod17)^{16(j-9)}\bigr),
\tag{7}
$$
因为 (6)下 dyadic Teich 因子恰为1，而非被任意删除。

工作在
$$
\mathbf F_{17^2}=\mathbf F_{17}[\omega]/(\omega^2+\omega+1).
$$
选择范数一群的生成元 $g$，满足
$$
g^6=\omega,\qquad g^9=-1,
$$
并令 $\iota(g)=\zeta_{18}=e^{2\pi i/18}$。
这样的 $g$ 恰有三个；它们是同一固定 $K$ 嵌入上
$\mathbf Q(\zeta_{18})$ 的三个选择。替换 $g$ 只置换原三个角色，
不会产生新有限角色。脚本选择字典序最小者仅为可复现标签。

原完整系数于是准确为
$$
a_{j,n}
=\sum_{\substack{a^2-ab+b^2=n\\(n,102)=1\\a,b\text{ 满足 }(6)}}
 (a+b\omega)^3\,
 \zeta_{18}^{(j-9)\log_g((a+b\omega)^{16})}.
\tag{8}
$$
对 $(n,102)>1$ 定义 $a_{j,n}=0$，这与真正 primitive Hecke
$L$-series 的 ramified Euler 因子一致。没有删掉额外好位 Euler 因子。

所有系数首先在
$$
\mathbf Z[Z]/(Z^6-Z^3+1)
$$
中精确计算，再作复数嵌入；不以浮点数识别角色或合并理想。
共轭理想和共轭系数成对，所以 $a_{j,n}$ 为实数。
脚本精确核对共轭不变性、$a_{j,1}=1$、$a_{j,25}=-125$，
以及规定的有限组好素数的原 Hecke 递推。
这些核对不替代 (7)–(8) 的来源证明。

对 $n\le B$，枚举
$$
|a|,|b|\le2(\lfloor\sqrt B\rfloor+1)
$$
包含 (8) 的全部项：由
$a^2-ab+b^2\ge3a^2/4$ 及其 $a,b$ 对称式即可。
故不存在未说明的理想或共轭遗漏。

## 3. 完整中心导数公式

令
$$
c=\frac{2\pi}{102},\qquad F_j(x)=f_j(ix/102).
$$
原 Fricke 关系为
$
F_j(1/x)=-x^4F_j(x).
$
它由 (4) 对应的原正规化 newform 给出；在 $x=1$ 特别有 $F_j(1)=0$。
将 Mellin 积分在 $1$ 处分段，并在下半段代入 $x\mapsto1/x$，得到
$$
\Lambda_j(s)
=\int_1^\infty F_j(x)
       \bigl(x^{s-1}-x^{3-s}\bigr)\,dx .
\tag{9}
$$
在 $s=2$ 求导得到
$$
\boxed{\Lambda'_j(2)
=2\int_1^\infty F_j(x)x\log x\,dx
=2\sum_{n\ge1}a_{j,n}K(cn),}
\tag{10}
$$
其中
$$
K(x)=\int_1^\infty e^{-xt}t\log t\,dt
=\frac{E_1(x)+e^{-x}}{x^2},
\qquad
E_1(x)=\int_x^\infty\frac{e^{-u}}u\,du .
\tag{11}
$$
(11)由分部积分两次直接得到。$x>0$ 时该核严格正。
下节的绝对收敛估计同时支付 (9)求导和 (10)换序。

## 4. 严格无条件全尾界

每个范数为 $n$ 的整理想满足 $|\lambda_j(\mathfrak a)|=n^{3/2}$。
此类理想的个数至多 $d(n)$，且 $d(n)\le2\sqrt n$，所以
$$
|a_{j,n}|\le d(n)n^{3/2}\le2n^2
\tag{12}
$$
对三个角色及其所有所选复嵌入同时成立。

由 $E_1(x)\le e^{-x}/x$，取 $M=B+1$ 得
$$
\begin{aligned}
\left|\Lambda'_j(2)
-2\sum_{n=1}^{B}a_{j,n}K(cn)\right|
&\le\frac4{c^2}\sum_{n\ge M}e^{-cn}
                  \left(1+\frac1{cn}\right)\\
&\le
\boxed{
\frac4{c^2}\left(1+\frac1{cM}\right)
\frac{e^{-cM}}{1-e^{-c}}
=:T_B.}
\end{aligned}
\tag{13}
$$
这是真正无限尾界，不是一次截断稳定或小数位比较。

同时 root $-1$ 给 $F_j(1)=0$。
脚本以另一个完整尾界支付这个归一化相容性核对：
$$
\left|F_j(1)-\sum_{n=1}^B a_{j,n}e^{-cn}\right|
\le
2e^{-cM}
\left(
\frac{M^2}{1-r}
+\frac{2Mr}{(1-r)^2}
+\frac{r(1+r)}{(1-r)^3}
\right),\quad r=e^{-c}.
\tag{14}
$$
(14)只作实际 phase/level 相容性检查；root 本身由 R806 的完整 epsilon
证明给出。

## 5. 公开严格球证书

唯一 producer 为
`scripts/check-r818-original-three-complex-central-derivatives.py`。
参数固定为 `--terms 2048 --bits 384`，依赖 python-flint 0.9.0。
它对 (8)先作精确整环运算，再以 Arb 的严格实球计算
$\cos(k\pi/9)$、$\exp(-cn)$ 和
$\Gamma(0,cn)=E_1(cn)$。所有误差均由库的包含区间保留。
非零判据是完整部分和球严格在 $T_B$ 球的正上方或负下方；
不使用区间中点或未经认证的小数舍入。

公开 GitHub Actions 运行已经成功，作者和根线程均已读完整日志；未重跑或另选参数。

- run：`43757109911`；job：`132943495723`。
- source commit：`7bff268dae6c9c2a73ee5ebb72786cca15e2eafc`。
- 参数：`--terms 2048 --bits 384`；python-flint `0.9.0`。
- 脚本 SHA256：`3131b552e728961167b4b2b1f3ab09a594fbfdc4f722f62bfa524a43dd9f3452`。
- stdout：4005 bytes；SHA256 `669fdf8ca39d11896d14e8491b3ca4b1b388a22389b4a098fc1080713f25caed`。
- 全部精确系数表的规范 SHA256：`54b768858d2a0c09c9f47bd1ccd0f62350eaaea0580c37635b9a1229e35e4320`。
- 公开日志：<https://github.com/Rogerhu12/math-research-public/actions/runs/43757109911/job/132943495723>。

运行中三个可用生成元依次为 $(2,11),(6,8),(9,15)$，固定选择 $g=(2,11)$；
$(6,8)$ 正是 R806 的 $2+4\delta$。下表的 $j$ 是所选系数域嵌入下 (8) 的标签；
转换回另一既有嵌入时只置换三行，不把字典序选择当作额外的原全局标号认同。

严格全尾满足
$
T_{2048}<2.718\cdot10^{-51},\qquad
\frac{4\pi^2}{10404}T_{2048}<1.032\cdot10^{-53}.
\tag{15}
$
将此无限尾加入每个 Arb 部分和球后，得到下列严格有理开区间：

| 所选嵌入标签 $j$ | 完整 $\Lambda'_j(2)$ 所在区间 | 完整 $L'(\lambda_j,2)$ 所在区间 |
|---|---:|---:|
| $4$ | $(1000.2818,1000.2819)$ | $(3.7956,3.7957)$ |
| $10$ | $(2245.1915,2245.1916)$ | $(8.5194,8.5195)$ |
| $16$ | $(1751.1165,1751.1166)$ | $(6.6446,6.6447)$ |

三个 Fricke 检查 (14) 均通过，全部精确角色和 Hecke 检查均通过。
这些粗区间已足以独立读出非零，证明不依赖日志中保留的更多小数。
结合 (4)，结论为
$
\boxed{\operatorname{ord}_{s=2}L(\lambda_j,s)=1\quad(j=4,10,16).}
\tag{16}
$
这里只在仓库保留 producer、参数及上述 run/hash；可重算系数和球输出不另存仓库或 Release。

## 6. 对原固定几何的准确作用

R814 先于研究素数固定了一个共同 good pair $(g,\chi_j)$，
其 companion 复值均非零。§5 已证明三个判据全部成立，故原 factorization
给三个固定 Rankin $L$-functions $L(g/K,\chi_j,s)$
在 $s=2$ 的阶数均恰为1。这个结论不更换 R814 的辅助角色、
几何 variety 或三个 cycle，也不由数值标签选择新的 good pair。

本篇与 R817 付的是两个不同事实：R817 在一个固定普通素数检测三个原
$p$-adic 值，并由该素数上的 Abel–Jacobi 映射推出固定 cycle 非零；
本篇检测同三个固定动机的复解析秩。对任意其他普通素数，
仍需原 R804/R811/R814 的实际局部化或 Abel–Jacobi 非零。
二者之间没有在本篇添加无证的跨素数注入。

具体说，Castella 的 A.1.1 以所选非经典 Katz 值非零推出 Selmer rank1，
A.2.1 以 Selmer dimension1 推出 Heegner class 非零；
Remark1.2.1及 A.1.2 明确保留 weight $>2$ 时从复 rank1
到所选 $p$-adic 值非零的缺口。因此本篇不会把 (10)非零代入一个
尚未满足的局部假设，也不据此赋原三项线性负二行或原三条中央导数非零。

## 7. 依赖与 primary 文献

- [R806](R806-original-type-four-order-eighteen-and-negative-two-katz.md)：完整 $\eta_j$、原 Schwartz、conductor $34\delta$、
  三条 weight4 角色及 root $-1$。
- [R804](R804-original-order-eighteen-soule-classes-and-negative-two-localization.md)、[R811](R811-canonical-soule-classes-and-global-heegner-comparison.md)：原 canonical 类、双 Euler 和仅在该 canonical 线上的严格核结果。
- [R814](R814-common-fixed-good-pair-and-three-original-aj-squares.md)：同一个先于 $p$ 固定的 good pair 与三个 cycle。
- [R817](R817-fixed-prime-original-negative-two-and-nonzero-fixed-cycles.md)：固定 $p=7993$ 的三个原单位负二值及固定 cycle 非零。
- F. Castella, *Tamagawa number conjecture for CM modular forms and
  Rankin–Selberg convolutions*, Remark1.2.1、RemarkA.1.2、
  TheoremA.1.1与 TheoremA.2.1：
  <https://arxiv.org/html/2407.11891v3>。
- python-flint 0.9.0，Arb 完整包含区间 API：
  <https://python-flint.readthedocs.io/en/stable/arb.html>。
