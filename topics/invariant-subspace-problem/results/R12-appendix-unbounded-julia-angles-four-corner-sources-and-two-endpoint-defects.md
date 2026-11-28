# R12 补充：无界 Julia 图角的四个真实高位来源与双端缺陷谱

日期：2026-11-28（Asia/Taipei）。  
会话：Astra-ISP-8542378f-20261127。作者：stable_kernel_return；AI-assisted GPT-6 Astra Pro。

接[原 Walsh 根图的最大本质距离](R12-appendix-walsh-root-maximal-essential-distance-and-no-bounded-angle.md)。本篇只使用该稿已经支付的同一原尾、同一未知普通不变投影及联合高位 pattern；新增内容是把近图向量实际投回闭图，得到无界图角及其伴随的原定义域来源。

## 1. 同一原对象和结论

固定原 Haar 尾 $C=A^{(m_0)}$，任选原 Walsh 完整循环块的全部平方根分支，令 $R$ 为相应最大直和闭根，$\Pi=P_{\Gamma R}$。亦允许先精确吸收一个固定有限头。

令 $P$ 为一个非零、非恒等的闭 $(C\oplus C)$ 不变子空间的正交投影。对每个 $p,q\in\{0,1\}$，存在实际单位弱零列 $w_j^{p,q}$，满足
$$
\boxed{
Pw_j^{p,q}=p\,w_j^{p,q},\qquad
\|(\Pi-qI)w_j^{p,q}\|\longrightarrow0.
}
\tag{1.1}
$$
第一个等式是精确等式，不是近图陈述。

再令 $\mathcal U$ 为同一 $R$ 的真实 Julia 酉矩阵，$\Pi=\mathcal UP_0\mathcal U^*$、$P_0=\operatorname{diag}(I,0)$。假设这个真正原不变子空间可以写成
$$
\operatorname{Ran}P=\mathcal U\Gamma Z,\qquad
\Gamma Z=\{(x,Zx):x\in\mathcal D(Z)\},
\tag{1.2}
$$
其中 $Z$ 是闭、稠密定义的算子，不假设有界。

则 $Z$、$Z^*$ 均有实际单位弱零来源
$$
x_j\in\mathcal D(Z),\quad Zx_j\to0,\qquad
y_j\in\mathcal D(Z^*),\quad Z^*y_j\to0.
\tag{1.3}
$$
它们同时都是无界算子，并且两个有界缺陷算子满足
$$
\boxed{
\{0,1\}\subset
\sigma_{\rm ess}\bigl((I+Z^*Z)^{-1}\bigr),\qquad
\{0,1\}\subset
\sigma_{\rm ess}\bigl((I+ZZ^*)^{-1}\bigr).
}
\tag{1.4}
$$

因此未知闭图角不仅不能有界，也不能具有有界逆、紧的图域嵌入或紧预解式。$Z$、$Z^*$ 都不能同时具有闭值域和有限维核。若另有 $\ker Z=0$ 与 $\overline{\operatorname{Ran}Z}=H$，则 $\operatorname{Ran}Z$ 必为稠密非闭真子空间；这两个额外条件不由本篇自动给出。

## 2. 已付联合来源与新的弱零性

前稿给出自伴酉
$$
U_j=M_{\chi_j}\oplus M_{\chi_j}
$$
及分支无关的物理中位半旗 $F_j$，其中 $F_j$ 只依赖第 $0,\ldots,j-1$ 位，并且
$$
\Pi U_j\xi-U_jF_j\xi\to0,\qquad
F_j\xrightarrow{\rm WOT}\tfrac12I,
\tag{2.1}
$$
对每个固定 $\xi\in H\oplus H$ 成立。前稿以真实 $s+1$ 位 pattern 和两次极限另行支付
$$
[P,U_j]\to0,\qquad [P,U_jF_j]\to0
\quad{\rm 强*}.
\tag{2.2}
$$
本篇不把两个单独的强极限相乘。

还需要
$$
U_jF_j\xrightarrow{\rm WOT}0,\qquad
U_j(I-F_j)\xrightarrow{\rm WOT}0.
\tag{2.3}
$$
对两个固定低柱向量，当 $j$ 超过其位数时，内积中第 $j$ 位只有均值为零的 $\chi_j$ 因子；$F_j$ 不用该位，所以内积精确为零。由两算子范数不超过 $1$ 和柱函数稠密性，得到 (2.3)。

## 3. 四角来源的构造与精确投回

取单位 $\eta\in\operatorname{Ran}P$，置
$$
a_j=U_jF_j\eta,\qquad
b_j=U_j(I-F_j)\eta.
$$
(2.1)、(2.3) 给
$$
a_j\rightharpoonup0,\quad b_j\rightharpoonup0,\qquad
\|a_j\|,\|b_j\|\longrightarrow1/\sqrt2.
\tag{3.1}
$$
由 (2.2)，
$$
Pa_j-a_j\to0,\qquad Pb_j-b_j\to0.
\tag{3.2}
$$
为处理 $\Pi$，不能把 (2.1) 直接作用到移动的 $F_j\eta$。令
$$
e_j=\Pi U_j\eta-a_j\to0.
$$
利用真实投影恒等式 $\Pi^2=\Pi$，
$$
\Pi a_j-a_j=(I-\Pi)e_j\to0,\qquad
\Pi b_j=e_j+a_j-\Pi a_j\to0.
\tag{3.3}
$$
所以对充分大的 $j$，可定义
$$
w_j^{1,1}=\frac{Pa_j}{\|Pa_j\|},\qquad
w_j^{1,0}=\frac{Pb_j}{\|Pb_j\|}.
\tag{3.4}
$$
它们是 $\operatorname{Ran}P$ 中真正的单位弱零列；由 (3.1)–(3.3)，分别满足 $\Pi w_j^{1,1}-w_j^{1,1}\to0$ 和 $\Pi w_j^{1,0}\to0$。

同样选单位 $\eta\in\ker P$，仍用同一 $a_j,b_j$。此时 (2.2) 给 $Pa_j,Pb_j\to0$，而 (3.1)、(3.3) 不变。定义
$$
w_j^{0,1}=\frac{(I-P)a_j}{\|(I-P)a_j\|},\qquad
w_j^{0,0}=\frac{(I-P)b_j}{\|(I-P)b_j\|}.
\tag{3.5}
$$
这给另两角，证明 (1.1)。整个构造仅用同一个未知 $P$，并保留真实范数归一。

## 4. 实际闭图中的小值与大值来源

假设 (1.2)。因为 $w_j^{1,q}$ 已精确属于 $\operatorname{Ran}P$，
$$
\mathcal U^*w_j^{1,q}=(u_j^{(q)},Zu_j^{(q)})
$$
是 $\Gamma Z$ 中的实际向量。因此
$$
u_j^{(q)}\in\mathcal D(Z),\qquad
\|u_j^{(q)}\|^2+\|Zu_j^{(q)}\|^2=1.
\tag{4.1}
$$
这不是从一个近图坐标直接宣称域包含。

对 $q=1$，(1.1) 变为
$$
\|u_j^{(1)}\|\to1,\qquad \|Zu_j^{(1)}\|\to0.
$$
两个坐标都弱趋零。令 $x_j=u_j^{(1)}/\|u_j^{(1)}\|$，得到 (1.3) 的第一列。

对 $q=0$，则有
$$
\|u_j^{(0)}\|\to0,\qquad \|Zu_j^{(0)}\|\to1.
\tag{4.2}
$$
故 $Z$ 不可能有界；这里的像仍只弱趋零，没有用 (4.2) 违反闭性。

为付伴随来源，使用闭、稠密定义算子的准确正交补公式
$$
(\Gamma Z)^\perp
=\{(-Z^*v,v):v\in\mathcal D(Z^*)\}.
$$
于是
$$
\mathcal U^*w_j^{0,q}=(-Z^*v_j^{(q)},v_j^{(q)}),
\qquad
\|Z^*v_j^{(q)}\|^2+\|v_j^{(q)}\|^2=1.
$$
$q=0$ 给 $\|Z^*v_j^{(0)}\|\to0$、$\|v_j^{(0)}\|\to1$，归一后得到 (1.3) 的第二列；$q=1$ 给 $\|v_j^{(1)}\|\to0$、$\|Z^*v_j^{(1)}\|\to1$，证明 $Z^*$ 无界。

## 5. 图范数、缺陷谱和范围边界

令
$$
A_Z=(I+Z^*Z)^{-1},\qquad
V_Z=Z(I+Z^*Z)^{-1/2}.
$$
闭图的标准酉参数化为
$$
h\longmapsto(A_Z^{1/2}h,V_Zh),
\qquad
A_Z+V_Z^*V_Z=I.
\tag{5.1}
$$
它是从 $H$ 到 $\Gamma Z$ 的酉算子，其中闭图使用 $H\oplus H$ 的范数。

将 §4 两列实际单位弱零闭图向量通过 (5.1) 的逆送回，得到单位弱零 $h_j^{(q)}$。$q=0$ 时
$$
\|A_Z^{1/2}h_j^{(0)}\|\to0
\quad\Longrightarrow\quad
\|A_Zh_j^{(0)}\|\to0.
$$
$q=1$ 时 $\|V_Zh_j^{(1)}\|\to0$，并由 $0\le I-A_Z\le I$ 得
$$
\|(I-A_Z)h_j^{(1)}\|^2
\le\langle(I-A_Z)h_j^{(1)},h_j^{(1)}\rangle
=\|V_Zh_j^{(1)}\|^2\to0.
$$
故 $0,1$ 都有实际单位弱零 Weyl 列，给 (1.4) 第一式。把同样论证用于 §4 的伴随列，给第二式。

图域嵌入
$$
(\mathcal D(Z),\|\cdot\|_{\rm graph})\longrightarrow H,\qquad x\longmapsto x
$$
不是紧算子：§4 的 $q=1$ 列在图 Hilbert 空间中弱趋零，但其原 $H$ 范数趋于 $1$。伴随图域同理。若存在 $\lambda\in\rho(Z)$，紧预解式会通过图范数同构使该嵌入紧，因此也被排除；没有预设预解集非空。

最后，若 $\operatorname{Ran}Z$ 闭且 $\ker Z$ 有限维，则闭值域定理给
$$
\|Zx\|\ge c\,\operatorname{dist}(x,\ker Z)
\qquad(x\in\mathcal D(Z))
$$
的某个 $c>0$。把 (1.3) 的单位弱零 $x_j$ 代入，有限维核投影趋零，矛盾。对 $Z^*$ 同理。这精确说明了范围结论的条件；不将一般未知 $Z$ 的核自动判零。

## 6. 未付的正向来源

本篇没有构造 $Z$，也没有给任意原不变子空间自动取得表示 (1.2)：相对 Julia 坐标可能首先只有闭线性关系，带有垂直部或非稠密第一投影。若 (1.2) 确实成立，则上述来源位于真正的 $\mathcal D(Z)$、$\mathcal D(Z^*)$，完整保留其图范数。

因此未知正向实现仍须处理两端同时退化的实际闭图域、非交换图正则器，或另行构造场外同源二次分子。不能用这些精确必要条件代替根存在或 ISP 完成。
