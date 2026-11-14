# R196. 完整连续第一带的 Euler–Padé 核与真实当行首项

日期：2026-11-12。**状态：以下归一第一带模 $p$ 核的等价描述、
当行首项及权理想端点的准确秩均已证明。** 结论针对同一个原
多项式的全部连续前缀。模 $p$ 归一核与可提升到特征零的准确前缀核
保持区分；本文不声称每个前者的向量均有后一种提升。

## 1. 原源、真实输出与归一前缀

取 $p=4r-1\ge7$，排除 $p=11$，令 $R=r(p-1)$。沿用
$$
 A=w+O(w^2),\quad C=B-A=v_0w^2+O(w^3),\quad v_0=-22,
 \qquad E_D=\mathbb Z_p[A,C]_{\le D}.
 \tag{1}
$$
真实 Cartan 坐标、径向轴与整 flowbox 是
$$
 U(w)=u_0w^r+O(w^{r+R}),\quad V(w)=w+O(w^{R+1}),\quad
 \tau=pu_0\bmod p\ne0,
 \tag{2}
$$
$$
 A=\Gamma^{17}f(y),\quad C=\Gamma^{17}c(y),\qquad
 f(y)=y+O(y^2),\quad c(y)=v_0y^2+O(y^3),\quad y=\zeta.
 \tag{3}
$$
所有环境级数均整。以下原次数 $D$ 任意，不附加 $D<p$。

固定
$$
 k=rq+s,\qquad 0\le s<r,\qquad 0\le q\le p-2.
 \tag{4}
$$
对 $n=rh+l<k$，$0\le l<r$，定义真正归一原行
$$
          \mathcal J_n(P)=p^h[w^n]P(A(w),C(w)).
 \tag{5}
$$
这些行是 $E_D$ 上的整线性行。因为 $k\le r(p-2)+r-1<R+1$，
本篇全部行都位于原 $w$ 单系数的准确第一带，不需要把单个高系数
偷换成 $V(w)$ 的系数。

若 $\widetilde P=\sum L_{i,j}(P)U^iV^j$，准确有
$$
 \mathcal J_{rh+l}(P)
 =\sum_{i=0}^h p^{h-i}(pu_0)^iL_{i,l+r(h-i)}(P)
 \equiv\tau^hL_{h,l}(P)\pmod p.
 \tag{6}
$$
所以全部早期行是在同一个完整多项式上取值；(6) 没有分别
假定其各项消失。

## 2. 连续 h 块与原 Euler 算子

设 $\mathcal E=A\partial_A+C\partial_C$ 是原平面的 Euler 算子。
按原齐次次数写 $P=\sum_mP_m$，则 $\mathcal E^hP_m=m^hP_m$。
这里的齐次次数是原 $A,C$ 次数，不是底层 theta 次数。

R175/R179 的真实径向式给
$$
 \mathfrak a(U)=e^U+O(U^p),\qquad
 \mathfrak b(U)=1+\frac{U^{p-1}}{(p-1)!}+O(U^p),
 \tag{7}
$$
以及对全部 $l<r$ 的准确轴公式
$$
 \sum_{h\ge0}L_{h,l}(P_m)U^h
       =[y^l]P_m(f(y),c(y))\,
              \mathfrak a(U)^{17m}\mathfrak b(U)^{-l}.
 \tag{8}
$$
在 $h\le p-2$ 时，(7) 因而给
$$
 \boxed{\quad
 \overline{\mathcal J}_{rh+l}(P)
   =\frac{(17\tau)^h}{h!}
          [y^l](\mathcal E^h\overline P)(f(y),c(y)).
 \quad}
 \tag{9}
$$
横线表示模 $p$，右侧亦在 $\mathbb F_p$ 中读取。全部 $h!$ 都是
单位；不需要额外假定 $h+l<p$。

用 $A=f(y)$ 作为严格整参数，定义
$$
 \phi(A)=c(f^{-1}(A))=v_0A^2+O(A^3)\in A^2\mathbb Z_p[[A]].
 \tag{10}
$$
严格换参保持每个完整低阶前缀，并保持其首个剩余系数。因此
$$
 \overline{\mathcal J}_n(P)=0\quad(0\le n<k)
 \tag{11}
$$
准确等价于
$$
 \begin{split}
 &(\mathcal E^h\overline P)(A,\phi(A))\in A^r\mathbb F_p[[A]]
                                      &&(0\le h<q),\\
 &(\mathcal E^q\overline P)(A,\phi(A))\in A^s\mathbb F_p[[A]].
 \end{split}
 \tag{12}
$$
$s=0$ 时最后一条没有限制；$q=0$ 时第一组为空。

## 3. 完整 graph–Hasse 核的精确等价式

置 $Z=C-\phi(A)$，并在 $\mathbb F_p[[A,Z]]$ 中写
$$
 \overline P(A,Z+\phi(A))=\sum_{j=0}^D a_j(A)Z^j,
 \qquad
 a_j(A)=(\partial_C^{[j]}\overline P)(A,\phi(A)).
 \tag{13}
$$
$\partial_C^{[j]}$ 是 Hasse 导数。它从原整数二项式定义，不涉及
除以可能非单位的 $j!$。对 $j>D$ 统一置 $a_j=0$，所以后文在
$q>D$ 时的式子仍按相同约定成立。

在这组坐标中，准确有
$$
 \mathcal E=A\partial_A+(Z+\lambda(A))\partial_Z,
 \qquad
 \lambda(A)=\phi(A)-A\phi'(A)=-v_0A^2+O(A^3).
 \tag{14}
$$
特别 $\lambda/A^2$ 是单位。

**定理 1（完整归一第一带核）。** (11)–(12) 准确等价于
$$
 \boxed{\begin{aligned}
 &a_j(A)\in A^{\max(r-2j,0)}\mathbb F_p[[A]]&& (0\le j<q),\\
 &a_q(A)\in A^{\max(s-2q,0)}\mathbb F_p[[A]].
 \end{aligned}}
 \tag{15}
$$
$j>q$ 的系数没有由这个模 $p$ 前缀新增限制。

**证明。** 给 $(A,Z)$ 以权 $(1,2)$。算子 (14) 保持每个
“权至少 $b$”的幂级数理想：$A\partial_A$、$Z\partial_Z$ 保权，
而 $\lambda\partial_Z$ 至少保权。第 $h$ 次运算后再令 $Z=0$，
$a_jZ^j$ 在 $j>h$ 时不能贡献；$j=h$ 的贡献准确为
$$
                    h!\lambda(A)^h a_h(A).
 \tag{16}
$$
因为恰好 $h$ 次都必须使用降低 $Z$ 次数的部分。

按 $h=0,\ldots,q-1$ 归纳。此前的 $j<h$ 项由 (15) 已具有权至少
$r$，其全部 $\mathcal E^h$ 贡献在 $Z=0$ 后仍被 $A^r$ 整除。
于是第 $h$ 条 (12) 等价于 $\lambda^ha_h\in A^r$。
$h!$ 是单位、$\operatorname{ord}_A\lambda=2$，故得到
$\operatorname{ord}_Aa_h\ge\max(r-2h,0)$。同一论证在最后一步
使用 $s<r$，给出 $a_q$ 的条件。反方向由这些权估计逐项代回
(16) 同时成立。$\square$

这是一份实际源上的核恒等式。可将其写成
$$
 \overline P(A,Z+\phi(A))\in
 \left(
 A^{\max(r-2j,0)}Z^j\ (0\le j<q),\
 A^{\max(s-2q,0)}Z^q,\ Z^{q+1}
 \right).
 \tag{17}
$$
式 (17) 的所有系数仍由同一个原 $P$ 产生；它不是把各齐次块或
每个 $a_j$ 免费作为新的独立源。

## 4. 真实当行的 leading valuation

现在取一个真正满足全部特征零前缀的原整多项式：
$$
                    P\in E_D,\qquad\operatorname{ord}_wP\ge k.
 \tag{18}
$$
其约化满足 (15)。此前 $j<q$ 项对 $\mathcal E^qP$ 的贡献有
$A$ 阶至少 $r>s$；当前项仍由 (16) 给出。

若 $s\ge2q$，由 $a_q\in A^{s-2q}$ 及
$\lambda/A^2\equiv-v_0\pmod A$，得到
$$
 \boxed{\quad
 p^q[w^{rq+s}]P
   \equiv(-17v_0\tau)^q
        [A^{s-2q}](\partial_C^{[q]}\overline P)(A,\phi(A))
             \pmod p.
 \quad}
 \tag{19}
$$
此处 $q!$ 已在 (9) 与 (16) 中准确抵消，$17$ 来自原函数的
theta 次数，负号来自 (14)。严格换参 $y\leftrightarrow A$ 的
首项一保持这一首个剩余系数。

若 $s<2q$，则当行右侧为空，准确有
$$
             p^q[w^{rq+s}]P\equiv0\pmod p,
 \qquad v_p([w^{rq+s}]P)\ge1-q.
 \tag{20}
$$
这包括 R194 的连续前缀一层收益，但 (19) 还给出所有其余角度的
明确剩余行。它并不保证 (19) 的右侧在实际准确前缀核上取到单位。

## 5. 半带端点的权理想与准确模 p 秩

若
$$
                    \lceil r/2\rceil\le q\le p-2,
 \tag{21}
$$
则 (15) 准确合成一个权理想
$$
 \mathcal I_r=(A^iZ^j:i+2j\ge r)\subset\mathbb F_p[[A,Z]].
 \tag{22}
$$
证明是：$j<q$ 时 (15) 正是相应的权限制，$j\ge q$ 时已有
$2j\ge r$；最后的 $s-2q$ 不再为正。

由于 $\phi(A)\in A^2\mathbb F_p[[A]]$，互逆的替换
$C=Z+\phi(A)$、$Z=C-\phi(A)$ 都保持权理想 (22)。因此在原
$E_D/pE_D$ 中，全部归一前缀行的核准确等于
$$
 \boxed{\quad
 \operatorname{span}_{\mathbb F_p}
       \{A^iC^j:i+j\le D,\ i+2j\ge r\}.
 \quad}
 \tag{23}
$$
相应归一矩阵模 $p$ 的秩准确是
$$
 \boxed{\quad
 N_{D,r}=\#\{(i,j)\in\mathbb Z_{\ge0}^2:i+j\le D,\ i+2j<r\}
   =\sum_{j=0}^{\min(D,\lfloor(r-1)/2\rfloor)}
            \bigl(\min(D-j,r-1-2j)+1\bigr).
 \quad}
 \tag{24}
$$
这是整个连续归一矩阵的准确模 $p$ 秩，而非选取稀疏子矩阵得到的
下界。对于真正准确前缀，(23) 只给
$$
 P\in pE_D+\operatorname{span}_{\mathbb Z_p}
                      \{A^iC^j:i+j\le D,\ i+2j\ge r\}.
 \tag{25}
$$
所以 $P/p$ 作为一个整体进入相应第一层分式格；两部分不因此
各自有前缀。对该新格继续求核时，R194 的多余类缺阶矩阵以及更高
$p$ 精度仍须实际支付。

### 5.1 同一完整归一前缀像的第一次 p-saturation

仍在 (21) 的范围，令 $J:E_D\longrightarrow\mathbb Z_p^k$ 是全部
早期归一行 (5) 组成的同一个矩阵，并置
$$
 H_{D,r}=\operatorname{span}_{\mathbb Z_p}
            \{A^iC^j:i+j\le D,\ i+2j\ge r\},\qquad
 M_1=E_D+p^{-1}H_{D,r}.
 \tag{26}
$$
式 (23) 准确给
$$
 \{P\in E_D:J(P)\in p\mathbb Z_p^k\}=pE_D+H_{D,r}.
$$
整体除以 $p$，得到两个准确等式
$$
 \boxed{\quad
 M_1=\{X\in p^{-1}E_D:J(X)\in\mathbb Z_p^k\},\qquad
 J(M_1)=\bigl(p^{-1}J(E_D)\bigr)\cap\mathbb Z_p^k.
 \quad}
 \tag{27}
$$
证明只使用整个像及其模 $p$ 核，不要求 $J$ 单射，也没有把源的
两部分分别置入前缀。

原源格的指数为 $M_D-N_{D,r}$。若 $\rho$ 是 $J$ 的有理秩，
则像格的指数准确为
$$
 \operatorname{length}_{\mathbb Z_p}\bigl(J(M_1)/J(E_D)\bigr)
                         =\rho-N_{D,r}.
 \tag{28}
$$
事实上 $J$ 的非零整 Smith 指数中，恰有 $N_{D,r}$ 个为零；
(27) 将其余正指数各降低一，而保持零指数不变。
源格指数与像格指数的差包含了准确核的格变化，不能将它丢掉。
第二次 saturation 必须重新计算 $J|_{M_1}$ 的模 $p$ 核；
(27) 不把 R194 的缺阶块自动变成单位矩阵。

## 6. 原级数上的有限证书与提升边界

[短脚本](../scripts/check-continuous-first-band-kernel.py) 使用 R162
固定有理级数 $P,Q,W$，先转换到原 $w=z^4$，然后在唯一固定素数
$p=19$、原次数 $D=5$ 的两个窗口核查本定理：

- $q=1,s=4$，$k=9$：对比全部归一原行与 (15) 的完整行空间，
  并在实际饱和前缀核上检验带非平凡右侧的 (19)。
- $q=3,s=0$，$k=15$：对比完整核、检验 (24) 的秩，并核查 (20)。

两个窗口都有非零特征零准确前缀核。脚本直接由原级数消元，不用
(19) 构造原曲线系数或其核向量。

实际输出分别为：$k=9$ 时归一模 $19$ 秩为七、准确前缀核秩为
十二、下一行值理想赋值为 $-1$；$k=15$ 时相应为九、六、$-2$。
后一个窗口的 (20) 一层收益因此准确达到，而非在零核上成立。

最后强调三个不同对象：归一原前缀的模 $p$ 核、准确前缀核的模
$p$ 像、以及当前剩余行在准确核上的值理想。本文准确计算第一个，
把第二个包含于第一个，并给出第三个的首层公式。没有未经证明
把第一种向量全部提升为第二种，也没有把模 $p$ 可取单位自动
当成准确核中的单位。

依赖：

- [R175：准确径向轴式](../notes/2026-11-12-euler-cartan-rows-and-joint-central-prefix-gain.md)。
- [R179：同原源整 flowbox](../notes/2026-11-12-full-depth-common-jet-core-and-as-defect.md)。
- [R188：原 Hasse 导数与整运输](R188-original-source-detection-and-integral-hasse-transport.md)。
- [R191：第一带整块整除](R191-first-band-source-divisibility-and-global-multiplicity.md)。
- [R194：稀疏 Smith 与多块原格](R194-sparse-jet-smith-and-actual-lacunary-hermite-blocks.md)。
