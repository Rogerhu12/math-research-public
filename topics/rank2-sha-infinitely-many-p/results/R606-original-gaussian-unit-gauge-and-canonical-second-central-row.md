# R606 — 原 Gaussian 的整单位变换与无提升参数的第二中央行

日期：2026-11-14。**状态：已证明。**

本篇保原 $S_{34},T_{72}$ 的完整 Newton 函数。
先证明：把原 Gaussian 系数改变一个整数，会把 Newton 函数乘上一个
显示的解析单位；因原常数项为零，**完整中央导数准确不变**。
由此可用一个显式二项式系数代替高度二反演中的提升量。

在同一 $u,t$ 参数中，这给一个完全在特征 $p$ 有限环内定义的共同级数。
两条原第二中央行都可从它读取，不再含任意提升参数。
原留数的 $H^{-p}$ 还贡献一条必须保留的 log 修正。
这些是原完整同时失败的更准确必要条件，尚未证明它们矛盾。

## 1. 原对象和一个准确的整数差

固定
$$
p=6s-1>71,\quad d=p+1=6s,\quad w=z^6,
$$
先在原共同 $E_1:y^2=x^3+1$ frame 中工作。
记 R301 的
$$
W(w)=1+\sum X_nw^n,\qquad
F=\log(\sigma/z),\qquad c=[w^s]F
=-\frac{X_s}{p(p+1)}.
\tag{1}
$$
R591/R595 的同一个参数为
$$
u=x^{-1/2},\quad t=u^6,\quad z=uH(t),\quad dz=C(t)\,du,
$$
$$
C(t)=(1+t)^{-1/2}=\sum C_nt^n,\qquad
H(t)=\sum\frac{C_n}{6n+1}t^n,\qquad
J(t)=\sum\frac{C_n}{1-6n}t^n,
$$
$$
K(t)=(\sigma(z(u))/u)^6,\qquad
\theta\log K=JC-1,\quad\theta=t\partial_t.
\tag{2}
$$
原绝对高斯单位和 Lagrange 反演给
$$
C_s=(-1)^s4^{-s}\binom{2s}{s}\in\mathcal O^\times,\qquad
X_s\equiv C_s\pmod p .
\tag{3}
$$
因此以下是一个真实整数，而非自由来源系数：
$$
\chi=\frac{X_s-C_s}{p}\in\mathcal O.
$$
定义显式的规范系数
$$
\boxed{
c^\dagger=-\frac{C_s}{p(p+1)},\qquad
c^\dagger-c=\frac{\chi}{p+1}\in\mathcal O,\qquad
\frac c{c^\dagger}=\frac{X_s}{C_s}\in1+p\mathcal O.
}
\tag{4}
$$
$c^\dagger$ 不被误称为原 $F$ 的系数；它和原 $c$ 的全部区别由 (4) 保留。

## 2. 整 Gaussian 改变如何作用于完整原 Newton 函数

先证明一般事实。设 $A(0)=0$ 是当前原来源，
原 charge 为 $m=34$ 或 $72$，原
$$
G=Ae^{-mcw^s},\quad
J_m(v)=\sum_{h\ge1}[w^{hs}]G\,(mc)^{-h}(v)_h .
$$
对任意 $c'=c+\eta$、$\eta\in\mathcal O$，令
$$
G'=Ae^{-mc'w^s}=G\,e^{-m\eta w^s},\qquad
J_m^{c'}(v)=\sum_{h\ge1}[w^{hs}]G'\,(mc')^{-h}(v)_h.
\tag{5}
$$
这里 $v_p(c')=-1$，$c/c'\in1+p\mathcal O$。

R602 的 Hurwitz 代数闭性保证 $e^{-m\eta w^s}$ 及实际规范化 $G'$
仍有同一 $n!$ 整性。
在每个闭 $R<R_*=p^{-1/[6(p-1)]}$ 的盘上，
该指数及其逆都是实际解析单位：其指数首阶是 $d=p+1$，
且 $d/[6(p-1)]=s/(p-1)>1/(p-1)$。
因此原完整尾及 Newton 解析性继续成立，不是一个只有形式意义的换元。

对每个非负整数 $k$，准确有限 Gaussian 卷积给
$$
J_m^{c'}(k)=k!(mc')^{-k}[w^{ks}]A
=\left(\frac c{c'}\right)^kJ_m(k).
\tag{6}
$$
两边在 $\mathbf Z_p$ 的一个邻域解析；
$(c/c')^v=\exp(v\log(c/c'))$ 使用 $1+p\mathcal O$ 中的唯一 log。
在 $k=p^n\to0$ 的无穷点上应用 (6)，解析恒等定理给
$$
\boxed{
J_m^{c'}(v)=\left(\frac c{c'}\right)^vJ_m(v).
}
\tag{7}
$$
这保留了完整所有 Newton 项；没有把不同 Gaussian 的系数逐项等同。

因 $J_m(0)=0$，立刻得到
$$
\boxed{
(J_m^{c'})'(0)=J_m'(0),\qquad
\operatorname{ord}_0J_m^{c'}=\operatorname{ord}_0J_m .
}
\tag{8}
$$
首个非零 Taylor 系数也准确相同。
若来源常数项非零，则导数会增加
$\log(c/c')J_m(0)$；所以 (8) 不被套到原质量一参考上。

对 (4)，两条原来源还使用同一个单位因子：
$$
\boxed{
J_m^\dagger(v)=\left(\frac{X_s}{C_s}\right)^vJ_m(v),
\qquad j_m:=(J_m^\dagger)'(0)=J_m'(0).
}
\tag{9}
$$
原通常 Selmer 比较因而仍使用同一个完整 $j_m$。
这是已经支付的整单位变换，不是新增一个算术零输入。

## 3. 原 t 参数中的规范余项

取原两个固定分子
$$
P_{34}=P_S=\frac{(1+t)(1-8t)(7-4t+16t^2)}7,
$$
$$
P_{72}=P_T=P_S(1+4t)(1-96t+48t^2+64t^3)(1+20t-8t^2).
\tag{10}
$$
R595 的准确原身份是
$$
A_m=u^6K^{m/6}P_m .
\tag{11}
$$
定义同一个规范 sigma 余项
$$
\boxed{
\Lambda^\dagger(t)
=K(t)\exp\{-6c^\dagger t^sH(t)^{p+1}\}.
}
\tag{12}
$$
因为 $z^{p+1}=t^sH^{p+1}$，
$$
A_m e^{-mc^\dagger z^{p+1}}
=u^6(\Lambda^\dagger)^{m/6}P_m.
\tag{13}
$$
所有幂在特征零按原 sigma 定义，有限约化使用常数一的整二项式式。

先付所需完整窗口的整性。
$C_n$ 对 $n<p$ 全整。
$H_n=C_n/(6n+1)$ 在该窗口唯一可能有 $p$ 分母的指标是
$n=5s-1=(5p-1)/6$。
该处 $p/2<n<p$、$p<2n<2p$，所以 $\binom{2n}{n}$ 恰有一次 $p$ 进位，
抵消 $6n+1=5p$ 的一次分母。
故
$$
H\bmod t^p\in\mathcal O[t]/t^p,\qquad H(0)=1.
\tag{14}
$$
R602 给 $F-cw^s$ 的全部 $w^{<p}$ 系数整。
用整代换 $w=tH^6$，再乘 $H^6$ 及 (4) 的整 Gaussian 修正，
得到
$$
\boxed{\Lambda^\dagger\bmod t^p\in\mathcal O[t]/t^p.}
\tag{15}
$$
没有把原未去 Gaussian 的 $K_s$ 视为整。

## 4. 完全显式的特征 p 连接

在 $\mathcal O[t]/t^p$ 中置
$$
J^\flat(t)=
\sum_{\substack{0\le n<p\\n\ne s}}\frac{C_n}{1-6n}t^n.
\tag{16}
$$
这些分母均为单位；原唯一坏项是 $J_s=-C_s/p$。

由 $H+6tH'=C$，
$$
\theta(t^sH^{p+1})=s\,t^sH^pC.
$$
因此 (2)、(4)、(12) 给准确的有限窗口恒等式
$$
\boxed{
\theta\log\Lambda^\dagger
=J^\flat C-1+
C_st^sC\,\frac{H^p-1}{p}
\pmod{t^p}.
}
\tag{17}
$$
右边最后的除 $p$ 只需到次数 $p-s-1$。
在此窗口，$H$ 整且常数一，故它确实整。

还须保这个除法的剩余值。令 $H=1+h$。对 $1\le k<p$，
$$
\frac1p\binom pk\equiv\frac{(-1)^{k-1}}k\pmod p.
$$
$h^p$ 的次数至少 $p$，不进入所读窗口。
所以准确有
$$
\boxed{\frac{H^p-1}{p}\equiv\log\bar H\pmod{p,t^{p-s}}.}
\tag{18}
$$
这里的 log 是有限整 log，不是在特征 $p$ 中取一个无限级数。

在 $k[t]/t^p$ 定义
$$
\boxed{
\mathcal R_p(t)=
\bar J^\flat\bar C-1+\bar C_s t^s\bar C\log\bar H.
}
\tag{19}
$$
它的常数项为零。因 $1,\ldots,p-1$ 在 $k$ 中可逆，
$\theta$ 在 $tk[t]/t^p$ 上可逆；定义
$$
\boxed{
\mathcal K_p=
\exp\bigl(\theta^{-1}\mathcal R_p\bigr)\in1+tk[t]/t^p.
}
\tag{20}
$$
exp/log 都只取到 $t^{p-1}$，所需阶乘均为单位。
(17)–(18) 和常数项一准确给
$$
\boxed{\overline{\Lambda^\dagger}=\mathcal K_p\quad\bmod t^p.}
\tag{21}
$$

(19)–(20) 只使用原显式 $C,H,J^\flat$ 和 $\bar C_s$。
它不含 $X_s$ 的下一位，也不含一个可自由选择的 $\chi$。
不过其中 $p,s$ 和截断仍随 $p$ 变化；
不能把它当成固定 CM 多项式而套用稀疏坏集引理。

## 5. 同一个原中央的前五个规范余项

记
$$
g^\dagger_{m,h}
=[w^{hs}]\bigl(A_m e^{-mc^\dagger w^s}\bigr).
$$
完整留数换元保 Jacobian 后给
$$
g^\dagger_{m,h}
=[t^{hs-1}](\Lambda^\dagger)^{m/6}
 P_m C H^{-h(p+1)-1}.
\tag{22}
$$
这与 R595 的首行是同一形式留数，不增添投影后的来源列。

当 $1\le h\le5$ 时 $hs-1<p$。
(14) 给 $\bar H^p=1\bmod t^p$，
所以 (21)–(22) 得到全部五行的显式剩余值
$$
\boxed{
B_{m,h}:=\overline{g^\dagger_{m,h}}
=[t^{hs-1}]\mathcal K_p^{m/6}P_m\bar C\,\bar H^{-h-1},
\qquad 1\le h\le5.
}
\tag{23}
$$
每个 $g^\dagger_{m,h}$ 的整性由 R602 和 §2 保证。
尤其
$$
B_{m,1}=\overline{A_{m,1}},\qquad
A_{m,1}=[w^s]A_m,
\tag{24}
$$
仍是两条原首对角，不是新的独立条件。

$h=6$ 需要规范化系数指标 $p$，
已经不在 (21) 的窗口，不能直接外推 (23)。

为显示原提升参数如何被完整消去，
原余项与规范余项的准确关系是
$$
g_{m,h}
=\sum_{j=0}^{h-1}\frac1{j!}
 \left(\frac{m\chi}{p+1}\right)^j g^\dagger_{m,h-j}.
\tag{25}
$$
对 $1\le h\le5$，可约化为
$$
\boxed{
\bar g_{m,h}=
\sum_{j=0}^{h-1}\frac{(m\bar\chi)^j}{j!}B_{m,h-j}.
}
\tag{26}
$$
例如 $\bar g_{m,2}=B_{m,2}+m\bar\chi B_{m,1}$。
当原首对角为零时，第二行的 $\chi$ 贡献准确消失。
更强的是 (9)：在完整 Newton 导数中，该变化在所有精度相消，
而非只在某个有限 Taylor 项中省略。

## 6. 原第二中央类及必须保留的 H 的 log 项

设原首层失败
$$
A_{m,1}\in p\mathcal O.
$$
置
$$
\gamma^\dagger_m=pmc^\dagger=-\frac{mC_s}{p+1},
\qquad\bar\gamma^\dagger_m=-m\bar C_s.
$$
R602 的完整 $p^3$ 尾应用于 §2 的规范余项，再用 (9)、(23)，准确有
$$
\boxed{
\frac{j_m}{p^2}\equiv
(\bar\gamma^\dagger_m)^{-1}\overline{A_{m,1}/p}
-(\bar\gamma^\dagger_m)^{-2}B_{m,2}\pmod p.
}
\tag{27}
$$
所以定义原实际第二类
$$
\boxed{
\Xi_{m,p}=B_{m,2}
+m\bar C_s\,\overline{A_{m,1}/p},
\qquad
\frac{j_m}{p^2}\equiv
-\frac{\Xi_{m,p}}{m^2\bar C_s^2}\pmod p.
}
\tag{28}
$$
若 $\Xi_{m,p}\ne0$，则原完整 $j_m$ 恰有赋值二；
原完整通常 Selmer 桥因此给对应固定曲线的初级有限。

还可将 (28) 的一次商完整写在 R595 的同一低窗口。
令 $N=s-1$，
$$
\mathcal A_m=[t^N]K^{m/6}P_m\,C/H^2\in\mathcal O,
$$
$$
\mathcal L_m=[t^N]\bar K^{m/6}P_m\bar C\,\bar H^{-2}
                 \log\bar H\in k.
\tag{29}
$$
此处 $K$ 只需 $t^{<s}$，全部分母为单位，因而
$\mathcal A_m$ 可以按原固定递推保留两位精度。

原准确留数为
$$
A_{m,1}=[t^N]K^{m/6}P_m C H^{-p-2}.
$$
在这个 $N<p$ 的整窗口，
$H^{-p}\equiv1-p\log H\bmod p^2$，所以
$$
\boxed{
A_{m,1}\equiv\mathcal A_m-p\mathcal L_m\pmod{p^2}.
}
\tag{30}
$$
右边的 $p\mathcal L_m$ 用任意整提升，模 $p^2$ 与提升无关。

若 $\bar A_{m,1}=0$，则 $\mathcal A_m\in p\mathcal O$，
故
$$
\boxed{
\overline{A_{m,1}/p}
=\overline{\mathcal A_m/p}-\mathcal L_m,
}
$$
$$
\boxed{
\Xi_{m,p}=
B_{m,2}+m\bar C_s
 \left(\overline{\mathcal A_m/p}-\mathcal L_m\right).
}
\tag{31}
$$
$\mathcal L_m$ 正是原 $H^{-p}$ 的完整第一 Frobenius 修正，
不能因首层曾有 $\bar H^p=1$ 而在第二层删掉。
$\mathcal A_m/p$ 仍是实际低系数的整除商，不是自由变量。

## 7. 两原曲线同时失败的准确必要条件

由 (24)、(28)，原完整两中央同时零必定满足
$$
\boxed{
B_{34,1}=B_{72,1}=0,\qquad
\Xi_{34,p}=\Xi_{72,p}=0.
}
\tag{32}
$$
前两条与 R595/R596 原首对角条件相同，
因此保其全部共同 pole 重建、低残差与非齐次单位目标。
后两条现在由 (19)–(23)、(29)–(31) 在同一来源中明确支付；
不再留一个可供独立调整的高度二提升参数。

本篇尚未证明 (32) 在原递推下不可能，
也没有从两个首对角零推两辅助 $c_4,c_1$ 零。
原首对角有非零时已经由 R303/R402 给有限性；
只有首层同时失败时，(31) 才用于下一真实判据。

还原一般共同 $b$ frame 时，
$A_{m,h,b}=b^{hs-1}A_{m,h,1}$、
$c_b=b^sc_1$，
所以完整 $j_{m,b}=b^{-1}j_{m,1}$；
原物理整体单位继续按 R303/R402 保留。
因此上述零/非零判据没有改换固定曲线或普通地点。

## 依赖

- [R301](R301-jzero-inert-analytic-half-factor-and-exact-first-denominator.md)：
  原 $c=-X_s/[p(p+1)]$ 与 $X_s\equiv C_s$。
- [R591](R591-original-inert-forcing-in-one-parameter-and-exact-resonance.md)、
  [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)：
  同一个 $K,H,C,J$、完整原分子和准确留数 Jacobian。
- [R602](R602-original-gaussian-hurwitz-integrality-and-next-central-bockstein.md)：
  全 Hurwitz 整性、严格完整 Newton 尾与原第二层。
- [R303](R303-jzero-inert-full-selmer-period-comparison-and-central-criterion.md)、
  [R402](R402-e24-inert-analytic-half-factor-full-selmer-and-joint-carry.md)：
  原整数权插值、完整物理缩放及通常 Selmer 比较。
- [R596](R596-original-pole-reconstruction-and-full-prefix-central-constraints.md)：
  首层同时失败的实际非齐次约束，不由本篇省略。

本篇是完整有限系数与解析单位证明，没有新增素数扫描。
