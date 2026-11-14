# 非 CM 互反函数在固定负七 CM 源点的简单零点

日期：2026-11-12。**已证明。** 本篇给源点上一条实际、跨素数的
一阶非零结论；不把总 Hecke 迹的简单零点当成指定 $C_p$ 纤维的
二阶矩非零。

## 1. 固定对象和结论

使用 R136 的
$$
 E:y^2+y=x^3+x^2-2x,\qquad F=\mathbb Q(\sqrt{-7}),
 \qquad \pi:X_0(389)\longrightarrow E,\quad\pi(\infty)=O.
\tag{1}
$$
令 $f=\sum a_nq^n$ 为正规化 newform。固定最大阶的两个
$389$-Heegner 点 $c_+,c_-\in X_0(389)(F)$。
R136 已证明
$$
 \pi(c_\pm)=O,\qquad d\pi(c_\pm)\ne0.
\tag{2}
$$
第二式先在明确的复 CM 参数上用严格 Acb 区间证明，另一点
由复共轭得到；它是代数微分的非零性。因此固定代数微分规范下
$f(c_\pm)$ 的值在固定有限个素位之外都是单位。

只在本篇取 $p$ 于 $F$ 分裂，删去固定有限集：模型、层结构、
微分和 Manin 因子的坏位，以及 $p\le5$、$p=7,389$。
原曲线在 $p$ 普通时当然适用下面的结论；所用特征 $p$ 函数的
导数计算本身不需 $a_p(E)\ne0$。

记 Hasse invariant 为 $H$，Katz holomorphic theta 算子为
$\Theta$。权零的原去 $p$ 原函数约化为
$$
 g_p=\frac{\Theta^{p-2}\bar f}{H^p}
      \in\mathbb F_p(X_0(389)),\qquad
 (g_p)_\infty=\sum_{p\nmid n}\frac{\bar a_n}{n}q^n.
\tag{3}
$$
必要时在固定细模覆盖上定义它，再由 $\Gamma_0(389)$ 对称性
下降。源的两个点在这些 $p$ 处普通，所以 (3) 在其约化附近正则。

**结论。** 有固定常数 $C$，使 $p\le X$、$p$ 在 $F$ 分裂且
$g_p$ 在任一个 $\bar c_\pm$ 不是简单零点的素数至多
$$
                         C X^{3/4}.
\tag{4}
$$
其中固定有限例外已吸收到常数中。尤其在分裂素数中，实际源
简单零点成立于相对密度一的集合。下面给准确导数、原点零性
及 (4) 的整数格证明。

## 2. 原点零性与真实互反函数

原曲线 $E$ 非 CM，所以在任何普通好位都不是 canonical lift：
若是，其剩余 Frobenius 提升为特征零非整数自同态，反与
$\operatorname{End}_{\overline{\mathbb Q}}E=\mathbb Z$ 矛盾。
Buium–Poonen（2009）Theorem 3.17(2) 因而给原模参数化的
互反函数约化恰为 (3)，只差已排除的固定 Manin 单位。
其 Theorem 3.5 把 $\pi(c)=O$ 送到互反函数的零点。源的最大阶
CM 提升在 split $p$ 处正是 canonical lift，所以
$$
                            g_p(\bar c_\pm)=0.
\tag{5}
$$
这可在 $X_1(389)$ 的任意兼容提升上应用，再下降到 $X_0(389)$。
源的 $j$ 在固定有限集外不为 $0,1728$，处于该定理的 standard open。

也可直接用 R134 的原 Coleman 比较验证 (5)，这同时覆盖目标
超奇异而源普通的好位：若 $G=\log_E\pi$ 以尖点常数为零，则
$$
 G^{[p]}=\left(1-\frac{a_p(E)}p V+\frac1pV^2\right)G.
\tag{6}
$$
源 connected CM $p$-商的 Artin 元由 $\mathfrak p\mid p$ 给出。
由于 $h_F=1$，它保持实际 $389$ 理想方向并把 $c_\pm$ 送到自己。
三个实际点的 $\pi$ 像均为 $O$，故 (6) 在该点为零。
原去 $p$ 原函数的 ordinary 约化是 (3)。这里先对真实函数应用
(6)，不在 $p$-整环中把一个未经整化的原函数任意除以 $p$。

## 3. Igusa 微分的准确比例及导数

固定一个 $c=c_\pm$ 及其上方的 $p$ 位。设 $(C_c,C_c[\mathfrak n])$
为对应的最大阶 $F$-CM 椭圆曲线和 $389$ 子群。
选在当前位整的固定代数不变微分 $\omega_0$。
因为 $p$ 在 $F$ 分裂，$c$、$C_c$ 和 $\omega_0$ 的约化可在
$\mathbb F_p$ 上取值。写
$$
 A_{c,p}=H(C_c,\omega_0)\in\mathbb F_p^\times,
 \qquad f_0=\bar f(C_c,C_c[\mathfrak n],\omega_0)
                  \in\mathbb F_p^\times.
\tag{7}
$$
$f_0\ne0$ 使用 (2) 的固定有限坏集，而不是关于变化权的猜想。

在 Igusa 覆盖上取 $\omega_{\rm ST}$，使 $H(\omega_{\rm ST})=1$。
定义比例为
$$
 \omega_{\rm ST}=\Omega\omega_0.
$$
Hasse 的权为 $p-1$，所以准确有
$$
                   \Omega^{p-1}=A_{c,p}.
\tag{8}
$$
这里 $\Omega$ 是**微分之比**。若改用形式群同构
$\beta:\widehat{\mathbb G}_m\to\widehat C_c$ 的导数规范
$\beta^*\omega_0=\Omega_\beta dT/(1+T)$，则
$\Omega=\Omega_\beta^{-1}$；不能交换这两个周期的方向。

权二形式的值为 $h=\Omega^{-2}f_0$。由于 $f_0^p=f_0$，由 (8)
得到无需选择 Frobenius 记号的恒等式
$$
                           h^p=A_{c,p}^{-2}h.
\tag{9}
$$

以 $\mathcal D$ 记 Igusa/ST 的 Kodaira–Spencer 导数，在 Tate
参数处为 $q\,d/dq$，在 ST 参数处为 $(1+T)d/dT$。
Hecke 递推 $a_{pn}=a_p a_n-p a_{n/p}$ 给
$$
                     \mathcal D g_p=\bar f-a_p(E)\bar f^{,p}
                    \quad\text{于 }H=1\text{ 的 Igusa 框架}.
\tag{10}
$$
为保持权的完整性，(10) 也可先在底曲线上写为同权的等式
$$
 \Theta^{p-1}\bar f
      =H^{p+1}\bar f-a_p(E)H^{p-1}\bar f^{,p}.
\tag{11}
$$
两边权都是 $p^2+1$，q 展开由上述 Hecke 递推相等；q 展开原则
给 (11)，再在 Igusa 框架 $H=1$ 中得到 (10)。

所以实际源导数是
$$
 \boxed{\quad
 (\mathcal D g_p)(\bar c)
      =h\left(1-\frac{a_p(E)}{A_{c,p}^{,2}}\right).
 \quad}
\tag{12}
$$
Igusa 覆盖在 ordinary locus 上 étale，且 ST 导数在中心是局部
参数的单位倍。结合 (5)，$g_p$ 在 $\bar c$ 非简单零的准确条件为
$$
                       a_p(E)\equiv A_{c,p}^{,2}\pmod p.
\tag{13}
$$
特别地目标 $a_p(E)=0$ 不造成这项导数退化。

## 4. 退化素数的无条件整数格上界

源的普通 Frobenius 是最大阶 $\mathcal O_F$ 中范数为 $p$ 的元素。
记其迹为 $u$，则有整数 $u,v$ 满足
$$
            \pi_c=(u+v\sqrt{-7})/2,\qquad
            u^2+7v^2=4p,
            \qquad A_{c,p}\equiv u\pmod p.
\tag{14}
$$
换一个 $F$-有理模型至多改变相应迹的符号；平方条件不变。
两个 CM 理想方向也由同一式控制。

若 (13) 成立，则
$$
                  u^2-a_p(E)=kp,
                    \qquad k\in\{0,1,2,3,4\}
\tag{15}
$$
对 $p>4$ 成立：$0\le u^2\le4p$，而 Hasse 界为
$|a_p(E)|\le2\sqrt p<p$。若 $p\le X$，消去 $p$ 给
$$
               |(4-k)u^2-7kv^2|\le8\sqrt X,
               \qquad |u|\le2\sqrt X,\quad |v|\le2\sqrt{X/7}.
\tag{16}
$$
只数全部整数格点就足够，不需要在这些格点中再筛出素数。

当 $k=0$，$u^2=a_p(E)$ 给 $|u|\ll X^{1/4}$，而
$|v|\ll X^{1/2}$，故至多 $O(X^{3/4})$ 对。
当 $k=4$，$-7v^2=a_p(E)$，交换两变量得到同样上界。

对 $k=1,2,3$，固定 $\alpha_k=\sqrt{7k/(4-k)}$。
先取 $u,v\ge0$，其余符号只增常数。$v\le X^{1/4}$ 时
(16) 迫 $u\ll X^{1/4}$，共 $O(X^{1/2})$ 对。
当 $X^{1/4}<v\ll X^{1/2}$ 时，
$$
 |u-\alpha_kv|
    \le\frac{C\sqrt X}{u+\alpha_kv}
    \le\frac{C'\sqrt X}{v}.
$$
固定 $v$ 的整数 $u$ 至多 $O(1+\sqrt X/v)$ 个，求和给
$O(\sqrt X\log X)$。故全部五种 $k$ 共
$$
                         O(X^{3/4}+\sqrt X\log X)=O(X^{3/4})
\tag{17}
$$
个格点。每个退化 $p$ 都产生至少一个格点，且每个格点由 (14)
决定唯一的 $p$，这证明 (4)。

这个上界不使用非 CM 曲线固定 Frobenius 迹的幂次估计，
也不把 $a_p(E)=\pm1$ 的 Lang–Trotter 问题偷换为已知幂次界。
它使用的是固定源 CM 范数式和目标的 Hasse 界。

## 5. 对真实 Hecke 总迹的作用及剩余问题

取 $\ell\ne p,389$。在记录全部 $\ell+1$ 个循环同源方向的
细覆盖上，对 (3) 作实际几何 Hecke 总迹。由权零 q 展开
$$
 \ell U_\ell g_p+V_\ell g_p=a_\ell(E)g_p.
\tag{18}
$$
确切系数是 $a_\ell(E)$：当 $p\nmid n$ 时，左边在 $q^n$ 的系数为
$(a_{\ell n}+\ell a_{n/\ell})/n$；当 $p\mid n$ 时两边系数均为零。
因此在 R138 的
$a_\ell(E)\not\equiv0\pmod p$ 输入上，对 (4) 以外的 split $p$，
这个真实总迹在 $\bar c$ 也有简单零点。

此处尚不能推出 R139 的原 $U$ 迹在 $C_p$ 纤维上的 $D_2$ 行非零。
即使在连通 étale $C_p$ 覆盖上，简单零的总迹也不足以推出这点。
例如在 $y^p-y=t+b$ 上，取 $e=-y^{p-1}$，则
$\operatorname{Tr}(e)=1$；函数 $B=te$ 满足
$\operatorname{Tr}(B)=t$，但在 $t=0$ 的整个纤维上 $B=0$，
故所有二阶矩为零。取 $b$ 的绝对迹非零可使该纤维本身是
非平凡的次数 $p$ 扩域。

所以 (12)、(17)、(18) 是已付的固定源一阶条件。下一条需要
的是原模形式/原同源轨道特有的额外关系，将它与指定纤维的
一阶、二阶 deck 矩联立；本篇没有用一般 étale 性替代这条关系。

## 来源

- R136 的明确 $c_\pm$、$\pi(c_\pm)=O$ 及非分歧 Acb 证书。
- N. Katz，*A result on modular forms in characteristic p*，
  LNM **601** (1977), 53–61，§II 的 theta 与 q 展开原则；
  [作者全文](https://web.math.princeton.edu/~nmk/old/modformcharp.pdf)。
  Hasse 规范及 ST 框架亦见 Katz，*Serre–Tate local moduli*，
  LNM **868** (1981)，Theorems 4.3.1–4.3.2。
- A. Buium、B. Poonen，*Independence of points on elliptic curves
  arising from special points on modular and Shimura curves, II:
  local results*，Compositio Math. **145** (2009), 566–602，
  [作者全文](https://math.mit.edu/~poonen/papers/local.pdf)，
  Theorems 3.5、3.17(2) 和 §4.3 的 (4.8)。
- R134 的原去 $p$ Coleman 恒等式和权零函数识别，及其引用的
  Bertolini–Darmon–Prasanna（2013）§3.8，Lemma 3.23、Proposition 3.24。
- (12) 的微分比例和 (17) 的全部格点预算在本篇直接证明；
  未以数值素数扫描代替跨素数上界。
