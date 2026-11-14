# 实际权一因子的完整角色分解与惰性 Hecke 恒等式

日期：2026-11-12。状态：本文的有限 Fourier 分解、全部非单位层、
常数项、diamond 与 Hecke 公式均已证明，并有精确 cyclotomic 证书。
这些是实际权一因子的恒等式，尚未推出中央除 $p$ 行在无穷多个
素数处非零。

## 1. 固定实际对象及层数

取 [R47 的全权一模形式](2026-11-12-central-borel-modular-uniformization.md)
$\mathcal G(\tau)$，而非另一个有相似 CM 性质的 theta series。
置
$$
N=68,\quad \zeta_N=e^{2\pi i/N},\quad
\chi_4=\chi_{-4},\qquad
F(\tau)=\frac{\mathcal G(N\tau)}{2\pi i}.
\tag{1}
$$
$F\in M_1(\Gamma_1(N^2))$，$N^2=4624$。
确实，$\mathcal G\in M_1(\Gamma(N))$；对
$\gamma\in\Gamma_1(N^2)$，把 $\gamma$ 用
$\operatorname{diag}(N,1)$ 共轭后落在 $\Gamma(N)$。
这种固定缩放只为得到整数次的 $q=e^{2\pi i\tau}$ 展开。
本文的标准 $T_p,U_p,V_p,\langle p\rangle$ 首先作用于 (1) 的
$F$；回到原来的 $\mathcal G$ 时明确共轭回去。

原 $256$ 点导子轨道的标签是
$$
\mathcal S=\langle-3,-2+i\rangle\cdot(1,-1)
       \ \subset(\mathbb Z/N)^2.
\tag{2}
$$
这里 $(1,-1)/N=1/(34(1+i))$，即原来的 $\Omega_E/f$ 标签。
两个生成元的作用分别为
$$
(a,b)\mapsto(-3a,-3b),\qquad
(a,b)\mapsto(-2a-b,a-2b).
$$
故原来的每一点、每个相位都保留了。置
$$
w(a,b)=1_{\mathcal S}(a,b)-1_{-\mathcal S}(a,b).
\tag{3}
$$
所有 $\mathcal S$ 中的 $a,b$ 都是奇数，且
$\mathcal S\cap(-\mathcal S)=\varnothing$。

关键标量性质为
$$
\boxed{
w(ua,ub)=\chi_4(u)w(a,b)
\qquad\bigl(u\in(\mathbb Z/N)^\times\bigr).}
\tag{4}
$$
证明只需原轨道中的 $-3$：它在模 $17$ 的阶为 $16$，
在模 $4$ 为 $1$，所以生成全部 $u\equiv1\pmod4$ 的模 $68$ 单位。
其余单位是这些单位的负数，而 (3) 是奇函数。
不需要假定实际 $17$ 角色为平凡。

## 2. 实际 Fourier 系数，含精确常数项

定义一个固定有限 Fourier 核
$$
C(d,e)=\sum_{a\bmod N}w(a,e)\zeta_N^{ad}.
\tag{5}
$$
它对两个指标均以 $N$ 为周期。准确有
$$
\boxed{
F(\tau)=4-\sum_{n\ge1}
       \left(\sum_{\substack{d,e>0\\de=n}}C(d,e)\right)q^n.}
\tag{6}
$$

为核对符号与常数，把每个标签取成 $0<b<N$。
R47 的 completed zeta 项满足
$$
\frac{U_{a/N,b/N}(N\tau)}{2\pi i}
=\frac bN-\frac12
-\sum_{\substack{d\ge1\\j\ge0}}\zeta_N^{ad}q^{d(b+Nj)}
+\sum_{\substack{d\ge1\\j\ge1}}\zeta_N^{-ad}q^{d(Nj-b)}.
\tag{7}
$$
这是 Jacobi theta 乘积对数导数的两个几何级数；
本题 $b$ 为奇数，所以没有 $b=0$ 的额外 cotangent 常数项。
对 $\mathcal S$ 求和，第二个正次数和通过
$(a,b)\mapsto(-a,-b)$ 化成 (5) 的第二部分，得到 (6)。
固定有限和直接给
$$
\sum_{(a,b)\in\mathcal S}
       \left(\frac b{68}-\frac12\right)=4.
\tag{8}
$$
该等式也在下面的精确证书中逐项验证。

由 (4) 换元得到
$$
\boxed{
C(ud,u^{-1}e)=\chi_4(u)C(d,e).}
\tag{9}
$$
尤其
$$
C(ud,e)=\chi_4(u)C(d,ue),\qquad
C(ud,ue)=\chi_4(u)\sigma_{u^2}C(d,e),
\tag{10}
$$
其中 $\sigma_v(\zeta_N)=\zeta_N^v$。

## 3. 包括非单位层的明确有限 Dirichlet 分解

对正整数 $d,e$ 置
$$
g=\gcd(d,N),\quad h=\gcd(e,N),\quad
R=N/g,\quad S=N/h.
$$
(5) 只有在 $h=1$ 或 $h=17$ 时可能非零，因为原标签的第二坐标
是奇数。写 $d=gx,e=hy$，则 $x\in(\mathbb Z/R)^\times$、
$y\in(\mathbb Z/S)^\times$。

取 Dirichlet 角色 $\chi$ 模 $R$，并将它膨胀到模 $N$ 的单位群。
只保留满足
$$
\psi:=\chi\chi_4
\quad\text{能下降为模 }S\text{ 的角色}
\tag{11}
$$
的 $\chi$。定义完全显式的系数
$$
\boxed{
A_{g,h,\chi}
=\frac1{\varphi(R)}
 \sum_{x\in(\mathbb Z/R)^\times}
     C(gx,h)\chi(x)^{-1}.}
\tag{12}
$$
模 $1$ 单位群按单点群处理。
则准确有
$$
C(d,e)=\sum_{\chi\text{ 满足 }(11)}
          A_{g,h,\chi}\chi(d/g)\psi(e/h).
\tag{13}
$$

证明先对 $C(gx,h)$ 作普通有限乘法 Fourier 展开。
对任一 $u\in(\mathbb Z/N)^\times$，(9) 给
$$
C(gx,hu)=\chi_4(u)C(gux,h).
$$
右边的 $\chi$ 分量乘以 $\chi(u)\chi_4(u)$。
若 $u\equiv1\pmod S$，左边不变，因此不满足 (11) 的分量为零；
其余分量准确取得 $\psi(u)$，证明 (13)。
这也证明所有非零分量都满足
$$
\chi(-1)\psi(-1)=-1,
\tag{14}
$$
正是 holomorphic 权一 Eisenstein 的奇偶条件。

令 $E_1(\chi,\psi)$ 表示正次数系数规范为
$$
[q^n]E_1(\chi,\psi)
=\sum_{de=n}\chi(d)\psi(e)
$$
的 Eisenstein series，角色可以不本原。
取通常的模形式常数项，则
$$
\boxed{
F=-\sum_{\substack{g\mid68\\h\in\{1,17\}}}
        \ \sum_{\chi\text{ 满足 }(11)}
 A_{g,h,\chi}\,E_1(\chi,\psi)(gh\,\tau).}
\tag{15}
$$
每项的层数整除
$(gh)(N/g)(N/h)=N^2$。
此处的输入是权一 Eisenstein 的实际构造和 Fourier 展开，
不是由“CM theta”这个名字推测其 Hecke 本征值。
Dasgupta–Kakde（2021），§4 开头、预印本印刷第 15 页，
明确允许 $k=1$ 和非本原角色，并给出上述 divisor-sum 系数；
其权一交换 $\chi,\psi$ 的对称性也在同处说明。

### 3.1 常数项没有遗漏

若 $\chi,\psi$ 是本原角色，权一的常数为
$$
\frac12\bigl(
  1_{\chi=1}L(0,\psi)+1_{\psi=1}L(0,\chi)
\bigr).
\tag{16}
$$
不能在权一时只保留这一对称式的一半。
非本原角色可从本原对分别施加
$1-\chi_0(\ell)V_\ell$ 或 $1-\psi_0(\ell)V_\ell$，
准确删去对应 divisor-sum 中被 $\ell$ 整除的因子。
这种有限操作给出 (15) 中全部非本原常数项。

本题所有含非平凡模 $17$ 角色的分量，两条本原角色都非平凡，
常数为零。其余分量的本原对是 $\{1,\chi_4\}$；
但任何多余的模 $2$ 或模 $17$ 削去因子都使常数为零，
因为 $1(\ell)=1$，且 $\chi_4(17)=1$。
唯一留下的是
$$
g=68,\quad h=17,\quad
\chi=1\pmod1,\quad\psi=\chi_4\pmod4.
$$
(12) 在这里准确为 $A_{68,17,1}=C(0,17)=-16$。
$L(0,\chi_4)=1/2$，所以该项为
$16E_1(1,\chi_4)(1156\tau)$，常数正是 $4$，与 (8) 一致。
即使不单独计算 (16)，(15) 的两边已是权一模形式且全部
正次数系数相同，其差为常数，模变换律同样迫使差为零。

### 3.2 全部 $57$ 个非零分量

取 $3$ 为模 $17$ 的原根，令
$\lambda_k(3)=e^{2\pi ik/16}$、$0\le k<16$，
并以 $\epsilon=0,1$ 表示模 $4$ 因子 $\chi_4^\epsilon$。
下表是 (12) 精确计算的全部非零项：

| $g$ | $h$ | $\epsilon$ | $k$ | 项数 |
|---:|---:|---:|---|---:|
| $1$ | $1$ | $1$ | $0,\ldots,15$ | $16$ |
| $2$ | $1$ | $0$ | $0,\ldots,15$ | $16$ |
| $4$ | $1$ | $0$ | $0,\ldots,15$ | $16$ |
| $17$ | $1$ | $1$ | $0$ | $1$ |
| $34,68$ | $1$ | $0$ | $0$ | $2$ |
| $1,17$ | $17$ | $1$ | $0$ | $2$ |
| $2,4,34,68$ | $17$ | $0$ | $4$ |

因此所有 $15$ 个非平凡模 $17$ 角色都真实出现。
不能把实际分解缩成只含平凡角色或只含一个 quartic 角色。
完整系数由有限公式 (12) 给出，表格没有隐去待定比例。

## 4. 准确的 diamond、Hecke 与两步关系

对 $p\nmid68$，在 (15) 的每一项上，diamond 本征值是
$\chi(p)\psi(p)$，而 $T_p$ 本征值是 $\chi(p)+\psi(p)$。
这些标准公式也可直接由 divisor-sum 与
$T_p=U_p+\langle p\rangle V_p$ 的 $q$-展开核对；
oldform 缩放 $gh$ 与这些好位算子交换。
所以 (10)、(13) 给整个实际 $F$ 的恒等式
$$
\boxed{\begin{aligned}
\langle p\rangle F&=\chi_4(p)\sigma_{p^2}F,\\
T_pF&=(1+\chi_4(p))\sigma_pF.
\end{aligned}}
\tag{17}
$$
这里 $\sigma$ 只作用于 $\mathbb Q(\zeta_{68})$ 中的代数
$q$ 系数，不作用于复常数 $2\pi i$。
常数项也满足 (17)：分别为 $4\chi_4(p)$ 及
$4(1+\chi_4(p))$。

因此对每个惰性 $p\equiv3\pmod4$、$p\ne17$，
$$
\boxed{
T_pF=0,\qquad
U_pF=V_p\sigma_{p^2}F,\qquad
U_p^2F=\sigma_{p^2}F.}
\tag{18}
$$
第二个等式中的 $\sigma_{p^2}$ 不能任意删去。
令 $d_p=\operatorname{ord}_{17}(p^2)\mid8$，则还得到
$U_p^{2d_p}F=F$。

若 $F=\sum a_nq^n$，(18) 等价于
$$
a_{pn}=0\quad(p\nmid n),\qquad
a_{p^2n}=\sigma_{p^2}(a_n)\quad(n\ge0).
\tag{19}
$$
这有一个不经过一般 Hecke 理论的完整独立证明。
直接把 $pn$ 的因子对按哪一个含 $p$ 拆开，重复部分减掉一次，得
$$
a_{pn}=
-\sum_{de=n}\bigl(C(pd,e)+C(d,pe)\bigr)
+1_{p\mid n}\sum_{de=n/p}C(pd,pe).
$$
第一和由 $C(pd,e)=-C(d,pe)$ 抵消；第二和用 (10) 变成
$1_{p\mid n}\sigma_{p^2}(a_{n/p})$。
常数项 $a_0=4$ 同样被 $\sigma_{p^2}$ 固定，
因此直接得到整个 $U_pF=V_p\sigma_{p^2}F$，
再用 $U_pV_p=1$ 得到两步关系。
角色分解另为 $T_p$ 与 diamond 的约定提供完整核对，
不是这个独立系数证明的隐含前提。

回到原来的 $\widetilde{\mathcal G}=\mathcal G/(2\pi i)$，
准确的复变量公式是
$$
\boxed{
\frac1p\sum_{j=0}^{p-1}
 \widetilde{\mathcal G}\!\left(\frac{\tau+68j}{p}\right)
=\sigma_{p^2}\widetilde{\mathcal G}(p\tau).}
\tag{20}
$$
右侧的 Galois 作用按代数 $q^{1/68}$ 系数定义。
这是 (18) 经固定缩放共轭后的等式；
不把原 $\Gamma(68)$ 上的算子约定与
$\Gamma_1(4624)$ 上的标准 $T_p$ 混写。
因为 $p\nmid68$，$68j$ 模 $p$ 仍遍历全部剩余类，
(20) 保留了全部 $p+1$ 条循环同源分支及其层结构运输。

### 4.1 准确接回实际 $M_e,M_o$ 两条截面

令 $\mathcal S^{\rm rot}=\{(b,-a):(a,b)\in\mathcal S\}$，
并由同样的 completed zeta 和定义 $\mathcal G_{\rm rot}$。
旋转与整数标量作用交换，所以该轨道的奇权重仍满足 (4)。
§2–4 的证明逐项适用；特别
$$
F_{\rm rot}(\tau)=\frac{\mathcal G_{\rm rot}(68\tau)}{2\pi i}
\quad\Longrightarrow\quad
U_pF_{\rm rot}=V_p\sigma_{p^2}F_{\rm rot}
\qquad(p\equiv3\pmod4).
\tag{21}
$$
旋转轨道的常数仍是一个有理有限和，因此也被
$\sigma_{p^2}$ 固定；这里没有只比较正次数系数。

沿用[实际固定除法单位模型](2026-11-12-weight-one-division-unit-relative-model.md)
及[实际 Kummer 半线](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)
的准确常数
$$
c_e=\frac{\sqrt2\,17^{17/4}}{4800f},\qquad
c_o=\frac{i\sqrt2\,17^{7/4}}{32f},\qquad f=34(1+i).
\tag{22}
$$
对每个目标惰性 $p\ge7$，这些常数及 $i$ 都被局部算术
Frobenius 的平方固定。证明需要核对四次根：
$\mu_4\subset\mathbb F_{p^2}$，而
$$
17^{(p^2-1)/4}
 =\left(17^{p-1}\right)^{(p+1)/4}=1.
$$
所以 $X^4-17$ 的全部根在 $\mathbb F_{p^2}$ 中。
它们是非零简单根，由 Hensel 引理全部提升到未分歧二次扩张。
$i$ 和 $\sqrt2$ 同样在这个扩张中；$p\ne2,17$ 保证可分性。
故所选正实根式的任意兼容 $p$ 进嵌入都满足
$$
\sigma_{p^2}(c_e)=c_e,\qquad
\sigma_{p^2}(c_o)=c_o,\qquad \sigma_{p^2}(i)=i.
\tag{23}
$$
把此局部作用与 $\mathbb Q(\zeta_{68})$ 上的
$\zeta_{68}\mapsto\zeta_{68}^{p^2}$ 合在同一未分歧复合域中，
即为 (17)–(21) 所需的兼容系数作用。

现在定义真正的权一截面
$$
\begin{aligned}
F_e&=\frac{c_e}{2}(F-iF_{\rm rot}),\\
F_o&=\frac{c_o}{2}(F+iF_{\rm rot}).
\end{aligned}
\tag{24}
$$
若 $t=\lambda-1/2$，$\omega_1=\pi\vartheta_3^2$ 是同一 Legendre
不变微分的周期，实际除法单位模型给
$$
F_e(\tau)=\frac{\omega_1(68\tau)}{2\pi i}
                M_e(t(68\tau)),\qquad
F_o(\tau)=\frac{\omega_1(68\tau)}{2\pi i}
                M_o(t(68\tau)).
\tag{25}
$$
所以 (24) 是原来的 $M_e=t^4+\frac72t^6+\cdots$、
$M_o=t+\frac12t^3+\cdots$ 所对应的模形式截面，
不是另选的相似函数。
由 (21)–(23)，两者分别满足
$$
\boxed{
T_pF_e=T_pF_o=0,\qquad
U_pF_\bullet=V_p\sigma_{p^2}F_\bullet,\qquad
U_p^2F_\bullet=\sigma_{p^2}F_\bullet
\quad(\bullet=e,o).}
\tag{26}
$$
这里 $T_p$ 对常数系数线性，最后两式另用了 (23)。

(26) 是作用于权一模形式**截面**及其 cusp $q$-展开的关系。
除去 $\omega_1$ 后，不能继续把同一个 $U_p$ 无修正地作用于
标量函数 $M_e,M_o$；同源运输也作用于该周期框架。
同样，$u=L/K$ 的 Cayley/GM 系数不是 cusp $q$ 系数。
因此 (26) 没有给出 $u^n\mapsto u^{n/p}$ 的算子公式。
二次 Frobenius 保持两条组合，各自的 Hecke 关系并不把
已知的奇部首项等同于实际偶部的中央除 $p$ 行。

## 5. 对第二 Witt 层有何实际输入

(20) 是完整函数恒等式，所以可对其作任意次数的真实模参数
微分，并保留原常数和 $17$ 角色；它可以与相应各同源上的
固定除法单位 norm 恒等式配对。
这是一个新的明确约束，而非只知道某个有限空间的名称。

但 (18) 中 $U_p^2$ 是 cusp $q$-展开上的 Hecke 算子，
不能直接替换为 Legendre 家族的单个 crystalline
$\phi^2$ 分支。原 CM 点 $\tau=i$ 的 $p$ 邻居在惰性处属于
导子增加 $p$ 的 CM 曲线；即使它们在特殊纤维合并，
其整变形、微分缩放和 Kummer norm 常数仍不同。
只取其中一个分支会删掉 (20) 的真实 trace 信息。

尤其，$T_pF=0$ 不是实际中央系数 $C_{p+1}/p$ 的消失断言。
例如 $p=7$ 时实际 $\beta_8=[z^8]A_1=97/60$，并且
$$
\frac{C_8}{7}
=\frac{9409}{15\cdot17^4}\equiv2\pmod7,
$$
与 (18) 完全相容。
下一步需要的是把全部同源分支的 (20) 与
[实际 Kummer 第二层](2026-11-12-kummer-frobenius-vertical-jets-and-gm-pairing.md)
及 [完整 GM 导数行](2026-11-12-exact-gm-wronskian-and-kummer-derivative-row.md)
作带整格和常数的比较；目前没有证明它迫使中央行非零。

## 6. 精确证书与一手输入

[check-weight-one-hecke-decomposition.py](../scripts/check-weight-one-hecke-decomposition.py)
仅用 Python 整数和有理数，完成以下有限核验：

1. 原 $256$ 点轨道、负轨道不交及 (4)；
2. (13) 在全部 $68^2$ 个剩余类对上的完整等式；
3. 上表恰有 $57$ 个非零分量；
4. 唯一常数分量 $A_{68,17,1}=-16$ 和原常数 $4$；
5. 在 $p=3,7,11,19$ 的有限 $q$ 系数中独立核对 (19)。

精确环是
$\mathbb Z[X]/\Phi_{272}(X)$，其中
$\zeta_{68}=X^4,\zeta_{16}=X^{17}$，且
$\Phi_{272}=X^{128}-X^{120}+\cdots-X^8+1$。
因此非零分量的判定不是复数近似或单个有限域试算。
在课题目录运行：

    python scripts/check-weight-one-hecke-decomposition.py

文献输入与本篇使用范围：

- Samit Dasgupta、Mahesh Kakde，*On Constant terms of Eisenstein Series*，
  Acta Arith. **200** (2021), 119–147，
  [作者预印本 arXiv:2010.00650](https://arxiv.org/pdf/2010.00650)，
  §4 开头，预印本印刷第 15 页：允许非本原角色和权一的实际
  Eisenstein 构造、divisor-sum 系数与权一角色交换。
  本篇不把其需要角色互素的后续 cusp 常数定理用于重叠模数。
- Lev Borisov、Paul Gunnells，*Toric varieties and modular forms*，
  Invent. Math. **144** (2001), 297–325，
  [作者全文](https://sites.math.rutgers.edu/~borisov/pubs/pdf/toric.pdf)，
  §5.1、式 (19)–(20)，预印本 pp. 20–21：
  $U_p,V_p,\langle p\rangle,T_p$ 的准确规范；
  §5.8–5.9 的 theta 对数导数计算也可核对 (7) 的 Fourier 形式。
- 原实际标签、completed zeta 与层 $68$ 模变换律：
  [R47 的完整证明](2026-11-12-central-borel-modular-uniformization.md)。
- (4)–(15)、(17)–(20) 的实际有限 Fourier 计算和角色限制
  都在本文给出，不把一个待证的跨 $p$ 非零性作为输入。
