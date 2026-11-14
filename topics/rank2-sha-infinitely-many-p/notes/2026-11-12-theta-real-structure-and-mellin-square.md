# 固定 theta 截面的实结构与中央 Mellin 分支的平方

日期：2026-11-12。状态：以下实结构、整支平方及每个因子的中心消失均已证明；无穷多个素数处的简单零点仍未证明。

## 1. 结论及与 R46 的关系

使用 [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)
已经构造的固定截面

$$
 S(z)=P(x(z)^2)\sigma_E(z)^d=\sum_{m\ge0}s_mz^m,\qquad d=L^2,
$$

以及

$$
 e_m=\kappa(Nf\,d)^{-m}s_m\bar s_m\quad(4\mid m).
                                                               \tag{1}
$$

$L$ 只含素因子 $2,17$，$\kappa>0$ 为固定代数数。
下面允许把 $S$ 乘一个固定的、复绝对值为一的代数数；
这不改变 (1) 的 $\kappa$ 或任何零点阶。

固定 R46 在 $17$ 处的分裂识别

$$
 K\otimes\mathbb Q_{17}=\mathbb Q_{17}\times\mathbb Q_{17},
 \qquad i=(x_0,-x_0).
$$

选 $\varpi\in\mathbb Z[i]$、$N\varpi=17$，使其在第一分量的赋值为一，
并置

$$
 q=\frac{\varpi}{\bar\varpi}\in K^\times,\qquad |q|_{\mathbb C}=1.
                                                               \tag{2}
$$

例如 $x_0\equiv4\pmod{17}$ 时可取 $\varpi=4-i$。
$q$ 在每个有理素数 $p\ne17$ 的上方都是单位。

**定理。** 上述一次固定相位调整之后，

$$
 \boxed{\quad
       \bar s_m=q^{-m}s_m\quad(m\ge0),
       \qquad
       \bar S(z)=S(q^{-1}z).
       \quad}                                                 \tag{3}
$$

这里 $\bar S$ 仍指共轭代数 Taylor 系数，不表示固定 $p$ 位上的连续共轭。

对所有目标普通素数 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$，
R46 的两个实际 principal Mellin 因子满足

$$
 \boxed{\quad
 G_p^\dagger(T)=(1+T)^{b_p}G_p(T),\qquad
 b_p=\frac{\log_p\langle q^{-1}\rangle}{\log_p(1+p)}
          \in\mathbb Z_p .
 \quad}                                                       \tag{4}
$$

因此，令

$$
 c_p=\frac{\log_p\langle f^2/(dq)\rangle}{\log_p(1+p)}
      \in\mathbb Z_p,\qquad
 \mathcal H_p(T)=(1+T)^{c_p/2}G_p(T),
                                                               \tag{5}
$$

则

$$
 \boxed{\quad F_p^{\Theta,-}(T)=\kappa f\Omega_p\,
                         \mathcal H_p(T)^2. \quad}              \tag{6}
$$

$p$ 为奇数，所以 (5) 的 $c_p/2\in\mathbb Z_p$。
$\mathcal H_p$ 非恒零、有界，且

$$
 \operatorname{ord}_0\mathcal H_p\ge1,\qquad
 \boxed{\quad
  \Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
     \iff \mathcal H_p'(0)\ne0
     \iff G_p'(0)\ne0.
 \quad}                                                       \tag{7}
$$

这里各因子的中心消失是结论：
没有预先从测度总质量为零推出单位区间质量为零。

## 2. 标准模型的反线性对称性，包含 $2$ 处

记 $\mathcal C\phi=\bar\phi$ 为 Schrödinger 模型中函数值的复共轭。
本节证明

$$
 \mathcal C\omega_{1,\chi_0}(g)\mathcal C
                    =\omega_{1,\chi_0}(g^{-1}).                \tag{8}
$$

不需要假设剩余特征为奇数，也不需要 $2$ 处显式 lattice 向量。

Yang 的标准基为 $\{\delta,1/(\delta^2\alpha)\}$。
对 $g=x+y\delta$，其 symplectic 矩阵是

$$
 \iota_\alpha(g)=
 \begin{pmatrix}
 x&\delta^4\alpha y\\
 y/(\delta^2\alpha)&x
 \end{pmatrix}.                                              \tag{9}
$$

关键是两个对角元相等。
若其左下元 $c_g\ne0$，标准 Schrödinger 算子差一个只依赖 $g$ 的标量后，
有核

$$
 |c_g|^{-1/2}
 \psi\!\left(\frac{x u^2-2uv+xv^2}{2c_g}\right).
                                                               \tag{10}
$$

(10) 可直接由 Bruhat 分解的乘法算子、伸缩与 Fourier 变换得到；
它在 $\mathbb Q_2$ 上同样成立。该核在 $u,v$ 下对称，
而 splitting 只乘一个标量，不破坏对称性。
故 $\omega(g)$ 关于双线性配对 $\int\phi\psi$ 的 transpose 等于自身。
当 $c_g=0$ 时 $g=\pm1$，算子为标量乘恒等或反射，其核也对称。

另一方面 Weil 表示是酉表示，
$\omega(g)^*=\omega(g^{-1})$。
把 Hermitian adjoint 写成
$\mathcal C\,\omega(g)^{\rm transpose}\mathcal C$，
即得 (8)。

在 $2$ 处，R46 所选的 $\phi_2$ 位于整个紧群 $K_2^1$ 的平凡等型线。
Yang 1997 Corollary 2.4 给这条线一维。
由 (8)，$\bar\phi_2$ 也在此线，因此存在固定 $c_2$ 使

$$
 \bar\phi_2=c_2\phi_2,\qquad |c_2|_{\mathbb C}=1.              \tag{11}
$$

$\phi_2$ 可取代数值且非零；在任一非零取值点取比值，
可知 $c_2\in\overline{\mathbb Q}^\times$。
其余未分歧有限处的向量为实值的 $\mathbf1_{\mathbb Z_\ell}$，
不产生其他相位。

## 3. $17$ 处的紧平均与准确 Fourier 计算

本节只在 $\mathbb Q_{17}$ 上计算，记 $r=17$，以免与变化的目标 $p$ 混淆。
令 $\lambda=(\chi_0)_{\mathfrak l}$ 为自然极化中第一分量的特征。
$\lambda$ 是酉特征，其单位限制为导子 $r$ 的非平凡四次特征。
固定加法特征 $\psi$ 的导子为 $\mathbb Z_r$，Haar 测度给
$\operatorname{vol}(\mathbb Z_r)=1$。

自然极化中的原向量为
$\sqrt r\,\mathbf1_{1+r\mathbb Z_r}$。
用 $\operatorname{vol}(\mathbb Z_r^\times)=1$ 的乘法 Haar 紧平均，
得到

$$
 v(y)=A_0\lambda^{-1}(y)\mathbf1_{\mathbb Z_r^\times}(y),
 \qquad A_0=\frac{\sqrt r}{r-1}\in\mathbb R_{>0}.
                                                               \tag{12}
$$

自然模型的作用是
$\omega^{\rm nat}_\lambda(a)\phi(y)=\lambda(a)|a|^{1/2}\phi(ay)$。
Yang 1997 (2.28) 的标准模型变换为

$$
 \rho\phi(x)=
 \psi(cx^2/2)\int_{\mathbb Q_r}
            \psi(cxy+cy^2/4)\phi(y)\,dy,\qquad c=x_0^3.
                                                               \tag{13}
$$

这里 $\alpha=1$、$|c|_r=1$，所以原文的 $|c|^{1/2}$ 等于一。

定义有限 Gauss 和

$$
 \mathfrak G(\lambda^{-1})
   =\sum_{a\in(\mathbb Z/r)^\times}
       \lambda^{-1}(a)\psi(a/r).
                                                               \tag{14}
$$

### 3.1 第一份向量

因 $y\in\mathbb Z_r^\times$ 时 $\psi(cy^2/4)=1$，
(13) 中的积分是一个 primitive tame Gauss 变换。
它只支撑在 $v_r(x)=-1$。
在 $x=t/r$、$t\in\mathbb Z_r^\times$ 时，

$$
 \rho v(t/r)
  =\frac{A_0}{r}\mathfrak G(\lambda^{-1})\lambda(ct)
        \psi\!\left(\frac{ct^2}{2r^2}\right).                \tag{15}
$$

因此

$$
 \overline{\rho v(t/r)}
  =\frac{A_0}{r}\overline{\mathfrak G(\lambda^{-1})}
        \lambda^{-1}(ct)
        \psi\!\left(-\frac{ct^2}{2r^2}\right).
                                                               \tag{16}
$$

### 3.2 乘统一化元后的向量

令 $v'=\omega^{\rm nat}_\lambda(r)v$。则

$$
 v'(y)=\frac{A_0\lambda(r)}{\sqrt r}
       \lambda^{-1}(ry)\mathbf1_{\{v_r(y)=-1\}}.             \tag{17}
$$

在 (13) 中令 $z=ry$，注意 $dy=r\,dz$，得到

$$
 \rho v'(x)=A_0\lambda(r)\sqrt r\,\psi(cx^2/2)
  \int_{\mathbb Z_r^\times}
       \lambda^{-1}(z)
       \psi\!\left(\frac{cxz}{r}+\frac{cz^2}{4r^2}\right)dz.
                                                               \tag{18}
$$

取 $x=t/r$。把积分按 $z\bmod r^2$ 展开，并写 $z=u+rh$，
对 $h\bmod r$ 的和只有当 $u=-2t\bmod r$ 时不为零。
在唯一的该 residue class 内改写 $z=-2t+rh$，
二次相位为

$$
 \frac{c}{r^2}(tz+z^2/4)
       =-\frac{ct^2}{r^2}+\frac{ch^2}{4}.
$$

后一项的加法特征为一。因此

$$
 \rho v'(t/r)=
 \frac{A_0\lambda(r)}{\sqrt r}\lambda^{-1}(-2t)
       \psi\!\left(-\frac{ct^2}{2r^2}\right).
                                                               \tag{19}
$$

这份向量也只支撑在 $v_r(x)=-1$。
确实，$v_r(x)\ge0$ 时，所有单位 $u\bmod r$ 的线性相位都非平凡；
$v_r(x)<-1$ 时，把单位区间分成模 $r^{-v_r(x)}$ 的小区间，
再作一次长度 $r$ 的平移，同样得到非平凡线性字符而积分为零。

比较 (16) 与 (19)，得到固定相位

$$
 \boxed{\quad
 \mathcal C\rho(v)=c_{17}\rho\bigl(\omega^{\rm nat}_\lambda(17)v\bigr),
 \qquad
 c_{17}=
 \frac{\overline{\mathfrak G(\lambda^{-1})}}
      {\sqrt{17}\lambda(17)}
       \lambda(-2/c).
 \quad}                                                       \tag{20}
$$

$c_{17}$ 代数，且 primitive Gauss 和的绝对值为 $\sqrt{17}$，
故 $|c_{17}|_{\mathbb C}=1$。
特别要注意 (20) 是乘 $17$，不是乘 $17^{-1}$。

## 4. 类数一把有限伸缩变成无穷旋转

令 $\phi_f^{\rm av}$ 为 R46 的同一个有限紧平均。
设 $g_{17}\in G(\mathbb A_f)$ 在 $17$ 处是
$(17,17^{-1})$，其余有限处是一。
由 (11)、(20) 及 $\rho$ 的等变性，

$$
 \overline{\phi_f^{\rm av}}
       =c_f\,\omega_f(g_{17})\phi_f^{\rm av},
 \qquad c_f=c_2c_{17}\in\overline{\mathbb Q},\quad |c_f|=1.
                                                               \tag{21}
$$

(2) 的 $q$ 在 $17$ 处的两个赋值是 $(1,-1)$，
其余有限处均为零。因此

$$
 q_f g_{17}^{-1}\in\mathcal K_f.
$$

$\phi_f^{\rm av}$ 在 $\mathcal K_f$ 下不变，所以
$\omega_f(g_{17})\phi_f^{\rm av}=\omega_f(q_f)\phi_f^{\rm av}$。

现在统一使用固定全局角色 $\chi_0$，
让无穷向量的 Hermite 指标 $m$ 变化。
R46 已核其无穷特征为

$$
 \omega_\infty(q_\infty)h_m=q^m h_m.
                                                               \tag{22}
$$

$h_m$ 实值。全局 theta 分布 $\mathcal T$ 在
$q\in G(\mathbb Q)$ 下不变，故

$$
 \begin{aligned}
 \overline{A_m}
 &=\mathcal T(h_m\otimes\overline{\phi_f^{\rm av}})\\
 &=c_f\mathcal T(h_m\otimes\omega_f(q_f)\phi_f^{\rm av})\\
 &=c_f q^{-m}\mathcal T(h_m\otimes\phi_f^{\rm av})
   =c_f q^{-m}A_m.
 \end{aligned}                                                \tag{23}
$$

这里 $A_m=\sum_n a_nh_m(n/L)$。
该论证对所有 $m$ 成立；$4\nmid m$ 时两边本来均为零。

Hermite 系数转换中的因子是实数，
所以 (23) 也给 $\bar b_m=c_f q^{-m}b_m$。
R46 的 $B(cz)=C S(z)$ 中 $c>0$ 为实数，
于是

$$
 \bar s_m=\xi q^{-m}s_m,\qquad
 \xi=c_f\,\frac{C}{\bar C},\qquad |\xi|=1.                    \tag{24}
$$

虽然尚不单独识别 $C$，取一个已知存在的非零 $s_{m_0}$，
就有

$$
 \xi=q^{m_0}\frac{\bar s_{m_0}}{s_{m_0}}
                 \in\overline{\mathbb Q}^\times.
                                                               \tag{25}
$$

取代数数 $a$ 满足 $a^2=\xi$；因 $|\xi|=1$，有
$|a|=1$ 及 $\bar a=a^{-1}$。
将 $S$ 换成 $aS$，(24) 就成为 (3)。
这一调整固定一次，对所有 $m$ 和所有目标素数同时使用。

## 5. 同一 $p$ 位上的测度关系与整支平方

固定一个目标普通 $p\ne17$。在本课题嵌入下
$q^{-1}\in\mathbb Z_p^\times$。
(3) 给全部矩的关系

$$
 \int x^m\,d\nu_p^\dagger
   =q^{-m}\int x^m\,d\nu_p\qquad(m\ge0).                     \tag{26}
$$

等价地，也可直接比较 Amice 变换：

$$
 \mathcal A_p^\dagger(Z)
   =S(q^{-1}\Omega_p\log(1+Z))
   =\mathcal A_p((1+Z)^{q^{-1}}-1).
                                                               \tag{27}
$$

所以有界测度严格满足

$$
 \nu_p^\dagger=[q^{-1}]_*\nu_p.
                                                               \tag{28}
$$

乘单位保持 $\mathbb Z_p^\times$；
又因 Teichmüller 分解具有乘法性，
$\langle q^{-1}x\rangle=\langle q^{-1}\rangle\langle x\rangle$。
对 (28) 取 principal Mellin 变换便得到 (4)。

此处没有在 $\mathbb C_p$ 内“作复共轭”：
先在固定代数系数上证明 (3)，再把两边嵌入同一个 $p$ 位，
得到实际乘单位的推前关系 (28)。

将 (4) 代入 R46 的完整分支恒等式

$$
 F_p^{\Theta,-}(T)=
 \kappa f\Omega_p(1+T)^{\log_p\langle f^2/d\rangle/\log_p(1+p)}
                      G_p(T)G_p^\dagger(T)
$$

即得 (5)–(6)。
所有额外幂级数都是无零点的整单位，常数 $\kappa f\Omega_p$ 非零。
于是

$$
 \operatorname{ord}_0 F_p^{\Theta,-}
              =2\operatorname{ord}_0\mathcal H_p
              =2\operatorname{ord}_0G_p.
                                                               \tag{29}
$$

R40 已证明左边至少为二，
故 $G_p(0)=G_p^\dagger(0)=\mathcal H_p(0)=0$。
R40 的准确有限性判据为左边等于二，
因而得到 (7)。

## 6. 另一种实系数形式与尚存缺口

(3) 还说明固定整函数

$$
 S_{\mathbb R}(z)=S(z/\varpi)
             =\sum_{m\ge0}\frac{s_m}{\varpi^m}z^m
$$

具有实代数系数：因为
$q^{-m}\bar\varpi^{-m}=\varpi^{-m}$。
这不表示原来的 $S$ 已有实系数，也不要求所选 $p$ 位被复共轭保持。

在固定有限例外集外，目标矩现在有准确偶赋值

这里的例外集明确包含最终系数数域的判别式素因子，
包括为上述相位调整加入的代数根所产生的分歧素数；
因而其外所用归一化赋值 $v_p(p)=1$ 对这些系数取整数值。

$$
 v_p(d_{p-1})=2v_p(s_{p-1}),
                                                               \tag{30}
$$

因为 $q$ 是 $p$ 单位，$\kappa$ 是除固定有限集合外的单位。
因此此前 $v_p(d_{p-1})<4$ 的充分条件，在这些素数上成为
$v_p(s_{p-1})=1$（已知下界为一）。
完整初级有限性仍由 (7) 的中心导数给出，
不能把固定测试权的充分条件反过来当成等价条件。

本文证明所有目标普通 $p$ 的同一单因子都有中心零点。
主问题还需要证明其中无穷多个是简单零点。
固定截面、实结构、代数有限挠点迹或复中央值非零，
本身都没有给出这个新的跨素数非消失输入。

### 一手来源与依赖

- Tonghai Yang, *Theta liftings and Hecke L-functions*,
  J. reine angew. Math. **485** (1997), 25–53：
  Corollary 2.4（非分裂等型线的一维性）、
  Corollary 2.10（自然极化作用）、
  (2.28) 与 Corollary 2.14（$\rho$ 的规范与等变性）、
  (2.12)–(2.14)（全局 theta 分布及不变性）。
  [作者原文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
- Tonghai Yang, *Nonvanishing of central Hecke L-values and rank of certain elliptic curves*,
  Compositio Math. **117** (1999), 337–359：
  Lemma 1.1、Appendix (A1)–(A3) 给相同标准模型。
  本文在 $2$ 处使用的是对称 kernel 加酉性的直接论证，
  没有套用该文只在奇剩余特征写出的 lattice eigenfunction 公式。
  [出版社原文](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/915B51D40C0BD146C3DBC94DE4041BDD/S0010437X99000433a.pdf/nonvanishing_of_central_hecke_lvalues_and_rank_of_certain_elliptic_curves.pdf)。
- 固定有限向量、共同代数 sigma 截面及完整分支比较：
  [R46](../results/R46-fixed-sigma-section-and-central-mellin-factors.md)。
  中央零阶与 Selmer 的准确比较使用 R40。

$17$ 处两份向量的全部 Gauss 因子、Haar 因子和乘 $17$ 的方向，
以及第 2 节的反线性论证，已在本文中直接证明。
