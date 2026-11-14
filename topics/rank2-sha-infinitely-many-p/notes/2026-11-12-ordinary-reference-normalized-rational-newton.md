# 用秩零参考消去周期：线性权 Newton 证书与纯有理版本

日期：2026-11-12。状态：已证明，主问题的无穷素数非消失仍未解决。
本篇把 R56 的无周期证书从单个指数增长权序列，改为有限个线性增长权。
再给一个只用两个固定整数序列的版本，连 Euler 因子也无需作为输入。

## 1. 同一正式周期下的实际参考

固定普通目标素数 $p\ge13$、$p\ne17$。
令 $E_0:y^2=x^3-x$，$E_{17}:y^2=x^3-17x$，
并在同一 $K=\mathbb Q(i)\hookrightarrow\mathbb Q_p$ 中取
$$
\pi_0=\psi_0(\mathfrak p),\qquad
\pi_{17}=\psi_{17}(\mathfrak p),\qquad
v_p(\pi_0)=v_p(\pi_{17})=1.
\tag{1}
$$
两者的共轭均为 $p$ 进单位。这两个 Hecke 角色分别属于两条曲线，
不能在 Euler 因子中未经说明地混用。

选 $\eta^4=17$。它在
$\mathcal O=\widehat{\mathbb Z_p^{\mathrm{ur}}}$ 中是单位，
曲线的整 CM 同构给
$$
\vartheta_{17}(z)=\vartheta_0(\eta z),\qquad
\Omega_0=\eta\Omega_{17}.
\tag{2}
$$
因此可把参考和实际因子放在同一个 $\Omega_{17}$ 上：
$$
\begin{aligned}
h_m&=m![z^m]A_{17}(z)\in\mathbb Z,\\
t_m&=m![z^m]\vartheta_{17}(z)\in\mathbb Z.
\end{aligned}
\tag{3}
$$
整性由 R57 的同一多项式流给出。
不把 $\eta$ 当成 $\mathbb Z_p$ 上的乘法自同态；
(2) 是两条椭圆正式群之间的真正整同构所诱导的周期选择。

记实际的 principal Mellin 变换为 $J_A=J_p$，
参考的为 $J_\theta$。R51 给 $J_A(0)=0$。
参考满足更强的
$$
\boxed{J_\theta(0)\in\mathcal O^\times.}
\tag{4}
$$
以下核实这一点，而不从正权矩擅自删掉原点原子。

参考的实际中央 theta 平方公式中，
$L(E_0,1)/\Omega_{\mathrm{real},0}=1/4$、
$d_0/f_0=1/4$，$f_0=2(1+i)$；
参考截面平方常数也是 $1/4$。
这些因子及正式周期在所列 $p$ 处均为单位，剩下的中央 Euler
因子为 $(1-\bar\pi_0^{-1})^2$。
它是单位：$E_0$ 的全二挠点有理，所以普通 $p$ 下
$a_p(E_0)\equiv2\pmod4$；Hasse 界在 $p\ge13$ 排除
$a_p(E_0)\equiv1\pmod p$。
因为 $\bar\pi_0\equiv a_p(E_0)\pmod p$，该 Euler 因子非零模 $p$。
于是实际中央平方公式的两侧赋值都为零，给出 (4)。
所有规范来自 R46 及
[dyadic/reference 笔记](2026-11-12-dyadic-vector-and-reference-theta.md)，
不是给未知周期另加单位假设。

## 2. 正权值的两个准确 Euler 因子

对正整数 $m\equiv0\pmod{p-1}$，写
$$
T_m=(1+p)^m-1,\qquad
E_D(m)=1-\frac{\pi_D^m}{\bar\pi_D^{m+1}}
\quad(D=0,17).
\tag{5}
$$
则
$$
\begin{aligned}
J_A(T_m)&=E_{17}(m)\Omega_{17}^m h_m,\\
J_\theta(T_m)&=E_0(m)\Omega_{17}^m t_m.
\end{aligned}
\tag{6}
$$
第一式是 R51 的实际 single-Euler 插值。
第二式在参考分布可能有原点原子时仍成立：
参考等式是
$$
\nu_\theta^{(0)}|_{p\mathbb Z_p}
-\bar\pi_0^{-1}[\pi_0/\bar\pi_0]_*\nu_\theta^{(0)}
=\gamma_p\delta_0.
$$
取正权 $x^m$ 时，$\delta_0$ 的矩为零，正好得到 (6)；
没有声称 $\gamma_p=0$。

由于 (4)，$J_\theta$ 在 $\mathcal O[[T]]$ 中是单位；
$T_m\in p\mathbb Z_p$，故 $J_\theta(T_m)$ 是单位。
$E_0(m)$、$\Omega_{17}$ 也为单位，所以
$$
\boxed{t_m\in\mathbb Z_p^\times
\quad\text{对每个正 }m\equiv0\pmod{p-1}.}
\tag{7}
$$
因此下面的所有系数比值都有准确可逆的分母。

## 3. 真正的 Iwasawa 商降到 $\mathbb Z_p$

在 Iwasawa 环中定义
$$
\mathscr R_p(T)=\frac{J_A(T)}{J_\theta(T)}\in\mathcal O[[T]].
\tag{8}
$$
它满足 $\mathscr R_p(0)=0$，且由 (6) 有
$$
\boxed{
\mathscr R_p(T_m)
=\frac{E_{17}(m)}{E_0(m)}\,\frac{h_m}{t_m}
\in\mathbb Q_p.
}
\tag{9}
$$
右端没有任何正式周期。
Euler 因子属于选定嵌入下的 $\mathbb Q(i)\subset\mathbb Q_p$，
而 $h_m,t_m$ 是固定整数。

事实上
$$
\boxed{\mathscr R_p(T)\in\mathbb Z_p[[T]].}
\tag{10}
$$
证明不需要一般的固定域定理。取 $m_n=(p-1)p^n$，
则 $T_{m_n}\ne0$ 且趋于零。若
$\mathscr R_p(T)=\sum c_kT^k$，先有 $c_0=0$；
已知 $c_0,\ldots,c_{k-1}\in\mathbb Q_p$ 时，
$$
c_k=\lim_{n\to\infty}
\frac{\mathscr R_p(T_{m_n})-
       \sum_{j<k}c_jT_{m_n}^{\,j}}{T_{m_n}^{\,k}}
\in\mathbb Q_p,
$$
因为 $\mathbb Q_p$ 在完备系数域中闭。
原有 $\mathcal O$ 整性再给 $c_k\in\mathbb Z_p$。

特别地，
$$
\mathscr R_p'(0)=J_p'(0)/J_\theta(0),\qquad
v_p\mathscr R_p'(0)=v_pJ_p'(0).
\tag{11}
$$
这是**两个 Mellin 变换在 Iwasawa 环中的商**。
本篇从未声称函数商 $A_{17}/\vartheta_{17}$ 的 Mellin 变换
等于 (8)；普通 Amice 乘法与单位 Mellin 乘法不能互换。

## 4. 完备、无周期的线性权证书

令 $m_j=j(p-1)$，$V_0=0$，并定义明确的代数数
$$
V_j=\frac{E_{17}(m_j)}{E_0(m_j)}\frac{h_{m_j}}{t_{m_j}}
\in\mathbb Q(i)\hookrightarrow\mathbb Q_p\quad(j\ge1).
\tag{12}
$$
置
$$
\Delta_r=\sum_{j=0}^r(-1)^{r-j}\binom rj V_j,\qquad
S_R=\sum_{r=1}^{R}\frac{(-1)^{r+1}}r\Delta_r.
\tag{13}
$$
因为 (10)，将其视为有界测度的 Amice 变换，或逐幂展开
$\mathscr R_p((1+p)^{(p-1)u}-1)$，均给
$\Delta_r\in p^r\mathbb Z_p$。
Newton 展开在 $u=0$ 求导于是得到
$$
(p-1)\log_p(1+p)\mathscr R_p'(0)
=\sum_{r\ge1}\frac{(-1)^{r+1}}r\Delta_r.
\tag{14}
$$
令
$$
H_p(R)=\min_{r>R}\bigl(r-v_p(r)\bigr)
\ge R+1-\lfloor\log_p(R+1)\rfloor.
\tag{15}
$$
则
$$
\boxed{
v_p\!\left(
S_R-(p-1)\log_p(1+p)\mathscr R_p'(0)
\right)\ge H_p(R).
}
\tag{16}
$$
由于 $H_p(R)\to\infty$，结合 R40/R51 得
$$
\boxed{
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}
\iff
\exists R\ge1:\ v_p(S_R)<H_p(R).
}
\tag{17}
$$
最高权只有 $R(p-1)$，而没有 $\Omega_p$ 的有限精度输入。
本条件对每个固定普通 $p$ 完备，不是只检测导数是否为单位。
若 $\mathscr R_p'(0)=0$，则每个 $S_R$ 都落入相应误差理想；
若其非零，任取 $H_p(R)>1+v_p\mathscr R_p'(0)$ 就能检测到。

## 5. 纯有理版本：连 Euler 因子也可去掉

还可以只使用两个固定整数序列，不输入 $\pi_0,\pi_{17}$。
对 $R\ge1$，选整数 $s=s(R)\ge1$ 满足
$$
p\nmid s,\qquad s(p-1)\ge R.
\tag{18}
$$
例如取不小于 $\lceil R/(p-1)\rceil$ 的第一个 $p$ 进单位整数。
设
$$
\rho_0=0,\qquad
\rho_j=\frac{h_{sj(p-1)}}{t_{sj(p-1)}}\in\mathbb Q,\qquad
\widetilde S_{p,R}
=\sum_{r=1}^{R}\frac{(-1)^{r+1}}r
 \sum_{j=0}^r(-1)^{r-j}\binom rj\rho_j.
\tag{19}
$$
则，记
$B_p(R)=R+1-\lfloor\log_p(R+1)\rfloor$，
有
$$
\boxed{
v_p\!\left(\widetilde S_{p,R}-
s(p-1)\log_p(1+p)\mathscr R_p'(0)\right)
\ge B_p(R).
}
\tag{20}
$$

**证明。** 沿步长 $s(p-1)$ 重做 (13)–(16)，因 $p\nmid s$，
Newton 差分仍在 $p^r\mathbb Z_p$ 中，尾界仍为 (15)。
而对 $m=sj(p-1)>0$，
$$
v_p\left(\frac{E_{17}(m)}{E_0(m)}-1\right)\ge m.
$$
又因为 $\mathscr R_p(0)=0$，
$$
v_p(\rho_j)
=v_p(\mathscr R_p(T_m))
\ge1+v_p(j).
$$
所以用 $\rho_j$ 代替含 Euler 的真实值，引入的每个误差
至少在 $p^{s(p-1)+1}$ 中。作整数差分后除以 $r\le R$，
总误差估值至少为
$$
s(p-1)+1-\lfloor\log_pR\rfloor\ge B_p(R).
$$
与尾界合并即得 (20)。$\square$

因此又有只含有理数的完整证书：
$$
\boxed{
\Sha[p^\infty]\text{有限}
\iff\exists R\ge1:
v_p(\widetilde S_{p,R})<B_p(R).
}
\tag{21}
$$
尽管 $s$ 随 $R$ 改变，$p\nmid s$ 保证 (20) 主项的赋值恒为
$1+v_p\mathscr R_p'(0)$，所以双向完备性的论证不受影响。

当 $1\le R\le p-2$，可直接取 $s=1$；
真实尾界恰为 $R+1$，Euler 误差比它更高，故 (20) 可用
$p^{R+1}$ 精度。这一范围仍只有线性最高权 $R(p-1)$。
一般情形按 (18) 取 $s$ 时，最高权
$sR(p-1)\le R^2+2R(p-1)$；
它是以二次权增长换来完全不含 Euler 数据的有理证书。

若用 R57 的统一整数 $a_r$ 和
$T_r=\vartheta_0^{(4r)}(0)\in\mathbb Z$，则 (19) 里的比值更简洁：
$$
\frac{h_{4r}}{t_{4r}}=\frac{a_r}{17T_r}.
\tag{22}
$$
分母 $T_r$ 在所用 principal 权上由 (7) 保证为 $p$ 进单位。

## 6. 一个归一化核查与保留的缺口

[纯有理 Newton 脚本](../scripts/check-ordinary-reference-newton.py)
只用 R57 的整数递推计算 (19)。
在 $p=13,R=2,s=1$ 时，
$$
\widetilde S_{13,2}\equiv1248\pmod{13^3},\qquad
\mathscr R_{13}'(0)\equiv60\pmod{13^2}.
$$
另由参考的权 $156$ 矩计算中心
$J_\theta(0)\equiv133\pmod{13^2}$；
所以
$$
J_{13}'(0)\equiv60\cdot133\equiv37\pmod{13^2},
$$
与 R56 独立单权规范一致。
权 $156$ 只用于这次归一化交叉核查；
本篇求 $\mathscr R_{13}'(0)$ 的实际证书仅用了权 $12,24$。

现在的全局输入确实只是同一对整数序列 $(a_r,T_r)$。
仍缺少的是对无穷多个普通 $p$，证明某个有限 $R$ 满足 (21)；
有限精度或固定上界 $R$ 的非消失未被本篇推出。
不把 Iwasawa 环中的可逆参考解释成已经计算了实际中心导数。

依赖：R40、R46、R49、R51、R55–R57（2026-11-12），以及
[五次参考截面](2026-11-12-degree-five-theta-lucas-interface.md) §4
已保留原点原子的正权分布。
所有新商、下降、误差与纯有理证书的证明均在本文给出。


## 7. 同一实际因子的四阶导数参考

还可以完全去掉另一条曲线的参考。令
\[
B(z)=A_{17}^{(4)}(z),\qquad h_4=24,
\]
并把实际 Amice 测度记为 \(\nu_A\)，即
\(A_{17}(\Omega_{17}\log(1+Z))=\int(1+Z)^x\,d\nu_A(x)\)。
对 \(\Theta_Z=(1+Z)d/dZ\) 有
\[
B(\Omega_{17}\log(1+Z))
=\Omega_{17}^{-4}\Theta_Z^4
 A_{17}(\Omega_{17}\log(1+Z)).
\]
因此 \(B\) 的有界整测度恰为
\[
d\nu_B(x)=\Omega_{17}^{-4}x^4\,d\nu_A(x).
\tag{23}
\]
这里 \(\Omega_{17}^{-4}\) 是必要的归一化；它是 \(\mathcal O\) 中的单位。
令 \(J_B\) 为该测度限制到 \(\mathbb Z_p^\times\) 的 principal Mellin 变换，则
\[
J_B(0)
=\Omega_{17}^{-4}\left(
 \int_{\mathbb Z_p}x^4\,d\nu_A-
 \int_{p\mathbb Z_p}x^4\,d\nu_A\right)
\equiv24\pmod{p^4\mathcal O}.
\tag{24}
\]
故 \(J_B\in\mathcal O[[T]]^\times\)。此单位性只用实际有界测度和
已认证的 \(h_4=24\)，无需秩零参考的中央值或原点原子分析。

对任意正 \(m\equiv0\pmod{p-1}\)，从总矩减去 \(p\mathbb Z_p\) 上的矩得
\[
\begin{aligned}
J_A(T_m)&=\Omega_{17}^m h_m+O(p^m),\\
J_B(T_m)&=\Omega_{17}^m h_{m+4}+O(p^{m+4}),
\end{aligned}
\tag{25}
\]
其中 \(O(p^a)\) 表示属于 \(p^a\mathcal O\)。
第二式与 (24) 给出
\[
h_{m+4}\in\mathbb Z_p^\times.
\tag{26}
\]
定义 \(\mathscr Q_p=J_A/J_B\)。它属于 \(\mathcal O[[T]]\)，满足
\(\mathscr Q_p(0)=0\)，且 (25) 给出真正的有理近似
\[
\mathscr Q_p(T_m)-\frac{h_m}{h_{m+4}}\in p^m\mathcal O.
\tag{27}
\]
这里不需要把近似误差提升为 \(p^{m+1}\)。

尽管 (27) 的真实值未必已知属于 \(\mathbb Q_p\)，仍有
\[
\boxed{\mathscr Q_p(T)\in\mathbb Z_p[[T]].}
\tag{28}
\]
完整下降证明如下。取 \(m_n=(p-1)p^n\)，则
\(v_p(T_{m_n})=n+1\)。写 \(\mathscr Q_p=\sum c_kT^k\)。
已知 \(c_0,\ldots,c_{k-1}\in\mathbb Q_p\) 时，
\[
c_k=\lim_{n\to\infty}
\frac{h_{m_n}/h_{m_n+4}
-\sum_{j<k}c_jT_{m_n}^{\,j}}{T_{m_n}^{\,k}}.
\]
因为 (27) 的差在右边除去 \(T_{m_n}^k\) 后，赋值至少为
\(m_n-k(n+1)\to+\infty\)，该等式成立。
每个近似项都在闭子域 \(\mathbb Q_p\) 中，故 \(c_k\in\mathbb Q_p\)；
原有 \(\mathcal O\) 整性给 \(c_k\in\mathbb Z_p\)。
并且
\[
\mathscr Q_p'(0)=J_A'(0)/J_B(0),\qquad
v_p\mathscr Q_p'(0)=v_pJ_A'(0).
\tag{29}
\]

现在所有有理输入均可取自**同一固定整数序列的相邻项**：
\[
\frac{h_{4r}}{h_{4r+4}}=\frac{a_r}{17a_{r+1}}.
\tag{30}
\]
具体地，在 (19) 中把 \(\rho_j\) 换为
\[
q_0=0,\qquad
q_j=\frac{h_{sj(p-1)}}{h_{sj(p-1)+4}},
\]
并要求
\[
p\nmid s,\qquad s(p-1)\ge R+1.
\tag{31}
\]
记相应 Newton 和为 \(\widehat S_{p,R}\)。由 (28) 的真实 Newton
尾界及 (27)，
\[
v_p\!\left(\widehat S_{p,R}
-s(p-1)\log_p(1+p)\mathscr Q_p'(0)\right)
\ge B_p(R).
\tag{32}
\]
确实，替换有限项的误差至少为
\(s(p-1)-\lfloor\log_pR\rfloor\ge B_p(R)\)，这解释了
(31) 比 (18) 多出的一阶。因而
\[
\Sha(E_{17}/\mathbb Q)[p^\infty]\text{有限}
\iff\exists R\ge1:\ v_p(\widehat S_{p,R})<B_p(R).
\tag{33}
\]
在 \(1\le R\le p-2\) 时可取 \(s=1\)，误差至少为 \(p^{R+1}\)，
最高导数仅为 \(R(p-1)+4\)。此外 (26) 给出一个统一的邻项约束：
对每个 \(j\ge1\)，
\[
p\nmid a_{\,j(p-1)/4+1}.
\tag{34}
\]

(30)–(34) 把后续全局问题缩到同一序列，仍未证明无穷多个 \(p\) 的
非消失。也不能把上一参考比值 \(a_r/(17T_r)\) 在 principal 权上的
单位分母推广到所有权：例如整递推直接给
\(a_{14}/(17T_{14})\) 在 \(p=97\) 的赋值为 \(-1\)。
本附录没有把任何这样的非 principal 比值当作整 Witt 矩。
