# R48. 实 theta 结构、中央平方与准确斜率判据

日期：2026-11-12。**状态：已证明；斜率对无穷多个素数非零仍待证明。**

## 1. 定理

在 R46 的固定截面
$$
S(z)=P(x(z)^2)\sigma_E(z)^d=\sum_{m\ge0}s_mz^m,\qquad d=L^2
$$
上作一次固定代数相位调整，使其复绝对值为一，不改变 R46 的 $\kappa$。
按 R46 在17处的第一分裂分量，选 $N\varpi=17$，
令 $q=\varpi/\bar\varpi$，其中 $\varpi$ 在该第一分量有赋值一。
则可以做到
$$
\boxed{\bar s_m=q^{-m}s_m\quad(m\ge0),\qquad
       \bar S(z)=S(q^{-1}z).}
\tag{1}
$$

对每个目标普通 $p\equiv1\pmod4$、$p\ge13$、$p\ne17$，
同一 $p$ 位上的实际测度和 Mellin 因子满足
$$
\nu_p^\dagger=[q^{-1}]_*\nu_p,\qquad
G_p^\dagger(T)=(1+T)^{b_p}G_p(T),
\quad b_p=\frac{\log_p\langle q^{-1}\rangle}{\log_p(1+p)}.
\tag{2}
$$
令
$$
c_p=\frac{\log_p\langle f^2/(dq)\rangle}{\log_p(1+p)},\qquad
\mathcal H_p(T)=(1+T)^{c_p/2}G_p(T).
$$
因为 $p$ 为奇数，$c_p/2\in\mathbb Z_p$，故这是无零点整单位的乘法。
R46 的完整中央分支成为
$$
\boxed{F_p^{\Theta,-}(T)=\kappa f\Omega_p\,\mathcal H_p(T)^2.}
\tag{3}
$$
$\mathcal H_p$ 非恒零、有界，且
$$
\mathcal H_p(0)=G_p(0)=G_p^\dagger(0)=0.
$$
R40 因而给出准确判据
$$
\boxed{
\Sha(E/\mathbb Q)[p^\infty]\text{ 有限}
\iff \mathcal H_p'(0)\ne0
\iff G_p'(0)\ne0.
}
\tag{4}
$$
以上对全部所列普通 $p$ 成立；常数是否整单位不影响零阶判据。

## 2. 包含2处的反线性对称性

在 Yang 的标准 Schrödinger 模型中，记复共轭算子为 $\mathcal C$。
对于 $g=x+y\delta\in K_v^1$，其 symplectic 矩阵为
$$
\iota_\alpha(g)=
\begin{pmatrix}
x&\delta^4\alpha y\\
y/(\delta^2\alpha)&x
\end{pmatrix}.
$$
两个对角元相同。若左下元 $c_g\ne0$，对应积分核差一个标量为
$$
|c_g|^{-1/2}
\psi\!\left(\frac{x u^2-2uv+xv^2}{2c_g}\right).
$$
它在 $u,v$ 下对称，故算子的 transpose 等于自身。
$c_g=0$ 时为标量乘恒等或反射，同样对称。
Weil 表示的酉性于是给
$$
\mathcal C\omega(g)\mathcal C
 =\mathcal C\omega(g)^{\rm transpose}\mathcal C
 =\omega(g)^*=\omega(g^{-1}).
\tag{5}
$$
这段直接论证也适用于 $\mathbb Q_2$，没有套用奇剩余特征的显式向量公式。

2处所选向量 $\phi_2$ 位于整个紧 norm-one 群的平凡等型线。
Yang 1997 Corollary 2.4 说明此线一维；
由 (5)，$\bar\phi_2$ 也在该线。
故 $\bar\phi_2=c_2\phi_2$，其中 $|c_2|=1$。
$\phi_2$ 的非零代数取值说明 $c_2$ 代数。

## 3. 17处的明确 Gauss 积分

本节写 $r=17$。设自然第一分量的 unitary 特征为 $\lambda$，
其单位限制为导子 $r$ 的四次特征。
R46 的单位范数向量经紧平均成为
$$
v(y)=A_0\lambda^{-1}(y)\mathbf1_{\mathbb Z_r^\times}(y),
\qquad A_0=\sqrt r/(r-1).
$$
自然作用为
$\omega_\lambda^{\rm nat}(a)\phi(y)=\lambda(a)|a|^{1/2}\phi(ay)$。
Yang (2.28) 给标准模型变换
$$
\rho\phi(x)=
\psi(cx^2/2)\int_{\mathbb Q_r}
       \psi(cxy+cy^2/4)\phi(y)\,dy,\qquad c=x_0^3\in\mathbb Z_r^\times.
\tag{6}
$$
Haar 测度取 $\operatorname{vol}(\mathbb Z_r)=1$。

第一份向量只支撑于 $v_r(x)=-1$。在 $x=t/r$、$t$ 为单位时，
$$
\rho v(t/r)=\frac{A_0}{r}\mathfrak G(\lambda^{-1})\lambda(ct)
          \psi(ct^2/(2r^2)).
\tag{7}
$$
这里 $\mathfrak G$ 是导子 $r$ 的有限 Gauss 和。

令 $v'=\omega_\lambda^{\rm nat}(r)v$。
换元 $z=ry$ 产生 Haar 因子 $r$，所以
$$
\rho v'(x)=A_0\lambda(r)\sqrt r\,\psi(cx^2/2)
 \int_{\mathbb Z_r^\times}
 \lambda^{-1}(z)\psi(cxz/r+cz^2/(4r^2))\,dz.
$$
对 $x=t/r$，按 $z=u+rh$ 求和，只有 $u=-2t\bmod r$ 留下；
在该类写 $z=-2t+rh$，二次相位为
$-ct^2/r^2+ch^2/4$，后一项的字符为一。
因此
$$
\rho v'(t/r)=\frac{A_0\lambda(r)}{\sqrt r}
 \lambda^{-1}(-2t)\psi(-ct^2/(2r^2)).
\tag{8}
$$
其余 $x$ 处由非平凡线性字符相消，仍只支撑在 $v_r(x)=-1$。

比较 (7) 的复共轭与 (8)，得到
$$
\mathcal C\rho(v)=c_{17}\rho(\omega_\lambda^{\rm nat}(17)v),
\qquad
c_{17}=
\frac{\overline{\mathfrak G(\lambda^{-1})}}
     {\sqrt{17}\lambda(17)}\lambda(-2/c).
\tag{9}
$$
$c_{17}$ 代数且复绝对值一。
方向是乘17，不能反写成乘 $17^{-1}$。
全部相位、Haar 因子及支撑计算的展开见下列完整证明笔记。

## 4. 从有限伸缩到固定系数关系

其余有限处的向量是实值未分歧向量。
设 $g_{17}$ 仅在17处等于 $(17,17^{-1})$。
由 (5)、(9)，R46 的同一有限平均满足
$$
\overline{\phi_f^{\rm av}}
 =c_f\,\omega_f(g_{17})\phi_f^{\rm av},
\qquad c_f=c_2c_{17},\quad |c_f|=1.
$$
$q=\varpi/\bar\varpi$ 的有限赋值恰为17处 $(1,-1)$，
其余为零，因此 $q_f g_{17}^{-1}$ 在固定紧群中。
有限平均在紧群下不变，故可将 $g_{17}$ 换成 $q_f$。

统一使用固定全局角色 $\chi_0$。
无穷 Hermite 向量 $h_m$ 实值，且
$\omega_\infty(q_\infty)h_m=q^m h_m$。
全局 theta 分布在 $G(\mathbb Q)$ 下不变，
于是
$$
\bar A_m=c_fq^{-m}A_m,\qquad
\bar b_m=c_fq^{-m}b_m.
$$
R46 的 $B(cz)=CS(z)$ 中 $c>0$ 为实数，
所以
$$
\bar s_m=\xi q^{-m}s_m,\qquad \xi=c_f C/\bar C,\quad|\xi|=1.
$$
由一个非零 $s_{m_0}$ 可识别
$\xi=q^{m_0}\bar s_{m_0}/s_{m_0}$ 为代数数。
取代数 $a$ 使 $a^2=\xi$，则 $|a|=1$、$\bar a=a^{-1}$。
将 $S$ 换成 $aS$，就得到 (1)。
这只作一次固定相位调整，不随 $m$ 或 $p$ 改变。

## 5. 平方及中心斜率

把代数恒等式 (1) 嵌入同一个目标 $p$ 位。
因为 $q^{-1}\in\mathbb Z_p^\times$，
全部矩满足
$$
\int x^m\,d\nu_p^\dagger=q^{-m}\int x^m\,d\nu_p.
$$
由有界测度的唯一性，或直接比较 Amice 变换，
得到 (2) 的推前式。乘单位保持单位区间，
其 principal Mellin 变换因此相差 $(1+T)^{b_p}$。

代入 R46 的整条分支恒等式，立即得到 (3)。
R40 已给 $\operatorname{ord}_0F_p^{\Theta,-}\ge2$，故
$$
\operatorname{ord}_0F_p^{\Theta,-}
 =2\operatorname{ord}_0\mathcal H_p
 =2\operatorname{ord}_0G_p\ge2.
$$
所以两个因子的单位质量确实都为零。
再用 R40 的准确有限性判据，得到 (4)。

注意这里没有把复共轭当成 $\mathbb C_p$ 的连续自同构；
先证明固定代数系数恒等式，之后才使用同一个 $p$ 嵌入。

## 6. 直接推论及范围

固定整函数
$$
S_{\mathbb R}(z)=S(z/\varpi)
$$
有实代数系数。这由
$q^{-m}\bar\varpi^{-m}=\varpi^{-m}$ 直接得到。

除一个固定有限集合外，
$$
v_p(d_{p-1})=2v_p(s_{p-1}).
$$
例外集须包括 $\kappa$ 的非单位素数及最终系数数域的分歧素数，
包括固定相位根所引入的分歧；此后 $v_p(s_{p-1})$ 为整数。
因此目标矩的赋值为偶整数，
$d_{p-1}\notin p^4$ 的充分条件等价于 $v_p(s_{p-1})=1$。
这仍仅是一个固定测试权的充分条件，不能替代 (4) 的完整充要判据。

[因子中心挠值证明](../notes/2026-11-12-theta-factor-center-torsion-trace.md)
还将 $G_p(0)$ 写成有限代数迹。
本结果遂证明该笔记的两个实际迹均为零。
下一项需要控制的是
[有限层对数和](../notes/2026-11-12-theta-slope-torsion-logarithm-tower.md)
所逼近的 $G_p'(0)$；各有限层非零不自动保证此极限非零。

### 完整证明与来源

- [实结构与整支平方完整证明](../notes/2026-11-12-theta-real-structure-and-mellin-square.md)，
  已由根端及另一研究线独立复算全部局部积分与全局方向。
- Tonghai Yang, *Theta liftings and Hecke L-functions*,
  J. reine angew. Math. **485** (1997), 25–53：
  Corollaries 2.4、2.10、2.14，式(2.28)，
  [作者全文](https://people.math.wisc.edu/~tonghaiyang/thetashort.pdf)。
- Tonghai Yang, *Nonvanishing of central Hecke L-values and rank of certain
  elliptic curves*, Compositio Math. **117** (1999), 337–359：
  Lemma 1.1、Appendix (A1)–(A3)；
  标准模型与无穷特征的第二次规范核对。
- R46 给同一固定截面及完整分支；R40 给完整 Selmer 的准确零阶判据。
