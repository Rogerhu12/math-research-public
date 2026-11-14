# R236 附录：已付 U 坐标与完整三生成元尾交

日期：2026-11-13 UTC。作者：Astra-ISP-0c017065 / normal_full_columns_1856；AI-assisted，GPT-6 Astra Pro。
状态：**已证明的完整实际尾交续接。** 本稿继续指定迟首正 $N_j$ 双行与已付的十五阶修正。将完整两位交换子改写为 $U$ 的有限自由模，使用一个实际 Neumann 单位。已知 $U-u_*$ 的前向源足够给完整下一尾交的三个生成元和正常余式；不必倒转前稿中可能昂贵的某个 H 源系数。本稿不把三个生成元缩成廉价的两个，也不声称全层一致度量。

## 1. 固定输入与原双源

使用[保留第二生成元的一次额外尾提升](R236-appendix-next-k-lagrange-correction-and-paid-original-normal-anchor.md)的同一固定起点 n，
令 $x=n+1$、$m=n+1$、$l=n+2$，原 $S,Z$、$U,V,H,K$ 和实际 $u_*$ 均取该稿原定义。
特别
$$
H=V^2-\delta N_l,\qquad K=U^2+\varepsilon V,
$$
$$
U=\alpha N_l+\alpha_1N_{l+1}+p,\qquad
V=\beta N_l+\beta_1N_{l+1}+q,
\quad p,q,u_*\in\mathcal B_{l+2}.
\tag{1.1}
$$
所有 scalar 系数都是上一稿的正实数，且
$$
\alpha\ge(81x^3)^{-1},\quad \alpha_1\ge(64x^3)^{-1},
\quad \alpha,\alpha_1,\beta,\beta_1\le1,
\quad\|p\|\le1,quad\|q\|\le x.
$$
记 $s=16^n$。该稿已经给出
$$
E:=U-u_*=S\mathcal E_S+Z\mathcal E_Z,
\qquad \|\mathcal E_S\|,\|\mathcal E_Z\|\le e^{483020s},
$$
$$
E=HA_H+KA_K,quad
\|u_*\|\le M_*:=e^{104100s},\qquad\|U\|\le1.
\tag{1.2}
$$
以下把这些已付源直接保留。原完整当前理想为
$$
\mathcal I=H\mathcal C_l+K\mathcal C_l,\qquad
\mathcal B=\mathcal C_{l+2}.
$$
$\mathcal C_j$ 是原完整尾交换子；其两位模分解、实际压缩和正常性都按原模型使用。

## 2. 一个完整两位的实际有限坐标变换

设
$$
N=N_l,\qquad M=N_{l+1},\qquad T_*=N_{l+2},
\quad N^2=\eta_lM,\qquad N^4=r,
$$
$$
r=\eta_l^2\eta_{l+1}T_*\in\mathcal B,\qquad
b_h=\alpha_1/\eta_l,\qquad Z_U=U-p=\alpha N+b_hN^2.
$$
定义实际尾单位
$$
\boxed{Q=\alpha^4I+4b_h^4r.}
\tag{2.1}
$$
小参数准确为
$$
\frac{4b_h^4\|r\|}{\alpha^4}
=\frac{4\alpha_1^4}{\alpha^4}
\frac{\eta_{l+1}}{\eta_l^2}.
$$
由精确 carry，
$$
u_{n+3}-2u_{n+2}\ge4695040s,\qquad
u_j=-\log\eta_j,
$$
而 $4\alpha^{-4}\le4\cdot81^4x^{12}$，故
$$
\boxed{
\|\alpha^{-4}4b_h^4r\|\le e^{-4695009s}<1/2,
\qquad\|Q^{-1}\|\le2\alpha^{-4}.
}
\tag{2.2}
$$
这个逆在原尾范数中由 Neumann 级数支付。

直接乘法给 N 的三次坐标式
$$
\boxed{
N=c_0+c_1Z_U+c_2Z_U^2+c_3Z_U^3,
}
\tag{2.3}
$$
其中
$$
c_0=-5\alpha b_h^3rQ^{-1},quad
c_1=(\alpha^4I-2b_h^4r)\alpha^{-1}Q^{-1},
$$
$$
c_2=-\alpha b_hQ^{-1},quad
c_3=2b_h^2\alpha^{-1}Q^{-1}.
\tag{2.4}
$$
例如在 $I,N,N^2,N^3$ 中展开 $Z_U,Z_U^2,Z_U^3$，三乘三非恒定块行列式恰为
$$
\alpha^2Q.
$$
解该有限线性系统即为 (2.3)–(2.4)。无需对 N 或其像作任何有界除法。

另外
$$
M=(Z_U-\alpha N)/\alpha_1,
$$
$$
NM=[Z_U^2-\alpha^2\eta_lM-\alpha_1^2\eta_{l+1}T_*]/(2\alpha\alpha_1).
\tag{2.5}
$$
原完整两位分解
$$
\mathcal C_l=\mathcal B\oplus N\mathcal B\oplus M\mathcal B\oplus NM\mathcal B
$$
因此等价于有限自由模分解
$$
\boxed{\mathcal C_l=\mathcal B\oplus U\mathcal B\oplus U^2\mathcal B\oplus U^3\mathcal B.}
\tag{2.6}
$$
基变换的逆由 (2.3)–(2.5) 明列，正向变换来自 (1.1)；行列式单位保证唯一性。
所有系数提取均为物理块压缩、固定尾乘法与固定单位逆的有限复合，故正常。

## 3. 单首四次关系与三个指定尾生成元

以下 z 是与尾系数交换的多项式不定元，写 $\zeta=z-p$。
$U$ 的准确单首关系是
$$
\boxed{
F(z)=\zeta^4-2b_h^2r\zeta^2-4\alpha^2b_hr\zeta
+b_h^4r^2-\alpha^4r,\qquad F(U)=0.
}
\tag{3.1}
$$
核验只需 $N^4=r$：展开 $Z_U^4$ 后相减
$2b_h^2rZ_U^2+4\alpha^2b_hrZ_U$，剩下 $\alpha^4r-b_h^4r^2$。
特别 F 单首且所有系数在真实 $\mathcal B$ 中。

令 $\mathfrak n(z)$ 为 (2.3) 右侧把 $Z_U$ 换成 $z-p$ 的多项式，并定义
$$
\mathfrak m(z)=\frac{z-p-\alpha\mathfrak n(z)}{\alpha_1},
\qquad
\mathfrak v(z)=\beta\mathfrak n(z)+\beta_1\mathfrak m(z)+q,
$$
$$
h(z)=\mathfrak v(z)^2-\delta\mathfrak n(z),\qquad
k(z)=z^2+\varepsilon\mathfrak v(z).
\tag{3.2}
$$
准确有 $\mathfrak n(U)=N$、$\mathfrak m(U)=M$、$\mathfrak v(U)=V$，
所以 $h(U)=H$、$k(U)=K$。

三个指定实际远尾生成元为
$$
\boxed{h_*=h(u_*),\qquad k_*=k(u_*),\qquad f_*=F(u_*).}
\tag{3.3}
$$
其真实原来源可直接写出。
对任意多项式 g 记 $g^{[1]}(z,w)$ 为多项式差商。
由 (1.2)，
$$
\boxed{
h_*=H-Eh^{[1]}(U,u_*),quad
k_*=K-Ek^{[1]}(U,u_*),quad
f_*=-EF^{[1]}(U,u_*).
}
\tag{3.4}
$$
再代入原 H,K 与 E 的 S,Z 源即可。
每个差商都是有限多项式；没有对其中任何一项再求逆。

## 4. 完整尾交、范数闭包及超弱闭包

按 (2.6) 唯一写
$$
X=\sum_{i=0}^3U^ix_i,\qquad x_i\in\mathcal B,
$$
定义有界正常余式
$$
\boxed{\mathfrak r_*(X)=\sum_{i=0}^3u_*^ix_i\in\mathcal B.}
\tag{4.1}
$$
它在 $\mathcal B$ 上为恒等。
准确有限差商给
$$
X-\mathfrak r_*(X)
=(U-u_*)\sum_{i=1}^3\sum_{r=0}^{i-1}U^ru_*^{i-1-r}x_i
\in\mathcal I.
\tag{4.2}
$$

**定理。** 令
$$
\mathcal J=h_*\mathcal B+k_*\mathcal B+f_*\mathcal B.
$$
则
$$
\boxed{
\mathcal I\cap\mathcal B=\mathcal J,
\qquad\mathcal I=\mathfrak r_*^{-1}(\mathcal J).
}
\tag{4.3}
$$
并准确有
$$
\boxed{
\overline{\mathcal I}^{\|\cdot\|}
=\mathfrak r_*^{-1}(\overline{\mathcal J}^{\|\cdot\|}),
\qquad
\overline{\mathcal I}^{uw}
=\mathfrak r_*^{-1}(\overline{\mathcal J}^{uw}).
}
\tag{4.4}
$$

证明：由 (3.4)，$\mathcal J\subseteq\mathcal I\cap\mathcal B$。
若 $X=HA+KB$，将 A,B 写成 U 基的三次多项式。
乘积 $h(z)A(z)+k(z)B(z)$ 按单首 F 作有限多项式除法，得到余式 L(z)，次数小于4。
实际 X=L(U)，所以
$$
\mathfrak r_*(X)
=h_*A(u_*)+k_*B(u_*)-f_*Q_0(u_*)\in\mathcal J,
$$
其中 $Q_0$ 是此次有限多项式商。
若 X 本身属于尾 B，则 $X=\mathfrak r_*(X)$，给反包含。
结合 (4.2) 即得完整 (4.3)。

对闭包，连续性/正常性给一个包含；反向取 $\mathcal J$ 中趋于
$\mathfrak r_*(X)$ 的网，再加上固定的 $X-\mathfrak r_*(X)\in\mathcal I$ 即得。
这一步既没有交换交与闭包，也没有暗设原逼近网或原源的一致范数。
证毕。

因原前两次尾交已完整给 $(S,Z)\cap\mathcal C_l=(H,K)$，(4.3)–(4.4)
就是该同一个原双行理想在 $\mathcal C_{l+2}$ 的完整尾交。
这里是三个显式生成元，没有用未付的 H 源逆把它们缩成两个。

## 5. 付清坐标、余式和原源的粗预算

以下用多项式的尾系数范数和作为 $\|\cdot\|_{\rm coef}$。
(2.2)–(2.4) 给（常数仅为方便的上界）
$$
\|\mathfrak n\|_{\rm coef}\le10^{12}x^{15}\eta_l^{-2},
\qquad
\|\mathfrak m\|_{\rm coef}\le10^{15}x^{18}\eta_l^{-2},
$$
$$
\|\mathfrak v\|_{\rm coef}\le D_0:=10^{16}x^{18}\eta_l^{-2}.
\tag{5.1}
$$
例如 c1 范数至多 $3/\alpha$，c2 至多 $2\alpha^{-3}/\eta_l$，
c3 至多 $4\alpha^{-5}/\eta_l^2$；c0 也由 (2.4) 直接控制。
把 $z-p$ 展开至多乘8，便得前两界。
(2.5) 的 NM 坐标也有三次尾系数和至多 $10^{19}x^{24}\eta_l^{-2}$。
因此可用统一基变换常数
$$
C_0=10^{20}x^{24}\eta_l^{-2}.
$$
原物理两位每个块系数范数不超过 $\|X\|$，故
$$
\boxed{\|\mathfrak r_*X\|\le4C_0(1+M_*)^3\|X\|,}
$$
$$
\boxed{
\left\|\sum_{i=1}^3\sum_{r=0}^{i-1}U^ru_*^{i-1-r}x_i\right\|
\le12C_0(1+M_*)^2\|X\|.
}
\tag{5.2}
$$
这两式分别支付全部完整交换子的余式度量与 (4.2) 的源乘因子；不局限于原范数代数右测试。

由 (3.1) 的实际微小系数可取
$$
\|F\|_{\rm coef}\le32,
\quad\|h\|_{\rm coef}\le2D_0^2,
\quad\|k\|_{\rm coef}\le2D_0.
$$
次数依次为4、至多6、至多3。
因此 (3.3) 及 (3.4) 的所有目标和原源已有明确有限乘积上界。
为显示费用仍在原 carry 尺度内，用 $u_l\le358400s$、$\log x\le s$ 可取
$$
\boxed{
\|\mathfrak r_*\|\le e^{1040000s},
\qquad \max\{\|h_*\|,\|k_*\|,\|f_*\|\}\le e^{2060000s}.
}
\tag{5.3}
$$
对每个 $g_*=h_*,k_*,f_*$，由 (3.4) 可明确取
$$
g_*=S\mathcal U_g+Z\mathcal V_g,\qquad
\boxed{\|\mathcal U_g\|,\|\mathcal V_g\|\le e^{2500000s}.}
\tag{5.4}
$$
例如最大差商费用来自 h：
$6\|h\|_{\rm coef}(1+M_*)^5$，再乘 (1.2) 的 $e^{483020s}$；
其指数小于 $2440000s$，所以 (5.4) 留有余量。
有限单首多项式除法也有明确预算：次数至多9，最多6次递推，
多项式商的尾系数和至多输入系数和乘 $33^6$，再在 $u_*$ 求值至多乘 $(1+M_*)^5$。
没有引入新的算子逆。

反向原来源可以直接写为一个可用不等式。
若给定 $X\in\mathcal C_l$ 及实际尾表示
$$
\mathfrak r_*(X)=h_*b_1+k_*b_2+f_*b_3,
$$
则把 (4.2) 的明确因子乘 (1.2) 的原源，再加 (3.4) 的三个原源，得到
$$
X=S\mathcal U_X+Z\mathcal V_X,
$$
$$
\boxed{
\|\mathcal U_X\|,\|\mathcal V_X\|
\le e^{1410000s}\|X\|
+e^{2500000s}(\|b_1\|+\|b_2\|+\|b_3\|).
}
\tag{5.5}
$$
第一项就是 $e^{483020s}\,12C_0(1+M_*)^2\|X\|$ 的保守上界。
(5.5) 没有声称每个尾元素自动存在统一小范数的三源分解；它支付的是所给实际分解的全部返回费用。

## 6. 正常见证与后继问题的准确位置

若原同一个正正常 $\rho$ 湮灭 $S\mathcal A'+Z\mathcal A'$，
则 (3.4)、(5.4) 保证同一实际部分迹湮灭三个尾生成元的全部完整右倍数。
(4.4) 同时覆盖完整正常尾理想。
没有在经过余式后把 $\rho$ 换为另一个态，也没有声称余式是正映射。

前稿的 $P_*=N_{l+1}+R_*$ 及条件锚 $\Theta_*$ 保持原准确身份和已付费用。
本稿补上的是它之后完整 $\mathcal C_{l+2}$ 尾交的实际三生成元描述，
从而继续研究完整尾理想时无需等待一个未知的两生成元反向单位。

三个新尾元素一般不是原来的两条纯线性行；没有据此取得全层统一费用或不消失的统一正常锚。
继续从它们的实际系数中构造下一廉价正规化行，仍是原问题。
