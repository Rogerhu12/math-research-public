# R691 — 原轨道单位、真实不分歧 Kummer 域及边界和的迹判据

日期：2026-11-15。**状态：已证明。** 主目标仍未完成。

R688 的原 $p$ 次根并非可以自由指定的形式根。本篇证明它们来自
原全除点域的一个处处不分歧、在 $p$ 完全分裂的初等 $p$ 扩张。
全部根的相等字符类由同一个明确稳定子决定；原完整边界和为零，
准确等价于该稳定子上的一条原迹为零。

若这个稳定子恰为原六次自同构群，则原两个边界和都非零。
本篇不预先断言稳定子最小，也不把边界非零直接当作原中央非零。

后续 [R694](R694-original-cm-kummer-descent-and-full-norm-one-trace.md)
已确定本题实际稳定子为整个 H，原 M_T=F；因此下文 J=μ6 的条件命题
在本题 p>101 中不适用。这里的单位性、Kummer/迹身份和条件证明仍保留。

## 1. 原域、原单位根分支及准确 cocycle

沿 R688 固定
$$
p=6s-1>101,\quad d=p+1,\quad q=p^2,\quad
K_0=\mathbf Q(\omega),\quad F=K_0(E[p]),\quad E:y^2=x^3+17.
$$
同一嵌入 $\overline{\mathbf Q}\hookrightarrow\mathbf C_p$ 下，
R688 已付
$$
\operatorname{Gal}(F/K_0)=\mathbf F_q^\times,\qquad
F_{\mathfrak p}=L=K_p(v_T),\qquad v_T^{q-1}=p,
$$
且 $\mathfrak p$ 为唯一 $p$ 位，$\mu_p\subset F$。
置
$$
H=\ker(\operatorname{Norm}_{\mathbf F_q/\mathbf F_p}),\qquad
|H|=d,\quad F^H=K_0(\mu_p).
$$
$h\in H$ 在局部形式群上的 Teichmüller 作用记作 $\zeta_h\in\mu_d$。
这里 $\zeta_h\in K_p$，**不**据此声称 $\zeta_h\in F$。

保原
$$
\alpha=\omega^2+p\omega,\quad n=p+1,\quad
a_T=\psi_\alpha(T)^{2s}/\psi_n(T)^{2s-1}\in F^\times.
$$
原 R688 的实际根为
$$
r_{h,T}=\zeta_hP_{\zeta_h}(u_T)\in L\cap\overline{\mathbf Q},
\qquad
\boxed{r_{h,T}^{\,p}=a_T/a_{hT}.}
\tag{1}
$$
所有根仍由原有限 $u^d$ jet 按距离 $>1/(p-1)$ 选定，未重新选相位。

原正式比值满足
$P_{\zeta\eta}(u)=P_\zeta(u)P_\eta([\zeta]u)$。
两边都是原整收敛函数，故在同一个挠点准确给
$$
\boxed{r_{hk,T}=r_{h,T}r_{k,hT},\qquad
r_{1,T}=1.}
\tag{2}
$$
局部 $H$ 作用固定所有 $\zeta_k\in K_p$，且对原级数等变，故
$$
h(r_{k,T})=r_{k,hT}.
\tag{3}
$$
式 (2)–(3) 保完整原根，不能只从其 $p$ 次幂反推而遗漏 $\mu_p$ 因子。

## 2. 原相对除点值在每一个有限位都是单位

**引理 1。** 对所有非零 $T\in E[p]$、$h\in H$，
$$
\boxed{a_T/a_{hT}\in\mathcal O_F^\times.}
\tag{4}
$$

先证明所有有限位都可使用的潜好模型，不跳过 $2,3,17$。
在任意剩余特征 $\ell\ne2,3$，有限扩张中取 $c^6=17$，
则 $x=c^2X,y=c^3Y$ 将原曲线送到
$Y^2=X^3+1$，其判别式为 $-432$，在该位为单位。
在 $\ell=2$，取 $c^6=68$，使用
$$
x=c^2X,\qquad y=c^3(Y+1/2).
$$
新模型 $Y^2+Y=X^3$ 的判别式为 $-27$，亦为单位。
在 $\ell=3$，取 $r^3=-17,u^4=3r^2$，使用
$$
x=r+u^2X,\qquad y=u^3Y.
$$
新模型是
$$
Y^2=X^3+(3r/u^2)X^2+X,\qquad
(3r/u^2)^2=3,\qquad\Delta=-16.
$$
系数整、判别式为单位。因此所有位在一个有限扩张后都有光滑、
proper、几何连通特纤维的椭圆模型。

现取 $v\nmid p$，作上述有限潜好扩张，再作必要有限扩张使全部
相关截面及 CM 定义。由于 $p$ 在基环中可逆，$\mathcal E[p]$
有限 étale；非零 $p$ 挠点的约化仍非零。
原等式
$$
[\alpha]T=[\omega^2]T,\qquad [n]T=T
\tag{5}
$$
及 $hT$ 的同样等式在好模型上继续成立。
因此 $T,hT$ 两截面同时避开
$[O]$、$[\alpha]^*[O]$、$[n]^*[O]$ 的支撑。

这里不要求 $\ell\nmid\deg\alpha$ 或 $\ell\nmid n$。
即使特纤维上相应同态不可分，(5) 仍直接保证不落入其核。
原 CM 同态及整数同态在好椭圆模型上的延拓与群运算相容。

原除点函数的 generic 除子是
$$
\operatorname{div}(\psi_\alpha)=[\alpha]^*[O]-(\deg\alpha)[O],
\qquad
\operatorname{div}(\psi_n)=[n]^*[O]-n^2[O].
$$
在上述光滑 proper 模型上，减掉这些水平零极后，只能剩下
整条特纤维的整数倍：特纤维几何不可约，没有可分别赋值的其它分量。
于是 $\psi_\alpha(T)$ 与 $\psi_\alpha(hT)$ 的 valuation 相同；
$\psi_n$ 亦然。其相除消去全部垂直常数。
有限扩张只将 valuation 乘一个正分歧指数，故零 valuation 可下降，
从而 (4) 在所有 $v\nmid p$ 成立。

在唯一 $\mathfrak p\mid p$，原 $P_{\zeta_h}(u_T)\in1+\mathfrak m_L$，
$\zeta_h$ 为单位；所以 (1) 直接给
$v_{\mathfrak p}(a_T/a_{hT})=p\,v_{\mathfrak p}(r_{h,T})=0$。
这证明 (4)，并保原坏位的全部贡献。

## 3. 实际 Kummer 域是 Hilbert p 类域的商

定义
$$
\boxed{M_T=F(r_{h,T}:h\in H).}
\tag{6}
$$
因为 (1) 的系数在 F 且 $\mu_p\subset F$，
$M_T/F$ 为有限 Galois 初等 $p$ 扩张。
它的根是原实际根；由于所有 $p$ 次单位根已在 F，
改写为多项式分裂域并不改变 (6) 的域。

在 $v\nmid p$，(4) 的单位在最大不分歧局部扩张中有 $p$ 次根：
先在代数闭剩余域取根，再由导数 $pX^{p-1}$ 为单位作 Hensel 提升。
故 $M_T/F$ 在该位不分歧。
在 $\mathfrak p$，所有原 $r_{h,T}$ 已属于准确完成域
$L=F_{\mathfrak p}$，所以该位完全分裂，而非只不分歧。
F 全虚，没有实位问题。于是
$$
\boxed{M_T/F\text{ 处处不分歧，且 }\mathfrak p\text{ 完全分裂}.}
\tag{7}
$$

令
$$
D_T=\left\langle[a_T/a_{hT}]:h\in H\right\rangle_{\mathbf F_p}
\subset F^\times/F^{\times p},\qquad r_T=\dim_{\mathbf F_p}D_T.
$$
准确 Kummer 配对与 Hilbert 类域定理给
$$
\boxed{\operatorname{Gal}(M_T/F)\simeq
\operatorname{Hom}(D_T,\mu_p),\quad
[M_T:F]=p^{r_T},\quad
\operatorname{Gal}(M_T/F)\text{ 是 }\operatorname{Cl}(F)/p\operatorname{Cl}(F)
\text{ 的商}.}
\tag{8}
$$
$\mathfrak p$ 在这个商中为零也可直接看出：
$(p)=\mathfrak p^{q-1}$，且 $(p,q-1)=1$。
因此不要把已知的 $p$ 分裂再当成一个新的独立类群限制。

式 (2)–(3) 还说明 H 的局部自同构保持 $M_T$。
其在 $M_T$ 上的限制是 (8) 的真实分解群补，给
$$
\operatorname{Gal}(M_T/F^H)
=\operatorname{Gal}(M_T/F)\rtimes H.
\tag{9}
$$
这里只断言一个 H 轨道的 M；全 G 作用可能将它送到另一个 $M_{gT}$，
不能把一个轨道的次数界直接给全轨道合成域。

## 4. 六次自同构与实际类的稳定子

原 $h=\sigma/z$ 在 $\mu_6$ 下不变。对 $\epsilon\in\mu_6\subset H$，
$$
P_\epsilon=1,\qquad
r_{\epsilon,T}=\epsilon,\qquad
a_{\epsilon T}=\epsilon a_T.
\tag{10}
$$
最后一个式子也准确由 (1) 和 $\epsilon^p=\epsilon^{-1}$ 得到。
$\epsilon$ 是 F 中的 $p$ 次幂，所以 $\mu_6$ 固定 $[a_T]$。

定义真正的稳定子
$$
\boxed{
J=\{h\in H:[a_{hT}]=[a_T]\text{ in }F^\times/F^{\times p}\}.
}
\tag{11}
$$
这是 H 对一个实际向量的稳定子，故为子群，且
$$
\mu_6\subset J\subset H.
\tag{12}
$$
由于 $\operatorname{Gal}(F/K_0)$ 交换并在非零 $p$ 挠点上传递，
(11) 不依非零 T 的选择。这里只是同一实际稳定子，未指定它的大小。

两个原根所对应的 Kummer 字符相同，准确等价于
$$
\boxed{
[a_T/a_{hT}]=[a_T/a_{kT}]
\iff hJ=kJ.
}
\tag{13}
$$
不同 coset 的根不必构成乘法独立族；下面只用它们的字符不同。

此外 $D_T$ 是 H 的 augmentation 作用在 $[a_T]$ 上的循环像。
H 的作用在此循环源上经 $H/\mu_6$（阶 s）分解。
其 augmentation 理想维数 $s-1$，故
$$
\boxed{r_T\le s-1,\qquad [M_T:F]\le p^{s-1}.}
\tag{14}
$$
这也可由一个循环生成元 $\tau$ 的
$1+\tau+\cdots+\tau^{s-1}$ 关系直接得到。
没有把 $\operatorname{Cl}(F)[p]$ 的维数假定为零或有界。

## 5. 完整原边界和的按类分组

原 $m=34,72$ 的全部和保持 R688：
$$
\mathscr S_{m,T}
=\sum_{h\in H}r_{h,T}^{\,m}\phi_m(hT),
\qquad
\mathcal B_m(v_T^d)=0\iff\mathscr S_{m,T}=0.
\tag{15}
$$
其中 $\phi_m\in K_0(E)$ 是同一固定原函数，只有 O 极点，极阶 $m-6$。
原 CM 角型准确给
$$
\phi_m(\epsilon P)=\epsilon^{-m}\phi_m(P)
\qquad(\epsilon\in\mu_6).
\tag{16}
$$

对 $j\in J$，(1)、(11) 及 $\mu_p\subset F$ 说明原 $r_{j,T}\in F$：
只要一个 $p$ 次根在 F，全部根就在 F，故原有限 jet 分支也在 F。
定义完整同类块
$$
\boxed{C_{J,m,T}=\sum_{j\in J}r_{j,T}^{\,m}\phi_m(jT)\in F.}
\tag{17}
$$
由 (2)–(3)，任取 $H/J$ 的代表集即可准确写
$$
\boxed{
\mathscr S_{m,T}
=\sum_{h\in H/J}r_{h,T}^{\,m}\,h(C_{J,m,T}).
}
\tag{18}
$$
式子保全部 $d$ 项，只按相同 Kummer 字符重排。

$\operatorname{Gal}(M_T/F)$ 作用在不同
$r_{h,T}^{\,m}$ 上的字符互异：由 (13) 区分 coset，
且 $p\nmid m$，取 m 次方不合并字符。
不同字符的特征向量在 F 上线性独立。
例如可用有限群字符投影
$|A|^{-1}\sum_{\sigma\in A}\chi(\sigma)^{-1}\sigma$
逐项分离；F 的特征为零，$\mu_p\subset F$，故投影合法。
从 (18) 得到准确充要式
$$
\boxed{
\mathcal B_m(v_T^d)=0
\iff\mathscr S_{m,T}=0
\iff C_{J,m,T}=0.
}
\tag{19}
$$
这一步只使用已确定的实际类，没有擅自令全部根独立。

## 6. 同类块进一步成为一个明确的原迹

由 (2)–(3)，$j\mapsto r_{j,T}$ 是 J 在 $F^\times$ 中的原 cocycle。
取 $c\in F$ 使
$$
b_T=\sum_{j\in J}r_{j,T}\,j(c)\ne0.
\tag{20}
$$
这样的 c 存在：不同域自同构的线性独立性排除这个线性算子恒零。
对 $k\in J$，(2) 给
$k(b_T)=r_{k,T}^{-1}b_T$，故
$$
r_{j,T}=b_T/j(b_T).
\tag{21}
$$
这是保全部原根的 Hilbert 90 构造；没有重新选一个 cocycle。

代入 (17)，
$$
\boxed{
C_{J,m,T}
=b_T^m\operatorname{Tr}_{F/F^J}
       \bigl(b_T^{-m}\phi_m(T)\bigr).
}
\tag{22}
$$
任意另一个有效 $b_T$ 只差 $F^{J,\times}$ 的倍数，迹为零的条件不变。
还准确有 $b_T^p/a_T\in F^J$，但这不允许换掉原 (21) 的分支。
最终：
$$
\boxed{
\mathcal B_m(v_T^d)=0
\iff
\operatorname{Tr}_{F/F^J}
       \bigl(b_T^{-m}\phi_m(T)\bigr)=0.
}
\tag{23}
$$
(11)、(20)、(21) 完整指定了 (23) 的实际输入。

## 7. 最小稳定子给出真正边界非零的充分条件

先证明 $\phi_m(T)\ne0$。若某个非零 p 挠点是其零点，
原全局群 $\mathbf F_q^\times$ 的传递性会使全部 $q-1$ 个非零
p 挠点都是零点。它们不同，且 $\phi_m$ 是定义在 $K_0$ 上的非零
有理函数，其零除子总度为 $m-6<q-1$，矛盾。因此
$$
\boxed{\phi_m(T)\ne0\quad(m=34,72).}
\tag{24}
$$

若 $J=\mu_6$，(10)、(16) 给每一个同类项
$r_{\epsilon,T}^m\phi_m(\epsilon T)=\phi_m(T)$，故
$$
C_{J,m,T}=6\phi_m(T)\ne0.
$$
由 (19)，得到
$$
\boxed{
J=\mu_6\quad\Longrightarrow\quad
\mathcal B_{34}(v_T^d)\ne0,\quad
\mathcal B_{72}(v_T^d)\ne0
\quad\text{对全部非零 }T.
}
\tag{25}
$$
反之，任一原边界为零都迫 $J\supsetneqq\mu_6$，
且仍须满足 (23) 的准确迹零条件。
本篇未证明这些稳定子或迹在无穷 p 上具有指定行为。

还需防止反向误用类数：若 $p\nmid\#\operatorname{Cl}(F)$，
(8) 反而给 $M_T=F$、$J=H$。
这只把问题化为整个 H 的迹；它不自动给 (25) 的最小稳定子情形，
也不自动令该迹非零。

## 8. 与原中央条件之间仍保的接口

原首边界零的完整无限尾已经在 (15)、(19)、(23) 中准确保留。
对每个 H 轨道使用这些等式，即为 R663 的全部首 Q 余数判定；
没有改换原 $T_g$、$\phi_m$ 或有限 jet 的根。

本篇新付的是全坏位单位性、实际不分歧域及其类群商、
真实稳定子分组、原迹的充要判据和 (25)。
原中央 $j_m=0$ 尚未被证明迫使这些边界余数为零。
原 X 闭盘下降还须 R663 的更高 $Q^{d-m}$ 条件；
不能用 (25) 越过这一接口，亦不能据有限 p 的类数计算完成无穷性。

后续直接研究 (11) 的原 $p$ 次幂稳定子、(23) 的指定迹，
或原中央到这些完整余数的传播，不引入自由根或免费全局列。

## 依赖和标准定理

- [R688](R688-full-division-field-phase-cancellation-and-original-kummer-sums.md)：
  原完整全局除点域、准确 $p$ 次根及同一个完整 Kummer 和。
- [R681](R681-original-torsion-gauge-and-finite-algebraic-residues.md)、
  [R663](R663-original-lubin-tate-residues-and-closed-boundary-equivalence.md)：
  原整解析分支、固定 $\phi_m$、完整余数和中央/闭盘接口。
- J. S. Milne, *Class Field Theory*, v4.03，
  Chapter VII, Appendix A, Theorem A.3（Kummer 配对）；
  Chapter V, Example 3.9（Hilbert 类域），
  [作者官方正文](https://www.jmilne.org/math/CourseNotes/CFT.pdf)。
- K. S. Kedlaya, *Notes on class field theory*, Theorem 2.1.3，
  [作者官方正文](https://kskedlaya.org/cft/sec_hilbert.html)。
  本文用其 Hilbert 类域与理想类群的对应；所有坏位、
  实际 cocycle、分组及原迹公式已在正文逐项证明。

本篇没有新增数值检查或可重算数据文件。
