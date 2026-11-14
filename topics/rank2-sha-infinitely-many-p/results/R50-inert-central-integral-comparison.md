# R50. 惰性中央权的整周期比较与初级有限证书

日期：2026-11-12。**状态：已证明；所需的无穷中央单位仍未证明。**

## 1. 定理

固定 $E_{17}:y^2=x^3-17x$，参考曲线 $E_0:y^2=x^3-x$。
两条曲线的导子生成元为
$f_{17}=34(1+i)$、$f_0=2(1+i)$。
令 $d_m^{(j)}$ 为各自导子轨道的完整 Kronecker 中央系数。

对每个 $p\ge7$、$p\equiv3\pmod4$，令 $\mathcal O=\mathbb Z_{p^2}$。
存在实际整幂级数 $\mathcal A_p\in\mathcal O[[T]]$ 及
$x_p\in p\mathcal O$，满足
$$
v_p(x_p)=1,\qquad
v_p\mathcal A_p(x_p)=v_pd_{p+1}^{(17)}+2,
\tag{1}
$$
以及
$$
2\le s_p\le\operatorname{ord}_{T=0}\mathcal A_p,
\qquad
s_p=\operatorname{corank}_{\mathbb Z_p}
 \operatorname{Sel}_{p^\infty}(E_{17}/\mathbb Q)\text{ 为偶数}.
\tag{2}
$$
因此
$$
\boxed{v_pd_{p+1}^{(17)}\le1
 \ \Longrightarrow\ \Sha(E_{17}/\mathbb Q)[p^\infty]\text{ 有限}.}
\tag{3}
$$
特别是 $d_{p+1}$ 为单位足够。此比较还证明所有这些 $p$ 处
$d_{p+1}$ 都整，不需要 R46 系数整模型的未知有限例外集。
它不声称初级部分为零，也不假设高度非退化。

## 2. 两条曲线使用同一个局部整模

因为 $4\mid p+1$，$\mathbb F_p^\times$ 中每个元素都是
$\mathbb F_{p^2}^\times$ 中的四次幂。Hensel 提升给单位 $a$，
$a^4=17$。同构
$$
F_a:E_0\longrightarrow E_{17},\quad(x,y)\longmapsto(a^2x,a^3y),
\qquad F_a^*\omega_{17}=a^{-1}\omega_0
\tag{4}
$$
是实际光滑整模型、形式群和完整 Tate 格的同构。

两条全球 CM 特征之比为四次特征。
对 $p+1\mid m$，它们给同一个反圆分角色
$$
\chi_m=(\varphi_j/\bar\varphi_j)^m.
$$
局部其 tame 指数为 $(1-p)m$，所以首个保持同支的正中央权是
$m=p+1$。选 $\Gamma$ 的生成元后，
$x_m=\kappa_{\rm ac}(\gamma)^m-1$ 满足 $v_p(x_m)=1+v_p(m)$。
不能改用另一 tame 分支的单位或非整系数 $d_{p+2}$。

BKO 的局部 Rubin 定理给完整整分解
$$
M_j=\varprojlim_nH^1(K_{n,p},T_pE_j^{-1}(1))
 =M_j^+\oplus M_j^-,
\qquad M_j^\pm\simeq\mathcal O[[T]].
$$
signed 子模由有限特征下的 dual exponential 消失定义，
故 (4) 及其逆准确保持它们。
根数为正的标准椭圆单位局部像 $\xi_j$ 位于 $M_j^+$。

参考曲线的真实导子点 $S=(i,1-i)$ 满足 $[2]S=(0,0)$。
sigma duplication 给
$$
d_0^{(0)}=(1+i)/2,\qquad L(E_0,1)/\Omega_0=d_0^{(0)}/f_0=1/4.
$$
BKO24 Corollary 4.11(i) 的证明给其 Rubin 函数为
$\Lambda^\times$，故 $\xi_0$ 本身是 $M_0^+$ 的原始基。
于是有唯一的整级数
$$
F_a^*\xi_{17}=\mathcal A_p(T)\xi_0.
\tag{5}
$$
这是整格结论，不是给未知局部周期任意指定一个单位归一。

## 3. 混合权 specialization 与周期的准确抵消

完整证明中的二变量图从同一个 full ray-class 椭圆单位系统出发：
先走基层反圆分 $\chi_m$ 路线，或先用 $2m+1$ 次 CM tensor
再走 cyclotomic 中央权路线，目标都为
$$
T_j^{-(2m+1)}(1+m),\qquad
\varphi_j^{-(2m+1)}\chi_{\rm cyc}^{1+m}.
\tag{6}
$$
tensor 向量在两条路线都是
$\mathbf u_j\otimes b_j^{\otimes(2m+1)}\otimes\zeta^{\otimes m}$。
norm、twist、specialization 都由同一群环基变换定义，故与局部化
和 dual exponential 交换。

full 系统的辅助 Euler 算子不能无证据在整个二变量环里求逆。
可选惰性 $\ell\equiv1\bmod p$、$\ell\nmid34p$，在两条目标角色上
该算子同为 $\ell^2+\ell^{-1}\equiv2\bmod p$。
所以最后的除法在同一个实际整格上合法。

Kato 2004 §15.8 给 CM tensor 的 period map；(15.16.1)
把上述椭圆单位类识别为对应高权 Beilinson–Kato 类。
Theorem 12.5(1) 在
$$
k=2m+2,\qquad r_{\rm crit}=m+1
$$
给共同 Tate 因子 $(2\pi i)^m$。
Lemma 15.11 的两个定义性 period 图将该结论拉回原 CM tensor 线；
任意的中间缩放同时消去。
此处不假设 Kato 在 §15.11 末尾明确未证明的高权 Betti/étale
motivic 兼容性，也不从“存在非零 de Rham 向量”推断整单位比较。

在同一实际 CM 整格中，(4) 的 tensor 比仅为 $a^{-(2m+1)}$，
是 $p$-单位。两条曲线的中央 theta 规范为
$$
d_m^{(j)}
 =f_j^{m+1}\bar f_j^{-m}
  \frac{\pi_{\mathbb C}^m}{m!\Omega_j^{2m+1}}
  L_{f_j}(\varphi_j^{2m+1},m+1).
\tag{7}
$$
Kato 规范与 (7) 相差
$(2i)^m m!\bar f_j^m/f_j^{m+1}$ 及去 $p$ 的 Euler 因子。
其中 $m!$ 两边完全相同；去 $p$ 的因子两边均为
$$
1-\frac{(-p)^{2m+1}}{p^{2m+2}}=1+\frac1p.
$$
这两个可能非单位的因子都准确抵消。
导子幂之比只含 $17$，局部微分之比是单位。
各自始终使用 primitive conductor，未给 $E_0$ 人为添上删 $17$
的 Euler 因子。

故当 $d_m^{(0)}\ne0$ 时，(5) 的同一个 specialization 满足
$$
\boxed{
v_p\mathcal A_p(x_m)=v_pd_m^{(17)}-v_pd_m^{(0)}.
}
\tag{8}
$$
这一相对式无需计算惰性 Lubin–Tate period 的绝对赋值。

## 4. 参考值与基层控制

[参考值完整证明](../notes/2026-11-12-rank-zero-reference-central-inert-value.md)
对所有上述惰性 $p$ 给
$$
p^2d_{p+1}^{(0)}
 \equiv\kappa_{0,p}^{\,2}(1+i)/2\not\equiv0\bmod p,
\quad
\kappa_{0,p}=-\frac12(-1)^{(p+1)/4}
 \binom{(p+1)/2}{(p+1)/4}.
\tag{9}
$$
证明直接使用实际点的 duplication、$\mathcal D^p=-\kappa\partial_U$、
实际 Cartier 常数 $C_p(S)=0$，以及完整中央有限和中仅可能留下的两项。
特别是 $v_pd_{p+1}^{(0)}=-2$。把它代入 (8) 即得 (1)。

BKO21 Theorems 6.1–6.2 对根数 $+$ 及平凡特征给
$$
\operatorname{corank}_{\mathcal O}
 \operatorname{Sel}_{p^\infty}(E_{17}/K)
 \le\operatorname{ord}_0\mathcal A_p.
$$
$-1$ 二次扭转与 $E_{17}$ 是同一 $\mathbb Q$ 曲线。
限制、corestriction 和两个整投影给该 $\mathcal O$ 余秩恰为
$s_p$。R4 给 $s_p\ge2$，已发表的 $p$-parity 定理给 $s_p$ 偶。

写 $\mathcal A_p=T^rB$，$B\in\mathcal O[[T]]$。
由 $v_px_p=1$ 得
$$
2\le s_p\le r\le v_p\mathcal A_p(x_p)
 =v_pd_{p+1}^{(17)}+2.
\tag{10}
$$
(10) 给中央整性；若 $v_pd_{p+1}\le1$，则偶数 $s_p$ 只能等于二。
Kummer 正合列及余有限生成性给初级 $\Sha$ 有限，证明 (3)。

## 5. 尚需完成的无穷性

充分目标现在是证明无穷多个惰性 $p$ 有 $d_{p+1}\not\equiv0\bmod p$。
R49 把固定中央值写成同一个有理 theta 系数的平方；
在固定有限例外之外，所需条件就是该固定系数 $b_{p+1}$ 为单位。
有限 $7,11$ 进证书仅检验本接口，不能代替无穷性。

### 完整证明与已发表来源

- [相对整周期比较全文](../notes/2026-11-12-inert-central-reference-curve-comparison.md)，
  包含整格、二变量交换图、全部非单位因子及精确符号范围。
- [秩零参考的全惰性首中央值](../notes/2026-11-12-rank-zero-reference-central-inert-value.md)。
- K. Kato, *p-adic Hodge theory and values of zeta functions of modular forms*,
  Astérisque **295** (2004), 117–290，Theorem 12.5(1)、§15.8、
  Proposition 15.9、Lemma 15.11、(15.16.1)：
  [原文](https://www.numdam.org/item/AST_2004__295__117_0.pdf)。
- A. Burungale, S. Kobayashi, K. Ota,
  *Rubin's conjecture on local units in the anticyclotomic tower at inert primes*,
  Annals of Mathematics **194** (2021), 943–966，
  Theorems 2.1、6.1、6.2：
  [原文](https://par.nsf.gov/servlets/purl/10336626)。
- 同三位作者，*p-adic L-functions and rational points on CM elliptic curves
  at inert primes*, JIMJ **23** (2024), 1417–1460，
  §2.2.1、Proposition 3.1、Definition 3.13、Corollary 4.11(i) 的证明：
  [期刊](https://doi.org/10.1017/S147474802300021X)。
- Dokchitser–Dokchitser, *On the Birch–Swinnerton-Dyer quotients modulo squares*,
  Annals **172** (2010), 567–596，Theorems 1.4、4.19；
  适用范围已在 R7 §9.5 核准。
- BKOY, JNT **270** (2025), Proposition 5.10，仅用于核对 mixed
  specialization 范围；本证明不以其任意非零 period 简写充当整比较。
