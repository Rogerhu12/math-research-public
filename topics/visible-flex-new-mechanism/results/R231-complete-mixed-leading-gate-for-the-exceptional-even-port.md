# R231：例外偶端芽的完整 mixed 领先项与两个准确能量门

日期：2026-11-15。完整纸面推导；没有新的研究运行。本稿不预先断言冻结八包的两个新能量值非零。

来源：[R56 原分子恢复](R56-full-variable-range-numerator-calculus-and-finite-fourth-system.md)、[R73 点态八矩及链式项](R73-pointwise-eight-matrix-and-local-third-bridge.md)、[R183 合法重叠圆](R183-overlapping-derivative-packet-circle-invisible-to-third-hook.md)、[R221 完整 gauge ruling](R221-complete-fixed-circle-ruling-moment-map-and-joint-right-inverse.md)、[R224 偶部商与中心化](R224-even-germ-ruling-invariant-and-positive-epsilon-obstruction.md)、[R227 可实现例外端芽](R227-realizable-quadratic-k-even-ports-and-the-exceptional-germ.md)和 [R229 p2 能量边界身份](R229-p2-energy-boundary-identity-for-exceptional-germs.md)。

R229 已说明例外端芽的候选 pure 四次能量在三矩圆上准确为零。本稿保留全部第三局部恢复、变化 profile 链式项和传入 histories，证明同一端芽仍有两个具体的 mixed 领先系数。二者若有一个非零，就严格排除该固定圆上的整个第四 ruling，且不能由二阶或三阶 homogeneous gauge 改变。

## 1. 端芽、物理支与三矩圆

令 $\varepsilon>0,h_e>0,k_e\ne0$，取准确局部端芽

$$
h=h_e e^{\varepsilon\sigma^2},\qquad
k=k_e(1-2\varepsilon\sigma^2),\qquad
\omega=b+\frac{k_e}{h}.
\tag{1}
$$

固定 $I=[l,r]$，假定

$$
x+b>0,\qquad x+b+\frac{k_e}{h_e}>0
\quad(x\in I).
\tag{2}
$$

沿显式解析模型的整个实 $\sigma$ 轴，$z=x+\omega$ 均为正：$k_e/h$ 位于 $0$ 和 $k_e/h_e$ 之间。本稿只用这个解析模型检验局部 germ 身份，不延长实际闭路径。

取双 collar 为零的实 f、g，满足

$$
\mathbf m(f,f)=\mathbf m(g,g),\qquad
\mathbf m(f,g)=0.
\tag{3}
$$

令

$$
\phi_\theta=\cos\theta f+\sin\theta g,\qquad
D_\theta=f^2-\phi_\theta^2.
\tag{4}
$$

二次算子槽位按对称双线性解释，故 $\mathbf m(D_\theta)=0$。置 $q=x+b$，定义

$$
E_b(u,v)=\frac14\int_I(q^2u''v''+2u'v')\,dx
\tag{5}
$$

以及

$$
8G_b(u,v)=4quv-2q^2(uv'+u'v)+2q^3u'v'
+q^2J(q^2u''v''+2u'v').
\tag{6}
$$

J 始终是同一个正右积分。式 (5) 对带左尾的输入也按真实原函数计算，不重新置零。

## 2. 中心化与完整 gauge 商

(1) 的 scalar 全偶，所以 R73 的 $M_{\rm raw}$ 偶。按 R224 取中心第二累计矩阵 $\mathsf o(0)=0$，保留全部二阶局部恢复；第三场仍用完整 forcing 恢复，只规定中心 characteristic 初值为零，不把 normal 或 eta 同时置零。

记中心模型的 ruling 为 $\widehat{\mathscr K}_\theta$。R224 的真实比较给

$$
[\operatorname{Ev}\mathscr K^0_\theta]
=[\widehat{\mathscr K}_\theta]\quad\bmod\mathcal W_e,
\qquad
\mathcal W_e=\operatorname{span}
\left\{h,\sigma^2,
\frac{1+4\varepsilon^2k_e^2\sigma^4}{h}\right\}.
\tag{7}
$$

其依据不是删除前缀：由 (3)，真实中心二阶初值差
$\Phi_{\mathsf m_*}D_\theta$ 是双 collar 为零的固定 profile。其二阶 gauge 响应的偶部在 $\mathcal W_e$；相应平方项和真实第三初值差也只给三矩项。中心第三模型即使尚不满足左 range，这个比较仍成立；R221 的单紧槽配对保留了该初值的完整尾。

协变导数的奇偶链与 R224 相同：第一场 TB 偶；第二场 N 偶、TB 奇；第三场 TB 偶、N 奇。故中心第四 ruling 自身为偶。下面的增长极限因而直接作用于 (7)。

## 3. 唯一正 h 层与真实第二累计量

记

$$
v=2\varepsilon\sigma,\qquad
j=2\varepsilon k_e\sigma^2,\qquad
z=q+\frac{k_e}{h},\qquad e=hq+j.
\tag{8}
$$

R227 由 R73 六项式已准确提取

$$
r_\sigma=hk\,G_b+R_\sigma,\qquad
R_\sigma=O(\mathrm{poly}).
\tag{9}
$$

这里 $O(h^a\mathrm{poly})$ 表示：在本稿所需的固定有限个 x 导数范数中，被 $C h^a(1+|\sigma|)^N$ 控制；N 可以依表达式改变。R73 的显式系数保证 $R_\sigma$ 只含多项式增长项及乘 $h^{-1},h^{-2},h^{-3}$ 的多项式项，有限阶 s 导数也满足同类界。这个界不是对第四余项的猜测。

令

$$
\beta(\sigma)=\int_0^\sigma hk\,d\tau.
$$

由 $(\sigma h)'=h+2\varepsilon\sigma^2h$，

$$
\boxed{
\beta=2k_e\int_0^\sigma h\,d\tau-k_e\sigma h,\qquad
\frac{\beta}{\sigma h}\longrightarrow-k_e.
}
\tag{10}
$$

因为 $\int_0^\sigma h/(\sigma h)\to0$；其导数之比为
$(1+2\varepsilon\sigma^2)^{-1}\to0$。因此

$$
h\beta^2\sim k_e^2\sigma^2h^3.
\tag{11}
$$

完整第二 history 是

$$
O_D=\Phi_{\mathsf o(\sigma)}D_\theta
=\beta G_b(D_\theta)+C_D(\sigma),\qquad
C_D=O(\mathrm{poly}).
\tag{12}
$$

$C_D$ 是 (9) 中余算子的真实 s 积分，没有被置零。

## 4. 保留局部恢复与变化 profile 链式项

本节全部估计针对 R56 分子。初场

$$
V_f=\left(-\frac{f'}2,0,hf-\frac e2f'\right)
$$

及所需 x 导数、完整协变 s 导数均至多
$O(h\mathrm{poly})$。框架矩阵 $\Omega(k)$ 只有多项式增长。

二阶局部场的原分子为

$$
V_K=\left(\frac{\eta_2}{h},zP_2+B_2,
\frac{e\eta_2}{h}\right).
\tag{13}
$$

其 forcing 配对 $J,T_\xi,T_s,T_{s\xi}$ 至多
$O(h^2\mathrm{poly})$。由 R56 (2)、(6)，

$$
P_2,B_2,\eta_2=O(h\mathrm{poly}),\qquad
V_K=(O(\mathrm{poly}),O(h\mathrm{poly}),O(h\mathrm{poly})).
\tag{14}
$$

其所需导数仍至多 $O(h\mathrm{poly})$。故在
$\ell_\sigma(f;u,v)=R[H(Y_f,K_\sigma(u,v))]$ 中，配对分子至多
$O(h^2\mathrm{poly})$，P、B 至多 $O(h\mathrm{poly})$。又有

$$
K_0=O(\mathrm{poly}),\qquad
\lambda=\frac{e_s}{h^2}=O(h^{-1}\mathrm{poly}),\qquad
\frac{h_s}{h^2}=O(h^{-1}\mathrm{poly}).
$$

将这些量逐项放入 R56 (5)，包括 $K_0P$ 和 $(K_0/z)B$，得到

$$
\boxed{\ell_\sigma=O(h\mathrm{poly}).}
\tag{15}
$$

变化 profile 的链式项必须保留。R73 (15) 的第一系数准确满足

$$
\nu-\frac{\gamma k}{h^2}
=-\left(\frac dh\right)_s
=-\left(\frac jh\right)_s=O(h^{-1}\mathrm{poly}).
\tag{16}
$$

其余两项连同 $J_e$ 至多为固定 profile 算子的
$O(\mathrm{poly})$，所以

$$
\Psi_\sigma(f,r_\sigma D_\theta)=O(h\mathrm{poly}).
\tag{17}
$$

这是完整几何方程中的抵消，不能分别扩大 $\nu$ 和
$\gamma k/h^2$ 的界后忽略 (16)。

## 5. 完整第三 history 和第四 leading

中心第三 characteristic 的原式为

$$
(W_3)_s=
-2\ell_\sigma(\phi_\theta;D_\theta)
+2r_\sigma(\phi_\theta,O_D)
+2\Psi_\sigma(\phi_\theta,r_\sigma D_\theta).
\tag{18}
$$

由 (9)、(12)，唯一 $h^2$ 级主项是

$$
2hk\beta\,G_b(\phi_\theta,G_bD_\theta)
=(\beta^2)'G_b(\phi_\theta,G_bD_\theta).
$$

其他全部项至多 $O(h\mathrm{poly})$。其从零起的真实 s 积分仍为
$O(h\mathrm{poly})$，故

$$
\boxed{
W_3=\beta^2G_b(\phi_\theta,G_bD_\theta)
+O(h\mathrm{poly}).
}
\tag{19}
$$

第三局部恢复也没有删除。完整二阶分子
$V_Z=V_K-V_{Y_{O_D}}$ 及其导数至多 $O(h^2\mathrm{poly})$；
第三 forcing 的四个配对至多 $O(h^3\mathrm{poly})$。
R56 因而给

$$
P_3,B_3,\eta_3=O(h^2\mathrm{poly}),
\tag{20}
$$

第三局部分子三分量分别至多
$(O(h\mathrm{poly}),O(h^2\mathrm{poly}),O(h^2\mathrm{poly}))$。

R56 的 ruling 是配对的 $T_\xi/h$。二阶局部平方、二阶局部与 history 的交叉，以及第一场与第三局部场的交叉，合计至多
$O(h^2\mathrm{poly})$，相对于 (11) 都严格低一指数 h 层。

原第一场能量的准确分解为

$$
\mathcal E_\sigma(u,v)
=hE_b(u,v)+\frac j2\int_Iq\,u''v''
+\frac{1+j^2}{4h}\int_Iu''v''.
\tag{21}
$$

代入 (12)、(19)，得到完整 ruling 的极限

$$
\boxed{
\frac{\widehat{\mathscr K}_\theta}{h\beta^2}
\longrightarrow
C_\theta=
-E_b(G_bD_\theta,G_bD_\theta)
+2E_b(\phi_\theta,G_b(\phi_\theta,G_bD_\theta)).
}
\tag{22}
$$

规范沿用 R224 的整个 ruling；不是从单个 pure Fourier 系数猜一个因子。

(7) 中每个函数除以 $h\beta^2$ 都趋零。如果某个
$C_\theta\ne0$，则中心模型不可能在 germ 中属于
$\mathcal W_e$。确切地，(1)、(2) 上的 R56 有限分离表示给全实
$\sigma$ 的解析三角系统；germ 中的常系数 membership 若成立，就解析延续成整个模型的同一身份，与 (22) 矛盾。这里只要求固定 profile 足够光滑，不要求其关于 x 解析。

通过 (7)，这个必要门与实际前缀及所有允许的二、三阶 gauge 无关。

## 6. pure 精确消去后留下两个 mixed 数值

R229 的同锚式给，对任意紧支撑 u，

$$
E_b(u,G_b(u,u))=0.
\tag{23}
$$

例如写 $u=qy,R=y''$，其密度是
$-(q^9R^3)'/48$。极化得三个紧槽的循环身份

$$
E_b(u,G_b(v,w))+E_b(v,G_b(u,w))
+E_b(w,G_b(u,v))=0.
\tag{24}
$$

置

$$
A_f=G_b(f,f),\quad A_g=G_b(g,g),\quad A_{fg}=G_b(f,g).
$$

(3) 保证 $A_g-A_f,A_{fg}$ 和 $G_bD_\theta$ 真正双 collar 为零；
$A_f,A_g$ 各自一般保留共同非零二次左尾。

在 (24) 取 $(u,v,w)=(\phi_\theta,\phi_\theta,G_bD_\theta)$。
这三个输入都是紧槽，所以

$$
2E_b(\phi_\theta,G_b(\phi_\theta,G_bD_\theta))
=-E_b(G_bD_\theta,G_b(\phi_\theta,\phi_\theta)).
$$

于是

$$
\boxed{
C_\theta=-E_b(G_bD_\theta,A_f)
=\sin^2\theta\,L_c+\sin(2\theta)\,L_s,
}
\tag{25}
$$

其中

$$
\boxed{
L_c=E_b(A_f,A_g-A_f),\qquad
L_s=E_b(A_f,A_{fg}).
}
\tag{26}
$$

两个能量都按真实左尾计算。没有把 $A_f$ 或 $A_g$ 假称紧槽；
(24) 合法使用的是紧的第三输入 $G_bD_\theta$。

因此整个领先相位为零，当且仅当

$$
L_c=L_s=0.
\tag{27}
$$

这里没有第四谐波，与 R229 的三矩 pure 恒等式一致；但那个恒等式不蕴含 (27)。任一标量非零即排除完整 ruling；二者均零则只支付这一主层，不能宣完整次层或局部恢复已消失。

## 7. 冻结八包的最小新计算

固定 $b=0$。保留 R193 的同一个 step、三个左补矩 bump、八个七差分幅度和 packet 平移。新目标只有 (26) 的两个 raw 值，不重算旧
$c_0,c_2,c_4,c_6$，不编旧 forcing 或 W 基。

R193 宽度是共同伸缩
$f_\lambda(\lambda x)=f_{\rm raw}(x)$、
$g_\lambda(\lambda x)=g_{\rm raw}(x)$。由 (6) 逐项，

$$
G_0(f_\lambda,g_\lambda)(\lambda x)
=\lambda G_0(f_{\rm raw},g_{\rm raw})(x),
$$

所以

$$
\boxed{
L_c(\lambda)=\lambda L_c(1),\qquad
L_s(\lambda)=\lambda L_s(1).
}
\tag{28}
$$

共同正归一化只增加其四次幂因子。两个准确 raw 系数便决定全部正宽度的符号；实际几何排除只作用于能嵌入所选 I 的宽度。

所有跨 packet 的尾都须支付。每个完整单 packet 单独满足三矩，
故该包的 $A_g-A_f,A_{fg}$ 紧支撑。右方各 packet 在本包上给
$A_f$ 增加一个 $c x^2$ 尾，而

$$
E_0(x^2,Z)=0
\quad\text{对每个双 collar 为零的 }Z.
\tag{29}
$$

这是
$\int x^2Z''=2\int Z$ 与 $\int xZ'=-\int Z$
的完整边界计算。因此跨 packet 的这些共同尾交叉准确为零。
单 packet 内所有左补矩、常平台、空隙和四个主导数段之间的真实尾仍完整保留。

据此只需八个 packet 各两个有理能量。幅度四次使最终结果落在四个正立方根槽
$(1,\sqrt[3]7,\sqrt[3]{21},\sqrt[3]{35})$。
新消费者仍须验证每包的相同左实尾、零交叉尾和完整差的紧尾，不因预期而删除任何端常数。

若实际得到某个严格非零 raw 系数，固定支撑的足够高阶邻域
（例如 $C^4$）保持其值非零。按 R193/R183 的有限三矩修复，将 piecewise $C^7$ 输入换成 $C^\infty$ 时，(3) 精确恢复且非零值由连续性保持。只有实际完成后，才能将此条件结论应用为原八包全允许宽度的平滑排除；本文不预填实际结果。
