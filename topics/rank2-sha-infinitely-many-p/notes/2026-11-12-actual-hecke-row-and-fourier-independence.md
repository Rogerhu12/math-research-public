# 实际 Hecke 各支的 Fourier 独立性及二阶加权行

日期：2026-11-12。**已证明的函数域结论。**
本篇证明原二阶权重在真实全 level 覆盖上给非零函数，
并保留简单超奇异极点。固定 $F$-CM 纤维上的取值非零尚未证明。
实际环类标签、两条 nonsplit Cartan 轨道与 $C_p$ 覆盖的完整对接见
[环面覆盖与原 CM 迹](2026-11-12-torus-cover-and-actual-cm-trace-row.md)；
本篇不以单条 Cartan 轨道替代原完整迹。

## 1. 原函数及共同连通覆盖

沿用 R135，取 $p\ge13$ 在 $\mathbb Q(i)$ 分裂，删去其中固定
有限坏集。令
$$
 E:y^2=x^3-17x,\quad N=9248,\quad M=3N,\qquad
 h_p=\bar H_p/\mathrm{Ha}_p\in
              \overline{\mathbb F}_p(X_0(N)).
 \tag{1}
$$
函数域命题只需这个目标 ordinary 条件；与原 CM 纤维取值
比较时另保持 $p$ 在 $F=\mathbb Q(\sqrt{-15})$ 分裂，
确保源点 ordinary，因而下面的函数在该纤维有定义。
为保留原类数 $2$ 的完整映射
$\Phi=\pi d_1+\pi d_3$，在 $C=X_0(M)$ 上使用
$$
        \mathcal H=h_p\circ d_1+h_p\circ d_3,\qquad
        \mathcal H(q)=h_p(q)+h_p(q^3)=\sum_{n\ge1}b_nq^n.
 \tag{2}
$$
特别 $b_1=1$。$\mathcal H$ 在所有尖点为零，仅可能在
超奇异点有简单极点。只使用 $\pi$ 的版本可将 $\mathcal H$
换成 $h_p$；下面证明相同。

令 $\ell\nmid Mp$ 为素数。取 $k=\overline{\mathbb F}_p$，
选择相容的 Weil 配对值，并令
$$
                  X=X(M)_k,\qquad Y_{\rm full}=X(M\ell)_k
 \tag{3}
$$
表示所选配对值的连通 full-level 分量。它们是光滑射影
几何连通曲线。这里使用 full-level 模型的好约化定理，
不是仅从 $E[\ell]$ 是 étale 推断整个覆盖连通：
Cais–Conrad Theorems 2.2–2.3 准确给该模型在
$p\nmid M\ell$ 时的光滑性、几何连通性和尖点参数。

在非尖点处，忘掉 $\ell$-level 是有限 étale 的
$\mathrm{SL}_2(\mathbb F_\ell)$-torsor，次数
$$
                 [Y_{\rm full}:X]=\ell(\ell^2-1).
 \tag{4}
$$
即使 $p\mid\ell+1$，$\ell$ 仍在基域可逆，(4) 仍成立；
不把有限 étale 覆盖的次数错误限制为素于特征。
固定 $M$-level 已经消除曲线对象的非平凡自同构，所以
这里首先是 $\mathrm{SL}_2$，不能直接写成 $\mathrm{PSL}_2$。

对每条线 $v\in\mathbb P^1(\mathbb F_\ell)$，由对应的
$\ell$ 阶循环子群作商，并运输原循环 $M$-level，得真正同源映射
$$
       r_v:Y_{\rm full}\longrightarrow C,\qquad
                      h_v=r_v^*\mathcal H.
 \tag{5}
$$
全部 $h_v$ 对 $\ell$-level 中心 $\{\pm I\}$ 不变，故下降到
连通中心商
$$
                Y=Y_{\rm full}/\{\pm I\}.
 \tag{6}
$$
它在非尖点处的 deck 群为 $\mathrm{PSL}_2(\mathbb F_\ell)$。
后文 Cartan 群均在 (6) 上取；证明常系数关系可以在
$Y_{\rm full}$ 上完成，因为函数域拉回单射。

## 2. 同一尖点的全部同源支与 Hecke 总迹

在 (3) 的标准 Tate 尖点，固定一个原始 $\ell$ 次根
$\zeta_\ell\in k$。标记诸线使
$$
 h_\infty(q)=\mathcal H(q^\ell),\qquad
 h_a(q)=\mathcal H(\zeta_\ell^a q^{1/\ell}),
                       \quad a\in\mathbb F_\ell.
 \tag{7}
$$
这些都是同一个完成域中的展开。若其参数取
$Q=q^{1/(M\ell)}$，则 (7) 的幂分别为
$Q^{M\ell^2n}$ 与 $Q^{Mn}$；并未混用不同曲线的形式参数。
公式也直接由 Tate 曲线的子群 $\mu_\ell$ 与
$\langle\zeta_\ell^a q^{1/\ell}\rangle$ 得到。

记几何 Hecke 算子为所有 $\ell+1$ 个循环商的无权和。
在 q 展开上它是 $\ell U_\ell+V_\ell$。R135 的
$H_p=\theta(\psi_E^{p-2})$ 满足经典权 $p-1$ Hecke 关系。
对素于 $pN$ 的 $\ell$，其特征值模 $p$ 为
$a_\ell(E)/\ell$，且 $\ell^{p-2}=\ell^{-1}$。
因此 q 展开原则给
$$
       \sum_{v\in\mathbb P^1(\mathbb F_\ell)}h_v
                         =\bar a_\ell(E)\,\mathcal H\circ r_{\rm src},
 \tag{8}
$$
其中 $r_{\rm src}$ 忘掉 $\ell$-level，不作商。
因 $\ell\ne3$，$V_3$ 与这里的 Hecke 算子交换，
所以 (8) 对真实旧形式 (2) 也成立。

以后取本题实际 $\ell\equiv-1\pmod{1020p}$，并保
$v_p(\ell+1)=1$。此时 $\ell$ 在 $\mathbb Q(i)$ 惰性，
故 $a_\ell(E)=0$，(8) 准确成为
$$
                         \sum_vh_v=0.
 \tag{9}
$$
在后面的 Fourier 论证中只除以 $\ell$，**不除以**
$\ell+1=pu$。

## 3. 每个非零 residue class 都有一个非零 prime 系数

固定 $r\in\mathbb F_\ell^\times$，置
$L_p=\mathbb Q(E[p])$。由于 $E$ 在 $\ell$ 有好约化且
$\ell\ne p$，其好模型上的 $E[p]$ 是有限 étale 群概形；
因而 $L_p/\mathbb Q$ 在 $\ell$ 不分歧。

另一方面，$\mathbb Q(\zeta_\ell)$ 在 $\ell$ 全分歧。
可直接用 Eisenstein 多项式
$((1+X)^\ell-1)/X$ 核定局部次数 $\ell-1$；其每个
非平凡子域在 $\ell$ 仍分歧。因此
$$
                  L_p\cap\mathbb Q(\zeta_\ell)=\mathbb Q.
 \tag{10}
$$
两个域均 Galois，故其合成域的 Galois 群是直積。
Chebotarev 应用于元素 $(1,r)$，给一个（事实上无穷多个）
素数 $q\nmid 3Np\ell$，满足
$$
       \operatorname{Frob}_q|E[p]=1,\qquad q\equiv r\pmod\ell.
 \tag{11}
$$
在 $E[p]$ 上取 trace 和 determinant 得
$$
               a_q(E)\equiv2\pmod p,\qquad q\equiv1\pmod p.
 \tag{12}
$$
R135 的逐理想系数式及 $q\ne3$ 遂给
$$
                         b_q=a_q/q\equiv2\ne0\pmod p.
 \tag{13}
$$
这里完全不需要 $\bar\rho_{E,p}$ 满像或残余像为
$\mathrm{GL}_2$，也没有使用有效 Chebotarev 或关于 $q$ 大小的估计。

## 4. 唯一的常系数关系

**命题。** 在 $k(Y_{\rm full})$ 或 $k(Y)$ 中，诸函数
$\{h_v\}_{v\in\mathbb P^1(\mathbb F_\ell)}$ 的全部
$k$-常系数关系恰为
$$
       \ker\!\left(k^{\mathbb P^1(\mathbb F_\ell)}
                   \longrightarrow k(Y),\
                    (c_v)\longmapsto\sum_vc_vh_v\right)
                    =k\cdot(1,\ldots,1).
 \tag{14}
$$
特别，它们张成的空间维数准确为 $\ell$。

**证明。** 设 $c_\infty h_\infty+\sum_ac_ah_a=0$。
对任意 $r\ne0$，取 §3 的素数 $q\equiv r\pmod\ell$。
比较 (7) 中 $q^{q/\ell}$，即 $Q^{Mq}$ 的系数。
因为该 $q$ 是不等于 $\ell$ 的素数，$\infty$ 支对此幂没有贡献。
由 (13)，
$$
                       \sum_{a\in\mathbb F_\ell}
                                     c_a\zeta_\ell^{ar}=0
                       \quad(r\ne0).
 \tag{15}
$$
长度 $\ell$ 的 Fourier 变换可逆，因为 $\ell\ne p$。
(15) 迫使所有有限支系数 $c_a$ 同为一个 $c\in k$。
再用 (9)，原关系等于 $(c_\infty-c)h_\infty=0$。
$h_\infty$ 的首项是 $q^\ell$，所以 $c_\infty=c$。
反向包含正是 (9)。证毕。

更一般地，若 (8) 中 $\bar a_\ell\ne0$，同样比较先迫
所有有限支系数为 $c$。剩余关系为
$(c_\infty-c)\mathcal H(q^\ell)+c\bar a_\ell\mathcal H(q)=0$；
比较 q 一次项先得 $c=0$，再得 $c_\infty=0$。
此时全部 $\ell+1$ 支线性独立，**但总迹不为零**，
不能套用以下以 (9) 为前提的增广等式。
本篇实际应用始终是 $E_{17}$ 的 (9)。

## 5. 原两轨道权重确为非恒定

写 $\ell+1=pu$，$u$ 为偶数且素于 $p$。
在 $\mathrm{PGL}_2(\mathbb F_\ell)$ 的 nonsplit torus
$T$ 中，$|T|=\ell+1$，它在 $\mathbb P^1(\mathbb F_\ell)$
上单传递。其
$$
 T_0=T\cap\mathrm{PSL}_2(\mathbb F_\ell),\quad |T_0|=pu/2
$$
有两条轨道，不能遗漏其中之一。设 $U\le T$ 阶为 $u$，
$U_0=U\cap T_0$ 阶为 $u/2$。取
$\rho\in U\setminus U_0$、$v_-=\rho v_+$，并取
$\tau\in T_0$ 映为 $T_0/U_0\simeq C_p$ 的生成元。
采用使 $\tau h_v=h_{\tau v}$ 的函数作用约定，定义
$$
 B=\sum_{a\in U_0}(h_{av_+}+h_{av_-}),\qquad
 D_j=\sum_{r=0}^{p-1}\binom rj\tau^r\quad(j=1,2).
 \tag{16}
$$
几何桥证明：在带原 CM 标签的纤维，$B$ 正是对 (2)
取原阶 $u$ 子群的迹，亦即对 $\pi$ 取原 $2u$ 项完整迹；
不是任意同次数的替代和。

$D_jB$ 在每条线 $\tau^ra v_\pm$ 上的系数是
$\binom rj$。对 $j=1$，$r=0,1$ 的系数分别为 $0,1$；
对 $j=2$，$r=0,2$ 的系数分别为 $0,1$。
由 (14) 严格得到
$$
                             D_1B\ne0,\qquad D_2B\ne0.
 \tag{17}
$$
这是原始 Hecke 行的**函数非零**，不再只是任意抽象
有限维空间中存在非零向量。

总迹 (9) 给 $N_\Gamma B=0$。令 $\Delta=\tau-1$，
在特征 $p$ 的群环中直接重排二项式系数得
$$
 \Delta D_1B=0,\qquad
 \Delta D_2B=-D_1B,\qquad
 \Delta^2D_2B=0.
 \tag{18}
$$
由 (17)，$D_2B$ 的实际 Jordan 长度准确为 $2$。
在连通 $C_p$ 函数域扩张的 normal-basis 模中，
$N_\Gamma B=0$ 给 $B\in\Delta k(Y/U_0)$，而
$D_1=-\tau\Delta^{p-2}$ 与 (17) 给
$$
               B\notin\Delta^2 k(Y/U_0).
 \tag{19}
$$
这些是 deck 算子的陈述；绝对 Frobenius 只有在原标记
CM 纤维取值时才按其 Artin 元识别，二者未在整个模曲线上等同。

## 6. 共同简单极点与下降后的次数

设 $\mathrm{SS}_Z$ 为有关细模曲线 $Z$ 的 reduced
超奇异除子。一个素于 $p$ 的同源给 Hodge 线之间的同构；
Hasse 拉回只差一个单位。因此 (5) 的全部分母都在
$Y_{\rm full}$ 上有同一个零除子
$\mathrm{SS}_{Y_{\rm full}}$，且是简单零。
分子 holomorphic；故
$$
             (h_v)_\infty\le\mathrm{SS}_{Y_{\rm full}}
                  \quad\text{对全部 }v.
 \tag{20}
$$
线性和也满足 (20)。极点预算不用再乘 $\ell+1$。
这同样可从 prime-to-$p$ 同源对应在内点的 étale 性验证。

置固定常数
$$
                    d_M=\deg\omega_{X(M)}
                          =\frac{2g_{X(M)}-2+\nu_{X(M)}}2.
$$
Hasse 的权为 $p-1$，结合 (4)，得
$$
 \deg\mathrm{SS}_{Y_{\rm full}}
        =(p-1)d_M\,\ell(\ell^2-1).
 \tag{21}
$$
中心商和 Cartan 商的这些映射在非尖点处 étale，所以
极点阶不增加，极点除子次数按覆盖次数相除。
于是 $D_2B$ 在 $Y/U_0$ 上、$D_1B$ 在 $Y/T_0$ 上分别满足
$$
 \begin{aligned}
 \deg(D_2B)&\le (p-1)d_M\,
      \frac{|\mathrm{PSL}_2(\mathbb F_\ell)|}{u/2}
        =(p-1)d_M\,p\ell(\ell-1),\\
 \deg(D_1B)&\le (p-1)d_M\,
      \frac{|\mathrm{PSL}_2(\mathbb F_\ell)|}{pu/2}
        =(p-1)d_M\,\ell(\ell-1).
 \end{aligned}
 \tag{22}
$$
后者使用 (18) 的真实 $T_0$-不变性。这里说的是函数的
总 degree，未将单点 simple pole 误当总 degree 为常数。

诸 $h_v$ 在共同标准尖点的常数项都是零。因此 (17) 的
两个函数非恒定；若无极点，它们在射影曲线上为常数零，
矛盾。结合 (20)，各至少有一个真实简单超奇异极点。
所以在各自函数域中均有
$$
                 D_jB\notin\operatorname{AS}(k(\,\cdot\,)),
                    \qquad \operatorname{AS}(x)=x^p-x,
                    \quad j=1,2.
 \tag{23}
$$
证明仍是简单极点不可能是 $p$ 倍阶。此 AS 是绝对
$p$ 次幂；(19) 的 $\Delta$ 是有限 deck 差分，二者不同。

## 7. 尚需证明的准确取值

对原 $F$-CM 点和原环类商，R135 将 $D_2B$ 的取值
准确识别为实际半局部测试的单位倍数。函数非零说明该
测试没有因为整条模曲线上的 Hecke 恒等式而恒等消失，
却没有证明所选 CM 点避开它的零除子。
一个非零有理函数可以在指定的有限 CM 纤维为零；
这里 $\ell$ 和覆盖都随 $p$ 变化，(22) 也没有给这样的
纤维避零定理。

特别，(19) 的函数域增广原始性不能通过简单取值推出
原环类点的整数增广原始性。证明主目标仍需要在无穷个
真实输入中证明 $D_2B(x_\ell)\ne0$，或从该纤维的全部
额外结构推出一个足以排除共同零的结论。

## 一手来源

- B. Cais, B. Conrad, *Modular curves and Ramanujan's continued
  fraction*，2006 年作者版，Theorems 2.2–2.3，印页 4，
  [作者全文](https://virtualmath1.stanford.edu/~conrad/papers/J5final.pdf)。
  这两条定理准确陈述固定 Weil 配对 full-level 模型的几何
  连通性、好约化及 Tate 尖点参数，所引基础是
  Katz–Mazur (1985) §§10.9.1、10.9.6–7 与 Deligne–Rapoport。
- J. S. Milne, *Algebraic Number Theory*，2020 年 v3.08，
  Theorem 8.31，印页 147，
  [作者全文](https://www.jmilne.org/math/CourseNotes/ANT.pdf)。
  这里只用固定有限 Galois 扩张的 Chebotarev 存在性；
  两域互不交与全部 trace/determinant 条件在 §3 直接证明。
- R135 的完整 CM 伴随形式、简单 Hasse 极点及 q 展开；
  R134 的原 Heegner 迹与二阶测试。本文的 Fourier 核、
  非恒定权重和 (18)–(23) 均附直接证明，没有调用一个
  未匹配的 Ihara 饱和或新型 Heegner 非零定理。
