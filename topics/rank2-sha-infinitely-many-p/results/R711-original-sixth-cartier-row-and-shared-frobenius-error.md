# R711 — 原第六 Cartier 行、首个 Frobenius 误差与两来源的准确消去

日期：2026-11-15。**状态：原第六块的完整 Cartier 有限部、实际首 Frobenius 修正及其两来源消去已证明。未证明原中央非零，也未把实际低部分和的除商删除。**

R647 的共同有理模型准确支付前五个原块；第六块正好落在该模型首个未付系数上。本篇保持同一个 \(P_2,\Theta_p,Z,G\)，把那一个实际误差明确保留，再在原不同 \(m\) 之间消去它。第六 Cartier 输入出现原点简单极，必须先处理这个极，不能沿用前五块的“输入正则”。

## 1. 同一个原来源与第六块的精度

取
\[
p=6s-1>101,\qquad b=17,\qquad d=p+1,\qquad
m\in\{34,72\}.
\]
若纳入第三个原 \(m=136\)，另取 \(p>136\)。
所有约化都在同一 \(k=\mathcal O/p\mathcal O\) 内。
令
\[
\sigma^\circ(z)=\sigma(z)e^{-c z^d},\qquad
c=[z^d]\log(\sigma/z),\qquad
\mathscr G_m(z)=(\sigma^\circ(z))^m\phi_m(P_z),
\]
\[
g_{m,h}=[z^{dh}]\mathscr G_m(z).
\tag{1}
\]
完整 \(\phi_m\) 分别为 R647 的原 \(x^2F_4(x^3)\)、
\(x^3F_{10}(x^3)\)、\(x^2F_{21}(x^3)\)；
极阶为 \(m-6\)，首 Laurent 系数一。
所以 \(\mathscr G_m=z^6+\cdots\)。

保持 R647 的原有理对象
\[
DZ=1,\quad DG=-x+c_pZ^{p-1},\quad
c_p=\binom{3s-1}{2s-1}b^s\in k^\times,
\]
\[
\nabla_2=D-2G,\qquad
P_2=-\nabla_2^{p-1}Z^{p+1},\qquad
\widehat A_m=P_2^{m/2}\phi_m.
\tag{2}
\]
它们没有被换成另一个有理近似。
R647 给
\[
P_2\equiv(\sigma^\circ)^2\pmod{z^{6p+2}},\qquad
Z=z-\kappa_5z^{5p}+\cdots,\qquad
\kappa_5=\frac{(3b/5)^p}{c_p}\ne0.
\tag{3}
\]

R614 的原整窗口 \(<p^2-1\) 包含本篇所有实际输入；
特别 \(6p+12<p^2-1\)。
原形式对数坐标和其逆在所需低窗内整，故原有理函数的局部展开与
\((\sigma^\circ)^2\) 的这些系数可在同一参数中约化。
定义唯一的实际误差
\[
\boxed{\;
\eta_p=[z^{6p+2}]
       \left(P_2-(\sigma^\circ)^2\right)\in k.
\;}
\tag{4}
\]
它由原 sigma 和原 \(P_2\) 决定，不是可选择的 lift。
由于两者的 \(\mu_6\) 型为二，
\[
P_2-(\sigma^\circ)^2
 =\eta_p z^{6p+2}+O(z^{6p+8}).
\]
乘上同一完整 \(\phi_m\) 后，
\[
\boxed{\;
\widehat A_m(z)
 =\overline{\mathscr G_m(z)}
  +\frac m2\eta_p z^{6p+6}
  +O(z^{6p+12}).
\;}
\tag{5}
\]
这里只展开一阶误差：原 \(\mathscr G_m\) 的首阶六使所有二次误差远高于目标。
这也说明为何第六块不能直接套 R647 的前五块同余。

## 2. 原 \(z/Z\) 坐标修正的下一个实际影响

在当前整窗口中 \(dZ=dz\)，故 \(D(Z-z)=0\)。
\(Z,z\) 同为 \(\mu_6\) 型一。
因此它们差的非零指数必须同时为 \(p\) 的倍数且同余 \(1\bmod6\)。
因 \(p\equiv-1\bmod6\)，首两个允许指数是 \(5p,11p\)。
(3) 因而可准确加强为
\[
Z=z-\kappa_5z^{5p}+O(z^{11p}),\qquad
\boxed{\;z=Z+\kappa_5Z^{5p}+O(Z^{11p}).\;}
\tag{6}
\]
反演的交叉项在此范围内也不出现；这也可由特征 \(p\) 的
\((Z+\kappa Z^{5p})^p=Z^p+\kappa^pZ^{5p^2}\) 直接检查。

记另一个原实际低系数
\[
\boxed{\;
a_m^{+}=[z^{p+7}]\mathscr G_m(z)
       =[w^{s+1}]\mathscr G_m,\qquad w=z^6.
\;}
\tag{7}
\]
把 (6) 代入 (5)，求 \(Z^{6p+6}\) 系数。
一阶坐标修正只能来自指数
\[
n-1+5p=6p+6,\quad n=p+7=6(s+1),
\]
故其系数为 \((p+7)\kappa_5\overline{a_m^+}
=7\kappa_5\overline{a_m^+}\)。
二次坐标修正至少从 \(10p+4\) 开始，高于目标。
因此
\[
\boxed{\;
[Z^{6(p+1)}]\widehat A_m
 =\overline{g_{m,6}}
   +\frac m2\eta_p
   +7\kappa_5\overline{a_m^+}.
\;}
\tag{8}
\]
原第一块坐标修正为 R647 的 \(6\kappa_5\)；
本篇新出现的是下一个实际低系数 (7)，不能把它也换成常数一。

## 3. 第六 Cartier 行必须取有限部

记 \(\omega_E=dZ\)，\(\mathcal C\) 为原 Cartier 算子。
因为 \(\widehat A_m=Z^6+\cdots\)，
\[
Z^{-7}\widehat A_m\omega_E
 =(Z^{-1}+\text{正则项})\,dZ.
\]
故其 Cartier 输出仍有准确的简单极 \(dZ/Z\)，留数一。
定义
\[
\mathfrak C_{m,6}
 =\frac{\mathcal C(Z^{-7}\widehat A_m\omega_E)}{\omega_E}
   -\frac1Z.
\tag{9}
\]
它在 \(O\) 正则；其余原二挠点和 \(Z\) 的全部零点仍保留。
真正的第六行为
\[
\boxed{\;
\mathcal T^{\rm Cart}_{m,6}
 =\left(\frac{D^5\mathfrak C_{m,6}(O)}{5!}\right)^p
 =\operatorname{Res}_O
       \frac{\widehat A_m\omega_E}{Z^{6(p+1)+1}}.
\;}
\tag{10}
\]
证明直接用局部 Cartier 规则：
\(Z^{np+p-1}dZ\) 的系数经 \(p\) 次根变为输出 \(Z^n dZ\) 的系数。
输出的 \(Z^5\) 项读输入 \(Z^{6p-1}\)，亦即 \(\widehat A_m\) 的
\(Z^{6p+6}\) 项。减掉 \(1/Z\) 后才可在 \(O\) 取五阶导数；
最后的 \(p\) 次方恢复输入的实际系数。

结合 (8)，完整原第六块为
\[
\boxed{\;
\mathcal T^{\rm Cart}_{m,6}
 =\overline{g_{m,6}}
   +\frac m2\eta_p
   +7\kappa_5\overline{a_m^+}.
\;}
\tag{11}
\]
这是原两项误差全部保留的公式，不是一个新的独立中央零。

## 4. 两个原 m 的组合同时消去两个共同 lift 系数

先取任意两个实际来源 \(m,m'\)。
(11) 中 \(\eta_p\) 的系数是 \(m/2\)，故
\[
m'\mathcal T^{\rm Cart}_{m,6}
 -m\mathcal T^{\rm Cart}_{m',6}
 =
m'\overline{g_{m,6}}-m\overline{g_{m',6}}
 +7\kappa_5\left(
       m'\overline{a_m^+}-m\overline{a_{m'}^+}\right).
\tag{12}
\]
这里先在同一实际来源上消去误差，没有假设 \(\eta_p=0\)。

括号中的低行也可以完整落在更短的原窗。
令
\[
U(w)=\frac{\sigma(z)}z e^{-cw^s}
       =\sum_{n\ge0}u_nw^n,\qquad
U_{<s}(w)=\sum_{n=0}^{s-1}u_nw^n,\qquad
X(w)=z^2x(z),
\]
\[
\mathcal P_m(w)
 =X(w)^{(m-6)/2}
   P_m\!\left(\frac{bw}{X(w)^3}\right),
\qquad P_{34}=P_S,\ P_{72}=P_T,\ P_{136}=P_U.
\tag{13}
\]
全部原有限分子均保留；\(\mathcal P_m(0)=1\)。
原 identity 是
\[
\mathscr G_m=w\,U^m\mathcal P_m,\qquad
a_m^+=[w^s](U^m\mathcal P_m).
\]
而
\[
a_m^+=m u_s+[w^s](U_{<s}^m\mathcal P_m).
\tag{14}
\]
所以定义原整残差
\[
\boxed{\;
\mathcal R_{m,m'}^{(6)}
 =[w^s]\left(
 m'U_{<s}^{\,m}\mathcal P_m
 -mU_{<s}^{\,m'}\mathcal P_{m'}\right),
\;}
\tag{15}
\]
准确有
\[
m'a_m^+-ma_{m'}^+=\mathcal R_{m,m'}^{(6)}.
\tag{16}
\]
这是特征零中的实际等式；\(m'mu_s-mm'u_s=0\)。
它只使用 \(U\) 的 \(<s\) 系数与原 \(X\) 的 \(\le s\) 系数。
前者尚未受到首 Gaussian 的改动，因此可直接由原
\(\sigma/z\bmod z^{p+1}\) 取得。所需所有系数均整。
并未把余下的 (15) 也赋为零。

第六块的准确两来源形式因此为
\[
\boxed{\;
m'\mathcal T^{\rm Cart}_{m,6}
 -m\mathcal T^{\rm Cart}_{m',6}
 -7\kappa_5\overline{\mathcal R_{m,m'}^{(6)}}
 =
m'\overline{g_{m,6}}-m\overline{g_{m',6}}.
\;}
\tag{17}
\]
例如对原两来源，系数就是 \(72,34\)。
(17) 同时不含首实际 Frobenius 误差 \(\eta_p\) 和
首 Gaussian 的实际整系数 \(u_s\)，但仍保完整低卷积残差。

## 5. 原完整中央失败的第六必要式

继续 R614/R647 的原
\[
\gamma_m=pmc\in\mathcal O^\times,\qquad
L_{m,H}
 =\sum_{h=1}^{H}(-1)^{h-1}(h-1)!
            (p/\gamma_m)^h g_{m,h}.
\]
若实际 \(j_m=0\)，完整 Newton 尾使
\[
\mathscr B_{m,6}:=p^{-6}L_{m,5}\in\mathcal O,
\qquad L_{m,6}\in p^7\mathcal O.
\]
第六项符号为负，故
\[
\boxed{\;
\overline{g_{m,6}}
 =\frac{\bar\gamma_m^{\,6}}{120}\,
                       \overline{\mathscr B_{m,6}}.
\;}
\tag{18}
\]
其中 \(\mathscr B_{m,6}\) 是原低部分和的真实除商，不是新的自由变量。

将其代回 (11)，得到
\[
\boxed{\;
\mathcal T^{\rm Cart}_{m,6}
 =\frac{\bar\gamma_m^{\,6}}{120}
                         \overline{\mathscr B_{m,6}}
   +\frac m2\eta_p+7\kappa_5\overline{a_m^+}.
\;}
\tag{19}
\]
若两个原中央均为零，则
\[
\boxed{\;
m'\mathcal T^{\rm Cart}_{m,6}
 -m\mathcal T^{\rm Cart}_{m',6}
 -7\kappa_5\overline{\mathcal R_{m,m'}^{(6)}}
 =
\frac{m'\bar\gamma_m^{\,6}\overline{\mathscr B_{m,6}}
      -m\bar\gamma_{m'}^{\,6}\overline{\mathscr B_{m',6}}}{120}.
\;}
\tag{20}
\]
右侧仍是两条原来源的实际除商。
(20) 没有将“共同 Frobenius 误差已消掉”误当成“指定行已非零”。

## 6. 与 R708 首边界判据的接续

R708 的实际短前缀在充分大 \(p\) 时包含第六块。
若两个原首边界均准确为零，便有
\(\bar g_{m,6}=\bar g_{m',6}=0\)。
此时 (17) 必须满足
\[
m'\mathcal T^{\rm Cart}_{m,6}
 -m\mathcal T^{\rm Cart}_{m',6}
 =7\kappa_5\overline{\mathcal R_{m,m'}^{(6)}}.
\tag{21}
\]
这给出了无需支付 \(\eta_p\) 或 \(u_s\) 的指定第六行。
但还须在同一原有理模型、全部极点及实际残差中
证明额外约束，才能排除 (21) 或将原 \(j_m=0\) 推到整个前缀。

原 \(m=136\) 可按同一证明参与 (17)；
只有在另有实际 \(j_{136}=0\) 时，才加入其 (18)–(20)。
本篇没有从前两条中央自动添第三条零，没有把
\(O(p^3)\) 的原有理极帽变成固定来源预算，也没有把
第六有限部当作总中央非零。

## 依赖

- [R647](R647-original-three-source-rational-model-and-five-cartier-conditions.md)：同一 \(P_2,\Theta_p,Z,G\)、完整三来源、前五 Cartier 行及原 \(z/Z\) 首差。
- [R614](R614-original-addition-integrality-window-and-complete-newton-tail.md)：完整整窗、三段分母与全部 Newton 高尾。
- [R708](R708-original-mod-p-prefix-and-integral-gaussian-return.md)：原首边界的短模 \(p\) 前缀与实际 Gaussian 返回。
- [R595](R595-original-central-diagonals-and-integral-four-row-comparison.md)：原两完整分子与保留实际低卷积残差的约定。

本篇全部为显示局部展开、Cartier 系数和整恒等证明；没有新增扫描或可重算输出。
