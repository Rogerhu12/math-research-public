# R250 附录：正常双边矩逼近坐标投影与变形慢核的闭图结构

日期：2026-11-13（UTC+8）。作者：normal_states。状态：已证明的中间结论；以下加强完整证明，依赖 R250 的实际双边矩实现。本文不把所得图子空间宣称为 $A^+$ 不变。

## 1. 定理

记 $P_I$ 为投影到
$$
H_I=\overline{\operatorname{span}}\{\chi_F:F\subset I,\ F\text{ 有限}\}.
$$
对任意正常泛函 $\phi$ 和任意 $\varepsilon>0$，可以在 R250 的构造中选
$$
\delta_j=
\begin{cases}
1,&j\in I=\{i_n\},\\
c(j+2)^{-\sigma},&j\notin I,
\end{cases}
\quad 0<c\le1,\quad1/2<\sigma<1,\quad i_n\ge2^n,
\tag{1.1}
$$
使同一实际有界双边矩算子满足
$$
\boxed{\|H_{\phi,\delta}-\phi(I)P_I\|<\varepsilon.}
\tag{1.2}
$$
仍有
$B(H_{\phi,\delta}\chi_G,\chi_F)=\delta_F\delta_G\phi(V_FV_G)$
及 R250 的全部相反阻尼交织。

若 $\phi\ge0$、$\lambda=\phi(I)>0$ 且
$\phi(S\mathcal A)=0$，则对任意给定 $\eta>0$，可选择 (1.1)，使实际
$\ker S^+$ 包含一个闭子空间
$$
K=\{u+Lu:u\in H_I\},\qquad
L:H_I\to H_I^\perp,\quad\|L\|<\eta.
\tag{1.3}
$$
此外存在 $C$-对称的有界幂等算子 $Q$，其像为 $K$，且
$$
S^+Q=Q S^-=0,\qquad \|Q-P_I\|\text{ 可任意小}.
\tag{1.4}
$$
一般不知 $Q$ 是否为正交投影，也不知 $K$ 是否在 $A^+$ 下不变。

## 2. 同时保留“含未升级位”的余列估计

按 R250 写
$$
\phi(T)=\sum_\nu\langle Tf_\nu,g_\nu\rangle,
\quad\mathbf f,\mathbf g\in H^{(\infty)}.
$$
零泛函无需证明。对两端分别记合成 $T_{\mathbf f,n}$、$T_{\mathbf{Cg},n}$。
第 $n$ 步已经升级集合 $I_n$，其余位取
$\beta_j=c(j+2)^{-\sigma}$。令
$$
R_{\mathbf f,n}=T_{\mathbf f,n}(I-P_{I_n}),
\quad
R_{\mathbf{Cg},n}=T_{\mathbf{Cg},n}(I-P_{I_n}).
\tag{2.1}
$$
全部四个算子在每个有限步骤都是 Hilbert–Schmidt。

若下一步升级 $j\notin I_n$，则新余列仍按“不含 $j$”和“含 $j$”分成两份。
前一份的索引 $G$ 除不含 $j$ 外，还必须含某个不在 $I_n\cup\{j\}$ 的位。
因此新余列算子是
$$
[R_{\mathbf f,n},\,V_j^{(\infty)}R_{\mathbf f,n}]
$$
在相应两个定义域子空间上的限制；另一端相同。
所以 R250 的紧行引理可以同时作用于完整合成和余列合成。
选择可和的正数 $e_n$，令 $K_0=\prod_n(1+e_n)$，可以使
$$
\|T_{\mathbf f,n}\|\le K_0\|T_{\mathbf f,0}\|,
\qquad
\|R_{\mathbf f,n}\|\le K_0\|R_{\mathbf f,0}\|,
\tag{2.2}
$$
两端均成立。可预先令 $K_0\le2$。

置
$$
P(c)=\prod_{j\ge0}(1+36c^2(j+2)^{-2\sigma}).
$$
则 $P(c)<\infty$，且 $P(c)\to1$ 当 $c\downarrow0$。
初始 $I_0=\varnothing$，故
$$
\|T_{\mathbf f,0}\|
 \le\|\mathbf f\|\sqrt{P(c)},\qquad
\|R_{\mathbf f,0}\|
 \le\|\mathbf f\|\sqrt{P(c)-1}.
\tag{2.3}
$$
第二式只对非空 Walsh 列求 Hilbert–Schmidt 和。

最终 $T_{\mathbf f,n}\to T_{\mathbf f,\delta}$ 强，
$P_{I_n}\to P_I$ 强，统一范数界给
$$
R_{\mathbf f,n}\to T_{\mathbf f,\delta}(I-P_I)
\quad\text{强}.
$$
因此 (2.2)–(2.3) 保留到极限。

由 $H=T_{\mathbf{Cg},\delta}^{\top}T_{\mathbf f,\delta}$，
$$
\|H(I-P_I)\|
 \le K_0^2\|\mathbf f\|\|\mathbf g\|
       \sqrt{P(c)(P(c)-1)}.
\tag{2.4}
$$
因为 $H^\top=H$、$P_I^\top=P_I$，转置等距还给
$\|(I-P_I)H\|=\|H(I-P_I)\|$。
于是
$$
\boxed{
\|H-P_IHP_I\|
\le2K_0^2\|\mathbf f\|\|\mathbf g\|
       \sqrt{P(c)(P(c)-1)}.
}
\tag{2.5}
$$
右侧随 $c\downarrow0$ 趋零。

## 3. 主块可保持为标量单位的任意小扰动

记
$$
M_n=\bigl((-1)^{|F|}\phi(V_FV_G)\bigr)_{F,G\subset I_n}.
\tag{3.1}
$$
这是 $H$ 在 $H_{I_n}$ 上的压缩矩阵，既不依赖未升级位的权，也不依赖以后如何选择高位。
初始 $M_0=\phi(I)$。

对任一固定 $F,G$，正常泛函
$T\mapsto\phi(V_FV_GT)$ 在一致有界 WOT 收敛序列上连续。
由 $V_j\to0$ WOT，
$$
\phi(V_FV_GV_j)\to0.
\tag{3.2}
$$
又 $V_j$ 与纯 $D_j^0=I-2E_j$ 的范数差为 $O(\eta_j)$，
而 $(D_j^0)^2=2D_j^0-I$，故
$$
V_j^2\to-I\quad\text{WOT},
\qquad
\phi(V_FV_GV_j^2)\to-\phi(V_FV_G).
\tag{3.3}
$$

将 $I_n\cup\{j\}$ 的有限基按不含、含 $j$ 分块。
两个非对角块由 (3.2) 趋零；右下块还有
$(-1)^{|F|+1}$ 的符号，所以 (3.3) 使它趋于 $M_n$。
因此
$$
M_{n+1}\longrightarrow
\begin{pmatrix}M_n&0\\0&M_n\end{pmatrix}
\quad(j\to\infty)
\tag{3.4}
$$
于这个有限矩阵空间的算子范数。

每一步除了第2节的四个紧行条件，还可要求
$$
\left\|M_{n+1}-
\begin{pmatrix}M_n&0\\0&M_n\end{pmatrix}\right\|<a_n,
\tag{3.5}
$$
其中 $a_n>0$ 预先取可和且总和任意小。这只是同时满足有限多个高位极限条件。
归纳得到
$$
\|M_n-\phi(I)I_{H_{I_n}}\|\le\sum_{k<n}a_k.
$$
有限 Walsh 子空间在 $H_I$ 中稠密，故
$$
\boxed{\|P_IHP_I-\phi(I)P_I\|\le\sum_ka_k.}
\tag{3.6}
$$
先把 $c$ 选得使 (2.5) 小于 $\varepsilon/2$，再令
$\sum a_k<\varepsilon/2$，即证 (1.2)。

所有真实变形仍有界。与 R250 的条件数相比，局部长度 $r-j+1$
只额外支付 $c^{-(r-j+1)}$，仍被
$e^{-770\,16^{r-1}}$ 的真实 carry 支付（此处 $r>j$；$r=j$ 是单独处理的纯局部项）。
同时
$\sum_j(j+1)^{-2}\delta_j^{-1}<\infty$。
固定 $c>0$ 后，高位 carry 误差仍趋零。

## 4. 正常正湮灭者迫使变形核包含一个闭图

现设 $\lambda=\phi(I)>0$，取 (1.2) 中
$\varepsilon<\lambda/8$。
因为 $\lambda P_I$ 为正规算子，圆周
$\Gamma=\{z:|z-\lambda|=\lambda/2\}$ 到其谱 $\{0,\lambda\}$
的距离为 $\lambda/2$。Neumann 逆公式保证 $\Gamma\subset\rho(H)$。

令
$$
Q=\frac1{2\pi i}\int_\Gamma(zI-H)^{-1}\,dz.
\tag{4.1}
$$
这是有界幂等算子，且由预解恒等式
$$
\boxed{
\|Q-P_I\|
\le\frac{\varepsilon}{\lambda/2-\varepsilon}.
}
\tag{4.2}
$$
特别它与 $P_I$ 的距离小于1。因为 $H^\top=H$，其预解式和 (4.1)
也 $C$-对称，所以 $Q^\top=Q$。

R250 给 $S^+H=H S^-=0$。
圆周不包围零，故
$$
Q=H\left(\frac1{2\pi i}
          \int_\Gamma z^{-1}(zI-H)^{-1}\,dz\right),
$$
而括号中的算子与 $H$ 交换。因此
$$
S^+Q=Q S^-=0.
\tag{4.3}
$$

令 $t=\|Q-P_I\|<1$。映射
$P_I:\operatorname{Ran}Q\to H_I$ 单射：
若 $x=Qx$ 且 $P_Ix=0$，则
$\|x\|\le t\|x\|$。
它也满射，因为
$P_IQ|_{H_I}=I+P_I(Q-P_I)|_{H_I}$ 可逆。
于是 $\operatorname{Ran}Q$ 是 $H_I$ 上的闭图，其图算子为
$$
L=(I-P_I)Q(P_IQ|_{H_I})^{-1},
\qquad
\|L\|\le\frac{t}{1-t}.
\tag{4.4}
$$
由 (4.2) 可使 $t$ 任意小，得到 (1.3)。

这里 $Q$ 是 $H$ 的谱投影，未证明它与 $A^+$ 交换。
$A^+H=HA^-$ 不允许把 $H^n$ 或一般 $f(H)$ 免费写成相同交织。
所以只声称这个闭图包含在 $\ker S^+$，不声称它是 $A^+$ 的不变子空间。

## 5. 本质范数与非紧性

对于 R250 的任意这类 $\delta$，沿无阻尼位 $j\in I$ 有
$$
\|V_j^\pm-D_j^0\|\to0.
$$
同时 $D_j^0-J_j\to0$ 强、
$(D_j^0)^*+J_j\to0$ 强。
由 $HV_j^-=V_j^+H$ 及其伴随，得到
$$
[H,J_j]\to0\quad\text{强},\qquad
[H^*,J_j]\to0\quad\text{强}\qquad(j\in I,\ j\to\infty).
\tag{5.1}
$$

固定单位 $x$，则 $J_jx\rightharpoonup0$，且
$\|HJ_jx\|\to\|Hx\|$。
对任意紧 $K$，$KJ_jx\to0$，故
$\|H-K\|\ge\|Hx\|$。
对 $x$ 取上确界，得到
$$
\boxed{\|H\|_{\rm ess}=\|H\|.}
\tag{5.2}
$$
因此非零 $H$ 不紧，特别不能把它冒充有限秩正常密度。

直接的对角核查也相容：沿 $j\in I$，
$$
\langle H\chi_j,\chi_j\rangle
=-\phi(V_j^2)\to\phi(I).
\tag{5.3}
$$

新闭图没有撤销表示改变。随着 $\varepsilon\downarrow0$，选择的 $c$、$\delta$
和实际 $S^\pm$ 也变化；其范数不具有所需的统一控制。
所以不能对 (1.3) 取一个未经控制的极限，把原 $S$ 送成有核。
它提供的是假想正常湮灭者在其适配变形中的精确必要几何结构。
