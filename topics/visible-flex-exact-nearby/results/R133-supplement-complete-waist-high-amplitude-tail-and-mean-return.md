# R133 补篇：完整腰振幅高模尾、有限头部修正及平均回传

2026-11-14。**已证明；10 个严格 BigInt 有理门实际执行并全部通过。**
本文直接消费已公开的最终完整腰32模向量，不需要失联的径向 shards，
也没有声称运行不存在的 head、response 或 adjoint。

固定中心仍是
\(\mathtt{ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413}\)，
完整原 \(|\eta|\le10^{-9}\)。
它给真实物理腰幅度行在整个 \(j\ge97\) 高空间的界，
并明确保留 mean 消去后由真实外端返回腰的额外路径。
有限头部是 \(|j|\le96\)，实际物理频率 \(4j\)。

## 1. 完整原输入和真实振幅梯度

全部输入来自已执行
[腰坐标23门报告](../notes/2026-11-13-R133-final-waist-amplitude-chart-rational.json)，
SHA256
\[
 \mathtt{8066f501acc87d42e7d58f30377680aaa317be500471fa71bcceef336fc9357b}.
\]
新报告保存相同准确 \(\alpha\)、全部33个 \(V_j\)（包括 mean）、
以及原整参数 target 腰半径区间
\[
 a_0\in
 [53436641/50000000,\ 1068732841/1000000000].
\]
因真实 \(a'(0)=0\)，准确 \(s_0=-a_0\)。
记
\[
 v_0=-a_0+\alpha\left(V_0+\sum_{j=1}^{32}V_j\cos4j\phi\right),
 \quad m_0=\langle v_0\rangle,\quad
 \psi_0=I(v_0-m_0)/m_0 .
 \tag{W.1}
\]
全部高指标32以内的 tiny coefficients 仍保留，未当作数值噪声删除。

真实物理幅度为
\[
 {\cal A}(v)=\frac2m\langle\cos(4\phi+4\psi)\rangle,\qquad
 m=\langle v\rangle,\quad \psi=I(v-m)/m .
\]
对 mean-free 方向，准确梯度是
\[
 G_{\perp}(v)=\frac8{m^2}I\sin(4\phi+4\psi),\qquad
 D{\cal A}(v)[h_2]=\langle G_\perp(v),h_2\rangle .
 \tag{W.2}
\]
这是原物理 \(\cos4\theta\) 幅度的微分，不是 moving 第一系数。
完整 mean 梯度另由
[真实 mean 列篇](R133-supplement-final-waist-mean-column-for-adjoint-lift.md)
支付，在本篇没有删除。

令 \(P_H\) 为全部 \(|j|\ge N,\ N=97\) 的 moving Fourier 投影。
对任意 \(h_{2,H}\in L^2\)，
\[
 |D{\cal A}(v)[h_{2,H}]|
 \le\|P_HG_\perp(v)\|_{L^2}\|h_{2,H}\|_{L^2}.
 \tag{W.3}
\]
没有对方向作 finite Fourier 截断；其 mean 为零仅因为它属于指定高空间。

## 2. 同一 finite 中心的完整解析尾

取真实复角宽 \(\sigma=1/4\)，并以完整 Wiener 和定义
\[
 P_0=\|\psi_0\|_{A^0},\qquad P_\sigma=\|\psi_0\|_{A^\sigma}.
\]
若
\(g_0=a_{0,-}-\alpha V_0>0\)，则逐项准确有
\[
 P_0\le \sum_{j=1}^{32}\frac{\alpha|V_j|}{4jg_0},\qquad
 P_\sigma\le\sum_{j=1}^{32}
                     \frac{\alpha|V_j|e^j}{4jg_0}.
 \tag{W.4}
\]
全部32项实际代入有理预算，得到
\[
 P_0<.228928090337669475446392871079,\qquad
 P_\sigma<.632419537669125157744493578495<13/20.
 \tag{W.5}
\]
这些是当前 finite 中心的解析界，不给未知扰动免费授同一解析宽。

由于
\(\|\sin(4\phi+4\psi_0)\|_{A^\sigma}
 \le e^{4\sigma+4P_\sigma}\)，高频原函数给
\[
 \|P_HG_\perp(v_0)\|_{L^2}
 \le \|P_HG_\perp(v_0)\|_{A^0}
 \le \frac2{Ng_0^2}
       \exp\{-4\sigma(N-1)+4P_\sigma\}.
 \tag{W.6}
\]
这里保留了 \(I\) 在高空间的实际 \(1/(4N)\)，没有用粗的 \(1/4\)。
新10门实际得
\[
 \boxed{\ \|P_HG_\perp(v_0)\|_{L^2}
       <4.601240858219287009509214\,10^{-43}<10^{-42}.\ }
 \tag{W.7}
\]
它控制所有 \(j\ge97\)，不是有限几个模式的采样上界。

## 3. 整个任意未知 Wiener 球，包括 mean

现在允许
\[
 v=v_0+\delta v,\qquad
 \|\delta v\|_{A^0}\le\rho=10^{-6},
 \tag{W.8}
\]
仍为原真实 even 四重反射类，完整未知 Fourier 尾和 mean 都存在。
此前腰坐标报告已证明此球保持 \(v<0\) 和 \(m<0\)，
所以物理角图仍合法。

令 \(\delta m=\langle\delta v\rangle\)、
\(g=g_0-\rho>0\)。准确相位差是
\[
 \psi-\psi_0=\frac{I\delta v-\psi_0\delta m}{m_0+\delta m}.
\]
Wiener 范数具有准确的 mean/nonmean 和分解
\[
 \|P_{\ne0}\delta v\|_{A^0}
                   \le\rho-|\delta m|.
\]
利用 (W.5) 的 \(P_0<1/4\)，得到更紧且保留 mean 的界
\[
 \boxed{\ \|\psi-\psi_0\|_{A^0}
 \le\frac{(\rho-|\delta m|)/4+P_0|\delta m|}{g}
 \le\Delta:=\frac{\rho}{4g}<\frac1{4000000}.\ }        \tag{W.9}
\]
这一步没有假定 \(\delta m=0\)，也没有给 \(\delta v\) 加任何解析假设。

Banach 代数指数差给
\[
 \|\sin(4\phi+4\psi)-\sin(4\phi+4\psi_0)\|_{A^0}
 \le4\Delta e^{4(P_0+\Delta)}.
\]
将两个部分都先投至高空间，再用真实 \(I\) 权，
\[
 \|P_HG_\perp(v)\|_{L^2}
 \le \frac2{Ng^2}
 \left[
 e^{-4\sigma(N-1)+4P_\sigma}
       +4\Delta e^{4(P_0+\Delta)}
 \right].
 \tag{W.10}
\]
实际有理预算给整个无限维球
\[
 \boxed{\ \sup_{\|\delta v\|_{A^0}\le10^{-6}}
 \|P_HG_\perp(v)\|_{L^2}
 <4.220280070616092379084897\,10^{-8}<4.5\,10^{-8}.\ }
 \tag{W.11}
\]
这是更新后振幅行的完整高尾上界；没有用 (W.7) 的 finite 中心尾
替代未知无限尾的影响。若后续使用更强的 \(A^3\) 球，它是 (W.8)
的子集，所以 (W.11) 同样适用。

原腰23门已经在同一个球证明
\[
 |D{\cal A}(v)[\cos4\phi]|^{-1}<5/3 .
\]
因而对任意完整高方向，可用一个明确 head trace 修正
\[
 h_{2,H}\longmapsto h_{2,H}
       -\frac{D{\cal A}(v)[h_{2,H}]}
                    {D{\cal A}(v)[\cos4\phi]}\cos4\phi ,
 \tag{W.12}
\]
使真实幅度行准确为零；mean 不变。
其新增 head cosine **幅度系数**满足
\[
 |c_{\rm head}|
 <7.033800117693487298474827\,10^{-8}\|h_{2,H}\|_2
 <7.5\,10^{-8}\|h_{2,H}\|_2 .                         \tag{W.13}
\]
这里仅支付腰 trace 的完整行消去；径向延伸和 body 解算子的费用
仍由实际 BVP 支付，不能把这一行的右逆叫作 whole inverse。

## 4. 消去真实 mean 后，外端高输入到腰的路径仍保留

这一节回到固定 actual finite32 中心及其原 scalar mean Green；
不把 local 腰扰动球自动推广为新 whole-body 证书。
记 nonmean 变化为 \(w=(\xi,\zeta_\perp)\)。
原完整 mean 体行含
\[
 B_{\rm int}w=2\beta m
   \langle u\xi+K(v-m)\zeta_\perp\rangle .
\]
若 \(w=w_H\) 在每个径向点都只含 \(|j|\ge97\)，则中心的
\(u,v-m\) 仅有 \(|j|\le32\)，所以
\[
                       B_{\rm int}w_H=0
 \tag{W.14}
\]
是全空间正交恒等式。但 true 外 mean 功能
\(\ell_R\zeta_\perp(R)\) 并非有限带，不能删除。

对齐次普通数据与无 mean jumps，消元后的完整 mean 是
\[
 z(r)=H(r,R)\ell_R w_{2,H}(R),
\]
于是 effective 腰幅度高输入准确为
\[
 D{\cal A}_{\rm red}[w_H]
 =\langle P_HG_\perp(v_0),w_{2,H}(0)\rangle
      +b_{{\rm amp},m}H(0,R)\ell_Rw_{2,H}(R).          \tag{W.15}
\]
消费已经证明的实际界
\[
 |b_{{\rm amp},m}|<13/10,\quad
 H(0,R)<2.693551\,10^{-13}\Gamma,\quad
 \|\ell_R\|_{L^2\to\mathbb R}<1.084\,10^{-6},
\]
10门有理预算给
\[
 \boxed{\begin{aligned}
 |D{\cal A}_{\rm red}[w_H]|
 <{}&10^{-42}\|w_{2,H}(0)\|_2\\
 &+3.796\,10^{-19}\Gamma\|w_{2,H}(R)\|_2 .
 \end{aligned}}                                      \tag{W.16}
\]
第二项经 (W.12) 的 head 幅度修正，系数小于
\(6.327\,10^{-19}\Gamma\)。
**完整径向 \(\Gamma\) 尚未实际计算，不能置为1。**

普通 mean 源、独立 \(f_B\)、response mean jumps 和参数 mean 源
仍按原完整 scalar Green 加入。它们不是 (W.14) 的高方向正交项。
对更新后含无限 Fourier 尾的 whole-body 中心，\(B_{\rm int}w_H\)
未必为零；(W.14)–(W.16) 不自动转授给那个新对象。

## 5. mean 消去后真正 \(\nu\) 数据仍全部位于 head

固定当前 finite32 中心时，原完整 B.8–B.13 已支付
\[
 \operatorname{supp}F_\nu\subset\{|j|\le96\},\qquad
 \operatorname{supp}a_{\rm int}\subset\{|j|\le64\}.
\]
令 \(F_m\) 为完整参数 mean 数据，\(\mathbb G\) 为真实 scalar Green。
原 exact elimination 给
\[
 \widehat F=F_w-\mathbb C\mathbb GF_m.
 \tag{W.17}
\]
体部分仍支持 \(|j|\le96\)。由于 compact metric control 在外端恒零，
\((\mathbb GF_m)(R)=0\)，其 ordinary mean 解连续，
所以新增外端和 jump 数据准确为零。
腰 odd 条件也不受 mean 变化影响。
唯一额外腰行是实际 head 中保留的真实幅度标量
\[
                 -b_{{\rm amp},m}(\mathbb GF_m)(0).
 \tag{W.18}
\]
因此完整 \(\widehat F\) 在 \(|j|\ge97\) 的 high 数据槽里准确为零，
而不是仅很小。它的径向支持一般已延伸至腰，不能再按原 bump 支集截掉。

这说明真正193-state head / full high 接合时，应完整保留这条 scalar
mean 回传，而不需要虚构一个未支付的 \(\nu\) high 源尾。
它不使真实物理 \(b_4\)、其它外行或腰 mean 泛函变成有限带。
实际 high inverse、head response/adjoint、参数 Schur 及 far regular
标签方程仍须各自完成。

## 6. 实际有理执行

- [精确 BigInt 源](../scripts/fourfold_codazzi_waist_high_amplitude_tail.mjs)；
- [10门完整报告](../notes/2026-11-14-R133-final-waist-high-amplitude-tail-rational.json)。

指数在正有理参数上用完整 Taylor 加几何尾，正运算每步在
90位十进小数外舍，报告保留完整上下界、项数和尾。
\(e^{-96}\) 通过 \(e\) 的已证下界连续相乘并取倒数支付，
没有调用浮点指数当作严格数值。
同一完整函数已在可用 V8 中执行10门，全部通过。
所有 native 结论仅为上述准确已公开输入的有理消费；
没有恢复或伪造任何缺失径向 trial。
